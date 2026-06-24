```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international
title: Impact of Mental Representation on Consumer Behaviors: Implications for Mental Budgeting and Prediction Algorithm Preferences
authors: Fei, L.
year: 2023
venue: University of Chicago Booth School of Business
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 7.A
  - 7.D
  - 8.B
  - 12.A
tldr: Consumers represent expenditures in hierarchical taxonomies, and the taxonomic distance between items predicts spending adjustments when budgets deviate.
problem_and_motivation: Existing mental budgeting research assumes single-level categories, failing to capture how consumers naturally organize expenditures. Understanding this hierarchical representation is crucial for predicting spending adjustments and improving personal finance tools.
approach:
  - Recovered consumer expenditure taxonomies using a successive pile-sort method with 27 US participants.
  - Validated taxonomy consensus and stability across time using Cultural Consensus Model analysis.
  - Tested spending adjustment predictions using lab experiments with self-reported and consequential choices.
  - Analyzed over 7 million grocery shopping trips to examine real-world spending patterns in response to promotions.
  - Controlled for substitutability and complementarity to isolate the effect of taxonomic distance.
findings:
  - Consumers show consensus in their hierarchical representations of expenditures.
  - Taxonomic distance predicts spending adjustment: closer items are adjusted more than distant ones.
  - num: Spending adjustment increased by 0.5 units for each taxonomic level closer between items.
  - The taxonomy effect persists even when controlling for substitutability and complementarity.
  - num: Analysis of 7 million grocery trips shows consumers spend more on items when taxonomically close items are on sale.
  - People spontaneously recruit taxonomies for spending decisions without explicit category prompts.
key_figures_tables:
  - Figure 1.3: MDS plot shows clustered groups of expenditures → Reveals consensus in mental representation structure.
  - Figure 1.5: Bar chart of spending adjustment by taxonomic distance → Closer items show higher spending adjustment.
  - Figure 1.9: Regression coefficients for close vs. far focal items over years → Close items consistently drive higher spending.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: Taxonomic Distance
    definition: The level at which expenditures are categorized together in a consumer's hierarchy.
  - term: Cultural Consensus Model
    definition: A statistical framework to test agreement across individual mental representations.
critical_citations:
  - "[Thaler, 1985] — Foundation of mental accounting theory."
  - "[Heath and Soll, 1996] — Establishes mental budgeting with category-level adjustments."
  - "[Henderson and Peterson, 1992] — Preliminary evidence for hierarchical mental accounts."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Paper proposes hierarchical taxonomy for expenditure categorization.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: high
      justification: Provides empirical basis for designing multi-level spending categories.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Critiques single-level budgeting approaches as insufficient.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Highlights gap in capturing hierarchical mental accounts.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Taxonomy reflects individual spending patterns and profiles.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Directly tests and refines mental budgeting theory.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: medium
      justification: Hierarchical adjustment suggests structured reduction priorities.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Taxonomic context could inform anomaly baselines.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: contextual
      justification: Uses field data to evaluate taxonomy-based spending predictions.
  contribution: The paper provides a cognitive framework for understanding how consumers naturally categorize expenses, which can inform Odin's expense categorization engine by moving beyond flat category structures. It validates that taxonomic distance predicts real spending adjustments, offering a basis for Odin's budget recommendation module to model user behavior more accurately. The findings also support Odin's anomaly detection by providing a baseline for what constitutes typical spending relationships. Additionally, the paper demonstrates that consumers spontaneously recruit taxonomies, suggesting Odin can leverage implicit user structures without explicit input.
  directly_justifies:
    - Odin should implement a hierarchical expense categorization system based on taxonomic distance.
    - Budget recommendations should account for relative distance between expense items.
    - Spending adjustments follow predictable patterns tied to mental taxonomies.
    - Mobile UX can leverage hierarchical categories for intuitive budget tracking.
  limits:
    - Study population is US-based, limiting generalizability to Filipino young professionals.
    - Taxonomic recovery may vary across cultural contexts and financial literacy levels.
    - The field data focuses only on grocery purchases, not total spending.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes flagged several as relevant. The paper directly addresses expense categorization (3.A, 3.B) by proposing a hierarchical taxonomy, and critiques existing systems (4.A, 4.B) for their single-level assumptions. It supports behavioral profiling (5.A) by showing taxonomic consensus across consumers. The core contribution to budget recommendation (7.A) is high, as it tests and refines mental budgeting theory, with implications for infeasibility handling (7.D) through structured adjustment priorities. Anomaly detection (8.B) was considered low because the paper does not directly address detection algorithms, though taxonomic context could inform baselines. System evaluation (12.A) was deemed contextual due to the use of field data. Domains like Filipino cultural context (2.A-D), mobile-first design (9.A-B), data privacy (10.A-B), user retention (11.A-B), and savings/debt management (13.A-C) were rejected as they are not addressed. The paper overall provides foundational cognitive insights for Odin's expense management and budgeting modules.
limitations:
  - Taxonomic recovery may not capture all relevant spending categories for Filipino users. [unacknowledged]
  - Field data limited to grocery purchases, not validating total spending adjustments. [unacknowledged]
  - Spontaneous adjustment may be weaker when users are explicitly reminded of budgets.
remember_this:
  - Consumers mentally organize expenses in nested hierarchies, not just flat categories.
  - Spending adjustments are stronger for taxonomically closer items.
  - Hierarchical taxonomies predict real grocery spending based on promotions.
  - The taxonomy effect remains after controlling for substitutability and complementarity.
  - People spontaneously use taxonomies even without budget category prompts.
```