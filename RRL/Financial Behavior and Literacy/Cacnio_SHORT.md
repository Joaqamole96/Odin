---
name: research-summary
source_document: "DP202413.md"
designation: local
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[ ]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
summary_date: 2026-04-23
version: "1.0"
---

# How does financial literacy affect financial behavior over the life cycle? Evidence from Filipino households

## TL;DR (One Sentence)
Higher financial literacy reduces the likelihood of spending within income but increases retirement planning and insurance uptake across age groups.

## Core Problem & Motivation
Does financial literacy affect short‑term (spending, loans) and long‑term (retirement, insurance) financial behaviors differently across life stages? Prior studies focus on developed countries; this study uses Philippine data to inform targeted financial education.

## Methods / Approach (Bulleted)
- **Data:** 2018 BSP Consumer Finance Survey (7,084 households, income ≥₱10k, spending ≥₱1k).
- **Financial Literacy Index (FLI):** Two equal components (0.5 each): **Financial Attitude** (money/spending attitude, risk attitude, time discounting) and **Financial Aptitude** (loan score, deposit score, surplus score). Scores scaled [0,1].
- **OLS regression** to identify FLI determinants (age, gender, income, education, children, remittances).
- **Logit regressions** (odds ratios) for five binary financial behaviors: spending ≤ income, paying loans on time, loan‑to‑income ≤1, having pension/retirement plan, having insurance.
- **Age groups:** Young adult (18‑39), Middle‑aged (40‑59), Senior (60+).

## Key Findings / Results (Numbered or Bulleted)
1. **FLI scores:** Young adults highest (0.392), middle‑aged (0.387), seniors lowest (0.370).  
2. **Determinants:** Education (+) and income (+) most influential; females slightly lower FLI (−0.005). Having children (+) and receiving remittances (+) increase FLI.  
3. **Spending behavior:** Higher FLI reduces odds of spending ≤ income (odds ratio 0.435 for attitude, 0.051 for aptitude). Middle‑aged and seniors also less likely to spend within income (0.610 and 0.667).  
4. **Loan payment:** Higher financial attitude increases odds of paying on time (**OR = 4.011**).  
5. **Loan‑to‑income ratio:** Middle‑aged are **less likely** to have ratio ≤1 (OR 0.280) vs. young adults – they take bigger loans (e.g., houses).  
6. **Retirement/pension plans:** Higher financial aptitude strongly increases odds (OR **85.48**). Middle‑aged (OR 1.281) and seniors (OR 3.663) more likely to have plans.  
7. **Insurance:** Higher financial aptitude (OR 46.81) and senior age (OR 2.113) increase odds. Education, children, remittances also positive.

## Important Figures & Tables (Condensed)
- **Figure 1:** Knowledge → Literacy → Behavior → Well‑being chain. *Takeaway: financial literacy is the bridge from knowledge to action.*  
- **Table 2:** FLI mean = 0.386; financial aptitude (0.099) much lower than attitude (0.673). *Key: Filipinos have positive attitudes but low aptitude (loans, deposits, surplus use).*  
- **Table 5 (OLS):** Education coefficient +0.015 (largest positive); senior coefficient −0.018 (largest negative). *Education boosts literacy; old age reduces it slightly.*

## Equations to Remember

$$ FLI_i = \frac{1}{2}\sum_{j}^{n}x_{ij}\gamma_{j1} + \frac{1}{2}\sum_{j}^{n}x_{ij}\gamma_{j2} \in [0,1] $$

*Financial Literacy Index = weighted average of attitude and aptitude sub‑scores. Higher = more literate.*

## Definitions & Acronyms

| Term/Acronym | Definition |
|--------------|------------|
| **FLI** | Financial Literacy Index (0 to 1) |
| **CFS** | Consumer Finance Survey (BSP, 2018) |
| **Financial Attitude** | Component measuring money mindset, risk tolerance, time preference [think: ‘willingness to plan’] |
| **Financial Aptitude** | Component measuring actual financial actions (loans, deposits, surplus allocation) [think: ‘doing not just knowing’] |
| **OLS** | Ordinary Least Squares regression |

## Critical Citations
- **[Lusardi & Mitchell, 2014]** – Foundational link between financial literacy and retirement planning.  
- **[Huston, 2010]** – Defines financial literacy as knowledge + skills + application (used for Figure 1).  
- **[Magante et al., 2023]** – Methodology for constructing FLI from CFS data (directly adapted).

## Limitations & Assumptions
- **Causality direction:** Assumes literacy → behavior; reverse causality possible (behavior → literacy).  
- **Missing financial knowledge questions:** CFS lacks numeracy/knowledge items; FLI relies on attitude+aptitude only.  
- **Self‑report bias:** Savings and debt amounts may be under‑reported.  
- **Sample restricted:** Only households with income ≥₱10k and spending ≥₱1k; excludes very poor.

## Takeaway for Memory (≤ 3 bullet points)
- 🔑 **Aptitude > Attitude for long‑term actions** – Higher financial aptitude (not just attitude) boosts retirement plan odds **85×** and insurance odds **47×**.  
- 💡 **Middle‑aged take bigger loans** – They are **72% less likely** to have loan/income ≤1 than young adults (buying houses).  
- 📌 **More literacy, more spending?** – Higher FLI linked to spending **more** than income (*not* a typo; possibly due to higher consumption or confidence to use credit).