# A Systematic Literature Review: Present Bias versus Financial Literacy as Determinants of Savings Behavior Among Entrepreneurs

## Metadata

```yaml
---
paper_id: "10.69569/jip.2025.758"
designation: local
title: "A Systematic Literature Review: Present Bias versus Financial Literacy as Determinants of Savings Behavior Among Entrepreneurs"
authors: "Aquino, E. J.; Sealmoy, R.; Mandap, O."
year: 2026
venue: "Journal of Interdisciplinary Perspectives"
odin_topics: ["1.C", "5.A", "7.B", "8.A", "11.A"]
shorthand_tags: ["/literacy-behavior-gap", "/budget-failure-points", "/profiling-role", "/anomaly-behavioral-evidence"]
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

Present bias more strongly predicts poor savings than financial literacy among entrepreneurs; knowledge improves savings only when paired with high self-control.

## Problem and Motivation

Prior systematic reviews have not compared the relative predictive power of financial literacy versus present bias on entrepreneurial savings behavior. Entrepreneurs frequently fail to save even when financially knowledgeable, undermining business sustainability. What was missing is a direct comparison of knowledge-based versus bias-based determinants within a single analytical framework.

## Approach

- PRISMA 2020 guidelines ensured transparency and reproducibility.
- Searched Google Scholar, Scopus, and Web of Science using Boolean keywords on literacy, present bias, savings, and entrepreneurs.
- Included peer-reviewed English articles from 2020–2025 with Journal Impact Factor ≥1.5, focused on entrepreneurs or entrepreneurial populations.
- Excluded conceptual papers without empirical data and non-entrepreneurial samples.
- Two independent reviewers screened titles/abstracts; 20 studies met final inclusion.
- Quality appraised using JBI and CASP checklists; synthesis was thematic comparing predictive strength.

## Findings

- **Present bias consistently overrides financial literacy as a predictor of poor savings** – even literate entrepreneurs engage in impulsive spending when present bias is strong.
- Financial literacy’s impact is conditional: it improves savings only among entrepreneurs with high self-control; without self-control, knowledge fails to translate into action.
- Self-control moderates the literacy–savings relationship, reframed as an emotional struggle (immediate rewards vs. long-term planning) rather than a simple cognitive trade-off.
- Most studies (78%) used primary data, predominantly cross-sectional surveys in Asian contexts, limiting causal claims.
- Behavioral interventions (commitment devices, automated savings, framed reminders) are more effective than financial education alone.

## Key Figures and Tables

- Figure 1: Theoretical framework contrasting Financial Literacy Pathway vs. Behavioral Bias Pathway → Present bias directly reduces savings; literacy works only via self-control.
- Figure 2: PRISMA flow diagram → 20 studies retained from initial search after screening.
- Table 1: Journal impact factors (range 1.5–8.6) → High-quality source journals strengthen evidence base.
- Table 3: Primary vs. secondary data sources → 78% primary surveys, indicating people-oriented empirical approach.
- Table 4: Statistical treatments (regression 37%, SEM 17%) → Quantitative methods dominate, enabling predictive modeling.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Present bias | Tendency to prioritize immediate rewards over future benefits, leading to impulsive spending. |
| Financial literacy | Knowledge of financial concepts (saving, investing, budgeting) assumed to drive sound decisions. |
| Self-control | Ability to resist immediate temptations in favor of long-term goals; reframed as an emotional struggle. |
| PRISMA | Preferred Reporting Items for Systematic Reviews and Meta-Analyses – a guideline for transparent reviews. |
| JIF | Journal Impact Factor – metric of journal citation influence; threshold ≥1.5 ensured quality. |
| CASP | Critical Appraisal Skills Programme – checklist for qualitative study quality assessment. |
| SEM | Structural Equation Modeling – statistical technique for testing complex mediated relationships. |

## Critical Citations

- [Loewenstein & Carbone, 2024] – Reframes self-control as emotional conflict, not simple temporal discounting.
- [Mpaata et al., 2021] – Empirically shows financial literacy only improves savings with high self-control.
- [McKenzie et al., 2022] – RCT evidence from Filipino entrepreneurs linking aspirations and financial decisions.
- [Alshebami & Al Marri, 2022] – Demonstrates savings behavior mediates literacy → entrepreneurial intention.
- [Molina-García et al., 2022] – Bibliometric review establishing financial literacy as an emerging SME research field.

## Relevance to Odin

**Topics:**

1.C — Financial Behavior of Filipino Young Professionals

5.A — Financial Behavioral Profiles in Personal Finance

7.B — Budget Recommendation in Personal Finance Systems

8.A — Anomaly Detection in Personal Finance Systems

11.A — Engagement Dynamics in Personal Finance Applications

**Contribution to Odin:**

This paper directly informs Odin’s behavioral profiling module by establishing present bias as a stronger predictor of poor savings than financial literacy – justifying inclusion of bias indicators in user profiles. For budget recommendation, the finding that literacy only works with self-control suggests Odin must embed behavioral guardrails (e.g., commitment devices) rather than assume knowledge alone changes behavior. The review also supports Odin’s anomaly detection design: present bias-driven impulsive spending represents a predictable deviation pattern that can trigger alerts. Finally, the knowledge-behavior gap explains why users may disengage despite financial education, reinforcing Odin’s value-driven retention strategy.

**Directly justifies:**

- “Present bias leads to impulsive spending even among financially literate entrepreneurs, directly reducing savings – a pattern that overrides the effect of financial knowledge alone.”
- “Financial literacy improves savings behavior only when entrepreneurs possess high self-control; without self-control, literacy fails to translate into action (Mpaata et al., 2021).”
- “Behavioral interventions – commitment devices, automated savings defaults, and framed reminders – are more effective than pure financial education in promoting savings behavior.”
- “Cross-sectional surveys dominate the literature (78% of studies), limiting causal inference about the literacy-bias-savings relationship.”
- “Present bias persists across developing economies including the Philippines, as shown in RCTs with Filipino entrepreneurs (McKenzie et al., 2022).”

**Limits of relevance:**

- The review targets entrepreneurs, whose income volatility and business expenses differ from general young professionals – direct transferability requires validation.
- Most studies are cross-sectional and Asia-focused, limiting causal claims for Metro Manila’s specific context.
- No study in the review evaluated mobile-first personal finance apps or manual transaction entry; findings come from survey and experimental contexts.
- The review does not compare specific ML algorithms (e.g., LSTM vs. GRU) for detecting present-bias-driven anomalies.

## Limitations

- Heavy reliance on cross-sectional designs (acknowledged) – cannot establish causality between present bias and savings outcomes.
- Geographical concentration in Asia (56% of studies) – may not fully generalize to other regions, though Filipino studies are present. [unacknowledged]
- No longitudinal tracking of how present bias changes over time – relevant to Odin’s profile dynamics. [unacknowledged]
- Exclusion of grey literature (conference papers, dissertations) may introduce publication bias.
- Does not address how present bias interacts with mobile UX or manual data entry friction. [unacknowledged]

## Remember This

- 🔑 Present bias overrides financial literacy – the stronger predictor of poor savings in entrepreneurs.
- 📌 Financial literacy works only with high self-control; without it, knowledge fails to change behavior.
- 💡 Behavioral tools (commitment devices, auto-savings) beat education alone – design Odin’s budget module accordingly.
- ⚠️ 78% of studies used cross-sectional surveys – limited causal evidence for real-world app deployment.
