```yaml
paper_id: 10.15294/sji.v11i3.4067
designation: international-algorithm-specific
title: Classification Modeling with RNN-based, Random Forest, and XGBoost for Imbalanced Data: A Case of Early Crash Detection in ASEAN-5 Stock Markets
authors: Siswara, D.; Soleh, A. M.; Wigena, A. H.
year: 2024
venue: Scientific Journal of Informatics
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 5.C
  - 2.D
tldr: RNN-based models, especially Simple RNN, outperform Random Forest and XGBoost for one-day-ahead market crash detection in ASEAN-5 stock markets, with SMOTE-ENN improving performance on imbalanced data.
problem_and_motivation: Predicting rare market crashes is critical yet challenging due to data imbalance and the need for timely warnings. Existing research often focuses on price movement rather than crash events, especially for emerging ASEAN-5 markets. There is a gap in comparing modern RNN architectures with classical algorithms for this specific imbalanced classification problem.
approach:
  - Used daily stock data (2010-2023) from five ASEAN-5 markets (Indonesia, Malaysia, Philippines, Singapore, Thailand) obtained from Yahoo Finance.
  - Defined market crashes using three Value at Risk (VaR) thresholds (5%, 2.5%, 1%) to create imbalanced binary target variables.
  - Engineered 213 technical indicators from local/global markets and commodities, expanded to 1,491 features using a time step of 7.
  - Compared three RNN architectures (Simple RNN, LSTM, GRU) against Random Forest and XGBoost, using SMOTE-ENN for handling class imbalance.
  - Employed Time Series Cross-Validation and a grid search for hyperparameter tuning, evaluating models on false alarm rate, hit rate, balanced accuracy, and PRC score.
findings:
  - num: RNN architectures demonstrated superior hit rates, balanced accuracy, and PRC scores compared to Random Forest and XGBoost across all VaR scenarios.
  - num: Simple RNN was the most superior RNN variant, achieving a balanced accuracy of up to 64% in some cases.
  - num: The overall hit rate for crash detection averaged 21%, which is consistent with findings in prior research on similar financial crises (9%-71%).
  - RNNs were particularly effective at detecting crashes during major crises like the COVID-19 pandemic but showed limitations in predicting crashes outside such periods.
  - SMOTE-ENN significantly improved model performance over the baseline, where most RNNs failed to detect any crashes.
  - In the Thailand dataset with 1% VaR, Random Forest unexpectedly outperformed RNNs, suggesting market-specific data characteristics influence model selection.
  - Simple RNN's superior performance is attributed to the data's limited complexity and its focus on short-term dependencies.
key_figures_tables:
  - Table 4: VaR thresholds for each country → Defines crash levels, showing varying risk tolerance (e.g., Indonesia -1.62% for 5% VaR).
  - Figure 5: Performance metrics after SMOTE-ENN for 1% VaR → RNNs show higher hit rate, balanced accuracy, and PRC than RF/XGBoost.
  - Table 5: Average performance values across all datasets → RNN has highest hit rate (0.278) for 1% VaR, XGBoost has highest false alarm rate (0.987).
  - Figure 6: Country-wise performance for 1% VaR → Thailand dataset shows Random Forest outperforming RNNs in hit rate and balanced accuracy.
  - Figure 7: Visualization of RNN crash detection for Indonesia (2020-2023) → Model successfully identified COVID-19 crash but missed later events.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: RNN
    definition: Recurrent Neural Network, a class of neural networks designed for sequential data.
  - term: LSTM
    definition: Long Short-Term Memory, an RNN variant with gating mechanisms for long-term dependencies.
  - term: GRU
    definition: Gated Recurrent Unit, a simplified RNN variant with fewer gates than LSTM.
  - term: XGBoost
    definition: Extreme Gradient Boosting, an ensemble machine learning algorithm known for handling imbalanced data.
  - term: VaR
    definition: Value at Risk, a statistical measure of the potential loss in value of an asset or portfolio.
  - term: SMOTE-ENN
    definition: Synthetic Minority Over-sampling Technique combined with Edited Nearest Neighbors for handling imbalanced data.
critical_citations:
  - "[Chatzis et al., 2018] — Foundational for using deep learning for stock market crisis events."
  - "[Dichtl et al., 2023] — Provided comparative hit rate intervals for stock market crash prediction."
  - "[Bluwstein et al., 2023] — Used machine learning for financial crisis prediction, relevant for methodology."
  - "[Tölö, 2020] — Applied RNNs for systemic financial crisis detection, a key reference."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly compares predictive models (RNNs, RF, XGBoost) for time-series classification of crash events.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Evaluates specific sequential algorithms (Simple RNN, LSTM, GRU) on daily market data, analogous to spending data.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Market crash detection is framed as an anomaly classification problem in financial data.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: The RNN and ensemble methods are applicable to anomaly detection; provides performance benchmarks.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: The classification approach is for market events, not user behaviors, but the methodology is transferable.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: The Philippines is one of the five markets studied, providing general insight into its market behavior.
  contribution: "This research provides a comparative benchmark for RNN and ensemble methods on imbalanced time-series classification, which can inform the selection of models for Odin's anomaly detection and forecasting modules. The finding that Simple RNN outperforms more complex LSTM and GRU for certain data characteristics is a critical design insight for model choice in Odin. The successful application of SMOTE-ENN to improve model performance offers a potential strategy for Odin's cold-start problem in anomaly detection. The study's rigorous evaluation framework (hit rate, false alarm rate, PRC) provides a template for evaluating Odin's predictive modules."
  directly_justifies:
    - "RNN-based models are more effective than tree-based models for predicting rare sequential events like market crashes."
    - "Simple RNN can outperform LSTM and GRU when the data characteristics are not overly complex and focus on short-term dependencies."
    - "SMOTE-ENN is an effective technique for improving classification performance on highly imbalanced datasets."
    - "Market-specific data characteristics may require different model selections."
  limits:
    - "The study's average hit rate of 21% is relatively low, indicating room for significant improvement in crash detection accuracy."
    - "Analysis is specific to ASEAN-5 stock markets and may not generalize directly to personal spending data."
    - "RNN models showed limitations in detecting crashes outside of major crisis periods, suggesting challenges in long-term prediction."
    - "The study only predicts one day ahead, which may be too short a horizon for some personal finance use cases."
    - "The performance of models on the Philippines market is not broken out separately [unacknowledged]."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The domains flagged as relevant were 'Spending Forecasting' (6.A, 6.B) and 'Anomaly Detection' (8.A, 8.B) due to the paper's core focus on predictive modeling for rare crash events. 'Behavioral Profiling & Classification' (5.C) was flagged as low relevance because the classification is for events, not user profiles, but the algorithmic approach is transferable. 'Filipino Cultural Context' (2.D) was marked as contextual as the Philippines is part of the dataset. Domains such as 'Expense Categorization,' 'Budget Recommendation,' and 'Mobile-First Design' were considered and rejected as the paper does not address these areas. The borderline case of 6.A/6.B and 8.A/8.B was resolved by selecting both sets, as the paper is equally applicable to forecasting and anomaly detection. Overall, the paper is highly relevant for its evaluation of forecasting and anomaly detection algorithms in a time-series context."
limitations:
  - "The study's average hit rate of 21% is relatively low, indicating room for significant improvement in crash detection accuracy."
  - "Analysis is specific to ASEAN-5 stock markets and may not generalize directly to personal spending data."
  - "RNN models showed limitations in detecting crashes outside of major crisis periods, suggesting challenges in long-term prediction."
  - "The study only predicts one day ahead, which may be too short a horizon for some personal finance use cases."
  - "The performance of models on the Philippines market is not broken out separately [unacknowledged]."
remember_this:
  - "Simple RNN outperformed LSTM and GRU for ASEAN-5 crash detection."
  - "RNN models achieved superior hit rates over Random Forest and XGBoost."
  - "SMOTE-ENN was necessary for RNNs to detect any crashes on imbalanced data."
  - "The average hit rate for crash detection was 21%."
  - "Simple RNN achieved a balanced accuracy of up to 64%."
```