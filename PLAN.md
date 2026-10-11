# PLAN — fresh start from Naura's proposal

## Confirmed goal
Hogyun and Naura agreed to restart from Naura's original idea: **Does backchannel information retain its value when negotiation messages are expressed through an LLM?** Build the Track C project toward an actual COLING short-paper submission, not only classroom completion.

The LLM is a spokesperson/channel between a learned party A and a fixed-rule opponent B. This repository is NOT a continuation of the earlier policy-comparison experiments.

## Relevant files
- `README.md`: project entry point and current status.
- `docs/PROPOSAL.md`: neutral research question and original proposal architecture.
- `docs/EXPERIMENTS.md`: proposed experiment matrix, gates, outputs and validation.
- `docs/DATA.md`: source/synthetic separation, annotation and leakage controls.
- `docs/DECISIONS.md`: confirmed decisions and unresolved technical choices.
- `docs/WORKFLOW.md`: collaboration and contribution recording.
- `docs/REPRODUCIBILITY.md`: environment, API, storage and security conventions.
- `docs/SOURCES.md`: original source material locations and source roles.
- `scripts/openrouter_request.py`, `configs/openrouter_luna_flex.json`, `tests/`: basic single-request infrastructure only.
- `data/README.md`, `paper/README.md`: future data and paper boundaries.

## Planned steps / progress
- [x] Re-read Naura's source proposal and confirm the chosen topic.
- [x] Prepare a clean, standalone project folder without old results/models.
- [x] Document research questions, module boundaries and experiment gates.
- [x] Verify basic tooling: 10 offline tests pass; dry-run succeeds, no key access or paid request.
- [x] Create new PRIVATE GitHub repository: https://github.com/yoohogyun/emnlp-track-c-wording (owner/visibility API-verified).
- [x] Review staged files, commit and push main; initial local/remote commit equality verified.
- [ ] Add Naura after receiving her verified GitHub username and invite authorization.
- [ ] Both members review the proposed scope and record actual task ownership.
- [ ] Freeze the source/document split, annotation guideline and semantic frames.
- [ ] Specify and validate a minimal text-driven environment; calculate rewards by hand.
- [ ] Pilot the generator/parser independently; resolve design questions before scale-up.
- [ ] Freeze protocol; generate NEW message bank and train/evaluate NEW policies.
- [ ] Analyze actual utterances, generate results, complete independent reproduction.
- [ ] Write/review the short paper, check the actual venue/cycle requirements and submit.

## Assumptions / constraints
- Existing `../track_c/` and original MIDTERM documents remain untouched outside this repository.
- Do not import old message banks, trained policies, scenario splits or numerical results as new evidence.
- OpenRouter GPT-5.6 Luna / OpenAI Flex is the current approved generator infrastructure. No other model or dependency installation without agreement.
- API credential name is `OR_KEY`; never commit/read aloud credentials or modify `.env` automatically. No paid experiments during repository setup.
- Earlier workspace API spending (~$0.30) belongs to the existing cumulative <$10 authorization; a fresh repository does not reset the budget. Any batch runner must reconcile spending before execution.
- No simulator, parser benchmark, human gold labels or new study results are implemented/completed here yet.
- Core loss-of-information hypotheses are not conclusions; preserve null and contrary results.

## Open questions / risks
- Exact first experiment scope, sample sizes, independent scenario families, numerical rules and model-selection criterion are not frozen.
- Original proposal suggests an independent model-family parser, whereas current approved model is Luna only: decide between human-validated rule parser, a correlated Luna-parser diagnostic, or separately approved independent model.
- Define actual opponent acceptance separately from perceived acceptance; parsing a rejection as acceptance must not create a real agreement.
- Define whether an 'unclear' response is type-independent. It is only uninformative when its likelihood supports that assumption.
- Validate whether wording loss is generated-content error or interpretation error; source-frame mismatch alone does not identify the cause.
- Human annotation and real-text parser evaluation remain outstanding, not automatically supplied by existing files.
- GitHub collaboration, research contribution and all meeting details beyond the confirmed topic still require explicit records.

## Commands / checks
From this repository root:
```powershell
python -B -m unittest discover -s tests -v
python -B scripts/openrouter_request.py
# Review before any future explicit paid smoke:
# python -B scripts/openrouter_request.py --execute
git status --short
git diff --check
```

## Final setup checklist
- [x] No credentials, raw archives, old results or personal absolute paths tracked (20 explicitly staged files reviewed).
- [x] Offline tests and dry-run pass with no key access/API charges.
- [x] main has an initial commit; remote contains that commit.
- [x] GitHub visibility verified PRIVATE through the API.
- [x] Local working tree clean after initial push; owner `yoohogyun`, private remote URL recorded.
- [x] README clearly identifies the fresh study and unimplemented work.
- [x] Fresh private GitHub clone passes the same 10 offline tests and dry-run without original workspace data or credentials file. This is an infrastructure checkout check, not independent human reproduction of research.

Setup complete: https://github.com/yoohogyun/emnlp-track-c-wording. New research implementation/experiments remain planned; no fresh-study API generation or training was run. Git commit identity was configured only in this repository using the verified account and GitHub noreply email; global Git configuration was not changed.
