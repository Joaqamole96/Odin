```yaml
paper_id: 10.3390/fi18030156
designation: international-algorithm-specific
title: Adaptive Healthcare Monitoring Through Drift-Aware Edge-Cloud Intelligence
authors: Stojnev Ilic, A.; Ilic, M.; Stojanovic, N.; Stojanovic, D.
year: 2026
venue: Future Internet
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 9.A
  - 9.B
  - 10.A
  - 12.A
tldr: Drift-aware edge-cloud architecture elevates concept drift to a supervisory signal for adaptive model lifecycle, user reclassification, and inference consistency in non-stationary healthcare streams.
problem_and_motivation: Physiological data streams are inherently non-stationary, causing static models to deteriorate. Treating drift as a maintenance signal is insufficient for systems requiring continuous, accurate, and resource-efficient inference, particularly in distributed IoT environments.
approach:
  - Proposed a drift-aware multi-tier edge-cloud architecture with hierarchical drift handling: lightweight screening at the edge, rigorous validation in the cloud.
  - Edge nodes perform low-latency inference and preliminary drift screening under resource constraints using a four-detector ensemble.
  - Cloud tier executes advanced drift validation, orchestrates user reclassification, model retraining, and manages model evolution via a feedback loop.
  - The system integrates a Model-as-a-Service component for model distribution, versioning, and atomic deployment to edge devices.
  - Evaluated on a containerized testbed with 20 synthetic multi-user streams and one real continuous glucose monitoring dataset.
findings:
  - num: 40.6% reduction in prediction MAE compared to periodic retraining.
  - num: End-to-end adaptation latency from drift onset to edge deployment was 66 ± 37 seconds.
  - num: Hierarchical cloud validation reduced the false-positive retraining rate from 88.9% (edge-only) to 27.3%.
  - The system maintained uninterrupted inference throughout all adaptation events.
  - Dynamic user-state modeling successfully reduced retraining frequency by reassigning users to compatible model ensembles.
key_figures_tables:
  - Figure 3: End-to-end execution timeline for multiple users → Drift events trigger a coordinated validation, retraining, and deployment pipeline.
  - Figure 4: Prediction error over time for real CGM user → Drift-aware adaptation prevents performance degradation and triggers timely model updates.
  - Table 4: System-level performance metrics → Quantifies detection delay, validation pass rate, and latency of the feedback loop.
key_equations:
  - equation: "P(X, y) changes between t and t+∆t"
    explanation: Formal definition of concept drift occurrence.
definitions:
  - term: Concept Drift
    definition: Temporal changes in data distributions or in the relationship between input features and target variables.
  - term: CGM
    definition: Continuous Glucose Monitoring, a representative sensing modality generating minute-level physiological data.
  - term: MaaS
    definition: Model-as-a-Service, a logical service responsible for model distribution, version management, and deployment coordination.
critical_citations:
  - "[Webb et al., 2016] — Formalizes concept drift in streaming data."
  - "[Lu et al., 2020] — Comprehensive review of concept drift adaptation."
  - "[Gkonis et al., 2023] — Survey on challenges in IoT-edge-cloud continuum."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Proposes a drift-aware framework for continuous adaptation of predictive models on streaming data.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: The architecture explicitly addresses forecasting on sequential, non-stationary data streams.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: The system's goal includes anomaly detection on glucose streams, a relevant analog for spending anomaly detection.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: The edge tier operates on resource-constrained devices, aligning with mobile-first constraints.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: contextual
      justification: Mentions a user-facing component for visualization and actions, relevant to mobile UX, but not a primary focus.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Acknowledges privacy as a future direction but does not directly address security mechanisms.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a concrete system-level evaluation methodology and performance baselines for adaptive systems.
  contribution: "The architecture provides a blueprint for building drift-aware financial management systems where user spending patterns evolve over time. The hierarchical drift-handling strategy can be directly applied to detect and adapt to changing financial behavior, preventing budget recommendations from becoming outdated. The feedback loop and MaaS integration offer a design for continuous model improvement in a PFMS. The evaluation methodology, particularly the use of real-world data to validate adaptation, sets a precedent for evaluating such systems in Odin."
  directly_justifies:
    - "Concept drift should be elevated from a maintenance signal to a primary mechanism governing system adaptation."
    - "Hierarchical drift detection with edge screening and cloud validation is essential for balancing responsiveness and stability."
    - "User reclassification to compatible model states can reduce unnecessary retraining and computational cost."
    - "Asynchronous adaptation is sufficient to preserve continuous inference during system updates."
    - "A feedback loop decoupling inference, retraining, and deployment reduces operational risk."
  limits:
    - "Evaluation is conducted in a containerized environment that does not fully replicate real-world network instability."
    - "The dataset is limited to one physiological signal (CGM), requiring further validation on financial transaction data."
    - "User reclassification strategy is demonstrated but not subjected to a comparative quantitative analysis of optimality."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The domains flagged as highly relevant were Spending Forecasting (6.A, 6.B), as the core contribution is a forecasting pipeline for non-stationary data; Anomaly Detection (8.A), as the system performs anomaly detection; and System Evaluation (12.A), due to its rigorous evaluation framework. Mobile-First Design (9.A, 9.B) was assigned medium/contextual relevance due to the edge deployment constraints and user-facing components. Data Privacy (10.A) was noted as a future work, hence contextual. Domains such as Filipino Cultural Context (2.A-D), Expense Categorization (3.A-C), and User Retention (11.A-B) were considered and rejected as they are outside the scope of this algorithmic architecture paper. The architecture is highly relevant to Odin as it provides a concrete, validated design for an adaptive inference system that can manage evolving user behavior."
limitations:
  - "Evaluation was conducted in a containerized testbed, not a real-world distributed network with instability."
  - "Only evaluated on CGM data; applicability to financial transaction streams requires further validation. [unacknowledged]"
  - "Quantitative analysis of user reclassification optimality is deferred to future work."
  - "Considerations for privacy, regulatory compliance, and security are explicitly beyond the current scope."
remember_this:
  - "Drift-aware adaptation reduced prediction MAE by 40.6% compared to periodic retraining."
  - "Hierarchical cloud validation cut false-positive retraining rates from 88.9% to 27.3%."
  - "Concept drift must be treated as a first-class system event, not passive monitoring."
  - "Asynchronous retraining and deployment preserves continuous inference during updates."
  - "User reclassification to existing model states can effectively limit retraining frequency."
```