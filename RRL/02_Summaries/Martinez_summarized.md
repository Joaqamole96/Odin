```yaml
paper_id: 10.21203/rs.3.rs-7893661/v1
designation: international-algorithm-specific
title: A Review of Machine Learning and Deep Learning Approaches for Fraud Detection Across Financial and Supply Chain Domains
authors: Martínez, Ó.
year: 2025
venue: Systematic Review (Preprint)
odin_topics:
  - "8.A"
  - "8.B"
  - "5.A"
  - "5.C"
  - "12.A"
  - "12.B"
  - "12.C"
tldr: A systematic review of machine learning and deep learning for fraud detection, evaluating traditional, ensemble, and semi-supervised methods across financial and supply chain domains.
problem_and_motivation: Fraud detection is critical yet challenging due to sophisticated schemes and extreme class imbalance. Traditional rule-based systems are inadequate, and a gap exists in comprehensive reviews bridging financial and supply chain fraud with modern ML/DL techniques.
approach:
  - "Conducted a systematic literature review following PRISMA guidelines."
  - "Searched multiple academic databases for studies published between 2015 and 2025."
  - "Screened 1,847 publications, resulting in a final corpus of 97 high-quality studies."
  - "Categorized methodologies into traditional ML, deep learning, ensemble, semi-supervised, and emerging technologies."
  - "Evaluated approaches based on performance metrics, imbalance handling, interpretability, and computational efficiency."
findings:
  - "num: Ensemble methods and tree-based models consistently achieve superior performance in credit card fraud detection, with AUC-ROC often exceeding 0.95."
  - "num: Semi-supervised approaches, such as two-phase frameworks combining Isolation Forest and self-training SVM, achieve an F1-score of 0.817 with a false positive rate under 3% in supply chain contexts."
  - "Deep learning methods like LSTM excel at capturing temporal dependencies but do not consistently outperform optimized gradient boosting on tabular data."
  - "Extreme class imbalance and concept drift remain fundamental challenges, with Borderline-SMOTE and ensemble methods offering the most effective mitigation."
  - "Explainable AI (XAI) techniques like SHAP and LIME are critical for regulatory compliance and can improve fraud analyst efficiency by 35%."
key_figures_tables:
  - "Table 8: Traditional ML performance → Random Forest offers the best balance for general-purpose fraud detection."
  - "Table 12: Training time comparison on IEEE-CIS scale → LightGBM is fastest among high-performance algorithms."
  - "Table 13: Inference latency per transaction → XGBoost and LightGBM meet sub-100ms real-time requirements."
  - "Table 15: Interpretability requirements by context → Regulatory and customer-facing contexts demand high interpretability."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "ML"
    definition: "Machine learning."
  - term: "DL"
    definition: "Deep learning."
  - term: "AUC-ROC"
    definition: "Area under the receiver operating characteristic curve."
  - term: "AUC-PR"
    definition: "Area under the precision-recall curve."
  - term: "SMOTE"
    definition: "Synthetic minority over-sampling technique."
  - term: "XAI"
    definition: "Explainable artificial intelligence."
  - term: "GNN"
    definition: "Graph neural network."
  - term: "LSTM"
    definition: "Long short-term memory network."
critical_citations:
  - "[Chawla et al., 2002] — Introduces SMOTE for handling class imbalance."
  - "[Chen & Guestrin, 2016] — Proposes XGBoost, a top-performing algorithm."
  - "[Moradi et al., 2025] — Comprehensive study on ensemble methods for fraud detection."
relevance:
  topics:
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Paper reviews anomaly detection as a core fraud detection technique."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Evaluates algorithms like Isolation Forest, Autoencoders, and LOF for anomaly detection."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "contextual"
      justification: "Discusses behavioral features but not in the context of profiling."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "contextual"
      justification: "Reviews classification approaches generally, not specifically for profile building."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides a comprehensive overview of evaluation metrics and protocols."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Compares performance of various algorithmic modules across domains."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "contextual"
      justification: "Focuses on fraud detection, not budget recommendation."
  contribution: "This review informs Odin's anomaly detection module by identifying state-of-the-art algorithms (e.g., Isolation Forest, XGBoost) and best practices for handling class imbalance. It supports the design of Odin's evaluation framework by detailing appropriate metrics (AUC-PR) and validation protocols. The findings justify the use of semi-supervised approaches for Odin in data-scarce scenarios. It provides a foundation for selecting the most effective and computationally efficient algorithms for real-time detection. It also highlights the importance of interpretability, guiding the integration of XAI techniques into Odin's decision-making process."
  directly_justifies:
    - "Ensemble methods like XGBoost and Random Forest are top performers for imbalanced tabular fraud data."
    - "A two-phase framework of unsupervised pre-filtering and semi-supervised refinement is effective with minimal labeled data."
    - "AUC-PR is the preferred metric for evaluating models on extremely imbalanced datasets."
    - "Concept drift necessitates frequent model retraining or online learning strategies."
    - "Explainable AI is essential for regulatory compliance and user trust."
  limits:
    - "The review's primary focus is on credit card and supply chain fraud, with less emphasis on other domains."
    - "Findings are based on public benchmarks, which may not fully represent proprietary industry data patterns."
  mapping_rationale: "The paper was systematically scanned against all 12 functional domains. Domains related to Anomaly Detection (8.A, 8.B) were flagged as high relevance due to the paper's core subject. System Evaluation (12.A, 12.B, 12.C) was assessed as medium relevance because it provides extensive benchmarking and evaluation frameworks. Behavioral Profiling (5.A, 5.C) was considered contextual, as the paper discusses behavioral features and general classification but does not focus on building user profiles for financial management. Domains concerning Filipino cultural context, expense categorization, existing systems, forecasting, budgeting, mobile design, privacy, retention, and savings/debt management were considered and rejected as the paper does not address these specific Odin concerns. The overall relevance is high for informing the technical design of anomaly detection and evaluation components within Odin."
limitations:
  - "Reliance on public benchmarks may limit generalizability to proprietary industry data."
  - "Deep learning for fraud is covered, but practical deployment details are often abstracted away."
  - "The review does not provide a novel algorithmic contribution, only a synthesis of existing work."
remember_this:
  - "Ensemble methods like XGBoost and stacking are the current state-of-the-art."
  - "Semi-supervised learning is highly effective when fraud labels are scarce."
  - "Concept drift requires continuous model adaptation for sustained performance."
  - "Explainable AI is crucial for regulatory compliance and building user trust."
  - "Borderline-SMOTE is a top choice for addressing extreme class imbalance."
```