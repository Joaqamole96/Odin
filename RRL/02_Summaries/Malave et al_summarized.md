```yaml
paper_id: 2c8a9b4e-1e5d-5a2f-9b3c-8d7e6f5a4b3c
designation: international-algorithm-specific
title: Transforming financial documents into credit decisions using explainable artificial intelligence and optical character recognition
authors: Malave, S.; Khemani, B.; Patil, H.; Nandurkar, S.; Nandurkar, O.; Nayak, A.
year: 2026
venue: MethodsX
odin_topics:
  - 4.A
  - 4.B
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
tldr: An XAI framework integrates OCR and XGBoost to automate credit scoring, achieving 92.5% accuracy while providing SHAP and LIME explanations for transparency.
problem_and_motivation: Existing credit scoring models either lack interpretability or fail to utilize unstructured document data. A unified system is needed that extracts financial features from documents and provides explainable predictions to ensure fairness and regulatory compliance.
approach:
  - Documents are processed using EasyOCR, PyPDF2, and PdfPlumber to extract identity and financial data.
  - Extracted data is cleaned, normalized, and transformed into 15 engineered financial features.
  - XGBoost predicts credit scores, outperforming LightGBM, Random Forest, Logistic Regression, and LSTM.
  - SHAP provides global and local feature importance explanations for model predictions.
  - LIME generates instance-specific explanations to support transparent decision-making.
  - A human-in-the-loop review allows loan officers to validate features, predictions, and explanations before final decisions.
findings:
  - XGBoost achieved the lowest MAE of 13.71 and RMSE of 18.87, indicating high prediction consistency.
  - num: XGBoost attained a classification accuracy of 92.5% at the decision threshold of 650.
  - num: XGBoost achieved precision of 0.938, recall of 0.945, and F1-score of 0.942, outperforming all baselines.
  - SHAP analysis identified income stability, average balance, and monthly credit as top positive contributors to credit scores.
  - LIME explanations matched SHAP results, confirming consistent local and global interpretability.
  - The framework addresses the gap of integrating document intelligence with explainable machine learning for credit scoring.
key_figures_tables:
  - Figure 1: Flowchart of the proposed end-to-end framework → visualizes the complete pipeline from document ingestion to final output.
  - Table 1: Document types and extracted fields → details the specific data extracted from Aadhaar, PAN, salary slips, and bank statements.
  - Table 2: Feature description → lists all 15 engineered features used for credit risk prediction.
  - Figure 6: Correlation matrix of engineered features → shows relationships between financial attributes and their influence on credit score.
  - Figure 11: SHAP beeswarm plot for global feature importance → illustrates feature contributions across all instances.
  - Figure 12: LIME-based local explanation → demonstrates instance-specific feature contributions for an individual prediction.
key_equations:
  - equation: "AverageMonthlyCredit = (1/N) * sum(C_i)"
    explanation: "Mean of credited amounts over N months."
  - equation: "AverageUsableSalary = (1/N) * sum(S_i - EMI_i)"
    explanation: "Average income left after EMI payments."
  - equation: "AverageEligibleEMI = 0.4 * AverageUsableSalary"
    explanation: "Maximum EMI capacity set at 40% of usable salary."
  - equation: "EMI = P * r * ((1+r)^n) / ((1+r)^n - 1)"
    explanation: "Calculates monthly installment for a loan."
definitions:
  - term: XAI
    definition: "Explainable Artificial Intelligence, methods that make AI model decisions transparent."
  - term: OCR
    definition: "Optical Character Recognition, technology to extract text from images and documents."
  - term: XGBoost
    definition: "Extreme Gradient Boosting, a tree-based ensemble machine learning algorithm."
  - term: SHAP
    definition: "SHapley Additive exPlanations, a game-theoretic approach for explaining model outputs."
  - term: LIME
    definition: "Local Interpretable Model-agnostic Explanations, a method for explaining individual predictions."
critical_citations:
  - "[Nwafor et al., 2024] — Proposes a hybrid ML approach for transparent credit decisions."
  - "[Nallakaruppan et al., 2024] — Reviews XAI for credit risk and financial decision support."
  - "[De Lange et al., 2022] — Discusses XAI for credit assessment in banking."
  - "[Chang et al., 2025] — Presents an explainable ML study for credit worthiness prediction."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: "Reviews existing credit scoring systems and their limitations."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: "Explicitly addresses the lack of integration between document data and explainable ML."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: "Proposes XGBoost for credit score prediction, relevant to forecasting."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: "Uses aggregated financial features for prediction, not sequential data directly."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: "Features like bounce_count and gambling_transaction_count are related to anomaly detection."
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: "Mentions features indicative of anomalies but does not focus on detection algorithms."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: "Mentions role-based authentication, audit trails, and document deletion for privacy."
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: "Focuses on transparency via SHAP/LIME to build trust and support regulatory compliance."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: "Provides a comprehensive evaluation using MAE, RMSE, R2, Accuracy, Precision, Recall, F1."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: "Compares XGBoost against LGBM, RF, LR, and LSTM using standard regression metrics."
  contribution: "The paper contributes to Odin's XAI module by demonstrating how SHAP and LIME can explain predictions of a tree-based ensemble. It supports the feature engineering pipeline (3.B) by validating that derived financial features (e.g., income stability, obligation-to-income ratio) are predictive and interpretable. The human-in-the-loop review aligns with Odin's need for user trust and explainability (10.B). The evaluation methodology (12.A, 12.B, 12.C) provides a template for assessing Odin's own predictive modules. The work directly justifies the use of XGBoost for structured financial data and the application of SHAP/LIME for transparency."
  directly_justifies:
    - "XGBoost achieves superior performance (92.5% accuracy) for credit scoring on structured financial features."
    - "SHAP and LIME provide consistent global and local explanations for tree-based ensemble models."
    - "Combining document-based feature extraction with explainable ML enhances transparency and regulatory compliance."
    - "Derived financial features like income stability and obligation-to-income ratio are strong predictors of financial risk."
  limits:
    - "Dependency on OCR accuracy, which may vary with document quality and noise."
    - "Trained on a structured dataset that may not cover all variations of real-world financial data."
    - "SHAP and LIME may not capture all possible model interactions, limiting deeper explanation."
  mapping_rationale: "A systematic scan of all 12 functional domains was conducted. The paper was flagged as most relevant to 'Existing Systems & Gaps' (4.A, 4.B) due to its explicit focus on limitations of current credit scoring models, and to 'Data Privacy & User Trust' (10.A, 10.B) through its emphasis on XAI for transparency. High relevance was also assigned to 'System Evaluation' (12.A, 12.B) given the detailed model comparison and metrics. Medium relevance was assigned to 'Spending Forecasting' (6.A, 6.B) as it uses aggregated financial features, and 'Anomaly Detection' (8.A, 8.B) due to risk-related features like bounce_count. The domains of 'Filipino Cultural Context' (2.A-D), 'Behavioral Profiling' (5.A-C), 'Budget Recommendation' (7.A-D), 'Mobile-First Design' (9.A-B), and 'Savings & Debt Management' (13.A-C) were considered but rejected as the paper does not address these topics. Overall, the paper provides strong support for Odin's predictive modeling, explainability, and evaluation modules."
limitations:
  - "Dependency on OCR accuracy, which may vary with document quality and noise."
  - "Trained on a structured dataset that may not cover all variations of real-world financial data."
  - "SHAP and LIME may not capture all possible model interactions, limiting deeper explanation."
remember_this:
  - "XGBoost achieved 92.5% accuracy for credit risk classification."
  - "SHAP and LIME provide consistent explanations for financial predictions."
  - "Integrating document OCR with ML improves data utilization."
  - "Human-in-the-loop review ensures accountability and compliance."
  - "Feature engineering transforms documents into 15 predictive financial attributes."
```