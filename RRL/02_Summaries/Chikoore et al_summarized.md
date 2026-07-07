```yaml
paper_id: 10.1109/ACCESS.2026.3703181
designation: international-algorithm-specific
title: Adaptive Credit Scoring Model With Concept Drift Detection and Adaptation Technique for a Dynamic Environment
authors: Chikoore, R.; Ojo, S. O.; Kogeda, O. P.
year: 2026
venue: IEEE Access
odin_topics:
  - 4.B
  - 5.A
  - 5.C
  - 6.A
  - 8.A
  - 12.B
  - 13.B
tldr: An adaptive credit scoring framework integrating multiple ML models with dynamic adaptation strategies addresses concept drift in developing economies, achieving superior predictive performance.
problem_and_motivation: Traditional static credit scoring models lack drift detection and adaptation, causing performance degradation in dynamic economic conditions. Existing adaptive approaches are developed for advanced economies and are not suited to developing contexts, necessitating a framework tailored to such environments.
approach:
  - The German Credit dataset was used with simulated drifts: feature distribution shift, noise addition, and class distribution change.
  - Four vanilla models (CART, Naive Bayes, Random Forest, XGBoost) were benchmarked; Random Forest was selected as baseline.
  - Four adaptation strategies were implemented: retraining on drifted data, sliding window learning, soft voting ensemble, and adaptive fusion.
  - Adaptive fusion dynamically weights outputs from original, retrained, and windowed models with weights summing to one.
  - Evaluation metrics include accuracy, precision, recall, F1-score, and ROC-AUC.
findings:
  - num: Retrained Random Forest, Ensemble, and Adaptive Fusion achieved 95.0% accuracy, 0.9275 precision, 0.9645 recall, 0.9426 F1, and ROC-AUC >0.96.
  - num: Adaptive Fusion outperformed state-of-the-art DGHNL (94.60% accuracy, AUC 0.9360).
  - Adaptive Fusion demonstrated the most robust performance across all drift scenarios with minimal degradation.
  - Ensemble approach was consistently second best, while windowing underperformed in recall and F1.
  - Batch retraining yielded reasonable accuracy but slower adaptation compared to fusion.
key_figures_tables:
  - Table 1: Vanilla model performance on original dataset → Random Forest highest at 0.77 accuracy.
  - Figure 3: Bar chart of vanilla model metrics → Random Forest and XGBoost outperform others.
  - Figure 4: ROC-AUC for adaptive retraining → Shows AUC >0.96 for top strategies.
  - Figure 5: ROC-AUC for adaptive windowing → Lower performance than fusion.
  - Figure 6: ROC-AUC for ensemble and adaptive fusion → Adaptive fusion highest and most stable.
key_equations:
  - equation: X_d = X_n + 5
    explanation: Feature distribution shift by aging all instances by 5 years.
  - equation: N(0, 1000) noise added to credit amount
    explanation: Simulates random fluctuations in loan sizes.
  - equation: f(x) = (1/(σ√(2π))) e^(-(x-µ)^2/(2σ^2)) with σ=1000
    explanation: Gaussian distribution for noise addition.
  - equation: P'(C_i) = (w_i · P(C_i)) / (Σ_j w_j · P(C_j))
    explanation: Weighted class probability to simulate class distribution drift.
  - equation: p_final = w_0*p_0 + w_r*p_r + w_w*p_w, with sum w=1
    explanation: Adaptive fusion combines predictions from three models.
definitions:
  - term: Concept drift
    definition: Change in data distribution over time that degrades model performance.
  - term: Adaptive fusion
    definition: Dynamic weighting of multiple model outputs to adapt to drift.
  - term: Population drift
    definition: Shift in the underlying characteristics of the borrower population.
  - term: ROC-AUC
    definition: Area under the receiver operating characteristic curve, measures classification performance.
  - term: DGHNL
    definition: Deep Genetic Hierarchical Network of Learners, a state-of-the-art credit scoring model.
critical_citations:
  - "[Liu et al., 2021] — Introduced diverse instance-weighting ensemble for drift adaptation."
  - "[Nikolaidis and Doumpos, 2022] — Adaptive credit scoring using local regions of competence."
  - "[Museba, 2023] — Adaptive heterogeneous ensemble for credit scoring."
  - "[Barddal et al., 2020] — Data stream classification applied to credit scoring."
relevance:
  topics:
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Paper identifies limitations of static models in dynamic environments.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Credit scoring classifies borrowers based on financial behavior.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Uses ML classifiers to categorize credit risk, directly relevant to profile classification.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Credit scoring is a form of predictive modeling in finance.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Mentions fraud detection but primary focus is credit scoring.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Extensive evaluation of adaptive algorithms with multiple metrics.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: medium
      justification: Credit scoring informs lending decisions, relevant to debt management.
  contribution: The adaptive fusion technique can inform Odin's spending forecasting module by providing a method to combine multiple models to adapt to shifting spending patterns. The evaluation metrics and methodology can be used to assess Odin's classification modules. The paper's treatment of concept drift and adaptation strategies is directly applicable to Odin's anomaly detection component, which must handle evolving user behavior. The emphasis on developing economy contexts aligns with Odin's target demographic, justifying the adoption of such adaptive methods.
  directly_justifies:
    - Adaptive models that dynamically fuse multiple classifiers outperform static models in dynamic environments.
    - Retrained models achieve high accuracy but adaptive fusion offers similar performance with lower computational cost.
    - Ensemble methods provide robust performance without full retraining, balancing accuracy and efficiency.
  limits:
    - Results are based on a single dataset (German Credit) with simulated drifts, not real streaming data.
    - The study does not address fairness and bias in credit scoring beyond mentioning it.
    - Generalizability to other developing economy contexts beyond South Africa may be limited.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant to the following domains: Existing Systems & Gaps (4.A, 4.B) because it discusses limitations of static credit scoring models; Behavioral Profiling & Classification (5.A, 5.C) as it uses ML to classify borrowers into risk categories; Predictive Modeling (6.A) as credit scoring is a form of predictive modeling; Anomaly Detection (8.A) as it touches on fraud detection and risk identification; System Evaluation (12.A, 12.B) as it provides extensive model evaluation; and Savings & Debt Management (13.B) as credit scoring is integral to debt management. Specific topic codes selected: 4.B (medium), 5.A (medium), 5.C (high), 6.A (medium), 8.A (low), 12.B (high), 13.B (medium). Borderline cases: The paper's focus on concept drift could also relate to 6.B (forecasting algorithms) and 8.B (anomaly detection algorithms), but these were rejected because the paper does not deal with sequential spending data or specific anomaly detection algorithms; it is primarily classification. The topics 3.A, 3.B, 3.C were considered but rejected as the paper does not address expense categorization. 7.A-D were rejected as it does not address budgeting. 9.A-B, 10.A-B, 11.A-B were rejected as they are not addressed. Overall, the paper provides a valuable adaptive modeling approach that can inform Odin's classification, evaluation, and adaptation strategies, with high relevance to model evaluation and classification approaches.
limitations:
  - The study relies on simulated drift scenarios rather than real-world streaming data.
  - Only the German Credit dataset is used, limiting generalizability.
  - Fairness and bias are mentioned but not systematically evaluated. [unacknowledged]
remember_this:
  - Adaptive Fusion achieved 95.0% accuracy and ROC-AUC >0.96 in credit scoring.
  - Dynamic fusion of multiple models is more robust to concept drift than retraining alone.
  - The study demonstrates the need for drift-aware models in developing economy contexts.
  - Ensemble and adaptive strategies maintain performance under data distribution shifts.
```