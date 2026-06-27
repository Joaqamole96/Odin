```yaml
paper_id: 549d7af6-15d6-5c3f-b483-6c0f6de1b738
designation: international-algorithm-specific
title: PERSONAL FINANCE TRACKER WITH AI BASED EXPENSE PREDICTION
authors: Chandana, M.; Reddy, E. M.; Reddy, E. P.; Vaishnavi, I. S.; Vaishnavi, K.
year: 2026
venue: AMERICAN JOURNAL OF MANAGEMENT AND IOT MEDICAL COMPUTING
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 9.A
  - 9.B
  - 12.A
  - 12.B
tldr: An AI-powered finance tracker using Flask, MySQL, Random Forest, and LSTM to forecast expenses, detect anomalies, and automatically categorize transactions for enhanced user financial awareness.
problem_and_motivation: Existing expense trackers passively record data without providing predictive insights or personalized budgeting guidance. Users need intelligent systems that analyze behavioral patterns to offer actionable financial foresight. This project addresses the gap between simple tracking and proactive financial management.
approach:
  - The system is built with Python and Flask for the backend, MySQL for data storage, and a frontend using HTML, CSS, and JavaScript with Chart.js.
  - Historical transaction data is preprocessed to remove nulls, encode categorical features, and normalize numerical values for model input.
  - A Random Forest classifier is used to automatically categorize transactions into predefined groups such as food, travel, and bills.
  - An LSTM neural network is applied for time-series forecasting to predict future monthly expenses based on past spending behavior.
  - Anomaly detection algorithms analyze spending trends to identify unusual patterns or sudden spikes in expenditure.
  - A real-time dashboard visualizes income, expense distribution, and predictions through charts and graphs to improve user understanding.
  - User authentication and session management secure access and isolate individual financial data within the MySQL database.
  - The system was tested on both sample and real transaction datasets to evaluate the performance of its core modules.
findings:
  - The LSTM model achieved approximately 85% accuracy in forecasting next-month expenses.
  - The Random Forest classifier achieved over 90% accuracy in automatically categorizing financial transactions.
  - The anomaly detection module successfully identified sudden spending spikes and irregular transactions with good accuracy.
  - Users found the dashboard interface easy to understand and the visual insights improved their financial awareness.
  - Predicted values from the LSTM model closely matched actual spending patterns for most categories.
  - The system proved more effective than manual or static trackers by providing accurate predictions and helpful alerts for unusual expenses.
key_figures_tables:
  - Figure 1: System architecture overview of the AI-powered tracker → Shows the integration of modules with LSTM and Random Forest.
  - Figure 2: Flask-based ML dashboard flow → Illustrates the technical workflow from user input to insights and storage.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network used for time-series forecasting in this system.
  - term: AI
    definition: Artificial Intelligence, used for predictive analysis and automation in the finance tracker.
critical_citations:
  - "[Kaur and Singh, 2022] — AI-based expense prediction using ML."
  - "[Patel and Sinha, 2021] — Random Forest and LSTM for expenditure analysis."
  - "[Bhattacharya, 2023] — Automated finance tracking with data analytics."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Implements Random Forest for automated expense classification.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: Uses predefined categories (food, travel) and visualizes them.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Reviews limitations of traditional static trackers as a baseline.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly addresses the lack of predictive and analytical features in existing systems.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Core contribution is forecasting future expenses using LSTM.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Uses LSTM specifically for time-series expense prediction.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Includes a module to identify unusual spending patterns and generate alerts.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Mentions anomaly detection techniques but provides limited algorithmic detail.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: contextual
      justification: The web-based system could inform mobile-first design but is not the focus.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: Mentions an intuitive dashboard but focuses on web, not mobile UX specifically.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Presents accuracy results and user-friendliness evaluations.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides quantitative accuracy metrics for both classification and prediction modules.
  contribution: The paper provides a practical implementation of a predictive finance tracker, demonstrating how LSTM and Random Forest can be integrated into a web application. It justifies the use of these algorithms for Odin's expense prediction (6.A, 6.B) and categorization modules (3.A). Its evaluation framework (12.A, 12.B) offers a template for testing similar modules, while its anomaly detection component (8.A, 8.B) validates the need for proactive spending alerts.
  directly_justifies:
    - The LSTM model achieves 85% accuracy in forecasting monthly expenses.
    - The Random Forest classifier attains over 90% accuracy in automated transaction categorization.
    - Anomaly detection can effectively identify sudden spending spikes for user alerts.
    - Users respond positively to dashboards that present predictive and categorized financial insights.
  limits:
    - The dataset used for testing is not clearly described, making reproducibility difficult. [unacknowledged]
    - Lack of comparison against a robust set of baseline or state-of-the-art models. [unacknowledged]
    - No explicit discussion of privacy-preserving techniques for handling sensitive financial data. [unacknowledged]
    - The system is a web application, and no discussion is provided on how its design translates to a mobile-first experience. [unacknowledged]
  mapping_rationale: A systematic scan was conducted across all 12 functional domains for this paper. The domain of 'Expense Categorization' was flagged as highly relevant (3.A, 3.B) due to the Random Forest classifier. 'Spending Forecasting' was also high (6.A, 6.B) given the LSTM model. 'Anomaly Detection' (8.A, 8.B) was relevant due to the dedicated module. 'Existing Systems & Gaps' (4.A, 4.B) was identified as contextual/high as the motivation explicitly critiques traditional systems. 'System Evaluation' (12.A, 12.B) was medium/high due to reported accuracy metrics. The 'Mobile-First Design' domain (9.A, 9.B) was considered but rejected to low/contextual as the work is web-focused and does not address mobile-specific challenges. 'Data Privacy' and 'User Retention' were considered and rejected as they are not discussed. The paper's overall relevance to Odin is moderate, as it validates the technical feasibility and impact of predictive and categorical modules, which are core components of the system.
limitations:
  - The paper does not specify the size or source of the dataset used for validation. [unacknowledged]
  - No comparison is made with other forecasting models like XGBoost or Transformer-based networks. [unacknowledged]
  - The anomaly detection method lacks algorithmic detail, making its performance difficult to assess. [unacknowledged]
  - The evaluation focuses on accuracy and usability but does not test the system's performance under varying data distributions. [unacknowledged]
remember_this:
  - LSTM achieved 85% accuracy in forecasting monthly expenses.
  - Random Forest automatically categorized transactions with over 90% accuracy.
  - Anomaly detection provided effective early warnings for unusual spending.
  - The system transformed a passive tracker into an intelligent predictive assistant.
  - The dashboard improved user financial awareness through clear visualizations.
```