# Source registry

## Research direction
Naura's supplied proposal is the starting document, confirmed by Hogyun after their meeting. Its neutral working question is preserved in [PROPOSAL.md](PROPOSAL.md). Do not replace it with the earlier workspace's information-policy comparison topic.

## Source bundles (not uploaded to this repository)
The following files remain in Hogyun's parent MIDTERM folder. Collaborators should obtain the same originals from the team and verify checksums in `source_manifest.json`; do not rely on a user's absolute machine path.

| Bundle/file | Purpose |
|---|---|
| `Midterm-20261010T021032Z-1-001.zip` | Naura proposal DOCX/PDF under `Midterm/proposal/`; dataset copy |
| `dataset-20261010T022106Z-1-001.zip` | Candidate source sentences, source logs, guidelines and blank human sheets |
| `ABC_Track_Guides_COLING_Examples_EN.zip` | General guide, Track C detailed guide and example paper |
| `EMNLP_Capstone_Guide_EN (1).pdf` | Course-wide implementation/evaluation/writing requirements |
| `Midterm Exam NLP_261008_161545.pdf` | Background notes and example project ideas; not a substitute for the main guide |

Keep local copies in `data/raw/` or another ignored location. Do not bulk-upload source archives. The two dataset copies were previously found identical; this does not establish correct splits or completed annotations.

## Source interpretation
- Proposal paragraphs describing human labels and experiments are a plan, not proof they are completed.
- Some proposal equations were not preserved by document conversion. Check the source document and independently validate equations before committing a simulator specification; do not fill missing symbols by guesswork.
- The professor's example paper illustrates reporting and assumptions. Do not copy its numerical results into this study.
- Existing workspace research results and conference-readiness reviews are not new-study evidence. Keep any future reuse explicit and separately labelled.

## External documentation
- OpenRouter model metadata: https://openrouter.ai/api/v1/models/openai/gpt-5.6-luna/endpoints
- Parameters: https://openrouter.ai/docs/api_reference/parameters
- Service tiers: https://openrouter.ai/docs/guides/features/service-tiers
- Reasoning: https://openrouter.ai/docs/guides/best-practices/reasoning-tokens
- COLING official site referenced by course guide: https://2027.coling-iccl.org/
- ARR: https://aclrollingreview.org/

Verify current model and conference requirements when execution/submission is scheduled. The user has confirmed the actual conference-submission goal; do not use the classroom guide's minimum requirements to dismiss that goal.
