# Compiled Research Summaries

**Total Papers:** 50

**Note:** Included papers positions 51 to 100, Sorted by year.

---

## Paper 1: Goncu et al_summarized.md

**Source File:** `Goncu et al_summarized.md`

```yaml
paper_id: 10.1016/j.bir.2026.100800
designation: international-algorithm-specific
title: Machine learning for risk profiling: An analysis of pension fund participants
authors: Göncü, A.; Kuzubaş, T.U.; Saltoğlu, B.
year: 2026
venue: Borsa Istanbul Review
odin_topics:
  - 5.A
  - 5.C
  - 6.A
  - 12.A
  - 12.B
  - 2.C
tldr: Boosting methods modestly improve risk profiling over regulatory benchmarks by identifying a concise set of four predictors, though overall explanatory power remains low.
problem_and_motivation: Existing risk questionnaires have limited predictive power and create operational friction for pension providers. Accurate risk assessment is critical for aligning investor preferences with portfolio choices, yet current tools often fail to predict actual behavior. The lack of systematic comparison of machine learning methods against regulatory benchmarks in emerging markets leaves room for improvement.
approach:
  - Analyzed 81,563 participants from a Turkish pension fund with portfolio risk as dependent variable.
  - Applied recursive feature elimination (RFE) across eight models to select the most predictive variables.
  - Compared ordinary least squares, ridge, Lasso, CART, random forest, and three boosting algorithms.
  - Used 20‑fold cross‑validation with grid search for hyperparameter tuning.
  - Included age‑squared to capture the nonlinear age‑risk relationship.
findings:
  - "num: LightGBM achieved R² of 0.167 vs. the regulatory benchmark of 0.131, a 27% relative increase."
  - "num: Four variables (self‑reported risk, lottery choice, age, and age‑squared) capture most of the predictive power."
  - Age exhibits an inverted‑U relationship with portfolio risk, peaking in middle age.
  - Boosting methods show less performance variability across cross‑validation folds than the benchmark.
  - The performance using just four variables is comparable to using the full questionnaire.
key_figures_tables:
  - "Figure 1: Age vs. average portfolio risk → Inverted‑U relationship with peak at 35–44 age group."
  - "Figure 2: R² distribution across folds for all features → Boosting methods have higher mean and lower variance."
  - "Figure 3: R² distribution for selected features → Simplified model still outperforms regulatory benchmark."
key_equations:
  - equation: "\\sigma = \\sqrt{52 \\times \\frac{1}{T-1} \\sum_{t=1}^{T} (r_{f,t} - \\bar{r})^2}"
    explanation: "Annualized weekly return volatility used as portfolio risk measure."
definitions:
  - term: RFE
    definition: "Recursive feature elimination, an iterative feature selection method."
  - term: CMB
    definition: "Capital Markets Board of Türkiye, the regulatory body that mandates risk questionnaires."
  - term: OLS
    definition: "Ordinary least squares, a linear regression method."
  - term: Lasso
    definition: "Least absolute shrinkage and selection operator, a linear model with L1 regularization."
  - term: CART
    definition: "Classification and regression tree, a decision‑tree algorithm."
  - term: GBoost
    definition: "Gradient boosting, an ensemble method that builds models sequentially."
  - term: XGBoost
    definition: "Extreme gradient boosting, a scalable boosting implementation."
  - term: LightGBM
    definition: "Light gradient boosting machine, a fast boosting framework."
critical_citations:
  - "[Dohmen et al., 2011] — Established low R² for risk preference prediction."
  - "[Beauchamp et al., 2017] — Similar modest explanatory power in risk preference studies."
  - "[Kuzubaş & Saltoğlu, 2024] — Factor analysis of the same pension context."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: "Directly models risk tolerance as a behavioral profile using portfolio choices."
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: "Compares multiple ML algorithms for profiling risk behavior."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: "Applies predictive models to forecast revealed risk from questionnaire responses."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: "Uses cross‑validation and multiple performance metrics to evaluate models."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: "Provides systematic comparison of algorithmic performance (boosting vs. linear models)."
    - code: 2.C
      name: User-Declared Financial Preferences
      relevance: contextual
      justification: "Uses self‑reported risk attitudes as predictors, but does not address preference elicitation for PFMS."
  contribution: "This paper's feature selection method can inform Odin's behavioral profiling module by identifying the most predictive user attributes for financial risk. Its comparison of ML models provides a benchmark for evaluating Odin's predictive algorithms, particularly for forecasting spending or risk. The finding that a small set of variables suffices supports efficient user onboarding in Odin's mobile‑first design, reducing friction. The study's cross‑validation framework offers a template for Odin's system evaluation, ensuring robust performance assessment. However, the modest explained variance reminds that risk‑taking is inherently difficult to predict, guiding realistic expectations for Odin's models."
  directly_justifies:
    - "Boosting methods can improve predictive accuracy for financial risk profiling."
    - "A four‑variable model can match the predictive power of a full questionnaire."
    - "Age has a nonlinear relationship with risk‑taking behavior."
    - "Self‑reported risk attitude is the single most important predictor."
    - "Simplified assessments can reduce operational friction without substantial loss of accuracy."
  limits:
    - "The study uses cross‑sectional data, limiting insights on temporal dynamics."
    - "Modest R² indicates that risk‑taking is not well explained by standard demographic and survey variables."
    - "Generalizability to other cultural contexts (e.g., the Philippines) is untested."
    - "No consideration of cold‑start scenarios or initial user onboarding [unacknowledged]."
    - "Does not address data privacy or user trust concerns [unacknowledged]."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant for Behavioral Profiling & Classification (5.A, 5.C) because it directly models and classifies risk tolerance using ML. It also touches on Predictive Modeling (6.A) as it forecasts portfolio risk, and on Evaluation Frameworks (12.A, 12.B) due to its extensive cross‑validation and model comparisons. User‑Declared Preferences (2.C) was considered but assigned contextual because the survey responses are used as predictors rather than as a design consideration for PFMS. Domains related to Expense Categorization (3.A–3.C), Budgeting (7.A–7.D), Anomaly Detection (8.A–8.C), Mobile‑First Design (9.A–9.B), Data Privacy (10.A–10.B), Engagement (11.A–11.B), and Savings/Debt (13.A–13.C) were rejected because the paper does not address these areas. Overall, the paper provides moderate direct justification for Odin's behavioral profiling and evaluation components, but its findings are primarily methodological and not specific to PFMS or Filipino context."
limitations:
  - "Cross‑sectional analysis prevents studying changes in risk preferences over time."
  - "The dependent variable (portfolio risk) may be influenced by advisor recommendations or defaults, not solely individual preferences."
  - "Overall explanatory power is modest (R² 0.13–0.17), indicating unobserved factors dominate."
  - "Findings may not generalize to other cultural or regulatory environments."
  - "No exploration of cold‑start or initial user profiling [unacknowledged]."
  - "Lacks discussion of interpretability trade‑offs for regulatory compliance [unacknowledged]."
remember_this:
  - "Boosting improves R² from 0.131 to 0.167, a 27% relative gain."
  - "Four predictors (risk attitude, lottery choice, age, age²) capture most power."
  - "Age‑risk relationship is inverted‑U, peaking in middle age."
  - "Simplified questionnaires can maintain accuracy and reduce operational friction."
  - "Overall predictive power remains low, highlighting inherent difficulty in risk prediction."
```
---

## Paper 2: Bustamante & Ubilla_summarized.md

**Source File:** `Bustamante & Ubilla_summarized.md`

```yaml
paper_id: 10.1108/JEFAS-10-2025-0378
designation: international
title: Retail investor behavior and social media signals: exploring attention dynamics
authors: Bustamante, D.; Ubilla, A.
year: 2026
venue: Journal of Economics, Finance and Administrative Science
odin_topics:
  - 1.C
  - 2.D
  - 4.B
  - 5.A
  - 5.C
  - 10.B
  - 11.A
  - 12.A
tldr: Social media influencer attention increases stock investment propensity, but digital financial literacy's moderating role varies significantly across countries.
problem_and_motivation: The influence of social media recommendations on retail investor behavior is underexplored, particularly regarding how digital financial literacy (DFL) moderates this relationship across diverse national contexts. Existing studies often rely on single-country samples or aggregated data, limiting generalizability and understanding of underlying mechanisms.
approach:
  - Analyzed microdata from the OECD/INFE 2023 Adult Financial Literacy Survey covering Brazil, Finland, Philippines, and Saudi Arabia.
  - Employed logistic regression with country fixed effects to model stock investment as a function of investor attention and DFL.
  - Constructed a DFL index using principal component analysis across three dimensions: digital financial behavior, knowledge, and attitude.
  - Addressed endogeneity using instrumental variable (two-stage residual inclusion) and propensity score matching techniques.
  - Examined interaction effects between attention and DFL to test for moderation across countries.
findings:
  - num: Investor attention increases the probability of stock investment by 12.2% in the pooled sample, remaining robust across countries.
  - num: Digital financial literacy (DFL) raises stock investment probability by 5.8% in the pooled sample, driven primarily by digital financial knowledge.
  - The moderating effect of DFL on the attention-investment relationship is heterogeneous: negative in the Philippines, positive in Saudi Arabia, and insignificant in Brazil and Finland.
  - Endogeneity corrections confirm the positive effect of social media attention on investment decisions remains significant.
  - Socioeconomic factors like gender, education, employment, and income consistently predict stock market participation.
key_figures_tables:
  - "Table 1: Descriptive statistics showing 21.4% stock investment and 17.7% investor attention rates → Baseline participation and attention levels are adequate for analysis."
  - "Table 2: Marginal effects from logistic regressions show attention increases investment by 12-28% across models → Attention is a robust predictor of stock investment."
  - "Table 3: Interaction effects reveal DFL moderates attention differently by country → The buffering role of DFL is not universal."
  - "Table 5: Two-stage residual inclusion results confirm attention remains significant after endogeneity correction → Main findings are robust to reverse causality concerns."
  - "Table 6: Propensity score matching shows a 10% ATT for attention on investment → Selection bias does not explain the attention effect."
key_equations:
  - equation: "Pr(SI_i = 1 | X) = Λ(β_0 + β_1·Atten_i + β_2·DFL_i + Σβ_k·Controls_ki + ΣCountry_h)"
    explanation: "Logistic model for stock investment probability as function of attention, DFL, and controls."
definitions:
  - term: "SI"
    definition: "Stock investment, a binary variable indicating direct ownership of stocks."
  - term: "Atten"
    definition: "Investor attention, coded 1 if decisions were influenced by social media or unknown individuals."
  - term: "DFL"
    definition: "Digital financial literacy, a PCA-based index of digital financial behavior, knowledge, and attitude."
  - term: "DFK"
    definition: "Digital financial knowledge, based on correct responses to questions on digital finance and regulation."
  - term: "2SRI"
    definition: "Two-stage residual inclusion, a control function method for endogeneity in nonlinear models."
critical_citations:
  - "[Barber and Odean, 2008] — Attention theory for investor behavior."
  - "[Hirshleifer and Teoh, 2003] — Limited attention and information processing."
  - "[OECD, 2023] — Source of DFL definition and survey data."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: "Provides behavioral evidence on investment decisions influenced by social media, relevant to Filipino sample."
    - code: 2.D
      name: Filipino Spending Cycles and 'Occasions'
      relevance: contextual
      justification: "Includes Philippines in cross-country analysis, offering context for financial behavior but not specific spending cycles."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: low
      justification: "Highlights gaps in understanding DFL's moderating role, which is relevant for system design but not directly evaluating existing PFMS."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: "Directly examines how attention and DFL shape investment behavior, contributing to behavioral profiling."
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: "Uses logistic regression to classify investment behavior based on attention and DFL, informing classification approaches."
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: "Discusses trust implications of social media influence and DFL, tangentially related to user trust in systems."
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: contextual
      justification: "Addresses attention as a driver of engagement, providing background but not direct design insights."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: low
      justification: "Uses econometric evaluation methods that could inform system evaluation frameworks."
  contribution: "This paper validates that social media attention is a significant driver of investment behavior, which Odin must account for when modeling user financial decisions. It demonstrates that digital financial literacy does not uniformly moderate this effect, suggesting Odin's behavioral profiling (Topic 5.A) must be context-sensitive. The cross-country comparison provides a template for evaluating how Odin's algorithms might perform differently across user segments. The methodological approach, including endogeneity correction, offers a framework for robustly evaluating Odin's predictive modules."
  directly_justifies:
    - "Social media attention significantly increases the likelihood of stock investment, requiring Odin to consider external digital signals."
    - "Digital financial literacy's moderating role is context-dependent, necessitating adaptive profiling in Odin."
    - "Endogeneity concerns in behavioral data must be addressed in Odin's evaluation framework."
  limits:
    - "Relies on cross-sectional self-reported data, limiting causal inference."
    - "Attention measure is binary and does not capture intensity or content characteristics."
    - "DFL index components vary across countries, complicating cross-national comparisons."
  mapping_rationale: "Systematic scan across 12 functional domains flagged behavioral profiling (5.A, 5.C) as highly relevant due to direct analysis of attention and DFL on investment decisions. The Filipino context (1.C, 2.D) was considered relevant because the Philippines is a sample country, though the paper does not focus on Filipino-specific practices. Existing systems gaps (4.B) and evaluation frameworks (12.A) were noted as low relevance because the paper does not evaluate PFMS but provides methodological insights. Domains like expense categorization (3.A) and budget recommendation (7.A) were rejected as the paper focuses on investment, not expense management. The overall relevance is moderate: it offers behavioral and methodological insights for Odin's profiling and evaluation modules but does not directly address core PFMS functionalities."
limitations:
  - "Cross-sectional design limits causal inference and dynamic analysis. [unacknowledged]"
  - "Self-reported data may introduce reporting and social desirability biases. [unacknowledged]"
  - "The attention question was newly introduced, preventing longitudinal comparisons. [acknowledged]"
  - "Results are based on only four countries, limiting generalizability. [acknowledged]"
  - "DFL moderating effect is heterogeneous, requiring context-specific interpretation. [acknowledged]"
remember_this:
  - "Social media attention increases stock investment propensity by 12.2% on average."
  - "Digital financial literacy's moderating role varies significantly by country context."
  - "DFL does not universally buffer against social media persuasion."
  - "Endogeneity concerns in behavioral finance require robust econometric correction."
  - "Context-sensitive digital literacy is critical for financial system design."
```
---

## Paper 3: Rafiaei_summarized.md

**Source File:** `Rafiaei_summarized.md`

```yaml
paper_id: 2d8a3b1c-5e4f-4a2b-9c7d-8f1e3a5b7c9d
designation: international-algorithm-specific
title: Keyword Matching vs. LLM-Based Classification for Personal Finance Transaction Categorization: A Benchmark Study on Real Canadian Bank Data
authors: Rafiaei, M.
year: 2026
venue: Unknown
odin_topics:
  - 3.A
  - 5.C
  - 6.A
  - 12.A
  - 12.B
  - 4.A
  - 8.A
tldr: A benchmark study of transaction classification on Canadian bank data finds LLMs outperform keyword matching by 51 percentage points and resolve structural limitations including context blindness and coverage decay.
problem_and_motivation: Automatic transaction categorization is central to personal finance software, yet the dominant keyword-based approach exhibits uneven performance across account types. No prior work has studied the performance gap on real Canadian bank data or provided a statistically validated comparison with LLMs.
approach:
  - Constructed a labeled dataset of 7,152 transactions from two account holders, five accounts across two Canadian banks (CIBC and BMO), spanning 4.5 years (September 2021 – April 2026).
  - Implemented a priority-ordered keyword dictionary classifier with 45 patterns, routed by account type, following the inverted-index retrieval model.
  - Experiment 1: Controlled benchmark on 200 CIBC chequing transactions comparing keyword matching to Claude (claude-3-5-sonnet-20241022) in a zero-shot regime.
  - Experiment 2: Exploratory scale-up on all 7,152 transactions using Llama-3.1-8B and Llama-3.3-70B via Groq API, with ground-truth labels generated by the MonIQ rule-based import parser.
  - Conducted formal structural analysis of three keyword classifier limitations and proposed a hybrid cascade architecture.
findings:
  - num: Keyword classifier achieved 96.3% category F1 on credit card but only 27.5% on chequing, a 69 percentage point structural gap.
  - num: In the controlled benchmark, Claude achieved 96.5% type accuracy versus 45.5% for keyword matching, a +51.0 percentage point improvement (McNemar's χ²=81.06, p<0.001).
  - num: Claude raised Transfer F1 from 0% to 99.0%, Fees F1 from 13.7% to 100%, and Insurance F1 from 0% to 100%.
  - num: Llama-3.3-70B achieved 71.9% type accuracy and 42.8% category accuracy on the full dataset, with Transfer F1 rising from 40.1% (8B) to 57.9% (70B), establishing Transfer classification as the single most diagnostic metric.
  - Three root causes account for all chequing keyword errors: transfer-fee ambiguity (67.1%), income-expense context dependence (12.6%), and incomplete merchant coverage (20.4%).
  - LLMs resolve all three structural limitations of keyword matching: context blindness, coverage decay, and priority collision.
key_figures_tables:
  - Figure 1: Precision, recall, and F1 definitions with numerical example from Transfer category data → Defines metrics used in the evaluation.
  - Figure 2: Per-category F1 scores, keyword classifier, CIBC evaluation subset (N=2,222) → Visualization of the 69pp gap between credit card and chequing.
  - Figure 3: Failure mode breakdown of 868 errors in keyword classification → Identifies transfer-fee ambiguity as dominant (67.1%).
  - Figure 4: Hybrid cascade classifier architecture → Keyword handles high-confidence cases; LLM escalates ambiguous chequing transactions (~20-30%).
  - Table VI: Llama model size comparison on full dataset (Exploratory) → Shows model-size effect on Transfer F1 (40.1% to 57.9%).
key_equations:
  - equation: f(d) = γ(k_i*) where i* = min{i : k_i ⊆ d}; f(d) = c_default if no match
    explanation: Keyword classifier definition: priority-ordered dictionary matching.
  - equation: F1 = 2·TP/(2·TP+FP+FN)
    explanation: F1 calculation for imbalanced category distributions.
definitions:
  - term: PFMS
    definition: Personal Finance Management System
  - term: LLM
    definition: Large Language Model
  - term: F1
    definition: Harmonic mean of precision and recall, ranges from 0 to 1
  - term: Transfer F1
    definition: F1 score specifically for the Transfer category classification
critical_citations:
  - "[Lesner et al., 2019] — Large-scale production system for personalized categorization"
  - "[García-Méndez et al., 2020] — SVM for banking transaction descriptions"
  - "[Kotios et al., 2022] — Hybrid rule-based and ML categorization model"
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Directly benchmarks and compares categorization methods (keyword vs. LLM) for personal finance transactions.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Evaluates classification approaches (keyword matching and LLMs) for categorizing financial transactions, which underpin behavioral profiling.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Provides a foundation for accurate transaction data that informs predictive modeling, though not directly about forecasting.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Offers a benchmark methodology and statistical validation framework for evaluating classification modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Directly evaluates and compares algorithmic modules (keyword classifier and LLMs) with statistical rigor.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Mentions existing systems (Mint, YNAB, Monarch Money) and their reliance on keyword matching.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: The formal analysis of classification failures could inform anomaly detection by identifying ambiguous or misclassified transactions.
  contribution: This paper provides a labeled dataset and benchmark for transaction classification on Canadian bank data, with a statistically validated comparison showing LLMs outperform keyword matching. The findings justify Odin's adoption of LLM-based or hybrid classification for chequing accounts to improve accuracy. The formal analysis of keyword limitations provides a theoretical foundation for designing robust categorization modules. The identification of Transfer classification as the most diagnostic metric directly informs Odin's evaluation strategy for classification algorithms. The cost-accuracy tradeoff analysis and hybrid cascade proposal offer a practical design pathway for Odin's expense categorization module.
  directly_justifies:
    - LLMs resolve structural limitations of keyword matching including context blindness and coverage decay.
    - Transaction classification accuracy on chequing accounts is fundamentally limited by description format, not tuning.
    - A hybrid cascade architecture can achieve high accuracy with acceptable latency and cost.
    - Transfer category F1 is the single most diagnostic metric for evaluating classification performance.
  limits:
    - Controlled benchmark uses a 200-transaction stratified sample from one CIBC chequing account.
    - Experiment 2 ground-truth labels were generated by a keyword parser, introducing circular dependence for Llama evaluation.
    - Results may not generalize across all Canadian banks or account holder demographics.
    - No cross-user generalization tests were performed on the BMO accounts.
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The Expense Categorization (3.A) and Classification Approaches (5.C) domains were flagged as high relevance due to the paper's direct benchmarking of transaction classification methods. Behavioral Profiling (5.A) and Forecasting (6.A) were considered medium relevance as accurate categorization is foundational but not the primary focus. System Evaluation (12.A/B) was flagged as high because the paper provides a rigorous evaluation framework with statistical validation. Existing Systems (4.A) was considered low as the paper only references them. Anomaly Detection (8.A) was contextual because while failure analysis could inform anomaly detection, it is not explicitly addressed. Budget Recommendation (7.A-D), Savings & Debt Management (13.A-C), Mobile-First Design (9.A-B), Data Privacy (10.A-B), User Retention (11.A-B), and Filipino Cultural Context (2.A-D) were rejected as they are not addressed. The paper's overall relevance to Odin is high for its classification module design and evaluation methodology.
limitations:
  - Controlled benchmark uses a 200-transaction stratified sample from one CIBC chequing account [unacknowledged].
  - Experiment 2 ground-truth labels were generated by a keyword parser, introducing circular dependence for Llama evaluation [unacknowledged].
  - Results may not generalize across all Canadian banks or account holder demographics.
  - No cross-user generalization tests were performed.
  - Hybrid cascade architecture is estimated, not empirically validated [unacknowledged].
remember_this:
  - Keyword matching achieves 96.3% F1 on credit cards but only 27.5% on chequing.
  - Claude achieves 96.5% type accuracy versus 45.5% for keyword matching.
  - Transfer classification is the most diagnostic metric for this task.
  - LLMs resolve all three structural limitations of keyword matching.
  - A hybrid cascade can balance accuracy, latency, and cost.
```
---

## Paper 4: Ilic et al_summarized.md

**Source File:** `Ilic et al_summarized.md`

```yaml
paper_id: 10.3390/fi18030156
designation: international-algorithm-specific
title: Adaptive Healthcare Monitoring Through Drift-Aware Edge-Cloud Intelligence
authors: Stojnev Ilic, A.; Ilic, M.; Stojanovic, N.; Stojanovic, D.
year: 2026
venue: Future Internet
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 9.A
  - 9.B
  - 10.A
  - 12.A
tldr: Drift-aware edge-cloud architecture elevates concept drift to a supervisory signal for adaptive model lifecycle, user reclassification, and inference consistency in non-stationary healthcare streams.
problem_and_motivation: Physiological data streams are inherently non-stationary, causing static models to deteriorate. Treating drift as a maintenance signal is insufficient for systems requiring continuous, accurate, and resource-efficient inference, particularly in distributed IoT environments.
approach:
  - Proposed a drift-aware multi-tier edge-cloud architecture with hierarchical drift handling: lightweight screening at the edge, rigorous validation in the cloud.
  - Edge nodes perform low-latency inference and preliminary drift screening under resource constraints using a four-detector ensemble.
  - Cloud tier executes advanced drift validation, orchestrates user reclassification, model retraining, and manages model evolution via a feedback loop.
  - The system integrates a Model-as-a-Service component for model distribution, versioning, and atomic deployment to edge devices.
  - Evaluated on a containerized testbed with 20 synthetic multi-user streams and one real continuous glucose monitoring dataset.
findings:
  - num: 40.6% reduction in prediction MAE compared to periodic retraining.
  - num: End-to-end adaptation latency from drift onset to edge deployment was 66 ± 37 seconds.
  - num: Hierarchical cloud validation reduced the false-positive retraining rate from 88.9% (edge-only) to 27.3%.
  - The system maintained uninterrupted inference throughout all adaptation events.
  - Dynamic user-state modeling successfully reduced retraining frequency by reassigning users to compatible model ensembles.
key_figures_tables:
  - Figure 3: End-to-end execution timeline for multiple users → Drift events trigger a coordinated validation, retraining, and deployment pipeline.
  - Figure 4: Prediction error over time for real CGM user → Drift-aware adaptation prevents performance degradation and triggers timely model updates.
  - Table 4: System-level performance metrics → Quantifies detection delay, validation pass rate, and latency of the feedback loop.
key_equations:
  - equation: "P(X, y) changes between t and t+∆t"
    explanation: Formal definition of concept drift occurrence.
definitions:
  - term: Concept Drift
    definition: Temporal changes in data distributions or in the relationship between input features and target variables.
  - term: CGM
    definition: Continuous Glucose Monitoring, a representative sensing modality generating minute-level physiological data.
  - term: MaaS
    definition: Model-as-a-Service, a logical service responsible for model distribution, version management, and deployment coordination.
critical_citations:
  - "[Webb et al., 2016] — Formalizes concept drift in streaming data."
  - "[Lu et al., 2020] — Comprehensive review of concept drift adaptation."
  - "[Gkonis et al., 2023] — Survey on challenges in IoT-edge-cloud continuum."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Proposes a drift-aware framework for continuous adaptation of predictive models on streaming data.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: The architecture explicitly addresses forecasting on sequential, non-stationary data streams.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: The system's goal includes anomaly detection on glucose streams, a relevant analog for spending anomaly detection.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: The edge tier operates on resource-constrained devices, aligning with mobile-first constraints.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: contextual
      justification: Mentions a user-facing component for visualization and actions, relevant to mobile UX, but not a primary focus.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Acknowledges privacy as a future direction but does not directly address security mechanisms.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a concrete system-level evaluation methodology and performance baselines for adaptive systems.
  contribution: "The architecture provides a blueprint for building drift-aware financial management systems where user spending patterns evolve over time. The hierarchical drift-handling strategy can be directly applied to detect and adapt to changing financial behavior, preventing budget recommendations from becoming outdated. The feedback loop and MaaS integration offer a design for continuous model improvement in a PFMS. The evaluation methodology, particularly the use of real-world data to validate adaptation, sets a precedent for evaluating such systems in Odin."
  directly_justifies:
    - "Concept drift should be elevated from a maintenance signal to a primary mechanism governing system adaptation."
    - "Hierarchical drift detection with edge screening and cloud validation is essential for balancing responsiveness and stability."
    - "User reclassification to compatible model states can reduce unnecessary retraining and computational cost."
    - "Asynchronous adaptation is sufficient to preserve continuous inference during system updates."
    - "A feedback loop decoupling inference, retraining, and deployment reduces operational risk."
  limits:
    - "Evaluation is conducted in a containerized environment that does not fully replicate real-world network instability."
    - "The dataset is limited to one physiological signal (CGM), requiring further validation on financial transaction data."
    - "User reclassification strategy is demonstrated but not subjected to a comparative quantitative analysis of optimality."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The domains flagged as highly relevant were Spending Forecasting (6.A, 6.B), as the core contribution is a forecasting pipeline for non-stationary data; Anomaly Detection (8.A), as the system performs anomaly detection; and System Evaluation (12.A), due to its rigorous evaluation framework. Mobile-First Design (9.A, 9.B) was assigned medium/contextual relevance due to the edge deployment constraints and user-facing components. Data Privacy (10.A) was noted as a future work, hence contextual. Domains such as Filipino Cultural Context (2.A-D), Expense Categorization (3.A-C), and User Retention (11.A-B) were considered and rejected as they are outside the scope of this algorithmic architecture paper. The architecture is highly relevant to Odin as it provides a concrete, validated design for an adaptive inference system that can manage evolving user behavior."
limitations:
  - "Evaluation was conducted in a containerized testbed, not a real-world distributed network with instability."
  - "Only evaluated on CGM data; applicability to financial transaction streams requires further validation. [unacknowledged]"
  - "Quantitative analysis of user reclassification optimality is deferred to future work."
  - "Considerations for privacy, regulatory compliance, and security are explicitly beyond the current scope."
remember_this:
  - "Drift-aware adaptation reduced prediction MAE by 40.6% compared to periodic retraining."
  - "Hierarchical cloud validation cut false-positive retraining rates from 88.9% to 27.3%."
  - "Concept drift must be treated as a first-class system event, not passive monitoring."
  - "Asynchronous retraining and deployment preserves continuous inference during updates."
  - "User reclassification to existing model states can effectively limit retraining frequency."
```
---

## Paper 5: Tia et al_summarized.md

**Source File:** `Tia et al_summarized.md`

```yaml
paper_id: 10.48550/arXiv.2505.22125
designation: "local-algorithm-specific"
title: "Sentiment Simulation Using Generative AI Agents"
authors: "Tia, M.; Lanuzo, J. S.; Baltazar, L. R.; Lopez-Relente, M. J.; Quiñones, D. M.; Albia, J."
year: 2026
venue: "Unknown"
odin_topics:
  - "1.A"
  - "5.A"
  - "5.B"
  - "5.C"
  - "12.A"
  - "12.B"
tldr: "A generative AI agent framework with contextualized psychographic profiles achieves up to 92% alignment in replicating survey responses and 81-86% accuracy in sentiment simulation, demonstrating scalable sentiment modeling grounded in behavioral science."
problem_and_motivation: "Traditional sentiment analysis relies on surface linguistic patterns and retrospective data, failing to capture psychological drivers and limiting predictive insight for policy testing and behavioral forecasting. This constrains applications like narrative framing and synthetic focus groups. The paper aims to enable prospective sentiment simulation through psychographically grounded AI agents."
approach:
  - "The framework uses Llama 3.1 70B to instantiate agents from a nationally representative survey of 2,485 Filipino respondents with sociodemographic and psychological variables (personality, values, beliefs, attitudes)."
  - "Two encoding strategies are compared: categorical labels (e.g., Low, Moderate, High) and contextualized narrative descriptions of psychological traits."
  - "Agents are exposed to real-world socio-political and economic scenarios (wage policies, budget transparency, inflation, justice system, political dynasties) with positive or negative framing."
  - "Agents generate sentiment ratings on a 5-point Likert scale accompanied by explanatory rationales, followed by a self-assessment for coherence."
  - "Performance is evaluated using Quadratic Weighted Accuracy (QWA) and statistical tests (Wilcoxon signed-rank, paired t-test, Cohen's d) across repeated trials."
findings:
  - "num: Contextualized encoding achieved 92% alignment in survey replication, significantly outperforming categorical encoding (p<0.0001, Cohen's d=0.70)."
  - "num: Sentiment simulation accuracy ranged from 81% to 86% across five scenarios, with contextualized encoding outperforming categorical in four scenarios."
  - "num: Simulation outputs were stable across repeated trials with standard deviations of 0.17% to 0.51%."
  - "num: Scenario framing did not significantly affect accuracy (p=0.9676, Cohen's d=0.02), indicating robustness."
  - "Contextualized encoding improved accuracy most for political dynasties (+12.8%) and inflation (+6.9%)."
  - "The justice system scenario showed near-identical performance between encodings, suggesting less reliance on psychological traits."
key_figures_tables:
  - "Figure 2: Cumulative distribution of QWA scores by encoding strategy → Contextualized encoding shifts distribution rightward, indicating higher alignment."
  - "Figure 3: Per-agent comparison of QWA scores → Most agents show improved alignment with contextualized encoding."
  - "Figure 4: QWA across positive and negative framing → Scores remain high and similar across framing, with negligible effect size."
  - "Table 3: Sentiment simulation accuracy across scenarios → Contextualized encoding consistently outperforms categorical except in justice system."
key_equations:
  - equation: "w_{ij} = 1 - (d_{ij} / d_{max})^2"
    explanation: "Quadratic weight for ordinal alignment, penalizing distant misclassifications."
  - equation: "t = \\bar{d} / (s_d / \\sqrt{n})"
    explanation: "Paired t-test for comparing framing conditions."
definitions:
  - term: "QWA"
    definition: "Quadratic Weighted Accuracy; metric for ordinal classification that weights errors quadratically by distance."
  - term: "Contextualized encoding"
    definition: "Narrative description of psychological traits integrated into prompts to enhance agent realism."
  - term: "Categorical encoding"
    definition: "Discrete labels (Low, Moderate, High) used to represent psychological variables in prompts."
  - term: "LLM"
    definition: "Large Language Model; here, Llama 3.1 70B used as the generative agent engine."
critical_citations:
  - "[Aher et al., 2023] — LLMs can replicate human subject studies across domains."
  - "[Park et al., 2023] — Generative agents exhibit emergent human-like behavior."
  - "[Park et al., 2024] — LLM-based agents replicate survey responses with ≈85% accuracy."
  - "[Xie et al., 2024] — LLM agents simulate human trust behavior."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "low"
      justification: "Provides nationally representative Filipino sample including young adults but not exclusively young professionals."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Directly demonstrates creating psychographically grounded agent profiles that can inform financial behavioral profiling."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "medium"
      justification: "Agent embodiment from survey data offers a method for initializing profiles in cold-start scenarios."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "The LLM-based sentiment simulation approach could be adapted to classify financial behavioral profiles."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "low"
      justification: "Uses QWA and statistical tests for evaluation, providing general methodological insights for system evaluation."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Evaluates the simulation algorithm with rigorous metrics, applicable to evaluating Odin's algorithmic components."
  contribution: "The paper's agent simulation framework can directly inform Odin's behavioral profiling module (Topic 5.A) by providing a data-driven approach to characterize user attitudes and preferences based on validated psychological constructs. Its use of QWA and statistical significance testing offers a rigorous evaluation framework that can be applied to assess Odin's recommendation and anomaly detection modules (Topics 12.A and 12.B). The robustness of agent responses to framing suggests that such simulations can provide stable baselines for cold-start scenarios (Topic 5.B) where user data is limited. The paper's reliance on nationally representative Filipino data provides contextual grounding for Odin's target demographic (Topic 1.A), though it does not focus exclusively on young professionals."
  directly_justifies:
    - "Contextualized encoding of psychological profiles significantly improves agent-human alignment over categorical encoding."
    - "Agent simulations can replicate survey responses with up to 92% accuracy."
    - "Sentiment simulation accuracy remains stable across alternative scenario framings."
    - "The framework provides a scalable approach for synthetic population simulation in behavioral science."
  limits:
    - "The paper does not address personal finance scenarios or spending behavior specifically."
    - "The framework uses a generic LLM without fine-tuning for financial domain; performance on financial tasks is untested."
    - "The sample includes all adult age groups, not specifically young professionals, limiting direct applicability to Odin's target demographic."
  mapping_rationale: "A systematic scan across all 12 functional domains and associated topic codes was performed. The paper was flagged as relevant to Behavioral Profiling & Classification (topics 5.A, 5.B, 5.C) because it demonstrates the creation of psychographically grounded agent profiles from survey data and uses them to simulate responses, directly supporting the development of behavioral profiles. It also contributes to System Evaluation (topics 12.A, 12.B) due to its rigorous use of QWA and statistical tests for evaluating simulation alignment. Topic 1.A was considered low relevance because while the data is Filipino, it does not focus on young professionals; this borderline case was resolved by including it with low relevance due to demographic overlap. All other domains—Expense Categorization, Spending Forecasting, Budget Recommendation, Anomaly Detection, Mobile-First Design, Data Privacy, User Retention, and Savings & Debt Management—were rejected as the paper does not provide citeable claims or methods that inform Odin's design or implementation in those areas. Overall, the paper's primary relevance to Odin lies in its methodology for behavioral profiling and evaluation, offering a foundation for simulating user attitudes and validating system outputs."
limitations:
  - "The simulation relies on self-reported survey data, which may contain response biases. [unacknowledged]"
  - "The framework does not model temporal dynamics of sentiment or behavior. [unacknowledged]"
  - "Generalizability to other cultural contexts or financial domains is not established."
  - "The use of Llama 3.1 70B may introduce proprietary or computational constraints."
remember_this:
  - "Contextualized psychographic profiles yield 92% alignment in replicating survey responses."
  - "Sentiment simulation accuracy ranges from 81% to 86% across scenarios."
  - "Framing effects are negligible with Cohen's d of 0.02."
  - "The framework provides a scalable method for synthetic population simulation."
  - "Contextualized encoding outperforms categorical in most scenarios, especially for complex issues."
```
---

