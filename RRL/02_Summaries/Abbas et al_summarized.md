```yaml
paper_id: 10.1007/s42979-025-04214-8
designation: international-algorithm-specific
title: Machine Learning-Based Analysis of Technology Acceptance in FinTech: A Behavioral Study Using Digital Wallet Data
authors: Abbas, S. K.; Hussain, M.; Rimal, Y. N.
year: 2025
venue: SN Computer Science
odin_topics:
  - 5.C
  - 11.A
  - 12.A
  - 12.B
tldr: Machine learning models using transactional data show limited predictive power for classifying high-engagement FinTech users due to class imbalance and overlapping behavioral patterns.
problem_and_motivation: Existing technology acceptance models rely on surveys and intention-based indicators, which may not capture real-world engagement and are susceptible to bias. There is limited empirical evidence on how actual behavioral data maps onto technology acceptance in FinTech.
approach:
  - Used a Kaggle dataset of 7000 digital wallet users with 20 demographic, transactional, and behavioral features.
  - Operationalized technology acceptance as daily app usage, creating a binary classification target.
  - Applied Logistic Regression, SVM, Random Forest, and XGBoost classifiers.
  - Addressed class imbalance (33.5% high-acceptance) using SMOTE during training.
  - Evaluated models using accuracy, ROC AUC, precision, recall, F1-score, and SHAP for feature importance.
findings:
  - All models achieved ~66.5% accuracy, but ROC AUC scores were modest (XGBoost highest at 0.519).
  - Linear classifiers (Logistic Regression, SVM) failed to identify any high-acceptance users (precision and recall = 0).
  - XGBoost achieved the best F1-score for the high-acceptance class at 0.22, improving to 0.36 with SMOTE.
  - num: SMOTE increased XGBoost's recall for high-acceptance users from 0.16 to 0.27.
  - Customer Lifetime Value (LTV), Satisfaction Score, and Issue Resolution Time were the most influential features.
  - PCA showed first three components captured only 35.6% of variance, with no clear separation between classes.
  - Predicted probabilities for both classes showed significant overlap, indicating model uncertainty.
key_figures_tables:
  - Figure 1: Precision-Recall and ROC curves → XGBoost slightly outperformed others but remained near random.
  - Figure 2: PCA 3D projection and loadings → LTV, Total Spent, and Satisfaction Score dominate PC1.
  - Figure 3: Feature importance and calibration curves → Satisfaction and LTV are top predictors; models are poorly calibrated.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: TAM
    definition: Technology Acceptance Model; posits perceived usefulness and ease of use influence adoption.
  - term: UTAUT
    definition: Unified Theory of Acceptance and Use of Technology; extends TAM with social influence and facilitating conditions.
  - term: LTV
    definition: Customer Lifetime Value; a metric representing the total revenue a customer is expected to generate.
critical_citations:
  - "[Zhang et al., 2021] — Found perceived competence and benevolence of algorithms impact robo-advisor adoption."
  - "[Davis, 1989] — Introduced TAM, the foundational model for technology acceptance."
relevance:
  topics:
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Applies ML classifiers (RF, XGBoost) to classify user engagement levels based on behavioral data.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: Directly models user engagement (daily app usage) as the target variable for technology acceptance.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides a comparative evaluation of ML models for behavioral prediction, relevant to system assessment.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Evaluates algorithm performance using metrics like precision, recall, and F1-score in an imbalanced setting.
  contribution: The paper demonstrates that machine learning can be applied to behavioral data to predict user engagement, which is relevant to Odin's profiling and engagement modules. It shows that ensemble methods like XGBoost outperform linear models, suggesting their use for user classification tasks. The identification of LTV and satisfaction as key predictors highlights the importance of user value and experience metrics for Odin's personalization. The study's findings on the limitations of static features inform Odin's need for temporal and psychographic data. The methodological framework offers a template for evaluating Odin's own classification modules.
  directly_justifies:
    - "XGBoost outperformed linear classifiers for imbalanced user engagement classification."
    - "Customer satisfaction and lifetime value are strong behavioral predictors of engagement."
    - "Static transactional data alone is insufficient for robust user acceptance prediction."
  limits:
    - "The dataset is from a single non-Philippine platform, limiting generalizability to Filipino users."
    - "Technology acceptance is operationalized only as daily usage, omitting cognitive and affective components."
    - "The study uses cross-sectional data, lacking temporal dynamics of user behavior."
    - "Psychographic variables like financial literacy and trust are absent from the model."
  mapping_rationale: A systematic scan of all 12 functional domains and their topic codes was conducted. The paper was flagged as relevant to the "Behavioral Profiling & Classification" (5.C) domain due to its application of ML classifiers to user data. It also strongly informs "User Retention & Engagement" (11.A) by directly modeling daily app usage as a proxy for acceptance. The evaluation methodology (12.A, 12.B) is relevant as a comparative benchmark. Domains like Filipino Cultural Context (2), Expense Categorization (3), Existing Systems (4), Forecasting (6), Budgeting (7), Anomaly Detection (8), Mobile Design (9), Privacy (10), and Savings/Debt (13) were rejected because the paper does not address these topics. The paper's overall relevance to Odin is medium; it provides methodological insights for user profiling and engagement prediction but lacks direct applicability to PFMS-specific functions.
limitations:
  - "Single, cross-sectional dataset limits generalizability. [unacknowledged]"
  - "Behavioral proxy (daily usage) may not capture full technology acceptance. [acknowledged]"
  - "Use of only static features misses temporal behavioral patterns. [acknowledged]"
  - "Lack of psychographic variables constrains interpretability. [acknowledged]"
  - "Class imbalance and overlapping behaviors constrain predictive performance despite SMOTE. [acknowledged]"
remember_this:
  - "XGBoost outperformed linear models for imbalanced user engagement classification."
  - "SMOTE improved XGBoost recall for high-engagement users from 0.16 to 0.27."
  - "Customer satisfaction and lifetime value are the strongest behavioral predictors."
  - "Static transactional data alone provides only weak signals of technology acceptance."
  - "Predicting user engagement from behavioral data remains a challenging task."
```