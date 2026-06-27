```yaml
paper_id: 10.23919/JSC.2025.0015
designation: international
title: Consumer Autonomy or Illusion? Rethinking Consumer Agency in the Age of Algorithms
authors: Nokhiz, P.; Ruwanpathirana, A. K.
year: 2025
venue: Journal of Social Computing
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.B
  - 2.D
  - 4.B
  - 5.A
  - 5.B
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 7.D
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 13.A
tldr: Formal analysis demonstrates that limited consumer agency from obligatory consumption, algorithmic persuasion, and work instability leads to financial ruin even for rational utility-maximizing agents.
problem_and_motivation: Consumers face systemic barriers and algorithmic manipulation that erode financial autonomy, yet the consequences of diminished agency are not formally understood. This gap prevents the design of effective interventions to protect consumer welfare and promote genuine agency.
approach:
  - Uses discounted utility models to analyze intertemporal consumption under agency constraints.
  - Constructs analytical scenarios for obligatory consumption, algorithmic impulse spending, and unpredictable work schedules.
  - Formalizes financial ruin as a state where assets reach zero within a finite time horizon.
  - Applies Jensen's inequality and concentration inequalities to prove ruin under concave utility.
  - Demonstrates that advance schedule knowledge (lookahead) significantly improves utility and reduces ruin risk.
findings:
  - num: Rational agents under obligatory consumption can achieve higher utility by consuming all assets and going to ruin within a finite time.
  - num: Under impulsive consumption with minimum subsistence, the probability of avoiding ruin decays exponentially with time.
  - num: Workers with k-step lookahead achieve utility that is Ω(k) greater than those without lookahead.
  - num: Low-income agents experience near-instantaneous ruin under impulsive consumption, while high-income agents show delayed collapse.
  - num: Agents with high-school education (lower discount factor) exhibit ruin within 20 steps, whereas college-educated agents show more spread in ruin times.
  - Consumer agency must be treated as a value requiring active cultivation, not an inherent given.
  - Value deliberation interventions enable consumers to avoid ruin when income covers basic needs.
key_figures_tables:
  - "Figure 1: Summary of limited agency scenarios and outcomes → Visualizes how obligatory, impulsive, and temporal constraints lead to ruin."
  - "Figure A1: Ruin times under algorithmic persuasion → Most agents ruin within first 10 months under impulsive consumption."
  - "Figure A2: Ruin times by income level → Low-income agents ruin instantly; high-income show delayed but still rapid ruin."
  - "Figure A3: Ruin times by education → High-school diploma holders ruin within 20 steps; college degree holders show more spread."
key_equations:
  - equation: "max E[∑_{t=0}^{∞} β^t u(c_t)]"
    explanation: "Maximizes discounted utility over infinite horizon."
  - equation: "a_{t+1} = R(a_t - c_t) + y_t"
    explanation: "Asset evolution equation with return R and income y."
  - equation: "0 ≤ c_t ≤ a_t"
    explanation: "Consumption constrained by available assets."
  - equation: "Pr(a_T ≤ 0) ≥ 1 - exp(-cT)"
    explanation: "Probability of ruin grows exponentially with time."
definitions:
  - term: Ruin
    definition: "State where consumer assets reach zero within a finite time horizon."
  - term: Lookahead
    definition: "Number of future time steps an agent can perfectly foresee income and financial shocks."
  - term: Obligatory Consumption
    definition: "Fixed expenses driven by social, legal, or infrastructural pressures that limit consumer choice."
  - term: Algorithmic Persuasion
    definition: "Manipulative digital tactics that steer consumers toward impulsive spending."
  - term: Value Deliberation
    definition: "Active evaluation of competing needs and preferences to make consumption decisions aligned with personal values."
critical_citations:
  - "[Pariser, 2011] — Introduces filter bubbles and algorithmic curation."
  - "[Mathur et al., 2019] — Documents dark patterns in digital interfaces."
  - "[Nguyen, 2024] — Defines value capture in algorithmic systems."
  - "[Frederick et al., 2002] — Reviews time discounting and preference."
  - "[Schneider & Harknett, 2019] — Documents work schedule instability effects."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: low
      justification: "Discusses general consumer agency, not specific to Filipino young professionals."
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: low
      justification: "Uses U.S. income data and models, not Philippine-specific financial structures."
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: low
      justification: "Provides general behavioral insights applicable broadly."
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: high
      justification: "Formalizes predictable spending cycles through fixed obligatory consumption patterns."
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: medium
      justification: "Obligatory consumption framework applies to cultural spending cycles."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: "Identifies algorithmic manipulation and lack of agency as key system gaps."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: "Models rational agent behavior under agency constraints and proposes profiles for deliberation."
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: "Discusses adaptation and value deliberation over time."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: contextual
      justification: "Uses predictive models of ruin but does not focus on forecasting algorithms."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: contextual
      justification: "Mentions lookahead but not specific forecasting algorithms."
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: "Proposes value deliberation and budgeting as solutions to agency erosion."
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: "Demonstrates that deliberate consumption choices improve financial outcomes."
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: high
      justification: "Introduces minimum subsistence constraints and shows how to avoid ruin with proper budgeting."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: "Ruin analysis provides a framework for detecting financial instability."
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: "Mentions detection of impulsive spending but not specific algorithms."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: "Does not address privacy or security directly."
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: "Discusses transparency and ethical AI as trust-building mechanisms."
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: "Analyzes how algorithmic persuasion manipulates engagement and spending."
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: high
      justification: "Algorithmic tactics like scarcity and FOMO are explicitly linked to retention and spending."
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: "Proves that value deliberation and budgeting enable saving and avoid ruin."
  contribution: "This paper provides a formal framework for analyzing consumer agency erosion, which can inform Odin's design of user-facing budget recommendation and behavioral profiling modules. Its analytical models of ruin under limited agency justify the need for proactive intervention mechanisms in PFMS. The proposed value deliberation approach aligns with Odin's goal of fostering user autonomy and financial well-being. The theorem on lookahead utility directly supports incorporating schedule-aware features for users with variable income."
  directly_justifies:
    - "Even rational utility-maximizing agents can face financial ruin when agency is limited across structural, behavioral, or temporal dimensions."
    - "Value deliberation and budgeting interventions can help consumers avoid financial ruin when income covers basic needs."
    - "Workers with greater advance knowledge of income schedules achieve significantly higher utility, supporting the need for prediction-aware features."
    - "Algorithmic persuasion creates value capture where consumers adopt externally imposed consumption values without critical reflection."
  limits:
    - "Model assumes rational utility-maximizing agents, which may not reflect real-world behavioral biases."
    - "Does not include debt, credit, or liabilities in the formal model."
    - "Assumes societal uniformity; does not account for disparities in algorithmic targeting or policy access."
    - "Proposed interventions are high-level and lack specific implementation details for PFMS."
  mapping_rationale: "Systematic scan across all 12 functional domains identified 4 domains as highly relevant: Filipino Cultural Context (2.B, 2.D), Behavioral Profiling (5.A), Budget Recommendation (7.A, 7.D), and User Retention (11.A, 11.B). The paper's formal models of obligatory consumption (2.B) and algorithmic persuasion (11.A) provide direct justification for Odin's budgeting and engagement modules. The lookahead theorem (6.A, 6.B) supports forecasting features. Expense Categorization (3.A-C) and Anomaly Detection (8.A-C) were considered but rejected as the paper does not address categorization algorithms or anomaly detection techniques. Mobile-First Design (9.A, 9.B) and Data Privacy (10.A) were considered contextual. The paper's overall relevance to Odin is high, providing theoretical justification for user autonomy and proactive intervention features."
limitations:
  - "Intertemporal consumption model assumes rational utility-maximizing agents, simplifying real-world behavioral complexity."
  - "Debt and liabilities are not included in the formal framework."
  - "Model assumes societal uniformity and does not account for demographic disparities in algorithmic targeting."
  - "Proposed interventions are high-level and lack specific implementation details."
  - "Behavioral economics factors like present bias and loss aversion are acknowledged but not formally incorporated. [unacknowledged]"
  - "External macro-socioeconomic impacts like inflation and recessions are not modeled. [unacknowledged]"
remember_this:
  - "num: Even rational consumers can go to ruin under obligatory consumption with concave utility."
  - "num: Probability of avoiding ruin decays exponentially under impulsive consumption with minimum subsistence."
  - "num: Workers with advance schedule knowledge achieve Ω(k) higher utility than those without."
  - "Consumer agency must be actively cultivated as a value, not assumed as a given."
  - "Value deliberation and budgeting interventions enable consumers to avoid financial ruin."
```