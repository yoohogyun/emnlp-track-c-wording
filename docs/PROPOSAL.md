# Research proposal — fresh interpretation of Naura's idea

## Source and status
Based on Naura's supplied **Course Research Proposal — Track C**, originally titled *Under Careful Consideration: How LLM Wording Erodes the Value of Backchannel Information in a Bargaining Simulator*. Hogyun confirmed after their meeting that this is the agreed direction for the fresh start.

This is a working research summary, not the original document or a final preregistration. Additional meeting decisions are unknown and are not invented here. Numeric settings, implementation and conclusions remain open until documented.

Neutral working title: **Does Backchannel Information Survive LLM Wording?**

## One-sentence idea
Test whether linguistic realization preserves the information and commitments selected by a negotiation policy, and whether interpretation errors change beliefs, costs and agreement quality.

## What stays fixed / what changes
| Component | Role |
|---|---|
| Party A | One learned/fixed high-level policy, compared across Random/Heuristic/Bandit/PPO |
| Party B | Fixed response rules with hidden acceptance conditions/type |
| Limited resources | Negotiation turns and explicitly declared question/signal/commitment costs |
| Utterance generator | Frozen LLM spokesperson, not a competing learned policy |
| Interpreter | Frozen parser recovering fields from text |
| Primary intervention | Template vs LLM wording; plain/diplomatic/hedged styles |
| Information intervention | Naive vs channel-aware belief updating, with calibration outside test |
| Real text | Expression inventory, style exemplars and human-annotated parser test material |

Do not change policy, scenario distribution, response rules and language model simultaneously and call the difference a wording effect.

## Research questions
1. Under which declared costs/response rules can backchannel information improve decisions relative to credible fixed strategies?
2. How faithfully do language styles carry proposal amounts, reciprocal conditions, public commitments and answers?
3. How does measured wording/interpretation error affect information value and final utility?
4. Does updating beliefs using a calibrated language channel recover any lost utility?

## Hypotheses, not assumptions
- Information can justify its cost in some environments; offers may already reveal enough information in others.
- Hedged/diplomatic wording may change recoverability, but it might preserve all task-relevant meaning.
- Channel-aware beliefs may help if miscalibration matters; they cannot recover information that was genuinely absent.
- PPO may match or underperform strong rules. Do not alter the environment merely to force a desired winner.

## Text–state contract
For A's message, separately preserve:
1. intended semantic frame;
2. generated utterance;
3. parsed frame visible to B;
4. resulting proposal/commitment/cost/state transition.

For B's reply, preserve:
1. actual response selected by fixed rules;
2. realized utterance;
3. A's interpreted response;
4. A's belief update and subsequent action.

The source frame is available to the evaluator for fidelity, not as a hidden shortcut for the recipient. Actual B acceptance and A's belief that B accepted must be separate: misunderstanding cannot create a mutually valid agreement.

## Data provenance and scope
Actual speeches, briefings and joint statements establish language examples and context. They are not complete negotiation trajectories and do not provide real hidden utility functions. All authored opponent rules, types, synthetic utterances and parameter scenarios must be labelled as such.

## Core comparison boundaries
- **Fidelity** (intended frame vs recovered frame) is end-to-end transmission quality, not pure parser accuracy.
- **Generator error** means the text does not express the intended frame.
- **Parser error** means the text expresses it but the interpretation is wrong.
- Human review is needed to distinguish those cases; model self-labels are not human gold.
- The probability of an `unclear` reply can itself be informative if it differs by hidden type. 'No update' requires an explicit modelling assumption, not a blanket rule.

## Proposed paper structure
Question and motivation → declared simulator and two-way language channel → data and controlled policies → fidelity/information/utility results → actual utterance trajectories → limitations and conclusion.

No result, performance table, trained checkpoint or old evaluation is carried into this new proposal.
