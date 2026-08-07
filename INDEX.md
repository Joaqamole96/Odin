# Odin Papers — Repository Index

- **Project:** Development of Odin: A Personal Finance Management Application for Filipino Working Young Adults Using Random Forest, LSTM, and Isolation Forest
- **Institution:** University of Makati | Group 4, III-DCSAD
- **Last indexed:** 2026-08-06

---

> **Ground truth:** the authoritative versions of the thesis documents live in the Google Drive folder. Copies in this repository are working mirrors and may lag behind the Drive source — verify before citing.

---

## How to Use This Index

| Need | Go to |
| :--- | :--- |
| Formal RP2 proposal, title, objectives, scope | `docs/research-proposal/Research-Proposal.md` |
| Topical outline of the thesis | `docs/thesis/topical-outline/topical-outline.md` |
| System specification (working contract) | `docs/thesis/specifications/system-spec.md` |
| Chapter 1 draft | `docs/thesis/paper/chapter-1.md` |
| Product-facing app scope, user stories, screens | `docs/thesis/system/PRD-Full-Odin-App.md` |
| RRL workspace: papers, summaries, conversions | `rrl/` |
| Survey instrument | `survey/PUEPS.md` |
| Agent navigation and standards | `AGENTS.md` |

---

## Repository Map

| Path | Purpose |
| :--- | :--- |
| `AGENTS.md` | Agent navigation guide, standards, and repository conventions. |
| `INDEX.md` | This file. Master navigation index. |
| `requirements.txt` | Python dependencies for RRL scripts. |
| `rrl/` | Review of Related Literature: PDFs, conversions, summaries, compilations, scripts. |
| `docs/` | Thesis documents, standards, and documentation. |
| `survey/` | Survey instruments. |

---

## Source-of-Truth Stack

| Layer | Source | Notes |
| :--- | :--- | :--- |
| Formal research proposal | `docs/research-proposal/Research-Proposal.md` | Authoritative for RP2 framing, objectives, scope. |
| Topical outline | `docs/thesis/topical-outline/topical-outline.md` | Thesis structure: problem, PFM systems, application, ML, metrics, evaluation. |
| System specification | `docs/thesis/specifications/system-spec.md` | Working system contract (v0.1.0, 2026.08.05). |
| Paper chapters | `docs/thesis/paper/` | Drafts such as `chapter-1.md`. |
| Product scope | `docs/thesis/system/PRD-Full-Odin-App.md` | Full-app PRD with user stories and screen descriptions. |
| RRL workspace | `rrl/` | Papers, summaries, conversions, compilations. Topic codes (1.A–14.C) still follow the old topic outline — see RRL note below. |

---

## docs/

### Research Proposal

| File | Purpose |
| :--- | :--- |
| `research-proposal/Research-Proposal.md` | Formal RP2 proposal. |
| `research-proposal/Proposal Panel's Comments & Suggestions/Panel-Comments-and-Suggestions.md` | Organized panel comments. |
| `research-proposal/Proposal Panel's Comments & Suggestions/Transcription-of-Comments-and-Suggestions.md` | Verbatim panel defense Q&A. |

### Thesis — Topical Outline

| File | Purpose |
| :--- | :--- |
| `thesis/topical-outline/topical-outline.md` | Official topical outline (v0.1.0). Supersedes the old `thesis/system/topic-outline (OLD).md`. |

### Thesis — Specifications

| File | Purpose |
| :--- | :--- |
| `thesis/specifications/system-spec.md` | Working system specification (v0.1.0). Supersedes `thesis/system/specification (OLD).md` (v4.0). |

### Thesis — Paper

| File | Purpose |
| :--- | :--- |
| `thesis/paper/chapter-1.md` | Chapter 1 draft (Introduction). |
| `thesis/paper/README.md` | Paper-copy rules (Google Drive ground truth, metadata requirement). |

### Thesis — System (working & preserved)

| File | Purpose |
| :--- | :--- |
| `thesis/system/PRD-Full-Odin-App.md` | Product requirements document. |
| `thesis/system/requirements-engineering/ODIN-REQUIREMENTS-ENGINEERING-V1.07.27.2026.md` | Functional requirements per module. |
| `thesis/system/screen-descriptions/` | 24 screen descriptions. See `00-index.md`. |
| `thesis/system/Notes.md` | Research notes on data synthesis and SME validation. |
| `thesis/system/specification (OLD).md` | Superseded technical specification (v4.0). Historical; do not use as current spec. |
| `thesis/system/topic-outline (OLD).md` | Superseded topical outline. Historical; do not use as current outline. |

### Screen Descriptions (24 screens)

