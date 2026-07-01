```yaml
paper_id: f5a8b3e2-9c4d-4a7f-8e1a-2b3c4d5e6f7g
designation: local-algorithm-specific
title: Rapid Assessment of Real Estate Loan Disapproval via Predictive Modeling: A Case for the Philippines
authors: Corpuz, A.N.; Lansangan, J.R.
year: 2019
venue: The Philippine Statistician
odin_topics:
  - 5.A
  - 5.C
  - 7.B
  - 7.C
  - 7.D
  - 8.A
tldr: Predictive models, especially random forest, accurately identify home loan disapproval determinants using client and housing data.
problem_and_motivation: Philippine housing backlog necessitates efficient loan approval processes. Developers face forfeitures when buyers fail to secure financing. Rapid assessment models can identify likely disapprovals early, allowing buyers to adjust.
approach:
  - Data from 9,316 Pro-Friends homebuyers (2014-2016) was used, with 1,042 disapproved loans.
  - Predictive models included binary logistic regression, CART, CTree, CHAID, and random forest.
  - Training and test sets were split 75/25, maintaining the 89% approval rate.
  - Performance was evaluated using accuracy, sensitivity, specificity, and F-score.
  - Random forest utilized 500 trees with mtry=5.
findings:
  - num: Random forest achieved 98.68% accuracy on test data, outperforming all other models.
  - num: Logistic regression, CART, and CHAID had similar test accuracies around 92.84-92.90%.
  - num: CTree had a test accuracy of 93.12% and the highest F-score (43.95%) among non-RF models.
  - num: Random forest's sensitivity (87.65%) was nearly four times higher than logistic regression (24.12%).
  - The main determinants of loan approval are equity term, total contract price, payment status, and income.
  - Payment status is the most important predictor across all tree-based models.
  - Self-employed and unemployed applicants face higher disapproval likelihood.
  - In this dataset, females were more likely to have loans disapproved than males.
key_figures_tables:
  - Table 8: Loan applications show ~12% disapproval rate across 2014-2016 → Consistent imbalance in data.
  - Table 10: Descriptive stats show average TCP is ~1.8M PHP and most buyers are 30-49 years old → Key applicant profile.
  - Figure 3: CTree uses payment status, age, and equity discount as top splits → Non-linear interactions.
  - Figure 5: Random Forest Mean Decrease Gini shows TCP, payment status, equity term as most important → Key features for model.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: CART
    definition: Classification and Regression Trees, a decision tree algorithm.
  - term: CHAID
    definition: Chi-squared Automatic Interaction Detection, a decision tree method.
  - term: CTree
    definition: Conditional Inference Trees, a recursive partitioning algorithm.
  - term: F-score
    definition: Harmonic mean of precision and recall, balancing prediction performance.
critical_citations:
  - "[Galindo and Tamayo, 2000] — CART had lowest test error (8.3%) in mortgage default."
  - "[Ghatasheh, 2014] — Random Forest is competitive and interpretable for credit risk."
  - "[Wah and Ibrahim, 2011] — Logistic regression achieved 74.56% accuracy for credit scoring."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Models classify applicants by approval risk, reflecting financial behavior profiles.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Compares decision trees, random forest, and logistic regression for classification.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: contextual
      justification: Addresses loan affordability indirectly through income and TCP.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: low
      justification: Identifies factors (income, TCP) that could constrain budget allocation.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: low
      justification: Model flags high-risk applicants, akin to identifying infeasible loan cases.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Loan disapproval prediction can be framed as anomaly detection.
  contribution: The paper provides a validated random forest model for classifying loan disapproval risk, demonstrating high accuracy and sensitivity. This directly supports Odin's module for behavioral profiling by showing how tree-based methods can identify key financial risk indicators. The findings on payment status and income inform Odin's budget recommendation and infeasibility handling by highlighting critical constraints. The comparative evaluation of multiple classifiers offers a methodology for Odin's system evaluation.
  directly_justifies:
    - Random forest is superior for balanced prediction of financial risk (F-score 92.55%).
    - Payment status is the most important predictor of loan disapproval.
    - Income must be commensurate with total contract price and equity term for loan approval.
    - Self-employed and unemployed applicants have higher disapproval risk.
  limits:
    - "Model derived from a single developer's data, limiting generalizability. [unacknowledged]"
    - "Only 1% missing values excluded; imputation could improve robustness. [unacknowledged]"
    - "No external validation on new datasets from other developers or regions."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains flagged as relevant include Behavioral Profiling & Classification (high relevance for 5.C), Budget Recommendation (contextual for 7.B, low for 7.C and 7.D), and Anomaly Detection (medium for 8.A). The paper directly compares classification algorithms (logistic regression, CART, CTree, CHAID, random forest), making 5.C highly relevant. Its focus on loan approval risk aligns with anomaly detection (8.A) and behavioral profiles (5.A). The paper touches on income and contract price as constraints, linking to budget recommendation topics (7.B, 7.C, 7.D) but only contextually. Domains like Filipino Cultural Context (2), Expense Categorization (3), Existing Systems (4), Spending Forecasting (6), Mobile-First Design (9), Data Privacy (10), User Retention (11), System Evaluation (12), and Savings & Debt Management (13) were considered and rejected because the paper does not address these areas. The overall relevance is moderate, primarily contributing to algorithmic classification approaches for financial risk assessment.
limitations:
  - "Model is specific to Pro-Friends data and may not generalize to other developers."
  - "Potential confounding effects in logistic regression due to multicollinearity."
  - "No model maintenance or updating procedures were explored for long-term validity. [unacknowledged]"
remember_this:
  - Random forest achieved 98.68% accuracy in predicting loan disapproval.
  - Payment status is the strongest predictor of loan disapproval.
  - Total contract price and equity term are key determinants.
  - Random forest provides balanced performance with 92.55% F-score.
```