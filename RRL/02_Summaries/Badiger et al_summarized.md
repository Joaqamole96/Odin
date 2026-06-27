```yaml
paper_id: 10.17148/IJARCCE.2025.14364
designation: international-algorithm-specific
title: Next.js-Powered AI Platform for Smart Expense Tracking, Budgeting and Insights
authors: Badiger, R.; Robin, R.; Moraas, T.; Naik, V. G.; Karthikeyan A N, P.
year: 2025
venue: International Journal of Advanced Research in Computer and Communication Engineering
odin_topics:
  - 3.A
  - 4.A
  - 4.B
  - 6.A
  - 8.A
  - 12.A
tldr: An AI-powered personal finance platform integrating machine learning categorization, large language model insights, and time-series forecasting within a Next.js full-stack architecture.
problem_and_motivation: Existing personal finance tools lack automated real-time categorization, personalized natural-language insights, and predictive budgeting capabilities. This gap is particularly acute for users navigating multi-channel digital payment ecosystems, leading to poor financial decision-making.
approach:
  - The system is built on Next.js 14, Prisma ORM, Supabase PostgreSQL, and Clerk authentication.
  - Automated transaction categorization uses an XGBoost classifier trained on labelled transaction data.
  - Natural-language financial insights are generated using Google's Gemini LLM with a RAG pattern.
  - Expense forecasting is implemented using Meta's Prophet time-series model per spending category.
  - The platform supports multi-modal data ingestion including manual entry, CSV import, and receipt scanning.
  - Evaluation was performed on a held-out test set of 4,200 transactions from anonymized datasets.
findings:
  - "num: The XGBoost categorization model achieves a weighted F1-score of 0.913 across 18 spending categories."
  - "num: Server response times average 420ms for dashboard loads, with AI insight generation adding 800-1,400ms."
  - "num: The system reduces manual expense-logging effort by approximately 78% compared to conventional approaches."
  - Categories with high linguistic diversity show lower precision, while frequent categories achieve F1-scores above 0.95.
  - User feedback indicated that 84% of participants found the AI-generated insights useful for guiding financial decisions.
key_figures_tables:
  - "Figure 1: End-to-End User Workflow of Spend AI → visualizes the seven-stage process from authentication to budget alerts."
  - "Figure 2: Five-Layer System Architecture of Spend AI → illustrates the modular presentation, business, AI, data, and authentication layers."
  - "Figure 3: Technology Stack Overview → summarizes the complete technology stack from frontend to AI components."
  - "Figure 4: AI Insight Generation Pipeline (RAG Pattern) → shows the RAG-based prompt construction for the Gemini LLM."
  - "Figure 5: XGBoost Transaction Categorisation F1-Scores → displays per-category performance of the classification model."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "LLM"
    definition: "Large Language Model, used for natural-language insight generation."
  - term: "RAG"
    definition: "Retrieval-Augmented Generation, a pattern for grounding LLM responses in specific data."
  - term: "XGBoost"
    definition: "Extreme Gradient Boosting, a gradient-boosted tree classifier used for transaction categorization."
  - term: "UPI"
    definition: "Unified Payments Interface, India's real-time payment system."
  - term: "RLS"
    definition: "Row-Level Security, a database feature for enforcing per-user data isolation."
critical_citations:
  - "[Verma et al., 2024] — demonstrated Next.js viability but lacked AI categorization."
  - "[Kotios et al., 2022] — provided benchmarks for hybrid transaction classification."
  - "[Hean et al., 2025] — evaluated Gemini's capability for personal finance tasks."
  - "[Pancholi et al., 2026] — proposed multi-agent AI system for personal finance."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: "Implements an XGBoost model achieving 91.3% F1-score for transaction categorization."
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: "Reviews existing PFM systems and identifies gaps in automation and personalization."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: "Explicitly addresses limitations of prior systems and motivates the development of Spend AI."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: "Uses Prophet for time-series forecasting of monthly expenses by category."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: "Includes anomaly detection as a core feature, flagging transactions exceeding statistical thresholds."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: "Evaluates system performance through categorization accuracy and user experience feedback."
  contribution: "The paper's architecture for integrating ML categorization, LLM insights, and time-series forecasting directly informs Odin's design for the Categorization Engine, AI Insight Module, and Forecasting Module. Its use of a full-stack framework with row-level security provides a production-ready template for Odin's Mobile-First Design and Data Privacy & User Trust considerations. The experimental evaluation methodology offers a framework for evaluating Odin's algorithmic modules."
  directly_justifies:
    - "A gradient-boosted tree classifier can achieve over 91% accuracy for transaction categorization tasks."
    - "LLM-based insights grounded in user data via RAG can generate useful and validated financial guidance."
    - "Time-series forecasting with Prophet is feasible for personal spending prediction using limited historical data."
    - "Row-level security is a critical architectural property for systems handling sensitive financial data."
  limits:
    - "Categorization accuracy is lower for new users with fewer than 50 historical transactions (cold-start problem)."
    - "LLM hallucination risk remains, though mitigated by RAG-style prompting."
    - "Forecasting accuracy requires at least 3 months of historical data for reliable predictions."
    - "Data residency and regulatory compliance (e.g., DPDP Act) require further attention. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes flagged four domains as highly relevant: Expense Categorization (3.A), Existing Systems & Gaps (4.A, 4.B), Spending Forecasting (6.A), and Anomaly Detection (8.A). The paper's core contribution is algorithmic, justifying the 'algorithm-specific' designation, with direct implications for Odin's predictive and categorization modules. The System Evaluation domain (12.A) was considered relevant as the paper provides a performance evaluation framework. The Behavioral Profiling & Classification (5.A) domain was considered but rejected as the paper does not develop or utilize user financial profiles. The Savings & Debt Management domain (13.A, 13.B) was also considered but rejected as the paper's primary focus is on expense tracking and budgeting rather than savings or debt-specific features. Overall, the paper provides strong, directly applicable evidence for building an AI-powered PFMS, particularly its core algorithmic components."
limitations:
  - "LLM hallucination risk remains; critical recommendations should be verified."
  - "Manual data entry dependency persists in the absence of direct banking API integration."
  - "Data residency and regulatory compliance require further attention. [unacknowledged]"
  - "Forecasting accuracy requires at least 3 months of historical data for reliable predictions."
remember_this:
  - "XGBoost achieved 91.3% F1-score for transaction categorization across 18 categories."
  - "Platform reduces manual expense-logging effort by approximately 78%."
  - "84% of pilot users found Gemini-generated insights useful for financial decisions."
  - "System architecture separates presentation, business, AI, data, and authentication layers."
  - "RAG-based prompting grounds LLM insights in verifiable user data to reduce hallucination."
```