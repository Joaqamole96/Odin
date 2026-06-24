```yaml
paper_id: 3f7a1c8e-9b2d-5a4f-8e7c-1d2f3a4b5c6d
designation: local-algorithm-specific
title: Use of Boosting Algorithms in Household-Level Poverty Measurement: A Machine Learning Approach to Predict and Classify Household Wealth Quintiles in the Philippines
authors: Salvador, E. L. V.
year: 2022
venue: Unknown
odin_topics:
  - "5.A"
  - "6.A"
tldr: CatBoost achieved 90.93% accuracy in predicting Philippine household wealth quintiles, outperforming XGBoost, GBM, LightGBM, and AdaBoost using DHS data.
problem_and_motivation: Conventional econometric poverty measurements oversimplify poverty's multidimensional nature by relying on pre-selected features like income. Accurate poverty data is crucial for effective policy interventions, yet a gap exists in applying diverse machine learning methods to extensive Philippine household datasets.
approach:
  - Data from the 2022 Philippine Demographic and Health Survey was cleaned, reducing features from 2,099 to 396 and households from 30,372 to 20,679.
  - The dataset was split into 80% training and 20% testing, with 10% of training used for validation and hyperparameter tuning via manual and grid search.
  - Five boosting algorithms (AdaBoost, CatBoost, GBM, LightGBM, XGBoost) were implemented to classify wealth into five quintiles.
  - Feature selection using SelectFromModel identified 66 key features, with multicollinearity checked via Pearson correlation.
  - SMOTE addressed class imbalance, and models were evaluated on accuracy, precision, recall, F1-score, AUC-ROC, and computational efficiency metrics.
findings:
  - "num: CatBoost achieved the highest accuracy at 90.93%, followed by XGBoost (89.41%), GBM (89.05%), and LightGBM (88.52%)."
  - "num: AdaBoost performed significantly lower across all metrics, with an accuracy of 80.39% and F1-score of 80.15%."
  - CatBoost, GBM, LightGBM, and XGBoost achieved near-perfect AUC-ROC scores (0.98-1.00) for most wealth classes, effectively distinguishing poverty levels.
  - AdaBoost showed lower discriminative ability, especially for the "Poorest" and "Poorer" classes with AUC scores of 0.90 and 0.73 respectively.
  - "num: LightGBM and XGBoost exhibited a strong balance of performance and computational efficiency, with training times of 2.17 and 2.58 seconds and model sizes of 2.50 MB and 3.10 MB."
  - "num: CatBoost had the longest training time (69.29 seconds) and largest model size (30.50 MB) but was the most efficient during testing (0.01 seconds)."
  - AdaBoost had the shortest training time (4.48 seconds) but the longest testing time (0.23 seconds).
  - Feature selection highlighted household assets (e.g., television, refrigerator, vehicle) and housing characteristics as the most important predictors.
key_figures_tables:
  - "Figure 1: Distribution of missing values across features with threshold of 3,050 → Features with missing values exceeding the threshold were removed."
  - "Table 1: Description of 36 key features selected for poverty prediction → Key predictors include assets, housing materials, and utilities."
  - "Table 3: Performance metrics (Accuracy, Precision, Recall, F1) for five boosting models → CatBoost consistently outperformed all models across all metrics."
  - "Table 4: AUC-ROC scores per wealth class for each model → CatBoost, GBM, LightGBM, and XGBoost achieved near-perfect scores for most classes."
  - "Table 5: Computational efficacy (Training time, Testing time, Model size) → LightGBM and XGBoost offer the best balance of speed and size."
key_equations:
  - equation: "Accuracy = (TP + TN) / (TP + TN + FP + FN)"
    explanation: "Calculates overall correct predictions proportion."
  - equation: "Precision = TP / (TP + FP)"
    explanation: "Proportion of correct positive predictions."
  - equation: "Recall = TP / (TP + FN)"
    explanation: "Proportion of actual positives correctly identified."
  - equation: "F1 Score = 2 * (Precision * Recall) / (Precision + Recall)"
    explanation: "Harmonic mean of precision and recall."
definitions:
  - term: "AdaBoost"
    definition: "Adaptive Boosting, an ensemble method that combines weak learners sequentially."
  - term: "CatBoost"
    definition: "Gradient boosting algorithm designed to handle categorical features efficiently."
  - term: "DHS"
    definition: "Demographic and Health Survey, a nationally representative household survey."
  - term: "GBM"
    definition: "Gradient Boosting Machine, an ensemble method building models sequentially."
  - term: "LightGBM"
    definition: "Light Gradient Boosting Machine, a fast, distributed gradient boosting framework."
  - term: "SMOTE"
    definition: "Synthetic Minority Over-sampling Technique, addresses class imbalance by creating synthetic samples."
  - term: "XGBoost"
    definition: "Extreme Gradient Boosting, a scalable and efficient gradient boosting implementation."
critical_citations:
  - "[Li et al., 2022] — Identified underutilization of boosting in poverty prediction."
  - "[Tingzon et al., 2019] — Used machine learning with geospatial data for Philippine poverty mapping."
  - "[Bentéjac et al., 2021] — Comparative analysis shows boosting algorithms have improved speed and accuracy."
  - "[Alkire et al., 2015] — Supports multidimensional nature of poverty."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "low"
      justification: "Paper focuses on general household wealth classification, not financial behavior profiles."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "low"
      justification: "Demonstrates use of boosting algorithms for classification, a technique transferable to spending prediction."
  contribution: "This paper's comparative evaluation of boosting algorithms (CatBoost, XGBoost) for household classification provides a methodological reference for Odin's predictive modules. The use of SMOTE for class imbalance and feature selection techniques (SelectFromModel) can inform Odin's approach to handling sparse user data. The study's consideration of computational efficiency (training/testing time, model size) is directly relevant to Odin's mobile-first deployment constraints. However, the paper's application to poverty measurement, not personal finance, limits its direct applicability to Odin's forecasting or behavioral profiling tasks."
  directly_justifies:
    - "Boosting algorithms like CatBoost and XGBoost demonstrate high accuracy in classification tasks with structured data."
    - "Computational efficiency metrics are critical for selecting models for mobile-first applications."
    - "Feature selection and SMOTE can improve model performance on imbalanced datasets."
  limits:
    - "Paper predicts static wealth quintiles, not dynamic spending patterns or financial behaviors."
    - "The model is trained on DHS survey data, which differs significantly from app-generated transaction data."
    - "Analysis is for poverty classification, not regression-based forecasting of spending amounts."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. Domains related to Filipino cultural context (2.A-2.D), expense categorization (3.A-3.C), and user behavioral profiling (5.A-5.C) were considered. The paper was flagged as relevant for topic 5.A (Financial Behavioral Profiles) and 6.A (Predictive Modeling) due to its use of machine learning classification algorithms, but assigned a 'low' relevance because it addresses general poverty classification, not financial behavior. Domains such as budgeting (7.A-7.D), anomaly detection (8.A-8.C), and mobile-first design (9.A-9.B) were rejected as the paper does not address these areas. The overall relevance to Odin is contextual, providing methodological insights for model selection and evaluation rather than domain-specific knowledge."
limitations:
  - "Reliance on DHS data limits generalizability to other contexts."
  - "Further validation using alternative datasets is needed."
  - "Manual removal of interview-related features may introduce bias."
  - "Hyperparameter tuning was limited to manual and grid search."
  - "No error analysis for misclassifications per wealth class."
remember_this:
  - "CatBoost achieved the highest accuracy at 90.93%."
  - "LightGBM and XGBoost offer the best balance of speed and size."
  - "CatBoost had the longest training time but fastest testing."
  - "AdaBoost performed significantly worse than other boosting algorithms."
  - "Feature selection identified assets and housing as key poverty predictors."
```