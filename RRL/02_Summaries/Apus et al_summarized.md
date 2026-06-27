```yaml
paper_id: d2a3b4c5-6e7f-48a9-b0c1-d2e3f4a5b6c7
designation: local-algorithm-specific
title: Predicting the Filipino Household Income Using Naive Bayes Classification Algorithm
authors: Apus, J.O.; Mantalaba, K.D.V.; Mackno, A.J.B.; Bokingkito, P.B.
year: 2023
venue: International Journal of Computing and Digital Systems
odin_topics:
  - 3.A
  - 5.A
  - 5.C
  - 6.A
  - 12.B
tldr: Predicts Filipino household income class using Naive Bayes with expenditure and income features from FIES data, achieving 93% accuracy with bagging.
problem_and_motivation: Philippine poverty reduction requires accurate identification of vulnerable households. Existing predictive models rely mainly on socio-demographic variables, neglecting expenditure and income data. This gap limits the effectiveness of targeted interventions.
approach:
  - Used the 2018 FIES dataset with 41,545 households and 60 features, cleaning missing values using mode for categorical and mean/median for numeric.
  - Selected 13 features using univariate chi-squared feature selection based on correlation with income class.
  - Implemented Naive Bayes classifier with bagging and boosting ensemble techniques using Python's sklearn.
  - Split data 80-20 for training and testing; evaluated using confusion matrix, precision, recall, F1-score, and accuracy.
  - Compared bagging and boosting ensemble methods to determine best performance.
findings:
  - "num: Bagging ensemble achieved 93% accuracy, while boosting achieved 89% accuracy."
  - "num: Bagging model had precision 0.93, recall 0.94, and F1-score 0.94 weighted mean."
  - "num: Boosting model had precision 0.90, recall 0.93, F1-score 0.91."
  - Poor income class had the most true positives; rich class had the least.
  - Models with accuracy above 80% are considered good, indicating Naive Bayes is effective for this task.
key_figures_tables:
  - "Table III: Selected features with chi-squared scores → top features include total food and transportation expenditure."
  - "Figure 3: Confusion matrix for bagging model → shows strong diagonal performance across income classes."
  - "Table VI: Classification report for bagging ensemble → weighted averages above 0.93 for precision, recall, F1."
key_equations:
  - equation: "Precision = TP/(TP+FP)"
    explanation: "Measures accuracy of positive predictions."
  - equation: "Recall = TP/(TP+FN)"
    explanation: "Measures proportion of actual positives correctly identified."
  - equation: "F1 = 2*(Precision*Recall)/(Precision+Recall)"
    explanation: "Harmonic mean of precision and recall."
  - equation: "Accuracy = (TP+TN)/(P+N)"
    explanation: "Overall proportion of correct predictions."
definitions:
  - term: "FIES"
    definition: "Family Income and Expenditure Survey conducted by the Philippine Statistics Authority."
  - term: "PSA"
    definition: "Philippine Statistics Authority, the national statistical agency."
  - term: "Bagging"
    definition: "Bootstrap aggregating; an ensemble method to reduce variance."
  - term: "Boosting"
    definition: "An ensemble method that iteratively adjusts weights of misclassified instances."
critical_citations:
  - "None."
relevance:
  topics:
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "medium"
      justification: "Uses expenditure categories as predictive features, relevant to categorization design."
    - code: "5.A"
      name: "Financial Behavioral Profiles"
      relevance: "medium"
      justification: "Classifies households into income classes, a form of financial profile."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Directly applies a classification algorithm to financial data, relevant to profile classification module."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "low"
      justification: "Predicts income class, but not spending forecasting; general predictive modeling context."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Provides evaluation metrics and comparison of ensembles, useful for algorithm evaluation."
  contribution: "This paper's use of expenditure features for classification can inform Odin's expense categorization module by highlighting which spending categories are most discriminative of income class. The Naive Bayes algorithm and ensemble evaluation provide a baseline for Odin's behavioral profiling module. The feature selection method (chi-squared) can guide Odin's feature engineering for user profiles. The high accuracy suggests that expenditure data alone can predict financial class, which can be used for cold-start profiling in Odin."
  directly_justifies:
    - "Expenditure categories such as food and transportation are strong predictors of income class."
    - "Naive Bayes with bagging achieves 93% accuracy in classifying Filipino household income."
    - "Feature selection using chi-squared can identify relevant expenditure features."
    - "Models with accuracy above 80% are considered effective for classification tasks."
  limits:
    - "The model is trained on aggregated survey data, not individual spending transactions, limiting applicability to personal finance systems [unacknowledged]."
    - "Only uses 13 features; other relevant financial behaviors may be omitted [unacknowledged]."
    - "The dataset is from 2018; spending patterns may have changed [unacknowledged]."
  mapping_rationale: "Systematic scan of all 12 functional domains and their associated topic codes flagged the Expense Categorization (3.A, medium), Behavioral Profiling (5.A medium, 5.C high), Predictive Modeling (6.A low), and System Evaluation (12.B medium) domains as relevant. The paper's focus on classifying income using expenditure features directly maps to 5.C (classification approach) and 3.A (use of expense categories). The borderline case of predictive modeling was considered: although it is predictive, it does not forecast sequential spending, so 6.A is low. Domains such as Budget Recommendation, Anomaly Detection, Mobile-First, Data Privacy, and Retention were rejected as the paper does not address them. Overall, the paper provides moderate to high relevance for Odin's profiling and classification modules."
limitations:
  - "Only used 13 features; additional parameters like region and family size could improve accuracy."
  - "Explored only Naive Bayes; other algorithms may yield better performance."
  - "The study does not address real-time application or integration into a PFMS."
remember_this:
  - "Bagging Naive Bayes achieved 93% accuracy for income class prediction."
  - "Food and transportation expenditures are top predictors of income class."
  - "Naive Bayes is simple, fast, and robust to missing data."
  - "Feature selection using chi-squared improves model performance."
  - "Expenditure data alone can effectively classify Filipino household income."
```
