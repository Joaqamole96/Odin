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
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 8.C
  - 12.A
  - 12.B
tldr: An adaptive fusion framework integrates baseline machine learning models with dynamic adaptation to counter concept drift, achieving 95.0% accuracy in credit scoring under distributional shifts.
problem_and_motivation: Static credit scoring models degrade as borrower behavior and economic conditions change, exposing lenders to financial and regulatory risks. Existing adaptive solutions are designed for advanced economies and lack effectiveness in developing contexts. A robust framework is needed to detect and adapt to drift in dynamic, resource-constrained environments.
approach:
  - Used the German Credit dataset and introduced three synthetic drift scenarios.
  - Benchmarked vanilla models including CART, Naïve Bayes, Random Forest, and XGBoost.
  - Developed adaptive strategies: model retraining, windowing, ensemble learning, and a proposed Adaptive Fusion algorithm.
  - Adaptive Fusion dynamically weights outputs from three Random Forest models for real-time prediction.
  - Evaluated performance using accuracy, precision, recall, F1-score, and ROC-AUC.
findings:
  - num: The Adaptive Fusion, Ensemble, and Retrained Random Forest models each achieved an accuracy of 95.0%.
  - num: Adaptive Fusion maintained a precision of 0.9275, recall of 0.9645, and F1-score of 0.9426.
  - num: ROC-AUC values exceeded 0.96 for the best-performing adaptive models.
  - num: The method outperformed the state-of-the-art DGHNL model, which achieved 94.60% accuracy and an AUC of 0.9360.
  - Adaptive Fusion proved the most robust solution, enabling continuous adaptation to evolving patterns.
  - The windowed learning approach underperformed, showing limitations in capturing long-term behavioral shifts.
  - The ensemble approach performed well but was slightly less stable than Adaptive Fusion.
key_figures_tables:
  - Figure 3: Vanilla model performance comparison on original dataset → Random Forest was the best baseline.
  - Figure 4: ROC-AUC for adaptive retraining on drift scenarios → ROC-AUC remained high, demonstrating effective adaptation.
  - Figure 5: Model evaluation results on adaptive strategies → Adaptive Fusion and Retrained Random Forest were top performers.
  - Table 1: Vanilla model performance metrics on original dataset → Random Forest achieved the highest accuracy (0.77) and ROC-AUC (0.768).
key_equations:
  - equation: X_d = X_n + 5
    explanation: Simulates temporal shift by increasing all age values.
  - equation: New credit amount = Original credit amount + N(0,1000)
    explanation: Adds Gaussian noise to model variability in loan sizes.
  - equation: p_{final} = w_0 p_0 + w_r p_r + w_w p_w
    explanation: Fuses model probabilities via dynamically updated weights.
definitions:
  - term: Concept drift
    definition: A change in the data distribution over time that degrades model performance.
  - term: Adaptive fusion
    definition: An algorithm that dynamically integrates multiple model outputs based on recent performance.
  - term: ROC-AUC
    definition: A metric for a model's ability to distinguish between classes, useful for drift detection.
critical_citations:
  - "[Museba, 2023] — Supports effectiveness of heterogeneous ensembles in credit scoring."
  - "[Krempl et al., 2000] — Advocates for explicit drift modelling in financial data."
  - "[Barddal et al., 2020] — Demonstrates data stream learners outperform static models."
relevance:
  topics:
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies static models' failure in dynamic environments.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: Discusses evolving borrower behavior leading to concept drift.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: contextual
      justification: Addresses adaptation to changing borrower characteristics over time.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: The adaptive fusion method is a classification approach for dynamic profiles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: The paper focuses on predictive modeling under distributional shifts.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Directly evaluates and proposes an algorithm for forecasting under drift.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Mentions fraud detection as an application domain.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Adaptive algorithms are applicable to detecting anomalies in spending.
    - code: 8.C
      name: Cold‑Start Baseline Strategies for Anomaly Detection
      relevance: medium
      justification: Transfer learning discussed for initial model building.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses standard metrics like accuracy and AUC for evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Compares multiple algorithmic modules like retraining, ensemble, and fusion.
  contribution: "The study introduces a novel Adaptive Fusion algorithm for credit scoring that dynamically integrates multiple models. This approach directly informs the design of Odin's budget recommendation and anomaly detection modules, which must also adapt to shifting spending patterns. The framework's use of retraining and windowing strategies provides a methodological blueprint for handling concept drift in forecasting. Its emphasis on maintaining model robustness under class imbalance is relevant for detecting rare but significant financial events. The evaluation framework based on accuracy, precision, recall, and F1-score offers a template for assessing Odin's algorithmic modules."
  directly_justifies:
    - "Adaptive Fusion can maintain high predictive accuracy under concept drift by dynamically reweighting model outputs."
    - "Retraining models on recent data is effective for adapting to long-term behavioral shifts."
    - "Ensemble methods offer a stable approach to handling data distribution changes without full retraining."
    - "Window-based approaches have limitations in capturing long-term trends."
  limits:
    - "The experimental evaluation is limited to a single dataset (German Credit). [unacknowledged]"
    - "The paper does not explore the impact of different drift types on real-world Filipino spending data. [unacknowledged]"
    - "The computational cost of the adaptive fusion algorithm in a real-time system is not detailed. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains 'Spending Forecasting' (6.A, 6.B) and 'Anomaly Detection' (8.A, 8.B, 8.C) were flagged as having high relevance because the paper directly addresses algorithms for predictive modeling and drift adaptation under changing data distributions, which is analogous to forecasting Filipino young professionals' spending and detecting anomalies. The 'Behavioral Profiling' domain (5.A, 5.B, 5.C) was assessed as medium to contextual, as it discusses evolving borrower behavior but does not build financial profiles in the Odin sense. 'Existing Systems & Gaps' (4.A, 4.B) was also considered medium, as the paper critiques static systems and provides a solution. The 'System Evaluation' domain (12.A, 12.B) was flagged as relevant due to its detailed performance analysis. Other domains such as 'Filipino Cultural Context', 'Budget Recommendation', and 'User Retention' were considered but rejected as the paper does not address cultural practices, budget allocation constraints, or engagement mechanisms, being focused on a generic credit scoring algorithm. The overall relevance to Odin is significant for its algorithmic approaches to handling temporal data shifts."
limitations:
  - "The concept drift scenarios are synthetically generated, which may not fully represent real-world drifts."
  - "The study does not account for fairness and bias mitigation, which is critical for personal finance applications. [unacknowledged]"
  - "No data stream was used for real-time evaluation, limiting the assessment of the algorithm's true online performance. [unacknowledged]"
remember_this:
  - "Adaptive Fusion achieved 95.0% accuracy and an AUC exceeding 0.96 for credit scoring."
  - "Dynamic model integration outperformed static retraining and windowing techniques."
  - "Adaptive algorithms are essential for maintaining accuracy when data distributions change."
  - "Ensemble methods provide a stable, though less optimal, alternative to adaptive fusion."
  - "Concept drift detection is critical for forecasting personal finance behavior."
```