# From Borrowing to Building: A Systematic Literature Review of Data-Driven Strategies for Cultivating Better Money Habits through Consumer Credit

## Metadata

```yaml
---
paper_id: "10.37502/IJSMR.2025.81004"
designation: international
title: "From Borrowing to Building: A Systematic Literature Review of Data-Driven Strategies for Cultivating Better Money Habits through Consumer Credit"
authors: "Oyeyemi, D. O.; Moussa, A. H.; Abioye, V. O."
year: 2025
venue: "International Journal of Scientific and Management Research"
odin_topics: ["1.C", "2.B", "5.A", "5.C", "8.A", "10.A", "10.B"]
shorthand_tags: ["/literacy-behavior-gap", "/budget-failure-points", "/calendar-spending-cycles", "/anomaly-behavioral-evidence", "/data-sensitivity", "/user-trust-behavior", "/forecasting-methods-survey"]
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[X]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---
```

## TL;DR

Synthesizes how alternative data, machine learning, and behavioral insights integrate into credit systems to foster healthier money habits while raising privacy, bias, and ethical concerns.

## Problem and Motivation

The literature lacks a systematic synthesis of how data-driven strategies within consumer credit actually cultivate better money habits rather than merely predicting risk or expanding access. Digital credit platforms increasingly shape financial behavior, making it critical to understand which interventions effectively promote responsible borrowing and repayment. No prior review had comprehensively integrated findings across alternative data sources, behavioral drivers, and information design to identify mechanisms for sustainable habit formation.

## Approach

- Systematic literature review across Scopus, Web of Science, IEEE Xplore, and Google Scholar
- Keywords: "data-driven," "consumer credit," "financial habits," "machine learning," "alternative data," "fintech," "behavioral intervention"
- Inclusion: peer-reviewed articles, conference papers, book chapters in English addressing data analytics or ML in consumer credit and their impact on financial behavior
- Exclusion: review articles, editorials, opinion pieces unless providing foundational insights
- Data extraction: study objectives, methodology, data sources, analytical techniques, findings on behavior/habit formation, limitations
- Synthesis: thematic categorization and quality assessment of methodological rigor and bias

## Findings

1. Ensemble ML models (XGBoost) **outperform logistic regression in credit classification tasks**, achieving superior accuracy, precision, recall, and ROC-AUC when trained on traditional plus alternative data.
2. Mobile phone data (usage patterns, communication stability) effectively predicts credit default for individuals lacking traditional credit histories.
3. The "statement effect" — arrival of a credit card statement — temporarily reduces spending or increases payment activity, demonstrating that information timing influences short-term behavior.

- Personality traits (conscientiousness, emotional stability, honesty-humility) correlate with responsible financial management; impulsivity predicts higher debt.
- Higher self-control is associated with lower credit card debt and greater savings; higher financial literacy correlates with better credit utilization and investment intentions.
- Mandatory disclosures show limited behavioral impact due to cognitive overload; personalized feedback loops demonstrate stronger short-term engagement and habit-promising potential.
- Ethical concerns: algorithmic bias, data privacy, "off-label" credit score use (employment, housing, insurance) risks amplifying socioeconomic inequality.

## Key Figures and Tables

- Figure 1: Timeline of consumer credit evolution → from traditional banking to AI-based adaptive platforms; each phase increased efficiency and inclusion but also complexity.
- Figure 2: Conceptual model linking personality, self-control, literacy, demographics to credit behaviors → self-control and literacy are strong predictors; demographics condition decision context.
- Figure 3: Framework from alternative data → ML models → personalized decisions → feedback → habit formation → emphasizes iterative role of data-driven interventions.
- Figure 4: Feedback loop (action → data capture → ML analysis → personalized feedback → behavior adjustment) → illustrates adaptive cycle at heart of digital platforms.
- Table 3: Comparison of logistic regression, decision trees, random forests, XGBoost in credit risk → XGBoost has highest predictive accuracy but black-box concerns.
- Table 4: Comparative effectiveness of interventions → mandatory disclosures (weak long-term), behavioral nudges (strong short-term, mixed long-term), feedback loops (promising for habits).

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Alternative data | Non-traditional information sources (mobile usage, social media, utility payments) used for credit assessment. |
| Behavioral nudge | A subtle intervention that steers decisions without restricting choice, e.g., payment reminders. |
| CCPA | California Consumer Privacy Act — includes "inferences drawn" from personal data as protected information. |
| Ensemble model | A machine learning method combining multiple algorithms to improve prediction accuracy (e.g., Random Forest, XGBoost). |
| FCRA | Fair Credit Reporting Act — U.S. law governing collection and use of consumer credit information. |
| HEXACO | A personality model measuring Honesty-Humility, Emotionality, eXtraversion, Agreeableness, Conscientiousness, Openness. |
| Mental accounting | Cognitive partitioning of money into subjective categories (e.g., tax refund vs. salary) leading to irrational decisions. |
| ROC-AUC | Receiver Operating Characteristic — Area Under the Curve; a metric for classification model performance. |
| Statement effect | Temporary reduction in spending or increase in payment activity triggered by receiving a credit card statement. |
| XGBoost | Extreme Gradient Boosting — an ensemble ML algorithm known for high predictive accuracy in credit scoring. |

