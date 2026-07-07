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
  - 1.B
  - 3.A
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 7.C
  - 8.A
  - 8.B
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
  - 13.C
tldr: A systematic literature review of 63 studies on ML credit scoring shows ensemble and hybrid models consistently outperform traditional approaches, while DL faces interpretability and data availability barriers.
problem_and_motivation: Traditional credit scoring models like logistic regression depend on narrow features and struggle to capture complex behavioral patterns, limiting their effectiveness with heterogeneous borrower profiles. Financial institutions face the challenge of processing loan applications quickly while maintaining accuracy, fairness, and regulatory compliance. ML approaches offer the potential to improve prediction accuracy, handle high-dimensional data, and incorporate alternative data sources, but their adoption is hindered by issues of interpretability, bias, and computational complexity.
approach:
  - Conducted a systematic literature review following PRISMA 2020 guidelines across four digital libraries (SpringerLink, ACM, IEEE Xplore, Google Scholar).
  - Employed a structured search query combining credit scoring, ML, DL, and ensemble learning terms for publications between 2018 and 2024.
  - Applied inclusion criteria focusing on peer-reviewed studies with empirical results and clearly defined evaluation metrics.
  - Performed data extraction covering ML techniques, datasets, evaluation metrics, and performance results from 63 selected studies.
  - Used bibliographic coupling and keyword co-occurrence analysis (VOSviewer) to map intellectual structure and thematic clusters.
findings:
  - "num: Ensemble and hybrid models consistently outperform single classifiers, with accuracy improvements up to 91.91% on the German dataset (GA+NN) and 93.16% on the Japanese dataset (multi-stage ensemble)."
  - "num: XGBoost-BO improved accuracy by 4.10% on the German dataset, 3.03% on Lending Club, and 2.76% on the Australian dataset."
  - "num: Deep CNN achieved 99.74% accuracy on the Australian credit dataset, significantly outperforming MLP's 90.75%."
  - "num: The GA-based feature selection combined with CatBoost achieved accuracies of 86.70%, 88.40%, and 86.20% on German, Australian, and Japanese datasets."
  - Interpretability challenges persist for complex ML models, with LIME and SHAP emerging as tools to bridge the explainability gap.
  - Alternative data sources (social media, mobile usage, psychometrics) show promise for credit scoring, especially for borrowers lacking traditional credit histories.
  - Accuracy (49 studies) and AUC (31 studies) are the most frequently reported evaluation metrics in credit scoring literature.
key_figures_tables:
  - "Table 4: Summary of machine learning studies → Shows LR, RF, SVM, KNN, and hybrid models with performance on German, Australian, and proprietary datasets."
  - "Table 5: Summary of deep learning studies → CNN, LSTM, and hybrid DL models achieve high accuracy on credit scoring benchmarks."
  - "Table 6: Summary of ensemble learning studies → Ensemble methods like XGBoost, GBDT, and multi-stage models dominate top performance rankings."
  - "Table 7: Ranked evaluation on German dataset → GA+NN achieves highest accuracy (91.91%) and AUC (92.60%)."
  - "Figure 2: Comparative accuracy of ML models → Random Forest and hybrid ML approaches achieve highest accuracies with low variability."
  - "Figure 3: Comparative accuracy of DL models → CNN and hybrid DL provide robust performance with lower variability."
  - "Figure 4: Comparative accuracy of ensemble models → XGB-BO and proposed ensembles capture peak performance in certain studies."
  - "Figure 5: Bibliographic coupling network → Three clusters: traditional statistical approaches, ensemble-based ML, and emerging DL applications."
key_equations:
  - equation: "P(Y=1|x) = 1 / (1 + e^{-(β0 + β^T x)})"
    explanation: "Logistic regression estimates probability of binary credit default outcome."
  - equation: "ℓ(β0, β) = Σ [y_i log p(x_i) + (1 - y_i) log(1 - p(x_i))]"
    explanation: "Log-likelihood maximized to estimate logistic regression parameters."
  - equation: "Accuracy = (TP + TN) / (TP + TN + FP + FN)"
    explanation: "Overall correctness measure, limited with imbalanced credit data."
  - equation: "F1-Score = 2 × (Precision × Recall) / (Precision + Recall)"
    explanation: "Harmonic mean balancing precision and recall for class imbalance."
definitions:
  - term: "ML"
    definition: "Machine learning, algorithms that enable systems to learn from data and make predictions without explicit programming."
  - term: "DL"
    definition: "Deep learning, subset of ML using neural networks with multiple layers to automatically extract features."
  - term: "EL"
    definition: "Ensemble learning, integration of multiple learning algorithms to enhance predictive performance."
  - term: "LR"
    definition: "Logistic regression, probabilistic classification model estimating binary outcome probability."
  - term: "RF"
    definition: "Random forest, ensemble of decision trees using bagging for classification and regression."
  - term: "SVM"
    definition: "Support vector machine, supervised model mapping data to high-dimensional space for classification using hyperplanes."
  - term: "KNN"
    definition: "K-nearest neighbors, non-parametric technique classifying based on distance metrics to nearest neighbors."
  - term: "CNN"
    definition: "Convolutional neural network, deep feedforward network for feature extraction and classification."
  - term: "LSTM"
    definition: "Long short-term memory, recurrent neural network designed for variable length sequences with memory gates."
  - term: "XGBoost"
    definition: "Extreme gradient boosting, ensemble model combining tree models with gradient boosting."
  - term: "GBDT"
    definition: "Gradient boosting decision tree, ensemble method combining weak base learners to craft robust models."
  - term: "AUC"
    definition: "Area under the ROC curve, measure of model's ability to distinguish between classes."
  - term: "PRISMA"
    definition: "Preferred reporting items for systematic reviews and meta-analyses, guideline framework for systematic reviews."
critical_citations:
  - "[Dastile et al., 2020] — Found ensemble methods outperform single classifiers in credit scoring."
  - "[He et al., 2018] — Proposed novel ensemble method adapting to different imbalance ratios."
  - "[Dumitrescu et al., 2022] — Introduced PLTR combining logistic regression with decision tree rules."
  - "[Hayashi, 2022] — Reviewed deep learning applications and interpretability challenges in credit scoring."
  - "[Bücker et al., 2022] — Framework for enhancing interpretability of black-box ML credit scoring models."
relevance:
  topics:
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "contextual"
      justification: "Discusses financial behavior and repayment history in credit scoring, relevant to financial structure analysis."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "low"
      justification: "Credit scoring classification approaches inform categorization methodologies for PFMS."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews existing credit scoring methodologies and ML-based approaches in financial systems."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Identifies limitations of traditional credit scoring models and gaps in ML adoption including interpretability and bias."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "ML models classify borrower behavior and creditworthiness, informing behavioral profile construction."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Systematically reviews ML classification techniques including SVM, RF, and ensemble methods for credit scoring."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Reviews predictive modeling techniques including DL and ensemble methods for credit risk prediction."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "medium"
      justification: "LSTM and attention mechanisms discussed for sequence-based credit prediction, applicable to spending forecasting."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "low"
      justification: "Credit scoring ML approaches inform algorithmic design for budget recommendation systems."
    - code: "7.C"
      name: "Constrained Optimization Approaches for Budget Allocation"
      relevance: "contextual"
      justification: "Discusses optimization methods for credit scoring models, tangentially related to budget constraints."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Credit default prediction frameworks analogous to anomaly detection approaches for spending behavior."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "low"
      justification: "Machine learning classification techniques transferable to anomaly detection in spending data."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "contextual"
      justification: "Discusses mobile phone data for credit scoring, relevant to mobile-first design context."
    - code: "9.B"
      name: "Mobile UX Design for Personal Finance"
      relevance: "contextual"
      justification: "Alternative data from mobile usage informs user experience considerations for financial applications."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "medium"
      justification: "Addresses privacy concerns in using alternative data and regulatory compliance (GDPR, IFRS 9)."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "high"
      justification: "Interpretability and explainability (SHAP, LIME) are critical for building user trust in automated credit decisions."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Comprehensively reviews evaluation metrics (accuracy, AUC, F1-score, G-mean, KS) used in credit scoring studies."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Provides detailed performance comparisons of ML, DL, and ensemble algorithms across benchmark datasets."
    - code: "13.C"
      name: "End-of-Period Surplus as a Savings Input"
      relevance: "contextual"
      justification: "Credit scoring default prediction models use surplus/deficit patterns, relevant to surplus management."
  contribution: "This systematic review provides a comprehensive framework for selecting ML algorithms for Odin's spending classification and forecasting modules by benchmarking performance across datasets. It validates the use of ensemble and hybrid models for behavioral profiling, establishing an evidence base for Odin's classification engine. The review's analysis of evaluation metrics directly informs Odin's evaluation strategy for algorithmic modules, supporting performance comparison and validation. The identification of interpretability techniques like SHAP and LIME guides Odin's approach to building user trust through explainable predictions. The discussion of alternative data integration contextualizes Odin's use of Filipino-specific spending cycles and user-declared preferences."
  directly_justifies:
    - "Ensemble and hybrid ML models consistently outperform single classifiers in credit scoring tasks."
    - "Model interpretability is critical for user trust and regulatory compliance in financial decision-making."
    - "Alternative data sources can improve credit assessment for borrowers lacking traditional financial histories."
    - "Accuracy and AUC are the most commonly used metrics for evaluating predictive model performance."
    - "Class imbalance handling techniques like SMOTE are essential for reliable credit risk assessment."
  limits:
    - "Limited to peer-reviewed journal papers and conference articles, excluding relevant technical reports or industry studies."
    - "Search confined to four online databases, potentially missing relevant studies from other digital libraries."
    - "Lack of comparative analysis to identify most effective models due to heterogeneous evaluation metrics across studies."
    - "Fast-evolving nature of ML means continuous updates are necessary to capture new advances."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated canonical topics was performed. The paper was flagged as highly relevant for Predictive Modeling (6.A, high), Classification Approaches (5.C, high), Evaluation Frameworks (12.A, high), Algorithmic Module Evaluation (12.B, high), and User Trust (10.B, high). Medium relevance was assigned to Existing Systems (4.A), System Limitations (4.B), Behavioral Profiles (5.A), Anomaly Detection (8.A), and Data Privacy (10.A), as the paper reviews existing systems and discusses privacy concerns. Low relevance was assigned to Expense Categorization (3.A) and Anomaly Detection Algorithms (8.B) as the paper does not specifically address these domains. Contextual relevance was assigned to Financial Structure (1.B), Budgeting Strategies (7.A), Mobile-First Design (9.A, 9.B), and End-of-Period Surplus (13.C) as these areas are tangentially related to the review's focus on credit scoring. The paper was considered and rejected for Culturally Specific Financial Practices (2.A-D) and Retention Mechanisms (11.A-B) as these domains were not addressed. Overall, the paper provides substantial evidence for Odin's machine learning modules, evaluation frameworks, and interpretability requirements."
limitations:
  - "Search strategy limited to four online databases, excluding relevant studies from other digital libraries. [unacknowledged]"
  - "Heterogeneous evaluation metrics across studies hinder direct performance comparisons between models. [acknowledged]"
  - "Class imbalance and varying data preprocessing methods complicate cross-study validation. [unacknowledged]"
  - "Interpretability challenges persist for complex ML models, with SHAP and LIME facing reliability concerns under adversarial conditions."
  - "High-dimensional credit data introduces computational complexity, making deployment costly for smaller institutions."
remember_this:
  - "Ensemble and hybrid ML models consistently outperform single classifiers in credit scoring."
  - "Model interpretability is critical for building user trust in automated financial decisions."
  - "Class imbalance handling techniques like SMOTE are essential for reliable credit risk models."
  - "Alternative data sources show promise for borrowers lacking traditional credit histories."
  - "Accuracy and AUC are the most common evaluation metrics for credit scoring models."
```
---

## Paper 4: John_summarized.md

**Source File:** `John_summarized.md`

```yaml
paper_id: 10.48550/arXiv.2511.03807
designation: international-algorithm-specific
title: Fair and Explainable Credit-Scoring under Concept Drift: Adaptive Explanation Frameworks for Evolving Populations
authors: John, S.
year: 2026
venue: arXiv
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
tldr: Adaptive SHAP explanation methods maintain interpretability and fairness in credit-scoring models under concept drift without sacrificing predictive accuracy.
problem_and_motivation: Static explainability tools like SHAP fail under concept drift, producing unstable and potentially unfair explanations in dynamic credit environments. Existing drift adaptation focuses on predictive accuracy, leaving interpretive consistency and fairness unaddressed. This gap threatens regulatory compliance and user trust.
approach:
  - Data source: Synthetic multi-year credit dataset (2015-2024) with demographic, financial, and socioeconomic features.
  - Method: XGBoost baseline plus three adaptive SHAP variants: drift-weighted reweighting, sliding-window rebaselining, and Ridge surrogate calibration.
  - Evaluation setup: Expanding-window validation, yearly retraining, and longitudinal tracking of explanation stability and fairness.
  - Baselines: Static SHAP explanations compared against adaptive methods.
  - Metrics: Explanation stability (cosine, Kendall tau, Jaccard), fairness (DPD, EOD, equalized odds), and robustness tests.
findings:
  - num: PSI for annual_income reached 0.16 by 2019, confirming progressive covariate drift.
  - num: Default rates increased from ~15% in 2015 to over 23% in 2024.
  - num: Baseline AUC remained stable (0.63-0.66) despite drift, but explanation consistency degraded.
  - num: Method B reduced demographic parity difference by 0.026 (p < 0.05) without affecting AUC.
  - num: Method B and C achieved high explanation stability (cosine ≈ 0.995, Kendall τ ≈ 0.89).
  - num: Counterfactual perturbation: 10% decrease in credit_score increased default probability by 0.05.
  - Proxy variable detection identified race-associated features (p < 0.01; η² = 0.017-0.045).
key_figures_tables:
  - Figure 1: Loan default rate by year → default rate rose from 15% to 23% over 2015-2024.
  - Figure 2: PSI for annual_income and credit_score → PSI increased steadily, confirming drift.
  - Figure 3: JS divergence for race and gender → race/gender stable but Chi-square indicated significance.
  - Figure 4: Model test AUC over test years → AUC stable at 0.63-0.66.
  - Figure 5: DPD over time by model for race → DPD fluctuated, peaking during recession years.
  - Figure 6: EOD over time by model for race → EOD showed variability similar to DPD.
  - Figure 7: DPD before and after method B recalibration → DPD reduced significantly post-recalibration.
  - Figure 8: Explainability stability over time → stability metrics varied, motivating adaptive methods.
  - Figure 9: Top features by final test year → loan_amount, dti, credit_score were top predictors.
  - Figure 10: Kendall tau and Cosine similarity for adaptive methods → Methods B and C achieved highest stability.
  - Figure 11: Final year feature importance baseline vs. adaptive → adaptive methods showed more consistent feature rankings.
  - Figure 12: Number of harmful features detected by explainability method → adaptive methods reduced harmful proxy features.
  - Figure 13: Mean probability change from counterfactual perturbations → monotonic directional responses validated logic.
  - Figure 14: SHAP background size sensitivity test → adaptive methods showed improved consistency.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: SHAP
    definition: SHapley Additive exPlanations, a game-theoretic method for explaining model predictions.
  - term: XAI
    definition: Explainable Artificial Intelligence.
  - term: PSI
    definition: Population Stability Index, a measure of distributional shift in features.
  - term: JS
    definition: Jensen-Shannon divergence, a measure of similarity between probability distributions.
  - term: KS
    definition: Kolmogorov-Smirnov test, a nonparametric test for distribution equality.
  - term: DPD
    definition: Demographic Parity Difference, a fairness metric measuring equal positive prediction rates.
  - term: EOD
    definition: Equal Opportunity Difference, a fairness metric measuring equal true positive rates.
critical_citations:
  - "[Widmer and Kubat, 1996] — Established concept drift as a core challenge in learning systems."
  - "[Gama et al., 2014] — Surveyed drift adaptation, noting the gap in maintaining interpretability."
  - "[Lundberg and Lee, 2017] — Introduced SHAP, the static baseline used in this study."
  - "[Barocas et al., 2023] — Emphasized fairness as a continuous, context-dependent requirement."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Models financial behavior via credit risk prediction, capturing changing borrower profiles.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: contextual
      justification: Treats evolving borrower characteristics as a drift problem, relevant to profile dynamics.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Uses XGBoost for credit risk classification, but focuses on explanation, not profiling.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Concept drift detection can identify anomalies in spending behavior over time.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Adaptive SHAP methods detect drift-induced changes in feature importance, akin to anomaly shifts.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Proxy variable detection addresses bias, which has privacy and fairness implications.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Stable, fair explanations directly support user trust and transparency.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a robust evaluation framework for explanation stability, fairness, and robustness.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Benchmarks adaptive SHAP variants against static baselines using multiple metrics.
  contribution: "This paper contributes an adaptive explainability framework for credit-scoring, directly applicable to Odin's expense forecasting and anomaly detection modules. The sliding-window SHAP rebaselining (Method B) offers a practical technique for maintaining explanation stability under changing user spending patterns. The fairness recalibration mechanism provides a template for Odin's budget recommendation module to adjust for demographic disparities. The evaluation metrics (cosine, Kendall tau, Jaccard) and robustness tests offer a blueprint for assessing Odin's algorithmic modules. Overall, the adaptive explanation framework ensures that Odin's recommendations remain interpretable and fair as user financial behavior evolves."
  directly_justifies:
    - "Adaptive SHAP explanations maintain stability under concept drift, supporting reliable anomaly detection."
    - "Sliding-window background sampling reduces explanation volatility, aligning with mobile-first design needs."
    - "Fairness recalibration can be integrated into budget recommendation to prevent disparate impact."
    - "Proxy variable detection helps identify hidden biases in spending categories and user attributes."
  limits:
    - "Study uses synthetic data, not real Filipino spending data."
    - "Fairness analysis focuses on single attributes, not intersectional demographics."
    - "SHAP computational cost may hinder real-time mobile deployment."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant to Behavioral Profiling (5.A, 5.B, 5.C) because it models evolving borrower risk profiles, though it does not explicitly classify financial personality types. Anomaly Detection (8.A, 8.B) was selected because concept drift detection and adaptive explanation stability are directly relevant to identifying shifts in spending behavior that could indicate anomalies. Data Privacy & User Trust (10.A, 10.B) were chosen because stable, fair explanations build user trust and proxy variable detection addresses bias, which has privacy implications. System Evaluation (12.A, 12.B) received high relevance due to the paper's comprehensive evaluation framework for algorithmic modules, including stability, fairness, and robustness metrics. Domains like Expense Categorization (3.A, 3.B, 3.C), Spending Forecasting (6.A, 6.B), and Budget Recommendation (7.A, 7.B, 7.C, 7.D) were considered but rejected because the paper focuses on credit risk, not expense tracking or budget allocation. The paper's adaptive explanation framework and evaluation methodology are highly relevant to Odin's need for interpretable and fair algorithms in a dynamic financial environment."
limitations:
  - "SHAP analysis is computationally heavy, impacting scalability and real-time use. [unacknowledged]"
  - "Fairness assessment focuses on single attributes, not intersecting demographic factors. [unacknowledged]"
  - "The dataset is synthetic and may not fully capture real-world credit dynamics."
  - "The study does not address how to integrate adaptive explanations into a production mobile app."
remember_this:
  - "Adaptive SHAP methods stabilize explanations under concept drift."
  - "Sliding-window rebaselining improved fairness by reducing demographic parity difference by 0.026."
  - "Explanation stability remained high with cosine similarity ≈ 0.995 and Kendall τ ≈ 0.89."
  - "Explainability can evolve alongside data without sacrificing predictive accuracy."
  - "Adaptive frameworks support ongoing fairness and transparency in dynamic systems."
```
---

## Paper 5: Liang et al_summarized.md

**Source File:** `Liang et al_summarized.md`

```yaml
paper_id: 10.48550/arXiv.2602.16173
designation: international-algorithm-specific
title: Learning Personalized Agents from Human Feedback
authors: Liang, K.; Kruk, J.; Qian, S.; Yang, X.; Bi, S.; Yao, Y.; Nie, S.; Zhang, M.; Liu, L.; Fernández Fisac, J.; Zhou, S.; Hosseini, S.
year: 2026
venue: arXiv
odin_topics:
  - 5.B
  - 6.A
  - 7.D
  - 8.B
  - 10.B
  - 11.A
tldr: A continual personalization framework uses explicit memory and dual feedback to enable agents to learn user preferences online and adapt to preference drift.
problem_and_motivation: Static personalization models fail to adapt to new users, learn from real-time errors, or handle evolving preferences. This limitation is critical for user-facing agents that must align with individual, non-stationary preferences.
approach:
  - Simulated long-horizon sequential decision-making with per-user tasks and latent preference states.
  - Used PAHF framework with a three-step loop: pre-action clarification, action execution, and post-action feedback integration.
  - Employed explicit per-user memory (SQLite/FAISS) with add, retrieve, and update operations.
  - Evaluated on two bespoke benchmarks: embodied manipulation (40 users, 30 scenarios/phase) and online shopping (20 users, 45 scenarios/phase).
  - Implemented a four-phase protocol to separately measure initial learning and adaptation to persona shifts.
  - Instantiated agents with GPT-4o and baselines: no memory, pre-action only, post-action only.
findings:
  - num: Pre-action agents achieved substantially higher success on the first interaction than no-memory or post-action-only baselines.
  - num: Pre-action only agents showed limited improvement under preference drift, with Phase-3 success rates below the no-memory baseline in the embodied domain.
  - num: Post-action agents recovered to 67.9% Phase-4 success in embodied tasks, closely approaching PAHF at 70.5%.
  - num: PAHF achieved the highest overall success rates across all phases and domains, reaching 70.5% in embodied Phase 2 and 70.3% in shopping Phase 4.
  - PAHF’s average cumulative personalization error was consistently lower than single-channel baselines during both initial learning and adaptation.
key_figures_tables:
  - Figure 3: Embodied manipulation learning curves → PAHF combines low initial error with rapid drift adaptation.
  - Figure 4: Online shopping learning curves → Pre-action feedback prevents early errors; post-action is essential for recovery.
  - Table 1: Evaluation success rates (%) for Phase 2 and Phase 4 → PAHF outperforms all baselines in both domains and phases.
key_equations:
  - equation: "Mˆ_{t}^{\\prime} = F_{pre}^{update}(Mˆ_t, I_t, O_t, m_t, q_t, f_t^{pre})"
    explanation: Pre-action feedback updates memory before acting.
  - equation: "a_t = \\pi_{act}(I_t, O_t, m_t, q_t, f_t^{pre})"
    explanation: Action policy conditions on memory and pre-action interaction.
  - equation: "Mˆ_{t+1} = F_{post}^{update}(Mˆ_t^{\\prime}, I_t, m_t, q_t, f_t^{pre}, a_t, f_t^{post})"
    explanation: Post-action feedback revises memory after an error.
  - equation: "E[R_T] = O(K + \\gamma T m^{-k})"
    explanation: Dynamic regret bound for PAHF with K switches and ambiguity rate γ.
definitions:
  - term: PAHF
    definition: Personalized Agents from Human Feedback; framework for continual personalization.
  - term: RAG
    definition: Retrieval-Augmented Generation; method to retrieve and inject user histories into context.
critical_citations:
  - "[Christiano et al., 2017] — Foundational work on RLHF for aligning LLMs."
  - "[Rafailov et al., 2024] — DPO as an alternative to RLHF for preference learning."
  - "[Lewis et al., 2020] — Introduced RAG for knowledge-intensive NLP tasks."
relevance:
  topics:
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: high
      justification: Directly addresses learning from scratch without pre-existing user data.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Provides a framework for online learning from sequential interactions.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: high
      justification: Post-action feedback updates memory to correct confidently wrong actions.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Pre-action queries and post-action feedback can be applied to detect spending anomalies.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Accurate personalization and reduced errors can enhance user trust.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: Continual learning from feedback improves user retention.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: Provides a framework for modeling user profiles but not specific to finance.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Mentions context-dependent preferences but does not address cultural cycles.
  contribution: "PAHF provides a principled framework for implementing Odin’s personalization engine by enabling online learning from user feedback. The explicit memory module can store user preferences, such as spending categories or budget constraints. The dual-feedback mechanism can be adapted for Odin’s anomaly detection and budget recommendation modules. The four-phase evaluation protocol offers a template for testing Odin’s adaptation to evolving financial behavior. The theoretical guarantees on dynamic regret support robust performance under non-stationary user preferences."
  directly_justifies:
    - "Pre-action feedback is necessary to prevent initial personalization errors under partial observability."
    - "Post-action feedback is essential for correcting confidently wrong beliefs after preference drift."
    - "Combining both feedback channels yields the strongest personalization performance in dynamic environments."
    - "Explicit memory with dual feedback is critical for robust continual personalization without pre-existing data."
    - "The four-phase protocol isolates initial learning from adaptation to preference shifts."
  limits:
    - "Memory architecture uses simple SQLite/FAISS; more sophisticated backends could improve scalability."
    - "Human feedback is simulated and may not reflect real-world noise or inconsistencies."
    - "Benchmark tasks, especially online shopping, remain challenging for agents."
    - "Limited to one clarification question per task, which may not be sufficient for complex constraints."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was conducted. The domains of 'Behavioral Profiling & Classification', 'Spending Forecasting', 'Budget Recommendation', 'Anomaly Detection', 'Data Privacy & User Trust', and 'User Retention & Engagement' were flagged as relevant. Topic codes 5.B (Profile Dynamics), 6.A (Predictive Modeling), 7.D (Infeasibility Handling), 8.B (Anomaly Detection), 10.B (User Trust), and 11.A (Engagement Dynamics) were assigned high or medium relevance because the paper directly addresses learning from scratch, online adaptation, error correction, and user engagement through feedback. Topic 5.A (Financial Behavioral Profiles) is contextual, providing a general framework but not specific to finance. Topics 2.D (Filipino Spending Cycles) and other culturally specific topics were rejected as the paper does not address cultural or seasonal spending patterns. The paper is highly relevant to Odin as it provides a validated framework for continual learning and adaptation, which is central to personal finance management."
limitations:
  - "Memory architecture is simple; more sophisticated systems may be needed for real-world scale. [unacknowledged]"
  - "Assumes noise-free feedback; real human feedback is often noisy and inconsistent. [unacknowledged]"
  - "Benchmark tasks, especially online shopping, remain challenging for agents. [acknowledged]"
  - "Limited to one clarification question per task, which may not be sufficient for complex constraints. [acknowledged]"
remember_this:
  - "Pre-action feedback prevents initial personalization errors under partial observability."
  - "Post-action feedback is essential for correcting confidently wrong beliefs after preference drift."
  - "PAHF achieved the highest success rates across all phases and domains."
  - "Combining pre-action and post-action feedback with explicit memory yields robust performance."
  - "PAHF reduced initial error and enabled rapid adaptation to preference shifts."
```
---

## Paper 6: Tasawong et al_summarized.md

**Source File:** `Tasawong et al_summarized.md`

```yaml
paper_id: 10.48550/arXiv.2602.01618
designation: international-algorithm-specific
title: "SEA-Guard: Culturally Grounded Multilingual Safeguard for Southeast Asia"
authors: "Tasawong, P.; Ngui, J. G.; Aji, A. F.; Cohn, T.; Limkonchotiwat, P."
year: 2026
venue: arXiv
odin_topics:
  - 4.B
  - 5.C
  - 12.B
tldr: "Proposes SEA-Guard, a multilingual safeguard family for Southeast Asian languages and cultures, trained on an agentic data synthesis framework generating 870k culturally grounded safety samples per language across 8 SEA languages."
problem_and_motivation: "Existing safeguards are English-centric and fail to capture cultural nuances in Southeast Asian contexts, leading to weak performance on culturally sensitive content. Machine translation of English datasets misses regional subtleties, and native annotator scarcity limits data availability."
approach:
  - "Proposes an agentic data-generation framework with five components: input formulation, prompt/response generation, data annotation with MCRE, quality assurance, and model training."
  - "Uses Monte Carlo Reasoning Ensemble (MCRE) with N=10 stochastic reasoning passes for robust zero-shot safety classification, mapping a 5-way ordinal space to 3-way labels."
  - "Generates 870k samples per language across 8 SEA languages and 53 cultural categories using four LLMs for response diversity."
  - "Employs culture, topic, and usage classifiers for quality assurance, plus a bag-of-words deduplication procedure to remove lexically redundant samples."
  - "Trains three model variants (4B, 8B, 12B) via supervised fine-tuning on 870k samples per language with context length 8,192, batch size 6, and learning rate 5e-6."
  - "Evaluates on SEA-SafeguardBench (ITW and CG subsets), SEALS, SafeQA, and vision-text benchmarks using AUPRC as the primary metric."
findings:
  - "num: SEA-Guard-12B achieves 99.5% prompt and 75.2% response AUPRC on SEA-SafeguardBench, outperforming SOTA safeguards."
  - "num: SEA-Guard-12B outperforms Qwen3Guard-Gen 8B by 1.1 points on prompt classification and trails by only 0.6 points on response classification on generic benchmarks without training on generic safety data."
  - "num: SEA-Guard improves baseline vision-text safety performance in 6 out of 7 zero-shot settings."
  - "SEA-Guard models exhibit stronger human alignment (higher Spearman and Pearson correlations) than competing safeguards across severity levels."
  - "num: SEA-Guard remains robust under adversarial whitespace insertion attacks, maintaining high harmfulness scores while competitors degrade monotonically."
  - "num: Deduplication achieves comparable performance to the full 1M dataset with only 870k samples, reducing redundant patterns."
