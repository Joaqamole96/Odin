# System Specification

---

## Metadata

```json
{
  "document-type": "system-spec",
  "version": 0.2.0,
  "date": "2026.08.06",
  "authors": [
    "Gabion, Stefanie S.",
    "Guevarra, Joaquin Luis T.",
    "San Jose, Alexa Joanne Paula G.",
    "Togle, Charles Nathaniel B."
  ],
  "thesis-adviser": "Prof. Era Marie F. Gannaban",
  "technical-adviser": "Prof. Christian Michael Mansueto",
  "subject-matter-expert": "Dr. Pamela A. Go",
  "panels": {
    "chair": "Prof. Daniel Dellosa",
    "members": [
      "Prof. Jomariss Plan",
      "Prof. Janice Congzon"
    ]
  },
  "affiliation": {
    "department": "College of Computing and Information Sciences",
    "university": "University of Makati"
  }
}
```

---

## Acronyms and Abbreviations

| Acronym | Definition |
| :--- | :--- |
| PFM | Personal Finance Management |
| PFMS | Personal Finance Management System |
| PFP | Personal Financial Profile |
| ML | Machine Learning |
| NCR | National Capital Region |
| BSP | Bangko Sentral ng Pilipinas |
| FIES | Family Income and Expenditure Survey (PSA) |
| PSA | Philippine Statistics Authority |
| PUF | Public Use File |
| PUEPS | Public User Expectations and Perception Survey |
| SME | Subject Matter Expert |
| MDD | Model Design Document |
| RA 10173 | Data Privacy Act of 2012 |
| SUS | System Usability Scale |
| ISO | International Organization for Standardization |

---

## 0. Document Control

### 0.1 Change Log

| Version | Date | Author(s) | Summary of Change |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026.08.05 | Gabion, Guevarra, San Jose, Togle | Initial skeleton: Metadata, Acronyms, and section placeholders. |
| 0.2.0 | 2026.08.06 | Gabion, Guevarra, San Jose, Togle | First content fill: sections 0–13 and Appendices drafted; section numbering reordered to be sequential; change log added. |

### 0.2 Relationship to Other Documents

This specification is the main design contract for Odin. It sits above the detailed design documents and below the thesis outline:

- **Topical outline** (`../topical-outline/topical-outline.md`, v0.1.0) — defines the thesis chapter structure, including the application modules (§3.3) that this specification details.
- **Product Requirements Document** (`../system/PRD-Full-Odin-App.md`) — problem statement, solution direction, user stories, implementation decisions, and testing decisions.
- **Requirements Engineering** (`../system/requirements-engineering/ODIN-REQUIREMENTS-ENGINEERING-V1.07.27.2026.md`) — the full functional requirement statements, cited by ID in §6.
- **Screen descriptions** (`../system/screen-descriptions/00-index.md`) — 24 user-facing screens that translate this specification into buildable product surfaces.
- **Model design documents (Odin-ML)** — PFP Classifier MDD (v1.3), Forecaster MDD (v2.3), Anomaly Detector MDD, `feature-set.md` (v1.0), `module-integration.md` (v1.0), and `deployment-architecture.md` (v1.0), all under `Odin-ML/training/docs/1_problem-statement/`.
- **Survey instrument** (`../../../survey/PUEPS.md`) — Public User Expectations and Perception Survey, an input to user roles, personas, and non-functional requirements.
- **Chapter drafts** (`../paper/chapter-1.md`) — thesis narrative that motivates and evaluates this design.

The Model Design Documents are authoritative for their own modules' contracts and are referenced rather than duplicated here.

---

## 1. System Overview

### 1.1 Product Perspective

Odin is an **Android-first, offline-first personal finance management (PFM) application** for Filipino working young adults in the National Capital Region (NCR). It lets users record, review, and act on their finances even when network connectivity is unreliable, while serving as a defensible, testable system for the thesis evaluation of its intelligent finance modules.

Odin is a **decision-support system, not a licensed financial adviser**. Intelligent outputs (profiles, forecasts, budget recommendations, and anomaly alerts) must be explained in plain language, keep users in control of final decisions, and avoid shame-based financial messaging.

### 1.2 Problem Statement

Filipino working young adults manage money under real conditions that generic expense trackers do not serve well:

- Intermittent internet access.
- Variable income (freelance, gig, project-based, contractual work).
- Fixed obligations and debt pressure.
- Family support obligations and culturally patterned expenses.
- Limited time for manual transaction tracking.

Generic trackers record what already happened; they do not adequately support Filipino budgeting behavior, protected obligations, financial behavioral profiling, forward-looking cash planning, offline transaction entry, local-first dashboards, or thesis-grade evaluation of intelligent finance modules. Odin addresses both halves of this problem at once: a useful mobile-first app and a testable system for research.

### 1.3 Target Users

The thesis target population — and the model-training target — is **Filipino working young adults aged 20 to 40 who live or work in Metro Manila**. The app is usable by anyone, but only data from consenting, qualifying target users is used to train or improve AI models. The system discloses this during onboarding (see §6, CP-01).

### 1.4 Core Capabilities

The confirmed primary product areas are:

1. Identity and authenticated app entry
2. Consent, privacy, and governance
3. Onboarding and profile assessment
4. Taxonomy and restriction levels (including protected/fixed expense categories)
5. Financial accounts, income sources, and obligations
6. Ledger, transactions, templates, and recurring records
7. Dashboard
8. Budgets and allocations
9. Budget recommendations
10. Forecasts and expected events
11. Anomalies and overspending
12. Alerts and notifications
13. Savings goals
14. Debt management
15. Reports and analytics
16. Help and problem reporting
17. Offboarding and account governance
18. Offline sync status, recovery, and discard flows

### 1.5 System Context

```text
                       ┌───────────────────────────────────────────────┐
                       │                      Odin                     │
                       │                                                 │
   Filipino working    │   ┌──────────────┐   ┌──────────────────────┐   │
   young adults (20–   │   │  Odin mobile │──▶│  Backend services    │   │
   40, NCR)            │   │  app         │◀──│  (auth, sync, API)   │   │
        │              │   └──────┬───────┘   └──────────┬───────────┘   │
        │  records,    │          │                      │               │
        ▼  reviews     │   ┌──────▼───────┐   ┌──────────▼───────────┐   │
   ┌───────────────┐   │   │ Local SQLite │   │  ML subsystem         │   │
   │ External      │   │   │ + sync queue │   │  (PFP Classifier,     │   │
   │ services:     │   │   └──────────────┘   │  Forecaster, Anomaly  │   │
   │ Google Auth   │   │                      │  Detector)            │   │
   │ (TBD cloud)   │   │                      └──────────┬───────────┘   │
   └───────────────┘   │                                 │               │
                       └─────────────────────────────────┼───────────────┘
                                                         │
                       ┌─────────────────────────────────▼───────────────┐
                       │  Data sources (offline, research-only):          │
                       │  PSA FIES 2023 (NCR), BSP Consumer Finance       │
                       │  Report, synthetic personas/transactions, PUEPS  │
                       └──────────────────────────────────────────────────┘
```

