# Compiled Research Summaries

## Filters Applied

- Designation: `local`

**Total Papers:** 25

**Note:** Included papers positions 1 to 25, Sorted by year.

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

## Paper 2: Navarro & Bantulo_summarized.md

**Source File:** `Navarro & Bantulo_summarized.md`

```yaml
paper_id: 10.46827/ejes.v13i5.6659
designation: local
title: FINANCIAL HARDSHIPS OF TRICENARIANS EDUCATORS: PREPARING FOR THE FUTURE AMID DEBT CHALLENGES
authors: Navarro, R. J. L.; Bantulo, J. S.
year: 2026
venue: European Journal of Education Studies
odin_topics:
  - 1.C
  - 2.A
  - 5.A
  - 13.A
tldr: Tricenarian educators face financial strain, mental burden, and work disruption from debt, yet develop coping strategies like budgeting, seeking support, and gaining insights for financial discipline and career growth.
problem_and_motivation: Educators in their thirties face significant financial hardships due to low salaries, rising living costs, and student debt, which affect their well-being and professional performance. There is a lack of localized research on how these tricenarian educators manage debt while preparing for future financial stability. This study addresses that gap by documenting their lived experiences to inform support mechanisms and policy development.
approach:
  - A qualitative single-case study design was used to explore the lived experiences of five tricenarian educators at Platon Esperanza Taguding Elementary School.
  - Participants were purposively selected, aged 30-39 with 8-15 years of teaching experience, and actively managing loans.
  - Data was collected through semi-structured interviews, conducted in person or online, and audio-recorded with informed consent.
  - The Colaizzi method was employed for data analysis, involving familiarization, coding, and thematic synthesis.
  - Thematic analysis followed Braun and Clarke's framework to identify patterns related to financial strain, coping, and career effects.
findings:
  - Participants reported major challenges including financial strain, mental burden, work distraction, and postponed aspirations.
  - Coping mechanisms included financial planning, controlled spending, emotional release, and seeking social and family support.
  - Insights gained included empowered financial decisions, financial growth, career motivation, and long-term planning.
  - num: All five participants experienced persistent debt-related pressure affecting their teaching performance and personal well-being.
  - Participants demonstrated resilience through strategic coping and reflective financial awareness despite continuing hardships.
key_figures_tables:
  - Table 1: Challenges, coping, and insights for Participant 1 → Highlights financial strain and the use of budgeting and emotional release.
  - Table 2: Challenges, coping, and insights for Participant 2 → Shows limited income and reliance on support systems for coping.
  - Table 3: Challenges, coping, and insights for Participant 3 → Demonstrates emotional exhaustion and the use of digital tracking tools.
  - Table 4: Challenges, coping, and insights for Participant 4 → Reveals work disruption and the role of prayer and family support.
  - Table 5: Challenges, coping, and insights for Participant 5 → Indicates persistent burdens and the use of budget monitoring tools.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Tricenarian educators
    definition: Teachers aged 30 to 39 years old.
  - term: PFMS
    definition: Personal Finance Management System.
critical_citations:
  - "[Moghayedi et al., 2022] — Context for global teacher financial challenges."
  - "[Olyn, 2023] — Context for global teacher financial challenges."
  - "[Webber & Burns, 2021] — Context for global teacher financial challenges."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly examines financial behaviors, coping mechanisms, and decision-making of Filipino educators.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Describes debt reliance and family support as coping strategies within a Filipino cultural context.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Provides insights into the financial behavioral profiles and coping strategies of a specific demographic group.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Highlights challenges in saving and the postponement of financial goals due to debt and limited income.
  contribution: This paper provides qualitative evidence on the financial behaviors and coping mechanisms of Filipino educators, which can inform the design of behavioral profiling and expense categorization modules in Odin. It highlights the need for culturally sensitive financial support and the importance of understanding user constraints for effective budget recommendation. The findings on debt management and long-term planning are directly relevant to savings and debt management features.
  directly_justifies:
    - "Financial strain and debt burden directly affect user focus and teaching performance."
    - "Educators use budgeting tools and financial planning as coping mechanisms."
    - "Debt is incurred to support family and professional aspirations."
    - "Financial hardship leads to postponed aspirations and career advancement delays."
    - "Emotional and social support are key coping strategies for financial stress."
  limits:
    - "The study is limited to five educators in a single school district, limiting generalizability."
    - "The qualitative design provides rich narratives but does not quantify the financial impact."
    - "The sample is restricted to educators in a rural setting, which may not reflect urban experiences."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains flagged as relevant were Filipino Cultural Context, Behavioral Profiling & Classification, and Savings & Debt Management. Topic codes 1.C (Financial Behavior), 2.A (Culturally Specific Financial Practices), 5.A (Financial Behavioral Profiles), and 13.A (Savings Goal Management) were selected. The relevance was assessed as high for 1.C due to the direct focus on financial decision-making, and medium for 2.A, 5.A, and 13.A due to their contextual and supporting evidence. Borderline cases included the paper's discussion of spending cycles (2.B) and user constraints (3.C), but these were rejected as the paper does not provide actionable insight for Odin's design in those specific areas. The paper's overall relevance to Odin is contextual, providing foundational behavioral insights rather than algorithmic or system-specific contributions.
limitations:
  - "The study is based on a small sample size of five participants. [unacknowledged]"
  - "The findings may not be generalizable to other populations or settings. [unacknowledged]"
  - "The study relies on self-reported data, which may be subject to recall bias. [unacknowledged]"
  - "The research was conducted in a specific rural context, limiting its applicability to urban educators. [unacknowledged]"
remember_this:
  - "Tricenarian educators use budgeting and financial planning to manage debt."
  - "Financial hardship causes mental burden and work disruption among educators."
  - "Coping strategies include seeking social and family support for relief."
  - "Debt is often incurred to support family and professional development goals."
  - "Financial literacy is crucial for long-term financial stability and career growth."
```
---

## Paper 3: Bangko Sentral ng Pilipinas-2026_summarized.md

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

## Paper 4: Espiritu-2026_summarized.md

**Source File:** `Espiritu-2026_summarized.md`

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

## Paper 5: Amado_summarized.md

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

## Paper 6: Del Rosario_summarized.md

**Source File:** `Del Rosario_summarized.md`