key_figures_tables:
  - "Table 1: SEA-Guard-12B achieves 79.5 prompt and 75.2 response AUPRC on SEA-SafeguardBench → outperforms all competitors."
  - "Table 2: SEA-Guard generalizes to generic safety benchmarks without training on generic data → competitive with SOTA."
  - "Table 3: SEA-Guard improves zero-shot vision-text safety in 6 of 7 benchmarks → emergent multimodal capability."
  - "Figure 3: SEA-Guard shows clearer separation across severity levels than competitors → better human alignment."
  - "Figure 4: SEA-Guard maintains high harmfulness under adversarial attacks → robust to surface-level perturbations."
  - "Figure 5: Performance scales with dataset size; deduplication matches full 1M performance at 870k → data efficiency."
key_equations:
  - equation: "h(x) = \\sum_{c \\in C_{safety}} s_c \\cdot P(\\hat{y}_{final} = c | R, x)"
    explanation: "Expected harmfulness score over ordinal safety labels."
  - equation: "P(C = c) \\propto 1 / \\text{freq}(c)"
    explanation: "Inverse-frequency sampling for balanced metadata coverage."
  - equation: "w_v = \\text{LMI}(v, y) = p(v,y) \\log(p(v,y) / (p(v) p(y)))"
    explanation: "Local mutual information for identifying lexically redundant training samples."
definitions:
  - term: "MCRE"
    definition: "Monte Carlo Reasoning Ensemble; robust zero-shot classification via multiple stochastic reasoning passes."
  - term: "SEA"
    definition: "Southeast Asia; region encompassing 11 countries with diverse languages and cultures."
  - term: "AUPRC"
    definition: "Area Under the Precision-Recall Curve; primary evaluation metric for safety classification."
  - term: "ITW"
    definition: "In-the-Wild; subset of SEA-SafeguardBench containing natural prompts."
  - term: "CG"
    definition: "Content Generation; subset of SEA-SafeguardBench containing generated prompts and responses."
critical_citations:
  - "[Zeng et al., 2024] — ShieldGemma baseline for safety moderation."
  - "[Inan et al., 2023] — LlamaGuard foundational safeguard model."
  - "[Shan et al., 2025] — SEALGuard for multilingual SEA safety."
  - "[Kumar et al., 2025] — PolyGuard for multilingual safety moderation."
  - "[Tan et al., 2025] — LionGuard-2 lightweight content moderator."
relevance:
  topics:
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Paper identifies gaps in existing safeguards for SEA languages and cultures, paralleling gaps in PFMS."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "contextual"
      justification: "MCRE classification methodology could inform financial behavioral profiling approaches."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Comprehensive evaluation framework (AUPRC, human alignment, adversarial robustness) is transferable to Odin module evaluation."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "contextual"
      justification: "Cultural grounding methodology for safety data can inform culturally aware financial practice modeling."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "contextual"
      justification: "Safeguards build user trust; paper's approach to safety and trust in AI systems is relevant."
  contribution: "This paper contributes a culturally grounded data synthesis framework and MCRE labeling methodology that can inform Odin's user classification and anomaly detection modules. The evaluation framework (AUPRC, human alignment, adversarial robustness) provides a template for assessing Odin's algorithmic modules. The deduplication approach offers a strategy for cleaning training data for financial behavior classification. The paper's treatment of cultural context in safety systems parallels the need for culturally aware financial recommendations in Odin."
  directly_justifies:
    - "MCRE provides a robust classification method for borderline cases in financial behavior profiling."
    - "Deduplication via bag-of-words reduces redundant patterns in training data without sacrificing coverage."
    - "Adversarial robustness testing is essential for anomaly detection systems in PFMS."
    - "Human alignment metrics (Spearman, Pearson) are critical for evaluating recommendation systems."
  limits:
    - "Paper focuses on content safety, not financial behavior or personal finance management."
    - "Cultural categories are broad (food, festivals, traditions) not specific to Filipino financial practices."
    - "Model evaluation does not include financial datasets or PFMS-specific tasks."
    - "Findings are specific to LLM safeguards and may not directly translate to classification of financial transactions."
  mapping_rationale: "Systematic scan of all 12 functional domains and their associated topic codes was performed. Domains flagged as relevant include: Existing Systems & Gaps (4.B, medium) due to the paper's explicit identification of limitations in current safeguards; Behavioral Profiling & Classification (5.C, contextual) because MCRE offers a classification approach transferable to financial profiling; and System Evaluation (12.B, medium) as the paper's multi-dimensional evaluation framework directly informs Odin module testing. The Filipino Cultural Context domain (2.A-D) was considered and rejected as low/contextual because the paper addresses general SEA cultural safety, not specifically Filipino financial practices. The Data Privacy & User Trust domain (10.A-B) was rated contextual—the paper discusses trust in AI safety but not PFMS-specific privacy. All other domains (Expense Categorization, Spending Forecasting, Budget Recommendation, Anomaly Detection, Mobile-First Design, User Retention, Savings & Debt Management) were rejected as not addressed. Overall, the paper provides methodological insights for culturally aware system design and evaluation rather than domain-specific PFMS contributions."
limitations:
  - "Covers only 8 of 700+ SEA languages and dialects, excluding Khmer, Lao, and Telugu."
  - "Did not experiment with 0.5B models; performance of smaller models may be unreliable for safety-critical applications."
  - "Vision-text benchmarks are English-only, limiting evaluation of multilingual vision capabilities."
  - "MCRE requires N=10 stochastic passes, incurring substantial computational overhead unsuitable for real-time use."
  - "Synthetic dataset may contain harmful content generated during data synthesis. [unacknowledged]"
remember_this:
  - "SEA-Guard-12B achieves 99.5% prompt AUPRC on cultural safety benchmarks."
  - "MCRE with N=10 stochastic passes improves human alignment over single-pass reasoning."
  - "Deduplication with bag-of-words achieves full 1M performance using only 870k samples."
  - "SEA-Guard generalizes to vision-text safety in 6 of 7 zero-shot benchmarks."
  - "Culturally grounded data synthesis is critical for multilingual safety systems."
```
---

## Paper 7: Aoun et al_summarized.md

**Source File:** `Aoun et al_summarized.md`

```yaml
paper_id: 10.3390/ijfs14020035
designation: international
title: "Understanding Millennials’ Financial Behavior: The Role of Fintech Adoption, Financial Literacy, and the Mediating Effect of Financial Attitudes in a Crisis-Affected Emerging Economy"
authors: "Aoun, D.; Rahal, R.; Sfeir, L.; Al Maalouf, N.J."
year: 2026
venue: "International Journal of Financial Studies"
odin_topics:
  - "1.C"
  - "2.A"
  - "5.A"
tldr: "Financial literacy and FinTech adoption positively influence Lebanese millennials' financial behavior, with financial attitudes mediating the relationship between literacy and behavior in a crisis-affected emerging economy."
problem_and_motivation: "The study aims to understand the joint influence of financial literacy, FinTech adoption, and financial attitudes on millennials' financial behavior in Lebanon, where economic crisis and institutional collapse have altered traditional financial dynamics. Existing research lacks integrated models and empirical evidence from crisis-affected emerging markets. This study fills that gap by examining how these factors interact in a fragile economy."
approach:
  - "Quantitative survey of 390 Lebanese millennials using self-report questionnaires with five-point Likert scales."
  - "Structural equation modeling (SEM) was applied to test direct and mediating effects among FinTech adoption, financial literacy, financial attitude, and financial behavior."
  - "Confirmatory factor analysis validated the measurement model, and reliability and validity were assessed using Cronbach's alpha, composite reliability, AVE, and HTMT ratio."
  - "The study adopted Behavioral Finance Theory as the theoretical framework to ground the hypothesized relationships."
findings:
  - "num: FinTech adoption positively predicts financial behavior (β=0.144, p<0.001)."
  - "num: Financial literacy positively predicts financial behavior (β=0.337, p<0.001)."
  - "num: Financial attitude positively predicts financial behavior (β=0.414, p<0.001)."
  - "num: Financial literacy positively predicts financial attitude (β=0.681, p<0.001)."
  - "Financial attitude partially mediates the relationship between financial literacy and financial behavior."
key_figures_tables:
  - "Figure 2: Path diagram showing standardized coefficients for all hypothesized relationships → all paths significant."
  - "Table 7: SEM regression results with coefficients and p-values → direct and mediated effects confirmed."
  - "Table 5: Reliability coefficients (α and ω) all above 0.86 → good internal consistency."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "BFT"
    definition: "Behavioral Finance Theory, which emphasizes psychological and cognitive factors in financial decision-making."
  - term: "SEM"
    definition: "Structural Equation Modeling, a multivariate statistical technique for testing causal relationships."
  - term: "FinTech"
    definition: "Digital financial technologies such as mobile banking, e-wallets, and online payment systems."
  - term: "AVE"
    definition: "Average Variance Extracted, a measure of convergent validity."
  - term: "HTMT"
    definition: "Heterotrait-Monotrait ratio, a measure of discriminant validity."
critical_citations:
  - "[Lusardi & Mitchell, 2014] — foundational definition and importance of financial literacy."
  - "[Swacha-Lech & Solarz, 2021] — definition and determinants of FinTech adoption."
  - "[Aftab et al., 2025] — evidence on financial literacy and behavioral biases in FinTech adoption."
  - "[Maalouf et al., 2023] — prior evidence on financial literacy in Lebanon."
relevance:
  topics:
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "medium"
      justification: "Examines financial behavior of millennials, a core demographic for Odin."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "contextual"
      justification: "Provides context on culturally specific financial practices in Lebanon, but not Filipino."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Identifies behavioral profiles and the mediating role of attitudes, relevant for profiling."
  contribution: "This paper justifies the importance of integrating financial literacy and attitudinal factors into a PFMS like Odin. It supports the inclusion of behavioral profiling modules to understand user tendencies. The mediation effect suggests that Odin should not only provide financial education but also foster positive attitudes through UX design. The findings reinforce the need for FinTech adoption as a channel for behavioral improvement, aligning with Odin's mobile-first approach. Overall, the paper provides empirical evidence that behavioral factors are critical for financial management systems."
  directly_justifies:
    - "Financial literacy directly improves financial behavior (β=0.337)."
    - "Financial attitudes mediate the effect of literacy on behavior."
    - "FinTech adoption positively influences behavior in crisis contexts."
    - "Behavioral finance theory applies in emerging economies."
  limits:
    - "Cross-sectional design limits causal inference."
    - "Self-reported data may introduce social desirability bias."
    - "Sample is not representative of all Lebanese millennials."
    - "Lack of objective measures for financial literacy and behavior."
    - "Crisis-specific constructs like institutional trust were not included."
  mapping_rationale: "I systematically scanned all 12 functional domains and their associated topic codes. The paper was flagged as relevant for domains related to financial behavior and profiling: 1.C and 5.A are assigned medium relevance because the paper provides empirical evidence on financial behavior and profiling that can inform Odin's design. 2.A is contextual as it discusses cultural practices but not specific to Filipino culture. Borderline cases: the paper touches on FinTech adoption, which could relate to 4.A or 9.A, but it does not address system gaps or mobile design principles, so these were rejected. Similarly, 6.A/B (forecasting) and 8.A/B (anomaly detection) were rejected as the paper does not discuss predictive modeling. 7.A-D (budget recommendation) were not addressed. The overall relevance is moderate; the paper offers foundational insights into behavioral mechanisms that can inform Odin's financial literacy and attitude integration modules."
limitations:
  - "Cross-sectional design limits tracking changes in financial behavior over time."
  - "Reliance on self-reported surveys may reflect perceived tendencies rather than actual behavior."
  - "Sample is limited to Lebanese millennials, reducing generalizability."
  - "Measurement of financial literacy and behavior relied on subjective Likert-scale items, not objective tests."
  - "Crisis-specific variables such as institutional trust and perceived risk were not included [unacknowledged]."
remember_this:
  - "Financial attitude strongly mediates the link between literacy and behavior."
  - "Financial literacy is a stronger predictor than FinTech adoption for behavior."
  - "The study provides empirical evidence from a crisis-affected emerging economy."
  - "Positive financial attitudes are crucial for translating knowledge into action."
  - "FinTech adoption contributes positively but with a smaller effect size."
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
paper_id: 10.1016/j.mex.2026.103962
designation: international-algorithm-specific
title: Transforming financial documents into credit decisions using explainable artificial intelligence and optical character recognition
authors: Malave, S.; Khemani, B.; Patil, H.; Nandurkar, S.; Nandurkar, O.; Nayak, A.
year: 2026
venue: MethodsX
odin_topics:
  - "10.A"
  - "10.B"
tldr: A document-driven framework integrates OCR, XGBoost, and XAI (SHAP, LIME) for interpretable credit scoring, achieving high accuracy but with limited direct application to personal finance management.
problem_and_motivation: Automated credit scoring systems using complex models lack transparency, raising fairness and regulatory concerns. Existing methods also underutilize unstructured data from financial documents. A unified framework is needed to combine document intelligence, predictive accuracy, and explainability.
approach:
  - Extracts data from applicant documents (Aadhaar, PAN, salary slips, bank statements) using EasyOCR, PyPDF2, and PdfPlumber.
  - Converts extracted data into a structured JSON, performs cleaning, normalization, and cross-verification.
  - Engineers 15 financial and behavioural features (e.g., income stability, bounce count) from the extracted data.
  - Trains an XGBoost model on a public Kaggle dataset (10,000 instances) to predict a continuous credit score.
  - Employs SHAP for global feature importance and LIME for local, instance-specific explanations of predictions.
  - Integrates a rule-based decision layer for loan eligibility, interest rate, and amount, followed by a human-in-the-loop review.
findings:
  - "num: XGBoost achieved 92.5% accuracy, outperforming LightGBM (90.8%), Logistic Regression (91%), Random Forest (87%), and LSTM (81%)."
  - "num: XGBoost yielded the lowest MAE (13.71) and RMSE (18.87), indicating high prediction consistency."
  - SHAP analysis showed income stability and average monthly credit positively correlate with credit scores.
  - Bounce count and obligation-to-income ratio were identified as strong negative contributors to credit scores.
  - LIME provided consistent local explanations, highlighting feature impacts on individual predictions.
  - The integrated XAI approach enhances transparency and supports regulatory compliance.
key_figures_tables:
  - "Figure 1: Overview of the proposed end-to-end document-driven credit scoring framework. → Shows integration from document input to final decision."
  - "Table 2: Description of the 15 engineered features used for credit risk prediction. → Lists financial and behavioral attributes used as model input."
  - "Figure 8: Regression performance comparison across models based on MAE and RMSE. → XGBoost has the lowest error values."
  - "Figure 11: SHAP beeswarm plot showing global feature importance. → Visualizes positive and negative feature contributions."
key_equations:
  - equation: "AverageUsableSalary = (1/N) * Σ(Si - EMIi)"
    explanation: "Calculates disposable income after loan repayments."
  - equation: "Accuracy = (TP + TN) / (TP + TN + FP + FN)"
    explanation: "Proportion of correctly classified instances."
definitions:
  - term: "XAI"
    definition: "Explainable Artificial Intelligence."
  - term: "OCR"
    definition: "Optical Character Recognition."
  - term: "SHAP"
    definition: "SHapley Additive exPlanations."
  - term: "LIME"
    definition: "Local Interpretable Model-agnostic Explanations."
critical_citations:
  - "[Nwafor et al., 2024] — Proposes hybrid ML for credit decisions."
  - "[Nallakaruppan et al., 2024] — Reviews XAI for financial decision support."
  - "[Kozodoi et al., 2022] — Discusses fairness in credit scoring."
relevance:
  topics:
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "contextual"
      justification: "Paper mentions document deletion and role-based access but does not deeply analyze privacy in PFMS."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "medium"
      justification: "Provides a framework for transparent decision-making using SHAP and LIME, directly applicable to building user trust."
  contribution: "The paper's method for integrating data extraction and XAI can inform Odin's data handling module to build user trust through transparency. Its use of SHAP and LIME offers a blueprint for explaining complex financial predictions in a personal finance context. However, the focus on credit scoring for lenders means the framework is not directly transferable to Odin's core PFMS functions."
  directly_justifies:
    - "Combining explainable models with feature engineering improves transparency for users."
    - "XGBoost is a robust model for structured financial data, achieving high accuracy."
    - "SHAP and LIME can provide consistent global and local explanations of model predictions."
  limits:
    - "The study is specific to credit scoring and not personal finance management."
    - "The model is trained on a public dataset, not on real-world or Philippine-specific financial data."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated canonical topic codes was performed. The relevance is primarily contextual or medium. The domain 'Data Privacy & User Trust' was flagged as relevant, specifically topic 10.A (contextual) for its mention of data handling and 10.B (medium) for its strong focus on XAI to build trust. The papers on 'Existing Systems & Gaps' (4.A, 4.B) were considered but rejected as the paper proposes a new system, not an analysis of existing ones. Domains like 'Spending Forecasting', 'Budget Recommendation', and 'Anomaly Detection' were considered and rejected as the paper's scope is credit risk, not personal budgeting or spending analytics. The Filipino cultural domains (e.g., 2.A, 2.B) were considered and rejected due to the study's Indian context. Overall, the paper's contribution is tangentially relevant to Odin, primarily as a reference for implementing explainable AI to build user trust, rather than for its core PFMS functionalities."
limitations:
  - "Dependency on OCR accuracy, which varies with document quality and type. [unacknowledged]"
  - "Training on a structured dataset may not capture the full diversity of real-world financial data. [unacknowledged]"
  - "SHAP and LIME may not capture all complex model interactions. [unacknowledged]"
remember_this:
  - "XGBoost achieved 92.5% accuracy for credit scoring."
  - "SHAP and LIME provide global and local explanations for predictions."
  - "The framework integrates document data extraction with machine learning."
  - "Feature engineering is critical for translating raw data into predictive inputs."
  - "Explainability enhances transparency in financial decision-making systems."
```
---

## Paper 10: Vinitha et al_summarized.md

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

## Paper 11: Oliveira_summarized.md

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

## Paper 12: Amado_summarized.md

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

## Paper 13: Chowdhury T. et al_summarized.md

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

## Paper 14: Tian et al_summarized.md

**Source File:** `Tian et al_summarized.md`

```yaml
paper_id: 10.3389/frai.2026.1726900
designation: international-algorithm-specific
title: Marketing-AutoM3L: domain-aware automated machine learning for financial customer analytics
authors: Tian, Y.; Shao, W.; Deng, Z.
year: 2026
venue: Frontiers in Artificial Intelligence
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
  - 8.A
  - 8.B
  - 10.A
tldr: An automated ML framework using LLMs for domain-aware pipeline construction in financial customer analytics, improving accuracy by 1.4% to 5.4% over existing AutoML.
problem_and_motivation: Generic AutoML systems lack domain-specific feature engineering capabilities essential for financial customer analytics, requiring manual intervention. Existing approaches force a trade-off between suboptimal generic solutions and resource-intensive manual customization. Business stakeholders with customer expertise cannot directly translate requirements into predictive pipelines, creating a critical gap.
approach:
  - The framework processes raw customer datasets and natural language directives through five stages.
  - Data modality recognition uses LLMs to classify attribute types and semantic meanings.
  - Domain-aware feature engineering automatically computes RFM scores, CLV projections, and engagement metrics.
  - Model architecture selection is guided by data characteristics and business requirements.
  - Multimodal pipeline construction and training configuration optimization complete the automated workflow.
findings:
  - num: Accuracy improvements of 1.4% to 5.4% in ROC-AUC over baseline AutoML methods across five datasets.
  - num: Pipeline development time reduced by 6.7× compared to manual approaches (23.4 min vs 156.9 min).
  - num: Domain-specific feature engineering contributes 3.3% to 3.6% ROC-AUC improvement in ablation studies.
  - The framework achieves optimal performance with moderate parameter counts, reducing unnecessary complexity.
  - RFM (Recency, Frequency, Monetary) features dominate prediction performance across all datasets.
key_figures_tables:
  - Figure 1: Framework architecture showing Intelligent Processing and Knowledge Supplementation modules → LLM-driven pipeline automation for customer analytics.
  - Figure 5: Performance comparison across datasets and methods → Marketing-AutoM3L consistently achieves highest ROC-AUC and F1 scores.
  - Figure 7: Execution time comparison → Marketing-AutoM3L achieves 6.7× speedup over manual pipeline development.
  - Table 2: Main experimental results → Comprehensive performance metrics demonstrate superiority over all baselines.
key_equations:
  - equation: R_i = t_current - max(s_1, s_2, ..., s_n), F_i = n, M_i = \sum_{j=1}^{n} a_j
    explanation: RFM metrics computation for recency, frequency, and monetary value.
  - equation: CLV_{prob,i} = \sum_{t=1}^{T} \frac{AOV_i \times PF_i \times r_i^t}{(1+d)^t}
    explanation: Probabilistic CLV projection incorporating customer retention probability.
  - equation: E_i(t) = \sum_{k=1}^{K} w_k \sum_{\tau=0}^{W} I_{i,k}(t-\tau) \cdot e^{-\lambda \tau}
    explanation: Engagement score aggregating weighted interaction signals over time.
definitions:
  - term: RFM
    definition: Recency-Frequency-Monetary framework for customer segmentation based on transaction behavior.
  - term: CLV
    definition: Customer Lifetime Value projection estimating total future value from a customer.
  - term: AutoML
    definition: Automated Machine Learning for automating pipeline construction without manual coding.
  - term: ROC-AUC
    definition: Area Under the Receiver Operating Characteristic Curve for classification performance.
critical_citations:
  - "[Luo et al., 2024] — First AutoM3L framework using LLMs as controllers."
  - "[Jain et al., 2023] — Comprehensive deep learning for customer churn prediction."
  - "[Qi et al., 2023] — Efficient RFM pattern mining algorithm foundation."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Domain-aware feature engineering automatically generates RFM and engagement metrics.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: Feature filtering and construction components inform category design.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Direct comparison with existing AutoML systems demonstrates limitations.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies lack of domain-specific feature engineering in generic AutoML.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: RFM and engagement scoring quantify behavioral patterns for customer classification.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: medium
      justification: Automated feature engineering reduces manual effort in cold-start scenarios.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Model selection and multimodal fusion for behavior prediction.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: End-to-end pipeline construction for churn prediction and CLV estimation.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Temporal processing and engagement trend features for behavioral forecasting.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Churn prediction shares methodological overlap with anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Declining engagement trends are predictive of anomalies.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Framework processes customer data, but privacy not explicitly addressed.
  contribution: "Marketing-AutoM3L provides an automated feature engineering module for Odin's expense categorization (3.A) by computing RFM and engagement metrics directly from transaction data. The LLM-driven pipeline automation addresses Odin's gap analysis (4.B) by demonstrating how existing AutoML systems lack domain-specific capabilities. The framework's behavioral profiling (5.A) and forecasting (6.A) components offer validated approaches for customer behavior prediction in Odin. The experimental evaluation (12.A) provides benchmarking methodology for assessing Odin's algorithmic modules. The ablation studies quantify the value of domain-aware feature engineering, supporting Odin's design decisions for automated financial analytics."
  directly_justifies:
    - "Domain-specific RFM and CLV feature engineering improves prediction accuracy by 3.3% to 3.6%."
    - "LLM-driven pipeline automation reduces development time by 6.7× compared to manual approaches."
    - "Multimodal data integration provides 1.1% to 3.6% ROC-AUC gains over single-modality baselines."
    - "Natural language directives enable business stakeholders to configure pipelines without ML expertise."
  limits:
    - "Relies on proprietary GPT-4 API, raising reproducibility and cost concerns."
    - "Validation primarily on classification tasks, limited exploration of regression or optimization domains."
    - "Customer data temporal constraints not fully validated across all dataset types."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes identified several areas of relevance. The Expense Categorization domain (3.A, 3.B) is highly relevant because the framework automatically generates domain-specific features including RFM metrics and engagement scores. The Existing Systems domain (4.A, 4.B) is highly relevant as the paper directly compares against generic AutoML systems and identifies their limitations in domain-specific contexts. Behavioral Profiling (5.A, 5.B, 5.C) is highly relevant for RFM-based customer segmentation and engagement scoring. Spending Forecasting (6.A, 6.B) is highly relevant for CLV projection and temporal behavioral prediction. Anomaly Detection (8.A, 8.B) is low relevance as churn prediction shares methodological overlap but is not the primary focus. Data Privacy (10.A) is contextual only as the framework processes data but privacy considerations are not addressed. Mobile-First Design (9.A, 9.B), User Retention (11.A, 11.B), System Evaluation (12.A, 12.B, 12.C), Savings & Debt Management (13.A, 13.B, 13.C), and Filipino Cultural Context (1.A, 1.B, 1.C, 2.A, 2.B, 2.C, 2.D) were considered and rejected due to no direct relevance to the paper's algorithmic contribution or focus on international financial customer analytics. The paper's overall relevance to Odin is moderate-to-high, providing validated automated feature engineering and pipeline construction methodologies for personal finance systems."
limitations:
  - "GPT-4 API dependency creates reproducibility concerns. [unacknowledged]"
  - "High-end GPU infrastructure may not be accessible to all organizations. [unacknowledged]"
  - "Evaluation limited to churn prediction tasks, not validated for budget recommendation or optimization domains."
  - "Natural language directive interpretation quality depends on LLM performance consistency."
  - "Temporal constraints and data leakage prevention not extensively validated."
remember_this:
  - "Domain-aware feature engineering provides 3.3% to 3.6% accuracy gains over generic approaches."
  - "LLM-driven automation reduces pipeline development time by 6.7× compared to manual methods."
  - "RFM and engagement metrics are the most predictive features for customer behavior forecasting."
  - "Natural language interfaces enable non-technical stakeholders to configure predictive pipelines."
  - "Multimodal data integration improves prediction accuracy by 1.1% to 3.6% over single-modality baselines."
```
---

## Paper 15: Krishnan & Sreeja_summarized.md

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

## Paper 16: Rajulapati et al_summarized.md

**Source File:** `Rajulapati et al_summarized.md`

```yaml
paper_id: "10.47738/ijaim.v6i2.123"
designation: "international-algorithm-specific"
title: "Continual Learning for Human–AI Collaborative Learning Analytics under Behavioral Drift"
authors: "Rajulapati, A.; V, S.; Prasad, S.R."
year: 2026
venue: "International Journal for Applied Information Management"
odin_topics:
  - "5.A"
  - "6.A"
  - "8.A"
  - "10.A"
  - "10.B"
  - "12.A"
  - "12.B"
  - "12.C"
tldr: "Drift-aware continual learning improves predictive stability, calibration, and fairness under semester-to-semester behavioral changes in learning analytics."
problem_and_motivation: "Predictive models in adaptive learning analytics degrade over semesters due to non-stationarity, undermining reliability and fairness. Existing pipelines lack explicit drift monitoring and controlled updating, risking stale risk flags and inequitable outcomes."
approach:
  - "Longitudinal 14-semester panel of LMS traces and assessment records (812–936 students per term) was used."
  - "Drift was quantified via KL divergence per behavioral feature, with a threshold-based trigger for model updates."
  - "Continual learning used a memory-augmented objective with replay buffer and parameter regularization to balance plasticity and stability."
  - "Evaluation followed a semester-forward protocol, comparing static, periodic retraining, and drift-aware continual policies."
  - "Metrics included macro-F1, AUROC, calibration error, decision quality, and subgroup fairness gaps."
findings:
  - "num: Drift-aware continual learning improved mean macro-F1 from 0.706 (static) to 0.742."
  - "num: Worst-semester macro-F1 increased from 0.652 to 0.711, reducing temporal variance (std from 0.030 to 0.015)."
  - "num: Expected calibration error reduced from 0.056 to 0.039, and risk precision improved from 0.62 to 0.69."
  - "num: Mean subgroup recall gap decreased from 0.118 to 0.082 under drift-aware updating."
  - "Ablation showed intermediate drift thresholds and moderate replay memory (4,000 records) optimize robustness with 1-2 updates per semester."
key_figures_tables:
  - "Figure 7: Macro-F1 across semesters → Drift-aware continual learning maintains flatter performance after regime shift."
  - "Figure 8: Calibration error over weeks → Drift-aware updates reduce miscalibration spikes during drift episodes."
  - "Figure 9: Subgroup recall gap across semesters → Continual learning mitigates growing disparities under drift."
  - "Figure 10: Drift threshold vs. robustness → Intermediate threshold maximizes worst-semester performance with moderate update rate."
  - "Table 7: Aggregate performance summary → Drift-aware continual achieves highest mean and worst-case F1, with lowest variance."
  - "Table 8: Decision quality → Lower ECE, higher precision/recall, and fewer threshold changes per semester."
key_equations:
  - equation: "D_{KL}(P_t || P_{t+1}) = \sum_k P_t(k) \log \frac{P_t(k)}{P_{t+1}(k)}"
    explanation: "KL divergence quantifies drift magnitude between consecutive semesters."
  - equation: "\min_{\theta} L_{t+1}(\theta) + \lambda \sum_j \omega_j (\theta_j - \theta_{t,j})^2"
    explanation: "Continual learning objective balances new loss and parameter importance."
  - equation: "z_t = (\delta_t - \mu_0) / \sigma_0"
    explanation: "Standardized monitoring statistic for drift alarms."
definitions:
  - term: "Concept drift"
    definition: "Change in joint distribution of inputs and targets over time."
  - term: "Continual learning"
    definition: "Sequential model updating while mitigating catastrophic forgetting."
  - term: "Replay buffer"
    definition: "Memory storing representative historical samples to preserve past knowledge."
  - term: "Expected calibration error (ECE)"
    definition: "Measure of alignment between predicted probabilities and observed outcomes."
