```yaml
paper_id: 10.12720/jait.17.2.378-389
designation: local
title: Benchmarking Federated Learning in Edge Computing Environments: A Systematic Review and Performance Evaluation
authors: Aribe, S. G.; Cagande, G. N. T.
year: 2026
venue: Journal of Advances in Information Technology
odin_topics:
  - 4.A
  - 4.B
  - 5.C
  - 6.B
  - 8.B
  - 12.A
  - 12.B
  - 12.C
tldr: A systematic review and performance evaluation of federated learning techniques for edge computing, categorizing methods across optimization, communication, privacy, and architecture, with benchmark results showing trade-offs between accuracy, efficiency, and robustness.
problem_and_motivation: The intersection of federated learning (FL) and edge computing lacks a comprehensive review that not only categorizes techniques but also systematically benchmarks them against practical performance metrics relevant to edge scenarios. This gap hinders the selection and deployment of FL methods in resource-constrained, privacy-sensitive edge environments.
approach:
  - Followed a PRISMA-inspired and SALSA-guided systematic review methodology.
  - Searched six academic databases (IEEE Xplore, Scopus, SpringerLink, ScienceDirect, ACM DL, arXiv) for peer-reviewed papers from January 2017 to June 2025.
  - Initial search yielded 602 articles; 308 were retained after duplicate removal and applying inclusion/exclusion criteria.
  - Extracted data using a standardized template covering FL algorithm, datasets, deployment environment, and performance metrics.
  - Classified extracted studies into a four-dimensional taxonomy: optimization strategies, communication efficiency, privacy-preserving mechanisms, and system architecture.
  - Benchmarked five leading FL algorithms (FedAvg, FedProx, SCAFFOLD, FedNova, FedAvg+DP) across metrics including accuracy, convergence time, communication overhead, energy consumption, and non-IID robustness.
findings:
  - num: SCAFFOLD achieved the highest accuracy (84.7% on Shakespeare) and robust non-IID performance.
  - num: FedAvg demonstrated superior communication efficiency (45 MB/round) and energy use (38 Joules/round).
  - num: FedAvg+DP showed a noticeable performance penalty (74.1% accuracy on CIFAR-10), highlighting the privacy-utility trade-off.
  - FEMNIST (3400 clients) and Shakespeare (1126 clients) are identified as the most representative datasets for real-world edge conditions due to high non-IID severity.
  - Open challenges persist in data heterogeneity, energy efficiency, communication overhead, privacy preservation, and benchmarking reproducibility.
  - No single algorithm dominates across all criteria; selection depends on specific edge deployment priorities.
key_figures_tables:
  - Table I: Performance matrix comparing FL algorithms across datasets and metrics → SCAFFOLD leads in accuracy/robustness, FedAvg leads in efficiency.
  - Figure 3: Taxonomy diagram of FL techniques for edge computing → Visual classification into four primary methodological dimensions.
  - Figure 4: Comparison of benchmark datasets by client count and non-IID severity → FEMNIST and Shakespeare are the most challenging.
  - Figure 5: Radar plot of relative performance across five metrics → Visualizes trade-offs and highlights algorithm-specific strengths.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: FL
    definition: Federated Learning; a decentralized machine learning approach where multiple clients collaboratively train a shared model without sharing raw data.
  - term: Edge Computing
    definition: A decentralized computing paradigm that processes data at or near the source of data generation.
  - term: non-IID
    definition: Non-Independent and Identically Distributed; refers to statistical heterogeneity in data across clients.
  - term: FedAvg
    definition: Federated Averaging; a baseline FL algorithm that averages locally computed gradients or weights from selected clients.
  - term: FedProx
    definition: An FL algorithm introducing a proximal term to limit local update divergence and improve convergence under heterogeneous data.
  - term: SCAFFOLD
    definition: An FL algorithm using control variates to correct for client-drift caused by non-IID data.
  - term: Differential Privacy (DP)
    definition: A privacy-preserving technique that adds calibrated noise to local updates or global aggregations.
  - term: Secure Aggregation
    definition: A cryptographic protocol that enables secure aggregation of model updates without revealing individual contributions.
  - term: Communication Overhead
    definition: The amount of data transmitted between clients and servers per communication round, typically measured in megabytes.
critical_citations:
  - "[McMahan et al., 2016] — Introduces FedAvg, the foundational FL algorithm."
  - "[Li et al., 2020] — Surveys FL challenges and methods, including FedProx."
  - "[Karimireddy et al., 2019] — Proposes SCAFFOLD for improving FL convergence."
  - "[Kairouz et al., 2021] — Comprehensive review of advances and open problems in FL."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides a high-level framework for evaluating decentralized systems, though not finance-specific.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies limitations in FL (heterogeneity, energy, privacy) relevant to evaluating PFMS architecture gaps.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Discusses FL as a distributed classification framework; can inform profile classification design.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: contextual
      justification: Provides benchmarking methodology that can be adapted for evaluating forecasting algorithms.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Federated anomaly detection is mentioned as a future application, providing foundational context.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a structured benchmarking framework (metrics, datasets) directly applicable to evaluating Odin's modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Benchmarks FL algorithms using accuracy, convergence, communication, and energy metrics, directly transferable to Odin's module evaluation.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: The comparative matrix and radar plot methodologies offer a template for evaluating budget recommendation algorithms.
  contribution: This paper provides a systematic evaluation framework comprising performance metrics (accuracy, convergence, communication, energy, robustness) and a multi-dataset benchmarking methodology that is directly applicable to Odin's algorithmic modules. The taxonomy of FL techniques informs the design of distributed and privacy-preserving components within Odin's architecture. The comparative matrix and radar plot visualization offer a clear template for evaluating trade-offs between different recommendation or anomaly detection strategies. The identification of open challenges (heterogeneity, energy, privacy, reproducibility) highlights critical considerations for Odin's deployment and long-term viability.
  directly_justifies:
    - "Federated learning enables privacy-preserving distributed model training without sharing raw data, supporting Odin's data privacy requirements."
    - "Systematic benchmarking using multiple datasets and metrics is essential for evaluating Odin's algorithmic modules."
    - "No single algorithm dominates across all metrics, so Odin's algorithm selection must align with specific deployment priorities."
    - "Energy efficiency is a key constraint for edge deployments that should be considered in Odin's mobile-first design."
  limits:
    - "The review synthesizes simulation-based results; real-world deployment performance may differ."
    - "Does not evaluate FL algorithms specifically for personal finance or spending data."
    - "Focuses on horizontal FL; vertical FL and federated transfer learning are not systematically benchmarked."
    - "Energy consumption values are normalized across studies, not based on consistent hardware."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated canonical topic codes was conducted. The paper was flagged as relevant for the System Evaluation domain (codes 12.A, 12.B, 12.C) with high relevance because it provides a structured benchmarking framework, performance metrics, and comparative analysis methodology that directly apply to evaluating Odin's algorithmic modules. It was also relevant for Existing Systems & Gaps (codes 4.A, 4.B) with medium relevance due to its identification of systemic limitations in distributed learning systems. Behavioral Profiling & Classification (5.C), Forecasting (6.B), and Anomaly Detection (8.B) were assigned low/contextual relevance as the paper's distributed classification and anomaly detection discussions provide foundational context but are not directly finance-specific. The paper was considered but rejected for other domains such as Filipino Cultural Context, Expense Categorization, Budget Recommendation, Mobile-First Design, Data Privacy, User Retention, Savings & Debt Management as it does not address these financial or user-centric aspects. Overall, the paper's primary relevance to Odin lies in its evaluation framework and benchmarking methodology.
limitations:
  - "Benchmarking results are based on simulated edge environments, not real-world deployments. [unacknowledged]"
  - "The review does not evaluate FL algorithms on personal finance datasets, limiting direct applicability to Odin. [unacknowledged]"
  - "Energy consumption results are derived from disparate hardware platforms, making cross-study comparison difficult."
  - "Privacy metrics are proxied by the presence of DP or secure aggregation, rather than measured leakage risk."
  - "The review does not consider cross-silo FL scenarios, which may be relevant for multi-institutional financial data collaboration. [unacknowledged]"
remember_this:
  - "SCAFFOLD achieved the highest accuracy (84.7%) and robustness to non-IID data."
  - "FedAvg was the most communication-efficient (45 MB/round) and energy-efficient (38 J/round)."
  - "No single FL algorithm dominates all metrics; selection depends on deployment priorities."
  - "FEMNIST and Shakespeare best simulate real-world non-IID edge data conditions."
  - "Privacy enhancement via DP incurs a significant accuracy and convergence penalty."
```