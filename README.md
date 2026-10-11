# Does Backchannel Information Survive LLM Wording?

**Hogyun & Naura · EMNLP Track C · Fresh research repository · Intended COLING short paper**

Private GitHub: https://github.com/yoohogyun/emnlp-track-c-wording

This project restarts from **Naura's research proposal**. We study whether the value of information-seeking and conditional offers survives when a language model expresses negotiation messages and each recipient responds to the meaning recovered from the text.

> 한국어 요약: 협상 행동을 고르는 정책과 말을 표현하는 LLM을 분리하고, LLM을 거친 질문·답변·조건·약속이 제대로 전달되는지, 그리고 그 차이가 협상 결과에 영향을 주는지 연구한다.

## Core architecture
```text
Party A's policy chooses an intended semantic frame
  -> LLM spokesperson produces A's utterance
  -> parser recovers what B understood
  -> fixed-rule party B responds using its private type
  -> LLM spokesperson produces B's reply
  -> parser recovers what A understood
  -> A updates its public belief and chooses the next action
```

**The LLM is the language channel, not the main learned negotiator.** Compare Random, Heuristic, immediate-reward Bandit and PPO under shared execution modules. Templates are a controlled language baseline.

## Fresh-start boundary
- Old local experiments remain in the separate `MIDTERM/track_c/` folder. They are not part of this repository's evidence.
- No previous simulator rules, trained models, message bank, test split or results have been imported.
- Only basic OpenRouter transport, offline checks, an example request and security/reproducibility practices are retained.
- There are **no new study results yet**. The repository is a planning and infrastructure starting point.
- The original title's claim that wording "erodes" information value is a hypothesis to test, not a result we assume.

## Start here
1. [Research proposal](docs/PROPOSAL.md)
2. [Implementation and experiment plan](docs/EXPERIMENTS.md)
3. [Data and annotation plan](docs/DATA.md)
4. [Decisions and unresolved choices](docs/DECISIONS.md)
5. [Team workflow](docs/WORKFLOW.md)
6. [Current progress / handoff](PLAN.md)

## Repository layout
| Path | Purpose |
|---|---|
| `docs/` | Research design, sources, decisions and collaboration |
| `configs/` | Explicit non-secret settings; current config is an API smoke example, not a frozen experiment |
| `prompts/` | Versioned prompts; currently one synthetic infrastructure example |
| `scripts/` | Small executable entry points; currently the single-request API tool |
| `tests/` | Offline infrastructure tests with fake credentials |
| `data/` | Data-use policy; raw/local material stays ignored |
| `paper/` | Paper plan only; no fabricated abstract or results |
| `artifacts/` | Created by runs, ignored by Git; requests, responses, logs and later models |

Create implementation modules only when their protocol and interfaces are agreed; do not fill this repository with copied experimental branches.

## Quick start (no installation required for current tools)
The current tooling uses Python's standard library. No RL/model dependencies have been installed for this fresh start.

```powershell
python -B -m unittest discover -s tests -v
python -B scripts/openrouter_request.py
```

The second command is a **dry-run**: no credential access, no network, no API charge.

Credentials are supplied via the process environment variable `OR_KEY`. For Hogyun's current directory layout, the example config can fall back to `../.env`; no `.env` is included, created or modified. On another machine prefer the environment variable. See [reproducibility and security](docs/REPRODUCIBILITY.md).

## Before implementing experiments
- Confirm the minimum scope and register choices before generating the final bank or examining test outcomes.
- Audit document/scenario grouping and exact-text duplicates before splitting.
- Keep human gold labels separate from model-generated labels.
- Log intended frame, actual text, interpreted fields, state changes, both sides' utilities and itemized costs.
- Do not give downstream components the original frame or true response as a shortcut around the language channel.
- Preserve all errors and negative results; do not regenerate only the samples that support a hypothesis.

## Collaboration and privacy
Use this as a **private** research repository. Invite only verified team accounts. Do not push credentials, full raw corpora, source ZIPs or unreviewed execution traces. Raw material is distributed separately; see [source registry](docs/SOURCES.md).

The shared goal is an **actual COLING short-paper submission**. Meeting the course checklist is a baseline, not proof of conference novelty or acceptance. Paper preparation must verify the selected venue/cycle's current requirements.
