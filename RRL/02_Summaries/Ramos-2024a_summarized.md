```yaml
paper_id: 10.1177/09500170241247121
designation: local
title: Extreme Lockdowns and the Gendered Informalization of Employment: Evidence from the Philippines
authors: Ramos, V. J.
year: 2024
venue: Work, Employment and Society
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 10.A
tldr: Extreme lockdowns in the Philippines increased informal employment probability among employed women by 2.2 percentage points, driven by survivalist motives and compositional changes.
problem_and_motivation: The impact of extreme mobility restrictions on informal employment, distinct from pandemic recessionary effects, is understudied. Understanding gendered informalization is critical for designing targeted safety nets, especially in developing countries with large informal sectors and limited welfare support.
approach:
  - Used 16 pooled quarterly Labour Force Survey rounds (2016-2020) from the Philippines.
  - Applied a two-way fixed effects difference-in-differences design comparing lockdown and non-lockdown regions.
  - Defined informal employment per ILO guidelines, excluding professional, agricultural, and public sector workers.
  - Conducted heterogeneous analyses by gender, marital status, and presence of minor children.
  - Tested robustness using alternative age restrictions, time periods, and informal employment definitions.
findings:
  - Extreme lockdowns increased the probability of informal employment by 1.7 percentage points overall.
  - num: The effect was 2.2 percentage points for women and statistically insignificant for men.
  - num: The informalization effect was strongest for married/cohabiting women with minor children, at 8.0 percentage points.
  - num: Around 44% of households in lockdown regions engaged in additional income-generating work.
  - Compositional changes showed formal employment declined more than informal employment in lockdown areas.
  - Survivalist motives were supported as males were more likely to be informally employed than unemployed.
  - Women in lockdown regions experienced a steeper increase in informal employment rates than men.
  - The gendered informalization finding is robust across alternative definitions of informal employment.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Compositional informalization
    definition: Informality induced by changes in the size and composition of overall employment.
  - term: Survivalist informalization
    definition: Informality induced by the need to work due to absent welfare support and low savings.
  - term: Two-way fixed effects difference-in-differences
    definition: An econometric method using region and time fixed effects to estimate causal effects.
critical_citations:
  - "[ILO, 2020] — Established informal workers were directly affected by lockdowns."
  - "[Maurizio, 2021] — Found informal employment did not play its usual countercyclical role in Latin America."
  - "[Floro and Meurs, 2009] — Demonstrated gendered informalization after the Asian Financial Crisis."
  - "[Ducanes and Ramos, 2023] — Showed female employment declines in Philippines during lockdowns."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Directly analyzes labor market outcomes for Filipino workers.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Discusses low savings rates and lack of social protection as drivers of informalization.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Examines survivalist motives and coping mechanisms during crises.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Describes the survivalist motive as a culturally embedded coping strategy.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Contextualizes economic shocks but does not directly analyze seasonal spending.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Mentions crisis-driven spending but not cyclical occasions.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews state social assistance mechanisms as context.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies gaps in social protection and safety nets.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Provides empirical evidence of survivalist behavioral profiles.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: high
      justification: Demonstrates how crises shift workers into informal profiles.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Relies on survey data but does not address privacy.
  contribution: "This paper provides a causal framework for understanding how external shocks (lockdowns) drive informalization, which is critical for Odin's behavioral profiling module. The distinction between compositional and survivalist informalization offers a taxonomy for classifying user financial behaviors during crises. The finding that women with minor children are most affected informs Odin's cold-start handling for female users. The documented lack of social protection mechanisms underscores the need for Odin's proactive budgeting and savings features. The survivalist motive evidence supports Odin's design of flexible budget constraints to accommodate crisis-driven financial behaviors."
  directly_justifies:
    - "Extreme lockdowns increase informal employment probability among women by 2.2 percentage points."
    - "Women with minor children faced an 8.0 percentage point higher informalization risk."
    - "Survivalist motives drive workers to accept informal jobs over unemployment."
    - "Households with low savings are more likely to engage in informal income-generating work."
    - "Compositional changes alone cannot explain gendered informalization; survivalist motives matter."
  limits:
    - "LFS data undercount informal employment, potentially underestimating the true lockdown effect."
    - "Absence of panel data prevents tracking individual transitions into informal work."
    - "Sector-specific differences in informal employment are not analyzed."
    - "The study does not differentiate between voluntary and involuntary informal employment."
  mapping_rationale: "A systematic scan of all 12 functional domains and their 28 associated topic codes was conducted. Domains flagged as relevant include Filipino Cultural Context (2.A, 2.B, 2.D), Existing Systems & Gaps (4.A, 4.B), Behavioral Profiling (5.A, 5.B), and Data Privacy (10.A) as contextual. Topic 1.A (Filipino Young Professionals) was assigned high relevance as the paper directly studies Filipino workers. Topic 1.B (Financial Structure) was high due to low savings and welfare gaps. Topic 1.C (Financial Behavior) was high for survivalist motives. Topic 2.A (Cultural Practices) was medium for coping strategies. Topic 2.B (Seasonal Patterns) was contextual, as the paper does not analyze seasonal spending. Topic 2.D (Spending Cycles) was low, with only passing mention. Topic 4.A (Existing Systems) was medium for reviewing social assistance. Topic 4.B (Gaps) was high for identifying welfare shortcomings. Topic 5.A (Behavioral Profiles) was high for demonstrating crisis-induced informal profiles. Topic 5.B (Cold-Start) was high for showing how shocks shift profiles. Topic 10.A (Privacy) was contextual, as privacy is not addressed. Domains like Spending Forecasting (6), Budget Recommendation (7), and Anomaly Detection (8) were rejected as the paper does not address predictive modeling or algorithmic recommendations. The overall relevance is high for Odin's behavioral and contextual modules, providing foundational evidence for crisis-driven financial behavior and gender-sensitive design."
limitations:
  - "LFS data undercount informal employment in developing countries. [unacknowledged]"
  - "No panel data to analyze individual transitions. [unacknowledged]"
  - "Sector-specific differences are not explored. [unacknowledged]"
  - "The study does not differentiate voluntary from involuntary informal employment. [unacknowledged]"
remember_this:
  - "Extreme lockdowns increased informal employment by 2.2 percentage points for women."
  - "Mothers with minor children faced an 8.0 percentage point informalization risk."
  - "Survivalist motives drove workers to informal jobs over unemployment."
  - "Low social protection and savings are key drivers of crisis informalization."
  - "Gendered informalization is robust across alternative definitions and samples."
```
