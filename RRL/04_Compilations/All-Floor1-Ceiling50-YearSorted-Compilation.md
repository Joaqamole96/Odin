# Compiled Research Summaries

**Total Papers:** 50

**Note:** Included papers positions 1 to 50, Sorted by year.

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

## Paper 3: Ayari et al_summarized.md

**Source File:** `Ayari et al_summarized.md`

```yaml
paper_id: 10.1007/s10462-025-11416-2
designation: international
title: Machine learning powered financial credit scoring: a systematic literature review
authors: Ayari, H.; Guetari, R.; Kraïem, N.
year: 2026
venue: Artificial Intelligence Review
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
  - 12.C
tldr: A systematic review of 63 studies on machine learning credit scoring identifies ensemble and hybrid models as most accurate, with key challenges in interpretability, bias, and alternative data integration.
problem_and_motivation: Traditional credit scoring models rely on narrow features and linear assumptions, limiting their effectiveness for non-traditional borrowers. There is a need to systematically synthesize recent ML advancements to guide practitioners and researchers. This review addresses the gap by providing a comprehensive and structured analysis of ML methods, trends, and challenges for credit scoring.
approach:
  - Conducted a systematic literature review following PRISMA 2020 guidelines, searching four major digital libraries (Springer, ACM, IEEE, Google Scholar).
  - Analyzed 330 initial papers, selecting 63 peer-reviewed studies from 2018-2024 after rigorous screening for empirical results and methodological transparency.
  - Extracted data on ML techniques, datasets, evaluation metrics, and performance results using a structured form and quality assessment checklist.
  - Categorized models into traditional ML, deep learning, and ensemble learning, including hybrid approaches within each category.
  - Applied science mapping methods, including bibliographic coupling and keyword co-occurrence, to identify thematic clusters and research trends.
  - Performed a comparative analysis of model performance on standard datasets (German, Australian, Japanese, Lending Club) and discussed challenges.
findings:
  - Ensemble and hybrid models, combining feature optimization and multiple classifiers, consistently outperform single classifiers across benchmark datasets.
  - num: On the German dataset, the GA+NN model achieved the highest accuracy (91.91%) and AUC (92.60%).
  - num: Deep learning models like CNNs show promise with large datasets but are less commonly applied due to interpretability challenges.
  - The use of alternative data sources (social media, mobile usage, psychometrics) is an emerging trend that can enhance predictive accuracy.
  - Interpretability techniques like SHAP and LIME are increasingly adopted to address the "black box" nature of complex ML models.
  - Key challenges in adopting ML for credit scoring include interpretability, potential biases, and the curse of dimensionality.
key_figures_tables:
  - Table 7: Performance comparison on German dataset → GA+NN achieves highest accuracy (91.91%) and AUC (92.60%).
  - Table 8: Performance comparison on Australian dataset → Multi-stage ensemble model achieves best accuracy (92.36%) and AUC (96.65%).
  - Table 9: Performance comparison on Japanese dataset → Multi-stage ensemble model achieves best accuracy (93.16%) and AUC (96.95%).
  - Figure 2: Comparative accuracy of ML models → Hybrid ML approaches demonstrate top performance with low variability.
  - Figure 5: Bibliographic coupling network → The literature is organized into three main clusters: traditional, ensemble, and deep learning approaches.
key_equations:
  - equation: "P(Y=1|x) = 1 / (1 + e^{-(β0 + β^T x)})"
    explanation: Logistic regression estimates probability of binary outcome for credit scoring.
  - equation: "Accuracy = (TP + TN) / (TP + TN + FP + FN)"
    explanation: Overall correctness of a classification model.
  - equation: "F1-Score = 2 × (Precision × Recall) / (Precision + Recall)"
    explanation: Harmonic mean of precision and recall for imbalanced datasets.
definitions:
  - term: AUC
    definition: Area Under the ROC Curve, measures model's ability to distinguish between classes.
  - term: G-Mean
    definition: Geometric mean of sensitivity and specificity, balances class performance.
  - term: KS
    definition: Kolmogorov-Smirnov statistic, measures model's discriminatory power in credit scoring.
  - term: SHAP
    definition: SHapley Additive exPlanations, a method to explain predictions by quantifying feature contributions.
  - term: LIME
    definition: Local Interpretable Model-agnostic Explanations, explains individual predictions using local approximations.
  - term: SMOTE
    definition: Synthetic Minority Over-sampling Technique, addresses class imbalance by generating synthetic samples.
critical_citations:
  - "[Dumitrescu et al., 2022] — Introduces PLTR, combining LR with decision-tree rules for interpretable non-linear credit scoring."
  - "[He et al., 2018] — Proposes an ensemble method adapting to varying class imbalance ratios using BalanceCascade and stacking."
  - "[Bao et al., 2019] — Demonstrates the value of integrating unsupervised learning with supervised models for credit risk assessment."
  - "[Hayashi, 2022] — Highlights the superior performance of Deep Belief Networks and challenges in DL interpretability."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: Provides a general overview of ML classification methods that could be adapted for expense categorization.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: contextual
      justification: Discusses feature selection and data preprocessing, relevant for designing effective categories.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Surveys existing credit scoring systems and their evolution, providing context for PFMS.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Explicitly details the limitations of traditional credit scoring (e.g., narrow features, linearity) which are relevant to PFMS gaps.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Reviews methods for classifying borrower creditworthiness, which parallels user behavioral profiling in PFMS.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Reviews ML classification techniques applicable to user profiling.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Central focus of the review; provides extensive evidence on forecasting methods for financial outcomes.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: Discusses LSTM networks for sequential data, relevant for spending prediction.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Discusses outlier detection methods in credit scoring, which can inform anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: Reviews outlier detection techniques that could be applied to spending data.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Identifies privacy concerns with alternative data and compliance with standards like GDPR and IFRS 9.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Emphasizes the need for interpretability and transparency to build trust, a core challenge for user adoption.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a comprehensive overview of evaluation metrics (accuracy, AUC, F1, KS) and their use in financial systems.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Compares performance of different ML algorithms, directly relevant for evaluating Odin's modules.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Discusses comparative evaluation of models, which can inform budget recommendation evaluation.
  contribution: "This systematic review provides a comprehensive synthesis of ML applications in credit scoring, offering a benchmark for selecting models and evaluation metrics for Odin's forecasting and classification modules. Its detailed analysis of ensemble and hybrid models directly informs the design of Odin's core algorithms for spending prediction and user profiling. The review's emphasis on interpretability and bias mitigation guides the development of trustworthy and fair recommendation and anomaly detection systems. Furthermore, its discussion of alternative data sources and privacy concerns offers a framework for responsibly expanding Odin's data inputs while maintaining user trust and regulatory compliance."
  directly_justifies:
    - "Ensemble and hybrid models consistently outperform single classifiers in credit scoring tasks."
    - "Interpretability techniques like SHAP and LIME are essential for building trust in financial AI systems."
    - "Model evaluation should use a combination of metrics (AUC, F1, KS) to address the limitations of accuracy on imbalanced data."
    - "Addressing algorithmic bias is critical for ensuring fair and non-discriminatory credit decisions."
    - "Alternative data sources can enhance predictive accuracy, particularly for users lacking formal financial histories."
  limits:
    - "The review does not provide a direct comparative analysis to identify the single most effective model due to heterogeneity in datasets and evaluation metrics across studies."
    - "The review may have missed relevant studies published outside the selected four digital libraries or within the 2018-2024 timeframe."
    - "The focus on credit scoring may limit the direct applicability of all findings to broader personal finance management functions like budget optimization."
  mapping_rationale: "A systematic scan across all 12 functional domains was conducted. The domains 'Expense Categorization' (3.A, 3.B) and 'Behavioral Profiling' (5.A, 5.C) were flagged as contextual/medium because the review provides general ML classification methods, but not specific to expense taxonomy or dynamic user profiling. 'Existing Systems & Gaps' (4.A, 4.B) was deemed high and medium, respectively, as the review explicitly outlines the evolution and limitations of traditional scoring models, directly informing Odin's need to address PFMS gaps. The 'Spending Forecasting' domain (6.A, 6.B) received high and medium relevance due to the review's core focus on predictive modeling and mention of LSTM for sequential data. 'Anomaly Detection' (8.A, 8.B) was considered contextual as the review touches on outlier detection but does not detail specific algorithms for spending data. 'Data Privacy & User Trust' (10.A, 10.B) was flagged as medium and high because the review extensively discusses interpretability, privacy concerns with alternative data, and regulatory compliance (GDPR, IFRS 9), which are critical for user trust. 'System Evaluation' (12.A, 12.B, 12.C) was given high relevance due to the review's comprehensive analysis of evaluation metrics and algorithmic comparison, directly supporting Odin's testing and validation. The domain 'Filipino Cultural Context' was rejected as the paper is an international review with no specific focus on Philippine culture or practices. 'User Retention & Engagement' and 'Savings & Debt Management' were also rejected as the review does not address user engagement strategies or specific debt management techniques. The paper's overall relevance is high for guiding the selection of forecasting and classification algorithms, evaluation methodologies, and addressing interpretability and privacy challenges in Odin."
limitations:
  - "The review is limited to studies published between 2018 and 2024, potentially omitting older foundational work. [unacknowledged]"
  - "The search strategy was confined to only four online databases, which may have led to the omission of relevant studies from other sources. [unacknowledged]"
  - "A direct comparative analysis to identify the most effective model is lacking due to the heterogeneity in datasets and evaluation metrics used across the reviewed studies. [acknowledged]"
  - "Heterogeneity in datasets and evaluation metrics across studies complicates direct performance comparisons."
remember_this:
  - "Ensemble and hybrid models are the most effective for financial classification tasks."
  - "Interpretability is a critical challenge for building trust in ML-based financial systems."
  - "Using a combination of metrics like AUC and F1 is essential for evaluating models on imbalanced data."
  - "Alternative data can improve credit scoring accuracy but raises significant privacy concerns."
  - "Addressing algorithmic bias is fundamental to ensuring fairness in automated financial decisions."
```
---

## Paper 4: John_summarized.md

**Source File:** `John_summarized.md`

```yaml
paper_id: 9f7b8a6c-5d4e-3b2a-1f0e-9d8c7b6a5f4e
designation: international-algorithm-specific
title: Fair and Explainable Credit-Scoring under Concept Drift: Adaptive Explanation Frameworks for Evolving Populations
authors: John, S.
year: 2026
venue: Unknown
odin_topics:
  - 2.B
  - 5.B
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 12.B
tldr: Adaptive SHAP frameworks improve explanation stability and fairness in credit scoring under concept drift without reducing predictive accuracy.
problem_and_motivation: Static explainability methods like SHAP become unstable and potentially unfair when concept drift alters the data distributions underlying credit-scoring models. Existing adaptive learning research focuses on restoring predictive accuracy, leaving the explanation layer outdated and unreliable. A mechanism is needed to maintain interpretive consistency and fairness as borrower populations evolve.
approach:
  - Uses a multi-year lending dataset from 2015 to 2024 with demographic, financial, and socioeconomic features.
  - Employs XGBoost for predictive modeling and applies three adaptive SHAP variants for explanation: drift-weighted adjustment, sliding background sampling, and Ridge surrogate recalibration.
  - Benchmarks adaptive methods against static SHAP using metrics for predictive performance (AUC, F1), explanation stability (cosine, Kendall tau), and fairness (demographic parity).
  - Conducts robustness tests including counterfactual perturbations, background sensitivity analysis, and proxy-variable detection.
  - Uses paired bootstrap confidence intervals and paired t-tests to confirm statistical significance of improvements.
findings:
  - Static SHAP explanations showed high cosine stability (0.991-0.998) but moderate rank stability (Kendall tau = 0.758-0.912) under drift.
  - num: Adaptive Method B (sliding window) achieved the highest stability with cosine ≈ 0.995 and Kendall τ ≈ 0.89 across years.
  - num: Method B reduced demographic parity difference by approximately 0.026 (95% CI: -0.035, -0.016, p < 0.05) compared to baseline.
  - num: Default rates increased from ~15% in 2015 to over 23% in 2024, indicating label drift.
  - Counterfactual tests showed valid monotonic responses: decreasing credit score by 10% increased default probability by 0.05.
key_figures_tables:
  - Figure 1: Loan default rate by year shows an increase from 15% to 23% over the study period, confirming label drift.
  - Figure 2: PSI for annual_income and credit_score shows steady increase, indicating covariate drift.
  - Figure 5: DPD over time by model for race shows fairness fluctuates with data drift, especially during 2020-2021.
  - Figure 7: DPD before and after Method B recalibration demonstrates a clear reduction in disparity.
  - Figure 13: Counterfactual perturbations show monotonic response, validating model logic and explanation reliability.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: SHAP
    definition: SHapley Additive exPlanations; a game-theoretic approach to explain model predictions by assigning importance to features.
  - term: Concept Drift
    definition: A change in the underlying data distribution over time, which can degrade model accuracy and interpretability.
  - term: Demographic Parity Difference
    definition: A fairness metric measuring the difference in positive prediction rates across demographic groups.
  - term: XGBoost
    definition: Extreme Gradient Boosting; an ensemble machine learning algorithm widely used for its handling of nonlinear interactions.
critical_citations:
  - "[Lundberg and Lee, 2017] — Foundation for SHAP as the static explanation baseline."
  - "[Gama et al., 2014] — Defines concept drift and notes the research gap in adaptive explainability."
  - "[Barocas et al., 2023] — Emphasizes that fairness requires continuous attention in evolving systems."
  - "[Slack et al., 2020] — Highlights adversarial vulnerability of static explanation tools."
relevance:
  topics:
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: The dataset includes multi-year economic cycles and recessionary periods, which relate to cyclical patterns.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: medium
      justification: Addresses how borrower profiles and feature importance shift over time, directly informing profile dynamics.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly evaluates predictive performance (AUC, F1) of XGBoost in a dynamic credit-scoring context.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: The study's longitudinal setup and evaluation of explanation stability over time are relevant to forecasting.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: The robustness and proxy-variable detection methods are relevant to identifying anomalous or biased feature influences.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: The adaptive frameworks are designed to detect and adjust for distributional shifts, akin to anomaly detection.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: While not the primary focus, the fairness and stability analysis addresses aspects of responsible data use.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: The paper discusses how stable and fair explanations build user trust and support regulatory compliance.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Directly compares the evaluation of adaptive explanation modules against a static baseline using specific metrics.
  contribution: This paper provides a framework for evaluating and improving explanation stability in dynamic environments, which can inform Odin's approach to maintaining transparent and fair spending forecasts. The adaptive SHAP methods offer a way to recalibrate feature attributions as user behavior evolves, supporting Odin's behavioral profiling and anomaly detection modules. The emphasis on fairness and stability aligns with Odin's need to build user trust and comply with data privacy expectations.
  directly_justifies:
    - Static SHAP explanations become unstable under concept drift, requiring adaptive methods for reliable interpretation.
    - Adaptive explanation frameworks can improve fairness metrics without degrading predictive accuracy.
    - Sliding-window background sampling is an effective strategy for maintaining explanation stability over time.
  limits:
    - The analysis focuses primarily on single-attribute fairness rather than intersectional demographic factors.
    - The study does not test the framework on live, real-world banking data with missing or delayed information.
    - The computational cost of SHAP-based methods may limit scalability in real-time applications.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant for predictive modeling (6.A, 6.B) and algorithmic evaluation (12.B) because it directly benchmarks model and explanation performance in a dynamic environment. It was assigned medium relevance for behavioral profiling (5.B) due to its focus on feature importance shifts over time, and for anomaly detection (8.A, 8.B) through its robustness tests against distributional changes. The domains of data privacy (10.A) and user trust (10.B) were considered and assigned medium to low relevance as the paper discusses them conceptually but does not propose specific technical mechanisms for Odin. Cultural context (2.B) is contextual, as the dataset reflects economic cycles. The mapping rationale concludes that while the paper's primary domain is credit scoring, its methodologies for adaptive explanation, stability evaluation, and fairness recalibration are directly transferable to Odin's budget recommendation and behavioral forecasting modules.
limitations:
  - SHAP-based analysis is computationally heavy, which could hinder scalability and real-time use in Odin. [unacknowledged]
  - The fairness assessment focuses mainly on single attributes (race, gender) rather than the intersectional factors common in real-world scenarios. [acknowledged]
  - The study does not test the adaptive framework on live, real-world banking data with missing information or delayed updates. [acknowledged]
remember_this:
  - Adaptive SHAP methods stabilize explanations under concept drift without harming predictive accuracy.
  - Sliding-window background sampling provides the most consistent improvements in explanation stability.
  - num: Adaptive recalibration reduced demographic parity difference by 0.026 compared to baseline.
  - Explanation and fairness must be maintained dynamically as data and user behavior evolve.
  - Reliable explanations support both regulatory compliance and user trust in financial systems.
```
---

## Paper 5: Liang et al_summarized.md

**Source File:** `Liang et al_summarized.md`

```yaml
paper_id: 10.48550/arXiv.2602.16131
designation: international-algorithm-specific
title: Learning Personalized Agents from Human Feedback
authors: Liang, K.; Kruk, J.; Qian, S.; Yang, X.; Bi, S.; Yao, Y.; Nie, S.; Zhang, M.; Liu, L.; Fernández Fisac, J.; Zhou, S.; Hosseini, S.
year: 2026
venue: Unknown
odin_topics:
  - 5.A
  - 5.B
 5.C
  - 6.A
  - 7.B
  - 8.A
  - 11.A
  - 12.A
  - 12.B
tldr: A continual personalization framework using explicit memory and dual pre- and post-action feedback channels enables agents to learn initial preferences and adapt to drift.
problem_and_motivation: Static personalization methods fail with new users, cannot learn from real-time corrective feedback, and cannot handle evolving user preferences. This limits the deployment of personalized AI agents in interactive settings.
approach:
  - Data is generated via two new benchmarks: embodied manipulation and online shopping with simulated personas.
  - The PAHF framework operationalizes a three-step loop: pre-action clarification, action execution, and post-action feedback integration.
  - Agents use a standard dense-retrieval memory backend (SQLite or FAISS) to store and retrieve preference notes.
  - Evaluation follows a four-phase protocol that separates initial preference learning from adaptation to persona shifts.
  - Baselines include No Memory, Pre-action Only, and Post-action Only to isolate the effect of each feedback channel.
findings:
  - num: Pre-action agents achieve substantially higher success on the first interaction, reducing initial personalization error by over 30% compared to no-memory baselines.
  - Pre-action Only agents are brittle under drift, with Phase 3 success rates failing to improve or even falling below the no-memory baseline.
  - Post-action feedback is essential for fast adaptation, enabling agents to recover to high Phase-4 success rates (e.g., 67.9% in embodied domain).
  - PAHF combines both strengths, achieving the highest success rates across all phases (e.g., 70.5% in embodied Phase 2, 70.3% in shopping Phase 4).
  - PAHF consistently achieves the lowest average cumulative personalization error (ACPE) across both domains and phases.
  - The combination of pre- and post-action feedback with explicit memory is critical for robust continual personalization.
  - Online shopping domain, with its conjunctive acceptance policies and near-miss distractors, is significantly more challenging than embodied manipulation.
key_figures_tables:
  - Figure 3: Embodied Phase 1 learning curves → Pre-action feedback prevents initial errors, PAHF achieves lowest ACPE.
  - Figure 4: Shopping Phase 3 learning curves → Post-action feedback enables steep recovery, PAHF matches Post-action Only in success but has lower ACPE.
  - Table 1: Evaluation success rates (%) for Phase 2 and 4 → PAHF achieves the highest or tied-highest success rates in all settings.
  - Figure 5: Embodied results with FAISS memory → PAHF consistently outperforms baselines, confirming robustness to memory backend.
key_equations:
  - equation: Mˆ′_t = Fpre_update(Mˆ_t, I_t, O_t, m_t, q_t, fpre_t)
    explanation: Pre-action update function integrating clarification feedback.
  - equation: a_t = π_act(I_t, O_t, m_t, q_t, fpre_t)
    explanation: Action policy synthesizing instruction, observation, and retrieved preferences.
  - equation: Mˆ_{t+1} = Fpost_update(Mˆ′_t, I_t, m_t, q_t, fpre_t, a_t, fpost_t)
    explanation: Post-action update function integrating corrective feedback after an error.
definitions:
  - term: PAHF
    definition: Personalized Agents from Human Feedback, a continual personalization framework.
  - term: ACPE
    definition: Average Cumulative Personalization Error, the average error rate over iterations.
  - term: RAG
    definition: Retrieval-Augmented Generation, a technique for enhancing LLM outputs with retrieved information.
  - term: FF
    definition: Feedback Frequency, the proportion of tasks using any human feedback.
  - term: SR
    definition: Success Rate, the fraction of tasks completed correctly.
  - term: ReAct
    definition: A framework for LLMs to interleave reasoning and acting.
critical_citations:
  - "[Chhikara et al., 2025] — Production-ready memory for AI agents."
  - "[Salemi et al., 2024a] — Optimization for retrieval-augmented personalization."
  - "[Qiu et al., 2025] — Bayesian teaching for LLM probabilistic reasoning."
  - "[Li et al., 2025] — Benchmarks for interactive preference discovery."
  - "[Liang et al., 2025a] — Hindsight simulation mitigates RLHF misalignment."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly models user personas with idiosyncratic and context-dependent preferences.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: high
      justification: Addresses learning from scratch for new users and adapting to preference drift.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Provides a framework (PAHF) for dynamically updating profiles via feedback.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: The framework's memory and feedback mechanism could inform forecasting by tracking preference changes.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: The concept of learning user preferences from feedback is broadly relevant to personalization in PFMS.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: The post-action feedback mechanism could conceptually inform anomaly detection by identifying unexpected or corrected actions.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: contextual
      justification: The feedback loop is designed for live interaction, a core engagement dynamic.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Proposes a four-phase evaluation protocol for continual personalization.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Empirically evaluates the PAHF algorithm against baselines on two benchmarks.
  contribution: PAHF provides a general framework and evaluation protocol for continual personalization that can be directly applied to Odin's behavioral profiling module (5.A, 5.B) to learn user financial profiles from scratch. Its evaluation methodology (12.A, 12.B) offers a template for testing Odin's algorithmic components like forecasting or anomaly detection under user preference drift. The framework's emphasis on explicit memory and corrective feedback (5.C) provides a design pattern for building Odin's user model that adapts to changing financial behaviors.
  directly_justifies:
    - "Explicit memory combined with dual feedback channels is critical for robust personalization without pre-existing user data."
    - "Pre-action clarification prevents initial personalization errors caused by partial observability."
    - "Post-action feedback is essential for correcting miscalibrated beliefs under preference drift."
    - "The four-phase evaluation protocol separately quantifies initial learning and adaptation to drift."
  limits:
    - "The memory architecture is deliberately simple; more sophisticated backends could improve scalability."
    - "The framework does not explicitly handle inconsistent or noisy human feedback."
    - "The benchmarks, especially online shopping, remain challenging for agents."
    - "The agent is limited to at most one clarification question per task, increasing difficulty."
  mapping_rationale: A systematic scan of all 12 functional domains was performed. The paper is most directly relevant to Behavioral Profiling (5.A, 5.B, 5.C) and System Evaluation (12.A, 12.B) due to its focus on learning user personas from scratch and adapting to drift, and its proposed evaluation protocol. It was considered for Spending Forecasting (6.A) and Budget Recommendation (7.B) given its personalization focus, but assigned low relevance as it does not address financial data or budget optimization specifically. The domains of Filipino Cultural Context (2.A-D), Expense Categorization (3.A-C), Existing Systems (4.A-B), Mobile-First Design (9.A-B), Data Privacy (10.A-B), Savings & Debt Management (13.A-C) were rejected as the paper does not address these topics. The paper's theoretical and empirical results on continual personalization provide a strong foundation for Odin's user modeling and evaluation components.
limitations:
  - "The memory architecture is deliberately simple and may not scale to complex user histories. [unacknowledged]"
  - "The framework assumes human feedback is truthful and noise-free. [unacknowledged]"
  - "The online shopping domain remains challenging, with even PAHF achieving only ~70% success in Phase 4."
  - "The agent is limited to a single clarification question per task, which may be insufficient for complex preference elicitation."
remember_this:
  - "PAHF uses explicit memory and dual feedback channels for continual personalization."
  - "Pre-action feedback reduces initial errors by resolving ambiguity before acting."
  - "Post-action feedback is essential for correcting confidently wrong beliefs after preference drift."
  - "PAHF achieves 70.5% success in embodied tasks and 70.3% in shopping tasks after drift."
  - "The combination of pre- and post-action feedback yields the strongest personalization performance."
```
---

## Paper 6: Tasawong et al_summarized.md

**Source File:** `Tasawong et al_summarized.md`

```yaml
paper_id: 10.48550/arXiv.2602.01618
designation: international-algorithm-specific
title: SEA-Guard: Culturally Grounded Multilingual Safeguard for Southeast Asia
authors: Tasawong, P.; Ngui, J. G.; Aji, A. F.; Cohn, T.; Limkonchotiwat, P.
year: 2026
venue: Unknown
odin_topics:
  - 5.A
  - 5.C
  - 6.B
  - 8.B
  - 8.C
  - 9.A
  - 9.B
  - 10.A
tldr: SEA-Guard is a multilingual AI safety safeguard trained on a novel culturally-grounded dataset for 8 Southeast Asian languages, achieving state-of-the-art performance on cultural safety benchmarks.
problem_and_motivation: Existing AI safeguards are primarily designed for English and fail to capture cultural nuances or perform reliably in low-resource Southeast Asian languages. This gap poses safety risks when deployed in regions with diverse cultural values and norms, as harmful content may bypass moderation.
approach:
  - Proposed a multi-agent data synthesis framework to generate 870k culturally grounded safety samples per language across 53 SEA cultural categories.
  - Developed MCRE, an ensemble technique with multiple stochastic reasoning passes, for robust zero-shot labeling and quality assurance of generated data.
  - Trained three safeguard model variants (4B, 8B, 12B) using supervised fine-tuning on Qwen-SEA-LION and Gemma base models.
  - Evaluated models on three benchmarks: a SEA cultural safety benchmark, a generic multilingual safety benchmark, and zero-shot vision-text safety benchmarks.
  - Compared performance against existing safeguards including ShieldGemma, LlamaGuard, PolyGuard, Qwen3Guard, and commercial APIs.
findings:
  - num: SEA-Guard-12B achieved a 19.9-point AUPRC improvement over ShieldGemma on response classification (75.2 vs 55.2) and scored 80.0 on cultural prompt classification.
  - The model demonstrated strong cross-lingual robustness with performance gaps below one point across all 8 SEA languages for prompt classification.
  - SEA-Guard generalized effectively to generic safety benchmarks, with a 95.9 AUPRC on English prompt classification, despite not being trained on generic safety data.
  - Zero-shot performance on vision-text safety benchmarks improved the baseline in 6 out of 7 settings, indicating emergent cross-modal capabilities.
  - SEA-Guard maintained robust performance under adversarial white-space insertion attacks, with larger variants showing the most stable harmfulness scores.
key_figures_tables:
  - "Figure 3: Model alignment with human-severity judgments → SEA-Guard achieves higher Spearman/Pearson correlations and clearer separation across severity levels than baselines."
  - "Figure 4: Robustness to adversarial attack → SEA-Guard models maintain high harmfulness scores under white-space perturbations, unlike Qwen3Guard and LlamaGuard which degrade."
  - "Table 1: Performance on SEA-SafeguardBench → SEA-Guard-12B scores 80.0 AUPRC on prompt and 75.2 on response classification, outperforming all competitors."
  - "Table 2: Generic safety performance → SEA-Guard-12B reaches 95.9 AUPRC on English prompt classification, generalizing well without generic training data."
key_equations:
  - equation: "h(x) = \\sum_{c \\in C_{safety}} s_c \\cdot P(\\hat{y}_{final} = c | R, x)"
    explanation: "Computes a continuous harmfulness score from MCRE class probabilities."
definitions:
  - term: MCRE
    definition: "Monte Carlo Reasoning Ensemble; a zero-shot classification method using multiple stochastic reasoning passes to estimate robust class probabilities."
  - term: SEA
    definition: "Southeast Asia."
  - term: PFMS
    definition: "Personal Finance Management System."
  - term: SFT
    definition: "Supervised Fine-Tuning."
  - term: AUPRC
    definition: "Area Under the Precision-Recall Curve."
critical_citations:
  - "[Tasawong et al., 2025b] — Defines the SEA-SafeguardBench used for evaluation."
  - "[Zeng et al., 2024] — Introduces ShieldGemma, a primary baseline model."
  - "[Inan et al., 2023] — Introduces LlamaGuard, a primary baseline model."
  - "[Kumar et al., 2025] — Introduces PolyGuard, a multilingual safety tool."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: "Provides a multi-agent data synthesis framework applicable to profile generation."
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: "Directly proposes MCRE, a robust classification ensemble method, relevant for behavioral profiling."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: "The data synthesis and evaluation methodology for time-series patterns is relevant."
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: "The safeguard classification task is analogous to anomaly detection in user transactions."
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: high
      justification: "Addresses cold-start issues in low-resource contexts via synthetic data generation."
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: high
      justification: "Emphasizes multilingual and culturally-aware systems, foundational for mobile-first design."
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: "Provides a framework for designing user-friendly, culturally-sensitive mobile interfaces."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: "Moderation framework aligns with user trust and data privacy needs in financial systems."
  contribution: "The paper's data synthesis framework and MCRE technique offer a scalable method for generating culturally-grounded safety data. This can be directly adapted to create behavioral profile and anomaly detection datasets for Odin. The robust classification approach (MCRE) is applicable to user behavior classification and cold-start problem-solving. The evaluation methodology provides a blueprint for benchmarking PFMS modules."
  directly_justifies:
    - "The MCRE technique can be used for robust classification of financial behaviors in Odin."
    - "The multi-agent data synthesis framework can generate synthetic user spending data for Odin."
    - "Cross-lingual robustness techniques are essential for a PFMS serving Filipino young professionals."
  limits:
    - "The paper focuses on safety moderation, not financial behavior prediction, requiring translation of methods."
    - "The models are trained on text data, not financial transaction data, so direct application is limited."
    - "Performance on specific PFMS tasks (like anomaly detection) needs further validation."
  mapping_rationale: "A systematic scan across all 12 domains and associated topic codes was performed. The paper's focus on multilingual AI safety and cultural grounding directly informs behavioral profiling (5.A, 5.C), forecasting (6.B), and anomaly detection (8.B, 8.C). The data synthesis and classification methodology are relevant to mobile-first design (9.A, 9.B) and data privacy/trust (10.A). Domains like Expense Categorization (3.A, etc.) and Savings/Debt Management (13.A, etc.) were rejected as they are not directly addressed. Borderline cases like cultural practices (2.A, etc.) were considered but not selected, as the paper's cultural grounding is on safety, not financial practices. Overall, the paper provides high-value methodological contributions for building robust, culturally-aware classifiers for a PFMS like Odin."
limitations:
  - "The study did not cover over 700 SEA dialects and languages, limiting generalizability."
  - "The paper did not experiment with 0.5B models due to performance reliability concerns."
  - "Safety evaluation benchmarks for SEA languages are still needed."
  - "The potential for generated datasets to be misused for harmful content generation is acknowledged. [unacknowledged]"
remember_this:
  - "Multilingual safeguards perform poorly without culturally-grounded training data."
  - "MCRE improves classification robustness by aggregating multiple stochastic reasoning passes."
  - "SEA-Guard generalizes to unseen vision-text tasks despite text-only training."
  - "A 19.9-point AUPRC gap was observed between SEA-Guard and ShieldGemma on response classification."
  - "Data deduplication and scale (870k samples per language) are critical for robust performance."
```
---

## Paper 7: Aoun et al_summarized.md

**Source File:** `Aoun et al_summarized.md`

```yaml
paper_id: 10.3390/ijfs14020035
designation: international
title: "Understanding Millennials’ Financial Behavior: The Role of Fintech Adoption, Financial Literacy, and the Mediating Effect of Financial Attitudes in a Crisis-Affected Emerging Economy"
authors: "Aoun, D.; Rahal, R.; Sfeir, L.; Jabbour Al Maalouf, N."
year: 2026
venue: "International Journal of Financial Studies"
odin_topics:
  - "1.C"
  - "4.A"
  - "4.B"
  - "5.A"
  - "10.B"
tldr: "FinTech adoption and financial literacy positively predict millennial financial behavior, with financial attitude mediating the literacy-behavior link in Lebanon's crisis context."
problem_and_motivation: "Lebanon's economic crisis and banking collapse have eroded financial trust, yet little is known about how FinTech adoption, financial literacy, and attitudes jointly affect millennial financial behavior. Understanding these dynamics is critical for designing effective financial interventions in fragile economies. Prior research largely omits the attitudinal mediator in crisis settings."
approach:
  - "Collected survey data from 390 Lebanese millennials using a structured questionnaire."
  - "Measured FinTech adoption, financial literacy, financial attitude, and financial behavior via Likert scales."
  - "Applied structural equation modeling (SEM) to test direct and mediating effects."
  - "Assessed model fit using CFI, TLI, SRMR, and RMSEA, achieving good fit indices."
  - "Conducted confirmatory factor analysis and validated reliability via Cronbach's alpha and composite reliability."
findings:
  - "FinTech adoption positively predicts financial behavior (β = 0.144, p < 0.001)."
  - "Financial literacy positively predicts financial behavior (β = 0.337, p < 0.001)."
  - "Financial attitude positively predicts financial behavior (β = 0.414, p < 0.001)."
  - "Financial literacy strongly predicts financial attitude (β = 0.681, p < 0.001)."
  - "Financial attitude partially mediates the relationship between financial literacy and financial behavior."
  - "num: Financial attitude has the strongest effect on behavior among the predictors (β = 0.414)."
key_figures_tables:
  - "Table 7: SEM regression estimates showing all hypothesized paths are significant."
  - "Figure 2: Path diagram illustrating direct and mediated relationships with standardized coefficients."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "FinTech adoption"
    definition: "The extent to which individuals accept and integrate digital financial technologies into their financial activities."
  - term: "Financial literacy"
    definition: "The knowledge and skills that enable informed decision-making about budgeting, saving, investing, and managing credit."
  - term: "Financial attitude"
    definition: "An individual's psychological tendencies, beliefs, and evaluative judgments about money and financial decision-making."
  - term: "Financial behavior"
    definition: "Actual actions and conduct related to saving, spending, budgeting, debt repayment, and investing."
  - term: "Structural equation modeling (SEM)"
    definition: "A multivariate statistical technique for testing complex causal relationships among latent constructs."
critical_citations:
  - "[Lusardi & Mitchell, 2014] — Foundational definition and importance of financial literacy."
  - "[Swacha-Lech & Solarz, 2021] — Key determinants of FinTech adoption among millennials."
  - "[Abu Daqar et al., 2021] — Establishes link between FinTech and millennial financial behavior."
relevance:
  topics:
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "contextual"
      justification: "Focuses on millennial financial behavior but in Lebanese, not Filipino, context."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "low"
      justification: "Discusses FinTech adoption but not specific PFMS systems."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Identifies gaps like financial illiteracy and trust issues relevant to PFMS."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Directly examines behavioral determinants and attitudinal mediation, key for profiling."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "medium"
      justification: "Highlights trust erosion in financial institutions, relevant to user trust in PFMS."
  contribution: "This study provides empirical evidence that financial attitude mediates the literacy-behavior link, which can directly inform Odin's behavioral profiling module by emphasizing attitudinal drivers over knowledge alone. It also highlights the importance of institutional trust and crisis context, offering insights for Odin's user trust and engagement strategies. The methodological approach using SEM provides a template for evaluating multi‑factor behavioral models within a PFMS. Finally, the findings on FinTech adoption's weaker effect in fragile economies suggest that Odin's design should prioritize attitudinal and cognitive interventions over purely technological features."
  directly_justifies:
    - "Financial literacy alone is insufficient without attitudinal reinforcement to improve financial behavior."
    - "FinTech adoption positively influences financial behavior, but its effect is weaker in crisis contexts."
    - "Financial attitude is the strongest predictor of millennial financial behavior."
    - "In crisis settings, psychological and attitudinal mechanisms amplify over rational knowledge."
  limits:
    - "Cross‑sectional design prevents causal inference and tracking of behavioral changes over time."
    - "Self‑reported measures may be biased by social desirability and perceived versus actual behavior."
    - "Sample may not be representative of all Lebanese millennials, limiting generalizability."
    - "Excludes crisis‑specific constructs such as institutional trust and perceived financial risk [unacknowledged]."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to Behavioral Profiling (5.A) because it directly models financial behavior and attitudes, providing empirical support for attitudinal mediation. It also informs Existing Systems & Gaps (4.A, 4.B) through its discussion of FinTech adoption and identified limitations like financial illiteracy and trust erosion, with 4.B rated medium and 4.A low due to limited PFMS specificity. User Trust (10.B) was rated medium given the emphasis on trust in the financial system. The paper touches on Financial Behavior (1.C) but only contextually, as the population is Lebanese rather than Filipino. Other domains—Expense Categorization, Spending Forecasting, Budget Recommendation, Anomaly Detection, Mobile‑First Design, Engagement, Evaluation, and Savings/Debt Management—were considered and rejected because the paper does not address algorithmic or design‑specific aspects of these areas. Overall, the paper provides robust behavioral evidence that can guide Odin's profiling and trust‑building features, though it is not directly transferable to Filipino cultural specifics."
limitations:
  - "Cross‑sectional design prevents causal inference and tracking of behavioral changes over time."
  - "Self‑reported measures may be biased by social desirability and perceived versus actual behavior."
  - "Sample may not be representative of all Lebanese millennials, limiting generalizability."
  - "Excludes crisis‑specific constructs such as institutional trust and perceived financial risk [unacknowledged]."
remember_this:
  - "Financial attitude mediates the link between literacy and financial behavior."
  - "FinTech adoption improves behavior but less than literacy in crisis contexts."
  - "Financial attitude has the largest effect size (β = 0.414) on behavior."
  - "Financial literacy strongly shapes attitudes (β = 0.681), which then drive behavior."
  - "In unstable economies, psychological factors outweigh cognitive knowledge in predicting behavior."
```
---

## Paper 8: Jayaprakashnarayan et al_summarized.md

**Source File:** `Jayaprakashnarayan et al_summarized.md`

```yaml
paper_id: 10.15662/IJEETR.2026.0802073
designation: international-algorithm-specific
title: AI-Enabled NLP Framework for Automated Expense Management and Financial Analysis
authors: Jayaprakashnarayan, N.; Sakthivel, M.; Sachidhanandam, P.; Devi, N. Kanjana; Mughilan, T.S. Manivel
year: 2026
venue: International Journal of Engineering & Extended Technologies Research
odin_topics:
  - 3.A
  - 3.B
  - 3.C
  - 5.C
  - 6.A
  - 8.A
  - 8.B
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
tldr: A multi-task NLP framework using MuRIL and ensemble fraud detection automates expense tracking from financial SMS with 96.8% extraction accuracy and 91.7% fraud sensitivity.
problem_and_motivation: Digital payment proliferation generates fragmented financial notifications that overwhelm manual tracking. Existing systems fail to handle code-mixed languages, evolving message formats, and personalized spending patterns. A unified, adaptive NLP framework is needed for accurate, privacy-preserving expense management.
approach:
  - Framework integrates transformer-based language model (MuRIL) for contextual understanding of financial messages.
  - Multi-task learning architecture performs simultaneous entity extraction and transaction classification using shared representations.
  - Ensemble anomaly detection combines rule-based screening, statistical outlier detection, and LSTM autoencoders for fraud identification.
  - Online learning enables on-device personalization from user corrections without transmitting financial data.
  - Uncertainty-aware processing flags low-confidence extractions for human review, ensuring accuracy.
findings:
  - num: Entity extraction achieved 96.8% F1-score overall, with amount and date extraction exceeding 98%.
  - num: Transaction classification reached 94.9% weighted F1-score across 14 expense categories.
  - num: Ensemble fraud detection attained 91.7% sensitivity with 3.8% false positive rate.
  - num: On-device processing achieved 43-127ms latency with 0.9-2.0% hourly battery impact on commodity smartphones.
  - num: Multi-task learning improved entity extraction by 1.2% over single-task MuRIL fine-tuning.
  - Multi-layered security protocol includes account matching, duplicate detection, and encrypted local storage.
  - The framework processes code-mixed Hinglish text effectively, a challenge for English-only models.
  - Federated learning with differential privacy enables global model improvement without compromising user data.
key_figures_tables:
  - Table I: Dataset characteristics (124,583 messages, 42 banks, 18 UPI apps) → Diverse financial SMS corpus.
  - Table II: Entity extraction by type → Merchants hardest (95.2% F1), amounts easiest (98.8% F1).
  - Table IV: Classification per category → Shopping hardest (92.4% F1), income easiest (98.6% F1).
  - Table V: Fraud detection comparison → Ensemble best (91.7% sensitivity, 95.6% AUC).
  - Figure 2: Entity-level performance by type → Visualizes extraction difficulty variation.
key_equations:
  - equation: L = λ_entity L_entity + λ_class L_class
    explanation: Multi-task objective balancing entity and classification losses.
  - equation: H_token = -∑ p(t|x) log p(t|x)
    explanation: Token-level uncertainty measured as entropy of tag distribution.
  - equation: Margin = p(c1|x) - p(c2|x)
    explanation: Classification uncertainty via gap between top probabilities.
definitions:
  - term: MuRIL
    definition: Multilingual Representations for Indian Languages, a BERT model pre-trained on 17 Indian languages.
  - term: UPI
    definition: Unified Payments Interface, India's real-time payment system.
  - term: NLP
    definition: Natural Language Processing, enabling computers to understand human language.
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network for sequence modeling.
  - term: CRF
    definition: Conditional Random Field, a statistical modeling method for structured prediction.
critical_citations:
  - "[Devlin et al., 2019] — BERT transformer architecture for language understanding."
  - "[Khanuja et al., 2021] — MuRIL multilingual model for Indian languages."
  - "[Hochreiter and Schmidhuber, 1997] — LSTM foundations for sequence modeling."
  - "[Liu et al., 2023] — Financial named entity recognition benchmarks."
  - "[Ahmed and Mahmood, 2020] — Hybrid fraud detection ensemble methodology."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Proposes a multi-task classification system for 14 expense categories with 94.9% F1.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: high
      justification: Defines and evaluates a detailed 14-category taxonomy for personal finance.
    - code: 3.C
      name: User-Defined Allocation Constraints
      relevance: medium
      justification: Online learning enables personalization of category boundaries via user corrections.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Transaction classification and fraud detection infer spending behavior.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: low
      justification: Framework foundation for future predictive modules via sequential transaction modeling.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Ensemble fraud detection module directly addresses transaction anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Compares rule-based, statistical, and LSTM autoencoder anomaly detection methods.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: high
      justification: On-device processing and optimization for mobile constraints (latency, battery, memory).
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Uncertainty-aware UI and interactive dashboards enhance user experience.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: On-device processing, encryption, and differential privacy prevent data leakage.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Explainable AI and uncertainty flags build user trust and enable informed overrides.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Phased evaluation (component, end-to-end, longitudinal, UX) provides a rigorous framework.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Detailed component-level benchmarking of entity extraction, classification, and fraud detection.
  contribution: The paper directly informs Odin's expense categorization engine by providing a validated multi-task NLP architecture for parsing financial messages and classifying transactions into a detailed category taxonomy. Its ensemble fraud detection module offers a template for Odin's anomaly detection subsystem, incorporating rule-based, statistical, and deep learning components with uncertainty quantification. The privacy-preserving on-device processing and federated learning approach provide a blueprint for Odin's data security and personalization mechanisms. The rigorous component-level and longitudinal evaluation frameworks establish benchmarks for Odin's own algorithmic module testing. The mobile optimization strategies (quantization, pruning, latency/battery analysis) offer practical guidance for deploying Odin on resource-constrained devices in the Philippines.
  directly_justifies:
    - "Transformer-based models significantly outperform rule-based and recurrent baselines for financial entity extraction (F1 0.968 vs 0.888)."
    - "Multi-task learning with shared representations improves both entity extraction and classification performance."
    - "Ensemble fraud detection achieves 91.7% sensitivity with 3.8% false positive rate on personal transaction data."
    - "On-device deployment with quantization achieves 4× size reduction while preserving 98.7% accuracy."
    - "Uncertainty-aware processing prevents automation errors in ambiguous cases."
  limits:
    - "Dataset focused on Indian financial ecosystem; generalization to Philippine banks and payment systems untested."
    - "Model compression (quantization/pruning) sacrifices 1.3% accuracy for mobile deployment."
    - "Longitudinal adaptation study limited to 6 months; longer-term concept drift effects unexplored."
    - "Battery impact scales with transaction volume; heavy users may experience significant drain."
  mapping_rationale: Systematic scanning of all 12 functional domains and their associated topic codes flagged relevance primarily in Expense Categorization (3.A, 3.B, 3.C), Anomaly Detection (8.A, 8.B), Mobile-First Design (9.A, 9.B), Data Privacy (10.A, 10.B), and System Evaluation (12.A, 12.B). High relevance was assigned for topics directly addressed by core algorithms: 3.A (categorization framework), 8.A (anomaly detection system), 9.A (mobile optimization), 10.A (privacy architecture), and 12.B (algorithm evaluation). Medium relevance for 5.C (classification informing profiles), 3.C (personalization), 9.B (UX), 10.B (trust), and 12.A (evaluation framework). Low relevance for 6.A because predictive modeling is discussed as future work, not a primary contribution. Domains like Filipino Cultural Context (2.A-D), Behavioral Profiling (5.A-B), Budget Recommendation (7.A-D), Retention (11.A-B), and Savings/Debt (13.A-C) were rejected as not addressed. Borderline cases: 6.A was considered due to sequential modeling but is not a central prediction engine; 5.C was included for its classification methodology though not directly user profiling. Overall, the paper is highly relevant for Odin's algorithmic core, especially NLP-based parsing, classification, anomaly detection, and mobile-first secure architecture.
limitations:
  - "Geographic generalizability to Philippine banks and payment systems is untested. [unacknowledged]"
  - "Long-term performance after 6+ months without retraining is not evaluated. [unacknowledged]"
  - "Heavy transaction volumes may cause significant battery drain on low-end devices."
  - "Loss of 1.3% accuracy due to quantization may affect millions of transactions annually."
  - "Shopping category classification remains challenging (92.4% F1) due to merchant diversity."
remember_this:
  - "96.8% entity extraction accuracy using MuRIL multi-task learning on financial SMS."
  - "94.9% classification F1 across 14 expense categories with on-device personalization."
  - "91.7% fraud sensitivity with only 3.8% false positives via ensemble detection."
  - "Quantized models achieve 4× size reduction with 98.7% accuracy preservation."
  - "Uncertainty-aware processing flags low-confidence decisions for user review."
```
---

## Paper 9: Malave et al_summarized.md

**Source File:** `Malave et al_summarized.md`

```yaml
paper_id: 2c8a9b4e-1e5d-5a2f-9b3c-8d7e6f5a4b3c
designation: international-algorithm-specific
title: Transforming financial documents into credit decisions using explainable artificial intelligence and optical character recognition
authors: Malave, S.; Khemani, B.; Patil, H.; Nandurkar, S.; Nandurkar, O.; Nayak, A.
year: 2026
venue: MethodsX
odin_topics:
  - 4.A
  - 4.B
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
tldr: An XAI framework integrates OCR and XGBoost to automate credit scoring, achieving 92.5% accuracy while providing SHAP and LIME explanations for transparency.
problem_and_motivation: Existing credit scoring models either lack interpretability or fail to utilize unstructured document data. A unified system is needed that extracts financial features from documents and provides explainable predictions to ensure fairness and regulatory compliance.
approach:
  - Documents are processed using EasyOCR, PyPDF2, and PdfPlumber to extract identity and financial data.
  - Extracted data is cleaned, normalized, and transformed into 15 engineered financial features.
  - XGBoost predicts credit scores, outperforming LightGBM, Random Forest, Logistic Regression, and LSTM.
  - SHAP provides global and local feature importance explanations for model predictions.
  - LIME generates instance-specific explanations to support transparent decision-making.
  - A human-in-the-loop review allows loan officers to validate features, predictions, and explanations before final decisions.
findings:
  - XGBoost achieved the lowest MAE of 13.71 and RMSE of 18.87, indicating high prediction consistency.
  - num: XGBoost attained a classification accuracy of 92.5% at the decision threshold of 650.
  - num: XGBoost achieved precision of 0.938, recall of 0.945, and F1-score of 0.942, outperforming all baselines.
  - SHAP analysis identified income stability, average balance, and monthly credit as top positive contributors to credit scores.
  - LIME explanations matched SHAP results, confirming consistent local and global interpretability.
  - The framework addresses the gap of integrating document intelligence with explainable machine learning for credit scoring.
key_figures_tables:
  - Figure 1: Flowchart of the proposed end-to-end framework → visualizes the complete pipeline from document ingestion to final output.
  - Table 1: Document types and extracted fields → details the specific data extracted from Aadhaar, PAN, salary slips, and bank statements.
  - Table 2: Feature description → lists all 15 engineered features used for credit risk prediction.
  - Figure 6: Correlation matrix of engineered features → shows relationships between financial attributes and their influence on credit score.
  - Figure 11: SHAP beeswarm plot for global feature importance → illustrates feature contributions across all instances.
  - Figure 12: LIME-based local explanation → demonstrates instance-specific feature contributions for an individual prediction.
key_equations:
  - equation: "AverageMonthlyCredit = (1/N) * sum(C_i)"
    explanation: "Mean of credited amounts over N months."
  - equation: "AverageUsableSalary = (1/N) * sum(S_i - EMI_i)"
    explanation: "Average income left after EMI payments."
  - equation: "AverageEligibleEMI = 0.4 * AverageUsableSalary"
    explanation: "Maximum EMI capacity set at 40% of usable salary."
  - equation: "EMI = P * r * ((1+r)^n) / ((1+r)^n - 1)"
    explanation: "Calculates monthly installment for a loan."
definitions:
  - term: XAI
    definition: "Explainable Artificial Intelligence, methods that make AI model decisions transparent."
  - term: OCR
    definition: "Optical Character Recognition, technology to extract text from images and documents."
  - term: XGBoost
    definition: "Extreme Gradient Boosting, a tree-based ensemble machine learning algorithm."
  - term: SHAP
    definition: "SHapley Additive exPlanations, a game-theoretic approach for explaining model outputs."
  - term: LIME
    definition: "Local Interpretable Model-agnostic Explanations, a method for explaining individual predictions."
critical_citations:
  - "[Nwafor et al., 2024] — Proposes a hybrid ML approach for transparent credit decisions."
  - "[Nallakaruppan et al., 2024] — Reviews XAI for credit risk and financial decision support."
  - "[De Lange et al., 2022] — Discusses XAI for credit assessment in banking."
  - "[Chang et al., 2025] — Presents an explainable ML study for credit worthiness prediction."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: "Reviews existing credit scoring systems and their limitations."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: "Explicitly addresses the lack of integration between document data and explainable ML."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: "Proposes XGBoost for credit score prediction, relevant to forecasting."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: "Uses aggregated financial features for prediction, not sequential data directly."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: "Features like bounce_count and gambling_transaction_count are related to anomaly detection."
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: "Mentions features indicative of anomalies but does not focus on detection algorithms."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: "Mentions role-based authentication, audit trails, and document deletion for privacy."
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: "Focuses on transparency via SHAP/LIME to build trust and support regulatory compliance."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: "Provides a comprehensive evaluation using MAE, RMSE, R2, Accuracy, Precision, Recall, F1."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: "Compares XGBoost against LGBM, RF, LR, and LSTM using standard regression metrics."
  contribution: "The paper contributes to Odin's XAI module by demonstrating how SHAP and LIME can explain predictions of a tree-based ensemble. It supports the feature engineering pipeline (3.B) by validating that derived financial features (e.g., income stability, obligation-to-income ratio) are predictive and interpretable. The human-in-the-loop review aligns with Odin's need for user trust and explainability (10.B). The evaluation methodology (12.A, 12.B, 12.C) provides a template for assessing Odin's own predictive modules. The work directly justifies the use of XGBoost for structured financial data and the application of SHAP/LIME for transparency."
  directly_justifies:
    - "XGBoost achieves superior performance (92.5% accuracy) for credit scoring on structured financial features."
    - "SHAP and LIME provide consistent global and local explanations for tree-based ensemble models."
    - "Combining document-based feature extraction with explainable ML enhances transparency and regulatory compliance."
    - "Derived financial features like income stability and obligation-to-income ratio are strong predictors of financial risk."
  limits:
    - "Dependency on OCR accuracy, which may vary with document quality and noise."
    - "Trained on a structured dataset that may not cover all variations of real-world financial data."
    - "SHAP and LIME may not capture all possible model interactions, limiting deeper explanation."
  mapping_rationale: "A systematic scan of all 12 functional domains was conducted. The paper was flagged as most relevant to 'Existing Systems & Gaps' (4.A, 4.B) due to its explicit focus on limitations of current credit scoring models, and to 'Data Privacy & User Trust' (10.A, 10.B) through its emphasis on XAI for transparency. High relevance was also assigned to 'System Evaluation' (12.A, 12.B) given the detailed model comparison and metrics. Medium relevance was assigned to 'Spending Forecasting' (6.A, 6.B) as it uses aggregated financial features, and 'Anomaly Detection' (8.A, 8.B) due to risk-related features like bounce_count. The domains of 'Filipino Cultural Context' (2.A-D), 'Behavioral Profiling' (5.A-C), 'Budget Recommendation' (7.A-D), 'Mobile-First Design' (9.A-B), and 'Savings & Debt Management' (13.A-C) were considered but rejected as the paper does not address these topics. Overall, the paper provides strong support for Odin's predictive modeling, explainability, and evaluation modules."
limitations:
  - "Dependency on OCR accuracy, which may vary with document quality and noise."
  - "Trained on a structured dataset that may not cover all variations of real-world financial data."
  - "SHAP and LIME may not capture all possible model interactions, limiting deeper explanation."
remember_this:
  - "XGBoost achieved 92.5% accuracy for credit risk classification."
  - "SHAP and LIME provide consistent explanations for financial predictions."
  - "Integrating document OCR with ML improves data utilization."
  - "Human-in-the-loop review ensures accountability and compliance."
  - "Feature engineering transforms documents into 15 predictive financial attributes."
```
---

## Paper 10: Guedi_summarized.md

**Source File:** `Guedi_summarized.md`

```yaml
paper_id: 5b3e3e7a-6f5b-5a3e-8f5e-6b3e3e7a6f5b
designation: international
title: Predictive Financial Decision Platform through Scalable Online Computing and Reward-Driven Analytical Mechanisms
authors: Guedi, H. I.
year: 2026
venue: Frontiers in Emerging Multidisciplinary Sciences
odin_topics:
  - 1.A
  - 2.A
  - 2.D
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 9.A
  - 10.A
  - 10.B
  - 11.A
  - 11.B
tldr: Integrates scalable cloud computing and reinforcement learning into a predictive financial platform to improve decision-making, personalization, and user engagement.
problem_and_motivation: Conventional financial decision systems suffer from limited personalization, insufficient predictive capability, and weak scalability under real-time demand. There is a need for an intelligent platform that unifies scalable analytics, behavioral adaptation, and digital literacy integration to improve financial decision reliability.
approach:
  - The framework integrates a digital financial data acquisition layer, a scalable cloud computing layer, and a reward-driven reinforcement learning engine.
  - It incorporates a financial literacy and capability assessment layer to personalize recommendations based on user understanding.
  - A predictive risk and portfolio intelligence layer performs portfolio risk estimation, savings forecasting, and debt-risk prediction using deep reinforcement learning.
  - The adaptive decision recommendation layer provides personalized budgeting, savings, investment, and debt reduction strategies.
  - The system uses a distributed cloud model to scale computational resources dynamically according to analytical demand.
findings:
  - num: Reward-driven reinforcement learning significantly improved predictive financial decision coordination and adaptive portfolio prediction.
  - num: The scalable online computing infrastructure improved real-time analytical responsiveness during high-volume transaction conditions.
  - num: Financial literacy integration enhanced recommendation personalization and behavioral adaptability for users with varying capability levels.
  - Behavior-sensitive reinforcement learning improved long-term financial planning outcomes and encouraged stable savings behavior.
  - The framework improved system accessibility for diverse user populations through cloud-enabled continuous online financial interaction.
key_figures_tables:
  - Table 1: Comparison of traditional systems vs. proposed framework across scalability, user modeling, and behavioral learning parameters → Proposed framework is highly adaptive and intelligent.
key_equations:
  - equation: "R_t = \\alpha P_t - \\beta Risk_t + \\gamma S_t"
    explanation: Balances portfolio performance, risk exposure, and savings stability.
  - equation: "L_s = \\frac{\\sum_{i=1}^{n} w_i f_i}{n}"
    explanation: Weighted indicators determine digital financial capability.
  - equation: "Risk_{opt} = \\min \\sum_{i=1}^{n}(r_i - \\mu)^2"
    explanation: Minimizes volatility while preserving adaptive financial growth.
definitions:
  - term: Reinforcement Learning
    definition: A machine learning technique where an agent learns to make decisions by performing actions and receiving rewards or penalties.
  - term: Scalable Online Computing
    definition: A computational architecture that can dynamically adjust its resources to handle varying workloads in real-time.
critical_citations:
  - "[Mirza et al., 2025] — Demonstrates deep reinforcement learning improves portfolio risk prediction."
  - "[Lusardi, Mitchell, and Curto, 2010] — Establishes link between financial literacy and planning."
  - "[Demirgüç-Kunt and Klapper, 2013] — Foundational work on financial inclusion measurement."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Provides general context on financial behavior and literacy relevant to YPs.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: low
      justification: Discusses digital financial literacy but not specific Filipino cultural practices.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Focuses on general financial behavior, not specific Filipino spending cycles.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Critiques limitations of conventional financial advisory systems.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly identifies gaps like limited personalization and predictive capability.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Employs behavioral analytics and adaptive user modeling.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses literacy and behavior assessment to personalize recommendations.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Core contribution is a predictive financial decision platform.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Uses reinforcement learning for predictive analytics and portfolio forecasting.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Provides budgeting guidance as a key recommendation feature.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: The adaptive recommendation layer provides personalized budgeting.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: Discusses digital accessibility but not specifically mobile-first design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Framework includes data privacy protection and secure authentication.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Mentions improving user trust through privacy and ethical governance.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: Reward-driven mechanisms improve user engagement and confidence.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: Adaptive personalization supports long-term engagement.
  contribution: "This paper provides a theoretical and methodological foundation for Odin's predictive modules by demonstrating the integration of scalable cloud computing and reinforcement learning. It validates the use of reward-driven optimization to adapt financial recommendations to user behavior. The framework's literacy-sensitive personalization directly informs Odin's approach to user profiling. Its emphasis on behavioral engagement supports Odin's retention strategies."
  directly_justifies:
    - "Reinforcement learning improves adaptive portfolio prediction and dynamic risk management."
    - "Scalable online computing reduces latency in recommendation generation and portfolio evaluation."
    - "Financial literacy integration enhances recommendation personalization and behavioral adaptability."
  limits:
    - "Reinforcement-learning systems require large-scale behavioral data, which may create privacy concerns."
    - "Computational scalability demands substantial cloud infrastructure resources during high analytical workloads."
    - "Financial uncertainty and sudden market volatility may reduce predictive reliability under extreme conditions."
    - "Excessive dependence on automated recommendation systems may reduce independent financial reasoning among users."
    - "Training data inadequacy may introduce bias in reinforcement-learning systems [unacknowledged]."
  mapping_rationale: "A systematic scan of all 12 functional domains was conducted. Domains flagged as relevant include: Existing Systems & Gaps (4.A high, 4.B high), Behavioral Profiling (5.A high, 5.C medium), Spending Forecasting (6.A high, 6.B high), Budget Recommendation (7.A high, 7.B high), User Retention (11.A high, 11.B medium), Data Privacy (10.A medium, 10.B medium), and Filipino Cultural Context (1.A contextual, 2.A low, 2.D low). The paper's core on predictive reinforcement learning strongly supports 6.A and 6.B. Its critique of existing systems and adaptive personalization justify 4.A, 4.B, and 5.A. Budgeting and engagement features align with 7.A, 7.B, 11.A, and 11.B. Privacy mentions support 10.A and 10.B but are not central. Domains like Mobile-First Design (9.A) and Anomaly Detection (8.A-8.C) were considered but rejected as the paper does not address them specifically. Overall, the paper offers strong justification for Odin's predictive, behavioral, and adaptive recommendation modules."
limitations:
  - "Reinforcement-learning systems require large-scale behavioral data, which may create privacy concerns."
  - "Computational scalability demands substantial cloud infrastructure resources during high analytical workloads."
  - "Financial uncertainty and sudden market volatility may reduce predictive reliability under extreme conditions."
  - "Excessive dependence on automated recommendation systems may reduce independent financial reasoning among users."
  - "Training data inadequacy may introduce bias in reinforcement-learning systems [unacknowledged]."
remember_this:
  - "Reinforcement learning significantly improves adaptive portfolio prediction and risk management."
  - "Scalable cloud computing reduces latency in financial recommendation generation."
  - "Literacy-sensitive personalization enhances accessibility for diverse user populations."
  - "Reward-driven optimization encourages stable savings behavior and debt reduction."
  - "Integrating scalable cloud and reinforcement learning creates a robust foundation for intelligent financial ecosystems."
```
---

## Paper 11: Vinitha et al_summarized.md

**Source File:** `Vinitha et al_summarized.md`

```yaml
paper_id: 1b4e3c2d-5a6f-7b8c-9d0e-1f2a3b4c5d6e
designation: international-algorithm-specific
title: AI-Driven Personal Finance Management: Predictive Expense Forecasting and Behavioural Clustering
authors: Vinitha, C.; Krishna, A. H.; Reddy, E. M.; Javari, P.
year: 2026
venue: International Journal of Data Science and IoT Management System
odin_topics:
  - 3.A
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 7.B
  - 8.A
  - 12.B
  - 13.A
tldr: Combines LSTM forecasting and K-Means clustering to provide personalized expense predictions and spending behavior insights for improved financial decision-making.
problem_and_motivation: Manual financial tracking and basic budgeting tools fail to capture complex temporal dependencies and spending patterns, making accurate future expense prediction difficult. This leads to inefficient financial decisions and a lack of personalized, actionable insights for users. There is a need for an intelligent system that analyzes historical data to forecast expenses and understand underlying spending behavior.
approach:
  - Developed a Django-based web application with a MySQL database and email OTP authentication for secure access.
  - Applied K-Means clustering to expense categories and amounts to group similar spending behaviors and identify financial patterns.
  - Implemented an LSTM deep learning model to analyze historical daily expense data and generate future expense predictions, addressing non-linear trends and temporal dependencies.
  - Integrated VADER sentiment analysis to evaluate user feedback, classifying it as positive, negative, or neutral for continuous system improvement.
  - Used the predicted expenses to compute a surplus against a generated income approximation, providing investment or savings recommendations.
findings:
  - num: The LSTM model achieved an accuracy of 99.93% with a Mean Squared Error of 35.41 for predicting future expenses.
  - num: K-Means clustering successfully grouped transaction records into distinct expense behavior patterns based on category and amount.
  - The combined approach of prediction and clustering enables users to make informed budgeting and investment planning decisions.
  - The proposed system automates financial insights and provides personalized recommendations, addressing limitations of traditional financial tools.
key_figures_tables:
  - Figure 4: K-Means clustering results for expense behavior patterns → Identifies distinct spending clusters for better financial understanding.
  - Figure 5: LSTM model evaluation comparing predicted vs. actual expenses → Demonstrates high accuracy in forecasting.
  - Figure 6: Budget recommendation screen showing surplus calculation → Provides actionable investment suggestions based on predictions.
  - Figure 7: VADER sentiment analysis of user feedback → Classifies feedback to improve user interaction.
key_equations:
  - equation: "MSE = \\frac{1}{n} \\sum_{i=1}^{n} (y_i - \\hat{y}_i)^2"
    explanation: Loss function for evaluating LSTM prediction accuracy.
definitions:
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network capable of learning long-term dependencies in sequential data.
  - term: K-Means Clustering
    definition: An unsupervised learning algorithm that groups data points into k distinct clusters based on similarity.
  - term: VADER
    definition: Valence Aware Dictionary and sEntiment Reasoner, a rule-based sentiment analysis tool.
  - term: SMTP
    definition: Simple Mail Transfer Protocol, used for sending OTP authentication emails.
  - term: OTP
    definition: One-Time Password, a temporary passcode for user verification.
critical_citations:
  - "[Sirisha et al., 2022] — Benchmarks LSTM for profit prediction."
  - "[Shiyyab et al., 2023] — Discusses AI adoption and financial performance."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Uses K-Means clustering to categorize and group expenses.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Clustering analysis identifies distinct spending behavior patterns.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: K-Means is applied to classify expenses and uncover user financial profiles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Core contribution is the LSTM model for expense prediction.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: LSTM is specifically used for time-series forecasting of daily expenses.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: System provides a budget recommendation based on predicted expenses and estimated income.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Mentions detecting anomalies but does not focus on it as a primary feature.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Reports performance metrics (MSE and accuracy) for the LSTM module.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Surplus from predicted expenses is recommended as potential savings or investment.
  contribution: This paper provides a practical implementation of an LSTM model for expense forecasting, which can directly inform the design of Odin's predictive engine. The use of K-Means clustering for expense categorization offers a viable approach for behavioral profiling. The integration of these predictive and clustering techniques demonstrates a feasible pipeline for generating personalized financial insights and recommendations. The sentiment analysis module provides a model for incorporating user feedback into system iteration. The evaluation metrics presented validate the accuracy of the algorithmic components.
  directly_justifies:
    - An LSTM model can accurately forecast daily expenses, achieving 99.93% accuracy on test data.
    - K-Means clustering is effective for categorizing expenses into meaningful behavioral groups.
    - Combining expense prediction with surplus calculation can generate actionable investment or savings recommendations.
    - Secure authentication (OTP via SMTP) is a necessary feature for a personal finance management system.
  limits:
    - The evaluation is performed on a single dataset; generalizability to diverse spending patterns may be limited.
    - The paper does not thoroughly discuss the handling of infeasible budget recommendations or user-defined constraints.
    - The system's recommendation is based on a simple surplus calculation, lacking nuanced optimization strategies.
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The domains of Spending Forecasting (6), Behavioral Profiling & Classification (5), Budget Recommendation (7), and System Evaluation (12) were flagged as highly relevant due to the paper's focus on LSTM forecasting, K-Means clustering, and the reporting of model accuracy. The Expense Categorization (3) and Savings & Debt Management (13) domains were marked as medium, as the paper addresses expense grouping and mentions savings recommendations. The Anomaly Detection (8) domain was considered low because it is only briefly referenced. Domains related to Filipino Cultural Context (2), Mobile-First Design (9), Data Privacy (10), and User Retention (11) were rejected as they were not addressed in the paper. The paper's overall relevance to Odin is high as it provides concrete, algorithm-specific evidence for building a predictive and profiling system.
limitations:
  - The paper does not discuss the model's performance on irregular spending patterns or its robustness to data sparsity. [unacknowledged]
  - The integration of sentiment analysis is superficial and not directly linked to improving the core predictive modules. [unacknowledged]
  - The budget recommendation is simplistic and does not account for user-defined allocation constraints.
remember_this:
  - LSTM achieved 99.93% accuracy for financial expense prediction.
  - K-Means clustering groups expenses into meaningful behavioral categories.
  - Predictive insights are used to generate investment or savings recommendations.
  - System integrates secure OTP authentication via SMTP for user access.
  - User feedback is analyzed with VADER for continuous system improvement.
```
---

## Paper 12: Oliveira_summarized.md

**Source File:** `Oliveira_summarized.md`

```yaml
paper_id: 10.66104/xkad2306
designation: international
title: Neural Networks for Real-Time Financial Fraud Detection
authors: Oliveira, D. N. O.
year: 2026
venue: Unknown
odin_topics:
  - 8.A
  - 8.B
  - 4.B
  - 10.A
  - 10.B
  - 12.B
tldr: Neural network architectures are redefining real-time fraud detection, yet their deployment faces significant challenges in latency, explainability, adversarial robustness, and cross-institutional collaboration.
problem_and_motivation: Conventional rule-based and statistical fraud detection methods are structurally inadequate for the complexity, volume, and adaptability of modern fraud operations. This detection gap necessitates fundamentally different solutions capable of real-time analysis and continuous adaptation.
approach:
  - The paper presents a narrative literature review of neural network architectures for fraud detection.
  - It covers theoretical foundations and six principal architectures: MLP, LSTM, GRU, CNN, Autoencoders, GNN, and Transformers.
  - The review analyzes critical operational challenges including concept drift, adversarial evasion, class imbalance, and explainability.
  - It examines production infrastructure requirements such as latency budgets and stream processing architectures.
  - Real-world implementations across credit card networks, PIX, AML, and insurance fraud are documented.
findings:
  - num: Global fraud losses were estimated at $485.6 billion in 2023, with $3.1 trillion in illicit funds flowing through the global financial system.
  - num: GNN-based models achieve recall of 0.89 on financial transaction data, compared to 0.78 for Random Forest and 0.81 for XGBoost.
  - num: PGD adversarial training reduces Attack Success Rate from 87.5% to 32.0%, delivering a 52.3% reduction in expected annual fraud loss.
  - num: Mastercard's AI-enhanced system detects three times the volume of fraudulent transactions while reducing false positives tenfold.
  - No single neural architecture dominates across all fraud typologies, making hybrid and ensemble frameworks the current performance frontier.
  - The integration of regulatory compliance, explainability, adversarial robustness, and data privacy alongside predictive accuracy is the defining challenge for production systems.
key_figures_tables:
  - "Table 1: Comparative performance of neural network architectures → Shows MLP F1 0.851, 1D-CNN F1 0.960, VAE+GAT+XGBoost AUC 0.995."
  - "Table 2: Computational profiles of architectures → MLP fastest, GNN and Transformer have high complexity/latency."
key_equations:
  - equation: "\\text{BCE}(y, \\hat{y}) = -[y \\log(\\hat{y}) + (1-y) \\log(1-\\hat{y})]"
    explanation: Binary Cross-Entropy loss for fraud classification.
  - equation: "\\text{ReLU}(x) = \\max(0, x)"
    explanation: Dominant activation function in fraud detection models.
definitions:
  - term: CNP Fraud
    definition: Card-not-present fraud, where stolen credentials are used in online or telephone transactions.
  - term: GNN
    definition: Graph Neural Network, which operates on relational data to detect fraud rings and network-level anomalies.
  - term: FL
    definition: Federated Learning, a training paradigm allowing cross-institutional model training without centralizing raw data.
  - term: DP
    definition: Differential Privacy, a technique providing formal guarantees against inferring individual data points from model outputs.
  - term: Concept Drift
    definition: The change in the relationship between input features and the target label over time.
critical_citations:
  - "[Ngo et al., 2025] — Comprehensive deep learning fraud detection survey."
  - "[Hilal et al., 2022] — Anomaly detection techniques review, defines real-time fraud as soft real-time."
  - "[Liu et al., 2024] — Systematic review of GNNs for financial fraud detection."
  - "[Černevičienė & Kabašinskas, 2024] — XAI in finance, highlights interpretability vs. opacity tension."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly reviews anomaly detection methods and their theoretical foundations applied to financial fraud.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Provides detailed comparative analysis of algorithms (LSTM, GNN, Autoencoders, Transformers) for fraud detection.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Extensively documents structural inadequacies of rule-based and statistical legacy systems.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Discusses Federated Learning and Differential Privacy as constraints and solutions for fraud detection.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: contextual
      justification: Indirectly relevant via discussion of false positives and algorithmic bias, which affect trust.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Critically assesses performance benchmarks and identifies overfitting, data leakage, and publication bias.
  contribution: "This paper provides a comprehensive, systems-level review of neural network architectures for real-time fraud detection. It directly justifies Odin's use of anomaly detection modules (8.A, 8.B) by demonstrating the necessity of moving beyond rule-based systems. The analysis of concept drift and adversarial attacks (8.B) informs the design of robust, adaptive ML components. The detailed review of GNNs and ensemble methods offers concrete architectural options for anomaly detection. The discussion of production constraints, including latency and feature stores, provides critical context for deployment."
  directly_justifies:
    - "Rule-based and statistical fraud detection systems are structurally inadequate for modern financial fraud."
    - "Real-time detection requires neural network inference within sub-100-millisecond latency budgets."
    - "Graph Neural Networks are uniquely capable of detecting fraud rings invisible to transaction-level classifiers."
    - "Federated Learning enables privacy-preserving cross-institutional model training for fraud detection."
  limits:
    - "The review is a narrative synthesis, not a systematic meta-analysis, introducing potential subjective bias in study selection."
    - "Benchmark performance metrics (e.g., AUC > 0.99) are optimistic upper bounds and may not generalize to production. [unacknowledged]"
    - "The review does not empirically compare architectures on a unified dataset, making direct performance claims difficult to validate. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to 'Anomaly Detection' (8.A, 8.B) as its core subject. It also provides strong evidence for 'Limitations and Gaps in Existing Systems' (4.B), justifying the need for Odin's ML-based approach. It touches on 'Data Privacy' (10.A, 10.B) at a medium level through discussions of Federated Learning and user trust via false positive analysis. Evaluation frameworks (12.B) are also relevant, as the paper critically reviews benchmarking methodologies. The paper was considered and rejected for topics like 'Spending Forecasting' (6.A) and 'Budget Recommendation' (7.A) as it does not directly address personal spending prediction or allocation, which are Odin's core functionalities. Borderline cases included concept drift (2.B, 2.D), which was rejected in favor of 8.B as the paper frames it as an ML operational challenge, not a cultural spending pattern. Overall, the paper is highly relevant for informing the design, justification, and evaluation of Odin's anomaly detection module."
limitations:
  - "Access to real financial transaction data is severely restricted by data protection regulations, limiting generalizability."
  - "The literature exhibits a publication bias toward positive results, creating a distorted picture of the state of the art. [unacknowledged]"
  - "Reproducibility poses a structural challenge due to proprietary datasets and omitted implementation details. [unacknowledged]"
  - "The review's narrative methodology may introduce subjective bias. [unacknowledged]"
remember_this:
  - "Neural networks structurally outperform rule-based systems for fraud detection."
  - "Real-time fraud detection must operate within a strict 100-millisecond latency budget."
  - "GNNs are uniquely effective at detecting fraud rings through relational analysis."
  - "Adversarial training can reduce fraud loss by 52.3% against evasion attacks."
  - "Federated Learning enables cross-institutional fraud model training without sharing raw data."
```
---

## Paper 13: Amado_summarized.md

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

## Paper 14: Chowdhury T. et al_summarized.md

**Source File:** `Chowdhury T. et al_summarized.md`

```yaml
paper_id: 10.1016/j.chbr.2025.100926
designation: international-algorithm-specific
title: Modeling financial literacy through explainable machine learning and behavioral segmentation in emerging economies
authors: Chowdhury, T.A.; Chowdhury, M.A.H.; Rahman, M.T.; Ahmed, I.; Ahmed, N.; Tuhin, M.A.I.; Kafy, A.A.
year: 2026
venue: Computers in Human Behavior Reports
odin_topics:
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 3.A
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 10.B
  - 11.A
  - 12.A
tldr: A machine learning and behavioral segmentation framework reveals that institutional trust and digital comfort predict financial literacy better than formal education in Bangladesh.
problem_and_motivation: Traditional demographic models fail to capture the complexity of digital financial behavior in emerging economies. The lack of advanced analytics to map financial literacy across behavioral groups limits the design of effective, targeted interventions.
approach:
  - Collected primary survey data from 1067 adults in Bangladesh using a structured instrument aligned with OECD/INFE guidelines.
  - Applied Random Forest, XGBoost, and Decision Tree to classify financial literacy levels.
  - Used SHAP analysis to identify key predictors and explain feature importance globally and locally.
  - Performed k-means clustering to segment the population based on behavioral and financial characteristics.
  - Validated clusters using silhouette score (0.42), Davies-Bouldin Index (1.08), and Calinski-Harabasz Index (287.3).
findings:
  - num: XGBoost achieved an F1-score of 0.52, representing a 58% improvement over the random baseline of 0.33.
  - num: Institutional trust was the second-strongest predictor (SHAP importance = 0.18), surpassing education (0.09) and gender (0.06).
  - num: Rural participants scored 7.3% higher in financial literacy than urban participants, though the difference was not statistically significant.
  - num: Correlation coefficients between financial knowledge and actual behaviors were below 0.10, indicating a knowledge-behavior gap.
  - Three behavioral clusters emerged: Digitally Literate Planners (34%), Informally Active but Underskilled (41%), and Digitally Excluded Traditionalists (25%).
  - num: The Digitally Excluded Traditionalists cluster had a mean financial knowledge score of 3.1/10 and an institutional trust score of 1.9/5.
  - Gender-education interaction analysis showed women benefit more from tertiary education (F=4.83, p=0.003) compared to men (F=0.91, p=0.44).
key_figures_tables:
  - Figure 2: Literacy scores by region → Rural participants slightly outperformed urban ones (5.73 vs. 5.34).
  - Figure 5: Gender-education interaction effects → Women's literacy scores peak at graduate level (mean 6.12).
  - Figure 9: Model performance metrics → XGBoost marginally outperforms Random Forest and Decision Tree.
  - Figure 11: SHAP feature importance → Income, trust, and age are the top predictors of financial literacy.
  - Figure 13: Behavioral profiles across clusters → Cluster profiles show distinct patterns in financial behaviors and digital engagement.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "SHAP"
    definition: "SHapley Additive exPlanations, a method to explain individual predictions of machine learning models."
  - term: "XGBoost"
    definition: "Extreme Gradient Boosting, an ensemble learning algorithm used for classification and regression."
  - term: "SMOTE"
    definition: "Synthetic Minority Over-sampling Technique, used to address class imbalance by generating synthetic examples."
  - term: "OECD"
    definition: "Organisation for Economic Co-operation and Development."
  - term: "F1-score"
    definition: "The harmonic mean of precision and recall, balancing both metrics."
critical_citations:
  - "[Lusardi & Messy, 2023] — Foundational framework for financial literacy and well-being."
  - "[Lusardi & Streeter, 2023] — Established measurement of financial literacy and well-being in the US."
  - "[OECD, 2022] — Policy handbook guiding financial literacy assessment."
  - "[Koskelainen et al., 2023] — Research agenda on financial literacy in the digital age."
relevance:
  topics:
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "contextual"
      justification: "This paper analyzes the financial structure of Bangladeshi adults, providing a comparable emerging economy context."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Directly analyzes financial behaviors through behavioral segmentation and identifies knowledge-behavior gaps."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "medium"
      justification: "Highlights role of informal networks (samitis, family) and community-based financial practices in Bangladesh."
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "contextual"
      justification: "Addresses seasonal income management needs, relevant to understanding cyclical spending patterns in emerging economies."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "contextual"
      justification: "Provides analogous context on spending cycles in a South Asian emerging economy."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "contextual"
      justification: "Discusses savings, budgeting, and borrowing behaviors relevant to expense categorization."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Empirically identifies three distinct behavioral profiles using k-means clustering."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "medium"
      justification: "Suggests pathways between clusters, implying dynamic profiles and transitional states."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Uses Random Forest, XGBoost, and k-means for behavioral classification and segmentation."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Develops predictive ML models (Random Forest, XGBoost) to forecast financial literacy as a proxy for financial behavior."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "medium"
      justification: "Provides methodological foundation using ML algorithms (XGBoost) for predicting financial outcomes."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "medium"
      justification: "Budgeting practices are a key behavioral indicator across all three clusters."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "high"
      justification: "Institutional trust (SHAP importance 0.18) is identified as a top predictor of financial literacy."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "medium"
      justification: "Cluster analysis shows variation in digital banking usage and comfort, relevant to engagement."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Evaluates ML models using F1-score, AUC-ROC, accuracy, and confusion matrices."
  contribution: "This paper's segmentation framework directly informs Odin's behavioral profiling module (5.A, 5.C) by providing a data-driven method to categorize users based on financial behaviors and digital engagement. The SHAP-based feature importance analysis guides the design of Odin's budget recommendation and anomaly detection algorithms by identifying institutional trust, digital comfort, and income as critical predictors to incorporate as features. The weak correlation between knowledge and behavior supports Odin's approach to infer financial capability from behavioral signals rather than relying on user-declared knowledge, addressing the cold-start problem (5.B, 7.D). The recommendation to allocate resources based on segment needs (60% to the least capable) provides a strategy for prioritizing Odin's user retention and engagement mechanisms (11.B)."
  directly_justifies:
    - "Financial literacy interventions must address behavioral barriers and institutional trust, not just information gaps."
    - "Formal education is a weak predictor of financial literacy; informal community networks are more influential."
    - "Rural users can exhibit higher financial literacy than urban users due to community-based learning mechanisms."
    - "Women benefit more from formal education, suggesting gender-differentiated pathways to financial capability."
    - "Resource allocation for interventions should be prioritized for the most excluded segments (60% to Cluster 2)."
  limits:
    - "The digital-only survey method excludes the most financially vulnerable individuals without internet access, potentially overestimating literacy. [unacknowledged]"
    - "The cross-sectional design limits causal inferences about the relationship between institutional trust and literacy. [unacknowledged]"
    - "Self-reported behaviors are subject to social desirability and recall bias. [unacknowledged]"
    - "The modest F1-score (0.52) indicates that unmeasured variables, such as psychological traits and social network factors, may influence literacy outcomes. [unacknowledged]"
    - "The survey instrument, while adapted to Bangladesh, may not fully capture the nuances of culturally specific practices. [unacknowledged]"
  mapping_rationale: "A systematic scan was performed across all 12 functional domains and their associated topic codes. The following domains were flagged as relevant: Behavioral Profiling & Classification (codes 5.A, 5.B, 5.C) with high relevance due to the paper's core segmentation and ML classification; Spending Forecasting (6.A, 6.B) with high relevance due to the predictive modeling framework; and Data Privacy & User Trust (10.B) with high relevance due to institutional trust being a top predictor. The Filipino Cultural Context domain (codes 2.A, 2.B, 2.D) was assigned contextual/medium relevance as the paper provides an analogous emerging economy context (Bangladesh) with comparable cultural financial practices (ROSCAs, family advice). Borderline cases included seasonal spending (2.B) and financial structure (1.B), which were considered relevant but not directly central to the paper's primary contribution; they were included as contextual. Domains such as Expense Categorization (3.A) and System Evaluation (12.A) were assigned contextual/medium relevance as they relate to budgeting practices and model evaluation metrics, respectively, though they are not the paper's focus. The paper's overall relevance to Odin is substantial, providing a validated methodological framework for behavioral segmentation and predictive modeling, with concrete findings on key predictors that can directly inform Odin's algorithm design and user profiling."
limitations:
  - "Digital-only survey excludes the most financially vulnerable populations without internet access, potentially biasing results toward more digitally engaged groups. [unacknowledged]"
  - "Cross-sectional design prevents causal inferences about the direction of relationships between trust and literacy. [unacknowledged]"
  - "Self-reported behavioral data are subject to social desirability and recall bias. [unacknowledged]"
  - "The modest F1-score (0.52) suggests unmeasured psychological or social variables may significantly influence literacy outcomes. [unacknowledged]"
  - "The survey, while adapted to Bangladesh, may not fully capture the nuances of informal financial systems. [unacknowledged]"
remember_this:
  - "Institutional trust (SHAP 0.18) predicts financial literacy better than formal education (SHAP 0.09)."
  - "Weak knowledge-behavior correlations (<0.10) challenge education-only financial literacy interventions."
  - "Rural residents showed 7.3% higher literacy than urban, suggesting informal community learning is effective."
  - "Three behavioral segments require differentiated interventions: 60% resources to the most excluded group."
  - "ML models with SHAP provide transparent, actionable insights beyond predictive accuracy."
```
---

## Paper 15: Tian et al_summarized.md

**Source File:** `Tian et al_summarized.md`

```yaml
paper_id: 10.3389/frai.2026.1726900
designation: international-algorithm-specific
title: Marketing-AutoM3L: domain-aware automated machine learning for financial customer analytics
authors: Tian, Y.; Shao, W.; Deng, Z.
year: 2026
venue: Frontiers in Artificial Intelligence
odin_topics:
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 7.B
  - 7.D
  - 8.A
  - 8.B
  - 12.A
  - 12.B
  - 12.C
tldr: An LLM-driven framework automatically constructs domain-aware ML pipelines for customer analytics, outperforming generic AutoML by 1.4%–5.4% in ROC-AUC while reducing development time 6.7-fold.
problem_and_motivation: Generic AutoML systems lack the capacity to automatically construct domain-specific features (e.g., RFM, CLV, engagement scores) essential for financial customer analytics, forcing organizations to either accept suboptimal performance or dedicate scarce data science expertise to manual pipeline development.
approach:
  - The framework takes raw customer data and natural language directives as input to generate executable training pipelines.
  - An LLM acts as an intelligent controller, orchestrating five stages: modality recognition, domain-aware feature engineering, model selection, multimodal pipeline construction, and training configuration optimization.
  - Domain-specific feature engineering automatically computes RFM scores, CLV projections, and engagement scores with temporal trend derivatives.
  - Model selection is guided by data characteristics, computational constraints, and business requirements expressed in natural language.
  - The system employs a late fusion strategy to integrate predictions from modality-specific models (tabular, text, temporal) into a unified pipeline.
findings:
  - num: Marketing-AutoM3L achieved ROC-AUC improvements of 1.4% to 5.4% over existing automated and manual approaches across five customer analytics datasets.
  - num: The framework reduced pipeline development time from 156.9 minutes (manual) to 23.4 minutes, representing a 6.7-fold speedup.
  - Domain-aware feature engineering alone contributed 3.3%–3.6% ROC-AUC improvement in ablation studies.
  - The framework maintains balanced performance across precision and recall while achieving the highest F1-scores on all datasets.
  - Multimodal integration (tabular+text+temporal) consistently outperforms single-modality approaches by 1.1% to 3.6% ROC-AUC.
key_figures_tables:
  - Figure 1: Overall framework architecture showing Intelligent Processing and Knowledge Supplementation modules → LLM orchestrates five-stage pipeline construction.
  - Table 2: Main experimental results comparing Marketing-AutoM3L against baselines → Framework achieves highest ROC-AUC and F1-scores across all five datasets.
  - Table 3: Performance when baselines receive pre-computed domain features → Marketing-AutoM3L maintains 0.8%–2.1% advantage even when features are provided externally.
  - Table 5: Ablation study results showing individual component contributions → Feature engineering provides largest gain (3.3%–3.6%).
  - Figure 5: Performance comparison across datasets and methods → Consistent superiority across ROC-AUC, F1, precision, and recall.
key_equations:
  - equation: "RFM = (R_i, F_i, M_i) where R_i = t_current - max(s_1,...,s_n), F_i = n, M_i = sum(a_j)"
    explanation: RFM metrics quantify customer recency, frequency, and monetary value.
  - equation: "CLV_hist_i = AOV_i × PF_i × CL_i"
    explanation: Historical averaging method projects customer lifetime value.
  - equation: "CLV_prob_i = sum_{t=1}^{T} (AOV_i × PF_i × r_i^t) / (1+d)^t"
    explanation: Probabilistic model incorporates retention probabilities for CLV projection.
  - equation: "E_i(t) = sum_{k=1}^{K} w_k sum_{\\tau=0}^{W} I_{i,k}(t-\\tau) · e^{-\\lambda \\tau}"
    explanation: Engagement score aggregates weighted, temporally decayed interaction signals.
definitions:
  - term: RFM
    definition: Recency-Frequency-Monetary analysis for customer segmentation based on transactional behavior.
  - term: CLV
    definition: Customer Lifetime Value, the total projected value a customer will generate over their relationship.
  - term: AutoML
    definition: Automated Machine Learning, systems that automate pipeline construction without manual intervention.
  - term: LLM
    definition: Large Language Model, used as an intelligent controller for decision-making across pipeline stages.
  - term: Late Fusion
    definition: Strategy combining predictions from modality-specific models after independent processing.
critical_citations:
  - "[Luo et al., 2024a] — Foundation for LLM-driven multimodal pipeline construction."
  - "[Jain et al., 2023] — Demonstrates BiLSTM-CNN effectiveness for churn prediction."
  - "[Shen et al., 2025e] — AutoML agent framework for histopathology images."
relevance:
  topics:
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: Addresses dynamic customer behavior patterns and evolving engagement trends over time.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Proposes and evaluates classification architectures (RFM, CLV, engagement scoring) for behavioral profiling.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly tackles predictive modeling for customer churn and behavior prediction in financial contexts.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Implements and evaluates temporal forecasting with RFM, CLV, and engagement trend features.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: contextual
      justification: Provides methodological framework for automated recommendation via LLM-driven optimization.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: contextual
      justification: Pipeline construction handles constraints through LLM-driven adaptation to business objectives.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Churn prediction as anomaly detection; framework identifies at-risk customers deviating from behavioral norms.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Evaluates classification algorithms (gradient boosting, neural networks) applicable to anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides comprehensive evaluation across multiple datasets with ROC-AUC, F1, precision, recall metrics.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Ablation studies quantify individual component contributions to overall performance.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Evaluation methodology for automated recommendation systems is generalizable to budget recommendation.
  contribution: The framework directly addresses Odin's need for domain-aware feature engineering in Modules 5 (behavioral profiling) and 6 (forecasting) by automatically computing RFM, CLV, and engagement features. It provides a methodology for Module 7 (budget recommendation) through LLM-driven optimization guided by natural language objectives. The experimental evaluation framework (Module 12) establishes rigorous baselines and ablation methodologies. The natural language interface design (Module 9) enables non-technical stakeholders to configure pipelines, aligning with Odin's mobile-first accessibility goals. The temporal constraint enforcement ensures no data leakage, critical for Module 8's cold-start anomaly detection baselines.
  directly_justifies:
    - "Marketing-AutoM3L's domain-aware feature engineering improves ROC-AUC by 3.3%–3.6% over generic approaches."
    - "The LLM-driven pipeline automation reduces development time by 6.7× compared to manual approaches."
    - "Natural language interfaces enable business stakeholders to specify requirements without ML expertise."
    - "Multimodal integration (tabular+text+temporal) outperforms single-modality approaches by 1.1%–3.6% ROC-AUC."
    - "The framework maintains balanced precision and recall, critical for cost-sensitive retention interventions."
  limits:
    - "Evaluation focuses on customer churn prediction rather than the full spectrum of financial behavior Odin addresses."
    - "CLV projection assumes stable customer behavior patterns, which may not hold for young professionals with dynamic financial situations."
    - "Engagement scoring weights are dataset-specific and may require recalibration for Odin's target demographic."
    - "The GPT-4 dependency introduces reproducibility concerns as model updates could affect framework behavior."
  mapping_rationale: I systematically scanned all 12 functional domains and their associated 28 topic codes against the paper's contributions. The paper is highly relevant to Predictive Modeling (6.A, 6.B) as it directly proposes and evaluates forecasting algorithms for customer behavior. It is directly applicable to Behavioral Profiling (5.B, 5.C) through its RFM, CLV, and engagement scoring methodologies. The evaluation framework (12.A, 12.B) provides rigorous baselines and ablation studies. The paper has medium relevance to Anomaly Detection (8.A, 8.B) as churn prediction is a form of anomaly detection, and the classification algorithms are transferable. It provides contextual relevance to Budget Recommendation (7.B, 7.D) through its LLM-driven optimization and constraint handling, and to Mobile-First Design (9.A, 9.B) through its natural language interface. I rejected the following domains as non-applicable: Filipino Cultural Context (2.A–D) as the paper uses international datasets; Expense Categorization (3.A–C) as it does not address category design; Existing Systems (4.A–B) as the focus is on new methodology rather than landscape analysis; Data Privacy (10.A–B) as it is not addressed; User Retention (11.A–B) except as a prediction target; and Savings/Debt Management (13.A–C) as these are not covered. The overall relevance is high, as the paper provides a directly applicable methodology for automating domain-aware ML pipelines that could be adapted to Odin's architecture.
limitations:
  - "Reliance on proprietary GPT-4 API introduces cost and reproducibility concerns for deployment. [unacknowledged]"
  - "Experiments use international datasets; generalizability to Filipino young professionals is untested. [unacknowledged]"
  - "The framework assumes high-quality, well-structured input data, which may not reflect real-world PFMS data quality. [unacknowledged]"
  - "Evaluation focuses on predictive accuracy rather than the full PFMS workflow including budgeting and savings recommendations. [unacknowledged]"
remember_this:
  - "LLM-driven AutoML reduces pipeline development time from 157 to 23 minutes."
  - "Domain-aware feature engineering improves ROC-AUC by 3.3%–3.6% over generic approaches."
  - "Natural language directives enable non-experts to configure ML pipelines without coding."
  - "Multimodal data integration outperforms single-modality approaches by up to 3.6% ROC-AUC."
  - "RFM, CLV, and engagement scores are the most predictive features across all datasets."
```
---

## Paper 16: Li_summarized.md

**Source File:** `Li_summarized.md`

```yaml
paper_id: 10.71222/7v3b7272
designation: international-algorithm-specific
title: Research on Personalized Asset Allocation Using AI Agents in Robo-Advisory Scenarios
authors: Li, J.
year: 2026
venue: Journal of Computer, Signal, and System Research
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 11.A
tldr: A systematic review of AI-driven personalized asset allocation in robo-advisory, covering risk profiling, dynamic optimization, behavioral finance integration, and key challenges like explainability and privacy.
problem_and_motivation: Standard robo-advisory models rely on generalized algorithms that fail to address individual investor circumstances and risk preferences. This limitation motivates the development of sophisticated AI techniques to deliver truly personalized asset allocation.
approach:
  - Systematic review of literature on AI applications in robo-advisory.
  - Examines machine learning, reinforcement learning, and NLP for risk profiling and investor segmentation.
  - Analyzes dynamic asset allocation strategies, including RL-based adaptive portfolios.
  - Compares AI algorithms and discusses challenges like transparency and data privacy.
  - Provides a synthesis of current methodologies and identifies future research directions.
findings:
  - num: RL agents learn optimal trading strategies, improving portfolio adaptability to market conditions.
  - Deep learning models, especially RNNs, effectively capture temporal dependencies in financial data.
  - NLP enhances risk assessment by extracting sentiment and goals from investor communication.
  - Integrating behavioral finance principles mitigates cognitive biases in investment decisions.
  - Explainability and data privacy remain significant hurdles for AI adoption in robo-advisory.
key_figures_tables:
  - Table 1: Comparison of early robo-advisory models → highlights rule-based limitations.
  - Table 2: Timeline of AI integration in robo-advisory → shows evolution to RL and evolutionary algorithms.
  - Table 3: Comparison of risk profiling methods → AI enhances personalization and dynamic capability.
  - Table 4: Behavioral biases and mitigation strategies → AI counters loss aversion, confirmation bias, etc.
  - Table 5: Key challenges and mitigation strategies → addresses privacy, security, and trust issues.
key_equations:
  - equation: A_t = f(M_t, I_t)
    explanation: Optimal asset allocation depends on market and investor needs.
  - equation: \sum_{t=0}^{T} \gamma^t r_t
    explanation: Objective function for maximizing cumulative discounted reward in RL.
  - equation: B_s
    explanation: Bias score quantifying influence of a behavioral bias on decisions.
definitions:
  - term: Robo-advisor
    definition: Automated investment platform using algorithms to manage portfolios.
  - term: Reinforcement Learning (RL)
    definition: ML paradigm where agents learn optimal actions through trial and error to maximize rewards.
  - term: NLP
    definition: Natural Language Processing, analyzing textual data for sentiment and insights.
  - term: XAI
    definition: Explainable AI, focusing on transparent and interpretable model decisions.
  - term: Federated Learning
    definition: Decentralized model training across datasets without sharing raw data.
critical_citations:
  - "[Shetty et al., 2026] — Foundational work on robo-advisors and personalization."
  - "[Shen et al., 2025] — Empirically validates AI-driven wealth management models."
  - "[Tahvildari, 2025] — Systematic review of generative AI in robo-advisory."
  - "[Rizinski and Trajanov, 2025] — Comprehensive review of AI agents in finance."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Reviews AI techniques for profiling investor risk and behavior.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: Discusses dynamic risk assessment adapting to evolving preferences.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Compares clustering and classification for investor segmentation.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Covers ML models predicting market trends and investor behavior.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: contextual
      justification: Mentions predictive modeling broadly but not specific spending data.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: Asset allocation strategies provide indirect domain knowledge for budgeting.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Focuses on investment allocation, not direct budget recommendations.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Touches on risk and volatility but not explicit anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: References market volatility but not specific anomaly algorithms.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Discusses encryption, access controls, and regulatory compliance.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Emphasizes explainability and transparency to build user trust.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Mentions user engagement and satisfaction via personalization.
  contribution: This paper reviews AI-driven asset allocation, directly justifying Odin's use of RL and deep learning for adaptive financial planning. It supports Odin's risk profiling module by highlighting AI-enhanced investor segmentation and behavioral integration. The review's emphasis on explainability and privacy informs Odin's trust and security design. Findings on dynamic allocation validate Odin's forecasting and optimization components.
  directly_justifies:
    - "Reinforcement learning agents can adapt asset allocations to individual investor profiles and market changes."
    - "Deep learning models capture temporal dependencies for predictive financial modeling."
    - "AI-driven risk assessment improves upon static questionnaires by analyzing behavioral data."
    - "Integrating behavioral finance principles mitigates cognitive biases in financial decisions."
    - "Explainable AI is critical for user trust and regulatory compliance in robo-advisory."
  limits:
    - "Focuses on investment asset allocation, not directly on personal expense categorization or savings goals."
    - "Does not provide empirical evaluation on Filipino-specific financial behaviors or contexts."
    - "Lacks detailed implementation guidance for integrating AI into mobile-first PFMS."
    - "Does not address cold-start baselines for anomaly detection or profile initialization."
  mapping_rationale: The systematic scan across all 12 functional domains identified relevance primarily in Behavioral Profiling, Forecasting, Budgeting, Data Privacy, and Engagement. Topics 5.A, 5.C, and 6.A were flagged as high due to direct coverage of AI-based risk profiling and predictive modeling. Topics 10.A and 10.B were high given the extensive discussion on privacy and trust. Topic 5.B and 11.A were medium for dynamic profiling and user engagement. Topics 7.B, 8.A, and 8.B were low/contextual as the paper focuses on investments rather than budgeting or anomaly detection. Domains like Filipino Cultural Context and Mobile-First Design were rejected as the paper is international and not context-specific. The overall relevance is medium-high for Odin's algorithmic and trust-related modules but limited by its investment-specific focus and lack of Filipino data.
limitations:
  - "Generalizes findings from international contexts; may not apply to Filipino young professionals. [unacknowledged]"
  - "Focuses on asset allocation, not expense categorization or savings management."
  - "Does not address cold-start or low-data scenarios common in PFMS. [unacknowledged]"
  - "Lacks specific recommendations for mobile-first UX design."
  - "Does not evaluate performance on Philippine financial data. [unacknowledged]"
remember_this:
  - "RL and deep learning enhance adaptive asset allocation and risk profiling."
  - "AI-driven personalization improves investment outcomes over static approaches."
  - "Explainability and privacy are critical barriers to AI adoption in finance."
  - "Behavioral biases can be mitigated through AI-driven nudges and personalized strategies."
  - "Future robo-advisors will integrate alternative data and federated learning for personalization."
```
---

## Paper 17: Krishnan & Sreeja_summarized.md

**Source File:** `Krishnan & Sreeja_summarized.md`

```yaml
paper_id: 10.1109/ACCESS.2026.3695458
designation: international-algorithm-specific
title: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems: A Formal Framework for Continuous Verification
authors: Krishnan, V.; Sreeja, C.S.
year: 2026
venue: IEEE Access
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 8.A
  - 8.B
  - 8.C
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
  - 12.C
tldr: A Zero-Trust Hybrid Adaptive Authentication (ZeTHAA) framework integrating continuous authentication, probabilistic risk modeling, and dual-policy thresholds for security-usability trade-offs.
problem_and_motivation: Existing adaptive authentication systems lack formal mathematical models for continuous trust evolution, often relying on heuristic scoring and binary decisions. This gap leads to either excessive user friction or inadequate security, especially in post-login authorization.
approach:
  - The ZeTHAA framework models trust as a continuous, time-evolving state variable rather than a binary policy outcome.
  - It integrates a composite attribute set covering user, device, application, and contextual signals into a unified risk metric.
  - Attribute importance and penalties are dynamically derived from entropy and Beta-posterior distributions, enabling robust cold-start initialization.
  - A global admissibility predicate distinguishes hard violations from soft probabilistic violations for clear enforcement.
  - The system incorporates retry dynamics with exponential risk escalation and temporal decay into a unified threat model.
  - Evaluation uses a large-scale synthetic dataset with realistic authentication flows and adversarial patterns against multiple baselines.
findings:
  - num: ZeTHAA outperformed baselines with Recall and Area Under the Curve (AUC) exceeding 79% and 15.1%, respectively.
  - num: F1-Scores showed increases of 48%-147%, with efficiency boost of 20-65%, while reducing the cost per attack by up to 39.6%.
  - num: Benchmarks against frameworks from Dasu et al. and Matiushin et al. showed a 57.5% lead in F1-Score.
  - num: ZeTHAA blocked 70.78% more attacks than comparable frameworks.
  - The framework achieves a 33% reduction in Equal Error Rate compared to a heuristic approach.
  - The risk distribution shows a clear separation between benign and attack events, enabling logical threshold placement.
  - Detection latency is immediate with a 95th percentile delay of 0 events for strong contextual signals.
key_figures_tables:
  - Figure 1: ZeTHAA system architecture highlighting the composite attribute set and policy enforcement points → Shows integration of continuous monitoring and authorization.
  - Figure 2: Feature importance from Bayesian calibration → Attack campaign and geo-anomaly signals dominate risk.
  - Figure 3: Risk score distribution by class → Clear separation between benign and attack sessions.
  - Figure 4: Policy decision with risk score distribution → Shows the three decision regions: allow, step-up, block.
  - Figure 5: ROC curve comparison across models → ZeTHAA achieves highest TPR at low FPR.
  - Figure 6: Risk-trust correlation → High risk correlates with low trust, diagonal trend supports classification.
  - Figure 8: Cost vs attack detection recall → Framework balances security and usability effectively.
  - Table 13: Performance metrics → ZeTHAA achieves 0.735 recall, 0.874 AUC, F1-score of 0.761.
  - Table 21: Performance comparison between baselines → ZeTHAA leads in recall and AUC.
key_equations:
  - equation: T(t) = (1 - λ^+ - λ^+·C(t) - γ)·T(t-) + R(t)
    explanation: Dynamic trust update based on context and risk.
  - equation: Pr[AttackSuccess|C(t)] = 1 - (1 - Pr[Attack_auth|C(t)])·(1 - Pr[Attack_authz|C(t)])
    explanation: Unified attack success probability combining authentication and authorization phases.
  - equation: Trust(C(t)) = Σ w_i(t) Indicator[match(a_i)] - Σ π^miss_i(t) Indicator[missing(a_i)] - Σ π^mm_i(t) Indicator[mismatch(a_i)]
    explanation: Trust as weighted positive evidence minus penalties for missing/mismatched attributes.
definitions:
  - term: Zero-Trust Hybrid Adaptive Authentication (ZeTHAA)
    definition: A framework integrating contextual attributes, authentication strength, behavioral evidence, and retry dynamics for continuous authentication and authorization.
  - term: Global Admissibility Predicate
    definition: A system-wide safety invariant that distinguishes hard violations from soft violations, enabling deterministic security responses.
  - term: Trust
    definition: A continuous, time-evolving, and bounded state variable representing accumulated confidence in a session context.
  - term: Risk
    definition: The estimated probability of adversarial success, distinct from trust, used in authorization decisions.
  - term: Hard Violation
    definition: A non-compensable state (e.g., impossible travel, cryptographic failure) that triggers immediate access denial and session termination.
  - term: Soft Violation
    definition: A statistically unlikely but plausible behavioral deviation that incurs penalties but does not terminate the session.
  - term: Attribute Penalty
    definition: A reactive measure reducing effective trust when contextual attributes mismatch or are missing from expectations.
  - term: Authentication Penalty
    definition: A reactive measure reducing effective authentication assurance due to failures, degradation, or fallback behavior.
critical_citations:
  - "[Dasu et al., 2023] — Heuristic risk scoring with static weights."
  - "[Matiushin and Korkhov, 2025] — ML-empowered RBA with dynamic threshold."
  - "[Rose et al., 2020] — NIST SP 800-207 Zero Trust Architecture principles."
  - "[Temoshok et al., 2025] — NIST SP 800-63 Digital Identity Guidelines."
  - "[Wiefling et al., 2020] — Study on usability and security of risk-based authentication."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Formalizes continuous, time-evolving trust states as behavioral profiles.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: high
      justification: Introduces robust cold-start initialization via entropy and Bayesian priors.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Uses ML strictly for evidence interpretation, not direct decision-making.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Models trust and risk evolution with temporal decay and reinforcement.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Provides a formal anomaly detection framework with hard/soft violations.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Evaluates anomaly detection performance against multiple baselines.
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: high
      justification: Addresses cold-start with Beta-posterior and uniform initialization.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Framework is designed for mobile contexts with device attestation.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Balances security and usability with step-up authentication mechanisms.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Aligns with NIST standards and includes application/device integrity checks.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Models trust as a continuous state to improve user confidence.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses comprehensive metrics including ROC, EER, and operational efficiency.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Evaluates algorithmic components against heuristic and ML baselines.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: contextual
      justification: Provides methodology applicable to evaluating decision-making systems.
  contribution: "The framework formalizes continuous trust computation for adaptive authentication, directly applicable to Odin's behavioral profiling and anomaly detection modules. Its cold-start initialization strategy provides a robust baseline for new users, addressing the cold-start problem in financial behavior modeling. The separation between hard and soft violations informs Odin's design for handling both extreme anomalies and gradual behavioral shifts. The composite attribute set and policy-driven thresholds offer a blueprint for Odin's expense categorization and budget recommendation systems. The unified threat model and attack surface analysis provide a security foundation for Odin's data privacy and user trust modules."
  directly_justifies:
    - "Continuous trust evaluation is essential for Zero-Trust systems and should replace binary decisions in financial applications."
    - "Attribute weights must be dynamically recalibrated using Bayesian learning, not static heuristics."
    - "A global admissibility predicate is required to distinguish impossible states from probabilistic anomalies."
    - "Retry dynamics and temporal decay should be modeled explicitly in threat surfaces."
    - "Multi-threshold decision regions improve security-usability trade-offs compared to single-threshold approaches."
  limits:
    - "Evaluation is conducted on a synthetic dataset, which may not fully capture real-world behavioral complexity."
    - "The framework assumes availability of device capabilities (e.g., TEE, FIDO2) that may not be present in all contexts."
    - "Authentication strength mappings to NIST AALs are indicative and may require calibration for specific implementations."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was conducted. The paper directly addresses behavioral profiling and anomaly detection (Domains 5 and 8) with high relevance, as it formalizes continuous trust states and hard/soft violation handling. It also provides strong justification for mobile-first design and data privacy (Domains 9 and 10) through its focus on device attestation and NIST alignment. The framework's evaluation methodology (Domain 12) is directly applicable to Odin's system evaluation needs. Topics related to expense categorization (Domain 3) and budget recommendation (Domain 7) were considered but rejected, as the paper focuses on authentication rather than financial allocation. Savings and debt management (Domain 13) were considered contextual at best. The paper's contributions to predictive modeling (Domain 6) and engagement (Domain 11) are secondary but relevant. Borderline cases: The paper's treatment of 'trust' as a cumulative state could inform spending pattern modeling (2.D), but the connection is indirect, so it was not selected. Overall, the paper provides high-value methodological and algorithmic insights for Odin's behavioral profiling, anomaly detection, and security architecture."
limitations:
  - "The evaluation relies on a synthetic dataset, limiting generalizability to real-world user behavior. [unacknowledged]"
  - "The framework assumes device capabilities that may not be available in all contexts, such as TEE and FIDO2 support. [unacknowledged]"
  - "Authentication strength mappings are indicative and may require recalibration for specific enterprise deployments."
  - "The dataset does not include long-term behavioral drifts, which could affect profile adaptation strategies. [unacknowledged]"
  - "Computational overhead of continuous monitoring and Bayesian updates is not fully characterized for resource-constrained devices. [unacknowledged]"
  - "The framework does not address user acceptance of continuous step-up challenges, which may impact engagement. [unacknowledged]"
remember_this:
  - "ZeTHAA achieves 15.1% higher AUC and 57.5% better F1-Score than heuristic RBA methods."
  - "Dual thresholds reduce false blocking by 70.78% while maintaining high attack detection."
  - "Continuous trust computation with Bayesian learning enables robust cold-start anomaly detection."
  - "Hard and soft violation separation allows deterministic security responses for impossible states."
  - "Framework aligns with NIST Zero Trust principles, extending security beyond authentication into resource access."
```
---

## Paper 18: Dela Cruz_summarized.md

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

## Paper 19: Rajulapati et al_summarized.md

**Source File:** `Rajulapati et al_summarized.md`

```yaml
paper_id: 10.47738/ijaim.v6i2.123
designation: international-algorithm-specific
title: Continual Learning for Human–AI Collaborative Learning Analytics under Behavioral Drift
authors: Rajulapati, A.; Sridevi, V.; Prasad, S. R.
year: 2026
venue: International Journal for Applied Information Management
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 8.C
  - 10.B
  - 12.A
  - 12.B
tldr: Continual learning with drift-aware updates improves predictive stability and fairness in semester-spanning educational analytics.
problem_and_motivation: Static predictive models degrade as student behavior evolves across semesters, yet deployed learning analytics rarely monitor or adapt to drift. This limits reliability for adaptive interventions and risks unfair outcomes under shifting distributions.
approach:
  - 14-semester longitudinal panel with 812–936 students and 18–21 courses per semester was constructed from LMS traces.
  - Drift was quantified using KL divergence on behavioral features including practice attempts, timeliness, and session regularity.
  - A drift-aware continual learning framework used replay buffers and parameter regularization to update models only when drift exceeded a threshold.
  - Semester-forward evaluation compared static, periodic retraining, and drift-aware continual policies on macro-F1, AUROC, and calibration.
  - Fairness was assessed via recall gaps across subgroups under drift.
findings:
  - num: Drift-aware continual learning achieved mean macro-F1 of 0.742 and worst-semester macro-F1 of 0.711, compared to 0.706 and 0.652 for static models.
  - num: Calibration error improved from 0.056 (static) to 0.039 under continual learning.
  - num: Risk precision and recall at fixed intervention capacity increased from 0.62 to 0.69 and 0.48 to 0.56.
  - num: Mean subgroup recall gap was reduced from 0.118 to 0.082.
  - Drift concentrated in practice attempts, submission timeliness, and session regularity, with a regime shift mid-sequence.
key_figures_tables:
  - Figure 7: Predictive performance over semesters → Drift-aware continual learning maintains flatter macro-F1 trajectory than static or periodic retraining.
  - Figure 8: Calibration error across weeks → Continual learning reduces miscalibration spikes during drift episodes.
  - Figure 9: Subgroup recall gap across semesters → Continual learning stabilizes and reduces recall disparities.
  - Table 7: Aggregate performance summary → Drift-aware continual learning has highest mean (0.742) and worst-semester (0.711) macro-F1.
  - Table 9: Subgroup error summary → Continual learning yields lowest mean recall gap (0.082) and max gap (0.121).
key_equations:
  - equation: D_KL(P_t || P_{t+1}) = \sum_k P_t(k) \log \frac{P_t(k)}{P_{t+1}(k)}
    explanation: KL divergence quantifies behavioral drift magnitude between consecutive semesters.
  - equation: \min_\theta L_{t+1}(\theta) + \lambda \sum_j \omega_j (\theta_j - \theta_{t,j})^2
    explanation: Continual learning objective combines current loss with parameter regularization.
  - equation: m \pm 1.96 \frac{s_m}{\sqrt{K}}
    explanation: Confidence interval for mean performance across evaluated semesters.
definitions:
  - term: Concept Drift
    definition: Change in joint distribution of inputs and targets over time.
  - term: Continual Learning
    definition: Sequential model updating that mitigates catastrophic forgetting via replay or regularization.
  - term: Semester-Forward Evaluation
    definition: Training on past semesters and testing on future semesters to simulate deployment.
  - term: Expected Calibration Error (ECE)
    definition: Mean absolute difference between predicted probabilities and observed frequencies.
  - term: Replay Buffer
    definition: Curated memory of prior samples used to retain historical knowledge during updates.
critical_citations:
  - "[Gama et al., 2014] — Foundational survey on concept drift adaptation strategies."
  - "[Lu et al., 2018] — Framework for drift detection and adaptation as a lifecycle problem."
  - "[Delange et al., 2021] — Comprehensive survey of continual learning approaches."
  - "[Deho et al., 2024] — Shows dataset drift impacts fairness in learning analytics."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Behavioral drift monitoring parallels financial profile evolution.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: Semester-to-semester drift mirrors cold-start challenges in financial behavior modeling.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: contextual
      justification: Classification under drift is addressed but not specific to financial profiles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly addresses maintaining predictive accuracy under evolving behavioral patterns.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Drift-aware updating and replay strategies are applicable to sequential financial data.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Drift-aware calibration improves risk ranking, analogous to anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Framework for detecting distributional shifts can be adapted for spending anomalies.
    - code: 8.C
      name: Cold‑Start Baseline Strategies for Anomaly Detection
      relevance: contextual
      justification: Replay buffers provide a retention mechanism relevant to cold-start baselines.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: Mentions trust via stable interpretability and reduced alert volatility.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Semester-forward protocol and rolling evaluation are applicable to PFMS evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Detailed comparison of static, periodic, and drift-aware continual learning modules.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: contextual
      justification: Evaluation methodology is general and not specific to budget recommendation.
  contribution: The paper provides a drift-aware continual learning framework that directly informs Odin's forecasting module by demonstrating how to maintain predictive stability under behavioral change. Its rigorous semester-forward evaluation protocol offers a template for assessing Odin's algorithmic modules over time. The fairness analysis under drift validates the importance of monitoring subgroup disparities, which is relevant to Odin's behavioral profiling and anomaly detection. The replay-based retention mechanism offers a practical approach to handling cold-start issues in sequential spending data.
  directly_justifies:
    - "Drift-aware updating stabilizes predictive performance under evolving behavioral patterns."
    - "Continual learning with replay buffers reduces catastrophic forgetting in sequential domains."
    - "Fairness disparities can widen under drift, necessitating monitoring of subgroup recall gaps."
    - "Calibration error should be tracked alongside accuracy to ensure reliable risk scores."
    - "Selective adaptation based on drift thresholds balances robustness with operational overhead."
  limits:
    - "The study is situated in educational analytics, not personal finance, so behavioral constructs differ."
    - "The dataset is institutional and may not generalize to individual spending behavior."
    - "Only semester-level drift is analyzed; finer-grained drift patterns remain unexplored."
    - "The framework assumes labeled outcomes are available per semester, which may not hold for financial data."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes flagged Forecasting, Anomaly Detection, and Evaluation as most relevant. Under Forecasting (6.A, 6.B), the paper directly informs sequential modeling under drift. For Anomaly Detection (8.A, 8.B), the calibration and risk ranking improvements are analogous to anomaly scoring stability. Evaluation (12.A, 12.B) benefits from the semester-forward protocol and ablation analysis. Behavioral Profiling (5.A, 5.B) is medium relevance due to drift dynamics, though the behavioral features differ. User Trust (10.B) is low relevance, mentioned only indirectly via stability. Domains related to Filipino cultural context, expense categorization, existing systems, mobile design, privacy, retention, savings, and debt management were not addressed. The paper is thus primarily methodological, offering transferable techniques for adaptation and evaluation in dynamic behavioral domains.
limitations:
  - "Educational context may not map directly to personal finance behavior. [unacknowledged]"
  - "The study does not address individual-level heterogeneity beyond subgroup analysis. [unacknowledged]"
  - "Deployment constraints such as real-time latency or mobile-first concerns are not discussed. [unacknowledged]"
  - "The privacy-preserving aspects are limited to pseudonymization and access control. [unacknowledged]"
remember_this:
  - "Drift-aware continual learning improves worst-semester macro-F1 from 0.652 to 0.711."
  - "Calibration error reduced from 0.056 to 0.039 under drift-aware updating."
  - "Mean subgroup recall gap decreased from 0.118 to 0.082 with continual learning."
  - "Intermediate drift thresholds balance robustness with update frequency."
  - "Replay buffers of moderate size provide near-peak performance with low overhead."

```
---

## Paper 20: Montagna_summarized.md

**Source File:** `Montagna_summarized.md`

```yaml
paper_id: 70d5269c-1cbd-5b71-afa6-86550a29e2e4
designation: international-algorithm-specific
title: Integration of Explainability in Recommender Systems to Enhance Enterprise Value Strategies
authors: Montagna, A.
year: 2026
venue: University of Padova
odin_topics:
  - 4.A
  - 4.B
  - 7.A
  - 7.B
  - 7.D
  - 9.A
  - 9.B
  - 10.A
  - 10.B
tldr: A comprehensive thesis that surveys Value-Aware Recommender Systems, proposes an explainable value-aware matrix factorization model, and critiques the evaluation of explanations in graph-based recommenders for enterprise contexts.
problem_and_motivation: Recommender systems are widely used but often lack transparency and fail to align with business value objectives. Value-aware systems exist but have not been systematically surveyed, and a key gap remains in balancing the generation of business value with the need for explainable, trustworthy recommendations. This research addresses this gap by creating a bridge between these perspectives through novel models and evaluation frameworks.
approach:
  - A systematic literature review following PRISMA guidelines was conducted to survey and classify Value-Aware Recommender Systems (VARSs), analyzing 109 studies.
  - A novel model, Explainable Value-aware Matrix Factorization (XVMF), is proposed to balance explainability and business value by integrating both terms into a unified objective function.
  - The model is evaluated on Yelp and Amazon datasets using NDCG, E-NDCG, and a novel NDCV metric to assess accuracy, explainability, and business value trade-offs.
  - A critical analysis of Graph-Based Explainable Recommender Systems (GxRSs) is performed, highlighting the lack of quantitative evaluation methods for explanation quality.
findings:
  - num: The systematic review identified 109 relevant studies on VARSs, which are classified into in-processing and post-processing techniques.
  - The proposed XVMF model successfully balances explainability and business value, achieving performance that exceeds baseline MF and EMF models on the Yelp dataset.
  - num: For the Yelp dataset, the XVMF model achieved an NDCV of 0.5042% and an E-NDCG of 1.9954%, outperforming the baseline models.
  - num: On the Amazon dataset, the XVMF-e model achieved an E-NDCG of 0.1723%, a significant improvement over EMF, while the XVMF-v model achieved an NDCV of 0.1154%.
  - A key finding is that the optimal balance between explainability and value is achieved at low regularization parameter values, after which performance degrades quickly.
  - The analysis of GxRSs reveals that most papers rely on qualitative case-based analyses, with only a few employing quantitative metrics for explanation evaluation.
  - The thesis proposes that future work on GxRSs should adopt standardized quantitative metrics to ensure comparability and rigorous evaluation.
key_figures_tables:
  - "Figure 2.1: PRISMA flow diagram summarizing the systematic literature review process → 109 studies were included in the final review."
  - "Figure 2.2: Taxonomy of value-aware recommender algorithms → Divides VARSs into in-processing and post-processing methods."
  - "Table 2.1: Application domains of value-aware recommender systems → Shows product, advertising, news, and media as key domains."
  - "Figure 3.1-3.4: Performance analysis for Yelp and Amazon datasets → Show the trade-off and optimal balance between explainability and value regularization."
  - "Table 3.5 and 3.6: Evaluation metrics for MF, EMF, and XVMF → XVMF outperforms baselines, particularly on the Yelp dataset."
key_equations:
  - equation: |
      G_{expl} = \sum_{u,i \in R} (r_{ui} - a_u b_i^T)^2 + \frac{\beta}{2} (\| a_u \|^2 + \| b_i \|^2) + \lambda \| a_u - b_i \|^2 E_{ui}
    explanation: Objective function for explainable matrix factorization, incorporating an explainability regularization term.
  - equation: |
      L = \sum_{(u,i) \in S} (r_{u,i} - p_u \cdot q_i^T)^2 + \frac{\beta}{2} (\| p_u \|^2 + \| q_i \|^2) + \| p_u - q_i \|^2 (\lambda W_{u,i} + \delta v_i)
    explanation: Objective function for the proposed XVMF model, balancing explainability and business value.
  - equation: |
      \text{NDCV} = \sum_{i=1}^{k} \frac{2^{rel_i} - 1}{\log_2 (i+1)}
    explanation: Novel metric to evaluate the business value of a recommendation list, based on the gain from the item's value.
definitions:
  - term: VARS
    definition: Value-Aware Recommender System, designed to directly maximize the economic value of recommendations.
  - term: xRS
    definition: Explainable Recommender System, which provides reasons or evidence for its recommendations.
  - term: XVMF
    definition: Explainable Value-aware Matrix Factorization, a novel model proposed in this thesis to balance explainability and business value.
  - term: E-NDCG
    definition: Explainable Normalized Discounted Cumulative Gain, a metric for evaluating the explainability quality of a ranked recommendation list.
  - term: NDCV
    definition: Normalized Discounted Cumulative Value, a novel metric proposed to evaluate the business value generated by a recommendation list.
  - term: GxRS
    definition: Graph-Based Explainable Recommender System, a system that uses graph structures to generate and explain recommendations.
  - term: MEP
    definition: Mean Explainability Precision, a quantitative metric to evaluate the explainability of recommendations.
critical_citations:
  - "[Page et al., 2021] — PRISMA guidelines for systematic reviews."
  - "[Ricci et al., 2022] — Overview of recommender systems techniques."
  - "[Abdollahi and Nasraoui, 2016] — Basis for explainable matrix factorization (EMF)."
  - "[Coba et al., 2019] — Basis for E-NDCG and NEMF model."
  - "[De Biasio et al., 2023] — The first systematic review of VARSs."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Surveys existing VARSs, providing a landscape of systems optimizing business value.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies the gap between business value optimization and explainability in current systems.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: Discusses business value optimization, a key driver for budget recommendation strategies.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: The thesis focuses on recommender systems in general, but the principles are transferable to budget recommendations.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: low
      justification: The XVMF model involves trade-offs between objectives, related to handling competing priorities.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Emphasizes the importance of human-centered design and trust in user adoption of AI systems.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: Discusses interface design for explanations, which is relevant to UX in general.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Focuses on trustworthy AI principles, including privacy and security.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: A central theme of the thesis is that explainability builds user trust and system adoption.
  contribution: "This thesis contributes to Odin's design by providing a systematic survey of value-aware systems, which can inform the development of Odin's budget recommendation and anomaly detection modules. The proposed XVMF model offers a concrete, data-driven approach for balancing user preference accuracy with business value, directly applicable to Odin's core functionality of generating personalized financial plans. Furthermore, the critical analysis of explanation evaluation in graph-based systems provides a methodological blueprint for ensuring that Odin's recommendations are not only accurate but also transparent and trustworthy. Finally, the emphasis on human-centered evaluation and user interfaces is crucial for designing Odin's mobile-first application to foster user engagement and trust."
  directly_justifies:
    - "The proposed XVMF model can be adapted to balance recommendation accuracy with Odin's business goals of user retention and savings growth."
    - "Systematic review of VARSs identifies key algorithms and datasets relevant for building Odin's value-optimization modules."
    - "Analysis of GxRSs highlights the need for quantitative explainability metrics, guiding Odin's evaluation framework."
  limits:
    - "The experimental validation of XVMF is limited to Yelp and Amazon datasets, which may not fully represent the financial behavior of Filipino young professionals."
    - "The qualitative limitations of existing explainability evaluations in GxRSs are noted, but a new comprehensive metric is not proposed."
    - "The thesis focuses on algorithm performance and does not include an end-to-end user study in a real-world business setting."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The 'Existing Systems & Gaps' domain was flagged as highly relevant (topics 4.A, 4.B), as the thesis directly surveys VARSs and identifies the specific gap in explainable value-aware systems. The 'Budget Recommendation' domain (topics 7.A, 7.B, 7.D) was considered relevant due to the focus on optimizing economic value and balancing competing objectives, though the application is not specific to budgeting. The 'Mobile-First Design' and 'Data Privacy & User Trust' domains (topics 9.A, 9.B, 10.A, 10.B) are medium to low relevance, as the thesis discusses trust and interface design in the context of explainability, which is a key principle for Odin. Domains like 'Filipino Cultural Context' (2.A-D), 'Expense Categorization' (3.A-C), 'Behavioral Profiling' (5.A-C), 'Spending Forecasting' (6.A-B), 'Anomaly Detection' (8.A-C), 'Engagement & Retention' (11.A-B), 'System Evaluation' (12.A-C), and 'Savings & Debt Management' (13.A-C) were considered and rejected as the thesis does not directly address these specific areas, focusing instead on recommender system algorithms and their evaluation in a general enterprise context. The overall relevance to Odin is high, as it provides both a foundational survey of value-aware systems and a novel model for balancing key performance objectives."
limitations:
  - "The systematic review is based on articles from specific databases and excludes non-English and unpublished works. [unacknowledged]"
  - "The datasets used for XVMF (Yelp, Amazon) do not contain Filipino user data, limiting direct applicability to the target demographic. [unacknowledged]"
  - "The evaluation of XVMF is offline and does not include online A/B testing or user studies to validate real-world performance. [unacknowledged]"
  - "The thesis criticizes the lack of quantitative evaluation in GxRSs but does not itself propose a new, comprehensive metric to address this gap."
remember_this:
  - "Value-aware recommender systems are a distinct class that directly optimize economic value."
  - "The XVMF model successfully balances explainability and business value on benchmark datasets."
  - "Offline evaluation metrics for business value and explainability are critical for model selection."
  - "Current graph-based explainable recommenders lack rigorous quantitative evaluation of their explanations."
  - "Balancing user trust and system adoption is a key challenge for enterprise recommender systems."
```
---

## Paper 21: Jiang et al_summarized.md

**Source File:** `Jiang et al_summarized.md`

```yaml
paper_id: 10.1109/ACCESS.2026.3670857
designation: international-algorithm-specific
title: A Dynamic Framework for Causal User Profiling and Treatment Segmentation via Uplift Modeling in Internet Lending
authors: Jiang, J.; Abdul Hamid, N. W.; Yap, N. K.; Chong, C. W.
year: 2026
venue: IEEE Access
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 7.B
  - 7.C
  - 8.B
  - 9.A
  - 9.B
  - 12.B
tldr: An integrated Causal User Profiling (CUP) framework combines causal inference and uplift modeling to segment users into four response types, improving personalized intervention targeting.
problem_and_motivation: Conventional user profiling is descriptive and correlation-based, failing to predict how users respond to interventions. This limits personalization in internet lending, as platforms cannot distinguish users who are truly responsive to actions from those with high baseline propensities.
approach:
  - The CUP framework integrates feature selection, stratified clustering, confounding adjustment, and causal effect estimation into a single pipeline.
  - Hybrid feature selection combines Information Value, Causal Forest importance, Population Stability Index, and Stepwise refinement.
  - A C2 replacement strategy for clustering stabilizes weak clusters by reverting to global model predictions when local performance degrades.
  - Causal effects are estimated using meta-learners (T-, S-, X-, R-, DR-) and Causal Forests, with Logistic Regression as the preferred base learner.
  - Users are classified into four response types (Persuadable, Sure Thing, Lost Cause, Do-Not-Disturb) using a hybrid causal-behavioral labeling procedure.
  - The framework is evaluated on six months of proprietary internet-lending data using a rolling train/validation/test protocol and AUUC as the primary metric.
findings:
  - num: Hybrid feature selection increases AUUC by 25–30% compared to using all features.
  - num: The C2 clustering strategy provides an additional 10–12% uplift in AUUC.
  - num: The DR-Learner with Logistic Regression yields a further 5–8% improvement in AUUC.
  - num: The full integrated CUP pipeline achieves 45–50% higher AUUC than the baseline model.
  - The X-Learner demonstrates the most consistent improvement under clustering, while the DR-Learner shows higher variance.
  - Clustering based on causal features produces more coherent and stable treatment heterogeneity than clustering based on predictive features alone.
key_figures_tables:
  - Figure 1: Traditional vs. CUP roadmap → CUP adds clustering, bias adjustment, causal estimation, and response-type labeling.
  - Figure 5: Distribution of four causal response types → Persuadables and Lost Causes are the most prevalent segments.
  - Figure 6: Feature-selection and meta-learner interactions → DR-Learner with IV+Causal features achieves highest AUUC.
  - Figure 7: Clustering strategies and meta-learner performance → C2 strategy ranks highest in stability and performance.
  - Figure 8: Meta-Learner × Base-Learner heatmap → DR-Learner + Logistic Regression offers the best balance of accuracy and stability.
key_equations:
  - equation: u = \hat{p}_1 - \hat{p}_0
    explanation: Uplift score as the difference in outcome probabilities between treatment and control.
  - equation: WeightedAUUC = \sum_{k=1}^K w_k \cdot AUUC_k
    explanation: Weighted average of cluster-level AUUC by sample proportion.
definitions:
  - term: CUP
    definition: Causal User Profiling, an integrated framework combining causal inference, uplift modeling, and user profiling.
  - term: CATE
    definition: Conditional Average Treatment Effect, the expected causal effect conditional on observed covariates.
  - term: HTE
    definition: Heterogeneous Treatment Effect, variation in treatment effects across individuals or subgroups.
  - term: AUUC
    definition: Area Under the Uplift Curve, a metric for evaluating uplift model ranking performance.
  - term: AAUC
    definition: Average AUUC across multiple monthly evaluation windows.
  - term: PSI
    definition: Population Stability Index, a measure of temporal distributional shift in features.
  - term: IV
    definition: Information Value, a measure of predictive relevance for a binary target.
  - term: IPW
    definition: Inverse Probability Weighting, a method for adjusting for treatment assignment bias.
  - term: DR-Learner
    definition: Doubly Robust Learner, a meta-learner that combines outcome and propensity models for causal estimation.
critical_citations:
  - "[Radcliffe & Surry, 2011] — Defined the four-type response taxonomy for uplift modeling."
  - "[Athey & Imbens, 2016] — Introduced Causal Trees for heterogeneous treatment effect estimation."
  - "[Wager & Athey, 2018] — Extended Causal Forests for consistent CATE estimation."
  - "[Künzel et al., 2019] — Developed the meta-learner framework for flexible HTE estimation."
  - "[Devriendt et al., 2018] — Surveyed uplift modeling and emphasized upstream design choices."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Proposes a four-type response taxonomy (Persuadable, Sure Thing, Lost Cause, Do-Not-Disturb) grounded in causal potential outcomes, directly defining behavioral profiles for intervention responsiveness.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: high
      justification: Addresses temporal stability of user profiles across monthly deployments and provides a reproducible pipeline that can support cold-start labeling with observed data.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Evaluates meta-learners (T, S, X, DR) and base learners (LR, RF, GBDT, XGB) for classifying users into causal response types.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Uses uplift modeling and Causal Forests to predict individual treatment effects, directly applicable to forecasting user responses to interventions.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: The rolling monthly evaluation design and temporal stability analysis are relevant for sequential forecasting, though the paper focuses on treatment effects rather than spending amounts.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: The segmentation of users into Persuadables vs. Sure Things can inform budget recommendations by identifying which users are likely to respond to nudges.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: contextual
      justification: The CUP framework enables targeting optimization by identifying Persuadables, but does not explicitly formulate budget constraints.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: While not focused on anomaly detection, the CUP framework’s capability to identify Do-Not-Disturb users could inform baseline models for anomaly detection.
    - code: 9.A
      name: Mobile‑First Design Principles and Rationale
      relevance: low
      justification: The paper uses mobile app data from an internet lending platform and discusses personalization, but does not explicitly address mobile-first design principles.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: The study is grounded in a mobile platform context, but the UX implications of the profiling framework are not a focus.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Conducts component-wise ablation analysis to quantify the marginal contribution of feature selection, clustering, and meta-learner configuration to AUUC.
  contribution: The CUP framework directly justifies Odin's design of a behavioral profiling module that classifies users into causal response types for personalized interventions. It provides a methodology for estimating heterogeneous treatment effects that can be embedded in Odin's forecasting and recommendation modules. The component-wise ablation analysis offers a reproducible evaluation strategy for Odin's algorithmic modules. The emphasis on temporal stability and interpretability aligns with Odin's need for reliable user profiles over time. The framework's ability to separate Persuadables from Sure Things is critical for designing cost-effective budget nudges and retention mechanisms.
  directly_justifies:
    - "Users can be classified into Persuadable, Sure Thing, Lost Cause, and Do-Not-Disturb categories based on causal treatment effects."
    - "Feature selection using Information Value and causal importance improves uplift model performance by 25–30%."
    - "The C2 clustering strategy stabilizes weak clusters and provides an additional 10–12% uplift gain."
    - "The DR-Learner with Logistic Regression offers the best balance of accuracy and stability for causal user profiling."
    - "Component-wise ablation is necessary to quantify the contribution of each pipeline module to overall performance."
  limits:
    - "The dataset is from a single Chinese internet lending platform, limiting generalizability to other financial contexts or Filipino users."
    - "The treatment variable aggregates multiple intervention types, obscuring intervention-specific causal mechanisms."
    - "Formal statistical significance testing is not conducted; evaluation focuses on temporal consistency and magnitude of differences."
    - "Fairness, transparency, and ethical deployment considerations are not addressed. [unacknowledged]"
  mapping_rationale: All 12 functional domains and their associated topic codes were systematically scanned against the paper's contributions. The paper is highly relevant to Behavioral Profiling & Classification (5.A, 5.B, 5.C) as it proposes and evaluates a four-type causal response taxonomy. It is also highly relevant to Spending Forecasting (6.A, 6.B) through its uplift modeling and temporal evaluation. The paper provides medium relevance to Budget Recommendation (7.B, 7.C) by enabling identification of persuadable users for targeted nudges. It offers contextual relevance to Anomaly Detection (8.B) for establishing baselines and low relevance to Mobile-First Design (9.A, 9.B) as the context is a mobile platform but UX is not a focus. The paper strongly justifies Algorithmic Module Evaluation (12.B) through its ablation design. Topics related to Filipino cultural context (2.A, 2.B, 2.C, 2.D) were considered and rejected because the data is from China and the framework is culturally neutral, though its methodology could be adapted. Expense Categorization (3.A, 3.B, 3.C) and Existing Systems (4.A, 4.B) were not addressed directly. Data Privacy (10.A, 10.B), Engagement (11.A, 11.B), and Savings/Debt (13.A, 13.B, 13.C) were not explicitly covered. Overall, the paper is highly relevant to Odin's need for a causally grounded behavioral profiling and forecasting system.
limitations:
  - "The dataset is from a single Chinese internet lending platform, limiting generalizability."
  - "The treatment variable aggregates multiple intervention types, obscuring specific mechanisms."
  - "Formal statistical significance testing is not conducted."
  - "Fairness and ethical deployment considerations are not discussed. [unacknowledged]"
  - "Computational costs are substantial due to extensive ablation experiments, which may not be feasible in resource-constrained settings. [unacknowledged]"
remember_this:
  - "CUP segments users into Persuadable, Sure Thing, Lost Cause, and Do-Not-Disturb types based on causal treatment effects."
  - "Feature selection and C2 clustering contribute 25–30% and 10–12% AUUC gains, respectively."
  - "The DR-Learner with Logistic Regression achieves the best balance of accuracy and stability."
  - "The full CUP pipeline yields 45–50% higher AUUC than baseline uplift modeling."
  - "Clustering is effective only when based on causal features and paired with robust meta-learners."
```
---

## Paper 22: Ma C. et al_summarized.md

**Source File:** `Ma C. et al_summarized.md`

```yaml
paper_id: 10.2139/ssrn.6363518
designation: international
title: Consumers semi-intertemporally make intertemporal decisions: insights from the payday effects
authors: Ma, C.; Gu, Y.; Chong, J. K.
year: 2026
venue: Unknown
odin_topics:
  - 2.D
  - 4.A
  - 5.A
  - 6.A
  - 7.A
  - 10.B
tldr: Consumers without liquidity constraints self-impose monthly mental budgets renewed on paydays, leading to predictable spending cycles that decrease over trips until the next payday.
problem_and_motivation: Traditional economic models assume rational long-horizon intertemporal utility maximization, but consumers are neither fully rational nor completely myopic. The gap is understanding how consumers with no liquidity constraints actually make intertemporal spending decisions, particularly regarding storable goods.
approach:
  - Analyzed individual-level transaction data from a global cosmetic retail chain in a Southeast Asian country from 2011-2015, covering 300 stores and 600,000 members.
  - Employed regression discontinuity design with customer-day-level and trip-level regressions to isolate payday effects.
  - Controlled for customer fixed effects, store fixed effects, year, month, day-of-week, public holidays, and daily discount rates.
  - Compared cash versus credit card users to disentangle liquidity from behavioral effects.
  - Examined multiple dependent variables: expenditure, basket size, new product adoption, product upgrading, and purchase mistakes.
findings:
  - num: Payday shifts up unconditional daily expenditure by 4.7% for all members, driven by higher spending conditional on shopping (3.3% increase per trip) rather than increased shopping likelihood.
  - num: Credit card users show larger payday expenditure jumps (3.7%) than cash users (2.3%), disconfirming liquidity constraint explanations.
  - num: Per-trip expenditures decrease over subsequent trips within a paycheck cycle, with the first post-payday trip being significantly larger even when it occurs on a non-payday.
  - num: Expenditure on the first trip is dramatically larger if it falls on the payday versus one day after, indicating a salience effect beyond mental budget renewal.
  - num: Payday increases probability of purchasing a new variety by 0.63% and mistake probability (never-purchased-again variety) by 1.08%.
  - num: Payday effect shifts up daily consumption rate of the brand by US$0.0212 relative to a mean of US$0.263.
  - num: Mental budget renewing contributes 55% (credit card) and 75% (cash) of payday expenditure elevation; salience contributes the remainder.
  - Projection bias is triggered by salience but not by mental-budget renewing, as mistakes drop sharply from payday to day-after but do not decrease over trips.
key_figures_tables:
  - Figure 1: Unconditional daily expenditure shows a sudden spike at payday (day 0) across all members, credit card, and cash users → Payday increases spending even when including non-shopping days.
  - Figure 2: Conditional-on-visit expenditure spikes at payday → The payday effect is driven by larger purchases when shopping, not by more frequent shopping.
  - Figure 3: Panels A-D show payday increases variety seeking, new-product trying, upgrading to premium products, and daily consumption rate → Real economic impact beyond stockpiling.
  - Figure 5: First-trip expenditure drops sharply from payday to day-after, then remains flat → Salience effect distinct from mental budget renewal.
key_equations:
  - equation: ݕ = ߛ + ߛ ܫ(߬ ≥ 0) + ݂(߬ ) + ߚܺ + ߝ
    explanation: Regression discontinuity design isolating payday effect on daily expenditure.
  - equation: ܷ(݁) = ((1−ߜ௧̅)/(1−ߜ)) ݑ(݁/ݐ̅)
    explanation: Present value of utility from a storable product purchase.
  - equation: max ܷ(݁) + ݃(ℎ − ݁)
    explanation: Consumer maximizes utility from purchase plus pain of depleting mental budget.
definitions:
  - term: Mental Accounting
    definition: Consumers group expenditures into separate budgets (periodic or bracket-specific) rather than treating money as fully fungible.
  - term: Salience
    definition: Payday event draws attention and reduces self-control, causing overspending.
  - term: Projection Bias
    definition: Consumers overestimate how much future tastes will resemble current tastes, leading to purchase mistakes.
  - term: Mental Budget Renewal
    definition: Paycheck receipt resets the monthly spending limit consumers impose on themselves.
critical_citations:
  - "[Amador et al., 2006] — Optimal commitment imposes minimum savings per period."
  - "[Heath & Soll, 1996] — Foundational work on mental budgeting and fungibility."
  - "[Huffman & Barenstein, 2005] — Proposed monthly mental budgeting for credit card users."
  - "[Thaler, 1985] — Transaction utility and mental accounting theory."
relevance:
  topics:
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: high
      justification: Directly examines monthly paycheck cycles and spending patterns relevant to Filipino cultural payday practices.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Provides evidence that users impose their own mental constraints even without system support, informing baseline behavior.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Demonstrates distinct consumer profiles (cash vs. credit card) with different behavioral susceptibilities.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Spending patterns are predictable by trip count within a paycheck cycle, directly informing forecasting.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Reveals that consumers naturally use rule-of-thumb mental budgets, validating domain assumptions for recommendation systems.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: contextual
      justification: Relates to psychological mechanisms of self-control and commitment, indirectly relevant to trust in system recommendations.
  contribution: The paper provides empirical evidence for monthly mental budgeting behavior among consumers without liquidity constraints, which directly informs Odin's budget recommendation module by validating that users naturally think in monthly cycles. It identifies salience and projection bias as critical behavioral factors that cause overspending on paydays, suggesting Odin should incorporate payday-aware alerts and reminders. The cash vs. credit card user differences imply Odin should tailor interventions based on payment method profiles to maximize effectiveness. The finding that per-trip spending decreases over trips within a cycle indicates Odin's spending forecasting should track trip frequency, not just calendar days. Finally, the evidence that consumers allocate expenditures into bracket-specific mental accounts supports Odin's expense categorization and category-level budgeting features.
  directly_justifies:
    - "Consumers without liquidity constraints self-impose monthly mental budgets, supporting Odin's default monthly budgeting paradigm."
    - "Payday salience causes overspending, justifying Odin's payday-specific alerts and nudges."
    - "Per-trip expenditure decreases over trips within a paycheck cycle, informing Odin's spending forecasting models."
    - "Cash users are less susceptible to behavioral biases, suggesting Odin should offer different intervention strategies by payment type."
    - "Projection bias from salience leads to purchase mistakes, supporting Odin's post-purchase reflection and learning features."
  limits:
    - "The sample consists of upper-middle-class consumers in a Southeast Asian country, which may not generalize to all Filipino young professionals."
    - "The study focuses on a single cosmetic retail chain, so findings may not extend to essential goods or broader spending categories."
    - "Cash vs. credit card user differences could be confounded by income or financial sophistication rather than payment method alone."
    - "The data predates widespread mobile payment adoption, which may affect salience effects in contemporary users. [unacknowledged]"
  mapping_rationale: The systematic scan across all 12 functional domains and their associated topic codes identified that this paper directly addresses consumer spending cycles (2.D), behavioral profiling (5.A), spending forecasting (6.A), budget recommendation domain knowledge (7.A), and system landscape (4.A). The high relevance assignments for 2.D, 5.A, 6.A, and 7.A are justified by the paper's rigorous empirical documentation of predictable monthly spending cycles, consumer self-imposed mental budgets, and payday-triggered behavioral patterns that directly inform Odin's algorithmic modules. The paper was considered and rejected for topics 3.A, 3.B, 3.C, and 7.B-D because it does not address categorization frameworks, allocation constraints, or optimization approaches for budget recommendations. It was also rejected for 8.A-C, 9.A-B, 10.A, 11.A-B, 12.A-C, and 13.A-C due to lack of coverage of anomaly detection, mobile UX, privacy, engagement, evaluation, or savings/debt management. The borderline case of user trust (10.B) was assigned contextual relevance because the psychological mechanisms described (self-control, commitment) indirectly relate to trust in system recommendations but are not directly studied. Overall, the paper has high relevance for Odin's core behavioral modeling and budget recommendation domains.
limitations:
  - "The sample consists of upper-middle-class consumers, limiting generalizability to lower-income Filipino young professionals."
  - "The study examines a single retail chain selling storable products, so findings may not extend to essential goods or overall spending."
  - "The data is from a Southeast Asian country and may not fully reflect Filipino cultural spending nuances."
  - "Cash vs. credit card differences may be confounded by unobserved income or financial literacy differences. [unacknowledged]"
  - "The study does not account for the impact of modern fintech like mobile payments on payday behaviors. [unacknowledged]"
remember_this:
  - "Consumers impose monthly mental budgets even without liquidity constraints."
  - "Payday salience, not just renewal, drives spending overshoots."
  - "Per-trip spending decreases predictably over trips within a paycheck cycle."
  - "Credit card users are more susceptible to payday behavioral biases than cash users."
  - "num: Mental budget renewal explains 55-75% of payday spending increases."
```
---

## Paper 23: Heirene R. et al-2026a_summarized.md

**Source File:** `Heirene R. et al-2026a_summarized.md`

```yaml
paper_id: 10.1186/s12954-026-01402-4
designation: local-algorithm-specific
title: Development of lower-risk guidelines for online sports and race betting in Australia using objective behavioural data
authors: Heirene, R. M.; Chandrakumar, D.; Fahey, G.; Huynh, E. L. Y.; Gainsbury, S. M.
year: 2026
venue: Harm Reduction Journal
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 7.D
  - 8.A
  - 8.B
  - 13.A
  - 13.B
  - 13.C
tldr: Empirically derived lower-risk guidelines for online sports betting use objective account data to define thresholds for deposits, income percentage, account numbers, and betting variety associated with reduced harm.
problem_and_motivation: Existing lower-risk gambling guidelines rely on self-reported data and are not specific to online wagering, limiting their accuracy and relevance. Online sports betting poses unique risks, yet no evidence-based thresholds exist for this growing form of gambling. This study addresses the gap by deriving limits from objective behavioural data linked to validated harm measures.
approach:
  - Surveyed 1,647 customers from two Australian online wagering sites, linking responses to six months of objective account data.
  - Used Problem Gambling Severity Index and Gambling Harm Measure to classify harmed versus unharmed participants.
  - Applied Receiver Operating Characteristic curve analyses with bootstrapping to identify optimal thresholds for eight behavioural indicators.
  - Evaluated predictive validity using weighted logistic regression models controlling for demographics and other gambling.
  - Compared newly derived limits against previously established Australian guidelines for sports and race betting.
findings:
  - num: All behavioural indicators except betting frequency achieved acceptable AUC values (≥0.60) for classifying harm.
  - num: Optimal thresholds were higher for GHM harm (e.g., ≤10% income deposited) than for PGSI harm (e.g., ≤2% income deposited).
  - num: Surpassing the deposit frequency limit (4/month) was associated with 2.60 times greater odds of PGSI harm.
  - num: Exceeding the income-deposited limit (2%) was associated with 3.78 times greater odds of PGSI harm.
  - num: Exceeding all eight limits resulted in 8.04 times greater odds of PGSI harm and 8.92 times greater odds of GHM harm.
  - Exceeding multiple limits showed a dose-response relationship with increasing odds of harm.
  - Activity-specific indicators (deposits, income deposited, number of accounts) outperformed standard indicators in predicting harm.
  - Newly derived limits showed higher accuracy than prior self-report-based limits for GHM harm classification.
  - Younger adults (≤25) required lower threshold values on most indicators to distinguish harmed from unharmed gamblers.
  - Betting frequency was not a reliable indicator of harm and was inversely associated with harm in multivariate models.
key_figures_tables:
  - Table 2: Optimal limit values and performance metrics → AUC values for deposit-based indicators were highest, suggesting strong classification ability.
  - Figure 2: Odds ratios for total limits surpassed → Exceeding more limits exponentially increases harm odds for both PGSI and GHM.
  - Figure 3: Risk curves for behavioural indicators → Deposit percentage shows steepest risk increase; betting frequency shows flattest.
  - Figure 5: Proposed "2-2-4-4 Rule" infographic → Visual summary of recommended guidelines for consumer use.
  - Table 5: Rates above limits pre- and post-survey → Harmed participants consistently more likely to surpass all thresholds.
key_equations:
  - equation: "AUC = \\int_0^1 TPR(FPR^{-1}(x)) dx"
    explanation: "Area under ROC curve measures classification ability."
  - equation: "OR = \\frac{p/(1-p)}{q/(1-q)}"
    explanation: "Odds ratio compares harm likelihood between groups."
  - equation: "Youden = sensitivity + specificity - 1"
    explanation: "Maximizes overall classification accuracy."
definitions:
  - term: PGSI
    definition: "Problem Gambling Severity Index; 9-item screening measure for gambling problems."
  - term: GHM
    definition: "Gambling Harm Measure; 16-item scale assessing harm across six life domains."
  - term: AUC
    definition: "Area Under the Receiver Operating Characteristic Curve; measure of test accuracy."
  - term: ROC
    definition: "Receiver Operating Characteristic; graphical plot of true positive rate vs. false positive rate."
  - term: OR
    definition: "Odds Ratio; measure of association between an exposure and an outcome."
  - term: "Youden index"
    definition: "J = sensitivity + specificity - 1; maximizes correct classification rate."
critical_citations:
  - "[Currie et al., 2017] — Derived low-risk limits from longitudinal Canadian data."
  - "[Dowling et al., 2021] — Established Australian low-risk limits by gambling activity."
  - "[Louderback et al., 2021] — Used objective data to derive online gambling thresholds."
  - "[Heirene et al., 2021] — Documented inaccuracies in self-reported gambling behaviour."
  - "[Young et al., 2021] — Developed Canadian lower-risk guidelines framework."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: "Study develops behavioural thresholds to classify harmed vs. unharmed gamblers, directly informing financial risk profiling."
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: "Findings on younger adults requiring lower thresholds inform how initial profiles might be calibrated for new users."
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: "Uses ROC analysis and logistic regression to classify individuals based on behavioural indicators."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: "Identifies behavioural indicators (deposit frequency, income percentage) that could serve as predictive features for forecasting spending risk."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: "Does not develop forecasting algorithms but establishes thresholds that could inform sequential data labelling for forecasting models."
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: "Proposed income-relative thresholds (≤2% deposited) can inform budget allocation strategies that prioritize financial safety."
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: "Provides empirical justification for recommending deposit limits as a budgeting tool in PFMS."
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: low
      justification: "Dose-response analysis of multiple limits suggests how infeasibility might be managed by prioritizing certain constraints."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: "Behavioral thresholds (e.g., >4 deposits/month, >2% income deposited) provide clear cut-points for flagging anomalous spending."
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: "Study identifies indicators but does not propose or evaluate anomaly detection algorithms."
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: contextual
      justification: "Limits on gambling expenditure indirectly relate to protecting savings capacity, but savings not directly measured."
    - code: 13.B
      name: Debt Management in PFMS
      relevance: contextual
      justification: "GHM includes financial strain and borrowing items, but study does not focus on debt management strategies."
    - code: 13.C
      name: End‑of‑Period Surplus as a Savings Input
      relevance: contextual
      justification: "Reduced gambling expenditure (≤2% income deposited) could increase surplus, but not explicitly modeled."
  contribution: "This paper provides empirical evidence that objective behavioural indicators, particularly deposit frequency and income-relative deposits, can effectively classify financial risk. For Odin, these findings directly justify implementing deposit-based thresholds as primary risk indicators in user financial profiles. The dose-response relationship supports a multi-constraint approach to budget recommendations where exceeding multiple limits triggers enhanced user warnings. The paper's methodological framework for deriving limits from linked survey-account data offers a template for calibrating Odin's cold-start anomaly detection. Finally, the emphasis on income-relative thresholds provides Odin with a domain-justified, personalised basis for setting spending guardrails."
  directly_justifies:
    - "Odin should monitor monthly deposit frequency with a recommended upper limit of four deposits per month."
    - "Odin should calculate and flag users who deposit more than 2% of monthly household income into discretionary spending accounts."
    - "Odin's cold-start profile for new users should apply lower behavioural thresholds for users aged 25 and under."
    - "Odin's budget recommendation module should warn users when multiple spending limits are simultaneously exceeded."
    - "Odin should prioritize deposit-based indicators over betting frequency metrics for financial risk classification."
  limits:
    - "Sample overrepresented frequent bettors and older individuals, potentially skewing limits toward heavier users."
    - "Behavioural data from only one operator may not capture full gambling activity across multiple accounts."
    - "Harm classification based on self-report may not fully capture objective financial harm or debt accumulation."
    - "Limits derived from Australian wagering context may not generalize to other spending categories or jurisdictions."
    - "Cross-sectional design limits causal inference; post-survey analysis shows persistence but not causality. [unacknowledged]"
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated canonical topic codes was conducted. The paper's core contribution on behavioural risk profiling directly flagged domains 5 (Behavioral Profiling) and 6 (Spending Forecasting) with high relevance, as the study's thresholds and classification methods provide empirical grounding for Odin's user profiling and forecasting modules. Domain 7 (Budget Recommendation) was flagged medium because the income-relative deposit limit (2%) offers a concrete, evidence-based constraint for budget allocation systems. Domain 8 (Anomaly Detection) was flagged high because the identified thresholds (e.g., >4 deposits/month) serve as direct cut-points for anomaly flagging. Domain 13 (Savings & Debt) was assessed as contextual only, since savings and debt are not directly measured or modeled. Domain 2 (Filipino Cultural Context) and Domain 3 (Expense Categorization) were rejected because the study focuses on Australian gambling behaviour without cultural or category-specific insights transferable to Filipino PFMS. Domain 9 (Mobile-First Design) and 11 (Retention & Engagement) were rejected as the study does not address user interface or engagement mechanisms. Overall, the paper provides moderate-to-high relevance for Odin's risk profiling and anomaly detection modules, with actionable thresholds that can be directly embedded into system logic."
limitations:
  - "Sample skewed toward older, more frequent bettors, limiting generalizability to casual users."
  - "Single-operator data may underestimate total gambling activity, affecting threshold accuracy."
  - "Self-report measures of harm may not capture objective financial consequences like debt or bankruptcy."
  - "Cross-sectional design prevents establishing causal thresholds for harm prevention."
  - "Findings may not generalize to non-gambling spending categories within PFMS. [unacknowledged]"
  - "Income estimates from bracketed survey responses introduce measurement error in income-relative thresholds. [unacknowledged]"
  - "The study does not evaluate the long-term stability of the proposed thresholds over time. [unacknowledged]"
remember_this:
  - "Limit monthly deposits to four to reduce gambling-related financial harm."
  - "Deposit no more than 2% of monthly household income into gambling accounts."
  - "Using three or more betting accounts more than doubles the odds of harm."
  - "Exceeding multiple spending limits compounds harm risk exponentially."
  - "Younger adults under 25 require stricter thresholds to avoid similar risk levels."
```
---

## Paper 24: Ashta_summarized.md

**Source File:** `Ashta_summarized.md`

```yaml
paper_id: 8a7f4e3d-2b1c-4a5d-9e8f-0a1b2c3d4e5f
designation: international
title: Artificial Intelligence in Microfinance and Financial Inclusion: Applications, Issues, and Future Directions
authors: Ashta, A.
year: 2026
venue: Unknown
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 12.A
tldr: AI enables financial inclusion through alternative credit scoring, automated underwriting, and personalized savings, but risks algorithmic bias, proxy discrimination, privacy violations, and digital exclusion.
problem_and_motivation: Two billion adults lack access to formal financial services due to credit invisibility and high operational costs. Traditional systems fail to serve marginalized populations without formal credit histories. AI offers a potential solution by leveraging alternative data and automation to expand access.
approach:
  - A critical review of peer-reviewed articles, working papers, and reports from organizations like the World Bank and CGAP was conducted.
  - The analysis includes multiple purposively selected case studies from the Global South, such as M-Pesa, Tala, Branch, BIMA, and Pula.
  - The BHAI framework is adopted as an interpretative-constructivist lens to guide the assessment of AI's role in microfinance.
  - The study examines AI applications across payments, savings, lending, insurance, and investments.
  - The paper identifies recurring patterns, operational challenges, and ethical dilemmas from the case studies.
  - The paper synthesizes findings to highlight both the potential and risks of AI for financial inclusion.
  - It incorporates quantitative evidence, such as default rate reductions and cost savings from AI implementations.
findings:
  - num: Alternative data models achieve correlations of 0.65 to 0.72 between payment consistency and loan repayment, matching FICO performance.
  - num: Machine learning for alternative credit scoring reduces default rates and can lower operational costs by 6% to 25% of total losses.
  - num: AI-driven underwriting reduces decision-making costs from hundreds of dollars to pennies and processes loans in minutes instead of weeks.
  - Alternative data can encode existing societal inequalities, leading to proxy discrimination against marginalized groups.
  - AI-powered behavioral nudges can increase savings engagement but risk becoming manipulative dark patterns.
  - Supervised learning, particularly gradient boosting, dominates 70-80% of production systems for alternative credit scoring.
  - Deep learning is deployed for unstructured data like biometrics and damage assessment in payments and insurance.
  - Reinforcement learning is less common, used mainly for optimization in payment routing, pricing, and portfolio management.
  - There is an "inclusion paradox" where AI enables access to financial services, but often at exploitative terms for vulnerable populations.
  - AI-driven financial inclusion faces critical challenges, including bias, privacy violations, lack of transparency, and cultural insensitivity.
key_figures_tables:
  - Table 1: Behavioral finance nudges in digital savings → AI can operationalize nudges through predictive analytics and automated savings plans.
  - Table 2: Traditional versus Alternative Data → Alternative data includes mobile money, utility payments, and behavioral analytics for credit scoring.
  - Table 3: AI Technologies by Financial Sector → Supervised learning dominates, with gradient boosting for credit scoring and CNNs for biometrics and damage assessment.
  - Table 4: Humane Considerations by Financial Sector → All sectors face challenges like algorithmic bias, privacy violations, and lack of transparency.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: Artificial Intelligence (AI)
    definition: Computer systems that can perform tasks typically requiring human intelligence such as pattern recognition, decision-making, and language understanding.
  - term: Machine Learning
    definition: A subset of AI where algorithms improve automatically through experience.
  - term: Supervised Learning
    definition: Training algorithms on labeled datasets where the correct answer is known.
  - term: Unsupervised Learning
    definition: Discovering hidden patterns in data without pre-labeled examples.
  - term: Reinforcement Learning
    definition: Algorithms learn optimal strategies through trial and error with rewards for successful actions.
  - term: Natural Language Processing (NLP)
    definition: Technology enabling computers to understand and generate human language.
  - term: Computer Vision
    definition: AI systems that can 'see' and interpret images.
  - term: Alternative Data
    definition: Non-traditional data sources such as mobile phone usage, e-commerce history, utility payments, and social network data.
  - term: Gradient Boosting
    definition: Ensemble methods combining multiple decision trees, like XGBoost and LightGBM, effective for alternative credit scoring.
  - term: Deep Learning
    definition: Uses interconnected layers of algorithms (neural networks) to learn from large amounts of data.
  - term: Parametric Insurance
    definition: Coverage that pays out automatically when specific measurable events occur.
  - term: Robo-Advisor
    definition: Automated platforms providing financial planning and investment management.
  - term: Proxy Discrimination
    definition: Using variables that correlate with protected characteristics as a substitute for those attributes.
  - term: Digital Divide
    definition: The gap between those who have access to digital technologies and those who do not.
  - term: BHAI Framework
    definition: A framework advocating for humane AI development through multidimensional inclusion, ethical oversight, and contextual sensitivity.
  - term: Credit Invisibility
    definition: Individuals with no footprint in conventional credit bureaus, lacking formal credit history.
critical_citations:
  - "[Consumer Financial Protection Bureau, 2015] — Documents 45 million credit-invisible adults in the U.S."
  - "[Björkegren & Grissen, 2019] — Demonstrates mobile phone data predicts credit repayment."
  - "[Berg, Burg, Gombović, & Puri, 2019] — Shows ML reduces default rates in fintech lending."
  - "[S. Barocas & Selbst, 2016] — Analyzes proxy discrimination in algorithmic systems."
  - "[Zuboff, 2019] — Critiques surveillance capitalism and data commodification."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Discusses transaction analysis for fraud detection and personalization.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: low
      justification: Mentions personalized payment options but does not focus on category design.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Reviews major fintech systems and AI applications globally.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Critically assesses limitations like bias, privacy, and exclusion in current systems.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Uses behavioral nudges and segmentation based on transaction patterns.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: low
      justification: Addresses the cold-start problem through alternative data for new users.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses clustering and classification for user segmentation and fraud detection.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Discusses forecasting for credit risk, savings, and market movements.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Mentions time-series forecasting (ARIMA, LSTM) for income and spending prediction.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Discusses automated savings and goal-based trackers as budgeting strategies.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Touches on personalized savings recommendations but not explicit budget allocation.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Describes real-time fraud detection as a core application in payments.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Mentions supervised and unsupervised learning for detecting transaction anomalies.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Extensively covers privacy violations, data breaches, and surveillance concerns.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Discusses building trust through security, transparency, and recourse mechanisms.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Calls for fairness audits, impact assessments, and outcome-based evaluation.
  contribution: The paper provides a broad overview of AI applications in financial inclusion, directly relevant to Odin's core domains of expense analysis, forecasting, and anomaly detection. It offers a critical lens on the limitations of existing systems and highlights the importance of user privacy and trust. The detailed discussion on algorithmic bias and fairness directly informs Odin's design to ensure equitable financial management. The paper's case studies of Global South fintech implementations offer practical insights for Odin's contextual relevance.
  directly_justifies:
    - Odin must be designed with fairness-aware machine learning to avoid perpetuating proxy discrimination.
    - Alternative data and predictive modeling require transparency to allow users to challenge automated decisions.
    - User trust is foundational for retention and engagement, requiring clear communication and ethical data handling.
    - Anomaly detection systems must adapt to evolving spending patterns to effectively flag fraud and irregularities.
  limits:
    - The review is non-systematic, which may introduce selection bias in the case studies chosen.
    - The paper does not provide a deep technical analysis of specific algorithms but rather a high-level overview.
    - The analysis is based on existing literature and may not capture the most recent developments in AI.
    - The paper focuses on the Global South, which may limit the direct applicability of specific case studies to Odin's Filipino context.
  mapping_rationale: The systematic scan of the 12 functional domains identified the paper as highly relevant to Predictive Modeling (6.A/6.B) and Anomaly Detection (8.A/8.B), due to its extensive coverage of alternative credit scoring, forecasting algorithms, and fraud detection systems. It also shows high relevance to Data Privacy & Trust (10.A/10.B) and Existing Systems & Gaps (4.A/4.B), with detailed discussions on ethical challenges and system limitations. Medium relevance was assigned to domains like Expense Categorization (3.A/3.B) and Behavioral Profiling (5.A/5.C), as these are secondary themes informing the core predictive applications. Domains like Mobile-First Design (9.A/9.B) and Savings/Debt Management (13.A/13.B) were considered but rejected as the paper lacks specific focus on these areas. Borderline cases included seasonal spending (2.B), which is implicitly addressed through income volatility modeling, and user-defined constraints (3.C, 7.B), which are not central to the paper's argument. The paper is highly relevant to Odin as it provides both the technological justification and the critical ethical framework necessary for building a responsible PFMS.
limitations:
  - The review is non-systematic, potentially introducing selection bias in case studies.
  - The paper does not provide deep technical analysis of specific algorithms but a high-level overview.
  - The analysis is based on existing literature and may not capture the most recent AI developments.
  - The focus on the Global South may limit direct applicability of specific case studies to Odin's Filipino context. [unacknowledged]
remember_this:
  - Alternative data correlates with creditworthiness at rates comparable to traditional FICO scores.
  - AI-driven underwriting reduces costs from hundreds of dollars to pennies per loan.
  - Algorithmic bias can create proxy discrimination without explicitly using protected attributes.
  - Financial inclusion via AI risks becoming exploitation if deployed without adequate ethical oversight.
  - Success requires prioritizing human dignity and transparent governance over efficiency metrics.
```
---

## Paper 25: Chandana et al_summarized.md

**Source File:** `Chandana et al_summarized.md`

```yaml
paper_id: 549d7af6-15d6-5c3f-b483-6c0f6de1b738
designation: international-algorithm-specific
title: PERSONAL FINANCE TRACKER WITH AI BASED EXPENSE PREDICTION
authors: Chandana, M.; Reddy, E. M.; Reddy, E. P.; Vaishnavi, I. S.; Vaishnavi, K.
year: 2026
venue: AMERICAN JOURNAL OF MANAGEMENT AND IOT MEDICAL COMPUTING
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 9.A
  - 9.B
  - 12.A
  - 12.B
tldr: An AI-powered finance tracker using Flask, MySQL, Random Forest, and LSTM to forecast expenses, detect anomalies, and automatically categorize transactions for enhanced user financial awareness.
problem_and_motivation: Existing expense trackers passively record data without providing predictive insights or personalized budgeting guidance. Users need intelligent systems that analyze behavioral patterns to offer actionable financial foresight. This project addresses the gap between simple tracking and proactive financial management.
approach:
  - The system is built with Python and Flask for the backend, MySQL for data storage, and a frontend using HTML, CSS, and JavaScript with Chart.js.
  - Historical transaction data is preprocessed to remove nulls, encode categorical features, and normalize numerical values for model input.
  - A Random Forest classifier is used to automatically categorize transactions into predefined groups such as food, travel, and bills.
  - An LSTM neural network is applied for time-series forecasting to predict future monthly expenses based on past spending behavior.
  - Anomaly detection algorithms analyze spending trends to identify unusual patterns or sudden spikes in expenditure.
  - A real-time dashboard visualizes income, expense distribution, and predictions through charts and graphs to improve user understanding.
  - User authentication and session management secure access and isolate individual financial data within the MySQL database.
  - The system was tested on both sample and real transaction datasets to evaluate the performance of its core modules.
findings:
  - The LSTM model achieved approximately 85% accuracy in forecasting next-month expenses.
  - The Random Forest classifier achieved over 90% accuracy in automatically categorizing financial transactions.
  - The anomaly detection module successfully identified sudden spending spikes and irregular transactions with good accuracy.
  - Users found the dashboard interface easy to understand and the visual insights improved their financial awareness.
  - Predicted values from the LSTM model closely matched actual spending patterns for most categories.
  - The system proved more effective than manual or static trackers by providing accurate predictions and helpful alerts for unusual expenses.
key_figures_tables:
  - Figure 1: System architecture overview of the AI-powered tracker → Shows the integration of modules with LSTM and Random Forest.
  - Figure 2: Flask-based ML dashboard flow → Illustrates the technical workflow from user input to insights and storage.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network used for time-series forecasting in this system.
  - term: AI
    definition: Artificial Intelligence, used for predictive analysis and automation in the finance tracker.
critical_citations:
  - "[Kaur and Singh, 2022] — AI-based expense prediction using ML."
  - "[Patel and Sinha, 2021] — Random Forest and LSTM for expenditure analysis."
  - "[Bhattacharya, 2023] — Automated finance tracking with data analytics."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Implements Random Forest for automated expense classification.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: Uses predefined categories (food, travel) and visualizes them.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Reviews limitations of traditional static trackers as a baseline.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly addresses the lack of predictive and analytical features in existing systems.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Core contribution is forecasting future expenses using LSTM.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Uses LSTM specifically for time-series expense prediction.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Includes a module to identify unusual spending patterns and generate alerts.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Mentions anomaly detection techniques but provides limited algorithmic detail.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: contextual
      justification: The web-based system could inform mobile-first design but is not the focus.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: Mentions an intuitive dashboard but focuses on web, not mobile UX specifically.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Presents accuracy results and user-friendliness evaluations.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides quantitative accuracy metrics for both classification and prediction modules.
  contribution: The paper provides a practical implementation of a predictive finance tracker, demonstrating how LSTM and Random Forest can be integrated into a web application. It justifies the use of these algorithms for Odin's expense prediction (6.A, 6.B) and categorization modules (3.A). Its evaluation framework (12.A, 12.B) offers a template for testing similar modules, while its anomaly detection component (8.A, 8.B) validates the need for proactive spending alerts.
  directly_justifies:
    - The LSTM model achieves 85% accuracy in forecasting monthly expenses.
    - The Random Forest classifier attains over 90% accuracy in automated transaction categorization.
    - Anomaly detection can effectively identify sudden spending spikes for user alerts.
    - Users respond positively to dashboards that present predictive and categorized financial insights.
  limits:
    - The dataset used for testing is not clearly described, making reproducibility difficult. [unacknowledged]
    - Lack of comparison against a robust set of baseline or state-of-the-art models. [unacknowledged]
    - No explicit discussion of privacy-preserving techniques for handling sensitive financial data. [unacknowledged]
    - The system is a web application, and no discussion is provided on how its design translates to a mobile-first experience. [unacknowledged]
  mapping_rationale: A systematic scan was conducted across all 12 functional domains for this paper. The domain of 'Expense Categorization' was flagged as highly relevant (3.A, 3.B) due to the Random Forest classifier. 'Spending Forecasting' was also high (6.A, 6.B) given the LSTM model. 'Anomaly Detection' (8.A, 8.B) was relevant due to the dedicated module. 'Existing Systems & Gaps' (4.A, 4.B) was identified as contextual/high as the motivation explicitly critiques traditional systems. 'System Evaluation' (12.A, 12.B) was medium/high due to reported accuracy metrics. The 'Mobile-First Design' domain (9.A, 9.B) was considered but rejected to low/contextual as the work is web-focused and does not address mobile-specific challenges. 'Data Privacy' and 'User Retention' were considered and rejected as they are not discussed. The paper's overall relevance to Odin is moderate, as it validates the technical feasibility and impact of predictive and categorical modules, which are core components of the system.
limitations:
  - The paper does not specify the size or source of the dataset used for validation. [unacknowledged]
  - No comparison is made with other forecasting models like XGBoost or Transformer-based networks. [unacknowledged]
  - The anomaly detection method lacks algorithmic detail, making its performance difficult to assess. [unacknowledged]
  - The evaluation focuses on accuracy and usability but does not test the system's performance under varying data distributions. [unacknowledged]
remember_this:
  - LSTM achieved 85% accuracy in forecasting monthly expenses.
  - Random Forest automatically categorized transactions with over 90% accuracy.
  - Anomaly detection provided effective early warnings for unusual spending.
  - The system transformed a passive tracker into an intelligent predictive assistant.
  - The dashboard improved user financial awareness through clear visualizations.
```
---

## Paper 26: Pesa et al_summarized.md

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

## Paper 27: Gong_summarized.md

**Source File:** `Gong_summarized.md`

```yaml
paper_id: 10.1051/itmconf/20268402004
designation: international
title: Research Progress and Trends of Deep Learning in Stock Price Prediction: A Systematic Review from LSTM to Transformer
authors: Gong, H.
year: 2026
venue: ITM Web of Conferences
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
tldr: A systematic review of deep learning models for stock prediction, tracing the evolution from LSTM to Transformer and hybrid architectures, with empirical comparisons and future research directions.
problem_and_motivation: Stock price prediction remains challenging due to high volatility and non-linearity, and traditional methods are insufficient. Deep learning models like LSTM and Transformer have shown promise, but a comprehensive review linking their evolution from LSTM to hybrid architectures is lacking. This review aims to systematically summarize these methods, compare their performance, and identify challenges and future trends.
approach:
  - Systematically reviews the evolution of stock prediction models from RNNs and LSTM to Transformer and hybrid architectures.
  - Classifies and analyzes mainstream deep learning models, detailing their characteristics, advantages, and limitations.
  - Compares empirical studies on different datasets, focusing on evaluation metrics like RMSE, MAE, and Sharpe Ratio.
  - Discusses current challenges in data, model, and deployment, and proposes future research directions.
  - Synthesizes findings from prior research to provide a complete technical roadmap for applying deep learning to stock price prediction.
findings:
  - num: LSTM achieved a 0.46% daily return on S&P 500 constituents, outperforming DNN (0.32%) and logistic regression (0.26%).
  - num: LSTM generated trading signals with a Sharpe ratio up to 2.34, while other models were far less than 1.0.
  - num: Transformer models reduced MAE by 20.73%, MSE by 34.84%, and MAPE by 25.63% compared to LSTM in some studies.
  - num: The LSTM-Transformer hybrid model showed MAE and RMSE reductions of over 50% compared to the parent models.
  - num: The hybrid model achieved an R² value of 0.9618, higher than LSTM (0.8430) and Transformer (0.7763).
  - LSTM is advantageous for short-term prediction and generating trading signals with high Sharpe ratios.
  - Transformer excels in long-range dependency and cross-asset modeling, improving overall prediction accuracy.
  - The evolution of models shows a trend towards hybrid and multimodal fusion for better performance and interpretability.
key_figures_tables:
  - "Table 1: Summary of evaluation criteria (RMSE, MAE, MAPE, DA, R2, Sharpe Ratio) used in empirical studies."
  - "Table 2: Comparison of empirical results for LSTM, Transformer, and hybrid models, showing performance metrics and improvements."
  - "Figure 1: Schematic diagram of the Transformer architecture, highlighting its self-attention mechanism for time series prediction."
  - "Figure 2: Framework of the LSTM-Transformer dual-branch hybrid model for stock price prediction."
  - "Figure 3: Trends in deep learning model evolution for stock prediction, from LSTM to multimodal fusion models."
key_equations:
  - equation: "MAE = \\frac{1}{n} \\sum_{i=1}^{n} |y_i - \\hat{y}_i|"
    explanation: "Average absolute error between predicted and actual values."
  - equation: "RMSE = \\sqrt{\\frac{1}{n} \\sum_{i=1}^{n} (y_i - \\hat{y}_i)^2}"
    explanation: "Square root of average squared errors, sensitive to large deviations."
  - equation: "Sharpe Ratio = \\frac{R_p - R_f}{\\sigma_p}"
    explanation: "Risk-adjusted return, higher values indicate better performance."
definitions:
  - term: "LSTM"
    definition: "Long Short-Term Memory, an RNN variant with gating mechanisms to handle long-term dependencies."
  - term: "Transformer"
    definition: "Model architecture using self-attention mechanisms for processing sequences, avoiding recurrence."
  - term: "MAE"
    definition: "Mean Absolute Error, measures average magnitude of errors."
  - term: "RMSE"
    definition: "Root Mean Square Error, measures error magnitude with a higher penalty for large errors."
  - term: "Sharpe Ratio"
    definition: "Metric for risk-adjusted return, calculated as excess return over risk-free rate per unit of volatility."
critical_citations:
  - "[Fischer & Krauss, 2018] — LSTM outperforms memoryless models in predicting S&P 500 returns."
  - "[Wang et al., 2022] — Transformer model shows significant error reduction compared to LSTM."
  - "[Zhao et al., 2025] — LSTM-Transformer hybrid model achieves superior performance over parent models."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Reviews predictive models applicable to financial forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Systematically evaluates LSTM, Transformer, and hybrid models for time series forecasting.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Discusses challenges like data noise and overfitting relevant to anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: Mentions CNN for feature extraction and noise filtering, relevant to detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Compares models using standard metrics like RMSE, MAE, and Sharpe Ratio.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides empirical comparisons and performance benchmarks for various deep learning modules.
  contribution: "This review provides a comprehensive benchmarking of time series forecasting models, offering a direct evaluation framework for Odin's predictive modules. The empirical comparisons of LSTM and Transformer models, including their hybrid variations, justify the choice of foundational algorithms for spending forecasting. The detailed analysis of model strengths (e.g., LSTM for short-term patterns) and weaknesses (e.g., Transformer's computational cost) informs architectural decisions. The identified challenges, such as overfitting and interpretability, align with Odin's design constraints for a robust and trustworthy system."
  directly_justifies:
    - "LSTM is a reliable benchmark for medium and short-term prediction tasks."
    - "Transformer models provide better prediction accuracy, with lower MAE, MSE, and MAPE."
    - "Hybrid LSTM-Transformer models achieve higher accuracy and stability than parent models."
    - "The choice of evaluation metrics (RMSE, MAE, DA) is critical for assessing prediction models."
    - "Interpretability and computational efficiency are key challenges for deploying deep learning in finance."
  limits:
    - "The review does not propose a new model or application in personal finance."
    - "Findings are based on stock market data and may not directly transfer to spending data."
    - "Lacks specific guidance on handling cold-start problems in personal finance systems."
  mapping_rationale: "A systematic scan across all 12 functional domains and 43 topic codes was conducted. Domains most relevant to this paper are Spending Forecasting (6.A, 6.B) and System Evaluation (12.A, 12.B) due to its focus on predictive modeling and empirical performance comparisons. The paper also provides contextual value for Anomaly Detection (8.A, 8.B) through discussions on data noise. Topics related to Filipino Cultural Context, Expense Categorization, and Behavioral Profiling were considered but rejected as the paper is a general technical review without specific application to personal finance or Filipino users. The relevance is high for forecasting algorithms and evaluation frameworks, medium for predictive modeling, and contextual for anomaly detection. Overall, the paper's strength lies in its comprehensive review of forecasting techniques and evaluation metrics, making it highly relevant for designing and assessing Odin's algorithmic modules."
limitations:
  - "The review focuses on stock price prediction, not personal spending forecasting. [unacknowledged]"
  - "Does not address the cold-start problem or how to profile users with limited data. [unacknowledged]"
  - "Limited discussion on mobile-first design or user trust implications. [unacknowledged]"
  - "The paper is a review and does not introduce a novel algorithm or empirical dataset. [unacknowledged]"
remember_this:
  - "LSTM excels in short-term prediction and generating high Sharpe ratio trading signals."
  - "Transformer models reduce prediction errors by over 20% compared to LSTM."
  - "Hybrid LSTM-Transformer models can reduce MAE and RMSE by more than 50%."
  - "Deep learning models outperform traditional methods in financial time series forecasting."
  - "Interpretability and real-time adaptation remain critical challenges for deployment."
```
---

## Paper 28: Paz et al_summarized.md

**Source File:** `Paz et al_summarized.md`

```yaml
paper_id: 10.3390/math14030429
designation: international
title: Interpretable Binary Classification Under Constraints for Financial Compliance Modeling
authors: "Paz, Á.; Crawford, B.; Monfroy, E.; Rodriguez-Tello, E.; Barrera-García, J.; Cisternas-Caneo, F.; López Cortés, B.; Lazo, Y.; Yáñez, A.; Peña Fritz, Á.; Soto, R."
year: 2026
venue: Mathematics
odin_topics:
  - "5.A"
  - "5.B"
  - "5.C"
  - "10.A"
  - "12.A"
  - "12.B"
tldr: Evaluates interpretable binary classifiers for predicting student loan income declaration compliance using only pre-event administrative data under class imbalance.
problem_and_motivation: Predicting borrower compliance in income-contingent loan systems is challenging due to class imbalance and the need for transparent decisions using only pre-deadline information. Existing approaches often lack a systematic framework that balances predictive performance, error analysis, and explainability under realistic administrative constraints.
approach:
  - "Dataset of 30,736 borrowers from PUCV's FSCU system, with 9 features retained after preprocessing and feature engineering."
  - "Evaluated 7 supervised algorithms: KNN, Naive Bayes, Logistic Regression, Linear SVM, Decision Tree, Random Forest, and LightGBM."
  - "Addressed class imbalance using SMOTE, ADASYN, and Random Undersampling within a cross-validated grid search."
  - "Optimized hyperparameters for each model-sampling combination using exhaustive grid search with MCC as the primary selection criterion."
  - "Employed a unified pipeline to prevent data leakage, separating 70% training and 30% test sets."
  - "Conducted multi-level interpretability analysis using permutation feature importance, decision tree paths, and SHAP values."
findings:
  - "num: Optimized ensemble models (Random Forest, LightGBM) achieved F1-scores above 0.85 and MCC around 0.42."
  - "num: Linear models (Logistic Regression, Linear SVM) achieved stable performance with F1-scores >0.85 and MCC near 0.37."
  - "num: A simple rule-based threshold baseline achieved MCC of only 0.141, demonstrating the superiority of learned models."
  - "Total debt, enrollment count, marital status, and loan enforceability year were consistently the most important predictors across all models."
  - "Tree-based models offered a favorable balance between expressive power and human verifiability through explicit decision paths."
  - "SHAP analysis confirmed that higher debt and continuous enrollment increase compliance probability, while recent enforceability years and single status increase risk."
  - "Hyperparameter tuning and Random Undersampling consistently improved minority-class recall without substantial accuracy loss."
  - "Ensemble models exhibited a more balanced error structure, avoiding extreme concentration on either Type I or Type II errors."
key_figures_tables:
  - "Table 4: Final feature set used for model training after preprocessing. → Lists 9 core predictive variables."
  - "Figure 12: Average Permutation Feature Importance across all models. → deud_monto and conteo_matr are the dominant predictors."
  - "Figure 15-17: Decision tree snapshots at depths 4, 5, and 11. → Shallow trees provide compact, auditable decision rules."
  - "Figure 18: SHAP summary plot for LightGBM. → Confirms dominance of debt, enrollments, and marital status with clear directional effects."
  - "Figures 10-11: Confusion matrices for best-performing models. → Ensemble models balance Type I/II errors better than linear models."
key_equations:
  - equation: "MCC = (TP*TN - FP*FN) / sqrt((TP+FP)(TP+FN)(TN+FP)(TN+FN))"
    explanation: "Primary metric for imbalanced classification evaluation."
  - equation: "z = (x - μ) / σ"
    explanation: "Standardization formula for numerical features."
  - equation: "θˆ = argmax_{θ∈Θ} (1/K) Σ_{k=1}^K MCC_k(θ)"
    explanation: "Selection of optimal hyperparameters by maximizing mean validation MCC."
definitions:
  - term: "FSCU"
    definition: "Fondo Solidario de Crédito Universitario, Chile's income-contingent student loan system."
  - term: "MCC"
    definition: "Matthews Correlation Coefficient, a balanced metric for binary classification under imbalance."
  - term: "PFI"
    definition: "Permutation Feature Importance, a model-agnostic global interpretability method."
  - term: "SHAP"
    definition: "SHapley Additive exPlanations, a method for local, additive feature attribution."
  - term: "SMOTE"
    definition: "Synthetic Minority Over-sampling Technique for addressing class imbalance."
  - term: "ADASYN"
    definition: "Adaptive Synthetic Sampling, an adaptive oversampling method."
  - term: "Type I error"
    definition: "False positive: predicting a borrower will declare when they do not."
  - term: "Type II error"
    definition: "False negative: predicting a borrower will not declare when they do."
critical_citations:
  - "[He & Garcia, 2009] — Foundational work on learning from imbalanced data."
  - "[Chicco & Jurman, 2020] — Establishes MCC's advantages over F1 and accuracy."
  - "[Breiman, 2001] — Introduces Random Forests, a key ensemble method used."
  - "[Doshi-Velez & Kim, 2017] — Framework for the science of interpretable machine learning."
  - "[Lessmann et al., 2015] — Benchmarking classification algorithms for credit scoring."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Directly constructs borrower profiles from administrative data to predict compliance behavior."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "high"
      justification: "Explicitly addresses the cold-start problem by using only pre-event information for prediction."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Compares and evaluates multiple classification algorithms for profiling compliance risk."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses use of institutional administrative data and the constraints of pre-declaration information."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Proposes MCC as a primary metric and provides a comprehensive evaluation protocol."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Evaluates algorithmic performance of classifiers and resampling strategies."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Reviews related work on student loan repayment prediction systems."
  contribution: "This paper provides a methodological blueprint for predictive decision support in administrative compliance settings, directly applicable to Odin's behavioral profiling modules (5.A, 5.B, 5.C) by demonstrating how to construct and evaluate interpretable classifiers from pre-event data. Its emphasis on MCC as a robust evaluation metric under imbalance informs Odin's evaluation framework (12.A, 12.B). The study's analysis of feature importance and model interpretability using SHAP and decision paths offers a template for transparent model auditing in Odin's system."
  directly_justifies:
    - "Reliable prediction of compliance is achievable using only pre-event administrative data."
    - "MCC is a more appropriate primary metric than accuracy or F1 for imbalanced classification tasks."
    - "Feature importance and SHAP analyses can identify the most influential predictors of financial behavior."
    - "Tree-based models provide a favorable balance between predictive performance and interpretability."
    - "Hyperparameter optimization and resampling are critical for achieving robust performance under imbalance."
  limits:
    - "Study is limited to first-declaration outcomes within a single Chilean university's FSCU system."
    - "Generalizability to other institutions or loan systems is not formally established."
    - "Longitudinal analysis and prediction of recurring non-compliance are not addressed."
    - "The lack of institutionally defined cost-sensitive policies precludes the establishment of optimal decision thresholds."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated canonical topic codes was performed. The paper's core contribution lies in predicting a binary financial compliance outcome, which directly maps to 'Behavioral Profiling & Classification' (domains 5.A, 5.B, 5.C) with 'high' relevance. The methodological emphasis on rigorous evaluation under imbalance maps to 'System Evaluation' (domains 12.A, 12.B) with 'medium' relevance. The discussion of using constrained administrative data touches upon 'Data Privacy & User Trust' (domain 10.A) with 'medium' relevance. The contextual review of related work maps to 'Existing Systems & Gaps' (domain 4.A) with 'contextual' relevance. Domains related to spending patterns (2.A, 2.B), expense categorization (3.A), budget recommendation (7.A), anomaly detection (8.A), mobile design (9.A), user retention (11.A), and savings/debt management (13.A) were considered but deemed not directly relevant, as the paper does not address these topics. The classification task provides a strong foundation for behavioral profiling in Odin."
limitations:
  - "The dataset is limited to a single institution and may not generalize to other populations. [unacknowledged]"
  - "The analysis is cross-sectional and does not model temporal drift or longitudinal compliance patterns."
  - "Socioeconomic variables like employment type or household composition are excluded from the data."
  - "Interpretability of ensemble models is mediated by post-hoc tools, not intrinsic to the model structure. [unacknowledged]"
  - "Model predictions are not linked to specific institutional policies or decision thresholds for action."
remember_this:
  - "MCC values around 0.42 were achieved using only pre-declaration administrative features."
  - "Debt amount, enrollment count, and marital status are the most influential predictors."
  - "Interpretable models can achieve reliable performance under class imbalance and data constraints."
  - "Simple threshold rules performed poorly compared to optimized machine learning models."
  - "A structured pipeline with cross-validation and hyperparameter tuning is essential for reproducibility."
```
---

## Paper 29: Luong & Xie_summarized.md

**Source File:** `Luong & Xie_summarized.md`

```yaml
paper_id: 10.1016/j.jfds.2026.100195
designation: international-algorithm-specific
title: Explainable ensemble machine learning for financial transaction fraud detection: Insights from XGBoost and deep neural networks
authors: Luong, N.D.A.; Xie, S.
year: 2026
venue: The Journal of Finance and Data Science
odin_topics:
  - 8.A
  - 8.B
  - 8.C
  - 5.C
  - 12.A
  - 12.B
tldr: A hybrid XGBoost and deep neural network ensemble with SHAP-based interpretability detects financial fraud with high accuracy and recall on imbalanced transaction data.
problem_and_motivation: Fraud detection systems must balance accuracy, interpretability, and regulatory compliance, yet existing approaches often sacrifice one for the other. Extreme class imbalance and high-dimensional data complicate the identification of rare fraudulent transactions. A unified framework that integrates advanced machine learning, imbalance handling, and explainability is needed for practical deployment.
approach:
  - Data source: IEEE-CIS dataset with ~590k records merged from transaction and identity files, containing 434 features.
  - Preprocessing: Median imputation for numerical features, label encoding for categoricals, and z-score normalization for neural networks.
  - Imbalance handling: Cost-sensitive learning via class weighting for XGBoost and focal loss for DNN, plus threshold optimization for F1.
  - Models: Logistic regression, random forest, XGBoost, enhanced XGBoost, shallow ANN, deep DNN, and a weighted hybrid XGB+DNN ensemble.
  - Evaluation: Stratified 80/20 split; metrics include ROC-AUC, PR-AUC, precision, recall, F1, and inference time.
  - Interpretability: SHAP global feature importance and local beeswarm plots to explain predictions.
  - Benchmarking: Compared against OLightGBM, LSTM, and Kaggle top solutions.
findings:
  - num: The hybrid XGB+DNN ensemble achieved the highest F1-score of 0.74, PR-AUC of 0.7897, and ROC-AUC of 0.9638.
  - num: Enhanced XGBoost attained a recall of 0.83 and precision of 0.42, outperforming standard XGBoost.
  - num: The proposed cost-sensitive approach outperformed SMOTE-based ensemble, with ROC-AUC of 0.9638 vs. 0.9037.
  - num: LSTM performed near-randomly with ROC-AUC 0.502, indicating weak sequential structure in the dataset.
  - Transaction amount and identity-related features (card6, C14, C13) are the most influential predictors.
  - Fraud patterns concentrate in low-value test transactions, high-value opportunistic purchases, and late-night hours.
  - Free email domains, mobile devices, and specific device identifiers are disproportionately associated with fraud.
  - SHAP analysis reveals that feature effects are context-dependent, with anonymized V-series features capturing interaction patterns.
key_figures_tables:
  - Table 3: SMOTE vs. cost-sensitive learning → cost-sensitive approach yields superior PR-AUC and F1.
  - Table 4: Model performance comparison → XGB+DNN ensemble achieves best F1 and PR-AUC.
  - Figure 2: Fraud by amount and product → fraud concentrated at extremes and in product categories C and S.
  - Figure 3: Temporal/spatial patterns → fraud peaks late-night and weekends, varies by region and country.
  - Figure 6: SHAP global importance → TransactionAmt and identity features dominate importance.
key_equations:
  - equation: L_focal = -∑[α(1-ŷ_i)^γ y_i log ŷ_i + (1-α)ŷ_i^γ (1-y_i) log(1-ŷ_i)]
    explanation: Focal loss down-weights easy examples to focus on hard fraud cases.
  - equation: ŷ_i = λ⋅ŷ_i^XGB + (1-λ)⋅ŷ_i^DNN
    explanation: Weighted averaging combines XGBoost and DNN probabilities.
definitions:
  - term: XGBoost
    definition: Extreme Gradient Boosting, a scalable tree-based ensemble method.
  - term: DNN
    definition: Deep Neural Network with multiple hidden layers and non-linear activations.
  - term: SHAP
    definition: SHapley Additive exPlanations, a game-theoretic method for model interpretability.
  - term: Focal Loss
    definition: A loss function that down-weights well-classified examples to focus on hard ones.
  - term: PR-AUC
    definition: Area Under the Precision-Recall Curve, suited for imbalanced classification.
  - term: ROC-AUC
    definition: Area Under the Receiver Operating Characteristic curve, measures discriminative ability.
critical_citations:
  - "[Deotte et al., 2019] — Kaggle 1st place ensemble achieved ROC-AUC ~0.94-0.95."
  - "[Bahnsen et al., 2016] — Feature engineering reduced financial losses by 13%."
  - "[Alamri and Ykhlef, 2024] — BCB-SMOTE achieved F1-score 85.2% with reduced overlap."
  - "[Lin and Gao, 2022] — SHAP reveals complex financial feature interactions."
  - "[Taha and Malebary, 2020] — OLightGBM achieved ROC-AUC 0.9288."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Fraud detection is a core anomaly detection problem addressed directly.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Evaluates XGBoost, DNN, and hybrid ensembles for fraud detection.
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: medium
      justification: Class weighting and focal loss are strategies applicable to cold-start scenarios.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses behavioral and identity features to classify fraudulent vs. legitimate transactions.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides a comprehensive multi-metric evaluation for imbalanced classification.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Compares multiple algorithms and imbalance handling techniques systematically.
  contribution: The paper's hybrid ensemble model offers a blueprint for Odin's anomaly detection module, balancing predictive performance and interpretability. Its cost-sensitive learning strategies (focal loss, class weighting) are directly transferable to Odin's spending anomaly detection. The SHAP-based explainability framework aligns with Odin's need for transparent, user-trustworthy AI. The evaluation methodology provides a template for assessing Odin's algorithmic modules under imbalanced conditions. Moreover, the emphasis on identity and temporal features mirrors Odin's data structure, making the approach applicable to Filipino user spending patterns.
  directly_justifies:
    - An ensemble of XGBoost and DNN improves fraud detection F1-score to 0.74.
    - Focal loss and class weighting are effective for handling extreme class imbalance.
    - SHAP analysis identifies transaction amount and identity features as key predictors.
    - Feature engineering for time-of-day and day-of-week captures periodic fraud patterns.
    - Inference time of 0.35 ms/transaction supports real-time deployment feasibility.
  limits:
    - Dataset anonymization limits interpretability of merchant and demographic patterns.
    - Offline evaluation does not simulate real-world latency or streaming constraints.
    - Concept drift in evolving fraud tactics was not addressed.
    - Deep neural network interpretability remains less mature than tree-based SHAP. [unacknowledged]
    - The study uses a fixed historical snapshot, not accounting for data distribution shifts. [unacknowledged]
  mapping_rationale: Systematic scanning across all 12 functional domains and associated topic codes flagged the following as relevant: Anomaly Detection (8.A, 8.B, 8.C) at high relevance because the paper directly addresses fraud detection as an anomaly detection problem; Behavioral Profiling & Classification (5.C) at medium relevance as it uses classification to distinguish fraud from legitimate behavior; System Evaluation (12.A, 12.B) at medium relevance for its comprehensive evaluation framework. Borderline case: the paper's temporal analysis (e.g., hour of day) touches 6.A/6.B but does not forecast spending, so it was rejected for those codes. Domains such as Filipino Cultural Context, Expense Categorization, Budget Recommendation, Savings & Debt Management were considered but rejected due to no direct content. Overall, the paper provides strong empirical and methodological support for Odin's anomaly detection and evaluation modules.
limitations:
  - Dataset is anonymized, lacking merchant categories and customer demographics.
  - Real-world deployment constraints like latency and streaming were not simulated.
  - Concept drift and evolving fraud tactics were not addressed.
  - Interpretability of deep neural networks remains limited compared to tree models. [unacknowledged]
  - The static offline validation may not generalize to live production environments. [unacknowledged]
remember_this:
  - Hybrid XGB+DNN ensemble achieved F1-score 0.74 on imbalanced fraud data.
  - Transaction amount and identity features are the strongest fraud predictors.
  - SHAP enables transparent, case-level explanations for regulatory compliance.
  - Cost-sensitive learning with focal loss outperforms SMOTE-based oversampling.
  - Ensemble model has 0.35 ms inference time, viable for real-time detection.
```
---

## Paper 30: Cabral et al_summarized.md

**Source File:** `Cabral et al_summarized.md`

```yaml
paper_id: 326ca948-31b5-5a2b-adf8-513e8912fcc7
designation: international
title: "Non-Stationarity in Financial Time Series: A Unifying Survey on Drift Detection, Adaptive Learning, and Evaluation"
authors: "Cabral, D. M.; Lima, A. M. A.; Oliveira, G. H. F. M.; Oliveira, A. L. I."
year: 2026
venue: "Unknown"
odin_topics:
  - "2.B"
  - "2.D"
  - "4.A"
  - "4.B"
  - "5.A"
  - "5.C"
  - "6.A"
  - "6.B"
  - "7.A"
  - "7.B"
  - "7.D"
  - "8.A"
  - "8.B"
  - "8.C"
  - "9.A"
  - "10.A"
  - "11.A"
  - "12.A"
  - "12.B"
  - "12.C"
tldr: "A unified survey on non-stationarity in financial time series provides a taxonomy, a processing pipeline, and an evaluation playbook to address fragmentation across econometrics, statistics, and machine learning."
problem_and_motivation: "Predictive models in finance fail in deployment due to structural changes in data-generating processes, degrading calibration and increasing tail risk. Results across disciplines are hard to reconcile because of divergent terminology and incompatible evaluation protocols. A unified framework is needed to support research and deployment under non-stationarity."
approach:
  - "A unified taxonomy of drift and regime change is proposed along temporal, statistical, spatial, and ontological axes."
  - "An end-to-end pipeline connects representation, detection, adaptation, and evaluation choices for financial time series."
  - "A review of drift-aware representations covers internal signals, exogenous context, latent structure, and robustness-oriented features."
  - "Change detection methods are surveyed including segmentation, sequential monitoring, Bayesian, embedding-based, and multivariate dependence approaches."
  - "Adaptation strategies are examined including parametric, ensemble, hybrid continuous, and modern continual learning and test-time adaptation methods."
  - "Evaluation guidance is consolidated covering detection delay, false-alarm control, computational cost, and finance-specific utility."
  - "Emerging directions are highlighted including foundation models, multimodal context, and parameter-efficient adaptation."
findings:
  - "num: 174 references are cited in the survey."
  - "num: The literature on non-stationarity is fragmented across 5 distinct research traditions with limited cross-fertilization."
  - "The four-axis taxonomy (temporal, statistical, spatial, ontological) provides a framework to describe real drift scenarios consistently."
  - "Learned embeddings from methods like TS2Vec and drift-oriented contrastive learning are more effective for capturing complex drift patterns than hand-crafted features."
  - "Incorporating exogenous context through multimodal embeddings can anticipate market shifts before they are fully reflected in prices."
  - "Graph neural networks effectively capture spatial drifts such as correlation collapse during crisis periods."
  - "Bayesian online changepoint detection (BOCPD) provides real-time change probabilities with explicit uncertainty quantification."
  - "Dynamic ensembles and hybrid continuous-adaptation flows balance stability and responsiveness under different drift types."
  - "Sequential protocols like prequential evaluation are essential to respect temporal order and avoid information leakage."
  - "Benchmarking in finance lacks standardization, with studies relying on ad hoc asset selections and heterogeneous protocols."
key_figures_tables:
  - "Figure 1: Extended taxonomy of non-stationarity along five axes. → Provides a unified framework for describing drift phenomena in finance."
  - "Figure 2: Temporal morphology of drifts. → Illustrates abrupt, gradual, incremental, and recurrent drift patterns."
  - "Figure 10: Representation layers for drift-aware financial modeling. → Shows how raw data is transformed through internal, exogenous, latent, and robustness layers."
  - "Table 1: Terminological equivalences across traditions. → Maps 'concept drift' terminology across machine learning, econometrics, statistics, and finance."
  - "Table 6: Change axes and indicative methods. → Links drift types to appropriate detection strategies."
  - "Table 7: Computational complexity of change-detection methods. → Provides practical guidance on method scalability."
  - "Table 8: Comparison of adaptation methods. → Compares speed, memory, complexity, and use cases for adaptation strategies."
  - "Table 9: Cost-benefit trade-offs for adaptation strategies. → Quantifies performance gains and resource requirements for different adaptation approaches."
key_equations:
  - equation: "P(X,Y) = P(Y|X)P(X)"
    explanation: "Decomposition of joint distribution for defining shift types."
  - equation: "C(a,b) ≈ -log p(X_{a:b} | θ̂_{a:b})"
    explanation: "Intra-segment cost for segmentation based on negative log-likelihood."
  - equation: "z_t = f_θ(w_t)"
    explanation: "Parametric mapping from time window to latent embedding."
  - equation: "p(r_t | x_{1:t})"
    explanation: "Posterior distribution of run-length in Bayesian online changepoint detection."
  - equation: "S_t^+ = max(0, S_{t-1}^+ + z_t - k)"
    explanation: "CUSUM update rule for detecting mean shifts."
definitions:
  - term: "Non-stationarity"
    definition: "Variation over time in the statistical or structural properties of a data-generating process."
  - term: "Concept drift"
    definition: "Change in the conditional distribution P(Y|X), i.e., the relationship between inputs and targets. Also used broadly for any change in P(X,Y)."
  - term: "Regime"
    definition: "A persistent mode of operation of the data-generating system with relatively stable statistical properties."
  - term: "Structural break"
    definition: "A sudden, persistent change in the parameters of a data-generating process, often used in econometrics."
  - term: "Covariate shift"
    definition: "Change in the marginal distribution of inputs P(X) while the predictive relationship P(Y|X) remains stable."
  - term: "Run-length"
    definition: "The time elapsed since the most recent changepoint in a time series."
  - term: "Prequential"
    definition: "A sequential evaluation protocol where models are trained on past data and tested on new data as it arrives."
critical_citations:
  - "[Žliobaite, 2013] — Critique of concept drift benchmark limitations."
  - "[Hamilton, 1989] — Seminal work on regime-switching models in econometrics."
  - "[Bai & Perron, 2003] — Foundational work on multiple structural break segmentation."
  - "[Killick et al., 2012] — PELT algorithm for efficient changepoint detection."
  - "[Adams & MacKay, 2007] — Bayesian online changepoint detection framework."
  - "[Kolmogorov-Smirnov, 1933] — Basis for non-parametric distribution comparison tests."
  - "[Arlot et al., 2019] — Survey on change point detection methods."
relevance:
  topics:
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "medium"
      justification: "Taxonomy includes recurrent/seasonal drift tied to deterministic patterns like calendar cycles."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "medium"
      justification: "Taxonomy frames recurrent drift and seasonal spending as regime phenomena."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "low"
      justification: "Contextual framing of system needs under non-stationarity; mentions real-time system challenges."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Explicitly discusses limitations of stationarity-based assumptions in financial systems."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "contextual"
      justification: "General behavioral profiling mentioned via regime-switching models of user states."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "low"
      justification: "Classification context appears in supervised concept drift detection, not primary focus."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Reviews forecasting models under non-stationarity including time-varying parameters and adaptive models."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Evaluates forecasting algorithms under sequential data drift."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "medium"
      justification: "Discusses adaptive strategies that can inform budgeting under regime changes."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "high"
      justification: "Directly addresses budget recommendation via adaptive model updates under shifting user spending patterns."
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "low"
      justification: "Not explicitly addressed but related through constraint management in adaptation."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Discusses anomaly detection as a proxy for regime detection."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Reviews OOD and anomaly detection methods that apply to spending data."
    - code: "8.C"
      name: "Cold-Start Baseline Strategies for Anomaly Detection"
      relevance: "low"
      justification: "Mentions baseline comparisons but cold-start not explicitly covered."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "contextual"
      justification: "Mentions real-time constraints and computational budgets relevant to mobile-first systems."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "contextual"
      justification: "Identifies privacy as a challenge for federated learning in drift settings."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "medium"
      justification: "Adaptation mechanisms for engagement under evolving user behavior are discussed."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Dedicated section on evaluation protocols and metrics for adaptive systems."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Specific metrics for detection delay, false alarms, and computational cost."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "high"
      justification: "Provides framework for evaluating adaptive recommendation under shifting data distributions."
  contribution: "The survey provides a unified taxonomy and pipeline that directly informs Odin's design for forecasting user spending behavior. The detection and adaptation methods reviewed support Odin's anomaly detection and budget recommendation modules by offering robust approaches to handle shifting user financial patterns. The evaluation protocols specified enable systematic assessment of Odin's predictive models and behavioral profiling against non-stationary spending data. The framework also directly justifies Odin's data privacy considerations through its analysis of financial system constraints. Finally, the survey's emphasis on mobile-first computational budgets aligns with Odin's design for Filipino young professionals."
  directly_justifies:
    - "Forecasting algorithms must account for concept drift to maintain accuracy under changing user spending patterns."
    - "Anomaly detection systems require baseline strategies that adapt to evolving data distributions."
    - "Budget recommendations should utilize adaptive models that respond to shifts in user financial behavior."
    - "Evaluation of PFMS should include detection delay, false-alarm control, and computational cost metrics."
    - "Adaptation mechanisms must balance responsiveness with stability to avoid erratic budget recommendations."
    - "Sequential evaluation protocols are necessary to respect temporal order and avoid information leakage in model assessment."
    - "Learned embeddings can effectively capture complex spending patterns and facilitate drift detection."
    - "Multimodal representations (spending data + contextual information) provide early signals of behavioral changes."
    - "Regime-switching models offer a probabilistic framework for classifying user financial behavior over time."
    - "Ensemble methods can handle heterogeneous user behaviors and recurring spending patterns."
  limits:
    - "Benchmarking in finance lacks standardization, making cross-study comparisons difficult."
    - "The survey is primarily conceptual and does not provide empirical validation of proposed methods on PFMS data."
    - "Assumptions of independence within regimes may not hold for correlated spending events."
    - "Operational costs of adaptation are acknowledged but not systematically quantified for PFMS contexts."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was conducted for this survey paper on non-stationarity in financial time series. The domains of Spending Forecasting (6), Budget Recommendation (7), Anomaly Detection (8), and System Evaluation (12) were flagged as highly relevant because the paper directly addresses predictive modeling under drift, adaptive budget allocation, anomaly detection algorithms, and evaluation protocols for such systems. The Behavioral Profiling domain (5) was assessed as medium relevance, as the paper reviews classification approaches under concept drift and regime-switching models that can be applied to user profiling. Cultural Context domains (2.A, 2.B, 2.D) were flagged as medium/contextual relevance because the paper discusses seasonal and recurrent spending patterns through its temporal axis taxonomy, though not specifically applied to Filipino contexts. Existing Systems (4) was assessed as medium due to explicit discussion of limitations in current financial systems under non-stationarity. Mobile-First Design (9) and Data Privacy (10) were considered contextual, as the paper mentions real-time constraints and privacy challenges but does not focus on these domains. Domains related to Expense Categorization (3), Savings & Debt Management (13), and Retention & Engagement (11.B) were rejected as not directly addressed by the paper's core content. The paper provides a foundational framework for Odin's algorithmic modules, offering practical guidance for implementing adaptive models, detection systems, and evaluation protocols under real-world data shifts, with particular emphasis on the taxonomy of drift types and their corresponding detection strategies."
limitations:
  - "The survey relies on a broad literature review rather than empirical experiments, limiting direct validation of proposed pipelines. [unacknowledged]"
  - "Computational costs of advanced methods (e.g., GNNs, foundation models) are discussed qualitatively but not benchmarked for PFMS scale. [unacknowledged]"
  - "The four-axis taxonomy, while comprehensive, may be difficult to operationalize for specific PFMS contexts without domain-specific adaptations. [unacknowledged]"
  - "Evaluation protocols emphasize temporal order but do not fully address the cold-start problem in PFMS with limited user history. [unacknowledged]"
  - "The survey does not consider Filipino-specific cultural factors or expense categorization frameworks. [unacknowledged]"
remember_this:
  - "Non-stationarity in financial data requires unified frameworks across taxonomy, detection, and adaptation."
  - "Four axes (temporal, statistical, spatial, ontological) classify drift types for method selection."
  - "Evaluation must include detection delay, false-alarm control, and computational cost metrics."
  - "Foundation models and parameter-efficient adaptation offer scalable responses to regime changes."
  - "Sequential protocols and realistic computational budgets are essential for reproducible benchmarking."
```
---

## Paper 31: Heirene R. et al-2026b_summarized.md

**Source File:** `Heirene R. et al-2026b_summarized.md`

```yaml
paper_id: 10.1556/2006.2025.00525
designation: international-algorithm-specific
title: Predicting problem gambling among online sports and race bettors: Assessing the value of machine learning using behavioural and self-reported data
authors: Heirene, R. M.; Vanichkina, D.; Zhang, E.; Huynh, C. T. De; Leau, E. L. Y.; Gainsbury, S. M.
year: 2026
venue: Journal of Behavioral Addictions
odin_topics:
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 9.A
  - 10.A
  - 12.B
tldr: Machine learning models using 30 days of behavioural data adequately classify online sports bettors at risk of problem gambling, with performance significantly enhanced by adding two self-reported survey variables.
problem_and_motivation: Online gambling operators collect behavioural data to identify at-risk customers, but clarity on optimal variables and data windows is lacking. Regulatory frameworks increasingly require timely intervention, yet research comparing short-term versus longer-term data windows for risk detection is limited.
approach:
  - Analysed account data and survey responses from 1,470 Australian sports and race betting customers (N=1,349 for six-month window).
  - Built machine learning models (XGBoost, Random Forest, Logistic Regression, Decision Tree, Neural Network) to classify PGSI risk groups.
  - Compared models trained on 30-day versus six-month behavioural data windows.
  - Evaluated performance improvement from adding 11-13 self-reported survey variables (e.g., gambling satisfaction, number of accounts).
  - Used 70/30 train-test split with 10-fold cross-validation and SMOTE for class imbalance.
findings:
  - num: Models using only 30 days of behavioural data achieved adequate classification (AUROC 0.752).
  - num: Extending data to six months did not meaningfully improve performance (AUROC 0.743).
  - num: Adding self-report variables substantially improved performance (AUROC 0.850 for 30-day model).
  - num: Two self-reported variables—gambling satisfaction and number of gambling accounts—were primarily responsible for the improvements.
  - Most predictive account-based variables: age, deposits per active day, average stake, and days since last bet.
  - XGBoost achieved the best classification accuracy among tested algorithms.
  - The binary PGSI ≥8 threshold outperformed the ≥5 threshold for model discrimination.
  - Models using 30-day data with both survey variables achieved 66.2% sensitivity and 84.4% specificity.
key_figures_tables:
  - Figure 2: Confusion matrix and ROC curve for optimal 30-day account model → AUROC 0.752 with 66.2% sensitivity.
  - Figure 4: Performance of 30-day model combining account and survey data → AUROC 0.850, highest overall performance.
  - Figure 6: Comparison of models including/excluding survey predictors → Gambling satisfaction and number of accounts drive performance gains.
  - Table 3: Comparison of classification approaches across PGSI thresholds → Binary ≥8 classification using XGBoost performed best.
  - Table 4: Model performance comparison across phases → Phase 3 models with survey data achieved highest AUROC and balanced accuracy.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: PGSI
    definition: Problem Gambling Severity Index, a 9-item scale assessing gambling problems.
  - term: AUROC
    definition: Area Under the Receiver Operating Characteristic curve, a measure of classification performance.
  - term: AUPRC
    definition: Area Under the Precision-Recall Curve, focused on positive class performance.
  - term: SMOTE
    definition: Synthetic Minority Oversampling Technique, used to address class imbalance.
  - term: XGBoost
    definition: Extreme Gradient Boosting, a machine learning algorithm using gradient boosting.
critical_citations:
  - "[Auer & Griffiths, 2022] — Found Random Forest performs best for self-reported problem gambling prediction."
  - "[Murch et al., 2023] — Used similar PGSI-based classification with account data from Quebec."
  - "[Andersson et al., 2025] — Found similar performance across 30-, 60-, and 90-day data windows."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly classifies customers into risk profiles (PGSI groups) based on behavioural data.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Compares multiple machine learning classifiers (XGBoost, Random Forest, etc.) for risk classification.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Demonstrates predictive modeling of risk status using behavioural account data.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: Applies time-series features from sequential betting data for risk prediction.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Risk detection in gambling spending patterns is analogous to anomaly detection in PFMS.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Uses machine learning algorithms for identifying anomalous (risky) spending behaviour.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: contextual
      justification: Mentions online gambling platforms and customer interactions, provides context for mobile usage.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Discusses use of personal data (behavioural and survey) for risk detection, touches on privacy implications.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides thorough evaluation of model performance using AUROC, AUPRC, sensitivity, specificity, etc.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides background on existing risk detection systems in online gambling, analogous to PFMS.
  contribution: This paper provides a robust methodology for predicting at-risk user behaviour using short-term (30-day) data, which can be applied to Odin's anomaly detection and behavioral profiling modules. It demonstrates that adding minimal self-reported data (e.g., user satisfaction, number of financial accounts) significantly enhances classification accuracy, informing Odin's user-declared preferences module. The finding that longer historical data does not improve performance justifies Odin's potential use of recent spending data for timely intervention. The comparative evaluation of XGBoost against other classifiers guides Odin's algorithm selection for behavioural classification tasks.
  directly_justifies:
    - Machine learning models can classify financial risk profiles using only 30 days of transactional data.
    - Self-reported user variables like satisfaction and number of accounts improve predictive model performance.
    - XGBoost is a competitive algorithm for classification in personal finance behavioral profiling contexts.
    - Short-term data windows are sufficient for risk detection, enabling early intervention strategies.
    - Evaluation using AUROC and AUPRC provides a comprehensive framework for model assessment in imbalanced classification.
  limits:
    - Single-site behavioural data may not capture full user spending across multiple platforms.
    - Self-report variables may suffer from common method bias as they are collected simultaneously with the outcome.
    - Survey sample was not fully representative of the wider customer base, with more engaged bettors self-selecting.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The domain of Behavioral Profiling & Classification (5.A, 5.C) and Anomaly Detection (8.A, 8.B) were flagged as high relevance because the paper directly classifies customers into risk profiles using predictive models. Spending Forecasting (6.A, 6.B) was also high/medium relevance due to the use of predictive modeling on spending data. System Evaluation (12.B) is high relevance due to the extensive model performance comparison. The domain of Mobile-First Design (9.A) was considered but rejected for direct relevance, only providing contextual background on online platforms. Data Privacy (10.A) was considered low relevance as privacy is not a central focus, though user data use is discussed. The domains of Filipino Cultural Context (2.A-D), Expense Categorization (3.A-C), Existing Systems (4.A-B), Budget Recommendation (7.A-D), Retention (11.A-B), Savings & Debt (13.A-C) were considered and rejected as the paper does not address these topics. Borderline cases included seasonal spending (2.B) being tangentially related to betting patterns but not addressed, and user-defined constraints (3.C) touching on self-report data but not in a PFMS context. Overall, the paper is highly relevant to Odin's predictive modeling, profiling, and anomaly detection modules, but has limited direct applicability to cultural, budgeting, or debt management domains.
limitations:
  - Single-site account data may not capture gambling behaviour across multiple platforms. [unacknowledged]
  - Self-report survey variables and the PGSI outcome share common method bias due to simultaneous collection. [unacknowledged]
  - Survey respondents were more engaged bettors, potentially limiting generalisability to the full customer base.
  - The study did not compare performance using the first 30 days of account history, only the 30 days preceding the survey.
remember_this:
  - Classification models using 30 days of data match six-month data performance.
  - Adding gambling satisfaction and account count variables lifts AUROC from 0.752 to 0.850.
  - XGBoost outperforms Random Forest and other algorithms in this risk detection context.
  - The models correctly classify 66% of high-risk individuals but flag many false positives.
  - Short-term data windows enable earlier risk detection and intervention in PFMS systems.
```
---

## Paper 32: Li C. et al_summarized.md

**Source File:** `Li C. et al_summarized.md`

```yaml
paper_id: 10.1109/ACCESS.2026.3697984
designation: international-algorithm-specific
title: "BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation With Autoencoder-Enhanced Feature Learning"
authors: "Li, C.; Ishak, I.; Ibrahim, H.; Zolkeply, M.; Sidi, F.; Li, C."
year: 2026
venue: IEEE Access
odin_topics:
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 7.A
  - 7.B
  - 12.A
  - 12.B
  - 12.C
tldr: "BIRCH-AE integrates BIRCH clustering with autoencoder feature learning and ensemble consensus to enable scalable, high-quality e-commerce user segmentation."
problem_and_motivation: "Traditional clustering algorithms fail to scale to millions of users and suffer from the curse of dimensionality when processing high-dimensional behavioral data. Moreover, they cannot adapt incrementally to new users, making them unsuitable for dynamic e-commerce environments. There is a gap in systematic approaches that combine scalable hierarchical methods with advanced feature learning for e-commerce segmentation."
approach:
  - "Uses a deep autoencoder to compress 30-50 behavioral features into a 14-dimensional latent space."
  - "Employs the Balanced Iterative Reducing and Clustering using Hierarchies (BIRCH) algorithm for memory-efficient, single-pass clustering."
  - "Generates ensemble diversity by varying BIRCH parameters and global clustering methods, including agglomerative and K-Means on CFs."
  - "Implements four ensemble consensus strategies: Majority Voting, Weighted Voting, AASC, and a novel BOHC method."
  - "Features a dynamic selection mechanism that automatically chooses the best ensemble strategy based on a multi-criteria score."
  - "Evaluated on Retail Rocket (1.4M users) and E-Commerce Behavior (4.5M users) datasets using repeated 30% stratified subset trials."
  - "Benchmarks against K-Means, PCA+K-Means, Agglomerative, and standard BIRCH across 5 to 25 clusters."
findings:
  - "num: BOHC achieves up to 23% silhouette score improvement over a single BIRCH model on transaction-focused data."
  - "num: Autoencoder feature learning improves clustering quality by 23-53% over raw features."
  - "num: A full-scale BOHC run on 4.5M users completed in approximately 5 minutes."
  - "Domain granularity is a critical determinant: ensemble methods excel on single-domain datasets, while base algorithms are superior on multi-domain data."
  - "BIRCH maintains superior performance at higher cluster counts where K-Means degrades dramatically, e.g., 0.603 vs. 0.332 at 15 clusters."
key_figures_tables:
  - "Figure 2: Performance comparison on Retail Rocket → Ensemble methods, especially BOHC/AASC, achieve the highest quality."
  - "Figure 4: Autoencoder training and impact → AE features significantly outperform PCA and raw features."
  - "Figure 5: Single-domain category comparison → Ensemble methods consistently outperform base algorithms in electronics and appliances."
  - "Table 2: Base vs. ensemble performance on Retail Rocket → BOHC and AASC are the top performers."
  - "Table 4: Performance on multi-category E-Commerce Behavior → Base algorithms excel over ensembles."
  - "Table 6: Cross-dataset summary → Single-domain favors ensembles, multi-domain favors base algorithms."
key_equations:
  - equation: "CF = (N, LS, SS)"
    explanation: "Clustering Feature summary of a cluster for BIRCH."
  - equation: "D0 = ||LS1/N1 - LS2/N2||"
    explanation: "Centroid Euclidean distance metric for CFs."
  - equation: "z = f_theta_e(x) = sigma(W_e x + b_e)"
    explanation: "Encoder maps input to a latent representation."
  - equation: "L_total = L_reconstruction + lambda_1 * L_sparsity + lambda_2 * ||theta||^2"
    explanation: "Autoencoder training objective with regularization."
  - equation: "A_ij^BOHC = (1/M) * sum_{m=1}^{M} exp(-alpha * h_m(i, j))"
    explanation: "BOHC affinity based on hierarchical merge heights."
  - equation: "Score(E) = 0.5*S_norm(E) + 0.3*CH_norm(E) - 0.2*DB_norm(E)"
    explanation: "Composite score for dynamic ensemble selection."
definitions:
  - term: BIRCH
    definition: "Balanced Iterative Reducing and Clustering using Hierarchies; a scalable, incremental clustering algorithm."
  - term: CF Tree
    definition: "Clustering Feature Tree; a height-balanced tree that stores compact summaries of data points."
  - term: Autoencoder
    definition: "A neural network for unsupervised feature learning that compresses data into a lower-dimensional latent space."
  - term: BOHC
    definition: "BIRCH-Optimized Hierarchical Consensus; a novel ensemble method that uses hierarchical affinity matrices."
  - term: AASC
    definition: "Advanced Affinity-based Spectral Clustering; an ensemble method using a co-association matrix and spectral clustering."
critical_citations:
  - "[Zhang et al., 1996] — Introduces the BIRCH algorithm, foundational to this work."
  - "[Xie et al., 2015] — Pioneers deep embedded clustering, contrasting with BIRCH-AE's modular approach."
  - "[Strehl and Ghosh, 2002] — Foundational work on ensemble clustering methods."
  - "[Zhao et al., 2021] — Addresses correlated variables in high-dimensional customer segmentation."
relevance:
  topics:
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Context for evaluating a new scalable user segmentation system."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Directly addresses scalability, high-dimensionality, and dynamic data limitations of traditional methods."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "The framework is a method for creating behavioral profiles, relevant to PFMS."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Provides a concrete algorithm for classifying users into behavioral segments."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "contextual"
      justification: "User segmentation informs tailoring of budgeting strategies."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Segmentation is a prerequisite for effective personalized budget recommendations."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides a rigorous quantitative evaluation framework using multiple metrics."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Extensive evaluation of the clustering algorithm's performance."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "contextual"
      justification: "The methodology for evaluating a clustering system is analogous to evaluating recommendations."
  contribution: "BIRCH-AE provides a scalable hierarchical clustering framework that can be adapted to segment Filipino young professionals for personalized financial planning. Its ability to handle large-scale, high-dimensional data and incrementally update user segments is directly applicable to Odin's need for dynamic user profiling and classification. The autoencoder integration addresses the challenge of correlated financial behavioral features, while the BOHC ensemble method offers a way to improve segmentation quality for distinct user groups. The dynamic ensemble selection mechanism ensures the system can adapt to different types of financial data, mirroring Odin's requirement for robustness."
  directly_justifies:
    - "BIRCH-AE demonstrates that hierarchical clustering can effectively segment millions of users, supporting Odin's need for scalability."
    - "Autoencoder-based feature learning improves clustering quality by 23-53%, justifying its use for extracting latent behavioral patterns."
    - "Incremental learning in BIRCH-AE enables real-time user segment updates, a critical capability for a dynamic PFMS."
    - "Domain granularity influences optimal method selection, suggesting Odin should tailor its approach to the type of financial data."
    - "BIRCH maintains higher performance at granular cluster counts, allowing for fine-grained segmentation of user financial behavior."
  limits:
    - "Evaluation is limited to e-commerce datasets; applicability to financial transaction data requires further validation."
    - "Temporal dynamics of user behavior are not explicitly modeled; the framework treats users as static entities."
    - "Cluster quality is assessed using internal metrics without external business-impact validation."
    - "The dynamic selection weights are fixed; sensitivity to this choice is not exhaustively explored."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The most relevant domains identified were 'Existing Systems & Gaps' (4.A, 4.B), 'Behavioral Profiling & Classification' (5.A, 5.C), 'Budget Recommendation' (7.B), and 'System Evaluation' (12.A, 12.B). 4.B was rated 'high' because the paper directly identifies scalability and adaptability limitations of traditional clustering. 5.C and 12.B were rated 'high' as the paper proposes a novel algorithm and provides a thorough evaluation. Topics under 'Mobile-First Design' (9.A, 9.B), 'Data Privacy' (10.A), and 'User Retention & Engagement' (11.A, 11.B) were considered and rejected as the paper does not address these aspects. The topics 'Budgeting Strategies as Domain Knowledge' (7.A) and 'Evaluation Methodologies for Budget Recommendation Systems' (12.C) were flagged as 'contextual' as the segmentation method is foundational to these areas. The paper's core contribution as a scalable segmentation framework makes it highly relevant to Odin's algorithmic design, especially for user classification and the need for a robust evaluation methodology."
limitations:
  - "The autoencoder reduces interpretability, obscuring direct feature-to-cluster relationships. [unacknowledged]"
  - "The framework faces a cold-start problem for users with minimal historical data. [unacknowledged]"
  - "The evaluation metrics are internal; no external validation on business outcomes like retention or campaign lift is provided."
  - "Memory constraints for ensemble affinity matrices may limit scalability to extremely large datasets at the full user-level."
  - "The framework's performance on domains with clusters defined by higher-order feature interactions is not guaranteed."
remember_this:
  - "BIRCH-AE segments 4.5M e-commerce users in 5 minutes using a scalable hierarchical ensemble."
  - "Autoencoder integration improves clustering quality by 23-53% over raw features."
  - "Domain granularity dictates method choice: single-domain favors ensembles, multi-domain favors base algorithms."
  - "BIRCH maintains performance at high cluster counts, supporting multi-resolution segmentation."
  - "The BOHC ensemble method leverages hierarchical structure to improve consensus accuracy."
```
---

## Paper 33: Olabintan_summarized.md

**Source File:** `Olabintan_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international-algorithm-specific
title: FairLend-Africa: An Explainable Machine Learning Framework for Alternative Credit Scoring Using Behavioral Financial Data in Financially Excluded African Communities
authors: Olabintan, I.
year: 2026
venue: Unknown
odin_topics:
  - 10.A
  - 7.D
  - 8.A
  - 6.A
  - 6.B
  - 5.A
  - 5.C
  - 4.A
  - 4.B
  - 12.A
  - 12.B
tldr: An explainable ML framework combines XGBoost, SHAP, and fairness auditing for credit scoring using behavioral financial data from mobile money, airtime, and savings.
problem_and_motivation: Over 1.4 billion adults lack formal credit histories, excluding them from traditional credit systems. Mobile money creates an alternative data source, but integrating it fairly and explainably remains challenging. A framework combining predictive performance with interpretability and fairness auditing is needed for underserved populations.
approach:
  - A synthetic dataset of 10,000 borrower records is generated with 16 raw and 4 engineered behavioral features from mobile money, airtime, and savings domains.
  - An XGBoost classifier is trained after hyperparameter optimization via RandomizedSearchCV with 5-fold CV, using median imputation for MNAR missing data.
  - The framework evaluates ROC-AUC and compares against logistic regression and majority class baselines on a held-out test set.
  - SHAP TreeExplainer provides local and global explanations, using dependence plots and waterfall charts.
  - A fairness audit evaluates demographic parity, equal opportunity, and predictive parity across regional and gender subgroups using the 80% rule.
  - The complete system is implemented as a REST API with a React dashboard and released as open source.
findings:
  - "num: The tuned XGBoost model achieves a test ROC-AUC of 0.714, which aligns with benchmarks in thin-file credit scoring literature."
  - "num: Logistic regression achieves near-identical performance (AUC = 0.713), suggesting primarily linear structures in the synthetic data."
  - "num: SHAP analysis identifies wallet balance trend as the dominant feature with a mean SHAP value of 0.377, 1.74 times the second-ranked feature."
  - The synthetic data fairness audit finds no disparity across groups under the data's demographic-behavioral independence assumption, but this requires empirical verification.
  - Engineered composite features provide no measurable predictive lift in the ablation study, with a ΔAUC of -0.0002.
  - SHAP explanations are implemented to provide individual-level transparency for credit decisions, suitable for loan officer and borrower communication.
key_figures_tables:
  - "Figure 4: ROC curve on held-out test set → AUC of 0.714 shows meaningful discrimination."
  - "Table 3: Model comparison test set performance → Tuned XGBoost has 0.714 ROC-AUC."
  - "Figure 7: Global feature importance by SHAP → Wallet balance trend dominates all other features."
  - "Table 5: Fairness disparity ratios → All ratios exceed 0.80 across all groups."
  - "Figure 11: Demographic parity analysis → Selection rates are equal across all subgroups."
key_equations:
  - equation: "f(x_i) = φ_0 + ∑_{j=1}^{p} φ_{ij}"
    explanation: "SHAP decomposition into base rate and feature contributions."
  - equation: "logit(P(y=1)) = β_0 + ∑ β_j x_j + ε"
    explanation: "Data generating process for synthetic labels."
definitions:
  - term: "ROC-AUC"
    definition: "Area Under the Receiver Operating Characteristic Curve, a measure of model discrimination."
  - term: "SHAP"
    definition: "SHapley Additive exPlanations, a game-theoretic method for explaining model predictions."
  - term: "MNAR"
    definition: "Missing Not At Random, where missingness is related to the missing value itself."
  - term: "Demographic Parity"
    definition: "Equal positive prediction rates across demographic groups."
  - term: "Equal Opportunity"
    definition: "Equal true positive rates across demographic groups."
critical_citations:
  - "[Björkegren and Grissen, 2018] — Established AUC baseline ~0.70 for behavioral credit scoring."
  - "[Lundberg and Lee, 2017] — Introduced SHAP framework used for model explainability."
  - "[Baesens et al., 2003] — Found ensemble methods outperform single classifiers in credit scoring."
  - "[Chouldechova, 2017] — Demonstrated impossibility of satisfying all fairness criteria simultaneously."
relevance:
  topics:
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "medium"
      justification: "Paper discusses synthetic data use to address privacy and regulatory barriers."
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "low"
      justification: "Discusses threshold tuning cost asymmetry but not explicit infeasibility handling."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "contextual"
      justification: "Methodological framework for ML could be adapted, but anomaly detection not a focus."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Core contribution is a predictive modeling framework for credit scoring."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "low"
      justification: "Uses static features; sequential forecasting is not addressed."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Features engineered to capture behavioral signals like savings consistency."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "Evaluates ML classification approaches using behavioral features."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Reviews existing systems and alternative data landscape."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Identifies gaps: lack of formal credit histories, limited explainability, fairness concerns."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Provides evaluation framework with ROC-AUC and fairness metrics."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Includes detailed evaluation of prediction, explainability, and fairness modules."
  contribution: "This paper contributes a predictive modeling module for assessing creditworthiness from behavioral data. The SHAP explanation module provides local and global interpretability suitable for explaining decisions to users or loan officers. The fairness auditing module offers a systematic method to evaluate and mitigate demographic disparities. These modules are integrated into a deployable architecture, demonstrating how Odin might incorporate alternative data for financial behavior analysis. The codebase and methodology serve as a reference for implementing similar explainable AI components in a PFMS."
  directly_justifies:
    - "Behavioral financial data from mobile money can serve as a proxy for creditworthiness."
    - "XGBoost with SHAP can provide both predictive performance and individual-level explanations."
    - "Fairness criteria like demographic parity and equal opportunity can be audited systematically."
    - "Synthetic data generation is a valid method for methodology development in privacy-sensitive domains."
  limits:
    - "All results are based on synthetic data and do not generalize to real African borrower behavior."
    - "The fairness audit relies on the synthetic data's designed independence between demographics and behavior."
    - "The engineered composite features provided no measurable improvement over raw features."
    - "SHAP explanations assume feature independence, which may misrepresent contributions with correlated features."
    - "Temporal stability and concept drift are not evaluated, limiting production readiness."
  mapping_rationale: "A systematic scan across all 12 functional domains was conducted. The paper was flagged as highly relevant to predictive modeling (6.A) and system evaluation (12.A, 12.B), as its core contribution is a framework for predictive credit scoring with performance and fairness metrics. It has medium relevance to behavioral profiling (5.A, 5.C) and system gaps (4.B) because it uses engineered behavioral features and identifies limitations of existing credit systems. It has low relevance to forecasting (6.B) and infeasibility handling (7.D) since it does not address sequential data or constraint reduction. Data privacy (10.A) was assessed as medium relevance due to the paper's explicit use of synthetic data to circumvent privacy barriers. Borderline cases included behavioral features touching both 5.A and 2.D (seasonal patterns), but seasonal patterns were not explicitly modeled, so only 5.A was selected. The overall relevance is methodological, providing infrastructure for future empirical work rather than direct evidence for Odin's specific design decisions."
limitations:
  - "Dataset is synthetic; results require validation on real mobile money data."
  - "Fairness analysis is constrained by the synthetic data's independence assumption."
  - "Feature set is literature-informed and may differ substantially across populations."
  - "Temporal stability and concept drift are not evaluated. [unacknowledged]"
  - "Engineered features provided no measurable benefit in this dataset."
  - "SHAP explanations can be manipulated and assume feature independence."
  - "Model accuracy falls below the majority-class baseline at the optimal threshold."
remember_this:
  - "XGBoost achieved a ROC-AUC of 0.714 on synthetic behavioral credit data."
  - "SHAP identified wallet balance trend as the dominant creditworthiness signal."
  - "Fairness audit showed no disparity due to synthetic data independence assumption."
  - "Logistic regression performed nearly identically to XGBoost on this dataset."
  - "Results are methodological and require real-world validation before deployment."
```
---

## Paper 34: Patel & Singh_summarized.md

**Source File:** `Patel & Singh_summarized.md`

```yaml
paper_id: 5c8f3d6e-8b1a-5a2b-9c4d-7e6f8a9b0c1d
designation: international-algorithm-specific
title: An Intelligent AI-Based Framework for Automated Personal Financial Management
authors: Patel, A.; Singh, A.
year: 2026
venue: International Conference on Multidisciplinary Perspectives in Advanced Computing and Technology (IMPACT 2026)
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 9.A
  - 9.B
  - 10.A
  - 11.A
  - 11.B
tldr: Integrates AI and full-stack technology to aggregate financial data, classify transactions, forecast spending, and deliver personalized budgeting recommendations and alerts.
problem_and_motivation: Digital financial services generate fragmented personal data that manual tracking cannot efficiently manage. Existing applications lack intelligent automation and personalized decision support, creating a gap between raw data and informed financial decisions, especially for young professionals.
approach:
  - Collects financial data from multiple digital sources like UPI and banking records using secure APIs.
  - Preprocesses and normalizes raw transaction data for consistency and analysis.
  - Classifies transactions automatically using a hybrid of rule-based logic and machine learning algorithms.
  - Employs statistical and time-series methods to analyze spending patterns and forecast future expenditures.
  - Implements an event-driven background workflow for periodic report generation and AI analysis.
findings:
  - AI-driven classification enhanced accuracy in categorizing transactions compared to manual procedures.
  - The system aggregates financial information from different platforms into a unified real-time interface.
  - The budgeting module analyzes previous spending to generate personalized budget limits.
  - Alert notifications inform users when spending approaches or exceeds predefined thresholds.
  - Predictive insights enable users to anticipate future expenditures and improve financial planning.
  - Interactive dashboards and simplified statements improved user financial understanding and engagement.
key_figures_tables:
  - Figure 1: Monthly expense breakdown by category → Shows automated categorization and spending distribution.
  - Figure 2: Income and expense analysis dashboard → Visualizes aggregated financial data for user insights.
  - Table 1: Methodology phases → Outlines data collection, preprocessing, categorization, and visualization steps.
  - Table 2: Result analysis comparison → Demonstrates performance improvements over traditional tools.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: None.
    definition: ""
critical_citations:
  - "[Grass & Lynch, 1982] — foundational resource for financial workshop proceedings."
  - "[Naik et al., 2024] — discusses automated expense tracking systems."
  - "[Stefanov et al., 2024] — covers personal finance management application design."
  - "[Fernández, 2019] — reviews AI applications in financial services."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Proposes ML and rule-based automated transaction categorization.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: Discusses classification into categories like food, travel, bills.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Reviews traditional systems and identifies their limitations.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Explicitly outlines lack of intelligence, automation, and integration.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Implements forecasting of future expenditures based on historical data.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Uses time-series analysis and regression for expense prediction.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Provides adaptive budgeting based on spending behavior analysis.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Generates personalized budget limits and recommendations.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Mentions detection of anomalies in spending patterns indirectly.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Does not focus on a specific anomaly detection algorithm.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: Suggests future deployment as a cross-platform mobile application.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: Mentions user engagement but not specific mobile UX design details.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Emphasizes secure storage and management of financial information.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Claims improved user engagement through alerts and analytics.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: low
      justification: Discusses notifications but not specific retention mechanisms.
  contribution: The paper provides a modular architecture integrating AI for automated transaction categorization and predictive analytics, which directly informs Odin's expense tracking module. Its emphasis on aggregating fragmented data from multiple digital payment sources supports Odin's data integration layer design. The adaptive budgeting and alert system offers a blueprint for Odin's recommendation engine. The discussion of security and privacy considerations provides foundational justification for Odin's data protection protocols. Overall, the framework demonstrates how AI can enhance user financial awareness and decision support.
  directly_justifies:
    - Automated transaction categorization using rule-based and ML techniques is feasible and improves accuracy.
    - Aggregating financial data from multiple sources into a single platform enhances financial awareness.
    - Predictive analytics on historical spending data can enable effective future expense forecasting.
    - Personalized budget recommendations based on spending behavior promote better financial discipline.
    - Real-time alerts and visual analytics increase user engagement and sound financial decision-making.
  limits:
    - The system's performance depends on the quality of input data and reliability of third-party services. [unacknowledged]
    - Direct bank API integration for real-time synchronization is not fully implemented and is noted as future work.
    - The study does not provide quantitative performance metrics from a large-scale user study.
    - Security measures are discussed generally, without detailing specific encryption or blockchain implementations.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was conducted. Domains relevant to expense categorization (3.A, 3.B), existing systems (4.A, 4.B), forecasting (6.A, 6.B), and budgeting (7.A, 7.B) were flagged as high relevance because the paper directly addresses these with proposed algorithms and system features. Domains like anomaly detection (8.A, 8.B) and engagement (11.A, 11.B) were assigned medium or low relevance, as they are mentioned but not the core focus. The paper's general nature led to rejecting culturally specific domains (2.A-D) and Filipino demographic topics (1.A-C). The paper's contribution is overall highly relevant to Odin's architectural and algorithmic modules.
limitations:
  - Direct bank API-UPI gateway integration for real-time synchronization is not fully implemented. [unacknowledged]
  - Deep learning algorithms for expense forecasting are suggested but not incorporated in the current framework. [unacknowledged]
  - Features like investment analysis, credit score evaluation, and debt management are outside the system's scope. [unacknowledged]
  - The system has not been deployed as a cross-platform mobile application for large-scale testing. [unacknowledged]
  - Relies on the accuracy and availability of third-party AI and data ingestion services.
remember_this:
  - Integrates rule-based and ML for accurate automated transaction categorization.
  - Aggregates fragmented data from multiple digital payment platforms into one view.
  - Uses historical spending to forecast future expenses and personalize budgets.
  - Real-time alerts and interactive dashboards enhance financial discipline and awareness.
  - Reduces manual effort and improves financial transparency compared to traditional tools.
```
---

## Paper 35: Zhang & Hou_summarized.md

**Source File:** `Zhang & Hou_summarized.md`

```yaml
paper_id: 10.1016/j.procs.2026.05.035
designation: international-algorithm-specific
title: Consumer Behavior Data Mining and Analysis Using Machine Learning Algorithms
authors: Zhang, H.; Hou, Y.
year: 2026
venue: Procedia Computer Science
odin_topics:
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 12.B
  - 12.C
tldr: XGBoost achieves the highest accuracy and F1 score among four ML algorithms for predicting customer purchase intention from e-commerce transaction data.
problem_and_motivation: Predicting customer purchase intention from vast e-commerce data is challenging for traditional statistical tools. A systematic comparison of modern machine learning algorithms under a unified framework is needed to guide model selection for practical applications.
approach:
  - Used the UCI Online Retail dataset with transactions from Dec 2020 to Dec 2021 for model training and evaluation.
  - Engineered 28 numerical features per customer, including RFM, behavioral breadth, consumption patterns, and temporal patterns.
  - Evaluated logistic regression, SVM, random forest, and XGBoost on the binary prediction task of future purchase intent.
  - Employed grid search with 5-fold cross-validation for hyperparameter tuning on the training set.
  - Assessed models on a held-out test set using accuracy, precision, recall, F1 score, and AUC metrics.
findings:
  - XGBoost achieves the highest F1 score of 0.680 and AUC of 0.872 among all models tested.
  - Random forest obtains a balanced performance with an F1 score of 0.651 and AUC of 0.853.
  - Logistic regression shows the lowest recall at 0.468, indicating a conservative prediction strategy.
  - Recency is the most important predictor across all models, validating the RFM framework's core premise.
  - XGBoost demonstrates superior training efficiency compared to random forest despite its higher accuracy.
key_figures_tables:
  - Table 1: Comprehensive performance metrics for four models → XGBoost leads all models across accuracy, F1, and AUC.
  - Table 2: Training and prediction time comparison → Logistic regression is fastest; SVM is slowest; XGBoost is efficient.
  - Table 3: Top three feature importance rankings → Recency is consistently the most important feature across models.
key_equations:
  - equation: P(y = 1 | x) = 1 / (1 + e^{-(w^T x + b)})
    explanation: Sigmoid function maps features to purchase probability in logistic regression.
  - equation: f(x) = sign(∑_{i=1}^{n} α_i y_i K(x_i, x) + b)
    explanation: Decision function for SVM using kernel trick for nonlinear classification.
definitions:
  - term: RFM
    definition: Recency, Frequency, Monetary; a customer segmentation framework using three transaction metrics.
  - term: AUC
    definition: Area Under the ROC Curve; measures the model's ability to rank positive samples higher than negative ones.
  - term: XGBoost
    definition: eXtreme Gradient Boosting; an optimized implementation of gradient boosting for efficiency and performance.
critical_citations:
  - "[Akram, 2025] — Reviews ML algorithms for consumer behavior prediction."
  - "[Lin, 2023] — Applies ML to e-commerce customer shopping behavior analysis."
  - "[Zvarikova, 2022] — Discusses cognitive AI algorithms for customer behavior analysis."
relevance:
  topics:
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: The study's feature engineering and predictive modeling approach can inform how Odin initializes user profiles based on sparse transaction data.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: The paper compares classification algorithms (LR, SVM, RF, XGBoost) that could be used to classify user spending behavior profiles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: The paper directly addresses predictive modeling of consumer behavior using machine learning on transaction data.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: The study compares various forecasting algorithms, including XGBoost and Random Forest, on sequential transaction data for future purchase prediction.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: The paper provides a rigorous comparative evaluation framework for different machine learning algorithms on an e-commerce dataset.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: The evaluation metrics (accuracy, F1, AUC, efficiency) and cross-validation methodology are directly applicable to testing budget recommendation modules in Odin.
  contribution: The paper's comparative analysis of ML algorithms provides a benchmark for Odin's spending forecasting module, suggesting XGBoost as a high-accuracy option. The feature importance analysis validates RFM as a core framework for behavior prediction in personal finance. The evaluation methodology establishes a template for testing Odin's algorithmic modules, including efficiency metrics crucial for mobile-first applications. The study's approach to handling customer transaction data informs how Odin can structure and process user spending history for predictive tasks.
  directly_justifies:
    - "XGBoost achieves the highest predictive accuracy for future purchase behavior among tested algorithms."
    - "Recency of customer activity is the strongest predictor of future behavior."
    - "Ensemble methods (XGBoost, Random Forest) outperform linear models in predicting purchase intent."
    - "Evaluation of algorithms must consider both accuracy and computational efficiency for practical deployment."
  limits:
    - "The analysis is conducted on e-commerce transaction data, not personal finance spending data."
    - "The paper focuses on predicting purchase intent, not directly on budgeting or anomaly detection."
    - "The dataset is international and not specific to Filipino young professionals. [unacknowledged]"
    - "The study does not consider interpretability trade-offs in depth beyond feature importance. [unacknowledged]"
  mapping_rationale: This paper was systematically scanned against all 12 functional domains. The core contribution is an algorithmic comparison for predictive modeling, making it highly relevant to the Spending Forecasting domain (Topics 6.A, 6.B) and System Evaluation (Topics 12.B, 12.C). It also provides medium relevance to Behavioral Profiling & Classification (Topics 5.B, 5.C) through its classification approach and feature engineering. Domains like Filipino Cultural Context, Expense Categorization, and Mobile-First Design were rejected as the study does not address cultural factors, budget categories, or mobile-specific design considerations. The user retention domain was considered but rejected as the paper does not discuss engagement dynamics or retention mechanisms. The overall relevance is moderate, primarily contributing to forecasting and evaluation methodologies for Odin.
limitations:
  - The study uses e-commerce transaction data, which may not fully represent personal financial management scenarios.
  - The paper does not address real-time prediction latency or deployment constraints for mobile applications. [unacknowledged]
  - Generalizability to the Filipino context or young professional demographics is not established. [unacknowledged]
remember_this:
  - XGBoost achieves the best F1 score (0.680) for predicting purchase behavior.
  - Recency is the single most important predictor of future customer activity.
  - Logistic regression offers the fastest processing but the lowest predictive accuracy.
  - Feature engineering with domain knowledge (RFM) is as critical as model selection.
  - Ensemble methods like XGBoost provide a superior balance of accuracy and efficiency.
```
---

## Paper 36: Chikoore et al_summarized.md

**Source File:** `Chikoore et al_summarized.md`

```yaml
paper_id: 10.1109/ACCESS.2026.3703181
designation: international-algorithm-specific
title: Adaptive Credit Scoring Model With Concept Drift Detection and Adaptation Technique for a Dynamic Environment
authors: Chikoore, R.; Ojo, S. O.; Kogeda, O. P.
year: 2026
venue: IEEE Access
odin_topics:
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 8.C
  - 12.A
  - 12.B
tldr: An adaptive fusion framework integrates baseline machine learning models with dynamic adaptation to counter concept drift, achieving 95.0% accuracy in credit scoring under distributional shifts.
problem_and_motivation: Static credit scoring models degrade as borrower behavior and economic conditions change, exposing lenders to financial and regulatory risks. Existing adaptive solutions are designed for advanced economies and lack effectiveness in developing contexts. A robust framework is needed to detect and adapt to drift in dynamic, resource-constrained environments.
approach:
  - Used the German Credit dataset and introduced three synthetic drift scenarios.
  - Benchmarked vanilla models including CART, Naïve Bayes, Random Forest, and XGBoost.
  - Developed adaptive strategies: model retraining, windowing, ensemble learning, and a proposed Adaptive Fusion algorithm.
  - Adaptive Fusion dynamically weights outputs from three Random Forest models for real-time prediction.
  - Evaluated performance using accuracy, precision, recall, F1-score, and ROC-AUC.
findings:
  - num: The Adaptive Fusion, Ensemble, and Retrained Random Forest models each achieved an accuracy of 95.0%.
  - num: Adaptive Fusion maintained a precision of 0.9275, recall of 0.9645, and F1-score of 0.9426.
  - num: ROC-AUC values exceeded 0.96 for the best-performing adaptive models.
  - num: The method outperformed the state-of-the-art DGHNL model, which achieved 94.60% accuracy and an AUC of 0.9360.
  - Adaptive Fusion proved the most robust solution, enabling continuous adaptation to evolving patterns.
  - The windowed learning approach underperformed, showing limitations in capturing long-term behavioral shifts.
  - The ensemble approach performed well but was slightly less stable than Adaptive Fusion.
key_figures_tables:
  - Figure 3: Vanilla model performance comparison on original dataset → Random Forest was the best baseline.
  - Figure 4: ROC-AUC for adaptive retraining on drift scenarios → ROC-AUC remained high, demonstrating effective adaptation.
  - Figure 5: Model evaluation results on adaptive strategies → Adaptive Fusion and Retrained Random Forest were top performers.
  - Table 1: Vanilla model performance metrics on original dataset → Random Forest achieved the highest accuracy (0.77) and ROC-AUC (0.768).
key_equations:
  - equation: X_d = X_n + 5
    explanation: Simulates temporal shift by increasing all age values.
  - equation: New credit amount = Original credit amount + N(0,1000)
    explanation: Adds Gaussian noise to model variability in loan sizes.
  - equation: p_{final} = w_0 p_0 + w_r p_r + w_w p_w
    explanation: Fuses model probabilities via dynamically updated weights.
definitions:
  - term: Concept drift
    definition: A change in the data distribution over time that degrades model performance.
  - term: Adaptive fusion
    definition: An algorithm that dynamically integrates multiple model outputs based on recent performance.
  - term: ROC-AUC
    definition: A metric for a model's ability to distinguish between classes, useful for drift detection.
critical_citations:
  - "[Museba, 2023] — Supports effectiveness of heterogeneous ensembles in credit scoring."
  - "[Krempl et al., 2000] — Advocates for explicit drift modelling in financial data."
  - "[Barddal et al., 2020] — Demonstrates data stream learners outperform static models."
relevance:
  topics:
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies static models' failure in dynamic environments.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: Discusses evolving borrower behavior leading to concept drift.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: contextual
      justification: Addresses adaptation to changing borrower characteristics over time.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: The adaptive fusion method is a classification approach for dynamic profiles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: The paper focuses on predictive modeling under distributional shifts.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Directly evaluates and proposes an algorithm for forecasting under drift.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Mentions fraud detection as an application domain.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Adaptive algorithms are applicable to detecting anomalies in spending.
    - code: 8.C
      name: Cold‑Start Baseline Strategies for Anomaly Detection
      relevance: medium
      justification: Transfer learning discussed for initial model building.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses standard metrics like accuracy and AUC for evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Compares multiple algorithmic modules like retraining, ensemble, and fusion.
  contribution: "The study introduces a novel Adaptive Fusion algorithm for credit scoring that dynamically integrates multiple models. This approach directly informs the design of Odin's budget recommendation and anomaly detection modules, which must also adapt to shifting spending patterns. The framework's use of retraining and windowing strategies provides a methodological blueprint for handling concept drift in forecasting. Its emphasis on maintaining model robustness under class imbalance is relevant for detecting rare but significant financial events. The evaluation framework based on accuracy, precision, recall, and F1-score offers a template for assessing Odin's algorithmic modules."
  directly_justifies:
    - "Adaptive Fusion can maintain high predictive accuracy under concept drift by dynamically reweighting model outputs."
    - "Retraining models on recent data is effective for adapting to long-term behavioral shifts."
    - "Ensemble methods offer a stable approach to handling data distribution changes without full retraining."
    - "Window-based approaches have limitations in capturing long-term trends."
  limits:
    - "The experimental evaluation is limited to a single dataset (German Credit). [unacknowledged]"
    - "The paper does not explore the impact of different drift types on real-world Filipino spending data. [unacknowledged]"
    - "The computational cost of the adaptive fusion algorithm in a real-time system is not detailed. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains 'Spending Forecasting' (6.A, 6.B) and 'Anomaly Detection' (8.A, 8.B, 8.C) were flagged as having high relevance because the paper directly addresses algorithms for predictive modeling and drift adaptation under changing data distributions, which is analogous to forecasting Filipino young professionals' spending and detecting anomalies. The 'Behavioral Profiling' domain (5.A, 5.B, 5.C) was assessed as medium to contextual, as it discusses evolving borrower behavior but does not build financial profiles in the Odin sense. 'Existing Systems & Gaps' (4.A, 4.B) was also considered medium, as the paper critiques static systems and provides a solution. The 'System Evaluation' domain (12.A, 12.B) was flagged as relevant due to its detailed performance analysis. Other domains such as 'Filipino Cultural Context', 'Budget Recommendation', and 'User Retention' were considered but rejected as the paper does not address cultural practices, budget allocation constraints, or engagement mechanisms, being focused on a generic credit scoring algorithm. The overall relevance to Odin is significant for its algorithmic approaches to handling temporal data shifts."
limitations:
  - "The concept drift scenarios are synthetically generated, which may not fully represent real-world drifts."
  - "The study does not account for fairness and bias mitigation, which is critical for personal finance applications. [unacknowledged]"
  - "No data stream was used for real-time evaluation, limiting the assessment of the algorithm's true online performance. [unacknowledged]"
remember_this:
  - "Adaptive Fusion achieved 95.0% accuracy and an AUC exceeding 0.96 for credit scoring."
  - "Dynamic model integration outperformed static retraining and windowing techniques."
  - "Adaptive algorithms are essential for maintaining accuracy when data distributions change."
  - "Ensemble methods provide a stable, though less optimal, alternative to adaptive fusion."
  - "Concept drift detection is critical for forecasting personal finance behavior."
```
---

## Paper 37: Dhanekula & Munira_summarized.md

**Source File:** `Dhanekula & Munira_summarized.md`

```yaml
paper_id: 10.63125/p4y4te47
designation: international
title: Deep Neural Network Models for Real-Time Financial Forecasting and Market Intelligence
authors: Dhanekula, A.; Munira, M. S. K.
year: 2026
venue: American Journal of Advanced Technology and Engineering Solutions
odin_topics:
  - 6.B
  - 8.B
  - 12.B
  - 10.A
  - 9.A
tldr: A quantitative case study of a DNN forecasting service finds that data quality, robustness, and explanation quality are the strongest drivers of perceived forecasting and market intelligence effectiveness.
problem_and_motivation: Organizations deploy DNN forecasting services but lack quantitative evidence on which operational capabilities drive real-time effectiveness and whether forecasting gains convert into decision-ready intelligence. Decision teams need empirical guidance on capability priorities to maximize intelligence value.
approach:
  - Quantitative cross-sectional case-study design using a five-point Likert survey administered to N=210 active users of a DNN forecasting service.
  - Participants were 58.1% analysts, 21.9% traders, and 20.0% risk or portfolio staff.
  - Capability variables measured: Data Quality (DQ), Feature Richness (FR), Update Responsiveness (UR), Robustness (ROB), and Explanation Quality (EQ).
  - Outcome variables measured: Forecasting Effectiveness (FE) and Market Intelligence Effectiveness (MIE).
  - Analysis included descriptive statistics, reliability testing (Cronbach's alpha), Pearson correlations, and two multiple regression models with diagnostic checks.
findings:
  - num: Reliability was strong across all constructs (α = .84 to .90).
  - num: Mean ratings for all capability dimensions were high (DQ M=4.12, FR M=3.98, UR M=3.85, ROB M=3.90, EQ M=3.76).
  - num: Composite DNN capability correlated strongly with FE (r=.68, p<.001) and MIE (r=.62, p<.001).
  - num: FE correlated strongly with MIE (r=.71, p<.001).
  - num: Model 1 explained 56% of variance in FE (R²=.56), with significant effects for DQ (β=.32), ROB (β=.28), FR (β=.21), and UR (β=.14).
  - num: Model 2 explained 61% of variance in MIE (R²=.61), driven by FE (β=.52), EQ (β=.29), and UR (β=.12).
key_figures_tables:
  - "Figure 1: DNN-Driven Real-Time Financial Forecasting for Market Intelligence → Visualizes the end-to-end intelligence workflow."
  - "Figure 2: Real-Time Financial Forecasting: Concepts, Metrics, and Challenges → Summarizes forecast evaluation complexity."
  - "Figure 7: Conceptual Framework and Research Model Development → Depicts the hypothesized capability-to-intelligence pathway."
  - "Table 4: Pearson Correlation Matrix → Shows moderate-to-strong positive associations among all constructs."
  - "Table 5 & 6: Multiple Regression Models → Identifies DQ, ROB, FE, and EQ as the most influential predictors."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: DNN
    definition: Deep Neural Network, a multi-layer computational architecture for learning hierarchical representations.
  - term: DQ
    definition: Data Quality, perceived accuracy, completeness, and timeliness of input streams.
  - term: FR
    definition: Feature Richness, breadth of technical, macro, and alternative features available to the model.
  - term: UR
    definition: Update Responsiveness, frequency of model and feature refresh to reflect new information.
  - term: ROB
    definition: Robustness, stability of outputs under noisy or shifting conditions.
  - term: EQ
    definition: Explanation Quality, clarity and usefulness of the system's explanations for forecasts.
  - term: FE
    definition: Forecasting Effectiveness, perceived accuracy, timeliness, and stability of generated forecasts.
  - term: MIE
    definition: Market Intelligence Effectiveness, degree to which the service helps detect changes, prioritize assets, improve confidence, and coordinate actions.
critical_citations:
  - "[LeCun et al., 2015] — Foundational deep learning theory."
  - "[Gu et al., 2020] — DNNs capture nonlinear predictor interactions in finance."
  - "[Fischer & Krauss, 2018] — LSTM benchmarks in market prediction."
  - "[Ribeiro et al., 2016] — Local surrogate explanations for model interpretability."
  - "[Zhang et al., 2005] — Microstructure noise challenges in high-frequency data."
relevance:
  topics:
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: The paper directly evaluates a DNN forecasting service, identifying key drivers of forecasting effectiveness.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: The study provides a quantitative evaluation framework (survey, regression) for assessing algorithmic module performance.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: The paper discusses robustness and market intelligence which are relevant to anomaly detection contexts, though not the primary focus.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: The discussion mentions security controls (data lineage, access control, logging) for forecasting pipelines, providing background framing.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: The paper's focus on user-facing explanation quality and decision support offers tangential relevance to UX, but not mobile-specific design.
  contribution: The paper provides a validated quantitative framework for evaluating DNN forecasting services. It empirically demonstrates that data quality and robustness are the primary drivers of perceived forecasting effectiveness. The findings highlight that explanation quality is a critical independent predictor of market intelligence effectiveness. These results offer actionable levers for governance and monitoring of secure forecasting platforms. The study bridges technical forecasting performance with user-perceived decision value.
  directly_justifies:
    - "Prioritizing data quality and robustness controls is essential for real-time forecasting effectiveness."
    - "Forecasting effectiveness serves as the central transmission mechanism between capability and market intelligence."
    - "Explanation quality is a measurable driver of intelligence usefulness and decision confidence."
    - "Update responsiveness contributes significantly to both forecasting and intelligence outcomes."
  limits:
    - "Cross-sectional design limits causal inference."
    - "Single case-study context constrains generalizability."
    - "Self-reported Likert data captures perceived usefulness, not directly observed economic outcomes."
    - "Potential common method bias due to same-source survey responses."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to the "Forecasting Algorithms" (6.B) and "System Evaluation" (12.B) domains due to its direct focus on evaluating a DNN-based forecasting service and identifying key performance drivers. It was also deemed relevant to "Anomaly Detection" (8.B) given its treatment of robustness and market intelligence, which are conceptually linked to detecting outliers. "Data Privacy" (10.A) was flagged as contextual due to passing mentions of security controls in the discussion. Other domains like "Spending Patterns" (2.B, 2.D), "Expense Categorization" (3.A), "Savings" (13.A), and "Budget Recommendation" (7.A) were rejected as the paper's focus on financial market forecasting (asset returns, volatility) does not map to personal spending, saving, or budgeting contexts. The paper's overall relevance to Odin is moderate, providing a robust evaluation methodology and emphasizing the importance of data quality, robustness, and explainability for predictive systems.
limitations:
  - "Quantitative, cross-sectional design limits definitive causal interpretation."
  - "Single case-study setting constrains generalizability to other organizational contexts. [unacknowledged]"
  - "Self-reported Likert-scale data captures perceived outcomes rather than directly observed financial performance."
  - "Potential common method bias from collecting capability and outcome perceptions in the same instrument."
  - "The conceptual framework simplifies complex technical realities by using linear regression on perceptual dimensions. [unacknowledged]"
remember_this:
  - "Data quality and robustness are the strongest predictors of forecasting effectiveness."
  - "Forecasting effectiveness strongly mediates the link between capability and market intelligence."
  - "Explanation quality is an independent driver of market intelligence effectiveness."
  - "The evaluated model explained 61% of variance in perceived market intelligence effectiveness."
```
---

## Paper 38: Cabalfin et al_summarized.md

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

## Paper 39: Islam A. et al_summarized.md

**Source File:** `Islam A. et al_summarized.md`

```yaml
paper_id: "5d4e3c2b-1a0f-9e8d-7c6b-5a4f3e2d1c0b"
designation: "international-algorithm-specific"
title: "Benchmarking Machine Learning Models for Real-Time Fraud Detection in Digital Banking Transactions"
authors: "Islam, A.; Miah, M.; Akhir, A.; Munni, A.; Jahan, I.; Nashid, S."
year: 2026
venue: "Unknown"
odin_topics:
  - "8.A"
  - "8.B"
  - "8.C"
  - "12.A"
  - "12.B"
  - "5.C"
tldr: "Benchmarks machine learning models for real-time fraud detection, revealing trade-offs between detection accuracy, inference latency, throughput, and operational cost, with hybrid layered pipelines offering the best balance."
problem_and_motivation: "Current fraud detection systems often prioritize accuracy over real-time constraints and cost efficiency, leading to high false-positive rates and operational overhead. There is a lack of comprehensive benchmarking that simultaneously evaluates predictive performance, latency, and financial impact. This study addresses that gap by systematically assessing multiple models under streaming conditions."
approach:
  - "Used two datasets: ULB credit card fraud (284,807 transactions) and PaySim synthetic (6.36M transactions)."
  - "Evaluated Random Forest, XGBoost, LightGBM, LSTM, TCN, and Transformer models."
  - "Measured precision, recall, F1, ROC-AUC, PR-AUC, average and 95th percentile latency, throughput, and total cost from false positives and negatives."
  - "Implemented a streaming evaluation framework with Apache Kafka and Spark/Flink for real-time inference."
  - "Applied SMOTE for class imbalance and standardized preprocessing."
findings:
  - "num: XGBoost achieved ROC-AUC of 0.9998 and PR-AUC of 0.966 on PaySim."
  - "num: LSTM processed up to 18,315 transactions per second on ULB with sub-millisecond latency."
  - "num: Random Forest had 7.6 ms latency and 130 tx/sec throughput on ULB."
  - "Gradient-boosted models offered superior scalability and responsiveness compared to deep learning."
  - "Cost–benefit analysis showed that minimizing false positives and latency yields significant operational savings."
  - "Hybrid layered pipelines balance accuracy and latency effectively."
key_figures_tables:
  - "Table 2: Predictive performance on ULB dataset → XGBoost achieved highest F1 (0.859) among ensembles."
  - "Table 3: Predictive performance on PaySim dataset → XGBoost near-perfect ROC-AUC (0.9998) and PR-AUC (0.966)."
  - "Table 4: Real-time performance on ULB → LSTM had highest throughput (18,315 tx/sec)."
  - "Table 5: Real-time performance on PaySim → TCN and Transformer achieved >15,000 tx/sec with ~0.06 ms latency."
  - "Figure 22: Cost vs F1 plot → models with slightly lower F1 but much lower cost are more practical."
key_equations:
  - equation: "$f(x) = w^T x + b$, $p(y=1|x) = \\sigma(f(x))$"
    explanation: "Logistic regression linear score and probability."
  - equation: "$\\mathcal{L}_t \\approx \\sum_{i=1}^n [g_i f_t(x_i) + \\frac{1}{2} h_i f_t(x_i)^2] + \\Omega(f_t)$"
    explanation: "XGBoost second-order Taylor approximation for boosting."
  - equation: "$i_t = \\sigma(W_i x_t + U_i h_{t-1} + b_i)$"
    explanation: "LSTM input gate activation."
  - equation: "$c_t = f_t \\odot c_{t-1} + i_t \\odot \\tilde{c}_t$"
    explanation: "LSTM cell state update."
  - equation: "$y_t = \\sum_{k=0}^{K-1} W_k x_{t-d \\cdot k} + b$"
    explanation: "TCN dilated causal convolution."
definitions:
  - term: "Concept drift"
    definition: "Change in data distribution over time, degrading model performance."
  - term: "ROC-AUC"
    definition: "Area under the receiver operating characteristic curve, measures discriminative ability."
  - term: "PR-AUC"
    definition: "Area under the precision-recall curve, sensitive to imbalanced classes."
  - term: "Latency"
    definition: "Time taken for a model to make a prediction on a single transaction."
  - term: "Throughput"
    definition: "Number of transactions processed per second."
  - term: "SMOTE"
    definition: "Synthetic Minority Oversampling Technique to address class imbalance."
critical_citations:
  - "[Dal Pozzolo et al., 2015] — ULB dataset and imbalanced classification."
  - "[Lopez-Rojas & Axelsson, 2016] — PaySim synthetic dataset."
  - "[Jurgovsky et al., 2018] — sequence classification for fraud detection."
  - "[Bahnsen et al., 2016] — feature engineering for fraud detection."
relevance:
  topics:
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Directly addresses fraud detection as a critical anomaly detection task."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Benchmarks multiple algorithms (LSTM, XGBoost, etc.) on transaction data."
    - code: "8.C"
      name: "Cold‑Start Baseline Strategies for Anomaly Detection"
      relevance: "medium"
      justification: "Includes logistic regression as a baseline and discusses concept drift adaptation."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides a comprehensive evaluation framework including latency, throughput, and cost."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Evaluates individual models on predictive and operational metrics."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "low"
      justification: "Uses classification techniques, but not specifically for behavioral profiling; contextual relevance."
  contribution: "The paper's benchmarking framework provides a methodology for evaluating anomaly detection algorithms under real-time constraints, directly applicable to Odin's fraud/anomaly detection module. Its cost-benefit analysis informs Odin's design trade-offs between detection accuracy and system responsiveness. The hybrid layered pipeline concept can guide Odin's architecture to balance computational cost and user experience. The evaluation metrics (latency, throughput, cost) offer a template for assessing Odin's algorithmic modules."
  directly_justifies:
    - "XGBoost achieves high fraud detection accuracy with low latency, suitable for real-time screening."
    - "Deep learning models like LSTM and Transformer provide high accuracy but higher latency, suitable for secondary verification."
    - "Cost–benefit analysis reveals that reducing false positives and latency is economically beneficial."
    - "Hybrid pipelines can balance accuracy and operational efficiency in fraud detection."
  limits:
    - "Does not address Filipino cultural or demographic context."
    - "Relies on synthetic (PaySim) and anonymized (ULB) datasets, limiting generalizability to real-world banking systems."
    - "Does not explore privacy-preserving techniques like federated learning."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The anomaly detection domain (8.A, 8.B, 8.C) was flagged as high relevance because the paper directly benchmarks anomaly detection algorithms for financial transactions. The system evaluation domain (12.A, 12.B) was marked medium as the paper provides a comprehensive evaluation framework including latency, throughput, and cost. Classification approaches (5.C) were assigned low relevance because the paper applies classification to fraud, not specifically to financial behavioral profiles. Other domains—Filipino cultural context, expense categorization, existing systems, behavioral profiling (except 5.C), spending forecasting, budget recommendation, mobile-first design, data privacy, user retention, and savings/debt management—were considered but rejected for lacking direct citeable claims or relevance to Odin's core functions. Borderline cases: the paper touches on cost-sensitive classification and concept drift, which relate to 7.D (infeasibility) and 8.C, but we assigned only 8.C. Overall, the paper is highly relevant to Odin's anomaly detection module and offers actionable insights for real-time system evaluation."
limitations:
  - "Reliance on synthetic and anonymized datasets may limit external validity. [unacknowledged]"
  - "Does not cover all fraud typologies present in global banking. [unacknowledged]"
  - "Latency measurements may not fully capture production-grade network overhead."
  - "Cost estimates are based on hypothetical per-case values, not real banking data."
remember_this:
  - "XGBoost achieved ROC-AUC 0.9998 on PaySim with high throughput."
  - "LSTM processed 18,315 transactions per second on ULB."
  - "Model selection must balance accuracy, latency, and cost."
  - "Hybrid layered pipelines offer the best trade-off for real-time fraud detection."
```
---

## Paper 40: Kristiana et al_summarized.md

**Source File:** `Kristiana et al_summarized.md`

```yaml
paper_id: "10.1109/OJCS.2026.3658518"
designation: "international-algorithm-specific"
title: "Validating AI-Driven Nudge Recommendations: A/B Testing Two-Tower and Bandit Models in Simulated Digital Banking Environment"
authors: "Kristiana, I.; Prabowo, H.; Gaol, F. L.; Qomariyah, N. N."
year: 2026
venue: "IEEE Open Journal of the Computer Society"
odin_topics:
  - "5.A"
  - "5.C"
  - "6.A"
  - "7.B"
  - "7.D"
  - "8.C"
  - "9.A"
  - "10.A"
  - "11.B"
  - "12.B"
tldr: "A hybrid AI model combining Two-Tower Networks for static personalization and Multi-Armed Bandits for adaptive nudging significantly improved purchase and recommendation-following rates in a simulated digital banking A/B test."
problem_and_motivation: "Existing recommender systems in banking often fail due to data sparsity, cold-start issues, and a lack of behavioral awareness. There is a gap in integrating static personalization with real-time adaptive learning and explicit behavioral nudging. This study empirically validates a hybrid nudge recommendation model to improve user engagement and decision-making."
approach:
  - "A Two-Tower Network (TWN) was trained on baseline interaction data from 214 rule-based control users to generate static personalization scores."
  - "A Multi-Armed Bandit (MAB) algorithm used these scores as priors and dynamically adapted nudge selection based on simulated Gaussian rewards."
  - "The integrated model was evaluated in a simulated mobile banking environment with 174 treatment users."
  - "The treatment group's performance was compared against a rule-based control group and a TWN-only ablation baseline."
  - "Behavioral metrics included purchase conversion, recommendation-following rates, and alignment with the bandit's optimal arm."
findings:
  - "num: The AI-driven treatment group achieved a 62.07% purchase rate, up from 48.6% in the control."
  - "num: Recommendation-following behavior increased from 13.6% (control) to 52.87% (treatment)."
  - "num: 100% of recommendation-driven purchases in the treatment group aligned with the MAB's optimal arm."
  - "A chi-square test confirmed the behavioral shift was statistically significant (χ2 = 6.49, p < 0.0108)."
  - "The hybrid model combining TWN and MAB outperformed both rule-based and TWN-only baselines."
  - "Reward and regret analyses confirmed stable online learning and effective exploration-exploitation balance."
key_figures_tables:
  - "Figure 1: DSR methodology flow → Outlines the research framework from problem identification to evaluation."
  - "Figure 2: A/B testing research flow diagram → Shows the sequential control and treatment group deployment."
  - "Figure 3: Integrated architecture of the nudge recommendation model → Illustrates data flow from TWN to MAB and nudge deployment."
  - "Figure 4: Stability of event-level reward trajectories → Shows stable online learning under noisy feedback."
  - "Figure 5: Smoothed instant regret over rounds → Demonstrates bandit policy stays near the optimal nudge."
  - "Table 1: TWN configuration parameters → Details embedding dimensions and training setup."
  - "Table 2: A/B Testing Metrics for Control and Treatment Groups → Summarizes key behavioral outcomes."
key_equations:
  - equation: "$Q_{t+1}(a) = Q_t(a) + \\frac{1}{N_t(a)}(R_t - Q_t(a))$"
    explanation: "Updates value estimate for each product arm using incremental reward."
  - equation: "$a_t = \\begin{cases} \\arg\\max_a Q_t(a), & \\text{with probability } 1-\\epsilon \\\\ \\text{random arm}, & \\text{with probability } \\epsilon \\end{cases}$"
    explanation: "Epsilon-greedy policy for selecting product recommendations."
  - equation: "$\\text{Regret}_t = \\mu^* - \\mu_t$"
    explanation: "Measures the instantaneous loss from not selecting the optimal nudge."
definitions:
  - term: "Two-Tower Network (TWN)"
    definition: "A dual-encoder model generating personalized product relevance scores from user and item embeddings."
  - term: "Multi-Armed Bandit (MAB)"
    definition: "An online learning algorithm balancing exploration and exploitation to adaptively select actions."
  - term: "Nudge"
    definition: "A subtle change in choice architecture that steers behavior while preserving freedom of choice."
  - term: "A/B Testing"
    definition: "A controlled experiment comparing two versions of a system to measure the impact of a change."
  - term: "Regret"
    definition: "The cumulative loss in reward from not always choosing the optimal action."
critical_citations:
  - "[Jesse & Jannach, 2021] — Survey on digital nudging with recommenders."
  - "[Kristiana et al., 2025] — Foundation work on TWN+MAB integration for nudge optimization."
  - "[Thaler & Sunstein, 2008] — Seminal work on nudge theory."
  - "[Cossatin et al., 2024] — Application of digital nudging in recommender systems."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "The model explicitly profiles users via 54-item behavioral instrument for personalization."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "Uses user embeddings and behavioral data to classify financial behavior."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "The TWN predicts product relevance scores based on user and item features."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Provides framework for recommending products and nudges, informing budget allocation decisions."
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "contextual"
      justification: "The adaptive bandit layer handles uncertainty, similar to infeasibility in constraint satisfaction."
    - code: "8.C"
      name: "Cold-Start Baseline Strategies for Anomaly Detection"
      relevance: "high"
      justification: "The TWN provides a baseline for cold-start using static personalization before online adaptation."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "low"
      justification: "The experiment uses a mobile banking simulator, supporting mobile-first research."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "contextual"
      justification: "Paper mentions data privacy and security as concerns for future deployment."
    - code: "11.B"
      name: "Retention Mechanisms and Engagement Design"
      relevance: "medium"
      justification: "Demonstrates that adaptive nudging improves user engagement and responsiveness."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Employs rigorous A/B testing to evaluate the algorithmic recommendation modules."
  contribution: "This paper provides a validated architecture integrating a Two-Tower Network for static personalization and a Multi-Armed Bandit for adaptive behavioral nudging, directly informing Odin's recommendation and anomaly detection modules. The A/B testing methodology offers a blueprint for evaluating predictive algorithms, and the findings on recommendation-following behavior justify user-adaptive engagement strategies. The study's focus on cold-start mitigation via TWN is directly applicable to Odin's profile classification and forecasting systems. The demonstrated behavioral influence supports the design of Odin's budget recommendation and anomaly alert systems."
  directly_justifies:
    - "Hybrid TWN+MAB models are effective for personalized, adaptive recommendation in digital banking."
    - "A/B testing in simulated environments can validate the causal impact of AI-driven nudging interventions."
    - "Adaptive nudging can increase recommendation-following behavior by over four times compared to static rules."
    - "Statistical tests confirm significant behavioral improvements attributable to AI-driven personalization."
  limits:
    - "Simulated environment lacks real financial consequences and long-term behavioral data."
    - "Sequential quasi-experimental design cannot fully control for time-period effects."
    - "Generalizability limited by medium-sized dataset and domain-specific training corpus."
    - "Potential ethical concerns regarding fairness and user autonomy were not fully addressed in deployment."
  mapping_rationale: "All 12 functional domains and their associated topic codes were systematically scanned. The paper was flagged as highly relevant for Behavioral Profiling (5.A, 5.C), Forecasting (6.A), and Evaluation (12.B) due to its focus on user embeddings, predictive scoring, and A/B testing. Medium relevance was assigned to Budget Recommendation (7.B) and Retention (11.B) as the nudge mechanism directly influences user choices and engagement. Contextual relevance was noted for Infeasibility Handling (7.D) and Data Privacy (10.A) where the adaptive layer's behavior relates to constraint handling and mentions of future ethical concerns. The paper's focus on mobile simulation gave low relevance to Mobile-First Design (9.A). Domains like Expense Categorization (3.A-C) and Existing Systems (4.A-B) were rejected as the paper does not address these topics. Overall, the paper provides strong validation for adaptive personalization algorithms central to Odin's core functionality."
limitations:
  - "Experiments conducted in a simulated digital banking environment, not a live production setting with real monetary consequences."
  - "Model trained on a medium-sized, domain-specific corpus, limiting generalizability to underrepresented demographic groups."
  - "The A/B testing used non-overlapping deployment windows, introducing potential time-based confounds."
  - "Ethical implications of personalized nudging, such as fairness and user autonomy, were not thoroughly addressed [unacknowledged]."
  - "Recommendation-following behavior does not necessarily imply long-term preference stabilization or sustained engagement [unacknowledged]."
remember_this:
  - "Hybrid TWN+MAB model increased purchase rates from 48.6% to 62.07% in A/B test."
  - "Recommendation-following rate grew over fourfold from 13.6% to 52.87% under AI nudging."
  - "100% of recommendation-driven purchases aligned with the MAB optimal arm."
  - "Adaptive nudging significantly improves user behavioral response compared to static rules."
  - "Statistical validation confirms causal impact of AI-driven personalization on user decisions."
```
---

## Paper 41: Chahar et al_summarized.md

**Source File:** `Chahar et al_summarized.md`

```yaml
paper_id: 10.2139/ssrn.6377518
designation: "international-algorithm-specific"
title: "Artificial Intelligence Powered Personal Finance Management System"
authors: "Chahar, P.; Vishwakarma, Y. K.; Mishra, R.; Paliwal, G."
year: 2026
venue: "Unknown"
odin_topics:
  - "3.A"
  - "4.A"
  - "4.B"
  - "6.A"
  - "7.A"
  - "7.B"
  - "8.A"
  - "10.A"
  - "10.B"
  - "13.A"
tldr: "Proposes an AI-powered PFMS using ML and NLP for dynamic budget recommendations, financial education, and secure data handling to address limitations of static tools."
problem_and_motivation: "Individuals face challenges managing complex finances due to limited literacy and inadequate static budgeting tools. Existing systems lack adaptability, personalization, and predictive capabilities. There is a pressing need for intelligent, automated systems that can provide dynamic and personalized financial insights."
approach:
  - "Conducted a systematic literature review of existing PFMS, ML classification, predictive forecasting, and recommendation systems."
  - "Proposed a modular architecture with components for data collection, expense classification, predictive analytics, recommendations, and NLP interface."
  - "Designed a web-based prototype using React.js for frontend, Flask for backend ML operations, MongoDB for database, and Firebase for authentication."
  - "Evaluated the prototype's performance using metrics like accuracy, precision, MAE, and F1-score, alongside user satisfaction surveys."
  - "The expense classification engine employs supervised ML (Random Forest, SVM, LSTM) and uses techniques like TF-IDF and word embeddings."
findings:
  - "num: The system achieved high user satisfaction with a rating of 4.4/5 overall."
  - "num: Convenience of use received an average score of 4.5/5."
  - "num: Correctness of transaction categorization was rated at 4.2/5."
  - "num: Goal-setting functionality was rated at 4.3/5."
  - "The system effectively categorized transactions and provided relevant financial advice for users with stable incomes."
  - "Recorded data quality, especially incomplete or inaccurate transactions, negatively impacted the reliability of predictions and recommendations."
key_figures_tables:
  - "Figure 4: Data flow diagram shows the system architecture from data input to report generation."
  - "Figure 6: Distribution of Expenses across Transaction Types illustrates the categorization of spending."
  - "Table 1: Summary of AI-powered finance management tools like Mint, YNAB, Digit, and Tally."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "NLP"
    definition: "Natural Language Processing, used for user interaction via chatbots."
  - term: "LSTM"
    definition: "Long Short-Term Memory, a deep learning network for sequential text analysis."
  - term: "ML"
    definition: "Machine Learning, used for classification, forecasting, and personalization."
  - term: "PFMS"
    definition: "Personal Finance Management System."
critical_citations:
  - "[Zhang et al., 2007] — Used decision trees and SVM for transaction classification."
  - "[Siami-Namini et al., 2018] — Compared ARIMA and LSTM for forecasting spending patterns."
  - "[Luef et al., 2020] — Developed a recommender system for financial advice."
relevance:
  topics:
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "high"
      justification: "Paper details an ML-based expense classification engine using models like Random Forest and SVM."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews existing tools (Mint, YNAB) and their limitations, establishing context for the proposed system."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Directly addresses limitations of static, rule-based systems and the lack of personalization and adaptability."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Proposes a predictive analytics module using time series forecasting (ARIMA, LSTM) for proactive planning."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "medium"
      justification: "Discusses personal budgeting as a critical financial process and mentions strategies for budget adherence."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "high"
      justification: "System includes a recommendation module to generate personalized budgeting tips and advice."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Mentions anomaly detection for fraud and identity theft as a potential system capability."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "Dedicates a whole component to security measures, including encryption, anonymization, and compliance."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "medium"
      justification: "Identifies user trust as a key challenge for adoption and suggests explainability to build it."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "medium"
      justification: "The system's expected outcomes include helping users create budgets that facilitate saving."
  contribution: "This paper provides a high-level blueprint for an AI-driven PFMS that can justify Odin's modular design, specifically for modules like expense classification (Topic 3.A) and budget recommendation (Topic 7.B). Its systematic review of existing system limitations (Topic 4.B) directly supports the rationale for developing a more intelligent and adaptive solution. The emphasis on security and user trust (Topics 10.A, 10.B) validates Odin's commitment to data privacy as a core functional requirement. Furthermore, the positive user satisfaction metrics reported provide a benchmark for evaluating the success of a new PFMS. The paper's approach of combining ML, NLP, and a robust web framework offers a viable architecture for Odin's own implementation."
  directly_justifies:
    - "The proposed AI-powered assistant can deliver dynamic, user-specific financial insights."
    - "Integrating ML for expense classification and forecasting enhances financial management tools."
    - "Incorporating robust security mechanisms is essential for protecting sensitive user data."
    - "Personalized recommendations help users achieve financial goals and improve engagement."
  limits:
    - "The paper presents a proposal and preliminary prototype, lacking empirical validation of its core algorithms in a real-world setting."
    - "The proposed system's ability to handle irregular income streams is acknowledged as a limitation."
    - "Findings rely on a literature review and high-level architecture; detailed algorithmic performance data is absent."
  mapping_rationale: "A systematic scan across all 12 functional domains was performed. The paper was flagged as highly relevant to 'Existing Systems & Gaps' (4.A, 4.B) and 'Budget Recommendation' (7.A, 7.B) due to its clear identification of static tool limitations and its proposal of a recommendation module. It also shows high relevance to 'Expense Categorization' (3.A) and 'Data Privacy' (10.A, 10.B) because it details ML classification techniques and a dedicated security layer. Medium relevance was assigned to 'Predictive Modeling' (6.A) and 'Savings Management' (13.A) as these are mentioned but not deeply explored. The paper touches on 'Anomaly Detection' (8.A) and 'User Trust' (10.B), but these are brief discussions, hence a 'medium' relevance. Other domains like 'Filipino Cultural Context,' 'Mobile-First Design,' and 'User Retention' were considered but rejected as the paper does not address them. The paper's overall relevance to Odin is strong as it provides a comprehensive justification for an AI-driven PFMS, covers several key modules, and highlights critical implementation concerns like privacy."
limitations:
  - "The proposed system is a prototype and lacks real-world deployment validation. [unacknowledged]"
  - "Difficulty in handling users with irregular income patterns. [acknowledged]"
  - "Data quality issues can lead to less reliable predictions."
  - "Reliance on user survey data for success metrics, which may not directly correlate with algorithmic performance."
remember_this:
  - "An AI-powered PFMS requires ML for classification and NLP for user interaction."
  - "Static financial tools lack adaptability and personalization for modern users."
  - "Security and user trust are critical for the adoption of AI in personal finance."
  - "The proposed system's high user satisfaction (4.4/5) highlights the value of usability."
  - "Challenges remain in handling irregular income and maintaining data quality."
```
---

## Paper 42: Claros et al_summarized.md

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

## Paper 43: Mienye et al-2026_summarized.md

**Source File:** `Mienye et al-2026_summarized.md`

```yaml
paper_id: "10.3390/info17040395"
designation: "international"
title: "Deep Learning for Credit Risk Prediction: A Survey of Methods, Applications, and Challenges"
authors: "Mienye, I. D.; Esenogho, E.; Modisane, C."
year: 2026
venue: "Information"
odin_topics:
  - "4.A"
  - "4.B"
  - "5.C"
  - "6.A"
  - "6.B"
  - "10.A"
  - "10.B"
tldr: "A systematic survey of deep learning architectures for credit risk prediction, covering MLP, CNN, RNN, Transformer, and GNN models across tabular, sequential, and relational borrower data."
problem_and_motivation: "Traditional credit risk models like logistic regression and tree-based ensembles struggle to capture nonlinearities, temporal dynamics, and relational dependencies in modern financial datasets. While deep learning offers a path forward, the review literature has lacked a unified synthesis that maps model families to data modalities and credit-risk objectives for borrower-level prediction."
approach:
  - "Searched IEEE Xplore, Scopus, ACM Digital Library, ScienceDirect, SpringerLink, Web of Science, and Google Scholar using credit-risk and deep learning keywords."
  - "Restricted to journal articles and conference papers from 2015 to 2025, with foundational earlier studies added via citation tracking."
  - "Screened 380 initial records through de-duplication, title/abstract screening, and full-text assessment to retain 140 application studies and 18 survey papers."
  - "Organised reviewed studies by model class: tabular MLP, sequential RNN/LSTM/GRU, CNN, Transformer, GNN, and hybrid architectures."
  - "Extracted data modality, architecture, credit product segment, prediction target, and evaluation metrics for each included study."
findings:
  - "num: MLPs with L1–L2 regularisation achieved 80.12% accuracy for corporate credit risk, outperforming logistic regression (AUC 0.717) and SVM (AUC 0.738)."
  - "num: LSTM networks reduced MAE from 0.095 to 0.072 and RMSE from 0.119 to 0.093 for monthly default rate forecasting versus ARIMA and SVM."
  - "num: TabNet-Stacking ensemble reached 97.9% accuracy and 0.941 AUC on a large-scale credit dataset with 800,000 cases."
  - "num: Residual-enhanced BiLSTM with multi-head attention achieved AUC 0.982 and F1 0.958 on the Freddie Mac Single-Family dataset."
  - "num: Weighted-loss TabTransformer increased accuracy on the German Credit dataset from 93% to 95% with SHAP-based explanations."
  - "num: Relational graph attention networks achieved AUC 0.799 and KS 0.528 for SME default prediction using shared-director and business-interaction graphs."
  - "Deep tabular models are competitive with tree-based ensembles on large datasets with high-cardinality categorical features but offer modest gains on small benchmarks."
  - "Sequential architectures like LSTM and GRU excel at dynamic behavioural scoring when rich post-origination histories are available."
  - "Transformers unify behavioural sequences, categorical embeddings, textual narratives, and graph-structured relationships within a single modelling interface."
  - "GNNs capture contagion and correlated risk in interconnected portfolios that tabular and sequential models cannot represent structurally."
key_figures_tables:
  - "Table 1: Summary of related reviews on credit risk modelling → Positions this survey as the first unified synthesis of DL model families for borrower-level credit risk."
  - "Figure 1: PRISMA flowchart of literature search and screening → Documents the systematic selection of 140 application studies and 18 survey papers."
  - "Figure 2: Basic structure of a feed-forward neural network for tabular credit data → Illustrates MLP architecture with hidden layers for default prediction."
  - "Figure 3: Architecture of the LSTM network showing gating mechanisms → Visualises forget, input, and output gates for long-term temporal pattern preservation."
  - "Figure 4: Architecture of the GRU network with update and reset gates → Shows simplified recurrent structure for efficient behavioural sequence modelling."
  - "Figure 5: Basic CNN architecture adapted for one-dimensional financial sequences → Depicts convolutional and pooling layers for local repayment pattern extraction."
  - "Figure 6: Message passing mechanism in a GNN for borrower networks → Illustrates neighbour aggregation for relational credit risk propagation."
  - "Table 2: Summary of benchmark datasets commonly used in credit risk prediction → Lists German Credit, Australian Credit, Taiwan Credit Card Default, Home Credit, and LendingClub datasets."
  - "Table 3: Summary of deep learning architectures for credit risk modelling → Compares MLP, CNN, RNN, Transformer, GNN, and hybrid models by mechanism, strengths, and limitations."
  - "Table 4: Summary of deep learning applications in credit risk prediction → Consolidates 25 peer-reviewed studies across tabular, sequential, transformer-based, and GNN-based models."
  - "Table 5: Challenges in deep learning credit risk modelling and aligned research directions → Maps evaluation integrity, imbalance, interpretability, robustness, and governance issues to emerging research directions."
key_equations:
  - equation: "EL = PD × LGD × EAD"
    explanation: "Expected loss decomposes into probability of default, loss given default, and exposure at default."
  - equation: "P(y=1|x) = σ(w^T x + b) = 1/(1 + exp(-w^T x - b))"
    explanation: "Logistic regression models default probability as a linear log-odds function."
  - equation: "h_t = ϕ(W h_{t-1} + U x_t + b)"
    explanation: "RNN hidden state update with nonlinear activation over sequential input."
  - equation: "f_t = σ(W_f [h_{t-1}, x_t] + b_f), i_t = σ(W_i [h_{t-1}, x_t] + b_i), C_t = f_t ⊙ C_{t-1} + i_t ⊙ C̃_t"
    explanation: "LSTM forget and input gates regulate memory cell updates for long-term dependencies."
  - equation: "Attention(Q,K,V) = softmax(QK^T / √d_k) V"
    explanation: "Scaled dot-product attention enables global dependency modelling across sequences or features."
  - equation: "h_v^{(l+1)} = σ(∑_{u∈N(v)} 1/c_{vu} W^{(l)} h_u^{(l)})"
    explanation: "GNN message passing updates borrower embeddings by aggregating neighbour representations."
definitions:
  - term: "AUC"
    definition: "Area under the receiver operating characteristic curve, a threshold-agnostic measure of ranking performance."
  - term: "AUPRC"
    definition: "Area under the precision-recall curve, sensitive to minority-class performance in imbalanced datasets."
  - term: "BiLSTM"
    definition: "Bidirectional long short-term memory network that processes sequences in both forward and backward directions."
  - term: "CNN"
    definition: "Convolutional neural network using shared-weight filters to extract local temporal or spatial patterns."
  - term: "DL"
    definition: "Deep learning, a subfield of machine learning using multi-layered neural networks for representation learning."
  - term: "EAD"
    definition: "Exposure at default, the total outstanding amount a lender is exposed to when default occurs."
  - term: "EL"
    definition: "Expected loss, the product of PD, LGD, and EAD used in regulatory capital calculations."
  - term: "GNN"
    definition: "Graph neural network, a model that learns representations by message passing over graph-structured relational data."
  - term: "GRU"
    definition: "Gated recurrent unit, a simplified recurrent architecture with update and reset gates for sequence modelling."
  - term: "LGD"
    definition: "Loss given default, the proportion of exposure not recovered after a borrower defaults."
  - term: "LR"
    definition: "Logistic regression, a linear model for binary classification with a sigmoid output."
  - term: "LSTM"
    definition: "Long short-term memory, a recurrent network with gating mechanisms for preserving long-range temporal dependencies."
  - term: "ML"
    definition: "Machine learning, algorithms that learn patterns from data without explicit programming."
  - term: "MLP"
    definition: "Multi-layer perceptron, a feed-forward neural network with multiple hidden layers and nonlinear activations."
  - term: "MLOps"
    definition: "Machine learning operations, practices for versioning, monitoring, and governing ML models in production."
  - term: "PD"
    definition: "Probability of default, the likelihood that a borrower fails to meet repayment obligations."
  - term: "RNN"
    definition: "Recurrent neural network, a model with cyclic connections for processing sequential data."
  - term: "RWA"
    definition: "Risk-weighted asset, a measure of asset risk used in Basel regulatory capital requirements."
  - term: "SHAP"
    definition: "SHapley Additive exPlanations, a game-theoretic approach for interpreting model predictions."
  - term: "SME"
    definition: "Small and medium enterprise, a business segment frequently targeted in credit risk studies."
  - term: "TCN"
    definition: "Temporal convolutional network, a dilated convolutional architecture for sequence modelling with parallel computation."
  - term: "XAI"
    definition: "Explainable artificial intelligence, methods for making model decisions interpretable to humans."
critical_citations:
  - "[LeCun et al., 2015] — Foundational paper establishing deep learning as a transformative approach."
  - "[Vaswani et al., 2017] — Introduced the Transformer architecture with self-attention for sequence modelling."
  - "[Lessmann et al., 2015] — Benchmarking study highlighting limitations of small public credit datasets."
  - "[Thomas et al., 2017] — Comprehensive text on credit scoring and probability of default modelling."
  - "[Rudin, 2019] — Argues for interpretable models over black-box explanations in high-stakes decisions."
  - "[Hardt et al., 2016] — Established equalised odds as a fairness criterion for supervised learning."
  - "[Bergmeir and Benítez, 2012] — Critical analysis of cross-validation for time-series evaluation."
relevance:
  topics:
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Reviews the broader credit risk modelling landscape but not PFMS specifically."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "contextual"
      justification: "Discusses limitations of statistical and ML credit models that parallel gaps in PFMS."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "low"
      justification: "Covers classification methods for credit scoring that could inform user profiling in Odin."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Provides a comprehensive review of DL predictive models applicable to spending and risk forecasting."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "medium"
      justification: "Reviews LSTM, GRU, and TCN architectures for behavioural sequence forecasting."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "low"
      justification: "Discusses differential privacy and federated learning as deployment considerations."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "low"
      justification: "Addresses interpretability, fairness, and governance as trust-enabling factors."
  contribution: "This paper surveys deep learning architectures that can inform Odin's predictive modules, particularly spending forecasting and user behavioural classification. The synthesis of sequential models provides methodological grounding for Odin's 6.A and 6.B forecasting components. The critical assessment of evaluation integrity, including out-of-time validation and calibration-aware reporting, guides how Odin's algorithmic modules should be assessed. The discussion of privacy-preserving techniques and interpretability frameworks supports Odin's data privacy and user trust design principles. The taxonomy linking model families to data structures offers a conceptual map for selecting appropriate techniques for Odin's heterogeneous user data."
  directly_justifies:
    - "LSTM and GRU networks outperform static classifiers for behavioural sequence forecasting when rich post-origination histories are available."
    - "Out-of-time validation is essential to avoid temporal leakage and obtain faithful deployment performance estimates."
    - "Calibration-aware reporting using Brier score and expected calibration error should accompany AUC-based evaluation."
    - "Tabular deep models with attention mechanisms improve discrimination on high-cardinality categorical features."
    - "GNNs capture relational dependencies in interconnected financial networks that tabular models cannot represent."
  limits:
    - "Survey focuses on credit risk prediction in lending, not on personal finance management or spending behaviour."
    - "Reviewed studies rely heavily on small public benchmarks that understate uncertainty and overestimate generalisability."
    - "Interpretability and fairness are discussed as challenges but few reviewed studies implement fairness-aware training objectives."
    - "Privacy-preserving techniques like differential privacy are mentioned but not empirically evaluated in the covered credit risk studies."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The following domains were flagged as relevant: Existing Systems & Gaps (4.A, 4.B) as contextual because the paper reviews the credit risk modelling landscape and its limitations, though not PFMS specifically. Behavioral Profiling & Classification (5.C) as low because the classification approaches for credit scoring have methodological overlap with user profiling. Spending Forecasting (6.A, 6.B) as medium because the paper provides a comprehensive review of predictive models and sequential forecasting algorithms directly applicable to Odin's forecasting modules. Data Privacy & User Trust (10.A, 10.B) as low because privacy and interpretability are discussed as deployment challenges but are not central to the survey. The following domains were considered and rejected: Filipino Cultural Context (no Philippine or cultural content), Expense Categorization (no expense taxonomy), Budget Recommendation (no budget allocation methods), Anomaly Detection (only passing mention), Mobile-First Design (not addressed), User Retention & Engagement (not addressed), System Evaluation (evaluation is for credit risk, not PFMS), Savings & Debt Management (credit default is tangentially related to debt but the paper does not address debt management strategies). The paper's overall relevance to Odin is methodological rather than domain-specific, providing techniques and evaluation principles that can inform Odin's predictive modules and design choices."
limitations:
  - "The survey relies on English-language peer-reviewed studies indexed in major databases, excluding proprietary implementations and regulatory grey literature. [unacknowledged]"
  - "Performance comparisons across studies are not standardised due to heterogeneous datasets, targets, and evaluation horizons. [unacknowledged]"
  - "No formal risk-of-bias scoring protocol was applied, limiting the ability to assess study quality systematically. [unacknowledged]"
  - "The survey focuses on borrower-level credit risk and does not cover market risk, liquidity risk, or portfolio optimisation without borrower-level labels."
  - "Small public benchmarks dominate the reviewed studies, limiting generalisability to real-world portfolios with macroeconomic dynamics."
remember_this:
  - "LSTM and GRU networks excel at behavioural sequence forecasting for dynamic credit scoring."
  - "Out-of-time validation avoids temporal leakage and yields more faithful performance estimates."
  - "Deep tabular models with attention compete with tree ensembles on large, high-cardinality datasets."
  - "GNNs capture relational risk propagation in interconnected borrower networks."
  - "Calibration-aware evaluation using Brier score should accompany AUC-based reporting."
```
---

## Paper 44: Moury_summarized.md

**Source File:** `Moury_summarized.md`

```yaml
paper_id: 10.63125/0nbg6w69
designation: international
title: Machine Learning–Based Transaction Risk Scoring Models for Financial Compliance Monitoring in Foreign Exchange Operations
authors: Moury, R. K.
year: 2026
venue: International Journal of Scientific Interdisciplinary Research
odin_topics:
  - 6.B
  - 7.B
  - 8.B
  - 12.A
  - 12.B
  - 10.A
  - 9.A
tldr: A quantitative synthesis of 124 ML-based FX risk scoring models shows ensemble methods most common but governance and calibration reporting are underdeveloped.
problem_and_motivation: The FX compliance monitoring literature is fragmented, with inconsistent labeling, validation, and governance reporting. This heterogeneity limits cross-study comparison and operational interpretability. A systematic synthesis is needed to quantify methodological patterns and gaps.
approach:
  - Conducted a systematic quantitative review of 89 publications yielding 124 analytic records on FX transaction risk scoring models.
  - Developed a structured extraction protocol to code model family, feature groups, validation design, metrics, and governance controls.
  - Computed descriptive prevalence statistics and reliability indices for governance and documentation completeness.
  - Applied logistic regression to identify predictors of high predictive performance reporting.
  - Used linear regression to examine associations with governance maturity scores.
findings:
  - num: Ensemble models appeared in 44.4% of records, logistic/GLM in 37.1%, decision trees in 33.9%, neural in 29.8%, and unsupervised in 26.6%.
  - num: Customer-profile variables (69.4%) and geographic corridor indicators (62.1%) were the most common feature groups.
  - num: Discrimination metrics were reported in 82.3% of records, but calibration metrics appeared in only 34.7%.
  - num: Out-of-time validation (OR = 2.83, p = 0.004) and ensemble models (OR = 2.27, p = 0.008) were significantly associated with high performance reporting.
  - num: Governance controls were documented in fewer than one-third of records, but operational studies showed significantly higher governance maturity (β = 1.12, p < 0.001).
  - num: Network feature usage was associated with higher performance reporting (φ = 0.22, p = 0.015).
  - Governance and auditability constructs were underreported, with traceability artifacts in only 22.6% of records.
  - Labeling heterogeneity was substantial, with SAR-derived labels most common (46.8%) but confidence stratification underutilized.
  - Calibration and cost-sensitive evaluation were among the least reported evaluation constructs.
  - The Evidence Quality Index was positively associated with both performance reporting and governance maturity.
key_figures_tables:
  - Table 1: Publication characteristics show 68.5% of records are from 2018–2023 → recent research concentration.
  - Table 2: Model family prevalence shows ensemble methods most frequent at 44.4% → dominance of ensemble learning.
  - Table 3: Feature usage shows customer profile (69.4%) and corridor (62.1%) as most common → domain features prioritized.
  - Table 4: Evaluation metrics show discrimination (82.3%) but calibration (34.7%) and cost-sensitive (28.2%) less reported → evaluation imbalance.
  - Table 7: Logistic regression shows out-of-time validation (OR=2.83) strongest predictor of high performance → temporal rigor matters.
  - Table 8: Operational study type (β=1.12) and logging coverage (β=1.27) predict governance maturity → deployment drives governance.
  - Figure 12: FX Compliance Risk Scoring Evidence summary → comprehensive visual of key findings.
key_equations:
  - equation: "OR = 2.27, p = 0.008"
    explanation: Ensemble models significantly increase odds of high performance reporting.
  - equation: "β = 1.12, p < 0.001"
    explanation: Operational studies strongly predict higher governance maturity scores.
definitions:
  - term: "FX"
    definition: "Foreign exchange operations, currency trading and settlement."
  - term: "GLM"
    definition: "Generalized linear models, a statistical modeling framework."
  - term: "SAR"
    definition: "Suspicious activity report, a formal compliance alert."
  - term: "ROC"
    definition: "Receiver operating characteristic, a performance evaluation curve."
critical_citations:
  - "[Leo et al., 2019] — Framed ML risk scoring as decision support in banking."
  - "[Jullum et al., 2020] — Addressed label uncertainty and temporal validation."
  - "[Kaur et al., 2018] — Emphasized ranking for capacity-constrained monitoring."
  - "[Bhatore et al., 2020] — Reviewed ML credit risk evaluation in finance."
relevance:
  topics:
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Directly synthesizes forecasting model performance across 124 records.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Risk scoring prioritization methods analogous to budget alert ranking.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Unsupervised and semi-supervised anomaly detection approaches reviewed.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Comprehensive evaluation of metrics including discrimination and calibration.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Compares model families and validation designs systematically.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Mentions data quality and schema harmonization but not privacy directly.
    - code: 9.A
      name: Mobile‑First Design Principles and Rationale
      relevance: contextual
      justification: Discusses latency and throughput for real-time systems relevant to mobile.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: low
      justification: Focus on risk scoring evaluation, not budget recommendations specifically.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Classification of transactions, not user behavioral profiles.
  contribution: This paper provides quantitative benchmarks for model selection, feature engineering, and validation rigor that directly inform Odin's algorithmic design. It establishes that ensemble methods and temporally separated validation are associated with stronger performance, guiding Odin's forecasting module. The underreporting of calibration and governance highlights areas where Odin can differentiate itself through transparent evaluation. The emphasis on ranking metrics aligns with Odin's need to prioritize alerts for young professionals with limited review capacity. Findings on feature importance (customer profile, temporal aggregation) validate Odin's planned feature engineering priorities.
  directly_justifies:
    - Ensemble models are significantly associated with higher predictive performance in financial monitoring.
    - Out-of-time validation is a strong predictor of robust model performance.
    - Calibration metrics are rarely reported, indicating a gap in probability reliability evaluation.
    - Governance instrumentation is more common in operational deployments than in experimental studies.
    - Network features, when used, are linked to stronger performance outcomes.
    - Feature engineering choices may be more influential than model family selection alone.
  limits:
    - The sample is skewed toward experimental benchmarking with proprietary datasets.
    - Governance indices measure documented controls, not verified operational implementation.
    - Publication bias may inflate the prevalence of reported high-performance outcomes.
    - Calibration and cost-sensitive reporting were too sparse for robust subgroup analysis.
    - Availability-focused threat modeling was untestable due to structural missingness.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was executed. The paper was flagged as highly relevant to forecasting algorithms (6.B) and anomaly detection (8.B) due to its comprehensive meta-analysis of model families for transaction risk prediction. It also strongly informs evaluation frameworks (12.A) and algorithmic evaluation (12.B) by quantifying metric prevalence and validation rigor. Medium relevance was assigned to budget recommendation (7.B) as the prioritization methods are analogous to ranking alerts for young professionals. Contextual relevance was noted for data privacy (10.A) and mobile design (9.A) because the paper discusses data quality and real-time latency constraints, though not as primary focuses. Low relevance was assigned to behavioral profiling topics (5.C) and evaluation methodologies for budgets (12.C) as the paper focuses on transaction classification, not user profiles or budget-specific recommendation. The systematic scan confirmed that governance and calibration constructs were underreported, which is a key gap the paper highlights.
limitations:
  - Reliance on explicitly reported information; many studies lacked complete descriptions of labeling and preprocessing.
  - Performance measures were not uniformly comparable across studies due to different datasets and labeling standards. [unacknowledged]
  - Multiple configurations from the same publication may introduce residual correlation despite clustering adjustments.
  - Construct validity constrained by infrequent reporting of operational disruption and supervisory review outcomes. [unacknowledged]
  - Evidence base skewed toward experimental studies and proprietary datasets, limiting generalizability. [unacknowledged]
  - Publication bias may inflate the prevalence of high-performance outcomes. [unacknowledged]
  - Governance indices measured declared practices, not verified operational implementation.
remember_this:
  - Ensemble models were the most frequently evaluated approach at 44.4%.
  - Out-of-time validation was the strongest predictor of high performance reporting.
  - Calibration metrics appeared in only 34.7% of records.
  - Operational studies showed significantly higher governance maturity scores.
  - Network feature usage was associated with stronger performance outcomes.
```
---

## Paper 45: Miranda et al_summarized.md

**Source File:** `Miranda et al_summarized.md`

```yaml
paper_id: 10.48550/arXiv.2604.11290
designation: international-algorithm-specific
title: "Polyglot Teachers: Evaluating Language Models for Multilingual Synthetic Data Generation"
authors: "Miranda, L. J. V.; Vulic, I.; Korhonen, A."
year: 2026
venue: "Unknown"
odin_topics:
  - 5.C
  - 6.B
  - 7.D
  - 8.B
  - 12.B
  - 12.C
  - 2.A
  - 2.D
tldr: A systematic evaluation of language models as multilingual teachers for synthetic data generation reveals that model scale is less important than data quality metrics for student performance.
problem_and_motivation: Selecting teacher models for multilingual synthetic data generation is often ad hoc, defaulting to the largest models which may have capability gaps in non-English languages. This practice can produce poor-quality synthetic data, creating a need for a systematic way to measure teacher effectiveness.
approach:
  - Evaluated 10 teacher LMs across 6 typologically diverse languages by generating over 1.4M SFT examples.
  - Proposed POLYGLOT SCORE, a metric combining intrinsic data quality and extrinsic student model performance.
  - Measured intrinsic quality via prompt/response diversity, response perplexity, and a multilingual reward model score.
  - Assessed extrinsic performance by finetuning an OLMo 3 7B student model and evaluating on multilingual benchmarks.
  - Analyzed correlations between teacher model properties and data quality to identify factors driving effectiveness.
findings:
  - "num: Gemma 3 27B and Aya Expanse 32B are the most effective teachers, with PG-SCOREs of 0.726 and 0.706, respectively."
  - "num: Model scale does not significantly predict teacher effectiveness (p=0.507)."
  - "num: Data quality metrics (prompt diversity, length, response fluency) capture over 93.3% of variance in intrinsic quality."
  - "num: A linear model using principal components of intrinsic metrics predicts student performance with R2=0.664."
  - "num: Matching teacher-student model families yields at least a 20.5% increase in PG-SCORE."
  - For high-resource languages like German, the Generate method works best; for less-resourced languages, Respond or Translate methods are more effective.
  - Teacher performance varies significantly by language, likely due to pretraining data representation.
  - Teachers from the Gemma family consistently outperform others, including larger models from the Llama family.
key_figures_tables:
  - "Figure 1: Overview of POLYGLOT SCORE evaluation pipeline. → Pipeline combines intrinsic data quality and extrinsic student performance to assess teachers."
  - "Table 1: PG-SCORE of teacher models across 6 languages. → Gemma 3 27B and Aya Expanse 32B are top performers, regardless of size."
  - "Table 3: Regression results show model size and benchmark performance do not significantly predict PG-SCORE. → Common assumptions about teacher strength are insufficient."
  - "Figure 4: Linear regression of intrinsic PCs to predict extrinsic student performance. → Intrinsic data quality metrics are strong predictors of downstream performance."
key_equations:
  - equation: "PG-SCORET,ℓ = z-score(Intr.T,ℓ + Extr.T,ℓ)"
    explanation: "Combines intrinsic and extrinsic metrics into a single teacher effectiveness score."
  - equation: "Intr.T,ℓ = 1/|M| ∑_{m∈M} z-score(m(DT,ℓ))"
    explanation: "Averages normalized intrinsic quality metrics for a teacher on a language."
  - equation: "Extr.T,ℓ = 1/|B| ∑_{b∈B} (score_b(ST,ℓ) − score_b(Sϕ)) / (score_b(SREF) − score_b(Sϕ))"
    explanation: "Performance gain recovered by the student over a reference model."
definitions:
  - term: "POLYGLOT SCORE (PG-SCORE)"
    definition: "A metric to holistically assess a teacher model's effectiveness for multilingual synthetic data generation, combining intrinsic data quality and extrinsic student model performance."
  - term: "SFT"
    definition: "Supervised Fine-Tuning, a standard approach for adapting language models to specific tasks or languages."
  - term: "PGR"
    definition: "Performance Gap Recovered, a metric measuring the improvement of a finetuned student model over a base model relative to a reference."
  - term: "LLM-as-a-judge"
    definition: "Using a large language model to evaluate the quality of generated text based on a given rubric."
  - term: "CommonCrawl representation"
    definition: "The proportion of a language in the CommonCrawl dataset, used as a proxy for a language's presence in pretraining data."
critical_citations:
  - "[Kim et al., 2025] — Found model scale doesn't predict teacher effectiveness for English-based tasks."
  - "[Xu et al., 2025b] — Showed stronger models are not always better teachers for instruction tuning."
  - "[Pombal et al., 2025] — Introduced M-Prometheus, a strong multilingual reward model."
relevance:
  topics:
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "contextual"
      justification: "The paper's methodology of evaluating teacher models is analogous to selecting a model to generate training data for behavioral profile classification."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "The paper's evaluation framework for synthetic data generation can be directly adapted to select models for generating training data for spending forecasting modules."
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "medium"
      justification: "The principles of selecting effective 'teachers' for data generation can be applied to selecting models for generating training data for infeasibility handling in budget recommendations."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "The systematic approach to evaluating data generation quality is directly relevant for selecting teacher models to generate synthetic anomaly data for training detection algorithms."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "This paper provides a comprehensive evaluation framework (PG-SCORE) for algorithmic modules (teacher models) in a data generation pipeline."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "high"
      justification: "The structured, multi-metric evaluation methodology (intrinsic + extrinsic) can inform the design of evaluation frameworks for budget recommendation systems."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "contextual"
      justification: "The paper emphasizes the importance of cultural appropriateness in generated data, which is relevant to capturing culturally specific financial practices."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "contextual"
      justification: "The case study on Tagalog and the focus on cultural appropriateness in data generation are relevant to modeling Filipino-specific spending cycles."
  contribution: "This paper offers a systematic, data-centric approach to evaluating LMs as teachers, directly applicable to Odin's data generation needs for multiple modules. The POLYGLOT SCORE framework provides a blueprint for evaluating and selecting models for generating synthetic training data for forecasting, anomaly detection, and budget recommendation. Its finding that data quality metrics are more predictive than model scale offers a practical, cost-effective strategy for building these modules. The demonstrated effectiveness of model family matching provides a concrete heuristic for teacher selection. The case study on Tagalog validates the approach for a new language, suggesting adaptability to low-resource contexts."
  directly_justifies:
    - "The POLYGLOT SCORE framework offers a structured method to evaluate models for generating synthetic data."
    - "Model scale alone does not guarantee data generation quality, so small models can be effective."
    - "Data quality metrics such as prompt diversity and response fluency are predictive of student model performance."
    - "Matching teacher and student model families is a reliable heuristic for improving performance."
    - "For less-resourced languages, generating responses to existing prompts is more effective than few-shot generation."
  limits:
    - "The study evaluates only six languages, which limits the generalizability of findings to the full diversity of Odin's potential user base."
    - "The Translate method assumes access to English prompts that are meaningful for the target language, which may not always hold."
    - "The evaluation focuses on general-purpose benchmarks, not on financial or PFMS-specific tasks."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains of Spending Forecasting (6), Budget Recommendation (7), Anomaly Detection (8), and System Evaluation (12) were flagged as highly relevant due to the paper's direct contribution to selecting models for generating training data for these algorithmic modules. The domain of Behavioral Profiling & Classification (5) was assigned 'contextual' relevance as the methodology could be adapted. The domains of Filipino Cultural Context (2) were also marked 'contextual' due to the paper's focus on cultural appropriateness in data generation, which is relevant to modeling specific financial behaviors. The domains of Expense Categorization (3), Existing Systems (4), Mobile-First Design (9), Data Privacy (10), User Retention (11), and Savings & Debt Management (13) were considered but rejected as the paper does not provide citeable claims for these specific Odin domains. The paper's primary contribution is its evaluation framework and findings on synthetic data generation, which directly informs the development of data-centric algorithmic modules in Odin."
limitations:
  - "Language set limited to six typologically diverse languages, representing a small sample of the world's languages."
  - "Assumes access to English prompts for the Translate method, which may not always be culturally appropriate."
  - "Relies on automatic evaluation metrics that may not fully capture the nuances of human language quality."
  - "The computational cost of evaluating all teacher models via student finetuning is high. [unacknowledged]"
  - "Does not explore the potential for bias amplification in synthetic data pipelines, especially for low-resource languages. [unacknowledged]"
remember_this:
  - "Gemma 3 27B is an effective multilingual teacher for synthetic data generation."
  - "Model scale does not predict teacher effectiveness in multilingual settings."
  - "Data quality, not model size, is the primary driver of student performance."
  - "Teacher-student model family matching yields significant performance gains."
  - "For less-resourced languages, the Respond or Translate methods are most effective."
```
---

## Paper 46: Athique & Lorenzana_summarized.md

**Source File:** `Athique & Lorenzana_summarized.md`

```yaml
paper_id: 10.1177/13678779251348945
designation: international
title: Abot kamay: Embedding digital transactions in the Philippines
authors: Athique, A.; Lorenzana, J. A.
year: 2026
venue: International Journal of Cultural Studies
odin_topics:
  - 2.A
  - 2.D
  - 3.A
  - 4.A
  - 4.B
  - 9.A
  - 10.A
  - 10.B
  - 11.A
  - 11.B
tldr: Digital transaction platforms in the Philippines become embedded through culturally specific practices of reciprocity, redistribution, and remuneration, particularly via the idiom of abot kamay.
problem_and_motivation: The digitalization of financial systems in the Global South is often analyzed through a purely functional lens, neglecting the cultural and social meanings of exchange. Understanding how digital platforms interact with established cultural norms is crucial for assessing their impact, yet this perspective is frequently missing from policy and industry literature.
approach:
  - An ethnographic study was conducted in Metro Manila across three socio-economically distinct communities: Santa Mesa, Payatas, and Quezon City.
  - The research employed focus groups and interviews (in Tagalog) with participants from 2019-2022, alongside physical observation and photographic recording of local retail outlets.
  - A multi-sited approach was used to explore the utility and meaning of digital transactions across disparate needs and means of the larger urban population.
  - The study was grounded in Karl Polanyi's concept of embeddedness, analyzing how digital transactions are given meaning within established social and cultural norms.
  - The researchers identified and analyzed three key forms of digitally-enabled support: Abono, Pantawid, and Emergency transfers, which they collectively term 'abot kamay'.
findings:
  - Digital transactions were preferred by participants for managing the awkwardness of refusing requests or awaiting repayment within kinship and community networks.
  - The use of GCash was found to enable secret financial transfers, allowing individuals to manage family obligations and avoid conflict.
  - num: Digital payments in the Philippines reached 42.1% of retail payments in 2022, with peer-to-peer transfers growing at 91.2% per annum by mid-2023.
  - Participants consistently framed their adoption of digital transactions not around convenience, but around the maintenance and management of social relationships.
  - Digital transaction affordances like SMS receipts were used by participants to create personal records for tracking social debts and obligations.
  - The digital platform ecosystem enables novel transaction chains, such as earning GCash credits through attention-economy apps like Buzz Break or gaming on Mobile Legends.
  - The sharing of mobile "load" (airtime) remains a critical form of reciprocal exchange, often acting as a precursor to or substitute for digital money transfers.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: abot kamay
    definition: Literally 'within reach' and figuratively 'a helping hand', it denotes the use of digital platforms to enable remote monetary support, embodying functional assistance and ontological proximity.
  - term: Abono
    definition: Paying for someone else's expense, for example, when they are unable to pay due to distance or lack of cash.
  - term: Pantawid
    definition: Money borrowed to get through a cash shortage.
  - term: suki
    definition: A loyal customer who receives privileges such as discounts and credit from a vendor.
  - term: kakayahan
    definition: Capacity; denotes the capacity of the giver to give and offer help, defining the limits and possibilities of abot kamay.
critical_citations:
  - "[Polanyi, 1944] — Foundational framework for economic embeddedness."
  - "[Granovetter, 1985] — Frames the ongoing relevance of reciprocity and redistribution."
  - "[Madianou and Miller, 2013] — Establishes the role of media in transnational Filipino families."
relevance:
  topics:
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Core focus on abot kamay, suki, and reciprocity as key Filipino financial norms.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: high
      justification: Directly analyzes abot kamay in contexts of emergencies, kinship obligations, and community support.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Implicitly challenges purely transactional views by categorizing digital money flows as gifts, debts, and support.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Provides a detailed overview and comparison of GCash, PayMaya/Maya, and GrabPay in the Philippines.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies key barriers like stringent ID requirements, account fees, and security concerns as gaps.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Highlights how mobile platforms are the primary interface for transactions in a context of limited traditional banking.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Discusses user anxiety about hacking and the use of intermediary accounts like GCash as an added security layer.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Shows trust is built through social networks and platform agents, not solely through institutional credibility.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Explains how features like receipts and records shape user engagement with financial obligations.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: Describes how gamification and rewards via platforms like Mobile Legends and Buzz Break drive retention and usage.
  contribution: This paper provides a crucial qualitative foundation for Odin's behavioral models by demonstrating that financial decisions in the Philippines are deeply embedded in social relationships and obligations like abot kamay. The findings directly inform the design of Odin's expense categorization, suggesting the need to distinguish between personal, familial, and communal financial flows. Furthermore, the paper's insights on trust and privacy directly justify a mobile-first design that prioritizes user control and security, as seen in the preference for intermediary accounts. Finally, the description of engagement dynamics via gaming and rewards provides a rationale for designing Odin's retention mechanisms around culturally relevant social interactions rather than purely utilitarian features.
  directly_justifies:
    - "Digital transactions are chosen to manage the awkwardness of refusing requests or awaiting repayment."
    - "SMS receipts from digital transactions are used as mental accounting for tracking social debts."
    - "Users adopt intermediary digital wallets as an extra layer of security against fraud."
    - "Engagement with transaction platforms is driven by social obligations and community practices."
    - "The need for a mobile-first design is justified by the high dependence on smartphones for financial access."
  limits:
    - "Study is qualitative and limited to three communities in Metro Manila, which may not be representative of all Filipino users."
    - "The research primarily focuses on the social meanings of transactions, offering limited quantitative insights into usage patterns [unacknowledged]."
    - "The impact of platform design features on user behavior is discussed anecdotally rather than systematically [unacknowledged]."
  mapping_rationale: The systematic scan across all 12 functional domains identified 10 relevant topic codes. The paper's core contribution to understanding culturally specific practices (2.A) and Filipino spending cycles (2.D) is high, as it directly explains the abot kamay idiom. The detailed landscape of GCash, Maya, and other platforms made it highly relevant to topics 4.A and 4.B. Topics related to mobile-first design (9.A), data privacy (10.A, 10.B), and engagement (11.A, 11.B) were flagged as medium due to supporting evidence on user preferences and behaviors. Domains like forecasting (6.A, 6.B), anomaly detection (8.A-C), and savings/debt management (13.A-C) were rejected because the paper does not address predictive modeling or specific algorithmic approaches to these areas. The overall relevance is medium-high, as it provides essential cultural and contextual grounding for Odin's behavioral and design modules, though it offers no technical solutions.
limitations:
  - "The qualitative study is based on a limited number of participants and communities in Metro Manila, restricting generalizability."
  - "The research does not provide a quantitative baseline for comparing the adoption and usage patterns across different demographic groups [unacknowledged]."
  - "The paper does not evaluate the efficacy of specific app features or their impact on user financial behavior [unacknowledged]."
  - "The study does not address the potential for digital transactions to increase financial vulnerability or debt among users [unacknowledged]."
remember_this:
  - "Filipino financial behavior is driven by culturally specific norms of reciprocity and obligation."
  - "Digital transaction platforms are embedded within existing social structures, not replacing them."
  - "Privacy in financial apps is managed through social practices like using intermediary accounts."
  - "GCash facilitates secret transfers to manage family obligations and avoid conflict."
  - "Digital receipts are used for personal accounting of social debts and relationships."
```
---

## Paper 47: Mohammad et al_summarized.md

**Source File:** `Mohammad et al_summarized.md`

```yaml
paper_id: 10.1038/s41598-026-51764-9
designation: international-algorithm-specific
title: Transforming credit risk evaluation in digital lending from black box models to transparent decisions
authors: Mohammad, A.A.S.; Mohammad, S.I.; Vasudevan, A.; Azam, S.M.F.; Sevukamoorthy, L.; Parhi, M.; Shankalia, M.U.; Salami, Z.A.
year: 2026
venue: Scientific Reports
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
  - 12.C
tldr: A hybrid framework integrating gradient boosting models with metaheuristic optimization improves credit risk prediction accuracy and interpretability for digital lending.
problem_and_motivation: Traditional credit scoring models fail to assess non-traditional borrowers, while existing machine learning approaches often lack interpretability, limiting trust and regulatory compliance. A unified framework is needed to jointly optimize predictive performance and transparency.
approach:
  - A publicly available dataset of 1,000 loan applications with 16 attributes was used.
  - LightGBM, CatBoost, and Explainable Boosting Machine were selected as base models.
  - Brown-Bear Optimization Algorithm and Puma Optimizer were used for hyperparameter tuning.
  - Class imbalance was addressed using cost-sensitive learning with class weights.
  - Feature importance was analyzed using SHAP and permutation-based methods.
findings:
  - num: Optimized CatBoost achieved 99.50% test accuracy and 0.9951 F1-score.
  - num: Optimized LightGBM achieved 99.01% test accuracy and 0.9901 F1-score.
  - num: Optimized EBM achieved 98.51% test accuracy and 0.9852 F1-score.
  - Metaheuristic optimization consistently improved performance over baseline models.
  - SHAP analysis identified credit history age as the most influential predictor.
  - The framework balances predictive accuracy with feature-level interpretability.
key_figures_tables:
  - Table 4: K-fold cross-validation results → Models show stable performance across folds.
  - Table 6: Performance metrics for baseline and optimized models → Optimization significantly improves all metrics.
  - Table 7: Confusion matrices → Optimized models reduce false positives and negatives substantially.
  - Figure 6: SHAP values → Credit history age is the most influential feature in risk prediction.
key_equations:
  - equation: "Accuracy = (TP + TN) / (TP + TN + FP + FN)"
    explanation: "Proportion of correctly classified instances."
  - equation: "Precision = TP / (TP + FP)"
    explanation: "Proportion of true positives among predicted positives."
  - equation: "Recall = TP / (TP + FN)"
    explanation: "Proportion of actual positives correctly identified."
  - equation: "F1 = 2 * (Precision * Recall) / (Precision + Recall)"
    explanation: "Harmonic mean of precision and recall."
definitions:
  - term: BNPL
    definition: "Buy Now, Pay Later; a short-term financing model."
  - term: LightGBM
    definition: "A gradient boosting framework using histogram-based splitting."
  - term: CatBoost
    definition: "A gradient boosting algorithm with native categorical feature handling."
  - term: EBM
    definition: "Explainable Boosting Machine; a transparent, GAM-based model."
  - term: BBOA
    definition: "Brown-Bear Optimization Algorithm; a nature-inspired metaheuristic."
  - term: PO
    definition: "Puma Optimizer; a metaheuristic inspired by puma hunting behavior."
  - term: SHAP
    definition: "SHapley Additive exPlanations; a method for explaining model predictions."
critical_citations:
  - "[Roy and Vasa, 2025] — Reviews AI methods for credit risk assessment."
  - "[Zhou and Wang, 2025] — Uses XGBoost with SHAP for interpretable credit risk."
  - "[Papa and Ricafort, 2024] — Demonstrates ANN/RNN for cooperative lending."
  - "[De Silva, 2025] — Achieves 99% accuracy with human-in-the-loop models."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly models borrower characteristics and default risk.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: medium
      justification: Addresses non-traditional borrowers with limited credit history.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Uses boosting and optimization for borrower classification.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Develops a predictive framework for credit risk.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: Provides a general methodology applicable to spending data.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: Credit risk assessment informs budgeting decisions.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Not directly about budget recommendations but can inform credit limits.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Default prediction is a form of anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Uses classification algorithms applicable to anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Employs robust cross-validation and multiple metrics.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Evaluates individual models and optimization effects.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: low
      justification: Focuses on credit risk, but uses similar evaluation metrics.
  contribution: "This paper provides a framework for integrating explainable boosting models with metaheuristic optimization for credit risk assessment. The approach can inform Odin's behavioral profiling module by demonstrating how to classify borrowers using financial and demographic features. The use of SHAP for interpretability aligns with Odin's need for transparent decision-making in financial profiling. The methodology also offers a template for evaluating prediction models using cross-validation and imbalance-aware metrics."
  directly_justifies:
    - "Gradient boosting models achieve high accuracy on tabular financial data."
    - "Metaheuristic optimization improves hyperparameter tuning over grid search."
    - "SHAP analysis identifies key features influencing default risk."
    - "EBM provides feature-level transparency suitable for regulated environments."
    - "Class imbalance can be addressed via cost-sensitive learning without synthetic data."
  limits:
    - "Dataset is not from a BNPL platform, limiting direct applicability."
    - "Results are based on a single, relatively small dataset (n=1000)."
    - "Real-world operational validation was not conducted."
    - "Comparison with other metaheuristics or deep learning models is limited [unacknowledged]."
  mapping_rationale: "A systematic scan of all 12 functional domains was conducted to map the paper to Odin's topic codes. The paper's core contribution lies in algorithmic credit risk prediction, directly informing domains such as Behavioral Profiling (5.A, 5.B, 5.C), Predictive Modeling (6.A, 6.B), and Anomaly Detection (8.A, 8.B). The rigorous evaluation framework (12.A, 12.B) was also flagged as highly relevant. The paper was considered for topics in Budget Recommendation (7.A, 7.B) and Savings/Debt Management (13.A, 13.B, 13.C) but received low or contextual relevance because it does not directly address budgeting strategies, savings goals, or debt management practices. Similarly, Mobile-First Design (9.A, 9.B) and Data Privacy (10.A, 10.B) were not relevant. Borderline cases included the connection between credit risk and budget constraints (7.A), which was deemed contextual, and the application of classification algorithms to anomaly detection (8.B), which was considered medium due to shared methodology. Overall, the paper provides high relevance for modules involving predictive modeling, user classification, and system evaluation, but limited direct applicability to budgeting, savings, or engagement features."
limitations:
  - "Limited to a single dataset of 1,000 records, reducing generalizability."
  - "No comparison with other metaheuristic optimization algorithms."
  - "No real-world deployment or user study was conducted."
  - "The trade-off between interpretability and performance is not quantitatively assessed [unacknowledged]."
remember_this:
  - "Optimized CatBoost achieved 99.5% accuracy on credit risk prediction."
  - "Metaheuristic optimization significantly outperforms baseline tuning methods."
  - "EBM provides transparent feature contributions for regulatory compliance."
  - "Credit history age is the most influential predictor of default risk."
  - "Hybrid frameworks can balance accuracy and interpretability in finance."
```
---

## Paper 48: Bhardwaj_summarized.md

**Source File:** `Bhardwaj_summarized.md`

```yaml
paper_id: f47ac10b-58cc-4372-a567-0e02b2c3d479
designation: international-algorithm-specific
title: Agent Behavioral Contracts: Formal Specification and Runtime Enforcement for Reliable Autonomous AI Agents
authors: Bhardwaj, V. P.
year: 2026
venue: arXiv
odin_topics:
  - 4.B
  - 5.B
  - 8.A
  - 8.B
  - 8.C
  - 10.A
  - 10.B
  - 12.A
  - 12.B
tldr: A formal framework for behavioral contracts enables runtime enforcement, drift detection, and recovery for autonomous AI agents, making violations measurable and bounds provable.
problem_and_motivation: Large language model agents lack formal behavioral specifications, leading to undetected drift and governance failures. Existing approaches like prompts and guardrails cannot provide runtime guarantees or compositionality. This paper addresses the need for a contract-based framework with probabilistic compliance and bounded drift.
approach:
  - Define Agent Behavioral Contracts as a tuple of preconditions, invariants (hard/soft), governance constraints, and recovery mechanisms.
  - Introduce (p,δ,k)-satisfaction to account for LLM non-determinism with bounded recovery windows.
  - Model drift as an Ornstein-Uhlenbeck process and prove a drift bound theorem with closed-form design criterion.
  - Implement ContractSpec DSL and AgentAssert runtime library with sub-10ms per-action overhead.
  - Evaluate on 7 models from 6 vendors using AgentContract-Bench across 1,980 sessions, comparing contracted vs uncontracted agents.
findings:
  - "num: 5.2-6.8 soft violations per session detected in contracted agents, versus 0.0-0.3 in uncontracted (p<0.0001, Cohen's d=6.7-33.8)."
  - "num: Hard compliance reached 88-100% under contract, with 100% for GPT-5.2 and GPT-4o-mini."
  - "num: Behavioral drift was bounded to D*<0.27 over 12-turn sessions, matching OU mean-reversion (R2=0.49-0.75)."
  - "num: Recovery re-prompting achieved 100% success for frontier models; average 67% across all models."
  - "num: Runtime overhead remained below 10ms per action, <1% of LLM inference latency."
key_figures_tables:
  - "Table 9: E1 results across 7 models → Contracted agents detect 5.2–6.8 soft violations vs 0.0–0.3 in uncontracted."
  - "Figure 2: Drift trajectory over 12-turn sessions → Contracted drift stabilizes and remains bounded, while uncontracted has no measurable drift."
  - "Figure 3: OU model fit → Drift dynamics match mean-reversion with R2=0.49–0.75."
  - "Figure 4: Ablation heatmap → Removing recovery or soft constraints degrades reliability index by ∼0.20."
  - "Figure 5: Runtime overhead scaling → Overhead scales linearly with constraints, below 10ms for typical contracts."
key_equations:
  - equation: "C_hard(t) = |{c ∈ I_hard ∪ G_hard : c(s_t,a_t)=true}| / |I_hard ∪ G_hard|"
    explanation: "Fraction of satisfied hard constraints."
  - equation: "C_soft(t) = |{c ∈ I_soft ∪ G_soft : c(s_t,a_t)=true}| / |I_soft ∪ G_soft|"
    explanation: "Fraction of satisfied soft constraints."
  - equation: "P(∀t: C_hard(t)=1) ≥ p and P(∀t: C_soft(t)<1-δ ⇒ ∃t'≤t+k: C_soft(t')≥1-δ) ≥ p"
    explanation: "(p,δ,k)-satisfaction with hard persistent and soft recoverable guarantees."
  - equation: "dD = (α - γD)dt + σdW(t)"
    explanation: "OU drift dynamics with injection rate α and recovery rate γ."
  - equation: "π_D = N(α/γ, σ²/(2γ))"
    explanation: "Stationary drift distribution with mean α/γ and variance σ²/(2γ)."
  - equation: "γ ≥ (2αD_max + σ² ln(1/ε) + sqrt((2αD_max + σ² ln(1/ε))² - 4α²D_max²)) / (2D_max²)"
    explanation: "Minimum recovery rate to keep drift below D_max with confidence 1-ε."
definitions:
  - term: ABC
    definition: "Agent Behavioral Contracts: formal framework for agent specification and enforcement."
  - term: OU
    definition: "Ornstein-Uhlenbeck: stochastic process with mean-reversion."
  - term: JSD
    definition: "Jensen-Shannon divergence: symmetric measure of distributional distance."
  - term: SPRT
    definition: "Sequential Probability Ratio Test: sequential hypothesis test for compliance certification."
  - term: (p,δ,k)-satisfaction
    definition: "Probabilistic contract compliance with probability p, tolerance δ, recovery window k."
critical_citations:
  - "[Meyer, 1992] — Design-by-Contract foundational work."
  - "[Bai et al., 2022] — Constitutional AI training-time alignment."
  - "[Wang et al., 2026a] — Impossibility of safety invariance without external correction."
  - "[Rath, 2026] — Behavioral drift in multi-agent LLM systems."
relevance:
  topics:
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: "Paper identifies gaps in existing agent guardrails and provides formal contracts."
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: "Requires reference distribution calibration, analogous to cold-start baseline."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: "Violation detection is a form of anomaly detection applicable to spending."
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: "Proposes constraint evaluation and drift detection algorithms."
    - code: 8.C
      name: Cold‑Start Baseline Strategies for Anomaly Detection
      relevance: medium
      justification: "Reference distribution serves as cold-start baseline."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: "Hard invariants enforce PII and data protection, directly relevant."
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: "Contracts build trust through enforceability and transparency."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: "Introduces benchmark and metrics for evaluating contract enforcement."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: "Provides empirical evaluation of the enforcement algorithm across models."
  contribution: "The ABC framework's hard/soft constraint separation and drift detection can inform Odin's anomaly detection module by providing formal violation metrics and leading indicators. The reference distribution calibration addresses Odin's cold-start problem for user profiling. The compositionality theorem supports evaluating multi-agent pipelines, applicable to Odin's modular architecture. The runtime enforcement and recovery mechanisms offer a template for ensuring data privacy and user trust in financial systems."
  directly_justifies:
    - "Runtime contract enforcement detects soft violations that would otherwise be invisible."
    - "Recovery mechanisms convert exponential compliance decay into linear decay."
    - "Contracts with recovery rate γ > α bound behavioral drift to α/γ in expectation."
    - "Hard constraints can enforce zero-tolerance privacy and security policies."
    - "Reference distribution calibration enables cold-start baseline for drift detection."
  limits:
    - "State dictionary assumption: contract predicates require pre-computed features."
    - "Reference distribution must be calibrated; no automated recalibration for non-stationary environments."
    - "Recovery is monitoring by default; deployers must implement custom recovery handlers."
    - "k-window stationarity assumption may be optimistic for short sessions."
    - "Compositionality under correlated failures may be optimistic."
    - "Benchmark circularity: synthetic traces test engine consistency, not live behavioral detection."
  mapping_rationale: "All 12 functional domains were systematically scanned for relevance. The paper most directly informs the Existing Systems & Gaps (4.A, 4.B), Anomaly Detection (8.A, 8.B, 8.C), Data Privacy & User Trust (10.A, 10.B), and System Evaluation (12.A, 12.B) domains. It also touches on Behavioral Profiling (5.B) via cold-start drift detection. Cultural, expense categorization, forecasting, budget recommendation, mobile design, retention, and savings/debt domains were considered but rejected as the paper does not address those specific financial constructs. The overall relevance is medium-to-high for governance and evaluation modules."
limitations:
  - "State dictionary assumption: contract predicates require pre-computed features."
  - "Reference distribution must be calibrated; no automated recalibration for non-stationary environments."
  - "Recovery is monitoring by default; deployers must implement custom recovery handlers."
  - "k-window stationarity assumption may be optimistic for short sessions."
  - "Compositionality under correlated failures may be optimistic."
  - "Benchmark circularity: synthetic traces test engine consistency, not live behavioral detection."
remember_this:
  - "Contracted agents detect 5.2–6.8 soft violations per session that baselines miss."
  - "Hard compliance reaches 88–100% across models under contract enforcement."
  - "Drift is bounded to D*<0.27 over extended sessions with OU dynamics."
  - "Runtime overhead is under 10ms per action, negligible relative to inference."
  - "Recovery mechanisms significantly improve reliability, with ∼0.20 Θ degradation when removed."
```
---

## Paper 49: Askhiyah_summarized.md

**Source File:** `Askhiyah_summarized.md`

```yaml
paper_id: 10.59784/journaljoae.v1i1.37
designation: international
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

## Paper 50: D. R. et al_summarized.md

**Source File:** `D. R. et al_summarized.md`

```yaml
paper_id: 10.51483/IJAIML.6.2s.2026.754-762
designation: international-algorithm-specific
title: Robust Learning Under Distribution Shifts for Non-Stationary Data Environments
authors: "D, Rekha; Vairavan, Shanthi; MP, Sunil; Katariya, Jitendra Kumar; Parikh, Swapnil Maheshkumar; Shanthi, T.; Shanthi, R."
year: 2026
venue: International Journal of Artificial Intelligence and Machine Learning
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 12.B
tldr: Introduces an adaptive learning framework combining drift detection, online incremental learning, and AHO optimization to maintain robust classification performance under sudden, gradual, and recurrent distribution shifts.
problem_and_motivation: Non-stationary data environments cause performance degradation in static ML models due to concept drift. Existing approaches treat drift detection, adaptation, and optimization separately, limiting robustness. A unified framework is needed to handle diverse drift types while maintaining computational efficiency.
approach:
  - Uses PaySim mobile money transaction dataset with 743 time steps and five transaction types.
  - Proposes AHO-InDNN combining an incremental deep neural network with archerfish hunting optimization for parameter tuning.
  - Integrates drift detection module to identify sudden, gradual, and recurrent concept drift using statistical divergence.
  - Employs online and incremental learning to update model parameters without full retraining upon drift detection.
  - Applies Lévy flight reinitialization to avoid stagnation and an LDP-based optimization for stability and uncertainty reduction.
  - Compares against KNN, SMOTEBoost with cost-sensitive learning, and MH-DRNN using accuracy, precision, recall, F1.
findings:
  - "num: AHO-InDNN achieved 98.74% accuracy, 98.42% precision, 98.52% recall, and 98.37% F1-score."
  - "num: Outperformed MH-DRNN by 0.24% in accuracy and 0.37% in F1."
  - Demonstrated superior robustness across sudden, gradual, and recurrent drift scenarios.
  - LDP-based optimization reduced false alarms and improved stability under distribution shifts.
key_figures_tables:
  - "Figure 2: Illustrates sudden, gradual, and recurrent concept drift patterns in fraud rate → demonstrates need for adaptive learning."
  - "Table 2: Performance comparison of models under dynamic shifts → AHO-InDNN achieves highest metrics."
  - "Figure 3: Recall and F1 comparison → proposed model outperforms baselines."
key_equations:
  - equation: "y' = (y - y_min) / (y_max - y_min)"
    explanation: Min-max normalization scales features to [0,1].
  - equation: "F(θ) = - (1/M) ∑_m ∑_p s_mp log x_mp"
    explanation: Regularized loss function mitigates overfitting under drift.
  - equation: "θ_s = θ_{s-1} - α * (β1*m_{s-1} + (1-β1)*∇θ F(θ_{s-1})) / (sqrt(β2*v_{s-1} + (1-β2)*(∇θ F(θ_{s-1}))^2) + ε)"
    explanation: Adaptive moment-based gradient optimization for dynamic environments.
  - equation: "lim_{s→∞} (1/s) log P(X_s ∈ A) = - inf_{x∈A} I(x)"
    explanation: LDP detects rare distributional shifts in streaming data.
definitions:
  - term: AHO
    definition: Archerfish Hunting Optimization, a metaheuristic for parameter tuning balancing exploration and exploitation.
  - term: InDNN
    definition: Incremental Deep Neural Network with dynamic depth and neuron structure for non-stationary data.
  - term: LDP
    definition: Large Deviations Principle, a framework for estimating probabilities of rare events in streaming data.
  - term: Concept Drift
    definition: Change in the input-output relationship over time, causing model performance decay.
  - term: Distribution Shift
    definition: Change in the data distribution between training and testing phases.
critical_citations:
  - "[Liu et al., 2024] — Introduces deep reinforcement learning in nonstationary environments."
  - "[Halstead et al., 2022] — Analyzes concept drift adaptation in data streams."
  - "[Ma et al., 2023] — Discusses transfer learning under domain shift."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: low
      justification: Paper uses predictive modeling for fraud, not personal finance, but concept is transferable.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: Handles sequential transaction data and concept drift, relevant to spending forecasting.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Fraud detection is a form of anomaly detection; framework can inform spending anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Proposes a novel drift-adaptive algorithm for detecting fraudulent anomalies in transaction streams.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Provides comparative evaluation metrics and baselines useful for assessing Odin's modules.
  contribution: The paper's drift-adaptive framework informs Odin's anomaly detection module (8.B) by providing a robust online learning approach to detect unusual spending patterns. Its incremental learning capability supports forecasting module (6.B) for adapting to evolving user behavior. The evaluation methodology offers a baseline for assessing Odin's algorithmic modules (12.B). The LDP-based optimization could enhance stability in rare anomaly detection. Overall, the adaptive principles are applicable to Odin's real-time adjustment to shifting user financial behavior.
  directly_justifies:
    - "Adaptive models are necessary to maintain accuracy when spending patterns shift over time."
    - "Incremental updating without full retraining reduces computational cost while preserving performance."
    - "LDP-based optimization enhances stability under rare anomalous events."
    - "Drift detection enables timely model updates without manual intervention."
  limits:
    - "Relies on synthetic PaySim data rather than real-world financial transactions."
    - "Computational complexity of AHO optimization may need optimization for mobile deployment."
    - "Generalization to other financial domains (e.g., savings, budgeting) not evaluated. [unacknowledged]"
  mapping_rationale: "All 12 functional domains and their associated topic codes were systematically scanned. The paper is relevant to Anomaly Detection (8.A, 8.B) and Spending Forecasting (6.A, 6.B) because it addresses concept drift in sequential transaction data, a core challenge for personal finance systems. Evaluation methodologies (12.B) are also flagged due to the comparative benchmarking. Domains such as Filipino Cultural Context (2.A–D), Expense Categorization (3.A–C), Existing Systems (4.A–B), Behavioral Profiling (5.A–C), Budget Recommendation (7.A–D), Mobile-First Design (9.A–B), Data Privacy (10.A–B), User Retention (11.A–B), and Savings/Debt (13.A–C) were considered but rejected because the paper does not address these aspects; it focuses solely on algorithmic robustness under drift. Relevance levels: 8.B = high (direct algorithm for anomaly detection), 8.A and 6.B = medium (contextual but transferable), 6.A and 12.B = low/medium. Borderline cases: 6.A (predictive modeling) overlaps with 6.B but the paper is more about forecasting sequential data than general predictive modeling; we selected 6.B as more specific. Overall, the paper offers actionable insights for Odin's adaptive learning and anomaly detection modules but is not directly applicable to other domains."
limitations:
  - "Synthetic dataset may not capture real-world noise and variability."
  - "AHO optimization adds computational overhead not quantified for edge devices. [unacknowledged]"
  - "Framework tested only on fraud detection; applicability to spending categorization or budgeting not explored. [unacknowledged]"
remember_this:
  - "AHO-InDNN achieves 98.74% accuracy on fraud detection under concept drift."
  - "Incremental learning adapts to sudden, gradual, and recurrent drifts without full retraining."
  - "LDP optimization reduces false alarms and stabilizes model updates."
  - "Drift detection and online adaptation are key for maintaining performance in non-stationary environments."
```
---


---

## Agent Instruction

If the agent reading this document believes further context about a paper is needed, it may request the original converted markdown file (with the '_marked' suffix) from the user for the relevant paper(s).
