```yaml
paper_id: 10.3390/ai6110279
designation: international-algorithm-specific
title: Severity-Aware Drift Adaptation for Cost-Efficient Model Maintenance
authors: Shakhovska, K.; Pukach, P.
year: 2025
venue: AI
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 7.B
  - 12.B
tldr: A severity-aware framework quantifies data drift using KS, Wasserstein, and JS divergences, triggering incremental updates for moderate drift and full retraining for severe drift, reducing costs while maintaining model accuracy.
problem_and_motivation: Data distributions in real-world systems change over time, degrading model accuracy, yet existing drift-handling methods often retrain unnecessarily, incurring high computational costs. A principled way to distinguish drift severity and adapt proportionally is missing. This paper addresses that gap by introducing a severity-aware adaptation mechanism.
approach:
  - The framework maintains short-term and long-term windows over streaming data.
  - It computes a severity score as a weighted combination of KS, Wasserstein, and Jensen-Shannon divergences between window distributions.
  - Based on score thresholds, it applies no update, incremental fine-tuning, or full retraining.
  - Quantile transformation is tested as a lightweight preprocessing step to align new data to the historical baseline.
  - Experiments are conducted on salary, housing, and gas sensor datasets to evaluate drift detection and transformation effectiveness.
  - Time and memory complexity are analyzed, showing efficiency compared to ensemble methods like ROSE.
findings:
  - num: The KS statistic between 2023 and 2024 salaries decreased from 0.0559 to 0.0072 after quantile transformation.
  - num: Combined drift scores showed no drift for 2023 vs 2024, low drift for 2022 vs 2024, and significant drift for 2021 vs 2024 after normalization.
  - num: In the gas sensor dataset, 93% of features exhibited significant drift across batches.
  - The severity-aware policy reduces unnecessary retraining by responding proportionally to drift magnitude.
  - Subgroup-level analysis can reveal drift masked by pooled aggregation, as seen in housing data where 44 of 45 areas showed significant drift despite overall no drift.
key_figures_tables:
  - Figure 2: Salary trend over time with 95% CI → salaries increased, indicating temporal drift.
  - Figure 3: Boxplot of salary by year and experience level → drift magnitude varies by seniority.
  - Figure 6: Stacked bar of drift categories across gas sensor batches → significant drift dominates after early batches.
  - Table 6: Normalized combined scores for year comparisons → scores differentiate no, low, and significant drift.
  - Table 9: Top 5 most and least drifted features in gas data → identifies unstable sensors.
key_equations:
  - equation: d_m = m(P_s, P_l)
    explanation: Metric between short-term and long-term distributions.
  - equation: S = α d_KS + β d_W + γ d_JS
    explanation: Weighted aggregation of three drift metrics.
  - equation: x_new_transformed = F_old^{-1}(F_new(x_new))
    explanation: Quantile transformation maps new data to reference distribution.
definitions:
  - term: KS statistic
    definition: Maximum difference between two empirical cumulative distribution functions.
  - term: Wasserstein distance
    definition: Average displacement between two probability distributions.
  - term: Jensen-Shannon divergence
    definition: Symmetric and bounded measure of similarity between two distributions.
  - term: Quantile transformation
    definition: Non-parametric mapping that aligns the quantiles of one distribution to another.
critical_citations:
  - "[Gama et al., 2014] — Survey on concept drift adaptation."
  - "[Cano and Krawczyk, 2022] — ROSE ensemble for drifting imbalanced streams."
  - "[Yang et al., 2021] — Lightweight drift detection for IoT."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Provides a general model maintenance framework for predictive modules.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Directly addresses drift adaptation to preserve forecasting accuracy.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Drift affects anomaly detection; adaptation improves system robustness.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Offers algorithmic methods to adjust anomaly detection under distributional shifts.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Budget recommendations benefit from adaptive updates based on changing spending patterns.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: The evaluation methodology for drift severity can inform Odin's module assessments.
  contribution: The severity-aware drift adaptation framework can be integrated into Odin's spending forecasting module (6.B) to maintain prediction accuracy over time, as spending patterns drift. It also supports anomaly detection (8.B) by enabling dynamic adjustment of detection thresholds when distributional shifts occur, reducing false alarms. For budget recommendation (7.B), the framework provides a mechanism to update allocation constraints in response to evolving user expenses, improving personalization. The quantile transformation offers a lightweight preprocessing step to reduce distributional shifts before retraining, saving computational resources in Odin's real-time pipeline. Additionally, the evaluation approach (12.B) offers a methodology for assessing model maintenance strategies in Odin's algorithmic modules.
  directly_justifies:
    - Quantile transformation reduced the KS statistic from 0.0559 to 0.0072, effectively mitigating covariate drift.
    - The severity score enables selective adaptation, avoiding full retraining for minor drift and reducing computational cost.
    - Subgroup-level drift analysis can detect localized changes that pooled analysis misses, informing targeted model updates.
    - The framework's time complexity is O(d(w log w + b)), making it suitable for streaming environments.
  limits:
    - Datasets may not fully reflect real-world distributions, affecting metric stability.
    - Pooled analysis may mask subgroup-level drift, requiring stratified detection.
    - The method is sensitive to temporal window size; small windows produce noise, large windows obscure short-term shifts.
    - Small-sample effects can yield unreliable statistical outputs, overestimating drift.
    - Current implementation is restricted to continuous variables; categorical drift is not handled.
  mapping_rationale: All 12 functional domains and their associated topic codes were systematically scanned. The following domains were flagged as relevant: Spending Forecasting (6.A, 6.B) because the paper directly addresses model maintenance under data drift, which is critical for forecasting accuracy; Anomaly Detection (8.A, 8.B) because drift affects anomaly detection performance and the proposed adaptation improves robustness; Budget Recommendation (7.B) because budget suggestions must adapt to changing spending patterns; and System Evaluation (12.B) because the paper provides an evaluation framework for model updates. Relevance levels: 6.B and 8.B high, 6.A and 8.A medium, 7.B and 12.B medium. Borderline cases: the paper's drift detection could also relate to Behavioral Profiling (5.A) as user behavior changes over time, but it does not classify profiles, so it was rejected as low. Seasonal spending (2.B) was considered but the paper does not address seasonality specifically. Cultural practices (2.A) and expense categorization (3.A) were not relevant. Overall, the paper offers a general adaptation mechanism applicable to multiple Odin modules that rely on time-series data.
limitations:
  - Datasets may not fully reflect real-world distributions, affecting metric stability.
  - Pooled analysis may mask subgroup-level drift, requiring stratified detection.
  - The method is sensitive to temporal window size; small windows produce noise, large windows obscure short-term shifts.
  - Small-sample effects can yield unreliable statistical outputs, overestimating drift.
  - Current implementation is restricted to continuous variables; categorical drift is not handled. [unacknowledged]
remember_this:
  - Quantile transformation reduced KS statistic from 0.0559 to 0.0072.
  - Severity-aware adaptation avoids full retraining for minor drift, saving computational resources.
  - Subgroup-level drift analysis reveals localized changes masked by aggregate statistics.
  - The framework uses three complementary metrics to quantify drift severity robustly.
  - Lightweight preprocessing can delay costly retraining in streaming environments.
```