```yaml
paper_id: 10.5281/zenodo.1234567
designation: local
title: The Moderating Effect of Access to Finance on Myopic Decision-Making and Business Performance of Low-income Household Micro-Enterprises in Manila
authors: Ong, H. T.; Keh, K. Z. N.; Lui, N. C. J. L.; Santos, A. H. M.; Suarez, E. J. P.
year: 2026
venue: Review of Integrative Business and Economics Research
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.D
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 13.A
  - 13.B
  - 13.C
tldr: Myopic decision-making significantly reduces micro-enterprise performance, but access to finance moderates this negative effect among low-income households in Manila.
problem_and_motivation: Low-income micro-entrepreneurs in Manila face barriers to formal finance and often make short-sighted decisions due to survival pressures. No prior work has investigated the combined effect of myopic decision-making and access to finance on micro-enterprise performance in this context. This study addresses that gap to inform targeted interventions.
approach:
  - Quantitative survey of 100 sari-sari store owners in Manila using a pen-and-paper questionnaire.
  - Measured myopic decision-making across competitive, cooperative, temporal, and learning dimensions using a validated scale.
  - Assessed access to finance through barriers, formal lending, and informal credit indicators.
  - Evaluated business performance via financial, customer satisfaction, market competitiveness, growth, and operational metrics.
  - Used regression analysis to test direct and moderating effects with p-value significance thresholds.
findings:
  - num: Myopic decision-making significantly impacts business performance (p < 0.001).
  - num: Access to finance significantly improves business performance (p < 0.001).
  - num: Access to finance moderates the negative effect of myopic decision-making on performance (p = 0.005).
  - Temporal myopia (mean 2.96) and learning myopia (mean 2.44) are the most and least prevalent dimensions, respectively.
  - Barriers to access (mean 2.81) are the highest perceived financial constraint, while formal lending use is very low (mean 1.49).
  - Customer satisfaction (mean 3.53) is the strongest performance area, while financial performance (mean 2.61) is the weakest.
  - 44% of respondents cut R&D spending, indicating high temporal myopia.
  - 33% rarely consider collaborations, reflecting cooperative myopia.
key_figures_tables:
  - Figure 1: Operational framework linking myopic decision-making, access to finance, and business performance → Framework for integrated analysis.
  - Table 3: Summary stats for myopic dimensions → Temporal myopia highest, learning myopia lowest.
  - Table 4: Access to finance stats → Barriers high, formal and informal use low.
  - Table 5: Business performance stats → Customer satisfaction highest, financial performance lowest.
  - Table 6: Hypothesis test results → All three hypotheses significant (p < 0.001 and p = 0.005).
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Myopic Decision-Making
    definition: A cognitive bias prioritizing immediate rewards over long-term benefits, encompassing competitive, cooperative, temporal, and learning myopia.
  - term: Access to Finance
    definition: Availability and use of formal financial services including credit, savings, and payments, as well as informal credit sources.
  - term: Business Performance
    definition: Holistic measure of effectiveness and success, encompassing financial and non-financial metrics.
  - term: Micro-Enterprise
    definition: Business with assets below ₱3 million and fewer than 10 employees in the Philippines.
  - term: Low-Income Households
    definition: Families earning around or below ₱24,000 monthly, sufficient for basic food but inadequate for essential non-food expenses.
critical_citations:
  - "[Czakon et al., 2023] — Validated strategic myopia scale used."
  - "[Amadasun & Mutezo, 2022] — Framework for access to finance barriers."
  - "[Jachimowicz et al., 2017] — Links poverty to myopic decisions."
  - "[Orbeta et al., 2020] — Micro-enterprises as livelihood for low-income Filipinos."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Directly studies low-income micro-entrepreneurs in Manila, a core user demographic.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Examines income constraints and financial barriers faced by low-income households.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Focuses on myopic decision-making and financial access behaviors.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Informal credit and family loans are culturally embedded practices in the Philippines.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: Sari-sari stores cater to daily and occasion-based spending, though not directly measured.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Identifies gaps in formal financial access that PFMS like Odin could address.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Highlights barriers to formal finance (collateral, documentation) that digital PFMS can mitigate.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Myopic decision-making is a behavioral profile directly relevant to personal finance systems.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: medium
      justification: Temporal and learning myopia patterns inform initial user profile assumptions.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: contextual
      justification: Provides behavioral dimensions that could be used for classification.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: Mentions inadequate savings as a consequence of myopia but does not focus on goal management.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: medium
      justification: Addresses informal credit and debt cycles, relevant to debt management features.
    - code: 13.C
      name: End-of-Period Surplus as a Savings Input
      relevance: low
      justification: Tangentially related through business reinvestment but not directly addressed.
  contribution: This paper provides empirical evidence that myopic decision-making reduces business performance, which directly informs Odin's behavioral profiling module. The finding that access to finance moderates this effect justifies Odin's budget recommendation and savings management features. The identification of specific myopia dimensions (temporal, learning) guides the design of user onboarding and financial literacy interventions within the app. The study's focus on low-income Filipino micro-entrepreneurs validates Odin's target demographic and contextual design choices.
  directly_justifies:
    - Myopic decision-making significantly reduces micro-enterprise business performance.
    - Access to finance significantly improves business performance for low-income micro-entrepreneurs.
    - Access to finance moderates the negative effect of myopic decision-making on business performance.
    - Financial literacy programs and improved formal access are recommended interventions.
    - Temporal myopia (short-term focus) is the most prevalent form of myopic decision-making.
  limits:
    - Focuses only on sari-sari store owners in Manila, limiting generalizability to other micro-enterprise types.
    - Cross-sectional design cannot establish causality.
    - Self-reported measures may introduce social desirability or recall bias.
    - Does not cover other factors beyond myopic decision-making and access to finance.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was conducted. The paper was flagged as highly relevant to the Filipino Cultural Context domain (topics 1.A, 1.B, 1.C) because it directly studies low-income micro-entrepreneurs in Manila, providing foundational demographic and behavioral insights. It was also relevant to Existing Systems & Gaps (4.A, 4.B) due to its identification of formal finance barriers that Odin can address. For Behavioral Profiling (5.A, 5.B, 5.C), the paper's myopia dimensions offer a validated framework for classifying user financial behavior. The Savings & Debt Management domain (13.A, 13.B, 13.C) was moderately relevant due to discussions of informal credit and inadequate savings. Topics like Expense Categorization (3.A-3.C), Forecasting (6.A-6.B), Anomaly Detection (8.A-8.C), and Mobile Design (9.A-9.B) were considered but rejected as the paper does not address algorithmic or design aspects. The paper was deemed contextual for 2.D (spending cycles) as it mentions daily sales but does not analyze seasonal patterns. Overall, the paper provides strong empirical justification for Odin's behavioral and financial access features, though its non-algorithmic nature limits direct technical contributions.
limitations:
  - Limited to sari-sari stores in Manila; may not generalize to other micro-enterprises or regions.
  - Cross-sectional design prevents causal inference.
  - Self-reported data may be biased.
  - Excludes other potentially important factors like market conditions or family support.
  - No historical financial data used due to lack of formal record-keeping. [unacknowledged]
remember_this:
  - Myopic decision-making significantly harms micro-enterprise business performance.
  - Access to finance improves performance and buffers against myopic decisions.
  - Temporal myopia is the most common form of short-term thinking among entrepreneurs.
  - Barriers to formal finance are high, while informal credit is limited in this sample.
  - Customer satisfaction is the strongest performance area; financial performance is weakest.
```