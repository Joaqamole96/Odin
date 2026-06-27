```yaml
paper_id: 10.14778/3632093.3632110
designation: international-algorithm-specific
title: An Experimental Evaluation of Anomaly Detection in Time Series
authors: Zhang, A.; Deng, S.; Cui, D.; Yuan, Y.; Wang, G.
year: 2023
venue: Proceedings of the VLDB Endowment
odin_topics:
  - 8.A
  - 8.B
  - 8.C
  - 12.A
  - 12.B
  - 6.A
tldr: A comprehensive experimental evaluation of 17 time-series anomaly detection algorithms, analyzing effectiveness, efficiency, and robustness across multiple factors.
problem_and_motivation: The diversity and complexity of time-series data, coupled with a lack of standardized comparative evaluations, make it difficult for users to select appropriate anomaly detection methods for real-world applications. This is especially critical in personal finance, where inaccurate anomaly detection can erode user trust.
approach:
  - Presents a taxonomy of anomaly detection methods based on data dimension, processing technique, and anomaly type, with six inner classes.
  - Conducts systematic intra- and inter-class comparisons of 17 state-of-the-art algorithms on real and synthetic datasets.
  - Evaluates algorithms using both point and range metrics, analyzing effectiveness, efficiency, and robustness to anomaly rates, data sizes, dimensions, patterns, and thresholds.
  - Tests algorithm performance under different application scenarios, including false positive/negative rates and early detection capabilities.
  - Provides a practical guide for selecting anomaly detection methods based on experimental findings.
findings:
  - "num: Online methods can be ten times slower than simple batch methods when the window size is large."
  - "num: The point-adjust method can inflate F-measure by an average of 27.0% for point datasets and 31.2% for subsequence datasets under point metrics."
  - "num: Using range metrics on subsequence datasets leads to a negative average promotion of -67.6% when using the point-adjust method."
  - Point methods can perform well for global subsequence anomalies with extreme values, potentially relaxing the need for length input.
  - No single algorithm is suitable for all cases; optimal selection depends on dataset characteristics and application requirements.
key_figures_tables:
  - "Figure 1: Taxonomy of anomaly detection algorithms based on three facets (data dimension, processing technique, anomaly type) → Provides a structured framework for method classification."
  - "Table 2: Properties of considered anomaly detection algorithms (algorithm, multi-dimensional, process, anomaly type, threshold, code, speedup) → Summarizes key characteristics and implementation details."
  - "Table 4: Accuracy over various datasets for point and subsequence methods → Shows that NETS performs best in many point cases, while PBAD and BeatGAN have better overall accuracy for subsequence anomalies."
  - "Figure 15: Varying thresholds on ECG and Uni-sub-g datasets → Demonstrates the robustness of NormA and IDK compared to other methods, with IDK showing the best overall performance."
  - "Figure 18: Practical guide for timeseries anomaly detection → Provides a decision flowchart for method selection based on anomaly type, dimensionality, and application needs."
key_equations:
  - equation: "Precision = TP / (TP + FP)"
    explanation: "Metric for point anomaly detection accuracy."
  - equation: "Recall = TP / (TP + FN)"
    explanation: "Metric for point anomaly detection completeness."
  - equation: "F-measure = 2 * Precision * Recall / (Precision + Recall)"
    explanation: "Harmonic mean of precision and recall."
definitions:
  - term: "Point Anomaly"
    definition: "An individual data point that deviates significantly from the majority of the data."
  - term: "Subsequence Anomaly"
    definition: "A consecutive set of data points that is inconsistent with the rest of the time series."
  - term: "Range Metric"
    definition: "An evaluation metric for subsequence anomalies that focuses on the overlap between predicted and true anomaly ranges."
  - term: "Point-adjust"
    definition: "A method that converts false negatives to true positives within an anomaly segment if any point in the segment is detected as anomalous."
critical_citations:
  - "[Tatbul et al., 2018] — Introduced range metrics for subsequence anomalies."
  - "[Lai et al., 2021] — Provides definitions and benchmarks for time series outlier detection."
  - "[Schmidl et al., 2022] — Comprehensive evaluation of anomaly detection methods."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly addresses anomaly detection in time series, a core module of Odin.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Evaluates 17 state-of-the-art algorithms, many applicable to spending data.
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: medium
      justification: Discusses threshold robustness and parameter search, relevant for cold-start scenarios.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides a systematic evaluation methodology applicable to Odin's modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Directly compares effectiveness, efficiency, and robustness of anomaly detection algorithms.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Many anomaly detection methods rely on prediction models, and the paper's findings on LSTM and GAN are relevant.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: The paper discusses seasonal anomalies in a general sense, but not specifically Filipino contexts.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Provides a landscape of TAD, but not PFMS specifically.
  contribution: "This paper provides an experimental framework and baseline comparisons that can directly inform the selection of anomaly detection algorithms for Odin's spending monitoring module. The findings on point-adjust method biases are critical for ensuring Odin does not overstate its detection accuracy. The practical guide (Figure 18) offers a decision-making tool for integrating a suitable algorithm, and the analysis of efficiency and robustness helps in balancing accuracy with mobile-first constraints. The paper's taxonomy and evaluation metrics can also be adopted for Odin's system evaluation to benchmark its anomaly detection performance against established methods."
  directly_justifies:
    - "The point-adjust method can inflate F-measure by an average of 27.0% for point datasets."
    - "Online methods can be ten times slower than simple batch methods when the window size is large."
    - "No single anomaly detection algorithm is suitable for all cases; optimal selection depends on data characteristics."
    - "NP performs best for global subsequence anomalies, while NormA is more robust to threshold settings."
    - "Using range metrics on subsequence anomalies leads to more reasonable and robust results than point metrics."
  limits:
    - "The study focuses on a specific set of algorithms and does not cover all possible anomaly detection techniques."
    - "The evaluation is primarily on synthetic and benchmark datasets, which may not fully capture the nuances of real-world Filipino spending data."
    - "The practical guide is based on current findings and may not be exhaustive for all future scenarios."
    - "The paper does not address the specific contextual and cultural factors relevant to Filipino young professionals."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains of Anomaly Detection (8) and System Evaluation (12) were flagged as highly relevant, with codes 8.A, 8.B, 8.C, 12.A, and 12.B assigned. The paper directly evaluates algorithms and provides a framework for assessing their performance, which is directly applicable to Odin's anomaly detection module. The code 6.A was also selected as medium relevance because many TAD methods use predictive models, and the paper's findings on deep learning architectures (LSTM, GAN) are relevant to forecasting. Borderline cases were considered: while the paper discusses seasonal anomalies (2.D), it is not specific to Filipino cultural contexts; the discussion of existing systems (4.A) is at a TAD level, not PFMS. Domains like Mobile-First Design (9), Data Privacy (10), and User Retention (11) were considered and rejected as the paper does not address these aspects. The overall relevance to Odin is high, as it provides a critical evaluation of a core algorithmic component for the PFMS."
limitations:
  - "The study does not consider the specific characteristics of Filipino financial data, such as high variability and unique cultural spending patterns."
  - "The parameter search is conducted per dataset, which may not be feasible in a real-time mobile-first application like Odin."
  - "The practical guide, while useful, requires expertise to interpret and adapt to specific application contexts. [unacknowledged]"
  - "The evaluation of deep learning methods did not compare their efficiency, which is a key constraint for mobile applications. [unacknowledged]"
  - "The study uses anomaly-free training sets, which may not be available in real-world scenarios for Odin. [unacknowledged]"
remember_this:
  - "No single anomaly detection algorithm fits all cases."
  - "Point-adjust methods can inflate reported accuracy by 27-31%."
  - "NETS is the most efficient point anomaly method."
  - "NP performs best for global subsequence anomalies."
  - "Range metrics are more robust than point metrics for subsequence anomalies."
```