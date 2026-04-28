# Odin — Research & Design Foundations Document

---

# PART I: TOPIC OUTLINE
> Topics define the conceptual territories the RRL must cover to justify Odin's existence and every design decision within it. Researched in order. Each topic feeds into the next.

---

## Topic 1: Spending and Budgeting Behavior of Filipino Young Professionals

**Purpose:** Establish who the users are at a behavioral level. The framing is that Filipino young professionals have documented income patterns, expenditure patterns, and budgeting behaviors that an intelligent system can model, support, and improve.

### Subtopics

- What are the documented income structures of Filipino young professionals? (stable salaried, freelance/project-based, mixed, informal)

- What time horizons do Filipino young professionals actually use for budgeting and financial planning — weekly, biweekly, semi-monthly, monthly, or other — and which are most practiced or most appropriate for this demographic?

- What are the documented expenditure patterns of Filipino young professionals, broken down where possible by income type?

- What budgeting behaviors are documented among this demographic — do they budget at all, and if so, by what method or horizon?

- What are the documented failure points in their financial management — irregular tracking, overspending, failure to plan for irregular or culturally obligated expenses?

- How does financial behavior differ between income stability types within this demographic?

- What role do culturally specific financial obligations (remittances, paluwagan, religious contributions, informal lending) play in the expenditure patterns of this demographic, and how do these differ from Western spending profiles?

- In what way does an intelligent budgeting and forecasting system — as opposed to a literacy or education intervention — directly address these behavioral patterns?

---

## Topic 2: Existing Personal Finance and Budget Management Systems

**Purpose:** Establish what systems already exist, how they work, and where they fall short — creating the documented gap that Odin fills.

### Subtopics

- What categories of PFMS/PBMS exist, and how are they typically classified in the literature?

- What are the dominant features of existing systems, and what do they do well?

- What are the documented limitations of existing systems, particularly around:
  - Manual data entry burden on users
  - Lack of intelligent or adaptive budget recommendation
  - Absence of forecasting capabilities
  - Absence of anomaly or overage detection
  - Generic, non-localized category structures
  - Static display of statistics vs. dynamic, predictive insights
  - Et cetera

- How do existing systems handle budget recommendation — rule-based, user-defined, or algorithmically driven?

- What budgeting strategies are implemented in existing systems, and how are they technically realized?

- Where is the documented gap between what existing systems offer and what an intelligent, adaptive, locally-grounded system would offer — and how does Odin fill that gap?

---

## Topic 3: Mobile-First Design in Personal Finance Systems

**Purpose:** Establish why mobile-first is the correct deployment approach for Odin, and what technical and design constraints it introduces — constraints that directly justify specific algorithm and interaction design choices downstream.

### Subtopics

- What does mobile-first mean in the context of PFMS/PBMS, and how does it differ from desktop-first or responsive web approaches?

- What is the documented evidence that mobile-first is the preferred and dominant deployment approach for personal finance tools, particularly among younger users in emerging markets like the Philippines?

- What are the documented technical constraints of mobile-first PFMS/PBMS:
  - Limited local compute for ML inference
  - Intermittent or low-bandwidth connectivity
  - Smaller screen real estate and UX simplicity requirements
  - Battery and memory constraints on mobile devices
  - Et cetera

- How do these constraints influence algorithm selection for forecasting, anomaly detection, and budget recommendation in mobile-deployed systems — specifically, what does the literature say about lightweight vs. heavyweight models in this context?

- What mobile-first design patterns are documented as effective for minimizing user input burden while maintaining data accuracy in personal finance applications?

---

## Topic 4: Budgeting Strategies and Budget Recommendation in Personal Finance Systems

**Purpose:** Establish the theoretical and technical basis for Odin's budget recommendation module. This topic surveys multiple budgeting strategies before any one algorithm is adopted — the system may distill properties from several into one unified technical configuration.

### Subtopics

- What budgeting strategies are documented in personal finance literature, and what are their core mechanics? (zero-based, envelope/category-based, pay-yourself-first, proportional/50-30-20, needs-based, hybrid approaches)

- What are the documented strengths and weaknesses of each strategy, particularly for users with:
  - Stable salaried income
  - Variable or irregular income
  - Lump-sum income followed by periods of no income
  - Et cetera

- Is there documented precedent for a system that distills multiple budgeting strategies into one unified technical configuration, and how is that achieved?

- How have existing systems technically implemented budget recommendation — purely rule-based, user-configured, or algorithmically driven?

