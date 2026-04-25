# Odin — Research & Design Foundations Document

---

# PART I: PILLAR STRUCTURE

Pillars are conceptual territories the RRL must cover to justify Odin's existence and design decisions. Researched in order. Each pillar feeds into the next.

---

## Pillar 1: Spending and Budgeting Behavior of Filipino Young Professionals

**Purpose:** Establish who the users are at a behavioral level — that their specific income patterns, expenditure patterns, and budgeting behaviors create a concrete problem that an intelligent system can address.

**What this needs to establish:**

- What are the documented income structures of Filipino young professionals? (stable salaried, freelance/project-based, mixed, informal)

- What time horizons do Filipino young professionals actually use for budgeting and financial planning — weekly, biweekly, monthly, or other — and what does the literature or institutional data say about which are most common?

- What are the documented expenditure patterns of Filipino young professionals, broken down where possible by income type?

- What budgeting behaviors — if any — are documented among this demographic? Do they budget at all, and if so, how?

- What are the documented failure points in their financial management — irregular tracking, overspending in specific categories, failure to plan for irregular expenses?

- How does financial behavior differ between income stability types within this demographic?

- What role do culturally specific obligations (remittances, paluwagan, religious contributions) play in the expenditure patterns of this demographic?

- In what way does an intelligent budgeting and forecasting system — as opposed to a literacy or education app — address these behavioral patterns directly?

---

## Pillar 2: Existing Personal Finance and Budget Management Systems

**Purpose:** Establish what systems already exist, how they work, and where they fall short — creating the gap that Odin fills.

**What this needs to establish:**

- What categories of PFMS/PBMS exist, and how are they typically classified in the literature?

- What are the dominant features of existing systems — what do they do well?

- What are the documented limitations of existing systems, particularly around:
  - Manual data entry burden on users
  - Lack of intelligent or adaptive budget recommendation
  - Absence of forecasting capabilities
  - Absence of anomaly detection
  - Generic, non-localized category structures
  - Et cetera.

- How do existing systems handle budget recommendation — rule-based, user-defined, or algorithmically driven?

- What budgeting strategies (zero-based, envelope, pay-yourself-first, proportional, hybrid) are implemented in existing systems, and how are they technically realized?

- Where is the documented gap between what existing systems offer and what an intelligent, adaptive, locally-grounded system would offer?

---

## Pillar 3: Mobile-First Design in Personal Finance Systems

**Purpose:** Establish why mobile-first is the correct deployment approach and what technical and design constraints it introduces — constraints that directly inform algorithm and interaction design choices.

**What this needs to establish:**

- What does "mobile-first" mean in the context of PFMS/PBMS, and how does it differ from desktop-first or responsive web approaches?

- What is the documented evidence that mobile-first is the preferred and dominant deployment approach for personal finance tools, particularly among younger users in emerging markets?

- What are the documented technical constraints of mobile-first PFMS/PBMS:
  - Limited local compute for ML inference
  - Intermittent or low-bandwidth connectivity
  - Smaller screen real estate and UX simplicity requirements
  - Battery and memory constraints
  - Et cetera.

- How do these constraints influence algorithm selection for forecasting and anomaly detection in mobile-deployed systems?

- What mobile-first design patterns are documented as effective for minimizing user input burden while maintaining data accuracy?

---

## Pillar 4: Budgeting Strategies and Budget Recommendation in Personal Finance Systems

**Purpose:** Establish the theoretical and technical basis for Odin's budget recommendation module — what strategies exist, how they've been implemented, and which combination is appropriate for Odin's use case.

**What this needs to establish:**

- What budgeting strategies are documented in personal finance literature? (zero-based, envelope/category-based, pay-yourself-first, proportional allocation, needs-based, hybrid)

- What are the documented strengths and weaknesses of each strategy, particularly for users with:
  - Stable salaried income
  - Variable or irregular income
  - Lump-sum income followed by periods of no income
  - Et cetera.

- How have existing systems technically implemented budget recommendation — purely rule-based, user-configured, or algorithmically adaptive?

- Is there documented precedent for a system that distills multiple budgeting strategies into one unified technical configuration?

- What does the literature say about budget period resetting — should budgets reset to a baseline each period, carry surplus forward, or adapt based on prior period behavior?

- What does the literature say specifically about surplus handling:
  - Is surplus carryforward appropriate?
  - Under what conditions is it appropriate vs.
    inappropriate?
  - Does income stability type affect the answer?
  - Et cetera.

- How should a budget recommendation system behave when income data is absent, irregular, or declared as a lump sum?

- What is the minimum user input required for a budget recommendation to be accurate and useful, and what does the literature say about the tradeoff between input burden and output quality?

---

## Pillar 5: Predictive Modeling in Personal Finance Systems

**Purpose:** Establish the basis for Odin's forecasting module —
what methods exist, what data characteristics they require,
and why the chosen algorithm is appropriate.

**What this needs to establish:**

- What forecasting methods have been applied to personal finance spending data in the literature? (ARIMA, SARIMA, Random Forest, XGBoost, LightGBM, LSTM, hybrid models)

