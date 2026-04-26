# Odin — Research & Design Foundations Document
> **Version:** Post-Defense + Post-Discussion
> **Living document.** All items are open unless marked [RESOLVED].
> **Precedence rule:** Decisions from the post-defense team discussion
> supersede any conflicting position from the defense transcript.

---

# PART I: PILLAR STRUCTURE
> Pillars define the conceptual territories the RRL must cover
> to justify Odin's existence and every design decision within it.
> Researched in order. Each pillar feeds into the next.
> Pillar structure and establishment requirements reflect
> post-discussion refinements — not the defense transcript state.

---

## Pillar 1: Spending and Budgeting Behavior of Filipino Young Professionals

**Purpose:** Establish who the users are at a behavioral level.
The framing is NOT "Filipinos lack financial literacy" — that
positions Odin as an education app. The framing IS "Filipino young
professionals have documented income patterns, expenditure patterns,
and budgeting behaviors that an intelligent system can model,
support, and improve." Financial literacy is context, not the problem.

**What this needs to establish:**

- What are the documented income structures of Filipino young
  professionals?
  (stable salaried, freelance/project-based, mixed, informal)

- What time horizons do Filipino young professionals actually
  use for budgeting and financial planning — weekly, biweekly,
  semi-monthly, monthly, or other — and which are most
  practiced or most appropriate for this demographic?

- What are the documented expenditure patterns of Filipino
  young professionals, broken down where possible by income type?

- What budgeting behaviors are documented among this demographic —
  do they budget at all, and if so, by what method or horizon?

- What are the documented failure points in their financial
  management — irregular tracking, overspending, failure to plan
  for irregular or culturally obligated expenses?

- How does financial behavior differ between income stability
  types within this demographic?

- What role do culturally specific financial obligations
  (remittances, paluwagan, religious contributions, informal
  lending) play in the expenditure patterns of this demographic,
  and how do these differ from Western spending profiles?

- In what way does an intelligent budgeting and forecasting
  system — as opposed to a literacy or education intervention —
  directly address these behavioral patterns?

---

## Pillar 2: Existing Personal Finance and Budget Management Systems

**Purpose:** Establish what systems already exist, how they work,
and where they fall short — creating the documented gap that Odin fills.

**What this needs to establish:**

- What categories of PFMS/PBMS exist, and how are they
  typically classified in the literature?

- What are the dominant features of existing systems,
  and what do they do well?

- What are the documented limitations of existing systems,
  particularly around:
  - Manual data entry burden on users
  - Lack of intelligent or adaptive budget recommendation
  - Absence of forecasting capabilities
  - Absence of anomaly detection
  - Generic, non-localized category structures
  - Static display of statistics vs. dynamic, predictive insights

- How do existing systems handle budget recommendation —
  rule-based, user-defined, or algorithmically driven?

- What budgeting strategies are implemented in existing systems,
  and how are they technically realized?

- Where is the documented gap between what existing systems offer
  and what an intelligent, adaptive, locally-grounded system
  would offer — and how does Odin fill that gap?

---

## Pillar 3: Mobile-First Design in Personal Finance Systems

**Purpose:** Establish why mobile-first is the correct deployment
approach for Odin, and what technical and design constraints it
introduces — constraints that directly justify specific algorithm
and interaction design choices downstream.

**What this needs to establish:**

- What does mobile-first mean in the context of PFMS/PBMS,
  and how does it differ from desktop-first or responsive
  web approaches?

- What is the documented evidence that mobile-first is the
  preferred and dominant deployment approach for personal
  finance tools, particularly among younger users in
  emerging markets like the Philippines?

- What are the documented technical constraints of
  mobile-first PFMS/PBMS:
  - Limited local compute for ML inference
  - Intermittent or low-bandwidth connectivity
  - Smaller screen real estate and UX simplicity requirements
  - Battery and memory constraints on mobile devices

- How do these constraints influence algorithm selection
  for forecasting and anomaly detection in mobile-deployed
  systems — specifically, what does the literature say about
  lightweight vs. heavyweight models in this context?

