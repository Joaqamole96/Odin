```yaml
paper_id: 10.5281/zenodo.17795962
designation: international-algorithm-specific
title: DYNAMIC CREDIT SCORING WITH MACHINE LEANING: ENHANCING FINANCIAL INCLUSION AND RISK MANAGEMENT
authors: Bakuwa, D.; Jimu, P.
year: 2026
venue: Afriresearch.com
odin_topics:
  - 1.A
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 3.A
  - 3.B
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 10.A
  - 10.B
tldr: Dynamic machine learning credit scoring integrates alternative data sources to expand financial inclusion and improve default prediction for underserved populations.
problem_and_motivation: Traditional credit scoring relies on static financial data, excluding unbanked individuals and limiting financial inclusion. Dynamic credit scoring using machine learning addresses this gap by enabling continuous, adaptive risk assessment using alternative data.
approach:
  - A three-tier system architecture was designed with presentation, application, and data layers.
  - Data was collected from traditional sources and alternative sources like mobile money, utility payments, and social behavior.
  - Data was cleaned and features were engineered, including temporal and network-based indicators.
  - Machine learning models including logistic regression, XGBoost, and LSTM were developed and trained.
  - Models were evaluated using ROC-AUC, precision, recall, and Gini coefficient, with fairness checks across groups.
findings:
  - num: Ensemble and LSTM models outperformed traditional logistic regression in predictive accuracy.
  - Incorporating alternative data significantly improved model performance for borrowers without formal credit histories.
  - num: 62% of borrowers were classified as low-risk, 25% as moderate-risk, and 13% as high-risk.
  - num: 58% of borrowers with no credit history were correctly identified as low or moderate risk using alternative data.
  - num: Risk-adjusted strategies using dynamic scoring could reduce expected default rates by 15-20%.
  - Dynamic models enable early detection of default signs and proactive intervention.
  - The LSTM model effectively tracked evolving borrower behavior in real-time.
  - Explainable AI tools like SHAP provide transparency into model predictions.
key_figures_tables:
  - "Figure: Risk tier classification distribution → 62% low-risk, 25% moderate-risk, 13% high-risk."
  - "Table: Model performance comparison → Ensemble and LSTM outperform logistic regression."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Machine Learning"
    definition: "A subset of artificial intelligence enabling systems to learn from data and make predictions."
  - term: "Dynamic Credit Scoring"
    definition: "Continuous updating of borrower credit profiles using real-time data."
  - term: "Financial Inclusion"
    definition: "Providing access to useful and affordable financial products and services."
  - term: "Alternative Data"
    definition: "Non-traditional data sources used for credit assessment, such as mobile transactions."
  - term: "XGBoost"
    definition: "An optimized gradient boosting algorithm for scalable and accurate predictive modeling."
  - term: "LSTM"
    definition: "Long Short-Term Memory, a neural network for capturing temporal patterns in sequential data."
critical_citations:
  - "[Lessmann et al., 2015] — Benchmarking classification algorithms for credit scoring."
  - "[Chen & Guestrin, 2016] — Introduces the XGBoost algorithm used in this study."
  - "[Khandani et al., 2010] — Demonstrates machine learning algorithms for consumer credit risk."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "contextual"
      justification: "Focuses on underserved populations in developing economies, relevant to similar demographics."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "medium"
      justification: "Examines behavioral financial patterns and alternative data for credit assessment."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "medium"
      justification: "Highlights cooperative savings groups and social behavior as credit indicators."
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "medium"
      justification: "Uses temporal features to capture evolving financial behaviors over time."
    - code: "2.D"
      name: "Filipino Spending Cycles and Occasions"
      relevance: "low"
      justification: "Discusses adaptive credit for changing financial conditions, broadly applicable."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "low"
      justification: "Mentions transaction data but focuses on credit risk, not expense categorization."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      relevance: "low"
      justification: "Alternative data types are mentioned but not categorized for user budgets."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Directly models borrower behavior profiles for credit risk assessment."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "high"
      justification: "Addresses scoring new borrowers without credit history using alternative data."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Compares ensemble, neural network, and regression models for behavior classification."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Core focus on predictive modeling for credit default and risk."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Uses LSTM to forecast default risk from sequential behavioral data."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "contextual"
      justification: "Discusses risk management but not specific budget recommendation strategies."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "contextual"
      justification: "Does not address budget recommendation, though credit access is related."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Fraud detection is mentioned as a risk management benefit."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "medium"
      justification: "Implicitly supports anomaly detection through temporal pattern analysis."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "medium"
      justification: "Explicitly discusses data privacy concerns in implementation."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "medium"
      justification: "Addresses model transparency and explainability as factors for borrower trust."
  contribution: "This paper justifies Odin's use of machine learning for behavioral profiling and risk prediction. It validates the integration of alternative data for scoring users without formal financial histories. The comparative model evaluation informs Odin's algorithm selection. The emphasis on explainable AI supports Odin's transparency and trust-building design. The findings on dynamic, real-time adaptation directly support Odin's forecasting and anomaly detection modules."
  directly_justifies:
    - "Machine learning models with alternative data can evaluate users lacking formal credit histories."
    - "LSTM models effectively capture temporal financial behavior for dynamic risk assessment."
    - "Dynamic scoring enables early default detection and proactive financial intervention."
    - "Ensemble methods like XGBoost improve predictive accuracy over static models for credit risk."
  limits:
    - "Study lacks empirical data from real-world loan defaults, relying on simulated performance metrics."
    - "Model bias may persist due to uneven data representation despite fairness monitoring. [unacknowledged]"
    - "Scalability and infrastructure challenges in low-resource regions are noted. [unacknowledged]"
    - "Highly accurate models like LSTM can be difficult to interpret without explainability tools. [unacknowledged]"
  mapping_rationale: "The systematic scan across all 12 functional domains flagged the Behavior and Forecasting domains as highly relevant. Topics 5.A, 5.B, 5.C (Behavioral Profiling) were selected with high relevance due to the paper's direct modeling of borrower behavior profiles and the cold-start problem. Topics 6.A and 6.B (Forecasting) received high relevance as the core contribution involves predictive modeling and sequential data forecasting. Topics 8.A and 8.B (Anomaly Detection) were rated medium, as fraud detection is cited as a benefit. Topics 10.A and 10.B (Privacy & Trust) were rated medium due to explicit discussions of data privacy and transparency. The borderline case of 2.B (Seasonal Spending) and 2.D (Filipino Occasions) was resolved by rating them medium and low respectively, as the paper addresses temporal patterns but not specifically Filipino seasonal cycles. Domains like Budget Recommendation (7) were considered but rejected as the paper does not address constrained optimization or budget allocation strategies. Similarly, Expense Categorization (3) was rejected due to a lack of focus on user-defined budget rules or category frameworks. Overall, the paper provides strong, directly actionable evidence for Odin's behavioral modeling, forecasting, and risk assessment modules, while offering contextual support for privacy and anomaly detection features."
limitations:
  - "Limited availability of alternative data for some borrowers reduces model coverage."
  - "Real-time scoring requires stable digital infrastructure and internet access."
  - "Data privacy and consent concerns are noted as implementation challenges."
  - "Model bias due to training data reflecting socio-economic disparities is acknowledged."
remember_this:
  - "Dynamic credit scoring improves financial inclusion for previously unbanked individuals."
  - "Alternative data enables risk assessment for borrowers without formal credit histories."
  - "LSTM and ensemble models achieve higher predictive accuracy for default prediction."
  - "Explainable AI tools are needed to ensure transparency and trust in lending decisions."
```