```yaml
paper_id: b9c0c8e3-2c9b-5e8d-9a1b-8c6f4e3a2d7e
designation: local
title: Big Five Personality Traits and Financial Literacy: Effect on Risk Tolerance of Filipino Investors from Higher Education Institutions in Metro Manila
authors: Mendoza, D. M.; Padernal, A. M. G.; Pante, E. M. S.; Magbata, E. V. S.; Mandigma, M. B. S.
year: 2023
venue: Review of Integrative Business and Economics Research
odin_topics:
  - 1.C
  - 5.A
  - 5.B
  - 5.C
tldr: Extraversion, openness, neuroticism, and financial literacy positively influence risk tolerance among Filipino investors, while agreeableness and conscientiousness do not.
problem_and_motivation: Understanding the factors that influence investor risk tolerance is critical for financial decision-making, yet the combined effect of personality traits and financial literacy on Filipino investors remains underexplored. This gap hinders the development of tailored financial advice and educational programs in the Philippine context.
approach:
  - Surveyed 320 students and faculty from Metro Manila higher education institutions using a four-point Likert scale.
  - Measured risk tolerance, Big Five personality traits, and financial literacy via adapted and modified questionnaires.
  - Employed multiple regression analysis to determine the influence of independent variables on risk tolerance.
  - Used snowball sampling to reach participants who invest at least PHP 1,000 in stocks, bonds, or cryptocurrency.
  - Controlled for age and monthly family income in a subsequent regression model.
findings:
  - Extraversion, openness to experience, and neuroticism significantly and positively influence risk tolerance.
  - Financial literacy has a significant positive influence on risk tolerance, with the highest standardized coefficient (Beta = 0.504).
  - Agreeableness and conscientiousness do not have a significant influence on risk tolerance.
  - num: The regression model with personality traits and financial literacy explains 43.6% of the variance in risk tolerance (R² = 0.436).
  - num: Including age and income as control variables increases the explained variance to 45.1% (R² = 0.451).
  - Monthly family income has a significant negative influence on risk tolerance when controls are added.
  - Age is not a significant predictor of risk tolerance in the model with controls.
  - The study provides empirical evidence from a Filipino sample, a demographic often underrepresented in behavioral finance research.
  - The findings support the Prospect Theory by showing differential risk attitudes based on personal factors.
key_figures_tables:
  - Table 1: Cronbach's Alpha values for Big Five (.913), Financial Literacy (.918), and Risk Tolerance (.881) → All constructs have high internal consistency.
  - Table 2: Demographic profile of respondents → Majority are female (68.75%), aged 18-25 (92.81%), and students (89.06%).
  - Table 3: Descriptive statistics → Openness has the highest mean (3.18) among personality traits, indicating high agreement.
  - Table 4: Multiple regression results → Extraversion, openness, neuroticism, and financial literacy are significant predictors of risk tolerance.
  - Table 5: Regression with controls → Income negatively influences risk tolerance; age is insignificant.
key_equations:
  - equation: Risk Tolerance = 0.882 + 0.091E + 0.086O + 0.089N + 0.474FL
    explanation: Predicts risk tolerance from significant personality traits and financial literacy.
definitions:
  - term: Risk Tolerance
    definition: The maximum uncertainty an investor is willing to accept before making a financial decision.
  - term: Financial Literacy
    definition: Knowledge and ability to manage personal finances effectively.
  - term: Big Five Personality Traits
    definition: Five broad domains of personality: openness, conscientiousness, extraversion, agreeableness, and neuroticism.
critical_citations:
  - "[Pak & Mahmood, 2015] — Foundational for personality trait measurement in this context."
  - "[Hamza & Arif, 2019] — Basis for financial literacy questionnaire used."
  - "[Ainia & Lutfi, 2019] — Source of risk tolerance scale adapted for this study."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly examines financial behavior (risk tolerance) of Filipino investors.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Links personality traits to financial risk tolerance, a key behavioral profile.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: Provides empirical basis for initial user profiling using personality and literacy.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Demonstrates regression analysis to classify/explain risk tolerance based on predictors.
  contribution: This paper provides a validated model linking personality traits and financial literacy to risk tolerance, directly informing Odin's user profiling module for Filipino young professionals. The significant influence of extraversion, openness, neuroticism, and financial literacy on risk tolerance offers a foundation for building behavioral profiles. The finding that agreeableness and conscientiousness are non-significant can refine feature selection for classification algorithms. The negative influence of income on risk tolerance, when controlled for, adds a layer of socioeconomic nuance to user modeling. Overall, the study's empirical framework and localized data directly support the design of Odin's behavioral assessment and personalization features.
  directly_justifies:
    - Odin's behavioral profiling module can use extraversion, openness, neuroticism, and financial literacy scores to estimate user risk tolerance.
    - Financial literacy is a crucial predictor of risk behavior and should be a core component of user onboarding assessment.
    - The non-significance of agreeableness and conscientiousness suggests these traits may be deprioritized in Odin's initial risk tolerance models.
    - The negative influence of income on risk tolerance, after accounting for other factors, indicates a complex relationship to be incorporated into user models.
    - The study's use of a Filipino sample provides culturally relevant data for calibrating Odin's algorithms for the target demographic.
  limits:
    - The sample is limited to students and faculty, not fully representing all Filipino investor groups.
    - Data was collected online, which may introduce selection bias.
    - The cross-sectional design cannot establish causation between personality/literacy and risk tolerance.
    - Reliance on self-reported measures may be subject to social desirability bias.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The domain "Behavioral Profiling & Classification" was flagged as directly relevant, leading to the selection of codes 5.A (high), 5.B (medium), and 5.C (medium) because the paper empirically establishes personality and literacy as predictors of risk tolerance, which is a core behavioral profile. The domain "Filipino Cultural Context" was considered but only code 1.C (Financial Behavior) was selected as high relevance due to the focus on Filipino investor behavior. Other domains such as "Spending Forecasting" (6.A, 6.B), "Budget Recommendation" (7.A-D), "Anomaly Detection" (8.A-C), "Mobile-First Design" (9.A, 9.B), "Data Privacy" (10.A, 10.B), and "System Evaluation" (12.A-C) were rejected as the paper does not address these algorithmic or design aspects. The domain "Existing Systems & Gaps" (4.A, 4.B) was rejected because the paper does not review existing systems. The domain "User Retention & Engagement" (11.A, 11.B) was rejected. The domain "Savings & Debt Management" (13.A-C) was rejected. The paper's overall relevance to Odin is moderate, providing foundational knowledge for user profiling but lacking direct application to Odin's core algorithmic functions.
limitations:
  - Sample demographics skew young and female, limiting generalizability to all Filipino investors. [unacknowledged]
  - Causality cannot be inferred due to the correlational design.
  - The study did not control for other potential confounding variables like financial experience or risk perception.
  - The use of a convenience sample (snowball) may introduce bias.
  - Generalizing findings to other economic or political contexts may not be valid.
remember_this:
  - Financial literacy has the strongest positive influence on risk tolerance.
  - Extraversion, openness, and neuroticism significantly increase risk tolerance.
  - Agreeableness and conscientiousness do not significantly affect risk tolerance.
  - num: Personality traits and literacy explain 43.6% of risk tolerance variance.
  - Monthly family income negatively affects risk tolerance when controlled for.
```