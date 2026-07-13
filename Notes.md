### Original Notes (Preserved)

- No PFMS in the related literature explicitly formally defined threshold for income stability and obligation weight. The researchers can define it themselves with validation from the SME.
    - Most literature define thresholds for other indicators like financial vulnerability and poverty likeliness. 
- Obligation weight DOES get affected by proportion of income to expenditure. A small gap between leads to high vulnerability to income or obligation changes. Income stability does not get affected, because an increase in obligation expenses does not equate to a shift in income frequency or amount. 
- Here's the plan: the researchers will formally define the thresholds for income stability and obligation weight themselves, since the comprehensive review of the related literature has turned up NO studies that explicitly or implicitly define thresholds for the dimensions (the closest ones we have are about credit score risks, poverty indicators, loan risks), provided that the thresholds the researchers will formally define will be validated and verified by the SME.
    - The researchers can develop samples of users with varying income stability and obligation weight features, and have the SME classify them.
    - Need ruleset from SME to determine criteria for income stability and obligation weight.
- Add to the limitations/disclaimers of the thesis that the dataset represents the general population of the NCR, since PUFs are anonymized (stripped of personal identifiers like age or employment type)
- In generation of expense transaction data, we can randomly distribute it along the days of a month. The RRL supports that we distribute it more on 1-2 days after paydays & before/during holidays. It also supports that we distribute it less on a few days or a week before payday. A lot of the plus/minus variations in spending is discretionary; essentials largely remain the same throughout
- Propose to use this data modeling method: generate user personas, add variations to their financial behavior using statistical curves (e.g. LogNormal, Gamma)

---

### ADDENDA: Additional Context, Justification, and Implementation Details

**On Note 1 (Thresholds & Literature Gap):**

> **ADDENDUM 1.1 – Categorizing Existing Thresholds for Contrast**  
> The thresholds found in the related literature can be grouped into two types: **(a) absolute thresholds** (e.g., the PSA's official poverty threshold of PhP 12,030 per capita per annum, or the World Bank's $2.15/day international poverty line), and **(b) probabilistic thresholds** (e.g., credit scoring models where a PD > 5% flags high default risk, or loan-to-value ratios > 80% flag high mortgage risk). Neither type addresses the **frequency and composition** of income and expenses—they are outcome-oriented, not behavior-oriented. By defining our own thresholds, we are not contradicting the literature; we are extending it into a new domain (personal financial management for young adults), making this a novel contribution of the thesis.

> **ADDENDUM 1.2 – SME Validation Protocol (Double-Blind Sorting)**  
> The SME validation process shall follow a structured protocol:
> 1. **Sample Generation**: The researchers will generate a matrix of 30–50 synthetic user profiles, each described by 8–10 key features (e.g., monthly income, income sources, total essential expenses, total discretionary expenses, number of income streams, occupation type, etc.).
> 2. **Blind Sorting**: The SME will be given these profiles (anonymised, randomly ordered) and asked to sort them into two piles for *income stability* (Stable vs. Variable) and two piles for *obligation weight* (Flexible vs. Obligated), without any pre-defined criteria.
> 3. **Rule Extraction**: After sorting, the researchers will perform a **CART (Classification and Regression Tree)** analysis on the features to extract the decision rules the SME implicitly used (e.g., "If REG_SAL / TOINC > 0.65, classify as Stable"). 
> 4. **Consensus Refinement**: The extracted rules will be presented back to the SME for refinement and adjustment, resulting in a **formal, documented ruleset** that becomes the operational definition for the thesis.

---

**On Note 2 (Obligation Weight vs. Income Stability – Orthogonality):**

> **ADDENDUM 2.1 – Definition of Financial Slack**  
> We define `Financial Slack = (TOINC - TOTEX) / TOINC` as the proportion of income remaining after all expenses. A low positive Financial Slack (e.g., < 5%) indicates high vulnerability, because even a minor obligation increase forces reallocation from essential to discretionary (or leads to deficit). This vulnerability is **moderated** by income stability: a Stable profile with low Slack can adjust gradually, but a Variable profile with low Slack faces immediate crisis risk.

