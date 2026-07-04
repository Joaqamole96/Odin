# Skill Document: Paper Categorization for Odin (Crucial, Supporting, or Irrelevant)

## Purpose

This skill enables an AI agent to review a compilation of research paper summaries and classify each paper into one of **three groups** based on its **true relevance** to the Odin Personal Finance Management System. The classification goes beyond numeric scores – it incorporates qualitative judgment about the paper’s direct applicability, novelty, empirical quality, and redundancy.

---

## Input

A **compilation document** (Markdown) produced by `Z_Compiler.py`, containing full YAML summaries for each paper. Each summary includes:

- `title`, `authors`, `year`
- `odin_topics` and `relevance.topics` with relevance levels (high/medium/low/contextual)
- `tldr`, `problem_and_motivation`, `approach`, `findings`
- `contribution`, `directly_justifies`
- `limitations`
- `designation` (local/international, algorithm‑specific or not)

---

## Output Format

Produce a Markdown document with three sections:

### 1. **Crucial Papers** (must‑include)
Papers that **directly justify or inform a core Odin module** (e.g., Behavioral Profiling, Forecasting, Budget Recommendation, Anomaly Detection, Savings/Debt Management) and are **highly empirical**, **unique**, or **specifically Filipino‑context**. These papers will be foundational to the thesis.

For each paper, provide:
- Filename
- One‑sentence justification (e.g., *“Provides nationally representative baseline for cold‑start forecasting (BSP CES).”*)

### 2. **Irrelevant / Cull** (exclude)
Papers that are:
- **Out of scope** (e.g., pure stock market prediction, corporate credit risk, agricultural economics, educational analytics)
- **Redundant** – nearly identical findings to other papers (choose the best one, cull the rest)
- **Low empirical quality** – tiny sample, no rigorous methodology, purely conceptual with no data
- **No direct connection** to any Odin module – even if they mention “financial behavior” in passing, the core contribution does not apply to PFMS design

For each paper, provide:
- Filename
- One‑sentence reason for exclusion (e.g., *“Focuses on stock prediction algorithms; no spending/forecasting relevance.”*)

### 3. **Ordinary / Supporting** (use as secondary)
Papers that are **relevant but not essential** – they provide background, context, supporting evidence, or complementary insights that can be cited but are not central to module design. They may be used to enrich the literature review but are not the primary justification for design decisions.

For each paper, provide:
- Filename
- One‑sentence justification (e.g., *“Supports the importance of financial literacy but does not directly inform algorithm design.”*)

---

## Judgement Criteria

Use the following **four‑factor framework** to evaluate each paper. Do not rely solely on the provided numeric score; apply your own reasoning.

### 1. **Direct Module Relevance**
- Does the paper provide a **specific, actionable claim** that directly influences how a module (e.g., FBP, Forecasting, Budget, Anomaly, Savings, Debt) should be designed?
- **Crucial**: Yes, it explicitly tests or justifies a core algorithm, baseline, or constraint.
- **Supporting**: It provides context or background but not a direct design input.
- **Irrelevant**: No mention or only tangential.

### 2. **Uniqueness / Novelty**
- Are the findings **new** relative to other papers in the compilation?
- **Crucial**: Unique insight not found elsewhere.
- **Supporting**: Common finding, but still useful.
- **Irrelevant**: Completely redundant – multiple papers say the same thing.

### 3. **Empirical Foundation**
- How robust is the methodology? (sample size, representativeness, rigor)
- **Crucial**: Nationally representative (e.g., BSP, PSA), large N, rigorous statistical/ML validation.
- **Supporting**: Moderate quality (e.g., n=200, survey‑based, limited geography).
- **Irrelevant**: Purely conceptual, literature review only, or no data.

### 4. **Contextual Fit**
- Does the paper specifically address **Filipino young professionals** or the Philippine financial ecosystem?
- **Crucial**: Yes, it uses Philippine data or focuses on Filipino demographic.
- **Supporting**: International but directly applicable (e.g., mental budgeting, payday effects).
- **Irrelevant**: Completely foreign context with no clear transferability.

