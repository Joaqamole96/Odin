```yaml
paper_id: 10.21608/IJTAR.2025.427658.1148
designation: international-algorithm-specific
title: An Intelligent Budget Management Mobile Application Based on a Recurrent Neural Network
authors: Ghonaim, W. A.; El-Sharawy, E. E.
year: 2025
venue: International Journal of Theoretical and Applied Research
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 9.A
  - 9.B
tldr: Develops a bilingual mobile budget app using an RNN to classify financial transaction risk, achieving 97.45% accuracy across low, medium, and high risk categories.
problem_and_motivation: Existing budgeting apps often lack Arabic language support and AI-based forecasting features. This paper addresses the gap by developing a mobile application that combines RNN-based risk prediction with a user-friendly interface for Arabic and English speakers.
approach:
  - Dataset of 1,048,576 financial transactions from Kaggle was used, split 70/15/15 for training, validation, and testing.
  - A bidirectional LSTM with two hidden layers (128 units each) and ReLU activation was implemented.
  - Risk labels (low/medium/high) were constructed using a scoring method based on income, debt, transaction frequency, and budget adherence.
  - The model was deployed via a Flask API with Firebase Firestore, integrating with a React Native mobile frontend.
  - Evaluation used precision, recall, F1-score, and accuracy, comparing predictions to actual risk levels.
findings:
  - num: 97.45% overall accuracy was achieved on the test set.
  - num: Precision, recall, and F1-score all exceeded 0.97 for each risk category.
  - The model demonstrated high reliability in detecting both low and high-risk financial behaviors.
  - The mobile application successfully integrated AI predictions with real-time user alerts.
  - Functional testing confirmed the stability and usability of the application for key features like registration and transaction entry.
key_figures_tables:
  - Table 2: Classification report showing precision, recall, and F1-score per risk level → All metrics exceed 0.97.
  - Table 3: Confusion matrix illustrating prediction alignment across risk categories → Strong diagonal values with minor overlaps in medium risk.
  - Figure 5: Report and Add Account interfaces → Visualizes the user workflow for managing financial accounts.
  - Figure 6: My Budget and Add Budget interfaces → Shows the interface for setting and managing budget categories.
key_equations:
  - equation: Precision = TP / (TP + FP)
    explanation: Measures the accuracy of positive predictions.
  - equation: Recall = TP / (TP + FN)
    explanation: Measures the ability to find all positive instances.
  - equation: F1 = 2 * (Precision * Recall) / (Precision + Recall)
    explanation: Harmonic mean of precision and recall.
definitions:
  - term: RNN
    definition: Recurrent Neural Network, a class of neural networks for sequential data.
  - term: LSTM
    definition: Long Short-Term Memory, an advanced RNN variant for long-term dependencies.
  - term: GRU
    definition: Gated Recurrent Unit, a simplified LSTM variant.
  - term: Firestore
    definition: Firebase's NoSQL cloud database for real-time data synchronization.
  - term: Flask
    definition: A Python microframework for building web APIs.
critical_citations:
  - "[Hochreiter & Schmidhuber, 1997] — Introduces LSTM architecture."
  - "[Cho et al., 2014] — Introduces GRU architecture."
  - "[Pascanu et al., 2013] — Discusses vanishing gradient problem in RNNs."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: App includes expense tracking and categorization.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: low
      justification: Mentions categories like necessities and discretionary spending.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Extensively reviews and compares existing budgeting applications.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies lack of Arabic support and AI features as key gaps.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses RNN to classify transactions into risk profiles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Core contribution is RNN-based risk prediction.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Applies RNN (LSTM) to sequential financial transaction data.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: App provides budgeting features and strategies.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Offers personalized financial plans and recommendations.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Risk prediction can alert users to potential financial issues.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Model detects high-risk spending patterns as anomalies.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Developed as a mobile-first application using React Native.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Designed over 27 interfaces with a focus on user experience.
  contribution: The paper provides a complete implementation of an RNN-based risk classifier that can be integrated into Odin's Anomaly Detection module to flag high-risk spending. The comparative analysis of existing apps informs Odin's competitive positioning and feature prioritization, particularly the need for AI-driven insights and multilingual support. The study's validation methodology, including precision, recall, and F1, offers a template for evaluating Odin's classification modules. The system's architecture combining Firebase, Flask, and React Native provides a blueprint for Odin's mobile-first, cloud-backed design. Finally, the user-centric features like real-time alerts and budget tracking directly justify similar components in Odin's Mobile UX and Budget Recommendation modules.
  directly_justifies:
    - Bilingual support and AI forecasting are critical gaps in existing PFMS apps.
    - RNNs can effectively classify financial risk from sequential transaction data.
    - 97.45% accuracy validates the reliability of deep learning for spending risk assessment.
    - Real-time budget alerts improve user financial awareness and decision-making.
  limits:
    - The risk labeling process was heuristic and may not generalize to all user contexts.
    - The study lacks longitudinal user studies to assess real-world impact on financial behavior.
    - No comparison with baseline or alternative ML models (e.g., GRU, XGBoost) for risk prediction.
  mapping_rationale: The paper was systematically scanned against all 12 functional domains and their associated topic codes. The "Expense Categorization" domain was flagged as medium relevance (3.A, 3.B) due to the app's transaction categorization. "Existing Systems & Gaps" was high relevance (4.A, 4.B) from the comprehensive literature review and comparative analysis. "Behavioral Profiling" was medium (5.C) via risk profile classification. "Spending Forecasting" was high (6.A, 6.B) due to the core RNN prediction task. "Budget Recommendation" was medium (7.A, 7.B) from the personalized planning features. "Anomaly Detection" was high (8.A, 8.B) through risk detection. "Mobile-First Design" was medium (9.A, 9.B) given the app's development focus. Domains like "Filipino Cultural Context" and "Savings & Debt Management" were considered but rejected as the paper is Egypt-based and does not address specific Filipino practices or advanced savings/debt features. The paper's primary relevance to Odin lies in its practical demonstration of AI-driven risk classification within a mobile PFMS context, offering a validated approach for the Forecasting and Anomaly Detection modules.
limitations:
  - Risk labels were artificially constructed from financial indicators, not verified against real-world financial distress outcomes. [unacknowledged]
  - The model was trained on fraud detection data, which may not fully represent general spending behavior for budget management. [unacknowledged]
  - No long-term user study was conducted to measure the app's actual impact on budgeting behavior or financial health.
remember_this:
  - The RNN model achieved 97.45% accuracy in classifying spending risk levels.
  - Arabic and English language support was a primary design requirement for the app.
  - The system provides real-time risk alerts based on transaction patterns.
  - The application architecture uses Firebase for backend and React Native for frontend.
  - Personal financial plans and recommendations are generated using AI predictions.
```