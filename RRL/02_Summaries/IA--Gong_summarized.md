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
  - 8.A
  - 8.B
  - 12.A
  - 12.B
tldr: A systematic review of deep learning models for stock prediction, tracing the evolution from LSTM to Transformer and hybrid architectures, with empirical comparisons and future research directions.
problem_and_motivation: Stock price prediction remains challenging due to high volatility and non-linearity, and traditional methods are insufficient. Deep learning models like LSTM and Transformer have shown promise, but a comprehensive review linking their evolution from LSTM to hybrid architectures is lacking. This review aims to systematically summarize these methods, compare their performance, and identify challenges and future trends.
approach:
  - Systematically reviews the evolution of stock prediction models from RNNs and LSTM to Transformer and hybrid architectures.
  - Classifies and analyzes mainstream deep learning models, detailing their characteristics, advantages, and limitations.
  - Compares empirical studies on different datasets, focusing on evaluation metrics like RMSE, MAE, and Sharpe Ratio.
  - Discusses current challenges in data, model, and deployment, and proposes future research directions.
  - Synthesizes findings from prior research to provide a complete technical roadmap for applying deep learning to stock price prediction.
findings:
  - num: LSTM achieved a 0.46% daily return on S&P 500 constituents, outperforming DNN (0.32%) and logistic regression (0.26%).
  - num: LSTM generated trading signals with a Sharpe ratio up to 2.34, while other models were far less than 1.0.
  - num: Transformer models reduced MAE by 20.73%, MSE by 34.84%, and MAPE by 25.63% compared to LSTM in some studies.
  - num: The LSTM-Transformer hybrid model showed MAE and RMSE reductions of over 50% compared to the parent models.
  - num: The hybrid model achieved an R² value of 0.9618, higher than LSTM (0.8430) and Transformer (0.7763).
  - LSTM is advantageous for short-term prediction and generating trading signals with high Sharpe ratios.
  - Transformer excels in long-range dependency and cross-asset modeling, improving overall prediction accuracy.
  - The evolution of models shows a trend towards hybrid and multimodal fusion for better performance and interpretability.
key_figures_tables:
  - "Table 1: Summary of evaluation criteria (RMSE, MAE, MAPE, DA, R2, Sharpe Ratio) used in empirical studies."
  - "Table 2: Comparison of empirical results for LSTM, Transformer, and hybrid models, showing performance metrics and improvements."
  - "Figure 1: Schematic diagram of the Transformer architecture, highlighting its self-attention mechanism for time series prediction."
  - "Figure 2: Framework of the LSTM-Transformer dual-branch hybrid model for stock price prediction."
  - "Figure 3: Trends in deep learning model evolution for stock prediction, from LSTM to multimodal fusion models."
key_equations:
  - equation: "MAE = \\frac{1}{n} \\sum_{i=1}^{n} |y_i - \\hat{y}_i|"
    explanation: "Average absolute error between predicted and actual values."
  - equation: "RMSE = \\sqrt{\\frac{1}{n} \\sum_{i=1}^{n} (y_i - \\hat{y}_i)^2}"
    explanation: "Square root of average squared errors, sensitive to large deviations."
  - equation: "Sharpe Ratio = \\frac{R_p - R_f}{\\sigma_p}"
    explanation: "Risk-adjusted return, higher values indicate better performance."
definitions:
  - term: "LSTM"
    definition: "Long Short-Term Memory, an RNN variant with gating mechanisms to handle long-term dependencies."
  - term: "Transformer"
    definition: "Model architecture using self-attention mechanisms for processing sequences, avoiding recurrence."
  - term: "MAE"
    definition: "Mean Absolute Error, measures average magnitude of errors."
  - term: "RMSE"
    definition: "Root Mean Square Error, measures error magnitude with a higher penalty for large errors."
  - term: "Sharpe Ratio"
    definition: "Metric for risk-adjusted return, calculated as excess return over risk-free rate per unit of volatility."
critical_citations:
  - "[Fischer & Krauss, 2018] — LSTM outperforms memoryless models in predicting S&P 500 returns."
  - "[Wang et al., 2022] — Transformer model shows significant error reduction compared to LSTM."
  - "[Zhao et al., 2025] — LSTM-Transformer hybrid model achieves superior performance over parent models."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Reviews predictive models applicable to financial forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Systematically evaluates LSTM, Transformer, and hybrid models for time series forecasting.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Discusses challenges like data noise and overfitting relevant to anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: Mentions CNN for feature extraction and noise filtering, relevant to detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Compares models using standard metrics like RMSE, MAE, and Sharpe Ratio.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides empirical comparisons and performance benchmarks for various deep learning modules.
  contribution: "This review provides a comprehensive benchmarking of time series forecasting models, offering a direct evaluation framework for Odin's predictive modules. The empirical comparisons of LSTM and Transformer models, including their hybrid variations, justify the choice of foundational algorithms for spending forecasting. The detailed analysis of model strengths (e.g., LSTM for short-term patterns) and weaknesses (e.g., Transformer's computational cost) informs architectural decisions. The identified challenges, such as overfitting and interpretability, align with Odin's design constraints for a robust and trustworthy system."
  directly_justifies:
    - "LSTM is a reliable benchmark for medium and short-term prediction tasks."
    - "Transformer models provide better prediction accuracy, with lower MAE, MSE, and MAPE."
    - "Hybrid LSTM-Transformer models achieve higher accuracy and stability than parent models."
    - "The choice of evaluation metrics (RMSE, MAE, DA) is critical for assessing prediction models."
    - "Interpretability and computational efficiency are key challenges for deploying deep learning in finance."
  limits:
    - "The review does not propose a new model or application in personal finance."
    - "Findings are based on stock market data and may not directly transfer to spending data."
    - "Lacks specific guidance on handling cold-start problems in personal finance systems."
  mapping_rationale: "A systematic scan across all 12 functional domains and 43 topic codes was conducted. Domains most relevant to this paper are Spending Forecasting (6.A, 6.B) and System Evaluation (12.A, 12.B) due to its focus on predictive modeling and empirical performance comparisons. The paper also provides contextual value for Anomaly Detection (8.A, 8.B) through discussions on data noise. Topics related to Filipino Cultural Context, Expense Categorization, and Behavioral Profiling were considered but rejected as the paper is a general technical review without specific application to personal finance or Filipino users. The relevance is high for forecasting algorithms and evaluation frameworks, medium for predictive modeling, and contextual for anomaly detection. Overall, the paper's strength lies in its comprehensive review of forecasting techniques and evaluation metrics, making it highly relevant for designing and assessing Odin's algorithmic modules."
limitations:
  - "The review focuses on stock price prediction, not personal spending forecasting. [unacknowledged]"
  - "Does not address the cold-start problem or how to profile users with limited data. [unacknowledged]"
  - "Limited discussion on mobile-first design or user trust implications. [unacknowledged]"
  - "The paper is a review and does not introduce a novel algorithm or empirical dataset. [unacknowledged]"
remember_this:
  - "LSTM excels in short-term prediction and generating high Sharpe ratio trading signals."
  - "Transformer models reduce prediction errors by over 20% compared to LSTM."
  - "Hybrid LSTM-Transformer models can reduce MAE and RMSE by more than 50%."
  - "Deep learning models outperform traditional methods in financial time series forecasting."
  - "Interpretability and real-time adaptation remain critical challenges for deployment."
```