- What algorithmic approaches to budget recommendation are documented in the literature — constraint-based optimization, multi-criteria decision making, reinforcement learning, recommendation systems, or other methods?

- What does the literature say about budget period resetting:
  - Should budgets reset to a baseline each period?
  - Should surplus carry forward, and under what conditions?
  - Does the answer differ by income stability type?
  - Et cetera

- How should a budget recommendation system behave when income data is absent, irregular, or declared as a lump sum?

- What is the minimum user input required for a budget recommendation to be accurate and useful, and what does the literature say about the tradeoff between input burden and output quality in intelligent systems?

---

## Topic 5: Budget Recommendation Algorithm

**Purpose:** Justify the specific algorithm chosen for Odin's budget recommendation module, from the most general treatment of resource allocation and optimization to the most specific application in personal finance budget distribution.

### Subtopics

- At the most general level: what class of problem is budget recommendation — optimization, ranking, prediction, or recommendation? What does the literature say?

- What algorithms have been applied to resource allocation and budget distribution problems in the literature, and with what results?

- Narrowing to personal finance: what algorithmic approaches to budget recommendation or financial resource allocation are documented in PFMS/PBMS contexts specifically?

- What are the documented tradeoffs between candidate algorithms in terms of:
  - Computational feasibility on mobile-deployed systems
  - Explainability to users (can the system explain why it recommended this allocation?)
  - Adaptability to user profile and behavioral history
  - Cold-start performance before sufficient data exists
  - Et cetera

- Why is the chosen algorithm more appropriate for Odin's specific use case than the alternatives — what data characteristics, user context, and system constraints make it the justified choice?

---

## Topic 6: Predictive Modeling in Personal Finance Systems

**Purpose:** Establish the domain-level case for spending forecasting in PFMS/PBMS — what methods have been used, how personal finance spending data is characterized, and what the literature says about temporal dependency in spending behavior.

### Subtopics

- What forecasting methods have been applied to personal finance spending data in the literature? (ARIMA, SARIMA, Random Forest, XGBoost, LightGBM, LSTM, hybrid models — with documented results for each)

- How is personal finance spending data characterized in forecasting literature — as sequential time-series, structured tabular records, or both? This characterization is the primary justification for or against LSTM.

- What does the literature say specifically about whether spending in one period sequentially influences spending in subsequent periods — i.e., is there a temporal dependency that sequence-aware models are suited to capture?

- How do mobile deployment constraints interact with forecasting algorithm selection?

- What fallback mechanisms are documented for cold-start forecasting when insufficient personal transaction history exists?

- How is per-category forecasting (needs, expenses, savings separately) handled in the literature — is it a recognized and solved problem?

---

## Topic 7: Spending Forecasting Algorithm

**Purpose:** Justify LSTM specifically as Odin's forecasting algorithm, from the most general treatment of sequence modeling to the most specific application in per-category personal finance forecasting.

### Subtopics

- At the most general level: what is LSTM, how does it work, and what class of problems is it designed to solve? (sequential dependency modeling in time-series data)

- What are LSTM's documented strengths and weaknesses relative to alternative forecasting models — where does it outperform and where does it underperform?

- Narrowing to financial data: what does the literature say about LSTM applied to household expenditure, personal spending, or budget forecasting specifically?

- How does LSTM handle per-category forecasting across
  multiple spending categories simultaneously?

- What does the literature say about LSTM's feasibility
  on mobile-deployed or resource-constrained systems —
  model compression, inference optimization, or
  lightweight LSTM variants?

- Why is LSTM more appropriate for Odin's specific use case
  than the alternatives surveyed in Topic 6 — what
  data characteristics and system context make it
  the justified choice?

---

## Topic 8: Anomaly Detection in Personal Finance Systems

**Purpose:** Establish the domain-level case for anomaly or
overage detection in PFMS/PBMS — what constitutes a detectable
financial event, what approaches have been used, and critically,
whether behavioral anomaly detection or threshold-based
overage alerting is more appropriate for Odin's defined
module scope. Opens the algorithmic question that Topic 9 closes.

**Critical unresolved question:** The team is consulting
advisors and the panel on whether the anomaly detection module
should detect behavioral deviations from personal baselines
(requires Isolation Forest or equivalent) or simply flag
budget overage events (requires threshold alerting, no ML).
This topic's literature must inform that decision.

### Subtopics

- What constitutes a detectable financial anomaly or overage
  event in personal finance contexts — how is it defined
  and taxonomized in the literature?

