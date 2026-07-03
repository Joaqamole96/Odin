```yaml
paper_id: 10.1038/s41598-026-51764-9
designation: international-algorithm-specific
title: Transforming credit risk evaluation in digital lending from black box models to transparent decisions
authors: Mohammad, A.A.S.; Mohammad, S.I.; Vasudevan, A.; Azam, S.M.F.; Sevukamoorthy, L.; Parhi, M.; Shankalia, M.U.; Salami, Z.A.
year: 2026
venue: Scientific Reports
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
  - 12.C
tldr: A hybrid framework integrating gradient boosting models with metaheuristic optimization improves credit risk prediction accuracy and interpretability for digital lending.
problem_and_motivation: Traditional credit scoring models fail to assess non-traditional borrowers, while existing machine learning approaches often lack interpretability, limiting trust and regulatory compliance. A unified framework is needed to jointly optimize predictive performance and transparency.
approach:
  - A publicly available dataset of 1,000 loan applications with 16 attributes was used.
  - LightGBM, CatBoost, and Explainable Boosting Machine were selected as base models.
  - Brown-Bear Optimization Algorithm and Puma Optimizer were used for hyperparameter tuning.
  - Class imbalance was addressed using cost-sensitive learning with class weights.
  - Feature importance was analyzed using SHAP and permutation-based methods.
findings:
  - num: Optimized CatBoost achieved 99.50% test accuracy and 0.9951 F1-score.
  - num: Optimized LightGBM achieved 99.01% test accuracy and 0.9901 F1-score.
  - num: Optimized EBM achieved 98.51% test accuracy and 0.9852 F1-score.
  - Metaheuristic optimization consistently improved performance over baseline models.
  - SHAP analysis identified credit history age as the most influential predictor.
  - The framework balances predictive accuracy with feature-level interpretability.
key_figures_tables:
  - Table 4: K-fold cross-validation results → Models show stable performance across folds.
  - Table 6: Performance metrics for baseline and optimized models → Optimization significantly improves all metrics.
  - Table 7: Confusion matrices → Optimized models reduce false positives and negatives substantially.
  - Figure 6: SHAP values → Credit history age is the most influential feature in risk prediction.
key_equations:
  - equation: "Accuracy = (TP + TN) / (TP + TN + FP + FN)"
    explanation: "Proportion of correctly classified instances."
  - equation: "Precision = TP / (TP + FP)"
    explanation: "Proportion of true positives among predicted positives."
  - equation: "Recall = TP / (TP + FN)"
    explanation: "Proportion of actual positives correctly identified."
  - equation: "F1 = 2 * (Precision * Recall) / (Precision + Recall)"
    explanation: "Harmonic mean of precision and recall."
definitions:
  - term: BNPL
    definition: "Buy Now, Pay Later; a short-term financing model."
  - term: LightGBM
    definition: "A gradient boosting framework using histogram-based splitting."
  - term: CatBoost
    definition: "A gradient boosting algorithm with native categorical feature handling."
  - term: EBM
    definition: "Explainable Boosting Machine; a transparent, GAM-based model."
  - term: BBOA
    definition: "Brown-Bear Optimization Algorithm; a nature-inspired metaheuristic."
  - term: PO
    definition: "Puma Optimizer; a metaheuristic inspired by puma hunting behavior."
  - term: SHAP
    definition: "SHapley Additive exPlanations; a method for explaining model predictions."
critical_citations:
  - "[Roy and Vasa, 2025] — Reviews AI methods for credit risk assessment."
  - "[Zhou and Wang, 2025] — Uses XGBoost with SHAP for interpretable credit risk."
  - "[Papa and Ricafort, 2024] — Demonstrates ANN/RNN for cooperative lending."
  - "[De Silva, 2025] — Achieves 99% accuracy with human-in-the-loop models."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly models borrower characteristics and default risk.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: medium
      justification: Addresses non-traditional borrowers with limited credit history.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Uses boosting and optimization for borrower classification.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Develops a predictive framework for credit risk.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: Provides a general methodology applicable to spending data.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: Credit risk assessment informs budgeting decisions.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Not directly about budget recommendations but can inform credit limits.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Default prediction is a form of anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Uses classification algorithms applicable to anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Employs robust cross-validation and multiple metrics.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Evaluates individual models and optimization effects.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: low
      justification: Focuses on credit risk, but uses similar evaluation metrics.
  contribution: "This paper provides a framework for integrating explainable boosting models with metaheuristic optimization for credit risk assessment. The approach can inform Odin's behavioral profiling module by demonstrating how to classify borrowers using financial and demographic features. The use of SHAP for interpretability aligns with Odin's need for transparent decision-making in financial profiling. The methodology also offers a template for evaluating prediction models using cross-validation and imbalance-aware metrics."
  directly_justifies:
    - "Gradient boosting models achieve high accuracy on tabular financial data."
    - "Metaheuristic optimization improves hyperparameter tuning over grid search."
    - "SHAP analysis identifies key features influencing default risk."
    - "EBM provides feature-level transparency suitable for regulated environments."
    - "Class imbalance can be addressed via cost-sensitive learning without synthetic data."
  limits:
    - "Dataset is not from a BNPL platform, limiting direct applicability."
    - "Results are based on a single, relatively small dataset (n=1000)."
    - "Real-world operational validation was not conducted."
    - "Comparison with other metaheuristics or deep learning models is limited [unacknowledged]."
  mapping_rationale: "A systematic scan of all 12 functional domains was conducted to map the paper to Odin's topic codes. The paper's core contribution lies in algorithmic credit risk prediction, directly informing domains such as Behavioral Profiling (5.A, 5.B, 5.C), Predictive Modeling (6.A, 6.B), and Anomaly Detection (8.A, 8.B). The rigorous evaluation framework (12.A, 12.B) was also flagged as highly relevant. The paper was considered for topics in Budget Recommendation (7.A, 7.B) and Savings/Debt Management (13.A, 13.B, 13.C) but received low or contextual relevance because it does not directly address budgeting strategies, savings goals, or debt management practices. Similarly, Mobile-First Design (9.A, 9.B) and Data Privacy (10.A, 10.B) were not relevant. Borderline cases included the connection between credit risk and budget constraints (7.A), which was deemed contextual, and the application of classification algorithms to anomaly detection (8.B), which was considered medium due to shared methodology. Overall, the paper provides high relevance for modules involving predictive modeling, user classification, and system evaluation, but limited direct applicability to budgeting, savings, or engagement features."
limitations:
  - "Limited to a single dataset of 1,000 records, reducing generalizability."
  - "No comparison with other metaheuristic optimization algorithms."
  - "No real-world deployment or user study was conducted."
  - "The trade-off between interpretability and performance is not quantitatively assessed [unacknowledged]."
remember_this:
  - "Optimized CatBoost achieved 99.5% accuracy on credit risk prediction."
  - "Metaheuristic optimization significantly outperforms baseline tuning methods."
  - "EBM provides transparent feature contributions for regulatory compliance."
  - "Credit history age is the most influential predictor of default risk."
  - "Hybrid frameworks can balance accuracy and interpretability in finance."
```