## Paper 6: Amrith_summarized.md

**Source File:** `Amrith_summarized.md`

```yaml
paper_id: 10.1080/1369183X.2025.2542769
designation: international
title: "Reimagining social protection: financialised futures among ageing migrant domestic workers in Asia"
authors: "Amrith, M."
year: 2026
venue: "Journal of Ethnic and Migration Studies"
odin_topics:
  - "2.C"
  - "2.D"
  - "4.B"
  - "5.A"
  - "7.A"
  - "10.B"
  - "13.A"
tldr: "Financial education courses for ageing Filipino domestic workers cultivate self-responsibility for retirement security amid precarious state and kinship social protection."
problem_and_motivation: "Migrant domestic workers face precarious futures with limited state-based social protection and uncertain kinship care upon mandatory return. Financial education courses have proliferated to address this gap, yet their role and implications are understudied. The paper examines how these courses shape aspirations and strategies for later-life security."
approach:
  - "Ethnographic fieldwork in Singapore and Hong Kong from 2018 to 2022."
  - "Conducted over 50 in-depth interviews with migrant domestic workers aged 45-65 from the Philippines, Indonesia, India, and Sri Lanka."
  - "Observed financial education courses run by NGOs, corporate partners (KPMG), and a Filipino-led cooperative."
  - "Followed online spaces (WhatsApp, Facebook, YouTube) during the COVID-19 pandemic."
  - "Engaged with policy officers, cooperative representatives, and activist leaders."
findings:
  - "Financial education cultivates a narrative of transformation from breadwinner to financially-independent investor."
  - "Participation enables women to give themselves permission to save for themselves, challenging endless remittance obligations."
  - "Financialised aspirations exist alongside alternative strategies: political activism, faith-based resignation, and land ownership."
  - "The 'self' in financialisation remains socially embedded, with migrants continuing to navigate kin obligations and employer dependencies."
  - "num: Only 5% of overseas Filipinos in Singapore paid into the state social security system (SSS) as of 2018."
  - "State-backed schemes and private financial products generate new forms of dependency alongside promises of independence."
key_figures_tables:
  - "None."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "SSS"
    definition: "Philippine Social Security System, a contributory pension scheme."
  - term: "OFW"
    definition: "Overseas Filipino Worker."
  - term: "Paluwagan"
    definition: "Informal rotating savings and lending group among Filipinos."
critical_citations:
  - "[Rodriguez, 2010] — Philippine state's institutionalized labour export policy."
  - "[Silvey and Parreñas, 2020] — Precarity chains in domestic worker migration."
  - "[Nguyen, 2021] — Portfolios of social protection in contexts of limited state welfare."
  - "[Kar, 2017] — Financialisation of social security and self-help narratives."
relevance:
  topics:
    - code: "2.C"
      name: "User-Declared Financial Preferences"
      relevance: "high"
      justification: "Directly examines how migrant women articulate and shift their financial goals and priorities."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "medium"
      justification: "Discusses remittance obligations tied to family events and cyclical demands."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Provides detailed evidence of gaps in state social security and kinship care for returning migrants."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Describes the shift from a breadwinner to an investor mindset, revealing behavioral profile dynamics."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "medium"
      justification: "Financial literacy courses teach budgeting as a core strategy for future security."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "medium"
      justification: "Examines trust in financial products, employers, and state schemes; highlights scam awareness."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "high"
      justification: "Core focus on how migrant women plan and invest savings for retirement goals."
  contribution: "This paper informs Odin's understanding of financial behavioral profiles (5.A) by detailing the transformation from remittance-focused breadwinner to self-oriented investor among Filipino migrants. It provides evidence for the design of savings goal management (13.A) by illustrating real-world strategies like land purchase and cooperative investments. It highlights user trust dynamics (10.B) in financial products and state schemes, crucial for Odin's data privacy and trust modules. The findings on budget recommendation (7.A) reveal that financial literacy courses are a form of domain knowledge that Odin can emulate. The paper's evidence on the limitations of existing systems (4.B) directly justifies Odin's need to address gaps in social protection and financial planning."
  directly_justifies:
    - "Migrant women shift from viewing themselves as breadwinners to investors."
    - "State-based social security coverage for overseas Filipinos is extremely low (5%)."
    - "Financial education courses promote self-responsibility for retirement security."
    - "Kinship care is not a guaranteed form of social protection for returning migrants."
    - "Financialised aspirations exist alongside alternative strategies like activism and faith."
  limits: |
    - Focus on Filipino migrants may limit generalizability to other nationalities.
    - The study is qualitative and does not quantitatively measure the long-term financial outcomes of course participation.
    - The research was conducted during a specific period (2018-2022) including COVID-19, which may have influenced dynamics.
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to 'Behavioral Profiling & Classification' (5.A) and 'Savings & Debt Management' (13.A) due to its detailed account of the breadwinner-to-investor mindset shift and savings strategies. It showed medium relevance to 'Expense Categorization' (2.C, 2.D), 'Existing Systems & Gaps' (4.B), 'Budget Recommendation' (7.A), and 'Data Privacy & User Trust' (10.B) due to its discussions on financial preferences, system gaps, budgeting, and trust dynamics. Domains like 'Spending Forecasting' (6.A, 6.B), 'Anomaly Detection' (8.A), and 'Mobile-First Design' (9.A) were considered but rejected as the paper does not address predictive modeling, anomaly algorithms, or mobile UX. The borderline case of seasonal spending (2.D) was resolved by selecting 2.D as a medium relevance topic because the paper discusses cyclical remittance demands tied to family events and 'crises,' which are analogous to seasonal patterns. The paper's overall relevance to Odin is substantial, providing qualitative insights into user behavior, system gaps, and trust, though it is not directly algorithmic."
limitations:
  - "Focuses on a specific demographic (ageing Filipino domestic workers) which may not generalize to all Filipino young professionals. [unacknowledged]"
  - "The study is qualitative and does not provide quantitative metrics for financial literacy program effectiveness. [unacknowledged]"
  - "The research was conducted in Singapore and Hong Kong; findings may not apply to other migration contexts."
  - "Does not examine the long-term outcomes of financial education, such as actual retirement security."
remember_this:
  - "Only 5% of overseas Filipinos in Singapore contribute to the state pension system."
  - "Migrant women are taught to prioritize self-savings over endless kin remittances."
  - "Financialisation creates new aspirations for independence and purpose in retirement."
  - "Social protection remains a hybrid portfolio of state, kin, and market actors."
  - "Financial education is one strategy among many, including activism and faith."
```
---

## Paper 7: Sireesha et al_summarized.md

**Source File:** `Sireesha et al_summarized.md`

```yaml
paper_id: 3b5f9c8e-6d4a-4f2e-8b1c-9a7d6e5f4c3b
designation: international-algorithm-specific
title: AI-Based Personal Finance Manager
authors: Sireesha, B.; Kumar, K. K.; Lavanya, O.; Keshan, S.; Ramsai, N.; Kumar, K. L.
year: 2026
venue: International Journal of AI Electronics and Nexus Energy
odin_topics:
  - 3.A
  - 3.B
  - 4.B
  - 6.A
  - 6.B
  - 7.B
  - 8.A
  - 8.B
  - 12.A
  - 10.A
  - 10.B
  - 11.A
tldr: An AI-based personal finance manager uses machine learning and deep learning to automate expense categorization, forecast spending, and provide personalized financial recommendations.
problem_and_motivation: Users struggle to monitor spending and make informed financial decisions due to limited time, financial literacy, and analytical tools. AI provides an effective solution by enabling automated, personalized, and data-driven financial management.
approach:
  - Data is collected from banking statements, e-commerce receipts, and user inputs.
  - Preprocessing includes cleaning, normalization, tokenization, and category mapping.
  - Random Forest and neural networks classify transactions into categories like food and rent.
  - An LSTM model predicts future expenses and revenue based on historical patterns.
  - The system uses Isolation Forest for anomaly detection and a hybrid model combining rule-based logic, supervised ML, and reinforcement learning for recommendations.
findings:
  - num: The Random Forest expense classifier achieved 93–96% accuracy.
  - num: Traditional rule-based systems plateau at around 75–80% accuracy.
  - num: The LSTM forecasting model achieved a Mean Absolute Error (MAE) of 4.7%.
  - num: Anomaly detection demonstrated a precision of 92%.
  - num: 84% of users reported better spending awareness, and 78% claimed increased savings control.
key_figures_tables:
  - "Table 1: Accuracy comparison of ML models → Random Forest outperforms traditional rule-based systems."
  - "Table 2: LSTM forecasting performance → MAE of 4.7% for monthly expenditure prediction."
key_equations:
  - equation: "MAE = (1/n) * Σ|y_i - ŷ_i|"
    explanation: "Mean Absolute Error for LSTM forecasting accuracy."
definitions:
  - term: "LSTM"
    definition: "Long Short-Term Memory, a recurrent neural network for time-series prediction."
  - term: "Random Forest"
    definition: "An ensemble learning method for classification and regression."
  - term: "Isolation Forest"
    definition: "An anomaly detection algorithm that isolates outliers."
critical_citations:
  - "[Patel and Kumar, 2022] — AI-driven personal finance automation."
  - "[Chen et al., 2022] — Deep learning for financial forecasting."
  - "[Singh and Sharma, 2021] — LSTM for expense prediction."
  - "[Zhao, 2021] — Isolation Forest for financial anomaly detection."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: "Evaluates Random Forest and neural networks for classifying transactions."
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: "Discusses mapping transactions to categories like food, rent, and utilities."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: "Explicitly compares AI system against static, rule-based tools and their limited personalization."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: "Uses LSTM for time-series financial prediction."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: "Applies LSTM to forecast monthly expenditures and recurring payments."
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: "Recommendation engine suggests savings, budget adherence, and expense reduction."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: "Uses Isolation Forest to detect unusual transactions and overspending."
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: "Evaluates Isolation Forest precision for fraud prevention."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: "Presents usability study with 50 participants and quantitative metrics."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: "Mentions security concerns and blockchain for tamper-proof logs as future work."
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: "Uses explainable AI to improve transparency and user trust."
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: "Reports improved user engagement and satisfaction metrics."
  contribution: "This paper directly justifies the use of a hybrid AI architecture (Random Forest, LSTM, and reinforcement learning) for Odin's predictive modeling and recommendation modules. The high accuracy of expense classification (93–96%) provides a strong empirical basis for Odin's categorization engine. The LSTM forecasting results (MAE 4.7%) support the development of a reliable forecasting module for cash flow prediction. The usability study findings validate the need for personalized, real-time financial insights to enhance user engagement and retention."
  directly_justifies:
    - "Random Forest classifiers can achieve 93–96% accuracy in expense categorization."
    - "LSTM models provide reliable forecasts with a 4.7% MAE for monthly expenditures."
    - "Anomaly detection using Isolation Forest can achieve 92% precision."
    - "Real-time alerts help users avoid unnecessary spending."
    - "User satisfaction increases with personalized budget recommendations."
  limits:
    - "The study was conducted with a limited dataset and 50 participants for usability. [unacknowledged]"
    - "Long-term performance and adaptability of the models are not evaluated. [unacknowledged]"
    - "The paper does not address cold-start scenarios for new users. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains identified the Expense Categorization, Forecasting, and Recommendation domains as highly relevant due to the paper's direct evaluation of ML models for these tasks. The Anomaly Detection domain was flagged as medium relevance due to the evaluation of Isolation Forest. The System Evaluation domain was deemed high relevance because of the reported quantitative metrics (accuracy, MAE, precision) and usability study. Data Privacy and User Trust were considered low to medium relevance because the paper mentions explainable AI and security only briefly, without detailed analysis. Domains like Filipino Cultural Context, Behavioral Profiling, Savings & Debt Management, and Mobile-First Design were rejected as the paper does not address these specific aspects. Overall, the paper is highly relevant to Odin's algorithmic core."
limitations:
  - "The dataset size and diversity are not fully specified, which may affect generalizability. [unacknowledged]"
  - "The study does not address the cold-start problem for new users. [unacknowledged]"
  - "There is no discussion of model fairness or bias across different user demographics. [unacknowledged]"
remember_this:
  - "Random Forest achieved 93–96% accuracy for expense categorization."
  - "LSTM forecasting achieved a 4.7% Mean Absolute Error."
  - "Anomaly detection precision reached 92% with Isolation Forest."
  - "84% of users reported better spending awareness."
  - "The system combines supervised, deep, and reinforcement learning."
```
---

## Paper 8: Lockwood et al_summarized.md

**Source File:** `Lockwood et al_summarized.md`

```yaml
paper_id: 9f7a3b4c-5d6e-7f8a-9b0c-1d2e3f4a5b6c # No DOI available
designation: international
title: Machine Learning Approaches for Credit Default Prediction in Emerging Economies
authors: Lockwood, T.; Whitfield, V.; Whitlock, T.
year: 2026
venue: Global Financial Analytics Research Review
odin_topics:
  - 4.B
  - 5.A
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 9.A
  - 10.A
  - 10.B
tldr: A system-level analysis of machine learning credit default prediction in emerging economies, covering algorithmic architectures, data scarcity, alternative data integration, fairness, bias, and regulatory governance.
problem_and_motivation: Traditional credit scoring models developed for advanced economies fail in emerging markets due to fragmented credit registries, large informal sectors, and unbanked populations. Machine learning offers a paradigm shift by leveraging alternative data streams like mobile money and e-commerce footprints. However, deploying these opaque systems introduces challenges around interpretability, algorithmic bias, data privacy, and systemic resilience that require holistic socio-technical governance.
approach:
  - Systematic literature review and synthesis across computational data science, institutional economics, and public policy domains.
  - Analysis of three machine learning architectures: gradient-boosted decision trees, deep neural networks, and multi-agent ensemble systems.
  - Examination of edge deployment architectures with model quantization and knowledge distillation for resource-constrained environments.
  - Assessment of algorithmic fairness frameworks including pre-processing, in-processing, and post-processing interventions.
  - Comparative regional case illustrations across Latin America, Sub-Saharan Africa, and Southeast Asia.
findings:
  - Traditional credit scoring fails in emerging markets due to information asymmetries and lack of formal credit histories.
  - Gradient-boosted trees offer the best balance of predictive accuracy and interpretability for tabular credit data.
  - Deep neural networks capture sequential dependencies but operate as black boxes with systemic opacity risks.
  - Multi-agent ensemble systems enhance robustness by partitioning feature space and isolating data quality anomalies.
  - Alternative data integration without fairness interventions codifies historical societal biases as algorithmic discrimination.
  - Edge deployment with model compression enables offline inference in regions with unstable connectivity.
  - Regulatory sandboxes and algorithmic auditability are essential for consumer protection and systemic stability.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: ML
    definition: Machine Learning
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network architecture
  - term: RNN
    definition: Recurrent Neural Network
  - term: SHAP
    definition: Shapley Additive Explanations, a model interpretability framework
  - term: XGBoost
    definition: Extreme Gradient Boosting, a scalable tree boosting system
  - term: LightGBM
    definition: Light Gradient Boosting Machine, a gradient boosting framework
  - term: CatBoost
    definition: Categorical Boosting, a gradient boosting library handling categorical features
critical_citations:
  - "[Chen & Guestrin, 2016] — Foundational XGBoost algorithm for credit scoring."
  - "[Breiman, 2001] — Random forests ensemble methodology for classification."
  - "[Hardt et al., 2016] — Equality of opportunity framework for algorithmic fairness."
  - "[Björkegren & Grissen, 2020] — Mobile phone transaction data for credit scoring."
relevance:
  topics:
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Critiques traditional credit scoring models for failing in emerging economies.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Uses behavioral data from mobile money and e-commerce for credit profiling.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Core focus on machine learning architectures for default prediction.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: Discusses RNN and LSTM architectures for sequential transaction modeling.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Credit default prediction shares methodological overlap with anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: Reviews ML algorithms applicable to both default prediction and anomaly detection.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Examines edge deployment and mobile inference for credit scoring in low-connectivity regions.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Extensive discussion of data privacy, consumer vulnerability, and digital sovereignty.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Addresses trust, explainability, and consumer recourse in algorithmic lending.
  contribution: This paper provides a comprehensive socio-technical framework for understanding ML-based credit prediction in emerging economies. It directly informs Odin's predictive modeling module by evaluating trade-offs between gradient-boosted trees, neural networks, and ensemble architectures. The analysis of alternative data integration and algorithmic fairness guides Odin's behavioral profiling and anomaly detection design. The deployment infrastructure discussion supports Odin's mobile-first architecture with edge computing considerations. The regulatory and privacy analysis strengthens Odin's data privacy and user trust requirements.
  directly_justifies:
    - "Gradient-boosted decision trees offer the best interpretability-accuracy trade-off for tabular financial data."
    - "Deep neural networks require post-hoc interpretability tools like SHAP for regulatory compliance."
    - "Edge deployment with model compression enables offline inference in low-connectivity environments."
    - "Algorithmic fairness interventions must be integrated to prevent historical bias codification."
    - "Regulatory sandboxes and auditability protocols are essential for responsible ML deployment."
  limits:
    - "The paper is a review without empirical validation of specific models on Philippine data."
    - "No quantitative performance metrics are reported for any specific algorithm on any dataset."
    - "The analysis focuses on credit default rather than personal expense management directly."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to Predictive Modeling (6.A) and Data Privacy (10.A), as it directly addresses ML architectures for financial prediction and extensive privacy concerns in emerging markets. Medium relevance was assigned to Behavioral Profiles (5.A), Forecasting Algorithms (6.B), Mobile-First Design (9.A), User Trust (10.B), and Limitations of Existing Systems (4.B), as these domains are supported by the paper's discussion of behavioral data, sequential modeling, edge deployment, trust, and critiques of legacy systems. Contextual relevance was assigned to Anomaly Detection (8.A, 8.B) due to methodological overlap with default prediction. Topics related to Filipino cultural context, expense categorization, budgeting, and savings management were considered and rejected as the paper does not address these domains. Overall, the paper provides strong conceptual grounding for Odin's predictive and privacy-related modules.
limitations:
  - "No empirical validation on Philippine-specific data or Filipino young professional cohorts."
  - "The review does not provide comparative quantitative benchmarks across evaluated ML architectures. [unacknowledged]"
  - "Regional case illustrations are high-level and lack granular implementation details. [unacknowledged]"
remember_this:
  - "Gradient-boosted trees balance accuracy and interpretability for tabular financial data."
  - "Algorithmic fairness interventions are necessary to prevent historical bias codification."
  - "Edge deployment with model compression enables offline credit inference in low-connectivity regions."
  - "Regulatory sandboxes and auditability are essential for responsible ML system governance."
  - "Alternative data integration exposes vulnerabilities in consumer privacy and digital sovereignty."
```
---

## Paper 9: Silvestre et al_summarized.md

**Source File:** `Silvestre et al_summarized.md`

```yaml
paper_id: 10.1007/s40558-025-00349-9
designation: international-algorithm-specific
title: Navigating uncertainty: enhancing hotel cancellation predictions with adaptive machine learning
authors: Silvestre, P.; Antonio, N.; Carrasco, P.
year: 2026
venue: Information Technology & Tourism
odin_topics:
  - 6.A
  - 6.B
  - 4.A
  - 4.B
  - 12.A
  - 12.B
  - 11.A
  - 11.B
  - 8.A
tldr: Dynamic retraining with a sliding window improves hotel cancellation prediction accuracy during pandemics, supporting proactive revenue management.
problem_and_motivation: Machine learning models for hotel booking cancellations perform well on historical data but are rarely tested under severe disruption like the COVID-19 pandemic. The gap is understanding if pre-pandemic models remain effective under extreme volatility and how to adapt them to maintain predictive accuracy.
approach:
  - Used hotel booking data from four Portuguese hotels (two city, two resort) with 670,343 bookings from 2014 to 2021.
  - Applied XGBoost classifiers with hyperparameter tuning via grid and random search.
  - Study One trained models on pre-pandemic data (before March 2020) and tested on pandemic data.
  - Study Two used a sliding-window training approach incorporating pandemic data with a 24-month training and 9-month test window.
  - Evaluated performance using Accuracy, Precision, F1-Score, and AUC, and interpreted features with SHAP.
findings:
  - num: Pre-pandemic models achieved fair to excellent AUC scores (0.70-0.93) on pandemic test data.
  - num: Sliding-window models improved AUC by up to 5 percentage points over static models.
  - num: A nine-month training window with the sliding approach balanced stability and responsiveness to rapid shifts.
  - Feature importance shifted during the pandemic; LeadTime remained dominant but its effective crossover threshold compressed.
  - num: City hotel C2 achieved the highest performance with an AUC of 0.99 in the sliding-window approach.
  - Resort hotels, which performed worse with static models, showed substantial improvement with the sliding window approach.
key_figures_tables:
  - Table 1: Dataset statistics for four hotels → Provides context on data size and composition.
  - Figure 2: Monthly cancellation rate per hotel pre- and during COVID-19 → Shows unprecedented spikes in cancellations during the pandemic.
  - Table 7: Performance metrics for sliding window models → Documents improved AUC values across all hotels.
  - Figure 5: Lead time density plots with crossover thresholds → Shows pandemic-era compression of cancellation risk thresholds.
  - Figure 7: SHAP summary plots for W2 models → Visualizes the rotation of feature importance across regimes.
key_equations:
  - equation: ADRThirdQuartileDeviation = ADR / ADR_{third quartile of DistributionChannel, per room type, week and year}
    explanation: Captures normalized price position relative to similar bookings.
definitions:
  - term: AUC
    definition: Area Under the ROC Curve, a measure of classification model performance.
  - term: XGBoost
    definition: An optimized gradient boosting algorithm for supervised learning.
  - term: CRISP-DM
    definition: Cross-Industry Standard Process for Data Mining, a structured data mining methodology.
  - term: SHAP
    definition: Shapley Additive Explanations, a method for interpreting model predictions.
  - term: Concept Drift
    definition: Change in the data distribution or the relationship between inputs and outputs over time.
critical_citations:
  - "[António, 2019a] — Established baseline models for booking cancellation prediction."
  - "[Žliobaitė et al., 2016] — Provided theoretical framing for concept drift application."
  - "[Lundberg and Lee, 2017] — Introduced SHAP for model interpretability."
  - "[Baier et al., 2020] — Demonstrated retraining with recent data for concept drift."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly evaluates forecasting models under distributional change.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Tests XGBoost and sliding-window adaptation on sequential booking data.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews state of ML for cancellation prediction, analogous to PFMS forecasting.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies lack of robustness testing under concept drift as a gap.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses standard ML metrics (AUC, F1) and out-of-time validation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Provides a blueprint for evaluating model performance under data shifts.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: Adaptive models support proactive interventions, indirectly linking to user engagement.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: low
      justification: Concept drift management helps maintain forecast reliability for retention strategies.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: The pandemic is treated as an anomaly context, but the paper is about prediction, not detection.
  contribution: This paper provides a validated methodology for building adaptive machine learning models that maintain predictive accuracy under severe disruption, directly applicable to Odin's spending forecasting module. It demonstrates that dynamic retraining with a sliding window outperforms static models, supporting Odin's need for robust and responsive financial predictions. The use of SHAP for tracking feature importance shifts offers a framework for monitoring and explaining changes in user financial behavior. The concept-drift analysis and LeadTime threshold compression can inform Odin's design of proactive notifications and adaptation mechanisms.
  directly_justifies:
    - "Maintaining forecast accuracy under volatility requires scheduled retraining and drift monitoring."
    - "Adaptive models with sliding-window retraining capture rapid shifts in behavioral patterns."
    - "Monitoring feature importance changes helps understand evolving user behavior."
    - "A nine-month training window balances stability and responsiveness in volatile contexts."
    - "Interpretable diagnostics like threshold shifts support actionable model insights."
  limits:
    - "Models were not deployed in a live production environment."
    - "Qualitative reasons behind cancellations or hotel-forced cancellations were not captured."
    - "Customer country of origin, which could provide further insights, was not included."
    - "The study is limited to four hotels in Portugal, which may not generalize to other contexts [unacknowledged]."
  mapping_rationale: The systematic scan across all 12 functional domains and their topic codes flagged the Spending Forecasting domain as highly relevant, with codes 6.A and 6.B identified as high relevance because the paper directly tests and compares forecasting algorithms under distributional shift. The Existing Systems & Gaps domain was assessed as medium relevance, as the paper reviews prior models and identifies the gap in robustness testing. The System Evaluation domain was also medium relevance, as it uses standard ML evaluation metrics and frameworks. The User Retention & Engagement domain was considered low relevance because while adaptive models support proactive interventions, engagement dynamics are not the focus. The Anomaly Detection domain was contextual, as the pandemic is an anomaly context but the paper is about prediction, not detection. Domains related to Filipino cultural context, expense categorization, behavioral profiling, budget recommendation, mobile-first design, data privacy, and savings/debt management were rejected as they are not addressed. The overall relevance is medium-high, as the paper provides a robust methodology and framework for adaptive prediction that directly informs Odin's forecasting module.
limitations:
  - "Models were not deployed in a live production environment."
  - "Qualitative reasons behind cancellations or hotel-forced cancellations were not captured."
  - "Customer country of origin, which could provide further insights, was not included."
  - "The study is limited to four hotels in Portugal, which may not generalize to other contexts [unacknowledged]."
remember_this:
  - "Sliding-window retraining improved AUC by up to 5 percentage points."
  - "Adaptive models better capture rapid shifts in cancellation behavior."
  - "LeadTime remained the dominant predictor despite changed thresholds."
  - "Monitoring feature importance shifts helps identify changing user patterns."
  - "Dynamic model retraining is essential for maintaining accuracy under volatility."
```
---

## Paper 10: Li & Conrad_summarized.md

**Source File:** `Li & Conrad_summarized.md`

```yaml
paper_id: 10.48550/arXiv.2603.27056
designation: international-algorithm-specific
title: Persona-Based Simulation of Human Opinion at Population Scale
authors: Li, M.; Conrad, F. G.
year: 2026
venue: Unknown
odin_topics:
  - 5.B
  - 5.C
  - 9.B
  - 11.B
  - 2.B
tldr: SPIRIT infers semi-structured personas from social media to simulate individual survey responses, producing more accurate and diverse outputs than demographic-only personas when validated against a U.S. probability panel.
problem_and_motivation: Demographic-only personas in LLM simulations are insufficient for capturing the nuance of individual opinions and behaviors, leading to unrealistic and homogenized responses. There is a lack of frameworks that can create rich, reusable person-representations and calibrate them for reliable population-level inference.
approach:
  - The SPIRIT framework uses a Painter module to infer a structured JSON persona (Big Five traits, world beliefs, values, etc.) and a narrative from a user's social media posts.
  - A Reasoner module then conditions an LLM on the inferred persona to answer survey questions, optionally using a web search for time-sensitive topics.
  - The framework was evaluated using 1,410 Twitter/X and 893 Reddit users linked to the Ipsos KnowledgePanel, a U.S. probability-based sample.
  - Performance was benchmarked against 52 held-out non-demographic survey questions, comparing SPIRIT personas against a baseline of 7 demographic attributes.
  - Calibration weights were constructed via raking to align the persona bank with U.S. Census and ACS margins.
findings:
  - num: SPIRIT personas improved user-level inference accuracy by 8–9% over demographic-only personas across all tested models.
  - SPIRIT personas produce substantially broader and more heterogeneous response distributions that more closely resemble human response patterns.
  - Qualitative rationales from SPIRIT agents show a "deliberation bias," where they construct more analytic causal chains than typical human survey respondents.
  - The Persona Bank, after weighting, reproduced coherent within-cluster directional trends that aligned with external polling benchmarks on political issues.
key_figures_tables:
  - Figure 1A: Box plots of per-user composite scores. → SPIRIT distributions show greater human-like heterogeneity than demographic personas.
  - Figure 1B: Bar chart of inference accuracy. → SPIRIT consistently outperforms demographic personas across all model sizes.
  - Figure 2: Bar charts comparing persona-bank and polling benchmarks. → Weighted Twitter-based estimates closely track benchmark magnitudes and directions.
key_equations:
  - equation: w_i \leftarrow w_i \times \frac{T_{v,c}}{\hat{P}_{v,c}}
    explanation: Raking adjustment factor for each margin during iterative proportional fitting.
definitions:
  - term: SPIRIT
    definition: A framework for inferring semi-structured personas from social media to simulate individual opinions.
  - term: Persona Bank
    definition: A collection of SPIRIT personas treated as a virtual respondent panel for surveying.
  - term: Painter Module
    definition: The component of SPIRIT that infers the structured persona profile from raw social media posts.
  - term: Reasoner Module
    definition: The component of SPIRIT that conditions an LLM on the persona to answer downstream tasks.
  - term: Raking
    definition: Iterative proportional fitting used to calibrate sample weights to population benchmarks.
  - term: Position-Weighted Mean
    definition: A composite score aggregating survey responses, weighted by survey sequence order.
  - term: "None."
    definition: ""
critical_citations:
  - "[Argyle et al., 2023] — Foundation for LLM-based human sample simulation."
  - "[Horton, 2023] — Illustrates LLMs as simulated economic agents."
  - "[Park et al., 2024] — Demonstrates generative agent simulations of individuals."
  - "[Kosinski et al., 2013] — Shows digital records predict personal attributes."
relevance:
  topics:
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: high
      justification: Introduces a framework for enriching cold-start profiles from social media to improve simulation fidelity.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: The process of inferring structured personas is a transferable method for classifying profiles from text.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: contextual
      justification: Insights on richer persona data could inform UX personalization, but the paper focuses on survey simulation.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: The persona bank concept offers a method for testing engagement mechanisms on a simulated user base.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: The framework's ability to infer behavioral patterns could be applied to detect cyclical spending from user text.
  contribution: The paper provides a validated methodology for building reusable, rich user personas from digital traces, which can be directly applied to Odin's user profiling module to overcome the cold-start problem. The SPIRIT framework's two-stage design (inference then reasoning) offers a blueprint for creating interpretable financial behavior profiles. Its Persona Bank concept suggests a strategy for testing Odin's features on a representative simulated user base, aiding evaluation frameworks. The study's focus on using non-demographic data to improve prediction supports Odin's rationale for leveraging behavioral and contextual data.
  directly_justifies:
    - SPIRIT personas, inferred from user text, significantly outperform demographic-only baselines in simulating individual responses.
    - Weighted persona banks can produce population-level estimates that align with external benchmarks.
    - A two-stage framework of persona inference and reasoning is effective for LLM-based simulation.
  limits:
    - The paper focuses on simulating survey opinions, not financial behaviors, which are a specific use case for Odin.
    - The evaluation is on a U.S. population panel, and results may not directly generalize to the Filipino context.
    - The "deliberation bias" in agents indicates that simulations may not perfectly replicate human satisficing behavior.
  mapping_rationale: A systematic scan across all 12 functional domains identified relevant work primarily in Behavioral Profiling & Classification (Domain 5). Within this domain, topic 5.B (Profile Dynamics) is flagged as high, as SPIRIT directly solves the cold-start problem by enriching profiles from social media. Topic 5.C (Classification Approaches) is medium, as the persona inference is a specific classification methodology. For User Retention & Engagement (Domain 11), topic 11.B is medium, as the Persona Bank offers a way to test retention strategies. For Mobile-First Design (Domain 9), topic 9.B is contextual, as the persona concept could inform personalization. For Filipino Cultural Context (Domain 2), topic 2.B is medium, as the method of inferring behavioral patterns is applicable to detecting cyclical spending. Other domains like Expense Categorization (3), Anomaly Detection (8), and Savings & Debt Management (13) were considered but rejected as the paper lacks specific methodologies or findings for these financial decision-making tasks. The overall relevance is high for profiling and simulation, providing a methodological foundation for building and evaluating user models in Odin.
limitations:
  - The requirement for active social media accounts introduces selection bias, acknowledged and addressed via weighting.
  - Persona quality is dependent on the richness of the user's text traces, limiting effectiveness for non-expressive users.
  - LLMs exhibit a "deliberation bias," over-analyzing survey questions compared to satisficing human respondents. [unacknowledged]
  - The study's persona schema is comprehensive but may need adaptation for financial-specific attributes like risk tolerance.
remember_this:
  - Non-demographic signals from social media improve simulation accuracy by over 8%.
  - SPIRIT personas create more heterogeneous responses than demographic-only prompts.
  - A persona bank can be a reusable virtual panel for testing and evaluation.
  - Calibration weights are essential for aligning biased samples with population benchmarks.
  - A key LLM limitation is its deliberation bias, which differs from human satisficing.
```
---

## Paper 11: Patterson & Lindberg_summarized.md

**Source File:** `Patterson & Lindberg_summarized.md`

