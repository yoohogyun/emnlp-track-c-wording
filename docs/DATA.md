# Data and annotation

## Available input, not completed evaluation
Naura's supplied package contains a 250-sentence main sample plus 31 condition-supplement sentences, source metadata, annotation instructions and scripts. The supplied two 100-row human sheets were blank when inspected. A file named `model_labels.csv` is model annotation, not human gold.

We retain this package as a **candidate source pool**. The new study has not finalized its split or imported the old experimental split. Original files stay outside this repository until an explicit, provenance-preserving preparation step is implemented.

## Planned uses
- Source sentences: utterance-function inventory and disjoint style examples.
- Human-labelled real-text subset: parser evaluation for function, condition, commitment and answer type.
- Synthetic semantic frames/messages: numeric/role/condition transmission tests and controlled simulator execution.
- Synthetic parameter scenarios: policy learning/evaluation, not independent historical events.

## Annotation workflow from the proposal
1. Read the context document and mark proposals, conditions and commitments.
2. Calibrate on roughly20 extra examples outside the final evaluation set.
3. Select a document-disjoint evaluation set; the proposal target is100 independently labelled rows, with explicit conditions represented. Counts can change only with a recorded justification.
4. Each annotator works independently without looking at model labels or the other person's answers.
5. Compute pre-adjudication agreement per field; discuss disagreements and record final gold labels separately.
6. Spot-check model labels used only for description/style retrieval; do not claim all were human verified.
7. Keep inaccessible/ambiguous/broken-sentence exclusions and reasons. Preserve identifiers and provenance.

Human labels/κ are **not completed** merely because the proposal describes them in future/present tense. Do not fill them with LLM outputs while calling them human judgments.

## Splitting and leakage
- Group source document/event before sentence sampling and augmentation.
- Do not reuse style exemplars or their source group as the claimed held-out real-text parser test.
- Group exact and near-duplicate generated messages; held-out generation request IDs alone are not held-out language.
- Keep language-channel calibration separate from final test messages; specify whether scenarios and wordings generalize independently.
- For each feature, document whether it is observed, inferred, or evaluator-only. Gold frames/types/replies cannot bypass a recipient's text interpretation.

## Schema to agree before preparation
Suggested source columns: sentence_id, document_id, source, title/date/URL_or_DOI, source_type(original/official-English/translation), text, split and annotation status. Annotation columns: function, condition_present, commitment_strength, answer_type, notes, annotator/version.

Suggested bank columns: frame_id, explicit semantics, speaker, style, split/group_id, exemplar_ids, prompt/model/config/seed, request_hash, actual_text, parsed_fields, failure_status and usage. The frame must include the actual reciprocal condition, not just a Boolean.

## Interpretation pitfalls
- An `if` clause is not automatically an offer; its function needs context.
- A response cannot reliably be called evasive without the question/context; retain it when required.
- Intended-frame mismatch mixes generation and parsing errors. Use human text inspection to separate them.
- Public briefings are linguistic examples, not observed private backchannel dialogues.
- Track source documents, sentences, synthetic frames/messages, parameter scenarios and repetitions separately.

## Storage
`data/raw/`, `data/local/`, `data/processed/` and `artifacts/` are initially Git-ignored. Commit only reviewed small manifests/annotations after checking rights and removing private information. A private GitHub repository is not a substitute for redistribution permission.
