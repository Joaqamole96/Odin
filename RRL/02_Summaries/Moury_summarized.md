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