```yaml
paper_id: 10.66372/JGER.v1i1.1
designation: international-algorithm-specific
title: Concept drift monitoring and continual learning in production AI systems: an empirical cost–benefit comparison of detection methods and adaptation strategies
authors: Patterson, S. M.; Lindberg, M. J.
year: 2026
venue: Journal of Global Engineering Review
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
tldr: An empirical comparison of ADWIN, DDM, and Page-Hinkley drift detectors with incremental learning and full retraining shows no single configuration dominates across drift regimes.
problem_and_motivation: Production machine learning models suffer performance degradation from concept drift, but practitioners lack comparative cost-benefit evidence to select detector-strategy pairs. The gap lies in integrating accuracy, latency, compute cost, and false-alarm rate into a unified operational framework.
approach:
  - Evaluated three drift detectors (ADWIN, DDM, Page-Hinkley) on Electricity and SEA benchmarks plus a noisy variant.
  - Paired each detector with incremental learning (Hoeffding tree) and full retraining (XGBoost) adaptation strategies.
  - Defined a cost-benefit score S = α·Acc − β·Lat − γ·Cost − δ·FAR with coefficients calibrated for balanced contribution.
  - Conducted 60 controlled trials across five random seeds per configuration.
  - Measured prequential accuracy, detection delay, update cost, and false-alarm rate.
findings:
  - num: ADWIN with incremental learning achieved the highest mean accuracy (0.864) and lowest update cost (1.00 baseline).
  - num: DDM with retraining had the lowest detection delay (138 steps mean) but cost was 4.7× baseline and false-alarm rate 38% higher.
  - ADWIN+Incremental dominated on gradual, recurring drift (Electricity) with highest accuracy and lowest false alarms.
  - DDM+Retraining recovered fastest on abrupt drift (SEA) but its accuracy advantage was marginal after accounting for delay.
  - Page-Hinkley+Incremental offered a middle ground with lowest false-alarm rate (0.42 per 1k steps) and moderate cost.
  - num: On SEA-Noisy, all detectors degraded by 4–6 percentage points in accuracy.
  - Detector quality is poorly summarized by accuracy alone; two configurations differed by <1% accuracy but nearly 5× in cost.
key_figures_tables:
  - Table 1: Representative studies on drift detection → contextual examples across domains.
  - Table 2: Detector configurations → parameter rationale for ADWIN, DDM, Page-Hinkley.
  - Table 3: Dataset configurations → drift types and points for Electricity, SEA, SEA-Noisy.
  - Table 4: Headline performance comparison → accuracy, latency, cost, FAR across six pairs.
  - Figure 1: Overall research framework → stream input to drift detector to adaptation to scoring.
  - Figure 2: Methodological pipeline → prequential loop showing detector-strategy interaction.
  - Figure 3: Per-segment accuracy vs. compute cost → ADWIN+Incremental flat cost, DDM+Retraining step spikes.
key_equations:
  - equation: S = α·Acc − β·Lat − γ·Cost − δ·FAR
    explanation: Cost-benefit score integrating four operational metrics.
definitions:
  - term: Concept drift
    definition: Change in the joint distribution P_t(x, y) over time.
  - term: ADWIN
    definition: Adaptive Windowing detector using Hoeffding bounds to detect mean shifts.
  - term: DDM
    definition: Drift Detection Method monitoring classifier error-rate changes.
  - term: Page-Hinkley
    definition: Cumulative sum detector for one-sided deviation signals.
  - term: Prequential evaluation
    definition: Online evaluation framework that updates metrics incrementally as data arrives.
critical_citations:
  - "[Zhong, 2024] — Time-decay features for transaction fraud drift."
  - "[Han & Cao, 2024] — Multi-source fusion for credit default early warning."
  - "[Li & Ling, 2026] — Ensemble anomaly detection for community banks."
  - "[Wei & Shang, 2026] — Oversampling-ensemble interactions under imbalance."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly evaluates predictive performance degradation under drift, informing Odin's forecasting module.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Compares adaptation strategies for streaming data, directly applicable to spending forecast updates.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Drift detection is a core component of anomaly detection pipelines; framework informs trigger design.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: ADWIN, DDM, and Page-Hinkley are candidate detectors for spending anomalies.
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: contextual
      justification: Mentions cold-start only indirectly via buffer/window initialization.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Cost-benefit framework provides a multi-metric evaluation template for Odin modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Directly compares algorithmic detector-strategy pairs with controlled experiments.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: low
      justification: Only tangentially related via drift in user behavior distributions.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: contextual
      justification: Identifies gap in cost-benefit evidence for drift handling, analogous to PFMS gaps.
  contribution: The paper provides a directly reusable cost-benefit evaluation framework for Odin's algorithmic modules, particularly for spending forecasting (6.A/6.B) and anomaly detection (8.A/8.B). The empirical comparison of ADWIN, DDM, and Page-Hinkley offers concrete guidance for selecting drift detectors based on dominant drift profiles in user spending data. The adaptation strategy comparison (incremental vs. full retrain) informs Odin's design choices for updating user profiles and budget recommendations. The multi-metric approach (accuracy, latency, cost, false-alarm rate) establishes a template for evaluating Odin's system components beyond predictive accuracy.
  directly_justifies:
    - "ADWIN with incremental learning is preferred when spending patterns change gradually and compute is constrained."
    - "DDM with retraining reacts fastest to abrupt shifts, justifying higher compute for critical anomaly scenarios."
    - "No single detector-strategy pair dominates across all regimes, supporting adaptive configuration in Odin."
    - "False-alarm rate carries significant operational cost, informing threshold tuning for spending anomaly alerts."
  limits:
    - "Benchmarks may not represent all production drift profiles (e.g., seasonal spending cycles)."
    - "Cost coefficients are illustrative rather than universal; teams should calibrate against true unit costs."
    - "Evaluation considered only binary classification; Odin's spending data may involve multi-class or regression settings."
    - "The study does not address privacy-preserving adaptation, which is relevant to Odin's data handling."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The Spending Forecasting domain (6.A, 6.B) was flagged as high relevance because the paper directly evaluates predictive accuracy under drift and compares adaptation strategies for streaming data, both core to Odin's forecasting module. The Anomaly Detection domain (8.A, 8.B) was also high relevance as the drift detectors studied (ADWIN, DDM, Page-Hinkley) are directly applicable to spending anomaly detection, and the cost-benefit framework informs trigger design. The System Evaluation domain (12.A, 12.B) was high relevance because the multi-metric experimental framework provides a template for evaluating Odin's algorithmic modules. Behavioral Profiling (5.A) was considered but assigned low relevance because the paper does not address user profile construction or classification. Existing Systems & Gaps (4.B) was contextual only, as the paper identifies a general gap in cost-benefit evidence analogous to Odin's design gap. Mobile-First Design, Data Privacy, User Retention, and Savings/Debt Management domains were rejected as the paper contains no actionable claims for those areas. The overall relevance is high for forecasting, anomaly detection, and system evaluation modules."
limitations:
  - "Electricity and SEA benchmarks may not represent all production drift profiles; seasonal spending cycles are unrepresented. [unacknowledged]"
  - "Cost coefficients are illustrative; Odin-specific calibration is required. [acknowledged]"
  - "Only binary classification was evaluated; Odin's spending data may require multi-class or regression settings. [unacknowledged]"
  - "Privacy-preserving adaptation is not addressed, limiting direct applicability to privacy-sensitive PFMS contexts. [unacknowledged]"
remember_this:
  - "ADWIN with incremental learning gives the best accuracy-to-cost ratio for gradual drift."
  - "DDM with retraining reacts fastest to abrupt shifts but costs nearly 5× more."
  - "Page-Hinkley offers a middle ground with the lowest false-alarm rate."
  - "No single drift detection configuration dominates across all operational regimes."
  - "The cost-benefit framework enables multi-metric evaluation beyond accuracy alone."
```
---

## Paper 12: Quan_summarized.md

**Source File:** `Quan_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international
title: A Strategic Analysis of AI-Driven Customer Relationship Management Systems in Enhancing Personalization and Retention in Financial Institutions
authors: Quaˆn, T. M.
year: 2026
venue: Orient Journal of Emerging Paradigms in Artificial Intelligence and Autonomous Systems
odin_topics:
  - 6.A
  - 6.B
  - 7.B
  - 7.D
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 12.A
  - 12.B
  - 12.C
tldr: AI-driven CRM systems integrating machine learning and NLP enable dynamic customer segmentation and personalized retention strategies in financial institutions.
problem_and_motivation: Traditional CRM systems based on deterministic rules fail to meet demands for hyper-personalized, context-aware customer experiences. This gap necessitates AI-driven platforms that leverage real-time data and machine learning to adapt to evolving behaviors and improve engagement.
approach:
  - The paper presents a strategic framework for AI-driven CRM architecture, covering data ingestion, feature engineering, and adaptive recommendation.
  - Mathematical models for optimizing retention objectives under probabilistic customer lifetime value estimation are formalized.
  - Simulation results are reported using synthetic and anonymized datasets.
  - The framework emphasizes balancing computational efficiency, regulatory compliance, data privacy, and model interpretability.
  - Modular deployment strategies are evaluated for seamless integration with legacy banking infrastructures.
findings:
  - num: The proposed approach reduces churn rates by up to 15 percent.
  - num: The system increases cross-sell conversion by 22 percent.
  - AI-driven CRM systems facilitate dynamic segmentation and sentiment analysis to enhance personalization.
  - Continuous retraining pipelines are best practices to combat model drift in evolving customer environments.
  - Uplift modeling and causal inference techniques are essential for quantifying the incremental impact of personalized interventions.
key_figures_tables:
  - Table 1: Comparative overview of AI techniques in CRM applications → Summarizes methods, applications, advantages, and challenges.
  - Table 2: Key metrics for evaluating AI-driven CRM performance → Lists CLV, churn rate, NPS, conversion rate, response time, and model accuracy metrics.
key_equations:
  - equation: J(θ) = E[∑γ^t R(s_t, a_t)]
    explanation: Expected discounted cumulative reward under policy πθ.
  - equation: C(θ) = E[∑ c(s_t, a_t)] ≤ C_max
    explanation: Cumulative cost constraint over the horizon.
  - equation: L(θ, λ) = J(θ) - λ(C(θ) - C_max)
    explanation: Lagrangian for constrained optimization.
  - equation: ∇_θ J(θ) = E[∇_θ log π_θ(a|s)Qπθ(s,a)]
    explanation: Policy gradient for optimizing retention.
  - equation: Qπ(s,a)=R(s,a)+γ∑ P(s′|s,a)∑ π(a′|s′)Qπ(s′,a′)
    explanation: Bellman equation for action-value function.
definitions:
  - term: CLV
    definition: Customer Lifetime Value, monetary value over customer lifespan.
  - term: CRM
    definition: Customer Relationship Management.
  - term: MDP
    definition: Markov Decision Process.
  - term: SHAP
    definition: SHapley Additive exPlanations for model interpretability.
  - term: NPS
    definition: Net Promoter Score, a measure of customer loyalty.
critical_citations:
  - "[Huang et al., 2021] — Discusses ethical guidelines for commercial AI in finance."
  - "[Belle, 2019] — Discusses interpretable and responsible AI."
  - "[Chen et al., 2020] — Covers deep learning for laryngoscopic images, used as an example of AI application."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Focuses on predictive modeling using machine learning for churn and engagement.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Discusses sequence-aware recommenders and time-series patterns in transactions.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Provides a general framework for personalized recommendations that can inform budget allocation.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: contextual
      justification: General optimization framework is discussed, not specific to infeasibility.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Discusses short-term aggregates for anomaly detection, though not the central theme.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: General techniques like SHAP and LIME are mentioned for detecting anomalies.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Emphasizes data privacy, encryption, GDPR/CCPA compliance.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Model interpretability is stressed as crucial for regulatory compliance and consumer trust.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: The entire paper is centered on improving engagement metrics through personalization.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: high
      justification: Directly discusses retention strategies and mechanisms to reduce churn.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides comprehensive metrics (CLV, churn, NPS) for evaluating system performance.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Discusses evaluation of specific models (e.g., uplift modeling, survival analysis).
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: low
      justification: The framework is general; not specifically focused on budget recommendation evaluation.
  contribution: The paper provides a strategic framework for AI-driven CRM that directly supports the design of Odin's personalization and retention modules. Its emphasis on real-time data pipelines and feature engineering justifies Odin's data ingestion architecture. The mathematical formulation of constrained policy optimization offers a rigorous basis for Odin's budget recommendation engine under user constraints. The discussion of interpretability, privacy, and regulatory compliance underpins Odin's trust and privacy-by-design principles.
  directly_justifies:
    - "AI-driven CRM systems enable dynamic segmentation and adaptive personalization to improve engagement."
    - "Quantitative gains such as 15% reduction in churn and 22% increase in cross-sell justify investment in personalization algorithms."
    - "Comprehensive performance metrics (CLV, churn rate, NPS) provide a framework for evaluating Odin's impact."
  limits:
    - "General CRM framework may not be directly tailored to the PFMS context of Filipino young professionals."
    - "Simulation results based on synthetic and anonymized data may not perfectly reflect real-world behavioral dynamics."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant for domains concerning Predictive Modeling (6.A, 6.B), Engagement and Retention (11.A, 11.B), and System Evaluation (12.A, 12.B), as it directly addresses these with machine learning and strategic KPIs. Relevance to Privacy and Trust (10.A, 10.B) was also high, given its emphasis on compliance and interpretability. The framework provides a strategic foundation for personalization in finance, aligning with Recommendation (7.B) and Anomaly Detection (8.A, 8.B) at a medium level. The paper does not significantly contribute to domains on Filipino Cultural Context (2.A-D), Expense Categorization (3.A-C), or Existing Systems (4.A-B). Overall, while not PFMS-specific, the paper's technical and strategic insights on AI-driven personalization are highly relevant to Odin's core algorithmic and retention-focused modules.
limitations:
  - "General CRM framework may not be directly tailored to the PFMS context of Filipino young professionals. [unacknowledged]"
  - "Simulation results based on synthetic and anonymized data may not perfectly reflect real-world behavioral dynamics. [unacknowledged]"
  - "The paper provides a strategic overview but lacks empirical validation specific to small-budget personal finance management systems. [unacknowledged]"
remember_this:
  - AI-driven personalization reduces churn by up to 15 percent.
  - Cross-sell conversion increases by 22 percent through targeted AI interventions.
  - Model interpretability and data privacy are non-negotiable for regulatory compliance.
  - Continuous learning pipelines are essential to adapt to shifting consumer behavior.
  - A modular architecture ensures scalable integration with legacy financial systems.
```
---

## Paper 13: Rabinovich et al_summarized.md

**Source File:** `Rabinovich et al_summarized.md`

```yaml
paper_id: "5f4e3d2c-1b0a-9f8e-7d6c-5b4a3f2e1d0c"
designation: "international-algorithm-specific"
title: "Mapping Financial Mindsets: A Two-Stage Unsupervised Framework for Behavioral Profiling Using High-Dimensional Psychometric Data"
authors: "Rabinovich, I.; Rabinovich, R.; Ashburn, N.; DeGeare, M."
year: 2026
venue: "Unknown"
odin_topics:
  - "5.A"
  - "5.B"
  - "5.C"
  - "10.B"
  - "12.A"
  - "12.B"
tldr: "A two-stage unsupervised framework combining manifold learning and spectral clustering identifies psychologically interpretable financial behavioral profiles from psychometric data."
problem_and_motivation: "Financial well-being is multidimensional, yet segmentation approaches overlook psychological traits. There is a gap in modeling interactions across psychometric domains to reveal latent financial mindsets. This limits personalized financial tools and interventions that account for behavioral heterogeneity."
approach:
  - "Stage 1 derives unidimensional domain scores via anchor-based projection, weighted averages, or simple averages depending on domain structure."
  - "Stage 2 applies UMAP to domain scores followed by spectral clustering to identify behavioral profiles."
  - "The framework is evaluated on a proprietary psychometric dataset (N=337) and the nationally representative CFPB Financial Well-Being Survey (N=5,897)."
  - "Hyperparameters are tuned via randomized search optimizing trustworthiness, continuity, silhouette score, Calinski-Harabasz index, and Davies-Bouldin index."
  - "Cluster stability is assessed via 100 random seeds and subsampling, and external validity is tested against independent outcomes."
findings:
  - "num: 79.2% accuracy achieved in assigning new individuals to learned profiles using a soft-voting classifier."
  - "num: Cluster membership explains 19-61% of variance in life satisfaction, psychological well-being, and financial health in the proprietary dataset."
  - "num: Cluster membership explains 14-44% of variance in life satisfaction, material hardship, and financial health in the CFPB dataset."
  - "Demographic variables alone provide limited predictive power for cluster membership (McFadden pseudo-R² = .061-.091)."
  - "The framework reveals interpretable, psychologically coherent profiles that are not captured by linear or demographic segmentation approaches."
key_figures_tables:
  - "Figure 1: UMAP projections show clear cluster separation in both datasets → Clusters are spatially distinct and interpretable."
  - "Figure 3: Heatmaps of mean domain scores reveal distinctive cluster-level profiles across domains → Profiles are psychologically coherent."
  - "Figure 5: Variance explained by clusters exceeds that of demographics for subjective outcomes → Profiles capture behavioral-psychological structure beyond SES."
  - "Figure 6: Cluster centroids align along a global functioning axis across datasets → Framework captures shared latent structure."
  - "Table 5a/5b: Descriptive cluster profiles range from low capability to highly resourced → Profiles reflect distinct behavioral pathways."
key_equations:
  - equation: "s_i = [(p_i - v_min^e) · (v_max^e - v_min^e)] / ||v_max^e - v_min^e||^2"
    explanation: "Orthogonal projection of participant embedding onto anchor axis for domain scoring."
  - equation: "CPSI_{i,j} = 1 / (1 + d(i,j))"
    explanation: "Normalized inverse-distance measure for cross-dataset cluster similarity."
definitions:
  - term: "UMAP"
    definition: "Uniform Manifold Approximation and Projection, a nonlinear dimensionality reduction technique."
  - term: "Spectral Clustering"
    definition: "A graph-based clustering method that uses eigenvalues of a similarity matrix."
  - term: "Anchor-based projection"
    definition: "Scoring method projecting participant embeddings onto an axis defined by theoretical anchor profiles."
  - term: "CFPB"
    definition: "Consumer Financial Protection Bureau, a U.S. government agency."
critical_citations:
  - "[Kahneman & Tversky, 1979] — Foundational for behavioral finance and non-rational decision-making."
  - "[Lusardi & Mitchell, 2011] — Provides validated financial literacy measurement items."
  - "[Ryan & Deci, 2017] — Theoretical basis for motivation domain in the proprietary dataset."
  - "[McInnes et al., 2018] — Introduces UMAP, the core dimensionality reduction method."
  - "[Ng et al., 2002] — Foundational for spectral clustering algorithm used."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "The paper's core contribution is identifying distinct financial behavioral profiles using unsupervised learning."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "high"
      justification: "Section 4.8 addresses cold-start assignment of new individuals to learned profiles using a classifier."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "The framework uses a two-stage unsupervised approach and validates classification performance."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "medium"
      justification: "Interpretable profiles can support trust by providing transparent explanations for personalization."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "The study uses internal validation metrics and external outcome associations, providing an evaluation framework."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Cluster stability is assessed via random seeds and subsampling, validating algorithmic reproducibility."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Background section reviews existing financial well-being assessments and their limitations."
    - code: "9.A"
      name: "Mobile‑First Design Principles and Rationale"
      relevance: "contextual"
      justification: "The framework is discussed as applicable to fintech platforms, but mobile-specific design is not addressed."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "contextual"
      justification: "Profiles could inform engagement strategies, but the paper does not directly study engagement dynamics."
  contribution: "This paper directly informs Odin's behavioral profiling module (5.A, 5.B, 5.C) by providing a validated two-stage unsupervised framework for identifying financial mindsets. The classifier for assigning new users to profiles supports Odin's cold-start problem (5.B). The interpretable profiles can inform personalized budget recommendations (7.B) and engagement strategies (11.A) by aligning system behavior with user psychology. The framework's validation methodology also provides a template for evaluating Odin's algorithmic modules (12.B)."
  directly_justifies:
    - "A two-stage unsupervised framework can identify psychologically interpretable financial behavioral profiles."
    - "Demographic variables alone do not substantially account for the clustering structure."
    - "Cluster membership explains more variance in financial health and life satisfaction than demographics alone."
    - "A supervised classifier can assign new users to learned profiles with 79.2% accuracy."
    - "The framework reveals shared latent structure across different instruments and populations."
  limits:
    - "Both datasets are cross-sectional, preventing assessment of profile dynamics over time."
    - "All measures are self-reported, which may introduce response biases."
    - "The proprietary dataset is modest in size and drawn from a convenience sample."
    - "The framework involves analytic design choices that can influence the resulting structure."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated canonical topic codes was performed. Domains directly related to behavioral profiling (5.A, 5.B, 5.C) were flagged as high relevance because the paper's core contribution is identifying financial behavioral profiles using unsupervised learning and addressing cold-start assignment. Domains related to system evaluation (12.A, 12.B) were assigned medium relevance due to the comprehensive validation framework used. The data privacy domain (10.A) was considered but rejected because the paper does not address privacy mechanisms. The expense categorization (3.A, 3.B, 3.C) and budget recommendation (7.A-D) domains were rejected as the paper focuses on profiling rather than categorization or optimization. The forecasting domain (6.A, 6.B) was rejected because the paper does not model spending sequences. The mobile-first design domain (9.A, 9.B) was considered contextual because the framework is discussed as applicable to fintech but mobile-specific considerations are absent. The Filipino cultural context (2.A-D) was not applicable given the U.S.-focused datasets. Overall, the paper provides strong methodological support for behavioral profiling and moderate support for evaluation frameworks, but limited direct relevance to other Odin modules."
limitations:
  - "Both datasets are cross-sectional, precluding assessment of profile dynamics over time. [unacknowledged]"
  - "All measures are self-reported, which may be influenced by response styles. [unacknowledged]"
  - "The proprietary dataset is modest in size and drawn from a convenience sample. [acknowledged]"
  - "The framework involves analytic design choices that can influence the resulting structure. [acknowledged]"
  - "The framework's generalizability to other populations and domains requires further validation. [acknowledged]"
remember_this:
  - "Two-stage framework with UMAP and spectral clustering reveals interpretable financial profiles."
  - "Cluster membership explains up to 61% of variance in financial health outcomes."
  - "Demographics alone explain only 6-9% of cluster membership variance."
  - "A classifier can assign new individuals to profiles with 79.2% accuracy."
  - "The framework captures shared latent structure across different survey instruments."
```
---

## Paper 14: Ahmed_summarized.md

**Source File:** `Ahmed_summarized.md`

```yaml
paper_id: ce4d2a9c-aec4-57f0-a6e2-9a09e3b56c2e # No DOI available
designation: international
title: AI-Driven Credit Risk Assessment in Fintech Lending: Implications for Financial Inclusion, Systemic Risk, and Regulatory Governance
authors: Ahmed, S. I.
year: 2026
venue: American International Journal of Business Management
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 4.B
  - 8.A
  - 10.A
  - 10.B
tldr: A systematic review of AI credit risk models shows they improve predictive power but introduce governance challenges in fairness, systemic stability, and regulation, addressed via a proposed five-stage governance framework.
problem_and_motivation: Fintech lending uses AI for credit assessment, offering inclusion benefits but raising unaddressed governance issues like algorithmic bias and systemic risk. Existing regulatory frameworks are fragmented and lag behind technological adoption, especially in emerging markets. A unified governance approach is needed to balance innovation with stability and equity.
approach:
  - Systematic literature review of 30 peer-reviewed articles and regulatory reports from 2012-2025.
  - PRISMA-inspired protocol used for screening and selecting the final corpus of documents.
  - Comparative model analysis conducted on performance metrics like AUC-ROC, Gini coefficient, and KS statistic.
  - Iterative framework construction method employed to develop the Integrated AI Credit Risk Framework (IACRF).
  - The IACRF operationalizes the SAFE AI principles across five stages of a fintech credit system lifecycle.
findings:
  - num: Gradient boosting models achieve AUC-ROC values of 0.83-0.91, a 7-19 percentage point improvement over logistic regression baselines.
  - num: Hybrid XAI models with SHAP achieve AUC-ROC of 0.84-0.92 while improving interpretability to meet regulatory criteria.
  - num: AI models on alternative data increase approval rates for thin-file borrowers by 20-40 percentage points in new markets.
  - Algorithmic bias arises from historical data and can be identified via XAI but requires institutional accountability for remediation.
  - Systemic risk propagates through model herding, procyclicality, and platform contagion, unaddressed by current frameworks.
  - The EU AI Act represents the most advanced regulatory model but lacks systemic risk monitoring tools.
key_figures_tables:
  - Table 1: Comparative performance of AI/ML models → Ensemble XAI models offer the best balance of performance and regulatory suitability.
  - Table 2: Financial inclusion metrics by region → Inclusion benefits are highest in emerging markets but come with high digital exclusion risk.
  - Table 3: Comparative AI credit governance frameworks → Significant governance gaps exist in emerging markets.
  - Figure 1: Conceptual architecture of IACRF → The five-stage framework integrates accuracy, fairness, stability, and ethics.
  - Figure 3: Systemic risk propagation pathways → Model herding, procyclicality, and platform contagion create systemic vulnerability.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: IACRF
    definition: Integrated AI Credit Risk Framework, a five-stage governance model for fintech lending.
  - term: SAFE AI
    definition: Principles for Statistical accuracy, Algorithmic fairness, Financial stability, and Ethical governance in AI.
  - term: XAI
    definition: Explainable Artificial Intelligence, techniques like SHAP and LIME for model interpretability.
  - term: AUC-ROC
    definition: Area Under the Receiver Operating Characteristic Curve, a measure of model predictive performance.
critical_citations:
  - "[Fan, 2025] — Reviews AI/ML classification models for credit risk performance."
  - "[Giudici & Raffinetti, 2023] — Proposes the SAFE AI framework for finance."
  - "[Berg et al., 2022] — Reviews market structure and dynamics of FinTech lending."
  - "[Billio et al., 2012] — Introduces econometric measures of systemic risk connectedness."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: Discusses AI models inferring creditworthiness from behavioral data, which is conceptually relevant to profiling user financial behavior.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: Addresses using alternative data for thin-file borrowers, analogous to cold-start profiling but not directly on personal finance management.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Reviews ML models like gradient boosting for classifying credit risk, which are similar to techniques used for behavioral profile classification.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly identifies governance gaps in current fintech lending systems, including fairness, transparency, and systemic risk oversight.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Mentions model monitoring for performance degradation and distributional shifts, which are related to anomaly detection concepts.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Discusses data governance, consent architectures, and privacy in the context of training AI models with alternative data.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Identifies algorithmic opacity and lack of explainability as direct threats to user trust and accountability in credit decisions.
  contribution: The paper's IACRF directly justifies the need for multi-level governance in Odin, covering data handling, algorithmic fairness, and systemic risk monitoring. It provides a rationale for incorporating explainability and bias auditing into Odin's recommendation and anomaly detection modules. The discussion on regulatory compliance informs Odin's design for data privacy and user trust. Its findings on performance-fairness trade-offs influence the approach to behavioral profiling and budget recommendations. The framework's emphasis on impact evaluation supports Odin's need for continuous system evaluation and improvement.
  directly_justifies:
    - "AI credit models offer performance gains but create interpretability challenges for regulatory compliance."
    - "Financial inclusion benefits of AI are constrained by digital exclusion and pricing bias risks."
    - "Systemic risk from AI lending propagates via model herding and procyclicality."
    - "Regulatory frameworks are fragmented, with emerging markets facing the largest governance gaps."
  limits:
    - "Literature-based synthesis limits causal inference and may suffer from publication bias."
    - "IACRF is theoretical and requires empirical validation in real fintech settings."
    - "Rapid regulatory changes may render some jurisdictional analyses outdated quickly."
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The paper was flagged as relevant primarily to the "Existing Systems & Gaps" and "Data Privacy & User Trust" domains due to its thorough analysis of limitations in current fintech lending systems and governance challenges related to fairness and opacity. It also touches on "Behavioral Profiling" (topic 5.A) and "Classification" (topic 5.C) because it reviews ML models used to infer borrower risk from behavioral data, but these are not the core focus. The paper was considered and rejected for domains like "Expense Categorization," "Spending Forecasting," and "Budget Recommendation," as it does not address personal finance management or budget allocation. Similarly, it was deemed non-relevant for "Mobile-First Design," "User Retention," and "Savings & Debt Management" as it focuses on institutional lending, not individual financial health management. Overall, the paper provides strong contextual and supporting evidence for Odin's design concerning system limitations, fairness, and trust but is not directly algorithmic for spending forecasting or recommendation.
limitations:
  - "The study relies on published literature, which may not capture unpublished industry practices and may be subject to publication bias."
  - "The IACRF is a theoretical framework that has not yet been empirically tested in operational fintech environments. [unacknowledged]"
  - "The rapid evolution of AI governance regulations means some specific jurisdictional references may become outdated. [unacknowledged]"
remember_this:
  - "AI credit models improve predictive accuracy but introduce significant governance challenges."
  - "Financial inclusion from AI lending is countered by risks of digital exclusion and over-indebtedness."
  - "Systemic risk arises from model herding, procyclicality, and platform interconnectedness."
  - "Regulatory governance for AI in lending is fragmented, with emerging markets least protected."
  - "The IACRF integrates fairness and systemic stability into a five-stage governance lifecycle."
```
---

## Paper 15: Wei et al_summarized.md

**Source File:** `Wei et al_summarized.md`

```yaml
paper_id: "arXiv:2506.21812v1"
designation: "international-algorithm-specific"
title: "Bridging the Cold-Start Gap: LLM-Powered Synthetic Data Generation for Natural Language Search at Airbnb"
authors: "Wei, W.R.; Li, H.; Guo, W.W.; Liu, X.W.; Chen, X.Y.; Davis, D.; Haldar, M.; Banerjee, S.; Bellare, K.; Gao, H.; Moyerman, S.; Katariya, S."
year: 2026
venue: "arXiv"
odin_topics:
  - "4.B"
  - "5.B"
  - "5.C"
  - "12.A"
  - "12.B"
tldr: "A framework generates synthetic search queries and relevance labels using LLMs, combining contrastive listing pairs and seed queries to bridge the cold-start gap for natural language search at Airbnb."
problem_and_motivation: "Launching natural language search without historical user queries or relevance labels creates a cold-start challenge. Existing rule-based methods cannot capture nuanced intent, and human labeling is expensive and slow. There is a need for scalable and realistic synthetic data to bootstrap model training."
approach:
  - "Uses contrastive listing pairs from booking sessions and seed queries from user research to ground queries in real platform features and linguistic patterns."
  - "Develops three prompt variants: template-based (seed_controlled), few-shot (seed_freeform), and variety generation to balance realism and diversity."
  - "Generates synthetic queries via LLM conditioned on listing attributes and seed templates, producing labeled triplets (query, positive listing, negative listing)."
  - "Introduces Virtual Judge labeling using LLMs for broader relevance coverage beyond contrastive generation."
  - "Evaluates generated data against baseline without seed data using KL divergence on query length and attribute distributions, and pairwise accuracy for retrieval and ranking."
findings:
  - "num: Seed-guided approach reduces KL divergence for query length from 4.95 (baseline) to 0.66, a 7.5× improvement."
  - "num: Our approach achieves the lowest attribute type KL divergence (0.04) compared to baseline (0.13) and seed queries (0.09)."
  - "num: Our approach produces harder evaluation examples, with retrieval accuracy dropping from 0.967 (baseline) to 0.790 (our approach) for Qwen3."
  - "num: The pipeline generates approximately 10,000 synthetic queries daily in production."
  - "Seed-controlled prompt variant best matches real user attribute distributions, while variety best matches length distributions."
key_figures_tables:
  - "Figure 1: Contrastive query generation pipeline → illustrates data sources, sampling, and LLM processing steps."
  - "Figure 2: Example of baseline vs. our approach → shows seed guidance produces terse natural queries vs verbose baseline."
  - "Table 1: Comparison of query generation approaches → highlights realism of seed-guided generation."
  - "Table 2: Comparison of query characteristics across datasets → shows KL divergence improvements and distribution alignment."
  - "Table 3: Attribute type distribution comparison → demonstrates lowest KL divergence for attribute types."
key_equations:
  - equation: "D_KL(P_true || P_synth) = ∑ P_true(q) log(P_true(q)/P_synth(q))"
    explanation: "Measures divergence between true and synthetic query distributions."
  - equation: "P_synth(q) = E_{t~P(t), e~P(e)} [P_LLM(q|t,e)]"
    explanation: "Synthetic query distribution as expectation over templates and entities."
definitions:
  - term: "LLM"
    definition: "Large language model."
  - term: "KL divergence"
    definition: "Measure of difference between two probability distributions."
  - term: "Contrastive generation"
    definition: "Generating queries where one listing is more relevant than another by construction."
  - term: "Virtual Judge"
    definition: "Using LLM to evaluate relevance of query-listing pairs."
  - term: "Topicality"
    definition: "Relevance of a listing to the query's stated intent, independent of booking likelihood."
critical_citations:
  - "[Bonifacio et al., 2022] — InPars: data augmentation for IR using LLMs."
  - "[Dai et al., 2023] — Promptagator: few-shot dense retrieval."
  - "[Liu et al., 2023] — G-Eval: LLM-as-a-judge for NLG evaluation."
  - "[Zheng et al., 2023] — LLM-as-a-judge benchmark for evaluation."
relevance:
  topics:
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Paper critiques rule-based and human-labeling methods, highlighting their limitations."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "high"
      justification: "Directly addresses cold-start by generating synthetic data to bootstrap model training."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "low"
      justification: "Uses LLM-generated labels for relevance classification, analogous to profiling classification."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "contextual"
      justification: "Provides evaluation metrics like KL divergence and pairwise accuracy for synthetic data quality."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Evaluates retrieval and ranking models trained on synthetic data, offering a methodology for module assessment."
  contribution: "This paper provides a method for generating synthetic data to address cold-start profiling, which can be adapted to Odin's behavioral profiling module (5.B). Its evaluation metrics, such as KL divergence and pairwise accuracy, offer a framework for assessing synthetic data quality (12.A). The contrastive learning approach for generating relevance labels can inform Odin's classification module (5.C). The paper also highlights limitations of rule-based and human-labeling methods, motivating Odin's need for scalable data generation (4.B). The production pipeline demonstrates daily refresh and cold-to-warm transition, relevant to Odin's system deployment."
  directly_justifies:
    - "Synthetic data can bootstrap training without real user data, addressing cold-start."
    - "Seed-guided generation produces more realistic queries than unguided generation."
    - "Harder evaluation examples provide better discriminative signal for model improvement."
    - "LLM-generated synthetic data can be produced at scale for production systems."
  limits:
    - "Synthetic-real distribution shift remains; models may need adaptation post-launch."
    - "LLM self-preference bias may affect Virtual Judge labeling."
    - "Assumption of independence between templates and entities may not hold."
  mapping_rationale: "A systematic scan across all 12 functional domains and associated topic codes was performed. Only domains related to cold-start, system evaluation, and classification were flagged: 5.B (high) for directly addressing cold-start via synthetic data, 4.B (medium) for critiquing existing limitations, 12.B (medium) for evaluating algorithmic modules, 12.A (contextual) for evaluation frameworks, and 5.C (low) for classification parallels. Borderline cases: the paper's focus on search cold-start is analogous to behavioral profiling; its evaluation metrics are transferable to system evaluation. Domains such as Filipino cultural context, expense categorization, forecasting, anomaly detection, mobile design, privacy, retention, and savings/debt were rejected as unrelated. Overall, the paper provides moderate-to-high relevance for cold-start data generation and evaluation."
limitations:
  - "The framework assumes independence between templates and entities, which may not hold."
  - "Distribution shift between synthetic and real queries is inherent; models may require adaptation."
  - "LLM self-preference bias may affect Virtual Judge labeling."
  - "Transition from topicality to bookability is not addressed and requires future work."
remember_this:
  - "Seed guidance reduces KL divergence for query length by 7.5×."
  - "Combining contrastive generation with seed queries yields the most realistic attribute distributions."
  - "Synthetic data serves as a bridge from cold start to warm start as real data accumulates."
  - "Harder evaluation examples provide better discriminative signal than easy baselines."
```
---

## Paper 16: Ng et al_summarized.md

**Source File:** `Ng et al_summarized.md`

