```yaml
paper_id: 10.3390/ijfs11030094
designation: international-algorithm-specific
title: Forecasting Stock Market Prices Using Machine Learning and Deep Learning Models: A Systematic Review, Performance Analysis and Discussion of Implications
authors: Sonkavde, G.; Dharrao, D. S.; Bongale, A. M.; Deokate, S. T.; Doreswamy, D.; Bhat, S. K.
year: 2023
venue: International Journal of Financial Studies
odin_topics:
  - 6.A
  - 6.B
  - 7.B
  - 12.B
  - 12.C
tldr: A systematic review and comparative analysis of machine learning and deep learning models for stock price forecasting, including an ensemble model that achieves superior performance.
problem_and_motivation: Accurately forecasting stock prices remains challenging due to market volatility and limitations of traditional analysis. While many ML/DL models have been proposed, there is a need for a structured summary and practical comparative analysis of their performance.
approach:
  - This review systematically examines supervised, unsupervised, ensemble, time series, and deep learning algorithms for stock price prediction.
  - A generic machine learning pipeline for stock price prediction and classification is described, covering data collection, pre-processing, and evaluation.
  - An ensemble model combining Random Forest, XG-Boost, and LSTM is implemented and tested on TAINIWALCHM and AGROPHOS stock data.
  - Performance is evaluated using RMSE and R² scores, comparing the ensemble against standalone models like SVR, MLPR, KNN, and LSTM.
  - Hyperparameter tuning via grid search is employed to optimize the ensemble model's configuration.
findings:
  - num: The ensemble model (Random Forest + XG-Boost + LSTM) achieved the lowest RMSE (2.0247 for TANIWALCHM, 1.2658 for AGROPHOS) and highest R² scores (0.9921 and 0.9897, respectively).
  - XG-Boost outperformed ARIMA and LSTM in a prior study, with an MSE of 360.0 for a specific dataset.
  - The review identified hyperparameter tuning as a crucial step for maximizing model performance in stock forecasting.
  - Ensemble techniques generally provide superior performance over standalone models for stock price prediction.
  - The study found that sentiment analysis, when combined with price data, can improve prediction accuracy.
key_figures_tables:
  - Table 1: Ensemble model parameter configuration → Details the settings for Random Forest, XG-Boost, and LSTM in the implemented model.
  - Figure 7: TANIWALCHM stock price forecasting → Visual comparison shows ensemble model fits actual prices most closely.
  - Figure 8: AGROPHOS stock price forecasting → Ensemble model demonstrates superior fit over individual algorithms.
  - Table 2: RMSE and R² scores of algorithms → Ensemble achieves best performance with RMSE 2.0247 (TANIWALCHM) and 1.2658 (AGROPHOS).
key_equations:
  - equation: O = S_x + K
    explanation: Linear regression equation for stock price prediction.
  - equation: D(h_i, p_r) = sqrt(Σ_{l=1}^{n} (P_r - h_i)^2)
    explanation: Euclidean distance calculation for KNN.
  - equation: y'_t = k + β_p * ωD y'_{t-1} + ... + θ_q * ε_{t-q} + ε_t
    explanation: ARIMA model formula combining AR and MA components.
  - equation: Y_t = l(t) + sp(t) + v(t) + ε_t
    explanation: FBProphet model combining trend, seasonality, and holiday effects.
definitions:
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network variant with gating mechanisms.
  - term: GRU
    definition: Gated Recurrent Unit, a simpler RNN variant with two gates.
  - term: XG-Boost
    definition: Extreme Gradient Boosting, an optimized distributed gradient boosting library.
  - term: ARIMA
    definition: Autoregressive Integrated Moving Average, a classical time series forecasting model.
  - term: RMSE
    definition: Root Mean Square Error, a metric for regression model performance.
critical_citations:
  - "[Zhu and He, 2022] — Compared XG-Boost, ARIMA, and LSTM, finding XG-Boost superior."
  - "[Li and Pan, 2021] — Presented a blending ensemble of LSTM and GRU for stock prediction."
  - "[Xu et al., 2020] — Proposed E-SVR-RF ensemble algorithm for financial stock forecasting."
  - "[Di Persio and Honchar, 2017] — Demonstrated RNN, LSTM, and GRU for Google stock forecasting."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Reviews forecasting models applicable to spending prediction in PFMS.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Compares LSTM, GRU, ARIMA, and ensemble methods for sequential data.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: The forecasting techniques could be adapted for budget recommendation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Discusses RMSE and R2 for evaluating forecasting algorithms.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: low
      justification: Evaluation metrics (RMSE, R2) are transferable to budget systems.
  contribution: This paper provides a comprehensive systematic review of machine learning and deep learning models for financial forecasting, which informs the selection of predictive algorithms for Odin's spending forecasting module. It demonstrates the effectiveness of ensemble methods (Random Forest + XG-Boost + LSTM) in improving forecast accuracy, which could enhance Odin's budget recommendation and anomaly detection capabilities. The comparative analysis of evaluation metrics (RMSE, R²) establishes a benchmark for assessing Odin's algorithmic modules.
  directly_justifies:
    - "Ensemble models combining Random Forest, XG-Boost, and LSTM achieve superior forecast accuracy."
    - "Hyperparameter tuning is critical for maximizing model performance in forecasting."
    - "LSTM and GRU can capture long-term dependencies in sequential financial data."
  limits:
    - "The experimental validation is limited to two Indian stock datasets, which may not generalize."
    - "The study does not address cold-start scenarios, which are relevant to Odin's anomaly detection."
    - "Privacy and user trust implications of using ML models in finance are not discussed."
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The paper was flagged as highly relevant to the "Spending Forecasting" domain (6.A, 6.B) due to its extensive review of forecasting algorithms like LSTM, GRU, and ARIMA, as well as ensemble techniques. It was deemed relevant to "System Evaluation" (12.B, 12.C) because of its detailed discussion of evaluation metrics (RMSE, R2). A low relevance was assigned to "Budget Recommendation" (7.B) and "Anomaly Detection" (8.B) because the paper focuses on stock price prediction, not personal budget allocation or anomaly detection. The paper was rejected for all other domains (e.g., Filipino Cultural Context, Behavioral Profiling, Mobile-First Design, Data Privacy) as it does not address these areas. Overall, the paper's primary contribution to Odin lies in its methodological review of algorithms and evaluation approaches for time-series forecasting.
limitations:
  - "The study focuses only on stock market data, which may not fully represent personal spending patterns."
  - "The implemented ensemble model's performance was not compared against more recent transformer-based models."
  - "The impact of data privacy and security on model performance was not investigated [unacknowledged]."
  - "The review does not address the deployment and computational constraints of mobile-first applications [unacknowledged]."
remember_this:
  - "An ensemble of Random Forest, XG-Boost, and LSTM achieved the highest R² score of 0.9921."
  - "Hyperparameter tuning significantly enhances the performance of forecasting models."
  - "Ensemble learning techniques generally outperform individual machine learning models."
  - "LSTM and GRU are suitable for capturing long-term dependencies in sequential data."
```