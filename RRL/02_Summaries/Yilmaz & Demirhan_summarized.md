```yaml
paper_id: 10.1016/j.asoc.2023.110020
designation: international-algorithm-specific
title: Weighted kappa measures for ordinal multi-class classification performance
authors: Yilmaz, A. E.; Demirhan, H.
year: 2023
venue: Applied Soft Computing
odin_topics:
  - 5.A
  - 12.A
  - 12.B
  - 12.C
  - 6.A
  - 8.B
tldr: Weighted agreement measures, especially Scott's quadratic weighted pi, reliably evaluate ordinal classifiers under imbalanced data compositions better than mainstream metrics.
problem_and_motivation: Evaluating ordinal multi-class classifiers is challenging with imbalanced data, as mainstream metrics like accuracy become unreliable. Existing metrics lack sensitivity to off-diagonal misclassifications critical for ordinal scales. There is no clear guidance on which metric best captures classifier performance across diverse data compositions.
approach:
  - Compared 37 metrics including agreement measures (weighted κ, π, α, BP, AC2) with six weighting schemes and mainstream metrics (accuracy, recall, precision, F1, MCC, IA).
  - Conducted first numerical study with synthetic confusion matrices generated under balanced, imbalanced, and extremely imbalanced compositions for three true accuracy levels (0.2, 0.5, 0.8).
  - Generated confusion matrices using product-multinomial sampling with varying misclassification scenarios (Case 1: equal class accuracy, Case 2: two classes accurate, Case 3: one class accurate).
  - Conducted second numerical study with 40 real datasets from social sciences, life sciences, engineering, and other fields, using SVMOP, WKNNOR, and KDLOR classifiers.
  - Evaluated metric sensitivity via ANOVA and Tukey's pairwise tests to distinguish between two similar classifiers with slightly different parameters.
findings:
  - num: Scott's quadratic weighted π and Cohen's quadratic weighted κ show the best MAE and RMSE for high/moderate true accuracy under imbalanced data.
  - num: For low true accuracy (0.2) and imbalanced data, unweighted AC2 outperforms other agreement metrics for sample sizes >50.
  - Mainstream metrics (except MCC) are generally insensitive to subtle performance differences between similar ordinal classifiers.
  - Scott's π metrics consistently distinguish between similar classifiers across data compositions and ordinal classification methods.
  - AC2 and BP metrics show similar behavior but are less sensitive than π for extremely imbalanced datasets.
key_figures_tables:
  - Figure 2: Mean metric values for SVMOP classifiers show weighted π metrics best distinguish SVMOP1 from SVMOP2.
  - Figure 3: For WKNNOR classifiers, BP metrics show highest sensitivity to small performance differences.
  - Figure 4: For KDLOR classifiers, weighted π metrics display strongest distinction between classifiers, surpassing MCC.
  - Table B.3: Tukey's pairwise comparison p-values show Scott's π consistently significant for SVMOP classifiers across data compositions.
  - Table B.4-B.6: Sensitivity of metrics to classifier differences is not impacted by the number of features (2-10 features tested).
key_equations:
  - equation: "A = (P_o - P_e(A)) / (1 - P_e(A))"
    explanation: General form for agreement coefficients.
  - equation: "P_o = ∑_{i,j=1}^R w_{ij} p_{ij}"
    explanation: Observed agreement weighted by cell weights.
  - equation: "MCC = (n_ii n - ∑ R_i=1 n_i. n_.i) / sqrt((n^2 - ∑_i n_i.^2)(n^2 - ∑_i n_.i^2))"
    explanation: Matthews correlation coefficient for multi-class.
definitions:
  - term: κ (Cohen's kappa)
    definition: Agreement measure assessing inter-rater reliability, used here for classifier performance.
  - term: π (Scott's pi)
    definition: Agreement measure assuming homogeneity of marginal distributions.
  - term: AC2 (Gwet's AC2)
    definition: Agreement measure adjusting for chance agreement using a chance-corrected formula.
  - term: BP (Brennan-Prediger)
    definition: Agreement measure assuming uniform marginal distributions.
  - term: α (Krippendorff's alpha)
    definition: Agreement measure without requiring marginal homogeneity.
  - term: TA
    definition: True accuracy, the ratio of correctly classified labels to total labels.
  - term: MAE
    definition: Mean absolute error, used to compare metric estimates to true accuracy.
  - term: RMSE
    definition: Root mean squared error, used to compare metric estimates to true accuracy.
  - term: SVMOP
    definition: Support vector machines with ordered partitions for ordinal classification.
  - term: WKNNOR
    definition: Weighted K-nearest neighbors for ordinal classification.
  - term: KDLOR
    definition: Kernel discriminant learning for ordinal regression.
  - term: IA
    definition: Informational agreement, a recently proposed metric based on mutual information.
critical_citations:
  - "[Delgado and Tibau, 2019] — Shows κ-measure differs from MCC and is unreliable for imbalanced data."
  - "[Chicco and Jurman, 2020] — MCC is more reliable than F1 and accuracy for binary classification."
  - "[Ferri et al., 2009] — κ-measure shows similar performance to F1 for large datasets but not for ordinal-specific evaluation."
  - "[Warrens, 2013] — Demonstrates theoretical relationship between unweighted κ and MCC."
  - "[Tran et al., 2020] — Describes weighted agreement measures for ordinal outcomes."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: low
      justification: Paper discusses classifier evaluation but not behavioral profiling specifically.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Directly addresses comparative evaluation of classification metrics, foundational for choosing Odin's evaluation framework.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides specific recommendations for metrics (e.g., Scott's π) that can evaluate Odin's algorithmic modules like forecasting or anomaly detection.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: high
      justification: Recommends metrics suitable for evaluating ordinal classifiers, applicable to budget recommendation (ordinal spending categories).
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: low
      justification: Touches on classifiers but not forecasting models specifically.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Evaluation of classifiers with imbalanced data is directly relevant to anomaly detection where anomalies are rare (imbalanced).
  contribution: "This paper provides a comprehensive evaluation framework for choosing performance metrics, which is directly applicable to Odin's system evaluation module (12.A, 12.B, 12.C). It recommends Scott's quadratic weighted π over MCC and F1 for ordinal classification, justifying its use for evaluating Odin's budget recommendation and anomaly detection components. The finding that AC2 performs best for low true accuracy in imbalanced data is critical for Odin's cold-start scenarios. The systematic comparison of 37 metrics offers a validated methodology for Odin's ongoing performance assessment."
  directly_justifies:
    - "Scott's quadratic weighted π is recommended for evaluating ordinal classifiers under imbalanced data."
    - "Mainstream metrics like accuracy are unreliable for extremely imbalanced data compositions."
    - "MCC and IA are not recommended for general use in ordinal classification evaluation."
    - "Unweighted AC2 performs best for low true accuracy in imbalanced datasets."
    - "Weighted agreement measures are more sensitive to off-diagonal misclassifications than mainstream metrics."
  limits:
    - "Synthetic data study limited to 3 ordinal classes and specific true accuracy levels; may not generalize to all real-world scenarios."
    - "Real data study uses only SVMOP, WKNNOR, and KDLOR; other ordinal classifiers might yield different metric sensitivities."
    - "Metric sensitivity assessed only by distinguishing two similar classifiers; not tested for absolute performance measurement accuracy."
    - "Number of features tested limited to 2-10; impact of high-dimensional data on metric sensitivity not explored."
  mapping_rationale: "A systematic scan across all 12 functional domains and their canonical topics was performed. Domains related to evaluation (12.A, 12.B, 12.C) were flagged as high relevance because the paper directly compares and recommends metrics for assessing ordinal classifiers, which is foundational for evaluating Odin's algorithmic modules. The forecasting domain (6.A) and anomaly detection (8.B) were flagged as medium/low relevance because while the paper discusses classifiers, it does not specifically address predictive modeling algorithms. The behavioral profiling topic (5.A) was considered but rejected as low because the paper focuses on evaluation metrics, not behavioral classification itself. Borderline cases included 7.B (Budget Recommendation) because evaluating classifiers is relevant to recommendation systems, but the paper does not discuss constrained optimization or user-specific recommendation generation. The paper's comprehensive metric comparison provides a rigorous methodology for choosing Odin's evaluation metrics, making it highly relevant for 12.A-C."
limitations:
  - "Theoretical relationship between unweighted κ and MCC only holds for symmetric confusion matrices; not general." [unacknowledged]
  - "Results based on synthetic data may not cover all real-world data compositions encountered in PFMS."
  - "Only three ordinal classification methods were used in the real data study; performance may vary with other methods."
  - "Computational cost of metrics not discussed; may be a concern for real-time applications." [unacknowledged]
remember_this:
  - Scott's quadratic weighted π reliably evaluates ordinal classifiers under imbalanced data.
  - Mainstream metrics like accuracy and F1 are insensitive to subtle performance differences.
  - Unweighted AC2 is best for low true accuracy in imbalanced datasets.
  - Weighted agreement measures outperform MCC and F1 for ordinal multi-class classification.
  - Evaluation metric choice significantly impacts classifier selection in PFMS modules.
```