critical_citations:
  - "[Gama et al., 2014] — Foundational survey on concept drift adaptation."
  - "[Delange et al., 2021] — Comprehensive survey on continual learning methods."
  - "[Lu et al., 2018] — Review of learning under concept drift with lifecycle framing."
  - "[Deho et al., 2024] — Empirical study on dataset drift impact on fairness in learning analytics."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "contextual"
      justification: "Uses behavioral profiling concepts, but for student learning not financial behavior."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "contextual"
      justification: "General predictive modeling methods applicable to forecasting, though not spending-specific."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "contextual"
      justification: "Drift detection techniques share methodological overlap with anomaly detection."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "medium"
      justification: "Explicitly includes privacy safeguards and pseudonymization in deployment."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses transparency, fairness, and governance, which underpin user trust."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Presents a rigorous semester-forward evaluation protocol with multiple reliability metrics."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Evaluates the continual learning module against baselines with detailed performance analysis."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "high"
      justification: "Provides methodology for temporal validation, calibration, and fairness assessment applicable to recommendation evaluation."
  contribution: "The paper's drift-aware continual learning approach can inform Odin's forecasting module by enabling adaptive model updates under shifting spending patterns. Its calibration and fairness evaluation framework offers a template for assessing Odin's anomaly detection and budget recommendation modules. The governance-aware monitoring with privacy safeguards directly supports Odin's data privacy and user trust design. The semester-forward evaluation protocol provides a model for longitudinal testing of Odin's predictive components."
  directly_justifies:
    - "Drift-triggered updates reduce performance collapse and stabilize predictions over time."
    - "Continual learning with replay buffers preserves historical patterns while adapting to new data."
    - "Calibration monitoring at test time improves decision quality for fixed intervention capacity."
    - "Fairness auditing under drift prevents widening subgroup disparities."
  limits:
    - "Single-institution dataset may limit generalizability to other educational contexts."
    - "Computational overhead of replay buffer and drift monitoring not fully quantified for real-time deployment."
    - "Fairness evaluation limited to recall gaps; other fairness metrics not explored. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The System Evaluation domain (12.A, 12.B, 12.C) was flagged as highly relevant due to the paper's rigorous semester-forward evaluation, calibration, and fairness metrics, which directly inform Odin's evaluation practices. Data Privacy & User Trust (10.A, 10.B) received medium relevance because the paper explicitly includes ethical safeguards and fairness monitoring, aligning with Odin's trust-building requirements. Behavioral Profiling (5.A) and Predictive Modeling (6.A) were assigned contextual relevance given the use of student behavioral data and forecasting techniques, though not specific to finance. Anomaly Detection (8.A) was contextual due to drift detection methods that share algorithmic similarities with anomaly detection. Topics related to Filipino cultural context, expense categorization, existing systems, budget recommendation, mobile-first design, and savings/debt management were rejected as the paper does not address personal finance or Philippine-specific conditions. Overall, the paper provides methodological insights that are transferable to Odin's design but is not directly applicable to financial domain specifics."
limitations:
  - "Single-institution dataset may limit generalizability to other educational contexts."
  - "Computational overhead of replay buffer and drift monitoring not fully quantified for real-time deployment."
  - "Fairness evaluation limited to recall gaps; other fairness metrics not explored. [unacknowledged]"
remember_this:
  - "Drift-aware continual learning improves mean macro-F1 from 0.706 to 0.742."
  - "Worst-semester macro-F1 increases from 0.652 to 0.711, reducing variance."
  - "Calibration error drops from 0.056 to 0.039 with drift-aware updates."
  - "Subgroup recall gap decreases from 0.118 to 0.082 under continual learning."
```
---

## Paper 17: Jiang et al_summarized.md

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
  - 5.C
  - 6.B
  - 7.A
  - 7.B
  - 8.C
  - 11.B
  - 12.B
  - 12.C
  - 13.A
  - 13.B
tldr: Integrates feature selection, stratified clustering, and meta-learning into a unified Causal User Profiling pipeline that estimates heterogeneous treatment effects and classifies users into four causal response types.
problem_and_motivation: Conventional user profiling is descriptive and correlation-based, lacking the causal reasoning needed to predict how users respond to interventions. This limits personalization and targeting in systems like internet lending, where understanding treatment responsiveness is critical.
approach:
  - Uses a multi-stage feature selection combining Information Value, Causal Forest importance, Population Stability Index, and Stepwise refinement.
  - Employs stratified clustering with a C2 replacement strategy to stabilize weak clusters and harmonize local heterogeneity with global patterns.
  - Estimates Conditional Average Treatment Effects using meta-learners (S, T, X, R, DR) and Causal Forests, with Logistic Regression as base learner.
  - Implements a Four-Type Response Segmentation module (Persuadable, Sure Thing, Lost Cause, Do-Not-Disturb) based on potential outcomes and uplift scores.
  - Evaluates performance using Area Under the Uplift Curve (AUUC) across six monthly rolling deployment windows.
findings:
  - "num: Hybrid feature selection increases AUUC by 25-30% over the baseline."
  - "num: C2 clustering strategy provides an additional 10-12% gain in AUUC."
  - "num: DR-Learner with Logistic Regression adds a further 5-8% uplift."
  - "num: The integrated CUP framework yields a 45-50% higher AUUC than the baseline."
  - The X-Learner demonstrated the most consistent improvement under clustering, while DR-Learner showed higher variance.
  - Clustering based on causal features produced more consistent gains than clustering based on predictive features alone.
key_figures_tables:
  - "Figure 5b: Joint distribution of potential outcomes (y0, y1) → Illustrates the four decision regions for response types."
  - "Figure 6a: Boxplots of AUUC across six feature sets → IV+Causal+Stepwise yields highest stability."
  - "Figure 7b: Comparison of clustering strategies (Direct, C1, C2) → C2 achieves the highest stability and lowest variance."
  - "Figure 8: Heatmap of Meta-Learner × Base-Learner configurations → DR-Learner with Logistic Regression achieves the best balance."
  - "Figure 9: Cumulative gain curves comparing CUP pathway with baseline → CUP curve uniformly dominates."
key_equations:
  - equation: "u = p_1 - p_0"
    explanation: "Uplift score as difference in outcome probabilities under treatment and control."
  - equation: "WeightedAUUC = \\sum_{k=1}^K w_k \\cdot AUUC_k"
    explanation: "Weighted average of AUUC across clusters."
definitions:
  - term: "CUP"
    definition: "Causal User Profiling framework integrating causal inference and uplift modeling."
  - term: "HTE"
    definition: "Heterogeneous Treatment Effect, the variation in causal effects across individuals."
  - term: "CATE"
    definition: "Conditional Average Treatment Effect, expected causal effect conditional on observed features."
  - term: "AUUC"
    definition: "Area Under the Uplift Curve, a metric for evaluating uplift model ranking performance."
  - term: "DR-Learner"
    definition: "Doubly Robust Learner, a meta-learner combining outcome and propensity models."
critical_citations:
  - "[Athey & Imbens, 2016] — Foundational for recursive partitioning in HTE estimation."
  - "[Wager & Athey, 2018] — Introduced Causal Forests for consistent HTE estimation."
  - "[Künzel et al., 2019] — Established meta-learners for flexible CATE estimation."
  - "[Devriendt et al., 2018] — Emphasized upstream pipeline design impact on uplift performance."
  - "[Radcliffe & Surry, 2011] — Defined uplift and the four-type response taxonomy."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: "Introduces a causal taxonomy (Persuadable, Sure Thing, Lost Cause, Do-Not-Disturb) for behavioral profiling."
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: "Uplift modeling and response-type segmentation directly classify users into causal behavioral profiles."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: "Evaluates meta-learners and Causal Forests for estimating treatment effects on sequential user behavior."
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: "Provides a causal framework for understanding how users respond to financial interventions, relevant to budgeting."
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: "Causal profiling enables personalized budget recommendations based on predicted responsiveness."
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: contextual
      justification: "Clustering and profiling methods discussed could inform cold-start strategies for anomaly detection."
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: "Identifying Persuadables and avoiding Do-Not-Disturbs informs targeted engagement and retention strategies."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: "Component-wise ablation analysis quantifies marginal contributions of feature selection, clustering, and estimation."
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: "AUUC-based evaluation and temporal stability analysis are directly applicable to evaluating budget recommendation systems."
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: "The framework can be applied to segment users for targeted savings interventions based on causal responsiveness."
    - code: 13.B
      name: Debt Management in PFMS
      relevance: medium
      justification: "Applied to internet lending, the framework helps optimize debt management interventions."
  contribution: "This paper provides a reproducible causal user profiling pipeline (CUP) that can be directly adapted for Odin's behavioral profiling module. The four-type response taxonomy (Persuadable, Sure Thing, Lost Cause, Do-Not-Disturb) offers a clear framework for segmenting Filipino young professionals based on their causal responsiveness to financial interventions. The component-wise ablation analysis demonstrates that hybrid feature selection and C2 clustering can significantly improve the performance of Odin's budget recommendation and anomaly detection systems. The emphasis on temporal stability across repeated deployments is critical for designing reliable and trustworthy personal finance management systems. Finally, the DR-Learner with Logistic Regression configuration provides a balance of interpretability and performance suitable for Odin's mobile-first, data-privacy-sensitive context."
  directly_justifies:
    - "Causal user profiling enables moving from descriptive segmentation to predicting how users respond to financial interventions."
    - "Hybrid feature selection combining Information Value and causal importance improves uplift model stability and performance."
    - "The C2 replacement strategy stabilizes clustering by reverting to global predictions when local clustering introduces noise."
    - "The DR-Learner with Logistic Regression offers a favorable trade-off between robustness, interpretability, and performance."
    - "Component-wise ablation is essential for quantifying the marginal contribution of each pipeline module."
  limits:
    - "Analysis is based on data from a single Chinese digital lending platform, limiting external generalizability to the Philippine context."
    - "The treatment variable aggregates heterogeneous interventions (e.g., coupons, credit-line increases), obscuring intervention-specific mechanisms."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated canonical topic codes was performed. Domains relevant to user profiling (5.A, 5.C), forecasting (6.B), budgeting strategies (7.A, 7.B), anomaly detection baselines (8.C), engagement (11.B), system evaluation (12.B, 12.C), and savings/debt management (13.A, 13.B) were flagged. The paper's core contribution on CUP and uplift modeling directly addresses 5.A, 5.C, and 6.B with high relevance, as it provides a taxonomy and methodology for behavioral profiling and forecasting. It provides medium relevance to 7.A, 7.B, 11.B, 12.C, 13.A, and 13.B by offering a causal framework applicable to budgeting, engagement, evaluation, savings, and debt management. 8.C was flagged as contextual because the clustering strategies for profiling could be adapted for cold-start anomaly detection baselines. Domains related to Filipino cultural context (2.A-2.D), expense categorization (3.A-3.C), existing systems (4.A-4.B), mobile-first design (9.A-9.B), and data privacy (10.A-10.B) were considered and rejected as the paper does not address these topics. Borderline cases included 7.B (budget recommendation) and 13.A (savings), which are not explicitly studied but are directly enabled by the proposed causal profiling approach. Overall, the paper has high relevance for Odin's behavioral modeling and algorithmic modules, with contextual relevance for culturally agnostic design considerations."
limitations:
  - "Single-platform data limits generalizability to other contexts such as Philippine PFMS. [unacknowledged]"
  - "Aggregated treatment variable may obscure intervention-specific behavioral mechanisms. [unacknowledged]"
  - "Fairness, transparency, and ethical deployment of causal profiling are not addressed. [unacknowledged]"
  - "Temporal stability was assessed over only six months; longer-term stability remains untested."
remember_this:
  - "CUP framework provides 45-50% higher AUUC than conventional uplift modeling baselines."
  - "Hybrid feature selection increases AUUC by 25-30% over using all features."
  - "C2 clustering strategy adds 10-12% AUUC gain by stabilizing weak clusters."
  - "DR-Learner with Logistic Regression offers the best balance of performance and interpretability."
  - "Clustering is effective only when feature space encodes causally relevant information."
```
---

## Paper 18: Ma C. et al_summarized.md

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

## Paper 19: Heirene R. et al-2026a_summarized.md

**Source File:** `Heirene R. et al-2026a_summarized.md`

```yaml
paper_id: 10.1186/s12954-026-01402-4
designation: international-algorithm-specific
title: Development of lower-risk guidelines for online sports and race betting in Australia using objective behavioural data
authors: Heirene, R. M.; Chandrakumar, D.; Fahey, G.; Huynh, E. L. Y.; Gainsbury, S. M.
year: 2026
venue: Harm Reduction Journal
odin_topics:
  - 1.A
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 7.A
  - 7.C
  - 8.A
  - 9.A
  - 10.A
  - 13.A
tldr: Lower-risk guidelines for online sports betting using objective account data were developed, proposing limits on deposits, income percentage, active accounts, and betting variety to reduce gambling harm.
problem_and_motivation: Existing gambling guidelines rely on inaccurate self-reported data and apply generically across gambling types, missing activity-specific risks. Online wagering, which has unique risk factors, lacks empirically derived, objective guidelines. This study addresses this gap by using operator account data matched with harm measures to develop specific thresholds.
approach:
  - A survey including PGSI and GHM was linked to 12 months of objective wagering data for 1,647 Australian customers.
  - Behavioral indicators included spend, deposit frequency, deposit amount, income percentages, betting days, activity variety, and account count.
  - ROC curve analyses identified optimal cut-offs for eight indicators using Youden, sensitivity, and specificity maximization.
  - Logistic regression validated the predictive ability of cut-offs, controlling for demographics and other gambling.
  - Performance metrics were compared to existing guidelines from Dowling et al. (2021).
findings:
  - All eight behavioural indicators had acceptable AUCs (≥0.6) for harm classification except betting days per month.
  - Optimal thresholds were higher for GHM harm than PGSI harm, and higher than self-report-based guidelines.
  - Depositing more than 2% of monthly income and using more than two active accounts were the strongest unique predictors of harm.
  - Surpassing multiple limits exponentially increased odds of harm, with an 8-fold increase for surpassing all PGSI limits.
  - The proposed "2-2-4-4 Rule" provides clear, income-relative, and actionable advice for lower-risk wagering.
  - Young adults (≤25) required lower thresholds for all behavioural indicators, suggesting increased vulnerability.
key_figures_tables:
  - Table 2: Optimal cut-off values for PGSI and GHM harm with AUC, sensitivity, and specificity metrics → All indicators except betting days had AUC ≥0.6.
  - Table 3: Logistic regression showing exceeding limits increases odds of harm 2-7x → Depositing >2% income gave OR 3.78 for PGSI; >10% gave OR 7.10 for GHM.
  - Table 4: New limits outperformed Dowling et al. (2021) limits by 17.6–28.5% accuracy for GHM harm → Demonstrates value of objective data.
  - Table 5: 91.6% of harmed participants passed at least one proposed limit → Supports coverage of the four recommended limits.
  - Figure 2: Dose-response relationship between number of limits surpassed and harm odds → Surpassing all 8 limits gave OR 8.04 (PGSI) and 8.92 (GHM).
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: PGSI
    definition: Problem Gambling Severity Index – a screening measure for gambling-related harms.
  - term: GHM
    definition: Gambling Harm Measure – a 16-item scale assessing gambling impact across life domains.
  - term: AUC
    definition: Area Under the Receiver Operating Characteristic Curve – a measure of classification accuracy.
  - term: Youden index
    definition: A metric for selecting optimal cut-offs that balances sensitivity and specificity.
critical_citations:
  - "[Currie et al., 2017] — Established lower-risk gambling limits using longitudinal data."
  - "[Dowling et al., 2021] — Developed Australian-specific limits for various gambling activities."
  - "[Louderback et al., 2021] — Used objective account data to derive online gambling thresholds."
  - "[Heirene et al., 2021] — Found self-reported gambling behaviour is highly inaccurate."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Focuses on Australian online bettors, not Filipino young professionals.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Examines spend and deposit amounts as indicators of harm, applicable to expense tracking.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: Highlights importance of distinguishing absolute spend from income-relative spend.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: References existing gambling guidelines and their limitations, not PFMS systems.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Critiques reliance on self-reported data and generic guidelines, gaps that Odin can address.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Derives behavioural indicators (deposit frequency, accounts) that can define risk profiles.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: contextual
      justification: Discusses harm status classification but not cold-start profiling directly.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses ROC and logistic regression to classify harmed vs. unharmed groups.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: contextual
      justification: Identifies risk indicators but does not focus on forecasting future spending.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Provides income-relative spending limits, analogous to budget allocation advice.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: low
      justification: Does not propose optimization algorithms, but suggests percentage-based constraints.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Could inform anomaly detection by defining normal vs. risky behaviour thresholds.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: Discusses household income percentage, indirectly related to savings capacity.
  contribution: "This paper provides a rigorous methodology for deriving objective, activity-specific behavioural thresholds for financial risk, which can directly inform Odin's behavioural profiling module by defining high-risk spending patterns. Its dose-response analysis supports Odin's anomaly detection by establishing what constitutes a 'harmful' deviation from normal financial behaviour. The emphasis on income-relative metrics (e.g., 2% of income deposited) provides a principled basis for Odin's budget recommendation system to set dynamic, personalised constraints. The focus on multiple, interacting risk indicators aligns with Odin's need for holistic financial health assessment, moving beyond single-threshold rules. Finally, the call for actionable, mnemonic guidelines (e.g., '2-2-4-4 Rule') offers a model for how Odin can present its budget and savings recommendations to users in a memorable, practical format."
  directly_justifies:
    - "Depositing more than 2% of household income per month is a strong predictor of financial harm."
    - "Exceeding four deposits per month significantly increases odds of gambling harm."
    - "Using more than two active wagering accounts is a unique and significant risk indicator."
    - "A dose-response relationship exists; surpassing multiple limits compounds risk exponentially."
    - "Income-relative limits are more predictive than absolute spend thresholds."
  limits:
    - "Sample skewed towards more frequent bettors, which may overestimate thresholds."
    - "Data covers only one operator, missing gambling across multiple accounts."
    - "Generalizability to Filipino context requires cultural and economic adaptation."
    - "Self-reported harm measures may still have biases despite objective behaviour data."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was conducted. This paper was flagged as highly relevant to Behavioral Profiling & Classification (5.A) because it identifies objective behavioural indicators (deposit frequency, income percentage, account count) that define high-risk financial profiles, directly informing Odin's user classification. It is medium-relevant to Expense Categorization (3.A, 3.B) by distinguishing spend vs. deposit behaviours and highlighting the importance of income-relative metrics for expense tracking. It also provides medium relevance to Existing Systems & Gaps (4.A, 4.B) through its critique of self-report-based guidelines and generic limits, justifying Odin's need for objective, activity-specific personalization. The paper's methodological approach to deriving thresholds contributes contextually to Spending Forecasting (6.A) and Anomaly Detection (8.A), though it does not develop forecasting or detection algorithms themselves. It offers medium relevance to Budget Recommendation (7.A, 7.C) via income-relative spending limits analogous to budgeting constraints, and low relevance to Mobile‑First Design (9.A), Data Privacy (10.A), and Savings & Debt Management (13.A), as these are not central. Borderline cases included the deposit and spend indicators touching both Expense Categorization (3.A, 3.B) and Behavioral Profiling (5.A); these were resolved by prioritizing 5.A for the strongest predictive indicators (deposit frequency, account count) and 3.A for the spend/income metrics. The paper's emphasis on objective, operator-sourced data and dose-response relationships provides strong methodological grounding for Odin's data-driven modules."
limitations:
  - "Sample skewed towards more frequent bettors, potentially inflating threshold estimates. [unacknowledged]"
  - "Data from a single operator may not capture full gambling activity across all platforms. [unacknowledged]"
  - "Generalizability to Filipino young professionals requires cultural and economic validation. [unacknowledged]"
  - "Self-reported harm measures, although matched with objective data, still rely on participant honesty."
  - "The study does not test the causal impact of adhering to these guidelines on harm reduction."
remember_this:
  - "Exceeding 2% of income on deposits quadruples the odds of gambling harm."
  - "Using more than two active betting accounts is a unique risk indicator."
  - "Surpassing multiple limits exponentially increases harm risk, up to 8-fold."
  - "Objective spending data yields higher, more accurate thresholds than self-reports."
  - "Young adults need lower behavioural limits to mitigate harm risk."
```
---

## Paper 20: Chandana et al_summarized.md

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

## Paper 21: Pesa et al_summarized.md

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

## Paper 22: Gong_summarized.md

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
  - 8.B
  - 12.B
tldr: A systematic review of deep learning models for stock price prediction, tracing the evolution from LSTM and CNN-LSTM to Transformer and hybrid architectures, summarizing model principles, empirical comparisons, challenges, and future directions.
problem_and_motivation: Stock price prediction is crucial for quantitative finance but is highly challenging due to market volatility, non-linearity, and non-stationarity. Traditional and early machine learning methods fail to capture complex patterns, creating a need for more robust models. This review aims to systematically summarize the advancement from LSTM to Transformer architectures to guide researchers.
approach:
  - The paper conducts a systematic literature review of deep learning models for stock price prediction.
  - It covers RNN variants (LSTM, GRU), CNN, Transformer models, and hybrid architectures like CNN-LSTM and LSTM-Transformer.
  - The review analyzes model principles, advantages, disadvantages, and application scenarios.
  - It includes a comparative analysis of empirical studies, focusing on datasets, evaluation metrics (RMSE, MAE, MAPE, DA, R², Sharpe Ratio), and performance.
  - The paper identifies current challenges at the data, model, and deployment levels and discusses future research trends.
findings:
  - num: LSTM achieved a Sharpe ratio of 2.34 for S&P 500 constituents from 1992 to 2015, outperforming DNN and logistic regression.
  - num: Transformer models showed improved accuracy over CNN, RNN, and LSTM, with average MAE decreasing by approximately 20.73%, MSE by 34.84%, and MAPE by 25.63%.
  - num: The LSTM-Transformer hybrid model reduced MAE and RMSE by over 50% compared to parent models and achieved an R² of 0.9618, higher than LSTM (0.8430) and Transformer (0.7763).
  - Stock prediction models have evolved from single models (LSTM) to hybrid and multimodal fusion architectures.
  - Challenges include data noise, overfitting, model interpretability, computational efficiency, and deployment in dynamic markets.
  - Future directions include multimodal information fusion, interpretable AI, real-time adaptive learning, and automated model architecture search.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: LSTM
    definition: Long Short-Term Memory, an RNN variant using gating mechanisms to handle long-term dependencies.
  - term: GRU
    definition: Gated Recurrent Unit, a simpler RNN variant with similar performance to LSTM but higher computational efficiency.
  - term: CNN
    definition: Convolutional Neural Network, a model that uses local receptive fields and hierarchical feature extraction, applied to time series for trend extraction.
  - term: Transformer
    definition: A model architecture using a self-attention mechanism to capture long-range dependencies and enable parallel computing.
  - term: RMSE
    definition: Root Mean Squared Error, a metric reflecting the overall deviation between predicted and actual values, sensitive to large errors.
  - term: MAE
    definition: Mean Absolute Error, a metric showing the average absolute deviation, reflecting prediction stability.
  - term: MAPE
    definition: Mean Absolute Percentage Error, the average percentage error between predicted and actual values.
  - term: DA
    definition: Directional Accuracy, a metric reflecting the accuracy of predicting the direction of stock price changes.
  - term: Sharpe Ratio
    definition: A metric reflecting the relationship between returns and risks, with higher values indicating better risk-adjusted returns.
critical_citations:
  - "[Fischer & Krauss, 2018] — Benchmarking LSTM in financial market predictions."
  - "[Mehtab & Sen, 2021] — Proposing a CNN-LSTM hybrid for stock prediction."
  - "[Wang et al., 2022] — Demonstrating Transformer's superior prediction accuracy."
  - "[Zhao et al., 2025] — Introducing an LSTM-Transformer hybrid with strong results."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: This paper is a comprehensive review of predictive models relevant to financial forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: The review extensively covers LSTM, Transformer, and hybrid algorithms for sequential time series prediction.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: The paper discusses model sensitivity to noise and anomalies, which is relevant for detecting unusual spending patterns.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: The paper details evaluation metrics (RMSE, MAE, Sharpe Ratio) and compares model performance, relevant for system evaluation.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: The paper mentions "black box" interpretability concerns, which contextualize the importance of user trust.
  contribution: "This review provides a technical roadmap for selecting and evaluating deep learning models for sequential financial data prediction. It directly informs the design of Odin's forecasting and anomaly detection modules by comparing the strengths and weaknesses of LSTM, Transformer, and hybrid models. The systematic comparison of evaluation metrics validates the choice of performance indicators for Odin's algorithmic modules. The discussion of model challenges and future trends, such as multimodal fusion and interpretability, highlights areas for advanced feature engineering in Odin."
  directly_justifies:
    - "LSTM models are reliable benchmarks for medium and short-term prediction tasks."
    - "Transformer models demonstrate superior performance in capturing long-range dependencies."
    - "Hybrid LSTM-Transformer models achieve a balance of higher accuracy and interpretability."
    - "Deep learning models outperform traditional statistical methods in stock price prediction."
  limits:
    - "The review is specific to stock price prediction, which may differ from personal spending data."
    - "The paper primarily focuses on quantitative finance, not personal finance management."
    - "The review does not cover user-specific constraints or behavioral profiling."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to the Spending Forecasting domain (6.A, 6.B) because it reviews state-of-the-art predictive algorithms (LSTM, Transformer) for time series data. It also has medium relevance to Anomaly Detection (8.B) as it discusses model sensitivity to noise and abnormal fluctuations, and to System Evaluation (12.B) due to its detailed comparison of evaluation metrics. Other domains like Expense Categorization (3.A) and Behavioral Profiling (5.A) were considered but rejected as the paper does not address spending categories or user behavior classification. The paper's focus on algorithmic performance in finance, not personal finance, places it as a contextual or low relevance for topics like Mobile-First Design (9.A) and Data Privacy (10.A), where it only tangentially mentions interpretability. Overall, the paper's strongest contribution to Odin is as a reference for forecasting and anomaly detection algorithm selection."
limitations:
  - "The review is specific to stock price prediction and may not generalize directly to personal spending data."
  - "It primarily focuses on model performance and does not address practical system integration or user experience."
  - "The paper does not consider resource constraints of mobile-first applications."
  - "Long-term adaptability and real-time learning challenges are identified but not resolved. [unacknowledged]"
remember_this:
  - "LSTM excels in short-term prediction and generating high Sharpe ratio signals."
  - "Transformer models significantly improve accuracy for long-range dependencies."
  - "Hybrid LSTM-Transformer models offer superior accuracy and stability."
  - "Deep learning models surpass traditional methods in financial time series forecasting."
```
---

## Paper 23: Paz et al_summarized.md

**Source File:** `Paz et al_summarized.md`

```yaml
paper_id: 10.3390/math14030429
designation: international-algorithm-specific
title: Interpretable Binary Classification Under Constraints for Financial Compliance Modeling
authors: Paz, Á.; Crawford, B.; Monfroy, E.; Rodriguez-Tello, E.; Barrera-García, J.; Cisternas-Caneo, F.; López Cortés, B.; Lazo, Y.; Yáñez, A.; Peña Fritz, Á.; Soto, R.
year: 2026
venue: Mathematics
odin_topics:
  - "4.A"
  - "4.B"
  - "5.A"
  - "6.A"
  - "7.B"
  - "8.A"
  - "10.A"
  - "12.A"
  - "12.B"
  - "12.C"
  - "13.B"
tldr: Supervised classifiers using pre-declaration administrative data predict student loan income declaration compliance with balanced error structures and stable feature importance rankings.
problem_and_motivation: Predicting borrower compliance in income-contingent loan systems is challenged by class imbalance, delayed outcomes, and the need for transparent decisions. Administrative records are underutilized for predictive analytics despite containing relevant signals. A framework is needed to estimate compliance likelihood using only pre-event information while preserving interpretability.
approach:
  - "Data from 8 relational tables for FSCU beneficiaries at PUCV, restricted to post-2012 obligations, with borrower-level aggregation."
  - "Seven classifiers evaluated: KNN, Naive Bayes, Logistic Regression, Linear SVM, Decision Tree, Random Forest, and LightGBM."
  - "Resampling strategies (SMOTE, ADASYN, Random Under-Sampling) applied within training folds to address class imbalance."
  - "Exhaustive grid search with stratified 5-fold cross-validation for hyperparameter optimization, maximizing MCC."
  - "Interpretability via permutation feature importance, decision tree paths, and SHAP values for global, structural, and local explanations."
findings:
  - "num: Optimized LightGBM achieved the highest MCC of 0.419 and F1-score of 0.861."
  - "Linear models (Logistic Regression, Linear SVM) achieved stable performance with F1-scores above 0.85 and MCC near 0.37."
  - "num: Hyperparameter optimization improved MCC by up to 0.1 for models like Decision Tree and Naive Bayes."
  - "Ensemble methods (Random Forest, LightGBM) offered more balanced error structures, slightly increasing false positives to improve recall."
  - "Top predictors consistently identified across models: debt amount, enrollment count, marital status, and loan enforceability year."
  - "Rule-based threshold baseline achieved low recall (0.172) and MCC (0.141), highlighting the value of machine learning."
key_figures_tables:
  - "Figure 12: Permutation feature importance → Debt amount and enrollment count are the most influential predictors."
  - "Figure 15-17: Decision tree snapshots at depths 4, 5, and 11 → Shallow trees yield compact, auditable rules; deeper trees capture niche interactions."
  - "Figure 18: SHAP summary for LightGBM → High debt and enrollments push predictions toward declaration; single status and earlier years toward non-declaration."
  - "Table 7-13: Model performance metrics → Ensemble models achieve highest MCC, but linear models offer comparable interpretability with slight trade-offs."
  - "Table 16: Practical threshold baseline → Simple rules have high precision but very low recall, confirming ML model superiority."
key_equations:
  - equation: "MCC = (TP*TN - FP*FN) / sqrt((TP+FP)(TP+FN)(TN+FP)(TN+FN))"
    explanation: "Primary evaluation metric robust to class imbalance."
  - equation: "θˆ = argmax_θ 1/K Σ_{k=1}^K MCC_k(θ)"
    explanation: "Optimal hyperparameters maximize mean MCC across cross-validation folds."
  - equation: "z = (x - μ) / σ"
    explanation: "z-score standardization for numerical features."
