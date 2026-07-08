```yaml
paper_id: 10.3390/math13030368
designation: local-algorithm-specific
title: Evaluation of Cost-Sensitive Learning Models in Forecasting Business Failure of Capital Market Firms
authors: Peykani, P.; Peymany Foroushany, M.; Tanasescu, C.; Sargolzaei, M.; Kamyabfar, H.
year: 2025
venue: Mathematics
odin_topics:
  - 4.A
  - 5.A
  - 6.A
  - 8.A
  - 8.B
  - 12.A
tldr: Cost-sensitive machine learning models, particularly CatBoost, effectively identify failing businesses in an imbalanced Iranian capital market dataset, achieving high sensitivity but low precision.
problem_and_motivation: Credit datasets are inherently imbalanced, causing standard machine learning models to achieve high accuracy but low sensitivity in identifying failing firms, which is costly. Existing cost-sensitive methods have been underexplored for business failure prediction, especially in emerging markets like Iran.
approach:
  - Applied CorrOV-CSEn, a correlation-based oversampling with cost-sensitive ensemble learning, to an Iranian capital market dataset of 2987 training and 1240 test instances from 2015-2022.
  - Evaluated six algorithms: Multi-Layer Perceptron (MLP), Random Forest, Gradient Boosting, XGBoost, AdaBoost, and CatBoost.
  - Used nine financial and stock price-based features derived from Altman and Carton & Hofer models.
  - Compared CorrOV-CSEn performance against the standard SMOTE resampling method.
  - Assessed models using sensitivity, precision, and F1-score, with statistical significance evaluated via the Friedman–Nemenyi test.
findings:
  - num: CorrOV-CSEn CatBoost achieved the highest sensitivity of 0.909 on the test data.
  - num: SMOTE CatBoost achieved the highest F1-score of 0.733 and precision of 0.717.
  - num: Across four datasets, CatBoost consistently showed perfect sensitivity (1.00) in two subsets.
  - All models exhibited relatively low precision when using the CorrOV-CSEn method.
  - The Friedman test revealed CatBoost had significantly higher sensitivity but significantly lower precision than AdaBoost and Gradient Boosting.
  - X1 (Net Working Capital/Total Assets) was the most important feature across all models except MLP.
key_figures_tables:
  - Table 2: Dataset features and their formulas used for prediction → Defines the nine financial and stock-price features.
  - Table 6: Performance metrics for CorrOV-CSEn and SMOTE across all models → Shows CatBoost's sensitivity advantage and precision trade-off.
  - Table 7: Model performance across four data subsets → Highlights variability and CatBoost's consistent high sensitivity.
  - Figure 2: Percentage of firms failing under Article 141 from 2015 to 2022 → Shows the yearly proportion of failed firms in the dataset.
  - Figure 3: Feature importance across models → Indicates X1 as the most influential feature for most algorithms.
key_equations:
  - equation: "Sensitivity = TP / (TP + FN)"
    explanation: "Measures the model's ability to identify actual failures."
  - equation: "Precision = TP / (TP + FP)"
    explanation: "Measures accuracy of positive predictions for failures."
  - equation: "F1Score = (2 * Precision * Sensitivity) / (Precision + Sensitivity)"
    explanation: "Harmonic mean balancing precision and sensitivity."
  - equation: "X2_F = 12 / (nk(k+1)) * sum(R_i^2) - 3n(k+1)"
    explanation: "Friedman statistic for comparing multiple model performances."
definitions:
  - term: Business Failure
    definition: "A firm facing significant operational challenges, broader than default or bankruptcy."
  - term: CorrOV-CSEn
    definition: "Correlation-based Oversampling aided Cost-Sensitive Ensemble learning technique."
  - term: Sensitivity
    definition: "True positive rate, measuring success in identifying failing firms."
  - term: Precision
    definition: "Proportion of predicted failures that are actual failures."
  - term: Article 141
    definition: "Iranian regulation requiring recovery plans for companies with losses exceeding equity."
critical_citations:
  - "[Barboza et al., 2017] — Comprehensive baseline for ML in bankruptcy prediction."
  - "[Devi et al., 2022] — Introduced the CorrOV-CSEn method used in this study."
  - "[Breiman, 2001] — Foundational work for the Random Forest algorithm."
  - "[Chen & Guestrin, 2016] — Foundational work for the XGBoost algorithm."
  - "[Friedman, 1937] — Provides the statistical test for model comparison."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: "Provides examples of ML models used for credit risk in capital markets."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: "Classifies firms into 'failed' and 'healthy', analogous to financial behavior profiling."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: "Demonstrates the application of predictive models (ML) for financial risk."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: "Directly models the detection of failing (anomalous) firms using cost-sensitive learning."
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: "Evaluates multiple ML algorithms (XGBoost, Random Forest, CatBoost) specifically for detecting rare failure events."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: "Uses sensitivity, precision, F1-score, and the Friedman–Nemenyi test for a rigorous model comparison."
  contribution: "This paper justifies Odin's use of cost-sensitive learning algorithms for anomaly detection (8.B) by demonstrating their effectiveness in identifying rare financial distress events. It provides a comparative framework (12.A) for evaluating such algorithms using metrics like sensitivity and precision. The study's focus on detecting 'business failure' directly supports Odin's core functionality of identifying anomalous spending patterns. Furthermore, its emphasis on high sensitivity over raw accuracy validates the design goal of prioritizing the detection of financially risky behavior in users. The findings also highlight the critical trade-off between sensitivity and precision, informing Odin's algorithm selection and performance-tuning strategies."
  directly_justifies:
    - "Cost-sensitive learning is necessary to effectively detect rare but costly financial anomalies in imbalanced datasets."
    - "CatBoost can achieve superior sensitivity in detecting failure cases, making it suitable for anomaly detection modules."
    - "Feature importance analysis can identify the most predictive variables for financial risk assessment."
    - "There is a significant performance trade-off between sensitivity and precision in anomaly detection models."
  limits:
    - "The study focuses on corporate business failure, not individual spending behavior, limiting direct applicability to PFMS."
    - "Precision was notably low for high-sensitivity models like CatBoost, suggesting a high false-positive rate."
    - "The findings are based on the Iranian capital market, which has unique political and economic conditions, limiting generalizability."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domain of 'Anomaly Detection' (8.A, 8.B) was flagged as highly relevant because the core task of the paper is identifying failing firms, which is analogous to detecting anomalies in a financial system. The 'Existing Systems & Gaps' (4.A) domain was considered contextual as the paper provides a landscape of ML models in finance. The 'Behavioral Profiling' (5.A) domain was assigned medium relevance because the binary classification of firms parallels profiling user financial behavior. 'Predictive Modeling' (6.A) was also medium for the same reason. The 'System Evaluation' (12.A) domain was deemed medium due to its detailed performance comparison framework. Topics related to Filipino cultural context (2.A-D), expense categorization (3.A-C), and others like mobile-first design (9.A-B) were rejected as they are not addressed. The paper is highly relevant for its contributions to algorithmic approaches for anomaly detection and the quantitative evaluation of such methods."
limitations:
  - "Data is from a single country's capital market, limiting generalizability to individual PFMS users."
  - "Precision was very low for CatBoost, which is a significant limitation for practical use."
  - "The paper does not account for the potential impact of the COVID-19 pandemic on the dataset."
  - "Models were not optimized with hyperparameter tuning (e.g., grid search). [unacknowledged]"
  - "The study uses 'business failure' under Article 141, not actual default, which may not perfectly reflect financial distress. [unacknowledged]"
remember_this:
  - "Cost-sensitive learning is critical for detecting rare financial anomalies."
  - "CatBoost achieved 90.9% sensitivity but at only 20.1% precision."
  - "A trade-off exists between maximizing detection and minimizing false alarms."
  - "Feature X1 was the most important predictor across all models."
  - "SMOTE improved precision but often reduced sensitivity compared to CorrOV-CSEn."
```