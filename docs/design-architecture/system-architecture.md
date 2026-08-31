# System Architecture

## Purpose

High-level architecture for BUDI: the three subsystems, the offline-first sync model, the module breakdown, the technology stack, and the deployment topology. The authoritative and detailed specification is the [System Specification](../requirements-engineering/system-spec.md) (Section 3: System Architecture). This document provides the overview and points to the authoritative source.

## Subsystems

The system has three subsystems (see System Specification §3.1):

1. **Mobile client** — Expo/React Native Android-first application. Business data is stored locally in SQLite; the UI reads from and writes through local repositories. React Native Web is used for development and wider-layout review.
2. **Backend services** — Express API with a Supabase-backed data layer for authentication, server-side validation, sync endpoints, and online-only operations (registration, login, password flows, data export, account deletion, push token registration).
3. **ML subsystem** — FastAPI microservices serving the PFP Classifier, Forecaster, Anomaly Detector, and Budget Optimizer, wired to the backend through an API gateway and event bus.

## Offline-First Sync Model

```text
UI -> local repository -> SQLite table -> sync_queue -> runSync() -> /odin/api/sync/push
   -> apply_sync_operation() -> /odin/api/sync/pull -> SQLite convergence
```

- The UI reads from local SQLite and writes through feature repositories; network sync is background convergence, not the primary interaction path.
- The sync queue stores domain operations (e.g., "create transaction", "update category"), not stored HTTP requests.
- Conflict resolution is automatic: delete wins, then per-field last-write-wins for concurrent edits.
- Synced user-owned rows preserve `user_id`, versioning, deletion state (tombstones), timestamps, and last-sync metadata.
- All user-owned data is scoped to the authenticated user, locally and remotely; foreign keys are validated against the user's ownership boundary before persistence and before remote sync application.

Full rules are in System Specification §3.2.

## Application Modules

The application modules follow the topical outline (see System Specification §3.3):

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

These map to the product areas and the 24 screens documented in `screen-descriptions/`.

## Technology Stack

| Layer | Technology |
| :--- | :--- |
| Mobile frontend | Expo SDK 55, React Native 0.83, React Native Web 0.21, React Native Paper, NativeWind/Tailwind CSS 4 |
| Main backend | Node.js 24 LTS, Express 5.1, Supabase |
| Local storage | SQLite (local-first source of truth) |
| ML service | Python 3.14, FastAPI, PyTorch, scikit-learn |
| Package/tooling | pnpm (Node), Python virtual environment (ML) |
| Deployment | Docker containers; cloud provider TBD |

## Deployment Architecture

The ML modules and supporting services run as independent Docker containers (see System Specification §3.5 and `../ml/1_problem-statement/deployment-architecture.md`):

| Container | Port | Purpose |
| :--- | :--- | :--- |
| api-gateway | 8000 | Route and aggregate ML requests |
| pfp-classifier | 8001 | PFP classification |
| forecaster | 8002 | Forecasting |
| anomaly-detector | 8003 | Anomalous transaction detection |
| transaction-service | 8004 | Transaction ingestion and event publishing |
| budget-optimizer | 8005 | Budget optimization (definition pending) |

---

> **Authoritative source:** [System Specification — Section 3](../requirements-engineering/system-spec.md) governs. Where this document and the system spec differ, the system spec prevails.
