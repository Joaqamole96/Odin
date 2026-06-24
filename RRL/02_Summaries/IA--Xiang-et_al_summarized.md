```yaml
paper_id: 10.3390/app13116515
designation: international
title: Concept Drift Adaptation Methods under the Deep Learning Framework: A Literature Review
authors: Xiang, Q.; Zi, L.; Cong, X.; Wang, Y.
year: 2023
venue: Applied Sciences
odin_topics:
  - 4.B
  - 5.B
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 12.A
tldr: A literature review that systematically categorizes concept drift adaptation methods within the deep learning framework, covering discriminative, generative, hybrid, and other learning approaches for dynamic data streams.
problem_and_motivation: Deep learning models degrade when data distributions change due to concept drift, particularly in dynamic environments like epidemics and big data. Existing surveys lack a focused review of adaptation methods specifically under the deep learning framework. This gap hinders decision-makers from effectively utilizing deep learning for timely and accurate predictions amidst evolving data streams.
approach:
  - The paper provides a formal definition of concept drift, distinguishing between real, virtual, and hybrid drift, and outlines their causes.
  - It establishes a general process for concept drift adaptation, explaining update modes (parameter vs. structure) and detection modes (active vs. passive).
  - A taxonomy is built to classify adaptation methods into discriminative learning, generative learning, hybrid learning, and other deep learning paradigms.
  - For each category, the review details representative algorithms, their specific update/detection modes, the types of drift they address, and their application domains.
  - The paper summarizes common datasets and evaluation metrics used for benchmarking, and concludes with a discussion of current challenges and future research directions.
findings:
  - Discriminative learning-based methods, particularly MLPs and RNNs, are the most widely used for handling concept drift in streaming data.
  - Active detection combined with parameter updates is the most common strategy for adapting deep learning models to concept drift.
  - Hybrid models, especially LSTM combined with other architectures, are prevalent for capturing long-term dependencies and adapting to drifts in time-series data.
  - Deep reinforcement learning and deep transfer learning are emerging areas for adapting to concept drift in complex, non-stationary environments.
  - num: The review analyzes over 40 different algorithms, highlighting that abrupt drift is the most frequently addressed type, while recurring drift receives the least attention.
key_figures_tables:
  - Figure 1: Visualization of causes for virtual, real, and hybrid concept drift → Illustrates how data distribution changes affect the decision boundary.
  - Figure 2: Types of concept drift over time → Shows abrupt, incremental, gradual, and recurring drift patterns.
  - Figure 3: General process of concept drift adaptation under deep learning → Outlines the steps from data input to model update.
  - Figure 4: A taxonomy of concept drift adaptation methods → Categorizes methods into discriminative, generative, hybrid, and other deep learning techniques.
  - Table 1: Summary of discriminative learning-based methods → Provides an overview of algorithms, detection modes, update modes, adaptation drift types, and limitations.
  - Table 2: Summary of generative learning-based methods → Details methods using autoencoders, GANs, RBMs, and SOMs for drift adaptation.
  - Table 3: Summary of hybrid learning-based methods → Highlights combined models like LSTM+CNN and their characteristics.
  - Table 4: Summary of other concept drift adaptation methods → Covers deep transfer learning and deep reinforcement learning approaches.
key_equations:
  - equation: $P_{t0}(x,y) \neq P_{t1}(x,y)$
    explanation: Formal definition of concept drift as a change in joint probability distribution over time.
  - equation: $P(y|x) = \frac{P(y) * P(x|y)}{P(x)}$
    explanation: Bayes theorem showing how real concept drift can be indirectly caused by changes in prior or likelihood.
  - equation: $T(v_o, v_r, n_o, n_r) = \frac{|v_o/n_o - v_r/n_r| - 0.5 \times (1/n_o + 1/n_r)}{\sqrt{\mu + (1-\mu) \times (1/n_o + 1/n_r)}}$
    explanation: Statistical test used in STEPD to compare accuracies between two windows for drift detection.
  - equation: $MCC = \frac{TP \times TN - FP \times FN}{\sqrt{(TP+FP)(TP+FN)(TN+FP)(TN+FN)}}$
    explanation: Matthews correlation coefficient, a balanced measure for classification performance on imbalanced data.
definitions:
  - term: Concept Drift
    definition: The change in the underlying data stream distribution over time, which can degrade the performance of a predictive model.
  - term: Real Concept Drift
    definition: A change in the conditional probability P(y|x), which directly affects the decision boundary and model predictions.
  - term: Virtual Concept Drift
    definition: A change in the distribution of input features P(x) without affecting the decision boundary P(y|x).
  - term: Parameter Update
    definition: Updating the weights of a deep learning model to adapt to new data without changing its architecture.
  - term: Structural Update
    definition: Modifying the architecture of a deep learning model, such as by adding or removing nodes or layers.
  - term: Active Detection
    definition: A mode where a separate algorithm is used to explicitly detect concept drift before triggering a model update.
  - term: Passive Detection
    definition: A mode where the model is continuously updated in response to incoming data without an explicit drift detection step.
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network variant designed to handle long-term dependencies in sequence data.
  - term: GAN
    definition: Generative Adversarial Network, a deep learning framework for generating new data instances that resemble the training data.
  - term: DRL
    definition: Deep Reinforcement Learning, which combines deep learning's perceptual abilities with reinforcement learning's decision-making capabilities.
critical_citations:
  - "[Schlimmer and Granger, 1986] — First proposed the concept of concept drift in machine learning."
  - "[Gama et al., 2014] — A comprehensive survey on concept drift adaptation covering four key aspects."
  - "[Lu et al., 2018] — A broad review on learning under concept drift, covering multiple dimensions like drift type and imbalance."
  - "[Webb et al., 2016] — Characterizes concept drift and provides a framework for analyzing its different types."
relevance:
  topics:
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly addresses the limitation of deep learning models degrading under concept drift, a key gap in PFMS.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: medium
      justification: Discusses the challenge of adapting to recurring drift, which parallels the cold-start problem and the need for dynamic user profiles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: The entire paper is a review of predictive modeling techniques (deep learning) that are essential for forecasting in PFMS.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Reviews RNNs and LSTMs, which are core algorithms for forecasting sequential financial data like spending.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Covers concept drift adaptation methods specifically applied to anomaly detection, a core function for identifying fraudulent or unusual transactions.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Reviews algorithms like I-LSTM, MemStream, and ARCUS that are directly applicable to anomaly detection in data streams.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Summarizes evaluation metrics (accuracy, MCC, RMSE) and datasets (KDD Cup, Electricity) that can be used to benchmark PFMS modules.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides a general landscape of concept drift adaptation methods, which is foundational to understanding potential integrations into PFMS.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: low
      justification: No direct mention of handling infeasible recommendations, a key aspect of budget allocation.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Mentions federated learning (FedHAR) as a method that can handle concept drift while preserving privacy, but this is not a primary focus.
  contribution: This review paper contributes a comprehensive taxonomy of concept drift adaptation methods under the deep learning framework. Its categorization into discriminative, generative, hybrid, and other learning approaches provides a clear structure for understanding the landscape of available techniques. For Odin, this is crucial as it helps us identify state-of-the-art deep learning algorithms for key modules. Specifically, it guides our selection of RNNs/LSTMs for the spending forecasting module and GANs/autoencoders for the anomaly detection module. Furthermore, its detailed discussion of update and detection modes informs the design of our online learning strategy for adapting to new user spending patterns in real-time.
  directly_justifies:
    - "Deep learning models are susceptible to performance degradation when concept drift occurs."
    - "Active detection methods can provide decision-makers with knowledge of dynamic concept changes."
    - "Parameter updates, such as adjusting weights, are a common and efficient way to adapt to abrupt concept drift."
    - "LSTM-based methods are suitable for processing and forecasting events with relatively long intervals in time series."
    - "Hybrid learning models that combine LSTM and CNN are effective for capturing spatial and temporal features in data."
  limits:
    - "The review does not provide an empirical comparison of the performance of different concept drift adaptation methods."
    - "The effectiveness of many algorithms is demonstrated on specific datasets, and their generalizability to diverse financial data is not fully explored. [unacknowledged]"
    - "The review focuses on deep learning methods and does not compare them against traditional machine learning approaches for concept drift."
    - "Specific guidance on implementing these complex deep learning models in a mobile-first application like Odin is not provided. [unacknowledged]"
    - "The review does not address the unique challenges of applying these algorithms to noisy, sparse, or class-imbalanced personal financial data, which is a common reality in PFMS. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed for this paper. Domains flagged as relevant were: Predictive Modeling, Anomaly Detection, and System Evaluation. For the Predictive Modeling domain (6.A, 6.B), relevance was high, as the paper is a review of deep learning forecasting algorithms (RNNs, LSTMs) which are directly applicable to spending prediction. For Anomaly Detection (8.A, 8.B), relevance was high, given the paper's specific coverage of anomaly detection methods (I-LSTM, ARCUS, MemStream) that adapt to concept drift. For System Evaluation (12.A), relevance was medium because it summarizes metrics and datasets that can be used for testing. The topic 'Limitations and Gaps in Existing Systems' (4.B) was assigned high relevance as the paper explicitly frames the problem of model degradation as a key limitation. 'Profile Dynamics' (5.B) was considered a medium relevance case because the concept of recurring drift relates to the challenge of maintaining accurate user profiles over time. Domains rejected included those focused on Filipino cultural context (2.A, 2.B, 2.C, 2.D), Expense Categorization (3.A, 3.B, 3.C), Budget Recommendation (7.A, 7.B, 7.C, 7.D), Mobile-First Design (9.A, 9.B), User Retention (11.A, 11.B), and Savings & Debt Management (13.A, 13.B, 13.C), as the paper does not provide direct, citeable claims for these specific areas. The concept of 'cold-start' (5.B) was considered but rejected as the paper's discussion of recurring drift is a related but separate challenge. Overall, the paper provides a strong, high-level justification for incorporating advanced deep learning techniques into Odin's predictive and anomaly detection modules to ensure their robustness over time."
limitations:
  - "The review lacks an empirical comparison of the discussed algorithms, making it difficult to select the most effective method for a specific task."
  - "The surveyed methods are not evaluated on personal finance data, limiting the direct transferability of the findings to Odin's context. [unacknowledged]"
  - "The computational cost and resource requirements of many deep learning methods, especially hybrid models, are a significant limitation for mobile deployment. [unacknowledged]"
  - "The review does not address the challenge of dealing with sparse or missing data, which is common in real-world financial datasets. [unacknowledged]"
  - "Some algorithms discussed (e.g., DCA-DNN) suffer from model update latency, which could be critical for real-time applications like fraud detection."
remember_this:
  - "Concept drift causes deep learning models to produce poor predictions as data distributions change."
  - "Active detection methods can identify and explain concept drift, aiding in better decision-making."
  - "LSTM-based methods are crucial for forecasting sequential spending data in personal finance."
  - "Num: The review finds that abrupt drift is the most frequently addressed type in the literature."
  - "Autoencoders and GANs are powerful generative models for unsupervised anomaly detection in dynamic data streams."
```