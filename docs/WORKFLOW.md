# Team workflow

## People and confirmed contributions
- Hogyun: requested the clean restart and repository setup; previous discussions assigned local experimentation to Hogyun.
- Naura: supplied the research proposal and candidate data package.
- Specific responsibilities after the latest meeting have not been supplied. Record actual agreements here; do not invent authorship/contributions.
- Naura's GitHub username and invitation permissions are pending. Private repository access is not automatic from having this URL.

## Small shared milestones
| Milestone | Deliverable | Owner | Review |
|---|---|---|---|
| Scope | One-page agreed question + first experiment | To agree | Both |
| Data | Group split, guideline and human review plan | To agree | Both |
| Environment | Rules, hand calculations and tests | To agree | Other member |
| Language | Frames, generator/parser pilot and failure examples | To agree | Both |
| Experiments | Frozen matrix, run manifests and complete logs | To agree | Other member |
| Paper | Actual results, limitations and reproducibility | To agree | Both |

## Git use
- `main`: reviewed, coherent work.
- Short branches such as `data/source-audit`, `feat/text-channel`, `docs/protocol`.
- Keep changes small; use a pull request when one person's changes affect the other's interfaces or evaluation rules.
- Before a commit: `git status --short`, `git diff --check`, offline tests, and inspect the exact staged diff.
- Avoid `git add .` when run outputs/credentials/source material may be nearby. Stage named files/directories deliberately.
- Never force-push/rewrite shared history or change repository visibility without agreement.

## Meeting note template
Date / attendees / confirmed topic / decisions / open questions / owner+next action / next check-in.
Only the topic-level decision has been reported for the current restart; no detailed meeting transcript is assumed.

## Research integrity and collaboration
Annotate independently before adjudication. Do not claim completed human agreement or independent reproduction until it happened. Include failed runs and negative findings. Record AI assistance in drafting/coding/annotation according to the selected venue's current policy.
