```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: local
title: ASSESSING THE FINANCIAL LITERACY OF SENIOR HIGH SCHOOL AND COLLEGE STUDENTS: A COMPREHENSIVE ANALYSIS
authors: Dela Rama, K.; Baylon, F.; Balwet, L.; Pullos, K.; Durias, R.; Cabusca, J.; Eguia, A.; Cabilin, L.; Duran, R.; Mante, J.; Prepecio, D.; Gilongos, C.; Rosel, M.
year: 2024
venue: The Threshold
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.D
  - 3.A
  - 13.A
tldr: Senior high and college students demonstrate basic financial knowledge but significant practical gaps in budgeting, compound interest, and investment strategies.
problem_and_motivation: Young Filipinos face complex financial decisions but often lack formal education, leading to poor money management. This gap is critical as students transition to independent financial responsibilities.
approach:
  - Quantitative survey of 345 randomly selected SHS and college students at CSFJ using a 4-point Likert scale.
  - Adapted OECD/INFE questionnaire covering financial knowledge and behavior in savings, budgeting, and borrowing.
  - Stratified random sampling by year level and program to ensure representative data.
  - Data analyzed via descriptive statistics, Welch's t-test for group comparisons, and Pearson correlation.
  - Used Python with Pandas and SciPy for statistical computation and visualization.
findings:
  - Students possess a basic understanding of financial concepts (mean score 2.10 for SHS, 2.11 for College).
  - num: Less than 30% of respondents could accurately explain compound interest, indicating a major knowledge gap.
  - Moderate financial behavior (mean score 1.92 for SHS, 1.85 for College), with less consistent budgeting practices.
  - No significant gender differences in financial literacy were found within the sample.
  - Many students rely on family as their primary source of financial knowledge rather than formal education.
key_figures_tables:
  - "Table 1: Mean financial knowledge scores (SHS=2.10, College=2.11) → Students have comparable basic knowledge levels."
  - "Table 2: Mean financial behavior scores (SHS=1.92, College=1.85) → Behavior lags behind knowledge for both groups."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Financial Literacy
    definition: Ability to understand and effectively use financial skills including management, budgeting, and investing.
  - term: OECD/INFE
    definition: Organisation for Economic Co-operation and Development / International Network on Financial Education.
  - term: APY
    definition: Annual Percentage Yield, the real rate of return earned on savings.
critical_citations:
  - "[Lusardi & Mitchell, 2014] — foundational work on financial literacy importance."
  - "[OECD, 2016] — provides key definitions and frameworks for financial education."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Directly profiles the financial literacy of Filipino students, the target user base.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Details the financial knowledge and behaviors of the target demographic.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Provides baseline data on saving, budgeting, and borrowing habits.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Mentions family influence and financial practices within the Philippine context.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: Background on Philippine economic challenges and financial literacy gaps.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: Discusses budgeting but does not propose or evaluate specific categorization frameworks.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Highlights savings behavior and goals, relevant for savings feature design.
  contribution: This paper provides foundational data on the financial knowledge gaps and behavioral tendencies of Filipino students, which directly informs the user persona modeling for Odin's onboarding and profile creation. The identified lack of practical budgeting skills justifies the need for Odin's core expense tracking and budget recommendation features. Furthermore, the paper's emphasis on savings goals supports the design of Odin's savings and debt management modules. The absence of significant gender differences simplifies the design of personalized financial profiles.
  directly_justifies:
    - "The target demographic (Filipino young adults) exhibits significant gaps in practical financial application."
    - "Financial literacy initiatives should focus on both knowledge and behavior for effectiveness."
    - "Family is a primary source of financial education, suggesting community-based design considerations."
  limits:
    - "The study is limited to a single institution (CSFJ) in Mindanao, reducing generalizability across the Philippines."
    - "The sample includes only students, not young professionals already in the workforce."
    - "The study does not evaluate the impact of digital financial tools or PFMS on financial literacy."
  mapping_rationale: All 12 functional domains and their associated topic codes were systematically scanned. The paper was flagged as highly relevant to the Filipino Cultural Context (1.A, 1.B) because it provides empirical data on the financial profile and behaviors of the target demographic. It has medium relevance to Expense Categorization (3.A) and Savings Goal Management (13.A) because it discusses budgeting and savings practices that inform feature design. It is contextual for topics like Culturally Specific Financial Practices (2.A) as it mentions family influence but doesn't delve deeply into specific cultural norms. Other domains, such as Existing Systems & Gaps (4.A), Behavioral Profiling (5.A), Forecasting (6.A), and Evaluation (12.A), were considered and rejected because the paper does not address system design, algorithms, or evaluation methodologies. Overall, the paper serves as a crucial reference for understanding the user's baseline financial capability, which is essential for Odin's user-centric design.
limitations:
  - "[unacknowledged] Focus on a single institution limits external validity."
  - "The study relies on self-reported data, which may introduce social desirability bias."
  - "It does not assess the influence of digital tools on financial literacy."
  - "[unacknowledged] The use of AI for editing was disclosed, but not the specific prompts or extent of modification."
remember_this:
  - Students understand basic finance but fail to apply it to compound interest and budgeting.
  - Less than 30% of students can accurately explain compound interest.
  - Financial behavior scores are lower than knowledge scores for both student groups.
  - No gender differences in financial literacy were found in the study sample.
  - Practical skill development is needed beyond theoretical financial education.
```