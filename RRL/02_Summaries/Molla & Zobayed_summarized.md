```yaml
paper_id: 10.32996/jcsts.2026.5.7.3
designation: international
title: Artificial Intelligence for High-Stakes Decision Support: Architectures, Applications, and Deployment Challenges
authors: Molla, S.; Zobayed, S.
year: 2026
venue: Frontiers in Computer Science and Artificial Intelligence
odin_topics:
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 11.A
  - 12.A
  - 12.B
  - 12.C
tldr: A cross-domain taxonomy and critical review of AI architectures and deployment concerns for high-stakes decision support, identifying shared challenges and future research priorities.
problem_and_motivation: Existing reviews of AI in decision support focus narrowly on single domains, leaving cross-domain structural similarities and shared deployment challenges underexamined. A review spanning multiple high-stakes domains is needed to map recurring architectural patterns, deployment tensions, and governance gaps.
approach:
  - A structured critical review of 79 papers across six application domains: healthcare, assistive AI, smart infrastructure, agriculture, business, and cybersecurity.
  - Uses a four-axis taxonomy to classify papers by application domain, data modality, architecture family, and deployment concern.
  - Covers eight architecture families, from conventional machine learning and CNNs to vision transformers, graph neural networks, Bayesian models, and federated learning.
  - Synthesizes evidence on deployment-critical properties like explainability, robustness, privacy, real-time feasibility, and governance readiness.
  - Identifies shared failure modes and proposes a staged evidence-readiness framework for high-stakes AI deployment.
findings:
  - Architecture selection in high-stakes AI is shaped by deployment constraints including computational resources, privacy requirements, interpretability obligations, and human oversight needs.
  - Explainability is the most consistently addressed deployment requirement across all six application domains, primarily through post-hoc attention visualization and saliency mapping.
  - Privacy-preserving AI and federated learning are emerging as operational requirements in health, workforce, and government contexts.
  - Real-time inference on resource-constrained devices is a deployment-critical requirement in IoT, agricultural, and clinical point-of-care contexts.
  - The corpus reveals inconsistent benchmarking practices, including a lack of cross-institutional validation and shared reporting standards.
key_figures_tables:
  - "Figure 1: End-to-end pathway for high-stakes AI decision-support → Maps lifecycle from data to governance."
  - "Figure 2: Shared failure modes in high-stakes AI deployment → Highlights data, model, environmental, and governance risks."
  - "Table 1: Human-AI interaction modes and accountability boundaries → Distinguishes informative, assistive, deferral, collaborative, and autonomous modes."
  - "Table 2: Evidence-readiness levels for high-stakes AI studies → Six-stage framework from proof-of-concept to post-deployment monitoring."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "AI"
    definition: "Artificial intelligence"
  - term: "CNN"
    definition: "Convolutional neural network"
  - term: "ViT"
    definition: "Vision transformer"
  - term: "GNN"
    definition: "Graph neural network"
  - term: "XAI"
    definition: "Explainable artificial intelligence"
  - term: "IoT"
    definition: "Internet of Things"
  - term: "EEG"
    definition: "Electroencephalography"
critical_citations:
  - "[78, 2026] — Framework for trustworthy AI in high-stakes decision support."
  - "[79, 2026] — Edge-cloud-6G-federated learning for secure auditable decision support."
  - "[76, 2026] — AI-enabled management information systems for economic resilience and governance."
  - "[75, 2026] — Resilience-by-design AI for security, sustainability, and health."
  - "[16, 2025] — Discusses the prospect of full autonomy in underwater robotics and human oversight."
relevance:
  topics:
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Reviews the broad landscape of AI decision-support systems, providing context for PFMS."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Identifies gaps in explainability, robustness, privacy, and governance relevant to PFMS."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "contextual"
      justification: "Discusses classification approaches that can be applied to user profiling."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "contextual"
      justification: "Discusses data scarcity challenges that are relevant to cold-start profiling."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews forecasting algorithms that are directly relevant to spending prediction."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "medium"
      justification: "Discusses LSTM and gradient boosting models applicable to sequential spending forecasting."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "contextual"
      justification: "Provides a general review of decision-support architectures, relevant to budget recommendation."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews AI systems that provide recommendations, relevant to budget generation."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses robustness and distribution shift, key concerns for anomaly detection."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "medium"
      justification: "Reviews various ML algorithms that can be applied to anomaly detection."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "low"
      justification: "Mentions web-based and edge deployment, touching on mobile-relevant constraints."
    - code: "9.B"
      name: "Mobile UX Design for Personal Finance"
      relevance: "contextual"
      justification: "Discusses human oversight and interface design for decision support."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "Explicitly addresses privacy-preserving AI, federated learning, and security as critical deployment concerns."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "high"
      justification: "Emphasizes explainability and trustworthy AI as essential for building user trust."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "low"
      justification: "Discusses human-in-the-loop and collaborative systems, which relate to engagement."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Proposes an evidence-readiness framework and criticizes inconsistent benchmarking."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Reviews how algorithm performance is evaluated across domains, applicable to PFMS modules."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "medium"
      justification: "Discusses the need for standardized evaluation of decision-support systems."
  contribution: "This review provides a cross-domain taxonomy and a structured synthesis of AI architectures and deployment challenges for high-stakes decision support. It offers Odin a consolidated evidence base for selecting appropriate architectures (e.g., lightweight CNNs for mobile inference, ensemble methods for recommendation) and for prioritizing deployment requirements. It directly justifies the need for explainable AI, privacy-preserving techniques, and robust evaluation frameworks. The paper's evidence-readiness framework can guide the development and validation of Odin's algorithmic modules."
  directly_justifies:
    - "Privacy-preserving AI is an operational requirement in health and workforce contexts, relevant to user financial data."
    - "Explainability mechanisms must be preserved under deployment constraints, such as web-based inference."
    - "Human oversight is a structural requirement in high-stakes AI, supporting a human-in-the-loop design for budget recommendations."
    - "Real-time feasibility on resource-constrained devices is critical for edge deployment in IoT and point-of-care contexts."
  limits:
    - "Review is based on titles only, preventing the extraction of specific performance metrics or experimental protocols. [unacknowledged]"
    - "The corpus reflects a curated selection and may not represent all active research threads (e.g., legal AI, autonomous vehicles)."
    - "Cross-domain comparison is difficult due to inconsistent benchmarking practices across domains."
  mapping_rationale: "A systematic scan across all 12 functional domains and their 30 associated topic codes was performed. The review's focus on cross-domain AI architectures and deployment challenges provides strong evidence for topics related to system evaluation (12.A, 12.B, 12.C), data privacy and trust (10.A, 10.B), and predictive modeling (6.A, 6.B). It offers medium relevance to anomaly detection (8.A, 8.B), budgeting (7.A, 7.B), and existing systems (4.A, 4.B) by reviewing applicable algorithms and gaps. Topics on mobile-first design (9.A, 9.B) and engagement (11.A) received lower or contextual relevance as the paper does not directly address UX or retention. The paper is highly relevant to Odin as it provides a comprehensive framework for selecting, evaluating, and deploying the AI modules that underpin a PFMS, especially in terms of privacy, explainability, and robust evaluation."
limitations:
  - "The synthesis is thematic and architectural rather than quantitative, as it is based on titles only. [unacknowledged]"
  - "Full paper-level extraction is required for meta-analytic comparison of model performance."
  - "The taxonomy represents one defensible organization, not the only possible one."
  - "Domains such as legal AI, financial systemic risk, and autonomous vehicles are not well represented."
remember_this:
  - "Privacy-preserving AI is an operational requirement in financial and health systems."
  - "Explainability is the most consistently addressed deployment requirement across all domains."
  - "Human oversight is a structural requirement for trustworthy high-stakes AI systems."
  - "Cross-domain benchmarking and standardized reporting standards are critical research gaps."
  - "Architecture selection is shaped by deployment constraints like privacy, real-time feasibility, and governance."
```