```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international-algorithm-specific
title: Personal Financial Information Presentation and Consumer Spending
authors: Levi, Y.
year: 2025
venue: Unknown
odin_topics:
  - 2.B
  - 5.B
  - 6.B
  - 7.B
  - 8.B
  - 9.B
  - 11.A
  - 12.B
tldr: Consumers exposed to a consumption-oriented frame and a salient comparison of a personalized net-worth index with past spending reduced discretionary spending by 15%.
problem_and_motivation: Individuals interact with finances digitally, but the influence of information presentation on spending behavior is underexplored. A gap exists in understanding if simple design changes can overcome strong spending habits. This study tests if framing and salience of financial information can prompt consumers to adjust spending.
approach:
  - Randomized field experiment with 3,138 users of an online account aggregation app.
  - Personalized index presented net worth as lifetime monthly cash flow from an annuity.
  - Treatments varied index name: Financial Sustainability Index (FSI, consumption frame) vs. Life Annuity Index (LAI, neutral frame).
  - Salience manipulated by providing a context plot comparing the index to historical monthly spending.
  - Difference-in-differences analysis with individual and event-month fixed effects.
findings:
  - num: FSI-Plot group reduced discretionary spending by 15% relative to control during the 8-month experiment.
  - num: Effect persisted for 8 months after treatment removal, with a gradual return to baseline.
  - num: Spending decreased in restaurants (14%), clothing (20%), entertainment (14%), travel (24%), and cash withdrawals (25%).
  - No significant change in non-discretionary spending categories like gas, groceries, and utilities.
  - No effect from the index name or context plot alone; both consumption frame and salient context were necessary.
  - Login frequency increased similarly across all treated groups, controlling for attention effects.
key_figures_tables:
  - Figure 3: Monthly logins by treatment group → All treated groups increased logins similarly.
  - Figure 4: Monthly discretionary spending by treatment group → FSI-Plot groups diverged lower immediately at experiment start.
  - Table 5: Treatment effects on discretionary spending → FSI-Plot groups show 15% decrease during intra period.
  - Table 7: Spending category effects → Reductions largest in restaurants, clothing, entertainment, travel, and cash.
key_equations:
  - equation: y_{i,t} = \sum_{j=2}^{5} \beta_j TG_{j,i} Intra_t + \sum_{j=2}^{5} \gamma_j TG_{j,i} Post_t + \delta_i + \theta_j + \epsilon_{i,t}
    explanation: Main diff-in-diff specification with individual and month fixed effects.
definitions:
  - term: FSI
    definition: Financial Sustainability Index, the consumption-framed name for the personalized index.
  - term: LAI
    definition: Life Annuity Index, the neutral-framed name for the personalized index.
  - term: Personalized Index
    definition: Net worth presented as the equivalent inflation-protected lifetime monthly cash flow.
  - term: Context Plot
    definition: Time series plot directly comparing the index level with the user's historical monthly spending.
critical_citations:
  - "[Benartzi et al., 2011] — Annuitization puzzles and framing effects on annuity valuation."
  - "[Goldstein et al., 2016] — Illusion of wealth from lump-sum vs. cash-flow presentation."
  - "[Karlan et al., 2016] — Salient reminders promote staying within means."
  - "[Sussman and Alter, 2012] — Underestimation of exceptional expenses leads to overspending."
relevance:
  topics:
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: Provides evidence of spending adjustments in response to information, not seasonal drivers.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: Results suggest behavioral response to a reference point, but not directly profile classification.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: Uses historical spending data, but does not develop or test forecasting algorithms.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: Directly tests how presenting a benchmark (the index) influences spending, a core budget recommendation mechanism.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Examines spending changes in categories, but not anomaly detection methods.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Tests information presentation within a digital (app) environment, relevant to UX design choices.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Measures login behavior as a proxy for attention, relevant to engagement.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides a rigorous experimental evaluation framework (RCT, diff-in-diff) applicable to evaluating Odin's modules.
  contribution: This paper provides a rigorous experimental framework for testing information presentation effects, directly applicable to evaluating Odin's budget recommendation module. The finding that a salient benchmark reduces spending offers a design principle for Odin's interface to encourage savings. The persistence of the effect beyond treatment exposure informs retention strategies for Odin. The detailed spending category analysis can guide Odin's expense categorization and anomaly detection design by highlighting responsive categories.
  directly_justifies:
    - A consumption-oriented frame combined with a salient context can reduce discretionary spending by 15%.
    - Information design can influence spending behavior without changing economic variables.
    - Effects persist for months after treatment removal, suggesting habit formation.
    - Non-discretionary spending is less responsive to information interventions.
  limits:
    - Sample consists of relatively wealthy users (top 20% income), limiting generalizability to lower-income Filipino young professionals.
    - Data may be incomplete if users did not link all financial accounts to the app.
    - The experiment was conducted in 2014, before pre-registration became common.
    - The study population is U.S.-based, which may not fully reflect Filipino cultural and financial contexts.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated canonical topic codes was conducted. The paper was flagged as relevant primarily for the "Budget Recommendation" (7.B) and "System Evaluation" (12.B) domains, receiving a 'high' relevance assignment, as the experimental design directly tests a benchmark-based spending adjustment mechanism and provides a rigorous evaluation framework. It also touches on "User Retention & Engagement" (11.A) and "Mobile UX Design" (9.B) with a 'medium' relevance, as the study measures attention effects and manipulates in-app information presentation. Topics related to "Seasonal Spending" (2.B) and "Profile Dynamics" (5.B) were considered but assigned 'low' relevance, as the paper does not directly model seasonality or user profiles. Domains like "Anomaly Detection" (8.B) and "Forecasting" (6.B) were rejected for direct inclusion, as the paper does not propose or evaluate algorithms in these areas. The paper's overall relevance is moderate, providing a foundational experimental paradigm and evidence of behavioral responsiveness to information design, but its U.S.-based, high-income sample limits direct applicability to the Filipino young professional demographic.
limitations:
  - Sample consists of relatively wealthy U.S. users, limiting generalizability to Filipino young professionals. [unacknowledged]
  - Potential incompleteness of transaction data from account aggregation. [unacknowledged]
  - Experiment was conducted in 2014, before pre-registration became common.
  - The study does not explore the exact psychological mechanism (e.g., anchoring vs. reference point updating).
remember_this:
  - Presenting a consumption-framed benchmark with a context plot reduced discretionary spending by 15%.
  - The spending reduction persisted for eight months after the intervention was removed.
  - Largest decreases occurred in restaurants, clothing, entertainment, travel, and cash withdrawals.
  - Information design effects require both a relevant frame and a salient comparison context.
  - Login frequency increased similarly across all treatments, ruling out attention as the primary driver.
```