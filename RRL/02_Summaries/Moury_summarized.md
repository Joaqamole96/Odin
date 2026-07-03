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