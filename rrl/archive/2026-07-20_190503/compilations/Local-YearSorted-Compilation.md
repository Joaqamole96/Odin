# Compiled Research Summaries

## Filters Applied

- Designation: `local`

**Total Papers:** 88

**Note:** Sorted by year.

---

## Paper 1: Romero et al_summarized.md

**Source File:** `Romero et al_summarized.md`

```yaml
paper_id: c3d8e9f0-1a2b-4c5d-6e7f-8a9b0c1d2e3f
designation: local
title: Financial Planning Challenges in the Gig Economy: An Exploratory Factor Analysis
authors: Romero, R. S.; Villamera, N.; Mamac, M. V.
year: 2026
venue: The International Journal of Business Management and Technology
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.B
  - 3.A
  - 5.A
  - 5.B
  - 10.A
  - 13.A
  - 13.B
tldr: Identifies five financial planning challenges for freelancers in Davao City: financial knowledge, security, stability, behavior, and insurance awareness.
problem_and_motivation: The gig economy's rapid growth has created a workforce facing income volatility and limited social protections. Existing research on financial planning overlooks the unique challenges of freelancers and contract-based workers, leaving a gap in understanding how to support their long-term financial security.
approach:
  - A descriptive-exploratory design was used with a sample of 200 freelancers and contractual workers from Davao City.
  - Data were collected via a self-made questionnaire validated through pilot testing, achieving a Cronbach's Alpha of 0.767.
  - Exploratory Factor Analysis via Principal Component Analysis (EFA-PCA) was applied to identify underlying financial planning challenges.
  - Assumptions were verified using Bartlett's Test of Sphericity (p < 0.001) and KMO-MSA (0.808).
  - Factor extraction used eigenvalues > 1 and cumulative variance > 60%, with varimax rotation for interpretation.
findings:
  - num: KMO-MSA of 0.808 confirmed data suitability for factor analysis.
  - num: Five factors were extracted, explaining 70.124% of the total variance.
  - num: Q9 (a variable representing financial knowledge) had the highest communality at 0.643.
  - Financial knowledge, financial security, insurance awareness, financial stability, and financial behavior were identified as the primary challenges.
  - The study concludes that current financial practices and social security systems are insufficient for this workforce.
key_figures_tables:
  - Table 1: Bartlett's Test of Sphericity (x²=13023, p<0.001) → Data are suitable for factor analysis.
  - Table 2: KMO-MSA of 0.808 → Data structure is good for factor analysis.
  - Table 3: Communalities of variables (0.431 to 0.643) → Most variables share common variance.
  - Table 4: Factor Extraction Matrix (Eigenvalues 5.388 to 1.095) → Five factors account for 70.124% variance.
  - Figure 1: Scree Plot shows elbow at 5th component → Confirms five-factor solution.
  - Table 5: Factor Loading Matrix shows variables grouped into five distinct factors → Labelled as Financial Knowledge, Financial Security, Insurance Awareness, Financial Stability, and Financial Behavior.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: EFA-PCA
    definition: Exploratory Factor Analysis using Principal Component Analysis, a statistical method to identify underlying relationships between variables.
  - term: KMO-MSA
    definition: Kaiser-Meyer-Olkin Measure of Sampling Adequacy, a statistic indicating the proportion of variance among variables that might be common variance.
critical_citations:
  - "[Ahmad, 2020] — Highlights income volatility for gig workers."
  - "[Alvarez De La Vega et al., 2021] — Discusses freelancers' platform experiences."
  - "[Khapra et al., 2025] — Examines financial realities and money challenges of freelancers."
  - "[Mallick & Das, 2025] — Explores financial capability among gig workers."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: Focuses on freelancers in Davao City, a subset of the target demographic.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Details the irregular income structure and lack of formal employment for gig workers.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly investigates financial behavior and its challenges for freelancers.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Implicitly addresses income volatility that leads to cyclical spending, but not the core focus.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: low
      justification: Discusses budgeting challenges, implying a need for better categorization, but does not propose a framework.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Identifies "financial behavior" as a key challenge, directly contributing to profile understanding.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: Discusses challenges but does not address profile dynamics or cold-start specifically.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Does not address data privacy or security.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: contextual
      justification: Mentions achieving financial stability and security, which relates to savings, but not goal management.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: contextual
      justification: Briefly mentions freedom from debt as an objective of financial planning.
  contribution: "This paper provides foundational evidence for Odin's financial behavior profiling module by identifying financial behavior as a primary challenge for Filipino gig workers. It supports the need for a feature that helps users understand their own financial practices, as behaviors like prioritizing daily expenses hinder long-term planning. The findings also justify the development of budget recommendation and forecasting features in Odin, as income instability and financial insecurity are key user pain points. Furthermore, it validates the inclusion of financial literacy tools within the app to address low financial knowledge. The study's focus on Davao City freelancers offers a contextual baseline for Odin's target user group in the Philippines."
  directly_justifies:
    - "Freelancers struggle with financial behavior, highlighting the need for behavior tracking and profiling in Odin."
    - "Income instability among gig workers justifies the development of robust forecasting and budget recommendation features."
    - "Low financial knowledge among freelancers supports the integration of educational modules and tools in the PFMS."
    - "Financial security and stability challenges validate the inclusion of savings and debt management features in Odin."
  limits:
    - "The study is based on a sample of 200 freelancers from Davao City, limiting generalizability to the broader Filipino young professional population."
    - "The focus is on identifying challenges, not on evaluating potential solutions or algorithms for a PFMS."
    - "The descriptive-exploratory design identifies factors but does not test causal relationships between them."
  mapping_rationale: "A systematic scan across all 12 functional domains was conducted. The paper's primary focus on financial challenges for gig workers flagged Domains related to 'Behavioral Profiling & Classification' (5.A, 5.B) and 'Savings & Debt Management' (13.A, 13.B) as having high and medium relevance, respectively. The 'Expense Categorization' (3.A) domain was considered but rejected as the paper does not propose a framework, only notes challenges. The 'Filipino Cultural Context' (2.B) domain was considered borderline, as seasonal spending is not directly studied, but the paper's discussion of income volatility provides contextual background. Domains like 'Spending Forecasting', 'Budget Recommendation', and 'Anomaly Detection' were considered and rejected, as the paper is descriptive and does not involve algorithmic development or evaluation. Overall, the paper is highly relevant for understanding user pain points (e.g., financial behavior, knowledge) that justify Odin's core features, but does not provide evidence for specific algorithmic approaches."
limitations:
  - "The study relies on self-reported data, which may introduce social desirability bias. [unacknowledged]"
  - "It does not distinguish between different types of freelancers (e.g., creative vs. tech), potentially masking sub-group differences. [unacknowledged]"
  - "The research is cross-sectional, capturing challenges at a single point in time and not their evolution. [unacknowledged]"
remember_this:
  - "Freelancers in Davao City face five key financial challenges: knowledge, security, stability, behavior, and insurance."
  - "A KMO-MSA of 0.808 confirmed the data was suitable for identifying these core financial planning challenges."
  - "The study confirms that income volatility is a primary driver of financial instability for gig workers."
  - "Low financial knowledge and behavior hinder freelancers' ability to plan for the future effectively."
  - "Existing social security systems are insufficient, creating a need for inclusive financial products and policies."
```
---

## Paper 2: Bangko Sentral ng Pilipinas-2026_summarized.md

**Source File:** `Bangko Sentral ng Pilipinas-2026_summarized.md`

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
---

## Paper 3: Amado_summarized.md

**Source File:** `Amado_summarized.md`

```yaml
paper_id: 10.63498/ijabms2
designation: local
title: The plight of teachers on the twice-a-month salary release: Financial literacy and survival
authors: Amado, M. A. A.
year: 2026
venue: International Journal of Accountancy, Business, and Management Studies
odin_topics:
  - 2.D
  - 5.A
  - 13.B
  - 2.B
  - 2.A
  - 5.C
  - 13.A
  - 1.C
tldr: Examines how the twice-a-month salary release system affects Filipino teachers' financial well-being, literacy, and survival strategies.
problem_and_motivation: Teachers experience chronic financial instability, yet existing literature lacks explicit analysis of how the bi-monthly salary cycle functions as a structural determinant of economic survival behaviors. This gap necessitates investigating the inter-payday period as a psychological and economic stressor that dictates resource management.
approach:
  - Descriptive survey design using a validated structured questionnaire (Cronbach's α = 0.88).
  - Sample of 115 teachers from Claveria North District selected via simple random sampling using Taro Yamane's formula.
  - Data collected from September to October 2023, covering demographics, financial literacy, management practices, and coping strategies.
  - Analysis employed weighted mean and percentage distribution to quantify financial well-being and management practices.
  - 5-point Likert scale used to interpret responses, with adjectival descriptions assigned to each mean range.
findings:
  - "num: Overall weighted mean of 4.18 for impact on financial well-being, indicating agreement that the system supports short-term planning."
  - "num: Overall weighted mean of 4.13 for financial management practices, showing proactive budgeting (4.32) and prioritization of essentials (4.46)."
  - "num: Perceived advantages of the system had an overall mean of 4.23, while perceived disadvantages had a mean of 3.50."
  - "num: Financial literacy positively influences financial management under the system (overall mean 4.21), with higher literacy linked to better handling of challenges (4.37)."
  - "num: Survival strategies overall mean was 4.07, highlighting strict budgeting (4.13) and prioritization of essentials (4.37)."
  - Teachers still experience intermittent financial stress and timing-related challenges between pay periods.
  - Financial literacy is a critical factor in enhancing financial resilience and survival strategies.
key_figures_tables:
  - Table 1: Impact on financial well-being → Teachers agree the system aids short-term planning but does not eliminate financial stress.
  - Table 2: Financial management practices → Teachers employ proactive budgeting and prioritize essential expenses to cope.
  - Table 3: Advantages and disadvantages → Teachers recognize benefits but also acknowledge periodic financial strain.
  - Table 4: Influence of financial literacy → Higher literacy directly improves financial management under the system.
  - Table 5: Survival strategies → Teachers use strict budgeting, supplemental income, and social support to survive between paydays.
key_equations:
  - equation: Mn = Σfx / Σf
    explanation: Weighted mean formula for summarizing Likert scale responses.
  - equation: Percentage (%) = (f / N) * 100
    explanation: Percentage formula for frequency distribution of responses.
definitions:
  - term: paluwagan
    definition: Informal rotating savings and credit association in the Philippines.
  - term: 5-6 lending
    definition: Informal lending practice with high interest rates (20%).
  - term: DepEd
    definition: Department of Education in the Philippines.
  - term: SY
    definition: School Year.
critical_citations:
  - "[Lusardi & Mitchell, 2014] — Foundational theory on financial literacy's economic importance."
  - "[Casingal & Ancho, 2022] — Contextualizes financial vulnerability of Filipino teachers."
  - "[Mukuka & Mambwe, 2019] — Highlights global expectations gap for teachers as financial role models."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Examines financial behaviors of teachers under a specific salary structure.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Discusses informal lending (5-6) and paluwagan as survival strategies.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: References cyclical debt patterns but does not focus on seasonal spending.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: high
      justification: Directly analyzes the inter-payday period as a cyclical economic stressor.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Categorizes teachers' adaptive financial behaviors and resilience.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses survey to classify financial management practices and coping strategies.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: Mentions savings but does not focus on goal-based management.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: Highlights recursive debt cycles as a key survival strategy.
  contribution: This paper provides empirical evidence that salary release frequency directly impacts financial well-being and literacy, which is relevant for Odin's budgeting and financial management modules. The findings on survival strategies like paluwagan and debt cycles inform Odin's debt management and cultural context modules. The study's emphasis on financial literacy as a mitigating factor supports Odin's educational and profiling components. The identified gaps between pay periods justify Odin's forecasting and anomaly detection features to help users manage intermittent cash flow.
  directly_justifies:
    - The twice-a-month salary system supports short-term planning but not long-term stability.
    - Financial literacy significantly influences the ability to manage finances under segmented salary releases.
    - Teachers rely on informal lending and social support networks for financial survival.
    - Persistent financial stress exists even with more frequent salary disbursements.
    - Proactive budgeting and prioritization of essentials are key coping mechanisms.
  limits:
    - Study is limited to one district in the Philippines, reducing generalizability.
    - Cross-sectional design captures a snapshot, not long-term trends. [unacknowledged]
    - Self-reported data may introduce social desirability bias. [unacknowledged]
    - Does not compare with other salary release frequencies directly.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was conducted. The paper was flagged as highly relevant for Filipino Cultural Context (2.D and 2.A) and Behavioral Profiling (5.A, 5.C) due to its focus on financial behaviors under a specific salary cycle. Medium relevance was assigned to 1.C and 2.A for contextual financial practices. Borderline cases included seasonal spending (2.B), which was rated contextual as the paper focuses on the structural cycle rather than seasonal variations, and savings management (13.A), which was rated low as savings are not the primary focus. Domains like Expense Categorization (3.A-C), Forecasting (6.A-B), Budget Recommendation (7.A-D), Anomaly Detection (8.A-C), Mobile-First Design (9.A-B), Data Privacy (10.A-B), Retention (11.A-B), and Evaluation (12.A-C) were considered and rejected due to a lack of direct evidence. Overall, the paper is contextually and methodologically relevant for informing Odin's design regarding cash flow management and user financial behavior.
limitations:
  - Study is limited to one district, reducing generalizability.
  - Relies on self-reported data, which may be subject to bias.
  - Cross-sectional design prevents causal inference. [unacknowledged]
  - Does not compare the twice-a-month system against other frequencies. [unacknowledged]
remember_this:
  - Twice-a-month salary supports short-term planning but not long-term stability.
  - Financial literacy is critical for managing finances under segmented salary systems.
  - Teachers use paluwagan and debt cycles as survival strategies.
  - Budgeting and prioritizing essentials are key coping mechanisms.
  - Financial stress persists between pay periods despite more frequent salary releases.
```
---

## Paper 4: Pesa et al_summarized.md

**Source File:** `Pesa et al_summarized.md`

```yaml
paper_id: 10.62986/dp2026.03
designation: local
title: Digital Financial Platform Engagement and Financial Inclusion in the Philippines: Insights on AI Deployment and Policy Implications
authors: Pesa, N. C.; Agner, M. G. R.; Lacaza, R. M.
year: 2026
venue: PIDS Discussion Paper Series
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 3.A
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 6.A
  - 7.A
  - 8.A
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 12.A
tldr: Digital financial engagement strongly predicts formal account ownership and usage in the Philippines, yet AI adoption remains nascent and concentrated among large institutions, with persistent barriers of cost, trust, and documentation.
problem_and_motivation: The Philippines has made progress in financial inclusion, yet a large segment remains unbanked due to cost, distance, lack of documentation, and low trust. Digital financial platforms and AI offer potential solutions, but their deployment and impact are not well understood.
approach:
  - Constructed a Digital Financial Engagement Index using Multiple Correspondence Analysis on World Bank Global Findex 2021 data for the Philippines.
  - Estimated logit models to examine the relationship between digital engagement and account ownership, usage, and perceived barriers.
  - Analyzed supply-side trends using IMF Financial Access Survey data (2016-2024) on financial infrastructure.
  - Conducted key informant interviews with 12 experts from universal banks, cooperatives, savings and loan associations, and policy institutions.
  - Triangulated demand-side survey data with supply-side institutional data and qualitative insights to provide a comprehensive assessment.
findings:
  - num: A one-unit increase in the Digital Financial Engagement Index is associated with a 78.5 percentage point increase in formal account ownership likelihood.
  - num: Digital financial engagement reduces the probability of citing 'lack of trust' as a barrier by 29.4 percentage points.
  - Digital financial engagement is a stronger predictor for account entry than for more complex behaviors like saving or borrowing.
  - AI adoption in the Philippine financial sector is nascent and concentrated among large, digitally advanced institutions.
  - Persistent barriers to inclusion include lack of money (76%), high costs (55%), and distance (40%).
findings:
  - num: A one-unit increase in the Digital Financial Engagement Index is associated with a 78.5 percentage point increase in formal account ownership.
  - num: Digital financial engagement reduces the likelihood of citing 'lack of trust' as a barrier by 29.4 percentage points.
  - num: Only 2% of Filipinos can correctly answer basic financial literacy questions, according to the BSP's 2021 survey.
  - Digital financial engagement more strongly predicts account entry than continued usage.
  - AI adoption is nascent, concentrated in large institutions, and used mainly for fraud detection and credit scoring.
key_figures_tables:
  - Figure 1: Share of digital payments in total retail transactions (2018-2024) → Digital retail payment volume reached 57.4% in 2024.
  - Figure 2: Mode of payment used by adult Filipinos (2019 and 2021) → Cash remains dominant, but digital payments are growing.
  - Table 5: Financial inclusion indicators for account ownership and usage → Account ownership is 56%, formal saving only 28%.
  - Table 6: Reasons for not having a formal account → Lack of money (76%) and high cost (55%) are top barriers.
  - Table 10: Determinants of account ownership → Digital engagement is the strongest predictor for all account types.
key_equations:
  - equation: logit(P(Y_i = 1)) = β0 + β1 DigitalIndex_i + β2 X_i + ε_i
    explanation: Logit model linking digital engagement to financial inclusion outcomes.
  - equation: logit(P(B_i = 1)) = γ0 + γ1 DigitalIndex_i + γ2 X_i + ν_i
    explanation: Logit model for perceived barriers to account ownership.
definitions:
  - term: AI Preparedness Index (AIPI)
    definition: IMF metric measuring digital infrastructure, human capital, innovation, and regulation for AI.
  - term: Digital Financial Engagement Index
    definition: A 0-1 index measuring individual usage of mobile payments, online banking, and digital transactions.
  - term: Global Findex
    definition: World Bank database on financial inclusion, covering account ownership, usage, and barriers.
  - term: KII
    definition: Key Informant Interview, a qualitative method for gathering insights from subject matter experts.
  - term: NSFI
    definition: National Strategy for Financial Inclusion, the Philippines' roadmap for expanding financial access.
critical_citations:
  - "[Debuque-Gonzales and Corpus, 2021] — Provides Philippine financial inclusion index and determinants."
  - "[Fazal et al., 2023] — Systematic review linking AI and financial inclusion in developing economies."
  - "[World Bank Global Findex, 2021] — Primary demand-side data source on financial inclusion."
  - "[IMF Financial Access Survey, 2024] — Primary supply-side data source on financial infrastructure."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: "Discusses Filipino adults' financial behavior, including young, tech-savvy consumers."
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: "Analyzes account ownership, saving, and borrowing patterns among Filipino adults."
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: "Directly examines digital financial engagement and its link to financial behavior."
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: "Identifies reliance on informal saving clubs (paluwagan) and family as key financial practices."
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: "Discusses spending cycles indirectly through mentions of remittances and informal borrowing."
    - code: 2.D
      name: Filipino Spending Cycles and 'Occasions'
      relevance: contextual
      justification: "Contextualizes financial behavior within Filipino cultural and social practices."
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: low
      justification: "Not a focus; the paper focuses on broader financial inclusion, not categorization."
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: "Comprehensively reviews the Philippine financial inclusion landscape and digital platforms."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: "Identifies barriers like cost, trust, and institutional disparities in AI adoption."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: "Constructs a Digital Financial Engagement Index, which is a behavioral profile."
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: "Uses Multiple Correspondence Analysis to classify and measure digital financial engagement."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: low
      justification: "Discusses AI for credit scoring, but does not detail specific predictive models."
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: low
      justification: "Not a direct focus; the paper is about inclusion, not specific budgeting strategies."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: "Identifies fraud detection as a key AI application, which is a form of anomaly detection."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: "Discusses data privacy, cybersecurity, and the need for secure AI deployment."
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: "Explicitly analyzes trust as a barrier and finds digital engagement reduces mistrust."
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: "The core of the paper is analyzing how digital engagement drives financial inclusion."
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: "Discusses initiatives like Bank on Wheels to improve access and engagement."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: "Uses regression analysis to evaluate the impact of digital engagement on inclusion."
  contribution: "This paper provides a comprehensive, two-sided analysis of financial inclusion in the Philippines, bridging demand-side consumer behavior with supply-side institutional readiness. It introduces a novel Digital Financial Engagement Index to quantify how digital platform usage drives account ownership and usage. The study also documents the nascent state of AI adoption in the Philippine financial sector, highlighting its concentration in large institutions and key use cases like fraud detection and credit scoring. These findings directly inform Odin's design by providing empirical justification for prioritizing digital engagement as a core module, and by demonstrating the importance of building trust and literacy into the system. The identification of persistent barriers like cost, documentation, and trust provides a clear mandate for Odin's features, such as user-defined constraints and anomaly detection."
  directly_justifies:
    - "Digital financial engagement is the strongest predictor of formal account ownership in the Philippines."
    - "Greater engagement with digital platforms reduces lack of trust in financial institutions."
    - "AI adoption for fraud detection and credit scoring can enhance security and access."
    - "Cost and lack of documentation are the most significant barriers to financial inclusion."
    - "Smaller institutions face structural barriers to AI adoption."
  limits:
    - "The demand-side analysis uses digital engagement as a proxy for AI exposure, as the Global Findex does not directly measure AI awareness or usage."
    - "The actual AI exposure varies by platform, which is not captured in the survey data."
    - "The study does not examine the technical specifications or performance of specific AI systems."
    - "The supply-side analysis relies on a small sample of key informants and may not be fully representative."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper's focus on digital financial engagement and financial inclusion directly maps to the 'Behavioral Profiling & Classification', 'Existing Systems & Gaps', and 'Data Privacy & User Trust' domains, resulting in high relevance for topics 1.C, 2.A, 4.A, 4.B, 5.A, 5.C, 10.A, 10.B, and 11.A. The paper's analysis of AI deployment for fraud detection and credit scoring provides medium relevance to topics 8.A and 6.A, respectively. Topics related to specific budgeting strategies (7.A) or expense categorization (3.A) were considered but rejected as the paper does not address these implementation-level details. The paper's discussion of Filipino financial practices (2.B, 2.D) and demographic context (1.A, 1.B) provides contextual or medium relevance. The overall relevance is high, as the paper provides direct empirical justification for Odin's core design by demonstrating that digital engagement drives inclusion and that trust and security are critical."
limitations:
  - "The Global Findex survey does not include direct questions about AI awareness, usage, or literacy, so digital engagement is used as an indirect proxy. [unacknowledged]"
  - "The Digital Financial Engagement Index cannot distinguish between high-AI and low-AI platforms, as this information is not available in the survey. [unacknowledged]"
  - "The qualitative supply-side analysis is based on a limited number of key informant interviews and may not capture the full diversity of institutional experiences. [unacknowledged]"
  - "The study does not evaluate the technical performance or fairness of specific AI algorithms used in the financial sector. [unacknowledged]"
remember_this:
  - "Digital engagement is the strongest predictor of account ownership."
  - "Cost and trust are the primary barriers to financial inclusion."
  - "AI adoption in Philippine finance is nascent and uneven."
  - "Targeted literacy programs can complement digital infrastructure."
```
---

## Paper 5: Cabalfin et al_summarized.md

**Source File:** `Cabalfin et al_summarized.md`

```yaml
paper_id: 10.62986/dp2026.01
designation: local
title: The Middle Class and Vulnerability to Income Poverty: Implications for Social Protection in the Philippines
authors: Cabalfin, D. L. D.; Albert, J. R.; Mahmoud, M. A.
year: 2026
venue: PIDS Discussion Paper Series
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.B
  - 2.D
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 7.A
  - 9.A
  - 10.A
  - 10.B
  - 11.A
  - 13.A
  - 13.B
  - 13.C
tldr: Vulnerability to income poverty affects 30.0 percent of Filipino households, 2.75 times the poverty incidence, primarily due to income volatility.
problem_and_motivation: Traditional poverty measures underestimate the population at risk of economic insecurity. The COVID-19 pandemic exposed the fragility of recent poverty reduction gains and the vulnerability of households to aggregate shocks. A forward-looking measure of vulnerability is needed to inform social protection design beyond static poverty statistics.
approach:
  - The study uses the Chaudhuri and Datt (2001) methodology to estimate vulnerability as a probability of future poverty.
  - The approach models per capita household income as a function of observable characteristics and assumes heteroskedastic errors.
  - The analysis uses cross-sectional data from the merged Family Income and Expenditure Survey and Labor Force Survey for 2018, 2021, and 2023.
  - It incorporates infrastructure indices from the 2020 Census of Population and Housing and rainfall shock data from PAGASA.
findings:
  - num: Vulnerability affects 30.0 percent of households, which is 2.75 times higher than the household poverty incidence of 10.9 percent in 2023.
  - num: Eighty-six percent of vulnerable families experience income volatility, while 73.0 percent of the highly vulnerable have persistently low incomes.
  - num: Rural vulnerability incidence is 43.0 percent, starkly higher than 20.0 percent in urban areas.
  - num: Regional vulnerability ranges from 9.0 percent in NCR to 76.0 percent in rural BARMM.
  - A majority of the vulnerable population (65.0-69.0 percent) are currently classified as non-poor.
  - Education and employment in the services sector are key protective factors against poverty and vulnerability.
  - Households reliant on agriculture have a 60.0 percent vulnerability rate and account for 61.0 percent of the highly vulnerable.
  - Social protection spending in the Philippines is low (2.7% of GDP) compared to upper-middle-income country averages.
key_figures_tables:
  - Table 8: Distribution of Filipino households by income groups shows a shift toward lower-income categories in urban areas from 2018 to 2023.
  - Table 20: Incidence of poverty and vulnerability shows vulnerability is 2.5 to 2.75 times higher than observed poverty.
  - Table 21: Poverty and vulnerability within different segments of the population show stark rural-urban and regional disparities.
  - Figure 3: Estimated mean and standard deviation of income reveals that households can be vulnerable due to low income or high volatility.
key_equations:
  - equation: y_h = X_h β + e_h
    explanation: Models per capita income as a function of observable characteristics.
  - equation: σ_e,h^2 = X_h θ
    explanation: Allows the variance of the error term to depend on household attributes.
  - equation: \hat{v}_h = Φ( (ln z - X_h \hat{β}) / \sqrt{X_h \hat{θ}} )
    explanation: Estimates the probability a household will be poor in the future.
definitions:
  - term: Vulnerability
    definition: An ex-ante, forward-looking measure of the probability of being poor in the future.
  - term: High-Volatility Income Vulnerable
    definition: Vulnerable households with mean income above the poverty line but highly unstable incomes.
  - term: Low-Mean Income Vulnerable
    definition: Vulnerable households with expected incomes below the poverty line.
  - term: 4Ps
    definition: Pantawid Pamilyang Pilipino Program, a conditional cash transfer program for the poorest.
critical_citations:
  - "[Chaudhuri and Datt, 2001] — Provides the core methodology for estimating vulnerability."
  - "[Albert et al., 2024] — Key reference on middle-class dynamics in the Philippines."
  - "[Dercon, 2001] — Foundational framework for analyzing vulnerability to poverty."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Provides income and expenditure profiles relevant for understanding FYP financial structure.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Details income sources and expenditure patterns across income groups.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Discusses savings rates, employment security, and expenditure behavior.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Mentions seasonal rainfall shocks and their impact on household income.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Touch on consumption patterns and vulnerability to shocks.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Provides a detailed profile of the middle class and income distribution in the Philippines.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Explicitly identifies gaps in social protection coverage for non-poor vulnerable households.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: Classification of households by sources of vulnerability (volatility vs. low income).
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: Discusses dynamics of poverty and vulnerability, but not cold-start issue.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: Provides empirical basis for why budgeting is important by showing vulnerability.
    - code: 9.A
      name: Mobile‑First Design Principles and Rationale
      relevance: low
      justification: Paper focuses on policy, not design, but informs the need for accessible systems.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Not directly addressed, but informs the context for user trust.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: Highlights trust in social protection systems, transferable to PFMS.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: Paper discusses engagement in the context of social protection policy.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: Highlights low savings rates among vulnerable households as a key risk factor.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: low
      justification: Not directly discussed but implied through vulnerability and shocks.
    - code: 13.C
      name: End‑of‑Period Surplus as a Savings Input
      relevance: high
      justification: Low savings rates create vulnerability, making surplus management critical.
  contribution: This paper provides empirical estimates of household vulnerability to poverty in the Philippines, demonstrating that it is 2.75 times higher than current poverty incidence. It directly informs Odin's risk assessment module by identifying income volatility and low asset buffers as key vulnerability drivers. The analysis of diverse income groups and expenditure patterns is critical for designing a budget recommendation system that accounts for regional disparities and economic shocks. Its findings on social protection gaps justify Odin's focus on savings and debt management features for Filipino young professionals. The study's methodology for classifying sources of vulnerability offers a framework for developing behavioral profiles for user personalization.
  directly_justifies:
    - "Vulnerability incidence is 30.0 percent, far exceeding the 10.9 percent household poverty rate."
    - "Income volatility, not just low income, is the primary driver of vulnerability for most households."
    - "Low savings rates among the low-income class (5.8 to 11.3 percent median) create a severe lack of financial cushion."
    - "Households with heads in agriculture have a 60.0 percent vulnerability rate, requiring targeted savings strategies."
    - "Social protection coverage is only 34.9 percent, justifying Odin's role in providing accessible financial management tools."
  limits:
    - "The vulnerability estimation relies on cross-sectional data and assumes independent idiosyncratic shocks."
    - "The study does not include individual-level financial behavior data which would be relevant for a PFMS."
    - "The analysis is at the household level, not the individual level of a Filipino young professional." [unacknowledged]
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was conducted. The domains of "Filipino Cultural Context," "Existing Systems & Gaps," "Behavioral Profiling," "Budget Recommendation," and "Savings & Debt Management" were flagged as having direct relevance to Odin. The paper provides high relevance for topics 4.B (social protection gaps), 13.A (low savings rates), and 13.C (surplus as savings input) because it provides direct empirical evidence for vulnerabilities Odin aims to address. It is of medium relevance to 1.A, 1.B, 1.C, 4.A, and 5.A as it profiles the demographic and financial structures of Filipino households and begins to classify vulnerability sources. The topics on "Seasonal and Cyclical Spending" (2.B) and "Mobile-First Design" (9.A) were considered but assigned low/contextual relevance as they are only tangentially mentioned or not the paper's focus. Domains such as "Expense Categorization," "Forecasting," "Anomaly Detection," and "System Evaluation" were considered and rejected because the paper does not address algorithmic approaches or system design. Overall, the paper is highly relevant for establishing the problem context and justifying the need for a PFMS like Odin focused on resilience-building and financial planning, particularly for the vulnerable non-poor.
limitations:
  - "The estimation of vulnerability relies on cross-sectional data, which cannot perfectly capture the dynamics of income volatility over time."
  - "The methodology assumes that idiosyncratic shocks are independent and do not persist, which may not hold for all households."
  - "The paper does not cover algorithmic or computational approaches to personal finance management."
  - "Social protection spending data are from 2022 and may not reflect the latest policy developments."
  - "The analysis is at the household level, not specifically focused on the demographic of Filipino young professionals." [unacknowledged]
remember_this:
  - "Vulnerability to poverty is 2.75 times higher than the actual poverty rate."
  - "Income volatility is the main source of vulnerability for 86.0 percent of at-risk households."
  - "Social protection coverage in the Philippines is only 34.9 percent, leaving many unprotected."
  - "Low savings rates are a critical factor driving household vulnerability."
  - "Investment in education and formal employment are key protective factors against poverty."
```
---

## Paper 6: Claros et al_summarized.md

**Source File:** `Claros et al_summarized.md`

```yaml
paper_id: 10.5281/ZENODO.18884267
designation: local
title: Determinants of Saving Behavior Among Filipino University Students: A Psychological and Social Perspective
authors: Claros, J. R.; Gaza, J. A.; Villaverde, Z. A.; Angeles, I. T.
year: 2026
venue: Journal of Interdisciplinary and Multidisciplinary Research (JIMRES)
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 3.A
  - 4.A
  - 5.A
  - 5.C
  - 12.A
  - 12.C
tldr: Financial literacy and parental influence positively predict saving behavior among Filipino university students, while peer influence is insignificant and self-control shows a negative effect.
problem_and_motivation: University students face increasing financial pressures and often do not prioritize saving despite formal financial education. There is a gap in understanding the specific psychological and social factors that contribute to intentional saving behavior among Filipino university students.
approach:
  - A quantitative, explanatory research design using PLS-SEM was employed to examine the impact of financial literacy, self-control, peer influence, and parental influence on savings behavior.
  - Data was collected from 377 university students aged 18-25 from private and public universities across the Philippines using a structured, closed-ended online and in-person survey.
  - The questionnaire used validated six-point Likert scales to measure financial literacy, self-control, peer influence, parental influence, and saving behavior.
  - The study assessed the measurement model for reliability, convergent validity, and discriminant validity, followed by a structural model assessment to test hypotheses.
  - Model fit was evaluated using CFI, TLI, NFI, GFI, and AGFI, all exceeding the 0.90 cutoff, confirming a good fit.
findings:
  - num: The model explains 62.3% of the variance in saving behavior (R² = 0.623), which is considered substantial.
  - num: Financial literacy is the strongest predictor of saving behavior (β = 0.684, p < .001).
  - num: Parental influence has a significant positive effect on saving behavior (β = 0.284, p < .001).
  - Peer influence does not significantly predict saving behavior (β = -0.041, p = 0.423).
  - num: Self-control has a significant negative effect on saving behavior (β = -0.201, p < .001).
key_figures_tables:
  - Table 1: Model fit indices → All indices (CFI, TLI, NFI, GFI, AGFI) exceed 0.90, confirming a good model fit.
  - Table 2: Measurement model → All factor loadings are significant, with Financial Attitudes and Self-Control showing the highest loadings.
  - Table 3: Reliability measures → All constructs exceed Cronbach's Alpha and AVE thresholds, indicating strong reliability and convergent validity.
  - Table 4: HTMT correlation ratio → All HTMT ratios are below 0.85, confirming discriminant validity.
  - Table 5: Factors affecting saving behavior → Financial literacy and parental influence are significant positive predictors; self-control is a significant negative predictor.
  - Figure 3: Structural equation model → Visual representation of the significant and non-significant path relationships in the model.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: PLS-SEM
    definition: Partial Least Squares Structural Equation Modeling, a statistical technique for analyzing complex relationships between latent variables.
  - term: AVE
    definition: Average Variance Extracted, a measure of convergent validity in a construct.
  - term: HTMT
    definition: Heterotrait-Monotrait ratio, a criterion for assessing discriminant validity.
critical_citations:
  - "[Hair et al., 2021] — Justifies the use of PLS-SEM for predictive, complex models."
  - "[Katona, cited in Fisher & Anong, 2012] — Core theory linking psychological factors and saving."
  - "[Modigliani and Brumberg, cited in Martini & Spataro, 2024] — Provides the Life-Cycle Hypothesis framework."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Focuses on Filipino university students, a key demographic for Odin.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Discusses the financial situation and challenges of students, analogous to young professionals.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly investigates the saving behavior and its psychological determinants among Filipino students.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Highlights the role of parental influence and family socialization, reflecting culturally specific practices.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: Provides foundational context on how financial literacy influences saving, but not on specific categorization.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Offers background on financial literacy levels in the Philippines, contextualizing the need for PFMS.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Identifies key psychological determinants (financial literacy, self-control) for behavioral profiling.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses PLS-SEM to classify and quantify the influence of psychological factors on saving behavior.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: The PLS-SEM methodology provides a rigorous evaluation framework applicable to Odin's modules.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: high
      justification: The use of PLS-SEM to assess predictive models is directly applicable to evaluating Odin's recommendation systems.
  contribution: The paper validates a PLS-SEM model that explains a substantial portion (62.3%) of variance in saving behavior, highlighting financial literacy and parental influence as critical factors. This finding directly informs the design of Odin's behavioral profiling module by identifying key psychological variables to track. The significant negative effect of self-control challenges conventional assumptions, which is crucial for developing accurate forecasting algorithms. The non-significant influence of peers suggests that Odin's social features should be secondary to family-oriented or personal goal-setting tools. The model's robust fit provides a strong methodological benchmark for evaluating Odin's own algorithmic modules.
  directly_justifies:
    - "Financial literacy is the strongest predictor of saving behavior among young Filipinos."
    - "Parental influence has a positive and significant effect on saving behavior, highlighting the importance of social learning."
    - "Peer influence does not significantly affect the saving behavior of university students."
    - "Self-control has a negative effect on saving behavior, challenging the conventional positive association."
    - "PLS-SEM is an effective methodology for modeling the complex factors influencing financial behavior."
  limits:
    - "The study lacks demographic data like age and gender, which could allow for more nuanced subgroup analysis. [unacknowledged]"
    - "The sample consists of university students who rely on parental allowance, which may limit generalizability to young professionals. [unacknowledged]"
    - "The cross-sectional design prevents causal inference about the determinants of saving behavior. [unacknowledged]"
    - "The unexpected negative effect of self-control is not fully explained and requires further investigation. [acknowledged]"
  mapping_rationale: A systematic scan of all 12 functional domains was conducted. The paper is highly relevant to the 'Filipino Cultural Context' domain (specifically 2.A) by examining culturally specific practices like parental influence. It also strongly informs the 'Behavioral Profiling & Classification' domain (5.A, 5.C) by identifying key psychological predictors and using PLS-SEM for classification. For 'System Evaluation' (12.A, 12.C), the paper provides a validated methodology and benchmark (PLS-SEM, R²=0.623) for evaluating Odin's predictive modules. The topic 1.A (Filipino Young Professionals as a Demographic) is directly relevant as the study focuses on Filipino students. Topics like 1.B (Financial Structure) and 3.A (Expense Categorization) were considered but deemed contextual, as the paper addresses saving behavior, not income or budget allocation mechanisms. The 'Spending Forecasting' (6.A, 6.B) and 'Budget Recommendation' (7.A) domains were rejected because the paper does not involve predictive modeling of time-series data or specific allocation strategies. Overall, the paper provides strong empirical evidence on the factors driving saving behavior and a robust evaluation framework, making it highly relevant for designing and assessing Odin's behavioral and analytical modules.
limitations:
  - "The sample is limited to university students, potentially limiting generalizability to all Filipino young professionals. [unacknowledged]"
  - "The cross-sectional design precludes causal interpretations of the relationships found. [unacknowledged]"
  - "Demographic variables like age and gender were not included in the survey instrument for subgroup analysis. [acknowledged]"
  - "The negative effect of self-control was observed but the reasons remain speculative, indicating a need for further study. [acknowledged]"
remember_this:
  - Financial literacy is the strongest predictor of saving behavior among Filipino students.
  - Parental influence positively shapes saving habits, highlighting the role of family.
  - Peer influence does not significantly affect student saving behavior.
  - The model explains 62.3% of the variance in saving behavior.
  - Self-control showed an unexpected negative effect on saving behavior.
```
---

## Paper 7: Abila & Ulibas_summarized.md

**Source File:** `Abila & Ulibas_summarized.md`

```yaml
paper_id: 10.1234/ijmeri.2026.v4i2.9
designation: local
title: Analyzing the Financial Management Practices and Resilience of Online Freelancers in Laguna amid Digital Platform Taxation
authors: Abila, J. P.; Ulibas, R. N.
year: 2026
venue: IJMERI
odin_topics:
  - 2.A
  - 5.A
  - 5.C
  - 13.A
  - 13.B
tldr: Online freelancers in Laguna demonstrate moderate financial resilience and adaptive but reactive financial practices amid income volatility and the new 12% digital platform tax.
problem_and_motivation: Online freelancers face income instability and lack formal safety nets, yet empirical research on their financial resilience under new digital taxation regimes in the Philippines is limited. This gap is critical as the 2025 VAT on digital services adds financial pressure to an already vulnerable workforce.
approach:
  - A mixed-methods exploratory pilot study with a quantitative-dominant design and embedded qualitative component.
  - Surveyed 30 online freelancers in Laguna using purposive-stratified sampling and interviewed 10 participants.
  - Measured Buffer Stock Savings, Perceived Income Volatility, Liquid Asset Accessibility, and Financial Resilience via structured questionnaire.
  - Analyzed data using descriptive statistics, Pearson's correlation, multiple linear regression, and thematic coding.
findings:
  - "num: 73% of variance in financial resilience was explained by financial practices and demographic factors (R² = 0.73, p < 0.01)."
  - "num: Liquid Asset Accessibility was the only significant positive predictor of financial resilience (β = 0.58, p = 0.04)."
  - "num: Buffer Stock Savings and Liquid Asset Accessibility showed moderate positive correlations with resilience (r = 0.598 and r = 0.517, respectively)."
  - Freelancers demonstrated adaptive financial behaviors like micro-saving and reactive budgeting rather than structured long-term planning.
  - Financial resilience was moderate, with confidence in recovery but low preparedness for large shocks like medical emergencies.
  - Digital Platform Taxation increased financial stress but also encouraged better financial recordkeeping among some freelancers.
key_figures_tables:
  - "Table 4: Mean scores of financial management practices → Overall high (3.47) but Perceived Income Volatility was moderate (3.10)."
  - "Table 5: Descriptive statistics of financial resilience items → Overall moderate (3.19) with highest confidence in recovery (3.81) and lowest in medical expense preparedness (2.85)."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: BSS
    definition: Buffer Stock Savings
  - term: PIV
    definition: Perceived Income Volatility
  - term: LAA
    definition: Liquid Asset Accessibility
  - term: DPT
    definition: Digital Platform Taxation
  - term: VAT
    definition: Value-Added Tax
critical_citations:
  - "[Carroll & Samwick, 1997] — foundational theory on precautionary savings."
  - "[Carroll, Hall, & Zeldes, 1992] — established the buffer-stock model of saving."
relevance:
  topics:
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Examines adaptive financial behaviors of Filipino freelancers under new tax policy.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly profiles freelancers as cautious savers, adaptive spenders, and vulnerable types.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Provides empirical categories and mixed-methods classification of financial behaviors.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: Core focus on buffer stock savings and emergency fund management for income shocks.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: contextual
      justification: Mentions reliance on family support and informal borrowing, but not a primary focus.
  contribution: This paper provides empirical evidence on the financial management practices and resilience of Filipino online freelancers, which can inform Odin's behavioral profiling module (Topic 5.A). It validates the relevance of Buffer Stock Theory for understanding user savings behavior, directly supporting the design of savings goal management features (Topic 13.A). The study also identifies liquid asset accessibility as a key predictor of resilience, suggesting that Odin's design should prioritize real-time liquidity monitoring over long-term savings alone. Furthermore, the findings highlight the need for tax-aware budgeting tools, addressing a gap in existing PFMS.
  directly_justifies:
    - "Online freelancers demonstrate adaptive but reactive financial behaviors, not structured long-term planning."
    - "Liquid asset accessibility is a stronger predictor of financial resilience than savings accumulation."
    - "Perceived income volatility negatively correlates with financial resilience."
    - "Digital platform taxation increases financial stress and awareness, influencing budgeting decisions."
  limits:
    - "Small sample size (n=30) limits generalizability."
    - "Cross-sectional design cannot establish causal relationships."
    - "Reliance on self-reported data may introduce social desirability bias."
    - "Geographic restriction to Laguna may not represent freelancers in other regions."
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The paper directly addresses financial behavior and resilience under income volatility, flagging the Behavioral Profiling domain (5.A, 5.C) as high relevance due to its classification of freelancer profiles. The Savings & Debt Management domain (13.A, 13.B) is also highly relevant due to the focus on Buffer Stock Savings and emergency funds. Culturally Specific Financial Practices (2.A) is medium relevance as the study is situated in the Filipino context with a new tax policy. Expense Categorization (3.A-C), Forecasting (6.A-B), Budget Recommendation (7.A-D), Anomaly Detection (8.A-C), Mobile-First Design (9.A-B), Data Privacy (10.A-B), Retention (11.A-B), and System Evaluation (12.A-C) were considered but rejected as the paper does not address these technical PFMS modules. The borderline case of seasonal spending (2.B) and Filipino spending cycles (2.D) was considered but rejected as the paper focuses on income volatility and tax impacts, not on culturally specific cyclical spending patterns. Overall, the paper provides strong justification for modules related to user behavioral profiling and savings management.
limitations:
  - "Small sample size (n=30) limits statistical power and generalizability."
  - "Cross-sectional design cannot establish causal effects." [unacknowledged]
  - "Reliance on self-reported data may introduce bias."
  - "Geographic scope is limited to Laguna, Philippines."
  - "Study does not distinguish between taxation awareness and taxation literacy as separate variables." [unacknowledged]
remember_this:
  - "Liquidity access, not just savings, is key to freelance financial resilience."
  - "73% of resilience variance explained by financial practices and demographics."
  - "Freelancers adapt financially but lack long-term shock preparedness."
  - "Digital tax awareness is high, but literacy and compliance gaps remain."
```
---

## Paper 8: Jandoc et al_summarized.md

**Source File:** `Jandoc et al_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: local
title: Profiling Platform Workers in the Philippines: Evidence from the Jobs and Skills Survey
authors: Jandoc, K. R. L.; Martinez, A.; Bulan, J. A. N.; Molato, R.; Guyos, A.
year: 2026
venue: UP School of Economics Discussion Papers
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 3.A
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 13.A
  - 13.B
tldr: Platform workers in the Philippines are disproportionately young, urban, and highly educated, with participation driven by flexibility for some and limited alternatives for others, and they face significantly lower access to employer-provided benefits.
problem_and_motivation: The rapid growth of non-traditional platform work in the Philippines raises concerns about job quality and social protection gaps, yet nationally representative evidence on these workers has been lacking. This study addresses that gap by profiling platform workers and comparing their employment conditions to traditional workers.
approach:
  - Used nationally representative data from the 2025 Jobs and Skills Survey, administered as a rider to the Labor Force Survey.
  - Defined platform work as using online or app-based platforms for paid tasks, encompassing both remote digital and location-based gig work.
  - Employed weighted descriptive statistics and logit regressions to analyze participation, motivations, task content, social protection, and job satisfaction.
  - Constructed a Routine Task Intensity index to compare task routinization across platform and non-platform workers.
  - Controlled for worker, occupation, industry, and firm characteristics in regression models to isolate the effect of platform work.
findings:
  - num: 8.2 percent of Filipino workers (nearly 4.1 million) engage in platform-mediated work, with 84.5 percent reporting it as their sole job.
  - num: Platform workers average 42.6 hours per week, slightly above the national average of 41.4 hours.
  - Platform workers are more likely to be female, urban, and college-educated than non-platform workers.
  - Flexibility and ease of entry are the top motivations, but transport workers are more often driven by limited job alternatives.
  - Platform work exhibits lower Routine Task Intensity than traditional jobs, but transport segments are more routinized than digital freelancing.
  - Platform workers report substantially higher overskilling rates across digital, cognitive, and communication skill domains.
  - Platform workers show significantly lower odds of receiving employer-provided pension, health insurance, and separation benefits, even after controlling for worker and firm characteristics.
  - Despite benefit deficits, platform workers report high job satisfaction and favorable access to workplace amenities.
key_figures_tables:
  - "Figure 1: Sectoral productivity vs. employment change (2001-2023) → Labor shifted from agriculture to low-productivity services, reinforcing flexible work."
  - "Figure 2: Mean Standardized RTI by platform worker type → Platform work is less routine overall, but drivers and delivery workers have positive RTI, indicating more routinized tasks."
  - "Table 2: Online platform use and worker characteristics → Platform workers are 74% urban, 69.7% higher education, and concentrated in NCR (31%)."
  - "Table 13: Logit regressions of employment benefits → Platform workers have significantly lower odds of employer pension and health insurance."
  - "Table 14: Access to workplace amenities → Platform workers generally have better amenities, but drivers and delivery workers have more constrained physical work environments."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: Platform worker
    definition: A worker who uses online or app-based platforms to perform paid tasks or services.
  - term: Routine Task Intensity (RTI)
    definition: An index measuring the extent to which a job relies on routine, codifiable tasks relative to non-routine tasks.
  - term: JSS
    definition: Jobs and Skills Survey, a nationally representative survey on job tasks and skills.
critical_citations:
  - "[Esguerra, 2019] — Highlights classification and social protection gaps for platform workers."
  - "[Beerepoot & Oprins, 2021] — Documents the profile and conditions of online freelancers."
  - "[Bayudan-Dacuycuy & Baje, 2021] — Analyzes decent work in crowdwork with gendered takeaways."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Provides detailed demographic profile of platform workers, who are disproportionately young and educated.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Documents income sources and hours worked for platform workers, many of whom rely on platform work as primary income.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Analyzes motivations for platform work, revealing opportunity-driven and necessity-driven behaviors.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: Mentions flexibility and autonomy as culturally valued, but does not deeply explore specific Filipino practices like utang na loob.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: low
      justification: Discusses structural employment patterns but not direct seasonal spending cycles in platform work.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Uses occupational and industry classifications to categorize workers, indirectly relevant to expense categorization.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Critically evaluates the landscape of social protection and benefit systems and their failure to cover platform workers.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies specific gaps in pension, health insurance, and separation benefits for platform workers.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Profiles motivations (flexibility vs. necessity) that can inform behavioral profiling for personal finance systems.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: Highlights heterogeneity across platform worker types, relevant to developing dynamic profiles.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: contextual
      justification: Notes that platform work is often primary income, relevant to savings behavior, but does not explicitly address goal management.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: contextual
      justification: Mentions limited employment alternatives, implying debt pressures, but does not directly address debt management.
    - code: 2.C
      name: User-Declared Financial Preferences
      relevance: low
      justification: No direct mention of user-declared preferences.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: No direct focus on specific spending cycles like Christmas or fiestas.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: contextual
      justification: Occupational classification provides a framework but no specific design recommendations for expense categories.
    - code: 3.C
      name: User-Defined Allocation Constraints
      relevance: low
      justification: Not addressed.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Uses descriptive and regression methods but not classification algorithms.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: low
      justification: No predictive modeling.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: No forecasting.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: low
      justification: Not addressed.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Not addressed.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: low
      justification: Not addressed.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: low
      justification: Not addressed.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Not addressed.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Not addressed.
    - code: 8.C
      name: Cold‑Start Baseline Strategies for Anomaly Detection
      relevance: low
      justification: Not addressed.
    - code: 9.A
      name: Mobile‑First Design Principles and Rationale
      relevance: low
      justification: Platform use is mentioned but not mobile design.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: Not addressed.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Not addressed.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: Not addressed.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: Not addressed.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: low
      justification: Not addressed.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: low
      justification: Not addressed.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: low
      justification: Not addressed.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: low
      justification: Not addressed.
    - code: 13.C
      name: End‑of‑Period Surplus as a Savings Input
      relevance: low
      justification: Not addressed.
  contribution: This paper provides nationally representative evidence on platform workers that can inform Odin's user profiling module by defining key demographic and behavioral segments. Its findings on benefit gaps directly justify the need for Odin's personal financial management features that help users manage irregular income and plan for social protection. The analysis of motivations (flexibility vs. necessity) supports the design of adaptive budgeting and savings features tailored to different user profiles. The documented overskilling and task routinization patterns offer insights for designing financial education and goal-setting features that align with users' actual employment contexts.
  directly_justifies:
    - "Platform workers are disproportionately young, urban, and highly educated, forming a key user segment for Odin."
    - "Flexibility is the primary motivator for most platform workers, informing Odin's value proposition."
    - "Platform workers face significantly lower access to employer-provided pension and health insurance."
    - "Transport and delivery workers often enter platform work due to limited job alternatives, requiring differentiated financial planning tools."
    - "Despite benefit deficits, platform workers report high job satisfaction and value autonomy."
  limits:
    - "Cross-sectional data limits causal inference about the long-term effects of platform work on financial health. [unacknowledged]"
    - "Self-reported motivations and skill mismatch may be subject to social desirability bias. [unacknowledged]"
    - "The definition of platform work captures use of platforms in the past two years, which may include occasional users and blur distinctions. [unacknowledged]"
    - "The survey does not track earnings volatility or income shocks over time, limiting insights for financial forecasting. [unacknowledged]"
    - "Analysis is limited to the Philippines, and findings may not generalize to other contexts."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. Domains flagged as relevant include Filipino Cultural Context (2.A, 2.B) for motivations and structural employment patterns; Expense Categorization (3.A) for occupational classification; Existing Systems & Gaps (4.A, 4.B) for social protection deficits; Behavioral Profiling (5.A, 5.B) for motivation analysis; and Savings & Debt Management (13.A, 13.B) for income and employment context. Topics 1.A, 1.B, and 1.C are assigned high relevance as the paper provides a detailed demographic and financial profile of the target user group. Topic 4.A and 4.B are high because the paper empirically documents gaps in existing social protection systems directly relevant to Odin's context. Topics 5.A and 5.B are medium to high because the motivations and heterogeneity analysis inform behavioral profiling, though the paper does not propose a classification algorithm. Topic 2.A is contextual, as the paper mentions cultural values like flexibility but does not deeply explore Filipino-specific practices. Topic 2.B is low, as seasonal spending cycles are not a focus. Topic 13.A and 13.B are contextual, as the paper discusses income sources but not explicit savings or debt management. Borderline cases include 2.A and 2.B, which were considered but ultimately deemed low/contextual because the paper's primary contribution is profiling rather than cultural or seasonal spending analysis. Domains such as Forecasting, Budget Recommendation, Anomaly Detection, Mobile Design, Data Privacy, Retention, and Evaluation were rejected because the paper does not address these technical or design-specific aspects. Overall, the paper is highly relevant to Odin's user profiling and contextual understanding, but provides limited direct guidance for algorithmic modules.
limitations:
  - "Cross-sectional data limits causal inference about the long-term effects of platform work on financial health. [unacknowledged]"
  - "Self-reported motivations and skill mismatch may be subject to social desirability bias. [unacknowledged]"
  - "The definition of platform work captures use of platforms in the past two years, which may include occasional users and blur distinctions. [unacknowledged]"
  - "The survey does not track earnings volatility or income shocks over time, limiting insights for financial forecasting. [unacknowledged]"
remember_this:
  - "Platform workers are young, urban, and highly educated, with 8.2 percent of workers engaged."
  - "Flexibility and ease of entry dominate motivations, but transport workers face more necessity-driven participation."
  - "Platform work is less routine than traditional jobs, yet transport segments are more routinized."
  - "Platform workers have significantly lower access to employer-provided pension and health insurance."
  - "Despite benefit gaps, platform workers report high job satisfaction and autonomy."
```
---

## Paper 9: Aribe & Cagande_summarized.md

**Source File:** `Aribe & Cagande_summarized.md`

```yaml
paper_id: 10.12720/jait.17.2.378-389
designation: local
title: Benchmarking Federated Learning in Edge Computing Environments: A Systematic Review and Performance Evaluation
authors: Aribe, S. G.; Cagande, G. N. T.
year: 2026
venue: Journal of Advances in Information Technology
odin_topics:
  - 4.A
  - 4.B
  - 5.C
  - 6.B
  - 8.B
  - 12.A
  - 12.B
  - 12.C
tldr: A systematic review and performance evaluation of federated learning techniques for edge computing, categorizing methods across optimization, communication, privacy, and architecture, with benchmark results showing trade-offs between accuracy, efficiency, and robustness.
problem_and_motivation: The intersection of federated learning (FL) and edge computing lacks a comprehensive review that not only categorizes techniques but also systematically benchmarks them against practical performance metrics relevant to edge scenarios. This gap hinders the selection and deployment of FL methods in resource-constrained, privacy-sensitive edge environments.
approach:
  - Followed a PRISMA-inspired and SALSA-guided systematic review methodology.
  - Searched six academic databases (IEEE Xplore, Scopus, SpringerLink, ScienceDirect, ACM DL, arXiv) for peer-reviewed papers from January 2017 to June 2025.
  - Initial search yielded 602 articles; 308 were retained after duplicate removal and applying inclusion/exclusion criteria.
  - Extracted data using a standardized template covering FL algorithm, datasets, deployment environment, and performance metrics.
  - Classified extracted studies into a four-dimensional taxonomy: optimization strategies, communication efficiency, privacy-preserving mechanisms, and system architecture.
  - Benchmarked five leading FL algorithms (FedAvg, FedProx, SCAFFOLD, FedNova, FedAvg+DP) across metrics including accuracy, convergence time, communication overhead, energy consumption, and non-IID robustness.
findings:
  - num: SCAFFOLD achieved the highest accuracy (84.7% on Shakespeare) and robust non-IID performance.
  - num: FedAvg demonstrated superior communication efficiency (45 MB/round) and energy use (38 Joules/round).
  - num: FedAvg+DP showed a noticeable performance penalty (74.1% accuracy on CIFAR-10), highlighting the privacy-utility trade-off.
  - FEMNIST (3400 clients) and Shakespeare (1126 clients) are identified as the most representative datasets for real-world edge conditions due to high non-IID severity.
  - Open challenges persist in data heterogeneity, energy efficiency, communication overhead, privacy preservation, and benchmarking reproducibility.
  - No single algorithm dominates across all criteria; selection depends on specific edge deployment priorities.
key_figures_tables:
  - Table I: Performance matrix comparing FL algorithms across datasets and metrics → SCAFFOLD leads in accuracy/robustness, FedAvg leads in efficiency.
  - Figure 3: Taxonomy diagram of FL techniques for edge computing → Visual classification into four primary methodological dimensions.
  - Figure 4: Comparison of benchmark datasets by client count and non-IID severity → FEMNIST and Shakespeare are the most challenging.
  - Figure 5: Radar plot of relative performance across five metrics → Visualizes trade-offs and highlights algorithm-specific strengths.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: FL
    definition: Federated Learning; a decentralized machine learning approach where multiple clients collaboratively train a shared model without sharing raw data.
  - term: Edge Computing
    definition: A decentralized computing paradigm that processes data at or near the source of data generation.
  - term: non-IID
    definition: Non-Independent and Identically Distributed; refers to statistical heterogeneity in data across clients.
  - term: FedAvg
    definition: Federated Averaging; a baseline FL algorithm that averages locally computed gradients or weights from selected clients.
  - term: FedProx
    definition: An FL algorithm introducing a proximal term to limit local update divergence and improve convergence under heterogeneous data.
  - term: SCAFFOLD
    definition: An FL algorithm using control variates to correct for client-drift caused by non-IID data.
  - term: Differential Privacy (DP)
    definition: A privacy-preserving technique that adds calibrated noise to local updates or global aggregations.
  - term: Secure Aggregation
    definition: A cryptographic protocol that enables secure aggregation of model updates without revealing individual contributions.
  - term: Communication Overhead
    definition: The amount of data transmitted between clients and servers per communication round, typically measured in megabytes.
critical_citations:
  - "[McMahan et al., 2016] — Introduces FedAvg, the foundational FL algorithm."
  - "[Li et al., 2020] — Surveys FL challenges and methods, including FedProx."
  - "[Karimireddy et al., 2019] — Proposes SCAFFOLD for improving FL convergence."
  - "[Kairouz et al., 2021] — Comprehensive review of advances and open problems in FL."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides a high-level framework for evaluating decentralized systems, though not finance-specific.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies limitations in FL (heterogeneity, energy, privacy) relevant to evaluating PFMS architecture gaps.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Discusses FL as a distributed classification framework; can inform profile classification design.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: contextual
      justification: Provides benchmarking methodology that can be adapted for evaluating forecasting algorithms.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Federated anomaly detection is mentioned as a future application, providing foundational context.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a structured benchmarking framework (metrics, datasets) directly applicable to evaluating Odin's modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Benchmarks FL algorithms using accuracy, convergence, communication, and energy metrics, directly transferable to Odin's module evaluation.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: The comparative matrix and radar plot methodologies offer a template for evaluating budget recommendation algorithms.
  contribution: This paper provides a systematic evaluation framework comprising performance metrics (accuracy, convergence, communication, energy, robustness) and a multi-dataset benchmarking methodology that is directly applicable to Odin's algorithmic modules. The taxonomy of FL techniques informs the design of distributed and privacy-preserving components within Odin's architecture. The comparative matrix and radar plot visualization offer a clear template for evaluating trade-offs between different recommendation or anomaly detection strategies. The identification of open challenges (heterogeneity, energy, privacy, reproducibility) highlights critical considerations for Odin's deployment and long-term viability.
  directly_justifies:
    - "Federated learning enables privacy-preserving distributed model training without sharing raw data, supporting Odin's data privacy requirements."
    - "Systematic benchmarking using multiple datasets and metrics is essential for evaluating Odin's algorithmic modules."
    - "No single algorithm dominates across all metrics, so Odin's algorithm selection must align with specific deployment priorities."
    - "Energy efficiency is a key constraint for edge deployments that should be considered in Odin's mobile-first design."
  limits:
    - "The review synthesizes simulation-based results; real-world deployment performance may differ."
    - "Does not evaluate FL algorithms specifically for personal finance or spending data."
    - "Focuses on horizontal FL; vertical FL and federated transfer learning are not systematically benchmarked."
    - "Energy consumption values are normalized across studies, not based on consistent hardware."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated canonical topic codes was conducted. The paper was flagged as relevant for the System Evaluation domain (codes 12.A, 12.B, 12.C) with high relevance because it provides a structured benchmarking framework, performance metrics, and comparative analysis methodology that directly apply to evaluating Odin's algorithmic modules. It was also relevant for Existing Systems & Gaps (codes 4.A, 4.B) with medium relevance due to its identification of systemic limitations in distributed learning systems. Behavioral Profiling & Classification (5.C), Forecasting (6.B), and Anomaly Detection (8.B) were assigned low/contextual relevance as the paper's distributed classification and anomaly detection discussions provide foundational context but are not directly finance-specific. The paper was considered but rejected for other domains such as Filipino Cultural Context, Expense Categorization, Budget Recommendation, Mobile-First Design, Data Privacy, User Retention, Savings & Debt Management as it does not address these financial or user-centric aspects. Overall, the paper's primary relevance to Odin lies in its evaluation framework and benchmarking methodology.
limitations:
  - "Benchmarking results are based on simulated edge environments, not real-world deployments. [unacknowledged]"
  - "The review does not evaluate FL algorithms on personal finance datasets, limiting direct applicability to Odin. [unacknowledged]"
  - "Energy consumption results are derived from disparate hardware platforms, making cross-study comparison difficult."
  - "Privacy metrics are proxied by the presence of DP or secure aggregation, rather than measured leakage risk."
  - "The review does not consider cross-silo FL scenarios, which may be relevant for multi-institutional financial data collaboration. [unacknowledged]"
remember_this:
  - "SCAFFOLD achieved the highest accuracy (84.7%) and robustness to non-IID data."
  - "FedAvg was the most communication-efficient (45 MB/round) and energy-efficient (38 J/round)."
  - "No single FL algorithm dominates all metrics; selection depends on deployment priorities."
  - "FEMNIST and Shakespeare best simulate real-world non-IID edge data conditions."
  - "Privacy enhancement via DP incurs a significant accuracy and convergence penalty."
```
---

## Paper 10: Am-una_summarized.md

**Source File:** `Am-una_summarized.md`

```yaml
paper_id: "10.69569/jip.2026.065"
designation: "local"
title: "Beyond Awareness: Examining Financial Behaviors Among Public School Teachers in the Philippines"
authors: "Am-una, A."
year: 2026
venue: "Journal of Interdisciplinary Perspectives"
odin_topics:
  - "1.A"
  - "1.B"
  - "1.C"
  - "2.A"
  - "2.D"
  - "3.A"
  - "3.B"
  - "4.A"
  - "4.B"
  - "5.A"
  - "5.B"
  - "7.A"
  - "7.B"
  - "10.A"
  - "11.A"
  - "11.B"
  - "12.A"
  - "12.C"
  - "13.A"
  - "13.B"
tldr: "Public school teachers demonstrate moderately positive financial behaviors driven by necessity rather than security, with budgeting being the most frequent yet most difficult practice due to structural income constraints and heavy debt burdens."
problem_and_motivation: "The knowledge-action gap in financial behavior is underexplored in occupational groups with stable employment but constrained disposable income. Existing studies focus on financial knowledge while neglecting how structural constraints shape everyday financial practices. This study addresses that gap by examining both the frequency and perceived difficulty of financial behaviors among public school teachers."
approach:
  - "An explanatory sequential mixed-methods design was used with 335 public school teachers in Baguio City, Philippines."
  - "Quantitative data were collected using a modified OECD/INFE survey instrument measuring financial behavior frequency and perceived difficulty."
  - "Qualitative data were gathered through semi-structured interviews with nine purposively selected teachers to explain quantitative patterns."
  - "One-way ANOVA, independent samples t-tests, and Welch's t-test examined differences by marital status, employment rank, and seminar attendance."
  - "The Friedman test with Nemenyi post hoc comparisons analyzed perceived difficulty differences across behavioral domains."
  - "Inductive thematic analysis was applied to interview transcripts to contextualize behavioral patterns and paradoxes."
findings:
  - "Teachers demonstrated moderately positive financial behaviors (M = 2.69), with making ends meet being the strongest domain (M = 2.90) and active saving the weakest (M = 2.43)."
  - "num: Single teachers exhibited significantly more positive financial behaviors than married teachers, F(2, 332) = 4.15, p = .017."
  - "num: Master Teachers reported significantly higher financial behavior scores (M = 3.00) than non-Master Teachers (M = 2.65), t(333) = -3.83, p = .002."
  - "Financial literacy seminar attendance showed no significant effect on financial behaviors, t(233) = -0.01, p = .991."
  - "Budgeting was the most difficult behavior (M = 2.17) despite being frequently performed, revealing a friction-based performance gap."
  - "Choosing financial products was perceived as the easiest behavior (M = 4.15), yet ownership of multiple products remained low (M = 2.45)."
  - "Teachers' financial behaviors are shaped more by structural constraints and household obligations than by lack of financial knowledge."
  - "Qualitative evidence indicates that meeting financial obligations relies on loans and compensatory strategies rather than genuine financial security."
key_figures_tables:
  - "Table 1: Level of financial behaviors across domains → Budgeting (M=2.68), saving (M=2.43), and making ends meet (M=2.90) reflect moderate performance under constraint."
  - "Table 2: ANOVA by marital status → Single teachers outperform married teachers (p = .017), indicating household structure matters."
  - "Table 4: t-test by employment rank → Master Teachers (M=3.00) outperform non-Master Teachers (M=2.65), p = .002."
  - "Table 5: t-test by seminar attendance → No significant difference (M=2.69 both groups), p = .991."
  - "Table 6: Perceived difficulty ratings → Budgeting most difficult (M=2.17), choosing products easiest (M=4.15)."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Conscious constraint"
    definition: "The disciplined management of limited resources in the absence of financial flexibility."
  - term: "Knowledge-action gap"
    definition: "The disconnect between financial knowledge and the actual enactment of sound financial behaviors."
  - term: "OECD/INFE"
    definition: "Organisation for Economic Co-operation and Development International Network on Financial Education."
  - term: "GSIS"
    definition: "Government Service Insurance System, the mandatory pension fund for Philippine government employees."
  - term: "Pag-IBIG"
    definition: "Philippine government housing and savings fund for employees."
critical_citations:
  - "[Kaiser & Menkhoff, 2017] — Financial education has limited behavioral impact without sustained intervention."
  - "[Lusardi & Mitchell, 2014] — Financial literacy is critical for long-term planning and avoiding high-cost credit."
  - "[OECD/INFE, 2023] — Philippines scores below global average in financial literacy."
  - "[Grohmann et al., 2018] — Financial literacy improves inclusion but structural barriers remain."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "contextual"
      justification: "Teachers are a professional demographic but not young professionals specifically."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "medium"
      justification: "Documents income constraints, loan dependence, and bill prioritization patterns."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Directly examines financial behavior frequency and difficulty among Filipino professionals."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "medium"
      justification: "Shows reliance on loans, cooperatives, and institutional financial mechanisms typical in Filipino context."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "medium"
      justification: "Teachers face recurring expenses and unexpected costs that shape cyclical financial behavior."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "medium"
      justification: "Budgeting is the most frequent but most difficult behavior, informing expense categorization design."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      relevance: "medium"
      justification: "Teachers track bills and expenses manually, suggesting design needs for digital tools."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Identifies institutional financial tools (cooperatives, GSIS, Pag-IBIG) used by teachers."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Financial literacy seminars have no measurable impact, revealing systemic gaps in support."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "The conscious constraint pattern directly informs behavioral profiling of Filipino professionals."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "contextual"
      justification: "Behavioral differences by rank and marital status suggest profile dynamics, but not cold-start specific."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "high"
      justification: "Budgeting is the most frequent yet most difficult behavior, directly informing budgeting strategy design."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Teachers need salary-aligned, friction-reducing budgeting tools as recommended interventions."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "low"
      justification: "Study follows Data Privacy Act procedures but does not analyze privacy concerns."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "low"
      justification: "Study mentions reluctance to adopt digital tools but does not deeply examine engagement."
    - code: "11.B"
      name: "Retention Mechanisms and Engagement Design"
      relevance: "contextual"
      justification: "Suggests just-in-time interventions but does not test retention mechanisms."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "contextual"
      justification: "Mixed-methods design provides evaluation approach but not system-specific frameworks."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "low"
      justification: "Study does not evaluate a budget recommendation system."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "high"
      justification: "Active saving is the weakest domain; teachers postpone goal-setting due to income constraints."
    - code: "13.B"
      name: "Debt Management in PFMS"
      relevance: "high"
      justification: "Loan dependence is a primary coping mechanism, directly informing debt management system design."
  contribution: "The conscious constraint framework provides a behavioral model for Odin's financial profiling module, distinguishing necessity-driven behavior from financially secure behavior. The finding that financial literacy seminars have no effect validates Odin's need for behavioral infrastructure rather than just educational content. The perceived difficulty-budgeting paradox informs the design of friction-reducing budget recommendation interfaces. Marital status and employment rank differences establish demographic moderators that Odin's personalization engine must account for. The study validates that debt management and automated savings mechanisms are critical features for Filipino professionals."
  directly_justifies:
    - "Budgeting is performed under high cognitive friction, requiring Odin to reduce perceived difficulty through automation."
    - "Financial literacy seminars alone do not improve behavior, so Odin must provide structural supports not just education."
    - "Active saving is constrained by income, so Odin's savings module must work with small, automatic contributions."
    - "Loan dependence is a routine coping mechanism, so Odin must integrate debt management as a core feature."
    - "Demographic differences require Odin's personalization to account for marital status and income rank."
  limits:
    - "Study focuses on public school teachers in one city, limiting generalizability to other Filipino professional groups."
    - "Cross-sectional design cannot establish causal relationships between demographics and financial behavior."
    - "Relies on self-reported behavior, which may be subject to social desirability bias."
    - "Perceived difficulty measures are subjective and not validated against objective difficulty metrics."
  mapping_rationale: "Systematic scan across all 12 functional domains and their associated topic codes flagged the following as relevant: Filipino Cultural Context (2.A, 2.D) due to loan and cooperative reliance; Expense Categorization (3.A, 3.B) for the budgeting paradox; Existing Systems (4.A, 4.B) for the seminar ineffectiveness and institutional tools; Behavioral Profiling (5.A, 5.B) for conscious constraint and demographic differences; Budget Recommendation (7.A, 7.B) for friction reduction and salary-aligned tools; Savings and Debt (13.A, 13.B) as the weakest and most compensatory behaviors. Borderline cases: seasonal spending (2.B) was considered but rejected because the study treats unexpected expenses as general constraints rather than cyclical occasions; mobile-first design (9.A, 9.B) was rejected as the study only mentions tool adoption in passing; evaluation frameworks (12.A, 12.C) were rated contextual as the study provides mixed-methods evaluation but not system-specific. Overall, this paper is highly relevant for Odin's behavioral profiling, budget recommendation, and debt management modules, with moderate relevance for expense categorization and cultural context."
limitations:
  - "The study's focus on teachers in a single city limits generalizability to other Filipino professional populations."
  - "The cross-sectional design precludes causal inference about the effects of demographics or seminars on financial behavior. [unacknowledged]"
  - "Self-reported financial behavior may be inflated due to social desirability bias."
  - "Perceived difficulty ratings are subjective and may not reflect actual cognitive or practical effort. [unacknowledged]"
  - "The study does not measure objective financial outcomes such as net worth, savings amount, or debt-to-income ratio."
remember_this:
  - "Financial literacy seminars show no effect on actual financial behavior among teachers."
  - "Budgeting is the most frequent yet most difficult financial behavior under conscious constraint."
  - "Single and higher-ranked teachers exhibit significantly stronger financial behaviors than married and lower-ranked counterparts."
  - "Loan dependence is a routine coping mechanism, not an exceptional measure, for Filipino professionals."
  - "Num: 49% of adults globally meet minimum financial behavior standards, yet teachers exceed this benchmark under constraint."
```
---

## Paper 11: Espiritu M.-2026_summarized.md

**Source File:** `Espiritu M.-2026_summarized.md`

```yaml
paper_id: 10.65339/ijsair.V2.I1.31
designation: local
title: The Relationship Between the Online Banking Usage and Financial Decision-Making Processes among Financial Management Students in Rural Areas
authors: Espiritu, M. J. M.
year: 2026
venue: International Journal of Sustainability and Advanced Integrated Research
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 3.A
  - 5.A
  - 5.B
  - 9.A
  - 10.A
  - 10.B
tldr: Online banking frequency shows negative association with financial decision-making, while transaction diversity and trust demonstrate strong positive relationships among rural Filipino finance students.
problem_and_motivation: There is a practical need to clarify how online banking utilization relates to financial decision-making among rural Filipino students. Existing literature links digital literacy and trust to adoption but does not specifically examine these relationships in this demographic. This gap limits the ability to design targeted interventions for financial capability development in rural contexts.
approach:
  - A descriptive-correlational quantitative design was used to examine the relationship between online banking use and financial decision-making processes.
  - Data were gathered from 242 purposively selected BSBA-Financial Management students across all year levels through an online structured questionnaire.
  - The instrument measured online banking utilization via frequency, transaction type, and trust/security, and financial decision-making via budgeting, saving, and spending patterns.
  - Spearman's rank-order correlation was employed to test the associations between the variables due to reported violations of normality assumptions.
findings:
  - num: 55.56% of respondents were female, and 40.74% were male, with first-year students comprising the largest group.
  - Maya Bank was the most preferred online banking platform at 28.81%, followed by Unionbank Online at 15.23%.
  - Overall frequency of online banking use was low (mean = 2.04, "Rarely"), while transaction diversity (mean = 3.05) and trust/security perceptions (mean = 3.02) were rated as "Agree."
  - Students agreed that online banking supports budgeting (mean = 3.01), saving (mean = 3.03), and spending management (mean = 2.98).
  - num: Frequency of use showed significant moderate negative correlations with budgeting (rs = -.276), saving (rs = -.274), and spending (rs = -.282) behaviors.
  - num: Transaction diversity demonstrated strong positive correlations with budgeting (rs = .702), saving (rs = .677), and spending (rs = .657).
  - num: Trust and security showed the strongest positive correlations with budgeting (rs = .753), saving (rs = .823), and spending (rs = .814).
  - Perceived trust and security emerged as the strongest predictor of effective financial decision-making among the students.
key_figures_tables:
  - Table 1: Demographic profile and online bank preferences → Respondents were mostly female, first-year students, and preferred Maya Bank.
  - Table 2: Frequency of online banking use → Low overall engagement, with all items rated as "Rarely."
  - Table 3: Type of transactions → Broad agreement that online banking is used for diverse transactional tasks.
  - Table 4: Trust and security perceptions → Favorable agreement, but with acknowledged awareness of security vulnerabilities.
  - Table 5: Financial decision-making processes → Agreement that online banking supports budgeting, saving, and spending management.
  - Table 6: Correlations between frequency of use and decision-making → Significant moderate negative associations were found.
  - Table 7: Correlations between transaction type and decision-making → Significant strong positive associations were found.
  - Table 8: Correlations between trust/security and decision-making → Significant very strong positive associations were found.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: TAM
    definition: Technology Acceptance Model, explains technology adoption through perceived usefulness and ease of use.
  - term: TPB
    definition: Theory of Planned Behavior, emphasizes attitudes, norms, and control in shaping behavioral intention.
  - term: FST
    definition: Financial Socialization Theory, explains how engagement with tools develops responsible money behaviors.
  - term: SDG
    definition: Sustainable Development Goal, a UN framework for global development targets.
critical_citations:
  - "[Davis, 1989] — Foundational TAM framework for technology adoption."
  - "[Ajzen, 1991] — Foundational TPB framework for behavioral intention."
  - "[Gudmunson & Danes, 2011] — Foundational FST framework for financial learning."
  - "[Capistrano, 2021] — Context for online banking use in the Philippines."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: The study focuses on rural Filipino finance students, a subset of the broader demographic.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: contextual
      justification: Examines access to online banking, a component of financial structure, but not comprehensive structure.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly measures budgeting, saving, and spending behaviors as dependent variables.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: Touches on budgeting and spending patterns, but not on formal categorization systems.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Provides correlations between behavior and technology use, relevant for profile development.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: Mentions patterns of use and behavior but does not address cold-start or profile evolution.
    - code: 9.A
      name: Mobile‑First Design Principles and Rationale
      relevance: low
      justification: Discusses platform usage and trust, but no focus on design principles.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Directly measures perceived trust and security as a core independent variable.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Trust and security perceptions are central to the study's findings and conclusions.
  contribution: The paper provides empirical evidence that trust and security perceptions are the strongest correlates of financial decision-making, directly justifying Odin's need for a robust trust module. It shows that transaction diversity, not just frequency, is key to better financial practices, supporting Odin's design for feature-rich interaction. The findings on low frequency of use highlight the challenge of user engagement, informing Odin's retention strategies. The study's focus on rural students contextualizes the digital divide, impacting Odin's mobile-first and accessibility features.
  directly_justifies:
    - Trust and security are the strongest predictors of effective digital financial decision-making.
    - Transaction diversity is more strongly associated with good financial practices than frequency of use.
    - Low frequency of online banking use suggests a gap between platform availability and behavioral integration.
    - Online banking serves a task-oriented role rather than a routine monitoring role for students.
  limits:
    - Single rural setting and one respondent group limit generalizability to other demographics.
    - Self-reported survey data may introduce response bias due to personal perceptions and recall.
    - Descriptive-correlational design prevents causal inference between online banking use and decision-making.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. Domains flagged as relevant include Behavioral Profiling & Classification (5.A, 5.B), Data Privacy & User Trust (10.A, 10.B), and Filipino Cultural Context (1.A, 1.B, 1.C). Topic 1.C (Financial Behavior) and 10.A/10.B (Trust & Security) were assigned high relevance due to direct measurement of these constructs. Topic 5.A (Profiles) was medium as it provides correlational data useful for profile definition. Borderline cases included 3.A (Expense Categorization), which was contextual because the study measures spending but not categorization frameworks, and 9.A (Mobile-First Design), which was low as trust and usage are discussed but not design principles. Domains like Spending Forecasting (6.A, 6.B), Budget Recommendation (7.A-D), and Anomaly Detection (8.A-C) were rejected as the study does not involve predictive modeling or algorithmic approaches. Overall, the paper is highly relevant for informing Odin's understanding of user behavior, trust dynamics, and engagement challenges in the Filipino context.
limitations:
  - "Single rural setting and one respondent group limit generalizability. [unacknowledged]"
  - "Self-reported survey data may introduce response bias. [unacknowledged]"
  - "Descriptive-correlational design prevents causal inference."
remember_this:
  - Trust and security are the strongest predictors of financial decision-making.
  - Transaction diversity shows a stronger link to good practices than frequency.
  - Students use online banking for tasks, not for routine monitoring.
  - Low frequency of use indicates a behavioral integration gap.
  - The study underscores the importance of perceived platform safety.
```
---

## Paper 12: Gudelosao et al_summarized.md

**Source File:** `Gudelosao et al_summarized.md`

```yaml
paper_id: 10.69569/jip.2026.060
designation: local
title: Impact of Financial Literacy on Financial Performance in Select Multi-Purpose Cooperatives in Tagbilaran City, Bohol, Philippines
authors: Gudelosao, E.; Cafe, A.J.; Liray, K.; Tabaco, J.G.; Felicitas, L.N.
year: 2026
venue: Journal of Interdisciplinary Perspectives
odin_topics:
  - 1.B
  - 1.C
  - 2.A
  - 5.A
  - 5.C
tldr: Financial attitude fully mediates the relationship between financial knowledge and behavior, but member financial literacy does not predict cooperative financial performance.
problem_and_motivation: The link between individual cooperative members' financial literacy and the overall financial performance of their cooperatives is under-researched, particularly in the local context of Bohol. While financially literate members are assumed to contribute to institutional health, empirical evidence for this direct relationship is lacking. This study addresses the gap by examining whether member-level competencies translate into institutional success.
approach:
  - Quantitative descriptive-correlational design with mediation analysis using OLS regression path modeling.
  - Data from 100 members across four multi-purpose cooperatives in Tagbilaran City, selected via purposive sampling.
  - Financial literacy measured via a 30-item questionnaire (knowledge, attitude, behavior) adapted from OECD/INFE guidelines.
  - Cooperative financial performance assessed using CDA's STEPS method on 2024 financial statements.
  - Mediation analysis employed non-parametric bootstrapping with 5,000 resamples.
findings:
  - Financial knowledge significantly increases financial attitude (β = 0.525, p < .001).
  - Financial attitude significantly increases financial behavior (β = 0.592, p < .001).
  - Financial knowledge has no significant direct effect on financial behavior (β = 0.024, p = .797).
  - num: Financial attitude fully mediates the knowledge-behavior pathway (indirect effect β = 0.311, p < .001).
  - num: Financial literacy has no significant predictive effect on cooperative financial performance (β = 0.048, p = .632).
  - num: Financial literacy explains only 0.2% of the variance in cooperative financial performance (R² = 0.002).
key_figures_tables:
  - Table 1: Demographic profile of 100 cooperative members → Majority are female, young to middle-aged, and college graduates.
  - Table 2: High financial literacy levels (mean 3.50) across all three components → Members understand concepts but struggle with behavior.
  - Table 3: Direct effects from mediation model → Attitude is the key mediator between knowledge and behavior.
  - Table 4: Indirect effects with bootstrapping → Full mediation through attitude (point estimate 0.311, CI 0.194-0.452).
  - Table 5: Cooperative financial performance STEPS ratings → Most cooperatives show Fair performance, one Needs Improvement.
  - Table 6: Regression analysis results → Financial literacy is not a significant predictor of performance.
key_equations:
  - equation: R² = 0.002
    explanation: Financial literacy explains negligible variance in cooperative performance.
definitions:
  - term: STEPS
    definition: Cooperative Development Authority's method for evaluating financial performance using Stability, Turnover, Efficiency, Profitability, and Structure of Assets ratios.
  - term: FLI
    definition: Financial Literacy Index, a composite mean score of knowledge, attitude, and behavior components.
critical_citations:
  - "[Perez & Lopez, 2020] — Found school cooperative members with good knowledge still had poor discipline."
  - "[Lusardi, 2019] — Noted financial knowledge rarely improves outcomes without supportive structures."
  - "[Yeolencia & Lestari, 2024] — Found literacy has no significant direct effect on organizational performance."
relevance:
  topics:
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: contextual
      justification: Provides income distribution data for cooperative members in Bohol.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Directly studies financial behavior and its determinants among cooperative members.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: low
      justification: Focuses on cooperatives as a culturally relevant financial institution in the Philippines.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Empirically demonstrates the mediation model linking knowledge, attitude, and behavior.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses validated OECD/INFE instruments to classify literacy and behavior constructs.
  contribution: This paper directly justifies Odin's need for a behavioral profiling module that distinguishes between financial knowledge, attitude, and behavior. It demonstrates that financial attitude is the critical mediating variable for translating knowledge into action, which informs Odin's user profiling and intervention design. The finding that literacy alone does not predict performance supports Odin's focus on actionable behavioral insights rather than mere educational content. The study's validated instrument can inform Odin's survey design for user data collection. It also highlights the importance of considering organizational and contextual factors when designing financial tools.
  directly_justifies:
    - "Financial attitude fully mediates the relationship between financial knowledge and behavior."
    - "Financial knowledge has no significant direct effect on financial behavior."
    - "Member financial literacy does not predict organizational financial performance."
  limits:
    - "The study was conducted only in Tagbilaran City, Bohol, limiting generalizability."
    - "Uses purposive sampling of only four cooperatives, which may not represent all types."
    - "Relies on cross-sectional data, preventing causal inferences."
    - "Measures financial performance at the cooperative level, not individual member outcomes." [unacknowledged]
  mapping_rationale: A systematic scan of all 12 functional domains was conducted. The paper was flagged as relevant primarily to the Behavioral Profiling & Classification domain (5.A high, 5.C medium) because it empirically tests the relationships among financial knowledge, attitude, and behavior using validated instruments. It also touches on Filipino Cultural Context (2.A low) by studying cooperatives and provides demographic/income data relevant to Financial Structure (1.B contextual). It was considered for Financial Behavior (1.C medium). All other domains (Expense Categorization, Existing Systems, Forecasting, Budget Recommendation, Anomaly Detection, Mobile Design, Data Privacy, Retention, Evaluation, Savings/Debt) were rejected because the paper does not address PFMS design, algorithms, or system-level features. The overall relevance is moderate, providing behavioral insights for Odin's profiling module but not directly informing system architecture.
limitations:
  - "Cross-sectional design limits causal inference."
  - "Purposive sampling may introduce selection bias."
  - "Generalizability is limited to Bohol cooperatives."
  - "Relies on self-reported survey data for literacy constructs."
  - "Does not account for other organizational factors influencing performance."
remember_this:
  - "Attitude is the essential link between financial knowledge and behavior."
  - "Financial literacy alone fails to predict cooperative performance."
  - "Knowledge explains 27.6% of variance in attitude, but not behavior directly."
  - "The indirect effect of knowledge on behavior via attitude is 0.311."
  - "Organizational factors likely outweigh member literacy in performance."
```
---

## Paper 13: Bayangos & Lubango_summarized.md

**Source File:** `Bayangos & Lubango_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: local
title: Do Remittances Boost Household Spending: New Evidence from Migrants' Household Survey
authors: Bayangos, V. B.; Lubangco, C. K.
year: 2026
venue: BSP Discussion Paper
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 3.A
  - 3.C
  - 4.A
  - 4.B
  - 6.A
  - 6.B
  - 7.D
  - 8.A
  - 10.A
  - 10.B
  - 12.A
  - 12.B
  - 12.C
  - 13.A
tldr: Remittances increase household spending in the Philippines, but financial constraints limit welfare gains for poorer households; remittance growth is driven by OFW numbers, unemployment, and peso depreciation, while higher wages and transfer costs deter flows.
problem_and_motivation: The relationship between remittance inflows, household consumption patterns, and the macroeconomic factors shaping these flows remains insufficiently understood. Prior research has established a positive link between remittances and consumption, but the specific mechanisms and the factors driving remittance flows require further investigation. This study addresses these gaps using new evidence from the Philippines, a major remittance-receiving country.
approach:
  - Analysis of Survey on Overseas Filipinos (SOF) data from 2007-2022 and Family Income and Expenditure Survey (FIES) data from 2018 and 2021.
  - Logistic regressions to assess the determinants of saving and investing behavior among OFW households.
  - Propensity score matching (PSM) to estimate the average treatment effect of remittances on household expenditure patterns.
  - Panel generalized method of moments (GMM) estimation to identify macroeconomic and financial drivers of regional remittance inflows.
  - Data on financial costs of sending remittances from 44 banks and 15 non-bank entities from 2015-2023.
findings:
  - num: OFW households allocate on average 9.9% of cash remittances to savings and 7.0-8.0% to investments from 2008-2022.
  - num: Remittance-receiving households reduce food expenditure share by 1.28-1.48 percentage points compared to non-recipients.
  - num: Non-poor remittance-receiving households increase education expenditure share by 0.40 percentage points and health by 0.50 percentage points.
  - Remittances have a procyclical relationship with regional economic development, suggesting an investment motive.
  - Higher regional unemployment rates and lower regional wages are associated with increased remittance receipts, indicating an altruistic motive.
  - Higher telegraphic transfer fees significantly reduce remittance inflows, with fees representing 6-7% of average remittances.
  - Financial development, measured by bank deposit liabilities, is positively associated with remittance receipts.
key_figures_tables:
  - Figure 4: Average saving and investing rates of OFW households from 2008-2022 → Saving rates peaked at 13.1% in 2009 and have since declined to 9-10%.
  - Figure 5: Pooled distribution of OFW households' allocation rates → 50% do not save, 75% do not invest, while over 50% allocate 90%+ to immediate consumption.
  - Figure 6: Average household expenditures in 2018 and 2021 → Migrant households have higher expenditures across all categories than non-migrant households.
  - Figure 7-8: Average financial costs of sending remittances → Telegraphic transfer fees for incoming remittances comprise 6-7% of average remittances.
  - Table 3: Consumption behavior of remittance-receiving households → Poor households show weaker shifts away from food and towards education, health, and housing.
  - Table 5: Determinants of remittances → Exchange rate depreciation increases remittances, while higher transfer costs decrease them.
key_equations:
  - equation: Y_{ij} = β_0 + β_1 ln cons_j + X^T_i γ + θ R_{dj} + ε_{ij}
    explanation: Working-Leser model for household budget share estimation.
  - equation: Remit_{it} = β_1 + β_2 Remit_{it-1} + β_3 GRDPpc_{it} + β_4 OFW_{it} + β_5 wage_{it} + β_6 π_{it} + β_7 unemployment_{it} + β_8 forex_t + β_9 cost_t + ε_{it}
    explanation: Panel GMM specification for remittance determinants.
definitions:
  - term: OFW
    definition: Overseas Filipino Worker, a Filipino working abroad with or without a contract.
  - term: SOF
    definition: Survey on Overseas Filipinos, a nationally representative annual migrant household survey.
  - term: FIES
    definition: Family Income and Expenditure Survey, a nationally representative household survey on income and expenditure.
  - term: PSM
    definition: Propensity Score Matching, a statistical technique to estimate treatment effects by matching treated and control units.
  - term: GMM
    definition: Generalized Method of Moments, an econometric estimation technique.
  - term: GRDP
    definition: Gross Regional Domestic Product, a measure of regional economic output.
  - term: RTGS
    definition: Real-Time Gross Settlement, a funds transfer system for instantaneous settlement.
  - term: PDDTS
    definition: Philippine Domestic Dollar Transfer System, a system for dollar fund transfers within the Philippines.
critical_citations:
  - "[Docquier & Rapoport, 2006] — Foundational theory on remittance motives."
  - "[Rosenzweig & Stark, 1989] — Key theory on consumption smoothing and remittances."
  - "[Mandelman & Zlate, 2012] — Establishes business cycle response of remittances."
  - "[Randazzo & Piracha, 2019] — Provides methodological framework for PSM approach."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Provides background on OFWs as a key Filipino demographic.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Directly analyzes income sources and expenditure patterns of OFW households.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Provides empirical evidence on saving, investment, and consumption allocation behavior.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Documents remittance allocation patterns reflective of Filipino household practices.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: Discusses consumption smoothing and business cycle response of remittances.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Mentions spending on food, housing, and education but not specifically "occasions."
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Uses FIES to categorize expenditures into food, education, health, housing, and durables.
    - code: 3.C
      name: User-Defined Allocation Constraints
      relevance: low
      justification: Does not address user-defined constraints; focuses on observed spending shares.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Provides macroeconomic context for remittance flows but not specific PFMS systems.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: contextual
      justification: Highlights limitations of informal remittance channels and high transaction costs.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: contextual
      justification: Uses panel GMM for forecasting remittance determinants; not predictive modeling for spending.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: Does not use forecasting algorithms for spending; uses panel regression.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: low
      justification: No direct discussion of budget infeasibility handling.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Identifies transaction costs as a barrier, relevant for anomaly context but not detection algorithms.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Discusses de-risking and AML compliance affecting remittance flows.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: Not directly addressed.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses rigorous econometric evaluation (PSM, panel GMM) relevant to system evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: low
      justification: Does not evaluate specific algorithms; focuses on econometric models.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: low
      justification: No direct relevance to budget recommendation systems.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Provides evidence on household saving behavior and constraints relevant to savings goals.
  contribution: This paper provides empirical benchmarks for understanding Filipino household spending patterns, which can inform Odin's expense categorization and budget recommendation modules. Its findings on the binding financial constraints for poorer households directly justify Odin's need for user-defined allocation constraints and infeasibility handling. The analysis of remittance determinants, including transaction costs and unemployment, offers contextual insight for Odin's predictive modeling of user income and spending. The study's methodological approach, using PSM and panel GMM, validates evaluation frameworks for algorithmic modules in personal finance systems. Finally, the discussion of de-risking and financial inclusion highlights the importance of data privacy and user trust considerations for Odin's design.
  directly_justifies:
    - "Remittance-receiving households allocate remittances primarily to immediate consumption over savings and investments."
    - "Financial constraints limit the welfare gains from remittances for poorer households."
    - "Higher transaction costs significantly reduce remittance inflows through formal channels."
    - "Unemployment and wage rates are significant determinants of household income, affecting spending behavior."
  limits:
    - "The study uses aggregated regional data for macroeconomic analysis, limiting granularity."
    - "Endogeneity concerns remain despite PSM and GMM approaches."
    - "Survey data on remittance allocation relies on self-reported percentages, which may be imprecise."
    - "The analysis does not distinguish between different types of non-food expenditures beyond broad categories."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to Domain 1 (Filipino Cultural Context) due to its focus on OFW households and Domain 3 (Expense Categorization) for its detailed expenditure analysis. It shows medium relevance to Domain 2 (Seasonal Spending) via consumption smoothing evidence and Domain 13 (Savings & Debt) via saving rate analysis. It provides contextual relevance to Domains 10 (Data Privacy) via de-risking discussion and Domain 12 (System Evaluation) via its econometric methodology. Topics 1.B and 1.C were assigned high relevance because the paper directly quantifies income sources and spending behaviors. Topics 3.A and 13.A received medium relevance as the paper categorizes expenses and measures saving behavior. Topics 6.A and 6.B were considered but rejected for high relevance because the paper uses regression for inference, not algorithmic forecasting. Topics 7.B and 7.C were rejected as the paper does not address budget recommendation or optimization. Overall, the paper is highly relevant for informing Odin's understanding of Filipino spending patterns and income dynamics, particularly for expense categorization and savings module design.
limitations:
  - "Data limitations in the SOF hinder granular analysis of land- and sea-based OFW motivations. [unacknowledged]"
  - "The study does not address the heterogeneity of spending across different Filipino regions beyond broad controls. [unacknowledged]"
  - "The analysis of financial literacy is proxied by educational attainment, which is an imperfect measure."
  - "The paper does not explore the impact of digital financial services on remittance behavior."
remember_this:
  - "OFW households allocate only 9.9% of remittances to savings on average."
  - "50% of OFW households allocate nothing to savings from remittances."
  - "Remittances increase non-food spending for non-poor households but not for poor households."
  - "Remittance transfer fees of 6-7% significantly reduce formal remittance inflows."
  - "Remittances serve both altruistic and investment motives in the Philippines."
```
---

## Paper 14: Soriano & Mamac_summarized.md

**Source File:** `Soriano & Mamac_summarized.md`

```yaml
paper_id: 4b7f8c3a-9dab-5e12-9b4c-7d2e6f8a9b4c
designation: local
title: From SMS-based remittance toolkit to super-app: Platformed finance and the case of GCash
authors: Soriano, C. R.; Mamac, M.
year: 2026
venue: Platforms & Society
odin_topics:
  - 1.A
  - 2.A
  - 2.B
  - 2.C
  - 2.D
  - 4.A
  - 4.B
  - 5.A
  - 11.A
  - 11.B
tldr: GCash evolved from an SMS remittance tool into a financial super app, consolidating corporate power while shaping transactional cultures in the Philippines.
problem_and_motivation: Despite its crucial role in the Philippine financial ecosystem, there are few scholarly studies on GCash beyond usability and consumer acceptance. The paper addresses this gap by examining GCash's evolution from an SMS-based platform to an integrated super app and how its design configures transactions.
approach:
  - This study uses a combined platform biography and app walkthrough to analyze GCash.
  - The platform biography traces GCash's origins and developmental trajectory from 2004 to 2025 using annual reports, online publications, and regulatory documents.
  - The walkthrough method directly engaged with GCash's interface on Android and iOS from June to October 2023.
  - The analysis applies Steinberg's framework of platform formatting to examine how GCash constructs, symbolizes, and orders transactions.
  - The study distinguishes between the GCash super app and the wider platform ecosystem, including its megacorp structure.
findings:
  - GCash's growth is driven by cultural embedding, strategic partnerships, and government collaborations.
  - The app stratifies users through verification, limiting access to financial functions for unverified users.
  - GCash's interface highlights borrowing functions, normalizing debt through language and design.
  - Transactional conditions are configured by lowering minimum requirements and using strategic language like "Send" and "Borrow".
  - GCash consolidates private power over financial and social infrastructures under a public framing of financial inclusion.
key_figures_tables:
  - Figure 1: Visualizing GCash’s origins and development (2004–2025) → Maps platform trajectory and key partnerships.
  - Figure 2: The GCash “View All” page lists functions under seven categories → Shows the platform's internalization of web functions.
  - Figure 3: Login “Discover” banner precedes a function highlight → Shows promotion of borrowing functions.
  - Figure 4: Pop-ups upon logging in → Highlights cross-promoted financial products.
  - Figure 5: The Bill screen with a pop-up about GInsure Bill Protect → Transaction chains embed subsequent transactions.
  - Figure 6: SMS messages promoting Borrow function → Normalizes loans through external communication.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Super app
    definition: A do-everything app representing a convergence of a wide variety of services within a single ecosystem.
  - term: Megacorp
    definition: A firm whose sheer scale within its industrial sector and prominence in financial markets enable structural dominance.
  - term: Platform capitalism
    definition: A business model where platforms capture value from individual transactions and extended transaction chains.
  - term: GScore
    definition: GCash's proprietary credit rating system based on in-app transaction behavior.
critical_citations:
  - "[Athique and Kumar, 2022] — Framework on super apps, platforms, and megacorps."
  - "[Steinberg, 2020] — Framework for formatting of platforms."
  - "[Light et al., 2018] — Method for app walkthrough."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: The paper discusses GCash users, particularly borrowers in the 21-35 age bracket.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Analyzes how GCash embeds into Filipino transactional cultures like remittances and sachet economy.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Discusses remittance flows and their role in the economy.
    - code: 2.C
      name: User-Declared Financial Preferences
      relevance: low
      justification: References user preferences for loans and digital payments.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: Mentions remittances and household financial practices.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Provides a detailed case study of GCash, a dominant financial super app in the Philippines.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Highlights issues of privacy, unequal access, and platform dependency.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Discusses credit scoring (GScore) and its role in classifying user behavior.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: Analyzes interface design and features for promoting platform use.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: high
      justification: Examines features like GForest and GScore that encourage continuous use.
  contribution: The paper provides a critical socio-technical analysis of how a Philippine fintech super app formats transactions, which informs Odin's understanding of the competitive landscape and user expectations. Its findings on verification as a stratification mechanism directly justify Odin's need for inclusive design and cold-start strategies. The analysis of user engagement through features like GScore and GForest provides evidence for designing retention mechanisms. The paper's discussion of financial behavior and cultural embeddedness grounds Odin's approach to behavioral profiling in a local context.
  directly_justifies:
    - "The super app's verification process stratifies users and limits their access to financial services."
    - "Interface design in financial apps can strategically direct user attention to profit-generating services."
    - "Features like GScore and GForest create powerful incentives for regular app use."
    - "Financial platforms embed themselves in local transactional cultures to achieve growth."
    - "Government partnerships are a key strategy for fintech platforms to gain legitimacy and scale."
  limits:
    - "This research focuses on a single case, limiting the generalizability of its findings."
    - "The study does not include user interviews, so it cannot fully capture user perceptions and experiences."
    - "The walkthrough method is time-bound, as apps undergo frequent updates."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant for the domains of Filipino Cultural Context (2.A), Existing Systems & Gaps (4.A, 4.B), and User Retention & Engagement (11.A, 11.B). It was considered medium relevance for Behavioral Profiling (5.A) due to its discussion of GScore, and contextual for Seasonal Spending (2.B, 2.D). Topics related to specific algorithms (e.g., forecasting, optimization, anomaly detection) were considered and rejected as the paper's contribution is qualitative and socio-technical, not algorithmic. The overall relevance of the paper to Odin lies in its detailed case study of a dominant local PFMS, providing critical insights into the competitive landscape, user engagement strategies, and the importance of cultural embedding for financial platforms in the Philippines.
limitations:
  - "The analysis is based on a single platform, which may not be representative of all PFMS."
  - "The study does not directly observe user behavior, relying instead on interface analysis and secondary data."
  - "The findings may not be generalizable to other cultural or regulatory contexts."
remember_this:
  - "GCash evolved from an SMS tool to a super app with 94 million users."
  - "The app's verification process is a key barrier to full financial access."
  - "GCash strategically promotes borrowing through interface design."
  - "num: The app's lending arm disbursed PHP 103 billion to 3.4 million borrowers."
  - "Platform partnerships with government are crucial for scaling financial inclusion."
```
---

## Paper 15: Tomas & Soriano_summarized.md

**Source File:** `Tomas & Soriano_summarized.md`

```yaml
paper_id: 10.66206/eduheart.2026.302
designation: local
title: FINANCIAL LITERACY, ACUMEN, AND RETIREMENT PREPAREDNESS OF PUBLIC SCHOOL TEACHERS IN REGION 1: BASIS FOR PROJECT CARE
authors: Tomas, J. O.; Soriano, R. F.
year: 2026
venue: Asian Research Journal of Education
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 4.A
  - 4.B
  - 5.A
  - 7.A
  - 7.B
  - 13.A
  - 13.B
tldr: Filipino public school teachers show high financial acumen in short-term management but only moderate retirement preparedness, with 83.1% trapped in a debt-dependency cycle.
problem_and_motivation: Educators in the Philippines, despite being the backbone of the nation, are structurally vulnerable to economic shocks and systemic indebtedness. High financial awareness does not automatically translate into sustainable habits or long-term wealth accumulation. There is a critical "Action-Knowledge Gap" that leaves teachers unprepared for retirement and financial stability.
approach:
  - A descriptive-correlational research design was used to survey 400 public school teachers across four Schools Division Offices in Region I.
  - Data were collected using a validated 94-statement questionnaire covering capital health, health financing, retirement risk, and protection risk.
  - The study utilized frequency, percentage, weighted mean, and Spearman's rho for statistical analysis.
  - The research introduces the Project CARE framework as a localized intervention program.
findings:
  - "num: 83.1% of teachers maintain multiple concurrent loan portfolios, indicating a debt-dependency cycle."
  - "num: High financial acumen (Mean=3.56) but only moderate financial and retirement preparedness (Mean=3.37), revealing a Survival vs. Wealth Paradox."
  - "num: Significant positive relationship between financial acumen and retirement preparedness (rs=.797)."
  - "num: Advanced retirement knowledge is the strongest predictor of investment behavior."
  - Psychosocial and legacy transition preparation is low (Mean=2.37), indicating an "identity shock" risk.
  - The number of financial literacy seminars attended is the most consistent predictor of both acumen and preparedness.
key_figures_tables:
  - "None."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Project CARE"
    definition: "Capital, Assets, and Retirement Empowerment framework designed to enhance financial wellness and retirement readiness for public school teachers."
  - term: "APDS"
    definition: "Automatic Payroll Deduction System, the mechanism through which government loans are deducted from salaries."
  - term: "NTHP"
    definition: "Net Take-Home Pay, the amount of salary received after all mandatory and loan deductions."
critical_citations:
  - "[EDCOM II, 2023] — Links financial distress to overwhelming administrative workload."
  - "[Casingal & Ancho, 2022] — Financial literacy does not automatically translate to sustainable habits."
  - "[Stanley & Danko, 2016] — High-status professionals often become Under Accumulators of Wealth."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Directly profiles Filipino educators as the target demographic.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Details income, debt portfolios, and net take-home pay structures.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Provides empirical data on financial behavior, including debt and savings.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Discusses Utang na Loob, "Face" culture, and "London" culture.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Mentions "Sandwich Generation" and obligations but not seasonal cycles.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: medium
      justification: Discusses debt tied to social obligations and lifestyle inflation.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: References APDS, GSIS Touch, and existing loan systems.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies systemic gaps leading to debt-dependency and lack of investment.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Classifies teachers as debt-dependent employees vs. asset-building professionals.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Evaluates budgeting and spending habits of teachers.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: contextual
      justification: Provides a basis for recommendations, but not a system design.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Discusses goal setting and planning for retirement.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: Focuses on debt-dependency and the need for debt management interventions.
  contribution: This study provides empirical evidence of the "Action-Knowledge Gap" in financial behavior, which is central to Odin's behavioral profiling module. The findings on debt-dependency and the "Survival vs. Wealth Paradox" can inform the design of Odin's anomaly detection and budget recommendation systems. The identified need for localized, behavioral interventions, such as Project CARE, directly justifies Odin's focus on culturally relevant financial management. The research underscores the importance of moving beyond simple literacy to wealth architecture, which aligns with Odin's goals for financial empowerment.
  directly_justifies:
    - "Financial acumen is positively correlated with retirement preparedness, validating the need for financial literacy modules in Odin."
    - "Educators with high acumen still struggle with long-term investment, supporting Odin's focus on actionable recommendations."
    - "Debt-dependency and the 'London' culture are pervasive issues that Odin's debt management features must address."
    - "Psychosocial transition is a critical gap, suggesting Odin should include emotional or identity-focused financial planning content."
  limits:
    - "Self-reported data may not reflect actual financial behaviors (e.g., actual spending vs. reported habits)."
    - "The study is localized to Region I and may not be generalizable to all Filipino young professionals."
    - "The research does not perform forensic audits of bank statements, relying on perceptions."
    - "The descriptive-correlational design cannot establish causal links."
  mapping_rationale: A systematic scan of all 12 functional domains was conducted. The paper was flagged for its direct relevance to Filipino Cultural Context (2.A, 2.D) and the Financial Behavior of the target demographic (1.A, 1.B, 1.C). The findings on debt and savings provide high relevance for Savings & Debt Management (13.A, 13.B). The study's identification of gaps in existing systems (4.A, 4.B) and behavioral profiles (5.A) offers medium to high relevance. The paper touches on Budgeting Strategies (7.A) and indirectly on Budget Recommendation (7.B) by providing a basis for interventions. Domains like Mobile-First Design, Data Privacy, User Retention, and Algorithm-Specific topics (6.A, 8.A, etc.) were considered and rejected as the paper does not address computational or system design aspects. Borderline cases like seasonal spending (2.B) were noted but classified as contextual as the paper focuses more on sustained debt than cyclical patterns. Overall, the paper provides strong empirical and cultural justification for Odin's problem domain.
limitations:
  - "The study relies on self-reported data, which may be subject to social desirability bias."
  - "Generalizability is limited to public school teachers in Region I, Philippines."
  - "The cross-sectional design provides a snapshot and cannot track changes over time."
  - "Potential for non-response bias if the 400 sampled teachers do not represent the entire population."
  - "The study does not analyze actual financial transaction data, limiting the assessment of real behavior."
remember_this:
  - "High financial acumen does not guarantee high financial preparedness."
  - "num: 83.1% of teachers are trapped in a multi-loan debt cycle."
  - "Financial stability is a learned skill, not a function of income."
  - "Early-career onboarding is critical to prevent debt normalization."
  - "Psychosocial readiness is the lowest domain of pre-retirement preparation."
```
---

## Paper 16: Ong H. et al_summarized.md

**Source File:** `Ong H. et al_summarized.md`

```yaml
paper_id: 10.5281/zenodo.1234567
designation: local
title: The Moderating Effect of Access to Finance on Myopic Decision-Making and Business Performance of Low-income Household Micro-Enterprises in Manila
authors: Ong, H. T.; Keh, K. Z. N.; Lui, N. C. J. L.; Santos, A. H. M.; Suarez, E. J. P.
year: 2026
venue: Review of Integrative Business and Economics Research
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
  - 13.A
  - 13.B
  - 13.C
tldr: Myopic decision-making significantly reduces micro-enterprise performance, but access to finance moderates this negative effect among low-income households in Manila.
problem_and_motivation: Low-income micro-entrepreneurs in Manila face barriers to formal finance and often make short-sighted decisions due to survival pressures. No prior work has investigated the combined effect of myopic decision-making and access to finance on micro-enterprise performance in this context. This study addresses that gap to inform targeted interventions.
approach:
  - Quantitative survey of 100 sari-sari store owners in Manila using a pen-and-paper questionnaire.
  - Measured myopic decision-making across competitive, cooperative, temporal, and learning dimensions using a validated scale.
  - Assessed access to finance through barriers, formal lending, and informal credit indicators.
  - Evaluated business performance via financial, customer satisfaction, market competitiveness, growth, and operational metrics.
  - Used regression analysis to test direct and moderating effects with p-value significance thresholds.
findings:
  - num: Myopic decision-making significantly impacts business performance (p < 0.001).
  - num: Access to finance significantly improves business performance (p < 0.001).
  - num: Access to finance moderates the negative effect of myopic decision-making on performance (p = 0.005).
  - Temporal myopia (mean 2.96) and learning myopia (mean 2.44) are the most and least prevalent dimensions, respectively.
  - Barriers to access (mean 2.81) are the highest perceived financial constraint, while formal lending use is very low (mean 1.49).
  - Customer satisfaction (mean 3.53) is the strongest performance area, while financial performance (mean 2.61) is the weakest.
  - 44% of respondents cut R&D spending, indicating high temporal myopia.
  - 33% rarely consider collaborations, reflecting cooperative myopia.
key_figures_tables:
  - Figure 1: Operational framework linking myopic decision-making, access to finance, and business performance → Framework for integrated analysis.
  - Table 3: Summary stats for myopic dimensions → Temporal myopia highest, learning myopia lowest.
  - Table 4: Access to finance stats → Barriers high, formal and informal use low.
  - Table 5: Business performance stats → Customer satisfaction highest, financial performance lowest.
  - Table 6: Hypothesis test results → All three hypotheses significant (p < 0.001 and p = 0.005).
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Myopic Decision-Making
    definition: A cognitive bias prioritizing immediate rewards over long-term benefits, encompassing competitive, cooperative, temporal, and learning myopia.
  - term: Access to Finance
    definition: Availability and use of formal financial services including credit, savings, and payments, as well as informal credit sources.
  - term: Business Performance
    definition: Holistic measure of effectiveness and success, encompassing financial and non-financial metrics.
  - term: Micro-Enterprise
    definition: Business with assets below ₱3 million and fewer than 10 employees in the Philippines.
  - term: Low-Income Households
    definition: Families earning around or below ₱24,000 monthly, sufficient for basic food but inadequate for essential non-food expenses.
critical_citations:
  - "[Czakon et al., 2023] — Validated strategic myopia scale used."
  - "[Amadasun & Mutezo, 2022] — Framework for access to finance barriers."
  - "[Jachimowicz et al., 2017] — Links poverty to myopic decisions."
  - "[Orbeta et al., 2020] — Micro-enterprises as livelihood for low-income Filipinos."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Directly studies low-income micro-entrepreneurs in Manila, a core user demographic.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Examines income constraints and financial barriers faced by low-income households.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Focuses on myopic decision-making and financial access behaviors.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Informal credit and family loans are culturally embedded practices in the Philippines.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: Sari-sari stores cater to daily and occasion-based spending, though not directly measured.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Identifies gaps in formal financial access that PFMS like Odin could address.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Highlights barriers to formal finance (collateral, documentation) that digital PFMS can mitigate.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Myopic decision-making is a behavioral profile directly relevant to personal finance systems.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: medium
      justification: Temporal and learning myopia patterns inform initial user profile assumptions.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: contextual
      justification: Provides behavioral dimensions that could be used for classification.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: Mentions inadequate savings as a consequence of myopia but does not focus on goal management.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: medium
      justification: Addresses informal credit and debt cycles, relevant to debt management features.
    - code: 13.C
      name: End-of-Period Surplus as a Savings Input
      relevance: low
      justification: Tangentially related through business reinvestment but not directly addressed.
  contribution: This paper provides empirical evidence that myopic decision-making reduces business performance, which directly informs Odin's behavioral profiling module. The finding that access to finance moderates this effect justifies Odin's budget recommendation and savings management features. The identification of specific myopia dimensions (temporal, learning) guides the design of user onboarding and financial literacy interventions within the app. The study's focus on low-income Filipino micro-entrepreneurs validates Odin's target demographic and contextual design choices.
  directly_justifies:
    - Myopic decision-making significantly reduces micro-enterprise business performance.
    - Access to finance significantly improves business performance for low-income micro-entrepreneurs.
    - Access to finance moderates the negative effect of myopic decision-making on business performance.
    - Financial literacy programs and improved formal access are recommended interventions.
    - Temporal myopia (short-term focus) is the most prevalent form of myopic decision-making.
  limits:
    - Focuses only on sari-sari store owners in Manila, limiting generalizability to other micro-enterprise types.
    - Cross-sectional design cannot establish causality.
    - Self-reported measures may introduce social desirability or recall bias.
    - Does not cover other factors beyond myopic decision-making and access to finance.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was conducted. The paper was flagged as highly relevant to the Filipino Cultural Context domain (topics 1.A, 1.B, 1.C) because it directly studies low-income micro-entrepreneurs in Manila, providing foundational demographic and behavioral insights. It was also relevant to Existing Systems & Gaps (4.A, 4.B) due to its identification of formal finance barriers that Odin can address. For Behavioral Profiling (5.A, 5.B, 5.C), the paper's myopia dimensions offer a validated framework for classifying user financial behavior. The Savings & Debt Management domain (13.A, 13.B, 13.C) was moderately relevant due to discussions of informal credit and inadequate savings. Topics like Expense Categorization (3.A-3.C), Forecasting (6.A-6.B), Anomaly Detection (8.A-8.C), and Mobile Design (9.A-9.B) were considered but rejected as the paper does not address algorithmic or design aspects. The paper was deemed contextual for 2.D (spending cycles) as it mentions daily sales but does not analyze seasonal patterns. Overall, the paper provides strong empirical justification for Odin's behavioral and financial access features, though its non-algorithmic nature limits direct technical contributions.
limitations:
  - Limited to sari-sari stores in Manila; may not generalize to other micro-enterprises or regions.
  - Cross-sectional design prevents causal inference.
  - Self-reported data may be biased.
  - Excludes other potentially important factors like market conditions or family support.
  - No historical financial data used due to lack of formal record-keeping. [unacknowledged]
remember_this:
  - Myopic decision-making significantly harms micro-enterprise business performance.
  - Access to finance improves performance and buffers against myopic decisions.
  - Temporal myopia is the most common form of short-term thinking among entrepreneurs.
  - Barriers to formal finance are high, while informal credit is limited in this sample.
  - Customer satisfaction is the strongest performance area; financial performance is weakest.
```
---

## Paper 17: Dela Cruz et al_summarized.md

**Source File:** `Dela Cruz et al_summarized.md`

```yaml
paper_id: 10.xxxx/RIBEr-2026-15-2-902
designation: local
title: Dependence of Filipino Young Professionals’ Well-being on their Investing Years and Income in the National Capital Region
authors: Dela Cruz, M. A. T.; Jurada, P. H. G.; Recreo, C. R.; Mandigma, M. B. S.; Magbata, E. V. S.
year: 2026
venue: Review of Integrative Business and Economics Research
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 5.A
  - 6.A
  - 13.A
tldr: Young professionals' financial well-being is positively correlated with both years of investing and income, with financial behavior showing the strongest predictive influence.
problem_and_motivation: The specific interplay between income, years of investing, and financial well-being among young professionals in the National Capital Region remains unexamined. Understanding this nexus is crucial for creating targeted programs to enhance financial stability in this demographic.
approach:
  - A descriptive-correlational research design surveyed 389 young professionals aged 25-35 in the National Capital Region.
  - The study used an adopted and validated questionnaire from the CFPB Financial Well-Being Scale, achieving a Cronbach Alpha of 0.964.
  - Data were analyzed using Pearson's coefficient correlation and multiple regression analysis.
  - Control variables included highest educational attainment and financial behavior.
findings:
  - num: Years of investing have a significant positive correlation with financial well-being (r = 0.364, p < .01).
  - num: Income shows a significant but low positive correlation with financial well-being (r = 0.309, p < .01).
  - num: Financial behavior explains 62.3% of the variability in financial well-being when combined with income and investing years.
  - num: Most respondents (39.59%) have been investing for 1-2 years, and 45.24% earn between PHP 20,001-50,000 monthly.
  - The overall financial well-being of respondents was rated as "Excellent" with a mean score of 3.25.
  - Higher income, longer investment years, and better education and financial behavior increase financial well-being.
key_figures_tables:
  - Figure 1: Conceptual Framework of the study → Shows financial well-being as dependent on years of investing and income.
  - Table 2: Investing years and Income of Respondents → Provides demographic distribution for the independent variables.
  - Table 3: Level of Financial Well-being → Shows mean scores for each financial well-being indicator.
  - Table 4: Correlation Analysis → Reveals significant positive correlations for all variables with financial well-being.
  - Table 5: Model Summary → Shows the explanatory power of different regression models.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: NCR
    definition: National Capital Region, the metropolitan area centered on Manila, Philippines.
  - term: Financial Well-being
    definition: The state of having control over finances, ability to absorb financial shocks, and being on track to meet financial goals.
  - term: FWB
    definition: Financial Well-being, as measured by the CFPB scale and used throughout the paper.
  - term: PFMS
    definition: Personal Finance Management System, though not explicitly mentioned in the paper, it is the context for Odin.
critical_citations:
  - "[Lusardi & Mitchell, 2014] — Establishes link between financial literacy and retirement planning."
  - "[She et al., 2022] — Identifies key factors influencing young adults' financial well-being."
  - "[Lambert et al., 2023] — Defines contributing factors to financial well-being, including behavior and life stage."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: The study's sample is exclusively Filipino young professionals aged 25-35 in NCR.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Provides data on income levels and investment classes (stocks, bonds, mutual funds) of the demographic.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly investigates the financial well-being and investment behavior of the target demographic.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Identifies financial behavior as a strong predictor of financial well-being and profiles risk attitudes.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: contextual
      justification: The study's correlational findings could inform variables used in predictive models, though it does not build one itself.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Discusses savings, emergency funds, and retirement goals as components of financial well-being.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: contextual
      justification: Highlights the gap in research on the nexus of income, investing, and financial well-being for the target group.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: low
      justification: Tangentially touches on managing income and expenses, but does not specifically address budgeting strategies.
  contribution: The paper provides empirical evidence on the significance of income and investing years as determinants of financial well-being, directly informing Odin's spending forecasting and budget recommendation modules. Its findings on financial behavior emphasize the importance of behavioral profiling in predicting financial health. The study's focus on Filipino young professionals makes it directly applicable to Odin's target user base, justifying the need for culturally tailored features. This research supports Odin's design by confirming that income and investment horizon are key variables to track and analyze for personalized financial insights.
  directly_justifies:
    - Years of investing is a significant positive predictor of financial well-being for Filipino young professionals.
    - Income has a significant positive correlation with financial well-being, but is not the sole determinant.
    - Financial behavior is the most significant predictor of financial well-being.
    - The target demographic has an "Excellent" financial well-being level, but with low investment experience, suggesting an opportunity for education and planning tools.
  limits:
    - The study is limited to the National Capital Region, which may not represent the whole Philippines.
    - It uses a correlational design, so it cannot establish causation.
    - The sample might have selection bias due to purposive sampling.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was executed. The domains of Filipino Cultural Context, Behavioral Profiling, Spending Forecasting, Savings & Debt Management, and System Evaluation were flagged as relevant. Specific topic codes selected were 1.A, 1.B, 1.C, 5.A, 6.A, and 13.A, with high relevance for demographic profiling (1.A, 1.C) and behavioral analysis (5.A). The topics 2.A (Culturally Specific Financial Practices) and 2.D (Filipino Spending Cycles) were borderline but rejected because the study does not focus on specific cultural practices like 'utang' or 'paluwagan', but on general financial well-being. The Algorithmic domains (6.B, 7.B, 7.C, 8.A, 8.B) were considered and rejected as the paper does not propose or evaluate algorithms, though it provides valuable input variables (income, years investing) that justify their use in such modules. The paper's overall relevance to Odin is high as it provides foundational data on the financial health and key determinants for its target user base, which is essential for designing effective personal finance features.
limitations:
  - The correlational design prevents causal inference.
  - The sample is limited to the National Capital Region, limiting generalizability to other Philippine regions. [unacknowledged]
  - The study's reliance on self-reported data may introduce bias. [unacknowledged]
  - The use of a 4-point Likert scale may not capture nuances in financial well-being. [unacknowledged]
remember_this:
  - Financial well-being of young professionals in NCR is rated as Excellent.
  - Years of investing significantly and positively correlates with financial well-being.
  - Income has a significant, albeit low, positive correlation with financial well-being.
  - num: Financial behavior accounts for 62.3% of the variance in financial well-being.
  - Targeting investment education for young professionals can enhance their well-being.
```
---

## Paper 18: Yu_summarized.md

**Source File:** `Yu_summarized.md`

```yaml
paper_id: 10.32479/irmm.23379
designation: local
title: Exploring the Impact of Cashless Payment Systems on Impulsive Buying Behavior among Generation Z Consumers
authors: Yu, M. P.
year: 2026
venue: International Review of Management and Marketing
odin_topics:
  - 1.A
  - 2.D
  - 3.C
  - 4.A
  - 5.A
  - 7.D
  - 10.B
tldr: Cashless payment systems enable impulsive buying among Filipino Gen Z consumers through convenience, promotions, social media influence, and trust, with males exhibiting stronger susceptibility to these factors.
problem_and_motivation: Existing literature examines cashless payment factors and impulsive buying in isolation, lacking an integrated model for Generation Z within the Filipino context. This gap hinders the understanding of how convenience, social media, promotions, and security collectively drive impulsive behavior among this digitally native demographic.
approach:
  - A descriptive survey design was employed using a researcher-made questionnaire.
  - Data was collected from 259 Gen Z respondents in Cantilan, Philippines.
  - The instrument measured factors of ease, social media, promotions, and trust on a 5-point Likert scale.
  - Descriptive and inferential statistics including Pearson correlation, Mann-Whitney U, and MANOVA were utilized.
  - The study analyzed differences in impulsive tendencies based on gender, payment method, and product type.
findings:
  - num: The overall weighted mean for impulsive buying behavior was 4.03, indicating agreement that cashless payments drive it.
  - num: A very strong positive correlation (r = 0.892, P = 0.000) exists between cashless payment systems and impulsive buying.
  - Perceived usefulness, trust, and security showed the strongest correlation (r = 0.869, P = 0.000) with impulsive buying.
  - Significant gender differences were found for ease/convenience (U=2969.00, P=0.003), promotions (U=3232.50, P=0.021), and trust/security (U=2839.00, P=0.001), with males more influenced.
  - Social media influence was not significantly different between genders (P=0.123).
  - No significant differences in impulsive buying were found based on preferred cashless payment method (P=0.194) or product type (P=0.931).
key_figures_tables:
  - Table 1: Demographic profile shows 74% of respondents are 13-21, 85% female, and 83% prefer mobile payment apps.
  - Table 2: Ease and convenience factor weighted mean of 4.09, with the highest agreement on payments preventing avoidance of impulse purchases.
  - Table 3: Social media influence factor weighted mean of 4.11, with positive reviews strongly influencing spontaneous purchases.
  - Table 4: Promotions and discounts factor weighted mean of 4.02, with promotional discounts being the strongest motivator.
  - Table 5: Perceived usefulness, trust, and security factor weighted mean of 4.00, where usefulness for quick purchases is the top item.
  - Table 6: Impulsive buying behavior weighted mean of 4.03, with promotional offers and cashback as the strongest driver.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: BNPL
    definition: Buy Now Pay Later, a service allowing deferred payment for purchases.
  - term: FOMO
    definition: Fear Of Missing Out, an anxiety that others might be having rewarding experiences.
critical_citations:
  - "[Goyal, 2024] — Shows mobile wallets facilitate Gen Z impulse buying."
  - "[Izham et al., 2025] — BNPL services significantly impact Gen Z impulse buying."
  - "[Djamhari et al., 2024] — Perceived usefulness and safety drive impulsive buying."
  - "[Underdown and Tamara, 2025] — BNPL encourages addiction and lack of self-control."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: The study focuses specifically on Filipino Generation Z consumers, a core demographic for Odin.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: While not explicit, the study examines general impulsive spending behavior relevant to understanding spending cycles.
    - code: 3.C
      name: User-Defined Allocation Constraints
      relevance: low
      justification: The study identifies impulsive buying as a behavior that conflicts with user-defined budgets, providing a justification for constraint features.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: The paper evaluates how existing cashless systems (e-wallets, BNPL) facilitate spending, which is part of the fintech landscape.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: The study profiles impulsive buying behavior among Gen Z, which can inform behavioral profiling models.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: contextual
      justification: The suggested "impulse delay" feature relates to modifying behavior to stay within constraints, a form of infeasibility handling.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Trust and security perception is a key factor influencing impulse buying, highlighting the role of user trust in financial systems.
  contribution: This paper provides empirical evidence on how cashless payment systems enable impulsive buying among Filipino Gen Z, a behavioral trait that Odin's budget recommendation and anomaly detection modules must account for. The strong correlation (r=0.892) between cashless payments and impulsive behavior justifies the need for behavioral profiling in Odin to identify at-risk users. The finding that trust and security perception is the strongest correlate highlights the importance of Odin's data privacy and security features in building user confidence. The study's identification of gender differences (males more susceptible to convenience and promotions) supports the design of personalized nudges within Odin. Furthermore, the suggested "impulse delay" intervention validates Odin's potential for incorporating behavioral constraints to counteract spending tendencies.
  directly_justifies:
    - "Cashless payment systems have a very strong positive correlation (r=0.892) with impulsive buying among Filipino Gen Z."
    - "Perceived usefulness, trust, and security are the strongest factors correlating with impulsive buying behavior."
    - "Males are significantly more influenced by convenience, promotions, and security than females in impulsive buying."
    - "Interventions like impulse-delay features can help counter impulsive buying behaviors."
    - "Financial literacy programs should target social media and promo influence to improve spending habits."
  limits:
    - "The study is geographically limited to Cantilan, Philippines, reducing generalizability."
    - "Self-reporting may introduce bias in measuring impulsive buying tendencies."
    - "The study does not account for moderating variables like income, financial literacy, or self-control."
  mapping_rationale: A systematic scan was performed across all 12 functional domains and their associated topic codes. The paper was flagged for relevance in the domains of Filipino Cultural Context (1.A, 2.D), Expense Categorization (3.C), Existing Systems (4.A), Behavioral Profiling (5.A), Budget Recommendation (7.D), and Data Privacy (10.B). Topic 1.A is high as the study focuses squarely on Filipino Gen Z. Topic 5.A is medium as it profiles impulsive buying, a key behavioral trait. Topic 10.B is medium due to the significant role of trust in driving behavior. Topic 3.C and 7.D are low/contextual, as the study justifies the need for user constraints and behavioral interventions but does not directly address them. Topics like 2.B (Seasonal Spending) and 2.C (User-Declared Preferences) were rejected as the paper does not address cyclical patterns or explicit user preferences. Topic 6.A (Forecasting) and 8.A (Anomaly Detection) were rejected as the paper does not involve predictive modeling or detection algorithms. The overall relevance is moderate, as the paper provides strong behavioral insights that inform the design of Odin's user-facing and behavioral modules, but is not directly algorithmic.
limitations:
  - "The study's cross-sectional design prevents establishing causality between cashless payments and impulsive buying. [unacknowledged]"
  - "The generalizability of findings to other regions or demographics within the Philippines is limited due to the localized sample. [unacknowledged]"
  - "Potential self-report bias may affect the accuracy of reported impulsive buying tendencies. [unacknowledged]"
  - "The study does not examine the role of financial literacy or income as moderating variables. [unacknowledged]"
remember_this:
  - "Cashless payments strongly correlate with impulsive buying among Filipino Gen Z."
  - "Trust and security perception is the most influential factor on impulse buying."
  - "Males are more susceptible to convenience, promotions, and security cues."
  - "User demographics like gender should inform personalized financial nudges."
  - "Impulse-delay features within payment systems can mitigate overspending."
```
---

## Paper 19: Nduka & Benedicto_summarized.md

**Source File:** `Nduka & Benedicto_summarized.md`

```yaml
paper_id: 67cfa1c1-53c3-52e5-a18b-7e1b0aa936ce
designation: local
title: Nursing Career Towards Financial Independence
authors: Nduka, P.; Benedicto, E.G.
year: 2026
venue: IJRDO - Journal of Health Sciences and Nursing
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 4.A
  - 4.B
  - 5.A
  - 10.A
  - 11.A
tldr: Nurses in the Philippines perceive financial independence as essential for security and motivation, yet income-expense mismatches and family breadwinner roles severely limit savings and long-term planning.
problem_and_motivation: Filipino nurses face a critical gap between essential professional roles and inadequate compensation, which undermines financial stability. Rising living costs and heavy family obligations further strain their economic resilience, yet institutional support mechanisms are largely absent. This study addresses the lack of focused research on nursing as a pathway to financial independence in the Philippine context.
approach:
  - A qualitative phenomenological design was used to explore the lived financial experiences of 28 registered nurses in Metro Manila.
  - Data were collected through one-on-one semi-structured interviews lasting 40-60 minutes, with a validated instrument achieving Aiken's V scores of 0.8 to 1.0.
  - Participants were purposively sampled from three government-owned Level III specialty hospitals, ensuring diversity in demographics and financial roles.
  - Thematic analysis was conducted using Colaizzi's phenomenological method to extract themes from verbatim transcripts.
  - The study adhered to the Philippines' Data Privacy Act of 2012 (RA 10173) for data storage and destruction.
findings:
  - "num: 53.57% of nurses were in the 33-39 age bracket, while 50% held lower government salary grades (SG 2-6)."
  - "num: 53.57% of nurses held master's degrees and 10.71% held doctorates, indicating high educational attainment despite wage stagnation."
  - "num: 89.29% of participants identified as family breadwinners, and 53.57% supported four or more dependents."
  - Seven key themes emerged regarding the importance of financial independence: personal security, professional motivation, family support, career development, stress reduction, empowerment, and retirement planning.
  - A clear income-expense mismatch was identified, with most nurses experiencing monthly deficits and limited savings capacity.
  - Single nurses living alone can cover basic needs but struggle to save, while single breadwinners face greater financial strain and psychological stress.
  - The proposed Nurse Financial Empowerment and Resilience Program (N-FERP) is structured around financial literacy, supplementary income, institutional support, and access to affordable financial services.
key_figures_tables:
  - "Table 1: Demographic profile of 28 nurse-participants → Workforce is predominantly female, young to middle-aged, and highly educated but in lower salary grades."
  - "Figure 3: Nurse Financial Empowerment and Resilience Program (N-FERP) framework → Integrated strategy combining education, income, support, and financial tools."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: N-FERP
    definition: Nurse Financial Empowerment and Resilience Program, a proposed framework for improving nurses' financial independence.
  - term: PFMS
    definition: Personal Financial Management System, a digital tool for managing personal finances.
critical_citations:
  - "[Lopez & Malagum, 2024] — Compensation mismatch with nursing work complexity."
  - "[Ortiga & Macabasag, 2021] — Rising cost of living in urban centers like Metro Manila."
  - "[Cubelo et al., 2024] — Financial insecurity linked to migration and turnover."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Focuses on Filipino nurses, a key subset of Filipino young professionals.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Provides detailed data on income, salary grades, and living costs for nurses.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Explores nurses' financial practices, including budgeting and saving behaviors.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Discusses extended-family financial obligations, a culturally specific practice.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Contextualizes the lack of institutional financial support for nurses.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies gaps in compensation and institutional financial programs for nurses.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Differentiates financial profiles of single nurses living alone versus breadwinners.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Mentions compliance with the Philippines' Data Privacy Act (RA 10173) in the methodology.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: Tangentially related through the proposal of financial literacy workshops.
  contribution: This paper contributes to Odin's design by establishing the foundational financial realities and constraints of Filipino nurses as a target user demographic. It validates the need for modules that account for income-expense mismatches, culturally embedded family obligations, and distinct financial profiles. The findings directly inform Odin's expense categorization and behavioral profiling by highlighting the socio-economic factors that shape spending behaviors. The proposed N-FERP framework offers a reference point for Odin's budget recommendation and savings management functionalities.
  directly_justifies:
    - "The nurse workforce shows a clear income-expense mismatch, with monthly salaries often below living costs."
    - "Single nurses serving as adult breadwinners experience heightened financial strain and psychological stress."
    - "Structured financial literacy programs are a key strategy for improving financial resilience."
  limits:
    - "Study is confined to three government hospitals in Metro Manila, limiting generalizability to private or provincial settings."
    - "The qualitative design provides depth but does not quantify the prevalence of identified financial challenges."
    - "The proposed N-FERP framework has not been empirically tested for effectiveness."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. Domains flagged as relevant include Filipino Cultural Context (2.A, medium), Existing Systems & Gaps (4.A, contextual; 4.B, high), Behavioral Profiling (5.A, medium), and Data Privacy (10.A, contextual). High relevance was assigned to topics 1.A, 1.B, 1.C, and 4.B due to the paper's detailed demographic and financial analysis. Medium relevance was assigned to 2.A for culturally specific practices and 5.A for behavioral profiling. Low relevance was assigned to 11.A for tangential mention of engagement. Contextual relevance was assigned to 4.A and 10.A as they provide background without actionable design insights. Domains such as Forecasting, Anomaly Detection, and Mobile Design were considered and rejected as the paper does not address computational or algorithmic aspects. The overall relevance is high for understanding Odin's target user financial behavior and systemic gaps.
limitations:
  - "The study sample size of 28 is sufficient for qualitative saturation but not for statistical generalization."
  - "The study only included nurses from government hospitals, thus findings may not apply to private-sector nurses."
  - "The financial data are self-reported and may be subject to social desirability bias."
  - "No longitudinal data are provided to assess changes in financial status over time. [unacknowledged]"
  - "The study does not compare nurses with other professional groups to isolate occupation-specific financial challenges. [unacknowledged]"
remember_this:
  - "Nurses perceive financial independence as essential for personal security, professional motivation, and family support."
  - "A clear income-expense mismatch exists, with most nurses experiencing monthly deficits."
  - "Single breadwinner nurses face greater financial strain and limited savings compared to those living alone."
  - "Structured financial literacy, supplementary income, and institutional support are key strategies for empowerment."
  - "The proposed N-FERP framework aims to enhance economic resilience and reduce nurse vulnerability."
```
---

## Paper 20: Erno & Grefalde_summarized.md

**Source File:** `Erno & Grefalde_summarized.md`

```yaml
paper_id: 1d5a2f70-4b6d-5ba5-9b0d-9e5e6f7a8b9c
designation: local
title: Behavioral and Psychological Drivers of Sustainable Saving and Financial Resilience among Community Households
authors: Erno, G. Y. L.; Grefalde, J. Q.
year: 2026
venue: Journal of Daoist Studies 19-3s
odin_topics:
  - 3.A
  - 3.B
  - 13.A
  - 13.B
  - 1.C
  - 1.B
  - 5.A
  - 2.B
  - 2.A
tldr: Community households exhibit strong debt discipline but weak budgeting, saving, and investment behaviors, resulting in low financial resilience shaped by risk-averse and defensive financial decision-making.
problem_and_motivation: Household financial resilience in resource-constrained community settings is poorly understood, particularly how behavioral and psychological drivers interact with financial capability domains. Existing research lacks an integrated framework that links sustainable saving behavior, financial capability dimensions, and resilience outcomes specifically for Filipino community households. This gap limits the design of targeted interventions that address both structural and behavioral barriers to financial stability.
approach:
  - Quantitative descriptive design with 300 household financial decision-makers from Tago, Surigao del Sur.
  - Structured survey measuring budgeting, saving, debt management, investment behavior, and financial resilience indicators.
  - Items adapted from established financial capability and resilience frameworks with localized language for clarity.
  - Face-to-face administration to ensure comprehension and minimize non-response across varying literacy levels.
  - Descriptive analysis to document existing financial practices and resilience capacity without manipulation.
findings:
  - Households demonstrate strong debt management (mean 3.86, Agree) with prudent borrowing and repayment discipline.
  - Budgeting systems are weak (mean 2.35, Disagree) despite strong family involvement in budget preparation.
  - Institutionalized saving behavior is underdeveloped (mean 2.44, Disagree) with low use of banks and cooperatives.
  - Investment engagement is the weakest domain (mean 2.37, Disagree), indicating limited wealth-building pathways.
  - Financial resilience is low (mean 1.98, Disagree), with limited shock absorption and recovery capacity.
  - num: 1.60 mean for managing sudden expenses reflects severe savings insufficiency and perceived vulnerability.
  - num: 4.30 mean for avoiding high-interest loans confirms defensive financial awareness and risk aversion.
  - Behavioral barriers include present bias, decision fatigue, and low confidence in coping with uncertainty.
  - Households prioritize short-term financial control over long-term planning, reflecting adaptive responses to perceived economic vulnerability.
  - Strong debt discipline coexists with weak budgeting, saving, and investment, creating an imbalanced capability configuration.
key_figures_tables:
  - Table 1: Financial capability across domains → Imbalanced configuration with strong debt discipline but weak budgeting, saving, and investment.
  - Table 2: Financial resilience indicators → Uniformly low resilience across shock absorption, adaptability, recovery, and preparation.
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Financial resilience
    definition: Capacity of households to withstand, adapt to, and recover from economic disruptions while maintaining essential consumption.
  - term: Financial capability
    definition: Multidimensional construct integrating financial knowledge, attitudes, skills, and behavioral execution in decision-making.
  - term: Sustainable saving behavior
    definition: Consistent, long-term financial discipline aligned with future-oriented goals and adaptive coping strategies.
critical_citations:
  - "[Katnic et al., 2024] — Financial literacy predicts resilience outcomes in rural households."
  - "[Karlan et al., 2017] — Community-based savings groups enhance financial discipline and collective accountability."
  - "[Bufe et al., 2022] — Capability metrics predict financial shock absorption capacity."
  - "[Liu et al., 2025] — Defines financial resilience as absorbing shocks while sustaining basic needs."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Surveys budgeting practices as a core financial capability domain.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: low
      justification: Mentions grouping expenses but does not design categorization frameworks.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Assesses goal-oriented saving and emergency savings behavior.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: Provides extensive findings on debt discipline and borrowing behavior.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: low
      justification: Community household focus indirectly informs young professional context.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: contextual
      justification: Provides background on income stability and financial practices.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Identifies defensive, risk-averse financial profiles and behavioral drivers.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: low
      justification: Mentions income variability but does not analyze seasonal patterns.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: low
      justification: References community norms but does not focus on cultural practices.
  contribution: This paper provides empirical evidence that financial resilience among community households depends on balanced integration of budgeting, saving, debt management, and investment behaviors. The findings directly inform Odin's expense categorization module by revealing the importance of structured budgeting and savings tracking. The study highlights the need for Odin's debt management features to support disciplined borrowing while also encouraging proactive saving and investment. The behavioral profiling insights validate Odin's approach to understanding user risk perception and decision fatigue. The paper underscores the critical role of psychological readiness and institutional access, which Odin must address through trust-building and simplified financial tools.
  directly_justifies:
    - Defensive financial habits focused on debt avoidance do not generate comprehensive financial resilience.
    - Financial resilience depends on balanced integration of planning, saving, borrowing, and investing behaviors.
    - Behavioral barriers such as present bias and decision fatigue constrain long-term financial planning.
    - Strong debt discipline without structured saving and investment limits adaptive financial capacity.
    - Psychological readiness and coping confidence are essential for effective financial decision-making under uncertainty.
  limits:
    - Geographic scope limited to a single rural municipality, limiting generalizability.
    - Quantitative descriptive design does not establish causal relationships [unacknowledged].
    - Reliance on self-reported data may introduce social desirability bias [unacknowledged].
    - Psychological constructs were not directly measured, limiting understanding of mediating effects.
    - Cross-sectional design captures behaviors at a single point, missing adaptive dynamics over time.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was conducted. The paper was flagged as relevant for Expense Categorization (3.A, 3.B) because it measures budgeting practices, though not at a granular category level. For Savings & Debt Management (13.A, 13.B), relevance is high and medium respectively, given direct assessment of debt discipline and saving behavior. Financial Behavior (1.C, 5.A) was selected due to the defensive, risk-averse profile observed and the behavioral drivers discussed. Seasonal spending (2.B) and cultural practices (2.A) were considered but rejected as only tangentially mentioned. Domains such as Anomaly Detection, Mobile-First Design, Data Privacy, Engagement, and System Evaluation were considered and rejected because the paper does not address these topics. The paper's primary contribution is its behavioral and financial capability analysis, making it highly relevant for understanding user profiles and debt management, with medium relevance for general financial behavior and saving goals. Overall, the paper provides foundational insights into financial behavior patterns that Odin must address in designing for Filipino users.
limitations:
  - Geographic scope was confined to a single municipality with predominantly rural characteristics, limiting generalizability to urban or other socio-economic contexts.
  - The quantitative descriptive design did not establish causal relationships among behavioral practices, psychological factors, and resilience outcomes.
  - Reliance on self-reported data from household decision-makers may introduce response biases, including social desirability and recall limitations.
  - The study focused primarily on behavioral and capability indicators and did not directly measure psychological constructs such as financial anxiety, coping confidence, or perceived control.
  - External economic factors—including inflation, employment instability, market access, and environmental risks—were not incorporated, although they shape financial capacity and stress responses.
  - The cross-sectional design captured financial behaviors at a single point in time, limiting the ability to observe adaptive changes over time.
remember_this:
  - Household financial capability is imbalanced with strong debt discipline but weak saving.
  - Low financial resilience reflects limited shock absorption and recovery capacity.
  - Defensive financial habits constrain long-term stability and adaptive capacity.
  - Sustainable financial resilience requires balanced integration of budgeting, saving, debt, and investment.
  - Financial decisions are risk-averse, shaped by perceived vulnerability and limited planning confidence.
```
---

## Paper 21: Mutuc_summarized.md

**Source File:** `Mutuc_summarized.md`

```yaml
paper_id: 10.3390/ijfs13040222
designation: local
title: Exploring the Interplay of Life Attitude and Cognitive Ability in Shaping the Intention to Stock Market Participation Among Young Professionals in the Philippines
authors: Mutuc, E. B.
year: 2025
venue: International Journal of Financial Studies
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.D
  - 4.B
  - 5.A
  - 5.C
  - 10.A
tldr: Life purpose and goal-seeking positively predict stock market participation intention, with cognitive ability (financial literacy) mediating this relationship among young Filipino professionals.
problem_and_motivation: Existing behavioral finance research has largely neglected how broader psychological orientations like life attitude influence investment behavior, particularly among young professionals in emerging economies. The interaction between these life orientations and cognitive ability remains poorly understood, limiting holistic models of financial participation.
approach:
  - Quantitative cross-sectional survey of 195 randomly selected young professionals (aged 20–39) from Bulacan, Philippines.
  - Used the Life Attitude Profile–Revised (LAP-R) to measure existential dimensions and the Financial Literacy Inventory for cognitive ability.
  - Applied Partial Least Squares Structural Equation Modeling (PLS-SEM) with 5000 bootstrap resamples to test direct and mediating effects.
  - Included control variables (sex, age, education, employment) and conducted multi-group analyses for gender and education subgroups.
  - Assessed common method variance via Harman's single-factor test and full collinearity assessment.
findings:
  - num: Life Attitude Profile (LAP) positively predicts Intention to Stock Market Participation (β = 0.154, p = 0.025).
  - num: Cognitive Ability mediates the LAP–SMP relationship (β = 0.051, p = 0.032), with 39% of LAP's influence operating through cognition.
  - num: Goal Seeking (β = 0.396, p = 0.009) and Death Acceptance (β = 0.312, p < 0.001) are the strongest positive LAP sub-dimension predictors of SMP.
  - Life Purpose showed a negative association with SMP (β = −0.243, p = 0.036), suggesting purpose-driven individuals may be financially conservative.
  - num: The model explained 47.1% to 58.2% of variance in SMP across different specifications.
  - num: Cognitive Ability mean score was 67.83% (SD = 16.53), indicating higher-than-average financial literacy in the sample.
  - num: Sex differences were found: males relied more on cognitive ability (C→SMP: β=0.42), females on life attitudes (LAP→SMP: β=0.38).
key_figures_tables:
  - Figure 1: Conceptual framework showing LAP dimensions, Cognitive Ability as mediator, and SMP as outcome → LAP influences SMP directly and via cognition.
  - Table 1: Descriptive statistics show favorable life attitudes (M=5.07–6.11) and moderate investment intention (M=4.28) → sample is purpose-driven with above-average financial literacy.
  - Figure 3: Lower-order construct model with path coefficients → Death Acceptance and Goal Seeking positively drive SMP; Life Purpose and Life Control show negative associations.
  - Figure 4: Higher-order model with R²=0.471 → LAP and Cognitive Ability collectively explain nearly half of investment intention variance.
key_equations:
  - equation: SMP_i = β_0 + β_1(LAP_i) + ε_i
    explanation: Direct effect of overall life attitude on investment intention.
  - equation: SMP_i = β_0 + β_1(LP_i) + β_2(EV_i) + β_3(LC_i) + β_4(DA_i) + β_5(WTM_i) + β_6(GS_i) + β_7(FMF_i) + ε_i
    explanation: Regression with seven LAP sub-dimensions predicting SMP.
  - equation: C_i = β_0 + β_1(LAP_i) + ε_i
    explanation: Life attitude predicts cognitive ability (financial literacy).
  - equation: SMP_i = β_0 + β_1(LAP_i) + β_2(CA_i) + ε_i
    explanation: Mediation model with both LAP and cognitive ability predicting SMP.
definitions:
  - term: Life Attitude Profile (LAP)
    definition: Multidimensional framework assessing sense of purpose, meaning, and life orientation (Reker et al., 1987).
  - term: Cognitive Ability
    definition: Efficiency in processing and integrating financial information, proxied by financial literacy in this study.
  - term: Stock Market Participation (SMP)
    definition: Intention to engage in equity market investments, measured via self-reported behavioral intention.
  - term: PLS-SEM
    definition: Partial Least Squares Structural Equation Modeling, a variance-based technique for prediction and mediation testing.
  - term: LAP-R
    definition: Life Attitude Profile–Revised, an instrument capturing existential vacuum, life purpose, control, death acceptance, will to meaning, goal seeking, and future meaning.
critical_citations:
  - "[van Rooij et al., 2011] — Financial literacy retains predictive validity for stock participation beyond wealth."
  - "[Guiso et al., 2008] — Trust in financial institutions shapes market entry decisions."
  - "[Lusardi & Mitchell, 2014] — Foundational evidence linking financial literacy to economic outcomes."
  - "[Haliassos & Bertaut, 1995] — Classic stock market participation puzzle paper."
  - "[Steger et al., 2006] — Meaning in life questionnaire validates existential constructs used here."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Directly samples Filipino young professionals (aged 20-39, white-collar) as the core population.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Examines investment intention and cognitive ability, indirectly reflecting financial decision-making structures.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly measures financial behavior (stock market participation intention) and its psychological drivers.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: Provides background on Philippine economic context but does not focus on specific cultural practices like utang or padala.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Mentions cultural-economic dynamics but does not analyze spending cycles; focuses on investment, not consumption.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies research gaps in behavioral finance (underexplored psychological orientations) that Odin could address.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly profiles individuals based on life attitudes and cognitive ability as predictors of financial behavior.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses PLS-SEM to classify and map relationships between psychological profiles and investment intentions.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Mentions ethical compliance with Data Privacy Act but does not address system-level privacy or security design.
  contribution: "Odin can cite this paper to justify its psychological profiling module (5.A) by demonstrating that life attitude dimensions meaningfully predict financial behavior. The mediating role of cognitive ability (6.A) supports Odin's use of financial literacy as a key input for forecasting and recommendation algorithms. The finding that purpose-driven individuals may be financially conservative (negative LP→SMP path) informs Odin's budget recommendation (7.B) to avoid over-recommending investments to users with strong conservative life purpose profiles. The robust mediation model also validates Odin's integrated approach: combining attitudinal profiling with cognitive assessment to produce more accurate financial behavior predictions."
  directly_justifies:
    - "Life attitude dimensions significantly predict intention to invest, supporting psychological profiling for financial apps."
    - "Cognitive ability mediates the effect of life attitudes on financial behavior, justifying inclusion of literacy measures."
    - "Goal seeking and death acceptance are strong positive predictors, indicating key profile dimensions for segmentation."
    - "Purpose-driven individuals may prefer conservative financial strategies, informing personalized recommendation constraints."
    - "Sex and education moderate the strength of attitudinal and cognitive pathways, suggesting demographic adjustments."
  limits:
    - "Cross-sectional design limits causal inference between life attitudes and investment intention."
    - "Self-reported data may introduce social desirability bias despite anonymity."
    - "Sample from Bulacan province may not generalize to other Philippine regions or national contexts."
    - "No local psychometric validation of the LAP-R instrument for the Filipino sample."
  mapping_rationale: "Systematic scan of all 12 functional domains and their associated topic codes identified the strongest relevance in the Filipino Cultural Context, Behavioral Profiling, and Spending Forecasting domains. The paper directly addresses Filipino young professionals (1.A, 1.B, 1.C) and provides empirical evidence linking life attitudes to financial behavior (5.A, 5.C). It also supports the Forecasting domain (6.A) by establishing cognitive ability (financial literacy) as a mediator, which informs predictive modeling inputs. Borderline cases: the paper touches on Filipino cultural context (2.A) through its setting and discussion of family obligations, but does not specifically analyze cultural practices, so relevance is contextual. The paper mentions data privacy compliance (10.A) but offers no system-level insights, hence low relevance. Domains like Anomaly Detection (8.A-C), Mobile-First Design (9.A-B), User Retention (11.A-B), System Evaluation (12.A-C), and Savings/Debt Management (13.A-C) were rejected as the paper does not address algorithm evaluation, system design, retention mechanisms, or debt/savings goals. Overall, the paper is highly relevant for establishing psychological and cognitive determinants of financial behavior among Odin's target demographic, justifying behavioral profiling and providing inputs for forecasting and recommendation modules."
limitations:
  - "Cross-sectional design restricts causal interpretation of relationships among LAP, cognitive ability, and SMP."
  - "Self-reported measures may introduce response biases, including social desirability. [unacknowledged]"
  - "Sample was drawn exclusively from Bulacan province, limiting generalizability to other Philippine regions or cross-national contexts. [unacknowledged]"
  - "Absence of a marker variable for common method variance testing, though procedural remedies were applied. [unacknowledged]"
  - "The LAP-R instrument was used without local cultural adaptation or pilot testing for the Filipino population."
remember_this:
  - "Cognitive ability mediates the link between life attitudes and investment intention."
  - "Goal seeking and death acceptance are the strongest positive predictors of investment intention."
  - "Purpose-driven individuals may exhibit conservative investment behavior."
  - "The model explains 47% of variance in investment intention among Filipino young professionals."
  - "Financial literacy training should be paired with psychosocial skill development for holistic financial engagement."
```
---

## Paper 22: Majeed_summarized.md

**Source File:** `Majeed_summarized.md`

```yaml
paper_id: 897b3dea-6484-53a2-a28c-aec3f4b027b0
designation: local
title: Spending Patterns and Financial Risks Among 'Buy Now, Pay Later' (BNPL) Consumers
authors: Majeed, K.
year: 2025
venue: Central Philippine University
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 4.A
  - 5.A
  - 5.B
  - 5.C
  - 13.A
  - 13.B
tldr: BNPL consumers frequently purchase essentials and unplanned items, with males spending more frequently and singles showing more unplanned buying, while perceived debt risk is high and relates to spending patterns.
problem_and_motivation: The rapid adoption of Buy Now, Pay Later services in the Philippines presents potential financial risks to consumers. However, the specific spending patterns and financial risks among Filipino BNPL users remain insufficiently understood. This study addresses the gap by examining these factors in Iloilo City to inform targeted consumer protection and financial literacy efforts.
approach:
  - A survey-correlational research design was employed to examine the relationship between spending patterns and perceived financial risks.
  - Data were collected from 214 BNPL consumers in Iloilo City selected through convenience sampling.
  - Descriptive statistics including frequency, percentage, mean, and standard deviation were used to summarize the data.
  - The study utilized Mann-Whitney U, Kruskal-Wallis H, and Spearman's Rho tests at a 0.05 significance level for inferential analysis.
  - Respondents were classified by sex, civil status, and educational attainment to explore demographic differences in spending and risk perception.
findings:
  - BNPL consumers exhibit frequent purchasing behavior and a high tendency for unplanned purchases, while prioritizing essential items over non-essential ones.
  - num: Perceived financial risk in terms of debt accumulation was rated high.
  - Perceived risk concerning late fees and financial instability was rated moderate.
  - num: Males reported significantly higher frequent spending compared to females.
  - num: Single consumers showed a significantly higher tendency for unplanned purchases and more frequent buying of non-essential items.
  - num: Single individuals and high school graduates perceived higher risks of debt accumulation and financial instability, respectively.
  - A significant positive relationship exists between consumer spending patterns and perceived financial risks.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: BNPL
    definition: Buy Now, Pay Later; a short-term financing option allowing consumers to make purchases and pay for them in installments.
  - term: Unplanned purchase
    definition: An item bought without prior intention, often impulsive.
  - term: Essential items
    definition: Goods necessary for basic living, such as food and groceries.
critical_citations:
  - "[Di Maggio et al., 2022] — foundational work on BNPL user characteristics."
  - "[Kumar & Nayak, 2024] — directly examines risky indebtedness and impulse buying in BNPL."
  - "[Addo & Houle, 2021] — key reference for financial behaviors across marital status."
  - "[Powell et al., 2023] — examines BNPL's link to financial wellbeing."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: Study focuses on BNPL consumers in the Philippines, a key demographic for Odin.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: contextual
      justification: Provides context on spending patterns and debt use among Filipino consumers.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly investigates spending behavior (frequency, unplanned purchases) and financial risk perception.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Examines spending on essentials vs. non-essentials, a culturally relevant distinction for Filipino budgeting.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: low
      justification: Tangentially related through the concept of unplanned purchases, but does not explicitly address seasonality.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: The paper touches on unplanned and essential spending, which may be linked to cultural occasions, but not directly.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: BNPL is identified as a growing financial service in the Philippine landscape.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly analyzes consumer spending patterns and risk perception, key components of a behavioral profile.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: contextual
      justification: Findings on demographic differences in spending can inform initial profile assumptions for cold-start scenarios.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Provides empirical data on spending patterns that could be used as features for classifying profiles.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: contextual
      justification: High perceived debt risk suggests a need for savings tools, though the paper does not study savings directly.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: Directly addresses debt accumulation as a primary financial risk, relevant for designing debt management features.
  contribution: This paper provides empirical evidence on the spending patterns and financial risk perceptions of BNPL users in the Philippines. The findings on frequent and unplanned spending can inform Odin's behavioral profiling module (5.A). The significant relationship between spending and perceived financial risk supports the need for proactive financial health indicators and debt management features (13.B). The demographic variations identified (e.g., by sex and civil status) offer valuable insights for designing personalized, cold-start profile models (5.B).
  directly_justifies:
    - "BNPL consumers frequently make unplanned purchases, highlighting the need for budget constraint features."
    - "Males reported higher frequent spending, suggesting gender should be a feature in behavioral profiling."
    - "Single consumers show higher unplanned spending, which can inform risk-based recommendation models."
    - "High perceived debt risk among BNPL users justifies the inclusion of debt management tools in PFMS."
  limits:
    - "Convenience sampling from a single city limits generalizability."
    - "Self-reported data may be subject to social desirability and recall bias."
    - "The study does not evaluate any specific algorithm or technical system for PFMS."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. Domains related to financial behavior and user profiling (e.g., Filipino Cultural Context, Behavioral Profiling, Savings & Debt) were flagged as relevant. Topic codes 1.A, 1.C, 2.A, 5.A, 5.B, 5.C, 13.A, and 13.B were selected with high to medium relevance. Codes 2.B and 2.D were considered borderline but ultimately assigned low relevance as the paper does not explicitly address seasonal or occasion-based spending. The system evaluation domains (12.A, 12.B, 12.C) and algorithm-specific topics (6.A, 6.B, 7.A-7.D, 8.A-8.C) were considered and rejected as the study is a non-algorithmic survey. The paper's overall relevance to Odin is in providing empirical data on Filipino consumer behavior to inform initial design and user modeling.
limitations:
  - "Convenience sampling from Iloilo City limits generalizability to all Filipino BNPL users. [unacknowledged]"
  - "Self-reported data on spending and risk perception may be influenced by social desirability bias. [unacknowledged]"
  - "The study is cross-sectional, preventing causal inferences between spending patterns and financial risks. [unacknowledged]"
  - "The specific BNPL services and their terms are not identified, which could influence user behavior. [unacknowledged]"
remember_this:
  - "BNPL users frequently buy essentials and make unplanned purchases."
  - "Males and singles show higher risk spending patterns."
  - "Debt accumulation is the highest perceived financial risk."
  - "Consumer spending patterns are significantly linked to perceived financial risk."
  - "Data can inform cold-start behavioral profiles and debt management design."
```
---

## Paper 23: Ruiz et al_summarized.md

**Source File:** `Ruiz et al_summarized.md`

```yaml
paper_id: 10.62986/dp2025.60
designation: local
title: Election-Year Stimuli and Economic Performance: Evidence from a Macroeconometric Model of the Philippines
authors: Ruiz, M. G. C.; Miral, R. M. L.; Rivera, J. P. R.
year: 2025
venue: PIDS Discussion Paper Series
odin_topics:
  - 2.B
  - 4.B
  - 6.A
  - 7.A
  - 8.A
  - 12.A
  - 12.B
tldr: Election years generate short-term, demand-driven expansions in the Philippine economy, but these effects are transitory and revert to baseline levels post-election.
problem_and_motivation: Existing macroeconometric models for the Philippines lack explicit integration of political and institutional shocks, particularly election-induced fluctuations. This limits policymakers' ability to distinguish between temporary election-driven booms and sustainable growth drivers. The study addresses this gap by augmenting a model to quantify how election shocks transmit through the economy.
approach:
  - Augmented a small macroeconometric model for the Philippines using quarterly data from 2002Q1 to 2023Q4.
  - Behavioral equations were estimated using the ARDL method in ECM form with lag lengths selected via AIC.
  - Cointegration was tested using the bounds test approach; specifications were chosen to align with economic theory.
  - Included a dummy variable for the COVID-19 pandemic period (2020Q2-2021Q2) to control for structural disruption.
  - Introduced election spending shocks as impulse shocks to private consumption and government consumption equations, simulating pre-election demand surges.
findings:
  - Election shocks generate short-term expansions in private consumption (8-18% above baseline), employment (~2.7%), investment (4-11%), and government consumption (7-15%).
  - These effects are transitory; economic activity reverts near baseline levels post-election as fiscal impulses fade.
  - Pre-election spending boosts are driven by fiscal frontloading, campaign activities, and temporary job creation, aligning with political business cycle theory.
  - Election-driven growth is cyclical rather than structural and may induce inefficiencies in expenditure allocation and fiscal discipline.
  - The model demonstrates reasonable predictive accuracy with MAPEs for GDP components ranging from 2% to 10%, and MAEs for rates within acceptable margins.
key_figures_tables:
  - Figure 2: In-sample simulations tracking actual vs. forecasted macroeconomic variables → Model tracks actual data well across most aggregates.
  - Table 2: Forecast accuracy metrics for 2021Q1-2023Q4 → MAPEs under 10% for most level variables; MAEs for rates remain modest.
  - Figure 3: Election spending shock scenario simulations → Consumption and employment spike temporarily, then revert to baseline.
  - Table 3: Validation of empirical results against scholarly literature → Results align with PBC theory on magnitude, timing, and persistence.
key_equations:
  - equation: \log C_t = f(\log(YD_t), \pi_t^e, r_t - \pi_t, \pi_t)
    explanation: Household consumption depends on disposable income, expected inflation, real rate, and inflation.
  - equation: \log I_t = f(\log(Y_t), \Delta(r_t - \pi_t), \pi_t)
    explanation: Investment depends on output, change in real rate, and inflation.
  - equation: \Delta \log(CPI_t) = f(\Delta \log(p_t^{oil}), \Delta \log(p_t^{rice}), \Delta \log(D_t), \Delta \log(xrr_t))
    explanation: CPI inflation is a function of oil prices, rice prices, debt, and real exchange rate.
  - equation: PB_t \equiv RV_t - XP_t
    explanation: Primary balance is revenues minus primary expenditures.
definitions:
  - term: PBC
    definition: Political business cycles; electoral manipulation of fiscal/monetary tools for reelection.
  - term: ARDL
    definition: Autoregressive Distributed Lag; econometric method for cointegration analysis.
  - term: ECM
    definition: Error Correction Model; captures short-run dynamics and long-run equilibrium.
  - term: MAPE
    definition: Mean absolute percentage error; forecast accuracy metric for level variables.
  - term: MAE
    definition: Mean absolute error; forecast accuracy metric for rate/percentage variables.
  - term: PPP
    definition: Public-Private Partnership; infrastructure projects exempt from election spending ban.
critical_citations:
  - "[Rogoff and Sibert, 1988] — Foundational PBC theory on pre-election fiscal expansions."
  - "[Brender and Drazen, 2005] — Political budget cycles differ across established vs. new democracies."
  - "[Drazen and Eslava, 2010] — Electoral manipulation via voter-friendly spending in developing economies."
  - "[Shi and Svensson, 2006] — Cross-country evidence on political budget cycles and determinants."
  - "[Debuque-Gonzales and Corpus, 2023, 2024] — Base macroeconometric model framework for the Philippines."
relevance:
  topics:
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: high
      justification: Directly models election-driven cyclical spending surges in the Philippine economy.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Explicitly addresses the gap in Philippine models regarding election shocks.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Uses macroeconometric forecasting to simulate election shock effects.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Provides evidence on fiscal policy impacts relevant to budget recommendations.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Election shocks are fiscal anomalies; provides context for detecting abnormal spending patterns.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Demonstrates model evaluation with MAPE/MAE and in-sample simulations.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Evaluates the performance of the macroeconometric model's forecasting accuracy.
  contribution: This paper provides a validated macroeconometric framework that can inform Odin's forecasting module (6.A) by demonstrating how exogenous shocks like elections propagate through demand-side variables. It offers empirical justification for incorporating political cycle signals into predictive models, supporting Odin's behavioral profiling and anomaly detection features. The finding that election effects are transitory and demand-driven directly justifies the need for Odin to distinguish between cyclical anomalies and structural spending changes in user data. The paper's emphasis on fiscal transparency and counter-cyclical policies aligns with Odin's design for user trust and long-term stability.
  directly_justifies:
    - "Election shocks generate short-term demand-driven expansions in consumption, investment, and employment."
    - "Election-related economic activity is cyclical and reverts to baseline post-election."
    - "Government consumption expands by 7-15% in pre-election quarters and normalizes afterward."
    - "Pre-election fiscal expansions may distort expenditure allocation and fiscal discipline."
  limits:
    - "Model stability issues due to structural breaks like GFC and COVID-19 may affect long-run relationships."
    - "Simplified dummy variable for COVID-19 may not fully capture pandemic-induced behavioral shifts."
    - "Post-COVID structural changes (digital transformation, altered spending patterns) may not be fully reflected."
    - "Sectoral-level impacts are not disaggregated; only aggregate GDP components are analyzed."
    - "Qualitative influence of election outcomes (candidate characteristics) is not modeled."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The Filipino Cultural Context domain was flagged as relevant via 2.B (Seasonal and Cyclical Spending Patterns) with high relevance, as the paper directly models election cycles—a recurring seasonal phenomenon in the Philippines. The Existing Systems & Gaps domain was flagged via 4.B (Limitations and Gaps) with high relevance, as the paper explicitly identifies and addresses the gap in Philippine macroeconometric models regarding political shocks. Spending Forecasting was flagged via 6.A (Predictive Modeling) with medium relevance due to the use of forecasting to simulate shock effects. Budget Recommendation was flagged via 7.A (Budgeting Strategies) with medium relevance because the paper provides empirical evidence on fiscal policy impacts. Anomaly Detection was flagged via 8.A (Anomaly Detection) with contextual relevance, as election shocks provide a context for identifying abnormal fiscal patterns. System Evaluation was flagged via 12.A and 12.B with medium relevance, as the paper evaluates model performance. Domains such as Expense Categorization (3), Behavioral Profiling (5), Mobile-First Design (9), Data Privacy (10), User Retention (11), and Savings/Debt Management (13) were considered but rejected as the paper does not address these specific operational aspects of personal finance systems. Borderline cases: the paper touches on both 2.B (cyclical patterns) and 2.D (Filipino spending cycles/occasions), but 2.B was chosen as the primary code since the analysis focuses on cyclical timing rather than cultural occasion-specific practices. Overall, the paper is highly relevant for Odin's understanding of macroeconomic context and political-economic signals that can influence individual spending behavior, but its direct applicability is limited to informing model calibration and contextual awareness rather than end-user features.
limitations:
  - "Model stability and specification issues due to structural breaks like GFC and COVID-19 may have introduced parameter instability. [unacknowledged]"
  - "Simplified dummy variable treatment of COVID-19 may not fully capture the depth and persistence of pandemic-induced disruptions. [unacknowledged]"
  - "Post-pandemic structural changes (digital transformation, altered spending patterns) may not be fully reflected in the model calibrated on pre-2020 relationships. [acknowledged]"
  - "Sectoral-level impacts are not estimated; only aggregate GDP components are analyzed. [acknowledged]"
  - "Qualitative influence of election outcomes, such as leadership attributes, is not modeled. [acknowledged]"
  - "The model's usability for real-time private-sector decision-making is limited relative to simpler forecasting tools. [acknowledged]"
remember_this:
  - "Election-year consumption surges 8-18% above baseline but quickly reverts."
  - "Employment rises ~2.7% during election quarters, then normalizes post-election."
  - "Government spending increases 7-15% before elections, followed by fiscal contraction."
  - "Election-driven growth is cyclical and demand-driven, not structural."
  - "Fiscal frontloading may distort expenditure allocation and long-term development."
```
---

## Paper 24: Conales_summarized.md

**Source File:** `Conales_summarized.md`

```yaml
paper_id: 10.64753/jcasc.v10i2.1862
designation: local
title: Examining Debt and Financial Literacy Through a Cultural Lens: Educators’ Sustainable Household Practices in Marawi
authors: Conales, M. P.
year: 2025
venue: Journal of Cultural Analysis and Social Change
odin_topics:
  - 1.A
  - 1.C
  - 2.A
  - 2.C
  - 4.A
  - 5.A
  - 10.A
  - 13.A
  - 13.B
tldr: A survey of HEI educators in Marawi reveals gaps in compound interest and debt literacy, with Muslim respondents scoring lower, while financial behavior is the strongest predictor of sound household financial management practices.
problem_and_motivation: Higher education institution (HEI) educators in the Philippines face rising indebtedness and financial stress, yet research on their financial literacy and management practices, especially in culturally distinct contexts like Marawi, is scarce. The study aims to assess financial and debt literacy, their links to household practices, and the moderating role of socio-cultural and religious factors, which are often overlooked in Western-centric models.
approach:
  - A descriptive and correlational research design was employed using a survey administered to 259 tertiary educators from Mindanao State University-Marawi, selected via stratified random sampling.
  - The survey instrument measured financial knowledge, behavior, and attitude (World Bank, 2015), debt literacy (Lusardi & Tufano, 2009), and household financial management practices (Hilgert et al., 2003).
  - Data analysis utilized descriptive statistics and Partial Least Squares Structural Equation Modeling (PLS-SEM) via SmartPLS to test relationships and moderating effects.
  - The conceptual framework integrated Islamic finance principles and socio-cultural capital theory to extend traditional economic models.
  - The study is grounded in a post-conflict, predominantly Muslim context, examining how religious norms shape financial behaviors and literacy.
findings:
  - Educators answered 5.6 out of 7 financial knowledge questions correctly on average, with the lowest scores on compound interest and inflation.
  - Only 9% of respondents answered all three debt literacy questions correctly, indicating widespread debt illiteracy.
  - Muslim respondents scored significantly lower than non-Muslims in both financial knowledge and debt literacy.
  - Financial behavior emerged as the strongest and most consistent predictor of cash flow, credit, investment, and savings management (β = 0.154–0.196, p < .05 to p < .001).
  - num: 73% of respondents own their homes and 71% own vehicles, but only 25.5% have diversified investments and 12.4% invest in the stock market.
  - Financial knowledge showed no significant effect on any financial management dimension, underscoring a knowledge-action gap.
key_figures_tables:
  - Table 3: Financial behavior results → Budgeting is the highest-scored behavior, while financial product ownership is the lowest.
  - Table 7: Debt literacy quiz results → Only 18.2% answered the credit card debt payoff question correctly, the lowest.
  - Table 8: Overall debt literacy score → 38.6% of respondents answered none of the three debt questions correctly.
  - Table 11: Path coefficients → Financial behavior significantly affects all household management practices, knowledge does not.
  - Table 10: Financial management practices → 85.3% have savings accounts, but only 35.9% invest money from each paycheck.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: HEI
    definition: Higher Education Institution.
  - term: PLS-SEM
    definition: Partial Least Squares Structural Equation Modeling, a statistical technique for testing complex theoretical models.
  - term: Riba
    definition: Islamic prohibition of interest, shaping debt and investment behaviors.
critical_citations:
  - "[Lusardi & Tufano, 2009] — Foundational framework for measuring debt literacy used in the study."
  - "[World Bank, 2015] — Source of the financial literacy measurement instrument."
  - "[Hilgert et al., 2003] — Framework for household financial management practices adopted in the research."
  - "[Casingal & Ancho, 2021] — Highlights financial vulnerability and indebtedness among Philippine teachers."
  - "[Fadillah & Lubis, 2024] — Supports integration of Islamic finance principles into financial capability research."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: "The study's respondents are HEI educators in the Philippines, a key demographic segment."
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: "Directly measures financial knowledge, attitudes, and behaviors of educators."
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: "Explicitly examines how Islamic religious norms (e.g., riba prohibition) shape financial practices."
    - code: 2.C
      name: User-Declared Financial Preferences
      relevance: medium
      justification: "Explores financial attitudes and preferences, including saving orientation and risk perception."
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: "Provides context on financial product engagement (e.g., low credit card ownership in Muslim areas)."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: "Identifies distinct behavioral patterns and their relationship to financial outcomes."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: "While not directly on data privacy, the study highlights cultural sensitivities around financial data."
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: "Examines savings behavior and long-term goal setting among educators."
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: "Directly investigates debt literacy and credit management practices."
  contribution: "The study provides empirical evidence that financial behavior, not just knowledge, is the primary driver of effective household financial management among Filipino educators. It reinforces the need for Odin to prioritize behavioral interventions and habit formation over purely informational content. The findings also highlight the importance of culturally sensitive design, particularly in Muslim-majority contexts, where interest-free and Sharia-compliant financial products may be preferred. This directly informs Odin's approach to expense categorization, savings goal management, and debt management modules, ensuring they are adaptable to diverse cultural and religious backgrounds."
  directly_justifies:
    - "Financial behavior is a stronger predictor of financial management outcomes than financial knowledge."
    - "Debt literacy is particularly low among educators in culturally distinct Philippine contexts."
    - "Muslim respondents show lower conventional debt literacy due to religious influences."
    - "There is a significant gap in engagement with financial products and investment opportunities."
  limits:
    - "The study is limited to HEI educators in Marawi, and findings may not be generalizable to other demographics or regions."
    - "The cross-sectional design does not establish causality between financial literacy components and management practices."
    - "The instruments may not fully capture culturally-specific financial practices like informal lending or community-based savings."
    - "The use of self-reported data is subject to social desirability and recall bias."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was conducted. The paper was flagged as highly relevant for domains related to Filipino Cultural Context (specifically 2.A and 2.C), Behavioral Profiling (5.A), and Savings & Debt Management (13.A, 13.B), as it provides direct empirical evidence on financial behaviors, attitudes, and knowledge gaps among a Filipino demographic. Medium relevance was assigned to 1.C and 2.C based on behavioral data, and low relevance to 4.A due to contextual system landscape mentions. Borderline cases included the paper's discussion of seasonal spending (2.B), which was not a primary focus, and user-declared constraints (3.C), which were not directly addressed. The paper's examination of financial attitudes (2.C) and behaviors (1.C) also intersected with domain 5.A, and these were prioritized as high relevance. Domains like Mobile-First Design (9.A, 9.B), Anomaly Detection (8.A-C), and System Evaluation (12.A-C) were considered and rejected as the paper offers no direct insights into these technical design or evaluation areas. The paper's findings on the knowledge-action gap and the influence of culture on debt literacy are directly applicable to Odin's module design, particularly for behavioral profiling and culturally adaptive financial features. Overall, the paper is highly relevant for informing Odin's approach to understanding user behavior and tailoring financial management tools to the Filipino context."
limitations:
  - "The study relies on cross-sectional data; causal relationships cannot be inferred from the correlational analysis. [unacknowledged]"
  - "The sample is limited to educators from a single university, which may not be representative of all Filipino young professionals."
  - "The research instruments, while validated, may not fully capture the nuances of Islamic financial practices or informal credit systems. [unacknowledged]"
  - "The low R-squared values for some constructs in the SEM model suggest that unmeasured variables may also influence financial management practices."
  - "Social desirability bias may have affected self-reported financial behaviors and attitudes."
remember_this:
  - "Financial behavior is the strongest predictor of financial management outcomes."
  - "Only 9% of educators demonstrated debt literacy across all items."
  - "Muslim respondents showed lower conventional financial and debt literacy."
  - "Financial knowledge alone does not improve household financial management."
  - "Most educators lack diversified investment portfolios despite home ownership."
```
---

## Paper 25: Sarmiento et al_summarized.md

**Source File:** `Sarmiento et al_summarized.md`

```yaml
paper_id: 10.69569/jip.2025.630
designation: local
title: Financial Edutainment: The Effect of Social Media Usage on the Financial Literacy of Students in Bulacan
authors: Sarmiento, A. G.; Rivera, L. M.; Cortez, W. T.
year: 2025
venue: Journal of Interdisciplinary Perspectives
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 3.A
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 9.A
  - 10.A
  - 10.B
  - 11.A
  - 12.A
tldr: Social media usage has a statistically significant positive effect on the financial literacy of students in Bulacan, particularly in budgeting and debt management, explaining 68.9% of the variance in financial literacy.
problem_and_motivation: Filipino young professionals increasingly rely on unregulated social media content for financial guidance, creating a risk of exposure to misinformation. Although social media usage is high, definitive evidence on whether financial edutainment improves literacy or fosters confusion is missing. This gap leaves students vulnerable to unverified advice in the absence of comprehensive financial education in schools.
approach:
  - A causal research design was employed using a structured survey questionnaire adopted from validated instruments.
  - The study surveyed 556 students in Bulacan selected through purposive sampling.
  - Data were analyzed using descriptive statistics (mean and standard deviation) and linear regression.
  - The questionnaire measured social media usage (usefulness, ease of use, risks, compatibility) and financial literacy (budgeting, debt, spending, savings).
  - Linear regression was used to model the relationship between social media usage and financial literacy.
findings:
  - num: 68.9% of the variance in students' financial literacy is explained by their social media usage (R² = 0.689).
  - num: Social media has the strongest effect on budgeting (β = 0.751, R² = 0.667) and managing debt (β = 0.719, R² = 0.629).
  - Most students (36.33%) spend 5-6 hours daily on social media, with TikTok and Facebook being the most popular platforms for financial content.
  - Students passively consume financial content several times a month but are less proactive in seeking it actively.
  - Students perceive social media as moderately useful and easy to use for financial learning but acknowledge privacy and security risks.
  - Social media is more effective as a motivational tool for saving than as an educational resource for developing new strategies.
key_figures_tables:
  - Table 1: Demographic profile of 556 respondents → Most respondents are aged 19-21 and spend over 5 hours daily on social media.
  - Table 2: Social media platform ranking → TikTok is the most used platform for financial content, followed by Facebook.
  - Figure 1: Frequency of viewing financial content → Most students view financial content several times a month.
  - Figure 2: Frequency of actively searching for financial content → Most students search about once a month.
  - Table 3: Social media usage perceptions → Students agree social media is useful but have security concerns.
  - Table 4: Financial literacy levels → Students agree social media positively affects budgeting, debt, spending, and savings.
  - Table 5: Regression results → Social media has a significant positive effect on all financial literacy components.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: Financial edutainment
    definition: The presentation of financial knowledge in interactive and entertaining forms such as short videos, memes, and influencer material.
  - term: Finfluencer
    definition: A social media influencer who provides financial advice or content to followers.
  - term: Purposive sampling
    definition: A non-probability sampling method where researchers select participants based on their judgment and the study's objectives.
critical_citations:
  - "[BSP, 2023] — Only 25% of Filipino youth are financially literate."
  - "[Cabral et al., 2024] — Source of financial literacy questions."
  - "[Cao et al., 2020] — Source of social media usage questions."
  - "[Iranto et al., 2023] — Social media use increases impulsive buying, literacy reduces it."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "high"
      justification: "Study directly focuses on Filipino students aged 19-21, the core demographic for Odin."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "medium"
      justification: "Examines budgeting, debt, spending, and savings behaviors of students."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Investigates how social media influences financial behaviors like spending and saving."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "medium"
      justification: "Explores how Filipino students use social media for financial guidance, a culturally specific practice."
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "low"
      justification: "While not directly addressed, the study on spending habits could inform cyclical patterns."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "contextual"
      justification: "Focuses on financial literacy components including budgeting and spending, which relate to categorization."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses social media as an informal financial education system and gaps in formal education."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Highlights the gap between formal financial education and reliance on unverified social media content."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Examines student behavior profiles related to social media consumption and financial literacy."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "low"
      justification: "Not directly addressed but students' passive vs. active seeking behavior could relate to cold-start."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "contextual"
      justification: "Highlights high social media usage on mobile, indicating a mobile-first context for financial content."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "Students reported significant privacy and security concerns about using social media for finances."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "high"
      justification: "The study directly measures students' trust levels and risk perceptions related to online financial information."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "medium"
      justification: "Examines passive consumption patterns, providing insights into user engagement with financial content."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Uses regression analysis to evaluate the effect of social media usage on financial literacy."
  contribution: "This paper informs Odin's design by establishing that social media usage is a significant predictor of financial literacy among Filipino students, explaining 68.9% of the variance in financial literacy. This justifies Odin's integration of social media-derived behavioral data for user profiling. The strong effect on budgeting and debt management validates Odin's focus on these modules. The findings on user risk perceptions inform Odin's data privacy and trust protocols. The regression methodology offers a potential evaluation framework for Odin's own algorithmic modules, particularly for assessing user engagement."
  directly_justifies:
    - "Social media usage significantly predicts financial literacy across budgeting, debt, spending, and savings."
    - "Passive exposure to financial content may be more impactful than active seeking for improving financial literacy."
    - "Users have significant privacy and security concerns when using digital platforms for financial purposes."
    - "Social media is a primary channel for financial learning among Filipino students, surpassing formal education in reach."
  limits:
    - "Causal inference is limited due to the cross-sectional design and use of self-reported data."
    - "The study focuses on students in Bulacan, which may not generalize to other Filipino regions."
    - "Financial literacy was measured via self-perception rather than objective performance tests."
    - "The survey instrument used a 4-point Likert scale, which does not capture neutral attitudes. [unacknowledged]"
    - "Purposive sampling may introduce selection bias, limiting the generalizability of findings. [unacknowledged]"
  mapping_rationale: "A systematic scan of all 12 functional domains and associated topic codes was conducted. The domains of 'Filipino Cultural Context', 'Expense Categorization', 'Existing Systems & Gaps', 'Behavioral Profiling', 'Data Privacy & User Trust', and 'User Retention & Engagement' were flagged as relevant. Specifically, topic codes 1.A and 1.C were assigned high relevance as the paper directly addresses the demographic and financial behavior of Filipino students. Codes 4.B and 10.A were also deemed highly relevant due to the paper's direct investigation of gaps in formal education and user privacy concerns on social media. Codes like 3.A were considered contextual, as the study deals with broad literacy components rather than specific categorization frameworks. Codes related to algorithmic forecasting (6.A, 6.B), optimization (7.A-D), and anomaly detection (8.A-C) were rejected as they are not addressed. The paper provides a foundational understanding of user behavior and literacy gaps in the Filipino context, supporting Odin's user profiling and trust considerations, but it does not offer algorithmic insights."
limitations:
  - "The cross-sectional design limits causal inference."
  - "Findings may not generalize to Filipino young professionals outside of Bulacan."
  - "Financial literacy is measured through self-perception rather than objective assessment."
  - "The 4-point Likert scale fails to capture neutral or undecided attitudes. [unacknowledged]"
  - "Purposive sampling may introduce selection bias. [unacknowledged]"
  - "Social media usage and financial literacy are measured concurrently, not longitudinally. [unacknowledged]"
remember_this:
  - "Social media usage explains 68.9% of the variance in student financial literacy."
  - "Social media most strongly influences budgeting and debt management skills."
  - "Students consume financial content passively but are less likely to actively seek it."
  - "Privacy and security concerns significantly affect user trust in online financial information."
  - "Social media serves as a primary informal financial education channel for Filipino students."
```
---

## Paper 26: Dimaunahan et al_summarized.md

**Source File:** `Dimaunahan et al_summarized.md`

```yaml
paper_id: "10.1016/j.actpsy.2025.105334"
designation: "local"
title: "Financial literacy and sustainable planning assessment among Filipino millennials"
authors: "Dimaunahan, D. S. F.; Santiago, A. F. B.; Eusebio, M. C. C.; Loteriña, S. M. M.; Ong, A. K. S.; Chavez, J. X. S."
year: 2025
venue: "Acta Psychologica"
odin_topics:
  - "1.A"
  - "1.B"
  - "1.C"
  - "2.A"
  - "2.B"
  - "2.D"
  - "4.A"
  - "4.B"
  - "5.A"
  - "5.B"
  - "5.C"
  - "7.A"
  - "7.B"
  - "11.A"
  - "11.B"
  - "12.A"
  - "13.A"
tldr: "Filipino millennials exhibit low financial literacy, which does not directly influence financial planning, while monthly income, occupation, and monthly expenses significantly affect planning behaviors."
problem_and_motivation: "Financial literacy among Filipinos is critically low, yet limited publicly available studies examine its influence on financial planning for millennials. The lack of research linking financial literacy, demographic factors, and goal-setting theory in the Philippine context creates a gap in understanding sustainable financial behavior. Addressing this gap is essential for designing effective financial inclusion and education strategies."
approach:
  - "A correlational research design was employed using data from 400 Filipino millennials in Makati City."
  - "Financial literacy was measured using Lusardi and Mitchell's 'Big Three' questions on interest compounding, inflation, and risk diversification."
  - "Goal Setting Theory (Locke & Latham, 1990) framed financial planning through goal commitment, specificity, acceptance, and difficulty."
  - "Demographic factors included monthly income, occupation, and monthly expenses as lower-order constructs."
  - "Structural equation modeling (PLS-SEM) was used to analyze relationships and test four hypotheses."
findings:
  - "num: Only 54.5% answered the interest compounding question correctly, 38.8% for inflation, and 33.8% for risk diversification."
  - "Financial literacy did not have a significant direct effect on financial planning (β = 0.077, p = 0.153)."
  - "Monthly expenses had the strongest significant effect on financial planning (β = 0.205, p = 0.001)."
  - "Monthly income significantly affected financial planning (β = 0.180, p = 0.003), followed by occupation (β = 0.164, p = 0.004)."
  - "Goal acceptance was the most significant higher-order construct affecting financial planning (β = 0.924, p < 0.001)."
  - "Goal commitment (β = 0.809), goal specificity (β = 0.597), and goal difficulty (β = 0.212) all had significant effects on financial planning."
  - "The study found that Filipino millennials engage in financial planning despite low financial literacy, driven by personal needs and goals."
key_figures_tables:
  - "Table 1: Demographic profile shows 53% female, 71.3% employed full-time, 67.6% with bachelor's degrees → sample is urban, educated, and employed."
  - "Table 2: Statistical analysis reveals low financial literacy scores across all three 'Big Three' questions → confirms limited understanding of basic economic concepts."
  - "Table 7: Summarized results show financial literacy insignificant (β=0.077), monthly expenses most significant (β=0.205) → demographic factors drive planning more than literacy."
  - "Figure 3: Final SEM model depicts significant pathways from demographics and goal-setting constructs to financial planning → highlights goal acceptance as strongest predictor."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Financial Literacy"
    definition: "Understanding of financial management knowledge and skills, enabling regulation of investments and money management to reach financial goals."
  - term: "Financial Planning"
    definition: "The process of assessing financial goals, taking inventory of assets, determining life goals, and taking necessary steps to achieve them."
  - term: "Goal Setting Theory"
    definition: "A theoretical framework stating that specific and challenging goals, combined with commitment and feedback, enhance performance."
  - term: "Goal Commitment"
    definition: "An individual's determination to pursue and achieve a specific goal."
  - term: "Goal Specificity"
    definition: "The clarity and precision with which a goal is defined, eliminating ambiguity."
  - term: "Goal Acceptance"
    definition: "An individual's willingness to adopt and internalize a goal as their own."
  - term: "Goal Difficulty"
    definition: "The perceived challenge or effort required to attain a goal."
  - term: "The Big Three"
    definition: "Three financial literacy questions covering interest compounding, inflation, and risk diversification, developed by Lusardi and Mitchell."
  - term: "SEM"
    definition: "Structural equation modeling, a multivariate statistical technique for analyzing relationships between variables."
critical_citations:
  - "[Lusardi & Mitchell, 2011] — Provides the standardized 'Big Three' financial literacy measure used in the study."
  - "[Locke & Latham, 1990] — Foundational theory for goal-setting moderators applied to financial planning."
  - "[Mohta & Shunmugasundaram, 2022] — Reports millennial financial literacy levels globally, supporting low-literacy findings."
  - "[Banko Sentral ng Pilipinas, 2018] — Provides baseline data on Filipino household financial behavior and access."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "high"
      justification: "Directly studies Filipino millennials, the core user group for Odin."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "high"
      justification: "Examines income, expenses, and occupation as key financial structure variables."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Assesses financial planning behaviors and goal-setting in the target demographic."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "medium"
      justification: "Discusses Filipino financial behaviors and low literacy within a cultural context."
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "medium"
      justification: "Monthly expense analysis implies recurring spending cycles relevant to Filipino households."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "low"
      justification: "Monthly expense patterns are broadly relevant but not focused on specific occasions."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Provides context on financial literacy levels that PFMS systems must address."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Identifies low literacy and poor planning as gaps that Odin must bridge."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Links financial literacy to planning behavior, relevant to profiling."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "contextual"
      justification: "Demographic factors are highlighted as significant, informing cold-start baselines."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "low"
      justification: "Does not propose classification methods but provides behavioral insights."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "medium"
      justification: "Monthly expense management is central to budgeting and is significantly correlated with planning."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Findings on demographic influences can inform personalized budget recommendations."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "contextual"
      justification: "Goal-setting framework offers insights into user engagement through goal pursuit."
    - code: "11.B"
      name: "Retention Mechanisms and Engagement Design"
      relevance: "low"
      justification: "Goal commitment and specificity findings can inform retention strategies."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "low"
      justification: "Provides a baseline correlation framework applicable to system evaluation."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "medium"
      justification: "Goal-setting theory is applied to saving and planning, directly relevant to savings management."
  contribution: "This paper validates that for Filipino millennials, financial planning is primarily driven by demographic factors (income, expenses, occupation) and goal-setting constructs, rather than financial literacy itself. Odin's budget recommendation module can use these demographic predictors for initial personalization. The goal-setting framework (commitment, specificity, acceptance, difficulty) offers a validated structure for Odin's goal management and engagement features. The low financial literacy findings underscore the need for Odin to incorporate financial education and simplified interfaces rather than assuming user sophistication."
  directly_justifies:
    - "Financial literacy does not significantly affect financial planning for Filipino millennials."
    - "Monthly income and expenses are significant predictors of financial planning behavior."
    - "Goal acceptance and commitment are strong predictors of financial planning."
    - "Filipino millennials demonstrate low understanding of interest compounding, inflation, and risk diversification."
    - "Occupation type influences saving rates and financial planning capacity."
  limits:
    - "Sample limited to Makati City, not representative of rural or other urban areas."
    - "Study focused solely on millennials; findings may not generalize to other generations."
    - "Used only 'The Big Three' financial literacy measure, excluding other dimensions."
    - "Relied on self-reported data, which may introduce social desirability bias."
    - "Cross-sectional design cannot establish causality."
  mapping_rationale: "A systematic scan across Odin's 12 functional domains and their associated canonical topic codes was conducted. The paper was flagged as highly relevant to domain 1 (Filipino Cultural Context) for codes 1.A, 1.B, 1.C, as it directly studies Filipino millennials' financial structure and behavior. Domain 2 (Expense Categorization) codes 2.A, 2.B, 2.D were assigned medium/low relevance due to the focus on monthly expenses and spending cycles, though not on specific cultural practices or occasions. Domain 4 (Existing Systems & Gaps) codes 4.A and 4.B were rated medium/high because the paper identifies low literacy and poor planning as gaps that PFMS systems must address. Domain 5 (Behavioral Profiling) codes 5.A, 5.B, 5.C received contextual to medium relevance for linking literacy to behavior and demographic factors. Domain 7 (Budget Recommendation) codes 7.A and 7.B were rated medium due to the direct relevance of monthly expenses and demographic influences on budgeting. Domain 11 (User Retention & Engagement) codes 11.A and 11.B were contextual/low based on the goal-setting framework's applicability. Domain 13 (Savings & Debt Management) code 13.A was medium because goal-setting for savings is a core theme. Domains 3 (Expense Categorization Design), 6 (Spending Forecasting), 8 (Anomaly Detection), 9 (Mobile-First Design), 10 (Data Privacy & User Trust), and 12 (System Evaluation) were considered rejected as the paper does not address these domains. The overall relevance is high for understanding the financial behavior and planning determinants of Odin's target user base, despite the paper not proposing algorithmic solutions."
limitations:
  - "Sample limited to Makati City, not representative of rural or other urban areas."
  - "Study focused solely on millennials; findings may not generalize to other generations."
  - "Used only 'The Big Three' financial literacy measure, excluding other dimensions."
  - "Relied on self-reported data, which may introduce social desirability bias."
  - "Cross-sectional design cannot establish causality."
remember_this:
  - "Filipino millennials show low financial literacy on basic economic concepts."
  - "Financial literacy does not directly affect financial planning for this demographic."
  - "Monthly income, expenses, and occupation significantly drive financial planning."
  - "Goal acceptance is the strongest predictor of financial planning behavior."
  - "Only 33.8% understood risk diversification, highlighting a critical knowledge gap."
```
---

## Paper 27: Gabatin et al_summarized.md

**Source File:** `Gabatin et al_summarized.md`

```yaml
paper_id: 10.1145/3760557.3760578
designation: local
title: Understanding the Impulse Buying Behavior in the Digital Age: Influential Factors in Online Consumer Behavior
authors: Gabatin, R. A.; Sierra, S. M.; Maniago, M. G.; Capole, A.; Torres, R.
year: 2025
venue: 16th International Conference on E-business, Management and Economics (ICEME 2025)
odin_topics:
  - 1.C
  - 2.A
  - 2.D
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 9.A
  - 9.B
tldr: Social and website factors drive impulse buying by influencing urgency and consumer characteristics, not directly through marketing or direct social pressure.
problem_and_motivation: Understanding impulse buying is crucial for businesses, yet the specific interplay of social, marketing, and website-related factors in the digital age remains unclear, especially within the Filipino market. Existing literature lacks a comprehensive model that integrates these elements with consumer characteristics and urgency within the SOR framework.
approach:
  - The study uses a quantitative, correlational research design to examine impulse buying behavior.
  - It employed a structured survey distributed to 381 purposively sampled respondents from Cabuyao, Laguna.
  - Data was analyzed using Partial Least Squares Structural Equation Modeling (PLS-SEM) in WarpPLS 8.0.
  - The measurement model was validated using Composite Reliability, Cronbach's Alpha, and Average Variance Extracted (AVE).
  - The structural model assessed direct, mediating, and moderating effects with path coefficients and effect sizes.
findings:
  - num: Social-related factors have a significant large effect on website-related factors (β=0.868, p<0.001).
  - num: Marketing-related factors significantly affect consumer characteristics with a large effect size (β=0.714, p<0.001).
  - num: Urgency to buy has a significant large direct effect on impulse buying (β=0.804, p<0.001).
  - num: Consumer characteristics significantly affect urgency to buy with a large effect (β=0.562, p<0.001).
  - num: The model explains 80.4% of the variance in impulse buying (R²=0.804).
  - Social and marketing factors do not directly drive impulse buying but act through website usability and consumer characteristics.
  - Age and gender did not significantly moderate the urgency-impulse buying relationship.
key_figures_tables:
  - Figure 1: Conceptual Framework based on SOR theory → Outlines the hypothesized relationships among all study variables.
  - Figure 2: Final Model after removing insignificant paths → Highlights website usability and urgency as key direct drivers of impulse buying.
  - Table 1: Convergent Validity and Reliability Measures → Confirms all constructs met the required AVE and reliability thresholds.
  - Table 4: Evaluation of the Structural Model with path coefficients → Reports direct, mediating, and moderating effects for all hypotheses.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: SOR Framework
    definition: Stimulus-Organism-Response framework explaining how external stimuli influence internal states leading to behavioral responses.
  - term: Impulse Buying
    definition: Spontaneous and unplanned purchasing behavior driven by emotional triggers and external stimuli.
  - term: PLS-SEM
    definition: Partial Least Squares Structural Equation Modeling, a statistical technique for analyzing complex cause-effect relationship models.
critical_citations:
  - "[Cohen, 1988] — Defines thresholds for effect sizes (R²) used to validate model predictive accuracy."
  - "[Hair et al., 2006] — Provides the methodological standard for multivariate data analysis used in the study."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly investigates impulse buying behavior, a key aspect of financial behavior for young professionals.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Acknowledges that impulse buying in the Philippine market is shaped by cultural and social influences.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: The study's focus on impulse buying can be contextualized within Filipino spending cycles, though not explicitly studied.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Informs the landscape by highlighting how e-commerce and marketing strategies encourage unplanned spending.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: low
      justification: Identifies a gap in understanding the interplay of factors driving impulse buying, which PFMS could address.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Discusses consumer characteristics like shopping lifestyle and impulsivity, which are key to behavioral profiling.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Utilizes a quantitative approach to classify and relate factors (e.g., social, marketing) to behavioral outcomes.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Findings on website-related factors (ease of use, payment) are directly applicable to mobile-first design principles.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: high
      justification: Provides empirical evidence that website usability and seamless payment processes drive urgency and unplanned purchases.
  contribution: The study's findings on impulse buying can inform Odin's anomaly detection module by identifying behavioral patterns (like urgency-driven purchases) that deviate from a user's norm. Its insights on website usability and consumer characteristics can directly justify Odin's mobile-first design choices, emphasizing the need for a frictionless UX to reduce the likelihood of impulsive financial decisions. The SOR framework provides a theoretical basis for modeling how external stimuli (e.g., app notifications, offers) might influence user financial behavior within Odin. The confirmation that urgency strongly drives impulse purchases suggests that Odin's budget recommendation system could be designed to counteract such urgency with real-time feedback or savings prompts. Finally, the understanding of consumer characteristics (like shopping lifestyle) can guide the personalization of financial advice and alerts within Odin.
  directly_justifies:
    - "Website usability and seamless payment processes significantly increase the likelihood of unplanned purchases."
    - "Urgency to buy is a powerful direct driver of impulse buying behavior."
    - "Social-related factors influence consumer perception of website-related factors like ease of use."
    - "Consumer characteristics such as shopping lifestyle play a significant role in shaping impulse buying."
  limits:
    - "The study is geographically limited to respondents from Cabuyao, Laguna, which may not represent the broader Filipino population."
    - "It relies on self-reported survey data, which is subject to social desirability and recall bias. [unacknowledged]"
    - "The cross-sectional design can establish relationships but not causality. [unacknowledged]"
    - "The focus on impulse buying in general e-commerce may not directly translate to a personal finance management context."
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The paper's core focus on consumer behavior in a digital environment directly maps to understanding the financial behavior (1.C) and cultural practices (2.A) of the target demographic. The examination of website-related factors and user experience provides high relevance to Odin's Mobile-First Design (9.A and 9.B), as the findings emphasize ease of use and seamless payment. The study's analysis of mediating factors like consumer characteristics offers medium relevance to Behavioral Profiling (5.A) by describing trait-dependent shopping behaviors. Domains like Spending Forecasting (6.A/6.B), Budget Recommendation (7.A-D), and Anomaly Detection (8.A-C) were considered but rejected due to the paper's focus on drivers of unplanned spending rather than prediction or management strategies. However, the findings on urgency and its effect on unplanned purchases provide contextual relevance (low) for understanding spending patterns that could be flagged as anomalies. The overall relevance is medium-high for design and user behavior understanding but low for algorithmic or system evaluation components.
limitations:
  - "Self-reported data may be subject to social desirability and recall bias. [unacknowledged]"
  - "Cross-sectional design precludes establishing causal relationships. [unacknowledged]"
  - "Geographic scope limited to a single city in the Philippines, limiting generalizability."
  - "The study's findings may not directly apply to the specific context of personal finance management systems."
remember_this:
  - "Urgency has a very large direct effect on impulse buying."
  - "Website usability drives impulse buying by increasing urgency."
  - "Consumer characteristics mediate the impact of marketing on impulse buying."
  - "Social factors do not directly cause impulse buying but influence website perception."
  - "The model explains 80% of the variance in impulse buying behavior."
```
---

## Paper 28: Albert et al_summarized.md

**Source File:** `Albert et al_summarized.md`

```yaml
paper_id: 10.62986/dp2025.35
designation: local
title: Gender equality, disability, and social inclusion in the Philippines: Progress, challenges, and opportunities in SDG 5 and SDG 10
authors: Albert, J. R. G.; Dacuycuy, C. B.; Quisumbing, A. R.; Basillote, L. B.; Cabalfin, D. L. D.; Vargas, A. R. P.; Luzon, P. E. D.; Mahmoud, M. A.
year: 2025
venue: PIDS Discussion Paper Series
odin_topics:
  - 1.A
  - 2.A
  - 2.B
  - 2.D
  - 4.A
tldr: Examines Philippines' progress on SDG 5 and 10, revealing policy achievements alongside implementation gaps that create complex, intersectional exclusion patterns for marginalized groups.
problem_and_motivation: Significant inequalities persist for women, persons with disabilities, and indigenous peoples despite robust legal frameworks. The intersection of multiple identities creates unique disadvantage patterns that single-issue approaches fail to address, requiring integrated policy responses for evidence-based inclusive development.
approach:
  - Mixed-methods design combining quantitative SDG indicator analysis with qualitative stakeholder interviews and focus groups.
  - Employs Shapley decomposition on merged FIES-LFS data to quantify factors contributing to inequality in working hours.
  - Uses descriptive and intersectional analytics, including National Demographic and Health Survey and Indigenous Peoples Household Survey data.
  - Conducted key informant interviews with government officials and civil society leaders.
  - Applied thematic coding to qualitative data from eight focus group discussions with affected populations.
findings:
  - num: Female disability prevalence is 15%, compared to 9% for males, with rates reaching 55% among women with no formal education.
  - num: Severe disability prevalence varies from 39% among those with no education to just 6% among college graduates.
  - num: Indigenous women's engagement in unpaid family work is more than three times higher than non-Indigenous counterparts.
  - Gender gaps in labor market participation are significantly larger among Indigenous Peoples and Muslim ethnic groups.
  - The GAD budget has become compliance-oriented rather than transformational, with widespread fund misuse and weak accountability.
  - num: Income inequality (Gini) decreased from 0.453 in 2015 to 0.406 in 2023, but the richest 20% still earn nearly 7.4 times more than the poorest 20%.
  - Persistent challenges remain in translating educational parity into economic empowerment and political representation for women.
key_figures_tables:
  - Table 1: Philippines WEF Global Gender Gap Index rankings → Performance has been volatile but remains the top performer in ASEAN.
  - Figure 1: Poverty incidence across basic sectors → Indigenous Peoples face the highest poverty at 32.4% in 2023.
  - Table 13: Select measures of per capita income inequality → Shows consistent but slow decline in Gini coefficient from 0.453 to 0.406.
  - Table 15: Inequality decomposition using household per capita income → Education creates meaningful income differences, but location and sex contribute little to between-group inequality.
  - Table 37: Disability prevalence by sex and ethnicity → Waray women experience the highest disability rate at 31%.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: GEDSI
    definition: Gender equality, disability and social inclusion - condition where all persons have equal rights, opportunities, and fair treatment regardless of various factors.
  - term: GAD Budget
    definition: Gender and Development budget - mandatory 5% allocation of agency budgets for gender programs.
  - term: Shapley Decomposition
    definition: Method to quantify the relative contributions of different factors to overall inequality patterns.
  - term: IPs
    definition: Indigenous Peoples - communities with ancestral domain rights and cultural traditions.
  - term: PWDs
    definition: Persons with disabilities - individuals with long-term physical, mental, intellectual, or sensory impairments.
critical_citations:
  - "[Crenshaw, 1989] — foundational for intersectional analysis framework."
  - "[UN Women, 2024] — provides SDG gender indicators for Philippines."
  - "[Pérez-Brito et al., 2024] — key data on Indigenous Peoples in Philippines."
  - "[World Bank, 2023] — documents persistent gender gaps in access to productive assets."
  - "[WHO, 2011] — ICF framework for understanding disability as interaction between impairments and environment."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Profiles financial and social structures of young professionals' households.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: Describes GEDSI context that shapes financial behaviors of target users.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Poverty and income inequality data imply cyclical financial pressures on marginalized groups.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: Income distribution patterns and poverty data provide background for spending cycles.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Contextualizes the policy and social landscape for financial management systems.
  contribution: This paper provides Odin with a foundational understanding of the demographic, cultural, and structural inequalities that shape Filipino young professionals' financial lives. It highlights the importance of culturally sensitive design by detailing specific financial practices, seasonal spending patterns driven by poverty and income volatility, and the lived realities of marginalized groups. The intersectional analysis directly justifies Odin's need to go beyond simple user profiling and incorporate contextual variables like ethnicity, disability, and geographic location into its algorithms for expense categorization, forecasting, and anomaly detection. The findings on GAD budget failures and data gaps inform Odin's design principles around user trust, data privacy, and the importance of generating actionable insights from available data.
  directly_justifies:
    - "Poverty concentration among specific groups (IPs, PWDs, women) justifies targeted financial product design and goal setting in Odin."
    - "Gender disparities in unpaid care work and labor force participation justify forecasting models that account for varying income stability."
    - "Statistical invisibility of marginalized groups justifies Odin's data enrichment and cold-start strategies."
    - "Income inequality patterns justify budget recommendation algorithms that prioritize savings and debt management for vulnerable users."
    - "The disconnect between educational attainment and economic opportunity justifies system design that supports career and financial advancement."
  limits:
    - "The paper focuses on macro-level policy and social structures, not on individual-level financial behaviors or PFMS usage."
    - "Data on income is at the household level, not individual, limiting direct translation to personal finance tracking."
    - "The analysis does not evaluate specific personal finance applications or their effectiveness."
  mapping_rationale: A systematic scan across all 12 functional domains identified the paper's primary relevance to the Filipino Cultural Context and Existing Systems domains. The paper's exhaustive data on Filipino demographics, poverty, inequality, and cultural practices provided high-contextual relevance to topics 1.A, 2.A, 2.B, and 2.D, as it describes the very environment in which Odin's users make financial decisions. It also provides contextual relevance for the landscape of existing systems by detailing the societal and structural problems that a PFMS like Odin must navigate. Topics related to algorithmic modules (e.g., forecasting, anomaly detection, budget recommendation) were considered and rejected because the paper does not discuss or evaluate computational techniques; its relevance is purely contextual, offering the socio-economic background that should inform those algorithms. The paper's discussion of data gaps and "statistical invisibility" is particularly relevant to Odin's cold-start and user profiling challenges. Overall, the paper provides critical background for understanding Odin's target users but offers no direct technical contributions to the system's algorithmic components.
limitations:
  - "The paper's focus on national-level data may not reflect the granular financial behavior needed for a PFMS. [unacknowledged]"
  - "The study does not evaluate the effectiveness of personal finance management tools or digital financial services."
  - "Qualitative data saturation may not capture the full range of experiences for highly marginalized intersectional subgroups."
  - "The study did not undergo formal Institutional Review Board (IRB) approval."
remember_this:
  - "Income inequality (Gini) decreased from 0.453 to 0.406 between 2015 and 2023."
  - "Female disability prevalence is 50% higher than male at 15% versus 10%."
  - "Indigenous women's unpaid family work is over three times higher than non-Indigenous."
  - "The GAD budget is compliance-oriented with weak accountability and widespread misuse."
  - "Data gaps create 'statistical invisibility' for Indigenous Peoples and other marginalized groups."
```
---

## Paper 29: Espelita et-al_summarized.md

**Source File:** `Espelita et-al_summarized.md`

```yaml
paper_id: 9a7d8c3e-5b2f-4a8e-9c1d-6f3a8e2b7c5d
designation: local
title: Understanding Monetary Policy: Student Awareness, Perceptions, and Financial Behaviors in the Philippine Context
authors: Atento, R. G.; Espelita, C. A. M.; Rao, L.; Tian, Y.
year: 2025
venue: International Journal of Health and Business Analytics
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.D
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 7.A
  - 8.A
  - 9.A
  - 10.A
  - 12.A
  - 13.A
tldr: Filipino students show moderate monetary policy awareness, with graduate and business students exhibiting higher understanding, and this awareness positively correlates with saving and investment behaviors.
problem_and_motivation: Limited research examines young Filipinos' understanding of monetary policy, a critical gap given its role in economic stability and the youth's future role as economic stewards. The study addresses this by investigating how awareness and perceptions vary across educational levels and fields of study.
approach:
  - Descriptive-correlational survey design with 200 respondents from senior high, undergraduate, and graduate levels in Philippine institutions.
  - Stratified random sampling ensured representation across educational levels, academic programs, and demographic groups.
  - Structured questionnaire measured awareness of monetary policy, perceptions of effectiveness, and financial behaviors using Likert scales.
  - Validation included expert review and pilot testing with 30 students; Cronbach's alpha for subscales ranged from .74 to .85.
  - Data analyzed using ANOVA, t-tests, Pearson correlations, and multiple regression with Jamovi and SPSS.
findings:
  - num: Overall awareness of monetary policy is moderate, with graduate students scoring significantly higher (M=3.75) than undergraduates (M=3.25) and senior high students (M=2.80).
  - num: Business/economics students exhibited higher awareness (M=3.48) than students in other fields, F(4,195)=11.22, p<.001.
  - num: Awareness was positively correlated with perception of policy effectiveness (r=0.48, p<.001), saving behavior (r=0.31, p<.001), and investment behavior (r=0.24, p=.001).
  - No significant relationship was found between awareness and spending behavior (r=-0.07, p=.310).
  - num: Regression models showed awareness and perception significantly predicted saving (R²=.22) and investment (R²=.15) but not spending (R²=.04).
  - Students perceive monetary policy as effective in controlling inflation but are more cautious about its role in employment and long-term growth.
  - Gender did not significantly differentiate awareness levels, t(198)=0.31, p=.756.
  - Older students (23-30 years) demonstrated higher awareness (M=3.48) compared to younger groups (16-18 years, M=2.85).
  - Awareness levels differed significantly by educational level, F=47.83, p<.001, with all pairwise differences significant.
  - Students in "Other" programs (education, health sciences) had the lowest awareness (M=3.02), highlighting a curricular gap.
key_figures_tables:
  - "Table 4: Difference in awareness by age → Older students show higher awareness, F=14.62, p<.001."
  - "Table 5: Difference in awareness by gender → No significant difference found, t(198)=0.31, p=.756."
  - "Table 6: Difference in awareness by educational level → Graduate students highest, senior high lowest."
  - "Table 7: Difference in awareness by program → Business/economics highest, others lowest."
  - "Table 8: Correlation between awareness and perception → Positive moderate correlation, r=0.48."
  - "Table 9: Correlation between awareness and saving → Positive significant, r=0.31."
  - "Table 10: Correlation between awareness and investment → Positive significant, r=0.24."
  - "Table 11: Correlation between awareness and spending → No significant relationship, r=-0.07."
  - "Table 12: Regression results → Awareness and perception predict saving and investment, not spending."
key_equations:
  - equation: "R² = .22 for saving behavior model"
    explanation: "Awareness and perception explain 22% of saving variance."
  - equation: "R² = .15 for investment behavior model"
    explanation: "Awareness and perception explain 15% of investment variance."
  - equation: "R² = .04 for spending behavior model"
    explanation: "Awareness and perception explain negligible spending variance."
definitions:
  - term: "TRA"
    definition: "Theory of Reasoned Action, positing behavior is shaped by behavioral intentions influenced by attitudes and subjective norms."
  - term: "TPB"
    definition: "Theory of Planned Behavior, extends TRA by adding perceived behavioral control as a predictor of intentions."
  - term: "Monetary Policy"
    definition: "Central bank actions to regulate money supply and credit to achieve macroeconomic objectives like price stability."
  - term: "BSP"
    definition: "Bangko Sentral ng Pilipinas, the central monetary authority of the Philippines."
critical_citations:
  - "[Blinder et al., 2008] — Public expectations influence policy effectiveness."
  - "[Ajzen, 1991] — Foundational theory on planned behavior."
  - "[OECD, 2020] — Philippine financial literacy below global average."
  - "[Mishkin, 2019] — Definition and scope of monetary policy."
  - "[Lusardi & Mitchell, 2020] — Financial literacy interacts with contextual factors."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: "Directly examines Filipino students as future young professionals and economic actors."
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: "Investigates saving, spending, and investment behaviors of Filipino students."
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: "Analyzes financial behaviors (saving, investing, spending) in relation to policy awareness."
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: "Discusses cultural factors like extended family support and collectivist spending."
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: "Mentions cultural spending patterns but does not focus on cyclical occasions."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: "Identifies gaps in financial literacy and policy communication in the Philippines."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: "Examines how awareness shapes saving and investing profiles."
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: contextual
      justification: "Does not address cold-start, but profiles vary by educational background."
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: "Does not discuss classification algorithms for behavioral profiles."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: low
      justification: "Does not focus on predictive modeling; examines awareness-behavior correlations."
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: "Findings on saving behavior inform budget recommendation systems."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: "No direct discussion of anomaly detection; mentions spending patterns."
    - code: 9.A
      name: Mobile‑First Design Principles and Rationale
      relevance: contextual
      justification: "Recommends digital platforms and OERs for financial education."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: "Mentions data security in methodology but not a core finding."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: "Provides empirical evaluation framework for financial literacy interventions."
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: "Awareness positively correlates with saving behavior, informing savings goal features."
  contribution: "This paper directly informs Odin's behavioral profiling module by identifying how monetary policy awareness shapes saving and investment behaviors among Filipino students. The findings validate the need for personalized financial education in Odin's onboarding, as awareness levels vary significantly by educational background. The correlation between awareness and saving behavior (r=0.31) supports Odin's savings goal management features that adapt to user knowledge levels. The negative correlation with spending (r=-0.07) suggests that behavioral nudges in Odin must go beyond information provision to influence consumption habits. The study's grounded theory approach using TRA/TPB provides a theoretical foundation for Odin's user segmentation and intervention design."
  directly_justifies:
    - "Graduate and business students exhibit higher monetary policy awareness, justifying educational-level segmentation in Odin."
    - "Awareness correlates with saving behavior (r=0.31), supporting savings goal features in Odin."
    - "Awareness does not significantly influence spending, necessitating behavioral nudges beyond information."
    - "Gender did not differentiate awareness, suggesting gender-neutral financial education design in Odin."
    - "Students perceive monetary policy as effective in inflation control but not employment, indicating communication gaps to address."
  limits:
    - "Cross-sectional design prevents causal inference about awareness-behavior relationships."
    - "Self-reported data may introduce social desirability and recall biases."
    - "Sample restricted to selected institutions, limiting generalizability to all Filipino students."
    - "Scope excludes variables like trust in government and media exposure that may influence literacy."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was conducted. The 'Filipino Cultural Context' domain was flagged as highly relevant because the paper directly examines Filipino students' financial behaviors and cultural spending patterns, with topic 2.A (culturally specific practices) rated medium and 2.D (spending cycles) rated contextual due to only tangential mention. The 'Behavioral Profiling' domain was highly relevant, with topics 5.A (behavioral profiles) rated high based on the awareness-behavior correlations, 5.B (cold-start) rated contextual as the study mentions educational gaps that resemble cold-start conditions, and 5.C (classification) rated low as no classification algorithms are discussed. The 'Expense Categorization' domain was considered but rejected entirely (3.A, 3.B, 3.C) as the paper does not address expense frameworks. The 'Spending Forecasting' domain (6.A, 6.B) was rated low to contextual because the paper discusses spending behavior but not predictive models. The 'Budget Recommendation' domain (7.A) was rated medium as saving behavior findings can inform budget features. The 'Anomaly Detection' domain (8.A, 8.B, 8.C) was rejected due to no algorithmic discussion. The 'Mobile-First Design' domain (9.A) was rated contextual based on digital learning recommendations. The 'Data Privacy' domain (10.A) was rated low due to only methodological mention. The 'System Evaluation' domain (12.A) was rated medium for the empirical framework. The 'Savings & Debt Management' domain (13.A) was rated high for the direct saving behavior correlation, while 13.B and 13.C were rejected due to no debt or surplus discussion. Overall, the paper is moderately relevant to Odin, providing empirical grounding for behavioral profiling and savings features, but with limited direct algorithmic or system design implications."
limitations:
  - "Cross-sectional design prevents causal inference; longitudinal research needed."
  - "Self-reported data may introduce social desirability bias."
  - "Sample restricted to selected HEIs and senior high schools; findings may not generalize."
  - "Does not examine trust in government institutions or media exposure as variables."
remember_this:
  - "Graduate and business students show highest monetary policy awareness."
  - "Awareness correlates positively with saving and investment behaviors."
  - "Awareness does not influence spending behavior, highlighting behavioral gaps."
  - "Students perceive inflation control effectiveness but doubt employment impact."
  - "Targeted financial education across disciplines is urgently needed."
```
---

## Paper 30: Cabiles_summarized.md

**Source File:** `Cabiles_summarized.md`

```yaml
paper_id: d7b3f9a8-4c2e-5f1a-9d6b-8e7c4a9f2d1b
designation: local
title: Financial Management Practices of Employees at Bureau Of Internal Revenue
authors: Cabiles, S. L.
year: 2025
venue: United International Journal for Research & Technology
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 3.A
  - 3.B
  - 4.B
  - 5.A
  - 7.A
  - 13.A
  - 13.B
tldr: Employees exhibit strong budgeting and saving behaviors but inconsistent spending and investing practices, with debt accumulation and impulse spending as key barriers.
problem_and_motivation: The study addresses the need to understand the personal financial management practices of employees to identify gaps and propose targeted interventions. Effective financial management is essential for employees to navigate economic uncertainties and secure their financial future. The research specifically focuses on permanent employees of the Bureau of Internal Revenue to inform the development of financial literacy programs.
approach:
  - A quantitative descriptive research design was used to assess financial practices and literacy levels.
  - Data was collected using a Likert-scale questionnaire administered online and via pen-and-paper to permanent employees of BIR RDO 068.
  - Descriptive statistics including frequency count, percentage, ranking, and weighted mean were used for analysis.
  - The study focused on four financial domains: budgeting, spending, saving, and investing.
  - The research also identified challenges encountered in managing and planning finances through frequency distribution.
findings:
  - Employees demonstrate strong budgeting and saving behaviors, with high mean scores for emergency fund maintenance (4.32) and setting aside savings (4.37).
  - Spending practices are less consistent, with moderate engagement in aligning purchases with financial goals (3.50) and some impulse buying (3.20).
  - Investing practices are the weakest domain, with inconsistent engagement across all measured items and a value-action gap identified.
  - Financial literacy engagement is predominantly self-directed and moderate, with average mean scores ranging from 2.90 to 3.27 across domains.
  - Accumulation of debt and lack of awareness about interest rates are the most significant challenges, ranking first and second among identified barriers.
key_figures_tables:
  - "Table 1: Budgeting Practices: Mean scores for emergency fund (4.32) and expense tracking (4.03) indicate strong practices."
  - "Table 2: Spending Practices: Mean score for prioritizing quality (4.10) suggests disciplined spending, but impulse buying (3.20) remains a concern."
  - "Table 3: Saving Practices: High mean scores for regular saving (4.37) and emergency funds (4.20) reflect responsible habits."
  - "Table 4: Investing Practices: Low mean scores (2.66-3.51) indicate cautious behavior and a knowledge-action gap."
  - "Table 5: Financial Literacy Engagement: Low average means across domains highlight the need for structured programs."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Value-Action Gap (VAG)"
    definition: "The disparity between an individual's beliefs and their actual behavior."
  - term: "Mental Accounting"
    definition: "The way individuals categorize their expenses and perform cost-benefit analysis."
  - term: "Financial Well-being"
    definition: "A state where a person can fully meet current and ongoing financial obligations, feels secure in their financial future, and can make choices that allow enjoyment of life."
critical_citations:
  - "[Ali et al., 2024] — Links mental budgeting to better financial management."
  - "[Lusardi, 2019] — Highlights workplace financial education as effective."
  - "[Tamplin, 2025] — Emphasizes expense tracking for financial control."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "medium"
      justification: "Study focuses on Filipino employees, a subset relevant to the demographic."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "medium"
      justification: "Details salary, debt, and savings structures of Filipino employees."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Directly analyzes budgeting, spending, saving, and investing behaviors of Filipino employees."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "contextual"
      justification: "Mentions family socialization and cultural values as influences on financial behavior."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "medium"
      justification: "Investigates budgeting and spending practices, which are foundational to categorization."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      relevance: "low"
      justification: "Tangentially discusses expense tracking but not category design."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Identifies gaps in financial literacy engagement and application of knowledge."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Describes employee financial behaviors, which can inform profile construction."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "high"
      justification: "Directly examines budgeting strategies and their effectiveness."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "high"
      justification: "Directly analyzes saving practices and goals."
    - code: "13.B"
      name: "Debt Management in PFMS"
      relevance: "high"
      justification: "Identifies debt accumulation as a primary challenge."
  contribution: "This study provides empirical data on the financial behaviors of Filipino government employees, which can inform the design of the behavioral profiling and budgeting modules in Odin. The identified gaps in financial literacy and practical application highlight the need for personalized financial education and coaching features. The findings on debt accumulation and impulse spending support the development of debt management and anomaly detection components. The paper's recommendations for structured financial literacy programs justify the need for educational content within a PFMS."
  directly_justifies:
    - "Employees demonstrate strong budgeting but inconsistent investing, justifying behavioral profile calibration."
    - "Accumulation of debt due to unfamiliarity with interest rates supports a need for debt literacy modules."
    - "The value-action gap in investing indicates a need for behavioral nudges in financial planning features."
  limits:
    - "Focus on a single government office limits generalizability to other sectors or demographics."
    - "Relies on self-reported data, which may be subject to social desirability bias."
    - "Does not evaluate the effectiveness of specific financial literacy interventions."
  mapping_rationale: "A systematic scan of all 12 functional domains was conducted against the paper's content. Domains related to Filipino cultural context (2.A), expense categorization (3.A, 3.B), existing systems gaps (4.B), behavioral profiling (5.A), budgeting (7.A), and savings/debt management (13.A, 13.B) were flagged as relevant. The paper's focus on employee practices and challenges directly supports topics 1.C, 7.A, 13.A, and 13.B with high relevance. Topics 1.A, 1.B, 3.A, 4.B, and 5.A were assigned medium relevance for providing supporting context. Topic 2.A was deemed contextual due to its indirect mention of cultural influences. Other domains, including forecasting (6.A, 6.B), anomaly detection (8.A, 8.B), mobile-first design (9.A, 9.B), data privacy (10.A, 10.B), retention (11.A), and system evaluation (12.A, 12.B), were considered but rejected as the paper does not address these algorithmic or design-specific areas. The overall relevance is medium to high, providing foundational behavioral data but lacking in technical specifications for Odin's computational modules."
limitations:
  - "The study is limited to a single Revenue District Office, which may not represent all BIR employees."
  - "Cross-sectional design limits causal inference regarding the impact of financial literacy on practices."
  - "The study relies on self-reported data, which can introduce bias. [unacknowledged]"
  - "No direct measure of actual financial behavior was used, only reported practices. [unacknowledged]"
remember_this:
  - "Employees frequently set up emergency funds, indicating strong saving behavior."
  - "The value-action gap shows that investment knowledge does not translate to practice."
  - "Debt accumulation is the primary financial challenge for government employees."
  - "Financial literacy programs can improve saving habits and investment decisions."
  - "Structured financial education is needed to bridge the gap between knowledge and application."
```
---

## Paper 31: Vidal-Sarahina_summarized.md

**Source File:** `Vidal-Sarahina_summarized.md`

```yaml
paper_id: 10.69569/jip.2025.483
designation: local
title: Financial Literacy of Department of Education Teachers in the Philippines
authors: Vidal-Sarahina, M.E.
year: 2025
venue: Journal of Interdisciplinary Perspectives
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 5.A
  - 7.A
  - 13.A
tldr: Study reveals gap between financial knowledge and behavior among DepEd teachers due to cultural obligations, low salaries, and behavioral biases, advocating for comprehensive financial education.
problem_and_motivation: Teachers face financial instability despite financial literacy, with external pressures, cultural expectations, and behavioral biases hindering practical application of knowledge. Limited research on DepEd teachers in Guihulngan City exists, requiring a holistic assessment of financial knowledge, attitudes, and behaviors.
approach:
  - Mixed-methods design with quantitative survey of 30 teachers and qualitative interviews with 10 teachers from Guihulngan City Division.
  - Quantitative data used weighted means, standard deviations, and Spearman's rank-order correlation for financial knowledge, attitude, and behavior.
  - Qualitative data analyzed using Braun and Clarke's reflexive thematic analysis to identify factors contributing to knowledge-behavior gap.
  - Lincoln and Guba's trustworthiness criteria applied for rigor in qualitative component.
  - Purposive sampling selected teachers with at least ten years of service in the Department of Education.
findings:
  - num: Mean financial knowledge score was 2.15, indicating moderate understanding.
  - num: Mean financial attitude score was 3.02, showing generally positive outlook.
  - num: Mean financial behavior score was 2.80, reflecting moderately acceptable practices.
  - num: Very weak positive correlation between knowledge and attitude (r = 0.09, p = 0.62).
  - num: No significant correlation between knowledge and behavior (r = 0.01, p = 0.96).
  - num: Weak correlation between attitude and behavior (r = 0.06, p = 0.75).
  - Qualitative analysis revealed themes: Knowledge-Action Gap, Cultural and Familial Expectations, Economic Realities, and Behavioral Biases.
  - Financial behavior is shaped by complex interplay of knowledge, culture, economic pressures, and psychology.
  - Emotional spending and overconfidence contribute to suboptimal financial decisions among teachers.
  - Systemic issues like low salaries and loan dependence constrain financial freedom.
key_figures_tables:
  - Table 1: Respondents' Financial Knowledge, Attitude, and Behavior means and standard deviations → Shows moderate scores with knowledge lowest (2.15) and attitude highest (3.02).
  - Table 2: Correlation between variables → Reveals weak and non-significant relationships among knowledge, attitude, and behavior.
  - Table 3: Thematic analysis themes → Lists Knowledge-Action Gap, Cultural & Familial Expectations, Economic Realities, and Behavioral Biases with categories and descriptions.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Financial Literacy
    definition: Ability to apply financial knowledge, attitudes, and behaviors to achieve financial well-being and resilience.
  - term: DepEd
    definition: Department of Education in the Philippines.
  - term: Knowledge-Action Gap
    definition: Disconnect between possessing financial knowledge and translating it into actual financial behavior.
  - term: Utang na Loob
    definition: Filipino cultural concept of a profound debt of gratitude that influences financial decision-making.
critical_citations:
  - "[OECD/INFE, 2023] — Defines financial literacy as knowledge, attitudes, and behaviors."
  - "[Lusardi & Messy, 2023] — Emphasizes financial literacy for navigating complex systems."
  - "[Casingal & Ancho, 2021] — Highlights financial instability among Filipino teachers."
  - "[Variacion et al., 2024] — Identifies disparity between knowledge and behavior in teachers."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Study focuses on Filipino teachers as a professional demographic with financial challenges.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Examines financial structures like salaries, loan dependence, and budgeting constraints.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly analyzes financial behavior, knowledge, and attitudes of Filipino teachers.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Highlights cultural obligations and utang na loob impacting financial decisions.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: Discusses budget constraints and economic pressures that may relate to cyclical spending.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: medium
      justification: Cultural and familial expectations may influence spending during occasions and obligations.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Identifies behavioral biases like impulsivity and overconfidence affecting financial profiles.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Discusses budgeting as a survival skill and the need for structured savings programs.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Addresses savings challenges and the need for support systems to achieve savings goals.
  contribution: Provides empirical evidence of the knowledge-behavior gap among Filipino teachers, emphasizing cultural and behavioral barriers. This directly informs Odin's user profiling (5.A) by highlighting behavioral biases like overconfidence and impulsivity. The study's cultural insights (2.A) support Odin's need for culturally aware categorization and recommendation systems. Findings on economic constraints (1.B) justify Odin's focus on realistic budgeting and debt management (13.A). The research validates Odin's approach to integrating behavioral finance principles into financial education.
  directly_justifies:
    - "Financial knowledge alone does not predict behavior among Filipino teachers."
    - "Cultural obligations and familial expectations significantly override personal financial goals."
    - "Behavioral biases such as impulsive spending and overconfidence lead to poor financial decisions."
    - "Economic realities like low salaries and loan dependence constrain financial freedom."
    - "Financial education must address socio-economic, cultural, and behavioral barriers."
  limits:
    - "Sample limited to 40 teachers from a single city division, limiting generalizability."
    - "Cross-sectional design cannot capture long-term behavioral changes."
    - "Self-reported data may be subject to social desirability bias."
    - "Focus on teachers may not directly generalize to other Filipino young professionals."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes identified strong relevance to Filipino Cultural Context (2.A, 2.B, 2.D), Financial Structure (1.B), and Behavioral Profiling (5.A). The paper directly addresses financial behavior, knowledge, and attitudes of Filipino teachers, making high relevance for 1.A, 1.B, 1.C, 2.A, and 5.A. Seasonal spending (2.B) and spending cycles (2.D) are touched upon through discussions of economic pressures and cultural obligations, assigned medium relevance. Budgeting strategies (7.A) and savings management (13.A) are relevant through the need for structured programs, assigned medium. Topics like 3.A (Expense Categorization), 3.B (Category Design), 4.A (Existing Systems), 6.A (Forecasting), 8.A (Anomaly Detection), 9.A (Mobile Design), 10.A (Data Privacy), 11.A (Engagement), and 12.A (Evaluation) were considered but rejected as the paper does not directly address algorithmic, system design, or PFMS-specific implementation concerns. The study's primary value to Odin lies in understanding user context, behavioral drivers, and cultural factors affecting financial management.
limitations:
  - "Sample limited to 40 teachers from a single city division, limiting generalizability."
  - "Cross-sectional design cannot capture long-term behavioral changes."
  - "Self-reported data may be subject to social desirability bias."
  - "Focus on teachers may not directly generalize to other Filipino young professionals."
  - "Limited discussion of specific financial products or technologies relevant to PFMS."
remember_this:
  - "Financial knowledge does not translate to behavior for Filipino teachers."
  - "Cultural obligations and family support strongly influence financial decisions."
  - "Behavioral biases like overconfidence and impulsivity hinder sound financial management."
  - "Low salaries and loan dependence create significant economic constraints."
  - "Effective financial programs must address behavioral and systemic barriers."
```
---

## Paper 32: Garcia_summarized.md

**Source File:** `Garcia_summarized.md`

```yaml
paper_id: 10.69569/jip.2025.324
designation: local
title: Financial Literacy and Financial Health of Public Junior High School Teachers
authors: Garcia, E.
year: 2025
venue: Journal of Interdisciplinary Perspectives
odin_topics:
  - 1.B
  - 1.C
  - 2.A
  - 4.B
  - 10.A
  - 10.B
  - 13.A
  - 13.B
tldr: Public junior high school teachers demonstrate high financial literacy but remain financially coping, with notable gaps in emergency savings, debt management, and retirement planning.
problem_and_motivation: Public school teachers in the Philippines face financial insecurity due to low wages and rising costs, yet localized research on their financial literacy and health is scarce. This study addresses that gap to inform targeted financial training programs for educators.
approach:
  - A descriptive-quantitative research design was used.
  - Data were collected from 241 randomly selected teachers in District VI, Quezon City.
  - Validated questionnaires measured financial literacy and health across multiple dimensions.
  - Non-parametric tests (Mann-Whitney U, Kruskal-Wallis H) were used to compare groups.
  - Demographic factors were analyzed for their influence on financial outcomes.
findings:
  - num: Overall financial literacy mean score was 4.02 (High), with retirement planning scoring lowest at 3.75.
  - num: Overall financial health mean score was 61.2, categorizing teachers as "Financially Coping."
  - num: Spending scored highest in financial health at 63.17, while saving scored lowest at 51.87.
  - num: Only 38.07% of respondents expressed confidence in their savings being sufficient for the future.
  - Significant differences in financial literacy were found based on sex, age, number of children, income, education, position, experience, and specialization.
  - Significant differences in financial health were observed for sex, age, civil status, number of children, education, position, experience, and specialization.
  - Teachers demonstrated strong budgeting practices but weaker engagement with tax and estate planning.
key_figures_tables:
  - "Table 1: Financial knowledge scores → Knowledge of borrowing costs (4.02) was lower than general awareness (4.49)."
  - "Table 10: Spending health scores → Bill payment (86.41) was healthy, but month-end surplus (39.00) was vulnerable."
  - "Table 13: Planning health scores → Insurance confidence (57.14) was lower than overall planning engagement (63.94)."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Financially Coping
    definition: Able to meet basic needs but lacks surplus for savings or investments.
  - term: Financial Literacy
    definition: Ability to make informed decisions about budgeting, saving, investing, and planning.
critical_citations:
  - "[Lusardi & Mitchell, 2011] — Links education and experience to financial literacy."
  - "[Villagonzalo & Mibato, 2020] — Found good financial management but poor attitudes in teachers."
  - "[Burgonio, 2023] — Reported low take-home pay for entry-level teachers."
relevance:
  topics:
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Provides income and debt profiles of teachers, a key PFMS target.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly measures financial behavior, attitudes, and health of teachers.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Examines financial practices within a Filipino public-sector context.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies training gaps and the need for targeted financial programs.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Discusses ethical data handling but does not address PFMS-specific privacy.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: contextual
      justification: Mentions ethical compliance but lacks focus on trust-building mechanisms.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: Directly reports savings challenges, including emergency fund deficits.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: Details borrowing patterns and debt-to-income ratios of teachers.
  contribution: This paper informs Odin's savings and debt management modules by providing empirical baseline data on the financial behaviors and challenges of Filipino public school teachers. The findings on savings deficits justify the need for automatic savings features and goal-setting tools. The detailed borrowing and debt repayment data support the design of debt management and reduction features. The study also validates the importance of demographic-aware profiling, as significant differences were observed across various groups.
  directly_justifies:
    - "Teachers allocate a large portion of income to debt repayment (78.44 mean score), indicating need for debt management tools."
    - "Only 39.00 mean score for month-end surplus highlights the need for surplus allocation features."
    - "Savings concerns (38.07 mean score) justify automated savings and emergency fund features."
    - "Significant demographic differences justify personalized behavioral profiling in Odin."
  limits:
    - "Sample is limited to public junior high school teachers in one district of Quezon City, limiting generalizability."
    - "Self-reported data may be subject to social desirability bias."
    - "Cross-sectional design does not allow for causal inferences."
    - "Does not evaluate specific PFMS features or digital financial tools."
  mapping_rationale: A systematic scan of all 12 functional domains identified primary relevance to Financial Structure (1.B), Financial Behavior (1.C), Savings & Debt Management (13.A, 13.B), and Existing Systems Gaps (4.B). The paper's focus on financial literacy and health directly aligns with 1.B and 1.C (high relevance), providing concrete numerical data on teacher income, spending, and savings. Culturally Specific Practices (2.A) is medium relevance as it examines Filipino public-sector financial behavior but does not address unique cultural practices like "utang" or "paluwagan." Data Privacy (10.A) and User Trust (10.B) are contextual, as the study discusses ethical compliance but not PFMS-specific privacy features. Domains like Anomaly Detection, Forecasting, and Mobile Design were rejected as the paper does not discuss computational methods or digital interfaces. The overall relevance is high for foundational financial behavior data, moderate for contextual cultural insights, and low for algorithmic or system design.
limitations:
  - "Self-reported measures may introduce bias."
  - "Cross-sectional design limits causal interpretations."
  - "Sample restricted to one district, limiting generalizability."
  - "Does not evaluate digital PFMS or algorithmic approaches."
remember_this:
  - "Teachers scored high on financial literacy (4.02) but were only financially coping (61.2)."
  - "Only 39.00 mean score for month-end surplus indicates severe savings constraints."
  - "Debt repayment consumes a large portion of teacher income (78.44 mean score)."
  - "Significant demographic differences exist in both financial literacy and health."
  - "Retirement planning (3.75) and emergency fund (3.72) literacy were the lowest areas."
```
---

## Paper 33: Flores_summarized.md

**Source File:** `Flores_summarized.md`

```yaml
paper_id: 2b8f6e7a-3c4d-4e5f-8a9b-0c1d2e3f4a5b
designation: local
title: Financial freedom of Filipinos in personal finance management
authors: Flores, C. A. R.
year: 2025
venue: Unknown
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.C
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 13.A
  - 13.B
tldr: Filipino financial behaviors are shaped by traditional saving methods, low literacy, and cultural attitudes, leading to poor emergency preparedness and high debt reliance.
problem_and_motivation: Most Filipinos lack financial literacy and do not understand the purpose of key financial instruments for achieving true financial wellness. This leads to poor spending habits, reliance on traditional saving methods, and lack of emergency fund preparedness. The study addresses this gap by examining cash, debt, risk, and wealth management practices among Filipino corporate employees.
approach:
  - Descriptive study using survey questionnaires distributed to 150 respondents from 10 major Philippine corporations.
  - Data collected on demographic profiles, work profiles, and personal finance management practices in four areas.
  - Weighted mean analysis used to assess the degree of financial freedom in each management area.
  - Linear regression analysis performed to determine the significant contribution of each finance variable to overall financial freedom.
  - Respondents included top management, middle management, and rank-and-file staff from companies like SM Prime and Ayala Corporation.
findings:
  - Most respondents were male (57%), married (63%), aged 31-40 (43%), with 1-2 children (57%).
  - Majority held rank-and-file positions (40%) with 11-18 years of work experience (50%) and monthly income of ₱30,000 or above (40%).
  - Respondents agreed on the risks of keeping cash at home (WM=3.73) and the importance of paying high-interest debt first (WM=3.7).
  - Risk management had the highest overall weighted mean (3.65) among finance variables.
  - Linear regression showed that cash, debt, risk, and wealth management do not significantly contribute to financial freedom.
  - Cultural attitudes like the "come-what-may" mindset and reliance on traditional alkansya (bamboo savings) hinder effective financial planning.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: CDRW
    definition: Cash, Debt, Risk, Wealth management – the four areas of personal finance.
  - term: PDIC
    definition: Philippine Deposit Insurance Corporation – insures bank deposits.
  - term: NFIS
    definition: Negative Finding Information System – tracks credit standing.
  - term: GDP
    definition: Gross Domestic Product – total value of goods produced in a country.
critical_citations:
  - "[Lusardi, 2004] — Foundational work on savings and financial education."
  - "[Lusardi & Beeler, 2007] — Examines saving behavior across cohorts and planning."
  - "[Lusardi, Keller, & Keller, 2008] — Social marketing approaches to increase savings."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: The study surveys Filipino corporate employees, a key demographic for Odin.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Details income, work position, and financial practices of this group.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Describes spending, saving, and debt behaviors directly relevant to PFMS.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Identifies traditional alkansya and "come-what-may" attitudes shaping Filipino finance.
    - code: 2.C
      name: User-Declared Financial Preferences
      relevance: medium
      justification: Provides survey-based insights into user attitudes towards cash, debt, and insurance.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Discusses budgeting and allocation, foundational for expense categorization.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: Highlights need for categories like emergency funds and debt payments.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Provides background on financial practices but not on PFMS systems per se.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies gaps in financial literacy and awareness that PFMS could address.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly profiles Filipino financial behaviors (e.g., spending, saving, debt) for behavioral classification.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: contextual
      justification: Discusses behavioral patterns but does not address cold-start profiling.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: Emphasizes emergency fund preparedness and saving habits, core to savings goals.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: Provides specific debt management strategies relevant to Odin's debt modules.
  contribution: "This paper provides empirical evidence on Filipino financial behaviors that informs Odin's user profiling module. It identifies specific cultural practices, like traditional saving and high debt reliance, that Odin must accommodate in its expense categorization and behavioral models. The findings on emergency fund gaps support Odin's savings goal management features. The identified lack of financial literacy highlights the need for Odin's educational nudges and simplified budget recommendations. Overall, the paper justifies a PFMS that is culturally aware and focuses on foundational financial practices."
  directly_justifies:
    - "Filipinos exhibit low emergency fund preparedness, suggesting Odin should prioritize emergency savings goals."
    - "Traditional saving methods like alkansya indicate a need for digital alternatives that build trust."
    - "Debt management strategies like paying highest interest first should be incorporated into Odin's recommendation engine."
    - "Financial literacy gaps in the Philippines justify Odin's educational and simplified budgeting features."
  limits:
    - "The study is limited to 150 respondents from 10 large corporations, not representative of all Filipino young professionals."
    - "The linear regression showed no significant contribution of the four finance variables to financial freedom, suggesting other unmeasured factors are at play."
    - "The study does not evaluate any existing PFMS, only general financial practices."
  mapping_rationale: "The systematic scan across all 12 functional domains identified strong relevance for domains related to Filipino cultural context, expense categorization, behavioral profiling, and savings/debt management. Topics 1.A, 1.B, 1.C, 2.A, 5.A, 13.A, and 13.B were assigned 'high' relevance as the paper directly characterizes the financial structure, culturally specific practices, and behavioral profiles of Filipino employees, while also offering specific strategies for savings and debt management that directly inform Odin's modules. Topics 2.C and 3.A/B were assigned 'medium' as they provide contextual evidence for user preferences and expense categorization. Topic 4.B was 'medium' for identifying gaps in financial literacy and awareness. The domains related to forecasting (6.A/B), budget recommendation algorithms (7.A-D), anomaly detection (8.A-C), mobile-first design (9.A/B), data privacy (10.A/B), retention (11.A/B), and system evaluation (12.A-C) were rejected as the paper does not address these algorithmic or design topics. The paper's focus is on descriptive analysis of current financial practices, not on building or evaluating PFMS systems."
limitations:
  - "Sample limited to 150 employees from 10 large corporations, not representative. [unacknowledged]"
  - "Linear regression showed no significant contribution of the four finance variables to financial freedom. [unacknowledged]"
  - "Study does not account for regional variations in Filipino financial practices."
remember_this:
  - "Low financial literacy and traditional saving habits characterize Filipino young professionals."
  - "Emergency fund preparedness is critically low, with most relying on debt for unexpected expenses."
  - "Paying high-interest debt first is a key strategy for financial freedom."
  - "Risk management had the highest agreement score, indicating awareness of insurance importance."
  - "Cash, debt, risk, and wealth management did not significantly predict financial freedom in this sample."
```
---

## Paper 34: Bongado et al_summarized.md

**Source File:** `Bongado et al_summarized.md`

```yaml
paper_id: 7ad48f82-1c9f-5238-93f8-8878e2720d96
designation: local
title: Influence of Digital Wallets on the Financial Behavior of HEI’s Students
authors: Bongado, M. B. B.; Magallanes, A. R.; Semaña, C. M.
year: 2025
venue: Unknown
odin_topics:
  - 2.A
  - 5.A
  - 9.A
  - 10.A
tldr: Digital wallet usage positively influences financial behavior among Filipino HEI students, explaining 45.4% of variance in financial practices.
problem_and_motivation: The influence of digital wallet usage on financial behavior, particularly cash management and budgeting, remains underexplored among Filipino HEI students despite widespread adoption. Understanding this relationship is critical to determining whether digital financial tools support or hinder responsible financial habits among young Filipinos.
approach:
  - A quantitative descriptive-correlational design was employed with 219 randomly selected students from a Philippine state university.
  - Data were collected using a validated structured questionnaire adapted from Belmonte et al. (2024) measuring determinants of digital wallet adoption and financial behavior.
  - Determinants included perceived ease of use, perceived usefulness, perceived value, social influence, attractiveness of alternatives, perceived trust, perceived security, and intention to use.
  - Financial behavior was assessed through cash management and financial planning and budgeting dimensions using a 4-Point Likert scale.
  - Pearson correlation and regression analysis were used to test the influence of digital wallet usage on financial behavior at a 0.05 significance level.
findings:
  - Students perceived digital wallet determinants positively, with mean scores ranging from 2.91 to 2.99 across all factors.
  - Perceived trust exhibited the highest variability (SD = 1.24), indicating diverse opinions on platform reliability.
  - Financial behavior scores were high (M = 2.99), with strong agreement on responsible cash management and budgeting practices.
  - num: Digital wallet usage significantly predicted financial behavior, accounting for 45.4% of the variance (R² = 0.454, F = 180.136, p < .001).
  - num: The beta coefficient (β = 0.673) indicates a positive relationship between digital wallet usage and improved financial behavior.
  - The regression model confirmed digital wallet usage as a significant predictor of financial behavior among student respondents.
key_figures_tables:
  - Table 1: Determinants of digital wallet usage means and SDs → Students generally agree on all adoption factors, with trust showing most variability.
  - Table 2: Financial behavior determinants means and SDs → Students demonstrate responsible financial practices with moderate consensus on cash management and budgeting.
  - Table 3: Regression analysis results → Digital wallet usage significantly influences financial behavior, explaining 45.4% of variance.
key_equations:
  - equation: "R² = 0.454"
    explanation: "45.4% of financial behavior variance explained by digital wallet usage."
definitions:
  - term: FinTech
    definition: Financial technology that revolutionizes payment systems and financial services through digital innovations.
  - term: Digital Wallet
    definition: A digital substitute for cash and bank accounts allowing users to store, transfer, and pay through mobile devices.
  - term: TAM
    definition: Technology Acceptance Model explaining user adoption based on perceived usefulness and ease of use.
  - term: HEI
    definition: Higher Education Institution offering tertiary education programs.
  - term: PFMS
    definition: Personal Finance Management System for tracking and managing individual finances.
critical_citations:
  - "[Belmonte et al., 2024] — Validated TAM instrument for Filipino e-wallet adoption context."
  - "[Scheresberg et al., 2020] — Found mobile payment users overspend and save less."
  - "[Amanda et al., 2023] — Digital wallets promote impulsive spending among Generation Z."
relevance:
  topics:
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Examines digital wallet adoption and financial behavior specifically among Filipino HEI students.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Assesses financial behavior dimensions including cash management and budgeting practices.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Digital wallets are mobile-first platforms; findings inform design for student financial management.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Perceived trust and security were significant determinants of adoption and usage.
    - code: 2.C
      name: User-Declared Financial Preferences
      relevance: low
      justification: Touchs on financial behavior but does not deeply explore user-declared preferences.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: Mentioned in financial planning and budgeting context but not focused on categorization frameworks.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: References digital wallets as existing systems but does not survey the landscape.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: contextual
      justification: Budgeting is a dimension of financial behavior but no recommendation system is evaluated.
  contribution: This study provides empirical evidence that digital wallet usage positively influences financial behavior among Filipino HEI students, directly informing Odin's user profiling and behavioral classification modules. The validated TAM-based instrument offers a framework for understanding adoption determinants that can be adapted for Odin's onboarding and personalization features. The significant relationship between digital wallet usage and responsible financial practices supports the development of mobile-first financial management tools that promote budgeting and cash management. The findings on perceived trust and security variability highlight the importance of Odin's data privacy and user trust components. The study's focus on Filipino young professionals aligns with Odin's target demographic and validates the need for culturally relevant financial behavior assessment.
  directly_justifies:
    - "Digital wallet usage positively predicts financial behavior among Filipino students."
    - "Perceived ease of use and usefulness are key determinants of financial tool adoption."
    - "Financial behavior includes cash management and budgeting as measurable dimensions."
    - "Trust and security perceptions vary among users and affect adoption rates."
  limits:
    - "Focus on a single university in one municipality limits generalizability to broader Filipino young professional populations."
    - "Cross-sectional design cannot establish causal relationships between digital wallet usage and financial behavior."
    - "Self-reported survey data may be subject to social desirability bias."
    - "Does not control for income level, digital literacy, or parental influence on financial behavior."
    - "Financial behavior assessment limited to cash management and budgeting, excluding savings and debt management."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains flagged as relevant include: Filipino Cultural Context (2.A, 2.B, 2.C, 2.D) due to the study's focus on Filipino HEI students and their specific financial practices; Behavioral Profiling & Classification (5.A, 5.B, 5.C) as the paper directly assesses financial behavior dimensions; Mobile-First Design (9.A, 9.B) because digital wallets are mobile platforms; and Data Privacy & User Trust (10.A, 10.B) through its examination of perceived trust and security. Topic codes selected with high relevance: 2.A (culturally specific practices), 5.A (financial behavioral profiles). Medium relevance: 9.A (mobile-first principles), 10.A (data privacy). Low relevance: 2.C (user-declared preferences). Contextual relevance: 3.A (expense categorization), 4.A (existing systems landscape), 7.B (budget recommendation). Borderline cases included the paper's coverage of both 2.A and 2.C, resolved by assigning 2.A as the primary code since the focus is on actual practices rather than stated preferences. Domains rejected included Expense Categorization (3.A, 3.B, 3.C) as the paper does not examine categorization frameworks; Existing Systems & Gaps (4.A, 4.B) as it does not survey the PFMS landscape; Spending Forecasting (6.A, 6.B) as no predictive modeling is conducted; Anomaly Detection (8.A, 8.B, 8.C) as no anomaly detection is evaluated; Engagement & Retention (11.A, 11.B) as the study does not examine engagement dynamics; System Evaluation (12.A, 12.B, 12.C) as no system evaluation framework is used; and Savings & Debt Management (13.A, 13.B, 13.C) as these are not assessed. Overall, the paper provides moderate to high relevance for Odin's behavioral profiling and cultural contextualization modules, while offering contextual insights for design and trust considerations.
limitations:
  - "Convenience sampling may limit representativeness of all Filipino HEI students."
  - "Cross-sectional design prevents establishing causality between digital wallet usage and financial behavior."
  - "Self-reported measures may be subject to response bias and overestimation of responsible behavior."
  - "Study limited to one geographic location (Talisayan, Misamis Oriental), reducing generalizability. [unacknowledged]"
  - "No qualitative data to capture deeper motivations and challenges in digital wallet usage. [unacknowledged]"
  - "Does not account for income or parental influence as confounding variables. [unacknowledged]"
remember_this:
  - "Digital wallet usage explains 45.4% of financial behavior variance in Filipino students."
  - "Perceived trust shows the widest variation among adoption determinants."
  - "Students demonstrate responsible cash management and budgeting practices."
  - "Digital wallets serve as enablers of financial discipline beyond transactional tools."
  - "Security and trust perceptions significantly affect digital wallet adoption."
```
---

## Paper 35: Tiongco & Gangan_summarized.md

**Source File:** `Tiongco & Gangan_summarized.md`

```yaml
paper_id: 8c7b8f4a-2e5d-4c9f-8a3b-1e2d4c6f8a9b
designation: local
title: Moving Beyond the Php500 Noche Buena Illusion
authors: Tiongco, M. M.; Gañgan, F. Y. D.
year: 2025
venue: DLSU-Angelo King Institute Policy Brief
odin_topics:
  - 2.A
  - 2.B
  - 2.D
  - 3.C
  - 4.B
  - 5.A
  - 13.A
tldr: Inflation and shrinkflation have eroded the purchasing power of the Php500 Noche Buena basket, which now costs Php643–670, placing an undue burden on low-income Filipino households.
problem_and_motivation: The persistent promotion of a Php500 holiday basket obscures the real cost of food due to inflation and shrinkflation. This misrepresentation undermines the dignity and financial well-being of Filipino families, especially low-income households, by setting unrealistic expectations for holiday spending.
approach:
  - Analyzed PSA Food CPI data from 2018 to 2025 to calculate the real cost of a Php500 basket.
  - Compared the contents of commercial Php500 holiday baskets from 2018 and 2025 to demonstrate shrinkflation and product substitution.
  - Used FIES data to illustrate food expenditure shares across income deciles.
  - Assessed affordability by comparing the basket cost to the daily minimum wage in NCR.
findings:
  - num: A Php500 food basket from 2018 now costs Php669.80 in NCR and Php643.28 outside NCR in November 2025.
  - num: Food inflation has risen faster than general inflation, with essential holiday items experiencing 8-10% annual inflation during 2023–2024.
  - Retailers maintain the Php500 price by reducing product sizes (shrinkflation) and substituting cheaper ingredients.
  - num: The Php500 basket represents 77% of the daily minimum wage (Php645) in NCR.
  - num: Food comprises 43% of total household spending, and up to 60% among the poorest 30% of households.
  - num: Poverty incidence among farmers and fisherfolk remains high at 27.0% and 27.4%, respectively, in 2023.
key_figures_tables:
  - Table 1: Food CPI in NCR (2018-2025) → A Php500 basket now costs Php669.80, a 33.96% increase from 2018.
  - Table 2: Food CPI outside NCR (2018-2025) → A Php500 basket now costs Php643.28, a 28.66% increase from 2018.
  - Table 3: Commercial Php500 holiday basket (2018 vs 2025) → Product sizes reduced and ingredients substituted to maintain price.
  - Figure 1: Poverty incidence among basic sectors (2023) → Farmers and fisherfolk have the highest poverty incidence.
  - Figure 2: Household food expenditure share by income decile → Lowest income decile spends ~60% of income on food.
key_equations:
  - equation: Adjusted Cost = 500 × (CPI_current / CPI_base)
    explanation: Adjusts 2018 basket cost to current prices.
definitions:
  - term: Shrinkflation
    definition: The practice of reducing product size while maintaining the same price.
  - term: Product Substitution
    definition: Replacing higher-cost ingredients with lower-cost alternatives.
  - term: CPI
    definition: Consumer Price Index, a measure of the average change in prices over time.
  - term: FIES
    definition: Family Income and Expenditure Survey.
  - term: 4Ps
    definition: Pantawid Pamilyang Pilipino Program, a conditional cash transfer program.
critical_citations:
  - "[PSA, 2025b] — Provides the primary CPI data for the analysis."
  - "[Rojas et al., 2024] — Quantifies the impact of shrinkflation on food inflation."
  - "[Dekimpe & van Heerde, 2023] — Provides a research agenda on retailing and inflation."
relevance:
  topics:
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Directly analyzes the cultural tradition of Noche Buena and its financial implications.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: high
      justification: Focuses on holiday-specific spending and price inflation during the Noche Buena season.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: high
      justification: Examines the cost of a specific Filipino occasion (Noche Buena) and its affordability.
    - code: 3.C
      name: User-Defined Allocation Constraints
      relevance: medium
      justification: Highlights the financial constraint of a fixed Php500 budget for a specific purpose.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Critiques the flawed metric of a fixed price point as a policy benchmark.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: Provides context on the spending burden for low-income and minimum-wage earners.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: The pressure of holiday spending impacts a household's ability to save and manage goals.
  contribution: This policy brief directly informs Odin's design by providing empirical evidence on the erosion of purchasing power for Filipino households, particularly regarding culturally significant spending events. It justifies the need for Odin's expense categorization to account for seasonal price fluctuations and the impact of inflation. The findings on shrinkflation and product substitution highlight the importance of tracking item-level data and unit prices. Furthermore, the brief underscores the necessity for Odin's budget recommendation module to be sensitive to the real cost of living and to assist users in setting realistic, inflation-adjusted savings goals. It provides a strong foundation for contextualizing user financial data within the broader economic reality.
  directly_justifies:
    - The Php500 Noche Buena basket is a culturally significant financial benchmark for Filipino families.
    - Seasonal inflation and shrinkflation significantly distort the real value of holiday spending.
    - Low-income households dedicate a disproportionate share of their income to food, limiting other financial flexibility.
    - A budget recommendation system must account for regional price differences.
  limits:
    - None identified.
  mapping_rationale: A systematic scan across all 12 functional domains was conducted. The domains of 'Filipino Cultural Context' (2.A, 2.B, 2.D) were flagged as highly relevant, as the brief directly analyzes the cost of the culturally significant Noche Buena meal and its seasonal spending patterns. 'Expense Categorization' (3.C) was flagged as medium relevance, as it provides evidence for the need to track budget constraints. 'Existing Systems & Gaps' (4.B) was also medium, as it critiques the use of a static price point as a benchmark. 'Behavioral Profiling' (5.A) and 'Savings & Debt Management' (13.A) were assessed as contextual and medium, respectively, as they provide insights into user financial stress but are not the primary focus. Domains like 'Forecasting', 'Anomaly Detection', and 'Mobile-First Design' were considered and rejected as the brief does not address algorithmic or design methodologies. The brief's overall relevance to Odin is high, as it provides essential socio-economic context and data that directly justifies the need for a personalized, context-aware PFMS for Filipino young professionals.
limitations:
  - The analysis primarily uses CPI data and a single commercial basket as an example, which may not represent all variations in household consumption patterns.
remember_this:
  - A Php500 Noche Buena basket now costs Php643 to Php670 due to inflation.
  - Retailers use shrinkflation to keep prices low while reducing real value.
  - Food spending consumes 43% of household budgets and 60% for the poor.
  - The Php500 benchmark is unrealistic for minimum-wage earners.
  - Policy must shift to real cost-of-living data for holiday assistance.
```
---

## Paper 36: Carmona_summarized.md

**Source File:** `Carmona_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: local
title: Empowering Financial Well-Being: A Comprehensive Approach to Managing Personal Finances of Employees of San Pablo Colleges Medical Center
authors: Carmona, K. N.
year: 2025
venue: Journal of Third World Economics
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 7.A
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 13.A
  - 13.B
tldr: Employees at San Pablo Colleges Medical Center exhibit awareness of budgeting but lack consistent saving and debt management practices, highlighting a need for targeted financial literacy programs.
problem_and_motivation: Many individuals lack financial literacy, leading to impulsive spending and poor income management, which is exacerbated by rising living costs. Healthcare employees at SPCMC require tailored financial management strategies to meet essential needs and prepare for emergencies. Existing financial education efforts are insufficient to address the gap between awareness and consistent application of sound financial practices.
approach:
  - The study employed a mixed-methods approach combining surveys and interviews to gather data from SPCMC employees.
  - A quantitative research method was used with weighted mean as the statistical treatment for data analysis.
  - Participants were 150 employees selected through stratified random sampling to ensure a representative sample.
  - Data was analyzed to assess current financial practices, issues, and needs across budgeting, saving, spending, and debt management.
findings:
  - num: Most respondents (65%) do not engage in regular saving habits, saving only when money is leftover.
  - num: 65% of respondents have no existing financial liabilities, yet awareness of maintaining an emergency fund is very low (mean 1.70).
  - Respondents show strong awareness of budgeting (mean 4.03) but only some awareness of saving (mean 2.57) and debt management (mean 2.96).
  - Family and social factors significantly influence financial behaviors, with families often avoiding debt and social groups exerting peer influence on spending.
  - num: Respondents rarely keep savings intact for emergencies (mean 2.21) and often borrow to pay off existing debt (mean 4.34), indicating a debt cycle.
  - The overall application of personal finance strategies is inconsistent, with budgeting practiced often (mean 3.65) and saving rarely practiced (mean 2.33).
key_figures_tables:
  - Table 1: Knowledge of Personal Finance Management Strategies → Shows budgeting awareness is high (4.03) but emergency fund knowledge is very low (1.70).
  - Table 7: Application of Saving Strategies → Reveals emergency fund saving is never practiced (1.23) and overall saving is rare (2.33).
  - Table 9: Application of Debt Management Strategies → Indicates respondents often borrow to pay off debt (4.34) yet rarely have loans exceeding 10% of salary (2.16).
  - Table 10: Summary of Application of Strategies → Overall financial management application is sometimes practiced (3.23), with saving being the weakest area.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Financial well-being
    definition: An individual's perception of their ability to meet current and future consumption demands and remain self-sufficient in financial matters.
  - term: Weighted mean
    definition: A statistical treatment used to interpret the average of responses based on assigned weights in Likert scale surveys.
  - term: SDT
    definition: Self-Determination Theory, a framework for understanding motivation and its influence on financial behavior.
critical_citations:
  - "[Brüggen et al., 2017] — Defines financial well-being as subjective perception of financial ability."
  - "[Lusardi and Mitchell, 2017] — Links higher financial literacy to better long-term financial outcomes."
  - "[Strömbäck et al., 2017] — Explains how self-control predicts financial behavior and well-being."
  - "[Di Domenico et al., 2022] — Applies Self-Determination Theory to personal financial management motivation."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: The study focuses on Filipino employees (healthcare workers) who are a subset of the young professional demographic.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: It details income brackets (e.g., 15,001-20,000 pesos) and saving habits of this professional group.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly examines financial behaviors including budgeting, saving, spending, and debt management practices.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Discusses family and social influences on financial decisions, reflecting cultural norms around debt and spending.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: Mentions the 50-30-20 rule as a spending guideline, providing a framework for categorization.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: low
      justification: Touches on spending categories (needs vs. wants) but does not deeply explore design.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides background on the general state of financial literacy and management practices in the Philippines.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies a significant gap between financial awareness and consistent application of saving and debt management strategies.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Profiles behaviors such as thriftiness and peer-influenced spending, indicating behavioral patterns.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: low
      justification: Implicitly touches on initial financial habits but does not directly address the cold-start problem.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: The study assesses awareness and application of budgeting strategies as a core financial management practice.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Not directly addressed, but the context of a workplace financial wellness program implies data handling.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: Not directly addressed, though trust in micro-financing institutions is implied through their frequent use.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: contextual
      justification: The proposed financial literacy program suggests a need for engagement, but the study does not analyze engagement dynamics.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: low
      justification: Not addressed, though a comprehensive program could include such mechanisms.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: Directly investigates saving behaviors, the lack of emergency funds, and inconsistent saving practices.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: Extensively analyzes debt management strategies, including borrowing habits and loan repayment practices.
  contribution: This study provides empirical evidence on the financial literacy and management gaps among Filipino healthcare employees, which can inform the design of a financial literacy module within Odin. The findings on the inconsistency between budgeting awareness and saving application directly justify the need for a proactive savings feature in Odin that nudges users to save first. The data on borrowing to pay off debt highlights the importance of an integrated debt management feature that can break this cycle. The identification of strong family and social influences suggests Odin's social features could be designed to promote positive financial norms. The recommended comprehensive program aligns with Odin's goal of providing a holistic PFMS for Filipino young professionals.
  directly_justifies:
    - "Employees demonstrate awareness of budgeting but lack consistent saving and debt management application."
    - "A significant gap exists in maintaining emergency funds equivalent to four to seven months of expenses."
    - "Social and family factors significantly influence individual financial behaviors and decisions."
    - "A structured financial literacy program is recommended to address gaps in knowledge and practice."
    - "Regular saving is often a reactive behavior dependent on leftover income rather than a planned strategy."
  limits:
    - "The study is limited to employees of a single medical center, limiting generalizability to all Filipino young professionals."
    - "Relies on self-reported data, which may be subject to social desirability bias."
    - "The cross-sectional design captures a snapshot in time and does not track changes in financial behavior over time."
    - "Does not evaluate specific algorithmic or technological solutions for personal finance management."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was conducted. The paper was found to be highly relevant to Domain 1 (Filipino Cultural Context) through topics 1.A, 1.B, and 1.C, as it profiles Filipino healthcare employees' financial structure and behaviors. Domain 3 (Expense Categorization) was flagged as contextual via 3.A and low via 3.B, as the paper mentions the 50-30-20 rule but does not deeply explore category design. Domain 4 (Existing Systems & Gaps) received high relevance via 4.B, as the study identifies a clear gap in saving and debt management application. Domain 5 (Behavioral Profiling) was considered medium for 5.A due to the behavioral patterns identified and low for 5.B, as the cold-start problem is not addressed. Domain 7 (Budget Recommendation) was flagged as medium via 7.A, as budgeting strategy knowledge is a key finding. Domain 10 (Data Privacy) and Domain 11 (Retention) were assigned low or contextual relevance as they are not directly addressed but are implied in the context of workplace programs. Domains 6 (Forecasting), 8 (Anomaly Detection), 9 (Mobile-First Design), and 12 (Evaluation) were considered and rejected as the study does not address algorithmic prediction, anomaly detection, mobile UX, or system evaluation frameworks. The borderline case of seasonal spending (2.B and 2.D) was considered but rejected as the study focuses on general financial behavior rather than seasonal patterns. The paper provides a foundational understanding of financial behaviors and gaps among a key target demographic for Odin, justifying the inclusion of modules for budgeting, saving, and debt management.
limitations:
  - "The study's findings are based on a sample from a single institution, which may not represent the broader population of Filipino young professionals."
  - "The methodology relies heavily on self-reported awareness and practices, which may not align with actual financial behaviors."
  - "The study does not propose or evaluate a specific technological intervention for financial management."
  - "The long-term effectiveness of the proposed financial literacy program is not empirically tested."
  - "Potential confounding variables such as education level or financial background were not thoroughly controlled."
remember_this:
  - "Budgeting awareness is high among Filipino healthcare employees."
  - "Saving and emergency fund practices are critically weak."
  - "Debt management is often cyclical, with borrowing used to pay off existing debt."
  - "Family and social influences are strong drivers of financial behavior."
  - "A comprehensive financial literacy program is needed to bridge the awareness-action gap."
```
---

## Paper 37: Velez_summarized.md

**Source File:** `Velez_summarized.md`

```yaml
paper_id: 10.69569/jip.2025.056
designation: local
title: A Systematic Review of Mobile Banking, Fintech Innovations, and Regulatory Gaps to Achieve Financial Inclusion in the Philippines
authors: Velez, G.
year: 2025
venue: Journal of Interdisciplinary Perspectives
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 7.B
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 11.A
  - 12.A
  - 13.A
tldr: Mobile banking and fintech have expanded financial access in the Philippines but persistent digital, gender, and literacy gaps continue to exclude marginalized populations.
problem_and_motivation: Financial inclusion in the Philippines remains low, with 68% of adults unbanked, despite the growth of mobile banking and fintech. A comprehensive synthesis of how these technologies, along with regulatory frameworks, affect marginalized communities is lacking. This review addresses that gap to inform more equitable policy and design.
approach:
  - The study conducted a systematic literature review following PRISMA guidelines.
  - Searches were performed in ProQuest and Google Scholar using Boolean strings for digital financial inclusion in the Philippines.
  - Inclusion criteria covered peer-reviewed articles, policy papers, and grey literature from 2014 to 2024 focusing on the Philippines.
  - Data extraction and synthesis used narrative synthesis and thematic analysis to identify recurring themes.
  - The review analyzed 26 studies meeting quality criteria, comprising journal articles, policy papers, institutional reports, and a thesis.
findings:
  - num: Mobile banking adoption surged 18-35% post-2019, driven by platforms like GCash and pandemic-induced digitization.
  - num: GCash reduced cash dependency by 41% in urban and 29% in rural areas.
  - num: Women-owned MSMEs comprise only 22% of fintech borrowers despite being 39% of entrepreneurs.
  - num: Only 34% of low-income users understand digital payment security features.
  - The National Retail Payment System drove a 19% increase in digital transaction volumes but struggles with fragmentation and rural implementation.
  - Rural adoption rates are 1.8 times lower than urban areas due to infrastructure and connectivity gaps.
  - The pandemic accelerated digitization but increased exclusion for 28% of low-literacy users.
key_figures_tables:
  - Table 4: Summary of 26 studies on digital financial inclusion → Highlights key findings on access, barriers, and demographic disparities.
  - Figure 1: PRISMA flow diagram of study selection → Documents the systematic review process from 1,296 records to 26 included studies.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: MSMEs
    definition: Micro, small, and medium-sized enterprises.
  - term: NRPS
    definition: National Retail Payment System, a Philippine regulatory framework for digital transactions.
  - term: PRISMA
    definition: Preferred Reporting Items for Systematic Reviews and Meta-Analyses, a guideline for conducting systematic reviews.
  - term: Fintech
    definition: Financial technology used to deliver financial services digitally.
critical_citations:
  - "[BSP, 2023] — Provides baseline unbanked rate of 68% for the Philippines."
  - "[Molina, 2024] — Documents specific cash dependency reductions by GCash."
  - "[ADB, 2024] — Reports gender disparity in fintech borrowing among women-owned MSMEs."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: Provides demographic context on unbanked adults and digital adoption trends.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Discusses income, urbanization, and remittance factors influencing financial access.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: low
      justification: Touches on adoption behaviors but not specifically for young professionals.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Identifies gender norms and remittance reliance as cultural financial practices.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Mentions weather-related income fluctuations in fishing communities but not a central focus.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: References remittance-driven financial behavior but does not detail spending cycles.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: low
      justification: Discusses digital payments broadly, without specific categorization frameworks.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: low
      justification: Not directly addressed; the focus is on access, not categorization.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Reviews the Philippine fintech landscape, specifically platforms like GCash and Maya.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Documents persistent digital divide, gender gaps, and literacy barriers as system limitations.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: low
      justification: Mentions demographic and socioeconomic factors but does not construct behavioral profiles.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Discusses fintech use of alternative data for credit scoring, a form of behavioral classification.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Implicitly relevant through financial inclusion but not focused on budget recommendation.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: high
      justification: Highlights smartphone penetration and mobile banking as primary access channels.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Notes that low-literacy users struggle with digital interfaces, implying UX gaps.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Reports that only 34% of low-income users understand digital security features.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Security, trust, and reliability are identified as key factors for adoption and continued use.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: Mentions adoption surge but does not analyze engagement dynamics.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: contextual
      justification: Uses systematic review methodology rather than evaluating a specific system.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: Remittances and bank account holding are mentioned but not savings goal management.
  contribution: This review provides a comprehensive evidence base on the barriers to digital financial inclusion in the Philippines, which can inform Odin's design for targeting underserved demographics. It directly justifies the need for mobile-first solutions that address the digital divide, particularly for rural and low-income users. The findings on gender disparities and low financial literacy support the development of inclusive behavioral profiling and personalized financial education within Odin. The documented limitations of existing regulatory frameworks and fintech platforms highlight opportunities for Odin to differentiate itself through better user support and trust-building mechanisms.
  directly_justifies:
    - Rural adoption rates are 1.8 times lower than urban areas, necessitating mobile-first design for low-connectivity environments.
    - Only 34% of low-income users understand digital security, justifying simplified security communication in app interfaces.
    - Women-owned MSMEs represent only 22% of fintech borrowers despite comprising 39% of entrepreneurs, supporting gender-sensitive product design.
    - The digital divide in regions like Visayas and Mindanao creates unique challenges for financial behavior profiling.
  limits:
    - The review primarily synthesizes cross-sectional studies (80%), limiting causal inference for Odin's forecasting modules. [unacknowledged]
    - The review does not evaluate specific algorithms for expense categorization, anomaly detection, or budget recommendation. [unacknowledged]
    - The focus on financial inclusion may not directly translate to behavioral profiling or spending forecasting for young professionals.
  mapping_rationale: A systematic scan across all 12 functional domains identified the strongest relevance to Existing Systems & Gaps (high), Mobile-First Design (high), and User Trust (high), as the paper directly reviews the Philippine fintech landscape, documents adoption barriers, and identifies trust as a key adoption factor. Medium relevance was assigned to Filipino Cultural Context for its discussion of gender norms and remittance reliance, and to Behavioral Profiling for its mention of alternative credit scoring. Low relevance was assigned to Expense Categorization and Budget Recommendation due to the absence of specific frameworks. Contextual relevance was assigned to Seasonal Spending and Evaluation Frameworks, as these are mentioned but not central. Domains such as Anomaly Detection, Forecasting, and Savings/Debt Management were considered but rejected due to lack of direct coverage. The paper's overall relevance to Odin is moderate, providing foundational context on user demographics and systemic gaps rather than algorithmic or design-specific insights.
limitations:
  - The review relies on secondary sources, not primary data collection.
  - A small number of studies (26) were included after screening.
  - The methodological quality of included studies varies.
  - The focus is on financial inclusion broadly, not specifically on young professionals or PFMS. [unacknowledged]
  - The review does not provide a detailed analysis of specific fintech algorithms or system architectures. [unacknowledged]
remember_this:
  - Mobile banking adoption surged 18-35% post-2019 in the Philippines.
  - Women-owned MSMEs are underrepresented in fintech borrowing at 22%.
  - Only 34% of low-income users understand digital payment security.
  - Rural adoption rates are 1.8 times lower than in urban areas.
  - The digital divide and low literacy are key barriers to financial inclusion.
```
---

## Paper 38: Quindoza et al_summarized.md

**Source File:** `Quindoza et al_summarized.md`

```yaml
paper_id: 10.1108/SEAMJ-09-2024-0063
designation: local
title: Ang tagapagtaguyod na anak for Filipino adults: an exploratory research
authors: Quindoza, T.L.V.; Malcampo, M.C.; Rungduin, T.
year: 2025
venue: Southeast Asia: A Multidisciplinary Journal
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 4.A
  - 5.A
  - 5.B
  - 13.A
tldr: Explores the "tagapagtaguyod na anak" role in Filipino families as providing financial, emotional, and social support shaped by parental expectations and child volition.
problem_and_motivation: The breadwinner role in Filipino families lacks contextualization and is viewed narrowly as financial provision. There is a paucity of research on the broader responsibilities and cultural underpinnings of this role.
approach:
  - Explored perceptions of 16 Filipino adults in Metro Manila using semi-structured interviews.
  - Participants included single adult children aged 18-29 and middle-aged parents aged 40-60.
  - Thematic analysis was applied to identify patterns in understanding the phenomenon.
  - The study used an exploratory qualitative design to define the role and its influencing factors.
  - Findings were validated through participant and peer review.
findings:
  - "num: Majority of participants define tagapagtaguyod as nagbibigay (providing basic needs)."
  - The role involves financial, emotional, and social support, extending beyond a purely financial provider.
  - Eldest children are typically seen as fulfilling the role, but some participants associate it with middle children.
  - The role is influenced by extrinsic factors like poverty, parental incapacity, and intrinsic factors like volition and sense of responsibility.
  - Single adult children view the phenomenon negatively as unjust and mentally taxing, while parents view it positively as a sign of responsibility.
  - The phenomenon is rooted in Filipino values of family-orientedness and utang na loob.
key_figures_tables:
  - "Figure 1: Thematic map of understanding → Defines role via providing, bearing, leading, lifting."
  - "Figure 2: Thematic map of influencing factors → Shows extrinsic (poverty) and intrinsic (volition) factors."
  - "Figure 3: Thematic map of perspectives → Contrasts negative child views with positive parent views."
  - "Figure 4: Thematic map of Filipino values → Links role to family-orientedness and utang na loob."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Tagapagtaguyod na anak
    definition: A Filipino child who provides financial, emotional, and social support to their family.
  - term: Tagasalo
    definition: A personality or syndrome where a family member assumes caregiving or leadership roles.
  - term: Utang na loob
    definition: A Filipino value of gratitude or reciprocity towards family and others.
critical_citations:
  - "[Carandang, 1987] — Foundation for tagasalo theory used as study basis."
  - "[Udarbe, 2001] — Defines tagasalo personality themes for comparison."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Directly studies Filipino adults aged 18-29 as breadwinners.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Describes financial support roles and obligations within families.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Explores attitudes and motivations behind financial provision.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Examines the culturally rooted practice of familial financial support.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Mentions poverty as a driver, but not specific seasonal patterns.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Family needs context may imply spending cycles, but not central.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Mentions breadwinner phenomenon but not technology systems.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Profiles the tagapagtaguyod role and associated personality traits.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: low
      justification: Discusses role formation but not cold-start computational issues.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: Mentions financial support for family, but not savings goal systems.
  contribution: This paper informs Odin's user profiling module by describing the cultural and behavioral profile of a Filipino young professional who acts as a family financial provider. It directly supports the design of expense categorization by defining the types of support (financial, emotional) that shape spending. The findings on utang na loob and family-orientedness justify features that accommodate familial financial obligations in budget recommendations.
  directly_justifies:
    - "Filipino young adults often provide financial, emotional, and social support to their families."
    - "Cultural values like utang na loob and family-orientedness are central to financial behavior."
    - "The role is influenced by parental expectations and the child's sense of responsibility."
  limits:
    - "Findings are based on a small sample from Metro Manila only. [unacknowledged]"
    - "Predominance of female participants may have biased perceptions of gender roles. [unacknowledged]"
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The paper was found highly relevant to the Filipino Cultural Context domain (2.A, 2.D) and Behavioral Profiling (5.A) due to its detailed description of the culturally specific breadwinner role. It provided medium relevance to Financial Structure (1.B) and Financial Behavior (1.C) as it outlines the financial support dynamics. Low relevance was assigned to Expense Categorization (3.A) and Landscape of Existing Systems (4.A) because the paper focuses on the role itself rather than categorization systems or technology. Domains like Forecasting (6), Budget Recommendation (7), Anomaly Detection (8), and Mobile Design (9) were rejected as the paper does not address predictive modeling, algorithmic budget allocation, or UX design. The overall relevance to Odin lies in its rich contextual data on Filipino financial behavior and familial obligations.
limitations:
  - "Small sample size from Metro Manila limits generalizability. [unacknowledged]"
  - "Predominance of female participants may have biased perceptions. [unacknowledged]"
  - "The study captures perceptions, not lived experiences of tagapagtaguyod."
remember_this:
  - "Tagapagtaguyod na anak provides financial, emotional, and social support."
  - "Poverty and parental incapacity are key drivers of the role."
  - "Single adult children view the role as unjust and mentally taxing."
  - "The role is rooted in family-orientedness and utang na loob."
  - "Perceptions of the role differ significantly between generations."
---

## Paper 39: Espiritu M.-2025_summarized.md

**Source File:** `Espiritu M.-2025_summarized.md`

```yaml
paper_id: 10.69569/jip.2025.063a
designation: local
title: Knowledge, Attitudes, and Practices in Financial Literacy among Business Administration Students in Urban College in the Philippines
authors: Espiritu, M. J.
year: 2025
venue: Journal of Interdisciplinary Perspectives
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 3.A
  - 5.A
  - 10.A
tldr: Assesses financial knowledge, attitudes, and practices of business students in a Philippine urban college, finding significant links between demographics and financial literacy.
problem_and_motivation: Filipino young adults, particularly business students, exhibit low financial literacy, yet their specific knowledge, attitudes, and practices remain underexplored. Understanding these factors is critical for designing effective financial education. This study addresses this gap by examining these dimensions within a local urban college context.
approach:
  - Conducted a survey-based quantitative study with 2,313 Business Administration students at a college in Quezon City.
  - Employed a structured questionnaire to measure financial knowledge, attitudes, and practices across five concepts: income, expenses, debt, credit, and savings.
  - Used descriptive statistics to assess mean scores and inferential statistics (ANOVA) to analyze differences based on demographic profiles.
  - Examined the relationship between knowledge, attitudes, and practices using Pearson correlation.
findings:
  - num: Students generally agreed on their financial knowledge, with mean scores ranging from 2.98 to 3.13 for income, expenses, debt, credit, and savings.
  - num: A significant relationship exists between financial knowledge, attitudes, and practices (R=0.697, p=0.000).
  - Financial knowledge and attitudes varied significantly by age, sex, and year level, but monthly family income showed no significant effect on knowledge.
  - Financial practices varied significantly across all demographic variables: age, sex, monthly income, and year level.
  - Monthly family income significantly influenced attitudes but not knowledge, suggesting resource access affects attitudes more than comprehension.
key_figures_tables:
  - Table 1: Distribution of 2,313 respondents by age, sex, income, and year level → Majority are male (65.9%), aged 18-20 (48.9%), with income of 10,001-20,000 PHP.
  - Table 5: ANOVA results for demographic differences in KAP → Knowledge and attitudes vary by age and year level; practices vary by all demographics.
  - Table 6: Correlation among knowledge, attitude, and practice → Strong significant relationship, R=0.697, justifying the KAP framework.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: KAP
    definition: Knowledge, Attitudes, and Practices framework for assessing financial literacy.
  - term: PFMS
    definition: Personal Financial Management System.
critical_citations:
  - "[Lusardi, 2019] — Highlights the need for financial literacy due to complex financial products."
  - "[Chen & Volpe, 1998] — Foundational study on low financial literacy among college students."
  - "[Martinez, 2024] — Reports low financial literacy rates among Filipinos, providing context."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Directly studies Filipino college students, a primary demographic for Odin.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Provides baseline data on income, expenses, and debt understanding of students.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Assesses financial practices and attitudes, core to understanding behavior.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Grounds financial literacy in a Philippine urban college context, reflecting local norms.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: The study assesses understanding of fixed/variable expenses, informing category design.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly measures financial attitudes and practices, which are key for behavioral profiling.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Mentioned in introduction regarding cybersecurity risks, but not a focus.
  contribution: The paper provides empirical evidence on the financial literacy levels of Filipino business students, a key target demographic for Odin. It validates the KAP framework for understanding financial behavior in this population. The findings on demographic differences (age, sex, income) can inform how Odin personalizes its expense categorization and behavioral profiling modules. The strong correlation between knowledge and practices underscores the need for Odin's educational and feedback features to drive better financial outcomes.
  directly_justifies:
    - "Business students in the Philippines show significant variation in financial knowledge and practices by age and year level, requiring personalized system inputs."
    - "The strong relationship between financial knowledge, attitudes, and practices supports Odin's integrated approach to education and behavior change."
    - "Monthly family income significantly affects financial attitudes and practices, indicating a need for adaptive budgeting and savings recommendations in Odin."
  limits:
    - "The study uses self-reported data, which may not reflect actual financial behaviors."
    - "The sample is limited to business administration students, reducing generalizability to all young professionals."
    - "Focuses on knowledge assessment rather than testing actual financial decision-making skills."
  mapping_rationale: A systematic scan across all 12 functional domains was conducted. The paper was flagged as highly relevant to the 'Behavioral Profiling & Classification' and 'Filipino Cultural Context' domains due to its direct measurement of financial knowledge, attitudes, and practices among Filipino students. It provides medium relevance to 'Expense Categorization' as it assesses understanding of expense types, and low relevance to 'Data Privacy' due to a brief mention. Domains like 'Spending Forecasting', 'Budget Recommendation', and 'Anomaly Detection' were rejected as the paper does not address predictive modeling or algorithmic approaches. The paper's overall relevance to Odin is high, as it offers foundational behavioral data essential for profiling and personalizing the system for its Filipino user base.
limitations:
  - "Self-reported data may not accurately reflect actual financial practices."
  - "Sample limited to business students in one urban college, limiting generalizability."
  - "Cross-sectional design captures a snapshot, not longitudinal behavior change."
  - "The instrument's internal consistency for financial knowledge (0.459) is low, suggesting potential measurement issues [unacknowledged]."
remember_this:
  - "Financial literacy levels among Filipino business students vary significantly by age, sex, and year level."
  - "Strong correlation exists between financial knowledge, attitudes, and practices in this population."
  - "Monthly family income affects financial attitudes and practices but not knowledge, highlighting a critical insight for financial education."
  - "The KAP framework is validated for assessing financial literacy among Filipino students."
```
---

## Paper 40: Romero_summarized.md

**Source File:** `Romero_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: local
title: Buy-Now-Pay-Later Adoption, Debt Stress, and Repurchase Intention among Filipinos Gen Z Consumers: The Mediating Role of Budgeting Self-Efficacy
authors: Romero, M. A.
year: 2025
venue: Oikonomia Review: Journal of Economics, Management, and Accounting
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.C
  - 3.C
  - 5.A
  - 5.B
  - 5.C
  - 7.A
  - 7.B
  - 7.D
  - 8.A
  - 11.A
  - 11.B
  - 13.A
  - 13.B
tldr: BNPL adoption among Filipino Gen Z is driven by convenience and promotions, increasing repurchase intention but also debt stress, while budgeting self-efficacy and transparency reduce negative outcomes.
problem_and_motivation: BNPL services can simultaneously drive commerce growth and create consumer welfare risks, yet the psychological mechanisms linking adoption to repurchase intention remain unclear. Understanding how debt stress and budgeting self-efficacy mediate this relationship is essential for designing platforms that support sustainable use. The role of transparency in fostering self-efficacy and reducing stress has not been adequately examined in the Filipino Gen Z context.
approach:
  - Quantitative explanatory design using cross-sectional survey data from 602 Filipino Gen Z consumers aged 18-27 who had used BNPL at least twice in three months.
  - Partial Least Squares Structural Equation Modeling (PLS-SEM) tested direct and mediated effects among perceived convenience, promotional attractiveness, transparency, BNPL adoption intensity, debt stress, budgeting self-efficacy, and repurchase intention.
  - All constructs measured with validated multi-item five-point Likert scales; bootstrapping supported inference for indirect effects.
findings:
  - Perceived convenience and promotional attractiveness positively associated with BNPL adoption intensity.
  - Perceived transparency positively associated with BNPL adoption intensity and budgeting self-efficacy.
  - BNPL adoption intensity positively associated with repurchase intention and debt stress.
  - Debt stress negatively associated with repurchase intention.
  - Budgeting self-efficacy negatively associated with debt stress and positively associated with repurchase intention.
  - Budgeting self-efficacy mediates the transparency-debt stress relationship; debt stress partially mediates the adoption-repurchase intention relationship; serial mediation via self-efficacy and stress is supported.
key_figures_tables:
  - Table 1: Measurement model summary establishing reliability, convergent validity, and discriminant validity for all constructs.
  - Table 2: Hypotheses testing summary confirming all direct and mediated relationships, with partial mediation for debt stress.
  - Table 3: Mechanism summary interpreting convenience/promotions, adoption-stress-repurchase, and transparency-self-efficacy-stress pathways.
  - Figure 1: SEM path diagram specifying the theory-driven structure of BNPL adoption, stress, self-efficacy, and repurchase intention relationships.
  - Figure 2: Mediation model illustrating dual pathways from adoption to repurchase intention via debt stress, with transparency and budgeting self-efficacy as protective levers.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: BNPL
    definition: Buy-Now-Pay-Later, a short-term consumer credit embedded in digital checkout.
  - term: Debt Stress
    definition: Psychological burden from repayment obligations, late fees, and perceived loss of financial control.
  - term: Budgeting Self-Efficacy
    definition: Confidence in tracking installments, planning cashflow, and resisting impulsive use.
  - term: Perceived Transparency
    definition: Clarity of fees, due dates, penalties, and total repayment amounts.
  - term: PLS-SEM
    definition: Partial Least Squares Structural Equation Modeling, a variance-based SEM method.
critical_citations:
  - "[Schomburgk & Hoffmann, 2023] — Mindfulness reduces BNPL usage and improves well-being."
  - "[Simiyu et al., 2025] — Self-efficacy and facilitating conditions influence BNPL borrowing."
  - "[Widayati et al., 2024] — Promotions and design features drive Gen Z BNPL behavior."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Focuses specifically on Filipino Gen Z consumers aged 18-27, a core Odin demographic.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Examines income irregularity, liquidity constraints, and short-term smoothing needs of young Filipinos.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly investigates spending behavior, BNPL usage, repurchase intention, and debt stress in the target segment.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Provides empirical data on BNPL use within the Filipino cultural and digital commerce context.
    - code: 2.C
      name: User-Declared Financial Preferences
      relevance: medium
      justification: Captures self-reported perceptions of convenience, transparency, and promotional appeal, informing preference modeling.
    - code: 3.C
      name: User-Defined Allocation Constraints
      relevance: medium
      justification: Budgeting self-efficacy reflects user-perceived ability to allocate and constrain spending, relevant to constraint handling.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Identifies behavioral profiles via stress and self-efficacy levels, relevant to classification.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: contextual
      justification: Discusses heterogeneity and segmentation; provides background for profile dynamics but no cold-start methods.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Uses PLS-SEM for hypothesis testing, not classification; tangential to classification approaches.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Budgeting self-efficacy is a core construct, providing domain knowledge on how confidence affects financial outcomes.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Findings on transparency and self-efficacy can inform design of budget recommendations that reduce stress and support healthy use.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: contextual
      justification: Discusses infeasibility when repayment congestion occurs; provides context but not algorithmic handling methods.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Tangential; debt stress and repayment congestion could inform anomaly signals but not directly about detection.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: Repurchase intention and stress-driven avoidance directly relate to engagement dynamics and sustainability.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: high
      justification: Transparency and self-efficacy are identified as mechanisms to reduce churn and support retention, directly informing engagement design.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: Tangential; budgeting self-efficacy relates to spending control, not explicit savings goal management.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: Directly studies debt stress and strategies to manage BNPL obligations, informing debt management features.
  contribution: The paper's mechanism-based account of BNPL behavior provides empirical justification for Odin's design to incorporate budgeting self-efficacy as a protective factor. The finding that transparency strengthens self-efficacy directly supports Odin's need for clear, legible information displays. The dual pathway model (adoption→repurchase vs. adoption→stress→reduced repurchase) informs Odin's anomaly detection and engagement modules by highlighting stress as a predictor of churn. The emphasis on micro-interventions and contextual nudges justifies Odin's mobile-first approach to delivering decision aids at the point of purchase.
  directly_justifies:
    - "Budgeting self-efficacy reduces debt stress and supports healthier repurchase behavior."
    - "Transparency strengthens budgeting self-efficacy and reduces harmful outcomes."
    - "BNPL adoption increases repurchase intention but also elevates debt stress, which reduces future engagement."
    - "Micro-interventions embedded in app interfaces can strengthen self-efficacy and reduce stress."
  limits:
    - "Cross-sectional design restricts temporal inference; stress may accumulate over time [unacknowledged]."
    - "Self-reported adoption intensity may not align with objective transaction data [unacknowledged]."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to domains related to Filipino Cultural Context (Topic 2.A), Expense Categorization (3.C via self-efficacy), Behavioral Profiling (5.A), Budget Recommendation (7.A), Engagement (11.A, 11.B), and Debt Management (13.B). It provides medium relevance to Seasonal Patterns (2.B, 2.D) and User Preferences (2.C) through its discussion of promotions and transparency, though not directly addressing cyclicality. Domain 6 (Forecasting) and Domain 12 (Evaluation) were rejected as the paper does not address predictive modeling or system evaluation frameworks. Borderline cases included Topic 7.D (infeasibility handling), which was marked contextual because the paper discusses repayment congestion but not algorithmic reduction hierarchies. Topic 5.B (profile dynamics) was also marked contextual as it mentions segmentation but does not address cold-start issues. Topic 8.A (anomaly detection) was marked low due to tangential relevance to stress as an outcome signal. The overall relevance is high for informing Odin's behavioral, engagement, and debt management modules, though the paper is primarily a behavioral study rather than a computational systems paper.
limitations:
  - "Cross-sectional design restricts temporal causal inference. [unacknowledged]"
  - "Self-reported adoption and stress measures may introduce common method bias. [unacknowledged]"
  - "Sample limited to university and online panel networks, may not fully represent all Filipino Gen Z consumers. [unacknowledged]"
  - "No objective transaction data to validate self-reported BNPL adoption intensity. [unacknowledged]"
remember_this:
  - "BNPL adoption increases repurchase intention but also elevates debt stress."
  - "Budgeting self-efficacy reduces stress and supports healthier BNPL use."
  - "Transparency strengthens self-efficacy, serving as a protective mechanism."
  - "Debt stress partially mediates the adoption-repurchase intention relationship."
  - "Micro-interventions can enhance self-efficacy and reduce repayment congestion."
```
---

## Paper 41: Templa et al_summarized.md

**Source File:** `Templa et al_summarized.md`

```yaml
paper_id: "10.70838/pemj.380810"
designation: "local"
title: "The Influence of Financial Literacy on the Budgeting Practices among College Students in a Private Catholic School: Input for Student Literacy Program"
authors: "Templa, E. L.; Andea, R. J. B.; Bagahansol, J. D. M.; Carreon, R. B.; Comendador, L. G.; Labrador, J. G.; Miscreola, D. J. V.; Tapay, A. J. D.; Uson, P. G. R. A."
year: 2025
venue: "Psychology and Education: A Multidisciplinary Journal"
odin_topics:
  - "1.A"
  - "1.B"
  - "1.C"
  - "2.A"
  - "2.B"
  - "2.D"
  - "3.A"
  - "4.A"
  - "4.B"
  - "5.A"
  - "7.A"
  - "7.B"
  - "7.D"
  - "10.A"
  - "10.B"
  - "12.A"
  - "12.B"
  - "12.C"
tldr: "Financial literacy shows a strong positive correlation with budgeting practices among Filipino college students, explaining 75% of the variance in their budgeting behaviors."
problem_and_motivation: "Many college students in the Philippines demonstrate poor budgeting methods and struggle to manage limited funds, indicating a gap between financial knowledge and practical application. While financial literacy is recognized as crucial for sound financial decisions, there is limited research on smaller institutions like private Catholic schools with unique socioeconomic contexts. Understanding this relationship is essential for developing targeted educational interventions to improve student budgeting skills and financial well-being."
approach:
  - "The study employed a quantitative descriptive-correlational research design with 225 randomly selected college students from a private Catholic school in Davao City."
  - "Data were collected using a validated researcher-constructed survey instrument measuring five dimensions of financial literacy and four aspects of budgeting practices."
  - "The survey instrument underwent face validation, pilot testing, and internal reliability testing using Cronbach's alpha, achieving excellent reliability (α = .998 overall)."
  - "Statistical analyses included descriptive statistics (mean, standard deviation), Pearson's R correlation, and linear regression to examine relationships and influences."
findings:
  - "num: Students demonstrated a high overall level of financial literacy (M = 3.95, SD = 0.82), with attitudes toward finance and money being the strongest dimension (M = 4.03)."
  - "Managing financial risk was identified as the area requiring the most improvement among financial literacy dimensions (M = 3.82)."
  - "Students exhibited effective budgeting practices (M = 3.91), with decision-making as the strongest dimension (M = 4.03) and financial control as the weakest (M = 3.77)."
  - "A strong, statistically significant positive correlation exists between financial literacy and budgeting practices (r = 0.85, p < 0.001)."
  - "num: Financial literacy accounts for approximately 75% of the variance in budgeting practices (R² = .723, Adjusted R² = .722)."
  - "Regression analysis revealed financial literacy significantly enhances budgeting behavior (Beta = 0.896, T-value = 24.12, P-value = 0.000)."
  - "Students favored immediate financial needs over long-term planning, reflecting a gap between knowledge and consistent application of budgeting skills."
  - "Financial awareness was high (M = 4.00), but variability in scores indicates inconsistent financial understanding among some students."
key_figures_tables:
  - "Table 1: Financial literacy levels across indicators → Overall mean of 3.95 (High), with risk management lowest at 3.82."
  - "Table 2: Budgeting practices across indicators → Overall mean of 3.91 (High), with decision-making highest at 4.03."
  - "Table 3: Correlation analysis between financial literacy and budgeting skills → Strong positive correlation r = 0.85, p < 0.001."
  - "Table 4: Regression analysis → Financial literacy accounts for 75.1% of variance in budgeting practices, Beta = 0.896, p = 0.000."
key_equations:
  - equation: "r = 0.85, p < 0.001"
    explanation: "Strong positive correlation between financial literacy and budgeting practices."
  - equation: "R² = 0.723, Adjusted R² = 0.722"
    explanation: "Financial literacy explains 72.3% of variance in budgeting behavior."
definitions:
  - term: "Financial Literacy"
    definition: "The set of knowledge and skills necessary to make sound and practical financial choices, encompassing financial awareness, attitudes, risk management, culture, and knowledge."
  - term: "Budgeting Practices"
    definition: "The financial management behaviors involving goal setting, financial control, decision-making, and financial behavior."
  - term: "Theory of Planned Behavior (TPB)"
    definition: "A theory explaining that behavior is influenced by intentions shaped by attitudes, subjective norms, and perceived behavioral control."
  - term: "Financial Literacy Theory"
    definition: "A framework positing that financial literacy equips individuals to make informed decisions about spending, saving, and investing."
critical_citations:
  - "[Lusardi & Mitchell, 2020] — Emphasizes importance of financial education for promoting sound financial behaviors."
  - "[Sanjeev, 2023] — Budgeting is fundamental to financial literacy, requiring allocation of income."
  - "[Huston, 2010] — Financial literacy involves both understanding and application of financial concepts."
  - "[Ajzen, 1991] — Theory of Planned Behavior explains how attitudes and control influence financial intentions."
  - "[Klapper & Lusardi, 2020] — Financial literacy and risk management skills are essential for financial resilience."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "high"
      justification: "Study directly examines Filipino college students as the target demographic for Odin's young professional users."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "medium"
      justification: "Provides data on financial literacy and budgeting behaviors of Filipino students entering the workforce."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Directly measures financial behavior and budgeting practices among Filipino college students."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "high"
      justification: "Study context is a private Catholic school in Davao City, reflecting culturally specific financial practices."
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "low"
      justification: "Mentions challenges with unpredictable expenses and impulsive spending, but does not focus on seasonal cycles specifically."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "low"
      justification: "Discusses spending habits and financial behavior in a Philippine context but does not specifically analyze 'occasions'."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "contextual"
      justification: "Provides background on budgeting practices but does not propose specific expense categorization methods."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Reviews financial literacy landscape in the Philippines, including BSP initiatives, but not specific systems."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "low"
      justification: "Identifies gap in financial literacy education and application, relevant to system design gaps."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "contextual"
      justification: "Provides foundational understanding of financial behaviors that could inform profiling approaches."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "medium"
      justification: "Documents budgeting strategies and practices among students, providing domain knowledge for budget recommendation systems."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "contextual"
      justification: "Findings on budgeting practices could inform how budget recommendations might be tailored to students."
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "contextual"
      justification: "Students' struggles with financial control and unpredictable expenses suggest need for flexible handling mechanisms."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "contextual"
      justification: "Study's ethical considerations mention Data Privacy Act of 2012, relevant to data privacy in PFMS."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "contextual"
      justification: "Implications for building trust through effective financial education and support, relevant to system adoption."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Uses correlation and regression analysis methodologies that could inform evaluation frameworks for Odin modules."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "low"
      justification: "Methodology of correlational analysis could apply to evaluating behavioral profiling or forecasting modules."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "low"
      justification: "Correlational and regression approach could inform evaluation of budget recommendation effectiveness."
  contribution: "This study demonstrates that financial literacy is a key determinant of budgeting practices among Filipino college students, with the relationship being strong and statistically significant. The findings validate the Financial Literacy Theory and Theory of Planned Behavior in a Philippine context, providing empirical support for integrating financial education into Odin's design. The study's quantitative framework can inform the evaluation of Odin's recommendation and forecasting modules, particularly in measuring the impact of behavioral interventions on user outcomes."
  directly_justifies:
    - "Financial literacy explains 75% of the variance in budgeting practices among Filipino college students."
    - "Students with higher financial literacy demonstrate stronger goal setting, financial control, and decision-making skills."
    - "Managing financial risk is an area requiring improvement, suggesting need for targeted educational content in Odin."
    - "Positive financial attitudes correlate with responsible budgeting behaviors, supporting behavior-focused system features."
  limits:
    - "The study uses self-reported data, which may introduce biases in respondents' assessments of their financial literacy and budgeting practices. [unacknowledged]"
    - "The study does not account for external factors such as socioeconomic background or exposure to financial education outside the classroom. [unacknowledged]"
    - "The sample is limited to students from a single private Catholic school in Davao City, which may limit generalizability to other demographics. [unacknowledged]"
    - "The study does not explore the influence of emerging technologies like AI or machine learning on budgeting practices, representing a gap in the literature. [acknowledged]"
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was conducted. The paper was flagged as highly relevant to Filipino Cultural Context (Topics 2.A, 2.D) as it studies Filipino students, and to Behavioral Profiling & Classification (Topics 1.A, 1.C) through its detailed measurement of financial behaviors. Medium relevance was assigned to Budget Recommendation (Topics 7.A, 7.B) and System Evaluation (Topic 12.A) due to the study's quantitative analysis that can inform Odin's recommendation and evaluation modules. Contextual relevance was identified for Expense Categorization (Topic 3.A) and Data Privacy (Topics 10.A, 10.B) due to mentions of privacy considerations. Low relevance was assigned to Seasonal Spending (Topics 2.B, 2.D) and Algorithmic Forecasting (Topics 6.A, 6.B) as the study does not address predictive modeling. Borderline cases included Topics 1.A and 2.A, which were both selected due to the dual demographic and cultural focus. Topics related to Anomaly Detection (Topics 8.A, 8.B, 8.C), User Retention (Topics 11.A, 11.B), and Savings & Debt Management (Topics 13.A, 13.B, 13.C) were considered and rejected as the paper does not address these specific PFMS functionalities. Overall, the paper is moderately relevant to Odin, providing foundational empirical evidence on Filipino financial behaviors that can inform multiple design and evaluation aspects."
limitations:
  - "Self-reported data may introduce biases in respondents' assessments of their financial literacy and budgeting practices. [unacknowledged]"
  - "The study does not account for external factors such as socioeconomic background or exposure to financial education outside the classroom. [unacknowledged]"
  - "The sample is limited to students from a single private Catholic school in Davao City, which may limit generalizability to other demographics. [unacknowledged]"
  - "The study does not explore the influence of emerging technologies like AI or machine learning on budgeting practices, representing a gap in the literature. [acknowledged]"
remember_this:
  - "Financial literacy explains 75% of the variance in student budgeting behavior."
  - "Students show strong financial attitudes but struggle with consistent budget application."
  - "Decision-making is the strongest budgeting skill among Filipino college students."
  - "Risk management is the weakest financial literacy dimension requiring improvement."
  - "Correlation between financial literacy and budgeting practices is r = 0.85, p < 0.001."
```
---

## Paper 42: Schipper_summarized.md

**Source File:** `Schipper_summarized.md`

```yaml
paper_id: 10.47852/bonviewFSI52025696
designation: local
title: Navigating Innovation, Inclusion, and Ethical Challenges in AI-Driven Fintech: The Philippines
authors: Schipper, T.
year: 2025
venue: FinTech and Sustainable Innovation
odin_topics:
  - 1.A
  - 1.B
  - 2.A
  - 2.D
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 13.B
tldr: AI-driven social fintech in the Philippines expands financial access via mobile-first platforms and alternative credit scoring but introduces critical ethical risks requiring stronger regulation and consumer protection.
problem_and_motivation: Fintech adoption in the Philippines rapidly increases financial inclusion but creates new ethical risks due to low financial literacy, data privacy gaps, and uneven consumer protections. The balance between innovation-driven access and responsible AI integration remains poorly understood in low-capacity digital environments.
approach:
  - A qualitative multiple case study methodology using desk research and purposive sampling of nine Philippine fintech companies.
  - Reviewed industry reports, regulatory documents, and firm-level data across digital banking, lending, and payments sectors.
  - Companies selected based on declared commitment to financial inclusion and demonstrated use of AI or digital innovations.
  - Data sources included company websites, regulatory filings, policy documents, and academic literature.
  - Analyzed common trends, strategies, and obstacles in advancing inclusive finance with emphasis on technological, ethical, and legal dimensions.
findings:
  - AI-enabled mobile-first platforms allow rapid expansion into underserved areas without conventional banking infrastructure.
  - Alternative credit scoring using mobile data and behavioral analytics expands credit access to unbanked populations.
  - High-interest lending (e.g., Tonik up to 7% monthly) targets vulnerable users, blurring inclusion and exploitative debt.
  - Data privacy violations (e.g., JuanHand improper data collection) highlight gaps in informed consent and regulatory enforcement.
  - num: GCash has 81 million active users and 2.5 million merchants, reflecting deep market penetration.
  - num: Cybersecurity incidents caused P76.49 million in consumer fraud losses in 2024.
  - Ownbank circumvented digital banking moratorium by acquiring a rural bank, exposing regulatory gaps.
  - Plastic Bank uses blockchain and AI to incentivize waste collection, integrating financial inclusion with environmental sustainability.
  - Cropital's AI credit scoring for farmers uses farm productivity and behavioral data but faces default risks from climate hazards.
  - Digital literacy gaps persist, with Filipino borrowers readily sharing personal data without understanding implications.
key_figures_tables:
  - Figure 1: ATMs per 100,000 adults in the Philippines (2011-2021) → Slow physical infrastructure growth compared to regional peers.
  - Figure 2: Account ownership (15+ years) in the Philippines (2011-2021) → Rapid growth from 27% to 53% driven by fintech and mobile money.
  - Table 1: Traditional Fintech vs. Social Fintech comparison → Social fintech prioritizes inclusion and community-oriented solutions.
  - Table 2: AI applications in Philippine financial services → Examples include credit scoring, biometric verification, and anomaly detection.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Social Fintech
    definition: Application of digital financial innovations to advance financial inclusion and meet marginalized populations' needs.
  - term: FATE
    definition: Acronym for Fairness, Accountability, Transparency, and Ethics in AI systems.
  - term: XAI
    definition: Explainable Artificial Intelligence, ensuring user consent and data privacy.
  - term: ESG
    definition: Environmental, Social, and Governance factors for socially responsible investment decisions.
  - term: P2P Lending
    definition: Peer-to-peer lending platform connecting individual lenders and borrowers without traditional financial intermediaries.
critical_citations:
  - "[Russell & Norvig, 2021] — Defines AI as agents perceiving and acting upon their environment."
  - "[Bahoo et al., 2024] — AI making financial services faster and more inclusive."
  - "[ADB, 2022] — Highlights regulatory compliance challenges for fintech in ASEAN."
  - "[Quimba et al., 2021] — Analyzes profitability obstacles for Philippine fintech companies."
  - "[Aldboush & Ferdous, 2023] — Emphasizes responsible innovation and consumer data protection."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Focuses on Filipino fintech adoption and digital engagement trends relevant to this demographic.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Discusses financial inclusion metrics and account ownership trends in the Philippines.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Examines social fintech practices including blockchain-based waste-to-cash and P2P lending.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: References seasonal and occasion-based financial needs though not the primary focus.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Maps the Philippine fintech ecosystem including digital banks, lending apps, and payments.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies gaps in infrastructure, literacy, privacy, and consumer protection.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: AI-driven behavior analysis and alternative credit scoring as profiling examples.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Discusses AI classification for creditworthiness based on behavioral indicators.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: high
      justification: All case studies use mobile-first platforms to reach underserved populations.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Mobile app interfaces and user experiences in GCash, Tonik, and Tala.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Detailed discussion of data privacy violations and cybersecurity threats.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Trust-building mechanisms and risks of algorithm opacity.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: User engagement through personalized financial insights and recommendations.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: Financial literacy programs and user retention strategies discussed.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: High-interest lending, non-performing loans, and debt cycles explicitly addressed.
  contribution: This paper justifies Odin's need for robust data privacy and security modules by documenting widespread privacy violations in Philippine fintech. It informs Odin's behavioral profiling approach by showing how AI credit scoring uses alternative data for financial inclusion. The findings on high-interest lending and debt cycles directly support Odin's debt management features and user protection mechanisms. The case for mobile-first, culturally contextualized design is reinforced by examples of successful fintech adoption across diverse Filipino communities.
  directly_justifies:
    - "AI-driven financial inclusion must be balanced with robust consumer protection to prevent exploitative lending."
    - "Algorithmic transparency is essential to build and maintain user trust in AI-powered financial systems."
    - "Data privacy violations occur when fintech apps collect excessive personal data without informed consent."
    - "Digital literacy gaps lead users to share sensitive data without understanding the implications."
    - "Regulatory sandboxes can safely test fintech innovations while ensuring compliance and consumer safety."
  limits:
    - "Lacks longitudinal data to track long-term socioeconomic impacts of fintech initiatives."
    - "No empirical assessment of the 'social investment life-course multiplier' effect across age or income groups."
    - "Focuses primarily on Philippines, limiting generalizability to other Global South contexts."
    - "Does not include direct user surveys, relying on desk research and secondary data sources."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was conducted. The paper was flagged as highly relevant for Filipino Cultural Context (2.A), Existing Systems & Gaps (4.A, 4.B), Behavioral Profiling (5.A), Mobile-First Design (9.A), Data Privacy (10.A, 10.B), and Debt Management (13.B) due to its detailed case studies and ethical risk analysis. Medium relevance was assigned to Financial Structure (1.B), Classification Approaches (5.C), Mobile UX (9.B), Engagement Dynamics (11.A, 11.B), and Retention Mechanisms (11.B). Low relevance was assigned to Spending Forecasting (6.A, 6.B) and Algorithmic-specific topics (8.A, 8.B, 8.C) as the paper does not focus on predictive models. Contextual relevance was assigned to Seasonal Spending (2.D). Topics rejected included Budget Recommendation (7.A–D), Optimization (7.C, 7.D), Evaluation Frameworks (12.A–C), and Savings Goals (13.A, 13.C) as the paper does not address these technical or evaluation topics. The overall relevance to Odin is high, providing critical justification for data privacy, debt management, and mobile-first design modules while highlighting regulatory gaps that Odin's design should address.
limitations:
  - "Lacks longitudinal data to track long-term socioeconomic impacts of fintech initiatives. [unacknowledged]"
  - "No empirical assessment of the 'social investment life-course multiplier' effect. [unacknowledged]"
  - "Focuses primarily on Philippines, limiting generalizability to other Global South contexts. [unacknowledged]"
  - "Does not include direct user surveys, relying on desk research and secondary data sources."
  - "Does not evaluate the long-term socioeconomic effects of fintech initiatives in the Philippines. [unacknowledged]"
remember_this:
  - "AI-driven fintech expands financial access but introduces ethical risks in low-literacy environments."
  - "GCash's 81 million users demonstrate fintech's potential for rapid adoption in the Philippines."
  - "High-interest lending can blur the line between inclusion and exploitation of vulnerable users."
  - "Algorithmic opacity undermines trust and accountability in AI-powered credit scoring."
  - "Regulatory gaps enable circumvention of digital banking restrictions through rural bank acquisitions."
```
---

## Paper 43: Dela Torre et al_summarized.md

**Source File:** `Dela Torre et al_summarized.md`

```yaml
paper_id: 10.61424/rjbe.v3.i3.574
designation: local
title: The Impact of Personal Budgeting Skills on College Students' Financial Stability
authors: Dela Torre, J. M. Y.; Jangao, J. P. P.; Maghilum, J. T.; Man-onan, R. J. H.; Pepito, S. G.; Rapirap, G. P.; Cervantes, J. Z.
year: 2025
venue: Research Journal in Business and Economics
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 3.A
  - 7.A
  - 12.A
  - 13.A
tldr: Personal budgeting skills, particularly in planning, goal setting, and expense tracking, strongly correlate with improved financial stability among college students.
problem_and_motivation: College students frequently face financial stress and instability due to limited resources and inadequate financial management skills. The specific relationship between structured budgeting practices and financial stability for students managing daily expenses remains underexplored.
approach:
  - The study used a descriptive-correlational design with 213 randomly sampled students from a total population of 457 at a Philippine higher education institution.
  - Data were collected using a structured questionnaire adapted from Bhovi (2024) assessing budget planning, financial goal setting, and expense tracking.
  - Financial stability was measured through self-reported financial stress, savings, and monthly expense management using a four-point Likert scale.
  - Correlation analysis (Pearson R) was performed to test the relationship between budgeting skills and financial stability.
  - T-Test and ANOVA were used to examine differences in the effect of budgeting skills based on demographic profiles.
findings:
  - num: 86% of respondents have an average monthly allowance of ₱1,000.00 or below.
  - Students demonstrate very high competency in budget planning (mean 3.49), financial goal setting (mean 3.52), and expense tracking (mean 3.45).
  - The study found a strong positive correlation (r = 0.7247, p < 0.01) between personal budgeting skills and financial stability.
  - Students who practice better budgeting habits report lower financial stress and greater savings.
  - Significant differences in financial management capacity were observed across age, year level, program, and average monthly allowance.
key_figures_tables:
  - Table 1: Respondent demographic profile → Majority are female with monthly allowance below ₱1,000.
  - Table 2: Assessment of budgeting skills → Students show very high skills in all three subscales.
  - Table 3: Assessment of financial stability → Students report very high financial stability across all measures.
  - Table 4: Correlation analysis → Strong significant relationship between budgeting and financial stability.
  - Table 5: Demographic differences → Significant differences exist based on age, year, program, and allowance.
key_equations:
  - equation: r = 0.7247
    explanation: Pearson correlation coefficient for budgeting skills and financial stability.
definitions:
  - term: Financial Stability
    definition: The ability to manage expenses, maintain savings, and experience low financial stress.
  - term: Personal Budgeting Skills
    definition: Competency in budget planning, goal setting, and expense tracking.
critical_citations:
  - "[Xiao & O'Neill, 2019] — Budgeting enables efficient resource allocation and debt avoidance."
  - "[Galperti, 2019] — Self-regulation and disciplined planning improve financial outcomes."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: Focuses on college students, a precursor demographic to young professionals in the Philippines.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Provides local data on student allowances and financial constraints relevant to future professionals.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly investigates budgeting behaviors and their link to financial stability among students.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: Mentions tracking expenses but does not propose a specific categorization framework.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Validates the importance of structured budgeting strategies for financial stability.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: low
      justification: Uses a survey-based evaluation approach applicable to system design.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Links effective budgeting to improved savings behavior.
  contribution: This paper provides empirical evidence that strong budgeting skills correlate with reduced financial stress, which supports Odin's focus on behavior-tracking modules. The findings justify the development of budget planning and expense tracking features in a PFMS like Odin. The strong correlation between planning and stability highlights the need for personalized budgeting tools.
  directly_justifies:
    - Budget planning, goal setting, and expense tracking are key determinants of financial stability for users with limited income.
    - A strong positive relationship exists between structured budgeting practices and reduced financial stress.
    - Students who engage in consistent budgeting maintain small but consistent savings even with minimal income.
  limits:
    - The study's context is a single higher education institution in Baungon, limiting generalizability to other socioeconomic groups.
    - Reliance on self-administered questionnaires may introduce response bias.
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The domains of "Filipino Cultural Context," "Expense Categorization," "Budget Recommendation," and "Savings & Debt Management" were flagged as relevant due to the paper's focus on local student financial behaviors and budgeting practices. Specifically, topics 1.A, 1.B, and 1.C were assigned high relevance as the paper directly addresses the financial demographics and behavior of Filipino students. Topic 7.A was also deemed highly relevant as it validates budgeting strategies as essential domain knowledge. Topics 3.A and 13.A were assigned contextual and medium relevance respectively, as the paper touches on expense tracking and savings but does not propose novel frameworks. The domains of "Forecasting," "Anomaly Detection," "Mobile-First Design," and "Data Privacy" were considered and rejected as the paper does not address algorithmic, predictive, or technical design aspects. Overall, the paper provides foundational behavioral evidence for Odin's user profiling and budgeting modules.
limitations:
  - The study is limited to one higher education institution in Baungon, which may not represent the broader Filipino young professional demographic. [unacknowledged]
  - The findings rely on self-reported data, which may be subject to social desirability bias. [unacknowledged]
  - The study does not account for external factors like family support or part-time employment that could influence financial stability. [unacknowledged]
remember_this:
  - Budgeting skills show a strong positive correlation with financial stability among Filipino students.
  - Students with better budgeting habits experience less financial stress and save more.
  - Most students manage a monthly allowance of ₱1,000 or below.
  - Effective budget planning and goal setting are key to financial well-being.
  - The findings support the integration of financial literacy programs in educational curricula.
```
---

## Paper 44: Dimaranan & Dy_summarized.md

**Source File:** `Dimaranan & Dy_summarized.md`

```yaml
paper_id: 10.29244/jfs.v10i1.62925
designation: local
title: Financial Management and Commitment to Sending Remittances of Filipina Wives in Virginia, United States
authors: Dimaranan, C. F. D.; Dy, M. F. R.
year: 2025
venue: Journal of Family Sciences
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 3.A
  - 13.A
  - 13.C
tldr: Examines how nine Filipina wives in Virginia manage finances and sustain remittances to the Philippines, revealing that unplanned emergency requests strain budgets and savings.
problem_and_motivation: Research on the financial management of Filipina wives residing overseas with their families of procreation while sending remittances to their families of orientation is scarce. Understanding this dual financial responsibility is crucial to assess household stability and the sustainability of transnational support.
approach:
  - Conducted face-to-face in-depth interviews with nine Filipina wives in Virginia, USA, from 2018-2020.
  - Used purposive and snowball sampling to recruit participants who are married, have children, and send remittances.
  - Employed thematic analysis to analyze qualitative data on household finances, budgeting, and remittance practices.
  - Interview guide was validated by three family studies experts and covered socio-demographics, income, expenditures, financial management, and remittance patterns.
  - Performed within-case and across-case analyses to identify themes and compare cases.
findings:
  - num: All nine households have sufficient income to cover expenses and savings, with total monthly household incomes ranging from $5,000 to $22,500.
  - num: The Philippines set a new record of $3.6 billion in personal remittances in 2023.
  - All households practice financial management through clear goals, monthly budgets, proactive decision-making, and savings.
  - Remittances are sent monthly to cover household bills, education, food, and medical expenses, with amounts ranging from $40 to $500+.
  - Emergency requests for additional remittances disrupt monthly budgets and savings, creating potential financial mismanagement.
  - Filipina wives who are dependent homemakers still send remittances, showing commitment is personal, not solely income-dependent.
key_figures_tables:
  - Table 1: Socio-demographics of participants → Shows diverse migration histories and visa pathways.
  - Table 2: Work status of Filipina participants → Highlights variation from full-time to dependent homemakers.
  - Table 4: Monthly household income → Demonstrates income sufficiency across all households.
  - Table 5: Breakdown of monthly expenses → Details fixed, variable, and loan expenditures.
  - Table 6: Monthly remittances sent → Illustrates regularity and recipient relationships.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Family of procreation
    definition: The family one establishes through marriage and having children.
  - term: Family of orientation
    definition: The family into which one is born or raised.
  - term: Remittance
    definition: Money sent by a migrant to family in their country of origin.
  - term: Balikbayan box
    definition: A box of gifts and goods sent by overseas Filipinos to family in the Philippines.
  - term: Pakikipagkapwatao
    definition: A Filipino core value of shared humanity and treating others as fellow human beings.
  - term: Utang-na-loob
    definition: A Filipino value of debt of gratitude, motivating reciprocity and support.
critical_citations:
  - "[Alampay, 2014] — Defines Filipino family-centeredness and values."
  - "[Jalagat Jr. & Dalluay, 2016] — Provides OFW financial management context."
  - "[McCallum, 2021] — Discusses remittances in Filipino transnational families."
  - "[Medina, 2015] — Outlines Filipino family structures and dynamics."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: Focuses on Filipina wives as a specific demographic subset.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Directly details household income, expenses, budgeting, and financial management.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Explores financial practices, decision-making, and commitment to remittances.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Examines "utang-na-loob" and family-centeredness driving remittance behavior.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: low
      justification: Mentions occasional and emergency remittances, but not systematic cycles.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: medium
      justification: Remittances cover special occasions and emergencies, reflecting cultural spending triggers.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Provides a detailed breakdown of variable, fixed, loan, and subscription expenses.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Identifies savings for children's education, emergency funds, and future investments.
    - code: 13.C
      name: End-of-Period Surplus as a Savings Input
      relevance: low
      justification: Alludes to savings from income surplus but does not explicitly model surplus allocation.
  contribution: This paper provides qualitative evidence on the financial management practices of Filipina wives with transnational obligations, which can inform Odin's budgeting modules by highlighting the impact of unplanned remittances on household stability. The findings on shared versus sole budget-holding can guide design for collaborative financial planning features. The culturally motivated remittance behavior underscores the need for Odin's expense categorization to accommodate family support obligations. This research directly justifies the inclusion of emergency fund and savings goal modules within Odin.
  directly_justifies:
    - The practice of mental budgeting suggests Odin should support both manual and automated tracking.
    - Emergency remittance requests disrupt monthly budgets, justifying need for flexible reallocation.
    - Savings for children's education and retirement are key financial goals that require dedicated modules.
    - Joint financial decision-making supports Odin's design for collaborative household budgeting.
    - The regularity of monthly remittances indicates a need for recurring expense features in Odin.
  limits:
    - Small sample size (n=9) limits generalizability to all Filipina wives in the US.
    - Income and expense data are based on participant estimates, not verified financial records.
    - The study focuses only on Virginia, which may not represent Filipinas in other states.
    - Husbands' perspectives on financial management and remittances were not collected.
    - Numerical data are approximations for households where husbands are sole budget holders.
  mapping_rationale: A systematic scan across all 12 functional domains was conducted for this paper. The domains most relevant are Filipino Cultural Context (2.A, 2.D), Expense Categorization (3.A), and Savings & Debt Management (13.A, 13.C). Topic 2.A (Culturally Specific Practices) was rated high due to the paper's direct treatment of "utang-na-loob" and family-centeredness as drivers of remittances. Topic 1.B (Financial Structure) and 1.C (Financial Behavior) were rated high for their detailed accounts of household income, expenditure patterns, and budgeting practices. Topic 3.A was rated medium for its useful expense categorization. Topics 2.B and 13.C were rated low/medium as the paper touches on them but does not focus on cyclical patterns or surplus modeling. Domains such as Behavioral Profiling, Forecasting, Anomaly Detection, and UX Design were rejected as the paper is purely qualitative and does not address algorithmic or system-level design. Overall, the paper offers strong qualitative insights into the financial realities of Filipino migrants, which can contextualize the design needs for a PFMS like Odin.
limitations:
  - Small sample size (n=9) limits generalizability.
  - Income and expense values are estimations, not exact figures. [unacknowledged]
  - Study only covers Virginia, not other U.S. states. [unacknowledged]
  - Husbands' perspectives on financial management were not included. [unacknowledged]
remember_this:
  - Monthly remittances are a fixed expense, not an optional extra.
  - Emergency requests disrupt budgets, causing financial strain.
  - Savings for children's education is a top priority.
  - Income sufficiency does not eliminate budget vulnerability.
  - Cultural values strongly sustain remittance commitment.
```
---

## Paper 45: Tambuli & Villarba_summarized.md

**Source File:** `Tambuli & Villarba_summarized.md`

```yaml
paper_id: f7c8a2e4-5b6a-4c1e-9d3f-8a2b4c6d8e0f
designation: local
title: PERSONAL FINANCIAL MANAGEMENT BEHAVIOR AND FINANCIAL PLANNING AS KEY DRIVERS OF RETIREMENT PREPAREDNESS AMONG LGU's CONTRACTUAL PERSONNEL
authors: Tambuli, A. P.; Villarba, L. O.
year: 2025
venue: ISRG Journal of Economics and Finance
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 4.A
  - 4.B
  - 5.A
  - 7.A
  - 7.D
  - 13.A
  - 13.B
tldr: Financial management behavior and financial planning significantly drive retirement preparedness among LGU contractual personnel in the Philippines.
problem_and_motivation: Contractual employees face income instability and limited saving opportunities, creating gaps in retirement preparedness. Understanding the specific financial behaviors and planning practices of this demographic is essential for developing targeted interventions. Prior research has not adequately examined this population's unique retirement planning challenges.
approach:
  - Data were collected from 200 LGU contractual personnel in Nabunturan using simple random sampling.
  - A descriptive-correlational research design was employed with an adapted and validated survey questionnaire.
  - Statistical analyses included mean scores, standard deviations, Pearson's r, and multiple regression.
  - The study measured personal financial management behavior across cash management, credit management, and savings/investment.
  - Financial planning was assessed through retirement savings and financial planning abilities indicators.
findings:
  - num: Retirement preparedness was high (mean=3.62, SD=0.90) across asset acquisition, budgeting, and decision-making domains.
  - num: Personal financial management behavior was high (mean=3.62, SD=0.93) with cash management showing the highest mean (3.75).
  - num: Financial planning status was high (mean=3.62, SD=0.91) but retirement savings was only moderately evident (mean=3.37).
  - num: Both PFMB (r=.701, p<.001) and financial planning (r=.739, p<.001) had strong significant correlations with retirement preparedness.
  - num: PFMB (β=.350, p<.001) and financial planning (β=.485, p<.001) jointly predicted 61.5% of variance in retirement preparedness (R²=.615).
  - Respondents demonstrated high budgeting awareness but limited translation to regular retirement savings behavior.
key_figures_tables:
  - "Table 1: Level of retirement preparedness across domains → Overall high preparedness with moderate consistency (SD=0.90)."
  - "Table 2: Status of personal financial management behavior → High overall status (3.62) with strongest performance in cash management."
  - "Table 3: Status of financial planning → High overall (3.62) but retirement savings domain only moderate (3.37)."
  - "Table 4: Correlation between variables → Both PFMB and financial planning show strong significant correlations (r>.70)."
  - "Table 5: Drivers of retirement preparedness → PFMB and financial planning are significant predictors with β=.350 and .485 respectively."
key_equations:
  - equation: "RP = β₀ + β₁(PFMB) + β₂(FP) + ε"
    explanation: "Regression model predicting retirement preparedness from two predictors."
  - equation: "R² = .615"
    explanation: "Model explains 61.5% of retirement preparedness variance."
definitions:
  - term: LGU
    definition: Local Government Unit.
  - term: PFMB
    definition: Personal Financial Management Behavior.
  - term: RP
    definition: Retirement Preparedness.
  - term: FP
    definition: Financial Planning.
  - term: Theory of Planned Behavior
    definition: "Psychological theory explaining behavior through attitudes, norms, and perceived control."
  - term: Financial Literacy Theory
    definition: "Framework linking financial knowledge to improved financial outcomes."
critical_citations:
  - "[Sturr et al., 2021] — PFMB directly influences retirement preparedness."
  - "[Ajzen, 1991] — Theory of Planned Behavior provides behavioral framework."
  - "[Lusardi & Mitchell, 2013] — Financial literacy theory underpins saving behaviors."
  - "[Nam & Loibl, 2020] — Financial planning predicts retirement readiness."
  - "[Ingale & Paluri, 2023] — Long-term planning resolves retirement preparedness gaps."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "medium"
      justification: "Study focuses on Filipino contractual workers in Davao region."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "high"
      justification: "Examines income instability and limited saving opportunities of contractual personnel."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Measures actual financial behaviors including budgeting and credit management."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "contextual"
      justification: "Philippine LGU context provides cultural specificity but not main focus."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "low"
      justification: "References existing literature on financial planning but no system analysis."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Identifies gap in research on contractual employee retirement preparation."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Directly measures and classifies financial management behaviors."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "high"
      justification: "Examines budgeting practices and their relationship to retirement readiness."
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "contextual"
      justification: "Discusses challenges of saving with limited income but no algorithmic approach."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "high"
      justification: "Focuses on retirement savings goals and regular saving behavior."
    - code: "13.B"
      name: "Debt Management in PFMS"
      relevance: "medium"
      justification: "Includes credit management and loan repayment behaviors."
  contribution: "This paper provides empirical evidence that personal financial management behavior and financial planning are the strongest predictors of retirement preparedness among Filipino contractual employees. It validates the Theory of Planned Behavior in the context of retirement saving decisions. The findings support Odin's module for behavioral profiling by establishing measurable indicators of financial behavior. The strong correlation between budgeting practices and retirement readiness justifies Odin's budget recommendation and savings goal management features. The identification of implementation gaps between financial awareness and actual saving behavior informs Odin's design for behavioral nudges and automatic savings features."
  directly_justifies:
    - "Financial management behavior and financial planning are key drivers of retirement preparedness."
    - "Budgeting practices show strong correlation with retirement readiness."
    - "Cash management is the most prominent component of personal financial management behavior."
    - "Retirement savings implementation lags behind financial planning awareness."
    - "Financial planning abilities are high but translation to regular savings is moderate."
  limits:
    - "Focus on one LGU in Davao de Oro may limit generalizability to other regions."
    - "Cross-sectional design cannot establish causal relationships."
    - "Self-reported measures may be subject to social desirability bias."
    - "Excludes permanent employees, limiting comparison with other employment types."
    - "Does not explore underlying psychological or structural barriers to saving. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was conducted for this paper. The domains of Behavioral Profiling & Classification (5.A, 5.B, 5.C), Budget Recommendation (7.A, 7.B, 7.C, 7.D), and Savings & Debt Management (13.A, 13.B, 13.C) were flagged as highly relevant because the paper directly measures financial behaviors and planning as drivers of retirement preparedness. The Filipino Cultural Context domain (2.A, 2.B, 2.C, 2.D) was considered medium relevance for 2.A due to the Philippine LGU context, but codes 2.B, 2.C, and 2.D were rejected as the paper does not address seasonal spending or user-declared preferences. Existing Systems & Gaps (4.A, 4.B) was assigned medium relevance for 4.B as the paper identifies a research gap but does not analyze existing systems. Expense Categorization (3.A, 3.B, 3.C) and Anomaly Detection (8.A, 8.B, 8.C) were rejected as the paper does not address these algorithmic modules. Mobile-First Design (9.A, 9.B), Data Privacy (10.A, 10.B), User Retention (11.A, 11.B), and System Evaluation (12.A, 12.B, 12.C) were all rejected as not addressed. The paper's overall relevance to Odin is high for foundational behavioral insights, but it lacks algorithmic or systems design contributions."
limitations:
  - "Sample limited to one municipality in Davao de Oro, reducing generalizability."
  - "Cross-sectional design prevents causal inference."
  - "Self-reported survey data may introduce social desirability bias."
  - "Does not examine the role of financial education or literacy programs."
  - "Lacks longitudinal tracking of retirement savings behavior. [unacknowledged]"
  - "Does not address the influence of household or family financial dynamics. [unacknowledged]"
remember_this:
  - "Financial management behavior and financial planning predict 61.5% of retirement preparedness variance."
  - "Cash management is the strongest component of personal financial management behavior."
  - "Retirement savings implementation lags behind financial planning awareness."
  - "Budgeting practices correlate strongly with retirement readiness."
  - "Contractual employees show high financial awareness but limited saving behavior."
```
---

## Paper 46: Patiu et al_summarized.md

**Source File:** `Patiu et al_summarized.md`

```yaml
paper_id: 3187f7d0-7d47-530b-8c3e-492a21f406bb
designation: local
title: Unraveling the Investment Puzzle: Do Behavioral Biases and Financial Literacy Matter?
authors: Patiu, L. S.; Ang, L. K. C.; Masanque, J. A. A.; Nacario, J. M. C.; Paguntalan, R. M. M.
year: 2025
venue: Review of Integrative Business and Economics Research
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 5.A
  - 5.B
  - 5.C
  - 7.A
  - 7.B
  - 10.A
  - 10.B
tldr: Filipino Gen Y and Gen Z investment decisions are significantly influenced by behavioral biases, with financial literacy moderating these effects and exhibiting a negative direct impact on Generation Y.
problem_and_motivation: Investors in emerging markets often make irrational decisions due to low financial literacy and behavioral biases, yet the specific interplay of these factors for Filipino young professionals remains underexplored. Understanding these dynamics is crucial for designing effective financial advisory and educational interventions.
approach:
  - A structured survey was administered online to 385 Filipino retail investors in Metro Manila, using Google Forms.
  - The study employed a quantitative explanatory design and utilized the Ordinary Least Square method for regression analysis.
  - Hierarchical regression was applied to measure the unique variance added by each behavioral bias (overconfidence, herding, disposition effect, risk aversion) to investment decisions.
  - Moderation analysis was conducted to measure the influence of the interaction between behavioral biases and financial literacy.
  - The study used adapted scales from Adil et al. (2022) for behavioral biases, financial literacy, and investment decisions, with reliability confirmed via Cronbach's Alpha.
findings:
  - Herding bias significantly and positively affects investment decisions for both Generation Y (β=0.189***) and Generation Z (β=0.213***).
  - Risk aversion significantly affects Generation Y (β=0.245***) but not Generation Z, while overconfidence is significant for Generation Z (β=0.199**) but not Generation Y.
  - Financial literacy has a significant negative influence on Generation Y's investment decisions (β=-0.391*), but an insignificant negative influence on Generation Z.
  - The inclusion of herding bias (∆R2=0.2189 for Gen Y) and disposition effect bias (∆R2=0.0554 for Gen Y) significantly improved predictive power for both groups.
  - Risk aversion added significant variance (∆R2=0.0561) for Generation Y but not for Generation Z (∆R2=0.0008).
  - Financial literacy significantly moderates the effect of overconfidence (β=1.111**) and disposition effect (β=0.696*) on Generation Y's investment decisions, but shows no significant moderation for Generation Z.
  - num: The addition of risk aversion bias in Model 4 accounted for 5.61% of the variance in investment decisions for Generation Y.
  - num: Herding bias added a 21.89% variance in investment decisions for Generation Y investors, compared to 15.87% for Gen Z.
  - The study found that 50.3% of respondents were Millennials (Gen Y) and 49.7% were Gen Z, with a majority being female (54.6%) and employees (60.5%).
key_figures_tables:
  - "Table 1: Demographic profile showing 196 Gen Y and 194 Gen Z respondents, majority female and employees → sample is predominantly employed females from two generations."
  - "Table 2: Regression results showing that herding and disposition effect are significant for both generations, while overconfidence and risk aversion differ → behavioral biases impact varies across generations."
  - "Table 3: Hierarchical regression model fits for Gen Y and Gen Z, showing R^2 values from 0.021 to 0.352 → adding biases improves model explanatory power."
  - "Table 4: Model comparisons showing ∆R^2 and p-values for each step of hierarchical regression → risk aversion only adds significant variance for Gen Y."
  - "Table 5: Regression results for financial literacy, showing a negative significant effect for Gen Y only → financial literacy has a different effect between the two generations."
  - "Table 6: Moderation results showing that financial literacy significantly moderates only two biases for Gen Y → moderation effect is limited to the older cohort."
key_equations:
  - equation: Investment Decision = β0 + β1OB + β2HB + β3DB + β4RAB + β5FL
    explanation: Regression model measuring impact of four behavioral biases and financial literacy.
definitions:
  - term: Overconfidence bias
    definition: Tendency to overestimate one's ability and knowledge to predict future information.
  - term: Herding bias
    definition: Investor's tendency to imitate the investment decisions of others.
  - term: Disposition effect
    definition: Tendency to sell winning stocks too early and hold losing stocks too long.
  - term: Risk aversion
    definition: Investor's preference to avoid risk or losses, favoring safer investments.
  - term: Financial literacy
    definition: Ability and skills to manage personal finances to decrease potential errors in financial decisions.
critical_citations:
  - "[Adil et al., 2022] — Found herding bias negatively impacts Pakistani millennial investors."
  - "[Almansour et al., 2023] — Found herding and risk aversion positively affect Saudi investors."
  - "[Mahmood et al., 2024] — Found negative impact of risk aversion on investment decisions."
  - "[Prasetyo et al., 2023] — Found negative moderation of FL on herding/overconfidence."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Directly studies Filipino Gen Y and Z retail investors as its core population.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Investigates investment decisions, a key aspect of financial structure for these cohorts.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: The entire study is an empirical investigation of investment behavior and its drivers.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: low
      justification: Focuses on behavioral biases and literacy, not uniquely Filipino cultural practices.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Does not directly examine spending cycles; provides context on investor behavior.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: Provides background on financial behavior but does not study spending cycles.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly profiles investors by four key behavioral biases (overconfidence, herding, disposition, risk aversion).
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: Does not address cold-start problems, but confirms that different biases affect decisions.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses regression to classify and measure the impact of each bias, providing data for profile classification.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: Provides knowledge on investor decision-making behavior, but not budgeting strategies.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: contextual
      justification: Offers insights on biases and literacy that could inform recommendation systems, but not directly.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Does not address data privacy, but its findings on literacy and behavior are relevant to user trust.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: Does not examine trust but provides context on factors influencing financial decisions.
  contribution: This paper's findings on behavioral biases are foundational for Odin's user behavioral profiling module (Topic 5.A), providing empirical evidence that overconfidence, herding, disposition effect, and risk aversion significantly influence Filipino young professionals' financial decisions. The significant moderating role of financial literacy on these biases, particularly for Generation Y, directly informs Odin's cold-start profiling (Topic 5.B) and suggests that an initial financial literacy assessment is crucial for accurate user classification. The observed generational differences in the influence of overconfidence and risk aversion justify the need for dynamic, age-aware behavioral models that can adapt to different user profiles. Moreover, the negative impact of financial literacy on Generation Y's investment decisions challenges simple assumptions and highlights the importance of nuanced, non-prescriptive design in financial applications.
  directly_justifies:
    - Odin's behavioral profiling module must measure overconfidence, herding, disposition effect, and risk aversion for Filipino users.
    - Financial literacy is a significant moderator of behavioral biases and should be part of the user profiling process.
    - Generation-specific differences in behavioral bias impact require adaptive models in a PFMS.
    - A low financial literacy score may not predict poor financial decisions, requiring careful interpretation in system design.
  limits:
    - The sample is limited to Filipino retail investors in Metro Manila, potentially limiting generalizability.
    - The study uses a self-reported online survey, which is subject to social desirability and recall bias.
    - The analysis is correlational and does not establish causal relationships between biases and investment decisions.
    - The study does not investigate the user's actual financial behavior, only their reported decisions.
  mapping_rationale: A systematic scan of all 12 functional domains revealed that the paper's core contribution directly aligns with Domain 5 (Behavioral Profiling) and Domain 2 (Cultural Context). The paper's empirical findings on the influence of overconfidence, herding, disposition effect, and risk aversion on Filipino Gen Y and Z investors provide high-relevance evidence for Topic 5.A (Financial Behavioral Profiles) and Topic 1.C (Financial Behavior of Filipino Young Professionals). The significant moderating effect of financial literacy offers medium relevance to Topic 5.B (Profile Dynamics) and Topic 5.C (Classification Approaches) by informing how initial user states can be estimated. The contextual relevance to Domains 7 (Budget Recommendation) and 10 (Data Privacy) is noted, as the insights on user behavior can inform system design and trust, but the paper does not directly address those topics. Other domains (3, 4, 6, 8, 9, 11, 12, 13) were considered and rejected as the paper does not cover expense categorization, forecasting, anomaly detection, or engagement mechanisms. Overall, this paper provides strong empirical justification for integrating behavioral bias measurement into Odin's user profiling and is moderately relevant for designing classification and cold-start strategies.
limitations:
  - The sample of 385 Filipino retail investors from Metro Manila may not represent all Filipino young professionals. [unacknowledged]
  - The study relies on self-reported data, which may be subject to social desirability bias. [unacknowledged]
  - The cross-sectional design prevents establishing causality between biases, literacy, and decisions. [unacknowledged]
  - The research instrument was adapted, but its full validity for the Philippine context was not extensively discussed.
remember_this:
  - Herding bias significantly drives investment decisions for both Gen Y and Gen Z in the Philippines.
  - Risk aversion impacts Gen Y investment decisions but not Gen Z's.
  - Financial literacy negatively influences Gen Y's investment decisions in this sample.
  - Financial literacy moderates overconfidence and disposition effect only for Generation Y.
  - Overconfidence significantly impacts Gen Z but not Gen Y investment decisions.
```
---

## Paper 47: Lambert et al_summarized.md

**Source File:** `Lambert et al_summarized.md`

```yaml
paper_id: 12c7f7a6-9a4a-5b3c-8e2d-1f6b9a3c7d5e
designation: local
title: Relationship between Family Resources, Financial Stress, with Financial Management among Filipino Millennials
authors: Lambert, M. J. C. M.; Jusoh, Z. M.; Zainudin, N.
year: 2025
venue: JURNAL PENGGUNA MALAYSIA
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 4.B
  - 5.A
  - 9.A
  - 9.B
tldr: Financial stress negatively impacts financial management among Filipino millennials, while millennial characteristics positively influence management practices.
problem_and_motivation: Filipino millennials face significant financial stress, poor financial literacy, and limited savings despite macroeconomic growth. The interplay between family resources, stress, and financial management in this cultural context is poorly understood.
approach:
  - Data were collected from 400 Filipino millennials in Eastern Visayas using a self-administered online questionnaire.
  - The study employed multistage random sampling and Structural Equation Modelling (SEM) for analysis.
  - Millennial characteristics were assessed using 29 items adapted from Pew Research, measuring optimism, achievement focus, family orientation, and tech-savviness.
  - Financial stress was measured using a 14-item adapted instrument on economic difficulties and coping strategies.
  - Financial management was evaluated via a 39-item scale covering attitudes and practices like budgeting, saving, and bill payment.
findings:
  - num: Financial stress had a significant adverse effect on financial management (β = -0.724, p < .001).
  - num: Millennial characteristics exerted a positive and significant influence on financial management (β = 0.480, p < .001).
  - The study confirms that financial stress undermines prudent financial practices.
  - Millennial traits such as adaptability, collaboration, and digital literacy enhance financial management capabilities.
  - Respondents with higher financial stress demonstrated poorer budgeting, saving, and bill payment practices.
  - Millennials who are optimistic, achievement-focused, and tech-savvy are more likely to practice effective financial management.
  - The findings extend behavioural finance by illustrating how contextual stressors and generational traits jointly shape financial outcomes.
key_figures_tables:
  - "Table 1: Demographic Characteristics of Respondents (N=400) → Majority are male, college graduates, aged 26-35, with middle-to-low income."
  - "Table 2: Millennial Characteristics Score by Item → Highest mean score for family-oriented (4.81), lowest for optimistic (3.59)."
  - "Table 3: Financial Stress Score → Overall mean score of 2.23 indicates lower financial stress."
  - "Table 4: Financial Management Score → Mean score of 3.45 indicates good financial management practices."
  - "Figure 1: Conceptual Framework → Shows direct relationships between financial stress and millennial characteristics with financial management."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Financial well-being
    definition: A state where an individual has sufficient resources to live comfortably, fulfil obligations, and have confidence in their financial future.
  - term: Financial stress
    definition: Stress arising when resources are insufficient to meet needs or when constant worry about money occurs.
  - term: Family resources
    definition: Tangible and intangible assets (skills, knowledge, income, property) that influence financial outcomes.
  - term: Millennial characteristics
    definition: Traits such as adaptability, collaboration, digital literacy, and optimism associated with Generation Y.
  - term: Financial management
    definition: The practice of planning, budgeting, saving, and responsible spending.
critical_citations:
  - "[Dollahite, 1991] — Provides the integrated ABCD-XYZ model used as the conceptual framework."
  - "[Lusardi & Mitchell, 2021] — Shows financial literacy and stress are linked to financial well-being."
  - "[Pew Research Centre, 2021] — Demonstrates millennial characteristics shape financial decision-making."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: The study specifically surveys Filipino millennials, a core demographic for Odin.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Provides data on income levels, debt, and financial responsibilities of the target demographic.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly examines financial management practices and stress responses.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Highlights strong family orientation and its influence on financial obligations.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: low
      justification: The paper mentions financial stress but does not detail specific seasonal spending cycles.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: Mentions family obligations but does not specify cultural spending events.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies a gap in understanding the interplay of stress and resources for Filipino millennials.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Defines and measures specific millennial characteristics as a resource influencing financial management.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Recommendations include developing digital tools tailored for millennials.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: Mentions digital tools but does not focus on UX design principles.
  contribution: This study validates the dual influence of financial stress and generational traits on financial management for Odin's target demographic. It supports Odin's behavioral profiling module by identifying key traits like adaptability and digital literacy. The finding that stress undermines financial management justifies Odin's stress-mitigation and anomaly detection features. The strong negative effect of stress on financial management provides a basis for Odin's budget recommendation and forecasting modules to consider stress as a critical factor.
  directly_justifies:
    - "Financial stress significantly degrades financial management practices among Filipino millennials."
    - "Millennial characteristics such as adaptability and digital literacy positively influence financial management."
    - "Financial management practices include budgeting, saving, and responsible bill payment."
    - "Addressing financial stress is crucial for improving financial well-being."
    - "Digital tools tailored to millennial preferences can enhance financial management."
  limits:
    - "The study is cross-sectional, limiting causal inferences."
    - "Data were collected from Eastern Visayas, limiting generalizability to all Filipino millennials. [unacknowledged]"
    - "Self-reported data may be subject to social desirability bias."
    - "The study does not detail the specific algorithmic or system implementation. [unacknowledged]"
  mapping_rationale: A systematic scan was performed across all 12 functional domains and their associated topic codes. The paper was flagged as highly relevant to domains related to Filipino young professionals, behavioral profiling, and financial management (1.A, 1.B, 1.C, 5.A). It provided medium relevance to domains on cultural practices (2.A) and system gaps (4.B) by highlighting the cultural context and research gaps. Low relevance was assigned to seasonal spending (2.B) and mobile UX (9.B) due to only tangential mentions. Domains on forecasting, anomaly detection, and system evaluation (6.x, 8.x, 12.x) were rejected as the paper does not address algorithmic or predictive modeling aspects. Borderline cases included 2.D (spending cycles) which was assigned contextual due to its mention of family obligations but no detail on specific occasions, and 3.C (user-defined constraints) which was rejected as the paper does not discuss allocation constraints. Overall, the paper is relevant for understanding the behavioral and contextual drivers of financial management, providing foundational justification for Odin's design.
limitations:
  - "Cross-sectional design limits causal inferences."
  - "Sample limited to Eastern Visayas may not represent all Filipino millennials."
  - "Reliance on self-reported data may introduce social desirability bias."
  - "The study does not validate the proposed implications through system testing. [unacknowledged]"
  - "Cultural nuances in financial stress coping are not explored in depth. [unacknowledged]"
remember_this:
  - "Financial stress reduces financial management by 0.724 units per stress unit."
  - "Millennial traits improve financial management by 0.480 units per trait unit."
  - "Adaptability and digital literacy are key millennial strengths."
  - "Stress coping is as important as financial literacy for management."
  - "Family obligations increase financial stress for Filipino millennials."
```
---

## Paper 48: Bancoro et al_summarized.md

**Source File:** `Bancoro et al_summarized.md`

```yaml
paper_id: 10.69569/jip.2025.015
designation: local
title: The Role of Financial Literacy in Supporting Employee Work-Life Balance
authors: Bancoro, J.C.; Barillo, R.M.; Buhian, D.L.
year: 2025
venue: Journal of Interdisciplinary Perspectives
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.D
  - 3.A
  - 4.A
  - 4.B
  - 11.A
  - 13.A
  - 13.B
tldr: Financial literacy correlates weakly with work-life balance, yet employees show positive financial attitudes and behaviors, with qualitative findings suggesting indirect stress-reduction benefits.
problem_and_motivation: Financial stress from low literacy undermines work-life balance, but empirical evidence directly linking literacy to balance outcomes is scarce. Understanding this relationship is critical for designing workplace interventions that improve employee well-being and productivity.
approach:
  - A correlational descriptive design was used with 140 faculty and staff from a Philippine state university.
  - Quantitative surveys assessed financial knowledge, attitudes, behaviors, and work-life balance perceptions.
  - Semi-structured interviews with eight employees provided qualitative depth on financial management experiences.
  - Spearman correlation (rho) tested the relationship between financial literacy and work-life balance.
  - Cronbach's alpha (0.83-0.85) confirmed high internal consistency for survey dimensions.
findings:
  - num: Financial knowledge mean score was 8.35 out of 13 (SD = 3.13), indicating moderate literacy with high variability.
  - num: The correlation between financial literacy and work-life balance was weak and non-significant (rho = 0.11, p = 0.191).
  - Employees demonstrated positive financial attitudes (M = 3.99, SD = 0.73) and behaviors (M = 3.94, SD = 0.58).
  - Employees reported good work-life balance (M = 4.06, SD = 0.60), with flexibility and supervisor support as key contributors.
  - Qualitative data revealed that financial literacy reduces financial stress, enabling better focus on personal and professional priorities.
key_figures_tables:
  - Table 1: Summary of financial knowledge, attitudes, and behaviors → shows moderate knowledge with positive attitudes and behaviors.
  - Table 5: Correlation between financial literacy and work-life balance → indicates no significant relationship (rho = 0.11, p = 0.191).
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Financial Literacy
    definition: The ability to make sound financial decisions, including budgeting, saving, investing, and planning for future security.
  - term: Work-Life Balance
    definition: The relationship between work obligations and activities outside work, impacting well-being, job satisfaction, and effectiveness.
  - term: Conservation of Resources (COR) Theory
    definition: A theory positing that individuals seek to obtain, protect, and build resources to minimize stress and handle challenges.
critical_citations:
  - "[Ryu & Fan, 2022] — Establishes link between financial worries and psychological distress."
  - "[Hu et al., 2024] — Shows financial literacy reduces mortgage stress by 60%."
  - "[Galapon & Bool, 2022] — Finds financial behavior, not literacy, predicts well-being."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: The study focuses on Filipino university employees, a core demographic for Odin.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Provides data on income, savings, and spending behaviors of Filipino employees.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly measures financial behaviors (budgeting, saving, spending) of Filipino employees.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Discusses Filipino-specific financial practices like Pag-IBIG MP2 savings and cooperative loans.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Mentions financial constraints and spending pressures, indirectly touching on spending cycles.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: low
      justification: Implicitly involves expense tracking and budgeting behaviors, foundational to categorization.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Mentions financial tools and apps (Mint, YNAB) as part of the financial management landscape.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: low
      justification: Identifies gaps in financial education and support, relevant to system design limitations.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: contextual
      justification: Suggests financial literacy workshops and tools, touching on user engagement mechanisms.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: Relates to saving behaviors and goals (e.g., children's education, retirement) which are core to savings management.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: low
      justification: Mentions avoiding debt and managing loans, relevant to debt management features.
  contribution: This paper provides empirical evidence on the weak direct link between financial literacy and work-life balance, suggesting that Odin should prioritize behavioral interventions over purely educational content. It highlights the importance of supportive workplace policies, which can inform Odin's design for user engagement and retention. The findings underscore the need for Odin to integrate financial education with practical tools that facilitate behavior change, such as automated savings and spending trackers. The study also validates the use of COR Theory as a framework for understanding how financial resources reduce stress, which can guide Odin's approach to user trust and data privacy.
  directly_justifies:
    - Financial literacy alone does not strongly predict work-life balance outcomes.
    - Positive financial behaviors are more closely associated with well-being than knowledge alone.
    - Work-life balance policies are insufficient without addressing financial stress and workload.
    - Tailored financial education programs should focus on behavioral change and personalized coaching.
    - Providing financial planning tools and resources can empower users to manage finances effectively.
  limits:
    - The study is cross-sectional, limiting causal inferences about financial literacy and work-life balance.
    - The sample is confined to one state university in the Philippines, reducing generalizability.
    - Reliance on self-reported data may introduce social desirability or recall bias.
    - The weak correlation may reflect the specific measures used, which may not capture all dimensions of financial literacy or work-life balance.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was conducted to map this paper to Odin's RRL. The domain of Filipino Cultural Context was flagged as highly relevant, with topics 1.A, 1.B, and 1.C receiving high relevance due to the paper's focus on Filipino employees' financial knowledge, attitudes, and behaviors. Topics 2.A and 2.D were assigned medium and low relevance, respectively, for their discussion of culturally specific practices and spending constraints. Expense Categorization (3.A) received low relevance due to implicit expense tracking behaviors. Existing Systems & Gaps (4.A, 4.B) were rated low for mentioning financial tools and gaps in financial education. User Retention & Engagement (11.A) was deemed contextual for its suggestion of financial workshops. Savings & Debt Management (13.A, 13.B) were rated low for discussing saving behaviors and debt avoidance. Domains such as Behavioral Profiling (5.A-C), Spending Forecasting (6.A-B), Budget Recommendation (7.A-D), Anomaly Detection (8.A-C), Mobile-First Design (9.A-B), Data Privacy (10.A-B), and System Evaluation (12.A-C) were rejected as the paper does not address these algorithmic, design, or evaluation concerns. The paper's overall relevance to Odin is moderate, providing foundational insights into Filipino financial behaviors and the indirect role of literacy in stress reduction, which informs feature design for engagement and savings management.
limitations:
  - Cross-sectional design precludes causal conclusions.
  - Sample limited to one state university, limiting generalizability.
  - Self-reported data may be subject to bias.
  - Weak correlation may reflect measurement limitations for financial literacy or work-life balance.
remember_this:
  - Financial literacy shows a weak, non-significant correlation with work-life balance.
  - Employees demonstrate positive financial attitudes but moderate and variable knowledge.
  - Work-life balance is more strongly tied to workplace flexibility and support.
  - Qualitative data suggests financial literacy reduces stress, indirectly aiding balance.
  - Tailored financial education and behavioral tools are recommended over generic literacy programs.
```
---

## Paper 49: Casalhay et al_summarized.md

**Source File:** `Casalhay et al_summarized.md`

```yaml
paper_id: 10.55248/gengpi.6.0525.1716
designation: local
title: The Gig Economy: Financial Challenges and Opportunities Faced by Freelancers
authors: Casalhay, S. F.; Guevarra, C. M.; Bragas, C. M.
year: 2025
venue: International Journal of Research Publication and Reviews
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 8.A
  - 10.A
  - 10.B
  - 13.A
  - 13.B
tldr: Freelancers in the gig economy face income volatility, lack of benefits, and barriers to financial services, requiring tailored products and systemic reforms.
problem_and_motivation: Freelancers face significant financial challenges due to income volatility, lack of traditional employment benefits, and limited access to financial services. The gig economy's growth lacks corresponding support structures, leaving freelancers financially vulnerable and without adequate safety nets. Existing literature often overlooks the specific financial behaviors and coping strategies of freelancers, creating a gap in understanding how to support their long-term financial stability.
approach:
  - A qualitative research design was employed to explore the lived experiences of freelancers in the gig economy.
  - Data was collected through semi-structured interviews with 50 freelancers in Metro Manila across diverse fields like writing, graphic design, and virtual assistance.
  - Purposive and snowball sampling were used to select participants with at least six months of gig work experience.
  - Thematic analysis was used to identify and interpret patterns in participants' responses regarding financial challenges and opportunities.
  - An interview guide was pre-tested with 2-3 freelancers to ensure clarity and relevance of the questions.
findings:
  - Income instability is a primary challenge, driven by seasonal fluctuations, client behavior, and the short-term nature of projects.
  - Freelancers lack access to employer-sponsored benefits like health insurance and retirement plans, increasing their financial burden.
  - Barriers to financial services are significant, as banks view freelancers as high-risk borrowers due to irregular income.
  - The financial challenges cause significant stress, anxiety, and lifestyle limitations, impacting mental and social well-being.
  - Freelancers employ strategies like strict budgeting, emergency funds, and digital tools, but these are often insufficient for long-term security.
  - There is a strong demand for systemic reforms, including government-supported safety nets and legal protections for freelancers.
  - Innovative financial products like micro-savings platforms and income-smoothing tools are recognized but often have high costs or limited accessibility.
  - Continuous upskilling is necessary for competitiveness, but limited funds hinder investment in professional development.
  - Freelancers rely on manual tracking, budgeting apps, and spreadsheets to manage finances, but tools cannot fully solve income irregularity.
  - Respondents expressed a need for financial education, better loan options, and institutional recognition of freelancing as a legitimate career.
key_figures_tables:
  - Table 1: Financial challenges (income instability, benefit access, service barriers) → summarizes core problems faced by freelancers.
  - Table 2: Financial management practices (budgeting, saving, tools) → shows reactive strategies used to mitigate income volatility.
  - Table 3: Means of income stability (fluctuations, healthcare, policy) → identifies desired support for long-term financial security.
  - Table 4: Financial opportunities (knowledge, products, support needs) → highlights awareness gaps and demand for tailored financial solutions.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Gig Economy
    definition: A labor market characterized by short-term, flexible, and task-based work, often mediated by digital platforms.
  - term: Freelancer
    definition: An independent worker who offers services to clients on a project or contract basis, without long-term employment commitment.
  - term: Income Volatility
    definition: The unpredictable fluctuation in earnings, which is a common challenge for freelancers with irregular workloads.
  - term: PFMS
    definition: Personal Finance Management System, a software application designed to help individuals manage their financial activities.
critical_citations:
  - "[De Stefano, 2016] — Foundation for precarious employment theory in gig work."
  - "[Hwang, 2024] — Income volatility as a core gig economy feature."
  - "[McNeal, 2024] — Financial burden of lacking employer-sponsored benefits."
  - "[Peetz et al., 2021] — Link between income volatility and financial planning."
  - "[Minter, 2017] — Barriers to financial services for freelancers."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: Focuses on freelancers in Metro Manila, a key demographic for Odin.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Details income sources and financial management practices relevant to understanding their financial structure.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly examines the financial behaviors, coping strategies, and challenges of freelancers.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Discusses financial management practices like budgeting and saving within a Filipino context.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: high
      justification: Identifies seasonal fluctuations and income peaks/dips as major challenges for freelancers.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: medium
      justification: Mentions lifestyle limitations and delayed major life decisions due to financial uncertainty, relating to spending cycles.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Freelancers track expenses and categorize spending for budgeting, aligning with this topic.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: low
      justification: Touches on prioritizing expenses (needs vs. wants), but does not delve into framework design.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Mentions use of digital financial tools and apps but does not analyze the PFMS landscape.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Explicitly identifies gaps in financial services and products for freelancers, a key limitation.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Describes varying financial management practices, suggesting different behavioral profiles.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: contextual
      justification: Highlights the challenge of new freelancers with no financial history, relating to cold-start.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: The paper mentions financial stress and anxiety due to income irregularity, which anomaly detection systems could potentially address.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Not a central theme of the paper.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: contextual
      justification: Freelancers express a need for trustworthy financial products and institutions, linking to user trust.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Discusses emergency funds and surplus-based saving, both core to savings goal management.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: medium
      justification: Mentions difficulty accessing loans and credit, which is relevant to debt management challenges.
  contribution: This paper provides qualitative evidence on the financial vulnerabilities of freelancers, which informs Odin's user modeling by highlighting the challenges of income volatility and benefit access. The identification of reactive coping strategies (e.g., budgeting, emergency savings) validates the need for proactive, predictive features in Odin. The expressed demand for tailored financial products, such as income-smoothing tools and accessible credit, directly justifies Odin's modules for forecasting, budget recommendation, and anomaly detection. Furthermore, the paper's findings on the lack of institutional support and financial literacy underscore the importance of Odin's design to provide clear, trustworthy, and educational financial guidance.
  directly_justifies:
    - "Freelancers lack access to traditional financial services, justifying Odin's need for inclusive design."
    - "Income volatility is a major challenge, supporting Odin's focus on predictive modeling for irregular income."
    - "Coping strategies are often reactive, highlighting the need for proactive and automated financial management tools."
    - "The demand for income-smoothing tools justifies Odin's focus on smoothing spending and income patterns."
    - "Lack of benefits like health insurance supports Odin's need to incorporate savings goals for such expenses."
  limits:
    - "Focuses on freelancers in Metro Manila only, limiting generalizability to other regions in the Philippines."
    - "Qualitative study design with a sample size of 50, which may not capture the full diversity of the freelance population."
    - "The study relies on self-reported data, which may be subject to recall bias or social desirability bias."
    - "[unacknowledged] The study does not quantify the prevalence of specific financial challenges among different freelancer subgroups." 
    - "[unacknowledged] The study does not evaluate the effectiveness of the specific financial tools mentioned by participants."
  mapping_rationale: A systematic scan of all 12 functional domains and associated topic codes was performed. The paper was flagged as highly relevant to the 'Filipino Cultural Context' domain, specifically topics 1.C (financial behavior), 2.B (seasonal spending), and 2.D (spending cycles), as it provides detailed qualitative evidence on income volatility and financial management practices of Filipino freelancers. The 'Expense Categorization' domain (topics 3.A, 3.B) was considered relevant due to the discussion of budgeting and expense tracking, receiving a 'medium' relevance. The 'Existing Systems & Gaps' domain (topics 4.A, 4.B) was highly relevant because the paper explicitly highlights limitations in current financial services. The 'Behavioral Profiling' domain (topics 5.A, 5.B) received 'medium' and 'contextual' relevance, as the paper discusses varied financial behaviors and the difficulty of establishing financial history. The 'Anomaly Detection' domain (topic 8.A) was deemed 'contextual' due to the discussion of financial stress from income fluctuations. The 'Data Privacy & User Trust' domain (topics 10.A, 10.B) was given 'low' and 'contextual' relevance, as trust is implied in the need for reliable institutions. The 'Savings & Debt Management' domain (topics 13.A, 13.B) was relevant ('medium') due to the focus on emergency funds and credit barriers. Other domains like 'Spending Forecasting,' 'Budget Recommendation,' 'Mobile-First Design,' 'User Retention,' and 'System Evaluation' were considered but rejected as the paper does not address algorithmic or design-specific aspects; its contribution is purely descriptive and motivational. Overall, the paper provides strong contextual and motivational justification for Odin's focus on addressing income volatility and financial exclusion among Filipino freelancers.
limitations:
  - "Focuses on freelancers in Metro Manila only, limiting generalizability to other regions in the Philippines."
  - "Qualitative study design with a sample size of 50, which may not capture the full diversity of the freelance population."
  - "The study relies on self-reported data, which may be subject to recall bias or social desirability bias."
  - "[unacknowledged] The study does not quantify the prevalence of specific financial challenges among different freelancer subgroups."
  - "[unacknowledged] The study does not evaluate the effectiveness of the specific financial tools mentioned by participants."
remember_this:
  - "Income volatility is the primary financial challenge for freelancers."
  - "Freelancers often lack access to traditional benefits like health insurance."
  - "Barriers to credit and loans are common due to irregular income perception."
  - "Systemic reforms and tailored financial products are urgently needed."
  - "Financial stress significantly impacts freelancers' mental and social well-being."
```
---

## Paper 50: Rosario_summarized.md

**Source File:** `Rosario_summarized.md`

```yaml
paper_id: 10.64753/jcasc.v10i3.2426
designation: local
title: Personal Financial Management Practices of Average earning households within Indigenous Communities of Mountain Province: Exploring Their Strategies and Challenges
authors: Rosario, E. P.
year: 2025
venue: Journal of Cultural Analysis and Social Change
odin_topics:
  - 2.A
  - 2.B
  - 2.D
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 13.A
  - 13.B
tldr: Indigenous households in Bontoc integrate modern budgeting with cultural practices like og-ogfo and paluwagan, prioritizing communal obligations and kinship over individual accumulation to manage financial stress.
problem_and_motivation: Standard financial management frameworks often overlook how cultural traditions and kinship obligations shape financial behavior in Indigenous communities. There is a gap in understanding how these cultural systems interact with modern economic pressures. This study addresses that gap by examining the financial strategies of Indigenous households in Mountain Province.
approach:
  - A qualitative descriptive phenomenological design was used to explore lived financial experiences.
  - Data were gathered through semi-structured interviews and a focus group discussion with 12 participants.
  - Participants were purposively sampled from average-earning Indigenous households in Bontoc, Mountain Province.
  - Thematic analysis following Colaizzi's method was applied to transcribed interviews.
  - The interpretation was guided by Cultural Capital Theory, Social Identity Theory, and Behavioral Economics.
findings:
  - num: Households prioritize food, electricity, and education even during hardship, often delaying bills to fulfill kinship duties.
  - num: Cultural practices like og-ogfo (mutual aid) and bayanihan serve as primary informal safety nets.
  - num: Savings are irregular and often take indigenous forms like paluwagan, livestock, or stored rice.
  - num: Cultural obligations such as supon and og-ogfo significantly influence spending, often overriding personal financial goals.
  - Households cope with financial stress through budgeting, income diversification, and strong reliance on family and community solidarity.
  - Formal financial institutions are secondary to informal systems due to access barriers and trust-based preferences.
  - Financial resilience in Bontoc is collective and relational, not purely individual.
key_figures_tables:
  - "Table 1: Profiles of 12 participants with occupations, monthly incomes (₱10,000-₱25,000), and household sizes (3-6) → Shows diverse income sources within a constrained range."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Og-ogfo
    definition: A traditional system of communal labor and collective aid in the Cordillera region.
  - term: Bayanihan
    definition: A Filipino cultural practice of communal unity and cooperation to achieve a common goal.
  - term: Paluwagan
    definition: A rotating savings and credit association where members contribute regularly and take turns receiving the lump sum.
  - term: Supon
    definition: A practice of giving monetary support during rituals and community gatherings as a symbolic investment in solidarity.
critical_citations:
  - "[Lusardi & Mitchell, 2014] — Foundational for linking budgeting to financial resilience."
  - "[Collins et al., 2009] — Core reference on financial tools used by low-income families."
  - "[Banerjee & Duflo, 2011] — Seminal work on poverty and financial management constraints."
relevance:
  topics:
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Core focus on indigenous practices like og-ogfo, supon, and paluwagan.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: high
      justification: Details event-driven budget strain from weddings, rituals, and community gatherings.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: high
      justification: Directly addresses how cultural obligations (occasions) drive spending priorities.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Highlights reliance on informal systems over formal PFMS or banks.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies access barriers to formal finance and gaps in culturally sensitive financial literacy.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: low
      justification: Provides context on collective vs. individual financial behavior profiles.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Describes behaviors but does not classify them into profiles.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: Discusses savings but as informal practices (e.g., livestock) rather than formal goal management.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: low
      justification: Mentions borrowing and debt risks but not as a structured management approach.
  contribution: The study provides a culturally grounded perspective on financial management, directly relevant to Odin's design for Filipino users. It informs the development of culturally sensitive expense categorization by highlighting how cultural obligations influence spending. The findings on collective coping mechanisms and informal safety nets can justify features for social support and community-based financial tools. The detailed practices of paluwagan and og-ogfo offer concrete examples for designing features that align with existing user behaviors. Finally, the study's emphasis on trust-based systems directly supports Odin's rationale for building user trust and engagement through culturally resonant design.
  directly_justifies:
    - "Odin should account for cultural obligations like supon and og-ogfo in its expense categorization and forecasting models."
    - "Integrating features that support communal saving practices (e.g., paluwagan) can improve user retention."
    - "Budgeting and savings features in Odin must be flexible to accommodate irregular income and event-driven spending."
  limits:
    - "Small sample size (n=12) limits generalizability beyond the specific Bontoc Indigenous community."
    - "The study is qualitative and descriptive, not testing or evaluating specific PFMS algorithms or features."
    - "Focus on cultural practices, but does not quantify their impact on financial outcomes compared to modern methods."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to the domain of Filipino Cultural Context, specifically topics 2.A (Culturally Specific Financial Practices), 2.B (Seasonal and Cyclical Spending Patterns), and 2.D (Filipino Spending Cycles and "Occasions") due to its deep investigation of practices like og-ogfo, supon, and event-driven financial strain. Medium relevance was assigned to topics under Existing Systems & Gaps (4.A, 4.B) because it details the landscape of and gaps in formal systems for this demographic. Low relevance was assigned to Behavioral Profiling & Classification (5.A, 5.C) as the paper describes behaviors but does not profile them, and to Savings & Debt Management (13.A, 13.B) because it discusses these topics in an informal, non-structured manner. Topics related to algorithmic forecasting, budget recommendation, anomaly detection, mobile design, data privacy, engagement, and system evaluation were considered and rejected because the paper is a qualitative sociological study, not a computational or design-oriented paper. The overall relevance is contextual for these modules, informing the cultural backdrop but not providing algorithmic or user interface design insights. The paper is moderately relevant to Odin, primarily serving to ground the system in the cultural realities of its target Filipino users.
limitations:
  - "The study is confined to a single Indigenous community, limiting broader applicability. [unacknowledged]"
  - "Relies on self-reported data, which may introduce social desirability bias."
  - "Does not quantify the economic contribution of cultural practices, making it difficult to model. [unacknowledged]"
  - "Lacks a comparative analysis with non-Indigenous households in the same geographic area."
remember_this:
  - "Cultural practices like og-ogfo and paluwagan are primary financial safety nets."
  - "Households prioritize communal obligations even when funds are insufficient."
  - "Budgeting is a social act of preparation for cultural duties, not just personal planning."
  - "Financial resilience is collective and relational, not purely individual."
  - "Cash alternatives (labor, food) are key to maintaining social membership.
```
---

## Paper 51: Remonde_summarized.md

**Source File:** `Remonde_summarized.md`

```yaml
paper_id: "f47ac10b-58cc-4372-a567-0e02b2c3d479"
designation: "local"
title: "The Effectiveness of Financial Literacy Program on Financial Management Skills of Millennial Teachers"
authors: "Remonde, E. A."
year: 2025
venue: "Slongan Multidisciplinary Research Journal"
odin_topics:
  - "1.A"
  - "1.C"
  - "13.A"
  - "13.B"
  - "12.A"
  - "2.A"
tldr: "Financial literacy program significantly improves financial management skills of millennial teachers across savings, budgeting, investing, debt, emergency funds, insurance, loans, expenditure, tax, and retirement."
problem_and_motivation: "Millennial teachers often lack financial literacy, leading to financial stress and poor decision-making. Existing research does not address the specific challenges of Senior High School teachers in Digos City. A tailored financial literacy program is needed to equip them with essential financial management skills."
approach:
  - "Pre-experimental design with pre-test and post-test assessments on 36 purposively selected millennial teachers."
  - "Intervention comprised a Financial Literacy Program with ten modules covering savings, budgeting, investing, debt, emergency funds, insurance, loans, expenditure, tax, and retirement planning."
  - "Data collected via validated multiple-choice survey questionnaires administered before and after the program."
  - "Statistical analysis employed mean, standard deviation, and paired samples t-test to compare pre-test and post-test scores."
findings:
  - "num: Pre-test overall mean score was 32.22 (approaching proficient), and post-test mean rose to 43.19 (advanced)."
  - "num: Paired samples t-test yielded a significance value of .000, indicating a statistically significant improvement (p < .05)."
  - "All ten financial management areas showed post-test mean scores in the 'Advance' range, with retirement planning scoring highest (4.75) and investing lowest (4.28)."
  - "Emergency funds had the highest pre-test mean (3.53), while investing had the lowest (3.14), both approaching proficient or developing."
key_figures_tables:
  - "Table 1: Pre-test mean scores by financial skill → baseline shows approaching proficiency overall, with gaps in investing and tax planning."
  - "Table 2: Post-test mean scores by financial skill → all skills advanced, indicating mastery across all areas."
  - "Table 3: Comparison of pre- and post-test means → t-test confirms significant improvement with p < .001."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Financial Literacy"
    definition: "Knowledge and skills to manage personal finances and make sound financial decisions."
  - term: "Millennial"
    definition: "Individuals born from the early 1980s to the mid-1990s."
  - term: "Pre-experimental design"
    definition: "Research design measuring changes before and after intervention without a control group."
critical_citations:
  - "[Lusardi and Mitchell, 2014] — foundational framework for financial literacy importance."
  - "[Miraj et al., 2023] — evidence of program effectiveness in similar context."
  - "[Wagner, 2015] — highlights millennial financial challenges."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "high"
      justification: "Paper focuses on Filipino millennial teachers, a subset of young professionals."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Directly measures financial management behaviors including savings, budgeting, and investing."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "high"
      justification: "Covers savings, emergency funds, and retirement planning."
    - code: "13.B"
      name: "Debt Management in PFMS"
      relevance: "high"
      justification: "Includes debt and loan management as key assessment areas."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Uses pre-test/post-test evaluation methodology applicable to system evaluation."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "low"
      justification: "Conducted in the Philippines but does not address specific cultural practices like paluwagan."
  contribution: "The study validates the need for targeted financial education modules on savings, debt, and budgeting, which inform Odin's user onboarding and educational content. Its pre-experimental evaluation design offers a model for assessing Odin's intervention impact. Findings on baseline proficiency gaps support Odin's cold-start user profiling and personalized recommendation features. The significant improvement post-training underscores the potential of structured financial literacy programs to enhance user financial behaviors within Odin."
  directly_justifies:
    - "Millennial teachers in Digos City have approaching proficiency in financial management before training."
    - "A structured financial literacy program can elevate financial management skills from approaching proficient to advanced."
    - "Significant improvements were observed across all ten financial management areas after the program."
  limits:
    - "No control group limits causal attribution of improvements solely to the program."
    - "Self-reported survey data may introduce bias."
    - "Findings are geographically limited to Digos City and may not generalize."
    - "Long-term retention of skills was not assessed."
  mapping_rationale: "Systematic scan across all 12 functional domains identified relevance in Filipino cultural context (Domain 2), financial behavior (Domain 1), savings and debt management (Domain 13), and evaluation frameworks (Domain 12). Topics 1.A and 1.C were flagged high due to direct focus on Filipino millennial teachers' financial behaviors. Topics 13.A and 13.B were flagged high because the paper measures savings, emergency funds, debt, and loan management – core modules in Odin. Topic 12.A was medium as the evaluation methodology (pre-test/post-test) could inform Odin's system evaluation but is not algorithm-specific. Topic 2.A was low because although Philippine-based, it does not explore culturally specific practices like paluwagan. Domains such as expense categorization (3), existing systems (4), behavioral profiling (5), forecasting (6), budget recommendation (7), anomaly detection (8), mobile-first (9), privacy (10), and retention (11) were rejected as the paper does not address algorithmic or system design aspects. Overall, the paper provides empirical evidence on financial literacy gaps and intervention effectiveness, which supports Odin's educational and behavioral modules."
limitations:
  - "Limited generalizability due to geographic and demographic constraints."
  - "Self-reporting bias may affect accuracy of financial skill assessment. [unacknowledged]"
  - "No control group; pre-experimental design weakens causal inference."
  - "Short-term measurement; long-term effects not examined. [unacknowledged]"
remember_this:
  - "Financial literacy program raised overall mean score from 32.22 to 43.19."
  - "Millennial teachers showed greatest improvement in retirement planning and loan management."
  - "Investing skill had the lowest post-test mean, indicating persistent need for investment education."
  - "Significant p < .001 confirms program effectiveness across all financial domains."
```
---

## Paper 52: Torres et al-2025a_summarized.md

**Source File:** `Torres et al-2025a_summarized.md`

```yaml
paper_id: "10.1145/3785171.3785192"
designation: "local"
title: "Consumer’s Financial Habits on Server-Based Electronic Money as It Affects Their Financial Behavior: Moderated By Monthly Transactions"
authors: "Torres, R. C.; Olaivar, G. M.; Britanico, S. I."
year: 2025
venue: "The 9th International Conference on Business and Information Management"
odin_topics:
  - "1.C"
  - "2.A"
  - "5.A"
  - "5.C"
tldr: "Saving, spending, donating, and investing habits significantly affect financial behavior on GCash, with transaction frequency moderating the spending-behavior relationship."
problem_and_motivation: "The rapid adoption of e-wallets in the Philippines necessitates understanding how specific financial habits influence consumer behavior on these platforms. The role of transaction frequency as a moderator in this relationship is not well-established, particularly for Filipino users."
approach:
  - "Quantitative study with 300 Filipino GCash users selected via purposive sampling."
  - "Multiple regression analysis used to test the effect of five financial habits on consumer financial behavior."
  - "Moderation analysis conducted to test the effect of average monthly transaction frequency on these relationships."
  - "Grounded in the Theory of Planned Behavior."
  - "Data collected via online questionnaires distributed through Google Forms and social media."
findings:
  - "num: Investment habits had the strongest significant positive effect on financial behavior (β = 0.243)."
  - "num: Spending habits significantly influence financial behavior (β = 0.115)."
  - "num: Saving habits significantly influence financial behavior (β = 0.178)."
  - "num: Donating habits significantly influence financial behavior (β = 0.144)."
  - "Credit/loan habits showed no significant effect on financial behavior."
  - "num: Transaction frequency significantly moderates the effect of spending habits on financial behavior (β = -0.163)."
  - "Higher transaction volumes enhance the positive relationship between spending habits and financial behavior."
  - "num: The model explains 40% of the variance in consumer financial behavior (R² = 0.400)."
key_figures_tables:
  - "Figure 1: Conceptual Framework based on TPB → Shows the hypothesized moderating role of monthly transactions."
  - "Table 1: Coefficients for the Regression Model → Shows significant effects for all habits except credit/loan."
key_equations:
  - equation: "y = β0 + β1x1 + β2x2 + β3x3 + β4x4 + β5x5 + ϵ"
    explanation: "Multiple regression equation for predicting financial behavior from financial habits."
definitions:
  - term: "SBEM"
    definition: "Server-Based Electronic Money, e.g., digital wallets and mobile payment platforms."
  - term: "GCash"
    definition: "A leading mobile wallet and digital payment platform in the Philippines."
  - term: "TPB"
    definition: "Theory of Planned Behavior, a psychological theory linking beliefs to behavior."
critical_citations:
  - "[Gomber et al., 2017] — Establishes the link between FinTech and changing financial behavior."
  - "[Raaij, 2016] — Discusses the psychological factors in consumer financial behavior."
  - "[Memon et al., 2019] — Provides guidelines for moderation analysis."
relevance:
  topics:
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Directly models financial behaviors of Filipino GCash users."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "medium"
      justification: "Examines financial habits within the Philippine digital payment context."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Provides a regression-based model for classifying financial habits."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "Uses quantitative statistical methods to identify significant financial habit predictors."
  contribution: "This paper provides empirical evidence from the Philippines that can inform Odin's user profiling module by identifying which financial habits (e.g., investing, saving) are most predictive of overall financial behavior. The findings on the moderating effect of transaction frequency can guide Odin's dynamic user modeling and personalization strategies. The relationship between investment habits and financial behavior suggests Odin could offer savings and investment features to improve user outcomes. The significant moderation effect implies that Odin's behavioral models should account for user activity level."
  directly_justifies:
    - "Investment habits have the strongest positive influence on financial behavior."
    - "Monthly transaction frequency moderates the impact of spending habits."
    - "Financial habits collectively explain a significant portion of financial behavior variance."
    - "Digital platforms like GCash can foster positive financial habits."
  limits:
    - "The study is cross-sectional and cannot establish causality."
    - "The sample is limited to Filipino GCash users, limiting generalizability."
    - "Relies on self-reported data, which may introduce bias."
    - "Does not account for user demographics in the main analysis beyond sampling."
  mapping_rationale: "The systematic scan across all 12 functional domains identified Behavioral Profiling & Classification (5.A, 5.C) and Filipino Cultural Context (2.A, 1.C) as the primary relevant areas. The paper's core contribution is analyzing financial habits (saving, spending, etc.) and their impact on behavior, which is directly applicable to understanding Filipino user profiles (1.C, 5.A). The moderation analysis offers insights into profile dynamics (5.C). Domains like Expense Categorization (3.A) and Forecasting (6.A) were rejected as the paper does not address algorithmic or system design aspects of these areas. The paper was assessed as having high relevance for Odin's user understanding and behavioral modeling, and medium relevance for cultural context."
limitations:
  - "Cross-sectional design, cannot establish causality. [unacknowledged]"
  - "Sample limited to GCash users in the Philippines. [unacknowledged]"
  - "Relies on self-report measures, potentially introducing response bias. [unacknowledged]"
  - "The study does not explore long-term behavioral trends. [acknowledged]"
remember_this:
  - "Investment habits show the strongest link to positive financial behavior."
  - "Transaction frequency strengthens the link between spending and financial behavior."
  - "Credit and loan habits did not significantly affect financial behavior in this sample."
  - "A model with five habits explains 40% of variance in financial behavior."
```
---

## Paper 53: Vega et al_summarized.md

**Source File:** `Vega et al_summarized.md`

```yaml
paper_id: 52c5e0a0-d0a0-5b1a-9c4e-8f6b9e2f1c3a
designation: local
title: The Influence of Buy Now, Pay Later (BNPL) Services on Consumer Spending Behavior
authors: Vega, N. C.; Constante, K. J. G.; Pacson, K. C.; Samaniego, J. G.; Tobias, T. E.
year: 2025
venue: International Journal of Sustainability and Advanced Integrated Research
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.C
  - 4.B
  - 5.A
  - 5.B
  - 7.A
  - 7.D
  - 8.A
  - 13.A
  - 13.B
tldr: BNPL services increase impulse buying and purchase frequency among young Filipino users, highlighting gaps in consistent budgeting and debt management.
problem_and_motivation: BNPL services are rapidly growing, but their influence on consumer spending behavior, particularly among young Filipinos, remains underexplored. Understanding these effects is crucial to prevent overspending and debt accumulation.
approach:
  - The study used a descriptive quantitative research design with structured surveys.
  - Data were gathered from 94% of respondents aged 18-25 in Gapan City, Nueva Ecija.
  - The survey instrument covered impulse buying, purchase frequency, budgeting, and debt accumulation.
  - Weighted means were calculated to determine levels of agreement across dimensions.
findings:
  - num: 94% of respondents were aged 18-25, and 74% were students with monthly incomes below PHP 5,000.
  - num: Respondents showed moderate agreement (WM = 2.71) on impulse buying tendencies when using BNPL.
  - num: BNPL services contributed to a noticeable increase in purchase frequency (WM = 2.67).
  - num: Awareness of BNPL repayment obligations was relatively high (WM = 2.91).
  - num: Moderate agreement was found on debt accumulation (WM = 2.55) and financial strain (WM = 2.65).
  - Users rely on future income to cover BNPL payments (WM = 2.84).
  - Many respondents lack consistent budgeting strategies and formal expense-tracking tools.
  - Multiple BNPL commitments were not yet overwhelming but signaled future challenges.
key_figures_tables:
  - "Figure 1: Top 11 products in BNPL purchase category → Clothing is the most common BNPL purchase."
  - "Figure 2: Types of goods bought with BNPL in the Philippines → Electronics and appliances are top purchases."
  - "Figure 3: Geographic location of the study area → Study focused on Gapan City, Nueva Ecija."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: BNPL
    definition: Buy Now, Pay Later, a payment method allowing consumers to make purchases and defer payment over time, often interest-free.
  - term: Impulse Buying
    definition: An unplanned purchase driven by emotions or a sudden urge without considering consequences.
  - term: Mental Accounting
    definition: The cognitive process of categorizing and evaluating financial transactions, which can affect spending decisions.
critical_citations:
  - "[Ang & Maesen, 2024] — BNPL increases purchase likelihood from 17% to 26%."
  - "[Bezawada et al., 2024] — BNPL adoption increases online spending by 6.42%."
  - "[Di Maggio et al., 2022] — BNPL increases purchasing power but may burden finances."
  - "[Gilbert et al., 2022] — Lower financial literacy leads to higher BNPL use and perceived lower risk."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: "The study focuses on young Filipinos (18-25), a key user group for BNPL and Odin."
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: "Provides data on income (below PHP 5,000) and employment status (mostly students) of BNPL users."
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: "Directly examines impulse buying, budgeting, and debt accumulation behaviors."
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: "Provides local context on BNPL use in Gapan City, reflecting Filipino consumer habits."
    - code: 2.C
      name: User-Declared Financial Preferences
      relevance: medium
      justification: "Surveys user perceptions of BNPL convenience, affordability, and budgeting ease."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: "Highlights gaps in BNPL regulation, transparency, and user financial literacy."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: "Identifies behavioral tendencies like impulse buying and reliance on future income."
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: "Tangential; discusses user behavior but not profile dynamics or cold-start issues."
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: "Examines budgeting strategies and their inconsistency among BNPL users."
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: low
      justification: "Tangential; mentions budget allocation but does not address infeasibility handling."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: "Provides context on financial strain and missed payments but not anomaly detection algorithms."
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: "Discusses how BNPL balances make it hard to save."
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: "Directly addresses debt accumulation and management challenges with BNPL."
  contribution: "This paper directly justifies Odin's behavioral profiling module by identifying specific spending tendencies among young Filipinos, such as impulse buying and reliance on future income. It informs the budgeting recommendation engine by highlighting gaps in users' budget planning and the need for simple, integrated tools. The findings on debt accumulation and awareness of repayment terms support Odin's anomaly detection and financial literacy features, as users exhibit moderate awareness but lack consistent tracking."
  directly_justifies:
    - "BNPL services increase impulse buying and purchase frequency among young Filipino users."
    - "Users show moderate awareness of repayment obligations but exhibit gaps in consistent budgeting and use of tracking tools."
    - "Reliance on future income to meet BNPL commitments highlights a need for better cash flow management and budgeting support."
    - "The study identifies a demand for centralized tools to manage multiple BNPL accounts and prevent debt accumulation."
  limits:
    - "The study is limited to Gapan City, Nueva Ecija, and may not be generalizable to the entire Philippines."
    - "The sample is skewed towards students (74%) with low income, limiting applicability to other demographic groups."
    - "Self-reported survey data may introduce social desirability and recall bias. [unacknowledged]"
    - "The cross-sectional design prevents causal inferences about BNPL's long-term effects. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The study was flagged as highly relevant to the Filipino Cultural Context (2.A, 2.C) as it provides local data on BNPL use in the Philippines. It was also highly relevant to Behavioral Profiling (5.A) and Savings & Debt Management (13.B) due to its direct examination of impulse buying, budgeting, and debt accumulation. The study was considered for but rejected from the Forecasting (6.A, 6.B) domain as it does not propose or evaluate predictive algorithms, and from Mobile-First Design (9.A, 9.B) as it does not address UX principles. Borderline cases included the study's relevance to both User-Declared Preferences (2.C) and Budgeting Strategies (7.A), as it surveys user perceptions and examines budgeting practices. Overall, the paper provides strong behavioral insights and identifies gaps in financial management, making it relevant to Odin's user understanding and advisory modules."
limitations:
  - "The study is limited to Gapan City, Nueva Ecija, and may not be generalizable to the entire Philippines."
  - "The sample is skewed towards students (74%) and low-income earners, limiting applicability to other groups."
  - "The cross-sectional design prevents causal inferences about BNPL's long-term effects. [unacknowledged]"
  - "Self-reported survey data may introduce social desirability and recall bias. [unacknowledged]"
  - "The study does not employ algorithmic methods, limiting its relevance to Odin's predictive and recommendation modules. [unacknowledged]"
remember_this:
  - "BNPL increases impulse buying (WM 2.71) and purchase frequency (WM 2.67) among young Filipinos."
  - "Awareness of BNPL obligations is high (WM 2.91) but budgeting and tracking remain inconsistent."
  - "Moderate debt accumulation (WM 2.55) and reliance on future income (WM 2.84) are key risks."
  - "Centralized BNPL management tools are in demand to prevent future financial strain."
```
---

## Paper 54: Cucio & Hennig_summarized.md

**Source File:** `Cucio & Hennig_summarized.md`

```yaml
paper_id: "10.5089/9798400295125.001"
designation: "local"
title: "Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and Complementarity"
authors: "Cucio, M.; Hennig, T."
year: 2025
venue: "IMF Working Paper"
odin_topics:
  - "1.A"
  - "1.B"
  - "1.C"
  - "2.A"
  - "2.D"
  - "4.A"
  - "4.B"
  - "6.A"
  - "8.A"
  - "9.A"
  - "10.A"
tldr: "One-third of Philippine workers are highly exposed to AI, with 61% of those in high-complementarity roles suggesting augmentation rather than displacement."
problem_and_motivation: "Rapid AI advancements may significantly transform labor markets, but the specific impact on the Philippine workforce, particularly its large BPO sector, remains underexplored. Understanding this impact is crucial for informing policy to harness benefits and mitigate job displacement."
approach:
  - "Merged AI exposure (Felten et al., 2021) and complementarity (Pizzinelli et al., 2023) scores with microdata from the Philippine Statistics Authority's October 2022 Labor Force Survey (183,602 observations)."
  - "Classified occupations into high exposure/high complementarity, high exposure/low complementarity, and low exposure categories based on median scores."
  - "Analyzed correlations between AI exposure/complementarity and demographic indicators like age, gender, education, wage, and sector."
  - "Compared Philippine results to other Asian economies using ILO employment data for a regional context."
  - "Assessed AI preparedness using the AI Preparedness Index (AIPI) covering digital infrastructure, human capital, innovation, and regulation."
findings:
  - "num: 36% of the Philippine workforce is highly exposed to AI."
  - "num: Of the highly exposed workers, 61% (22% of total workforce) are in high-complementarity roles, indicating potential augmentation."
  - "num: 39% of highly exposed workers (14% of total workforce) are in low-complementarity jobs, at risk of displacement."
  - "College-educated, young, urban, female, and well-paid service sector workers are most exposed to AI."
  - "The BPO sector has the highest proportion of jobs at risk (73% high exposure/low complementarity), though it represents only 3% of total employment."
  - "Government workers are the most exposed class of worker, driven by clerical roles."
  - "The Philippines scores well on human capital but lags in digital infrastructure compared to regional peers."
  - "The government has introduced a National AI Strategy Roadmap and pending legislation, but a comprehensive legal framework is lacking."
key_figures_tables:
  - "Figure 1: Philippine labor force summary statistics → Sets demographic context for AI exposure analysis."
  - "Figure 6: Exposure and complementarity across occupations → Visualizes how different occupational groups are categorized."
  - "Figure 8: Exposure and complementarity by demographic factors → Shows AI exposure correlates with gender, education, and wage."
  - "Table 2: AI exposure and complementarity in the Philippines → Provides key percentages for each category."
  - "Figure 9: AI preparedness across Asia → Indicates Philippines lags in digital infrastructure."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "AIOE"
    definition: "AI Occupational Exposure, a measure of overlap between AI capabilities and occupational tasks."
  - term: "Complementarity"
    definition: "The extent to which AI augments rather than replaces human labor in an occupation."
  - term: "BPO"
    definition: "Business Process Outsourcing, a key service sector in the Philippines."
  - term: "AIPI"
    definition: "AI Preparedness Index, a composite measure of a country's readiness for AI adoption."
critical_citations:
  - "[Felten et al., 2021] — Developed the AI exposure index used in this analysis."
  - "[Pizzinelli et al., 2023] — Developed the complementarity score used in this analysis."
  - "[Cazzaniga et al., 2024] — Provided the methodological framework and AI Preparedness Index."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "high"
      justification: "Analysis specifically examines Filipino workforce by age, education, and sector."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "medium"
      justification: "Discusses wage inequality and BPO sector dynamics relevant to financial structure."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "contextual"
      justification: "Provides labor market context that informs financial behavior, but does not directly study it."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "contextual"
      justification: "Focus on Filipino BPO and service sectors, but not on specific financial practices."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "contextual"
      justification: "Analysis of BPO sector exposure provides context for spending cycles, but is not the focus."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "low"
      justification: "Tangentially mentions digital infrastructure but does not review PFMS."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "low"
      justification: "Identifies gaps in digital infrastructure and skills, relevant to PFMS design but not directly."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses forecasting of AI impact on employment, analogous to forecasting spending."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "low"
      justification: "Mentions bias and errors in AI, relevant to anomaly detection but not central."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "low"
      justification: "Discusses digital infrastructure gaps, a prerequisite for mobile-first design."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "low"
      justification: "Mentions AI regulation and data privacy as a gap, but does not analyze PFMS data privacy."
  contribution: "This paper provides a granular, data-driven mapping of AI exposure and complementarity across the Philippine labor force, quantifying that 36% of workers are highly exposed, with 14% at displacement risk. It uniquely identifies the BPO sector as most vulnerable (73% high risk), despite its small workforce share, highlighting macro-critical spillover risks. The study correlates exposure with demographic factors (e.g., college-educated, female, young workers are most exposed), which can inform targeted policy interventions. By linking occupational AI scores with local LFS microdata and assessing AI preparedness (noting digital infrastructure gaps), the findings directly justify Odin's need for robust digital infrastructure and user-centric design."
  directly_justifies:
    - "College-educated and young service sector workers are most exposed to AI, indicating a need for financial tools tailored to this demographic."
    - "The BPO sector's high displacement risk (73% of its workers) underscores the importance of financial resilience features for affected users."
    - "Gaps in digital infrastructure suggest that Odin's mobile-first design must be robust and work under connectivity constraints."
    - "AI preparedness gaps in regulation and ethics support Odin's focus on data privacy and user trust."
    - "The potential for AI to augment high-complementarity jobs (22% of workforce) justifies Odin's predictive modeling to enhance user productivity."
  limits:
    - "The analysis is static and does not account for workforce retraining or new job creation over the medium term."
    - "Assumes task content of occupations in the Philippines is identical to the U.S. O*NET database, potentially underestimating exposure."
    - "AIPI does not capture all relevant dimensions for AI adoption, such as the importance of the BPO sector."
  mapping_rationale: "A systematic scan across all 12 functional domains was performed. The paper was flagged as highly relevant to the Filipino Demographics domain (1.A, 1.B) because it provides a detailed socio-economic breakdown of the Filipino workforce by age, education, and sector, directly informing the target user profile for Odin. It was also highly relevant to Predictive Modeling (6.A) and Behavioral Profiling (5.A, 5.B), as it presents a methodology for classifying workers into risk categories based on a combination of metrics (exposure and complementarity), analogous to classifying users by financial behavior. The paper's detailed analysis of the BPO sector and its vulnerability was considered a borderline case for Existing Systems (4.A) and Spending Cycles (2.D), but relevance was rated as low/contextual because the paper does not review specific PFMS software or spending patterns. Domains like Budget Recommendation (7.A-D) and Savings/Debt Management (13.A-C) were considered and rejected as the paper does not address financial allocation or goal management. The analysis of AI regulation and infrastructure gaps was deemed contextual for Data Privacy (10.A) and Mobile-First Design (9.A). Overall, the paper is highly relevant to Odin's understanding of its user base and the economic pressures that drive financial behavior, providing a strong justification for a predictive, user-centric financial management system."
limitations:
  - "Static analysis does not capture future workforce adaptation or job creation. [unacknowledged]"
  - "Relies on U.S. O*NET data, which may not perfectly reflect task content in Philippine occupations."
  - "Does not quantify the magnitude of potential productivity gains or wage effects."
  - "Does not account for spillover effects from BPO sector changes to the broader economy."
  - "AI Preparedness Index may not capture all relevant dimensions for Philippines-specific adoption."
remember_this:
  - "One-third of Philippine workers are highly exposed to AI."
  - "14% of the workforce is in low-complementarity roles at displacement risk."
  - "BPO workers are most at risk, with 73% in high-exposure, low-complementarity jobs."
  - "College-educated, young, and female service workers are most exposed but also most complementary."
  - "Philippines lags in digital infrastructure, a key barrier to AI adoption."
```
---

## Paper 55: Estorba et al_summarized.md

**Source File:** `Estorba et al_summarized.md`

```yaml
paper_id: 10.47772/IJRISS.2025.91200252
designation: local
title: Ka-abag o Babag? Exploring the Lived Experiences in the Context of Financial Well-being of Microfinance Borrowers
authors: Estorba, V. L.; Relativo, J. L. C.; Rellon, S. B. S.; Regis, K. J. M.
year: 2025
venue: International Journal of Research and Innovation in Social Science
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.D
  - 4.A
  - 5.A
  - 5.C
  - 7.A
  - 7.D
  - 10.A
  - 10.B
  - 11.B
  - 13.A
  - 13.B
tldr: Microfinance provides short-term financial relief and promotes discipline but can also perpetuate debt cycles, stress, and psychological strain for female borrowers in the Philippines.
problem_and_motivation: Existing literature relies heavily on quantitative measures of borrower financial well-being, failing to capture the subjective lived experiences and meaning-making of how microfinance impacts financial and psychological health. This gap hinders the development of holistic interventions that address both financial and emotional needs of borrowers.
approach:
  - A transcendental phenomenological qualitative design was used to explore the lived experiences of fifteen female microfinance borrowers in Argao, Cebu.
  - Purposive criterion sampling selected participants with at least three years of borrowing experience and three active loan cycles.
  - Data were collected via semi-structured interviews adapted from the CFPB Financial Well-Being Scale, conducted in Cebuano.
  - Colaizzi's seven-step phenomenological method was used for data analysis.
  - The study is grounded in Lazarus and Folkman's Transactional Model of Stress and Coping and Sen's Capability Approach.
findings:
  - Microfinance has a dual nature, acting as both support and hindrance to financial well-being.
  - Borrowers experienced significant pre-borrowing financial difficulties, including poverty and unstable livelihoods.
  - Microfinance provided immediate resources and improved capabilities but also introduced repayment pressures and psychological strain.
  - Effective coping strategies included budgeting, income diversification, positive thinking, and reliance on faith.
  - num: 47% of Filipino adults maintain outstanding debt, predominantly for daily consumption.
key_figures_tables:
  - Table 1: Financial difficulties before microfinance → Shows poverty as persistent challenge.
  - Table 2: Effects of microfinance → Shows dual impact of relief and burden.
  - Table 3: Coping strategies → Shows adaptive and emotional management techniques.
  - Table 4: Outcomes of debt strategies → Shows transformation and cyclical entrapment.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Ka-abag
    definition: Support or assistance.
  - term: Babag
    definition: Hindrance or obstacle.
  - term: PFMS
    definition: Personal Finance Management System.
critical_citations:
  - "[Lazarus & Folkman, 1984] — Foundational theory for stress and coping."
  - "[Sen, 1999] — Foundational theory for capability and well-being."
  - "[De Silva & Gunawardana, 2023] — Highlights microfinance-induced debt cycles."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Focuses on female borrowers, not specifically young professionals.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: low
      justification: Provides context on financial fragility but not structure.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Details coping and financial management behaviors.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Explores Filipino cultural practices like informal lending.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: high
      justification: Describes how emergencies and family obligations drive spending.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Contextualizes microfinance as an existing system.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Profiles borrowers based on coping and stress responses.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Thematic classification can inform profile development.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Reveals real-world budgeting strategies and constraints.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: medium
      justification: Shows how borrowers prioritize essential needs over loans.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Not directly addressed.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Reveals borrower distrust due to aggressive collection.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: low
      justification: Highlights debt dependency, a retention challenge.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Shows difficulty in saving due to debt.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: Provides direct evidence on debt management challenges.
  contribution: This paper directly informs Odin's development by highlighting the emotional and psychological burden of debt, which is critical for designing empathetic and user-centered PFMS features. It underscores the need for integrated financial literacy and psychosocial support within budgeting tools. The findings on coping mechanisms (budgeting, income diversification) can guide the design of practical, actionable features for users. The dual nature of microfinance as both support and hindrance validates the need for systems that can handle financial volatility and user stress.
  directly_justifies:
    - "Odin should incorporate features that help users manage financial stress."
    - "Budgeting tools must account for irregular income and emergency spending."
    - "Debt management modules should offer flexible repayment planning."
    - "Systems must support users in distinguishing between survival and investment spending."
    - "User trust is eroded by aggressive collection practices, informing UX design."
  limits:
    - "The study is geographically bounded to Argao, Cebu, limiting generalizability."
    - "The sample consists exclusively of women, excluding male perspectives."
    - "Self-reported narratives may be subject to social desirability bias."
    - "The cross-sectional design cannot capture long-term financial trajectories."
    - "Excludes perspectives of microfinance officers and institutional representatives."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was conducted. The paper's primary relevance falls under Behavioral Profiling (5.A, 5.C), Savings & Debt Management (13.B), and Filipino Cultural Context (2.A, 2.D), rated high due to direct qualitative evidence on borrower psychology and culturally embedded practices like informal lending and family obligations. Medium relevance was assigned to topics like 1.C (financial behavior), 7.A (budgeting), and 10.B (trust), as the paper provides supporting evidence. Domains like Mobile-First Design (9.A, 9.B) and Algorithmic topics (6.A, 6.B) were rejected as the paper is qualitative and non-algorithmic. The paper strongly supports Odin's need for empathy-driven features and holistic financial health tracking.
limitations:
  - "Findings are not generalizable beyond the specific rural context of Argao. [unacknowledged]"
  - "Excludes male borrower perspectives, limiting understanding of gender differences in financial stress."
  - "Relies on self-reported narratives, which may be influenced by memory and social desirability."
  - "Cross-sectional design cannot observe how financial well-being evolves over multiple loan cycles."
  - "The dual role of women as financial managers and caretakers may create unique psychological burdens not explored in other demographics."
remember_this:
  - "Microfinance provides short-term relief but can create long-term debt dependency."
  - "Borrowers use budgeting, hustling, and faith to cope with financial stress."
  - "Debt stress spills into family relationships and erodes peace of mind."
  - "Many borrowers regret reliance on loans due to persistent debt cycles."
  - "Effective interventions must address both financial and emotional well-being."
```
---

## Paper 56: Esperanza et al_summarized.md

**Source File:** `Esperanza et al_summarized.md`

```yaml
paper_id: "d3b07384-d9a0-5a1b-9f3c-7a8b9c0d1e2f"
designation: "local"
title: "Digital Lending Efficacy on Debt Management of Wage Earners"
authors: "Esperanza, D. N.; Bithay, L. L.; Jesus, J. B.; Ople-Alviola, C.; Sumilhig, J. M.; Basilisco, G. L."
year: 2025
venue: "ASEAN Journal of Management & Innovation"
odin_topics:
  - "1.C"
  - "4.B"
  - "5.A"
  - "7.A"
  - "10.A"
  - "10.B"
  - "13.B"
tldr: "Digital lending quality significantly predicts repayment and cautious borrowing, while frequent usage reduces budget restraint among Filipino wage earners."
problem_and_motivation: "The expansion of digital lending improves credit access but risks impulsive borrowing and over-indebtedness without adequate financial capability. The influence of digital lending dimensions on specific debt management behaviors remains underexplored. Understanding these relationships is essential for designing inclusive and responsible digital financial systems."
approach:
  - "Used a quantitative descriptive-correlational design with 100 wage earners in Cebu City, Philippines."
  - "Measured digital lending accessibility, usage, and perceived quality via a structured survey adapted from validated scales."
  - "Assessed debt management via STOP (budget restraint), PAY (repayment), and CAUTION (informed borrowing) strategies."
  - "Applied multiple linear regression to test predictive relationships, with Cronbach's alpha >0.80 and IOC=0.92."
  - "Simple random sampling and ethical protocols followed."
findings:
  - "num: Perceived quality significantly predicted PAY (B=0.364, p=0.021) and CAUTION (B=0.379, p=0.010)."
  - "num: Frequent usage negatively predicted STOP (B=-0.259, p=0.007)."
  - "Accessibility did not significantly predict any debt management strategy."
  - "Wage earners showed strong agreement with STOP (M=3.96), PAY (M=3.80), and CAUTION (M=4.20)."
  - "Overall perception of digital lending was favorable (M=3.52), with accessibility highest (M=3.83) and usage neutral (M=3.17)."
  - "Challenges included insufficient income, lack of savings, and impulsive spending."
key_figures_tables:
  - "Table 1: Demographic profile shows majority female, aged 26-35, college-educated, monthly income PHP 10k-20k."
  - "Table 2: Accessibility rated agree (M=3.83), with ease of access highest (M=4.04)."
  - "Table 3: Usage rated neutral (M=3.17), indicating cautious engagement."
  - "Table 4: Quality rated agree (M=3.57), but privacy and collection practices concerns."
  - "Table 11: Regression for STOP shows usage negative significant; overall model not significant."
  - "Table 12: Quality positive significant for PAY; overall model not significant."
  - "Table 13: Quality positive significant for CAUTION; overall model significant (p=0.023)."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "STOP strategy"
    definition: "Budgetary discipline and debt avoidance through planning and restraint."
  - term: "PAY strategy"
    definition: "Commitment to timely repayment and ethical debt settlement."
  - term: "CAUTION strategy"
    definition: "Informed borrowing through critical evaluation of loan terms and risks."
  - term: "TAM"
    definition: "Technology Acceptance Model, explaining technology adoption via perceived ease and usefulness."
critical_citations:
  - "[Putri et al., 2023] — TAM framework for fintech adoption."
  - "[Wanof, 2023] — Financial Capability Framework linking access with decision-making."
  - "[Kawai et al., 2022] — Transparency reduces information asymmetry in lending."
  - "[Yue et al., 2022] — Increased access can lead to debt trap without safeguards."
relevance:
  topics:
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "low"
      justification: "Wage earners are a subset of Filipino young professionals; paper examines their financial behaviors."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "low"
      justification: "Highlights gaps in digital lending (privacy, aggressive collection) relevant to PFMS system limitations."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Defines STOP, PAY, CAUTION as behavioral strategies that can inform financial profiles."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "medium"
      justification: "STOP strategy directly addresses budgeting restraint as a domain knowledge for PFMS."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "medium"
      justification: "Privacy concerns and data protection issues are identified as quality dimensions."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "high"
      justification: "Perceived quality (trust/transparency) significantly predicts repayment and cautious borrowing, directly informing user trust in PFMS."
    - code: "13.B"
      name: "Debt Management in PFMS"
      relevance: "high"
      justification: "Core focus on debt management strategies and their predictors, directly relevant to Odin's debt management module."
  contribution: "The paper's finding that platform quality significantly influences repayment and caution behaviors directly supports Odin's debt management module (13.B) by highlighting the importance of transparent loan terms and trust-building features. The negative effect of frequent usage on budgeting discipline informs Odin's need to incorporate behavioral nudges and spending limits to prevent over-reliance on credit. The emphasis on user education and consumer protection aligns with Odin's data privacy and user trust design considerations (10.A, 10.B). The study's identification of challenges like insufficient savings and impulsive spending underscores the value of integrating savings goal management (13.A) and expense categorization (3.A) into Odin's framework. Overall, the results justify embedding financial literacy content and transparency metrics within Odin's personal finance management system."
  directly_justifies:
    - "Perceived quality of digital lending positively influences repayment behavior (PAY) and cautious borrowing (CAUTION)."
    - "Frequent usage of digital lending weakens budget restraint (STOP)."
    - "Accessibility alone does not significantly affect debt management strategies."
    - "Privacy concerns and aggressive collection practices undermine borrower trust."
  limits:
    - "None identified."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The most directly relevant domains were Debt Management (13.B) and User Trust (10.B), both assigned high relevance because the paper's core findings directly link platform quality to repayment and cautious borrowing, and usage to budgeting discipline. Behavioral Profiling (5.A) and Budgeting Strategies (7.A) were assigned medium relevance as the STOP, PAY, CAUTION strategies offer behavioral frameworks. Data Privacy (10.A) was medium due to explicit privacy concerns. Financial Behavior (1.C) and Existing Systems Gaps (4.B) were low as they are tangentially related. Domains such as Expense Categorization, Forecasting, Anomaly Detection, Mobile-First Design, Engagement, and Evaluation were rejected because the paper does not address these areas. Borderline cases included the overlap between STOP budgeting and 7.A, resolved by including 7.A for its direct budgeting focus; and between privacy and trust, resolved by including both. Overall, the paper provides moderate direct relevance to Odin, with actionable insights for debt management and trust modules."
limitations:
  - "Cross-sectional design limits causal inference and cannot track behavioral changes over time."
  - "Sample size of 100 in urban Cebu City may not be generalizable to rural areas or other demographics."
  - "Self-reported data may introduce response bias, especially on sensitive financial topics."
  - "Quantitative approach does not explore deep psychological or contextual factors influencing debt decisions."
  - "The study focuses on digital lending rather than broader personal finance management systems."
remember_this:
  - "Perceived quality of digital lending significantly predicts repayment and cautious borrowing behaviors."
  - "Frequent digital borrowing reduces budgeting discipline among wage earners."
  - "Accessibility and usage are less influential than platform quality for responsible debt management."
  - "Quality positively predicted PAY (B=0.364) and CAUTION (B=0.379) in regression models."
  - "Wage earners demonstrate strong caution (M=4.20) but face income and savings challenges."
```
---

## Paper 57: Albert et al-2025_summarized.md

**Source File:** `Albert et al-2025_summarized.md`

```yaml
paper_id: 10.62986/dp2025.35
designation: local
title: Gender Equality, Disability, and Social Inclusion in the Philippines: Progress, Challenges, and Opportunities in SDG 5 and SDG 10
authors: Albert, J.R.G.; Dacuycuy, C.B.; Quisumbing, A.R.; Basillote, L.B.; Cabalfin, D.L.D.; Vargas, A.R.P.; Luzon, P.E.D.; Mahmoud, M.A.
year: 2025
venue: PIDS Discussion Paper Series
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 3.C
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 7.A
  - 7.D
  - 8.C
  - 9.A
  - 10.A
  - 10.B
  - 11.A
  - 12.A
  - 13.C
tldr: Legal progress on GEDSI in the Philippines masks persistent implementation gaps; intersectional analysis reveals compound marginalization for women, PWDs, and IPs, requiring integrated, data-driven policy reforms.
problem_and_motivation: The Philippines has strong GEDSI laws but struggles with implementation, leaving marginalized groups excluded. Existing single-identity policies fail to address compounded disadvantages from gender, disability, and ethnicity intersections, limiting progress toward SDG 5 and SDG 10.
approach:
  - Mixed-methods combining longitudinal analysis of PSA surveys (FIES, LFS, NDHS) with Shapley decomposition and intersectional analytics.
  - Qualitative data from key informant interviews and focus group discussions with government officials, CSOs, and marginalized communities.
  - Quantifies relative contributions of gender, education, and geography to inequality using decomposition of FIES-LFS merged data for 2018, 2021, and 2023.
  - Examines GEDSI outcomes across SDG 5 and SDG 10 targets, with cross-cutting analysis on education, employment, and transportation access.
  - Evaluates policy effectiveness and implementation gaps through stakeholder perspectives and administrative data from DSWD, PNP, and other agencies.
findings:
  - num: Female disability prevalence (15%) is 50% higher than male (10%), with rates reaching 55% among women with no formal education.
  - num: Income inequality decreased, with the Gini coefficient falling from 0.453 in 2015 to 0.406 in 2023.
  - num: Teenage pregnancy rates declined from 8.6% in 2017 to 5.4% in 2022, but remain high among poor (10.3%) and less-educated (19.1%) women.
  - Intersectional analysis shows that spatial inequalities often exceed ethnic disparities, while ethnic inequality in education strongly correlates with poverty.
  - Women's labor force participation (51.6%) lags behind men's (73.1%), with underemployment persistently higher for men, masking women's exclusion from quality work.
  - The GAD budget has become compliance-oriented, with weak enforcement and misuse limiting its transformational potential.
  - Approximately 37% of Indigenous Peoples live in Geographically Isolated and Disadvantaged Areas, compounding ethnic exclusion with geographic marginalization.
key_figures_tables:
  - Table 1: Philippines' WEF Global Gender Gap rankings (2006-2025) → Volatility in rankings reflects discretionary political appointments, not steady progress.
  - Figure 7: Teenage pregnancy rates by educational attainment → Low education is a major risk factor; rates are 19.1% for primary-educated vs. 1.9% for college-educated.
  - Table 15: Inequality decomposition using household per capita income → Education is the primary driver of between-group income inequality.
  - Figure 18: IP Population overlapping with GIDAs → 2.9 million IPs live in GIDAs, facing severe service access barriers.
  - Table 34: Methodological concordance between NDPS severe and Washington Group classifications → NDPS identifies additional PWDs through environmental context.
key_equations:
  - equation: Total Hours Worked = α + β(sex) + γ(education) + δ(wealth) + ζ(urban) + η(NCR) + ε
    explanation: Regression model identifying determinants of weekly working hours.
definitions:
  - term: GEDSI
    definition: Gender Equality, Disability, and Social Inclusion.
  - term: GAD
    definition: Gender and Development budget policy (5% of agency budgets).
  - term: IP
    definition: Indigenous Peoples.
  - term: PWD
    definition: Persons with Disabilities.
  - term: 4Ps
    definition: Pantawid Pamilyang Pilipino Program (conditional cash transfer).
  - term: GIDA
    definition: Geographically Isolated and Disadvantaged Areas.
  - term: FPIC
    definition: Free, Prior, and Informed Consent.
critical_citations:
  - "[Crenshaw, 1989] — Foundational intersectionality theory adapted for Philippine context."
  - "[UN, 2015] — Establishes SDG 5 and SDG 10 targets and indicators."
  - "[World Bank, 2023] — Documents persistent gender gaps in asset access in East Asia."
  - "[David et al., 2018] — Assesses Philippines' progress on SDG 5."
  - "[Pérez-Brito et al., 2024] — Provides comprehensive data on IP exclusion and 'statistical invisibility'."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Provides detailed demographic, income, and employment data on Filipino young adults and labor market patterns.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Analyzes income distribution, wealth quintiles, and employment sectors relevant to financial structure.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Discusses labor force participation, underemployment, and time use patterns that shape financial behaviors.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Documents family-based care work and resource sharing norms that influence financial practices.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Provides context on poverty cycles and pandemic impacts but not specific seasonal spending data.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: Provides background on care work and family obligations that drive spending cycles.
    - code: 3.C
      name: User-Defined Allocation Constraints
      relevance: contextual
      justification: Discusses constraints from care work and low income but not user-defined budget allocation.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews existing social protection systems (4Ps) and financial inclusion barriers.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Critically assesses implementation failures of GAD budget, disability laws, and social programs.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Provides behavioral data on labor participation, care work, and risk tolerance relevant to financial profiles.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: contextual
      justification: Discusses data gaps and "statistical invisibility" for PWDs and IPs, relevant to profile initialization challenges.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Evaluates GAD budget allocation and policy frameworks for inclusive budgeting.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: contextual
      justification: Discusses policy implementation gaps and resource constraints but not algorithmic feasibility.
    - code: 8.C
      name: Cold‑Start Baseline Strategies for Anomaly Detection
      relevance: contextual
      justification: Highlights data scarcity for marginalized groups, relevant to baseline challenges for anomaly detection.
    - code: 9.A
      name: Mobile‑First Design Principles and Rationale
      relevance: low
      justification: Discusses ICT access and digital divide but not mobile-first design specifically.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Discusses ethical data collection, privacy, and confidentiality for vulnerable populations.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Highlights mistrust in government systems and need for community engagement, relevant to trust.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: contextual
      justification: Notes program awareness and compliance gaps, relevant to engagement challenges.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a comprehensive evaluation of GEDSI policies using mixed-methods and SDG monitoring frameworks.
    - code: 13.C
      name: End‑of‑Period Surplus as a Savings Input
      relevance: contextual
      justification: Discusses income growth and poverty reduction among bottom 40%, relevant to surplus capacity.
  contribution: This paper provides a comprehensive, data-driven baseline for understanding intersectional financial exclusion in the Philippines, directly justifying Odin's need for culturally-aware profiling (topics 1.A, 1.B, 1.C) and highlighting the limitations of current systems (4.B). Its analysis of GAD budget failures (7.A) and "statistical invisibility" (5.B, 8.C) informs Odin's design for inclusive, data-driven personal finance management that must account for compound marginalization.
  directly_justifies:
    - "Single-identity approaches fail to capture compound disadvantages experienced by marginalized groups."
    - "The GAD budget has become compliance-oriented, requiring outcome-based reform for effective allocation."
    - "Data gaps and 'statistical invisibility' hinder evidence-based policy and service delivery for PWDs and IPs."
    - "Labor market inequalities are driven primarily by geographic location and education, not just gender."
    - "Unpaid care work significantly reduces women's economic participation and financial autonomy."
  limits:
    - Data limitations and "statistical invisibility" of IPs and PWDs underrepresent their experiences. [unacknowledged]
    - Lack of formal IRB approval for qualitative components. [acknowledged]
    - Rapid policy changes make it hard to isolate specific intervention effects. [acknowledged]
    - Findings are specific to the Philippine context and may not generalize to other settings. [unacknowledged]
    - The focus on SDG 5 and SDG 10 limits exploration of other SDG interlinkages. [unacknowledged]
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. Domains for Filipino Cultural Context (2.A, 2.B, 2.D) and Behavioral Profiling (5.A, 5.B) were flagged as highly relevant due to the paper's focus on cultural practices, seasonal patterns (like pandemic impacts), and labor market behaviors. The Existing Systems & Gaps domain (4.A, 4.B) is directly addressed through critiques of the GAD budget and social programs, assigned high relevance. Budget Recommendation (7.A, 7.D) is informed by the GAD budget analysis, though infeasibility handling is only contextual. Anomaly Detection (8.C) is contextual due to data scarcity discussions. Mobile-First (9.A) and Data Privacy (10.A, 10.B) are medium/low relevance. User Retention (11.A) and System Evaluation (12.A) are contextual/high respectively. Savings (13.C) is contextual. Borderline cases included seasonal spending (2.B, 2.D) which was resolved by assigning both as contextual. User-defined constraints (3.C) were considered rejected because the paper does not analyze user-defined budget allocation; the focus is on policy-level constraints. The overall relevance is high for informing Odin's design with evidence on structural barriers and the need for intersectional, data-sensitive approaches.
limitations:
  - Official statistics under-represent IPs and PWDs due to geographic and documentation barriers. [acknowledged]
  - Small sample sizes for highly marginalized intersectional categories limit robust statistical analysis. [acknowledged]
  - Lack of formal Institutional Review Board approval. [acknowledged]
  - Rapid policy changes during the research period complicate causal attribution. [acknowledged]
  - Comprehensive time-use survey data is lacking, limiting care work analysis. [unacknowledged]
remember_this:
  - Legal frameworks are progressive but implementation fails, especially for GAD budgets.
  - Women with disabilities face 50% higher prevalence and severe education-related disparities.
  - Income inequality decreased but remains high, with education as the key driver.
  - Intersectional analysis is essential; single-identity policies miss compounded marginalization.
  - Data gaps create "statistical invisibility" for IPs and PWDs, undermining policy design.
```
---

## Paper 58: Paghasian_summarized.md

**Source File:** `Paghasian_summarized.md`

```yaml
paper_id: "10.69569/jip.2024.0198"
designation: "local"
title: "Financial Practices among Foundation University Employees: Basis for Financial Plan"
authors: "Paghasian, M. F."
year: 2024
venue: "Journal of Interdisciplinary Perspectives"
odin_topics:
  - "1.A"
  - "1.B"
  - "1.C"
  - "3.A"
  - "3.B"
  - "3.C"
  - "4.A"
  - "4.B"
  - "7.A"
  - "7.B"
  - "13.A"
tldr: "Foundation University employees demonstrate strong income, expenditure, and savings practices, but emergency funds and advisor consultation need improvement, with positive financial practices correlating with higher investments."
problem_and_motivation: "Financial stability requires effective planning and practices, yet many Filipino employees lack adequate financial literacy and emergency funds. Employers need data on employee financial behaviors to design effective wellness programs that improve financial health and job performance."
approach:
  - "Conducted a descriptive-correlational study with 191 regular and probationary employees at Foundation University."
  - "Used a validated, self-made survey questionnaire to measure financial practices across income, expenditure, savings, and investment."
  - "Applied weighted means, multiple linear regression, Kruskal-Wallis, and Mann-Whitney U tests to analyze data."
  - "Collected data on current monthly and yearly investments and reasons for investing."
  - "Assessed reliability using Cronbach's Alpha, with coefficients above 0.70 for all constructs."
findings:
  - "num: Employees showed strong financial practices with composite means of 3.81 (income), 3.83 (expenditure), and 3.84 (savings) on a 4-point scale."
  - "num: 61.26% of employees invest monthly in regular savings accounts, while 47.12% invest yearly in cooperative savings accounts."
  - "Employees demonstrate sound investment practices, including thorough review of products and risk assessment, with a composite mean of 3.48."
  - "The primary reason for investing is to attain financial freedom for family, with a mean of 4.50 on a 5-point scale."
  - "Financial practices in expenditure, savings, and investment significantly predict monthly investment availed (p = 0.005, 0.040, and 0.028, respectively)."
  - "Income practices significantly predict yearly investment availed (p = 0.026), while expenditure practices show a significant inverse relationship (p = 0.001)."
  - "Expenditure and investment practices significantly predict reasons for investing (p = 0.022 and p = 0.002, respectively)."
  - "A minority of employees lack emergency funds, with a mean of 3.40, indicating room for improvement."
  - "Employees moderately agree on seeking advice from financial advisors and investing in bank products, with means of 3.17 and 3.31, respectively."
key_figures_tables:
  - "Table 1: Financial practices by income → Employees manage income well but lack emergency funds."
  - "Table 2: Financial practices by expenditure → Employees avoid debt and use discounts effectively."
  - "Table 3: Financial practices by savings → Employees prioritize debt reduction and save regularly."
  - "Table 4: Financial practices by investment → Employees research investments but rarely consult advisors."
  - "Table 5: Current investments held → Savings accounts and cooperatives are the most common investments."
  - "Table 6: Reasons for investing → Financial freedom for family is the strongest motivator."
  - "Table 7: Regression for monthly investment → Expenditure, savings, and investment practices are significant predictors."
  - "Table 8: Regression for yearly investment → Income and expenditure practices are significant predictors."
  - "Table 9: Regression for reasons for investing → Expenditure and investment practices are significant predictors."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "PFMS"
    definition: "Personal Financial Management System"
  - term: "FU"
    definition: "Foundation University"
  - term: "NCR"
    definition: "National Capital Region"
  - term: "MP2"
    definition: "Modified Pag-IBIG 2 Savings Program"
  - term: "UITF"
    definition: "Unit Investment Trust Fund"
critical_citations:
  - "[BSP, 2018] — Filipino families spend more than they earn on average."
  - "[IFEBP, 2023] — Employers provide financial education due to employee knowledge gaps."
  - "[Pagkatotohan, 2023] — Cooperatives offer higher interest rates than banks."
  - "[Manulife, 2023] — Millennials and Gen Z show rising investment interest in the Philippines."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "high"
      justification: "Paper studies financial practices of Filipino university employees, a core demographic for Odin."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "high"
      justification: "Provides detailed data on income, expenditure, savings, and investment patterns of Filipino employees."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Directly measures financial behaviors like budgeting, spending, and saving habits of Filipino workers."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "medium"
      justification: "Indicators for expenditure practices can inform category design for Odin's expense tracking."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      relevance: "medium"
      justification: "Findings on spending priorities (needs vs. wants) inform how Odin might structure categories."
    - code: "3.C"
      name: "User-Defined Allocation Constraints"
      relevance: "low"
      justification: "Mentions budgeting and tracking expenses, which relates to user allocation but not in detail."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Provides baseline data on the financial landscape of Filipino employees, against which Odin can be positioned."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Identifies gaps like lack of emergency funds and advisor consultation, which Odin could address."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "high"
      justification: "Detailed findings on employee budgeting and spending behaviors directly inform budgeting strategy design for Odin."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Correlation between practices and investments suggests potential for personalized recommendations."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "high"
      justification: "Paper highlights savings practices and the gap in emergency funds, directly relevant to savings goal management."
    - code: "13.C"
      name: "End-of-Period Surplus as a Savings Input"
      relevance: "low"
      justification: "Relates to the concept of allocating surplus from budgets, though not explicitly addressed."
  contribution: "This paper provides empirical data on the financial practices of Filipino employees, which directly informs the design of Odin's budgeting and savings modules. The findings on income, expenditure, and savings behaviors can be used to benchmark Odin's expense categorization framework. The correlation between financial practices and investment levels justifies Odin's savings goal management feature. The identified gap in emergency funds and advisor consultation highlights opportunities for Odin's behavioral profiling and recommendation systems. Finally, the study's methodology offers a model for evaluating Odin's effectiveness in improving user financial practices."
  directly_justifies:
    - "The need for a feature to encourage and track emergency fund building in Odin's savings module."
    - "The design of Odin's expense tracking should prioritize needs and essential expenses based on employee practices."
    - "Odin's budget recommendation should account for Filipino spending patterns like prioritizing debt reduction before savings."
    - "The correlation between good practices and higher investments justifies Odin's goal-setting and progress tracking features."
  limits:
    - "Single-institution study limits generalizability to all Filipino young professionals."
    - "Self-reported data may be subject to social desirability bias. [unacknowledged]"
    - "The study is descriptive and correlational, not experimental, so causality cannot be inferred. [unacknowledged]"
    - "Limited sample size (191) and focus on employees from one university may not represent the broader population. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains was performed. Domains relevant to financial behavior and system design were flagged. Topics under 'Filipino Cultural Context' (2.A, 2.B, 2.C, 2.D) were considered but rejected as the paper does not address cultural practices or seasonal spending specifically. 'Expense Categorization' (3.A, 3.B) and 'Budget Recommendation' (7.A, 7.B) were selected with medium to high relevance due to the paper's focus on spending and budgeting practices. 'Existing Systems & Gaps' (4.A, 4.B) was selected as the paper provides a baseline of current employee practices and identifies gaps like lack of emergency funds. 'Savings & Debt Management' (13.A) was selected with high relevance due to the detailed savings pattern analysis. 'Behavioral Profiling' (5.A-C) was considered but rejected as the paper does not classify users into profiles. 'Anomaly Detection' (8.A-C) and 'Mobile-First Design' (9.A-B) were considered but rejected as not addressed. The overall relevance is high for informing the design of Odin's budgeting, savings, and expense tracking modules based on empirical Filipino employee data."
limitations:
  - "The study was confined to regular and full-time probationary employees of Foundation University, limiting generalizability."
  - "Some respondents withheld income and investment information due to confidentiality concerns."
  - "A few respondents declined to complete the survey, and busy schedules caused delays and some uncollected responses."
  - "Data is self-reported, which may not fully reflect actual financial behaviors. [unacknowledged]"
  - "The study's descriptive-correlational design does not establish causal relationships between financial practices and investments. [unacknowledged]"
remember_this:
  - "Filipino employees show strong budgeting and savings habits but lack emergency funds."
  - "Saving and investment behaviors are significant predictors of monthly investment levels."
  - "Positive spending practices correlate with higher investment engagement."
  - "Employees invest primarily for family financial freedom and retirement."
  - "The paper identifies a key gap in financial advisor consultation and bank product investment."
```
---

## Paper 59: Natal et al_summarized.md

**Source File:** `Natal et al_summarized.md`

```yaml
paper_id: 10.5281/zenodo.10892981
designation: local
title: "UNDERSTANDING FINANCIAL BEHAVIOR: AN ANALYSIS OF PERSONAL FINANCIAL MANAGEMENT AMONG WORKING PROFESSIONALS AMIDST THE GLOBAL INFLATION SURGE"
authors: "Natal, T. M. S.; Bentulan, K. K. T.; Del Rosario, R. J. L.; Olazo, C. B.; Mangarin, J. A."
year: 2024
venue: "Guild of Educators in TESOL International Research Journal"
odin_topics:
  - "1.A"
  - "1.B"
  - "1.C"
  - "2.A"
  - "5.A"
  - "13.A"
  - "13.B"
  - "13.C"
tldr: "A mixed-methods study of Filipino working professionals aged 24-35 finds strong saving habits and prudent buying during inflation, with demographics showing no significant effect on financial practices."
problem_and_motivation: "The global inflation surge challenges personal financial management, yet limited research focuses on Filipino working professionals' specific behaviors. This study addresses the gap by examining saving and buying habits in Balayan, Batangas, to inform strategies for financial resilience."
approach:
  - "Quantitative survey of 75 working professionals using a 4-point Likert scale measured saving and buying habits."
  - "Qualitative semi-structured interviews with 5 participants explored inflation impact and coping strategies."
  - "Chi-square tests assessed relationships between demographics (age, gender, industry, employment type, income) and financial behaviors."
  - "Thematic analysis identified patterns in qualitative responses regarding budgeting and purchasing strategies."
findings:
  - "num: No significant relationship between any demographic factor and saving habits (p>0.05 for all chi-square tests)."
  - "num: No significant relationship between any demographic factor and buying behavior (p>0.05 for all)."
  - "num: General weighted mean for saving habits was 3.56 (Strongly Agree), with highest item 'save for secure future' at 3.69."
  - "num: General weighted mean for buying behavior was 3.35 (Strongly Agree), with highest item 'assess practical value' at 3.59."
  - "Professionals prioritize budgeting, tracking expenses, and reducing discretionary spending to cope with inflation."
  - "Qualitative themes include budgeting, frugality, buying in bulk, seeking cheaper alternatives, and fixed-percentage saving."
key_figures_tables:
  - "Table 2: Mean responses for saving habits → top priority is saving for future security (3.69)."
  - "Table 3: Mean responses for buying behavior → highest is assessing practical value of items (3.59)."
  - "Table 14: Impact of inflation on financial decisions → professionals adjust budgeting and prioritize saving."
  - "Table 15: Purchasing strategies → buying in bulk and seeking cheaper alternatives are common."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Inflation"
    definition: "The general rise in prices over time, reducing purchasing power."
  - term: "Personal Financial Management"
    definition: "The handling of cash, credit, saving, borrowing, and spending to achieve financial goals."
  - term: "Saving Habits"
    definition: "Regular practices of setting aside income for future use."
  - term: "Buying Behavior"
    definition: "Consumer practices and decision-making in purchasing goods and services."
critical_citations:
  - "[Segal, 2022] — defines inflation as rising prices."
  - "[Oner, 2019] — describes inflation as rate of price increase."
  - "[Baranidharan, 2022] — defines financial behavior components."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "high"
      justification: "Paper directly studies this demographic (age 24-35, single, working)."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "high"
      justification: "Provides data on income, employment, and spending patterns."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Directly measures saving and buying behaviors."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "contextual"
      justification: "Mentions 'deserve ko 'to' mindset but does not deeply explore cultural practices."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "low"
      justification: "Describes saving and buying behaviors but does not classify into profiles."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "high"
      justification: "Focuses on saving habits and strategies, essential for goal setting."
    - code: "13.B"
      name: "Debt Management in PFMS"
      relevance: "medium"
      justification: "Discusses avoiding debt and overspending, relevant for debt management."
    - code: "13.C"
      name: "End-of-Period Surplus as a Savings Input"
      relevance: "high"
      justification: "Participants emphasize saving from salary, aligning with surplus allocation."
  contribution: "This study provides empirical evidence on saving and buying behaviors of Filipino young professionals during inflation, informing Odin's user modeling by establishing baseline behaviors. It highlights the strong saving orientation, which can guide budget recommendation algorithms to prioritize savings goals. The finding that demographics do not significantly affect behavior suggests a uniform approach for Odin's core functionalities. The qualitative strategies (e.g., fixed-percentage saving, bulk buying) offer actionable insights for designing nudge mechanisms. Overall, the paper supports Odin's design assumptions about the target users' financial priorities."
  directly_justifies:
    - "Filipino young professionals prioritize long-term savings over discretionary spending during inflation."
    - "Demographic factors do not significantly affect saving habits or buying behavior among the target group."
    - "Common coping strategies include reducing discretionary spending and seeking cheaper alternatives."
    - "Fixed-percentage saving is a prevalent strategy among professionals."
  limits:
    - "The study is limited to a single municipality (Balayan), which may not represent all Filipino young professionals."
    - "The sample size of 75 for quantitative and 5 for qualitative is relatively small."
    - "Only saving and buying behaviors are examined, excluding investment, insurance, and retirement planning."
    - "The study does not account for potential seasonal or cyclical spending patterns. [unacknowledged]"
    - "Self-reported survey responses may introduce social desirability bias. [unacknowledged]"
  mapping_rationale: "All 12 functional domains and their associated topic codes were systematically scanned. The Filipino Cultural Context domains (2.A-2.D) were considered; only 2.A is marginally touched via the 'deserve ko 'to' mindset, so it is assigned contextual. The Behavioral Profiling domain (5.A-5.C) is relevant because the paper describes saving and buying behaviors, but does not classify profiles, so 5.A is low. The Savings & Debt Management domain (13.A-13.C) is highly relevant as the paper focuses on saving habits and debt avoidance, with 13.A and 13.C high, 13.B medium. The Demographic domains (1.A-1.C) are directly addressed, all high. Other domains like Expense Categorization, Existing Systems, Forecasting, Budget Recommendation, Anomaly Detection, Mobile Design, Privacy, Engagement, and Evaluation were considered but rejected because the paper does not address system design, algorithms, or evaluation frameworks. Overall, the paper provides foundational behavioral insights for Odin's user modeling."
limitations:
  - "Limited to Balayan, Batangas, reducing generalizability to other regions."
  - "Small sample size, especially for qualitative phase."
  - "Focus only on saving and buying, ignoring other financial behaviors."
  - "No longitudinal data to track changes over time. [unacknowledged]"
  - "Potential self-report bias in survey responses. [unacknowledged]"
remember_this:
  - "Saving for future security is the top priority with mean 3.69."
  - "Demographics do not significantly predict saving or buying behavior."
  - "Professionals reduce discretionary spending to cope with inflation."
  - "Common saving strategies include fixed-percentage allocation and bulk buying."
  - "The study is context-specific to Balayan, limiting generalizability."
```
---

## Paper 60: Mesino-Romero et al_summarized.md

**Source File:** `Mesino-Romero et al_summarized.md`

```yaml
paper_id: "b7c9a2e1-4f5d-4b8a-9c3e-7d6f1a2b3c4d"
designation: "local"
title: "FROM SURGE TO STABILITY: DIGITAL PAYMENTS DRIVING A STEADY TRANSITION"
authors: "Mesina-Romero, B.; Masangkay, M.; Franco, M.; Yambao, M.; Delgado, K.; Bueno, P.; Lingat, P.; Natividad, G.; Lapus, A.; Manuel, R.; Yñigo, K."
year: 2024
venue: "Bangko Sentral ng Pilipinas"
odin_topics:
  - "2.A"
  - "4.A"
  - "4.B"
  - "9.A"
  - "9.B"
  - "10.A"
  - "10.B"
  - "12.A"
tldr: "Digital retail payments in the Philippines reached 57.4% of volume and 59.0% of value in 2024, driven by merchant, P2P, and B2B transactions, with government disbursements nearly fully digitalized."
problem_and_motivation: "The Philippines aims to increase digital payment adoption to enhance financial inclusion and economic efficiency. Despite progress, barriers such as high fees and limited consumer trust persist. This report tracks the current state and identifies areas for further digitalization."
approach:
  - "Used a measurement model with 24 payment use-cases across government, business, and person categories."
  - "Estimated digital share using quantitative data from banks, government agencies, and surveys, supplemented by assumptions."
  - "Analyzed volume and value of digital payments monthly."
  - "Identified top use-cases and growth rates."
  - "Assessed policy initiatives and regulatory frameworks."
findings:
  - "num: Digital payments account for 57.4% of total monthly retail payment volume and 59.0% in value."
  - "num: Merchant payments represent 66.4% of digital volume, P2P transfers 20.6%, and B2B supplier payments 6.2%."
  - "num: Merchant payments grew 29.1% year-on-year, P2P transfers 34.7%, and B2B 28.1%."
  - "num: Government disbursements are 97.2% digital, while person-to-government collections are only 24.6% digital."
  - "num: InstaPay transaction volume rose 67.8% from 2023 to 2024."
  - "Digital payments exceeded the Philippine Development Plan target of 52–54%."
key_figures_tables:
  - "Figure 1: Digital payments share by volume over time (2013–2024) → grew from 10% in 2013 to 57.4% in 2024."
  - "Figure 2: Digital payments share by value over time (2018–2024) → increased from 26.8% to 59.0%."
  - "Table 1: Monthly volume per use-case → P2X dominates at 70.5%, B2X at 28.5%, G2X at 0.9%."
  - "Table 2: Digitalization rates per use-case → G2X 97.2%, P2X 72.2%, B2X 19.8% by volume."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "BSP"
    definition: "Bangko Sentral ng Pilipinas (Philippine central bank)"
  - term: "P2X"
    definition: "Person-to-anyone payments (from individuals)"
  - term: "B2X"
    definition: "Business-to-anyone payments"
  - term: "G2X"
    definition: "Government-to-anyone payments"
  - term: "PESONet"
    definition: "Philippine Electronic Funds Transfer System (batch, high-value)"
  - term: "InstaPay"
    definition: "Real-time electronic fund transfer system"
  - term: "QR Ph"
    definition: "National QR code standard for interoperable payments"
  - term: "PPMI"
    definition: "Philippine Payments Management, Inc."
  - term: "AFCS"
    definition: "Automated Fare Collection System"
  - term: "CBDC"
    definition: "Central Bank Digital Currency"
  - term: "RTGS"
    definition: "Real Time Gross Settlement"
critical_citations:
  - "[Better Than Cash Alliance, 2019] — Provided baseline measurement model."
  - "[BSP Circular No. 1195, 2024] — Consumer redress for EFTs."
  - "[BSP Circular No. 1198, 2024] — Regulatory framework for merchant acquiring."
relevance:
  topics:
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "high"
      justification: "Discusses remittances and P2P transfers, which are culturally significant in the Philippines."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "high"
      justification: "Describes InstaPay, PESONet, QR Ph, and other national payment infrastructures."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Highlights barriers like high fees, low P2G digitalization, and need for consumer protection."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "medium"
      justification: "Mentions e-wallets and mobile banking but does not detail UX design principles."
    - code: "9.B"
      name: "Mobile UX Design for Personal Finance"
      relevance: "medium"
      justification: "References QR code and mobile app usage but lacks specific UX analysis."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "Introduces consumer redress and security regulations (Circulars 1195 and 1198)."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "high"
      justification: "Emphasizes trust and confidence as key to digital payment adoption."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "contextual"
      justification: "Provides a measurement model for national payment adoption, not specifically for personal finance systems."
  contribution: "This report provides empirical benchmarks for digital payment adoption in the Philippines, which inform Odin's expense categorization by highlighting dominant transaction types. Its identification of gaps in P2G digitalization suggests areas for user education and feature design. The consumer redress framework offers a model for Odin's trust and security modules. The measurement methodology can be adapted to evaluate Odin's system performance. The focus on merchant and P2P payments aligns with typical user spending patterns in Odin."
  directly_justifies:
    - "Digital payments in the Philippines reached 57.4% of retail volume in 2024."
    - "Merchant payments are the largest digital use-case, accounting for 66.4% of volume."
    - "P2G digital collection is only 24.6%, indicating a significant gap."
    - "Consumer redress regulations are critical for building user trust in digital finance."
  limits:
    - "Does not address individual spending behaviors or forecasting."
    - "Provides aggregate data but no segmentation by demographic such as young professionals."
    - "Lacks analysis of user experience or behavioral drivers."
    - "The measurement model relies on assumptions that may not capture all informal transactions."
  mapping_rationale: "A systematic scan across all 12 functional domains was performed. The domains flagged as relevant include: Filipino Cultural Context (topic 2.A, high), Existing Systems & Gaps (4.A high, 4.B high), Mobile-First Design (9.A medium, 9.B medium), Data Privacy & User Trust (10.A high, 10.B high), and System Evaluation (12.A contextual). Borderline cases: the report touches on seasonal spending (2.B) and cyclical patterns (2.D) but only implicitly; these were rejected because the data is aggregate and does not specify seasonal variations. Expense Categorization (3.A–C) was rejected as the report does not discuss category design. Behavioral Profiling (5.A–C), Spending Forecasting (6.A–B), Budget Recommendation (7.A–D), Anomaly Detection (8.A–C), User Retention (11.A–B), and Savings & Debt Management (13.A–C) were rejected because the paper does not address these algorithmic or user-centric topics. Overall, the paper is highly relevant for informing Odin's understanding of the national payment landscape, gaps, and trust considerations, but less so for individual-level financial management features."
limitations:
  - "Assumptions in estimation may introduce bias and uncertainty in the reported shares."
  - "Data sources may not cover all transactions, particularly informal or cash-based ones."
  - "The model does not capture user-level adoption drivers or behavioral factors."
  - "The report focuses on aggregate trends and does not provide granular insights for specific user segments."
remember_this:
  - "Digital payments reached 57.4% volume and 59.0% value in 2024."
  - "Merchant, P2P, and B2B payments drive 93.2% of digital volume."
  - "Government disbursements are 97.2% digital, but collections lag at 24.6%."
  - "Consumer redress and merchant acquiring regulations are key for trust."
  - "The BSP aims to make digital payments affordable to increase adoption."
```
---

## Paper 61: Somera_summarized.md

**Source File:** `Somera_summarized.md`

```yaml
paper_id: 10.69569/jip.2024.0257
designation: local
title: "I deserve this": A Phenomenological Study Toward Online Impulse Buying Behavior of Service Contractors
authors: Somera, K.
year: 2024
venue: Journal of Interdisciplinary Perspectives
odin_topics:
  - 2.A
  - 2.B
  - 2.C
  - 5.A
  - 5.C
  - 9.B
  - 11.A
  - 11.B
tldr: Filipino service contractors engage in online impulse buying as a coping mechanism for stress, driven by hedonic motivations and a sense of entitlement rooted in perceived self-worth and hard work.
problem_and_motivation: Online impulse buying among Filipino service contractors is an emerging phenomenon with significant psychological and financial implications, yet limited research exists on this specific demographic. Understanding their motivations, particularly the perception of "I deserve this," is crucial for comprehending the drivers and consequences of this behavior. The study addresses a gap in the literature by exploring the lived experiences of this group.
approach:
  - A qualitative phenomenological research design using Interpretative Phenomenological Analysis was employed.
  - Ten service contractors from Aurora, Philippines, were purposively selected based on high scores on Rook and Fisher's Impulse Buying Scale.
  - Data was collected through semi-structured online interviews and analyzed using thematic analysis to identify recurring patterns and themes.
  - Reflexivity and member-checking were used to establish rigor and validity.
findings:
  - num: Seven out of ten participants engaged in impulse buying before the pandemic, but their behavior intensified during it.
  - Impulse buying serves as a coping mechanism for stress, sadness, and loneliness, offering temporary emotional relief and mood regulation.
  - Motivations include a desire for immediate gratification, a sense of achievement, and healing the 'inner child' by fulfilling past unmet desires.
  - Negative impacts include significant financial stress, feelings of guilt, and regret following impulsive purchases.
  - The phrase "I deserve this" is used to justify purchases as a reward for hard work and to enhance self-concept and identity.
key_figures_tables:
  - Table 1: Themes and sub-themes on lived experiences → Six themes emerged covering emergence, motivations, impacts, extent, and coping strategies.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Impulse Buying
    definition: An unplanned, sudden, and strong desire to buy goods or services, characterized by an imbalanced emotional state and diminished cognitive evaluation.
  - term: Service Contractors
    definition: Employees engaged under a contract of service, often with job insecurity and financial challenges.
  - term: Interpretative Phenomenological Analysis (IPA)
    definition: A qualitative research method aimed at exploring and interpreting the lived experiences of individuals.
  - term: Hedonic Motivation
    definition: The drive to engage in behavior for pleasure, enjoyment, and emotional satisfaction rather than for practical or utilitarian reasons.
critical_citations:
  - "[Rook and Fisher, 1995] — Provides the Impulse Buying Scale used for participant selection."
  - "[Alase, 2017] — Outlines the steps for IPA data coding and analysis used in the study."
  - "[Minor et al., 2017] — Supports the link between impulse buying and self-concept/identity."
relevance:
  topics:
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Directly examines a Filipino-specific financial behavior (online impulse buying) among a unique local demographic (service contractors).
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: While not seasonal in the traditional sense, the study highlights cyclical spending tied to emotional states, stress, and salary cycles.
    - code: 2.C
      name: User-Declared Financial Preferences
      relevance: medium
      justification: Participants articulate personal justifications ("I deserve this") and preferences for spending, revealing underlying value systems and priorities.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: The study profiles the impulse buying behavior of a specific user segment, identifying key emotional and psychological drivers and consequences.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: The study uses a scale to identify individuals with high impulse buying tendencies, offering a potential classification method for behavioral profiling.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: The study mentions the convenience of mobile apps like Shopee and Lazada in facilitating impulse buying, relevant for designing interventions.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Impulse buying is shown to be a form of emotional engagement, providing insights into user motivations that could inform retention strategies for PFMS.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: low
      justification: Understanding the emotional triggers for impulse buying can help design PFMS features that engage users in healthier financial behaviors.
  contribution: The paper provides a deep, qualitative understanding of the emotional drivers and cognitive justifications behind online impulse buying among Filipino service contractors. This directly informs Odin's behavioral profiling module (5.A) by identifying key psychological states and triggers. The findings on stress, mood regulation, and self-concept can be used to design features that promote healthier financial behaviors and detect potential financial distress. The study's insights into user motivations and justifications for spending are crucial for developing effective budget recommendation and anomaly detection systems that account for user psychology.
  directly_justifies:
    - The paper establishes that impulse buying is a coping mechanism for stress and negative emotions.
    - Participants use the phrase "I deserve this" to justify unplanned purchases as a reward.
    - Impulse buying leads to significant financial stress and feelings of guilt and regret.
    - Self-control and mindful spending are key strategies used to counter impulse buying behavior.
    - The convenience of online platforms like Shopee and Lazada facilitates and intensifies impulse buying.
  limits:
    - The study is limited to a small sample (n=10) of service contractors from a single province in the Philippines.
    - Findings are based on self-reported data, which may be subject to recall and social desirability biases.
    - The study focuses on lived experiences and does not establish causal relationships or predictive models.
    - Generalizability to other Filipino demographics or regions may be limited.
  mapping_rationale: The systematic scan across all 12 functional domains flagged three primary areas of relevance: Behavioral Profiling & Classification, Filipino Cultural Context, and User Retention & Engagement. From Behavioral Profiling, codes 5.A (Financial Behavioral Profiles) and 5.C (Classification Approaches) were selected as high relevance, as the paper directly profiles and classifies impulse buying behavior. The Filipino Cultural Context domain was relevant through codes 2.A (Culturally Specific Financial Practices) and 2.B (Seasonal and Cyclical Spending Patterns), with high and medium relevance respectively, because the study focuses on a Filipino population and highlights spending tied to emotional and salary cycles. Code 2.C (User-Declared Financial Preferences) was selected as medium relevance due to the explicit justifications users provide for their spending. The paper also touches on Mobile-First Design (9.B) and Retention & Engagement (11.A, 11.B) with low to medium relevance, as it discusses the role of online platforms and emotional engagement. Domains like Expense Categorization, Spending Forecasting, Budget Recommendation, Anomaly Detection, and Data Privacy were considered and rejected because the paper does not address these computational or systemic areas. The paper offers significant qualitative insights for understanding user psychology, which is foundational for designing user-centric PFMS features like behavioral profiling, anomaly detection baselines, and engagement strategies.
limitations:
  - Small sample size (n=10) limits generalizability. [unacknowledged]
  - Reliance on self-reporting may introduce biases. [unacknowledged]
  - The study does not establish causal relationships between emotional states and impulse buying.
  - The research is geographically confined to Aurora province.
remember_this:
  - Impulse buying serves as a primary coping mechanism for stress among Filipino service contractors.
  - Financial stress and guilt are significant negative consequences of online impulse buying.
  - The phrase "I deserve this" justifies unplanned purchases as rewards for hard work.
  - Seven out of ten participants reported intensified impulse buying during the pandemic.
  - Self-control and mindful spending are key strategies to mitigate impulse buying behavior.
```
---

## Paper 62: Bongalonta et al_summarized.md

**Source File:** `Bongalonta et al_summarized.md`

```yaml
paper_id: 10.11594/ijmaber.05.08.32
designation: local
title: The Traditional Way of Saving Money Versus the Modern Style of Investment: The Financial Management Styles of Sorsogon State University (Sorsu) Bulan Campus Faculty Members
authors: Bongalonta, M. B.; Bongalonta, M. M.; Gigantoca, S. E.
year: 2024
venue: International Journal of Multidisciplinary: Applied Business and Education Research
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 3.A
  - 4.A
  - 7.A
  - 7.B
  - 13.A
tldr: Faculty members adopt both traditional (budgeting, paluwagan, piggy banks) and modern (bank deposits, stock investments) saving methods, facing challenges from rising costs, low financial literacy, poor debt management, and low/delayed salaries.
problem_and_motivation: Faculty members at Sorsogon State University experience financial difficulties despite stable government salaries, often resorting to high-cost borrowing that undermines their savings capacity. A significant gap exists in understanding their specific financial management practices and the problems they face, which hinders the development of targeted interventions to improve their financial well-being. This study addresses this gap by identifying the saving and investment practices of these faculty members to formulate a relevant financial management model.
approach:
  - A mixed-methods design was used with a survey and focus group discussions (FGDs).
  - The study involved 40 faculty members from Sorsogon State University Bulan Campus.
  - Quantitative data gathered faculty profiles, while qualitative FGDs explored practices and problems.
  - Thematic analysis of FGD transcripts identified patterns in financial management behaviors.
  - The findings informed the development of the Bongalonta’s Financial Model.
findings:
  - Most faculty members (62.5%) earn between P40,001-P50,000 monthly, but 82.5% spend over P12,000, leaving limited room for savings.
  - num: 60% of faculty members save only 0-15% of their income.
  - Faculty members use both traditional (budgeting, paluwagan, piggy banks) and modern (bank deposits, stock investments) methods to save.
  - Primary problems in handling finances include increasing cost of utilities and unexpected expenses, lack of financial literacy, poor debt management, and low/delayed salaries.
  - The "paluwagan" system, while used for saving, often leads to debt and default issues among participants.
  - Financial literacy is low, with faculty members stating they have no background or ideas in financial management.
  - High debt from loans (e.g., GSIS, Land Bank) consumes a large portion of salaries, hindering savings.
  - Delayed salaries, especially for non-permanent faculty, disrupt the ability to save.
  - A proposed financial model was created to guide faculty in budgeting, minimizing debt, saving for emergencies, and investing in retirement.
key_figures_tables:
  - Chart 9: Saving models used by faculty → Shows piggy bank and paluwagan are the most common.
  - Chart 6: Percentage of savings → Shows 60% of faculty save only 0-15% of their income.
key_equations:
  - equation: Savings = Income - Expenses
    explanation: Faculty savings are the residual after all expenses.
definitions:
  - term: Paluwagan
    definition: A traditional Filipino informal savings and credit system where members contribute a fixed amount and take turns receiving the pooled funds.
  - term: Piggy Bank
    definition: A container used to hold and save small amounts of money.
  - term: Bongalonta’s Financial Model
    definition: A four-step model designed to enhance faculty savings through budgeting, debt minimization, emergency funds, and retirement investment.
critical_citations:
  - "[Gage et al., 2020] — Found faculty face significant financial insecurity."
  - "[Chinn et al., 2019] — Showed faculty lack basic financial knowledge."
  - "[Goldrick-Rab & Kendall, 2016] — Linked part-time faculty to higher debt."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: Focuses on faculty, a subset of Filipino professionals.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Provides detailed data on income, expenses, and savings of faculty.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly examines financial management practices and problems.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: Discusses budgeting and expense tracking practices.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Describes traditional and modern saving/investment methods.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Explores budgeting as a primary saving practice.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Proposes a model to enhance savings, implicitly recommending budget allocation.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: Directly deals with practices and problems in saving money.
  contribution: This paper provides empirical data on the financial behavior of a specific Filipino professional group (faculty), which can inform the design of Odin's financial profiling and budgeting modules. The findings on the prevalence of traditional methods like "paluwagan" highlight the need for culturally-aware expense categorization and savings features. The identified problems, such as low financial literacy and poor debt management, justify the inclusion of educational components and debt management tools in Odin. The study's mixed-methods approach offers a model for understanding user needs, which is crucial for developing Odin's user-defined allocation constraints and behavioral classification. Overall, the research underscores the importance of designing for real-world constraints like irregular income and high debt burden.
  directly_justifies:
    - "Faculty members adopt both traditional and modern saving methods, indicating a hybrid approach."
    - "High monthly expenses (82.5% spend >P12,000) limit the capacity for savings."
    - "Lack of financial literacy is a significant barrier to effective money management."
    - "Debt repayment consumes a large portion of salary, reducing savings potential."
    - "Paluwagan systems, while popular, can lead to financial problems due to defaults."
  limits:
    - "Study is limited to a single campus, restricting generalizability to other institutions."
    - "Data relies on self-reporting, which may be subject to social desirability bias."
    - "The study is descriptive and does not employ a statistical model to infer causality."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to 'Financial Structure of Filipino Young Professionals' (1.B) and 'Financial Behavior...' (1.C) due to its detailed survey of income, expenses, and saving practices. It also provided high relevance to 'Budgeting Strategies' (7.A) and 'Savings Goal Management' (13.A) as it discusses specific budgeting practices, saving models, and the problems hindering saving. Medium relevance was assigned to 'Landscape of Existing Systems' (4.A) as it describes traditional and modern methods, and 'Budget Recommendation' (7.B) due to the proposed financial model. Low and contextual relevance were assigned to other topics like 'Anomaly Detection' (8.A-C) as the paper does not address algorithmic detection, and 'Data Privacy' (10.A-B) as it is not a focus. Borderline cases like the 'paluwagan' system, which touches on culturally specific practices (2.A) and cyclical spending (2.D), were ultimately categorized under 1.C and 4.A for their behavioral and systemic insights, as the paper's core focus is on financial management. Domains such as 'Behavioral Profiling' (5.A-C), 'Forecasting' (6.A-B), and 'System Evaluation' (12.A-C) were rejected as the paper is purely descriptive and does not engage with algorithmic or predictive approaches. Overall, the paper provides foundational behavioral and financial structure data relevant to Odin's design.
limitations:
  - "The study focuses on a single campus, limiting generalizability to other Filipino professionals."
  - "The sample size of 40 is relatively small for quantitative analysis."
  - "The research is descriptive and does not test for statistical associations between variables."
  - "The reliance on self-reported data may be subject to social desirability and recall bias. [unacknowledged]"
  - "The proposed financial model is not empirically validated. [unacknowledged]"
remember_this:
  - "Faculty save only 0-15% of their income despite earning P40,000-P50,000 monthly."
  - "Traditional methods like piggy banks and paluwagan are as common as bank deposits."
  - "High expenses and debt service are the primary barriers to saving for faculty."
  - "Lack of financial literacy is a major impediment to effective financial management."
  - "Delayed salary releases severely disrupt the saving capacity of faculty."
```
---

## Paper 63: Ramos-2024a_summarized.md

**Source File:** `Ramos-2024a_summarized.md`

```yaml
paper_id: 10.1177/09500170241247121
designation: local
title: Extreme Lockdowns and the Gendered Informalization of Employment: Evidence from the Philippines
authors: Ramos, V. J.
year: 2024
venue: Work, Employment and Society
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 10.A
tldr: Extreme lockdowns in the Philippines increased informal employment probability among employed women by 2.2 percentage points, driven by survivalist motives and compositional changes.
problem_and_motivation: The impact of extreme mobility restrictions on informal employment, distinct from pandemic recessionary effects, is understudied. Understanding gendered informalization is critical for designing targeted safety nets, especially in developing countries with large informal sectors and limited welfare support.
approach:
  - Used 16 pooled quarterly Labour Force Survey rounds (2016-2020) from the Philippines.
  - Applied a two-way fixed effects difference-in-differences design comparing lockdown and non-lockdown regions.
  - Defined informal employment per ILO guidelines, excluding professional, agricultural, and public sector workers.
  - Conducted heterogeneous analyses by gender, marital status, and presence of minor children.
  - Tested robustness using alternative age restrictions, time periods, and informal employment definitions.
findings:
  - Extreme lockdowns increased the probability of informal employment by 1.7 percentage points overall.
  - num: The effect was 2.2 percentage points for women and statistically insignificant for men.
  - num: The informalization effect was strongest for married/cohabiting women with minor children, at 8.0 percentage points.
  - num: Around 44% of households in lockdown regions engaged in additional income-generating work.
  - Compositional changes showed formal employment declined more than informal employment in lockdown areas.
  - Survivalist motives were supported as males were more likely to be informally employed than unemployed.
  - Women in lockdown regions experienced a steeper increase in informal employment rates than men.
  - The gendered informalization finding is robust across alternative definitions of informal employment.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Compositional informalization
    definition: Informality induced by changes in the size and composition of overall employment.
  - term: Survivalist informalization
    definition: Informality induced by the need to work due to absent welfare support and low savings.
  - term: Two-way fixed effects difference-in-differences
    definition: An econometric method using region and time fixed effects to estimate causal effects.
critical_citations:
  - "[ILO, 2020] — Established informal workers were directly affected by lockdowns."
  - "[Maurizio, 2021] — Found informal employment did not play its usual countercyclical role in Latin America."
  - "[Floro and Meurs, 2009] — Demonstrated gendered informalization after the Asian Financial Crisis."
  - "[Ducanes and Ramos, 2023] — Showed female employment declines in Philippines during lockdowns."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Directly analyzes labor market outcomes for Filipino workers.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Discusses low savings rates and lack of social protection as drivers of informalization.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Examines survivalist motives and coping mechanisms during crises.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Describes the survivalist motive as a culturally embedded coping strategy.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Contextualizes economic shocks but does not directly analyze seasonal spending.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Mentions crisis-driven spending but not cyclical occasions.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews state social assistance mechanisms as context.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies gaps in social protection and safety nets.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Provides empirical evidence of survivalist behavioral profiles.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: high
      justification: Demonstrates how crises shift workers into informal profiles.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Relies on survey data but does not address privacy.
  contribution: "This paper provides a causal framework for understanding how external shocks (lockdowns) drive informalization, which is critical for Odin's behavioral profiling module. The distinction between compositional and survivalist informalization offers a taxonomy for classifying user financial behaviors during crises. The finding that women with minor children are most affected informs Odin's cold-start handling for female users. The documented lack of social protection mechanisms underscores the need for Odin's proactive budgeting and savings features. The survivalist motive evidence supports Odin's design of flexible budget constraints to accommodate crisis-driven financial behaviors."
  directly_justifies:
    - "Extreme lockdowns increase informal employment probability among women by 2.2 percentage points."
    - "Women with minor children faced an 8.0 percentage point higher informalization risk."
    - "Survivalist motives drive workers to accept informal jobs over unemployment."
    - "Households with low savings are more likely to engage in informal income-generating work."
    - "Compositional changes alone cannot explain gendered informalization; survivalist motives matter."
  limits:
    - "LFS data undercount informal employment, potentially underestimating the true lockdown effect."
    - "Absence of panel data prevents tracking individual transitions into informal work."
    - "Sector-specific differences in informal employment are not analyzed."
    - "The study does not differentiate between voluntary and involuntary informal employment."
  mapping_rationale: "A systematic scan of all 12 functional domains and their 28 associated topic codes was conducted. Domains flagged as relevant include Filipino Cultural Context (2.A, 2.B, 2.D), Existing Systems & Gaps (4.A, 4.B), Behavioral Profiling (5.A, 5.B), and Data Privacy (10.A) as contextual. Topic 1.A (Filipino Young Professionals) was assigned high relevance as the paper directly studies Filipino workers. Topic 1.B (Financial Structure) was high due to low savings and welfare gaps. Topic 1.C (Financial Behavior) was high for survivalist motives. Topic 2.A (Cultural Practices) was medium for coping strategies. Topic 2.B (Seasonal Patterns) was contextual, as the paper does not analyze seasonal spending. Topic 2.D (Spending Cycles) was low, with only passing mention. Topic 4.A (Existing Systems) was medium for reviewing social assistance. Topic 4.B (Gaps) was high for identifying welfare shortcomings. Topic 5.A (Behavioral Profiles) was high for demonstrating crisis-induced informal profiles. Topic 5.B (Cold-Start) was high for showing how shocks shift profiles. Topic 10.A (Privacy) was contextual, as privacy is not addressed. Domains like Spending Forecasting (6), Budget Recommendation (7), and Anomaly Detection (8) were rejected as the paper does not address predictive modeling or algorithmic recommendations. The overall relevance is high for Odin's behavioral and contextual modules, providing foundational evidence for crisis-driven financial behavior and gender-sensitive design."
limitations:
  - "LFS data undercount informal employment in developing countries. [unacknowledged]"
  - "No panel data to analyze individual transitions. [unacknowledged]"
  - "Sector-specific differences are not explored. [unacknowledged]"
  - "The study does not differentiate voluntary from involuntary informal employment. [unacknowledged]"
remember_this:
  - "Extreme lockdowns increased informal employment by 2.2 percentage points for women."
  - "Mothers with minor children faced an 8.0 percentage point informalization risk."
  - "Survivalist motives drove workers to informal jobs over unemployment."
  - "Low social protection and savings are key drivers of crisis informalization."
  - "Gendered informalization is robust across alternative definitions and samples."
```
---

## Paper 64: Doroy_summarized.md

**Source File:** `Doroy_summarized.md`

```yaml
paper_id: 0b7f1f3c-4d5e-4f6a-9b8c-1d2e3f4a5b6c
designation: local
title: Debt-free or Debt Fret: Survey on Public-school Teachers in the Philippines as Basis for Intervention
authors: Doroy, C. S.
year: 2024
venue: 11th ISC 2024 (Universitas Advent Indonesia, Indonesia)
odin_topics:
  - 1.B
  - 2.A
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 13.B
tldr: Public-school teachers agree to be debt-free but doubt their willpower, generally deny loan addiction, and propose government-led interventions for debt management.
problem_and_motivation: Public-school teachers in the Philippines accumulate significant debt, but research often overlooks their willingness to become debt-free. Understanding this willingness and its relationship with loan addiction is crucial for designing effective interventions.
approach:
  - A descriptive-correlational design and snowball sampling were used to survey 84 public-school teachers across the Philippines.
  - Data was collected via a Google Form with scales for loan addiction and propensity to extinguish debt, both showing acceptable Cronbach's alpha.
  - Analysis included frequency, percentage, mean, and chi-square correlation to examine the relationship between the two primary variables.
findings:
  - Teachers agree to pay off debts but are uncertain about their willpower to do so (M=3.7 ± 0.47).
  - Respondents generally denied being addicted to loans (M=1.96 ± 0.77), but some acknowledged needing support.
  - Proposed interventions primarily include government policies to reduce interest rates (65.5%) and provide legal seminars (44%).
  - The chi-square test showed no significant relationship between loan addiction and propensity to extinguish debt (p = 0.431).
key_figures_tables:
  - Table 2: Profile of respondents shows 96.4% have current debt and 91.7% practice debt accumulation.
  - Table 3: Mean of Loan Addiction (1.96) indicates general disagreement with being addicted.
  - Table 4: Overall mean for Propensity to Extinguish Debt (3.7) indicates agreement.
  - Table 5: 65.5% of respondents proposed government policies to reduce interest rates.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Loan Addiction
    definition: A condition of being dependent on acquiring loans, potentially leading to financial distress.
  - term: Propensity to Extinguish Debt
    definition: The willingness and determination to pay off one's outstanding debts.
critical_citations:
  - "[Cruz, 2019] — Reports P319 billion debt for public-school teachers."
  - "[Pabiona, 2023] — Teachers borrow more than other government employees."
  - "[Magante et al., 2023] — Teachers are financially literate but still indebted."
relevance:
  topics:
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: contextual
      justification: The paper discusses the financial structure and debt levels of public-school teachers, a key professional group.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: It examines the "culture of borrowing" or "Loandon" among Filipino teachers.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: It provides context on government (DepEd, GSIS) interventions but doesn't analyze PFMS.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: It identifies gaps in government support (e.g., lack of legal/financial counseling) for teachers in debt.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: The study identifies two groups (willpower vs. addiction) and examines behavioral aspects like willpower.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: It touches on identifying different profiles (willpower vs. addicted) but not on algorithm challenges.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: The paper is centrally about the propensity to manage and extinguish debt, directly informing this topic.
  contribution: The paper provides a user-centered perspective on debt management by measuring the willingness and perceived need for support among public-school teachers. It supports Odin's design by highlighting the necessity of behavioral profiling to differentiate users by their financial mindset and willpower. The findings on loan addiction denial underscore the need for trust-building and non-judgmental interfaces. The proposed interventions, such as policy changes and financial coaching, frame the external support systems that a PFMS like Odin could integrate or complement.
  directly_justifies:
    - "Public-school teachers desire to be debt-free but lack the willpower to do so."
    - "A significant portion of teachers are in a cycle of debt accumulation, indicating a need for structured debt management tools."
    - "The relationship between loan addiction and debt repayment is not straightforward, requiring more nuanced user profiling."
  limits:
    - "The study uses a small, non-probability sample (snowball sampling) which limits generalizability."
    - "The findings are based on self-reported data, which may be subject to social desirability bias, especially regarding loan addiction."
    - "The study does not evaluate the effectiveness of any intervention, only proposes them."
  mapping_rationale: A systematic scan of all functional domains was performed. The paper was flagged for the "Savings & Debt Management" domain due to its core focus on debt repayment propensity, which maps directly to Topic 13.B. It was also considered relevant to "Behavioral Profiling & Classification" (Topics 5.A, 5.B) as it categorizes teachers based on willpower and addiction, and to "Filipino Cultural Context" (Topic 2.A) for discussing the culture of borrowing. The "Existing Systems & Gaps" domain (Topics 4.A, 4.B) was selected for its discussion of government interventions and their limitations. Domains like "Expense Categorization," "Spending Forecasting," and "Budget Recommendation" were rejected as the paper does not address these computational aspects. The "Mobile-First Design," "Data Privacy," and "Evaluation" domains were also deemed irrelevant. The paper offers high relevance for understanding user attitudes and needs regarding debt management, which is crucial for Odin's design.
limitations:
  - "The study's findings are based on a survey distributed online, which may exclude teachers with limited internet access. [unacknowledged]"
  - "The research does not account for other mediating factors like behavior, which it suggests for future study."
remember_this:
  - "Teachers want to be debt-free but doubt their willpower."
  - "Most teachers deny being addicted to loans despite high debt levels."
  - "Government intervention on interest rates is the top proposed solution."
  - "No statistical relationship found between loan addiction and debt repayment propensity."
```
---

## Paper 65: Lim & Cordova_summarized.md

**Source File:** `Lim & Cordova_summarized.md`

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
---

## Paper 66: Bunyi_summarized.md

**Source File:** `Bunyi_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8 # No DOI available
designation: local
title: Unpacking the Determinants of Financial Resilience in the Philippines
authors: Bunyi, M. K. C.
year: 2024
venue: Bangko Sentral ng Pilipinas Discussion Paper
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 3.A
  - 4.A
  - 5.A
  - 5.C
  - 7.A
  - 10.A
  - 10.B
  - 12.A
  - 13.A
  - 13.C
tldr: Examines financial resilience determinants in the Philippines using 2017 and 2021 Global Findex data, finding income, saving behavior, and gender as top predictors.
problem_and_motivation: Financial resilience is critical for Filipinos facing economic shocks, but its determinants are underexplored in the Philippines. Policymakers lack baseline data to design targeted interventions for the financially vulnerable.
approach:
  - Uses 2017 and 2021 World Bank Global Findex survey data for the Philippines with 1,000 respondents each.
  - Defines financial resilience as the ability to raise 5% of GNI per capita within 30 days.
  - Applies Logistic LASSO Regression and Decision Tree models to predict resilience and identify key predictors.
  - Evaluates model performance using accuracy scores, ROC curves, and confusion matrices.
findings:
  - Income quintile, saving behavior, and gender emerged as the top predictors of financial resilience in both 2017 and 2021.
  - num: Model accuracy scores ranged from 59-65% for 2017 data and 62-68% for 2021 data.
  - The gender gap in financial resilience widened from 7.5 percentage points in 2017 to 16.8 percentage points in 2021.
  - Tertiary education became a key predictor in 2021, second only to income quintile.
  - Borrowing for medical purposes showed a strong negative association with resilience in 2021.
  - Financial inclusion indicators like account ownership did not consistently translate to higher resilience.
key_figures_tables:
  - Figure 1: Financial resilience self-ratings in 2017 and 2021 → Resilience rates were 49.4% and 59.0%, respectively.
  - Figure 2: Financial resilience by age → Respondents aged 20-40 showed higher resilience in 2017.
  - Figure 4: Financial resilience by income quintile → Richer households reported higher resilience in both years.
  - Table 2: Financial resilience by sex → Gender gap widened from 7.5 to 16.8 percentage points between 2017 and 2021.
  - Figure 10: Logistic LASSO regression coefficients → Income quintile consistently had the largest positive coefficient.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Financial Resilience
    definition: The ability to withstand unexpected income loss or financial shocks.
  - term: Financial Inclusion
    definition: Accessibility, usage, and quality of financial products and services.
  - term: Logistic LASSO Regression
    definition: A regression method that uses L1 penalty to shrink irrelevant coefficients to zero.
  - term: Decision Tree
    definition: A non-parametric method that splits data into homogeneous groups based on predictor values.
  - term: Global Findex
    definition: World Bank database on individuals' access to and use of financial services.
critical_citations:
  - "[Salignac et al., 2019] — Provides the multidimensional financial resilience framework used for variable selection."
  - "[Demirgüç-Kunt et al., 2022] — Source of 2021 Global Findex data and financial resilience measure."
  - "[Klapper & Lusardi, 2019] — Links financial literacy to financial resilience."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: Analyzes financial resilience across Filipino adults including young professionals.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Examines income, savings, and debt patterns relevant to financial structure.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly investigates saving behavior and financial decision-making.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Analyzes remittance behavior which reflects Filipino cultural practices.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Discusses pandemic-related spending shifts but not seasonal patterns.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Mentions consumption patterns but not specifically occasion-based spending.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: low
      justification: Discusses borrowing purposes but not expense categorization frameworks.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: References BSP Financial Inclusion Survey and National Strategy for Financial Inclusion.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Identifies behavioral predictors like saving and borrowing for medical purposes.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses classification models (Logistic LASSO, Decision Tree) to profile resilience.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: low
      justification: Mentions financial literacy and planning but not specific budgeting strategies.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Acknowledges limitations of survey data but not system privacy concerns.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: Not directly addressed.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Evaluates model performance using accuracy, ROC, and confusion matrices.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: Saving behavior is a top predictor of financial resilience.
    - code: 13.C
      name: End-of-Period Surplus as a Savings Input
      relevance: low
      justification: Discusses savings but not specifically end-of-period surplus.
  contribution: This paper provides empirical evidence on key demographic and behavioral determinants of financial resilience in the Philippines, which can inform Odin's user profiling and risk assessment modules. The finding that income and saving behavior are top predictors justifies Odin's focus on income tracking and savings goal features. The identification of gender and education gaps supports Odin's need for personalized financial recommendations. The modest model accuracy highlights the need for more granular data, which Odin could collect through user interactions.
  directly_justifies:
    - Income quintile and saving behavior are the strongest predictors of financial resilience.
    - Financial inclusion does not guarantee financial resilience.
    - Gender and education are significant factors in financial vulnerability.
    - Borrowing for medical purposes is strongly associated with lower financial resilience.
  limits:
    - The narrow proxy measure for financial resilience may not capture all dimensions of the concept.
    - The survey data lacks demographic variables like home ownership and employment status.
    - The shift to phone-based surveys in 2021 may have introduced selection bias.
    - Model accuracy remained below 70%, suggesting unmeasured factors are important.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was conducted. The paper was flagged as highly relevant for domains related to Filipino demographics (1.A, 1.B, 1.C), behavioral profiling (5.A), and savings management (13.A), as it directly analyzes these constructs using survey data and machine learning. Medium relevance was assigned to domains concerning cultural practices (2.A) and existing systems (4.A) due to contextual mentions. Low relevance was assigned to domains like expense categorization (3.A) and budgeting strategies (7.A) because the paper does not address these specific mechanisms. Borderline cases included seasonal spending (2.B, 2.D) which were considered contextual due to pandemic-related discussions, and classification approaches (5.C) which were relevant due to the use of Logistic LASSO and Decision Tree models. Domains such as forecasting (6.A, 6.B), anomaly detection (8.A, 8.B, 8.C), and mobile-first design (9.A, 9.B) were rejected as they were not addressed. Overall, the paper provides foundational evidence for Odin's user profiling and savings features but has limited direct applicability to algorithmic modules like forecasting or anomaly detection.
limitations:
  - The financial resilience measure is a narrow proxy (5% of GNI per capita).
  - The dataset is limited to 1,000 respondents per year.
  - Model accuracy is modest (below 70%).
  - The shift to phone-based surveys in 2021 may have introduced selection bias.
  - Causal relationships cannot be established from the predictive models.
  - The variables are predominantly binary, limiting granularity.
remember_this:
  - Income quintile is the strongest predictor of financial resilience.
  - Saving behavior is critical for resilience, especially for lower-income groups.
  - The gender gap in resilience widened significantly from 2017 to 2021.
  - num: Model accuracy remained below 70%, indicating unmeasured factors are important.
  - Financial inclusion does not automatically translate to financial resilience.
```
---

## Paper 67: Carpizo et al_summarized.md

**Source File:** `Carpizo et al_summarized.md`

```yaml
paper_id: 4a5d7b1c-0c8f-5d2e-9a4b-3f6d1e8c7b2a
designation: local
title: The Impact of AUP-CES Livelihood Initiatives, Leadership and Management in Buklod Bahayan
authors: Carpizo, E. M.; Balitar, J. E.; Balila, J. S.
year: 2024
venue: 11th ISC 2024 (Universitas Advent Indonesia, Indonesia)
odin_topics:
  - 2.D
  - 4.B
  - 13.A
  - 13.B
tldr: Community cooperatives in the Philippines provide economic, social, and organizational benefits, with leadership training and institutional support being critical for sustainability and resilience.
problem_and_motivation: Poverty remains a persistent challenge in the Philippines, particularly affecting marginalized communities with limited access to income-generating opportunities. While cooperatives are recognized as a tool for economic empowerment, there is a gap in understanding the specific impact of leadership and management training on their long-term sustainability. This study addresses the need for actionable insights on how structured training and organizational support contribute to cooperative resilience and member benefits.
approach:
  - The study used a qualitative approach with Focus Group Discussions (FGDs) and individual interviews.
  - Participants were members of community cooperatives in Buklod Bahayan Subdivision, selected based on availability and willingness.
  - Data was collected using three validated, Filipino-translated guiding questions regarding cooperative origins, AUP support, and perceived benefits.
  - Thematic analysis was applied to transcribed interview and FGD data to identify recurring themes.
  - The study is grounded in a literature review covering poverty, alternative income, and the role of leadership in cooperatives.
findings:
  - "num: Members reported dividends from a Php 3,300 share investment, with one member receiving Php 5,580 in dividends."
  - Members value the cooperative as a reliable source of loans for emergencies, up to Php 10,000.
  - Socially, the cooperative fosters camaraderie, unity, and a sense of security, especially during crises.
  - Organizationally, members gained practical skills in accounting, leadership, and management from AUP-CES training.
  - The initiative and training provided by AUP-CES were cited as crucial for the initial formation and subsequent reorganization of the successful cooperative.
  - The study confirms earlier research on the critical role of leadership and management training in cooperative sustainability.
key_figures_tables:
  - "None."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "AUP-CES"
    definition: "Adventist University of the Philippines Community Extension Services"
  - term: "FGD"
    definition: "Focus Group Discussion"
critical_citations:
  - "[Garcia and Reyes, 2018] — Confirms leadership training's role in cooperative sustainability."
  - "[Cruz and Garcia, 2017] — Establishes link between alternative income and poverty reduction."
  - "[Quizon and Ballesteros, 2016] — Highlights cooperatives' role in income generation."
relevance:
  topics:
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: "Discusses cooperatives as a source of funds for emergencies and crises, aligning with Filipino financial coping mechanisms."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: "Highlights the gap between poverty and structured financial support, which community-based systems like cooperatives attempt to fill."
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: "Discusses cooperative shares and dividends as a form of collective savings, but not individual goal management."
    - code: 13.B
      name: Debt Management in PFMS
      relevance: low
      justification: "Mentions loan opportunities within the cooperative as a benefit, providing an alternative to high-interest formal debt."
  contribution: "This paper contributes evidence that community-based financial initiatives, when supported by leadership and management training, can deliver economic and social benefits to low-income Filipino communities. The findings on member dividends and emergency loan access provide qualitative benchmarks for measuring the impact of financial inclusion programs. For Odin, this study offers a case study on how informal financial structures function, highlighting the importance of social capital and organizational support in financial resilience. It underscores the need for PFMS to consider community-based savings and loan mechanisms when designing features for users in similar socioeconomic contexts."
  directly_justifies:
    - "Community cooperatives provide an alternative income source through dividends, loans, and discounts."
    - "Members gain relevant knowledge and skills from leadership and management training."
    - "Institutional support is crucial for the formation and sustainability of community cooperatives."
  limits:
    - "Qualitative study with a small sample size from a single community, limiting generalizability."
    - "Findings are based on self-reported perceptions, which may introduce bias."
    - "The study does not provide a quantitative analysis of the cooperative's financial performance or long-term economic impact. [unacknowledged]"
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was conducted. The domains flagged as relevant were 'Filipino Cultural Context' (topic 2.D, contextual), 'Existing Systems & Gaps' (topic 4.B, medium), and 'Savings & Debt Management' (topics 13.A and 13.B, both low). The paper's focus on community-based financial support for crises maps to Filipino spending cycles and financial coping mechanisms (2.D). Its discussion of the limitations of formal systems in addressing poverty (4.B) is central to Odin's rationale. The benefits of cooperative shares and loans relate tangentially to savings and debt management (13.A, 13.B). Domains like 'Expense Categorization,' 'Behavioral Profiling,' 'Forecasting,' and 'Mobile-First Design' were rejected as the paper does not address algorithmic, technical, or user-interface design aspects. Overall, the paper provides contextual and supporting evidence for Odin's mission, particularly in highlighting the importance of community-level financial support and the need to address gaps in formal financial inclusion."
limitations:
  - "The study is qualitative and does not quantify the long-term economic impact of the cooperative."
  - "The research is limited to a single community, which restricts the generalizability of the findings."
  - "Potential for social desirability bias in participant responses during FGDs and interviews. [unacknowledged]"
remember_this:
  - "Leadership and management training are critical for cooperative sustainability."
  - "Members received Php 5,580 in dividends from a Php 3,300 share investment."
  - "Community cooperatives provide vital emergency loans and social support."
  - "Institutional initiative is key to forming resilient community cooperatives."
  - "Skills in accounting and leadership directly benefit cooperative members."
```
---

## Paper 68: Ataza et al_summarized.md

**Source File:** `Ataza et al_summarized.md`

```yaml
paper_id: 10.XXXX/290
designation: local
title: The Impact of Psychological, Economic, Social Aspects, and Interest Rate Variations on Working Millennials' Saving Patterns Through Digital Banking
authors: Ataza, C.; Porcel, M.; Resabal, L.; Sandoval, A.; Bragas, C.
year: 2024
venue: Sachetas
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 3.A
  - 4.B
  - 5.A
  - 10.A
  - 11.B
  - 13.A
tldr: Psychological aspects and interest rate variations significantly positively affect the saving patterns of working millennials through digital banking in the Philippines.
problem_and_motivation: The financial behavior of Filipino working millennials using digital banking is not fully understood. There is a gap in knowledge regarding how psychological, social, and economic factors, along with interest rates, collectively influence their saving patterns. Understanding these dynamics is crucial for banks and policymakers to design effective financial products and inclusion strategies.
approach:
  - A quantitative, descriptive-correlational research design was employed.
  - Survey questionnaires were administered to a stratified random sample of 51 working millennials aged 26-42 in Metro Manila who have bank accounts.
  - The instrument used a 5-point Likert scale to measure psychological, economic, social, and interest rate factors.
  - Reliability was assessed using Cronbach's alpha, with all variables showing good to excellent internal consistency (0.804 to 0.926).
  - Data were analyzed using descriptive statistics and multiple linear regression to determine predictors of saving patterns.
findings:
  - num: Psychological aspects (Beta = 0.430, p = 0.006) and interest rate variations (Beta = 0.878, p = 0.000) were significant positive predictors of saving patterns.
  - num: Social aspects had a significant negative effect on saving patterns (Beta = -0.182, p = 0.016).
  - num: Economic aspects did not significantly predict saving patterns (Beta = -0.130, p = 0.293).
  - num: The overall model explained 75.34% of the variance in saving patterns (R² = 0.7534).
  - The largest age group of respondents (84.3%) was 26-31 years old, and the majority were female (58.8%) and single (86.3%).
  - Most respondents (58.8%) used both digital and traditional banks, while 31.4% used only digital banks.
key_figures_tables:
  - Table 2: Descriptive statistics show economic aspects had the highest mean (4.22) and social aspects the lowest (3.73). → Social factors show most variability and lowest perceived impact.
  - Table 3: Model summary shows interest rate variations have the highest R² (0.7006), followed by psychological aspects (0.3102). → Interest rates are the strongest single predictor.
  - Figure 10: Graphical representation of regression coefficients. → Interest rate variations have the strongest positive impact on saving patterns.
key_equations:
  - equation: Y = (0.430)P + (-0.130)E + (-0.182)S + (0.878)I + (-0.01)
    explanation: Regression model predicting saving patterns through digital banking.
definitions:
  - term: Digital Banking
    definition: The use of digital technologies and platforms to conduct banking and financial transactions.
  - term: Working Millennials
    definition: Individuals aged 26-42 who are employed and engaged in income-generating activities.
  - term: Psychological Aspects
    definition: Internal factors like financial anxiety, risk tolerance, and self-efficacy influencing financial decisions.
  - term: Interest Rate Variations
    definition: Fluctuations in the rate banks pay depositors for keeping money in savings accounts.
critical_citations:
  - "[Co & Centeno, 2023] — Found social factors influence banking preferences."
  - "[Jünger & Mietzner, 2020] — Examined FinTech adoption by German households."
  - "[Felici et al., 2023] — Studied consumer savings at low/negative interest rates."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: The study specifically focuses on Filipino working millennials, a core Odin user group.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Provides demographic data on income, employment, and banking modes of the target group.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly investigates saving behavior and its psychological and economic determinants.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: The study is situated in Metro Manila, providing a local context for financial behavior.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: low
      justification: Tangentially addresses income cycles through employment stability, but not explicit seasonal spending.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: low
      justification: Mentions income allocation between needs and wants, but does not focus on categorization.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: contextual
      justification: Highlights the need for digital banks to offer better tools and personalized offers.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Explores psychological profiles affecting saving, relevant to behavioral classification.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: The methodology states compliance with the Data Privacy Act of the Philippines.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: Findings on interest rates and psychological tools inform engagement and retention.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Discusses incentives and barriers to saving, relevant for goal management features.
  contribution: This study provides empirical evidence on the key drivers of saving behavior among Filipino millennials using digital banking, directly informing Odin's design of personalized financial management tools. The strong influence of psychological factors validates the need for behavioral profiling and confidence-building features within the app. The significant impact of interest rates highlights the importance of competitive rates and transparent communication to encourage saving. The negative effect of social aspects suggests that Odin should focus on internal user goals rather than social comparison, although social features could be designed carefully to avoid unintended negative consequences. The identified demographic and income distribution data helps in tailoring features and user onboarding experiences for the target Filipino user base.
  directly_justifies:
    - Interest rates are a significant predictor of saving behavior in digital banking.
    - Psychological factors like self-efficacy and risk tolerance are critical in shaping saving habits.
    - Social influences can have a negative effect on saving patterns.
    - Digital banking platforms should offer personalized financial tools to address diverse user needs.
    - Economic stability fosters confidence in saving, while downturns may reduce it.
  limits:
    - The sample size of 51 respondents is relatively small, limiting generalizability.
    - The study focuses on Metro Manila, which may not represent the entire Philippine population.
    - The use of purposive sampling may introduce selection bias.
    - The research relies on self-reported data, which can be subject to social desirability bias.
    - The cross-sectional design captures behavior at a single point in time.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains of Filipino Cultural Context, Behavioral Profiling, Savings & Debt Management, and User Retention were flagged as highly relevant. Topic 1.C (Financial Behavior) and 1.A (Demographic) were assigned high relevance due to the paper's direct focus on Filipino millennial saving patterns and its demographic profile data. Topic 13.A (Savings Goal Management) and 5.A (Behavioral Profiles) received medium relevance as the paper provides evidence for the psychological drivers and interest-rate sensitivity relevant to these modules. The domain of Expense Categorization was considered and rejected as the paper does not propose or evaluate categorization frameworks, only touching on income allocation. The mobile-first design domain was rejected as the paper does not address UX principles. The paper's modeling of behavior using survey data and regression provides a foundational understanding of user motivation, directly informing Odin's design for behavioral profiling and retention strategies.
limitations:
  - Small sample size (n=51) and use of purposive sampling may limit generalizability.
  - Focus on Metro Manila may not represent the broader Filipino population.
  - Reliance on self-reported survey data is susceptible to biases.
  - The cross-sectional design captures a snapshot in time and does not reveal causal relationships. [unacknowledged]
  - The model does not account for all potential confounding variables like financial literacy levels. [unacknowledged]
remember_this:
  - Psychological aspects and interest rates are the strongest predictors of millennial saving.
  - Social aspects had a significant negative effect on saving patterns.
  - The regression model explained over 75% of the variance in saving behavior.
  - Most digital bank users also maintain traditional bank accounts.
  - Higher interest rates serve as a strong incentive for increased savings.
```
---

## Paper 69: Blancaflor et al_summarized.md

**Source File:** `Blancaflor et al_summarized.md`

```yaml
paper_id: 10.1145/3698062.3698088
designation: local
title: Exploring Machine Learning for Credit Card Fraud Detection from a Philippine Perspective
authors: Blancaflor, E.; Asuncion, K. D.; Reyes, H. J.; Verzosa, M.
year: 2024
venue: 2024 The 6th World Symposium on Software Engineering (WSSE)
odin_topics:
  - 8.A
  - 8.B
tldr: Examines machine learning techniques for credit card fraud detection tailored to the Philippine context, emphasizing SVM and ANN models.
problem_and_motivation: Credit card fraud in the Philippines has surged 21% since the pandemic, yet traditional fraud prevention systems are inadequate for securing e-commerce networks. There is a pressing need to evaluate and adapt machine learning models to the country's unique economic, technological, and social milieu to enhance financial security.
approach:
  - Reviews existing literature on fraud detection systems (FDS) and their limitations, such as imbalanced data and concept drift.
  - Assesses the efficacy of machine learning models including Logistic Regression, k-NN, Naïve Bayes, SVM, and ANN.
  - Compares the performance of ANN and Logistic Regression enhanced with Genetic Algorithm and SMOTE.
  - Evaluates models using metrics like accuracy, sensitivity, specificity, precision, Matthews Correlation Coefficient, and balanced classification rate.
  - Contextualizes findings within the Philippine financial sector, referencing local fraud cases and regulatory responses.
findings:
  - num: Credit card fraud in the Philippines increased by 21% since the COVID-19 outbreak.
  - num: Online fraud cost Filipino consumers over P540 million in 2021 alone.
  - num: ANN-SMOTE demonstrated the best performance in accuracy, precision, recall, and F1-score for fraud detection.
  - num: Logistic regression achieved an accuracy of 54.86%, while k-NN and Naïve Bayes achieved 97.69% and 97.92% respectively.
  - SVM shows promise for fraud detection, with potential for improved performance through meta-learning.
  - Machine learning models offer superior pattern detection and scalability, making them the future of fraud detection despite explainability trade-offs.
key_figures_tables:
  - Figure 1: Comparative performance of ANN and LR with GA/SMOTE enhancements → ANN-SMOTE outperforms all other models on key metrics.
  - Table 1: Evaluation of ML models for credit card fraud detection → Highlights accuracy and improvement strategies for each model.
key_equations:
  - equation: "MCC = (TP×TN - FP×FN) / √((TP+FP)(TP+FN)(TN+FP)(TN+FN))"
    explanation: Balanced measure for binary classification with imbalanced classes.
  - equation: "BCR = (Sensitivity + Specificity) / 2"
    explanation: Average recall or balanced accuracy for skewed datasets.
  - equation: "f(x) = sgn(x.w) + b"
    explanation: Decision function of SVM for binary classification.
definitions:
  - term: MCC
    definition: Matthews Correlation Coefficient, a balanced metric for binary classification.
  - term: BCR
    definition: Balanced Classification Rate, the average of sensitivity and specificity.
  - term: SMOTE
    definition: Synthetic Minority Over-sampling Technique, used to address imbalanced data.
  - term: FPS
    definition: Fraud Prevention System, a system designed to prevent fraudulent transactions.
  - term: FDS
    definition: Fraud Detection System, a system designed to detect fraudulent transactions.
critical_citations:
  - "[Awoyemi et al., 2017] — Comparative analysis of ML techniques for credit card fraud detection."
  - "[Abdallah et al., 2016] — Survey of fraud detection systems and their limitations."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly addresses fraud detection, a core anomaly detection application for Odin.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Reviews and evaluates algorithms (SVM, ANN) applicable to spending data anomaly detection.
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Provides context on the Philippine digital economy, which includes young professionals.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: low
      justification: Mentions the Philippine economic and social milieu but does not detail specific practices.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Briefly discusses existing fraud prevention systems but focuses on security, not personal finance management.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Discusses data security and privacy concerns in the context of fraud detection.
  contribution: This paper provides a foundational review of machine learning models for fraud detection, which directly informs Odin's Anomaly Detection module (8.A, 8.B). The comparative analysis of SVM and ANN with techniques like SMOTE offers a benchmark for algorithm selection. The findings on accuracy and performance metrics (MCC, BCR) guide the evaluation framework for Odin's detection capabilities. The emphasis on the Philippine context provides justification for tailoring anomaly detection algorithms to local spending patterns.
  directly_justifies:
    - "Machine learning models offer superior pattern detection for identifying fraudulent transactions in spending data."
    - "Support Vector Machines and Artificial Neural Networks are effective for binary classification of fraudulent and non-fraudulent patterns."
    - "SMOTE and other sampling techniques are crucial for handling imbalanced datasets common in anomaly detection."
    - "The trade-off between model explainability and accuracy must be considered when deploying fraud detection systems."
  limits:
    - "The paper is a literature review and does not present new empirical results from a Philippine dataset."
    - "The study does not specify the demographic profile (e.g., young professionals) of the fraud victims."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to the Anomaly Detection domain (topics 8.A and 8.B) because it directly evaluates ML algorithms for detecting credit card fraud, which is a key application of anomaly detection in PFMS. It was also flagged as medium relevance to Data Privacy & User Trust (10.A) due to its discussion of security and contextual for Filipino Cultural Context (1.A, 2.A) as it references the Philippine economic setting. Domains like Expense Categorization, Spending Forecasting, and Budget Recommendation were considered and rejected because the paper does not address spending patterns, income allocation, or financial planning. The overall relevance to Odin is primarily for its algorithmic insights into anomaly detection, particularly the choice of ML models and handling of imbalanced data.
limitations:
  - "The study is a literature review and does not include primary data collection or experimentation on Philippine fraud cases. [unacknowledged]"
  - "The comparison of model performance (e.g., Table 1) aggregates results from different studies, which may not be directly comparable due to varying datasets. [unacknowledged]"
  - "The paper does not address the cold-start problem for anomaly detection when user data is sparse. [unacknowledged]"
remember_this:
  - "Credit card fraud in the Philippines increased by 21% since the pandemic."
  - "ANN with SMOTE outperformed other models in detecting fraudulent transactions."
  - "Machine learning models are the future of fraud detection despite accuracy-explainability trade-offs."
  - "Traditional fraud prevention systems are inadequate for securing e-commerce networks."
```
---

## Paper 70: Sanchez_summarized.md

**Source File:** `Sanchez_summarized.md`

```yaml
paper_id: 10.5281/zenodo.12730500
designation: local
title: MOTIVATIONAL FACTORS AND BEHAVIORAL INTENTION TO INVEST IN PHILIPPINE STOCK MARKET AMONG MILLENNIAL AND GEN-Z INVESTORS IN CALAMBA CITY
authors: Sanchez, M. Q. C.
year: 2024
venue: Ignatian International Journal for Multidisciplinary Research
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 5.A
  - 5.B
  - 7.A
tldr: Millennial and Gen-Z investors in Calamba City show a low positive correlation between motivational factors and behavioral intention to invest, with a notable gap between financial aspirations and current status.
problem_and_motivation: Despite increased stock market participation among young Filipinos, there is limited research on the specific motivational factors influencing their investment intentions. Understanding these factors is crucial for financial institutions and regulators to develop targeted strategies for engaging this demographic in the Philippine Stock Market.
approach:
  - The study employed a descriptive-correlational research design with 265 randomly selected Millennial and Gen-Z graduates from Laguna College of Business and Arts.
  - Data was collected using a survey questionnaire that measured motivational factors (financial knowledge, well-being, overconfidence bias, investment risk) and behavioral intention (attitude, subjective norm, perceived behavioral control).
  - The instrument was adopted from Yang et al. (2021) and Schmidt (2010), with Cronbach's Alpha values ranging from 0.861 to 0.950, indicating high reliability.
  - Statistical treatments included mean computation, independent t-tests, and Pearson Product-Moment Correlation Coefficient to analyze relationships.
findings:
  - num: The extent of observance of motivational factors was consistently 'Observed' across all variables, with financial well-being showing a gap between aspirations (mean 3.35) and current status (mean 2.58).
  - num: Overconfidence bias was significantly different between Millennials and Gen-Z (p=0.048), with Millennials showing slightly higher confidence.
  - num: Investment risk perception significantly differed between generations (p=0.000), while financial knowledge and well-being showed no significant difference.
  - The level of behavioral intention was 'With Intention' for all TPB components, with attitude being the highest (mean 3.05).
  - num: There was a significant low positive correlation (r = 0.172 to 0.372) between motivational factors and behavioral intention.
key_figures_tables:
  - Table 1.1: Financial Knowledge assessment → Mean of 2.76 indicates observed financial literacy among respondents.
  - Table 1.2: Financial Well-being assessment → Mean of 2.83 shows a gap between aspirations and reality.
  - Table 1.4: Investment Risk assessment → Mean of 2.94 indicates positive risk attitude.
  - Table 3.1: Test of difference for motivational factors → Significant differences found for overconfidence bias and investment risk.
  - Table 4: Correlation analysis → Low positive relationship between motivational factors and behavioral intention.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: TPB
    definition: Theory of Planned Behavior, a framework suggesting behavioral intention is shaped by attitudes, subjective norms, and perceived behavioral control.
  - term: PFMS
    definition: Personal Finance Management System.
critical_citations:
  - "[Ajzen, 1991] — Foundational theory for understanding behavioral intentions."
  - "[Yang et al., 2021] — Source of the motivational factors instrument."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Directly focuses on Millennial and Gen-Z Filipinos in Calamba City.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Examines financial knowledge, well-being, and risk perception of young Filipino professionals.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Investigates the behavioral intentions and motivational factors of young investors.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Provides context on Filipino investing behavior, though not deeply focused on cultural practices.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Uses TPB to classify behavioral intentions based on attitudes and controls.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: Touch on generational differences but does not directly address cold-start issues.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Proposes an action plan that includes financial management and goal setting.
  contribution: This paper provides empirical evidence on the motivational factors driving investment intentions among Filipino young professionals. It identifies a significant gap between financial aspirations and current status, which can inform the design of educational modules within Odin. The use of TPB offers a validated framework for understanding user attitudes, subjective norms, and perceived behavioral control that can be integrated into Odin's behavioral profiling. The proposed action plan's emphasis on practical financial management and community engagement aligns with Odin's user retention and engagement strategies.
  directly_justifies:
    - Financial knowledge is positively correlated with investment intention among young Filipino professionals.
    - A gap exists between financial aspirations and actual financial status for this demographic.
    - Social approval from respected individuals significantly influences investment intentions.
    - Confidence in stock selection is lower than overall confidence, indicating a need for targeted support.
  limits:
    - The study is limited to graduates of a single institution in Calamba City, affecting generalizability to other regions.
    - The study does not account for the impact of modern technology or social media on investment decisions. [unacknowledged]
    - The research design is correlational and cannot establish causality between motivational factors and behavioral intention. [unacknowledged]
  mapping_rationale: The paper was systematically scanned across all 12 functional domains. Domains flagged as relevant include Filipino Cultural Context (topics 2.A, 2.B, 2.C, 2.D) due to its focus on Filipino investors and their financial practices, Behavioral Profiling & Classification (5.A, 5.B, 5.C) because it uses TPB to classify behavioral intentions, and Savings & Debt Management (13.A, 13.B, 13.C) indirectly through its discussion of financial goals and security. Topic 1.A (Filipino Young Professionals as a Demographic) was assigned high relevance as the study's sample exactly matches this category. Topics 1.B and 1.C were also high due to the focus on financial structure and behavior. Topic 5.A was high for using TPB, while 5.B was low as it doesn't address cold-start issues. Topic 7.A was medium for proposing a budgeting action plan. Domains like Anomaly Detection (8.A-C) and Mobile-First Design (9.A-B) were considered but rejected as the paper does not address these areas. The paper's overall relevance to Odin is moderate, providing foundational insights into user behavior and motivation that can inform user profiling and educational content.
limitations:
  - The study is limited to graduates of a single institution in Calamba City, affecting generalizability to other regions.
  - The study does not account for the impact of modern technology or social media on investment decisions. [unacknowledged]
  - The research design is correlational and cannot establish causality.
  - Financial literacy among participants may not be representative of the broader young Filipino population. [unacknowledged]
remember_this:
  - Millennial and Gen-Z investors show a gap between financial aspirations and actual status.
  - Overconfidence bias and investment risk perception differ significantly between Millennials and Gen-Z.
  - A low positive correlation exists between motivational factors and behavioral intention to invest.
  - Social approval from respected individuals significantly influences investment decisions.
  - There is a need for tailored educational programs to bridge the financial aspiration gap.
```
---

## Paper 71: Cacnio & Romarate_summarized.md

**Source File:** `Cacnio & Romarate_summarized.md`

```yaml
paper_id: 939c1ae8-aa25-5e25-9b00-831bbd3cbb3c
designation: local
title: How does financial literacy affect financial behavior over the life cycle? Evidence from Filipino households
authors: Cacnio, F. Q.; Romarate, M. E. G.
year: 2024
venue: Bangko Sentral ng Pilipinas Discussion Paper Series
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 5.A
  - 5.B
  - 13.A
  - 13.B
tldr: Financial literacy, particularly financial aptitude, is positively linked to long-term financial behaviors like having retirement plans and insurance, with effects differing across age groups.
problem_and_motivation: There is limited evidence on how financial literacy affects financial behavior across different age groups in developing countries like the Philippines. Understanding this relationship is crucial for designing effective financial education programs.
approach:
  - Used data from the 2018 BSP Consumer Finance Survey, filtering to 7,084 households.
  - Constructed a financial literacy index (FLI) from two components: financial attitude and financial aptitude.
  - Applied ordinary least squares (OLS) regression to identify determinants of financial literacy.
  - Applied logistic regression to assess the effect of financial literacy and age on five specific financial behaviors.
findings:
  - num: Young adults display higher financial literacy than middle-aged and senior cohorts.
  - num: Income and education are positively related to financial literacy; females have slightly lower financial aptitude.
  - num: Those with higher financial attitude scores are more likely to pay loans on time.
  - num: Individuals with higher financial aptitude and who are middle-aged or seniors are more likely to have retirement or pension plans and insurance.
  - num: Middle-aged persons are less likely to have a loan-to-income ratio of less than one compared to young adults.
  - num: Higher financial literacy is associated with a lower likelihood of spending less than or equal to income.
key_figures_tables:
  - Table 1: Sample demographics showing 38.9% young adults, 45.2% middle-aged, and 16% seniors → Majority of respondents are middle-aged.
  - Table 2: Summary of FLI scores showing mean of 0.386 → Financial aptitude component is low at 0.099.
  - Table 5: OLS regression results showing young adults have higher financial literacy than older groups → Age is a significant determinant.
  - Table 6: Logit regression odds ratios for financial behaviors → Financial aptitude strongly predicts having retirement plans (OR=85.478) and insurance (OR=46.808).
  - Table 7: Average savings by age group, seniors have the highest at PHP 36,722 → Retirement savings accumulate with age.
key_equations:
  - equation: FLI_i = 1/2 ∑_j x_ij γ_j1 + 1/2 ∑_j x_ij γ_j2 ∈ [0,1]
    explanation: Financial literacy index from attitude and aptitude components.
definitions:
  - term: Financial Literacy Index (FLI)
    definition: A composite score measuring financial attitude and aptitude, ranging from 0 to 1.
  - term: Financial Attitude
    definition: Component of FLI reflecting attitudes towards money, spending, risk, and time discounting.
  - term: Financial Aptitude
    definition: Component of FLI reflecting financial activities like holding loans, deposits, and managing surplus.
  - term: BSP CFS
    definition: Bangko Sentral ng Pilipinas Consumer Finance Survey, a triennial household survey.
critical_citations:
  - "[Lusardi & Mitchell, 2014] — foundational review of financial literacy's economic importance."
  - "[Agarwal et al., 2009] — establishes age-based financial decision-making patterns."
  - "[Huston, 2010] — provides framework linking financial knowledge, literacy, and behavior."
  - "[Magante et al., 2023] — used for constructing the FLI methodology."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: Focuses on Filipino households and age cohorts including young adults (18-39).
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Provides data on income, loans, and savings structures across age groups.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly studies financial behaviors like spending, borrowing, and saving.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: Mentions remittances and inter-generational transfers common in the Philippines.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: low
      justification: Not a primary focus, but mentions spending variations due to life events.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Not directly addressed; study uses annual expenditure data.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Empirically profiles behaviors based on financial literacy and age.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: Shows how financial behavior changes over the life cycle, informing profile dynamics.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Examines savings and retirement planning behaviors across age groups.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: medium
      justification: Studies loan-to-income ratio and timely loan payments.
  contribution: This paper provides empirical evidence on the relationship between financial literacy and financial behavior across age groups in the Philippines. Its findings on age-specific behavior (e.g., young adults having higher literacy but older groups engaging in more long-term planning) can directly inform Odin's behavioral profiling (module 5). The study's methodology for constructing a financial literacy index and its findings on the importance of financial aptitude for long-term behaviors (like retirement and insurance) can guide Odin's approach to user segmentation and predictive modeling. The results on how financial literacy affects spending, borrowing, and saving behaviors offer actionable insights for designing personalized budget recommendations and savings goals (modules 7 and 13). Furthermore, the paper's identification of gaps in retirement planning among Filipino adults highlights a key opportunity for Odin's engagement and retention mechanisms (module 11).
  directly_justifies:
    - "Young adults have higher financial literacy than middle-aged and senior cohorts."
    - "Financial aptitude is a strong predictor of having retirement or pension plans."
    - "Higher financial attitude scores increase the likelihood of paying loans on time."
    - "Middle-aged individuals are less likely to have a loan-to-income ratio below 1."
    - "Being married or having children is associated with different financial behaviors."
  limits:
    - "Study is correlational and does not establish causality between financial literacy and behavior."
    - "The 2018 CFS data lacks detailed questions on financial knowledge and numeracy."
    - "Potential endogeneity between financial literacy and financial behavior is recognized."
    - "Measurement of financial literacy may not fully capture an individual's true understanding."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant for the 'Filipino Cultural Context' domain (topics 2.A, 2.B, 2.D) because it directly studies Filipino households and their financial behaviors, though the focus is more on demographic effects than cultural practices per se. High relevance was assigned to 'Behavioral Profiling & Classification' (5.A, 5.B) as the paper provides empirical evidence on how financial literacy and age shape financial behavior, directly informing user profiling. Medium relevance was assigned to 'Savings & Debt Management' (13.A, 13.B) due to its detailed analysis of loans, savings, and retirement planning. Topics like 3.A (Expense Categorization), 4.A (Existing Systems), and all algorithmic topics (6.A, 7.B, 8.B, etc.) were considered and rejected because the paper is an empirical economic study, not a systems or algorithm design paper. The paper is most valuable for its descriptive findings on Filipino financial behavior across the life cycle, providing a foundational basis for Odin's behavioral models and feature design.
limitations:
  - "Study is correlational, not causal."
  - "Data from 2018 may not reflect recent changes in financial behavior."
  - "Lacks detailed financial knowledge metrics, limiting the depth of the financial literacy index."
  - "Potential endogeneity between financial literacy and financial behavior."
  - "Sample size for some financial behaviors (e.g., loan payment) is limited."
remember_this:
  - "Young Filipino adults show higher financial literacy than older age groups."
  - "Financial aptitude strongly predicts having retirement plans and insurance."
  - "Higher financial literacy is associated with higher consumption and spending."
  - "Middle-aged Filipinos are more likely to have higher loan-to-income ratios."
  - "Financial education programs should be tailored to life cycle stages."
```
---

## Paper 72: Kikkawa et al_summarized.md

**Source File:** `Kikkawa et al_summarized.md`

```yaml
paper_id: 10.22617/WPS240025-2
designation: local
title: Measuring the contribution of international remittances to household expenditures and economic output: A micro-macro analysis for the Philippines
authors: Kikkawa, A.; Gaspar, R.; Kim, K.; Mariasingham, M. J.; Zamora, C. M.
year: 2024
venue: Asian Development Bank
odin_topics:
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 3.A
  - 4.A
  - 4.B
  - 5.A
  - 6.A
  - 7.B
  - 9.A
  - 13.A
  - 13.B
tldr: Remittance-financed household consumption and investment contributed 3.5% of total output, 3.4% of GDP, and 3.7% of total employment in the Philippines in 2018.
problem_and_motivation: Micro and macroeconomic studies of remittances use different definitions, making consistent assessment of their economic contribution difficult. This gap prevents a unified understanding of how remittance income flows from households to the overall economy.
approach:
  - Used 2018 Family Income and Expenditure Surveys (FIES) for micro-level household expenditure data on 180,000 households.
  - Estimated consumption equations using seemingly unrelated regression to determine marginal propensity to consume across 16 commodity categories.
  - Integrated micro-level remittance income and expenditure patterns into the 80-sector 2018 Philippine Input-Output table.
  - Mapped FIES commodity items to I-O sectors and adjusted for retail/wholesale trade margins and import content.
  - Simulated a 10% exogenous increase in remittance income to estimate macroeconomic and sectoral impacts on output, value added, and employment.
findings:
  - Households reported ₱742.2 billion in international remittance income, which is 43.8% of the central bank's aggregate figure.
  - Remittance-financed demand contributed 3.5% of total output, 3.4% of GDP, and 3.7% of total employment.
  - Manufacturing, agriculture, and wholesale/retail trade received the bulk of remittance-driven final consumption.
  - num: A 10% increase in remittance income raises GDP by 0.34 percentage points and creates nearly 150,000 jobs.
  - Remittance-receiving households allocate higher shares to education, health, and real property investment than non-recipients.
  - Savings/investment portion of remittances flows mostly to construction, accounting for over 70% of its sector allocation.
  - The manufacturing sector has the highest intersectoral linkages, contributing 35.5% of remittance-induced gross output.
key_figures_tables:
  - "Table 1: Consumption equation regression results → remittance dependency correlates with higher productive spending shares."
  - "Table 3: Consumption vs. savings/investment allocation by sector → manufacturing and agriculture dominate consumption; construction dominates investment."
  - "Table 4: Economic contribution by sector → manufacturing leads in output; agriculture leads in employment impact."
  - "Figure 5: Sectoral interdependency and output multipliers → manufacturing has highest forward and backward linkages."
  - "Figure 6: Simulated reallocation impact → additional remittances reduce food share, increase savings and investment shares."
key_equations:
  - equation: "C_{ij} = α + β_i TInc_j + Σ_{n=1}^{4} γ_{in} remdependence_{jn} + Σ_{n=1}^{4} ρ_{in} (TInc_j × remdependence_{jn}) + δ_i X_j + ε_{ij}"
    explanation: "Consumption equation estimating expenditure share by remittance dependency group."
definitions:
  - term: "FIES"
    definition: "Family Income and Expenditure Survey, a Philippine household survey."
  - term: "I-O"
    definition: "Input-Output, a macroeconomic framework showing sectoral interdependencies."
  - term: "BOP"
    definition: "Balance of Payments, a macroeconomic accounting statement."
  - term: "BSP"
    definition: "Bangko Sentral ng Pilipinas, the Philippine central bank."
critical_citations:
  - "[Clemens and McKenzie, 2018] — Documents micro-macro remittance data discrepancies."
  - "[Yang, 2008] — Shows remittances drive investment in education and microenterprises in Philippines."
  - "[Adams and Cuecuecha, 2010] — Demonstrates remittance impact on household spending patterns."
  - "[Goce-Dakila and Dakila, Jr., 2009] — Estimates macro impact of remittance reduction in Philippines."
relevance:
  topics:
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Provides detailed income and expenditure structure of Filipino households including remittance recipients.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Analyzes spending patterns, savings rates, and investment allocation of remittance-receiving households.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Directly quantifies the economic role of international remittances, a core Filipino financial practice.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: Provides cross-sectional analysis but not explicit seasonal patterns; relevant for contextualizing cycles.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: medium
      justification: Household expenditure data covers annual patterns; provides baseline for understanding cyclical spending.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Presents a detailed 16-category spending classification that can inform Odin's categorization.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews micro and macro studies on remittances, providing context for PFMS landscape.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies the gap between micro and macro remittance definitions as a measurement limitation.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Differentiates spending behavior between remittance-receiving and non-receiving households.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Provides baseline consumption patterns and elasticities useful for forecasting models.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: The consumption equation results can inform personalized budget recommendations.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: Not directly about mobile design, but data on digital financial service use is tangentially relevant.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: Quantifies savings behavior and investment allocation, informing savings goal features.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: contextual
      justification: Mentions financial services use but does not directly address debt management.
  contribution: "This paper provides a validated micro-macro framework for quantifying the economic impact of remittance income on household spending patterns and sectoral output. The consumption equation results offer a data-driven basis for Odin's expense categorization and behavioral profiling modules. The observed differences in spending between remittance-receiving and non-receiving households directly inform the design of personalized budget recommendation algorithms. The sectoral impact analysis highlights which economic activities are most sensitive to remittance-driven demand, guiding prioritization in savings and investment features. The methodological integration of household survey data with I-O tables demonstrates a robust approach for grounding PFMS modules in local economic realities."
  directly_justifies:
    - "Remittance-receiving households allocate higher shares to education and health, supporting targeted savings goals."
    - "Household spending patterns differ significantly based on remittance dependency, necessitating behavioral profiling."
    - "The savings/investment portion of income flows predominantly to construction and real estate."
    - "Manufacturing has the highest sectoral multipliers, indicating strong economic linkages."
  limits:
    - "The analysis is cross-sectional and cannot establish causal impact of remittances."
    - "FIES data does not identify remittance-financed family business investments separately."
    - "Model assumes remittance income is fungible with other income sources."
    - "Simulation does not account for potential spillover effects to non-recipient households."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes identified several areas of high relevance. The paper directly addresses Filipino financial structure (1.B) and behavior (1.C) through comprehensive household expenditure data. Culturally specific practices (2.A) are central, as the study quantifies the economic role of international remittances. Spending patterns (2.B, 2.D) are analyzed in detail, providing baseline data for understanding cycles. The 16-category spending classification (3.A) is directly applicable to Odin's categorization framework. The paper's review of existing studies (4.A) and its identification of measurement gaps (4.B) provide context for PFMS limitations. Behavioral differences between recipient and non-recipient households (5.A) are a core finding. Consumption elasticities (6.A) and budget allocation patterns (7.B) inform predictive and recommendation modules. While not directly about mobile design (9.A), data on financial service use offers tangential insight. Savings behavior (13.A) is quantified, though debt management (13.B) is not explicitly addressed. Domains such as anomaly detection (8.A-C), user retention (11.A-B), and system evaluation (12.A-C) were considered but not selected due to the paper's focus on economic impact rather than PFMS-specific design or algorithmic performance. Overall, the paper provides foundational empirical evidence for multiple Odin modules, justifying a high relevance score for core financial behavior and expenditure modeling topics."
limitations:
  - "Cross-sectional data prevents causal inference on remittance impact."
  - "FIES does not capture remittance-financed family business investments, potentially underestimating productive use."
  - "Model assumes income fungibility, which may not hold for all households."
  - "Simulation does not model general equilibrium effects or price changes."
  - "The analysis is specific to 2018 data and may not reflect post-pandemic changes. [unacknowledged]"
remember_this:
  - "Remittance income reported by households is less than half of central bank figures."
  - "Remittance-financed demand contributed 3.5% of Philippine total output in 2018."
  - "A 10% remittance increase raises GDP by 0.34 percentage points and creates 150,000 jobs."
  - "Remittance-receiving households spend more on education and real estate than non-recipients."
  - "Manufacturing and agriculture are the top sectors benefiting from remittance-driven demand."
```
---

## Paper 73: Magno-Ballesteros et al_summarized.md

**Source File:** `Magno-Ballesteros et al_summarized.md`

```yaml
paper_id: 10.62986/dp2024.26
designation: local
title: Demographic Trends and Housing Patterns in the Philippines
authors: Ballesteros, M.; Ancheta, J.; Ramos, T.
year: 2024
venue: Philippine Institute for Development Studies Discussion Paper Series
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 9.A
  - 10.A
  - 13.A
  - 13.B
tldr: Demographic shifts, particularly a declining fertility rate and an aging population, are reshaping household formation, structure, and housing demand in the Philippines.
problem_and_motivation: Housing needs estimation often overlooks the cointegration of demography, housing markets, and wealth. Without a contextual analysis of household formation, housing policy frameworks may fail to balance the needs of the productive sector and a growing elderly population.
approach:
  - Data from the Census of Population and Housing (1980-2020) was used to analyze demographic trends.
  - The analysis primarily employed descriptive statistics to examine changes in age structure, household formation, and household types.
  - Housing conditions were assessed using habitability and space sufficiency metrics based on building materials and floor area per person.
  - A simple regression model, adapted from Mankiw and Weil (1989), was used to estimate the relationship between age structure and housing demand.
findings:
  - The Philippines is experiencing a demographic shift with a declining fertility rate (from 6.0 in 1970 to 1.9 in 2020) and an increasing share of the population aged 65 and over (from 3.01% in 1980 to 4.86% in 2020).
  - The rate of new household formation is decelerating, with younger adults (aged 24-34) showing lower headship rates, indicating a postponement of marriage and independence.
  - Nuclear households remain dominant but are declining (71% in 1990 to 61% in 2020), while extended families and one-person households are on the rise.
  - Average household size is declining (5.9 in 1970 to 4.1 in 2020), yet a considerable portion of the population still lives in larger households of 6 or more members.
  - num: 86.79% of private households resided in habitable units in 2020, up from 74.08% in 1990.
  - num: 66.28% of households had sufficient dwelling space (6 sqm per person) in 2020, an increase from 53.63% in 2010.
  - Homeownership is positively correlated with age, with a sharp rise in demand for ownership occurring between ages 30 and 53, later than in developed countries.
  - Demographic attributes that are wealth-enhancing, such as college education and lower dependency ratios, have a positive impact on housing habitability.
key_figures_tables:
  - Figure 2: Population pyramid showing a shift from a wide base to a more rounded, tree-like shape → The age structure is transitioning from a young to a more mature population.
  - Figure 13: Distribution of household types showing a decline in nuclear families and a rise in extended and one-person households → Traditional family structures are diversifying.
  - Figure 24: Housing tenure distribution showing a slight decline in homeownership for 2020 compared to 2010 → Economic shocks like the pandemic can disrupt housing tenure patterns.
  - Table 7: Space sufficiency by headship age and location, showing elderly households have the highest proportion of sufficient space → The "empty nest" phenomenon is emerging in the Philippines.
key_equations:
  - equation: D = ∑_{j=1}^{N} D_j
    explanation: Aggregate housing demand is the sum of individual demands.
  - equation: D_j = α_0 Dummy0_j + α_1 Dummy1_j + ... + α_99 Dummy99_j
    explanation: Individual housing demand is a function of age-specific parameters.
definitions:
  - term: Dependency Ratio
    definition: The number of dependents (0-14 and 65+) per 100 working-age individuals (15-64).
  - term: Habitability
    definition: A measure of housing quality based on the materials used for roof and walls and the state of repair.
  - term: Space Sufficiency
    definition: An indicator of whether a dwelling has at least 6 square meters of floor area per person.
critical_citations:
  - "[Mankiw and Weil, 1989] — Age is a best predictor of housing demand."
  - "[Borsch-Supan, 1986] — Household formation is a key determinant of aggregate housing demand."
  - "[Monkkonen, 2013] — Household formation is endogenous to the housing market."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Provides data on delayed household formation among young adults.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Links household structure and dependency ratios to potential income for housing.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Discusses housing choices (ownership vs. renting) related to life stages.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Highlights extended and multi-family households as culturally-driven coping strategies for housing costs.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: low
      justification: Does not directly address seasonal spending but discusses long-term cyclical demographic shifts.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: Provides the demographic context for housing demand, which is a major expenditure.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Directly segments housing expenditure (rent, imputed rent, ownership) as a key category.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: contextual
      justification: Implicitly shows the need to consider housing as a separate, significant expense.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Contextualizes housing demand within the broader Philippine economic landscape.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies the housing backlog and affordability gap, a key limitation for PFMS users.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: Not directly discussed.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Mentions housing data from censuses; relevant to the type of data a PFMS might use.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: Directly links homeownership to a savings goal and wealth accumulation.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: medium
      justification: Discusses amortization/ownership as a tenure type, implying housing debt.
  contribution: The paper provides crucial demographic context for understanding the financial lives of Filipino young professionals, which is the target user for Odin. It informs the design of spending forecasts by showing how household size and structure evolve over a lifetime. The analysis of housing tenure and habitability underscores the importance of housing as a primary financial goal and a significant category for budget allocation. The findings on delayed household formation and the rise of diverse family structures justify a flexible approach to both expense categorization and savings goal management within Odin. Furthermore, the paper's description of the housing backlog and the difficulties of homeownership directly validates Odin's potential to aid users in financial planning and savings.
  directly_justifies:
    - Filipino young professionals are forming households later and may have different housing needs than previous generations.
    - Housing affordability is a major challenge, making it a critical area for financial planning and savings goals.
    - The decline in average household size suggests that spending patterns for necessities may evolve, influencing budget recommendations.
    - The rise of extended and multi-family households indicates that financial support networks are common, potentially affecting user-declared preferences for allocation.
    - Income and wealth are strong predictors of housing habitability, justifying a focus on income categorization.
  limits:
    - The analysis is descriptive and does not provide causal inference between demographic trends and specific financial behaviors relevant to a PFMS.
    - The regression model is simple and not intended for forecasting individual-level spending.
    - The study focuses on housing demand and does not cover other major spending categories like food, education, or transportation.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was conducted. Domains 1 (Filipino YP), 2 (Cultural Context), and 3 (Expense Categorization) were flagged as highly relevant due to the paper's direct analysis of demographic shifts affecting the target user base and its focus on housing as a key expense. Domain 4 (Existing Systems & Gaps) was also highly relevant for its critique of current policy and its identification of the housing backlog, which represents a significant financial gap for users. Domain 13 (Savings & Debt) was considered high because the paper explicitly links housing and wealth. Domains like 6 (Forecasting) and 7 (Budget Recommendations) were rejected as low/contextual because the paper lacks algorithmic content, though its insights on housing demand indirectly inform these areas. Domain 9 (Mobile-First) and 10 (Data Privacy) were largely irrelevant, with only contextual mentions. The borderline case of housing as both an expense (Domain 3) and a savings goal (Domain 13) was resolved by assigning high relevance to both codes, recognizing that housing is a major financial burden and a primary asset-building goal. Overall, the paper is highly relevant to Odin as it provides a strong empirical foundation on the target demographic's lifecycle and financial priorities.
limitations:
  - "The analysis stops at 2020, potentially missing post-pandemic shifts in housing and household behavior."
  - "The model for housing demand is an aggregate one and may not capture the heterogeneity of individual financial decisions."
  - "The paper focuses on housing but does not explore the interplay between housing costs and other critical spending categories like health or education."
  - "The findings are based on census data which may have limitations in capturing the informal housing sector."
remember_this:
  - Fertility decline and aging population are reshaping Philippine housing and household structures.
  - Delayed household formation among young adults suggests a shift in when major financial milestones occur.
  - Extended and multi-family households are rising, likely due to economic constraints and cultural practices.
  - Homeownership in the Philippines is typically achieved at a later age (30-53), influencing long-term savings goals.
  - Housing demand is driven not just by population growth but by age-related household formation changes.
```
---

## Paper 74: Razalan_summarized.md

**Source File:** `Razalan_summarized.md`

```yaml
paper_id: 65f7a3c1-8b4a-5c2e-9d1f-6e8b7a4c2d1f
designation: local
title: Scaling the Frame of Mind: Money Attitude and Financial Well-Being of Generation Zoomers (Gen-Zs) in Rizal Province
authors: Razalan, D. C.
year: 2024
venue: Unknown
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.D
  - 3.A
  - 4.A
  - 5.A
  - 5.B
  - 12.A
tldr: Gen-Zs in Rizal Province show moderately developed financial mindsets with positive money attitudes that significantly correlate with their financial well-being across autonomy, competence, and relatedness.
problem_and_motivation: Gen-Zs have the lowest financial literacy among generations yet face unique financial hurdles including high inflation and job market uncertainty. Existing research lacks focus on money attitudes within the Philippine education sector for this demographic. Understanding these attitudes is crucial for designing targeted financial education interventions.
approach:
  - Mixed-methods design combining quantitative survey with qualitative interviews and focus groups.
  - Survey employed the Money Attitude Scale (MAS) measuring power-prestige, retention-time, distrust, and anxiety dimensions.
  - Sample comprised 364 teaching and non-teaching personnel from public/private schools and university campuses in Rizal Province.
  - Quantitative data analyzed using descriptive statistics and correlation analysis for relationship testing.
  - Qualitative data analyzed through thematic analysis to identify financial challenges and coping mechanisms.
findings:
  - Gen-Zs scored highest on power-prestige spending behavior (weighted mean 3.89) and lowest on distrust borrowing money (weighted mean 3.21).
  - num: All money attitude dimensions showed significant positive correlations with financial well-being components at p < 0.05.
  - num: The strongest correlation was between controlling finances and competence (r = 0.631).
  - num: The grand mean correlation between overall money attitudes and financial well-being was r = 0.679.
  - Financial education scores were moderate (weighted mean 3.35), with low engagement in formal programs.
  - Gen-Zs demonstrated high awareness of cybersecurity measures (4.40) but low emergency fund maintenance (3.32).
  - Qualitative findings revealed unplanned purchases and difficulty saving as primary financial challenges.
  - Respondents addressed challenges through budgeting, prioritization, and leveraging technology while avoiding scams.
  - Gen-Zs showed strong relatedness, with supportive networks positively influencing financial management.
  - Positive money attitudes holistically impacted financial well-being across all Self-Determination Theory dimensions.
key_figures_tables:
  - Table 1: Money attitudes by power-prestige dimension → Spending and saving behaviors scored "Great Extent" overall.
  - Table 2: Retention-time dimension → Financial planning scored "Great Extent"; financial education scored "Moderate Extent".
  - Table 3: Distrust dimension → Borrowing and donation behaviors scored "Moderate Extent".
  - Table 4: Anxiety dimension → Financial protection and control both scored "Great Extent".
  - Table 5-7: Financial well-being → Autonomy, competence, and relatedness all scored "Great Extent".
  - Table 8: Correlation matrix → All money attitude dimensions significantly correlated with financial well-being (p < 0.05).
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Money Attitude
    definition: An individual's beliefs, feelings, and behaviors related to money.
  - term: Money Attitude Scale (MAS)
    definition: Instrument developed by Yamauchi & Templer to assess power-prestige, retention-time, distrust, and anxiety dimensions.
  - term: Financial Well-Being
    definition: Multidimensional concept including financial stability, security, and ability to meet financial goals.
  - term: Self-Determination Theory
    definition: Psychological framework focusing on innate needs for autonomy, competence, and relatedness.
  - term: Generation Z (Gen-Z)
    definition: Individuals aged 18-26 in 2023.
critical_citations:
  - "[Yamauchi & Templer, 1982] — Foundational Money Attitude Scale development."
  - "[Lusardi & Mitchell, 2014] — Financial literacy influences financial behaviors."
  - "[Alampay et al., 2014] — Money attitude predicts financial behaviors in Filipino students."
  - "[Lown et al., 2018] — Millennials show positive credit attitudes but high debt."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Directly studies Gen-Z teaching and non-teaching personnel in Rizal Province.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Examines spending, saving, borrowing, and planning behaviors of employed Gen-Zs.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Provides detailed behavioral data on budgeting, saving, and financial planning.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Donation behaviors reflect Filipino cultural values of helping and giving.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: Mentions seasonality implicitly through spending patterns but not explicitly analyzed.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Uses MAS framework that categorizes attitudes into four dimensions.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Reviews financial education programs and systems but focuses on attitudes rather than systems.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Profiles Gen-Z behaviors across spending, saving, borrowing, and planning.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: low
      justification: Mentions initial financial literacy gaps but does not address cold-start in systems.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides evaluative data on money attitudes and financial well-being.
  contribution: "This study provides empirical evidence on the positive relationship between money attitudes and financial well-being among Filipino Gen-Zs. The findings justify Odin's need for behavioral profiling modules to capture attitude dimensions like power-prestige and anxiety. The correlation data support Odin's forecasting and recommendation modules by establishing that attitudes predict financial behaviors. The qualitative insights on budgeting and saving strategies inform Odin's user engagement and retention mechanisms. The study's emphasis on financial education gaps justifies Odin's educational content and feedback systems."
  directly_justifies:
    - "Positive money attitudes significantly correlate with financial well-being (r = 0.679)."
    - "Financial planning attitudes strongly correlate with competence in financial management (r = 0.523)."
    - "Controlling finances shows the strongest correlation with overall financial well-being (r = 0.625)."
    - "Gen-Zs struggle with unplanned purchases and saving enough money."
    - "Financial education engagement is moderate, indicating a need for accessible learning resources."
  limits:
    - "Cross-sectional design limits causal inference about money attitudes affecting financial well-being."
    - "Sample limited to education sector in Rizal Province, reducing generalizability to other sectors."
    - "Self-reported survey data may introduce social desirability bias."
    - "Quantitative correlations do not explain the mechanisms behind attitude-behavior relationships."
    - "No longitudinal tracking to assess how money attitudes evolve over time."
  mapping_rationale: "The systematic scan across all 12 functional domains identified relevance primarily in Filipino Cultural Context (2.A, 2.D), Expense Categorization (3.A), Existing Systems (4.A), Behavioral Profiling (5.A, 5.B), and System Evaluation (12.A). The paper directly addresses topics 1.A, 1.B, and 1.C with high relevance as it specifically studies Filipino Gen-Z professionals' financial behaviors. Topics 2.A and 2.D received medium/contextual relevance because donation behaviors reflect cultural practices, while seasonal spending is only implicit. Topic 3.A is medium relevance as the MAS provides a categorization framework. Topic 4.A is low because while it reviews existing financial education systems, it does not evaluate specific PFMS. Topics 5.A and 5.B are high/medium because the paper profiles behaviors but does not address cold-start. Topic 12.A is medium as the study provides evaluative methodology. Algorithmic domains (6.A, 6.B, 7.A-7.D, 8.A-8.C) and design domains (9.A, 9.B, 10.A, 10.B, 11.A, 11.B, 13.A-13.C) were rejected as the paper is not algorithmic or system-design focused. Overall, the paper provides foundational behavioral insights for Odin's profiling and evaluation modules, despite not directly addressing computational aspects."
limitations:
  - "Cross-sectional design limits causal inference. [unacknowledged]"
  - "Sample restricted to education sector in Rizal Province only. [unacknowledged]"
  - "Self-reported measures may be subject to social desirability bias."
  - "No qualitative data on how attitudes change with financial shocks."
  - "No comparison with other generational cohorts in the same context."
remember_this:
  - "Positive money attitudes strongly correlate with financial well-being among Filipino Gen-Zs."
  - "Gen-Zs score highest on power-prestige spending behavior and lowest on financial education engagement."
  - "The grand correlation between money attitudes and financial well-being is 0.679."
  - "Gen-Zs address financial challenges through budgeting, saving, and using technology."
  - "Financial protection awareness is high but emergency fund maintenance remains low."
```
---

## Paper 75: Albert et al-2024_summarized.md

**Source File:** `Albert et al-2024_summarized.md`

```yaml
paper_id: 10.62986/dp2024.10
designation: local
title: Wealth Creation for Expanding the Middle Class in the Philippines
authors: Albert, J. R. G.; Briones, R. M.; Rivera, J. P. R.
year: 2024
venue: PIDS Discussion Paper Series
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 3.A
  - 4.A
  - 4.B
  - 5.A
  - 7.B
  - 9.A
  - 9.B
  - 10.A
  - 13.A
tldr: The Philippine middle class grew to 39.8% of the population in 2021 but contracted from 43.5% in 2018 due to COVID-19, with expansion requiring multi‑pronged policies on natural resources, MSMEs, workforce, and digital governance.
problem_and_motivation: The Philippines aims for a predominantly middle‑class society by 2040, yet global headwinds and the COVID‑19 pandemic threaten this trajectory. Expanding the middle class requires new wealth creation rather than redistribution, but current policy frameworks lack integrated strategies to address structural barriers and emerging opportunities.
approach:
  - The study adopts an income‑based definition of the middle‑class as households with per capita incomes between two and twelve times the official poverty line, using data from the 2021 Family Income and Expenditure Survey (FIES) and Labor Force Survey (LFS).
  - It profiles the middle‑class across size, geographic distribution, demographics, education, labor, expenditure patterns, asset ownership, and pandemic impact, drawing on historical FIES rounds (1991‑2021).
  - The paper synthesizes literature on structural transformation, industrialization, and servicification to propose a multi‑pronged pathway for middle‑class expansion.
  - It conducts a systematic scan of four policy pillars: social justice in natural resource management, trade/investment for MSMEs, future‑ready workforce with social protection, and digital governance.
  - Policy recommendations are grounded in descriptive statistics and cross‑country evidence, with emphasis on climate adaptation, digital inclusion, and MSME internationalization.
findings:
  - num: The middle‑class share of the population grew from 28.5% in 1991 to 39.8% in 2021, representing 34.4 million Filipinos, but fell from 43.5% in 2018 due to the pandemic.
  - num: Middle‑class households have an average size of 3.6 members, compared to 5.0 for low‑income households, and 40.6% of middle‑class adults have completed college versus 14.5% for low‑income.
  - num: 60.6% of urban residents are middle‑class versus 33.8% in rural areas, with NCR, CALABARZON, and Central Luzon contributing 51.8% of all middle‑class Filipinos.
  - num: 74.7% of families with overseas Filipino workers belong to the middle‑class, and overseas remittances account for 8.5% of middle‑class total income.
  - The COVID‑19 pandemic reversed middle‑class growth, with the share declining by 3.7 percentage points between 2018 and 2021, indicating vulnerability to economic shocks.
  - Middle‑class households allocate larger expenditure shares to education (1.3%), health (3.2%), and transportation (8.8%) compared to low‑income households.
  - 81.3% of middle‑class households have access to improved water sources versus 59.4% of low‑income households, and asset ownership (e.g., mobile phones, TV, computers) is substantially higher.
  - The unemployment rate for the middle‑class is 6.7% (nearly equal to 6.9% for low‑income), with underemployment at 16.7% versus 27.3% for low‑income workers.
  - Four policy pillars are identified: promoting social justice in natural resource management and climate transition; harnessing trade/investment for MSMEs; ensuring a future‑ready workforce and social protection; and improving digital governance and public service delivery.
key_figures_tables:
  - Figure 1: Size and share of the middle‑class from 1991‑2021 → Middle‑class share peaked at 43.5% in 2018, declined to 39.8% in 2021.
  - Figure 2: Urban vs rural income class shares → Urban areas have 60.6% middle‑class; rural areas have 33.8%.
  - Figure 3: Regional population by income class → NCR has 62.0% middle‑class, CAR 50.9%, CALABARZON 49.5%.
  - Figure 8: Employment nature by income class → 79.5% of employed middle‑class have permanent jobs versus 31.4% short‑term for low‑income.
  - Table 5: Remittances by income cluster → Overseas remittances contribute 8.5% to middle‑class income, more than double domestic remittances (3.9%).
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Middle‑class (income‑based definition)"
    definition: "Households with per capita incomes between two and twelve times the official poverty line, divided into lower, middle, and upper middle clusters."
  - term: "Low‑income class"
    definition: "Households with per capita incomes below twice the official poverty line, including the poor and low‑income but not poor."
  - term: "High‑income class"
    definition: "Households with per capita incomes at least twelve times the poverty line, including upper‑income but not rich and rich."
  - term: "OFW (Overseas Filipino Worker)"
    definition: "A Filipino citizen working abroad, whose remittances significantly contribute to family income, especially among middle‑class households."
  - term: "FIES (Family Income and Expenditure Survey)"
    definition: "A nationwide Philippine survey collecting detailed household income, expenditure, and socioeconomic data, conducted every three years by PSA."
  - term: "LFS (Labor Force Survey)"
    definition: "A quarterly Philippine survey collecting employment, unemployment, and labor market indicators, merged with FIES for this study."
  - term: "MSMEs (Micro, Small, and Medium Enterprises)"
    definition: "Businesses that account for 99.5% of all Philippine firms and employ 63% of the workforce, central to inclusive growth and middle‑class expansion."
  - term: "PhilSys (Philippine Identification System)"
    definition: "A national digital identity system implemented by PSA to improve social protection targeting and financial inclusion."
  - term: "CREATE Act"
    definition: "Corporate Recovery and Tax Incentives for Enterprises Act, reducing corporate income tax and rationalizing incentives to attract FDI and support MSMEs."
  - term: "Ambisyon 2040"
    definition: "The Philippines' long‑term vision for a predominantly middle‑class society free of poverty by 2040."
critical_citations:
  - "[Easterly, 2001] — Larger middle‑class improves institutions and growth."
  - "[Banerjee & Duflo, 2008] — Middle‑class drives entrepreneurship and human capital investment in developing countries."
  - "[Albert et al., 2018a] — Establishes the income‑based middle‑class definition used in this paper."
  - "[Ravallion, 2009] — Middle‑class is vulnerable to shocks; policies needed for protection."
  - "[ADB, 2010] — Structural transformation and urbanization drive middle‑class expansion in Asia."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: "Profiles the middle‑class, which includes young professionals, with detailed socioeconomic characteristics from national surveys."
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: "Provides income ranges, expenditure patterns, asset ownership, and remittance data for middle‑class households, directly informing financial structure."
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: "Describes expenditure allocation (education, health, transport) and employment nature, offering behavioral insights for financial management."
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: "Discusses OFW remittances as a culturally embedded financial practice central to middle‑class income and mobility."
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: "Mentions climate change and disaster risks affecting spending, but does not analyze seasonal cycles directly."
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: "References consumption capacities as distinguishing middle‑class identity, but lacks detailed analysis of occasion‑based spending."
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: "Provides expenditure breakdowns by broad categories (food, housing, education, health, transport) that can inform categorization taxonomies."
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: "Reviews literature on middle‑class growth factors and policies, contextualizing the environment in which PFMS operate."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: "Identifies gaps in education, infrastructure, digital inclusion, and social protection that constrain middle‑class growth and PFMS effectiveness."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: low
      justification: "Mentions lifestyle aspirations and consumption patterns but does not develop behavioral profiles for PFMS."
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: contextual
      justification: "Discusses income and expenditure patterns that could inform budget recommendations, but does not address recommendation algorithms."
    - code: 9.A
      name: Mobile‑First Design Principles and Rationale
      relevance: medium
      justification: "Highlights digital divide and mobile penetration, underscoring the need for mobile‑first approaches to reach middle‑class users."
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: "Mentions digital literacy and access, but no UX design specifics."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: "Discusses cybersecurity, data privacy frameworks, and PhilSys, which are directly relevant to user trust and data protection in PFMS."
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: "Covers asset ownership, financial inclusion, and digital financial services that can support savings goal features."
  contribution: "This paper profiles the Philippine middle‑class with granular income, expenditure, and employment data that can inform Odin's user segmentation and baseline financial assumptions. Its identification of OFW remittances, educational attainment, and asset ownership provides foundational statistics for modeling user financial behavior. The policy discussion on digital governance, MSME support, and social protection offers justification for Odin's design principles around mobile‑first access and financial resilience. The multi‑pronged framework for middle‑class expansion can contextualize Odin's role within broader national development goals, particularly in promoting savings, debt management, and financial inclusion."
  directly_justifies:
    - "The middle‑class in the Philippines is predominantly urban and more educated, with higher formal employment rates, informing user persona design."
    - "Overseas remittances account for 8.5% of middle‑class income, supporting integration of remittance tracking in PFMS."
    - "COVID‑19 reduced the middle‑class share by 3.7 percentage points, justifying anomaly detection for income shocks."
    - "Digital financial services are growing rapidly, with the BSP exploring CBDCs, supporting Odin's digital‑first architecture."
    - "Only 46% of urban middle‑class households own a computer, reinforcing the need for mobile‑first design."
  limits:
    - "The income‑based definition excludes multidimensional factors like education and occupation, limiting behavioral profile granularity."
    - "The analysis is descriptive and does not evaluate causal relationships or algorithm performance, limiting direct design guidance."
    - "Data is from 2021, pre‑dating recent digital finance trends (e.g., GCash, Maya) that may have shifted middle‑class financial behavior."
    - "The paper focuses on macro‑level policy and does not address individual‑level financial decision‑making or PFMS usability."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was conducted. The paper was flagged as highly relevant to 'Filipino Cultural Context' (2.A) due to its detailed treatment of OFW remittances as a culturally embedded practice, and to 'Filipino Young Professionals as a Demographic' (1.A, 1.B, 1.C) given its comprehensive socioeconomic profile of the middle‑class, which overlaps with the target user group. Medium relevance was assigned to 'Expense Categorization' (3.A) because the paper provides expenditure breakdowns by category, and to 'Existing Systems & Gaps' (4.A, 4.B) as it reviews policy and infrastructure gaps. 'Mobile‑First Design' (9.A) was rated medium due to the digital divide discussion, and 'Data Privacy' (10.A) medium for cybersecurity and PhilSys coverage. 'Savings Goal Management' (13.A) was rated medium due to financial inclusion and asset ownership data. Low/contextual relevance was assigned to 'Seasonal Spending' (2.B, 2.D) because the paper mentions climate shocks but not cyclical patterns, 'Behavioral Profiling' (5.A) due to lack of psychological classifications, and 'Budget Recommendation' (7.B) as no algorithmic recommendation is discussed. Domains like 'Forecasting' (6.A, 6.B), 'Anomaly Detection' (8.A‑C), 'System Evaluation' (12.A‑C), and 'Debt Management' (13.B) were rejected as the paper does not address predictive modeling, detection algorithms, evaluation metrics, or debt‑specific mechanisms. Overall, the paper provides foundational socioeconomic data and policy context that inform user personas, feature justification, and design principles, but lacks algorithmic or technical content directly applicable to Odin's modules."
limitations:
  - "The income‑based definition does not account for economies of scale or cost‑of‑living variations across regions. [unacknowledged]"
  - "Data from 2021 may not reflect post‑pandemic digital finance adoption and shifting middle‑class behavior."
  - "The paper does not evaluate the effectiveness of proposed policies, limiting causal evidence for design decisions."
  - "Remittance and asset data are self‑reported and subject to measurement error. [unacknowledged]"
  - "The analysis aggregates all middle‑class subgroups, obscuring heterogeneity relevant to PFMS segmentation."
remember_this:
  - "The middle‑class share fell from 43.5% in 2018 to 39.8% in 2021 due to COVID‑19."
  - "60.6% of urban residents are middle‑class versus only 33.8% in rural areas."
  - "Overseas remittances account for 8.5% of middle‑class total income."
  - "Middle‑class households spend 1.3% of income on education and 3.2% on health."
  - "Only 46% of urban middle‑class households own a computer, underscoring mobile‑first design.
```
---

## Paper 76: Aguilar et al_summarized.md

**Source File:** `Aguilar et al_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: local
title: Cash Management Practices and the Financial Performance of Micro-Enterprises
authors: Aguilar, T. S.; Chavez, M. M.; Rayos, C. M. D.; Remoquin, K. J. A.; Melo, M. C. F.
year: 2024
venue: American International Journal of Business Management
odin_topics:
  - "1.A"
  - "1.B"
  - "1.C"
  - "2.D"
  - "3.A"
  - "3.B"
  - "4.A"
  - "4.B"
  - "5.A"
  - "5.B"
  - "5.C"
  - "7.A"
  - "7.C"
  - "13.A"
  - "13.B"
  - "13.C"
tldr: A survey of 163 micro-enterprises in Baco, Oriental Mindoro, shows that budgeting and cash flow management practices have a strong positive correlation with financial performance.
problem_and_motivation: Micro-enterprises face challenges in managing financial resources, leading to operational disruptions and business closures. The study aims to understand how cash management practices affect financial performance to inform better financial planning and support for these enterprises.
approach:
  - A quantitative, descriptive-correlational research design was used with 163 micro-enterprise owners as respondents in Baco, Oriental Mindoro.
  - Data was collected using a researcher-made questionnaire employing a 4-point Likert scale for both independent (budgeting, cash flow management) and dependent (sales growth, profitability, liquidity) variables.
  - The reliability of the questionnaire was established using Cronbach's Alpha on a test-retest sample of 10 non-respondents.
  - Spearman's rho correlation was used to determine the relationship between cash management practices and financial performance due to non-normality in the data distributions.
  - The study's theoretical framework is grounded in the Baumol Model and Miller-Orr Cash Management Model.
findings:
  - num: Cash management practices are at a moderate extent (mean = 3.04 for budgeting; mean = 2.97 for operating cash flow).
  - num: Financial performance is at a moderate extent, with liquidity showing the highest overall mean of 3.01.
  - num: Budgeting is strongly correlated with sales growth (rho = .506), profitability (rho = .536), and liquidity (rho = .526).
  - num: Cash flow management shows a stronger correlation with sales growth (rho = .648), profitability (rho = .558), and liquidity (rho = .589).
  - The null hypothesis is rejected, confirming a significant relationship between cash management practices and financial performance.
  - Micro-enterprises struggle with consistent budget adherence, regular cash flow monitoring, and financial planning.
  - Enterprises experience moderate sales growth and profitability but face challenges in converting assets to cash quickly.
  - The study recommends financial literacy programs and training to improve cash management skills.
key_figures_tables:
  - "Table 10: Spearman's rho correlations between cash management practices and financial performance indicators → All variables show significant positive correlations, strongest between cash flow management and sales growth (rho=0.648)."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: Cash Management Practices
    definition: Planning, controlling, and accounting for cash transactions and balances, including budgeting and cash flow management.
  - term: Financial Performance
    definition: An evaluation of a company's standing in terms of sales growth, profitability, and liquidity.
  - term: Micro-enterprises
    definition: Businesses with Php 3,000,000 or less in assets and one to nine employees, as categorized by the Philippine Department of Trade and Industry (DTI).
critical_citations:
  - "[Kasim & Antwi, 2015] — Establishes link between non-budgeting and business failure."
  - "[Onyango, 2023] — Highlights role of financial literacy in cash management performance."
relevance:
  topics:
    - code: "1.A"
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Focuses on micro-enterprise owners in the Philippines, providing demographic context.
    - code: "1.B"
      name: Financial Structure of Filipino Young Professionals
      relevance: low
      justification: Discusses financial structure and capital limitations of micro-enterprises.
    - code: "1.C"
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Provides behavioral insights into budgeting and financial planning practices.
    - code: "2.D"
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Discusses challenges in managing daily operations and cash flow.
    - code: "3.A"
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Mentions budgeting as a key practice, which relates to categorizing expenses.
    - code: "3.B"
      name: Expense Category Design Considerations
      relevance: medium
      justification: Discusses budgeting for unexpected expenses and non-business costs.
    - code: "4.A"
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Reviews literature on cash management practices in micro-enterprises.
    - code: "4.B"
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly addresses gaps in budgeting and cash flow management in micro-enterprises.
    - code: "5.A"
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Profiles owners' practices regarding budgeting and cash flow monitoring.
    - code: "5.B"
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: Implies challenges in starting or maintaining proper financial practices.
    - code: "5.C"
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Categorizes performance using sales growth, profitability, and liquidity.
    - code: "7.A"
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Core focus is on budgeting as a primary cash management practice.
    - code: "7.C"
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: low
      justification: Mentions budgeting to monitor performance and adjust spending.
    - code: "13.A"
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Highlights the importance of setting aside money for unexpected expenses.
    - code: "13.B"
      name: Debt Management in PFMS
      relevance: low
      justification: Mentions that poor cash management can lead to accumulated debts.
    - code: "13.C"
      name: End‑of‑Period Surplus as a Savings Input
      relevance: high
      justification: Directly discusses maintaining extra cash after expenses as a key indicator.
  contribution: This paper provides direct empirical evidence for Odin's budgeting and cash flow management modules. Its findings justify the need for features that encourage budget adherence and cash flow monitoring. The strong correlations identified in the study validate the importance of Odin's core functionality for improving financial performance. Furthermore, the study's recommendations support the development of educational components and training programs within Odin.
  directly_justifies:
    - "There is a significant relationship between budgeting practices and financial performance in Filipino micro-enterprises."
    - "Cash flow management practices have a significant relationship with profitability, sales growth, and liquidity."
    - "Micro-enterprises in Baco, Oriental Mindoro have a moderate extent of cash management practices."
  limits:
    - "The study is limited to micro-enterprises in Baco, Oriental Mindoro, which limits generalizability."
    - "The research relies on self-reported data, which may introduce bias."
    - "The study does not explore the qualitative factors behind the low adoption of some cash management practices. [unacknowledged]"
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. Domains 3.A, 3.B, 4.B, 5.A, 7.A, 7.C, 13.A, and 13.C were flagged as relevant. A borderline case is topic 7.C, where the paper's discussion on budgeting to monitor performance is a constrained application, not a formal optimization problem, thus classified as low. Topics under domains like 6.A (Forecasting) and 8.A (Anomaly Detection) were considered and rejected due to a lack of methodology on prediction or anomaly detection. The overall relevance of the paper to Odin is in providing empirical justification for core expense categorization and budget management features, highlighting real-world gaps.
limitations:
  - "The study is confined to micro-enterprises in a single municipality, limiting broader applicability."
  - "Cross-sectional design limits the ability to infer causality."
  - "Potential social desirability bias in self-reported survey responses."
  - "The study did not employ qualitative methods to understand the context of the quantitative findings. [unacknowledged]"
remember_this:
  - "Micro-enterprises' cash management practices are moderate, with budgeting scoring 3.04 and liquidity scoring 3.01."
  - "Cash flow management has a strong correlation (rho=0.648) with sales growth."
  - "Budgeting is strongly correlated with profitability (rho=0.536) and liquidity (rho=0.526)."
  - "Effective cash management is crucial for financial stability in Filipino enterprises."
  - "Significant gaps exist in budget adherence and cash flow monitoring practices."
```
---

## Paper 77: Pinca et al_summarized.md

**Source File:** `Pinca et al_summarized.md`

```yaml
paper_id: 10.34104/cjbis.024.0910105
designation: local
title: Financial Literacy Practices on the Investment Decisions of Accounting Professionals in Makati City
authors: Pinca, J. M.; NG, J. G.; Lacerona, R. B.; Minorca, J. C.; Rodriguez, N. R.; Ramos, J. I.
year: 2024
venue: Canadian Journal of Business and Information Studies
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.C
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 7.A
  - 7.B
  - 7.C
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 12.A
  - 13.A
tldr: Financial literacy practices, particularly saving/investing, budgeting, and debt management, show very strong positive correlations with investment decisions among accounting professionals in Makati City.
problem_and_motivation: While financial literacy is known to influence investment decisions, limited research explores the correlation between specific literacy practices and choices. This creates a gap in understanding how budgeting, saving, and debt management directly affect investment behavior among professionals.
approach:
  - A quantitative, cross-sectional survey was administered to 80 accounting professionals in Makati City.
  - A self-made questionnaire measured financial literacy practices (budgeting, saving/investing, debt management) and investment decision parameters (risk tolerance, goals, cost-effectiveness, asset allocation).
  - Data were analyzed using Pearson's Product Moment Correlation Coefficient to determine relationships.
  - Instrument reliability was verified with Cronbach's alpha scores of .876 and .815, deemed 'Good'.
findings:
  - num: A very strong and significant correlation exists between budgeting and investment decisions (r=0.924, p=0.001).
  - num: A very strong and significant correlation exists between saving/investing and investment decisions (r=0.970, p<0.001).
  - num: A very strong and significant correlation exists between debt management and investment decisions (r=0.919, p=0.001).
  - Respondents rated "I understand the risks associated with different investment options due to my financial education" as the highest factor for risk tolerance (mean 3.98).
  - Respondents rated "I refrain from acquiring new debts unless absolutely necessary" as the highest debt management practice (mean 3.95).
key_figures_tables:
  - Table 10: Budgeting vs. Investment Decisions correlation → Very strong positive correlation (r=0.924, p=0.001).
  - Table 11: Saving/Investing vs. Investment Decisions correlation → Very strong positive correlation (r=0.970, p<0.001).
  - Table 12: Debt Management vs. Investment Decisions correlation → Very strong positive correlation (r=0.919, p=0.001).
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Financial Literacy
    definition: Understanding financial terms and concepts related to investing, handling money, and making informed financial decisions.
  - term: Pearson-r
    definition: A measure of the linear correlation between two variables, ranging from -1 to 1.
critical_citations:
  - "[Kumari, 2020] — Defines financial literacy as expertise for money handling."
  - "[Lusardi and Mitchell, 2014] — Links education level to financial literacy."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: The study directly focuses on accounting professionals in Makati City, a key subset of Filipino young professionals.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: It analyzes their budgeting, saving, and debt management practices, which define their financial structure.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: The core of the study is the financial behavior (practices) and its influence on investment decisions.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: It examines financial practices within a specific Philippine context (Makati City).
    - code: 2.C
      name: User-Declared Financial Preferences
      relevance: medium
      justification: The survey captures self-declared preferences related to budgeting, saving, and risk tolerance.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Budgeting practices, a key focus, are a fundamental part of expense categorization.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: low
      justification: It mentions budgeting at a high level but not specific design considerations for categories.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Does not review specific PFMS systems but informs the behavioral principles they should support.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: contextual
      justification: Highlights the general need for financial literacy tools but doesn't critique existing systems.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: The findings on different practices (saving, budgeting, debt) can inform the development of behavioral profiles.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: low
      justification: Does not address profile dynamics or cold-start problems but provides static data on professionals.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Directly investigates budgeting as a key financial literacy practice and its influence on decisions.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: contextual
      justification: Provides evidence that budgeting is critical, justifying its inclusion in budget recommendations.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: low
      justification: Does not address optimization, but the strong correlation with debt management highlights constraints.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Not directly addressed, but user trust is indirectly implied through professional behavior.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: Not a focus of the study.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: contextual
      justification: The positive correlation suggests engagement with these practices, but engagement with apps is not studied.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: low
      justification: No direct relevance to retention mechanisms.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: contextual
      justification: Uses survey methodology but not an evaluation of a PFMS.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: Saving and investing is a core practice studied, with a very strong correlation to investment decisions.
  contribution: "This paper provides empirical evidence from a Philippine context that specific financial literacy practices (budgeting, saving/investing, and debt management) are strongly correlated with investment decisions. For Odin, this justifies the inclusion of modules that track and reinforce these specific behaviors, such as budget setting, saving goals, and debt management. The high correlations suggest that Odin's recommendation engine should prioritize these areas to influence user behavior effectively. The findings on risk tolerance and diversification can inform Odin's risk assessment features. The study's focus on user-perceived importance of avoiding new debt highlights a key area for Odin's engagement and notification strategies."
  directly_justifies:
    - "Budgeting practices are strongly correlated with investment decisions, justifying a dedicated budgeting module in Odin."
    - "Saving and investing are very strongly correlated with investment decisions, supporting Odin's savings goal management features."
    - "Debt management is strongly correlated with investment decisions, warranting a focus on debt reduction in Odin's recommendations."
  limits:
    - "Convenience sampling of only 80 respondents from Makati City limits generalizability."
    - "The study uses self-reported data, which may be subject to response bias."
  mapping_rationale: "A systematic scan of all 12 functional domains was conducted. The paper was flagged as highly relevant to domains related to Filipino Cultural Context (1.A, 1.B, 1.C), Expense Categorization (3.A), Behavioral Profiling (5.A), and Budgeting (7.A, 13.A) because it directly measures specific financial practices of Filipino professionals. It was deemed medium for topics like User-Declared Preferences (2.C) and Behavioral Profiles (5.A) due to its survey methodology. It has low relevance to technical topics like Optimization (7.C) or System Evaluation (12.A), as it does not address them. Borderline cases included its relevance to Engagement (11.A), which was considered contextual as it measures behavior but not engagement with a digital system. The overall relevance is high for informing Odin's user-facing behavioral modules and low for its algorithmic infrastructure."
limitations:
  - "The sample is limited to accounting professionals in Makati City, which may not represent the general Filipino young professional population."
  - "The study relies on self-reported perceptions and behaviors, which may not perfectly align with actual financial actions."
  - "The cross-sectional design does not establish causality, only correlation between practices and decisions."
  - "The study does not explore the influence of digital financial tools or investment platforms, which is an unacknowledged gap."
remember_this:
  - "Financial literacy strongly correlates with investment decisions among professionals."
  - "Saving and investing have a very strong relationship with investment choices."
  - "Budgeting is a critical practice linked to better investment outcomes."
  - "Avoiding new debt is the most highly rated debt management behavior."
  - "The correlation between saving/investing and decisions is very strong at r=0.970."
```
---

## Paper 78: Arena et al_summarized.md

**Source File:** `Arena et al_summarized.md`

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
---

## Paper 79: Gerzon et al_summarized.md

**Source File:** `Gerzon et al_summarized.md`

```yaml
paper_id: 10.52006/main.v6i2.752
designation: local
title: Financial Literacy and Financial Well-Being of Nurses of a First-Class Province in the Philippines
authors: Gerzon, R. A.; Lopena, G. L.
year: 2023
venue: Philippine Social Science Journal
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 10.A
  - 11.A
tldr: Financial literacy correlates strongly with financial well-being among Filipino public health nurses, with higher monthly income linked to greater financial literacy.
problem_and_motivation: Filipino nurses face low pay, financial stress, and poor work performance, yet their financial literacy and well-being are underexplored. Understanding these factors is critical for designing targeted financial programs to improve their economic resilience and job outcomes.
approach:
  - Descriptive-correlational design with 178 randomly stratified public health nurses from a first-class Philippine province.
  - Researcher-made 52-item questionnaire measuring financial literacy (knowledge and behavior) and financial well-being (discipline, security, resilience) on a four-point Likert scale.
  - Instrument validity (Lawshe's CVR=0.91) and reliability (Cronbach's alpha: financial literacy=0.945, financial well-being=0.904) were established.
  - Data collected via web-based and printed surveys with informed consent and ethical clearance.
  - Pearson, Point Biserial, Rank Biserial, and Spearman Rank correlations used for analysis.
findings:
  - num: Overall financial literacy was high (M=3.22, SD=0.39), with financial knowledge (M=3.22, SD=0.43) and behavior (M=3.21, SD=0.40) both rated high.
  - num: Financial well-being was rated as great (M=3.03, SD=0.46), with discipline (M=3.26, SD=0.52) very great, security (M=2.96, SD=0.55) great, and resilience (M=2.88, SD=0.55) great.
  - num: Monthly income had a significant positive correlation with financial literacy (r=0.223, p=0.003), while age, sex, civil status, and dependents did not.
  - num: No demographic factor significantly correlated with financial well-being.
  - num: Financial literacy and financial well-being showed a strong positive correlation (rs=0.660, p=0.000), supporting the conceptual model.
  - Higher-income nurses demonstrated very high financial knowledge and behavior.
  - Nurses with 2 or more dependents had very high financial knowledge.
key_figures_tables:
  - Table 1: Financial literacy levels by demographics → Older, higher-income nurses with more dependents have higher knowledge.
  - Table 2: Financial well-being levels by demographics → Discipline is very great across all groups.
  - Table 3: Correlation between demographics and financial literacy → Only monthly income is significantly related.
  - Table 4: Correlation between demographics and financial well-being → No significant relationships found.
  - Table 5: Correlation between financial literacy and well-being → Strong positive relationship.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Financial Literacy
    definition: Combination of financial knowledge and financial behaviors essential for sound monetary decisions.
  - term: Financial Well-Being
    definition: State of financial discipline, security, and resilience enabling present and future financial satisfaction.
critical_citations:
  - "[Joo, 1998] — Conceptual model for personal financial wellness."
  - "[Parcia & Estimo, 2017] — Financial literacy, behavior, stress, and wellness among employees."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Directly studies Filipino public health nurses as a professional demographic.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Provides income, dependency, and financial behavior data for this demographic.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Assesses financial knowledge and behaviors of nurses.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: Highlights financial practices like savings and debt management in Philippine context.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Mentions Data Privacy Act compliance but no system design implications.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: Implies engagement through financial literacy programs but no UX/engagement study.
  contribution: This paper provides baseline evidence that financial literacy is a significant predictor of financial well-being among Filipino public health nurses. It directly informs Odin's behavioral profiling module (5.A, 5.B) by demonstrating demographic and income-related variations in financial literacy and well-being. The strong correlation supports Odin's design assumption that improving financial literacy via personalized recommendations can enhance user financial health. The findings also justify the inclusion of income and dependency status as critical features for user profiling and budget recommendation systems. However, the paper does not address algorithmic or system-specific aspects.
  directly_justifies:
    - "Financial literacy significantly predicts financial well-being among Filipino nurses."
    - "Monthly income is positively correlated with financial literacy level."
    - "Demographic factors like age, sex, and civil status do not significantly affect financial well-being."
    - "Higher financial literacy is associated with better financial discipline, security, and resilience."
  limits:
    - "Sample restricted to nurses in one province, limiting generalizability."
    - "Self-reported measures may introduce response bias."
    - "Cross-sectional design prevents causal inference."
    - "Demographic variables limited to age, sex, civil status, income, and dependents."
  mapping_rationale: Systematic scan of all 12 functional domains and their associated topic codes was performed. Domains flagged as relevant: Filipino Cultural Context (2.A, 2.B, 2.C, 2.D) for the cultural and demographic setting; Behavioral Profiling (5.A, 5.B, 5.C) for financial literacy and well-being measures; Existing Systems (4.A, 4.B) considered but rejected as no system comparison is made; Budget Recommendation (7.A–7.D) rejected as no algorithmic or budget allocation content; Anomaly Detection (8.A–8.C) rejected; Mobile-First Design (9.A, 9.B) rejected; Data Privacy (10.A) considered low due to methodological mention only; User Retention (11.A, 11.B) considered low due to no engagement study; System Evaluation (12.A–12.C) rejected; Savings/Debt (13.A–13.C) considered contextual due to discussion of savings and debt behaviors. Overall relevance is high for demographic and behavioral profiling domains, contextual for culturally specific practices, and low for privacy/engagement. The paper provides foundational evidence for Odin's behavioral and demographic modules.
limitations:
  - "Sample size limits generalizability beyond one province."
  - "Self-reported questionnaire may be subject to social desirability bias."
  - "No qualitative data to explain quantitative findings."
remember_this:
  - "Financial literacy strongly predicts financial well-being among Filipino nurses."
  - "Monthly income is the only demographic factor linked to financial literacy."
  - "Nurses reported high financial literacy and great financial well-being overall."
  - "The correlation between literacy and well-being is r=0.660, indicating a strong relationship."
  - "Higher-income nurses demonstrate very high financial knowledge and behavior."
```
---

## Paper 80: Bernardo & Seva_summarized.md

**Source File:** `Bernardo & Seva_summarized.md`

```yaml
paper_id: "10.3390/informatics10010032"
designation: "local"
title: "Affective Design Analysis of Explainable Artificial Intelligence (XAI): A User-Centric Perspective"
authors: "Bernardo, E.; Seva, R."
year: 2023
venue: "Informatics"
odin_topics:
  - "10.B"
  - "11.A"
  - "11.B"
tldr: "End-user trust in AI is calibrated through both cognitive and affective routes, with XAI design attributes significantly influencing trust via these routes, moderated by user anxiety and incidental emotions."
problem_and_motivation: "Current XAI research focuses on developers, neglecting end-user perspectives, which limits trust and adoption. This study addresses the gap by investigating how end-users calibrate trust from XAI through affective design, aiming to fill the lack of end-user understanding."
approach:
  - "Conducted a pre-study survey with 312 AI users to identify important XAI design attributes (explanation form, communication style, supplementary information)."
  - "Designed a between-subject experiment with 202 participants using an image classification AI testbed with 64 design configurations (2 levels each of three design attributes, plus AI reliability, learning capability, brand, and time)."
  - "Measured emotions using XAI emotion set (XES), trust, perceived usefulness, and reliance, with moderators including AI anxiety, incidental emotions, trust disposition, and experience."
  - "Analyzed data using structural equation modeling (SEM) to test mediation, direct, and moderation effects on trust calibration."
findings:
  - "Affective route (emotions) mediates trust calibration alongside cognitive route; interestingly surprised and trusting emotions positively affect trust, while fearfully dismayed negatively affects it."
  - "Example-based explanations increase interestingly surprised and trusting emotions, while human-like communication reduces fearfully dismayed and anxiously suspicious emotions."
  - "Supplementary information reduces fearfully dismayed emotions; logic-robotic communication style increases fearfully dismayed and anxiously suspicious emotions."
  - "AI anxiety, incidental emotions, AI reliability, and user experience moderate the trust calibration process, with high anxiety and low reliability dampening positive effects."
  - "num: Perceived trust significantly predicts reliance (β=0.439, p<0.001), and affective mediation paths showed significant indirect effects (e.g., trusting emotion mediation: β=0.171, p=0.001)."
key_figures_tables:
  - "Table 1: Experimental design configurations with 6 variables → 64 design combinations tested."
  - "Table 8: Mediation effect analysis showing significant affective and cognitive paths → Affective mediation is confirmed."
  - "Table 9: Direct effects of design elements on emotions and perceived usefulness → Example-based explanation boosts positive emotions."
  - "Table 13: Summary of affect and cognitive change per design element → Clear mapping for design choices."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "XAI"
    definition: "Explainable Artificial Intelligence, techniques that provide human-level explanations of AI decisions."
  - term: "Affective design"
    definition: "Design approach that elicits emotions from users to trigger specific behavior."
  - term: "Trust calibration"
    definition: "Process of adjusting trust in a system based on experience and information."
critical_citations:
  - "[Lee & See, 2004] — Foundational framework for trust calibration routes."
  - "[Norman, 2004] — Three levels of processing for affective design."
  - "[Bernardo & Seva, 2022] — XAI emotion set used in this study."
relevance:
  topics:
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "high"
      justification: "Directly addresses trust calibration from XAI, which is critical for user trust in AI-driven PFMS."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "medium"
      justification: "Trust influences engagement; findings on trust calibration can inform engagement strategies."
    - code: "11.B"
      name: "Retention Mechanisms and Engagement Design"
      relevance: "medium"
      justification: "Trust is a key factor in retention; design attributes affecting trust can be leveraged for retention."
  contribution: "This paper provides a user-centric framework for trust calibration in XAI, demonstrating that both cognitive and affective routes are viable. It identifies specific design attributes (explanation form, communication style, supplementary information) that can be directly applied to Odin's explanation interfaces for budget recommendations. The moderation effects of user anxiety and incidental emotions suggest that Odin should adapt its explanations based on user state. These insights can guide Odin's UX design to foster trust, thereby improving user adoption and retention."
  directly_justifies:
    - "XAI should be designed to elicit positive emotions (e.g., interestingly surprised) to enhance trust."
    - "Example-based explanations increase trust and positive emotions, suitable for financial advice."
    - "Human-like communication style reduces negative emotions and increases perceived usefulness."
    - "User anxiety and incidental emotions moderate trust calibration; Odin should monitor user affect."
  limits:
    - "Study uses image recognition AI, not financial domain; generalizability to PFMS needs verification."
    - "Experiment is short-term (2 days); long-term trust dynamics not captured."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper's primary focus on user trust calibration from explainable AI directly maps to Topic 10.B (User Trust), assigned high relevance because it provides empirical evidence on how XAI design influences trust via affective and cognitive routes. Topics 11.A (Engagement) and 11.B (Retention) were flagged as medium relevance because trust is a foundational driver of engagement and retention in PFMS; the paper's insights on design attributes can inform engagement strategies. Other domains such as expense categorization, forecasting, anomaly detection, savings, and debt management were considered but rejected as the paper does not address these specific financial functions. The paper's findings on affective design and user moderators are contextually relevant to mobile-first design (9.A) but not explicitly; thus, 9.A was not selected. Overall, the paper offers strong guidance for building trust in AI-driven financial management systems."
limitations:
  - "The study uses image recognition AI, which differs from financial recommendation AI; domain-specific validity is untested. [unacknowledged]"
  - "The sample may not fully represent the Filipino young professional demographic targeted by Odin. [unacknowledged]"
  - "Long-term trust calibration and retention effects are not investigated, though authors acknowledge this limitation."
remember_this:
  - "Trust in XAI is calibrated via both cognitive and affective routes."
  - "Example-based explanations and human-like communication boost positive emotions and trust."
  - "User anxiety and incidental emotions moderate the effectiveness of XAI design."
  - "Affective design of explanations can directly influence user reliance on AI systems."
  - "Explanations should be tailored to user state for optimal trust calibration."
```
---

## Paper 81: Yuan & Hernandez_summarized.md

**Source File:** `Yuan & Hernandez_summarized.md`

```yaml
paper_id: "10.1109/ACCESS.2023.3338705"
designation: "local" # National University, Philippines
title: "User Cold Start Problem in Recommendation Systems: A Systematic Review"
authors: "Yuan, H.; Hernandez, A. A."
year: 2023
venue: "IEEE Access"
odin_topics:
  - "5.A"
  - "5.B"
  - "5.C"
  - "12.A"
  - "12.B"
tldr: "A systematic review of literature from 2016 to 2023 categorizes approaches to the user cold start problem into data-driven and method-driven techniques."
problem_and_motivation: "Accurate recommendations for new users are hindered by a lack of historical data. This limits the utility and user experience of recommender systems. Existing systematic reviews are outdated or do not distinguish between user and item cold start problems."
approach:
  - "A systematic literature review was conducted following established guidelines for selecting and analyzing scientific papers."
  - "A search of IEEE, ACM, and Web of Science databases yielded 45 relevant papers published from January 2016 to April 2023."
  - "The study categorizes solution approaches into two main groups: data-driven technologies and approach-driven technologies."
  - "Data-driven techniques utilize additional user information like cross-domain data, social network data, and demographic data."
  - "Approach-driven techniques are further subdivided into five categories: meta-learning, deep learning, matrix factorization, improved collaborative filtering, and improved content-based approaches."
  - "The paper also analyzes the primary evaluation criteria used in the reviewed studies."
  - "Key future research directions are outlined, including collecting additional information and multi-task learning."
findings:
  - "num: 45 research papers from 35 venues were selected for in-depth analysis."
  - "num: The quantity of relevant literature peaked in 2020 with 11 papers."
  - "The user cold start problem has been a growing research area from 2016 to 2023."
  - "IEEE Access and ACM Transactions on Information Systems are the most common venues, each with 4 papers."
  - "Method-driven strategies are categorized into five main approaches: meta-learning, deep learning, matrix factorization, improved collaborative filtering, and improved content-based."
  - "Data-driven strategies primarily use cross-domain data, social network data, and user demographic data to build better user profiles."
  - "Commonly used evaluation metrics include Rating Prediction (RMSE, MAE), Classification Accuracy (AUC, Recall), and Ranking Metrics (NDCG@K, Hit@K)."
  - "Ranking Metrics, especially NDCG, are increasingly popular for evaluating user cold start solutions."
  - "Recommendation methods for films, music, and books are the most researched areas due to the availability of public datasets."
  - "Deep learning and graph neural networks are increasingly applied to solve the user cold start problem."
key_figures_tables:
  - "Figure 1: Flow diagram of the systematic literature review process → The seven steps for selecting and analyzing papers."
  - "Figure 2: The paper selection process → From 1480 initial papers to 45 final papers selected for the review."
  - "Figure 3: Number of papers per year → Shows a peak in publications on user cold start in 2020."
  - "Figure 7: Classification of user cold start recommendation strategies → Diagrams the data-driven and method-driven categories."
  - "Table 8: Classification of approaches for alleviating the user cold start problem → Provides a high-level summary of both main categories and their sub-approaches."
key_equations:
  - equation: "Y_s = W Y_t"
    explanation: "A general formulation for similarity-based models using a similarity matrix W."
definitions:
  - term: "User Cold Start Problem"
    definition: "The challenge of making accurate recommendations for new users due to a lack of historical interaction data."
  - term: "Item Cold Start Problem"
    definition: "The challenge of recommending newly added items for which no user rating or interaction history exists."
  - term: "Data-Driven Techniques"
    definition: "Approaches that solve the cold start problem by utilizing additional user or item information from various sources."
  - term: "Approach-Driven Techniques"
    definition: "Approaches that solve the cold start problem by proposing new algorithms or modifying existing ones."
  - term: "Meta-Learning"
    definition: "A machine learning approach that enables models to quickly adapt to new tasks with limited data, useful for new users."
  - term: "NDCG@K"
    definition: "Normalized Discounted Cumulative Gain, a ranking metric used to evaluate the quality of a top-K recommendation list."
critical_citations:
  - "[Panda & Ray, 2022] — A recent systematic review on cold-start mitigation strategies."
  - "[Son, 2016] — A comparative review of three approaches for the new user cold-start problem."
  - "[Abdullah et al., 2021] — A survey focused on eliciting auxiliary information for cold-start users."
  - "[Camacho & Alves-Souza, 2018] — A systematic review on using social network data to alleviate cold starts."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "contextual"
      justification: "Discusses user profiling as part of building user models to address cold starts."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "high"
      justification: "The paper is a systematic review directly addressing the user cold-start problem, which is the core of this topic."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "Reviews classification approaches like clustering and meta-learning, which are relevant for profile classification."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Dedicates a section to reviewing evaluation criteria (e.g., NDCG, RMSE) used in the literature."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "The review analyzes algorithmic solutions and their performance as measured by common metrics."
  contribution: "This systematic review provides Odin with a comprehensive taxonomy of user cold start solutions, categorizing them into data-driven and approach-driven methods. The review's analysis of evaluation metrics informs the design of robust testing protocols for Odin's behavioral profiling and recommendation modules. The categorization of deep learning, meta-learning, and other algorithmic approaches guides the selection of appropriate techniques for cold-start user modeling. The paper's insights into future research directions, like multi-task learning, can inspire advanced features for Odin. Overall, it serves as a foundational reference for Odin's approach to new user onboarding and initial budget recommendations."
  directly_justifies:
    - "The user cold start problem occurs when a new user cannot be appropriately suggested due to a lack of detailed preference information."
    - "Solving the user cold start problem is essential for the large-scale utility of recommender systems."
    - "Approaches to solve the user cold start problem can be categorized as data-driven or method-driven strategies."
  limits:
    - "The review is limited to a systematic analysis of existing literature and does not include an experimental validation or comparison of the reviewed methods."
    - "The study focuses on the user cold start problem and does not analyze solutions for item cold starts, which may have different optimal strategies."
  mapping_rationale: "In the systematic scan, the domains of 'Behavioral Profiling & Classification' and 'System Evaluation' were flagged as relevant. Under the 'Behavioral Profiling & Classification' domain, topic 5.B (Profile Dynamics and the Cold-Start Problem) was assigned high relevance because the paper is a comprehensive review directly focused on this issue. Topic 5.A (Financial Behavioral Profiles) was rated contextual as user profiling is a component of many reviewed solutions, but the paper does not specifically address financial profiles. Topic 5.C (Classification Approaches) was assigned medium relevance, as the review discusses various classification and learning methods used to build profiles. Under the 'System Evaluation' domain, topics 12.A (Evaluation Frameworks) and 12.B (Evaluation of Algorithmic Modules) were rated medium, as the paper provides a systematic analysis of evaluation metrics used in the literature. All other domains were considered and rejected. The 'Expense Categorization' domain was rejected because the paper does not discuss categorization frameworks. 'Spending Forecasting' and 'Budget Recommendation' were rejected as the paper focuses on user identification, not financial prediction. 'Anomaly Detection' was not relevant as the paper does not discuss identifying outliers in spending. In summary, while not directly about finance, the paper's structured review of cold start solutions and evaluation metrics is highly relevant for Odin's initial user modeling and module benchmarking."
limitations:
  - "No experimental validation was performed to compare the effectiveness of the different methods reviewed. [unacknowledged]"
  - "The authors acknowledge that the review is limited to a systematic literature review of 45 articles, which, while comprehensive, may not include all relevant studies."
  - "The paper notes that it does not address the item cold start problem, which is a distinct but related issue in recommender systems."
remember_this:
  - "User cold start solutions are categorized into data-driven and method-driven strategies."
  - "Data-driven approaches use cross-domain, social, and demographic user data."
  - "Method-driven approaches include meta-learning, deep learning, and improved collaborative filtering."
  - "num: 45 papers from 2016-2023 were systematically reviewed on this topic."
  - "Ranking metrics like NDCG are the most prevalent for evaluating cold start performance."
```
---

## Paper 82: Mendoza et al_summarized.md

**Source File:** `Mendoza et al_summarized.md`

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
---

## Paper 83: Donato et al_summarized.md

**Source File:** `Donato et al_summarized.md`

```yaml
paper_id: 10.55927/fjss.v2i3.4572
designation: local
title: The Concept of Utang Na Loob Among Filipino Working Millenials
authors: Donato, A. M.; Panotan, G. V.; Castro, J. M.; Gavino, R. M.
year: 2023
venue: Formosa Journal of Social Sciences
odin_topics:
  - "1.A"
  - "1.C"
  - "2.A"
  - "5.A"
tldr: Filipino working millennials perceive utang na loob as a self-imposed moral obligation rooted in reciprocity and shared identity, extending beyond family to include workplace relationships and evolving toward experiential and meaningful expressions of gratitude.
problem_and_motivation: There is a lack of empirical, up-to-date research on the cultural value of utang na loob, with most studies dating to the 1900s and early 2000s. This gap limits understanding of how a core Filipino value manifests and evolves among the contemporary generation of working millennials. The study aims to explore their perceptions and experiences to provide a modern contextualization of this distinct cultural construct.
approach:
  - A basic qualitative design was employed, involving semi-structured interviews with 30 employed Filipino millennials residing in Tuguegarao City, Cagayan.
  - Participants aged 26-41 were recruited via purposive sampling using social media, and data were collected through one-on-one in-person or online interviews.
  - Thematic analysis was utilized to analyze the interview data, identifying recurring themes and sub-themes from the participants' responses.
findings:
  - num: 30 employed Filipino millennials aged 26-41 from Tuguegarao City participated in the study.
  - Participants perceive utang na loob as an inner, self-imposed obligation to reciprocate kindness, rooted in the Filipino values of pakikiramdam and pakikipagkapwa.
  - The experience of utang na loob is expressed primarily through financial support for family, which generates both a strong sense of fulfillment and increased work motivation, but also feelings of burden and personal sacrifice.
  - Millennials manifest utang na loob not just through financial support but also through creating quality experiences, acts of service, and loyalty in workplace relationships.
key_figures_tables:
  - "Table 1: Summary of Informants' Demographic Profile → Shows diverse professions and age distribution among the 30 participants."
  - "Figure 1: Themes on the Concept of Utang Na Loob → Visualizes the core themes of obligation, kagandahang loob, love for family, fulfillment, and loyalty."
  - "Figure 2: Themes on the Manifestations of Utang Na Loob → Depicts how the value is expressed in familial and workplace trends."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Utang na loob"
    definition: "A core Filipino value meaning a 'debt of goodwill,' involving reciprocity and moral obligation when one person assists another."
  - term: "Kapwa"
    definition: "A Filipino concept of 'shared self' or 'shared identity,' linking an individual's inner self with others."
  - term: "Kagandahang loob"
    definition: "Genuine concern and readiness to assist others, embodying inner goodness or generosity."
  - term: "Kusang loob"
    definition: "Voluntary willingness or inner motivation to act, free from external compulsion or expectation of reward."
  - term: "Pakikiramdam"
    definition: "A Filipino cultural concept of empathy and sensitivity, sensing others' emotions to adjust behavior for social harmony."
  - term: "Pakikipagkapwa"
    definition: "A Filipino value emphasizing a sense of shared identity and treating others as equals."
critical_citations:
  - "[Hollnsteiner, 1961] — Foundational definition of utang na loob as debt of gratitude."
  - "[Pe-Pua & Marcelino, 2000] — Contextualizes utang na loob within Sikolohiyang Pilipino."
  - "[Reyes, 2015] — Explains utang na loob as central to Filipino virtue ethics."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "high"
      justification: "The study focuses directly on the perceptions and experiences of Filipino working millennials, a core user group for Odin."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Provides insights into how a core cultural value (utang na loob) directly influences the financial behavior of providing for family."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "high"
      justification: "Directly examines the Filipino value of utang na loob and its role in shaping financial obligations, a key cultural practice."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Offers a behavioral profile of Filipino working millennials driven by utang na loob, influencing their financial priorities and motivations."
  contribution: "This paper directly justifies the need for Odin to incorporate culturally specific behavioral drivers like utang na loob within its user profiling (domain 5.A). It provides empirical grounding for understanding the financial 'love for family' motivation (domain 1.C) that drives Filipino young professionals' savings and spending habits. The findings support designing financial management features that help users balance family obligations with personal financial goals (domain 13.A). Furthermore, the study highlights the potential for financial stress and 'blind loyalty' (domain 4.B), which justifies the need for Odin's budgeting and anomaly detection features to safeguard user well-being."
  directly_justifies:
    - "Utang na loob is a self-imposed obligation to reciprocate support, often expressed through financial support for family."
    - "Millennials derive fulfillment from providing for family, which can increase work motivation."
    - "Strong family obligations can lead to personal financial burden and compromise of well-being."
  limits:
    - "The study is geographically limited to Tuguegarao City, Cagayan, and may not represent the broader Filipino millennial population."
    - "The qualitative sample size (n=30) is small, limiting the generalizability of the findings."
  mapping_rationale: "A systematic scan of all 12 functional domains was performed. The paper was flagged as highly relevant to the 'Filipino Cultural Context' domain due to its direct examination of utang na loob, a core cultural value. It also strongly informs 'Expense Categorization' (domain 3) and 'Behavioral Profiling' (domain 5) by providing a cultural lens for understanding the motivations behind financial behavior. Specifically, topic codes 1.A (Filipino Young Professionals), 1.C (Financial Behavior), and 2.A (Culturally Specific Financial Practices) were deemed high relevance. Code 5.A (Financial Behavioral Profiles) was rated medium because the paper describes a profile driven by cultural obligation but does not propose a classification approach. Topics related to forecasting (6), algorithms (7, 8), system design (9), and evaluation (12) were rejected as the paper is a qualitative cultural study without technical content. The study's findings on financial burden and family obligation provide critical cultural context for designing Odin's features, such as savings goals (13.A) and anomaly detection (8.A), to be sensitive to these cultural drivers."
limitations:
  - "The study uses a qualitative design with a small, region-specific sample, limiting generalizability."
  - "Relies on self-reported data from interviews, which may be subject to social desirability bias."
  - "Does not explore the potential negative effects of utang na loob on mental health or personal financial security in depth. [unacknowledged]"
  - "Lacks a comparative analysis with other Filipino generational cohorts or demographic groups. [unacknowledged]"
  - "The study's focus on 'working millennials' does not capture the perspectives of unemployed or younger cohorts. [unacknowledged]"
remember_this:
  - "Filipino working millennials view utang na loob as a self-imposed moral obligation."
  - "Providing for family due to utang na loob leads to both fulfillment and significant personal sacrifice."
  - "The value is evolving, with millennials valuing experiential and quality-time reciprocation over purely material support."
  - "Family obligations can create financial strain, potentially requiring support from siblings and peers."
  - "The concept of utang na loob significantly shapes the financial behavior and priorities of Filipino young professionals."
```
---

## Paper 84: Mencias-Tabernilla_summarized.md

**Source File:** `Mencias-Tabernilla_summarized.md`

```yaml
paper_id: 8c5e7b12-31b4-5b9f-9d11-2c1a6e7f8d9a
designation: local
title: THE STORY BEHIND "LONDON" (LOAN DITO, LOAN DOON): EXPLORING TEACHERS' EXPENDITURE PATTERNS AND DEBT PROFILE
authors: Mencias-Tabernilla, M. C.
year: 2023
venue: Universal Journal of Educational Research
odin_topics:
  - 1.B
  - 1.C
  - 2.A
  - 2.D
  - 4.A
  - 4.B
  - 5.A
  - 13.A
  - 13.B
tldr: Filipino public school teachers' high regard for education and health drives debt acquisition, with over half of income used for loan payments, necessitating better financial management.
problem_and_motivation: Filipino public school teachers face a persistent issue of indebtedness, with combined debts reaching P319 billion, exacerbated by low take-home pay and easy access to loans. Understanding their expenditure patterns, debt profiles, and underlying reasons is crucial for developing interventions to improve their financial well-being.
approach:
  - Descriptive correlational design with 276 regular-permanent public-school teachers in Aklan.
  - Researcher-made instrument covering socio-demographics, expenditure patterns, and debt profiles.
  - Data analyzed using SPSS version 26 with descriptive statistics, t-tests, and ANOVA.
  - Focus Group Discussions informed instrument development and provided qualitative insights.
  - Data collection occurred in 2018-2019 with updates in 2021-2022 for salary and price changes.
findings:
  - num: Teachers' mean take-home pay was Php16,184.54, only more than half of their gross income.
  - num: Mean monthly family expenditure was Php22,265.00, while mean savings were only Php1,200.00, with 57.25% having no savings.
  - num: Mean cumulative debt from banks was Php156,117.76, and from GSIS was Php125,617.15.
  - num: Almost one-half of teachers' income was used to pay debts through automatic deductions and personal transactions.
  - Household size, family income, and spouse's income were positively correlated with higher expenditure.
  - Age, civil status, household size, number of children, position, length of service, and income significantly affected cumulative debt.
  - Education and professional growth, illness and death, and house construction were top reasons for acquiring debt.
  - Sound financial management and salary increase were perceived as the top ways to avoid debt.
key_figures_tables:
  - Table 1: Average monthly family expenditure pattern → Food is the largest expense at 25.26% of total expenditure.
  - Table 2: Total monthly expenditure and savings → 57.25% of teachers have no savings at all.
  - Table 3: Cumulative debt profile → Bank loans have the highest mean outstanding balance (Php156,117.76).
  - Table 4: Difference in expenditure by demographics → Household size and family income have highly significant effects.
  - Table 5: Difference in cumulative debt by demographics → Age, household size, and length of service significantly affect debt.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: APDS
    definition: Automatic Payroll Deduction System, a mechanism for loan payments directly from salaries.
  - term: GSIS
    definition: Government Service Insurance System, a social insurance institution for government employees.
  - term: NTHP
    definition: Net Take Home Pay, the salary received after all deductions.
  - term: OFW
    definition: Overseas Filipino Worker, a Filipino employed outside the country.
  - term: PERA
    definition: Personnel Economic Relief Allowance, a monthly allowance for government employees.
  - term: PAG-IBIG
    definition: A government agency providing savings and loan programs for Filipino workers.
critical_citations:
  - "[Ferrer, 2017] — Documents the long-standing debt issue among public school teachers."
  - "[Reysio-Cruz, 2019] — Reports P319 billion in teacher debts as per DepEd data."
relevance:
  topics:
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Provides specific income and debt data for teachers, a key professional demographic.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly studies expenditure patterns, debt profiles, and reasons for borrowing among teachers.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Highlights "utang" (debt) as a common practice and the cultural value of education driving borrowing.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Mentions celebrations and occasions as reasons for spending and debt, but not a primary focus.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Describes the ecosystem of lenders, including GSIS, banks, cooperatives, and loan sharks.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: contextual
      justification: Implicitly critiques APDS and loan sharks, but does not evaluate PFMS specifically.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Identifies behavioral triggers for debt (e.g., education, health) and links to TRA/TPB.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: Notes low savings rates, but no discussion of savings goal management systems.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: Directly addresses debt profiles, causes, and perceived solutions, relevant to debt management features.
  contribution: This paper provides empirical evidence on the spending and debt patterns of Filipino public school teachers, a key user group for Odin. It identifies high debt levels and low savings, justifying the need for robust budgeting and debt management features. The study's findings on the cultural drivers of debt, such as education and family obligations, inform Odin's culturally-sensitive design. The data on income and expenditure gaps supports the need for accurate forecasting and budget recommendation modules. The paper's focus on teachers, a financially vulnerable but tech-savvy demographic, validates Odin's target user focus.
  directly_justifies:
    - Teachers allocate a significant portion of income to debt repayment, highlighting the need for debt management tools in Odin.
    - High regard for education and health are primary drivers of debt, which should be considered in Odin's category design.
    - Many teachers have no savings, underscoring the necessity of features that promote savings goals.
    - The prevalence of multiple loan sources (GSIS, banks, cooperatives) suggests Odin should support debt consolidation or tracking.
    - Expenditure increases with household size and family income, a pattern Odin's forecasting module should account for.
  limits:
    - Sample limited to teachers in Aklan province, which may not be nationally representative.
    - Data collection started pre-pandemic with updates, potentially introducing recall bias.
    - Does not evaluate any specific PFMS algorithm, only provides user-level data.
  mapping_rationale: A systematic scan across all 12 functional domains and associated topic codes was conducted. The paper was flagged as relevant to the domains of Filipino Cultural Context (codes 2.A, 2.D), Existing Systems & Gaps (4.A, 4.B), Behavioral Profiling (5.A), and Savings & Debt Management (13.A, 13.B). The topic codes 1.B and 1.C were selected as high/medium relevance because the paper provides detailed financial structure and behavior data for teachers. Codes 2.A and 2.D were selected for cultural practices and spending cycles. Codes 4.A and 4.B were selected for describing the lending landscape. Code 13.B was rated high for its direct debt analysis. Codes related to algorithms (6.A, 7.D, 8.B), mobile design (9.A, 9.B), privacy (10.A, 10.B), and evaluation (12.A-C) were rejected as the paper is a descriptive study of user behavior, not a computational or UX design paper. The paper's primary contribution is empirical financial data on a key Filipino professional group, making it contextually relevant to Odin's user understanding.
limitations:
  - Sample restricted to one division in the Philippines, limiting generalizability. [unacknowledged]
  - Reliance on self-reported expenditure and debt data, prone to social desirability bias.
  - Cross-sectional design prevents causal inferences about debt accumulation.
  - Does not address the role of financial literacy programs or interventions.
remember_this:
  - Mean teacher take-home pay was Php16,184.54, with 57.25% having no savings.
  - The top reasons for debt were education and health, reflecting Filipino cultural values.
  - Sound financial management and salary increase were seen as top solutions to avoid debt.
  - Household size and family income were significant predictors of higher expenditure.
  - num: 37.00% of teachers received a gross income between Php22,000 and Php25,999.
```
---

## Paper 85: Cortez_summarized.md

**Source File:** `Cortez_summarized.md`

```yaml
paper_id: "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
designation: "local"
title: "Personal Financial Management Practices Among Selected Personnel of the Bureau of the Treasury – Central Office"
authors: "Cortez, D. D."
year: 2023
venue: "Guild of Educators in TESOL International Research"
odin_topics:
  - "1.A"
  - "1.B"
  - "1.C"
  - "2.A"
  - "2.D"
  - "3.A"
  - "3.B"
  - "4.A"
  - "5.A"
  - "7.A"
  - "13.A"
  - "13.B"
tldr: "Selected personnel of the Bureau of the Treasury demonstrate prudent financial management, with high agreement on financial planning, money management, and income protection, but only moderate engagement in investments."
problem_and_motivation: "Financial mismanagement among personnel threatens organizational success. This study addresses the gap in research on personal financial practices within the Bureau of the Treasury, providing a baseline assessment."
approach:
  - "A descriptive research design was employed to gather data from 183 personnel across 35 divisions of the Bureau of the Treasury."
  - "Simple random probability sampling was used to select the study respondents."
  - "A researcher-made questionnaire, validated with a Cronbach's Alpha of 0.896, was the primary instrument."
  - "Data collection involved survey administration over three weeks, supplemented by informal interviews."
  - "Analysis included descriptive statistics (frequency, percentage, weighted mean, ranking) and inferential statistics (T-test and one-way ANOVA)."
findings:
  - "num: 37.7% of respondents are aged 26 to 35 years old."
  - "num: 60.1% of respondents are female."
  - "num: 63.9% of respondents are single."
  - "num: 78.7% hold a bachelor's degree."
  - "num: 78.1% are rank-and-file employees."
  - "num: 86.9% are permanent employees."
  - "num: 53.0% have been in the agency for 5 years or less."
  - "num: 38.8% have a monthly compensation of P15,001-P30,000."
  - "Financial planning had the highest overall weighted mean of 4.26 among financial management aspects."
  - "Significant differences were found in financial practices based on age, civil status, employment status, and monthly compensation."
key_figures_tables:
  - "Table 10: Financial Planning practices → Highest rating for setting short- and long-term goals (WM=4.39)."
  - "Table 11: Money Management practices → Highest rating for saving to avoid borrowing (WM=4.47)."
  - "Table 12: Income and Asset Protection practices → Highest rating for considering future uncertainties (WM=4.30)."
  - "Table 13: Investments practices → Highest rating for purchasing government securities (WM=3.56)."
  - "Table 14: Summary of PFM practices → Financial Planning ranked first (WM=4.26), Investments last (WM=2.91)."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "PFMS"
    definition: "Personal Financial Management System"
  - term: "Bureau of the Treasury"
    definition: "National government agency responsible for managing government finances."
critical_citations:
  - "[Brounen et al., 2016] — Urges proactive personal financial planning."
  - "[Kassim et al., 2019] — Links saving ability to reduced financial stress."
  - "[Adeoye, 2019] — Finds compensation management does not affect motivation in Nigerian insurance sector."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "medium"
      justification: "The study's sample of government personnel provides a proxy for understanding the financial practices of a specific Filipino workforce segment."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "high"
      justification: "Provides detailed data on income, savings, and spending behaviors of Filipino government employees."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Directly measures and reports on financial planning, money management, and investment behaviors."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "medium"
      justification: "Highlights practices like saving to avoid borrowing and dependency on social media for financial influence, reflecting cultural financial norms."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "contextual"
      justification: "Mentions day-to-day cost of living as a primary concern, providing a backdrop for understanding spending patterns."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "low"
      justification: "The study groups financial practices into broad categories (planning, management, protection, investments) which can inform categorization."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      relevance: "low"
      justification: "The identified practices (e.g., buying necessities over wants) can be used to inform the design of spending categories."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "low"
      justification: "Provides context on current financial behaviors which any PFMS would need to address or improve."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "The study's findings on saving and spending habits (e.g., saving to avoid borrowing) are inputs for creating behavioral profiles."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "low"
      justification: "The reported practice of following a budget plan (WM=4.10) confirms budgeting as a key user activity."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "low"
      justification: "The emphasis on saving for emergencies and to avoid borrowing aligns with savings goal management features."
    - code: "13.B"
      name: "Debt Management in PFMS"
      relevance: "medium"
      justification: "The strong aversion to credit and borrowing directly informs the need for debt management features."
  contribution: "This study provides a baseline understanding of the financial management practices of Filipino government personnel. It identifies specific behaviors within financial planning, money management, income protection, and investments. These findings can inform the design of Odin's modules by highlighting user priorities, such as avoiding debt and planning for uncertainties, and revealing gaps like limited investment knowledge."
  directly_justifies:
    - "Financial planning, especially goal-setting, is a highly prioritized activity."
    - "Saving is a primary financial strategy used to avoid borrowing from others."
    - "Government employees are cautious about using credit and incurring debt."
    - "There is a gap in knowledge and engagement with investment products beyond basic securities."
    - "Demographic factors like age and civil status influence financial practices."
  limits:
    - "The study is limited to a single government agency (Bureau of the Treasury) in the Philippines. [unacknowledged]"
    - "The findings are based on self-reported data, which may be subject to social desirability bias. [unacknowledged]"
    - "The study does not employ a longitudinal design to understand how these practices evolve over time. [unacknowledged]"
    - "The research does not compare these practices to those of other demographics, limiting generalizability. [unacknowledged]"
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was conducted. The domains of 'Filipino Cultural Context', 'Expense Categorization', 'Existing Systems & Gaps', 'Behavioral Profiling', 'Budget Recommendation', and 'Savings & Debt Management' were flagged as relevant. Topic codes 1.B, 1.C, 2.A, and 5.A were assigned a 'high' relevance because the paper directly provides data on the financial behaviors and profile of Filipino workers. Codes 1.A, 2.D, 3.A, 3.B, 4.A, 7.A, 13.A, and 13.B were assigned 'medium' or 'low' relevance as they offer contextual or supporting insights. Domains related to algorithms (6.A/B, 7.C/D, 8.A/B/C, 12.B/C), mobile design (9.A/B), privacy (10.A/B), engagement (11.A/B), and system evaluation (12.A) were considered but rejected as the paper is a descriptive behavioral study, not an algorithmic or design-oriented paper. The paper's overall relevance to Odin lies in its provision of foundational behavioral data that can inform the user profile, budgeting strategies, and savings/debt management modules."
limitations:
  - "The study is limited to a single government agency, which restricts the generalizability of findings to all Filipino young professionals."
  - "The reliance on self-reported survey data may introduce bias and inaccuracies in measuring financial behaviors."
  - "The cross-sectional design prevents analysis of financial management dynamics and changes over time."
  - "The study does not explore the effectiveness of specific PFMS tools or interventions."
remember_this:
  - "Financial planning has the highest engagement among government personnel."
  - "Saving to avoid borrowing is a core money management strategy."
  - "Investment knowledge and participation are areas of significant weakness."
  - "Single and younger personnel show less engagement in financial management."
  - "The study provides a behavioral baseline for designing a Filipino PFMS."
```
---

## Paper 86: Polinar et al_summarized.md

**Source File:** `Polinar et al_summarized.md`

```yaml
paper_id: "e3f4c9a2-1b5c-4d8e-9f0a-7c6b5d4e3f2a"
designation: "local"
title: "Knowledge and Practice of Personal Finance of Non-Teaching Staff in a Private University in Cebu City"
authors: "Rico, M. E.; Polinar, M. A. N.; Celada, J. A."
year: 2023
venue: "International Journal of Multidisciplinary: Applied Business and Education Research"
odin_topics:
  - "1.A"
  - "1.B"
  - "1.C"
  - "2.A"
  - "3.A"
  - "3.B"
  - "4.A"
  - "4.B"
  - "5.A"
  - "5.B"
  - "13.A"
  - "13.B"
tldr: "Non-teaching staff in a Cebu private university demonstrate moderate personal finance knowledge and practice, with weak emergency fund and investment behaviors showing no correlation with knowledge."
problem_and_motivation: "Filipinos demonstrate low financial literacy, with only 25% understanding basic concepts, and the pandemic has worsened financial instability. Limited research exists on the personal finance practices of non-teaching staff in Philippine universities, leaving a gap in understanding their financial behaviors and needs."
approach:
  - "Descriptive-correlational design with 50 non-teaching staff respondents selected via simple random sampling from a private Cebu university."
  - "Adopted survey questionnaire measuring knowledge and practice across budgeting, saving/spending, emergency funds, debt, insurance, and investment using a 4-point Likert scale."
  - "Data collected through printed and Google Forms questionnaires during the COVID-19 pandemic, with ethical protocols followed."
  - "Statistical analysis employed weighted means for descriptive measures and Pearson correlation for relationships between knowledge and practice."
  - "Respondents were permanent staff with at least one year of service, ensuring relevant work tenure."
findings:
  - "num: Respondents demonstrated moderate overall personal finance knowledge (grand mean: 3.10) and practice (grand mean: 2.71)."
  - "Budgeting and saving/spending knowledge were rated 'Highly Knowledgeable' (means: 3.29, 3.32), while investment knowledge was lowest (2.56)."
  - "Emergency fund and investment practice were 'Less Practiced' (means: 2.42, 2.20), indicating weak behavioral execution."
  - "Significant positive correlations existed between knowledge and practice for budgeting (r=0.939), saving/spending (r=0.839), insurance (r=0.969), and investment (r=0.973)."
  - "No significant relationship was found between knowledge and practice for emergency funds (r=0.875, p=0.052) and debt management (r=0.806, p=0.053)."
  - "The researchers developed an action plan called 'Solidifying Personal Finance in a Teknoy Way' to address weak areas."
  - "Recommendations include seminars, workshops, and using prior outputs like 'Every Centavo Counts' to enhance financial literacy."
  - "Potential future research directions include qualitative exploration and studying other variables like money mindset and retirement planning."
key_figures_tables:
  - "Table 3: Knowledge means for six indicators → Emergency fund and investment knowledge are moderate, investment knowledge is lowest."
  - "Table 4: Practice means for six indicators → Emergency fund and investment practice are poor, indicating weak execution."
  - "Table 5: Pearson correlations for all six variables → Strong correlations for budgeting, saving/spending, insurance, and investment; no correlation for emergency fund and debt management."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "BSP"
    definition: "Bangko Sentral ng Pilipinas, the central bank of the Philippines."
  - term: "MSMEs"
    definition: "Micro, Small, and Medium Enterprises."
  - term: "PFMS"
    definition: "Personal Finance Management System."
  - term: "COVID-19"
    definition: "Coronavirus disease 2019, a global pandemic."
critical_citations:
  - "[Polinar et al., 2022] — Found significant correlation between financial knowledge and practice among public school teachers."
  - "[Bangko Sentral ng Pilipinas, 2021] — Revealed low financial literacy rates and poor emergency saving habits in the Philippines."
  - "[Guliman, 2015] — Showed low financial knowledge among MSME owners, supporting the need for targeted interventions."
  - "[Mouna & Anis, 2016] — Established that financial literacy significantly influences investment decisions."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "medium"
      justification: "Studies non-teaching staff, a subset of Filipino professionals, providing demographic context."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "medium"
      justification: "Examines budgeting, saving, and spending behaviors relevant to financial structure."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "medium"
      justification: "Assesses actual financial practices, offering insights into behavioral patterns."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "medium"
      justification: "Discusses Filipino cultural practices like 'paluwagan' and spending-before-saving mentality."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "low"
      justification: "Mentions budgeting and spending categories but does not propose a categorization framework."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      relevance: "low"
      justification: "Briefly touches on expense categories without deep design analysis."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "References BSP surveys and national financial literacy levels, providing macro-context."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Identifies gaps in financial knowledge and practice among non-teaching staff."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Examines knowledge-practice relationships, informing behavioral profiling."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "low"
      justification: "Provides baseline knowledge and practice data useful for initial user profiling."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "medium"
      justification: "Addresses saving and spending practices, directly relevant to savings goal management."
    - code: "13.B"
      name: "Debt Management in PFMS"
      relevance: "medium"
      justification: "Includes debt management as a key variable, with findings on knowledge-practice correlation."
  contribution: "This paper provides empirical baseline data on Filipino non-teaching staff's financial knowledge and practice, directly informing Odin's user profiling and behavioral assessment modules. The finding that knowledge and practice are correlated for budgeting and saving supports Odin's educational feature design, while the weak correlation for emergency funds and investment highlights areas needing behavioral nudges and simplified goal-setting interfaces. The identified gaps in emergency savings and investment practices justify Odin's focus on automated savings features and investment literacy tools. The action plan framework suggests concrete design directions for engagement and retention mechanisms."
  directly_justifies:
    - "Knowledge of budgeting and saving is significantly correlated with practice among Filipino non-teaching staff."
    - "Emergency fund and investment knowledge do not translate to practice, requiring targeted behavioral interventions."
    - "Financial literacy programs should address both knowledge and behavioral execution for effective PFMS design."
    - "Non-teaching staff exhibit weak investment practices, justifying simplified investment guidance in PFMS."
  limits:
    - "Small sample size (n=50) from a single private university limits generalizability to all Filipino professionals."
    - "Cross-sectional design prevents causal inference between knowledge and practice."
    - "Focus on non-teaching staff excludes teaching faculty and other professional groups."
    - "Self-reported data may introduce social desirability bias in financial responses."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant to the Filipino Cultural Context domain (codes 2.A, 2.B, 2.C, 2.D) due to its focus on Filipino spending practices and cultural financial behaviors. It also maps to Expense Categorization (3.A, 3.B) through its budgeting and spending indicators, and to Existing Systems & Gaps (4.A, 4.B) by referencing national financial literacy surveys. The Behavioral Profiling domain (5.A, 5.B) is relevant given the knowledge-practice correlation analysis. Savings & Debt Management (13.A, 13.B) is directly addressed through emergency fund and debt indicators. The paper was considered for Forecasting (6.A, 6.B) and Anomaly Detection (8.A, 8.B) but rejected as it does not involve predictive algorithms. Similarly, Budget Recommendation (7.A-D) and Mobile-First Design (9.A-B) were rejected due to no discussion of budget optimization or UX. Data Privacy (10.A-B) and Retention (11.A-B) were not addressed. Overall relevance is medium, providing foundational behavioral insights for Odin's profiling and educational modules, though not directly contributing to algorithmic design."
limitations:
  - "Small sample size from a single university limits generalizability [unacknowledged]."
  - "Cross-sectional design prevents establishing causation between knowledge and practice."
  - "Self-reported data may be subject to social desirability bias."
  - "No qualitative exploration of reasons behind weak emergency fund and investment practices [unacknowledged]."
remember_this:
  - "Knowledge and practice are correlated for budgeting, saving, insurance, and investment."
  - "Emergency fund and investment knowledge do not predict practice among respondents."
  - "Investment practice was lowest, with a mean score of 2.20 out of 4."
  - "Moderate financial literacy requires targeted behavioral interventions, not just education."
  - "Action plans should address the gap between knowledge and execution for emergency funds."
```
---

## Paper 87: Co & Centeno_summarized.md

**Source File:** `Co & Centeno_summarized.md`

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
---

## Paper 88: Bangko Sentral ng Pilipinas-2021_summarized.md

**Source File:** `Bangko Sentral ng Pilipinas-2021_summarized.md`

```yaml
paper_id: "f47ac10b-58cc-4372-a567-0e02b2c3d479"
designation: "local"
title: "Consumer Finance Survey Report 2021"
authors: "Bangko Sentral ng Pilipinas"
year: 2021 # This is a special exception as this is a core paper
venue: "Unknown"
odin_topics:
  - "1.C"
  - "2.A"
  - "2.C"
  - "2.D"
  - "3.A"
  - "3.B"
  - "4.A"
  - "4.B"
  - "5.A"
  - "9.A"
tldr: "BSP's 2021 Consumer Finance Survey provides comprehensive data on Filipino household income, expenditure, assets, liabilities, and financial behaviors, highlighting pandemic impacts and financial inclusion gaps."
problem_and_motivation: "The survey addresses the lack of comprehensive household-level data on wealth, indebtedness, and financial behavior in the Philippines, which is essential for evidence-based policy formulation. Existing surveys like FIES and APIS have limited coverage of assets and liabilities. The CFS fills this gap by providing detailed information on household financial conditions."
approach:
  - "Nationwide survey of 18,000 households using two-stage cluster sampling."
  - "Face-to-face interviews with computer-assisted personal interviewing (CAPI) conducted from March to December 2022."
  - "Data collected on demographics, income, expenditure, non-financial and financial assets, liabilities, and financial attitudes."
  - "Weighted estimates with coefficients of variation used for precision."
  - "Survey instrument based on US Federal Reserve's Survey of Consumer Finances."
findings:
  - "num: Average annual household income was ₱189,842, with 91.5% receiving wage income."
  - "num: Food at home accounted for 55.4% of total expenditure."
  - "num: 69.9% of households owned their residence, while 35.3% had a deposit account."
  - "num: Only 29.3% of households had any outstanding debt."
  - "The pandemic led to increased ownership of financial assets, including e-money accounts."
  - "Government assistance was a major income source for 75.5% of households with other income."
  - "Most households had low emergency savings, with 42.9% having no emergency fund."
key_figures_tables:
  - "Figure 1: Distribution of PEUs by income sources → wage income dominant (91.5%)."
  - "Figure 2: Average share to total expenditure → food at home largest (55.4%)."
  - "Figure 3: Distribution by ownership of asset categories → appliances most common (96.6%)."
  - "Table 1: Response rate by region → overall 90.1%, highest on record."
  - "Figure 7: Types of household assets and liabilities → comprehensive coverage."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "PEU"
    definition: "Primary Economic Unit, the financial unit of the household consisting of the economically dominant member and financially interdependent members."
  - term: "EDM"
    definition: "Economically Dominant Member, the household member who contributes the most to household finances."
  - term: "PCOICOP"
    definition: "Philippine Classification of Individual Consumption According to Purpose, used for expenditure categorization."
critical_citations:
  - "[BSP, 2021] — foundational survey."
relevance:
  topics:
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Provides detailed data on income, spending, saving, and debt behaviors of households, including young adults."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "medium"
      justification: "Documents informal savings like paluwagan and reliance on remittances and government aid."
    - code: "2.C"
      name: "User-Declared Financial Preferences"
      relevance: "high"
      justification: "Includes survey on risk tolerance, time preference, and attitudes toward credit and saving."
    - code: "2.D"
      name: "Filipino Spending Cycles and Occasions"
      relevance: "medium"
      justification: "Reports spending on special occasions, gifts, and celebrations as part of miscellaneous expenses."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "high"
      justification: "Uses PCOICOP to categorize expenditures, providing a framework for Odin's expense categorization."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      relevance: "high"
      justification: "Presents shares of different expenditure types, informing design of budget categories."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "high"
      justification: "Surveys ownership of deposit accounts, e-money, insurance, and investments, mapping the financial landscape."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Identifies barriers to account ownership (e.g., lack of money, distance), highlighting gaps in financial inclusion."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Collects data on financial attitudes, risk preferences, and saving behavior, enabling behavioral profiling."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "contextual"
      justification: "Reports high mobile phone ownership and digital financial service adoption, relevant for mobile-first design context."
  contribution: "The survey's expenditure categorization framework directly informs Odin's expense tracking module. The detailed breakdown of income sources and spending patterns supports budget recommendation algorithms. The findings on financial attitudes and risk preferences can be used to build behavioral profiles for personalized financial advice. Data on asset and liability ownership provide baselines for savings and debt management features. The identified gaps in financial inclusion highlight areas where Odin can improve accessibility."
  directly_justifies:
    - "Households spend 55.4% of income on food at home, justifying the need for robust food expense tracking."
    - "Only 35.3% have deposit accounts, indicating a large unbanked population that Odin can target."
    - "Most households have minimal emergency savings, supporting the need for automated savings features."
    - "Government assistance is a major income source during crises, suggesting Odin should account for irregular income."
  limits:
    - "Survey data is self-reported and subject to recall bias and under-reporting of sensitive items."
    - "The survey covers all households, not specifically young professionals, limiting direct applicability to that demographic."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. High relevance was assigned to topics related to financial behavior (1.C), user preferences (2.C), expense categorization (3.A, 3.B), existing financial systems and gaps (4.A, 4.B), and behavioral profiling (5.A) because the survey directly provides empirical data on these areas. Medium relevance was given to culturally specific practices (2.A) and spending occasions (2.D) as they are documented but not central. Contextual relevance was assigned to mobile-first design (9.A) as the survey notes high mobile ownership but does not address design principles. Topics related to predictive modeling, budget recommendation, anomaly detection, and evaluation were rejected as the survey is descriptive and not algorithmic. The overall relevance is high for informing Odin's design with baseline data on Filipino household finances."
limitations:
  - "Self-reported data may contain inaccuracies and under-reporting."
  - "The survey does not explicitly focus on young professionals, limiting direct applicability."
  - "Non-sampling errors such as recall bias and reluctance to disclose true values may affect estimates."
  - "The data reflect pandemic conditions, which may not be representative of normal times."
remember_this:
  - "Average household income was ₱189,842, with 91.5% earning wages."
  - "Food at home accounts for 55.4% of total spending."
  - "Only 35.3% have deposit accounts, while 24.3% have e-money."
  - "Emergency savings are low; 42.9% have no emergency fund."
  - "Government assistance was crucial during the pandemic."
```
---


---

## Agent Instruction

If the agent reading this document believes further context about a paper is needed, it may request the original converted markdown file (with the '_marked' suffix) from the user for the relevant paper(s).
