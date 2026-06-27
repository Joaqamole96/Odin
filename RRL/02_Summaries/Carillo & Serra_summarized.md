```yaml
paper_id: 10.29020/nybg.ejpam.v18i4.6875
designation: local-algorithm-specific
title: Optimized Nonlinear Grey Bernoulli Model for Nowcasting the Philippine Gross Domestic Product
authors: Carillo, S. K.; Serra, I. J.
year: 2025
venue: European Journal of Pure and Applied Mathematics
odin_topics:
  - 2.B
  - 6.A
  - 6.B
  - 7.D
  - 8.B
  - 12.B
tldr: PSO-optimized NGBM(1,1) achieved the lowest out-of-sample MAPE of 5.45% for Philippine GDP nowcasting, outperforming benchmark grey models.
problem_and_motivation: Quarterly GDP data are released with significant delays, disrupting planning for stakeholders. Existing grey models often struggle with parameter estimation in nonlinear systems, limiting forecast accuracy for the Philippines.
approach:
  - Data consists of quarterly Philippine GDP figures from 2021 Q1 to 2024 Q4, sourced from the Philippine Statistics Authority.
  - A harmonic regression simulation with a 70/30 training-testing split was used to determine the optimal data partitioning scheme.
  - The NGBM(1,1) model was optimized using Particle Swarm Optimization (PSO) to minimize out-of-sample MAPE.
  - An alternative optimization strategy using an exponential background value was also implemented for comparison.
  - Performance was evaluated against standard GM(1,1) and NGBM(1,1) benchmarks using out-of-sample MAPE and RMSE.
findings:
  - num: PSO-NGBM(1,1) achieved the lowest out-of-sample MAPE of 5.45% and RMSE of 362,077.8.
  - num: After seasonal adjustment, forecasting accuracy improved dramatically, with MAPE values falling below 1% for all models.
  - The PSO algorithm converged rapidly, stabilizing after approximately 30 iterations.
  - The exponential background value offered a modest advantage only for data with highly pronounced cyclical patterns.
  - PSO-NGBM(1,1) demonstrated superior generalization, maintaining lower out-of-sample errors than models with better in-sample fit.
key_figures_tables:
  - Table 1: Forecast accuracy grades based on MAPE → Provides benchmark for interpreting model performance.
  - Table 2: Best-performing models under 70/30 split → PSO-NGBM(1,1) dominated most simulation scenarios.
  - Figure 1: Convergence plot of PSO for NGBM(1,1) → Shows efficient optimization reaching near-optimal solution in ~30 iterations.
  - Table 5: Forecast results of all models → PSO-NGBM(1,1) had lowest out-of-sample MAPE and RMSE.
  - Figure 4: Seasonal-trend decomposition of Philippine GDP → Confirms strong seasonal pattern with Q1 decline and Q4 surge.
key_equations:
  - equation: MAPE = (1/(n-1)) \sum_{t=2}^n |(x^{(0)}(t) - \hat{x}^{(0)}(t)) / x^{(0)}(t)| \times 100\%
    explanation: Out-of-sample percentage error metric minimized by PSO.
  - equation: \hat{x}^{(1)}(k) = \left[ x^{(1)}(1)^{(1-m)} - \frac{b}{a} \right] e^{-a(1-m)(k-1)} + \frac{b}{a}
    explanation: Time response function for NGBM(1,1) AGO sequence.
  - equation: y(t) = \beta_0 t + \beta_1 \cos(\gamma t) + \beta_2 \sin(\gamma t), \gamma = 2\pi/4
    explanation: Harmonic regression for quarterly cycle simulation.
definitions:
  - term: NGBM(1,1)
    definition: Nonlinear Grey Bernoulli Model, a grey systems model incorporating a power index for nonlinearity.
  - term: PSO
    definition: Particle Swarm Optimization, a metaheuristic algorithm for parameter optimization.
  - term: MAPE
    definition: Mean Absolute Percentage Error, a scale-independent forecast accuracy metric.
  - term: RMSE
    definition: Root Mean Square Error, an absolute forecast error metric in original units.
  - term: AGO
    definition: Accumulated Generating Operation, a data transformation in grey models that smoothens sequences.
critical_citations:
  - "[Chen et al., 2006] — Introduced the NGBM(1,1) model framework."
  - "[Cheng et al., 2021] — Proposed exponential background value optimization method."
  - "[Zhou et al., 2008] — Applied PSO to optimize NGBM(1,1) parameters."
relevance:
  topics:
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: Paper analyzes seasonal patterns in Philippine GDP, applicable to spending cycles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly benchmarks forecasting models for economic time series.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Compares NGBM(1,1) variants and GM(1,1) on quarterly sequential data.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: contextual
      justification: Optimization strategies for parameter estimation are analogous to constraint handling.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Nowcasting detects deviations from expected trends, similar to anomaly detection.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides a rigorous evaluation framework using MAPE and RMSE for forecasting modules.
  contribution: "This paper demonstrates that PSO-optimized NGBM(1,1) provides a robust forecasting module for Odin's spending prediction engine. The seasonal decomposition approach directly informs how Odin should handle cyclical spending patterns in the Philippines. The comparative evaluation framework (MAPE, RMSE) can be adopted for Odin's algorithm testing. The finding that optimization techniques outperform background value adjustments guides Odin's choice of parameter tuning methods. Furthermore, the dramatic improvement after seasonal adjustment validates Odin's need for explicit seasonal modeling in its forecasting pipeline."
  directly_justifies:
    - "PSO optimization significantly improves forecasting accuracy over standard grey models."
    - "Seasonal adjustment reduces MAPE from over 5% to below 1% for quarterly data."
    - "70/30 train-test split is more effective than 80/20 for this data size and periodicity."
    - "Exponential background value offers limited benefit compared to PSO optimization."
  limits:
    - "The study uses only 16 quarterly observations, limiting generalizability for longer-term forecasts."
    - "None of the models fully captured sharp quarterly fluctuations, indicating a need for explicit seasonal components."
    - "Seasonal adjustment was applied as post-modeling analysis, not integrated into the grey models themselves [unacknowledged]."
  mapping_rationale: "A systematic scan across all 12 functional domains identified three domains with strong relevance: Spending Forecasting (6.A, 6.B) due to the paper's primary focus on GDP nowcasting, System Evaluation (12.B) due to the rigorous comparative methodology, and Anomaly Detection (8.B) because nowcasting inherently detects deviations from expected trends. The Filipino Cultural Context domain (2.B) was flagged as medium relevance because the paper analyzes seasonal patterns in Philippine data, which directly parallels spending cycles. The Algorithmic Optimization domain (7.D) was marked contextual as parameter optimization is analogous to constraint handling. Domains such as Expense Categorization (3.A-C), Behavioral Profiling (5.A-C), and Mobile Design (9.A-B) were considered and rejected as the paper contains no relevant citeable claims. The Budget Recommendation domain (7.A-C) was rejected despite optimization being mentioned, as the paper does not address allocation or constraint management. Overall, the paper is highly relevant to Odin's forecasting and evaluation modules but provides only indirect support for user-facing features."
limitations:
  - "Limited dataset size (16 quarterly observations) constrains model training."
  - "None of the grey models fully captured short-term volatility in GDP."
  - "Seasonal patterns were handled via preprocessing rather than integrated into the model."
  - "Statistical significance of performance differences between models was not tested [unacknowledged]."
remember_this:
  - "PSO-optimized NGBM(1,1) achieved a 5.45% out-of-sample MAPE for Philippine GDP."
  - "Seasonal adjustment reduced forecasting errors from over 5% to under 1%."
  - "PSO optimization outperformed exponential background value methods in forecast accuracy."
  - "Grey models show promise for short-term forecasting in data-constrained environments."
  - "Explicit seasonal modeling is needed to capture quarterly fluctuations in economic data."
```