```yaml
paper_id: "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d"
designation: "local-algorithm-specific"
title: "AI-BAAM: AI-Driven Bank Statement Analytics as Alternative Data for Malaysian MSME Credit Scoring"
authors: "Ng, C. C.; Chu, Z. H.; Lim, J. Y.; Boon, Y. Y.; Low, W. Z.; Tan, J. K."
year: 2026
venue: "ICLR 2026"
odin_topics:
  - "3.A"
  - "4.A"
  - "4.B"
  - "5.A"
  - "5.B"
  - "5.C"
  - "6.A"
  - "10.A"
  - "12.A"
  - "12.B"
  - "13.B"
tldr: "Bank statement transaction data substantially improves MSME credit scoring in Malaysia, with a blended logistic regression model achieving AUROC 0.806, a 24.6% gain over application-only models."
problem_and_motivation: "Traditional credit scoring relies on credit bureau data, excluding MSMEs with thin credit files and creating a MYR90 billion funding gap in Malaysia. Real-time cash flow signals and alternative indicators are overlooked, limiting financial inclusion. There is a need for verifiable, up-to-date financial data to assess creditworthiness for underserved MSMEs."
approach:
  - "Proposes an end-to-end cash flow underwriting workflow with six modules: OCR-based key information and transaction extraction, fraud detection, network analysis, cash flow analysis, and credit scoring."
  - "Constructs the first Malaysian bank statement dataset of 611 MSME loan applicants, with 518 non-default and 93 default cases, split 60/40 for training/validation."
  - "Benchmarks Logistic Regression, Random Forest, Gradient Boosting, and AdaBoost using application information and bank statement-derived features (account behavior and business demographics)."
  - "Uses WOE/IV framework for feature transformation and supervised monotonic binning to handle class imbalance and ensure interpretability."
  - "Evaluates over 30 OCR and LLM configurations for key information and transaction table extraction across six Malaysian banks, comparing with template matching."
  - "Applies CRISP-DM methodology for systematic data mining and model development."
findings:
  - "num: Blended Logistic Regression achieves validation AUROC of 0.806, a 24.6% relative improvement over application-only models."
  - "num: Bank statement features alone yield validation AUROC of 0.763, while application-only yields 0.647."
  - "num: Log growth rate of average balance has the highest IV of 0.484, outperforming the top application feature (business duration, IV 0.213)."
  - "num: Template matching achieves 100% exact match accuracy on key information fields and 98.08% matching NED on transaction tables, with zero API cost and sub-second latency (0.01s key info, 0.11s table)."
  - "num: Rejected applicant analysis shows 96.97% classified as high risk, validating alignment with original underwriting decisions."
key_figures_tables:
  - "Figure 1: Proposed end-to-end workflow for credit scoring using bank statement data → workflow comprises six modules from extraction to scoring."
  - "Figure 2: AUROC across algorithms and feature sets → blended features consistently outperform application-only and bank-only, with LR best at 0.806."
  - "Figure 3: Information Value of features → bank statement features dominate top positions, with log growth rate of average balance highest."
  - "Table 1: Dataset statistics showing 611 applicants with 15.2% default rate → stratified split preserves class distribution."
  - "Table 2: Summary of extraction performance, latency, and cost → template matching achieves best accuracy-efficiency trade-off."
key_equations:
  - equation: "WOE_{jk} = log( (n_{gjk}/N_g) / (n_{bjk}/N_b) )"
    explanation: "Measures relative risk of feature bin jk; positive indicates lower default risk."
  - equation: "IV_j = sum_{k=1}^{K_j} (Dist(g)_{jk} - Dist(b)_{jk}) * WOE_{jk}"
    explanation: "Summarizes predictive power of feature j; higher IV means stronger discrimination."
  - equation: "P(y_i=1|x_i;β) = σ(β_0 + x_i^T β)"
    explanation: "Logistic regression models default probability as sigmoid of linear combination."
definitions:
  - term: "AUROC"
    definition: "Area Under the Receiver Operating Characteristic Curve, measures discrimination ability (0.5 random, 1 perfect)."
  - term: "MSME"
    definition: "Micro, Small, and Medium Enterprises, backbone of Malaysian economy."
  - term: "OCR"
    definition: "Optical Character Recognition, extracts text from images/PDFs."
  - term: "IV"
    definition: "Information Value, quantifies predictive strength of a feature in credit scoring."
  - term: "WOE"
    definition: "Weight of Evidence, log-odds transformation of feature bins for logistic regression."
  - term: "NED"
    definition: "Normalized Edit Distance, measures string similarity (1 perfect match)."
critical_citations:
  - "[Breiman, 2001] — Introduced Random Forest used as ensemble baseline."
  - "[Friedman, 2001] — Gradient Boosting baseline."
  - "[Bunker et al., 2016] — Showed bank statement features improve credit scoring."
  - "[Lessmann et al., 2015] — Benchmarking classification algorithms for credit scoring."
relevance:
  topics:
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "medium"
      justification: "Paper uses NLP to classify transaction descriptions into categories, relevant for expense tracking."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Reviews traditional credit scoring and alternative data, but not PFMS landscape."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Directly identifies shortcomings of bureau-based credit scoring for thin-file MSMEs."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Derives behavioral features from transaction data to profile credit risk."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "high"
      justification: "Addresses cold-start for MSMEs lacking credit history; uses bank statements as alternative."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Compares Logistic Regression, Random Forest, Gradient Boosting, AdaBoost for default classification."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Builds predictive models for default probability using transaction-derived features."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "Discusses data masking, anonymization, compliance with Malaysia's PDPA."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "low"
      justification: "Evaluates model performance via AUROC but not specifically PFMS evaluation frameworks."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Thoroughly evaluates OCR extraction and credit scoring models with multiple metrics."
    - code: "13.B"
      name: "Debt Management in PFMS"
      relevance: "medium"
      justification: "Assesses default risk and repayment capacity, relevant to debt management."
  contribution: "This paper provides a validated approach for transaction categorization (module 3.A) and behavioral profiling (5.A) using bank statement data, which can be adapted for Odin's expense tracking and user profiling. Its evaluation of cold-start strategies (5.B) informs Odin's handling of new users with limited history. The privacy-preserving data handling practices (10.A) align with Odin's requirements for user trust. The benchmarking of algorithmic modules (12.B) offers a template for evaluating Odin's machine learning components."
  directly_justifies:
    - "Bank statement transaction data improves default prediction by 24.6% over application-only data."
    - "Transaction-derived features have higher discriminatory power than static application information."
    - "Template matching outperforms LLM-based extraction for structured financial documents in terms of accuracy, latency, and cost."
    - "Rejected applicant analysis validates that bank statement features capture genuine credit risk signals."
  limits:
    - "Dataset is limited to 611 applications from a single Malaysian consulting firm, potentially limiting generalizability."
    - "Class imbalance (15.2% default) reflects real-world lending but may affect minority class prediction."
    - "Module-level evaluation is constrained by proprietary methods; only overall scoring performance is reported."
    - "Validation across different institutions and economic cycles is needed."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was found highly relevant to the following domains: Expense Categorization (3.A) due to its transaction classification, Limitations of Existing Systems (4.B) for its critique of bureau-based scoring, Behavioral Profiling and Classification (5.A, 5.B, 5.C) for deriving and modeling behavioral features, Predictive Modeling (6.A) for default prediction, Data Privacy (10.A) for ethical handling, and Evaluation of Algorithmic Modules (12.B) for extensive benchmarking. Domains related to budgeting (7.A-D), mobile-first design (9.A-B), and engagement (11.A-B) were considered but rejected as the paper focuses on credit scoring rather than PFMS features. Seasonal spending (2.B, 2.D) and savings goals (13.A, 13.C) were also not addressed. The paper provides strong justification for using transaction data to address cold-start issues and improve predictive accuracy, with moderate relevance to debt management (13.B). Overall, the paper offers actionable insights for Odin's core modules in behavioral modeling and evaluation, while its privacy practices and rejection analysis provide supporting evidence for trust and robustness."
limitations:
  - "Dataset size is limited (611 applicants) from a single institution."
  - "Class imbalance is inherent but not addressed with resampling techniques."
  - "Module-level assessment is constrained by proprietary methods; only overall scoring performance is reported."
  - "Generalizability across different banks and regions is not tested."
  - "Focus on credit scoring rather than full PFMS features like savings goals or budgeting. [unacknowledged]"
remember_this:
  - "Blended bank statement and application features yield AUROC 0.806, 24.6% gain over application-only."
  - "Bank statement features dominate predictive power, with log growth of average balance IV 0.484."
  - "Template matching outperforms LLM-based extraction with 100% accuracy and zero cost."
  - "Transaction data provides strong signals for cold-start credit assessment of thin-file MSMEs."
  - "Privacy-preserving data handling is critical for adoption in financial systems."
```
---

## Paper 17: Balbal & Birant_summarized.md

**Source File:** `Balbal & Birant_summarized.md`

```yaml
paper_id: 10.3390/app16052223
designation: international-algorithm-specific
title: RFM-Net: A Convolutional Neural Network for Customer Segment Classification
authors: Balbal, K.F.; Birant, D.
year: 2026
venue: Applied Sciences
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 12.A
  - 12.B
tldr: Integrates RFM analysis with a custom CNN to classify customers into predefined behavioral segments using structured transactional data.
problem_and_motivation: Traditional RFM-based segmentation relies on rule-based logic that may not capture nonlinear patterns in customer behavior. Existing statistical and clustering approaches often lack the adaptability required for dynamic markets. There is a need for a robust, intelligent, and scalable technique that combines domain knowledge with data-driven learning.
approach:
  - Uses the UCI Online Retail dataset with 541,909 records from a UK-based retailer.
  - Transforms raw transactional data into Recency, Frequency, and Monetary (RFM) features.
  - Discretizes continuous RFM values into 1-5 scores using user-defined thresholds.
  - Applies a rule-based scheme to label customers into seven segments (e.g., Champions, At Risk) using RFM scores.
  - Trains a custom, lightweight CNN (RFM-Net) on the labeled data to learn the mapping from RFM values to segments.
  - Evaluates model performance using 10-fold cross-validation and metrics like accuracy, precision, recall, and F-measure.
findings:
  - num: The proposed RFM-Net achieved a classification accuracy of 94.33% on the test set.
  - num: RFM-Net demonstrated a relative average increase of 13.17% in accuracy compared to previous studies on the same dataset.
  - Recency was identified as the most important feature for prediction, followed by Frequency and Monetary.
  - The lightweight CNN architecture with only 6,823 parameters proved efficient and prevented overfitting.
  - Model performance was consistent across two different retail datasets (Online Retail I and II), showing robustness.
key_figures_tables:
  - Table 7: Performance metrics across 10 folds → Average accuracy of 94.33% with high precision and recall.
  - Figure 3: Distribution of customer segments → Potential Loyalists form the largest group (23.70%).
  - Figure 4: Feature importance analysis → Recency is the most significant predictor of customer segment.
  - Figure 5: Confusion matrix → High classification accuracy for most segments, with minor confusion between adjacent groups.
  - Figure 6: Training and validation loss → Loss curves converge, indicating effective learning and generalization.
key_equations:
  - equation: R_c = (d_ref - d_last^c).days
    explanation: Calculates days since customer's last purchase.
  - equation: F_c = | {x.InvoiceNo | ∀x ∈ T_c } |
    explanation: Counts distinct purchase events per customer.
  - equation: M_c = ∑_{x∈T_c} (x.Quantity × x.UnitPrice)
    explanation: Sums total spending per customer.
definitions:
  - term: RFM
    definition: Recency, Frequency, and Monetary; a framework for customer behavior analysis.
  - term: CNN
    definition: Convolutional Neural Network; a deep learning model for feature extraction.
  - term: RFM-Net
    definition: Proposed CNN model designed for customer segmentation using RFM features.
  - term: Champions
    definition: Most active and profitable customers with high R, F, and M scores.
critical_citations:
  - "[Christy et al., 2021] — Introduces RFM ranking for customer segmentation."
  - "[Chen et al., 2012] — Source of the UCI Online Retail dataset used in the study."
  - "[Talaat et al., 2023] — Previous work on RFM and deep learning for segmentation."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: The paper's core task is classifying customers into behavioral profiles (e.g., Champions, At Risk).
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: contextual
      justification: While not explicitly on cold-start, the method uses rule-based labels, indirectly addressing the challenge of initial profile creation.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: The paper proposes a novel classification approach (CNN) for financial behavioral profiles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Customer segment prediction is a form of predictive modeling applicable to spending behavior.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: contextual
      justification: The RFM features are derived from sequential transaction data, though the paper focuses on classification rather than forecasting.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: The paper uses standard metrics (accuracy, precision, recall) applicable to evaluating system modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: The paper provides a detailed evaluation of the proposed RFM-Net algorithm against baseline models.
  contribution: "RFM-Net provides a methodological template for classifying users into strategic behavioral segments using only RFM features, which can be integrated into Odin's behavioral profiling engine. The high accuracy of the model (94.33%) justifies the use of supervised learning for personal finance categorization tasks where ground-truth labels are derived from expert-defined rules. The lightweight CNN architecture demonstrates that effective segmentation is possible with minimal computational resources, supporting Odin's mobile-first design principle. The feature importance analysis, showing Recency as the strongest predictor, guides the design of Odin's engagement and retention features."
  directly_justifies:
    - "A lightweight CNN can achieve high accuracy (94.33%) for segmenting users based on RFM features."
    - "Recency is the most important behavioral indicator for predicting future engagement."
    - "Supervised learning can effectively learn expert-defined segmentation rules from structured financial data."
    - "The CNN architecture acts as an implicit regularizer, improving generalization on tabular data."
  limits:
    - "The study relies on predefined thresholds for discretizing RFM values, which may not be optimal for all user populations."
    - "The model was evaluated on retail transaction data, not on personal finance management logs, so generalizability to Odin's context is not directly established."
    - "The labels are derived from the same RFM scores used as features, introducing a degree of circularity in the modeling process."
  mapping_rationale: "The systematic scan across Odin's 12 functional domains flagged three domains as highly relevant: Behavioral Profiling & Classification (Topic 5), Spending Forecasting (Topic 6), and System Evaluation (Topic 12). The paper's central contribution—a CNN model for customer segmentation—directly informs Topics 5.A, 5.B, and 5.C, with 'high' relevance assigned due to its novel classification approach for behavioral profiles. Topic 6 (Predictive Modeling & Forecasting) was considered relevant but only at a 'medium' or 'contextual' level, as the paper focuses on classification rather than sequence forecasting, though its RFM features derive from temporal data. Topic 12 (System Evaluation) received 'high' relevance for its evaluation framework and 'medium' for its comparison against baselines. Domains like Filipino Cultural Context (2), Expense Categorization (3), Mobile-First Design (9), and Data Privacy (10) were considered and rejected, as the paper does not address cultural practices, categorization taxonomies, mobile constraints, or privacy concerns. The paper's overall relevance to Odin is significant for its behavioral modeling and classification methodologies, offering a computationally efficient approach to segmenting users based on spending patterns."
limitations:
  - "Circularity: Segment labels are derived from the same RFM scores that serve as model input. [unacknowledged]"
  - "Threshold generalizability: The optimal RFM thresholds were empirically determined for the specific retail dataset and may not generalize to other domains or user populations. [unacknowledged]"
  - "Domain gap: The dataset is from a retail e-commerce context, which may not fully represent the complexities of personal financial management. [unacknowledged]"
  - "Interpretability: The 'black box' nature of the CNN may present challenges for explaining model decisions to end-users, despite being more interpretable than deeper networks. [unacknowledged]"
remember_this:
  - The RFM-Net achieves 94.33% accuracy in customer classification.
  - Recency is the most important feature for segment prediction.
  - A lightweight CNN prevents overfitting on low-dimensional data.
  - Rule-based labeling enables supervised learning of behavioral profiles.
  - The model performs effectively on structured, tabular data.
```
---

## Paper 18: Han & Lai_summarized.md

**Source File:** `Han & Lai_summarized.md`

```yaml
paper_id: 10.69987/JACS.2026.60403
designation: international-algorithm-specific
title: Temporal Feature Engineering and Threshold Optimization for Early Warning in Healthcare Claims Anomaly Detection
authors: Han, M.; Lai, J.
year: 2026
venue: Journal of Advanced Computing Systems
odin_topics:
  - 6.B
  - 8.B
  - 12.A
  - 10.A
  - 9.A
tldr: Systematic temporal feature engineering and adaptive threshold optimization significantly improve early-warning anomaly detection in healthcare claims.
problem_and_motivation: Healthcare fraud causes massive financial losses, but existing detection methods often miss subtle temporal patterns or generate excessive false alarms. The temporal dimension of claims data remains underutilized, limiting early warning capabilities.
approach:
  - This paper develops a framework to extract 127 temporal features from Medicare Part B claims, including service intervals, submission patterns, and frequency distributions.
  - Feature construction combines statistical analysis, functional principal component analysis, and LSTM autoencoder embeddings to capture multi-scale temporal dependencies.
  - The paper proposes an adaptive threshold optimization methodology that dynamically adjusts detection boundaries based on performance feedback and concept drift.
  - The approach is evaluated on a dataset with 47.3 million claims from 892,450 providers, comparing against baseline statistical and RFM features.
  - The framework includes cost-sensitive optimization, Pareto frontier analysis, and context-aware adjustments for seasonal and specialty variations.
findings:
  - num: The proposed framework achieved a detection rate of 0.87 and false positive rate of 0.06, improving over baseline rates of 0.73 and 0.14.
  - num: The adaptive threshold framework outperformed static approaches, maintaining stable performance (detection rate variation within 0.03) over 12 months.
  - num: The cost-benefit analysis identified an optimal threshold at 0.60, generating net annual savings of 8.2 million dollars in the study's setting.
  - Service-to-submission lag standard deviation and weekend submission ratio were the most important temporal features for fraud detection.
  - LSTM autoencoder embeddings provided a 0.06 improvement in detection rate over statistical features alone.
  - The adaptive framework responded to concept drift with an average latency of 8.3 days, preventing performance degradation seen in fixed thresholds.
key_figures_tables:
  - Figure 1: Temporal billing frequency distributions for legitimate, early-stage, and sophisticated fraud providers → Fraud patterns show distinct frequency spikes and periodicities.
  - Figure 2: LSTM autoencoder embedding space visualization → Fraudulent providers cluster at the periphery, distinct from legitimate providers.
  - Figure 3: Threshold performance trade-off curves → Optimal cost-savings balance occurs at threshold 0.60 with 79% detection rate and 3% false positive rate.
  - Figure 4: Adaptive threshold evolution and performance tracking → Dynamic adjustments maintain performance within acceptable ranges across drift events.
  - Table 7: Cost-benefit analysis for threshold selection → Threshold 0.60 yields the highest net benefit at 315.6 million dollars.
key_equations:
  - equation: D_KL(P||Q) = Σ P(x)·log(P(x)/Q(x))
    explanation: KL divergence measures difference between provider and reference temporal distributions.
  - equation: EWMA_t = α·x_t + (1-α)·EWMA_{t-1}
    explanation: Exponentially weighted moving average emphasizes recent billing patterns.
definitions:
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network for sequential data.
  - term: FPCA
    definition: Functional Principal Component Analysis, for capturing dominant modes of temporal variation.
  - term: ROC
    definition: Receiver Operating Characteristic, a curve showing detection trade-offs.
  - term: RFM
    definition: Recency-Frequency-Monetary features, measuring recent activity and spending.
  - term: CMS
    definition: Centers for Medicare & Medicaid Services, the US federal agency.
critical_citations:
  - "[Ahmed et al., 2016] — Survey of temporal anomaly detection methods."
  - "[Malhotra et al., 2015] — LSTM networks for time-series anomaly detection."
  - "[Bauder & Khoshgoftaar, 2023] — Cost-sensitive learning for insurance fraud."
relevance:
  topics:
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: This paper evaluates forecasting-relevant temporal modeling techniques like LSTM for anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Core contribution is an anomaly detection framework for temporal claims data, directly applicable to spending patterns.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides a rigorous evaluation methodology with cost-benefit analysis and ROC curves.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Discusses de-identified data use but does not focus on privacy-preserving techniques.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: contextual
      justification: Mentions real-time processing but does not address mobile-specific design.
  contribution: This paper's temporal feature engineering framework can inform Odin's anomaly detection module by providing a methodology for extracting patterns from sequential spending data. The adaptive threshold optimization approach offers a strategy for Odin to balance detection sensitivity with user alert fatigue. The cost-sensitive evaluation framework provides a template for assessing the financial impact of Odin's recommendations. The importance of features like service intervals and frequency distributions can guide the selection of attributes for Odin's behavioral profiling. The concept drift handling methods are relevant for Odin's adaptation to changing user spending habits over time.
  directly_justifies:
    - "Temporal features like service-to-submission lag are critical for identifying anomalous patterns in sequential data."
    - "Adaptive thresholding based on performance feedback improves detection stability over time."
    - "Cost-benefit analysis is essential for optimizing alert thresholds in resource-constrained settings."
    - "LSTM-based embeddings can capture complex dependencies in spending sequences."
  limits:
    - "The evaluation is limited to Medicare Part B fee-for-service data and may not generalize to other payment models."
    - "The fraud labels depend on completed investigations, introducing a temporal lag that may affect early warning evaluation."
    - "The ground-truth labels may reflect enforcement priorities and could miss novel fraud schemes."
  mapping_rationale: This paper was systematically scanned against all 12 functional domains and their associated topic codes. The core contribution on anomaly detection algorithms (8.B) and forecasting algorithms (6.B) was flagged as high relevance, as the paper directly addresses predictive modeling for sequential claims data. The evaluation framework (12.A) was assigned medium relevance, as the paper provides rigorous performance and cost-benefit analysis methods. Data privacy (10.A) was considered low relevance, as the paper uses de-identified data but does not focus on privacy techniques. Mobile-first design (9.A) was flagged as contextual only, as the paper mentions real-time processing but does not address mobile UX. Other domains like Filipino cultural context, expense categorization, and savings/debt management were rejected as not applicable. The paper's overall relevance to Odin is moderate: its methodological contributions on temporal feature engineering and adaptive thresholding for anomaly detection are directly transferable to Odin's core modules, but the specific domain context differs.
limitations:
  - "The evaluation relies on a single payer's (Medicare) claims data and may not generalize to other contexts."
  - "The ground-truth fraud labels introduce temporal lag and selection bias. [unacknowledged]"
  - "Computational requirements for deep learning features may limit accessibility for smaller organizations. [unacknowledged]"
  - "Threshold optimization assumes stable cost parameters which may vary in practice. [unacknowledged]"
  - "Interpretability of deep learning representations remains challenging. [unacknowledged]"
remember_this:
  - "Temporal features significantly improve anomaly detection over baseline methods."
  - "Adaptive thresholds maintain stable performance under concept drift."
  - "Feature importance analysis identifies submission lag as the most critical signal."
  - "Cost-benefit analysis is crucial for practical threshold selection."
  - "num: The framework improved detection rate by 0.14 over baseline approaches."
```
---

## Paper 19: Cerqueira et al_summarized.md

**Source File:** `Cerqueira et al_summarized.md`

```yaml
paper_id: 10.1145/3770855.3819070
designation: international-algorithm-specific
title: A Framework for Evaluating and Benchmarking Concept Drift Detection Methods
authors: Cerqueira, V.; Gomes, H. M.; Heyden, M.; Pfahringer, B.; Bifet, A.
year: 2026
venue: Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '26)
odin_topics:
  - 6.B
  - 8.B
  - 12.A
  - 12.B
tldr: A benchmarking framework for concept drift detectors with a drift simulation method, timing-aware metrics, and a leave-one-dataset-out hyperparameter optimization protocol.
problem_and_motivation: Evaluating concept drift detectors is hindered by inconsistent practices and a lack of ground truth in real-world data. This makes fair comparisons and reliable performance assessments difficult, limiting progress in the field.
approach:
  - A Monte Carlo drift simulation injects controlled distribution changes into real-world datasets, enabling supervised evaluation while preserving data complexity.
  - New timing-aware metrics are introduced, including an F1 detection score and normalized detection time, for comparable evaluation across streams.
  - A leave-one-dataset-out cross-validation protocol is advocated for robust hyperparameter optimization of drift detectors.
  - Fourteen widely used drift detection methods are benchmarked on seven real-world datasets.
  - Four drift types were simulated (class prior, label swap, feature permutation, feature filtering), each with abrupt and gradual transitions.
findings:
  - num: SEED and STEPD consistently outperform other detectors across distinct drift types.
  - num: Hyperparameter optimization using the proposed approach significantly improves detection performance over default configurations.
  - num: Abrupt drifts are generally easier to detect than gradual drifts.
  - Unsupervised detectors perform better on feature-space drifts than on label-based changes.
  - SEED achieves the best F1 rank while maintaining a moderate false alarm rate.
key_figures_tables:
  - "Table 1: Average rank of drift detectors for abrupt drifts → SEED and STEPD are top performers across most drift types."
  - "Table 2: Average rank of drift detectors for gradual drifts → SEED and STEPD maintain top performance, though with degradation."
  - "Figure 3: Distribution of F1 scores for abrupt vs gradual drifts → Gradual drifts are systematically harder to detect."
  - "Figure 4: Trade-off between F1 and False Alarm Rate → SEED is the most balanced; ABCD minimizes false alarms."
  - "Figure 5: Impact of hyperparameter optimization → Optimization improves median F1 scores for most detectors."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: Concept Drift
    definition: A change in the underlying data distribution over time, which can degrade model performance.
  - term: Abrupt Drift
    definition: A sudden, instantaneous shift from one concept to another.
  - term: Gradual Drift
    definition: A transition where two distinct concepts coexist during a period, with observations increasingly drawn from the new concept.
critical_citations:
  - "[Gama et al., 2014] — Comprehensive survey on concept drift adaptation."
  - "[Bifet, 2017] — Critiques the illusion of progress in drift detection evaluation."
  - "[Baena-García et al., 2006] — Introduces the Early Drift Detection Method (EDDM)."
  - "[Bifet and Gavalda, 2007] — Presents ADWIN, an adaptive windowing method."
relevance:
  topics:
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: contextual
      justification: Provides a framework for evaluating forecasting algorithm performance under changing data distributions.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: Offers a systematic way to evaluate anomaly detectors, which is a related problem to drift detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Directly proposes a novel framework for evaluating drift detectors, applicable to evaluating PFMS modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides a standardized protocol and metrics for evaluating algorithmic modules like drift detectors.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: low
      justification: While not directly about budgets, the evaluation principles (e.g., hyperparameter tuning) are transferable.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies inconsistencies in evaluation practices as a key gap in the field of drift detection.
  contribution: The proposed framework provides a methodology for rigorously evaluating algorithmic modules within Odin, such as anomaly detection and forecasting components. Its drift simulation method can be adapted to create realistic spending data shifts for testing system robustness. The evaluation metrics and hyperparameter optimization protocol ensure that performance claims for Odin's modules are reliable and not overfitted to specific datasets. This establishes a standard for how Odin's performance should be measured and compared against alternatives.
  directly_justifies:
    - "Evaluating drift detectors requires a simulation method that preserves real-world data complexity."
    - "Timing-aware metrics are necessary for fair comparison across datasets with different stream lengths."
    - "Hyperparameter optimization should be conducted on data distinct from the evaluation data to avoid overfitting."
  limits:
    - "The experiments are limited to one classifier (Hoeffding Tree) and four drift types."
    - "The framework assumes immediate feedback in a prequential setting, which may not hold in all PFMS contexts."
    - "The data streams are shuffled, removing pre-existing temporal dependencies."
  mapping_rationale: A systematic scan was performed across all 12 functional domains and their associated canonical topic codes. Domains related to system evaluation (12.A, 12.B, 12.C) were flagged as highly relevant because the paper's core contribution is a methodological framework for benchmarking. Domains concerning forecasting algorithms (6.B) and anomaly detection (8.B) were deemed contextual as the paper provides a framework applicable to evaluating such modules. Domain 4.B (Limitations and Gaps) was considered medium relevance as the paper explicitly addresses inconsistencies in current evaluation practices. Other domains (e.g., 1.A, 2.A, 3.A, 7.A, 9.A, 10.A, 11.A, 13.A) were rejected as they are outside the paper's scope of evaluating algorithmic performance. Overall, the paper is highly relevant to establishing robust evaluation standards for Odin's algorithmic modules.
limitations:
  - "The evaluation framework uses a single classifier (Hoeffding Tree), which may not represent all model types. [unacknowledged]"
  - "The approach assumes immediate label availability, which is unrealistic in many personal finance contexts. [unacknowledged]"
  - "Shuffling the data streams removes pre-existing temporal structures, limiting the generalizability to real-world sequential data. [acknowledged]"
  - "The experiments are limited to four simulated drift types, potentially missing other real-world distribution changes. [acknowledged]"
remember_this:
  - "SEED and STEPD show the most consistent performance across all drift scenarios."
  - "A standardized framework is critical for fair evaluation of concept drift detectors."
  - "Hyperparameter optimization must be done on distinct data to ensure robust performance."
  - "Gradual drifts are significantly harder to detect than abrupt ones."
  - "Unsupervised detectors perform well on feature shifts but poorly on label changes."
```
---

## Paper 20: Am-una_summarized.md

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

## Paper 21: Unde et al_summarized.md

**Source File:** `Unde et al_summarized.md`

```yaml
paper_id: 10.1555/ijarp.6353
designation: international-algorithm-specific
title: AI-BASED REAL-TIME PERSONAL FINANCE DASHBOARD
authors: Unde, S. P.; Ghule, A. B.; Jaware, R. S.; Kanawade, S. N.; Koli, Y. K.
year: 2026
venue: International Journal Advanced Research Publication
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.B
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
  - 12.A
  - 12.B
  - 12.C
tldr: An AI-driven dashboard integrates real-time data ingestion, BERT-based categorization, and autoencoder anomaly detection to automate personal finance management and provide predictive insights.
problem_and_motivation: Digital payment proliferation fragments financial data across platforms, while manual tracking tools are time-consuming and error-prone. Existing systems lack real-time, proactive intelligence for automated categorization, anomaly detection, and forecasting. An integrated, automated dashboard is needed to unify data and enable intelligent financial oversight.
approach:
  - Data is ingested via banking APIs, webhooks, and an OCR module using CNNs (YOLOv4) for receipt digitization.
  - A preprocessing pipeline cleans data, normalizes features, and applies NLP tokenization to transaction descriptions.
  - A fine-tuned BERT model is used for automated expense categorization into domains like utilities and groceries.
  - A dual anomaly detection engine uses Isolation Forests and Conditional Autoencoders to flag point and contextual outliers.
  - LSTM networks forecast cash flows, and linear programming or LLM optimization generates dynamic savings recommendations.
findings:
  - num: Fine-tuned BERT model achieves 90-95% categorization accuracy, outperforming traditional keyword-based systems.
  - num: The system reduces manual data entry effort by over 80% through automated API and OCR integration.
  - Conditional Autoencoders successfully identify contextual outliers (e.g., duplicate subscriptions) with a low false-positive rate.
  - LSTM-based forecasts provide superior predictive accuracy for future savings trajectories and cash flows.
  - Users of the AI dashboard exhibit more disciplined spending habits due to automated alerts and real-time goal progress visualization.
key_figures_tables:
  - Figure 1: System architecture diagram illustrating four-layer pipeline → Overview of data flow from ingestion to presentation.
  - Figure 2: Project plan timeline → Visual representation of development phases and milestones.
  - Table 1: Performance comparison between traditional systems and proposed dashboard → Proposed AI dashboard metrics show higher accuracy, lower effort, and proactive functionality.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: API
    definition: Application Programming Interface, used for secure data ingestion from financial institutions.
  - term: BERT
    definition: Bidirectional Encoder Representations from Transformers, a deep learning model for natural language understanding.
  - term: CNN
    definition: Convolutional Neural Network, used for image feature extraction in OCR.
  - term: LSTM
    definition: Long Short-Term Memory network, a recurrent neural network for time-series forecasting.
  - term: NLP
    definition: Natural Language Processing, used for processing transaction text descriptions.
  - term: OCR
    definition: Optical Character Recognition, technology for digitizing text from physical receipts.
  - term: UPI
    definition: Unified Payments Interface, a real-time payment system in India.
critical_citations:
  - "[Patil and Jadhav, 2025] — Hybrid ML for automated expense classification."
  - "[Kharat, 2025] — Validates BERT for categorization and LSTM for forecasting."
  - "[Inzirillo and De Villelongue, 2023] — Autoencoder for anomaly detection."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Directly proposes BERT-based automated categorization of transactions.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: high
      justification: Discusses categorization into domains like utilities and groceries for dashboard design.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews existing systems and their limitations (manual tracking, fragmentation).
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies gaps like lack of real-time insights and intelligent automation.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: low
      justification: Touch on user behavior and spending habits, but does not address cold-start.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Uses LSTM for predictive cash flow forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: LSTM specifically chosen for sequential spending data forecasting.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Discusses budget monitoring and goal-based savings automation.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: LLM/linear programming for optimizing savings and adjusting spending limits.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Proactive anomaly detection is a core feature.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Implements Isolation Forest and Conditional Autoencoders for this purpose.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: Mentions a web interface but does not focus on mobile-first principles.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: Lacks detailed discussion on mobile UX design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Addresses secure API data flow and integrity, but not extensively.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Automated alerts and visualization foster engagement and awareness.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides a comparative analysis between traditional and proposed systems.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Evaluates categorization accuracy and anomaly detection performance.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Evaluates budget management and savings adherence improvements.
  contribution: This paper directly justifies Odin's core modules by demonstrating the effectiveness of a unified, automated dashboard. The BERT-based categorization validates Odin's expense classification approach. The dual autoencoder/Isolation Forest anomaly detection engine supports Odin's proactive security layer. The LSTM forecasting and LLM-optimized savings modules align with Odin's predictive budgeting and recommendation features. Overall, the proposed architecture provides a blueprint for Odin's integrated, real-time financial management system.
  directly_justifies:
    - Automated expense categorization using BERT can achieve over 90% accuracy.
    - Conditional Autoencoders are effective for detecting contextual outliers in spending data.
    - LSTM networks provide superior accuracy for forecasting future cash flows.
    - Reducing manual data entry by over 80% significantly improves user engagement.
    - An AI-driven dashboard can directly improve savings adherence through automated alerts.
  limits:
    - The performance of the OCR module is dependent on receipt image quality.
    - Accuracy of categorization is reliant on the consistency of bank API data.
    - The study does not address the cold-start problem for new users with no historical data.
  mapping_rationale: A systematic scan across all 12 functional domains was executed. The paper was flagged as highly relevant for Expense Categorization (3.A, 3.B), Existing Systems (4.B), Predictive Modeling (6.A, 6.B), Budget Recommendation (7.B), and Anomaly Detection (8.A, 8.B) due to its direct proposal of BERT, LSTM, and autoencoder-based solutions. Medium relevance was assigned to domains like Landscape (4.A), Engagement (11.A), and Evaluation (12.A, 12.B, 12.C) for its review context and comparative analysis. Topics like Filipino Cultural Context (2.A-D) and Mobile-First Design (9.A, 9.B) were considered but rejected as the paper is geographically unbound and focuses on a general web interface rather than mobile-specific UX. The paper's overall relevance to Odin is high as it provides empirical evidence for several core algorithmic modules, though it is from a general international context.
limitations:
  - Performance depends on receipt image quality and API data consistency. [unacknowledged]
  - Does not address the cold-start problem for new users.
remember_this:
  - BERT-based categorization achieves 90-95% accuracy.
  - The system reduces manual effort by over 80%.
  - Conditional Autoencoders detect contextual outliers effectively.
  - LSTM forecasting enables dynamic budget adjustments.
  - An AI dashboard promotes disciplined spending through automation.
```
---

## Paper 22: Espiritu M.-2026_summarized.md

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

## Paper 23: Percca_summarized.md

**Source File:** `Percca_summarized.md`

