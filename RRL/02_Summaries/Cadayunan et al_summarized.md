```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: local
title: A Descriptive-Correlational Analysis of Social Media Usage and Personal Finance Competencies Among University Students
authors: Cadayunan, A. M. G.; Fabe, A. C. M.; Tingabngab, G. T.; Bagtong, S. M. D.
year: 2025
venue: Unknown
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 5.C
tldr: Social media usage among university students correlates moderately with higher self-reported financial literacy and decision-making abilities, but a knowledge-to-action gap persists in budgeting and impulse control.
problem_and_motivation: Social media's influence on financial competencies among Filipino university students is not well understood. While digital platforms can disseminate financial information, they also expose users to consumer-driven content that may undermine sound financial behavior. This gap in localized research hinders the development of targeted financial education strategies.
approach:
  - A quantitative descriptive-correlational design was used to examine the relationship between social media usage and personal finance competencies.
  - The sample comprised 173 BSBA students from Bukidnon State University - Talisayan Campus, selected via stratified random sampling.
  - A structured questionnaire with Likert scales measured social media usage (platform preference and frequency) and financial competencies (literacy and decision-making).
  - Data collection involved direct distribution of pre-validated surveys to participants over a two-week period.
  - Descriptive statistics and Pearson's product-moment correlation (r) were used to analyze the data, with a two-tailed significance test (p).
findings:
  - num: Social media usage is high, with Facebook and TikTok being the most preferred platforms among students.
  - Students reported high self-perceived financial literacy but lower scores in practical application, such as budget adherence and regular saving.
  - Financial decision-making abilities were rated as moderate, with difficulties reported in resisting impulse purchases.
  - num: A moderate positive correlation was found between social media frequency and financial literacy (r=0.359, p<.001).
  - num: A moderate positive correlation was found between social media frequency and decision-making abilities (r=0.361, p<.001).
  - The moderate correlation suggests that social media's educational potential is countered by its commercial, impulse-driven nature.
key_figures_tables:
  - Table 2: Correlation between social media usage and financial competencies → Moderate positive correlation exists for both literacy and decision-making.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: PFMS
    definition: Personal Finance Management System.
  - term: BSP
    definition: Bangko Sentral ng Pilipinas, the central bank of the Philippines.
  - term: BSBA
    definition: Bachelor of Science in Business Administration.
critical_citations:
  - "[Sarmiento et al., 2025] — Found social media impacts Filipino student financial literacy."
  - "[Subburayan et al., 2023] — Confirms social media as a tool for digital financial literacy."
  - "[BSP, 2022] — Provides national context on financial inclusion goals."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Directly studies university students, a core demographic for Odin's target users.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Explores financial competencies and behaviors of students transitioning to financial independence.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Highlights the knowledge-to-action gap in financial behavior.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Provides a localized study on Filipino students' financial competencies.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Mentions social media's role in consumer exposure, relevant to spending triggers.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: Contextual framing on social media's influence on consumer behavior.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Does not directly review PFMS but discusses the need for financial education tools.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies a gap in translating financial knowledge into practical behavior.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Discusses behavioral aspects like impulse buying and budget adherence.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: contextual
      justification: Background on student financial behavior, relevant to initial user profiling.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Does not propose classification, but provides behavioral data.
  contribution: This paper provides empirical evidence on the relationship between social media usage and financial competencies among Filipino university students, which can inform Odin's user modeling module (1.A, 1.B). The finding of a moderate correlation validates the use of digital platforms for financial literacy dissemination, supporting Odin's engagement strategies (11.A). The identified knowledge-to-action gap and difficulties with impulse buying and budget adherence directly justify the need for Odin's behavioral nudging and budget recommendation features (3.C, 7.B).
  directly_justifies:
    - Social media can be leveraged for financial education campaigns targeting Odin's user base.
    - Students' difficulty with impulse purchases highlights the need for in-app behavioral controls.
    - The knowledge-to-action gap justifies Odin's focus on actionable budgeting tools.
    - The positive correlation supports the use of social media-like engagement mechanics in Odin.
  limits:
    - Self-reported data on financial competencies may not reflect actual abilities.
    - The sample is limited to BSBA students from a single campus, limiting generalizability.
    - The study is correlational, so no causal relationship can be established.
    - Does not specify which specific social media content influences financial behavior.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was conducted. The paper was flagged as highly relevant to domains concerning the Filipino user demographic (1.A, 1.B), as it directly studies university students' financial competencies. It provided medium relevance to behavioral profiling (5.A) and existing systems gaps (4.B) by highlighting the knowledge-to-action gap and behavioral challenges like impulse spending. Borderline cases included the paper's mention of seasonal spending and occasions (2.B, 2.D), which was assigned contextual relevance as it only mentions consumer exposure without specific analysis of cycles. Domains related to algorithmic modules (forecasting, anomaly detection, budget recommendation) and design (mobile, privacy) were considered and rejected as the paper offers no insights into these technical areas. Overall, the paper is relevant for establishing the behavioral baseline and challenges of Odin's target users but offers little for the system's algorithmic design.
limitations:
  - Self-reported financial literacy may overestimate actual knowledge. [unacknowledged]
  - The sample is limited to business administration students from one campus. [unacknowledged]
  - The study cannot establish a causal link between social media and financial competencies.
  - The specific types of financial content consumed on social media were not analyzed.
remember_this:
  - Social media use correlates with higher self-reported financial literacy.
  - Students know financial concepts but struggle to apply them in practice.
  - Resisting impulse purchases is a significant challenge for students.
  - The correlation between social media and financial skills is moderate.
  - The knowledge-to-action gap is a critical design problem for Odin.
```