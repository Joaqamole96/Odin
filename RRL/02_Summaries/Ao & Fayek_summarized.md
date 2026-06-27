```yaml
paper_id: 10.3390/s23167167
designation: international
title: Continual Deep Learning for Time Series Modeling
authors: Ao, S.-I.; Fayek, H.
year: 2023
venue: Sensors
odin_topics:
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 9.A
  - 12.A
  - 12.B
tldr: A systematic review of deep learning applications for sensor time series, highlighting the need for preprocessing and continual learning to address non-stationary data and catastrophic forgetting.
problem_and_motivation: Real-world time series data often exhibit non-stationary distributions, causing deep learning models to suffer from catastrophic forgetting. This limits the practical deployment of these models in dynamic environments where data distributions shift over time. A systematic review of techniques to address these challenges is needed to guide the development of more robust systems.
approach:
  - Surveys recent deep learning methods (MLP, RNN, LSTM, CNN, GNN) for sensor time series classification and forecasting.
  - Reviews advanced preprocessing techniques including EMD, wavelet transform, and data augmentation.
  - Examines continual learning strategies (regularization, replay, parameter isolation) to mitigate catastrophic forgetting.
  - Evaluates the performance and applicability of these methods across diverse sensor time series datasets.
  - Discusses limitations of current CL research, including a focus on classification over regression and scalability issues.
findings:
  - "num: LSTM achieved superior forecasting performance with 4.82% MAPE vs. 20.97% for ARIMA on traffic flow data."
  - "num: Attention and DCN models work best with wavelet and FFT preprocessing for wind prediction."
  - "num: MC-SGD reduced forgetting by nearly 29% compared to joint-task training for activity recognition."
  - "num: Bidirectional LSTM achieved 94.75% accuracy for classifying resting vs. working states using EEG data."
  - "num: ConvLSTM outperformed persistence, SVR, and LSTM models for SST prediction."
  - "num: 2D CNN was the most reliable model for structural damage detection from raw time series data."
  - "num: Preprocessing with EMD improved CNN validation accuracy from 94.22% to 99.73% for gesture classification."
key_figures_tables:
  - "Table 1: Summary of DL techniques for sensor time series → Shows a wide variety of models and their applications."
  - "Table 2: Advanced preprocessing for DL applications → Demonstrates that preprocessing can significantly boost performance."
  - "Table 3: Continual learning techniques for time series → Highlights CL as a solution for non-stationary data."
  - "Figure 1: Tree diagram of DL methods for sensor time series → Provides a taxonomy of key DL architectures."
  - "Figure 2: Tree diagram of popular preprocessing methods → Categorizes techniques like EMD and wavelet transform."
  - "Figure 3: Taxonomy of continual learning methods → Groups CL strategies into regularization, replay, and isolation."
key_equations:
  - equation: "E(y_t) = E(y_{t-1}) = μ, Var(y_t) = σ^2 < ∞, Cov(y_t, y_{t-k}) = γ(k)"
    explanation: "Definition of weak stationarity for a time series."
  - equation: "L_i = (1/N_i) Σ_{r=1}^{N_i} L(y_{i,r}, ŷ_{i,r}; θ_i) + (q/( (i-1)N )) Σ_{j=1}^{i-1} Σ_{r=1}^{N_j} L( y_{j,r}, M(x̂_{j,r}; θ_i); θ_i )"
    explanation: "Continual learning objective combining current and previous task losses."
definitions:
  - term: "Continual Learning (CL)"
    definition: "A machine learning paradigm to handle non-stationary data by learning sequentially without forgetting."
  - term: "Catastrophic Forgetting (CF)"
    definition: "The abrupt loss of previously learned knowledge when a neural network is trained on new data."
  - term: "Non-stationary Time Series"
    definition: "A time series whose statistical properties, like mean and variance, change over time."
  - term: "Empirical Mode Decomposition (EMD)"
    definition: "A preprocessing technique that decomposes a signal into intrinsic mode functions (IMFs)."
critical_citations:
  - "[Kirkpatrick et al., 2017] — Introduced Elastic Weight Consolidation (EWC) to overcome catastrophic forgetting."
  - "[Hochreiter & Schmidhuber, 1997] — Developed the LSTM architecture to handle long-term dependencies."
  - "[LeCun et al., 2015] — Provided a foundational overview of deep learning and its capabilities."
  - "[De Lange et al., 2022] — Offered a comprehensive survey on continual learning for classification."
relevance:
  topics:
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Provides a general overview of DL/CL applications but not specific PFMS."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Directly discusses limitations of DL (forgetting, non-stationarity) and gaps in CL research."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "contextual"
      justification: "Focuses on technical modeling rather than financial behavior itself."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "low"
      justification: "CL addresses dynamic data, but not explicitly user profile cold-start."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Reviews many forecasting models (LSTM, CNN, etc.) directly applicable to spending prediction."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Evaluates algorithms (LSTM, GRU, etc.) for time series forecasting tasks."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews DL and CL methods for anomaly detection in time series."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "medium"
      justification: "Discusses specific algorithms like Graph Deviation Networks and VAE for anomaly detection."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "contextual"
      justification: "Mentions resource constraints for embedded/mobile sensing, informing design trade-offs."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides evaluation approaches for DL and CL models, including accuracy and forgetting metrics."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Empirically compares different DL and CL algorithms on various tasks and datasets."
  contribution: "This paper provides a foundational review of deep learning and continual learning techniques for time series modeling. It informs Odin's forecasting module by comparing the performance of various models like LSTM and CNN. The review of continual learning is crucial for Odin's anomaly detection and personalization, as it highlights methods to adapt to changing user behavior. The discussion of preprocessing techniques is relevant for ensuring data quality in Odin's expense categorization pipeline. Finally, the analysis of mobile and embedded sensing constraints can guide Odin's mobile-first design choices."
  directly_justifies:
    - "LSTM networks are a strong choice for sequential spending forecasting due to their superior performance over ARIMA."
    - "Continual learning is necessary to prevent catastrophic forgetting when adapting to a user's evolving financial patterns."
    - "Advanced preprocessing, like wavelet transforms and EMD, can significantly improve the accuracy of DL models on time series data."
    - "Replay-based continual learning methods are effective for mobile/embedded devices, balancing performance and resource use."
    - "Graph neural networks can be used for anomaly detection by modeling relationships between different spending categories."
  limits:
    - "The survey focuses on sensor time series, which may not perfectly replicate the noise and patterns of financial transaction data."
    - "Most reviewed CL methods are evaluated on classification tasks, with less focus on regression problems like spending prediction [unacknowledged]."
    - "The paper does not address the unique challenges of personal finance data, such as user privacy and sparse, irregular transactions [unacknowledged]."
    - "Specific guidance on integrating CL with constraint-based budget optimization is not provided [unacknowledged]."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains most directly relevant were 'Spending Forecasting' (6.A, 6.B) and 'Anomaly Detection' (8.A, 8.B) due to the paper's central focus on time series modeling techniques. 'System Evaluation' (12.A, 12.B) was also relevant as the paper compares different algorithms. 'Behavioral Profiling' (5.A) and 'Existing Systems' (4.A, 4.B) were assessed as medium or contextual because the paper discusses model limitations but not financial behavior or systems specifically. Domains like 'Filipino Cultural Context' (2.A-D), 'Savings & Debt Management' (13.A-C), and 'User Retention' (11.A-B) were considered and rejected as the paper provides no direct claims or evidence for these areas. The overall relevance is high for Odin's technical modules (forecasting, anomaly detection) but contextual for its domain-specific aspects, as the paper is a general methodology review."
limitations:
  - "The survey focuses on sensor time series, which may not perfectly replicate the noise and patterns of financial transaction data."
  - "Most reviewed CL methods are evaluated on classification tasks, with less focus on regression problems like spending prediction. [unacknowledged]"
  - "The paper does not address the unique challenges of personal finance data, such as user privacy and sparse, irregular transactions. [unacknowledged]"
  - "Specific guidance on integrating CL with constraint-based budget optimization is not provided. [unacknowledged]"
remember_this:
  - "Continual learning is essential for adapting to non-stationary time series data."
  - "LSTM and CNN are strong baselines for time series forecasting tasks."
  - "Preprocessing can significantly enhance deep learning model performance, with up to 99.73% accuracy."
  - "Deep learning models without CL suffer from catastrophic forgetting in dynamic environments."
  - "Replay-based CL methods balance performance and resource constraints for mobile deployment."
```