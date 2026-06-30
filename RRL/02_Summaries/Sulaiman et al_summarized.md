```yaml
paper_id: 10.24996/ijs.2024.65.4.42
designation: international
title: Credit Card Fraud Detection Challenges and Solutions: A Review
authors: Sulaiman, S. S.; Nadher, I.; Hameed, S. M.
year: 2024
venue: Iraqi Journal of Science
odin_topics:
  - 8.A
  - 8.B
  - 8.C
  - 12.A
  - 12.B
tldr: A review of credit card fraud detection challenges including class imbalance, concept drift, and verification latency, with a survey of machine learning and deep learning solutions.
problem_and_motivation: Credit card fraud is increasing with the growth of electronic payments, yet detection systems face significant challenges such as data imbalance and changing fraud patterns. A systematic review of these challenges and their proposed solutions is needed to guide the development of more robust fraud detection systems.
approach:
  - The paper is a literature review that synthesizes research on credit card fraud detection challenges.
  - It focuses on three core challenges: class imbalance, concept drift, and verification latency.
  - The review surveys both machine learning and deep learning techniques proposed to address these challenges.
  - It categorizes preprocessing techniques like undersampling, oversampling, and hybrid methods.
  - The paper also reviews concept drift handling methods including ensemble and sliding-window approaches.
  - Verification latency solutions such as active learning and importance weighting are examined.
  - It presents a comparative analysis of various detection techniques and datasets used in the literature.
  - The paper uses figures and tables to summarize the distribution of research and compare methods.
  - It identifies research gaps, particularly the limited attention to verification latency compared to other challenges.
findings:
  - num: 98% of transactions are legitimate, while only 2% are fraudulent, highlighting the extreme class imbalance.
  - The AllKNN-CatBoost model achieved 99.96% accuracy for credit card fraud detection.
  - SMOTE-Tomek improved results to 99% compared to 94% with random undersampling.
  - The CtRUSBoost approach achieved 95.7% precision, outperforming RUSBoost (85.9%), DT (49.5%), and SVM (67.8%).
  - The hybrid data-point approach enhanced predictive accuracy for SVM, RF, LR, and DT by 73%, 90%, 90%, and 100%, respectively.
  - Auto-encoder achieved an AUC of 96.03% for anomaly detection, outperforming Restricted Boltzmann Machine's 95.05%.
  - The hierarchical BKS-based framework achieved over 99% accuracy in identifying fraudulent transactions.
  - The LSTM-Attention Mechanism model achieved 96.72% accuracy on European Credit Card data.
  - Most research focuses on class imbalance, with fewer studies addressing verification latency.
key_figures_tables:
  - Figure 1: Global retail e-commerce sales growth from 2015 to 2025 → Shows the increasing reliance on online transactions.
  - Figure 2: Worldwide fraudulent card payment value from 2021 to 2027 → Illustrates the growing financial impact of fraud.
  - Figure 3: Distribution of published papers by publisher for challenges and techniques → Highlights research focus areas.
  - Table 1: Description of imbalance pre-processing techniques → Summarizes advantages and disadvantages of sampling methods.
  - Table 2: Description of concept drift techniques → Compares methods for handling changing data patterns.
  - Table 3: Comparison of verification latency techniques → Contrasts approaches for delayed supervised information.
  - Table 4: Comparative analysis of CCFD applications → Provides a comprehensive overview of techniques and performance.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: CCFD
    definition: Credit Card Fraud Detection
  - term: CCFDS
    definition: Credit Card Fraud Detection Systems
  - term: ML
    definition: Machine Learning
  - term: DL
    definition: Deep Learning
  - term: SMOTE
    definition: Synthetic Minority Oversampling Technique
  - term: RUS
    definition: Random Undersampling
  - term: RO
    definition: Random Oversampling
  - term: AUC
    definition: Area Under the Curve
  - term: MCC
    definition: Matthew Coefficient Correlation
  - term: SSB
    definition: Sample Selection Bias
  - term: EDM
    definition: Expert-Driven Model
  - term: DDM
    definition: Data-Driven Model
  - term: BKS
    definition: Behavior-Knowledge Space
critical_citations:
  - "[Dal Pozzolo et al., 2017] — Foundational work on realistic CCFD modeling and learning strategy."
  - "[Benchaji et al., 2021] — Key study on LSTM with attention mechanism for fraud detection."
  - "[Ahmad et al., 2022] — Proposed robust class balancing framework using fuzzy C-means."
  - "[Alfaiz and Fati, 2022] — Demonstrated high accuracy with AllKNN-CatBoost model."
  - "[Makki et al., 2019] — Comparative study of imbalanced classification approaches."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly addresses the detection of anomalous transactions, a core function for Odin.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Reviews various ML/DL algorithms specifically for detecting fraud anomalies.
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: medium
      justification: Discusses techniques for dealing with limited or delayed labeled data, relevant to cold-start.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides performance metrics like accuracy, AUC, and precision used in evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Compares the performance of different algorithmic modules for fraud detection.
  contribution: This review provides a comprehensive overview of anomaly detection techniques and their evaluation, directly informing the design of Odin's anomaly detection module. The analysis of class imbalance handling (8.A) and concept drift adaptation (8.B) offers methodological guidance for developing robust spending anomaly detection. The discussion of verification latency (8.C) raises awareness of practical constraints in real-world systems, which is relevant to Odin's feedback loop design. The paper's comparative performance data (12.A, 12.B) helps in selecting appropriate algorithms and evaluation metrics for Odin's algorithmic modules.
  directly_justifies:
    - "Class imbalance is a major challenge in anomaly detection systems."
    - "Hybrid sampling techniques like SMOTE-ENN improve detection performance."
    - "Concept drift requires frequent model updates to maintain accuracy."
    - "Evaluation metrics like AUC and precision are critical for comparing detection algorithms."
    - "Verification latency introduces challenges for supervised learning in real-time systems."
  limits:
    - "The review focuses on credit card fraud, not general personal spending behavior."
    - "It does not address the Filipino cultural or economic context."
    - "The review is not specific to personal finance management systems for young professionals."
    - "It does not cover mobile-first design or user experience considerations."
    - "The paper is a survey and does not present a novel algorithm or framework for Odin."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to the Anomaly Detection domain (8.A, 8.B) because its core subject is detecting fraudulent (anomalous) transactions. It was assessed as medium relevance for System Evaluation (12.A, 12.B) due to its extensive review of performance metrics and algorithm comparisons. The Behavioral Profiling (5.A-C), Forecasting (6.A-B), Budget Recommendation (7.A-D), and Savings & Debt Management (13.A-C) domains were rejected as the paper does not cover behavioral profiling, spending prediction, or budget allocation. The Filipino Cultural Context (2.A-D) and Demographic/Financial Structure domains (1.A-C) were also rejected, as the study is not focused on the Philippines. The paper's overall relevance to Odin is contextual and methodological, providing foundational knowledge on anomaly detection techniques and their evaluation, which can inform the design of Odin's anomaly detection module.
limitations:
  - "The review does not propose a specific solution for real-time anomaly detection with limited labeled data."
  - "The effectiveness of the surveyed techniques on non-credit card spending data is not discussed. [unacknowledged]"
  - "The paper does not address the scalability of these methods for a mobile-first personal finance app. [unacknowledged]"
  - "None."
remember_this:
  - "Class imbalance where 98% of transactions are normal is a key anomaly detection challenge."
  - "Hybrid sampling techniques like SMOTE-ENN achieve precision up to 90%."
  - "The AllKNN-CatBoost model attained 99.96% accuracy in fraud detection."
  - "Concept drift requires continuous model adaptation to maintain detection performance."
  - "Verification latency is a critical but under-addressed challenge in real-world detection systems."
```