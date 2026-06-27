```yaml
paper_id: 10.1109/ACCESS.2023.3317791
designation: international-algorithm-specific
title: Anomaly Detection in Multi-Seasonal Time Series Data
authors: Williams, A. T.; Sperl, R. E.; Chung, S. M.
year: 2023
venue: IEEE Access
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 2.B
tldr: Extends SARIMA to model multiple seasonal patterns, improving anomaly detection accuracy in time series data with two seasonalities.
problem_and_motivation: Most forecasting models for anomaly detection incorporate only one seasonal component, failing to capture multiple known seasonal patterns common in real-world data. This limitation reduces anomaly detection accuracy in datasets with multiple seasonalities, such as daily and weekly cycles.
approach:
  - Proposes multi-SARIMA, a model that extends SARIMA to incorporate two seasonal periods using a derived equation combining two SARIMA models.
  - Evaluates on three datasets containing two meaningful seasonal trends: NYC Taxi, a synthetic dataset, and a smaller version of Numenta's HotGym.
  - Compares multi-SARIMA against MA, SIMA, SARIMA, HTM, and TBATS in single-step and two-step (with MA/SIMA as first step) anomaly detection settings.
  - Uses a dynamic anomaly score threshold based on Mean Absolute Deviation (MAD) to label data points.
  - Validates seasonal components in datasets using Multiple Seasonal-Trend decomposition using Loess (MSTL).
findings:
  - num: Multi-SARIMA achieved the highest true positives for every dataset while maintaining fewer false positives than SARIMA.
  - num: Multi-SARIMA doubled the true positive rate of HTM and TBATS for the HotGym dataset.
  - num: Multi-SARIMA had the highest runtime among models due to training on two seasonal periods.
  - num: Two-step approach with MA + multi-SARIMA significantly reduced false positives compared to standalone multi-SARIMA for all datasets.
  - num: TBATS outperformed SARIMA and HTM but was outperformed by multi-SARIMA in two of three datasets.
key_figures_tables:
  - "Table 1: Overview of datasets → Shows datasets with two meaningful seasonal trends and hand-labeled anomalies."
  - "Figure 1: MSTL decomposition of NYC Taxi dataset → Confirms daily and weekly seasonal patterns in taxi traffic."
  - "Figure 2: MSTL decomposition of Synthetic dataset → Confirms daily and weekly seasonal patterns simulating a work schedule."
  - "Figure 3: MSTL decomposition of HotGym dataset → Confirms daily and weekly patterns in gym energy consumption."
  - "Table 2: Single-step experimental results → Multi-SARIMA has highest true positives and competitive false positives across datasets."
  - "Table 3: Two-step experimental results → Multi-SARIMA as second step reduces false positives while maintaining true positives."
key_equations:
  - equation: |
      X_t = ∇_{m_2}^{d_2} X_t + \sum_{i=0}^{d_2-1} B^{m_2} \nabla_{m_2}^{i} X_t
    explanation: "Reconstructs original time series from the differenced series."
  - equation: |
      \nabla_{m_2}^{d_2} X_t = (\sum_{i=1}^{p_1} a_{1,i} B^{m_1 i}) \nabla_{m_2}^{d_2} X_t + (\sum_{i=1}^{p_2} a_{2,i} B^{m_2 i}) \nabla_{m_2}^{d_2} X_t - (\sum_{j=1}^{p_2} \sum_{i=1}^{p_1} a_{1,i} a_{2,j} B^{m_1 i + m_2 j}) \nabla_{m_2}^{d_2} X_t + \epsilon_t
    explanation: "Multi-SARIMA equation combining two seasonal AR and MA components."
definitions:
  - term: Multi-SARIMA
    definition: Extension of SARIMA that incorporates two seasonal components to improve anomaly detection.
  - term: TBATS
    definition: Trigonometric seasonality, Box-Cox transformation, ARMA errors, Trend, and Seasonal components model for multi-seasonal forecasting.
  - term: MAD (Mean Absolute Deviation)
    definition: A robust metric for calculating dynamic anomaly threshold, insensitive to outliers.
  - term: MSTL (Multiple Seasonal-Trend decomposition using Loess)
    definition: Decomposition method for time series with multiple seasonal patterns.
  - term: SDR (Sparse Distributed Representations)
    definition: Vectors with thousands of bits representing semantic properties, used in HTM.
critical_citations:
  - "[Bandara et al., 2021] — Source for MSTL decomposition algorithm."
  - "[De Livera et al., 2011] — Source for TBATS forecasting model."
  - "[Sperl and Chung, 2019] — Proposed the two-step anomaly detection approach."
  - "[Hyndman and Athanasopoulos, 2021] — Standard reference for SARIMA models."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: "Directly addresses forecasting models for sequential spending data."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: "Proposes multi-SARIMA, a novel forecasting algorithm for multi-seasonal data."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: "Core focus is anomaly detection in time series data with multiple seasonalities."
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: "Evaluates and compares multiple anomaly detection algorithms including the proposed multi-SARIMA."
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: "The paper focuses on multi-seasonal patterns, applicable to cyclical spending in personal finance."
  contribution: "The multi-SARIMA model provides a mathematical framework for Odin's anomaly detection module to handle user spending data with multiple seasonal cycles (e.g., daily and weekly). The two-step approach with multi-SARIMA offers a strategy to optimize Odin's prediction engine for accuracy and runtime, balancing performance and resource constraints for mobile users. The experimental methodology demonstrates how to validate seasonal components and evaluate forecasting models, guiding Odin's model selection and tuning. The paper's findings on TBATS and SARIMA inform the choice of baseline algorithms for comparison in Odin's system evaluation."
  directly_justifies:
    - "Multi-seasonal forecasting improves anomaly detection accuracy in time series data."
    - "Two-step anomaly detection can reduce false positives while maintaining true positive rates."
    - "SARIMA can be extended to incorporate multiple seasonal patterns using the derived multi-SARIMA equation."
  limits:
    - "Increased processing time for multi-SARIMA due to training on two seasonal periods."
    - "Multi-SARIMA is designed for two seasonal periods; performance with more than two is not evaluated."
    - "The two-step approach is limited by the true positive rate of the first-step model. [unacknowledged]"
  mapping_rationale: "All 12 functional domains and their associated topic codes were systematically scanned. The paper was flagged as highly relevant to the 'Spending Forecasting' and 'Anomaly Detection' domains, specifically topics 6.A, 6.B, 8.A, and 8.B, due to its core contribution of a novel multi-seasonal forecasting model for anomaly detection. Topic 2.B (Seasonal and Cyclical Spending Patterns) was marked as medium relevance because the paper's focus on multiple seasonalities provides a contextual basis for understanding spending cycles, but it does not directly address Filipino cultural practices. The 'Budget Recommendation' domain (topics 7.A-7.D) was considered but rejected because the paper does not involve budget allocation or optimization. The 'Mobile-First Design' and 'Data Privacy' domains were rejected as they are not addressed. The overall relevance is high because the paper provides a directly applicable algorithmic approach for detecting anomalies in multi-seasonal spending data, a key requirement for Odin's core functionality."
limitations:
  - "Multi-SARIMA has higher runtime compared to single-season models."
  - "The model assumes pre-determined seasonal periods, which may not be known a priori for all datasets."
  - "Performance is not guaranteed if seasonal patterns are insignificant or datasets have more than two seasonalities."
  - "Experimental evaluation limited to three datasets, two of which are from the Numenta Anomaly Benchmark. [unacknowledged]"
  - "Comparison with deep learning methods like TCN is noted as future work, leaving a gap in benchmarking against state-of-the-art neural approaches. [unacknowledged]"
remember_this:
  - "Multi-SARIMA extends SARIMA to model two seasonal patterns for better anomaly detection."
  - "It achieved the highest true positives while maintaining fewer false positives than SARIMA."
  - "The two-step approach with multi-SARIMA significantly reduces false positives."
  - "Multi-SARIMA doubled the true positive rate of HTM and TBATS on the HotGym dataset."
  - "Increased accuracy comes with higher runtime due to training on two seasonal periods."
```