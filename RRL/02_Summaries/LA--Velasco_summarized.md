```yaml
paper_id: 10.20944/preprints202603.1811.v1
designation: local
title: A Decade of Applied Quantitative Analytics for Philippine Policy: Forecasting, Statistical Forensics, and Predictive Modeling Across Education, Energy, Agriculture, Health, and Finance
authors: Velasco, A.
year: 2026
venue: Preprints.org
odin_topics:
  - 4.A
  - 4.B
  - 6.A
  - 6.B
  - 7.A
  - 8.A
  - 8.B
  - 12.A
  - 12.B
tldr: Reviews Philippine policy analytics across sectors, showing a progression from descriptive models toward machine learning, Benford-based anomaly detection, and explainable AI.
problem_and_motivation: Governments must allocate scarce resources under uncertainty, and while quantitative analytics is central to this, the application and maturation of these methods in the Philippine context across key policy sectors has not been systematically synthesized.
approach:
  - A structured narrative review of a core corpus of 17 Philippine studies from 2019 to 2025 was conducted.
  - Studies were coded on five dimensions: domain, dataset, modeling approach, validation strategy, and policy contribution.
  - The sectors covered include education, energy, agriculture, health, and finance.
  - External comparison literature was used to position the corpus against broader international developments in the respective fields.
  - The review identifies cross-cutting methodological trends and gaps in validation and integration.
findings:
  - The literature shows a clear progression from descriptive diagnostics and classical time-series models toward machine learning, deep learning, and explainable AI.
  - A distinct forensics strand emerged through Benford-based anomaly detection for data quality assessment in agriculture and health.
  - Forecasting studies have moved from univariate ARIMA to comparative machine learning, including random forests, neural networks, and LSTM.
  - Validation rigor is uneven, ranging from explicit holdout sets to residual diagnostics and significance testing.
  - num: The machine-learning study on rice and corn forecasting reported the best overall performance for random forests.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: ARIMA
    definition: Autoregressive Integrated Moving Average, a class of statistical models for time series forecasting.
  - term: SARIMA
    definition: Seasonal Autoregressive Integrated Moving Average, an extension of ARIMA that supports seasonal data.
  - term: LSTM
    definition: Long Short-Term Memory, a type of recurrent neural network architecture capable of learning long-term dependencies.
  - term: NNAR
    definition: Neural Network Autoregression, a time series forecasting model using a neural network.
  - term: SHAP
    definition: SHapley Additive exPlanations, a method for interpreting the output of machine learning models.
  - term: Benford's Law
    definition: An observation that in many naturally occurring datasets, the leading digit is likely to be small.
critical_citations:
  - "[Rumberger & Lim, 2008] — Foundational review of dropout research."
  - "[van Klompenburg et al., 2020] — Systematic review of ML for crop yield prediction."
  - "[World Health Organization, 2021] — Guide on using routine data for health monitoring."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides a methodological landscape for applied analytics in the Philippines.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies specific gaps like limited multivariate modeling and uneven validation.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Reviews forecasting methods applicable to spending prediction.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Discusses ARIMA, machine learning, and deep learning for time-series forecasting.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Reviews forecasting as a basis for planning and resource allocation.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Reviews Benford-based anomaly detection for data quality and fraud screening.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Forensics strand using Benford's law provides a methodological example.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Critiques validation practices, noting uneven rigor and advocating for better methods.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Discusses model benchmarking, error metrics, and the need for external validation.
  contribution: "This paper provides a systematic review of forecasting, anomaly detection, and predictive modeling techniques applied to Philippine data, which directly informs Odin's algorithmic module selection and validation framework. Its critique of univariate models and uneven validation justifies Odin's investment in multivariate forecasting and rigorous holdout evaluation. The review of Benford-based forensics supports Odin's anomaly detection approach, and its call for integrated analytics architectures aligns with Odin's goal of combining forecasting, budgeting, and anomaly detection. The identified gaps, such as limited uncertainty quantification and operational deployment, serve as cautionary points for Odin's development roadmap."
  directly_justifies:
    - "The progression from ARIMA to machine learning supports selecting LSTM or random forest for spending forecasting."
    - "Benford-based anomaly detection is a valid, low-cost method for screening financial data."
    - "Explicit train-validation splits and error metrics are necessary for evaluating Odin's forecasting module."
    - "External validation across user cohorts is a critical gap that Odin should address."
  limits:
    - "The paper is a review and does not provide original empirical findings for Odin to directly cite for specific model performance."
    - "The financial sector review is limited to stock-index prediction, not personal spending patterns."
    - "Recommendations are high-level and require translation into specific implementation details for a PFMS."
  mapping_rationale: "All 12 functional domains and their associated topic codes were systematically scanned. The domains of 'Spending Forecasting' (6.A, 6.B), 'Anomaly Detection' (8.A, 8.B), and 'System Evaluation' (12.A, 12.B) were flagged as high relevance due to the paper's detailed review of forecasting methods, Benford-based forensics, and validation practices. The 'Existing Systems & Gaps' domain (4.A, 4.B) was selected as high/contextual because the paper provides a landscape of applied analytics and explicitly lists methodological limitations. 'Budget Recommendation' (7.A) was medium relevance as it provides domain knowledge on resource allocation. The paper was considered and rejected for 'Financial Behavioral Profiles' (5.A-C), 'Filipino Cultural Context' (2.A-D), and 'Data Privacy & User Trust' (10.A, 10.B) as it does not discuss these specific topics. The overall relevance is high for informing the design and evaluation of Odin's algorithmic core."
limitations:
  - "The corpus is heterogeneous, mixing journal articles and preprints with varying validation designs. [unacknowledged]"
  - "Direct numerical comparison across sectors is not intended due to differences in data frequency and sample size. [acknowledged]"
  - "Limited evidence of operational deployment or external validation of the models reviewed. [acknowledged]"
  - "The review focuses on sectoral policy and does not cover personal finance or behavioral profiling. [unacknowledged]"
remember_this:
  - "Philippine applied analytics progressed from descriptive models to machine learning and anomaly detection."
  - "Validation practices are uneven; explicit holdout sets are not universal."
  - "Benford-based law is used for data quality audits in health and agriculture."
  - "Future work requires integrated, multivariate, and uncertainty-aware analytics."
```