The mobile app is the primary product surface. Research data sources are consumed during dataset construction (training/evaluation) and are not queried at runtime.

---

## 2. Glossary

| Term | Definition |
| :--- | :--- |
| Protected (fixed) category | An expense category a user marks so the system will not recommend reducing it (e.g., rent, tuition, family support). |
| Obligation weight | The proportion of total expenses consumed by essential and obligatory spending; one of the three PFP classifying dimensions. |
| Income stability | The consistency of a user's inflow, measured by the coefficient of variation of income; one of the three PFP classifying dimensions. |
| Financial tolerance | A user's capacity to absorb shocks, measured by emergency runway (months of expenses covered by savings); one of the three PFP classifying dimensions. |
| PFP class / octant | One of eight profile categories produced by combining the three binary dimensions (Stability × Obligation × Tolerance). |
| Cold-start | The condition of a new user with little or no transaction history, served by questionnaire-based defaults (PFP) and fallback estimates (Forecaster). |
| Sync queue | The local queue that records domain operations (transaction creation, category update, etc.) for background synchronization. |
| Sync convergence | The state reached when push and pull synchronization have brought local and remote data to the same consistent version. |
| Tombstone | A marker left in place of a deleted synced record so deletes propagate instead of being lost. |
| Archetype | A named, parameterized segment of the target population (12 total) used to generate personas. |
| Persona | An individual synthetic user generated from an archetype, with a ground-truth PFP and a transaction history. |
| Classification mode | The PFP classifier input mode: `STANDARD` (transaction history) or `QUESTIONNAIRE` (onboarding answers). |
| PFP Tier | One of the evaluated classifier designs (Tier 0 naive baseline through Tier 4 advanced learner); the final module may be rule-based or learned. |
| Walk-forward validation | Time-series validation that trains on expanding windows and evaluates one step ahead, avoiding information leakage. |
| Expected event | A known recurring income or expense the user has declared (e.g., rent, salary), incorporated into forecast display. |

---

## 3. System Architecture

### 3.1 High-Level Architecture

Odin has three subsystems:

1. **Mobile client** — an Expo/React Native application (Android-first, React Native Web for development/wider-layout review). Business data is stored locally in SQLite; the UI reads from local repositories and writes through them.
2. **Backend services** — an Express API and Supabase-backed data layer providing authentication, server-side validation, sync endpoints, and online-only operations (registration, login, password flows, data export, account deletion, push token registration).
3. **ML subsystem** — a set of FastAPI microservices serving the PFP Classifier, Forecaster, and Anomaly Detector, wired to the backend through an API gateway and event bus.

### 3.2 Offline-First Sync Model

The canonical implementation model is:

```text
UI -> local repository -> SQLite table -> sync_queue -> runSync() -> /odin/api/sync/push
   -> apply_sync_operation() -> /odin/api/sync/pull -> SQLite convergence
```

- The UI reads from local SQLite and writes through feature repositories; network sync is background convergence, not the primary interaction path.
- The sync queue stores domain operations (e.g., "create transaction", "update category"), not stored HTTP requests.
- Conflict resolution is automatic: delete wins, then per-field last-write-wins for concurrent edits.
- Duplicate operations are idempotent through operation IDs and applied-operation tracking; losing/rejected operations are logged for audit/recovery.
- Synced user-owned rows preserve `user_id`, versioning, deletion state (tombstones), timestamps, and last-sync metadata; deletes for synced entities are tombstones, not hard deletes.
- All user-owned data is scoped to the authenticated user, locally and remotely; foreign keys and related record references are validated against the user's ownership boundary before local persistence and before remote sync application.

### 3.3 Application Modules

The application modules follow the topical outline (§3.3):

| Module | Sub-modules |
| :--- | :--- |
| Login module | — |
| Registration module | — |
| Questionnaire module | — |
| User module | User account module, Financial profile module |
| Financial account module | — |
| Dashboard module | — |
| Transaction management module | Transaction entry, Transaction template, Transaction history |
| Budget management module | Budget planning, Budget tracking and health, Budget report and analysis |
| Financial intelligence module | Financial forecasting, Anomaly detection |
| Reports and statistics module | — |

These map to the 18 product areas in §1.4 and the 24 screens in the screen descriptions.

### 3.4 Technology Stack

| Layer | Technology |
| :--- | :--- |
| Mobile frontend | Expo SDK 55, React Native 0.83, React Native Web 0.21, React Native Paper, NativeWind/Tailwind CSS 4, `@expo/vector-icons` |
| Main backend | Node.js 24 LTS, Express 5.1, Supabase (`@supabase/supabase-js`) |
| Local storage | SQLite (local-first source of truth for offline-capable modules) |
| ML service | Python 3.14, FastAPI, PyTorch (LSTM/GRU/BiLSTM), scikit-learn (Random Forest, Isolation Forest, SVM, Logistic Regression), XGBoost |
| Package/tooling | pnpm (Node), Python virtual environment (ML) |
| Deployment | Docker containers; cloud provider TBD |

### 3.5 Deployment Architecture

The three ML modules and two supporting services run as independent Docker containers (see `deployment-architecture.md` v1.0):

| Container | Port | Purpose |
| :--- | :--- | :--- |
| api-gateway | 8000 | Route and aggregate ML requests |
| fbp-classifier | 8001 | PFP classification |
| forecaster | 8002 | Expense forecasting |
| anomaly-detector | 8003 | Anomalous transaction detection |
| transaction-service | 8004 | Transaction ingestion and event publishing |

Separate containers give independent scaling, independent deployment, and fault isolation. Model artifacts are stored in versioned object storage with metadata (training data hash, performance metrics, dependency versions). Each module exposes `/health`, `/ready`, and `/metrics` endpoints.

### 3.6 Integration Architecture

Following `module-integration.md` v1.0:

```text
[User App] -> [API Gateway] -> [Transaction Service]
                                    ↓
                            [Event Bus (Kafka/RabbitMQ)]
                                    ↓
                    ┌───────────────┼───────────────┐
                    ↓               ↓               ↓
            [PFP Classifier] [Forecaster]  [Anomaly Detector]
                    ↓               ↓               ↓
                    └───────────────┼───────────────┘
                                    ↓
                            [Response Aggregator]
                                    ↓
                            [User App (Response)]
```

Integration principles: loose coupling (API-based, no shared state), event-driven (modules react to transaction events), fail-safe (module failures degrade gracefully without crashing the system), and composable (outputs can be combined or used independently).

---

## 4. User Roles, Archetypes, and Personas

### 4.1 User Roles

Odin is a **single-user-account application** (1 user = 1 account; no tenant/workspace scope). Product and research roles:

| Role | Description |
| :--- | :--- |
| End user (general) | Any user of the app; records transactions, manages budgets/goals/debts, uses dashboards, reports, and sync recovery. |
| Thesis participant | A target-population user (20–40, working, Metro Manila) who gives or withholds consent for data use in model training/evaluation; eligible research data is subject to consent. |
| Thesis evaluator | Evaluates the system through SUS, ISO 25010 mapping, and model evaluation separate from UI evaluation. |
| Development team | Consumes problem reports and maintains the app and models. No admin/agent roles exist for problem reporting. |

### 4.2 Archetypes

Archetype segmentation (12 total: the 8 canonical PFP octants plus 4 edge-case archetypes) is informed by the **BSP Consumer Finance Report**; granular income/expense parameters are drawn from **PSA FIES 2023 NCR microdata**. Values below are the archetype generation targets from `Odin-ML/training/synth/archetype_summary.json`.

| ID | Archetype | Expected PFP | Avg income (₱) | Obligation ratio | Income CV | Runway (months) |
| :--- | :--- | :--- | ---: | ---: | ---: | ---: |
| A | BPO Employee, Moderate Obligations, Healthy Fund | Stable/Obligated/Tolerant | 39,993 | 0.70 | 0.10 | 5.00 |
| B | Manufacturing Worker, Heavy Obligations, No Savings | Stable/Obligated/Tight | 29,975 | 0.85 | 0.15 | 0.50 |
| C | Tech Employee, Low Obligations, Strong Savings | Stable/Flexible/Tolerant | 62,642 | 0.45 | 0.08 | 8.98 |
| D | Government Employee, Low Obligations, Minimal Savings | Stable/Flexible/Tight | 34,897 | 0.50 | 0.12 | 1.49 |
| E | Freelancer, High Obligations, Adequate Buffer | Variable/Obligated/Tolerant | 42,782 | 0.75 | 0.70 | 4.01 |
| F | Contract Worker, High Obligations, Paycheck-to-Paycheck | Variable/Obligated/Tight | 28,668 | 0.80 | 0.65 | 0.32 |
| G | Freelance Writer/VA, Low Obligations, Healthy Fund | Variable/Flexible/Tolerant | 32,620 | 0.40 | 0.60 | 7.00 |
| H | Tricycle Driver/Vendor, No Emergency Fund | Variable/Flexible/Tight | 14,002 | 0.45 | 0.80 | 1.00 |
| I | Recovering from Financial Shock, Depleted Savings | Variable/Obligated/Tight | 27,595 | 0.78 | 0.70 | 0.80 |
| J | Part-time Sales + Online Selling, Borderline Tolerance | Variable/Flexible/Tight | 22,341 | 0.55 | 0.55 | 2.50 |
| K | Telecom Employee, High Obligations Near Threshold | Stable/Obligated/Tolerant | 50,111 | 0.65 | 0.10 | 4.03 |
| L | Marketing Agency, No Savings Habit Despite Stable Income | Stable/Flexible/Tight | 42,155 | 0.50 | 0.10 | 1.01 |

### 4.3 Personas

- **Planned set:** 12,000 personas (1,000 per archetype), each with a full 12-month transaction history, per the MDDs.
- **Current synthetic run:** 300 personas (see `Odin-ML/training/synth/`), 35,568 transactions over 12 months, used for the current training runs.
- **Ground truth:** each persona's PFP label is derived deterministically from its full mature history via the score/threshold formula (§5.2); borderline cases are reserved for manual SME review.
- **Validation:** `persona-validation-list.md` and `persona-validation-list-SME-draft.md` (Odin-ML) track persona acceptance; the PUEPS survey informs persona prevalence weights so the synthetic population statistically resembles the target demographic.

---

## 5. Personal Financial Profile (PFP) Specification

### 5.1 Classifying Dimensions

A user's PFP is defined by three binary dimensions:

| Dimension | Split | Operational measure |
| :--- | :--- | :--- |
| Income stability | Stable / Variable | Coefficient of variation of income, `CV = σ(income) / μ(income)` |
| Obligation weight | Flexible / Obligated | `obligation_ratio = (essential + obligatory expenses) / total expenses` |
| Financial tolerance | Tolerant / Tight | Emergency runway: months of expenses covered by savings |

### 5.2 SME-Draft Thresholds

Thresholds are **researcher-defined and SME-validated**. The comprehensive literature review found no PFMS study that formally defines these thresholds, so the researchers define them and validate them with the SME (see `../system/Notes.md`). Current SME-draft thresholds (provisional, pending the SME validation protocol):

| Dimension | Threshold | Rationale (SME draft) |
| :--- | :--- | :--- |
| Income stability | `CV < 0.5` → Stable | Moderate income-consistency cutoff |
| Obligation weight | `ratio > 0.6` → Obligated | Essential obligations exceed 60% of expenses |
| Financial tolerance | `runway ≥ 3 months` → Tolerant | 3-month buffer before depletion |

Synthetic-data distributions of the three measures are listed in §8.5. These thresholds are calibrated on the training persona set (ROC-based cutoff selection) rather than fixed a priori, so the rule-based candidate is compared fairly against learned candidates.

### 5.3 Label Space

Combining the three dimensions yields eight PFP classes:

| Class | Income Stability | Obligation Weight | Financial Tolerance |
| :--- | :--- | :--- | :--- |
| Stable/Flexible/Tolerant | Stable | Flexible | Tolerant |
| Stable/Flexible/Tight | Stable | Flexible | Tight |
| Stable/Obligated/Tolerant | Stable | Obligated | Tolerant |
| Stable/Obligated/Tight | Stable | Obligated | Tight |
| Variable/Flexible/Tolerant | Variable | Flexible | Tolerant |
| Variable/Flexible/Tight | Variable | Flexible | Tight |
| Variable/Obligated/Tolerant | Variable | Obligated | Tolerant |
| Variable/Obligated/Tight | Variable | Obligated | Tight |

