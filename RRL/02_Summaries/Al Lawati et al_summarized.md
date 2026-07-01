```yaml
paper_id: 10.1109/ACCESS.2025.3569609
designation: international-algorithm-specific
title: An Integrated Preprocessing and Drift Detection Approach With Adaptive Windowing for Fraud Detection in Payment Systems
authors: Al Lawati, H. M. R.; Zainal, A.; Al-Rimy, B. A. S.; Al-Azawi, M.; Kassim, M. N.; Almalki, S. A.; Alghamdi, T. A.
year: 2025
venue: IEEE Access
odin_topics:
  - 4.A
  - 4.B
  - 6.A
  - 8.A
  - 8.B
  - 12.A
  - 12.B
tldr: A framework combining Mutual Information feature selection, ADASYN class balancing, CNN classification, and dual EDDM/ADWIN drift detection achieves 100% accuracy on real fraud datasets.
problem_and_motivation: Static rule-based and machine learning fraud detection systems fail to capture evolving fraudulent behaviors in payment systems. Concept drift and class imbalance degrade detection accuracy and increase false positive rates over time. Existing approaches lack integrated preprocessing and adaptive drift detection mechanisms for real-time transaction environments.
approach:
  - Applied Mutual Information with SelectKBest for supervised feature selection to eliminate irrelevant features.
  - Used ADASYN (Adaptive Synthetic Sampling) to balance the minority fraud class against the majority legitimate class.
  - Employed Convolutional Neural Networks (CNN) as the primary classifier to capture complex transaction patterns.
  - Integrated Early Drift Detection Method (EDDM) to identify gradual and abrupt changes in transaction data distributions.
  - Combined ADWIN (ADaptive WINdowing) with EDDM for complementary drift detection and dynamic window adjustment.
  - Evaluated on three datasets: European credit card dataset (2013), GCC bank transactions (2019), and UCI Spam dataset.
  - Used confusion matrix, accuracy, precision, recall, F1, ROC-AUC, and drift detection rate as evaluation metrics.
findings:
  - "num: 100% accuracy and 100% drift detection rate achieved on the Real Dataset with 90 features."
  - "num: 100% accuracy and 100% F1 Score achieved on the Credit Card Dataset with 30 features."
  - "num: 99.34% accuracy, 100% precision, and 98.69% recall achieved on the Spam Dataset with 55 features."
  - "EDDM captured all critical drifts across all datasets, detecting 284,313 drifts on the Credit Card Dataset."
  - "ADWIN uniquely detected 1 gradual drift missed by EDDM, complementing the drift detection capability."
  - "K-fold cross-validation confirmed consistent performance, with accuracy remaining stable across all folds."
  - "The dual EDDM and ADWIN approach detected both abrupt and gradual drifts without sacrificing speed or accuracy."
key_figures_tables:
  - "Figure 12: Proposed two-phase methodology with preprocessing and drift detection → Framework for integrated fraud detection."
  - "Figure 13: Drift detection workflow using CNN, EDDM, and ADWIN → Adaptive drift monitoring and model update mechanism."
  - "Table 5: Pre-processing stage results across all datasets → Feature selection and balancing impact on performance metrics."
  - "Table 6: Detection stage results across all datasets → Final performance with 100% accuracy on real dataset."
  - "Figure 14-16: Venn diagrams showing drift detection overlap → EDDM captures nearly all drifts; ADWIN provides complementary detection."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: EDDM
    definition: Early Drift Detection Method; monitors error rates to identify gradual and abrupt changes in data streams.
  - term: ADWIN
    definition: ADaptive WINdowing; dynamically adjusts window size to detect concept drift in data streams.
  - term: CNN
    definition: Convolutional Neural Network; deep learning model used to classify transactions and detect fraud patterns.
  - term: ADASYN
    definition: Adaptive Synthetic Sampling; oversampling technique that generates synthetic minority class instances.
  - term: FDS
    definition: Fraud Detection System; system designed to identify fraudulent transactions in payment processing.
  - term: CP
    definition: Card-Present; transactions where the physical card is present at the point of sale.
  - term: CNP
    definition: Card-Not-Present; transactions conducted online or remotely without physical card presence.
  - term: EMV
    definition: Europay, MasterCard, and Visa; global standard for secure payment processing using smart card technology.
  - term: MI
    definition: Mutual Information; measure of dependence between features and target variables for feature selection.
critical_citations:
  - "[Bifet and Gavalda, 2007] — ADWIN adaptive windowing for drift detection."
  - "[Priya and Uthra, 2021] — Deep learning framework for concept drift handling."
  - "[Smith, Johnson, and Williams, 2021] — Concept drift increases false alarm rates."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews existing fraud detection systems and their limitations.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies concept drift, class imbalance, and static models as key gaps.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Uses CNN for predictive fraud classification from transaction data.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly addresses fraud detection as anomaly detection in payment transactions.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Evaluates CNN, EDDM, and ADWIN as algorithmic approaches for anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses accuracy, precision, recall, F1, ROC-AUC, and drift detection rate as metrics.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Evaluates feature selection, balancing, classification, and drift detection components.
  contribution: The framework's feature selection and ADASYN balancing directly inform Odin's anomaly detection preprocessing pipeline. The dual EDDM and ADWIN drift detection strategy provides a template for Odin's adaptive anomaly detection module. The CNN-based classification approach offers a reference for modeling transaction patterns in user spending data. The evaluation methodology with cross-validation and multiple metrics establishes a baseline for Odin's system evaluation practices. The integrated preprocessing and drift-aware design demonstrates how to maintain detection performance under evolving financial behaviors.
  directly_justifies:
    - "Concept drift detection is essential for maintaining anomaly detection accuracy over time."
    - "Class imbalance handling via ADASYN improves fraud detection sensitivity without overfitting."
    - "Feature selection using Mutual Information reduces computational overhead while preserving predictive power."
    - "Dual drift detection (EDDM + ADWIN) captures both gradual and abrupt changes in transaction patterns."
    - "CNN can effectively model complex transaction patterns for real-time fraud detection."
  limits:
    - "The dual drift detection approach introduces communication and computational overhead during validation steps."
    - "Real-time online learning is not implemented; model retraining is triggered only after drift confirmation."
    - "The approach was not evaluated on Philippine-specific financial data or Filipino spending patterns."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to the Anomaly Detection domain (8.A, 8.B) because it directly addresses fraud detection in payment systems using preprocessing, classification, and drift detection algorithms. Medium relevance was assigned to Existing Systems (4.A, 4.B) as the paper reviews and identifies gaps in current fraud detection approaches, and to Predictive Modeling (6.A) for using CNN as a predictive classifier. The Evaluation domain (12.A, 12.B) received medium relevance for the comprehensive evaluation methodology. Borderline cases included 8.C (Cold-Start Baseline Strategies) which was rejected as the paper does not specifically address cold-start scenarios, and 5.B (Profile Dynamics) which was considered contextual only because concept drift is discussed at the transaction level rather than user profiling. Topics related to Filipino cultural context (1.A, 1.B, 1.C, 2.A, 2.B, 2.C, 2.D), expense categorization (3.A, 3.B, 3.C), budgeting (7.A, 7.B, 7.C, 7.D), data privacy (10.A, 10.B), user retention (11.A, 11.B), and savings/debt management (13.A, 13.B, 13.C) were considered and rejected due to lack of relevance to the paper's focus on fraud detection. Overall, the paper provides strong algorithmic foundations for Odin's anomaly detection module, particularly in handling concept drift and class imbalance.
limitations:
  - "Real-time online learning is not implemented; the model retrains only after drift confirmation. [unacknowledged]"
  - "The dual drift detection approach introduces communication and computational overhead during validation steps."
  - "Evaluation was conducted on credit card and spam datasets, not on Filipino PFMS spending data. [unacknowledged]"
  - "The approach does not address privacy-preserving techniques such as federated learning. [unacknowledged]"
  - "Lightweight model architectures for real-time scalability were not explored. [unacknowledged]"
remember_this:
  - "Dual EDDM and ADWIN drift detection captures both gradual and abrupt changes."
  - "Integrated feature selection and ADASYN balancing achieved 100% accuracy on real data."
  - "EDDM detected all critical drifts; ADWIN provided complementary unique detections."
  - "Static models fail as fraud patterns evolve; drift-aware systems maintain performance."
  - "CNN with preprocessing handles high-dimensional imbalanced transaction data effectively."
```