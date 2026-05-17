# Consumers semi-intertemporally make intertemporal decisions: insights from the payday effects

## Metadata

```yaml
---
paper_id: "8a7b6c5d-4e3f-2a1b-9c8d-7e6f5a4b3c2d"
designation: international
title: "Consumers semi-intertemporally make intertemporal decisions: insights from the payday effects"
authors: "Ma, C.; Gu, Y.; Chong, J. K."
year: 2026
venue: "Unknown"
odin_topics: ["1.C", "2.B", "5.A", "6.A", "7.A", "8.A"]
shorthand_tags: ["/budgeting-prevalence", "/income-type-behavior-diff", "/calendar-spending-cycles", "/cyclical-pattern-implications", "/profiling-role", "/profile-dimensions", "/temporal-dependency", "/per-category-forecast", "/strategy-mechanics", "/budgeting-evidence", "/anomaly-behavioral-evidence", "/overage-vs-deviation"]
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

Even without liquidity constraints, consumers self-impose a monthly mental budget renewed on paydays, causing per-trip expenditures to decrease over trips within the cycle, with an extra overshoot on paydays due to salience.

## Problem and Motivation

Standard models assume consumers solve complex long-horizon intertemporal problems, yet real-world spending exhibits simple rule-of-thumb patterns like larger purchases right after payday. Understanding these heuristics is critical for designing realistic financial behavior models. Prior work had not directly tested whether monthly mental budgeting (separate from liquidity constraints or present bias) drives within-cycle expenditure decay.

## Approach

- **Data**: 5 years of transaction records from a global cosmetic/personal-care retail chain (300 stores, 600k+ members) in a Southeast Asian country with a national payday (26th of each month).
- **Design**: Regression discontinuity (RD) around paydays with a [−12, 12] day window; customer‑day‑level and customer‑trip‑level analyses.
- **Key comparisons**: Expenditure on first trip since payday vs. later trips; payday vs. one day after payday; cash vs. credit card users.
- **Outcomes**: Per‑trip expenditure, basket size, new‑product tries, high‑end upgrades, purchase mistakes (new variety never repurchased).
- **Controls**: Customer, store, year, month, day‑of‑week fixed effects; discount rates; public holidays.

## Findings

1. **Payday effect on unconditional daily expenditure** is +4.7% (p < 0.01), driven entirely by spending more when shopping, not by higher visit probability.
2. **First trip since payday** (even on a non‑payday) is **3.3% larger** than later trips; per‑trip spending then decreases over trips within the month (Table 4).
3. **Salience effect**: Expenditure on a payday first trip is dramatically larger than on the day after payday (≈ $0.98 for credit card users), while the mental‑budget‑renewing effect is ≈ $1.19.
4. **Mistakes** (purchasing a new variety never bought again) rise **1.08% on paydays**; this increase comes from salience, not from mental‑budget renewing.
5. **Cash vs. credit card**: Credit card users show larger salience effects (45% of payday elevation) than cash users (25%); mental‑budget renewing is similar across both groups.

## Key Figures and Tables

- Figure 1: Unconditional daily expenditure around paydays → sharp spike at day 0 (payday).
- Figure 2: Conditional expenditure on store‑visit days → same spike, proving it is not driven by trip frequency.
- Figure 5: First‑trip expenditure by days since payday → drop from day 0 to day 1, then flat → salience.
- Table 4: Per‑trip expenditure over trips within a paycheck cycle → monotonic decrease (e.g., first trip $0.73 higher than second trip for credit card users).
- Figure 4: Mistakes around payday → spike only on payday, not on subsequent days.

## Key Equations

$$ \max_{B} \left[ \frac{1 - \beta^{L}}{1 - \beta} U\!\left(\frac{B}{L}\right) + \Gamma(M - B) \right] $$
*Utility of purchasing storable product equals discounted consumption utility plus the "pain" from exhausting the mental budget.*

$$ \frac{1 - \beta^{L}}{1 - \beta} \cdot \frac{1}{L} U'\!\left(\frac{B}{L}\right) - \Gamma'(M - B) = 0 $$
*First‑order condition: marginal consumption utility equals marginal pain of spending.*

$$ B^{*\prime}(M) = \frac{ \Gamma''(M - B) }{ \frac{1 - \beta^{L}}{1 - \beta} \cdot \frac{1}{L^{2}} U''(\frac{B}{L}) + \Gamma''(M - B) } > 0 $$
*Larger remaining mental budget → larger expenditure on current trip.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Mental accounting | Cognitive process where people treat money as non‑fungible across separate accounts (time periods or spending brackets). |
| Payday effect | Observed increase in spending on days when a paycheck is received. |
| Salience (of paydays) | The heightened attention to payday as a landmark, reducing self‑control and causing spending overshoots. |
| Projection bias | Mistakenly predicting future tastes by exaggerating how much they will resemble current tastes (e.g., buying a new fragrance on payday and later regretting it). |
| Storable products | Goods that can be purchased today and consumed over many future days (e.g., shampoo, fragrance, makeup). |
| Intrinsic self‑control device | Internal cognitive rule or effort that limits spending to avoid breaking a mental budget. |

## Critical Citations

- [Amador et al., 2006] — Optimal commitment device imposes a minimum savings per period; frames mental budget as a self‑control tool.
- [Thaler, 1985, 1999] — Foundational mental accounting theory; separate budgets for different spending categories and time periods.
- [Loewenstein et al., 2003] — Formal model of projection bias; used to explain why payday salience increases purchase mistakes.
- [Carvalho et al., 2014] — Payday effects in low‑income households; this paper extends by showing mental budgeting exists even without liquidity constraints.

## Relevance to Odin

**Topics:**

1.C — Financial Behavior of Filipino Young Professionals

2.B — Seasonal and Cyclical Spending Patterns

5.A — Financial Behavioral Profiles in Personal Finance

6.A — Predictive Modeling in Personal Finance Systems

7.A — Budgeting Strategies as Domain Knowledge

8.A — Anomaly Detection in Personal Finance Systems

**Contribution to Odin:**

This paper provides direct empirical evidence that consumers use **monthly mental budgets** as a rule‑of‑thumb, renewing them on paydays and letting per‑trip spending decay within the cycle. For Odin, this justifies designing the budget recommendation module around a **periodic (monthly) envelope** that resets on user‑defined income dates, rather than a static rolling budget. The documented **salience‑driven overshoot** on paydays informs Odin’s anomaly detection: such predictable spikes should be flagged as “planned anomalies” to avoid false alerts. The cash‑vs‑credit card differences support **profile‑based classification** (users with different payment modes exhibit different sensitivity to salience). Finally, the finding that per‑trip spending decays monotonically over trips provides a **temporal dependency pattern** that can be incorporated into Odin’s spending forecasting algorithm.

**Directly justifies:**

- “Consumers self‑impose a monthly mental budget that renews on paydays, causing the first shopping trip after payday to be 3.3% larger than later trips even on non‑paydays.”
- “Salience of paycheck receipt produces an additional expenditure overshoot on payday itself (e.g., $0.98 for credit card users) that is separate from mental‑budget renewal.”
- “Purchase mistakes (new varieties never repurchased) increase by 1.08% on paydays, indicating that projection bias is triggered by payday salience, not by the budget reset alone.”
- “Credit card users are more susceptible to payday salience (45% of payday elevation) than cash users (25%), while mental‑budget renewal effects are similar across payment modes.”
- “Per‑trip expenditure on storable products decreases over trips within a paycheck cycle — a pattern that can be modeled as a decreasing function of remaining mental budget.”

**Limits of relevance:**

- Study population is upper‑middle‑class consumers in a Southeast Asian country; Filipino young professionals may have different income volatility and cultural obligations.
- Data come from a single brand of storable products (cosmetics/personal care), not from general daily expenses like food or transportation.
- The paper does not evaluate any specific ML algorithm; it provides behavioral patterns that must be translated into algorithmic design choices.
- No cold‑start analysis — the mental budgeting mechanism relies on established payment cycles; new Odin users without income‑date information would need a different approach.

## Limitations

- Sample is high‑income, not representative of lower‑income Filipinos who may face real liquidity constraints. [unacknowledged]
- The study cannot fully separate mental budgeting from present bias for storable goods, though it argues present bias plays a trivial role.
- No longitudinal test of whether users actually follow the mental budget over many months; only intra‑month decay is observed.
- The brand’s loyalty program and member bias may limit generalizability to non‑member or multi‑brand shoppers. [unacknowledged]
- The stylized model assumes rational monthly planning, but the paper does not validate the model’s predictions against alternative heuristics.

## Remember This

- 🔑 **+3.3% per‑trip jump** on first visit after payday — mental budget resets even if you don’t shop on payday itself.
- 📌 Payday itself adds **$0.98 extra** (credit card) — salience, not just budget renewal, drives the spike.
- ⚠️ **Mistakes +1.08%** on paydays — users buy new varieties they later regret; projection bias matters.
- 💡 Cash users feel **25% of payday effect** from salience; credit card users feel **45%** — payment mode shapes behavior.
- 🔍 Per‑trip spending **decays over trips** within a month — treat it as a decreasing function of remaining budget in forecasting models.