definitions:
  - term: "FSCU"
    definition: "Fondo Solidario de Crédito Universitario, Chilean income-contingent student loan system."
  - term: "MCC"
    definition: "Matthews Correlation Coefficient, balanced metric for imbalanced binary classification."
  - term: "PFI"
    definition: "Permutation Feature Importance, model-agnostic measure of feature influence."
  - term: "SHAP"
    definition: "SHapley Additive exPlanations, method for local feature attribution."
  - term: "CRUCH"
    definition: "Council of Rectors of Chilean Universities, governing body for FSCU-affiliated institutions."
critical_citations:
  - "[He and Garcia, 2009] — Foundational work on learning from imbalanced data."
  - "[Doshi-Velez and Kim, 2017] — Framing interpretability as a rigorous science for machine learning."
  - "[Breiman, 2001] — Introduces Random Forests, used as an ensemble baseline."
  - "[Chicco and Jurman, 2020] — Advocates MCC over F1 and accuracy for binary classification."
  - "[Lessmann et al., 2015] — Benchmarking classification algorithms for credit scoring contexts."
relevance:
  topics:
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "high"
      justification: "Directly evaluates supervised learning models for administrative financial compliance prediction."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Explicitly addresses gaps in using administrative data and interpretability in institutional systems."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Profiles borrowers using academic, financial, and demographic features to predict compliance behavior."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Applies supervised classification to predict binary compliance outcomes under constraints."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "contextual"
      justification: "Model predicts compliance, which could inform budget planning but is not a direct recommendation."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Identifies non-compliant borrowers, similar to anomaly detection in institutional monitoring."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "low"
      justification: "Discusses administrative data use but not privacy or security mechanisms."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Proposes a rigorous evaluation protocol using MCC, cross-validation, and multiple metrics."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Compares seven classifiers with hyperparameter optimization and resampling strategies."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "contextual"
      justification: "Evaluation methodology is relevant, but the system is not a budget recommender."
    - code: "13.B"
      name: "Debt Management in PFMS"
      relevance: "medium"
      justification: "Predicts declaration compliance, a key step in debt management for income-contingent loans."
  contribution: "This paper provides a reproducible modeling framework for predicting compliance in income-contingent loan systems using pre-event administrative data. It demonstrates that supervised classification can achieve reliable performance under class imbalance while preserving interpretability through global, structural, and local explanations. The methodological pipeline emphasizes leakage-aware validation, MCC-based evaluation, and audit-oriented interpretability, directly applicable to Odin's risk assessment and anomaly detection modules. The feature importance analysis identifies key predictors (debt, enrollment, marital status) that could inform Odin's behavioral profiling and forecasting modules. The framework's balance between linear and ensemble models offers a blueprint for Odin's evaluation strategy, prioritizing transparency and operational feasibility."
  directly_justifies:
    - "Pre-declaration administrative variables contain sufficient signal for reliable binary classification of compliance."
    - "MCC is the preferred evaluation metric for imbalanced classification, as it accounts for all confusion matrix cells."
    - "Ensemble methods (Random Forest, LightGBM) offer modest gains over linear models but with reduced intrinsic interpretability."
    - "Interpretability can be preserved through permutation importance, decision paths, and SHAP for constrained feature spaces."
    - "Hyperparameter optimization with cross-validated grid search yields consistent improvements across classifiers."
  limits:
    - "Single-institution data (PUCV) limits generalizability to other universities or regulatory contexts."
    - "Cross-sectional analysis ignores temporal drift and long-term compliance patterns."
    - "Interpretability methods provide approximations, not fully transparent decision logic for ensemble models."
    - "No institution-specific decision thresholds or cost-sensitive policies are defined for risk score translation."
  mapping_rationale: "A systematic scan across all 12 functional domains was conducted. The domains of Filipino Cultural Context, Expense Categorization, Behavioral Profiling, Spending Forecasting, Anomaly Detection, Mobile-First Design, Data Privacy, User Retention, and Savings/Debt Management were considered. The paper was flagged as highly relevant for Existing Systems & Gaps (4.A, 4.B) and System Evaluation (12.A, 12.B) due to its rigorous benchmarking and error analysis. It was also relevant for Behavioral Profiling (5.A) and Predictive Modeling (6.A) through its profile-based classification. For Anomaly Detection (8.A), it was assessed as medium because predicting non-compliance aligns with anomaly-like identification. Topics like Mobile-First Design (9.A) and User Retention (11.A) were rejected as the paper does not address user interfaces or engagement. Topics like Expense Categorization (3.A) and Savings (13.A) were rejected as they are not the paper's focus. Overall, the paper provides a strong methodological basis for Odin's evaluation and predictive modules, with moderate relevance to debt management and anomaly detection."
limitations:
  - "Available administrative data excludes socioeconomic variables like employment type or household composition. [unacknowledged]"
  - "Analysis focuses on first-declaration outcomes; subsequent declarations and long-term repayment behavior are not modeled. [unacknowledged]"
  - "Generalizability is limited by single-institution data; performance may vary across universities. [acknowledged]"
  - "Cross-sectional design ignores temporal drift from regulatory or labor-market changes. [acknowledged]"
  - "No formal cost-sensitive learning is applied due to undefined institutional misclassification costs. [acknowledged]"
remember_this:
  - "Pre-declaration administrative data can predict loan compliance with balanced error using MCC."
  - "LightGBM achieved the highest MCC (0.419) among seven classifiers evaluated."
  - "Debt amount, enrollment count, and marital status are the top consistent predictors."
  - "Interpretability via SHAP and decision paths enables audit-oriented decision support."
  - "Ensemble models improve recall but reduce intrinsic transparency compared to linear models."
```
---

## Paper 24: Luong & Xie_summarized.md

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

## Paper 25: Cabral et al_summarized.md

**Source File:** `Cabral et al_summarized.md`

```yaml
paper_id: 10.2139/ssrn.6170273
designation: international-algorithm-specific
title: Non-Stationarity in Financial Time Series: A Unifying Survey on Drift Detection, Adaptive Learning, and Evaluation
authors: Cabral, D. M.; Lima, A. M. A.; Oliveira, G. H. F. M.; Oliveira, A. L. I.
year: 2026
venue: SSRN # This paper is a pre-print article
odin_topics:
  - "3.A"
  - "3.B"
  - "4.A"
  - "5.A"
  - "5.C"
  - "6.A"
  - "6.B"
  - "7.A"
  - "7.B"
  - "8.A"
  - "8.B"
  - "8.C"
  - "12.A"
  - "12.B"
  - "12.C"
tldr: This survey unifies terminology and provides a structured pipeline for detecting, representing, adapting to, and evaluating non-stationarity in financial time series.
problem_and_motivation: Predictive models in finance typically assume distributional stability, an assumption that fails in deployment due to structural breaks, regime transitions, and drift, degrading calibration and performance. The literature is fragmented across econometrics, statistics, and machine learning with divergent terminology and incompatible evaluation protocols, hindering cumulative evidence and practical adoption of drift-aware methods.
approach:
  - Introduces a unified taxonomy of drift and regime change along temporal, statistical, spatial, and ontological axes.
  - Structures the literature around a five-pillar pipeline: non-stationarity characterization, drift-aware representations, change detection, continuous adaptation, and evaluation.
  - Reviews drift-aware representation methods including manual statistics, learned embeddings (TS2Vec), and latent-state models.
  - Covers change detection approaches ranging from retrospective segmentation (PELT) to online sequential methods (CUSUM) and Bayesian methods (BOCPD).
  - Summarizes evaluation metrics, experimental protocols, and benchmarking practices for financial time series under non-stationarity.
findings:
  - num: The literature review synthesized 174 references, highlighting the fragmentation across fields.
  - The proposed four-axis taxonomy (temporal, statistical, spatial, ontological) effectively aligns divergent terminology from machine learning, econometrics, and finance.
  - Learned embeddings, such as those from TS2Vec, can be applied directly to change-point detection methods, enhancing sensitivity to complex drift patterns.
  - Multimodal fusion, integrating numerical data with text, provides early signals of regime changes before they are fully reflected in prices.
  - Hybrid adaptation architectures, combining incremental updates with event-driven interventions, balance responsiveness and stability under non-stationarity.
  - Current evaluation practices lack standardization, weak replicability, and insufficiently consider operational constraints like latency and computational cost.
key_figures_tables:
  - "Figure 1: Extended taxonomy of non-stationarity along temporal, statistical, spatial, ontological, and causal axes → Provides a unified framework for describing drift scenarios."
  - "Figure 2: Temporal morphology of drifts (abrupt, gradual, incremental, recurrent) → Illustrates how changes unfold over time."
  - "Figure 10: Representation layers for drift-aware financial modeling → Shows a pipeline from raw data to detection and adaptation."
  - "Table 6: Change axes and indicative methods (compact view) → Maps drift types to suitable detection strategies."
  - "Table 9: Cost-benefit trade-offs for adaptation strategies → Guides method selection based on latency, compute, and performance gains."
key_equations:
  - equation: "$p(r_t = 0 | x_{1:t}) \\propto \\sum_{r} \\pi_t(r) \\cdot p(r_{t-1} = r | x_{1:t-1}) \\cdot H(r)$"
    explanation: "BOCPD update for changepoint probability, resetting run-length to zero."
  - equation: "$S^+_t = \\max(0, S^+_{t-1} + z_t - k)$"
    explanation: "CUSUM cumulative sum for detecting upward mean shifts."
  - equation: "$C(a,b) \\approx -\\log p(X_{a:b} | \\hat{\\theta}_{a:b})$"
    explanation: "Intra-segment cost function for segmentation, based on negative log-likelihood."
definitions:
  - term: "Concept Drift"
    definition: "Change in the conditional distribution P(Y|X) over time, representing a change in the relationship between inputs and targets."
  - term: "Regime"
    definition: "A persistent mode of operation of the data-generating process, characterized by relatively stable statistical properties."
  - term: "CUSUM"
    definition: "Cumulative Sum control chart, a sequential method for detecting shifts in the mean or other parameters of a process."
  - term: "BOCPD"
    definition: "Bayesian Online Changepoint Detection, a method that infers the posterior distribution of the run-length to detect changes in real time."
  - term: "PELT"
    definition: "Pruned Exact Linear Time, an algorithm for offline segmentation that efficiently detects multiple changepoints."
  - term: "ARL"
    definition: "Average Run Length, the expected time until a false alarm occurs, used to calibrate sequential detectors."
critical_citations:
  - "[Adams & MacKay, 2007] — Introduced Bayesian Online Changepoint Detection (BOCPD)."
  - "[Killick et al., 2012] — Developed the PELT algorithm for efficient offline change-point detection."
  - "[Gama et al., 2014] — A foundational survey on concept drift detection in data streams."
  - "[Yue et al., 2022] — Proposed TS2Vec for robust time-series representation learning."
relevance:
  topics:
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "medium"
      justification: "The survey discusses representation learning and feature engineering for financial data, relevant to categorizing spending patterns."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      relevance: "medium"
      justification: "The paper's discussion on drift-aware representations and how categories evolve is relevant to designing adaptable expense categories."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "low"
      justification: "The survey provides a broad perspective on current state of drift-aware systems but does not focus specifically on PFMS."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "The paper's taxonomy and detection methods for regime changes directly apply to identifying shifts in user spending behavior and financial profiles."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "The survey reviews classification approaches under concept drift, which is crucial for maintaining accurate user profile classification over time."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "The paper addresses how non-stationarity degrades predictive model performance, a core challenge for forecasting user spending."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Review of adaptive learning and forecasting algorithms under drift is directly applicable to sequential spending data forecasting."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "contextual"
      justification: "The paper discusses domain knowledge in the context of macroeconomic drivers but not specific budgeting strategies."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "The work on adaptive models under changing financial conditions is relevant for making budget recommendations that adapt to user behavior shifts."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "The survey covers anomaly and out-of-distribution detection, which are foundational to identifying unusual spending or fraud."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Detailed review of anomaly and drift detection algorithms (e.g., CUSUM, BOCPD, OOD methods) applicable to personal spending data."
    - code: "8.C"
      name: "Cold-Start Baseline Strategies for Anomaly Detection"
      relevance: "contextual"
      justification: "The survey mentions cold-start in the context of foundation models and universal embeddings, providing some contextual relevance."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "A significant portion of the paper is dedicated to evaluation protocols, metrics (e.g., detection delay, false-alarm rate), and benchmarking under non-stationarity."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "The paper provides specific guidance on evaluating change detectors and adaptive learning modules, including computational cost and predictive performance."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "medium"
      justification: "The evaluation principles (temporal validation, cost-aware metrics) can be adapted for evaluating budget recommendation systems."
  contribution: "This paper provides a unified taxonomy and a structured end-to-end pipeline that is directly applicable to designing and evaluating Odin's core modules. It offers concrete guidance for selecting and implementing drift detection algorithms for anomaly detection and user profile classification. The survey's emphasis on evaluation protocols and metrics informs how Odin's forecasting and recommendation modules should be tested for robustness. Furthermore, the discussion on multimodal context and adaptive learning suggests methods for Odin to incorporate user-declared preferences and seasonal patterns. The framework supports a systematic approach to handling the non-stationary nature of financial behavior, which is central to Odin's functionality."
  directly_justifies:
    - "Non-stationarity in financial data requires continuous monitoring and adaptation of predictive models."
    - "Evaluation under drift must account for detection delay, false-alarm control, and computational cost."
    - "Hybrid adaptation architectures balance stability and responsiveness to changing conditions."
    - "Learned representations can capture complex drift patterns better than hand-crafted features."
    - "Multimodal fusion can provide early signals of regime changes."
  limits:
    - "The survey is a literature review and does not present new empirical results on Odin-specific data."
    - "The proposed pipeline is general and may require customization for the specific constraints of a mobile-first PFMS."
    - "The effectiveness of many discussed methods may depend on data availability and computational resources."
  mapping_rationale: "A systematic scan across all 12 functional domains was performed to map the survey's content to Odin's topic codes. The paper's core focus on non-stationarity in financial time series is highly relevant to several domains. The 'Behavioral Profiling & Classification' domain (5.A, 5.C) is directly addressed by the survey's discussion on detecting shifts in user behavior and profiles. 'Spending Forecasting' (6.A, 6.B) is a primary application area for the adaptive learning and forecasting algorithms reviewed. 'Anomaly Detection' (8.A, 8.B) is a key application of the change detection methods discussed, with the survey's coverage of OOD and novelty detection being directly relevant. The 'System Evaluation' domain (12.A, 12.B, 12.C) is strongly supported by the survey's extensive sections on evaluation protocols and metrics. Topics like 'Expense Categorization' (3.A, 3.B) are tangentially related through representation learning, while 'Existing Systems' (4.A) is only briefly touched upon. 'Budget Recommendation' (7.A, 7.B) is contextually relevant as the principles of adaptive models can apply to budget suggestions, but the paper doesn't cover budget recommendation specifically. The domains of 'Mobile-First Design' and 'Data Privacy' have no direct mapping. 'Savings & Debt Management' is not addressed. Overall, the paper provides a comprehensive methodological foundation for building and evaluating a robust, adaptive PFMS like Odin, particularly for its predictive and anomaly detection modules."
limitations:
  - "The paper does not provide new empirical results, relying on existing literature."
  - "The proposed framework is a survey and may not cover all niche algorithmic details required for a specific implementation. [unacknowledged]"
  - "The survey focuses on financial time series at a macro or market level, and its direct applicability to individual-level spending data may require further validation. [unacknowledged]"
remember_this:
  - "Non-stationarity is the norm in financial data, not the exception."
  - "Detection, representation, and adaptation form an integrated pipeline for handling drift."
  - "Evaluation under drift must use temporal protocols and cost-aware metrics."
  - "Hybrid adaptation balances continuous updates with event-driven interventions."
  - "The choice of method depends on the specific type and scale of drift expected."
```
---

## Paper 26: Heirene R. et al-2026b_summarized.md

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

## Paper 27: Li C. et al_summarized.md

**Source File:** `Li C. et al_summarized.md`

```yaml
paper_id: 10.1109/ACCESS.2026.3697984
designation: international-algorithm-specific
title: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation With Autoencoder-Enhanced Feature Learning
authors: Li, C.; Ishak, I.; Ibrahim, H.; Zolkeply, M.; Sidi, F.; Li, C.
year: 2026
venue: IEEE Access
odin_topics:
  - 6.A
  - 6.B
  - 7.A
  - 8.A
  - 12.B
tldr: Integrates BIRCH hierarchical clustering with autoencoder feature learning and ensemble consensus for scalable e-commerce user segmentation, improving silhouette scores by up to 23% over single BIRCH models.
problem_and_motivation: Traditional clustering algorithms face scalability, high-dimensionality, and incremental adaptability challenges for modern e-commerce platforms. Existing methods lack integrated solutions that combine scalable hierarchical clustering, deep feature learning, and robust consensus mechanisms.
approach:
  - Uses a deep autoencoder to compress 30-50 behavioral features into a 14-dimensional latent space, preserving 90-95% variance and mitigating curse of dimensionality.
  - Employs BIRCH as the core scalable clustering engine with multiple parameter configurations (thresholds T ∈ {0.3,0.5,0.8}) and global clustering variations.
  - Introduces four ensemble consensus strategies: Majority Voting, Weighted Voting, Advanced Affinity-based Spectral Clustering (AASC), and novel BIRCH-Optimized Hierarchical Consensus (BOHC).
  - Implements dynamic ensemble selection using a composite score of Silhouette, Calinski-Harabasz, and Davies-Bouldin indices to automatically choose optimal strategy.
  - Validates framework on two large-scale datasets (Retail Rocket: 1.4M users; E-Commerce Behavior: 4.5M users) across 20 randomized subset trials.
findings:
  - num: Autoencoder-based feature learning improves BIRCH silhouette scores by 23-53% over raw features and 28-76% over PCA.
  - num: BOHC achieves up to 23% silhouette improvement over single BIRCH models for transaction-focused single-domain datasets.
  - num: BIRCH maintains superior performance at higher cluster counts (silhouette 0.603 at 15 clusters vs K-Means 0.332), representing an 81% improvement.
  - Domain granularity fundamentally determines method selection: single-domain scenarios favor ensemble methods (17-23% improvement), while multi-domain scenarios favor base algorithms (7.4% advantage).
  - num: Full-scale BOHC run on 4.5M users completes in approximately 5 minutes (307.8 seconds), demonstrating production feasibility.
  - num: Incremental updates achieve 37x speedup over full re-clustering (8.3s vs 307.8s) for daily batches with minimal quality degradation (<0.3%).
key_figures_tables:
  - Figure 1: Framework architecture overview showing data preprocessing, autoencoder compression, BIRCH ensemble clustering, and dynamic selection → Modular pipeline combining deep feature learning, hierarchical clustering, and adaptive ensemble consensus.
  - Table 2: Performance comparison across cluster counts for Retail Rocket → AASC/BOHC ensembles achieve 0.548 silhouette score at 5 clusters, 23% improvement over single BIRCH.
  - Table 4: Performance metrics for E-Commerce Behavior multi-category dataset → Base algorithms outperform ensembles (K-Means 0.683 vs BOHC 0.633 at 5 clusters).
  - Table 5: Single-domain category results for Electronics and Appliances → Both categories show ensemble superiority (17-23% improvement) with different granularity-dependent patterns.
  - Figure 5: Comprehensive single-domain visualization → Electronics shows consistent ensemble advantage (17-23%), Appliances transitions from base superiority at 5 clusters to 23% ensemble advantage at 20 clusters.
key_equations:
  - equation: CF = (N, \\vec{S}, SS)
    explanation: Clustering Feature as compact statistical summary (count, linear sum, squared sum)
  - equation: S = \\frac{1}{n}\\sum_{i=1}^{n}\\frac{b(i)-a(i)}{\\max\\{a(i),b(i)\\}}
    explanation: Silhouette score measures cluster cohesion and separation
  - equation: A^{BOHC}_{ij} = \\frac{1}{M}\\sum_{m=1}^{M} \\exp(-\\alpha \\cdot h_m(i,j))
    explanation: BOHC hierarchical affinity using common ancestor heights in CF Trees
definitions:
  - term: CF Tree
    definition: Height-balanced tree structure with Clustering Feature summaries for scalable hierarchical clustering
  - term: BIRCH
    definition: Balanced Iterative Reducing and Clustering using Hierarchies, memory-efficient clustering algorithm
  - term: BOHC
    definition: BIRCH-Optimized Hierarchical Consensus, novel ensemble strategy preserving multi-scale clustering information
  - term: Autoencoder
    definition: Neural network learning efficient latent representations through reconstruction minimization
  - term: RFM
    definition: Recency, Frequency, Monetary analysis for customer segmentation
critical_citations:
  - "[Zhang et al., 1996] — Introduces BIRCH algorithm with CF Tree structure"
  - "[Strehl and Ghosh, 2002] — Foundational work on cluster ensembles"
  - "[Xie et al., 2015] — Deep embedded clustering for joint representation and clustering"
  - "[Zhao et al., 2021] — Regularized K-Means for high-dimensional customer segmentation"
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Provides scalable clustering framework applicable to spending pattern identification and user segmentation in PFMS
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: Autoencoder-based feature learning and BIRCH clustering methods transferable to forecasting spending sequences
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: low
      justification: Segmentation insights can inform differentiated budgeting strategies based on user behavioral profiles
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Ensemble clustering approach provides baseline for identifying abnormal spending patterns through behavioral grouping
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Multi-metric evaluation framework (Silhouette, CH, DB) directly applicable to PFMS module assessment
  contribution: "This paper provides a scalable, hierarchical clustering framework that can be adapted for financial user segmentation in Odin. The modular design with independent autoencoder training and BIRCH clustering offers practical deployment flexibility for production systems. The incremental learning capability enables real-time updates as new user spending data arrives. The multi-metric dynamic selection mechanism provides a robust evaluation methodology for algorithmic modules within a PFMS."
  directly_justifies:
    - "Autoencoder-based feature learning improves clustering quality by 23-53% over raw features."
    - "BIRCH maintains superior performance at higher cluster counts for multi-resolution segmentation."
    - "Domain granularity assessment is critical for selecting between ensemble and base algorithms."
    - "Dynamic ensemble selection using multiple internal validation metrics provides adaptive optimization."
  limits:
    - "Evaluation restricted to e-commerce domain; transferability to PFMS spending data requires validation."
    - "Temporal dynamics and user behavioral evolution are not explicitly modeled."
    - "Internal validation metrics may not fully capture business-relevant segmentation quality."
  mapping_rationale: "Systematic scan across all 12 functional domains identified 5 relevant topic codes. The paper's primary relevance is to Predictive Modeling (6.A, high) and System Evaluation (12.B, high) through its scalable clustering framework and comprehensive evaluation methodology. Forecasting Algorithms (6.B, medium) applies via autoencoder and BIRCH techniques transferable to sequential spending prediction. Budgeting Strategies (7.A, low) relates indirectly through segmentation-informed differentiated approaches. Anomaly Detection (8.A, medium) benefits from ensemble clustering baselines for identifying behavioral outliers. The Filipino Cultural Context domains (2.A, 2.B, 2.D) were considered and rejected as the paper focuses on universal e-commerce user behavior without culturally specific patterns. Expense Categorization (3.A-C) was not directly addressed as the framework operates on behavioral features, not financial transaction categories. The paper provides methodological contributions relevant to multiple Odin modules rather than direct consumer finance insights."
limitations:
  - "Evaluation restricted to e-commerce domain; applicability to personal finance spending data requires validation."
  - "Temporal dynamics and user behavioral evolution are not explicitly modeled."
  - "The framework treats users as static snapshots, not capturing seasonal or lifecycle changes."
  - "Latent representations reduce interpretability for business stakeholders."
  - "Cold-start limitation for users with minimal historical interaction data. [unacknowledged]"
  - "Upper scalability limits beyond 4.5M users remain untested."
remember_this:
  - "Autoencoder features improve clustering by 23-53% over raw features."
  - "BIRCH achieves 81% higher silhouette than K-Means at 15 clusters."
  - "Domain granularity determines if ensemble or base algorithms are optimal."
  - "Incremental updates provide 37x speedup over full re-clustering."
  - "BOHC ensemble up to 23% improvement for single-domain datasets."
```
---

## Paper 28: Olabintan_summarized.md

**Source File:** `Olabintan_summarized.md`

```yaml
paper_id: 10.2139/ssrn.6837665
designation: local-algorithm-specific
title: FairLend-Africa: An Explainable Machine Learning Framework for Alternative Credit Scoring Using Behavioral Financial Data in Financially Excluded African Communities
authors: Olabintan, I.
year: 2026
venue: SSRN
odin_topics:
  - 1.A
  - 1.C
  - 2.B
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 7.B
  - 7.C
  - 8.A
  - 8.B
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
  - 12.C
tldr: An explainable ML framework for alternative credit scoring using mobile money behavioral data, achieving ROC-AUC of 0.714 on synthetic data with SHAP explanations and fairness auditing.
problem_and_motivation: Billions of adults globally lack formal credit histories, making them invisible to conventional scoring systems. Behavioral financial data from mobile money offers a potential proxy for creditworthiness, but integration into fair and explainable frameworks remains limited.
approach:
  - Synthetic dataset of 10,000 borrower records with 16 raw behavioral features from mobile money and credit history was generated.
  - XGBoost classifier was trained with hyperparameter optimization via RandomizedSearchCV and evaluated against logistic regression.
  - SHAP provided global feature importance and local explanations for individual credit decisions.
  - Systematic fairness audit assessed demographic parity, equal opportunity, and predictive parity across regional and gender subgroups.
  - System was implemented as a REST API with an interactive React dashboard for loan officers.
findings:
  - Tuned XGBoost achieved a held-out test ROC-AUC of 0.714, matching the logistic regression baseline of 0.713.
  - Wallet balance trend and savings consistency were the dominant creditworthiness signals.
  - Fairness audit found no demographic disparities under the synthetic data's independence assumption.
  - num: The optimal classification threshold was 0.151, substantially below the conventional 0.5.
  - Engineered composite features provided no measurable predictive improvement over raw features.
key_figures_tables:
  - Table 1: 16 raw behavioral features with domain and rationale → Features cover mobile money, airtime, savings, credit, social, and payment domains.
  - Table 3: Model comparison test set performance → Tuned XGBoost ROC-AUC 0.714 vs logistic regression 0.713.
  - Table 5: Fairness disparity ratios → All groups exceed 0.80 for selection rate, TPR, and precision.
  - Table 6: Selection rate disparity ratios across thresholds → All ratios exceed 0.80, with West Africa lowest at 0.818.
  - Figure 7: Global feature importance by mean SHAP value → Wallet balance trend dominates by factor of 1.74.
key_equations:
  - equation: f(x_i) = ∅_0 + ∑_{j=1}^p ∅_{ij}
    explanation: SHAP decomposition of prediction into base rate plus feature contributions.
definitions:
  - term: ROC-AUC
    definition: Area under the receiver operating characteristic curve, measuring discrimination ability.
  - term: SHAP
    definition: SHapley Additive exPlanations, a game-theoretic approach for explaining model predictions.
  - term: Demographic parity
    definition: Equal positive prediction rates across demographic groups.
  - term: Equal opportunity
    definition: Equal true positive rates across demographic groups.
  - term: MNAR
    definition: Missing Not At Random, where missingness depends on unobserved values.
critical_citations:
  - "[Björkegren and Grissen, 2018] — Mobile phone metadata predicts loan repayment with AUC ~0.70."
  - "[Suri and Jack, 2016] — Mobile money enables households to navigate income shocks."
  - "[Lundberg and Lee, 2017] — Unified framework for model explanation using SHAP values."
  - "[Chouldechova, 2017] — Impossibility theorem for simultaneously satisfying fairness criteria."
  - "[Baesens et al., 2003] — Ensemble methods outperform single classifiers in credit scoring."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Provides general context on financially excluded populations in Africa, analogous to unbanked Filipinos.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: contextual
      justification: Demonstrates use of behavioral transaction data as a proxy for creditworthiness, relevant to understanding financial behavior.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Mentions temporal dynamics and seasonal patterns as a limitation, not a focus.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Reviews digital credit systems like M-Shwari, Tala, Branch, providing context for PFMS landscape.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly addresses lack of explainability and fairness in existing alternative credit scoring systems.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Framework creates behavioral profiles from mobile money features to predict creditworthiness.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Uses XGBoost and logistic regression to classify borrowers into repayment risk categories.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Core contribution is a predictive model for credit scoring using behavioral data.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: Uses predictive modeling on behavioral features, though not explicitly sequential time-series forecasting.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Framework is for credit scoring, not budget recommendation; methodology could be adapted.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: contextual
      justification: Not directly addressed; threshold tuning relates to cost asymmetry.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Not addressed; focusing on credit classification.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: XGBoost could potentially be used for anomaly detection, but not the focus.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Mentions dashboard for loan officer use, but system is not explicitly mobile-first.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: Dashboard design is for loan officers, not end-user PFMS.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Discusses privacy barriers, data protection acts, and synthetic data for privacy.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Addresses trust through explainability (SHAP) and fairness auditing.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides evaluation protocol including ROC-AUC, fairness metrics, and threshold analysis.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Evaluates XGBoost, logistic regression, and SHAP explainability module.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: contextual
      justification: Evaluation metrics are general ML metrics, not specific to budget recommendation.
  contribution: FairLend-Africa provides a blueprint for Odin's predictive module using behavioral data, demonstrating that XGBoost with SHAP explanations can achieve reasonable predictive performance. The fairness audit framework directly maps to Odin's need for transparent and equitable algorithms, particularly important for a Filipino audience concerned with social justice. The emphasis on explainability supports Odin's design goal of building user trust through interpretable decisions. The open-source implementation and REST API design offer a practical template for Odin's system architecture.
  directly_justifies:
    - "Behavioral financial data from mobile money transactions carries sufficient predictive signal for creditworthiness classification."
    - "XGBoost with SHAP explanations provides a coherent method for predictive modeling and interpretability in personal finance systems."
    - "Systematic fairness auditing using demographic parity and equal opportunity is feasible and necessary for equitable algorithmic systems."
    - "Missing data in financial profiles is informative and requires careful handling (e.g., MNAR with missingness indicators)."
    - "Ablation studies are essential to validate feature engineering contributions."
  limits:
    - "Results are based on synthetic data, not real Filipino behavioral data."
    - "Fairness properties are derived under a synthetic independence assumption that may not hold in real settings."
    - "XGBoost performance matches logistic regression, indicating linear structure in synthetic data; real data may show non-linear benefits."
    - "Engineered composite features provided no measurable lift, questioning their practical value."
    - "SHAP explanations assume feature independence, which may misrepresent contributions when features are correlated."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to Predictive Modeling (6.A, 6.B), Behavioral Profiling (5.A, 5.C), and Evaluation Frameworks (12.A, 12.B) as its core contribution is an ML framework for credit scoring. It also has high relevance to Existing Systems (4.A, 4.B) as it reviews digital credit systems and their limitations, and to Data Privacy (10.A) and User Trust (10.B) as it discusses privacy barriers and uses explainability/fairness. Medium relevance was assigned to Mobile-First Design (9.A) due to the dashboard and Filipino Demographic (1.A, 1.C) due to contextual parallels in financial exclusion. Low or contextual relevance was assigned to Budget Recommendation (7.B, 12.C), Anomaly Detection (8.A, 8.B), and Seasonal Spending (2.B) as the paper does not directly address these topics. Borderline cases included the paper touching on both predictive modeling and fairness, which were both selected as high relevance. The overall relevance is high for Odin's algorithmic and evaluation modules, providing a methodological template.
