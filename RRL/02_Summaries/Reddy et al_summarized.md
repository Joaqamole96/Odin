```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international
title: AI-Powered Financial Insights Platform
authors: Reddy, S. T.; Soniya, C.; Thanushree, G.; Darshan, B. G.; Gupta, S.
year: 2024
venue: Unknown
odin_topics:
  - 3.A
  - 4.A
  - 4.B
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 11.A
  - 12.A
  - 12.B
tldr: Develops an AI-powered personal finance platform integrating a conversational advisor, receipt scanner, portfolio tracker, EMI manager, and dashboard to unify financial management.
problem_and_motivation: Individuals in India lack access to personalized, affordable financial advisory services despite widespread digital banking adoption. Existing commercial solutions fail to offer comprehensive, unified platforms that combine budgeting, investment, EMI tracking, and tax planning. This absence of a single, intelligent system leaves users without context-aware guidance tailored to their actual financial data.
approach:
  - Builds a full-stack web application using Next.js 15, React 18, and Tailwind CSS with a serverless architecture.
  - Implements a conversational AI advisor "CA Arjun" using Groq's LLAMA 3.1 (8B for intent, 70B for investments) with user financial context injection.
  - Integrates an automated receipt scanner using Google Gemini 1.5 Flash for multimodal OCR extraction of transaction details.
  - Develops a live portfolio tracker pulling real-time stock and mutual fund data from Yahoo Finance and MFAPI.in APIs.
  - Creates an EMI calculator and tracker with server-side amortization schedule generation stored in PostgreSQL via Prisma.
  - Designs a comprehensive analytics dashboard with interactive charts using Recharts and a CA-generated financial health report.
  - Employs a dedicated LSTM prediction microservice (FastAPI/TensorFlow) for forecasting spending and cash flow trajectories.
findings:
  - num: Dashboard initial load achieves approximately 420ms to first meaningful content using SSR with Suspense.
  - num: CA Report generation with parallel database fetches and Groq inference averages approximately 1.8 seconds.
  - num: Investment recommendations using the LLAMA 3.1 70B model average a response time of approximately 3.2 seconds.
  - num: Receipt scanning with Gemini 1.5 Flash averages approximately 2.1 seconds and achieves over 92% accuracy.
  - num: Live portfolio fetch for 10 holdings executes in approximately 1.4 seconds using parallel API calls.
  - num: Creation of a 60-month EMI schedule requires a database round-trip time of approximately 180ms.
  - The system successfully handles blurry or non-receipt images with graceful error fallbacks.
  - The platform demonstrates architectural resilience by gracefully handling offline LSTM services and missing API keys.
  - The platform consolidates budgeting, investment tracking, EMI management, and tax planning into a single application.
key_figures_tables:
  - Figure 1: Operational workflow showing the four layers (User, Blockchain Data Access, Backend & AI Reasoning, Masumi Verification) → Visualizes the end-to-end data and verification flow.
  - Table: Database schema diagram showing central User model with cascading relations to Accounts, Transactions, Budgets, Goals, Loans, and Holdings → Defines the core relational data structure.
  - Visual: DashboardCharts component with "6M Trend", "Categories", and "Daily" tabs → Showcases the multi-dimensional financial charting capabilities.
  - Diagram: Future Smart Automated Financial Ecosystem with Inngest workers for proactive alerts → Illustrates planned extension for automated monitoring and notifications.
key_equations:
  - equation: EMI = P × r × (1+r)^n / ((1+r)^n - 1)
    explanation: Standard reducing-balance formula for monthly EMI calculation.
definitions:
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network architecture for time-series forecasting.
  - term: NLG
    definition: Natural Language Generation, translating structured data into human-readable summaries.
  - term: RAG
    definition: Retrieval-Augmented Generation, enhancing LLM responses with retrieved external knowledge.
  - term: OCR
    definition: Optical Character Recognition, extracting text from images.
  - term: JWT
    definition: JSON Web Token, a compact standard for secure information transmission.
critical_citations:
  - "[Chen et al., 2023] — Demonstrates LLM-based financial advisory accuracy with RAG/prompt engineering."
  - "[Reddy et al., 2022] — Shows OCR for receipt processing using multimodal transformers exceeds 92% accuracy."
  - "[Zhang et al., 2021] — Validates LSTM-based time-series forecasting for personal finance applications."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Uses predefined enum categories for receipts and transactions.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Explicitly reviews and compares Mint, YNAB, Zerodha Kite, and Groww.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies lack of AI advisory, geographic restrictions, and lack of integration in existing solutions.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Implements LSTM microservice for spending and cash flow forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: Uses LSTM networks for time-series prediction, referencing Zhang et al. (2021).
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Includes budget tracking with alert thresholds and spending limits.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: AI advisor provides budget analysis and actionable recommendations.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: contextual
      justification: Discusses web app UI with responsive design but primarily desktop focus.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: contextual
      justification: Mentions dark-mode-first design and intuitive interface, but mobile-specific evaluation is limited.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Details JWT authentication, data isolation, rate limiting, and in-memory receipt processing.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Masumi verification layer provides cryptographic proof, enhancing auditability and trust.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Conversational AI and comprehensive dashboard aim to increase user engagement.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Conducts functional testing across all modules with PASS results and performance metrics.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Reports specific latency and accuracy benchmarks for AI inference, receipt scanning, and API fetches.
  contribution: "The Welth platform's modular architecture integrating a conversational AI advisor, multi-modal receipt scanner, and live portfolio tracker provides a blueprint for consolidating fragmented PFMS functionalities. Its use of Groq's LPU infrastructure for sub-second LLM inference demonstrates a practical path to real-time, context-aware financial advice in consumer applications. The documented performance benchmarks and graceful fallback strategies offer valuable design patterns for building resilient, AI-driven financial tools. The explicit evaluation of the LSTM prediction service and its integration as a separate microservice informs modular predictive module deployment. This work directly justifies Odin's architectural decisions, particularly the need for a unified, AI-augmented system that addresses the gaps identified in existing platforms."
  directly_justifies:
    - "Users lack access to personalized, affordable financial advisory services, justifying AI-driven assistance in Odin."
    - "Existing platforms like Mint and YNAB lack advanced AI advisory and are geographically restricted, supporting a localized PFMS."
    - "Manual expense logging leads to poor tracking accuracy, validating the need for automated receipt scanning."
    - "LSTM networks can effectively forecast cash flow trajectories, supporting predictive spending analytics in Odin."
    - "Conversational AI with user-specific context provides highly contextual and actionable financial advice."
  limits:
    - "Geographical and regulatory focus on the Indian market (SEBI guidelines), limiting direct applicability to the Philippines."
    - "Heavy dependency on third-party APIs (Yahoo Finance, MFAPI.in, Gemini) introduces potential service reliability risks."
    - "The platform requires a stable, high-speed internet connection, which may not be universally available."
    - "The LSTM prediction service is a separate microservice without an explicit high-availability strategy beyond a fallback."
    - "The AI advisor requires at least 3 months of aggregated data for accurate insights, posing a cold-start challenge."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was conducted. The paper's primary contribution—a comprehensive AI-powered PFMS with conversational advisory, receipt scanning, and portfolio tracking—directly aligns with Domain 4 (Existing Systems & Gaps) as it explicitly reviews and identifies limitations in platforms like Mint and YNAB, and Domain 10 (Data Privacy & User Trust) through its detailed security architecture. High relevance was assigned to 4.A, 4.B, 10.A, 12.A, and 12.B due to direct, actionable insights on system gaps, privacy implementation, and rigorous performance evaluation. Medium relevance was assigned to 3.A (expense categorization enums), 6.A/6.B (LSTM forecasting), 7.A/7.B (budgeting and recommendations), 10.B (verification for trust), and 11.A (engagement via AI). Contextual relevance was assigned to 9.A and 9.B as the paper discusses a web app with responsive design but lacks dedicated mobile-first evaluation. Borderline cases included 2.B (seasonal patterns) and 2.D (Filipino spending cycles), which were rejected as the paper's context is strictly Indian and does not address cultural spending nuances. Topics like 1.A, 1.B, 1.C (Filipino demographics), 5.A, 5.B, 5.C (behavioral profiling), 7.C/7.D (constrained optimization), 8.A/8.B/8.C (anomaly detection), 11.B (retention mechanisms), 12.C (specific budget recommendation evaluation), and 13.A/13.B/13.C (savings/debt specifics) were considered but rejected as they are not the focus or are not addressed in sufficient detail. Overall, the paper provides a strong proof-of-concept and architectural benchmarks that justify several Odin design decisions, particularly around system integration, AI advisory, and performance evaluation."
limitations:
  - "Geographical and regulatory focus is specifically on the Indian market and SEBI guidelines, which may limit direct utility for Filipino users. [unacknowledged]"
  - "The platform relies heavily on external third-party APIs (Yahoo Finance, MFAPI.in, Google Gemini), introducing potential points of failure. [acknowledged]"
  - "As a serverless web application requiring live data and AI inference, a stable, high-speed internet connection is a prerequisite. [unacknowledged]"
  - "The LSTM prediction service is implemented as a separate microservice without a specified high-availability failover beyond a graceful fallback. [unacknowledged]"
  - "The conversational AI advisor requires at least 3 months of aggregated user data to provide accurate insights, limiting immediate value for new users. [acknowledged]"
remember_this:
  - "Welth unifies budgeting, investments, EMI, and tax planning into one platform."
  - "CA Arjun provides contextual financial advice using real user transaction data."
  - "The automated receipt scanner achieves over 92% accuracy using Gemini 1.5 Flash."
  - "Groq's LPU enables sub-second latency for the 70B parameter LLM inference."
  - "Dashboard initial load is approximately 420ms, with most AI features under 3.2 seconds."
```