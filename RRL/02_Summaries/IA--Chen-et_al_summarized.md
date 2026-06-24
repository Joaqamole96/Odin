```yaml
paper_id: 10.56557/jobari/2024/v30i69014
designation: international
title: A Survey of Time Series Data Forecasting Methods Based on Deep Learning
authors: Chen, J.; Chen, T.; Wang, Y.; Wang, L.
year: 2024
venue: Journal of Basic and Applied Research International
odin_topics:
  - 3.A
  - 4.A
  - 6.A
  - 6.B
  - 7.A
  - 8.A
  - 8.B
  - 12.A
tldr: A survey comparing RNN, LSTM, GRU, and Transformer models for time series forecasting, with experimental evaluation on public datasets.
problem_and_motivation: Traditional machine learning methods struggle with massive time series datasets due to temporal dependence and seasonality. Deep learning offers an alternative with minimal manual feature engineering.
approach:
  - Reviews common features, datasets, and evaluation metrics for time series forecasting.
  - Surveys deep learning models including RNN, LSTM, GRU, Bi-LSTM, and Transformer.
  - Conducts univariate prediction experiments on ETTm2, Electricity, Weather, and Traffic datasets.
  - Uses input sequence length of 24 and prediction length of 1 with MSE and MAE as metrics.
  - Compares performance of RNN, LSTM, GRU, Transformer, and LSTM-RNN models.
findings:
  - num: Transformer achieved the best performance on ETTm2 with MSE 3.418 and MAE 1.399.
  - num: LSTM achieved minimum MAE on Electricity (1.848) and Traffic (0.020) datasets.
  - num: GRU achieved minimum MSE on Electricity (19.524) and Traffic (0.00110) datasets.
  - num: RNN achieved best performance on Weather with MSE 0.007 and MAE 0.060.
  - The LSTM-RNN hybrid generally outperforms standard RNN and LSTM in some cases.
  - Deep learning models accurately identify complex patterns with lower human resource requirements.
key_figures_tables:
  - Table 1: Comparison of MSE and MAE for five models across four datasets → Transformer best on ETTm2, GRU best on Electricity/Traffic MSE.
  - Figure 10: Prediction curves on ETTm2 dataset → Transformer shows closest fit to actual values.
  - Figure 11: Prediction curves on ECL dataset → GRU and Transformer capture patterns effectively.
  - Figure 12: Prediction curves on Weather dataset → RNN performs surprisingly well on meteorological data.
  - Figure 13: Prediction curves on Traffic dataset → GRU demonstrates strong performance on occupancy data.
key_equations:
  - equation: MSE = (1/n) ∑(y_i - ŷ_i)^2
    explanation: Average squared difference between predicted and actual values.
  - equation: MAE = (1/n) ∑|y_i - ŷ_i|
    explanation: Mean absolute difference between predicted and actual values.
  - equation: Attention(Q,K,V) = softmax(QK^T/√d_k)V
    explanation: Self-attention mechanism computes weighted sum of values.
  - equation: PE(t,i) = sin(t/10000^(2k/d)) for i=2k
    explanation: Positional encoding using sine functions for even dimensions.
definitions:
  - term: TSF
    definition: Time Series Forecasting, predicting future values from historical patterns.
  - term: RNN
    definition: Recurrent Neural Network, processes sequential data with hidden states.
  - term: LSTM
    definition: Long Short-Term Memory, RNN variant with gating mechanisms for long dependencies.
  - term: GRU
    definition: Gated Recurrent Unit, simplified LSTM with update and reset gates.
  - term: MSE
    definition: Mean Squared Error, evaluation metric measuring average squared error.
  - term: MAE
    definition: Mean Absolute Error, evaluation metric measuring average absolute error.
  - term: ETT
    definition: Electricity Transformer Temperature, dataset of transformer oil temperatures.
critical_citations:
  - "[Vaswani et al., 2017] — Introduced Transformer with self-attention mechanism."
  - "[Hochreiter & Schmidhuber, 1997] — Proposed LSTM for long-term dependencies."
  - "[Wu et al., 2021] — Introduced Autoformer with decomposition architecture."
  - "[Liu et al., 2022] — Proposed non-stationary Transformers for time series."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Survey discusses feature extraction relevant to categorization.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Provides context on deep learning models applicable to PFMS.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly surveys forecasting models applicable to spending prediction.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Compares RNN, LSTM, GRU, and Transformer for sequential forecasting.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Forecasting accuracy underpins budget recommendation systems.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Forecasting models are foundational for anomaly detection baselines.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Compares algorithms applicable to anomaly detection in spending.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides evaluation metrics (MSE, MAE) directly applicable to PFMS modules.
  contribution: This survey establishes a comparative benchmark of deep learning forecasting models, which directly informs Odin's spending forecasting module. The evaluation framework using MSE and MAE provides a template for assessing Odin's predictive accuracy. The discussion of model strengths and weaknesses guides architecture selection for Odin's forecasting engine. The Transformer and LSTM performance comparisons offer empirical evidence for algorithm selection. The survey's experimental methodology can be adapted for evaluating Odin's forecasting and anomaly detection components.
  directly_justifies:
    - "Transformers achieve superior performance on the ETTm2 dataset for univariate forecasting."
    - "LSTM and GRU models are effective for electricity and traffic prediction tasks."
    - "MSE and MAE are standard evaluation metrics for time series forecasting models."
    - "RNN variants are foundational for capturing temporal dependencies in sequential data."
  limits:
    - "The survey focuses on univariate prediction only, not multivariate spending patterns."
    - "Experiments use short prediction horizons (length 1), not long-term forecasting."
    - "No comparison on financial transaction datasets specific to personal finance."
    - "Limited discussion of computational efficiency or deployment constraints."
  mapping_rationale: All 12 functional domains and associated topic codes were systematically scanned. The paper's primary relevance is to 6.A and 6.B (predictive modeling and forecasting algorithms) at high relevance, as it directly surveys and compares deep learning models for time series forecasting. Topic 12.A (evaluation frameworks) is also high relevance due to detailed discussion of MSE and MAE metrics. Topics 3.A, 4.A, 7.A, 8.A, and 8.B are medium relevance as the forecasting methods and metrics are foundational to categorization, system landscape, budgeting, and anomaly detection but are not directly addressed. Topics related to Filipino cultural context, behavioral profiling, mobile design, privacy, retention, and debt management were considered and rejected as the paper contains no relevant content. The overall relevance is high for Odin's algorithmic forecasting modules.
limitations:
  - "Prediction experiments limited to univariate time series only."
  - "No evaluation on financial transaction data."
  - "Short prediction horizon may not generalize to monthly budget cycles."
  - "Does not address real-time forecasting constraints or model interpretability."
remember_this:
  - "Transformer achieved MAE of 1.399 on ETTm2, best among compared models."
  - "GRU achieved minimum MSE of 19.524 on Electricity and 0.00110 on Traffic."
  - "LSTM-RNN hybrid generally improves over standalone RNN models."
  - "MSE and MAE are the standard evaluation metrics for forecasting."
  - "Deep learning models capture complex patterns with minimal manual feature engineering."
```