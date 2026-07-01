```yaml
paper_id: 10.63125/9b316w70
designation: international
title: Advancements in Machine Learning for Customer Retention: A Systematic Literature Review of Predictive Models and Churn Analysis
authors: Mamun, M. N. H.
year: 2025
venue: Journal of Sustainable Development and Policy
odin_topics:
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 8.A
  - 10.A
  - 10.B
  - 12.A
  - 12.B
  - 12.C
tldr: A systematic review of 112 studies finds ensemble and deep learning models consistently outperform traditional classifiers for churn prediction, especially when integrating behavioral and sentiment features.
problem_and_motivation: Customer churn leads to billions in annual revenue loss, yet traditional statistical models cannot capture the nonlinear relationships in modern behavioral data. Organizations need predictive tools that identify at-risk customers for proactive, cost-effective retention interventions in saturated markets.
approach:
  - Conducted a systematic literature review following PRISMA guidelines.
  - Searched six major academic databases for studies on ML-based churn prediction published between 2005 and 2025.
  - Retrieved 1,268 articles, screened to 116 empirical studies for meta-analysis.
  - Coded studies by algorithm type, evaluation metrics, dataset, and industry domain.
  - Used random-effects meta-analysis to pool performance metrics like AUC-ROC and F1-score.
findings:
  - num: Ensemble methods (gradient boosting, random forests) show the highest pooled AUC-ROC and F1-scores across industries.
  - num: Deep learning models (LSTM, CNN) significantly outperform classical algorithms on sequential behavioral data.
  - num: Feature engineering with RFM and engagement features improves model performance more than algorithmic choice alone.
  - num: Models using SMOTE and cost-sensitive learning achieve higher recall in imbalanced churn datasets.
  - num: Deep learning models can reduce false-negative churn predictions by up to 30% relative to static feature models.
  - num: AUC-ROC values for high-performing models consistently exceed 0.80, with F1-scores above 0.70.
  - num: Incorporating sentiment analysis features improves recall by over 8% in some studies.
  - num: Public datasets like IBM Telco Churn provide standardized benchmarks with reported AUC-ROC ranges of 0.75-0.90 for ensemble models.
  - num: CNN-based detectors have shown up to a ten-point gain in AUC-ROC over gradient boosting machines on unstructured log data.
  - Interpretability tools like SHAP and LIME are increasingly adopted to bridge transparency gaps in black-box models.
key_figures_tables:
  - "Figure 1: Theoretical Framework for ML-Based Retention → Shows data sources and ML models driving retention strategies."
  - "Figure 2: ML-Driven Churn Prediction Process → Illustrates the pipeline from data preprocessing to model deployment."
  - "Figure 3: ML-Driven Customer Retention and Churn Prediction → Highlights integration of ML into CRM systems."
  - "Figure 9: Key Metrics and Validation Techniques → Visualizes how AUC-ROC, F1, and lift charts are used to evaluate models."
  - "Figure 15: Pooled Performance Metrics → Compares AUC-ROC and F1-scores across different algorithm classes."
  - "Table: None specified in the text."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Churn
    definition: The cessation or significant reduction of a customer's commercial activity within a predefined observation window.
  - term: Customer Retention
    definition: A firm's capacity to sustain an ongoing commercial relationship with a buyer over time.
  - term: RFM
    definition: Recency, Frequency, Monetary value – a framework for customer segmentation and behavior analysis.
  - term: AUC-ROC
    definition: Area Under the Receiver Operating Characteristic Curve, measuring a model's ability to distinguish between classes.
  - term: SHAP
    definition: SHapley Additive exPlanations, a tool for explaining predictions of machine learning models.
  - term: LIME
    definition: Local Interpretable Model-agnostic Explanations, a technique to explain individual predictions.
  - term: SMOTE
    definition: Synthetic Minority Over-sampling Technique, used to address class imbalance by generating synthetic samples.
  - term: CLV
    definition: Customer Lifetime Value, the total worth of a customer to a business over the entire relationship.
  - term: GBM
    definition: Gradient Boosting Machine, an ensemble learning technique that builds models sequentially to correct errors.
  - term: XAI
    definition: Explainable Artificial Intelligence, a set of tools and techniques to make AI decisions understandable to humans.
critical_citations:
  - "[Jajam et al., 2023] — Demonstrates effectiveness of ensemble deep learning for churn prediction."
  - "[Zhu et al., 2023] — Shows bagging-based ensembles improve performance on imbalanced data."
  - "[Sikri et al., 2024] — Confirms ensemble models enhance customer retention in telecom."
  - "[Boozary et al., 2025] — Compares ensemble models for accurate churn prediction."
  - "[Coussement & De Bock, 2013] — Establishes ensemble learning benefits for customer churn prediction."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: "Reviews ML-based churn models widely used in financial services, contextualizing PFMS analytics."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: "Identifies gaps in traditional models and highlights need for real-time, privacy-preserving ML systems."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: "Directly addresses modeling customer behavior for classification and churn prediction."
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: contextual
      justification: "Mentions concept drift and need for retraining, but does not focus on cold-start scenarios."
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: "Comprehensively reviews supervised, unsupervised, and hybrid classification methods for churn."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: "Core focus on predictive modeling, forecasting churn using historical behavioral data."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: "Reviews LSTM, RNN, and TCN for time-series forecasting, directly applicable to spending data."
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: "Discusses feature engineering (RFM) which is foundational for budget allocation and strategy design."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: "Variational autoencoders are mentioned for anomaly detection, a key technique for early churn warnings."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: "Discusses privacy-preserving techniques (federated learning, differential privacy) for compliance."
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: "Emphasizes interpretability (SHAP, LIME) to build user and managerial trust in AI predictions."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: "Dedicates significant analysis to evaluation metrics (AUC-ROC, F1, lift) and cross-validation strategies."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: "Meta-analytically compares performance of various ML algorithms for churn prediction."
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: "Methods for evaluating classification models (calibration, profit-based metrics) translate to budget rec systems."
  contribution: "This review provides a meta-analytic benchmark for selecting ML models in Odin's Behavioral Profiling module. It directly justifies using ensemble or deep learning models for the Spending Forecasting module's predictive engine. The detailed evaluation framework can be adopted for Odin's System Evaluation module to ensure robust model validation. The analysis of feature engineering (RFM, sentiment) guides the design of Odin's Expense Categorization and User Profile modules."
  directly_justifies:
    - "Ensemble and deep learning models consistently outperform traditional classifiers on behavioral data."
    - "AUC-ROC and F1-score are more reliable metrics than accuracy for imbalanced churn datasets."
    - "Feature engineering with recency, frequency, and monetary metrics significantly improves prediction."
    - "Privacy-preserving techniques like federated learning are viable for compliance-focused PFMS."
    - "Interpretability tools (SHAP, LIME) are essential for building user trust in financial recommendations."
  limits:
    - "The review is not specifically focused on personal finance management systems for Filipino users."
    - "Most reviewed studies rely on proprietary data, potentially limiting generalizability to local spending patterns."
    - "Performance metrics are averaged across industries; context-specific tuning for PFMS may be required."
  mapping_rationale: "A systematic scan across all 12 functional domains identified the paper's strongest relevance to Behavioral Profiling & Classification (5.A, 5.C), Spending Forecasting (6.A, 6.B), and System Evaluation (12.A, 12.B). Topics under Filipino Cultural Context (2.A-D) were considered but rejected as the review is global, with no specific focus on Filipino practices. Expense Categorization (3.A-C) and Budget Recommendation (7.A-D) received medium relevance because the paper covers classification and feature engineering techniques foundational to these modules, though it does not directly address category design or allocation constraints. Anomaly Detection (8.A) was flagged for its discussion of autoencoders, and Data Privacy (10.A-B) for its coverage of federated learning and SHAP. User Retention (11.A-B) was considered but rejected as the paper is about modeling churn, not designing engagement mechanisms. Overall, the paper provides strong theoretical and empirical justification for Odin's predictive modeling and evaluation framework, but requires localization for the Philippine context."
limitations:
  - "The study is a literature review and does not provide novel empirical validation on a new dataset."
  - "The meta-analysis pools results from studies with heterogeneous preprocessing methods, which may affect comparability. [unacknowledged]"
  - "The review may have publication bias, as it includes only peer-reviewed studies from major databases. [unacknowledged]"
  - "The findings are based on customer churn in general, not specifically on financial behavior for personal budgeting. [unacknowledged]"
remember_this:
  - "Ensemble models (GBM, Random Forest) are the gold standard for churn prediction across sectors."
  - "Deep learning (LSTM, CNN) excels when modeling sequential behavioral data."
  - "AUC-ROC > 0.80 and F1 > 0.70 indicate robust model performance for imbalanced data."
  - "Feature engineering (RFM, engagement) often improves accuracy more than algorithm selection."
  - "Interpretability (SHAP/LIME) is critical for trust and adoption in regulated financial systems."
```