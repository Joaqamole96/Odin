```yaml
paper_id: 10.1016/j.mex.2026.103962
designation: international-algorithm-specific
title: Transforming financial documents into credit decisions using explainable artificial intelligence and optical character recognition
authors: Malave, S.; Khemani, B.; Patil, H.; Nandurkar, S.; Nandurkar, O.; Nayak, A.
year: 2026
venue: MethodsX
odin_topics:
  - "10.A"
  - "10.B"
tldr: A document-driven framework integrates OCR, XGBoost, and XAI (SHAP, LIME) for interpretable credit scoring, achieving high accuracy but with limited direct application to personal finance management.
problem_and_motivation: Automated credit scoring systems using complex models lack transparency, raising fairness and regulatory concerns. Existing methods also underutilize unstructured data from financial documents. A unified framework is needed to combine document intelligence, predictive accuracy, and explainability.
approach:
  - Extracts data from applicant documents (Aadhaar, PAN, salary slips, bank statements) using EasyOCR, PyPDF2, and PdfPlumber.
  - Converts extracted data into a structured JSON, performs cleaning, normalization, and cross-verification.
  - Engineers 15 financial and behavioural features (e.g., income stability, bounce count) from the extracted data.
  - Trains an XGBoost model on a public Kaggle dataset (10,000 instances) to predict a continuous credit score.
  - Employs SHAP for global feature importance and LIME for local, instance-specific explanations of predictions.
  - Integrates a rule-based decision layer for loan eligibility, interest rate, and amount, followed by a human-in-the-loop review.
findings:
  - "num: XGBoost achieved 92.5% accuracy, outperforming LightGBM (90.8%), Logistic Regression (91%), Random Forest (87%), and LSTM (81%)."
  - "num: XGBoost yielded the lowest MAE (13.71) and RMSE (18.87), indicating high prediction consistency."
  - SHAP analysis showed income stability and average monthly credit positively correlate with credit scores.
  - Bounce count and obligation-to-income ratio were identified as strong negative contributors to credit scores.
  - LIME provided consistent local explanations, highlighting feature impacts on individual predictions.
  - The integrated XAI approach enhances transparency and supports regulatory compliance.
key_figures_tables:
  - "Figure 1: Overview of the proposed end-to-end document-driven credit scoring framework. → Shows integration from document input to final decision."
  - "Table 2: Description of the 15 engineered features used for credit risk prediction. → Lists financial and behavioral attributes used as model input."
  - "Figure 8: Regression performance comparison across models based on MAE and RMSE. → XGBoost has the lowest error values."
  - "Figure 11: SHAP beeswarm plot showing global feature importance. → Visualizes positive and negative feature contributions."
key_equations:
  - equation: "AverageUsableSalary = (1/N) * Σ(Si - EMIi)"
    explanation: "Calculates disposable income after loan repayments."
  - equation: "Accuracy = (TP + TN) / (TP + TN + FP + FN)"
    explanation: "Proportion of correctly classified instances."
definitions:
  - term: "XAI"
    definition: "Explainable Artificial Intelligence."
  - term: "OCR"
    definition: "Optical Character Recognition."
  - term: "SHAP"
    definition: "SHapley Additive exPlanations."
  - term: "LIME"
    definition: "Local Interpretable Model-agnostic Explanations."
critical_citations:
  - "[Nwafor et al., 2024] — Proposes hybrid ML for credit decisions."
  - "[Nallakaruppan et al., 2024] — Reviews XAI for financial decision support."
  - "[Kozodoi et al., 2022] — Discusses fairness in credit scoring."
relevance:
  topics:
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "contextual"
      justification: "Paper mentions document deletion and role-based access but does not deeply analyze privacy in PFMS."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "medium"
      justification: "Provides a framework for transparent decision-making using SHAP and LIME, directly applicable to building user trust."
  contribution: "The paper's method for integrating data extraction and XAI can inform Odin's data handling module to build user trust through transparency. Its use of SHAP and LIME offers a blueprint for explaining complex financial predictions in a personal finance context. However, the focus on credit scoring for lenders means the framework is not directly transferable to Odin's core PFMS functions."
  directly_justifies:
    - "Combining explainable models with feature engineering improves transparency for users."
    - "XGBoost is a robust model for structured financial data, achieving high accuracy."
    - "SHAP and LIME can provide consistent global and local explanations of model predictions."
  limits:
    - "The study is specific to credit scoring and not personal finance management."
    - "The model is trained on a public dataset, not on real-world or Philippine-specific financial data."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated canonical topic codes was performed. The relevance is primarily contextual or medium. The domain 'Data Privacy & User Trust' was flagged as relevant, specifically topic 10.A (contextual) for its mention of data handling and 10.B (medium) for its strong focus on XAI to build trust. The papers on 'Existing Systems & Gaps' (4.A, 4.B) were considered but rejected as the paper proposes a new system, not an analysis of existing ones. Domains like 'Spending Forecasting', 'Budget Recommendation', and 'Anomaly Detection' were considered and rejected as the paper's scope is credit risk, not personal budgeting or spending analytics. The Filipino cultural domains (e.g., 2.A, 2.B) were considered and rejected due to the study's Indian context. Overall, the paper's contribution is tangentially relevant to Odin, primarily as a reference for implementing explainable AI to build user trust, rather than for its core PFMS functionalities."
limitations:
  - "Dependency on OCR accuracy, which varies with document quality and type. [unacknowledged]"
  - "Training on a structured dataset may not capture the full diversity of real-world financial data. [unacknowledged]"
  - "SHAP and LIME may not capture all complex model interactions. [unacknowledged]"
remember_this:
  - "XGBoost achieved 92.5% accuracy for credit scoring."
  - "SHAP and LIME provide global and local explanations for predictions."
  - "The framework integrates document data extraction with machine learning."
  - "Feature engineering is critical for translating raw data into predictive inputs."
  - "Explainability enhances transparency in financial decision-making systems."
```