```yaml
paper_id: 10.48550/arXiv.2602.22302
designation: international-algorithm-specific
title: Agent Behavioral Contracts: Formal Specification and Runtime Enforcement for Reliable Autonomous AI Agents
authors: Bhardwaj, V.
year: 2026
venue: arXiv preprint # This paper is a pre-print article
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 8.A
  - 8.B
  - 8.C
  - 11.A
  - 11.B
  - 12.A
  - 12.B
tldr: Introduces Agent Behavioral Contracts (ABC), a formal framework with probabilistic satisfaction and drift bounds that brings Design-by-Contract principles to autonomous AI agents for runtime enforcement.
problem_and_motivation: AI agents operate on prompts with no formal behavioral specification, causing drift, governance failures, and project failures. Existing training-time alignment and output guardrails lack runtime enforcement and formal guarantees. This gap necessitates a framework for specifying, verifying, and enforcing agent behavior.
approach:
  - Defines contract C = (P,I,G,R) with hard/soft constraints and recovery.
  - Introduces (p,δ,k)-satisfaction for probabilistic compliance.
  - Proves stochastic drift bounds using Ornstein-Uhlenbeck dynamics.
  - Establishes compositionality conditions for multi-agent chains.
  - Implements in ContractSpec DSL and AgentAssert runtime library.
  - Evaluates on AgentContract-Bench and 7 models from 6 vendors.
findings:
  - num: Contracted agents detect 5.2–6.8 soft violations per session invisible to baselines (p < 0.0001, Cohen's d = 6.7–33.8).
  - num: Hard constraint compliance reaches 88–100% under contracts.
  - num: Behavioral drift is bounded to D* < 0.27 across extended sessions.
  - num: Recovery success is 100% for frontier models and 17–100% across all models.
  - num: Runtime overhead is < 10ms per action.
  - Contract enforcement makes previously invisible violations measurable.
  - Hard constraints enforce safety-critical properties reliably.
  - Drift monitoring provides a leading indicator of emerging misalignment.
  - Recovery transforms exponential compliance decay into linear decay.
  - Contract components are non-redundant; removing recovery drops reliability index by ~0.20.
key_figures_tables:
  - Figure 1: Agent reliability index Θ across 7 models → Llama 3.3 70B highest (0.956), Mistral Large 3 lowest (0.908).
  - Figure 2: Drift trajectory over extended sessions → Contracted agents exhibit bounded drift consistent with OU mean-reversion.
  - Figure 3: OU model fit to drift trajectories → R2 = 0.49–0.75 confirms qualitative structure.
  - Figure 4: Ablation heatmap → Removing recovery or soft constraints degrades Θ by ~0.20.
  - Figure 5: Runtime overhead scaling → Linear in constraint count, <25ms for k=100.
  - Figure 6: Recovery mechanism impact → Degrades Θ by 0.199–0.215 when removed.
  - Figure 7: SPRT vs fixed-sample efficiency → SPRT requires 150–300 sessions vs 18,445 for Hoeffding.
key_equations:
  - equation: C = (P, I_hard ∪ I_soft, G_hard ∪ G_soft, R)
    explanation: Contract structure with hard/soft constraints and recovery.
  - equation: C_hard(t) = |{c ∈ I_hard ∪ G_hard : c(s_t, a_t) = true}| / |I_hard ∪ G_hard|
    explanation: Fraction of hard constraints satisfied at step t.
  - equation: C_soft(t) = |{c ∈ I_soft ∪ G_soft : c(s_t, a_t) = true}| / |I_soft ∪ G_soft|
    explanation: Fraction of soft constraints satisfied at step t.
  - equation: D(t) = w_c · D_compliance(t) + w_d · D_distributional(t)
    explanation: Behavioral drift score as weighted sum of compliance and distributional components.
  - equation: dD(t) = (α − γD(t))dt + σdW(t)
    explanation: Ornstein-Uhlenbeck drift dynamics for agent behavioral drift.
  - equation: E_π[D(t)] = α/γ
    explanation: Stationary mean drift under contract enforcement.
definitions:
  - term: ABC
    definition: Agent Behavioral Contracts, a formal framework for runtime enforcement of behavioral specifications in autonomous AI agents.
  - term: Design-by-Contract
    definition: Software engineering paradigm specifying preconditions, postconditions, and invariants for components.
  - term: (p,δ,k)-satisfaction
    definition: Probabilistic contract compliance where hard constraints hold with probability p, soft deviations within δ, recovery within k steps.
  - term: Behavioral Drift
    definition: Progressive divergence of agent behavior from intended specification over extended interactions.
  - term: OU Process
    definition: Ornstein-Uhlenbeck process, a stochastic differential equation with mean-reversion.
  - term: JSD
    definition: Jensen–Shannon divergence, a metric for measuring similarity between probability distributions.
  - term: SPRT
    definition: Sequential Probability Ratio Test, a sequential hypothesis test for minimal expected sample size.
critical_citations:
  - "[Meyer, 1992] — Introduced Design-by-Contract paradigm."
  - "[Benveniste et al., 2018] — Algebra for assume-guarantee contracts."
  - "[Alshiekh et al., 2018] — Shielding for safe RL."
  - "[Wang et al., 2026a] — Proved safety degradation absent external intervention."
  - "[Rath, 2026] — First systematic study of agent behavioral drift."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: Provides general framework for behavioral profiling via drift monitoring.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: Mention of cold-start baseline strategies in anomaly detection.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: General classification via contract compliance.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly addresses runtime anomaly detection via contract enforcement.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Proposes probabilistic anomaly detection with hard/soft constraints.
    - code: 8.C
      name: Cold‑Start Baseline Strategies for Anomaly Detection
      relevance: medium
      justification: Discusses reference distribution calibration for drift detection.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: contextual
      justification: General framework for engagement via compliance monitoring.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: contextual
      justification: Recovery mechanisms as retention enablers.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Introduces a comprehensive evaluation protocol with metrics like Θ, D(t), C(t).
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Evaluates algorithmic module (AgentAssert) across models and scenarios.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: contextual
      justification: General evaluation methodology for PFMS modules.
  contribution: "Provides a formal contract framework (ABC) for runtime enforcement in autonomous agents, directly applicable to anomaly detection and system evaluation modules in Odin. The (p,δ,k)-satisfaction definition offers a probabilistic compliance model usable for spending anomaly detection. The drift bounds theorem gives a theoretical basis for predicting and bounding behavioral drift in user financial profiles. The evaluation methodology with metrics like Θ and D(t) can be adopted for Odin's system evaluation framework."
  directly_justifies:
    - "Runtime contracts can detect 5.2–6.8 soft violations per session that are otherwise invisible."
    - "Hard constraint compliance reaches 88–100% with contract enforcement."
    - "Behavioral drift can be bounded to D* < 0.27 using contracts with recovery rate γ > α."
    - "Recovery mechanisms transform exponential compliance decay into linear decay."
    - "Contract components are non-redundant; each contributes meaningfully to reliability."
  limits:
    - "Evaluation primarily on financial advisory domain; broader validation across spending/forecasting is needed."
    - "State extraction from raw agent output is outside the framework's scope."
    - "Reference distribution for drift calibration requires dedicated setup."
    - "Compositionality relies on conditional independence assumptions that may not hold in shared-LLM pipelines."
  mapping_rationale: "A systematic scan across all 12 functional domains and their canonical topic codes was performed. The paper is fundamentally algorithmic, proposing and evaluating a runtime enforcement framework for AI agents. Domains flagged as relevant include: Anomaly Detection (8.A, 8.B) because the contract violation detection directly addresses anomaly detection; Behavioral Profiling (5.A, 5.B, 5.C) due to the drift monitoring and classification via compliance; System Evaluation (12.A, 12.B) because the paper introduces a comprehensive evaluation methodology. Domain 11 (Engagement/Retention) is contextual, as recovery mechanisms support engagement but are not the primary focus. Domains rejected include: Filipino Cultural Context (2.A–2.D), Expense Categorization (3.A–3.C), Existing Systems (4.A–4.B), Spending Forecasting (6.A–6.B), Budget Recommendation (7.A–7.D), Mobile-First Design (9.A–9.B), Data Privacy (10.A–10.B), and Savings/Debt Management (13.A–13.C) because the paper does not address these PFMS-specific concerns. Overall, the paper provides high relevance for runtime enforcement, anomaly detection, and system evaluation modules in Odin."
limitations:
  - "Requires structured state dictionary for constraint evaluation; feature extraction is out of scope. [unacknowledged]"
  - "Reference distribution for drift calibration must be established manually. [unacknowledged]"
  - "Default recovery is monitoring-only; domain-specific recovery logic must be implemented. [unacknowledged]"
  - "Stationarity assumptions in drift bounds may not hold for short sessions. [unacknowledged]"
  - "Compositionality bound becomes optimistic under correlated LLM failures. [acknowledged]"
remember_this:
  - "Contracts detect 5.2–6.8 soft violations per session invisible without monitoring."
  - "Hard constraints achieve 88–100% compliance with runtime enforcement."
  - "Behavioral drift is bounded to D* < 0.27 using contracts with recovery."
  - "Recovery transforms exponential compliance decay into linear decay."
  - "Each contract component is non-redundant; removing recovery drops reliability by 0.20."
```