- What mobile-first design patterns are documented as effective
  for minimizing user input burden while maintaining data
  accuracy in personal finance applications?

---

## Pillar 4: Budgeting Strategies and Budget Recommendation
##           in Personal Finance Systems

**Purpose:** Establish the theoretical and technical basis for
Odin's budget recommendation module. This pillar must survey
multiple budgeting strategies before any one is adopted —
the system may distill properties from several into one unified
technical configuration.

**What this needs to establish:**

- What budgeting strategies are documented in personal finance
  literature, and what are their core mechanics?
  (zero-based, envelope/category-based, pay-yourself-first,
  proportional/50-30-20, needs-based, hybrid approaches)

- What are the documented strengths and weaknesses of each
  strategy, particularly for users with:
  - Stable salaried income
  - Variable or irregular income
  - Lump-sum income followed by periods of no income

- Is there documented precedent for a system that distills
  multiple budgeting strategies into one unified technical
  configuration, and how is that done?

- How have existing systems technically implemented budget
  recommendation — purely rule-based, user-configured,
  or algorithmically adaptive?

- What does the literature say about budget period resetting:
  - Should budgets reset to a baseline each period?
  - Should surplus carry forward, and under what conditions?
  - Does the answer differ by income stability type?

- How should a budget recommendation system behave when
  income data is absent, irregular, or declared as a lump sum?

- What is the minimum user input required for a budget
  recommendation to be accurate and useful, and what does
  the literature say about the tradeoff between input
  burden and output quality?

- What does the literature say about budget recommendation
  as an intelligent, automated feature — not just a
  user-configured tool?

---

## Pillar 5: Predictive Modeling in Personal Finance Systems

**Purpose:** Establish the basis for Odin's LSTM forecasting
module — what methods exist, how personal finance spending data
is characterized, and why LSTM is the justified choice.

**What this needs to establish:**

- What forecasting methods have been applied to personal
  finance spending data in the literature?
  (ARIMA, SARIMA, Random Forest, XGBoost, LightGBM,
  LSTM, hybrid models — with documented results for each)

- How is personal finance spending data characterized in
  forecasting literature — as sequential time-series,
  structured tabular records, or both? This characterization
  is the primary justification for or against LSTM.

- What does the literature say specifically about whether
  spending in one period sequentially influences spending
  in subsequent periods — i.e., is there a temporal
  dependency that LSTM is suited to capture?

- What are the documented strengths and weaknesses of LSTM
  applied to personal finance or household expenditure
  forecasting — where does it perform well and where
  does it underperform?

- How do mobile deployment constraints (from Pillar 3)
  interact with LSTM selection — is LSTM feasible on
  a mobile-deployed system, and what optimizations
  are documented?

- What fallback mechanisms are documented for cold-start
  forecasting when insufficient personal transaction
  history exists?

- How is per-category forecasting (needs, expenses, savings
  separately) handled in the literature — is it a
  recognized and solved problem?

---

## Pillar 6: Anomaly Detection in Personal Finance Systems

**Purpose:** Establish the basis for Odin's anomaly detection
module — what financial anomalies are, how they're detected,
and whether Isolation Forest or a rule-based approach is
more appropriate for Odin's specific use case.

**What this needs to establish:**

- What constitutes a financial anomaly in personal finance
  contexts — how is it defined and taxonomized in the
  literature?

