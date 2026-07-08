```yaml
paper_id: 10.30919/es2245
designation: international
title: Artificial Intelligence-Driven Transformation in Financial Technology: Applications, Agents and Challenges
authors: Zhang, Z.; Lu, M.
year: 2026
venue: Engineered Science
odin_topics:
  - 4.A
  - 4.B
  - 5.A
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 9.A
  - 10.A
  - 11.A
  - 12.A
  - 12.B
tldr: A comprehensive review synthesizing AI applications in fintech, from predictive models to autonomous agents, while systematically analyzing technical and ethical challenges.
problem_and_motivation: Financial systems generate large-scale, heterogeneous data exceeding conventional analytical capacity, yet existing literature treats machine learning, explainable AI, and governance as separate lines of inquiry. A unified synthesis of predictive models, generative systems, and agent-based architectures within a single fintech framework remains limited.
approach:
  - This review provides a holistic synthesis and structured taxonomy of AI applications in fintech.
  - It classifies applications ranging from foundational machine learning for credit scoring to advanced autonomous agents.
  - The review systematically analyzes critical technical and ethical hurdles, including interpretability, data quality, and security.
  - It examines emerging paradigms like autonomous and multi-agent systems revolutionizing financial workflows.
  - The analysis bridges the gap between AI and financial applications to delineate a future research agenda.
findings:
  - Generative AI market is projected to grow from USD 13.5 billion in 2023 to approximately USD 255.8 billion by 2033.
  - num: North America accounted for over 42.1% of global revenue in 2023, valued at USD 5.6 billion.
  - AI-driven credit modelling using alternative data improves default prediction and widens access for thin-file borrowers.
  - Fraud detection systems benefit from AI through reduced false positives and faster manual review times.
  - Reinforcement learning and deep learning models improve risk-adjusted metrics in portfolio management backtests.
  - Explainable AI is becoming a major component of finance research due to regulatory and accountability demands.
  - AI agents are transitioning fintech from task-specific automation towards adaptive, interactive, and autonomous workflows.
key_figures_tables:
  - Figure 1: Market map of AI application areas in fintech → Shows AI's pervasive role across payments, credit, and trading.
  - Table 1: Open-source resources for AI in fintech → Lists tools (FinQA, TensorFlow) that democratize access to AI capabilities.
  - Figure 2: AI applications in fintech industry → Visualizes deployment across client interaction, security, and complex analysis.
  - Figure 3: Core architecture of AI agents in fintech → Describes agentic workflow combining LLMs, tools, and memory for finance.
  - Figure 4: Multi-agent workflow for credit assessment → Illustrates query routing and collaboration for fraud detection.
  - Figure 5: Technical, regulatory and system challenges → Summarizes key hurdles for responsible AI deployment in finance.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Fintech
    definition: Financial technology integrating AI and digital services to enhance financial operations.
  - term: XAI
    definition: eXplainable Artificial Intelligence for making model decisions transparent.
  - term: AML
    definition: Anti-Money Laundering, a compliance process to prevent financial crime.
  - term: RAG
    definition: Retrieval Augmented Generation to ground LLM outputs in verified knowledge.
  - term: SupTech
    definition: Supervisory Technology using AI for regulatory oversight.
critical_citations:
  - "[Cao et al., 2021] — Establishes data science and AI as core fintech foundation."
  - "[Lessmann et al., 2015] — Benchmarks modern classifiers for credit scoring."
  - "[Ryman-Tubb et al., 2018] — Surveys ML impact on payment card fraud detection."
  - "[Theate & Ernst, 2021] — Foundational study on deep RL for algorithmic trading."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Surveys current AI applications across fintech lending, fraud, and trading.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Systematic analysis of data quality, transparency, and robustness gaps in current AI models.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: Discusses personalization and robo-advisory but not behavioral profiling specifically.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Reviews predictive models for credit scoring and market forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: Covers time-series forecasting with LSTM and deep learning for market data.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: Mentions personalized financial advice but not budgeting strategies in depth.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Focuses on robo-advisory for investment, not expense budgeting.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly addresses fraud detection and transactional anomaly recognition.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Reviews algorithms (neural networks, graph networks) for financial anomaly detection.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: contextual
      justification: Mentions fintech services but does not focus on mobile design specifically.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Dedicated sections on data privacy, federated learning, and security vulnerabilities.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: contextual
      justification: Mentions customer service chatbots but not engagement dynamics or retention.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Calls for frameworks to evaluate robustness, fairness, and governance.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Reviews benchmarking datasets and validation techniques for fintech models.
  contribution: This paper surveys the entire AI in fintech landscape, offering a taxonomy that connects predictive models, generative AI, and autonomous agents. It systematically catalogs technical challenges (data quality, black-box models) and emerging agent-based architectures relevant to Odin's design. Its organized literature review justifies Odin's selection of algorithmic approaches (e.g., LSTM for forecasting, XAI for transparency) and highlights evaluation frameworks for modules like anomaly detection.
  directly_justifies:
    - "AI in fintech is transitioning from task-specific automation to adaptive, interactive workflows."
    - "Explainable AI is essential for regulatory compliance in high-stakes financial decisions."
    - "Graph neural networks are being adopted for transaction monitoring in anti-money laundering."
    - "Generative AI can produce synthetic data for training robust models without compromising privacy."
  limits:
    - "This is a review paper; it does not introduce a novel algorithm or empirical study."
    - "The scope is broad, limiting deep technical analysis of specific Odin-relevant tasks like budgeting."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. Domains flagged as relevant include Existing Systems & Gaps (4.A, 4.B), Anomaly Detection (8.A, 8.B), and Data Privacy (10.A) for high relevance. Medium relevance was assigned to Predictive Modeling (6.A, 6.B) and System Evaluation (12.A, 12.B) due to broad algorithm reviews. Borderline cases: Papers on spending cycles (2.B, 2.D) and mobile design (9.A) were considered but rejected as the paper is a high-level technology survey lacking Filipino cultural specifics. The paper's overall relevance to Odin is high for justifying the need for robust, explainable, and adaptive AI modules within a PFMS, providing a literature-backed rationale for architectural choices and challenges.
limitations:
  - "Broad review scope, lacks in-depth empirical validation for specific algorithms. [unacknowledged]"
  - "Focuses on international fintech, lacks direct cultural context for Filipino users. [unacknowledged]"
  - "Optimistic projections for AI adoption may overlook regulatory and implementation friction."
  - "Discussion of agentic AI is forward-looking, with limited evidence of mature deployment."
remember_this:
  - "AI in finance requires a balance between predictive accuracy and interpretability."
  - "Data quality and privacy are foundational challenges for deploying fintech models."
  - "XAI is critical for regulatory audit and trust in automated credit decisions."
  - "The global generative AI market is projected to grow at a 34.2% CAGR until 2033."
  - "Agent-based systems may shift fintech from predictive tools to autonomous decision-making."
```