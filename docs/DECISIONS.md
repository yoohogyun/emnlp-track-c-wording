# Decision log

## Confirmed by Hogyun
- **D001 — Fresh start:** After meeting Naura, restart from her original proposal. Preserve old work separately; do not continue its models/results as this study.
- **D002 — Research direction:** Two-way LLM wording between party A's policy and fixed-rule party B; measure preservation of information/conditions/commitments and consequences for negotiation.
- **D003 — Destination:** Actual COLING short-paper submission is the goal. Classroom checklist completion alone does not establish conference readiness.
- **D004 — Repository:** New PRIVATE GitHub repository, working name `emnlp-track-c-wording`. Do not publish the old workspace or credentials.
- **D005 — Practical base:** Existing approved generator infrastructure is OpenRouter GPT-5.6 Luna / OpenAI Flex. `OR_KEY` remains local. This setup phase makes no paid calls.

## Not yet decided / not inferred from the meeting
- Exact first full experiment, scenario families, sample sizes, training budgets and primary metric.
- Which styles are in the first milestone versus later breadth.
- Rules for noisy acceptance, costs and the relationship between actual and perceived acceptance.
- Parser architecture and independent validation. Original proposal suggests another model family; current approval is Luna-only. Do not silently add a provider/model or call a correlated generator/parser agreement independent evidence.
- Complete language-channel confusion matrix and treatment of type-dependent unclear answers.
- Final team task ownership, updated dates, verified Naura GitHub username and collaboration permissions.
- Dependency/environment choice, licensing and final anonymous submission packaging.

## Changes that must be recorded
For any change, add: decision ID/date, proposer/reviewer, rationale, affected files/experiments, whether test results were already inspected, and whether earlier data are now exploratory. Do not overwrite the decision history to make it look as though an outcome-driven choice was made in advance.

## Known carry-over cautions (not new study results)
- Keep semantic input complete and distinguish intended meaning from interpreted meaning.
- Do not validate a parser solely against model-produced labels.
- Freeze/test language and scenario splits at the correct group level.
- Same API seed is not a guarantee of identical fresh completions; replay saved responses.
- Count earlier API charges against any cumulative user budget; fresh Git history does not create a fresh spending authorization.
