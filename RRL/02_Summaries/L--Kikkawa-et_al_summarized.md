```yaml
paper_id: 10.69569/jip.2026.060
designation: local
title: Impact of Financial Literacy on Financial Performance in Select Multi-Purpose Cooperatives in Tagbilaran City, Bohol, Philippines
authors: Gudelosao, E.; Cafe, A.J.; Liray, K.; Tabaco, J.G.; Felicitas, L.N.
year: 2026
venue: Journal of Interdisciplinary Perspectives
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.C
  - 3.A
  - 3.C
  - 5.A
  - 5.B
  - 5.C
  - 13.A
  - 13.B
  - 13.C
tldr: Financial attitude fully mediates the relationship between financial knowledge and behavior, but member literacy does not predict cooperative financial performance.
problem_and_motivation: Cooperatives are vital for financial inclusion in the Philippines, yet low member financial literacy may undermine individual decisions and organizational performance. The direct link between member-level financial competence and institutional success remains under-researched in the local context.
approach:
  - Quantitative descriptive-correlational design with mediation analysis.
  - Data from 100 members across four large multi-purpose cooperatives in Tagbilaran City.
  - Questionnaire with 30 items measuring financial knowledge, attitude, and behavior.
  - Cooperative financial performance assessed via CDA STEPS ratios from 2024 financial statements.
  - OLS regression path analysis and PROCESS bootstrapping for mediation.
findings:
  - Financial knowledge significantly increases financial attitude (β = 0.525, p < .001).
  - Financial attitude significantly increases financial behavior (β = 0.592, p < .001).
  - num: Financial knowledge has no significant direct effect on financial behavior (β = 0.024, p = .797).
  - num: Financial attitude fully mediates the knowledge-behavior pathway (indirect effect β = 0.311, p < .001).
  - num: Financial literacy does not significantly predict cooperative financial performance (β = 0.048, p = .632).
  - num: The model explains only 0.2% of the variance in cooperative financial performance (R² = 0.002).
key_figures_tables:
  - Table 1: Demographic profile of 100 cooperative members → Majority are female, college graduates, and lower-income.
  - Table 2: Financial literacy component means → Overall FLI of 3.50 (High), with knowledge highest and behavior lowest.
  - Table 3: Direct effects in mediation model → Attitude fully mediates the knowledge-behavior relationship.
  - Table 4: Indirect effects with bootstrapping → Full mediation confirmed (95% CI: 0.194 to 0.452).
  - Table 5: Cooperative financial performance STEPS scores → Most cooperatives rated 'Fair' (scores 56-70).
  - Table 6: Regression of literacy on performance → Non-significant with trivial effect size.
key_equations:
  - equation: \beta = 0.525, p < .001
    explanation: Knowledge strongly predicts positive financial attitude.
  - equation: \beta = 0.592, p < .001
    explanation: Attitude strongly predicts improved financial behavior.
  - equation: \beta = 0.024, p = .797
    explanation: Knowledge does not directly change behavior.
  - equation: R^2 = 0.002
    explanation: Literacy explains negligible variance in cooperative performance.
definitions:
  - term: FLI
    definition: Financial Literacy Index, a composite mean score of knowledge, attitude, and behavior.
  - term: STEPS
    definition: Stability, Turnover, Efficiency, Profitability, and Structure of Assets ratio framework by CDA.
  - term: OLS
    definition: Ordinary Least Squares regression for estimating linear relationships.
critical_citations:
  - "[Perez & Lopez, 2020] — School coop members have knowledge but poor discipline."
  - "[Yeolencia & Lestari, 2024] — Attitude mediates knowledge-behavior link."
  - "[Lusardi, 2019] — Knowledge alone rarely improves outcomes without structural support."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Studies cooperative members, not specifically young professionals.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: low
      justification: Focuses on cooperative savings/loans, not personal financial structure.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Directly measures financial behavior of cooperative members.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Examines Filipino cooperative membership as a financial practice.
    - code: 2.C
      name: User-Declared Financial Preferences
      relevance: contextual
      justification: Surveys attitudes but does not analyze declared allocation preferences.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: low
      justification: Does not address categorization of expenses.
    - code: 3.C
      name: User-Defined Allocation Constraints
      relevance: low
      justification: No discussion of user-defined budget constraints.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Identifies distinct roles of knowledge, attitude, and behavior.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: contextual
      justification: Highlights that knowledge alone is insufficient, relevant to initialization.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Uses regression, not classification models.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: Discusses saving behavior generally, not goal management.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: low
      justification: Mentions borrowing but not debt management systems.
    - code: 13.C
      name: End-of-Period Surplus as a Savings Input
      relevance: low
      justification: Does not address surplus allocation or savings input mechanics.
  contribution: The paper confirms that financial attitude is a necessary mediator between knowledge and behavior, which directly informs Odin's behavioral profiling module by emphasizing attitudinal data collection. The finding that member literacy does not predict cooperative performance suggests Odin's budget recommendation and anomaly detection systems must account for organizational constraints. The mediation framework provides a methodological template for Odin's user classification pipeline. The non-significant direct effect of knowledge on behavior justifies Odin's focus on behavioral nudges over purely educational content. Finally, the study's local Filipino context validates Odin's culturally grounded design assumptions.
  directly_justifies:
    - Odin must measure financial attitude separately from knowledge and behavior.
    - Knowledge-based interventions alone are insufficient for behavior change.
    - Behavioral profiling should include attitudinal mediators for accurate predictions.
    - Organizational factors dominate individual literacy in predicting financial outcomes.
    - Financial performance improvements require system-level changes beyond user education.
  limits:
    - Sample limited to four cooperatives in Tagbilaran City.
    - Non-probability purposive sampling limits generalizability.
    - Cross-sectional design cannot establish causality.
    - Financial performance data aggregated to cooperative level, not individual.
    - Reliance on self-reported measures may introduce social desirability bias.
  mapping_rationale: The systematic scan across all 12 functional domains flagged the Filipino Cultural Context, Behavioral Profiling, and Savings & Debt Management domains as relevant. Topics 1.C, 2.A, 5.A, and 5.B were selected with medium relevance for their direct measurement of financial behavior and the mediating role of attitude in a Filipino cooperative context. Topics 1.A, 2.C, and 5.C were considered contextual or low because the demographic is not specifically young professionals, user preferences are not explicitly modeled, and classification approaches are not used. All algorithmic domains (Expense Categorization, Forecasting, Recommendation, Anomaly Detection, Evaluation) were rejected as the paper contains no computational techniques. Mobile design, privacy, retention, and engagement domains were also rejected for lack of relevant content. The paper's overall relevance to Odin is moderate, providing behavioral and attitudinal insights for profiling but no algorithmic or system design contributions.
limitations:
  - Cross-sectional design prevents causal inference of mediation.
  - Non-probability sampling limits external validity to Tagbilaran cooperatives. [unacknowledged]
  - Self-reported attitudes and behaviors may not reflect actual practices.
  - Cooperative performance metrics may not capture member-level financial outcomes.
  - The instrument's 30-item scale may not cover all dimensions of financial literacy.
remember_this:
  - Financial attitude fully mediates the knowledge-behavior pathway.
  - Knowledge alone has no significant direct effect on financial behavior.
  - Member financial literacy does not predict cooperative financial performance.
  - Organizational factors dominate individual literacy in driving performance.
  - Attitude-focused training is more effective than information-heavy lectures.
```