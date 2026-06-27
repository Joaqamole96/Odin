```yaml
paper_id: 10.1051/bioconf/20249305010
designation: local
title: Decoding the eco-financial mindset: financial literacy, attitudes, and efficacy measures and the spending behavior of Filipino millennials
authors: Lim, C. T.; Cordova, W.
year: 2024
venue: BIO Web of Conferences
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 5.A
  - 11.A
tldr: Filipino millennials' spending behavior shows a significant negative correlation with financial attitude, while financial literacy, attitude, and efficacy are strongly interrelated.
problem_and_motivation: Filipino millennials face financial vulnerability due to economic uncertainties, high education costs, and a perceived lack of financial acumen, yet their significant workforce presence makes their financial behavior crucial. Existing research often studies financial literacy, attitude, and efficacy in isolation, leaving a gap in understanding their combined effect on spending behavior.
approach:
  - Surveyed 431 millennials in Laguna, Philippines, via Google Forms.
  - Measured financial literacy, attitude, efficacy, and spending behavior using a custom questionnaire with Likert scales.
  - Employed Confirmatory Factor Analysis (CFA) to validate the measurement model for each latent variable.
  - Used Structural Equation Modeling (SEM) in Jamovi to test hypothesized relationships among the latent variables.
  - Evaluated model fit using RMSEA, TLI, CFI, and SRMR, and checked for multicollinearity using VIF.
findings:
  - num: Strong positive correlations were found between financial efficacy and literacy (β = 0.61, p < .001), and between financial attitude and literacy (β = 0.58, p < .001).
  - num: A significant negative correlation was identified between spending behavior and financial attitude (β = -0.18, p = 0.034).
  - num: 42% of respondents reported spending 41% or more of their income, indicating high variability in total spending.
  - num: 93.7% of respondents allocated 10% or less of their income to beer and wine, showing high consistency in this spending category.
  - The study did not find a statistically significant relationship between spending behavior and financial literacy or financial efficacy.
  - Millennials with a more positive financial attitude tend to exhibit more responsible spending behaviors.
  - Financial literacy, attitude, and efficacy are interdependent, suggesting a comprehensive strategy for financial well-being.
key_figures_tables:
  - Table 1: Socio-demographic characteristics of respondents → Shows sample is predominantly male, aged 26-27, earning PHP 20,000-26,999.
  - Table 2: List of latent variables and constructs → Details the observed variables for each financial construct, all with acceptable Cronbach's alpha.
  - Table 3: Spending construct observed variables frequency → Highlights variability in overall spending and consistency in alcohol spending.
  - Table 4: CFA fit indices for latent variables → Indicates a reasonable to good fit for the measurement models.
  - Table 5: Parameter estimates of structural paths → Quantifies the strength and direction of relationships among constructs.
  - Figure 1: Path diagram of the proposed SEM framework → Visually depicts the relationships among financial literacy, attitude, efficacy, and spending.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: CFA
    definition: Confirmatory Factor Analysis
  - term: SEM
    definition: Structural Equation Modeling
  - term: TPB
    definition: Theory of Planned Behavior
  - term: RMSEA
    definition: Root Mean Square Error of Approximation
  - term: TLI
    definition: Tucker-Lewis Coefficient
  - term: CFI
    definition: Comparative Fit Index
  - term: SRMR
    definition: Standardized Root Mean Square Residual
  - term: VIF
    definition: Variance Inflation Factor
critical_citations:
  - "[Ajzen, 1991] — Foundational theory for the study's framework."
  - "[Yanto et al., 2021] — Links social media to financial literacy development."
  - "[Sotiropoulos & d'Astous, 2013] — Supports link between financial attitude and spending."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Directly studies Filipino millennials, a core demographic for Odin.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Provides data on income levels, employment, and primary financial goals of the target demographic.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Core focus of the paper is on spending behavior, a key financial behavior.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Investigates financial attitudes and behaviors within the Filipino cultural context.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Discusses general spending variability but does not explicitly analyze seasonal patterns.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Provides a breakdown of spending categories but does not specifically address spending cycles or occasions.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: The findings on the interplay of literacy, attitude, and efficacy can inform the development of behavioral profiles.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Recommendations for using social media and peer influence for financial education are relevant for user engagement.
  contribution: |
    This paper provides direct empirical evidence that financial attitude is a more significant predictor of spending behavior than financial literacy for Filipino millennials. This finding is directly relevant to Odin's user profiling module, suggesting that attitudinal metrics should be weighted heavily. The study's recommendation for tailored financial education programs that leverage social media can inform Odin's user retention and engagement strategies. The identified spending variability and consistency across categories can guide the design of Odin's expense categorization and anomaly detection features.
  directly_justifies:
    - "A positive financial attitude is significantly correlated with responsible spending behavior in Filipino millennials."
    - "Financial literacy, attitude, and efficacy are strongly interrelated and should be considered together."
    - "Tailored financial education programs that leverage social media can improve financial literacy and engagement."
  limits:
    - "Self-reported data may be subject to recall and social desirability bias."
    - "The sample is skewed towards respondents with jobs requiring financial skills."
    - "The cross-sectional design limits the ability to track changes in financial behavior over time."
    - "The study is geographically limited to Laguna, Philippines."
  mapping_rationale: |
    A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as high relevance for 'Filipino Cultural Context' (2.A) as it directly studies a Filipino demographic, and for 'Behavioral Profiling & Classification' (5.A) due to its analysis of financial attitudes and behaviors. It was also deemed high relevance for 'User Retention & Engagement' (11.A) because its recommendations for social media-based education can inform engagement strategies. The topics 1.A and 1.C were assigned high relevance as the paper directly addresses the demographic and its financial behavior. Topic 1.B was medium due to providing supporting demographic data. Topic 2.B was considered contextual as seasonal spending is not examined. Topic 2.D was low because while spending categories are broken down, the paper does not analyze spending cycles or occasions. Other domains like 'Spending Forecasting', 'Budget Recommendation', 'Anomaly Detection', and 'Data Privacy' were rejected as they are not addressed by the paper. The paper's overall relevance to Odin is medium, primarily informing the user profiling and engagement modules.
limitations:
  - "Self-reported data may be prone to recall and social desirability bias. [unacknowledged]"
  - "The sample is skewed towards respondents with jobs requiring financial skills, limiting generalizability."
  - "The cross-sectional design limits the ability to track changes in financial behavior over time. [unacknowledged]"
  - "The study is geographically limited to Laguna, Philippines. [unacknowledged]"
remember_this:
  - "Financial attitude, not literacy, is the strongest predictor of spending behavior."
  - "Millennials show high consistency in spending on alcohol, with 93.7% spending 10% or less."
  - "Financial literacy, attitude, and efficacy are strongly interdependent."
  - "Tailored programs using social media can improve financial literacy and engagement."
  - "42% of respondents spent 41% or more of their income, indicating high spending variability."
```