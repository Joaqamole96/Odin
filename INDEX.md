# Odin Papers — Repository Index

- **Project:** Development of Odin: A Personal Budget Management System Using Random Forest, LSTM, and Isolation Forest Algorithms
- **Institution:** University of Makati | Group 4, III-DCSAD
- **Last indexed:** 2026-07-17

---

## How to Use This Index

| Need | Go to |
| :--- | :--- |
| Formal RP2 proposal, title, objectives, scope | `Documents/Research Proposal/Research-Proposal.md` |
| Current technical and paper specification | `Documents/Thesis/System/Specification.md` |
| Product-facing app scope, user stories, screens | `Documents/Thesis/System/PRD-Full-Odin-App.md` |
| Gap analysis between PRD and specification | `Documents/Specification-PRD-Alignment-Report.md` |
| Revision checklist for specification | `Documents/Specification-Revision-Points-Based-on-PRD.md` |
| Open specification issues and validation work | `Open-Items.md` |
| RRL topic hierarchy and search prompts | `Topic-Outline.md` |
| Chapter 1 draft | `Documents/Thesis/Paper/CHAPTER-1/purpose-and-description.md` |
| Survey instrument | `Survey/PRESURVEY - ODIN.md` |
| Data synthesis and model training handoffs | `Data/` |
| RRL source store, summaries, conversions | `RRL/` |
| Agent navigation and standards | `AGENTS.md` |

---

## Repository Map

| Path | Purpose |
| :--- | :--- |
| `AGENTS.md` | Agent navigation guide, standards, and repository conventions. |
| `INDEX.md` | This file. Master navigation index. |
| `Topic-Outline.md` | RRL topic map. Defines 13 major topics and subtopic codes. |
| `Open-Items.md` | Open validation items and unresolved specification decisions. |
| `Notes.md` | Research notes with addenda on data synthesis. |
| `Documents/` | Proposal, PRD, specification, alignment reports, screen descriptions, panel feedback. |
| `RRL/` | Review of Related Literature: PDFs, conversions, summaries, compilations, scripts. |
| `Model/` | ML model design documents, data analysis, classifier prep. |
| `Data/` | Data sources: FIES CSV, BSP/PSA data, synthetic data handoffs. |
| `Survey/` | Pre-survey instrument and notes. |
| `PDF-to-MD/` | Standalone PDF-to-Markdown converter utility. |
| `docs/standards/` | Naming conventions, workflow, summary format, commit standards. |

---

## Source-of-Truth Stack

| Layer | Source | Notes |
| :--- | :--- | :--- |
| Formal research proposal | `Documents/Research Proposal/Research-Proposal.md` | Authoritative for RP2 framing, objectives, scope. |
| Product scope | `Documents/Thesis/System/PRD-Full-Odin-App.md` | Full-app PRD with user stories and screen descriptions. |
| Technical contract | `Documents/Thesis/System/Specification.md` | Detailed system and paper specification (v4.0). |
| Reconciliation | `Documents/Specification-PRD-Alignment-Report.md` | Gaps between PRD and specification. |
| Revision plan | `Documents/Specification-Revision-Points-Based-on-PRD.md` | Editing checklist for specification alignment. |
| Issue list | `Open-Items.md` | RRL validation needs, definitions, threshold justifications. |
| RRL map | `Topic-Outline.md` | Current topic taxonomy (13 topics, codes 1.A–13.C). |

---

## Documents/

### Research Proposal

| File | Purpose |
| :--- | :--- |
| `Research Proposal/Research-Proposal.md` | Formal RP2 proposal. |
| `Research Proposal/Proposal Panel's Comments & Suggestions/Panel-Comments-and-Suggestions.md` | Organized panel comments. |
| `Research Proposal/Proposal Panel's Comments & Suggestions/Transcription-of-Comments-and-Suggestions.md` | Verbatim panel defense Q&A. |

### Thesis — System

| File | Purpose |
| :--- | :--- |
| `Thesis/System/Specification.md` | Technical specification (v4.0). |
| `Thesis/System/Specification-(OUTDATED).md` | Superseded specification. Do not use. |
| `Thesis/System/PRD-Full-Odin-App.md` | Product requirements document. |
| `Thesis/System/Model-&-Algorithm-Plan-(OUTDATED).md` | Superseded model plan. Do not use. |

