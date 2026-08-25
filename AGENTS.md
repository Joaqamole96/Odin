# Odin-Paper — Agent Guide

**Thesis**: Development of Odin: A Personal Finance Management Application for Filipino Working Young Adults Using Random Forest, LSTM, and Isolation Forest
**Group 4, III-DCSAD, University of Makati**

---

## Repository Role

This is the **knowledge base** for the Odin thesis. It contains thesis documents, specifications, PRDs, and survey instruments. It does **not** contain application code, API servers, or ML model implementations — those live in `Odin-App/` and `Odin-ML/` respectively.

The RRL corpus, scoring pipeline, and related tooling live in **Odin-Literature** (https://github.com/VibeCoders-3DCSAD/Odin-Literature).

> **Ground truth:** the authoritative versions of the thesis documents live in the Google Drive folder. Copies in this repository are working mirrors and may lag behind the Drive source — verify before citing.

---

## Coding Standards

This repository does not contain application code, so backend/frontend coding standards from `REPOSITORY-STANDARDS.md` do not apply. The applicable standards are:

| Standard | Location |
|----------|----------|
| Git commit messages | `docs/standards/git-commit-standards.md` |
| Documentation discipline | `docs/standards/documentation-discipline.md` |

Enforcement: Follow the commit message format for all commits. Keep `INDEX.md` updated when adding or moving files.

> **RRL standards** (naming conventions, summary format, workflow) have moved to **Odin-Literature**: `docs/standards/`.

---

## Git Commit Message Standards

```text
<type>(<scope>): <brief message>
```

Always include a scope. Use imperative mood. 50-72 characters.

### Scopes for This Repository

| Scope | Use For |
|-------|---------|
| `model` | Model design documents and data analysis |
| `data` | Data sources, synthetic data, FIES/BSP files |
| `docs` | Thesis documents, specifications, chapter drafts |
| `survey` | Survey instruments and notes |
| `config` | Repo configuration, tooling |
| `standards` | Shared engineering standards and agent guidance |

Full reference: `docs/standards/git-commit-standards.md`

---

## Top-Level Directory Layout

```
Odin-Paper/
  AGENTS.md              # This file — agent navigation and standards
  INDEX.md               # Master navigation index (authoritative)
  docs/                  # Thesis documents and standards
  survey/                # Survey instruments
  literature/            # DEPRECATED — see literature/DEPRECATED.md
```

---

## Navigation

| Document | Purpose |
|----------|---------|
| **`INDEX.md`** | Master index. Authoritative navigation for all files. |
| **`docs/planning-management/topical-outline.md`** | Topical outline. Thesis structure ground truth. |
| **`docs/thesis/specifications/system-spec.md`** | System specification. The main design contract. |
| **`docs/thesis/paper/chapter-1.md`** | Chapter 1 draft (Introduction). |
| **`docs/thesis/system/PRD-Full-Odin-App.md`** | Product requirements. 24 screen descriptions in `docs/thesis/system/screen-descriptions/`. |
| **`docs/research-proposal/Research-Proposal.md`** | Formal RP2 proposal. Authoritative for objectives/scope. |
| **`docs/ml/README.md`** | ML model design, data analysis, and training documentation (phases 1-6). |

---

## Model & Data

- ML model design, data analysis, and training documentation are in `docs/ml/` (see `docs/ml/README.md`).
- FIES CSV, BSP/PSA data, and synthetic data handoffs are in `Odin-ML/`.

---

## Python Environment

A `.venv/` exists (gitignored). This repository has no Python dependencies of its own — `requirements.txt` is a legacy artifact. All RRL processing scripts now live in **Odin-Literature**.

---

## Important Gotchas

- `docs/thesis/system/` holds preserved historical copies: `specification (OLD).md` (v4.0 spec) and `topic-outline (OLD).md`. Both are superseded.
- 518 PDFs (~969 MB) are tracked via Git LFS in `literature/papers/`. These will be migrated to Odin-Literature when verified against the new topical outline.
- **`literature/` is deprecated.** See `literature/DEPRECATED.md`. All RRL work happens in Odin-Literature.
- RRL topic codes (`1.A`-`14.C`) follow the **old** topic outline. The new topical outline supersedes it; re-mapping is pending.