> **ADDENDUM 2.2 – Mathematical Orthogonality Justification**  
> Let `IS = f(Variance(Income_Sources))` and `OW = g(Essential / Total)`. Since `IS` measures the **coefficient of variation** of inflows, and `OW` measures the **proportion of outflows** to a fixed class (essentials), changes in `OW` do not automatically change `IS`—a user's income can remain volatile (low IS) even if they reduce their essential spending (low OW). Our modeling will treat `IS` and `OW` as independent dimensions, while acknowledging their interaction through a **moderation analysis** (i.e., we will test if the effect of OW on budget feasibility is stronger for Variable users than for Stable users).

---

**On Note 3 (Formal Definition & Ruleset from SME):**

> **ADDENDUM 3.1 – Candidate Ruleset Structure**  
> The final ruleset from the SME will likely take the following form:
> 
> **Income Stability Rules (Binary):**
> - *Stable*: `(REG_SAL + PENSION) / TOINC >= X%` AND `(SEASON_SAL + EAINC) / TOINC <= Y%` (where X and Y are derived from SME sorting).
> - *Variable*: Otherwise, or if `CASH_ABROAD` + `SEASON_SAL` accounts for > Z% of income.
>
> **Obligation Weight Rules (Binary):**
> - *Obligated*: `(FOOD + HOUSING_WATER + HEALTH + EDUCATION + TRANSPORT) / TOTEX >= W%`
> - *Flexible*: Otherwise.
>
> These candidate thresholds will be refined during the SME validation session.

> **ADDENDUM 3.2 – Documenting the SME Validation**  
> The thesis will include a dedicated appendix titled *"Expert Validation of Financial Behavioral Profile Thresholds"* containing:
> - The anonymised profiles presented to the SME.
> - The SME's classifications.
> - The extracted CART decision tree.
> - The final agreed-upon ruleset, signed off by the SME.

---

**On Note 4 (Limitation: Anonymised PUF Represents General NCR):**

> **ADDENDUM 4.1 – Impact on Model Generalizability**  
> Since the training data cannot be filtered by age or employment type, the classification model will learn patterns from the *general* NCR adult population. At inference time (during app onboarding), the model receives the user's self-reported age and employment type as input features. If the model was trained without these features, it must rely on spending patterns alone. To mitigate this gap, we will:
> - Use the pre-survey to compute **calibration weights** that upweight synthetic personas that match the target demographic (20‑40, working).
> - Conduct a **sensitivity analysis** to test model performance on a held‑out synthetic set that matches the target demographic (generated separately).
> - Explicitly state in the thesis: *"The model is trained on NCR‑wide spending patterns, but is expected to perform on the target demographic because spending patterns of working young adults in NCR are a subset of the broader NCR patterns, and the model receives age/employment as features at inference to offset the training‑inference covariate shift."*

> **ADDENDUM 4.2 – Pre-Survey as a Constraint on Persona Prevalence**  
> The pre‑survey (100 respondents) will be used to estimate the **prevalence of each FBP** among the target demographic. If, for example, the pre‑survey shows that 60% of respondents are Variable‑Flexible, but the FIES general NCR sample shows only 20%, we will **resample** the FIES-based personas with weights that make the synthetic population match the pre‑survey distribution. This ensures the synthetic training data is not just "any NCR household," but statistically resembles the target audience.

---

**On Note 5 (Expense Distribution: Payday & Holidays vs. Essentials):**