- What is the distinction between:
  - Threshold-based overage alerting: spending exceeds
    allocated budget for a category
  - Behavioral anomaly detection: spending deviates from
    the user's own established behavioral baseline,
    regardless of budget threshold
  And which is more appropriate for Odin's defined module scope?

- What detection approaches have been applied to personal
  finance data in the literature, and with what results?
  (rule-based threshold, statistical methods, Isolation Forest,
  One-Class SVM, Z-score, autoencoders, LOF)

- What are the documented tradeoffs between rule-based and
  algorithmic detection in terms of implementation complexity,
  explainability, accuracy, and adaptability?

- How does detection output feed into subsequent budget
  recommendation — is there documented precedent for this
  feedback loop in PFMS/PBMS?

- Are there culturally specific Filipino spending behaviors
  (large remittances, festival spending, paluwagan contributions)
  that a system should recognize as expected rather than
  anomalous or flagged?

- What does the literature say about surfacing detection
  alerts to users — format, frequency, and framing that
  minimizes alert fatigue while preserving utility?

---

## Topic 9: Anomaly Detection Algorithm

**Purpose:** Close the algorithmic question opened by Topic 8.
Justify the specific detection algorithm or mechanism chosen
for Odin's module, from the most general treatment of anomaly
detection to the most specific application in personal finance.

**Algorithm status:** PENDING — awaiting advisor, technical
advisor, and panel consultation on module scope definition.
If scope is behavioral deviation: Isolation Forest is the
current candidate. If scope is budget overage alerting:
this topic is removed and the module is reframed as
rule-based with no algorithm topic.

**What this needs to establish (if algorithmic path is taken):**

- At the most general level: what is anomaly detection as a
  machine learning problem, and what are the major families
  of approaches?

- What are Isolation Forest's documented strengths relative
  to alternatives — specifically its ability to establish
  per-user behavioral baselines without labeled training data?

- Narrowing to personal finance: what does the literature say
  about unsupervised anomaly detection applied to personal
  spending or transaction data?

- What are the documented tradeoffs in terms of computational
  feasibility on mobile systems, false positive rates,
  and user-facing explainability?

- Why is the chosen approach more appropriate for Odin's
  specific use case than alternatives?

**What this needs to establish (if rule-based path is taken):**

- This topic is removed entirely.
- Topic 8 is updated to reflect that threshold-based
  overage alerting is the documented and sufficient approach
  for Odin's defined module scope.
- The module is renamed from "anomaly detection module"
  to "budget overage alert module" in all documents.

---

## Topic 10: User Behavioral Profiling in Filipino
##            Personal Finance Contexts

**Purpose:** Establish the domain-level case for user profiling
in Odin — why profiles are necessary, why they must be
Filipino-specific, what behavioral dimensions define them,
and how profiles should evolve over time. Opens the algorithmic
question that Topic 11 closes.

### Subtopics

- What is user behavioral profiling in personal finance systems,
  and what role does it play in budget recommendation,
  forecasting fallback, and system personalization?

- Why are Western financial behavioral taxonomies insufficient
  for Filipino young professionals — what specific cultural
  and structural differences make direct application
  inappropriate?

- What Filipino-specific financial behavioral patterns are
  documented in BSP CFS, FIES, or academic literature that
  would distinguish Filipino user profiles from Western ones?

- Are there documented Filipino financial behavioral archetypes
  or segments? If not, is constructing profiles from
  institutional data (FIES, BSP CFS) a recognized and
  methodologically defensible approach?

- What behavioral dimensions are documented as meaningful
  differentiators in personal finance profiling — income
  stability, obligation weight, savings disposition,
  spending flexibility?

- What is concept drift in user behavioral modeling, and
  is drift detection an appropriate framework for
  progressively updating a user's profile as their
  behavior evolves over time?

- What behavioral signals should trigger a profile
  reassessment — spending shifts, income changes,
  obligation changes — and at what frequency or threshold?

- Should profile updates be automatic (system-driven)
  or require user confirmation before taking effect?

- What does the literature say about the cold-start problem
  in personalized financial systems, and what profile-average
  fallback approaches are documented?

---

## Topic 11: Profile Classification Algorithm

**Purpose:** Close the algorithmic question opened by Topic 10.
Justify the specific ML classification algorithm chosen to
assign users to Odin's four predefined behavioral profiles,
from the most general treatment of supervised classification
to the most specific application in financial user profiling.

