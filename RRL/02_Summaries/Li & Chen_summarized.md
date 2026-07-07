```yaml
paper_id: 10.1007/s10791-025-09549-7
designation: international-algorithm-specific
title: Dynamic quantification anti‑fraud machine learning model for real‑time transaction fraud detection in banking
authors: Li, F.; Chen, Z.
year: 2025
venue: Discover Computing
odin_topics:
  - 4.A
  - 4.B
  - 8.A
  - 8.B
  - 12.A
tldr: A dynamic quantification anti-fraud model combining expert rules, double machine learning, and real-time transaction flows detects fraud with a recall of 0.506 and reduces implicated card proportions by 30 percentage points post-deployment.
problem_and_motivation: Traditional anti-fraud models suffer from poor real-time performance and high false positive rates. Expert rules lack adaptability, while machine learning is computationally intensive, hindering proactive fraud prevention. A model that balances accuracy, speed, and dynamic adaptation is needed for banking transaction monitoring.
approach:
  - Data from Agricultural Bank of China Zhejiang Branch (Jan 2022-Jun 2023) with positive samples defined by low assets and large unfamiliar transfers.
  - Built 20+ expert-defined transactional features (e.g., small amount test, unfamiliar counterparty transfer) with F-Beta scores.
  - Used Double Machine Learning (DML) with LightGBM and XGBoost to quantify feature weights and causal impacts on fraud outcomes.
  - Applied logarithmic transformation and regularization to balance feature contributions and control false positives.
  - Deployed in a banking production system with dynamic threshold adjustment based on branch capacity and complaint rates.
findings:
  - num: The model achieved a recall of 0.506 on a test sample of 633 implicated cards in July 2023.
  - num: Post-deployment, the bank's proportion of implicated cards dropped by 30 percentage points from over 50% to 20%.
  - num: The bank's ranking for implicated cards fell from first to fourth among four banks in the province.
  - num: The model generated 170,594 clues over six months, demonstrating significant real-world operational impact.
  - num: The false positive rate was estimated between 0.15 and 0.20, with an F1-score of 0.32-0.38.
  - The model processes transactions in 5-10 seconds, enabling near-instantaneous interception.
  - Dynamic weight adjustment allows the model to adapt to evolving fraud patterns.
  - The model reduces operational costs by 30-40% compared to XGBoost due to fewer false positives.
key_figures_tables:
  - Table 1: F-Beta scores for 20+ expert features → Shows feature performance variation, justifying logarithmic transformation.
  - Figure 1: Prediction procedure flowchart → Outlines the real-time data retrieval and risk scoring process.
  - Figure 2: DML causal inference workflow → Illustrates the residual-based feature weighting mechanism.
  - Figure 3: Nominal distribution of f-beta values → Demonstrates the need for logarithmic scaling to balance features.
key_equations:
  - equation: F_\beta = (1 + \beta^2) \frac{Precision \times Recall}{\beta^2 Precision + Recall}
    explanation: F-beta score balances precision and recall, with beta emphasizing recall.
  - equation: F(x) = \sum_{i \in \mathbf{I}_x} W(i) \frac{\log_{10}(1000 \cdot (F_\beta)_i)}{\log_{10}(1000 \cdot (F_\beta)_{\max})}
    explanation: Multi-feature weighted combination with logarithmic normalization.
  - equation: R(x) = \sum_{j \in \mathbf{J}} \frac{-n (F_\beta)_j}{m}
    explanation: Regularization penalty based on complaint rates to control false positives.
definitions:
  - term: Double Machine Learning (DML)
    definition: A framework using machine learning to estimate causal effects by residualizing treatment and outcome variables.
  - term: F-Beta Score
    definition: A weighted harmonic mean of precision and recall, prioritizing recall with beta > 1.
  - term: Implicated Card
    definition: A bank account suspected of being involved in fraudulent activity.
  - term: CART
    definition: Classification and Regression Trees, used as base learners in the DML framework.
critical_citations:
  - "[Chernozhukov et al., 2018] — Introduces the DML framework for causal inference."
  - "[Islam et al., 2024] — Demonstrates rule-based fraud detection, highlighting limitations."
  - "[Yang et al., 2025] — Proposes ensemble BRB for fraud detection, relevant to combining expert rules."
  - "[Afriyie et al., 2023] — Compares ML algorithms, providing baseline performance context."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews expert rules and ML systems for fraud detection.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies poor real-time performance and high false positives in current systems.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly addresses anomaly detection for fraudulent transactions.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Proposes a novel algorithm (DML + expert rules) for real-time anomaly scoring.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses recall, FPR, and real-world deployment metrics to evaluate model performance.
  contribution: The paper provides a real-time anomaly detection model that combines expert rules and double machine learning, offering a practical solution for high-volume transaction monitoring. This directly informs Odin's anomaly detection module by presenting a method to quantify risk scores dynamically. The regularization based on complaint rates is a key design consideration for managing false positives. The 5-10 second processing latency sets a benchmark for Odin's real-time requirements. The approach of using F-beta features for risk classification offers a structured way to integrate domain knowledge into machine learning.
  directly_justifies:
    - DML can quantify feature importance for fraud detection, improving model interpretability.
    - Real-time transaction streams enable dynamic weight adjustment based on recent false positive rates.
    - Regularization using complaint rates balances detection and user inconvenience.
    - A recall of 0.506 demonstrates the feasibility of detecting fraud in imbalanced transaction data.
    - Post-deployment metrics show that dynamic thresholds can reduce false positives by 30-40%.
  limits:
    - The model was tested primarily on low-asset accounts, limiting generalizability to other segments.
    - The paper does not report stratified results for different asset tiers or external validation.
    - Potential bias in dataset composition is acknowledged but not quantified.
    - Reliance on 20+ expert-defined features may introduce redundancy and manual engineering overhead.
    - The recall is calculated on a test set, but confidence intervals are not provided.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper is most relevant to the 'Anomaly Detection' domain (codes 8.A, 8.B) as its core contribution is a real-time fraud detection algorithm. It also relates to 'Existing Systems & Gaps' (4.A, 4.B) by critiquing traditional methods and identifying their limitations. The 'System Evaluation' domain (12.A) is relevant due to the use of recall, FPR, and deployment metrics. Domains like 'Behavioral Profiling' (5.A-C) and 'Budget Recommendation' (7.A-D) were considered but rejected, as the paper does not address user behavior profiling or budget allocation. The 'Data Privacy' (10.A-B) and 'Retention' (11.A-B) domains are not directly addressed. The paper's focus on algorithmic technique and international (Chinese) context leads to a designation of 'international-algorithm-specific'. Overall, the paper provides direct evidence for designing a real-time, adaptive anomaly detection module for Odin, emphasizing the trade-off between recall and false positive management.
limitations:
  - Potential biases in the dataset due to over- or under-representation of transaction types. [unacknowledged]
  - The model's reliance on transaction data neglects other data sources like demographics or social media. [acknowledged]
  - Generalizability is limited as the study focuses on low-asset accounts (≤ 5000 RMB). [unacknowledged]
  - The paper does not report confidence intervals for key metrics like recall (0.506). [unacknowledged]
  - Feature selection relies on expert-defined rules rather than automated methods, limiting transparency. [unacknowledged]
remember_this:
  - The model achieved a recall of 0.506 on a test sample of 633 implicated cards.
  - Post-deployment, the bank's proportion of implicated cards dropped by 30 percentage points.
  - Double machine learning quantifies feature weights for dynamic risk scoring.
  - Regularization via complaint rates balances detection accuracy and user inconvenience.
  - Real-time processing latency of 5-10 seconds is critical for transaction interception.
```