### 5.4 Classification Modes

The PFP module accepts two input modes (see PFP MDD v1.3):

| Mode | Payload | Purpose |
| :--- | :--- | :--- |
| `STANDARD` | `payload.historical_transactions` (list) | Profile from available transaction history, including partial, short-window, or inconsistent self-logged data. |
| `QUESTIONNAIRE` | `payload.questionnaire_answers` (dict) | Deterministic cold-start mapping from onboarding answers to an initial PFP when no transaction history exists. |

### 5.5 Module Output Contract

The module returns, at minimum: `prediction` (one of the eight PFP classes), `income_stability_score`, `obligation_weight_score`, `financial_tolerance_score` (each calibrated 0–1), `confidence` (0–1), and `status` (`SUCCESS`, `FAILURE`, or `FALLBACK`). The module must never throw an unhandled exception; it always returns the structured contract with fallback values if the model fails.

### 5.6 How a User's PFP Is Derived

1. A new user completes onboarding, producing an initial PFP via `QUESTIONNAIRE` mode (§5.4).
2. As transaction history accumulates, `STANDARD` mode produces a behavioral classification; the user can review, accept, reject, or manually change the assigned profile and request reassessment later (see OB-03).
3. The current assignment and its explanation are cached locally for offline display.
4. Dimension thresholds are SME-validated and calibrated on the training set; the final classifier may be rule-based (Tier 1) or learned (Tiers 2–4), selected per the criteria in §7.1.

### 5.7 Relationship to Classification Tiers

The PFP module's design is tiered (Tier 0 naive baseline through Tier 4 advanced learner). The final deployed design is the candidate selected by the pre-registered comparison in §7.1 — this specification intentionally does not pre-commit to a single algorithm.

---

## 6. Functional Requirements

The authoritative, full requirement statements are in the Requirements Engineering document (`../system/requirements-engineering/ODIN-REQUIREMENTS-ENGINEERING-V1.07.27.2026.md`), cited by ID below. This section summarizes each module.

### 6.0 Cross-cutting: Offline Sync Behavior

All offline-capable modules inherit the sync behavior of §3.2: local-first writes, queued domain operations, idempotent push, delete-wins conflict resolution, tombstone deletes, user-ownership validation before persistence and before remote application, and audited rejected/losing operations. Online-only flows (registration, login, logout, password reset/update, account deletion, data export, push token registration) are excluded from offline behavior.

### 6.1 Identity and Authenticated App Entry

| ID | Component | Requirement summary |
| :--- | :--- | :--- |
| ID-01 | Registration | Create account with email + password; block invalid/empty submissions; require email verification before access. |
| ID-02 | Login | Email/password or Google Authentication; deny until credentials valid; detect network failure and show a network-required message. |
| ID-03 | Session Management | Preserve local financial records and sync queue rows on login/network failure; never store credentials, passwords, or tokens in local business tables. |

### 6.2 Consent, Privacy, and Governance

| ID | Component | Requirement summary |
| :--- | :--- | :--- |
| CP-01 | Thesis Disclosure | Inform users during onboarding the app is a thesis project for Filipino working young adults 20–40 in Metro Manila; clarify the app is open to all users. |
| CP-02 | Consent Management | Allow give/withhold of data consent for training/evaluation; review, accept, reject, or change consent at any time; never use non-target-user data without explicit consent. |
| CP-03 | Privacy Settings | Display privacy/data-use settings accessibly; distinguish app access from research eligibility; cache privacy settings for offline display. |

### 6.3 Onboarding and Profile Assessment

| ID | Component | Requirement summary |
| :--- | :--- | :--- |
| OB-01 | Guided Onboarding | Guided flow capturing financial situation before recommendations; resume partially completed onboarding. |
| OB-02 | Eligibility Capture | Capture target-population eligibility fields (age, work/residence location); execute server-side profile classification during onboarding. |
| OB-03 | Profile Assignment | Assign and explain a behavioral profile; allow review/accept/reject/manual change; support later reassessment; cache profile + explanation offline. |

### 6.4 Taxonomy and Restriction Levels

| ID | Component | Requirement summary |
| :--- | :--- | :--- |
| TX-01 | Category Groups | Provide spending/income category groups reflecting Filipino financial realities; deliver system taxonomy as pull-only catalog data. |
| TX-02 | User Categories | Allow custom categories/subcategories; sync via user CRUD sync. |
| TX-03 | Restriction Levels | Allow marking expenses protected or fixed so non-negotiable spending is not recommended for reduction; validate restriction data downstream; sync via user CRUD sync. |

### 6.5 Financial Accounts, Income Sources, and Obligations

| ID | Component | Requirement summary |
| :--- | :--- | :--- |
| FA-01 | Financial Accounts | Create/view/edit/delete accounts offline; display local balance; scope to authenticated user; sync via user CRUD sync. |
| FA-02 | Income Sources | Record income sources with amount, frequency, and associated account; sync via user CRUD sync. |
| FA-03 | Obligations | Record obligations with amount, due date, frequency, and category; sync via user CRUD sync. |
| FA-04 | Ownership and Sync | Validate FK references against the user's ownership boundary before persistence and sync application; use tombstone deletes. |

### 6.6 Ledger, Transactions, Templates, and Recurring Records

| ID | Component | Requirement summary |
| :--- | :--- | :--- |
| LG-01 | Transaction Entry | Record income, expense, and transfer transactions with amount, date, category, account, notes; record offline with immediate local SQLite writes. |
| LG-02 | Templates | Create templates from existing/new transactions; apply a template to record a transaction quickly. |
| LG-03 | Recurring Records | Set recurring income/expense records with frequency and end conditions; generate and queue recurring entries automatically. |
| LG-04 | Transaction Management | Edit, delete, search, sort, and filter transactions; reflect local balance effects immediately; sync via user CRUD sync. |

### 6.7 Dashboard

| ID | Component | Requirement summary |
| :--- | :--- | :--- |
| DA-01 | Financial Overview | Show balance, recent activity, budget status, alerts, savings goals, debts, and forecasts; render from local SQLite, not server-only endpoints; update immediately after local writes. |
| DA-02 | Dashboard Degradation | Show stale/cached labels when downstream data is unavailable; degrade gracefully without blocking the dashboard. |

