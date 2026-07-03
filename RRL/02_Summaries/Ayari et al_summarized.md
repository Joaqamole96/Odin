```yaml
paper_id: 10.1007/s10462-025-11416-2
designation: international
title: Machine learning powered financial credit scoring: a systematic literature review
authors: Ayari, H.; Guetari, R.; Kraïem, N.
year: 2026
venue: Artificial Intelligence Review
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
  - 12.C
tldr: A systematic review of 63 studies on machine learning credit scoring identifies ensemble and hybrid models as most accurate, with key challenges in interpretability, bias, and alternative data integration.
problem_and_motivation: Traditional credit scoring models rely on narrow features and linear assumptions, limiting their effectiveness for non-traditional borrowers. There is a need to systematically synthesize recent ML advancements to guide practitioners and researchers. This review addresses the gap by providing a comprehensive and structured analysis of ML methods, trends, and challenges for credit scoring.
approach:
  - Conducted a systematic literature review following PRISMA 2020 guidelines, searching four major digital libraries (Springer, ACM, IEEE, Google Scholar).
  - Analyzed 330 initial papers, selecting 63 peer-reviewed studies from 2018-2024 after rigorous screening for empirical results and methodological transparency.
  - Extracted data on ML techniques, datasets, evaluation metrics, and performance results using a structured form and quality assessment checklist.
  - Categorized models into traditional ML, deep learning, and ensemble learning, including hybrid approaches within each category.
  - Applied science mapping methods, including bibliographic coupling and keyword co-occurrence, to identify thematic clusters and research trends.
  - Performed a comparative analysis of model performance on standard datasets (German, Australian, Japanese, Lending Club) and discussed challenges.
findings:
  - Ensemble and hybrid models, combining feature optimization and multiple classifiers, consistently outperform single classifiers across benchmark datasets.
  - num: On the German dataset, the GA+NN model achieved the highest accuracy (91.91%) and AUC (92.60%).
  - num: Deep learning models like CNNs show promise with large datasets but are less commonly applied due to interpretability challenges.
  - The use of alternative data sources (social media, mobile usage, psychometrics) is an emerging trend that can enhance predictive accuracy.
  - Interpretability techniques like SHAP and LIME are increasingly adopted to address the "black box" nature of complex ML models.
  - Key challenges in adopting ML for credit scoring include interpretability, potential biases, and the curse of dimensionality.
key_figures_tables:
  - Table 7: Performance comparison on German dataset → GA+NN achieves highest accuracy (91.91%) and AUC (92.60%).
  - Table 8: Performance comparison on Australian dataset → Multi-stage ensemble model achieves best accuracy (92.36%) and AUC (96.65%).
  - Table 9: Performance comparison on Japanese dataset → Multi-stage ensemble model achieves best accuracy (93.16%) and AUC (96.95%).
  - Figure 2: Comparative accuracy of ML models → Hybrid ML approaches demonstrate top performance with low variability.
  - Figure 5: Bibliographic coupling network → The literature is organized into three main clusters: traditional, ensemble, and deep learning approaches.
key_equations:
  - equation: "P(Y=1|x) = 1 / (1 + e^{-(β0 + β^T x)})"
    explanation: Logistic regression estimates probability of binary outcome for credit scoring.
  - equation: "Accuracy = (TP + TN) / (TP + TN + FP + FN)"
    explanation: Overall correctness of a classification model.
  - equation: "F1-Score = 2 × (Precision × Recall) / (Precision + Recall)"
    explanation: Harmonic mean of precision and recall for imbalanced datasets.
definitions:
  - term: AUC
    definition: Area Under the ROC Curve, measures model's ability to distinguish between classes.
  - term: G-Mean
    definition: Geometric mean of sensitivity and specificity, balances class performance.
  - term: KS
    definition: Kolmogorov-Smirnov statistic, measures model's discriminatory power in credit scoring.
  - term: SHAP
    definition: SHapley Additive exPlanations, a method to explain predictions by quantifying feature contributions.
  - term: LIME
    definition: Local Interpretable Model-agnostic Explanations, explains individual predictions using local approximations.
  - term: SMOTE
    definition: Synthetic Minority Over-sampling Technique, addresses class imbalance by generating synthetic samples.
critical_citations:
  - "[Dumitrescu et al., 2022] — Introduces PLTR, combining LR with decision-tree rules for interpretable non-linear credit scoring."
  - "[He et al., 2018] — Proposes an ensemble method adapting to varying class imbalance ratios using BalanceCascade and stacking."
  - "[Bao et al., 2019] — Demonstrates the value of integrating unsupervised learning with supervised models for credit risk assessment."
  - "[Hayashi, 2022] — Highlights the superior performance of Deep Belief Networks and challenges in DL interpretability."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: Provides a general overview of ML classification methods that could be adapted for expense categorization.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: contextual
      justification: Discusses feature selection and data preprocessing, relevant for designing effective categories.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Surveys existing credit scoring systems and their evolution, providing context for PFMS.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Explicitly details the limitations of traditional credit scoring (e.g., narrow features, linearity) which are relevant to PFMS gaps.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Reviews methods for classifying borrower creditworthiness, which parallels user behavioral profiling in PFMS.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Reviews ML classification techniques applicable to user profiling.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Central focus of the review; provides extensive evidence on forecasting methods for financial outcomes.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: Discusses LSTM networks for sequential data, relevant for spending prediction.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Discusses outlier detection methods in credit scoring, which can inform anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: Reviews outlier detection techniques that could be applied to spending data.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Identifies privacy concerns with alternative data and compliance with standards like GDPR and IFRS 9.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Emphasizes the need for interpretability and transparency to build trust, a core challenge for user adoption.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a comprehensive overview of evaluation metrics (accuracy, AUC, F1, KS) and their use in financial systems.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Compares performance of different ML algorithms, directly relevant for evaluating Odin's modules.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Discusses comparative evaluation of models, which can inform budget recommendation evaluation.
  contribution: "This systematic review provides a comprehensive synthesis of ML applications in credit scoring, offering a benchmark for selecting models and evaluation metrics for Odin's forecasting and classification modules. Its detailed analysis of ensemble and hybrid models directly informs the design of Odin's core algorithms for spending prediction and user profiling. The review's emphasis on interpretability and bias mitigation guides the development of trustworthy and fair recommendation and anomaly detection systems. Furthermore, its discussion of alternative data sources and privacy concerns offers a framework for responsibly expanding Odin's data inputs while maintaining user trust and regulatory compliance."
  directly_justifies:
    - "Ensemble and hybrid models consistently outperform single classifiers in credit scoring tasks."
    - "Interpretability techniques like SHAP and LIME are essential for building trust in financial AI systems."
    - "Model evaluation should use a combination of metrics (AUC, F1, KS) to address the limitations of accuracy on imbalanced data."
    - "Addressing algorithmic bias is critical for ensuring fair and non-discriminatory credit decisions."
    - "Alternative data sources can enhance predictive accuracy, particularly for users lacking formal financial histories."
  limits:
    - "The review does not provide a direct comparative analysis to identify the single most effective model due to heterogeneity in datasets and evaluation metrics across studies."
    - "The review may have missed relevant studies published outside the selected four digital libraries or within the 2018-2024 timeframe."
    - "The focus on credit scoring may limit the direct applicability of all findings to broader personal finance management functions like budget optimization."
  mapping_rationale: "A systematic scan across all 12 functional domains was conducted. The domains 'Expense Categorization' (3.A, 3.B) and 'Behavioral Profiling' (5.A, 5.C) were flagged as contextual/medium because the review provides general ML classification methods, but not specific to expense taxonomy or dynamic user profiling. 'Existing Systems & Gaps' (4.A, 4.B) was deemed high and medium, respectively, as the review explicitly outlines the evolution and limitations of traditional scoring models, directly informing Odin's need to address PFMS gaps. The 'Spending Forecasting' domain (6.A, 6.B) received high and medium relevance due to the review's core focus on predictive modeling and mention of LSTM for sequential data. 'Anomaly Detection' (8.A, 8.B) was considered contextual as the review touches on outlier detection but does not detail specific algorithms for spending data. 'Data Privacy & User Trust' (10.A, 10.B) was flagged as medium and high because the review extensively discusses interpretability, privacy concerns with alternative data, and regulatory compliance (GDPR, IFRS 9), which are critical for user trust. 'System Evaluation' (12.A, 12.B, 12.C) was given high relevance due to the review's comprehensive analysis of evaluation metrics and algorithmic comparison, directly supporting Odin's testing and validation. The domain 'Filipino Cultural Context' was rejected as the paper is an international review with no specific focus on Philippine culture or practices. 'User Retention & Engagement' and 'Savings & Debt Management' were also rejected as the review does not address user engagement strategies or specific debt management techniques. The paper's overall relevance is high for guiding the selection of forecasting and classification algorithms, evaluation methodologies, and addressing interpretability and privacy challenges in Odin."
limitations:
  - "The review is limited to studies published between 2018 and 2024, potentially omitting older foundational work. [unacknowledged]"
  - "The search strategy was confined to only four online databases, which may have led to the omission of relevant studies from other sources. [unacknowledged]"
  - "A direct comparative analysis to identify the most effective model is lacking due to the heterogeneity in datasets and evaluation metrics used across the reviewed studies. [acknowledged]"
  - "Heterogeneity in datasets and evaluation metrics across studies complicates direct performance comparisons."
remember_this:
  - "Ensemble and hybrid models are the most effective for financial classification tasks."
  - "Interpretability is a critical challenge for building trust in ML-based financial systems."
  - "Using a combination of metrics like AUC and F1 is essential for evaluating models on imbalanced data."
  - "Alternative data can improve credit scoring accuracy but raises significant privacy concerns."
  - "Addressing algorithmic bias is fundamental to ensuring fairness in automated financial decisions."
```
