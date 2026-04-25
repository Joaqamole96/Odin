---
name: research-summary
source_document: "Ama.pdf"
designation: international
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[ ]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
summary_date: 2026-04-24
version: "1.0"
---

# Analysis of the Food and Income Expenditure Survey 2023 Among Filipino Households

## TL;DR (One Sentence)
Food is a necessity in the Philippines: a 1% income increase raises food spending by only 0.58%, and rural households spend more on food than urban.

## Core Problem & Motivation
Policymakers lack detailed evidence on how income, geography, and livelihood sources shape food expenditure across Filipino households. This study uses the 2023 Family Income and Expenditure Survey (FIES) to uncover spending patterns, spatial clusters, and predictors of food insecurity.

## Methods / Approach (Bulleted)
- Descriptive statistics, Gini coefficients, and Lorenz curves for income/food inequality.
- Principal Component Analysis (PCA) on 10 income sources to identify livelihood clusters.
- Spatial mapping of mean food expenditure across Philippine provinces (GADM level 1).
- Mann‑Whitney U test to compare rural vs. urban spending.
- Generalized Additive Model (GAM) for nonlinear predictors of food insecurity.
- Log‑log Engel curve regression to estimate income elasticity of food.
- Beta regression for proportion of food spent outside the home.

## Key Findings / Results (Numbered or Bulleted)
1. Mean food expenditure = **P101,708**; Gini for food (0.277) is lower than income (0.394) – food spending more evenly distributed.
2. PCA reveals five dominant income components: retail/transport, informal services, crop vs. fishing, forestry/remittances, and remittance/forestry.
3. Spatial clustering: Leyte and Bohol have highest food spending (>P120k), while Northern Luzon provinces spend P80k‑90k.
4. Rural households spend **more** on food (median P102,467 vs. P80,700) and have higher per capita income (P6,000 vs. P5,000) than urban (p < .001).
5. Food budget allocation: bread (29.5%), meat (14.8%), fish (14.2%), vegetables (7.2%), fruit (4.5%).
6. GAM: strongest predictor of food insecurity is real per capita income (s(RPCINC): edf=6.71, χ²=16,981). Urban residence lowers risk (β=-0.51). Model accuracy 90%, AUC=0.86.
7. Income elasticity of food = **0.58** – food is a necessity (Engel’s Law).
8. Higher‑income households allocate more to food outside home (β=0.72); urban and larger households allocate less.

## Important Figures & Tables (Condensed)
- Figure 1 (Lorenz curve): Food expenditure inequality is moderate, less than income inequality.
- Figure 5 (Spatial map): Visayas provinces (Leyte, Bohol) show highest food expenditure; Northern Luzon lowest.
- Figure 10 (Engel curve): Log‑log plot shows positive but inelastic relationship – slope 0.58.
- Table 1 (Descriptive stats): Mean income P332k, median P241k; mean food spending P101,708.
- Table 8 (Regression): Log‑log model R²=0.589, income elasticity 0.58 (p < .001).

## Equations to Remember
$$ \log(\text{FOOD}) = 4.177 + 0.58 \cdot \log(\text{TINC}) $$
*A 1% increase in total household income raises food expenditure by only 0.58%.*

## Definitions & Acronyms
| Term/Acronym | Definition |
|--------------|------------|
| FIES | Family Income and Expenditure Survey (Philippine Statistics Authority) |
| PCA | Principal Component Analysis – finds clusters of income sources |
| GAM | Generalized Additive Model – captures nonlinear effects |
| RPCINC | Real per capita income (in thousand pesos) |
| Engel’s Law | As income rises, the proportion spent on food falls |

## Critical Citations
- [Valera et al., 2022] – QUAIDS model for Philippine food demand with missing prices.
- [Briones, 2022] – Impact of food price shocks and government programs on nutrient intake.
- [Regmi & Meade, 2013] – Demand‑side drivers of global food security (income elasticity framework).

## Limitations & Assumptions
- Cross‑sectional data → no causal inference.
- No dietary diversity or nutritional status measures.
- Spatial analysis at provincial level misses intra‑provincial disparities.
- Self‑reported income/expenditure may have recall bias.

## Takeaway for Memory (≤ 3 bullet points)
- 🔑 **0.58 elasticity** – Food is a necessity; income rises, food spending lags.
- 📌 **Rural paradox** – Rural households spend more on food *and* have higher per capita income than urban.
- 💡 **Top predictor** – Per capita income nonlinearly drives food insecurity (lowest incomes most vulnerable).