**Algorithm status:** TBD — to be determined after Topic 10
literature is read. Given four predefined profile categories
(Stable-Flexible, Stable-Obligated, Variable-Flexible,
Variable-Obligated), this is a supervised classification
problem. Candidates include Logistic Regression, Decision Tree,
Random Forest, SVM, and lightweight neural classifiers.

**Panel directive:** Profile classification must use an ML
algorithm, not rule-based onboarding logic alone (Ma'am Plan,
mock defense).

### Subtopics

- At the most general level: what is supervised classification,
  and what distinguishes it from clustering? Why does Odin's
  predefined profile structure make this a classification
  rather than a clustering problem?

- What classification algorithms are documented as appropriate
  for behavioral or financial user profiling tasks?

- What features (input variables) should the classification
  algorithm use — onboarding questionnaire responses only,
  or a combination of onboarding inputs and early
  transaction history?

- How should the classifier be trained given that labeled
  user data (users with known profiles) may not exist
  at launch — what does the literature say about this
  cold-start classification problem?

- What does the literature say about progressively
  updating a classification as new behavioral data
  accumulates — is periodic re-classification, continuous
  updating, or drift detection the documented approach?

- What are the documented tradeoffs between candidate
  classifiers in terms of accuracy, interpretability,
  computational feasibility, and cold-start performance?

- Why is the chosen classifier more appropriate for Odin's
  specific use case than the alternatives?

---

## Topic 12: Expense Categorization in Filipino
##            Personal Finance Contexts

**Purpose:** Establish why Odin's expense categories are what
they are — grounded in Philippine institutional frameworks,
not arbitrary or borrowed from Western systems. Also establishes
the basis for protected categories and culturally specific
expense types.

### Subtopics

- What are the documented approaches to expense categorization
  in PFMS/PBMS — user-defined, institutionally derived,
  ML-generated, or hybrid?

- What are the documented limitations of generic Western
  expense categories when applied to Filipino spending contexts?

- What expenditure categories are defined by Philippine
  institutional frameworks:
  - PSA Family Income and Expenditure Survey (FIES)
  - BSP Consumer Finance Survey (CFS)
  And how do these map to the categories Odin implements?

- How are culturally specific Filipino expense types —
  paluwagan contributions, family remittances, religious
  obligations — recognized or treated in existing
  literature or institutional data?

- What is the documented basis for protecting certain
  expense categories from budget reduction — specifically,
  what literature or institutional source establishes
  that Essentials and Investments should have minimum
  spending floors the system should not recommend reducing?

- How do existing PFMS/PBMS serving Filipino users handle
  category design — do they use generic Western categories
  or locally derived ones — and what are the consequences
  of each approach?

- How should SSS and Pag-IBIG contributions be handled
  in expense categorization — as automatic deductions
  for regular employees (not manually entered) vs.
  voluntary inclusions for variable income users?

---

## Topic 13: Data Privacy, Security, and User Trust
##            in Personal Finance Systems

**Purpose:** Establish that Odin's handling of sensitive financial
data is grounded in documented technical standards, Philippine
regulatory requirements, and user trust considerations — including
how trust affects the quality and consistency of user-provided data.

### Subtopics

- What categories of data does a PFMS/PBMS collect, and why
  is financial data classified as particularly sensitive
  in the literature?

- What technical security measures are documented as standard
  or best practice for financial applications — encryption,
  authentication, data minimization, secure local storage?

- What does the literature say about user trust in financial
  applications — how does trust affect data sharing behavior,
  and what design decisions build or erode it?

- How do data privacy concerns specifically affect user
  willingness to log financial transactions regularly —
  connecting to Topic 14's user retention concern?

- What Philippine regulatory frameworks govern the collection,
  storage, and processing of personal financial data:
  - Republic Act 10173 (Data Privacy Act of 2012)
  - BSP regulatory guidelines on financial data
  - National Privacy Commission issuances

- What is privacy-by-design, and how has it been applied
  in comparable financial system research?

- Given that Odin uses manual transaction input with no
  banking integration, what are the specific privacy
  implications of storing self-reported financial data,
  and how should those be addressed in system design?

---

## Topic 14: User Retention and Engagement
##            in Personal Finance Systems

**Purpose:** Establish how Odin sustains the regular transaction
logging behavior that its ML modules require to function —
without gamification, which the team has explicitly excluded
from scope.

### Subtopics

