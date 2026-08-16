# RRL Processing Workflow

Workflow for adding and processing literature in the Review of Related Literature.

> **RRL migration:** the curated corpus (conversions, summaries, scores) lives in
> **Odin-Literature** (https://github.com/VibeCoders-3DCSAD/Odin-Literature).
> This repo (`Odin-Paper`) now only handles intake: source PDFs, conversion,
> summarization, and handing off to Odin-Literature. See
> `literature/_MIGRATION.md`.

## Steps

### 1. Intake

Place candidate PDFs in `literature/bucket/` (intake pool).

### 2. Convert

Run the pipeline orchestrator or the converter directly:

```bash
# Full pipeline (recommended):
python3 literature/scripts/pipeline.py --input-dir literature/bucket/ --step convert --page-aware

# Or directly:
python3 literature/scripts/prepare_pdf.py literature/bucket/ --page-aware
```

Produces `{stem}_marked.md` with YAML frontmatter (conversion metadata, SHA-256 hash, page count) and an empty `{stem}_summarized.json`.

Options:
- `--page-aware`: Add `<!-- PAGE N -->` markers extracted via pypdf
- `--json-sidecar`: Write a separate `{stem}_conversion_meta.json`

Requires: `markitdown`, `pypdf` (for `--page-aware`)

### 3. Summarize

Use `literature/skills/paper-summarizer-skill.md` as an AI agent prompt. Feed it the `_marked.md` file. The agent fills the corresponding `_summarized.json` with a structured JSON summary.

The summarizer is **objective and unbiased** — it describes what the paper says without application-specific framing. Page and paragraph references are included in structured `citations` objects.

See `docs/standards/summary-format.md` for the schema reference.

### 4. Move to Odin-Literature

Move the converted/summarized file pair into the Odin-Literature corpus:

```bash
mv <file>_marked.md <file>_summarized.json ../Odin-Literature/literature/conversions/batch-<N>/
```

Start a new `batch-<N>` directory (next number) when adding a group of papers.

### 5. Score

In Odin-Literature, compute embeddings and scores:

```bash
python3 scripts/embed.py
python3 scripts/score.py
```

`score.py` ranks every paper against the thesis modules (BERT 0.5 / TF-IDF 0.3 / BM25 0.2) and assigns tiers: **crucial** (≥0.45), **supporting** (≥0.30), **cull** (<0.30). Redundant near-duplicates are flagged (threshold 0.98). Outputs land in `scores/`.

### 6. Adapt to Thesis Changes

The thesis outline, architecture, and algorithm selections change often. When they do, edit **only** `Odin-Literature/config/modules.yaml` (module queries, weights, tier thresholds, redundancy threshold) and re-run `score.py`. No code changes needed.

## Python Dependencies

| Package | Required By |
|---------|------------|
| `markitdown` | `prepare_pdf.py` |
| `pypdf` | `count_pdf_pages.py`, `prepare_pdf.py` (--page-aware) |
| `PyPDF2` | `check_dupe_pdfs.py` |

Standard library only: `compile_summaries.py`, `pipeline.py`.

Install from repository root:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

## Utility Scripts

| Script | Purpose |
|--------|---------|
| `literature/scripts/prepare_pdf.py` | Convert PDFs to Markdown with metadata |
| `literature/scripts/pipeline.py` | Orchestrate the intake pipeline |
| `literature/scripts/compile_summaries.py` | Compile summaries into a single document (legacy) |
| `literature/scripts/count_pdf_pages.py` | List PDFs with page counts |
| `literature/scripts/check_dupe_pdfs.py` | Find duplicate PDFs by hash cascade |

Scoring utilities (embedding, scoring) are in Odin-Literature: `scripts/embed.py`, `scripts/score.py`, `config/modules.yaml`.
