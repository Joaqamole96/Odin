Thank you for the detailed clarifications. I will incorporate all of them into the draft and add research/RRL notes where concrete values or targets are not yet established.

---

# DRAFT — ARTICLE V. RANDOM FOREST CLASSIFIER

## Section 1. Overview

1. The Random Forest Classifier is the System's primary mechanism for assigning a Financial Behavioral Profile (FBP) to each user.

2. The classifier shall be implemented using the Random Forest ensemble learning method, which constructs multiple decision trees during training and outputs the mode of the classes (classification) or mean prediction (regression) of individual trees.

3. The classifier shall support both **cold-start classification** (using onboarding questionnaire data only) and **standard classification** (using onboarding data + transaction history).

4. The classifier shall provide **explainability** via SHAP (SHapley Additive exPlanations) values to communicate to users which features most influenced their classification.

---

## Section 2. Architecture

### 2.1. Ensemble Configuration

1. The Random Forest Classifier shall be configured with the following hyperparameters:

| Hyperparameter | Value | Justification |
|----------------|-------|---------------|
| Number of Trees (n_estimators) | **100** | Standard baseline for Random Forest; balances performance and computational cost |
| Maximum Depth (max_depth) | **10** | Prevents overfitting while capturing sufficient complexity |
| Minimum Samples Split (min_samples_split) | **5** | Ensures splits are based on meaningful sample sizes |
| Minimum Samples Leaf (min_samples_leaf) | **2** | Prevents leaf nodes from being too specific |
| Maximum Features (max_features) | **sqrt** | Standard practice for classification problems |
| Criterion | **Gini Impurity** | Standard for classification; computationally efficient |
| Bootstrap | **True** | Enables bagging for variance reduction |
| OOB Score | **True** | Enables out-of-bag evaluation for validation |

> **[RESEARCH NOTE]** The hyperparameters above are initial baselines derived from standard Random Forest implementations (scikit-learn defaults) and related works in financial classification. Hyperparameter tuning via Grid Search or Randomized Search shall be performed during algorithm prototyping to optimize for the target dataset. The tuned hyperparameters shall be documented in Appendix E of the thesis manuscript.

### 2.2. Training Data

1. The classifier shall be trained on a dataset comprising:
   - **Onboarding questionnaire responses** (declared features)
   - **Transaction history features** (derived from actual transactions)
   - **Ground truth labels** (manually validated FBP assignments from synthetic data and/or pilot users)

2. The training dataset shall be generated using synthetic data derived from:
   - BSP Consumer Finance Survey (CFS) 2021
   - PSA Family Income and Expenditure Survey (FIES) 2018
   - Pre-survey of 50–100 Filipino working young adults (optional)

3. The training dataset shall be balanced across all four FBP classes to prevent class imbalance bias.

### 2.3. Feature Engineering Pipeline

1. The classifier shall process input features through the following pipeline:

   2.3.1. **Feature Encoding:**
      - Categorical features (employment type, income frequency, location) shall be one-hot encoded.
      - Ordinal features (age bracket, number of dependents) shall be label encoded.
      - Continuous features (income amount, obligation ratio) shall be standardized (mean=0, std=1).

   2.3.2. **Feature Selection:**
      - Feature importance shall be computed during training to identify the most predictive features.
      - Features with importance below a threshold (e.g., < 0.01) may be considered for removal in subsequent iterations.

   2.3.3. **Imputation:**
      - Missing values shall be imputed using median values for continuous features and mode for categorical features.

---

## Section 3. Input Features

### 3.1. Feature Categories

1. The classifier shall accept the following input features, organized into four categories:

### 3.2. Onboarding Questionnaire Features

| Feature | Type | Description | Impact on FBP |
|---------|------|-------------|---------------|
| Employment Type | Categorical | Full-time, Part-time, Self-employed, Freelancer, Business Owner, Entrepreneur, Contractual, Gig Worker | Directly influences Income Stability score. Regular employees → Stable; Independent/Fixed-term → Variable. |
| Income Frequency | Categorical | Daily, Weekly, Bi-weekly, Monthly, Quarterly, Irregular | Directly influences Income Stability score. More frequent and regular → Stable. |
| Primary Income Amount | Continuous | Monthly income in PHP | Indirectly influences Income Stability. Higher income does not imply stability, but combined with frequency provides context. |
| Number of Income Sources | Integer | Count of declared income sources | May indicate diversification. However, multiple variable sources do not necessarily imply stability. Weight shall be lower than frequency and type. |
| Fixed Obligations | Continuous | Sum of declared fixed obligations (rent, utilities, etc.) in PHP | Directly influences Obligation Level score. Higher obligations → Obligated. |
| Number of Dependents | Integer | Count of declared dependents | Indirectly influences Obligation Level. More dependents → higher necessary expenses. |
| Debt Repayment Amount | Continuous | Monthly debt repayment amount in PHP | Directly influences Obligation Level. Higher debt payments → Obligated. |
| Protected Expense Amount | Continuous | Sum of protected expense floors | Directly influences Obligation Level. Higher protected expenses → Obligated. |
| Age | Integer | User's age in years | Minimal direct impact. May serve as a proxy for life stage and typical obligations. Weight shall be low. |
| Location | Categorical | Metro Manila city/municipality | Minimal direct impact. May serve as a proxy for cost of living variations. Weight shall be low. |

