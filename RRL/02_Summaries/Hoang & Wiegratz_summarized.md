```yaml
paper_id: 10.1111/eufm.12408
designation: international-algorithm-specific
title: Machine learning methods in finance: Recent applications and prospects
authors: Hoang, D.; Wiegratz, K.
year: 2023
venue: European Financial Management
odin_topics:
  - 4.A
  - 5.A
  - 6.A
  - 6.B
  - 7.B
  - 8.A
  - 10.A
  - 10.B
  - 12.A
tldr: A survey and taxonomy of machine learning applications in finance, classifying uses into constructing superior measures, reducing prediction errors, and extending econometric toolsets.
problem_and_motivation: Despite the rapid growth of ML publications in finance, there is a lack of clarity on how and where to apply ML to solve research problems. This paper aims to provide a systematic taxonomy and guide for financial economists to leverage ML effectively.
approach:
  - Provides a high-level primer on supervised and unsupervised learning and their differences from traditional econometrics.
  - Develops a taxonomy of ML applications in finance based on methodological purpose: superior/novel measures, prediction error reduction, and econometric tool extension.
  - Conducts a bibliometric analysis of 346 ML papers published in 45 major finance journals from 2010 to 2021.
  - Analyzes publication success by research field, journal rank, and application type using distribution and citation data.
  - Illustrates ML benefits with a real estate price prediction application using over four million German listings and comparing OLS to various ML methods.
findings:
  - num: The number of ML publications in finance grew almost elevenfold by 2021 compared to the 2010-2017 average.
  - ML publications account for approximately 3%-4% of publications in top finance journals in 2021, similar to lower-ranked journals.
  - Most ML publications (69.1%) are for economic prediction problems, while superior/novel measures are more common in higher-ranked journals.
  - Applications of ML to construct superior and novel measures receive 10.2 more citations on average than general finance publications.
  - The field of corporate finance/governance shows particularly high potential for ML-based superior/novel measures, receiving 24.2 more citations.
  - num: In a real estate pricing application, boosted regression trees achieved an out-of-sample R² of 77%, compared to 40% for OLS.
key_figures_tables:
  - Figure 1: Comparison of OLS and ML real estate price predictions → ML predictions are much closer to actual prices, especially at the upper end.
  - Figure 4: Prediction performance and average pricing errors of OLS vs. ML methods → Boosted regression trees outperform OLS, reducing average pricing error from 44% to 27%.
  - Table 5: Yearly number and relative share of ML publications in major finance journals by journal rank → ML share grew to 3-4% by 2021 across all ranks.
  - Table 7: Distribution of ML applications by application type and journal rank → Superior/novel measures are more prevalent in A+ journals (56.4%) than in B-ranked journals (18.4%).
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: Supervised Learning
    definition: ML method that makes predictions from labelled data.
  - term: Unsupervised Learning
    definition: ML method that infers data structure from unlabelled data.
  - term: LASSO
    definition: Regularized linear regression that shrinks coefficients and can drive irrelevant ones to zero.
  - term: Boosted Regression Trees
    definition: An ensemble method that iteratively builds trees, focusing on observations previous trees predicted poorly.
  - term: Causal Forests
    definition: A tree-based ML method used to estimate heterogeneous treatment effects.
critical_citations:
  - "[Mullainathan and Spiess, 2017] — Identifies prediction as main ML use in economics."
  - "[Athey and Imbens, 2019] — Reviews ML methods from an econometric perspective."
  - "[Gu et al., 2020] — Predicts stock returns using various ML methods."
  - "[Fuster et al., 2022] — Finds ML can increase bias in credit decisions."
  - "[Bianchi et al., 2021] — Predicts bond risk premiums using machine learning."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Provides a broad overview of ML applications, including those in credit risk and fraud detection relevant to PFMS.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Discusses limitations of traditional econometrics and highlights ML's potential to overcome them.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: low
      justification: Mentions ML for investor profiling and detecting credit risk, but not specifically for behavioral profiling.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly reviews ML methods for forecasting asset prices, volatility, and credit risk, applicable to spending forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Reviews algorithms like LSTM and boosted trees that are directly applicable to forecasting sequential financial data.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: contextual
      justification: Provides a general framework for prediction problems, which is foundational for budget recommendation.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Discusses ML for fraud detection and outlier detection, relevant to anomaly detection modules.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Briefly mentions algorithmic bias in credit decisions, related to trust and fairness, but not privacy.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: Mentions interpretability as a limitation of ML, which is key for user trust.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Uses bibliometric analysis to evaluate publication success and provides methods for comparing model performance.
  contribution: "This paper provides a foundational taxonomy for categorizing ML applications, which can be directly applied to evaluate Odin's algorithmic modules. The bibliometric analysis offers insights into the publication success of different ML approaches, guiding the selection of methods that are both effective and credible. The real estate pricing example demonstrates a concrete methodology for evaluating predictive models against traditional baselines, a process essential for Odin's own model validation."
  directly_justifies:
    - "Machine learning methods can reduce prediction error in economic prediction problems by leveraging high-dimensional data."
    - "ML applications are most successful in top journals when used to construct superior and novel measures, not just for prediction."
    - "The field of corporate finance and governance shows the highest potential for ML-based superior measures."
    - "Regularized linear methods like LASSO and tree-based methods like boosted regression trees are state-of-the-art for numerical data."
    - "Unsupervised learning methods such as clustering can be used to infer data structure in financial applications."
  limits:
    - "The survey's classification is based on a manual review and may not capture all nuances of ML applications."
    - "The bibliometric analysis is limited to papers published up to 2021 and may not reflect the most current trends."
    - "The real estate pricing example is illustrative and not generalizable to all prediction problems."
    - "The paper does not provide a practical implementation guide for applying ML in a production system."
  mapping_rationale: "A systematic scan across all 12 functional domains was performed. Domains related to predictive modeling (6.A, 6.B) and evaluation (12.A) were flagged as high relevance due to the paper's direct focus on forecasting algorithms and performance comparison. Domains concerning existing systems (4.A, 4.B) and anomaly detection (8.A) were assigned medium relevance because the paper reviews the landscape of ML applications and discusses fraud detection. Behavioral profiling (5.A), budget recommendation (7.B), data privacy (10.A), and user trust (10.B) were deemed low or contextual as the paper mentions them but does not provide design-specific insights for a PFMS. Domains like Filipino cultural context, expense categorization, and user retention (1.A-3.C, 11.A-11.B) were considered and rejected as the paper does not address these topics. The paper is overall highly relevant to Odin's design as it establishes the state-of-the-art in ML methods and their evaluation, providing a methodological blueprint for Odin's predictive and classification modules."
limitations:
  - "The illustrative application of ML to real estate pricing is conducted on German data and may not generalize to other markets or contexts."
  - "The paper's taxonomy is based on a manual review, which introduces some subjectivity." [unacknowledged]
  - "The study does not provide a detailed cost-benefit analysis of implementing ML versus traditional methods in a production setting." [unacknowledged]
  - "The paper acknowledges the low interpretability of complex ML models as a limitation."
  - "The paper acknowledges that ML generally requires large datasets and high computational costs."
remember_this:
  - "ML publications in finance grew almost elevenfold from 2010-2017 to 2021."
  - "Superior and novel measures are the most successful ML application type in top finance journals."
  - "Boosted regression trees achieved 77% R² in real estate pricing, far exceeding OLS at 40%."
  - "ML offers benefits over traditional methods for high-dimensional prediction problems."
  - "Algorithmic bias is a potential concern when ML influences credit or lending decisions."
```