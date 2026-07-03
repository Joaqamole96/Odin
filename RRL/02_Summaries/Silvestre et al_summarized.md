```yaml
paper_id: 10.1007/s40558-025-00349-9
designation: international-algorithm-specific
title: Navigating uncertainty: enhancing hotel cancellation predictions with adaptive machine learning
authors: Silvestre, P.; Antonio, N.; Carrasco, P.
year: 2026
venue: Information Technology & Tourism
odin_topics:
  - 6.A
  - 6.B
  - 4.A
  - 4.B
  - 12.A
  - 12.B
  - 11.A
  - 11.B
  - 8.A
tldr: Dynamic retraining with a sliding window improves hotel cancellation prediction accuracy during pandemics, supporting proactive revenue management.
problem_and_motivation: Machine learning models for hotel booking cancellations perform well on historical data but are rarely tested under severe disruption like the COVID-19 pandemic. The gap is understanding if pre-pandemic models remain effective under extreme volatility and how to adapt them to maintain predictive accuracy.
approach:
  - Used hotel booking data from four Portuguese hotels (two city, two resort) with 670,343 bookings from 2014 to 2021.
  - Applied XGBoost classifiers with hyperparameter tuning via grid and random search.
  - Study One trained models on pre-pandemic data (before March 2020) and tested on pandemic data.
  - Study Two used a sliding-window training approach incorporating pandemic data with a 24-month training and 9-month test window.
  - Evaluated performance using Accuracy, Precision, F1-Score, and AUC, and interpreted features with SHAP.
findings:
  - num: Pre-pandemic models achieved fair to excellent AUC scores (0.70-0.93) on pandemic test data.
  - num: Sliding-window models improved AUC by up to 5 percentage points over static models.
  - num: A nine-month training window with the sliding approach balanced stability and responsiveness to rapid shifts.
  - Feature importance shifted during the pandemic; LeadTime remained dominant but its effective crossover threshold compressed.
  - num: City hotel C2 achieved the highest performance with an AUC of 0.99 in the sliding-window approach.
  - Resort hotels, which performed worse with static models, showed substantial improvement with the sliding window approach.
key_figures_tables:
  - Table 1: Dataset statistics for four hotels → Provides context on data size and composition.
  - Figure 2: Monthly cancellation rate per hotel pre- and during COVID-19 → Shows unprecedented spikes in cancellations during the pandemic.
  - Table 7: Performance metrics for sliding window models → Documents improved AUC values across all hotels.
  - Figure 5: Lead time density plots with crossover thresholds → Shows pandemic-era compression of cancellation risk thresholds.
  - Figure 7: SHAP summary plots for W2 models → Visualizes the rotation of feature importance across regimes.
key_equations:
  - equation: ADRThirdQuartileDeviation = ADR / ADR_{third quartile of DistributionChannel, per room type, week and year}
    explanation: Captures normalized price position relative to similar bookings.
definitions:
  - term: AUC
    definition: Area Under the ROC Curve, a measure of classification model performance.
  - term: XGBoost
    definition: An optimized gradient boosting algorithm for supervised learning.
  - term: CRISP-DM
    definition: Cross-Industry Standard Process for Data Mining, a structured data mining methodology.
  - term: SHAP
    definition: Shapley Additive Explanations, a method for interpreting model predictions.
  - term: Concept Drift
    definition: Change in the data distribution or the relationship between inputs and outputs over time.
critical_citations:
  - "[António, 2019a] — Established baseline models for booking cancellation prediction."
  - "[Žliobaitė et al., 2016] — Provided theoretical framing for concept drift application."
  - "[Lundberg and Lee, 2017] — Introduced SHAP for model interpretability."
  - "[Baier et al., 2020] — Demonstrated retraining with recent data for concept drift."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly evaluates forecasting models under distributional change.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Tests XGBoost and sliding-window adaptation on sequential booking data.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews state of ML for cancellation prediction, analogous to PFMS forecasting.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies lack of robustness testing under concept drift as a gap.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses standard ML metrics (AUC, F1) and out-of-time validation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Provides a blueprint for evaluating model performance under data shifts.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: Adaptive models support proactive interventions, indirectly linking to user engagement.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: low
      justification: Concept drift management helps maintain forecast reliability for retention strategies.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: The pandemic is treated as an anomaly context, but the paper is about prediction, not detection.
  contribution: This paper provides a validated methodology for building adaptive machine learning models that maintain predictive accuracy under severe disruption, directly applicable to Odin's spending forecasting module. It demonstrates that dynamic retraining with a sliding window outperforms static models, supporting Odin's need for robust and responsive financial predictions. The use of SHAP for tracking feature importance shifts offers a framework for monitoring and explaining changes in user financial behavior. The concept-drift analysis and LeadTime threshold compression can inform Odin's design of proactive notifications and adaptation mechanisms.
  directly_justifies:
    - "Maintaining forecast accuracy under volatility requires scheduled retraining and drift monitoring."
    - "Adaptive models with sliding-window retraining capture rapid shifts in behavioral patterns."
    - "Monitoring feature importance changes helps understand evolving user behavior."
    - "A nine-month training window balances stability and responsiveness in volatile contexts."
    - "Interpretable diagnostics like threshold shifts support actionable model insights."
  limits:
    - "Models were not deployed in a live production environment."
    - "Qualitative reasons behind cancellations or hotel-forced cancellations were not captured."
    - "Customer country of origin, which could provide further insights, was not included."
    - "The study is limited to four hotels in Portugal, which may not generalize to other contexts [unacknowledged]."
  mapping_rationale: The systematic scan across all 12 functional domains and their topic codes flagged the Spending Forecasting domain as highly relevant, with codes 6.A and 6.B identified as high relevance because the paper directly tests and compares forecasting algorithms under distributional shift. The Existing Systems & Gaps domain was assessed as medium relevance, as the paper reviews prior models and identifies the gap in robustness testing. The System Evaluation domain was also medium relevance, as it uses standard ML evaluation metrics and frameworks. The User Retention & Engagement domain was considered low relevance because while adaptive models support proactive interventions, engagement dynamics are not the focus. The Anomaly Detection domain was contextual, as the pandemic is an anomaly context but the paper is about prediction, not detection. Domains related to Filipino cultural context, expense categorization, behavioral profiling, budget recommendation, mobile-first design, data privacy, and savings/debt management were rejected as they are not addressed. The overall relevance is medium-high, as the paper provides a robust methodology and framework for adaptive prediction that directly informs Odin's forecasting module.
limitations:
  - "Models were not deployed in a live production environment."
  - "Qualitative reasons behind cancellations or hotel-forced cancellations were not captured."
  - "Customer country of origin, which could provide further insights, was not included."
  - "The study is limited to four hotels in Portugal, which may not generalize to other contexts [unacknowledged]."
remember_this:
  - "Sliding-window retraining improved AUC by up to 5 percentage points."
  - "Adaptive models better capture rapid shifts in cancellation behavior."
  - "LeadTime remained the dominant predictor despite changed thresholds."
  - "Monitoring feature importance shifts helps identify changing user patterns."
  - "Dynamic model retraining is essential for maintaining accuracy under volatility."
```