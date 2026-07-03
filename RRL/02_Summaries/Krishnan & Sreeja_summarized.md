```yaml
paper_id: 10.1109/ACCESS.2026.3695458
designation: international-algorithm-specific
title: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems: A Formal Framework for Continuous Verification
authors: Krishnan, V.; Sreeja, C.S.
year: 2026
venue: IEEE Access
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 8.A
  - 8.B
  - 8.C
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
  - 12.C
tldr: A Zero-Trust Hybrid Adaptive Authentication (ZeTHAA) framework integrating continuous authentication, probabilistic risk modeling, and dual-policy thresholds for security-usability trade-offs.
problem_and_motivation: Existing adaptive authentication systems lack formal mathematical models for continuous trust evolution, often relying on heuristic scoring and binary decisions. This gap leads to either excessive user friction or inadequate security, especially in post-login authorization.
approach:
  - The ZeTHAA framework models trust as a continuous, time-evolving state variable rather than a binary policy outcome.
  - It integrates a composite attribute set covering user, device, application, and contextual signals into a unified risk metric.
  - Attribute importance and penalties are dynamically derived from entropy and Beta-posterior distributions, enabling robust cold-start initialization.
  - A global admissibility predicate distinguishes hard violations from soft probabilistic violations for clear enforcement.
  - The system incorporates retry dynamics with exponential risk escalation and temporal decay into a unified threat model.
  - Evaluation uses a large-scale synthetic dataset with realistic authentication flows and adversarial patterns against multiple baselines.
findings:
  - num: ZeTHAA outperformed baselines with Recall and Area Under the Curve (AUC) exceeding 79% and 15.1%, respectively.
  - num: F1-Scores showed increases of 48%-147%, with efficiency boost of 20-65%, while reducing the cost per attack by up to 39.6%.
  - num: Benchmarks against frameworks from Dasu et al. and Matiushin et al. showed a 57.5% lead in F1-Score.
  - num: ZeTHAA blocked 70.78% more attacks than comparable frameworks.
  - The framework achieves a 33% reduction in Equal Error Rate compared to a heuristic approach.
  - The risk distribution shows a clear separation between benign and attack events, enabling logical threshold placement.
  - Detection latency is immediate with a 95th percentile delay of 0 events for strong contextual signals.
key_figures_tables:
  - Figure 1: ZeTHAA system architecture highlighting the composite attribute set and policy enforcement points → Shows integration of continuous monitoring and authorization.
  - Figure 2: Feature importance from Bayesian calibration → Attack campaign and geo-anomaly signals dominate risk.
  - Figure 3: Risk score distribution by class → Clear separation between benign and attack sessions.
  - Figure 4: Policy decision with risk score distribution → Shows the three decision regions: allow, step-up, block.
  - Figure 5: ROC curve comparison across models → ZeTHAA achieves highest TPR at low FPR.
  - Figure 6: Risk-trust correlation → High risk correlates with low trust, diagonal trend supports classification.
  - Figure 8: Cost vs attack detection recall → Framework balances security and usability effectively.
  - Table 13: Performance metrics → ZeTHAA achieves 0.735 recall, 0.874 AUC, F1-score of 0.761.
  - Table 21: Performance comparison between baselines → ZeTHAA leads in recall and AUC.
key_equations:
  - equation: T(t) = (1 - λ^+ - λ^+·C(t) - γ)·T(t-) + R(t)
    explanation: Dynamic trust update based on context and risk.
  - equation: Pr[AttackSuccess|C(t)] = 1 - (1 - Pr[Attack_auth|C(t)])·(1 - Pr[Attack_authz|C(t)])
    explanation: Unified attack success probability combining authentication and authorization phases.
  - equation: Trust(C(t)) = Σ w_i(t) Indicator[match(a_i)] - Σ π^miss_i(t) Indicator[missing(a_i)] - Σ π^mm_i(t) Indicator[mismatch(a_i)]
    explanation: Trust as weighted positive evidence minus penalties for missing/mismatched attributes.
definitions:
  - term: Zero-Trust Hybrid Adaptive Authentication (ZeTHAA)
    definition: A framework integrating contextual attributes, authentication strength, behavioral evidence, and retry dynamics for continuous authentication and authorization.
  - term: Global Admissibility Predicate
    definition: A system-wide safety invariant that distinguishes hard violations from soft violations, enabling deterministic security responses.
  - term: Trust
    definition: A continuous, time-evolving, and bounded state variable representing accumulated confidence in a session context.
  - term: Risk
    definition: The estimated probability of adversarial success, distinct from trust, used in authorization decisions.
  - term: Hard Violation
    definition: A non-compensable state (e.g., impossible travel, cryptographic failure) that triggers immediate access denial and session termination.
  - term: Soft Violation
    definition: A statistically unlikely but plausible behavioral deviation that incurs penalties but does not terminate the session.
  - term: Attribute Penalty
    definition: A reactive measure reducing effective trust when contextual attributes mismatch or are missing from expectations.
  - term: Authentication Penalty
    definition: A reactive measure reducing effective authentication assurance due to failures, degradation, or fallback behavior.
critical_citations:
  - "[Dasu et al., 2023] — Heuristic risk scoring with static weights."
  - "[Matiushin and Korkhov, 2025] — ML-empowered RBA with dynamic threshold."
  - "[Rose et al., 2020] — NIST SP 800-207 Zero Trust Architecture principles."
  - "[Temoshok et al., 2025] — NIST SP 800-63 Digital Identity Guidelines."
  - "[Wiefling et al., 2020] — Study on usability and security of risk-based authentication."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Formalizes continuous, time-evolving trust states as behavioral profiles.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: high
      justification: Introduces robust cold-start initialization via entropy and Bayesian priors.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Uses ML strictly for evidence interpretation, not direct decision-making.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Models trust and risk evolution with temporal decay and reinforcement.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Provides a formal anomaly detection framework with hard/soft violations.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Evaluates anomaly detection performance against multiple baselines.
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: high
      justification: Addresses cold-start with Beta-posterior and uniform initialization.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Framework is designed for mobile contexts with device attestation.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Balances security and usability with step-up authentication mechanisms.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Aligns with NIST standards and includes application/device integrity checks.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Models trust as a continuous state to improve user confidence.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses comprehensive metrics including ROC, EER, and operational efficiency.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Evaluates algorithmic components against heuristic and ML baselines.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: contextual
      justification: Provides methodology applicable to evaluating decision-making systems.
  contribution: "The framework formalizes continuous trust computation for adaptive authentication, directly applicable to Odin's behavioral profiling and anomaly detection modules. Its cold-start initialization strategy provides a robust baseline for new users, addressing the cold-start problem in financial behavior modeling. The separation between hard and soft violations informs Odin's design for handling both extreme anomalies and gradual behavioral shifts. The composite attribute set and policy-driven thresholds offer a blueprint for Odin's expense categorization and budget recommendation systems. The unified threat model and attack surface analysis provide a security foundation for Odin's data privacy and user trust modules."
  directly_justifies:
    - "Continuous trust evaluation is essential for Zero-Trust systems and should replace binary decisions in financial applications."
    - "Attribute weights must be dynamically recalibrated using Bayesian learning, not static heuristics."
    - "A global admissibility predicate is required to distinguish impossible states from probabilistic anomalies."
    - "Retry dynamics and temporal decay should be modeled explicitly in threat surfaces."
    - "Multi-threshold decision regions improve security-usability trade-offs compared to single-threshold approaches."
  limits:
    - "Evaluation is conducted on a synthetic dataset, which may not fully capture real-world behavioral complexity."
    - "The framework assumes availability of device capabilities (e.g., TEE, FIDO2) that may not be present in all contexts."
    - "Authentication strength mappings to NIST AALs are indicative and may require calibration for specific implementations."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was conducted. The paper directly addresses behavioral profiling and anomaly detection (Domains 5 and 8) with high relevance, as it formalizes continuous trust states and hard/soft violation handling. It also provides strong justification for mobile-first design and data privacy (Domains 9 and 10) through its focus on device attestation and NIST alignment. The framework's evaluation methodology (Domain 12) is directly applicable to Odin's system evaluation needs. Topics related to expense categorization (Domain 3) and budget recommendation (Domain 7) were considered but rejected, as the paper focuses on authentication rather than financial allocation. Savings and debt management (Domain 13) were considered contextual at best. The paper's contributions to predictive modeling (Domain 6) and engagement (Domain 11) are secondary but relevant. Borderline cases: The paper's treatment of 'trust' as a cumulative state could inform spending pattern modeling (2.D), but the connection is indirect, so it was not selected. Overall, the paper provides high-value methodological and algorithmic insights for Odin's behavioral profiling, anomaly detection, and security architecture."
limitations:
  - "The evaluation relies on a synthetic dataset, limiting generalizability to real-world user behavior. [unacknowledged]"
  - "The framework assumes device capabilities that may not be available in all contexts, such as TEE and FIDO2 support. [unacknowledged]"
  - "Authentication strength mappings are indicative and may require recalibration for specific enterprise deployments."
  - "The dataset does not include long-term behavioral drifts, which could affect profile adaptation strategies. [unacknowledged]"
  - "Computational overhead of continuous monitoring and Bayesian updates is not fully characterized for resource-constrained devices. [unacknowledged]"
  - "The framework does not address user acceptance of continuous step-up challenges, which may impact engagement. [unacknowledged]"
remember_this:
  - "ZeTHAA achieves 15.1% higher AUC and 57.5% better F1-Score than heuristic RBA methods."
  - "Dual thresholds reduce false blocking by 70.78% while maintaining high attack detection."
  - "Continuous trust computation with Bayesian learning enables robust cold-start anomaly detection."
  - "Hard and soft violation separation allows deterministic security responses for impossible states."
  - "Framework aligns with NIST Zero Trust principles, extending security beyond authentication into resource access."
```