### 6.8 Budgets and Allocations

| ID | Component | Requirement summary |
| :--- | :--- | :--- |
| BU-01 | Budget CRUD | Create/view/edit/delete budgets offline; set amounts, date ranges, and allocation methods; sync via user CRUD sync. |
| BU-02 | Budget Actions | Activate, close, or archive budgets; show budget health indicators from spending against allocations. |
| BU-03 | Restriction-Aware Validation | Validate allocations against protected/fixed restrictions; never recommend reductions to protected categories. |

### 6.9 Budget Recommendations

| ID | Component | Requirement summary |
| :--- | :--- | :--- |
| BR-01 | Recommendation Generation | Generate budget recommendations via server-side calculation; cache results locally for offline display. |
| BR-02 | Recommendation Display | Explain the reasoning; indicate which categories are protected from cuts. |
| BR-03 | Recommendation Actions | Allow accept, modify, or reject per recommendation; never apply without explicit acceptance. |

### 6.10 Forecasts and Expected Events

| ID | Component | Requirement summary |
| :--- | :--- | :--- |
| FO-01 | Forecast Generation | Generate/refresh forecasts through online execution; cache runs, series, points, explanations, and metadata for offline display. |
| FO-02 | Forecast Display | Show total and category-level forecasts; label as personalized, fallback, or cold-start; show a four-line next-month category-group graph. |
| FO-03 | Expected Events | Show expected recurring events within forecast periods; incorporate into forecast display. |

### 6.11 Anomalies and Overspending

| ID | Component | Requirement summary |
| :--- | :--- | :--- |
| AN-01 | Anomaly Detection | Detect unusual spending/overspending risks (Isolation Forest executed on the server); cache results for offline display. |
| AN-02 | Anomaly Display | Explain the unusual pattern; allow users to mark intentional spending as expected. |
| AN-03 | Suppression Rules | Allow whitelist rules to suppress repeated warnings; sync approved rules via user CRUD sync; account for culturally expected spending patterns. |

### 6.12 Alerts and Notifications

| ID | Component | Requirement summary |
| :--- | :--- | :--- |
| AL-01 | Alert Inbox | Show cached alerts in-app; allow acknowledge, dismiss, snooze, and clear-all. |
| AL-02 | Notification Preferences | Configure preferences per alert category; sync via user CRUD sync. |
| AL-03 | Overspending Visibility | Show in-app overspending alerts prominently; allow marking as expected to suppress repeated warnings. |

### 6.13 Savings Goals

| ID | Component | Requirement summary |
| :--- | :--- | :--- |
| SG-01 | Goal CRUD | Create/view/edit/delete goals (target amount, progress, target date, category/type, contribution history, priority); sync via user CRUD sync. |
| SG-02 | Contributions | Contribute to goals with immediate local progress; show cached projections offline. |
| SG-03 | Goal Categories | Support Filipino savings categories once validated through RRL, interviews, and SME; emergency fund as a likely high-priority category subject to final validation. |
| SG-04 | Reallocation | Require explicit approval before recommending fund reallocation; create replenishment reminders for reduced lower-priority goals. |

### 6.14 Debt Management

| ID | Component | Requirement summary |
| :--- | :--- | :--- |
| DM-01 | Debt CRUD | Create/view/edit/delete debt records (lender, type, balance, schedule, interest, minimum payment, due date, payment history, priority, hardship state); sync via user CRUD sync. |
| DM-02 | Debt Payments | Log payments with immediate balance/progress updates; group debts by category/type. |
| DM-03 | Repayment Strategies | Choose per-group strategy (Snowball or Avalanche where validated); show cached projections offline. |
| DM-04 | Forecast Integration | Incorporate debt payments and payoff projections into savings forecasts, reflecting freed cash flow after payoff. |

### 6.15 Reports and Analytics

| ID | Component | Requirement summary |
| :--- | :--- | :--- |
| RA-01 | Report Generation | Generate weekly, monthly, and custom date-range reports from local aggregate data; show cached comparison labels. |
| RA-02 | Report Contents | Include spending summaries, budget-vs-actual, forecast summaries, savings progress, and debt summaries; support category-level views. |
| RA-03 | Report Layout | Usable across mobile and desktop viewports. |

### 6.16 Help and Problem Reporting

| ID | Component | Requirement summary |
| :--- | :--- | :--- |
| HP-01 | FAQ and Help | Display locally bundled static FAQ/help content. |
| HP-02 | Problem Reporting | Submit problem reports (subject, message body, registered email reply-to) via online-only email dispatch using the internal user ID; show network-required message offline; no ticketing/agent/admin workflow. |

### 6.17 Offboarding and Account Governance

| ID | Component | Requirement summary |
| :--- | :--- | :--- |
| OG-01 | Data Export | Export financial data as a downloadable file with explicit confirmation; requires connectivity. |
| OG-02 | Account Deletion | Request deletion with explicit confirmation of consequences; protect unsynced local changes before logout/deletion; attempt a final sync before destructive actions. |

### 6.18 Offline Sync Status, Recovery, and Discard Flows

| ID | Component | Requirement summary |
| :--- | :--- | :--- |
| SY-01 | Sync Status Display | Show pending and failed sync counts accessibly; allow viewing the specific operations. |
| SY-02 | Manual Retry and Recovery | Trigger manual retry; show an exhausted-failure recovery sheet with friendly, non-technical messages; paginate failed operations. |
| SY-03 | Discard Flows | Require explicit confirmation before discarding failed local changes; mark discarded rows and retain them temporarily before cleanup; use safe, user-facing copy. |

---

## 7. Machine Learning Model Specifications

Per the confirmed experimental methodology, this section states **candidate algorithms per model** rather than pre-committing to a single algorithm. Contracts and evaluation details are authoritative in the Model Design Documents (`Odin-ML/training/docs/1_problem-statement/module-design-document.md`).

### 7.1 PFP Classifier

