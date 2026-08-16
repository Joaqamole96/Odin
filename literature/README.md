# Review of Related Literature (RRL) — Workspace

> **Migration in progress:** the processed corpus (conversions + summaries) has
> moved to **`Odin-Literature`** — https://github.com/VibeCoders-3DCSAD/Odin-Literature
> Read **`_MIGRATION.md`** in this directory first.

This directory is now the **intake and tooling side** of the RRL. It holds
source PDFs, new-paper intake, conversion scripts, and AI summarization prompts.
The curated, scored corpus lives in Odin-Literature.

## What remains here (and why)

| Directory | Purpose |
|-----------|---------|
| `papers/` | Source-paper PDFs (518, Git LFS tracked). Ground truth for the corpus. |
| `bucket/` | Intake pool for new candidate PDFs. |
| `scripts/` | Conversion/dedupe/compile utilities (`prepare_pdf.py`, `pipeline.py`, `compile_summaries.py`, `count_pdf_pages.py`, `check_dupe_pdfs.py`). |
| `skills/` | AI agent prompts. Summarizer/synthesis still active; scorer/culler superseded (see `skills/DEPRECATED.md`). |
| `compilations/` | **Deprecated** — old-topic (1.A–14.C) copies of summaries (see `compilations/DEPRECATED.md`). |

**Removed:** `conversions/`, `summaries/`, `archive/` — migrated to
Odin-Literature or redundant; see `_MIGRATION.md`.

## New RRL workflow

1. Place candidate PDFs in `bucket/`.
2. Convert: `python3 scripts/prepare_pdf.py bucket/ --page-aware`
   → `{stem}_marked.md` + `{stem}_summarized.json`.
3. Summarize: use `skills/paper-summarizer-skill.md` as an AI prompt to fill the
   `_summarized.json`. Schema: `docs/standards/summary-format.md`.
4. Copy the pair into `Odin-Literature/literature/conversions/batch-<N>/`.
5. Score in Odin-Literature: `python3 scripts/embed.py` then `python3 scripts/score.py`.
6. Adapt module queries/thresholds in `Odin-Literature/config/modules.yaml` and re-run.

Full reference: `docs/standards/rrl-workflow.md`.

## Scripts (Python)

```bash
source .venv/bin/activate     # from repository root
```

| Script | Purpose |
|--------|---------|
| `scripts/prepare_pdf.py` | Convert PDFs → `_marked.md` + empty `_summarized.json` |
| `scripts/pipeline.py` | Orchestrate convert/manifest/validate/compile |
| `scripts/compile_summaries.py` | Compile summaries into one document (legacy workflow) |
| `scripts/count_pdf_pages.py` | List PDFs with page counts |
| `scripts/check_dupe_pdfs.py` | Find duplicate PDFs by hash cascade |

Dependencies: `markitdown`, `pypdf`, `pdfminer.six`, `PyPDF2` (see
`requirements.txt` at repository root).

## Naming & format standards

- `docs/standards/rrl-naming-conventions.md` — applies to files in Odin-Literature too
- `docs/standards/summary-format.md` — JSON schema for `_summarized.json`
- `docs/standards/rrl-workflow.md` — the (updated) processing workflow

## Topic taxonomy note

Compilation folder codes (`1.X`–`13.X`) follow the **old** outline and are
organizational only. The new thesis topical outline is
`docs/thesis/topical-outline/topical-outline.md`; re-mapping the RRL taxonomy is
pending. Once it is finalized, `Odin-Literature/config/modules.yaml` is where the
new topic/module definitions go.
