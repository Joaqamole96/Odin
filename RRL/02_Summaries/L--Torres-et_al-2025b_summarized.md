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
  - 2.A
  - 2.D
  - 5.A
  - 5.B
  - 7.A
  - 7.B
  - 13.A
  - 13.B
  - 9.A
  - 9.B
tldr: Compares platform-based gig workers and traditional employees in the Philippines on financial literacy, debt-to-income ratio, social support, and job satisfaction, finding significant differences only in DTI.
problem_and_motivation: The rapid rise of the gig economy in the Philippines, particularly post-pandemic, has created new income opportunities but also exposed workers to income instability and lack of benefits. There is a need to understand the financial and social well-being of platform-based gig workers compared to traditional employees to inform policies and support systems.
approach:
  - Quantitative comparative study using purposive sampling across five provinces in the Philippines.
  - Surveyed 276 gig workers and 307 traditional employees using a self-administered Google Forms questionnaire.
  - Assessed financial literacy via multiple-choice, DTI via ratio calculation, social support and job satisfaction via Likert scales.
  - Used Mann-Whitney U test for group comparisons due to non-normal data distribution.
  - Framed within Dual Labor Market Theory to analyze structural labor market divides.
findings:
  - No statistically significant differences were found between gig workers and traditional employees in financial literacy, social support networks, or job satisfaction.
  - A significant difference was identified in debt-to-income ratios, with traditional employees exhibiting a higher median DTI (40) compared to gig workers (31.41).
  - Qualitative insights suggest gig workers value autonomy and flexibility, contributing uniquely to their job satisfaction despite financial uncertainty.
  - Traditional workers may have a marginal advantage in social support from structured workplace relationships.
  - Both groups showed similar moderate levels of financial literacy (median score of 9).
key_figures_tables:
  - Table 1: Differences in financial status → Shows significant DTI difference (p<.001), no other significant differences.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: DTI
    definition: Debt-to-income ratio, comparing monthly debt payments to gross monthly income.
  - term: Gig Economy
    definition: A labor market characterized by short-term, flexible, and often platform-mediated work arrangements.
critical_citations:
  - "[Kaiser et al., 2022] — Financial education improves knowledge and behaviors."
  - "[Luthi, 2024] — Traditional employees have lower DTI due to stable salaries."
  - "[Sopan, 2023] — Gig workers face challenges in budgeting and planning."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Directly studies Filipino gig workers and traditional employees.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Compares DTI and financial literacy between employment types in the Philippines.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Analyzes financial behaviors like debt management and savings.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Discusses reliance on informal social support networks (family, peer lending) common in Filipino culture.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: Mentions gig workers' income volatility but does not explicitly analyze seasonal spending.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Compares financial behaviors (literacy, DTI) suggesting distinct profiles for gig vs. traditional workers.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: low
      justification: Does not address cold-start, but provides baseline behavioral data.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Mentions budgeting and financial planning skills as critical for gig workers.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: contextual
      justification: Recommends platform-driven financial tools like dynamic earnings forecasts but does not evaluate recommendation systems.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Recommends automated savings features for gig workers.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: Directly compares debt-to-income ratios, a key metric for debt management.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: contextual
      justification: The paper references platform-based work but does not discuss mobile UX design.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: Mentions platform-driven financial tools but not UI/UX specifics.
  contribution: This paper provides empirical evidence on the financial status of Filipino gig workers, which can inform Odin's user profiling and financial behavior modules. The finding that gig workers maintain lower DTI ratios despite income volatility can be used to design more nuanced budgeting and debt management features. The study's recommendations for platform-driven financial tools directly support Odin's budgeting and savings goal management functionalities. The comparison of financial literacy levels across groups highlights the need for integrated financial education within the app. Furthermore, the paper underscores the importance of social support networks, which can be considered in designing community or social features for user retention and engagement.
  directly_justifies:
    - Odin's budgeting features should account for income volatility, especially for gig workers.
    - Debt management modules can be calibrated using the observed differences in DTI ratios between employment types.
    - Financial literacy levels are comparable across groups, justifying a standardized educational approach within the app.
    - Social support mechanisms are important for financial resilience, informing potential community features.
  limits:
    - The study uses purposive sampling in only five provinces, which may not be nationally representative.
    - The sample includes various types of gig workers (e.g., ride-hailing, freelancers), whose financial experiences may differ.
    - The study is cross-sectional, not capturing longitudinal dynamics of financial status.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated 34 canonical topic codes was performed. The paper was flagged as highly relevant to the domains of Filipino Cultural Context (specifically financial behavior and practices of Filipino workers), Behavioral Profiling & Classification (through its comparison of financial literacy and DTI), and Savings & Debt Management (due to its core focus on DTI and financial literacy). Selected topic codes include 1.A, 1.B, 1.C (Filipino Young Professionals demographic and financial structure/behavior) as high relevance because the study directly examines Filipino workers' financial status. Codes 2.A (Culturally Specific Financial Practices) and 2.D (Spending Cycles) were assigned medium and contextual relevance, respectively, as the paper discusses social support networks common in Filipino culture but does not explicitly analyze spending cycles. Codes 5.A (Behavioral Profiles) and 13.B (Debt Management) were assigned high relevance because the study compares DTI and financial literacy between two distinct worker groups. Codes 7.A (Budgeting Strategies) and 13.A (Savings Goal Management) were assigned medium relevance due to the paper's recommendations for financial tools. Codes related to Mobile-First Design, Anomaly Detection, and System Evaluation were considered but rejected as the paper does not address these topics. The overall relevance is high for informing Odin's user profiling, debt management, and budgeting modules with empirically grounded data on Filipino workers.
limitations:
  - The generalizability of findings may be limited due to the non-probability purposive sampling method. [unacknowledged]
  - The reliance on self-reported data for DTI and financial literacy may introduce response bias. [unacknowledged]
  - The study does not explore the long-term financial stability or career progression of gig workers.
  - The paper does not address the algorithmic aspects of financial management tools.
  - The qualitative insights are limited and not systematically analyzed.
remember_this:
  - Traditional employees had a significantly higher median DTI (40) than gig workers (31.41).
  - Financial literacy levels were similar across both gig workers and traditional employees.
  - Job satisfaction did not differ significantly, but gig workers valued autonomy and flexibility.
  - Social support networks were comparable, though traditional workers had a marginal advantage.
  - The study recommends platform-driven financial tools like dynamic earnings forecasts for gig workers.
```