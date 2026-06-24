```yaml
paper_id: 10.1145/3760557.3760578
designation: local
title: Understanding the Impulse Buying Behavior in the Digital Age: Influential Factors in Online Consumer Behavior
authors: Gabatin, R. A.; Sierra, S. M.; Maniago, M. G.; Capole, A.; Torres, R.
year: 2025
venue: 16th International Conference on E-business, Management and Economics (ICEME 2025)
odin_topics:
  - 1.C
  - 2.A
  - 2.D
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 9.A
  - 9.B
tldr: Social and website factors drive impulse buying by influencing urgency and consumer characteristics, not directly through marketing or direct social pressure.
problem_and_motivation: Understanding impulse buying is crucial for businesses, yet the specific interplay of social, marketing, and website-related factors in the digital age remains unclear, especially within the Filipino market. Existing literature lacks a comprehensive model that integrates these elements with consumer characteristics and urgency within the SOR framework.
approach:
  - The study uses a quantitative, correlational research design to examine impulse buying behavior.
  - It employed a structured survey distributed to 381 purposively sampled respondents from Cabuyao, Laguna.
  - Data was analyzed using Partial Least Squares Structural Equation Modeling (PLS-SEM) in WarpPLS 8.0.
  - The measurement model was validated using Composite Reliability, Cronbach's Alpha, and Average Variance Extracted (AVE).
  - The structural model assessed direct, mediating, and moderating effects with path coefficients and effect sizes.
findings:
  - num: Social-related factors have a significant large effect on website-related factors (β=0.868, p<0.001).
  - num: Marketing-related factors significantly affect consumer characteristics with a large effect size (β=0.714, p<0.001).
  - num: Urgency to buy has a significant large direct effect on impulse buying (β=0.804, p<0.001).
  - num: Consumer characteristics significantly affect urgency to buy with a large effect (β=0.562, p<0.001).
  - num: The model explains 80.4% of the variance in impulse buying (R²=0.804).
  - Social and marketing factors do not directly drive impulse buying but act through website usability and consumer characteristics.
  - Age and gender did not significantly moderate the urgency-impulse buying relationship.
key_figures_tables:
  - Figure 1: Conceptual Framework based on SOR theory → Outlines the hypothesized relationships among all study variables.
  - Figure 2: Final Model after removing insignificant paths → Highlights website usability and urgency as key direct drivers of impulse buying.
  - Table 1: Convergent Validity and Reliability Measures → Confirms all constructs met the required AVE and reliability thresholds.
  - Table 4: Evaluation of the Structural Model with path coefficients → Reports direct, mediating, and moderating effects for all hypotheses.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: SOR Framework
    definition: Stimulus-Organism-Response framework explaining how external stimuli influence internal states leading to behavioral responses.
  - term: Impulse Buying
    definition: Spontaneous and unplanned purchasing behavior driven by emotional triggers and external stimuli.
  - term: PLS-SEM
    definition: Partial Least Squares Structural Equation Modeling, a statistical technique for analyzing complex cause-effect relationship models.
critical_citations:
  - "[Cohen, 1988] — Defines thresholds for effect sizes (R²) used to validate model predictive accuracy."
  - "[Hair et al., 2006] — Provides the methodological standard for multivariate data analysis used in the study."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly investigates impulse buying behavior, a key aspect of financial behavior for young professionals.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Acknowledges that impulse buying in the Philippine market is shaped by cultural and social influences.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: The study's focus on impulse buying can be contextualized within Filipino spending cycles, though not explicitly studied.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Informs the landscape by highlighting how e-commerce and marketing strategies encourage unplanned spending.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: low
      justification: Identifies a gap in understanding the interplay of factors driving impulse buying, which PFMS could address.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Discusses consumer characteristics like shopping lifestyle and impulsivity, which are key to behavioral profiling.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Utilizes a quantitative approach to classify and relate factors (e.g., social, marketing) to behavioral outcomes.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Findings on website-related factors (ease of use, payment) are directly applicable to mobile-first design principles.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: high
      justification: Provides empirical evidence that website usability and seamless payment processes drive urgency and unplanned purchases.
  contribution: The study's findings on impulse buying can inform Odin's anomaly detection module by identifying behavioral patterns (like urgency-driven purchases) that deviate from a user's norm. Its insights on website usability and consumer characteristics can directly justify Odin's mobile-first design choices, emphasizing the need for a frictionless UX to reduce the likelihood of impulsive financial decisions. The SOR framework provides a theoretical basis for modeling how external stimuli (e.g., app notifications, offers) might influence user financial behavior within Odin. The confirmation that urgency strongly drives impulse purchases suggests that Odin's budget recommendation system could be designed to counteract such urgency with real-time feedback or savings prompts. Finally, the understanding of consumer characteristics (like shopping lifestyle) can guide the personalization of financial advice and alerts within Odin.
  directly_justifies:
    - "Website usability and seamless payment processes significantly increase the likelihood of unplanned purchases."
    - "Urgency to buy is a powerful direct driver of impulse buying behavior."
    - "Social-related factors influence consumer perception of website-related factors like ease of use."
    - "Consumer characteristics such as shopping lifestyle play a significant role in shaping impulse buying."
  limits:
    - "The study is geographically limited to respondents from Cabuyao, Laguna, which may not represent the broader Filipino population."
    - "It relies on self-reported survey data, which is subject to social desirability and recall bias. [unacknowledged]"
    - "The cross-sectional design can establish relationships but not causality. [unacknowledged]"
    - "The focus on impulse buying in general e-commerce may not directly translate to a personal finance management context."
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The paper's core focus on consumer behavior in a digital environment directly maps to understanding the financial behavior (1.C) and cultural practices (2.A) of the target demographic. The examination of website-related factors and user experience provides high relevance to Odin's Mobile-First Design (9.A and 9.B), as the findings emphasize ease of use and seamless payment. The study's analysis of mediating factors like consumer characteristics offers medium relevance to Behavioral Profiling (5.A) by describing trait-dependent shopping behaviors. Domains like Spending Forecasting (6.A/6.B), Budget Recommendation (7.A-D), and Anomaly Detection (8.A-C) were considered but rejected due to the paper's focus on drivers of unplanned spending rather than prediction or management strategies. However, the findings on urgency and its effect on unplanned purchases provide contextual relevance (low) for understanding spending patterns that could be flagged as anomalies. The overall relevance is medium-high for design and user behavior understanding but low for algorithmic or system evaluation components.
limitations:
  - "Self-reported data may be subject to social desirability and recall bias. [unacknowledged]"
  - "Cross-sectional design precludes establishing causal relationships. [unacknowledged]"
  - "Geographic scope limited to a single city in the Philippines, limiting generalizability."
  - "The study's findings may not directly apply to the specific context of personal finance management systems."
remember_this:
  - "Urgency has a very large direct effect on impulse buying."
  - "Website usability drives impulse buying by increasing urgency."
  - "Consumer characteristics mediate the impact of marketing on impulse buying."
  - "Social factors do not directly cause impulse buying but influence website perception."
  - "The model explains 80% of the variance in impulse buying behavior."
```