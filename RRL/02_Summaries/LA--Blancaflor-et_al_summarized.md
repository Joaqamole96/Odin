```yaml
paper_id: 10.1145/3698062.3698088
designation: local-algorithm-specific
title: Exploring Machine Learning for Credit Card Fraud Detection from a Philippine Perspective
authors: Blancaflor, E.; Asuncion, K. D.; Reyes, H. J.; Verzosa, M.
year: 2024
venue: 2024 The 6th World Symposium on Software Engineering (WSSE)
odin_topics:
  - 8.A
  - 8.B
tldr: Examines machine learning techniques for credit card fraud detection tailored to the Philippine context, emphasizing SVM and ANN models.
problem_and_motivation: Credit card fraud in the Philippines has surged 21% since the pandemic, yet traditional fraud prevention systems are inadequate for securing e-commerce networks. There is a pressing need to evaluate and adapt machine learning models to the country's unique economic, technological, and social milieu to enhance financial security.
approach:
  - Reviews existing literature on fraud detection systems (FDS) and their limitations, such as imbalanced data and concept drift.
  - Assesses the efficacy of machine learning models including Logistic Regression, k-NN, Naïve Bayes, SVM, and ANN.
  - Compares the performance of ANN and Logistic Regression enhanced with Genetic Algorithm and SMOTE.
  - Evaluates models using metrics like accuracy, sensitivity, specificity, precision, Matthews Correlation Coefficient, and balanced classification rate.
  - Contextualizes findings within the Philippine financial sector, referencing local fraud cases and regulatory responses.
findings:
  - num: Credit card fraud in the Philippines increased by 21% since the COVID-19 outbreak.
  - num: Online fraud cost Filipino consumers over P540 million in 2021 alone.
  - num: ANN-SMOTE demonstrated the best performance in accuracy, precision, recall, and F1-score for fraud detection.
  - num: Logistic regression achieved an accuracy of 54.86%, while k-NN and Naïve Bayes achieved 97.69% and 97.92% respectively.
  - SVM shows promise for fraud detection, with potential for improved performance through meta-learning.
  - Machine learning models offer superior pattern detection and scalability, making them the future of fraud detection despite explainability trade-offs.
key_figures_tables:
  - Figure 1: Comparative performance of ANN and LR with GA/SMOTE enhancements → ANN-SMOTE outperforms all other models on key metrics.
  - Table 1: Evaluation of ML models for credit card fraud detection → Highlights accuracy and improvement strategies for each model.
key_equations:
  - equation: "MCC = (TP×TN - FP×FN) / √((TP+FP)(TP+FN)(TN+FP)(TN+FN))"
    explanation: Balanced measure for binary classification with imbalanced classes.
  - equation: "BCR = (Sensitivity + Specificity) / 2"
    explanation: Average recall or balanced accuracy for skewed datasets.
  - equation: "f(x) = sgn(x.w) + b"
    explanation: Decision function of SVM for binary classification.
definitions:
  - term: MCC
    definition: Matthews Correlation Coefficient, a balanced metric for binary classification.
  - term: BCR
    definition: Balanced Classification Rate, the average of sensitivity and specificity.
  - term: SMOTE
    definition: Synthetic Minority Over-sampling Technique, used to address imbalanced data.
  - term: FPS
    definition: Fraud Prevention System, a system designed to prevent fraudulent transactions.
  - term: FDS
    definition: Fraud Detection System, a system designed to detect fraudulent transactions.
critical_citations:
  - "[Awoyemi et al., 2017] — Comparative analysis of ML techniques for credit card fraud detection."
  - "[Abdallah et al., 2016] — Survey of fraud detection systems and their limitations."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly addresses fraud detection, a core anomaly detection application for Odin.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Reviews and evaluates algorithms (SVM, ANN) applicable to spending data anomaly detection.
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Provides context on the Philippine digital economy, which includes young professionals.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: low
      justification: Mentions the Philippine economic and social milieu but does not detail specific practices.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Briefly discusses existing fraud prevention systems but focuses on security, not personal finance management.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Discusses data security and privacy concerns in the context of fraud detection.
  contribution: This paper provides a foundational review of machine learning models for fraud detection, which directly informs Odin's Anomaly Detection module (8.A, 8.B). The comparative analysis of SVM and ANN with techniques like SMOTE offers a benchmark for algorithm selection. The findings on accuracy and performance metrics (MCC, BCR) guide the evaluation framework for Odin's detection capabilities. The emphasis on the Philippine context provides justification for tailoring anomaly detection algorithms to local spending patterns.
  directly_justifies:
    - "Machine learning models offer superior pattern detection for identifying fraudulent transactions in spending data."
    - "Support Vector Machines and Artificial Neural Networks are effective for binary classification of fraudulent and non-fraudulent patterns."
    - "SMOTE and other sampling techniques are crucial for handling imbalanced datasets common in anomaly detection."
    - "The trade-off between model explainability and accuracy must be considered when deploying fraud detection systems."
  limits:
    - "The paper is a literature review and does not present new empirical results from a Philippine dataset."
    - "The study does not specify the demographic profile (e.g., young professionals) of the fraud victims."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to the Anomaly Detection domain (topics 8.A and 8.B) because it directly evaluates ML algorithms for detecting credit card fraud, which is a key application of anomaly detection in PFMS. It was also flagged as medium relevance to Data Privacy & User Trust (10.A) due to its discussion of security and contextual for Filipino Cultural Context (1.A, 2.A) as it references the Philippine economic setting. Domains like Expense Categorization, Spending Forecasting, and Budget Recommendation were considered and rejected because the paper does not address spending patterns, income allocation, or financial planning. The overall relevance to Odin is primarily for its algorithmic insights into anomaly detection, particularly the choice of ML models and handling of imbalanced data.
limitations:
  - "The study is a literature review and does not include primary data collection or experimentation on Philippine fraud cases. [unacknowledged]"
  - "The comparison of model performance (e.g., Table 1) aggregates results from different studies, which may not be directly comparable due to varying datasets. [unacknowledged]"
  - "The paper does not address the cold-start problem for anomaly detection when user data is sparse. [unacknowledged]"
remember_this:
  - "Credit card fraud in the Philippines increased by 21% since the pandemic."
  - "ANN with SMOTE outperformed other models in detecting fraudulent transactions."
  - "Machine learning models are the future of fraud detection despite accuracy-explainability trade-offs."
  - "Traditional fraud prevention systems are inadequate for securing e-commerce networks."
```