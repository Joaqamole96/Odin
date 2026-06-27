```yaml
paper_id: 10.1057/s41264-023-00234-8
designation: international
title: Impact of financial behaviour on financial well-being: evidence among young adults in Malaysia
authors: Sabri, M. F.; Anthony, M.; Law, S. H.; Rahim, H. A.; Burhan, N. A. S.; Ithnin, M.
year: 2023
venue: Journal of Financial Services Marketing
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 3.B
  - 4.B
  - 5.A
  - 5.C
  - 7.A
  - 10.A
tldr: Financial behaviour mediates the relationships between financial literacy, socialisation, self-control, fintech, and financial well-being among young Malaysian adults during COVID-19.
problem_and_motivation: Young Malaysian adults face declining financial well-being due to COVID-19, including job loss, housing issues, and increased debt. The determinants of financial well-being, especially the mediating role of financial behaviour, remain unclear for this demographic, which constitutes a significant portion of the population.
approach:
  - Multi-stage random sampling collected 360 responses from young adults aged 18-29 across five Malaysian regions.
  - Structural equation modelling (SEM) was used to analyse the relationships between financial literacy, socialisation, self-control, fintech, financial behaviour, and well-being.
  - Financial behaviour was modelled as a mediator between four exogenous factors and financial well-being.
  - Sobel-Goodman mediation tests were used as a robustness check for the mediation effects.
findings:
  - num: Financial behaviour was the most important element influencing financial well-being (β = 0.48, t = 3.10, p < 0.05).
  - Financial behaviour significantly mediated the relationships between financial literacy, financial socialisation, self-control, financial technology, and financial well-being.
  - Financial literacy and self-control did not have a significant direct influence on financial well-being.
  - Financial technology and financial literacy were the factors most highly mediated by financial behaviour.
  - num: The model explained 74% of the variation in financial behaviour and 61% in financial well-being.
key_figures_tables:
  - Table 2: Reliability analysis of scales (Cronbach's alpha) for pilot and actual study → All constructs achieved acceptable reliability (>0.77).
  - Table 3: Average variance extracted (AVE) and composite reliability (CR) for constructs → All constructs met convergent validity and reliability thresholds (AVE > 0.5, CR > 0.6).
  - Table 4: Discriminant validity index summary for all constructs → The square root of AVE exceeded inter-construct correlations, confirming discriminant validity.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Financial well-being
    definition: A young adult's assessment of their quality of life based on their financial situation, including the ability to meet current commitments and have buffers for the future.
  - term: Financial behaviour
    definition: The actions of young adults regarding budgeting, cash flow management, spending plans, credit management, and long-term financial planning.
  - term: Financial technology (FinTech)
    definition: Innovative financial services that use new technologies to allow consumers to conduct financial activities through digital means.
  - term: Financial socialisation
    definition: The process by which young adults learn financial values, norms, and practices from agents like parents and family members.
  - term: Self-control
    definition: The ability to control oneself and overcome immediate needs for better future outcomes, including in financial matters.
critical_citations:
  - "[CFPB, 2015a] — Defines factors influencing financial well-being."
  - "[Deacon & Firebaugh, 1988] — Provides the systems theory underpinning the research model."
  - "[Xiao & Porto, 2017] — Supports the mediating role of financial behaviour."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: Studies young adults in Malaysia, a comparable ASEAN demographic, providing regional context.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Discusses income levels, debt (student loans, credit cards), and household size of young adults.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Core focus is on financial behaviour (budgeting, saving, credit use) and its direct influence on well-being.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Highlights the role of parental financial socialisation and family as key cultural influences on financial behaviour.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: low
      justification: Tangentially relevant as it discusses financial behaviour components like budgeting and spending, but not specific category design.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: contextual
      justification: Provides background on the financial struggles of young adults but does not evaluate existing PFMS.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly examines financial behaviour as a mediator and its classification through SEM, relevant to profiling.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses SEM to classify and validate the relationships between behaviour and its determinants.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Mentions financial behaviour components like having a budget and cash flow management as key to well-being.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Does not address data privacy, but contextual relevance for user trust is minimal.
  contribution: This paper provides empirical evidence that financial behaviour is a critical mediator for financial well-being, which directly supports the development of Odin's behavioral profiling module (5.A). The finding that financial technology only improves well-being when mediated by positive financial behaviour justifies Odin's focus on nudging users towards good behaviour rather than solely providing tools. The study's emphasis on financial socialisation and its impact on behaviour informs the design of culturally relevant onboarding and engagement strategies within Odin.
  directly_justifies:
    - "Financial behaviour is a significant predictor of financial well-being among young adults."
    - "Financial literacy alone does not directly improve financial well-being; it requires positive financial behaviour."
    - "Financial technology must be combined with good financial behaviour to be effective."
    - "Self-control impacts financial well-being through its influence on financial behaviour."
  limits:
    - "Survey sample is restricted to young adults aged 18-29 only."
    - "Study uses a subjective measure of financial well-being."
    - "Sampling method focused on youth organisations, which may not represent all young adults."
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The paper was found directly relevant to the Behavioral Profiling & Classification domain, with high relevance to topic 5.A (Financial Behavioral Profiles) and medium relevance to 5.C (Classification Approaches), as it uses SEM to model and validate financial behaviour's mediating role. It also provides supporting evidence for the Filipino Cultural Context domain, specifically topic 1.A, 1.B, and 1.C, by studying the financial structure and behaviour of Malaysian young adults, a comparable demographic. The paper's findings on the importance of financial literacy, socialisation, and self-control offer contextual insights for Expense Categorization (3.B) and Budget Recommendation (7.A) by highlighting the behaviours that lead to good financial management. Topics related to algorithm-specific areas like forecasting (6.A, 6.B), anomaly detection (8.A), or system evaluation (12.A) were rejected as the paper does not address computational methods. The overall relevance is high for informing Odin's core design around behavioural intervention and user profiling.
limitations:
  - "Sample restricted to ages 18-29, limiting generalisability to broader adult population."
  - "Subjective measure of financial well-being was used."
  - "Multi-stage random sampling may not have captured all socio-economic backgrounds."
  - "Cross-sectional design does not establish causality over time [unacknowledged]."
  - "Relies on self-reported data, which may be subject to social desirability bias [unacknowledged]."
remember_this:
  - "Financial behaviour is the strongest predictor of financial well-being."
  - "Financial literacy and self-control do not directly improve well-being."
  - "Fintech is only beneficial when paired with positive financial behaviour."
  - "Financial behaviour mediates the effect of socialisation and literacy."
  - "The model explains 61% of the variance in financial well-being."
```