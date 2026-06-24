```yaml
paper_id: 4b5a7d6e-8f9c-4a1b-9d3e-8f2a5c1e7d4b
designation: local-algorithm-specific
title: AI Wealth Navigator: An Integrated Platform for Smart Budgeting, Financial Learning, and Personalized Policy Guidance
authors: Yadav, A.; Prakash, R. S.; Iqubal, S. M.; Gebremicahea, M. G.
year: 2024
venue: Unknown
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 6.A
  - 7.A
  - 7.B
  - 8.A
  - 9.A
  - 9.B
  - 10.A
  - 11.A
  - 12.A
tldr: Integrates AI-driven budgeting, adaptive financial learning, and policy recommendations into a unified platform for personal finance management.
problem_and_motivation: Users face fragmented financial ecosystems where budgeting, education, and policy knowledge are disjointed. Low financial literacy in India exacerbates poor decision-making on savings, investments, and government benefits. A unified, intelligent platform is needed to bridge these gaps and promote financial inclusion.
approach:
  - System uses Next.js frontend with Supabase and Prisma for data management.
  - Inngest handles automated tasks and notifications for background processes.
  - Gemini LLM powers personalized financial recommendations and adaptive learning.
  - Policy recommendation engine uses hybrid data APIs to suggest government schemes.
  - Arcjet ensures secure data handling and transaction encryption.
  - Evaluation involved human assessment by 50 users and system performance metrics.
findings:
  - num: Receipt scanner achieved 94% accuracy on digital and physical receipts.
  - num: Average user ratings were 4.8/5 for budgeting insights, 4.7/5 for policy, and 4.6/5 for learning.
  - num: Over 70% of users discovered previously unknown government programs.
  - Arcjet blocked all simulated security threats during testing.
  - Integration of three domains into one platform eliminated the need for multiple apps.
key_figures_tables:
  - Figure 1.1: System layered architecture showing frontend, backend, AI, and security components → Modular design separates core functions for scalability.
  - Figure 1.2: Detailed architecture diagram with data flow between modules → Highlights integration of LLM, APIs, and user interface.
  - Figure 1.3: Sequence diagram of user interactions → Illustrates real-time data flow and response generation.
  - Figure 1.4: Dashboard interface → Shows visual spending analytics and budget tracking tools.
  - Figure 1.5: Transaction page with receipt scanner → Demonstrates OCR-based expense entry.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: LLM
    definition: Large Language Model used for generating personalized financial insights.
  - term: OCR
    definition: Optical Character Recognition used for scanning and digitizing receipts.
  - term: API
    definition: Application Programming Interface for data exchange between system components.
critical_citations:
  - "[Patel et al., 2023] — AI platforms improve financial literacy with personalized paths."
  - "[Kumar et al., 2023] — Dynamic budgeting systems enhance user engagement."
  - "[Lee et al., 2023] — AI suggests social benefits based on financial profiles."
  - "[Gupta et al., 2024] — AI secures transactions and detects fraud."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Provides AI-driven budget tracker with receipt scanning for automated categorization.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: Discusses receipt scanner accuracy and structured transaction logs.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Explicitly surveys fragmented existing systems and proposes a unified alternative.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies gaps in integration, literacy, and policy access in current apps.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: low
      justification: Mentions predictive financial planning as future work, not implemented.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Offers personalized savings alerts and dynamic recommendations based on spending habits.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: Gemini LLM provides tailored budgeting insights and investment advice.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Security evaluation mentions fraud detection but not as a primary focus.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Frontend uses responsive design for mobile and desktop, with dark/light mode.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Interface includes visual dashboards and interactive tools, but mobile-specific UX not detailed.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Arcjet ensures encryption, secure data handling, and threat prevention.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: User ratings (4.7–4.8/5) indicate trust in relevance and empathy of recommendations.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Gamified learning modules and real-time insights support sustained user engagement.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: Adaptive roadmap and policy alerts keep users returning for new recommendations.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Uses both quantitative performance metrics (response time, token efficiency) and human evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Evaluates receipt scanner accuracy and LLM response quality.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: contextual
      justification: Human ratings provide qualitative assessment but no benchmark comparison.
  contribution: "The paper directly supports Odin's Budget Recommendation module (7.B) by demonstrating a unified AI platform that integrates Gemini LLM for personalized budgeting insights and real-time spending analytics. For Expense Categorization (3.A/3.B), the receipt scanner with 94% accuracy provides a benchmark for automated transaction logging. The system's modular architecture and security measures (Arcjet) inform Odin's Mobile-First Design (9.A/9.B) and Data Privacy (10.A) considerations. Additionally, the evaluation framework using both system metrics and user ratings (4.8/5) offers a template for Odin's System Evaluation (12.A)."
  directly_justifies:
    - "AI-driven platforms can close financial literacy gaps and empower low-income communities."
    - "LLM-based systems provide context-aware, personalized financial recommendations."
    - "Integrating budgeting, education, and policy into one ecosystem improves user experience."
    - "Automated receipt scanning reduces manual entry errors and increases adoption."
    - "Multi-layer security is essential for protecting personal financial data."
  limits:
    - "Study conducted with only 50 Indian users, may not generalize to Filipino context."
    - "No longitudinal data on behavior change or retention over time."
    - "Dependence on full user profiles for policy matching may raise privacy concerns [unacknowledged]."
    - "Sporadic OCR errors mentioned as a drawback but not quantified in detail."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains of Expense Categorization, Existing Systems & Gaps, Budget Recommendation, Data Privacy, and System Evaluation were flagged as highly relevant, as the paper directly addresses these with algorithmic contributions and evaluation metrics. Behavioral Profiling (5.A) and Forecasting (6.A/6.B) were considered but rejected due to only cursory mentions (forecasting as future work, no behavioral classification). Anomaly Detection (8.A) was marked contextual because security evaluation touched on fraud prevention but without algorithmic detail. Mobile-First Design (9.A/9.B) was medium relevance due to the mention of responsive design but lack of in-depth UX analysis. Filipino-specific topics (2.A-2.D) were rejected entirely as the study is based in India and does not address Filipino cultural contexts. Overall, the paper is highly relevant for its integrated AI architecture, but its international algorithm-specific focus limits direct applicability to Odin's Philippine-centric design."
limitations:
  - "Limited user sample (n=50) and geographic scope (India)."
  - "No comparison against existing baseline systems or benchmarks."
  - "Relies on proprietary Gemini LLM, limiting reproducibility."
  - "Policy recommendation engine not evaluated for correctness or coverage."
  - "Long-term user retention and behavior change not assessed. [unacknowledged]"
remember_this:
  - "Unified platform combines budgeting, learning, and policy into one system."
  - "Receipt scanner achieves 94% accuracy on diverse receipt types."
  - "User ratings averaged 4.8/5 for budgeting insights and 4.7/5 for policy."
  - "Arcjet provides API-layer threat prevention and data encryption."
  - "Over 70% of users discovered new government programs through the engine."
```