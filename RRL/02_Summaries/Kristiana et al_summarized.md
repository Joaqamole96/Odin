```yaml
paper_id: 10.1109/OJCS.2026.3658518
designation: international-algorithm-specific
title: Validating AI-Driven Nudge Recommendations: A/B Testing Two-Tower and Bandit Models in Simulated Digital Banking Environment
authors: Kristiana, I.; Prabowo, H.; Lumbangaol, F.; Qomariyah, N. N.
year: 2026
venue: IEEE Open Journal of the Computer Society
odin_topics:
  - 4.B
  - 5.A
  - 5.C
  - 6.A
  - 11.A
  - 12.A
  - 12.B
  - 4.A
  - 6.B
  - 9.A
  - 9.B
tldr: A hybrid recommendation model combining Two-Tower Network static personalization with Multi-Armed Bandit adaptive nudge selection increases recommendation-following behavior from 13.6% to 52.87% in a simulated digital banking A/B test.
problem_and_motivation: Existing recommender systems in banking rely on collaborative or content-based filtering that fail due to data sparsity, cold-start problems, and the absence of behavioral mechanisms. No empirically validated model integrates static personalization, real-time adaptive learning, and explicit behavioral nudge design for financial decision support.
approach:
  - Data was collected from 214 control and 174 treatment verified bank customers via a 54-item behavioral questionnaire and mobile banking simulation with purchase-like actions.
  - A Two-Tower Network with 128-64-128 architecture generates user and product embeddings using PCA dimensionality reduction and SMOTE oversampling for class balance.
  - A Multi-Armed Bandit with ε-greedy policy and Gaussian reward feedback adaptively selects among nine nudge mechanisms based on TWN-generated relevance scores.
  - Sequential A/B testing compared rule-based nudging (App v1) against TWN+MAB-driven nudging (App v2) with no participant overlap between groups.
  - Evaluation used chi-square testing, odds ratio calculation, reward trajectory analysis, and regret analysis against empirical optimal arm.
  - A TWN-only ablation baseline isolated the effect of behavioral nudging and adaptive bandit layer beyond static personalization.
findings:
  - num: Purchase conversion rose from 48.6% in control to 62.07% in treatment, a relative improvement of 27.7%.
  - num: Recommendation-aligned purchases increased from 13.6% to 52.87%, representing a fourfold behavioral shift.
  - num: Chi-square test confirmed statistical significance (χ2 = 6.49, p < 0.0108).
  - num: Odds ratio of 7.15 indicates treatment users are over seven times more likely to follow recommendations than control users.
  - 100% of recommendation-driven purchases in the treatment group aligned with the MAB's empirically optimal arm.
  - Smoothed regret trajectories remained below 0.10-0.15 threshold, demonstrating stable bandit learning without policy divergence.
  - Event-level reward trajectories remained stable over interaction rounds, confirming robust online adaptation under noisy feedback.
key_figures_tables:
  - Figure 1: DSR methodology diagram → Illustrates the research framework from problem identification to evaluation.
  - Figure 2: A/B testing research flow → Shows control and treatment group allocation and measurement pipeline.
  - Figure 3: Integrated TWN+MAB architecture → Visualizes embedding generation, bandit decision, and nudge deployment.
  - Figure 4: Reward trajectories under MAB → Stable event-level reward confirms robust online learning.
  - Figure 5: Smoothed instant regret → Regret stays below threshold, validating exploration-exploitation balance.
  - Table 1: TWN configuration parameters → 128-64-128 architecture with 20 epochs and SMOTE oversampling.
  - Table 2: A/B testing metrics → Direct comparison of control and treatment behavioral outcomes.
key_equations:
  - equation: Q_{t+1}(a) = Q_t(a) + (1/N_t(a)) * (R_t - Q_t(a))
    explanation: Incremental reward estimate update for each product arm in MAB.
  - equation: a_t = argmax_a Q_t(a) with probability 1-ε, else random arm
    explanation: ε-greedy policy selects best arm or explores randomly.
definitions:
  - term: TWN
    definition: Two-Tower Network for learning deep user and product embeddings via dual-encoder architecture.
  - term: MAB
    definition: Multi-Armed Bandit for adaptive online learning balancing exploration and exploitation.
  - term: DSR
    definition: Design Science Research methodology for building and evaluating artifacts.
  - term: CF
    definition: Collaborative Filtering recommender system based on user-item interaction similarity.
  - term: CBF
    definition: Content-Based Filtering recommender system using item attribute similarity.
  - term: SMOTE
    definition: Synthetic Minority Oversampling Technique for addressing class imbalance.
  - term: PCA
    definition: Principal Component Analysis for dimensionality reduction while preserving variance.
critical_citations:
  - "[Thaler and Sunstein, 2008] — Foundation of nudge theory for choice architecture."
  - "[Jesse and Jannach, 2021] — Digital nudging with recommender systems survey."
  - "[Kristiana et al., 2025] — Prior work establishing AI-driven nudge optimization framework."
  - "[Yi et al., 2019] — Neural modeling for large corpus item recommendations."
  - "[Bouneffouf et al., 2020] — Survey on multi-armed bandit applications."
relevance:
  topics:
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly identifies CF/CBF limitations in banking and proposes hybrid solution.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Builds user embeddings from 54-item behavioral questionnaire for personalization.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Two-Tower Network classifies users into behavioral profiles via embeddings.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: TWN predicts user-product relevance scores as static personalization backbone.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: A/B testing measures behavioral engagement through purchase and recommendation-following.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Controlled A/B testing with chi-square validation provides evaluation methodology.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Separately evaluates TWN static personalization and MAB adaptive nudge selection.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews existing recommender systems in banking and their limitations.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: MAB adapts sequentially based on real-time user feedback and reward signals.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Evaluation conducted in a mobile banking simulator mirroring real application behavior.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Nudge mechanisms are presented through mobile UX with framing, saliency, and just-in-time cues.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Paper does not address anomaly detection; focus is on recommendation and nudging.
  contribution: The paper provides a validated hybrid architecture combining Two-Tower Network static personalization with Multi-Armed Bandit adaptive nudge selection that can inform Odin's recommendation and behavioral profiling modules. The A/B testing framework with chi-square validation offers a rigorous evaluation template for Odin's algorithmic modules. The finding that adaptive nudging significantly outperforms rule-based baselines justifies investing in real-time personalization for user engagement. The paper's emphasis on behavioral profiling via multi-dimensional questionnaires aligns with Odin's user classification needs.
  directly_justifies:
    - "Combining static personalization with adaptive learning increases recommendation-following by fourfold."
    - "Behavioral nudges delivered through AI models significantly influence financial decision-making."
    - "A/B testing with verified bank customers provides causal evidence for nudge effectiveness."
    - "Two-Tower Networks can address cold-start and sparsity in financial recommendation contexts."
    - "Multi-Armed Bandits enable real-time nudge optimization without premature convergence."
  limits:
    - "Simulated environment lacks real financial consequences, reducing ecological validity."
    - "Sequential quasi-experimental design allows potential time-based confounding."
    - "Training data from a single Indonesian bank may not generalize to Filipino young professionals."
    - "Ethical challenges around autonomy and fairness are acknowledged but not empirically addressed. [unacknowledged]"
  mapping_rationale: A systematic scan across all 12 functional domains and 31 canonical topic codes was performed. The paper was flagged as relevant primarily to Domains 4 (Existing Systems), 5 (Behavioral Profiling), 6 (Forecasting), 11 (Engagement), and 12 (Evaluation). Topic codes 4.B, 5.A, 5.C, 6.A, 11.A, 12.A, and 12.B were assigned high relevance because the paper directly addresses limitations of existing systems, builds behavioral profiles, applies predictive modeling, measures engagement, and provides A/B testing evaluation. Topic codes 4.A, 6.B, 9.A, and 9.B were assigned medium relevance as supporting context for system landscape, sequential adaptation, and mobile UX. Topic 8.A (Anomaly Detection) was considered and rejected as the paper does not address anomaly detection. Domains 2 (Cultural Context), 3 (Expense Categorization), 7 (Budget Recommendation), 10 (Privacy), and 13 (Savings/Debt) were considered and rejected as the paper focuses on recommendation and nudging rather than these specific PFMS functions. The paper is overall relevant to Odin's personalization and evaluation modules, though its Indonesian banking context limits direct cultural applicability.
limitations:
  - "Experiments conducted in simulated environment, not real financial application."
  - "Sequential A/B design with non-overlapping deployment windows may allow time-based confounds."
  - "Training corpus from a single domain limits generalizability to sparse or underrepresented users."
  - "Ethical safeguards for user autonomy and fairness were not empirically tested."
  - "Real-world deployment would require Responsible AI guardrails not explored in study. [unacknowledged]"
remember_this:
  - "AI-driven nudging increased recommendation-following from 13.6% to 52.87%."
  - "Hybrid TWN+MAB architecture outperformed rule-based baseline across all behavioral metrics."
  - "MAB achieved stable regret below threshold with 100% alignment on optimal arm."
  - "Statistical significance confirmed by chi-square test (p < 0.0108)."
  - "Odds ratio of 7.15 for recommendation-following behavior under AI treatment."
```