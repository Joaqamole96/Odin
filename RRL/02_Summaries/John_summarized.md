```yaml
paper_id: 9f7b8a6c-5d4e-3b2a-1f0e-9d8c7b6a5f4e
designation: international-algorithm-specific
title: Fair and Explainable Credit-Scoring under Concept Drift: Adaptive Explanation Frameworks for Evolving Populations
authors: John, S.
year: 2026
venue: Unknown
odin_topics:
  - 2.B
  - 5.B
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 12.B
tldr: Adaptive SHAP frameworks improve explanation stability and fairness in credit scoring under concept drift without reducing predictive accuracy.
problem_and_motivation: Static explainability methods like SHAP become unstable and potentially unfair when concept drift alters the data distributions underlying credit-scoring models. Existing adaptive learning research focuses on restoring predictive accuracy, leaving the explanation layer outdated and unreliable. A mechanism is needed to maintain interpretive consistency and fairness as borrower populations evolve.
approach:
  - Uses a multi-year lending dataset from 2015 to 2024 with demographic, financial, and socioeconomic features.
  - Employs XGBoost for predictive modeling and applies three adaptive SHAP variants for explanation: drift-weighted adjustment, sliding background sampling, and Ridge surrogate recalibration.
  - Benchmarks adaptive methods against static SHAP using metrics for predictive performance (AUC, F1), explanation stability (cosine, Kendall tau), and fairness (demographic parity).
  - Conducts robustness tests including counterfactual perturbations, background sensitivity analysis, and proxy-variable detection.
  - Uses paired bootstrap confidence intervals and paired t-tests to confirm statistical significance of improvements.
findings:
  - Static SHAP explanations showed high cosine stability (0.991-0.998) but moderate rank stability (Kendall tau = 0.758-0.912) under drift.
  - num: Adaptive Method B (sliding window) achieved the highest stability with cosine ≈ 0.995 and Kendall τ ≈ 0.89 across years.
  - num: Method B reduced demographic parity difference by approximately 0.026 (95% CI: -0.035, -0.016, p < 0.05) compared to baseline.
  - num: Default rates increased from ~15% in 2015 to over 23% in 2024, indicating label drift.
  - Counterfactual tests showed valid monotonic responses: decreasing credit score by 10% increased default probability by 0.05.
key_figures_tables:
  - Figure 1: Loan default rate by year shows an increase from 15% to 23% over the study period, confirming label drift.
  - Figure 2: PSI for annual_income and credit_score shows steady increase, indicating covariate drift.
  - Figure 5: DPD over time by model for race shows fairness fluctuates with data drift, especially during 2020-2021.
  - Figure 7: DPD before and after Method B recalibration demonstrates a clear reduction in disparity.
  - Figure 13: Counterfactual perturbations show monotonic response, validating model logic and explanation reliability.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: SHAP
    definition: SHapley Additive exPlanations; a game-theoretic approach to explain model predictions by assigning importance to features.
  - term: Concept Drift
    definition: A change in the underlying data distribution over time, which can degrade model accuracy and interpretability.
  - term: Demographic Parity Difference
    definition: A fairness metric measuring the difference in positive prediction rates across demographic groups.
  - term: XGBoost
    definition: Extreme Gradient Boosting; an ensemble machine learning algorithm widely used for its handling of nonlinear interactions.
critical_citations:
  - "[Lundberg and Lee, 2017] — Foundation for SHAP as the static explanation baseline."
  - "[Gama et al., 2014] — Defines concept drift and notes the research gap in adaptive explainability."
  - "[Barocas et al., 2023] — Emphasizes that fairness requires continuous attention in evolving systems."
  - "[Slack et al., 2020] — Highlights adversarial vulnerability of static explanation tools."
relevance:
  topics:
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: The dataset includes multi-year economic cycles and recessionary periods, which relate to cyclical patterns.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: medium
      justification: Addresses how borrower profiles and feature importance shift over time, directly informing profile dynamics.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly evaluates predictive performance (AUC, F1) of XGBoost in a dynamic credit-scoring context.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: The study's longitudinal setup and evaluation of explanation stability over time are relevant to forecasting.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: The robustness and proxy-variable detection methods are relevant to identifying anomalous or biased feature influences.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: The adaptive frameworks are designed to detect and adjust for distributional shifts, akin to anomaly detection.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: While not the primary focus, the fairness and stability analysis addresses aspects of responsible data use.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: The paper discusses how stable and fair explanations build user trust and support regulatory compliance.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Directly compares the evaluation of adaptive explanation modules against a static baseline using specific metrics.
  contribution: This paper provides a framework for evaluating and improving explanation stability in dynamic environments, which can inform Odin's approach to maintaining transparent and fair spending forecasts. The adaptive SHAP methods offer a way to recalibrate feature attributions as user behavior evolves, supporting Odin's behavioral profiling and anomaly detection modules. The emphasis on fairness and stability aligns with Odin's need to build user trust and comply with data privacy expectations.
  directly_justifies:
    - Static SHAP explanations become unstable under concept drift, requiring adaptive methods for reliable interpretation.
    - Adaptive explanation frameworks can improve fairness metrics without degrading predictive accuracy.
    - Sliding-window background sampling is an effective strategy for maintaining explanation stability over time.
  limits:
    - The analysis focuses primarily on single-attribute fairness rather than intersectional demographic factors.
    - The study does not test the framework on live, real-world banking data with missing or delayed information.
    - The computational cost of SHAP-based methods may limit scalability in real-time applications.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant for predictive modeling (6.A, 6.B) and algorithmic evaluation (12.B) because it directly benchmarks model and explanation performance in a dynamic environment. It was assigned medium relevance for behavioral profiling (5.B) due to its focus on feature importance shifts over time, and for anomaly detection (8.A, 8.B) through its robustness tests against distributional changes. The domains of data privacy (10.A) and user trust (10.B) were considered and assigned medium to low relevance as the paper discusses them conceptually but does not propose specific technical mechanisms for Odin. Cultural context (2.B) is contextual, as the dataset reflects economic cycles. The mapping rationale concludes that while the paper's primary domain is credit scoring, its methodologies for adaptive explanation, stability evaluation, and fairness recalibration are directly transferable to Odin's budget recommendation and behavioral forecasting modules.
limitations:
  - SHAP-based analysis is computationally heavy, which could hinder scalability and real-time use in Odin. [unacknowledged]
  - The fairness assessment focuses mainly on single attributes (race, gender) rather than the intersectional factors common in real-world scenarios. [acknowledged]
  - The study does not test the adaptive framework on live, real-world banking data with missing information or delayed updates. [acknowledged]
remember_this:
  - Adaptive SHAP methods stabilize explanations under concept drift without harming predictive accuracy.
  - Sliding-window background sampling provides the most consistent improvements in explanation stability.
  - num: Adaptive recalibration reduced demographic parity difference by 0.026 compared to baseline.
  - Explanation and fairness must be maintained dynamically as data and user behavior evolve.
  - Reliable explanations support both regulatory compliance and user trust in financial systems.
```