---

## Process Steps

0. **Count total papers first** – Before reading any summaries in detail, scan the compilation document to determine the exact total number of unique paper summaries. Record this number prominently at the very top of your output (e.g., *“Total papers in compilation: N”*). This count will serve as your immutable baseline for the final verification.

1. **Scan the compilation** – read each paper’s summary (title, tldr, findings, contribution, topics).

2. **Evaluate** using the four criteria. Be **critical** – a paper with a high score might still be irrelevant if its findings are too generic or not applicable to Odin.

3. **Compare** papers within the same topic area to detect **oversaturation** (e.g., five papers all saying “financial literacy improves savings” – keep the best one or two, cull the rest).

4. **Assign** to one of the three groups.

5. **Write justification** – be concise but specific (e.g., *“Unique finding: payday salience drives overspending; directly supports payday‑alert feature.”*)

6. **Verify tally and check for duplicates** – Once all papers have been assigned, perform a strict double‑check:
   - **Deduplication**: Ensure that no filename (or paper title, if filename is missing) appears in more than one group (Crucial, Supporting, or Irrelevant). Each paper must belong to exactly one section.
   - **Summation**: Sum the counts of papers in the three groups.
   - **Validation**: This sum must exactly equal the total number recorded in Step 0.
   - At the end of your output, include a clear tally table (e.g., *“Crucial: X, Supporting: Y, Irrelevant: Z, Total: X+Y+Z = N”*) to explicitly demonstrate that the counts reconcile.

---

## Important Considerations

- **Prioritise** local (Philippine) papers over international ones when they offer similar insights, but do not ignore high‑quality international work that provides unique algorithms or frameworks.
- **Algorithm‑specific** papers (designation contains “algorithm”) are often crucial for modules like Forecasting and Anomaly Detection, but **only if** they evaluate algorithms on personal spending or behavioural data – not if they are pure stock prediction.
- **Literature reviews** are **not** inherently crucial; they can be supporting (if they synthesise relevant methods) or irrelevant (if too broad).
- **The final list should be balanced** – you may end up with ~20‑30 crucial, ~50‑100 supporting, and the rest culled.

---

## Example Output Snippet

```markdown
# Paper Classification for Odin

**Total papers in compilation: 45**  *(Step 0 baseline)*

## Crucial Papers (Must Include)

1. **Bangko Sentral ng Pilipinas-2026_summarized.md** – Nationally representative survey providing cold‑start baselines for forecasting, budget recommendations, and savings behavior.

2. **Ma C. et al_summarized.md** – Direct evidence of monthly mental budgeting and payday salience; justifies Odin’s default monthly cycle and payday‑based nudges.

3. **Cabalfin et al_summarized.md** – Quantifies vulnerability to income poverty in the Philippines; justifies savings and debt management features.

... (continue)

## Irrelevant / Cull (Exclude)

1. **Gong_summarized.md** – Stock price prediction review; no application to personal spending or budgeting.

2. **Lou et al_summarized.md** – Income prediction using CNN; does not address spending behaviour or financial planning.

3. **Mienye et al-2026_summarized.md** – Credit risk survey; corporate lending focus, not personal finance.

... (continue)

## Ordinary / Supporting (Use as Secondary)

1. **Romero et al_summarized.md** – Identifies five financial challenges for Filipino freelancers; supports behavioural profiling but does not propose algorithms.

2. **Chowdhury T. et al_summarized.md** – ML for financial literacy in Bangladesh; methodological inspiration for profiling but not directly applicable.

... (continue)

---

## Final Tally Verification *(Step 6)*

- Crucial: 10
- Supporting: 25
- Irrelevant: 10
- **Total assigned: 45** ✅ (Matches initial count of 45. No duplicates found across groups.)