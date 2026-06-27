```yaml
paper_id: 10.1555/ijarp.6353
designation: international-algorithm-specific
title: AI-BASED REAL-TIME PERSONAL FINANCE DASHBOARD
authors: Unde, S. P.; Ghule, A. B.; Jaware, R. S.; Kanawade, S. N.; Koli, Y. K.
year: 2026
venue: International Journal Advanced Research Publication
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.B
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 9.A
  - 9.B
  - 10.A
  - 11.A
  - 12.A
  - 12.B
  - 12.C
tldr: An AI-driven dashboard integrates real-time data ingestion, BERT-based categorization, and autoencoder anomaly detection to automate personal finance management and provide predictive insights.
problem_and_motivation: Digital payment proliferation fragments financial data across platforms, while manual tracking tools are time-consuming and error-prone. Existing systems lack real-time, proactive intelligence for automated categorization, anomaly detection, and forecasting. An integrated, automated dashboard is needed to unify data and enable intelligent financial oversight.
approach:
  - Data is ingested via banking APIs, webhooks, and an OCR module using CNNs (YOLOv4) for receipt digitization.
  - A preprocessing pipeline cleans data, normalizes features, and applies NLP tokenization to transaction descriptions.
  - A fine-tuned BERT model is used for automated expense categorization into domains like utilities and groceries.
  - A dual anomaly detection engine uses Isolation Forests and Conditional Autoencoders to flag point and contextual outliers.
  - LSTM networks forecast cash flows, and linear programming or LLM optimization generates dynamic savings recommendations.
findings:
  - num: Fine-tuned BERT model achieves 90-95% categorization accuracy, outperforming traditional keyword-based systems.
  - num: The system reduces manual data entry effort by over 80% through automated API and OCR integration.
  - Conditional Autoencoders successfully identify contextual outliers (e.g., duplicate subscriptions) with a low false-positive rate.
  - LSTM-based forecasts provide superior predictive accuracy for future savings trajectories and cash flows.
  - Users of the AI dashboard exhibit more disciplined spending habits due to automated alerts and real-time goal progress visualization.
key_figures_tables:
  - Figure 1: System architecture diagram illustrating four-layer pipeline → Overview of data flow from ingestion to presentation.
  - Figure 2: Project plan timeline → Visual representation of development phases and milestones.
  - Table 1: Performance comparison between traditional systems and proposed dashboard → Proposed AI dashboard metrics show higher accuracy, lower effort, and proactive functionality.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: API
    definition: Application Programming Interface, used for secure data ingestion from financial institutions.
  - term: BERT
    definition: Bidirectional Encoder Representations from Transformers, a deep learning model for natural language understanding.
  - term: CNN
    definition: Convolutional Neural Network, used for image feature extraction in OCR.
  - term: LSTM
    definition: Long Short-Term Memory network, a recurrent neural network for time-series forecasting.
  - term: NLP
    definition: Natural Language Processing, used for processing transaction text descriptions.
  - term: OCR
    definition: Optical Character Recognition, technology for digitizing text from physical receipts.
  - term: UPI
    definition: Unified Payments Interface, a real-time payment system in India.
critical_citations:
  - "[Patil and Jadhav, 2025] — Hybrid ML for automated expense classification."
  - "[Kharat, 2025] — Validates BERT for categorization and LSTM for forecasting."
  - "[Inzirillo and De Villelongue, 2023] — Autoencoder for anomaly detection."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Directly proposes BERT-based automated categorization of transactions.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: high
      justification: Discusses categorization into domains like utilities and groceries for dashboard design.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews existing systems and their limitations (manual tracking, fragmentation).
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies gaps like lack of real-time insights and intelligent automation.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: low
      justification: Touch on user behavior and spending habits, but does not address cold-start.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Uses LSTM for predictive cash flow forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: LSTM specifically chosen for sequential spending data forecasting.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Discusses budget monitoring and goal-based savings automation.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: LLM/linear programming for optimizing savings and adjusting spending limits.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Proactive anomaly detection is a core feature.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Implements Isolation Forest and Conditional Autoencoders for this purpose.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: Mentions a web interface but does not focus on mobile-first principles.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: Lacks detailed discussion on mobile UX design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Addresses secure API data flow and integrity, but not extensively.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Automated alerts and visualization foster engagement and awareness.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides a comparative analysis between traditional and proposed systems.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Evaluates categorization accuracy and anomaly detection performance.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Evaluates budget management and savings adherence improvements.
  contribution: This paper directly justifies Odin's core modules by demonstrating the effectiveness of a unified, automated dashboard. The BERT-based categorization validates Odin's expense classification approach. The dual autoencoder/Isolation Forest anomaly detection engine supports Odin's proactive security layer. The LSTM forecasting and LLM-optimized savings modules align with Odin's predictive budgeting and recommendation features. Overall, the proposed architecture provides a blueprint for Odin's integrated, real-time financial management system.
  directly_justifies:
    - Automated expense categorization using BERT can achieve over 90% accuracy.
    - Conditional Autoencoders are effective for detecting contextual outliers in spending data.
    - LSTM networks provide superior accuracy for forecasting future cash flows.
    - Reducing manual data entry by over 80% significantly improves user engagement.
    - An AI-driven dashboard can directly improve savings adherence through automated alerts.
  limits:
    - The performance of the OCR module is dependent on receipt image quality.
    - Accuracy of categorization is reliant on the consistency of bank API data.
    - The study does not address the cold-start problem for new users with no historical data.
  mapping_rationale: A systematic scan across all 12 functional domains was executed. The paper was flagged as highly relevant for Expense Categorization (3.A, 3.B), Existing Systems (4.B), Predictive Modeling (6.A, 6.B), Budget Recommendation (7.B), and Anomaly Detection (8.A, 8.B) due to its direct proposal of BERT, LSTM, and autoencoder-based solutions. Medium relevance was assigned to domains like Landscape (4.A), Engagement (11.A), and Evaluation (12.A, 12.B, 12.C) for its review context and comparative analysis. Topics like Filipino Cultural Context (2.A-D) and Mobile-First Design (9.A, 9.B) were considered but rejected as the paper is geographically unbound and focuses on a general web interface rather than mobile-specific UX. The paper's overall relevance to Odin is high as it provides empirical evidence for several core algorithmic modules, though it is from a general international context.
limitations:
  - Performance depends on receipt image quality and API data consistency. [unacknowledged]
  - Does not address the cold-start problem for new users.
remember_this:
  - BERT-based categorization achieves 90-95% accuracy.
  - The system reduces manual effort by over 80%.
  - Conditional Autoencoders detect contextual outliers effectively.
  - LSTM forecasting enables dynamic budget adjustments.
  - An AI dashboard promotes disciplined spending through automation.
```