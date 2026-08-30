# Odin Papers — Repository Index

- **Project:** Development of BUDI: A Personalized Intelligent Finance Management Application for Filipinos Using Classification, Forecasting, Optimization, and Anomaly Detection Models for Improving Savings and Debt
- **Institution:** University of Makati | Group 4, III-DCSAD
- **Last indexed:** 2026-08-26

---

> **Ground truth:** the authoritative versions of the thesis documents live in the Google Drive folder. Copies in this repository are working mirrors and may lag behind the Drive source — verify before citing.

---

## How to Use This Index

| Need | Go to |
| :--- | :--- |
| Formal RP2 proposal, title, objectives, scope | `docs/research-proposal/Research-Proposal.md` |
| Topical outline of the thesis | `docs/planning-management/topical-outline.md` |
| System specification (working contract) | `docs/thesis/specifications/system-spec.md` |
| Chapter 1 draft | `docs/thesis/paper/chapter-1.md` |
| Product-facing app scope, user stories, screens | `docs/thesis/system/PRD-Full-Odin-App.md` |
| RRL corpus, scoring, pipeline | **Odin-Literature** (https://github.com/VibeCoders-3DCSAD/Odin-Literature) |
| Survey instrument | `survey/PUEPS.md` |
| Google Drive CLI tool | `scripts/gdrive/README.md` |
| Agent navigation and standards | `AGENTS.md` |

---

## Repository Map

| Path | Purpose |
| :--- | :--- |
| `AGENTS.md` | Agent navigation guide, standards, and repository conventions. |
| `INDEX.md` | This file. Master navigation index. |
| `docs/` | Thesis documents, standards, and documentation. |
| `docs/ml/` | ML model design, data analysis, and training documentation. |
| `google-drive/` | Local mirrors of Drive files. Gitignored. Run `fetch_drive.py` to refresh. |
| `scripts/gdrive/` | Google Drive API CLI tool (local OAuth 2.0). See `scripts/gdrive/README.md`. |
| `survey/` | Survey instruments. |
| `literature/` | **DEPRECATED.** See `literature/DEPRECATED.md`. RRL work lives in Odin-Literature. |

---

## Source-of-Truth Stack

| Layer | Source | Notes |
| :--- | :--- | :--- |
| Formal research proposal | `docs/research-proposal/Research-Proposal.md` | Authoritative for RP2 framing, objectives, scope. |
| Topical outline | `docs/planning-management/topical-outline.md` | Thesis structure: problem, PFM systems, application, ML, metrics, evaluation. |
| System specification | `docs/thesis/specifications/system-spec.md` | Working system contract. |
| Paper chapters | `docs/thesis/paper/` | Drafts such as `chapter-1.md`. |
| Product scope | `docs/thesis/system/PRD-Full-Odin-App.md` | Full-app PRD with user stories and screen descriptions. |
| RRL corpus & scoring | **Odin-Literature** | Conversions, summaries, scores, module config. |

---

## docs/

### Research Proposal

| File | Purpose |
| :--- | :--- |
| `research-proposal/Research-Proposal.md` | Formal RP2 proposal. |
| `research-proposal/Proposal Panel's Comments & Suggestions/Panel-Comments-and-Suggestions.md` | Organized panel comments. |
| `research-proposal/Proposal Panel's Comments & Suggestions/Transcription-of-Comments-and-Suggestions.md` | Verbatim panel defense Q&A. |

### Planning & Management

| File | Purpose |
| :--- | :--- |
| `planning-management/topical-outline.md` | Official topical outline. Supersedes the old `thesis/system/topic-outline (OLD).md`. |

### Thesis — Specifications

| File | Purpose |
| :--- | :--- |
| `thesis/specifications/system-spec.md` | Working system specification. Supersedes `thesis/system/specification (OLD).md` (v4.0). |

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

### ML — Model Design & Training

| Path | Purpose |
| :--- | :--- |
| `ml/README.md` | ML documentation index — phases 1-6, scripts, pipeline order. |
| `ml/TODO.md` | MDD follow-up tasks and known data/version gaps. |
| `ml/1_problem-statement/` | MDD (PFP, Forecaster, Anomaly, Budget Optimizer), feature-set, module integration, deployment architecture, synthetic-injection rules. |
| `ml/2_data-collection/` | FIES/BSP data sources. Dictionary xlsx + dependency report stay in `Odin-ML/`. |
| `ml/3_data-preprocessing/` | Preprocessing pipeline documentation. |
| `ml/4_eda/` | EDA guide (generated `eda_report.md` stays in `Odin-ML/`). |
| `ml/4.5_dimension-threshold-discovery/` | PFP dimension/threshold discovery. |
| `ml/5_feature-engineering/` | Feature engineering pipeline documentation. |
| `ml/6_model-training/` | PFP/Forecaster/Anomaly training documentation. |

### Meeting Records

| File | Purpose |
| :--- | :--- |
| `docs/group-sessions/4-24-meeting.md` | Group session notes (April 24). |

---

## literature/ (DEPRECATED)

**This directory is deprecated.** All RRL processing has moved to **Odin-Literature** (https://github.com/VibeCoders-3DCSAD/Odin-Literature).

| Path | Status |
| :--- | :--- |
| `literature/papers/` | Source PDFs (Git LFS). Pending migration to Odin-Literature. |
| `literature/bucket/` | Deprecated. Use Odin-Literature's bucket. |
| `literature/compilations/` | Deprecated. Old taxonomy. Do not use. |
| `literature/scripts/` | Deprecated. All useful scripts moved to Odin-Literature. |
| `literature/skills/` | Deprecated. Not moved. Skills form through demand in Odin-Literature. |
| `literature/DEPRECATED.md` | Full deprecation details. |
| `literature/_MIGRATION.md` | Final migration state. |

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
| Topical outline of the thesis | `docs/planning-management/topical-outline.md` |
| Full app product requirements | `docs/thesis/system/PRD-Full-Odin-App.md` |
| Detailed system rules | `docs/thesis/specifications/system-spec.md` |
| Chapter drafts | `docs/thesis/paper/` |
| Plan ML/model implementation | `docs/ml/` (design docs) + `Odin-ML/` (code) |
| Ground synthetic data parameters | `docs/ml/1_problem-statement/synthetic-injection-rules.md` |
| List/search/download Drive files | `scripts/gdrive/README.md` |
| RRL corpus and scoring | **Odin-Literature** — `scores/index.json` / `scores/report.md` |
| RRL processing workflow | **Odin-Literature** — `docs/standards/rrl-workflow.md` |