```yaml
paper_id: b8f9a7d3-5c4e-4f2a-9b1c-7d8e9f0a1b2c
designation: international-algorithm-specific
title: Unveiling the Financial Wellbeing Ecosystem: A Data-Driven Framework of Six Behavioral Profiles
authors: Percca, D. F. M.
year: 2026
venue: Unknown
odin_topics:
  - 1.A
  - 1.C
  - 5.A
  - 5.C
  - 7.A
  - 7.B
  - 12.A
  - 12.B
  - 13.A
tldr: A Random Forest classifier identifies six distinct financial wellbeing profiles, revealing subjective perception as the dominant predictor and differentiating structurally vulnerable segments.
problem_and_motivation: Traditional financial wellbeing evaluations rely on unidimensional, linear indices that overlook the complex interplay between short-term preparedness and long-term security. This simplification obscures the inherent heterogeneity of financial profiles, risking misguided conclusions and ineffective interventions. A holistic, intertemporal framework is needed to capture this complexity and inform tailored strategies.
approach:
  - Data from the 2021 National Financial Capability Study (NFCS) with 11,857 observations after excluding retired individuals and incomplete responses.
  - Theory-driven feature engineering binarised eight items to construct short-term and long-term financial wellbeing indices.
  - A 5x5 cross-tabulation of the indices produced a dependent variable with twenty-five cells, later synthesised into six distinct clusters.
  - Random Forest classification was implemented with 100 trees and hyperparameter tuning to validate the framework and analyse determinants.
  - Performance was evaluated using accuracy, precision, recall, and feature importance metrics, with SMOTE applied to address class imbalance.
findings:
  - num: Model 2 achieved 0.4557 accuracy, improving over the baseline model's 0.3689 through the inclusion of demographic controls.
  - The Subjective Index consistently emerged as the paramount classifier, outweighing both the Objective Index and Financial Literacy Index in predictive importance.
  - Six distinct financial profiles were identified: The Established, The Resilient, The Short-Sighted, The Illiquid Planners, The Precarious, and The Distressed.
  - The Short-Sighted (C3) are constrained by human capital deficits, while The Illiquid Planners (C4) are destabilised by exogenous income shocks despite planning capabilities.
  - A gender gap was evident, with females comprising 69.4% of The Distressed and males 57.8% of The Established.
  - Education and income strongly differentiated clusters, with 72.5% of those earning above $300,000 in The Established versus 66.1% of those earning below $50,000 in The Distressed.
  - Only 12% of The Established reported income disruption, compared with an average of 48.6% among vulnerable clusters.
  - Advanced financial literacy acts as a gatekeeper to the highest wellbeing tiers, with The Established showing a significant leap in their Literacy Index.
  - Misclassification patterns revealed persistent overlap between intermediate clusters (C3, C4, C5), indicating the complexity of financial wellbeing modelling.
key_figures_tables:
  - Figure 1: Intertemporal framework matrix with six profiles → Maps short-term/long-term intersection into distinct financial segments.
  - Figure 2: Normalised determinant scores across clusters → Shows progressive gradient and heterogeneity in core determinants.
  - Table 6: Random Forest performance metrics → Model 2 improves accuracy and recall for most clusters.
  - Table 7: Feature importance ranking → Subjective Index ranks highest in both models.
  - Table 8: Confusion matrix → Highlights persistent misclassification between adjacent clusters.
  - Table 9: Pairwise discriminant analysis → Reveals shifting determinants for different cluster boundaries.
key_equations:
  - equation: Y_i = f(X_{1,i} + X_{2,i} + X_{3,i}) + \epsilon_i
    explanation: Baseline Random Forest model without demographic controls.
  - equation: Y_i = f(X_{1,i} + X_{2,i} + X_{3,i} + Z_i) + \epsilon_i
    explanation: Full model including sociodemographic control variables.
definitions:
  - term: Random Forest
    definition: Ensemble method aggregating multiple decision trees for classification.
  - term: Subjective Dominance Effect
    definition: Individual self-perception outweighing objective metrics in predicting wellbeing.
  - term: Intertemporal Framework
    definition: Measurement combining short-term preparedness and long-term security.
  - term: NFCS
    definition: National Financial Capability Study, a US dataset on financial behaviours.
  - term: SMOTE
    definition: Synthetic Minority Over-sampling Technique for addressing class imbalance.
critical_citations:
  - "[Wagner & Walstad, 2019] — Foundational framework for index construction."
  - "[Lusardi & Streeter, 2023] — Establishes financial literacy as a core determinant."
  - "[Sticha, Lusardi, & Sconti, 2023] — Comprehensive financial wellbeing measure."
  - "[Kahneman & Deaton, 2010] — Income threshold for emotional stability plateau."
  - "[Breiman, 2001] — Random Forest methodology foundational reference."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "low"
      justification: "Paper uses US NFCS data, but profiles may generalise to Filipino YPs."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "low"
      justification: "Provides a behavioural profiling framework applicable to YPs."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Directly proposes a six-cluster taxonomy of financial profiles."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Uses Random Forest to classify individuals into wellbeing profiles."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "medium"
      justification: "Findings on short-term/long-term budgeting inform Odin's strategy design."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Cluster-specific interventions guide tailored budget recommendations."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides a robust multi-metric evaluation approach for classification."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Rigorous evaluation of Random Forest via precision, recall, and feature importance."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "medium"
      justification: "Addresses long-term security and savings planning across clusters."
  contribution: "This paper provides a validated intertemporal framework and six-cluster taxonomy that can be directly adapted for Odin's user profiling module. The 'subjective dominance effect' justifies the inclusion of user self-assessment in Odin's behavioural classification. The distinction between The Short-Sighted and The Illiquid Planners offers a template for Odin's infeasibility handling, where users with different root causes require different budget reduction strategies. The feature importance hierarchy (subjective > objective > literacy) guides Odin's feature engineering for its recommendation engine. The paper's evaluation methodology, including precision/recall for imbalanced classes, informs Odin's system evaluation approach for its algorithmic modules."
  directly_justifies:
    - "Subjective perception outweighs objective metrics in predicting financial wellbeing profiles."
    - "Six distinct financial profiles exist, ranging from 'The Established' to 'The Distressed'."
    - "The Short-Sighted and Illiquid Planners have structurally different vulnerability drivers."
    - "Advanced financial literacy is a gatekeeper to top-tier financial wellbeing."
    - "A 0.4557 accuracy is achievable when modelling financial profiles with demographic controls."
  limits:
    - "US-centric data limits generalisability to Filipino young professionals."
    - "Cross-sectional design prevents analysis of profile dynamics over time."
    - "Survivorship bias may result from excluding incomplete survey responses. [unacknowledged]"
    - "Preprint not peer-reviewed, requiring validation of findings."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The domains of Behavioral Profiling & Classification (5.A, 5.C), Budget Recommendation (7.A, 7.B), System Evaluation (12.A, 12.B), and Savings & Debt Management (13.A) were flagged as relevant. Topic 1.A and 1.C were assigned low relevance due to the US sample, but acknowledged for potential generalisability to Filipino YPs. Topic 5.A and 5.C received high relevance as the paper directly proposes and validates a six-profile taxonomy using Random Forest classification. Topics 7.A and 7.B were medium relevance because the cluster-specific interventions inform budget recommendation strategies. Topic 12.A and 12.B were medium and high respectively, as the paper's evaluation methodology is directly applicable. Topic 13.A was medium for its insights on long-term planning. Borderline cases included Topic 2.A (Culturally Specific Practices) and 2.D (Filipino Spending Cycles), which were rejected as the paper does not address Filipino culture. Topic 6.A (Predictive Modeling) was considered low and rejected because forecasting is not the primary focus. Overall, the paper provides strong empirical support for Odin's behavioural profiling and algorithmic evaluation modules, with moderate relevance to budgeting and savings functionalities."
limitations:
  - "US-centric data limits generalisability to Filipino young professionals."
  - "Cross-sectional design prevents analysis of profile dynamics over time."
  - "Survivorship bias may result from excluding incomplete survey responses. [unacknowledged]"
  - "Preprint not peer-reviewed, requiring validation of findings."
remember_this:
  - "Subjective perception dominates objective metrics in predicting financial wellbeing."
  - "Six distinct financial profiles exist, from established to distressed."
  - "The Short-Sighted need literacy interventions; Illiquid Planners need safety nets."
  - "Random Forest achieved 0.4557 accuracy with demographic controls."
  - "Advanced financial literacy is a gatekeeper to top-tier wellbeing."
```
---

## Paper 24: Aquino et al_summarized.md

**Source File:** `Aquino et al_summarized.md`

```yaml
paper_id: 10.69569/jip.2025.758
designation: local # Published in Bulacan State University, Philippines
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

## Paper 25: Gudelosao et al_summarized.md

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

## Paper 26: Bakuwa & Jimu_summarized.md

**Source File:** `Bakuwa & Jimu_summarized.md`

```yaml
paper_id: 10.5281/zenodo.17795962
designation: international-algorithm-specific
title: "DYNAMIC CREDIT SCORING WITH MACHINE LEANING: ENHANCING FINANCIAL INCLUSION AND RISK MANAGEMENT"
authors: "Bakuwa, D.; Jimu, P."
year: 2026
venue: "Afriresearch.com"
odin_topics:
  - "4.B"
  - "5.A"
  - "5.B"
  - "5.C"
  - "6.A"
  - "6.B"
  - "8.A"
  - "8.B"
  - "10.A"
  - "10.B"
  - "12.A"
  - "12.B"
tldr: "Dynamic credit scoring with machine learning uses alternative data and real-time updates to improve financial inclusion and risk management."
problem_and_motivation: "Traditional credit scoring relies on static, limited data, excluding many creditworthy individuals in developing economies. This limits financial inclusion and risk management. There is a need for adaptive systems that leverage alternative data and continuous updating."
approach:
  - "The system uses a three-tier architecture with presentation, application, and data layers."
  - "Data sources include traditional financial records and alternative data like mobile transactions and utility payments."
  - "Features were engineered including transaction consistency, debt-to-income ratio, and temporal trends."
  - "Models trained include logistic regression, XGBoost, and LSTM, using 80/20 stratified split and grid search with 5-fold cross-validation."
  - "Model evaluation used ROC-AUC, precision, recall, F1-score, KS statistic, and Gini coefficient."
  - "Risk tiers were defined: low (<10% PD), moderate (10-25% PD), and high (>25% PD)."
  - "Deployment enables real-time scoring and dynamic updates."
findings:
  - "num: XGBoost and LSTM outperformed logistic regression in predictive accuracy."
  - "num: Models with alternative data improved accuracy over traditional-only models."
  - "num: 62% of borrowers classified as low-risk, 25% moderate, 13% high-risk."
  - "num: 58% of borrowers with no formal credit history were identified as low or moderate risk using alternative data."
  - "num: Risk-adjusted strategies could reduce expected default rates by 15-20% compared to traditional methods."
  - "LSTM models effectively tracked evolving borrower behavior and provided early warnings."
key_figures_tables:
  - "None."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Dynamic credit scoring"
    definition: "Credit assessment that updates borrower risk profiles continuously using real-time data."
  - term: "Alternative data"
    definition: "Non-traditional data sources like mobile transactions, utility payments, and behavioral indicators."
  - term: "Explainable AI"
    definition: "AI techniques that provide interpretable model predictions to ensure transparency."
  - term: "ROC-AUC"
    definition: "Area under the receiver operating characteristic curve, a measure of model discrimination."
  - term: "LSTM"
    definition: "Long Short-Term Memory, a recurrent neural network for sequential data."
  - term: "XGBoost"
    definition: "Extreme Gradient Boosting, an ensemble learning method."
  - term: "Gini coefficient"
    definition: "A measure of inequality, used in credit scoring to assess model ranking power."
critical_citations:
  - "[Chen & Guestrin, 2016] — Introduced XGBoost used for credit scoring."
  - "[Lessmann et al., 2015] — Benchmarking state-of-the-art classification algorithms for credit scoring."
  - "[Bellotti & Crook, 2009] — Support vector machines for credit scoring."
  - "[Khandani et al., 2010] — Consumer credit-risk models via machine learning."
relevance:
  topics:
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Paper criticizes static credit scoring and proposes ML to overcome gaps, informing Odin's system design."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Paper uses behavioral data to create dynamic borrower profiles, directly applicable to Odin's profiling module."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "high"
      justification: "Dynamic updating and scoring of unbanked individuals addresses cold-start, relevant for new Odin users."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Paper employs classification algorithms (XGBoost, LSTM) for risk categorization, informing Odin's classification methods."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Predictive modeling of default using ML is transferable to predicting spending behavior in Odin."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "LSTM handles time-series data, applicable to forecasting spending patterns in Odin."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Paper discusses fraud detection and early warning, relevant to Odin's anomaly detection."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "medium"
      justification: "Machine learning algorithms used for detecting defaults can be adapted for spending anomalies."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "Paper highlights privacy concerns and data governance, directly relevant to Odin's privacy requirements."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "high"
      justification: "Emphasis on explainability and fairness to build trust, applicable to Odin's user trust considerations."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Paper uses ROC-AUC, Gini, etc., which can inform Odin's evaluation framework."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Evaluation of model performance (precision, recall, F1) is relevant for Odin's module assessment."
  contribution: "This paper directly supports Odin's behavioral profiling module by demonstrating the effectiveness of alternative data and time-series models for assessing financial behavior. Its dynamic scoring approach informs the design of Odin's predictive modeling and anomaly detection components, enabling early intervention. The emphasis on explainable AI and data privacy provides a framework for Odin's user trust and security features. The evaluation metrics (ROC-AUC, F1) are directly applicable to Odin's system evaluation."
  directly_justifies:
    - "Using mobile transaction data improves credit risk prediction for unbanked individuals."
    - "Dynamic models reduce expected default rates by 15-20% compared to static methods."
    - "LSTM networks effectively capture temporal patterns in borrower behavior for early warning."
    - "Explainable AI techniques enable transparency and regulatory compliance."
  limits:
    - "Data availability for some borrowers limits model coverage."
    - "Real-time scoring requires stable digital infrastructure, challenging in rural areas."
    - "Model bias may persist due to uneven data representation."
    - "Scalability requires efficient infrastructure for continual retraining."
    - "Interpretability of complex models like LSTMs may be difficult without explainability tools."
  mapping_rationale: "A systematic scan of all 12 functional domains and associated topic codes was performed. The paper was flagged as relevant for domains: Behavioral Profiling & Classification (high), Spending Forecasting (high), Anomaly Detection (medium), Data Privacy & User Trust (high), System Evaluation (medium), and Existing Systems & Gaps (high). The selected topic codes are 4.B, 5.A, 5.B, 5.C, 6.A, 6.B, 8.A, 8.B, 10.A, 10.B, 12.A, 12.B. Borderline cases included 8.A and 8.B, as default prediction overlaps with anomaly detection; they were assigned medium relevance. Domains like Filipino Cultural Context, Expense Categorization, Budget Recommendation, Mobile-First Design, User Retention, and Savings & Debt Management were rejected as the paper does not address them. Overall, the paper provides strong justification for Odin's predictive and privacy modules."
limitations:
  - "Data availability may be insufficient for some borrowers, limiting model coverage."
  - "Infrastructure challenges in rural regions can hinder real-time processing."
  - "Model bias may persist due to socio-economic disparities in training data."
  - "Scalability demands robust infrastructure for continuous retraining."
  - "Complex models like LSTM require explainability tools for stakeholder trust."
remember_this:
  - "Dynamic credit scoring reduces default rates by 15-20% relative to traditional methods."
  - "Alternative data enables scoring for 58% of unbanked borrowers."
  - "LSTM models provide real-time adaptability and early warning."
  - "Explainability and fairness are critical for user trust and regulatory compliance."
  - "Machine learning models outperform logistic regression in predictive accuracy."
```
---

## Paper 27: Bayangos & Lubango_summarized.md

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

## Paper 28: Oprins_summarized.md

**Source File:** `Oprins_summarized.md`

```yaml
paper_id: 10.1111/ntwe.70030
designation: "international"
title: "Understanding Online Freelancers' Labour Agency at the Intersection of Platforms, Wider Labour Markets, and Households: Evidence From the Philippines"
authors: "Oprins, J. H."
year: 2026
venue: "New Technology, Work and Employment"
odin_topics:
  - "1.A"
  - "1.B"
  - "1.C"
  - "2.A"
  - "2.D"
  - "4.A"
  - "4.B"
  - "5.A"
  - "5.C"
  - "11.A"
tldr: "Filipino online freelancers exercise labour agency through financial and temporal strategies shaped by platform logics, wider labour market positions, and gendered household responsibilities, with uneven implications for long-term platform success."
problem_and_motivation: "Research on online freelancers' labour agency often fails to account for the interplay between platform dynamics, broader labour market conditions, and gendered household responsibilities. This gap limits understanding of how freelancers make job-selection decisions critical to their platform success. An integrated framework is needed to examine these intersecting structures."
approach:
  - "Conducted in-depth interviews with 25 Filipino freelancers new to Upwork, recruited via Facebook groups."
  - "Used purposive sampling for diversity in urbanisation level, sex, and service type offered."
  - "Developed a semi-structured interview guide informed by a three-dimensional analytical framework: platform environment, wider labour market, and private sphere."
  - "Conducted walkthrough analysis of Upwork's features and examined each participant's platform profile."
  - "Applied Template Analysis with theory-driven initial coding and inductive refinement to capture participants' accounts."
findings:
  - "Freelancers exercise agency through two overarching strategies: optimising financial resources and managing temporal resources."
  - "Financial constraints from private lives limited freelancers' ability to purchase connects and absorb platform fees, leading some to accept off-platform work."
  - "Freelancers maximised limited free connects by carefully matching skills to job requirements and scrutinising clients for legitimacy."
  - "Men's full-time IT-BPO employment and breadwinner roles curtailed their time for Upwork, disadvantaging their platform career building."
  - "Women leveraged extended family support and experience with nocturnal work rhythms to accommodate Upwork's temporal demands."
  - "Gendered caregiving norms shaped women's turn to online freelancing for temporal flexibility in balancing paid work and domestic responsibilities."
  - "Freelancers' off-platform alternatives (other platforms, personal networks) reduced their adherence to a single platform's logics."
  - "Adherence to platform logics was necessary for accumulating reputation, yet structurally conditioned strategies often led freelancers to deprioritise Upwork."
key_figures_tables:
  - "None."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Labour agency"
    definition: "Intentional, purposive, and meaningful pursuit of self-interest with limited resources, exercised within and shaped by multiple intersecting contexts."
  - term: "Platformic management"
    definition: "Broad set of technological resources and rules wielded by online freelance platforms to enable and manage work."
critical_citations:
  - "[Graham et al., 2017] — Platform work can cause skill stagnation or downskilling."
  - "[Anwar and Graham, 2020] — New freelancers select easy jobs to build reputation quickly."
  - "[James, 2022, 2024] — Women's agency is constrained by social reproductive responsibilities."
  - "[Rahman, 2021] — Freelancers heavily dependent on a platform invest in rebuilding reputation after setbacks."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "high"
      justification: "Focuses on Filipino freelancers, a core demographic for Odin."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "medium"
      justification: "Details financial pressures and the role of online freelancing in household income strategies."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Examines financial optimisation strategies and resource allocation in job selection."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "high"
      justification: "Explores gendered household responsibilities, social reproduction, and family support structures."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "low"
      justification: "Provides contextual framing but does not directly address cyclical spending patterns."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Analyses platform logics of Upwork that inform Odin's consideration of existing PFMS and platform dynamics."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Identifies platform lock-in effects and reputation systems as limiting factors, relevant to PFMS gaps."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Demonstrates how behavioural strategies (financial/temporal optimisation) are shaped by structural contexts."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "contextual"
      justification: "Provides background on behavioural heterogeneity but does not address classification methods directly."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "medium"
      justification: "Highlights how platform engagement is shaped by temporal and financial logics, relevant to user retention."
  contribution: "This paper informs Odin's user profiling (5.A) by demonstrating that financial behavioural strategies are shaped by platform dynamics and household structures. It contributes to understanding culturally specific financial practices (2.A) by revealing gendered patterns in how Filipino freelancers manage temporal and financial resources. The findings on engagement dynamics (11.A) highlight how platform logics condition user behaviour, relevant for Odin's retention mechanisms. The paper justifies the need for Odin to account for users' broader labour market positions and private-sphere responsibilities in its design (4.B)."
  directly_justifies:
    - "Financial constraints from private lives limit freelancers' capacity to invest in platform engagement."
    - "Gendered caregiving norms shape women's pursuit of online freelancing for temporal flexibility."
    - "Men's full-time employment and breadwinner roles curtail their time for platform work."
    - "Adherence to platform logics is necessary for reputation accumulation but often deprioritised due to structural constraints."
  limits:
    - "Small sample size of 25 freelancers limits generalisability across the broader Filipino freelancer population."
    - "Qualitative design does not permit quantitative causal inference about platform success factors."
    - "Focus on new Upwork users may not reflect the strategies of established freelancers with strong reputations."
    - "Relies on self-reported accounts, which may be subject to social desirability or recall bias."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was conducted. The domains flagged as relevant were Filipino Cultural Context (codes 2.A, 2.D), Existing Systems & Gaps (4.A, 4.B), Behavioral Profiling & Classification (5.A, 5.C), and User Retention & Engagement (11.A). Code 2.A was assigned 'high' due to the paper's detailed treatment of gendered household roles and social reproduction. Code 2.D was assigned 'low' as seasonal spending is mentioned only as background framing. Code 1.A, 1.B, and 1.C were selected with 'high' and 'medium' relevance as the paper directly studies Filipino freelancers' demographics, financial structure, and behaviour. Code 4.A and 4.B received 'medium' relevance for their analysis of platform logics and gaps. Code 5.A and 5.C were rated 'medium' and 'contextual' respectively, as the paper demonstrates behavioural strategies but does not develop classification methods. Code 11.A was rated 'medium' for insights on engagement dynamics. Domains considered and rejected included Expense Categorization (3.A-C), Spending Forecasting (6.A-B), Budget Recommendation (7.A-D), Anomaly Detection (8.A-C), Mobile-First Design (9.A-B), Data Privacy (10.A-B), System Evaluation (12.A-C), and Savings & Debt Management (13.A-C), as the paper does not address these technical or design-focused domains. The paper is overall relevant to Odin for its rich qualitative insights into Filipino users' financial behaviours and the structural factors shaping them, though its primary contribution is conceptual rather than algorithmic."
limitations:
  - "Small sample size (n=25) limits generalisability."
  - "Qualitative design does not permit quantitative causal inference."
  - "Focus on new Upwork users may not reflect established freelancers' strategies. [unacknowledged]"
  - "Relies on self-reported accounts subject to bias. [unacknowledged]"
remember_this:
  - "Freelancers optimise financial and temporal resources in job selection."
  - "Gendered household responsibilities shape women's turn to online freelancing for flexibility."
  - "Men's full-time employment and breadwinner roles limit time for platform work."
  - "Adherence to platform logics is needed for reputation but often deprioritised."
  - "Structural constraints lead to uneven long-term platform success."
```
---

## Paper 29: Liu et al_summarized.md

**Source File:** `Liu et al_summarized.md`

```yaml
paper_id: 10.1145/3800645.3813097
designation: "international-algorithm-specific"
title: "Proteus: Shapeshifting Desktop Visualizations for Mobile via Multi-level Intelligent Adaptation"
authors: "Liu, C.; Cheng, S.; Liang, F.; Jiang, Z.; Huang, L.; Athapaththu, K.; Wang, Y."
year: 2026
venue: "ACM Designing Interactive Systems Conference (DIS'26)"
odin_topics:
  - "4.A"
  - "4.B"
  - "9.A"
  - "9.B"
  - "12.A"
  - "12.B"
tldr: "Proteus automates desktop-to-mobile visualization adaptation using a multi-level design space and LLM-driven multi-agent system, improving readability and interaction on small screens."
problem_and_motivation: "Desktop visualizations are designed for large screens, but mobile consumption is growing. Existing responsive techniques treat adaptation as a layout puzzle, lacking semantic understanding and hierarchical constraint handling. An automated approach that re-authors visualizations for mobile is needed."
approach:
  - "Constructed a multi-level design space (global topology, reference frame, visual elements) to model hierarchical adaptation constraints."
  - "Developed Proteus, an LLM-driven multi-agent system with Semantic Parser, Data Extractor, Design Planner, Frontend Engineer, and Visual Critic agents."
  - "The system parses desktop HTML/SVG, recovers data, plans transformations, generates TypeScript components, and iteratively refines based on critic feedback."
  - "Evaluated on 67 real-world web visualizations from Vega, Vega-Lite, Altair, and D3 galleries."
  - "Conducted a user study with 12 participants comparing Proteus to a strong multi-agent LLM baseline without the design space knowledge."
findings:
  - "num: Proteus achieved a render success rate of 91.8% compared to 87.8% for the baseline."
  - "num: Proteus significantly outperformed the baseline in data fidelity (p<0.05) and text readability (p<0.05)."
  - "num: Interaction reasonableness and visual aesthetics were significantly better (p<0.001)."
  - "The multi-level design space enables semantic re-authoring, such as converting static small multiples into interactive carousels."
  - "The critic agent is essential for convergence; without it, the system often fails to produce functional mobile variants."
  - "The system preserves data fidelity and improves readability by applying operations like tick decimation, label externalization, and layout serialization."
key_figures_tables:
  - "Figure 1: Multi-level design space (global topology, reference frame, visual elements) → hierarchical adaptation constraints."
  - "Figure 2: Proteus multi-agent architecture → automated adaptation pipeline with iterative refinement."
  - "Figure 3: Case studies on five real-world visualizations → effective adaptation across chart types."
  - "Figure 4: User study results → significant improvements over baseline in all five dimensions."
  - "Figure 5: Comparison examples → Proteus better preserves data and provides more reasonable interactions."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "LLM"
    definition: "Large Language Model"
  - term: "SVG"
    definition: "Scalable Vector Graphics"
  - term: "DOM"
    definition: "Document Object Model"
critical_citations:
  - "[Hoffswell et al., 2020] — established design space for responsive visualization."
  - "[Wu et al., 2020] — MobileVisFixer automates SVG layout repair."
  - "[Kim et al., 2022] — Cicero declarative grammar for responsive visualization."
relevance:
  topics:
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Surveys responsive visualization techniques and automated systems relevant to PFMS UI."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Identifies gaps in geometry-centric, flat-taxonomy approaches and proposes semantic re-authoring."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "high"
      justification: "Proposes a multi-level design space specifically for mobile adaptation, informing mobile-first UI design."
    - code: "9.B"
      name: "Mobile UX Design for Personal Finance"
      relevance: "contextual"
      justification: "Provides general mobile visualization UX principles, applicable to PFMS but not domain-specific."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "User study methodology with comparative evaluation can inform evaluation of PFMS systems."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Evaluates the algorithmic adaptation pipeline, relevant for assessing PFMS algorithmic components."
  contribution: "The paper's multi-level design space provides a framework for mobile-first design in Odin's UI. Its identification of gaps in existing responsive visualization techniques justifies Odin's need for semantic re-authoring. The iterative agent-based approach can inspire Odin's design for adaptive and intelligent user interfaces. The evaluation methodology offers a template for assessing Odin's mobile UX and algorithmic modules."
  directly_justifies:
    - "Geometry-centric adaptation fails to preserve semantic meaning on mobile screens."
    - "Hierarchical constraint propagation is needed to handle cross-level dependencies in mobile adaptation."
    - "Automated semantic re-authoring improves readability and interaction over simple resizing."
    - "LLM-driven multi-agent systems can effectively automate complex design tasks."
  limits:
    - "The study focuses on web visualizations, not specifically on personal finance data or Filipino context."
    - "Task-oriented analytical equivalence was not evaluated; only perceptual and usability metrics were used."
    - "Long-tail bespoke visualizations may not decompose cleanly into the proposed operators."
  mapping_rationale: "Systematic scan across all 12 functional domains: flagged 4.A (landscape) and 4.B (gaps) because the paper surveys existing responsive techniques and identifies limitations; 9.A (mobile-first design) and 9.B (mobile UX) because the paper proposes a design space and principles for mobile adaptation; 12.A and 12.B (evaluation) because the paper includes a user study and algorithmic evaluation. Borderline cases: 9.B is contextual as it is not specific to personal finance. Rejected domains: 1,2,3,5,6,7,8,10,11,13 as no mention of Filipino culture, spending, forecasting, budget, anomaly, privacy, engagement, or savings/debt. Overall, the paper is highly relevant to Odin's mobile UI design and evaluation methodology."
limitations:
  - "The current implementation operates on vector-based specifications, not raster images."
  - "Long-tail of bespoke designs may not be handled well by the predefined operators."
  - "User study focuses on perceived quality, not task completion or analytical outcomes."
  - "No direct comparison with MobileVisFixer or Cicero due to different task settings."
remember_this:
  - "Proteus achieved 91.8% render success on 67 real-world visualizations."
  - "Multi-level design space enables semantic re-authoring beyond geometric resizing."
  - "LLM-driven multi-agent system with critic feedback iteratively refines mobile adaptations."
  - "Significant improvements in readability, interaction, and aesthetics over baseline."
```
---

## Paper 30: Raman et al_summarized.md

**Source File:** `Raman et al_summarized.md`

```yaml
paper_id: 10.48550/arXiv.2606.9052
designation: international-algorithm-specific
title: "REMI: A Novel Causal Schema Memory Architecture for Personalized Lifestyle Recommendation Agents"
authors: "Raman, V.; R, V. A.; Ragav, A."
year: 2026
venue: "Unknown"
odin_topics:
  - 5.B
  - 6.A
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 9.A
  - 10.A
  - 12.A
tldr: "REMI combines a personal causal knowledge graph, causal reasoning, and schema-based planning to generate explainable, personalized lifestyle recommendations."
problem_and_motivation: "Current LLM-based personal assistants provide generic, population-level advice that fails to account for individual circumstances and lacks transparent reasoning. This limits their usefulness and trustworthiness in sensitive domains like health and lifestyle. A system is needed that leverages personal data to reason about cause-effect relationships and provides explainable, tailored recommendations."
approach:
  - "The system maintains a personal causal knowledge graph encoding user events and their causal relationships."
  - "A causal reasoner uses graph traversal, LLM-based path scoring, and counterfactual analysis to identify relevant causal factors for a user query."
  - "A schema-based planner retrieves and instantiates abstract plan templates with the user's specific causal factors to generate a personalized action plan."
  - "An LLM orchestrator assembles retrieved memory, causal factors, and the action plan into a coherent, explainable final response."
  - "The architecture was evaluated on 28 scenarios using two novel metrics: Personalization Salience Score (PSS) and Causal Reasoning Accuracy (CRA)."
findings:
  - "num: REMI achieved a PSS of 0.85-0.92, compared to 0.68-0.82 for memory-only and ablated CSM baselines."
  - "num: REMI achieved a CRA of 0.4-0.8, while the memory-only agent scored 0.0 and the ablated CSM scored 0.2-0.6."
  - "Causal reasoning and structured schema planning are crucial for accurate and consistent explainable recommendations."
  - "The system demonstrates robustness by maintaining high personalization even when responses are driven by causal inference rather than direct memory retrieval."
key_figures_tables:
  - "Figure 1: Overview of the Causal Schema Memory (CSM) architecture → Shows the four main components and their interaction."
  - "Figure 2: Example event graph illustrating the causal chain between lifestyle factors → Provides a visual example of the personal knowledge graph."
key_equations:
  - equation: "PSS = 1/|C| * sum_{c in C} [ max_{r in R} sim(c, r) >= tau ]"
    explanation: "Measures how much personal context is reflected in the response."
  - equation: "CRA = 1/|F| * sum_{f in F} [ sim(f, R) >= tau ]"
    explanation: "Measures if the explanation aligns with causal paths in the graph."
definitions:
  - term: "PSS"
    definition: "Personalization Salience Score; measures reflection of user context in output."
  - term: "CRA"
    definition: "Causal Reasoning Accuracy; measures alignment of explanation with causal paths."
  - term: "CSM"
    definition: "Causal Schema Memory; the proposed architecture for REMI."
  - term: "LLM"
    definition: "Large Language Model; used for orchestration and natural language generation."
critical_citations:
  - "[Harsha Tanneru et al., 2024] — Shows LLMs provide generic, population-level advice."
  - "[Subramanian et al., 2024] — Highlights lack of personalization in health advice from LLMs."
  - "[Yao et al., 2023] — Introduces ReAct, a baseline for LLM agents with reasoning and acting."
relevance:
  topics:
    - code: 5.B
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "high"
      justification: "The paper directly addresses cold-start via a fallback mechanism for sparse user data."
    - code: 6.A
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "The architecture's causal reasoning can be adapted for predicting spending behavior."
    - code: 7.A
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "contextual"
      justification: "The schema-based planning approach is analogous to using domain knowledge for budgeting."
    - code: 7.B
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "The paper's approach to generating personalized, explainable recommendations is directly applicable to budget recommendations."
    - code: 8.A
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Counterfactual reasoning can be used to identify anomalous spending patterns."
    - code: 8.B
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "low"
      justification: "The paper discusses counterfactual analysis, a technique relevant to anomaly detection, but not specific algorithms."
    - code: 9.A
      name: "Mobile‑First Design Principles and Rationale"
      relevance: "contextual"
      justification: "The paper does not address mobile design but the architecture could inform mobile-first systems."
    - code: 10.A
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "low"
      justification: "The paper mentions data privacy but does not propose specific privacy mechanisms."
    - code: 12.A
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "The paper introduces new evaluation metrics (PSS, CRA) that could be adapted for financial systems."
  contribution: "REMI's architecture provides a novel integration of causal reasoning and schema-based planning, offering a template for building transparent, personalized recommendation systems. The proposed evaluation metrics (PSS and CRA) provide a rigorous way to assess personalization and explainability, which can be directly adapted for evaluating Odin's modules. The modular design of REMI allows for independent improvement or replacement of components, which aligns with Odin's need for a flexible and extensible system. The focus on providing transparent, causal explanations for recommendations is crucial for building user trust in Odin. The system's ability to handle sparse data through a fallback mechanism is relevant for Odin's cold-start problem with new users."
  directly_justifies:
    - "A memory-augmented, causal reasoning architecture can provide more context-aware recommendations."
    - "Schema-based planning bridges symbolic planning and neural generation to create interpretable action plans."
    - "Explicit reasoning traces linked to user data enhance user trust and allow auditing of the agent."
    - "Counterfactual reasoning can be used to test and validate recommended actions."
  limits:
    - "The paper focuses on lifestyle and wellness, not personal finance, requiring adaptation."
    - "The system's performance is dependent on the quality and quantity of user data, which may be sparse initially."
    - "The evaluation was conducted on a limited number of scenarios (28), which may not be generalizable."
    - "The risk of the LLM generating hallucinations remains, even with structured inputs."
  mapping_rationale: "A systematic scan of all 12 functional domains was performed. The domains flagged as relevant were: Behavioral Profiling (for cold-start mitigation), Spending Forecasting (for its predictive modeling approach), Budget Recommendation (for its schema-based planning and explainable output), Anomaly Detection (for its use of counterfactual reasoning), Mobile-First Design (for its potential to inform architecture), Data Privacy (for its discussion of trust), and System Evaluation (for its proposed metrics). The highest relevance (high/medium) was assigned to topics directly related to cold-start (5.B), budget recommendation (7.B), and evaluation (12.A). Topics like spending forecasting (6.A) and anomaly detection (8.A, 8.B) were deemed medium relevance because the approach is conceptually transferable but not domain-specific. Domains like Filipino cultural context (2.A-D) and expense categorization (3.A-C) were considered but rejected as the paper does not address these specifics. The paper's overall relevance to Odin is moderate; it offers a robust architectural pattern and evaluation methodology, but requires significant adaptation to the financial domain."
limitations:
  - "The evaluation was performed on a limited set of 28 scenarios, which may not be representative of real-world user diversity."
  - "The system's effectiveness for cold-start users, a key issue for Odin, is acknowledged but not empirically validated."
  - "The reliance on a single LLM (Gemini-2.0-Flash) for orchestration may introduce model-specific biases."
  - "The paper does not address how the causal graph would be built from raw financial transaction data."
  - "The computational cost for maintaining and reasoning over personal causal graphs for thousands of users is not addressed."
  - "The paper does not detail a user study to validate the perceived trustworthiness and usefulness of the explanations." [unacknowledged]
remember_this:
  - "REMI uses a causal knowledge graph to model user context and generate recommendations."
  - "The architecture achieves a Personalization Salience Score (PSS) of 0.85-0.92."
  - "Causal Reasoning Accuracy (CRA) improved from 0.0 to 0.8 with the full REMI architecture."
  - "Schema-based planning bridges symbolic reasoning and neural generation for interpretable outputs."
  - "The system provides transparent explanations by tracing recommendations back to causal factors."
```
---

## Paper 31: Soriano & Mamac_summarized.md

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

## Paper 32: Wu Y. et al_summarized.md

**Source File:** `Wu Y. et al_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international-algorithm-specific
title: "Test-Time Adaptation for Non-stationary Time Series: From Synthetic Regime Shifts to Financial Markets"
authors: "Wu, Y.; Deng, Q.; Chung, W.; Li, M."
year: 2026
venue: "Unknown"
odin_topics:
  - "6.A"
  - "6.B"
  - "8.A"
  - "12.B"
  - "5.B"
  - "12.A"
tldr: "Evaluates small-footprint test-time adaptation for time series forecasting under non-stationarity, finding that batch-normalization statistics refresh is a safe default while aggressive norm-only updates can hurt financial market predictions."
problem_and_motivation: "Real-world time series are non-stationary, causing forecasting models trained on past data to lose accuracy during deployment. Existing test-time adaptation methods lack clear guidance for streaming time series, especially in noisy financial markets where aggressive adaptation can degrade performance. A practical framework that balances adaptation benefit with stability is needed."
approach:
  - "Freezes backbone model and updates only normalization affine parameters (gamma, beta) using recent unlabeled windows."
  - "For classification, minimizes entropy and enforces temporal consistency via weak time-preserving augmentations."
  - "For regression, minimizes prediction variance across augmentations and optionally distills from an EMA teacher."
  - "Adds quadratic drift penalty to constrain inter-day parameter changes and uses uncertainty-triggered fallback to batch-normalization statistics refresh."
  - "Evaluates on synthetic regime shifts on ETT benchmarks and daily equity/FX series (SPY, QQQ, EUR/USD) across pandemic, high-inflation, and recovery regimes."