### Screen Descriptions (24 screens)

| File | Screen |
| :--- | :--- |
| `Thesis/System/SCREEN-DESCRIPTIONS/01-login-register.md` | Login / Register |
| `Thesis/System/SCREEN-DESCRIPTIONS/02-onboarding-questionnaire.md` | Onboarding Questionnaire |
| `Thesis/System/SCREEN-DESCRIPTIONS/03-profile-result.md` | Profile Result |
| `Thesis/System/SCREEN-DESCRIPTIONS/04-dashboard-overview.md` | Dashboard / Overview |
| `Thesis/System/SCREEN-DESCRIPTIONS/05-add-transaction.md` | Add Transaction |
| `Thesis/System/SCREEN-DESCRIPTIONS/06-transactions-history.md` | Transactions History |
| `Thesis/System/SCREEN-DESCRIPTIONS/07-recurring-transactions.md` | Recurring Transactions |
| `Thesis/System/SCREEN-DESCRIPTIONS/08-categories-settings.md` | Categories Settings |
| `Thesis/System/SCREEN-DESCRIPTIONS/09-budget-setup.md` | Budget Setup |
| `Thesis/System/SCREEN-DESCRIPTIONS/10-budget-recommendation.md` | Budget Recommendation |
| `Thesis/System/SCREEN-DESCRIPTIONS/11-forecast-dashboard.md` | Forecast Dashboard |
| `Thesis/System/SCREEN-DESCRIPTIONS/12-alerts-anomaly-review.md` | Alerts / Anomaly Review |
| `Thesis/System/SCREEN-DESCRIPTIONS/13-savings-goals.md` | Savings Goals |
| `Thesis/System/SCREEN-DESCRIPTIONS/14-debt-accounts.md` | Debt Accounts |
| `Thesis/System/SCREEN-DESCRIPTIONS/15-reports-analytics.md` | Reports / Analytics |
| `Thesis/System/SCREEN-DESCRIPTIONS/16-settings-privacy-account.md` | Settings / Privacy |
| `Thesis/System/SCREEN-DESCRIPTIONS/17-user-profile.md` | User Profile |
| `Thesis/System/SCREEN-DESCRIPTIONS/18-financial-accounts.md` | Financial Accounts |
| `Thesis/System/SCREEN-DESCRIPTIONS/19-transaction-templates.md` | Transaction Templates |
| `Thesis/System/SCREEN-DESCRIPTIONS/20-budget-overview-categories.md` | Budget Overview / Categories |
| `Thesis/System/SCREEN-DESCRIPTIONS/21-notifications-alerts-center.md` | Notifications / Alerts Center |
| `Thesis/System/SCREEN-DESCRIPTIONS/22-installation-guide.md` | Installation Guide |
| `Thesis/System/SCREEN-DESCRIPTIONS/23-account-offboarding.md` | Account Offboarding |
| `Thesis/System/SCREEN-DESCRIPTIONS/24-help-problem-reporting.md` | Help / Problem Reporting |

### Thesis — Paper

| File | Purpose |
| :--- | :--- |
| `Thesis/Paper/CHAPTER-1/purpose-and-description.md` | Chapter 1 draft. |

### Specification Alignment

| File | Purpose |
| :--- | :--- |
| `Specification-PRD-Alignment-Report.md` | Gap analysis: PRD vs specification. |
| `Specification-Revision-Points-Based-on-PRD.md` | Revision checklist for specification. |

### Meeting Records

| File | Purpose |
| :--- | :--- |
| `Transcribed Group Sessions/4-24-meeting.md` | Group session notes (April 24). |

---

## RRL/

RRL is the largest and most active part of the workspace.

