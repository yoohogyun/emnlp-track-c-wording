# Implementation and experiments

Status: **planned; no fresh study experiments run**. This retains Naura's experiment structure while leaving final scope, settings and budget to a recorded protocol decision.

## Module boundaries (to implement)
| Module | Inputs | Outputs / side effects | Checks |
|---|---|---|---|
| Data preparation | Approved source files, grouping rules | Provenance and split manifests | Document/event overlap, duplicates, usage rights |
| Frames and generator | Explicit semantic content, style, exemplar IDs, model config, seed | New message bank; API cost/logs | Numbers/conditions fully specified; failures retained |
| Parser | Text and legitimate recipient context ONLY | Interpreted fields or explicit unknown | Human real-text test; negation, roles, numeric/condition tests |
| Language channel | Frame ID, frozen bank version, random condition | Actual text and recipient-visible interpretation | Never substitute the source frame after a parse failure |
| Environment | Scenario, action realization, fixed B rules | Observation/reward/termination/trajectory | Hidden-type boundary, bilateral acceptance, reward accounting |
| Policies | Public observation/history | Action; trained checkpoints for learned policies | Shared information/budgets; chosen-step reward only for Bandit |
| Evaluation/analysis | Frozen policy, scenario list, message split | Metrics, transitions, cases, tables | No learning on test; reconstruct every reported number |

## Stage gates
### G0 — Protocol and task definition
Agree on the negotiation object, action inventory, episode budget, opponent-response rules, information boundary, actual/perceived acceptance and reward timing. Inspect at least 10 hand-traced episodes. Include positive and negative information-value controls. Source examples must motivate utterance functions, not invented historical payoffs.

### G1 — Independent language pilot
Pilot generator and parser before RL scale-up. Supply complete semantic content (not only `condition=true` or opaque type labels). Check equivalent wording, role reversal, negation, commitment strength and explicit reciprocal conditions. Report malformed and duplicate generations. Do not optimize prompts against final test cases.

### G2 — Freeze splits, interpretations and costs
Group source documents before processing; group identical/similar generated text before splitting. Freeze semantic frames, parser/generator versions, response-failure rules, seed list, model selection, metric denominators and expected budget. No fresh study model should import earlier workspace checkpoints.

### G3 — Run controlled experiments
Compare policy under shared modules first, then change language channel or information assumptions independently. Separate frozen-policy evaluation from retraining under a changed channel. Retain failures and all seeds.

### G4 — Explain and reproduce
Reaggregate saved trajectories, evaluate saved models, distinguish full retraining. Analyze >=6 actual episodes and review >=20 turns. A second team member performs the documented reproduction. Write only measured claims.

## Naura proposal matrix
| ID | Main change / purpose | Status |
|---|---|---|
| V | Interface, hidden information, accounting, termination/acceptance validation | Planned |
| T1 | Edit numbers/conditions/costs in actual text and verify transitions | Planned |
| E0 | Template control; Random/strong Heuristic/Bandit/PPO | Planned |
| E1 | Offer-response uncertainty × outside option; establish when information can help | Planned |
| E2 | Precisely specified belief/response masking | Planned |
| E3 | Backchannel reliability variation | Planned |
| E4 | Signal-effect variation (different from information acquisition) | Planned |
| E5 | Agreement feasibility / rational withdrawal | Planned |
| E6a | One-way wording, A→B | Planned |
| E6b | Two-way wording, including B→A; template/plain/diplomatic/hedged | Planned |
| E7 | Discount, entropy and a major reward-component sweep | Planned |
| E8 | Naive vs language-channel-aware belief updates | Planned |

**First milestone:** V + T1 + a template environment + a small two-way language pilot. The first full-run scope is not yet approved/frozen; do not silently run the entire matrix.

## Course baseline versus extensions
Course baseline: Random/Heuristic/immediate-reward Bandit/PPO; base Bandit and PPO >=3 training seeds; discount/entropy/reward tests; actual-text trajectory analysis and reproducibility. Some masking/planner/retraining combinations in Naura's matrix are research extensions, not a reason to substitute away the required comparisons.

## Metrics
- Task: agreement, both utilities, cost-adjusted undiscounted return, breakdown, turns, escalation, reversals, acceptance violations.
- Language: per-field/full-frame fidelity, numeric error, missing condition, added commitment, answer flip/erasure, parse failure. Report human-label accuracy separately from frame-round-trip consistency.
- Information: calibrated response likelihoods, belief quality and utility benefit of querying, with information from offer responses also counted.
- Statistics: independent case/document groups distinct from stochastic repetitions and training seeds. Paired conditions where feasible; training-seed sample SD separate from case bootstrap. Main/test selection and additional exploratory runs explicitly labelled.

## Before a run is approved
Record question, data/split hashes, source/synthetic counts, configuration, policy/generator/parser versions, seeds, maximum cost/steps, positive/negative controls, failure rules, model-selection rule, and analysis command in a run manifest. Test data cannot be used to silently revise that manifest.
