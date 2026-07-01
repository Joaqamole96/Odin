```yaml
paper_id: 10.1186/s40537-024-00965-y
designation: international-algorithm-specific
title: A model for investment type recommender system based on the potential investors based on investors and experts feedback using ANFIS and MNN
authors: Asemi, A.; Asemi, A.; Ko, A.
year: 2024
venue: Journal of Big Data
odin_topics:
- 1.A
- 1.B
- 1.C
- 2.D
- 3.C
- 5.A
- 5.C
- 7.A
- 7.B
- 7.C
- 8.A
- 12.B
- 13.C
tldr: An ANFIS-MNN hybrid recommender system predicts investment types using clustered investor data, achieving a 0.667 F1-score and 0.721 RMSE.
problem_and_motivation: Investors struggle with complex markets and overwhelming data, making informed decisions difficult. Existing recommender systems rely on limited inputs and cannot adapt to dynamic feedback or conditions. A personalized, adaptive system is needed to match investor profiles with suitable investment products.
approach:
- Data was collected via a web questionnaire from 1542 respondents across eight categories including demographics, finances, and traits.
- Data was preprocessed using ETL tools, JMP, MATLAB, and Python, then clustered using K-Means with Elbow Curve and Silhouette score.
- An ANFIS model was designed with three clustered inputs and one output, trained with a hybrid approach over three epochs using 188 data pairs and 18 fuzzy rules.
- Multimodal Neural Network pretraining was applied to initialize ANFIS weights, enhancing accuracy and generalization.
- The system incorporates expert feedback and investor opinions to refine rules and recommendations, evaluated using RMSE, accuracy, precision, recall, and F1-score.
findings:
- num: The ANFIS model achieved a minimal training RMSE of 0.721054.
- num: The model achieved an F1-score of 0.6667, indicating reasonably good precision and recall.
- num: Multimodal neural network pretraining resulted in a test MSE of 0.0011995.
- The ANFIS-based system outperformed traditional methods like decision trees and logistic regression.
- The system successfully generates personalized investment recommendations based on clustered investor profiles.
- Expert and investor feedback effectively customizes and improves the system's recommendations.
key_figures_tables:
- Figure 1: Data and fuzzy function for ANFIS model → Shows 3 inputs for investor clusters and 1 output for investment product clusters.
- Figure 2: Trained and tested grid of the ANFIS system → Visualizes the trained ANFIS structure with 18 fuzzy rules.
- Figure 3: Proposed ANFIS structure → Depicts the complete ANFIS architecture including fuzzification, rules, and defuzzification.
- Table 1: Description of research methodology → Outlines the seven stages from data collection to final predictions.
- Table 2: Description of data preprocessing → Details the eight data columns and their clustering techniques.
key_equations:
- equation: "None."
  explanation: ""
definitions:
- term: ANFIS
  definition: Adaptive Neuro-Fuzzy Inference System, a hybrid of fuzzy logic and neural networks.
- term: IRS
  definition: Investment Recommender System, a system that suggests investment products to users.
- term: MNN
  definition: Multimodal Neural Network, a neural network that learns from multiple data modalities.
- term: RMSE
  definition: Root Mean Square Error, a metric for prediction error.
- term: MF
  definition: Membership Function, a function that maps inputs to fuzzy sets.
critical_citations:
- "[Jang, 1993] — Introduced the ANFIS architecture foundational to this work."
- "[Asemi & Ko, 2021] — Proposed a combined business recommender system using customer feedback."
- "[Asemi et al., 2023] — Applied ANFIS to customize investment types based on demographics."
- "[Chen et al., 2021] — Proposed a machine learning model for Robo-advisor investment classification."
relevance:
  topics:
  - code: 1.A
    name: Filipino Young Professionals as a Demographic
    relevance: low
    justification: Paper focuses on investors generally but provides a demographic profiling framework.
  - code: 1.B
    name: Financial Structure of Filipino Young Professionals
    relevance: low
    justification: Discusses financial inputs like income and savings but not specific to Filipinos.
  - code: 1.C
    name: Financial Behavior of Filipino Young Professionals
    relevance: low
    justification: Covers investment behavior and decision-making, but not culturally specific.
  - code: 2.D
    name: Filipino Spending Cycles and "Occasions"
    relevance: contextual
    justification: Provides a framework for modeling investor behavior, but no specific seasonal analysis.
  - code: 3.C
    name: User-Defined Allocation Constraints
    relevance: medium
    justification: System takes user preferences as input, but constraints are not explicitly modeled as constraints.
  - code: 5.A
    name: Financial Behavioral Profiles in Personal Finance
    relevance: high
    justification: Core contribution is clustering investors into behavioral profiles for recommendations.
  - code: 5.C
    name: Classification Approaches for Financial Behavioral Profiles
    relevance: high
    justification: Uses ANFIS to classify investors into investment types based on multiple trait clusters.
  - code: 7.A
    name: Budgeting Strategies as Domain Knowledge
    relevance: low
    justification: Focuses on investment recommendation, not budgeting, but similar strategy-domain mapping.
  - code: 7.B
    name: Budget Recommendation in Personal Finance Systems
    relevance: low
    justification: System is for investment products, not budget allocation, but similar recommendation mechanism.
  - code: 7.C
    name: Constrained Optimization Approaches for Budget Allocation
    relevance: low
    justification: Does not use optimization; uses ANFIS for prediction.
  - code: 8.A
    name: Anomaly Detection in Personal Finance Systems
    relevance: contextual
    justification: Mentions error correction and refinement but not explicitly for anomaly detection.
  - code: 12.B
    name: Evaluation of Algorithmic Modules
    relevance: high
    justification: Thoroughly evaluates the ANFIS and MNN modules using RMSE, F1-score, accuracy, precision, and recall.
  - code: 13.C
    name: End-of-Period Surplus as a Savings Input
    relevance: low
    justification: System predicts investment types, not savings from surplus, but user's financial status is considered.
  contribution: This paper provides a framework for behavioral profiling through clustering (5.A, 5.C) and a hybrid machine learning method for classification (ANFIS) that could be adapted for expense categorization (3.A) or spending forecasting (6.A). Its evaluation methodology (12.B) offers metrics (RMSE, F1-score) for testing Odin's algorithmic modules. The system's use of user feedback and expert rules could inform Odin's user constraint handling (3.C) and budget recommendation logic (7.B).
  directly_justifies:
  - "ANFIS models can effectively classify investors based on multi-dimensional clustered inputs."
  - "Hybrid training approaches produce robust predictions for financial product recommendations."
  - "Multimodal neural network pretraining improves the accuracy and generalization of ANFIS models."
  - "Incorporating expert and user feedback enhances the relevance of recommender system outputs."
  limits:
  - "The system requires a significant amount of data to train, which may be impractical for smaller firms or individual users."
  - "The system is designed for retail investors and may not be suitable for institutional investors or complex portfolios."
  - "Potential biases in historical data could perpetuate existing inequalities in investment recommendations. [unacknowledged]"
  mapping_rationale: A systematic scan was conducted across all 12 functional domains and their associated topic codes. The domains flagged as relevant were Behavioral Profiling & Classification (high for 5.A, 5.C), System Evaluation (high for 12.B), and to a lesser extent, Expense Categorization (medium for 3.C), and Spending Forecasting (contextual for 8.A). The paper's primary contribution is algorithmic (ANFIS-MNN) for classifying investors into behavioral profiles, making 5.A and 5.C core. Its evaluation metrics directly support 12.B. The user-input aspects touch on 3.C, and the dynamic adaptation could relate to 8.A, but these are secondary. Domains like Filipino Cultural Context (2.A-D) and Mobile-First Design (9.A-B) were considered but rejected as the paper does not address cultural or mobile specifics. The paper is of high relevance to Odin's behavioral classification and algorithm evaluation modules, offering a validated approach and evaluation framework.
limitations:
- "The system requires a significant amount of data to train the ANFIS model."
- "The system is designed for retail investors and may not be suitable for institutional investors or complex portfolios."
- "Potential biases in historical data could perpetuate existing inequalities in investment recommendations. [unacknowledged]"
remember_this:
- "ANFIS achieved a 0.667 F1-score for investment type prediction."
- "The model's RMSE was 0.721, indicating moderate prediction accuracy."
- "Multimodal pretraining resulted in a very low test MSE of 0.0012."
- "Clustering investors into profiles enables personalized financial recommendations."
- "Expert feedback loops are effective for refining rule-based recommender systems."
```