```yaml
paper_id: 10.65339/ijsair.V2.I2.228
designation: local
title: Financial Literacy of Teachers in Selected Private Schools
authors: Del Rosario, E. A.
year: 2026
venue: International Journal of Sustainability and Advanced Integrated Research
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.B
  - 3.A
  - 4.A
  - 4.B
  - 5.A
tldr: Examines financial literacy among 103 private school teachers in Binangonan, Rizal, finding moderate overall literacy with significant demographic and professional influences, particularly in retirement planning and investing.
problem_and_motivation: Private school teachers in the Philippines often lack structured financial education, leading to potential financial stress and limited long-term security. Despite legal mandates for financial literacy, there is insufficient empirical data on this specific population, especially in the Binangonan, Rizal context, which is crucial for designing targeted interventions.
approach:
  - Used a descriptive survey research design with a researcher-made questionnaire administered to 103 teachers from five private schools.
  - Measured financial literacy across four domains: retirement planning, budgeting and saving, insurance, and investing.
  - Profiled respondents by age, sex, civil status, position, education, service length, and in-service training.
  - Analyzed data using frequency, percentage, mean, and F-test to determine significant differences based on profile variables.
  - Ensured content validity through expert review and adhered to ethical standards including informed consent and data privacy.
findings:
  - Most respondents are young (20-25), female, single, contractual, with baccalaureate degrees and 0-5 years of service.
  - Overall financial literacy is moderate (composite mean 3.46), with budgeting and saving (3.90) highest and insurance (2.98) lowest.
  - num: Age significantly affects retirement planning (F=6.101, p=0.000), budgeting and saving (F=3.172, p=0.007), and investing (F=2.950, p=0.011).
  - num: Gender significantly influences budgeting and saving (F=4.085, p=0.046) but not other domains.
  - Position title significantly affects retirement planning (F=3.617, p=0.030) and budgeting and saving (F=3.771, p=0.026).
  - Length of service significantly influences retirement planning (F=3.143, p=0.018), insurance (F=3.601, p=0.009), and investing (F=3.331, p=0.013).
  - In-service training significantly improves literacy in retirement planning (F=2.861, p=0.027), budgeting and saving (F=3.85, p=0.006), and investing (F=6.223, p=0.000).
  - Civil status and educational attainment show limited significant effects, with the latter only affecting investing (F=3.983, p=0.049).
key_figures_tables:
  - "Table 1: Profile distribution of respondents by age, sex, civil status, position, education, service length, and training → Most teachers are young, female, single, contractual, and early-career."
  - "Table 2: Mean financial literacy scores for retirement planning, budgeting/saving, insurance, and investing → Budgeting and saving has the highest literacy; insurance the lowest."
  - "Table 3: F-test results for demographic/professional influences on financial literacy → Age, position, service length, and training significantly impact specific literacy domains."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: PFMS
    definition: Personal Finance Management System.
  - term: F-test
    definition: Statistical test used to compare variances and determine if group means are significantly different.
  - term: TCCM framework
    definition: Theory, Context, Characteristics, Methodology framework for systematic literature reviews.
critical_citations:
  - "[Chabaefe & Qutieshat, 2024] — Provides conceptual framework linking financial education, experience, and literacy."
  - "[Zuiker et al., 2022] — Highlights the role of financial professionals in tailored education across life stages."
  - "[Soroko, 2023] — Argues for a critical, context-aware approach to financial literacy education beyond personal management."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: low
      justification: Provides demographic data on private school teachers, a subset of Filipino professionals.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: low
      justification: Discusses income, savings, and investment practices relevant to financial structure.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Directly investigates budgeting, saving, and investing behaviors.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Does not address seasonal spending; focuses on general literacy and planning.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: Discusses budgeting and saving as a domain but does not propose categorization frameworks.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Reviews literature on financial literacy but not specific PFMS.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: contextual
      justification: Identifies gaps in financial literacy programs for private school teachers, but not in PFMS.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: low
      justification: Examines literacy levels which can inform behavioral profiling.
  contribution: This study provides empirical data on the financial literacy levels of a specific Filipino demographic (private school teachers), revealing that while they are confident in short-term budgeting, their knowledge of long-term financial planning like retirement and insurance is low. This finding can inform the design of Odin's user onboarding and educational content by highlighting the need to prioritize basic financial concepts, particularly in retirement and risk management. The study's identification of demographic factors that influence literacy (e.g., age, service length) suggests that Odin should consider user profiles and provide adaptive, lifecycle-based guidance. Ultimately, the work underscores the broader need for financial education interventions, which Odin's features could directly support or supplement.
  directly_justifies:
    - "Teachers show moderate financial literacy, suggesting Odin's educational content should start with foundational concepts."
    - "Budgeting and saving literacy is highest, indicating Odin should leverage this strength for engagement."
    - "Retirement planning literacy is low, justifying Odin's focus on long-term goal setting for young professionals."
    - "In-service training improves literacy, supporting the inclusion of educational modules within Odin."
  limits:
    - "Study is limited to private school teachers in one municipality, which may not be generalizable to all Filipino young professionals."
    - "The research relies on self-reported perceptions of financial literacy, which may not reflect actual knowledge."
    - "The study does not examine actual financial behaviors or outcomes, only self-assessed literacy."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was conducted. The paper was flagged as relevant to 'Filipino Cultural Context' (2.A, 2.B, 2.D) because it studies a specific Filipino population and mentions their financial practices, though it lacks focus on cultural practices or seasonal spending. It was highly relevant to 'Expense Categorization' (3.A) and 'Behavioral Profiling' (5.A) because it directly measures budgeting, saving, and investing behaviors and identifies demographic drivers of these behaviors. It touches on 'Existing Systems' (4.A, 4.B) by reviewing the landscape of financial literacy and identifying gaps in support for private school teachers. Borderline cases included its relevance to 3.C (User-Defined Allocation Constraints), which was considered and rejected as the paper does not discuss user-defined spending rules. Topics like 6.A, 7.A, 8.A, 9.A, 10.A, 11.A, 12.A, and 13.A were rejected for no direct mention of forecasting, algorithmic recommendations, anomaly detection, mobile design, data privacy, engagement, evaluation frameworks, or debt/savings management specific to a PFMS. Overall, the paper provides contextual evidence for the financial needs and literacy gaps of Filipino young professionals, which can inform Odin's foundational understanding of its user base.
limitations:
  - "The study is geographically limited to Binangonan, Rizal, which may affect generalizability across the Philippines. [unacknowledged]"
  - "Self-reported data on financial literacy may be subject to social desirability or overconfidence bias."
  - "The cross-sectional design captures literacy at one point in time, not accounting for changes or the impact of interventions."
remember_this:
  - "Private school teachers show moderate financial literacy, with budgeting skills stronger than retirement planning."
  - "Demographic factors like age, gender, and service length significantly influence financial literacy scores."
  - "In-service training improves financial literacy in key domains like retirement and investing for teachers."
  - "Insurance literacy is notably lower than other financial areas among the surveyed teachers."
```
---

## Paper 7: Dela Cruz_summarized.md

**Source File:** `Dela Cruz_summarized.md`

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

## Paper 8: Lantin-Magana et al_summarized.md

**Source File:** `Lantin-Magana et al_summarized.md`

```yaml
paper_id: 3a5c6d8e-9f0b-4a2c-8b3d-6e7f8a9b0c1d
designation: local
title: Predictors of Investment Decision among Selected Individuals in Key Cities of Laguna: An Extended Theory of Planned Behavior Approach
authors: Lantin-Magana, L.; Espelita, C.A.M.H.; Calingasan-Habana, C.A.; Atento, A.G.B.; Atento, R.G.O.
year: 2026
venue: Journal of Enterprise Strategy and Management Innovation
odin_topics:
  - "1.A"
  - "1.C"
  - "5.A"
  - "5.B"
tldr: Investment decisions among Filipino urban professionals are associated with attitudes toward investing, monthly salary, capital market knowledge, and sex, with attitude and salary being the strongest predictors in a TPB-extended model.
problem_and_motivation: Investment participation in the Philippines remains limited, and decisions to invest are shaped not only by financial capacity but also by evaluative beliefs, risk appraisal, institutional trust, and perceived readiness. An exclusive focus on financial capacity is insufficient for explaining observed differences in investment participation. The study addresses the gap by examining how individual perceptions and demographic attributes relate to investment decisions.
approach:
  - Data were collected via an online survey from 483 respondents in Calamba, Santa Rosa, and Biñan, Laguna.
  - The questionnaire measured risk tolerance, attitude toward capital markets, capital market knowledge, government trust, and attitude toward investment using a 6-point scale.
  - Investment decision was self-reported using a six-point scale.
  - Descriptive statistics, group comparisons (t-test and ANOVA), Pearson correlation, and stepwise multiple regression were used to analyze associations and identify predictors.
findings:
  - Risk tolerance received the highest rating (M=4.81), while government trust received the lowest (M=3.85).
  - num: Investment decision scores differed significantly by sex (p=0.002) and by monthly salary bracket (p<0.001).
  - num: Capital market knowledge showed the highest correlation with investment decision (r=0.210, p=0.001), followed by attitude toward investment (r=0.179, p=0.003).
  - num: Attitude toward investment (coefficient 0.345) and monthly salary (coefficient 0.368) jointly explained 16.2% of variance in investment decision (R²=0.162, p<0.001).
key_figures_tables:
  - Table 1: Mean and standard deviation of risk tolerance (4.81, 1.19), attitude toward capital markets (4.60, 1.23), knowledge (4.10, 1.32), and government trust (3.85, 1.33) → Perceptions vary, with risk tolerance highest and trust lowest.
  - Table 2: Stepwise regression coefficients for attitude toward investment (0.345) and monthly salary (0.368), R²=0.162 → Attitude and salary jointly predict investment decision.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "TPB"
    definition: "Theory of Planned Behavior, a framework emphasizing evaluative beliefs, perceived control, and social influences."
  - term: "PSE"
    definition: "Philippine Stock Exchange."
  - term: "Risk tolerance"
    definition: "Disposition or capacity to accept risk exposure in investment."
  - term: "Attitude toward capital markets"
    definition: "Favorable evaluation of market participation and its benefits."
  - term: "Government trust"
    definition: "Confidence in government institutions and political climate regarding investment."
  - term: "Investment decision"
    definition: "Self-reported decision to engage in investing, measured on a six-point scale."
critical_citations:
  - "Parsai & Chandok (2025) — financial literacy review in investment decision."
  - "Salampessy & Krisnawati (2025) — influence of literacy, risk perception on investment."
  - "Akhtar & Das (2019) — predictors of investment intention in stock markets."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "medium"
      justification: "The sample is drawn from urban Filipino populations, providing demographic context for young professionals."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Directly examines financial behavior related to investment decisions among Filipino respondents."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Identifies predictors (attitude, salary, knowledge) that can inform behavioral profiling in PFMS."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "medium"
      justification: "The identified predictors could serve as initial inputs for profiling new users, addressing cold-start."
  contribution: "The paper's identification of attitude toward investment and monthly salary as key predictors informs Odin's behavioral profiling module by highlighting which user attributes are most associated with investment decisions. The correlations between capital market knowledge and investment decisions support the inclusion of financial literacy assessments in user onboarding. The significant differences by sex and income suggest that Odin's recommendation engine should consider demographic factors when tailoring financial advice. The finding that government trust is low underscores the need for trust-building features in the app."
  directly_justifies:
    - "Attitude toward investment is a significant predictor of investment decision (coefficient 0.345)."
    - "Monthly salary is a significant predictor of investment decision (coefficient 0.368)."
    - "Capital market knowledge is positively correlated with investment decision (r=0.210)."
    - "Investment decisions differ significantly by sex (p=0.002)."
  limits:
    - "Cross-sectional design prevents causal inference."
    - "Purposive sampling and online data collection may limit generalizability."
    - "Self-reported measures may be subject to social desirability bias."
    - "The model explains only 16.2% of variance, indicating omitted variables."
    - "Stepwise regression may be sensitive to sample-specific patterns."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains of Behavioral Profiling & Classification and Filipino Cultural Context were flagged as relevant. Specifically, topics 1.A (demographic context), 1.C (financial behavior), 5.A (behavioral profiles), and 5.B (profile dynamics) were selected with high or medium relevance. Borderline cases included the overlap between 1.A and 1.C, both retained due to their complementary value. Domains such as Expense Categorization, Spending Forecasting, Budget Recommendation, Anomaly Detection, Mobile-First Design, Data Privacy, User Retention, System Evaluation, and Savings & Debt Management were rejected because the paper does not address those topics. The paper provides moderate overall relevance to Odin by offering empirical evidence on behavioral predictors that can be used in profiling and personalization."
limitations:
  - "Cross-sectional design prevents causal inference."
  - "Purposive sampling and online data collection may limit generalizability."
  - "Self-reported measures may be subject to social desirability bias."
  - "The model explains only 16.2% of variance, indicating omitted variables."
  - "Stepwise regression may be sensitive to sample-specific patterns."
remember_this:
  - "Attitude toward investment and monthly salary are the strongest predictors of investment decision."
  - "Capital market knowledge shows the highest correlation with investment decision among measured constructs."
  - "Investment decisions differ by sex and income, with males and higher earners scoring higher."
  - "The model explains 16.2% of variance, indicating other determinants also matter."
```
---

