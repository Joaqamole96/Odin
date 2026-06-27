```yaml
paper_id: 10.20944/preprints202508.0349.v1
designation: local-algorithm-specific
title: Analysis of the Food and Income Expenditure Survey 2023 Among Filipino Households
authors: Ama, N. A.
year: 2025
venue: Preprints.org
odin_topics:
  - 2.A
  - 2.B
  - 2.D
  - 3.A
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 6.A
  - 7.A
  - 8.A
  - 12.A
  - 13.A
tldr: Filipino household food spending is income-inelastic, spatially clustered, and higher in rural areas, with household size, income, and location as key nonlinear predictors of food insecurity.
problem_and_motivation: Understanding drivers of food expenditure among Filipino households is fundamental to shaping effective social, agricultural, and economic policies, yet detailed analysis of 2023 FIES data remains limited. This study addresses the gap by using advanced statistical methods to assess how income, geography, livelihood sources, and household characteristics shape food spending patterns and food insecurity.
approach:
  - Data from 163,268 households in the 2023 Philippine Family Income and Expenditure Survey (FIES) were analyzed using RStudio v4.5.1.
  - Principal Component Analysis (PCA) identified dominant income sources, supported by scree plots and loading scores.
  - Spatial clustering was evaluated via regional mapping using GADM shapefiles and visualizations.
  - Rural-urban differences were tested using the non-parametric Mann-Whitney U test due to normality violations.
  - A Generalized Additive Model (GAM) was employed to predict food insecurity, incorporating smooth terms for continuous predictors and a parametric term for urban-rural residence.
  - Log-log Engel curves and a beta regression model were used to analyze income elasticity and the proportion of food spent outside the home, respectively.
findings:
  - num: Food expenditure has an income elasticity of 0.58, confirming food as a necessity good under Engel's Law.
  - num: Rural households spend more on food (Median = ₱102,467) than urban households (Median = ₱80,700).
  - PCA identified retail, transport, and agriculture as dominant income source clusters.
  - Spatial clustering shows Leyte and Bohol have the highest mean food expenditure (≥₱120,000).
  - The GAM explained 27.2% of deviance in food insecurity, with RPCINC as the strongest nonlinear predictor.
  - num: The GAM achieved 90.02% accuracy and an AUC of 0.86 in predicting food insecurity.
  - Urban residence (β = -0.51) was associated with a lower likelihood of food insecurity.
  - Household size showed a significant nonlinear positive association with food insecurity risk.
  - Bread (29.5%) and meat (14.8%) account for the largest shares of food expenditure.
  - Higher-income and rural households spend a larger proportion of food outside the home.
key_figures_tables:
  - Figure 1: Lorenz curve of food expenditure → Food spending is more evenly distributed than income.
  - Figure 2: Histogram of food expenditure per member → Distribution is right-skewed with concentration at lower values.
  - Figure 5: Spatial map of mean food expenditure → High-spending clusters in Leyte and Bohol.
  - Figure 8: GAM partial effect plots → Income and household size show strong nonlinear effects on food insecurity.
  - Figure 10: Engel curve log-log plot → Positive but inelastic relationship between income and food spending.
key_equations:
  - equation: U = n1 * n2 + (n1(n1+1))/2 - R1
    explanation: Mann-Whitney U test statistic for group comparisons.
  - equation: g(E(Y)) = β0 + f1(x1) + ... + fm(xm)
    explanation: Generalized Additive Model with logit link function.
  - equation: log(FOOD_i) = β0 + β1 * log(TINC_i) + ε_i
    explanation: Log-log Engel curve for estimating income elasticity.
  - equation: logit(μ_i) = β0 + β1 * log(INCOME_i) + β2 * URB_i + β3 * FSIZE_i
    explanation: Beta regression model for proportion of food spent outside home.
definitions:
  - term: FIES
    definition: Family Income and Expenditure Survey conducted by the Philippine Statistics Authority.
  - term: PCA
    definition: Principal Component Analysis, a dimensionality reduction technique.
  - term: GAM
    definition: Generalized Additive Model, a flexible regression framework for nonlinear effects.
  - term: RPCINC
    definition: Real per capita income, adjusted for household size.
  - term: Engel's Law
    definition: As income rises, the proportion of income spent on food declines.
  - term: Beta regression
    definition: A regression model for proportions bounded between 0 and 1.
critical_citations:
  - "[Valera et al., 2022] — Found inelastic demand for rice and flexible preferences for meat and dairy."
  - "[Briones, 2022] — Examined food price shocks and cash transfer effects on nutrient intake."
  - "[Bairagi et al., 2022] — Identified structural shifts in rural vs. urban food basket composition."
  - "[Cigaral, 2025] — Reported food as the largest expenditure share (57.2%) in 2021."
relevance:
  topics:
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Highlights dominance of bread and meat in spending, reflecting local dietary patterns.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: Spatial and rural-urban spending variations suggest cyclical/geographic influences.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Mentions spending outside home, but not explicitly tied to festive occasions.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Provides empirical distribution of spending across major food categories.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: References BSP survey and PSA FIES as data sources for understanding spending.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: low
      justification: Acknowledges cross-sectional nature and lack of dietary/nutritional detail.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: PCA-based livelihood segmentation offers a proxy for behavioral profiles.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: contextual
      justification: Segmentation by income sources can inform initial profile estimation.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: GAM and Engel curve analysis demonstrate predictive modeling of food spending.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Income elasticity and food share patterns inform budget allocation strategies.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Identifies spending clusters and outliers in food expenditure distribution.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses accuracy, AUC, and R² to evaluate GAM classification performance.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: contextual
      justification: Food spending patterns indirectly relate to surplus available for savings.
  contribution: "The paper provides empirical benchmarks for income elasticity of food (0.58) and food expenditure distributions that can calibrate Odin's budget recommendation module. Its GAM framework for predicting food insecurity offers a methodological template for Odin's behavioral risk assessment. The PCA-derived livelihood segmentation can inform Odin's cold-start profiling for new users. The rural-urban spending differences provide contextual data for Odin's geographic customization. The beta regression for out-of-home food spending supports Odin's expense categorization logic."
  directly_justifies:
    - "Income elasticity of 0.58 establishes food as a necessity for Filipino households."
    - "Rural households exhibit higher median food spending (₱102,467) than urban (₱80,700)."
    - "Household size and income are significant nonlinear predictors of food insecurity."
    - "Bread and meat account for 29.5% and 14.8% of food expenditure, respectively."
    - "GAM models can achieve 90% accuracy in predicting household financial vulnerability."
  limits:
    - "Cross-sectional FIES data limits causal inference on spending dynamics. [unacknowledged]"
    - "Lack of nutritional/dietary diversity measures restricts analysis of food quality."
    - "Provincial-level aggregation obscures intra-regional disparities."
    - "Self-reported income may suffer from recall bias, especially in informal sectors."
    - "No detailed evaluation of algorithmic modules for budget recommendation is provided."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes identified relevant connections. Domains flagged as relevant include Filipino Cultural Context (2.A, 2.B, 2.D), Expense Categorization (3.A), Existing Systems (4.A, 4.B), Behavioral Profiling (5.A, 5.B), Forecasting (6.A), Budget Recommendation (7.A), Anomaly Detection (8.A), and Evaluation (12.A). High relevance was assigned to 6.A due to the predictive GAM and Engel curve modeling. Medium relevance was assigned to 2.A, 2.B, 3.A, 5.A, 7.A, 12.A, and 13.A based on empirical spending patterns. Borderline cases include 2.D (spending cycles) and 7.C (constrained optimization) — the paper discusses Engel curves but not optimization, so 7.C was rejected. Domains 9.A, 9.B, 10.A, 10.B, 11.A, 11.B, and 13.C were rejected as the paper does not address mobile design, privacy, retention, or surplus mechanisms. Overall, the paper provides strong empirical grounding for Odin's core financial understanding modules."
limitations:
  - "Cross-sectional design cannot establish causal relationships between income and food spending. [unacknowledged]"
  - "Lack of detailed nutritional and dietary diversity measures limits holistic food security assessment. [unacknowledged]"
  - "Spatial analysis limited to provincial aggregates, hiding intra-provincial disparities."
  - "Reliance on self-reported data may introduce recall bias among informal sector households."
  - "Beta regression pseudo-R² of 0.1403 indicates limited explanatory power for out-of-home food spending. [unacknowledged]"
remember_this:
  - "Food expenditure income elasticity is 0.58, confirming Engel's Law for Filipino households."
  - "Rural households spend more on food and face higher food insecurity risk."
  - "GAM achieved 90% accuracy in predicting food insecurity from household characteristics."
  - "Bread (29.5%) and meat (14.8%) dominate Filipino household food spending."
  - "Household size and income exhibit strong nonlinear associations with food insecurity."
```