> **ADDENDUM 5.1 – Formalizing the Temporal Weighting Function**  
> Let `d` be the day of the month (1–31). Define a base daily weight `w_base(d)` that reflects payday and holiday cycles:
> 
> | Day Range | Category | Weight Multiplier |
> |---|---|---|
> | 1–2 (Post‑15th payday), 15–17 (Post‑30th payday) | Payday Splurge | 1.4 – 1.6 |
> | 24–25, 30–31, key holidays (Dec 24, Dec 25, Dec 31, Jan 1, Holy Week) | Holiday Boost | 1.3 – 1.8 |
> | 11–14 (Pre‑15th payday), 26–29 (Pre‑30th payday) | Cash‑Depletion Dip | 0.4 – 0.6 |
> | All other days | Normal | 0.9 – 1.1 |
> 
> **Category‑Specific Modifiers**:
> - **Essential expenses** (FOOD, HOUSING_WATER, HEALTH, EDUCATION): The weight range is **narrowed** to 0.8–1.2, reflecting that these are inelastic.
> - **Discretionary expenses** (RECREATION, DURABLE, OCCASION, CLOTH): The weight range is **widened** to 0.3–2.0, reflecting that these are highly elastic and absorb most of the cash‑depletion and payday effects.
> - **Semi‑discretionary** (TRANSPORT, COMMUNICATION): Weight range is 0.6–1.5, as some transport is mandatory (commute) but some is leisure‑related.

> **ADDENDUM 5.2 – Implementation in the Synthesis Pipeline**  
> After generating the monthly total for a category, we allocate it to days using the following steps:
> 1. Compute `w_total = sum(w_day * modifier_category)` over all days of the month.
> 2. For each day, allocate `amount_day = monthly_total * (w_day * modifier_category) / w_total`.
> 3. This ensures the sum of daily allocations equals the monthly total exactly.
> 4. For transactional generation, we then split each day's amount into one or multiple transactions (using Poisson distribution for count, and Gamma for per‑transaction amount).

---

**On Note 6 (Persona-Based Microsimulation with LogNormal/Gamma):**

> **ADDENDUM 6.1 – Persona Hierarchy Definition**  
> The personas will be defined in a **two‑tier hierarchy**:
> - **Tier 1 (Macro Persona)**: Defined by the combination of:
>   - FBP (4 types: Stable‑Flexible, Stable‑Obligated, Variable‑Flexible, Variable‑Obligated).
>   - Income tercile (Low, Medium, High, based on `PERCAPITA`).
>   - *Total: 4 × 3 = 12 base personas*.
> - **Tier 2 (Micro Variation)**: For each of the 12 personas, we fit a **multivariate LogNormal distribution** to the vector of category totals (e.g., `[BREAD, MEAT, FISH, TRANSPORT, ...]`), preserving the covariance matrix observed in the FIES data for that persona. This ensures that generated users have realistic cross‑category correlations (e.g., high food spending tends to co‑occur with high housing spending).

> **ADDENDUM 6.2 – Parameter Estimation from FIES Macrodata**  
> For each persona `p` and each category `c`:
> - `μ_{p,c}` = mean of the six‑month total across all FIES records in that persona.
> - `σ_{p,c}` = standard deviation.
> - `ρ_{p,c1,c2}` = correlation coefficient between categories c1 and c2.
> 
> We then fit a multivariate LogNormal using the `scipy.stats.multivariate_normal` method after applying the LogNormal transformation (i.e., log‑transform the data, compute mean vector and covariance matrix, then use these to generate synthetic samples).
>
> **Distribution Assignment**:
> - **Six‑month totals**: Sampled from the persona‑specific multivariate LogNormal.
> - **Monthly totals**: Obtained by dividing the six‑month total by 6, then using a Dirichlet(1) to allocate across 6 months while preserving the sum constraint.
> - **Transaction frequency**: For each category, `λ = monthly_total / average_unit_price_estimate`. Since we lack actual unit prices in the PUF, we estimate average unit price from the FIES questionnaire metadata (using the unit price fields recorded in the survey, though not present in the PUF). Alternatively, we assume a fixed average unit price per category derived from the **national average retail prices** published by the PSA (available in separate publications).
> - **Transaction amount**: Sampled from a **Gamma distribution** with shape = 2 and scale = (monthly_total / frequency) / 2. (The Gamma(2) gives a plausible right‑skewed distribution of daily purchase amounts.)

