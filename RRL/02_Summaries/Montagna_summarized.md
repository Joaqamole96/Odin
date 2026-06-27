```yaml
paper_id: 70d5269c-1cbd-5b71-afa6-86550a29e2e4
designation: international-algorithm-specific
title: Integration of Explainability in Recommender Systems to Enhance Enterprise Value Strategies
authors: Montagna, A.
year: 2026
venue: University of Padova
odin_topics:
  - 4.A
  - 4.B
  - 7.A
  - 7.B
  - 7.D
  - 9.A
  - 9.B
  - 10.A
  - 10.B
tldr: A comprehensive thesis that surveys Value-Aware Recommender Systems, proposes an explainable value-aware matrix factorization model, and critiques the evaluation of explanations in graph-based recommenders for enterprise contexts.
problem_and_motivation: Recommender systems are widely used but often lack transparency and fail to align with business value objectives. Value-aware systems exist but have not been systematically surveyed, and a key gap remains in balancing the generation of business value with the need for explainable, trustworthy recommendations. This research addresses this gap by creating a bridge between these perspectives through novel models and evaluation frameworks.
approach:
  - A systematic literature review following PRISMA guidelines was conducted to survey and classify Value-Aware Recommender Systems (VARSs), analyzing 109 studies.
  - A novel model, Explainable Value-aware Matrix Factorization (XVMF), is proposed to balance explainability and business value by integrating both terms into a unified objective function.
  - The model is evaluated on Yelp and Amazon datasets using NDCG, E-NDCG, and a novel NDCV metric to assess accuracy, explainability, and business value trade-offs.
  - A critical analysis of Graph-Based Explainable Recommender Systems (GxRSs) is performed, highlighting the lack of quantitative evaluation methods for explanation quality.
findings:
  - num: The systematic review identified 109 relevant studies on VARSs, which are classified into in-processing and post-processing techniques.
  - The proposed XVMF model successfully balances explainability and business value, achieving performance that exceeds baseline MF and EMF models on the Yelp dataset.
  - num: For the Yelp dataset, the XVMF model achieved an NDCV of 0.5042% and an E-NDCG of 1.9954%, outperforming the baseline models.
  - num: On the Amazon dataset, the XVMF-e model achieved an E-NDCG of 0.1723%, a significant improvement over EMF, while the XVMF-v model achieved an NDCV of 0.1154%.
  - A key finding is that the optimal balance between explainability and value is achieved at low regularization parameter values, after which performance degrades quickly.
  - The analysis of GxRSs reveals that most papers rely on qualitative case-based analyses, with only a few employing quantitative metrics for explanation evaluation.
  - The thesis proposes that future work on GxRSs should adopt standardized quantitative metrics to ensure comparability and rigorous evaluation.
key_figures_tables:
  - "Figure 2.1: PRISMA flow diagram summarizing the systematic literature review process → 109 studies were included in the final review."
  - "Figure 2.2: Taxonomy of value-aware recommender algorithms → Divides VARSs into in-processing and post-processing methods."
  - "Table 2.1: Application domains of value-aware recommender systems → Shows product, advertising, news, and media as key domains."
  - "Figure 3.1-3.4: Performance analysis for Yelp and Amazon datasets → Show the trade-off and optimal balance between explainability and value regularization."
  - "Table 3.5 and 3.6: Evaluation metrics for MF, EMF, and XVMF → XVMF outperforms baselines, particularly on the Yelp dataset."
key_equations:
  - equation: |
      G_{expl} = \sum_{u,i \in R} (r_{ui} - a_u b_i^T)^2 + \frac{\beta}{2} (\| a_u \|^2 + \| b_i \|^2) + \lambda \| a_u - b_i \|^2 E_{ui}
    explanation: Objective function for explainable matrix factorization, incorporating an explainability regularization term.
  - equation: |
      L = \sum_{(u,i) \in S} (r_{u,i} - p_u \cdot q_i^T)^2 + \frac{\beta}{2} (\| p_u \|^2 + \| q_i \|^2) + \| p_u - q_i \|^2 (\lambda W_{u,i} + \delta v_i)
    explanation: Objective function for the proposed XVMF model, balancing explainability and business value.
  - equation: |
      \text{NDCV} = \sum_{i=1}^{k} \frac{2^{rel_i} - 1}{\log_2 (i+1)}
    explanation: Novel metric to evaluate the business value of a recommendation list, based on the gain from the item's value.
definitions:
  - term: VARS
    definition: Value-Aware Recommender System, designed to directly maximize the economic value of recommendations.
  - term: xRS
    definition: Explainable Recommender System, which provides reasons or evidence for its recommendations.
  - term: XVMF
    definition: Explainable Value-aware Matrix Factorization, a novel model proposed in this thesis to balance explainability and business value.
  - term: E-NDCG
    definition: Explainable Normalized Discounted Cumulative Gain, a metric for evaluating the explainability quality of a ranked recommendation list.
  - term: NDCV
    definition: Normalized Discounted Cumulative Value, a novel metric proposed to evaluate the business value generated by a recommendation list.
  - term: GxRS
    definition: Graph-Based Explainable Recommender System, a system that uses graph structures to generate and explain recommendations.
  - term: MEP
    definition: Mean Explainability Precision, a quantitative metric to evaluate the explainability of recommendations.
critical_citations:
  - "[Page et al., 2021] — PRISMA guidelines for systematic reviews."
  - "[Ricci et al., 2022] — Overview of recommender systems techniques."
  - "[Abdollahi and Nasraoui, 2016] — Basis for explainable matrix factorization (EMF)."
  - "[Coba et al., 2019] — Basis for E-NDCG and NEMF model."
  - "[De Biasio et al., 2023] — The first systematic review of VARSs."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Surveys existing VARSs, providing a landscape of systems optimizing business value.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies the gap between business value optimization and explainability in current systems.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: Discusses business value optimization, a key driver for budget recommendation strategies.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: The thesis focuses on recommender systems in general, but the principles are transferable to budget recommendations.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: low
      justification: The XVMF model involves trade-offs between objectives, related to handling competing priorities.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Emphasizes the importance of human-centered design and trust in user adoption of AI systems.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: Discusses interface design for explanations, which is relevant to UX in general.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Focuses on trustworthy AI principles, including privacy and security.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: A central theme of the thesis is that explainability builds user trust and system adoption.
  contribution: "This thesis contributes to Odin's design by providing a systematic survey of value-aware systems, which can inform the development of Odin's budget recommendation and anomaly detection modules. The proposed XVMF model offers a concrete, data-driven approach for balancing user preference accuracy with business value, directly applicable to Odin's core functionality of generating personalized financial plans. Furthermore, the critical analysis of explanation evaluation in graph-based systems provides a methodological blueprint for ensuring that Odin's recommendations are not only accurate but also transparent and trustworthy. Finally, the emphasis on human-centered evaluation and user interfaces is crucial for designing Odin's mobile-first application to foster user engagement and trust."
  directly_justifies:
    - "The proposed XVMF model can be adapted to balance recommendation accuracy with Odin's business goals of user retention and savings growth."
    - "Systematic review of VARSs identifies key algorithms and datasets relevant for building Odin's value-optimization modules."
    - "Analysis of GxRSs highlights the need for quantitative explainability metrics, guiding Odin's evaluation framework."
  limits:
    - "The experimental validation of XVMF is limited to Yelp and Amazon datasets, which may not fully represent the financial behavior of Filipino young professionals."
    - "The qualitative limitations of existing explainability evaluations in GxRSs are noted, but a new comprehensive metric is not proposed."
    - "The thesis focuses on algorithm performance and does not include an end-to-end user study in a real-world business setting."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The 'Existing Systems & Gaps' domain was flagged as highly relevant (topics 4.A, 4.B), as the thesis directly surveys VARSs and identifies the specific gap in explainable value-aware systems. The 'Budget Recommendation' domain (topics 7.A, 7.B, 7.D) was considered relevant due to the focus on optimizing economic value and balancing competing objectives, though the application is not specific to budgeting. The 'Mobile-First Design' and 'Data Privacy & User Trust' domains (topics 9.A, 9.B, 10.A, 10.B) are medium to low relevance, as the thesis discusses trust and interface design in the context of explainability, which is a key principle for Odin. Domains like 'Filipino Cultural Context' (2.A-D), 'Expense Categorization' (3.A-C), 'Behavioral Profiling' (5.A-C), 'Spending Forecasting' (6.A-B), 'Anomaly Detection' (8.A-C), 'Engagement & Retention' (11.A-B), 'System Evaluation' (12.A-C), and 'Savings & Debt Management' (13.A-C) were considered and rejected as the thesis does not directly address these specific areas, focusing instead on recommender system algorithms and their evaluation in a general enterprise context. The overall relevance to Odin is high, as it provides both a foundational survey of value-aware systems and a novel model for balancing key performance objectives."
limitations:
  - "The systematic review is based on articles from specific databases and excludes non-English and unpublished works. [unacknowledged]"
  - "The datasets used for XVMF (Yelp, Amazon) do not contain Filipino user data, limiting direct applicability to the target demographic. [unacknowledged]"
  - "The evaluation of XVMF is offline and does not include online A/B testing or user studies to validate real-world performance. [unacknowledged]"
  - "The thesis criticizes the lack of quantitative evaluation in GxRSs but does not itself propose a new, comprehensive metric to address this gap."
remember_this:
  - "Value-aware recommender systems are a distinct class that directly optimize economic value."
  - "The XVMF model successfully balances explainability and business value on benchmark datasets."
  - "Offline evaluation metrics for business value and explainability are critical for model selection."
  - "Current graph-based explainable recommenders lack rigorous quantitative evaluation of their explanations."
  - "Balancing user trust and system adoption is a key challenge for enterprise recommender systems."
```