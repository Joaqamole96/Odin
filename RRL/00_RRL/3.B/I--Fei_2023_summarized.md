# IMPACT OF MENTAL REPRESENTATION ON CONSUMER BEHAVIORS: IMPLICATIONS FOR MENTAL BUDGETING AND PREDICTION ALGORITHM PREFERENCES

## Metadata

```yaml
---
paper_id: "00000000-0000-5000-8000-000000000000"
designation: international
title: "IMPACT OF MENTAL REPRESENTATION ON CONSUMER BEHAVIORS: IMPLICATIONS FOR MENTAL BUDGETING AND PREDICTION ALGORITHM PREFERENCES"
authors: "Fei, L."
year: 2023
venue: "University of Chicago, Booth School of Business"
odin_topics: ["3.A", "3.B", "5.A", "7.A", "7.B"]
shorthand_tags: ["/cat-approaches", "/cat-groupings", "/profiling-role", "/strategy-mechanics", "/budget-rec-approaches"]
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[X]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---
```

## TL;DR

Consumers represent expenditures in hierarchical taxonomies, and overspending on an item leads them to cut back more on taxonomically close items than distant ones, even when money is fungible.

## Problem and Motivation

Existing mental budgeting research assumes consumers use single‑level categories, ignoring the hierarchical structure of how people naturally group expenses. Understanding hierarchical representation is critical for predicting how spending adjustments propagate across related purchases. Prior work had not tested whether taxonomic distance—the level at which items share a category—drives real‑world spending adjustments.

## Approach

- **Study 1a**: 27 US participants performed a successive pile‑sort of 28 common expenditures; multidimensional scaling recovered consensus hierarchical taxonomy.
- **Study 1b**: Test‑retest of the same pile‑sort after 3 months showed stable individual taxonomies.
- **Study 2a/2b**: Measured self‑reported spending adjustment after hypothetical overspending; adjustment decreased as taxonomic distance increased.
- **Study 2c**: Controlled for substitutability and complementarity; taxonomic distance predicted adjustment beyond those constructs.
- **Study 3a/3b**: Consequential choice experiments with promotions confirmed that consumers shift spending toward taxonomically close promoted items.
- **Study 4**: Field analysis of 7+ million grocery trips over a decade showed that sales on taxonomically close items increased spending on a focal item.

## Findings

1. **Consensus exists** across consumers in the hierarchical representation of 28 expenditures (first latent root ratio > 3:1 in Cultural Consensus Model).
2. **Stability over time**: Individual taxonomies correlated at r = 0.78 across a 3‑month interval.
3. **Spending adjustment follows taxonomic distance**: Overspending on an item caused **62% greater intended cutback** on taxonomically close items vs. far items (Study 2a).
4. **Effect persists with consequential choices**: Participants chose promoted items that were taxonomically closer to a prior overspend item 2.3× more often than distant items.
5. **Field data replication**: Grocery spending on an item increased significantly when taxonomically close items were on sale, controlling for price and seasonality.

## Key Figures and Tables

- Figure 1.3: MDS reduction with clustered groups → Consumers organize expenditures into interpretable, nested clusters (e.g., food → groceries/dining).
- Figure 1.4: Dendrogram of 28 products → Shows hierarchical grouping at aggregate level, validating taxonomic distance metric.
- Figure 1.5: Spending adjustment on comparison items (Study 2a) → Adjustment drops sharply as taxonomic distance increases from same to distant.
- Table 1.2: Stimuli for Study 3a/3b → Product sets varying taxonomic distance; used to test consequential promotion choices.
- Figure 1.9: Regression coefficients by year (Study 4) → Positive effect of close‑item sales on focal spending persists across all 10 years of grocery data.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Mental accounting | Cognitive operations that treat money as non‑fungible by assigning it to specific “topical” accounts rather than total wealth. |
| Taxonomic distance | The level in a hierarchical category tree at which two items are grouped together; smaller distance = more closely related. |
| Hierarchical representation | A multi‑level, nested category structure (e.g., “breakfast food” inside “food”). |
| Successive pile‑sort | A research method where participants repeatedly group items into finer or coarser clusters to reveal their mental taxonomy. |
| Cultural Consensus Model (CCM) | Statistical test for agreement across individuals’ responses (first latent root >3 indicates consensus). |

