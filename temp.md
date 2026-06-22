

---



---

## ===== Article IV. FBP Structure =====

### Section 1. Financial Behavioral Profile Dimensions

1. There are **two binary dimensions** that define the four FBPs: **Income Stability** and **Obligation Weight**.

2. **Income Stability** is defined as the capacity of the user's inflow to maintain a **stable amount and frequency** in regular intervals over time. It captures the predictability and reliability of the user's income stream.

   - 2.1. A user with **high Income Stability** (classified as **Stable**) receives income in predictable amounts at regular intervals (e.g., monthly salary).
   - 2.2. A user with **low Income Stability** (classified as **Variable**) experiences significant fluctuations in income amount or irregular intervals (e.g., freelancers with project‑based pay).

3. **Obligation Weight** is defined as the **proportion of the user's necessary expenses** (sum of Essential and Obligatory expenses) to their total expenses. It captures the degree to which the user's spending is committed to non‑discretionary items.

   - 3.1. A user with **high Obligation Weight** (classified as **Obligated**) allocates a large portion of their expenses to necessities and fixed commitments.
   - 3.2. A user with **low Obligation Weight** (classified as **Flexible**) retains a larger portion of discretionary spending capacity.

### Section 2. Income Stability Score

1. The System shall determine the user's income stability from their **Income Stability Score**, a continuous value between 0 and 1.

   1.1. The System shall analyze the user's **income transaction history** to derive the following core features:
      - **Income Frequency Regularity** (coefficient of variation of income intervals)
      - **Income Amount Variance** (standard deviation of income amounts)
      - **Number of Income Sources**
      - **Income Source Diversity** (weighted mix of sources)
      - **Income Source Types** (employment, government grants, allowances, remittances, investments, etc.)

   1.2. The Income Stability Score shall be computed as a **weighted combination** of the abovementioned features. The exact weights and formula shall be determined during algorithm prototyping.

   1.3. **Thresholding**:
      - If the score meets or exceeds the threshold, the user is classified as **Stable**.
      - If the score falls below the threshold, the user is classified as **Variable**.
      - The specific threshold value shall be determined during algorithm prototyping and validated against the training dataset.

   1.4. **Cold‑Start Handling**:
      - If the user's transaction history is **insufficient** (to be defined as < 3 months or < 12 income transactions), the score shall initially be derived from onboarding data (employment type, declared income frequency, and declared primary income amount).
      - This cold‑start classification shall be flagged as provisional.

### Section 3. Obligation Weight Score

1. The System shall determine the user's obligation weight from their **Obligation Weight Score**, a continuous value between 0 and 1.

   1.1. The System shall analyze the user's **expense transaction history** to derive the following core features:
      - **Obligation Ratio** = (Essential Expenses + Obligatory Expenses) / Total Expenses
      - **Total Essential Expense Amount** (absolute PHP value, normalized)
      - **Total Obligatory Expense Amount** (absolute PHP value, normalized)
      - **Number of Dependents** (declared by the user)
      - **Category Restriction Ratio** = (Protected Categories + Locked Categories) / Total Categories

   1.2. The Obligation Weight Score shall be computed as a **weighted combination** of the abovementioned features. The exact weights and formula shall be determined during algorithm prototyping.

   1.3. **Thresholding**:
      - If the score meets or exceeds the threshold, the user is classified as **Obligated**.
      - If the score falls below the threshold, the user is classified as **Flexible**.
      - The specific threshold value shall be determined during algorithm prototyping and validated against the training dataset.

   1.4. **Cold‑Start Handling**:
      - If the user's transaction history is **insufficient** (to be defined as < 3 months or < 12 expense transactions), the score shall initially be derived from onboarding data (declared total obligations, dependents, and category restriction ratio).
      - This cold‑start classification shall be flagged as provisional.

### Section 4. Financial Behavioral Profiles

1. The four FBPs are derived from the **combination** of the user's Income Stability and Obligation Weight binary classifications:

   | Income Stability | Obligation Weight | FBP |
   |------------------|-------------------|-----|
   | Stable           | Flexible          | **Stable‑Flexible** |
   | Stable           | Obligated         | **Stable‑Obligated** |
   | Variable         | Flexible          | **Variable‑Flexible** |
   | Variable         | Obligated         | **Variable‑Obligated** |

### Section 5. Periodic Reclassification *(moved and consolidated from NOTE)*

1. The System shall perform **periodic reclassification checks** at defined intervals to ensure the user's FBP remains accurate as their financial situation evolves.

   1.1. During each check, the System shall:
      - Re‑compute Income Stability and Obligation Weight scores based on the user's updated transaction history
      - Re‑classify the user if the computed scores cross the classification thresholds
      - Notify the user of any proposed profile change

   1.2. The reclassification interval shall be determined during algorithm prototyping. Factors to consider include:
      - Data sufficiency (minimum transaction count for reliable classification)
      - Behavioral change sensitivity (how quickly the system should adapt to changing user circumstances)
      - User experience (avoiding overly frequent classification changes)

2. The user shall have **control** over the reclassification process.

   2.1. By default, the System shall **automatically apply** reclassification upon detection of a significant change in the user's profile.

   2.2. The user may **disable autonomous reclassification** via the Settings screen. When disabled:
      - The System shall still compute reclassification scores but shall **not** automatically apply changes
      - The user shall be notified of any proposed changes and may manually approve or reject them

   2.3. The user may **manually trigger** a reclassification check at any time via the FBP Overview or Settings screens.

### Section 6. Manual Override Implications *(moved and consolidated from NOTE)*

1. When a user **manually selects** a profile (Manual Classification), the following rules apply:

   1.1. The selected profile shall be applied immediately and shall become the user's active profile.

   1.2. The System shall continue to perform periodic reclassification checks in the background.

   1.3. If a reclassification check produces a profile that differs from the user's manually selected profile:
      - The System shall **not** automatically apply the reclassification
      - The user shall be notified of the proposed change via a notification
      - The user may choose to accept the reclassification, reject it, or ignore it

   1.4. The System shall retain the user's manual selection preference until the user explicitly changes it.

2. If the user disables autonomous reclassification via Settings, the System shall not apply any reclassification automatically. The user shall be notified of changes but must manually approve them.

---

## Alignment Check

| Principle | Applied in Articles 0–IV? |
| :--- | :--- |
| **Model Agnosticism** | Not directly applicable yet (handled in Article V), but Articles III and IV are written independently of any specific ML model, defining *what* the system does, not *how*. |
| **Clear Operational Definitions** | ✅ Income Stability and Obligation Weight are now rigorously defined with specific features listed. |
| **Module‑Tailored Metrics/Explainability** | Not applicable here; will be reflected in Articles V, XIX, and XXII. |
| **Resolved Notes** | ✅ Moved Income Sources (III.3) and Data Usage (III.2.4) out of limbo; moved Periodic Reclassification (IV.5) and Manual Override (IV.6) into the correct article. |
| **Offline/Online Split** | ✅ Article I explicitly states offline capability support excludes the three intelligent modules. |
| **Scope Boundaries** | ✅ iOS exclusion explicitly stated. |

---

Does this alignment meet your expectations? Once you confirm, I will proceed to **Article VI. Financial Behavioral Profile Classification Process** (and subsequently the rest of the specification, article by article).