```yaml
paper_id: f47ac10b-58cc-4372-a567-0e02b2c3d479
designation: international-algorithm-specific
title: Agent Behavioral Contracts: Formal Specification and Runtime Enforcement for Reliable Autonomous AI Agents
authors: Bhardwaj, V. P.
year: 2026
venue: arXiv
odin_topics:
  - 4.B
  - 5.B
  - 8.A
  - 8.B
  - 8.C
  - 10.A
  - 10.B
  - 12.A
  - 12.B
tldr: A formal framework for behavioral contracts enables runtime enforcement, drift detection, and recovery for autonomous AI agents, making violations measurable and bounds provable.
problem_and_motivation: Large language model agents lack formal behavioral specifications, leading to undetected drift and governance failures. Existing approaches like prompts and guardrails cannot provide runtime guarantees or compositionality. This paper addresses the need for a contract-based framework with probabilistic compliance and bounded drift.
approach:
  - Define Agent Behavioral Contracts as a tuple of preconditions, invariants (hard/soft), governance constraints, and recovery mechanisms.
  - Introduce (p,δ,k)-satisfaction to account for LLM non-determinism with bounded recovery windows.
  - Model drift as an Ornstein-Uhlenbeck process and prove a drift bound theorem with closed-form design criterion.
  - Implement ContractSpec DSL and AgentAssert runtime library with sub-10ms per-action overhead.
  - Evaluate on 7 models from 6 vendors using AgentContract-Bench across 1,980 sessions, comparing contracted vs uncontracted agents.
findings:
  - "num: 5.2-6.8 soft violations per session detected in contracted agents, versus 0.0-0.3 in uncontracted (p<0.0001, Cohen's d=6.7-33.8)."
  - "num: Hard compliance reached 88-100% under contract, with 100% for GPT-5.2 and GPT-4o-mini."
  - "num: Behavioral drift was bounded to D*<0.27 over 12-turn sessions, matching OU mean-reversion (R2=0.49-0.75)."
  - "num: Recovery re-prompting achieved 100% success for frontier models; average 67% across all models."
  - "num: Runtime overhead remained below 10ms per action, <1% of LLM inference latency."
key_figures_tables:
  - "Table 9: E1 results across 7 models → Contracted agents detect 5.2–6.8 soft violations vs 0.0–0.3 in uncontracted."
  - "Figure 2: Drift trajectory over 12-turn sessions → Contracted drift stabilizes and remains bounded, while uncontracted has no measurable drift."
  - "Figure 3: OU model fit → Drift dynamics match mean-reversion with R2=0.49–0.75."
  - "Figure 4: Ablation heatmap → Removing recovery or soft constraints degrades reliability index by ∼0.20."
  - "Figure 5: Runtime overhead scaling → Overhead scales linearly with constraints, below 10ms for typical contracts."
key_equations:
  - equation: "C_hard(t) = |{c ∈ I_hard ∪ G_hard : c(s_t,a_t)=true}| / |I_hard ∪ G_hard|"
    explanation: "Fraction of satisfied hard constraints."
  - equation: "C_soft(t) = |{c ∈ I_soft ∪ G_soft : c(s_t,a_t)=true}| / |I_soft ∪ G_soft|"
    explanation: "Fraction of satisfied soft constraints."
  - equation: "P(∀t: C_hard(t)=1) ≥ p and P(∀t: C_soft(t)<1-δ ⇒ ∃t'≤t+k: C_soft(t')≥1-δ) ≥ p"
    explanation: "(p,δ,k)-satisfaction with hard persistent and soft recoverable guarantees."
  - equation: "dD = (α - γD)dt + σdW(t)"
    explanation: "OU drift dynamics with injection rate α and recovery rate γ."
  - equation: "π_D = N(α/γ, σ²/(2γ))"
    explanation: "Stationary drift distribution with mean α/γ and variance σ²/(2γ)."
  - equation: "γ ≥ (2αD_max + σ² ln(1/ε) + sqrt((2αD_max + σ² ln(1/ε))² - 4α²D_max²)) / (2D_max²)"
    explanation: "Minimum recovery rate to keep drift below D_max with confidence 1-ε."
definitions:
  - term: ABC
    definition: "Agent Behavioral Contracts: formal framework for agent specification and enforcement."
  - term: OU
    definition: "Ornstein-Uhlenbeck: stochastic process with mean-reversion."
  - term: JSD
    definition: "Jensen-Shannon divergence: symmetric measure of distributional distance."
  - term: SPRT
    definition: "Sequential Probability Ratio Test: sequential hypothesis test for compliance certification."
  - term: (p,δ,k)-satisfaction
    definition: "Probabilistic contract compliance with probability p, tolerance δ, recovery window k."
critical_citations:
  - "[Meyer, 1992] — Design-by-Contract foundational work."
  - "[Bai et al., 2022] — Constitutional AI training-time alignment."
  - "[Wang et al., 2026a] — Impossibility of safety invariance without external correction."
  - "[Rath, 2026] — Behavioral drift in multi-agent LLM systems."
relevance:
  topics:
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: "Paper identifies gaps in existing agent guardrails and provides formal contracts."
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: "Requires reference distribution calibration, analogous to cold-start baseline."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: "Violation detection is a form of anomaly detection applicable to spending."
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: "Proposes constraint evaluation and drift detection algorithms."
    - code: 8.C
      name: Cold‑Start Baseline Strategies for Anomaly Detection
      relevance: medium
      justification: "Reference distribution serves as cold-start baseline."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: "Hard invariants enforce PII and data protection, directly relevant."
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: "Contracts build trust through enforceability and transparency."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: "Introduces benchmark and metrics for evaluating contract enforcement."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: "Provides empirical evaluation of the enforcement algorithm across models."
  contribution: "The ABC framework's hard/soft constraint separation and drift detection can inform Odin's anomaly detection module by providing formal violation metrics and leading indicators. The reference distribution calibration addresses Odin's cold-start problem for user profiling. The compositionality theorem supports evaluating multi-agent pipelines, applicable to Odin's modular architecture. The runtime enforcement and recovery mechanisms offer a template for ensuring data privacy and user trust in financial systems."
  directly_justifies:
    - "Runtime contract enforcement detects soft violations that would otherwise be invisible."
    - "Recovery mechanisms convert exponential compliance decay into linear decay."
    - "Contracts with recovery rate γ > α bound behavioral drift to α/γ in expectation."
    - "Hard constraints can enforce zero-tolerance privacy and security policies."
    - "Reference distribution calibration enables cold-start baseline for drift detection."
  limits:
    - "State dictionary assumption: contract predicates require pre-computed features."
    - "Reference distribution must be calibrated; no automated recalibration for non-stationary environments."
    - "Recovery is monitoring by default; deployers must implement custom recovery handlers."
    - "k-window stationarity assumption may be optimistic for short sessions."
    - "Compositionality under correlated failures may be optimistic."
    - "Benchmark circularity: synthetic traces test engine consistency, not live behavioral detection."
  mapping_rationale: "All 12 functional domains were systematically scanned for relevance. The paper most directly informs the Existing Systems & Gaps (4.A, 4.B), Anomaly Detection (8.A, 8.B, 8.C), Data Privacy & User Trust (10.A, 10.B), and System Evaluation (12.A, 12.B) domains. It also touches on Behavioral Profiling (5.B) via cold-start drift detection. Cultural, expense categorization, forecasting, budget recommendation, mobile design, retention, and savings/debt domains were considered but rejected as the paper does not address those specific financial constructs. The overall relevance is medium-to-high for governance and evaluation modules."
limitations:
  - "State dictionary assumption: contract predicates require pre-computed features."
  - "Reference distribution must be calibrated; no automated recalibration for non-stationary environments."
  - "Recovery is monitoring by default; deployers must implement custom recovery handlers."
  - "k-window stationarity assumption may be optimistic for short sessions."
  - "Compositionality under correlated failures may be optimistic."
  - "Benchmark circularity: synthetic traces test engine consistency, not live behavioral detection."
remember_this:
  - "Contracted agents detect 5.2–6.8 soft violations per session that baselines miss."
  - "Hard compliance reaches 88–100% across models under contract enforcement."
  - "Drift is bounded to D*<0.27 over extended sessions with OU dynamics."
  - "Runtime overhead is under 10ms per action, negligible relative to inference."
  - "Recovery mechanisms significantly improve reliability, with ∼0.20 Θ degradation when removed."
```