- Why is regular transaction logging a prerequisite for
  LSTM forecasting and anomaly/overage detection to function
  accurately — what is the documented relationship between
  data completeness and ML model performance?

- What does the literature say about user retention and
  drop-off patterns in personal finance applications —
  when and why do users stop logging?

- What is the primary documented friction point in PFMS/PBMS
  engagement, and how has manual data entry burden been
  addressed in existing systems?

- What non-gamification retention mechanisms are documented
  as effective in PFMS/PBMS:
  - Notification and reminder design
  - Frictionless transaction entry (minimal taps,
    smart defaults, recurring expense scheduling)
  - Immediate value feedback — showing the user
    something useful right after logging
  - Progress toward user-defined financial goals

- What does the literature say about the minimum viable
  interaction frequency for a personal finance app to
  remain useful and engaging to its user?

- What is the documented relationship between perceived
  system value (accurate forecasts, useful alerts,
  clear budget health) and sustained engagement —
  is demonstrated value itself a retention mechanism?

---

## Topic 15: System Evaluation in Personal Finance
##            and Budget Management Systems

**Purpose:** Establish why ISO 25010 and SUS are the appropriate
evaluation frameworks for Odin — not just that they exist,
but that they have been used in comparable systems and are
suited to evaluating the specific quality dimensions Odin claims.

### Subtopics

- How have existing PFMS/PBMS been evaluated in the literature —
  what frameworks, metrics, and methodologies are most commonly
  used?

- What is ISO/IEC 25010:2023, what quality characteristics does
  it define, and which of those characteristics are most
  relevant to evaluating Odin as a software product?
  (functional suitability, performance efficiency, usability,
  reliability, security, maintainability, portability)

- What is the System Usability Scale (SUS), how is it
  administered, and what does it measure — and why is
  usability a critical evaluation dimension for a
  mobile-first application requiring regular user interaction?

- What does the literature say about applying ISO 25010
  and SUS together in software system evaluations —
  is this a documented and accepted combination?

- Have ISO 25010 and SUS been applied to PFMS/PBMS or
  comparable financial applications in the literature,
  and with what findings?

- What are the documented limitations of SUS and ISO 25010
  as evaluation frameworks, and how should those limitations
  be acknowledged in Odin's evaluation design?

- What sample size and respondent profile are documented
  as appropriate for SUS evaluation in comparable studies?

---

# PART II: OPEN QUESTIONS FOR SME CONSULTATION
> Questions are specific and open-ended.
> Sub-questions fragment the parent where needed.
> Post-discussion clarifications take precedence over
> defense-transcript-era assumptions.

---

## SECTION A: Budgeting Strategy and Logic

### A1. Which budgeting strategies are most relevant
###     to Filipino young professionals?

- A1a. Among zero-based budgeting, envelope budgeting,
  pay-yourself-first, and proportional allocation
  (e.g., 50/30/20), which — if any — are you aware of
  being commonly practiced or recommended for Filipino
  young professionals in your professional experience?

- A1b. Is there evidence that one strategy works better
  for stable income earners versus variable or irregular
  income earners among Filipinos?

- A1c. Is it methodologically defensible for a system to
  distill multiple budgeting strategies into one unified
  technical logic? Or does mixing strategies create
  practical problems?

---

### A2. How should budget size be determined?

- A2a. Should a budget recommendation system require the
  user to declare their income, or is it more appropriate
  to infer budget size from prior period spending history?

- A2b. What is the minimum information a system needs from
  a user to produce a reliable and useful budget
  recommendation on first use, before any transaction
  history exists?

- A2c. For a user who receives a large lump-sum income
  and then does not work for several months: how should
  a system determine periodic budget allocations?

- A2d. Is income-agnostic budgeting — constructing budgets
  entirely from prior period expense history — a
  recognized and sound approach in personal finance?

---

### A3. How should budget surplus be handled?

- A3a. If a user is allocated 20,000 PHP for a category
  but spends only 5,000 PHP, should the remainder carry
  forward, be redistributed, or reset entirely?

- A3b. Does your answer change for variable vs. stable
  income users?

- A3c. Is there a recognized scenario where surplus
  carryforward is appropriate or beneficial?

---

### A4. What time horizons are appropriate?

- A4a. Which budgeting time horizon is most commonly
  practiced or most appropriate for Filipino young
  professionals — weekly, biweekly, semi-monthly,
  or monthly?

- A4b. Should a system support multiple time horizons
  or enforce one for consistency and data quality?