## Critical Citations

- [Thaler, 1985; 1999] — Foundational theory of mental accounting and non‑fungibility of money, establishing the concept of topical accounts.
- [Heath and Soll, 1996] — Demonstrated that consumers track spending against category budgets and adjust spending on typical category members.
- [Henderson and Peterson, 1992] — First suggestion that mental accounts might be hierarchically organized, though without behavioral predictions.
- [Rosch et al., 1976] — Basic cognitive science evidence that everyday objects (e.g., furniture) are represented in hierarchical taxonomies.
- [Ratneshwar and Shocker, 1991] — Recovered hierarchical structures for snack foods, directly supporting product taxonomies in consumer contexts.

## Relevance to Odin

**Topics:**

3.A — Expense Categorization Frameworks

3.B — Expense Category Design Considerations

5.A — Financial Behavioral Profiles in Personal Finance

7.A — Budgeting Strategies as Domain Knowledge

7.B — Budget Recommendation in Personal Finance Systems

**Contribution to Odin:**

This paper directly informs Odin’s expense categorization module by demonstrating that users naturally organize spending items into nested hierarchies—suggesting that Odin should support multi‑level categories (e.g., “Food → Groceries → Dairy”) rather than flat lists. The finding that overspending on an item triggers larger cutbacks on taxonomically close items guides Odin’s anomaly detection and alert design: after detecting an overage in one category, the system should prioritize alerts on related categories. Finally, the taxonomic distance principle can improve Odin’s budget recommendation by allocating adjustments proportionally to category closeness, a novel constraint not present in current static or linear‑programming approaches.

**Directly justifies:**

- “Consumers represent expenditures in a consensual hierarchical taxonomy, recoverable via pile‑sort methods, with stable individual structures over three months.”
- “Taxonomic distance predicts spending adjustment even after controlling for substitutability and complementarity (Study 2c), implying that mental grouping—not just economic substitution—drives budget behavior.”
- “In field grocery data covering 7+ million trips, spending on an item increases significantly when taxonomically close items are on sale, consistent with cross‑category budget adjustments.”
- “Overspending on an item leads to 62% greater intended cutback on close items versus distant items, providing a quantitative benchmark for budget adherence models.”

**Limits of relevance:**

- Participants and grocery data are exclusively from the US; Filipino spending hierarchies (e.g., “bigas”, “sari‑sari store” items) may differ.
- The paper examines discretionary spending only; fixed expenses (rent, utilities) are excluded, limiting applicability to Odin’s essential‑category floors.
- Study 4 uses observed purchases, not manual transaction entry; manual entry may reduce spontaneous budget adjustment cues.
- The hierarchical representation was elicited from general consumers, not specifically young professionals—income stability and life stage may alter taxonomies.

## Limitations

- Only Chapter 1 (expenditure representation) was present in the provided file; Chapter 2 on prediction algorithms was unavailable for summarization.
- Study 1a sample size (n=27) is modest for consensus estimation; replication with larger, more diverse samples is needed.
- All lab studies used MTurk participants, who may not represent broader consumer populations in financial decision‑making.
- Self‑reported spending adjustment (Studies 2a/2b) may not perfectly mirror actual purchase behavior, though Studies 3 and 4 partially mitigate this.
- The field data (Study 4) is limited to grocery purchases; other spending domains (entertainment, transportation, utilities) were not tested. [unacknowledged]

## Remember This

- 🔑 **Taxonomic distance drives budget cuts** — overspending cuts close items 62% more than distant ones.
- 📌 **Consensus hierarchy exists** — consumers agree on how to group 28 common expenses (first root ratio >3).
- 💡 **Field evidence from 7M trips** — sales on close items increase focal spending, replicating lab findings.
- 🧠 **Nested categories, not flat lists** — Odin should support hierarchical expense categorization.
- ⚠️ **US‑only data** — Filipino spending taxonomies may differ; local elicitation needed.
