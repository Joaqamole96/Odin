```yaml
paper_id: 13523fe0-2a2d-5e2f-9a5c-5b8c9d2e4f3a
designation: local # Published in Technological University of the Philippines - Manila
title: WEKA-BASED DECISION-TREE MODEL FOR USER SUBSCRIPTION PLAN PREDICTION
authors: Guban, J. C. R.; Menderico, C. D. R.; Montalban, D. M. G.
year: 2025
venue: Technological University of the Philippines - Manila
odin_topics:
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 6.A
tldr: A J48 decision-tree model achieves 72% accuracy predicting streaming subscription plans from user demographics and behavioral attributes, identifying country as the strongest predictor.
problem_and_motivation: Streaming platforms lack interpretable models to predict how demographic and behavioral attributes jointly influence subscription plan selection. This limits data-driven personalization and targeted marketing strategies. An accessible, rule-based approach is needed to bridge user behavior with platform optimization.
approach:
  - A supervised classification model using the J48 decision-tree algorithm was developed in WEKA.
  - The dataset comprised 2,500 anonymized user records with six attributes: country, age, gender, device type, subscription start month, and target plan.
  - An 80/20 train-test split was applied to evaluate out-of-sample performance.
  - Performance was assessed using accuracy, Kappa statistic, precision, recall, F-measure, and ROC area.
  - The model was validated against a held-out test set of 500 instances.
findings:
  - num: The model achieved an overall accuracy of 72% on the test set.
  - Country was identified as the most influential predictor of subscription type, followed by age and device type.
  - The decision tree generated interpretable rules showing that younger smartphone users subscribing later in the year often chose Premium plans.
  - Older users on Smart TVs tended toward Standard or Basic tiers.
  - The Standard category achieved the highest precision (0.793) and ROC area (0.871), indicating reliable identification.
  - Confusion matrix showed balanced performance across classes with 123 Basic, 119 Standard, and 118 Premium correct predictions.
key_figures_tables:
  - Table 1: Performance summary on test set → Accuracy 72%, Kappa 0.5797, MAE 0.2216.
  - Table 2: User profile combinations for each country → Country-specific rules reveal distinct segmentation patterns.
  - Table 3: Class-level metrics → Standard has highest precision (0.793) and ROC (0.871); all plans show balanced F-measures.
  - Table 4: Confusion matrix → Diagonal values (123,118,119) show balanced correct classifications across tiers.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: J48
    definition: An open-source Java implementation of the C4.5 decision-tree algorithm in WEKA.
  - term: WEKA
    definition: Waikato Environment for Knowledge Analysis, a suite of machine learning software.
  - term: ROC Area
    definition: Area under the Receiver Operating Characteristic curve, measuring classification discrimination ability.
  - term: Kappa Statistic
    definition: A measure of agreement between predicted and actual classifications, correcting for chance.
  - term: Confusion Matrix
    definition: A table showing correct and incorrect classifications for each class.
critical_citations:
  - "[Aouad et al., 2023] — Validates large decision trees can generalize with proper validation."
  - "[Hsiao, 2023] — Establishes 70% accuracy benchmark for commercial predictive models."
  - "[Garcia & Lee, 2022] — Supports use of decision trees for subscription plan prediction."
  - "[Orozco-Arias, 2020] — Provides rationale for using ROC area as a performance metric."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Demonstrates a classification approach applicable to PFMS user segmentation.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: low
      justification: Recommends incorporating behavioral indicators beyond demographics to improve prediction.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Shows how demographic and behavioral attributes can profile user groups.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Directly applies decision-tree classification to predict user plan choices from profile attributes.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Demonstrates a predictive model for user behavior that can be adapted for spending forecasting.
  contribution: The paper's decision-tree methodology provides a template for Odin's behavioral profiling module, enabling interpretable classification of users based on demographic and behavioral attributes. The feature importance analysis (country, age, device) informs which user attributes are most predictive for segmentation. The validation approach with an 80/20 split and multi-metric evaluation (precision, recall, ROC) offers a framework for Odin's system evaluation module. The interpretable rule extraction supports transparent decision-making for budget recommendation and anomaly detection modules.
  directly_justifies:
    - "Decision trees can predict user plan choices with 72% accuracy from demographic and behavioral attributes."
    - "Country, age, and device type are the most influential predictors of user classification."
    - "Interpretable decision rules reveal how attribute combinations map to specific user segments."
    - "An 80/20 train-test split with multi-metric evaluation provides reliable model validation."
  limits:
    - "Dataset was limited to five user attributes, excluding behavioral indicators like watch time or session frequency."
    - "The model was validated on a single dataset; cross-validation or external validation was not performed."
    - "Ensemble methods were not explored, potentially missing complex nonlinear interactions."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains flagged as relevant were: Existing Systems & Gaps (4.A, 4.B), Behavioral Profiling & Classification (5.A, 5.C), and Spending Forecasting (6.A). Topic 5.C was assigned high relevance because the paper directly applies a decision-tree classifier to predict user plan choices from profile attributes—a technique transferable to financial behavioral profile classification in Odin. Topic 6.A received high relevance as the paper demonstrates a predictive modeling approach for user behavior that can be adapted for spending forecasting. Topic 4.A was deemed contextual, as the paper illustrates a classification approach applicable to PFMS user segmentation. Topic 4.B was low relevance, as limitations were acknowledged but not deeply explored. Topic 5.A was medium relevance, as the paper profiles user groups based on demographic attributes, aligning with behavioral profiling goals. Other domains (e.g., Cultural Context, Mobile-First Design, Data Privacy, User Retention) were considered and rejected because the paper does not address Filipino cultural practices, mobile design considerations, privacy concerns, or engagement dynamics. The paper's overall relevance to Odin lies in its provision of a validated, interpretable classification framework and a feature importance analysis that can inform user segmentation and predictive modeling modules.
limitations:
  - "The dataset was limited to five user attributes, excluding behavioral indicators such as watch time, session frequency, or genre preferences, which may improve prediction accuracy."
  - "The model was validated using a single 80/20 split; k-fold cross-validation was not employed to assess variance in performance [unacknowledged]."
  - "Ensemble methods like Random Forests or Gradient Boosted Trees were not explored, potentially missing complex nonlinear interactions [unacknowledged]."
  - "The model was not tested on a different dataset or in a real-time deployment setting to assess generalizability and operational value."
remember_this:
  - "A decision tree achieved 72% accuracy predicting subscription plans from six user attributes."
  - "Country was the strongest predictor, followed by age and device type."
  - "The model generated interpretable rules linking user profiles to Basic, Standard, or Premium plans."
  - "Standard plan classification performed best with precision of 0.793 and ROC area of 0.871."
  - "Feature importance from decision trees can inform targeted user segmentation in personal finance systems."
```
