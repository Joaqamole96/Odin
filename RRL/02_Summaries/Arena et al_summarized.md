```yaml
paper_id: 34ac84a5-02c7-5c65-9ff2-3c89a8a4923b
designation: local
title: Influences on the Stock Market Investing of Tertiary Students in the National Capital Region, Philippines
authors: Arena, C. M. R.; Batac, A. A. S.; Religioso, A. M. A.; Magbata, E. V. S.; Mandigma, M. B. S.
year: 2023
venue: Review of Integrative Business and Economics Research
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.C
  - 3.A
  - 5.A
  - 5.C
tldr: A survey of 387 Filipino tertiary students reveals that financial knowledge significantly predicts stock market investing, while money and risk attitudes do not, explaining only 8.8% of participation variance.
problem_and_motivation: Stock market participation in the Philippines remains low, and the factors driving investment decisions among young Filipinos are poorly understood. While attitudes and knowledge are theorized to influence investment, empirical evidence on their specific roles in this demographic is sparse.
approach:
  - A quantitative, descriptive-correlational design was used with 387 tertiary students in Metro Manila, Philippines, sampled via purposive sampling.
  - Data were collected through an online survey using established scales for money attitude (Klontz), risk attitude (Zhang), financial knowledge (Perry & Morris), and stock market investing (Luotonen).
  - Cronbach's alpha for the survey instrument was 0.889, indicating good internal consistency.
  - Pearson Correlation and Stepwise Regression analyses were performed to test relationships and predictive power of the independent variables on stock market investing.
  - Control variables, including the number of stocks owned and total annual investment, were added to the regression models to test the robustness of the findings.
findings:
  - num: Financial knowledge (r=0.297) shows a mild but significant positive correlation with stock market investing at p<0.01.
  - num: Money attitude (r=0.116) and risk attitude (r=0.148) have significant but very weak positive correlations with stock market investing.
  - num: Stepwise regression shows financial knowledge is the only significant predictor, explaining 8.8% (R²=0.088) of the variance in stock market investing.
  - Financial knowledge remains a significant predictor of stock market participation even when total annual stock market investment is included as a control variable (p=0.047).
  - The effect of financial knowledge on stock market investing is negated when the number of stocks owned by investors is added as a control variable (p=0.535).
  - Most respondents (43.67%) own less than 2 types of stocks and invest less than P25,000 annually (48.84%).
key_figures_tables:
  - Table 2: Stock market participation profile of respondents → Shows majority have low investment levels and holdings.
  - Table 3: Pearson correlation coefficients among variables → Significant but mild correlations (r<0.3) between all predictors and stock investing.
  - Table 4: Model summary of predictors → Financial knowledge yields the highest R² of 0.088 for predicting stock market investing.
  - Table 6: Stepwise regression analysis → The model formula: Stock Market Investing = 0.345 + 0.12 * Financial Knowledge.
key_equations:
  - equation: SMI = 0.345 + 0.12 * FK
    explanation: Model shows a 1-unit increase in FK raises SMI by 0.12.
definitions:
  - term: TPB
    definition: Theory of Planned Behavior by Ajzen (1991) explaining behavior via attitudes, subjective norms, and perceived control.
  - term: Risk Attitude
    definition: An individual's chosen response to uncertainty, influencing their financial decisions.
  - term: Financial Literacy
    definition: The ability to understand and use financial information for effective decision-making.
critical_citations:
  - "[Nadeem et al., 2020] — Found money attitudes do not significantly affect stock investing."
  - "[Van Rooij et al., 2011] — Financial literacy strongly predicts stock market participation."
  - "[Ahinful et al., 2021] — Financial literacy, ethics, and risk attitude influence investment willingness."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: The study's sample of tertiary students is a precursor to the young professional demographic.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: low
      justification: Provides limited data on income and investment structure (e.g., annual investment amounts).
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Examines financial behaviors (stock investing) and their psychological antecedents.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: It is a Philippines-based study, providing a culturally specific context for financial behavior.
    - code: 2.C
      name: User-Declared Financial Preferences
      relevance: low
      justification: Measures risk attitude and money attitude, which are forms of declared preferences.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: Focuses on investment, not expense categorization, but provides a framework for studying financial decisions.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly analyzes financial behavior (stock investing) as a function of money attitude, risk attitude, and financial knowledge.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses regression to identify financial knowledge as a key differentiator in investment behavior.
  contribution: The study's finding that financial knowledge is the primary driver of stock market participation can inform Odin's user onboarding and educational content. It suggests that Odin's behavioral profiling module should prioritize assessing financial literacy as a key feature for user classification. The weak influence of money and risk attitudes implies that Odin's design should not over-index on these psychological factors for engagement predictions. The research validates the importance of knowledge-based interventions, which could be integrated into Odin's savings and budgeting modules. This evidence supports Odin's strategy of providing clear, educational content to empower users rather than focusing on changing deep-seated attitudes.
  directly_justifies:
    - Financial literacy is the strongest predictor of investment behavior among young Filipinos.
    - Money attitudes do not have a significant effect on stock market investing decisions.
    - Risk attitudes do not have a significant effect on stock market investing decisions.
  limits:
    - The sample is limited to tertiary students in Metro Manila, which may not represent the broader Filipino young professional population.
  mapping_rationale: A systematic scan of all 12 functional domains identified the paper's relevance primarily to Behavioral Profiling & Classification (Domain 5) and, to a lesser extent, Filipino Cultural Context (Domain 2). The paper's analysis of financial knowledge, money attitudes, and risk attitudes as predictors of stock market participation directly informs 5.A (Financial Behavioral Profiles), meriting a 'high' relevance for that topic, and 5.C (Classification Approaches), with 'medium' relevance. Its local context supports 2.A (Culturally Specific Practices) with a 'medium' relevance due to its Filipino student sample. Topics like 3.A (Expense Categorization), 1.A (Demographic), and 1.C (Behavior) were also considered but received lower or 'contextual' ratings because the paper does not directly address Odin's core PFMS functions like categorization, forecasting, or budget recommendation. Domains related to expense tracking, savings, debt, and mobile design were considered and rejected as the paper's focus on stock market investment is tangential. Overall, the paper's contribution is highly specific to behavioral profiling, supporting Odin's efforts to understand user financial behavior, but offers little for its algorithmic or system design modules.
limitations:
  - The study uses a convenience sample that is overrepresented by students from one university (66.67% from UST). [unacknowledged]
  - The research design is cross-sectional and cannot establish causality between financial knowledge and stock investing. [unacknowledged]
  - The paper does not discuss potential demographic confounders like family income or field of study. [unacknowledged]
  - The sample is limited to the National Capital Region, limiting generalizability to other parts of the Philippines. [acknowledged]
remember_this:
  - Financial knowledge is the only significant predictor of stock market participation among Filipino students.
  - The effect size of financial knowledge on investment behavior is small, explaining only 8.8% of variance.
  - Money attitudes and risk attitudes do not significantly affect stock investment decisions.
  - Most student investors have low portfolios, with 48.84% investing less than P25,000 annually.
```