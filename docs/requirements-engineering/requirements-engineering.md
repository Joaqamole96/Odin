# Requirements Engineering

## Metadata

```json
{
  "document-type": "reqs-eng",
  "version": 0.1.0,
  "date": "2026.08.07",
  "authors": [
    "Gabion, Stefanie S.",
    "Guevarra, Joaquin Luis T.",
    "San Jose, Alexa Joanne Paula G.",
    "Togle, Charles Nathaniel B."
  ]
}
```

## Functional Requirements

### Identity and Authenticated App Entry Module

| ID | Component | Functional Requirements |
| :--- | :--- | :--- |
| ID-01 | Registration | 1. The system shall allow users to create an account using email and password. 2. The system shall prevent submission of the registration form if any required field is empty or invalid. 3. The system shall require email verification before granting access to the application. |
| ID-02 | Login | 1. The system shall allow users to log in using email and password. 2. The system shall allow users to log in using Google Authentication. 3. The system shall deny login until valid credentials are presented. 4. The system shall detect network connectivity failures during login and display a network-required message until a stable connection is established. |
| ID-03 | Session Management | 1. The system shall preserve locally stored financial records and sync queue rows when login or network problems occur. 2. The system shall not store auth credentials, passwords, access tokens, or refresh tokens in local business tables. |

### Consent, Privacy, and Governance Module

| ID | Component | Functional Requirements |
| :--- | :--- | :--- |
| CP-01 | Thesis Disclosure | 1. The system shall inform users during onboarding that the app is a thesis project designed primarily for Filipino working young adults aged 20 to 40 in Metro Manila. 2. The system shall inform users that all users may use the app regardless of target population membership. |
| CP-02 | Consent Management | 1. The system shall allow users to give or withhold consent for their data to be used for model training or evaluation. 2. The system shall allow users to review, accept, reject, or change their consent settings at any time. 3. The system shall not use non-target-user data for model training or improvement without explicit consent. |
| CP-03 | Privacy Settings | 1. The system shall display privacy and data-use settings in an accessible location within the app. 2. The system shall distinguish between general app access and research eligibility for thesis participants. 3. The system shall cache privacy settings locally for offline display. |

### Onboarding and Profile Assessment Module

| ID | Component | Functional Requirements |
| :--- | :--- | :--- |
| OB-01 | Guided Onboarding | 1. The system shall provide a guided onboarding flow that captures the user's financial situation before providing recommendations. 2. The system shall allow users to resume onboarding if they leave the app, preserving partially completed answers. |
| OB-02 | Eligibility Capture | 1. The system shall capture target population eligibility fields (age range, work/residence location) during onboarding. 2. The system shall execute server-side profile classification during onboarding. |
| OB-03 | Profile Assignment | 1. The system shall assign a behavioral profile based on captured financial data and display an explanation of the assignment. 2. The system shall allow users to review, accept, reject, or manually change their assigned profile. 3. The system shall allow users to request profile reassessment at a later time. 4. The system shall cache the current profile assignment and explanation locally for offline display. |

### Taxonomy and Restriction Levels Module

| ID | Component | Functional Requirements |
| :--- | :--- | :--- |
| TX-01 | Category Groups | 1. The system shall provide spending and income category groups that reflect Filipino financial realities. 2. The system shall deliver system taxonomy as pull-only catalog data from the server. |
| TX-02 | User Categories | 1. The system shall allow users to create custom categories and subcategories. 2. The system shall sync user-created categories and subcategories using user CRUD sync. |
| TX-03 | Restriction Levels | 1. The system shall allow users to mark expenses as protected or fixed so that the system does not recommend reducing non-negotiable spending. 2. The system shall validate restriction-level data against downstream budget and recommendation modules. 3. The system shall sync approved restriction-level data using user CRUD sync. |

### Financial Accounts, Income Sources, and Obligations Module

| ID | Component | Functional Requirements |
| :--- | :--- | :--- |
| FA-01 | Financial Accounts | 1. The system shall allow users to create, view, edit, and delete financial accounts offline. 2. The system shall display the current balance for each financial account from local data. 3. The system shall scope all financial account data to the authenticated user. 4. The system shall sync financial account records using user CRUD sync. |
| FA-02 | Income Sources | 1. The system shall allow users to record income sources with amount, frequency, and associated account details. 2. The system shall sync income source records using user CRUD sync. |
| FA-03 | Obligations | 1. The system shall allow users to record obligations with amount, due date, frequency, and category. 2. The system shall sync obligation records using user CRUD sync. |
| FA-04 | Ownership and Sync | 1. The system shall validate foreign key references against the current user's ownership boundary before local persistence and before remote sync application. 2. The system shall use tombstone deletes for synced entities. |

