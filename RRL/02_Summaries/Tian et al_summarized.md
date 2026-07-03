```yaml
paper_id: 10.3389/frai.2026.1726900
designation: international-algorithm-specific
title: Marketing-AutoM3L: domain-aware automated machine learning for financial customer analytics
authors: Tian, Y.; Shao, W.; Deng, Z.
year: 2026
venue: Frontiers in Artificial Intelligence
odin_topics:
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 7.B
  - 7.D
  - 8.A
  - 8.B
  - 12.A
  - 12.B
  - 12.C
tldr: An LLM-driven framework automatically constructs domain-aware ML pipelines for customer analytics, outperforming generic AutoML by 1.4%–5.4% in ROC-AUC while reducing development time 6.7-fold.
problem_and_motivation: Generic AutoML systems lack the capacity to automatically construct domain-specific features (e.g., RFM, CLV, engagement scores) essential for financial customer analytics, forcing organizations to either accept suboptimal performance or dedicate scarce data science expertise to manual pipeline development.
approach:
  - The framework takes raw customer data and natural language directives as input to generate executable training pipelines.
  - An LLM acts as an intelligent controller, orchestrating five stages: modality recognition, domain-aware feature engineering, model selection, multimodal pipeline construction, and training configuration optimization.
  - Domain-specific feature engineering automatically computes RFM scores, CLV projections, and engagement scores with temporal trend derivatives.
  - Model selection is guided by data characteristics, computational constraints, and business requirements expressed in natural language.
  - The system employs a late fusion strategy to integrate predictions from modality-specific models (tabular, text, temporal) into a unified pipeline.
findings:
  - num: Marketing-AutoM3L achieved ROC-AUC improvements of 1.4% to 5.4% over existing automated and manual approaches across five customer analytics datasets.
  - num: The framework reduced pipeline development time from 156.9 minutes (manual) to 23.4 minutes, representing a 6.7-fold speedup.
  - Domain-aware feature engineering alone contributed 3.3%–3.6% ROC-AUC improvement in ablation studies.
  - The framework maintains balanced performance across precision and recall while achieving the highest F1-scores on all datasets.
  - Multimodal integration (tabular+text+temporal) consistently outperforms single-modality approaches by 1.1% to 3.6% ROC-AUC.
key_figures_tables:
  - Figure 1: Overall framework architecture showing Intelligent Processing and Knowledge Supplementation modules → LLM orchestrates five-stage pipeline construction.
  - Table 2: Main experimental results comparing Marketing-AutoM3L against baselines → Framework achieves highest ROC-AUC and F1-scores across all five datasets.
  - Table 3: Performance when baselines receive pre-computed domain features → Marketing-AutoM3L maintains 0.8%–2.1% advantage even when features are provided externally.
  - Table 5: Ablation study results showing individual component contributions → Feature engineering provides largest gain (3.3%–3.6%).
  - Figure 5: Performance comparison across datasets and methods → Consistent superiority across ROC-AUC, F1, precision, and recall.
key_equations:
  - equation: "RFM = (R_i, F_i, M_i) where R_i = t_current - max(s_1,...,s_n), F_i = n, M_i = sum(a_j)"
    explanation: RFM metrics quantify customer recency, frequency, and monetary value.
  - equation: "CLV_hist_i = AOV_i × PF_i × CL_i"
    explanation: Historical averaging method projects customer lifetime value.
  - equation: "CLV_prob_i = sum_{t=1}^{T} (AOV_i × PF_i × r_i^t) / (1+d)^t"
    explanation: Probabilistic model incorporates retention probabilities for CLV projection.
  - equation: "E_i(t) = sum_{k=1}^{K} w_k sum_{\\tau=0}^{W} I_{i,k}(t-\\tau) · e^{-\\lambda \\tau}"
    explanation: Engagement score aggregates weighted, temporally decayed interaction signals.
definitions:
  - term: RFM
    definition: Recency-Frequency-Monetary analysis for customer segmentation based on transactional behavior.
  - term: CLV
    definition: Customer Lifetime Value, the total projected value a customer will generate over their relationship.
  - term: AutoML
    definition: Automated Machine Learning, systems that automate pipeline construction without manual intervention.
  - term: LLM
    definition: Large Language Model, used as an intelligent controller for decision-making across pipeline stages.
  - term: Late Fusion
    definition: Strategy combining predictions from modality-specific models after independent processing.
critical_citations:
  - "[Luo et al., 2024a] — Foundation for LLM-driven multimodal pipeline construction."
  - "[Jain et al., 2023] — Demonstrates BiLSTM-CNN effectiveness for churn prediction."
  - "[Shen et al., 2025e] — AutoML agent framework for histopathology images."
relevance:
  topics:
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: Addresses dynamic customer behavior patterns and evolving engagement trends over time.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Proposes and evaluates classification architectures (RFM, CLV, engagement scoring) for behavioral profiling.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly tackles predictive modeling for customer churn and behavior prediction in financial contexts.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Implements and evaluates temporal forecasting with RFM, CLV, and engagement trend features.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: contextual
      justification: Provides methodological framework for automated recommendation via LLM-driven optimization.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: contextual
      justification: Pipeline construction handles constraints through LLM-driven adaptation to business objectives.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Churn prediction as anomaly detection; framework identifies at-risk customers deviating from behavioral norms.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Evaluates classification algorithms (gradient boosting, neural networks) applicable to anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides comprehensive evaluation across multiple datasets with ROC-AUC, F1, precision, recall metrics.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Ablation studies quantify individual component contributions to overall performance.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Evaluation methodology for automated recommendation systems is generalizable to budget recommendation.
  contribution: The framework directly addresses Odin's need for domain-aware feature engineering in Modules 5 (behavioral profiling) and 6 (forecasting) by automatically computing RFM, CLV, and engagement features. It provides a methodology for Module 7 (budget recommendation) through LLM-driven optimization guided by natural language objectives. The experimental evaluation framework (Module 12) establishes rigorous baselines and ablation methodologies. The natural language interface design (Module 9) enables non-technical stakeholders to configure pipelines, aligning with Odin's mobile-first accessibility goals. The temporal constraint enforcement ensures no data leakage, critical for Module 8's cold-start anomaly detection baselines.
  directly_justifies:
    - "Marketing-AutoM3L's domain-aware feature engineering improves ROC-AUC by 3.3%–3.6% over generic approaches."
    - "The LLM-driven pipeline automation reduces development time by 6.7× compared to manual approaches."
    - "Natural language interfaces enable business stakeholders to specify requirements without ML expertise."
    - "Multimodal integration (tabular+text+temporal) outperforms single-modality approaches by 1.1%–3.6% ROC-AUC."
    - "The framework maintains balanced precision and recall, critical for cost-sensitive retention interventions."
  limits:
    - "Evaluation focuses on customer churn prediction rather than the full spectrum of financial behavior Odin addresses."
    - "CLV projection assumes stable customer behavior patterns, which may not hold for young professionals with dynamic financial situations."
    - "Engagement scoring weights are dataset-specific and may require recalibration for Odin's target demographic."
    - "The GPT-4 dependency introduces reproducibility concerns as model updates could affect framework behavior."
  mapping_rationale: I systematically scanned all 12 functional domains and their associated 28 topic codes against the paper's contributions. The paper is highly relevant to Predictive Modeling (6.A, 6.B) as it directly proposes and evaluates forecasting algorithms for customer behavior. It is directly applicable to Behavioral Profiling (5.B, 5.C) through its RFM, CLV, and engagement scoring methodologies. The evaluation framework (12.A, 12.B) provides rigorous baselines and ablation studies. The paper has medium relevance to Anomaly Detection (8.A, 8.B) as churn prediction is a form of anomaly detection, and the classification algorithms are transferable. It provides contextual relevance to Budget Recommendation (7.B, 7.D) through its LLM-driven optimization and constraint handling, and to Mobile-First Design (9.A, 9.B) through its natural language interface. I rejected the following domains as non-applicable: Filipino Cultural Context (2.A–D) as the paper uses international datasets; Expense Categorization (3.A–C) as it does not address category design; Existing Systems (4.A–B) as the focus is on new methodology rather than landscape analysis; Data Privacy (10.A–B) as it is not addressed; User Retention (11.A–B) except as a prediction target; and Savings/Debt Management (13.A–C) as these are not covered. The overall relevance is high, as the paper provides a directly applicable methodology for automating domain-aware ML pipelines that could be adapted to Odin's architecture.
limitations:
  - "Reliance on proprietary GPT-4 API introduces cost and reproducibility concerns for deployment. [unacknowledged]"
  - "Experiments use international datasets; generalizability to Filipino young professionals is untested. [unacknowledged]"
  - "The framework assumes high-quality, well-structured input data, which may not reflect real-world PFMS data quality. [unacknowledged]"
  - "Evaluation focuses on predictive accuracy rather than the full PFMS workflow including budgeting and savings recommendations. [unacknowledged]"
remember_this:
  - "LLM-driven AutoML reduces pipeline development time from 157 to 23 minutes."
  - "Domain-aware feature engineering improves ROC-AUC by 3.3%–3.6% over generic approaches."
  - "Natural language directives enable non-experts to configure ML pipelines without coding."
  - "Multimodal data integration outperforms single-modality approaches by up to 3.6% ROC-AUC."
  - "RFM, CLV, and engagement scores are the most predictive features across all datasets."
```