```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: local
title: Effects of Filipino Consumers' Financial Attitudes, Subjective Norms, and Perceived Behavioral Control on Intentions to Formal Banking: Towards Financial Inclusion
authors: Co, M.; Centeno, D.D.G.
year: 2023
venue: Philippine Management Review
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
  - 7.A
  - 7.B
  - 12.A
  - 12.B
  - 13.A
  - 13.C
tldr: Subjective norms and perceived behavioral control significantly predict Filipino intentions to save surplus money in formal banks, while general attitudes do not.
problem_and_motivation: Financial exclusion among Filipinos is often attributed to supply-side factors like cost and access, but the psychological and behavioral drivers on the demand side remain underexplored in local research. This gap limits the effectiveness of financial inclusion strategies that fail to address individual attitudes, social influences, and perceived behavioral control over saving. The paper aims to quantify how these factors affect intentions to use formal banking services.
approach:
  - Data from the 2014 Bangko Sentral ng Pilipinas Consumer Finance Survey with 15,503 households was analyzed.
  - A logistic regression model was constructed to predict the intention to deposit surplus money in a bank.
  - Independent variables included attitudes, subjective norms, perceived behavioral control, and demographic factors.
  - Subjective norm was proxied by the presence of a banked household member, and behavioral control by two survey items on saving capability.
  - Marginal effects were estimated using the delta method to interpret the predictors' influence.
findings:
  - num: Presence of a banked household member increases the probability of banking intention by 10.16 percentage points.
  - num: Perceived behavioral control statements significantly affect intention, with one item increasing probability by 1.42% and another decreasing it by 2.54%.
  - num: College graduates are 7.95 percentage points more likely to intend banking than non-graduates.
  - num: Males are 2.02 percentage points more likely to intend banking than females.
  - num: Middle-income individuals are 3.18 percentage points more likely than low-income to intend banking, while high-income individuals are 10.14 percentage points less likely.
  - Attitudes towards banking, though directionally consistent, were not a statistically significant predictor of intention.
  - Older generations (Baby Boomers) showed lower intention compared to Millennials.
  - Employment status was negatively associated with banking intention, contrasting with initial hypotheses.
key_figures_tables:
  - Table 1: Response rates of the household survey → 86.1% overall response rate from a sample of 18,000 households.
  - Table 2: Descriptive statistics of the sample → 87.6% of respondents are unbanked, but 41.2% express deposit intention.
  - Table 3: Logistic regression results → Subjective norms and perceived behavioral control are significant predictors of banking intention.
  - Table 4: Marginal effects of independent variables → Presence of a banked household member has the strongest marginal effect (10.16%).
key_equations:
  - equation: 'Logit(P(Bank)) = α + β1X1 + β2X2 + … + βkXk'
    explanation: Logistic model predicting probability of banking intention from independent variables.
definitions:
  - term: Theory of Planned Behavior
    definition: Framework linking attitudes, subjective norms, and perceived behavioral control to behavioral intentions.
  - term: Subjective norm
    definition: Perceived social pressure to perform or not perform a behavior, proxied by the presence of a banked family member.
  - term: Perceived behavioral control
    definition: One's perception of ease or difficulty in performing a behavior, measured through statements about earning and saving.
  - term: Financial inclusion
    definition: State of effective access to quality, responsive financial products and services for all sectors.
critical_citations:
  - '[Ajzen, 1991] — Foundational theory linking behavioral control to intention.'
  - '[BSP, 2014] — Primary data source for the nationwide consumer finance survey.'
  - '[Croson & Gneezy, 2009] — Documented gender differences in financial risk and behavior.'
  - '[Bandura, 1971] — Social learning theory underpinning the role of household influence.'
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Paper analyzes banking intentions across age, income, and education, directly profiling this demographic.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Examines income, employment, and household size as predictors of banking behavior.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly investigates the financial behavioral intentions of Filipinos towards formal banking.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Discusses social norms and family influence in a collectivist Filipino context.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Tangentially related through the focus on surplus money, but not a primary focus.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Describes the current status of financial inclusion and banking penetration in the Philippines.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies supply-side barriers (cost, access) and the gap in understanding demand-side psychological factors.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Uses TPB to segment and predict behavioral intentions based on psychological variables.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: low
      justification: Provides baseline demographic and behavioral data relevant to profiling, but not directly about cold-start dynamics.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses logistic regression to classify individuals based on their intention to use banking services.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: Provides background on saving behavior, a prerequisite for budgeting, but does not discuss specific strategies.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Offers insight into determinants of saving, which could inform budget recommendation systems.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: low
      justification: The logistic model serves as an evaluation framework for understanding banking behavior.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: low
      justification: The logistic regression can be considered a module for behavioral prediction.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: Directly studies the intention to save surplus money, the core input for savings goal management.
    - code: 13.C
      name: End-of-Period Surplus as a Savings Input
      relevance: medium
      justification: The dependent variable is precisely the intention to allocate end-of-period surplus to a bank.
  contribution: "The paper provides empirical evidence linking the Theory of Planned Behavior to banking intentions, which justifies Odin's use of behavioral factors in its profiling module. Findings on the predictive power of subjective norms and perceived behavioral control over general attitudes will directly inform Odin's survey design and initial user segmentation. The study's focus on surplus money as a primary savings input validates Odin's core assumption that identifying surplus is the first step in budget recommendation. The methodology using nationwide survey data offers a baseline for evaluating Odin's own recommendation algorithms against real-world behavioral patterns."
  directly_justifies:
    - "Subjective norms, proxied by the presence of a banked family member, are a strong predictor of banking intention."
    - "Perceived behavioral control over earning and saving significantly influences the intention to save surplus money."
    - "Higher educational attainment, being male, and younger age are associated with increased banking intention."
    - "Middle-income individuals have higher banking intentions than low or high-income groups."
  limits:
    - "The study uses intention as the dependent variable, not actual banking behavior, which limits the direct prediction of user actions."
    - "Data is from 2014, which may not reflect current post-pandemic digital banking adoption trends."
    - "The cross-sectional design cannot establish causality between psychological factors and banking intentions."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to the 'Behavioral Profiling & Classification' (5.A) and 'Filipino Cultural Context' (2.A) domains because it applies the Theory of Planned Behavior to a Filipino sample, providing a validated behavioral model. It also offers medium relevance to 'Expense Categorization' (3.A) and 'Savings & Debt Management' (13.A) through its focus on surplus money as the financial input for banking. The topics 6.A (Forecasting) and 8.A (Anomaly Detection) were considered but rejected as the paper does not involve predictive modeling or anomaly detection. Topic 4.A (Existing Systems) was selected for its detailed description of the Philippine financial landscape. Topic 9.A (Mobile-First Design) was rejected, as mobile design is not discussed. The overall relevance is high for informing Odin's behavioral profiling, user segmentation, and the initial design of the budgeting module based on actual Filipino behavioral predictors."
limitations:
  - "The study relies on self-reported behavioral intentions rather than observed financial behaviors, limiting the predictive validity for actual actions."
  - "Data are from 2014 and may not capture changes in financial behavior or attitudes due to post-pandemic digital financial services."
  - "The logistic model has a low Pseudo R2 (0.0094), indicating that many other unmeasured factors influence banking intentions."
  - "The study does not account for the potential mediating role of financial literacy or trust in the relationship between attitudes and intentions. [unacknowledged]"
  - "The treatment of perceived behavioral control uses only two items, which may not fully capture the construct's multi-dimensional nature. [unacknowledged]"
remember_this:
  - "Family influence is a 10.16% stronger predictor of banking intention than general attitudes."
  - "Perceived control over earning and saving is more important than positive attitudes towards banking."
  - "College graduates are 7.95 percentage points more likely to intend to use formal banking."
  - "Unbanked middle-income Filipinos have higher banking intentions than low or high-income groups."
  - "Attitude-intention inconsistency suggests behavioral control and social norms mediate the link."
```