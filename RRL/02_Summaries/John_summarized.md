```yaml
paper_id: 10.48550/arXiv.2511.03807
designation: international-algorithm-specific
title: Fair and Explainable Credit-Scoring under Concept Drift: Adaptive Explanation Frameworks for Evolving Populations
authors: John, S.
year: 2026
venue: arXiv
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
tldr: Adaptive SHAP explanation methods maintain interpretability and fairness in credit-scoring models under concept drift without sacrificing predictive accuracy.
problem_and_motivation: Static explainability tools like SHAP fail under concept drift, producing unstable and potentially unfair explanations in dynamic credit environments. Existing drift adaptation focuses on predictive accuracy, leaving interpretive consistency and fairness unaddressed. This gap threatens regulatory compliance and user trust.
approach:
  - Data source: Synthetic multi-year credit dataset (2015-2024) with demographic, financial, and socioeconomic features.
  - Method: XGBoost baseline plus three adaptive SHAP variants: drift-weighted reweighting, sliding-window rebaselining, and Ridge surrogate calibration.
  - Evaluation setup: Expanding-window validation, yearly retraining, and longitudinal tracking of explanation stability and fairness.
  - Baselines: Static SHAP explanations compared against adaptive methods.
  - Metrics: Explanation stability (cosine, Kendall tau, Jaccard), fairness (DPD, EOD, equalized odds), and robustness tests.
findings:
  - num: PSI for annual_income reached 0.16 by 2019, confirming progressive covariate drift.
  - num: Default rates increased from ~15% in 2015 to over 23% in 2024.
  - num: Baseline AUC remained stable (0.63-0.66) despite drift, but explanation consistency degraded.
  - num: Method B reduced demographic parity difference by 0.026 (p < 0.05) without affecting AUC.
  - num: Method B and C achieved high explanation stability (cosine ≈ 0.995, Kendall τ ≈ 0.89).
  - num: Counterfactual perturbation: 10% decrease in credit_score increased default probability by 0.05.
  - Proxy variable detection identified race-associated features (p < 0.01; η² = 0.017-0.045).
key_figures_tables:
  - Figure 1: Loan default rate by year → default rate rose from 15% to 23% over 2015-2024.
  - Figure 2: PSI for annual_income and credit_score → PSI increased steadily, confirming drift.
  - Figure 3: JS divergence for race and gender → race/gender stable but Chi-square indicated significance.
  - Figure 4: Model test AUC over test years → AUC stable at 0.63-0.66.
  - Figure 5: DPD over time by model for race → DPD fluctuated, peaking during recession years.
  - Figure 6: EOD over time by model for race → EOD showed variability similar to DPD.
  - Figure 7: DPD before and after method B recalibration → DPD reduced significantly post-recalibration.
  - Figure 8: Explainability stability over time → stability metrics varied, motivating adaptive methods.
  - Figure 9: Top features by final test year → loan_amount, dti, credit_score were top predictors.
  - Figure 10: Kendall tau and Cosine similarity for adaptive methods → Methods B and C achieved highest stability.
  - Figure 11: Final year feature importance baseline vs. adaptive → adaptive methods showed more consistent feature rankings.
  - Figure 12: Number of harmful features detected by explainability method → adaptive methods reduced harmful proxy features.
  - Figure 13: Mean probability change from counterfactual perturbations → monotonic directional responses validated logic.
  - Figure 14: SHAP background size sensitivity test → adaptive methods showed improved consistency.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: SHAP
    definition: SHapley Additive exPlanations, a game-theoretic method for explaining model predictions.
  - term: XAI
    definition: Explainable Artificial Intelligence.
  - term: PSI
    definition: Population Stability Index, a measure of distributional shift in features.
  - term: JS
    definition: Jensen-Shannon divergence, a measure of similarity between probability distributions.
  - term: KS
    definition: Kolmogorov-Smirnov test, a nonparametric test for distribution equality.
  - term: DPD
    definition: Demographic Parity Difference, a fairness metric measuring equal positive prediction rates.
  - term: EOD
    definition: Equal Opportunity Difference, a fairness metric measuring equal true positive rates.
critical_citations:
  - "[Widmer and Kubat, 1996] — Established concept drift as a core challenge in learning systems."
  - "[Gama et al., 2014] — Surveyed drift adaptation, noting the gap in maintaining interpretability."
  - "[Lundberg and Lee, 2017] — Introduced SHAP, the static baseline used in this study."
  - "[Barocas et al., 2023] — Emphasized fairness as a continuous, context-dependent requirement."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Models financial behavior via credit risk prediction, capturing changing borrower profiles.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: contextual
      justification: Treats evolving borrower characteristics as a drift problem, relevant to profile dynamics.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Uses XGBoost for credit risk classification, but focuses on explanation, not profiling.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Concept drift detection can identify anomalies in spending behavior over time.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Adaptive SHAP methods detect drift-induced changes in feature importance, akin to anomaly shifts.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Proxy variable detection addresses bias, which has privacy and fairness implications.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Stable, fair explanations directly support user trust and transparency.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a robust evaluation framework for explanation stability, fairness, and robustness.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Benchmarks adaptive SHAP variants against static baselines using multiple metrics.
  contribution: "This paper contributes an adaptive explainability framework for credit-scoring, directly applicable to Odin's expense forecasting and anomaly detection modules. The sliding-window SHAP rebaselining (Method B) offers a practical technique for maintaining explanation stability under changing user spending patterns. The fairness recalibration mechanism provides a template for Odin's budget recommendation module to adjust for demographic disparities. The evaluation metrics (cosine, Kendall tau, Jaccard) and robustness tests offer a blueprint for assessing Odin's algorithmic modules. Overall, the adaptive explanation framework ensures that Odin's recommendations remain interpretable and fair as user financial behavior evolves."
  directly_justifies:
    - "Adaptive SHAP explanations maintain stability under concept drift, supporting reliable anomaly detection."
    - "Sliding-window background sampling reduces explanation volatility, aligning with mobile-first design needs."
    - "Fairness recalibration can be integrated into budget recommendation to prevent disparate impact."
    - "Proxy variable detection helps identify hidden biases in spending categories and user attributes."
  limits:
    - "Study uses synthetic data, not real Filipino spending data."
    - "Fairness analysis focuses on single attributes, not intersectional demographics."
    - "SHAP computational cost may hinder real-time mobile deployment."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant to Behavioral Profiling (5.A, 5.B, 5.C) because it models evolving borrower risk profiles, though it does not explicitly classify financial personality types. Anomaly Detection (8.A, 8.B) was selected because concept drift detection and adaptive explanation stability are directly relevant to identifying shifts in spending behavior that could indicate anomalies. Data Privacy & User Trust (10.A, 10.B) were chosen because stable, fair explanations build user trust and proxy variable detection addresses bias, which has privacy implications. System Evaluation (12.A, 12.B) received high relevance due to the paper's comprehensive evaluation framework for algorithmic modules, including stability, fairness, and robustness metrics. Domains like Expense Categorization (3.A, 3.B, 3.C), Spending Forecasting (6.A, 6.B), and Budget Recommendation (7.A, 7.B, 7.C, 7.D) were considered but rejected because the paper focuses on credit risk, not expense tracking or budget allocation. The paper's adaptive explanation framework and evaluation methodology are highly relevant to Odin's need for interpretable and fair algorithms in a dynamic financial environment."
limitations:
  - "SHAP analysis is computationally heavy, impacting scalability and real-time use. [unacknowledged]"
  - "Fairness assessment focuses on single attributes, not intersecting demographic factors. [unacknowledged]"
  - "The dataset is synthetic and may not fully capture real-world credit dynamics."
  - "The study does not address how to integrate adaptive explanations into a production mobile app."
remember_this:
  - "Adaptive SHAP methods stabilize explanations under concept drift."
  - "Sliding-window rebaselining improved fairness by reducing demographic parity difference by 0.026."
  - "Explanation stability remained high with cosine similarity ≈ 0.995 and Kendall τ ≈ 0.89."
  - "Explainability can evolve alongside data without sacrificing predictive accuracy."
  - "Adaptive frameworks support ongoing fairness and transparency in dynamic systems."
```