"""Single-request OpenRouter runner (Python standard library only).

Inputs: JSON config, JSON role/content messages, nonnegative sample index.
Outputs: dry-run request summary, or an exclusive artifact directory with request,
response, provenance hashes and status. No automatic retries or batch execution.
Side effects: --execute reads OR_KEY and makes one paid HTTPS POST; metadata GET
preflight is public. Existing requests are replayed, never silently regenerated.
Errors: unsupported metadata, wrong tier, truncated/invalid JSON, missing key and
ambiguous network failure stop execution. Tests: python -B -m unittest discover -s tests.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import sys
from datetime import datetime, timezone
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
CHAT_URL = "https://openrouter.ai/api/v1/chat/completions"
META_URL = "https://openrouter.ai/api/v1/models/openai/gpt-5.6-luna/endpoints"


def canonical(value):
    """Stable UTF-8 serialization for content hashes; no side effects."""
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def save_new(path, value):
    """Write once; refuse overwrites, including interrupted experiments."""
    with Path(path).open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)


def read_key(config):
    """Environment first, then only the named entry in the specified .env.

    Supports KEY=value and quoted values; no interpolation or shell evaluation.
    Never returns any other entries or includes credential values in errors.
    """
    name = config["api_key_env"]
    if os.environ.get(name, "").strip():
        return os.environ[name].strip()
    path = (ROOT / config["api_key_file"]).resolve()
    if not path.is_file():
        raise ValueError("API credential missing; configure the named environment variable.")
    values = []
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        entry, sep, value = line.strip().removeprefix("export ").partition("=")
        if sep and entry.strip() == name:
            value = value.strip()
            if len(value) >= 2 and value[0] in "\"'" and value[-1] == value[0]:
                value = value[1:-1]
            else:
                value = value.split(" #", 1)[0].strip()
            values.append(value)
    if len(values) != 1 or not values[0] or "\n" in values[0] or "\r" in values[0]:
        raise ValueError("Expected exactly one nonempty API credential entry.")
    return values[0]


def build_request(config, messages, sample_index):
    """Create a fully specified request; sample index fixes the generation seed."""
    if config["endpoint_url"] != CHAT_URL or config["metadata_url"] != META_URL:
        raise ValueError("Unexpected API URL; credentials must only go to OpenRouter.")
    if sample_index < 0:
        raise ValueError("sample_index must be nonnegative.")
    if not isinstance(messages, list) or not messages:
        raise ValueError("messages must be a nonempty list.")
    for message in messages:
        if set(message) != {"role", "content"} or message["role"] not in {"system", "user", "assistant"}:
            raise ValueError("Only role/content text messages are allowed.")
        if not isinstance(message["content"], str) or not message["content"].strip():
            raise ValueError("Empty or non-text message.")
    if len(canonical(messages)) > 24000:
        raise ValueError("Prompt exceeds this single-request pilot's 24KB limit.")
    request = json.loads(json.dumps(config["request"]))
    request["messages"] = messages
    request["seed"] = config["generation_seed_base"] + sample_index
    if config["automatic_retries"] != 0:
        raise ValueError("This pilot runner does not retry potentially billed requests.")
    provider = request["provider"]
    if (request["model"] != "openai/gpt-5.6-luna" or request["service_tier"] != "flex"
            or provider["only"] != ["openai/flex"] or provider["order"] != ["openai/flex"]
            or provider["allow_fallbacks"] is not False or provider["require_parameters"] is not True
            or request["stream"] is not False or not 1 <= request["max_tokens"] <= 512):
        raise ValueError("Strict model/tier/routing or pilot token limits were changed.")
    if not 0 <= request["seed"] < 2**31:
        raise ValueError("Seed exceeds the experiment's signed 32-bit range.")
    return request


def check_metadata(metadata, request):
    """Fail closed against the selected endpoint's advertised capabilities/prices."""
    entries = [e for e in metadata["data"]["endpoints"] if e.get("tag") == "openai/flex"]
    if metadata["data"]["id"] != request["model"] or len(entries) != 1:
        raise ValueError("Expected model/Flex endpoint missing.")
    entry = entries[0]
    controls = {"model", "messages", "provider", "stream", "service_tier", "prompt_cache_options"}
    required = set(request) - controls
    if request["response_format"]["type"] == "json_schema":
        required.add("structured_outputs")
    unsupported = required - set(entry["supported_parameters"])
    if unsupported:
        raise ValueError("Unsupported request parameters: " + ", ".join(sorted(unsupported)))
    for name in ("prompt", "completion"):
        if float(entry["pricing"][name]) * 1e6 > request["provider"]["max_price"][name] + 1e-12:
            raise ValueError("Endpoint price exceeds the configured per-million-token ceiling.")
    return entry


