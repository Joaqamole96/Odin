# Odin-Paper — Agent Guide

**Thesis**: Development of Odin: A Personal Finance Management Application for Filipino Working Young Adults Using Random Forest, LSTM, and Isolation Forest
**Group 4, III-DCSAD, University of Makati**

---

## Repository Role

This is the **academic documentation repository** for the Odin thesis. It contains thesis documents, literature reviews (RRL), and survey instruments. It does **not** contain application code, API servers, or ML model implementations — those live in `Odin-App/` and `Odin-ML/` respectively.

> **Ground truth:** the authoritative versions of the thesis documents live in the Google Drive folder. Copies in this repository are working mirrors and may lag behind the Drive source — verify before citing.

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
| `rrl` | RRL workspace: `literature/` intake/tooling; curated corpus in Odin-Literature |
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
  literature/            # RRL intake & tooling: source PDFs, bucket, scripts, skills
  docs/                  # Thesis documents and standards
  survey/                # Survey instruments
```

> **RRL migration:** the curated corpus (conversions + summaries + scores) lives in
> **`Odin-Literature`** (https://github.com/VibeCoders-3DCSAD/Odin-Literature).
> `literature/` here holds source PDFs, intake, and tools only. See
> `literature/_MIGRATION.md`.

---

## Navigation

| Document | Purpose |
|----------|---------|
| **`INDEX.md`** | Master index. Authoritative navigation for all files. |
| **`docs/thesis/topical-outline/topical-outline.md`** | Topical outline (v0.1.0). Thesis structure ground truth. |
| **`docs/thesis/specifications/system-spec.md`** | System specification (v0.1.0). The main design contract. |
| **`docs/thesis/paper/chapter-1.md`** | Chapter 1 draft (Introduction). |
| **`docs/thesis/system/PRD-Full-Odin-App.md`** | Product requirements. 24 screen descriptions in `docs/thesis/system/screen-descriptions/`. |
| **`docs/research-proposal/Research-Proposal.md`** | Formal RP2 proposal. Authoritative for objectives/scope. |
| **`docs/ml/README.md`** | ML model design, data analysis, and training documentation (phases 1–6). |

---

## RRL Structure

Every curated paper has up to four files (same `{stem}`). The processed files
live in **Odin-Literature**; only the source PDF stays in this repo:

| File | Location |
|------|----------|
| `{stem}.pdf` | `literature/papers/` |
| `{stem}_marked.md` | `Odin-Literature/literature/conversions/` |
| `{stem}_summarized.json` | `Odin-Literature/literature/conversions/` (same folder, next to the `_marked.md`) |
| `{stem}_Compilation.md` | `literature/compilations/` (deprecated; old-taxonomy copies) |

### File Prefix Convention

`L--` = local (Philippine), `I--` = international, `A--` = algorithm/system focus.

Full reference: `docs/standards/rrl-naming-conventions.md`

> **Note:** the RRL topic codes (`1.A`–`14.C`, compilation folders `1.X`–`13.X`) follow the **old** topic outline. The new thesis topical outline (`docs/thesis/topical-outline/topical-outline.md`) supersedes it; re-mapping the RRL taxonomy is pending.

### Python Utilities

| Script | Deps | What it does |
|--------|------|-------------|
| `literature/scripts/prepare_pdf.py` | `markitdown`, `pypdf` | Converts PDFs → `_marked.md` with YAML frontmatter (metadata, SHA-256, page count) + empty `_summarized.json` |
| `literature/scripts/pipeline.py` | stdlib | Orchestrates the intake pipeline: convert, manifest, validate, compile |
| `literature/scripts/compile_summaries.py` | stdlib | Compiles summaries → single `_Compilation.md` or `.json` (legacy workflow) |
| `literature/scripts/count_pdf_pages.py` | `pypdf` | Lists PDFs with page counts, optional `--lte`/`--gte` filtering |
| `literature/scripts/check_dupe_pdfs.py` | `PyPDF2` (+ opt `PyMuPDF`, `Pillow`, `imagehash`) | Finds duplicate PDFs by hash cascade |

> Scoring utilities (BERT + TF-IDF + BM25 relevance, quality, redundancy) are in
> **Odin-Literature**: `scripts/embed.py`, `scripts/score.py`, config in
> `config/modules.yaml`.

### RRL Workflow (Intake → Odin-Literature)

1. Place candidate PDFs in `literature/bucket/`
2. Convert: `python3 literature/scripts/prepare_pdf.py literature/bucket/ --page-aware`
3. Summarize: use `literature/skills/paper-summarizer-skill.md` as AI prompt (fills `_summarized.json`)
4. Move the `_marked.md` + `_summarized.json` pair into `Odin-Literature/literature/conversions/batch-<N>/`
5. Score in Odin-Literature: `python3 scripts/embed.py` then `python3 scripts/score.py`
6. Adapt: edit `Odin-Literature/config/modules.yaml` (module queries, weights, thresholds) and re-run `score.py`

Full reference: `docs/standards/rrl-workflow.md`

### AI Agent Skills

| Skill | Status |
|-------|--------|
| `paper-summarizer-skill.md` | **Active** — fills `_summarized.json` for new papers |
| `synthesis-compiler-skill.md` | Active (old-taxonomy synthesis) |
| `cross-topic-synthesis-skill.md` | Active (cross-topic synthesis) |
| `paper-verifier-skill.md` | Active — verifies summary completeness |
| `paper-culler-skill.md` | **Superseded** — replaced by Odin-Literature `scripts/score.py` |
| `paper-scorer-skill.md` | **Superseded** — replaced by Odin-Literature `scripts/score.py` |

See `literature/skills/DEPRECATED.md`.

---

## Model & Data

- ML model design, data analysis, and training documentation are in `docs/ml/` (see `docs/ml/README.md`).
- FIES CSV, BSP/PSA data, and synthetic data handoffs are in `Odin-ML/`.

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

- `docs/thesis/system/` holds preserved historical copies: `specification (OLD).md` (v4.0 spec) and `topic-outline (OLD).md`. Both are superseded — the current spec is `docs/thesis/specifications/system-spec.md` and the current outline is `docs/thesis/topical-outline/topical-outline.md`.
- RRL topic codes (`1.A`–`14.C`) and topic-count references follow the **old** topic outline. The new topical outline is being finalized; expect the RRL taxonomy to be re-mapped to it. Until then, treat compilation folder codes as organizational only.
- 518 PDFs (~969 MB) are tracked via Git LFS. New clones require `git lfs pull` to fetch binary content.
- **Migrated:** `literature/conversions/`, `literature/summaries/`, and `literature/archive/` were removed — the corpus now lives in Odin-Literature. See `literature/_MIGRATION.md`.
- `literature/compilations/` is **deprecated** (old-taxonomy copies); do not add new files there.
- New summaries must be `.json` (schema: `docs/standards/summary-format.md`).