- How is personal finance spending data characterized in forecasting literature — as sequential time-series, structured tabular records, or both? This characterization directly determines algorithm fit.

- What are the documented strengths and weaknesses of each method on personal finance data, particularly regarding:
  - Data sparsity (new users with little history)
  - Per-category forecasting across multiple categories
  - Sequential behavioral dependency (does this month's spending affect next month's?)
  - Et cetera.

- What does the literature say specifically about LSTM applied to personal finance or household expenditure forecasting — where does it perform well and where does it underperform?

- How do mobile constraints (Pillar 3) interact with forecasting algorithm selection — what is computationally feasible on a mobile-deployed system?

- What fallback mechanisms are documented for cold-start forecasting when insufficient personal history exists?

---

## Pillar 6: Anomaly Detection in Personal Finance Systems

**Purpose:** Establish the basis for Odin's anomaly detection module — what anomalies are in personal finance, how they're detected, and whether a rule-based or algorithmic approach is more appropriate for Odin's use case.

**What this needs to establish:**

- What constitutes a financial anomaly in personal finance contexts — how is it defined and taxonomized in the literature?

- What is the distinction between a threshold-based alert ("spent more than X") and a behavioral deviation alert ("spent unusually relative to personal history")? Which is more appropriate for Odin's use case?

- What anomaly detection approaches have been applied to personal finance data, and with what results? (rule-based threshold, statistical methods, Isolation Forest, One-Class SVM, autoencoders)

- What are the documented tradeoffs between rule-based and algorithmic anomaly detection in terms of:
  - Implementation complexity
  - Explainability to users
  - Accuracy and false positive rates
  - Adaptability to individual behavioral patterns
  - Et cetera.

- What does the literature say about surfacing anomaly alerts to users — what format, frequency, and framing minimizes alert fatigue?

---

## Pillar 7: User Behavioral Profiling in Filipino Personal Finance Contexts

**Purpose:** Establish the basis for Odin's user profiling system — what profiles exist or can be constructed from Philippine data, and why Western taxonomies are insufficient.

**What this needs to establish:**

- What is user behavioral profiling in the context of personal finance systems, and what role does it play in budget recommendation and forecasting?

- What Filipino-specific financial behavioral patterns are documented in BSP CFS, FIES, or academic literature that would distinguish Filipino user profiles from Western ones?

- Are there documented Filipino financial behavioral archetypes or segments? If not, is constructing profiles from institutional data (FIES, BSP CFS) a recognized and methodologically defensible approach?

- How do culturally specific Filipino financial obligations (remittances, paluwagan, religious contributions) manifest as distinct behavioral signals that a profiling system must account for?

- What is the documented cold-start problem in personalized financial systems, and what fallback approaches are supported in the literature?

- How should a profile be updated over time as user behavior is observed — at what point does a system transition from profile-average priors to personalized predictions?

---

## Pillar 8: Expense Categorization in Filipino Personal Finance Contexts

**Purpose:** Establish why Odin's expense categories are what they are — grounded in Philippine institutional frameworks, not arbitrarily chosen or borrowed from Western systems.

**What this needs to establish:**

- What are the documented approaches to expense categorization in PFMS/PBMS — user-defined, institutionally derived, or ML-generated?

- What are the documented limitations of generic Western expense categories when applied to Filipino spending contexts?

- What expenditure categories are defined by Philippine institutional frameworks:
  - PSA Family Income and Expenditure Survey (FIES)
  - BSP Consumer Finance Survey (CFS)
  - Et cetera.

- How do these institutional categories map to the categories Odin implements, and is every Odin category traceable to a primary source?

- How are culturally specific Filipino expense types — paluwagan, remittances, religious obligations — recognized or treated in existing literature or institutional data?

- What is the basis for Odin's "protected categories" concept — which categories have documented minimum spending floors that should not be reduced below a threshold?

---

## Pillar 9: Data Privacy, Security, and User Trust in Personal Finance Systems

**Purpose:** Establish that Odin's handling of sensitive financial data is grounded in documented technical standards, regulatory requirements, and user trust considerations.

**What this needs to establish:**

- What categories of data does a PFMS/PBMS collect, and why is financial data classified as particularly sensitive in the literature?

- What technical security measures are documented as standard or best practice for financial applications — encryption, authentication, data minimization, secure storage?

- What does the literature say about user trust in financial applications — how does trust affect data sharing behavior, and what design decisions build or erode it?

- What Philippine regulatory frameworks govern the collection, storage, and processing of personal financial data:
  - Republic Act 10173 (Data Privacy Act of 2012)
  - BSP regulatory guidelines on financial data
  - National Privacy Commission issuances
  - Et cetera.

- What is privacy-by-design, and how has it been applied in comparable financial system research?

- How do data privacy concerns specifically affect user willingness to log financial transactions regularly — connecting to the user retention concern from the SME?

---

## Pillar 10: User Retention and Engagement in Personal Finance Systems