| Aspect | Specification |
| :--- | :--- |
| Task | 8-class multi-class classification over the three binary PFP dimensions (§5). |
| Input | JSON per PFP MDD v1.3: `user_id`, `classification_mode` (`STANDARD`/`QUESTIONNAIRE`), and the matching payload. |
| Output | `prediction`, three calibrated dimension scores, `confidence`, `status` (`SUCCESS`/`FAILURE`/`FALLBACK`). |
| Candidate algorithms | **Tier 0** majority-class baseline; **Tier 1** deterministic rule-based (thresholds on `income_stability_cv`, `obligation_ratio`, `runway_months`, ROC-calibrated); **Tier 2** Logistic Regression (multi-class, L2); **Tier 3** Random Forest and SVM (RBF); **Tier 4** XGBoost (MLP if needed). |
| Evaluation | Macro-F1 (primary), accuracy (secondary), per-class precision/recall/F1; persona-level split (never transaction-level); identical partial-window cuts (full, 2/4/6 weeks) for every tier; time-series split (3 months train / 1 month validation). |
| Selection rule | Highest Macro-F1 within latency budget; >75% per-class accuracy; ties within a pre-registered 2-point Macro-F1 margin favor the simpler/more interpretable candidate (Tier 1 over Tiers 3–4). |
| KPIs | Macro-F1 > 0.80 (on synthetic personas); deployment-model size suitable for mobile-app context. |
| Cold start | `QUESTIONNAIRE` mode serves day-0 users deterministically; the Tier comparison applies only once `STANDARD` mode is reachable. |
| Documented result | Phase-6 training compares all tiers via 5-fold expanding-window temporal folds (`Odin-ML/training/docs/6_model-training/README.md`); final selection is pending the pre-registered decision rule. |

### 7.2 Forecaster

| Aspect | Specification |
| :--- | :--- |
| Task | Multi-step time-series forecasting of expense amounts at total, category-group, and category levels. |
| Input | JSON per Forecaster MDD v2.3: `user_id`, non-empty `historical_transactions` (amount, category, date, type), `forecast_horizon` (`WEEKLY` 7d, `SEMI_MONTHLY` 15d, `MONTHLY` 30d), `forecast_level` (`TOTAL`/`CATEGORY_GROUP`/`CATEGORY`), optional `target_categories`, optional `user_metadata`. |
| Output | `forecasts` (date, amount, metadata), echoed `forecast_level`/`forecast_horizon`, 80%/95% confidence intervals, `model_version`, `status`. |
| Candidate algorithms | **Tier 1** ARIMA / ETS / Prophet baselines; **Tier 2** XGBoost, LightGBM, Random Forest regressors (lag + calendar features); **Tier 3** PyTorch LSTM, GRU, BiLSTM (`torch.nn`), Transformer/hybrid variants if needed. |
| Features | 23 per persona-day: temporal encoding (day-of-week sin/cos, day-of-month), lags (1/7/14/15/30/60 days), rolling statistics (7/14/30-day mean and std), calendar (is_payday 15th/16th/29th–31st, days_to_payday), RFM (recency, frequency, monetary), STL decomposition (trend, seasonal, residual). |
| Evaluation | MAPE (primary) at total (<15%), category group (<20%), category (<25%) levels; R² (>0.70), RMSE (<25% of mean daily spending); time-series 70/15/15 split; walk-forward validation (expanding window, 5 folds); must beat the naive baseline by ≥20% MAPE reduction. |
| Constraints | Fixed three horizons only (weekly/semi-monthly/monthly) aligned to Philippine pay cycles; model size <500 MB; P95 inference <1 s; RAM <1 GB (GPU optional). |
| Documented result | Phase-6 training: Random Forest (Tier 2) won at MAPE 9.63% ± 0.15%, R² 0.831 ± 0.022 (~77% MAPE reduction vs naive); PyTorch LSTM/GRU/BiLSTM remain the research comparison path (`Odin-ML/training/docs/6_model-training/forecaster-training.md`). |

### 7.3 Anomaly Detector

| Aspect | Specification |
| :--- | :--- |
| Task | Per-transaction anomaly detection (unsupervised/semi-supervised) for unusual spending or overspending risk. |
| Input | Transaction data plus per-user baseline (see Anomaly Detector MDD); scored at the individual transaction level. |
| Output | Anomaly score, threshold, and an explanation of the identified unusual pattern (for display per AN-02). |
| Candidate algorithms | **Tier 0** majority-class baseline; **Tier 1** IQR per-feature detector; **Tier 2** Isolation Forest, One-Class SVM (RBF), Autoencoder (Keras 24→7→3→7→24); **Tier 3** hybrid ensemble (averaged IQR + Isolation Forest + OCSVM scores). |
| Features | 24 per transaction: baseline (income/expense mean and std, category distribution, transaction frequency, avg transaction size, category entropy, volatility index, spending concentration) and detection (amount/category/frequency/income/expense deviation, novel-category flag, amount vs category mean/std, category frequency change, amount percentile in category, days since last transaction, weekend flag, overall and category amount z-scores). |
| Anomaly types | amount_spike, category_mismatch, frequency_change, new_merchant. |
| Evaluation | PR-AUC (primary), F1 at optimal threshold, precision, recall; walk-forward validation (expanding window, 5 folds); KPI F1 ≥ 0.85, Recall ≥ 0.85, FPR ≤ 0.05. |
| Cold start | First 6 months establish the per-user baseline; no detection until baseline exists. |
| Documented result | Phase-6 training: One-Class SVM won at PR-AUC 0.1478 ± 0.0358 (416.8% improvement over baseline); Isolation Forest remains a candidate and the thesis-title algorithm (`Odin-ML/training/docs/6_model-training/anomaly-training.md`). |

---

## 8. Data Specification

### 8.1 Data Sources

| Source | Use | Role |
| :--- | :--- | :--- |
| PSA FIES 2023 (NCR microdata, Public Use File) | Income/expense totals, family size, per-capita income, decile ranking, urban/rural | Primary statistical basis for persona parameterization. |
| BSP Consumer Finance Report | Archetype segmentation (12 archetypes) | Primary basis for archetype definitions. |
| PSA national retail prices / survey metadata | Average unit prices for transaction generation | Input to transaction synthesis. |
| Synthetic personas and transactions | Labeled training/evaluation datasets | Primary training data for all three modules. |
| PUEPS pre-survey | Target-population prevalence weights; user expectations | Constrains persona prevalence and informs NFRs. |
| Prototype user data (future) | Real anonymized transactions | Secondary validation of synthetic-to-real generalization. |

### 8.2 Key Data Limitation

FIES PUFs are anonymized per RA 10173 and PSA disclosure policy and contain only aggregate/geographic fields. There is no available Filipino dataset pairing household totals with granular behavioral transaction data, so **behavioral features must be synthetically injected**. Consequently, the dataset represents the **general population of the NCR** (no age/employment linkage); this is an explicit limitation of the thesis (see `../system/Notes.md`).