- What is the distinction between threshold-based alerting
  ("spent more than X in category Y") and behavioral
  deviation detection ("spent unusually relative to this
  user's own established pattern")? Which is more
  appropriate for Odin's use case?

- What anomaly detection approaches have been applied to
  personal finance data, and with what results?
  (rule-based threshold, statistical, Isolation Forest,
  One-Class SVM, autoencoders, LOF)

- What are the documented tradeoffs between rule-based and
  algorithmic anomaly detection in terms of:
  - Implementation complexity and explainability
  - Accuracy and false positive rates
  - Adaptability to individual behavioral baselines

- How does anomaly detection output feed into subsequent
  budget recommendation — is there documented precedent
  for this feedback loop in PFMS/PBMS?

- What does the literature say about surfacing anomaly
  alerts to users — format, frequency, and framing
  that minimizes alert fatigue while preserving utility?

- Are there culturally specific Filipino spending behaviors
  (large one-time remittances, festival spending, paluwagan
  contributions) that a system should recognize as expected
  rather than anomalous?

---

## Pillar 7: User Behavioral Profiling in Filipino
##           Personal Finance Contexts

**Purpose:** Establish the basis for Odin's four-profile
behavioral classification system — why profiles are necessary,
why they must be Filipino-specific, what ML algorithm should
classify users into them, and how profiles should evolve
over time.

**Note:** This pillar gained significant new requirements from
the mock defense. The panel mandated that profile classification
must use an ML algorithm, not rule-based onboarding alone.
Progressive behavioral tracking that updates profiles over time
was also mandated.

**What this needs to establish:**

- What is user behavioral profiling in personal finance systems,
  and what role does it play in budget recommendation,
  forecasting fallback, and system personalization?

- Why are Western financial behavioral taxonomies insufficient
  for Filipino young professionals — what specific
  cultural and structural differences make direct application
  inappropriate?

- What Filipino-specific financial behavioral patterns are
  documented in BSP CFS, FIES, or academic literature that
  would distinguish Filipino user profiles from Western ones?

- Are there documented Filipino financial behavioral archetypes
  or segments? If no such segmentation exists in the literature,
  is constructing profiles from institutional data (FIES,
  BSP CFS) a recognized and methodologically defensible approach?

- Given that Odin has four predefined profile categories
  (Stable-Flexible, Stable-Obligated, Variable-Flexible,
  Variable-Obligated), what supervised classification algorithms
  are documented as appropriate for classifying users into
  predefined financial behavioral categories?

- What features (input variables) should the classification
  algorithm use — onboarding questionnaire inputs only,
  or a combination of onboarding inputs and early
  transaction history?

- How should the classification algorithm be trained given
  that labeled user data may not exist at launch — what
  does the literature say about this cold-start classification
  problem?

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
  fallback approaches are supported?

---

## Pillar 8: Expense Categorization in Filipino
##           Personal Finance Contexts

**Purpose:** Establish why Odin's expense categories are what
they are — grounded in Philippine institutional frameworks,
not arbitrary or borrowed from Western systems. Also establishes
the basis for protected categories.

**What this needs to establish:**

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
  spending floors that the system should not recommend
  reducing below?

- How do existing PFMS/PBMS serving Filipino users
  handle category design — do they use generic Western
  categories (a documented limitation) or locally
  derived ones — and what are the consequences of
  each approach?

- How should SSS and Pag-IBIG contributions be handled
  in expense categorization — as automatic deductions
  for regular employees (not manually entered) vs.
  voluntary inclusions for variable income users?

---

## Pillar 9: Data Privacy, Security, and User Trust
##           in Personal Finance Systems

**Purpose:** Establish that Odin's handling of sensitive financial
data is grounded in documented technical standards, Philippine
regulatory requirements, and user trust considerations — including
how trust affects the quality of user-provided data.

**What this needs to establish:**

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
  connecting to Pillar 10's user retention concern?

- What Philippine regulatory frameworks govern the collection,
  storage, and processing of personal financial data:
  - Republic Act 10173 (Data Privacy Act of 2012)
  - BSP regulatory guidelines on financial data
  - National Privacy Commission issuances

- What is privacy-by-design, and how has it been applied
  in comparable financial system research?

- Given that Odin uses manual transaction input (no banking
  integration), what are the specific privacy implications
  of storing self-reported financial data, and how should
  those be addressed in system design?

---

## Pillar 10: User Retention and Engagement
##            in Personal Finance Systems

**Purpose:** Establish how Odin sustains the regular transaction
logging behavior that its ML modules require to function — without
gamification, which the team has explicitly excluded from scope.

**What this needs to establish:**

- Why is regular transaction logging a prerequisite for
  LSTM forecasting and anomaly detection to function accurately —
  what is the documented relationship between data completeness
  and ML model performance?

- What does the literature say about user retention and
  drop-off patterns in personal finance applications —
  when and why do users stop logging?

- What is the primary documented friction point in PFMS/PBMS
  engagement — and how has manual data entry burden been
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
  system value (accurate forecasts, useful alerts) and
  sustained engagement — is demonstrated value itself
  a retention mechanism?

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
  technical logic — for example, combining zero-based
  period resetting with envelope-style category floors
  and pay-yourself-first savings priority? Or does
  mixing strategies create problems in practice?

---

### A2. How should budget size be determined?

- A2a. Should a budget recommendation system require the
  user to declare their income, or is it more appropriate
  to infer budget size from prior period spending history?
  In your professional view, which produces more accurate
  and useful budgets for Filipino young professionals?

- A2b. What is the minimum information a system needs from
  a user to produce a reliable and useful budget
  recommendation on first use, before any transaction
  history exists?

- A2c. For a user who receives a large lump-sum income
  (e.g., 300,000 PHP from a project) and then does not
  work for several months: how should a system determine
  monthly or weekly budget allocations? Should it ask the
  user to declare a planning horizon, infer from spending
  history, or use another approach?

- A2d. Is income-agnostic budgeting — where the system
  constructs budgets entirely from prior period expense
  history without requiring income declaration — a
  recognized and sound approach in personal finance?

---

### A3. How should budget surplus be handled?

- A3a. If a user is allocated a budget of 20,000 PHP
  for a category in one period but spends only 5,000 PHP,
  should the remainder carry forward to the next period,
  be redistributed to other categories, or be reset
  entirely? What is the most sound approach?

- A3b. Does your answer change depending on whether the
  user has stable versus variable income?

- A3c. Is there a documented or professionally recognized
  scenario where budget inflation from surplus carryforward
  is appropriate or even beneficial?

---

### A4. What time horizons are appropriate?

- A4a. Based on your knowledge of Filipino young
  professional financial behavior, which budgeting
  time horizon is most commonly practiced or most
  appropriate for this demographic — weekly, biweekly,
  semi-monthly, or monthly?

- A4b. Should a system support multiple time horizons
  simultaneously, or enforce one horizon for consistency
  and data quality?

- A4c. For variable income earners, is budgeting per
  income event (rather than per calendar period) a
  recognized and appropriate approach? What are its
  practical implications?

---

## SECTION B: User Input and System Intelligence

### B1. How intelligent should budget recommendation be?

- B1a. Our core concept is an intelligent budgeting system
  that minimizes required user input. In your view,
  what level of user input is acceptable before a system
  can no longer be described as intelligent?

- B1b. Is it appropriate for a budget recommendation to
  be entirely system-generated on first use, before any
  personal transaction history exists? What should it
  be based on in that scenario?

- B1c. If a system produces inaccurate budget recommendations
  early on due to insufficient data, but improves over time
  as data accumulates — is that tradeoff acceptable from
  a user experience and financial planning perspective?

---

## SECTION C: User Profiling

### C1. Are there documented Filipino financial behavioral
###     archetypes or segments?

- C1a. In your field, are you aware of any study,
  institutional report, or framework that segments
  Filipino young professionals into financial behavioral
  profiles or archetypes?

- C1b. If no such segmentation exists in the literature,
  is it methodologically defensible to construct profiles
  from FIES and BSP CFS data? How would you recommend
  approaching that?

- C1c. The mock defense panel mandated that Odin must use
  an ML algorithm — not a rule-based questionnaire — to
  classify users into profiles. Given our four predefined
  profiles (Stable-Flexible, Stable-Obligated,
  Variable-Flexible, Variable-Obligated), what
  classification approach would you recommend or
  have seen used in comparable systems?

- C1d. What Filipino-specific financial behaviors —
  remittances, paluwagan, religious contributions,
  informal lending — do you consider most important
  for a profiling system to explicitly account for?

---

### C2. How should profiles evolve over time?

- C2a. The panel also mandated that a user's behavioral
  data must progressively influence their profile over time.
  In your view, what behavioral signals are most meaningful
  indicators that a user's profile should be reassessed?

- C2b. Should profile updates be automatic, or should
  the system prompt the user to confirm a profile change
  before it takes effect?

- C2c. How frequently should a system reassess a user's
  profile — after a fixed number of transactions, after
  each full budget period, or continuously?

---

## SECTION D: Anomaly Detection

### D1. What constitutes a meaningful financial anomaly
###     for Filipino young professionals?

- D1a. Is a financial anomaly best defined as spending
  that exceeds a fixed threshold, or spending that
  deviates significantly from a user's own established
  spending pattern? Which definition is more actionable
  for the target demographic?

- D1b. Are there culturally specific Filipino spending
  behaviors — large one-time remittances, festival-related
  spending, paluwagan lump-sum contributions — that a
  system should recognize as expected rather than anomalous?

- D1c. When the system detects an anomaly and flags a
  category as overspent, should the next period's
  allocation for that category be automatically reduced,
  or should the system recommend a reduction and let
  the user confirm?

- D1d. How should the system communicate a detected
  anomaly to a user — what tone, framing, and level
  of explanation is appropriate for Filipino users?

---

## SECTION E: Expense Categorization

### E1. What expense categories are appropriate for Odin?

- E1a. Do the expenditure categories defined by the PSA
  FIES and BSP Consumer Finance Survey adequately capture
  the spending patterns of Filipino young professionals,
  or are there significant gaps specific to this demographic?

- E1b. How should culturally specific expense types —
  paluwagan contributions, family remittances, and
  religious obligations — be categorized? As subcategories
  within an existing group, or as a distinct top-level
  category?

- E1c. What is the basis for protecting certain categories
  from budget reduction? Specifically, is there a
  professional or institutional basis for defining
  minimum spending floors for Essentials and Investments
  that the system should enforce?

- E1d. For regular employees, SSS and Pag-IBIG contributions
  are automatically deducted from salary by the employer.
  In your view, should these appear in the user's budget
  at all, or should the income input simply reflect
  take-home pay after deductions?

---

## SECTION F: Recurring Expense Scheduling

### F1. Should Odin support recurring expense scheduling?

- F1a. The mock defense panel raised the question of
  whether users can schedule recurring expenses
  (e.g., monthly rent, utility bills) so the system
  accounts for them automatically. In your view,
  is this a necessary feature for an intelligent
  budgeting system?

- F1b. If yes, how should a recurring expense interact
  with the budget recommendation — should it be
  pre-deducted from the period's budget before
  discretionary allocation begins?

- F1c. If the team decides not to include recurring
  expense scheduling, how significant a limitation
  is that for the system's practical usefulness?

---

## SECTION G: User Retention

### G1. How can Odin sustain regular transaction logging
###     without gamification?

- G1a. In your professional view, what is the primary
  reason Filipino young professionals stop logging
  transactions in personal finance applications?

- G1b. What non-gamification features or design decisions
  do you believe would most effectively sustain regular
  transaction logging behavior among this demographic?

- G1c. Is the value the system provides — accurate
  forecasts, useful anomaly alerts, clear budget health
  — itself a meaningful retention mechanism, or does
  the system need additional engagement features?

---

# PART III: RESOLVED DESIGN DECISIONS
> Items here are closed unless new evidence or expert
> consultation overturns them. Post-discussion decisions
> supersede defense-era positions.

| Decision | Resolution | Source |
|---|---|---|
| Primary forecasting algorithm | LSTM | Team + panel confirmation |
| Anomaly detection algorithm | Isolation Forest | Panel confirmation — algorithm-specific justification still required via Pillar 6 literature |
| Fallback forecasting basis | Behavioral profile averages | Team decision |
| Gamification direction | Removed from scope | Team decision (post-defense discussion) |
| Deployment | Mobile-first, web for accessibility | Panel confirmation |
| Admin users | None — general users only | Panel confirmation |
| Transaction input | Manual — no banking/e-wallet integration | Panel confirmation |
| SSS/Pag-IBIG — regular employees | Auto-deducted by employer, not entered by user | Panel confirmation |
| SSS/Pag-IBIG — variable users | Voluntary — user decides whether to include | Panel confirmation |
| User types | Regular employees, freelancers, contract workers | Panel confirmation |
| Odin's differentiator | Dynamic forecasting vs. static statistics display | Panel confirmation |
| Budget modifiability | System recommends, user can adjust | Panel confirmation |
| Debt management | Avalanche + Snowball options; user ultimately decides repayment | Panel confirmation |
| Profile basis | Income type + obligation weight | SME-validated, panel-confirmed |
| Profile classification method | OPEN — must use ML algorithm | Panel directive (Ma'am Plan) |
| Profile update over time | OPEN — must be behavior-driven, not manual-only | Panel directive (Ma'am Plan) |
| Western profiling taxonomies | Rejected — Filipino-specific required | Team decision |
| Anomaly → budget feedback loop | OPEN — must be explicitly designed | Implied by panel confirmation |
| Recurring expense scheduling | OPEN — team decision needed | Raised by panel chair |
| Expense category basis | FIES + BSP CFS as primary institutional sources | Team decision |
| Protected category justification | OPEN — needs primary literature or institutional source | Panel noted; SME validated but source still required |
| Budget surplus handling | OPEN — needs SME + literature validation | Post-discussion decision |
| Zero-based as sole strategy | OPEN — needs literature review (Pillar 4) | Post-discussion decision |
| Budget recommendation ML algorithm | Rule-based for now — pending Pillar 4 literature | Post-discussion decision |
| Financial literacy as core mission | Rejected — behavioral support is the mission | Post-discussion reframe |
| Data Privacy regulatory framework | RA 10173 + BSP guidelines + NPC issuances | Team decision |
| Dashboard features | Income-expense forecasting, spending breakdowns, budget health | Panel confirmation |

---

# PART IV: SOURCE CANDIDATE TRACKER
> All sources are pending team review unless marked [CONFIRMED].
> No source is used in the revised document until confirmed
> by at least one team member who has read it.

## Pillar 1 Candidates

| ID | Citation | Bucket | Status |
|---|---|---|---|
| E-P1-01 | Lusardi & Mitchell (2023). JEP, 37(4). DOI: 10.1257/jep.37.4.137 | International | In proposal — keep |
| E-P1-02 | Cacnio & Romarate (2024). BSP Discussion Paper 2024-13. | Local | In proposal — keep |
| E-P1-03 | Dimaunahan et al. (2025). Acta Psychologica. | Local | Pending DOI verification |
| E-P1-04 | Lim et al. (2024). BIO Web of Conferences. | Local | Pending DOI verification |
| E-P1-05 | Rodriguez et al. (2024). Journal of Global Awareness. | Local | Pending journal quality check |
| E-P1-06 | PSA FIES (2021 & 2024). | Local | Keep — primary source for category justification |
| C-P1-07 | Templa et al. (2025). Psych Educ, 38(8). DOI: 10.70838/pemj.380810 | Local | Conditional — assess student-vs-professional gap |
| C-P1-08 | Sinnewe (2023). Journal of Consumer Affairs. DOI: 10.1111/joca.12512 | International | Strong candidate |
| C-P1-09 | Sabri et al. (2023). J. Financial Services Marketing. DOI: 10.1057/s41264-023-00234-8 | International | Good candidate |
| C-P1-10 | Bai (2023). PLoS ONE, 18(11). DOI: 10.1371/journal.pone.0294466 | International | Good candidate |
| C-P1-11 | BSP Consumer Finance Survey 2021. | Local | Strong — expense category justification |

## Pillar 2 Candidates

| ID | Citation | Bucket | Status |
|---|---|---|---|
| E-P2-01 | Alenazi & Sas (2024). Interacting with Computers, 37(5). DOI: 10.1093/iwc/iwae041 | International | Keep — DOI confirmed |
| E-P2-02 | Aishwarya & Hemalatha (2023). AI4IoT 2023. | International | Keep — pending DOI |
| E-P2-03 | Bhatele et al. (2023). ICACTA 2023. | International | Keep — pending DOI |
| E-P2-04 | Jadhav & Patil (2025). Communications on Applied Nonlinear Analysis. | International | Keep |
| E-P2-05 | Talasila (2024). IRJET. | International | PENDING — low-tier journal, needs team assessment |
| E-P2-06 | Suria (2024). [SUS/UMUX usability study] | Local | Pending DOI |
| C-P2-07 | Stefanov et al. (2024). TEM Journal, 13(3). DOI: 10.18421/TEM133-34 | International | Good candidate |
| C-P2-08 | Grados-Espinoza & Velasquez-Jimenez (2025). IJETT, 73(2). | International | Good candidate |
| C-P2-09 | Jain (2024). Am. J. Computer Architecture, 11(6). DOI: 10.5923/j.ajca.20241106.01 | International | Moderate — verify journal quality |
| C-P2-10 | Meng et al. (2025). Journal of Consumer Behaviour. DOI: 10.1002/cb.2497 | International | Strong candidate |
| C-P2-11 | Jabar & Dayao (2025). RSIS International. | Local | Conditional — verify journal quality |

## Algorithm-Specific Candidates (Pillar 5 & 6)

| ID | Citation | Bucket | Status |
|---|---|---|---|
| E-A-01 | Mroua & Lamine (2023). Humanities and Social Sciences Communications. | Algorithm | In proposal — reassess with LSTM focus |
| E-A-02 | Yang (2025). Frontiers in Applied Mathematics and Statistics. | Algorithm | In proposal — keep |
| E-A-03 | Xiang et al. (2023). OptIForest. IJCAI 2023. | Algorithm | In proposal — keep |
| E-A-04 | Xiang et al. (2025). Machine Intelligence Research. | Algorithm | In proposal — keep |
| E-A-05 | Xu et al. (2023). Deep Isolation Forest. IEEE TKDE. | Algorithm | In proposal — keep |
| E-A-06 | Kumari & Kumar (2024). IET Information Security. | Algorithm | In proposal — keep |
| C-A-07 | McElfresh et al. (2023). NeurIPS 2023. DOI: 10.48550/arXiv.2305.02997 | Algorithm | Strong — tabular vs. NN landmark paper |
| C-A-08 | Hong et al. (2023). MLMI 2023. DOI: 10.1145/3635638.3635640 | Algorithm | Pending manual verification |
| C-A-09 | Naviamos & Niguidula (2024). arXiv:2407.13061 | Algorithm | Pending — preprint, assess dept. policy |

## Sources Flagged as Pending / At-Risk

| Source | Issue |
|---|---|
| Bangor et al. (2008) | Pre-2023 — cite only through recent applied work |
| Talasila (2024) IRJET | Non-peer-reviewed journal |
| Pascual & Santos-Recto (2024) ASMJ | Questionable impact profile |
| de Zarzà et al. (2024) | Relevance weakens if LSTM confirmed over LightGBM |
| Mireku et al. (2023) | Secondary citation issue — resolve Eloriaga et al. |

---

# PART V: SOURCE QUOTA TRACKER

| Bucket | Confirmed/Candidate | Target | Gap |
|---|---|---|---|
| Local | ~13 | 25 | ~12 |
| International | ~16 | 25 | ~9 |
| Algorithm-specific | ~9 | 25 | ~16 |
| **Total** | **~38** | **75** | **~37** |

> Algorithm-specific bucket remains the largest gap.
> Priority pillars for next search rounds: Pillar 5 (LSTM),
> Pillar 6 (Isolation Forest), Pillar 7 (ML classification).

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