## Paper 9: Pesa et al_summarized.md

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

## Paper 10: Velasco_summarized.md

**Source File:** `Velasco_summarized.md`

```yaml
paper_id: 10.20944/preprints202603.1811.v1
designation: local
title: A Decade of Applied Quantitative Analytics for Philippine Policy: Forecasting, Statistical Forensics, and Predictive Modeling Across Education, Energy, Agriculture, Health, and Finance
authors: Velasco, A.
year: 2026
venue: Preprints.org
odin_topics:
  - 4.A
  - 4.B
  - 6.A
  - 6.B
  - 7.A
  - 8.A
  - 8.B
  - 12.A
  - 12.B
tldr: Reviews Philippine policy analytics across sectors, showing a progression from descriptive models toward machine learning, Benford-based anomaly detection, and explainable AI.
problem_and_motivation: Governments must allocate scarce resources under uncertainty, and while quantitative analytics is central to this, the application and maturation of these methods in the Philippine context across key policy sectors has not been systematically synthesized.
approach:
  - A structured narrative review of a core corpus of 17 Philippine studies from 2019 to 2025 was conducted.
  - Studies were coded on five dimensions: domain, dataset, modeling approach, validation strategy, and policy contribution.
  - The sectors covered include education, energy, agriculture, health, and finance.
  - External comparison literature was used to position the corpus against broader international developments in the respective fields.
  - The review identifies cross-cutting methodological trends and gaps in validation and integration.
findings:
  - The literature shows a clear progression from descriptive diagnostics and classical time-series models toward machine learning, deep learning, and explainable AI.
  - A distinct forensics strand emerged through Benford-based anomaly detection for data quality assessment in agriculture and health.
  - Forecasting studies have moved from univariate ARIMA to comparative machine learning, including random forests, neural networks, and LSTM.
  - Validation rigor is uneven, ranging from explicit holdout sets to residual diagnostics and significance testing.
  - num: The machine-learning study on rice and corn forecasting reported the best overall performance for random forests.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: ARIMA
    definition: Autoregressive Integrated Moving Average, a class of statistical models for time series forecasting.
  - term: SARIMA
    definition: Seasonal Autoregressive Integrated Moving Average, an extension of ARIMA that supports seasonal data.
  - term: LSTM
    definition: Long Short-Term Memory, a type of recurrent neural network architecture capable of learning long-term dependencies.
  - term: NNAR
    definition: Neural Network Autoregression, a time series forecasting model using a neural network.
  - term: SHAP
    definition: SHapley Additive exPlanations, a method for interpreting the output of machine learning models.
  - term: Benford's Law
    definition: An observation that in many naturally occurring datasets, the leading digit is likely to be small.
critical_citations:
  - "[Rumberger & Lim, 2008] — Foundational review of dropout research."
  - "[van Klompenburg et al., 2020] — Systematic review of ML for crop yield prediction."
  - "[World Health Organization, 2021] — Guide on using routine data for health monitoring."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides a methodological landscape for applied analytics in the Philippines.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies specific gaps like limited multivariate modeling and uneven validation.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Reviews forecasting methods applicable to spending prediction.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Discusses ARIMA, machine learning, and deep learning for time-series forecasting.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Reviews forecasting as a basis for planning and resource allocation.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Reviews Benford-based anomaly detection for data quality and fraud screening.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Forensics strand using Benford's law provides a methodological example.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Critiques validation practices, noting uneven rigor and advocating for better methods.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Discusses model benchmarking, error metrics, and the need for external validation.
  contribution: "This paper provides a systematic review of forecasting, anomaly detection, and predictive modeling techniques applied to Philippine data, which directly informs Odin's algorithmic module selection and validation framework. Its critique of univariate models and uneven validation justifies Odin's investment in multivariate forecasting and rigorous holdout evaluation. The review of Benford-based forensics supports Odin's anomaly detection approach, and its call for integrated analytics architectures aligns with Odin's goal of combining forecasting, budgeting, and anomaly detection. The identified gaps, such as limited uncertainty quantification and operational deployment, serve as cautionary points for Odin's development roadmap."
  directly_justifies:
    - "The progression from ARIMA to machine learning supports selecting LSTM or random forest for spending forecasting."
    - "Benford-based anomaly detection is a valid, low-cost method for screening financial data."
    - "Explicit train-validation splits and error metrics are necessary for evaluating Odin's forecasting module."
    - "External validation across user cohorts is a critical gap that Odin should address."
  limits:
    - "The paper is a review and does not provide original empirical findings for Odin to directly cite for specific model performance."
    - "The financial sector review is limited to stock-index prediction, not personal spending patterns."
    - "Recommendations are high-level and require translation into specific implementation details for a PFMS."
  mapping_rationale: "All 12 functional domains and their associated topic codes were systematically scanned. The domains of 'Spending Forecasting' (6.A, 6.B), 'Anomaly Detection' (8.A, 8.B), and 'System Evaluation' (12.A, 12.B) were flagged as high relevance due to the paper's detailed review of forecasting methods, Benford-based forensics, and validation practices. The 'Existing Systems & Gaps' domain (4.A, 4.B) was selected as high/contextual because the paper provides a landscape of applied analytics and explicitly lists methodological limitations. 'Budget Recommendation' (7.A) was medium relevance as it provides domain knowledge on resource allocation. The paper was considered and rejected for 'Financial Behavioral Profiles' (5.A-C), 'Filipino Cultural Context' (2.A-D), and 'Data Privacy & User Trust' (10.A, 10.B) as it does not discuss these specific topics. The overall relevance is high for informing the design and evaluation of Odin's algorithmic core."
limitations:
  - "The corpus is heterogeneous, mixing journal articles and preprints with varying validation designs. [unacknowledged]"
  - "Direct numerical comparison across sectors is not intended due to differences in data frequency and sample size. [acknowledged]"
  - "Limited evidence of operational deployment or external validation of the models reviewed. [acknowledged]"
  - "The review focuses on sectoral policy and does not cover personal finance or behavioral profiling. [unacknowledged]"
remember_this:
  - "Philippine applied analytics progressed from descriptive models to machine learning and anomaly detection."
  - "Validation practices are uneven; explicit holdout sets are not universal."
  - "Benford-based law is used for data quality audits in health and agriculture."
  - "Future work requires integrated, multivariate, and uncertainty-aware analytics."
```
---

## Paper 11: Brucal et al_summarized.md

**Source File:** `Brucal et al_summarized.md`

