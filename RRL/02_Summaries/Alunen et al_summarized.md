```yaml
paper_id: 10.46254/FA6.20250062
designation: local-algorithm-specific
title: Comparing Machine Learning Forecasting Models Based on Accuracy and Efficiency for Predicting Demand in a Food and Beverage Company
authors: Alunen, R. B.; Molina, C. F.; Quesada, R. F.; Reyes, C. N.; Jacob, D.
year: 2025
venue: Proceedings of the 6th African International Conference on Industrial Engineering and Operations Management
odin_topics:
  - 2.B
  - 2.D
  - 4.B
  - 6.A
  - 6.B
  - 12.A
  - 12.B
  - 12.C
tldr: Machine learning models, especially XGBoost, outperform traditional methods in demand forecasting for alcoholic beverages in the Philippines by capturing non-linear relationships and external factors.
problem_and_motivation: The Philippine food and beverage industry lacks sophisticated forecasting tools, leading to inefficiencies like overstocking and waste. Traditional methods fail to capture the influence of external factors such as holidays and weather on demand, particularly for alcoholic beverages where consumption patterns are complex.
approach:
  - Historical sales data from a Quezon City restobar (2021-2024) was merged with external data on unemployment, temperature, holidays, and day of week.
  - Four algorithms were evaluated: Random Forest, Gradient Boosting, XGBoost, and AdaBoost, using 80/20 train-test split with 10-fold cross-validation.
  - Feature selection via Pearson correlation and hyperparameter tuning via Grid Search and Random Search were applied to optimize model performance.
  - Accuracy was measured using MAE, MSE, RMSE, and R², while computational efficiency was measured by execution time.
  - The best-performing framework was identified by balancing accuracy and speed across multiple products.
findings:
  - XGBoost provided the best balance between high forecasting accuracy and computational efficiency.
  - Feature selection using correlation analysis improved computational efficiency but led to a slight reduction in forecast accuracy.
  - Random Search for hyperparameter tuning outperformed Grid Search in both accuracy and execution time.
  - num: Machine learning models reduced prediction errors by 22-33% in RMSE compared to heuristic forecasts.
  - num: R² values for ML models were around 0.42, significantly higher than exponential smoothing's 0.07, indicating better explanatory power.
  - While XGBoost and Random Forest showed highest accuracy, AdaBoost was fastest in execution for certain products.
key_figures_tables:
  - Table 2: Comparison of feature selection impact → Feature selection slightly reduces MAE but increases execution time.
  - Table 3: Comparison of hyperparameter tuning → Random Search is faster and often more accurate than Grid Search.
  - Figure 3: Visual comparison of ML algorithms → XGBoost and AdaBoost are computationally efficient while maintaining low errors.
  - Figure 5: Feature selection impact graph → Feature selection lowers MAE and MSE but not R².
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: XGBoost
    definition: Extreme Gradient Boosting, a scalable tree boosting algorithm.
  - term: MAE
    definition: Mean Absolute Error, the average magnitude of prediction errors.
  - term: MSE
    definition: Mean Squared Error, penalizes larger errors by squaring them.
  - term: RMSE
    definition: Root Mean Squared Error, sensitive to outliers.
  - term: R²
    definition: Coefficient of Determination, explains the proportion of variance captured by the model.
critical_citations:
  - "[Groene and Zakharov, 2024] — ML models reduce forecast error vs heuristics by 22-33%."
  - "[Liashchynskyi and Liashchynskyi, 2021] — Random search is more practical than grid search."
  - "[Venkatesh and Anuradha, 2019] — Pearson correlation is a common feature selection method."
relevance:
  topics:
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: The paper explicitly models holidays, day-of-week, and weather as predictors of alcoholic beverage demand.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: medium
      justification: Uses Philippine holiday data and local restobar sales to capture culturally specific spending cycles.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly identifies traditional forecasting heuristics and their failure to capture non-linear external factors.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Benchmarks ML algorithms (XGBoost, RF) for demand prediction, directly relevant to spending forecasting in PFMS.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Compares XGBoost, Random Forest, AdaBoost, and Gradient Boosting on time-series sales data.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses MAE, MSE, RMSE, R², and execution time, a comprehensive framework applicable to Odin's forecasting modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Provides a structured comparison of algorithmic performance (feature selection, tuning) for forecasting tasks.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: contextual
      justification: While not directly about budget recommendations, the evaluation approach is methodologically analogous.
  contribution: This paper provides a methodology for evaluating forecasting algorithms that can be adapted for Odin's spending prediction module. The comparison of XGBoost against other tree-based methods, along with the analysis of feature selection and hyperparameter tuning, offers actionable insights for designing Odin's forecasting engine. The paper's emphasis on balancing accuracy and computational efficiency is directly applicable to Odin's mobile-first, real-time constraints. The findings that XGBoost provides the best trade-off can justify its selection for Odin's core prediction functions.
  directly_justifies:
    - "XGBoost balances high forecasting accuracy and computational efficiency, making it suitable for real-time PFMS applications."
    - "Random Search for hyperparameter tuning provides better accuracy and speed than Grid Search for tree-based models."
    - "Feature selection using correlation improves efficiency at a small cost to accuracy, useful for resource-constrained mobile systems."
    - "External factors like holidays and weather significantly improve demand forecasting accuracy over pure historical sales data."
  limits:
    - "Single product category (alcoholic beverages) limits generalizability to other spending categories."
    - "Dataset is from a single restobar in Quezon City, not representative of national Filipino spending patterns."
    - "Does not address concept drift or model retraining, critical for adaptive PFMS systems."
    - "Privacy and ethical considerations of using macroeconomic data for personal forecasting are not discussed. [unacknowledged]"
  mapping_rationale: The systematic scan across all 12 functional domains identified strong relevance to Forecasting Algorithms (6.A, 6.B) and System Evaluation (12.A, 12.B, 12.C) due to the paper's core contribution of comparing ML models for demand forecasting. The paper's use of Philippine holiday and sales data links it to Seasonal Spending (2.B, 2.D) and its critique of traditional heuristics connects to Existing Systems Gaps (4.B). The paper was rejected for topics related to Behavioral Profiling (5), Budget Recommendation (7), Anomaly Detection (8), Mobile Design (9), Privacy (10), or Engagement (11) as it does not address these domains. The relevance of Filipino Demographic (1.A) is contextual, as the study uses Filipino data but does not analyze the demographic itself. Overall, the paper is highly relevant for Odin's forecasting module but has limited applicability to other functional areas.
limitations:
  - "Single product category (alcoholic beverages) limits generalizability to other spending types."
  - "Single source (one restobar) limits national applicability."
  - "Models were not evaluated for concept drift or retraining needs."
  - "Does not explore deep learning approaches like LSTM, which may be superior for sequential data. [unacknowledged]"
  - "The paper does not discuss the ethical or privacy implications of using external macroeconomic data. [unacknowledged]"
remember_this:
  - "XGBoost offers the best trade-off between prediction accuracy and execution time."
  - "Random Search is computationally superior to Grid Search for hyperparameter tuning."
  - "Feature selection with correlation improves speed but can slightly reduce accuracy."
  - "num: ML models reduce forecasting error by 22% to 33% compared to heuristic methods."
  - "External factors (holidays, weather, employment) are critical for accurate demand forecasting."
```