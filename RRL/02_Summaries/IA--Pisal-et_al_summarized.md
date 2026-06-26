```yaml
paper_id: 10.1038/s41598-025-17604-y
designation: international-algorithm-specific
title: An integrated TOPSIS and ARAS method multi-criteria decision-making approach for optimizing investment portfolios using goal programming and genetic algorithm model
authors: Pisal, P.; Reddy, K. K.; Kishore, J.; Jonnalagadda, R. R.; Kumar, M.; Band, G.; Joshi, B. P.
year: 2025
venue: Scientific Reports
odin_topics:
  - 4.A
  - 4.B
  - 5.A
  - 6.A
  - 6.B
  - 7.B
  - 7.C
  - 7.D
  - 8.B
  - 12.A
  - 12.B
  - 12.C
  - 13.A
  - 13.B
tldr: A hybrid framework integrates TOPSIS-ARAS ranking with goal programming and genetic algorithms to optimize investment portfolios, achieving a Sharpe ratio of 2.241 on the FAR-Trans dataset.
problem_and_motivation: Existing portfolio optimization models either rank assets without allocating capital or optimize allocations without integrating investor preferences. This separation leads to suboptimal plans that fail to balance multiple objectives like return, risk, and diversification. A unified framework combining preference modeling with constrained optimization is critically needed.
approach:
  - Data from the FAR-Trans dataset (359,128 transactions, 2018-2022) is preprocessed using min-max scaling and one-hot encoding.
  - A two-layer MCDM framework fuses TOPSIS closeness coefficients and ARAS utility scores via a convex combination to rank assets.
  - A goal programming model encodes investor-specific return targets, risk thresholds, and budget constraints as deviation variables.
  - A genetic algorithm with tournament selection, SBX crossover, and Gaussian mutation explores the feasible space to refine portfolio weights.
  - The framework is benchmarked against Markowitz, NSGA-III, MOPSO, and other state-of-the-art models using Sharpe ratio, ROI, diversification, and budget adherence.
findings:
  - num: The proposed model achieved a Sharpe ratio of 2.241 and an annualized return of 4.6%.
  - num: The diversification score was 0.845 across 79 assets and 13 sectors.
  - num: A 0.729 correlation was found between TOPSIS-ARAS rankings and GP-configured portfolio returns.
  - The GA module converged within 80 generations, demonstrating computational efficiency.
  - Sensitivity analysis showed high rank stability (Kendall's τ > 0.89) across different MCDM fusion weights.
  - Investor segmentation revealed that 59% of transactions were purchases, indicating a bullish accumulation trend.
  - The model maintained a budget deviation of €36.2M while achieving over 30% returns in validation portfolios.
key_figures_tables:
  - Figure 3: Transaction distribution showing 59% purchases → Indicates alignment with stable asset selection.
  - Figure 4: Investor segmentation showing 61% "Mass" customers → Supports capital-based constraint modeling in GP.
  - Figure 9: ROI distribution across Stocks, Bonds, MTFs → Highlights equities achieving outlier returns >80%.
  - Figure 12: Top 10 asset allocations with Financial Services dominating → Reflects high MCDM scores for return-risk profile.
  - Table 4: Performance comparison vs. state-of-the-art → Confirms proposed model's superiority across all metrics.
key_equations:
  - equation: \phi_i = \alpha \cdot C_i^{TOPSIS} + (1-\alpha) \cdot U_i^{ARAS}
    explanation: Convex fusion of TOPSIS and ARAS scores for hybrid ranking.
  - equation: \text{Min} \sum_{j=1}^{n} (d_j^+ + d_j^-)
    explanation: Goal programming objective minimizing deviations from investor targets.
  - equation: \text{Fitness} = \sum x_i r_i - \lambda \left| \sum x_i \sigma_i - \sigma^* \right|
    explanation: GA fitness function balancing return and risk penalty.
definitions:
  - term: TOPSIS
    definition: Technique for Order Preference by Similarity to Ideal Solution, ranks alternatives by geometric distance to ideal and anti-ideal points.
  - term: ARAS
    definition: Additive Ratio Assessment, ranks alternatives using additive normalization and utility scores.
  - term: GP
    definition: Goal Programming, an optimization method that minimizes deviations from multiple, possibly conflicting, objectives.
  - term: GA
    definition: Genetic Algorithm, an evolutionary metaheuristic that iteratively improves solutions via selection, crossover, and mutation.
  - term: MCDM
    definition: Multi-Criteria Decision Making, a set of methods for evaluating alternatives based on multiple conflicting criteria.
  - term: FAR-Trans
    definition: Financial Asset Recommendation Transactions dataset, containing anonymized investor and asset data from a European institution.
critical_citations:
  - "[Vásquez et al., 2021] — AHP-TOPSIS benchmark for stock portfolio investments."
  - "[Anadani et al., 2023] — GA approach for portfolio optimization baseline."
  - "[Mwamba et al., 2025] — NSGA-III application for multi-objective portfolio selection."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Reviews traditional MCDM and optimization systems but not specific PFMS.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Explicitly identifies the gap between preference modeling and allocation optimization.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: low
      justification: Segments investors by risk tolerance but does not define behavioral profiles for PFMS.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: contextual
      justification: Uses historical returns and risk but not predictive spending models.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: Applies GA/GP to asset allocation, not to sequential spending forecasting.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Provides a general optimization framework that could inform budget recommendations.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: high
      justification: Directly presents a GP-GA model for constrained asset allocation.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: low
      justification: Penalty-based handling of risk constraints is mentioned but not a primary focus.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: The method uses deviation minimization, conceptually related to anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: low
      justification: Uses Sharpe ratio and ROI for evaluation, not PFMS-specific metrics.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Ablation study and comparative baselines validate each module's contribution.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: low
      justification: Evaluation is for investment portfolios, not budget recommendation systems.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: contextual
      justification: Return maximization could relate to savings growth but is not the core focus.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: low
      justification: Does not address debt; focuses on asset allocation for return.
  contribution: The paper provides a validated, modular framework for multi-objective portfolio optimization that can inform Odin's budget allocation and optimization modules. Its dual MCDM ranking (TOPSIS-ARAS) offers a stable asset pre-selection method that could be adapted for expense category prioritization. The GP-GA hybrid demonstrates how investor-specific constraints (return, risk, budget) can be encoded into a solvable optimization problem, relevant to Odin's budget recommendation engine. The ablation study and sensitivity analysis offer best practices for evaluating algorithmic modules and handling parameter uncertainty.
  directly_justifies:
    - "A hybrid MCDM-GP-GA framework can effectively balance multiple financial objectives with investor constraints."
    - "Integrating TOPSIS and ARAS via convex fusion reduces ranking sensitivity and stabilizes asset selection."
    - "Genetic algorithms are computationally feasible for portfolio optimization with early convergence under 100 generations."
    - "Sensitivity analysis with Kendall's τ can validate the robustness of ranking systems against parameter changes."
  limits:
    - "The model assumes single-period static optimization, which limits adaptability to dynamic market conditions."
    - "Computational time scales with portfolio size, requiring optimization for high-frequency use cases."
    - "Investor constraints are modeled as linear goals, ignoring fuzzy or utility-based preferences."
    - "Regulatory constraints, transaction costs, and tax implications are not included."
  mapping_rationale: A systematic scan across all 12 functional domains revealed that this paper most directly informs the System Evaluation domain (12.A, 12.B, 12.C) through its comprehensive evaluation framework. It also provides strong methodological insights for Budget Recommendation via Constrained Optimization (7.C) with its GP-GA model. The paper's explicit discussion of the gap between preference modeling and allocation (4.B) offers supporting evidence for the limitations of existing personal finance systems. Topics related to Behavioral Profiling (5.A) and Forecasting (6.A, 6.B) were flagged with low or contextual relevance because the paper uses general investor risk profiles and historical returns, not the specific Filipino behavioral or spending patterns relevant to Odin. The domains of Filipino Cultural Context (2.A-D) and Mobile-First Design (9.A-B) were considered and rejected as they are not addressed. Data Privacy (10.A-B) and User Retention (11.A-B) were also not within the paper's scope. The paper's overall relevance to Odin is medium, as it offers a robust, validated methodological template for building an optimization engine, but requires significant adaptation to the PFMS context.
limitations:
  - The model assumes single-period static optimization, not dynamic market conditions or multi-period planning. [unacknowledged]
  - Genetic algorithm convergence time may become a bottleneck for high-frequency portfolio recommendations.
  - The framework uses linear investor goals, but real-world preferences are often fuzzy or utility-based. [unacknowledged]
  - Regulatory constraints, transaction costs, and tax considerations are absent from the model. [unacknowledged]
  - The model's interpretability is enhanced by visualizations but lacks formal XAI modules like SHAP or LIME. [unacknowledged]
remember_this:
  - Hybrid MCDM-GP-GA achieved a Sharpe ratio of 2.241 and ROI of 4.6%.
  - Dual TOPSIS-ARAS ranking via convex fusion enhances asset selection stability.
  - GP encodes investor-specific return, risk, and budget constraints as deviations.
  - GA optimization converged within 80 generations with a population size of 100.
  - The framework outperformed NSGA-III and MOPSO across all key portfolio metrics.
```