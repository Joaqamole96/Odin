```yaml
paper_id: 10.1145/3785171.3785197
designation: local
title: The Shift to Gig Economy: How Traditional Employment Stacks Up Against Platform-Based Independent Workers
authors: Torres, R. C.; Bartolome, Z. M. I.; Jimena, L. G.; Paner, J. P.
year: 2025
venue: The 9th International Conference on Business and Information Management (ICBIM 2025)
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 3.A
  - 4.A
  - 4.B
  - 5.A
  - 13.A
  - 13.B
tldr: Platform-based gig workers and traditional employees in the Philippines show comparable financial literacy and social support, but traditional workers have significantly higher debt-to-income ratios.
problem_and_motivation: The rapid rise of the gig economy in the Philippines has created new income opportunities but also exposed workers to income instability and limited financial services. There is a lack of comparative research on the financial health and well-being of platform-based gig workers versus traditional employees. This gap hinders the development of targeted policies and financial tools to support diverse employment models.
approach:
  - A quantitative comparative analysis was conducted using purposive sampling across five Philippine provinces.
  - Participants included platform-based gig workers (e.g., ride-hailing, freelancing) and full-time traditional employees with formal contracts.
  - A self-administered Google Forms survey gathered data on demographics, financial literacy, debt-to-income ratio, social support, and job satisfaction.
  - The Mann-Whitney U test was employed as a non-parametric alternative after data failed normality checks via the Shapiro-Wilk test.
  - The study used established instruments, including a multiple-choice financial literacy quiz and the Job Satisfaction Survey (JSS).
findings:
  - Financial literacy levels were statistically similar between gig workers and traditional employees (p=0.267).
  - Traditional employees had a significantly higher median debt-to-income ratio (40) than gig workers (31.41), p < .001.
  - Social support networks were comparable across both groups, with no significant difference (p=0.135).
  - Job satisfaction scores did not differ significantly (p=0.797), though qualitative insights suggest gig workers value autonomy.
  - Traditional employees' higher DTI may be linked to greater access to credit and long-term financial commitments.
  - Gig workers demonstrated more cautious debt management, possibly due to income variability and limited credit access.
key_figures_tables:
  - Table 1: Differences in Financial Status → Traditional workers have higher DTI, other metrics are statistically similar.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Debt-to-Income (DTI) Ratio
    definition: A metric comparing an individual's monthly debt payments to their gross monthly income.
  - term: Gig Economy
    definition: A labor market characterized by short-term, flexible, and often platform-mediated work arrangements.
  - term: Platform-based gig workers
    definition: Independent workers engaged in technology-mediated work like ride-hailing or freelance digital services.
  - term: Dual Labor Market Theory
    definition: A theory positing a structural divide between a primary market with stable jobs and a secondary market with volatile, insecure work.
  - term: None.
    definition: ""
critical_citations:
  - "[Luthi, 2024] — Defines DTI ratio and its importance for credit access."
  - "[Sopan, 2023] — Discusses financial stability challenges for gig workers."
  - "[DeWaal, 2024] — Links financial literacy to better financial behaviors."
  - "[Kaiser et al., 2022] — Shows financial education improves financial knowledge."
  - "[Yumang, 2024] — Documents gig workers' reliance on predatory lending in the Philippines."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: Study focuses on Filipino workers, a key demographic for Odin.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Directly compares DTI and financial literacy of two worker groups in the Philippines.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Analyzes financial behaviors like debt management and savings in the Philippine context.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: Provides background on financial health metrics like DTI relevant to expense management.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Mentions the lack of financial tools and education for gig workers, a gap Odin could fill.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Highlights the absence of platform-driven financial education and support for gig workers.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: low
      justification: Suggests different debt management behaviors between employment types.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: Discusses financial resilience and need for savings features for gig workers.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: Provides empirical data on DTI ratios, crucial for informing debt management features in Odin.
  contribution: This paper provides empirical evidence on the financial health of Filipino gig workers, which is directly relevant to Odin's debt management and behavioral profiling modules. The finding that gig workers have lower DTI ratios than traditional employees challenges assumptions and can inform Odin's user modeling for income forecasting. The study's comparison of financial literacy and job satisfaction can guide the design of engagement and financial education features within Odin. Its identification of social support as a critical factor for worker well-being suggests integrating social or community features into Odin's design.
  directly_justifies:
    - "Traditional employees have significantly higher debt-to-income ratios than platform-based gig workers in the Philippines."
    - "Financial literacy levels do not differ significantly between gig workers and traditional employees."
    - "Gig workers value autonomy and flexibility as key contributors to job satisfaction."
  limits:
    - "Purposive sampling may limit generalizability to the broader Filipino workforce."
    - "The study is cross-sectional, so it cannot establish causal relationships between employment type and financial outcomes."
    - "Relies on self-reported data, which may be subject to social desirability bias."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant to the 'Behavioral Profiling & Classification' domain (code 5.A) because it compares financial behaviors across employment types. It was also flagged for 'Savings & Debt Management' (codes 13.A, 13.B) due to its key finding on DTI ratios and its discussion of financial resilience. The 'Filipino Cultural Context' (codes 1.A, 1.B, 1.C) was deemed highly relevant as the study focuses on Filipino workers and their financial structures. Codes under 'Expense Categorization' (3.A) were considered contextual, providing background on financial health. 'Existing Systems & Gaps' (4.A, 4.B) was seen as medium relevance, as it identifies a lack of support systems. Codes related to 'Spending Forecasting' (6.A, 6.B), 'Budget Recommendation' (7.A-D), 'Anomaly Detection' (8.A-C), 'Mobile-First Design' (9.A-B), 'Data Privacy' (10.A-B), 'User Retention' (11.A-B), and 'System Evaluation' (12.A-C) were considered and rejected as the paper does not address these technical or design topics. The paper's overall relevance to Odin is medium, providing crucial behavioral and financial data that can inform user profiling and debt management features, although it lacks direct guidance on algorithmic design.
limitations:
  - "Purposive sampling may limit generalizability to the broader Filipino workforce."
  - "The study is cross-sectional, so it cannot establish causal relationships between employment type and financial outcomes."
  - "Relies on self-reported data, which may be subject to social desirability bias."
  - "The qualitative insights on job satisfaction are not systematically analyzed, limiting their depth." [unacknowledged]
remember_this:
  - "Traditional employees in the Philippines have a median DTI of 40, significantly higher than gig workers at 31.41."
  - "Financial literacy is comparable between gig and traditional workers, both scoring a median of 9."
  - "Job satisfaction does not differ statistically, but gig workers derive satisfaction from autonomy."
  - "Gig workers demonstrate more cautious debt management despite income volatility."
  - "Social support networks are similar across both employment types."
```