### 8.3 Data Pipeline

1. Filter FIES to NCR; compute derived features (e.g., financial slack).
2. Define candidate thresholds for income stability and obligation weight; validate with the SME (blind sorting, CART rule extraction).
3. Define 12 archetypes from BSP CFS and FIES parameters.
4. Fit persona parameter distributions (multivariate LogNormal per category vector; Dirichlet for monthly allocation; Gamma for transaction amounts; Poisson for transaction counts).
5. Apply temporal weighting: expenses concentrate in the 1–2 days after paydays and before/during holidays, and shrink in the days before payday; essentials are inelastic, discretionary spending absorbs most variation.
6. Inject anomalies at fixed rates (≈3–5% overspending) for detector training.
7. Calibrate persona prevalence with PUEPS weights.
8. Export training datasets (tabular + time-series) with versioning (SHA hashes).

### 8.4 Per-Module Feature Sets

| Module | Feature set | Source |
| :--- | :--- | :--- |
| PFP Classifier | Tier 1: `income_stability_cv`, `obligation_ratio` (2); Tiers 2–4: 30 features (19 engineered + 11 raw) | `Odin-ML/training/docs/1_problem-statement/feature-set.md`; `6_model-training/README.md` §6 |
| Forecaster | 23 features per persona-day (§7.2) | `Odin-ML/training/docs/6_model-training/forecaster-training.md` |
| Anomaly Detector | 24 features per transaction (§7.3) | `Odin-ML/training/docs/6_model-training/anomaly-training.md` |

### 8.5 Dimension Distributions (Synthetic Data)

| Dimension | Mean | Std | Median | Range |
| :--- | ---: | ---: | ---: | ---: |
| income_stability_cv | 0.3874 | 0.2888 | 0.3595 | [0.0000, 0.9200] |
| obligation_ratio | 0.8800 | 0.0397 | 0.8810 | [0.5870, 1.0280] |
| runway_months | 0.7884 | 1.2686 | 0.2200 | [0.0000, 9.7200] |

Clustering analysis supports binary splits for each dimension (k = 2 sufficient). These distributions reflect the synthetic generation parameters, not real-world distributions.

### 8.6 Datasets and Splits

Splits are at the **persona level** (never transaction level) so no candidate is evaluated on a persona it was trained on. The forecaster's persona-level split follows a **70/15/15** train/validation/test ratio.

| Dataset | Split | Personas | Rows/Samples |
| :--- | :--- | ---: | ---: |
| `synth/transactions.parquet` | — | 300 | 35,568 transactions (12 months) |
| `datasets/forecaster/train.parquet` | Train (70%) | 210 | 76,650 daily rows / 1,260 monthly samples |
| `datasets/forecaster/val.parquet` | Validation (15%) | 45 | 16,425 daily rows / 270 monthly samples |
| `datasets/forecaster/test.parquet` | Test (15%) | 45 | 16,425 daily rows / 270 monthly samples |
| `datasets/anomaly/train.parquet` | Train | — | 25,135 rows @ 2.94% anomaly |
| `datasets/anomaly/val.parquet` | Validation | — | 4,980 rows @ 2.87% anomaly |
| `datasets/anomaly/test.parquet` | Test | — | 5,446 rows @ 3.23% anomaly |

### 8.7 Synthetic Data Schemas

`Odin-ML/training/synth/` contains:

| File | Contents |
| :--- | :--- |
| `personas.json` / `personas.parquet` | 300 personas with ground-truth attributes (archetype, PFP label, income/expense parameters). |
| `transactions.json` / `transactions.parquet` | Time-stamped transactions (amount, category, date, type) per persona. |
| `archetype_summary.json` | 12 archetypes with expected PFP, income, obligation ratio, income CV, and runway targets (§4.2). |
| `monthly_summaries.parquet` | Monthly aggregate income/expense summaries per persona. |
| `validation.json` | Validation record of the synthetic dataset. |

---

## 9. Non-Functional Requirements

Non-functional requirements are organized by ISO 25010 quality characteristics (see `../system/PRD-Full-Odin-App.md`, Testing Decisions; `../thesis/system/topic-outline (OLD).md` §12.A for the evaluation framing).

| ISO 25010 characteristic | Requirement |
| :--- | :--- |
| Functional suitability | Offline-capable modules must work without network; online-only flows must clearly signal connectivity requirements. Model quality is evaluated separately from UI quality. |
| Performance efficiency | Dashboard and reports read from local aggregates (no server-only reads for offline modules); ML P95 latency targets: PFP < 500 ms, Forecast < 1 s; mobile layouts usable on narrow phone widths without horizontal scrolling. |
| Usability | Manual entry friction minimized (templates, recurring records, immediate dashboard updates); intelligent outputs explained in plain language; no shame-based messaging; destructive actions require explicit confirmation. Evaluated via SUS. |
| Reliability | Offline-first sync must be idempotent, delete-wins, tombstone-based, and audited; failed operations recoverable without data loss; module failures degrade gracefully (stale/cached labels). |
| Security | Auth credentials, passwords, access tokens, and refresh tokens never stored in local business tables; all user-owned data scoped to the authenticated user; ownership checks on every read and write; TLS 1.3 in transit, AES-256 at rest; no raw exception messages or technical errors shown to users; no PII in client-side storage keys. |
| Maintainability | Modules loosely coupled via APIs and events; model artifacts versioned with training-data hashes and metadata; drift monitoring (PSI, ADWIN/CUSUM) and retraining triggers defined. |
| Portability | Android-first with web review flows; ML service deployable as Docker containers; model artifacts portable (`.joblib`, `.pth`). |
| Privacy | Consent management per RA 10173; thesis disclosure during onboarding; research eligibility distinct from app access; privacy settings cached locally; data export available; account deletion with explicit confirmation and final-sync safeguard. |

---

## 10. External Interfaces

### 10.1 Sync API

- `POST /odin/api/sync/push` — push queued domain operations (idempotent; applied-operation tracking; ownership validation).
- `POST /odin/api/sync/pull` — pull remote changes and tombstones for convergence.

### 10.2 ML Service API (via API Gateway)

