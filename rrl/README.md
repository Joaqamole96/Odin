# Review of Related Literature (RRL)

This directory contains the full RRL workspace: source papers, markdown conversions, structured summaries, compiled topic reviews, synthesis documents, processing scripts, and AI agent skills.

## Directory Structure

```
rrl/
├── bucket/              # Raw PDF intake pool (unprocessed candidates)
├── papers/              # Curated source-paper PDFs (Git LFS tracked)
├── conversions/         # _marked.md markdown conversions with YAML frontmatter
├── summaries/           # _summarized.json structured JSON summaries
├── compilations/        # Compiled topic-level review documents
│   ├── 1.X/ … 13.X/     # Topic folders (codes follow the old outline)
│   ├── local/           # By designation: local
│   ├── local-algorithm-specific/
│   ├── international/
│   └── international-algorithm-specific/
├── archive/             # Old/unsorted workspace snapshots (e.g. 2026-07-20_190503)
├── scripts/             # Python utility scripts
└── skills/              # AI agent skill prompts
```

## Naming Conventions

Every curated paper has up to four files sharing the same stem:

| File | Location | Description |
|------|----------|-------------|
| `{stem}.pdf` | `papers/` | Source PDF |
| `{stem}_marked.md` | `conversions/` | Markdown conversion with metadata frontmatter |
| `{stem}_summarized.json` | `summaries/` | Structured JSON summary |
| `{stem}_Compilation.md` | `compilations/` | Multi-paper compilation (generated) |

### Prefix Convention

| Prefix | Meaning |
|--------|---------|
| `L--` | Local (Philippine) study |
| `I--` | International study |
| `A--` | Algorithm/system focus |

Full reference: `docs/standards/rrl-naming-conventions.md`

## Scripts

All scripts are in `scripts/`. Activate the virtual environment before running:

```bash
source .venv/bin/activate
```

Install dependencies from the repository root:

```bash
pip install -r requirements.txt
```

### prepare_pdf.py

Converts PDFs in a directory to Markdown with YAML frontmatter containing conversion metadata (timestamp, SHA-256 hash, page count). Optionally extracts page-aware text via pypdf.

```bash
python3 rrl/scripts/prepare_pdf.py [target_dir] [options]
```

| Argument | Description |
|----------|-------------|
| `target_dir` | Directory containing PDF files (default: `.`) |
| `--suffix` | Suffix for converted Markdown (default: `_marked.md`) |
| `--summary-suffix` | Suffix for summary file (default: `_summarized.json`) |
| `--no-summary` | Skip creating empty summary files |
| `--no-frontmatter` | Skip adding YAML frontmatter |
| `--page-aware` | Add `<!-- PAGE N -->` markers via pypdf |
| `--json-sidecar` | Write a separate `{stem}_conversion_meta.json` |
| `-v, --verbose` | Enable verbose logging |

Requires: `markitdown`, `pypdf` (for `--page-aware`)

### pipeline.py

Orchestrates the full RRL pipeline: convert, manifest, validate, compile.

```bash
python3 rrl/scripts/pipeline.py --input-dir <dir> [options]
```

| Argument | Description |
|----------|-------------|
| `--input-dir, -i` | Input directory (required) |
| `--output-dir, -o` | Output directory (default: same as input) |
| `--step, -s` | Step to run: `convert`, `manifest`, `validate`, `compile`, `all` (default: `all`) |
| `--page-aware` | Enable page-aware extraction for convert step |
| `--json-sidecar` | Write JSON sidecar for convert step |
| `--designation, -d` | Filter for compile step |
| `--topic, -t` | Filter for compile step |
| `--sort` | Sort order for compile step |
| `--log-file` | Custom path for pipeline run log (default: `pipeline_run.json`) |

Requires: stdlib only

### compile_summaries.py

Compiles summary files into a single document. Supports JSON (preferred), YAML, and Markdown summaries. JSON summaries are parsed with `json.load()` for reliable field extraction.

```bash
python3 rrl/scripts/compile_summaries.py -i <input-dir> -o <output-dir> [options]
```

