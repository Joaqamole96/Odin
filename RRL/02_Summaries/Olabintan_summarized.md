```yaml
paper_id: 10.2139/ssrn.6837665
designation: local-algorithm-specific
title: FairLend-Africa: An Explainable Machine Learning Framework for Alternative Credit Scoring Using Behavioral Financial Data in Financially Excluded African Communities
authors: Olabintan, I.
year: 2026
venue: SSRN
odin_topics:
  - 1.A
  - 1.C
  - 2.B
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 7.B
  - 7.C
  - 8.A
  - 8.B
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
  - 12.C
tldr: An explainable ML framework for alternative credit scoring using mobile money behavioral data, achieving ROC-AUC of 0.714 on synthetic data with SHAP explanations and fairness auditing.
problem_and_motivation: Billions of adults globally lack formal credit histories, making them invisible to conventional scoring systems. Behavioral financial data from mobile money offers a potential proxy for creditworthiness, but integration into fair and explainable frameworks remains limited.
approach:
  - Synthetic dataset of 10,000 borrower records with 16 raw behavioral features from mobile money and credit history was generated.
  - XGBoost classifier was trained with hyperparameter optimization via RandomizedSearchCV and evaluated against logistic regression.
  - SHAP provided global feature importance and local explanations for individual credit decisions.
  - Systematic fairness audit assessed demographic parity, equal opportunity, and predictive parity across regional and gender subgroups.
  - System was implemented as a REST API with an interactive React dashboard for loan officers.
findings:
  - Tuned XGBoost achieved a held-out test ROC-AUC of 0.714, matching the logistic regression baseline of 0.713.
  - Wallet balance trend and savings consistency were the dominant creditworthiness signals.
  - Fairness audit found no demographic disparities under the synthetic data's independence assumption.
  - num: The optimal classification threshold was 0.151, substantially below the conventional 0.5.
  - Engineered composite features provided no measurable predictive improvement over raw features.
key_figures_tables:
  - Table 1: 16 raw behavioral features with domain and rationale → Features cover mobile money, airtime, savings, credit, social, and payment domains.
  - Table 3: Model comparison test set performance → Tuned XGBoost ROC-AUC 0.714 vs logistic regression 0.713.
  - Table 5: Fairness disparity ratios → All groups exceed 0.80 for selection rate, TPR, and precision.
  - Table 6: Selection rate disparity ratios across thresholds → All ratios exceed 0.80, with West Africa lowest at 0.818.
  - Figure 7: Global feature importance by mean SHAP value → Wallet balance trend dominates by factor of 1.74.
key_equations:
  - equation: f(x_i) = ∅_0 + ∑_{j=1}^p ∅_{ij}
    explanation: SHAP decomposition of prediction into base rate plus feature contributions.
definitions:
  - term: ROC-AUC
    definition: Area under the receiver operating characteristic curve, measuring discrimination ability.
  - term: SHAP
    definition: SHapley Additive exPlanations, a game-theoretic approach for explaining model predictions.
  - term: Demographic parity
    definition: Equal positive prediction rates across demographic groups.
  - term: Equal opportunity
    definition: Equal true positive rates across demographic groups.
  - term: MNAR
    definition: Missing Not At Random, where missingness depends on unobserved values.
critical_citations:
  - "[Björkegren and Grissen, 2018] — Mobile phone metadata predicts loan repayment with AUC ~0.70."
  - "[Suri and Jack, 2016] — Mobile money enables households to navigate income shocks."
  - "[Lundberg and Lee, 2017] — Unified framework for model explanation using SHAP values."
  - "[Chouldechova, 2017] — Impossibility theorem for simultaneously satisfying fairness criteria."
  - "[Baesens et al., 2003] — Ensemble methods outperform single classifiers in credit scoring."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Provides general context on financially excluded populations in Africa, analogous to unbanked Filipinos.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: contextual
      justification: Demonstrates use of behavioral transaction data as a proxy for creditworthiness, relevant to understanding financial behavior.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Mentions temporal dynamics and seasonal patterns as a limitation, not a focus.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Reviews digital credit systems like M-Shwari, Tala, Branch, providing context for PFMS landscape.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly addresses lack of explainability and fairness in existing alternative credit scoring systems.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Framework creates behavioral profiles from mobile money features to predict creditworthiness.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Uses XGBoost and logistic regression to classify borrowers into repayment risk categories.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Core contribution is a predictive model for credit scoring using behavioral data.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: Uses predictive modeling on behavioral features, though not explicitly sequential time-series forecasting.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Framework is for credit scoring, not budget recommendation; methodology could be adapted.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: contextual
      justification: Not directly addressed; threshold tuning relates to cost asymmetry.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Not addressed; focusing on credit classification.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: XGBoost could potentially be used for anomaly detection, but not the focus.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Mentions dashboard for loan officer use, but system is not explicitly mobile-first.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: Dashboard design is for loan officers, not end-user PFMS.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Discusses privacy barriers, data protection acts, and synthetic data for privacy.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Addresses trust through explainability (SHAP) and fairness auditing.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides evaluation protocol including ROC-AUC, fairness metrics, and threshold analysis.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Evaluates XGBoost, logistic regression, and SHAP explainability module.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: contextual
      justification: Evaluation metrics are general ML metrics, not specific to budget recommendation.
  contribution: FairLend-Africa provides a blueprint for Odin's predictive module using behavioral data, demonstrating that XGBoost with SHAP explanations can achieve reasonable predictive performance. The fairness audit framework directly maps to Odin's need for transparent and equitable algorithms, particularly important for a Filipino audience concerned with social justice. The emphasis on explainability supports Odin's design goal of building user trust through interpretable decisions. The open-source implementation and REST API design offer a practical template for Odin's system architecture.
  directly_justifies:
    - "Behavioral financial data from mobile money transactions carries sufficient predictive signal for creditworthiness classification."
    - "XGBoost with SHAP explanations provides a coherent method for predictive modeling and interpretability in personal finance systems."
    - "Systematic fairness auditing using demographic parity and equal opportunity is feasible and necessary for equitable algorithmic systems."
    - "Missing data in financial profiles is informative and requires careful handling (e.g., MNAR with missingness indicators)."
    - "Ablation studies are essential to validate feature engineering contributions."
  limits:
    - "Results are based on synthetic data, not real Filipino behavioral data."
    - "Fairness properties are derived under a synthetic independence assumption that may not hold in real settings."
    - "XGBoost performance matches logistic regression, indicating linear structure in synthetic data; real data may show non-linear benefits."
    - "Engineered composite features provided no measurable lift, questioning their practical value."
    - "SHAP explanations assume feature independence, which may misrepresent contributions when features are correlated."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to Predictive Modeling (6.A, 6.B), Behavioral Profiling (5.A, 5.C), and Evaluation Frameworks (12.A, 12.B) as its core contribution is an ML framework for credit scoring. It also has high relevance to Existing Systems (4.A, 4.B) as it reviews digital credit systems and their limitations, and to Data Privacy (10.A) and User Trust (10.B) as it discusses privacy barriers and uses explainability/fairness. Medium relevance was assigned to Mobile-First Design (9.A) due to the dashboard and Filipino Demographic (1.A, 1.C) due to contextual parallels in financial exclusion. Low or contextual relevance was assigned to Budget Recommendation (7.B, 12.C), Anomaly Detection (8.A, 8.B), and Seasonal Spending (2.B) as the paper does not directly address these topics. Borderline cases included the paper touching on both predictive modeling and fairness, which were both selected as high relevance. The overall relevance is high for Odin's algorithmic and evaluation modules, providing a methodological template.
limitations:
  - "Synthetic dataset not validated on real Filipino mobile money data. [unacknowledged]"
  - "Fairness audit assumes demographic-behavioral independence, which may not hold in real Philippines data."
  - "Engineered features provided no predictive improvement; practical value on real data is unproven."
  - "SHAP explanations assume feature independence, which can misrepresent correlated feature contributions."
  - "System has not been evaluated for temporal stability or concept drift."
  - "Near-identical XGBoost and logistic regression performance suggests primarily linear structure in data; non-linear benefits need real data validation."
remember_this:
  - "Behavioral data achieves 0.714 AUC for credit scoring, matching logistic regression on synthetic data."
  - "Wallet balance trend and savings consistency are the strongest creditworthiness signals."
  - "Fairness audit found no disparities, but this is contingent on synthetic data independence."
  - "SHAP explanations provide interpretability but assume feature independence, a known limitation."
  - "Feature ablation showed engineered features provided no measurable lift in predictive performance."
```