findings:
  - "num: Batch-normalization statistics refresh (bn_stats) improves direction accuracy on QQQ by 2.2 percentage points and on EUR/USD by 0.4 percentage points."
  - "num: Norm-only adaptation improves forecast error on ETT synthetic gradual drift but decreases direction accuracy on QQQ from 0.503 to 0.463."
  - "Diebold-Mariano tests show bn_stats significantly outperforms no_tta on SPY (DM=-2.781, p=0.0054) and QQQ (DM=-2.290, p=0.0220)."
  - "Structuralswitches in periodic components remain challenging, with norm-only updates yielding R2 of -0.02 and bn_stats yielding -20.80 on ETTh1."
  - "Uncertainty-triggered fallback mitigates harmful norm-only updates, improving stability in noisy financial regimes."
  - "EMA-teacher self-distillation reduces variance of adapted parameters, complementing augmentation-variance minimization for regression."
  - "Norm-only updates are effective for smooth low-order moment shifts but overfit short noisy windows in financial markets."
  - "Backtest shows bn_stats achieves highest Sharpe ratio (1.930 on SPY, 4.080 on QQQ) while norm_only underperforms the frozen baseline."
key_figures_tables:
  - "Table 1: Representative ETTh1 results under synthetic shifts → Norm-only improves gradual drift but fails on structural switches."
  - "Table 2: Directional accuracy on equity/FX → bn_stats has best average rank (1.66), norm_only second (2.00), no_tta worst (2.33)."
  - "Table 3: Diebold-Mariano tests → bn_stats significantly better than no_tta on all markets; norm_only worse on SPY/QQQ."
  - "Table 4-5: SPY/QQQ backtest performance → bn_stats yields higher Sharpe ratios; norm_only underperforms no_tta."
  - "Figure 2: Rolling forecast metrics on ETTh1 under gradual drift → norm-only reduces errors in later horizon segments."
  - "Figure 3: Rolling direction accuracy and RMSE for SPY/QQQ/EURUSD → TTA gains concentrated in pandemic and early recovery periods."
key_equations:
  - equation: "L_ent = -1/|B| sum_{X in B} sum_c p_c(X) log p_c(X)"
    explanation: "Entropy minimization sharpens classification posteriors."
  - equation: "L_cons = 1/|B| sum_{X in B} ||p(X) - p(T(X))||^2"
    explanation: "Consistency penalizes sensitivity to weak time-preserving transforms."
  - equation: "L_var = 1/|B| sum_{X in B} Var({y(T_k(X))}_{k=1}^K)"
    explanation: "Variance minimization reduces local Lipschitz constant of regressor."
  - equation: "L_sd = 1/|B| sum_{X in B} ||y_theta(X) - y_tilde(X)||^2"
    explanation: "Self-distillation anchors predictions to EMA teacher."
  - equation: "L_drift = gamma ||theta(t) - theta(t-1)||^2"
    explanation: "Drift penalty shrinks inter-day parameter changes."
definitions:
  - term: "TTA"
    definition: "Test-time adaptation, updating model parameters using unlabeled test inputs."
  - term: "BN"
    definition: "Batch normalization, normalizes hidden activations using batch statistics."
  - term: "RevIN"
    definition: "Reversible instance normalization, standardizes sequences and reverses before output."
  - term: "EMA"
    definition: "Exponential moving average, used for teacher model in self-distillation."
  - term: "DM test"
    definition: "Diebold-Mariano test, compares predictive accuracy of two forecasts."
critical_citations:
  - "[Wang et al., 2021] — Foundational TTA via entropy minimization."
  - "[Wang et al., 2022] — Stabilizers for streaming TTA."
  - "[Kim et al., 2022] — RevIN for distribution shift in time series."
  - "[Schneider et al., 2020] — BN statistics refresh improves robustness."
  - "[Diebold & Mariano, 1995] — Standard test for forecast comparison."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Directly evaluates forecasting models under distribution shift, core to Odin's predictive module."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Tests TTA algorithms on sequential financial time series, informing Odin's forecasting choices."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Uncertainty-triggered fallback provides baseline strategy for detecting and handling anomalous shifts."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Provides regime-wise evaluation framework and statistical tests (DM, NW) for comparing algorithms."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "medium"
      justification: "Addresses adaptation to changing user behavior over time, analogous to cold-start profile dynamics."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Uses rolling metrics, backtests, and statistical significance tests relevant to Odin's evaluation."
  contribution: "Provides empirical guidance for deploying test-time adaptation in Odin's forecasting module, recommending batch-normalization statistics refresh as a safe default. Informs the design of anomaly detection fallbacks when uncertainty is high. Offers a regime-wise evaluation framework with statistical tests (Diebold-Mariano, Newey-West) that Odin can adopt for rigorous module comparison. Quantifies the trade-off between adaptation benefit and stability, directly applicable to Odin's cold-start and profile dynamics challenges. The drift penalty and EMA-teacher stabilization techniques can be integrated into Odin's budget recommendation and forecasting systems to prevent overfitting to recent noisy spending patterns."
  directly_justifies:
    - "Batch-normalization statistics refresh is a safe default for adapting to spending pattern shifts."
    - "Aggressive norm-only updates can harm forecast accuracy on volatile spending data."
    - "Uncertainty-triggered fallback mitigates harmful updates in high-variance periods."
    - "Regime-wise evaluation with Diebold-Mariano tests is recommended for comparing forecasting modules."
  limits:
    - "Experiments focus on daily financial series; spending data may have different seasonality and autocorrelation."
    - "Synthetic shifts are stylized and may not capture all real-world non-stationarities in personal finance."
    - "TTA framework tested on TCN and Transformer backbones; Odin may use different architectures."
    - "Classification task is direction prediction, not directly applicable to Odin's spending forecasting needs."
  mapping_rationale: "Systematic scan across all 12 functional domains and canonical topics identified the paper's primary relevance to Forecasting (6.A, 6.B) and Anomaly Detection (8.A) due to its test-time adaptation framework for non-stationary time series. Algorithmic Evaluation (12.B) was flagged medium for its rigorous statistical testing methodology. Behavioral Profiling (5.B) was deemed medium because adaptation to shifting distributions parallels cold-start profile dynamics. System Evaluation (12.A) was marked medium for the regime-wise and backtest evaluation frameworks. Expense Categorization (3.A-C) and Budget Recommendation (7.A-D) were rejected as the paper does not address categorization or constrained optimization. Savings & Debt Management (13.A-C) was rejected as the focus is on forecasting, not savings/debt. Mobile-First Design (9.A-B), Data Privacy (10.A-B), and User Retention (11.A-B) were rejected as the paper is algorithmic and does not discuss UX, privacy, or engagement. User-Declared Preferences (2.C) and Culturally Specific Practices (2.A) were not addressed. The paper's overall relevance to Odin is high for forecasting and anomaly detection modules, providing both algorithmic choices and evaluation best practices."
limitations:
  - "Aggressive norm-only adaptation can overfit short windows and degrade performance on noisy financial data."
  - "The uncertainty threshold is estimated on validation data, which may not generalize to new regimes."
  - "Synthetic shift generators are stylized and may not capture all real-world distribution changes."
  - "Backtest strategies are simple and do not account for transaction costs or market impact. [unacknowledged]"
  - "The study does not explore adaptation for multi-horizon spending forecasts beyond 96-step horizons. [unacknowledged]"
remember_this:
  - "Batch-normalization statistics refresh is a safe default for test-time adaptation."
  - "Aggressive norm-only updates can significantly hurt forecast accuracy on volatile data."
  - "Uncertainty-triggered fallback prevents harmful gradient updates in high-variance periods."
  - "Regime-wise evaluation reveals that adaptation gains are concentrated during strong distribution shifts."
  - "Drift penalties and EMA teachers stabilize adaptation, preventing overreaction to noisy windows."
```
---

## Paper 33: Xu et al_summarized.md

**Source File:** `Xu et al_summarized.md`

```yaml
paper_id: 16e1b7fa-84da-5b1f-a6e4-9a1958f3e6a6
designation: international
title: Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions
authors: Xu, Y.; Chen, Q.; Ma, Z.; Liu, D.; Wang, W.; Wang, X.; Xiong, L.; Wang, W.
year: 2026
venue: ACM Computing Surveys
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 7.C
  - 7.D
  - 8.A
  - 8.B
  - 8.C
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 12.A
  - 12.B
tldr: A capability-oriented survey organizes personalized LLM agents into profile modeling, memory, planning, and action execution, evaluating their user adaptation, temporal continuity, and decision alignment.
problem_and_motivation: Personalization in LLM-powered agents extends beyond response style to influence the entire decision pipeline, yet prior reviews remain fragmented, focusing on isolated capabilities. A unified, system-level understanding of how personalization objectives propagate across agent components and affect evaluation is lacking.
approach:
  - Proposes a capability-oriented taxonomy with four interdependent components: profile modeling, memory, planning, and action execution.
  - Reviews representative methods for each capability, analyzing how user signals are represented, propagated, and operationalized.
  - Surveys evaluation metrics, assessment paradigms (automatic, rule-based, LLM-as-judge), and benchmarks for personalized agents.
  - Summarizes applications across conversational assistants, content creation, delegation, and expert domains.
  - Identifies open challenges including decision-critical user modeling, temporal dynamics, generalization, evaluation, privacy, and efficiency.
findings:
  - Personalization is a system-wide property requiring coordinated operation of multiple internal capabilities, not a single adaptation module.
  - Profile modeling bridges user understanding with agent role configuration through persona-based and response-based paradigms.
  - Memory schemes range from textual summaries to structured graphs, with retrieval mechanisms including content-based, structure-aware, and policy-guided approaches.
  - Planning is categorized into one-shot (user signal grounding and internal refinement) and feedback-driven (clarification seeking, user revision, non-user feedback) paradigms.
  - Evaluation must capture effectiveness, adaptivity, generalization, robustness, and risk using metrics like Preference Alignment, Adaptation Success Rate, and Privacy Leakage Rate.
  - num: Over 80 benchmarks and evaluation protocols are surveyed, highlighting the diversity of personalized agent assessment.
  - Deployed assistants (ChatGPT, Gemini, DeepSeek) now support persistent user memories and controllable personalization.
key_figures_tables:
  - Figure 1: Overview of personalized LLM agents showing the closed-loop interaction from user request through profile, memory, planning, and action execution → personalization forms a continuous adaptation loop.
  - Figure 2: User-specific data in personalization process, distinguishing historical data and interaction data → dual-timescale personalization from stable traits to real-time intent.
  - Figure 3: Two-dimensional taxonomy of user preferences by expression form (explicit/implicit) and semantic function (behavioral/topical) → enables targeted modeling and interpretability.
  - Figure 4: Taxonomy of personalized LLM-powered agents organized by the four core capabilities → structured foundation for reviewing methods and benchmarks.
  - Table 1: Comparison of the four core capabilities along typical inputs, temporal scope, and primary objectives → clarifies distinctions among profile, memory, planning, and action.
  - Table 2: Evaluation metrics for personalized agents across five goals → comprehensive framework for assessing personalization quality.
  - Table 3: Summary of personalized benchmarks with scale, task, preference type, goal, and evaluation metrics → representative coverage of interactive alignment and user-substitution settings.
key_equations:
  - equation: "\\pi(a_t|s_t, h_t)"
    explanation: Agent policy conditioned on environment and internal state.
  - equation: "h_{t+1} = f(h_t, a_t, s_{t+1})"
    explanation: Internal state update after action and environment transition.
  - equation: "\\pi(a_t|s_t, h_t, p_u)"
    explanation: User-conditioned policy incorporating user preferences.
  - equation: "h_{t+1} = f(h_t, a_t, s_{t+1}, p_u)"
    explanation: User-conditioned internal state update.
  - equation: "\\pi_u^* \\propto \\arg\\max_\\pi \\mathbb{E}_{\\tau(u) \\sim \\pi(\\cdot|Q, \\hat{p}_u)} R_u(\\tau(u))"
    explanation: Objective for personalized policy optimization maximizing user-aligned utility.
definitions:
  - term: PLA
    definition: Personalized LLM-powered agent adapting behavior to individual users across the decision pipeline.
  - term: RAG
    definition: Retrieval-Augmented Generation, a method to incorporate external memory into LLM generation.
  - term: POMDP
    definition: Partially Observable Markov Decision Process for decision-making under uncertainty.
  - term: PPR
    definition: Personalized PageRank for graph-based retrieval.
  - term: LLM-J
    definition: LLM-as-a-judge evaluation paradigm using a general-purpose LLM as evaluator.
  - term: LLM-E
    definition: Learned LLM-based evaluator trained for specific preference dimensions.
critical_citations:
  - "[Zhang et al., 2024] — Comprehensive survey on personalization of large language models."
  - "[Wu et al., 2025] — Survey on memory mechanisms in the era of LLMs."
  - "[Wei et al., 2025] — Modern survey of LLM planning capabilities."
  - "[Xu et al., 2025] — Survey on personalized generation in the large model era."
  - "[Ferrag et al., 2025] — Comprehensive review of autonomous AI agents."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly proposes capability-oriented taxonomy including profile modeling for user adaptation.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: medium
      justification: Discusses iterative refinement of user representations and sparsity issues.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: contextual
      justification: Mentions user profiling paradigms but does not focus on classification methods.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Reviews planning and forecasting as personalization capabilities.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: contextual
      justification: Does not address specific forecasting algorithms for spending data.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Discusses planning strategies and user constraints relevant to budgeting.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: Covers personalized planning and recommendation through user preference conditioning.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: contextual
      justification: Mentions constrained optimization but not specifically for budget allocation.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: medium
      justification: References infeasibility handling in action grounding (AWARE-US).
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Reviews evaluation metrics like risk sensitivity and safety relevant to anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Does not address specific anomaly detection algorithms.
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: low
      justification: Mentions cold-start in benchmarks but not specifically for anomaly detection.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: Not a focus; applications include mobile but design principles not discussed.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: Not a focus; applications are general and not mobile-specific.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Dedicated section on privacy, with benchmarks for Privacy Leakage Rate.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Mentions trust in applications (finance, healthcare) and privacy implications.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Proactivity metrics and retention mechanisms are reviewed.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: Covers interaction efficiency, proactivity, and iterative personalization loops.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Comprehensive evaluation section with metrics and benchmarks.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Component-probing benchmarks for memory, planning, and tool use.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: high
      justification: Covers preference alignment, planning accuracy, and personalized benchmarks.
  contribution: The survey provides a structured foundation for developing user-aligned, adaptive LLM agents by clarifying the design space of personalization. Its capability-oriented taxonomy (profile, memory, planning, action) directly informs how Odin could architect its personalization pipeline across modules like behavioral profiling, spending forecasting, and budget recommendation. The comprehensive evaluation framework offers metrics and benchmarks for validating Odin's algorithmic modules and user satisfaction. The discussion of open challenges (temporal dynamics, generalization, privacy) highlights critical considerations for Odin's long-term deployment and user trust.
  directly_justifies:
    - "Personalization permeates the entire decision pipeline, not just response generation, informing Odin's system-level design."
    - "Profile modeling bridges user understanding with agent role configuration, supporting Odin's user profiling module."
    - "Memory schemes maintain temporal continuity, enabling Odin to track user spending patterns across sessions."
    - "Planning translates user-specific information into actionable decisions, directly applicable to Odin's budget recommendation."
    - "Evaluation must balance effectiveness, adaptivity, and risk, guiding Odin's multi-metric validation approach."
  limits:
    - "Survey is conceptual and does not provide empirical validation of personalization techniques in financial domains."
    - "Focus is on general-purpose agents; financial-specific personalization (e.g., spending behavior) is not deeply addressed."
    - "Benchmarks are general; financial-specific benchmarks like spending forecasting or budget allocation are not covered."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated canonical topic codes was conducted to assess the paper's relevance to Odin. The paper's capability-oriented taxonomy and comprehensive review of personalization mechanisms directly informed high relevance assignments for domains including Behavioral Profiling & Classification (5.A, 5.B, 5.C), Budget Recommendation (7.B, 7.D), Data Privacy & User Trust (10.A, 10.B), and System Evaluation (12.A, 12.B, 12.C). Medium relevance was assigned to domains such as Spending Forecasting (6.A) due to the discussion of planning and prediction, and User Retention & Engagement (11.A, 11.B) through metrics like proactivity and interaction efficiency. Low relevance was noted for Mobile-First Design (9.A, 9.B) as the survey does not address platform-specific design, and for specific algorithmic domains like Anomaly Detection (8.B, 8.C) and Savings & Debt Management (13.A, 13.B, 13.C) which are not directly discussed. The paper's general-agent focus means it provides architectural and evaluative guidance rather than financial-domain-specific insights, making it highly relevant for Odin's system-level design and evaluation framework but contextual for domain-specific algorithm selection.
limitations:
  - "Survey synthesizes existing work but does not propose novel personalization algorithms."
  - "Focus on LLM agents may not directly translate to traditional personal finance rule-based systems."
  - "Real-world deployment constraints like latency and cost are discussed but not empirically analyzed. [unacknowledged]"
  - "Cultural and demographic specificity (e.g., Filipino context) is not addressed. [unacknowledged]"
remember_this:
  - "Personalization is a system-wide property across profile, memory, planning, and action."
  - "User preferences are categorized by expression form and semantic function."
  - "Memory schemes range from textual summaries to structured graphs with policy-guided retrieval."
  - "Evaluation must capture effectiveness, adaptivity, generalization, robustness, and risk."
  - "num: Over 80 benchmarks are surveyed for evaluating personalized agent capabilities."
```
---

## Paper 34: Tomas & Soriano_summarized.md

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

## Paper 35: Ong H. et al_summarized.md

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

## Paper 36: Lee J. et al_summarized.md

**Source File:** `Lee J. et al_summarized.md`

```yaml
paper_id: 10.1080/13696998.2026.2630598
designation: international
title: Comparing deep learning and classical regression approaches for predicting healthcare expenditure and spending: a systematic review
authors: Lee, J. T.; Yeh, M. H.-S.; Li, V. C.-S.; Chen, H.-H.; Liu, Y.-H.; Chen, Y.-C.; Wu, D. B.-C.
year: 2026
venue: Journal of Medical Economics
odin_topics:
  - 3.A
  - 4.A
  - 5.A
  - 6.A
  - 6.B
  - 7.A
  - 8.B
  - 12.A
  - 12.B
  - 12.C
tldr: Deep learning excels in longitudinal, sequence-rich cost forecasting, while tree-based methods remain highly competitive for cross-sectional tabular prediction.
problem_and_motivation: Accurate prediction of individual healthcare costs is crucial for insurance underwriting, risk adjustment, budget planning, and value-based payment strategies. Traditional statistical approaches often struggle to capture complex nonlinear interactions in health data, but a clear understanding of when deep learning offers a meaningful advantage over classical methods is lacking.
approach:
  - A preregistered systematic review (PROSPERO CRD420251129440) was conducted.
  - Searches were performed in Web of Science, PubMed, Embase, and Scopus through August 2025.
  - Eight studies were included that used real-world individual-level data and directly compared a deep learning architecture with a classical regression comparator.
  - Data were extracted on population, predictors, outcome horizon, model type, validation strategy, and performance metrics.
  - Findings were synthesized narratively, leading to the proposal of a Complexity-Performance Hypothesis.
findings:
  - "num: Sequential deep learning models showed approximately 10-20% reductions in RMSE/MAE over classical methods in longitudinal designs."
  - "num: R² improvements from deep learning ranged from 0.01 to 0.15 in various studies."
  - "num: Deep learning models achieved AUROC values up to 0.78 for high-risk classification of preventable hospitalizations."
  - Prior costs and utilization were consistently the strongest predictors across all studies.
  - For low-dimensional, structured, cross-sectional data, generalized linear models and tree-based approaches remain robust baselines.
  - A conceptual Complexity-Performance Hypothesis was formulated, linking model capacity to data complexity.
key_figures_tables:
  - "Figure 2: Conceptual model performance by data complexity → Deep learning excels in complex settings, while regression is best for simple data."
  - "Table 1: Characteristics of identified studies → Summary of study design, population, and models for all 8 included papers."
  - "Table 2: Model performance and features of included studies → Detailed comparative results for all studies."
  - "Table 3: Neural network architectures applied → Categorization of models by data type used."
  - "Table 4: Challenges of deep learning in spending prediction → Future strategies for interpretability, benchmarking, and generalizability."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: LSTM
    definition: Long short-term memory, a recurrent neural network architecture.
  - term: CNN
    definition: Convolutional neural network.
  - term: RNN
    definition: Recurrent neural network.
  - term: GLM
    definition: Generalized linear model.
  - term: RMSE
    definition: Root mean square error.
  - term: MAE
    definition: Mean absolute error.
  - term: AUROC
    definition: Area under the receiver operating characteristic curve.
  - term: EMR
    definition: Electronic medical records.
  - term: EHR
    definition: Electronic health records.
  - term: XAI
    definition: Explainable artificial intelligence.
critical_citations:
  - "[Drewe-Boss et al., 2022] — Provided a strong example of deep learning outperforming ridge regression."
  - "[Yang et al., 2018] — Showed RNN gains for high-cost patient forecasting."
  - "[Lewis et al., 2021] — Demonstrated LSTM and CNN superiority for preventable care prediction."
  - "[Esteva et al., 2019] — Cited for the promise of deep learning in healthcare."
  - "[Topol, 2019] — Cited for contextualizing the convergence of human and AI in medicine."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: The review discusses different outcome variables like total cost and pharmacy expenditure.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Reviews the predictive modeling landscape, which is relevant to PFMS.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Discusses predicting high-cost patients, analogous to financial profiling.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly compares forecasting models for expenditure, informing Odin's predictor selection.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Focuses on algorithms like LSTM and CNN-LSTM for sequential data, directly applicable to spending forecasting.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Finding on data complexity ties to optimal model choice for budget recommendation.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Discussion of identifying high-cost outliers relates to anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a systematic framework for comparing algorithmic modules, a core part of system evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Directly evaluates the performance of different algorithmic modules (deep learning vs. regression).
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: high
      justification: The systematic review methodology and metrics (RMSE, MAE, R²) are directly transferable to evaluating budget recommendation.
  contribution: This systematic review provides a clear, evidence-based framework for selecting between deep learning, tree-based, and regression models for spending prediction tasks. It directly informs Odin's algorithmic module selection by establishing that LSTM and CNN-LSTM models are best for longitudinal data, while simpler models are sufficient for cross-sectional data. The proposed Complexity-Performance Hypothesis can guide the design of Odin's forecasting and anomaly detection components.
  directly_justifies:
    - "Sequential deep learning models (LSTM, CNN-LSTM) offer clear predictive advantages for longitudinal spending data."
    - "Tree-based methods remain highly competitive for cross-sectional, tabular spending prediction."
    - "Prior costs and utilization are consistently the strongest predictors of future spending."
    - "The complexity of the data should dictate the choice of the forecasting model."
  limits:
    - "Review based on a small and heterogeneous set of eight studies, limiting generalizability."
    - "None of the studies performed full external validation across independent datasets."
    - "The review's findings are based on healthcare data, not personal finance data, which may have different characteristics."
    - "The Complexity-Performance Hypothesis is a conceptual framework requiring further systematic validation."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to the 'Spending Forecasting' domain (codes 6.A, 6.B) as it is a systematic review directly comparing forecasting algorithms. It also has high relevance to the 'System Evaluation' domain (codes 12.A, 12.B, 12.C) due to its focus on comparative performance metrics and evaluation frameworks. The paper provides medium relevance to 'Behavioral Profiling & Classification' (5.A) through its discussion of predicting high-cost populations, and 'Anomaly Detection' (8.B) via high-cost outlier identification. It offers contextual relevance to 'Expense Categorization' (3.A) and the 'Existing Systems' landscape (4.A). Domains such as Filipino Cultural Context, Mobile-First Design, and Data Privacy were considered and rejected because the paper does not address these topics. The 'Budget Recommendation' domain (7.A) is considered medium relevance as the findings on data complexity guide model choice for such recommendations. Overall, the paper provides strong empirical justification for model selection in Odin's forecasting and evaluation modules.
limitations:
  - "The evidence base is small (n=8) and heterogeneous in design and data sources."
  - "Prediction horizons are predominantly short-term (one year), limiting assessment of long-term performance. [unacknowledged]"
  - "Social determinants of health and behavioral predictors are rarely incorporated into the models. [unacknowledged]"
  - "None of the studies performed full external validation. [unacknowledged]"
  - "Assessments of calibration, fairness, and economic interpretability were sparse or absent. [unacknowledged]"
  - "The Complexity-Performance Hypothesis is a working hypothesis derived from a limited set of studies, not a definitive causal mechanism. [acknowledged]"
remember_this:
  - "Deep learning excels for longitudinal, sequence-rich cost forecasting."
  - "Tree-based methods are highly competitive for cross-sectional tabular data."
  - "Model accuracy is maximized when capacity is matched to data complexity."
  - "Prior costs and utilization are the strongest predictors of future spending."
  - "LSTM and CNN-LSTM hybrids reduced forecasting error by up to 20% in some studies."
```
---

## Paper 37: Dela Cruz et al_summarized.md

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

## Paper 38: Contreras_summarized.md

**Source File:** `Contreras_summarized.md`

```yaml
paper_id: 10.62762/JSE.2026.605759
designation: international-algorithm-specific
title: Adaptive Risk Evaluation in FinTech Systems via Reinforcement-Based Continuous Policy Optimization
authors: Contreras, E. M.
year: 2026
venue: ICCK Journal of Software Engineering
odin_topics:
  - 4.A
  - 4.B
  - 6.A
  - 6.B
  - 12.B
tldr: A reinforcement learning framework with continuous policy optimization enables adaptive risk scoring, achieving 97.4% accuracy and 98.8% adaptation rate in FinTech systems.
problem_and_motivation: Batch-trained risk models fail to adapt to drift and lack safe continuous update mechanisms, leading to performance degradation and operational risk. Existing systems do not support online learning without service interruption, creating a gap for deployable adaptive risk pipelines.
approach:
  - Formulates risk evaluation as a continuous-action Markov Decision Process with loss-sensitive rewards.
  - Uses a dual-module actor-critic with separate policy and value networks for stable convergence.
  - Separates online learning from inference to enable safe, downtime-free model updates.
  - Evaluates on a simulated FinTech environment with 8.5 million credit records.
  - Compares against Random Forest, Gradient Boosting, and Transformer baselines.
  - Implements a modular architecture with API gateway, online learning service, and model registry.
findings:
  - num: 97.4% classification accuracy, outperforming baselines by 18.9% over Transformer.
  - num: 98.8% trend adaptation rate, showing high responsiveness to distributional shifts.
  - num: 96.1% cumulative long-term performance index, indicating sustained optimization.
  - Provides system-level metrics: p50 inference latency 7.6ms, throughput 5,200 req/s.
  - ARL-CPO enables continuous policy updates without batch retraining, unlike baselines.
key_figures_tables:
  - Figure 1: ARL-CPO pipeline diagram → Shows closed-loop adaptive risk assessment.
  - Figure 2: Dual-module architecture with policy and value networks → Illustrates gradient-based refinement.
  - Figure 3: Integration into production FinTech risk system → Depicts separation of inference and learning.
  - Table 2: Experimental configuration → Lists hyperparameters and environment setup.
  - Table 3: Comparative performance analysis → ARL-CPO outperforms all baselines.
  - Table 4: Software system performance evaluation → Shows deployment-oriented metrics.
key_equations:
  - equation: Γ(t-1) = F(o,θ) - H(ξ) subject to V > L(t-g)
    explanation: Ensures risk actions meet minimum confidence under drift.
  - equation: Ψ = {q_r}(u,ξ) := λ(ξ-d)+Ω(λ_r - C_{r}{t-1}) · Ω_{u}{d-1}
    explanation: Modulates correction strength based on drift sensitivity.
  - equation: tV ≡ Λ_1 ∗(Φ_{t-1}) → Jλ|c−(β−η_r) ≡ ∇
    explanation: Monitors trade-off between service stability and risk governance.
  - equation: ||Λ(u,ω_r)|| = D_ξ(χ-λ_b)+G_ω(τ,ρ_k) := δ(u-ρ_w) ≥ ∇
    explanation: Compares update intensity against control boundaries.
definitions:
  - term: ARL-CPO
    definition: Adaptive Reinforcement Learning with Continuous Policy Optimization.
  - term: MDP
    definition: Markov Decision Process.
  - term: FinTech
    definition: Financial Technology.
  - term: RL
    definition: Reinforcement Learning.
  - term: TFM
    definition: Transformer-based model.
critical_citations:
  - [Mashrur et al., 2020] — survey of ML for financial risk management.
  - [Lu et al., 2018] — comprehensive review of learning under concept drift.
  - [Hambly et al., 2023] — recent advances in reinforcement learning in finance.
  - [Kreuzberger et al., 2023] — MLOps overview for production ML systems.
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews ML methods for risk, providing context for PFMS system design.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly addresses batch retraining and lack of continuous updates, a gap relevant to PFMS adaptation.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Uses reinforcement learning for predictive risk scoring, transferable to spending forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: Proposes continuous policy optimization for sequential decision making, applicable to spending forecasting.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: low
      justification: Provides evaluation methodology for algorithmic performance, but not specific to PFMS.
  contribution: ARL-CPO's continuous learning architecture can inform Odin's adaptive forecasting module by enabling real-time updates without retraining. Its separation of inference and learning provides a blueprint for Odin's system design to avoid service disruption. The reinforcement learning formulation could be adapted for Odin's anomaly detection to optimize long-term rewards. The evaluation metrics (accuracy, adaptation rate) offer benchmarks for Odin's predictive modules.
  directly_justifies:
    - Batch-trained models are fragile to drift and require manual retraining.
    - Continuous policy optimization improves adaptation rate to 98.8%.
    - Separation of online learning from inference enables safe updates without downtime.
    - Reinforcement learning with continuous actions yields higher accuracy than batch models.
  limits:
    - Use of synthetic data may limit generalizability to real-world FinTech data. [unacknowledged]
    - Operational constraints like feedback delays and compliance requirements are not addressed. [unacknowledged]
    - The study does not consider personal spending behavior, limiting direct applicability to PFMS. [unacknowledged]
  mapping_rationale: A systematic scan across all 12 functional domains and associated topic codes was performed. The paper was found most relevant to the 'Existing Systems & Gaps' domain (4.B) due to its focus on limitations of batch-trained models and the need for continuous adaptation. It also touches on 'Predictive Modeling' (6.A) and 'Forecasting Algorithms' (6.B) through its sequential decision formulation, though applied to credit risk rather than spending. 'Evaluation of Algorithmic Modules' (12.B) is tangentially relevant due to its empirical evaluation. Domains related to Filipino cultural context, expense categorization, budgeting, mobile design, privacy, retention, and savings/debt were rejected as the paper does not address these. The overall relevance is moderate, providing design insights for adaptive learning in PFMS.
limitations:
  - Use of synthetic data may limit generalizability to real-world FinTech data. [unacknowledged]
  - Operational constraints like feedback delays and compliance requirements are not addressed. [unacknowledged]
  - The study does not consider personal spending behavior, limiting direct applicability to PFMS. [unacknowledged]
remember_this:
  - Reinforcement learning with continuous actions achieves 97.4% accuracy in risk scoring.
  - Separating inference and learning enables safe, downtime-free model updates.
  - Dual-module actor-critic stabilizes learning under distributional shift.
  - ARL-CPO outperforms batch-trained baselines on adaptation and long-term performance.
  - Continuous policy optimization achieves 98.8% trend adaptation rate.
```
---

## Paper 39: Zhao et al_summarized.md

**Source File:** `Zhao et al_summarized.md`

```yaml
paper_id: 10.3389/frai.2026.1829649
designation: international-algorithm-specific
title: "DynEC: dynamic evolutionary clustering for power user load profiling using multi-view graph neural networks"
authors: "Zhao, L.; Zhao, H.; Li, M.; Wang, J.; Ke, X.; Yao, Y."
year: 2026
venue: "Frontiers in Artificial Intelligence"
odin_topics:
  - "5.A"
  - "5.B"
  - "5.C"
  - "6.A"
  - "6.B"
  - "8.A"
  - "8.B"
  - "8.C"
  - "10.A"
  - "10.B"
  - "12.A"
  - "12.B"
  - "12.C"
tldr: "DynEC is a dynamic evolutionary clustering framework using multi-view graph neural networks to profile power users, balancing snapshot quality and temporal smoothness to reduce identity switching during concept drift."
problem_and_motivation: "Static clustering models treat user load profiles as isolated snapshots, causing them to either overreact to daily noise or fail to adapt to genuine behavioral shifts. This leads to persistent misclassification and erratic cluster switching, undermining reliability in demand response and grid management. There is a need for a model that explicitly tracks behavioral evolution while suppressing unstable identity switching."
approach:
  - "Constructs a sparse multi-view dynamic graph integrating geometric proximity, temporal alignment via constrained DTW, and statistical dependence through Pearson correlation."
  - "Employs a gated spatio-temporal graph neural network (GST-GNN) with a multi-head graph attention network and GRU to learn evolution-aware node embeddings."
  - "Uses a dual-objective optimization strategy balancing snapshot clustering quality (KL divergence) with temporal consistency (KL divergence between consecutive soft assignments)."
  - "Evaluates on real-world smart meter data from three cities in China over one year, with data pre-processed into hourly load profiles."
  - "Compares against five baselines: K-Means, Spectral Clustering, Time2Graph, EvolveGCN-Clus, and evolutionary K-Means."
findings:
  - "num: DynEC achieves an ARI of 0.56 ± 0.06 in a mixed residential/commercial city, outperforming static K-Means (0.43) and Evol-KMeans (0.43)."
  - "num: DynEC reduces the Cluster Switching Rate (CSR) to 0.02-0.04 across all cities, significantly lower than K-Means (approx. 0.70-0.79)."
  - "The cDTW view is crucial, as removing it drops ARI from 0.62 to 0.35, confirming its importance for capturing shape similarity under temporal shifts."
  - "Removing the correlation view reduces stability (CSR from 0.02 to 0.05) and slightly decreases ARI, confirming its supplementary role."
  - "An ablation study shows that without the temporal consistency loss (λ=0), ARI drops from 0.62 to 0.50, although CSR remains low."
  - "The model demonstrates a smooth transition for a user adopting V2G, while K-Means shows erratic switching during the same concept drift event."
key_figures_tables:
  - "Figure 1: Overview of DynEC architecture → Illustrates the multi-view graph construction, spatio-temporal encoder, and dual-objective optimization."
  - "Figure 2: Sensitivity of λ on City A → Optimal trade-off between ARI and CSR occurs around λ=0.2."
  - "Figure 3: Sensitivity of fusion weights → Equal weighting (α=β=γ=1/3) provides the best balance between ARI and CSR."
  - "Figure 4: Robustness to phase shifts → cDTW aligns shape-similar but time-shifted profiles, whereas Euclidean distance fails."
  - "Figure 5: Concept drift visualization for User #42 → DynEC exhibits a smooth cluster transition compared to the erratic switching of K-Means."
  - "Figure 6: Event-driven validation → DynEC shows higher ARI than Evol-KMeans during high-event months, with a moderate CSR increase."
  - "Table 1: Comparison between static and dynamic clustering paradigms → Summarizes key differences in perspective, representation, and application."
  - "Table 2: Summary of baseline methods → Describes the five comparison models and their characteristics."
  - "Table 3: Implementation specifications → Details model architecture, hyperparameters, and training strategy."
  - "Table 4: Performance comparison → Presents quantitative results (ARI, SC, DBI, CSR) for all methods across three cities."
