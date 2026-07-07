```yaml
paper_id: 10.1007/s43926-026-00358-y
designation: international
title: Systematic review of the internet of things ecosystem for real-time detection of card-not-present (CNP) fraud
authors: Owusu-Mensah, K.; Ansong, E. D.; Adu-Manu, K. S.; Yaokumah, W.
year: 2026
venue: Discover Internet of Things
odin_topics:
  - 4.A
  - 4.B
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
tldr: A systematic review synthesizes 23 studies on IoT-enabled real-time CNP fraud detection, revealing fragmented research that prioritizes accuracy over latency, scalability, privacy, and governance.
problem_and_motivation: Existing CNP fraud detection surveys focus narrowly on algorithmic accuracy, overlooking critical system-level factors like real-time latency, scalability, and privacy-preserving governance. IoT-enabled payment ecosystems introduce contextual data and distributed intelligence, but lack an integrated framework that connects architectural layers, operational constraints, and evaluation metrics. This review addresses the gap by consolidating fragmented evidence into a scenario-aware, multi-layer reference architecture.
approach:
  - A systematic literature search (2015–April 2026) across six databases yielded 1,129 records, which were screened down to 23 peer-reviewed studies using PRISMA 2020 guidelines.
  - A PICO model structured the search strategy and inclusion criteria, focusing on IoT-based fraud detection in CNP environments.
  - A quality assessment checklist scored each study on five criteria (objectives, methodology, dataset, evaluation, relevance).
  - A structured data extraction protocol mapped frameworks to IoT layers, performance metrics, privacy mechanisms, and application scenarios.
  - Thematic synthesis and comparative performance analysis were applied to identify trends, gaps, and design principles.
  - A unified multi-layer IoT-CNP reference architecture was derived from the synthesized evidence.
findings:
  - num: 23 studies were included, with 43% from Asia-Pacific, 26% from Europe, and 22% from North America.
  - num: Federated and split learning achieved near-centralized accuracy (up to 99.94%) while reducing communication costs by up to 35%.
  - num: Latency reporting was inconsistent; only studies with explicit real-time validation (e.g., A14, A16, A20, A23) reported end-to-end decision delays under 30–40 ms.
  - num: Blockchain-supported frameworks achieved throughput up to 113 TPS but introduced confirmation latency and coordination overhead.
  - Predictive accuracy (F1, AUC) remains the dominant metric, but latency, throughput, energy, and communication costs are underreported.
  - Distributed learning models show strong privacy benefits but face challenges with client heterogeneity, non-IID data, and synchronization costs.
  - A unified six-layer IoT-CNP architecture is proposed, separating edge/fog detection from cloud analytics and blockchain governance.
key_figures_tables:
  - Figure 2: PRISMA flow diagram showing screening from 1,129 records to 23 included studies.
  - Table 7: Summary of 23 selected studies with approaches and focus areas.
  - Table 10: Evolution timeline of IoT ecosystem layers in fraud detection from 2015 to 2026.
  - Figure 5: Unified multi-layer IoT fraud detection framework with six architectural layers.
  - Figure 7: CNP transaction lifecycle aligned with IoT ecosystem layers.
key_equations:
  - equation: None.
    explanation: No key equations were presented in the review.
definitions:
  - term: Card-Not-Present (CNP) fraud
    definition: Fraudulent transactions conducted without physical presentation of the payment card.
  - term: Federated Learning (FL)
    definition: A distributed machine learning approach that trains models across decentralized devices without sharing raw data.
  - term: Split Learning (SL)
    definition: A privacy-preserving technique where model layers are split between client and server, sharing activations rather than raw data.
  - term: Edge-Fog Computing
    definition: A distributed computing paradigm that processes data near the source (edge) or intermediate nodes (fog) to reduce latency.
  - term: Internet of Things (IoT)
    definition: A network of interconnected devices that collect, transmit, and process data from the physical world.
  - term: Real-time detection
    definition: Fraud evaluation performed within transaction authorization windows, typically under millisecond latency constraints.
  - term: Non-IID data
    definition: Data that is not independent and identically distributed, common in federated settings with heterogeneous clients.
  - term: Blockchain
    definition: A decentralized, immutable ledger used for auditability, traceability, and governance in financial systems.
critical_citations:
  - "[Page et al., 2021] — Defines the PRISMA 2020 systematic review methodology used."
  - "[Dal Pozzolo et al., 2018] — Provides a realistic modeling approach for credit card fraud detection."
  - "[Yang et al., 2017] — Surveys security and privacy issues in IoT, foundational for privacy-preserving design."
  - "[Bhattacharyya et al., 2011] — Comparative study on data mining for credit card fraud."
  - "[Carcillo et al., 2018] — Scalable framework for streaming credit card fraud detection."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Provides a comprehensive review of IoT-based fraud detection systems, directly mapping to existing PFMS landscapes.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Explicitly identifies fragmentation, inconsistent benchmarking, and lack of governance integration as key gaps.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Core focus is anomaly detection for CNP fraud in IoT-enabled payment environments.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Reviews machine learning, deep learning, federated learning, and graph-based algorithms for fraud anomaly detection.
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: medium
      justification: Discusses adaptive learning and heterogeneity challenges, which relate to cold-start and non-IID data issues.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: contextual
      justification: Edge-assisted mobile payment scenarios are discussed, but mobile-first design is not a primary focus.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: contextual
      justification: UX considerations are implied in application-layer decisions but not explicitly analyzed.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Dedicated sections on federated learning, split learning, and blockchain for privacy-preserving fraud detection.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Trust is addressed through governance, auditability, and explainability mechanisms, though user trust is not directly measured.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Proposes a multi-dimensional benchmarking framework beyond accuracy, including latency, scalability, and trust.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Compares predictive effectiveness, real-time performance, and privacy-preserving algorithms across studies.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: low
      justification: Not directly applicable; the review focuses on fraud detection, not budget recommendation.
  contribution: The review contributes a scenario-aware synthesis that connects IoT architectural placement with CNP fraud detection requirements and evaluation practices. It provides explicit guidance for benchmarking that goes beyond accuracy to include latency, scalability, coordination cost, privacy, and trust indicators. A unified multi-layer IoT-CNP reference architecture is presented, aligning with the CNP transaction lifecycle and consolidating fragmented evidence into a practical deployment-oriented model. This framework directly informs Odin's anomaly detection module (8.A, 8.B) and evaluation strategy (12.A, 12.B). The emphasis on privacy-preserving learning (10.A) and system-level integration (4.A, 4.B) supports Odin's design as a trustworthy, real-time PFMS.
  directly_justifies:
    - "Real-time CNP fraud detection requires latency budgets under transaction authorization windows, typically tens of milliseconds."
    - "Federated and split learning enable collaborative fraud detection without centralizing sensitive transaction data."
    - "Blockchain mechanisms enhance auditability but must be separated from real-time decision paths to avoid latency overhead."
    - "Performance evaluation must include predictive accuracy, latency, throughput, communication cost, and privacy indicators."
    - "Edge-Fog processing reduces response time by moving inference closer to the transaction source."
  limits:
    - "The review is based on 23 studies, which is a focused corpus due to strict eligibility criteria; broader IoT anomaly detection studies were excluded."
    - "Industrial and proprietary fraud detection systems are underrepresented due to limited public disclosure."
    - "The proposed unified framework is analytically derived but has not been empirically validated in a production payment environment."
    - "Reporting inconsistencies in latency, throughput, and energy consumption across studies limit quantitative meta-analysis."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated canonical topic codes was performed. The paper is a review of IoT-based real-time CNP fraud detection. Domains flagged as relevant include: Existing Systems & Gaps (4.A, 4.B) due to its detailed landscape and gap analysis; Anomaly Detection (8.A, 8.B, 8.C) as the core subject; Data Privacy & User Trust (10.A, 10.B) via federated learning and blockchain discussions; and System Evaluation (12.A, 12.B) due to its proposed benchmarking framework. Mobile-First Design (9.A, 9.B) was rated contextual because edge/mobile payments are discussed but not as a design principle. Behavioral Profiling (5.A, 5.B, 5.C) and Spending Forecasting (6.A, 6.B) were considered and rejected as the paper does not address user profiling or predictive spending. Budget Recommendation (7.A–D) and Savings/Debt Management (13.A–C) were not relevant. The paper's overall relevance to Odin is high, as it directly informs the design of anomaly detection, privacy-preserving computation, and system evaluation for a PFMS.
limitations:
  - "Inconsistent reporting of latency, throughput, and energy consumption across studies limits cross-study comparability."
  - "The final corpus of 23 studies is relatively small due to strict inclusion criteria focused on real-time CNP fraud."
  - "Industrial and proprietary fraud detection systems are underrepresented due to limited public disclosure."
  - "The proposed unified framework has not been empirically validated in a real-world payment environment. [unacknowledged]"
  - "Potential bias from studies originating in adjacent IoT anomaly/intrusion detection domains, limiting direct transferability to CNP fraud."
remember_this:
  - "Federated learning achieves near-centralized accuracy while preserving data privacy."
  - "Real-time fraud detection requires latency under 40 ms for transaction authorization."
  - "Blockchain enhances auditability but adds latency and coordination overhead."
  - "Performance benchmarking must include accuracy, latency, throughput, and privacy metrics."
  - "Edge-Fog processing reduces response time and enables scalable IoT fraud detection."
```