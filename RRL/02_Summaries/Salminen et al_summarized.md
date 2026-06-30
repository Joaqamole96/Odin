```yaml
paper_id: 10.1057/s41270-023-00235-5
designation: international-algorithm-specific
title: How can algorithms help in segmenting users and customers? A systematic review and research agenda for algorithmic customer segmentation
authors: Salminen, J.; Mustak, M.; Sufyan, M.; Jansen, B. J.
year: 2023
venue: Journal of Marketing Analytics
odin_topics:
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 12.A
  - 12.B
  - 12.C
tldr: A systematic review of 172 articles identifies 46 algorithms and 14 evaluation metrics for customer segmentation, with K-means and separation-focused metrics being most prevalent, yet expert validation is rare.
problem_and_motivation: Firms and researchers lack a synthesized understanding of how algorithmic customer segmentation is performed in practice and theory. This gap hinders the development, evaluation, and implementation of effective approaches for segmentation.
approach:
  - Conducted a systematic literature review following Kitchenham et al.'s procedure.
  - Searched Web of Science, Emerald Insight, ACM Digital Library, and ABI/INFORM.
  - Screened articles for hygiene factors and relevance, resulting in 172 articles for analysis.
  - Extracted data on algorithms, segment count, evaluation metrics, hyperparameters, and use of experts.
  - Analyzed 134 algorithm-based studies for RQ1-2 and RQ4-RQ5, and 172 for RQ3 and RQ6.
findings:
  - num: 46 different algorithms were identified for customer segmentation, with K-means clustering being the most frequent (20.1%).
  - num: Approximately 80% of studies use a single algorithm for segmentation.
  - num: The average number of customer segments created is 5.7, with four segments being the most common (21.2%).
  - num: 14 unique evaluation metrics were identified, with separation-focused metrics being slightly more prevalent.
  - num: 82% of studies applied only segment size as a hyperparameter.
  - num: Subject matter experts were used for evaluation in only 7 studies (4.1%).
key_figures_tables:
  - Figure 1: Hierarchy of concepts from AI to customer segmentation → Shows segmentation as an unsupervised clustering application.
  - Figure 2: Increasing interest in segmentation studies over time → Confirms the timeliness of the systematic review.
  - Figure 3: Research process leading to article coding → Illustrates the screening and selection flow.
  - Figure 4: Frequency of algorithms used → K-means is the most dominant algorithm.
  - Figure 5: Number of customer segments created → Four segments are most common, with most studies creating ten or fewer.
  - Table 4: Examples of combining customer segmentation algorithms → Shows common multi-algorithm approaches like K-means with SOM or RFM.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Algorithmic customer segmentation (ACS)
    definition: The use of AI/ML algorithms, primarily clustering, to divide customers into groups based on similarities and differences.
  - term: Hyperparameter
    definition: A configuration setting external to the model, set before learning begins.
  - term: Ablation study
    definition: An experiment that removes parts of a model to study the effect on performance.
critical_citations:
  - "[Punj and Stewart, 1983] — Foundational review on clustering in marketing."
  - "[Fernández-Delgado et al., 2014] — Questions the need for many classifiers."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Provides a broad review of algorithmic segmentation methods used in various systems.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly identifies gaps like lack of expert validation and focus on technical metrics over business outcomes.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Reviews algorithms for segmenting users, a core method for creating behavioral profiles.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: contextual
      justification: Mentions segmentation challenges but doesn't specifically address cold-start dynamics.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Systematically classifies algorithms used for segmentation, a key approach for profiling.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Critiques existing evaluation practices and proposes a framework including expert validation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Details the 14 technical metrics commonly used to evaluate segmentation algorithms.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Provides a foundation for evaluation methodologies, relevant for recommendation systems.
  contribution: This paper provides a comprehensive taxonomy of algorithms and evaluation metrics for customer segmentation. It critiques the prevalent technical focus and lack of expert validation in current practice. The proposed research agenda directly informs the evaluation framework for Odin's behavioral profiling and algorithmic modules. The findings on hyperparameter prevalence justify Odin's design focus on the 'number of segments' as a core user-controlled parameter.
  directly_justifies:
    - "Algorithmic customer segmentation is predominantly conducted using a single algorithm, typically K-means."
    - "The number of segments is often determined inductively using quantitative metrics, with four segments being the most common."
    - "Subject matter experts are rarely used to validate segmentation results in research."
    - "Evaluation of segmentation often relies on separation-focused metrics like the Silhouette Index."
    - "Hyperparameters beyond the number of segments are infrequently explored."
  limits:
    - "Excludes articles before the year 2000, potentially missing foundational work."
    - "Focuses only on customer segmentation, not market segmentation."
    - "Does not provide an in-depth comparison of algorithm performance in different business scenarios."
  mapping_rationale: The systematic scan across all 12 functional domains and their topic codes flagged domains 4 (Existing Systems), 5 (Behavioral Profiling), and 12 (System Evaluation) as relevant. Topic codes 4.A, 4.B, 5.A, 5.C, 12.A, and 12.B were assigned 'high' relevance due to direct contributions. Code 5.B received 'contextual' relevance as the paper mentions segmentation challenges but not cold-start profiles. Code 12.C was deemed 'medium' as it provides methodological foundations for evaluating recommendation systems. Domains related to Filipino cultural context (2.A-D), expense categorization (3.A-C), forecasting (6.A-B), budget recommendation (7.A-D), anomaly detection (8.A-C), mobile-first design (9.A-B), data privacy (10.A-B), user engagement (11.A-B), and savings/debt management (13.A-C) were rejected as the paper does not address these specific areas. The paper's systematic review offers a critical framework for evaluating the algorithmic approaches that will underpin Odin's behavioral profiling and segmentation modules.
limitations:
  - "The study does not empirically validate the proposed evaluation framework in a real-world setting. [unacknowledged]"
  - "Does not address the specific challenges of segmenting young professional populations in developing economies. [unacknowledged]"
  - "The review's focus on academic literature may not fully reflect cutting-edge industry practices. [unacknowledged]"
remember_this:
  - K-means is the most dominant algorithm for customer segmentation.
  - Four customer segments are most commonly created.
  - Expert validation of segments is rare in research.
  - Evaluation focuses on technical metrics like separation and compactness.
  - There is a need for more comprehensive evaluation frameworks.
```