```yaml
paper_id: 10.3390/jrfm19020104
designation: international-algorithm-specific
title: Performance, Fairness, and Explainability in AI-Based Credit Scoring: A Systematic Literature Review
authors: Bahlool, R.; Hewahi, N.; Elmedany, W.
year: 2026
venue: Journal of Risk and Financial Management
odin_topics:
  - 5.C
  - 6.B
  - 7.B
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
tldr: A systematic review of 43 studies finds that performance, fairness, and explainability in AI credit scoring are treated in isolation, with limited joint optimization despite regulatory pressures for transparency and non-discrimination.
problem_and_motivation: AI adoption in credit scoring offers strong predictive performance but raises fairness and explainability concerns. Existing research addresses these dimensions in isolation, leaving a gap in understanding their interactions under regulatory and human oversight.
approach:
  - Systematic literature review following PRISMA guidelines, searching IEEE, Scopus, Web of Science, and ScienceDirect.
  - Included 43 peer-reviewed studies from 2020-2025 focusing on AI credit scoring with performance, fairness, or explainability.
  - Used a customized 3Rs&Q (Relevance, Rigor, Reproducibility, Quality) framework for quality assessment.
  - Structured data extraction using a PICOC framework to guide research questions on trade-offs, bias mitigation, and regulation.
  - Synthesized findings narratively, mapping studies to intersections of performance, explainability, fairness, regulation, and human-in-the-loop.
findings:
  - num: 55.81% of selected studies were published in domain-specific venues not belonging to a major digital library.
  - num: 48.8% of included studies were published in 2024, indicating recent research interest.
  - Explainability showed the strongest expansion between 2023 and 2024, becoming the dominant research pillar.
  - num: 21 papers explicitly discussed the association between fairness and protected attributes.
  - num: Only 10 out of 43 papers (23.25%) explicitly measured or proposed novel fairness mitigation strategies.
  - The trade-off between explainability and performance is largely assumed; limited empirical quantification shows marginal differences between interpretable and black-box models.
  - num: Performance gaps between interpretable and black-box models are often marginal, e.g., less than a 4% AUC difference in many reported cases.
  - Fairness is treated as a multi-objective optimization problem with tunable trade-offs; aggressive enforcement degrades performance.
  - Regulatory frameworks (e.g., EU AI Act, ECOA) increasingly mandate explainability and human oversight, but this is not fully integrated into unified pipelines.
  - Human-in-the-loop (HITL) oversight remains under-specified in practical implementation terms.
key_figures_tables:
  - Figure 4: Topic coverage by year → Explainability and fairness research surged from 2023 onward.
  - Table 5: Pairwise intersections grouped by base dimension → Fairness and protected attributes have the highest intersection (21 papers).
  - Table 6: Comparison of interpretable vs. black-box model performance → Performance differences are often marginal and dataset-dependent.
  - Table A10-A13: Summary of fairness mitigation strategies → No universally dominant strategy; effectiveness depends on deployment stage and regulatory context.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: XAI
    definition: Explainable Artificial Intelligence, techniques to make AI model outputs understandable to humans.
  - term: HITL
    definition: Human-in-the-loop, a paradigm where human judgment is integrated into AI system decision-making.
  - term: ECOA
    definition: Equal Credit Opportunity Act, a US law prohibiting discrimination in credit transactions.
  - term: GDPR
    definition: General Data Protection Regulation, an EU law on data protection and privacy.
  - term: SHAP
    definition: SHapley Additive exPlanations, a game-theoretic approach to explain the output of machine learning models.
  - term: LIME
    definition: Local Interpretable Model-agnostic Explanations, a technique to explain individual predictions of any classifier.
  - term: AUC
    definition: Area Under the ROC Curve, a performance metric for binary classification.
  - term: PRISMA
    definition: Preferred Reporting Items for Systematic Reviews and Meta-Analyses, a guideline for reporting systematic reviews.
critical_citations:
  - "[Kozodoi et al., 2022] — Establishes baseline fairness-performance trade-offs in credit scoring."
  - "[Valdrighi et al., 2025] — Provides a comprehensive review of bias mitigation and transparency tools."
  - "[Dessain et al., 2023] — Quantifies the marginal performance cost of explainability."
  - "[Langenbucher, 2020] — Outlines a legal framework for responsible AI credit scoring."
  - "[Kumar et al., 2022] — Aligns algorithmic fairness research with US fair lending regulation."
relevance:
  topics:
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: "Reviews classification models (LR, XGBoost, DL) and their fairness/explainability trade-offs."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: "Discusses predictive modeling for credit risk, including sequential and temporal data considerations."
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: contextual
      justification: "Provides background on algorithmic decision-making and constraints, but not directly on budget recommendation."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: "Mentions outlier and boundary sample detection in credit scoring models."
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: "Identifies data imbalance and protected attributes as sources of bias, relevant to anomaly detection design."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: "Discusses regulatory frameworks like GDPR and their implications for data privacy and fairness."
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: "Emphasizes explainability and fairness as foundational for user trust and regulatory compliance."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: "Reviews evaluation metrics for fairness (e.g., DI, EO) and performance (AUC, accuracy), crucial for system evaluation."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: "Provides systematic comparison of model performance and fairness metrics, directly applicable to evaluating Odin's algorithmic modules."
  contribution: "This review provides a governance-oriented synthesis of AI-based credit scoring. It justifies Odin's need for a fairness-aware and explainable architecture by demonstrating the limitations of performance-only models. It directly informs the design of Odin's behavioral profiling module (5.C) by highlighting classification trade-offs. It also underpins the importance of evaluation frameworks (12.A, 12.B) that jointly assess performance, fairness, and explainability. Finally, it provides a clear rationale for incorporating regulatory and privacy considerations (10.A, 10.B) into Odin's design."
  directly_justifies:
    - "Fairness and explainability must be integrated as joint objectives, not post-hoc additions, in AI-based financial systems."
    - "The performance gap between interpretable and black-box models is often marginal, making interpretable models a viable choice for regulated applications."
    - "Regulatory frameworks like the EU AI Act and ECOA mandate transparency, necessitating explainable AI for compliance."
    - "Human-in-the-loop oversight is essential for certifying fairness and mitigating residual bias in algorithmic decisions."
    - "There is no universally dominant fairness mitigation strategy; selection depends on context, regulation, and risk tolerance."
  limits:
    - "The review is a synthesis of existing literature and does not propose a deployable system."
    - "The focus is on credit scoring, which may not fully translate to PFMS domains like spending behavior prediction or budget recommendation."
    - "Specific algorithms for PFMS (e.g., for spending forecasting) are not directly evaluated."
    - "The review's findings are based on studies from a specific period (2020-2025) and may not capture all future developments."
  mapping_rationale: "All 12 functional domains and their associated canonical topic codes were systematically scanned. High relevance was assigned to 5.C (Classification Approaches) due to the review's focus on model selection and trade-offs; 10.A and 10.B (Data Privacy & User Trust) for its strong regulatory and governance discussion; and 12.A/12.B (Evaluation Frameworks) for its comprehensive review of performance and fairness metrics. Medium relevance was given to 6.B (Forecasting Algorithms) and 8.B (Anomaly Detection Algorithms) as the paper discusses predictive modeling and bias sources relevant to these modules. Contextual relevance was assigned to 7.B (Budget Recommendation) as the paper provides background on optimization but not direct methods. Domains like 2.A (Cultural Practices) and 9.A (Mobile-First Design) were rejected as they were not addressed. The primary contribution is its intersection-oriented synthesis, informing Odin's need for a balanced, explainable, and fair system, directly supporting evaluation and trust modules."
limitations:
  - "The review focuses on credit scoring, a specific financial domain, limiting generalizability to other PFMS functions."
  - "The study does not propose a novel algorithm or system, only synthesizes existing evidence."
  - "Human-in-the-loop oversight is discussed conceptually but lacks practical implementation details."
  - "The analysis is based on studies published up to 2025, and emerging trends may not be fully captured. [unacknowledged]"
remember_this:
  - "Performance gains from black-box models over interpretable models are often marginal."
  - "Explainability has become the dominant research pillar in AI credit scoring since 2023."
  - "Fairness is a multi-objective optimization problem, not a one-time correction."
  - "Regulatory frameworks are driving the need for explainable and fair AI systems."
  - "There is no single best fairness strategy; context and risk tolerance determine the choice."
```