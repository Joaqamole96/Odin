```yaml
paper_id: 10.1109/ACCESS.2025.3557229
designation: international-algorithm-specific
title: A Comparison of Approaches for Handling Concept Drifts in Data Processed With Machine Learning
authors: Pereira, E. V.; Da Silva, W. S.
year: 2025
venue: IEEE Access
odin_topics:
  - 4.A
  - 5.C
  - 6.A
  - 7.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
tldr: A comparison of concept drift handling techniques shows batch training and ensemble methods like BIC yield robust performance across diverse data streams.
problem_and_motivation: Machine learning models degrade when the statistical properties of target variables change over time, a phenomenon known as concept drift. This degradation is critical for domains like healthcare and finance. A comprehensive comparison of treatment methods across algorithms and drift types is lacking.
approach:
  - Utilized the scikit-multiflow framework to simulate and evaluate concept drift.
  - Tested eight datasets, including real-world data (Airlines, Electricity) and synthetic data (SEA, Hyperplane).
  - Evaluated various drift detection algorithms, including ADWIN, DDM, EDDM, and Page-Hinkley.
  - Assessed nine classifiers, including Hoeffding Tree (HT), Adaptive Random Forest, and KNN with Adaptive Windowing.
  - Applied treatment methods such as ignore, delete, retrain, and batch training to static models.
  - Compared performance of models with and without internal drift adaptation mechanisms.
findings:
  - num: Batch training consistently improved accuracy over ignoring drift across all tested datasets and classifiers.
  - num: The BIC ensemble classifier achieved strong and robust performance across all drift types and datasets.
  - num: The HAT decision tree algorithm, which uses ADWIN for branch-level monitoring, excelled in abrupt drift scenarios.
  - num: The KNNADW algorithm performed well on gradual concept drift due to its adaptive windowing.
  - The simple exclusion of drift-affected samples was ineffective, showing no significant performance change.
  - Combining treatment strategies within ensemble frameworks can amplify robustness against drift.
  - Algorithms lacking drift adaptation were consistently outperformed by those with adaptation mechanisms.
  - Ensemble methods like BIC, which combine batch training with model ensembles, are a potent strategy for dynamic data.
key_figures_tables:
  - "Figure 1: Comparison of HT, HAT, and EFDT classifiers across datasets → HAT and EFDT outperform HT on drift-affected data."
  - "Figure 2: Performance comparison of nine classifiers across varied datasets → BIC and HAT show superior and stable accuracy."
  - "Table 1: Dataset characteristics (samples, features, drift type) → Provides context for evaluating algorithm performance."
  - "Table 3-8: Accuracy of HT and KNN under different treatment methods → Batch training is the most effective standalone strategy."
key_equations:
  - equation: "p_t(X,y) \\neq p_{t+1}(X,y)"
    explanation: "Definition of concept drift in terms of joint probability."
definitions:
  - term: "Concept Drift"
    definition: "A change in the statistical properties of the target variable over time."
  - term: "ADWIN"
    definition: "Adaptive Windowing algorithm for detecting concept drift by monitoring statistical changes."
  - term: "scikit-multiflow"
    definition: "An open-source machine learning toolkit for streaming data."
critical_citations:
  - "[Lu et al., 2019] — Foundational review defining concept drift and its mathematical models."
  - "[Gama et al., 2014] — Comprehensive survey on concept drift adaptation strategies."
  - "[Gomes et al., 2017] — Introduces Adaptive Random Forest, a key ensemble method evaluated in the study."
relevance:
  topics:
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Provides a general benchmark for comparing algorithm performance."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "Evaluates classification algorithms that could be adapted for profiling."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Directly compares predictive models under data distribution shifts (concept drift)."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "contextual"
      justification: "Budgets must adapt to changing spending patterns, similar to model adaptation."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Concept drift detection techniques (e.g., ADWIN) are directly applicable to anomaly detection baselines."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "medium"
      justification: "Evaluation of drift detection algorithms informs the selection of anomaly detectors."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Provides a methodology for comparative evaluation of algorithmic modules."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Directly compares and evaluates multiple classification and detection algorithms."
  contribution: "This paper justifies Odin's use of ensemble and batch-training strategies for robust handling of changing spending patterns. It validates the need for adaptive algorithms over static ones in dynamic personal finance environments. The study's empirical comparison framework is directly applicable for evaluating Odin's classification and anomaly detection modules. Its findings on algorithm performance under different drift types inform the selection of optimal models for forecasting and anomaly detection within Odin."
  directly_justifies:
    - "Batch training is an effective strategy for maintaining model accuracy under concept drift."
    - "Ensemble classifiers like BIC provide robust performance across diverse data stream conditions."
    - "Models with integrated drift detection (e.g., ADWIN) outperform those without adaptation."
    - "The choice of optimal classifier depends on the type of concept drift (abrupt vs. gradual)."
  limits:
    - "The study does not specifically address personal finance data or spending behaviors."
    - "No deep learning models were evaluated."
    - "The analysis focuses on classification tasks, not forecasting or regression."
  mapping_rationale: "A systematic scan of all 12 functional domains was performed. Domains relevant to the core algorithmic contributions (Existing Systems & Gaps, Behavioral Classification, Forecasting, Anomaly Detection, and Evaluation) were flagged. Specifically, topic codes 4.A (landscape), 5.C (classification approaches), 6.A (predictive modeling), 8.A & 8.B (anomaly detection and algorithms), 12.A & 12.B (evaluation frameworks) were selected with high or medium relevance. The paper's focus on concept drift in data streams provides strong justification for its relevance to Odin's dynamic spending data. Borderline cases like 7.B (Budget Recommendation) and 7.C (Constrained Optimization) were considered but rejected as the paper does not address constraint-based allocation. Topics related to cultural context, mobile design, privacy, and retention (Domains 1, 2, 3, 9, 10, 11, 13) were considered and rejected, as the paper provides no information on those specific domains. The study's comparative framework is highly relevant for evaluating Odin's algorithmic modules, establishing a clear justification for its high relevance to the project."
limitations:
  - "The study does not address deep learning models. [unacknowledged]"
  - "The research is limited to classification problems and does not cover regression or forecasting. [unacknowledged]"
  - "No datasets specific to personal finance or developing economies were used."
remember_this:
  - "Batch training improves model accuracy during concept drift."
  - "Ensemble methods, like BIC, offer robust performance across drift types."
  - "The optimal classifier depends on the type of concept drift present."
  - "Adaptive algorithms consistently outperform static models on dynamic data."
  - "Ignoring drift-affected samples is an ineffective handling strategy."
```