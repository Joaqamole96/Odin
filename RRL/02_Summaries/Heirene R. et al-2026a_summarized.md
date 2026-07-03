```yaml
paper_id: 10.1186/s12954-026-01402-4
designation: local-algorithm-specific
title: Development of lower-risk guidelines for online sports and race betting in Australia using objective behavioural data
authors: Heirene, R. M.; Chandrakumar, D.; Fahey, G.; Huynh, E. L. Y.; Gainsbury, S. M.
year: 2026
venue: Harm Reduction Journal
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 7.D
  - 8.A
  - 8.B
  - 13.A
  - 13.B
  - 13.C
tldr: Empirically derived lower-risk guidelines for online sports betting use objective account data to define thresholds for deposits, income percentage, account numbers, and betting variety associated with reduced harm.
problem_and_motivation: Existing lower-risk gambling guidelines rely on self-reported data and are not specific to online wagering, limiting their accuracy and relevance. Online sports betting poses unique risks, yet no evidence-based thresholds exist for this growing form of gambling. This study addresses the gap by deriving limits from objective behavioural data linked to validated harm measures.
approach:
  - Surveyed 1,647 customers from two Australian online wagering sites, linking responses to six months of objective account data.
  - Used Problem Gambling Severity Index and Gambling Harm Measure to classify harmed versus unharmed participants.
  - Applied Receiver Operating Characteristic curve analyses with bootstrapping to identify optimal thresholds for eight behavioural indicators.
  - Evaluated predictive validity using weighted logistic regression models controlling for demographics and other gambling.
  - Compared newly derived limits against previously established Australian guidelines for sports and race betting.
findings:
  - num: All behavioural indicators except betting frequency achieved acceptable AUC values (≥0.60) for classifying harm.
  - num: Optimal thresholds were higher for GHM harm (e.g., ≤10% income deposited) than for PGSI harm (e.g., ≤2% income deposited).
  - num: Surpassing the deposit frequency limit (4/month) was associated with 2.60 times greater odds of PGSI harm.
  - num: Exceeding the income-deposited limit (2%) was associated with 3.78 times greater odds of PGSI harm.
  - num: Exceeding all eight limits resulted in 8.04 times greater odds of PGSI harm and 8.92 times greater odds of GHM harm.
  - Exceeding multiple limits showed a dose-response relationship with increasing odds of harm.
  - Activity-specific indicators (deposits, income deposited, number of accounts) outperformed standard indicators in predicting harm.
  - Newly derived limits showed higher accuracy than prior self-report-based limits for GHM harm classification.
  - Younger adults (≤25) required lower threshold values on most indicators to distinguish harmed from unharmed gamblers.
  - Betting frequency was not a reliable indicator of harm and was inversely associated with harm in multivariate models.
key_figures_tables:
  - Table 2: Optimal limit values and performance metrics → AUC values for deposit-based indicators were highest, suggesting strong classification ability.
  - Figure 2: Odds ratios for total limits surpassed → Exceeding more limits exponentially increases harm odds for both PGSI and GHM.
  - Figure 3: Risk curves for behavioural indicators → Deposit percentage shows steepest risk increase; betting frequency shows flattest.
  - Figure 5: Proposed "2-2-4-4 Rule" infographic → Visual summary of recommended guidelines for consumer use.
  - Table 5: Rates above limits pre- and post-survey → Harmed participants consistently more likely to surpass all thresholds.
key_equations:
  - equation: "AUC = \\int_0^1 TPR(FPR^{-1}(x)) dx"
    explanation: "Area under ROC curve measures classification ability."
  - equation: "OR = \\frac{p/(1-p)}{q/(1-q)}"
    explanation: "Odds ratio compares harm likelihood between groups."
  - equation: "Youden = sensitivity + specificity - 1"
    explanation: "Maximizes overall classification accuracy."
definitions:
  - term: PGSI
    definition: "Problem Gambling Severity Index; 9-item screening measure for gambling problems."
  - term: GHM
    definition: "Gambling Harm Measure; 16-item scale assessing harm across six life domains."
  - term: AUC
    definition: "Area Under the Receiver Operating Characteristic Curve; measure of test accuracy."
  - term: ROC
    definition: "Receiver Operating Characteristic; graphical plot of true positive rate vs. false positive rate."
  - term: OR
    definition: "Odds Ratio; measure of association between an exposure and an outcome."
  - term: "Youden index"
    definition: "J = sensitivity + specificity - 1; maximizes correct classification rate."
critical_citations:
  - "[Currie et al., 2017] — Derived low-risk limits from longitudinal Canadian data."
  - "[Dowling et al., 2021] — Established Australian low-risk limits by gambling activity."
  - "[Louderback et al., 2021] — Used objective data to derive online gambling thresholds."
  - "[Heirene et al., 2021] — Documented inaccuracies in self-reported gambling behaviour."
  - "[Young et al., 2021] — Developed Canadian lower-risk guidelines framework."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: "Study develops behavioural thresholds to classify harmed vs. unharmed gamblers, directly informing financial risk profiling."
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: "Findings on younger adults requiring lower thresholds inform how initial profiles might be calibrated for new users."
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: "Uses ROC analysis and logistic regression to classify individuals based on behavioural indicators."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: "Identifies behavioural indicators (deposit frequency, income percentage) that could serve as predictive features for forecasting spending risk."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: "Does not develop forecasting algorithms but establishes thresholds that could inform sequential data labelling for forecasting models."
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: "Proposed income-relative thresholds (≤2% deposited) can inform budget allocation strategies that prioritize financial safety."
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: "Provides empirical justification for recommending deposit limits as a budgeting tool in PFMS."
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: low
      justification: "Dose-response analysis of multiple limits suggests how infeasibility might be managed by prioritizing certain constraints."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: "Behavioral thresholds (e.g., >4 deposits/month, >2% income deposited) provide clear cut-points for flagging anomalous spending."
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: "Study identifies indicators but does not propose or evaluate anomaly detection algorithms."
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: contextual
      justification: "Limits on gambling expenditure indirectly relate to protecting savings capacity, but savings not directly measured."
    - code: 13.B
      name: Debt Management in PFMS
      relevance: contextual
      justification: "GHM includes financial strain and borrowing items, but study does not focus on debt management strategies."
    - code: 13.C
      name: End‑of‑Period Surplus as a Savings Input
      relevance: contextual
      justification: "Reduced gambling expenditure (≤2% income deposited) could increase surplus, but not explicitly modeled."
  contribution: "This paper provides empirical evidence that objective behavioural indicators, particularly deposit frequency and income-relative deposits, can effectively classify financial risk. For Odin, these findings directly justify implementing deposit-based thresholds as primary risk indicators in user financial profiles. The dose-response relationship supports a multi-constraint approach to budget recommendations where exceeding multiple limits triggers enhanced user warnings. The paper's methodological framework for deriving limits from linked survey-account data offers a template for calibrating Odin's cold-start anomaly detection. Finally, the emphasis on income-relative thresholds provides Odin with a domain-justified, personalised basis for setting spending guardrails."
  directly_justifies:
    - "Odin should monitor monthly deposit frequency with a recommended upper limit of four deposits per month."
    - "Odin should calculate and flag users who deposit more than 2% of monthly household income into discretionary spending accounts."
    - "Odin's cold-start profile for new users should apply lower behavioural thresholds for users aged 25 and under."
    - "Odin's budget recommendation module should warn users when multiple spending limits are simultaneously exceeded."
    - "Odin should prioritize deposit-based indicators over betting frequency metrics for financial risk classification."
  limits:
    - "Sample overrepresented frequent bettors and older individuals, potentially skewing limits toward heavier users."
    - "Behavioural data from only one operator may not capture full gambling activity across multiple accounts."
    - "Harm classification based on self-report may not fully capture objective financial harm or debt accumulation."
    - "Limits derived from Australian wagering context may not generalize to other spending categories or jurisdictions."
    - "Cross-sectional design limits causal inference; post-survey analysis shows persistence but not causality. [unacknowledged]"
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated canonical topic codes was conducted. The paper's core contribution on behavioural risk profiling directly flagged domains 5 (Behavioral Profiling) and 6 (Spending Forecasting) with high relevance, as the study's thresholds and classification methods provide empirical grounding for Odin's user profiling and forecasting modules. Domain 7 (Budget Recommendation) was flagged medium because the income-relative deposit limit (2%) offers a concrete, evidence-based constraint for budget allocation systems. Domain 8 (Anomaly Detection) was flagged high because the identified thresholds (e.g., >4 deposits/month) serve as direct cut-points for anomaly flagging. Domain 13 (Savings & Debt) was assessed as contextual only, since savings and debt are not directly measured or modeled. Domain 2 (Filipino Cultural Context) and Domain 3 (Expense Categorization) were rejected because the study focuses on Australian gambling behaviour without cultural or category-specific insights transferable to Filipino PFMS. Domain 9 (Mobile-First Design) and 11 (Retention & Engagement) were rejected as the study does not address user interface or engagement mechanisms. Overall, the paper provides moderate-to-high relevance for Odin's risk profiling and anomaly detection modules, with actionable thresholds that can be directly embedded into system logic."
limitations:
  - "Sample skewed toward older, more frequent bettors, limiting generalizability to casual users."
  - "Single-operator data may underestimate total gambling activity, affecting threshold accuracy."
  - "Self-report measures of harm may not capture objective financial consequences like debt or bankruptcy."
  - "Cross-sectional design prevents establishing causal thresholds for harm prevention."
  - "Findings may not generalize to non-gambling spending categories within PFMS. [unacknowledged]"
  - "Income estimates from bracketed survey responses introduce measurement error in income-relative thresholds. [unacknowledged]"
  - "The study does not evaluate the long-term stability of the proposed thresholds over time. [unacknowledged]"
remember_this:
  - "Limit monthly deposits to four to reduce gambling-related financial harm."
  - "Deposit no more than 2% of monthly household income into gambling accounts."
  - "Using three or more betting accounts more than doubles the odds of harm."
  - "Exceeding multiple spending limits compounds harm risk exponentially."
  - "Younger adults under 25 require stricter thresholds to avoid similar risk levels."
```