```yaml
paper_id: "d0e5f5a0-2b3c-4d5e-8f9a-1b2c3d4e5f6a"
designation: "local"
title: "Tracing the Trajectory of Supply and Demand Drivers in the Philippine Economy: Policy Implications, Econometric Applications, and Market Optimization"
authors: "Brucal, A. P.; Claveria, P. S. L.; Lacson, J. T. N.; Abante, M. V.; Vigonte, F. G.; Caisip, A."
year: 2026
venue: "Unknown"
odin_topics:
  - "4.A"
  - "6.A"
  - "7.A"
  - "10.A"
  - "13.A"
tldr: "A systematic literature review identifies government regulations, market frameworks, fiscal policies, consumer behavior, and income distribution as key supply-demand drivers in the Philippine economy."
problem_and_motivation: "Standardized econometric models often fail to capture the unique socio-economic and cultural determinants of the Philippine economy. There is a lack of localized models and comprehensive policies tailored to these characteristics, hindering effective market intervention. This gap limits the government's ability to foster transparency, equity, and sustainable growth."
approach:
  - "Conducted a systematic literature review (SLR) using the PRISMA framework to ensure transparency and reproducibility."
  - "Searched Google Scholar, ScienceDirect, ResearchGate, and JSTOR for peer-reviewed articles published from 2015 to the present."
  - "Focused on studies related to econometric modeling, consumer behavior, fiscal policies, and market structures within specific regional contexts."
  - "Included government sources and policy papers alongside academic literature for a comprehensive policy perspective."
  - "Classified selected works thematically to integrate findings on government interventions, pricing strategies, and demand forecasting."
findings:
  - "Government regulations like the CREATE Act and agricultural subsidies are key drivers of supply, increasing capacity and stabilizing prices."
  - "Market frameworks are hampered by infrastructure inadequacies and unequal resource access, requiring public-private partnerships for improvement."
  - "Keynesian interventions, such as public infrastructure projects during the COVID-19 pandemic, effectively stimulated demand and retained employment."
  - "Fiscal policies, including the TRAIN Law, aim to increase revenues while protecting low-income households from excessive tax burdens."
  - "Income distribution significantly affects demand patterns, with urban households consuming more discretionary goods than rural households."
  - "Econometric techniques, such as regression models and ARIMA time-series analysis, are critical for estimating demand and forecasting seasonal trends."
  - "Localized econometric models that integrate region-specific variables provide more accurate insights into Philippine market behaviors."
  - "The Philippine Competition Act seeks to prevent monopolistic practices and promote fair competition, but implementation challenges remain."
  - "The BSP's inflation-targeting policies have been crucial for maintaining price stability and a favorable investment environment."
  - "Collaboration between government and private sectors to establish centralized data repositories is essential for developing robust localized models."
key_figures_tables:
  - "Figure 1: PRISMA flow diagram outlining the systematic literature review process → Visual representation of study selection and screening methodology."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "ARIMA"
    definition: "Autoregressive Integrated Moving Average, a time-series analysis model used for forecasting."
  - term: "BSP"
    definition: "Bangko Sentral ng Pilipinas, the central bank of the Philippines."
  - term: "CREATE Act"
    definition: "Corporate Recovery and Tax Incentives for Enterprises Act, a Philippine law providing tax incentives."
  - term: "PRISMA"
    definition: "Preferred Reporting Items for Systematic Reviews and Meta-Analyses, a framework for systematic literature reviews."
  - term: "SLR"
    definition: "Systematic Literature Review, a method for identifying and synthesizing research evidence."
  - term: "TRAIN Law"
    definition: "Tax Reform for Acceleration and Inclusion Law, a Philippine tax reform law."
critical_citations:
  - "[De Loecker et al., 2016] — Examines pricing policies and market structures."
  - "[Hansen, 2022] — Provides a foundational framework for econometric modeling."
  - "[Auerbach & Smetters, 2017] — Analyzes the effects of fiscal policies on resource allocation."
  - "[Kumar et al., 2019] — Discusses big data approaches to demand forecasting in specific contexts."
  - "[Vu et al., 2022] — Analyzes the impact of supply chain financing and tax incentives on business performance."
relevance:
  topics:
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "low"
      justification: "Reviews general economic systems and policies, not specific PFMS."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses econometric demand estimation models applicable to spending forecasting."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "low"
      justification: "Focuses on macro-level fiscal policies rather than individual budgeting strategies."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "contextual"
      justification: "Discusses data infrastructure and transparency, indirectly relating to data handling practices."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "low"
      justification: "Mentions income distribution and economic growth, not specific savings goal management."
  contribution: "This paper provides a macro-level economic framework that can inform the foundational understanding of spending patterns for a PFMS like Odin. The discussion of government fiscal policies and their impact on consumer behavior offers context for designing budget recommendation modules. The review of econometric techniques, such as time-series analysis, provides a basis for developing Odin's spending forecasting algorithms. The emphasis on data infrastructure and transparency reinforces the need for secure and reliable data handling in the system."
  directly_justifies:
    - "Government policies and macroeconomic variables significantly influence consumer spending behavior and market dynamics."
    - "Econometric models, including time-series analysis, are effective for demand forecasting."
    - "Localized models that incorporate region-specific variables are necessary for accurate predictions."
  limits:
    - "The paper is a systematic literature review and does not present new empirical data or a novel algorithm."
    - "The findings are general and may not be directly transferable to the specific design of a personal finance application for young professionals."
    - "The paper does not address user-centric financial behaviors or behavioral profiling, which are core to Odin's purpose."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was conducted. Domains related to 'Filipino Cultural Context' (2.A-2.D) and 'Behavioral Profiling' (5.A-5.C) were considered but rejected as the paper focuses on macroeconomic drivers rather than individual financial practices. The domain 'Expense Categorization' (3.A-3.C) was also rejected as it does not address how to define or manage personal spending categories. The domain 'Existing Systems & Gaps' (4.A) was flagged as 'low' because the paper reviews general economic systems, not PFMS. The domain 'Spending Forecasting' (6.A) was flagged as 'medium' due to its discussion of econometric techniques. The domain 'Budget Recommendation' (7.A) was flagged as 'low' for its discussion of fiscal policies, and 'Data Privacy' (10.A) was 'contextual' for its mention of data infrastructure. 'Savings & Debt Management' (13.A) was 'low' as it only tangentially touches on income distribution. Overall, the paper's relevance to Odin is indirect, providing a high-level economic context rather than specific, actionable insights for PFMS design."
limitations:
  - "The review relies on secondary sources; the quality of findings depends on the included studies."
  - "Excluding non-English articles may have omitted relevant regional research."
  - "The focus on literature from 2015 onward may miss foundational older works."
  - "The study does not propose or validate a specific localized econometric model."
remember_this:
  - "Government fiscal policies shape consumer spending and market stability."
  - "Econometric techniques like ARIMA are used for demand forecasting."
  - "Localized economic models require region-specific data for accuracy."
  - "Data transparency and infrastructure are vital for evidence-based policy."
  - "Income inequality is a key driver of different demand patterns in the Philippines."
```
---

## Paper 12: Cabalfin et al_summarized.md

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

## Paper 13: Claros et al_summarized.md

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

## Paper 14: Askhiyah_summarized.md

**Source File:** `Askhiyah_summarized.md`

