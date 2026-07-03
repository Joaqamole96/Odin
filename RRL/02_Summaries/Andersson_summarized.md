```yaml
paper_id: 10.1556/2006.2025.00013
designation: international-algorithm-specific
title: Insights into the temporal dynamics of identifying problem gambling on an online casino: A machine learning study on routinely collected individual account data
authors: Andersson, S.; Carlbring, P.; Lyon, K.; Bermell, M.; Lindner, P.
year: 2025
venue: Journal of Behavioral Addictions
odin_topics:
  - 5.B
  - 5.C
  - 8.B
  - 10.A
  - 10.B
tldr: Machine learning on online gambling account data enables stable and early classification of players into low-risk and higher-risk categories, supporting real-time intervention.
problem_and_motivation: Identifying problem gamblers is crucial for public health, but existing methods like self-report and cross-sectional behavioral tracking suffer from validity issues and fail to capture temporal dynamics. A robust, scalable, and temporally stable method for early identification is needed to enable timely interventions.
approach:
  - Analyzed a 4.5-year dataset from a Swedish online gambling provider covering 35,048 players with detailed behavioral and transactional data.
  - Extensive feature engineering captured gambling behavior dynamics such as loss chasing, betting frequency, session length, and spending patterns.
  - Trained an XGBoost classifier to distinguish low-risk from higher-risk players, using a binary label derived from manual risk assessments.
  - Evaluated temporal stability by truncating training data at 30, 60, and 90 days before the maximum timestamp and comparing holdout performance.
  - Used SHAP values for feature importance and a nested forward-chaining cross-validation strategy to avoid data leakage.
findings:
  - num: Precision decreased slightly with data truncation, with a 95% CI entirely below zero [(−0.005, −0.001)].
  - num: F1 score remained stable across truncations, with a 95% CI for its linear slope including zero [(−0.008, 0.035)].
  - Loss chasing behavior, net balance trend, max deposit, session sum, and total bets daily were the most influential features across all truncation periods.
  - The model consistently underestimated risk for the low-risk category, with the largest gap (0.337) in the full dataset.
  - The model performed well for medium- and high-risk categories, with predicted means closely matching true means.
key_figures_tables:
  - "Figure 2: SHAP summary plot of top features → Loss chasing and net balance trend are most influential."
  - "Figure 3: Temporal evaluation of prediction stability → Performance metrics remained stable across data truncations."
  - "Table 1: Model performance metrics for different truncation labels → Metrics like F1 and ROC AUC were consistent."
  - "Table 2: Risk category prediction table with difference → Model underestimates low-risk but performs well for high-risk."
  - "Figure 4: Difference between true and predicted means → Prediction gap is largest for low-risk and smallest for high-risk."
key_equations:
  - equation: None.
    explanation: No explicit equations are presented in the paper.
definitions:
  - term: SHAP
    definition: SHapley Additive exPlanations, a method to explain individual predictions by attributing contributions to each feature.
  - term: XGBoost
    definition: eXtreme Gradient Boosting, a scalable and efficient machine learning algorithm for classification and regression.
  - term: GMLVQ
    definition: Generalized Matrix Learning Vector Quantization, a supervised learning technique for discriminative feature relevance.
critical_citations:
  - "[Auer & Griffiths, 2022] — Demonstrates machine learning for predicting limit-setting behavior."
  - "[Perrot et al., 2022] — Develops a prediction model for online gambling problems using account data."
  - "[Braverman & Shaffer, 2012] — Identifies behavioral markers for high-risk internet gambling."
relevance:
  topics:
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: Evaluates temporal stability of risk classification, relevant to dynamic profile updating.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Directly applies XGBoost classification to behavioral data for risk profiling.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Loss-chasing and spending patterns are used as key features for anomaly/risk detection.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Context of responsible gambling and duty of care, but not focused on PFMS data privacy.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: contextual
      justification: Discusses timely interventions and duty of care, which relate to user trust.
  contribution: This paper demonstrates the feasibility of using machine learning for early and stable classification of at-risk individuals based on behavioral data, a concept directly transferable to Odin's anomaly detection module. The focus on temporal stability using truncated training data provides a methodology for evaluating and implementing dynamic behavioral profiling in a PFMS. The identification of key predictive features like spending trends and loss-chasing behavior offers concrete signals for Odin's spending forecasting and anomaly detection systems. Furthermore, the study's emphasis on real-world deployment and regulatory compliance aligns with Odin's need for a reliable and trusted system.
  directly_justifies:
    - "Machine learning can reliably classify behavioral risk profiles with stable performance over time."
    - "Features like loss chasing and spending trends are key predictors of problematic financial behavior."
    - "Predictive models can be effectively trained on historical data to enable early intervention."
    - "Temporal stability of predictions supports their use in real-time monitoring systems."
  limits:
    - "Dataset comes from a single gambling operator, limiting generalizability due to lack of a 'single customer view'."
    - "Risk labels used for training may have temporal biases and inconsistencies due to manual assessment."
    - "The truncation strategy may bias the model toward accounts with more extensive activity histories."
    - "Bootstrapping analysis for temporal trends was limited by a small sample size (four data points per metric)."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper's focus on machine learning for risk classification and temporal stability directly maps to the Behavioral Profiling & Classification (5) and Anomaly Detection (8) domains. Specifically, the paper was assigned `high` relevance to 5.C (Classification Approaches) and 8.B (Anomaly Detection Algorithms) due to its direct application of XGBoost for binary risk classification and its use of behavioral features like loss-chasing. A `medium` relevance was assigned to 5.B (Profile Dynamics) as the temporal stability analysis is relevant to how profiles change and are updated. Domains related to User Trust and Data Privacy (10) were considered but assigned `contextual` relevance, as the paper discusses duty of care and intervention in a gambling context, which is analogous to trust in PFMS but not a direct focus. Domains like Expense Categorization (3), Budget Recommendation (7), and Savings & Debt Management (13) were rejected as the paper does not address these specific personal finance functions. Overall, the paper provides strong evidence for the algorithmic core of Odin's risk and anomaly detection capabilities.
limitations:
  - "Temporal biases in risk labels may lead the model to capture historical patterns rather than genuine risk. [unacknowledged]"
  - "The analysis is limited to a single operator, lacking data on cross-operator gambling activity. [acknowledged]"
  - "The truncation strategy may inadvertently bias the model toward accounts with longer activity histories. [acknowledged]"
  - "The low-risk category was consistently underestimated, indicating a potential weakness in distinguishing low from moderate risk."
remember_this:
  - "Machine learning models can classify risk profiles with stable performance over time."
  - "Loss chasing and spending trends are the most predictive features for risk classification."
  - "Precision decreased slightly with less historical data, but overall metrics remained stable."
  - "The model effectively identifies high-risk individuals but struggles with low-risk classification."
  - "Temporal stability of predictions supports real-time monitoring and early intervention."
```