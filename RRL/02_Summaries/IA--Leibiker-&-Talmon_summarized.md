```yaml
paper_id: 10.5555/3635637.3635953
designation: international-algorithm-specific
title: A Recommendation System for Participatory Budgeting
authors: Leibiker, G.; Talmon, N.
year: 2023
venue: International Conference on Autonomous Agents and Multiagent Systems
odin_topics:
  - 5.A
  - 7.A
  - 7.B
  - 7.C
  - 12.A
  - 12.C
tldr: Machine learning and recommender systems predict missing voter preferences from partial ballots to reduce cognitive burden in participatory budgeting.
problem_and_motivation: Participatory budgeting processes face information overload as voters must consider many projects. This increases cognitive burden and reduces participation. Existing systems lack methods to estimate complete voter preferences from partial ballots.
approach:
  - Formulates participatory budgeting with partial ballots and defines three algorithmic tasks: random, offline, and online preference elicitation.
  - Uses real-world PB datasets from Warsaw with voter and project attributes.
  - Implements prediction models: collaborative filtering via matrix factorization, factorization machines, and binary classification with XGBoost.
  - Evaluates prediction accuracy using precision, recall, F1, and bundle quality using Symmetric Distance and Fractional Allocation score.
  - Compares proposed sampling strategies (popularity, consensus, controversial) against a naive random sampling baseline.
findings:
  - num: Proposed solutions outperform naive sampling for low sampling degrees (0.1 and 0.15).
  - num: Classification-based prediction achieves the highest Fractional Allocation scores across all sampling degrees.
  - num: Online and offline popularity sampling strategies yield superior bundle prediction compared to random sampling.
  - The adaptive controversial online strategy shows improved performance over static offline methods.
  - Increasing both sampling degree and LV degree (number of full-ballot voters) improves prediction accuracy.
key_figures_tables:
  - Table 1: Description of real-world PB datasets → Provides dataset characteristics used in experiments.
  - Figure 5: Heatmap of FA scores vs sampling and LV degree → Shows FA score increases with more data.
  - Figure 6: Heatmap of SD vs sampling and LV degree → Shows SD decreases with more data.
key_equations:
  - equation: "FA = \\lambda / B, \\lambda = \\sum_{p \\in pb \\cap rb} cost(p)"
    explanation: "Fraction of budget correctly allocated to winning projects."
definitions:
  - term: "Participatory Budgeting"
    definition: "Democratic process where community members decide how to spend a public budget."
  - term: "Partial Ballot"
    definition: "A vote where a voter expresses preferences for only a subset of projects."
  - term: "Approval Score"
    definition: "Number of voters who approve a given project."
  - term: "Consensus Level"
    definition: "Absolute difference between approvals and disapprovals for a project."
critical_citations:
  - "[Aziz & Shah, 2021] — Foundational survey of PB models."
  - "[Ricci et al., 2011] — Standard reference for recommender systems."
  - "[Talmon & Faliszewski, 2019] — Defines greedy approval voting rule for PB."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Predicts voter preferences using behavior patterns, analogous to financial profiling.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Directly addresses preference elicitation for budget allocation decisions.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: Proposes a recommendation system for project selection, similar to budget item recommendation.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: medium
      justification: Uses budget constraint as a hard limit in the voting rule, akin to allocation optimization.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Proposes Fractional Allocation score and Symmetric Distance for evaluating allocation quality.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: high
      justification: Evaluates recommendation accuracy and downstream budget allocation performance.
  contribution: "This paper provides a framework for preference elicitation that can inform Odin's budget recommendation module. The classification-based prediction approach can be adapted to predict user spending categories or savings allocations from partial inputs. The Fractional Allocation score offers a direct evaluation metric for budget recommendation quality. The study of online vs offline preference collection informs Odin's UX design for progressive disclosure."
  directly_justifies:
    - "Machine learning can effectively predict missing user preferences from partial data."
    - "Classification models outperform matrix factorization for preference prediction in this domain."
    - "Sampling strategies that target controversial items improve prediction accuracy."
    - "Increasing data collection from users improves overall system performance."
  limits:
    - "Dataset is from civic PB, not personal finance; spending vs voting preferences differ."
    - "Assumes voters have consistent preferences, which may not hold for financial behavior."
    - "Limited to approval-based preferences; Odin uses numeric/percentage allocations."
    - "Does not address cold-start scenarios where no prior user data exists. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains identified high relevance for Budget Recommendation (7.B) and Evaluation (12.A, 12.C), as the paper directly proposes and evaluates a recommendation system for constrained allocation. Medium relevance was assigned to Financial Behavioral Profiles (5.A) because preference prediction is analogous to financial profiling, and to Budgeting Strategies (7.A) and Constrained Optimization (7.C) as background. Domains like Expense Categorization (3.A), Mobile-First Design (9.A), and Data Privacy (10.A) were considered and rejected as the paper does not address these topics. Borderline cases included 7.A (preference elicitation) and 7.B (recommendation system), both selected. Overall, the paper is relevant for Odin's prediction and evaluation modules but requires adaptation from civic to personal finance contexts."
limitations:
  - "Dataset from civic PB may not generalize to personal finance contexts."
  - "Assumes static preferences; financial behavior is dynamic."
  - "Does not address user trust or privacy concerns in preference collection."
  - "Cold-start performance not evaluated. [unacknowledged]"
remember_this:
  - "Classification models achieved highest prediction accuracy for missing preferences."
  - "Online preference elicitation outperforms static sampling strategies."
  - "Increasing collected data by 30% improved Fractional Allocation score by up to 15%."
  - "Sampling controversial items yields better predictions than random or popularity-based sampling."
  - "Machine learning reduces cognitive burden in participatory budgeting decisions."
```