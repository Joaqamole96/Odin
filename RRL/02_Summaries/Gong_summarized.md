```yaml
paper_id: 10.1051/itmconf/20268402004
designation: international
title: Research Progress and Trends of Deep Learning in Stock Price Prediction: A Systematic Review from LSTM to Transformer
authors: Gong, H.
year: 2026
venue: ITM Web of Conferences
odin_topics:
  - 6.A
  - 6.B
  - 8.B
  - 12.B
tldr: A systematic review of deep learning models for stock price prediction, tracing the evolution from LSTM and CNN-LSTM to Transformer and hybrid architectures, summarizing model principles, empirical comparisons, challenges, and future directions.
problem_and_motivation: Stock price prediction is crucial for quantitative finance but is highly challenging due to market volatility, non-linearity, and non-stationarity. Traditional and early machine learning methods fail to capture complex patterns, creating a need for more robust models. This review aims to systematically summarize the advancement from LSTM to Transformer architectures to guide researchers.
approach:
  - The paper conducts a systematic literature review of deep learning models for stock price prediction.
  - It covers RNN variants (LSTM, GRU), CNN, Transformer models, and hybrid architectures like CNN-LSTM and LSTM-Transformer.
  - The review analyzes model principles, advantages, disadvantages, and application scenarios.
  - It includes a comparative analysis of empirical studies, focusing on datasets, evaluation metrics (RMSE, MAE, MAPE, DA, R², Sharpe Ratio), and performance.
  - The paper identifies current challenges at the data, model, and deployment levels and discusses future research trends.
findings:
  - num: LSTM achieved a Sharpe ratio of 2.34 for S&P 500 constituents from 1992 to 2015, outperforming DNN and logistic regression.
  - num: Transformer models showed improved accuracy over CNN, RNN, and LSTM, with average MAE decreasing by approximately 20.73%, MSE by 34.84%, and MAPE by 25.63%.
  - num: The LSTM-Transformer hybrid model reduced MAE and RMSE by over 50% compared to parent models and achieved an R² of 0.9618, higher than LSTM (0.8430) and Transformer (0.7763).
  - Stock prediction models have evolved from single models (LSTM) to hybrid and multimodal fusion architectures.
  - Challenges include data noise, overfitting, model interpretability, computational efficiency, and deployment in dynamic markets.
  - Future directions include multimodal information fusion, interpretable AI, real-time adaptive learning, and automated model architecture search.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: LSTM
    definition: Long Short-Term Memory, an RNN variant using gating mechanisms to handle long-term dependencies.
  - term: GRU
    definition: Gated Recurrent Unit, a simpler RNN variant with similar performance to LSTM but higher computational efficiency.
  - term: CNN
    definition: Convolutional Neural Network, a model that uses local receptive fields and hierarchical feature extraction, applied to time series for trend extraction.
  - term: Transformer
    definition: A model architecture using a self-attention mechanism to capture long-range dependencies and enable parallel computing.
  - term: RMSE
    definition: Root Mean Squared Error, a metric reflecting the overall deviation between predicted and actual values, sensitive to large errors.
  - term: MAE
    definition: Mean Absolute Error, a metric showing the average absolute deviation, reflecting prediction stability.
  - term: MAPE
    definition: Mean Absolute Percentage Error, the average percentage error between predicted and actual values.
  - term: DA
    definition: Directional Accuracy, a metric reflecting the accuracy of predicting the direction of stock price changes.
  - term: Sharpe Ratio
    definition: A metric reflecting the relationship between returns and risks, with higher values indicating better risk-adjusted returns.
critical_citations:
  - "[Fischer & Krauss, 2018] — Benchmarking LSTM in financial market predictions."
  - "[Mehtab & Sen, 2021] — Proposing a CNN-LSTM hybrid for stock prediction."
  - "[Wang et al., 2022] — Demonstrating Transformer's superior prediction accuracy."
  - "[Zhao et al., 2025] — Introducing an LSTM-Transformer hybrid with strong results."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: This paper is a comprehensive review of predictive models relevant to financial forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: The review extensively covers LSTM, Transformer, and hybrid algorithms for sequential time series prediction.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: The paper discusses model sensitivity to noise and anomalies, which is relevant for detecting unusual spending patterns.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: The paper details evaluation metrics (RMSE, MAE, Sharpe Ratio) and compares model performance, relevant for system evaluation.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: The paper mentions "black box" interpretability concerns, which contextualize the importance of user trust.
  contribution: "This review provides a technical roadmap for selecting and evaluating deep learning models for sequential financial data prediction. It directly informs the design of Odin's forecasting and anomaly detection modules by comparing the strengths and weaknesses of LSTM, Transformer, and hybrid models. The systematic comparison of evaluation metrics validates the choice of performance indicators for Odin's algorithmic modules. The discussion of model challenges and future trends, such as multimodal fusion and interpretability, highlights areas for advanced feature engineering in Odin."
  directly_justifies:
    - "LSTM models are reliable benchmarks for medium and short-term prediction tasks."
    - "Transformer models demonstrate superior performance in capturing long-range dependencies."
    - "Hybrid LSTM-Transformer models achieve a balance of higher accuracy and interpretability."
    - "Deep learning models outperform traditional statistical methods in stock price prediction."
  limits:
    - "The review is specific to stock price prediction, which may differ from personal spending data."
    - "The paper primarily focuses on quantitative finance, not personal finance management."
    - "The review does not cover user-specific constraints or behavioral profiling."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to the Spending Forecasting domain (6.A, 6.B) because it reviews state-of-the-art predictive algorithms (LSTM, Transformer) for time series data. It also has medium relevance to Anomaly Detection (8.B) as it discusses model sensitivity to noise and abnormal fluctuations, and to System Evaluation (12.B) due to its detailed comparison of evaluation metrics. Other domains like Expense Categorization (3.A) and Behavioral Profiling (5.A) were considered but rejected as the paper does not address spending categories or user behavior classification. The paper's focus on algorithmic performance in finance, not personal finance, places it as a contextual or low relevance for topics like Mobile-First Design (9.A) and Data Privacy (10.A), where it only tangentially mentions interpretability. Overall, the paper's strongest contribution to Odin is as a reference for forecasting and anomaly detection algorithm selection."
limitations:
  - "The review is specific to stock price prediction and may not generalize directly to personal spending data."
  - "It primarily focuses on model performance and does not address practical system integration or user experience."
  - "The paper does not consider resource constraints of mobile-first applications."
  - "Long-term adaptability and real-time learning challenges are identified but not resolved. [unacknowledged]"
remember_this:
  - "LSTM excels in short-term prediction and generating high Sharpe ratio signals."
  - "Transformer models significantly improve accuracy for long-range dependencies."
  - "Hybrid LSTM-Transformer models offer superior accuracy and stability."
  - "Deep learning models surpass traditional methods in financial time series forecasting."
```