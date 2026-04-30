# Thesis Session Handoff Document
# LSTM-Driven Spending Forecast with Financial Behavioral Profile Cold-Start

**Geographic Scope:** Metro Manila, National Capital Region (NCR), Philippines
All data, literature, income ranges, spending distributions, and noise events are scoped to Metro Manila unless explicitly noted.

---

## Table of Contents

1. [Financial Behavioral Profiles (FBPs)](#1-financial-behavioral-profiles)
2. [Related Literature — BSP Sources](#2-related-literature--bsp-sources)
3. [Data Architecture](#3-data-architecture)
   - 3.1 Category Hierarchy (2nd Node)
   - 3.2 Data Schema
   - 3.3 Dataset Splits and Record Counts
4. [Synthetic Data Generation](#4-synthetic-data-generation)
   - 4.1 Statistical Parameters per FBP per Category
   - 4.2 Distribution Choice Justification
5. [Noise Design](#5-noise-design)
   - 5.1 Noise Justification
   - 5.2 Noise Event List and Parameters
   - 5.3 Noise as Sampled Distributions
6. [Model Architecture](#6-model-architecture)
   - 6.1 LSTM vs Prophet Justification
   - 6.2 Algorithm Design
   - 6.3 Minimum Data Threshold
   - 6.4 Cold-Start Fallback and Alpha Blending
   - 6.5 Forecasting Horizons
7. [Evaluation Framework](#7-evaluation-framework)
   - 7.1 Evaluation Metrics
   - 7.2 Fine-Tune Test Set (1K)
   - 7.3 Fallback Test Set (1K)
   - 7.4 Metric Applicability Matrix

---

## 1. Financial Behavioral Profiles

Profiles are rule-based, BSP-backed, and derived from FIES NCR regional data. Classification uses two orthogonal dimensions.

Metro Manila context: High urbanization, high cost of living, and elevated rent-to-income ratios compared to national averages. Obligated ratio thresholds may sit higher than national FIES benchmarks due to higher fixed housing and transport costs in NCR. Thresholds must be validated against FIES NCR figures specifically.

**Dimension 1 — Spending Consistency:**
- Stable: Coefficient of Variation (CV) < 0.2
- Variable: CV >= 0.2

**Dimension 2 — Spending Composition:**
- Obligated: Obligated expenditure ratio > 0.5 (fixed costs dominate)
- Flexible: Obligated expenditure ratio <= 0.5 (discretionary spend dominates)

**Resulting 4 FBPs:**

| Profile | CV | Obligated Ratio | Behavioral Description |
|---|---|---|---|
| Stable / Obligated | Low | High | Predictable, fixed-cost heavy. Rent, utilities, loan payments. |
| Stable / Flexible | Low | Low | Consistent but discretionary. Regular leisure, dining, shopping. |
| Variable / Obligated | High | High | Irregular income or irregular payment of fixed obligations. |
| Variable / Flexible | High | Low | Unpredictable discretionary. Impulse, travel, high variance. |

**Rule-based classification formula:**
```
CV = σ / μ  (computed on monthly total spend over observation window)
Obligated Ratio = (Essentials + Obligatory) / Total Spend
```

Profile is assigned during onboarding once sufficient transaction history is available. Reclassification triggers when spending pattern deviates from the assigned profile for 2-3 consecutive months.

---

## 2. Related Literature — BSP Sources

All categories and financial behavioral profiles are BSP-backed. NCR/Metro Manila regional breakdowns are used where available.

| Source | NCR Applicability | What It Validates |
|---|---|---|
| BSP Financial Inclusion Survey | NCR regional breakdown available | Obligated/Flexible spending dimensions; savings behavior; financial product access per income group |
| BSP Consumer Expectations Survey | NCR respondent data available | Spending intentions and temporal behavioral patterns; seasonal spending outlook |
| BSP Payment and Settlement Systems Report | National — NCR dominates volume | Semi-monthly payroll convention (15th and 30th); payday cycle timing; electronic payment behavior; BPO sector payroll patterns |
| BSP Financial Stability Report | NCR household data available | Household debt composition; obligation-heavy spending ratios per income decile |

> Note: FIES (Family Income and Expenditure Survey) is published by the Philippine Statistics Authority (PSA), not BSP. The NCR regional breakdown of FIES is used specifically — not national averages. NCR income deciles are significantly higher than national figures and must not be substituted with national data.

---

## 3. Data Architecture

### 3.1 Category Hierarchy (2nd Node)

LSTM is fed 2nd node only. 3rd node sub-categories are out of scope for this thesis iteration.

```
Spendings  [Top Node — aggregate total]
├── Essentials          [2nd Node]
├── Obligatory          [2nd Node]
├── Discretionary       [2nd Node]
└── Financial Allocation [2nd Node]
```

**Hierarchical forecasting constraint:** Essentials + Obligatory + Discretionary + Financial Allocation = Total Spendings. Category forecasts must sum to total forecast (coherence constraint).

### 3.2 Data Schema

```
user_id         INT         Unique user identifier
date            DATE        Transaction date (daily granularity)
category        ENUM        Essentials | Obligatory | Discretionary | Financial Allocation
amount          FLOAT       Spending amount in PHP
fbp             ENUM        Stable_Obligated | Stable_Flexible | Variable_Obligated | Variable_Flexible
income          FLOAT       Monthly income (collected during onboarding)
```

One row per user per day per category. A user with no spend in a category on a given day records 0.00.

### 3.3 Dataset Splits and Record Counts

**Temporal split — never randomized for time-series data.**

**Main Dataset — 10K Users:**

| Split | Days | Period | Records |
|---|---|---|---|
| Train | 255 (70%) | Jan 1 – Sep 12 | 10,200,000 |
| Validation | 55 (15%) | Sep 13 – Nov 6 | 2,200,000 |
| Test | 55 (15%) | Nov 7 – Dec 31 | 2,200,000 |
| **Subtotal** | **365** | | **14,600,000** |

Test set intentionally covers November–December to evaluate model performance on holiday noise (13th month pay, Christmas spending).

**Fine-Tune Test Set — 1K Users:**

| Window | Days | Purpose | Records |
|---|---|---|---|
| Fine-tune simulation | 1–90 | Alpha accumulation period | 360,000 |
| Evaluation | 91–365 | Personalized forecast accuracy | 1,100,000 |
| **Subtotal** | **365** | | **1,460,000** |

**Fallback Test Set — 1K Users:**

| Window | Days | Purpose | Records |
|---|---|---|---|
| Cold-start evaluation | 1–60 | Alpha = 0, profile baseline active | 240,000 |
| **Subtotal** | **60 active** | | **240,000** |

**Grand Total:**

| Dataset | Users | Records |
|---|---|---|
| Main (Train/Val/Test) | 10,000 | 14,600,000 |
| Fine-Tune Test | 1,000 | 1,460,000 |
| Fallback Test | 1,000 | 1,460,000 |
| **Grand Total** | **12,000** | **17,520,000** |

**Storage estimates:**

| Format | Volume |
|---|---|
| Raw CSV | ~3.5 GB |
| Parquet (compressed) | ~1.0 GB |
| NumPy training array in memory | ~248 MB |
| VRAM per batch (batch=128, seq=365, features=4) | ~3.2 MB |

All three datasets include noise. Noise is not isolated to the main dataset.

---

## 4. Synthetic Data Generation

### 4.1 Statistical Parameters per FBP per Category

Extract the following from **FIES NCR regional data** per income decile, then map to FBP. Do not use national FIES averages — NCR income and expenditure levels are materially higher.

```
μ            Mean monthly expenditure per category
Median       Median monthly expenditure (more robust for right-skewed distributions)
σ            Standard deviation per category
CV           Coefficient of Variation = σ / μ
Skewness     Expected: right-skewed (long right tail from large occasional purchases)
μ_ln         Log-normal location parameter
σ_ln         Log-normal scale parameter
Obligated Ratio   Fixed spend (Essentials + Obligatory) / Total spend
Savings Rate      (Income - Total Expenditure) / Income
Engel Coefficient Food expenditure / Total expenditure
Income Range      Per FIES decile mapped to each FBP
```

**FBP-to-FIES NCR Decile Mapping (approximate):**

| FBP | CV | Obligated Ratio | Likely FIES NCR Decile | Metro Manila Context |
|---|---|---|---|---|
| Stable / Obligated | Low | High | D3–D6 | Salaried employees, fixed rent/condo amortization, regular utility bills |
| Stable / Flexible | Low | Low | D6–D9 | Mid-to-upper income, consistent lifestyle spending, dining, leisure |
| Variable / Obligated | High | High | D1–D4 | Irregular income earners (freelance, informal sector) with fixed obligations |
| Variable / Flexible | High | Low | D7–D10 | High earners with volatile discretionary spending; BPO senior staff, entrepreneurs |

Validate this mapping against actual FIES NCR decile data and adjust thresholds accordingly. NCR D1 floor income is higher than national D1 — do not cross-substitute.

### 4.2 Distribution Choice Justification

Spending data follows a **log-normal distribution**, not Gaussian.

Reasons:
- Spending cannot go below zero
- Large occasional purchases (medical, appliances, holiday) create a long right tail
- Log-normal is standard in household expenditure literature
- Engel curve literature and FIES distributions confirm right-skewed behavior

```
Amount ~ LogNormal(μ_ln, σ_ln)

where:
μ_ln = log(μ² / sqrt(μ² + σ²))
σ_ln = sqrt(log(1 + σ²/μ²))
```

---

## 5. Noise Design

### 5.1 Noise Justification

Synthetic data without Philippine-specific temporal noise will not reflect real-world spending behavior. The LSTM trained on noise-free data will fail on actual user data where payday cycles, holiday spending, and cultural events create systematic deviations from baseline distributions.

All three datasets (main 10K, fine-tune 1K, fallback 1K) must include noise to ensure:
- The pre-trained model learns to handle noise as part of the spending pattern
- Fine-tuning evaluation reflects real transition conditions
- Fallback evaluation tests cold-start accuracy under realistic conditions

Academic backing for payday and temporal spending effects: Stephens (2003), Gelman et al. (2014) — adapted to Metro Manila payroll conventions. Metro Manila's high BPO concentration introduces payroll schedule variation beyond the standard semi-monthly convention, captured in the BPO Payday Variation noise event below.

### 5.2 Noise Event List and Parameters

**Petsa de Peligro (Petya de Peligo)**
```
Trigger:     Days 10–14 and 26–30 of each month
Description: Money runs out before semi-monthly payday. Spending drops sharply.
Categories:  Essentials, Discretionary
Multiplier:  × 0.4–0.6 (spending suppression)
Applies to:  All FBPs, higher severity on Variable profiles
```

**Payday Spree**
```
Trigger:     Day 15 and Day 30/31 (±1–2 days)
Description: Semi-monthly payroll release. Immediate spending spike.
Categories:  Discretionary, Essentials
Multiplier:  × 1.8–2.5
Spike decay: Returns to baseline over 2–3 days
Applies to:  All FBPs, Flexible profiles spike harder
```

**13th Month Pay**
```
Trigger:     December 15–24 (mandated before Dec 24 per RA 6686)
Description: Legally mandated 13th month bonus equivalent to one month gross salary.
Categories:  Discretionary, Essentials spike; Obligatory users redirect to debt payment
Lump sum:    Add ~1 month income to spending pool
Multiplier:  December spending × 1.8–2.5
Applies to:  All FBPs (category allocation differs per profile)
```

**Christmas / Ber Months**
```
Trigger:     September through December (gradual ramp)
Description: Philippine Christmas season begins September. Spending escalates monthly.
Categories:  Discretionary, Essentials
Monthly multipliers:
  September:  × 1.1
  October:    × 1.2
  November:   × 1.4
  December:   × 2.0–2.5 (compounded with 13th month)
```

**Semana Santa (Holy Week)**
```
Trigger:     March or April (moveable feast — verify year)
Description: Holy Week travel and leisure spike. Some daily essentials drop (closures).
Discretionary: × 1.3–1.5
Essentials:    × 0.8
Duration:      ~5 days
```

**School Enrollment Season**
```
Trigger:     June (public schools) + October (some private)
Description: School supplies, uniforms, fees redirect household spending.
Essentials:           × 1.3–1.5
Financial Allocation: slight decrease (funds redirected)
Duration:             2–3 weeks
```

**Undas / All Saints Day (Metro Manila-specific)**
```
Trigger:     November 1–2
Description: Metro Manila residents travel to home provinces to visit graves.
             Transport and Discretionary spike (travel, food for reunion).
             Local Essentials spending drops as households leave Metro Manila.
Categories:  Discretionary × 1.3–1.6 (travel, food)
             Essentials × 0.7–0.8 (fewer local purchases)
Duration:    3–5 days including travel days
Applies to:  Variable/Flexible and Stable/Flexible profiles most affected
```

**BPO Payday Variation (Metro Manila-specific)**
```
Trigger:     Varies — weekly or bi-weekly depending on employer
Description: Metro Manila hosts the largest BPO concentration in PH.
             BPO workers (night shift, offshore-aligned) often receive
             weekly or non-standard bi-weekly salaries — not 15th/30th.
             This creates an additional intra-month spending rhythm.
Categories:  Discretionary, Essentials
Effect:      Smooths out the sharp 15th/30th payday spike for affected users
             Introduces minor weekly spending rhythm instead
Applies to:  Variable/Flexible, Stable/Flexible (higher-income BPO workers)
Note:        Affects approximately 15–20% of Metro Manila workforce
```

**Metro Manila Film Festival — MMFF (Metro Manila-specific)**
```
Trigger:     December 25 – January 7
Description: Annual Metro Manila Film Festival drives entertainment spending.
             Cinema-going surges; often compounded with post-Christmas leisure.
Categories:  Discretionary × 1.2–1.4
Duration:    ~2 weeks
Applies to:  Flexible profiles, higher-income deciles
```

### 5.3 Noise as Sampled Distributions

Noise multipliers are sampled per user, not fixed. This gives each user a slightly different behavioral response to the same event — realistic and statistically defensible.

```python
payday_multiplier      = np.random.normal(loc=2.1,  scale=0.40)
petsa_multiplier       = np.random.normal(loc=0.50, scale=0.15)
thirteenth_multiplier  = np.random.normal(loc=2.0,  scale=0.30)
christmas_multiplier   = np.random.normal(loc=2.2,  scale=0.35)
semana_multiplier      = np.random.normal(loc=1.35, scale=0.20)
enrollment_multiplier  = np.random.normal(loc=1.40, scale=0.15)
undas_disc_multiplier  = np.random.normal(loc=1.45, scale=0.20)
undas_ess_multiplier   = np.random.normal(loc=0.75, scale=0.10)
mmff_multiplier        = np.random.normal(loc=1.30, scale=0.15)
# BPO variation: applied only to ~15-20% of users flagged as BPO workers
bpo_weekly_smoothing   = np.random.normal(loc=1.0,  scale=0.10)  # flattens payday spike
```

---

## 6. Model Architecture

### 6.1 LSTM vs Prophet Justification

| Criterion | LSTM | Prophet |
|---|---|---|
| Pre-train on all users | Native — shared weights learned across 10K users | Not possible — Prophet fits each series independently |
| Fine-tune per user | Standard transfer learning — freeze early layers, retrain later layers | No equivalent — refit is a full independent model, no cross-user knowledge |
| Alpha blending | Output is a scalar — blends cleanly with profile baseline | Outputs distribution with intervals — blending discards uncertainty, awkward |
| Cold-start coverage | Profile baseline handles α=0 cleanly | Prophet with sparse data (<60 days) produces unreliable forecasts |
| Noisy Philippine data | Non-linear pattern capture — holiday spikes, petsa cycles | Handles seasonality but assumes additive/multiplicative decomposition, less flexible on sharp irregular spikes |
| Cross-user learning | Transfers patterns from 2,500 similar profile users to a new user | Zero — knows nothing about other users |

**Key decision driver:** The architecture requires a shared pre-trained model that fine-tunes per user over time. This is fundamentally transfer learning — an LSTM-native capability. Prophet cannot fulfill this requirement regardless of accuracy.

**Prophet role:** Prophet serves as a benchmark comparison model, trained on the same noisy synthetic dataset, to demonstrate LSTM superiority under Philippine noise conditions. This comparison strengthens the thesis argument.

### 6.2 Algorithm Design

**Phase 1 — Pre-training (once, on 10K users):**
- LSTM trained on all 10K users' daily spending sequences
- Learns general spending patterns: weekly cycles, payday spikes, seasonal trends
- Output: shared pre-trained weights (the population model)

**Phase 2 — Fine-tuning (per user, triggered at threshold):**
- Load pre-trained weights
- Freeze early LSTM layers (preserve general population patterns)
- Retrain later layers on individual user's transaction history
- Save personalized weights per user

```python
# Freeze early layers — general patterns
for param in model.lstm_layer1.parameters():
    param.requires_grad = False

# Fine-tune later layers — personal adaptation
for param in model.lstm_layer2.parameters():
    param.requires_grad = True
```

**Hierarchical output (coherence constraint):**
```
Step 1: Forecast total Spendings (top node)
Step 2: Forecast category shares (4 proportions summing to 1.0)
Step 3: Category forecast = Total × Share
Result: All 4 categories sum to total forecast
```

Reference: Hyndman et al. (2011), *Optimal combination forecasts for hierarchical time series.*

### 6.3 Minimum Data Threshold

| Threshold | State |
|---|---|
| 0–59 days | Cold-start: profile baseline active, α = 0 |
| 60 days | Fine-tuning begins on accumulated history |
| 60–90 days | Transition: α rising, blended forecast |
| 90+ days | Fully personalized: α = 1.0 |

60 days was selected as the minimum for LSTM fine-tuning to ensure at least 2 complete payday cycles and one full month of behavioral data per category.

### 6.4 Cold-Start Fallback and Alpha Blending

**Cold-start mechanism:**
- New user is assigned an FBP during onboarding (income collected, initial profile survey)
- Profile baseline = average spending distribution of that FBP, scaled to user income
- Income scaling: `baseline = profile_avg_spend × (user_income / avg_profile_income)`

**Blended transition formula:**
```
forecast = (1 - α) × profile_baseline + α × lstm_prediction

α = min(1.0, days_of_data / 90)
```

**Visible indicator:** UI displays personalization progress (e.g., "Forecast is 40% personalized") reflecting the current α value. Fully profile-based forecasts are labeled as not yet personalized.

### 6.5 Forecasting Horizons

| Horizon | Method |
|---|---|
| Daily | Direct LSTM sequence output — next day per category |
| Weekly | Aggregate 7 daily forecasts |
| Monthly | Aggregate 30/31 daily forecasts |

Year-ahead forecast is excluded from scope. Annual figures can be derived by summing 12 monthly forecasts if needed.

---

## 7. Evaluation Framework

### 7.1 Evaluation Metrics

**MAE — Mean Absolute Error**
```
MAE = (1/n) Σ |actual - predicted|
```
Primary metric. Interpretable in peso amounts. Not sensitive to outliers.

**RMSE — Root Mean Square Error**
```
RMSE = sqrt((1/n) Σ (actual - predicted)²)
```
Penalizes large errors (holiday spikes) harder than MAE. Good stress test for noise events.

**sMAPE — Symmetric Mean Absolute Percentage Error**
```
sMAPE = (2 × |actual - predicted|) / (|actual| + |predicted|) × 100
```
Replaces MAPE. Handles zero-spend days (Financial Allocation is not spent every day). Symmetric and academically standard. MAPE is excluded because it is undefined when actual = 0.

**MDA — Mean Directional Accuracy**
```
MDA = (1/n) Σ 1[sign(actual_t - actual_{t-1}) == sign(predicted_t - predicted_{t-1})]
```
Measures whether the model correctly predicts direction of change (up/down). Useful for trend validation independent of magnitude accuracy.

### 7.2 Fine-Tune Test Set (1K Users)

Purpose: Evaluate the improvement in forecast accuracy as fine-tuning accumulates personal data.

Evaluation protocol:
- Days 1–90: simulate fine-tuning accumulation (α rising from 0 to 1.0)
- Days 91–365: evaluate personalized forecast accuracy against ground truth
- Compare at checkpoints: day 60 (fine-tune start), day 90 (full personalization), day 180, day 365
- Report MAE, RMSE, sMAPE, MDA at each checkpoint to show accuracy improving over time

All 1K users in this set include full noise (payday, petsa, holiday, seasonal).

### 7.3 Fallback Test Set (1K Users)

Purpose: Evaluate cold-start forecast accuracy (profile baseline) before personalization.

Evaluation protocol:
- Evaluate only days 1–60 (α = 0, pure profile baseline)
- Compare profile baseline forecast against actual spending
- Report MAE, RMSE, sMAPE, MDA for each FBP separately
- Expected result: Stable/Obligated baseline is most accurate; Variable/Flexible is least accurate

All 1K users in this set include full noise.

### 7.4 Metric Applicability Matrix

| Metric | LSTM Forecast | Fine-Tune 1K | Fallback 1K |
|---|---|---|---|
| MAE | Primary | Primary | Primary |
| RMSE | Stress test | Stress test | Stress test |
| sMAPE | Relative error | Relative error | Relative error |
| MDA | Directional | Directional | Directional |
| F1-Score | Excluded | Excluded | Excluded |

F1-Score is excluded. It is a classification metric and does not apply to spending amount regression. If profile classification accuracy is evaluated separately (rule-based FBP assignment), F1 per class is appropriate in that context only.

---

*Document generated: Session handoff — thesis architecture finalized*
*Scope: Metro Manila, NCR, Philippines*
*Next steps: FIES NCR regional metric extraction per category, synthetic data generation script, noise validation against BSP NCR benchmarks*
