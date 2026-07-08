```yaml
paper_id: 10.5281/zenodo.17074353
designation: international-algorithm-specific
title: Targeting Social Assistance Beneficiaries Using Machine Learning: A Poverty Probability-Based Approach
authors: Sahraoui, C.; Zari, T.
year: 2025
venue: International Journal of Accounting, Finance, Auditing, Management and Economics
odin_topics:
  - 4.A
  - 4.B
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 8.A
  - 10.A
  - 10.B
tldr: Machine learning models, particularly Random Forest, outperform traditional methods in targeting social assistance beneficiaries by reducing exclusion errors.
problem_and_motivation: Traditional social assistance targeting methods like categorical eligibility and proxy means testing often produce significant inclusion and exclusion errors. These approaches lack the flexibility to adapt to changing socio-economic conditions, highlighting a need for more precise and responsive mechanisms. This study addresses the gap by empirically evaluating machine learning models for enhancing targeting accuracy.
approach:
  - A synthetic dataset of 12,600 individuals with 59 socio-economic variables was used.
  - Three supervised learning models were compared: Logistic Regression, Random Forest, and XGBoost.
  - Categorical variables were one-hot encoded, and missing values were zero-imputed.
  - Models were evaluated using accuracy, precision, recall, F1-score, and ROC-AUC on an 80/20 train-test split.
  - Feature importance was analyzed to identify key predictors of poverty-based eligibility.
findings:
  - num: Random Forest achieved the highest accuracy of 0.778 and the strongest recall for eligible households at 0.886.
  - num: XGBoost showed improved recall for non-eligible households (0.611), reducing inclusion errors.
  - num: Logistic regression performed less well, with recall for eligible households at 0.863 and F1-scores lower than ensemble models.
  - num: Random Forest and XGBoost achieved AUC scores of 0.84 and 0.83, respectively, compared to 0.82 for logistic regression.
  - Education level, urban/rural residence, and access to digital and financial services emerged as the most significant predictors.
  - Ensemble methods were more effective at capturing the non-linear relationships characterizing poverty.
  - Access to financial and digital services showed strong predictive power, sometimes surpassing traditional demographic variables.
  - The study highlights the ethical need for transparency, bias reduction, and institutional accountability in algorithmic targeting.
key_figures_tables:
  - Table 1: Descriptive statistics for key predictors. Shows distribution of age, residence, gender, marital status, literacy, employment, financial inclusion, digital access, and education level.
  - Table 2: Model performance comparison. Shows Random Forest and XGBoost outperform logistic regression across all metrics, especially in recall for eligible households.
  - Figure 2: Top 10 features for Logistic Regression. Highlights country indicators and socio-demographic variables.
  - Figure 3: Top 10 features for Random Forest. Highlights age, education, urban status, and access to digital/financial services.
  - Figure 4: Top 10 features for XGBoost. Shows convergence on education, urban location, and financial/digital access as key predictors.
  - Figure 5: Correlation matrix of key predictors. Shows weak to moderate correlations, with strongest between financial inclusion and active bank use.
  - Figures 6-8: Confusion matrices. Show ensemble methods have fewer false negatives than logistic regression.
  - Figures 9-11: ROC curves. Show Random Forest has the highest AUC at 0.84.
key_equations:
  - equation: "Log(P(Y_i=1)/(1-P(Y_i=1))) = β_0 + β'X_i + ε_i"
    explanation: Specifies logistic regression for binary classification of poverty.
definitions:
  - term: PMT
    definition: Proxy Means Testing, a traditional targeting method using observable household attributes.
  - term: XAI
    definition: Explainable Artificial Intelligence, techniques to make model predictions transparent.
  - term: ROC-AUC
    definition: Area Under the Receiver Operating Characteristic Curve, a measure of model discrimination.
critical_citations:
  - "[Aiken et al., 2022] — ML on mobile data enhanced poverty targeting in Afghanistan."
  - "[Brown & Ravallion, 2020] — PMT leads to inclusion and exclusion errors in developing countries."
  - "[Athey, 2017] — ML outperforms traditional econometric tools for policy problems."
  - "[Wachter et al., 2017] — Highlights interpretability challenges in complex ML models."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides background on traditional targeting methods in social protection.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly documents inclusion/exclusion errors in PMT and categorical eligibility.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Compares machine learning classifiers for poverty prediction.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Empirically evaluates predictive models for eligibility classification.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: contextual
      justification: Uses tree-based and regression models, applicable to forecasting.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: low
      justification: Mentions trade-offs in classification thresholds, analogous to resource allocation.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Discusses error minimization, but not specifically anomaly detection.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Discusses privacy risks of using alternative data sources like mobile metadata.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Emphasizes transparency, accountability, and fairness as essential for user trust in algorithmic systems.
  contribution: The paper provides a framework for evaluating machine learning classifiers for beneficiary targeting, which can inform Odin's user profiling module. Its analysis of feature importance directly supports the design of Odin's expense categorization and behavioral profiling features by identifying key socio-economic indicators. The emphasis on reducing exclusion errors translates to Odin's goal of accurate spending forecasting and budget recommendation. The ethical discussion informs Odin's data privacy and user trust modules. Finally, the comparison of model performance offers a methodology for evaluating Odin's algorithmic modules.
  directly_justifies:
    - "Machine learning models can reduce exclusion errors in beneficiary targeting compared to traditional methods."
    - "Education level, urban residence, and digital access are strong predictors of socio-economic vulnerability."
    - "Tree-based ensemble models like Random Forest offer a better balance of accuracy and sensitivity than logistic regression."
    - "Transparency and bias reduction are essential for legitimizing algorithmic integration in social systems."
  limits:
    - "Use of a synthetic dataset, which may not fully capture the complexity of real-world administrative data."
    - "Models were trained with default hyperparameters without cross-validation, limiting robustness assessment."
    - "Feature importance analysis did not employ advanced explainability tools like SHAP to detail variable interactions."
    - "Ethical considerations were addressed conceptually but not empirically assessed through stakeholder consultation."
  mapping_rationale: A systematic scan of all 12 functional domains and their canonical topic codes was performed. The paper was flagged as relevant to the 'Existing Systems & Gaps' (4.A, 4.B) domain with high relevance for identifying limitations of PMT. For 'Behavioral Profiling & Classification' (5.C), it received medium relevance for its comparison of classifiers. High relevance was assigned to 'Spending Forecasting' (6.A) due to its empirical evaluation of predictive models, and 'Data Privacy & User Trust' (10.B) for its strong focus on transparency and accountability. Contextual relevance was noted for 'Budget Recommendation' (7.A) and 'Anomaly Detection' (8.A) due to the discussion of classification thresholds and error minimization. Topics related to Filipino cultural context (1.A-1.C, 2.A-2.D), expense categorization (3.A-3.C), and retention (11.A-11.B) were considered but rejected as the paper's scope is broader and does not address these specific areas. The paper's overall relevance lies in providing a methodological and ethical framework for integrating predictive algorithms into social systems, which directly informs Odin's design for accurate and trustworthy financial management.
limitations:
  - "Use of a synthetic dataset may limit generalizability to real-world applications. [unacknowledged]"
  - "Default hyperparameters and a simple train/test split were used without cross-validation. [unacknowledged]"
  - "Advanced explainability techniques were not applied to interpret feature interactions."
  - "Ethical and fairness concerns were not empirically validated through stakeholder engagement. [unacknowledged]"
remember_this:
  - Random Forest achieved the highest accuracy at 0.778 for poverty classification.
  - Tree-based models are better at reducing exclusion errors than logistic regression.
  - Education and digital access are key predictors of poverty vulnerability.
  - Transparency is crucial for legitimizing algorithms in social protection.
  - The study confirms the multidimensional nature of poverty beyond monetary criteria.
```