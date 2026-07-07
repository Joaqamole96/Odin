```yaml
paper_id: 10.1007/s10462-025-11416-2
designation: international
title: Machine learning powered financial credit scoring: a systematic literature review
authors: Ayari, H.; Guetari, R.; Kraïem, N.
year: 2026
venue: Artificial Intelligence Review
odin_topics:
  - 1.B
  - 3.A
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 7.C
  - 8.A
  - 8.B
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
  - 13.C
tldr: A systematic literature review of 63 studies on ML credit scoring shows ensemble and hybrid models consistently outperform traditional approaches, while DL faces interpretability and data availability barriers.
problem_and_motivation: Traditional credit scoring models like logistic regression depend on narrow features and struggle to capture complex behavioral patterns, limiting their effectiveness with heterogeneous borrower profiles. Financial institutions face the challenge of processing loan applications quickly while maintaining accuracy, fairness, and regulatory compliance. ML approaches offer the potential to improve prediction accuracy, handle high-dimensional data, and incorporate alternative data sources, but their adoption is hindered by issues of interpretability, bias, and computational complexity.
approach:
  - Conducted a systematic literature review following PRISMA 2020 guidelines across four digital libraries (SpringerLink, ACM, IEEE Xplore, Google Scholar).
  - Employed a structured search query combining credit scoring, ML, DL, and ensemble learning terms for publications between 2018 and 2024.
  - Applied inclusion criteria focusing on peer-reviewed studies with empirical results and clearly defined evaluation metrics.
  - Performed data extraction covering ML techniques, datasets, evaluation metrics, and performance results from 63 selected studies.
  - Used bibliographic coupling and keyword co-occurrence analysis (VOSviewer) to map intellectual structure and thematic clusters.
findings:
  - "num: Ensemble and hybrid models consistently outperform single classifiers, with accuracy improvements up to 91.91% on the German dataset (GA+NN) and 93.16% on the Japanese dataset (multi-stage ensemble)."
  - "num: XGBoost-BO improved accuracy by 4.10% on the German dataset, 3.03% on Lending Club, and 2.76% on the Australian dataset."
  - "num: Deep CNN achieved 99.74% accuracy on the Australian credit dataset, significantly outperforming MLP's 90.75%."
  - "num: The GA-based feature selection combined with CatBoost achieved accuracies of 86.70%, 88.40%, and 86.20% on German, Australian, and Japanese datasets."
  - Interpretability challenges persist for complex ML models, with LIME and SHAP emerging as tools to bridge the explainability gap.
  - Alternative data sources (social media, mobile usage, psychometrics) show promise for credit scoring, especially for borrowers lacking traditional credit histories.
  - Accuracy (49 studies) and AUC (31 studies) are the most frequently reported evaluation metrics in credit scoring literature.
key_figures_tables:
  - "Table 4: Summary of machine learning studies → Shows LR, RF, SVM, KNN, and hybrid models with performance on German, Australian, and proprietary datasets."
  - "Table 5: Summary of deep learning studies → CNN, LSTM, and hybrid DL models achieve high accuracy on credit scoring benchmarks."
  - "Table 6: Summary of ensemble learning studies → Ensemble methods like XGBoost, GBDT, and multi-stage models dominate top performance rankings."
  - "Table 7: Ranked evaluation on German dataset → GA+NN achieves highest accuracy (91.91%) and AUC (92.60%)."
  - "Figure 2: Comparative accuracy of ML models → Random Forest and hybrid ML approaches achieve highest accuracies with low variability."
  - "Figure 3: Comparative accuracy of DL models → CNN and hybrid DL provide robust performance with lower variability."
  - "Figure 4: Comparative accuracy of ensemble models → XGB-BO and proposed ensembles capture peak performance in certain studies."
  - "Figure 5: Bibliographic coupling network → Three clusters: traditional statistical approaches, ensemble-based ML, and emerging DL applications."
key_equations:
  - equation: "P(Y=1|x) = 1 / (1 + e^{-(β0 + β^T x)})"
    explanation: "Logistic regression estimates probability of binary credit default outcome."
  - equation: "ℓ(β0, β) = Σ [y_i log p(x_i) + (1 - y_i) log(1 - p(x_i))]"
    explanation: "Log-likelihood maximized to estimate logistic regression parameters."
  - equation: "Accuracy = (TP + TN) / (TP + TN + FP + FN)"
    explanation: "Overall correctness measure, limited with imbalanced credit data."
  - equation: "F1-Score = 2 × (Precision × Recall) / (Precision + Recall)"
    explanation: "Harmonic mean balancing precision and recall for class imbalance."
definitions:
  - term: "ML"
    definition: "Machine learning, algorithms that enable systems to learn from data and make predictions without explicit programming."
  - term: "DL"
    definition: "Deep learning, subset of ML using neural networks with multiple layers to automatically extract features."
  - term: "EL"
    definition: "Ensemble learning, integration of multiple learning algorithms to enhance predictive performance."
  - term: "LR"
    definition: "Logistic regression, probabilistic classification model estimating binary outcome probability."
  - term: "RF"
    definition: "Random forest, ensemble of decision trees using bagging for classification and regression."
  - term: "SVM"
    definition: "Support vector machine, supervised model mapping data to high-dimensional space for classification using hyperplanes."
  - term: "KNN"
    definition: "K-nearest neighbors, non-parametric technique classifying based on distance metrics to nearest neighbors."
  - term: "CNN"
    definition: "Convolutional neural network, deep feedforward network for feature extraction and classification."
  - term: "LSTM"
    definition: "Long short-term memory, recurrent neural network designed for variable length sequences with memory gates."
  - term: "XGBoost"
    definition: "Extreme gradient boosting, ensemble model combining tree models with gradient boosting."
  - term: "GBDT"
    definition: "Gradient boosting decision tree, ensemble method combining weak base learners to craft robust models."
  - term: "AUC"
    definition: "Area under the ROC curve, measure of model's ability to distinguish between classes."
  - term: "PRISMA"
    definition: "Preferred reporting items for systematic reviews and meta-analyses, guideline framework for systematic reviews."
critical_citations:
  - "[Dastile et al., 2020] — Found ensemble methods outperform single classifiers in credit scoring."
  - "[He et al., 2018] — Proposed novel ensemble method adapting to different imbalance ratios."
  - "[Dumitrescu et al., 2022] — Introduced PLTR combining logistic regression with decision tree rules."
  - "[Hayashi, 2022] — Reviewed deep learning applications and interpretability challenges in credit scoring."
  - "[Bücker et al., 2022] — Framework for enhancing interpretability of black-box ML credit scoring models."
relevance:
  topics:
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "contextual"
      justification: "Discusses financial behavior and repayment history in credit scoring, relevant to financial structure analysis."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "low"
      justification: "Credit scoring classification approaches inform categorization methodologies for PFMS."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews existing credit scoring methodologies and ML-based approaches in financial systems."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Identifies limitations of traditional credit scoring models and gaps in ML adoption including interpretability and bias."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "ML models classify borrower behavior and creditworthiness, informing behavioral profile construction."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Systematically reviews ML classification techniques including SVM, RF, and ensemble methods for credit scoring."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Reviews predictive modeling techniques including DL and ensemble methods for credit risk prediction."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "medium"
      justification: "LSTM and attention mechanisms discussed for sequence-based credit prediction, applicable to spending forecasting."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "low"
      justification: "Credit scoring ML approaches inform algorithmic design for budget recommendation systems."
    - code: "7.C"
      name: "Constrained Optimization Approaches for Budget Allocation"
      relevance: "contextual"
      justification: "Discusses optimization methods for credit scoring models, tangentially related to budget constraints."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Credit default prediction frameworks analogous to anomaly detection approaches for spending behavior."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "low"
      justification: "Machine learning classification techniques transferable to anomaly detection in spending data."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "contextual"
      justification: "Discusses mobile phone data for credit scoring, relevant to mobile-first design context."
    - code: "9.B"
      name: "Mobile UX Design for Personal Finance"
      relevance: "contextual"
      justification: "Alternative data from mobile usage informs user experience considerations for financial applications."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "medium"
      justification: "Addresses privacy concerns in using alternative data and regulatory compliance (GDPR, IFRS 9)."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "high"
      justification: "Interpretability and explainability (SHAP, LIME) are critical for building user trust in automated credit decisions."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Comprehensively reviews evaluation metrics (accuracy, AUC, F1-score, G-mean, KS) used in credit scoring studies."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Provides detailed performance comparisons of ML, DL, and ensemble algorithms across benchmark datasets."
    - code: "13.C"
      name: "End-of-Period Surplus as a Savings Input"
      relevance: "contextual"
      justification: "Credit scoring default prediction models use surplus/deficit patterns, relevant to surplus management."
  contribution: "This systematic review provides a comprehensive framework for selecting ML algorithms for Odin's spending classification and forecasting modules by benchmarking performance across datasets. It validates the use of ensemble and hybrid models for behavioral profiling, establishing an evidence base for Odin's classification engine. The review's analysis of evaluation metrics directly informs Odin's evaluation strategy for algorithmic modules, supporting performance comparison and validation. The identification of interpretability techniques like SHAP and LIME guides Odin's approach to building user trust through explainable predictions. The discussion of alternative data integration contextualizes Odin's use of Filipino-specific spending cycles and user-declared preferences."
  directly_justifies:
    - "Ensemble and hybrid ML models consistently outperform single classifiers in credit scoring tasks."
    - "Model interpretability is critical for user trust and regulatory compliance in financial decision-making."
    - "Alternative data sources can improve credit assessment for borrowers lacking traditional financial histories."
    - "Accuracy and AUC are the most commonly used metrics for evaluating predictive model performance."
    - "Class imbalance handling techniques like SMOTE are essential for reliable credit risk assessment."
  limits:
    - "Limited to peer-reviewed journal papers and conference articles, excluding relevant technical reports or industry studies."
    - "Search confined to four online databases, potentially missing relevant studies from other digital libraries."
    - "Lack of comparative analysis to identify most effective models due to heterogeneous evaluation metrics across studies."
    - "Fast-evolving nature of ML means continuous updates are necessary to capture new advances."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated canonical topics was performed. The paper was flagged as highly relevant for Predictive Modeling (6.A, high), Classification Approaches (5.C, high), Evaluation Frameworks (12.A, high), Algorithmic Module Evaluation (12.B, high), and User Trust (10.B, high). Medium relevance was assigned to Existing Systems (4.A), System Limitations (4.B), Behavioral Profiles (5.A), Anomaly Detection (8.A), and Data Privacy (10.A), as the paper reviews existing systems and discusses privacy concerns. Low relevance was assigned to Expense Categorization (3.A) and Anomaly Detection Algorithms (8.B) as the paper does not specifically address these domains. Contextual relevance was assigned to Financial Structure (1.B), Budgeting Strategies (7.A), Mobile-First Design (9.A, 9.B), and End-of-Period Surplus (13.C) as these areas are tangentially related to the review's focus on credit scoring. The paper was considered and rejected for Culturally Specific Financial Practices (2.A-D) and Retention Mechanisms (11.A-B) as these domains were not addressed. Overall, the paper provides substantial evidence for Odin's machine learning modules, evaluation frameworks, and interpretability requirements."
limitations:
  - "Search strategy limited to four online databases, excluding relevant studies from other digital libraries. [unacknowledged]"
  - "Heterogeneous evaluation metrics across studies hinder direct performance comparisons between models. [acknowledged]"
  - "Class imbalance and varying data preprocessing methods complicate cross-study validation. [unacknowledged]"
  - "Interpretability challenges persist for complex ML models, with SHAP and LIME facing reliability concerns under adversarial conditions."
  - "High-dimensional credit data introduces computational complexity, making deployment costly for smaller institutions."
remember_this:
  - "Ensemble and hybrid ML models consistently outperform single classifiers in credit scoring."
  - "Model interpretability is critical for building user trust in automated financial decisions."
  - "Class imbalance handling techniques like SMOTE are essential for reliable credit risk models."
  - "Alternative data sources show promise for borrowers lacking traditional credit histories."
  - "Accuracy and AUC are the most common evaluation metrics for credit scoring models."
```