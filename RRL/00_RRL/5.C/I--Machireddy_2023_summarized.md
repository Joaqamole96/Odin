# Data Science and Business Analytics Approaches to Financial Wellbeing: Modeling Consumer Habits and Identifying At-Risk Individuals in Financial Services

## Metadata

```yaml
---
paper_id: "8f3b7c2a-1d4e-5a6b-9c8d-7e6f5a4b3c2d"
designation: international
title: "Data Science and Business Analytics Approaches to Financial Wellbeing: Modeling Consumer Habits and Identifying At-Risk Individuals in Financial Services"
authors: "Machireddy, J."
year: 2023
venue: "Journal of Applied Big Data Analytics, Decision-Making, and Predictive Modelling Systems"
odin_topics: ["4.A", "5.A", "5.C", "6.A", "8.A", "8.B", "10.A", "10.B"]
shorthand_tags: ["/pfms-intelligent-features", "/profiling-role", "/classifier-candidates", "/forecasting-methods-survey", "/anomaly-ml-families", "/privacy-by-design", "/explainability-trust"]
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

Transaction data and digital footprints enable early detection of financial vulnerability via machine learning; **explainable AI** ensures transparent, ethical risk assessment.

## Problem and Motivation

Over-indebtedness, income volatility, and lack of savings cause financial hardship for individuals and economic instability. Traditional credit scoring uses limited static variables, missing early warning signs of distress. Prior work lacked real-time, behavioral, and ethical frameworks for consumer-centric risk management.

## Approach

- Dataset: Consumer transaction histories (credit/debit cards, bills, deposits) and digital footprints (mobile usage, subscriptions, e‑commerce).
- Feature extraction: Expense-to-income ratio, income volatility, discretionary spending %, liquidity trends, payment delinquency.
- ML models: Logistic regression, random forest, gradient boosting, neural networks, Hidden Markov Models, autoencoders, clustering (K‑means).
- Techniques: Sequence analysis, anomaly detection (unsupervised), real‑time stream processing with online learning.
- Psychological & contextual factors: Self‑control, financial literacy, life events, local economic indicators.
- Explainability: SHAP, LIME, and inherently interpretable models (decision trees, scorecards).
- Ethical framework: Three lines of defense (development, validation, audit), GDPR compliance, bias audits.

## Findings

- Transaction features (income volatility, liquidity trends, discretionary ratios) strongly predict financial distress.
- Sequence models (HMM, RNN) identify paths to crisis (e.g., income drop → increased credit → delinquency) before defaults occur.
- Unsupervised autoencoders detect spending anomalies without labeled data, solving cold‑start detection.
- Clustering produces three natural segments: financially secure, stretched, and vulnerable.
- **Explainable AI (SHAP) provides feature‑level justifications** for risk scores, enabling transparency and fairness audits.
- Ethical deployment requires explicit consent, bias testing, and human‑review triggers for adverse actions.

## Key Figures and Tables

- Figure 2: Transactional Data Modeling Pipeline → raw transactions → features → predictive models → risk insights.
- Table 3: Comparison of ML models (logistic regression to neural networks) → transparency and real‑time capability trade‑offs.
- Table 10: Consumer segments by financial traits → secure, stretched, vulnerable with distinct income and debt patterns.
- Figure 6: Financial Vulnerability Segmentation Pipeline → clustering → risk cohorts → targeted actions.
- Table 11: Vulnerability scoring dimensions → liquidity, leverage, stability, distress history, spending pressure.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| XAI | Explainable AI – techniques that make model decisions interpretable by humans. |
| SHAP | SHapley Additive exPlanations – method that attributes prediction to input features. |
| LIME | Local Interpretable Model‑agnostic Explanations – explains individual predictions via simpler surrogate models. |
| HMM | Hidden Markov Model – sequence model that infers hidden states (e.g., financial health) from observed transactions. |
| Autoencoder | Unsupervised neural network that learns normal patterns and flags deviations as anomalies. |
| Three lines of defense | Governance model: 1st line (development), 2nd line (independent validation), 3rd line (internal audit). |
| GDPR | EU General Data Protection Regulation – privacy law requiring consent, purpose limitation, and right to erasure. |

## Critical Citations

- [Salignac et al., 2019] – Foundational conceptualization of financial wellbeing as multidimensional.
- [Xiao, 2016] – Establishes consumer financial capability as a predictor of wellbeing.
- [Heiskanen, 2016] – Links problem gambling to financial distress signals used in transaction models.
- [Porter & Bowman, 2021] – Provides evidence on income shocks and safety nets during COVID‑19.

## Relevance to Odin

**Topics:**

4.A — Landscape of Existing Personal Finance Systems

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

10.A — Data Privacy and Security in Personal Finance Systems

10.B — User Trust in Personal Finance Systems

**Contribution to Odin:**

This paper directly justifies Odin’s use of transaction‑derived features (income volatility, expense ratios, liquidity trends) for behavioral profiling and risk detection. Its comparison of ML models (logistic regression, random forest, gradient boosting, neural networks) informs algorithm selection for classification, forecasting, and anomaly detection modules. The emphasis on explainable AI (SHAP) and ethical deployment (three lines of defense, privacy‑by‑design) provides a framework for building user trust and regulatory compliance, both critical for Odin’s manual‑input, mobile‑first design.

**Directly justifies:**

- "Transaction‑derived features such as expense‑to‑income ratio, income volatility, and liquidity trends are strong predictors of financial distress."
- "Unsupervised autoencoders detect spending anomalies without labeled training data, making them applicable to cold‑start user profiles."
- "SHAP‑based explainability enables transparent risk assessment, supporting user trust and regulatory compliance in financial apps."
- "The three‑lines‑of‑defense governance model (development, validation, audit) ensures ethical deployment of ML in consumer finance."
- "Clustering (K‑means) on financial behavior features produces natural segments (secure, stretched, vulnerable) that map to differentiated product interventions."

**Limits of relevance:**

- Paper is conceptual with no empirical validation; all numeric claims in figures are illustrative, not experimentally verified.
- Not specific to Filipino young professionals – income volatility patterns and cultural obligations may differ.
- Assumes access to real‑time banking APIs and open banking data, which Odin does not use (manual input only).
- Lacks treatment of cold‑start profiling for new users with no transaction history.

## Limitations

- No empirical results or performance metrics (accuracy, F1, etc.) are reported – numbers in figures are illustrative only. [unacknowledged]
- Assumes rich digital footprint data (mobile payments, social signals) not universally available in the Philippines. [unacknowledged]
- Does not address the cold‑start problem for users with sparse or no transaction history.
- Over‑reliance on external economic context (inflation, unemployment) may be impractical for a standalone mobile app.
- Ethical framework lacks concrete implementation guidance for small‑scale or resource‑constrained projects.

## Remember This

- 🔑 **Transaction features (income volatility, liquidity ratio)** – strong predictors of financial distress.
- 📌 **Explainable AI (SHAP)** – makes risk scores transparent and auditable, building user trust.
- 💡 **Unsupervised autoencoders** – detect anomalies without labeled data, solving cold‑start detection.
- ⚠️ **No empirical validation** – all numeric claims are illustrative; use as conceptual framework, not evidence of effect sizes.
- 🧠 **Three lines of defense** – governance model (dev → validation → audit) ensures ethical ML deployment.
