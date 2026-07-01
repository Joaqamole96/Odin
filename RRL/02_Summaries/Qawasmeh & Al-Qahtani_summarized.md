```yaml
paper_id: 8f4a4c5e-8a2d-5b6e-9c3f-1d2e3f4a5b6c
designation: international-algorithm-specific
title: Beyond Firewall: Leveraging Machine Learning for Real-Time Insider Threats Identification and User Profiling
authors: Qawasmeh, S.A.-D.; AlQahtani, A.A.S.
year: 2025
venue: Future Internet
odin_topics:
  - 8.A
  - 8.B
  - 5.A
  - 4.A
tldr: Integrates real-time anomaly detection with dynamic user profiling to classify employees into low, medium, and high risk using machine learning.
problem_and_motivation: Existing security tools like firewalls and signature-based IDS are inadequate for detecting novel insider threats. There is a critical gap in systems that provide both real-time analysis and comprehensive user risk classification.
approach:
  - Data acquisition utilized a synthetic dataset of 10,000 records representing 500 employees over 4 weeks, expanded via resampling.
  - Feature engineering introduced a composite RiskScore feature based on the weighted sum of first-occurrence anomalous activities.
  - Data preprocessing included imputing missing values with 1, adjusting outliers, and applying SMOTEENN to address class imbalance.
  - Four ML models (LR, RF, XGBoost, SVM) were trained on a 70/15/15 split and evaluated using accuracy, precision, recall, and F1-score.
  - A real-time simulator with a REST API was developed to test the system's detection and classification speed on streaming data.
findings:
  - XGBoost achieved the highest performance with 1.00 accuracy, precision, recall, and F1-score.
  - num: XGBoost demonstrated an average detection time of 0.056 seconds and a classification time of 0.102 seconds.
  - num: The proposed LR, XGBoost, and SVM implementations notably outperformed benchmarks in classification accuracy and precision.
  - Synthetic data effectively mimicked realistic organizational environments while mitigating privacy concerns.
  - The system addresses limitations of traditional tools by providing instantaneous data analysis and dynamic user profiling.
key_figures_tables:
  - Figure 1: System workflow diagram → Shows integration of real-time analysis and risk classification tools.
  - Figure 4: Performance results for ML models → XGBoost and SVM achieve near-perfect metrics.
  - Table 2: Abnormal behaviors description → Lists 17 anomalous activity types with assigned severity weights.
  - Table 5: Quantitative comparison with recent studies → Proposed models show superior or comparable performance with added real-time capability.
key_equations:
  - equation: RiskScore = ∑_{i=1}^{n} W_i · ⊮_{F_ij = 1}
    explanation: Calculates risk score by summing weights of first-time abnormal activities.
definitions:
  - term: SMOTEENN
    definition: Synthetic Minority Over-sampling Technique combined with Edited Nearest Neighbors for balancing datasets.
  - term: PFMS
    definition: Personal Financial Management System.
critical_citations:
  - "[Verizon, 2024] — Reports insiders account for 31% of data breaches."
  - "[IBM, 2024] — Malicious insider attacks cost an average of USD 4.99 million."
  - "[Le & Zincir-Heywood, 2021] — Addresses anomaly detection for insider threat identification."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Core contribution is real-time anomaly detection for user activities.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Benchmarks XGBoost, RF, SVM, and LR for anomaly detection.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Dynamic user profiling based on behavior for risk classification.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Literature review identifies gaps in existing security systems.
  contribution: The paper provides a validated framework for real-time anomaly detection and user risk classification. Its methodology for dynamic profiling can inform Odin's behavioral profiling module. The XGBoost model's performance justifies its selection for high-stakes classification tasks. The synthetic data generation approach offers a privacy-preserving template for model development. The emphasis on instantaneous analysis and continuous monitoring aligns with Odin's need for responsive systems.
  directly_justifies:
    - A weighted sum approach can provide a baseline risk score for initial user profiling.
    - XGBoost is a highly effective and efficient algorithm for real-time classification tasks.
    - Real-time simulation frameworks are essential for validating system performance before deployment.
    - Synthetic data can effectively replicate behavioral complexities while safeguarding privacy.
  limits:
    - The study primarily relies on synthetic data, which may not fully capture real-world behavioral complexities.
    - The paper focuses on technical indicators, potentially overlooking psychological and contextual factors.
    - Real-world performance may vary and requires integration with existing security infrastructure.
  mapping_rationale: A systematic scan across all 12 functional domains was performed. Domain 8 (Anomaly Detection) was flagged as highly relevant because the paper's core contribution directly addresses anomaly detection for user behavior classification, supporting codes 8.A and 8.B. Domain 5 (Behavioral Profiling & Classification) was identified as medium relevance due to its implementation of dynamic user profiling (5.A). Domain 4 (Existing Systems & Gaps) was considered contextual, as the literature review discusses the landscape and limitations of current security tools (4.A). Domains related to Filipino cultural context (2.A-2.D), expense categorization (3.A-3.C), budget recommendation (7.A-7.D), and savings/debt management (13.A-13.C) were rejected as the paper does not address these financial topics. The overall relevance is moderate, as the paper's anomaly detection and profiling methods are technically applicable to a PFMS like Odin, though it lacks financial domain specificity.
limitations:
  - The dataset is synthetic, generated by the authors, which may limit generalizability to real-world organizational data.
  - The paper does not address the integration of psychological or contextual factors like stress or job satisfaction. [unacknowledged]
  - The system's performance with significantly larger, more diverse, or noisier real-world data streams is not evaluated. [unacknowledged]
remember_this:
  - XGBoost achieved perfect accuracy and F1-score for risk classification.
  - The system provides real-time anomaly detection and classification in under one second.
  - Dynamic user profiling updates continuously based on observed behaviors.
  - The approach addresses key gaps in traditional insider threat detection systems.
  - Synthetic data generation enables privacy-preserving development and testing.
```