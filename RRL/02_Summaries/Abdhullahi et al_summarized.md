```yaml
paper_id: 10.1109/ACCESS.2025.3587231
designation: international-algorithm-specific
title: A Systematic Literature Review of Concept Drift Mitigation in Time-Series Applications
authors: Abdullahi, M.; Alhussian, H.; Aziz, N.; Abdulkadir, S. J.; Baashar, Y.; Alashhab, A. A.; Afrin, A.
year: 2025
venue: IEEE Access
odin_topics:
  - 4.A
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 9.A
  - 10.A
  - 12.A
  - 12.B
tldr: A systematic review identifying SVM as the most effective learner for detecting and adapting to concept drift in time-series classification and regression tasks.
problem_and_motivation: Concept drift continuously changes data statistical properties, degrading machine learning model performance in time-series applications. Existing research focuses on classification with minimal attention to regression, and efficient identification of changes and responses in a time-series context remains challenging.
approach:
  - A systematic literature review was conducted using PRISMA 2020 guidelines.
  - The search was performed across SCOPUS, ScienceDirect, IEEE Xplore, Web of Science, MDPI, and ACM databases.
  - A total of 60 studies published between 2013 and 2024 were selected for in-depth review.
  - Data extraction and synthesis focused on algorithms, evaluation metrics, problem scopes, and drift handling techniques.
  - A comparative analysis of baseline methods and a roadmap for AI-based drift detection were presented.
findings:
  - num: Support Vector Machines demonstrated high detection accuracy and effective memory for concept drift.
  - num: 60 studies were identified and surveyed, with the highest publication count in 2022.
  - num: 60% of the selected studies focused on classification tasks, while only 6% addressed regression.
  - Accuracy was the most common evaluation metric for assessing concept drift detection models.
  - Ensemble-based methods like ENSDS, SVR, and ELM are effective for detecting concept drift in time-series data.
  - ADWIN, HDDM, and DDM are the most frequently used algorithms for handling different drift types.
  - LSTM models are widely used due to their ability to capture temporal dependencies and adapt to gradual changes.
  - The TriLS system enables lightweight model tuning by offloading computationally intensive tasks to the cloud.
key_figures_tables:
  - Figure 2: SLR mapping process illustrating the four stages of screening → flow of study selection.
  - Figure 5: Publication trend from 2013 to 2024 showing a significant increase in 2021-2022 → growing research emphasis.
  - Figure 7: Distribution of ML problem scopes, with classification dominating at 60% → research gap in regression.
  - Figure 9: Frequency of learning algorithms, with SVM, LSTM, and k-NN being most common → preferred learners.
  - Table 8: Classification of studies by drift handling technique (e.g., ADWIN, HDDM) → commonly used methods.
key_equations:
  - equation: "Accuracy = (TP+TN) / (TP+TN+FP+FN)"
    explanation: Proportion of correctly identified instances.
  - equation: "Precision = TP / (TP+FP)"
    explanation: Proportion of detected drifts that are actual drifts.
  - equation: "Recall = TP / (TP+FN)"
    explanation: Proportion of actual drifts detected by the model.
  - equation: "F1 = 2 * (Precision * Recall) / (Precision + Recall)"
    explanation: Harmonic mean of precision and recall.
  - equation: "RMSE = sqrt( (1/n) * sum((y_i_hat - y_i)^2) )"
    explanation: Square root of average squared prediction error.
definitions:
  - term: Concept Drift
    definition: Continuous changes in the statistical properties of a dataset over time, degrading ML model performance.
  - term: Incremental Drift
    definition: Minimal and continuous change in the original data distribution.
  - term: Gradual Drift
    definition: Noticeable and gradual changes in the target data distribution.
  - term: Sudden Drift
    definition: Abrupt and significant change in the original data distribution at a specific time.
  - term: Recurring Drift
    definition: A situation in which an old concept reappears after a period of absence.
  - term: ADWIN
    definition: Adaptive Windowing algorithm that dynamically adjusts window size based on data variations.
  - term: DDM
    definition: Drift Detection Method based on monitoring prediction errors.
  - term: HDDM
    definition: Hoeffding Drift Detection Method using statistical measures for drift detection.
  - term: SVM
    definition: Support Vector Machine, a supervised learning model effective for detecting shifts in data structure.
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network for capturing temporal dependencies.
  - term: PRISMA
    definition: Preferred Reporting Items for Systematic Reviews and Meta-Analyses.
critical_citations:
  - "[Bayram et al., 2022] — Surveys performance-aware drift detectors."
  - "[Gama et al., 2014] — Comprehensive survey on concept drift adaptation."
  - "[Lima et al., 2022] — Systematic literature review on regression under concept drift."
  - "[Iwashita & Papa, 2019] — Overview of concept drift learning."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Reviews the broader landscape of ML systems affected by drift.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly addresses predictive modeling and performance degradation due to drift.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Reviews forecasting algorithms like LSTM and SVM for time-series data.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Discusses anomaly detection in the context of drift in time-series data.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Reviews algorithms like autoencoders for drift detection in multivariate streaming data.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Mentions edge computing and lightweight models like TML for on-device adaptation.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Discusses IoT and smart city applications, touching on data handling but not explicitly privacy.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a comprehensive evaluation framework with metrics for drift detection.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Compares algorithms like SVM and LSTM for predictive performance under drift.
  contribution: This systematic review provides a consolidated evaluation of algorithms for detecting concept drift, which is critical for maintaining the accuracy of predictive models like Odin's spending forecasts. Its identification of SVM and LSTM as effective learners informs the selection of core algorithms for Odin's forecasting and anomaly detection modules. The detailed mapping of evaluation metrics and experimental procedures offers a blueprint for rigorously testing Odin's machine learning components. The review's discussion of computational efficiency and edge-cloud architectures provides guidance for deploying Odin's algorithm modules in a mobile-first context.
  directly_justifies:
    - "SVM is the most effective learning algorithm for detecting concept drift in time-series data."
    - "LSTM models are effective in capturing temporal dependencies and adapting to gradual changes."
    - "ADWIN, HDDM, and DDM are the most frequently used algorithms for handling different drift types."
    - "Accuracy is the most common evaluation metric for assessing concept drift detection models."
  limits:
    - "The review focuses on classification and regression, potentially overlooking other learning paradigms like reinforcement learning."
    - "Most studies were evaluated on synthetic or limited real-world datasets, which may not reflect the complexity of personal finance data."
    - "The review does not provide an empirical benchmark or comparative analysis of the identified methods, relying instead on a synthesis of existing literature."
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The paper was flagged as highly relevant to Predictive Modeling (6.A, 6.B) because it directly addresses performance degradation in time-series forecasting, a core function of Odin. It is also highly relevant to System Evaluation (12.A, 12.B) for its detailed framework of evaluation metrics and algorithm comparison. Medium relevance was assigned to Anomaly Detection (8.A, 8.B) due to its focus on detecting changes in data distributions, and Mobile-First Design (9.A) for its discussion of edge computing and lightweight models. Contextual relevance was assigned to Landscape of Existing Systems (4.A) and Data Privacy (10.A) as the paper does not specifically address financial systems or privacy. While the paper touches on algorithm selection (12.B), its primary contribution is a synthesis of methods for drift handling, making it a foundational reference for Odin's algorithm evaluation and selection process.
limitations:
  - "The study analyzed only 60 research articles from a specific set of databases, potentially missing relevant studies."
  - "The search was limited to papers published in English between 2013 and 2024."
  - "Most of the currently proposed drift detection methods have not been fully solved, and reliance on simulation datasets may not capture real-world scenarios."
  - "Several studies tested their proposed methods using a single dataset, which may limit generalizability."
  - "Comparisons with state-of-the-art studies are limited."
  - "The study did not investigate similarity and dissimilarity-based methods for concept drift detection."
  - "The SLR focuses on algorithm review without a new empirical benchmark, limiting actionable design guidance without further testing on financial data. [unacknowledged]"
remember_this:
  - "Concept drift continuously degrades model performance in time-series forecasting."
  - "SVM is identified as the most effective learner for drift detection and adaptation."
  - "The number of concept drift publications has significantly increased, with 60 studies reviewed."
  - "Only 6% of reviewed studies focused on regression tasks, highlighting a gap."
  - "Accuracy was the most common metric for evaluating concept drift detection models."
```