```yaml
paper_id: 10.1016/j.heliyon.2023.e20644
designation: local-algorithm-specific
title: A machine learning ensemble approach to predicting factors affecting the intention and usage behavior towards online groceries applications in the Philippines
authors: Gumasing, M.J.J.; Ong, A.K.S.; Sy, M.A.P.C.; Prasetyo, Y.T.; Persada, S.F.
year: 2023
venue: Heliyon
odin_topics:
  - 1.A
  - 1.B
  - 2.A
  - 2.B
  - 2.D
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 11.A
  - 11.B
  - 12.A
  - 12.B
  - 12.C
tldr: Filipino consumers' intention and usage of online grocery apps during COVID-19 are driven by perceived benefits, vulnerability, behavioral intention, performance expectancy, and severity.
problem_and_motivation: Existing studies on online grocery acceptance show inconsistent results, often lacking a holistic measure of behavioral intention when health concerns are present. No prior study in the Philippines has established a comprehensive model for online grocery acceptance during a pandemic.
approach:
  - A conceptual framework integrating UTAUT2 and Protection Motivation Theory (PMT) was developed.
  - A 67-item survey was administered to 373 Filipino online grocery users via convenience sampling from August to December 2021.
  - Data preprocessing included correlation analysis, aggregation, and normalization.
  - A Random Forest Classifier was optimized across 6,400 runs with varying parameters and training-test splits.
  - An Artificial Neural Network (ANN) was optimized with Tanh/Softmax activations and Adam optimizer at 150 epochs.
findings:
  - The ANN achieved a high average accuracy of 96.63% with no overfitting.
  - The Random Forest Classifier achieved a high average accuracy of 96% with 0.00 standard deviation.
  - num: 96.63% accuracy from ANN and 96% from Random Forest Classifier were consistent.
  - Perceived Benefit was the most significant factor, followed by Perceived Vulnerability and Behavioral Intention.
  - Performance Expectancy was a top factor, indicating efficiency and time savings are key drivers.
  - All ten constructs were found to be significant predictors of behavioral intention and usage.
key_figures_tables:
  - Figure 1: E-commerce growth rate by sector → Food/beverage grew 170.8% during the pandemic.
  - Figure 2: Conceptual framework → Integrated UTAUT2 and PMT with 12 hypotheses.
  - Figure 4: Decision tree from Random Forest → Perceived Benefit is the root node for usage behavior.
  - Figure 5: Optimum ANN model → Achieved 96.63% accuracy with Tanh/Softmax and Adam optimizer.
  - Table 6: Score of importance → Perceived Benefit is the most influential factor at 100% score.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: UTAUT2
    definition: Unified Theory of Acceptance and Use of Technology 2, a model for technology acceptance.
  - term: PMT
    definition: Protection Motivation Theory, a model for health-related behavior.
  - term: ANN
    definition: Artificial Neural Network, a supervised machine learning algorithm.
  - term: Random Forest Classifier
    definition: A classification tool using an ensemble of decision trees.
  - term: Perceived Benefit
    definition: Belief that a course of action reduces disease risk and leads to positive results.
critical_citations:
  - "[Venkatesh et al., 2012] — Introduced UTAUT2 and its core constructs."
  - "[Chuenyindee et al., 2022] — Justified integrating PMT for health-related technology acceptance."
  - "[Ong et al., 2022] — Demonstrated machine learning ensemble for behavioral prediction."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: The study directly surveys Filipino consumers, establishing baseline demographics.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Provides income and spending data on groceries, relevant to financial structure.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Addresses the shift to online grocery in the Philippines, a culturally driven behavior.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Mentions pandemic-induced changes in grocery spending patterns.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: medium
      justification: Directly relevant to Filipino spending behavior during the pandemic.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Predicts factors affecting consumer behavior, directly contributing to profile understanding.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: contextual
      justification: Provides a framework for understanding initial behavioral intention.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Uses machine learning classification to categorize behavioral predictors.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Employs predictive modeling (ANN and Random Forest) to forecast usage behavior.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: The modeling approach could be extended to forecasting spending.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Directly addresses behavioral intention and usage, key engagement metrics.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: contextual
      justification: The findings can inform design for retention (e.g., highlighting benefits).
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses a systematic methodological framework for evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Specifically evaluates the performance of ANN and Random Forest classifiers.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: contextual
      justification: The evaluation methodology is relevant but not directly about budget recommendations.
  contribution: This study provides a validated machine learning ensemble framework for predicting behavioral intention and usage in the context of online grocery applications. It directly justifies the use of ANN and Random Forest classifiers for Odin's behavioral profiling and prediction modules. The integration of UTAUT2 and PMT offers a robust theoretical foundation for understanding user motivation, which can inform engagement strategies. The identification of perceived benefit and vulnerability as top predictors can guide Odin's user onboarding and feature prioritization. The high accuracy of the models demonstrates the feasibility of using similar techniques for Odin's forecasting and classification tasks.
  directly_justifies:
    - "Machine learning ensembles can achieve high accuracy (>96%) in predicting consumer behavior."
    - "Perceived benefit and vulnerability are the most significant drivers of behavioral intention."
    - "UTAUT2 and PMT can be effectively integrated to model technology acceptance in a health context."
    - "Filipino consumers are highly receptive to online services, indicating a strong market for PFMS."
  limits:
    - "Respondents were predominantly from highly urbanized areas, limiting generalizability to rural populations."
    - "The study did not consider socio-economic factors for clustering, which could refine user segmentation."
    - "Data was collected during the COVID-19 pandemic, which may not reflect post-pandemic baseline behavior."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant for domains related to Filipino context (2.A, 2.D), behavioral profiling (5.A, 5.C), predictive modeling (6.A, 6.B), and system evaluation (12.B). The paper's focus on machine learning for prediction directly justifies high relevance for 5.C, 6.A, 12.A, and 12.B. The integration of UTAUT2 and PMT provides a strong framework relevant to 5.A and 5.B. The study's context of Filipino consumer behavior is directly applicable to 2.A and 2.D. Domains like 1.A, 1.B were considered relevant as they provide demographic and financial structure data, assigned medium relevance. Domains like expense categorization (3.A, 3.B), anomaly detection (8.A, 8.B), and savings/debt (13.A, 13.B) were rejected as the paper does not address these specific functionalities. The overall relevance is high, as the paper provides a validated methodological approach for predicting user behavior, which is central to Odin's core functions.
limitations:
  - "The majority of respondents reside in highly urbanized cities, affecting generalizability to rural consumers."
  - "Lack of consideration of socio-economic factors (e.g., income, employment) for customer segmentation."
  - "Data was collected during COVID-19 lockdowns, which may not reflect behavior under normal conditions."
remember_this:
  - "Perceived benefit was the most significant driver of online grocery usage behavior."
  - "The Artificial Neural Network achieved a high accuracy of 96.63% for predicting usage behavior."
  - "The Random Forest Classifier achieved a consistent 96% accuracy with zero standard deviation."
  - "Filipino consumers were highly receptive to online grocery during the COVID-19 pandemic."
```