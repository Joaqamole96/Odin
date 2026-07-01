```yaml
paper_id: b8f9a7d3-5c4e-4f2a-9b1c-7d8e9f0a1b2c
designation: international-algorithm-specific
title: Unveiling the Financial Wellbeing Ecosystem: A Data-Driven Framework of Six Behavioral Profiles
authors: Percca, D. F. M.
year: 2026
venue: Unknown
odin_topics:
  - 1.A
  - 1.C
  - 5.A
  - 5.C
  - 7.A
  - 7.B
  - 12.A
  - 12.B
  - 13.A
tldr: A Random Forest classifier identifies six distinct financial wellbeing profiles, revealing subjective perception as the dominant predictor and differentiating structurally vulnerable segments.
problem_and_motivation: Traditional financial wellbeing evaluations rely on unidimensional, linear indices that overlook the complex interplay between short-term preparedness and long-term security. This simplification obscures the inherent heterogeneity of financial profiles, risking misguided conclusions and ineffective interventions. A holistic, intertemporal framework is needed to capture this complexity and inform tailored strategies.
approach:
  - Data from the 2021 National Financial Capability Study (NFCS) with 11,857 observations after excluding retired individuals and incomplete responses.
  - Theory-driven feature engineering binarised eight items to construct short-term and long-term financial wellbeing indices.
  - A 5x5 cross-tabulation of the indices produced a dependent variable with twenty-five cells, later synthesised into six distinct clusters.
  - Random Forest classification was implemented with 100 trees and hyperparameter tuning to validate the framework and analyse determinants.
  - Performance was evaluated using accuracy, precision, recall, and feature importance metrics, with SMOTE applied to address class imbalance.
findings:
  - num: Model 2 achieved 0.4557 accuracy, improving over the baseline model's 0.3689 through the inclusion of demographic controls.
  - The Subjective Index consistently emerged as the paramount classifier, outweighing both the Objective Index and Financial Literacy Index in predictive importance.
  - Six distinct financial profiles were identified: The Established, The Resilient, The Short-Sighted, The Illiquid Planners, The Precarious, and The Distressed.
  - The Short-Sighted (C3) are constrained by human capital deficits, while The Illiquid Planners (C4) are destabilised by exogenous income shocks despite planning capabilities.
  - A gender gap was evident, with females comprising 69.4% of The Distressed and males 57.8% of The Established.
  - Education and income strongly differentiated clusters, with 72.5% of those earning above $300,000 in The Established versus 66.1% of those earning below $50,000 in The Distressed.
  - Only 12% of The Established reported income disruption, compared with an average of 48.6% among vulnerable clusters.
  - Advanced financial literacy acts as a gatekeeper to the highest wellbeing tiers, with The Established showing a significant leap in their Literacy Index.
  - Misclassification patterns revealed persistent overlap between intermediate clusters (C3, C4, C5), indicating the complexity of financial wellbeing modelling.
key_figures_tables:
  - Figure 1: Intertemporal framework matrix with six profiles → Maps short-term/long-term intersection into distinct financial segments.
  - Figure 2: Normalised determinant scores across clusters → Shows progressive gradient and heterogeneity in core determinants.
  - Table 6: Random Forest performance metrics → Model 2 improves accuracy and recall for most clusters.
  - Table 7: Feature importance ranking → Subjective Index ranks highest in both models.
  - Table 8: Confusion matrix → Highlights persistent misclassification between adjacent clusters.
  - Table 9: Pairwise discriminant analysis → Reveals shifting determinants for different cluster boundaries.
key_equations:
  - equation: Y_i = f(X_{1,i} + X_{2,i} + X_{3,i}) + \epsilon_i
    explanation: Baseline Random Forest model without demographic controls.
  - equation: Y_i = f(X_{1,i} + X_{2,i} + X_{3,i} + Z_i) + \epsilon_i
    explanation: Full model including sociodemographic control variables.
definitions:
  - term: Random Forest
    definition: Ensemble method aggregating multiple decision trees for classification.
  - term: Subjective Dominance Effect
    definition: Individual self-perception outweighing objective metrics in predicting wellbeing.
  - term: Intertemporal Framework
    definition: Measurement combining short-term preparedness and long-term security.
  - term: NFCS
    definition: National Financial Capability Study, a US dataset on financial behaviours.
  - term: SMOTE
    definition: Synthetic Minority Over-sampling Technique for addressing class imbalance.
critical_citations:
  - "[Wagner & Walstad, 2019] — Foundational framework for index construction."
  - "[Lusardi & Streeter, 2023] — Establishes financial literacy as a core determinant."
  - "[Sticha, Lusardi, & Sconti, 2023] — Comprehensive financial wellbeing measure."
  - "[Kahneman & Deaton, 2010] — Income threshold for emotional stability plateau."
  - "[Breiman, 2001] — Random Forest methodology foundational reference."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "low"
      justification: "Paper uses US NFCS data, but profiles may generalise to Filipino YPs."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "low"
      justification: "Provides a behavioural profiling framework applicable to YPs."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Directly proposes a six-cluster taxonomy of financial profiles."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Uses Random Forest to classify individuals into wellbeing profiles."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "medium"
      justification: "Findings on short-term/long-term budgeting inform Odin's strategy design."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Cluster-specific interventions guide tailored budget recommendations."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides a robust multi-metric evaluation approach for classification."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Rigorous evaluation of Random Forest via precision, recall, and feature importance."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "medium"
      justification: "Addresses long-term security and savings planning across clusters."
  contribution: "This paper provides a validated intertemporal framework and six-cluster taxonomy that can be directly adapted for Odin's user profiling module. The 'subjective dominance effect' justifies the inclusion of user self-assessment in Odin's behavioural classification. The distinction between The Short-Sighted and The Illiquid Planners offers a template for Odin's infeasibility handling, where users with different root causes require different budget reduction strategies. The feature importance hierarchy (subjective > objective > literacy) guides Odin's feature engineering for its recommendation engine. The paper's evaluation methodology, including precision/recall for imbalanced classes, informs Odin's system evaluation approach for its algorithmic modules."
  directly_justifies:
    - "Subjective perception outweighs objective metrics in predicting financial wellbeing profiles."
    - "Six distinct financial profiles exist, ranging from 'The Established' to 'The Distressed'."
    - "The Short-Sighted and Illiquid Planners have structurally different vulnerability drivers."
    - "Advanced financial literacy is a gatekeeper to top-tier financial wellbeing."
    - "A 0.4557 accuracy is achievable when modelling financial profiles with demographic controls."
  limits:
    - "US-centric data limits generalisability to Filipino young professionals."
    - "Cross-sectional design prevents analysis of profile dynamics over time."
    - "Survivorship bias may result from excluding incomplete survey responses. [unacknowledged]"
    - "Preprint not peer-reviewed, requiring validation of findings."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The domains of Behavioral Profiling & Classification (5.A, 5.C), Budget Recommendation (7.A, 7.B), System Evaluation (12.A, 12.B), and Savings & Debt Management (13.A) were flagged as relevant. Topic 1.A and 1.C were assigned low relevance due to the US sample, but acknowledged for potential generalisability to Filipino YPs. Topic 5.A and 5.C received high relevance as the paper directly proposes and validates a six-profile taxonomy using Random Forest classification. Topics 7.A and 7.B were medium relevance because the cluster-specific interventions inform budget recommendation strategies. Topic 12.A and 12.B were medium and high respectively, as the paper's evaluation methodology is directly applicable. Topic 13.A was medium for its insights on long-term planning. Borderline cases included Topic 2.A (Culturally Specific Practices) and 2.D (Filipino Spending Cycles), which were rejected as the paper does not address Filipino culture. Topic 6.A (Predictive Modeling) was considered low and rejected because forecasting is not the primary focus. Overall, the paper provides strong empirical support for Odin's behavioural profiling and algorithmic evaluation modules, with moderate relevance to budgeting and savings functionalities."
limitations:
  - "US-centric data limits generalisability to Filipino young professionals."
  - "Cross-sectional design prevents analysis of profile dynamics over time."
  - "Survivorship bias may result from excluding incomplete survey responses. [unacknowledged]"
  - "Preprint not peer-reviewed, requiring validation of findings."
remember_this:
  - "Subjective perception dominates objective metrics in predicting financial wellbeing."
  - "Six distinct financial profiles exist, from established to distressed."
  - "The Short-Sighted need literacy interventions; Illiquid Planners need safety nets."
  - "Random Forest achieved 0.4557 accuracy with demographic controls."
  - "Advanced financial literacy is a gatekeeper to top-tier wellbeing."
```