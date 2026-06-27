```yaml
paper_id: 10.17559/TV-20220430111309
designation: international-algorithm-specific
title: An Overview of Forecasting Methods for Monthly Electricity Consumption
authors: Krstev, S.; Forcan, J.; Krneta, D.
year: 2023
venue: Technical Gazette
odin_topics:
  - 6.A
  - 6.B
  - 12.A
  - 12.B
  - 12.C
  - 2.B
  - 5.A
  - 5.B
tldr: Compares twelve statistical and machine learning forecasting models for monthly electricity consumption, finding neural network autoregression achieves the highest accuracy.
problem_and_motivation: Accurate mid-term electricity load forecasting is crucial for utility operations and deregulated markets, yet research on this time horizon is limited compared to short-term forecasting. The challenge is compounded by the influence of both consumption habits and external random factors.
approach:
  - Data is monthly electricity consumption (kWh) from 60,000 metering points in Bosnia and Herzegovina from 2000 to 2020.
  - Classical time series models include seasonal naïve, ARIMA, ETS, and structural models with Kalman filter.
  - Machine learning methods include linear regression, elastic net, KNN, random forest, XGBM, and SVM with lm and PCA feature selection.
  - A neural network autoregression (NNAR) with lagged values and a three-layer architecture is also applied.
  - Model performance is evaluated using Mean Absolute Percentage Error (MAPE) on a hold-out test set of the last 15 months.
findings:
  - "num: Neural network autoregression (NNAR) achieves the lowest MAPE of 2.67%."
  - "num: Classical time series methods (ETS at 3.28%, ARIMA at 3.36%) outperform most machine learning models."
  - "num: The best machine learning model, PCA+KNN, achieves a MAPE of 4.38%."
  - "num: The seasonal naïve method serves as a baseline with a MAPE of 4.16%."
  - Classical methods are more accurate than machine learning methods for this small sample size dataset.
key_figures_tables:
  - "Figure 4: Forecasts from classical models → ETS shows best fit visually."
  - "Figure 5 & 6: Forecasts from ML with lm and PCA → PCA feature selection slightly improves performance."
  - "Figure 7: Forecast from NNAR → Predictions closely follow the test data pattern."
  - "Figure 8: MAPE comparison bar chart → NNAR has the lowest MAPE, followed by ETS."
  - "Table 2: MAPE for ML methods → PCA+KNN is the best ML approach at 4.38%."
  - "Table 3: Monthly absolute relative errors → NNAR is most accurate for the majority of test months."
key_equations:
  - equation: "y'_{T+h|T} = y_{T+h-m(k+1)}"
    explanation: "Seasonal naive forecast equals value from previous season."
  - equation: "MAPE = 100/n * Σ(|(y_t - y'_t) / y_t|)"
    explanation: "Mean absolute percentage error as accuracy measure."
definitions:
  - term: "MTLF"
    definition: "Mid-term load forecast, for a time horizon from two weeks to two years."
  - term: "MAPE"
    definition: "Mean absolute percentage error, a measure of prediction accuracy."
  - term: "DSO"
    definition: "Distribution System Operator, the utility company managing the distribution network."
  - term: "NNAR"
    definition: "Neural network autoregression, a model using lagged values as inputs to a neural network."
critical_citations:
  - "[Makridakis et al., 2018] — Classical methods outperform ML for univariate series."
  - "[Cerqueira et al., 2019] — Sample size influences performance of statistical vs ML methods."
  - "[Hyndman & Athanasopoulos, 2014] — Source for time series forecasting methodologies."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: "Compares multiple predictive models for a sequential time series forecasting problem."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: "Evaluates classical and ML forecasting algorithms on monthly consumption data, a parallel to spending."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: "Provides a structured evaluation framework using MAPE and out-of-sample testing."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: "Provides a benchmark of algorithmic performance for forecasting modules."
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: low
      justification: "The comparative methodology for selecting a forecasting model can inform budget recommendation evaluation."
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: "The electricity consumption data demonstrates strong seasonality, analogous to spending cycles."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: low
      justification: "Briefly touches on consumption habits as a factor but does not profile users."
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: low
      justification: "The challenge of limited data for MTLF is analogous to the cold-start problem in profiling."
  contribution: "This paper provides a direct comparison of twelve forecasting models, which can guide the selection of a predictive engine for Odin's spending forecast module. The finding that neural networks excel with sufficient data supports the choice of algorithm for a core Odin feature. The rigorous evaluation using MAPE and a rolling forecast origin offers a template for testing Odin's own forecasting accuracy. The conclusion that data quality and pre-processing are critical validates the emphasis on data cleaning in Odin's pipeline."
  directly_justifies:
    - "Neural network autoregression is a high-accuracy method for monthly time series forecasting."
    - "Classical time series models like ETS are strong baselines for data with seasonal patterns."
    - "A rolling forecasting origin is a robust evaluation technique for time series models."
    - "For small datasets, classical methods can outperform more complex machine learning approaches."
  limits:
    - "The paper focuses on a single dataset (electricity) and may not generalize to all spending patterns."
    - "It does not address the integration of forecasting into a broader personal finance management system."
    - "The study does not explore real-time or user-interactive forecasting, which is key for Odin."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper's primary relevance is to the 'Spending Forecasting' domain (6.A, 6.B), as its core contribution is comparing forecasting methods for monthly data. It also provides a methodological framework for 'System Evaluation' (12.A, 12.B, 12.C), specifically for comparing algorithmic performance. The paper's mention of seasonal patterns (2.B) and consumption habits (5.A, 5.B) is contextual but does not provide actionable insights for user profiling. Domains like 'Expense Categorization' (3.A), 'Budget Recommendation' (7.A), and 'Anomaly Detection' (8.A) were considered but rejected as the paper focuses solely on forecasting, not on categorization, optimization, or anomaly identification. The paper's overall relevance is high for the forecasting module, medium for evaluation methodologies, and low or contextual for other domains. This contributes primarily to the technical design and evaluation strategy for Odin's predictive components."
limitations:
  - "Small sample size (228 training points) limits generalizability to data-rich environments. [unacknowledged]"
  - "The study does not compare hybrid models, which current research suggests may improve accuracy."
  - "Data is limited to a single geographic region and type of consumption, which may not represent PFMS spending data."
  - "The paper does not address computational cost, a key constraint for mobile-first systems."
  - "It does not evaluate the explainability of the models, crucial for user trust in PFMS."
remember_this:
  - "NNAR achieved the best forecasting accuracy with a MAPE of 2.67%."
  - "Classical time series models like ETS are robust baselines for seasonal data."
  - "Model performance is highly dependent on data quality and pre-processing."
  - "For small datasets, simpler models can outperform complex neural networks."
  - "Seasonal patterns are a critical component of monthly consumption forecasting."
```