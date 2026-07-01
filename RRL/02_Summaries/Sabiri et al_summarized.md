```yaml
paper_id: 10.3390/jimaging11010012
designation: international
title: Hybrid Quality-Based Recommender Systems: A Systematic Literature Review
authors: Sabiri, B.; Khtira, A.; El Asri, B.; Rhanoui, M.
year: 2025
venue: Journal of Imaging
odin_topics:
  - 6.A
  - 6.B
  - 7.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
tldr: A systematic review of hybrid recommender systems identifies key hybridization techniques, evaluation metrics, and research gaps, with a significant focus on addressing the cold-start problem and improving recommendation quality through algorithmic combinations.
problem_and_motivation: Recommender systems struggle with issues like information overload, data sparsity, and the cold-start problem, which limit their effectiveness. The motivation is to synthesize recent advances in hybrid approaches that combine multiple recommendation techniques to overcome these limitations and provide more accurate, personalized suggestions. There is a need for a comprehensive review to guide future research and practical implementations in the field.
approach:
  - Conducted a systematic literature review following the Cochrane Handbook and Kitchenham and Charters guidelines.
  - Searched five academic databases (ACM, Google Scholar, Scopus, Springer, Web of Science) using a defined search string.
  - Applied inclusion and exclusion criteria to screen papers, focusing on those published between 2020 and 2024.
  - Employed the ASReview tool, an open-source machine learning application, to assist in the efficient filtering and selection of relevant articles.
  - Performed both quantitative and qualitative analyses of the 52 selected primary studies to categorize challenges, hybridization strategies, datasets, and evaluation methods.
findings:
  - 75% of the reviewed studies on hybrid recommender systems were published within the last three years, indicating growing research interest.
  - num: Hybrid systems demonstrated a precision of 0.80, recall of 0.92, and an F1-score of 0.86, outperforming single-strategy approaches.
  - num: A hybrid approach combining collaborative filtering and sequential pattern analysis achieved the best performance with a CF-based weight of 0.1.
  - num: The study identified a 'watershed moment' in 2020 with the number of papers on the topic jumping to seven, with a subsequent surge to fifteen in 2022.
  - The cold-start problem and data sparsity are identified as the most critical challenges addressed by hybridization techniques.
key_figures_tables:
  - Figure 10: PRISMA flowchart detailing study selection process → Shows 52 articles were finally selected for review.
  - Figure 11: Spread of research based on publication year → Shows a significant increase in publications after 2020.
  - Figure 17: Confusion matrix for articles selected for the study → Summarizes the performance of the selection process with precision, recall, and F1-score.
  - Table A1: Recapitulative table of the selected articles → Provides a comprehensive overview of each study's issue, strategy, dataset, and results.
key_equations:
  - equation: "Evaluation = \\frac{\\sum_{i=1}^{N} q_{w_i} * a_{r_i}}{N}"
    explanation: Formula for calculating a paper's quality score in the systematic review.
definitions:
  - term: Hybrid Recommender System
    definition: A system that combines two or more recommendation techniques to improve accuracy and overcome individual method limitations.
  - term: Collaborative Filtering
    definition: A recommendation method that suggests items based on the preferences of similar users.
  - term: Content-Based Filtering
    definition: A recommendation method that suggests items based on the characteristics of items a user has liked in the past.
  - term: Cold-Start Problem
    definition: The difficulty of making recommendations for new users or items due to a lack of historical data.
  - term: Data Sparsity
    definition: The problem where limited user-item interactions make it difficult to find patterns for accurate recommendations.
critical_citations:
  - "[Kitchenham and Charters, 2007] — Foundational guidelines for conducting systematic literature reviews."
  - "[Higgins et al., 2023] — Provided the Cochrane Handbook standards for systematic reviews."
  - "[Page et al., 2021] — Standardized the reporting of systematic reviews through the PRISMA 2020 statement."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: The paper reviews algorithms like collaborative and content-based filtering, foundational for predictive modeling in PFMS.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: It analyzes forecasting algorithms such as sequential pattern analysis and deep learning models used in hybrid systems for sequential data.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: The review covers hybrid recommendation techniques that can be adapted for personalized budget recommendations.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Discusses evaluation methods and model performance, which are directly relevant to designing evaluation frameworks for anomaly detection modules.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Reviews algorithms that, while for recommender systems, use similar machine learning approaches (e.g., deep learning) applicable to anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a detailed methodology for evaluating recommender systems, directly applicable to evaluating Odin's algorithmic modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: The study uses metrics like precision, recall, F1-score, diversity, and novelty, which are key for evaluating individual algorithmic modules in a system like Odin.
  contribution: The paper provides a systematic methodology for evaluating hybrid recommender systems that can be directly applied to Odin's development. The discussion of cold-start and data sparsity challenges is crucial for Odin's early-stage user onboarding and forecasting. The review's categorization of hybridization techniques offers a framework for integrating multiple algorithms in Odin's recommendation and anomaly detection modules. It also identifies evaluation metrics and future research directions that inform the design and validation of Odin's financial planning features.
  directly_justifies:
    - Combining collaborative and content-based filtering can improve recommendation accuracy for new users (cold-start).
    - Hybrid systems generally outperform single-strategy approaches in precision and recall.
    - Metrics like novelty and diversity are critical for improving user engagement and satisfaction.
    - Data sparsity remains a key challenge that requires advanced techniques like matrix factorization to mitigate.
  limits:
    - The review focuses on general recommender systems, not specifically on the domain of personal finance management.
    - The findings are based on studies from 2020-2024, which may not cover the most recent algorithmic developments.
    - The review's scope is limited to English-language, peer-reviewed journal articles, potentially missing relevant gray literature.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated canonical topics was performed. The paper's content on algorithmic combinations, evaluation, and challenges was most relevant to the 'Predictive Modeling' (6.A), 'Forecasting' (6.B), 'Budget Recommendation' (7.B), 'Anomaly Detection' (8.A, 8.B), and 'System Evaluation' (12.A, 12.B) domains, yielding 'high' relevance for these topics due to direct applicability. Topics related to Filipino Cultural Context (2.A-D), Expense Categorization (3.A-C), and Mobile-First Design (9.A-B) were considered but rejected as the paper does not address these domain-specific aspects. The paper's focus on systematic review methodology and quantitative performance metrics makes its contribution most valuable to Odin's algorithmic and evaluation design phases, providing a solid foundation for developing and testing its core modules.
limitations:
  - The quality of the review depends on the completeness of the selected databases and search strategy. [unacknowledged]
  - The manual screening process prior to using ASReview may have introduced selection bias.
  - Publication bias may lead to an overestimation of effects, as top-tier journals tend to publish positive results.
  - The findings on algorithmic performance are derived from various domains (e-commerce, music, etc.) and may not directly generalize to PFMS.
remember_this:
  - Hybrid systems can achieve 92% recall in relevant item retrieval.
  - The cold-start problem is a primary challenge addressed by hybridization.
  - Springer was the source for 40% of reviewed papers on this topic.
  - Evaluation metrics like F1-score are crucial for assessing system performance.
  - Research output on hybrid recommenders surged after 2020.
```