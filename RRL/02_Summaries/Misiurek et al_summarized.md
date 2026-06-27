```yaml
paper_id: 10.3390/en18154032
designation: international
title: Review of Methods and Models for Forecasting Electricity Consumption
authors: Misiurek, K.; Olkuski, T.; Zyśk, J.
year: 2025
venue: Energies
odin_topics:
  - 6.A
  - 6.B
  - 8.C
  - 12.A
  - 12.B
tldr: A structured review of electricity load forecasting methods categorizes models by time horizon and evaluates classical statistical, machine learning, and deep learning techniques.
problem_and_motivation: Accurate electricity load forecasting is critical for grid stability and cost reduction, but the increasing complexity from renewable integration and variable consumption patterns challenges existing methods. A systematic comparison across time horizons is needed to guide model selection for different operational and strategic planning contexts.
approach:
  - A comprehensive literature review categorizes forecasting methods into very short-term, short-term, medium-term, and long-term horizons.
  - Classical statistical models (ARIMA/SARIMA, exponential smoothing, linear regression) are contrasted with modern AI techniques (ANN, LSTM, CNN, Transformer).
  - The review synthesizes findings from recent studies and evaluates methods based on input data, forecast horizon, and accuracy metrics (e.g., MAPE, RMSE).
  - A comparative analysis is provided for each time horizon, summarizing the advantages and limitations of each approach in tabular form.
  - The paper concludes with a mapping of forecasting methods to data types and applications.
findings:
  - num: LSTM models show high effectiveness for very short-term forecasting, achieving up to a 10-15% improvement in RMSE over traditional ML models for residential loads.
  - num: Hybrid CNN-LSTM models reduce MSE significantly, achieving values as low as 0.3738, by extracting spatial and temporal features.
  - num: Transformer-based models demonstrate comparable accuracy to RNNs but are up to five times faster in inference, with RMSE near 2.0 for short-term forecasts.
  - num: Hybrid statistical and machine learning models can achieve high accuracy (96.83%) for national-level hourly forecasting over a two-year period.
  - Classical ARIMA models remain competitive for structured seasonal data, often outperforming more complex models in data-scarce environments.
  - The study confirms that no universal forecasting approach exists and that hybrid models combining interpretability with high accuracy are a key research need.
key_figures_tables:
  - Table 1: Summary of very short-term load forecasting methods → Compares IT-1FIS, LSTM, CNN-LSTM, and Transformer models.
  - Table 2: Summary of short-term load forecasting methods → Details ARIMA, ANN, hybrid, and GAM models.
  - Table 3: Summary of medium-term load forecasting methods → Presents ARIMA, ANN, hybrid, and Grey models.
  - Table 4: Summary of long-term load forecasting methods → Reviews regression, ANN, LSTM, and Bayesian models.
  - Table 5: Mapping of forecasting methods to data types and applications → Connects model families to specific operational contexts.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: ARIMA
    definition: AutoRegressive Integrated Moving Average, a classical time-series forecasting model.
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network architecture for sequence prediction.
  - term: CNN
    definition: Convolutional Neural Network, a deep learning model for feature extraction.
  - term: MAPE
    definition: Mean Absolute Percentage Error, a common forecast accuracy metric.
  - term: RMSE
    definition: Root Mean Square Error, a common forecast accuracy metric.
critical_citations:
  - "[Azeem et al., 2021] — Provides categorization of electrical load forecasting."
  - "[Klyuev et al., 2022] — Reviews methods for forecasting electric energy consumption."
  - "[Singh et al., 2019] — Quantifies economic impact of forecasting error."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: contextual
      justification: Provides foundational concepts of predictive modeling but focused on electricity, not PFMS.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: contextual
      justification: Reviews algorithms (LSTM, Transformer) applicable to time-series forecasting for general sequential data.
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: low
      justification: Discusses data scarcity issues relevant to cold-start contexts but not directly in anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: low
      justification: Discusses model evaluation metrics (MAPE, RMSE) relevant to any forecasting system evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: low
      justification: Compares model performances, analogous to evaluating algorithmic modules.
  contribution: The paper offers a systematic taxonomy of forecasting methods by time horizon, which can inform the selection of algorithms for predicting financial inflows and outflows. The comparison of statistical and deep learning techniques highlights trade-offs between interpretability and accuracy, guiding module design for forecasting in Odin. The discussion of data variability and external factors is relevant for handling irregular spending patterns. The review's structured evaluation approach provides a methodological reference for assessing Odin's own forecasting modules.
  directly_justifies:
    - LSTM models are effective for capturing complex temporal dependencies in high-volatility data.
    - Hybrid models combining statistical and machine learning techniques often provide superior forecasting accuracy.
    - No universal forecasting method exists; model selection must be tailored to the specific data and forecast horizon.
  limits:
    - Focuses exclusively on electricity consumption, not personal financial transaction data.
    - Does not provide implementation details or code for the reviewed methods.
    - Does not address user privacy, interpretability, or user trust in the context of personal finance. [unacknowledged]
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. This paper is primarily a review of forecasting methods in the energy sector. Domains related to Filipino cultural context, expense categorization, existing systems, behavioral profiling, budget recommendation, anomaly detection, mobile design, privacy, retention, savings, and debt were all considered and rejected as they are outside the paper's scope. Topics under 'Predictive Modeling & Forecasting' (6.A, 6.B) were flagged as 'contextual' because the paper reviews algorithms and modeling concepts that are domain-agnostic and could be relevant to financial forecasting. Topic 8.C (Cold-Start Baseline Strategies) was given 'low' relevance due to the paper's discussion of data scarcity challenges. Topics 12.A and 12.B (Evaluation) were also noted as 'low' relevance for their discussion of general model evaluation metrics and approaches. The paper does not offer direct, actionable insights for Odin's specific financial domain but provides foundational knowledge on forecasting techniques. Overall relevance is low but provides a methodological starting point.
limitations:
  - Focuses exclusively on electricity consumption, not personal financial transaction data.
  - Does not provide implementation details or code for the reviewed methods.
  - Does not address user privacy, interpretability, or user trust in the context of personal finance. [unacknowledged]
remember_this:
  - The choice of forecasting model is highly dependent on the time horizon and data characteristics.
  - Hybrid models combining statistical and machine learning techniques often outperform standalone approaches.
  - Deep learning models like LSTM and Transformer are effective but require large datasets and computational resources.
  - Evaluation metrics like MAPE and RMSE are standard for comparing forecasting model performance.
```