> **ADDENDUM 6.3 – Linking Pre‑Survey Data to Personas**  
> The pre‑survey (100 respondents) will be used to:
> 1. **Estimate persona prevalence**: We will ask the pre‑survey respondents enough questions (e.g., employment type, income stability perception, essential expense perception) to approximate their FBP. This gives us a **target distribution** over the 12 personas.
> 2. **Compute importance weights**: For each persona `p`, we compute `weight_p = prevalence_in_pre‑survey / prevalence_in_FIES`. These weights are then used during synthetic user generation (i.e., we sample personas with probability proportional to `weight_p`).
> 3. **Validate synthetic distributions**: We will compare the income distribution of the generated synthetic users (after applying weights) against the income distribution of the pre‑survey. If they match, we have statistical evidence that our synthesis is capturing the target demographic.

> **ADDENDUM 6.4 – Justification for Distribution Choices**  
> - **LogNormal**: Chosen because financial quantities (expenditure totals) are positive, bounded by zero, and typically right‑skewed with a long tail. LogNormal is the standard distribution for income and expenditure in household surveys (e.g., the World Bank's Living Standards Measurement Study uses LogNormal for consumption).
> - **Gamma**: Chosen for transaction amounts because it is flexible (can model exponential, right‑skewed, or even symmetric shapes), positive, and is standard in inventory and purchase modeling.
> - **Dirichlet**: Chosen for monthly allocation because it ensures the sum constraint is exactly preserved, which is critical when generating monthly values that must sum to the six‑month total.
> - **Poisson**: Chosen for transaction frequency because it models count data (number of purchases) with a single parameter, is widely used in retail and consumption modeling, and can be easily extended to Negative Binomial if overdispersion is observed.

> **ADDENDUM 6.5 – Pilot Generation and Validation**  
> Before generating the full training set (e.g., 10,000 virtual users), the researchers will conduct a **pilot run** generating 100 virtual users. The pilot will be validated by:
> - Checking that for each persona, the mean generated category totals match the FIES persona means within ±10%.
> - Checking that the generated daily time series, when aggregated back to monthly totals, show the expected payday/holiday spike patterns.
> - Presenting the pilot-generated daily series to the SME for a face‑validity check (i.e., "Do these patterns look like a typical Filipino young adult's spending?").

---

### Summary of the Complete Data Synthesis Pipeline (Including Additions)

| Step | Action | Data/Method | SME Involvement |
|---|---|---|---|
| 1 | Filter FIES to NCR, Urban (`URB=1`). | FIES PUFs | None |
| 2 | Compute `Financial Slack` and other derived features. | FIES aggregates | None |
| 3 | Generate candidate thresholds for IS and OW. | Candidate ruleset (proposed) | **Phase 1**: Review proposed thresholds. |
| 4 | Blind sorting of synthetic profiles by SME; extract rules via CART. | SME classifications + CART | **Phase 2**: Perform blind sorting. |
| 5 | Finalise thresholds and define 12 personas. | SME‑validated ruleset | **Phase 3**: Approve final ruleset. |
| 6 | Fit multivariate LogNormal per persona. | FIES aggregates | None |
| 7 | Calibrate persona weights using pre‑survey. | Pre‑survey (100 respondents) | None |
| 8 | Generate synthetic virtual users with personas. | Sample from multivariate LogNormal | None |
| 9 | Apply temporal weighting (payday/holiday). | Defined weight function | SME face‑validity check (pilot) |
| 10 | Inject anomalies for training detector. | Fixed rates (3‑5% overspending) | None |
| 11 | Export training datasets (tabular + time series). | Final output | None |