```yaml
paper_id: 10.59784/journaljoae.v1i1.37
designation: local
title: Digital Finance Usage and Its Impact on Consumer Economic Behavior Based on National Data
authors: Askhiyah, U. M.
year: 2026
venue: Journal of Applied Econometric
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 5.A
  - 5.B
  - 6.A
  - 6.B
  - 7.B
  - 7.D
  - 8.A
  - 9.A
  - 10.A
tldr: Digital finance adoption increases household consumption by 8.7% and financial literacy by 1.4 points but reduces savings balances by 5.8% and raises debt-to-income ratios, with risks concentrated among young lower-middle-income households.
problem_and_motivation: The comprehensive impact of digital finance on consumer economic behavior remains inadequately understood despite its rapid proliferation. Existing research has produced mixed findings, creating ambiguity for policy formulation and raising concerns about potential negative consequences for financially vulnerable populations.
approach:
  - This study uses nationally representative household survey data from 45,678 respondents.
  - It employs a multidimensional digital finance usage intensity index reflecting breadth and depth of engagement.
  - Propensity score matching with sensitivity analysis constructs comparable treatment and control groups to mitigate selection bias.
  - Instrumental variable estimation leverages regional digital infrastructure density as an instrument for causal identification.
  - Panel data fixed-effects methods are applied to a longitudinal subsample of 8,234 households to control for time-invariant unobserved heterogeneity.
findings:
  - num: Digital finance adoption increases total household consumption expenditure by 8.7%.
  - num: Digital finance users have a 12.4 percentage point higher probability of having a formal savings account.
  - num: Users' average savings balance is 5.8% lower than that of comparable non-users.
  - num: Financial literacy scores rise by 1.4 points on a 10-point scale for digital finance users.
  - num: Digital finance users are 18.7 percentage points more likely to have access to formal credit.
  - num: Users show a debt-to-income ratio 6.4 percentage points higher than non-users.
  - num: Late payment rates are 6.3 percentage points higher among digital finance users.
  - num: 54.7% of digital credit users borrow for consumption, compared to 32.4% of traditional credit users.
  - num: The financial wellbeing composite index is 8.5 points higher for digital finance users.
  - The positive consumption effect is strongest for discretionary goods, with electronics spending increasing by 18.5%.
key_figures_tables:
  - Table 1: Demographic comparison of users vs. non-users → Digital finance users are younger, more urban, and more educated.
  - Table 2: Impact on consumption by category → Discretionary spending increases more than basic needs.
  - Table 3: Savings and financial management indicators → Digital finance improves financial planning practices.
  - Table 4: Digital credit utilization and debt profile → Users have higher debt burdens and late payment rates.
  - Table 5: Financial literacy and wellbeing outcomes → Users show higher literacy, confidence, and planning behavior.
  - Figure 1: Distribution of usage intensity → Most users have low-to-moderate intensity, with only 18.7% high-intensity.
  - Figure 2: Heterogeneous consumption effects → Young and urban households show the largest consumption increases.
  - Figure 3: Savings behavior comparison → Users have better access but lower balances than non-users.
  - Figure 4: Credit risk indicators → Vulnerable subgroups face the highest overleveraging risks.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: ATT
    definition: Average Treatment Effect on the Treated, measuring the impact on those who adopted digital finance.
  - term: PSM
    definition: Propensity Score Matching, a technique to reduce selection bias by matching treated and control units on observables.
  - term: IV
    definition: Instrumental Variable estimation, used to address endogeneity by leveraging exogenous variation.
  - term: OLS
    definition: Ordinary Least Squares, a standard linear regression method.
  - term: FE
    definition: Fixed Effects, a panel data method controlling for time-invariant unobserved heterogeneity.
critical_citations:
  - "[Li et al., 2020] — Found 7-9% consumption increase from mobile payment adoption."
  - "[Banna & Alam, 2021] — Linked digital finance to banking stability in ASEAN."
  - "[Batista & Vicente, 2020] — Documented positive savings effects of mobile money in Africa."
  - "[Danisman & Tarazi, 2020] — Raised concerns about rapid digital credit expansion risks."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: The study categorizes consumption into basic needs and discretionary goods, providing empirical categories.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: The heterogeneity in spending effects by category informs how Odin should weight or present different expense types.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides a broad context on digital finance penetration and usage patterns across demographics.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly profiles users based on consumption, savings, and credit behavior, highlighting different subpopulations.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: medium
      justification: The variation in adoption and behavioral responses provides evidence for how profiles evolve with technology.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: low
      justification: The paper documents spending patterns that could be used as input features for forecasting models.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: Although no specific algorithm is tested, the spending data patterns are relevant for forecasting contexts.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: The consumption and savings trade-offs directly relate to how budgets might be recommended to different user types.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: contextual
      justification: The heterogeneous impacts on vulnerable groups suggest the need for flexible budget recommendations.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: The documented shifts in spending and debt patterns provide a baseline for what constitutes normal vs. anomalous behavior.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: The high adoption rates and usage frequency underscore the importance of mobile-first design for engagement.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: The reliance on digital platforms for financial data highlights the critical need for privacy and security measures.
  contribution: This study provides robust empirical evidence on the causal effects of digital finance on consumption, savings, and credit behavior using multiple identification strategies, directly justifying Odin's need for dynamic financial behavior modeling. The finding that digital finance improves financial literacy and planning behavior supports the integration of educational and goal-setting features within Odin. The documented trade-off between consumption and savings informs how Odin's budget recommendation module should balance spending and saving goals. The heterogeneous effects across demographic groups, especially young households, justify Odin's cold-start problem and the need for personalized behavioral profiles. The identification of overleveraging risks for vulnerable groups supports the implementation of anomaly detection and user trust mechanisms to alert users to potential financial distress.
  directly_justifies:
    - The consumption increase of 8.7% from digital finance adoption justifies modeling spending shifts as a function of platform usage.
    - Financial literacy improvements of 1.4 points after adoption support embedding educational content within Odin's interface.
    - Higher savings access but lower balances suggests Odin should promote structured saving features like autosave.
    - The elevated debt-to-income ratios for users justify proactive debt management features and alerts.
    - Heterogeneous effects by age and income justify personalized budget recommendations.
  limits:
    - The observational data and self-report surveys may contain biases despite econometric controls.
    - The study only examines short-term effects up to 24 months, leaving long-term wealth impacts unknown.
    - Individual psychological factors like self-control and risk preferences were not deeply measured.
    - Spillover effects at the community or financial system level were not examined.
    - The findings are limited to a specific country and time period.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated 34 topic codes was conducted. The domains flagged as relevant were Expense Categorization (3.A, 3.B), Existing Systems (4.A), Behavioral Profiling (5.A, 5.B), Spending Forecasting (6.A, 6.B), Budget Recommendation (7.B, 7.D), Anomaly Detection (8.A), Mobile-First Design (9.A), and Data Privacy (10.A). The paper was assigned high relevance for Behavioral Profiling (5.A) and Anomaly Detection (8.A) due to its detailed causal analysis of financial behavior changes and identification of vulnerable groups. Medium relevance was given to Expense Categorization (3.A, 3.B), Budget Recommendation (7.B), and Data Privacy (10.A) because the findings provide empirical grounding for category design, personalized budgets, and the need for trust safeguards. Low relevance was assigned to Predictive Modeling (6.A, 6.B) and Mobile-First Design (9.A) as the paper describes behavior patterns rather than testing forecasting algorithms or design principles directly. Contextual relevance was assigned to Existing Systems (4.A) and Infeasibility Handling (7.D) for providing background landscape and highlighting the need for flexible systems. Borderline cases included the consumption-savings trade-off touching both spending forecasting (6.A) and budget recommendation (7.B), which was resolved by assigning relevance to both but with different levels. Domains such as Filipino Cultural Context (2.A-2.D), User Retention (11.A-11.B), and System Evaluation (12.A-12.C) were considered but rejected as the paper does not address cultural practices, retention mechanisms, or evaluation frameworks. The Savings & Debt Management domain (13.A-13.C) was deemed relevant via the specific findings on savings balances and debt ratios, though not as a primary topic code. Overall, the paper offers strong empirical evidence for behavioral dynamics in Odin's core modules.
limitations:
  - The study uses observational data and self-report surveys, which may contain biases despite instrumental variables and panel data. [unacknowledged]
  - The analysis only examines short-term effects up to 24 months, so the long-term impact on wealth accumulation remains unknown. [unacknowledged]
  - Individual psychological factors such as self-control and risk preferences were not deeply measured. [unacknowledged]
  - Spillover effects at the community level and the financial system were not examined. [unacknowledged]
  - The findings are limited to a specific country and time period, requiring cross-country validation.
remember_this:
  - Digital finance adoption increases consumption by 8.7% but reduces savings by 5.8%.
  - Financial literacy scores rise by 1.4 points after adopting digital finance.
  - Young lower-middle-income households face the highest overleveraging risks.
  - Digital finance improves financial planning and management practices substantially.
  - The consumption-savings trade-off is a key behavioral paradox in digital finance.
```
---

## Paper 15: Osit_summarized.md

**Source File:** `Osit_summarized.md`

```yaml
paper_id: "10.69569/jip.2025.762"
designation: "local"
title: "Perceptions of Life Insurance Among Young Professionals in Higher Education"
authors: "Osit, A."
year: 2026
venue: "Journal of Interdisciplinary Perspectives"
odin_topics:
  - "1.A"
  - "1.C"
  - "2.A"
  - "10.B"
tldr: "Young non-teaching professionals in a Philippine university show high awareness and positive perceptions of life insurance, with cost as the main barrier and family security as the primary motivator, though policy ownership remains moderate."
problem_and_motivation: "Research on life insurance perceptions among young professionals in higher education is limited, despite their role in financial resilience. Understanding awareness, barriers, and motivators is necessary to inform workplace financial education and benefit programs. This study addresses this gap by examining these factors at a Philippine university."
approach:
  - "Descriptive-correlational survey of 98 non-teaching professionals aged 20–34 at University of Baguio."
  - "Validated structured questionnaire adapted from Paudel & Silwal (2016), Ghai & Vaish (2023), and Sharma et al. (2021)."
  - "Four-point Likert scale measured awareness, barriers, and motivators."
  - "Data analyzed using descriptive statistics and Pearson correlation."
findings:
  - "num: Overall awareness mean was 3.13 (SD=0.56) on a 4-point scale, indicating moderately high awareness."
  - "num: Perceived barriers overall mean was 2.15 (SD=0.53), with cost as the only moderate barrier (mean 2.76)."
  - "num: Motivating factors overall mean was 3.24 (SD=0.52), with family security as the strongest motivator (mean 3.53)."
  - "num: Awareness correlated positively with motivation (r=.32, p=.001) and negatively with barriers (r=-.29, p=.004)."
  - "Actual policy ownership was moderate (mean 2.64, SD=1.19), indicating an awareness-adoption gap."
key_figures_tables:
  - "Table 1: Likert scale interpretation → Used to categorize mean scores into levels."
  - "Table 2: Awareness indicators → High awareness overall but moderate ownership."
  - "Table 3: Perceived barriers → Low barriers overall; cost is the only moderate barrier."
  - "Table 4: Motivating factors → Strong motivation driven by family security and preparedness."
  - "Table 5: Correlation matrix → Awareness significantly correlates with motivation and barriers."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "None."
    definition: ""
critical_citations:
  - "[Ghai & Vaish, 2023] — Gap between awareness and adoption among young adults."
  - "[Sharma et al., 2021] — Competing financial obligations as barriers."
  - "[Alkan et al., 2020] — Financial literacy constrains evaluation of options."
  - "[LIMRA & Life Happens, 2025] — Young adults overestimate insurance cost."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "high"
      justification: "Directly surveys young Filipino non-teaching professionals, providing empirical data on their financial perceptions."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Examines awareness, barriers, and motivation as key financial behaviors."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "medium"
      justification: "Highlights family security as primary motivator, reflecting Filipino cultural values."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "medium"
      justification: "Measures trust in insurance companies as a barrier, relevant to trust in financial systems."
  contribution: "This paper provides empirical evidence on financial awareness and barriers among Filipino young professionals, which can inform the user profiling module of Odin. The identified motivating factors, such as family security and workplace influence, can guide engagement strategies and feature design. The finding that cost is a primary barrier suggests that Odin should prioritize clear communication of costs and benefits. The correlation between awareness and motivation underscores the importance of financial literacy features within the app."
  directly_justifies:
    - "Young Filipino professionals exhibit high awareness but moderate adoption of financial protection products, indicating an awareness-adoption gap."
    - "Cost overestimation is a significant barrier to adoption of financial products."
    - "Family security is the strongest motivator for financial decisions among Filipino young professionals."
    - "Workplace-based financial programs increase willingness to adopt financial products."
  limits:
    - "Focuses on life insurance rather than general PFMS, limiting direct applicability to budgeting or expense tracking."
    - "Sample limited to one university, may not generalize to all Filipino young professionals."
    - "No algorithmic or design-specific insights for PFMS modules."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant for demographic (1.A) and financial behavior (1.C) domains due to its direct survey of young Filipino professionals and analysis of their financial perceptions. Cultural practice (2.A) was selected as medium relevance because family security emerged as a key motivator. User trust (10.B) was selected as medium because trust barriers were measured. Domains related to expense categorization (3.A-C), existing systems (4.A-B), behavioral profiling (5.A-C) were considered but rejected because the paper does not address classification, profiling, or system evaluation; it only describes variables. Forecasting, budgeting, anomaly detection, mobile design, privacy, retention, evaluation, and savings/debt management domains were rejected as the paper does not cover these topics. Borderline cases included 5.A (behavioral profiles) and 11.A (engagement), but the paper does not provide profile classifications or app engagement insights, so they were excluded. Overall, the paper provides contextual and behavioral background for Odin's user understanding, but lacks direct algorithmic or design contributions."
limitations:
  - "Sample size (98) and single institution limit generalizability."
  - "Reliability testing not conducted; instrument adapted but not re-validated [unacknowledged]."
  - "Cross-sectional design prevents causal inference."
  - "Self-reported data may introduce social desirability bias [unacknowledged]."
remember_this:
  - "Awareness of life insurance is high among young Filipino professionals but ownership is moderate."
  - "Cost overestimation is the main barrier to adoption."
  - "Family security is the strongest motivator for financial decisions."
  - "Higher awareness correlates with stronger motivation and fewer perceived barriers."
  - "Workplace support can increase willingness to adopt financial protection."
```
---

