# Skill Document: Systematic Evaluation of Research Papers for Odin

## Purpose

This skill document provides a standardized framework for evaluating research papers to determine their importance and relevance to the **Odin Personal Finance Management System** project. Use this framework to systematically assess papers and classify them into importance tiers.

---

## Evaluation Framework

### Core Assessment Dimensions

Score each paper on the following **four** dimensions using a scale of **1 (Low)** to **5 (High)** . For papers that don't apply to a dimension, score **0** and mark as N/A.

| Dimension | Description | Weight |
|-----------|-------------|--------|
| **1. Direct Module Relevance** | How directly does the paper's findings inform one or more of Odin's core functional modules? | 35% |
| **2. Topic Scope Breadth** | How many distinct Odin modules or features does the paper provide actionable insights for? | 25% |
| **3. Empirical Foundation** | How robust is the methodology (sample size, data quality, statistical rigor, national representativeness)? | 20% |
| **4. Novelty/Uniqueness** | Does the paper provide insights not readily available from other papers in the compilation? | 20% |

---

## Dimension Scoring Rubrics

### 1. Direct Module Relevance (1-5)

| Score | Criteria |
|-------|----------|
| **5** | Provides direct, quantifiable evidence that justifies the design of a core Odin module (e.g., Behavioral Profiling, Forecasting, Budget Recommendation, Savings/Debt Management) |
| **4** | Directly examines a key user behavior or financial practice that Odin must account for |
| **3** | Provides contextual evidence that supports module design but is not a direct study of the behavior |
| **2** | Mentions relevant concepts tangentially or as background |
| **1** | No discernible connection to Odin's design |

**Core Modules Reference:**
- FBP Classification Module
- Forecasting Module
- Anomaly Detection Module
- Budget Recommendation Module
- Savings Goal Management
- Debt Management
- Expense Categorization
- Transaction Entry

---

### 2. Topic Scope Breadth (1-5)

| Score | Criteria |
|-------|----------|
| **5** | Informative for 5+ Odin modules or features |
| **4** | Informative for 3-4 modules or features |
| **3** | Informative for 2 modules or features |
| **2** | Informative for 1 module or feature |
| **1** | No clear relevance to any specific module |

---

### 3. Empirical Foundation (1-5)

| Score | Criteria |
|-------|----------|
| **5** | Nationally representative survey (e.g., BSP, PSA, PIDS) with n > 5,000 OR rigorous experimental/quasi-experimental design with robust statistical analysis |
| **4** | Large sample (n > 300) with validated instruments and appropriate statistical methods |
| **3** | Moderate sample (n = 100-300) with clear methodology |
| **2** | Small sample (n < 100) or purely qualitative with limited generalizability |
| **1** | Literature review, opinion piece, or lacks methodological rigor |

---

### 4. Novelty/Uniqueness (1-5)

| Score | Criteria |
|-------|----------|
| **5** | Provides a unique insight, counterintuitive finding, or new framework not present in any other paper in the compilation |
| **4** | Provides an important finding that is rare in the compilation |
| **3** | Provides a finding that is common but with a unique methodological contribution |
| **2** | Provides a finding that is well-represented in other papers |
| **1** | Completely redundant; adds no new insight |

---

## Importance Classification

After scoring all four dimensions, calculate the **Weighted Score**:

```
Weighted Score = (Module Relevance × 0.35) + (Scope Breadth × 0.25) + (Empirical Foundation × 0.20) + (Novelty × 0.20)
```

### Classification Tiers

| Tier | Weighted Score | Description |
|------|----------------|-------------|
| **Crucial** | 4.0 - 5.0 | Essential for module justification or design. Must be cited. |
| **Highly Important** | 3.5 - 3.9 | Provides strong supporting evidence. Should be cited. |
| **Important** | 3.0 - 3.4 | Provides useful contextual or supporting evidence. May be cited. |
| **Contextual** | 2.5 - 2.9 | Provides background but not directly actionable. Reference as needed. |
| **Low** | 1.0 - 2.4 | Minimal relevance. Can be excluded. |

---

## Output Format

Produce the following for each paper:

```markdown
### Paper [ID]: [First Author] ([Year]) - [Short Title]

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | X/5 | [1-2 sentences on which modules and why] |
| Topic Scope Breadth | X/5 | [List which modules are informed] |
| Empirical Foundation | X/5 | [Sample size, methodology, rigor] |
| Novelty/Uniqueness | X/5 | [What makes it unique] |

**Weighted Score:** X.X / 5.0
**Classification:** [Crucial / Highly Important / Important / Contextual / Low]

**Key Citeable Claims:**
- [Claim 1]
- [Claim 2]
- [Claim 3]

**Relevant Odin Modules:**
- [Module 1]
- [Module 2]

**Justification:**
[2-3 sentences on why this paper matters for Odin]
```

