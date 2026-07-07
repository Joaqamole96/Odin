```yaml
paper_id: ce4d2a9c-aec4-57f0-a6e2-9a09e3b56c2e # No DOI available
designation: international
title: AI-Driven Credit Risk Assessment in Fintech Lending: Implications for Financial Inclusion, Systemic Risk, and Regulatory Governance
authors: Ahmed, S. I.
year: 2026
venue: American International Journal of Business Management
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 4.B
  - 8.A
  - 10.A
  - 10.B
tldr: A systematic review of AI credit risk models shows they improve predictive power but introduce governance challenges in fairness, systemic stability, and regulation, addressed via a proposed five-stage governance framework.
problem_and_motivation: Fintech lending uses AI for credit assessment, offering inclusion benefits but raising unaddressed governance issues like algorithmic bias and systemic risk. Existing regulatory frameworks are fragmented and lag behind technological adoption, especially in emerging markets. A unified governance approach is needed to balance innovation with stability and equity.
approach:
  - Systematic literature review of 30 peer-reviewed articles and regulatory reports from 2012-2025.
  - PRISMA-inspired protocol used for screening and selecting the final corpus of documents.
  - Comparative model analysis conducted on performance metrics like AUC-ROC, Gini coefficient, and KS statistic.
  - Iterative framework construction method employed to develop the Integrated AI Credit Risk Framework (IACRF).
  - The IACRF operationalizes the SAFE AI principles across five stages of a fintech credit system lifecycle.
findings:
  - num: Gradient boosting models achieve AUC-ROC values of 0.83-0.91, a 7-19 percentage point improvement over logistic regression baselines.
  - num: Hybrid XAI models with SHAP achieve AUC-ROC of 0.84-0.92 while improving interpretability to meet regulatory criteria.
  - num: AI models on alternative data increase approval rates for thin-file borrowers by 20-40 percentage points in new markets.
  - Algorithmic bias arises from historical data and can be identified via XAI but requires institutional accountability for remediation.
  - Systemic risk propagates through model herding, procyclicality, and platform contagion, unaddressed by current frameworks.
  - The EU AI Act represents the most advanced regulatory model but lacks systemic risk monitoring tools.
key_figures_tables:
  - Table 1: Comparative performance of AI/ML models → Ensemble XAI models offer the best balance of performance and regulatory suitability.
  - Table 2: Financial inclusion metrics by region → Inclusion benefits are highest in emerging markets but come with high digital exclusion risk.
  - Table 3: Comparative AI credit governance frameworks → Significant governance gaps exist in emerging markets.
  - Figure 1: Conceptual architecture of IACRF → The five-stage framework integrates accuracy, fairness, stability, and ethics.
  - Figure 3: Systemic risk propagation pathways → Model herding, procyclicality, and platform contagion create systemic vulnerability.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: IACRF
    definition: Integrated AI Credit Risk Framework, a five-stage governance model for fintech lending.
  - term: SAFE AI
    definition: Principles for Statistical accuracy, Algorithmic fairness, Financial stability, and Ethical governance in AI.
  - term: XAI
    definition: Explainable Artificial Intelligence, techniques like SHAP and LIME for model interpretability.
  - term: AUC-ROC
    definition: Area Under the Receiver Operating Characteristic Curve, a measure of model predictive performance.
critical_citations:
  - "[Fan, 2025] — Reviews AI/ML classification models for credit risk performance."
  - "[Giudici & Raffinetti, 2023] — Proposes the SAFE AI framework for finance."
  - "[Berg et al., 2022] — Reviews market structure and dynamics of FinTech lending."
  - "[Billio et al., 2012] — Introduces econometric measures of systemic risk connectedness."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: Discusses AI models inferring creditworthiness from behavioral data, which is conceptually relevant to profiling user financial behavior.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: Addresses using alternative data for thin-file borrowers, analogous to cold-start profiling but not directly on personal finance management.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Reviews ML models like gradient boosting for classifying credit risk, which are similar to techniques used for behavioral profile classification.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly identifies governance gaps in current fintech lending systems, including fairness, transparency, and systemic risk oversight.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Mentions model monitoring for performance degradation and distributional shifts, which are related to anomaly detection concepts.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Discusses data governance, consent architectures, and privacy in the context of training AI models with alternative data.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Identifies algorithmic opacity and lack of explainability as direct threats to user trust and accountability in credit decisions.
  contribution: The paper's IACRF directly justifies the need for multi-level governance in Odin, covering data handling, algorithmic fairness, and systemic risk monitoring. It provides a rationale for incorporating explainability and bias auditing into Odin's recommendation and anomaly detection modules. The discussion on regulatory compliance informs Odin's design for data privacy and user trust. Its findings on performance-fairness trade-offs influence the approach to behavioral profiling and budget recommendations. The framework's emphasis on impact evaluation supports Odin's need for continuous system evaluation and improvement.
  directly_justifies:
    - "AI credit models offer performance gains but create interpretability challenges for regulatory compliance."
    - "Financial inclusion benefits of AI are constrained by digital exclusion and pricing bias risks."
    - "Systemic risk from AI lending propagates via model herding and procyclicality."
    - "Regulatory frameworks are fragmented, with emerging markets facing the largest governance gaps."
  limits:
    - "Literature-based synthesis limits causal inference and may suffer from publication bias."
    - "IACRF is theoretical and requires empirical validation in real fintech settings."
    - "Rapid regulatory changes may render some jurisdictional analyses outdated quickly."
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The paper was flagged as relevant primarily to the "Existing Systems & Gaps" and "Data Privacy & User Trust" domains due to its thorough analysis of limitations in current fintech lending systems and governance challenges related to fairness and opacity. It also touches on "Behavioral Profiling" (topic 5.A) and "Classification" (topic 5.C) because it reviews ML models used to infer borrower risk from behavioral data, but these are not the core focus. The paper was considered and rejected for domains like "Expense Categorization," "Spending Forecasting," and "Budget Recommendation," as it does not address personal finance management or budget allocation. Similarly, it was deemed non-relevant for "Mobile-First Design," "User Retention," and "Savings & Debt Management" as it focuses on institutional lending, not individual financial health management. Overall, the paper provides strong contextual and supporting evidence for Odin's design concerning system limitations, fairness, and trust but is not directly algorithmic for spending forecasting or recommendation.
limitations:
  - "The study relies on published literature, which may not capture unpublished industry practices and may be subject to publication bias."
  - "The IACRF is a theoretical framework that has not yet been empirically tested in operational fintech environments. [unacknowledged]"
  - "The rapid evolution of AI governance regulations means some specific jurisdictional references may become outdated. [unacknowledged]"
remember_this:
  - "AI credit models improve predictive accuracy but introduce significant governance challenges."
  - "Financial inclusion from AI lending is countered by risks of digital exclusion and over-indebtedness."
  - "Systemic risk arises from model herding, procyclicality, and platform interconnectedness."
  - "Regulatory governance for AI in lending is fragmented, with emerging markets least protected."
  - "The IACRF integrates fairness and systemic stability into a five-stage governance lifecycle."
```