| Endpoint | Service |
| :--- | :--- |
| `POST /api/v1/fbp/classify` (+ `/batch`, `/user/{id}/history`, `/user/{id}/latest`) | PFP Classifier |
| `POST /api/v1/forecast/predict` (+ `/batch`, `/user/{id}/history`) | Forecaster |
| `POST /api/v1/anomaly/detect` (+ `/batch`, `/user/{id}/alerts`, `/user/{id}/baseline`) | Anomaly Detector |
| `POST /api/v1/analyze`, `GET /api/v1/user/{id}`, `POST /api/v1/classify`, `POST /api/v1/forecast` | Gateway convenience/aggregation |

Each service exposes `/health`, `/ready`, and `/metrics`.

### 10.3 Authentication

Google Authentication (OAuth) for login, in addition to email/password with email verification.

### 10.4 Data Formats

- Transaction event and request/response payloads use JSON (schemas in `module-integration.md` v1.0).
- Model artifacts: `.joblib` (scikit-learn), `.pkl`/`.joblib` (preprocessing pipelines), `.pth` (PyTorch weights).
- Data export: downloadable file of the user's financial data (requires connectivity and explicit confirmation).

### 10.5 Device and Platform

- Android is the primary supported platform; iOS development/testing/distribution is out of scope.
- Web access may exist for development or wider-layout review flows; mobile remains the primary product experience.
- ML services run as Docker containers on a cloud provider to be determined.

---

## 11. Constraints and Assumptions

### 11.1 Scope Boundaries (Out of Scope)

- iOS-specific development, testing, or distribution.
- Bank API, e-wallet API integration, or automatic transaction import.
- OCR/receipt scanning or external CSV/spreadsheet import (unless separately approved).
- Licensed financial, investment, retirement, legal, or tax advice; automated bill payment; credit-score monitoring.
- Full production-grade fraud detection or third-party merchant enrichment.
- Public marketplace deployment beyond thesis needs.
- Multi-tenant/organization/workspace architecture (single-user-account model).
- Admin dashboards, agent roles, or ticketing workflows for problem reporting.
- Final Top 10 Filipino savings/debt category sets, reallocation algorithms, or debt-strategy defaults before RRL, interviews, and SME validation.

### 11.2 Constraints

- **Data representativeness:** the dataset represents the general NCR population because PUFs are anonymized (stripped of age/employment identifiers); training-inference covariate shift is mitigated by calibration weights and sensitivity analysis but remains a limitation.
- **Thresholds:** income-stability and obligation-weight thresholds are researcher-defined (literature gap) and must be validated by the SME.
- **Synthetic-data dependence:** all KPIs are measured on synthetic personas; synthetic-to-real generalization is untested until prototype-user data exists. Injected behavioral features are based on RRL and expert judgment, a documented threat to validity.
- **Offline-first:** business data flows must remain offline-capable; auth and governance flows are online-only.
- **Android-first:** mobile layout is primary; narrow viewports must remain usable.
- **Cloud provider and infrastructure details** (provider, orchestration) are TBD.

### 11.3 Assumptions

- Target users are Filipino working young adults aged 20–40 living or working in Metro Manila.
- All users may use the app, but only consenting, qualifying target-user data is used for model training/evaluation.
- Expense patterns concentrate around paydays and holidays, with essentials largely inelastic (see §8.3).
- Module outputs are decision support, not licensed financial advice; users keep final control.
- Savings and debt category standards remain provisional until SME/RRL validation.

---

## 12. Dependencies

### 12.1 Service Dependencies

```text
Mobile app
   └── API Gateway ──▶ Transaction Service ──▶ Event Bus
                                                     ├──▶ PFP Classifier
                                                     ├──▶ Forecaster
                                                     └──▶ Anomaly Detector
Event Bus ──▶ Response Aggregator ──▶ Mobile app
```

- The PFP Classifier, Forecaster, and Anomaly Detector depend on the Transaction Service's transaction events (PFP: 3 months of history; Forecaster: 6 months; Anomaly: per transaction, after a 6-month baseline).
- The API Gateway aggregates module outputs for combined analysis; a module failure must not block the others (graceful degradation).
- The Forecaster and Budget modules consume each other's outputs; the PFP module consumes onboarding/questionnaire data for cold start; Debt Management feeds freed-cash-flow inputs into savings forecasts.

### 12.2 Data Dependencies

| Module | Depends on |
| :--- | :--- |
| PFP Classifier | Onboarding questionnaire answers (`QUESTIONNAIRE` mode), transaction history (`STANDARD` mode), SME-validated thresholds. |
| Forecaster | Daily aggregated expenses by category, calendar/payday features, user metadata for cold start. |
| Anomaly Detector | Transaction stream and per-user baseline; whitelist/suppression rules and culturally expected spending inputs. |

### 12.3 Document Dependencies

- This specification depends on the MDDs, PRD, and Requirements Engineering document for authoritative detail (§0.2).
- Feature sets depend on the shared synthetic data pipeline; module features are triplicated per module at feature engineering.
- The critical path for ML work: shared data phase → triplicated feature engineering → parallel module training (PFP 41 days, Forecaster 44 days, Anomaly 41 days).

---

## 13. Appendices

### A. References

- Odin thesis: *Development of Odin: A Personal Finance Management Application for Filipino Working Young Adults Using Random Forest, LSTM, and Isolation Forest* — topical outline (`../topical-outline/topical-outline.md`).
- Full Odin App PRD (`../system/PRD-Full-Odin-App.md`).
- Odin Requirements Engineering v1.07.27.2026 (`../system/requirements-engineering/ODIN-REQUIREMENTS-ENGINEERING-V1.07.27.2026.md`).
- Screen descriptions (`../system/screen-descriptions/00-index.md`).
- System notes and addenda (`../system/Notes.md`).
- Public User Expectations and Perception Survey (`../../../survey/PUEPS.md`).
- Model design documents and training documentation (`Odin-ML/training/docs/`): PFP MDD v1.3, Forecaster MDD v2.3, Anomaly Detector MDD, `feature-set.md` v1.0, `module-integration.md` v1.0, `deployment-architecture.md` v1.0, `dimension-threshold-candidates.md`, Phase-6 training docs (`6_model-training/`), and synthetic data (`training/synth/`).
- Preserved historical reference: `specification (OLD).md` (v4.0) and `topic-outline (OLD).md` under `../system/`.

### B. Revision History Detail

| Version | Date | Section(s) affected | Change detail |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026.08.05 | All | Skeleton created with Metadata, Acronyms, and section placeholders. |
| 0.2.0 | 2026.08.06 | All | Drafted full content for sections 0–13 and Appendices; renumbered sections sequentially (Document Control remains §0); added change log and references; bumped version and date. |
