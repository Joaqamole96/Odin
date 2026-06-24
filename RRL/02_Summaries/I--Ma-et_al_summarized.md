```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international
title: Consumers semi-intertemporally make intertemporal decisions: insights from the payday effects
authors: Ma, C.; Gu, Y.; Chong, J. K.
year: 2026
venue: Unknown
odin_topics:
  - 2.D
  - 4.A
  - 5.A
  - 6.A
  - 7.A
  - 10.B
tldr: Consumers without liquidity constraints self-impose monthly mental budgets renewed on paydays, leading to predictable spending cycles that decrease over trips until the next payday.
problem_and_motivation: Traditional economic models assume rational long-horizon intertemporal utility maximization, but consumers are neither fully rational nor completely myopic. The gap is understanding how consumers with no liquidity constraints actually make intertemporal spending decisions, particularly regarding storable goods.
approach:
  - Analyzed individual-level transaction data from a global cosmetic retail chain in a Southeast Asian country from 2011-2015, covering 300 stores and 600,000 members.
  - Employed regression discontinuity design with customer-day-level and trip-level regressions to isolate payday effects.
  - Controlled for customer fixed effects, store fixed effects, year, month, day-of-week, public holidays, and daily discount rates.
  - Compared cash versus credit card users to disentangle liquidity from behavioral effects.
  - Examined multiple dependent variables: expenditure, basket size, new product adoption, product upgrading, and purchase mistakes.
findings:
  - num: Payday shifts up unconditional daily expenditure by 4.7% for all members, driven by higher spending conditional on shopping (3.3% increase per trip) rather than increased shopping likelihood.
  - num: Credit card users show larger payday expenditure jumps (3.7%) than cash users (2.3%), disconfirming liquidity constraint explanations.
  - num: Per-trip expenditures decrease over subsequent trips within a paycheck cycle, with the first post-payday trip being significantly larger even when it occurs on a non-payday.
  - num: Expenditure on the first trip is dramatically larger if it falls on the payday versus one day after, indicating a salience effect beyond mental budget renewal.
  - num: Payday increases probability of purchasing a new variety by 0.63% and mistake probability (never-purchased-again variety) by 1.08%.
  - num: Payday effect shifts up daily consumption rate of the brand by US$0.0212 relative to a mean of US$0.263.
  - num: Mental budget renewing contributes 55% (credit card) and 75% (cash) of payday expenditure elevation; salience contributes the remainder.
  - Projection bias is triggered by salience but not by mental-budget renewing, as mistakes drop sharply from payday to day-after but do not decrease over trips.
key_figures_tables:
  - Figure 1: Unconditional daily expenditure shows a sudden spike at payday (day 0) across all members, credit card, and cash users → Payday increases spending even when including non-shopping days.
  - Figure 2: Conditional-on-visit expenditure spikes at payday → The payday effect is driven by larger purchases when shopping, not by more frequent shopping.
  - Figure 3: Panels A-D show payday increases variety seeking, new-product trying, upgrading to premium products, and daily consumption rate → Real economic impact beyond stockpiling.
  - Figure 5: First-trip expenditure drops sharply from payday to day-after, then remains flat → Salience effect distinct from mental budget renewal.
key_equations:
  - equation: ݕ = ߛ + ߛ ܫ(߬ ≥ 0) + ݂(߬ ) + ߚܺ + ߝ
    explanation: Regression discontinuity design isolating payday effect on daily expenditure.
  - equation: ܷ(݁) = ((1−ߜ௧̅)/(1−ߜ)) ݑ(݁/ݐ̅)
    explanation: Present value of utility from a storable product purchase.
  - equation: max ܷ(݁) + ݃(ℎ − ݁)
    explanation: Consumer maximizes utility from purchase plus pain of depleting mental budget.
definitions:
  - term: Mental Accounting
    definition: Consumers group expenditures into separate budgets (periodic or bracket-specific) rather than treating money as fully fungible.
  - term: Salience
    definition: Payday event draws attention and reduces self-control, causing overspending.
  - term: Projection Bias
    definition: Consumers overestimate how much future tastes will resemble current tastes, leading to purchase mistakes.
  - term: Mental Budget Renewal
    definition: Paycheck receipt resets the monthly spending limit consumers impose on themselves.
critical_citations:
  - "[Amador et al., 2006] — Optimal commitment imposes minimum savings per period."
  - "[Heath & Soll, 1996] — Foundational work on mental budgeting and fungibility."
  - "[Huffman & Barenstein, 2005] — Proposed monthly mental budgeting for credit card users."
  - "[Thaler, 1985] — Transaction utility and mental accounting theory."
relevance:
  topics:
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: high
      justification: Directly examines monthly paycheck cycles and spending patterns relevant to Filipino cultural payday practices.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Provides evidence that users impose their own mental constraints even without system support, informing baseline behavior.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Demonstrates distinct consumer profiles (cash vs. credit card) with different behavioral susceptibilities.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Spending patterns are predictable by trip count within a paycheck cycle, directly informing forecasting.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Reveals that consumers naturally use rule-of-thumb mental budgets, validating domain assumptions for recommendation systems.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: contextual
      justification: Relates to psychological mechanisms of self-control and commitment, indirectly relevant to trust in system recommendations.
  contribution: The paper provides empirical evidence for monthly mental budgeting behavior among consumers without liquidity constraints, which directly informs Odin's budget recommendation module by validating that users naturally think in monthly cycles. It identifies salience and projection bias as critical behavioral factors that cause overspending on paydays, suggesting Odin should incorporate payday-aware alerts and reminders. The cash vs. credit card user differences imply Odin should tailor interventions based on payment method profiles to maximize effectiveness. The finding that per-trip spending decreases over trips within a cycle indicates Odin's spending forecasting should track trip frequency, not just calendar days. Finally, the evidence that consumers allocate expenditures into bracket-specific mental accounts supports Odin's expense categorization and category-level budgeting features.
  directly_justifies:
    - "Consumers without liquidity constraints self-impose monthly mental budgets, supporting Odin's default monthly budgeting paradigm."
    - "Payday salience causes overspending, justifying Odin's payday-specific alerts and nudges."
    - "Per-trip expenditure decreases over trips within a paycheck cycle, informing Odin's spending forecasting models."
    - "Cash users are less susceptible to behavioral biases, suggesting Odin should offer different intervention strategies by payment type."
    - "Projection bias from salience leads to purchase mistakes, supporting Odin's post-purchase reflection and learning features."
  limits:
    - "The sample consists of upper-middle-class consumers in a Southeast Asian country, which may not generalize to all Filipino young professionals."
    - "The study focuses on a single cosmetic retail chain, so findings may not extend to essential goods or broader spending categories."
    - "Cash vs. credit card user differences could be confounded by income or financial sophistication rather than payment method alone."
    - "The data predates widespread mobile payment adoption, which may affect salience effects in contemporary users. [unacknowledged]"
  mapping_rationale: The systematic scan across all 12 functional domains and their associated topic codes identified that this paper directly addresses consumer spending cycles (2.D), behavioral profiling (5.A), spending forecasting (6.A), budget recommendation domain knowledge (7.A), and system landscape (4.A). The high relevance assignments for 2.D, 5.A, 6.A, and 7.A are justified by the paper's rigorous empirical documentation of predictable monthly spending cycles, consumer self-imposed mental budgets, and payday-triggered behavioral patterns that directly inform Odin's algorithmic modules. The paper was considered and rejected for topics 3.A, 3.B, 3.C, and 7.B-D because it does not address categorization frameworks, allocation constraints, or optimization approaches for budget recommendations. It was also rejected for 8.A-C, 9.A-B, 10.A, 11.A-B, 12.A-C, and 13.A-C due to lack of coverage of anomaly detection, mobile UX, privacy, engagement, evaluation, or savings/debt management. The borderline case of user trust (10.B) was assigned contextual relevance because the psychological mechanisms described (self-control, commitment) indirectly relate to trust in system recommendations but are not directly studied. Overall, the paper has high relevance for Odin's core behavioral modeling and budget recommendation domains.
limitations:
  - "The sample consists of upper-middle-class consumers, limiting generalizability to lower-income Filipino young professionals."
  - "The study examines a single retail chain selling storable products, so findings may not extend to essential goods or overall spending."
  - "The data is from a Southeast Asian country and may not fully reflect Filipino cultural spending nuances."
  - "Cash vs. credit card differences may be confounded by unobserved income or financial literacy differences. [unacknowledged]"
  - "The study does not account for the impact of modern fintech like mobile payments on payday behaviors. [unacknowledged]"
remember_this:
  - "Consumers impose monthly mental budgets even without liquidity constraints."
  - "Payday salience, not just renewal, drives spending overshoots."
  - "Per-trip spending decreases predictably over trips within a paycheck cycle."
  - "Credit card users are more susceptible to payday behavioral biases than cash users."
  - "num: Mental budget renewal explains 55-75% of payday spending increases."
```