### 3.3. Transaction-Derived Features

| Feature | Type | Description | Impact on FBP |
|---------|------|-------------|---------------|
| Income Consistency Score | Continuous (0–1) | Measure of regularity of income intervals | Directly influences Income Stability. High consistency → Stable. |
| Income Variance | Continuous | Standard deviation of income amounts | Directly influences Income Stability. Low variance → Stable. |
| Obligation Ratio | Continuous (0–1) | (Essential + Obligatory expenses) / Total expenses | Directly influences Obligation Level. High ratio → Obligated. |
| Expense Volatility | Continuous | Standard deviation of monthly expenses | Indirectly influences both dimensions. High volatility may indicate variable spending patterns. |
| Savings Rate | Continuous | (Income - Expenses) / Income | Indirectly influences Obligation Level. Low savings rate may indicate high obligations. |
| Average Transaction Count | Integer | Average number of transactions per month | Indirectly signals financial activity level. May be used for confidence weighting. |
| Recurring Expense Ratio | Continuous | Recurring expenses / Total expenses | Indirectly influences Obligation Level. Higher ratio → higher fixed obligations. |

### 3.4. Derived/Computed Features

| Feature | Type | Description | Impact on FBP |
|---------|------|-------------|---------------|
| Income Predictability Score | Continuous (0–1) | Composite of consistency and variance | Directly influences Income Stability. Higher predictability → Stable. |
| Financial Burden Score | Continuous (0–1) | Composite of obligation ratio, debt ratio, and dependency ratio | Directly influences Obligation Level. Higher burden → Obligated. |
| Confidence Weight | Continuous (0–1) | Measure of data sufficiency for transaction-derived features | Used to weight transaction-derived features vs. onboarding features. Lower confidence → greater reliance on onboarding. |

### 3.5. Feature Discussion

1. **Employment Type vs. Income Consistency:**
   - Employment type is a **proxy** for income stability, not a direct measure.
   - A self-employed individual may have highly stable income, while a part-time employee may have variable hours.
   - Therefore, employment type shall bear **less weight** than actual income consistency scores derived from transaction history.
   - Employment type shall primarily serve as a **cold-start fallback** when insufficient transaction data exists.

2. **Number of Income Sources:**
   - Multiple income sources do not automatically imply stability.
   - Example: A user with three freelance clients (all variable) has lower stability than a user with one full-time salary.
   - Therefore, the number of income sources shall be **contextualized** with the consistency scores of each source.
   - Weight shall be moderate.

3. **Age and Location:**
   - Age may serve as a weak proxy for life stage (e.g., older users may have more obligations).
   - Location may serve as a weak proxy for cost of living.
   - However, these are **indirect** and **low-impact** features.
   - They shall be included for exploratory analysis but shall bear low weight in the final model.

4. **Feature Weighting Philosophy:**
   - **High Weight:** Income Consistency, Income Variance, Obligation Ratio, Fixed Obligations
   - **Medium Weight:** Employment Type, Income Frequency, Debt Repayment Amount, Number of Dependents
   - **Low Weight:** Age, Location, Number of Income Sources (when not contextualized)
   - **Variable Weight:** Confidence Weight (adjusts based on data sufficiency)

---

## Section 4. Cold-Start Classification

### 4.1. Definition

1. Cold-start classification occurs when the System must assign a Financial Behavioral Profile to a user who has **insufficient transaction history** for reliable transaction-derived feature computation.

2. Insufficiency is defined as:
   - Fewer than **X** income transactions **OR**
   - Fewer than **Y** days of transaction history

> **[RESEARCH NOTE]** The specific thresholds (X income transactions, Y days) for cold-start vs. standard classification shall be determined during algorithm prototyping. Potential thresholds to evaluate:
> - 3 months of transaction history
> - 12 income transactions (weekly average)
> - 6 income transactions (monthly average)
>
> The threshold shall balance the need for reliable classification against the desire to move users to standard classification as quickly as possible.

### 4.2. Cold-Start Feature Values

1. During cold-start, the following features **cannot** be computed from transaction history and shall be **imputed**:

| Feature | Cold-Start Value | Justification |
|---------|------------------|---------------|
| Income Consistency Score | 1.0 (if employment type is Regular Employee), else 0.5 | Assumes regular employment is stable; independent/fixed-term is uncertain |
| Income Variance | 0.0 (if Regular Employee), else 0.3 | Assumes stable employment has no variance; others have moderate variance |
| Obligation Ratio | Declared obligations / Declared income | Uses onboarding declarations |
| Expense Volatility | 0.5 (default moderate) | Cannot compute; assume moderate volatility |
| Savings Rate | (Declared income - Declared obligations) / Declared income | Uses onboarding declarations |
| Recurring Expense Ratio | 1.0 (all declared obligations assumed recurring) | Assumes all declared obligations are recurring |
| Income Predictability Score | Derived from employment type + income frequency | Uses onboarding declarations |
| Financial Burden Score | Derived from declared obligations + dependents + debt | Uses onboarding declarations |
| Confidence Weight | 0.0 (no transaction data) | Signals that all features are imputed/declared |

2. The **Confidence Weight** value (0.0 during cold-start) shall signal the classifier to:
   - Weight onboarding-based features more heavily
   - Apply lower confidence to the final classification

### 4.3. Cold-Start Classification Logic

1. The Random Forest Classifier shall execute during cold-start with imputed feature values.

2. Additionally, a **rule-based fallback** classification shall be computed as a sanity check:

```
IF Employment Type IS Regular Employee AND Income Frequency IS Monthly/Weekly:
    Income Stability = Stable
ELSE IF Employment Type IS Independent/Fixed-Term OR Income Frequency IS Irregular:
    Income Stability = Variable
ELSE:
    Income Stability = Variable (default)

IF (Declared Fixed Obligations + Declared Debt + Protected Expenses) / Declared Income > Threshold:
    Obligation Level = Obligated
ELSE:
    Obligation Level = Flexible

FBP = Income Stability + Obligation Level
```

> **[RESEARCH NOTE]** The Obligation Ratio threshold that separates Flexible from Obligated shall be determined during algorithm prototyping. Candidate thresholds: 0.60, 0.65, 0.70. This threshold shall be validated against synthetic data distributions.

3. If the Random Forest classification and the rule-based fallback classification **differ**, the System shall:
   - Display both classifications to the user during onboarding
   - Provide the Random Forest classification as the primary recommendation
   - Allow the user to choose either classification via Manual Override

4. The rule-based fallback ensures that even if the Random Forest model produces an unexpected classification due to imputed features, the user is not left without a coherent explanation.

---

## Section 5. Standard Classification

### 5.1. Definition

1. Standard classification occurs when the System has **sufficient transaction history** for reliable transaction-derived feature computation.

2. Sufficiency is defined as:
   - At least **X** income transactions **AND**
   - At least **Y** days of transaction history

### 5.2. Standard Feature Values

1. During standard classification, all features shall be computed from:
   - Onboarding data (as baseline/reference)
   - Transaction history (primary source)
   - Derived/computed features (from transaction history)

2. The **Confidence Weight** shall be computed based on:
   - Number of transactions (more → higher confidence)
   - Time span of data (longer → higher confidence)
   - Consistency of data patterns (less variance → higher confidence)

3. Confidence Weight shall range from 0.0 to 1.0, with 1.0 indicating full confidence in transaction-derived features.

### 5.3. Standard Classification Logic

1. The Random Forest Classifier shall execute with all features computed from transaction history.

2. The rule-based fallback shall be **superseded** by the Random Forest classification, as transaction history provides more reliable information than onboarding declarations.

3. However, if the Random Forest classification and the onboarding-based classification differ significantly, the System shall:
   - Flag this discrepancy for user notification
   - Present both classifications with explanations
   - Allow the user to select their preferred profile

### 5.4. Periodic Reclassification

1. Standard classification shall be re-executed at periodic intervals (see Article IV, Section 5).

2. The System shall compare the new classification with the user's current active profile.

3. If the classification changes, the System shall notify the user as specified in Article IV, Section 5.2.

---

## Section 6. Output

### 6.1. Classification Output

1. The classifier shall output the following:

| Output Field | Description | Type |
|--------------|-------------|------|
| Financial Behavioral Profile | Stable-Flexible, Stable-Obligated, Variable-Flexible, Variable-Obligated | String |
| Income Stability Score | Continuous value (0–1) representing the probability of being Stable | Float |
| Obligation Level Score | Continuous value (0–1) representing the probability of being Obligated | Float |
| Confidence Score | Continuous value (0–1) representing confidence in the classification | Float |
| Feature Importance | Top 5 features and their SHAP values | Dictionary |

### 6.2. Explainability Output (SHAP)

1. For every classification, the System shall generate SHAP explanations.

2. The SHAP explanation shall include:
   - Top 5 features that most contributed to the classification
   - Direction of contribution (increased or decreased likelihood of each class)
   - Magnitude of contribution (SHAP value)

