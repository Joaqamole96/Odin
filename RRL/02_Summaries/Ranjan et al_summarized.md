```yaml
paper_id: 10.59256/ijsreat.20250505011
designation: international
title: Online Payment Fraud Detection Using Decission Tree and LSTM Neural Network
authors: Ranjan, A.; Jangir, A.K.; Abrol, K.; Saurav, S.
year: 2025
venue: International Journal of Scientific Research in Engineering & Technology
odin_topics:
  - 8.A
  - 8.B
tldr: A hybrid fraud detection system combines Decision Trees for rapid, interpretable screening with LSTM networks for sequential transaction analysis and temporal pattern recognition.
problem_and_motivation: Online payment fraud is escalating in sophistication, rendering traditional rule-based systems obsolete. There is a critical need for adaptive, data-driven frameworks that can learn evolving fraud patterns. Existing approaches lack the capacity to combine static, interpretable rules with the temporal intelligence required for modern fraud detection.
approach:
  - The study conducts a systematic literature review of machine learning and deep learning techniques for online payment fraud detection.
  - It synthesizes findings from peer-reviewed papers, focusing on Decision Trees, Random Forests, and LSTM neural networks.
  - The review analyzes common preprocessing steps including SMOTE for class imbalance and feature engineering for temporal data.
  - It describes a two-stage hybrid architecture where Decision Trees flag high-risk transactions for subsequent LSTM analysis.
  - The paper evaluates models using standard metrics such as precision, recall, F1-score, and ROC-AUC from the reviewed literature.
findings:
  - Decision Trees and Random Forests provide fast, interpretable baselines for fraud screening, often executing in less than one millisecond per transaction.
  - LSTM networks significantly outperform baseline models by effectively modeling temporal sequences and capturing long-term behavioral changes.
  - Hybrid models combining tree-based methods and LSTMs achieve superior results compared to standalone approaches by leveraging the strengths of each.
  - Addressing class imbalance via SMOTE is critical for improving model sensitivity to fraudulent transactions.
  - Feature engineering, including time-window aggregates and sequential encoding, substantially improves deep learning model accuracy.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network architecture designed to model sequential data and long-term dependencies.
  - term: SMOTE
    definition: Synthetic Minority Oversampling Technique, a method for addressing class imbalance by generating synthetic samples for the minority class.
  - term: ROC-AUC
    definition: Receiver Operating Characteristic - Area Under the Curve, a performance metric for binary classification that measures the model's ability to distinguish between classes.
critical_citations:
  - "[Jurgovsky et al., 2018] — Foundational for LSTM use in fraud detection."
  - "[Roy et al., 2018] — Key comparison of Decision Tree and Random Forest."
  - "[Nashaat and Khorasgani, 2021] — Key hybrid model architecture."
  - "[Fiore et al., 2019] — Key study on LSTM and feature engineering."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Provides general background on fraud as an anomaly detection problem.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Surveys algorithms like LSTM and Decision Trees applicable to anomaly detection.
  contribution: The paper surveys hybrid ML techniques for fraud detection, which could inform Odin's anomaly detection module (8.A, 8.B) for identifying unusual spending patterns. While the context is general online payments, the core algorithms (LSTM, Decision Trees) are transferable to personal finance transaction data. The review of SMOTE and feature engineering offers practical preprocessing strategies that could be adapted for Odin's spending data. The emphasis on real-time processing aligns with Odin's need for responsive anomaly detection.
  directly_justifies:
    - LSTM networks are effective for modeling temporal sequences in transaction data.
    - Hybrid models combining interpretable rules and deep learning achieve superior detection performance.
    - SMOTE is a standard technique to handle class imbalance in fraud detection.
  limits:
    - The paper is a survey and does not present original empirical results or a novel model.
    - The review is specific to fraud detection, which may not directly translate to all aspects of financial anomaly detection for personal budgeting.
    - The focus is on general online payments, not the specific spending patterns of a PFMS user.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The primary domain flagged as relevant was Anomaly Detection, as the paper focuses on a core problem of that domain (fraud identification). Within this domain, topic codes 8.A and 8.B were selected with a 'low' relevance level because the paper provides a broad survey of general algorithms (LSTM, Decision Trees) applicable to anomaly detection, but does not address the specific challenges of a PFMS like Odin. The domain was selected because the foundational concepts of fraud detection, such as identifying outliers and using temporal patterns, are directly transferable. All other functional domains (e.g., Filipino Cultural Context, Expense Categorization, Behavioral Profiling, etc.) were considered and rejected because the paper does not address cultural factors, user financial behavior, budgeting, system evaluation, or any other Odin-specific domain. The paper's focus is purely technical and domain-agnostic, providing only a general algorithmic background that could be a starting point for designing Odin's anomaly detection module but lacks any specific contextual or user-centric insights. Overall, the paper's relevance to Odin is limited to providing a high-level overview of potential algorithmic approaches for anomaly detection.
limitations:
  - The paper is a survey, not a primary research study with novel contributions. [unacknowledged]
  - It does not address the specific characteristics of personal finance data in a PFMS context. [unacknowledged]
  - The review does not cover the integration of anomaly detection with other PFMS modules like budgeting or forecasting. [unacknowledged]
remember_this:
  - Hybrid models combining Decision Trees and LSTMs are effective for fraud detection.
  - LSTM networks excel at capturing temporal patterns in sequential transaction data.
  - SMOTE is a standard technique for handling class imbalance in fraud detection.
  - Decision Trees offer fast, interpretable screening for real-time applications.
```