| Path | Purpose |
| :--- | :--- |
| `RRL/00_Bucket/` | Raw candidate PDF intake pool. |
| `RRL/00_Proc/` | Active processing scripts and prompts (`Z_Marker.py`, `Z_Mover.py`, `0_Summarizer.md`). |
| `RRL/01_Papers/` | Curated source-paper PDFs. |
| `RRL/02_Summaries/` | Structured `_summarized.md` paper summaries. |
| `RRL/03_Conversions/` | `_marked.md` Markdown conversions from source papers. |
| `RRL/04_Compilations/` | Compiled topic-level review documents and culling prompts. |
| `RRL/05_Archived/` | Empty — not in use. |
| `RRL/Z_Compiler.py` | Compiles summaries into a single `_Compilation.md`. |
| `RRL/Z_Counter.py` | Lists PDFs with page counts. |
| `RRL/Z_Dupechecker.py` | Finds duplicate PDFs by hash cascade. |
| `RRL/odin-app-report.md` | Q&A synthesis of Odin from repo materials. |

### RRL Workflow

1. Place PDFs in `RRL/00_Bucket/` or `RRL/00_Proc/`
2. Convert: `python3 RRL/00_Proc/Z_Marker.py [dir]`
3. Summarize: use `RRL/00_Proc/0_Summarizer.md` as AI prompt
4. Move: `python3 RRL/00_Proc/Z_Mover.py`
5. Classify into topic folders: `RRL/04_Compilations/{Topic}.{Letter}/`
6. Compile: `python3 RRL/Z_Compiler.py -i <dir> -o <outdir>`
7. Cull: use `RRL/04_Compilations/0_Culler.md` as AI prompt

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

## Model/

| Path | Purpose |
| :--- | :--- |
| `Model/MDD.md` | Model Design Document for FBP Classifier (v1.0). |
| `Model/5.X - Model Design.md` | Model design versions. |
| `Model/6.X - Model Design.md` | Model design versions. |
| `Model/8.X - Model Design.md` | Model design versions. |
| `Model/MDD - Template.md` | MDD template. |
| `Model/00_Analysis/` | PSA FIES data analysis files. |
| `Model/00_Preparation/` | Random Forest classifier prep notes. |
| `Model/01_Design/` | Training data design, synthetic data parameters. |

---

## Data/

| Path | Purpose |
| :--- | :--- |
| `Data/Family Income and Expenditure.csv` | FIES CSV data source. |
| `Data/data-synthesis-handoff.md` | Synthetic data generation pipeline. |
| `Data/BSP/` | Bangko Sentral ng Pilipinas data (Excel). |
| `Data/PSA/` | Philippine Statistics Authority data. |
| `Data/FIDashboard_1Q2023.pdf` | BSP Financial Inclusion Dashboard. |
| `Data/archive.zip` | Compressed data archive. |

---

## Survey/

| File | Purpose |
| :--- | :--- |
| `Survey/PRESURVEY - ODIN.md` | Presurvey instrument for Filipino working young adults. |
| `Survey/presurvey-pdf-with-removal-notes.md` | Presurvey with removal notes. |
| `Survey/Additional-Topics-To-Add.md` | Additional survey topics. |

---

## PDF-to-MD/

Standalone local PDF-to-Markdown converter. See `PDF-to-MD/README.md` for usage.

---

## Cross-References

| Task | Use |
| :--- | :--- |
| Understand what Odin proposes to build | `Documents/Research Proposal/Research-Proposal.md` |
| Full app product requirements | `Documents/Thesis/System/PRD-Full-Odin-App.md` |
| Detailed system rules | `Documents/Thesis/System/Specification.md` |
| Fix specification/PRD mismatches | `Documents/Specification-PRD-Alignment-Report.md` |
| Review unresolved items | `Open-Items.md` |
| Plan ML/model implementation | `Model/MDD.md`, `Model/01_Design/`, `Data/data-synthesis-handoff.md` |
| Ground synthetic data parameters | `Data/synthetic-data-parameters-handoff.md` (in `Model/01_Design/`) |
| Draft RRL topic sections | `Topic-Outline.md`, `RRL/04_Compilations/` |
| Evaluate one paper's relevance | `RRL/02_Summaries/` |
| Convert a PDF | `PDF-to-MD/README.md` or `RRL/00_Proc/Z_Marker.py` |
