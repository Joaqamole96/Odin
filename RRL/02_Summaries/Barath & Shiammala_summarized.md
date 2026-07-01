```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international-algorithm-specific
title: Loan Eligibility Prediction System Using Machine Learning
authors: Barath, S.; Shiammala, P. N.
year: 2026
venue: International Journal of Creative and Open Research in Engineering and Management
odin_topics:
  - 4.A
  - 4.B
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 10.A
  - 11.A
tldr: Automates loan eligibility screening using Logistic Regression and Random Forest, achieving 88.10% accuracy with the ensemble method.
problem_and_motivation: Manual loan verification is slow, error-prone, and introduces human bias, leading to financial losses and increased credit risk. Existing systems lack objective, data-driven automation. This paper addresses the need for a faster, more reliable loan approval workflow.
approach:
  - Uses a historical loan applicant dataset with features like income, credit history, and dependents.
  - Applies data preprocessing including imputation for missing values and label encoding for categorical variables.
  - Implements and compares Logistic Regression and Random Forest classifiers.
  - Evaluates models using accuracy, precision, and recall on an 80/20 train-test split.
  - Deploys the best-performing model as a Streamlit web application for real-time predictions.
findings:
  - num: Random Forest achieved an accuracy of 88.10% versus 82.45% for Logistic Regression.
  - The ensemble method (Random Forest) better captures non-linear relationships in financial data.
  - Credit history was identified as the most influential feature for predicting loan eligibility.
  - The system provides an instant, objective decision that reduces manual workload and human bias.
key_figures_tables:
  - Figure 1: Logistic Regression Sigmoid Curve showing probability mapping for approved/rejected loans.
  - Figure 2: Random Forest Architecture illustrating majority voting across decision trees for final prediction.
  - Table 1: Dataset description listing features like Gender, Income, Credit History, and Loan Status.
  - Figure 3: System architecture showing the three-tier flow from user input to prediction output.
key_equations:
  - equation: "P(Y=1) = 1 / (1 + e^{-z})"
    explanation: Sigmoid function maps features to a probability between 0 and 1.
definitions:
  - term: Random Forest
    definition: Ensemble learning method combining multiple decision trees via majority voting for robust prediction.
  - term: Logistic Regression
    definition: Statistical classification model using a sigmoid function for binary outcome prediction.
  - term: Label Encoding
    definition: Converting categorical text data into numerical format for machine learning models.
  - term: Pickle
    definition: Python serialization format used to save and load trained machine learning models.
  - term: Streamlit
    definition: Python framework for building interactive web applications for machine learning models.
critical_citations:
  - "[Breiman, 2001] — Introduced Random Forest ensemble learning method."
  - "[Hosmer et al., 2013] — Foundational text on Logistic Regression for binary classification."
  - "[Lessmann et al., 2015] — Ensemble methods outperform traditional models in credit scoring."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Discusses traditional manual loan processing as a baseline comparison.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly identifies manual verification as slow, biased, and error-prone.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Applies binary classification (approved/rejected) to loan applicants.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Uses ML to predict loan eligibility based on financial and historical data.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: Uses classification, not sequential forecasting, but relevant algorithm family.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: low
      justification: Tangentially related through income and loan amount features.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Indirectly related via credit history and loan eligibility assessment.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Mentions security as a benefit of automated systems but doesn't address privacy.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: contextual
      justification: Speeding up decisions could improve user experience and engagement.
  contribution: Provides a practical benchmark for comparing Logistic Regression and Random Forest on a binary financial classification task. Demonstrates a deployable architecture for automating approval workflows. The feature importance finding (credit history as dominant) can inform Odin's risk assessment modules. The end-to-end system design from preprocessing to UI deployment offers a template for similar modules. The performance comparison highlights the value of ensemble methods over simpler linear models.
  directly_justifies:
    - "Random Forest outperforms Logistic Regression for financial classification tasks."
    - "Automated ML systems reduce human bias and processing time."
    - "Credit history is the strongest predictor of loan eligibility."
  limits:
    - "Model performance depends on data entered by the user."
    - "Does not address cold-start problems for new applicants with no credit history."
    - "Not evaluated on Philippine-specific financial data or cultural contexts. [unacknowledged]"
  mapping_rationale: "A systematic scan of all 12 functional domains identified relevance primarily in 'Existing Systems & Gaps' (4.A, 4.B) and 'Predictive Modeling' (6.A). The paper's core contribution of comparing ML classifiers for binary financial decisions also informs 'Classification Approaches' (5.C) and 'Forecasting Algorithms' (6.B) at a low level. The domain 'Budget Recommendation' (7.A, 7.B) was considered due to the use of income and loan amounts, but rejected as the paper does not address budget allocation. 'Data Privacy' (10.A) is only mentioned superficially, providing contextual relevance. 'User Retention' (11.A) is indirectly touched upon via process automation. The algorithm-specific nature of the paper makes it relevant to 6.B, but the application to loan eligibility rather than spending forecasting keeps the relevance to 6.A as high and 6.B as low. The overall relevance is moderate as the paper provides a methodological benchmark and a deployable system template, but lacks direct application to PFMS features like categorization, forecasting, or behavioral profiling."
limitations:
  - "Model is not trained or validated on Philippine financial data."
  - "Does not explore advanced techniques for handling class imbalance. [unacknowledged]"
  - "Lacks a detailed comparison of feature engineering strategies."
  - "User interface is functional but not specifically designed for mobile-first interaction. [unacknowledged]"
remember_this:
  - "Random Forest achieved 88.10% accuracy for loan eligibility prediction."
  - "Credit history is the dominant feature for predicting loan approval."
  - "Ensemble methods outperform single classifiers in financial risk modeling."
  - "Automation reduces processing time and human bias in loan approvals."
```