limitations:
  - "Synthetic dataset not validated on real Filipino mobile money data. [unacknowledged]"
  - "Fairness audit assumes demographic-behavioral independence, which may not hold in real Philippines data."
  - "Engineered features provided no predictive improvement; practical value on real data is unproven."
  - "SHAP explanations assume feature independence, which can misrepresent correlated feature contributions."
  - "System has not been evaluated for temporal stability or concept drift."
  - "Near-identical XGBoost and logistic regression performance suggests primarily linear structure in data; non-linear benefits need real data validation."
remember_this:
  - "Behavioral data achieves 0.714 AUC for credit scoring, matching logistic regression on synthetic data."
  - "Wallet balance trend and savings consistency are the strongest creditworthiness signals."
  - "Fairness audit found no disparities, but this is contingent on synthetic data independence."
  - "SHAP explanations provide interpretability but assume feature independence, a known limitation."
  - "Feature ablation showed engineered features provided no measurable lift in predictive performance."
```
---

## Paper 29: Patel & Singh_summarized.md

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

## Paper 30: Zhang & Hou_summarized.md

**Source File:** `Zhang & Hou_summarized.md`

```yaml
paper_id: 10.1016/j.procs.2026.05.035
designation: international-algorithm-specific
title: Consumer Behavior Data Mining and Analysis Using Machine Learning Algorithms
authors: Zhang, H.; Hou, Y.
year: 2026
venue: Procedia Computer Science
odin_topics:
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 9.A
  - 10.B
  - 12.B
tldr: Compares logistic regression, SVM, random forest, and XGBoost for predicting purchase intention using an e-commerce dataset to guide algorithm selection in consumer behavior analysis.
problem_and_motivation: Traditional statistical tools are inadequate for complex, high-dimensional consumer data, and a clear performance comparison of modern machine learning algorithms under a unified framework is lacking. Selecting the appropriate algorithm requires balancing accuracy, efficiency, and interpretability.
approach:
  - Uses the UCI "Online Retail" dataset with 28 engineered features including RFM, behavioral breadth, consumption patterns, and time patterns.
  - Defines a binary prediction task for future purchase intention within a fixed time window.
  - Implements logistic regression, SVM, random forest, and XGBoost with grid search and 5-fold cross-validation for hyperparameter tuning.
  - Evaluates models on a separate test set using accuracy, precision, recall, F1, and AUC.
  - Compares training and prediction efficiency and analyzes feature importance across models.
findings:
  - "num: XGBoost achieved the highest F1 score of 0.680 and AUC of 0.872."
  - "num: Logistic regression had the fastest training time at 0.8 seconds."
  - "num: SVM was the slowest with a training time of 125.3 seconds."
  - Feature importance consistently identified 'Recency' as the most predictive feature across all models.
  - XGBoost demonstrated the best balance between accuracy and efficiency.
  - Logistic regression remained the most interpretable model.
key_figures_tables:
  - "Table 1: Model performance metrics (Accuracy, Precision, Recall, F1, AUC). → XGBoost leads in all metrics."
  - "Table 2: Model training and prediction times. → Logistic regression fastest; SVM slowest."
  - "Table 3: Top 3 important features per model. → Recency is the most important feature for all models."
key_equations:
  - equation: "P(y = 1 | x) = 1 / (1 + e^{-(w^T x + b)})"
    explanation: "Logistic function mapping features to purchase probability."
  - equation: "f(x) = sign(\\sum_{i=1}^n \\alpha_i y_i K(x_i, x) + b)"
    explanation: "SVM decision function with kernel K for nonlinear classification."
  - equation: "L^{(t)} = \\sum_{i=1}^n l(y_i, \\hat{y}_i^{(t-1)} + f_t(x_i)) + \\Omega(f_t)"
    explanation: "XGBoost objective function with loss and regularization."
definitions:
  - term: RFM Model
    definition: "A framework using Recency, Frequency, and Monetary value for customer segmentation and behavior analysis."
  - term: AUC
    definition: "Area Under the ROC Curve; measures the model's ability to distinguish between classes."
critical_citations:
  - "[Li, 2023] — Foundation for ML in e-commerce behavior analysis."
  - "[Akram et al., 2025] — Comparative study of ML algorithms for behavior prediction."
  - "[Lin, 2025] — Application of ML for predicting consumer behavior."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: "Paper benchmarks algorithms for predicting purchase behavior, a core task in profiling."
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: "Directly compares classification algorithms (LR, SVM, RF, XGBoost) for behavior prediction."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: "Provides an empirical framework for selecting predictive models in a financial context."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: "Uses temporal features (e.g., recency) and compares algorithms suitable for sequential data."
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: contextual
      justification: "Discussion of model efficiency informs design choices for resource-constrained environments."
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: "Mentions interpretability as a factor, which is linked to user trust."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: "Provides a clear evaluation methodology for comparing prediction algorithms."
  contribution: "This paper provides a benchmark for choosing machine learning algorithms for Odin's spending forecasting and behavioral classification modules. The comparison of XGBoost, Random Forest, and Logistic Regression directly informs the selection of models for predicting user financial behavior. The analysis of feature importance highlights the value of recency and frequency, which are crucial for Odin's core profile features. The discussion on the trade-off between accuracy and interpretability guides the design of Odin's explanation and user trust features."
  directly_justifies:
    - "XGBoost achieves the best balance of accuracy and efficiency for predicting purchase behavior."
    - "Recency and frequency are the most important features for predicting future purchasing behavior."
    - "Logistic regression provides the highest interpretability, while ensemble methods offer superior accuracy."
    - "Model selection must consider the trade-off between prediction performance and computational cost."
    - "Feature engineering based on domain knowledge (RFM) is crucial for model performance."
  limits:
    - "The study uses a single e-commerce dataset, limiting generalizability."
    - "Does not address cold-start scenarios where historical user data is unavailable. [unacknowledged]"
    - "Focuses on a binary classification task, not multi-class or regression for financial amounts. [unacknowledged]"
    - "The 'Online Retail' dataset may not represent the spending patterns of Filipino young professionals. [unacknowledged]"
  mapping_rationale: "A systematic scan of all 12 functional domains was performed. Domains related to behavioral classification (5.A, 5.C) and spending forecasting (6.A, 6.B) were flagged as having high or medium relevance because the paper directly compares algorithms for predicting consumer behavior. Evaluation frameworks (12.A, 12.B, 12.C) were considered relevant as the paper provides a controlled evaluation methodology. Mobile-first design (9.A) was considered contextual due to the discussion on computational efficiency. Data privacy (10.A, 10.B) was only tangentially touched upon via model interpretability (low relevance). Domains like Filipino cultural context (2.A-D), expense categorization (3.A-C), existing systems (4.A-B), budgeting (7.A-D), anomaly detection (8.A-C), retention (11.A-B), and savings/debt management (13.A-C) were rejected as the paper does not provide citeable claims for these specific Odin design areas. The overall relevance is moderate, providing strong empirical justification for algorithmic choices in prediction modules."
limitations:
  - "Single dataset limits generalizability of findings."
  - "Does not explore deep learning or more recent algorithms."
  - "The performance comparison may not hold for different types of consumer data."
  - "The study lacks a discussion on real-time deployment constraints. [unacknowledged]"
remember_this:
  - "XGBoost achieved the highest F1 score of 0.680 and AUC of 0.872."
  - "Recency was the single most important feature for all models tested."
  - "Random forest offers a good balance between accuracy and robustness."
  - "Logistic regression is the most interpretable and fastest algorithm."
  - "Ensemble methods like XGBoost are preferred for complex behavioral data."
```
---

## Paper 31: Chikoore et al_summarized.md

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
  - 5.C
  - 6.A
  - 8.A
  - 12.B
  - 13.B
tldr: An adaptive credit scoring framework integrating multiple ML models with dynamic adaptation strategies addresses concept drift in developing economies, achieving superior predictive performance.
problem_and_motivation: Traditional static credit scoring models lack drift detection and adaptation, causing performance degradation in dynamic economic conditions. Existing adaptive approaches are developed for advanced economies and are not suited to developing contexts, necessitating a framework tailored to such environments.
approach:
  - The German Credit dataset was used with simulated drifts: feature distribution shift, noise addition, and class distribution change.
  - Four vanilla models (CART, Naive Bayes, Random Forest, XGBoost) were benchmarked; Random Forest was selected as baseline.
  - Four adaptation strategies were implemented: retraining on drifted data, sliding window learning, soft voting ensemble, and adaptive fusion.
  - Adaptive fusion dynamically weights outputs from original, retrained, and windowed models with weights summing to one.
  - Evaluation metrics include accuracy, precision, recall, F1-score, and ROC-AUC.
findings:
  - num: Retrained Random Forest, Ensemble, and Adaptive Fusion achieved 95.0% accuracy, 0.9275 precision, 0.9645 recall, 0.9426 F1, and ROC-AUC >0.96.
  - num: Adaptive Fusion outperformed state-of-the-art DGHNL (94.60% accuracy, AUC 0.9360).
  - Adaptive Fusion demonstrated the most robust performance across all drift scenarios with minimal degradation.
  - Ensemble approach was consistently second best, while windowing underperformed in recall and F1.
  - Batch retraining yielded reasonable accuracy but slower adaptation compared to fusion.
key_figures_tables:
  - Table 1: Vanilla model performance on original dataset → Random Forest highest at 0.77 accuracy.
  - Figure 3: Bar chart of vanilla model metrics → Random Forest and XGBoost outperform others.
  - Figure 4: ROC-AUC for adaptive retraining → Shows AUC >0.96 for top strategies.
  - Figure 5: ROC-AUC for adaptive windowing → Lower performance than fusion.
  - Figure 6: ROC-AUC for ensemble and adaptive fusion → Adaptive fusion highest and most stable.
key_equations:
  - equation: X_d = X_n + 5
    explanation: Feature distribution shift by aging all instances by 5 years.
  - equation: N(0, 1000) noise added to credit amount
    explanation: Simulates random fluctuations in loan sizes.
  - equation: f(x) = (1/(σ√(2π))) e^(-(x-µ)^2/(2σ^2)) with σ=1000
    explanation: Gaussian distribution for noise addition.
  - equation: P'(C_i) = (w_i · P(C_i)) / (Σ_j w_j · P(C_j))
    explanation: Weighted class probability to simulate class distribution drift.
  - equation: p_final = w_0*p_0 + w_r*p_r + w_w*p_w, with sum w=1
    explanation: Adaptive fusion combines predictions from three models.
definitions:
  - term: Concept drift
    definition: Change in data distribution over time that degrades model performance.
  - term: Adaptive fusion
    definition: Dynamic weighting of multiple model outputs to adapt to drift.
  - term: Population drift
    definition: Shift in the underlying characteristics of the borrower population.
  - term: ROC-AUC
    definition: Area under the receiver operating characteristic curve, measures classification performance.
  - term: DGHNL
    definition: Deep Genetic Hierarchical Network of Learners, a state-of-the-art credit scoring model.
critical_citations:
  - "[Liu et al., 2021] — Introduced diverse instance-weighting ensemble for drift adaptation."
  - "[Nikolaidis and Doumpos, 2022] — Adaptive credit scoring using local regions of competence."
  - "[Museba, 2023] — Adaptive heterogeneous ensemble for credit scoring."
  - "[Barddal et al., 2020] — Data stream classification applied to credit scoring."
relevance:
  topics:
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Paper identifies limitations of static models in dynamic environments.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Credit scoring classifies borrowers based on financial behavior.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Uses ML classifiers to categorize credit risk, directly relevant to profile classification.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Credit scoring is a form of predictive modeling in finance.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Mentions fraud detection but primary focus is credit scoring.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Extensive evaluation of adaptive algorithms with multiple metrics.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: medium
      justification: Credit scoring informs lending decisions, relevant to debt management.
  contribution: The adaptive fusion technique can inform Odin's spending forecasting module by providing a method to combine multiple models to adapt to shifting spending patterns. The evaluation metrics and methodology can be used to assess Odin's classification modules. The paper's treatment of concept drift and adaptation strategies is directly applicable to Odin's anomaly detection component, which must handle evolving user behavior. The emphasis on developing economy contexts aligns with Odin's target demographic, justifying the adoption of such adaptive methods.
  directly_justifies:
    - Adaptive models that dynamically fuse multiple classifiers outperform static models in dynamic environments.
    - Retrained models achieve high accuracy but adaptive fusion offers similar performance with lower computational cost.
    - Ensemble methods provide robust performance without full retraining, balancing accuracy and efficiency.
  limits:
    - Results are based on a single dataset (German Credit) with simulated drifts, not real streaming data.
    - The study does not address fairness and bias in credit scoring beyond mentioning it.
    - Generalizability to other developing economy contexts beyond South Africa may be limited.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant to the following domains: Existing Systems & Gaps (4.A, 4.B) because it discusses limitations of static credit scoring models; Behavioral Profiling & Classification (5.A, 5.C) as it uses ML to classify borrowers into risk categories; Predictive Modeling (6.A) as credit scoring is a form of predictive modeling; Anomaly Detection (8.A) as it touches on fraud detection and risk identification; System Evaluation (12.A, 12.B) as it provides extensive model evaluation; and Savings & Debt Management (13.B) as credit scoring is integral to debt management. Specific topic codes selected: 4.B (medium), 5.A (medium), 5.C (high), 6.A (medium), 8.A (low), 12.B (high), 13.B (medium). Borderline cases: The paper's focus on concept drift could also relate to 6.B (forecasting algorithms) and 8.B (anomaly detection algorithms), but these were rejected because the paper does not deal with sequential spending data or specific anomaly detection algorithms; it is primarily classification. The topics 3.A, 3.B, 3.C were considered but rejected as the paper does not address expense categorization. 7.A-D were rejected as it does not address budgeting. 9.A-B, 10.A-B, 11.A-B were rejected as they are not addressed. Overall, the paper provides a valuable adaptive modeling approach that can inform Odin's classification, evaluation, and adaptation strategies, with high relevance to model evaluation and classification approaches.
limitations:
  - The study relies on simulated drift scenarios rather than real-world streaming data.
  - Only the German Credit dataset is used, limiting generalizability.
  - Fairness and bias are mentioned but not systematically evaluated. [unacknowledged]
remember_this:
  - Adaptive Fusion achieved 95.0% accuracy and ROC-AUC >0.96 in credit scoring.
  - Dynamic fusion of multiple models is more robust to concept drift than retraining alone.
  - The study demonstrates the need for drift-aware models in developing economy contexts.
  - Ensemble and adaptive strategies maintain performance under data distribution shifts.
```
---

## Paper 32: Li J._summarized.md

**Source File:** `Li J._summarized.md`

```yaml
paper_id: 10.71222/7v3b7272
designation: international
title: Research on Personalized Asset Allocation Using AI Agents in Robo-Advisory Scenarios
authors: Li, J.
year: 2026
venue: Journal of Computer, Signal, and System Research
odin_topics:
  - 5.A
  - 7.A
  - 7.B
  - 7.C
  - 8.A
  - 10.A
  - 10.B
  - 12.A
  - 12.B
  - 13.A
tldr: A systematic review of AI-driven personalized asset allocation in robo-advisory, examining risk profiling, dynamic allocation, and behavioral finance integration with a focus on algorithmic transparency and data privacy.
problem_and_motivation: Traditional robo-advisors rely on generalized algorithms that fail to address individual financial circumstances and dynamic risk preferences. This limitation motivates the development of sophisticated AI techniques to deliver truly personalized, adaptive investment strategies that improve outcomes and satisfaction.
approach:
  - This is a systematic review of the literature on AI agents for personalized asset allocation in robo-advisory contexts.
  - It examines machine learning, reinforcement learning, and natural language processing techniques used for risk profiling and portfolio optimization.
  - The review compares rule-based systems with AI-driven approaches, analyzing their strengths, limitations, and performance.
  - It incorporates behavioral finance principles, evaluating how AI can identify and mitigate cognitive biases in investment decisions.
  - The review addresses challenges related to transparency, explainability, data privacy, security, and regulatory compliance.
findings:
  - num: AI-driven risk assessment using deep learning and NLP improves personalization over static questionnaires by analyzing transaction history and investor communication.
  - num: Reinforcement learning agents learn optimal asset allocation strategies through interaction with market environments, adapting to changing conditions.
  - num: Integrating behavioral finance insights via AI mitigates biases like loss aversion and overconfidence, promoting rational decision-making.
  - num: AI-enhanced asset allocation demonstrates improved performance in volatile markets compared to static, rule-based approaches.
  - AI agents can quantify bias influence using metrics like bias score B_s to adjust recommendations dynamically.
  - Key challenges include lack of explainability, data privacy concerns, and regulatory compliance.
  - Federated learning and explainable AI are emerging trends to address trust and privacy in robo-advisory.
key_figures_tables:
  - Table 1: Comparison of early robo-advisory models, highlighting rule-based core algorithms, limited dynamic adjustment, and simple investment strategies.
  - Table 2: Timeline of AI integration in robo-advisory, showing progression from personalized AI agents to reinforcement learning and evolutionary algorithms.
  - Table 3: Comparison of risk profiling methods, contrasting traditional static questionnaires with AI-enhanced approaches using deep learning and NLP.
  - Table 4: Behavioral biases and mitigation strategies, listing loss aversion, confirmation bias, anchoring, overconfidence, and herding bias with corresponding AI interventions.
  - Table 5: Key challenges and mitigation strategies for data privacy, security, regulatory compliance, ethical concerns, and trust in AI recommendations.
key_equations:
  - equation: A_t = f(M_t, I_t)
    explanation: Optimal asset allocation at time t is a function of market conditions and investor needs.
  - equation: R^2
    explanation: Coefficient of determination indicating model fit for traditional risk profiling.
  - equation: f(x)
    explanation: AI-driven risk preference representation where x represents diverse data inputs.
  - equation: B_s
    explanation: Bias score representing the influence of a specific behavioral bias on investment decisions.
definitions:
  - term: Robo-advisor
    definition: An automated investment platform using algorithms to manage portfolios with minimal human intervention.
  - term: Reinforcement Learning (RL)
    definition: A machine learning paradigm where agents learn optimal actions through trial and error interactions with an environment.
  - term: Natural Language Processing (NLP)
    definition: A field of AI that enables computers to understand, interpret, and generate human language.
  - term: Explainable AI (XAI)
    definition: AI systems designed to provide transparent and understandable explanations for their decisions.
  - term: Federated Learning
    definition: A machine learning approach that trains models across decentralized data sources without sharing raw data.
critical_citations:
  - "[Shetty et al., 2026] — Foundational work on robo-advisors redefining wealth management with AI."
  - "[Shen et al., 2025] — Data-driven wealth management model analysis for AI empowering robo-advisors."
  - "[Tahvildari, 2025] — Systematic review of generative AI in robo-advisory, identifying opportunities and challenges."
  - "[Rizinski and Trajanov, 2025] — Scientific review of AI agent-based systems in finance and fintech."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Reviews AI-driven risk assessment and behavioral profiling using deep learning and NLP.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: Discusses asset allocation strategies but not specific budgeting frameworks.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: contextual
      justification: Focuses on investment allocation rather than budget recommendation.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: low
      justification: Mentions optimization in portfolio allocation but not budget constraints.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Does not directly address anomaly detection in spending data.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Dedicated section on data privacy, security, and regulatory compliance for robo-advisors.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Emphasizes transparency and explainability as essential for building user trust.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Compares AI algorithms and evaluates performance in various scenarios.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Comparative analysis of deep learning, RL, and genetic algorithms for asset allocation.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: contextual
      justification: Mentions financial goals like retirement and education but not savings goal management.
  contribution: This review paper provides a comprehensive overview of AI-driven personalized asset allocation, mapping techniques like reinforcement learning, deep learning, and NLP to the robo-advisory context. It directly informs Odin's behavioral profiling module by discussing AI-driven risk assessment from transaction data and communication. The review also contributes to Odin's data privacy and trust considerations by systematically addressing encryption, compliance, and explainability challenges. Additionally, its discussion of adaptive allocation strategies offers conceptual background for Odin's budget recommendation and forecasting modules.
  directly_justifies:
    - AI-driven risk assessment can be extended to financial behavioral profiling for young professionals.
    - Data privacy frameworks from robo-advisory are directly applicable to PFMS like Odin.
    - Explainable AI techniques are essential for building trust in automated financial recommendations.
    - Behavioral bias mitigation strategies can be integrated into personal finance management systems.
  limits:
    - The review is a survey and does not provide empirical results specific to PFMS or Filipino contexts.
    - Discussion of algorithmic performance is high-level and lacks detailed benchmark comparisons.
    - Limited treatment of cold-start problems or personalized recommendations with sparse user data.
  mapping_rationale: The systematic scan across all 12 functional domains and their associated canonical topic codes flagged relevance primarily in Behavioral Profiling (5.A), Data Privacy (10.A), User Trust (10.B), and System Evaluation (12.A, 12.B). The paper's discussion of AI-driven risk assessment using transaction history and behavioral data maps to 5.A (medium). Its dedicated sections on data encryption, regulatory compliance (GDPR, CCPA), and ethical bias directly inform 10.A and 10.B (high). The comparative analysis of AI algorithms and evaluation of performance in volatile markets relates to 12.A and 12.B (medium). Topics like Expense Categorization (3.A), Filipino Cultural Context (2.A), and Spending Forecasting (6.A) were considered but rejected because the paper focuses on investment allocation rather than spending categorization or forecasting. Borderline cases include 7.A (Budgeting Strategies) and 7.B (Budget Recommendation), which are tangentially related through asset allocation but not directly applicable to PFMS budgeting. Overall, the paper provides high-value insights for Odin's privacy, trust, and evaluation modules but limited direct applicability to core PFMS functionalities like expense tracking and budget recommendations.
limitations:
  - The paper is a review and does not present novel empirical findings. [unacknowledged]
  - It does not address the cold-start problem or zero-shot scenarios common in PFMS adoption.
  - The review lacks specific guidance on implementing AI in low-data environments.
  - It does not consider the unique financial behaviors of Filipino young professionals.
  - None identified.
remember_this:
  - AI-driven risk assessment improves personalization by analyzing transaction history and communication patterns.
  - Reinforcement learning enables dynamic portfolio adaptation to changing market conditions.
  - Mitigating cognitive biases like loss aversion requires explicit AI interventions and bias scoring.
  - Data privacy and explainability are critical barriers to user trust in automated financial advice.
  - num: AI-enhanced asset allocation shows improved performance in volatile markets compared to static approaches.
```
---

## Paper 33: Dhanekula & Munira_summarized.md

**Source File:** `Dhanekula & Munira_summarized.md`

```yaml
paper_id: 10.63125/p4y4te47
designation: international-algorithm-specific
title: Deep Neural Network Models for Real-Time Financial Forecasting and Market Intelligence
authors: Dhanekula, A.; Munira, M. S. K.
year: 2026
venue: American Journal of Advanced Technology and Engineering Solutions
odin_topics:
  - 6.A
  - 6.B
  - 7.A
  - 8.A
  - 10.A
  - 10.B
  - 12.A
  - 12.B
  - 12.C
tldr: DNN forecasting effectiveness depends heavily on data integrity and system robustness, while market intelligence outcomes are driven by forecast performance and explanation quality.
problem_and_motivation: Decision teams lack quantitative evidence on which operational capabilities drive real-time forecasting effectiveness and whether forecasting gains convert into decision-ready market intelligence. This gap limits the governance and user-centered adoption of DNN forecasting platforms.
approach:
  - Quantitative cross-sectional case-study design with N=210 active users of a DNN forecasting service.
  - Five-point Likert survey measuring DQ, FR, UR, ROB, EQ, FE, and MIE.
  - Reliability testing with Cronbach's alpha, Pearson correlations, and two multiple regression models.
  - Diagnostic checks for multicollinearity and residuals to support valid inference.
  - Descriptive statistics and hypothesis testing with standardized coefficients and model fit indicators.
findings:
  - num: Reliability was strong across all constructs with Cronbach's alpha ranging from .84 to .90.
  - num: DQ (M=4.12), FR (M=3.98), UR (M=3.85), ROB (M=3.90), EQ (M=3.76), FE (M=3.94), and MIE (M=4.01) were all perceived as high.
  - num: DNN capability correlated with FE (r=.68) and MIE (r=.62); FE correlated with MIE (r=.71).
  - num: Regression Model 1 explained 56% of FE variance with DQ (β=.32), ROB (β=.28), FR (β=.21), and UR (β=.14) as significant predictors.
  - num: Regression Model 2 explained 61% of MIE variance with FE (β=.52), EQ (β=.29), and UR (β=.12) as significant predictors.
  - Data quality and robustness were the strongest drivers of perceived forecasting effectiveness.
  - Explanation quality strongly predicted market intelligence effectiveness beyond forecast performance.
  - All eight hypotheses were supported at p < .05.
key_figures_tables:
  - Figure 1: DNN-Driven Real-Time Financial Forecasting → Shows the workflow from data to market intelligence.
  - Figure 2: Real-Time Financial Forecasting Concepts → Summarizes metrics and challenges like noise and loss functions.
  - Figure 3: Market Intelligence Framework → Links information sources to decision actions.
  - Figure 4: DNN Architectures → Depicts LSTM, CNN, and hybrid models for forecasting.
  - Figure 5: Data Inputs → Covers technical, fundamental, and alternative data sources.
  - Table 1: Respondent Demographics → Details role, experience, and usage frequency of the sample.
  - Table 2: Descriptive Statistics → Shows mean and SD for each construct.
  - Table 3: Cronbach's Alpha → Confirms strong internal consistency for all scales.
  - Table 4: Correlation Matrix → Shows significant positive associations among all constructs.
  - Table 5: Regression for FE → Reports standardized coefficients and model fit.
  - Table 6: Regression for MIE → Reports standardized coefficients and model fit.
  - Table 7: Hypothesis Summary → Lists all supported hypotheses with evidence.
key_equations:
  - equation: NB = γ0 + γ1·SQ + γ2·IQ + γ3·U + γ4·US + ε
    explanation: Perceived net benefit as a function of system and information quality.
  - equation: TP = α0 + α1·TTF + α2·ITeF + α3·TaIF + ε
    explanation: Task performance predicted by task-technology, individual-technology, and task-individual fit.
  - equation: WOA = (F − I) / (A − I)
    explanation: Weight-on-advice measure of reliance on algorithmic outputs.
  - equation: C = (1/k)·Σ_{i=1..k} x_i
    explanation: Composite score as the mean of item responses.
  - equation: α = (k/(k−1))·(1 − Σσ_i^2/σ_T^2)
    explanation: Cronbach's alpha for internal consistency.
definitions:
  - term: DQ
    definition: Data Quality – accuracy, completeness, timeliness of input streams.
  - term: FR
    definition: Feature Richness – breadth of technical, macro, and alternative features.
  - term: UR
    definition: Update Responsiveness – frequency of model and feature refresh.
  - term: ROB
    definition: Robustness – stability of outputs under noisy or shifting conditions.
  - term: EQ
    definition: Explanation Quality – clarity and usefulness of forecast rationales.
  - term: FE
    definition: Forecasting Effectiveness – perceived accuracy, timeliness, and stability of forecasts.
  - term: MIE
    definition: Market Intelligence Effectiveness – perceived actionability and decision support from forecasts.
critical_citations:
  - "[Gu et al., 2020] — ML improves asset pricing via nonlinear interactions."
  - "[Fischer & Krauss, 2018] — LSTM networks for financial market predictions."
  - "[Sirignano & Cont, 2019] — Deep learning for limit order book features."
  - "[Dietvorst et al., 2015] — Algorithm aversion after seeing errors."
  - "[Shin, 2021] — Explainability and causability affect trust and acceptance."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly evaluates DNN-based predictive modeling for forecasting effectiveness.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Tests DNN forecasting algorithms and identifies key drivers like data quality and robustness.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: Discusses forecast evaluation and decision support, which inform budgeting strategies.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Mentions robustness and stability, which are relevant to anomaly detection baselines.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Recommends integrity controls and secure deployment for forecasting pipelines.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Finds that explanation quality significantly predicts intelligence effectiveness and trust.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Uses a structured evaluation framework with reliability testing and regression modeling.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Evaluates DNN capability dimensions and their predictive influence on outcomes.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: The regression methodology can be applied to evaluating budget recommendation systems.
  contribution: "This paper provides a validated framework for evaluating DNN-driven financial forecasting as a market intelligence service. It demonstrates that forecasting effectiveness is the central mechanism linking technical capability to decision intelligence. The findings directly justify Odin's emphasis on data quality and system robustness in its forecasting module. The strong predictive role of explanation quality supports Odin's design for transparent and interpretable recommendations. The study's regression-based evaluation methodology offers a template for Odin's own system evaluation and hypothesis testing."
  directly_justifies:
    - "Data quality and robustness are the strongest predictors of forecasting effectiveness."
    - "Explanation quality is a significant independent predictor of market intelligence effectiveness."
    - "Forecasting effectiveness strongly mediates the link between capability and intelligence outcomes."
    - "Perceived forecasting performance and intelligence value are closely tied in user experience."
  limits:
    - "Cross-sectional design limits causal inference."
    - "Single case-study setting constrains generalizability."
    - "Self-reported Likert data may be subject to common method bias."
    - "Nonstationarity and regime changes are not captured by the snapshot design."
    - "The framework simplifies complex technical realities with linear regression."
  mapping_rationale: "All 12 functional domains and their associated topic codes were systematically scanned. The paper's core focus on DNN forecasting and user perceptions directly maps to high relevance for Predictive Modeling (6.A) and Forecasting Algorithms (6.B), as it evaluates DNN effectiveness and driver identification. The findings on explanation quality and user trust provide high relevance to User Trust (10.B). The paper's evaluation design offers high relevance to System Evaluation (12.A) and medium relevance to Algorithmic Module Evaluation (12.B) and Budget Recommendation Methodologies (12.C). Domains related to Filipino cultural context (2.A-D), Expense Categorization (3.A-C), Existing Systems (4.A-B), Behavioral Profiling (5.A-C), Anomaly Detection (8.B-C), Mobile-First Design (9.A-B), User Retention (11.A-B), and Savings/Debt Management (13.A-C) were considered but rejected due to no direct mention of personal finance, Filipino users, or specific PFMS features. The paper's contribution is highly relevant to Odin's forecasting and evaluation modules, providing evidence for design decisions on data integrity, robustness, and explainability."
limitations:
  - "Cross-sectional design prevents definitive causal inference. [unacknowledged]"
  - "Single case-study setting limits generalizability to other organizations. [unacknowledged]"
  - "Self-reported perceptions may not align with objective economic outcomes. [unacknowledged]"
  - "Nonstationarity and regime changes are not captured by the snapshot design. [unacknowledged]"
  - "Linear regression may oversimplify complex non-linear interactions in the data. [unacknowledged]"
remember_this:
  - "Data quality and robustness are the strongest drivers of forecasting effectiveness."
  - "Explanation quality is critical for converting forecasts into actionable intelligence."
  - "Forecasting effectiveness mediates the relationship between capability and intelligence."
  - "num: The regression model explained 61% of market intelligence effectiveness variance."
  - "DNN capability must be evaluated as an end-to-end service, not just a model."
```
---

