```yaml
paper_id: 10.62986/dp2026.03
designation: local
title: Digital Financial Platform Engagement and Financial Inclusion in the Philippines: Insights on AI Deployment and Policy Implications
authors: Pesa, N. C.; Agner, M. G. R.; Lacaza, R. M.
year: 2026
venue: PIDS Discussion Paper Series
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 3.A
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 6.A
  - 7.A
  - 8.A
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 12.A
tldr: Digital financial engagement strongly predicts formal account ownership and usage in the Philippines, yet AI adoption remains nascent and concentrated among large institutions, with persistent barriers of cost, trust, and documentation.
problem_and_motivation: The Philippines has made progress in financial inclusion, yet a large segment remains unbanked due to cost, distance, lack of documentation, and low trust. Digital financial platforms and AI offer potential solutions, but their deployment and impact are not well understood.
approach:
  - Constructed a Digital Financial Engagement Index using Multiple Correspondence Analysis on World Bank Global Findex 2021 data for the Philippines.
  - Estimated logit models to examine the relationship between digital engagement and account ownership, usage, and perceived barriers.
  - Analyzed supply-side trends using IMF Financial Access Survey data (2016-2024) on financial infrastructure.
  - Conducted key informant interviews with 12 experts from universal banks, cooperatives, savings and loan associations, and policy institutions.
  - Triangulated demand-side survey data with supply-side institutional data and qualitative insights to provide a comprehensive assessment.
findings:
  - num: A one-unit increase in the Digital Financial Engagement Index is associated with a 78.5 percentage point increase in formal account ownership likelihood.
  - num: Digital financial engagement reduces the probability of citing 'lack of trust' as a barrier by 29.4 percentage points.
  - Digital financial engagement is a stronger predictor for account entry than for more complex behaviors like saving or borrowing.
  - AI adoption in the Philippine financial sector is nascent and concentrated among large, digitally advanced institutions.
  - Persistent barriers to inclusion include lack of money (76%), high costs (55%), and distance (40%).
findings:
  - num: A one-unit increase in the Digital Financial Engagement Index is associated with a 78.5 percentage point increase in formal account ownership.
  - num: Digital financial engagement reduces the likelihood of citing 'lack of trust' as a barrier by 29.4 percentage points.
  - num: Only 2% of Filipinos can correctly answer basic financial literacy questions, according to the BSP's 2021 survey.
  - Digital financial engagement more strongly predicts account entry than continued usage.
  - AI adoption is nascent, concentrated in large institutions, and used mainly for fraud detection and credit scoring.
key_figures_tables:
  - Figure 1: Share of digital payments in total retail transactions (2018-2024) → Digital retail payment volume reached 57.4% in 2024.
  - Figure 2: Mode of payment used by adult Filipinos (2019 and 2021) → Cash remains dominant, but digital payments are growing.
  - Table 5: Financial inclusion indicators for account ownership and usage → Account ownership is 56%, formal saving only 28%.
  - Table 6: Reasons for not having a formal account → Lack of money (76%) and high cost (55%) are top barriers.
  - Table 10: Determinants of account ownership → Digital engagement is the strongest predictor for all account types.
key_equations:
  - equation: logit(P(Y_i = 1)) = β0 + β1 DigitalIndex_i + β2 X_i + ε_i
    explanation: Logit model linking digital engagement to financial inclusion outcomes.
  - equation: logit(P(B_i = 1)) = γ0 + γ1 DigitalIndex_i + γ2 X_i + ν_i
    explanation: Logit model for perceived barriers to account ownership.
definitions:
  - term: AI Preparedness Index (AIPI)
    definition: IMF metric measuring digital infrastructure, human capital, innovation, and regulation for AI.
  - term: Digital Financial Engagement Index
    definition: A 0-1 index measuring individual usage of mobile payments, online banking, and digital transactions.
  - term: Global Findex
    definition: World Bank database on financial inclusion, covering account ownership, usage, and barriers.
  - term: KII
    definition: Key Informant Interview, a qualitative method for gathering insights from subject matter experts.
  - term: NSFI
    definition: National Strategy for Financial Inclusion, the Philippines' roadmap for expanding financial access.
critical_citations:
  - "[Debuque-Gonzales and Corpus, 2021] — Provides Philippine financial inclusion index and determinants."
  - "[Fazal et al., 2023] — Systematic review linking AI and financial inclusion in developing economies."
  - "[World Bank Global Findex, 2021] — Primary demand-side data source on financial inclusion."
  - "[IMF Financial Access Survey, 2024] — Primary supply-side data source on financial infrastructure."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: "Discusses Filipino adults' financial behavior, including young, tech-savvy consumers."
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: "Analyzes account ownership, saving, and borrowing patterns among Filipino adults."
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: "Directly examines digital financial engagement and its link to financial behavior."
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: "Identifies reliance on informal saving clubs (paluwagan) and family as key financial practices."
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: "Discusses spending cycles indirectly through mentions of remittances and informal borrowing."
    - code: 2.D
      name: Filipino Spending Cycles and 'Occasions'
      relevance: contextual
      justification: "Contextualizes financial behavior within Filipino cultural and social practices."
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: low
      justification: "Not a focus; the paper focuses on broader financial inclusion, not categorization."
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: "Comprehensively reviews the Philippine financial inclusion landscape and digital platforms."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: "Identifies barriers like cost, trust, and institutional disparities in AI adoption."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: "Constructs a Digital Financial Engagement Index, which is a behavioral profile."
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: "Uses Multiple Correspondence Analysis to classify and measure digital financial engagement."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: low
      justification: "Discusses AI for credit scoring, but does not detail specific predictive models."
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: low
      justification: "Not a direct focus; the paper is about inclusion, not specific budgeting strategies."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: "Identifies fraud detection as a key AI application, which is a form of anomaly detection."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: "Discusses data privacy, cybersecurity, and the need for secure AI deployment."
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: "Explicitly analyzes trust as a barrier and finds digital engagement reduces mistrust."
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: "The core of the paper is analyzing how digital engagement drives financial inclusion."
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: "Discusses initiatives like Bank on Wheels to improve access and engagement."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: "Uses regression analysis to evaluate the impact of digital engagement on inclusion."
  contribution: "This paper provides a comprehensive, two-sided analysis of financial inclusion in the Philippines, bridging demand-side consumer behavior with supply-side institutional readiness. It introduces a novel Digital Financial Engagement Index to quantify how digital platform usage drives account ownership and usage. The study also documents the nascent state of AI adoption in the Philippine financial sector, highlighting its concentration in large institutions and key use cases like fraud detection and credit scoring. These findings directly inform Odin's design by providing empirical justification for prioritizing digital engagement as a core module, and by demonstrating the importance of building trust and literacy into the system. The identification of persistent barriers like cost, documentation, and trust provides a clear mandate for Odin's features, such as user-defined constraints and anomaly detection."
  directly_justifies:
    - "Digital financial engagement is the strongest predictor of formal account ownership in the Philippines."
    - "Greater engagement with digital platforms reduces lack of trust in financial institutions."
    - "AI adoption for fraud detection and credit scoring can enhance security and access."
    - "Cost and lack of documentation are the most significant barriers to financial inclusion."
    - "Smaller institutions face structural barriers to AI adoption."
  limits:
    - "The demand-side analysis uses digital engagement as a proxy for AI exposure, as the Global Findex does not directly measure AI awareness or usage."
    - "The actual AI exposure varies by platform, which is not captured in the survey data."
    - "The study does not examine the technical specifications or performance of specific AI systems."
    - "The supply-side analysis relies on a small sample of key informants and may not be fully representative."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper's focus on digital financial engagement and financial inclusion directly maps to the 'Behavioral Profiling & Classification', 'Existing Systems & Gaps', and 'Data Privacy & User Trust' domains, resulting in high relevance for topics 1.C, 2.A, 4.A, 4.B, 5.A, 5.C, 10.A, 10.B, and 11.A. The paper's analysis of AI deployment for fraud detection and credit scoring provides medium relevance to topics 8.A and 6.A, respectively. Topics related to specific budgeting strategies (7.A) or expense categorization (3.A) were considered but rejected as the paper does not address these implementation-level details. The paper's discussion of Filipino financial practices (2.B, 2.D) and demographic context (1.A, 1.B) provides contextual or medium relevance. The overall relevance is high, as the paper provides direct empirical justification for Odin's core design by demonstrating that digital engagement drives inclusion and that trust and security are critical."
limitations:
  - "The Global Findex survey does not include direct questions about AI awareness, usage, or literacy, so digital engagement is used as an indirect proxy. [unacknowledged]"
  - "The Digital Financial Engagement Index cannot distinguish between high-AI and low-AI platforms, as this information is not available in the survey. [unacknowledged]"
  - "The qualitative supply-side analysis is based on a limited number of key informant interviews and may not capture the full diversity of institutional experiences. [unacknowledged]"
  - "The study does not evaluate the technical performance or fairness of specific AI algorithms used in the financial sector. [unacknowledged]"
remember_this:
  - "Digital engagement is the strongest predictor of account ownership."
  - "Cost and trust are the primary barriers to financial inclusion."
  - "AI adoption in Philippine finance is nascent and uneven."
  - "Targeted literacy programs can complement digital infrastructure."
```