## Paper 16: Abila & Ulibas_summarized.md

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

## Paper 17: Jandoc et al_summarized.md

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

## Paper 18: Delos Santos et al_summarized.md

**Source File:** `Delos Santos et al_summarized.md`

```yaml
paper_id: 10.4898/jener.v2i3.a32
designation: local
title: Budgeting Practices and Challenges of Micro-Entrepreneurs in Maria Aurora Public Market: Toward a Strategic Management Plan
authors: Delos Santos, D. T.; Austria, M. G. P.; Candelario, C. C.; Garcia, L. E. B.; Gonaranao, B. S.
year: 2026
venue: JENER Journal of Empirical and Non-Empirical Research
odin_topics:
  - "1.C"
  - "3.A"
  - "4.A"
  - "4.B"
  - "7.A"
  - "13.A"
tldr: Micro-entrepreneurs exhibit high discipline in budgeting but face major challenges from financial liabilities and income volatility.
problem_and_motivation: Micro-entrepreneurs in developing economies often lack formal budgeting systems, hindering growth and increasing vulnerability to economic shocks. In the Philippines, MSMEs are vital to the economy, yet many do not use formal budgeting despite recognizing its importance. A specific gap exists in understanding the financial practices and challenges of micro-entrepreneurs in local public markets like Maria Aurora.
approach:
  - A quantitative research design using a structured survey questionnaire was employed.
  - Data were gathered from 68 randomly sampled micro-entrepreneurs in the Maria Aurora Public Market.
  - The survey measured budgeting practices across four dimensions: income utilization, expense tracking, savings, and financial planning.
  - Challenges were assessed in terms of financial liability and income generation.
  - Descriptive statistics, including frequency, percentage, and weighted means, were used for analysis.
findings:
  - "num: Overall budgeting practices were rated as Always with an AWM of 3.63 for income utilization."
  - "num: Financial planning had an AWM of 3.57, indicating a proactive and goal-oriented approach."
  - "num: The highest-ranked practice was setting financial goals for the business (AWM 3.77)."
  - "num: The lowest-ranked budgeting practice was depositing savings in a bank or cooperative (AWM 3.22)."
  - "num: Expense tracking showed an AWM of 3.48, with a gap in categorizing costs into fixed and variable (AWM 3.20)."
  - "num: Financial liability was a major challenge (AWM 3.27), with managing multiple obligations being the most pressing (AWM 3.42)."
  - "num: Income generation was also a major challenge (AWM 3.40), primarily due to economic changes like inflation (AWM 3.48)."
  - Micro-entrepreneurs excel at separating business and personal funds but struggle with formal banking and cost categorization.
  - External economic pressures and lack of affordable financing are significant barriers to growth.
key_figures_tables:
  - "Table 1: Budgeting practices in terms of income utilization → High discipline with an overall AWM of 3.63."
  - "Table 2: Budgeting practices in terms of expense tracking → Diligent recording but weak cost categorization."
  - "Table 3: Budgeting practices in terms of savings → Strong saving culture, but low engagement with formal banks."
  - "Table 4: Budgeting practices in terms of financial planning → Strong goal-setting, but weaker forecasting skills."
  - "Table 5: Challenges in financial liability → Multi-indebtedness is a major hindrance to budgeting."
  - "Table 6: Challenges in income generation → Economic volatility is the primary concern."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "AWM"
    definition: "Average Weighted Mean, a descriptive statistic used to interpret survey responses."
  - term: "MSMEs"
    definition: "Micro, Small, and Medium Enterprises, which form the backbone of the Philippine economy."
  - term: "Paluwagan"
    definition: "An informal rotating savings group common in the Philippines."
critical_citations:
  - "[Barbosa, 2022] — Highlights the gap between awareness and practice of formal budgeting among Filipino micro-entrepreneurs."
  - "[Dela Cerna, 2025] — Provides a framework for assessing budgeting practices of micro-business owners."
  - "[World Bank, 2019] — Identifies limited credit access as a leading cause of financial exclusion."
relevance:
  topics:
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "contextual"
      justification: "Focuses on micro-entrepreneurs, not young professionals, but reveals general financial behavior patterns in the Philippines."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "medium"
      justification: "Identifies a gap in cost categorization (fixed vs. variable), which is relevant to designing expense tracking features."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Describes current practices (often informal), providing a baseline for understanding the user's starting point."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Specifically highlights the lack of formal budgeting, poor record-keeping, and limited banking integration as key gaps."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "medium"
      justification: "Provides evidence of common budgeting practices (income utilization, expense tracking) and challenges (debt), informing system design."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "low"
      justification: "Discusses savings behaviors, including the use of informal methods and challenges with formal savings, but not focused on goal management."
  contribution: "This paper justifies Odin's design by revealing the prevalent financial behaviors and challenges in the Philippines. It confirms the need for modules that simplify expense tracking (3.A) and emphasize goal-setting (7.A). The paper's findings on debt and income instability (7.A, 13.A) support the need for robust features in these areas. It also validates a mobile-first approach (9.A) by illustrating the low use of formal banking and the potential for accessible digital tools."
  directly_justifies:
    - "A structured expense tracking module with automatic categorization is needed because manual cost categorization is a known weakness."
    - "Budget recommendation must account for irregular income and provide strategies for managing financial liabilities."
    - "A system that promotes formal savings integration is necessary to bridge the gap between high saving motivation and low banking engagement."
  limits: "The sample is limited to one public market (Maria Aurora), which may not be representative of all Filipino micro-entrepreneurs. The study is purely quantitative and lacks qualitative depth to explain the 'why' behind the behaviors and challenges. [unacknowledged] It does not explore the specific role or potential of digital tools as a solution."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was conducted. The domains flagged as relevant are 'Expense Categorization' (topic 3.A), 'Existing Systems & Gaps' (topics 4.A, 4.B), 'Budget Recommendation' (topic 7.A), and 'Savings & Debt Management' (topic 13.A). Topic 3.A was assigned 'medium' relevance as the paper identifies a specific gap in cost categorization. Topics 4.A and 7.A were deemed 'medium' and 'contextual' respectively, as they provide valuable background on current practices and challenges. Topic 13.A was rated 'low' relevance because while savings behavior is discussed, it does not directly address goal management. The domains of 'Behavioral Profiling', 'Spending Forecasting', 'Anomaly Detection', 'Mobile-First Design', 'Data Privacy', and 'User Retention' were rejected as the paper does not provide any citeable claims that directly inform their design or implementation. A borderline case was observed where the paper's discussion of 'income utilization' touches on both 'Financial Behavior' (1.C) and 'Budgeting Strategies' (7.A); it was resolved by selecting the more design-relevant topic (7.A) over the more descriptive one (1.C). The paper's discussion of 'savings' (13.A) and 'financial liability' (7.A) presents another borderline issue; both were selected, but with differing relevance levels to reflect the paper's primary focus. Overall, the paper is highly relevant to Odin as it provides empirical evidence of the financial management practices and challenges of Filipino micro-entrepreneurs, which can directly inform the design of features for expense tracking, budgeting, and debt management."
limitations:
  - "The sample was limited to 68 micro-entrepreneurs from a single public market, limiting generalizability. [unacknowledged]"
  - "The study relies on self-reported data, which may be subject to social desirability bias."
  - "The cross-sectional design does not capture how practices and challenges evolve over time. [unacknowledged]"
  - "A purely quantitative approach cannot fully explain the reasons behind observed behaviors and challenges."
  - "The paper does not explicitly examine the role of digital financial tools, a gap for a modern PFMS context. [unacknowledged]"
remember_this:
  - "Micro-entrepreneurs show strong daily financial discipline but lack formal banking integration."
  - "Managing multiple financial obligations and income volatility are the top challenges."
  - "A key gap exists in categorizing expenses into fixed and variable costs."
  - "Despite a proactive saving culture, the use of formal banks or cooperatives is low."
  - "Financial literacy and access to affordable credit are critical for business sustainability."
```
---

## Paper 19: Bayangos & Lubangco_summarized.md

**Source File:** `Bayangos & Lubangco_summarized.md`

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

## Paper 20: Lopez_summarized.md

**Source File:** `Lopez_summarized.md`