**Purpose:** Establish how Odin sustains the regular transaction logging behavior that its ML modules require to function.

**What this needs to establish:**

- Why is regular transaction logging a prerequisite for ML-driven forecasting and anomaly detection to function accurately — what is the relationship between data completeness and model performance?

- What does the literature say about user retention and drop-off patterns in personal finance applications — when and why do users stop logging?

- What retention mechanisms are documented as effective in PFMS/PBMS:
  - Notification and reminder design
  - Frictionless transaction entry
  - Immediate value feedback (showing the user something useful right after they log)
  - Progress toward user-defined goals
  - Et cetera.

- What does the literature say about the minimum viable interaction frequency for a personal finance app to remain useful to its user?

- How have comparable systems addressed the manual entry burden that is documented as the primary friction point in PFMS/PBMS?

---

# PART II: OPEN QUESTIONS FOR SME CONSULTATION
> Questions are specific and open-ended.
> Sub-questions are provided where the parent question
> is too broad to answer in one sitting.

---

## SECTION A: Budgeting Strategy and Logic

### A1. Which budgeting strategies are most relevant to Filipino young professionals?

- A1a. Among zero-based budgeting, envelope budgeting, pay-yourself-first, and proportional allocation (e.g., 50/30/20), which — if any — are you aware of being commonly practiced or recommended for Filipino young professionals?

- A1b. Is there evidence that one strategy works better for stable income earners versus variable or irregular income earners?

---

### A2. How should budget size be determined?

- A2a. Should a budget recommendation system require the user to declare their income, or is it more appropriate to infer budget size from prior period spending history?

- A2b. In your professional view, what is the minimum information a system needs from a user to produce a reliable and useful budget recommendation?

- A2c. For a user who receives a large lump-sum income (e.g., 300,000 PHP) and then chooses not to work for an extended period: how should a system determine monthly or weekly budget allocations? Should it ask the user to declare a planning horizon, infer from spending history, or use another approach?

- A2d. Is income-agnostic budgeting — where the system constructs budgets entirely from prior period expenses without requiring income declaration — a recognized and methodologically sound approach?

---

### A3. How should surplus be handled?

- A3a. If a user is allocated a budget of 20,000 PHP for a category in one period but only spends 5,000 PHP, should the remaining 15,000 PHP carry forward to the next period, be redistributed to other categories, or be reset entirely?

- A3b. Does your answer change depending on whether the user has stable vs. variable income?

- A3c. Is there a documented scenario where budget inflation from surplus carryforward is appropriate or even recommended?

---

### A4. What time horizons are appropriate?

- A4a. Based on your knowledge of Filipino young professional financial behavior, which budgeting time horizon — weekly, biweekly, semi-monthly, or monthly — is most commonly practiced or most appropriate for this demographic?

- A4b. Should a system support multiple time horizons simultaneously, or enforce one for consistency?

- A4c. For variable income earners, is it more appropriate to budget per income event rather than per calendar period? What are the practical implications of that approach?

---

## SECTION B: User Input and System Intelligence

### B1. How intelligent should the budget recommendation be?

- B1a. Our core concept is an intelligent budgeting system. In your view, what level of user input is acceptable before a system can no longer be described as intelligent?

- B1b. Is it appropriate for a budget recommendation to be entirely system-generated on first use, before any personal transaction history exists? What should it be based on in that case?

- B1c. What is the risk of a system that recommends budgets with minimal user input but produces inaccurate recommendations — is inaccuracy at onboarding acceptable if it improves over time?

---

## SECTION C: User Profiling

### C1. Are there documented Filipino financial behavioral archetypes or segments?

- C1a. In your field, are you aware of any study, institutional report, or framework that segments Filipino young professionals into financial behavioral profiles or archetypes?

- C1b. If no such segmentation exists in the literature, is it methodologically defensible to construct profiles from FIES and BSP CFS data? How would you recommend doing that?

- C1c. What Filipino-specific financial behaviors — remittances, paluwagan, religious contributions, informal lending — do you consider most important for a profiling system to account for?

---

## SECTION D: Anomaly Detection

### D1. What constitutes a meaningful financial anomaly for Filipino young professionals?

- D1a. In your view, is a financial anomaly best defined as spending that exceeds a fixed threshold, or spending that deviates from a user's own established pattern?

- D1b. Are there culturally specific spending behaviors among Filipinos — such as large one-time remittances or festival-related spending — that a system should recognize as expected rather than anomalous?

- D1c. How should a system communicate a detected anomaly to a user — what framing, frequency, and level of explanation is appropriate?

---

## SECTION E: Retention and Engagement

### E1. How can Odin sustain regular transaction logging?

- E1a. In your professional view, what is the primary reason users stop logging transactions in personal finance apps?

- E1b. What features or design decisions do you believe would most effectively sustain regular transaction logging behavior among Filipino young professionals?

- E1c. How much does the value a system provides — accurate forecasts, useful alerts — affect whether users continue to engage with it? Is demonstrated value itself a retention mechanism?

---