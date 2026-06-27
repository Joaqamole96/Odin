```yaml
paper_id: 10.32479/irmm.23379
designation: local
title: Exploring the Impact of Cashless Payment Systems on Impulsive Buying Behavior among Generation Z Consumers
authors: Yu, M. P.
year: 2026
venue: International Review of Management and Marketing
odin_topics:
  - 1.A
  - 2.D
  - 3.C
  - 4.A
  - 5.A
  - 7.D
  - 10.B
tldr: Cashless payment systems enable impulsive buying among Filipino Gen Z consumers through convenience, promotions, social media influence, and trust, with males exhibiting stronger susceptibility to these factors.
problem_and_motivation: Existing literature examines cashless payment factors and impulsive buying in isolation, lacking an integrated model for Generation Z within the Filipino context. This gap hinders the understanding of how convenience, social media, promotions, and security collectively drive impulsive behavior among this digitally native demographic.
approach:
  - A descriptive survey design was employed using a researcher-made questionnaire.
  - Data was collected from 259 Gen Z respondents in Cantilan, Philippines.
  - The instrument measured factors of ease, social media, promotions, and trust on a 5-point Likert scale.
  - Descriptive and inferential statistics including Pearson correlation, Mann-Whitney U, and MANOVA were utilized.
  - The study analyzed differences in impulsive tendencies based on gender, payment method, and product type.
findings:
  - num: The overall weighted mean for impulsive buying behavior was 4.03, indicating agreement that cashless payments drive it.
  - num: A very strong positive correlation (r = 0.892, P = 0.000) exists between cashless payment systems and impulsive buying.
  - Perceived usefulness, trust, and security showed the strongest correlation (r = 0.869, P = 0.000) with impulsive buying.
  - Significant gender differences were found for ease/convenience (U=2969.00, P=0.003), promotions (U=3232.50, P=0.021), and trust/security (U=2839.00, P=0.001), with males more influenced.
  - Social media influence was not significantly different between genders (P=0.123).
  - No significant differences in impulsive buying were found based on preferred cashless payment method (P=0.194) or product type (P=0.931).
key_figures_tables:
  - Table 1: Demographic profile shows 74% of respondents are 13-21, 85% female, and 83% prefer mobile payment apps.
  - Table 2: Ease and convenience factor weighted mean of 4.09, with the highest agreement on payments preventing avoidance of impulse purchases.
  - Table 3: Social media influence factor weighted mean of 4.11, with positive reviews strongly influencing spontaneous purchases.
  - Table 4: Promotions and discounts factor weighted mean of 4.02, with promotional discounts being the strongest motivator.
  - Table 5: Perceived usefulness, trust, and security factor weighted mean of 4.00, where usefulness for quick purchases is the top item.
  - Table 6: Impulsive buying behavior weighted mean of 4.03, with promotional offers and cashback as the strongest driver.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: BNPL
    definition: Buy Now Pay Later, a service allowing deferred payment for purchases.
  - term: FOMO
    definition: Fear Of Missing Out, an anxiety that others might be having rewarding experiences.
critical_citations:
  - "[Goyal, 2024] — Shows mobile wallets facilitate Gen Z impulse buying."
  - "[Izham et al., 2025] — BNPL services significantly impact Gen Z impulse buying."
  - "[Djamhari et al., 2024] — Perceived usefulness and safety drive impulsive buying."
  - "[Underdown and Tamara, 2025] — BNPL encourages addiction and lack of self-control."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: The study focuses specifically on Filipino Generation Z consumers, a core demographic for Odin.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: While not explicit, the study examines general impulsive spending behavior relevant to understanding spending cycles.
    - code: 3.C
      name: User-Defined Allocation Constraints
      relevance: low
      justification: The study identifies impulsive buying as a behavior that conflicts with user-defined budgets, providing a justification for constraint features.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: The paper evaluates how existing cashless systems (e-wallets, BNPL) facilitate spending, which is part of the fintech landscape.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: The study profiles impulsive buying behavior among Gen Z, which can inform behavioral profiling models.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: contextual
      justification: The suggested "impulse delay" feature relates to modifying behavior to stay within constraints, a form of infeasibility handling.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Trust and security perception is a key factor influencing impulse buying, highlighting the role of user trust in financial systems.
  contribution: This paper provides empirical evidence on how cashless payment systems enable impulsive buying among Filipino Gen Z, a behavioral trait that Odin's budget recommendation and anomaly detection modules must account for. The strong correlation (r=0.892) between cashless payments and impulsive behavior justifies the need for behavioral profiling in Odin to identify at-risk users. The finding that trust and security perception is the strongest correlate highlights the importance of Odin's data privacy and security features in building user confidence. The study's identification of gender differences (males more susceptible to convenience and promotions) supports the design of personalized nudges within Odin. Furthermore, the suggested "impulse delay" intervention validates Odin's potential for incorporating behavioral constraints to counteract spending tendencies.
  directly_justifies:
    - "Cashless payment systems have a very strong positive correlation (r=0.892) with impulsive buying among Filipino Gen Z."
    - "Perceived usefulness, trust, and security are the strongest factors correlating with impulsive buying behavior."
    - "Males are significantly more influenced by convenience, promotions, and security than females in impulsive buying."
    - "Interventions like impulse-delay features can help counter impulsive buying behaviors."
    - "Financial literacy programs should target social media and promo influence to improve spending habits."
  limits:
    - "The study is geographically limited to Cantilan, Philippines, reducing generalizability."
    - "Self-reporting may introduce bias in measuring impulsive buying tendencies."
    - "The study does not account for moderating variables like income, financial literacy, or self-control."
  mapping_rationale: A systematic scan was performed across all 12 functional domains and their associated topic codes. The paper was flagged for relevance in the domains of Filipino Cultural Context (1.A, 2.D), Expense Categorization (3.C), Existing Systems (4.A), Behavioral Profiling (5.A), Budget Recommendation (7.D), and Data Privacy (10.B). Topic 1.A is high as the study focuses squarely on Filipino Gen Z. Topic 5.A is medium as it profiles impulsive buying, a key behavioral trait. Topic 10.B is medium due to the significant role of trust in driving behavior. Topic 3.C and 7.D are low/contextual, as the study justifies the need for user constraints and behavioral interventions but does not directly address them. Topics like 2.B (Seasonal Spending) and 2.C (User-Declared Preferences) were rejected as the paper does not address cyclical patterns or explicit user preferences. Topic 6.A (Forecasting) and 8.A (Anomaly Detection) were rejected as the paper does not involve predictive modeling or detection algorithms. The overall relevance is moderate, as the paper provides strong behavioral insights that inform the design of Odin's user-facing and behavioral modules, but is not directly algorithmic.
limitations:
  - "The study's cross-sectional design prevents establishing causality between cashless payments and impulsive buying. [unacknowledged]"
  - "The generalizability of findings to other regions or demographics within the Philippines is limited due to the localized sample. [unacknowledged]"
  - "Potential self-report bias may affect the accuracy of reported impulsive buying tendencies. [unacknowledged]"
  - "The study does not examine the role of financial literacy or income as moderating variables. [unacknowledged]"
remember_this:
  - "Cashless payments strongly correlate with impulsive buying among Filipino Gen Z."
  - "Trust and security perception is the most influential factor on impulse buying."
  - "Males are more susceptible to convenience, promotions, and security cues."
  - "User demographics like gender should inform personalized financial nudges."
  - "Impulse-delay features within payment systems can mitigate overspending."
```