- A4c. For variable income earners, is budgeting per
  income event a recognized and appropriate approach?

---

## SECTION B: User Input and System Intelligence

### B1. How intelligent should budget recommendation be?

- B1a. What level of user input is acceptable before a
  system can no longer be described as intelligent?

- B1b. Is it appropriate for a budget recommendation to
  be entirely system-generated on first use, before
  any personal transaction history exists?

- B1c. Is early inaccuracy acceptable if the system
  improves as data accumulates?

---

## SECTION C: User Profiling

### C1. Are there documented Filipino financial behavioral
###     archetypes or segments?

- C1a. Are you aware of any study, institutional report,
  or framework that segments Filipino young professionals
  into financial behavioral profiles or archetypes?

- C1b. If no such segmentation exists, is constructing
  profiles from FIES and BSP CFS data methodologically
  defensible? How would you recommend approaching that?

- C1c. The mock defense panel mandated that Odin must use
  an ML classification algorithm — not rule-based logic —
  to assign users to profiles. Given our four predefined
  profiles (Stable-Flexible, Stable-Obligated,
  Variable-Flexible, Variable-Obligated), what
  classification approach would you recommend?

- C1d. What Filipino-specific financial behaviors do you
  consider most important for a profiling system to
  explicitly account for?

---

### C2. How should profiles evolve over time?

- C2a. What behavioral signals are most meaningful
  indicators that a user's profile should be reassessed?

- C2b. Should profile updates be automatic, or should
  the system prompt user confirmation before effect?

- C2c. How frequently should profile reassessment occur?

---

## SECTION D: Anomaly Detection

### D1. What constitutes a meaningful detectable financial
###     event for Filipino young professionals?

- D1a. Should the detection module flag spending that
  exceeds allocated budget thresholds, or spending that
  deviates from the user's own behavioral baseline —
  or both? What is more actionable for the target demographic?

- D1b. Are there culturally specific Filipino spending
  behaviors that a system should recognize as expected
  rather than flagged?

- D1c. When the system flags a category as overspent,
  should the next period's allocation be automatically
  reduced, or should the system recommend and let
  the user confirm?

- D1d. What tone, framing, and level of explanation is
  appropriate when communicating a flag to Filipino users?

---

## SECTION E: Expense Categorization

### E1. What expense categories are appropriate for Odin?

- E1a. Do FIES and BSP CFS categories adequately capture
  the spending patterns of Filipino young professionals,
  or are there significant gaps for this demographic?

- E1b. How should paluwagan contributions, family
  remittances, and religious obligations be categorized —
  as subcategories or as a distinct top-level group?

- E1c. What is the professional or institutional basis
  for defining minimum spending floors for Essentials
  and Investments that the system should enforce?

- E1d. Should SSS and Pag-IBIG contributions appear in
  the user's budget, or should income input simply
  reflect take-home pay after deductions?

---

## SECTION F: Recurring Expense Scheduling

### F1. Should Odin support recurring expense scheduling?

- F1a. Is pre-scheduling recurring expenses (e.g., monthly
  rent, utility bills) a necessary feature for an
  intelligent budgeting system?

- F1b. If yes, how should a recurring expense interact
  with the budget recommendation — pre-deducted before
  discretionary allocation begins?

- F1c. If excluded, how significant a limitation is that
  for the system's practical usefulness?

---

## SECTION G: User Retention

### G1. How can Odin sustain regular transaction logging
###     without gamification?

- G1a. What is the primary reason Filipino young
  professionals stop logging transactions in personal
  finance applications?

- G1b. What non-gamification features would most
  effectively sustain regular logging behavior?

- G1c. Is demonstrated system value itself a meaningful
  retention mechanism, or are additional engagement
  features needed?

---

# PART III: RESOLVED DESIGN DECISIONS
> Post-discussion decisions supersede defense-era positions.
> Items marked PENDING await advisor/panel consultation.