## Paper 34: Cabalfin et al_summarized.md

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

## Paper 35: Islam A. et al_summarized.md

**Source File:** `Islam A. et al_summarized.md`

```yaml
paper_id: "d8f4b2a5-6e7c-4b3d-9f1a-2c5d8e7f9a0b" # No DOI available
designation: "international-algorithm-specific"
title: "Benchmarking Machine Learning Models for Real-Time Fraud Detection in Digital Banking Transactions"
authors: "Islam, A.; Miah, M.; Akhir, A.; Munni, A.; Jahan, I.; Nashid, S."
year: 2026
venue: "SSRN"
odin_topics:
  - "6.A"
  - "8.A"
  - "8.B"
  - "12.A"
  - "12.B"
tldr: "Benchmarks machine learning models for real-time fraud detection, evaluating accuracy, latency, throughput, and cost on two datasets."
problem_and_motivation: "Existing fraud detection systems suffer from high false-positive rates and lack real-time feasibility. Accuracy alone is insufficient; operational latency and cost must be balanced. A comprehensive benchmark is needed to guide model selection for live banking environments."
approach:
  - "Used ULB credit card fraud dataset (284,807 transactions) and PaySim synthetic dataset (6.36 million transactions)."
  - "Preprocessed data via cleaning, normalization, feature engineering, and SMOTE oversampling to address class imbalance."
  - "Evaluated cost-sensitive logistic regression, random forest, XGBoost, LightGBM, LSTM, TCN, and Transformer models."
  - "Measured predictive metrics (precision, recall, F1, ROC-AUC, PR-AUC) and real-time metrics (average/95th percentile latency, throughput)."
  - "Performed cost–benefit analysis quantifying financial impact of false positives and false negatives."
  - "Implemented a streaming evaluation framework using Apache Kafka and Spark/Flink for latency and throughput testing."
findings:
  - "num: XGBoost achieved near-perfect ROC-AUC of 0.9998 and PR-AUC of 0.966 on PaySim, outperforming other models."
  - "num: Deep learning models (LSTM, TCN, Transformer) processed 15,000+ transactions per second with sub-millisecond latencies."
  - "num: Random Forest exhibited highest latency (7.6 ms) and lowest throughput (130 tx/sec) on ULB."
  - "Gradient-boosted trees provided superior scalability and real-time responsiveness compared to deep models."
  - "Cost–benefit analysis revealed that minimizing false positives and latency yields significant operational savings."
  - "Adaptive retraining effectively mitigated concept drift, preserving detection performance over time."
  - "A hybrid layered pipeline (lightweight models for initial screening, deep models for secondary verification) balances accuracy and efficiency."
key_figures_tables:
  - "Table 2: ULB predictive performance → XGBoost and Random Forest achieve highest F1 scores."
  - "Table 3: PaySim predictive performance → XGBoost achieves near-perfect ROC-AUC and PR-AUC."
  - "Table 4: ULB real-time performance → Deep learning models have highest throughput."
  - "Table 5: PaySim real-time performance → Deep models sustain >15k tx/sec with low latency."
  - "Figure 22: Cost vs F1 plot → Models with slightly lower F1 but much lower cost are more practical."
key_equations:
  - equation: "$f(x) = w^T x + b, \\quad p(y=1|x) = \\sigma(f(x))$"
    explanation: "Logistic regression linear score and probability."
  - equation: "$\\text{Gain} = \\frac{1}{2} \\left( \\frac{G_L^2}{H_L+\\lambda} + \\frac{G_R^2}{H_R+\\lambda} - \\frac{(G_L+G_R)^2}{H_L+H_R+\\lambda} \\right) - \\gamma$"
    explanation: "XGBoost split gain used for tree growth."
  - equation: "$i_t = \\sigma(W_{ix} x_t + U_{ih} h_{t-1} + b_i), \\quad f_t = \\sigma(W_{fx} x_t + U_{fh} h_{t-1} + b_f), \\quad o_t = \\sigma(W_{ox} x_t + U_{oh} h_{t-1} + b_o)$"
    explanation: "LSTM gate equations for input, forget, and output."
definitions:
  - term: "ML"
    definition: "Machine learning."
  - term: "LSTM"
    definition: "Long short-term memory, a recurrent neural network for sequence data."
  - term: "TCN"
    definition: "Temporal convolutional network, a dilated causal CNN for sequences."
  - term: "XGBoost"
    definition: "Extreme Gradient Boosting, a gradient-boosted tree ensemble."
  - term: "ROC-AUC"
    definition: "Area under the receiver operating characteristic curve."
  - term: "PR-AUC"
    definition: "Area under the precision-recall curve."
critical_citations:
  - "[Dal Pozzolo et al., 2018] — Concept drift in fraud detection."
  - "[Jurgovsky et al., 2018] — Sequence classification for credit-card fraud."
  - "[Bahnsen et al., 2016] — Feature engineering for credit card fraud."
  - "[Carcillo et al., 2019] — Scalable streaming fraud detection framework."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Benchmarks predictive models for fraud detection, applicable to spending prediction."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Directly addresses anomaly detection in transaction data, a core Odin module."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Evaluates multiple algorithms (LSTM, XGBoost, etc.) for anomaly detection."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides a comprehensive evaluation framework including accuracy, latency, and cost."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Evaluates algorithmic modules with multiple metrics and trade-off analysis."
  contribution: "This paper offers a rigorous benchmarking methodology that can be adapted to evaluate Odin's anomaly detection module. It highlights the importance of considering latency, throughput, and cost alongside predictive accuracy, which is crucial for Odin's real-time mobile-first design. The proposed hybrid layered pipeline provides a practical architecture for balancing detection performance and operational efficiency. The cost–benefit framework can be reused to quantify the financial impact of false alerts and missed detections in Odin. Overall, the paper's experimental approach and findings directly inform the design and evaluation of Odin's algorithmic components."
  directly_justifies:
    - "Lightweight models can serve as first-line screening for high-volume transactions in Odin."
    - "Hybrid pipelines balance detection accuracy and latency in real-time personal finance systems."
    - "Concept drift adaptation is essential for maintaining model performance over time."
    - "Cost–benefit analysis should guide Odin's anomaly detection threshold selection."
  limits:
    - "Datasets are banking transactions, not personal spending data; applicability to spending patterns is not validated."
    - "The paper does not address user-specific spending behavior or seasonal patterns, limiting direct transferability."
    - "None identified."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The domains flagged as relevant are: Existing Systems & Gaps (4.A, 4.B) – considered but rejected because the paper focuses on fraud detection rather than personal finance systems, though it does review ML-based systems; Behavioral Profiling (5.A, 5.B) – rejected because the paper does not address user profiles; Spending Forecasting (6.A, 6.B) – selected 6.A as medium because predictive modeling is central, and 6.B as contextual because sequence models are used but for detection not forecasting; Anomaly Detection (8.A, 8.B) – selected as high because fraud detection is a direct analog of anomaly detection; System Evaluation (12.A, 12.B, 12.C) – selected 12.A and 12.B as medium for evaluation framework, 12.C rejected as budget recommendation is unrelated; Data Privacy (10.A) – rejected because privacy is only briefly mentioned. The paper's primary contribution is algorithmic benchmarking with a strong evaluation component, making it most relevant to anomaly detection and system evaluation topics. Overall, the paper provides actionable insights for Odin's anomaly detection module design and evaluation."
limitations:
  - "The use of synthetic and anonymized datasets limits generalizability to real-world banking environments."
  - "Only two datasets were used; broader validation across diverse fraud typologies is needed."
  - "The study does not address explainability or regulatory compliance in depth."
  - "Concept drift mitigation was tested but not under long-term operational conditions. [unacknowledged]"
  - "Personal finance context (e.g., spending habits, savings goals) is not considered."
remember_this:
  - "XGBoost achieved near-perfect ROC-AUC of 0.9998 on PaySim."
  - "Deep learning models offer high throughput but higher latency and cost."
  - "Hybrid layered pipelines balance detection accuracy and real-time responsiveness."
  - "Cost–benefit analysis should prioritize reducing false positives and latency."
  - "Adaptive retraining is critical to maintain performance under concept drift."
```
---

## Paper 36: Kristiana et al_summarized.md

**Source File:** `Kristiana et al_summarized.md`

```yaml
paper_id: 10.1109/OJCS.2026.3658518
designation: international-algorithm-specific
title: Validating AI-Driven Nudge Recommendations: A/B Testing Two-Tower and Bandit Models in Simulated Digital Banking Environment
authors: Kristiana, I.; Prabowo, H.; Lumbangaol, F.; Qomariyah, N. N.
year: 2026
venue: IEEE Open Journal of the Computer Society
odin_topics:
  - 4.B
  - 5.A
  - 5.C
  - 6.A
  - 11.A
  - 12.A
  - 12.B
  - 4.A
  - 6.B
  - 9.A
  - 9.B
tldr: A hybrid recommendation model combining Two-Tower Network static personalization with Multi-Armed Bandit adaptive nudge selection increases recommendation-following behavior from 13.6% to 52.87% in a simulated digital banking A/B test.
problem_and_motivation: Existing recommender systems in banking rely on collaborative or content-based filtering that fail due to data sparsity, cold-start problems, and the absence of behavioral mechanisms. No empirically validated model integrates static personalization, real-time adaptive learning, and explicit behavioral nudge design for financial decision support.
approach:
  - Data was collected from 214 control and 174 treatment verified bank customers via a 54-item behavioral questionnaire and mobile banking simulation with purchase-like actions.
  - A Two-Tower Network with 128-64-128 architecture generates user and product embeddings using PCA dimensionality reduction and SMOTE oversampling for class balance.
  - A Multi-Armed Bandit with ε-greedy policy and Gaussian reward feedback adaptively selects among nine nudge mechanisms based on TWN-generated relevance scores.
  - Sequential A/B testing compared rule-based nudging (App v1) against TWN+MAB-driven nudging (App v2) with no participant overlap between groups.
  - Evaluation used chi-square testing, odds ratio calculation, reward trajectory analysis, and regret analysis against empirical optimal arm.
  - A TWN-only ablation baseline isolated the effect of behavioral nudging and adaptive bandit layer beyond static personalization.
findings:
  - num: Purchase conversion rose from 48.6% in control to 62.07% in treatment, a relative improvement of 27.7%.
  - num: Recommendation-aligned purchases increased from 13.6% to 52.87%, representing a fourfold behavioral shift.
  - num: Chi-square test confirmed statistical significance (χ2 = 6.49, p < 0.0108).
  - num: Odds ratio of 7.15 indicates treatment users are over seven times more likely to follow recommendations than control users.
  - 100% of recommendation-driven purchases in the treatment group aligned with the MAB's empirically optimal arm.
  - Smoothed regret trajectories remained below 0.10-0.15 threshold, demonstrating stable bandit learning without policy divergence.
  - Event-level reward trajectories remained stable over interaction rounds, confirming robust online adaptation under noisy feedback.
key_figures_tables:
  - Figure 1: DSR methodology diagram → Illustrates the research framework from problem identification to evaluation.
  - Figure 2: A/B testing research flow → Shows control and treatment group allocation and measurement pipeline.
  - Figure 3: Integrated TWN+MAB architecture → Visualizes embedding generation, bandit decision, and nudge deployment.
  - Figure 4: Reward trajectories under MAB → Stable event-level reward confirms robust online learning.
  - Figure 5: Smoothed instant regret → Regret stays below threshold, validating exploration-exploitation balance.
  - Table 1: TWN configuration parameters → 128-64-128 architecture with 20 epochs and SMOTE oversampling.
  - Table 2: A/B testing metrics → Direct comparison of control and treatment behavioral outcomes.
key_equations:
  - equation: Q_{t+1}(a) = Q_t(a) + (1/N_t(a)) * (R_t - Q_t(a))
    explanation: Incremental reward estimate update for each product arm in MAB.
  - equation: a_t = argmax_a Q_t(a) with probability 1-ε, else random arm
    explanation: ε-greedy policy selects best arm or explores randomly.
definitions:
  - term: TWN
    definition: Two-Tower Network for learning deep user and product embeddings via dual-encoder architecture.
  - term: MAB
    definition: Multi-Armed Bandit for adaptive online learning balancing exploration and exploitation.
  - term: DSR
    definition: Design Science Research methodology for building and evaluating artifacts.
  - term: CF
    definition: Collaborative Filtering recommender system based on user-item interaction similarity.
  - term: CBF
    definition: Content-Based Filtering recommender system using item attribute similarity.
  - term: SMOTE
    definition: Synthetic Minority Oversampling Technique for addressing class imbalance.
  - term: PCA
    definition: Principal Component Analysis for dimensionality reduction while preserving variance.
critical_citations:
  - "[Thaler and Sunstein, 2008] — Foundation of nudge theory for choice architecture."
  - "[Jesse and Jannach, 2021] — Digital nudging with recommender systems survey."
  - "[Kristiana et al., 2025] — Prior work establishing AI-driven nudge optimization framework."
  - "[Yi et al., 2019] — Neural modeling for large corpus item recommendations."
  - "[Bouneffouf et al., 2020] — Survey on multi-armed bandit applications."
relevance:
  topics:
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly identifies CF/CBF limitations in banking and proposes hybrid solution.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Builds user embeddings from 54-item behavioral questionnaire for personalization.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Two-Tower Network classifies users into behavioral profiles via embeddings.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: TWN predicts user-product relevance scores as static personalization backbone.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: A/B testing measures behavioral engagement through purchase and recommendation-following.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Controlled A/B testing with chi-square validation provides evaluation methodology.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Separately evaluates TWN static personalization and MAB adaptive nudge selection.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews existing recommender systems in banking and their limitations.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: MAB adapts sequentially based on real-time user feedback and reward signals.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Evaluation conducted in a mobile banking simulator mirroring real application behavior.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Nudge mechanisms are presented through mobile UX with framing, saliency, and just-in-time cues.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Paper does not address anomaly detection; focus is on recommendation and nudging.
  contribution: The paper provides a validated hybrid architecture combining Two-Tower Network static personalization with Multi-Armed Bandit adaptive nudge selection that can inform Odin's recommendation and behavioral profiling modules. The A/B testing framework with chi-square validation offers a rigorous evaluation template for Odin's algorithmic modules. The finding that adaptive nudging significantly outperforms rule-based baselines justifies investing in real-time personalization for user engagement. The paper's emphasis on behavioral profiling via multi-dimensional questionnaires aligns with Odin's user classification needs.
  directly_justifies:
    - "Combining static personalization with adaptive learning increases recommendation-following by fourfold."
    - "Behavioral nudges delivered through AI models significantly influence financial decision-making."
    - "A/B testing with verified bank customers provides causal evidence for nudge effectiveness."
    - "Two-Tower Networks can address cold-start and sparsity in financial recommendation contexts."
    - "Multi-Armed Bandits enable real-time nudge optimization without premature convergence."
  limits:
    - "Simulated environment lacks real financial consequences, reducing ecological validity."
    - "Sequential quasi-experimental design allows potential time-based confounding."
    - "Training data from a single Indonesian bank may not generalize to Filipino young professionals."
    - "Ethical challenges around autonomy and fairness are acknowledged but not empirically addressed. [unacknowledged]"
  mapping_rationale: A systematic scan across all 12 functional domains and 31 canonical topic codes was performed. The paper was flagged as relevant primarily to Domains 4 (Existing Systems), 5 (Behavioral Profiling), 6 (Forecasting), 11 (Engagement), and 12 (Evaluation). Topic codes 4.B, 5.A, 5.C, 6.A, 11.A, 12.A, and 12.B were assigned high relevance because the paper directly addresses limitations of existing systems, builds behavioral profiles, applies predictive modeling, measures engagement, and provides A/B testing evaluation. Topic codes 4.A, 6.B, 9.A, and 9.B were assigned medium relevance as supporting context for system landscape, sequential adaptation, and mobile UX. Topic 8.A (Anomaly Detection) was considered and rejected as the paper does not address anomaly detection. Domains 2 (Cultural Context), 3 (Expense Categorization), 7 (Budget Recommendation), 10 (Privacy), and 13 (Savings/Debt) were considered and rejected as the paper focuses on recommendation and nudging rather than these specific PFMS functions. The paper is overall relevant to Odin's personalization and evaluation modules, though its Indonesian banking context limits direct cultural applicability.
limitations:
  - "Experiments conducted in simulated environment, not real financial application."
  - "Sequential A/B design with non-overlapping deployment windows may allow time-based confounds."
  - "Training corpus from a single domain limits generalizability to sparse or underrepresented users."
  - "Ethical safeguards for user autonomy and fairness were not empirically tested."
  - "Real-world deployment would require Responsible AI guardrails not explored in study. [unacknowledged]"
remember_this:
  - "AI-driven nudging increased recommendation-following from 13.6% to 52.87%."
  - "Hybrid TWN+MAB architecture outperformed rule-based baseline across all behavioral metrics."
  - "MAB achieved stable regret below threshold with 100% alignment on optimal arm."
  - "Statistical significance confirmed by chi-square test (p < 0.0108)."
  - "Odds ratio of 7.15 for recommendation-following behavior under AI treatment."
```
---

## Paper 37: Claros et al_summarized.md

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

## Paper 38: Mienye et al-2026_summarized.md

**Source File:** `Mienye et al-2026_summarized.md`

```yaml
paper_id: 10.3390/info17040395
designation: international
title: Deep Learning for Credit Risk Prediction: A Survey of Methods, Applications, and Challenges
authors: Mienye, I. D.; Esenogho, E.; Modisane, C.
year: 2026
venue: Information
odin_topics:
  - 3.A
  - 4.A
  - 4.B
  - 5.A
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
  - 12.C
tldr: A survey of deep learning architectures for credit risk prediction, covering MLPs, RNNs, CNNs, Transformers, and GNNs, with a synthesis of methods, applications, and deployment challenges.
problem_and_motivation: Traditional credit risk models like logistic regression struggle to capture nonlinear relationships and temporal dynamics in modern financial datasets. While advanced ML methods offer higher accuracy, they often sacrifice interpretability and fail to model sequential or relational dependencies. There is a need for a systematic synthesis of deep learning approaches tailored to borrower-level credit risk to bridge academic research and industry deployment.
approach:
  - Conducted a structured literature search across IEEE Xplore, Scopus, ACM, ScienceDirect, and Google Scholar from 2015 to 2025.
  - Screened 380 initial records through title/abstract review and full-text assessment, resulting in 140 application studies and 18 survey papers.
  - Classified studies by data modality (tabular, sequential, textual, relational), architecture (MLP, CNN, RNN, Transformer, GNN), and credit product segment.
  - Synthesized methodological details, datasets, evaluation metrics, and quantitative performance from peer-reviewed sources.
  - Structured challenges into evaluation integrity, imbalanced learning, interpretability, robustness, and governance.
findings:
  - num: Deep tabular models like TabNet-Stacking achieve accuracy up to 0.979 on large-scale credit datasets, outperforming single-model baselines.
  - num: LSTM networks reduce MAE from 0.095 to 0.072 and RMSE from 0.119 to 0.093 for monthly default rate forecasting versus ARIMA.
  - num: Residual-enhanced BiLSTM with multi-head attention achieves AUC=0.982 and F1=0.958 on the Freddie Mac Single-Family dataset.
  - num: Multi-head RGAT achieves AUC=0.799 and KS=0.528 on SME relational graphs, exceeding non-graph baselines.
  - num: Weighted-loss TabTransformer improves accuracy on imbalanced MSME credit data from 86.35% to 89.27%.
  - Transformers and GNNs are increasingly adopted for modeling global dependencies and relational risk propagation in large-scale systems.
  - Most deep learning models outperform traditional scorecards on large, behaviorally rich datasets but show modest gains on small static benchmarks.
  - Interpretability and fairness are often treated as post-hoc add-ons, with limited integration into training objectives.
  - A non-trivial portion of studies still relies on random cross-validation, causing temporal leakage and over-optimistic performance estimates.
key_figures_tables:
  - Table 1: Summary of related reviews on credit risk → Highlights gap in synthesizing modern DL architectures for borrower-level risk.
  - Figure 1: PRISMA flowchart of literature search → Documents screening process resulting in 140 application studies.
  - Figure 2: MLP structure for tabular credit data → Illustrates hierarchical feature learning through nonlinear transformations.
  - Figure 3: LSTM architecture with gating mechanisms → Shows how sequential models capture long-term repayment patterns.
  - Table 4: Summary of DL applications in credit risk → Consolidates methods and performance across model families.
key_equations:
  - equation: "EL = PD × LGD × EAD"
    explanation: "Expected Loss calculation central to Basel risk-weighted assets."
  - equation: "P(y=1|x) = σ(w^T x + b)"
    explanation: "Logistic regression for probability of default."
  - equation: "h_t = tanh(W_h h_{t-1} + W_x x_t + b)"
    explanation: "RNN hidden state update for sequential data."
  - equation: "f_t = σ(W_f [h_{t-1}, x_t] + b_f)"
    explanation: "LSTM forget gate controls memory retention."
  - equation: "Attention(Q,K,V) = softmax(QK^T / √d_k) V"
    explanation: "Transformer self-attention for global dependency modeling."
definitions:
  - term: PD
    definition: Probability of Default, the likelihood a borrower fails to meet repayment obligations.
  - term: LGD
    definition: Loss Given Default, the proportion of exposure not recovered after default.
  - term: EAD
    definition: Exposure at Default, the total outstanding amount when default occurs.
  - term: AUC
    definition: Area Under the ROC Curve, a threshold-agnostic ranking performance metric.
  - term: AUPRC
    definition: Area Under the Precision-Recall Curve, sensitive to minority-class performance.
  - term: MLOps
    definition: Machine Learning Operations, practices for deploying and maintaining ML systems.
critical_citations:
  - "[Lessmann et al., 2015] — Benchmarking classifiers for credit scoring."
  - "[Gunnarsson et al., 2021] — Empirical study on when DL is beneficial."
  - "[Rudin, 2019] — Critique of black-box explanations for high-stakes decisions."
  - "[Vaswani et al., 2017] — Introduced the Transformer architecture."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: Discusses feature categorization for credit scoring but not spending categories.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews traditional and ML-based credit scoring as part of the financial system landscape.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Critically identifies gaps in evaluation, interpretability, and governance of existing systems.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Sequential models capture behavioral trajectories linked to repayment patterns.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Focuses on predictive modeling for default probability, a core predictive task.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Reviews LSTMs and GRUs for forecasting default rates from sequential repayment data.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: Discusses risk-based pricing and capital allocation but not personal budgeting strategies.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Does not address budget recommendation, only default prediction.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Credit default is an extreme financial anomaly, providing a related detection context.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: DL architectures for credit risk can be adapted for anomaly detection in spending.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Discusses privacy-preserving learning and differential privacy as emerging research directions.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Interpretability and fairness are central to building user and regulator trust.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a detailed critique of evaluation integrity, including calibration and temporal validation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Reviews evaluation metrics (AUC, AUPRC) and validation designs for DL modules.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: contextual
      justification: Focuses on credit risk evaluation, not budget recommendation specifically.
  contribution: This survey provides a unified taxonomy of deep learning methods for credit risk that maps model families to data structures and risk objectives, which can inform Odin's module selection. It offers a critical synthesis of evaluation challenges, including temporal leakage and calibration decay, directly relevant to Odin's forecasting and recommendation modules. The paper also outlines emerging research directions in interpretability, fairness, and privacy, providing a roadmap for designing trustworthy and regulation-ready features for Odin. Its detailed review of sequential and relational models supports Odin's development of behavioral profiling and anomaly detection functionalities. The identified gaps in current practice, such as limited cost-sensitive reporting and weak governance, guide Odin's evaluation and product strategy.
  directly_justifies:
    - "Sequential architectures like LSTMs are beneficial for dynamic behavioral scoring when historical data is rich."
    - "Transformers can unify heterogeneous signals, making them suitable for complex multimodal Odin data."
    - "Out-of-time validation and calibration metrics are essential for reliable model evaluation in production."
    - "Interpretability and fairness should be integrated at training time, not just as post-hoc add-ons."
    - "Privacy-preserving techniques like federated learning are needed for cross-institutional data collaboration."
  limits:
    - "The survey is limited to peer-reviewed English-language studies indexed in major databases."
    - "Performance comparisons across studies are not standardized due to varying datasets and evaluation protocols."
    - "The review does not cover proprietary implementations or regulatory grey literature."
    - "The paper focuses on probability of default, with limited coverage of LGD and EAD modelling."
  mapping_rationale: A systematic scan was performed across all 12 functional domains and their associated topic codes. The paper was flagged as highly relevant to Expense Categorization Frameworks (3.A) as it discusses feature categorization for credit risk, though contextual rather than direct. For Existing Systems & Gaps, it was rated high for 4.B (Limitations) due to its critical analysis of evaluation integrity and interpretability, and medium for 4.A (Landscape) for its review of traditional and ML systems. For Behavioral Profiling & Classification, it was rated medium (5.A) because sequential models capture behavioral trajectories. For Spending Forecasting, it was rated high for both 6.A (Predictive Modeling) and 6.B (Forecasting Algorithms) as the core of the paper is predicting default probabilities from financial data. For Budget Recommendation, it received low (7.B) and contextual (7.A) ratings as it does not directly address budget allocation but discusses domain knowledge. For Anomaly Detection, it received medium (8.B) as the architectures are transferable and contextual (8.A) for the related problem. For Data Privacy & Trust, it received medium ratings for 10.A and 10.B due to discussions on differential privacy and the importance of interpretability for trust. For System Evaluation, it was rated high for 12.A (Frameworks) and 12.B (Algorithmic Modules) due to its in-depth coverage of evaluation methodologies and metrics. The topic 12.C (Budget Recommendation Evaluation) was deemed contextual. Topics not selected include those related specifically to Filipino cultural practices (2.A-D), expense category design (3.B, 3.C), user constraints (3.C), cold-start profiling (5.B, 5.C), infeasibility handling (7.D), cold-start anomaly detection (8.C), mobile design (9.A, 9.B), retention (11.A, 11.B), savings (13.A, 13.B), and surplus management (13.C). Overall, the paper is highly relevant for Odin's foundational model selection, evaluation strategy, and consideration of trust and privacy issues.
limitations:
  - "Deep learning models may not always outperform tree-based ensembles on small static benchmarks. [unacknowledged]"
  - "Temporal leakage from random k-fold cross-validation remains common, weakening external validity."
  - "Interpretability and fairness are treated as add-ons rather than integrated training objectives."
  - "Robustness under concept drift and privacy constraints are rarely addressed in empirical studies."
  - "Operational governance and MLOps practices are often absent from research reporting."
remember_this:
  - "Deep models excel with large, behaviorally rich datasets but show modest gains on small static benchmarks."
  - "Out-of-time validation and calibration metrics are essential, yet often overlooked, for reliable evaluation."
  - "Transformers and GNNs are promising for modeling global dependencies and relational risk propagation."
  - "Interpretability and fairness require integration at training time, not just post-hoc explanation."
  - "Privacy-preserving learning and robust MLOps are critical for production-grade credit risk systems."
```
---

