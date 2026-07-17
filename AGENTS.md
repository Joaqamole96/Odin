# Odin-Paper — Agent Guide

**Thesis**: Development of Odin: A Personal Budget Management System Using Random Forest, LSTM, and Isolation Forest
**Group 4, III-DCSAD, University of Makati**

---

## Repository Role

This is the **academic documentation repository** for the Odin thesis. It contains thesis documents, literature reviews (RRL), model design specifications, data sources, and survey instruments. It does **not** contain application code, API servers, or ML model implementations — those live in `Odin-App/` and `Odin-ML/` respectively.

---

## Coding Standards

This repository does not contain application code, so backend/frontend coding standards from `REPOSITORY-STANDARDS.md` do not apply. The applicable standards are:

| Standard | Location |
|----------|----------|
| Git commit messages | `docs/standards/git-commit-standards.md` |
| Documentation discipline | `docs/standards/documentation-discipline.md` |
| RRL naming conventions | `docs/standards/rrl-naming-conventions.md` |
| RRL processing workflow | `docs/standards/rrl-workflow.md` |
| RRL summary format | `docs/standards/summary-format.md` |

Enforcement: Follow the commit message format for all commits. Keep `INDEX.md` updated when adding or moving files. Use the RRL naming conventions for all paper files.

---

## Git Commit Message Standards

```text
<type>(<scope>): <brief message>
```

Always include a scope. Use imperative mood. 50-72 characters.

### Scopes for This Repository

| Scope | Use For |
|-------|---------|
| `rrl` | RRL corpus: papers, summaries, compilations |
| `model` | Model design documents and data analysis |
| `data` | Data sources, synthetic data, FIES/BSP files |
| `docs` | Thesis documents, specifications, chapter drafts |
| `survey` | Survey instruments and notes |
| `config` | Repo configuration, tooling, scripts |
| `standards` | Shared engineering standards and agent guidance |
| `deps` | Dependency additions, removals, upgrades |

Full reference: `docs/standards/git-commit-standards.md`

---

## Top-Level Directory Layout

```
Odin-Paper/
  AGENTS.md              # This file — agent navigation and standards
  INDEX.md               # Master navigation index (authoritative)
  Topic-Outline.md       # RRL topic taxonomy (13 topics, codes 1.A–13.C)
  Open-Items.md          # Unresolved specification and validation items
  Notes.md               # Research notes and addenda
  Documents/             # Formal thesis materials (proposal, PRD, specification, chapters)
  RRL/                   # Review of Related Literature workspace (largest component)
  Model/                 # ML model design documents and data analysis
  Data/                  # Statistical data sources (FIES, BSP, PSA)
  Survey/                # Pre-survey instrument
  PDF-to-MD/             # Standalone PDF-to-Markdown converter utility
  docs/                  # Standards and documentation
```

---

## Navigation

| Document | Purpose |
|----------|---------|
| **`INDEX.md`** | Master index. Authoritative navigation for all files. |
| **`Topic-Outline.md`** | RRL topic taxonomy (13 topics, codes 1.A–13.C). Authoritative for topic mapping. |
| **`Documents/Thesis/System/Specification.md`** | Technical specification (v4.0). The main design contract. |
| **`Documents/Thesis/System/PRD-Full-Odin-App.md`** | Product requirements. 24 screen descriptions in `SCREEN-DESCRIPTIONS/`. |
| **`Documents/Research Proposal/Research-Proposal.md`** | Formal RP2 proposal. Authoritative for objectives/scope. |
| **`Open-Items.md`** | Unresolved specification and validation items. |

---

## RRL Structure

Every curated paper has three files (same `{stem}`):

| File | Location |
|------|----------|
| `{stem}.pdf` | `RRL/01_Papers/` |
| `{stem}_marked.md` | `RRL/03_Conversions/` |
| `{stem}_summarized.md` | `RRL/02_Summaries/` |

### File Prefix Convention

`L--` = local (Philippine), `I--` = international, `A--` = algorithm/system focus.

Full reference: `docs/standards/rrl-naming-conventions.md`

### Python Utilities

| Script | Deps | What it does |
|--------|------|-------------|
| `RRL/00_Proc/Z_Marker.py` | `markitdown` | Converts PDFs in a dir → `_marked.md` + empty `_summarized.md` |
| `RRL/00_Proc/Z_Mover.py` | stdlib | Moves processed files from working dir → `01_Papers/`, `02_Summaries/`, `03_Conversions/` |
| `RRL/Z_Compiler.py` | stdlib | Compiles `_summarized.md` files → single `_Compilation.md` with filters, sorting, range |
| `RRL/Z_Counter.py` | `pypdf` | Lists PDFs with page counts, optional `--lte`/`--gte` filtering |
| `RRL/Z_Dupechecker.py` | `PyPDF2` (+ opt `fitz`, `PIL`, `imagehash`) | Finds duplicate PDFs by hash cascade |
| `PDF-to-MD/pdf_to_md.py` | `pdftotext` in PATH | Standalone PDF→MD converter |
| `PDF-to-MD/pdf_to_md_server.py` | `pdftotext` in PATH | Web UI at `http://127.0.0.1:8000` |

### RRL Workflow

1. Place candidate PDFs in `RRL/00_Bucket/` or `RRL/00_Proc/`
2. Convert: `python3 RRL/00_Proc/Z_Marker.py [dir]`
3. Summarize: use `RRL/00_Proc/0_Summarizer.md` as AI prompt
4. Move: `python3 RRL/00_Proc/Z_Mover.py` (run from working dir)
5. Classify into topic folders: copy outputs into matching `RRL/04_Compilations/{Topic}.{Letter}/` folder
6. Compile: `python3 RRL/Z_Compiler.py -i <dir> -o <outdir> [--topic 7.C] [--designation local] [--sort year]`
7. Cull: use `RRL/04_Compilations/0_Culler.md` as AI prompt on a compilation

Full reference: `docs/standards/rrl-workflow.md`

---

## Model & Data

- `Model/00_Analysis/` — PSA FIES data analysis in Markdown
- `Model/00_Preparation/PREP-RandomForest.md` — RF classifier prep notes
- `Model/01_Design/` — `model-training-data-design.md`, `synthetic-data-parameters-handoff.md`
- `Model/MDD.md` — Model Design Document for FBP Classifier (v1.0)
- `Data/` — FIES CSV, BSP data, PSA data, synthetic data handoff documents

---

## Python Environment

A `.venv/` exists (gitignored). Scripts use standard library + these optional packages:

| Package | Required By |
|---------|------------|
| `markitdown` | `Z_Marker.py` |
| `pypdf` | `Z_Counter.py` |
| `PyPDF2` | `Z_Dupechecker.py` |

Activate before running scripts: `source .venv/bin/activate`

---

## Important Gotchas

- `Documents/Thesis/System/` contains `Specification-(OUTDATED).md` and `Model-&-Algorithm-Plan-(OUTDATED).md` — these are stale. Prefer the non-OUTDATED versions.
- `RRL/05_Archived/` is empty and should not be used.
- `Topic-Outline.md` has 13 topics, but `Specification.md` still says "twelve topics" in places.
- 520 PDFs (~969 MB) are tracked via Git LFS. New clones require `git lfs pull` to fetch binary content.
- Generated compilation files in `RRL/04_Compilations/` are gitignored. Regenerate with `Z_Compiler.py`.