| Decision | Resolution | Source |
|---|---|---|
| Primary forecasting algorithm | LSTM | Team + panel confirmation |
| Anomaly/overage detection algorithm | PENDING — awaiting advisor + panel consultation on module scope | Pending |
| Budget recommendation algorithm | TBD — determined after Topic 4 literature | Post-discussion |
| Profile classification algorithm | TBD — determined after Topic 10 literature; must be ML | Panel directive |
| Fallback forecasting basis | Behavioral profile averages | Team decision |
| Gamification | Removed from scope | Team decision |
| Deployment | Mobile-first, web for accessibility | Panel confirmation |
| Admin users | None — general users only | Panel confirmation |
| Transaction input | Manual — no banking/e-wallet integration | Panel confirmation |
| SSS/Pag-IBIG — regular employees | Auto-deducted by employer, not entered by user | Panel confirmation |
| SSS/Pag-IBIG — variable users | Voluntary — user decides whether to include | Panel confirmation |
| User types | Regular employees, freelancers, contract workers | Panel confirmation |
| Odin's differentiator | Dynamic forecasting vs. static statistics display | Panel confirmation |
| Budget modifiability | System recommends, user can adjust | Panel confirmation |
| Debt management | Avalanche + Snowball; user ultimately decides | Panel confirmation |
| Profile basis | Income type + obligation weight | SME-validated, panel-confirmed |
| Profile classification method | Must use ML algorithm — not rule-based onboarding | Panel directive (Ma'am Plan) |
| Profile update over time | Must be behavior-driven, not manual-only | Panel directive (Ma'am Plan) |
| Western profiling taxonomies | Rejected — Filipino-specific required | Team decision |
| Anomaly → budget feedback loop | OPEN — must be explicitly designed once module scope resolved | Pending |
| Recurring expense scheduling | OPEN — team decision needed | Raised by panel chair |
| Expense category basis | FIES + BSP CFS as primary institutional sources | Team decision |
| Protected category justification | OPEN — needs primary literature or institutional source | Pending |
| Budget surplus handling | OPEN — needs SME + literature validation | Post-discussion |
| Zero-based as sole strategy | OPEN — needs Topic 4 literature | Post-discussion |
| Financial literacy as core mission | Rejected — behavioral support is the mission | Post-discussion reframe |
| Data privacy regulatory framework | RA 10173 + BSP guidelines + NPC issuances | Team decision |
| Dashboard features | Income-expense forecasting, spending breakdowns, budget health | Panel confirmation |
| Evaluation frameworks | ISO/IEC 25010:2023 + SUS | Team decision |

---

# PART IV: SOURCE CANDIDATE TRACKER
> All sources pending team review unless marked [CONFIRMED].
> No source used in revised document until confirmed by at
> least one team member who has read it via the pipeline.

## Topic 1 Candidates

| ID | Citation | Bucket | Status |
|---|---|---|---|
| E-P1-01 | Lusardi & Mitchell (2023). JEP, 37(4). DOI: 10.1257/jep.37.4.137 | International | In proposal — keep |
| E-P1-02 | Cacnio & Romarate (2024). BSP Discussion Paper 2024-13 | Local | In proposal — keep |
| E-P1-03 | Dimaunahan et al. (2025). Acta Psychologica | Local | Pending DOI verification |
| E-P1-04 | Lim et al. (2024). BIO Web of Conferences | Local | Pending DOI verification |
| E-P1-05 | Rodriguez et al. (2024). Journal of Global Awareness | Local | Pending journal quality check |
| E-P1-06 | PSA FIES (2021 & 2024) | Local | Keep — primary source |
| C-P1-07 | Templa et al. (2025). Psych Educ, 38(8). DOI: 10.70838/pemj.380810 | Local | Conditional |
| C-P1-08 | Sinnewe (2023). Journal of Consumer Affairs. DOI: 10.1111/joca.12512 | International | Strong candidate |
| C-P1-09 | Sabri et al. (2023). J. Financial Services Marketing. DOI: 10.1057/s41264-023-00234-8 | International | Good candidate |
| C-P1-10 | Bai (2023). PLoS ONE, 18(11). DOI: 10.1371/journal.pone.0294466 | International | Good candidate |
| C-P1-11 | BSP Consumer Finance Survey 2021 | Local | Strong — expense category justification |

## Topic 2 Candidates

| ID | Citation | Bucket | Status |
|---|---|---|---|
| E-P2-01 | Alenazi & Sas (2024). Interacting with Computers, 37(5). DOI: 10.1093/iwc/iwae041 | International | Keep — DOI confirmed |
| E-P2-02 | Aishwarya & Hemalatha (2023). AI4IoT 2023 | International | Keep — pending DOI |
| E-P2-03 | Bhatele et al. (2023). ICACTA 2023 | International | Keep — pending DOI |
| E-P2-04 | Jadhav & Patil (2025). Communications on Applied Nonlinear Analysis | International | Keep |
| E-P2-05 | Talasila (2024). IRJET | International | PENDING — low-tier journal |
| E-P2-06 | Suria (2024). SUS/UMUX usability study | Local | Pending DOI |
| C-P2-07 | Stefanov et al. (2024). TEM Journal, 13(3). DOI: 10.18421/TEM133-34 | International | Good candidate |
| C-P2-08 | Grados-Espinoza & Velasquez-Jimenez (2025). IJETT, 73(2) | International | Good candidate |
| C-P2-09 | Jain (2024). Am. J. Computer Architecture, 11(6). DOI: 10.5923/j.ajca.20241106.01 | International | Moderate — verify journal |
| C-P2-10 | Meng et al. (2025). Journal of Consumer Behaviour. DOI: 10.1002/cb.2497 | International | Strong candidate |
| C-P2-11 | Jabar & Dayao (2025). RSIS International | Local | Conditional — verify journal |

## Algorithm-Specific Candidates (Topics 7, 9, 11)

| ID | Citation | Bucket | Status |
|---|---|---|---|
| E-A-01 | Mroua & Lamine (2023). Humanities and Social Sciences Communications | Algorithm | In proposal — keep for LSTM |
| E-A-02 | Yang (2025). Frontiers in Applied Mathematics and Statistics | Algorithm | In proposal — keep |
| E-A-03 | Xiang et al. (2023). OptIForest. IJCAI 2023 | Algorithm | In proposal — keep pending module decision |
| E-A-04 | Xiang et al. (2025). Machine Intelligence Research | Algorithm | In proposal — keep pending module decision |
| E-A-05 | Xu et al. (2023). Deep Isolation Forest. IEEE TKDE | Algorithm | In proposal — keep pending module decision |
| E-A-06 | Kumari & Kumar (2024). IET Information Security | Algorithm | In proposal — keep pending module decision |
| C-A-07 | McElfresh et al. (2023). NeurIPS 2023. DOI: 10.48550/arXiv.2305.02997 | Algorithm | Strong — tabular vs. NN landmark paper |
| C-A-08 | Hong et al. (2023). MLMI 2023. DOI: 10.1145/3635638.3635640 | Algorithm | Pending manual verification |
| C-A-09 | Naviamos & Niguidula (2024). arXiv:2407.13061 | Algorithm | Pending — preprint, assess dept. policy |

## Sources Flagged as Pending / At-Risk

| Source | Issue |
|---|---|
| Bangor et al. (2008) | Pre-2023 — cite only through recent applied work |
| Talasila (2024) IRJET | Non-peer-reviewed journal |
| Pascual & Santos-Recto (2024) ASMJ | Questionable impact profile |
| de Zarzà et al. (2024) | Relevance weakens with LSTM confirmed |
| Mireku et al. (2023) | Secondary citation issue — resolve Eloriaga et al. |
| Isolation Forest sources (E-A-03 to E-A-06) | Relevance contingent on module scope decision |

---

# PART V: SOURCE QUOTA TRACKER

| Bucket | Confirmed/Candidate | Target | Gap |
|---|---|---|---|
| Local | ~13 | 25 | ~12 |
| International | ~16 | 25 | ~9 |
| Algorithm-specific | ~9 | 25 | ~16 |
| **Total** | **~38** | **75** | **~37** |

> Algorithm-specific bucket is the largest gap.
> Priority topics for next search rounds:
> Topic 5 (budget recommendation algorithm),
> Topic 7 (LSTM), Topic 9 (anomaly/overage detection),
> Topic 11 (profile classification).

---

# PART VI: WORKFLOW NOTES

## Paper Processing Pipeline
PDF → z-converter skill (DeepSeek or equivalent) → `.md` file
→ z-summarizer skill → summary `.md` with Relevance to Odin section
→ Team member reads and checks off member_checklist
→ Source confirmed for use in revised document

## Designation Rules (affects quota counting)
- `algorithm-specific` overrides `local` or `international`
- A local paper on an algorithm counts as algorithm-specific,
  not local — impacts local quota
- Each source counts in only one bucket

## Recency Rule
- All sources must be 2023–2026
- Exception: foundational algorithm papers
  (cite only through recent applied works, not directly)
- Exception: laws and constitutions (RA 10173, etc.)
- Exception: ISO standards (ISO/IEC 25010:2023 is directly citable)

## Topic Research Order
1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11 → 12 → 13 → 14 → 15
Domain topics must be read before their corresponding
algorithm topics. Algorithm decisions finalize only after
domain topic literature is reviewed.