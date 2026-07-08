```yaml
paper_id: 10.1007/s10994-025-06880-4
designation: international-algorithm-specific
title: Counterfactual ensembles for interpretable churn prediction: from real-world to privacy-preserving synthetic data
authors: Tonati, S.; Di Vece, M.; Giannotti, F.; Pellungrini, R.
year: 2025
venue: Machine Learning
odin_topics:
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 12.A
  - 12.B
tldr: An ensemble framework ranks counterfactual explanations for churn prediction using tunable metrics and aligns synthetic-data counterfactuals with real-data distributions via KL divergence minimization.
problem_and_motivation: Customer churn prediction models often lack interpretability, hindering actionable retention strategies. Counterfactual explanations can bridge this gap, but existing methods produce explanations of inconsistent quality. A systematic, domain-tailored evaluation and selection mechanism is needed to provide reliable and actionable insights.
approach:
  - Proposes k-CEM, an ensemble framework that integrates multiple counterfactual generation methods.
  - Ranks counterfactuals using a customizable scoring function balancing proximity, sparsity, plausibility, and diversity.
  - Supports two scenarios: in-house analysis with interactive weight tuning and outsourced analysis using synthetic data.
  - For privacy-preserving settings, aligns synthetic counterfactual distributions with real ones by minimizing average KL divergence.
  - Evaluates four churn datasets using LightGBM as the black-box model and compares linear vs. hierarchical scoring.
findings:
  - num: CTGAN achieved the highest synthetic data quality score (0.89 average) across four churn datasets.
  - The ensemble's top-ranked counterfactual generator varies significantly across datasets and user-defined priorities.
  - KL divergence minimization aligns synthetic and real counterfactual ensemble compositions in three of four datasets.
  - Cluster-based analysis shows a correlation between cluster centroid distance and counterfactual ensemble divergence.
  - At least one ensemble configuration maintains high Kendall's Tau correlation with SHAP feature rankings for each dataset.
key_figures_tables:
  - Figure 3: Proportion of selected counterfactual generators under different weight configurations → Method dominance varies by dataset and scoring function.
  - Figure 5: Membership ratios after KL minimization → Synthetic ensembles closely match real ensembles in most datasets.
  - Figure 6: Kendall-Tau heatmap vs SHAP → Ensemble configurations can match or exceed individual methods in feature alignment.
  - Figure 7: Cluster centroid vs counterfactual delta distance → Structural similarity correlates with counterfactual consistency.
  - Table 1: Model performance on churn datasets → LightGBM outperforms or matches XGBoost, RF, and MLP.
key_equations:
  - equation: Linear Score = \sum_{i} w_i m_i
    explanation: Weighted sum of metrics, lower is better.
  - equation: \bar{D}_{KL}(S \parallel R) = \frac{1}{n}\sum_{i=1}^{n} D_{KL}(Q_i \parallel P_i)
    explanation: Average KL divergence between synthetic and real feature distributions.
definitions:
  - term: Counterfactual explanation
    definition: Minimal feature changes needed to flip a model's prediction.
  - term: k-CEM
    definition: k-Counterfactual Ensemble Method for ranking and selecting counterfactuals.
  - term: KL divergence minimization
    definition: Optimization to align synthetic counterfactual distributions with real ones.
  - term: Proximity
    definition: Measures how close a counterfactual is to the original instance.
  - term: Plausibility
    definition: Measures how similar a counterfactual is to real data instances.
  - term: Sparsity
    definition: Fraction of features changed in a counterfactual.
  - term: Diversity
    definition: Dissimilarity among generated counterfactuals for a given instance.
critical_citations:
  - "[Guidotti & Ruggieri, 2021] — Proposed ensemble of counterfactual explainers."
  - "[Bodria et al., 2023] — Survey on XAI and counterfactual explanations."
  - "[Geiler et al., 2022] — Survey on churn prediction methods."
  - "[Lundberg & Lee, 2017] — SHAP for feature importance."
relevance:
  topics:
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Directly addresses privacy-preserving churn analysis using synthetic data.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Counterfactual explanations enhance interpretability and trust in predictions.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: Churn prediction and retention strategies are core engagement concerns.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: high
      justification: Provides a framework for generating actionable retention interventions.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Proposes a structured evaluation approach for counterfactual explanations.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Evaluates multiple counterfactual generation algorithms within an ensemble.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: Churn prediction is a related predictive task; methods could inform anomaly detection.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: contextual
      justification: Synthetic data generation for new users relates to cold-start profiling.
  contribution: The k-CEM framework provides a customizable, multi-metric selection mechanism for counterfactual explanations, directly applicable to Odin's engagement and retention modules. Its privacy-preserving extension using synthetic data and KL divergence alignment informs Odin's data privacy strategy when outsourcing analysis. The cluster-based coherence assessment offers a methodology for evaluating explanation fidelity across user segments, relevant to Odin's behavioral profiling. The framework's model-agnostic design supports integration with various predictive models within Odin's forecasting and anomaly detection pipelines.
  directly_justifies:
    - Counterfactual explanations can provide actionable retention recommendations for users predicted to churn.
    - Synthetic data can be used for privacy-preserving analysis while maintaining explanation fidelity.
    - A multi-metric scoring function allows tailoring explanations to specific business priorities.
    - Ensemble selection improves the robustness and interpretability of generated counterfactuals.
  limits:
    - Focus on churn prediction in subscription services, not directly on personal spending or PFMS.
    - Relies on the quality of synthetic data generators, which may not perfectly capture complex financial behaviors.
    - User study on expert interaction with the framework is identified as future work.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to User Retention & Engagement (11.A, 11.B) due to its focus on churn prevention, and to Data Privacy (10.A) for its synthetic data approach. Medium relevance was assigned to System Evaluation (12.A, 12.B) due to the proposed evaluation framework for explanations. Contextual relevance was noted for Anomaly Detection (8.B) as a related predictive task, and for Profile Dynamics (5.B) regarding synthetic data for cold-start scenarios. Domains such as Expense Categorization, Budget Recommendation, and Savings/Debt Management were rejected as the paper does not address financial allocation or spending patterns. Overall, the paper offers strong methodological insights for Odin's retention, explainability, and privacy-preserving analytics modules, though not directly addressing core PFMS functionalities.
limitations:
  - The method is validated on churn datasets, not personal finance spending data. [unacknowledged]
  - Synthetic data quality is critical and may degrade for highly complex or imbalanced financial data.
  - The framework's effectiveness for non-technical users requires further user study evaluation.
  - Computation overhead of running multiple counterfactual generators may be high for large-scale systems.
remember_this:
  - CTGAN achieved the highest synthetic data quality score of 0.89 across churn datasets.
  - An ensemble of counterfactual methods improves explanation robustness and interpretability.
  - KL divergence minimization aligns synthetic explanations with real data distributions.
  - User-defined scoring weights allow tailoring explanations to specific retention priorities.
  - Cluster similarity correlates with consistency of counterfactual explanations across data sources.
```