key_equations:
  - equation: "X = {X(1), X(2), ..., X(T)}"
    explanation: "Dynamic load profile stream over time."
  - equation: "P(X(t)) ≠ P(X(t+1))"
    explanation: "Concept drift definition: change in underlying distribution."
  - equation: "G = {G(1), G(2), ..., G(T)}"
    explanation: "Dynamic graph flow as a sequence of graphs."
  - equation: "fθ: G(t) → C(t)"
    explanation: "Clustering mapping function for each time step."
  - equation: "d_geo(i,j) = ||x_i(t) - x_j(t)||_2"
    explanation: "Euclidean distance for geometric proximity."
  - equation: "cDTW(x_i, x_j) = min_W Σ_{k=1}^K w_k"
    explanation: "Constrained DTW objective with Sakoe-Chiba band."
  - equation: "S_dtw(i,j) = exp(-d^2(i,j)/σ^2)"
    explanation: "Gaussian kernel to transform cDTW distance to similarity."
  - equation: "ρ(i,j) = |Σ (x_i - x̄_i)(x_j - x̄_j)| / (||x_i - x̄_i||_2 ||x_j - x̄_j||_2)"
    explanation: "Absolute Pearson correlation for statistical dependency."
  - equation: "A_fused(t) = αA_geo(t) + βA_dtw(t) + γA_corr(t)"
    explanation: "Weighted fusion of the three adjacency matrices."
  - equation: "A(t) = D^{-1/2}(A_fused(t) + I)D^{-1/2}"
    explanation: "Symmetric normalization of the fused adjacency matrix."
  - equation: "q_ik = (1 + ||z_i - μ_k||^2/ν)^(-(ν+1)/2) / Σ_{k'}(1 + ||z_i - μ_{k'}||^2/ν)^(-(ν+1)/2)"
    explanation: "Soft assignment using Student's t-distribution kernel."
  - equation: "p_ik = q_ik^2 / f_k / Σ_{k'} q_{ik'}^2 / f_{k'}"
    explanation: "Self-training target distribution for sharpening."
  - equation: "L = L_clus + λL_temp"
    explanation: "Dual-objective loss function combining clustering and temporal terms."
  - equation: "L_clus = KL(P(t) || Q(t)) = Σ_i Σ_k p_ik(t) log(p_ik(t) / q_ik(t))"
    explanation: "Clustering loss via KL divergence from target distribution."
  - equation: "L_temp = KL(Q(t-1) || Q(t)) = Σ_i Σ_k q_ik(t-1) log(q_ik(t-1) / q_ik(t))"
    explanation: "Temporal consistency loss penalizing sudden assignment changes."
  - equation: "CSR = 1/(T-1) Σ_{t=1}^{T-1} (1/N) Σ_{i=1}^N 1(c_i(t) ≠ c_i(t+1))"
    explanation: "Cluster Switching Rate metric for temporal stability."
definitions:
  - term: "DynEC"
    definition: "Dynamic Evolutionary Clustering, the proposed framework."
  - term: "GNN"
    definition: "Graph Neural Network."
  - term: "GST-GNN"
    definition: "Gated Spatio-Temporal Graph Neural Network."
  - term: "cDTW"
    definition: "Constrained Dynamic Time Warping."
  - term: "CSR"
    definition: "Cluster Switching Rate, a metric for temporal stability."
  - term: "ARI"
    definition: "Adjusted Rand Index, a metric for clustering quality against ground truth."
  - term: "V2G"
    definition: "Vehicle-to-Grid, bi-directional power flow."
  - term: "DR"
    definition: "Demand Response."
  - term: "AMI"
    definition: "Advanced Metering Infrastructure."
  - term: "GRU"
    definition: "Gated Recurrent Unit."
  - term: "GAT"
    definition: "Graph Attention Network."
  - term: "KL"
    definition: "Kullback-Leibler divergence."
  - term: "MSE"
    definition: "Mean Squared Error."
critical_citations:
  - "[Chakrabarti et al., 2006] — Formalized evolutionary clustering with snapshot quality and temporal cost."
  - "[Berndt and Clifford, 1994] — Foundation for DTW in time-series alignment."
  - "[Sakoe and Chiba, 1978] — Introduced Sakoe-Chiba bands for cDTW."
  - "[Rousseeuw, 1987] — Defined the Silhouette Coefficient for clustering evaluation."
  - "[Wu et al., 2019] — Graph WaveNet for spatio-temporal forecasting."
  - "[Pareja et al., 2020] — EvolveGCN for dynamic graph evolution."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Introduces dynamic profiling approach for power users, analogous to financial behavior."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "high"
      justification: "Addresses the dynamics of user profiles and concept drift in load behavior."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "Proposes a novel clustering algorithm for dynamic user profiles."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Focuses on load profiling, a foundational task for forecasting."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Uses ST-GNN and GRU to model sequential load data for forecasting."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "low"
      justification: "The method reduces false identity switching, which is relevant to anomaly detection."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "low"
      justification: "The proposed method uses robust clustering to handle anomalies in load data."
    - code: "8.C"
      name: "Cold‑Start Baseline Strategies for Anomaly Detection"
      relevance: "contextual"
      justification: "Uses pre-training and self-training, concepts relevant for cold-start scenarios."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "low"
      justification: "Discusses data privacy in smart grids but not as a primary focus."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "low"
      justification: "The stability of profiling contributes to user trust in the system."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Uses a dual-metric system (ARI, SC, DBI, CSR) for holistic evaluation."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Conducts ablation and sensitivity analysis for different architectural components."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "medium"
      justification: "The evaluation approach is suitable for systems with dynamic recommendations."
  contribution: "DynEC's multi-view graph construction provides a robust way to model complex user relationships in a PFMS, addressing the cold-start problem by capturing similarities even with limited data. The evolutionary clustering framework with temporal smoothness is directly applicable to behavioral profiling and classification in Odin, enabling stable and reliable user segmentation. The dual-objective optimization strategy offers a principled method to balance snapshot accuracy with temporal consistency, which is crucial for forecasting and anomaly detection modules. The evaluation framework, including metrics like CSR and event-driven validation, provides a template for assessing the stability of Odin's clustering and recommendation modules. Finally, the focus on reducing false identity switching directly supports user trust and long-term retention by ensuring the system behaves predictably."
  directly_justifies:
    - "Dynamic evolutionary clustering should be used to track concept drift in user behavior."
    - "Multi-view graph construction with cDTW is necessary for handling temporal misalignments in user data."
    - "A dual-objective loss balancing snapshot quality and temporal smoothness improves system stability."
    - "Cluster Switching Rate (CSR) is an essential metric for evaluating user profile stability."
    - "GRU-based memory modules are effective for maintaining user identity during concept drift."
  limits:
    - "The framework is evaluated on electricity load data, not financial transaction data, which may have different patterns."
    - "The study does not address user-defined allocation constraints, a key feature of a PFMS."
    - "The model's performance on extremely stable data is slightly lower than static methods, indicating a trade-off."
    - "The self-training strategy relies on pre-defined number of clusters, which may not be known in advance."
  mapping_rationale: "All 12 functional domains were systematically scanned for relevance to Odin. The paper is directly relevant to the Behavioral Profiling & Classification domain, specifically topics 5.B (Profile Dynamics) and 6.B (Forecasting Algorithms for Sequential Spending Data), both rated high due to the paper's focus on tracking concept drift and using sequential models. Topics 5.A, 5.C, 6.A, 12.A, and 12.B were rated medium as they provide supporting concepts or evaluation frameworks. Topics 8.A, 8.B, 10.A, 10.B, and 12.C were rated low or contextual as they are tangentially related. Domains like Filipino Cultural Context, Expense Categorization, Budget Recommendation, and Savings & Debt Management were considered but rejected because the paper does not address cultural or financial-specific features, user-defined constraints, or budgeting strategies. The paper's overall relevance to Odin is high, providing a robust methodology for dynamic user profiling and a structured evaluation approach."
limitations:
  - "The paper uses electricity load data, which may not directly generalize to financial spending patterns. [unacknowledged]"
  - "There is a slight performance trade-off in highly stable environments, where static methods can be marginally more accurate on a single snapshot. [acknowledged]"
  - "The framework does not incorporate user-defined constraints or goals, which are central to a PFMS. [unacknowledged]"
  - "The self-training strategy assumes the number of clusters is known, which may not be the case in a real-world PFMS. [acknowledged]"
remember_this:
  - "DynEC uses multi-view graphs with cDTW to handle temporal misalignment in user data."
  - "A dual-objective loss balances snapshot quality and temporal consistency to reduce identity switching."
  - "The framework reduces Cluster Switching Rate to 0.02-0.04, far lower than static methods."
  - "Ablation studies show the cDTW view is the most critical component for clustering quality."
  - "The GRU memory module effectively maintains user identity during concept drift events."
```
---

## Paper 40: Yu_summarized.md

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

## Paper 41: Jouini et al_summarized.md

**Source File:** `Jouini et al_summarized.md`

```yaml
paper_id: "10.1080/24751839.2026.2674344"
designation: "international-algorithm-specific"
title: "Drift-driven collaborative learning for non-stationary time series: a COVID-19 case study"
authors: "Jouini, K.; Jemili, F.; Korbaa, O."
year: 2026
venue: "Journal of Information and Telecommunication"
odin_topics:
  - "6.A"
  - "6.B"
  - "8.A"
  - "8.B"
tldr: "Proposes an eager incremental regression tree and a collaborative framework combining incremental and batch learners to improve forecasting under concept drift, validated on COVID-19 data."
problem_and_motivation: "Conventional batch forecasting models degrade under concept drift, while incremental models have trade-offs in accuracy and adaptability. Existing approaches treat batch and incremental learning as mutually exclusive, failing to combine their complementary strengths. This limits effective forecasting of non-stationary time series such as pandemic data."
approach:
  - "EFRT-DD: an eager incremental regression tree that continuously revisits split decisions to maintain structural alignment with evolving data."
  - "CDR: a collaborative framework that integrates an incremental regressor (EFRT-DD) and a batch regressor (decision tree), coordinated by ADWIN drift detector."
  - "ADWIN maintains a variable-length window to detect concept drifts and triggers retraining of batch model on recent data."
  - "The framework dynamically selects the best-performing model over a sliding window of recent observations for inference."
  - "Evaluation uses prequential protocol on COVID-19 data from 219 countries, with MAE and RMSE metrics."
  - "Comparison against state-of-the-art incremental trees (HT, HAT, FIMT-DD) and batch decision tree."
findings:
  - "num: EFRT-DD improves RMSE for deaths by 2.38% and MAE by 8.91% over FIMT-DD on world data."
  - "num: CDR further improves over FIMT-DD: 3.61% RMSE and 14.77% MAE for deaths on world data."
  - "num: On Tunisia data, EFRT-DD reduces RMSE by 55.1% and MAE by 62.8% for deaths compared to FIMT-DD."
  - "num: CDR outperforms batch decision tree by 131.61% average RMSE improvement for deaths on world data."
  - "EFRT-DD is 5-6 times slower than FIMT-DD due to continuous reevaluation."
  - "Country-specific training yields higher gains than multi-country training due to asynchronous drifts."
key_figures_tables:
  - "Table 1: Comparison of MAE and RMSE for incremental learners and CDR on world and Tunisia data → CDR achieves lowest errors."
  - "Figure 3: MAE over time for daily new confirmed cases → CDR consistently outperforms incremental learners."
  - "Figure 4: MAE over time for deaths → CDR shows superior tracking of changes."
  - "Table 2: Batch decision tree vs CDR for cases over 9 milestones → CDR significantly better in all milestones."
key_equations:
  - equation: "e = sqrt( R^2 * ln(1/delta) / (2n) )"
    explanation: "Hoeffding bound for confidence in split decisions."
  - equation: "SDR(X) = sd(l) - (N_l/N) sd(l) - (N_r/N) sd(r)"
    explanation: "Standard deviation reduction for split evaluation."
  - equation: "sd(node) = sqrt( (1/N) * sum(y_i - \\bar{y})^2 )"
    explanation: "Standard deviation of target in a node."
  - equation: "epsilon_cut = sqrt( (1/(2m)) * ln(4|W|/delta) )"
    explanation: "ADWIN cut threshold for drift detection."
definitions:
  - term: "Concept drift"
    definition: "Change in the underlying data-generating process over time."
  - term: "Incremental learning"
    definition: "Model trained continuously on sequential data, updating as new samples arrive."
  - term: "Batch learning"
    definition: "Model trained on a fixed dataset, requiring retraining for updates."
  - term: "Prequential evaluation"
    definition: "Testing each data point sequentially before using it for training."
  - term: "ADWIN"
    definition: "Adaptive sliding window algorithm for detecting concept drift."
  - term: "EFRT-DD"
    definition: "Extremely Fast Regression Tree with Drift Detection, an eager incremental tree."
  - term: "CDR"
    definition: "Collaborative Drift-Driven Regression, a framework combining incremental and batch learners."
critical_citations:
  - "[Domingos & Hulten, 2000] — Introduced Hoeffding Tree for stream mining."
  - "[Ikonomovska et al., 2011] — Proposed FIMT-DD, a state-of-the-art incremental regression tree."
  - "[Bifet & Gavaldà, 2007] — Developed ADWIN drift detection method."
  - "[Manapragada et al., 2018] — Proposed extremely fast decision tree with eager splitting."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "The paper presents predictive modeling for non-stationary time series, directly applicable to spending forecasting."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Proposes two forecasting algorithms (EFRT-DD and CDR) that adapt to concept drift, suitable for spending data."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "low"
      justification: "Drift detection techniques can be repurposed for anomaly detection, but the paper does not address spending anomalies."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "low"
      justification: "The collaborative framework and drift detection are algorithmic approaches that could inform anomaly detection."
  contribution: "This work justifies the use of incremental learning for Odin's spending forecasting module to adapt to changing user behavior. The collaborative framework supports a hybrid approach combining real-time updates with periodic batch retraining, balancing accuracy and responsiveness. The drift detection mechanism can be integrated into Odin's anomaly detection module to identify shifts in spending patterns. The eager induction strategy demonstrates that revisiting model structure improves long-term predictive performance, which informs the design of adaptive algorithms in Odin."
  directly_justifies:
    - "Incremental models with eager splitting can better track concept drifts than lazy trees."
    - "Collaborative frameworks combining incremental and batch learners improve predictive performance under non-stationarity."
    - "Drift detection using ADWIN effectively identifies changes in data distribution, enabling timely model updates."
  limits:
    - "None identified."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was found most relevant to the Spending Forecasting domain (codes 6.A and 6.B) because it directly proposes algorithms for non-stationary time series prediction. It also touches on Anomaly Detection (8.A and 8.B) through its drift detection component, but with low relevance as it does not address spending anomalies. Other domains such as Expense Categorization, Behavioral Profiling, Budget Recommendation, and Savings/Debt were considered but rejected as the paper does not provide any citeable claims for those areas. The overall relevance is moderate, providing algorithmic insights for adaptive forecasting and drift detection that could be applied to Odin's modules."
limitations:
  - "Evaluation relies on retrospectively consolidated datasets, which may not reflect real-time operational uncertainties such as reporting delays or data revisions."
  - "The focus on pandemic data leaves external validity across other non-stationary domains, including personal finance, unconfirmed. [unacknowledged]"
  - "Computational overhead of eager splitting may be a challenge for high-throughput environments."
remember_this:
  - "EFRT-DD's eager splitting improves forecasting by continuously adapting tree structure."
  - "CDR combines incremental agility with batch accuracy to outperform standalone models."
  - "Drift detection enables timely model updates in response to changing data distributions."
  - "Country-specific modeling yields better performance than global training due to asynchronous drifts."
```
---

## Paper 42: Uppal et al_summarized.md

**Source File:** `Uppal et al_summarized.md`

```yaml
paper_id: 10.1007/s44163-026-00949-2
designation: international-algorithm-specific
title: Translating artificial intelligence into socio-economic insight: a hybrid deep learning approach to employee financial well-being
authors: Uppal, A.; Srivastava, A.; Awasthi, Y.; Srivastava, A.; Kakkar, B.
year: 2026
venue: Discover Artificial Intelligence
odin_topics:
  - 1.C
  - 3.A
  - 5.A
  - 5.B
  - 5.C
  - 6.B
  - 7.B
  - 8.B
  - 12.A
  - 12.B
tldr: Hybrid deep learning models classify individuals into three financial well-being categories, with Wide & Deep + CNN achieving the highest performance.
problem_and_motivation: Conventional financial well-being assessments rely on static, reactive indicators that fail to capture dynamic financial behavior and scale efficiently. There is a gap between advanced AI modeling techniques and their practical application for understanding individual financial stress in organizational contexts.
approach:
  - Data source includes 20,000 Indian individuals with structured financial and demographic features.
  - New features like Savings Ratio and Debt Ratio were engineered to provide normalized behavioral insights.
  - Fifteen deep learning models were implemented, including CNN, RNN, GRU, BiLSTM, and Wide & Deep networks.
  - Hybrid models were constructed by integrating Wide & Deep with CNN, BiLSTM, RNN, and Attention mechanisms.
  - TabNet was used for feature importance analysis to enhance model explainability.
findings:
  - num: The hybrid Wide & Deep + CNN model achieved a validation accuracy of 99.44% and a perfect ROC-AUC of 1.0000.
  - num: Debt Ratio was the most influential feature, accounting for nearly 50% of the decision weight in the TabNet model.
  - num: A strong correlation (r = 0.89) was found between grocery expenses and grocery savings potential.
  - BiLSTM and GRU models achieved perfect precision, recall, and F1-scores of 1.00 for certain financial health categories.
  - Models capable of both memorization and sequence modeling outperformed simpler architectures on financial behavior data.
key_figures_tables:
  - Table 2: Performance comparison of deep learning models → Wide & Deep + CNN shows superior validation accuracy and low loss.
  - Figure 4: Correlation heatmap of numerical features → Income is highly correlated with groceries, insurance, and healthcare expenses.
  - Figure 5: Correlation heatmap of potential saving features → Savings potential across categories shows moderate to strong positive correlations.
  - Figure 7: Feature importance using TabNet → Debt ratio and savings ratio are the most important predictors of financial well-being.
  - Figure 9: ROC-AUC score of financial health prediction models → Hybrid models, especially Wide & Deep + CNN, achieve perfect discrimination.
key_equations:
  - equation: $y = \sigma(W^T_{wide} x + W^T_{deep} \phi(x))$
    explanation: Prediction combining wide linear and deep nonlinear components.
definitions:
  - term: CNN
    definition: Convolutional Neural Network for extracting local feature hierarchies.
  - term: RNN
    definition: Recurrent Neural Network for modeling sequential data.
  - term: GRU
    definition: Gated Recurrent Unit for efficient sequential modeling.
  - term: BiLSTM
    definition: Bidirectional Long Short-Term Memory for capturing long-range dependencies.
  - term: TabNet
    definition: A deep learning model with sequential attention for tabular data.
  - term: ROC-AUC
    definition: Receiver Operating Characteristic - Area Under the Curve for classification performance.
critical_citations:
  - "[Ghashti & Thompson, 2023] — Foundational study on financial segmentation using clustering."
  - "[Polyzos et al., 2021] — Modeling subjective well-being effects of systemic shocks."
  - "[Khunger, 2022] — Deep learning for financial stress testing with CNN-LSTM."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: contextual
      justification: The paper presents a behavioral profiling framework applicable to understanding financial behaviors.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: The dataset includes detailed expense categories for financial analysis.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: The core contribution is classifying individuals into distinct financial well-being profiles.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: medium
      justification: The model classifies users based on static data, which relates to initial profile establishment.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: The paper extensively evaluates deep learning classifiers for financial profile classification.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: The paper explores sequence modeling architectures, though data is not explicitly temporal.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: contextual
      justification: The model's classification could inform budget recommendations, but this is not directly addressed.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: The approach uses deep learning to identify patterns, which has conceptual overlap with anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: The study employs rigorous evaluation metrics including accuracy, precision, recall, F1, and ROC-AUC.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: The paper systematically compares 15 algorithmic models for financial classification.
  contribution: The paper provides a validated deep learning pipeline for classifying financial well-being, which can be adapted for Odin's user profiling module. Its feature engineering approach, particularly the use of debt and savings ratios, informs Odin's expense categorization and behavioral classification design. The performance comparison of hybrid models offers guidance for selecting appropriate algorithms for Odin's recommendation and forecasting components. The emphasis on model interpretability using TabNet aligns with Odin's need for transparent decision support.
  directly_justifies:
    - Hybrid deep learning models can classify financial well-being with high accuracy.
    - Debt ratio is a critical feature for predicting financial stress.
    - Savings potential exhibits strong correlations across spending categories.
    - TabNet provides interpretable feature importance for financial classification.
  limits:
    - The dataset lacks temporal sequences or longitudinal financial behaviors.
    - The data is geographically and culturally confined to Indian individuals.
    - Some hybrid models showed instability due to architectural incompatibilities.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was found to be highly relevant to the Behavioral Profiling & Classification domain (5.A, 5.B, 5.C) because its core contribution is classifying individuals into financial well-being profiles using deep learning. It was also highly relevant to System Evaluation (12.A, 12.B) due to its comprehensive benchmarking of 15 models and use of standard metrics. Medium relevance was assigned to Expense Categorization (3.A) for its detailed expense feature set and Profile Dynamics (5.B) for initial user classification. The Spending Forecasting (6.B) and Budget Recommendation (7.B) domains were considered contextual, as the paper focuses on classification rather than prediction or optimization. Anomaly Detection (8.B) was also contextual, as the approach identifies patterns rather than anomalies. Domains like Filipino Cultural Context, Mobile-First Design, Data Privacy, and Savings & Debt Management were rejected as the paper does not address cultural specificity, UX, privacy, or explicit savings/debt management strategies. Overall, the paper provides strong justification for using hybrid deep learning in financial profiling modules but has limited direct applicability to Odin's specific Filipino context and design requirements.
limitations:
  - Data lacks temporal sequences for modeling behavioral dynamics. [unacknowledged]
  - Generalizability to other populations is limited due to geographic confinement to India.
  - CNN-based models underperformed on non-spatial tabular data.
  - Interpretability remains a challenge for AI-averse stakeholders.
remember_this:
  - Wide & Deep + CNN achieved 99.44% validation accuracy.
  - Debt ratio was the most influential predictor of financial well-being.
  - BiLSTM and GRU models reached perfect classification metrics.
  - Hybrid architectures outperformed standalone models on financial data.
  - Behavioral features like savings potential were more important than income.
```
---

## Paper 43: Breza & Kaur_summarized.md

**Source File:** `Breza & Kaur_summarized.md`

```yaml
paper_id: a8c9f2d1-4e5b-4a7d-9c3f-2b8d1e4f6a7b
designation: international
title: Psychology and Development: Applications from Cognitive and Social Psychology
authors: Breza, E.; Kaur, S.
year: 2026
venue: National Bureau of Economic Research
odin_topics:
  - "1.A"
  - "1.B"
  - "1.C"
  - "2.A"
  - "2.B"
  - "2.C"
  - "2.D"
  - "3.A"
  - "4.A"
  - "4.B"
  - "5.A"
  - "5.B"
  - "5.C"
  - "6.A"
  - "6.B"
  - "7.A"
  - "7.B"
  - "8.A"
  - "8.B"
  - "9.A"
  - "9.B"
  - "10.A"
  - "10.B"
  - "11.A"
  - "11.B"
  - "12.A"
  - "12.B"
  - "12.C"
  - "13.A"
  - "13.B"
  - "13.C"
tldr: A comprehensive research agenda for behavioral development economics, arguing that psychological constraints (self-control, cognition, self-beliefs, mental health, social norms) are amplified by poverty's features and shape both individual poverty traps and market functioning.
problem_and_motivation: Development economics has focused on external constraints like missing markets, but internal psychological constraints may similarly impede escaping poverty and may be amplified by poverty's core features. Understanding whether these psychological channels play a first-order role in perpetuating poverty and shaping informal institutions is a critical, underexplored question for the field.
approach:
  - Reviews evidence across five psychological constructs: self-control, cognitive constraints, self-beliefs, mental health, and social norms.
  - Applies a missing markets lens to argue why behavioral aids are under-supplied, justifying policy intervention to correct market failures.
  - Identifies five features of poverty (proximity to subsistence, high volatility, market failures, weak institutions, reliance on social ties) that amplify the consequences of psychological constraints.
  - Highlights where evidence is merely a proof of concept versus where meaningful impacts on education, investment, and earnings have been demonstrated.
  - Advocates for a complementary research approach that starts from broad stylized facts in developing countries (e.g., ROSCAs, high-interest debt cycles) and uses behavioral tools to unpack them.
findings:
  - num: Evidence for self-control problems is widespread, with commitment device take-up ranging from 11% to 36% in various field experiments.
  - num: Hard commitment devices can lower welfare due to naivete, with 66% of smokers in one study forfeiting savings, but learning over time can improve welfare.
  - num: Cognitive constraints, like retrieval failures, can lead to 20% higher savings and 9% higher yields through simple interventions prompting recall of future expenses.
  - num: Cash on hand can improve worker productivity by 7% and reduce attentional mistakes by reducing financial worries.
  - Interventions targeting self-beliefs (aspirations, self-efficacy) can have large, persistent impacts, such as a 0.09 standard deviation increase in math scores for teachers' students.
  - Psychotherapy for depression in Pakistan led to 0.2-0.3 standard deviation increases in parental investments in children.
  - Social norms act as powerful determinants of equilibrium outcomes, with 33% of workers accepting a job at the prevailing wage but only 1.8% accepting a 10% wage cut when socially observable.
  - The kin tax or social tax can distort labor supply, with workers being 10-11% more productive when their earnings are hidden from social networks.
  - Inter-group contact improves attitudes but effects on generalized prejudice are modest, often limited to the specific domain of contact.
key_figures_tables:
  - "Table 1: Summary of psychological constructs and their relevance to poverty → Provides a structured overview of key mechanisms and evidence."
  - "Figure 3.1: Payday effect on worker output → Illustrates cyclicality in effort consistent with self-control problems."
key_equations:
  - equation: "U = u(c_0) + β Σ_{t=1}^{T} δ^t u(c_t)"
    explanation: "Quasi-hyperbolic discounting function with present bias β."
definitions:
  - term: "Behavioral Aids"
    definition: "Tools, products, or services that mitigate the impacts of psychological constraints."
  - term: "Soft Commitment"
    definition: "Commitment devices relying on non-monetary costs like social pressure or internal psychological costs."
  - term: "Cognitive Endurance"
    definition: "The ability to sustain performance over time during a cognitively effortful task."
  - term: "Kin Tax"
    definition: "Redistributive pressures from family and social networks that can tax individual savings and earnings."
  - term: "Pluralistic Ignorance"
    definition: "A situation where individuals privately reject a norm but mistakenly assume others endorse it."
critical_citations:
  - "[Ashraf et al., 2006] — Foundational field experiment on commitment savings in the Philippines."
  - "[Mani et al., 2013] — Key evidence on poverty and cognitive function."
  - "[Hanna et al., 2014] — Demonstrates persistent learning failures due to selective attention."
  - "[Kaur et al., 2015] — Evidence for self-control problems and commitment demand in labor supply."
  - "[Kremer et al., 2019] — Previous review of behavioral development economics."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "contextual"
      justification: "Paper discusses poverty broadly, but not specifically Filipino young professionals."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "contextual"
      justification: "Discusses irregular income and expenditure shocks relevant to financial structure, but not specific to Filipinos."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "medium"
      justification: "Reviews financial behaviors (savings, borrowing, labor supply) relevant to understanding this demographic's behavior."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "medium"
      justification: "Discusses ROSCAs, susu collectors, and other culturally specific financial practices common in developing countries."
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "high"
      justification: "Dedicated section on seasonal poverty, hungry seasons, and harvest cycles directly informs this topic."
    - code: "2.C"
      name: "User-Declared Financial Preferences"
      relevance: "medium"
      justification: "Discusses how poverty affects time preferences and financial decision-making, relevant to user preferences."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "low"
      justification: "Reviews seasonal and cyclical spending broadly, but does not specifically mention Filipino 'occasions'."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "medium"
      justification: "Discusses mental accounting as a cognitive shortcut, which is a form of expense categorization."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews existing systems like microfinance, ROSCAs, and commitment savings products."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Directly discusses limitations of formal and informal financial systems, including missing markets for behavioral aids."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Discusses heterogeneity in self-control and its correlation with commitment demand."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "medium"
      justification: "Discusses learning about self-control problems and the challenges of initial measurement, related to cold-start."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "low"
      justification: "Discusses using payday effects and commitment take-up as proxies but not classification methods."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "low"
      justification: "Provides evidence of predictable patterns (e.g., payday effects, seasonal savings) that could inform forecasting models."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "low"
      justification: "Does not address specific forecasting algorithms, only behavioral patterns relevant to forecasting."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "medium"
      justification: "Discusses mental accounting and label-based savings as informal budgeting strategies."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Provides evidence on expense under-estimation, informing how budget recommendations might need to address retrieval failures."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "low"
      justification: "Does not directly address anomaly detection but discusses behavioral patterns that could be flagged as anomalies."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "low"
      justification: "No discussion of specific algorithms for anomaly detection."
    - code: "9.A"
      name: "Mobile‑First Design Principles and Rationale"
      relevance: "low"
      justification: "No direct discussion of mobile design."
    - code: "9.B"
      name: "Mobile UX Design for Personal Finance"
      relevance: "low"
      justification: "No direct discussion of mobile UX."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "low"
      justification: "No direct discussion of data privacy."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses trust as a barrier to commitment devices and formal financial services."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "medium"
      justification: "Discusses reminders and soft commitments as engagement mechanisms."
    - code: "11.B"
      name: "Retention Mechanisms and Engagement Design"
      relevance: "medium"
      justification: "Discusses learning dynamics and the design of commitment devices for sustained behavior change."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses challenges in evaluating welfare effects of interventions."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "low"
      justification: "No direct discussion of algorithmic evaluation."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "low"
      justification: "Does not discuss budget recommendation system evaluation."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "high"
      justification: "Extensive review of commitment devices, savings groups, and goal-setting interventions directly informs this topic."
    - code: "13.B"
      name: "Debt Management in PFMS"
      relevance: "medium"
      justification: "Discusses high-interest debt cycles and microfinance as a potential commitment device."
    - code: "13.C"
      name: "End‑of‑Period Surplus as a Savings Input"
      relevance: "low"
      justification: "Discusses post-harvest savings but not the specific mechanism of surplus as input."
  contribution: "Odin's design of behavioral profiles is supported by this paper's review of self-control heterogeneity and its link to commitment demand, informing both profile creation and forecasting. The paper's discussion of cognitive constraints and retrieval failures directly justifies Odin's need for modules that help users recall expenses and set realistic budgets. Its review of soft commitments and social signaling provides a rationale for designing engagement features that leverage social norms and peer support to improve user retention. The paper's emphasis on the welfare consequences of psychological constraints and the role of missing markets offers a framework for evaluating Odin's impact on user financial health. Finally, its analysis of mental accounting and goal setting validates Odin's focus on user-defined allocation constraints and savings goal management."
  directly_justifies:
    - "Poverty amplifies the consequences of cognitive and self-control failures, making behavioral aids particularly valuable for low-income users."
    - "Soft commitments like mental accounting can be as effective as hard commitments and avoid welfare losses from naivete."
    - "Reminders and salience interventions can significantly improve savings and other forward-looking behaviors."
    - "Social norms and image concerns are powerful drivers of behavior that can be harnessed for positive change."
    - "Users may systematically underestimate future expenses, a key insight for designing budget recommendations."
  limits:
    - "The paper is a review and does not present new empirical findings or test specific algorithms."
    - "The focus is on developing countries broadly, not specifically the Filipino context, requiring contextual adaptation."
    - "Evidence for some constructs (e.g., psychology of poverty mechanisms) remains nascent and proof-of-concept, limiting direct design implications."
  mapping_rationale: "A systematic scan across all 12 functional domains was conducted. Domains flagged as highly relevant include Expense Categorization, Existing Systems & Gaps, Behavioral Profiling, Budget Recommendation, and Savings & Debt Management due to the paper's extensive review of self-control, cognitive constraints, mental accounting, and financial behaviors. Medium relevance was assigned to Filipino Cultural Context and User Retention & Engagement, as the paper discusses social norms and practices common in developing countries but not specifically Filipino, and engagement mechanisms like reminders and soft commitments. Topics like Data Privacy & User Trust and Mobile‑First Design received low relevance as they are not directly addressed. Borderline cases included seasonal spending patterns (2.B and 2.D), where the paper's general discussion of seasonality was applied to both, and user constraints (3.C and 7.B), where the paper's discussion of cognitive failures and under-estimation of expenses was seen as relevant to both allocation constraints and budget design. The paper is highly relevant to Odin, providing a broad theoretical and empirical foundation for its core modules."
limitations:
  - "Much of the evidence for the psychology of poverty remains at the proof-of-concept stage, not yet demonstrating first-order economic impacts. [unacknowledged]"
  - "The paper does not provide specific guidance on how to measure or operationalize many of the discussed psychological constructs in a PFMS. [unacknowledged]"
  - "The potential for interventions to be scaled and integrated into a digital product is not thoroughly explored. [unacknowledged]"
  - "There is limited discussion of potential negative side effects or unintended consequences of behavioral interventions. [unacknowledged]"
remember_this:
  - "Poverty's features amplify psychological constraints, making behavioral aids critical for financial health."
  - "Soft commitments like mental accounting can be powerful tools for behavior change without high welfare costs."
  - "Cognitive constraints, especially retrieval failures, cause systematic underestimation of future expenses."
  - "Social norms and image concerns are powerful drivers of financial behavior, both positive and negative."
  - "Interventions targeting self-beliefs show meaningful, long-term impacts on education and earnings."
```
---

## Paper 44: Nduka & Benedicto_summarized.md

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

## Paper 45: Noel et al_summarized.md

**Source File:** `Noel et al_summarized.md`

```yaml
paper_id: 10.3389/frai.2026.1705245
designation: local-algorithm-specific
title: Small LLMs can be good coldstart recommenders
authors: Noel, J.; Monterola, C.; Tan, D. S.
year: 2026
venue: Frontiers in Artificial Intelligence
odin_topics:
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 8.C
  - 9.A
  - 12.B
tldr: Fine-tuned small language models with under 2B parameters using LoRA achieve competitive or superior sequential recommendation performance compared to standard models, especially in cold-start settings.
problem_and_motivation: Standard sequential recommendation models suffer in cold-start scenarios due to limited user interaction histories. Large language models (LLMs) have shown promise for recommendation but are computationally infeasible for most organizations.
approach:
  - Fine-tuned two small open-source LLMs, Danube-1.8B and Gemma-2B, using Low-Rank Adaptation (LoRA) for sequential recommendation.
  - The models were evaluated on the MovieLens10M and Yoochoose-clicks datasets, using only item IDs from short interaction sequences of length 5.
  - LoRA was used to update less than 0.5% of the original model parameters, enabling fine-tuning on consumer-grade GPUs.
  - Converted sequential interaction data into prompts for causal language modeling.
  - Compared performance against GRU4Rec, SASRec, and BERT4Rec in a cold-start scenario.
findings:
  - num: Fine-tuned LLMs achieved up to 8.7% higher HitRate@1 compared to the best baseline (Danube vs. BERT4Rec on MovieLens).
  - LLMs predict item IDs that are textually and numerically closer to input sequence IDs, as measured by lower average Hamming distance and deviation.
  - The tokenization of numeric item IDs into digit-level tokens creates a numeric bias that the LLMs exploit for predictions.
  - Despite digit-level bias, the LLMs also learn meaningful sequential co-occurrence patterns beyond simple numeric proximity.
  - LLMs scale independently of catalog size as they avoid a separate, linearly growing item-embedding matrix.
key_figures_tables:
  - Table 4: Comparison of HitRate@1, average distance, and deviation → LLMs outperform baselines on both datasets in cold-start settings.
  - Table 5: Example of tokenization for Gemma and Danube → Item IDs are tokenized into digit-level tokens, not atomic symbols.
  - Table 6: Sample correct predictions not numerically close to inputs → LLMs learn non-trivial sequential patterns beyond numeric bias.
  - Table 7: Results of different input sequence lengths on MovieLens → Unlike GRU4Rec, small LLM performance does not improve with longer histories.