def validate_response(response):
    """Reject wrong routing, incomplete output and schema violations, retaining raw evidence."""
    if response.get("error") or response.get("service_tier") != "flex":
        raise ValueError("Response failed or did not confirm Flex; do not use this sample.")
    if response.get("provider") != "OpenAI":
        raise ValueError("Response did not confirm the intended OpenAI provider.")
    if response.get("model") not in {"openai/gpt-5.6-luna", "openai/gpt-5.6-luna-20260709"}:
        raise ValueError("Response model mismatch; inspect before using this sample.")
    choices = response.get("choices", [])
    if len(choices) != 1 or choices[0].get("finish_reason") != "stop":
        raise ValueError("Missing, refused or truncated completion.")
    parsed = json.loads(choices[0]["message"]["content"])
    if (not isinstance(parsed, dict) or set(parsed) != {"utterance"}
            or not isinstance(parsed["utterance"], str) or not parsed["utterance"].strip()):
        raise ValueError("Completion does not match the utterance schema.")
    return parsed


def execute_one(config, request, destination):
    """One paid request, or offline replay if already saved. No silent retries."""
    if destination.exists():
        record = load_json(destination / "response.json")
        saved = load_json(destination / "request.json")
        receipt = load_json(destination / "receipt.json")
        if digest(saved) != digest(request) or digest(record) != receipt["response_sha256"]:
            raise ValueError("Artifact checksum mismatch.")
        validate_response(record)
        return "replayed", record
    key = read_key(config)
    with urlopen(Request(META_URL, headers={"User-Agent": "EMNLP-TrackC/1.0"}), timeout=30) as result:
        metadata = json.load(result)
    check_metadata(metadata, request)
    destination.mkdir(parents=True, exist_ok=False)
    save_new(destination / "request.json", request)
    save_new(destination / "config.json", config)
    save_new(destination / "endpoint_metadata.json", metadata)
    save_new(destination / "manifest.json", {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "request_sha256": digest(request), "config_sha256": digest(config),
        "metadata_sha256": digest(metadata), "python": sys.version,
        "platform": platform.platform(), "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "network_attempts": 1, "status": "attempt_reserved_not_yet_confirmed"
    })
    http_request = Request(CHAT_URL, data=canonical(request), method="POST", headers={
        "Content-Type": "application/json", "Authorization": "Bearer " + key
    })
    try:
        with urlopen(http_request, timeout=config["timeout_seconds"]) as result:
            raw = result.read().decode("utf-8")
        # Do not log headers or HTTP exception bodies; redact any accidental key echo.
        raw = raw.replace(key, "[REDACTED]")
        with (destination / "response.raw.txt").open("x", encoding="utf-8") as handle:
            handle.write(raw)
        response = json.loads(raw)
        save_new(destination / "response.json", response)
        validate_response(response)
        save_new(destination / "receipt.json", {
            "response_sha256": digest(response), "raw_sha256": hashlib.sha256(raw.encode()).hexdigest(),
            "finished_at_utc": datetime.now(timezone.utc).isoformat(), "status": "validated",
            "usage": response.get("usage"), "system_fingerprint": response.get("system_fingerprint")
        })
        return "generated", response
    except Exception as error:
        save_new(destination / "failure.json", {"error_type": type(error).__name__,
            "status": "failed_or_unconfirmed_do_not_retry_automatically"})
        raise RuntimeError("Request failed/unconfirmed; saved evidence needs review before any retry.") from None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=ROOT / "configs/openrouter_luna_flex.json")
    parser.add_argument("--messages", type=Path, default=ROOT / "prompts/smoke_messages.json")
    parser.add_argument("--sample-index", type=int, default=0)
    parser.add_argument("--execute", action="store_true", help="Authorize ONE paid generation, not a batch.")
    args = parser.parse_args()
    config = load_json(args.config)
    request = build_request(config, load_json(args.messages), args.sample_index)
    snapshot = load_json(ROOT / config["metadata_snapshot"])
    check_metadata(snapshot["response"], request)
    request_hash = digest(request)
    if not args.execute:
        print(json.dumps({"mode": "dry-run", "request_sha256": request_hash, "request": request}, indent=2))
        return
    mode, response = execute_one(config, request, ROOT / "artifacts/openrouter" / request_hash)
    print(json.dumps({"mode": mode, "request_sha256": request_hash,
                      "response_id": response.get("id"), "usage": response.get("usage")}, indent=2))


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        # No error-body/credential dump or traceback from requests.
        print("Stopped safely (" + type(error).__name__ + "). Review config/artifact status; no automatic retry.", file=sys.stderr)
        sys.exit(1)
