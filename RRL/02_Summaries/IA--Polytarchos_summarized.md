```yaml
paper_id: 10.47852/bonviewFSI52026108
designation: international-algorithm-specific
title: Credit Card Fraud Detection Through Deep Learning and Real-Time Data Streams: A Comparison and New Directions
authors: Polytarchos, E.
year: 2025
venue: FinTech and Sustainable Innovation
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
tldr: Compares deep learning and real-time data stream analysis for credit card fraud detection, finding deep learning more accurate but real-time clustering more adaptable and faster.
problem_and_motivation: Credit card fraud detection systems face a critical gap between high-accuracy batch-trained models and real-time adaptability needed for dynamic financial environments. Existing literature lacks a comprehensive empirical comparison of unsupervised stream-based methods against deep learning approaches. This comparison is essential for system designers to make informed deployment decisions.
approach:
  - Used two proprietary datasets: IND (17.5M individual transactions) and SUM (1.2M purchase summaries) for a single year.
  - Deep learning pipeline: trained LSTM and MLP models to classify customer labels and computed an ensemble-based Scale of Suspicious Transaction (SST).
  - Real-time pipeline: implemented the BEReTiC system using CluNN for clustering and KNN for classification on streaming data without preprocessing.
  - Injected 1000 synthetic fraudulent transactions into the IND dataset to evaluate detection capability.
  - Evaluated both approaches on accuracy, fraud detection rate, false positives, and adaptability.
findings:
  - LSTM achieved up to 92% accuracy in predicting total funds range, while real-time clustering achieved only 66% for the same label.
  - num: Deep learning detected 788 out of 1000 injected fraudulent transactions.
  - num: Real-time clustering detected 619 out of 1000 injected fraudulent transactions.
  - num: Real-time clustering produced fewer false positives (574) compared to deep learning (1340).
  - num: Real-time clustering had a lower misclassification rate (0.003%) than deep learning (0.007%).
  - Real-time clustering is inherently adaptive and can identify emerging fraud patterns without retraining.
  - Deep learning requires extensive preprocessing and frequent retraining, limiting real-time applicability.
  - A hybrid model integrating both techniques is proposed as a more effective solution.
key_figures_tables:
  - Table 1: Classification accuracy by label → LSTM highest at 92%, real-time clustering lower.
  - Table 2: Fraud detection performance → Deep learning detects more fraud (788 vs 619) but more false positives.
  - Table 3: Methodology trade-offs → Deep learning has high accuracy but high latency; real-time clustering has moderate accuracy but low latency.
key_equations:
  - equation: SST = percentage of classifiers that misclassified a transaction
    explanation: Scale of Suspicious Transaction for fraud scoring.
  - equation: CSST = product of accuracies of misclassifying classifiers
    explanation: Confidence of the SST score.
definitions:
  - term: BEReTiC
    definition: Best Effort Real-Time Clustering and Classification adapter for streaming data.
  - term: CluNN
    definition: Clustering algorithm used in the BEReTiC system.
  - term: SCoDe2
    definition: Sample collector and deviation detector module in BEReTiC.
  - term: SST
    definition: Scale of Suspicious Transaction, the percentage of classifiers that misclassified a transaction.
  - term: CSST
    definition: Confidence of the Scale of Suspicious Transaction.
  - term: Gower similarity
    definition: Metric combining categorical and numerical data for comparison.
critical_citations:
  - "[Polytarchos et al., 2024] — Patent for BEReTiC system."
  - "[Goodfellow et al., 2020] — Generative adversarial networks for fraud detection."
  - "[Li et al., 2022] — ECOD method for unsupervised outlier detection."
  - "[Huang et al., 2023] — Score-guided networks for anomaly detection."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Compares deep learning and real-time models for predictive fraud detection.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: LSTM networks are evaluated on sequential transaction data.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Core focus is anomaly detection for credit card fraud.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Compares LSTM and real-time clustering as anomaly detection algorithms.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides a comparative evaluation of two detection approaches.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Evaluates LSTM, MLP, and BEReTiC algorithmic modules.
  contribution: This paper provides a direct comparison between batch-trained deep learning models and real-time streaming algorithms for anomaly detection, a core function of Odin's fraud detection module. The evaluation metrics (accuracy, false positives, adaptability) are directly applicable to assessing Odin's algorithmic components. The finding that deep learning offers higher accuracy while real-time methods offer faster detection informs trade-offs in Odin's design. The proposed hybrid model suggests a potential architecture for balancing accuracy and responsiveness.
  directly_justifies:
    - Real-time clustering can detect anomalies in streaming data without preprocessing.
    - Deep learning models require extensive retraining to adapt to new fraud patterns.
    - A hybrid model can combine high accuracy with real-time adaptability.
    - False positive rates are a critical metric for user trust in anomaly detection systems.
  limits:
    - The study focuses on credit card fraud, not general personal finance anomaly detection.
    - Real-time clustering accuracy was substantially lower than deep learning.
    - The proprietary dataset limits reproducibility and generalizability.
    - The study does not address user-facing trust or explainability concerns.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated canonical topic codes was performed. The paper was flagged as relevant to the Anomaly Detection domain (8.A, 8.B) due to its primary focus on fraud detection algorithms. It also touches on Predictive Modeling (6.A, 6.B) through its use of LSTM networks and evaluation of forecasting approaches. The comparative evaluation framework (12.A, 12.B) is relevant for assessing Odin's algorithmic modules. Borderline cases included the paper's mention of gamified challenges (which touches 11.A) and customer profiling (5.A), but these were considered too tangential for inclusion. Domains such as Filipino Cultural Context, Expense Categorization, Data Privacy, and Mobile Design were rejected as the paper does not address these topics. Overall, the paper offers medium to high relevance for Odin's anomaly detection and evaluation modules, but low relevance for other domains.
limitations:
  - The study uses a proprietary dataset, limiting reproducibility. [unacknowledged]
  - Real-time clustering accuracy was substantially lower than deep learning. [acknowledged]
  - The paper does not address false positive impact on user trust or experience. [unacknowledged]
  - The hybrid model is proposed but not implemented or evaluated. [acknowledged]
remember_this:
  - Deep learning achieved 92% accuracy in classifying customer total funds range.
  - Real-time clustering detected 619 of 1000 injected frauds with fewer false positives.
  - A hybrid model integrating both approaches is suggested for optimal performance.
  - Real-time methods adapt to new fraud patterns without retraining.
  - Deep learning requires extensive preprocessing and is not ideal for real-time use.
```