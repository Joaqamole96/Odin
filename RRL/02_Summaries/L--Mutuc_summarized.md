```yaml
paper_id: 10.3390/ijfs13040222
designation: local
title: Exploring the Interplay of Life Attitude and Cognitive Ability in Shaping the Intention to Stock Market Participation Among Young Professionals in the Philippines
authors: Mutuc, E. B.
year: 2025
venue: International Journal of Financial Studies
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.D
  - 4.B
  - 5.A
  - 5.C
  - 10.A
tldr: Life purpose and goal-seeking positively predict stock market participation intention, with cognitive ability (financial literacy) mediating this relationship among young Filipino professionals.
problem_and_motivation: Existing behavioral finance research has largely neglected how broader psychological orientations like life attitude influence investment behavior, particularly among young professionals in emerging economies. The interaction between these life orientations and cognitive ability remains poorly understood, limiting holistic models of financial participation.
approach:
  - Quantitative cross-sectional survey of 195 randomly selected young professionals (aged 20–39) from Bulacan, Philippines.
  - Used the Life Attitude Profile–Revised (LAP-R) to measure existential dimensions and the Financial Literacy Inventory for cognitive ability.
  - Applied Partial Least Squares Structural Equation Modeling (PLS-SEM) with 5000 bootstrap resamples to test direct and mediating effects.
  - Included control variables (sex, age, education, employment) and conducted multi-group analyses for gender and education subgroups.
  - Assessed common method variance via Harman's single-factor test and full collinearity assessment.
findings:
  - num: Life Attitude Profile (LAP) positively predicts Intention to Stock Market Participation (β = 0.154, p = 0.025).
  - num: Cognitive Ability mediates the LAP–SMP relationship (β = 0.051, p = 0.032), with 39% of LAP's influence operating through cognition.
  - num: Goal Seeking (β = 0.396, p = 0.009) and Death Acceptance (β = 0.312, p < 0.001) are the strongest positive LAP sub-dimension predictors of SMP.
  - Life Purpose showed a negative association with SMP (β = −0.243, p = 0.036), suggesting purpose-driven individuals may be financially conservative.
  - num: The model explained 47.1% to 58.2% of variance in SMP across different specifications.
  - num: Cognitive Ability mean score was 67.83% (SD = 16.53), indicating higher-than-average financial literacy in the sample.
  - num: Sex differences were found: males relied more on cognitive ability (C→SMP: β=0.42), females on life attitudes (LAP→SMP: β=0.38).
key_figures_tables:
  - Figure 1: Conceptual framework showing LAP dimensions, Cognitive Ability as mediator, and SMP as outcome → LAP influences SMP directly and via cognition.
  - Table 1: Descriptive statistics show favorable life attitudes (M=5.07–6.11) and moderate investment intention (M=4.28) → sample is purpose-driven with above-average financial literacy.
  - Figure 3: Lower-order construct model with path coefficients → Death Acceptance and Goal Seeking positively drive SMP; Life Purpose and Life Control show negative associations.
  - Figure 4: Higher-order model with R²=0.471 → LAP and Cognitive Ability collectively explain nearly half of investment intention variance.
key_equations:
  - equation: SMP_i = β_0 + β_1(LAP_i) + ε_i
    explanation: Direct effect of overall life attitude on investment intention.
  - equation: SMP_i = β_0 + β_1(LP_i) + β_2(EV_i) + β_3(LC_i) + β_4(DA_i) + β_5(WTM_i) + β_6(GS_i) + β_7(FMF_i) + ε_i
    explanation: Regression with seven LAP sub-dimensions predicting SMP.
  - equation: C_i = β_0 + β_1(LAP_i) + ε_i
    explanation: Life attitude predicts cognitive ability (financial literacy).
  - equation: SMP_i = β_0 + β_1(LAP_i) + β_2(CA_i) + ε_i
    explanation: Mediation model with both LAP and cognitive ability predicting SMP.
definitions:
  - term: Life Attitude Profile (LAP)
    definition: Multidimensional framework assessing sense of purpose, meaning, and life orientation (Reker et al., 1987).
  - term: Cognitive Ability
    definition: Efficiency in processing and integrating financial information, proxied by financial literacy in this study.
  - term: Stock Market Participation (SMP)
    definition: Intention to engage in equity market investments, measured via self-reported behavioral intention.
  - term: PLS-SEM
    definition: Partial Least Squares Structural Equation Modeling, a variance-based technique for prediction and mediation testing.
  - term: LAP-R
    definition: Life Attitude Profile–Revised, an instrument capturing existential vacuum, life purpose, control, death acceptance, will to meaning, goal seeking, and future meaning.
critical_citations:
  - "[van Rooij et al., 2011] — Financial literacy retains predictive validity for stock participation beyond wealth."
  - "[Guiso et al., 2008] — Trust in financial institutions shapes market entry decisions."
  - "[Lusardi & Mitchell, 2014] — Foundational evidence linking financial literacy to economic outcomes."
  - "[Haliassos & Bertaut, 1995] — Classic stock market participation puzzle paper."
  - "[Steger et al., 2006] — Meaning in life questionnaire validates existential constructs used here."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Directly samples Filipino young professionals (aged 20-39, white-collar) as the core population.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Examines investment intention and cognitive ability, indirectly reflecting financial decision-making structures.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly measures financial behavior (stock market participation intention) and its psychological drivers.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: Provides background on Philippine economic context but does not focus on specific cultural practices like utang or padala.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Mentions cultural-economic dynamics but does not analyze spending cycles; focuses on investment, not consumption.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies research gaps in behavioral finance (underexplored psychological orientations) that Odin could address.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly profiles individuals based on life attitudes and cognitive ability as predictors of financial behavior.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses PLS-SEM to classify and map relationships between psychological profiles and investment intentions.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Mentions ethical compliance with Data Privacy Act but does not address system-level privacy or security design.
  contribution: "Odin can cite this paper to justify its psychological profiling module (5.A) by demonstrating that life attitude dimensions meaningfully predict financial behavior. The mediating role of cognitive ability (6.A) supports Odin's use of financial literacy as a key input for forecasting and recommendation algorithms. The finding that purpose-driven individuals may be financially conservative (negative LP→SMP path) informs Odin's budget recommendation (7.B) to avoid over-recommending investments to users with strong conservative life purpose profiles. The robust mediation model also validates Odin's integrated approach: combining attitudinal profiling with cognitive assessment to produce more accurate financial behavior predictions."
  directly_justifies:
    - "Life attitude dimensions significantly predict intention to invest, supporting psychological profiling for financial apps."
    - "Cognitive ability mediates the effect of life attitudes on financial behavior, justifying inclusion of literacy measures."
    - "Goal seeking and death acceptance are strong positive predictors, indicating key profile dimensions for segmentation."
    - "Purpose-driven individuals may prefer conservative financial strategies, informing personalized recommendation constraints."
    - "Sex and education moderate the strength of attitudinal and cognitive pathways, suggesting demographic adjustments."
  limits:
    - "Cross-sectional design limits causal inference between life attitudes and investment intention."
    - "Self-reported data may introduce social desirability bias despite anonymity."
    - "Sample from Bulacan province may not generalize to other Philippine regions or national contexts."
    - "No local psychometric validation of the LAP-R instrument for the Filipino sample."
  mapping_rationale: "Systematic scan of all 12 functional domains and their associated topic codes identified the strongest relevance in the Filipino Cultural Context, Behavioral Profiling, and Spending Forecasting domains. The paper directly addresses Filipino young professionals (1.A, 1.B, 1.C) and provides empirical evidence linking life attitudes to financial behavior (5.A, 5.C). It also supports the Forecasting domain (6.A) by establishing cognitive ability (financial literacy) as a mediator, which informs predictive modeling inputs. Borderline cases: the paper touches on Filipino cultural context (2.A) through its setting and discussion of family obligations, but does not specifically analyze cultural practices, so relevance is contextual. The paper mentions data privacy compliance (10.A) but offers no system-level insights, hence low relevance. Domains like Anomaly Detection (8.A-C), Mobile-First Design (9.A-B), User Retention (11.A-B), System Evaluation (12.A-C), and Savings/Debt Management (13.A-C) were rejected as the paper does not address algorithm evaluation, system design, retention mechanisms, or debt/savings goals. Overall, the paper is highly relevant for establishing psychological and cognitive determinants of financial behavior among Odin's target demographic, justifying behavioral profiling and providing inputs for forecasting and recommendation modules."
limitations:
  - "Cross-sectional design restricts causal interpretation of relationships among LAP, cognitive ability, and SMP."
  - "Self-reported measures may introduce response biases, including social desirability. [unacknowledged]"
  - "Sample was drawn exclusively from Bulacan province, limiting generalizability to other Philippine regions or cross-national contexts. [unacknowledged]"
  - "Absence of a marker variable for common method variance testing, though procedural remedies were applied. [unacknowledged]"
  - "The LAP-R instrument was used without local cultural adaptation or pilot testing for the Filipino population."
remember_this:
  - "Cognitive ability mediates the link between life attitudes and investment intention."
  - "Goal seeking and death acceptance are the strongest positive predictors of investment intention."
  - "Purpose-driven individuals may exhibit conservative investment behavior."
  - "The model explains 47% of variance in investment intention among Filipino young professionals."
  - "Financial literacy training should be paired with psychosocial skill development for holistic financial engagement."
```