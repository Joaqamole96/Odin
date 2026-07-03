```yaml
paper_id: 10.1177/18724981241289751
designation: international-algorithm-specific
title: Explainable AI - enhanced ensemble learning for financial fraud detection in mobile money transactions
authors: Vijayanand, D.; Smrithy, G.S.
year: 2025
venue: Intelligent Decision Technologies
odin_topics:
  - 4.B
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 12.B
tldr: Integrates ensemble machine learning with SHAP-based explainable AI to detect financial fraud in mobile money transactions, achieving 99.904% accuracy on a synthetic PaySim dataset.
problem_and_motivation: Financial fraud in digital banking is a growing threat, with global fraud losses reaching 5% of annual income. Existing machine learning models for fraud detection operate as black boxes, undermining trust and creating regulatory challenges. There is a need for systems that combine high accuracy with interpretability to foster transparency and accountability.
approach:
  - Uses PaySim simulator to generate 6,362,620 synthetic mobile money transaction records covering multiple transaction types.
  - Evaluates six classifiers: Logistic Regression, Decision Tree, Random Forest, XGBoost, LightGBM, and Neural Network.
  - Implements an ensemble Voting Classifier combining the six base models with soft voting to improve predictive performance.
  - Employs SHAP (SHapley Additive exPlanations) to provide global and local interpretability of model predictions.
  - Uses stratified 5-fold cross-validation and Friedman's statistical test with Nemenyi post-hoc for robust model comparison.
findings:
  - num: The ensemble learning model achieved 99.904% accuracy, 0.814 F1 score, and 0.990 ROC AUC score.
  - num: The Decision Tree model achieved the highest individual accuracy at 99.937% with an F1 score of 0.893.
  - num: Cash Out transactions comprised 81% of transaction types, while Transfer transactions comprised 19%.
  - num: OldBalanceOrg had the highest mean SHAP value of 0.065, indicating the strongest impact on model output.
  - num: The dataset contained 6,354,407 valid transactions (99.87%) and 8,213 fraudulent transactions (0.13%).
  - num: Fraudulent transactions were only found in the Transfer type, with flagged transactions totaling 16 all marked as TRANSFER.
key_figures_tables:
  - Figure 1: Architecture of proposed methodology → High-level system design for fraud detection with XAI integration.
  - Figure 2: Pie chart of transaction types → Cash Out (81%) and Transfer (19%) dominate transaction categories.
  - Figure 3: Total amount per transaction type → Transfer transactions have higher total monetary value than Cash Out.
  - Figure 4: Fraudulent transaction types by category → Transfer transactions show higher fraud frequency than Cash Out.
  - Figure 5: Proposed ensemble model → Voting Classifier combining XGBoost, LightGBM, Neural Network, Decision Tree, and Random Forest.
  - Figure 6: Process of Explainable AI → XAI pipeline from input data through model prediction to explanation interface.
  - Figure 7: Mean SHAP value bar chart → OldBalanceOrg has the highest average impact (0.065) on model output.
  - Figure 8: SHAP value and feature value scatter plot → Visualizes relationship between feature values and their SHAP impacts.
  - Table 1: Comparative analysis of research works → Summary of prior ML and DL studies on financial fraud detection.
  - Table 2: Dataset attributes → Description of 11 features including step, type, amount, and balance fields.
  - Table 3: Cross-validation results on accuracy → Accuracy per fold for all six base models.
  - Table 4: Cross-validation results on F1 scores → F1 per fold for all six base models.
  - Table 5: Cross-validation results on ROC AUC scores → ROC AUC per fold for all six base models.
  - Table 6: Performance metrics of classification models → Summary table of accuracy, F1, and ROC AUC for each model.
  - Table 7: Nemenyi Post-Hoc Test Results → Pairwise comparison p-values indicating statistically significant performance differences.
  - Table 8: Cross-validation results of ensemble learning classifier → Accuracy, F1, and ROC AUC across 5 folds.
  - Table 9: Performance measure of ensemble learning classifier → Final metrics: 99.904% accuracy, 0.814 F1, 0.990 ROC AUC.
  - Table 10: Average impact of attributes on model output → Mean SHAP values for key features.
key_equations:
  - equation: S(x) = 1 ÷ (1 + e^(-x))
    explanation: Sigmoid function used by logistic regression for probability estimation.
definitions:
  - term: SHAP
    definition: SHapley Additive exPlanations, a game-theoretic approach to explain model predictions by attributing feature importance.
  - term: XAI
    definition: Explainable Artificial Intelligence, AI systems designed to be transparent and interpretable to users.
  - term: Ensemble Learning
    definition: Combining multiple machine learning models to improve predictive performance beyond any single model.
  - term: PaySim
    definition: A financial mobile money simulator that generates synthetic transaction data for fraud detection research.
  - term: Voting Classifier
    definition: An ensemble method that combines predictions from multiple classifiers using majority or soft voting.
  - term: LightGBM
    definition: A gradient boosting framework using tree-based learning with histogram-based methods for efficient training.
critical_citations:
  - "[Hall & Gill, 2019] — Foundational work on machine learning interpretability and transparency."
  - "[Lopez-Rojas et al., 2016] — Introduced the PaySim dataset used in this study."
  - "[Ali et al., 2022] — Systematic literature review of ML techniques for financial fraud detection."
  - "[Awosika et al., 2023] — Combined XAI and federated learning for transparent fraud detection."
  - "[Al-Hashedi & Magalingam, 2021] — Comprehensive review of data mining for financial fraud from 2009-2019."
relevance:
  topics:
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies lack of interpretability in black-box fraud detection models as a critical gap.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly addresses anomaly detection for fraudulent transactions in financial systems.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Uses ensemble learning and XAI to detect fraud patterns in transaction data.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Fraud detection protects financial security, though privacy is not the primary focus.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: XAI via SHAP enhances transparency, which fosters user trust in financial systems.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Provides rigorous cross-validation and statistical testing of ML models for fraud detection.
  contribution: The paper's ensemble learning approach with SHAP explainability directly informs Odin's anomaly detection module (Topic 8.A) by providing a high-accuracy fraud detection framework with interpretable outputs. The Voting Classifier methodology offers a template for combining multiple anomaly detection algorithms to improve robustness in Odin's spending pattern analysis. The SHAP-based feature importance analysis provides a precedent for making Odin's anomaly alerts transparent to users, supporting the trust-building goal in Topic 10.B. The cross-validation and statistical testing framework offers a rigorous evaluation methodology for Odin's algorithmic modules in Topic 12.B.
  directly_justifies:
    - Ensemble learning achieves 99.904% accuracy for fraud detection on mobile money transaction data.
    - SHAP analysis reveals OldBalanceOrg as the most influential attribute for detecting fraudulent transactions.
    - Interpretability through XAI is essential for regulatory compliance and user trust in financial systems.
    - Decision Tree models achieve higher individual F1 scores than ensemble methods on imbalanced fraud data.
  limits:
    - Uses synthetic PaySim data, which may not fully represent real-world fraud patterns.
    - Dataset is highly imbalanced (0.13% fraud), potentially overestimating model performance on balanced data. [unacknowledged]
    - Limited to mobile money transactions; applicability to broader personal finance contexts is unclear. [unacknowledged]
  mapping_rationale: I systematically scanned all 12 functional domains and their associated topic codes from the Canonical Odin Topic List. Domains flagged as relevant include Anomaly Detection (8.A and 8.B with high relevance), Existing Systems & Gaps (4.B with medium relevance), Data Privacy & User Trust (10.A with medium and 10.B with medium relevance), and System Evaluation (12.B with medium relevance). Borderline cases included Behavioral Profiling (5.A-5.C) — while fraud detection involves behavioral patterns, the paper focuses on transaction-level anomaly detection rather than user profiling, so it was rejected. Mobile-First Design (9.A-9.B) was considered but rejected as the paper does not address mobile UX. Forecasting (6.A-6.B) and Budget Recommendation (7.A-7.D) were rejected as the paper does not address predictive spending or budgeting. Expense Categorization (3.A-3.C) and Filipino Cultural Context (2.A-2.D) were deemed irrelevant. The paper's overall relevance to Odin is strong for its anomaly detection methodology and XAI approach, providing a validated framework for detecting unusual spending patterns with interpretable outputs.
limitations:
  - Uses synthetic PaySim data rather than real financial transaction data, limiting real-world validation.
  - The highly imbalanced dataset (0.13% fraud) may overestimate model performance on balanced real-world data. [unacknowledged]
  - The study does not address cold-start scenarios or model adaptation to new fraud patterns over time. [unacknowledged]
  - Limited discussion of computational cost or deployment constraints for real-time mobile applications. [unacknowledged]
remember_this:
  - Ensemble Voting Classifier achieved 99.904% fraud detection accuracy.
  - SHAP analysis identified OldBalanceOrg as the most influential fraud indicator.
  - Interpretable AI models are essential for user trust and regulatory compliance.
  - PaySim synthetic dataset contained 0.13% fraudulent transactions among 6.36 million records.
  - Decision Tree outperformed individual models with 99.937% accuracy.
```