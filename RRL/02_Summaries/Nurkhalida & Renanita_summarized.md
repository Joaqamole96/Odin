```yaml
paper_id: 10.20885/psikologika.vol30.iss2.art5
designation: international
title: The Mediating Role of Financial Well-Being in the Relationship between Financial Behavior and Stress Among Irregular Income Workers
authors: Nurkhalida, K.; Renanita, T.
year: 2025
venue: Psikologika
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 3.A
  - 3.B
  - 5.A
  - 5.C
  - 13.A
  - 13.B
tldr: Financial well-being fully mediates the relationship between financial behavior and stress in irregular income workers, demonstrating that behavior reduces stress only through improved well-being.
problem_and_motivation: Irregular income workers face heightened stress due to financial instability and uncertainty, yet the mechanisms linking financial behavior to stress in this vulnerable population remain unexplored. Prior research has established connections between financial behavior and well-being or well-being and stress separately, but no study has examined the mediating role of financial well-being in the behavior-stress relationship specifically for irregular income earners. This gap is critical because understanding this pathway could inform targeted interventions to reduce stress among workers with unpredictable incomes.
approach:
  - Quantitative study with two phases: instrument validation (n=200) and hypothesis testing (n=266) using purposive non-probability sampling.
  - Participants were Indonesian irregular income workers aged 20-40 years, recruited via online survey in November-December 2024.
  - Instruments: DASS-21 stress scale (7 items), Financial Management Behavior Scale (15 items, 4 factors), and InCharge Financial Distress/Well-Being Scale (8 items).
  - Instruments were adapted to Indonesian using Beaton et al. (2000) guidelines and validated via expert assessment and CFA with Mplus.
  - Hypothesis tested using Hayes Process Macro (Model 4) in SPSS, with bootstrapping for indirect effects.
findings:
  - num: Financial behavior explains 43.12% of variance in financial well-being (R²=.4312) among irregular income workers.
  - num: Financial well-being fully mediates the behavior-stress relationship (indirect effect=-.5045, 95% CI [-.6070, -.4119]).
  - num: Direct effect of financial behavior on stress was non-significant (β=-.1039, p=.0564), confirming full mediation.
  - num: Combined financial behavior and well-being explain 56.01% of stress variance (R²=.5601).
  - num: Financial behavior positively predicts financial well-being (β=.6566, p<.001), which negatively predicts stress (β=-.6761, p<.001).
  - Financial worry, a sign of poor well-being, is associated with psychological distress including stress, depression, and anxiety.
  - Budgeting behavior mitigates negative effects of income uncertainty, supporting COR theory's resource conservation framework.
key_figures_tables:
  - Figure 1: CFA second-order factor loadings for Financial Behavior scale (.511-.942) → Scale valid for Indonesian irregular income workers.
  - Figure 2: CFA first-order factor loadings for Financial Well-Being scale (.629-.926) → Unidimensional structure confirmed.
  - Figure 3: CFA first-order factor loadings for Stress scale (.536-.768) → DASS-21 stress dimension validated.
  - Table 7: Model summary results showing R² values for all paths → Full mediation model explains 56% of stress variance.
  - Table 8: Path coefficients with significance and confidence intervals → All direct paths significant except c' path.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Irregular Income Workers
    definition: Individuals whose income is unpredictable and fluctuates, lacking fixed or guaranteed regular earnings.
  - term: Financial Well-Being
    definition: Perceived adequacy and stability of financial resources, characterized by meeting obligations and feeling secure about the future.
  - term: Financial Behavior
    definition: Individual's ability to manage finances effectively including planning, budgeting, controlling, monitoring, and saving.
  - term: COR Theory
    definition: Conservation of Resources theory; stress results from threatened or lost resources, and individuals strive to protect and maintain them.
  - term: DASS-21
    definition: Depression, Anxiety, and Stress Scales-21; instrument measuring three negative emotional states including stress dimension.
  - term: IFDW Scale
    definition: InCharge Financial Distress/Financial Well-Being Scale; measures financial situation, money management, and bill-paying behavior.
  - term: FMBs Scale
    definition: Financial Management Behaviors Scale; assesses cash management, credit use, savings/investment, and insurance behavior.
  - term: Process Macro
    definition: Hayes' SPSS macro for mediation, moderation, and conditional process analysis with bootstrapping for indirect effects.
critical_citations:
  - "[Hobfoll, 1989] — COR theory foundation for stress-resource relationship."
  - "[Prawitz et al., 2006] — Financial well-being scale validation."
  - "[Dew & Xiao, 2011] — Financial Management Behavior Scale validation."
  - "[Hassan et al., 2021] — Systematic review linking financial well-being to mental health."
  - "[Bhattacharya & Ray, 2021] — Precarious work and mental health outcomes."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Paper studies Indonesian irregular income workers aged 20-40, analogous demographic to Filipino YPs with similar income instability concerns.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: contextual
      justification: Examines financial behavior and well-being of irregular income workers, highly relevant to understanding financial structures in unstable income contexts.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly investigates financial behavior (budgeting, saving, credit use, insurance) and its effects on well-being and stress in irregular income workers.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Financial behavior scale includes cash flow management and budgeting, informing how expense categorization frameworks should be designed.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: Findings on budgeting behavior (cash management, savings, credit) inform category design for irregular income users.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Paper segments financial behavior into four factors (cash, credit, savings/investment, insurance), informing behavioral profile construction.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Validated multidimensional financial behavior scale offers a classification framework for profiling users based on four behavior dimensions.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Savings and investment dimension of financial behavior directly relates to savings goal management in PFMS.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: medium
      justification: Credit management dimension addresses debt behavior, relevant for debt management module design.
  contribution: This paper directly justifies Odin's behavioral profiling module (5.A) by validating a multidimensional financial behavior scale with four factors. It supports the stress reduction and well-being improvement rationale for Odin's savings and debt management features (13.A, 13.B). The finding that financial well-being fully mediates the behavior-stress relationship provides design justification for features that directly improve users' perceived financial security and stability. The emphasis on budgeting behavior as a buffer against income uncertainty informs Odin's expense categorization and budget recommendation modules.
  directly_justifies:
    - "Financial behavior positively predicts financial well-being, supporting behavioral profiling as a foundation for feature design."
    - "Financial well-being fully mediates the relationship between financial behavior and stress, justifying well-being metrics in PFMS."
    - "Budgeting and savings behavior mitigate negative effects of income uncertainty, supporting proactive financial planning features."
    - "Credit management and savings behavior are distinct dimensions, justifying separate modules for debt and savings in PFMS."
  limits:
    - "Data collected via online questionnaire may introduce sampling bias due to restricted internet access."
    - "Scope confined to internal variables, excluding external factors (social support, environment) that influence stress."
  mapping_rationale: A systematic scan was conducted across all 12 functional domains and their associated topic codes. The following domains were flagged as relevant: Filipino Cultural Context (codes 1.A, 1.B, 1.C) with contextual relevance due to the Indonesian population being analogous to Filipino YPs; Expense Categorization (3.A, 3.B) with medium relevance as the financial behavior scale measures budgeting and cash management, informing expense category design; Behavioral Profiling (5.A, 5.C) with high relevance because the validated multidimensional scale directly informs profile construction and classification; and Savings & Debt Management (13.A, 13.B) with medium relevance through the savings/investment and credit management dimensions. The paper also touches on Spending Forecasting (6.A, 6.B) and Budget Recommendation (7.A, 7.B) through its emphasis on budgeting behavior, but these were not selected as primary because forecasting algorithms and optimization approaches are not addressed. Domains such as Anomaly Detection (8), Mobile-First Design (9), Data Privacy (10), Retention (11), and System Evaluation (12) were considered and rejected due to no relevant content. The paper's primary contribution lies in demonstrating the full mediation pathway, making it highly relevant for behavioral profiling and financial well-being features in Odin.
limitations:
  - "Online questionnaire may introduce sampling bias due to restricted internet access. [unacknowledged]"
  - "Scope confined to internal variables, excluding external factors (social support, environment) that may influence stress. [unacknowledged]"
remember_this:
  - "Financial well-being fully mediates the behavior-stress relationship in irregular income workers."
  - "Financial behavior explains 43.12 percent of variance in financial well-being."
  - "Combined financial behavior and well-being explain 56.01 percent of stress variance."
  - "Budgeting behavior mitigates negative effects of income uncertainty."
  - "Savings and credit management are distinct behavioral dimensions requiring separate PFMS modules."
```