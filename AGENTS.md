# Odin-Paper — Agent Guide

**Thesis**: Development of Odin: A Personal Budget Management System Using Random Forest, LSTM, and Isolation Forest
**Group 4, III-DCSAD, University of Makati**

---

## Repository Role

This is the **academic documentation repository** for the Odin thesis. It contains thesis documents, literature reviews (RRL), and survey instruments. It does **not** contain application code, API servers, or ML model implementations — those live in `Odin-App/` and `Odin-ML/` respectively.

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
| `rrl` | RRL corpus: papers, summaries, compilations, syntheses |
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
  requirements.txt       # Python dependencies for RRL scripts
  rrl/                   # Review of Related Literature workspace (largest component)
  docs/                  # Thesis documents and standards
  survey/                # Survey instruments
```

---

## Navigation

| Document | Purpose |
|----------|---------|
| **`INDEX.md`** | Master index. Authoritative navigation for all files. |
| **`rrl/topic-outline.md`** | RRL topic taxonomy (14 topics, codes 1.A–14.C). Authoritative for topic mapping. |
| **`docs/thesis/system/Specification.md`** | Technical specification (v4.0). The main design contract. |
| **`docs/thesis/system/PRD-Full-Odin-App.md`** | Product requirements. 24 screen descriptions in `docs/thesis/system/screen-descriptions/`. |
| **`docs/research-proposal/Research-Proposal.md`** | Formal RP2 proposal. Authoritative for objectives/scope. |

---

## RRL Structure

Every curated paper has up to four files (same `{stem}`):

| File | Location |
|------|----------|
| `{stem}.pdf` | `rrl/papers/` |
| `{stem}_marked.md` | `rrl/conversions/` |
| `{stem}_summarized.json` | `rrl/summaries/` |
| `{stem}_Compilation.md` | `rrl/compilations/` (generated) |

### File Prefix Convention

`L--` = local (Philippine), `I--` = international, `A--` = algorithm/system focus.

Full reference: `docs/standards/rrl-naming-conventions.md`

### Python Utilities

| Script | Deps | What it does |
|--------|------|-------------|
| `rrl/scripts/prepare_pdf.py` | `markitdown`, `pypdf` | Converts PDFs → `_marked.md` with YAML frontmatter (metadata, SHA-256, page count) + empty `_summarized.json` |
| `rrl/scripts/pipeline.py` | stdlib | Orchestrates the full pipeline: convert, manifest, validate, compile |
| `rrl/scripts/compile_summaries.py` | stdlib | Compiles summaries → single `_Compilation.md` or `.json` with filters, sorting, range |
| `rrl/scripts/count_pdf_pages.py` | `pypdf` | Lists PDFs with page counts, optional `--lte`/`--gte` filtering |
| `rrl/scripts/check_dupe_pdfs.py` | `PyPDF2` (+ opt `PyMuPDF`, `Pillow`, `imagehash`) | Finds duplicate PDFs by hash cascade |

### RRL Workflow (9 Steps)

1. Place candidate PDFs in `rrl/bucket/`
2. Convert: `python3 rrl/scripts/prepare_pdf.py rrl/bucket/ --page-aware`
3. Summarize: use `rrl/skills/paper-summarizer-skill.md` as AI prompt (produces JSON)
4. Move converted/summarized files into `rrl/conversions/` and `rrl/summaries/`
5. Classify into topic folders: copy outputs into matching `rrl/compilations/{Topic}.{Letter}/` folder
6. Compile: `python3 rrl/scripts/compile_summaries.py -i <dir> -o <outdir>`
7. **Synthesize** (per-topic): use `rrl/skills/synthesis-compiler-skill.md` as AI prompt
8. **Cross-synthesize** (cross-topic): use `rrl/skills/cross-topic-synthesis-skill.md` as AI prompt
9. Cull: use `rrl/skills/paper-culler-skill.md` as AI prompt on a compilation

Full reference: `docs/standards/rrl-workflow.md`

### AI Agent Skills

| Skill | Purpose |
|-------|---------|
| `paper-summarizer-skill.md` | Objective, unbiased JSON summary from `_marked.md` with structured citations |
| `synthesis-compiler-skill.md` | Per-topic synthesis from a compilation of summaries |
| `cross-topic-synthesis-skill.md` | Cross-topic synthesis spanning multiple topic domains |
| `paper-culler-skill.md` | Classify papers as Crucial, Supporting, or Irrelevant |
| `paper-scorer-skill.md` | Score paper relevance with weighted dimensions |
| `paper-verifier-skill.md` | Verify summary completeness and designation correctness |

---

## Model & Data

- Model design docs, FIES CSV, BSP/PSA data, synthetic data handoffs are in `Odin-ML/`

---

## Python Environment

A `.venv/` exists (gitignored). Install dependencies from the repository root:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

| Package | Required By |
|---------|------------|
| `markitdown` | `prepare_pdf.py` |
| `pypdf` | `count_pdf_pages.py`, `prepare_pdf.py` (--page-aware) |
| `PyPDF2` | `check_dupe_pdfs.py` |

---

## Important Gotchas

- `docs/thesis/system/` contains `Specification-(OUTDATED).md` and `Model-&-Algorithm-Plan-(OUTDATED).md` — these are stale. Prefer the non-OUTDATED versions.
- `rrl/topic-outline.md` has 14 topics, but `docs/thesis/system/Specification.md` still says "twelve topics" in places.
- 518 PDFs (~969 MB) are tracked via Git LFS. New clones require `git lfs pull` to fetch binary content.
- Generated compilation files in `rrl/compilations/` are gitignored. Regenerate with `compile_summaries.py`.
- Legacy summaries (`.yaml`, `.md`) are still readable by `compile_summaries.py` but new summaries must be `.json`.
