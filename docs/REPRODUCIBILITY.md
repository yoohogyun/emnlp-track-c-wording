# Reproducibility, setup and safety

## What is implemented now
Only a standard-library, single-request OpenRouter tool and its offline tests. It creates a dry-run request by default, reads the credential only with `--execute`, pins the model/provider/tier, records request/response/settings/hashes, and reuses a previously completed response. This is infrastructure, not the research pipeline.

Adapted from the earlier local tooling; no previous requests, responses, model files or measured results are copied. `docs/openrouter_endpoints.snapshot.json` is public API capability metadata retained for an offline preflight, NOT an experiment result. Its timestamp is not a claim that every option remains supported forever; execution fetches current metadata before posting.

## Credentials
- Process variable: `OR_KEY`.
- Optional fallback configured as `../.env` for Hogyun's existing folder layout; the tool reads only that named entry and never writes the file.
- For a separate clone, prefer a process environment variable. Do not send a key in chat, commit it, put it in a remote URL or log Authorization headers.
- `.env*`, private keys and local artifacts are Git-ignored, even in this private repository.

## API configuration
`configs/openrouter_luna_flex.json` is a **smoke/example config, not the final experiment**:
- model `openai/gpt-5.6-luna`, `service_tier=flex`;
- only/order `openai/flex`, fallback disabled, require_parameters=true;
- explicit seed, max_tokens, reasoning effort/context/mode/exclusion, verbosity, JSON schema, no tools;
- temperature/top_p/penalty parameters not advertised by the selected endpoint are deliberately omitted, with reasons retained in config;
- cap advertised unit prices, check actual response provider/model/tier and keep usage.cost.

Do not assume Naura's original temperature0/0.7 or local7–8B-model generation plan applies to this API. Decide and record a supported generation protocol before experiments. Different wordings are not necessarily independent just because their request seeds differ.

## Current checks
```powershell
python -B -m unittest discover -s tests -v
python -B scripts/openrouter_request.py
```
Both are offline and do not read real credentials. No new dependencies installed. The future simulator/training environment and versions are still to be chosen; do not claim this skeleton already runs PPO or passes Gymnasium checks.

## Explicit paid smoke (not executed in this setup)
```powershell
python -B scripts/openrouter_request.py --execute
```
The tool performs at most one new paid POST, checks current public metadata first, and refuses automatic retries. Existing complete request hashes replay locally; partial/unconfirmed requests stop for inspection. A timeout may already have been billed. It is not a batch budget manager.

## Before a batch is built
Respect the user's existing cumulative <$10 authorization (internal ceiling $9.50), including approximately$0.30 spent in the separate older workspace. Implement a ledger and pre-call reservations; approve run size/settings before calling. Do not silently restart spending from zero because this repo is new.

## Record with every future run
- Code commit, config hash, data/split/bank hashes.
- Python/library/model versions, hardware and external-service settings.
- Full non-secret prompt, seed, model/provider/tier, response ID/raw output, token usage/cost, failure status and fingerprint when returned.
- Distinct source documents, source sentences, synthetic frames/messages, scenario groups, training seeds and stochastic repetitions.
- A method for reaggregation, saved-model evaluation and full retraining; distinguish these three reproduction levels.

## What can go into Git
Reviewed docs/config/code/tests and small, licensed manifests. Local raw corpora, original ZIPs, runtime traces, API logs, checkpoints and temporary files stay in ignored paths. Release selected reproduction materials deliberately after a privacy/rights review; Git ignore does not mean the raw evidence should be discarded.