---

## Quick Reference: Core Odin Modules

| Module | Key Topics |
|--------|------------|
| **FBP Classification** | Income stability, obligation weight, behavioral profiles, demographic segmentation |
| **Forecasting** | Spending patterns, income volatility, seasonal/cyclical spending, time-series methods |
| **Anomaly Detection** | Overspending, unusual transactions, financial stress indicators |
| **Budget Recommendation** | Protected categories, allocation strategies, cultural constraints |
| **Savings Goals** | Saving behavior, goal setting, emergency funds |
| **Debt Management** | Debt accumulation, repayment strategies, BNPL behavior |
| **Expense Categorization** | Filipino-specific categories, PCOICOP mapping, spending breakdowns |
| **Transaction Entry** | User behavior, manual logging, recurring transactions |

---

## Agent Instructions

1. **Score Each Paper:** Apply the four dimension rubrics to every paper in the compilation.

2. **Use the Output Format:** Produce the structured output for each paper.

3. **Identify Patterns:** Look for:
   - Papers that provide evidence for multiple modules (high scope breadth)
   - Papers with nationally representative data (high empirical foundation)
   - Papers with unique or counterintuitive findings (high novelty)

4. **Synthesize:** Group important papers by the module they inform to identify which modules have the strongest and weakest empirical support.

5. **Flag Gaps:** Note if any module lacks sufficient high-quality evidence from the compilation.

---

## Example Application

### Paper 1: Romero et al. (2026) - *Financial Planning Challenges in the Gig Economy*

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 5/5 | Directly identifies five financial challenges that map to FBP, Budget Recommendation, and Savings modules |
| Topic Scope Breadth | 4/5 | Informs FBP, Budgeting, Savings, Debt, and Literacy modules |
| Empirical Foundation | 3/5 | n=200, EFA-PCA, validated questionnaire, but limited to Davao City |
| Novelty/Uniqueness | 4/5 | Unique factor analysis identifying five challenge dimensions for Filipino gig workers |

**Weighted Score:** 4.25 / 5.0
**Classification:** Crucial

**Key Citeable Claims:**
- Freelancers in Davao City face five key financial challenges: knowledge, security, stability, behavior, and insurance.
- A KMO-MSA of 0.808 confirmed the data was suitable for identifying these core financial planning challenges.
- Income instability is a primary driver of financial instability for gig workers.
- Low financial knowledge and behavior hinder freelancers' ability to plan for the future effectively.

**Relevant Odin Modules:**
- FBP Classification Module
- Budget Recommendation Module
- Savings Goal Management
- Debt Management

**Justification:**
This paper provides empirical evidence for Odin's FBP module by identifying the specific financial challenges of a key target demographic (freelancers). Its findings on income instability and financial behavior directly justify the need for flexible budgeting, forecasting, and savings features in Odin.

---

### Paper 2: Bangko Sentral ng Pilipinas (2026) - *Consumer Expectations Survey Report (Q1 2026)*

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 5/5 | Provides nationally representative baseline data for cold-start forecasting and budget recommendations |
| Topic Scope Breadth | 5/5 | Informs Forecasting, Budget Recommendation, FBP, Savings, and Debt modules |
| Empirical Foundation | 5/5 | Nationally representative survey of 5,358 households with 98.5% response rate |
| Novelty/Uniqueness | 4/5 | Provides quarterly time-series data on Filipino consumer sentiment not available elsewhere |

**Weighted Score:** 4.80 / 5.0
**Classification:** Crucial

**Key Citeable Claims:**
- Consumer confidence improved from -22.2% in Q4 2025 to -15.8% in Q1 2026.
- Saving intention index surged to 12.4%, indicating rising financial prudence.
- OFW households allocated 40.2% of remittances to savings, up from 36.4%.
- Year-ahead inflation forecast rose to 2.7%, just below the BSP's 3.0% target.
- Spending outlook for Q2 2026 declined to 40.3%, signaling cautious consumer behavior.

**Relevant Odin Modules:**
- Forecasting Module
- Budget Recommendation Module
- FBP Classification Module
- Savings Goal Management
- Debt Management

**Justification:**
This BSP survey is essential for calibrating Odin's cold-start features across multiple modules. The nationally representative data on savings intentions, spending outlooks, and income-group baselines directly supports the development of accurate baseline models for forecasting and budget recommendations.