```yaml
paper_id: 10.3390/app13116515
designation: international
title: Concept Drift Adaptation Methods under the Deep Learning Framework: A Literature Review
authors: Xiang, Q.; Zi, L.; Cong, X.; Wang, Y.
year: 2023
venue: Applied Sciences
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 7.B
  - 7.C
  - 11.A
  - 12.A
  - 12.B
tldr: A literature review systematically classifying concept drift adaptation methods within deep learning, covering discriminative, generative, hybrid, and other frameworks.
problem_and_motivation: Deep learning models degrade when data distributions change (concept drift). Existing reviews on concept drift lack a dedicated focus on methods under the deep learning framework, which is crucial for modern AI-driven decision systems.
approach:
  - The paper conducts a literature review of concept drift adaptation methods.
  - It classifies methods into four deep learning categories: discriminative, generative, hybrid, and others (deep reinforcement/transfer learning).
  - For each category, it details update modes (parameter/structure), detection modes (active/passive), and types of drift handled.
  - It synthesizes findings from representative algorithms (e.g., SEOA, OARNN, ARCUS, HSN-LSTM, DeepPocket).
  - The review also covers common datasets, evaluation metrics, and identifies future research directions.
findings:
  - num: Discriminative and hybrid learning methods are most prevalent in concept drift adaptation.
  - num: Parameter updates are more common than structural updates due to faster convergence.
  - Active detection modes are widely used for explaining drift occurrence and saving computational resources.
  - Abrupt drift is the most frequently adapted type, while recurring drift is the least addressed.
  - Common challenges include high computational cost, slow convergence, and handling imbalanced data streams.
key_figures_tables:
  - "Figure 2: Types of concept drift (abrupt, incremental, gradual, recurring) → Visual classification of drift patterns."
  - "Table 1: Discriminant learning methods summary → Overview of MLP, RNN, LSTM, CNN methods and their limitations."
  - "Table 2: Generative learning methods summary → Overview of AE, GAN, RBM, SOM methods and their limitations."
  - "Table 3: Hybrid learning methods summary → Overview of LSTM+CNN, RNN+ARIMA etc., and their limitations."
key_equations:
  - equation: $P_{t0}(x,y) \neq P_{t1}(x,y)$
    explanation: Formal definition of concept drift occurrence.
  - equation: $MCC = \frac{TP \times TN - FP \times FN}{\sqrt{(TP+FP)(TP+FN)(TN+FP)(TN+FN)}}$
    explanation: Matthews correlation coefficient for imbalanced data evaluation.
definitions:
  - term: Concept Drift
    definition: Change in the underlying data stream distribution over time.
  - term: Virtual Concept Drift
    definition: Change in feature space distribution without affecting decision boundaries.
  - term: Real Concept Drift
    definition: Change in conditional probability distribution, affecting the prediction model.
  - term: Active Detection
    definition: Using a dedicated algorithm to trigger model updates upon detecting drift.
  - term: Passive Detection
    definition: Continuously adjusting the model without explicit drift detection.
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network variant for sequence data.
  - term: GAN
    definition: Generative Adversarial Network, for generating new data similar to training data.
  - term: DRL
    definition: Deep Reinforcement Learning, combining deep learning with reinforcement learning.
  - term: DTL
    definition: Deep Transfer Learning, transferring knowledge from one model to another.
  - term: AE
    definition: Autoencoder, for unsupervised feature learning and dimensionality reduction.
critical_citations:
  - "[Gama et al., 2014] — Foundational survey on concept drift adaptation."
  - "[Lu et al., 2018] — Comprehensive review of learning under concept drift."
  - "[Webb et al., 2016] — Characterized concept drift types."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly discusses forecasting models and adapting to changing data distributions.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Reviews RNN/LSTM-based algorithms for time-series prediction under drift.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly discusses anomaly detection in data streams with concept drift.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Reviews algorithms like I-LSTM and MemStream for anomaly detection under drift.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Provides a framework for adapting recommendations to changing user behavior.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: medium
      justification: Concept drift adaptation is a form of constrained optimization in dynamic environments.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: contextual
      justification: Maintaining model accuracy through adaptation is key to sustained user engagement.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Reviews evaluation metrics like accuracy, F1, MAE, and RMSE for streaming data.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides a detailed evaluation of algorithmic modules for drift adaptation.
  contribution: This review provides a taxonomy of concept drift adaptation methods that directly informs Odin's forecasting and anomaly detection modules. For Odin's spending forecasting (6.A), the review of LSTM-based online adaptive models offers a methodological baseline for dynamic prediction. For anomaly detection (8.A/8.B), the surveyed algorithms like I-LSTM and MemStream provide approaches for detecting irregular spending patterns. The paper's discussion on parameter vs. structural updates (7.C) is directly relevant to Odin's budget allocation and recommendation systems, which must adapt to user-defined constraints. The review's summary of evaluation metrics (12.A/12.B) for streaming data offers a framework for assessing Odin's algorithmic modules.
  directly_justifies:
    - "Online adaptive RNN models are effective for load forecasting under concept drift."
    - "LSTM-based anomaly detection algorithms can be enhanced with drift detection."
    - "Parameter updates reduce convergence time for abrupt concept drift."
    - "Active drift detection modes explain the occurrence of drift and save computing resources."
  limits:
    - "The paper is a literature review and does not present new empirical results."
    - "It does not specifically evaluate concept drift adaptation methods on financial spending data."
    - "The review is focused on deep learning methods and omits classical statistical or shallow methods."
  mapping_rationale: A systematic scan was performed across all 12 functional domains and their associated topic codes. The domains of 'Spending Forecasting' (6.A, 6.B) and 'Anomaly Detection' (8.A, 8.B) were flagged as highly relevant because the paper directly reviews deep learning methods designed to handle concept drift in streaming data for these exact tasks. The 'Budget Recommendation' domain (7.B, 7.C) was assigned medium relevance as the paper's discussion of model update strategies (parameter vs. structure) informs how a recommender system can adapt to changing user financial behavior. 'Engagement Dynamics' (11.A) was considered contextual, as accurate adaptive models would likely improve user trust and retention, though this is not a focus. 'System Evaluation' (12.A, 12.B) was also deemed highly relevant due to its comprehensive review of evaluation metrics for streaming algorithms. Topics related to 'Filipino Cultural Context' (2.A-D) and 'Data Privacy' (10.A) were considered and rejected as they are not addressed in the paper's scope, which is purely methodological. The overall relevance to Odin is high for its forecasting and detection modules, but contextual for user-centric or cultural aspects.
limitations:
  - "Does not provide empirical validation of the reviewed methods on financial data."
  - "Lacks a comparative analysis of the different adaptation methods' performance in a unified setting. [unacknowledged]"
  - "Focuses exclusively on deep learning, potentially overlooking simpler or more interpretable methods. [unacknowledged]"
  - "Does not discuss the practical implementation challenges of these methods in a mobile-first environment."
remember_this:
  - "Concept drift causes deep learning model degradation, affecting prediction accuracy."
  - "Parameter updates are faster than structural updates for adapting to concept drift."
  - "Abrupt drift is the most commonly addressed type in the reviewed literature."
  - "A common challenge is balancing old and new data during online model updates."
  - "Active detection modes are useful for explaining drift but add computational overhead."
```