| File | Screen |
| :--- | :--- |
| `thesis/system/screen-descriptions/00-index.md` | Screen set index and cross-cutting notes. |
| `thesis/system/screen-descriptions/01-login-register.md` | Login / Register |
| `thesis/system/screen-descriptions/02-onboarding-questionnaire.md` | Onboarding Questionnaire |
| `thesis/system/screen-descriptions/03-profile-result.md` | Profile Result |
| `thesis/system/screen-descriptions/04-dashboard-overview.md` | Dashboard / Overview |
| `thesis/system/screen-descriptions/05-add-transaction.md` | Add Transaction |
| `thesis/system/screen-descriptions/06-transactions-history.md` | Transactions History |
| `thesis/system/screen-descriptions/07-recurring-transactions.md` | Recurring Transactions |
| `thesis/system/screen-descriptions/08-categories-settings.md` | Categories Settings |
| `thesis/system/screen-descriptions/09-budget-setup.md` | Budget Setup |
| `thesis/system/screen-descriptions/10-budget-recommendation.md` | Budget Recommendation |
| `thesis/system/screen-descriptions/11-forecast-dashboard.md` | Forecast Dashboard |
| `thesis/system/screen-descriptions/12-alerts-anomaly-review.md` | Alerts / Anomaly Review |
| `thesis/system/screen-descriptions/13-savings-goals.md` | Savings Goals |
| `thesis/system/screen-descriptions/14-debt-accounts.md` | Debt Accounts |
| `thesis/system/screen-descriptions/15-reports-analytics.md` | Reports / Analytics |
| `thesis/system/screen-descriptions/16-settings-privacy-account.md` | Settings / Privacy |
| `thesis/system/screen-descriptions/17-user-profile.md` | User Profile |
| `thesis/system/screen-descriptions/18-financial-accounts.md` | Financial Accounts |
| `thesis/system/screen-descriptions/19-transaction-templates.md` | Transaction Templates |
| `thesis/system/screen-descriptions/20-budget-overview-categories.md` | Budget Overview / Categories |
| `thesis/system/screen-descriptions/21-notifications-alerts-center.md` | Notifications / Alerts Center |
| `thesis/system/screen-descriptions/22-installation-guide.md` | Installation Guide |
| `thesis/system/screen-descriptions/23-account-offboarding.md` | Account Offboarding |
| `thesis/system/screen-descriptions/24-help-problem-reporting.md` | Help / Problem Reporting |

### Meeting Records

| File | Purpose |
| :--- | :--- |
| `docs/group-sessions/4-24-meeting.md` | Group session notes (April 24). |

---

## rrl/

RRL is the largest and most active part of the workspace.

| Path | Purpose |
| :--- | :--- |
| `rrl/bucket/` | Raw candidate PDF intake pool. |
| `rrl/papers/` | Curated source-paper PDFs. |
| `rrl/summaries/` | Structured `_summarized.json` paper summaries. |
| `rrl/conversions/` | `_marked.md` Markdown conversions from source papers. |
| `rrl/compilations/` | Compiled topic-level review documents. |
| `rrl/scripts/` | Python utility scripts. |
| `rrl/skills/` | AI agent skill prompts. |

> **Note:** the RRL topic codes (`1.A`–`14.C`, folders `1.X`–`13.X`) follow the **old** topic outline. The new thesis topical outline is `docs/thesis/topical-outline/topical-outline.md`; re-mapping the RRL taxonomy to it is pending. See `rrl/README.md`.

### RRL Workflow

1. Place PDFs in `rrl/bucket/`
2. Convert: `python3 rrl/scripts/prepare_pdf.py rrl/bucket/`
3. Summarize: use `rrl/skills/paper-summarizer-skill.md` as AI prompt
4. Move converted/summarized files into `rrl/conversions/` and `rrl/summaries/`
5. Classify into topic folders: `rrl/compilations/{Topic}.{Letter}/`
6. Compile: `python3 rrl/scripts/compile_summaries.py -i <dir> -o <outdir>`
7. Cull: use `rrl/skills/paper-culler-skill.md` as AI prompt

Full reference: `docs/standards/rrl-workflow.md`

### RRL Naming Conventions

| Prefix | Meaning |
| :--- | :--- |
| `L--` | Local (Philippine) |
| `I--` | International |
| `A--` | Algorithm/system focus |

Full reference: `docs/standards/rrl-naming-conventions.md`

### RRL Topic Reference

| # | Topic |
| :---: | :--- |
| 1 | Filipino Young Professionals and the Financial Problem |
| 2 | Filipino Cultural Context in Personal Finance |
| 3 | Expense Categorization in Personal Finance Systems |
| 4 | Existing Personal Finance and Budget Management Systems |
| 5 | Financial Behavioral Profiling |
| 6 | Spending Forecasting |
| 7 | Budget Recommendation |
| 8 | Anomalous Spending Detection |
| 9 | Mobile-First Design |
| 10 | Data Privacy, Security, and User Trust |
| 11 | User Retention and Engagement |
| 12 | System Evaluation |
| 13 | Savings and Debt Management Algorithms |

---

## survey/

| File | Purpose |
| :--- | :--- |
| `survey/PUEPS.md` | Survey instrument. |
| `survey/PUEPS-with-notes.md` | Survey instrument with notes. |

---

## Cross-References

| Task | Use |
| :--- | :--- |
| Understand what Odin proposes to build | `docs/research-proposal/Research-Proposal.md` |
| Topical outline of the thesis | `docs/thesis/topical-outline/topical-outline.md` |
| Full app product requirements | `docs/thesis/system/PRD-Full-Odin-App.md` |
| Detailed system rules | `docs/thesis/specifications/system-spec.md` |
| Chapter drafts | `docs/thesis/paper/` |
| Plan ML/model implementation | `Odin-ML/` (separate repo: `docs/`, `scripts/`) |
| Ground synthetic data parameters | `Odin-ML/docs/data-synthesis-handoff.md` |
| Draft RRL topic sections | `rrl/compilations/` |
| Evaluate one paper's relevance | `rrl/summaries/` |
