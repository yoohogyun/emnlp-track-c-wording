"""Offline contract tests. No network, real credentials or paid calls."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("runner", ROOT / "scripts/openrouter_request.py")
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class RunnerTests(unittest.TestCase):
    def setUp(self):
        self.config = runner.load_json(ROOT / "configs/openrouter_luna_flex.json")
        self.messages = runner.load_json(ROOT / "prompts/smoke_messages.json")
        self.metadata = runner.load_json(ROOT / "docs/openrouter_endpoints.snapshot.json")["response"]
        self.response = {"model": "openai/gpt-5.6-luna", "provider": "OpenAI", "service_tier": "flex",
                         "choices": [{"finish_reason": "stop", "message": {
                             "content": '{"utterance":"We offer 0.4 if you de-escalate."}'}}]}

    def test_stable_request_and_explicit_seed(self):
        a = runner.build_request(self.config, self.messages, 0)
        b = runner.build_request(self.config, self.messages, 0)
        self.assertEqual(runner.digest(a), runner.digest(b))
        self.assertNotEqual(runner.digest(a), runner.digest(runner.build_request(self.config, self.messages, 1)))
        runner.check_metadata(self.metadata, a)
        self.assertNotIn("temperature", a)

    def test_reject_unknown_parameter(self):
        request = runner.build_request(self.config, self.messages, 0)
        request["temperature"] = 0
        with self.assertRaises(ValueError):
            runner.check_metadata(self.metadata, request)

    def test_reject_routing_fallback(self):
        self.config["request"]["provider"]["allow_fallbacks"] = True
        with self.assertRaises(ValueError):
            runner.build_request(self.config, self.messages, 0)

    def test_price_ceiling(self):
        request = runner.build_request(self.config, self.messages, 0)
        request["provider"]["max_price"]["prompt"] = 0
        with self.assertRaises(ValueError):
            runner.check_metadata(self.metadata, request)

    def test_response_checks(self):
        self.assertIn("utterance", runner.validate_response(self.response))
        for field, wrong in [("service_tier", "default"), ("model", "other"), ("provider", "Azure")]:
            response = dict(self.response, **{field: wrong})
            with self.assertRaises(ValueError):
                runner.validate_response(response)
        response = copy.deepcopy(self.response)
        response["choices"][0]["finish_reason"] = "length"
        with self.assertRaises(ValueError):
            runner.validate_response(response)

    def test_environment_key_takes_precedence(self):
        with patch.dict(runner.os.environ, {"OR_KEY": "FAKE_TEST_CREDENTIAL"}):
            with patch.object(Path, "read_text", side_effect=AssertionError("Should not read a file")):
                self.assertEqual(runner.read_key(self.config), "FAKE_TEST_CREDENTIAL")

    def test_dotenv_only_named_key_and_bom(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / ".env"
            path.write_text('OTHER=ignore\nOR_KEY="FAKE_TEST_CREDENTIAL"\n', encoding="utf-8-sig")
            config = dict(self.config, api_key_file=str(path))
            with patch.dict(runner.os.environ, {}, clear=True):
                self.assertEqual(runner.read_key(config), "FAKE_TEST_CREDENTIAL")

    def test_read_only_replay(self):
        request = runner.build_request(self.config, self.messages, 0)
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            runner.save_new(target / "request.json", request)
            runner.save_new(target / "response.json", self.response)
            runner.save_new(target / "receipt.json", {"response_sha256": runner.digest(self.response)})
            with patch.object(runner, "urlopen", side_effect=AssertionError("Network forbidden")):
                mode, _ = runner.execute_one(self.config, request, target)
            self.assertEqual(mode, "replayed")

    def test_pending_request_does_not_retry(self):
        request = runner.build_request(self.config, self.messages, 0)
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(runner, "urlopen", side_effect=AssertionError("Network forbidden")):
                with self.assertRaises(FileNotFoundError):
                    runner.execute_one(self.config, request, Path(directory))

    def test_no_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "record.json"
            runner.save_new(path, {"original": True})
            with self.assertRaises(FileExistsError):
                runner.save_new(path, {"original": False})
            self.assertTrue(json.loads(path.read_text())["original"])


if __name__ == "__main__":
    unittest.main()