## Critical Citations

- [Hershfield et al., 2015] — Foundational framework for leveraging psychological insights to encourage responsible consumer debt use.
- [Suhadolnik et al., 2023] — Empirical benchmark showing XGBoost outperforms traditional methods in credit risk assessment.
- [Zhao et al., 2022] — Identifies psycho-social and demographic factors affecting online consumer credit behavior in emerging markets.
- [Blanke, 2020] — Critical analysis of privacy protections for "inferences drawn" under CCPA and GDPR.
- [Cole et al., 2023] — Evidence that mandatory standardized disclosures often fail to improve consumer knowledge or decisions.

## Relevance to Odin

**Topics:**

1.C — Financial Behavior of Filipino Young Professionals

2.B — Seasonal and Cyclical Spending Patterns

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

8.A — Anomaly Detection in Personal Finance Systems

10.A — Data Privacy and Security in Personal Finance Systems

10.B — User Trust in Personal Finance Systems

**Contribution to Odin:**

This systematic review directly informs Odin's financial behavioral profiling module by establishing that personality traits (conscientiousness), self-control, and financial literacy are measurable correlates of responsible financial behavior — justifying the inclusion of these as classification features. The paper's synthesis of the "statement effect" and cyclical spending patterns provides a behavioral foundation for Odin's anomalous spending detection: deviations from an individual's established temporal patterns can trigger alerts, as information visibility temporarily modifies behavior. The review's critical assessment of data privacy and algorithmic bias concerns directly supports Odin's privacy-by-design mandate (RA 10173) and informs the trust-related design of explainable feedback mechanisms.

**Directly justifies:**

- "Personality traits, particularly conscientiousness and emotional stability, consistently correlate with responsible financial management and lower credit card debt levels."
- "The 'statement effect' demonstrates that the timing and visibility of financial information can temporarily alter spending patterns, supporting the use of statement-aligned anomaly detection alerts."
- "Ensemble machine learning models, especially XGBoost, outperform logistic regression in credit classification tasks when trained on diverse datasets, justifying algorithm selection for behavioral profiling."
- "Mandatory disclosures have limited behavioral impact due to cognitive overload; personalized, real-time feedback loops are more promising for long-term habit formation."
- "Mobile phone usage data can effectively predict credit default for individuals without traditional credit histories, supporting alternative data sources for cold-start profiling."

**Limits of relevance:**

- The review synthesizes studies primarily from Western and Chinese contexts; findings on personality-behavior correlations may not directly generalize to Filipino young professionals without local validation.
- The paper focuses on credit repayment behavior, not spending forecasting or budget recommendation — relevance is strongest for profiling and anomaly detection modules, weaker for forecasting.
- Digital lending platform findings assume banking integration (e.g., digital payments, credit scores); Odin relies on manual transaction input only, which may alter behavioral dynamics.
- No specific evaluation of cold-start profiling for new users with zero transaction history — a critical gap for Odin's onboarding design.

## Limitations

- Systematic review methodology synthesizes existing findings but does not present original empirical validation — causal claims remain dependent on primary studies' quality.
- Long-term behavioral impact of data-driven interventions is not rigorously evaluated in the synthesized literature, as noted by the authors themselves.
- Ethical dimensions (algorithmic bias, privacy) are articulated as concerns but not empirically investigated — frameworks for auditing fairness remain underdeveloped [unacknowledged].
- No analysis of how cultural context (e.g., Filipino family obligations, informal credit mechanisms) moderates the effectiveness of behavioral nudges or feedback loops [unacknowledged].
- The review does not address how manual transaction entry (vs. automated digital payment data) affects the "statement effect" or feedback loop efficacy [unacknowledged].

## Remember This

- 🔑 **XGBoost beats logistic regression** — ensemble models win on credit classification with diverse data.
- 📌 Statement effect: information timing changes behavior — supports anomaly alert design at statement dates.
- 💡 Self-control + literacy = lower debt — Odin's profiling must measure these as behavioral features.
- ⚠️ Mandatory disclosures fail; personalized feedback loops work — Odin needs interactive, not static, guidance.
- 🔍 No cold-start evaluation in this review — Odin's onboarding profiling remains an open gap.
