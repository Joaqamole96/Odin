```yaml
paper_id: 10.1145/3616855.3635778
designation: international-algorithm-specific
title: Budgeted Embedding Table For Recommender Systems
authors: Qu, Y.; Chen, T.; Nguyen, Q. V. H.; Yin, H.
year: 2024
venue: Proceedings of the 17th ACM International Conference on Web Search and Data Mining (WSDM ’24)
odin_topics:
  - 4.A
  - 4.B
  - 7.D
  - 8.B
  - 9.A
  - 12.A
  - 12.B
tldr: A method for generating table-level embedding sizes that strictly meet memory budgets, using a fitness predictor to efficiently evaluate actions without per-instance search.
problem_and_motivation: Existing lightweight embedding methods for recommender systems suffer from two major drawbacks: they rely on heuristic trade-off coefficients that fail to strictly meet memory budgets, and they perform per-instance embedding size searches which are computationally inefficient. This creates a need for a scalable solution that can guarantee memory constraints while efficiently finding optimal embedding sizes.
approach:
  - Proposes Budgeted Embedding Table (BET), which generates table-level actions specifying embedding sizes for all users and items simultaneously.
  - Employs a budget-aware sampler that draws embeddings sizes from probabilistic distributions (power law, truncated exponential, etc.) to strictly cap total parameter usage.
  - Introduces a DeepSets-based fitness prediction network that evaluates table-level actions by learning set-based action representations.
  - Alternates between three action selection strategies: greedy fitness prediction, random selection for diversity, and nearest neighbor search in action embedding space.
  - Conducts selective retraining on top actions from the population to identify the final optimal embedding size allocation.
findings:
  - num: BET achieves superior performance on Gowalla and Yelp2018 datasets across three backbone recommenders (LightGCN, NGCF, NCF) at 80%, 90%, and 95% sparsity levels.
  - The DeepSets-based fitness predictor significantly outperforms simpler fitness prediction and random selection variants.
  - BET guarantees strict adherence to pre-specified memory budgets, unlike ESAPN and OptEmbed which often fail to meet minimum sparsity targets.
  - num: BET with LightGCN at 95% sparsity achieves 0.0627 Recall@20 and 0.1037 NDCG@20 on Gowalla, outperforming the best baseline CIESS which achieves 0.0513 and 0.0853 respectively.
  - The fitness predictor converges within 15 iterations, with recommendation performance peaking around 40 iterations.
  - num: Setting the number of sampled actions рЭСЪ to 100 yields the best performance across both datasets.
  - BET is effective with multiple backbone recommenders, demonstrating model-agnostic applicability.
  - The fitness prediction network learns expressive set-based action representations using user/item frequency and embedding size information.
key_figures_tables:
  - Figure 1: Overview of BET workflow → Shows the three-component system of sampler, fitness predictor, and backbone recommender.
  - Figure 2: Set-based action formulation example → Illustrates how actions are represented as sets of users/items per embedding size.
  - Figure 3: DeepSets-based fitness predictor architecture → Depicts the user/item encoders and set aggregation for action representation.
  - Table 1: Performance comparison on Gowalla and Yelp → BET achieves the best results across most metrics and sparsity levels.
  - Table 2: Model component analysis → DeepSets-based predictor outperforms random and simple fitness prediction variants.
  - Figure 4: Sensitivity analysis of рЭСЪ → Performance improves with more sampled actions, plateauing at 100.
  - Figure 5: Sensitivity analysis of рЭСЗ → Performance improves up to 40 iterations then stabilizes.
  - Figure 6: Fitness prediction loss convergence → Loss diminishes within the first 15 iterations.
key_equations:
  - equation: L_BPR = -∑_{(u,i,j)∈D_train} ln σ(ŷ_ui - ŷ_uj) + λ||Θ||²
    explanation: Bayesian Personalized Ranking loss for optimizing recommenders.
  - equation: d_i = ⌊ p̃_i · w · d_max · (|U|+|V|) ⌋
    explanation: Calculates embedding size for each user based on normalized probability and memory budget.
  - equation: f_Θ(E ⊙ M | D_valid) / f_Θ(E | D_valid)
    explanation: Fitness score is the ratio of recommendation quality with sparsified vs full embeddings.
  - equation: Φ = argmin_{φ'} ∑_{a}(r_a - f_{φ'}(a))²
    explanation: Optimizes fitness predictor by minimizing mean squared error between predicted and actual scores.
definitions:
  - term: BET
    definition: Budgeted Embedding Table - the proposed method for table-level embedding size search.
  - term: Table-level action
    definition: An action that specifies embedding sizes for all users and items in one embedding table.
  - term: Fitness predictor
    definition: A DeepSets-based network that predicts the recommendation performance of a table-level action.
  - term: Set-based action formulation
    definition: Representing an action as sets of users/items grouped by their assigned embedding size.
  - term: Sparsity ratio
    definition: The ratio of active parameters in the compressed embedding table compared to the full table.
  - term: DeepSets
    definition: A neural architecture for learning permutation-invariant representations of sets.
critical_citations:
  - "[He et al., 2020] — Foundation for LightGCN backbone model."
  - "[Rendle et al., 2009] — Source of BPR loss function for recommendation."
  - "[Zhao et al., 2021] — Prior work on automated embedding dimensionality search."
  - "[Liu et al., 2021] — Prior work on learnable embedding sizes via pruning."
  - "[Qu et al., 2023] — Previous RL-based method for continuous embedding size search."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Discusses memory-efficient embedding techniques applicable to resource-constrained financial systems.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Explicitly identifies the limitations of existing lightweight embedding methods (implicit memory constraints, per-instance inefficiency) and proposes a solution.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: high
      justification: Provides a method to strictly enforce memory/sparsity constraints through probabilistic sampling, directly relevant to handling budget constraints in recommendation.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: The concept of adaptive embedding sizes could be extended to anomaly detection, but the paper focuses on recommendation.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: high
      justification: Addresses memory constraints critical for on-device/deployable systems, directly relevant to mobile-first financial applications.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses standard recommendation metrics (Recall, NDCG) that could be adapted to evaluate PFMS modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides a rigorous evaluation methodology for algorithmic modules (embedding size search) with ablation studies and hyperparameter analysis.
  contribution: This paper provides a novel algorithmic framework (BET) for efficiently searching embedding sizes under strict memory budgets, which directly addresses Odin's need to optimize resource-constrained financial recommendation modules. The set-based action formulation and DeepSets fitness predictor offer a scalable approach to managing user and item representations, relevant to Odin's expense categorization and behavioral profiling. The strict budget enforcement mechanism is directly applicable to Odin's constrained optimization and infeasibility handling modules. The model-agnostic design and selective retraining strategy demonstrate how algorithmic modules can be evaluated and optimized with minimal computational overhead.
  directly_justifies:
    - "Memory budgets can be strictly enforced using probabilistic sampling from table-level actions."
    - "DeepSets-based set representation learning enables efficient evaluation of unseen actions."
    - "Hybrid action selection strategies (greedy, random, nearest neighbor) improve search diversity and prevent overfitting."
    - "Selective retraining on top actions from the population identifies optimal embedding size allocations."
    - "The fitness predictor converges quickly, reducing the need for exhaustive retraining."
  limits:
    - "The study focuses on recommendation systems, not directly on personal finance or expense categorization."
    - "The approach assumes static user and item sets; handling dynamic users/items requires extension."
    - "Fitness predictor performance depends on the representativeness of the training samples; may require many iterations for complex domains."
    - "The effectiveness of the probabilistic distributions (power law, etc.) may vary with different data characteristics."
    - "No discussion on privacy-preserving aspects of embedding size search."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes revealed that this paper is most relevant to the 'Existing Systems & Gaps' (4.A, 4.B), 'Budget Recommendation' (7.D), 'Anomaly Detection' (8.B contextual), 'Mobile-First Design' (9.A), and 'System Evaluation' (12.A, 12.B) domains. The paper directly addresses the limitations of existing lightweight embedding methods (4.A, 4.B) and proposes a novel algorithm that strictly enforces memory constraints (7.D). The focus on reducing memory footprint is critical for mobile-first design (9.A). The rigorous evaluation framework and ablation studies (12.A, 12.B) are directly applicable. The paper was considered for 8.A and 8.B due to the potential of adaptive embeddings for anomaly detection, but the core contribution does not address detection algorithms, so it was assigned contextual relevance. The domains of Filipino cultural context, expense categorization, behavioral profiling, forecasting, user retention, and savings/debt management were considered but not selected as the paper does not provide claims directly informing those specific topics. Overall, the paper provides high relevance for Odin's algorithmic design, particularly in memory-constrained and budgeted recommendation scenarios.
limitations:
  - "The approach is designed for recommendation systems; adaptation to personal finance modules requires additional validation."
  - "Hyperparameters (e.g., number of iterations, sample size) may require tuning for different datasets and domains."
  - "The study does not explore the impact of dynamic user/item sets, which are common in financial applications."
  - "Fitness predictor may need retraining if the data distribution changes significantly over time."
  - "The method does not address cold-start scenarios for new users or items."
  - "Privacy implications of storing embedding sizes and distributions are not discussed. [unacknowledged]"
  - "Real-time performance and inference latency under strict budgets are not evaluated. [unacknowledged]"
  - "Integration with PFMS-specific features like expense categorization or savings goals is not explored. [unacknowledged]"
remember_this:
  - "BET guarantees strict adherence to memory budgets through table-level probabilistic sampling."
  - "DeepSets-based fitness predictor efficiently evaluates table-level actions without per-instance training."
  - "Hybrid action selection (greedy, random, nearest neighbor) improves search diversity and performance."
  - "BET outperforms state-of-the-art methods at 80%, 90%, and 95% sparsity across three recommenders."
  - "The fitness predictor converges within 15 iterations, enabling efficient search with only 40 iterations."
```