key_equations:
  - equation: \max_{\theta} \sum_{(x,y) \in Z} \sum_{t=1}^{|y|} \log(P_\theta(y_t | x, y_{<t}))
    explanation: Standard causal language modeling objective for LLM fine-tuning.
  - equation: \max_{\Phi} \sum_{(x,y) \in Z} \sum_{t=1}^{|y|} \log(P_{\theta+\Phi}(y_t | x, y_{<t}))
    explanation: LoRA fine-tuning objective updating only low-rank matrix Phi.
definitions:
  - term: LoRA
    definition: Low-Rank Adaptation, a parameter-efficient fine-tuning technique that adds trainable low-rank matrices to a pretrained model.
  - term: Cold-start
    definition: A recommendation scenario where new users or items have limited historical interaction data.
  - term: Sequential Recommendation
    definition: Predicting the next item a user will interact with based on their sequence of past interactions.
critical_citations:
  - "[Singer et al., 2024] — Defines the Danube-1.8B small LLM architecture."
  - "[Team et al., 2024] — Defines the Gemma-2B small LLM architecture."
  - "[Hu et al., 2022] — Introduces LoRA used for efficient fine-tuning."
  - "[Hidasi et al., 2016] — Defines the GRU4Rec baseline model."
  - "[Wang-Cheng Kang, 2018] — Defines the SASRec baseline model."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: Provides a general context for cold-start problems in user profiling.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Shows that small LLMs can classify user behavior from short sequences, akin to profile classification.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Demonstrates a predictive modeling approach (LLM-based) for sequential spending-like data.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Evaluates LLMs as forecasting algorithms for sequential item prediction, analogous to spending prediction.
    - code: 8.C
      name: Cold‑Start Baseline Strategies for Anomaly Detection
      relevance: high
      justification: The paper's core focus on cold-start recommendation directly informs baseline strategies for anomaly detection.
    - code: 9.A
      name: Mobile‑First Design Principles and Rationale
      relevance: medium
      justification: The use of small, efficient models aligns with the computational constraints of mobile deployment.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: The paper provides a direct evaluation framework (HitRate, tokenization analysis) for an algorithmic module (LLM-based recommender).
  contribution: "This paper directly validates the use of small LLMs (under 2B parameters) for the sequential recommendation task, a key component of Odin's forecasting module. It shows that these models, fine-tuned with LoRA, are computationally feasible on consumer hardware, which supports Odin's mobile-first design. The findings that LLMs perform well in cold-start scenarios offer a concrete strategy for Odin's cold-start baselines for both recommendation and anomaly detection."
  directly_justifies:
    - "Fine-tuned small LLMs under 2B parameters can be effective for sequential recommendation."
    - "LoRA enables efficient fine-tuning of LLMs with less than 0.5% of parameters trainable."
    - "LLMs avoid a separate item-embedding matrix, maintaining a constant memory footprint regardless of catalog size."
    - "Short historical sequences (length 5) are sufficient for small LLMs to make good predictions in a cold-start setting."
  limits:
    - "The study only uses two datasets (MovieLens, Yoochoose) which may not fully represent financial spending data. [unacknowledged]"
    - "The LLM's reliance on numeric ID tokenization may be a limitation if item IDs are not numeric or sequentially ordered. [unacknowledged]"
    - "Inference latency (34-59 ms/token) is slower than traditional models like GRU4Rec, which could be a constraint for real-time mobile applications. [acknowledged]"
    - "The study does not compare with state-of-the-art large LLMs (e.g., PaLM, Llama-3) to benchmark performance loss."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant primarily for the 'Spending Forecasting' (6.A, 6.B) domain due to its focus on sequential prediction, the 'Behavioral Profiling & Classification' (5.A, 5.C) domain for its cold-start recommendation which is analogous to user profile classification, and the 'Anomaly Detection' (8.C) domain for its direct treatment of the cold-start problem. It also touches on 'Mobile‑First Design' (9.A) due to the efficiency of the small models and 'System Evaluation' (12.B) for its empirical methodology. The paper was rejected for domains like 'Expense Categorization' (3.A) as it does not deal with categorizing items, and 'Data Privacy & User Trust' (10.A) as it offers no insights on those topics. Its relevance is high for the cold-start aspects of forecasting and anomaly detection, and medium for informing mobile deployment and evaluation frameworks."
limitations:
  - "Generalizability to non-numeric or non-sequential item IDs is not discussed. [unacknowledged]"
  - "The computational cost of fine-tuning is not compared to the cost of training baselines from scratch. [unacknowledged]"
  - "The study does not explore the use of LLMs for feature augmentation or dataset augmentation."
remember_this:
  - "Small LLMs can outperform standard recommenders in cold-start settings."
  - "LoRA fine-tuning updates less than 0.5% of small LLM parameters."
  - "LLMs maintain a fixed memory footprint independent of item catalog size."
  - "Small LLMs achieved up to 8.7% higher HitRate@1 on MovieLens."
  - "Short interaction histories are sufficient for effective cold-start predictions."
```
---

## Paper 46: Mercado M. et al_summarized.md

**Source File:** `Mercado M. et al_summarized.md`

```yaml
paper_id: 10.46932/sfjdv7n4-005
designation: local # Published in a Philippine university
title: The importance of financial literacy for young adults: a guide to smart money management
authors: Mercado, M. D.; Castillo, A. P.; Araves, J. A.
year: 2026
venue: South Florida Journal of Development
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 4.A
  - 4.B
  - 10.A
  - 10.B
tldr: Financial literacy is essential for young adults to avoid debt, build savings, and achieve life goals, yet most lack formal education in this area.
problem_and_motivation: Young adults face complex financial decisions early in life but lack foundational financial knowledge. This gap between responsibility and education leads to avoidable debt, stress, and delayed life milestones. The article addresses the urgent need for accessible financial literacy resources.
approach:
  - Reviews global surveys and national datasets to identify common financial challenges for young adults.
  - Compiles statistics from OECD, FINRA, Bankrate, and Federal Reserve to quantify the literacy gap.
  - Presents a practical money management guide covering budgeting, saving, debt, and investing.
  - Analyzes psychological barriers like financial stress and low self-efficacy.
  - Proposes solutions involving digital tools, community programs, and policy changes.
findings:
  - "num: 65% of young adults struggle to repay student loan debt."
  - "num: 58% live paycheck to paycheck."
  - "num: 54% have no emergency savings."
  - "num: Only 31% of young adults can correctly answer basic financial literacy questions."
  - "num: 60% of young adults have no long-term savings or investments."
  - "num: Over $3,200 is the average credit card balance for U.S. adults aged 18-29."
  - "num: Only 36% of young adults can cover a $500 emergency expense."
  - "num: Money is the top stressor for adults under 30."
  - Financial illiteracy leads to delayed milestones: home buying (67%), retirement savings (72%).
  - Financial education must be practical, relatable, and integrated into schools, workplaces, and communities.
key_figures_tables:
  - "Table 1: Common financial challenges for young adults → Shows high rates of debt, paycheck-to-paycheck living, and lack of savings."
  - "Figure 1: Areas of financial knowledge young adults struggle with → Visualizes gaps in budgeting, credit, and investment knowledge."
  - "Table 2: Personal and societal effects of poor financial literacy → Links individual financial mistakes to wider economic instability."
  - "Figure 2: Life milestones delayed by financial struggles → 72% delay retirement savings, 67% delay home buying."
  - "Figure 3: Power of starting early (saving $100/month from age 22 vs. 30) → Illustrates compound interest benefits."
  - "Figure 4: Intersection of digital tools, education, and community support → Shows a holistic framework for financial literacy."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Financial literacy"
    definition: "The ability to understand and effectively use various financial skills, including personal financial management, budgeting, and investing."
  - term: "Financial self-efficacy"
    definition: "An individual's belief in their capability to successfully manage financial tasks and decisions."
  - term: "APR"
    definition: "Annual Percentage Rate; the annual rate charged for borrowing or earned through an investment."
  - term: "Compound interest"
    definition: "Interest calculated on the initial principal and the accumulated interest from previous periods."
critical_citations:
  - "[OECD, 2023] — Key stat on youth financial literacy rates."
  - "[FINRA, 2023] — Data on young adults' understanding of APR."
  - "[Bankrate, 2023] — Emergency savings statistics for young adults."
  - "[APA, 2023] — Link between financial stress and mental health."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "contextual"
      justification: "The paper focuses on young adults globally, providing general demographic context applicable to Filipinos."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "contextual"
      justification: "Discusses general financial challenges like student loans and credit card debt relevant to understanding their financial structure."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "contextual"
      justification: "Describes financial behaviors such as living paycheck to paycheck and lack of savings, relevant to the target demographic."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Provides examples of existing digital tools (Mint, YNAB) and educational platforms."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Directly addresses the financial literacy gap and the lack of preparedness among young adults."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "low"
      justification: "Mentions digital tools but does not address privacy or security concerns."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "low"
      justification: "Discusses emotional barriers like shame and anxiety but not trust in systems specifically."
  contribution: "This paper highlights the critical need for financial literacy among young adults, providing foundational insights into their financial behaviors and challenges. It identifies the gap between financial responsibility and education, which supports Odin's purpose of guiding users through expense management and budgeting. The proposed solutions, including practical budgeting principles and digital tools, align with Odin's mobile-first design and goal of fostering financial confidence. The emphasis on user-defined savings goals and debt management supports Odin's modules for savings and debt management."
  directly_justifies:
    - "Young adults often lack formal financial education, leading to poor financial decisions and debt accumulation."
    - "Financial literacy is a key determinant of financial well-being and independence."
    - "Digital tools can make financial education more accessible and engaging for young adults."
  limits:
    - "The paper does not conduct primary research on Filipino young professionals specifically."
    - "The paper relies on global and U.S.-centric data, limiting its cultural specificity."
    - "The paper does not evaluate the effectiveness of specific digital tools or interventions."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains 'Filipino Cultural Context' (2.A-2.D) were considered but rejected due to the paper's global focus, lacking culturally specific practices. The domain 'Expense Categorization' (3.A-3.C) was considered and rejected as the paper does not propose a classification framework. 'Existing Systems & Gaps' (4.A, 4.B) was flagged as highly relevant because the paper documents the financial literacy gap and existing educational resources. 'Behavioral Profiling' (5.A-5.C) was considered but rejected as it does not discuss financial personality types. 'Spending Forecasting' (6.A-6.B), 'Budget Recommendation' (7.A-7.D), 'Anomaly Detection' (8.A-8.C), and 'System Evaluation' (12.A-12.C) were rejected as the paper is not algorithmic. 'Mobile-First Design' (9.A-9.B) was rejected; while digital tools are mentioned, design principles are not addressed. 'Data Privacy & User Trust' (10.A-10.B) was deemed low relevance, as privacy is not discussed. 'User Retention & Engagement' (11.A-11.B) was considered but rejected as it does not explore engagement dynamics. 'Savings & Debt Management' (13.A-13.C) was relevant contextually. Borderline cases were resolved by treating the paper as a broad foundation for understanding user needs rather than a technical guide. Overall, the paper is contextually relevant to Odin's user demographics and financial literacy goals."
limitations:
  - "Does not specifically address the Filipino cultural context. [unacknowledged]"
  - "Lacks empirical evaluation of proposed financial literacy interventions. [unacknowledged]"
  - "Relies heavily on U.S. survey data, which may not generalize to other national contexts."
  - "Does not consider algorithmic approaches to financial management, limiting its direct applicability to Odin's technical modules."
remember_this:
  - "Only 31% of young adults can answer basic financial literacy questions."
  - "Financial literacy is a foundation for freedom and reduced stress."
  - "Budgeting apps and digital tools can make financial management more accessible."
  - "Starting to save early has powerful compounding effects."
  - "Financial education must be integrated into schools, workplaces, and communities."
```
---

## Paper 47: Erno & Grefalde_summarized.md

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

## Paper 48: Bahlool et al_summarized.md

**Source File:** `Bahlool et al_summarized.md`

```yaml
paper_id: 10.3390/jrfm19020104
designation: international
title: Performance, Fairness, and Explainability in AI-Based Credit Scoring: A Systematic Literature Review
authors: Bahlool, R.; Hewahi, N.; Elmedany, W.
year: 2026
venue: Journal of Risk and Financial Management
odin_topics:
  - 5.C
  - 6.B
  - 7.B
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
tldr: A systematic review of 43 studies finds that performance, fairness, and explainability in AI credit scoring are treated in isolation, with limited joint optimization despite regulatory pressures for transparency and non-discrimination.
problem_and_motivation: AI adoption in credit scoring offers strong predictive performance but raises fairness and explainability concerns. Existing research addresses these dimensions in isolation, leaving a gap in understanding their interactions under regulatory and human oversight.
approach:
  - Systematic literature review following PRISMA guidelines, searching IEEE, Scopus, Web of Science, and ScienceDirect.
  - Included 43 peer-reviewed studies from 2020-2025 focusing on AI credit scoring with performance, fairness, or explainability.
  - Used a customized 3Rs&Q (Relevance, Rigor, Reproducibility, Quality) framework for quality assessment.
  - Structured data extraction using a PICOC framework to guide research questions on trade-offs, bias mitigation, and regulation.
  - Synthesized findings narratively, mapping studies to intersections of performance, explainability, fairness, regulation, and human-in-the-loop.
findings:
  - num: 55.81% of selected studies were published in domain-specific venues not belonging to a major digital library.
  - num: 48.8% of included studies were published in 2024, indicating recent research interest.
  - Explainability showed the strongest expansion between 2023 and 2024, becoming the dominant research pillar.
  - num: 21 papers explicitly discussed the association between fairness and protected attributes.
  - num: Only 10 out of 43 papers (23.25%) explicitly measured or proposed novel fairness mitigation strategies.
  - The trade-off between explainability and performance is largely assumed; limited empirical quantification shows marginal differences between interpretable and black-box models.
  - num: Performance gaps between interpretable and black-box models are often marginal, e.g., less than a 4% AUC difference in many reported cases.
  - Fairness is treated as a multi-objective optimization problem with tunable trade-offs; aggressive enforcement degrades performance.
  - Regulatory frameworks (e.g., EU AI Act, ECOA) increasingly mandate explainability and human oversight, but this is not fully integrated into unified pipelines.
  - Human-in-the-loop (HITL) oversight remains under-specified in practical implementation terms.
key_figures_tables:
  - Figure 4: Topic coverage by year → Explainability and fairness research surged from 2023 onward.
  - Table 5: Pairwise intersections grouped by base dimension → Fairness and protected attributes have the highest intersection (21 papers).
  - Table 6: Comparison of interpretable vs. black-box model performance → Performance differences are often marginal and dataset-dependent.
  - Table A10-A13: Summary of fairness mitigation strategies → No universally dominant strategy; effectiveness depends on deployment stage and regulatory context.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: XAI
    definition: Explainable Artificial Intelligence, techniques to make AI model outputs understandable to humans.
  - term: HITL
    definition: Human-in-the-loop, a paradigm where human judgment is integrated into AI system decision-making.
  - term: ECOA
    definition: Equal Credit Opportunity Act, a US law prohibiting discrimination in credit transactions.
  - term: GDPR
    definition: General Data Protection Regulation, an EU law on data protection and privacy.
  - term: SHAP
    definition: SHapley Additive exPlanations, a game-theoretic approach to explain the output of machine learning models.
  - term: LIME
    definition: Local Interpretable Model-agnostic Explanations, a technique to explain individual predictions of any classifier.
  - term: AUC
    definition: Area Under the ROC Curve, a performance metric for binary classification.
  - term: PRISMA
    definition: Preferred Reporting Items for Systematic Reviews and Meta-Analyses, a guideline for reporting systematic reviews.
critical_citations:
  - "[Kozodoi et al., 2022] — Establishes baseline fairness-performance trade-offs in credit scoring."
  - "[Valdrighi et al., 2025] — Provides a comprehensive review of bias mitigation and transparency tools."
  - "[Dessain et al., 2023] — Quantifies the marginal performance cost of explainability."
  - "[Langenbucher, 2020] — Outlines a legal framework for responsible AI credit scoring."
  - "[Kumar et al., 2022] — Aligns algorithmic fairness research with US fair lending regulation."
relevance:
  topics:
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: "Reviews classification models (LR, XGBoost, DL) and their fairness/explainability trade-offs."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: "Discusses predictive modeling for credit risk, including sequential and temporal data considerations."
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: contextual
      justification: "Provides background on algorithmic decision-making and constraints, but not directly on budget recommendation."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: "Mentions outlier and boundary sample detection in credit scoring models."
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: "Identifies data imbalance and protected attributes as sources of bias, relevant to anomaly detection design."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: "Discusses regulatory frameworks like GDPR and their implications for data privacy and fairness."
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: "Emphasizes explainability and fairness as foundational for user trust and regulatory compliance."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: "Reviews evaluation metrics for fairness (e.g., DI, EO) and performance (AUC, accuracy), crucial for system evaluation."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: "Provides systematic comparison of model performance and fairness metrics, directly applicable to evaluating Odin's algorithmic modules."
  contribution: "This review provides a governance-oriented synthesis of AI-based credit scoring. It justifies Odin's need for a fairness-aware and explainable architecture by demonstrating the limitations of performance-only models. It directly informs the design of Odin's behavioral profiling module (5.C) by highlighting classification trade-offs. It also underpins the importance of evaluation frameworks (12.A, 12.B) that jointly assess performance, fairness, and explainability. Finally, it provides a clear rationale for incorporating regulatory and privacy considerations (10.A, 10.B) into Odin's design."
  directly_justifies:
    - "Fairness and explainability must be integrated as joint objectives, not post-hoc additions, in AI-based financial systems."
    - "The performance gap between interpretable and black-box models is often marginal, making interpretable models a viable choice for regulated applications."
    - "Regulatory frameworks like the EU AI Act and ECOA mandate transparency, necessitating explainable AI for compliance."
    - "Human-in-the-loop oversight is essential for certifying fairness and mitigating residual bias in algorithmic decisions."
    - "There is no universally dominant fairness mitigation strategy; selection depends on context, regulation, and risk tolerance."
  limits:
    - "The review is a synthesis of existing literature and does not propose a deployable system."
    - "The focus is on credit scoring, which may not fully translate to PFMS domains like spending behavior prediction or budget recommendation."
    - "Specific algorithms for PFMS (e.g., for spending forecasting) are not directly evaluated."
    - "The review's findings are based on studies from a specific period (2020-2025) and may not capture all future developments."
  mapping_rationale: "All 12 functional domains and their associated canonical topic codes were systematically scanned. High relevance was assigned to 5.C (Classification Approaches) due to the review's focus on model selection and trade-offs; 10.A and 10.B (Data Privacy & User Trust) for its strong regulatory and governance discussion; and 12.A/12.B (Evaluation Frameworks) for its comprehensive review of performance and fairness metrics. Medium relevance was given to 6.B (Forecasting Algorithms) and 8.B (Anomaly Detection Algorithms) as the paper discusses predictive modeling and bias sources relevant to these modules. Contextual relevance was assigned to 7.B (Budget Recommendation) as the paper provides background on optimization but not direct methods. Domains like 2.A (Cultural Practices) and 9.A (Mobile-First Design) were rejected as they were not addressed. The primary contribution is its intersection-oriented synthesis, informing Odin's need for a balanced, explainable, and fair system, directly supporting evaluation and trust modules."
limitations:
  - "The review focuses on credit scoring, a specific financial domain, limiting generalizability to other PFMS functions."
  - "The study does not propose a novel algorithm or system, only synthesizes existing evidence."
  - "Human-in-the-loop oversight is discussed conceptually but lacks practical implementation details."
  - "The analysis is based on studies published up to 2025, and emerging trends may not be fully captured. [unacknowledged]"
remember_this:
  - "Performance gains from black-box models over interpretable models are often marginal."
  - "Explainability has become the dominant research pillar in AI credit scoring since 2023."
  - "Fairness is a multi-objective optimization problem, not a one-time correction."
  - "Regulatory frameworks are driving the need for explainable and fair AI systems."
  - "There is no single best fairness strategy; context and risk tolerance determine the choice."
```
---

## Paper 49: Khan & Sadaoui_summarized.md

**Source File:** `Khan & Sadaoui_summarized.md`

```yaml
paper_id: "b7a8c9d0-e1f2-4a3b-8c9d-0e1f2a3b4c5d"
designation: "international"
title: "Learner-based Concept Drift Detection: Analysis and Evaluation"
authors: "Khan, M.M.U.H.; Sadaoui, S."
year: 2026
venue: "Unknown"
odin_topics:
  - "2.B"
  - "5.A"
  - "5.B"
  - "5.C"
  - "6.A"
  - "6.B"
  - "7.B"
  - "8.A"
  - "8.B"
  - "12.A"
  - "12.B"
tldr: "Surveys and evaluates learner-based concept drift detection methods, including SPC, window-based, and ensemble-based detectors, on synthetic and real-world streaming datasets."
problem_and_motivation: "Concept drift in streaming data can severely degrade model performance, yet detecting drift events efficiently remains challenging due to diverse drift types and algorithmic complexity. A comprehensive survey and empirical comparison of detection methods is lacking for practitioners. This paper addresses this gap by reviewing learner-based detectors and evaluating them across multiple drift scenarios."
approach:
  - "Surveys concept drift formal definitions, types (real, virtual, mixed), and transitions (sudden, gradual, incremental, recurrent)."
  - "Reviews 15 learner-based drift detectors: SPC (FTDD, RDDM, FHDDM, EWMA, EDDM), window (KSWIN, FPDD, WSTD, MDDM, ADWIN, D3), and ensemble (ARF, AUE, DWM, AWE)."
  - "Evaluates detectors on six synthetic datasets (RT, SINE, MIXED) with abrupt and gradual drifts, and two real-world datasets (ELEC2, CIC-IDS2017)."
  - "Uses Naive Bayes and Hoeffding Tree as base learners with default hyperparameters and AUC as performance metric."
  - "Compares detector performance by category and drift type, and summarizes best-performing combinations."
findings:
  - "num: EWMA+HT and EDDM+HT achieve the best overall SPC performance with AUC ≈ 0.69."
  - "num: On abrupt synthetic drifts, ARF+HT achieves the highest average AUC ≈ 0.94."
  - "num: On real-world streams, AUE+HT performs best among ensemble methods with AUC ≈ 0.88."
  - "num: For window-based methods, KSWIN, WSTD, and D3 with HT share top abrupt-drift performance at AUC ≈ 0.61."
  - "Ensemble methods consistently outperform SPC and window-based detectors across all dataset types."
  - "HT generally outperforms NB, except on real-world streams where NB sometimes matches or exceeds HT for SPC and window-based detectors."
key_figures_tables:
  - "Table 8.1: Comparison of SPC-based methods with two base learners → shows FTDD best for abrupt, EWMA/EDDM best overall."
  - "Table 9.1: Comparison of window-based methods → shows KSWIN/WSTD/D3 best for abrupt, WSTD/D3 best overall."
  - "Table 10.1: Comparison of ensemble-based methods → shows ARF best for synthetic, AUE best for real-world."
  - "Table 11.1: Best-performing detectors per category → summarizes top performers by drift type and base learner."
key_equations:
  - equation: "\(P(|\bar{X} - \mu| \ge \epsilon) \le 2e^{-2n\epsilon^2}\)"
    explanation: "Hoeffding bound for deviation of sample mean."
  - equation: "\(\sigma_{z_t} = \sqrt{\frac{\lambda}{2-\lambda} p_0(1-p_0)(1-(1-\lambda)^{2t})}\)"
    explanation: "Standard deviation of EWMA estimator for drift detection."
definitions:
  - term: "Concept drift"
    definition: "Change in joint probability distribution of input features and target over time."
  - term: "Real drift"
    definition: "Change in posterior probability P(y|X), affecting decision boundary."
  - term: "Virtual drift"
    definition: "Change in feature distribution P(X) without changing P(y|X)."
  - term: "Abrupt drift"
    definition: "Sudden change from old to new concept at a precise timestamp."
  - term: "Gradual drift"
    definition: "Progressive change with a transition phase mixing old and new concepts."
  - term: "Learner-based detection"
    definition: "Detects drift by monitoring classifier performance, e.g., error rates."
critical_citations:
  - "[Gama et al., 2014] — Foundational survey on concept drift adaptation."
  - "[Bifet & Gavalda, 2007] — ADWIN adaptive windowing algorithm."
  - "[Kolter & Maloof, 2007] — Dynamic Weighted Majority ensemble method."
relevance:
  topics:
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "high"
      justification: "Explicitly discusses recurrent drift with seasonal spending changes as a concrete example."
    - code: "5.A"
      name: "Financial Behavioral Profiles"
      relevance: "high"
      justification: "Drift detection is essential for maintaining accurate behavioral profiles as user behavior changes."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "medium"
      justification: "Addresses profile dynamics through drift detection but does not cover cold-start."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Surveys classification-based drift detectors directly applicable to profile classification."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Concept drift degrades predictive models, and detection methods are critical for maintaining accuracy."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Drift detection informs adaptation of forecasting models to changing spending patterns."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Budget recommendations require adaptation to drift, and detection methods can support that."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Drift detection is a core component of anomaly detection in streaming data."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Surveys algorithms that can be used for anomaly detection in spending data."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides an evaluation methodology for drift detectors that can inform PFMS evaluation."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Empirical comparison of algorithmic modules (drift detectors) offers insights for module evaluation."
  contribution: "This paper's survey of drift detection methods directly informs the design of Odin's anomaly detection module by identifying suitable algorithms for detecting changes in user spending behavior. Its empirical comparison of SPC, window-based, and ensemble methods provides guidance for selecting a drift detector for Odin's forecasting and profile management components. The distinction between abrupt and gradual drifts is particularly relevant for Odin's handling of seasonal spending and unexpected financial events. The evaluation framework using synthetic and real-world datasets offers a template for testing Odin's algorithmic modules under controlled drift scenarios."
  directly_justifies:
    - "Seasonal changes in spending behavior are a type of recurrent drift that Odin must detect."
    - "Ensemble-based detectors like ARF with Hoeffding Trees achieve the highest accuracy on abrupt drifts."
    - "AUE with Hoeffding Trees is most effective on real-world data streams, suggesting a preference for Odin's real-world deployment."
    - "Hoeffding Trees generally outperform Naive Bayes, recommending their use as base learners for drift adaptation in Odin."
  limits:
    - "Only learner-based detectors are covered; distribution-based detectors are not evaluated."
    - "Only two base learners (Naive Bayes and Hoeffding Tree) are used; other classifiers may yield different results. [unacknowledged]"
    - "Synthetic datasets may not fully capture the complexity of real-world financial data. [unacknowledged]"
    - "The evaluation metric is limited to AUC; other metrics like F1 and detection delay are not considered. [unacknowledged]"
    - "Some detectors (WSTD, AUE) had no publicly available implementation, potentially affecting reproducibility. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated canonical topic codes was conducted. The following domains were flagged as relevant: Filipino Cultural Context (specifically 2.B due to recurrent drift examples), Behavioral Profiling (5.A, 5.B, 5.C), Spending Forecasting (6.A, 6.B), Anomaly Detection (8.A, 8.B), and System Evaluation (12.A, 12.B). Budget Recommendation (7.B) was also considered medium. Domains such as Mobile-First Design, Data Privacy, User Retention, Savings & Debt Management were considered but rejected because the paper does not address those aspects. Borderline cases: 2.B and 2.D both relate to spending cycles; since the paper explicitly mentions seasonal spending but not Filipino-specific, 2.B was chosen. 5.B (cold-start) was assigned medium because the paper does not discuss cold-start, though it covers profile dynamics. Overall, the paper provides high relevance for drift detection modules and medium relevance for evaluation and adaptation in Odin."
limitations:
  - "Only learner-based detectors are covered; distribution-based detectors are not evaluated."
  - "Only two base learners (Naive Bayes and Hoeffding Tree) are used; other classifiers may yield different results. [unacknowledged]"
  - "Synthetic datasets may not fully capture the complexity of real-world financial data. [unacknowledged]"
  - "The evaluation metric is limited to AUC; other metrics like F1 and detection delay are not considered. [unacknowledged]"
  - "Some detectors (WSTD, AUE) had no publicly available implementation, potentially affecting reproducibility. [unacknowledged]"
remember_this:
  - "Ensemble methods, especially ARF with HT, outperform SPC and window-based detectors on synthetic drifts."
  - "AUE with HT is best for real-world data streams, achieving AUC 0.88."
  - "EWMA and EDDM with HT are reliable SPC choices with AUC around 0.69."
  - "Hoeffding Trees are generally superior to Naive Bayes for drift adaptation."
  - "Drift detector selection depends on drift type and dataset characteristics."
```
---

## Paper 50: Ramesh & Shobha_summarized.md

**Source File:** `Ramesh & Shobha_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international
title: Dynamic Income Volatility and Adaptive Financial Planning Strategies in the Gig Economy: An Empirical Study
authors: Ramesh, S.; Shobha, C.
year: 2026
venue: Artha Vijnana
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.B
  - 3.A
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 13.A
tldr: Gig workers facing higher income volatility adopt more adaptive financial planning strategies, a relationship moderated by financial literacy and influenced by demographic and psychological factors.
problem_and_motivation: The gig economy's rapid growth presents unique financial challenges for workers due to pronounced income volatility. This instability complicates financial management for individuals lacking traditional employment benefits. Effective financial planning strategies are crucial for mitigating these adverse effects.
approach:
  - A longitudinal research design was used, surveying 500 gig workers bi-annually over three years.
  - Data was collected via online surveys optimized for mobile and desktop accessibility.
  - The study employed multiple regression analyses and structural equation modeling (SEM) to examine relationships.
  - Mixed-effects models and growth curve modeling were used for longitudinal data analysis.
  - Thematic analysis of qualitative data from open-ended questions and interviews was also conducted.
findings:
  - num: Higher income volatility is positively associated with adaptive financial planning strategies (β = 0.276, p < 0.001).
  - Financial literacy moderates the relationship between income volatility and adaptive strategies (β = 0.161, p = 0.009).
  - Education (β = 0.038, p = 0.002) and family status (β = 0.046, p = 0.046) significantly predict adaptive financial planning.
  - Risk tolerance positively influences adaptive planning (β = 0.332, p < 0.001), while cognitive bias has a negative impact (β = -0.220, p = 0.001).
  - Demographic factors like age, education, and family status significantly influence financial planning strategies.
key_figures_tables:
  - Table 1: Descriptive statistics for all study variables including means, standard deviations, and ranges.
  - Table 2: Cronbach's alpha values (0.78, 0.81) for financial literacy and adaptive financial planning scales, confirming reliability.
  - Table 3: VIF values for multicollinearity check, showing high VIFs for income volatility and its interaction term.
  - Table 4: Regression results for Model 1 showing significant positive effects of income volatility, risk tolerance, and demographic factors on adaptive planning.
  - Table 5: Regression results for Model 2 demonstrating the significant moderating effect of financial literacy on income volatility and adaptive planning.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: Financial Literacy
    definition: The ability to understand and use various financial skills, including personal financial management, budgeting, and investing.
  - term: Income Volatility
    definition: The degree of unpredictable fluctuation in an individual's earnings over time.
  - term: Adaptive Financial Planning
    definition: The use of flexible and dynamic strategies, such as diversified income sources and flexible budgeting, to manage financial instability.
  - term: Gig Economy
    definition: A labor market characterized by flexible, short-term, and task-based work arrangements often mediated by digital platforms.
  - term: Cognitive Bias
    definition: Systematic patterns of deviation from norm or rationality in judgment, affecting financial decision-making.
critical_citations:
  - "[Katz and Krueger, 2016] — Foundational for gig economy growth and worker challenges."
  - "[Lusardi and Mitchell, 2014] — Establishes the link between financial literacy and better financial outcomes."
  - "[Kahneman and Tversky, 1979] — Provides the theoretical basis (Prospect Theory) for understanding decision-making under uncertainty."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "contextual"
      justification: "While the study focuses on gig workers generally, its findings on financial behavior and volatility are applicable to demographic subsets like Filipino young professionals."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "contextual"
      justification: "Provides insights into income volatility and financial management challenges that can inform understanding of the financial structure of this group."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "medium"
      justification: "Directly studies financial planning behaviors (adaptive strategies) in response to income volatility, relevant to understanding financial behavior."
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "medium"
      justification: "Income volatility in gig work is linked to seasonality and demand cycles, which informs understanding of cyclical spending patterns."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "low"
      justification: "Adaptive strategies include flexible budgeting, which requires frameworks for expense categorization, though not the paper's focus."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Directly investigates how income volatility and psychological traits (risk tolerance, cognitive bias) shape financial behavioral profiles and adaptive planning."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "The study's identification of factors (literacy, demographics) influencing behavior can inform classification approaches for profiles."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "low"
      justification: "Findings on behavioral responses to volatility can be input features for predictive models but does not itself develop them."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "low"
      justification: "Insights on how volatility affects planning can inform forecasting, but the paper does not propose or evaluate algorithms."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "high"
      justification: "The paper identifies flexible budgeting and increased savings as key adaptive strategies, directly relevant to domain knowledge on budgeting."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "medium"
      justification: "Findings show increased savings during high-income periods as a coping strategy, relevant to savings goal management."
  contribution: This paper provides empirical evidence on how financial literacy and demographic factors moderate the behavioral response to income volatility, which can inform Odin's user profiling module. The identified adaptive strategies (flexible budgeting, increased savings) can be directly incorporated into Odin's budget recommendation and savings goal modules. The negative impact of cognitive bias on planning validates the need for behavioral nudges within the application. The methodology using mixed-effects models offers a framework for evaluating financial behavior over time.
  directly_justifies:
    - "Income volatility prompts adoption of flexible budgeting and increased savings."
    - "Financial literacy enhances the effectiveness of financial planning strategies."
    - "Risk tolerance is positively associated with better financial planning."
    - "Cognitive biases negatively impact financial decision-making."
    - "Demographic factors like education and family status influence financial planning."
  limits:
    - "The study focuses on the Indian gig economy context, which may limit generalizability to other regions."
    - "Self-reported data on income and financial behaviors may be subject to recall bias."
    - "The longitudinal period of three years may not capture long-term efficacy of adaptive strategies."
  mapping_rationale: During the systematic scan, the paper was flagged as highly relevant to the domains of Behavioral Profiling & Classification (specifically 5.A and 5.C) due to its focus on how workers adapt behaviors to income volatility and the influence of psychological factors. It also provides high relevance to Budget Recommendation (7.A) as it identifies key adaptive strategies like flexible budgeting. Medium relevance was assigned to topics related to Financial Behavior (1.C), Seasonal Patterns (2.B), and Savings Management (13.A), as the findings directly inform these areas. Low relevance was given to Expense Categorization (3.A), Predictive Modeling (6.A), and Forecasting (6.B), as the paper discusses concepts related to these topics but does not propose new frameworks or algorithms. Domains such as Mobile-First Design, Data Privacy, and User Retention were considered but rejected as the paper does not address them.
limitations:
  - "The study relies on self-reported income and financial strategies, which may introduce social desirability bias. [unacknowledged]"
  - "The sample, while diverse, is limited to platform-based gig workers in India, potentially limiting generalizability to other gig economy contexts."
  - "Potential multicollinearity noted in VIF values, particularly for income volatility and its interaction term, suggests caution in interpreting individual coefficients."
remember_this:
  - "Higher income volatility drives gig workers toward adaptive financial strategies."
  - "Financial literacy significantly improves the effectiveness of financial planning."
  - "Risk tolerance positively influences adaptive planning, while cognitive bias hinders it."
  - "Educational attainment and family status are key demographic predictors of financial behavior."
  - "num: Income volatility and financial literacy interaction has a beta coefficient of 0.161."
```
---


---

## Agent Instruction

If the agent reading this document believes further context about a paper is needed, it may request the original converted markdown file (with the '_marked' suffix) from the user for the relevant paper(s).
