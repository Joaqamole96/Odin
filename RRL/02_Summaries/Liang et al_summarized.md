```yaml
paper_id: 10.48550/arXiv.2602.16131
designation: international-algorithm-specific
title: Learning Personalized Agents from Human Feedback
authors: Liang, K.; Kruk, J.; Qian, S.; Yang, X.; Bi, S.; Yao, Y.; Nie, S.; Zhang, M.; Liu, L.; Fernández Fisac, J.; Zhou, S.; Hosseini, S.
year: 2026
venue: Unknown
odin_topics:
  - 5.A
  - 5.B
 5.C
  - 6.A
  - 7.B
  - 8.A
  - 11.A
  - 12.A
  - 12.B
tldr: A continual personalization framework using explicit memory and dual pre- and post-action feedback channels enables agents to learn initial preferences and adapt to drift.
problem_and_motivation: Static personalization methods fail with new users, cannot learn from real-time corrective feedback, and cannot handle evolving user preferences. This limits the deployment of personalized AI agents in interactive settings.
approach:
  - Data is generated via two new benchmarks: embodied manipulation and online shopping with simulated personas.
  - The PAHF framework operationalizes a three-step loop: pre-action clarification, action execution, and post-action feedback integration.
  - Agents use a standard dense-retrieval memory backend (SQLite or FAISS) to store and retrieve preference notes.
  - Evaluation follows a four-phase protocol that separates initial preference learning from adaptation to persona shifts.
  - Baselines include No Memory, Pre-action Only, and Post-action Only to isolate the effect of each feedback channel.
findings:
  - num: Pre-action agents achieve substantially higher success on the first interaction, reducing initial personalization error by over 30% compared to no-memory baselines.
  - Pre-action Only agents are brittle under drift, with Phase 3 success rates failing to improve or even falling below the no-memory baseline.
  - Post-action feedback is essential for fast adaptation, enabling agents to recover to high Phase-4 success rates (e.g., 67.9% in embodied domain).
  - PAHF combines both strengths, achieving the highest success rates across all phases (e.g., 70.5% in embodied Phase 2, 70.3% in shopping Phase 4).
  - PAHF consistently achieves the lowest average cumulative personalization error (ACPE) across both domains and phases.
  - The combination of pre- and post-action feedback with explicit memory is critical for robust continual personalization.
  - Online shopping domain, with its conjunctive acceptance policies and near-miss distractors, is significantly more challenging than embodied manipulation.
key_figures_tables:
  - Figure 3: Embodied Phase 1 learning curves → Pre-action feedback prevents initial errors, PAHF achieves lowest ACPE.
  - Figure 4: Shopping Phase 3 learning curves → Post-action feedback enables steep recovery, PAHF matches Post-action Only in success but has lower ACPE.
  - Table 1: Evaluation success rates (%) for Phase 2 and 4 → PAHF achieves the highest or tied-highest success rates in all settings.
  - Figure 5: Embodied results with FAISS memory → PAHF consistently outperforms baselines, confirming robustness to memory backend.
key_equations:
  - equation: Mˆ′_t = Fpre_update(Mˆ_t, I_t, O_t, m_t, q_t, fpre_t)
    explanation: Pre-action update function integrating clarification feedback.
  - equation: a_t = π_act(I_t, O_t, m_t, q_t, fpre_t)
    explanation: Action policy synthesizing instruction, observation, and retrieved preferences.
  - equation: Mˆ_{t+1} = Fpost_update(Mˆ′_t, I_t, m_t, q_t, fpre_t, a_t, fpost_t)
    explanation: Post-action update function integrating corrective feedback after an error.
definitions:
  - term: PAHF
    definition: Personalized Agents from Human Feedback, a continual personalization framework.
  - term: ACPE
    definition: Average Cumulative Personalization Error, the average error rate over iterations.
  - term: RAG
    definition: Retrieval-Augmented Generation, a technique for enhancing LLM outputs with retrieved information.
  - term: FF
    definition: Feedback Frequency, the proportion of tasks using any human feedback.
  - term: SR
    definition: Success Rate, the fraction of tasks completed correctly.
  - term: ReAct
    definition: A framework for LLMs to interleave reasoning and acting.
critical_citations:
  - "[Chhikara et al., 2025] — Production-ready memory for AI agents."
  - "[Salemi et al., 2024a] — Optimization for retrieval-augmented personalization."
  - "[Qiu et al., 2025] — Bayesian teaching for LLM probabilistic reasoning."
  - "[Li et al., 2025] — Benchmarks for interactive preference discovery."
  - "[Liang et al., 2025a] — Hindsight simulation mitigates RLHF misalignment."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly models user personas with idiosyncratic and context-dependent preferences.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: high
      justification: Addresses learning from scratch for new users and adapting to preference drift.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Provides a framework (PAHF) for dynamically updating profiles via feedback.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: The framework's memory and feedback mechanism could inform forecasting by tracking preference changes.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: The concept of learning user preferences from feedback is broadly relevant to personalization in PFMS.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: The post-action feedback mechanism could conceptually inform anomaly detection by identifying unexpected or corrected actions.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: contextual
      justification: The feedback loop is designed for live interaction, a core engagement dynamic.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Proposes a four-phase evaluation protocol for continual personalization.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Empirically evaluates the PAHF algorithm against baselines on two benchmarks.
  contribution: PAHF provides a general framework and evaluation protocol for continual personalization that can be directly applied to Odin's behavioral profiling module (5.A, 5.B) to learn user financial profiles from scratch. Its evaluation methodology (12.A, 12.B) offers a template for testing Odin's algorithmic components like forecasting or anomaly detection under user preference drift. The framework's emphasis on explicit memory and corrective feedback (5.C) provides a design pattern for building Odin's user model that adapts to changing financial behaviors.
  directly_justifies:
    - "Explicit memory combined with dual feedback channels is critical for robust personalization without pre-existing user data."
    - "Pre-action clarification prevents initial personalization errors caused by partial observability."
    - "Post-action feedback is essential for correcting miscalibrated beliefs under preference drift."
    - "The four-phase evaluation protocol separately quantifies initial learning and adaptation to drift."
  limits:
    - "The memory architecture is deliberately simple; more sophisticated backends could improve scalability."
    - "The framework does not explicitly handle inconsistent or noisy human feedback."
    - "The benchmarks, especially online shopping, remain challenging for agents."
    - "The agent is limited to at most one clarification question per task, increasing difficulty."
  mapping_rationale: A systematic scan of all 12 functional domains was performed. The paper is most directly relevant to Behavioral Profiling (5.A, 5.B, 5.C) and System Evaluation (12.A, 12.B) due to its focus on learning user personas from scratch and adapting to drift, and its proposed evaluation protocol. It was considered for Spending Forecasting (6.A) and Budget Recommendation (7.B) given its personalization focus, but assigned low relevance as it does not address financial data or budget optimization specifically. The domains of Filipino Cultural Context (2.A-D), Expense Categorization (3.A-C), Existing Systems (4.A-B), Mobile-First Design (9.A-B), Data Privacy (10.A-B), Savings & Debt Management (13.A-C) were rejected as the paper does not address these topics. The paper's theoretical and empirical results on continual personalization provide a strong foundation for Odin's user modeling and evaluation components.
limitations:
  - "The memory architecture is deliberately simple and may not scale to complex user histories. [unacknowledged]"
  - "The framework assumes human feedback is truthful and noise-free. [unacknowledged]"
  - "The online shopping domain remains challenging, with even PAHF achieving only ~70% success in Phase 4."
  - "The agent is limited to a single clarification question per task, which may be insufficient for complex preference elicitation."
remember_this:
  - "PAHF uses explicit memory and dual feedback channels for continual personalization."
  - "Pre-action feedback reduces initial errors by resolving ambiguity before acting."
  - "Post-action feedback is essential for correcting confidently wrong beliefs after preference drift."
  - "PAHF achieves 70.5% success in embodied tasks and 70.3% in shopping tasks after drift."
  - "The combination of pre- and post-action feedback yields the strongest personalization performance."
```