3. The SHAP explanation shall be presented to the user in natural language:

   *"You were classified as Stable-Obligated because:*
   - *Your income consistency score is high (0.92) → Stable*
   - *Your obligation ratio is high (0.74) → Obligated*
   - *Your fixed obligations are above average for your income level → Obligated*
   - *Your income variance is low → Stable*
   - *Your savings rate is below the threshold for your profile → Indicator of obligations"*

4. SHAP explanations shall be accessible from:
   - FBP Overview Screen
   - Onboarding Results Screen (during initial classification)

---

## Section 7. Evaluation

### 7.1. Performance Metrics

1. The Random Forest Classifier shall be evaluated using the following metrics:

| Metric | Description | Target |
|--------|-------------|--------|
| Accuracy | Overall classification accuracy | To be determined* |
| Precision (macro) | Average precision across four classes | To be determined* |
| Recall (macro) | Average recall across four classes | To be determined* |
| F1-Score (macro) | Harmonic mean of precision and recall | To be determined* |
| AUC-ROC | Area under ROC curve (one-vs-rest) | To be determined* |

> **[RESEARCH NOTE]** Performance targets for the Random Forest Classifier shall be derived from related works in financial behavioral profiling. Candidate targets from comparable studies:
> - Accuracy: ≥ 85%
> - F1-Score: ≥ 0.80
>
> These targets shall be validated against baseline models (Logistic Regression, Decision Tree) to demonstrate improvement. The specific targets shall be finalized during algorithm prototyping and documented in the thesis manuscript.

### 7.2. Validation Methodology

1. The classifier shall be validated using:
   - **Hold-out validation:** 80% training, 20% testing
   - **Cross-validation:** 5-fold stratified cross-validation
   - **OOB evaluation:** Out-of-bag samples during training
   - **Walk-forward validation:** For time-series transaction features

2. The evaluation shall be performed on synthetic data and optionally on pilot user data.

---

## Section 8. Fallback Mechanisms

### 8.1. Classification Failure

1. If the Random Forest Classifier fails to produce a classification (e.g., model loading error, insufficient features), the System shall fall back to:

   **Level 1 Fallback: Rule-Based Classification** (as defined in Section 4.3)

   **Level 2 Fallback: Default Profile**
   - Assign the user to Variable-Flexible as the most conservative default
   - Notify the user of the fallback and recommend manual selection or retaking the questionnaire

2. The failure and fallback shall be logged for monitoring and debugging.

---

## Section 9. SHAP Explainability Integration

### 9.1. Explanation Generation

1. The System shall use SHAP TreeExplainer for the Random Forest model.

2. For each prediction:
   - The SHAP values for all features shall be computed
   - The top 5 features by absolute SHAP value shall be extracted
   - Natural language explanations shall be generated from the SHAP values

### 9.2. Explanation Presentation

1. SHAP explanations shall be presented in two formats:

   1.1. **Simplified View (User-Friendly):**
   - Natural language sentences describing the top features
   - Visual indicator (arrows: ↑ increased chance, ↓ decreased chance)

   1.2. **Detailed View (Technical):**
   - SHAP summary plot (beeswarm or bar chart)
   - Feature importance values
   - Available via "Show Details" or "Technical Explanation" toggle

2. The System shall use SHAP to explain classification decisions at:
   - Initial onboarding (Onboarding Results Screen)
   - Periodic reclassification (notification + FBP Overview)
   - Manual classification override (confirmation dialog)

---

## QUESTIONS FOR ARTICLE VI — FINANCIAL BEHAVIORAL PROFILE CLASSIFICATION PROCESS

Before I draft **Article VI**, please confirm the following:

1. **Process flow diagram:**
   - Would you like me to include a flowchart or process diagram in this article? Or keep it as pure text/prose?

2. **Manual classification flow:**
   - When a user selects Manual Classification, does the System:
     - A) Immediately apply the selected profile and update the active profile?
     - B) Prompt for confirmation with a comparison of current vs. selected profile?
   - Should the user provide a reason for manual override (e.g., "I don't agree with the system's classification because...") for tracking purposes?

3. **Questionnaire classification flow:**
   - When a user retakes the questionnaire:
     - Should the System use the Random Forest model with the new questionnaire responses (but no transaction history if it's a new user)?
     - Should the System use the Random Forest model with the new questionnaire responses + existing transaction history (if it's an existing user)?
   - Should the System display the previous profile before the questionnaire results are shown?

4. **Standard classification flow details:**
   - Does the Standard Classification process happen on a schedule (e.g., every 30 days) or triggered by events (e.g., after a certain number of new transactions)?
   - Is there a cooldown period between reclassification checks to prevent rapid flip-flopping?