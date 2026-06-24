```yaml
paper_id: 10.5281/zenodo.18438866
designation: local
title: Financial Literacy of Public Secondary School Teachers in San Francisco District, Camotes Island, Cebu, Philippines
authors: Montuerto, J. E.; Ferrater-Gimena, J. A. O.
year: 2026
venue: Unknown
odin_topics:
  - 1.C
  - 2.A
  - 4.B
  - 5.A
  - 7.A
  - 13.A
  - 13.B
tldr: Public secondary school teachers in Camotes, Cebu show moderate financial literacy in budgeting and spending but lower in savings and investing, with debt cycles and demographic influences, prompting a primer.
problem_and_motivation: Public school teachers in the Philippines face serious financial struggles, often resorting to borrowing to cover budget deficits, yet there is limited understanding of their specific financial literacy levels. The debt problem is escalating, and teachers lack adequate financial management knowledge. A targeted primer is needed to guide teachers in better managing their income and breaking the debt cycle.
approach:
  - Used a descriptive-correlational design with 150 randomly selected teachers from three national high schools in San Francisco District, Camotes, Cebu.
  - Administered a researcher-made survey with two parts: demographic profile and financial literacy items on budgeting, savings, investing, spending, and credit/debt management.
  - The survey had good reliability (Cronbach's alpha = 0.885) after a pilot test with 20 respondents.
  - Data analyzed using frequency, percentage, weighted mean, Chi‑square test of independence, and independent t‑test.
  - Ethical principles of beneficence, non‑maleficence, justice, and autonomy were followed.
findings:
  - "num: 42% of respondents were aged 24‑32 years, 78.67% were female, and 74% had no other income sources."
  - "num: Aggregate mean for budgeting was 2.96 (moderate), savings 2.42 (less), investing 1.98 (less), spending 3.17 (moderate), and credit/debt 3.05 (moderate)."
  - "num: Age showed significant relationships with budgeting, savings, investing, and debt management (p ≤ 0.005)."
  - "num: Gender and other sources of income were significantly related to investing (p ≤ 0.010)."
  - "num: Highest educational attainment was significantly related to debt management (p = 0.001)."
  - Teachers prioritize family needs over wants and avoid unnecessary expenses.
  - Borrowing is typically reserved for emergencies, but many still experience deficit budgeting.
  - There is no significant difference in overall financial literacy across most demographic groups except age and educational attainment for certain aspects.
key_figures_tables:
  - "Table 2: Respondent profile (age, gender, civil status, etc.) → Majority are young, female, married, with no extra income."
  - "Table 3‑7: Extent of financial literacy in each domain → Budgeting and spending are moderate; savings and investing are low."
  - "Table 9‑13: Chi‑square tests for relationships → Age and education are significant predictors for several domains."
  - "Table 14‑18: ANOVA/t‑test for differences → Age, gender, length of service, steps, and other income affect investing; age and education affect debt management."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Financial literacy
    definition: Knowledge about financial, credit, and debt management necessary for making informed, responsible financial decisions.
  - term: Deficit budgeting
    definition: Spending money not yet earned, often leading to a cycle of borrowing to cover shortfalls.
critical_citations:
  - "[Lusardi & Mitchell, 2011] — Establishes importance of financial literacy globally."
  - "[Casingal & Ancho, 2022] — Benchmarks financial literacy of Philippine public teachers."
  - "[Tilan & Cabal, 2020] — Links teachers' low net pay to borrowing behaviors."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: contextual
      justification: Teachers are professionals; their behavior may inform similar cohorts.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Describes borrowing and family‑first spending practices common among Filipino teachers.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Highlights the lack of financial literacy and pervasive debt, indicating system gaps.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Profiles teachers by demographics and literacy levels, aiding behavioral segmentation.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Provides empirical data on teachers' budgeting practices and deficits.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: Directly measures savings behavior and finds low literacy, informing savings features.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: Assesses credit and debt management, revealing moderate literacy and debt cycles.
  contribution: This paper empirically documents the financial literacy gaps of Filipino public teachers across budgeting, savings, investing, spending, and debt management. It provides baseline data on demographic correlates that can inform Odin's user profiling and personalization modules. The identified deficit budgeting and debt cycles justify the need for Odin's budget recommendation and debt management features. The proposed primer framework can be adapted for in‑app educational content. The study's findings on spending priorities (family over wants) guide Odin's expense categorization and constraint settings.
  directly_justifies:
    - "Teachers show lower savings literacy (mean 2.42), supporting the need for Odin's savings goal tools."
    - "Credit/debt management is moderate (mean 3.05), but cycles of deficit budgeting are common."
    - "Age and education significantly affect financial behaviors, informing Odin's adaptive profiling."
    - "Most teachers (74%) have no additional income, highlighting the importance of managing single income streams."
  limits:
    - "Sample limited to three schools in one district, reducing generalizability."
    - "Self‑reported survey may suffer from social desirability bias."
    - "Cross‑sectional design prevents causal inference."
    - "Does not examine actual financial outcomes (e.g., loan defaults, savings balances)."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. Relevant domains flagged were Filipino Cultural Context (2.A), Existing Systems & Gaps (4.B), Behavioral Profiling (5.A), Budget Recommendation (7.A), and Savings & Debt Management (13.A, 13.B). The paper directly measures financial behaviors, making 13.A and 13.B high relevance; it provides supporting evidence for profiling and budgeting strategies (medium), and contextual background for cultural practices. Domains such as Forecasting, Anomaly Detection, Mobile Design, Privacy, Retention, and Evaluation were rejected because the paper does not address predictive models, outliers, UX, privacy, user engagement, or system evaluation. Borderline cases: 2.B (cyclical spending) was considered but only mentioned as a debt cycle without seasonal patterns, so not selected. Overall, the paper is moderately relevant to Odin, offering empirical grounding for savings/debt modules and user behavioral insights.
limitations:
  - "Sample limited to one district on Camotes Island, Philippines. [unacknowledged]"
  - "Self‑reported data may inflate literacy perceptions. [acknowledged in discussion?]"
  - "Cross‑sectional design cannot establish causality."
  - "Does not evaluate the actual effectiveness of the proposed primer."
remember_this:
  - "Teachers have moderate budgeting and spending literacy but low savings and investing literacy."
  - "Age is the strongest demographic predictor of financial literacy across multiple domains."
  - "74% of teachers have no income beyond their salary, emphasizing single‑income constraints."
  - "Debt cycles are common, with teachers using current income to pay past debts."
  - "Highest educational attainment significantly influences debt management skills."
```