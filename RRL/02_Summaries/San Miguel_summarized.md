```yaml
paper_id: 10.53378/iarr.924.113
designation: local
title: Investment behavior of cryptocurrency investors in Metro Manila
authors: San Miguel, E.
year: 2024
venue: Industry and Academic Research Review
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.D
  - 5.A
  - 5.C
tldr: Cryptocurrency investor behavior in Metro Manila differs significantly across age, education, income, employment, and experience, but not civil status, with social persuasion being the least differentiating factor.
problem_and_motivation: Cryptocurrency is gaining popularity among Filipinos, yet confusion and skepticism surround this asset class. Understanding the behavioral drivers and demographic differences in investment decisions is critical for informed participation and policy development.
approach:
  - A descriptive survey design was used with a self-administered questionnaire distributed online via Google Forms.
  - Data were collected from 385 self-identified cryptocurrency investors in Metro Manila using respondent-driven and purposeful sampling.
  - The instrument measured four self-efficacy sub-variables: experience, vicarious learning, social persuasion, and physiological feedback.
  - Reliability was assessed using Cronbach's alpha, with all sub-variables scoring above 0.70.
  - The Kruskal-Wallis H Test was employed to determine significant differences in behavioral factors across demographic groups.
findings:
  - All four self-efficacy sub-variables significantly affect cryptocurrency investment behavior.
  - Age, educational attainment, and years invested in cryptocurrency significantly differentiate behavior across all sub-variables.
  - Sex only significantly differentiates experience, while civil status shows no significant differences across any sub-variable.
  - Social persuasion was the only sub-variable not significantly impacted by income, employment status, or source of income.
  - Respondents with no exposure to financial management seminars or vlogs had the highest mean rank for social persuasion.
  - num: 53.25% of respondents were male.
  - num: Over 80% of respondents have invested in cryptocurrency for less than two years.
  - num: Respondents below 18 years old and those without tertiary education were most influenced by social persuasion.
key_figures_tables:
  - Table 1: Cronbach's alpha values (0.708-0.888) → Questionnaire is reliable for measuring self-efficacy.
  - Table 2: Age significantly differentiates all behavioral factors → Older investors rely more on experience.
  - Table 5: Educational attainment significantly affects all sub-variables → Higher education correlates with different behavioral drivers.
  - Table 6: Income significantly affects experience, vicarious learning, and physiological feedback → Higher income investors show different behavioral patterns.
  - Table 10: Years invested significantly affects experience, vicarious learning, and physiological feedback → Newer investors exhibit stronger physiological responses.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Self-efficacy
    definition: An individual's confidence in their ability to manage different scenarios and perform tasks.
  - term: Vicarious learning
    definition: Learning through observing the achievements or failures of others.
  - term: Social persuasion
    definition: The influence of encouragement, negativity, or trends from others, including social media, on an individual's beliefs and actions.
  - term: Physiological feedback
    definition: Physical and psychological responses experienced while performing a task.
critical_citations:
  - "[Bandura, 2002] — Foundational theory of self-efficacy used as the framework."
  - "[Lusardi, 2019] — Supports the role of education in financial literacy."
  - "[Kraaijeveld & De Smedt, 2020] — Supports the link between social media and cryptocurrency prices."
  - "[Zhao & Zhang, 2021] — Establishes the importance of investment experience over financial literacy."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: Focuses on Metro Manila investors, providing demographic insights on age, education, and income.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: contextual
      justification: Discusses income, employment, and investment sources relevant to financial structure.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Directly examines financial behavior through self-efficacy and demographic differences.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Study is situated in Metro Manila and discusses the Philippine context of cryptocurrency adoption.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: Mentions social media influence on investment timing, but not directly spending cycles.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Uses self-efficacy to profile investor behavior, a key component of behavioral profiling.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: contextual
      justification: Classifies investors based on demographic variables and self-efficacy sub-variables.
  contribution: This paper provides a foundation for understanding the demographic and behavioral drivers of cryptocurrency investment among Filipinos. The findings on self-efficacy and social persuasion can inform the design of Odin's onboarding and user profiling modules, particularly for young professionals. The identification of age and educational attainment as key differentiators can guide targeted financial education features within Odin. The study's focus on Metro Manila reinforces the need for culturally-aware design in Odin's recommendation and notification systems.
  directly_justifies:
    - "Cryptocurrency investment behavior differs significantly based on age, education, and income, supporting personalized user profiling in Odin."
    - "Social media significantly influences investment decisions, justifying the need for Odin to integrate trusted information sources."
    - "Experience is a stronger driver than formal financial literacy for high-risk investments, informing Odin's prioritization of user activity history."
    - "Newer investors experience stronger physiological feedback, which supports the need for anxiety-reducing onboarding and educational features in Odin."
  limits:
    - "The study focuses on cryptocurrency, which may not represent broader investment behavior in traditional assets."
    - "Data is self-reported and gathered during the pandemic, which may not reflect long-term behavior."
    - "The sample is limited to Metro Manila, which may not represent the diverse financial behavior across the Philippines."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains of Filipino Cultural Context, Behavioral Profiling & Classification, and Expense Categorization were flagged as relevant. Specifically, topic codes 1.A, 1.B, 1.C, and 2.A were selected with medium relevance for providing demographic and cultural context on Filipino investors. Code 5.A was assigned medium relevance for its use of self-efficacy as a profiling tool, and 5.C was assigned contextual relevance for its classification of investors by demographics. Codes 2.B (seasonal spending), 2.C (user-declared preferences), 3.A, 3.B, and 3.C (expense categorization) were considered but rejected as the paper does not address spending categorization or allocation. Codes 6.A, 6.B (forecasting), 7.A-D (budget recommendation), and 8.A-C (anomaly detection) were also rejected, as the study does not involve predictive modeling or anomaly detection. Codes 9.A, 9.B (mobile-first design), 10.A, 10.B (data privacy), 11.A, 11.B (retention), 12.A-C (evaluation), and 13.A-C (savings/debt) were not applicable. The paper's overall relevance to Odin is contextual and moderate, providing foundational behavioral insights but no direct algorithmic or system design contributions.
limitations:
  - "The study uses a non-probability sampling method (respondent-driven and purposeful), which may introduce selection bias."
  - "Causal relationships cannot be established due to the descriptive-correlational design."
  - "The study only examines four self-efficacy sub-variables, potentially omitting other relevant behavioral factors."
  - "Reliance on self-reported data may be subject to social desirability and recall bias."
  - "The generalizability of findings is limited to cryptocurrency investors in Metro Manila during the COVID-19 pandemic."
remember_this:
  - "Social persuasion equally influences all demographic groups in cryptocurrency investment."
  - "Age and education are key differentiators of financial behavior in high-risk investments."
  - "Experience drives investment behavior more strongly than formal financial literacy."
  - "Newer investors exhibit stronger physiological and emotional responses to market changes."
  - "Over 80% of surveyed investors have less than two years of cryptocurrency experience."
```