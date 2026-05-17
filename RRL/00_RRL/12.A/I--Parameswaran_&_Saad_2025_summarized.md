# DEVELOPMENT AND EVALUATION OF MY MONEY MANAGER: AN INTELLIGENT MOBILE APP FOR PERSONALIZED FINANCIAL INSIGHT

## Metadata

```yaml
---
paper_id: "10.32890/jdsd2025.3.2.9"
designation: international
title: "DEVELOPMENT AND EVALUATION OF MY MONEY MANAGER: AN INTELLIGENT MOBILE APP FOR PERSONALIZED FINANCIAL INSIGHT"
authors: "Parameswaran, S.; Saad, S. Z."
year: 2025
venue: "Journal of Digital System Development"
odin_topics: ["3.A", "3.B", "4.A", "4.B", "7.B", "8.A", "8.B", "9.A", "12.A", "12.B"]
shorthand_tags: ["/cat-approaches", "/pfms-intelligent-features", "/pfms-limitations", "/budget-rec-evidence", "/anomaly-behavioral-evidence", "/mobile-first-def", "/eval-pfms-applied"]
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

My Money Manager app achieved **82.8%** user agreement on reliable income/expense tracking and 74.3% reported improved financial habits through personalised insights and anomaly detection.

## Problem and Motivation

Existing personal finance apps lack intelligent expense categorisation and provide generic, one-size-fits-all advice that fails to differentiate between fixed and variable costs. This limits users' ability to detect abnormal spending and adjust financial habits effectively. Prior systems did not offer dynamic, evolving financial insights based on individual spending patterns over time.

## Approach

- Iterative and incremental (agile) development methodology with user feedback integration.
- Android mobile app built with Model-View-Controller (MVC) architecture following Material Design.
- Core features: expense categorisation (fixed vs variable), 90‑day spending pattern analysis, anomaly detection, personalised savings recommendations.
- Financial metrics: monthly income, expenses, savings, income/expense ratio, budget status, and category percentage.
- Usability evaluation with 35 participants using a six-point Likert scale across four dimensions: App Experience, Perceived Ease of Use, Perceived Usefulness, Perceived Acceptance.

## Findings

1. **82.8%** of users agreed income and expense tracking was efficient and reliable (45.7% strongly agreed, 37.1% agreed).
2. **74.3%** reported the app encouraged more effective personal finance management (28.6% strongly agreed, 45.7% agreed).
3. **71.4%** agreed financial insights helped guide their financial decision‑making (37.1% strongly agreed, 34.3% agreed).
4. Navigation and data entry ease received **77.1%** “strongly agree” ratings; budget setting similarly at 77.1%.

- Data security confidence was low: only 11.4% strongly agreed their data was safe, and 31.4% somewhat disagreed.
- Most mixed response: viewing and understanding financial insights — 14.3% found it somewhat difficult.

## Key Figures and Tables

- Figure 7: App Experience responses → visual appeal strong (45.7% strongly agreed); task completion independence weakest (only 14.3% strongly agreed).
- Figure 8: Perceived Ease of Use → navigation, data entry, budget setting all at 77.1% strongly agree; insights comprehension lowest (37.1% strongly agree).
- Figure 9: Perceived Usefulness → tracking highest (45.7% strongly agree); insights most varied (28.6% somewhat agree).
- Figure 10: Perceived Acceptance → satisfaction high (85.7% agree/strongly agree); data security concern (31.4% somewhat disagree).
- Table 1: Ease of Use percentages → 77.1% strongly agree for navigation, add entry, set budget.
- Table 2: Usefulness percentages → 82.8% agree/strongly agree for tracking; 74.3% for habit improvement.

## Key Equations

$$ \text{Monthly Income} = \sum(\text{all income entries for selected month}) $$
*Sum of all income entries in the chosen month.*

$$ \text{Monthly Expenses} = \sum(\text{all expense entries for selected month}) $$
*Sum of all expense entries in the chosen month.*

$$ \text{Monthly Savings} = \text{Monthly Income} - \text{Monthly Expenses} $$
*Savings equals income minus expenses.*

$$ \text{Category Percentage} = \left( \frac{\text{Category Expense}}{\text{Monthly Expenses}} \right) \times 100 $$
*Percentage of total spending contributed by a single category.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Fixed expenses | Regular, essential costs such as rent or loan payments that do not vary month to month. |
| Variable expenses | Discretionary costs such as entertainment or dining out that fluctuate with user behaviour. |
| Anomaly detection | Identification of spending that deviates from a user’s established historical pattern. |
| Financial insights | Data‑driven recommendations and visualisations derived from spending patterns over time. |
| MVC | Model-View-Controller — a software architecture pattern separating data, interface, and control logic. |

## Critical Citations

- [Shaikh et al., 2022] — Identified key gaps in mobile financial services, including failure to differentiate fixed vs variable expenses.
- [Mijić & Ćebić, 2023] — Applied UTAUT2 model to personal finance apps; provides theoretical basis for adoption factors.
- [Carlin et al., 2022] — Demonstrated that mobile apps improve financial behaviour by reducing barriers to data access.

## Relevance to Odin

**Topics:**

3.A — Expense Categorization Frameworks

3.B — Expense Category Design Considerations

4.A — Landscape of Existing Personal Finance Systems

4.B — Limitations and Gaps in Existing Systems

7.B — Budget Recommendation in Personal Finance Systems

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

9.A — Mobile-First Design Principles and Rationale

12.A — Evaluation Frameworks for Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly validates Odin’s core design decisions by demonstrating that users value intelligent expense categorisation (fixed vs variable) and anomaly detection for improving financial habits — with 74.3% of participants reporting better money management. The evaluation results (82.8% for tracking reliability) provide benchmark usability expectations for a manual‑entry PFMS. The identified weakness in data security confidence (only 11.4% strongly agreed data was safe) reinforces Odin’s need for privacy‑by‑design and transparent security communication. The mixed user response to financial insights (14.3% found them difficult to interpret) justifies Odin’s investment in clearer data visualisation and onboarding.

**Directly justifies:**

- “82.8% of users in a 35‑participant evaluation confirmed that income and expense tracking was efficient and reliable for monitoring daily financial activities.”
- “74.3% of users reported that personalised budget planning and savings recommendations encouraged more effective financial management.”
- “Anomaly detection and spending pattern analysis over a 90‑day window provided actionable insights, though 14.3% of users struggled to interpret the visualisations.”
- “Data security confidence was a critical concern: only 11.4% of users strongly agreed their financial data was safe, with 31.4% expressing some disagreement.”

**Limits of relevance:**

- Study conducted in Malaysia; cultural spending priorities and income structures may differ from Filipino young professionals.
- Evaluation used custom Likert scales, not ISO 25010 or SUS, limiting direct comparability with Odin’s planned evaluation framework.
- No longitudinal data; retention and behaviour change measured only at a single point.
- No ML algorithm details; the “intelligent” features rely on basic statistical calculations rather than advanced models.

## Limitations

- Small sample size (n=35) limits generalisability of percentage findings. [unacknowledged]
- No longitudinal follow‑up; cannot assess whether improved habits persist over time. [unacknowledged]
- Evaluation relies entirely on self‑reported perceptions, not objective financial outcomes (e.g., actual savings increase).
- Security and trust findings may be influenced by the study’s use of a QR‑linked .apk file rather than official app store distribution. [unacknowledged]
- The paper does not disclose how the anomaly detection algorithm was implemented or validated, making replication difficult.

## Remember This

- 🔑 **82.8%** of users found income/expense tracking reliable — manual entry can be highly trusted.
- 💡 **74.3%** reported better financial habits from budget planning and savings advice.
- 📌 Only **11.4%** strongly agreed data was secure — trust is the weakest link in PFMS adoption.
- ⚠️ 14.3% struggled with financial insights — visualisation clarity matters as much as accuracy.
- 🧠 Anomaly detection and 90‑day pattern analysis drove value, but cold‑start performance unmeasured.
