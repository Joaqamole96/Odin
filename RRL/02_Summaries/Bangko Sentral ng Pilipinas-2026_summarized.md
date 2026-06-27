```yaml
paper_id: 3f7a8c9d-5e4f-4a2b-8c1d-9e0f1a2b3c4d
designation: local
title: Consumer Expectations Survey Report (Q1 2026)
authors: Bangko Sentral ng Pilipinas
year: 2026
venue: Bangko Sentral ng Pilipinas
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 3.A
  - 3.B
  - 5.A
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 13.A
  - 13.B
  - 13.C
tldr: Consumer confidence improved in Q1 2026 but outlook for the year ahead became less upbeat due to inflation and corruption concerns.
problem_and_motivation: Understanding consumer sentiment and spending expectations is vital for economic policy and financial planning. The Philippines lacks granular, forward-looking data on household financial behavior across income groups and regions. This survey fills that gap by providing quarterly indices on confidence, spending, savings, and debt intentions.
approach:
  - Stratified multi-stage probability sample of 5,358 households nationwide drawn from the PSA's 2023 Geo-Enabled Master Sample.
  - Survey conducted 22 January – 5 February 2026, with 98.5% response rate and ±1.3% margin of error.
  - Confidence Index (CI) computed as percentage of optimistic households minus pessimistic households for three components: economic condition, family financial situation, and family income.
  - Diffusion Index (DI) used for selected economic indicators (inflation, interest, exchange, unemployment) to show directional expectations.
  - Data segmented by income group (low, middle, high), geography (NCR, AONCR), and OFW status for detailed behavioral profiling.
  - Tables report historical time series from Q1 2021 to Q1 2026 for trend analysis.
findings:
  - "num: Overall CI for current quarter improved from -22.2% in Q4 2025 to -15.8% in Q1 2026."
  - "num: Year-ahead CI declined from 11.8% in Q4 2025 to 9.6% in Q1 2026."
  - "num: Saving intention index increased sharply from 4.6% in Q4 2025 to 12.4% in Q1 2026."
  - "num: 73.9% of saving households planned to save less than 10% of income, up from 70.3%."
  - "num: OFW households allocating remittances to savings rose to 40.2% from 36.4%."
  - "num: Debt payments as a share of OFW remittance use declined to 27.2% from 29.0%."
  - "num: Spending outlook for Q2 2026 declined to 40.3% from 43.7% in Q4 2025."
  - "num: Borrowing intention index for next quarter improved to -69.5% from -71.7%."
  - "num: 58.6% of households intending to buy property preferred price range ₱450,000 and below."
  - "num: Year-ahead inflation forecast rose to 2.7% from 2.6%, below the BSP 3.0% target."
key_figures_tables:
  - "Figure 1: Overall Consumer Confidence Index (Q1 2021–Q1 2026) → Current quarter less negative, year-ahead less upbeat."
  - "Figure 2: CI by Component Index → Family financial situation and economic condition improved significantly."
  - "Figure 3: CI by Income Group → Confidence improved across all groups in Q1 2026."
  - "Table 1: Overall consumer outlook composite index → Shows historical CIs across time periods and segments."
  - "Table 10: Savings sentiment of households → 56.2% plan to save, 26.1% allocate ≥10% of income."
  - "Table 12: OFW remittance use → 96.1% for food, 69.9% education, 40.2% savings."
  - "Table 15a: Borrowing intention index → Less negative for next quarter and next 12 months."
key_equations:
  - equation: CI = (% Optimistic) - (% Pessimistic)
    explanation: Net balance measure of consumer sentiment.
definitions:
  - term: CI
    definition: Confidence Index; percentage of optimistic households minus pessimistic households.
  - term: DI
    definition: Diffusion Index; measures directional expectations for economic indicators.
  - term: NCR
    definition: National Capital Region (Metro Manila).
  - term: AONCR
    definition: Areas Outside the National Capital Region.
  - term: Low-income group
    definition: Monthly family income below ₱10,000.
  - term: Middle-income group
    definition: Monthly family income between ₱10,000 and ₱29,999.
  - term: High-income group
    definition: Monthly family income above ₱30,000.
  - term: OFW
    definition: Overseas Filipino Worker.
critical_citations:
  - "None."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "contextual"
      justification: "Survey segments by income, not by age or professional status."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "high"
      justification: "Provides income group data on savings, debt, spending, and remittances."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Directly measures intentions on saving, borrowing, and spending."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "medium"
      justification: "Data on OFW remittance allocation reflects family support norms."
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "medium"
      justification: "Historical quarterly time series enables cyclical analysis."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "medium"
      justification: "Spending outlook by item category can inform occasion-based budgeting."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "medium"
      justification: "Survey categorizes spending into 12 items that can ground a taxonomy."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      relevance: "low"
      justification: "Categories are broad and may need refinement for PFMS."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Provides behavioral indices (saving, spending, debt) for profiling."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Quarterly trends can inform and validate forecasting models."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "low"
      justification: "No algorithms; provides raw time series for training and validation."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "high"
      justification: "Saving intentions and spending expectations are inputs to budget strategies."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Income-group spending shares can calibrate recommended allocations."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "contextual"
      justification: "BSP's official survey data can serve as a benchmark for anonymized analysis."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "low"
      justification: "No direct measurement of trust in financial apps."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "low"
      justification: "No app engagement data; surveys measure financial intention."
    - code: "11.B"
      name: "Retention Mechanisms and Engagement Design"
      relevance: "low"
      justification: "Not applicable to survey design."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "high"
      justification: "Measures saving intention and income allocation preferences."
    - code: "13.B"
      name: "Debt Management in PFMS"
      relevance: "high"
      justification: "Provides borrowing intention and debt application indices."
    - code: "13.C"
      name: "End-of-Period Surplus as a Savings Input"
      relevance: "medium"
      justification: "Surplus is implied by saving intention and income allocation data."
  contribution: "This BSP survey provides official, nationally representative data on Filipino consumer sentiment, spending, saving, and borrowing intentions. It can calibrate Odin's behavioral profiling module with income-group and geographic baselines. The quarterly time series supports forecasting model validation for spending and savings. The detailed item-level spending outlook informs Odin's expense categorization and budget recommendation logic. The survey's historical consistency makes it a reliable reference for testing Odin's algorithmic modules."
  directly_justifies:
    - "Consumer confidence in the Philippines improved in Q1 2026 but year-ahead outlook declined."
    - "Saving intention increased sharply to 12.4% in Q1 2026, indicating greater financial prudence."
    - "OFW households allocate 40.2% of remittances to savings, a key baseline for surplus modeling."
    - "Spending outlook for Q2 2026 declined to 40.3%, suggesting cautious consumer behavior."
    - "Low-income groups have the most pessimistic outlook, consistent with their financial constraints."
  limits:
    - "Survey is conducted quarterly, not in real-time, limiting its use for dynamic PFMS tuning."
    - "Confidence and intention are stated preferences, not actual observed behavior."
    - "Income groups are broad; no specific data for young professionals aged 22–35."
    - "No algorithmic evaluation; purely descriptive and inferential statistics."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The survey was flagged as highly relevant to Financial Structure (1.B), Financial Behavior (1.C), Behavioral Profiling (5.A), Budgeting Strategies (7.A), Budget Recommendation (7.B), and Savings & Debt Management (13.A, 13.B) because it directly measures consumer intentions and income-based expectations. Medium relevance was assigned to Culturally Specific Practices (2.A), Seasonal Spending (2.B), Spending Cycles (2.D), Expense Categorization (3.A), Predictive Modeling (6.A), and Surplus as Savings (13.C) due to the survey's time-series and categorization capabilities. Low relevance was noted for App Engagement and Privacy, as the survey does not address these. Contextual relevance was noted for 1.A, 10.A, and 10.B due to indirect demographic framing. Borderline cases included 3.A (expense categories) vs. 3.B (design) – selected 3.A because the survey provides a category list, not design rationale. Also, 6.A vs. 6.B – selected 6.A because the survey's historical data can support model validation. Overall, the paper is highly relevant as a foundational dataset for Odin's behavioral and forecasting modules, but lacks algorithmic or privacy-specific content."
limitations:
  - "Survey period ended before the US-Israel-Iran conflict, so data does not reflect subsequent economic shocks."
  - "Only forward-looking questions on savings and debt were retained after Q1 2025; no current-period data for comparison."
  - "Income groups are based on total household income, not individual professional status, limiting direct applicability to young professionals."
  - "No data on user trust, privacy concerns, or mobile app usage. [unacknowledged]"
  - "No experimental validation of forecasting models or budget recommendation algorithms. [unacknowledged]"
remember_this:
  - "Consumer confidence improved to -15.8% in Q1 2026 from -22.2% in Q4 2025."
  - "Saving intention index surged to 12.4%, indicating rising financial prudence."
  - "OFW households allocated 40.2% of remittances to savings, up from 36.4%."
  - "Year-ahead inflation forecast rose to 2.7%, just below the BSP's 3.0% target."
  - "Spending outlook for Q2 2026 declined to 40.3%, signaling cautious consumer behavior."
```