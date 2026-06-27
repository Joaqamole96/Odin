```yaml
paper_id: 10.1109/ACCESS.2024.3440631
designation: international-algorithm-specific
title: Short-Term Load Forecasting: A Comprehensive Review and Simulation Study With CNN-LSTM Hybrids Approach
authors: Ullah, K.; Ahsan, M.; Hasanat, S. M.; Haris, M.; Yousaf, H.; Raza, S. F.; Tandon, R.; Abid, S.; Ullah, Z.
year: 2024
venue: IEEE Access
odin_topics:
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 12.A
  - 12.B
tldr: A comprehensive review of STLF methods is combined with a proposed CNN-LSTM hybrid model that demonstrates superior accuracy on datasets from Pakistan and the US.
problem_and_motivation: Accurate short-term load forecasting is critical for power grid stability and economical operation, yet existing methods face challenges with non-linearities and non-stationary data. A need exists for more robust and accurate forecasting models.
approach:
  - A comprehensive review categorizes STLF methods into statistical, intelligent, and hybrid models, analyzing their mathematical foundations and trade-offs.
  - The proposed model integrates 1D convolutional layers for feature extraction with LSTM layers for capturing temporal dependencies in sequential load data.
  - Input data comprises 24 time steps and 17 features, including historical load, hour, month, weekday, and holiday indicators.
  - Preprocessing includes outlier detection and handling using the IQR method, and feature extraction from NTDC Pakistan's national grid data.
  - The model is evaluated against baselines [55] and [79] using RMSE, MAE, and MAPE for both single-step and 24-hour forecasting horizons.
findings:
  - num: For single-step forecasting on the NTDC dataset, the proposed model achieved an RMSE of 538.71, MAE of 371.97, and MAPE of 2.72.
  - num: For 24-hour forecasting on the NTDC dataset, the proposed model achieved an RMSE of 951.94, MAE of 656.35, and MAPE of 4.72.
  - num: On the AEP dataset, the proposed model outperformed benchmarks with an RMSE of 126.35 for single-step forecasting.
  - The proposed CNN-LSTM hybrid consistently outperformed benchmark models from [55] and [79] across all metrics and forecast horizons.
  - The hybrid model effectively captures both spatial features and long-term temporal dependencies in load data, enhancing prediction accuracy.
key_figures_tables:
  - Figure 18: Actual vs predicted load consumption → Predicted load closely mirrors actual load trends.
  - Figure 19: Comparison with reference model → Proposed model predictions are closer to actual values than reference method.
  - Table 8: Performance evaluation for single-step → Proposed model achieves lowest RMSE, MAE, and MAPE compared to benchmarks.
  - Table 9: Performance evaluation for 24 hours → Proposed model achieves lowest RMSE, MAE, and MAPE compared to benchmarks.
  - Figure 14: Outliers before and after handling → IQR-based method effectively identifies and rectifies outliers in load data.
key_equations:
  - equation: Lower Outliers = Q1 - 1.5 * IQR
    explanation: Identifies low outliers for data cleaning.
  - equation: Upper Outliers = Q3 + 1.5 * IQR
    explanation: Identifies high outliers for data cleaning.
definitions:
  - term: STLF
    definition: Short-Term Load Forecasting, predicting electrical load from an hour to a week ahead.
  - term: CNN
    definition: Convolutional Neural Network, used for feature extraction.
  - term: LSTM
    definition: Long Short-Term Memory network, used for sequence prediction and capturing temporal dependencies.
  - term: NTDC
    definition: National Transmission and Dispatch Company of Pakistan, source of the dataset.
  - term: AEP
    definition: American Electric Power, source of a comparison dataset.
  - term: RMSE
    definition: Root Mean Square Error, a measure of forecast accuracy.
  - term: MAE
    definition: Mean Absolute Error, a measure of forecast accuracy.
  - term: MAPE
    definition: Mean Absolute Percentage Error, a measure of forecast accuracy.
critical_citations:
  - "[55, 2021] — Benchmark CNN-LSTM model for comparison."
  - "[79, 2020] — Benchmark hybrid CNN-LSTM model for comparison."
  - "[31, 2023] — Comparison of ARIMA and ANN for STLF."
  - "[48, 2022] — Comprehensive study of random forest for STLF."
  - "[62, 2023] — Review of STLF models challenges and progress."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly addresses predictive modeling via a CNN-LSTM hybrid for time-series forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Proposes and evaluates specific algorithms (CNN, LSTM, hybrid) for sequential load data, analogous to spending data.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Forecasting load demand informs resource allocation, akin to budgeting strategies.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Accurate forecasting is a prerequisite for effective budget recommendation based on predicted future states.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: The paper discusses outlier detection and handling in load data, a technique relevant for anomaly detection systems.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: The paper utilizes a standard evaluation framework (RMSE, MAE, MAPE) applicable to evaluating forecasting modules in PFMS.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: The core contribution is a comparative evaluation of algorithmic modules (CNN, LSTM, hybrid) for load forecasting.
  contribution: The paper provides a comprehensive review of STLF methods that can guide the selection of appropriate algorithms for Odin's forecasting modules. It proposes and validates a CNN-LSTM hybrid model that could be adapted for forecasting user spending patterns. The rigorous evaluation framework and performance metrics (RMSE, MAE, MAPE) are directly applicable for assessing Odin's predictive algorithms. The approach to feature engineering, including temporal and cyclical features, offers a blueprint for modeling financial data.
  directly_justifies:
    - "num: For single-step forecasting, the model yielded an RMSE of 538.71, MAE of 371.97, and MAPE of 2.72."
    - "The proposed model has outperformed previous models in comparison using the AEP dataset."
    - "Hybrid models that employ different forecasting approaches can improve accuracy."
  limits:
    - "The dataset used is from the power sector and may not directly reflect individual financial spending patterns."
    - "The study does not address the cold-start problem in forecasting, a key challenge for user-specific PFMS."
    - "The model's performance on irregular or sparse data, typical of personal spending, is not evaluated. [unacknowledged]"
    - "The paper does not address data privacy concerns related to the use of personal consumption data. [unacknowledged]"
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant for the 'Spending Forecasting' domain (6.A, 6.B) due to its core focus on predictive modeling for sequential time-series data, and for 'System Evaluation' (12.B) due to its comparative algorithmic evaluation. It shows medium relevance for 'Budget Recommendation' (7.B) as forecasting informs resource allocation, and for 'Evaluation Frameworks' (12.A). It has contextual relevance for 'Anomaly Detection' (8.A) due to its discussion of outlier handling. Domains like 'Filipino Cultural Context', 'User Retention', and 'Data Privacy' were considered and rejected as the paper provides no direct citeable claims for these areas. The paper's overall relevance to Odin is strong for the forecasting and evaluation components, providing validated algorithms and methodologies.
limitations:
  - "The study focuses on power systems, limiting the direct generalizability of findings to personal finance applications. [unacknowledged]"
  - "The hybrid CNN-LSTM model's complexity and computational cost are not fully explored. [unacknowledged]"
  - "The paper does not address the challenge of forecasting for sparse or irregular transaction data common in PFMS. [unacknowledged]"
  - "The potential for model overfitting, a common issue with complex deep learning models, is not thoroughly addressed."
remember_this:
  - CNN-LSTM hybrid achieved a MAPE of 2.72 for single-step forecasting on NTDC data.
  - Hybrid models integrating CNNs and LSTMs are highly effective for sequential data prediction.
  - Feature engineering with temporal and cyclical variables is crucial for forecasting accuracy.
  - The model consistently outperformed benchmarks across single-step and multi-step horizons.
  - Accurate forecasting is essential for effective resource management and balancing.
```