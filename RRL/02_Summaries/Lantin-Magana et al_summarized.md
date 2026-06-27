```yaml
paper_id: 3a5c6d8e-9f0b-4a2c-8b3d-6e7f8a9b0c1d
designation: local
title: Predictors of Investment Decision among Selected Individuals in Key Cities of Laguna: An Extended Theory of Planned Behavior Approach
authors: Lantin-Magana, L.; Espelita, C.A.M.H.; Calingasan-Habana, C.A.; Atento, A.G.B.; Atento, R.G.O.
year: 2026
venue: Journal of Enterprise Strategy and Management Innovation
odin_topics:
  - "1.A"
  - "1.C"
  - "5.A"
  - "5.B"
tldr: Investment decisions among Filipino urban professionals are associated with attitudes toward investing, monthly salary, capital market knowledge, and sex, with attitude and salary being the strongest predictors in a TPB-extended model.
problem_and_motivation: Investment participation in the Philippines remains limited, and decisions to invest are shaped not only by financial capacity but also by evaluative beliefs, risk appraisal, institutional trust, and perceived readiness. An exclusive focus on financial capacity is insufficient for explaining observed differences in investment participation. The study addresses the gap by examining how individual perceptions and demographic attributes relate to investment decisions.
approach:
  - Data were collected via an online survey from 483 respondents in Calamba, Santa Rosa, and Biñan, Laguna.
  - The questionnaire measured risk tolerance, attitude toward capital markets, capital market knowledge, government trust, and attitude toward investment using a 6-point scale.
  - Investment decision was self-reported using a six-point scale.
  - Descriptive statistics, group comparisons (t-test and ANOVA), Pearson correlation, and stepwise multiple regression were used to analyze associations and identify predictors.
findings:
  - Risk tolerance received the highest rating (M=4.81), while government trust received the lowest (M=3.85).
  - num: Investment decision scores differed significantly by sex (p=0.002) and by monthly salary bracket (p<0.001).
  - num: Capital market knowledge showed the highest correlation with investment decision (r=0.210, p=0.001), followed by attitude toward investment (r=0.179, p=0.003).
  - num: Attitude toward investment (coefficient 0.345) and monthly salary (coefficient 0.368) jointly explained 16.2% of variance in investment decision (R²=0.162, p<0.001).
key_figures_tables:
  - Table 1: Mean and standard deviation of risk tolerance (4.81, 1.19), attitude toward capital markets (4.60, 1.23), knowledge (4.10, 1.32), and government trust (3.85, 1.33) → Perceptions vary, with risk tolerance highest and trust lowest.
  - Table 2: Stepwise regression coefficients for attitude toward investment (0.345) and monthly salary (0.368), R²=0.162 → Attitude and salary jointly predict investment decision.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "TPB"
    definition: "Theory of Planned Behavior, a framework emphasizing evaluative beliefs, perceived control, and social influences."
  - term: "PSE"
    definition: "Philippine Stock Exchange."
  - term: "Risk tolerance"
    definition: "Disposition or capacity to accept risk exposure in investment."
  - term: "Attitude toward capital markets"
    definition: "Favorable evaluation of market participation and its benefits."
  - term: "Government trust"
    definition: "Confidence in government institutions and political climate regarding investment."
  - term: "Investment decision"
    definition: "Self-reported decision to engage in investing, measured on a six-point scale."
critical_citations:
  - "Parsai & Chandok (2025) — financial literacy review in investment decision."
  - "Salampessy & Krisnawati (2025) — influence of literacy, risk perception on investment."
  - "Akhtar & Das (2019) — predictors of investment intention in stock markets."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "medium"
      justification: "The sample is drawn from urban Filipino populations, providing demographic context for young professionals."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Directly examines financial behavior related to investment decisions among Filipino respondents."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Identifies predictors (attitude, salary, knowledge) that can inform behavioral profiling in PFMS."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "medium"
      justification: "The identified predictors could serve as initial inputs for profiling new users, addressing cold-start."
  contribution: "The paper's identification of attitude toward investment and monthly salary as key predictors informs Odin's behavioral profiling module by highlighting which user attributes are most associated with investment decisions. The correlations between capital market knowledge and investment decisions support the inclusion of financial literacy assessments in user onboarding. The significant differences by sex and income suggest that Odin's recommendation engine should consider demographic factors when tailoring financial advice. The finding that government trust is low underscores the need for trust-building features in the app."
  directly_justifies:
    - "Attitude toward investment is a significant predictor of investment decision (coefficient 0.345)."
    - "Monthly salary is a significant predictor of investment decision (coefficient 0.368)."
    - "Capital market knowledge is positively correlated with investment decision (r=0.210)."
    - "Investment decisions differ significantly by sex (p=0.002)."
  limits:
    - "Cross-sectional design prevents causal inference."
    - "Purposive sampling and online data collection may limit generalizability."
    - "Self-reported measures may be subject to social desirability bias."
    - "The model explains only 16.2% of variance, indicating omitted variables."
    - "Stepwise regression may be sensitive to sample-specific patterns."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains of Behavioral Profiling & Classification and Filipino Cultural Context were flagged as relevant. Specifically, topics 1.A (demographic context), 1.C (financial behavior), 5.A (behavioral profiles), and 5.B (profile dynamics) were selected with high or medium relevance. Borderline cases included the overlap between 1.A and 1.C, both retained due to their complementary value. Domains such as Expense Categorization, Spending Forecasting, Budget Recommendation, Anomaly Detection, Mobile-First Design, Data Privacy, User Retention, System Evaluation, and Savings & Debt Management were rejected because the paper does not address those topics. The paper provides moderate overall relevance to Odin by offering empirical evidence on behavioral predictors that can be used in profiling and personalization."
limitations:
  - "Cross-sectional design prevents causal inference."
  - "Purposive sampling and online data collection may limit generalizability."
  - "Self-reported measures may be subject to social desirability bias."
  - "The model explains only 16.2% of variance, indicating omitted variables."
  - "Stepwise regression may be sensitive to sample-specific patterns."
remember_this:
  - "Attitude toward investment and monthly salary are the strongest predictors of investment decision."
  - "Capital market knowledge shows the highest correlation with investment decision among measured constructs."
  - "Investment decisions differ by sex and income, with males and higher earners scoring higher."
  - "The model explains 16.2% of variance, indicating other determinants also matter."
```