```yaml
paper_id: 10.3389/frai.2026.1726900
designation: international-algorithm-specific
title: Marketing-AutoM3L: domain-aware automated machine learning for financial customer analytics
authors: Tian, Y.; Shao, W.; Deng, Z.
year: 2026
venue: Frontiers in Artificial Intelligence
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 10.A
tldr: An automated ML framework using LLMs for domain-aware pipeline construction in financial customer analytics, improving accuracy by 1.4% to 5.4% over existing AutoML.
problem_and_motivation: Generic AutoML systems lack domain-specific feature engineering capabilities essential for financial customer analytics, requiring manual intervention. Existing approaches force a trade-off between suboptimal generic solutions and resource-intensive manual customization. Business stakeholders with customer expertise cannot directly translate requirements into predictive pipelines, creating a critical gap.
approach:
  - The framework processes raw customer datasets and natural language directives through five stages.
  - Data modality recognition uses LLMs to classify attribute types and semantic meanings.
  - Domain-aware feature engineering automatically computes RFM scores, CLV projections, and engagement metrics.
  - Model architecture selection is guided by data characteristics and business requirements.
  - Multimodal pipeline construction and training configuration optimization complete the automated workflow.
findings:
  - num: Accuracy improvements of 1.4% to 5.4% in ROC-AUC over baseline AutoML methods across five datasets.
  - num: Pipeline development time reduced by 6.7× compared to manual approaches (23.4 min vs 156.9 min).
  - num: Domain-specific feature engineering contributes 3.3% to 3.6% ROC-AUC improvement in ablation studies.
  - The framework achieves optimal performance with moderate parameter counts, reducing unnecessary complexity.
  - RFM (Recency, Frequency, Monetary) features dominate prediction performance across all datasets.
key_figures_tables:
  - Figure 1: Framework architecture showing Intelligent Processing and Knowledge Supplementation modules → LLM-driven pipeline automation for customer analytics.
  - Figure 5: Performance comparison across datasets and methods → Marketing-AutoM3L consistently achieves highest ROC-AUC and F1 scores.
  - Figure 7: Execution time comparison → Marketing-AutoM3L achieves 6.7× speedup over manual pipeline development.
  - Table 2: Main experimental results → Comprehensive performance metrics demonstrate superiority over all baselines.
key_equations:
  - equation: R_i = t_current - max(s_1, s_2, ..., s_n), F_i = n, M_i = \sum_{j=1}^{n} a_j
    explanation: RFM metrics computation for recency, frequency, and monetary value.
  - equation: CLV_{prob,i} = \sum_{t=1}^{T} \frac{AOV_i \times PF_i \times r_i^t}{(1+d)^t}
    explanation: Probabilistic CLV projection incorporating customer retention probability.
  - equation: E_i(t) = \sum_{k=1}^{K} w_k \sum_{\tau=0}^{W} I_{i,k}(t-\tau) \cdot e^{-\lambda \tau}
    explanation: Engagement score aggregating weighted interaction signals over time.
definitions:
  - term: RFM
    definition: Recency-Frequency-Monetary framework for customer segmentation based on transaction behavior.
  - term: CLV
    definition: Customer Lifetime Value projection estimating total future value from a customer.
  - term: AutoML
    definition: Automated Machine Learning for automating pipeline construction without manual coding.
  - term: ROC-AUC
    definition: Area Under the Receiver Operating Characteristic Curve for classification performance.
critical_citations:
  - "[Luo et al., 2024] — First AutoM3L framework using LLMs as controllers."
  - "[Jain et al., 2023] — Comprehensive deep learning for customer churn prediction."
  - "[Qi et al., 2023] — Efficient RFM pattern mining algorithm foundation."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Domain-aware feature engineering automatically generates RFM and engagement metrics.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: Feature filtering and construction components inform category design.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Direct comparison with existing AutoML systems demonstrates limitations.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies lack of domain-specific feature engineering in generic AutoML.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: RFM and engagement scoring quantify behavioral patterns for customer classification.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: medium
      justification: Automated feature engineering reduces manual effort in cold-start scenarios.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Model selection and multimodal fusion for behavior prediction.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: End-to-end pipeline construction for churn prediction and CLV estimation.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Temporal processing and engagement trend features for behavioral forecasting.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Churn prediction shares methodological overlap with anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Declining engagement trends are predictive of anomalies.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Framework processes customer data, but privacy not explicitly addressed.
  contribution: "Marketing-AutoM3L provides an automated feature engineering module for Odin's expense categorization (3.A) by computing RFM and engagement metrics directly from transaction data. The LLM-driven pipeline automation addresses Odin's gap analysis (4.B) by demonstrating how existing AutoML systems lack domain-specific capabilities. The framework's behavioral profiling (5.A) and forecasting (6.A) components offer validated approaches for customer behavior prediction in Odin. The experimental evaluation (12.A) provides benchmarking methodology for assessing Odin's algorithmic modules. The ablation studies quantify the value of domain-aware feature engineering, supporting Odin's design decisions for automated financial analytics."
  directly_justifies:
    - "Domain-specific RFM and CLV feature engineering improves prediction accuracy by 3.3% to 3.6%."
    - "LLM-driven pipeline automation reduces development time by 6.7× compared to manual approaches."
    - "Multimodal data integration provides 1.1% to 3.6% ROC-AUC gains over single-modality baselines."
    - "Natural language directives enable business stakeholders to configure pipelines without ML expertise."
  limits:
    - "Relies on proprietary GPT-4 API, raising reproducibility and cost concerns."
    - "Validation primarily on classification tasks, limited exploration of regression or optimization domains."
    - "Customer data temporal constraints not fully validated across all dataset types."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes identified several areas of relevance. The Expense Categorization domain (3.A, 3.B) is highly relevant because the framework automatically generates domain-specific features including RFM metrics and engagement scores. The Existing Systems domain (4.A, 4.B) is highly relevant as the paper directly compares against generic AutoML systems and identifies their limitations in domain-specific contexts. Behavioral Profiling (5.A, 5.B, 5.C) is highly relevant for RFM-based customer segmentation and engagement scoring. Spending Forecasting (6.A, 6.B) is highly relevant for CLV projection and temporal behavioral prediction. Anomaly Detection (8.A, 8.B) is low relevance as churn prediction shares methodological overlap but is not the primary focus. Data Privacy (10.A) is contextual only as the framework processes data but privacy considerations are not addressed. Mobile-First Design (9.A, 9.B), User Retention (11.A, 11.B), System Evaluation (12.A, 12.B, 12.C), Savings & Debt Management (13.A, 13.B, 13.C), and Filipino Cultural Context (1.A, 1.B, 1.C, 2.A, 2.B, 2.C, 2.D) were considered and rejected due to no direct relevance to the paper's algorithmic contribution or focus on international financial customer analytics. The paper's overall relevance to Odin is moderate-to-high, providing validated automated feature engineering and pipeline construction methodologies for personal finance systems."
limitations:
  - "GPT-4 API dependency creates reproducibility concerns. [unacknowledged]"
  - "High-end GPU infrastructure may not be accessible to all organizations. [unacknowledged]"
  - "Evaluation limited to churn prediction tasks, not validated for budget recommendation or optimization domains."
  - "Natural language directive interpretation quality depends on LLM performance consistency."
  - "Temporal constraints and data leakage prevention not extensively validated."
remember_this:
  - "Domain-aware feature engineering provides 3.3% to 3.6% accuracy gains over generic approaches."
  - "LLM-driven automation reduces pipeline development time by 6.7× compared to manual methods."
  - "RFM and engagement metrics are the most predictive features for customer behavior forecasting."
  - "Natural language interfaces enable non-technical stakeholders to configure predictive pipelines."
  - "Multimodal data integration improves prediction accuracy by 1.1% to 3.6% over single-modality baselines."
```