### Ledger, Transactions, Templates, and Recurring Records Module

| ID | Component | Functional Requirements |
| :--- | :--- | :--- |
| LG-01 | Transaction Entry | 1. The system shall allow users to record income, expense, and transfer transactions with amount, date, category, account, and notes. 2. The system shall allow users to record transactions offline, with changes written to local SQLite immediately. |
| LG-02 | Templates | 1. The system shall allow users to create transaction templates from existing or new transactions. 2. The system shall allow users to apply a template to record a new transaction quickly. |
| LG-03 | Recurring Records | 1. The system shall allow users to set up recurring income or expense records with defined frequency and end conditions. 2. The system shall generate and queue recurring transaction entries automatically. |
| LG-04 | Transaction Management | 1. The system shall allow users to edit, delete, search, sort, and filter transactions. 2. The system shall display local balance effects immediately after transaction creation or modification. 3. The system shall sync transaction records using user CRUD sync. |

### Dashboard Module

| ID | Component | Functional Requirements |
| :--- | :--- | :--- |
| DA-01 | Financial Overview | 1. The system shall display current balance, recent activity, budget status, alerts, savings goals, debts, and forecasts on the dashboard. 2. The system shall render the dashboard from local SQLite data, not server-only endpoints. 3. The system shall update the dashboard immediately after local ledger writes. |
| DA-02 | Dashboard Degradation | 1. The system shall display stale or cached labels when downstream module data is unavailable. 2. The system shall degrade gracefully for missing downstream modules without blocking dashboard display. |

### Budgets and Allocations Module

| ID | Component | Functional Requirements |
| :--- | :--- | :--- |
| BU-01 | Budget CRUD | 1. The system shall allow users to create, view, edit, and delete budgets offline. 2. The system shall allow users to set budget amounts, date ranges, and allocation methods. 3. The system shall sync budget records using user CRUD sync. |
| BU-02 | Budget Actions | 1. The system shall allow users to activate, close, or archive budgets. 2. The system shall display budget health indicators based on spending against allocations. |
| BU-03 | Restriction-Aware Validation | 1. The system shall validate budget allocations against protected or fixed expense restrictions. 2. The system shall not recommend budget reductions for protected expense categories. |

### Budget Recommendations Module

| ID | Component | Functional Requirements |
| :--- | :--- | :--- |
| BR-01 | Recommendation Generation | 1. The system shall generate budget recommendations through server-side calculation. 2. The system shall cache recommendation results locally for offline display. |
| BR-02 | Recommendation Display | 1. The system shall display budget recommendations with an explanation of the reasoning. 2. The system shall indicate which categories are protected from cuts within the recommendation. |
| BR-03 | Recommendation Actions | 1. The system shall allow users to accept, modify, or reject each budget recommendation. 2. The system shall not apply any recommendation without explicit user acceptance. |

### Forecasts and Expected Events Module

| ID | Component | Functional Requirements |
| :--- | :--- | :--- |
| FO-01 | Forecast Generation | 1. The system shall generate and refresh LSTM forecasts through online execution. 2. The system shall cache forecast runs, series, points, explanations, and metadata locally for offline display. |
| FO-02 | Forecast Display | 1. The system shall display forecasts for total and category-level future financial activity. 2. The system shall label forecasts as personalized, fallback, or cold-start estimates so users understand forecast confidence. 3. The system shall display a four-line next-month category-group graph. |
| FO-03 | Expected Events | 1. The system shall allow users to view expected recurring events within forecast periods where included. 2. The system shall incorporate expected events into forecast display. |

### Anomalies and Overspending Module

| ID | Component | Functional Requirements |
| :--- | :--- | :--- |
| AN-01 | Anomaly Detection | 1. The system shall detect unusual spending or overspending risks using Isolation Forest anomaly detection executed on the server. 2. The system shall cache anomaly detection results locally for offline display. |
| AN-02 | Anomaly Display | 1. The system shall display anomaly alerts with an explanation of the identified unusual pattern. 2. The system shall allow users to mark unusual but intentional spending as expected. |
| AN-03 | Suppression Rules | 1. The system shall allow users to create whitelist rules to suppress repeated warnings for expected behavior. 2. The system shall sync approved whitelist and suppression rules using user CRUD sync. 3. The system shall account for culturally expected spending patterns when evaluating anomalies. |

### Alerts and Notifications Module

| ID | Component | Functional Requirements |
| :--- | :--- | :--- |
| AL-01 | Alert Inbox | 1. The system shall display cached alerts in an in-app alert inbox. 2. The system shall allow users to acknowledge, dismiss, or snooze individual alerts. 3. The system shall allow users to clear all alerts. |
| AL-02 | Notification Preferences | 1. The system shall allow users to configure notification preferences for alert categories. 2. The system shall sync notification preference updates using user CRUD sync. |
| AL-03 | Overspending Visibility | 1. The system shall display in-app overspending alerts prominently to ensure visibility. 2. The system shall allow users to mark overspending alerts as expected behavior to suppress repeated warnings. |

