```yaml
paper_id: 10.21070/acopen.10.2025.12858
designation: international-algorithm-specific
title: Goal Programming Model in Financial Planning of the International Development Bank
authors: Aboud, M.M.S.F.
year: 2025
venue: Academia Open
odin_topics:
  - 7.C
  - 12.C
tldr: Goal programming optimizes conflicting financial objectives in banking under resource constraints, achieving near-optimal solutions with minimal deviations.
problem_and_motivation: Financial institutions struggle to balance multiple conflicting objectives like profitability, cost control, and liquidity. Traditional planning models lack the capability to handle these competing goals, especially in resource-constrained environments. A quantitative method is needed to reconcile these trade-offs and improve decision-making.
approach:
  - A weighted-preemptive hybrid goal programming model is formulated for bank financial planning.
  - The model incorporates multiple objectives: revenue, expenses, net profit, fixed assets, loans, and equity.
  - WINQSB software is used to solve the model with prioritized goals and assigned weights.
  - The case study uses annual financial data from the International Development Bank for 2016-2024.
  - The model is evaluated by comparing actual and target values across all financial goals.
findings:
  - The GP model achieved near-optimal solutions for all prioritized goals.
  - Revenue goal was slightly underachieved with a negative deviation of 0.1884.
  - Expense goal was slightly underachieved with a negative deviation of 0.1873.
  - Net profit goal was underachieved with a negative deviation of 0.3006.
  - Fixed assets goal was overachieved with a positive deviation of 0.7833.
  - Equity goal was underachieved with a negative deviation of 0.2956.
  - The model demonstrates flexible prioritization of goals in a multi-objective setting.
key_figures_tables:
  - Table 1: Financial data summary 2016-2024 → Provides raw data for the model.
  - Table 2: Scaled financial data in billion IQD → Enables analysis with smaller numbers.
key_equations:
  - equation: Min Z = Σ(w_i^- d_i^- + w_i^+ d_i^+)
    explanation: Minimizes weighted deviations from multiple goals.
  - equation: Σ a_ij X_j + d_i^- - d_i^+ = b_i
    explanation: Defines goal constraints with deviation variables.
definitions:
  - term: Goal Programming
    definition: A mathematical model for solving multi-objective problems with competing goals.
  - term: Negative Deviation
    definition: The amount by which an actual value is below the aspiration level.
  - term: Positive Deviation
    definition: The amount by which an actual value exceeds the aspiration level.
  - term: Weighted Method
    definition: Assigns weights to goals and minimizes total weighted deviation.
  - term: Preemptive Method
    definition: Prioritizes goals, satisfying higher-priority ones first.
  - term: WINQSB
    definition: Software used to solve the goal programming model.
critical_citations:
  - "[Alam, 2022] — Foundational GP model for financial planning."
  - "[Lakshmi et al., 2021] — GP application in financial planning case study."
  - "[Nyor et al., 2022] — GP for financial management in Nigeria."
relevance:
  topics:
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: high
      justification: Applies goal programming to optimize multi-objective financial planning.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Demonstrates a method for evaluating optimal solutions against target values.
  contribution: "The paper provides a practical optimization framework that can inform Odin's budget recommendation module by demonstrating how conflicting objectives (e.g., maximizing savings while minimizing expenses) can be balanced using a weighted-preemptive goal programming approach. The solution method, using WINQSB, offers a reproducible technique for solving multi-objective financial planning problems with prioritized constraints. The case study results, including deviation analysis, provide a benchmark for evaluating optimization models. The model's flexibility suggests it can be adapted for personalized budget allocation based on user-defined financial goals. The research validates the use of constrained optimization for complex financial planning in resource-limited settings, directly applicable to Odin's budget recommendation engine."
  directly_justifies:
    - "Goal programming can optimize financial planning with conflicting objectives."
    - "The model achieves near-optimal solutions with minimal goal deviations."
    - "Prioritization of goals allows flexible decision-making in resource allocation."
    - "The approach is applicable to banking and personal finance contexts."
  limits:
    - "The model is demonstrated on a single bank's data and may not generalize."
    - "User preferences and behavioral factors are not incorporated."
    - "The study focuses on a bank, not individual personal finance management."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to the 'Budget Recommendation' domain (Topic 7.C) because it directly applies constrained optimization (goal programming) to balance multiple, conflicting financial objectives. It is also relevant to 'System Evaluation' (Topic 12.C) because it demonstrates an evaluation methodology based on comparing actual outcomes to target values and analyzing deviations. The paper touches on 'Savings & Debt Management' (Topic 13.A and 13.B) tangentially through its objectives but does not focus on user-level savings goals or debt management strategies. The following domains/topics were considered and rejected: 'Filipino Cultural Context' (Topics 2.A-2.D) because the case study is based on an Iraqi bank and does not address Filipino-specific practices; 'Expense Categorization' (Topic 3.A-3.C) because the paper does not deal with categorizing expenses; 'Behavioral Profiling' (Topics 5.A-5.C) because it does not involve user behavior or profiles; 'Anomaly Detection' (Topics 8.A-8.C) because it does not address detecting outliers. Overall, the paper is most relevant for its constrained optimization methodology, which can be adapted for Odin's budget recommendation algorithm."
limitations:
  - "The model is based on historical data from a single bank, limiting generalizability."
  - "The study does not consider dynamic changes in user behavior or financial conditions."
  - "Behavioral and psychological factors influencing financial decisions are not incorporated. [unacknowledged]"
  - "The approach is applied to banking rather than individual personal finance. [unacknowledged]"
remember_this:
  - "Goal programming balances conflicting financial objectives effectively."
  - "The model achieved near-optimal solutions with minimal deviations."
  - "Prioritization allows flexible resource allocation in financial planning."
  - "Multi-objective optimization is feasible for complex financial systems."
  - "The method can be adapted for personalized budget recommendation."
```