```yaml
paper_id: b7a8f3c2-d4e5-4f6a-8b9c-0d1e2f3a4b5c
designation: local
title: "Beyond the Beach: A Secondary Data Analysis of Micro-Entrepreneurship Survival Strategies in Philippine Tourism Enclaves During Economic Disruption"
authors: "Lopez, A."
year: 2026
venue: "Unknown"
odin_topics:
  - "2.A"
  - "2.B"
  - "2.D"
  - "4.B"
tldr: "Philippine tourism micro-entrepreneurs deploy culturally embedded survival strategies against recurring disruptions, but policy formalization bias systematically excludes the most vulnerable from institutional support."
problem_and_motivation: "Tourism micro-entrepreneurs in Philippine enclaves face recurring disruptions that deplete adaptive capacity, yet their survival strategies remain underexplored, leaving policy responses misaligned with their needs."
approach:
  - "Qualitative secondary data analysis (QSDA) of peer-reviewed academic publications, government reports, and institutional studies from 2013 to 2024."
  - "Thematic analysis and cross-case synthesis were applied to identify patterns across disruption types and destination contexts."
  - "Data sources include academic journals, government reports (DOT, DTI, DOLE), and institutional studies (ADB, ILO, PIDS)."
  - "An interpretivist paradigm guides the analysis, focusing on meaning-making and contextual interpretation of documentary evidence."
  - "The study constructs a four-quadrant survival strategy typology organized by temporal and resource-orientation axes."
findings:
  - "The secondary data documents six major disruption events across 2013-2024, with compound effects from overlapping shocks."
  - "Survival strategies include operational contraction, livelihood diversification, social capital activation (utang na loob, bayanihan, paluwagan), and institutional engagement."
  - "A four-quadrant typology reveals a resilience trap: the most vulnerable operators are confined to short-term strategies and excluded from transformative adaptation."
  - "num: only 38% of tourism micro-enterprises in surveyed destinations held valid business permits, limiting relief access."
  - "num: women-owned micro-enterprises were 40% more likely to activate kinship credit but 35% less likely to access formal microfinance."
  - "The policy landscape is fragmented and formalization-biased, with disbursement delays rendering assistance post-crisis for many operators."
key_figures_tables:
  - "Table 3: Major economic disruptions affecting Philippine tourism micro-entrepreneurs, 2013-2024 → lists six disruption events with impacts."
  - "Table 4: Four-quadrant typology of survival strategies → organizes strategies by temporal and resource orientation."
  - "Table 5: Mediating variables and their effects on survival strategy access → shows how geography, sector, gender, etc. mediate outcomes."
  - "Table 6: Policy gap analysis for tourism micro-enterprise support → identifies gaps in relief, credit, formalization, skills, and LGU coordination."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Utang na loob"
    definition: "Debt of gratitude; informal credit and support networks based on reciprocal obligation."
  - term: "Bayanihan"
    definition: "Community solidarity; collective mobilization of labor and resources for shared goals."
  - term: "Paluwagan"
    definition: "Informal rotating savings and credit association for accumulating lump-sum capital."
  - term: "QSDA"
    definition: "Qualitative Secondary Data Analysis; systematic analysis of existing qualitative data."
  - term: "MSME"
    definition: "Micro, Small and Medium Enterprises; Philippine classification for small businesses."
critical_citations:
  - "[Dahles & Bras, 1999] — Foundational work on tourism micro-entrepreneurship in developing Asia."
  - "[Doern et al., 2019] — Framework for firm-level responses to economic crises."
  - "[Chambers & Conway, 1992] — Sustainable Livelihoods Framework for understanding asset-based adaptation."
  - "[Hart, 1973] — Foundational theory on informal economy and its dynamics."
relevance:
  topics:
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "high"
      justification: "Paper details utang na loob, bayanihan, and paluwagan as key survival mechanisms."
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "medium"
      justification: "Documents tourism seasonality and disruption cycles affecting income and spending."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "medium"
      justification: "Discusses disruptions to tourism-driven spending cycles and community solidarity."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "contextual"
      justification: "Analyzes government policy gaps but not PFMS-specific systems."
  contribution: "The paper's documentation of culturally specific financial practices (utang na loob, bayanihan, paluwagan) can inform Odin's behavioral profiling and user engagement design. Its analysis of cyclical disruption patterns provides context for spending forecasting modules. The policy gap analysis on formalization bias and relief exclusion offers lessons for designing inclusive, trust-building features. The resilience trap concept highlights the need for adaptive system responses to user vulnerability. Overall, the paper provides empirical grounding for understanding Filipino financial behavior in informal and crisis contexts."
  directly_justifies:
    - "Culturally embedded social capital is critical for financial resilience in Filipino contexts."
    - "Sequential disruptions progressively deplete adaptive capacity, requiring dynamic modeling."
    - "Formalization bias excludes the most vulnerable from institutional support."
  limits:
    - "Geographic concentration in Boracay and Palawan limits generalizability to other Philippine destinations."
    - "Secondary data quality varies, with some government reports lacking methodological transparency."
    - "Causal relationships cannot be established; findings are associative patterns."
    - "Rapid policy changes may supersede some institutional findings."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was conducted. The domains flagged as relevant were: Filipino Cultural Context (2.A, 2.B, 2.D) and Existing Systems & Gaps (4.B). 2.A received 'high' relevance due to detailed treatment of utang na loob, bayanihan, and paluwagan as survival strategies. 2.B and 2.D received 'medium' because the paper addresses tourism seasonality and disruption cycles, which relate to spending patterns. 4.B received 'contextual' because it discusses government policy gaps but not PFMS-specific systems. Borderline cases: the paper touches on debt (13.B) but only informally, not in PFMS context; savings (13.A) is mentioned but as enterprise survival, not personal savings. Domains such as expense categorization, forecasting, anomaly detection, mobile design, and system evaluation were rejected because the paper does not address algorithmic or PFMS design considerations. Overall, the paper is contextually relevant for understanding Filipino financial behavior and cultural practices, but not directly applicable to algorithmic modules."
limitations:
  - "Reliance on secondary data means findings reflect prior interpretations, not direct experience."
  - "Geographic coverage is uneven, with Boracay and Palawan overrepresented. [unacknowledged]"
  - "Causal relationships cannot be established; only associative patterns are identified."
  - "Rapid policy changes may supersede some institutional findings. [unacknowledged]"
remember_this:
  - "Culturally embedded social capital is critical for micro-enterprise survival in the Philippines."
  - "Sequential disruptions progressively deplete adaptive capacity, worsening vulnerability."
  - "Formalization bias in government relief excludes most vulnerable micro-entrepreneurs."
  - "Women-operated micro-enterprises face compound disadvantages in accessing support."
  - "Policy responses must address multiple vulnerability dimensions simultaneously."
```
---

## Paper 21: Am-una_summarized.md

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

## Paper 22: Santos_summarized.md

**Source File:** `Santos_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: local
title: "The Future of Work: Gig Economy and Emerging Employment Patterns"
authors: "Santos, M."
year: 2026
venue: "Social Innovation and Development in Asia"
odin_topics:
  - "1.A"
  - "1.B"
  - "1.C"
tldr: "Examines the paradox of flexibility and insecurity in Southeast Asia's gig economy, highlighting income volatility and lack of social protections for young workers."
problem_and_motivation: "The rapid expansion of platform-based gig work in Southeast Asia offers income opportunities but lacks adequate labor protections. This creates systemic vulnerabilities for young workers, especially in countries like the Philippines, Indonesia, and Malaysia. The study addresses the gap in empirical research on the region's distinctive gig economy characteristics."
approach:
  - "Conducted a mixed-methods study across the Philippines, Indonesia, and Malaysia."
  - "Surveyed 500 gig workers aged 18-35 online in 2023 about income, hours, satisfaction, and benefits."
  - "Conducted semi-structured interviews with 30 gig workers, 10 per country, for qualitative insights."
  - "Analyzed case study data from each country to compare varying levels of digital economy maturity."
  - "Focused on platform-based employment in ride-hailing, food delivery, and online freelancing."
findings:
  - "num: Filipino freelancers report volatile earnings from $200 to $1,000 per month."
  - "num: Indonesian ride-hailing drivers work 10-12 hours daily with net incomes marginally above minimum wage."
  - "Gig work offers autonomy but institutionalizes precarity due to a lack of traditional labor rights."
  - "Algorithmic management creates new forms of dependency and erodes worker autonomy in practice."
  - "Gig economy participation is not limited to low-income workers, with middle-class youth in Malaysia also involved."
  - "Lack of career pathways prevents workers from transitioning to stable full-time employment."
key_figures_tables:
  - "None."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Gig Economy"
    definition: "A labor market characterized by short-term contracts or freelance work as opposed to permanent jobs."
  - term: "Algorithmic Management"
    definition: "The use of software algorithms to allocate work, monitor performance, and discipline workers on digital platforms."
critical_citations:
  - "[De Stefano, 2016] — Defines the just-in-time workforce and labor protection issues."
  - "[Prassl & Risak, 2017] — Analyzes platforms as employers and the legal classification of gig workers."
  - "[Kalleberg & Vallas, 2018] — Discusses job insecurity and the lack of career advancement in precarious work."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "high"
      justification: "Directly studies young gig workers (18-35) in the Philippines and Southeast Asia."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "high"
      justification: "Provides concrete data on income volatility and lack of benefits for young Filipino freelancers."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "medium"
      justification: "Highlights financial instability and reliance on family networks due to gig work."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "contextual"
      justification: "Mentions reliance on family networks for security, a culturally relevant financial practice."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "low"
      justification: "The paper does not explicitly address seasonal spending or cultural occasions."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "contextual"
      justification: "Discusses gaps in social protection systems but not specifically PFMS."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "low"
      justification: "The paper discusses income volatility which affects savings capacity but not PFMS features."
  contribution: "This paper provides a foundational understanding of the financial instability and lack of social protections experienced by Filipino gig workers. Its findings directly justify Odin's need for robust income volatility management features and flexible budget recommendation modules. The study emphasizes the importance of designing for users with irregular income, a core assumption for Odin's approach to behavioral profiling and savings management. It also underscores the cultural context of relying on family networks, which Odin's design should consider."
  directly_justifies:
    - "Young Filipino gig workers experience volatile monthly earnings from $200 to $1,000."
    - "Lack of social protections forces reliance on family networks for financial security."
    - "Gig workers often lack career pathways, leading to long-term financial uncertainty."
  limits:
    - "Focuses on the Philippines, Indonesia, and Malaysia, limiting generalizability to other ASEAN countries."
    - "Survey sample size of 500 is relatively small for a regional study."
    - "Does not evaluate the effectiveness of proposed policy solutions. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domain of 'Filipino Cultural Context' was flagged via topic 1.A (Filipino Young Professionals), as the paper directly profiles this demographic. Topic 1.B (Financial Structure) was identified as highly relevant due to specific data on income structures. Topic 1.C (Financial Behavior) was assessed as medium relevance because the paper discusses the resulting financial behaviors like instability. The 'Existing Systems & Gaps' domain was considered but only topic 4.B (Limitations) was deemed contextual, as the paper addresses broader social protection gaps, not PFMS-specific limitations. All other domains, such as 'Spending Forecasting', 'Budget Recommendation', and 'Anomaly Detection', were rejected as the paper contains no algorithmic, forecasting, or system-design content relevant to Odin. Overall, the paper provides critical demographic and financial-context data but has no direct technical or design relevance to Odin's algorithmic modules."
limitations:
  - "Focuses on the Philippines, Indonesia, and Malaysia, limiting generalizability to other ASEAN countries."
  - "Survey sample size of 500 is relatively small for a regional study."
  - "Does not evaluate the effectiveness of proposed policy solutions. [unacknowledged]"
remember_this:
  - "Filipino gig workers' income fluctuates between $200 and $1,000 monthly."
  - "The gig economy provides flexibility but erodes traditional labor protections."
  - "Southeast Asian gig workers lack portable social benefits across platforms."
  - "Algorithmic management creates new dependencies for gig workers."
```
---

