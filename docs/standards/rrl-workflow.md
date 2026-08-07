# RRL Processing Workflow

Nine-step workflow for adding, processing, and synthesizing literature in the Review of Related Literature.

> **Note:** topic codes referenced below (e.g. `5.C/`, `7.C`) follow the **old** topic outline. The new thesis topical outline is `docs/thesis/topical-outline/topical-outline.md`; re-mapping the RRL taxonomy to it is pending. The `rrl/syntheses/` output directory does not exist yet — create it when the first synthesis is produced.

## Steps

### 1. Intake

Place candidate PDFs in `rrl/bucket/` (intake pool).

### 2. Convert

Run the pipeline orchestrator or the converter directly:

```bash
# Full pipeline (recommended):
python3 rrl/scripts/pipeline.py --input-dir rrl/bucket/ --step convert --page-aware

# Or directly:
python3 rrl/scripts/prepare_pdf.py rrl/bucket/ --page-aware
```

Produces `{stem}_marked.md` with YAML frontmatter (conversion metadata, SHA-256 hash, page count) and an empty `{stem}_summarized.json`.

Options:
- `--page-aware`: Add `<!-- PAGE N -->` markers extracted via pypdf
- `--json-sidecar`: Write a separate `{stem}_conversion_meta.json`

Requires: `markitdown`, `pypdf` (for `--page-aware`)

### 3. Summarize

Use `rrl/skills/paper-summarizer-skill.md` as an AI agent prompt. Feed it the `_marked.md` file. The agent fills the corresponding `_summarized.json` with a structured JSON summary.

The summarizer is **objective and unbiased** — it describes what the paper says without application-specific framing. Page and paragraph references are included in structured `citations` objects.

See `docs/standards/summary-format.md` for the schema reference.

### 4. Move

Move converted and summarized files into their curated stores:

```bash
mv <file>_marked.md rrl/conversions/
mv <file>_summarized.json rrl/summaries/
```

### 5. Classify into Topics

Copy relevant `_marked.md`, `_summarized.json` files into the matching topic folder:

```
rrl/compilations/{Topic}.{Letter}/
```

Use the RRL topic codes (e.g., `5.C/`, `8.B/`) to determine placement. The codes come from the old outline (see note at top).

### 6. Compile

Run the compiler for the relevant topic folder:

```bash
# Markdown compilation (default):
python3 rrl/scripts/compile_summaries.py -i <dir> -o <outdir> [--topic 7.C] [--designation local] [--sort year]

# JSON compilation:
python3 rrl/scripts/compile_summaries.py -i <dir> -o <outdir> --format json

# Or use the pipeline orchestrator:
python3 rrl/scripts/pipeline.py --input-dir <dir> --output-dir <outdir> --step compile
```

Produces a single `_Compilation.md` (or `.json`) combining all summaries in the directory.

### 7. Synthesize (per-topic)

Use `rrl/skills/synthesis-compiler-skill.md` as an AI agent prompt on a compilation file. The agent produces a synthesis document that integrates findings across papers for a single topic.

Output: `rrl/syntheses/{Topic}.{Letter}_Synthesis.md`

The synthesis identifies:
- Areas of agreement across papers
- Areas of disagreement or diverging findings
- Gaps in the literature (methodological, empirical, conceptual)
- Key claims with structured citations

### 8. Cross-Synthesize (cross-topic)

Use `rrl/skills/cross-topic-synthesis-skill.md` as an AI agent prompt on two or more per-topic synthesis documents. The agent produces a cross-topic synthesis.

Output: `rrl/syntheses/{TopicA}x{TopicB}_Cross-Synthesis.md`

The cross-synthesis identifies:
- Cross-cutting themes spanning multiple topics
- Dependencies and interactions between topics
- Tensions where findings pull in opposite directions
- Cross-cutting gaps requiring multi-topic research

### 9. Cull

Use `rrl/skills/paper-culler-skill.md` as an AI agent prompt on a compilation. The agent classifies each paper as **Crucial**, **Supporting**, or **Irrelevant**.

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
| `rrl/scripts/prepare_pdf.py` | Convert PDFs to Markdown with metadata |
| `rrl/scripts/pipeline.py` | Orchestrate the full pipeline |
| `rrl/scripts/compile_summaries.py` | Compile summaries into a single document |
| `rrl/scripts/count_pdf_pages.py` | List PDFs with page counts |
| `rrl/scripts/check_dupe_pdfs.py` | Find duplicate PDFs by hash cascade |
