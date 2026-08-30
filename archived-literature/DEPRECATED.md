# Odin-Paper — literature/ (DEPRECATED)

**This entire directory is deprecated.** All RRL processing has moved to **Odin-Literature** (https://github.com/VibeCoders-3DCSAD/Odin-Literature).

## What lives where now

| What | Where it is now |
|------|-----------------|
| Curated corpus (conversions, summaries, scores) | `Odin-Literature/literature/conversions/` |
| Scoring pipeline (embed, score, manifest) | `Odin-Literature/scripts/` |
| Module configuration | `Odin-Literature/config/modules.yaml` |
| PDF fetch/convert/dedupe/count scripts | `Odin-Literature/scripts/` |
| Summary JSON schema | `Odin-Literature/docs/standards/summary-format.md` |
| Naming conventions | `Odin-Literature/docs/standards/rrl-naming-conventions.md` |
| Workflow documentation | `Odin-Literature/docs/standards/rrl-workflow.md` |

## What remains here (until manual migration)

- `literature/papers/` — source PDFs (Git LFS). These will be migrated to Odin-Literature when relevance is verified against the new topical outline.
- `literature/bucket/` — intake PDFs. Deprecated; use Odin-Literature's bucket.
- `literature/compilations/` — deprecated old-taxonomy compilations. Do not use.

## What was deprecated (not moved)

- `literature/scripts/convert_batch.py` — redundant wrapper around `prepare_pdf.py`
- `literature/scripts/pipeline.py` — orchestrator with legacy compile step
- `literature/scripts/compile_summaries.py` — tied to old topic taxonomy
- `literature/skills/` — AI prompt skills; not moved. Skills form through demand in Odin-Literature.

## Migration timeline

PDFs in `literature/papers/` will be verified against the new topical outline and migrated to Odin-Literature manually. Until then, the Odin-Literature pipeline operates on the already-migrated markdown conversions (518 papers in `literature/conversions/batch-1..6/`).
