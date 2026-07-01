```yaml
paper_id: 10.1016/j.procs.2026.05.035
designation: international-algorithm-specific
title: Consumer Behavior Data Mining and Analysis Using Machine Learning Algorithms
authors: Zhang, H.; Hou, Y.
year: 2026
venue: Procedia Computer Science
odin_topics:
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 12.B
  - 12.C
tldr: XGBoost achieves the highest accuracy and F1 score among four ML algorithms for predicting customer purchase intention from e-commerce transaction data.
problem_and_motivation: Predicting customer purchase intention from vast e-commerce data is challenging for traditional statistical tools. A systematic comparison of modern machine learning algorithms under a unified framework is needed to guide model selection for practical applications.
approach:
  - Used the UCI Online Retail dataset with transactions from Dec 2020 to Dec 2021 for model training and evaluation.
  - Engineered 28 numerical features per customer, including RFM, behavioral breadth, consumption patterns, and temporal patterns.
  - Evaluated logistic regression, SVM, random forest, and XGBoost on the binary prediction task of future purchase intent.
  - Employed grid search with 5-fold cross-validation for hyperparameter tuning on the training set.
  - Assessed models on a held-out test set using accuracy, precision, recall, F1 score, and AUC metrics.
findings:
  - XGBoost achieves the highest F1 score of 0.680 and AUC of 0.872 among all models tested.
  - Random forest obtains a balanced performance with an F1 score of 0.651 and AUC of 0.853.
  - Logistic regression shows the lowest recall at 0.468, indicating a conservative prediction strategy.
  - Recency is the most important predictor across all models, validating the RFM framework's core premise.
  - XGBoost demonstrates superior training efficiency compared to random forest despite its higher accuracy.
key_figures_tables:
  - Table 1: Comprehensive performance metrics for four models → XGBoost leads all models across accuracy, F1, and AUC.
  - Table 2: Training and prediction time comparison → Logistic regression is fastest; SVM is slowest; XGBoost is efficient.
  - Table 3: Top three feature importance rankings → Recency is consistently the most important feature across models.
key_equations:
  - equation: P(y = 1 | x) = 1 / (1 + e^{-(w^T x + b)})
    explanation: Sigmoid function maps features to purchase probability in logistic regression.
  - equation: f(x) = sign(∑_{i=1}^{n} α_i y_i K(x_i, x) + b)
    explanation: Decision function for SVM using kernel trick for nonlinear classification.
definitions:
  - term: RFM
    definition: Recency, Frequency, Monetary; a customer segmentation framework using three transaction metrics.
  - term: AUC
    definition: Area Under the ROC Curve; measures the model's ability to rank positive samples higher than negative ones.
  - term: XGBoost
    definition: eXtreme Gradient Boosting; an optimized implementation of gradient boosting for efficiency and performance.
critical_citations:
  - "[Akram, 2025] — Reviews ML algorithms for consumer behavior prediction."
  - "[Lin, 2023] — Applies ML to e-commerce customer shopping behavior analysis."
  - "[Zvarikova, 2022] — Discusses cognitive AI algorithms for customer behavior analysis."
relevance:
  topics:
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: The study's feature engineering and predictive modeling approach can inform how Odin initializes user profiles based on sparse transaction data.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: The paper compares classification algorithms (LR, SVM, RF, XGBoost) that could be used to classify user spending behavior profiles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: The paper directly addresses predictive modeling of consumer behavior using machine learning on transaction data.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: The study compares various forecasting algorithms, including XGBoost and Random Forest, on sequential transaction data for future purchase prediction.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: The paper provides a rigorous comparative evaluation framework for different machine learning algorithms on an e-commerce dataset.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: The evaluation metrics (accuracy, F1, AUC, efficiency) and cross-validation methodology are directly applicable to testing budget recommendation modules in Odin.
  contribution: The paper's comparative analysis of ML algorithms provides a benchmark for Odin's spending forecasting module, suggesting XGBoost as a high-accuracy option. The feature importance analysis validates RFM as a core framework for behavior prediction in personal finance. The evaluation methodology establishes a template for testing Odin's algorithmic modules, including efficiency metrics crucial for mobile-first applications. The study's approach to handling customer transaction data informs how Odin can structure and process user spending history for predictive tasks.
  directly_justifies:
    - "XGBoost achieves the highest predictive accuracy for future purchase behavior among tested algorithms."
    - "Recency of customer activity is the strongest predictor of future behavior."
    - "Ensemble methods (XGBoost, Random Forest) outperform linear models in predicting purchase intent."
    - "Evaluation of algorithms must consider both accuracy and computational efficiency for practical deployment."
  limits:
    - "The analysis is conducted on e-commerce transaction data, not personal finance spending data."
    - "The paper focuses on predicting purchase intent, not directly on budgeting or anomaly detection."
    - "The dataset is international and not specific to Filipino young professionals. [unacknowledged]"
    - "The study does not consider interpretability trade-offs in depth beyond feature importance. [unacknowledged]"
  mapping_rationale: This paper was systematically scanned against all 12 functional domains. The core contribution is an algorithmic comparison for predictive modeling, making it highly relevant to the Spending Forecasting domain (Topics 6.A, 6.B) and System Evaluation (Topics 12.B, 12.C). It also provides medium relevance to Behavioral Profiling & Classification (Topics 5.B, 5.C) through its classification approach and feature engineering. Domains like Filipino Cultural Context, Expense Categorization, and Mobile-First Design were rejected as the study does not address cultural factors, budget categories, or mobile-specific design considerations. The user retention domain was considered but rejected as the paper does not discuss engagement dynamics or retention mechanisms. The overall relevance is moderate, primarily contributing to forecasting and evaluation methodologies for Odin.
limitations:
  - The study uses e-commerce transaction data, which may not fully represent personal financial management scenarios.
  - The paper does not address real-time prediction latency or deployment constraints for mobile applications. [unacknowledged]
  - Generalizability to the Filipino context or young professional demographics is not established. [unacknowledged]
remember_this:
  - XGBoost achieves the best F1 score (0.680) for predicting purchase behavior.
  - Recency is the single most important predictor of future customer activity.
  - Logistic regression offers the fastest processing but the lowest predictive accuracy.
  - Feature engineering with domain knowledge (RFM) is as critical as model selection.
  - Ensemble methods like XGBoost provide a superior balance of accuracy and efficiency.
```