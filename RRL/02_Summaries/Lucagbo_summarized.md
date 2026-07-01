```yaml
paper_id: 3a8c4f5d-6e7b-4c9a-b1d2-3e4f5a6b7c8d
designation: local-algorithm-specific
title: Comparison of Ordinal Logistic Regression with Tree-Based Methods in Predicting Socioeconomic Classes in the Philippines
authors: Lucagbo, M.D.C.
year: 2016
venue: The Philippine Statistician
odin_topics:
  - 1.A
  - 2.A
  - 5.C
  - 12.A
  - 12.B
tldr: Ordinal logistic regression outperforms bagging, random forests, and boosting in predicting Philippine household socioeconomic classes, achieving 41.8% test set accuracy.
problem_and_motivation: Predicting socioeconomic class (SEC) in the Philippines is essential for targeted marketing and policy, but direct expenditure data is impractical for rapid surveys. Existing methods use proxy variables but require robust predictive models. This study addresses the gap by evaluating whether modern tree-based methods can improve upon the established ordinal logistic regression approach.
approach:
  - Data from 2009 Family Income and Expenditure Survey (FIES) with 36,812 households, split 90/10 into training and test sets.
  - Response variable is nine ordinal socioeconomic clusters; 61 predictors derived from 36 easy-to-ask variables.
  - Applied ordinal logistic regression using the cumulative logit model via R package 'rms'.
  - Implemented bagging with node size 30 and all 61 predictors considered per split using R package 'randomForest'.
  - Applied random forests with node size 30 and m≈√61≈8 predictors considered per split to decorrelate trees.
  - Used boosting with 220 trees, multinomial distribution, and maximum interaction depth of 4 via R package 'gbm'.
findings:
  - num: Ordinal logistic regression achieved the highest test set hitrate at 41.8%.
  - num: Random forests achieved a test set hitrate of 40.6%, slightly lower than logistic regression.
  - num: Bagging achieved a test set hitrate of 39.2%.
  - num: Boosting had the lowest performance with a test set hitrate of 35.8%.
  - Clusters 2, 3, 8, and 9 (lowest and highest expenditure) are consistently easier to predict, with hitrates often exceeding 50%.
  - Clusters 4, 5, 6, and 7 (middle class) are consistently the hardest to classify, with hitrates often below 30%.
  - The ordinal logistic regression model had a 16.3% test hitrate for cluster 4, while boosting had only 0.6%.
  - Random forests excelled at predicting cluster 3 (66.3% test hitrate), while boosting excelled at cluster 8 (63.4%).
key_figures_tables:
  - Table 2.1: Median total annual family expenditure by cluster → shows clear ordinal progression from Php 34,744 to Php 738,592.
  - Table 4.1.2: Confusion matrix for ordinal logistic regression on test set → hitrate 41.8% with cluster 4 hardest (16.3%).
  - Table 4.2.2: Confusion matrix for bagging on test set → hitrate 39.2% with cluster 4 hardest (13.1%).
  - Table 4.3.2: Confusion matrix for random forests on test set → hitrate 40.6% with cluster 4 hardest (5.4%).
  - Table 4.4.2: Confusion matrix for boosting on test set → hitrate 35.8% with cluster 4 hardest (0.6%).
  - Table 4.6: Summary hitrates for training and test sets by classifier → ordinal logistic regression best overall.
key_equations:
  - equation: "logit[P(Y ≤ j)] = log[(π1+...+πj)/(π(j+1)+...+πJ)], j=1,...,J-1"
    explanation: Defines cumulative logits for ordinal response modeling.
  - equation: "logit[P(Y ≤ j)] = α_j + βx"
    explanation: Proportional odds model with single slope parameter β.
  - equation: "f̂_bag(x) = (1/B) ∑_{b=1}^B f̂^{*b}(x)"
    explanation: Bagging averages predictions from B bootstrapped trees.
definitions:
  - term: SEC
    definition: Socioeconomic class of a Philippine household.
  - term: 1SEC
    definition: The new Philippine socioeconomic classification system introduced in 2012.
  - term: FIES
    definition: Family Income and Expenditure Survey conducted by the Philippine Statistics Authority.
  - term: Hitrate
    definition: Percentage of households correctly classified by a model.
  - term: Bagging
    definition: Bootstrap aggregation, an ensemble method that reduces variance by averaging predictions from bootstrapped samples.
  - term: Random Forests
    definition: An ensemble method that builds decorrelated decision trees by considering a random subset of predictors at each split.
  - term: Boosting
    definition: An ensemble method that grows trees sequentially, each fitting a modified version of the data.
critical_citations:
  - "[Bersales et al., 2013] — Defines the 1SEC 2012 classification system and the ordinal logistic regression approach."
  - "[James et al., 2013] — Provides theoretical and practical foundations for bagging, random forests, and boosting."
  - "[Breiman, 2001] — Establishes random forests as an accurate algorithm handling thousands of variables."
  - "[Lucagbo, 2015] — Previous comparison of ordinal logistic regression with ANN, SVM, and discriminant analysis."
  - "[Agresti, 2007] — Foundational text for cumulative logit models used in ordinal logistic regression."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Paper classifies Philippine households by expenditure, a key demographic attribute.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Uses Philippine FIES data and the 1SEC system, reflecting local financial structures.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Directly compares classification algorithms for household grouping, applicable to behavioral profiling.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses hitrate and confusion matrices as evaluation metrics, relevant to Odin's evaluation needs.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides a rigorous comparison of ordinal logistic regression against tree-based algorithms, informing module selection.
  contribution: "This paper validates ordinal logistic regression as a robust classifier for socioeconomic segmentation, providing a benchmark for Odin's behavioral classification module. The demonstrated superior performance over tree-based methods suggests a preference for interpretable, linear models when the outcome is ordinal and data is structured. The identified difficulty in classifying 'middle class' households mirrors the challenge Odin may face in profiling users with moderate or variable spending patterns. The use of hitrate and per-cluster accuracy provides a template for evaluating Odin's own classification modules. The paper's focus on Philippine data ensures its findings are culturally grounded and directly applicable to the target user base."
  directly_justifies:
    - "Ordinal logistic regression achieves 41.8% test hitrate, suitable for a 9-class problem in a Philippine context."
    - "Tree-based methods offer only marginal improvements and may not justify added complexity over logistic regression."
    - "Middle-class households are inherently harder to classify, requiring specialized handling in Odin's profiling."
    - "Boosting underperforms on this data, suggesting caution when applying it to Odin's classification tasks."
    - "Expenditure-based clusters in the Philippines exhibit a clear ordinal structure, supporting ordinal modeling."
  limits:
    - "Study uses 2009 FIES data, which may not reflect current spending patterns or the impact of digital financial services."
    - "Findings are specific to the Philippine 1SEC classification system and may not generalize to other segmentation schemes."
    - "The definition of 'easy-to-ask' variables may not align with data Odin can realistically collect from users."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant to the 'Behavioral Profiling & Classification' domain (Topic 5.C) because it directly compares classification algorithms for grouping households by financial characteristics, which is analogous to Odin's user profiling task. It also informs 'System Evaluation' (Topics 12.A and 12.B) by providing a rigorous comparative methodology and performance metrics like hitrate and confusion matrices. The 'Filipino Cultural Context' domain (Topics 1.A, 2.A) was considered relevant contextually, as the study is grounded in Philippine data and the culturally-specific 1SEC system. Topics related to expense categorization (3.A), forecasting (6.A), budgeting (7.A), and anomaly detection (8.A) were considered and rejected because the paper does not address these functional areas; it focuses solely on classification. The borderline case of 'Behavioral Profiling' (5.A) was considered, but the paper's primary contribution is the comparison of classification approaches (5.C), not the definition of the profiles themselves. The overall relevance to Odin is moderate to high, providing a strong methodological benchmark for classification modules and cultural grounding."
limitations:
  - "The 2009 FIES data is outdated and may not represent current financial behaviors of Filipino young professionals. [unacknowledged]"
  - "The study does not address model calibration or probability outputs, only classification accuracy. [unacknowledged]"
  - "The tree-based methods were not tuned extensively, potentially underrepresenting their true performance."
  - "The study uses expenditure as a proxy for SEC, which may not capture the full nuance of socioeconomic status."
  - "The hitrate metric does not account for the cost of misclassification, which may vary by cluster."
remember_this:
  - "Ordinal logistic regression achieved 41.8% test hitrate for 9-class SEC prediction."
  - "Middle-class clusters are consistently hardest to classify across all methods."
  - "Random forests (40.6%) and bagging (39.2%) are close alternatives to logistic regression."
  - "Boosting performed worst (35.8%) on this Philippine household classification task."
  - "Expenditure is a strong, ordinal proxy for socioeconomic class in the Philippines."
```