| Argument | Description |
|----------|-------------|
| `-i, --input` | Directory containing summary files (required) |
| `-o, --output-dir` | Output directory (required) |
| `-d, --designation` | Filter by designation |
| `-t, --topic` | Filter by topic code |
| `--floor` | Starting position (1-based) |
| `--ceiling` | Ending position (1-based, inclusive) |
| `--sort` | Sort: `alpha` (default) or `year` (descending) |
| `--format` | Output format: `markdown` (default) or `json` |
| `-r, --randomize` | Randomize order |
| `-q, --quiet` | Suppress progress messages |

Requires: stdlib only

### count_pdf_pages.py

Lists PDFs with page counts, with optional filtering.

```bash
python3 rrl/scripts/count_pdf_pages.py <directories> [options]
```

| Argument | Description |
|----------|-------------|
| `directories` | One or more directories to search (required) |
| `--lte N` | Only show PDFs with page count <= N |
| `--gte N` | Only show PDFs with page count >= N |
| `--sort` | Sort by `name` (default) or `pages` |

Requires: `pypdf`

### check_dupe_pdfs.py

Finds duplicate PDFs using a cascade of hashing and comparison methods.

```bash
python3 rrl/scripts/check_dupe_pdfs.py <directories> [options]
```

| Argument | Description |
|----------|-------------|
| `directories` | One or more directories to search (required) |
| `--method` | Single method: `byte`, `text_hash`, or `visual` |
| `--cascade` | Use full cascade: text → content hash → byte hash → visual |
| `--sim-threshold` | Text similarity threshold (default: 0.95) |
| `--vis-threshold` | Visual similarity threshold (default: 0.9) |

Requires: `PyPDF2` (required), `PyMuPDF`, `Pillow`, `imagehash` (optional, for visual dedup)

## Skills

AI agent skill prompts in `skills/`:

| Skill | Purpose |
|-------|---------|
| `paper-summarizer-skill.md` | Fill structured JSON summaries from `_marked.md` (objective, unbiased) |
| `synthesis-compiler-skill.md` | Produce per-topic synthesis from a compilation of summaries |
| `cross-topic-synthesis-skill.md` | Produce cross-topic synthesis from multiple per-topic syntheses |
| `paper-culler-skill.md` | Classify papers as Crucial, Supporting, or Irrelevant |
| `paper-scorer-skill.md` | Score paper relevance with weighted dimensions |
| `paper-verifier-skill.md` | Verify summary completeness and designation correctness |

## Workflow

See `docs/standards/rrl-workflow.md` for the full 9-step processing workflow. Summary:

1. Place PDFs in `bucket/`
2. Convert: `python3 rrl/scripts/prepare_pdf.py rrl/bucket/ --page-aware`
3. Summarize with AI using `skills/paper-summarizer-skill.md`
4. Move converted/summarized files into `conversions/` and `summaries/`
5. Classify into topic folders under `compilations/{Topic}.{Letter}/`
6. Compile: `python3 rrl/scripts/compile_summaries.py -i <dir> -o <outdir>`
7. **Synthesize** with AI using `skills/synthesis-compiler-skill.md`
8. **Cross-synthesize** with AI using `skills/cross-topic-synthesis-skill.md`
9. Cull with AI using `skills/paper-culler-skill.md`

## Topic Taxonomy

> **Note:** the RRL topic codes and folders below follow the **old** topic outline. The new thesis topical outline (`docs/thesis/topical-outline/topical-outline.md`) supersedes it, and re-mapping the RRL taxonomy to it is pending. Until then, treat compilation folder codes as organizational only.

The old taxonomy defined 14 major topics with codes 1.A–14.C (compilation folders currently cover `1.X`–`13.X`). Topics covered Filipino financial behavior, cultural context, expense categorization, existing systems, behavioral profiling, spending forecasting, budget recommendation, anomaly detection, mobile design, privacy, retention, system evaluation, savings/debt management, and ML pipeline infrastructure.

## Dependencies

| Package | Required By |
|---------|------------|
| `markitdown` | `prepare_pdf.py` |
| `pypdf` | `count_pdf_pages.py`, `prepare_pdf.py` (--page-aware) |
| `PyPDF2` | `check_dupe_pdfs.py` |

Optional (for visual dedup in `check_dupe_pdfs.py`): `PyMuPDF`, `Pillow`, `imagehash`