## Paper 39: Moury_summarized.md

**Source File:** `Moury_summarized.md`

```yaml
paper_id: 10.63125/0nbg6w69
designation: international-algorithm-specific
title: Machine Learning–Based Transaction Risk Scoring Models for Financial Compliance Monitoring in Foreign Exchange Operations
authors: Moury, R. K.
year: 2026
venue: International Journal of Scientific Interdisciplinary Research
odin_topics:
  - 4.A
  - 4.B
  - 6.A
  - 6.B
  - 7.B
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
  - 12.C
tldr: A quantitative synthesis of 124 records found that ensemble models dominate FX compliance risk scoring, while governance and calibration reporting remain underdeveloped relative to predictive performance metrics.
problem_and_motivation: The literature on machine learning for FX compliance risk scoring is methodologically heterogeneous, making cross-study comparison and synthesis difficult. There is a need to systematically quantify modeling practices, evaluation rigor, and governance instrumentation to identify consistent patterns and gaps. Without such synthesis, it is unclear which methodological choices are most strongly associated with reported performance and operational readiness.
approach:
  - The study is a systematic cross-study evidence synthesis with standardized content analysis and reproducible coding.
  - A total of 124 analytic records were coded from 89 publications using a structured extraction protocol.
  - Coded variables included model family, feature construction, validation design, labeling strategy, evaluation metrics, and governance controls.
  - Descriptive statistics, reliability testing (Cronbach's alpha), and regression analyses (logistic and linear) were conducted.
  - Dependent variables were high predictive performance reporting and governance maturity score, with independent variables including model family, validation rigor, and feature usage.
findings:
  - num: Ensemble models were the most frequently evaluated (44.4%), followed by logistic regression/GLM (37.1%).
  - num: Customer-profile (69.4%) and geographic corridor (62.1%) features were the most common feature groups.
  - num: Discrimination metrics were reported in 82.3% of records, while calibration (34.7%) and cost-sensitive analyses (28.2%) were less common.
  - num: Ensemble (OR=2.27, p=0.008) and neural models (OR=1.99, p=0.041) were significantly associated with high performance reporting.
  - num: Out-of-time validation (OR=2.83, p=0.004) and network feature usage (OR=2.08, p=0.016) were also strong predictors of high performance.
  - num: Operational studies were strongly associated with higher governance maturity scores (β=1.12, p<0.001).
  - Governance and auditability constructs were underreported, with access control in 29.8% and traceability in 22.6% of records.
  - Reliability testing showed strong internal consistency for governance maturity (α=0.86) and documentation completeness (α=0.84).
key_figures_tables:
  - Figure 1: FX Machine Learning Risk Framework → Framework illustrating the risk scoring conversion process.
  - Table 1: Publication and Context Characteristics → Sample is recent, journal-dominant, and uses proprietary datasets.
  - Table 2: Model, Feature, and Governance Characteristics → Ensemble methods and customer profile features are most prevalent.
  - Table 3: Prevalence of Major Construct Families → SAR-based labels and ensemble models dominate.
  - Table 4: Evaluation, Thresholding, and Governance Construct Reporting → Discrimination metrics are common, governance less so.
  - Table 5: Cronbach's Alpha Reliability Results → Governance Maturity Index shows strong reliability (α=0.86).
  - Table 7: Logistic Regression Predicting High Predictive Performance Reporting → Ensemble models and out-of-time validation are significant predictors.
  - Table 8: Linear Regression Predicting Governance Maturity Score → Operational study type and logging coverage are strong predictors.
key_equations:
  - equation: OR = e^{β}
    explanation: Odds ratio from logistic regression, indicating association strength.
definitions:
  - term: FX
    definition: Foreign exchange.
  - term: AML
    definition: Anti-money laundering.
  - term: SAR
    definition: Suspicious activity report.
  - term: GLM
    definition: Generalized linear model.
  - term: ROC
    definition: Receiver operating characteristic.
  - term: AUC
    definition: Area under the curve.
critical_citations:
  - "[Srokosz et al., 2023] — Defines transaction risk scoring."
  - "[Leo et al., 2019] — Discusses machine learning in banking risk."
  - "[Bhatore et al., 2020] — Reviews ML for credit risk."
  - "[Jullum et al., 2020] — ML for money laundering detection."
  - "[Alexandre & Balsa, 2023] — Risk-based AML multiagent system."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: The paper systematically reviews and synthesizes the landscape of ML models for transaction monitoring, directly mapping to PFMS evaluation.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: It explicitly identifies gaps in governance, calibration, and cost-sensitive evaluation, which are key limitations in existing systems.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: The core subject is predictive modeling for risk scoring, which is analogous to spending prediction in PFMS.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: While focused on risk, the discussion of temporal aggregation and out-of-time validation is relevant to forecasting sequential data.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: contextual
      justification: The methods for thresholding and alert prioritization provide a framework for resource allocation, which is conceptually similar to budget allocation.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: The paper extensively reviews unsupervised and semi-supervised methods for anomaly detection, which are directly applicable to PFMS.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: It evaluates specific algorithms like autoencoders for anomaly detection in transactional data.
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: low
      justification: The paper touches on label sparsity, which relates to cold-start, but does not focus on baseline strategies.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: The focus on governance and access controls directly relates to data privacy and security frameworks.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: The emphasis on explainability, auditability, and governance supports building user trust, though user trust is not directly measured.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: The paper provides a comprehensive evaluation framework, including metrics for discrimination, ranking, calibration, and cost-sensitivity.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: It systematically compares and evaluates different algorithmic modules (ensembles, neural nets, etc.) for the risk scoring task.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: The evaluation methodologies (out-of-time validation, subgroup analysis) are transferable to evaluating budget recommendation systems.
  contribution: This systematic review provides a quantitative evidence base that Odin can leverage to justify its choice of ensemble models for predictive tasks and to prioritize the development of robust evaluation frameworks that include ranking and calibration metrics. It also offers a clear rationale for investing in governance and auditability features from the outset, as these are identified as critical gaps in existing systems. The findings on feature engineering, particularly the importance of temporal and relational features, directly inform Odin's data architecture and feature construction strategy.
  directly_justifies:
    - "Ensemble models should be prioritized for predictive modules in PFMS due to their consistent association with strong performance."
    - "Out-of-time validation is essential for reliable model evaluation in dynamic financial environments."
    - "Feature engineering must incorporate temporal aggregation and relational signals to improve model performance."
    - "Governance and auditability controls are critical and should be integrated early in system design."
    - "Evaluation frameworks must include ranking and calibration metrics to align with operational workflows."
  limits:
    - "The evidence base is heavily skewed toward discrimination metrics, limiting understanding of operational calibration."
    - "Governance and auditability constructs were underreported, indicating a gap between research and operational practice."
    - "The focus on suspicious activity detection may not fully capture the breadth of personal finance management needs."
    - "The synthesis relies on reported outcomes, which may be subject to publication bias."
    - "The study does not provide direct empirical validation of any specific PFMS module."
  mapping_rationale: A systematic scan was conducted across all 12 functional domains and their associated topic codes. The paper's primary relevance is to the "Existing Systems & Gaps" (4.A, 4.B), "Spending Forecasting" (6.A, 6.B), "Anomaly Detection" (8.A, 8.B), and "System Evaluation" (12.A, 12.B, 12.C) domains, where it provides high-relevance evidence for model selection, feature engineering, and evaluation frameworks. Medium relevance was assigned to "Data Privacy & User Trust" (10.A, 10.B) due to its focus on governance and auditability, and to "Budget Recommendation" (7.B) due to conceptual parallels in resource allocation. "Behavioral Profiling" (5.A, 5.B, 5.C) and "Filipino Cultural Context" (2.A, 2.B, 2.C, 2.D) were considered and rejected as the paper does not address user profiling or cultural financial practices. The paper's systematic synthesis provides a strong foundation for justifying Odin's technical architecture and evaluation approach, while its identified gaps underscore the need for Odin to incorporate robust governance and calibration features.
limitations:
  - "The analysis relied on information explicitly reported in included studies, leading to missingness for several key constructs."
  - "Performance measures were not uniformly comparable across studies due to heterogeneous datasets and labeling standards."
  - "The evidence base was skewed toward experimental benchmarking and proprietary datasets, limiting generalizability."
  - "Publication bias may have inflated the prevalence of high-performance outcomes."
  - "Governance and auditability indices measured documented controls, not verified operational implementation."
  - "Several key compliance constructs were seldom reported, limiting the ability to test availability-focused propositions. [unacknowledged]"
remember_this:
  - Ensemble models show stronger performance reporting than logistic regression baselines in FX compliance.
  - Out-of-time validation is a key predictor of reliable model performance.
  - Governance and auditability are significantly underreported in the literature.
  - Calibration and cost-sensitive evaluation are crucial but rarely used in practice.
  - Operational deployment studies consistently show higher governance maturity.
```
---

## Paper 40: Miranda et al_summarized.md

**Source File:** `Miranda et al_summarized.md`

```yaml
paper_id: "10.48550/arXiv.2506.12345"
designation: "international-algorithm-specific"
title: "Polyglot Teachers: Evaluating Language Models for Multilingual Synthetic Data Generation"
authors: "Miranda, L. J. V.; Vulic, I.; Korhonen, A."
year: 2026
venue: "arXiv"
odin_topics:
  - "4.B"
  - "12.B"
tldr: "Evaluating ten language models as multilingual teachers for synthetic data generation reveals that model scale does not predict effectiveness; data quality metrics explain over 93% of variance and predict student performance."
problem_and_motivation: "Current teacher model selection for multilingual synthetic data generation is ad hoc, often defaulting to largest models despite capability gaps in non-English languages. This leads to poor-quality data and suboptimal student performance. A systematic characterization of what makes an effective multilingual teacher is missing."
approach:
  - "They evaluate 10 state-of-the-art LMs across 6 typologically diverse languages using three synthetic data generation methods: Generate, Translate, and Respond."
  - "They generate over 1.4 million SFT examples and fine-tune 240 student models from OLMo 3 7B."
  - "They compute intrinsic data quality metrics: prompt/response diversity, perplexity, and a multilingual reward model score."
  - "They measure extrinsic student performance via Performance Gap Recovered (PGR) on cultural, chat, and math benchmarks."
  - "They aggregate intrinsic and extrinsic metrics into a single POLYGLOT SCORE (PG-SCORE) using z-score normalization."
findings:
  - "num: Gemma 3 27B and Aya Expanse 32B achieve the highest average PG-SCORE of 0.726 and 0.706, respectively."
  - "Model scale does not significantly predict teacher effectiveness (p > 0.05)."
  - "Intrinsic data quality metrics explain 93.3% of variance and predict student performance with R^2 = 0.664."
  - "Matching teacher and student model families yields at least +20.5% higher PG-SCORE compared to mismatched pairs."
  - "For low-resource languages, Translate and Respond methods outperform Generate, with gains up to 458.9% for some teachers."
key_figures_tables:
  - "Table 1: PG-SCORE rankings of 10 teacher models across 6 languages → Gemma 3 27B and Aya Expanse 32B are top performers."
  - "Figure 2: PG-SCORE generalizes across different student base models, with family-matched pairs showing consistent improvements."
  - "Table 2: PG-SCORE by data generation method; Generate works best for high-resource languages, Translate/Respond for low-resource."
  - "Figure 4: Linear regression of intrinsic principal components predicts extrinsic student performance with R^2=0.664."
key_equations:
  - equation: "$\\text{Intrinsic}_{T,\\ell} = \\frac{1}{|\\mathcal{M}|} \\sum_{m \\in \\mathcal{M}} z\\text{-score}(m(\\mathcal{D}_{T,\\ell}))$"
    explanation: "Averages z-scored diversity, perplexity, and reward metrics."
  - equation: "$\\text{Extrinsic}_{T,\\ell} = \\frac{1}{|\\mathcal{B}|} \\sum_{b \\in \\mathcal{B}} \\frac{\\text{score}_b(S_{T,\\ell}) - \\text{score}_b(S_\\phi)}{\\text{score}_b(S_{\\text{REF}}) - \\text{score}_b(S_\\phi)}$"
    explanation: "Performance Gap Recovered averaged over benchmark tasks."
  - equation: "$\\text{PG-SCORE}_{T,\\ell} = z\\text{-score}(\\text{Intrinsic}_{T,\\ell} + \\text{Extrinsic}_{T,\\ell})$"
    explanation: "Combined metric for teacher effectiveness."
definitions:
  - term: "PG-SCORE"
    definition: "Metric combining intrinsic data quality and extrinsic student performance to evaluate teacher effectiveness."
  - term: "PGR"
    definition: "Performance Gap Recovered, measures student improvement over base model relative to a reference."
  - term: "SFT"
    definition: "Supervised fine-tuning."
  - term: "LM"
    definition: "Language model."
  - term: "PPL"
    definition: "Perplexity."
critical_citations:
  - "[Kim et al., 2025] — proposed extrinsic-only evaluation for English teachers."
  - "[Xu et al., 2025b] — showed stronger models not always better for English instruction tuning."
  - "[Aryabumi et al., 2024] — Aya dataset for multilingual instruction tuning."
relevance:
  topics:
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "contextual"
      justification: "Identifies limitations in existing ad-hoc teacher selection for multilingual data generation, relevant to gaps in systems."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Proposes a comprehensive evaluation metric (PG-SCORE) combining intrinsic and extrinsic measures, applicable to evaluating algorithmic modules."
  contribution: "The paper's evaluation framework (PG-SCORE) can inform Odin's module evaluation strategy by combining intrinsic data quality metrics with downstream performance. Its findings on family matching and data generation methods may guide the selection of ML models for Filipino-specific tasks. The systematic analysis of data quality predictors offers a methodology for evaluating algorithmic modules without full training runs. However, the paper does not address personal finance or Filipino financial behavior directly."
  directly_justifies:
    - "Intrinsic data quality metrics can serve as proxies for student performance, reducing evaluation cost."
    - "Teacher-student model family matching improves synthetic data quality, a heuristic applicable to model selection."
    - "For low-resource languages, generating responses to existing prompts or translating from English is more effective than generating from scratch."
  limits:
    - "Evaluation limited to 6 typologically diverse languages, may not generalize to all languages."
    - "Translation-based method assumes English prompts and may introduce translationese artifacts."
    - "Potential amplification of biases present in teacher models, especially for underrepresented languages."
    - "The study does not test on personal finance data or Filipino-specific tasks beyond a single held-out case."
  mapping_rationale: "Systematic scan across all 12 functional domains and their associated topic codes flagged only the System Evaluation domain as relevant. Specifically, the paper's contribution of a novel evaluation metric (PG-SCORE) directly supports topic 12.B (Evaluation of Algorithmic Modules) with medium relevance, as it provides a comprehensive methodology for assessing algorithmic performance. Topic 4.B (Limitations and Gaps in Existing Systems) was assigned contextual relevance because the paper identifies ad-hoc teacher selection as a gap in current synthetic data practices, but this is not specific to PFMS. Domains such as Filipino Cultural Context, Expense Categorization, Behavioral Profiling, and Spending Forecasting were rejected because the paper does not address financial behaviors or personal finance applications. Overall, the paper is methodologically relevant to Odin's evaluation strategies but not directly actionable for financial modules."
limitations:
  - "Evaluation limited to 6 typologically diverse languages, may not generalize to all languages."
  - "Translation-based method assumes English prompts and may introduce translationese artifacts."
  - "Potential amplification of biases present in teacher models, especially for underrepresented languages."
  - "The study does not test on personal finance data or Filipino-specific tasks beyond a single held-out case. [unacknowledged]"
remember_this:
  - "Gemma 3 27B and Aya Expanse 32B are the most effective multilingual teachers."
  - "Model scale alone does not predict teacher effectiveness; data quality metrics explain 93% of variance."
  - "Family-matched teacher-student pairs yield at least +20.5% higher performance."
  - "For low-resource languages, Translate and Respond methods outperform Generate with up to 458.9% gains."
  - "Intrinsic data quality metrics can predict student performance with R^2=0.664."
```
---

## Paper 41: Athique & Lorenzana_summarized.md

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

## Paper 42: Mohammad et al_summarized.md

**Source File:** `Mohammad et al_summarized.md`

```yaml
paper_id: "10.1038/s41598-026-51764-9"
designation: "international-algorithm-specific"
title: "Transforming credit risk evaluation in digital lending from black box models to transparent decisions"
authors: "Mohammad, A.A.S.; Mohammad, S.I.; Vasudevan, A.; Azam, S.M.F.; Sevukamoorthy, L.; Parhi, M.; Shankalia, U.M.; Salami, Z.A."
year: 2026
venue: "Scientific Reports"
odin_topics:
  - "4.B"
  - "5.A"
  - "5.C"
  - "6.A"
  - "10.B"
  - "12.B"
tldr: "An optimization-driven hybrid machine learning framework integrating gradient boosting and nature-inspired metaheuristics enhances credit risk prediction accuracy and interpretability for digital lending."
problem_and_motivation: "Traditional credit scoring models cannot assess non-traditional borrowers, while black-box machine learning models lack interpretability, limiting regulatory compliance and trust in digital lending. A unified framework combining predictive performance and transparency is missing."
approach:
  - "Dataset comprises 1000 loan applications with 16 financial, demographic, and behavioral features from University of Santiago de Chile."
  - "Preprocessing includes scaling, encoding, missing value handling, and feature engineering (loan-to-income, installment-to-income ratios)."
  - "Three gradient boosting models (LightGBM, CatBoost, Explainable Boosting Machine) are used for classification."
  - "Hyperparameters are optimized using Brown-Bear Optimization Algorithm and Puma Optimizer metaheuristics over 200 iterations."
  - "Stratified five-fold cross-validation and cost-sensitive learning address class imbalance."
  - "Model interpretability is provided via SHAP and permutation importance analyses."
  - "Evaluation uses accuracy, precision, recall, F1-score, confusion matrices, and Wilcoxon tests."
findings:
  - "num: Optimized LightGBM achieved 0.9901 test accuracy and 0.9901 F1-score."
  - "num: Optimized CatBoost achieved 0.9950 test accuracy and 0.9951 F1-score."
  - "num: Optimized EBM achieved 0.9851 test accuracy and 0.9852 F1-score."
  - "Metaheuristic optimization consistently improved model performance over baseline configurations."
  - "SHAP analysis identified credit age as the most influential predictor of default risk."
key_figures_tables:
  - "Figure 3: Permutation-based feature importance → Highlights key predictors for risk."
  - "Figure 5: Convergence trend of iterative optimization → Shows stable improvement over 200 iterations."
  - "Table 6: Performance metrics for all model configurations → Demonstrates optimization gains."
  - "Table 7: Confusion matrices → Shows reduced misclassifications after optimization."
key_equations:
  - equation: "Accuracy = (TP + TN) / (TP + TN + FP + FN)"
    explanation: "Overall correctness of classification."
  - equation: "Precision = TP / (TP + FP)"
    explanation: "Proportion of true positives among predicted positives."
  - equation: "Recall = TP / (TP + FN)"
    explanation: "Proportion of actual positives correctly identified."
  - equation: "F1 = 2 * (Precision * Recall) / (Precision + Recall)"
    explanation: "Harmonic mean of precision and recall."
definitions:
  - term: "LightGBM"
    definition: "Gradient boosting framework using histogram-based learning."
  - term: "CatBoost"
    definition: "Gradient boosting with native categorical feature handling and ordered boosting."
  - term: "EBM"
    definition: "Explainable Boosting Machine, a transparent additive model with pairwise interactions."
  - term: "BBOA"
    definition: "Brown-Bear Optimization Algorithm, nature-inspired metaheuristic for global search."
  - term: "PO"
    definition: "Puma Optimizer, hunting-inspired metaheuristic for optimization."
  - term: "SHAP"
    definition: "SHapley Additive exPlanations, a game-theoretic approach for model interpretability."
  - term: "BNPL"
    definition: "Buy Now, Pay Later, a short-term financing model."
critical_citations:
  - "[Ke et al., 2017] — LightGBM gradient boosting framework."
  - "[Prokhorenkova et al., 2018] — CatBoost ordered boosting."
  - "[Liu and Sun, 2023] — Explainable Boosting Machine."
  - "[Prakash et al., 2023] — Brown-Bear Optimization Algorithm."
  - "[Abdollahzadeh et al., 2024] — Puma Optimizer."
relevance:
  topics:
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Identifies black-box and tuning gaps relevant to PFMS development."
    - code: "5.A"
      name: "Financial Behavioral Profiles"
      relevance: "medium"
      justification: "Uses financial and behavioral features for borrower profiling."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Proposes a classification framework directly applicable to Odin's behavioral profiling."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Provides predictive modeling techniques transferable to spending forecasting."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "high"
      justification: "Emphasizes interpretability to build user trust and meet regulatory standards."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Uses cross-validation and multiple metrics that can inform Odin's module evaluation."
  contribution: "The optimization-driven classification framework can be directly applied to Odin's behavioral profiling module (5.C) to classify users' spending habits and financial risk levels. The use of interpretable models like EBM supports Odin's transparency requirements (10.B) by providing feature-level explanations of predictions. The evaluation methodology with cross-validation and multiple metrics provides a template for validating Odin's algorithmic modules (12.B). The findings on handling class imbalance via cost-sensitive learning are relevant to Odin's anomaly detection and forecasting tasks."
  directly_justifies:
    - "Optimized gradient boosting models achieve high predictive accuracy on imbalanced financial data."
    - "Feature-level explanations using SHAP enhance model transparency and user trust."
    - "Metaheuristic optimization improves hyperparameter search efficiency and model stability."
    - "Interpretable models like EBM facilitate regulatory compliance in financial decision-making."
  limits:
    - "Focuses on credit risk rather than spending behavior, requiring adaptation for Odin's forecasting modules."
    - "No explicit consideration of Filipino financial practices or seasonal spending patterns."
  mapping_rationale: "All 12 functional domains and their associated topic codes were systematically scanned. Domains related to Filipino cultural context (1, 2) and expense categorization (3) were deemed irrelevant as the paper does not address Filipino-specific practices or expense management. The domain of existing systems and gaps (4) was partially relevant, specifically 4.B (limitations) with medium relevance because the paper identifies black-box and tuning gaps. Behavioral profiling (5) was highly relevant, especially 5.C (classification approaches) as high, and 5.A (profiles) as medium due to use of financial/behavioral features. Predictive modeling (6) was considered medium via 6.A for its techniques, though not directly on spending. User trust (10) was flagged high via 10.B because interpretability is a core contribution. System evaluation (12) was flagged medium via 12.B for its robust evaluation methodology. Other domains (7, 8, 9, 11, 13) were rejected as they do not relate to credit risk or the paper's focus. Overall, the paper offers transferable techniques for classification, interpretability, and evaluation that can inform Odin's design."
limitations:
  - "Dataset size is limited to 1000 instances, which may restrict generalization. [unacknowledged]"
  - "The study uses a public credit dataset rather than actual BNPL data, though this is acknowledged."
  - "No comparison to state-of-the-art benchmark algorithms beyond within-family baselines. [unacknowledged]"
remember_this:
  - "Optimized CatBoost achieved 99.50% test accuracy on credit risk prediction."
  - "Metaheuristic optimization consistently improved model stability and predictive performance."
  - "Interpretable models like EBM provide feature-level explanations critical for regulatory trust."
  - "Cost-sensitive learning effectively addressed class imbalance without synthetic oversampling."
```
---

## Paper 43: Bhardwaj_summarized.md

**Source File:** `Bhardwaj_summarized.md`

```yaml
paper_id: 10.48550/arXiv.2602.22302
designation: international-algorithm-specific
title: Agent Behavioral Contracts: Formal Specification and Runtime Enforcement for Reliable Autonomous AI Agents
authors: Bhardwaj, V.
year: 2026
venue: arXiv preprint # This paper is a pre-print article
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 8.A
  - 8.B
  - 8.C
  - 11.A
  - 11.B
  - 12.A
  - 12.B
tldr: Introduces Agent Behavioral Contracts (ABC), a formal framework with probabilistic satisfaction and drift bounds that brings Design-by-Contract principles to autonomous AI agents for runtime enforcement.
problem_and_motivation: AI agents operate on prompts with no formal behavioral specification, causing drift, governance failures, and project failures. Existing training-time alignment and output guardrails lack runtime enforcement and formal guarantees. This gap necessitates a framework for specifying, verifying, and enforcing agent behavior.
approach:
  - Defines contract C = (P,I,G,R) with hard/soft constraints and recovery.
  - Introduces (p,δ,k)-satisfaction for probabilistic compliance.
  - Proves stochastic drift bounds using Ornstein-Uhlenbeck dynamics.
  - Establishes compositionality conditions for multi-agent chains.
  - Implements in ContractSpec DSL and AgentAssert runtime library.
  - Evaluates on AgentContract-Bench and 7 models from 6 vendors.
findings:
  - num: Contracted agents detect 5.2–6.8 soft violations per session invisible to baselines (p < 0.0001, Cohen's d = 6.7–33.8).
  - num: Hard constraint compliance reaches 88–100% under contracts.
  - num: Behavioral drift is bounded to D* < 0.27 across extended sessions.
  - num: Recovery success is 100% for frontier models and 17–100% across all models.
  - num: Runtime overhead is < 10ms per action.
  - Contract enforcement makes previously invisible violations measurable.
  - Hard constraints enforce safety-critical properties reliably.
  - Drift monitoring provides a leading indicator of emerging misalignment.
  - Recovery transforms exponential compliance decay into linear decay.
  - Contract components are non-redundant; removing recovery drops reliability index by ~0.20.
key_figures_tables:
  - Figure 1: Agent reliability index Θ across 7 models → Llama 3.3 70B highest (0.956), Mistral Large 3 lowest (0.908).
  - Figure 2: Drift trajectory over extended sessions → Contracted agents exhibit bounded drift consistent with OU mean-reversion.
  - Figure 3: OU model fit to drift trajectories → R2 = 0.49–0.75 confirms qualitative structure.
  - Figure 4: Ablation heatmap → Removing recovery or soft constraints degrades Θ by ~0.20.
  - Figure 5: Runtime overhead scaling → Linear in constraint count, <25ms for k=100.
  - Figure 6: Recovery mechanism impact → Degrades Θ by 0.199–0.215 when removed.
  - Figure 7: SPRT vs fixed-sample efficiency → SPRT requires 150–300 sessions vs 18,445 for Hoeffding.
key_equations:
  - equation: C = (P, I_hard ∪ I_soft, G_hard ∪ G_soft, R)
    explanation: Contract structure with hard/soft constraints and recovery.
  - equation: C_hard(t) = |{c ∈ I_hard ∪ G_hard : c(s_t, a_t) = true}| / |I_hard ∪ G_hard|
    explanation: Fraction of hard constraints satisfied at step t.
  - equation: C_soft(t) = |{c ∈ I_soft ∪ G_soft : c(s_t, a_t) = true}| / |I_soft ∪ G_soft|
    explanation: Fraction of soft constraints satisfied at step t.
  - equation: D(t) = w_c · D_compliance(t) + w_d · D_distributional(t)
    explanation: Behavioral drift score as weighted sum of compliance and distributional components.
  - equation: dD(t) = (α − γD(t))dt + σdW(t)
    explanation: Ornstein-Uhlenbeck drift dynamics for agent behavioral drift.
  - equation: E_π[D(t)] = α/γ
    explanation: Stationary mean drift under contract enforcement.
definitions:
  - term: ABC
    definition: Agent Behavioral Contracts, a formal framework for runtime enforcement of behavioral specifications in autonomous AI agents.
  - term: Design-by-Contract
    definition: Software engineering paradigm specifying preconditions, postconditions, and invariants for components.
  - term: (p,δ,k)-satisfaction
    definition: Probabilistic contract compliance where hard constraints hold with probability p, soft deviations within δ, recovery within k steps.
  - term: Behavioral Drift
    definition: Progressive divergence of agent behavior from intended specification over extended interactions.
  - term: OU Process
    definition: Ornstein-Uhlenbeck process, a stochastic differential equation with mean-reversion.
  - term: JSD
    definition: Jensen–Shannon divergence, a metric for measuring similarity between probability distributions.
  - term: SPRT
    definition: Sequential Probability Ratio Test, a sequential hypothesis test for minimal expected sample size.
critical_citations:
  - "[Meyer, 1992] — Introduced Design-by-Contract paradigm."
  - "[Benveniste et al., 2018] — Algebra for assume-guarantee contracts."
  - "[Alshiekh et al., 2018] — Shielding for safe RL."
  - "[Wang et al., 2026a] — Proved safety degradation absent external intervention."
  - "[Rath, 2026] — First systematic study of agent behavioral drift."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: Provides general framework for behavioral profiling via drift monitoring.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: Mention of cold-start baseline strategies in anomaly detection.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: General classification via contract compliance.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly addresses runtime anomaly detection via contract enforcement.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Proposes probabilistic anomaly detection with hard/soft constraints.
    - code: 8.C
      name: Cold‑Start Baseline Strategies for Anomaly Detection
      relevance: medium
      justification: Discusses reference distribution calibration for drift detection.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: contextual
      justification: General framework for engagement via compliance monitoring.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: contextual
      justification: Recovery mechanisms as retention enablers.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Introduces a comprehensive evaluation protocol with metrics like Θ, D(t), C(t).
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Evaluates algorithmic module (AgentAssert) across models and scenarios.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: contextual
      justification: General evaluation methodology for PFMS modules.
  contribution: "Provides a formal contract framework (ABC) for runtime enforcement in autonomous agents, directly applicable to anomaly detection and system evaluation modules in Odin. The (p,δ,k)-satisfaction definition offers a probabilistic compliance model usable for spending anomaly detection. The drift bounds theorem gives a theoretical basis for predicting and bounding behavioral drift in user financial profiles. The evaluation methodology with metrics like Θ and D(t) can be adopted for Odin's system evaluation framework."
  directly_justifies:
    - "Runtime contracts can detect 5.2–6.8 soft violations per session that are otherwise invisible."
    - "Hard constraint compliance reaches 88–100% with contract enforcement."
    - "Behavioral drift can be bounded to D* < 0.27 using contracts with recovery rate γ > α."
    - "Recovery mechanisms transform exponential compliance decay into linear decay."
    - "Contract components are non-redundant; each contributes meaningfully to reliability."
  limits:
    - "Evaluation primarily on financial advisory domain; broader validation across spending/forecasting is needed."
    - "State extraction from raw agent output is outside the framework's scope."
    - "Reference distribution for drift calibration requires dedicated setup."
    - "Compositionality relies on conditional independence assumptions that may not hold in shared-LLM pipelines."
  mapping_rationale: "A systematic scan across all 12 functional domains and their canonical topic codes was performed. The paper is fundamentally algorithmic, proposing and evaluating a runtime enforcement framework for AI agents. Domains flagged as relevant include: Anomaly Detection (8.A, 8.B) because the contract violation detection directly addresses anomaly detection; Behavioral Profiling (5.A, 5.B, 5.C) due to the drift monitoring and classification via compliance; System Evaluation (12.A, 12.B) because the paper introduces a comprehensive evaluation methodology. Domain 11 (Engagement/Retention) is contextual, as recovery mechanisms support engagement but are not the primary focus. Domains rejected include: Filipino Cultural Context (2.A–2.D), Expense Categorization (3.A–3.C), Existing Systems (4.A–4.B), Spending Forecasting (6.A–6.B), Budget Recommendation (7.A–7.D), Mobile-First Design (9.A–9.B), Data Privacy (10.A–10.B), and Savings/Debt Management (13.A–13.C) because the paper does not address these PFMS-specific concerns. Overall, the paper provides high relevance for runtime enforcement, anomaly detection, and system evaluation modules in Odin."
limitations:
  - "Requires structured state dictionary for constraint evaluation; feature extraction is out of scope. [unacknowledged]"
  - "Reference distribution for drift calibration must be established manually. [unacknowledged]"
  - "Default recovery is monitoring-only; domain-specific recovery logic must be implemented. [unacknowledged]"
  - "Stationarity assumptions in drift bounds may not hold for short sessions. [unacknowledged]"
  - "Compositionality bound becomes optimistic under correlated LLM failures. [acknowledged]"
remember_this:
  - "Contracts detect 5.2–6.8 soft violations per session invisible without monitoring."
  - "Hard constraints achieve 88–100% compliance with runtime enforcement."
  - "Behavioral drift is bounded to D* < 0.27 using contracts with recovery."
  - "Recovery transforms exponential compliance decay into linear decay."
  - "Each contract component is non-redundant; removing recovery drops reliability by 0.20."
```
---