### Savings Goals Module

| ID | Component | Functional Requirements |
| :--- | :--- | :--- |
| SG-01 | Goal CRUD | 1. The system shall allow users to create, view, edit, and delete savings goals with target amount, current progress, target date, category/type, contribution history, and priority data. 2. The system shall sync savings goal records using user CRUD sync. |
| SG-02 | Contributions | 1. The system shall allow users to contribute to savings goals and update progress immediately in local data. 2. The system shall display cached savings projections offline. |
| SG-03 | Goal Categories | 1. The system shall support Filipino savings categories once validated through RRL, informal interviews, and SME validation. 2. The system shall allow emergency fund as a savings category with high priority, subject to final validation. |
| SG-04 | Reallocation | 1. The system shall require explicit user approval before recommending reallocation of funds between savings goals. 2. The system shall create replenishment reminders for a lower-priority savings goal after an approved reallocation reduces its funds. |

### Debt Management Module

| ID | Component | Functional Requirements |
| :--- | :--- | :--- |
| DM-01 | Debt CRUD | 1. The system shall allow users to create, view, edit, and delete debt records with lender/creditor, debt category/type, outstanding balance, payment schedule, interest/fee fields, minimum payment, due date, payment history, priority, and hardship state. 2. The system shall sync debt records using user CRUD sync. |
| DM-02 | Debt Payments | 1. The system shall allow users to log debt payments and update outstanding balance and progress immediately in local data. 2. The system shall group debts by category or type. |
| DM-03 | Repayment Strategies | 1. The system shall allow users to choose a repayment strategy (Snowball or Avalanche where validated) per debt group. 2. The system shall display cached debt projections offline. |
| DM-04 | Forecast Integration | 1. The system shall incorporate debt payment computations and payoff projections into savings forecasts, reflecting freed cash flow after a debt is paid off. |

### Reports and Analytics Module

| ID | Component | Functional Requirements |
| :--- | :--- | :--- |
| RA-01 | Report Generation | 1. The system shall allow users to generate weekly, monthly, and custom date range reports from local aggregate data. 2. The system shall display cached comparison labels when comparing across time periods. |
| RA-02 | Report Contents | 1. The system shall include spending summaries, budget-vs-actual comparisons, forecast summaries, savings progress, and debt summaries in reports. 2. The system shall support category-level summary views within reports. |
| RA-03 | Report Layout | 1. The system shall provide usable report layouts across mobile and desktop viewports. |

### Help and Problem Reporting Module

| ID | Component | Functional Requirements |
| :--- | :--- | :--- |
| HP-01 | FAQ and Help | 1. The system shall display FAQ and help content from locally bundled static content. |
| HP-02 | Problem Reporting | 1. The system shall allow users to submit a problem report with subject, message body, and registered email as reply-to. 2. The system shall submit problem reports via online-only email dispatch using the internal user ID. 3. The system shall display a network-required message when the user attempts to submit a problem report without internet access. 4. The system shall not create a support ticketing workflow, agent role, or admin dashboard for problem reports. |

### Offboarding and Account Governance Module

| ID | Component | Functional Requirements |
| :--- | :--- | :--- |
| OG-01 | Data Export | 1. The system shall allow users to export their financial data as a downloadable file. 2. The system shall require confirmation before initiating data export. 3. The system shall require internet connectivity to perform data export. |
| OG-02 | Account Deletion | 1. The system shall allow users to request account deletion with explicit confirmation of consequences before proceeding. 2. The system shall protect unsynced local changes before logout or account deletion, preventing silent data loss. 3. The system shall attempt a final sync before executing any destructive account actions. |

### Offline Sync Status, Recovery, and Discard Flows Module

| ID | Component | Functional Requirements |
| :--- | :--- | :--- |
| SY-01 | Sync Status Display | 1. The system shall display pending and failed sync operation counts in an accessible location. 2. The system shall allow users to view the specific operations that are pending or have failed. |
| SY-02 | Manual Retry and Recovery | 1. The system shall allow users to trigger manual sync retry for failed operations. 2. The system shall display an exhausted-failure recovery sheet with friendly, non-technical failure messages when retry limits are reached. 3. The system shall support paginated display of failed operations. |
| SY-03 | Discard Flows | 1. The system shall require explicit user confirmation before discarding any failed local changes. 2. The system shall mark discarded sync rows as discarded and retain them temporarily before cleanup rather than deleting immediately. 3. The system shall display safe, user-facing copy when describing sync failures and discard consequences. |
