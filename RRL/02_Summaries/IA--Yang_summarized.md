```yaml
paper_id: 10.1007/s44196-024-00719-x
designation: international-algorithm-specific
title: Study of an Adaptive Financial Recommendation Algorithm Using Big Data Analysis and User Interest Pattern with Fuzzy K-Means Algorithm
authors: Yang, J.
year: 2024
venue: International Journal of Computational Intelligence Systems
odin_topics:
  - 3.A
  - 6.B
  - 7.B
  - 8.A
  - 8.B
  - 5.A
  - 5.B
  - 5.C
  - 4.A
  - 4.B
tldr: An adaptive recommendation system using Hadoop, fuzzy K-means clustering, and neural collaborative filtering improves financial product suggestions for users.
problem_and_motivation: Conventional financial services struggle with accessibility, personalization, and incomplete user interest data. This leads to suboptimal recommendations that fail to capture individual preferences and adapt to changing market conditions. A scalable, adaptive solution is needed to address these gaps.
approach:
  - The algorithm is implemented on a Hadoop platform using MapReduce for scalable big data processing.
  - Fuzzy K-means clustering handles uncertainty in financial data by grouping users with similar investment patterns.
  - An adaptive user profile is built from real-time data to capture evolving preferences.
  - Neural collaborative filtering (NCF) with a multi-layer perceptron learns user-item interactions for personalized recommendations.
  - The system uses binary cross-entropy loss for implicit feedback and is evaluated against ANFIS, PRS-MPT, IFCM, and K-L-KM.
findings:
  - num: The proposed FNFinRec algorithm achieved a maximum average silhouette score of 0.690, indicating well-separated user clusters.
  - num: FNFinRec demonstrated superior recommendation accuracy with lower MSE and higher Precision@k and Recall@k compared to existing algorithms.
  - The algorithm effectively segments users based on financial preferences, enabling personalized product recommendations.
  - The FNFinRec framework ensures competitive processing times, crucial for real-time financial decisions.
  - The system adapts to changing user interests and market conditions through continuous learning from new data.
key_figures_tables:
  - Figure 1: Overall working flow of FNFinRec → Integrates data intake, preprocessing, clustering, and NCF for recommendations.
  - Figure 4: Clustering quality using silhouette coefficient → Cluster 2 has the highest average score of 0.690, showing distinct user groups.
  - Figure 5: Davies-Bouldin Index for different clusters → DBI decreases as cluster count grows, improving cluster separation.
  - Figure 6: Recommendation accuracy using mean average precision → FNFinRec has lower MSE than other models, showing higher prediction accuracy.
  - Figure 7: Recommendation accuracy using Precision@k → FNFinRec achieves higher precision across k values, indicating more relevant top recommendations.
  - Figure 8: Recommendation accuracy using Recall@k → FNFinRec consistently obtains better recall, capturing more relevant financial items.
  - Figure 9: Processing time analysis → FNFinRec is more computationally efficient than ANFIS, PRS-MPT, and K-L-KM.
key_equations:
  - equation: "J_m = \\sum_{k=1}^{K} \\sum_{i=1}^{n} u_{rik}^m \\|x_k - c_k\\|^2"
    explanation: Fuzzy K-means objective function minimizing within-cluster variance.
  - equation: "u_{rij} = \\frac{1}{\\sum_{k=1}^{K} \\left( \\frac{\\|x_i - c_j\\|}{\\|x_i - c_k\\|} \\right)^{\\frac{2}{m-1}}}"
    explanation: Membership value of user i to cluster j.
  - equation: "c_j = \\frac{\\sum_{i=1}^{n} u_{rij}^m x_i}{\\sum_{i=1}^{n} u_{rij}^m}"
    explanation: Updating cluster centroids based on fuzzy memberships.
  - equation: "DBI = \\frac{1}{K} \\sum_{i=1}^{K} \\max_{j \\neq i} \\left( \\frac{S_i + S_j}{d(cent_i, cent_j)} \\right)"
    explanation: Davies-Bouldin Index for measuring cluster quality.
  - equation: "L = -\\sum_{(u_r,i) \\in R} \\left[ r_{u_r i} \\log \\hat{r}_{u_r i} + (1 - r_{u_r i}) \\log(1 - \\hat{r}_{u_r i}) \\right]"
    explanation: Binary cross-entropy loss for training the NCF model.
definitions:
  - term: FNFinRec
    definition: Fuzzy Neural Financial Recommendation Algorithm
  - term: NCF
    definition: Neural Collaborative Filtering
  - term: DBI
    definition: Davies-Bouldin Index
  - term: MSE
    definition: Mean Square Error
  - term: ANFIS
    definition: Adaptive Neuro-Fuzzy Inference System
critical_citations:
  - "[Luo, 2020] — Improved clustering for stock investment recommendations."
  - "[Asem et al., 2023] — ANFIS for investment recommendations using demographics."
  - "[Sengupta et al., 2024] — Portfolio recommender using MPT and greedy algorithms."
  - "[Dandugala and Vani, 2024] — Big data clustering with fuzzy C-means and BiLSTM."
  - "[Chiou-Wei and Lee, 2024] — K-L-KM for fund recommendations in Asia."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: Provides general context on categorizing user financial data but does not focus on expense taxonomy design.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews several financial recommendation systems (ANFIS, PRS-MPT, IFCM, K-L-KM) that are part of the existing landscape.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Explicitly identifies limitations of prior systems like scalability, lack of real-time adaptability, and handling of data uncertainty.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: The system uses fuzzy K-means to cluster users based on financial behavior patterns, creating behavioral profiles.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: contextual
      justification: The adaptive nature of the system addresses changing user patterns, but the cold-start problem is not directly discussed.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Fuzzy K-means is a classification approach used to group users into financial behavioral profiles.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: Focuses on investment recommendations rather than forecasting sequential spending data.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Recommends financial products, not budget allocations, so relevance to budget recommendation is low.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Does not address anomaly detection; focuses on recommendation accuracy.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: No mention of anomaly detection algorithms.
    - code: 9.A
      name: Mobile‑First Design Principles and Rationale
      relevance: low
      justification: Not discussed in the paper.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: Not discussed in the paper.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Not discussed in the paper.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: Not discussed in the paper.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: Not discussed in the paper.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: low
      justification: Not discussed in the paper.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses MSE, Precision@k, Recall@k, and processing time for system evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Evaluates clustering quality and recommendation accuracy of the algorithmic modules using standard metrics.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: low
      justification: Not a budget recommendation system.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: Not discussed in the paper.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: low
      justification: Not discussed in the paper.
    - code: 13.C
      name: End‑of‑Period Surplus as a Savings Input
      relevance: low
      justification: Not discussed in the paper.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: low
      justification: The paper does not address culturally specific financial practices of Filipinos.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: low
      justification: Not discussed in the paper.
    - code: 2.C
      name: User-Declared Financial Preferences
      relevance: medium
      justification: The system uses user interaction data and investment preferences to tailor recommendations.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Not discussed in the paper.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: low
      justification: Not discussed in the paper.
    - code: 3.C
      name: User-Defined Allocation Constraints
      relevance: low
      justification: Not discussed in the paper.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: low
      justification: The NCF model is predictive but focuses on recommendations, not forecasting.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: low
      justification: Not discussed in the paper.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: low
      justification: Not discussed in the paper.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: low
      justification: Not discussed in the paper.
    - code: 8.C
      name: Cold‑Start Baseline Strategies for Anomaly Detection
      relevance: low
      justification: Not discussed in the paper.
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: low
      justification: The study does not specifically focus on Filipino young professionals.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: low
      justification: Not discussed in the paper.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: low
      justification: Not discussed in the paper.
  contribution: The paper's hybrid architecture integrating fuzzy clustering and neural collaborative filtering provides a robust framework for personalization in financial systems. The FNFinRec algorithm's focus on scalability via Hadoop MapReduce directly informs Odin's backend processing requirements. Its use of clustering to build user profiles and adapt to changing patterns offers a methodological reference for Odin's behavioral profiling module.
  directly_justifies:
    - The FNFinRec system effectively segments users into distinct financial behavior clusters using fuzzy K-means.
    - The system demonstrates superior recommendation accuracy compared to existing methods like ANFIS and PRS-MPT.
    - Big data processing with Hadoop enables scalable and real-time adaptation to changing user financial patterns.
    - Neural collaborative filtering enhances the personalization of financial recommendations based on user-item interactions.
    - The paper acknowledges the limitations of existing systems in handling data uncertainty and user interest evolution.
  limits:
    - The study does not explicitly address the cold-start problem or new user onboarding. [unacknowledged]
    - The paper focuses on investment recommendations, not budget management or expense categorization. [unacknowledged]
    - The research does not consider Filipino cultural or financial practices. [unacknowledged]
    - No discussion of data privacy or user trust in the recommendation system. [unacknowledged]
    - The system's performance on diverse, non-investment financial data is not evaluated. [unacknowledged]
  mapping_rationale: During the systematic scan across all 12 functional domains, this paper was flagged as relevant primarily to the Behavioral Profiling & Classification and Existing Systems & Gaps domains. The topics 5.A, 5.B, and 5.C (Financial Behavioral Profiles and Classification) were assigned 'high' relevance due to the paper's explicit use of fuzzy clustering for user segmentation. For the Existing Systems & Gaps domain, topic 4.B received 'high' relevance as the paper critiques limitations of conventional financial systems, and topic 4.A received 'medium' relevance as it reviews several existing systems. The System Evaluation domain (12.A, 12.B) was assigned 'medium' and 'high' relevance, respectively, due to the use of standard evaluation metrics for algorithmic modules. Topic 2.C (User-Declared Preferences) was assigned 'medium' relevance as the system relies on user interaction data. All other topics related to Filipino context, expense categorization, forecasting, budget recommendation, anomaly detection, mobile design, privacy, engagement, and savings/debt were considered and rejected due to a lack of direct coverage or actionable insights for Odin's specific design. The paper's primary contribution is algorithmic and deals with product recommendation, making its direct relevance to many of Odin's core PFMS functions limited, but it offers valuable lessons on user clustering and adaptive personalization.
limitations:
  - The model's reliance on past user interaction data may not accurately predict future market trends or investor behavior. [unacknowledged]
  - Potential scaling issues with bigger datasets and requirement for additional processing to account for ever-changing market conditions are noted.
  - The study may be constrained by the computing capabilities needed for large-scale processing of data.
  - The assessment datasets may not apply to other big data environments.
  - The model’s dependence on precise initial gathering of data and potential scaling concerns with larger, more diversified datasets are limitations.
  - Possible sensitivity to clustering variables and limitations on dataset size are identified.
remember_this:
  - The FNFinRec algorithm achieved a silhouette score of 0.690, showing clear user segmentation.
  - The system effectively combines fuzzy K-means clustering with neural collaborative filtering for adaptive recommendations.
  - Its Hadoop-based implementation enables scalable processing of large financial datasets.
  - The algorithm adapts in real-time to changing user interests and market conditions.
  - FNFinRec showed superior precision and recall compared to existing recommendation algorithms.
```