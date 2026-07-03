```yaml
paper_id: 10.47738/ijaim.v6i2.123
designation: international-algorithm-specific
title: Continual Learning for Human–AI Collaborative Learning Analytics under Behavioral Drift
authors: Rajulapati, A.; Sridevi, V.; Prasad, S. R.
year: 2026
venue: International Journal for Applied Information Management
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 8.C
  - 10.B
  - 12.A
  - 12.B
tldr: Continual learning with drift-aware updates improves predictive stability and fairness in semester-spanning educational analytics.
problem_and_motivation: Static predictive models degrade as student behavior evolves across semesters, yet deployed learning analytics rarely monitor or adapt to drift. This limits reliability for adaptive interventions and risks unfair outcomes under shifting distributions.
approach:
  - 14-semester longitudinal panel with 812–936 students and 18–21 courses per semester was constructed from LMS traces.
  - Drift was quantified using KL divergence on behavioral features including practice attempts, timeliness, and session regularity.
  - A drift-aware continual learning framework used replay buffers and parameter regularization to update models only when drift exceeded a threshold.
  - Semester-forward evaluation compared static, periodic retraining, and drift-aware continual policies on macro-F1, AUROC, and calibration.
  - Fairness was assessed via recall gaps across subgroups under drift.
findings:
  - num: Drift-aware continual learning achieved mean macro-F1 of 0.742 and worst-semester macro-F1 of 0.711, compared to 0.706 and 0.652 for static models.
  - num: Calibration error improved from 0.056 (static) to 0.039 under continual learning.
  - num: Risk precision and recall at fixed intervention capacity increased from 0.62 to 0.69 and 0.48 to 0.56.
  - num: Mean subgroup recall gap was reduced from 0.118 to 0.082.
  - Drift concentrated in practice attempts, submission timeliness, and session regularity, with a regime shift mid-sequence.
key_figures_tables:
  - Figure 7: Predictive performance over semesters → Drift-aware continual learning maintains flatter macro-F1 trajectory than static or periodic retraining.
  - Figure 8: Calibration error across weeks → Continual learning reduces miscalibration spikes during drift episodes.
  - Figure 9: Subgroup recall gap across semesters → Continual learning stabilizes and reduces recall disparities.
  - Table 7: Aggregate performance summary → Drift-aware continual learning has highest mean (0.742) and worst-semester (0.711) macro-F1.
  - Table 9: Subgroup error summary → Continual learning yields lowest mean recall gap (0.082) and max gap (0.121).
key_equations:
  - equation: D_KL(P_t || P_{t+1}) = \sum_k P_t(k) \log \frac{P_t(k)}{P_{t+1}(k)}
    explanation: KL divergence quantifies behavioral drift magnitude between consecutive semesters.
  - equation: \min_\theta L_{t+1}(\theta) + \lambda \sum_j \omega_j (\theta_j - \theta_{t,j})^2
    explanation: Continual learning objective combines current loss with parameter regularization.
  - equation: m \pm 1.96 \frac{s_m}{\sqrt{K}}
    explanation: Confidence interval for mean performance across evaluated semesters.
definitions:
  - term: Concept Drift
    definition: Change in joint distribution of inputs and targets over time.
  - term: Continual Learning
    definition: Sequential model updating that mitigates catastrophic forgetting via replay or regularization.
  - term: Semester-Forward Evaluation
    definition: Training on past semesters and testing on future semesters to simulate deployment.
  - term: Expected Calibration Error (ECE)
    definition: Mean absolute difference between predicted probabilities and observed frequencies.
  - term: Replay Buffer
    definition: Curated memory of prior samples used to retain historical knowledge during updates.
critical_citations:
  - "[Gama et al., 2014] — Foundational survey on concept drift adaptation strategies."
  - "[Lu et al., 2018] — Framework for drift detection and adaptation as a lifecycle problem."
  - "[Delange et al., 2021] — Comprehensive survey of continual learning approaches."
  - "[Deho et al., 2024] — Shows dataset drift impacts fairness in learning analytics."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Behavioral drift monitoring parallels financial profile evolution.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: Semester-to-semester drift mirrors cold-start challenges in financial behavior modeling.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: contextual
      justification: Classification under drift is addressed but not specific to financial profiles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly addresses maintaining predictive accuracy under evolving behavioral patterns.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Drift-aware updating and replay strategies are applicable to sequential financial data.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Drift-aware calibration improves risk ranking, analogous to anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Framework for detecting distributional shifts can be adapted for spending anomalies.
    - code: 8.C
      name: Cold‑Start Baseline Strategies for Anomaly Detection
      relevance: contextual
      justification: Replay buffers provide a retention mechanism relevant to cold-start baselines.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: Mentions trust via stable interpretability and reduced alert volatility.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Semester-forward protocol and rolling evaluation are applicable to PFMS evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Detailed comparison of static, periodic, and drift-aware continual learning modules.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: contextual
      justification: Evaluation methodology is general and not specific to budget recommendation.
  contribution: The paper provides a drift-aware continual learning framework that directly informs Odin's forecasting module by demonstrating how to maintain predictive stability under behavioral change. Its rigorous semester-forward evaluation protocol offers a template for assessing Odin's algorithmic modules over time. The fairness analysis under drift validates the importance of monitoring subgroup disparities, which is relevant to Odin's behavioral profiling and anomaly detection. The replay-based retention mechanism offers a practical approach to handling cold-start issues in sequential spending data.
  directly_justifies:
    - "Drift-aware updating stabilizes predictive performance under evolving behavioral patterns."
    - "Continual learning with replay buffers reduces catastrophic forgetting in sequential domains."
    - "Fairness disparities can widen under drift, necessitating monitoring of subgroup recall gaps."
    - "Calibration error should be tracked alongside accuracy to ensure reliable risk scores."
    - "Selective adaptation based on drift thresholds balances robustness with operational overhead."
  limits:
    - "The study is situated in educational analytics, not personal finance, so behavioral constructs differ."
    - "The dataset is institutional and may not generalize to individual spending behavior."
    - "Only semester-level drift is analyzed; finer-grained drift patterns remain unexplored."
    - "The framework assumes labeled outcomes are available per semester, which may not hold for financial data."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes flagged Forecasting, Anomaly Detection, and Evaluation as most relevant. Under Forecasting (6.A, 6.B), the paper directly informs sequential modeling under drift. For Anomaly Detection (8.A, 8.B), the calibration and risk ranking improvements are analogous to anomaly scoring stability. Evaluation (12.A, 12.B) benefits from the semester-forward protocol and ablation analysis. Behavioral Profiling (5.A, 5.B) is medium relevance due to drift dynamics, though the behavioral features differ. User Trust (10.B) is low relevance, mentioned only indirectly via stability. Domains related to Filipino cultural context, expense categorization, existing systems, mobile design, privacy, retention, savings, and debt management were not addressed. The paper is thus primarily methodological, offering transferable techniques for adaptation and evaluation in dynamic behavioral domains.
limitations:
  - "Educational context may not map directly to personal finance behavior. [unacknowledged]"
  - "The study does not address individual-level heterogeneity beyond subgroup analysis. [unacknowledged]"
  - "Deployment constraints such as real-time latency or mobile-first concerns are not discussed. [unacknowledged]"
  - "The privacy-preserving aspects are limited to pseudonymization and access control. [unacknowledged]"
remember_this:
  - "Drift-aware continual learning improves worst-semester macro-F1 from 0.652 to 0.711."
  - "Calibration error reduced from 0.056 to 0.039 under drift-aware updating."
  - "Mean subgroup recall gap decreased from 0.118 to 0.082 with continual learning."
  - "Intermediate drift thresholds balance robustness with update frequency."
  - "Replay buffers of moderate size provide near-peak performance with low overhead."

```