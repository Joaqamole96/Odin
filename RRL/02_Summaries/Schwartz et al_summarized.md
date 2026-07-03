```yaml
paper_id: 10.48550/arXiv.2509.11389
designation: international
title: Enhancing ML Interpretability for Credit Scoring
authors: Schwartz, S.; Wang, Q.; Fang, F.
year: 2024
venue: Unknown
odin_topics:
  - 4.B
  - 5.B
  - 5.C
  - 6.B
  - 7.A
  - 7.B
  - 7.D
  - 8.A
  - 8.B
  - 12.B
tldr: A hybrid framework uses SHAP to select top features from a black-box XGBoost model, then trains a glass-box EBM model with 10 features, achieving comparable performance with an 88.5% feature reduction.
problem_and_motivation: Black-box machine learning models for credit scoring are accurate but lack transparency, limiting their use in regulated environments. Post-hoc explanation methods do not inherently produce lightweight or fully transparent models. There is a need for an approach that maintains predictive power while creating models that are inherently interpretable and meet regulatory expectations.
approach:
  - A high-performing XGBoost model is trained on the full feature set to serve as a performance benchmark.
  - SHAP is used to rank features by their importance based on the XGBoost model.
  - A subset of the top-ranked features, specifically 10, is selected to train glass-box models, such as Explainable Boosting Machine (EBM) and Penalized Logistic Tree Regression (PLTR).
  - The resulting glass-box models are refined through feature interaction analysis, correlation analysis, and potential expert input.
  - The approach is evaluated using the Lending Club dataset, comparing the reduced glass-box models against the benchmark and logistic regression.
findings:
  - The approach reduces the number of features from 86 to 10, an 88.5% reduction.
  - The reduced EBM model achieves performance comparable to the full-feature XGBoost benchmark.
  - num: The maximum improvement from including all nine pairwise interactions in EBM was 0.4% on the F1 score.
  - The SHAP top feature list is largely consistent across LR, XGBoost, and EBM models.
  - XGBoost provided the fastest computation of feature importance among the models compared, making it a practical choice for feature selection.
  - Correlation analysis can be used to refine the feature set and slightly improve performance.
key_figures_tables:
  - Figure 1: Loan amount and annual income feature interaction → Counterintuitive patterns can arise from feature interactions.
  - Figure 2: Loan amount attribution → Higher loan amounts are associated with a higher probability of default.
  - Figure 3: Annual income attribution → Higher annual incomes correspond to a lower probability of default.
  - Figure 4: Performance w.r.t. the number of (top) features → Adding more than 10 features yields no substantial performance improvement.
  - Table 1: Performance of base models → Base models show similar performance on AUPRC, AUROC, and F1.
  - Table 2: Top features in different models → Top features are largely consistent across LR, XGBoost, and EBM.
  - Table 3: Performance comparison after correlation analysis → Removing correlated lower-ranked features can improve performance.
key_equations:
  - equation: p = 1 / (1 + e^{-(β_0 + β_1 x_1 + ... + β_d x_d)})
    explanation: Logistic regression predicts probability using a linear combination of features.
  - equation: y_i = Σ_{k=1}^{K} f_k(x_i)
    explanation: XGBoost prediction is the sum of outputs from K decision trees.
  - equation: g(E[Y]) = β_0 + Σ_{j=1}^{d} f_j(x_j) + Σ_{1≤j<q≤d} f_{j,q}(x_j, x_q)
    explanation: EBM can model pairwise feature interactions within an additive framework.
definitions:
  - term: XAI
    definition: Explainable Artificial Intelligence; methods to make AI model decisions understandable to humans.
  - term: SHAP
    definition: SHapley Additive exPlanations; a game-theoretic approach to explain model predictions by assigning feature importance.
  - term: XGBoost
    definition: eXtreme Gradient Boosting; an optimized and scalable gradient boosting algorithm.
  - term: EBM
    definition: Explainable Boosting Machine; an interpretable glass-box model based on generalized additive models.
  - term: PLTR
    definition: Penalized Logistic Tree Regression; a hybrid model using decision tree-derived features in a penalized logistic regression.
critical_citations:
  - "[Lundberg & Lee, 2017] — Defines SHAP for additive feature attribution."
  - "[Chen & Guestrin, 2016] — Introduces the XGBoost algorithm used as benchmark."
  - "[Nori et al., 2019] — Presents the EBM glass-box model used in the approach."
relevance:
  topics:
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: The paper directly addresses the lack of transparency in black-box ML models for credit scoring, a key gap the paper aims to solve.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: The feature selection process could be analogous to cold-start issues by identifying essential features when data is limited.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: The models discussed (XGBoost, EBM) are classification approaches that could be adapted for financial behavioral profiling.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: While XGBoost is used for classification, its principles are relevant to forecasting, though the paper focuses on credit default, not sequential spending.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: The use of SHAP and correlation analysis reflects using domain knowledge to refine model feature sets, analogous to refining budget allocation strategies.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: contextual
      justification: The paper does not focus on recommendation but provides a methodology for selecting key features, which is a foundational step for recommendation systems.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: medium
      justification: The paper's approach to reducing features from 86 to 10 demonstrates a method for simplifying complex models, akin to reducing complexity in allocation problems.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: The paper discusses detecting default, a type of anomaly, but its core contribution is on model interpretability rather than anomaly detection methods.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: The algorithms used are for classification, not specifically for anomaly detection in spending data.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: The paper extensively evaluates the performance of different models (XGBoost, EBM, PLTR) using metrics like AUPRC, AUROC, and F1, which is central to evaluating algorithmic modules.
  contribution: The paper provides a concrete methodology for building transparent, lightweight ML models by using post-hoc explanation tools for feature selection. This methodology can be directly applied to Odin's budgeting and forecasting modules to ensure the core algorithms are both accurate and interpretable. The framework's emphasis on reducing feature complexity without losing performance is directly relevant to Odin's goal of providing clear, actionable financial insights. The paper demonstrates that high-performing models can be simplified, which is crucial for building user trust and meeting regulatory standards.
  directly_justifies:
    - Using SHAP for feature importance enables selection of a concise, high-impact feature set.
    - EBM can achieve performance comparable to XGBoost while being significantly more interpretable.
    - Reducing model complexity to about 10 features can maintain predictive power while enhancing transparency.
  limits:
    - The study is conducted on a single dataset (Lending Club), limiting generalizability.
    - The approach was not tested across diverse datasets to validate its robustness.
    - The focus is on binary classification (default vs. non-default), not on other financial applications like spending forecasting.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes identified the most relevant ones. The paper's core contribution on enhancing ML interpretability and reducing feature complexity maps most directly to "Existing Systems & Gaps" (4.B) and "System Evaluation" (12.B) with high relevance. Topics related to "Budget Recommendation" (7.A, 7.B, 7.D) and "Behavioral Profiling" (5.B, 5.C) were assigned medium relevance because the methodology for feature selection and model simplification is foundational to those areas, even though the paper's domain is credit scoring. The paper's discussion of default prediction touches on "Anomaly Detection" (8.A, 8.B), but its primary focus on explainability over detection algorithms makes the relevance low. Topics concerning "Filipino Cultural Context" (2), "Mobile-First Design" (9), "Data Privacy" (10), "User Retention" (11), and "Savings & Debt Management" (13) were considered and rejected as the paper provides no specific insights on these aspects of personal finance management. Overall, the paper offers a highly relevant methodology for building transparent and efficient algorithmic modules within Odin.
limitations:
  - "The proposed approach was only evaluated on a single dataset from Lending Club, which may not represent all credit or financial behaviors. [unacknowledged]"
  - "The study did not extensively optimize the base black-box model, which could affect the generalizability of the feature rankings. [unacknowledged]"
  - "The paper acknowledges that SHAP has limitations in handling correlated features, but the proposed mitigation through correlation analysis may not fully resolve this issue."
remember_this:
  - SHAP-guided feature selection can reduce features by 88.5% without significant performance loss.
  - EBM provides a strong balance between explainability and predictive performance.
  - Correlation analysis can refine feature sets and slightly improve model performance.
  - A hybrid approach using post-hoc explanations to build glass-box models enhances transparency.
```