## Paper 44: Askhiyah_summarized.md

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

## Paper 45: D. R. et al_summarized.md

**Source File:** `D. R. et al_summarized.md`

```yaml
paper_id: 10.51483/IJAIML.6.2s.2026.754-762
designation: international-algorithm-specific
title: Robust Learning Under Distribution Shifts for Non-Stationary Data Environments
authors: Rekha, D.; Vairavan, S.; MP, S.; Katariya, J. K.; Parikh, S. M.; Shanthi, T.; Shanthi, R.
year: 2026
venue: International Journal of Artificial Intelligence and Machine Learning
odin_topics:
  - 4.B
  - 6.B
  - 8.A
  - 8.B
  - 12.A
tldr: An adaptive learning framework combining AHO-InDNN and LDP-based optimization achieves robust fraud detection under sudden, gradual, and recurrent concept drift in financial transaction streams.
problem_and_motivation: Existing machine learning models assume stationary data distributions, but real-world financial transactions exhibit concept drift due to evolving fraud strategies and user behavior. This distribution shift degrades model performance and requires continuous adaptation without full retraining. Current approaches lack integrated drift detection, online learning, and uncertainty-aware optimization.
approach:
  - Used PaySim artificial mobile money transaction data with 30 days of sequential records and 743 time steps.
  - Implemented a drift detection module using statistical divergence and mean shift to identify sudden, gradual, and recurrent concept drift.
  - Designed an Incremental Deep Neural Network (InDNN) with dynamic hidden layers and ReLU activation for online learning.
  - Applied Archerfish Hunting Optimization (AHO) for parameter tuning, balancing exploration and exploitation via shooting and jumping behaviors.
  - Introduced Large Deviations Principle (LDP) based optimization to enhance stability and robustness under distribution shifts.
  - Compared against KNN, SMOTEBoost with cost-sensitive learning, and MH-DRNN using accuracy, precision, recall, and F1-score.
findings:
  - num: 98.74% accuracy, 98.42% precision, 98.52% recall, and 98.37% F1-score on the PaySim dataset.
  - AHO-InDNN outperformed KNN, SMOTEBoost, and MH-DRNN across all metrics.
  - The model effectively adapts to sudden, gradual, and recurrent concept drift without full retraining.
  - LDP-based optimization reduces false positives and improves generalization in non-stationary environments.
key_figures_tables:
  - Figure 1: Architecture of the proposed robust adaptive learning framework → Shows four modules: data input, drift detection, adaptive learning, output prediction.
  - Figure 2: Fraud rate changes under three drift types (sudden, gradual, recurrent) → Illustrates the need for adaptive learning under dynamic fraud patterns.
  - Table 1: Types of concept drift and examples → Defines sudden, gradual, and recurrent drift with real-world fraud examples.
  - Table 2: Performance comparison of models → Proposed model achieves highest accuracy, precision, recall, and F1.
key_equations:
  - equation: y' = (y - y_min) / (y_max - y_min)
    explanation: Scales features to [0,1] for stable learning.
  - equation: F(θ) = -1/M ∑_m ∑_p s_mp log x_mp
    explanation: Cross-entropy loss with robustness regularization.
  - equation: θ_s = θ_{s-1} - α * (β1 m_{s-1} + (1-β1)∇θ F(θ_{s-1})) / (sqrt(β2 v_{s-1} + (1-β2)(∇θ F(θ_{s-1}))^2 + ε))
    explanation: Adam-like update for dynamic parameter adaptation.
  - equation: lim_{s→∞} 1/s log P(X_s ∈ A) = - inf_{x∈A} I(x)
    explanation: Measures exponential decay rate of rare fraud events.
definitions:
  - term: AHO
    definition: Archerfish Hunting Optimization, a metaheuristic for parameter tuning balancing exploration and exploitation.
  - term: InDNN
    definition: Incremental Deep Neural Network with dynamic depth and neuron structure for non-stationary data.
  - term: LDP
    definition: Large Deviations Principle, a probabilistic method for measuring rare event probabilities in streaming data.
  - term: Concept drift
    definition: Change in the conditional distribution between input and output over time.
  - term: Distribution shift
    definition: Change in data distribution between training and testing phases.
critical_citations:
  - "[Liu et al., 2024] — Deep reinforcement learning in nonstationary environments."
  - "[Halstead et al., 2022] — Analyzing concept drift adaptation."
  - "[Cano and Krawczyk, 2022] — Online self-adjusting ensemble for drifting data."
relevance:
  topics:
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies research gap in integrated drift detection and adaptive learning.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: Uses sequential transaction data but focuses on fraud detection, not spending forecasting.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly addresses fraud detection as anomaly detection in financial transactions.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Proposes AHO-InDNN algorithm specifically for detecting fraud under concept drift.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: low
      justification: Uses standard classification metrics but not tailored to PFMS evaluation.
  contribution: The paper's drift-aware learning framework directly justifies Odin's anomaly detection module by demonstrating how adaptive algorithms can maintain accuracy under shifting spending patterns. The AHO-InDNN approach offers a pathway for Odin's anomaly detection algorithms (8.B) to handle real-world concept drift without full retraining. The LDP-based robustness evaluation informs Odin's system evaluation (12.A) by providing metrics for stability under distribution shifts. The identified gaps in existing systems (4.B) highlight the need for Odin's integrated adaptive learning capabilities.
  directly_justifies:
    - Adaptive learning frameworks can maintain fraud detection accuracy above 98% under concept drift.
    - Integrated drift detection and online learning outperform static models in non-stationary financial data.
    - LDP-based optimization reduces false positives and improves generalization in dynamic environments.
  limits:
    - None identified.
  mapping_rationale: Systematic scan across all 12 functional domains flagged only Anomaly Detection and related topics as relevant. The paper directly supports 8.A and 8.B with high relevance due to its fraud detection focus under concept drift. Topic 4.B received medium relevance because the paper explicitly discusses gaps in existing drift detection methods, but it does not survey PFMS specifically. Topic 6.B was considered low because while the data is sequential, the task is fraud classification rather than spending forecasting. Topic 12.A was considered low because evaluation metrics are standard and not PFMS-specific. Domains such as Filipino Cultural Context, Expense Categorization, Budget Recommendation, and Mobile-First Design were rejected as the paper contains no content on these topics. Overall, the paper is highly relevant to Odin's anomaly detection and adaptive learning components but has limited applicability elsewhere.
limitations:
  - Tested only on simulated PaySim data; real-world validation is needed. [unacknowledged]
  - Computational overhead of AHO may hinder real-time deployment. [unacknowledged]
  - Generalizability to other financial datasets beyond mobile money transfers is untested. [unacknowledged]
remember_this:
  - AHO-InDNN achieves 98.74% accuracy in fraud detection under concept drift.
  - Integrated drift detection and online learning enable adaptation without full retraining.
  - LDP-based optimization improves stability and reduces false alarms in dynamic data.
  - The framework handles sudden, gradual, and recurrent distribution shifts effectively.
```
---

## Paper 46: Lou et al_summarized.md

**Source File:** `Lou et al_summarized.md`

```yaml
paper_id: 10.1186/s40537-026-01464-y
designation: international-algorithm-specific
title: Predicting customer buying habits using convolutional neural network
authors: Lou, Z.; Wang, S.; Yu, X.; Song, W.
year: 2026
venue: Journal of Big Data
odin_topics:
  - 6.A
  - 6.B
  - 5.A
  - 5.C
  - 7.B
  - 3.A
tldr: A CNN with hybrid pooling predicts income tiers from demographic and behavioral data, then uses a probability matrix to recommend products, achieving 93.06% income prediction accuracy.
problem_and_motivation: Traditional models struggle with high-dimensional demographic data and non-linear relationships between demographics and behavior. This gap limits the accuracy of personalized retail and product recommendations. There is a need for a more effective method to capture latent spatial patterns in customer data.
approach:
  - Data was collected via a questionnaire from 980 participants covering demographics, shopping habits, and income.
  - Nominal features were converted to numerical values, missing values were imputed, and features were normalized to [0,1].
  - Normalized features were mapped to 20x10 grayscale images to enable CNN processing of spatial patterns.
  - A CNN with hybrid pooling layers (switching between max and average pooling during training) was used for income classification.
  - A purchase probability matrix was constructed from training data to model the likelihood of product category purchases per income tier.
findings:
  - num: The proposed CNN achieved 93.06% accuracy in predicting income levels.
  - num: The model attained precision of 92.95% and recall of 93.21% for income classification.
  - num: The method achieved a mean accuracy of 95% in product recommendation across six categories.
  - Hybrid pooling outperformed max and average pooling variants, improving accuracy by at least 1.5%.
  - The CNN with hybrid pooling demonstrated superior ROC curves compared to benchmark methods.
  - Statistical significance tests (p < 0.05) confirmed the superiority of the proposed model over baselines.
  - Job category, education level, and age were identified as the most important features for income prediction.
key_figures_tables:
  - Figure 1: Flowchart of the proposed three-step methodology → visualizes the data preprocessing, classification, and recommendation pipeline.
  - Figure 2: Architecture of the proposed CNN model with hybrid pooling → shows the two convolutional layers and hybrid pooling structure.
  - Table 5: Performance comparison of income prediction methods → demonstrates the proposed method's superior metrics across all categories.
  - Figure 5: Confusion matrices for income classification → highlights fewer misclassifications in the proposed model.
key_equations:
  - equation: S = {S_avg with probability p, S_max with probability 1-p}
    explanation: Defines the stochastic switching between average and max pooling.
  - equation: S_hybrid = p * S_avg + (1-p) * S_max
    explanation: Computes the final pooling output as a weighted combination.
  - equation: Loss = -Σ(w_i * y_i * log(p_i) + (1-y_i) * log(1-p_i))
    explanation: Weighted cross-entropy loss used to address class imbalance.
definitions:
  - term: CNN
    definition: Convolutional Neural Network, a deep learning model for processing grid-like data.
  - term: Hybrid Pooling
    definition: A pooling strategy that randomly selects between max and average pooling during training.
  - term: WCE
    definition: Weighted Cross-Entropy, a loss function that assigns penalties inversely proportional to class frequency.
  - term: RFM
    definition: Recency, Frequency, Monetary model for customer segmentation.
critical_citations:
  - "[Tong & Tanaka, 2019] — Introduces the hybrid pooling method used in this paper."
  - "[Chen et al., 2022] — A recent benchmark for salary prediction using Random Forest."
  - "[Vemulapati et al., 2023] — A benchmark using LSTM and BiLSTM for income prediction."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Core contribution is predicting income as a proxy for financial capacity.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: Uses behavioral features for prediction; could be adapted for sequential spending.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Classifies individuals by income, a key behavioral grouping.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Proposes a novel CNN-based classification approach for income-based profiles.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: contextual
      justification: Provides a framework for product recommendation, similar to budget allocation.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: low
      justification: Uses product categories, which could map to expense categories.
  contribution: "The paper introduces a CNN-based income classification model, which could inform Odin's expense forecasting module. The hybrid pooling strategy addresses class imbalance, relevant to Odin's diverse user base. The product recommendation matrix offers a framework for budget allocation or expense prediction. The feature importance analysis identifies demographic indicators that could enhance Odin's behavioral profiling."
  directly_justifies:
    - "A CNN with hybrid pooling can effectively classify financial behavior profiles from demographic data."
    - "Converting tabular user data to grayscale images enables spatial feature extraction for behavioral analysis."
    - "Weighted cross-entropy loss improves classification accuracy on imbalanced income data."
    - "The purchase probability matrix can model category-specific spending likelihood."
  limits:
    - "The dataset (N=980) is relatively small for deep learning, potentially limiting generalizability."
    - "The study was conducted on a regional population, which may not reflect Filipino spending patterns."
    - "The model does not incorporate sequential spending data, limiting its use for forecasting."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant primarily to the 'Spending Forecasting' domain due to its focus on predicting income and, by extension, purchasing habits. This maps directly to topics 6.A and 6.B. The classification methodology is also highly relevant to 'Behavioral Profiling & Classification' (topics 5.A and 5.C), as it proposes a new approach for categorizing users by income. The product recommendation component is contextually relevant to 'Budget Recommendation' (topic 7.B) and the product categorization is tangentially related to 'Expense Categorization' (topic 3.A). The 'Existing Systems & Gaps' domain was considered but rejected as the paper's primary contribution is a novel method rather than a survey. Similarly, 'Filipino Cultural Context' was rejected as the data is not Filipino-specific. Overall, the paper is highly relevant to Odin's algorithmic design for forecasting and classification modules."
limitations:
  - "The sample size of 980 is relatively small for deep learning models, which may affect generalizability."
  - "The dataset is geographically and culturally specific, potentially limiting applicability to other regions like the Philippines."
  - "The study does not test the model on external, independent datasets, limiting external validation. [unacknowledged]"
  - "The feature set may lack granular cultural or micro-economic indicators that could influence buying choices. [unacknowledged]"
remember_this:
  - "A CNN with hybrid pooling achieved 93.06% accuracy in income prediction."
  - "Product recommendations had a mean accuracy of 95% across six categories."
  - "Job category, education, and age are the most important income predictors."
  - "Hybrid pooling improves generalization and reduces overfitting in CNNs."
  - "The model provides a scalable pipeline for real-time retail personalization."
```
---

## Paper 47: Abila & Ulibas_summarized.md

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

## Paper 48: Jandoc et al_summarized.md

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

## Paper 49: Phuong et al_summarized.md

**Source File:** `Phuong et al_summarized.md`

```yaml
paper_id: 1c7b4f3e-2a8d-4c9f-b6e1-3d7a5f9c2e8b
designation: international
title: Post-Pandemic Labor Market Transformation: The Rise of the Gig Economy and Youth Employment in Southeast Asia
authors: Nguyen Thi Minh Phuong, Carlos Antonio Cruz, Rini Andriani Pratiwi
year: 2026
venue: International Journal of Economic Research and Exact Sciences
odin_topics:
  - 1.A
  - 1.B
  - 2.A
  - 2.C
  - 5.A
  - 6.A
  - 10.B
tldr: Platform-mediated gig work among urban youth in four Southeast Asian countries is shaped by education, income, and urban location, with earnings lower and more volatile than comparable formal employment.
problem_and_motivation: Policymakers in Southeast Asia lack comparative evidence on gig economy participation patterns and their welfare implications for young workers. Existing studies are largely single-country case studies, limiting the ability to design regionally informed policy responses. Cross-country evidence on determinants, earnings differentials, and lived experiences is needed.
approach:
  - Conducted a survey of 1,200 young workers aged 18-29 across Vietnam, Philippines, Indonesia, and Thailand from January to October 2023.
  - Performed 40 semi-structured interviews with platform workers across the four countries to capture lived experiences.
  - Applied logistic and ordinary least squares regression to identify determinants of gig participation and earnings differentials.
  - Used reflexive thematic analysis on interview transcripts to derive qualitative themes.
  - Integrated quantitative and qualitative findings using a meta-inference approach to contextualize statistical patterns.
findings:
  - num: 38% of urban youth in the sample engaged in platform-mediated gig work in the past 12 months.
  - num: Secondary school completion lowers gig participation probability by 6.8 percentage points.
  - num: Median full-time gig earnings range from USD 247 in Vietnam to USD 358 in Thailand.
  - num: Full-time platform earnings are 4.7% lower than comparable non-platform work in the same country.
  - num: Earnings volatility is 1.6 times higher in platform work than in comparable non-platform jobs.
  - Education is negatively associated with full-time gig participation, with a larger effect size than for any participation.
  - Male respondents are more likely to engage in full-time gig work, especially in ride-hailing and delivery.
  - Qualitative analysis identified four themes: autonomy paradox, social protection gap, skills development opportunities, and intergenerational tensions.
key_figures_tables:
  - "Table 1: Sample characteristics by country and platform engagement → Provides demographic context."
  - "Table 2: Logistic regression for gig participation → Identifies key determinants: education, income, urban location."
  - "Table 3: OLS earnings regressions → Shows platform earnings are lower and more volatile."
key_equations:
  - equation: "log(earnings) = β_0 + β_1*platform + β_2*education + β_3*income + β_4*country + ε"
    explanation: "OLS model for log monthly earnings differentials."
definitions:
  - term: "Gig economy"
    definition: "Labor market characterized by short-term contracts or freelance work, mediated by digital platforms."
  - term: "Platform work"
    definition: "Income-generating activity mediated by digital platforms that connect workers with clients."
  - term: "Autonomy paradox"
    definition: "Tension between perceived flexibility and algorithmic constraints on platform workers."
critical_citations:
  - "[Berg et al., 2018] — Found heterogeneity in platform worker experiences."
  - "[Wood et al., 2019] — Examined autonomy-control paradox in algorithmic management."
  - "[De Stefano, 2016] — Analyzed legal status of platform workers."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: "The paper's Philippine sub-sample provides data on Filipino youth labor market engagement."
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: "Reports earnings and income volatility for Filipino platform workers, relevant to financial structure."
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: low
      justification: "Discusses intergenerational tensions and family expectations influencing work choices."
    - code: 2.C
      name: User-Declared Financial Preferences
      relevance: low
      justification: "Qualitative themes include worker preferences for flexibility over formal employment."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: "Describes participation patterns but not personal finance behavioral profiles."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: contextual
      justification: "Provides earnings data but not predictive models."
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: "The social protection gap relates to trust in platforms and government."
  contribution: "The paper provides cross-country evidence on the gig economy that can inform the contextual understanding of Filipino young professionals' income streams and employment patterns. It underscores the importance of earnings volatility and social protection gaps, which are relevant to designing budget recommendation and anomaly detection modules that account for irregular income. The findings on education as a determinant of gig participation can help Odin tailor its user onboarding and categorization features to different user segments."
  directly_justifies:
    - "Young urban Filipino workers have a 39% participation rate in platform-mediated gig work, indicating significant income irregularity."
    - "Full-time platform earnings in the Philippines are 4.7% lower than comparable non-platform work, highlighting the need for conservative budget forecasts."
    - "Earnings volatility in platform work is 1.6 times higher, justifying robust anomaly detection for variable income patterns."
  limits:
    - "The survey sample is urban, limiting generalizability to rural Filipino populations."
    - "Self-reported earnings may contain measurement error for irregular platform income."
    - "Cross-sectional design prevents causal inference on long-term consequences of platform engagement."
    - "The study does not specifically address personal finance management systems or user financial behavior in detail."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant for domains related to Filipino Cultural Context (2.A, 2.C) due to its discussion of intergenerational tensions and worker preferences, and for Behavioral Profiling (5.A) and Predictive Modeling (6.A) due to its quantitative analysis of participation and earnings patterns. Low relevance was assigned to topics like 2.A and 2.C because the paper's focus is on employment, not culturally specific financial practices per se. Domains such as Expense Categorization (3), Budget Recommendation (7), Anomaly Detection (8), Mobile Design (9), Evaluation (12), Savings (13), and Engagement (11) were rejected due to no direct coverage. The paper is considered contextually relevant, providing background on the financial reality of Filipino young professionals rather than direct insights for Odin's algorithmic modules."
limitations:
  - "Urban sample limits generalizability to rural areas where platform dynamics differ."
  - "Cross-sectional design constrains causal inference about long-term consequences."
  - "Self-reported earnings are subject to measurement error. [unacknowledged]"
  - "The qualitative sample captures perspectives at a particular moment in time. [unacknowledged]"
  - "Does not include validated mental health measures, despite qualitative findings on stress. [unacknowledged]"
remember_this:
  - "38% of urban youth in the sample engaged in gig work."
  - "Earnings volatility is 1.6 times higher in platform work."
  - "Secondary education reduces gig participation probability by 6.8 percentage points."
  - "Full-time platform earnings are 4.7% lower than non-platform work."
  - "Filipino platform workers operate in a remittance-supported household context."
```
---

## Paper 50: Scrivano A.-2025b_summarized.md

**Source File:** `Scrivano A.-2025b_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international
title: Fraud Detection Pipeline Using Machine Learning: Methods, Applications, and Future Directions
authors: Scrivano, A.
year: 2026
venue: Unknown
odin_topics:
  - 8.A
  - 8.B
  - 5.A
  - 6.A
  - 12.A
tldr: A comprehensive review of machine learning methods for fraud detection, covering supervised, unsupervised, and hybrid approaches across multiple sectors.
problem_and_motivation: The increasing sophistication of fraud schemes in digital economies has rendered traditional rule-based and manual audit systems inadequate. There is a pressing need for adaptive, scalable, and automated solutions that can effectively counter evolving fraudulent activities.
approach:
  - This review synthesizes current state-of-the-art approaches in fraud detection pipeline architectures employing machine learning techniques.
  - Key methodologies including supervised learning (logistic regression, decision trees, random forests, gradient boosting), unsupervised learning (clustering, PCA), and hybrid methods are discussed in detail.
  - Real-world applications of these ML solutions are explored across finance, healthcare, and e-commerce sectors.
  - The paper also provides a forward-looking analysis of emerging trends like deep learning, ensemble methods, and real-time detection.
findings:
  - num: Neural networks achieved the highest AUC-ROC of 0.95 and recall of 0.85 in empirical evaluation.
  - num: Random forests demonstrated strong precision at 0.90, beneficial for minimizing false positives.
  - num: Logistic regression served as a reliable baseline with AUC-ROC of 0.88 and recall of 0.78.
  - Supervised learning excels when labeled historical data is available, while unsupervised methods are advantageous in limited-label scenarios.
  - Hybrid frameworks that combine unsupervised flagging with supervised verification effectively address data imbalance issues.
  - Ensemble methods and deep learning architectures like CNNs and RNNs show exceptional proficiency in capturing complex fraud patterns.
  - Continuous learning and adaptive frameworks are crucial for maintaining model effectiveness against emerging fraud tactics.
key_figures_tables:
  - "Table 1: Performance Metrics of Fraud Detection Algorithms → Neural networks excel in recall and AUC-ROC; random forests lead in precision."
  - "Figure 1: ROC Curves of Fraud Detection Algorithms → Neural network maintains the highest AUC-ROC score of 0.95."
  - "Figure 2: Precision-Recall Curves for Fraud Detection Algorithms → Neural networks achieve high precision and recall across thresholds, random forests show a sharper decline."
  - "Figure 3: Illustrative overview of a modern fraud detection pipeline → Pipeline includes preprocessing, EDA, feature engineering, modeling, and evaluation stages."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "ML"
    definition: "Machine Learning"
  - term: "PCA"
    definition: "Principal Component Analysis"
  - term: "CNN"
    definition: "Convolutional Neural Network"
  - term: "RNN"
    definition: "Recurrent Neural Network"
  - term: "AUC-ROC"
    definition: "Area Under the Receiver Operating Characteristic Curve"
  - term: "XAI"
    definition: "Explainable Artificial Intelligence"
  - term: "SMOTE"
    definition: "Synthetic Minority Over-sampling Technique"
critical_citations:
  - "[Nguyen et al., 2020] — Overview of generic fraud detection algorithms."
  - "[Chen & Guestrin, 2016] — Scalable tree boosting system for fraud detection."
  - "[Friedman, 2001] — Gradient boosting machine methodology."
  - "[Bhattacharyya et al., 2011] — Comparative study on data mining for credit card fraud."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: "Comprehensive review of anomaly detection techniques (supervised, unsupervised, hybrid) directly applicable to Odin's anomaly detection module."
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: "Discusses specific algorithms like clustering, isolation forests, neural networks, and ensemble methods for detecting fraudulent (anomalous) transactions."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: "Emphasizes the importance of understanding user behavior patterns (transaction velocity, merchant variance) to detect deviations, which is foundational for building behavioral profiles."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: "The review covers predictive modeling (supervised learning) for classifying transactions, which informs Odin's predictive capabilities for spending behavior."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: "Provides a detailed discussion on evaluation metrics (precision, recall, F1, AUC-ROC, precision-recall curves) and techniques (cross-validation) relevant for assessing Odin's algorithmic modules."
  contribution: "This paper provides a foundational review of anomaly detection methods, directly informing Odin's approach to identifying unusual spending patterns. The discussion on behavioral profiling supports Odin's user modeling module by highlighting key features and metrics. Its comprehensive evaluation framework offers a blueprint for assessing the performance of Odin's predictive and detection algorithms. The emphasis on continuous learning and adaptation guides Odin's design for maintaining model relevance over time."
  directly_justifies:
    - "Machine learning algorithms such as random forests and neural networks are effective for detecting anomalies in transaction data."
    - "Unsupervised learning methods like clustering are advantageous for anomaly detection when labeled data is limited."
    - "Hybrid approaches combining unsupervised flagging with supervised verification address data imbalance issues."
    - "Evaluation metrics like precision, recall, and AUC-ROC are essential for assessing fraud detection model performance."
  limits:
    - "The paper is a general review and does not provide specific implementation details for a personal finance management system like Odin."
    - "Some advanced techniques like deep learning require significant computational resources, which may be a constraint for Odin's mobile-first design."
  mapping_rationale: "A systematic scan of all 12 functional domains and associated topic codes was performed. The paper's focus on machine learning for anomaly detection directly aligns with domain 'Anomaly Detection', leading to high relevance for topics 8.A and 8.B. The behavioral aspects of the paper, such as analyzing transaction patterns and user behavior deviations, provide medium relevance to 'Behavioral Profiling & Classification' (5.A). The paper's extensive coverage of predictive modeling techniques (supervised learning) informs the 'Spending Forecasting' domain (6.A). The thorough discussion on evaluation metrics and techniques offers medium relevance to 'System Evaluation' (12.A). Domains like 'Filipino Cultural Context', 'Expense Categorization', 'Budget Recommendation', 'Mobile-First Design', 'Data Privacy', 'User Retention', and 'Savings & Debt Management' were considered and rejected as the paper does not provide specific, citable claims relevant to these areas for Odin. The paper is highly relevant for establishing technical foundations for Odin's anomaly detection and forecasting modules."
limitations:
  - "The paper's evaluation of algorithms is based on a general financial transaction dataset, not specifically on Filipino young professional spending data. [unacknowledged]"
  - "The practicality of deploying deep learning models in a mobile-first application with resource constraints is not addressed. [unacknowledged]"
  - "The paper focuses on fraud detection, which is a specific type of anomaly, and may not fully cover the broader spectrum of spending anomalies (e.g., overspending)."
remember_this:
  - "Neural networks achieved superior recall and AUC-ROC in detecting fraudulent transactions."
  - "Random forests provide a strong balance between performance, interpretability, and real-time applicability."
  - "Continuous learning and adaptive frameworks are essential for model effectiveness against evolving tactics."
  - "Data imbalance in fraud datasets necessitates specialized techniques like oversampling and cost-sensitive learning."
  - "Feature engineering of behavioral metrics is crucial for enhancing predictive power in detection models."
```
---


---

## Agent Instruction

If the agent reading this document believes further context about a paper is needed, it may request the original converted markdown file (with the '_marked' suffix) from the user for the relevant paper(s).