## Paper 23: Aquino et al_summarized.md

**Source File:** `Aquino et al_summarized.md`

```yaml
paper_id: 10.69569/jip.2025.758
designation: local
title: "A Systematic Literature Review: Present Bias versus Financial Literacy as Determinants of Savings Behavior Among Entrepreneurs"
authors: "Aquino, E. J.; Sealmoy, R.; Mandap, O."
year: 2026
venue: "Journal of Interdisciplinary Perspectives"
odin_topics:
  - "5.A"
  - "13.A"
  - "1.C"
  - "7.A"
tldr: "Present bias consistently predicts lower savings among entrepreneurs, while financial literacy's impact is conditional on self-control, according to a systematic review of 20 studies (2020-2025)."
problem_and_motivation: "Despite policy emphasis on financial literacy, entrepreneurs often fail to save, indicating behavioral barriers may outweigh knowledge. Prior reviews have not systematically compared the relative predictive power of financial literacy and present bias on entrepreneurial savings. This review addresses that gap by synthesizing evidence from 2020 to 2025."
approach:
  - "The review followed PRISMA 2020 guidelines for transparency and reproducibility."
  - "Searches were conducted in Google Scholar, Scopus, and Web of Science using Boolean keywords."
  - "Inclusion criteria required peer-reviewed English articles with JIF ≥1.5, focused on entrepreneurs or entrepreneurial populations."
  - "Two independent reviewers screened titles and abstracts, with disagreements resolved through discussion."
  - "Methodological quality was appraised using JBI and CASP checklists."
  - "Data extraction covered financial literacy measures, present-bias indicators, savings outcomes, and sample characteristics."
  - "Findings were synthesized thematically to compare predictive strength of literacy versus bias."
findings:
  - "Financial literacy's impact on savings is conditional and often negligible without self-control."
  - "Present bias consistently leads to impulsive spending and reduced savings among entrepreneurs."
  - "Behavioral factors frequently override financial knowledge in savings decisions."
  - "Self-control moderates the relationship between financial literacy and savings behavior."
  - "The review includes 20 peer-reviewed studies with a majority using primary data and regression analysis."
key_figures_tables:
  - "Figure 1: Theoretical framework contrasting Financial Literacy and Behavioral Bias pathways → present bias directly reduces savings."
  - "Figure 2: PRISMA flow diagram showing study selection process → 20 studies included after screening."
  - "Table 1: Journal impact factors of source journals → included journals have high impact factors (up to 8.6)."
  - "Table 2: Distribution of sampled articles by journal and year → research peaks in 2022 with 5 articles."
  - "Table 3: Sources of data (primary/secondary, sample sizes) → 78% of studies used primary data."
  - "Table 4: Statistical treatments used → regression analysis is most common (37% of studies)."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "PRISMA"
    definition: "Preferred Reporting Items for Systematic Reviews and Meta-Analyses"
  - term: "JBI"
    definition: "Joanna Briggs Institute"
  - term: "CASP"
    definition: "Critical Appraisal Skills Programme"
  - term: "RCT"
    definition: "Randomized Controlled Trial"
  - term: "SEM"
    definition: "Structural Equation Modeling"
  - term: "SME"
    definition: "Small and Medium Enterprise"
critical_citations:
  - "[Loewenstein & Carbone, 2024] — reframes self-control as emotional struggle."
  - "[Mpaata et al., 2021] — literacy improves savings only with high self-control."
  - "[McKenzie et al., 2022] — present bias drives impulsive spending."
  - "[Alshebami & Al Marri, 2022] — literacy predicts entrepreneurial intention but not savings directly."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "The paper directly compares present bias and financial literacy as predictors of savings, informing behavioral profiling."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "high"
      justification: "Savings behavior is the primary outcome variable, with implications for goal management."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "medium"
      justification: "The review includes multiple Philippine studies on entrepreneurs and millennials, providing local behavioral insights."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "medium"
      justification: "Financial literacy is a form of budgeting knowledge, and the paper shows its conditional effectiveness."
  contribution: "The paper justifies integrating behavioral interventions such as commitment devices and automated savings into Odin's savings module (13.A). It supports the use of behavioral profiling (5.A) to tailor interventions based on present bias. The finding that financial literacy alone is insufficient informs the design of budget recommendation (7.A) that incorporates self-control cues. The paper also underscores the need for user engagement strategies to overcome present bias."
  directly_justifies:
    - "Present bias consistently leads to impulsive spending and reduced savings among entrepreneurs."
    - "Financial literacy improves savings only when combined with high self-control."
    - "Behavioral factors frequently override financial knowledge in savings decisions."
    - "Self-control moderates the relationship between financial literacy and savings behavior."
  limits:
    - "Reliance on cross-sectional studies limits causal inference."
    - "Most studies are concentrated in Asian contexts, reducing generalizability."
    - "Few studies directly compare financial literacy and present bias within a single analytical framework."
    - "The review did not include experimental designs beyond the few RCTs."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The domains of Behavioral Profiling & Classification (5.A, 5.B, 5.C) and Savings & Debt Management (13.A, 13.B, 13.C) were flagged as highly relevant because the paper directly examines predictors of savings behavior and provides evidence for behavioral profiling. The Filipino Cultural Context domains (2.A, 2.B, 2.C, 2.D) were considered; 2.D (spending cycles) was borderline due to impulsive spending discussions but not explicitly about cyclical occasions, so only 1.C (Financial Behavior) was selected as medium due to inclusion of Philippine studies. Expense Categorization (3.A-C) and Existing Systems (4.A-B) were rejected as the paper does not address categorization or system evaluation. Forecasting (6.A-B) and Anomaly Detection (8.A-C) were not applicable. Mobile-First Design (9.A-B) and Data Privacy (10.A-B) were also not relevant. The paper's focus on behavioral versus knowledge factors directly supports Odin's need for behavioral interventions, making it highly relevant for modules 5.A and 13.A."
limitations:
  - "Most studies are cross-sectional, limiting causal inference."
  - "Geographic concentration in Asia reduces generalizability to other regions."
  - "Few studies directly compare financial literacy and present bias in a single analytical framework."
  - "The review relies on self-reported measures of financial literacy and savings behavior."
remember_this:
  - "Present bias is a stronger predictor of poor savings than financial literacy."
  - "Financial literacy requires self-control to translate into savings."
  - "Integrated behavioral and educational interventions are more effective."
  - "Most evidence is cross-sectional and Asian, limiting causality."
  - "Knowledge alone is insufficient to change savings behavior."
```
---

## Paper 24: Gudelosao et al_summarized.md

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

## Paper 25: Montuerto & Ferrater-Gimena_summarized.md

**Source File:** `Montuerto & Ferrater-Gimena_summarized.md`

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
---


---

## Agent Instruction

If the agent reading this document believes further context about a paper is needed, it may request the original converted markdown file (with the '_marked' suffix) from the user for the relevant paper(s).
