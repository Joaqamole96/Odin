```yaml
paper_id: 10.1145/3689627
designation: international
title: Multi-Class Imbalanced Data Handling with Concept Drift in Fog Computing: A Taxonomy, Review, and Future Directions
authors: Sharief, F.; Ijaz, H.; Shojafar, M.; Naeem, M. A.
year: 2024
venue: ACM Computing Surveys
odin_topics:
  - "5.A"
  - "5.B"
  - "6.A"
  - "6.B"
  - "8.A"
  - "8.B"
  - "12.A"
  - "12.B"
tldr: A systematic review of techniques for handling multi-class imbalanced data and concept drift in IoT and Fog computing environments.
problem_and_motivation: Imbalanced data in IoT and Fog computing leads to biased analytics and poor decision-making, especially for rare events. Existing solutions focus heavily on binary-class problems, while multi-class imbalanced data streams with concept drift remain largely unaddressed. A comprehensive review and taxonomy are needed to identify gaps and guide future research.
approach:
  - Conducted a systematic literature review using the PRISMA framework to identify 103 relevant studies.
  - Categorizes imbalanced data handling techniques into data-level, algorithmic, ensemble-level, and cost-sensitive solutions.
  - Distinguishes between batch and stream data processing for both binary and multi-class scenarios.
  - Reviews performance metrics, including binary-class (Accuracy, Kappa, MCC, Precision, Recall, F-measure, G-mean, AUC) and multi-class (AveAcc, Average Precision, MAUC, Kappa) metrics.
  - Specifically analyzes concept drift handling methods and their intersection with class imbalance.
findings:
  - num: MAUC was the most popular metric for multi-class imbalanced data, used in 23% of the surveyed studies.
  - num: Accuracy was the most common metric for multi-class imbalanced data in IoT networks, used in 22% of studies.
  - num: Accuracy was used for concept drift evaluation in 24% of studies, while MOA was the primary optimization tool in 36%.
  - num: Apache Storm was the most used stream processing tool in Fog, covering 17% of the research area.
  - Ensemble learning, particularly combining resampling with ensemble methods, is a preferred strategy for handling imbalanced data with concept drift.
  - The combined approach of oversampling and undersampling often yields better results than either technique alone.
key_figures_tables:
  - "Figure 4: Taxonomy of imbalanced data with concept drift → Provides a structured overview of the problem space."
  - "Figure 6: Metrics for multi-class general form of data → MAUC is the dominant metric for multi-class evaluation."
  - "Figure 7: Metrics used for multi-class data in IoT → Accuracy is the primary metric in IoT contexts."
  - "Figure 10: Software tools used for concept drift handling → MOA is the most widely used tool."
key_equations:
  - equation: "Acc = (TP + TN) / N"
    explanation: "Standard accuracy formula for classification performance."
  - equation: "G-mean = sqrt(Sensitivity * Specificity)"
    explanation: "Geometric mean of class-wise accuracies for imbalanced data."
  - equation: "MAUC = (2 / (r(r-1))) * sum_{i<j} [A(C_i, C_j) + A(C_j, C_i)]"
    explanation: "Mean AUC for multi-class problems, averaging pairwise AUCs."
definitions:
  - term: "Fog Computing"
    definition: "A distributed computing paradigm that brings cloud services closer to the network edge to reduce latency."
  - term: "Imbalanced Data"
    definition: "Data where one class has significantly more instances than another, leading to biased models."
  - term: "Concept Drift"
    definition: "The change in the statistical properties of a target variable over time in a data stream."
  - term: "SMOTE"
    definition: "Synthetic Minority Over-sampling Technique, a method for creating synthetic samples for the minority class."
  - term: "MAUC"
    definition: "Mean Area Under the ROC Curve, a metric for evaluating multi-class classifier performance."
  - term: "MOA"
    definition: "Massive Online Analysis, a popular open-source framework for data stream mining."
critical_citations:
  - "[Gao et al., 2007] — General framework for mining concept-drifting data streams with skewed distributions."
  - "[Wang et al., 2018] — Systematic study of online class imbalance learning with concept drift."
  - "[Korycki and Krawczyk, 2021] — Concept drift detection from multi-class imbalanced data streams."
  - "[Alencar et al., 2023] — New approach combining LSTM and concept drift for data stream analytics on Fog computing."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "contextual"
      justification: "Discusses classification of imbalanced data, relevant to profiling minority behaviors."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "contextual"
      justification: "Covers handling of novel and recurring classes, akin to cold-start and evolving profiles."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "contextual"
      justification: "Reviews forecasting and predictive modeling in data streams."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "contextual"
      justification: "Discusses algorithms applicable to sequential data streams, like spending data."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "contextual"
      justification: "Frames imbalanced data handling as crucial for anomaly detection (e.g., fraud)."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "contextual"
      justification: "Reviews algorithms (e.g., ensemble, cost-sensitive) used for detecting rare events."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Provides a comprehensive taxonomy of performance metrics for imbalanced data, directly applicable."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Discusses metrics like G-mean, AUC, and MAUC specifically designed for evaluating models on imbalanced data."
  contribution: "This survey provides a foundational taxonomy of methods for handling imbalanced data and concept drift, which is critical for Odin's algorithmic modules. Its systematic evaluation of performance metrics (e.g., MAUC, G-mean) offers a validated framework for assessing Odin's anomaly detection and forecasting modules. The analysis of ensemble and cost-sensitive methods informs the design of robust classifiers for imbalanced financial data. The review of concept drift handling techniques is directly relevant to Odin's need to adapt to evolving user spending patterns."
  directly_justifies:
    - "Performance metrics like MAUC and G-mean are more appropriate than accuracy for evaluating models on imbalanced financial data."
    - "Combining data-level (e.g., SMOTE) and algorithm-level methods improves classification performance on imbalanced streams."
    - "Ensemble learning is a robust strategy for handling both class imbalance and concept drift."
    - "Concept drift detection is essential for maintaining model accuracy in dynamic environments like personal finance."
  limits:
    - "The survey does not provide empirical results or benchmarks on financial datasets."
    - "It focuses on general imbalanced data issues, not specifically tailored to personal finance or spending behaviors."
    - "The discussion of concept drift is general and does not delve into specific financial patterns like seasonal spending."
  mapping_rationale: "A systematic scan was conducted across all 12 functional domains and their associated topic codes. The paper was flagged as relevant primarily for domains related to algorithmic evaluation (12.A, 12.B), anomaly detection (8.A, 8.B), and forecasting (6.A, 6.B) due to its exhaustive review of techniques and metrics. Topics like 2.A (Cultural Practices) and 2.B (Seasonal Spending) were rejected as they are not addressed. Codes under 'Behavioral Profiling' (5.A, 5.B) were marked contextual, as the paper's discussion of novel/recurring classes and classification challenges is analogous but not directly applied to financial behavior. The overall relevance is high for informing Odin's algorithmic design and evaluation strategy, particularly the selection of appropriate performance metrics for imbalanced data."
limitations:
  - "The survey is a literature review and does not propose or test new algorithms."
  - "The analysis of Fog computing for imbalanced streams is limited, highlighting it as a research gap rather than providing solutions. [unacknowledged]"
  - "The paper does not address data privacy or user trust, which are crucial for personal finance systems. [unacknowledged]"
remember_this:
  - "MAUC was the most popular metric for multi-class imbalanced data in the surveyed literature."
  - "Apache Storm was the dominant stream processing tool in Fog computing research."
  - "Ensemble methods are a preferred strategy for handling imbalanced data with concept drift."
  - "Combining oversampling and undersampling techniques often yields superior classification results."
  - "Accuracy is a misleading metric for imbalanced data; use G-mean, AUC, or MAUC instead."
```