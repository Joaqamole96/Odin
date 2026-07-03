# Compiled Research Summaries

**Total Papers:** 50

**Note:** Included papers positions 251 to 300, Sorted by year.

---

## Paper 1: Pretnar et al_summarized.md

**Source File:** `Pretnar et al_summarized.md`

```yaml
paper_id: 10.21203/rs.3.rs-7730348/v1
designation: international-algorithm-specific
title: Mental Accounting Through Two-stage Budgeting Under Bounded Rationality
authors: Pretnar, N.; Olivola, C. Y.; Montgomery, A.
year: 2025
venue: Research Square
odin_topics:
  - 3.A
  - 5.A
  - 6.A
  - 7.A
  - 7.C
  - 8.A
  - 10.B
tldr: A structural model generalizes two-stage budgeting with cognitive frictions to quantify mental accounting behavior from expenditure data alone.
problem_and_motivation: Classical two-stage budgeting assumes perfect fungibility and ex-post budget adherence, yet consumers exhibit mental accounting and sticky budgets due to cognitive costs. There is a lack of empirical, agent-level quantification of how bounded rationality manifests in budgeting. This gap prevents the design of effective financial interventions that account for heterogeneous consumer decision-making.
approach:
  - Proposes a dynamic, two-stage budgeting model where a planner sets ex-ante budgets subject to cognitive constraints and a doer realizes expenditure shocks.
  - Incorporates narrow choice bracketing via probabilistic budget re-evaluation (ψ) and numeracy constraints that prevent trivial budget changes.
  - Mental accounting is captured by a state variable (over/under-spending from prior periods) that influences future budget adjustments via a parameter γ.
  - Estimates the structural model using a hierarchical MH-within-Gibbs MCMC algorithm on weekly expenditure data from 2,509 low-income prepaid debit card users.
  - Compares model variants with absolute ($1) and relative (%) numeracy thresholds, and tests counterfactuals by fully relaxing cognitive constraints.
findings:
  - num: 80% of consumer-week combinations exhibit bounded rationality, with an average of 2.11 budget updates per week under the $1-threshold model.
  - num: A $1 numeracy threshold reduces budget updates by 14.9%, while relative thresholds of 1%, 5%, and 10% reduce updates by 41.8%, 64%, and 70% respectively.
  - Ex-ante budgeting behavior is largely consistent with mental accounting (78.7% are budget prioritizers), but ex-post spending behavior is mixed, with 46.8% classified as spendthrifts.
  - num: 22.3% of consumers are ex-ante budget prioritizers but ex-post habitual over-spenders (type ii), exhibiting a "planning fallacy" pattern after over-spending.
  - Counterfactual relaxation of cognitive constraints makes 68.4% of consumers worse off, and 3.3% go bankrupt under the $1-threshold model.
  - num: Consumers who go bankrupt when constraints are relaxed have significantly lower estimated updates (1.25/week) and are more likely to be ex-ante type (i) but ex-post type (ii).
key_figures_tables:
  - "Table 1: Summary statistics of agent-level means → Shows low-income sample (median weekly income $460) with substantial spending variation."
  - "Table 2: Posterior summary statistics for baseline and $1-threshold models → Reports estimated means and standard deviations for all key behavioral parameters."
  - "Table 3: Marginal distributions of ex-ante and ex-post types → Ex-ante most are budget prioritizers, ex-post plurality are spendthrifts."
  - "Table 4: Joint distributions of ex-ante and ex-post types → Reveals 37.5% are budget prioritizers ex-ante but spendthrifts ex-post."
  - "Figure 2: Time series of actual vs. predicted spending → Demonstrates the model's fit for a median-income agent across categories."
  - "Figure 3: Posterior density of budget updates per week → Shows distribution of k under different numeracy thresholds."
  - "Figure 4: Density of k conditional on counterfactual type → Bankrupt consumers have significantly fewer budget updates."
key_equations:
  - equation: $x_{ijt} = \omega_{ijt} + \zeta_{ijt}$
    explanation: Doer's expenditure is budget plus shock.
  - equation: $a_{ijt} = \omega_{ij,t-1} - x_{ij,t-1} = -\zeta_{ij,t-1}$
    explanation: Mental account balance equals negative prior shock.
  - equation: $\omega_{ijt} = \theta_{ijt} \ell_{it} + \gamma_i a_{ijt}$
    explanation: Budget is income share plus anchored mental account.
  - equation: $\Gamma_{ijt} \sim \text{Bernoulli}(\psi_{ij})$
    explanation: Probability of re-evaluating a specific budget.
  - equation: $\vartheta_{iyt}^* = \frac{\alpha_{i,\iota_{iyt}} \ell_{it} - \alpha_{i,\iota_{iyt}} \sum_{s<y} \ell_{it} \theta_{i,\iota_{ist},t} + \gamma_i a_{i,\iota_{iyt},t} + \zeta_{i,\iota_{iyt},t}}{\ell_{it}(\alpha_{i,\iota_{iyt}} + \alpha_{i,J+1})} \dots$
    explanation: Analytical expression for optimal candidate budget share.
definitions:
  - term: Mental Accounting
    definition: A book-keeping mechanism where past over/under-spending informs future budgets.
  - term: Narrow Choice Bracketing
    definition: Consumers re-evaluate only a subset of budgets per period due to cognitive constraints.
  - term: Numeracy Constraint
    definition: A threshold (absolute or relative) that a budget change must exceed to be implemented.
  - term: Budget Prioritizer
    definition: Consumer type that reduces budget after over-spending and increases after under-spending.
  - term: Spendthrift
    definition: Consumer type that increases spending regardless of prior over or under-spending.
critical_citations:
  - "[Thaler, 1985] — Foundational theory of mental accounting."
  - "[Deaton and Muellbauer, 1980] — Classical two-stage budgeting framework."
  - "[Shefrin and Thaler, 1981] — Planner/doer model of self-control."
  - "[Gabaix, 2014] — Sparse maximization and bounded rationality."
  - "[Kőszegi and Matějka, 2020] — Mental budgeting with attention costs."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: The model operationalizes budget categories and estimates category-specific expenditure shares.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Empirically classifies consumers into ex-ante and ex-post behavioral types (budget prioritizers, spendthrifts).
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Develops a structural forecasting model for spending based on budgets, mental accounts, and shocks.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Models the strategic process of setting and updating budgets under cognitive frictions.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: high
      justification: Formulates budget selection as a constrained optimization problem with cognitive and numeracy constraints.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Expenditure shocks (ζ) are modeled as deviations from budgets, which is foundational for anomaly detection.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: contextual
      justification: Counterfactual analysis shows that nudging via apps can harm certain users, affecting trust.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: low
      justification: The model captures spending spikes and trends but does not focus on seasonality.
  contribution: "The paper provides a structurally estimated model for inferring latent budgeting behavior from expenditure data, which can be used to enhance Odin's spending forecasting module (6.A) by incorporating cognitive constraints. It offers a methodology for dynamically classifying users into behavioral profiles (5.A) based on their budget-updating and spending responses, enabling adaptive budgeting strategies. The counterfactual analysis reveals critical insights for Odin's nudging features (11.A): increasing attentiveness can have adverse effects for some users, implying that interventions should be personalized and cautious. The model's framework for budget updating and mental accounting directly informs the design of Odin's budget recommendation (7.B) and anomaly detection (8.A) algorithms, providing a theoretical basis for handling infeasibility and user inertia. Finally, the identification of distinct consumer types (e.g., budget prioritizers vs. spendthrifts) supports the development of tailored financial advice and savings/debt management strategies (13.A, 13.B)."
  directly_justifies:
    - "Budget updates occur for approximately half of consumption categories each period, supporting a sparse-max approach for Odin's budget recommendation."
    - "A $1 numeracy threshold is a better fit than no threshold, justifying the inclusion of an 'inertia' parameter in Odin's budget adjustment logic."
    - "Relaxing cognitive constraints makes 68% of consumers worse off, suggesting Odin should avoid over-nudging and prioritize user autonomy."
    - "Ex-ante budgeting behavior is distinct from ex-post spending, indicating Odin should track both planned budgets and actual expenditure separately."
    - "Consumers who are ex-ante budget prioritizers but ex-post spendthrifts are most vulnerable to adverse outcomes, requiring targeted support."
  limits:
    - "Results are model-dependent and rely on unobserved latent variables, limiting the certainty of individual-type classifications."
    - "Data is from low-income, underbanked prepaid card users in North America, which may not generalize to Filipino young professionals."
    - "Assumes strong separability of utility, which may oversimplify substitution patterns across broad expenditure categories."
    - "Does not explicitly model price variation, aggregating prices into indices, which may miss important consumption adjustments."
  mapping_rationale: "A systematic scan across all 12 functional domains was conducted. The paper's core theoretical and empirical contributions on modeling bounded rationality in budgeting directly map to high relevance for domains: Expense Categorization (3.A, 3.B), Behavioral Profiling (5.A, 5.B, 5.C), Spending Forecasting (6.A, 6.B), and Budget Recommendation (7.A, 7.B, 7.C, 7.D). The structural estimation approach and consumer typing also offer medium relevance to Anomaly Detection (8.A) and System Evaluation (12.A, 12.B, 12.C). The counterfactual simulations on attentiveness inform Engagement & Retention (11.A) and Data Privacy/Trust (10.B), albeit with contextual or low relevance as the paper does not directly study app design or trust. Topics like Filipino Cultural Context (2.A, 2.B, 2.C) and Savings/Debt (13.A, 13.B) were considered but rejected as the paper's empirical setting is North American and its primary contribution is methodological, though findings on overspending cycles are tangentially relevant to debt management. Borderline cases included the mental accounting state variable (a), which relates to both expense categorization (3.A) and behavioral profiles (5.A); it was assigned to 5.A for its role in defining consumer types. The paper's overall relevance to Odin is high, providing a quantitative, micro-founded framework for modeling key user behaviors that directly informs the design of adaptive and personalized financial management features."
limitations:
  - "Findings are based on a model-dependent estimation of latent budgets, not directly observed." [unacknowledged]
  - "The dataset is from a specific low-income, underbanked population in North America; applicability to other demographics (e.g., Filipino YPs) is not tested." [acknowledged]
  - "Assumes strong separability in utility, which may not capture complex category interactions."
  - "The model does not incorporate explicit price effects, relying on aggregated price indices." [acknowledged]
  - "Counterfactual simulations of 'full rationality' may not reflect real-world behavioral changes from app nudges."
remember_this:
  - "Consumers update only about half their budgets per week, showing bounded rationality."
  - "Most consumers are budget prioritizers ex-ante but spendthrifts ex-post."
  - "Relaxing cognitive constraints makes 68% of consumers worse off."
  - "3.3% of consumers go bankrupt if all budgets are updated weekly."
  - "Sticky budgets can serve as a disciplinary tool for vulnerable consumers."
```
---

## Paper 2: Anes & Abreu_summarized.md

**Source File:** `Anes & Abreu_summarized.md`

```yaml
paper_id: 10.3390/app15074044
designation: international-algorithm-specific
title: Adaptive Cluster-Based Normalization for Robust TOPSIS in Multicriteria Decision-Making
authors: Anes, V.; Abreu, A.
year: 2025
venue: Applied Sciences
odin_topics:
  - 3.A
  - 7.C
  - 8.A
  - 8.B
  - 12.A
  - 12.B
  - 12.C
tldr: Proposes a cluster-based logarithmic normalization for TOPSIS that uses fuzzy numbers for uncertainty and expert-defined centroids to improve ranking stability and outlier robustness.
problem_and_motivation: Traditional TOPSIS normalization techniques like Min-Max and Z-score are sensitive to outliers and large variance, which can distort rankings. Clustering methods also often rely on rigid, data-driven classifications that fail to capture uncertainty or expert intent. There is a need for a more flexible and robust normalization and clustering framework.
approach:
  - Defines cluster centroids a priori using fuzzy numbers based on expert judgment and ideal conditions for each criterion.
  - Converts each alternative's fuzzy criterion scores into crisp centroids using the average of (a, b, c) values.
  - Assigns each alternative to the cluster with the nearest Euclidean distance to its predefined centroid.
  - Applies logarithmic normalization within each cluster to compress extreme values and stabilize variance.
  - Uses the cluster centroids to derive criterion weights and then applies the standard TOPSIS procedure.
  - Validates the approach using a case study on selecting a host city based on cost, infrastructure, safety, and accessibility.
findings:
  - The proposed fuzzy clustering method produced classifications nearly identical to Fuzzy K-Means but with a more logically coherent assignment for a borderline case (City K).
  - The proposed method is computationally simpler and more deterministic than iterative Fuzzy K-Means.
  - Logarithmic normalization provided more balanced and stable TOPSIS scores, especially in clusters with high variance, compared to Min-Max normalization.
  - Top-ranked alternatives (City K and City C) were consistent across both normalization methods, reinforcing the robustness of the overall framework.
key_figures_tables:
  - Table 5: Distances to cluster centroids → Used to assign each city to its most appropriate cluster based on Euclidean distance.
  - Table 8: Logarithmic normalization results → Shows how extreme cost values are compressed within each cluster.
  - Table 11: TOPSIS results using logarithmic normalization → City K (0.89), City C (1.00), and City E (0.89) are top-ranked in their clusters.
key_equations:
  - equation: C_{cwj} = (a_w + b_w + c_w) / 3
    explanation: Calculates the crisp centroid of a cluster for a criterion.
  - equation: C_{Aij} = (a_i + b_i + c_i) / 3
    explanation: Calculates the crisp centroid of an alternative for a criterion.
  - equation: X' = (log(X) - log(X_min)) / (log(X_max) - log(X_min))
    explanation: Logarithmic normalization formula to scale data and reduce outlier impact.
definitions:
  - term: TOPSIS
    definition: Technique for Order of Preference by Similarity to Ideal Solution, a multi-criteria decision-making method.
  - term: MCDM
    definition: Multi-criteria decision-making, a field for evaluating multiple conflicting factors.
  - term: Fuzzy Number
    definition: A representation of uncertainty using a triplet (a, b, c) for lower, central, and upper bounds.
  - term: Cluster Centroid
    definition: The ideal point representing the optimal position for a cluster across all criteria.
critical_citations:
  - "[Vafaei et al., 2021] — Compares normalization techniques on data with outliers."
  - "[Zavadskas & Turskis, 2008] — Introduces a novel logarithmic normalization method in game theory."
  - "[Štilic´ & Puška, 2023] — Comprehensive review of MCDM methods in sustainable engineering."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: Provides a methodological framework for categorizing alternatives (cities) based on cost and other criteria.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: low
      justification: The case study involves budget allocation (cost criterion), but the method does not address constraint optimization.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: The method mitigates the effect of outliers, which is conceptually similar to handling anomalies in financial data.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Focuses on algorithmic robustness to outliers, a key challenge in anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: The paper presents a novel evaluation methodology (TOPSIS with cluster-based normalization) that can be used to rank financial options.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Directly evaluates the performance of the proposed clustering and normalization algorithms within the TOPSIS framework.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: high
      justification: The TOPSIS-based ranking methodology can be applied to evaluate and rank budget recommendation strategies for Odin.
  contribution: The paper provides a methodological framework for evaluating and ranking alternatives under uncertainty, which can be directly applied to Odin's recommendation system. Its cluster-based normalization approach can enhance the robustness of the Budget Recommendation (7.B) and Anomaly Detection (8.A) modules by mitigating the impact of outliers in financial data. The use of expert-defined profiles offers a way to incorporate Filipino cultural context and user preferences into the ranking process. Finally, the deterministic clustering method provides a computationally efficient and transparent approach for grouping users with similar financial behavior profiles.
  directly_justifies:
    - "Cluster-based normalization improves ranking stability by reducing the influence of outliers."
    - "Logarithmic normalization is effective for datasets with high variance and non-linear distributions."
    - "Using predefined cluster centroids allows for expert judgment to guide the classification process."
    - "The proposed TOPSIS framework is computationally simple and easy to implement."
  limits:
    - "The definition of cluster centroids is based on expert judgment, introducing subjectivity."
    - "The method's performance on large-scale, high-dimensional datasets remains untested."
    - "The study does not compare its method against a wide array of modern optimization or machine learning baselines. [unacknowledged]"
    - "The applicability of the method to streaming or real-time data is not explored. [unacknowledged]"
  mapping_rationale: A systematic scan of all 12 functional domains was performed to map the paper's contributions to Odin's topics. The paper's core contribution is algorithmic and methodological, leading to the selection of topics under `12.A`, `12.B`, and `12.C` as `high` relevance, as it provides a framework for evaluating systems and algorithms. The case study's context of selecting an option based on multiple criteria (like cost) relates to `3.A` (`contextual`) and `7.A` (`low`). The method's ability to handle outliers directly informs the principles for anomaly detection (`8.A`, `8.B` - both `low`). The domain of "Behavioral Profiling" (`5.A`) was considered but rejected because the paper does not classify individuals. "Filipino Cultural Context" (`2.A`, `2.B`, `2.C`, `2.D`) was rejected as the case study is not culturally specific. The "Data Privacy" (`10.A`, `10.B`) and "Engagement" (`11.A`, `11.B`) domains were not addressed. The paper's overall relevance to Odin is high in its capacity to provide a robust, outlier-resistant, and expert-guided evaluation framework, which can be adapted for modules like budget recommendation and anomaly detection, despite its abstract, algorithm-focused nature.
limitations:
  - "The definition of ideal cluster centroids is based on expert judgment, introducing subjectivity."
  - "The method's performance on large-scale, high-dimensional datasets remains untested."
  - "The study does not compare its method against a wide array of modern optimization or machine learning baselines. [unacknowledged]"
  - "The applicability of the method to streaming or real-time data is not explored. [unacknowledged]"
remember_this:
  - "Logarithmic normalization in TOPSIS improves ranking stability with high-variance data."
  - "Fuzzy numbers enable the representation of uncertainty in expert-defined cluster profiles."
  - "The proposed clustering method is computationally simpler than Fuzzy K-Means."
  - "City K was more logically assigned to a cluster by the proposed method than by Fuzzy K-Means."
```
---

## Paper 3: Lambert et al_summarized.md

**Source File:** `Lambert et al_summarized.md`

```yaml
paper_id: 12c7f7a6-9a4a-5b3c-8e2d-1f6b9a3c7d5e
designation: local
title: Relationship between Family Resources, Financial Stress, with Financial Management among Filipino Millennials
authors: Lambert, M. J. C. M.; Jusoh, Z. M.; Zainudin, N.
year: 2025
venue: JURNAL PENGGUNA MALAYSIA
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 4.B
  - 5.A
  - 9.A
  - 9.B
tldr: Financial stress negatively impacts financial management among Filipino millennials, while millennial characteristics positively influence management practices.
problem_and_motivation: Filipino millennials face significant financial stress, poor financial literacy, and limited savings despite macroeconomic growth. The interplay between family resources, stress, and financial management in this cultural context is poorly understood.
approach:
  - Data were collected from 400 Filipino millennials in Eastern Visayas using a self-administered online questionnaire.
  - The study employed multistage random sampling and Structural Equation Modelling (SEM) for analysis.
  - Millennial characteristics were assessed using 29 items adapted from Pew Research, measuring optimism, achievement focus, family orientation, and tech-savviness.
  - Financial stress was measured using a 14-item adapted instrument on economic difficulties and coping strategies.
  - Financial management was evaluated via a 39-item scale covering attitudes and practices like budgeting, saving, and bill payment.
findings:
  - num: Financial stress had a significant adverse effect on financial management (β = -0.724, p < .001).
  - num: Millennial characteristics exerted a positive and significant influence on financial management (β = 0.480, p < .001).
  - The study confirms that financial stress undermines prudent financial practices.
  - Millennial traits such as adaptability, collaboration, and digital literacy enhance financial management capabilities.
  - Respondents with higher financial stress demonstrated poorer budgeting, saving, and bill payment practices.
  - Millennials who are optimistic, achievement-focused, and tech-savvy are more likely to practice effective financial management.
  - The findings extend behavioural finance by illustrating how contextual stressors and generational traits jointly shape financial outcomes.
key_figures_tables:
  - "Table 1: Demographic Characteristics of Respondents (N=400) → Majority are male, college graduates, aged 26-35, with middle-to-low income."
  - "Table 2: Millennial Characteristics Score by Item → Highest mean score for family-oriented (4.81), lowest for optimistic (3.59)."
  - "Table 3: Financial Stress Score → Overall mean score of 2.23 indicates lower financial stress."
  - "Table 4: Financial Management Score → Mean score of 3.45 indicates good financial management practices."
  - "Figure 1: Conceptual Framework → Shows direct relationships between financial stress and millennial characteristics with financial management."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Financial well-being
    definition: A state where an individual has sufficient resources to live comfortably, fulfil obligations, and have confidence in their financial future.
  - term: Financial stress
    definition: Stress arising when resources are insufficient to meet needs or when constant worry about money occurs.
  - term: Family resources
    definition: Tangible and intangible assets (skills, knowledge, income, property) that influence financial outcomes.
  - term: Millennial characteristics
    definition: Traits such as adaptability, collaboration, digital literacy, and optimism associated with Generation Y.
  - term: Financial management
    definition: The practice of planning, budgeting, saving, and responsible spending.
critical_citations:
  - "[Dollahite, 1991] — Provides the integrated ABCD-XYZ model used as the conceptual framework."
  - "[Lusardi & Mitchell, 2021] — Shows financial literacy and stress are linked to financial well-being."
  - "[Pew Research Centre, 2021] — Demonstrates millennial characteristics shape financial decision-making."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: The study specifically surveys Filipino millennials, a core demographic for Odin.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Provides data on income levels, debt, and financial responsibilities of the target demographic.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly examines financial management practices and stress responses.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Highlights strong family orientation and its influence on financial obligations.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: low
      justification: The paper mentions financial stress but does not detail specific seasonal spending cycles.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: Mentions family obligations but does not specify cultural spending events.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies a gap in understanding the interplay of stress and resources for Filipino millennials.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Defines and measures specific millennial characteristics as a resource influencing financial management.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Recommendations include developing digital tools tailored for millennials.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: Mentions digital tools but does not focus on UX design principles.
  contribution: This study validates the dual influence of financial stress and generational traits on financial management for Odin's target demographic. It supports Odin's behavioral profiling module by identifying key traits like adaptability and digital literacy. The finding that stress undermines financial management justifies Odin's stress-mitigation and anomaly detection features. The strong negative effect of stress on financial management provides a basis for Odin's budget recommendation and forecasting modules to consider stress as a critical factor.
  directly_justifies:
    - "Financial stress significantly degrades financial management practices among Filipino millennials."
    - "Millennial characteristics such as adaptability and digital literacy positively influence financial management."
    - "Financial management practices include budgeting, saving, and responsible bill payment."
    - "Addressing financial stress is crucial for improving financial well-being."
    - "Digital tools tailored to millennial preferences can enhance financial management."
  limits:
    - "The study is cross-sectional, limiting causal inferences."
    - "Data were collected from Eastern Visayas, limiting generalizability to all Filipino millennials. [unacknowledged]"
    - "Self-reported data may be subject to social desirability bias."
    - "The study does not detail the specific algorithmic or system implementation. [unacknowledged]"
  mapping_rationale: A systematic scan was performed across all 12 functional domains and their associated topic codes. The paper was flagged as highly relevant to domains related to Filipino young professionals, behavioral profiling, and financial management (1.A, 1.B, 1.C, 5.A). It provided medium relevance to domains on cultural practices (2.A) and system gaps (4.B) by highlighting the cultural context and research gaps. Low relevance was assigned to seasonal spending (2.B) and mobile UX (9.B) due to only tangential mentions. Domains on forecasting, anomaly detection, and system evaluation (6.x, 8.x, 12.x) were rejected as the paper does not address algorithmic or predictive modeling aspects. Borderline cases included 2.D (spending cycles) which was assigned contextual due to its mention of family obligations but no detail on specific occasions, and 3.C (user-defined constraints) which was rejected as the paper does not discuss allocation constraints. Overall, the paper is relevant for understanding the behavioral and contextual drivers of financial management, providing foundational justification for Odin's design.
limitations:
  - "Cross-sectional design limits causal inferences."
  - "Sample limited to Eastern Visayas may not represent all Filipino millennials."
  - "Reliance on self-reported data may introduce social desirability bias."
  - "The study does not validate the proposed implications through system testing. [unacknowledged]"
  - "Cultural nuances in financial stress coping are not explored in depth. [unacknowledged]"
remember_this:
  - "Financial stress reduces financial management by 0.724 units per stress unit."
  - "Millennial traits improve financial management by 0.480 units per trait unit."
  - "Adaptability and digital literacy are key millennial strengths."
  - "Stress coping is as important as financial literacy for management."
  - "Family obligations increase financial stress for Filipino millennials."
```
---

## Paper 4: Pereira & Da Silva_summarized.md

**Source File:** `Pereira & Da Silva_summarized.md`

```yaml
paper_id: 10.1109/ACCESS.2025.3557229
designation: international-algorithm-specific
title: A Comparison of Approaches for Handling Concept Drifts in Data Processed With Machine Learning
authors: Pereira, E. V.; Da Silva, W. S.
year: 2025
venue: IEEE Access
odin_topics:
  - 4.A
  - 5.C
  - 6.A
  - 7.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
tldr: A comparison of concept drift handling techniques shows batch training and ensemble methods like BIC yield robust performance across diverse data streams.
problem_and_motivation: Machine learning models degrade when the statistical properties of target variables change over time, a phenomenon known as concept drift. This degradation is critical for domains like healthcare and finance. A comprehensive comparison of treatment methods across algorithms and drift types is lacking.
approach:
  - Utilized the scikit-multiflow framework to simulate and evaluate concept drift.
  - Tested eight datasets, including real-world data (Airlines, Electricity) and synthetic data (SEA, Hyperplane).
  - Evaluated various drift detection algorithms, including ADWIN, DDM, EDDM, and Page-Hinkley.
  - Assessed nine classifiers, including Hoeffding Tree (HT), Adaptive Random Forest, and KNN with Adaptive Windowing.
  - Applied treatment methods such as ignore, delete, retrain, and batch training to static models.
  - Compared performance of models with and without internal drift adaptation mechanisms.
findings:
  - num: Batch training consistently improved accuracy over ignoring drift across all tested datasets and classifiers.
  - num: The BIC ensemble classifier achieved strong and robust performance across all drift types and datasets.
  - num: The HAT decision tree algorithm, which uses ADWIN for branch-level monitoring, excelled in abrupt drift scenarios.
  - num: The KNNADW algorithm performed well on gradual concept drift due to its adaptive windowing.
  - The simple exclusion of drift-affected samples was ineffective, showing no significant performance change.
  - Combining treatment strategies within ensemble frameworks can amplify robustness against drift.
  - Algorithms lacking drift adaptation were consistently outperformed by those with adaptation mechanisms.
  - Ensemble methods like BIC, which combine batch training with model ensembles, are a potent strategy for dynamic data.
key_figures_tables:
  - "Figure 1: Comparison of HT, HAT, and EFDT classifiers across datasets → HAT and EFDT outperform HT on drift-affected data."
  - "Figure 2: Performance comparison of nine classifiers across varied datasets → BIC and HAT show superior and stable accuracy."
  - "Table 1: Dataset characteristics (samples, features, drift type) → Provides context for evaluating algorithm performance."
  - "Table 3-8: Accuracy of HT and KNN under different treatment methods → Batch training is the most effective standalone strategy."
key_equations:
  - equation: "p_t(X,y) \\neq p_{t+1}(X,y)"
    explanation: "Definition of concept drift in terms of joint probability."
definitions:
  - term: "Concept Drift"
    definition: "A change in the statistical properties of the target variable over time."
  - term: "ADWIN"
    definition: "Adaptive Windowing algorithm for detecting concept drift by monitoring statistical changes."
  - term: "scikit-multiflow"
    definition: "An open-source machine learning toolkit for streaming data."
critical_citations:
  - "[Lu et al., 2019] — Foundational review defining concept drift and its mathematical models."
  - "[Gama et al., 2014] — Comprehensive survey on concept drift adaptation strategies."
  - "[Gomes et al., 2017] — Introduces Adaptive Random Forest, a key ensemble method evaluated in the study."
relevance:
  topics:
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Provides a general benchmark for comparing algorithm performance."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "Evaluates classification algorithms that could be adapted for profiling."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Directly compares predictive models under data distribution shifts (concept drift)."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "contextual"
      justification: "Budgets must adapt to changing spending patterns, similar to model adaptation."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Concept drift detection techniques (e.g., ADWIN) are directly applicable to anomaly detection baselines."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "medium"
      justification: "Evaluation of drift detection algorithms informs the selection of anomaly detectors."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Provides a methodology for comparative evaluation of algorithmic modules."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Directly compares and evaluates multiple classification and detection algorithms."
  contribution: "This paper justifies Odin's use of ensemble and batch-training strategies for robust handling of changing spending patterns. It validates the need for adaptive algorithms over static ones in dynamic personal finance environments. The study's empirical comparison framework is directly applicable for evaluating Odin's classification and anomaly detection modules. Its findings on algorithm performance under different drift types inform the selection of optimal models for forecasting and anomaly detection within Odin."
  directly_justifies:
    - "Batch training is an effective strategy for maintaining model accuracy under concept drift."
    - "Ensemble classifiers like BIC provide robust performance across diverse data stream conditions."
    - "Models with integrated drift detection (e.g., ADWIN) outperform those without adaptation."
    - "The choice of optimal classifier depends on the type of concept drift (abrupt vs. gradual)."
  limits:
    - "The study does not specifically address personal finance data or spending behaviors."
    - "No deep learning models were evaluated."
    - "The analysis focuses on classification tasks, not forecasting or regression."
  mapping_rationale: "A systematic scan of all 12 functional domains was performed. Domains relevant to the core algorithmic contributions (Existing Systems & Gaps, Behavioral Classification, Forecasting, Anomaly Detection, and Evaluation) were flagged. Specifically, topic codes 4.A (landscape), 5.C (classification approaches), 6.A (predictive modeling), 8.A & 8.B (anomaly detection and algorithms), 12.A & 12.B (evaluation frameworks) were selected with high or medium relevance. The paper's focus on concept drift in data streams provides strong justification for its relevance to Odin's dynamic spending data. Borderline cases like 7.B (Budget Recommendation) and 7.C (Constrained Optimization) were considered but rejected as the paper does not address constraint-based allocation. Topics related to cultural context, mobile design, privacy, and retention (Domains 1, 2, 3, 9, 10, 11, 13) were considered and rejected, as the paper provides no information on those specific domains. The study's comparative framework is highly relevant for evaluating Odin's algorithmic modules, establishing a clear justification for its high relevance to the project."
limitations:
  - "The study does not address deep learning models. [unacknowledged]"
  - "The research is limited to classification problems and does not cover regression or forecasting. [unacknowledged]"
  - "No datasets specific to personal finance or developing economies were used."
remember_this:
  - "Batch training improves model accuracy during concept drift."
  - "Ensemble methods, like BIC, offer robust performance across drift types."
  - "The optimal classifier depends on the type of concept drift present."
  - "Adaptive algorithms consistently outperform static models on dynamic data."
  - "Ignoring drift-affected samples is an ineffective handling strategy."
```
---

## Paper 5: Munira et al_summarized.md

**Source File:** `Munira et al_summarized.md`

```yaml
paper_id: 0f3a7b2c-8d4e-5f6a-9b1c-2d3e4f5a6b7c
designation: international
title: Artificial Intelligence in Financial Customer Relationship Management: A Systematic Review of AI-Driven Strategies in Banking and FinTech
authors: Munira, M. S. K.; Juthi, S.; Begum, A.
year: 2025
venue: American Journal of Advanced Technology and Engineering Solutions
odin_topics:
  - 4.A
  - 6.A
  - 7.A
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 12.A
  - 13.B
tldr: AI integration in financial CRM enhances customer engagement, fraud detection, predictive analytics, regulatory compliance, and marketing, yielding significant operational and financial improvements.
problem_and_motivation: Traditional CRM systems in finance rely on rule-based automation and limited data analysis, failing to adapt to dynamic customer behaviors and evolving markets. This limits customer retention, risk management, and personalization capabilities. A systematic review is needed to consolidate evidence on AI's transformative impact and provide strategic insights for adoption.
approach:
  - Conducted a systematic review of 83 scholarly sources, including peer-reviewed articles, industry reports, and case studies.
  - Adopted a case study approach, analyzing AI applications in banks, FinTech firms, and other financial institutions.
  - Focused on five key AI application areas: customer engagement, fraud detection, predictive analytics, regulatory compliance, and marketing.
  - Used thematic analysis to categorize AI applications and evaluate their impact across selected institutions.
  - Incorporated analysis of ethical considerations, transparency issues, and regulatory challenges associated with AI adoption.
findings:
  - AI-powered chatbots reduced customer response times by 57% and operational costs by 38%, increasing retention by 28%.
  - AI-driven fraud detection systems reduced false positives by 52% and improved detection efficiency by 74%, decreasing fraud losses by 43%.
  - Predictive analytics in credit risk assessment improved loan approval accuracy by 67%, expedited processing by 29%, and reduced default rates by 23%.
  - AI automation for KYC and AML processes increased compliance accuracy by 58% and reduced penalties by 37%.
  - AI-driven marketing strategies increased customer engagement by 53% and boosted product adoption rates by 31%.
  - Customer Lifetime Value (CLV) models contributed to a 27% increase in long-term retention and a 22% improvement in per-customer profitability.
key_figures_tables:
  - Figure 1: AI in Customer Engagement → Shows AI's role in enhancing customer interactions through various technologies.
  - Figure 2: AI-Powered CRM in Financial Services → Illustrates AI's applications in fraud detection, risk management, and compliance.
  - Figure 3: Benefits of Using AI in CRM → Outlines key benefits like automation, personalization, and decision-making.
  - Figure 4: ML algorithms for customer churn modeling → Depicts common ML techniques used for predicting churn.
  - Figure 5: AI-Driven Marketing Strategies in Financial CRM → Details AI's role in predictive marketing, cross-selling, and campaign optimization.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: AI
    definition: Artificial Intelligence
  - term: CRM
    definition: Customer Relationship Management
  - term: ML
    definition: Machine Learning
  - term: NLP
    definition: Natural Language Processing
  - term: KYC
    definition: Know Your Customer
  - term: AML
    definition: Anti-Money Laundering
  - term: CLV
    definition: Customer Lifetime Value
  - term: RPA
    definition: Robotic Process Automation
critical_citations:
  - "[Lee & Chen, 2022] — Foundational for AI adoption in banking."
  - "[Huang et al., 2019] — Key reference for AI in customer engagement."
  - "[Grennan & Michaely, 2020] — Important for FinTech market analysis."
  - "[Mhlanga, 2020] — Crucial for AI's role in financial inclusion."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Reviews AI adoption in finance, mapping the current technological landscape.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Highlights limitations of traditional rule-based CRM systems that AI addresses.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly discusses predictive analytics for credit risk, churn, and CLV.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: Mentions personalized financial product recommendations informed by spending behavior.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Focuses significantly on AI for detecting fraudulent transactions and anomalies.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Reviews ML models specifically for fraud detection in financial transactions.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: Discusses AI chatbots and virtual assistants relevant to mobile banking UX.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Mentions data privacy regulations like GDPR and CCPA in the context of AI.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Discusses how AI transparency and fairness impact customer trust.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides quantitative metrics (e.g., reduction in response time, fraud losses) for evaluating AI performance.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: low
      justification: Touches upon AI's role in credit risk assessment and responsible lending, which is related to managing debt risk.
  contribution: "This paper provides a comprehensive systematic review quantifying the impact of AI on financial CRM, offering key benchmarks (e.g., 57% reduction in response time, 67% improvement in loan approval accuracy) that can be used to set performance targets for Odin's predictive analytics and anomaly detection modules. The findings on AI-driven fraud detection and KYC automation provide strong justification for Odin's security and compliance frameworks. The review's emphasis on AI's role in personalization and customer retention directly supports the design of Odin's user engagement and behavioral profiling systems. Furthermore, the documented improvements in operational efficiency and cost reduction validate the investment in AI-driven automation for Odin's core functionalities. Finally, the discussion on data privacy and AI transparency underscores the importance of these considerations in Odin's architecture to maintain user trust."
  directly_justifies:
    - "AI-powered systems reduced customer response times by 57% and operational costs by 38%."
    - "Machine learning models improved fraud detection efficiency by 74% and reduced false positives by 52%."
    - "Predictive analytics improved loan approval accuracy by 67% and reduced default rates by 23%."
    - "AI-driven marketing increased customer engagement by 53% and boosted product adoption by 31%."
    - "AI automation for compliance increased accuracy by 58% and reduced penalties by 37%."
  limits:
    - "The paper is a systematic review aggregating findings from existing studies, not presenting novel primary research or a unique algorithm for financial CRM."
    - "The quantified benefits (e.g., 57% reduction) are averages reported across reviewed studies and may not be directly replicable in all contexts without similar implementation conditions."
    - "The paper primarily focuses on high-level banking and FinTech applications, with less specific detail on personal finance management features like savings or budgeting for individuals."
  mapping_rationale: "A systematic scan across all 12 functional domains was performed for this paper. The domains of 'Existing Systems & Gaps' (4.A, 4.B), 'Spending Forecasting' (6.A), 'Budget Recommendation' (7.A), 'Anomaly Detection' (8.A, 8.B), 'Data Privacy & User Trust' (10.A, 10.B), and 'System Evaluation' (12.A) were flagged as relevant. Specifically, Topic 6.A was given 'high' relevance due to the paper's extensive coverage of predictive analytics for credit risk and CLV. Topics 8.A and 8.B were marked 'high' because a major focus is on AI for fraud detection (anomaly detection). Topics 4.A and 10.A/B were assigned 'medium' relevance as the paper provides contextual landscape information and discusses privacy/trust issues. Topic 7.A received 'contextual' relevance as it mentions personalized recommendations but doesn't focus on budget allocation. The 'Mobile-First Design' (9.A, 9.B) and 'Savings & Debt Management' (13.A, 13.C) domains were considered but rejected as the paper does not address mobile-specific design principles or savings goal management, though it touches on debt management (13.B) peripherally through credit risk. The paper is highly relevant to Odin by providing broad empirical justification for AI implementation across several core modules."
limitations:
  - "As a systematic review, it synthesizes existing findings rather than presenting novel experimental results. [unacknowledged]"
  - "The case studies and reviewed papers are not described in detail, limiting the ability to assess implementation contexts for the reported metrics."
  - "The paper does not address the specific challenges of implementing such AI systems in a mobile-first PFMS context for Filipino users."
  - "Potential publication bias in the reviewed literature may favor positive AI outcomes, as negative results are less likely to be published. [unacknowledged]"
remember_this:
  - "AI in financial CRM reduces customer service response times by an average of 57%."
  - "Predictive analytics improves loan approval accuracy by 67% and reduces default rates by 23%."
  - "AI-driven fraud detection improves efficiency by 74% while reducing false positives by 52%."
  - "Automating KYC and AML with AI increases compliance accuracy by 58% and reduces penalties."
  - "AI-powered marketing strategies can increase customer engagement by over 50%."
```
---

## Paper 6: Nokhiz & Ruwanpathirana_summarized.md

**Source File:** `Nokhiz & Ruwanpathirana_summarized.md`

```yaml
paper_id: 10.23919/JSC.2025.0015
designation: international
title: Consumer Autonomy or Illusion? Rethinking Consumer Agency in the Age of Algorithms
authors: Nokhiz, P.; Ruwanpathirana, A. K.
year: 2025
venue: Journal of Social Computing
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.B
  - 2.D
  - 4.B
  - 5.A
  - 5.B
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 7.D
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 13.A
tldr: Formal analysis demonstrates that limited consumer agency from obligatory consumption, algorithmic persuasion, and work instability leads to financial ruin even for rational utility-maximizing agents.
problem_and_motivation: Consumers face systemic barriers and algorithmic manipulation that erode financial autonomy, yet the consequences of diminished agency are not formally understood. This gap prevents the design of effective interventions to protect consumer welfare and promote genuine agency.
approach:
  - Uses discounted utility models to analyze intertemporal consumption under agency constraints.
  - Constructs analytical scenarios for obligatory consumption, algorithmic impulse spending, and unpredictable work schedules.
  - Formalizes financial ruin as a state where assets reach zero within a finite time horizon.
  - Applies Jensen's inequality and concentration inequalities to prove ruin under concave utility.
  - Demonstrates that advance schedule knowledge (lookahead) significantly improves utility and reduces ruin risk.
findings:
  - num: Rational agents under obligatory consumption can achieve higher utility by consuming all assets and going to ruin within a finite time.
  - num: Under impulsive consumption with minimum subsistence, the probability of avoiding ruin decays exponentially with time.
  - num: Workers with k-step lookahead achieve utility that is Ω(k) greater than those without lookahead.
  - num: Low-income agents experience near-instantaneous ruin under impulsive consumption, while high-income agents show delayed collapse.
  - num: Agents with high-school education (lower discount factor) exhibit ruin within 20 steps, whereas college-educated agents show more spread in ruin times.
  - Consumer agency must be treated as a value requiring active cultivation, not an inherent given.
  - Value deliberation interventions enable consumers to avoid ruin when income covers basic needs.
key_figures_tables:
  - "Figure 1: Summary of limited agency scenarios and outcomes → Visualizes how obligatory, impulsive, and temporal constraints lead to ruin."
  - "Figure A1: Ruin times under algorithmic persuasion → Most agents ruin within first 10 months under impulsive consumption."
  - "Figure A2: Ruin times by income level → Low-income agents ruin instantly; high-income show delayed but still rapid ruin."
  - "Figure A3: Ruin times by education → High-school diploma holders ruin within 20 steps; college degree holders show more spread."
key_equations:
  - equation: "max E[∑_{t=0}^{∞} β^t u(c_t)]"
    explanation: "Maximizes discounted utility over infinite horizon."
  - equation: "a_{t+1} = R(a_t - c_t) + y_t"
    explanation: "Asset evolution equation with return R and income y."
  - equation: "0 ≤ c_t ≤ a_t"
    explanation: "Consumption constrained by available assets."
  - equation: "Pr(a_T ≤ 0) ≥ 1 - exp(-cT)"
    explanation: "Probability of ruin grows exponentially with time."
definitions:
  - term: Ruin
    definition: "State where consumer assets reach zero within a finite time horizon."
  - term: Lookahead
    definition: "Number of future time steps an agent can perfectly foresee income and financial shocks."
  - term: Obligatory Consumption
    definition: "Fixed expenses driven by social, legal, or infrastructural pressures that limit consumer choice."
  - term: Algorithmic Persuasion
    definition: "Manipulative digital tactics that steer consumers toward impulsive spending."
  - term: Value Deliberation
    definition: "Active evaluation of competing needs and preferences to make consumption decisions aligned with personal values."
critical_citations:
  - "[Pariser, 2011] — Introduces filter bubbles and algorithmic curation."
  - "[Mathur et al., 2019] — Documents dark patterns in digital interfaces."
  - "[Nguyen, 2024] — Defines value capture in algorithmic systems."
  - "[Frederick et al., 2002] — Reviews time discounting and preference."
  - "[Schneider & Harknett, 2019] — Documents work schedule instability effects."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: low
      justification: "Discusses general consumer agency, not specific to Filipino young professionals."
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: low
      justification: "Uses U.S. income data and models, not Philippine-specific financial structures."
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: low
      justification: "Provides general behavioral insights applicable broadly."
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: high
      justification: "Formalizes predictable spending cycles through fixed obligatory consumption patterns."
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: medium
      justification: "Obligatory consumption framework applies to cultural spending cycles."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: "Identifies algorithmic manipulation and lack of agency as key system gaps."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: "Models rational agent behavior under agency constraints and proposes profiles for deliberation."
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: "Discusses adaptation and value deliberation over time."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: contextual
      justification: "Uses predictive models of ruin but does not focus on forecasting algorithms."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: contextual
      justification: "Mentions lookahead but not specific forecasting algorithms."
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: "Proposes value deliberation and budgeting as solutions to agency erosion."
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: "Demonstrates that deliberate consumption choices improve financial outcomes."
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: high
      justification: "Introduces minimum subsistence constraints and shows how to avoid ruin with proper budgeting."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: "Ruin analysis provides a framework for detecting financial instability."
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: "Mentions detection of impulsive spending but not specific algorithms."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: "Does not address privacy or security directly."
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: "Discusses transparency and ethical AI as trust-building mechanisms."
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: "Analyzes how algorithmic persuasion manipulates engagement and spending."
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: high
      justification: "Algorithmic tactics like scarcity and FOMO are explicitly linked to retention and spending."
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: "Proves that value deliberation and budgeting enable saving and avoid ruin."
  contribution: "This paper provides a formal framework for analyzing consumer agency erosion, which can inform Odin's design of user-facing budget recommendation and behavioral profiling modules. Its analytical models of ruin under limited agency justify the need for proactive intervention mechanisms in PFMS. The proposed value deliberation approach aligns with Odin's goal of fostering user autonomy and financial well-being. The theorem on lookahead utility directly supports incorporating schedule-aware features for users with variable income."
  directly_justifies:
    - "Even rational utility-maximizing agents can face financial ruin when agency is limited across structural, behavioral, or temporal dimensions."
    - "Value deliberation and budgeting interventions can help consumers avoid financial ruin when income covers basic needs."
    - "Workers with greater advance knowledge of income schedules achieve significantly higher utility, supporting the need for prediction-aware features."
    - "Algorithmic persuasion creates value capture where consumers adopt externally imposed consumption values without critical reflection."
  limits:
    - "Model assumes rational utility-maximizing agents, which may not reflect real-world behavioral biases."
    - "Does not include debt, credit, or liabilities in the formal model."
    - "Assumes societal uniformity; does not account for disparities in algorithmic targeting or policy access."
    - "Proposed interventions are high-level and lack specific implementation details for PFMS."
  mapping_rationale: "Systematic scan across all 12 functional domains identified 4 domains as highly relevant: Filipino Cultural Context (2.B, 2.D), Behavioral Profiling (5.A), Budget Recommendation (7.A, 7.D), and User Retention (11.A, 11.B). The paper's formal models of obligatory consumption (2.B) and algorithmic persuasion (11.A) provide direct justification for Odin's budgeting and engagement modules. The lookahead theorem (6.A, 6.B) supports forecasting features. Expense Categorization (3.A-C) and Anomaly Detection (8.A-C) were considered but rejected as the paper does not address categorization algorithms or anomaly detection techniques. Mobile-First Design (9.A, 9.B) and Data Privacy (10.A) were considered contextual. The paper's overall relevance to Odin is high, providing theoretical justification for user autonomy and proactive intervention features."
limitations:
  - "Intertemporal consumption model assumes rational utility-maximizing agents, simplifying real-world behavioral complexity."
  - "Debt and liabilities are not included in the formal framework."
  - "Model assumes societal uniformity and does not account for demographic disparities in algorithmic targeting."
  - "Proposed interventions are high-level and lack specific implementation details."
  - "Behavioral economics factors like present bias and loss aversion are acknowledged but not formally incorporated. [unacknowledged]"
  - "External macro-socioeconomic impacts like inflation and recessions are not modeled. [unacknowledged]"
remember_this:
  - "num: Even rational consumers can go to ruin under obligatory consumption with concave utility."
  - "num: Probability of avoiding ruin decays exponentially under impulsive consumption with minimum subsistence."
  - "num: Workers with advance schedule knowledge achieve Ω(k) higher utility than those without."
  - "Consumer agency must be actively cultivated as a value, not assumed as a given."
  - "Value deliberation and budgeting interventions enable consumers to avoid financial ruin."
```
---

## Paper 7: Gao J. et al_summarized.md

**Source File:** `Gao J. et al_summarized.md`

```yaml
paper_id: "10.1007/s10462-025-11255-1"
designation: "international"
title: "Agent-in-the-loop to distill expert knowledge into artificial intelligence models: a survey"
authors: "Gao, J.; Zhang, Y.; Chen, Y.; Dong, Y.; Chen, Y.; Song, S.; Tang, B.; Gu, Y."
year: 2025
venue: "Artificial Intelligence Review"
odin_topics:
  - "5.B"
  - "6.A"
  - "7.B"
  - "8.A"
  - "12.A"
  - "4.B"
tldr: "Surveys Agent-in-the-Loop Machine Learning, integrating humans and large models as agents to distill expert knowledge into AI models across data processing and model development."
problem_and_motivation: "Large neural networks underperform in expert domains due to data sparsity and annotation costs. Human-in-the-loop ML integrates expert knowledge, but large models now offer new opportunities as agents. This survey proposes AIL-ML to unify human and large model collaboration, addressing the need for cost-effective and accurate vertical AI models."
approach:
  - "Proposes AIL-ML framework unifying humans and large models as agents in the ML loop."
  - "Categorizes methods into data acquisition/processing (collection, initialization, quality, annotation) and model development/optimization (cold start, training, iterative refinement)."
  - "Provides mathematical formalizations for each stage, e.g., data collection as x_t = f(S_t, D_t, M_t, A_t)."
  - "Reviews representative works from top conferences and arXiv (2018–2024) across HCI and ML."
  - "Discusses applications in general knowledge (smart homes, dialogue) and specialized domains (healthcare, finance, law)."
  - "Highlights challenges: lack of standardized methodologies, LLM biases, and high-dimensional data handling."
findings:
  - "AIL-ML reduces reliance on manual annotation by leveraging LLMs as proxies for human expertise."
  - "Iterative feedback from humans and LLMs improves model alignment with user intentions and adaptability."
  - "Cold start can be mitigated via LLM-generated initial datasets or transfer learning from related domains."
  - "num: Using GPT-3 for data annotation can reduce costs by 50% to 96% compared to manual annotation."
  - "AIL-ML enhances model performance in expert domains by integrating domain-specific knowledge through active learning and interactive refinement."
key_figures_tables:
  - "Figure 1: HIL-ML workflow with four stages → Shows continuous human involvement throughout ML loop."
  - "Figure 2: AIL-ML methodology framework → Divides into data processing and model development phases."
  - "Figure 3: Taxonomy of AIL-ML methods → Details subcategories under data and model stages."
  - "Figure 4: Annotation methods by degree of freedom → Classifies fixed-choice, range selection, open input."
  - "Figure 5: Strategies to reduce annotation costs → Data selection, process optimization, and hierarchical agents."
key_equations:
  - equation: "x_t = f(S_t, D_t, M_t, A_t)"
    explanation: "Data collection as function of seeds, dataset, model, and agent actions."
  - equation: "F_t = ψ(D_t, A_t, P_f)"
    explanation: "Feature representation from data, agent input, and preprocessing parameters."
  - equation: "D_{t+1} = θ(D_t, A_t, Q)"
    explanation: "Data quality enhancement via agent actions and quality parameters."
  - equation: "L_t = γ(D_t', A_t, Σ_t, Ω_t)"
    explanation: "Annotation output from selected samples, agent input, strategies, and output options."
  - equation: "M_{t+1} = ϕ(M_t, D_t, A_t, Θ_t)"
    explanation: "Model training update integrating agent insights and training parameters."
definitions:
  - term: "AIL-ML"
    definition: "Agent-in-the-Loop Machine Learning, integrating humans and large models as agents in the ML loop."
  - term: "HIL-ML"
    definition: "Human-in-the-Loop Machine Learning, incorporating human knowledge into the modeling process."
  - term: "LLM"
    definition: "Large Language Model, a neural network with billions of parameters trained on vast text data."
  - term: "Active Learning"
    definition: "ML approach where the model queries an oracle to label informative examples."
  - term: "Knowledge Distillation"
    definition: "Transferring knowledge from a larger teacher model to a smaller student model."
critical_citations:
  - "[Wu et al., 2022] — Comprehensive HIL-ML survey from data management perspective."
  - "[Mosqueira-Rey et al., 2023a] — Theoretical framework for HIL interaction types."
  - "[Brown et al., 2020] — Introduced GPT-3 as a few-shot learner and LLM capabilities."
  - "[Cui et al., 2021] — Analyzed interaction-outcome relationships in HIL."
relevance:
  topics:
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "high"
      justification: "Dedicates a section to model cold start, using LLM-generated data or transfer learning."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Covers model training and optimization techniques applicable to forecasting modules."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses interactive refinement with user feedback, relevant for recommendation personalization."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "low"
      justification: "Addresses error detection and uncertainty handling, tangentially related to anomaly detection."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews evaluation approaches for AIL-ML systems, can inform Odin's evaluation design."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "contextual"
      justification: "Highlights limitations of traditional ML in expert domains, parallels PFMS gaps."
  contribution: "This survey provides a systematic framework for AIL-ML that can guide Odin's design in areas like cold-start handling, data annotation, and iterative model improvement. The mathematical formalizations offer a theoretical foundation for implementing agent-assisted modules in Odin. The discussion on reducing annotation costs via LLMs is directly applicable to Odin's need for efficient data labeling. The emphasis on user feedback loops supports Odin's engagement and personalization features. Overall, the framework informs the development of robust, adaptive ML components for personal finance management."
  directly_justifies:
    - "AIL-ML can reduce manual annotation costs via LLM pseudo-labeling, enabling cost-effective data preparation for Odin."
    - "Iterative user feedback improves model alignment with user intentions, supporting personalized budget recommendations."
    - "Cold start can be addressed by transfer learning or LLM-generated initial data, critical for new Odin users."
    - "Agent-in-the-loop frameworks enhance model adaptability to changing user behavior over time."
  limits:
    - "The survey does not address specific financial or spending data characteristics."
    - "None identified."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains of Behavioral Profiling & Classification (5.A/B/C), Spending Forecasting (6.A/B), Budget Recommendation (7.A-D), Anomaly Detection (8.A-C), and System Evaluation (12.A-C) were flagged as relevant. Specifically, topic 5.B (cold start) received high relevance due to the paper's dedicated section on model cold start. Topics 6.A and 7.B were assigned medium relevance because the survey covers model training and iterative refinement, which are foundational for predictive and recommendation modules. Topic 8.A (anomaly detection) received low relevance as the paper focuses on error detection rather than financial anomaly detection. Topic 12.A (evaluation) was medium, as the paper reviews evaluation approaches for AIL-ML systems. Topic 4.B (limitations of existing systems) was contextual, providing background on general ML limitations. Domains like Filipino Cultural Context (2.A-D), Expense Categorization (3.A-C), and Mobile-First Design (9.A-B) were considered but rejected due to lack of direct coverage. The overall relevance to Odin lies in providing a methodological blueprint for integrating human and LLM agents into the ML pipeline, which can improve accuracy, reduce costs, and enhance user trust."
limitations:
  - "AIL-ML lacks standardized methodologies and evaluation criteria, making it a guiding philosophy rather than a technical toolkit."
  - "Reliance on LLM performance in specialized domains may introduce inaccuracies or biases."
  - "LLMs are often black boxes, limiting transparency in high-stakes applications."
  - "Human and LLM biases can propagate through feedback loops if not carefully managed."
  - "Current AIL-ML methods are primarily designed for low-dimensional or natural language data, not high-dimensional unstructured data."
remember_this:
  - "AIL-ML unifies human and LLM agents to reduce annotation costs and improve model performance."
  - "Iterative feedback from agents enhances model adaptability and user alignment."
  - "Cold start can be tackled via LLM-generated datasets or transfer learning."
  - "num: GPT-3 labeling can cut costs by up to 96% compared to manual annotation."
  - "Standardization and bias mitigation remain key challenges for AIL-ML adoption."
  ```
---

## Paper 8: Kalideen_summarized.md

**Source File:** `Kalideen_summarized.md`

```yaml
paper_id: "5b6d4f4e-8f0f-5b1e-9e5a-1c7f8f3f5f5a"
designation: "international-algorithm-specific"
title: "Detection of Fraudulent Transaction Issues in the Payment Card Industry using Machine Learning: A Comprehensive Survey"
authors: "Kalideen, M. R."
year: 2025
venue: "Journal of Information and Communication Technology"
odin_topics:
  - "4.A"
  - "4.B"
  - "5.A"
  - "5.B"
  - "5.C"
  - "8.A"
  - "8.B"
  - "8.C"
  - "10.A"
  - "10.B"
  - "12.A"
  - "12.B"
  - "12.C"
tldr: "A comprehensive survey of machine learning and deep learning techniques for payment card fraud detection, addressing challenges like imbalanced data and model interpretability, and exploring emerging trends such as explainable AI and privacy-preserving methods."
problem_and_motivation: "The rapid growth of digital payment card transactions has been paralleled by a surge in fraudulent activities, posing significant challenges to the financial industry. Traditional rule-based fraud detection methods are often static and inflexible, struggling to adapt to the ever-evolving tactics of fraudsters. There is a critical need for more advanced, adaptable, and accurate solutions like machine learning to safeguard financial systems."
approach:
  - "A systematic literature search was conducted in IEEE Xplore, Scopus, and PubMed using keywords related to credit card fraud, machine learning, and anomaly detection."
  - "The search was limited to English-language studies published between 2010 and 2024, with 49 studies meeting the final inclusion criteria after screening."
  - "The review covers a diverse array of algorithms including supervised, unsupervised, and hybrid learning methods, as well as deep learning architectures like DNNs, RNNs, Autoencoders, and GANs."
  - "Strengths and limitations of models are discussed in the context of challenges like imbalanced datasets, model interpretability, scalability, and security."
  - "Emerging trends such as explainable AI (XAI), privacy-preserving machine learning, and blockchain technology are also examined."
findings:
  - "num: Fraudulent transactions typically make up less than 1% of all transactions, leading to severe class imbalance."
  - "Deep learning models have exhibited exceptional performance in fraud detection, often outperforming conventional methods."
  - "Imbalanced datasets cause models to be biased toward the majority class, resulting in low recall for fraudulent transactions."
  - "Model interpretability is a major challenge for deep learning, as they function as 'black boxes,' hindering trust and regulatory compliance."
  - "Explainable AI is crucial for transparency, helping to build trust, meet regulatory requirements, and improve model accuracy."
  - "Privacy-preserving machine learning techniques are becoming critical to address privacy concerns and ensure compliance with laws like GDPR."
  - "Ensemble methods are particularly effective, offering higher overall accuracy, robustness to noise, and better generalization."
  - "Adversarial attacks pose a significant threat, where small changes to input data can lead to model misclassification."
  - "Federated learning allows for collaborative model training across institutions without sharing raw data, preserving privacy."
  - "The review provides actionable recommendations for practitioners and identifies promising future research directions."
key_figures_tables:
  - "Table I: Traditional Fraud Detection vs. Machine Learning in Fraud Detection → Compares adaptability, accuracy, and scalability of approaches."
  - "Table II: Widely Used Supervised Learning Algorithms for Fraud Detection → Summarizes logistic regression, SVM, decision trees, random forests, and neural networks."
  - "Table III: Deep Learning Techniques Used in Fraud Detection → Outlines DNN, RNN, Autoencoders, and GANs with their applications."
  - "Table IV: Ensemble Methods Used in Fraud Detection → Describes bagging, boosting, random forests, and stacking."
  - "Table V: Comparison of Machine Learning Techniques Used in Fraud Detection → Contrasts supervised, unsupervised, semi-supervised/hybrid, deep learning, and ensemble methods."
  - "Table VI: Comparison of Different Evaluation Metrics Used in Machine Learning → Analyzes accuracy, precision, recall, F1-score, AUC-ROC, and average precision."
key_equations:
  - equation: "Precision = True Positives / (True Positives + False Positives)"
    explanation: "Measures accuracy of positive predictions."
  - equation: "Recall = True Positives / (True Positives + False Negatives)"
    explanation: "Measures ability to find all positive instances."
  - equation: "F1-Score = 2 * (Precision * Recall) / (Precision + Recall)"
    explanation: "Harmonic mean of precision and recall."
definitions:
  - term: "XAI"
    definition: "Explainable Artificial Intelligence, a set of processes and methods that allows human users to understand and trust the results and output created by machine learning algorithms."
  - term: "PPML"
    definition: "Privacy-Preserving Machine Learning, techniques to train models on sensitive data without compromising individual privacy."
  - term: "GAN"
    definition: "Generative Adversarial Network, a class of machine learning frameworks where two neural networks contest with each other to generate new, synthetic instances of data."
  - term: "AUC-ROC"
    definition: "Area Under the Receiver Operating Characteristic curve, a performance metric that summarizes the trade-off between true positive and false positive rates."
critical_citations:
  - "[Yundong, 2023] — Foundational overview of logistic regression and random forest for fraud detection."
  - "[Kumar & Dwivedi, 2020] — Key study on unsupervised learning for fraud detection."
  - "[Rudin, 2019] — Seminal paper arguing for interpretable models over black boxes for high-stakes decisions."
  - "[Phua et al., 2010] — Comprehensive early survey on data mining-based fraud detection research."
relevance:
  topics:
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Provides context for traditional fraud detection methods within existing financial systems."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Explicitly details the limitations of traditional rule-based systems and the need for machine learning."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Discusses how ML models learn spending patterns to identify anomalies, which relates to behavioral profiling."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "low"
      justification: "Mentions the challenge of imbalanced datasets but not directly the cold-start problem for new users."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "Reviews supervised and unsupervised classification algorithms for fraud, which parallel profile classification."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "The core topic is anomaly detection for fraudulent transactions in payment systems."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Provides a comprehensive survey and comparison of various algorithms, including deep learning and ensembles."
    - code: "8.C"
      name: "Cold‑Start Baseline Strategies for Anomaly Detection"
      relevance: "low"
      justification: "Discusses imbalanced data but not specifically cold-start baseline strategies."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses privacy concerns and adversarial attacks, which are key to security."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "medium"
      justification: "Highlights the importance of model interpretability for building trust."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses evaluation metrics like precision, recall, F1-score, and AUC-ROC."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Compares the performance of different ML algorithms for fraud detection."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "contextual"
      justification: "Relevant to evaluation methodologies in general, though not specific to budget recommendation."
  contribution: "This survey provides a comprehensive review of machine learning techniques for fraud detection, which is directly applicable to Odin's anomaly detection module. The analysis of algorithm strengths and weaknesses informs the selection of techniques for identifying irregular spending. The discussion on evaluation metrics is crucial for assessing Odin's detection performance. The exploration of privacy-preserving methods guides the design of secure and trustworthy financial systems."
  directly_justifies:
    - "Machine learning can learn intricate patterns and relationships from extensive datasets to identify subtle indicators of fraud."
    - "Ensemble methods like Random Forest and XGBoost are inherently better suited for handling imbalanced datasets."
    - "Explainable AI (XAI) is crucial for transparency and building user trust in automated financial decisions."
    - "Federated learning enables collaborative model training without compromising customer privacy."
    - "Adversarial attacks pose a significant threat to machine learning models in finance."
  limits:
    - "The survey does not provide empirical results or benchmark specific algorithms on a common dataset."
    - "The specific details of the datasets used in the reviewed studies are often not provided due to privacy concerns."
    - "The review is limited to studies published up to 2024, potentially missing very recent developments."
    - "The paper focuses on payment card fraud and may not be directly transferable to other types of personal finance anomalies."
  mapping_rationale: "A systematic scan across all 12 functional domains was performed. The domains 'Anomaly Detection' and 'Existing Systems & Gaps' were flagged as highly relevant because the paper directly addresses machine learning for fraud detection and critiques traditional methods. Domains like 'Behavioral Profiling & Classification', 'Data Privacy & User Trust', and 'System Evaluation' were deemed medium relevance, as the paper discusses classification approaches, privacy (PPML), trust (XAI), and performance metrics. The 'Savings & Debt Management' and 'Budget Recommendation' domains were considered not applicable. Borderline cases included the discussion of spending patterns for anomaly detection, which was mapped to 5.A, while topics like 2.D were rejected because the analysis is not culturally specific to the Philippines. The overall relevance to Odin is high for the anomaly detection module and offers supporting insights for privacy, trust, and evaluation."
limitations:
  - "Relies on secondary sources (surveys) rather than primary experimental data. [unacknowledged]"
  - "Findings are based on general international literature and may not fully reflect the Filipino context."
  - "The survey does not propose a novel algorithm or system."
remember_this:
  - "Fraudulent transactions comprise less than 1% of all transactions."
  - "Deep learning models offer superior accuracy but suffer from a lack of interpretability."
  - "Explainable AI is essential for building trust in automated financial systems."
  - "Federated learning offers a path to privacy-preserving collaborative model training."
  - "Ensemble methods like Random Forest are robust and handle imbalanced data well."
```
---

## Paper 9: Bancoro et al_summarized.md

**Source File:** `Bancoro et al_summarized.md`

```yaml
paper_id: 10.69569/jip.2025.015
designation: local
title: The Role of Financial Literacy in Supporting Employee Work-Life Balance
authors: Bancoro, J.C.; Barillo, R.M.; Buhian, D.L.
year: 2025
venue: Journal of Interdisciplinary Perspectives
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.D
  - 3.A
  - 4.A
  - 4.B
  - 11.A
  - 13.A
  - 13.B
tldr: Financial literacy correlates weakly with work-life balance, yet employees show positive financial attitudes and behaviors, with qualitative findings suggesting indirect stress-reduction benefits.
problem_and_motivation: Financial stress from low literacy undermines work-life balance, but empirical evidence directly linking literacy to balance outcomes is scarce. Understanding this relationship is critical for designing workplace interventions that improve employee well-being and productivity.
approach:
  - A correlational descriptive design was used with 140 faculty and staff from a Philippine state university.
  - Quantitative surveys assessed financial knowledge, attitudes, behaviors, and work-life balance perceptions.
  - Semi-structured interviews with eight employees provided qualitative depth on financial management experiences.
  - Spearman correlation (rho) tested the relationship between financial literacy and work-life balance.
  - Cronbach's alpha (0.83-0.85) confirmed high internal consistency for survey dimensions.
findings:
  - num: Financial knowledge mean score was 8.35 out of 13 (SD = 3.13), indicating moderate literacy with high variability.
  - num: The correlation between financial literacy and work-life balance was weak and non-significant (rho = 0.11, p = 0.191).
  - Employees demonstrated positive financial attitudes (M = 3.99, SD = 0.73) and behaviors (M = 3.94, SD = 0.58).
  - Employees reported good work-life balance (M = 4.06, SD = 0.60), with flexibility and supervisor support as key contributors.
  - Qualitative data revealed that financial literacy reduces financial stress, enabling better focus on personal and professional priorities.
key_figures_tables:
  - Table 1: Summary of financial knowledge, attitudes, and behaviors → shows moderate knowledge with positive attitudes and behaviors.
  - Table 5: Correlation between financial literacy and work-life balance → indicates no significant relationship (rho = 0.11, p = 0.191).
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Financial Literacy
    definition: The ability to make sound financial decisions, including budgeting, saving, investing, and planning for future security.
  - term: Work-Life Balance
    definition: The relationship between work obligations and activities outside work, impacting well-being, job satisfaction, and effectiveness.
  - term: Conservation of Resources (COR) Theory
    definition: A theory positing that individuals seek to obtain, protect, and build resources to minimize stress and handle challenges.
critical_citations:
  - "[Ryu & Fan, 2022] — Establishes link between financial worries and psychological distress."
  - "[Hu et al., 2024] — Shows financial literacy reduces mortgage stress by 60%."
  - "[Galapon & Bool, 2022] — Finds financial behavior, not literacy, predicts well-being."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: The study focuses on Filipino university employees, a core demographic for Odin.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Provides data on income, savings, and spending behaviors of Filipino employees.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly measures financial behaviors (budgeting, saving, spending) of Filipino employees.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Discusses Filipino-specific financial practices like Pag-IBIG MP2 savings and cooperative loans.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Mentions financial constraints and spending pressures, indirectly touching on spending cycles.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: low
      justification: Implicitly involves expense tracking and budgeting behaviors, foundational to categorization.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Mentions financial tools and apps (Mint, YNAB) as part of the financial management landscape.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: low
      justification: Identifies gaps in financial education and support, relevant to system design limitations.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: contextual
      justification: Suggests financial literacy workshops and tools, touching on user engagement mechanisms.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: Relates to saving behaviors and goals (e.g., children's education, retirement) which are core to savings management.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: low
      justification: Mentions avoiding debt and managing loans, relevant to debt management features.
  contribution: This paper provides empirical evidence on the weak direct link between financial literacy and work-life balance, suggesting that Odin should prioritize behavioral interventions over purely educational content. It highlights the importance of supportive workplace policies, which can inform Odin's design for user engagement and retention. The findings underscore the need for Odin to integrate financial education with practical tools that facilitate behavior change, such as automated savings and spending trackers. The study also validates the use of COR Theory as a framework for understanding how financial resources reduce stress, which can guide Odin's approach to user trust and data privacy.
  directly_justifies:
    - Financial literacy alone does not strongly predict work-life balance outcomes.
    - Positive financial behaviors are more closely associated with well-being than knowledge alone.
    - Work-life balance policies are insufficient without addressing financial stress and workload.
    - Tailored financial education programs should focus on behavioral change and personalized coaching.
    - Providing financial planning tools and resources can empower users to manage finances effectively.
  limits:
    - The study is cross-sectional, limiting causal inferences about financial literacy and work-life balance.
    - The sample is confined to one state university in the Philippines, reducing generalizability.
    - Reliance on self-reported data may introduce social desirability or recall bias.
    - The weak correlation may reflect the specific measures used, which may not capture all dimensions of financial literacy or work-life balance.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was conducted to map this paper to Odin's RRL. The domain of Filipino Cultural Context was flagged as highly relevant, with topics 1.A, 1.B, and 1.C receiving high relevance due to the paper's focus on Filipino employees' financial knowledge, attitudes, and behaviors. Topics 2.A and 2.D were assigned medium and low relevance, respectively, for their discussion of culturally specific practices and spending constraints. Expense Categorization (3.A) received low relevance due to implicit expense tracking behaviors. Existing Systems & Gaps (4.A, 4.B) were rated low for mentioning financial tools and gaps in financial education. User Retention & Engagement (11.A) was deemed contextual for its suggestion of financial workshops. Savings & Debt Management (13.A, 13.B) were rated low for discussing saving behaviors and debt avoidance. Domains such as Behavioral Profiling (5.A-C), Spending Forecasting (6.A-B), Budget Recommendation (7.A-D), Anomaly Detection (8.A-C), Mobile-First Design (9.A-B), Data Privacy (10.A-B), and System Evaluation (12.A-C) were rejected as the paper does not address these algorithmic, design, or evaluation concerns. The paper's overall relevance to Odin is moderate, providing foundational insights into Filipino financial behaviors and the indirect role of literacy in stress reduction, which informs feature design for engagement and savings management.
limitations:
  - Cross-sectional design precludes causal conclusions.
  - Sample limited to one state university, limiting generalizability.
  - Self-reported data may be subject to bias.
  - Weak correlation may reflect measurement limitations for financial literacy or work-life balance.
remember_this:
  - Financial literacy shows a weak, non-significant correlation with work-life balance.
  - Employees demonstrate positive financial attitudes but moderate and variable knowledge.
  - Work-life balance is more strongly tied to workplace flexibility and support.
  - Qualitative data suggests financial literacy reduces stress, indirectly aiding balance.
  - Tailored financial education and behavioral tools are recommended over generic literacy programs.
```
---

## Paper 10: Saghafi et al_summarized.md

**Source File:** `Saghafi et al_summarized.md`

```yaml
paper_id: 10.1016/j.dss.2025.114499
designation: international
title: Impact of categorization autonomy on effective use and adoption intentions
authors: Saghafi, A.; Medappa, P.; Debrliev, A.
year: 2025
venue: Decision Support Systems
odin_topics:
  - 3.A
  - 5.A
  - 5.C
  - 9.B
  - 10.B
  - 11.A
tldr: User-defined categorization schemes improve search precision and usage intentions compared to fixed hierarchies, particularly for exploratory tasks.
problem_and_motivation: Predefined categorization trees may not align with individual users' cognitive schemas, potentially hindering effective information assimilation and decision-making. The impact of allowing users to create their own categorization hierarchies from base object types remains unexplored. This gap limits the potential for designing decision support systems that better fit users' mental models and task demands.
approach:
  - Conducted an online laboratory experiment with 201 Amazon Mechanical Turk workers as surrogates for e-commerce users.
  - Developed a functional experimental website with over 10,000 products scraped from a major North American e-retailer.
  - Manipulated categorization autonomy at three levels: fixed (control), partial autonomy (fixed top two levels), and full autonomy (user-defined hierarchy).
  - Task flexibility was manipulated as a moderator via closed-ended (exploitive) and open-ended (exploratory) search scenarios.
  - Search precision was measured as the ratio of correctly identified items to the total required items, while usage intentions were measured via survey scales.
findings:
  - num: Categorization autonomy led to significantly higher search precision (full autonomy outperformed fixed categorization by 0.155, p < 0.01).
  - num: Task flexibility significantly moderated the effect, with categorization autonomy being more beneficial for high-flexibility tasks (interaction effect 0.179, p < 0.01).
  - num: Full categorization autonomy increased usage intentions compared to fixed categorization (0.359, p < 0.01).
  - Perceived restrictiveness mediated the relationship between categorization autonomy and usage intentions for fixed vs. full autonomy comparisons.
  - num: Users' self-defined category trees were highly diverse, with a maximum cosine similarity of 0.58 between participants, and a mean similarity of 0.36 to the baseline retailer's scheme.
  - The openness personality trait was a significant predictor of greater dissimilarity from the baseline category scheme.
key_figures_tables:
  - Figure 1: Nomological research model → Shows hypothesized relationships among categorization autonomy, task flexibility, restrictiveness, and outcomes.
  - Table 2: Regression analysis for impact of categorization autonomy on search precision → Confirms main effect of autonomy on precision.
  - Table 3: Regression analysis for moderation effect of task flexibility → Shows autonomy's effect is stronger for flexible tasks.
  - Table 4: Regression analysis for effect on usage intentions → Confirms autonomy increases usage intentions.
  - Table 5: Analysis on mediation effect of restrictiveness → Shows restrictiveness mediates autonomy's effect on usage intentions.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Categorization autonomy
    definition: The extent to which users have the ability to define their own categorization schemes from a base level of object types.
  - term: Task flexibility
    definition: The extent to which a task allows for multiple ways of achieving the desired outcome.
  - term: Effective use
    definition: Using a system in a way that helps attain the goals for using the system, operationally assessed by performance.
  - term: Perceived restrictiveness
    definition: The extent to which a system constrains the user's decision-making processes to a particular subset of all possible processes.
critical_citations:
  - "[Burton-Jones & Grange, 2013] — Defines effective use as goal-attainment performance."
  - "[Vessey, 1991] — Establishes Cognitive Fit Theory linking representation to task performance."
  - "[Goodhue & Thompson, 1995] — Task-Technology Fit theory explaining system performance."
  - "[Wang & Benbasat, 2009] — Links perceived restrictiveness to usage intentions."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Directly investigates how user-defined categorization schemes improve performance and perceptions.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Provides evidence that individual cognitive schemas (profiles) lead to divergent category structures.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Demonstrates that allowing user-driven classification improves outcomes compared to fixed, one-size-fits-all approaches.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Categorization autonomy is a UX design principle directly applicable to PFMS interface design.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Shows autonomy increases trust, which mediates satisfaction and usage intentions (Appendix D).
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Autonomy increases usage intentions and satisfaction, key drivers of engagement.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: While not directly about Filipino spending, the concept of user-defined categories could support tracking cyclical or occasion-based spending.
    - code: 3.C
      name: User-Defined Allocation Constraints
      relevance: low
      justification: Autonomy in categorization is a prerequisite for user-defined allocation but not directly studied.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: contextual
      justification: Categorization autonomy is foundational for personalized recommendations but not the focus.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Mentions YNAB as an example but does not systematically review PFMS landscape.
  contribution: "This paper provides strong empirical justification for designing Odin with user-defined expense categories (3.A, 5.A). It validates that allowing users to structure their own financial data aligns with their cognitive schemas, improving both objective task performance (search precision) and subjective perceptions like trust and satisfaction, which are critical for Odin's adoption. The findings directly support Odin's mobile-first design (9.B) by demonstrating that personalized information structures enhance user experience. Furthermore, the mediating role of trust (10.B) and the impact on usage intentions (11.A) are foundational for Odin's retention and engagement strategies. The results also inform Odin's approach to behavioral profiling (5.C) by showing that profiles should be inferred from user-defined structures rather than imposed from the system."
  directly_justifies:
    - "User-defined categorization improves search precision compared to fixed taxonomies (Saghafi et al., 2025)."
    - "Categorization autonomy leads to higher usage intentions (Saghafi et al., 2025)."
    - "The benefits of categorization autonomy are stronger for exploratory, high-flexibility tasks (Saghafi et al., 2025)."
    - "Perceived restrictiveness mediates the effect of autonomy on usage intentions (Saghafi et al., 2025)."
    - "Users with higher openness create categorization trees more dissimilar to baseline schemes (Saghafi et al., 2025)."
  limits:
    - "Study was conducted in an e-commerce context, not a personal finance management system."
    - "Participants were US/Canadian AMT workers, not specifically Filipino young professionals."
    - "The experimental setting involved a one-time task, not longitudinal use which may affect cognitive fit."
    - "Search function was disabled to isolate the effect of categorization, limiting generalizability to real-world systems where both search and browse are available."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to Expense Categorization Frameworks (3.A), Financial Behavioral Profiles (5.A), and Classification Approaches (5.C), as its core contribution directly addresses how user-defined categorization improves performance and aligns with individual cognitive schemas. Medium relevance was assigned to Mobile UX Design (9.B), User Trust (10.B), and Engagement Dynamics (11.A), as the findings on autonomy, trust, satisfaction, and usage intentions have clear implications for these areas. Low relevance was noted for Filipino Spending Cycles (2.D) and User-Defined Allocation Constraints (3.C), as the paper does not directly address these but provides conceptual groundwork. Domains such as Forecasting (6), Budget Recommendation (7), Anomaly Detection (8), and System Evaluation (12) were considered and rejected, as the paper does not address these algorithmic functions. The paper's overall relevance to Odin is high, providing foundational evidence for user-controlled categorization, which is central to Odin's behavioral profiling and user experience design."
limitations:
  - "The study was conducted in an e-commerce context, limiting direct generalizability to PFMS. [unacknowledged]"
  - "Participants were not Filipino young professionals, reducing cultural relevance. [unacknowledged]"
  - "The experimental task was a one-time interaction, not capturing longitudinal effects of categorization autonomy. [unacknowledged]"
  - "Search functionality was removed, which may not reflect real-world mixed-use systems. [unacknowledged]"
  - "The simplification of tasks may not capture the full spectrum of information requirements for financial management."
remember_this:
  - "User-defined categories improve search precision by 0.155 over fixed hierarchies."
  - "Autonomy is more effective for flexible, exploratory tasks than rigid ones."
  - "Categorization autonomy increases usage intentions and trust in the system."
  - "Individuals create unique category trees that differ from vendor baselines."
  - "Openness personality trait predicts greater divergence from predefined schemes."
```
---

## Paper 11: Casalhay et al_summarized.md

**Source File:** `Casalhay et al_summarized.md`

```yaml
paper_id: 10.55248/gengpi.6.0525.1716
designation: local
title: The Gig Economy: Financial Challenges and Opportunities Faced by Freelancers
authors: Casalhay, S. F.; Guevarra, C. M.; Bragas, C. M.
year: 2025
venue: International Journal of Research Publication and Reviews
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 8.A
  - 10.A
  - 10.B
  - 13.A
  - 13.B
tldr: Freelancers in the gig economy face income volatility, lack of benefits, and barriers to financial services, requiring tailored products and systemic reforms.
problem_and_motivation: Freelancers face significant financial challenges due to income volatility, lack of traditional employment benefits, and limited access to financial services. The gig economy's growth lacks corresponding support structures, leaving freelancers financially vulnerable and without adequate safety nets. Existing literature often overlooks the specific financial behaviors and coping strategies of freelancers, creating a gap in understanding how to support their long-term financial stability.
approach:
  - A qualitative research design was employed to explore the lived experiences of freelancers in the gig economy.
  - Data was collected through semi-structured interviews with 50 freelancers in Metro Manila across diverse fields like writing, graphic design, and virtual assistance.
  - Purposive and snowball sampling were used to select participants with at least six months of gig work experience.
  - Thematic analysis was used to identify and interpret patterns in participants' responses regarding financial challenges and opportunities.
  - An interview guide was pre-tested with 2-3 freelancers to ensure clarity and relevance of the questions.
findings:
  - Income instability is a primary challenge, driven by seasonal fluctuations, client behavior, and the short-term nature of projects.
  - Freelancers lack access to employer-sponsored benefits like health insurance and retirement plans, increasing their financial burden.
  - Barriers to financial services are significant, as banks view freelancers as high-risk borrowers due to irregular income.
  - The financial challenges cause significant stress, anxiety, and lifestyle limitations, impacting mental and social well-being.
  - Freelancers employ strategies like strict budgeting, emergency funds, and digital tools, but these are often insufficient for long-term security.
  - There is a strong demand for systemic reforms, including government-supported safety nets and legal protections for freelancers.
  - Innovative financial products like micro-savings platforms and income-smoothing tools are recognized but often have high costs or limited accessibility.
  - Continuous upskilling is necessary for competitiveness, but limited funds hinder investment in professional development.
  - Freelancers rely on manual tracking, budgeting apps, and spreadsheets to manage finances, but tools cannot fully solve income irregularity.
  - Respondents expressed a need for financial education, better loan options, and institutional recognition of freelancing as a legitimate career.
key_figures_tables:
  - Table 1: Financial challenges (income instability, benefit access, service barriers) → summarizes core problems faced by freelancers.
  - Table 2: Financial management practices (budgeting, saving, tools) → shows reactive strategies used to mitigate income volatility.
  - Table 3: Means of income stability (fluctuations, healthcare, policy) → identifies desired support for long-term financial security.
  - Table 4: Financial opportunities (knowledge, products, support needs) → highlights awareness gaps and demand for tailored financial solutions.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Gig Economy
    definition: A labor market characterized by short-term, flexible, and task-based work, often mediated by digital platforms.
  - term: Freelancer
    definition: An independent worker who offers services to clients on a project or contract basis, without long-term employment commitment.
  - term: Income Volatility
    definition: The unpredictable fluctuation in earnings, which is a common challenge for freelancers with irregular workloads.
  - term: PFMS
    definition: Personal Finance Management System, a software application designed to help individuals manage their financial activities.
critical_citations:
  - "[De Stefano, 2016] — Foundation for precarious employment theory in gig work."
  - "[Hwang, 2024] — Income volatility as a core gig economy feature."
  - "[McNeal, 2024] — Financial burden of lacking employer-sponsored benefits."
  - "[Peetz et al., 2021] — Link between income volatility and financial planning."
  - "[Minter, 2017] — Barriers to financial services for freelancers."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: Focuses on freelancers in Metro Manila, a key demographic for Odin.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Details income sources and financial management practices relevant to understanding their financial structure.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly examines the financial behaviors, coping strategies, and challenges of freelancers.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Discusses financial management practices like budgeting and saving within a Filipino context.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: high
      justification: Identifies seasonal fluctuations and income peaks/dips as major challenges for freelancers.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: medium
      justification: Mentions lifestyle limitations and delayed major life decisions due to financial uncertainty, relating to spending cycles.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Freelancers track expenses and categorize spending for budgeting, aligning with this topic.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: low
      justification: Touches on prioritizing expenses (needs vs. wants), but does not delve into framework design.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Mentions use of digital financial tools and apps but does not analyze the PFMS landscape.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Explicitly identifies gaps in financial services and products for freelancers, a key limitation.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Describes varying financial management practices, suggesting different behavioral profiles.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: contextual
      justification: Highlights the challenge of new freelancers with no financial history, relating to cold-start.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: The paper mentions financial stress and anxiety due to income irregularity, which anomaly detection systems could potentially address.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Not a central theme of the paper.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: contextual
      justification: Freelancers express a need for trustworthy financial products and institutions, linking to user trust.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Discusses emergency funds and surplus-based saving, both core to savings goal management.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: medium
      justification: Mentions difficulty accessing loans and credit, which is relevant to debt management challenges.
  contribution: This paper provides qualitative evidence on the financial vulnerabilities of freelancers, which informs Odin's user modeling by highlighting the challenges of income volatility and benefit access. The identification of reactive coping strategies (e.g., budgeting, emergency savings) validates the need for proactive, predictive features in Odin. The expressed demand for tailored financial products, such as income-smoothing tools and accessible credit, directly justifies Odin's modules for forecasting, budget recommendation, and anomaly detection. Furthermore, the paper's findings on the lack of institutional support and financial literacy underscore the importance of Odin's design to provide clear, trustworthy, and educational financial guidance.
  directly_justifies:
    - "Freelancers lack access to traditional financial services, justifying Odin's need for inclusive design."
    - "Income volatility is a major challenge, supporting Odin's focus on predictive modeling for irregular income."
    - "Coping strategies are often reactive, highlighting the need for proactive and automated financial management tools."
    - "The demand for income-smoothing tools justifies Odin's focus on smoothing spending and income patterns."
    - "Lack of benefits like health insurance supports Odin's need to incorporate savings goals for such expenses."
  limits:
    - "Focuses on freelancers in Metro Manila only, limiting generalizability to other regions in the Philippines."
    - "Qualitative study design with a sample size of 50, which may not capture the full diversity of the freelance population."
    - "The study relies on self-reported data, which may be subject to recall bias or social desirability bias."
    - "[unacknowledged] The study does not quantify the prevalence of specific financial challenges among different freelancer subgroups." 
    - "[unacknowledged] The study does not evaluate the effectiveness of the specific financial tools mentioned by participants."
  mapping_rationale: A systematic scan of all 12 functional domains and associated topic codes was performed. The paper was flagged as highly relevant to the 'Filipino Cultural Context' domain, specifically topics 1.C (financial behavior), 2.B (seasonal spending), and 2.D (spending cycles), as it provides detailed qualitative evidence on income volatility and financial management practices of Filipino freelancers. The 'Expense Categorization' domain (topics 3.A, 3.B) was considered relevant due to the discussion of budgeting and expense tracking, receiving a 'medium' relevance. The 'Existing Systems & Gaps' domain (topics 4.A, 4.B) was highly relevant because the paper explicitly highlights limitations in current financial services. The 'Behavioral Profiling' domain (topics 5.A, 5.B) received 'medium' and 'contextual' relevance, as the paper discusses varied financial behaviors and the difficulty of establishing financial history. The 'Anomaly Detection' domain (topic 8.A) was deemed 'contextual' due to the discussion of financial stress from income fluctuations. The 'Data Privacy & User Trust' domain (topics 10.A, 10.B) was given 'low' and 'contextual' relevance, as trust is implied in the need for reliable institutions. The 'Savings & Debt Management' domain (topics 13.A, 13.B) was relevant ('medium') due to the focus on emergency funds and credit barriers. Other domains like 'Spending Forecasting,' 'Budget Recommendation,' 'Mobile-First Design,' 'User Retention,' and 'System Evaluation' were considered but rejected as the paper does not address algorithmic or design-specific aspects; its contribution is purely descriptive and motivational. Overall, the paper provides strong contextual and motivational justification for Odin's focus on addressing income volatility and financial exclusion among Filipino freelancers.
limitations:
  - "Focuses on freelancers in Metro Manila only, limiting generalizability to other regions in the Philippines."
  - "Qualitative study design with a sample size of 50, which may not capture the full diversity of the freelance population."
  - "The study relies on self-reported data, which may be subject to recall bias or social desirability bias."
  - "[unacknowledged] The study does not quantify the prevalence of specific financial challenges among different freelancer subgroups."
  - "[unacknowledged] The study does not evaluate the effectiveness of the specific financial tools mentioned by participants."
remember_this:
  - "Income volatility is the primary financial challenge for freelancers."
  - "Freelancers often lack access to traditional benefits like health insurance."
  - "Barriers to credit and loans are common due to irregular income perception."
  - "Systemic reforms and tailored financial products are urgently needed."
  - "Financial stress significantly impacts freelancers' mental and social well-being."
```
---

## Paper 12: Patra et al_summarized.md

**Source File:** `Patra et al_summarized.md`

```yaml
paper_id: 10.71443/er.ar16
designation: international-algorithm-specific
title: AI-Driven Goal Based Financial Planning System: A Framework for Contextual Feasibility Validation
authors: Patra, B.; Sarkar, S.; Pal, S.; Ghosh, S.; Datta, S.
year: 2025
venue: Engineering Research
odin_topics:
  - 3.A
  - 5.A
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 7.C
  - 7.D
  - 8.A
  - 13.A
  - 13.B
  - 13.C
tldr: An AI framework integrates predictive modeling, reinforcement learning, and Monte Carlo simulation to validate the feasibility of achieving personal financial goals under uncertainty.
problem_and_motivation: Conventional financial planning relies on static assumptions and fails to adapt to dynamic economic conditions and individual behavioral factors. A gap exists in integrating real-time data, adaptive decision-making, and probabilistic feasibility validation into a single goal-oriented system.
approach:
  - Financial factors, including income, expenditure, savings, risk, and market dynamics, are modeled as a multi-dimensional vector for holistic analysis.
  - Time-series forecasting using LSTM networks predicts future income, expenses, and savings from historical data.
  - A reinforcement learning agent optimizes investment allocation strategies by interacting with financial simulations and receiving rewards for goal progress.
  - Monte Carlo simulations generate probabilistic distributions of future wealth by varying return rates and economic parameters.
  - The framework comprises data, AI, and decision layers, enabling modularity and real-time updates based on new data.
  - Feasibility of goals is computed as the proportion of simulated scenarios where final wealth exceeds a target.
findings:
  - The proposed AI system increases forecasting accuracy, adaptability, and goal feasibility evaluations compared to traditional rule-based approaches.
  - num: The integration of contextual awareness significantly enhances the system's performance in providing personalized financial plans.
  - Reinforcement learning enables dynamic strategy adaptation, improving decision-making in response to changing financial circumstances.
  - Incorporating behavioral factors (e.g., risk tolerance) and macroeconomic data leads to more realistic and relevant financial advice.
  - The framework provides quantitative feasibility scores and actionable recommendations, supporting informed financial decision-making.
key_figures_tables:
  - Figure 2: Monthly income-expense dynamics → Highlights cash flow variability, crucial for time-series modeling.
  - Figure 3: Monthly savings variability → Savings fluctuate significantly, including deficits, impacting goal feasibility.
  - Figure 6: Income distribution → Income is not stable, supporting the need for probabilistic forecasting.
  - Figure 7: Risk score distribution → Risk tolerance is dynamic, requiring adaptive behavioral profiling.
  - Table 1: Monthly income and expense data → Quantifies the variability used for LSTM forecasting and simulation.
key_equations:
  - equation: S_t = I_t - E_t - C_t
    explanation: Savings model adjusted for contextual factors like inflation.
  - equation: X_t = [I_t, E_t, S_t, R_t, B_t, M_t]
    explanation: Financial state as a vector for machine learning models.
  - equation: W_{t+1} = W_t + S_t + A_t * r_t
    explanation: Wealth evolution from savings and investment returns.
  - equation: P(G) = (1/N) * sum_{i=1}^N I(W_T^(i) >= G)
    explanation: Probability of achieving a financial goal via simulation.
definitions:
  - term: LSTM
    definition: Long Short-Term Memory network for time-series forecasting.
  - term: Reinforcement Learning
    definition: A method for adaptive decision-making through reward-based learning.
  - term: Monte Carlo Simulation
    definition: A technique to model uncertainty by generating multiple random scenarios.
  - term: Feasibility Score
    definition: A probabilistic measure of the likelihood of achieving a financial goal.
critical_citations:
  - "[Kahneman and Tversky, 1979] — Basis for behavioral biases in finance."
  - "[Hochreiter and Schmidhuber, 1997] — Introduced LSTM for temporal data."
  - "[Markowitz, 1952] — Foundation for Modern Portfolio Theory."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Provides empirical expense distribution data (Figure 8, Table 4) relevant for categorization.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly models risk tolerance and behavioral factors as input variables.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Proposes LSTM-based forecasting for income and expenses.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Uses LSTM specifically for time-series forecasting of financial data.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Offers a goal-based planning framework that informs budgeting decisions.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Generates recommendations on savings, investment, and goal timelines.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: medium
      justification: Uses reinforcement learning for optimization under user constraints.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: high
      justification: Core focus on feasibility validation and providing corrective recommendations.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Mentions risk assessment but not explicit anomaly detection algorithms.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: Explicitly models savings and evaluates goal achievement probabilities.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: low
      justification: Briefly mentions liabilities but focuses more on savings and investments.
    - code: 13.C
      name: End-of-Period Surplus as a Savings Input
      relevance: high
      justification: Uses surplus (savings) as the primary driver for wealth accumulation and feasibility.
  contribution: The paper directly justifies Odin's goal-based financial planning module by providing a framework for feasibility validation. Its approach to using LSTM for forecasting supports Odin's predictive analytics component. The reinforcement learning method for investment allocation can inform Odin's budget recommendation and optimization algorithms. The Monte Carlo simulation for scenario analysis provides a methodology for Odin's feasibility assessment and risk evaluation. The emphasis on integrating behavioral factors validates Odin's need for behavioral profiling within its system.
  directly_justifies:
    - Dynamic financial planning requires AI-driven models for forecasting and adaptation.
    - Feasibility validation should be probabilistic, using simulation to handle uncertainty.
    - Incorporating behavioral factors and risk tolerance is essential for personalization.
    - Reinforcement learning can optimize financial strategies by learning from dynamic environments.
    - A layered, modular architecture is suitable for building intelligent and scalable PFMS.
  limits:
    - The empirical evaluation is limited to a small, illustrative dataset rather than a large-scale real-world user base.
    - The paper does not provide a detailed comparative analysis against state-of-the-art baseline algorithms.
    - The framework's practical deployment aspects, such as latency and data privacy, are not addressed. [unacknowledged]
  mapping_rationale: A systematic scan of all 12 functional domains was conducted. Domains 6 (Spending Forecasting), 7 (Budget Recommendation), and 13 (Savings & Debt Management) were flagged with high relevance due to the paper's core contribution on feasibility validation and goal-based planning. Domain 5 (Behavioral Profiling) was assessed as medium relevance because risk tolerance is modeled as a key variable. Domain 3 (Expense Categorization) was marked medium due to the presentation of expense distribution data. Domain 8 (Anomaly Detection) was considered contextual as the paper discusses risk but not explicit anomaly detection. Domains 1 (Filipino Context), 2 (Cultural Practices), 4 (Existing Systems), 9 (Mobile-First), 10 (Data Privacy), 11 (Retention), and 12 (Evaluation) were rejected as they are not the subject of the paper. The overall relevance is high, providing a methodological foundation for Odin's algorithmic modules.
limitations:
  - The empirical validation uses a limited synthetic dataset, not real-world user data.
  - The paper does not discuss the computational cost or scalability of the integrated AI models.
  - Integration with existing mobile or web-based applications is not explored. [unacknowledged]
  - Data privacy and security concerns in a real fintech deployment are not addressed. [unacknowledged]
remember_this:
  - Integrating predictive, adaptive, and probabilistic models enhances financial planning realism.
  - Feasibility validation via Monte Carlo simulation provides quantitative goal success probabilities.
  - LSTM forecasting captures non-linear patterns in income and expense data.
  - Dynamic risk profiling is essential for tailoring investment strategies effectively.
  - num: The proposed system outperforms traditional rule-based approaches in accuracy and adaptability.
```
---

## Paper 13: Rosario_summarized.md

**Source File:** `Rosario_summarized.md`

```yaml
paper_id: 10.64753/jcasc.v10i3.2426
designation: local
title: Personal Financial Management Practices of Average earning households within Indigenous Communities of Mountain Province: Exploring Their Strategies and Challenges
authors: Rosario, E. P.
year: 2025
venue: Journal of Cultural Analysis and Social Change
odin_topics:
  - 2.A
  - 2.B
  - 2.D
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 13.A
  - 13.B
tldr: Indigenous households in Bontoc integrate modern budgeting with cultural practices like og-ogfo and paluwagan, prioritizing communal obligations and kinship over individual accumulation to manage financial stress.
problem_and_motivation: Standard financial management frameworks often overlook how cultural traditions and kinship obligations shape financial behavior in Indigenous communities. There is a gap in understanding how these cultural systems interact with modern economic pressures. This study addresses that gap by examining the financial strategies of Indigenous households in Mountain Province.
approach:
  - A qualitative descriptive phenomenological design was used to explore lived financial experiences.
  - Data were gathered through semi-structured interviews and a focus group discussion with 12 participants.
  - Participants were purposively sampled from average-earning Indigenous households in Bontoc, Mountain Province.
  - Thematic analysis following Colaizzi's method was applied to transcribed interviews.
  - The interpretation was guided by Cultural Capital Theory, Social Identity Theory, and Behavioral Economics.
findings:
  - num: Households prioritize food, electricity, and education even during hardship, often delaying bills to fulfill kinship duties.
  - num: Cultural practices like og-ogfo (mutual aid) and bayanihan serve as primary informal safety nets.
  - num: Savings are irregular and often take indigenous forms like paluwagan, livestock, or stored rice.
  - num: Cultural obligations such as supon and og-ogfo significantly influence spending, often overriding personal financial goals.
  - Households cope with financial stress through budgeting, income diversification, and strong reliance on family and community solidarity.
  - Formal financial institutions are secondary to informal systems due to access barriers and trust-based preferences.
  - Financial resilience in Bontoc is collective and relational, not purely individual.
key_figures_tables:
  - "Table 1: Profiles of 12 participants with occupations, monthly incomes (₱10,000-₱25,000), and household sizes (3-6) → Shows diverse income sources within a constrained range."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Og-ogfo
    definition: A traditional system of communal labor and collective aid in the Cordillera region.
  - term: Bayanihan
    definition: A Filipino cultural practice of communal unity and cooperation to achieve a common goal.
  - term: Paluwagan
    definition: A rotating savings and credit association where members contribute regularly and take turns receiving the lump sum.
  - term: Supon
    definition: A practice of giving monetary support during rituals and community gatherings as a symbolic investment in solidarity.
critical_citations:
  - "[Lusardi & Mitchell, 2014] — Foundational for linking budgeting to financial resilience."
  - "[Collins et al., 2009] — Core reference on financial tools used by low-income families."
  - "[Banerjee & Duflo, 2011] — Seminal work on poverty and financial management constraints."
relevance:
  topics:
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Core focus on indigenous practices like og-ogfo, supon, and paluwagan.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: high
      justification: Details event-driven budget strain from weddings, rituals, and community gatherings.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: high
      justification: Directly addresses how cultural obligations (occasions) drive spending priorities.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Highlights reliance on informal systems over formal PFMS or banks.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies access barriers to formal finance and gaps in culturally sensitive financial literacy.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: low
      justification: Provides context on collective vs. individual financial behavior profiles.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Describes behaviors but does not classify them into profiles.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: Discusses savings but as informal practices (e.g., livestock) rather than formal goal management.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: low
      justification: Mentions borrowing and debt risks but not as a structured management approach.
  contribution: The study provides a culturally grounded perspective on financial management, directly relevant to Odin's design for Filipino users. It informs the development of culturally sensitive expense categorization by highlighting how cultural obligations influence spending. The findings on collective coping mechanisms and informal safety nets can justify features for social support and community-based financial tools. The detailed practices of paluwagan and og-ogfo offer concrete examples for designing features that align with existing user behaviors. Finally, the study's emphasis on trust-based systems directly supports Odin's rationale for building user trust and engagement through culturally resonant design.
  directly_justifies:
    - "Odin should account for cultural obligations like supon and og-ogfo in its expense categorization and forecasting models."
    - "Integrating features that support communal saving practices (e.g., paluwagan) can improve user retention."
    - "Budgeting and savings features in Odin must be flexible to accommodate irregular income and event-driven spending."
  limits:
    - "Small sample size (n=12) limits generalizability beyond the specific Bontoc Indigenous community."
    - "The study is qualitative and descriptive, not testing or evaluating specific PFMS algorithms or features."
    - "Focus on cultural practices, but does not quantify their impact on financial outcomes compared to modern methods."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to the domain of Filipino Cultural Context, specifically topics 2.A (Culturally Specific Financial Practices), 2.B (Seasonal and Cyclical Spending Patterns), and 2.D (Filipino Spending Cycles and "Occasions") due to its deep investigation of practices like og-ogfo, supon, and event-driven financial strain. Medium relevance was assigned to topics under Existing Systems & Gaps (4.A, 4.B) because it details the landscape of and gaps in formal systems for this demographic. Low relevance was assigned to Behavioral Profiling & Classification (5.A, 5.C) as the paper describes behaviors but does not profile them, and to Savings & Debt Management (13.A, 13.B) because it discusses these topics in an informal, non-structured manner. Topics related to algorithmic forecasting, budget recommendation, anomaly detection, mobile design, data privacy, engagement, and system evaluation were considered and rejected because the paper is a qualitative sociological study, not a computational or design-oriented paper. The overall relevance is contextual for these modules, informing the cultural backdrop but not providing algorithmic or user interface design insights. The paper is moderately relevant to Odin, primarily serving to ground the system in the cultural realities of its target Filipino users.
limitations:
  - "The study is confined to a single Indigenous community, limiting broader applicability. [unacknowledged]"
  - "Relies on self-reported data, which may introduce social desirability bias."
  - "Does not quantify the economic contribution of cultural practices, making it difficult to model. [unacknowledged]"
  - "Lacks a comparative analysis with non-Indigenous households in the same geographic area."
remember_this:
  - "Cultural practices like og-ogfo and paluwagan are primary financial safety nets."
  - "Households prioritize communal obligations even when funds are insufficient."
  - "Budgeting is a social act of preparation for cultural duties, not just personal planning."
  - "Financial resilience is collective and relational, not purely individual."
  - "Cash alternatives (labor, food) are key to maintaining social membership.
```
---

## Paper 14: Bhavana et al_summarized.md

**Source File:** `Bhavana et al_summarized.md`

```yaml
paper_id: 10.15662/IJARCST.2025.0805004
designation: international-algorithm-specific
title: AI-Based Wealth Advisory System using Machine Learning and Predictive Analytics for Personalized Budget Planning
authors: Bhavana, B. R.; Pavan, D.; Darshan, T. H. G.
year: 2025
venue: International Journal of Advanced Research in Computer Science & Technology (IJARCST)
odin_topics:
  - 3.A
  - 3.B
  - 5.C
  - 6.A
  - 6.B
  - 7.B
  - 8.A
  - 8.B
  - 10.A
  - 10.B
tldr: Integrates classification, forecasting, anomaly detection, and XAI into a single advisory system for personalized budget planning and financial goal setting.
problem_and_motivation: Existing personal finance applications are primarily reactive and rule-based, lacking predictive and adaptive capabilities to proactively manage wealth. A gap exists for consumer-centric AI systems that combine forecasting, anomaly detection, and explainability to bridge advanced analytics with practical usability.
approach:
  - Uses a multi-model architecture integrating XGBoost, BERT, and Random Forests for expense classification.
  - Employs ARIMA, Prophet, LSTM, and Transformers in an ensemble for expenditure forecasting.
  - Detects anomalies using Isolation Forests, Autoencoders, and GAN-based detectors.
  - Generates recommendations via Contextual Bandits and Reinforcement Learning.
  - Integrates SHAP and LIME for explainability and NLG for user-friendly output.
  - Implements AES-256, TLS 1.3, differential privacy, and federated learning for security.
findings:
  - num: Achieved 95% anomaly detection accuracy in a pilot study with 100 users.
  - num: Demonstrated a 22% improvement in savings among pilot participants.
  - num: Enhanced financial literacy for 78% of participants in the pilot study.
  - num: Reported expense classification F1-score of 91% and forecasting MAE of $43/month.
  - num: Recommendation adoption rate of 41% was observed during pilot testing.
key_figures_tables:
  - "Table II: Literature review summary → Organizes key prior work on AI in finance by technique and result."
  - "Figure 2: System architecture diagram → Shows integration of data sources, models, and XAI components."
  - "Figure 3: Pilot study results dashboard → Visualizes 95% anomaly detection accuracy and 22% savings improvement."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: XAI
    definition: Explainable AI, methods that make model predictions interpretable.
  - term: NLG
    definition: Natural Language Generation, converting data into human-readable text.
  - term: SHAP
    definition: SHapley Additive exPlanations, a method for explaining feature importance.
  - term: LIME
    definition: Local Interpretable Model-agnostic Explanations, a model-agnostic explanation method.
  - term: GAN
    definition: Generative Adversarial Network, used here for anomaly detection.
critical_citations:
  - "[Lundberg & Lee, 2017] — Provides SHAP framework for model explainability."
  - "[Ribeiro et al., 2016] — Provides LIME framework for model-agnostic interpretability."
  - "[Abadi et al., 2016] — Provides differential privacy mechanism for data protection."
  - "[Barocas et al., 2019] — Addresses fairness-aware ML methods for mitigating bias."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Paper explicitly uses classification models (XGBoost, BERT) for categorizing expenses.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: Discusses categorization via merchant codes and NLP but does not focus on category design itself.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses classification for expense patterns, which directly supports profile classification.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Core contribution is predictive modeling using ARIMA, Prophet, LSTM, and Transformers.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Directly evaluates and proposes forecasting algorithms for sequential financial data.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: System's primary purpose is personalized budget planning and recommendation.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Dedicated anomaly detection module with high reported accuracy.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Implements Isolation Forests, Autoencoders, and GANs for spending data.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Explicitly addresses privacy with encryption, differential privacy, and federated learning.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Directly addresses trust through XAI integration and transparency reports.
  contribution: "This paper validates an integrated AI architecture for personal finance that combines classification, forecasting, anomaly detection, and XAI, directly informing Odin's algorithmic module design. The reported metrics (e.g., 95% anomaly detection accuracy, 22% savings improvement) provide quantitative benchmarks for evaluating similar components in Odin. The emphasis on explainability and privacy offers a template for building user trust, critical for Odin's adoption. The proposed system addresses key Odin functions including budget recommendation, spending forecasting, and anomaly flagging. The pilot study methodology offers a framework for evaluating Odin's effectiveness before full deployment."
  directly_justifies:
    - "Combining forecasting and anomaly detection in one system improves user savings by 22%."
    - "XAI methods like SHAP and LIME are essential for building trust in financial advisory systems."
    - "Ensemble forecasting reduces prediction error compared to single-model approaches."
    - "Anomaly detection using Isolation Forests and Autoencoders achieves high accuracy on transaction data."
    - "Federated learning and differential privacy are viable approaches for data privacy in PFMS."
  limits:
    - "Pilot study used only 100 participants, which may not generalize to all user demographics."
    - "Privacy-preserving methods (differential privacy) were described but not empirically evaluated for their impact on model accuracy. [unacknowledged]"
    - "Paper provides limited details on the specific dataset used for evaluation, hindering reproducibility."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper's strongest relevance is to Expense Categorization (3.A), Predictive Modeling (6.A/6.B), Budget Recommendation (7.B), Anomaly Detection (8.A/8.B), and Data Privacy & User Trust (10.A/10.B), all rated 'high' due to the paper's direct focus on implementing and evaluating these modules. Medium relevance was assigned to 3.B (category design) and 5.C (profile classification) as the paper uses categorization and classification but does not deeply explore the design rationale or profile dynamics. Domains like Behavioral Profiling (5.A/5.B), Spending Cycles (2.B), Mobile-First Design (9.A/9.B), and System Evaluation (12.A/12.B/12.C) were considered but rejected as the paper does not provide substantial insights into these specific Odin concerns. The paper's comprehensive AI architecture makes it broadly relevant, particularly for Odin's algorithmic justification and user trust strategies."
limitations:
  - "Pilot study with only 100 users limits generalizability of reported metrics."
  - "Privacy-preserving techniques' impact on predictive accuracy was not empirically assessed. [unacknowledged]"
  - "Paper lacks a detailed description of the specific dataset used for training and evaluation."
  - "No comparison against a fully non-AI baseline to isolate the effect of AI components on user outcomes."
remember_this:
  - "Anomaly detection accuracy of 95% was achieved using a multi-model approach."
  - "A 22% savings improvement was observed in a pilot study with the integrated system."
  - "SHAP and LIME are integrated to provide explainable financial recommendations."
  - "Federated learning and differential privacy are proposed to protect user financial data."
  - "The system combines forecasting, classification, and anomaly detection in one architecture."
```
---

## Paper 15: Cabrera et al_summarized.md

**Source File:** `Cabrera et al_summarized.md`

```yaml
paper_id: 10.1057/s41599-025-05205-z
designation: local-algorithm-specific
title: Plastic to apparel: an analysis of sustainable purchasing intention using a machine learning ensemble
authors: Cabrera, C. A. L.; Ong, A. K. S.; Diaz, J. F. T.; Cahigas, M. M. L.; Gumasing, M. J. J.
year: 2025
venue: Humanities and Social Sciences Communications
odin_topics:
  - 1.A
  - 1.C
  - 2.A
  - 2.D
  - 5.A
  - 5.B
  - 5.C
tldr: Customer perceived value and perceived behavioral control are the primary factors influencing Filipino consumers' purchase intentions for apparel made from recycled plastic.
problem_and_motivation: Despite the environmental benefits of recycled apparel, a significant gap exists in understanding the key drivers of sustainable purchasing behavior. This is particularly relevant in the Philippines, a major contributor to ocean plastic pollution, yet behavioral intentions remain underexplored. The study addresses this gap by establishing the Sustainability Theory of Planned Behavior (STPB) model.
approach:
  - A survey of 500 Filipino respondents was conducted to evaluate eight factors from the STPB model on purchase intention for recycled plastic apparel.
  - The study employed a machine learning ensemble comprising Random Forest Classifier (RFC) and Artificial Neural Network (ANN) for analysis.
  - Data preprocessing involved feature selection and correlation analysis to validate and aggregate the data.
  - RFC was optimized with parameters including tree depth, criterion (gini/entropy), and splitter choice across multiple iterations.
  - ANN optimization was performed with varying activation functions (tanh, relu, elu), optimizers, and hidden layer nodes over 150 epochs.
findings:
  - num: RFC achieved a 92% accuracy rate with the optimum parameters of gini and best at a 90:10 training-testing ratio.
  - num: ANN achieved a 91% R-squared test value with the Elu activation function at 30 hidden layer nodes.
  - Customer Perceived Value (CPV) is the most important factor, with a 100% normalized importance score.
  - Perceived Behavioral Control (PBC), Attitude (AT), and Subjective Norm (SN) closely follow CPV with 94.7%, 87.4%, and 82.6% importance, respectively.
  - Perceived Authority Support (PAS) had the lowest importance among factors at 71.5%.
key_figures_tables:
  - Figure 3: Theoretical framework of the STPB model with eight factors → Framework for the study's hypothesis build-up.
  - Table 2: Demographic profile of the 500 respondents (e.g., age, gender, income) → Provides context for the sample population.
  - Table 3: Random Forest Classifier results showing accuracy rates for different parameters and splits → Demonstrates the best model configuration (92% at 90:10 split with gini).
  - Figure 4: Optimum classification model with RFC → Shows the decision tree for predicting purchase intention.
  - Figure 5: Optimum ANN classification model → Visualizes the neural network architecture with 30 nodes.
key_equations:
  - equation: f(x) = x if x > 0 else α(e^x - 1)
    explanation: The Elu activation function used for the ANN hidden layer.
definitions:
  - term: STPB
    definition: Sustainability Theory of Planned Behavior, an extension of TPB integrating all sustainability domains.
  - term: RFC
    definition: Random Forest Classifier, an ensemble machine learning algorithm for classification.
  - term: ANN
    definition: Artificial Neural Network, a machine learning algorithm with connected nodes for classification.
  - term: CPV
    definition: Customer Perceived Value, a customer's holistic evaluation of a product's utility.
  - term: PBC
    definition: Perceived Behavioral Control, the perception of how easy or challenging it is to perform an activity.
  - term: PECC
    definition: Perceived Economic Concern, a customer's inclination to allocate additional funds towards sustainable products.
  - term: PENC
    definition: Perceived Environmental Concern, a measurement of how a person perceives effects on the environment.
  - term: PAS
    definition: Perceived Authority Support, an individual's comprehension of support from authoritative entities.
critical_citations:
  - "[German et al., 2022] — Established the PEPB model used as the base for STPB."
  - "[Ajzen, 1991] — The foundational TPB theory is cited for the behavioral framework."
  - "[Ong et al., 2023] — Justified the inclusion of PECC as a necessary variable."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: The study's sample is Filipino, but not specifically focused on young professionals.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: low
      justification: While it assesses purchasing behavior, it does not specifically analyze the financial management behavior of Filipino young professionals.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: The paper touches on Filipino environmental context, but not on specific cultural financial practices like 'utang'.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: The study mentions purchase frequency intervals but does not link them to Filipino-specific spending cycles or occasions like 'fiestas' or '13th-month pay'.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: low
      justification: The study classifies behavioral intentions using machine learning but does not create distinct, actionable financial profiles for personal finance management.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: The study's machine learning model classifies behavior but does not address how to handle a new user with no history (cold-start).
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: The study uses RFC and ANN for classification, which is a relevant methodology but applied to sustainable purchasing, not directly to financial behavior profiling.
  contribution: The study contributes a validated STPB framework and a machine learning ensemble model (RFC and ANN) that can be adapted by Odin to analyze user financial behavior. The identification of CPV and PBC as the most significant drivers of intention provides a direct justification for Odin's expense categorization and user engagement modules to emphasize perceived value and user control over finances. The high accuracy of the RFC model at 92% supports the use of similar classification algorithms for Odin's behavioral profiling and anomaly detection modules.
  directly_justifies:
    - Customer Perceived Value (CPV) is the most significant driver of behavioral intention.
    - Perceived Behavioral Control is the second most significant factor influencing intention.
    - Machine learning ensembles like RFC and ANN provide high accuracy (92% and 91%) for analyzing complex behavioral relationships.
    - Authority support (PAS) is the least influential factor, suggesting a focus on peer influence and personal value over institutional endorsement.
  limits:
    - The study's sample is skewed towards younger demographics (55.4% aged 18-25) and urban residents (80.6%).
    - The model does not differentiate between online and in-person purchase intentions.
    - Demographic data was not directly correlated with specific behavioral outcomes.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was conducted. The paper was flagged as most relevant to the 'Behavioral Profiling & Classification' domain, as it employs classification algorithms (RFC, ANN) to analyze behavioral factors. Topics 5.A, 5.B, and 5.C were selected with 'medium' relevance because the paper classifies purchase intention, which is a form of behavioral profiling, though not specifically for financial management within a PFMS. The 'Filipino Cultural Context' domain was considered, with topic 2.A and 2.D receiving 'low' or 'contextual' relevance because the study uses Filipino respondents but doesn't explicitly analyze culturally specific spending practices like 'utang' or 'fiesta' cycles. Domains like 'Expense Categorization', 'Spending Forecasting', 'Budget Recommendation', 'Anomaly Detection', and 'Mobile-First Design' were rejected as the paper does not address these specific technical or design aspects of a PFMS. The overall relevance to Odin is moderate, providing methodological justification for using machine learning in behavioral analysis rather than direct technical implementation for its core functions.
limitations:
  - "The sample is heavily skewed towards younger demographics (18-25 years old) and urban areas. [unacknowledged]"
  - "The study does not differentiate between online and in-person purchase intentions for sustainable apparel. [unacknowledged]"
  - "The research did not correlate demographic data with specific behavioral outcomes to provide a comprehensive overview. [unacknowledged]"
  - "The model's findings are based on stated intentions, which may not perfectly reflect actual purchasing behavior."
remember_this:
  - Customer Perceived Value is the most critical factor for sustainable purchase intention.
  - Perceived Behavioral Control and Attitude are the second and third most important factors.
  - RFC achieved a 92% accuracy rate in predicting behavioral intention.
  - Authority support was the least influential factor on sustainable apparel purchase decisions.
  - The STPB framework can holistically assess sustainable consumption behavior.
```
---

## Paper 16: Chen X. et al_summarized.md

**Source File:** `Chen X. et al_summarized.md`

```yaml
paper_id: "3f5a6c7d-8e9f-4a1b-9c2d-3e4f5a6b7c8d"
designation: "international-algorithm-specific"
title: "Rethinking Time Encoding via Learnable Transformation Functions"
authors: "Chen, X.; Tang, Y.; Xu, J.; Zhang, J.; Zhang, S.; Peng, S.; Zheng, X.; Xiong, Y."
year: 2025
venue: "Proceedings of the 42nd International Conference on Machine Learning"
odin_topics:
  - "4.B"
  - "6.A"
  - "6.B"
  - "8.A"
  - "8.B"
  - "12.B"
tldr: "Introduces Learnable Transformation-based Generalized Time Encoding (LeTE) that parameterizes non-linear transformations to capture diverse time patterns, outperforming fixed encodings."
problem_and_motivation: "Existing time encoding methods rely on fixed inductive biases like trigonometric functions, limiting their ability to model complex mixed time patterns in real-world data. This gap hinders accurate predictions in tasks like forecasting and anomaly detection. A more flexible encoding is needed."
approach:
  - "Proposes LeTE with learnable non-linear transformations via Fourier series or B-splines."
  - "Implements Fourier-based, Spline-based, and combined variants with layer normalization."
  - "Parameterizes transformations jointly optimized with downstream tasks."
  - "Evaluates on image classification, time series forecasting, dynamic graph link prediction, and financial fraud detection."
findings:
  - "num: LeTE achieves average win rates of 98% on MAE and 95% on MSE across baselines and datasets."
  - "LeTE outperforms FTE with lower dimensions, e.g., 16-D LeTE matches 100-D FTE."
  - "LeTE effectively captures periodic, non-periodic, and mixed patterns."
  - "LeTE is invariant to time rescaling and interpretable via learned function reconstruction."
key_figures_tables:
  - "Table 1: MAE comparison on multivariate forecasting → LeTE beats HCTE and FTE in most cases."
  - "Table 2: AP on dynamic graph link prediction → LeTE consistently improves over FTE."
  - "Figure 4: AUC-ROC on financial risk control → LeTE outperforms without time and FTE."
  - "Figure 5: Dimension efficiency on dynamic graphs → LeTE maintains performance at low dimensions."
key_equations:
  - equation: "TE(t)[i] = phi_i(omega_i t + phi_i)"
    explanation: "Defines LeTE as learnable transformation of scaled time."
  - equation: "phi_i(x) = a_0 + sum_{k=1}^K (a_k cos(kx) + b_k sin(kx))"
    explanation: "Fourier series parameterization for periodic patterns."
  - equation: "phi_i(x) = sum_{j=1}^M c_{ij} B_j(x)"
    explanation: "B-spline parameterization for non-periodic patterns."
  - equation: "LeTE(t)[i] = s_i * LayerNorm(phi_i(omega_i t + phi_i))"
    explanation: "Combined LeTE with scaling and normalization."
definitions:
  - term: "LeTE"
    definition: "Learnable Transformation-based Generalized Time Encoding, a time encoding method with learnable non-linear transformations."
  - term: "FTE"
    definition: "Functional Time Encoding, includes FTR and Time2Vec with fixed sine transformations."
  - term: "HCTE"
    definition: "Hand-Crafted Time Encoding, manually designed temporal features."
  - term: "B-spline"
    definition: "Basis spline functions used for piecewise polynomial approximation."
critical_citations:
  - "[Kazemi et al., 2019] — Proposed Time2Vec with fixed sine activations."
  - "[Xu et al., 2019] — Proposed Functional Time Representation."
  - "[Wu et al., 2023] — TimesNet model for time series forecasting."
  - "[Yu et al., 2023] — DyGFormer for dynamic graph representation."
relevance:
  topics:
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Paper explicitly critiques fixed time encodings and identifies their limitations."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Provides a component that can enhance predictive modeling but not a full model."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Proposes a new time encoding algorithm for forecasting with strong empirical gains."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Applied to fraud detection, but the method is a general encoding not specific to anomaly framework."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Improves detection performance in financial risk control by modeling complex patterns."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Provides extensive evaluation of the time encoding module across multiple tasks."
  contribution: "LeTE can be integrated into Odin's spending forecasting module to improve prediction accuracy by capturing complex temporal patterns. It can enhance anomaly detection in transaction data by learning non-periodic and mixed patterns. Its dimension efficiency allows deployment in mobile-first settings with limited resources. The method's interpretability aids user trust by revealing learned time functions. Its plug-and-play nature simplifies integration into existing Odin modules."
  directly_justifies:
    - "LeTE outperforms fixed time encodings in forecasting accuracy."
    - "LeTE captures non-periodic patterns crucial for fraud detection."
    - "Lower-dimensional LeTE maintains performance, suitable for mobile devices."
    - "LeTE's invariance to time rescaling ensures robust handling of different time granularities."
  limits:
    - "Performance may depend on hyperparameter p and dimension choice."
    - "Extension to position encoding not formally proven."
    - "Evaluation limited to a few tasks; broader generalizability not fully tested."
  mapping_rationale: "Systematic scan across 12 functional domains identified relevance primarily in Spending Forecasting, Anomaly Detection, and System Evaluation. The paper directly addresses Limitations and Gaps (4.B) by critiquing fixed encodings. For Forecasting, it provides a new algorithm (6.B) and supports predictive modeling (6.A) via improved time representation. For Anomaly Detection, its fraud application justifies 8.A and 8.B. The extensive experiments on algorithmic modules fit 12.B. Borderline: the paper touches on Budget Recommendation (7.B) only indirectly through forecasting, but no explicit budget allocation, so rejected. Also Behavioral Profiling (5 series) not addressed. Mobile-First (9) and Data Privacy (10) not relevant. Overall, the paper's contribution is algorithmic and broadly applicable."
limitations:
  - "Performance may depend on hyperparameter p and dimension choice."
  - "Extension to position encoding not formally proven."
  - "Evaluation limited to a few tasks; broader generalizability not fully tested."
remember_this:
  - "LeTE achieves 98% win rate on MAE over baselines."
  - "LeTE captures mixed periodic and non-periodic patterns."
  - "LeTE is invariant to time rescaling."
  - "Lower-dimensional LeTE matches higher-dimensional FTE."
  - "LeTE is interpretable via function reconstruction."
```
---

## Paper 17: Yuttama_summarized.md

**Source File:** `Yuttama_summarized.md`

```yaml
paper_id: 10.34001/jmer.2025.12.06.4-80
designation: international
title: Behavioral Shifts in Digital Finance: How E-Payment Influences Consumer Spending and Financial Literacy
authors: Yuttama, F.
year: 2025
venue: Journal of Management and Entrepreneurship Research
odin_topics:
  - 1.C
  - 2.A
  - 2.B
  - 5.B
  - 5.C
  - 6.B
  - 7.A
  - 7.B
  - 10.B
  - 11.A
tldr: E-payment adoption in Indonesia exerts a dual effect on financial behavior, increasing spending propensity while enhancing cash management, with financial literacy moderating these effects.
problem_and_motivation: The influence of e-payment on consumer spending and financial discipline is inconclusive, with studies suggesting both impulsive spending and improved financial tracking. Existing research often treats e-payment as a direct driver without examining conditional factors like financial literacy. This gap is critical in emerging markets where digital payment adoption is rapidly transforming financial behavior.
approach:
  - A quantitative survey was administered to 400 active e-payment users in Central Java, Indonesia.
  - Constructs for e-payment usage, consumer behavior, cash management, and financial literacy were measured using validated Likert-scale items.
  - The hypothesized relationships were analyzed using Partial Least Squares Structural Equation Modeling (PLS-SEM) with SmartPLS 4.
  - Moderation analysis via PLS-SEM assessed the interactive effect of financial literacy on the relationships between e-payment usage and both consumer behavior and cash management.
  - Bootstrapping with 5,000 resamples was used to determine the statistical significance of path coefficients and moderation effects.
findings:
  - num: E-payment usage has a significant positive effect on consumer behavior (β = 0.731, p < 0.000).
  - num: E-payment usage has a significant positive effect on cash management (β = 0.493, p < 0.000).
  - num: Financial literacy significantly attenuates the positive relationship between e-payment and consumer behavior (β = -0.082, p < 0.000).
  - num: Financial literacy significantly strengthens the positive relationship between e-payment and cash management (β = -0.065, p = 0.005).
  - E-payment facilitates impulsive spending by lowering the psychological friction of payment.
  - Built-in transaction records and dashboards in e-payment systems improve expense tracking and budgeting.
  - The impact of e-payment is contingent on users' financial knowledge and self-regulation.
key_figures_tables:
  - Figure 1: E-payment transaction value growth in Central Java → shows rapid adoption of digital payments like QRIS and e-wallets.
  - Figure 2: PLS-SEM structural model results → illustrates significant paths and moderation effects of financial literacy.
  - Table 2: Demographic profile of respondents → shows majority are female, aged 25-34, with a bachelor's degree.
  - Table 4: Reliability and validity of measurement model → confirms all constructs meet thresholds for Cronbach's alpha and AVE.
  - Table 6: Structural model path coefficients → details the t-statistics and p-values for all hypothesized relationships.
key_equations:
  - equation: \eta = \frac{N}{1 + N e^2}
    explanation: Slovin's formula for determining sample size.
definitions:
  - term: PLS-SEM
    definition: Partial Least Squares Structural Equation Modeling, a variance-based method for analyzing complex cause-effect relationships.
  - term: AVE
    definition: Average Variance Extracted, a measure of convergent validity.
  - term: HTMT
    definition: Heterotrait-Monotrait ratio, a criterion for assessing discriminant validity.
critical_citations:
  - "[Hampson et al., 2021] — e-payment lowers psychological barriers, boosting impulse spending."
  - "[Liu & Zhang, 2021] — e-payment tools enhance financial tracking and management."
  - "[Lusardi & Mitchell, 2014] — financial literacy improves self-control and planning."
  - "[Thaler & Sunstein, 2008] — concept of 'pain of paying' in digital transactions."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Paper examines financial behavior in an emerging market context, providing comparative insights.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: low
      justification: Focuses on Indonesian context, offering limited but relevant cultural parallels for SE Asia.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: low
      justification: Touch on spending cycles but not a core focus of the study.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: Financial literacy is treated as a key moderating variable that differentiates user behavior.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Demonstrates how financial literacy can be used to classify and predict user responses to e-payment systems.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: Provides behavioral data (spending patterns) that could inform forecasting models, but no algorithms are proposed.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Paper directly investigates how e-payment tools and financial literacy facilitate budgeting and cash management.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: Findings directly support the need for in-app budgeting and monitoring features in PFMS like Odin.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Implications discuss building trust through features that promote financial discipline and user well-being.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Suggests features like spending alerts and goal tracking to maintain user engagement and financial discipline.
  contribution: This paper validates the dual nature of e-payment adoption, which Odin can leverage to design behavioral nudges and budgeting features. It emphasizes the crucial moderating role of financial literacy, informing Odin's user profiling and personalization engine. The study's empirical evidence from an emerging market supports Odin's mobile-first design for Filipino users, showing that app features can both encourage spending and aid cash management. The findings justify integrating financial literacy assessments to tailor budget recommendations and anomaly detection for users.
  directly_justifies:
    - "E-payment usage significantly increases consumer spending propensity."
    - "E-payment tools enhance users' ability to monitor and plan finances."
    - "Higher financial literacy attenuates the positive effect of e-payment on spending."
    - "Financially literate individuals use e-payment features more effectively for financial discipline."
  limits:
    - "Findings are based on a survey in Central Java, Indonesia, which may not be generalizable to other developing countries like the Philippines."
    - "Reliance on self-reported data may introduce social desirability bias."
    - "Study focuses on financial literacy as a moderator, excluding other contextual variables."
  mapping_rationale: A systematic scan across all 12 functional domains was performed for this paper. The domain of 'Budget Recommendation' (7) was flagged as high relevance because the paper directly examines how e-payment tools and financial literacy enable effective budgeting and cash management. 'Behavioral Profiling' (5) was assigned medium relevance, as financial literacy is shown to differentiate user behavior, which is crucial for the cold-start problem. 'Spending Forecasting' (6) and 'User Retention' (11) received low to medium relevance, as the behavioral patterns and feature suggestions (e.g., goal tracking, alerts) provide supporting evidence. Other domains like 'Expense Categorization' (3), 'Anomaly Detection' (8), and 'Data Privacy' (10) were considered but rejected as the paper does not directly address these technical aspects. The paper's overall relevance to Odin is moderate, providing valuable behavioral and cognitive evidence to inform budgeting, user profiling, and engagement strategies for the Filipino context.
limitations:
  - "Geographic focus on Central Java limits generalizability to the Philippines."
  - "Self-reported data may introduce social desirability bias."
  - "Excludes other behavioral and contextual variables like digital literacy or income."
  - "Cross-sectional design captures behavior at a single point in time. [unacknowledged]"
  - "Does not differentiate between types of e-payment (e.g., bank transfer vs. e-wallet) in the analysis. [unacknowledged]"
remember_this:
  - "E-payment adoption both increases spending and improves financial tracking."
  - "Financial literacy is a critical buffer against impulsive digital spending."
  - "Higher literacy strengthens the positive link between e-payment and cash management."
  - "In-app features like budgets and alerts can promote financial discipline."
  - "Moderation effect of literacy on spending is significant (β = -0.082, p < 0.000)."
```
---

## Paper 18: Hall_summarized.md

**Source File:** `Hall_summarized.md`

```yaml
paper_id: 9e8b75fe-0c8d-5cbb-96e4-1fb0e70723ec
designation: international-algorithm-specific
title: "Machine Learning Time Series Forecasting: A Comprehensive Survey and Stock Market Application"
authors: "Hall, T."
year: 2025
venue: "University of Georgia"
odin_topics:
  - "6.A"
  - "6.B"
  - "12.A"
  - "12.B"
  - "12.C"
  - "1.C"
  - "2.B"
tldr: "A survey and empirical application show tree-based and deep learning models, particularly LightGBM and recurrent networks, excel in time series forecasting, with a day-trading model achieving returns far exceeding human traders."
problem_and_motivation: "Accurate time series forecasting is critical for finance, but existing surveys cannot compare models fairly due to heterogeneous experimental setups. Day trading is especially challenging because of market complexity, yet ML offers potential to outperform human traders by processing vast data and identifying subtle patterns."
approach:
  - "Conducted a systematic literature review of 79 papers comparing tree-based and deep learning models under identical conditions using Web of Science."
  - "Implemented a day-trading framework using LightGBM with extensive engineered features from two years of second-by-second trade and quote data."
  - "Trained models to estimate risk-reward ratios over multiple forward time horizons."
  - "Simulated trading with realistic execution constraints using bid and ask prices."
  - "Evaluated performance using cumulative profit, Sharpe ratio, and daily returns."
findings:
  - "Tree-based methods like LightGBM and deep learning methods like RNNs deliver the best performance in time series forecasting."
  - "num: The day-trading model achieved an average profit of 20,000 basis points per day."
  - "num: The model's Sharpe ratio was 15.78 across an average of 999 trades per day."
  - "num: ML model returns were more than 500 times higher than top human day traders."
  - "Quality of data and feature engineering overshadow incremental benefits of hyperparameter tuning."
key_figures_tables:
  - "Figure 2.1: RF and GBDT architecture comparison → Shows structural differences between ensemble methods."
  - "Figure 2.3: Overall model performance FPA and WRA scores → Tree-based and RNN models score highest."
  - "Figure 3.2: Model 1 cumulative profit → Demonstrates consistent profitability over time."
  - "Table 3.1: Model 1 performance metrics → Reports Sharpe ratio and daily return statistics."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "TBML"
    definition: "Tree-Based Machine Learning, ensemble methods using decision trees."
  - term: "DL"
    definition: "Deep Learning, neural network architectures with multiple layers."
  - term: "LightGBM"
    definition: "A gradient boosting framework that uses tree-based learning algorithms."
  - term: "RNN"
    definition: "Recurrent Neural Network, a class of neural networks for sequential data."
critical_citations:
  - "[Chen & Guestrin, 2016] — Introduced XGBoost, a foundational tree-based method."
  - "[Ke et al., 2017] — Developed LightGBM, a high-performance tree-based implementation."
  - "[Prokhorenkova et al., 2018] — Created CatBoost, optimized for categorical features."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Directly surveys and applies predictive models for financial time series."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Evaluates forecasting algorithms applicable to sequential spending data."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides a methodology for comparative evaluation of forecasting models."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Benchmarks individual algorithmic modules against each other."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "low"
      justification: "Evaluation approach is general and not specific to budget recommendations."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "contextual"
      justification: "Financial behavior is the broader domain, but the study is not specific to Filipinos."
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "contextual"
      justification: "Addresses cyclical patterns in financial data generally, but not specifically seasonal spending."
  contribution: "This paper provides a comprehensive survey that can guide the selection of forecasting algorithms for Odin's predictive modules. The empirical application demonstrates a robust framework for feature engineering and model training on high-frequency financial data, which is relevant for Odin's spending forecasting. The results show that tree-based models like LightGBM are computationally efficient and highly accurate, making them suitable for Odin's mobile-first architecture. The study also highlights the critical importance of data quality and feature engineering, which should inform Odin's data preprocessing and feature design."
  directly_justifies:
    - "LightGBM and RNNs deliver the best performance in time series forecasting."
    - "Tree-based models offer a significant advantage in computational efficiency."
    - "Quality of data and feature engineering are more influential than hyperparameter tuning."
    - "Combining models and diverse information sources boosts forecasting performance."
    - "ML models can process vast data to identify patterns invisible to human traders."
  limits:
    - "The day-trading application focuses on U.S. equities, which may not generalize to Filipino financial contexts."
    - "The survey relies on citation counts, which may introduce a bias toward older, more cited papers."
    - "The study does not address specific constraints of personal finance systems like budgeting or anomaly detection."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to predictive modeling (6.A) and forecasting algorithms (6.B) because it is a comprehensive survey and application of these exact techniques. It has medium relevance to evaluation frameworks (12.A, 12.B) because it provides a comparative methodology, and low relevance to evaluation of budget recommendation systems (12.C) as the evaluation is not specific to that sub-domain. The paper has contextual relevance to Filipino financial behavior (1.C) and seasonal spending (2.B) because it discusses financial behavior and cyclical patterns but is not specific to the Filipino context. Domains like expense categorization, behavioral profiling, anomaly detection, mobile design, data privacy, user retention, and savings/debt management were rejected because the paper does not address these areas. Overall, the paper is highly relevant for informing Odin's algorithmic design and evaluation."
limitations:
  - "The empirical application is specific to stock market day trading, which differs from personal finance spending forecasting. [unacknowledged]"
  - "The survey focuses on research comparing tree-based and deep learning methods, potentially omitting other effective techniques. [unacknowledged]"
remember_this:
  - "LightGBM and RNNs are top performers for time series forecasting."
  - "Feature engineering and data quality outweigh hyperparameter tuning benefits."
  - "The day-trading model achieved 20,000 bps average daily profit."
  - "ML model outperformed human traders by over 500 times."
```
---

## Paper 19: Fariha et al_summarized.md

**Source File:** `Fariha et al_summarized.md`

```yaml
paper_id: "10.14419/c73kcb17"
designation: "international-algorithm-specific"
title: "Advanced fraud detection using machine learning models: enhancing financial transaction security"
authors: "Fariha, N.; Khan, M.N.M.; Hossain, M.I.; Reza, S.A.; Bortty, J.C.; Sultana, K.S.; Jawad, M.S.I.; Safat, S.; Ahad, M.A.; Begum, M."
year: 2025
venue: "International Journal of Accounting and Economics Studies"
odin_topics:
  - "4.A"
  - "4.B"
  - "5.A"
  - "5.B"
  - "5.C"
  - "8.A"
  - "8.B"
  - "8.C"
  - "10.A"
  - "10.B"
  - "12.A"
  - "12.B"
tldr: "An unsupervised machine learning framework combining Isolation Forest, One-Class SVM, autoencoders, and clustering detects credit card transaction anomalies and assigns composite risk scores with 95% detection rate and 5% false-positive rate."
problem_and_motivation: "Traditional rule-based fraud detection systems suffer from high false-positive rates and inadequate adaptability to evolving fraud patterns. Unsupervised anomaly detection can identify deviations without labeled data but requires robust feature engineering and model integration. There is a gap in unified frameworks that combine multiple detectors and provide actionable risk scoring for real-time prioritization."
approach:
  - "Merges transaction, cardholder, merchant, and merchant-category tables from a relational database into a unified dataset."
  - "Engineers behavioral features: amount deviation from cardholder average, inter-transaction intervals, temporal markers (hour, day, week), and merchant-category frequency."
  - "Trains Isolation Forest (contamination=0.01, 100 trees), One-Class SVM (RBF kernel, nu=0.01, gamma=0.1), and a deep autoencoder (4-8-4 architecture) to flag anomalies via reconstruction error threshold at 99th percentile."
  - "Applies K-Means (k=3) and DBSCAN (eps=0.25, min_samples=5) to cluster transactions and isolate sparse outlier regions."
  - "Proposes an Adaptive Risk-Scoring Framework (ARF) that dynamically weights detector outputs and behavioral indicators (unusual spend, rapid use, spending sprees) via online gradient descent."
  - "Evaluates models using detection rate, false-positive rate, precision, and AUC-ROC; achieves 95% detection with 5% FPR."
findings:
  - "num: 95.3% detection rate for Isolation Forest with 4.8% FPR."
  - "num: Autoencoder achieved highest AUC-ROC of 0.971 and reconstruction error threshold at 0.215 MSE."
  - "num: 99% of transactions classified as normal; anomalies have higher median amounts (~$750-$1500)."
  - "K-Means cluster 2 contained 93% of known anomalies; DBSCAN noise points captured ~1.5% of anomalies."
  - "Composite risk scoring identified top 10 riskiest cardholders with fraud ratios near 1.0 and high-risk merchants like Walmart/Ltd."
  - "Late-night transactions (0-6 AM) have highest average risk score of 0.72."
key_figures_tables:
  - "Figure 9: Autoencoder training loss converges stably with final MSE ~0.02 and reconstruction error distribution; 99th percentile threshold effectively separates anomalies."
  - "Figure 15: K-Means clustering (k=3) separates low-, medium-, and high-value transactions; Cluster 2 contains high-value outliers and 93% of known anomalies."
  - "Table 2: Evaluation results summary: Isolation Forest (95.3% detection, 4.8% FPR, AUC-ROC 0.964), One-Class SVM (95.0%, 5.1%, 0.958), Autoencoder (94.7%, 4.5%, 0.971)."
  - "Figure 19: Correlation analysis of risk indicators shows strong positive correlation (0.55) between Isolation Forest and Unusual Spend, and negative correlation (-0.44) between Autoencoder and Unusual Spend, indicating complementary detection."
key_equations:
  - equation: "$R_{ARF}(T_t) = w_1(t) f_{IF}(T_t) + w_2(t) f_{OCSVM}(T_t) + w_3(t) f_{AE}(T_t) + w_4(t) \Delta spend(T_t) + w_5(t) \Delta time(T_t)$"
    explanation: "Composite risk score as weighted sum of detector outputs and behavioral indicators."
  - equation: "$w_i(t+1) = w_i(t) - \alpha \frac{\partial \mathcal{L}}{\partial w_i}$"
    explanation: "Online weight update via gradient descent on composite loss."
definitions:
  - term: "Isolation Forest"
    definition: "Anomaly detection algorithm that isolates outliers by random partitioning; anomalies have shorter paths."
  - term: "One-Class SVM"
    definition: "A support vector machine that learns a boundary around normal data; points outside are anomalies."
  - term: "Autoencoder"
    definition: "Neural network that reconstructs input; high reconstruction error indicates anomaly."
  - term: "Reconstruction error"
    definition: "Mean squared error between input and output of autoencoder; used as anomaly score."
  - term: "Contamination rate"
    definition: "Expected proportion of anomalies in the dataset, used to set model thresholds."
  - term: "DBSCAN"
    definition: "Density-based clustering algorithm that identifies clusters and noise points based on density."
  - term: "K-Means"
    definition: "Partitioning clustering that groups data into k clusters based on centroid distances."
  - term: "Composite risk score"
    definition: "Aggregated score combining multiple detector flags and behavioral indicators to prioritize investigation."
  - term: "Adaptive Risk-Scoring Framework (ARF)"
    definition: "Dynamic weighting of detectors based on context and online learning."
critical_citations:
  - "[Bolton & Hand, 2002] — Seminal review of statistical fraud detection methods."
  - "[Phua et al., 2010] — Comprehensive survey of data mining-based fraud detection."
  - "[Chouksey et al., 2023] — Demonstrates autoencoder effectiveness in isolating anomalous transactions."
  - "[Stripe, 2023] — Real-world implementation of ML fraud detection reducing chargebacks."
relevance:
  topics:
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews existing fraud detection systems and their limitations, relevant to gap analysis."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Identifies gaps such as high false positives and lack of adaptability, informing Odin's design."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Constructs cardholder profiles using spending deviations, frequency, and temporal patterns."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "low"
      justification: "Mentions label scarcity but does not address cold-start; provides context for unsupervised adaptation."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Evaluates multiple unsupervised classification methods (Isolation Forest, SVM, autoencoder, clustering) for anomaly labeling."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Core contribution: detecting transaction anomalies in financial data."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Implements and compares Isolation Forest, One-Class SVM, autoencoder, DBSCAN, and K-Means."
    - code: "8.C"
      name: "Cold‑Start Baseline Strategies for Anomaly Detection"
      relevance: "low"
      justification: "Briefly discusses contamination assumptions but does not propose a cold-start strategy; relevant as background."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "contextual"
      justification: "Discusses GDPR, CCPA, and emerging-market privacy regulations; suggests federated learning."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "contextual"
      justification: "Mentions consumer trust erosion after fraud incidents; indirectly relevant to trust building."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides evaluation metrics (detection rate, FPR, AUC) and benchmarks against thresholds."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Compares performance of individual models and clustering methods using quantitative metrics."
  contribution: "The anomaly detection models (Isolation Forest, autoencoder) directly inform Odin's spending anomaly detection module, enabling identification of unusual transactions. The composite risk scoring approach can be integrated into Odin's alert prioritization system to guide user review. The behavioral feature engineering (deviation, frequency, temporal) provides a foundation for Odin's user profiling and classification components. The evaluation metrics and thresholds (95% detection, 5% FPR) offer benchmarks for Odin's system evaluation. The discussion of privacy and regulatory compliance supports Odin's data governance and trust considerations."
  directly_justifies:
    - "Unsupervised autoencoders can achieve 94.7% detection rate with 4.5% FPR for spending anomalies."
    - "Isolation Forest effectively isolates high-value outliers as anomalies with 95.3% detection rate."
    - "Clustering (K-Means, DBSCAN) reveals distinct transaction patterns and can separate normal from suspicious clusters."
    - "Composite risk scoring combining multiple detectors improves prioritization and reduces investigation overhead."
    - "Adaptive Risk-Scoring Framework can dynamically calibrate weights based on context (e.g., urban vs rural)."
  limits:
    - "Not tested on Philippine financial data; generalizability to Filipino young professionals is unknown."
    - "Lacks explicit cold-start strategy for new users without transaction history; unsupervised models assume some baseline."
    - "Computational cost of autoencoder and online weight updates may be high for mobile-first deployment."
    - "Privacy-preserving mechanisms (federated learning) are suggested but not implemented."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper's core algorithmic contributions on anomaly detection and behavioral profiling mapped directly to domains 5 (Behavioral Profiling & Classification) and 8 (Anomaly Detection), with high relevance for topics 5.A, 5.C, 8.A, and 8.B. Topic 5.B (cold-start) and 8.C (cold-start baseline) were assigned low relevance as they are only tangentially mentioned. Domain 4 (Existing Systems & Gaps) was flagged as medium for topics 4.A and 4.B, based on the literature review of existing fraud systems. Domain 10 (Data Privacy & User Trust) was assessed as contextual, as privacy regulations are discussed but not central to the framework. Domain 12 (System Evaluation) was deemed medium for evaluation metrics. Domains 1 (Filipino Cultural Context), 2 (Spending Cycles), 3 (Expense Categorization), 6 (Spending Forecasting), 7 (Budget Recommendation), 9 (Mobile-First Design), 11 (Retention & Engagement), and 13 (Savings & Debt) were rejected due to lack of relevant content. Borderline cases included the mention of seasonal spending in emerging markets (potentially 2.B) but this was not a focus and was not selected. The paper's overall relevance to Odin is moderate to high, providing strong methodological grounding for anomaly detection and user profiling modules, though with limitations for the Filipino context and cold-start scenarios."
limitations:
  - "Unsupervised models may miss fraud that resembles normal behavior; no supervised refinement with labeled data."
  - "The adaptive risk-scoring framework relies on accurate contextual weight initialization and may introduce bias. [unacknowledged]"
  - "Evaluation is based on a single 12-month dataset; cross-validation across multiple datasets is missing. [unacknowledged]"
  - "The paper does not address real-time latency requirements for deployment in high-throughput environments. [unacknowledged]"
  - "Potential biases in feature engineering (e.g., wealthier cardholders have higher averages) are mentioned but not mitigated. [unacknowledged]"
remember_this:
  - "Achieved 95% anomaly detection rate with 5% false-positive rate."
  - "Autoencoder attained highest AUC-ROC of 0.971 among unsupervised detectors."
  - "Composite risk scoring identified top 10 riskiest cardholders with fraud ratios near 1.0."
  - "Late-night transactions (0-6 AM) carry the highest average risk score of 0.72."
  - "Unsupervised clustering revealed that 93% of known anomalies fall into the high-value transaction cluster."
```
---

## Paper 20: Remonde_summarized.md

**Source File:** `Remonde_summarized.md`

```yaml
paper_id: "f47ac10b-58cc-4372-a567-0e02b2c3d479"
designation: "local"
title: "The Effectiveness of Financial Literacy Program on Financial Management Skills of Millennial Teachers"
authors: "Remonde, E. A."
year: 2025
venue: "Slongan Multidisciplinary Research Journal"
odin_topics:
  - "1.A"
  - "1.C"
  - "13.A"
  - "13.B"
  - "12.A"
  - "2.A"
tldr: "Financial literacy program significantly improves financial management skills of millennial teachers across savings, budgeting, investing, debt, emergency funds, insurance, loans, expenditure, tax, and retirement."
problem_and_motivation: "Millennial teachers often lack financial literacy, leading to financial stress and poor decision-making. Existing research does not address the specific challenges of Senior High School teachers in Digos City. A tailored financial literacy program is needed to equip them with essential financial management skills."
approach:
  - "Pre-experimental design with pre-test and post-test assessments on 36 purposively selected millennial teachers."
  - "Intervention comprised a Financial Literacy Program with ten modules covering savings, budgeting, investing, debt, emergency funds, insurance, loans, expenditure, tax, and retirement planning."
  - "Data collected via validated multiple-choice survey questionnaires administered before and after the program."
  - "Statistical analysis employed mean, standard deviation, and paired samples t-test to compare pre-test and post-test scores."
findings:
  - "num: Pre-test overall mean score was 32.22 (approaching proficient), and post-test mean rose to 43.19 (advanced)."
  - "num: Paired samples t-test yielded a significance value of .000, indicating a statistically significant improvement (p < .05)."
  - "All ten financial management areas showed post-test mean scores in the 'Advance' range, with retirement planning scoring highest (4.75) and investing lowest (4.28)."
  - "Emergency funds had the highest pre-test mean (3.53), while investing had the lowest (3.14), both approaching proficient or developing."
key_figures_tables:
  - "Table 1: Pre-test mean scores by financial skill → baseline shows approaching proficiency overall, with gaps in investing and tax planning."
  - "Table 2: Post-test mean scores by financial skill → all skills advanced, indicating mastery across all areas."
  - "Table 3: Comparison of pre- and post-test means → t-test confirms significant improvement with p < .001."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Financial Literacy"
    definition: "Knowledge and skills to manage personal finances and make sound financial decisions."
  - term: "Millennial"
    definition: "Individuals born from the early 1980s to the mid-1990s."
  - term: "Pre-experimental design"
    definition: "Research design measuring changes before and after intervention without a control group."
critical_citations:
  - "[Lusardi and Mitchell, 2014] — foundational framework for financial literacy importance."
  - "[Miraj et al., 2023] — evidence of program effectiveness in similar context."
  - "[Wagner, 2015] — highlights millennial financial challenges."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "high"
      justification: "Paper focuses on Filipino millennial teachers, a subset of young professionals."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Directly measures financial management behaviors including savings, budgeting, and investing."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "high"
      justification: "Covers savings, emergency funds, and retirement planning."
    - code: "13.B"
      name: "Debt Management in PFMS"
      relevance: "high"
      justification: "Includes debt and loan management as key assessment areas."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Uses pre-test/post-test evaluation methodology applicable to system evaluation."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "low"
      justification: "Conducted in the Philippines but does not address specific cultural practices like paluwagan."
  contribution: "The study validates the need for targeted financial education modules on savings, debt, and budgeting, which inform Odin's user onboarding and educational content. Its pre-experimental evaluation design offers a model for assessing Odin's intervention impact. Findings on baseline proficiency gaps support Odin's cold-start user profiling and personalized recommendation features. The significant improvement post-training underscores the potential of structured financial literacy programs to enhance user financial behaviors within Odin."
  directly_justifies:
    - "Millennial teachers in Digos City have approaching proficiency in financial management before training."
    - "A structured financial literacy program can elevate financial management skills from approaching proficient to advanced."
    - "Significant improvements were observed across all ten financial management areas after the program."
  limits:
    - "No control group limits causal attribution of improvements solely to the program."
    - "Self-reported survey data may introduce bias."
    - "Findings are geographically limited to Digos City and may not generalize."
    - "Long-term retention of skills was not assessed."
  mapping_rationale: "Systematic scan across all 12 functional domains identified relevance in Filipino cultural context (Domain 2), financial behavior (Domain 1), savings and debt management (Domain 13), and evaluation frameworks (Domain 12). Topics 1.A and 1.C were flagged high due to direct focus on Filipino millennial teachers' financial behaviors. Topics 13.A and 13.B were flagged high because the paper measures savings, emergency funds, debt, and loan management – core modules in Odin. Topic 12.A was medium as the evaluation methodology (pre-test/post-test) could inform Odin's system evaluation but is not algorithm-specific. Topic 2.A was low because although Philippine-based, it does not explore culturally specific practices like paluwagan. Domains such as expense categorization (3), existing systems (4), behavioral profiling (5), forecasting (6), budget recommendation (7), anomaly detection (8), mobile-first (9), privacy (10), and retention (11) were rejected as the paper does not address algorithmic or system design aspects. Overall, the paper provides empirical evidence on financial literacy gaps and intervention effectiveness, which supports Odin's educational and behavioral modules."
limitations:
  - "Limited generalizability due to geographic and demographic constraints."
  - "Self-reporting bias may affect accuracy of financial skill assessment. [unacknowledged]"
  - "No control group; pre-experimental design weakens causal inference."
  - "Short-term measurement; long-term effects not examined. [unacknowledged]"
remember_this:
  - "Financial literacy program raised overall mean score from 32.22 to 43.19."
  - "Millennial teachers showed greatest improvement in retirement planning and loan management."
  - "Investing skill had the lowest post-test mean, indicating persistent need for investment education."
  - "Significant p < .001 confirms program effectiveness across all financial domains."
```
---

## Paper 21: Torres et al-2025a_summarized.md

**Source File:** `Torres et al-2025a_summarized.md`

```yaml
paper_id: "10.1145/3785171.3785192"
designation: "local"
title: "Consumer’s Financial Habits on Server-Based Electronic Money as It Affects Their Financial Behavior: Moderated By Monthly Transactions"
authors: "Torres, R. C.; Olaivar, G. M.; Britanico, S. I."
year: 2025
venue: "The 9th International Conference on Business and Information Management"
odin_topics:
  - "1.C"
  - "2.A"
  - "5.A"
  - "5.C"
tldr: "Saving, spending, donating, and investing habits significantly affect financial behavior on GCash, with transaction frequency moderating the spending-behavior relationship."
problem_and_motivation: "The rapid adoption of e-wallets in the Philippines necessitates understanding how specific financial habits influence consumer behavior on these platforms. The role of transaction frequency as a moderator in this relationship is not well-established, particularly for Filipino users."
approach:
  - "Quantitative study with 300 Filipino GCash users selected via purposive sampling."
  - "Multiple regression analysis used to test the effect of five financial habits on consumer financial behavior."
  - "Moderation analysis conducted to test the effect of average monthly transaction frequency on these relationships."
  - "Grounded in the Theory of Planned Behavior."
  - "Data collected via online questionnaires distributed through Google Forms and social media."
findings:
  - "num: Investment habits had the strongest significant positive effect on financial behavior (β = 0.243)."
  - "num: Spending habits significantly influence financial behavior (β = 0.115)."
  - "num: Saving habits significantly influence financial behavior (β = 0.178)."
  - "num: Donating habits significantly influence financial behavior (β = 0.144)."
  - "Credit/loan habits showed no significant effect on financial behavior."
  - "num: Transaction frequency significantly moderates the effect of spending habits on financial behavior (β = -0.163)."
  - "Higher transaction volumes enhance the positive relationship between spending habits and financial behavior."
  - "num: The model explains 40% of the variance in consumer financial behavior (R² = 0.400)."
key_figures_tables:
  - "Figure 1: Conceptual Framework based on TPB → Shows the hypothesized moderating role of monthly transactions."
  - "Table 1: Coefficients for the Regression Model → Shows significant effects for all habits except credit/loan."
key_equations:
  - equation: "y = β0 + β1x1 + β2x2 + β3x3 + β4x4 + β5x5 + ϵ"
    explanation: "Multiple regression equation for predicting financial behavior from financial habits."
definitions:
  - term: "SBEM"
    definition: "Server-Based Electronic Money, e.g., digital wallets and mobile payment platforms."
  - term: "GCash"
    definition: "A leading mobile wallet and digital payment platform in the Philippines."
  - term: "TPB"
    definition: "Theory of Planned Behavior, a psychological theory linking beliefs to behavior."
critical_citations:
  - "[Gomber et al., 2017] — Establishes the link between FinTech and changing financial behavior."
  - "[Raaij, 2016] — Discusses the psychological factors in consumer financial behavior."
  - "[Memon et al., 2019] — Provides guidelines for moderation analysis."
relevance:
  topics:
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Directly models financial behaviors of Filipino GCash users."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "medium"
      justification: "Examines financial habits within the Philippine digital payment context."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Provides a regression-based model for classifying financial habits."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "Uses quantitative statistical methods to identify significant financial habit predictors."
  contribution: "This paper provides empirical evidence from the Philippines that can inform Odin's user profiling module by identifying which financial habits (e.g., investing, saving) are most predictive of overall financial behavior. The findings on the moderating effect of transaction frequency can guide Odin's dynamic user modeling and personalization strategies. The relationship between investment habits and financial behavior suggests Odin could offer savings and investment features to improve user outcomes. The significant moderation effect implies that Odin's behavioral models should account for user activity level."
  directly_justifies:
    - "Investment habits have the strongest positive influence on financial behavior."
    - "Monthly transaction frequency moderates the impact of spending habits."
    - "Financial habits collectively explain a significant portion of financial behavior variance."
    - "Digital platforms like GCash can foster positive financial habits."
  limits:
    - "The study is cross-sectional and cannot establish causality."
    - "The sample is limited to Filipino GCash users, limiting generalizability."
    - "Relies on self-reported data, which may introduce bias."
    - "Does not account for user demographics in the main analysis beyond sampling."
  mapping_rationale: "The systematic scan across all 12 functional domains identified Behavioral Profiling & Classification (5.A, 5.C) and Filipino Cultural Context (2.A, 1.C) as the primary relevant areas. The paper's core contribution is analyzing financial habits (saving, spending, etc.) and their impact on behavior, which is directly applicable to understanding Filipino user profiles (1.C, 5.A). The moderation analysis offers insights into profile dynamics (5.C). Domains like Expense Categorization (3.A) and Forecasting (6.A) were rejected as the paper does not address algorithmic or system design aspects of these areas. The paper was assessed as having high relevance for Odin's user understanding and behavioral modeling, and medium relevance for cultural context."
limitations:
  - "Cross-sectional design, cannot establish causality. [unacknowledged]"
  - "Sample limited to GCash users in the Philippines. [unacknowledged]"
  - "Relies on self-report measures, potentially introducing response bias. [unacknowledged]"
  - "The study does not explore long-term behavioral trends. [acknowledged]"
remember_this:
  - "Investment habits show the strongest link to positive financial behavior."
  - "Transaction frequency strengthens the link between spending and financial behavior."
  - "Credit and loan habits did not significantly affect financial behavior in this sample."
  - "A model with five habits explains 40% of variance in financial behavior."
```
---

## Paper 22: Kashif & Naseer_summarized.md

**Source File:** `Kashif & Naseer_summarized.md`

```yaml
paper_id: 10.5281/zenodo.15081246
designation: international-algorithm-specific
title: Comprehensive Analysis of Fraud Detection and Prevention Systems for Accuracy and Efficacy
authors: Kashif, H.; Naseer, F.
year: 2025
venue: Unknown
odin_topics:
  - 5.A
  - 5.C
  - 8.A
  - 8.B
  - 8.C
  - 12.A
  - 12.B
tldr: A systematic evaluation of fraud detection systems finds hybrid supervised-unsupervised learning approaches achieve superior performance over rule-based methods.
problem_and_motivation: Financial fraud costs global economies trillions annually, yet existing detection systems face challenges in accuracy, adaptability, and real-time processing. A systematic evaluation of contemporary fraud detection and prevention systems across major financial institutions is needed to identify optimal approaches.
approach:
  - A mixed-methods approach combined quantitative performance metrics from financial institutions with qualitative assessments from cybersecurity specialists.
  - The study evaluated detection algorithms across four dimensions: detection accuracy, computational efficiency, adaptability to emerging threats, and implementation feasibility.
  - Performance of detection techniques was analyzed based on their accuracy, speed, and cost in a comparative study.
findings:
  - num: Hybrid machine learning approaches combining supervised and unsupervised anomaly detection achieved 92.7% detection accuracy.
  - num: Traditional rule-based systems achieved 78.3% detection accuracy.
  - num: Models integrating graph-based network analysis with deep learning reduced false positives by 34%.
  - num: The same hybrid graph-based models increased true positive rates by 27% compared to standalone approaches.
  - num: Implementing a next-generation architectural framework emphasizing real-time adaptability could potentially reduce overall fraud losses by an estimated 41%.
  - The study categorizes financial fraud by financial institution involved, including securities fraud, bank-related scams, and insurance scams.
  - Support Vector Machine (SVM) has a low detection speed among compared techniques.
  - Artificial Immune System (AIS) has a high detection speed among compared techniques.
key_figures_tables:
  - "Table 1: Benefits and drawbacks of various fraud detection techniques → Provides a comparative summary of technique trade-offs."
  - "Table 2: Comparison of fraud detection techniques by speed, accuracy, and cost → Highlights Artificial Immune System as Very Fast, Good, and Inexpensive."
  - "Figure 1: Classification of Financial Institution and its types → Provides a framework for categorizing financial fraud."
  - "Figure 2: Fraud Detection Working Scenario → Illustrates the overall process of fraud detection."
  - "Figure 3: Count Nested → Shows the hierarchical relationship between AI, machine learning, neural networks, and deep learning."
  - "Figure 4: Simple Neural Network → Illustrates the structure of a basic neural network."
  - "Figure 5: Flowchart of Genetic Algorithm Process → Depicts the iterative process of a genetic algorithm."
  - "Figure 6: Flowchart of Training and Detection Phase in HMM → Shows the two phases of the Hidden Markov Model approach."
  - "Figure 7: BNN Graphical Representation → Depicts a Bayesian Belief Network as a directed acyclic graph."
  - "Figure 8: System Architecture of Cluster Method → Shows the architecture for a clustering-based detection system."
  - "Figure 9: Decision Tree Representation → Illustrates a basic decision tree structure."
  - "Figure 10: Fraud Prevention Steps → Outlines the eight steps in a fraud prevention strategy."
key_equations:
  - equation: "net = \u03A3(wi × xi)"
    explanation: "Calculates weighted sum of inputs to a neuron."
  - equation: "P(H|E) = P(E|H)P(H) / P(E)"
    explanation: "Bayes' theorem for calculating conditional probability."
definitions:
  - term: AIS
    definition: "Artificial Immune System, a data mining strategy detecting antigens by mimicking biological immune system behavior."
  - term: NN
    definition: "Neural Network, a computer model representing the human brain using vertices and edges."
  - term: GA
    definition: "Genetic Algorithm, an algorithm employing resident development to iteratively enhance solutions."
  - term: HMM
    definition: "Hidden Markov Model, a statistical model where the system is believed to remain a Markov process with an unseen state."
  - term: BBN
    definition: "Bayesian Belief Network, a statistical categorization approach employing Bayes' theorem."
  - term: SVM
    definition: "Support Vector Machine, a statistical learning approach that builds a hyperplane to maximize the distance between positive and negative modes."
critical_citations:
  - "[Ngai et al., 2011] — Foundational review of data mining techniques for financial fraud detection."
  - "[Bhattacharyya et al., 2011] — Comparative study on data mining for credit card fraud."
  - "[Quah and Sriganesh, 2008] — Real-time credit card fraud detection using computational intelligence."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "contextual"
      justification: "Discusses fraud detection techniques as a form of behavioral analysis."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "Compares various classification algorithms (SVM, DT, NN) for detecting fraudulent behavior."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Fraud detection is a core application of anomaly detection in financial systems."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Directly evaluates and compares multiple anomaly detection algorithms (NN, GA, HMM, BBN, etc.) for fraud."
    - code: "8.C"
      name: "Cold-Start Baseline Strategies for Anomaly Detection"
      relevance: "low"
      justification: "Mentions the challenge of training models without extensive labeled data but does not deeply address cold-start."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Proposes a framework for evaluating fraud detection systems across accuracy, speed, and cost."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Provides a detailed evaluation and comparison of various algorithmic modules for fraud detection."
  contribution: "This paper systematically evaluates and compares a wide range of fraud detection algorithms (NN, GA, HMM, BBN, DT, SVM, AIS, CM, SOM) using metrics like accuracy, speed, and cost. The findings justify Odin's adoption of hybrid anomaly detection approaches over simple rule-based systems for its Anomaly Detection Module (8.B). The proposed evaluation framework directly informs Odin's evaluation methodology for its algorithmic modules (12.B). The emphasis on adaptability and real-time processing supports the design priorities for Odin's forecasting and detection systems. The paper's categorization of fraud types can inform Odin's expense categorization logic."
  directly_justifies:
    - "Hybrid models combining supervised and unsupervised learning achieve superior fraud detection accuracy (92.7%)."
    - "Graph-based network analysis with deep learning significantly reduces false positives in anomaly detection."
    - "Adaptability is a critical requirement for effective anomaly detection systems."
    - "Evaluation of fraud detection systems must consider accuracy, speed, and cost."
  limits:
    - "The study is a literature review and comparative analysis, not an empirical implementation or validation of a single system."
    - "The comparative performance metrics (speed, accuracy, cost) are synthesized from the reviewed literature and may not be directly comparable due to different experimental setups."
    - "The paper does not specifically address financial data privacy concerns, which is a key domain for Odin. [unacknowledged]"
    - "The proposed next-generation framework is conceptual and lacks a detailed architectural specification or implementation plan."
  mapping_rationale: "A systematic scan was performed across all 12 functional domains. The domains flagged as relevant were 'Anomaly Detection' and 'System Evaluation'. Within the Anomaly Detection domain, the paper's core contribution directly relates to algorithms for fraud detection (8.B), with high relevance. It also provides comparative classification approaches (5.C) with medium relevance and contextual information on behavioral profiling (5.A). The paper's evaluation framework is highly relevant to 12.B and medium relevant to 12.A. Other domains, such as 'Filipino Cultural Context', 'Expense Categorization', 'Budget Recommendation', and 'Savings & Debt Management', were considered and rejected as the paper is a general survey of fraud detection techniques without specific application to personal finance management, Filipino culture, or these other domains. The overall relevance to Odin is moderate, providing strong justification for algorithm selection and evaluation but lacking direct application to the broader PFMS context."
limitations:
  - "The study is a literature review and comparative analysis, not an empirical implementation or validation of a single system."
  - "The comparative performance metrics (speed, accuracy, cost) are synthesized from the reviewed literature and may not be directly comparable due to different experimental setups."
  - "The paper does not specifically address financial data privacy concerns, which is a key domain for Odin. [unacknowledged]"
  - "The proposed next-generation framework is conceptual and lacks a detailed architectural specification or implementation plan."
remember_this:
  - "Hybrid machine learning models achieve 92.7% fraud detection accuracy."
  - "Graph-based deep learning reduces false positives by 34% compared to standalone methods."
  - "Adaptability is a critical requirement for effective anomaly detection systems."
  - "A mixed-methods approach is valuable for evaluating complex financial systems."
```
---

## Paper 23: Vega et al_summarized.md

**Source File:** `Vega et al_summarized.md`

```yaml
paper_id: 52c5e0a0-d0a0-5b1a-9c4e-8f6b9e2f1c3a
designation: local
title: The Influence of Buy Now, Pay Later (BNPL) Services on Consumer Spending Behavior
authors: Vega, N. C.; Constante, K. J. G.; Pacson, K. C.; Samaniego, J. G.; Tobias, T. E.
year: 2025
venue: International Journal of Sustainability and Advanced Integrated Research
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.C
  - 4.B
  - 5.A
  - 5.B
  - 7.A
  - 7.D
  - 8.A
  - 13.A
  - 13.B
tldr: BNPL services increase impulse buying and purchase frequency among young Filipino users, highlighting gaps in consistent budgeting and debt management.
problem_and_motivation: BNPL services are rapidly growing, but their influence on consumer spending behavior, particularly among young Filipinos, remains underexplored. Understanding these effects is crucial to prevent overspending and debt accumulation.
approach:
  - The study used a descriptive quantitative research design with structured surveys.
  - Data were gathered from 94% of respondents aged 18-25 in Gapan City, Nueva Ecija.
  - The survey instrument covered impulse buying, purchase frequency, budgeting, and debt accumulation.
  - Weighted means were calculated to determine levels of agreement across dimensions.
findings:
  - num: 94% of respondents were aged 18-25, and 74% were students with monthly incomes below PHP 5,000.
  - num: Respondents showed moderate agreement (WM = 2.71) on impulse buying tendencies when using BNPL.
  - num: BNPL services contributed to a noticeable increase in purchase frequency (WM = 2.67).
  - num: Awareness of BNPL repayment obligations was relatively high (WM = 2.91).
  - num: Moderate agreement was found on debt accumulation (WM = 2.55) and financial strain (WM = 2.65).
  - Users rely on future income to cover BNPL payments (WM = 2.84).
  - Many respondents lack consistent budgeting strategies and formal expense-tracking tools.
  - Multiple BNPL commitments were not yet overwhelming but signaled future challenges.
key_figures_tables:
  - "Figure 1: Top 11 products in BNPL purchase category → Clothing is the most common BNPL purchase."
  - "Figure 2: Types of goods bought with BNPL in the Philippines → Electronics and appliances are top purchases."
  - "Figure 3: Geographic location of the study area → Study focused on Gapan City, Nueva Ecija."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: BNPL
    definition: Buy Now, Pay Later, a payment method allowing consumers to make purchases and defer payment over time, often interest-free.
  - term: Impulse Buying
    definition: An unplanned purchase driven by emotions or a sudden urge without considering consequences.
  - term: Mental Accounting
    definition: The cognitive process of categorizing and evaluating financial transactions, which can affect spending decisions.
critical_citations:
  - "[Ang & Maesen, 2024] — BNPL increases purchase likelihood from 17% to 26%."
  - "[Bezawada et al., 2024] — BNPL adoption increases online spending by 6.42%."
  - "[Di Maggio et al., 2022] — BNPL increases purchasing power but may burden finances."
  - "[Gilbert et al., 2022] — Lower financial literacy leads to higher BNPL use and perceived lower risk."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: "The study focuses on young Filipinos (18-25), a key user group for BNPL and Odin."
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: "Provides data on income (below PHP 5,000) and employment status (mostly students) of BNPL users."
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: "Directly examines impulse buying, budgeting, and debt accumulation behaviors."
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: "Provides local context on BNPL use in Gapan City, reflecting Filipino consumer habits."
    - code: 2.C
      name: User-Declared Financial Preferences
      relevance: medium
      justification: "Surveys user perceptions of BNPL convenience, affordability, and budgeting ease."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: "Highlights gaps in BNPL regulation, transparency, and user financial literacy."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: "Identifies behavioral tendencies like impulse buying and reliance on future income."
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: "Tangential; discusses user behavior but not profile dynamics or cold-start issues."
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: "Examines budgeting strategies and their inconsistency among BNPL users."
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: low
      justification: "Tangential; mentions budget allocation but does not address infeasibility handling."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: "Provides context on financial strain and missed payments but not anomaly detection algorithms."
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: "Discusses how BNPL balances make it hard to save."
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: "Directly addresses debt accumulation and management challenges with BNPL."
  contribution: "This paper directly justifies Odin's behavioral profiling module by identifying specific spending tendencies among young Filipinos, such as impulse buying and reliance on future income. It informs the budgeting recommendation engine by highlighting gaps in users' budget planning and the need for simple, integrated tools. The findings on debt accumulation and awareness of repayment terms support Odin's anomaly detection and financial literacy features, as users exhibit moderate awareness but lack consistent tracking."
  directly_justifies:
    - "BNPL services increase impulse buying and purchase frequency among young Filipino users."
    - "Users show moderate awareness of repayment obligations but exhibit gaps in consistent budgeting and use of tracking tools."
    - "Reliance on future income to meet BNPL commitments highlights a need for better cash flow management and budgeting support."
    - "The study identifies a demand for centralized tools to manage multiple BNPL accounts and prevent debt accumulation."
  limits:
    - "The study is limited to Gapan City, Nueva Ecija, and may not be generalizable to the entire Philippines."
    - "The sample is skewed towards students (74%) with low income, limiting applicability to other demographic groups."
    - "Self-reported survey data may introduce social desirability and recall bias. [unacknowledged]"
    - "The cross-sectional design prevents causal inferences about BNPL's long-term effects. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The study was flagged as highly relevant to the Filipino Cultural Context (2.A, 2.C) as it provides local data on BNPL use in the Philippines. It was also highly relevant to Behavioral Profiling (5.A) and Savings & Debt Management (13.B) due to its direct examination of impulse buying, budgeting, and debt accumulation. The study was considered for but rejected from the Forecasting (6.A, 6.B) domain as it does not propose or evaluate predictive algorithms, and from Mobile-First Design (9.A, 9.B) as it does not address UX principles. Borderline cases included the study's relevance to both User-Declared Preferences (2.C) and Budgeting Strategies (7.A), as it surveys user perceptions and examines budgeting practices. Overall, the paper provides strong behavioral insights and identifies gaps in financial management, making it relevant to Odin's user understanding and advisory modules."
limitations:
  - "The study is limited to Gapan City, Nueva Ecija, and may not be generalizable to the entire Philippines."
  - "The sample is skewed towards students (74%) and low-income earners, limiting applicability to other groups."
  - "The cross-sectional design prevents causal inferences about BNPL's long-term effects. [unacknowledged]"
  - "Self-reported survey data may introduce social desirability and recall bias. [unacknowledged]"
  - "The study does not employ algorithmic methods, limiting its relevance to Odin's predictive and recommendation modules. [unacknowledged]"
remember_this:
  - "BNPL increases impulse buying (WM 2.71) and purchase frequency (WM 2.67) among young Filipinos."
  - "Awareness of BNPL obligations is high (WM 2.91) but budgeting and tracking remain inconsistent."
  - "Moderate debt accumulation (WM 2.55) and reliance on future income (WM 2.84) are key risks."
  - "Centralized BNPL management tools are in demand to prevent future financial strain."
```
---

## Paper 24: Weng_summarized.md

**Source File:** `Weng_summarized.md`

```yaml
paper_id: 5df13fe4-3a7a-5a44-b794-187b42a3d847
designation: international-algorithm-specific
title: Deep Embedding Clustering with Adaptive Feature Selection for Banking Customer Segmentation
authors: Weng, H.
year: 2025
venue: Spectrum of Research
odin_topics:
  - "5.A"
  - "5.C"
  - "4.A"
  - "4.B"
  - "7.A"
  - "10.A"
tldr: A deep embedding clustering framework with adaptive feature selection and business constraints discovers behavioral segments for banking marketing.
problem_and_motivation: Traditional clustering methods fail to capture complex behavioral patterns in high-dimensional credit card transaction data and lack interpretability for business decisions. Banking applications require sophisticated customer segmentation that balances algorithmic performance with actionable insights.
approach:
  - "A stacked autoencoder learns low-dimensional embeddings of behavioral features from a dataset of 7.9 million credit card customers."
  - "Kullback-Leibler divergence minimizes clustering loss on embeddings with an annealing schedule balancing reconstruction and clustering objectives."
  - "Mutual information quantifies feature relevance while a greedy selection algorithm minimizes redundancy, selecting 35 features."
  - "Mandatory inclusion ensures business-critical features like credit utilization are always included in the final subset."
  - "Business constraints enforce minimum cluster size, balanced distribution, temporal stability, and interpretability through sparse profiles."
  - "Clustering quality is evaluated using silhouette coefficient, Davies-Bouldin index, and Calinski-Harabasz score."
  - "K-Means++, hierarchical clustering, and Gaussian mixture models serve as baseline comparisons."
  - "The framework discovers eight distinct behavioral segments, each described by an average of 4.2 differentiating characteristics."
findings:
  - "num: The proposed method achieves a silhouette score of 0.673, significantly outperforming K-Means at 0.524 and hierarchical clustering at 0.558."
  - "num: Davies-Bouldin index improves to 0.847 compared to 1.234 for K-Means and 1.089 for Gaussian mixture models."
  - "num: Calinski-Harabasz score reaches 8,947, exceeding K-Means at 5,432 and DBSCAN at 6,104."
  - "Performance improvements are statistically significant with p-values below 0.001 from permutation tests."
  - "All eight discovered clusters exceed the minimum viable campaign size of 50,000 customers, with the smallest at 187,000."
  - "Segments are described using an average of 4.2 key differentiating characteristics, supporting clear marketing strategy development."
key_figures_tables:
  - "Figure 1: Mutual information-based feature selection process flowchart highlighting feature extraction, MI computation, redundancy analysis, and final selection."
  - "Table II: Top-20 features ranked by mutual information scores, showing selected and redundant features for banking segmentation."
  - "Figure 2: Training convergence plot showing reconstruction loss, clustering loss, and silhouette score progression over 150 epochs with key events."
  - "Figure 3: Radar chart visualization of eight discovered cluster behavioral profiles with key dimensions for cross-segment comparison."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "None."
    definition: ""
critical_citations:
  - "None."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Directly introduces a deep clustering method for deriving behavioral segments from transaction data."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Proposes a novel classification framework using deep embedding clustering for customer segmentation."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews traditional clustering methods like K-Means and hierarchical clustering used in financial analytics."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Explicitly identifies the inability of traditional methods to capture complex nonlinear patterns in financial data."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "low"
      justification: "Discusses segmentation for marketing strategies and resource optimization, tangentially related to budget allocation."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "contextual"
      justification: "Mentions privacy regulations like GDPR and CCPA as constraints on data usage and profiling."
  contribution: "Provides a deep learning framework for behavioral segmentation that can be adapted for Odin's user profile module. The mutual information-based feature selection technique supports the identification of discriminative financial behaviors. Business-constrained optimization principles can inform how Odin generates actionable spending insights. The approach for handling cold-start through embedding and clustering is relevant to Odin's classification challenges. The framework's design for marketing applications offers a template for segment-based budgeting features."
  directly_justifies:
    - "Deep embedding clustering can discover behavioral patterns not found by traditional methods."
    - "Feature selection based on mutual information identifies the most discriminative spending indicators."
    - "Business constraints ensure discovered segments are large enough for actionable insights."
    - "The adaptive feature mechanism balances data-driven discovery with the retention of critical financial indicators."
  limits:
    - "The model was developed for credit card customer segmentation and not directly tested on personal finance management data."
    - "The business constraints are tailored to marketing campaigns and may not directly transfer to budgeting constraints."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. Domains relevant to behavioral profiling (Topic 5.A and 5.C) were flagged as high relevance due to the paper's core contribution to customer segmentation. The domains related to system evaluation (Topic 4.A and 4.B) were assessed as medium and high relevance, as the paper extensively reviews existing segmentation methods and their limitations. Other domains, such as forecasting (Topic 6) and budget recommendation (Topic 7), were considered but found to be only low or contextual relevance; while the paper mentions spending patterns, it does not focus on predictive modeling or budget allocation. Data privacy (Topic 10.A) was noted as a contextual mention due to regulatory constraints. The paper's focus on clustering, feature selection, and segmentation for marketing strategies aligns primarily with behavioral profiling, making it a valuable reference for Odin's user classification module."
limitations:
  - "The paper does not provide performance details for segment assignment of new customers. [unacknowledged]"
  - "No analysis is included on segment stability over time, which is critical for long-term strategy. [unacknowledged]"
  - "Interpretability of the embeddings for non-technical users is not thoroughly assessed. [unacknowledged]"
remember_this:
  - "Deep embedding clustering achieves a silhouette score of 0.673 for banking segmentation."
  - "Mutual information identified 35 key behavioral features from 247 available indicators."
  - "Business constraints ensure each discovered segment exceeds a minimum viable size."
  - "Eight distinct behavioral segments were found, including Premium Travelers and Digital Natives."
```
---

## Paper 25: Darwish et al_summarized.md

**Source File:** `Darwish et al_summarized.md`

```yaml
paper_id: 10.1038/s41598-025-01223-8
designation: international-algorithm-specific
title: Intelligent approach to detecting online fraudulent trading with solution for imbalanced data in fintech forensics
authors: Darwish, S. M.; Salama, A. I.; Elzoghabi, A. A.
year: 2025
venue: Scientific Reports
odin_topics:
  - 8.A
  - 8.B
  - 8.C
  - 9.B
  - 12.A
  - 12.B
  - 12.C
tldr: A multi-stage fraud detection framework using ABC-based sampling and KNN classification addresses class imbalance and detects anomalous trading behaviors.
problem_and_motivation: Fraud detection in Fintech is challenged by imbalanced datasets where legitimate transactions vastly outnumber fraudulent ones, causing traditional machine learning models to exhibit high false negative rates. The choice of sampling technique requires domain expertise and experimentation, which is time-consuming and resource-intensive.
approach:
  - Artificial Bee Colony optimization generates synthetic minority samples to balance transaction data.
  - Rule-based filtering acts as an initial gatekeeper, flagging transactions that deviate from normal profiles.
  - K-means clustering groups transactions into legitimate and fraudulent clusters based on behavioral features.
  - ABC algorithm refines cluster centroids and assignments to enhance fraud detection accuracy.
  - KNN classifier performs final classification by comparing transactions to optimized solutions from training.
  - The framework combines unsupervised clustering and supervised classification in a multi-level pipeline.
findings:
  - num: ABC-Sampling achieved 95.7% accuracy and 87.3% F-measure, outperforming SMOTE and other techniques.
  - num: The proposed model attained 95.0% accuracy, 92.0% precision, 93.5% recall, and an AUC-ROC of 0.97.
  - Transaction amount and location are the most critical features for detecting fraudulent activities.
  - num: The multi-stage system maintained an average latency of 120 ms, supporting real-time fraud detection.
  - num: K-means clustering achieved 92.6% accuracy for legitimate traders and 90.2% for fraudulent traders.
key_figures_tables:
  - Table 4: Comparison of sampling techniques → ABC-Sampling outperforms all with 95.7% accuracy and 87.3% F-measure.
  - Table 7: Performance benchmarking vs. state-of-the-art → Proposed algorithm achieves highest accuracy and AUC-ROC at 95.0% and 0.97.
  - Table 8: Impact of data size and quality → Model maintains ≥85% accuracy even with 50% data or 5% noise.
  - Table 9: Real-time performance metrics → Throughput scales to 9,700 transactions/sec with latency under 200 ms.
key_equations:
  - equation: F(X_i) = 1 / (1 + dist(X_i, Centroid_fraud))
    explanation: Evaluates synthetic transaction realism based on distance to fraudulent centroid.
  - equation: P_i = F(X_i) / sum_{j=1}^{N} F(X_j)
    explanation: Probability of selecting a food source based on its fitness value.
  - equation: V_{ij} = X_{ij} + phi_{ij} * (X_{ij} - X_{kj})
    explanation: Generates new synthetic samples by exploring neighboring feature values.
definitions:
  - term: ABC-Sampling
    definition: Artificial Bee Colony optimization technique for generating synthetic samples to balance imbalanced datasets.
  - term: Fintech Forensics
    definition: Investigation of financial technology systems, transactions, and data to detect fraud.
  - term: Behavioral Profile
    definition: A model of an account's normal transaction behavior used to identify deviations indicative of fraud.
  - term: Multi-Stage Classification
    definition: A hierarchical detection pipeline combining rule-based filtering, clustering, and optimization-based classification.
critical_citations:
  - "[Khodabandehlou, 2024] — Introduced unsupervised graph-based fraud detection in dynamic streams."
  - "[Teng, 2024] — Proposed BalanceGAN for handling imbalanced online trading fraud data."
  - "[Vanini, 2023] — Developed risk modeling with ML-based optimization for payment fraud."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: The paper directly addresses anomaly detection for fraudulent transactions using behavioral profiling.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: The paper proposes and evaluates a novel ABC-based anomaly detection framework.
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: medium
      justification: The model uses historical data to establish profiles, but does not specifically address cold-start scenarios.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: contextual
      justification: The system is designed for real-time transaction processing, relevant to mobile app deployment contexts.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: The paper provides a comprehensive evaluation framework with accuracy, precision, recall, and F1 metrics.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: The paper benchmarks ABC-Sampling against SMOTE and other methods, evaluating each module's performance.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: low
      justification: The paper focuses on fraud detection evaluation, not budget recommendation methodologies.
  contribution: The paper provides an ABC-based sampling technique that can inform Odin's anomaly detection module by offering a method to handle imbalanced spending data. The multi-stage classification framework combining clustering and KNN offers a design pattern for Odin's fraud and anomaly detection pipeline. The feature importance analysis highlights transaction amount and location as critical signals, which can guide Odin's feature engineering for spending anomaly detection. The real-time performance metrics demonstrate that optimization-based approaches can meet latency requirements for mobile-first personal finance applications. The comparative evaluation methodology can be adapted for Odin's system-level validation of anomaly detection and spending pattern analysis modules.
  directly_justifies:
    - ABC-Sampling effectively balances imbalanced transaction datasets, improving fraud detection recall.
    - Multi-stage classification reduces false positives while maintaining high detection accuracy.
    - Transaction amount and location are the most discriminative features for detecting anomalies.
    - Real-time processing at 120 ms latency is achievable with optimization-based anomaly detection.
  limits:
    - Reliance on historical data may not capture novel fraud tactics not previously observed.
    - Computational overhead from ABC-sampling may impact scalability for large-scale datasets.
    - The clustering approach assumes fraudulent behaviors are distinct and separable, which may not hold for sophisticated fraudsters mimicking legitimate patterns.
    - Cross-market and cross-geography robustness remains to be thoroughly validated.
  mapping_rationale: All 12 functional domains and their associated topic codes were systematically scanned against the paper's content. The anomaly detection domain (8.A, 8.B, 8.C) was flagged as highly relevant because the paper's core contribution is an ABC-based sampling and multi-stage classification framework for identifying fraudulent transactions—a direct analogue to Odin's anomaly detection use case. The evaluation domain (12.A, 12.B, 12.C) was flagged as medium-to-high relevance because the paper provides extensive benchmarking and performance metrics that can inform Odin's system evaluation methodology. The mobile UX domain (9.B) was marked contextual because while the system is designed for real-time processing, the paper does not specifically address mobile user experience design. The behavioral profiling domain (5.A, 5.B) was considered but rejected because the paper's profiling approach is tailored to fraud detection, not general financial behavioral classification. The budgeting and forecasting domains were rejected as the paper does not address budget allocation, forecasting, or savings management. The paper is overall highly relevant to Odin's anomaly detection and system evaluation modules, offering algorithmic techniques and evaluation frameworks that can be adapted for detecting unusual spending patterns in Filipino young professionals' financial data.
limitations:
  - The ABC-Sampling technique introduces computational overhead that may impact real-time applicability for large-scale datasets.
  - The model's effectiveness depends on the quality and diversity of the training dataset; biases could reduce generalization.
  - The clustering approach assumes fraudulent behaviors are distinct, which may not hold for sophisticated fraudsters.
  - Cross-market and cross-geography robustness of the model remains to be thoroughly validated. [unacknowledged]
  - The study does not address the cold-start problem for new users or accounts with limited transaction history.
remember_this:
  - ABC-Sampling achieved 95.7% accuracy on imbalanced fraud detection datasets.
  - Transaction amount and location are the most critical features for detecting anomalies.
  - The multi-stage framework maintained 120 ms latency for real-time processing.
  - K-means clustering achieved 92.6% accuracy for legitimate trader classification.
  - The model's performance degrades with 10% missing data or higher noise levels.
```
---

## Paper 26: Cucio & Hennig_summarized.md

**Source File:** `Cucio & Hennig_summarized.md`

```yaml
paper_id: "10.5089/9798400295125.001"
designation: "local"
title: "Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and Complementarity"
authors: "Cucio, M.; Hennig, T."
year: 2025
venue: "IMF Working Paper"
odin_topics:
  - "1.A"
  - "1.B"
  - "1.C"
  - "2.A"
  - "2.D"
  - "4.A"
  - "4.B"
  - "6.A"
  - "8.A"
  - "9.A"
  - "10.A"
tldr: "One-third of Philippine workers are highly exposed to AI, with 61% of those in high-complementarity roles suggesting augmentation rather than displacement."
problem_and_motivation: "Rapid AI advancements may significantly transform labor markets, but the specific impact on the Philippine workforce, particularly its large BPO sector, remains underexplored. Understanding this impact is crucial for informing policy to harness benefits and mitigate job displacement."
approach:
  - "Merged AI exposure (Felten et al., 2021) and complementarity (Pizzinelli et al., 2023) scores with microdata from the Philippine Statistics Authority's October 2022 Labor Force Survey (183,602 observations)."
  - "Classified occupations into high exposure/high complementarity, high exposure/low complementarity, and low exposure categories based on median scores."
  - "Analyzed correlations between AI exposure/complementarity and demographic indicators like age, gender, education, wage, and sector."
  - "Compared Philippine results to other Asian economies using ILO employment data for a regional context."
  - "Assessed AI preparedness using the AI Preparedness Index (AIPI) covering digital infrastructure, human capital, innovation, and regulation."
findings:
  - "num: 36% of the Philippine workforce is highly exposed to AI."
  - "num: Of the highly exposed workers, 61% (22% of total workforce) are in high-complementarity roles, indicating potential augmentation."
  - "num: 39% of highly exposed workers (14% of total workforce) are in low-complementarity jobs, at risk of displacement."
  - "College-educated, young, urban, female, and well-paid service sector workers are most exposed to AI."
  - "The BPO sector has the highest proportion of jobs at risk (73% high exposure/low complementarity), though it represents only 3% of total employment."
  - "Government workers are the most exposed class of worker, driven by clerical roles."
  - "The Philippines scores well on human capital but lags in digital infrastructure compared to regional peers."
  - "The government has introduced a National AI Strategy Roadmap and pending legislation, but a comprehensive legal framework is lacking."
key_figures_tables:
  - "Figure 1: Philippine labor force summary statistics → Sets demographic context for AI exposure analysis."
  - "Figure 6: Exposure and complementarity across occupations → Visualizes how different occupational groups are categorized."
  - "Figure 8: Exposure and complementarity by demographic factors → Shows AI exposure correlates with gender, education, and wage."
  - "Table 2: AI exposure and complementarity in the Philippines → Provides key percentages for each category."
  - "Figure 9: AI preparedness across Asia → Indicates Philippines lags in digital infrastructure."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "AIOE"
    definition: "AI Occupational Exposure, a measure of overlap between AI capabilities and occupational tasks."
  - term: "Complementarity"
    definition: "The extent to which AI augments rather than replaces human labor in an occupation."
  - term: "BPO"
    definition: "Business Process Outsourcing, a key service sector in the Philippines."
  - term: "AIPI"
    definition: "AI Preparedness Index, a composite measure of a country's readiness for AI adoption."
critical_citations:
  - "[Felten et al., 2021] — Developed the AI exposure index used in this analysis."
  - "[Pizzinelli et al., 2023] — Developed the complementarity score used in this analysis."
  - "[Cazzaniga et al., 2024] — Provided the methodological framework and AI Preparedness Index."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "high"
      justification: "Analysis specifically examines Filipino workforce by age, education, and sector."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "medium"
      justification: "Discusses wage inequality and BPO sector dynamics relevant to financial structure."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "contextual"
      justification: "Provides labor market context that informs financial behavior, but does not directly study it."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "contextual"
      justification: "Focus on Filipino BPO and service sectors, but not on specific financial practices."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "contextual"
      justification: "Analysis of BPO sector exposure provides context for spending cycles, but is not the focus."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "low"
      justification: "Tangentially mentions digital infrastructure but does not review PFMS."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "low"
      justification: "Identifies gaps in digital infrastructure and skills, relevant to PFMS design but not directly."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses forecasting of AI impact on employment, analogous to forecasting spending."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "low"
      justification: "Mentions bias and errors in AI, relevant to anomaly detection but not central."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "low"
      justification: "Discusses digital infrastructure gaps, a prerequisite for mobile-first design."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "low"
      justification: "Mentions AI regulation and data privacy as a gap, but does not analyze PFMS data privacy."
  contribution: "This paper provides a granular, data-driven mapping of AI exposure and complementarity across the Philippine labor force, quantifying that 36% of workers are highly exposed, with 14% at displacement risk. It uniquely identifies the BPO sector as most vulnerable (73% high risk), despite its small workforce share, highlighting macro-critical spillover risks. The study correlates exposure with demographic factors (e.g., college-educated, female, young workers are most exposed), which can inform targeted policy interventions. By linking occupational AI scores with local LFS microdata and assessing AI preparedness (noting digital infrastructure gaps), the findings directly justify Odin's need for robust digital infrastructure and user-centric design."
  directly_justifies:
    - "College-educated and young service sector workers are most exposed to AI, indicating a need for financial tools tailored to this demographic."
    - "The BPO sector's high displacement risk (73% of its workers) underscores the importance of financial resilience features for affected users."
    - "Gaps in digital infrastructure suggest that Odin's mobile-first design must be robust and work under connectivity constraints."
    - "AI preparedness gaps in regulation and ethics support Odin's focus on data privacy and user trust."
    - "The potential for AI to augment high-complementarity jobs (22% of workforce) justifies Odin's predictive modeling to enhance user productivity."
  limits:
    - "The analysis is static and does not account for workforce retraining or new job creation over the medium term."
    - "Assumes task content of occupations in the Philippines is identical to the U.S. O*NET database, potentially underestimating exposure."
    - "AIPI does not capture all relevant dimensions for AI adoption, such as the importance of the BPO sector."
  mapping_rationale: "A systematic scan across all 12 functional domains was performed. The paper was flagged as highly relevant to the Filipino Demographics domain (1.A, 1.B) because it provides a detailed socio-economic breakdown of the Filipino workforce by age, education, and sector, directly informing the target user profile for Odin. It was also highly relevant to Predictive Modeling (6.A) and Behavioral Profiling (5.A, 5.B), as it presents a methodology for classifying workers into risk categories based on a combination of metrics (exposure and complementarity), analogous to classifying users by financial behavior. The paper's detailed analysis of the BPO sector and its vulnerability was considered a borderline case for Existing Systems (4.A) and Spending Cycles (2.D), but relevance was rated as low/contextual because the paper does not review specific PFMS software or spending patterns. Domains like Budget Recommendation (7.A-D) and Savings/Debt Management (13.A-C) were considered and rejected as the paper does not address financial allocation or goal management. The analysis of AI regulation and infrastructure gaps was deemed contextual for Data Privacy (10.A) and Mobile-First Design (9.A). Overall, the paper is highly relevant to Odin's understanding of its user base and the economic pressures that drive financial behavior, providing a strong justification for a predictive, user-centric financial management system."
limitations:
  - "Static analysis does not capture future workforce adaptation or job creation. [unacknowledged]"
  - "Relies on U.S. O*NET data, which may not perfectly reflect task content in Philippine occupations."
  - "Does not quantify the magnitude of potential productivity gains or wage effects."
  - "Does not account for spillover effects from BPO sector changes to the broader economy."
  - "AI Preparedness Index may not capture all relevant dimensions for Philippines-specific adoption."
remember_this:
  - "One-third of Philippine workers are highly exposed to AI."
  - "14% of the workforce is in low-complementarity roles at displacement risk."
  - "BPO workers are most at risk, with 73% in high-exposure, low-complementarity jobs."
  - "College-educated, young, and female service workers are most exposed but also most complementary."
  - "Philippines lags in digital infrastructure, a key barrier to AI adoption."
```
---

## Paper 27: Zhong_summarized.md

**Source File:** `Zhong_summarized.md`

```yaml
paper_id: "10.1145/3776759.3776850"
designation: "international-algorithm-specific"
title: "Adaptive Anomaly Detection Threshold for Financial Data Quality Monitoring Based on Time Series Features"
authors: "Zhong, M."
year: 2025
venue: "International Symposium on Artificial Intelligence and Computational Social Sciences (AICSS2025)"
odin_topics:
  - "8.A"
  - "8.B"
  - "8.C"
  - "4.B"
  - "12.A"
  - "12.B"
tldr: "An adaptive anomaly detection threshold framework using sliding window statistics and ensemble unsupervised learning reduces false positives by 46.5% while maintaining real-time processing."
problem_and_motivation: "Static threshold-based anomaly detection systems fail to adapt to distributional shifts in financial data, leading to high false positives and missed detections. The challenge is to distinguish natural changes from genuine anomalies while maintaining operational efficiency. There is a need for adaptive threshold management that can automatically adjust based on evolving data characteristics."
approach:
  - "The framework uses sliding window statistical analysis with Bayesian changepoint detection to identify significant pattern shifts."
  - "Ensemble unsupervised learning combines Isolation Forest, DBSCAN, and Local Outlier Factor for robust anomaly scoring."
  - "Seasonal decomposition and trend analysis capture temporal dependencies in transaction data."
  - "Dynamic threshold adjustment uses exponential decay based on mean, standard deviation, sensitivity, and decay factors."
  - "Adaptive DBSCAN epsilon parameter adjusts to local data density using k-nearest neighbor distances."
  - "Ensemble weights are dynamically updated based on recent AUC-ROC performance of each algorithm."
  - "Evaluation on synthetic financial datasets compares against fixed threshold and statistical ML-based adaptive methods."
findings:
  - "num: Precision of 0.847, recall of 0.891, and F1-score of 0.868 were achieved."
  - "num: False positive rates were reduced by 46.5% compared to fixed threshold approaches."
  - "The adaptive framework outperformed statistical and ML-based adaptive methods with statistical significance (p<0.001)."
  - "Processing time remained suitable for real-time applications at 21.5 ms per 1000 transactions."
  - "The framework maintained stable detection accuracy across different customer segments and transaction types."
key_figures_tables:
  - "Figure 1: Time series feature extraction pipeline architecture → illustrates the multi-stream processing for temporal, statistical, and frequency features."
  - "Figure 2: Multidimensional performance evaluation framework → shows detection accuracy, computational efficiency, and robustness metrics."
  - "Figure 3: Algorithm performance comparison across multiple dimensions → demonstrates superior precision, recall, and F1-score over baselines."
  - "Table 1: Adaptive threshold algorithm parameters → lists window size, sensitivity, decay, and changepoint threshold with ranges."
  - "Table 2: Unsupervised learning algorithm configuration → details key parameters and optimization methods for each algorithm."
  - "Table 3: Dataset characteristics and statistics → provides transaction counts, anomaly rates, and temporal spans for training, validation, and test sets."
  - "Table 4: Comparative analysis results summary → shows precision, recall, F1, FPR, and processing time for all methods."
key_equations:
  - equation: '\tau(t) = \mu(t) + \alpha \times \sigma(t) \times \beta^{(t-t_0)}'
    explanation: "Adaptive threshold based on mean, std, sensitivity, and decay."
  - equation: 'S(x) = \sum_{j=1}^{M} w_j s_j(x)'
    explanation: "Ensemble anomaly score as weighted sum of individual algorithm scores."
  - equation: 'w_j(t) = AUC\_ROC_j(t) / \sum_{k=1}^{M} AUC\_ROC_k(t)'
    explanation: "Dynamic weight based on recent performance of each algorithm."
definitions:
  - term: "Sliding window"
    definition: "A moving subset of recent observations used for local statistical analysis."
  - term: "Bayesian changepoint detection"
    definition: "Statistical method to detect abrupt changes in time series patterns."
  - term: "Isolation Forest"
    definition: "An unsupervised algorithm that isolates anomalies by random partitioning."
  - term: "DBSCAN"
    definition: "Density-based spatial clustering algorithm for identifying clusters and outliers."
  - term: "Local Outlier Factor (LOF)"
    definition: "An algorithm that measures local deviation of a point relative to neighbors."
  - term: "False Positive Rate (FPR)"
    definition: "Proportion of normal transactions incorrectly flagged as anomalies."
  - term: "AUC-ROC"
    definition: "Area under the receiver operating characteristic curve, a performance metric."
critical_citations:
  - "[Iqbal et al., 2024] — Foundational for deep ensemble methods in time series anomaly detection."
  - "[Asmar and Aqel, 2023] — Provides perspective on credit card anomaly detection processes."
  - "[Liu, 2025] — Discusses multi-variable time-series anomaly detection for intelligent operations."
relevance:
  topics:
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Directly addresses anomaly detection in financial transaction data."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Proposes ensemble unsupervised algorithms for anomaly scoring."
    - code: "8.C"
      name: "Cold‑Start Baseline Strategies for Anomaly Detection"
      relevance: "medium"
      justification: "Framework operates with only normal data initially, addressing cold-start."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Explicitly critiques static threshold limitations and proposes adaptive solution."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides comprehensive performance evaluation with multiple metrics."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Evaluates individual unsupervised algorithms and ensemble performance."
  contribution: "This paper provides a robust anomaly detection module for Odin by offering an adaptive threshold mechanism that automatically adjusts to evolving spending patterns. The ensemble unsupervised learning approach can be integrated into Odin's anomaly scoring pipeline to improve detection accuracy. The dynamic weight updating based on recent performance ensures the system remains responsive to changing user behavior. The framework's computational efficiency supports real-time anomaly detection on mobile devices, aligning with Odin's mobile-first design."
  directly_justifies:
    - "Static thresholds lead to high false positives in dynamic financial data."
    - "Ensemble unsupervised learning improves anomaly scoring robustness."
    - "Adaptive thresholds reduce false positive rates by 46.5%."
    - "Bayesian changepoint detection can identify significant pattern shifts."
    - "Seasonal decomposition helps distinguish legitimate seasonal variations from anomalies."
  limits:
    - "The evaluation is conducted on synthetic data, not validated on real-world financial transaction streams."
    - "The framework may struggle with unprecedented market conditions or regulatory changes that deviate from historical patterns."
    - "The approach does not incorporate external economic indicators or social media sentiment."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The Anomaly Detection domain (8.A, 8.B) was flagged as highly relevant because the paper's core contribution is an adaptive anomaly detection framework for financial data. The Cold-Start Baseline (8.C) was considered medium relevance because the method operates with only normal data initially, addressing a cold-start scenario. The Existing Systems & Gaps domain (4.B) was flagged medium as the paper explicitly critiques static thresholds. The System Evaluation domain (12.A, 12.B) was assigned medium because the paper provides comprehensive evaluation metrics and comparisons. Domains such as Filipino Cultural Context, Expense Categorization, Behavioral Profiling, Spending Forecasting, Budget Recommendation, Mobile-First Design, Data Privacy, User Retention, Savings & Debt Management were considered and rejected as the paper does not address these areas. The overall relevance is high for Odin's anomaly detection module, providing algorithmic and evaluation insights."
limitations:
  - "The framework is evaluated only on synthetic data, limiting generalizability to real-world systems. [unacknowledged]"
  - "It may not handle unprecedented market conditions or novel anomaly types not represented in training. [unacknowledged]"
  - "Computational overhead may increase with larger sliding windows, though processing time remains acceptable."
  - "The framework does not incorporate external economic indicators or cross-institutional data for context."
remember_this:
  - "Adaptive thresholds reduce false positive rates by 46.5% over static methods."
  - "Ensemble of Isolation Forest, DBSCAN, and LOF improves anomaly scoring robustness."
  - "Sliding window statistics with Bayesian changepoint detection enable dynamic threshold adjustment."
  - "The framework maintains real-time processing with 21.5 ms per 1000 transactions."
```
---

## Paper 28: Oyeyemi et al_summarized.md

**Source File:** `Oyeyemi et al_summarized.md`

```yaml
paper_id: 10.37502/IJSMR.2025.81004
designation: international
title: From Borrowing to Building: A Systematic Literature Review of Data-Driven Strategies for Cultivating Better Money Habits through Consumer Credit
authors: Oyeyemi, D. O.; Moussa, A. H.; Abioye, V. O.
year: 2025
venue: International Journal of Scientific and Management Research
odin_topics:
  - 1.C
  - 2.B
  - 2.D
  - 4.A
  - 5.A
  - 5.B
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 9.B
  - 10.A
  - 10.B
  - 11.A
  - 12.A
  - 12.B
  - 13.A
  - 13.B
tldr: A systematic literature review synthesizes how alternative data, machine learning, and behavioral insights are integrated into credit systems to foster healthier money habits.
problem_and_motivation: Consumer credit has evolved into data-driven platforms that both enable and influence financial behavior, yet a comprehensive synthesis of how these strategies cultivate positive money habits is lacking. Understanding the mechanisms through which data-driven interventions promote responsible credit usage and financial literacy is essential for designing equitable and effective financial systems.
approach:
  - The review followed a systematic methodology with structured searches across Scopus, Web of Science, IEEE Xplore, and Google Scholar.
  - Keywords encompassed terms related to data-driven credit, behavioral economics, machine learning, alternative data, and financial literacy.
  - Studies were included if they were peer-reviewed and directly addressed the application of data analytics or machine learning in consumer credit and its impact on behavior.
  - Data extraction employed a standardized protocol, capturing study objectives, methodologies, data sources, analytical techniques, and findings.
  - The synthesis was thematic, categorizing findings across recurring concepts, and included a quality assessment for methodological rigor and bias.
findings:
  - num: Ensemble models like XGBoost consistently outperform traditional logistic regression in credit classification tasks.
  - Alternative data sources, including mobile phone usage, social media activity, and utility payments, significantly expand financial inclusion for underserved populations.
  - Higher financial literacy correlates with improved investment intentions and more judicious credit utilization across various financial products.
  - The "statement effect" demonstrates that the timing and visibility of financial information can temporarily reduce spending or increase payment activity.
  - Behavioral nudges and personalized feedback loops demonstrate stronger short-term behavioral impacts than mandatory disclosures alone.
  - Financial incentives alone show limited sustained impact on long-term behavior change once the incentive is removed.
  - Data-driven interventions raise pressing concerns about data privacy, algorithmic bias, and the ethical use of consumer information.
  - The interaction between personality traits (conscientiousness, impulsivity), self-control, and demographics shapes borrowing, repayment, and saving decisions.
key_figures_tables:
  - "Figure 1: Timeline of consumer credit evolution from traditional banking to AI-driven adaptive platforms → Credit systems have grown more inclusive but also more complex."
  - "Figure 2: Conceptual model linking personality, self-control, financial literacy, and demographics to credit behaviors → Psychological traits strongly influence borrowing and repayment choices."
  - "Figure 3: Framework from alternative data to machine learning, personalized decisions, feedback, and habit formation → Data-driven interventions require iterative feedback loops to embed habits."
  - "Figure 4: Adaptive cycle of consumer actions, data capture, ML analysis, personalized feedback, and behavior adjustment → Continuous feedback is central to reinforcing positive money habits."
  - "Table 1: Comparative overview of alternative data types (social, behavioral, transactional) with advantages and risks → Transactional data offers the most reliable repayment predictions."
  - "Table 2: Key behavioral and demographic factors influencing credit use → High conscientiousness and self-control correlate with responsible repayment."
  - "Table 3: Comparison of statistical and ML models in credit risk evaluation → Ensemble models like XGBoost achieve the highest predictive accuracy at the cost of transparency."
  - "Table 4: Comparative effectiveness of data-driven interventions → Feedback loops show high engagement and promise for habit formation, while incentives lose effect once removed."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Alternative data
    definition: Non-traditional data sources for credit assessment, including social media activity, mobile phone usage, utility payments, and e-commerce transactions.
  - term: Financial literacy
    definition: The knowledge and understanding of financial concepts, instruments, and risks that enables informed financial decisions.
  - term: Mental accounting
    definition: A behavioral economics concept describing how individuals categorize and evaluate financial transactions differently based on subjective frames.
  - term: Statement effect
    definition: A temporary behavioral adjustment, such as reduced spending or increased payment activity, triggered by the receipt of a credit card statement.
critical_citations:
  - "[Nwaimo et al., 2024] — Predictive analytics expands credit access for underbanked populations."
  - "[Widagdo & Roz, 2022] — Personality, literacy, and behavior shape investment intentions."
  - "[Zhao et al., 2022] — Demographics and digital credit reliance drive online consumer credit behavior."
  - "[Suhadolnik et al., 2023] — ML improves credit risk assessment empirically."
  - "[Hershfield et al., 2015] — Psychological insights encourage responsible consumer debt use."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: "Reviews behavioral drivers like self-control and personality that shape financial behavior."
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: low
      justification: "Mentions cyclical spending tied to credit card statements ('statement effect'), but not seasonal patterns."
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: "Addresses cyclical spending behavior generally, not Filipino-specific occasions."
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: "Provides an overview of digital lending platforms and credit assessment innovations."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: "Explicitly links personality traits, self-control, and financial literacy to distinct credit usage patterns."
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: "Addresses behavioral dynamics and how profiles evolve with feedback, indirectly relevant to cold-start."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: "Reviews machine learning models, including XGBoost, for predicting credit risk and behavior."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: "Discusses ML algorithms for predicting behavior based on sequential transactional data."
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: "Discusses how feedback and financial literacy support budgeting and spending management."
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: "Reviews how personalized feedback and nudges can guide spending decisions."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: "Addresses predictive models for credit risk, not explicitly anomaly detection in spending."
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: "Mentions machine learning for spending pattern analysis, not specifically anomaly detection."
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: "Discusses digital lending platforms and mobile app interactions influencing financial behavior."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: "Dedicated sections on regulatory challenges, ethical data use, and privacy concerns with alternative data."
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: "Discusses transparency and ethical data use as prerequisites for building consumer trust."
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: "Reviews how personalized feedback mechanisms drive user engagement and financial learning."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: "Employs a systematic literature review methodology and quality assessment for evaluating interventions."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: "Compares performance of various ML algorithms for credit risk evaluation, including XGBoost."
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: "Mentions savings as an outcome of responsible credit behavior, but not goal management."
    - code: 13.B
      name: Debt Management in PFMS
      relevance: medium
      justification: "Discusses credit management practices and strategies to prevent over-indebtedness."
  contribution: "The systematic review provides a consolidated evidence base for integrating behavioral economics principles into Odin's financial behavioral profiling module. The comparative analysis of machine learning algorithms directly supports the selection of XGBoost for Odin's spending forecast engine. The synthesis of alternative data sources and their ethical implications informs Odin's data privacy and user trust framework. The review's discussion of feedback mechanisms and information design offers guidance for Odin's mobile UX and engagement strategies. Its identification of research gaps around long-term behavioral impacts justifies Odin's emphasis on continuous user feedback and adaptive personalization."
  directly_justifies:
    - "Ensemble machine learning models like XGBoost outperform traditional methods in predictive accuracy for financial behavior classification."
    - "Alternative data sources can expand credit access but raise significant data privacy and algorithmic bias concerns."
    - "Personalized feedback loops and transparent AI systems are the most promising avenues for sustainable financial habit formation."
    - "Self-control and financial literacy are critical determinants of responsible credit usage and repayment behavior."
    - "Behavioral nudges show stronger short-term impacts than mandatory disclosures, but financial incentives alone do not drive lasting change."
  limits:
    - "The review does not conduct primary empirical research; findings are synthesized from secondary sources."
    - "Limited longitudinal studies assessing long-term behavioral impact of data-driven interventions beyond repayment rates."
    - "The review does not propose or evaluate a specific system architecture or implementation for habit cultivation."
    - "Generalizability of findings to the Philippine context is not directly established, as the review does not focus on Filipino-specific data or institutions."
    - "The review's quality assessment of included studies is not detailed in terms of specific scoring or weighting of evidence."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was conducted for this review paper. The domains flagged as relevant include: Behavioral Profiling & Classification (5.A, 5.B, 5.C) – high relevance due to the paper's explicit focus on personality traits, self-control, and financial literacy as correlates of credit behavior; Spending Forecasting (6.A, 6.B) – high relevance for its comparative analysis of machine learning algorithms (e.g., XGBoost) for credit risk prediction; Budget Recommendation (7.A, 7.B, 7.C, 7.D) – medium relevance, as the paper discusses behavioral nudges and personalized feedback to guide spending, but does not cover constrained optimization or infeasibility handling; Data Privacy & User Trust (10.A, 10.B) – high relevance, with dedicated sections on regulatory challenges, ethical data use, and privacy concerns; User Retention & Engagement (11.A, 11.B) – medium relevance, for its review of feedback mechanisms and digital platforms; and System Evaluation (12.A, 12.B, 12.C) – medium to high relevance, given the systematic review methodology and performance comparisons of ML models. Domains such as Filipino Cultural Context (2.A, 2.B, 2.C, 2.D) are only contextually relevant, as the paper addresses general cyclical spending but not Filipino-specific cultural practices. Existing Systems & Gaps (4.A, 4.B) is moderately relevant for its landscape overview. Anomaly Detection (8.A, 8.B, 8.C) received low relevance because the paper focuses on prediction and classification, not explicit anomaly detection. Mobile-First Design (9.A, 9.B) is contextually relevant through its discussion of digital lending platforms. Savings & Debt Management (13.A, 13.B, 13.C) is relevant at a medium level for its discussion of credit management practices. Overall, the paper is highly relevant to Odin's core algorithmic and behavioral modules, serving as a foundational reference for integrating ML with behavioral insights in personal finance management."
limitations:
  - "The review does not conduct primary empirical research; findings are synthesized from secondary sources."
  - "Limited longitudinal studies assessing long-term behavioral impact of data-driven interventions beyond repayment rates."
  - "The review does not propose or evaluate a specific system architecture or implementation for habit cultivation."
  - "Generalizability of findings to the Philippine context is not directly established, as the review does not focus on Filipino-specific data or institutions."
  - "The review's quality assessment of included studies is not detailed in terms of specific scoring or weighting of evidence. [unacknowledged]"
remember_this:
  - "XGBoost outperforms logistic regression in predicting credit risk and financial behavior."
  - "Alternative data expands financial inclusion but raises significant privacy and bias concerns."
  - "Self-control and financial literacy are key predictors of responsible financial behavior."
  - "Personalized feedback loops are promising for building sustainable financial habits."
  - "Financial incentives alone do not produce lasting behavioral change once removed."
```
---

## Paper 29: Eliades & Papadopoulos_summarized.md

**Source File:** `Eliades & Papadopoulos_summarized.md`

```yaml
paper_id: "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
designation: "international-algorithm-specific"
title: "A Conformal Martingales Approach for Recurrent Concept Drift"
authors: "Eliades, C.; Papadopoulos, H."
year: 2025
venue: "Proceedings of Machine Learning Research"
odin_topics:
  - "2.B"
  - "4.A"
  - "4.B"
  - "6.A"
  - "6.B"
  - "7.D"
  - "8.A"
  - "8.B"
tldr: "Extends Inductive Conformal Martingales to reuse past models upon detecting recurrent concept drift, cutting retraining events by up to 94% with <3 percentage points accuracy loss."
problem_and_motivation: "Recurrent concept drift, where past data distributions reappear, is common but existing methods retrain models unnecessarily. This wastes computational resources and data, especially in seasonal or cyclic domains. A method that explicitly detects recurrence and reuses suitable models is needed."
approach:
  - "Uses Inductive Conformal Martingales (ICM) with a Cautious betting function to detect exchangeability violations indicating drift."
  - "Maintains a pool of classifiers trained on previously seen concepts."
  - "Upon drift detection, tests each stored model's exchangeability against a recent data window."
  - "Selects a model if it passes the exchangeability test and its F1 score on new data remains within a historical performance threshold."
  - "Trains a new model only when no stored model meets both criteria."
  - "Evaluated on synthetic STAGGER and real-world Airlines and ELEC datasets."
  - "Compares against Accuracy Weighted Ensemble (AWE) and Dynamic Weighted Majority (DWM) benchmarks."
findings:
  - "num: Pool ICM reduced retraining events by up to 94% on the STAGGER dataset."
  - "num: Wasted training instances were reduced by 22% to 33% across all datasets."
  - "num: Accuracy loss was limited to less than 3 percentage points compared to always retraining."
  - "The Cautious betting function (epsilon=100) improved drift detection speed and accuracy on datasets with long-duration concepts."
  - "Pool ICM maintained competitive accuracy while significantly lowering computational cost."
key_figures_tables:
  - "Table 1: Performance metrics (Accuracy, Delay, Alarms, Models) for Pool ICM on all datasets → Shows consistent reduction in models trained."
  - "Table 2: Accuracy comparison with Standard ICM, AWE, and DWM-NB → Pool ICM trades minimal accuracy for large efficiency gains."
key_equations:
  - equation: "p_j = (|{α_i ∈ H_j | α_i > α_j}| + U_j · |{α_i ∈ H_j | α_i = α_j}|) / (j - k)"
    explanation: "Computes p-value for exchangeability testing of a new example."
  - equation: "S_n = ∏_{i=1}^{n} f_i(p_i)"
    explanation: "Martingale value updated multiplicatively from p-values."
  - equation: "Relative Gain (%) = ((K - L)(NoDr - NoM) / (K · NoDr)) × 100"
    explanation: "Estimates prediction-instance savings from model reuse."
definitions:
  - term: "ICM"
    definition: "Inductive Conformal Martingales; a computationally efficient version of Conformal Martingales for testing exchangeability."
  - term: "RCD"
    definition: "Recurrent Concept Drift; when previously seen data distributions reappear over time."
  - term: "NCM"
    definition: "Nonconformity Measure; a function assigning a numerical score indicating how unusual an example is."
  - term: "EA"
    definition: "Exchangeability Assumption; the condition that the joint distribution of data is invariant under permutation."
critical_citations:
  - "[Lu et al., 2019] — Comprehensive survey framing concept drift taxonomies."
  - "[Suárez-Cetrulo et al., 2023] — Categorizes RCD approaches into supervised, meta, and unsupervised."
  - "[Vovk et al., 2003] — Foundational work on conformal prediction and martingales."
relevance:
  topics:
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "medium"
      justification: "Motivates RCD with examples like electricity consumption and user-behavior cycles."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Provides a general algorithmic approach to handling data distribution shifts applicable to PFMS."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Directly addresses the inefficiency of retraining models from scratch upon drift."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Proposes a method for maintaining predictive model accuracy under changing spending patterns."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Introduces Pool ICM as a forecasting-adjacent algorithm for sequential data with recurrent drifts."
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "medium"
      justification: "Model reuse strategy can be seen as handling infeasibility of a single model by reducing to past solutions."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "ICM detects exchangeability violations, analogous to detecting anomalies in data distribution."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "The conformal martingale framework is a non-parametric algorithm for detecting distributional anomalies."
  contribution: "Pool ICM's model reuse mechanism can reduce retraining costs for Odin's spending forecasting module when user spending patterns recur. The exchangeability test provides a statistically grounded way to detect when a user's behavior has shifted to a previously seen state. The F1-score criterion ensures that the reused model maintains acceptable predictive performance on current data. This directly supports Odin's goal of being computationally efficient and responsive to user behavior changes."
  directly_justifies:
    - "Retraining every time a drift is detected is computationally wasteful for recurrent patterns."
    - "A model can be reused if its data window is exchangeable with the training window and its F1 score is stable."
    - "Pool ICM reduces the number of models trained, saving up to 94% of retraining events."
  limits:
    - "Requires labeled data for drift detection and model evaluation."
    - "Accuracy is slightly lower than state-of-the-art methods focused solely on prediction."
    - "Performance may degrade with very short concept durations, as seen on ELEC with epsilon=100."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to the 'Existing Systems & Gaps' (4.A, 4.B), 'Spending Forecasting' (6.A, 6.B), and 'Anomaly Detection' (8.A, 8.B) domains because it directly proposes an algorithmic solution to the problem of model obsolescence and data distribution changes, which are core challenges in adaptive PFMS. It was deemed medium relevance to 'Filipino Cultural Context' (2.B) as its motivation includes seasonal and cyclic patterns, which are pertinent to Filipino spending occasions, but the paper does not use Filipino data. It also has medium relevance to 'Budget Recommendation' (7.D) as the strategy of model reuse can be interpreted as a form of handling infeasibility by reducing to past solutions. Topics related to 'User Trust' (10.A, 10.B), 'Mobile Design' (9.A, 9.B), and 'User Retention' (11.A, 11.B) were considered but rejected as the paper does not address these areas. The paper's overall relevance to Odin is moderate to high, providing a statistically principled and efficient approach to adapting predictive models over time, which is critical for a PFMS that must handle evolving user financial behavior."
limitations:
  - "Requires labeled data, which may not always be available in real-time PFMS settings."
  - "F1-score threshold is heuristic and may need tuning per user or domain."
  - "Accuracy trade-off is not quantified per user segment or spending category. [unacknowledged]"
  - "Does not address the cold-start problem or initial model training. [unacknowledged]"
remember_this:
  - "Pool ICM cut retraining events by 94% on synthetic data."
  - "Reduced training instances by 22% to 33% across all benchmarks."
  - "Accuracy loss was under 3 percentage points compared to full retraining."
  - "Uses exchangeability testing to decide if a past model is still valid."
  - "Reuses models only if their F1 score on recent data remains stable."
```
---

## Paper 30: Elliyana et al_summarized.md

**Source File:** `Elliyana et al_summarized.md`

```yaml
paper_id: 10.1234/wjebm.2025.2.6.1
designation: international
title: A Systematic Literature Review on Personal Financial Management Practices: Budgeting, Investment, Debt, and Saving
authors: Elliyana, E.; Maricar, R.; Toalib, R.
year: 2025
venue: World Journal of Economics, Business and Management
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 7.A
  - 7.B
  - 8.A
  - 9.A
  - 9.B
  - 10.A
  - 11.A
  - 12.A
  - 13.A
tldr: Financial literacy drives budgeting, saving, investing, and debt management, but digital tools and behavioral factors moderate its effectiveness.
problem_and_motivation: Personal financial management practices directly influence individual well-being, yet existing studies cover discrete dimensions without an integrated synthesis. A unified understanding of budgeting, saving, investing, and debt management is critically needed in the post-pandemic, digitalized context.
approach:
  - Systematic literature review followed PRISMA 2020 protocol.
  - Searched Scopus, Web of Science, Google Scholar, MDPI, and DOAJ for studies from 2018-2024.
  - Retrieved 2,342 records, removed 742 duplicates, screened 1,600 titles and abstracts, assessed 452 full texts.
  - Final sample comprised 47 peer-reviewed, open-access articles after applying exclusion criteria.
  - Quality appraisal used MMAT 2018; thematic synthesis organized findings by four PFM behaviors and cross-cutting factors.
findings:
  - "num: Financial education programs explain 26% of the variance in saving behavior."
  - "num: Only 44% of U.S. adults have sufficient savings for a $1,000 emergency expense."
  - Financial literacy correlates with improved budgeting, saving discipline, informed investment, and reduced debt reliance.
  - Digital financial tools enhance participation but risk amplifying vulnerabilities when literacy is low.
  - Behavioral biases like present bias and optimism hinder optimal financial decision-making.
  - Self-efficacy and early financial socialization are strong predictors of long-term saving habits.
  - Fintech platforms democratize investing but expose novice investors to speculation and financial loss.
key_figures_tables:
  - "Table 1: Summary of 47 studies on PFM practices → Financial literacy is the most consistent determinant across behaviors."
  - "Figure 1: PRISMA flow diagram → 47 studies were included after systematic screening."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "PFM"
    definition: "Personal Financial Management encompasses budgeting, saving, investing, and debt handling."
  - term: "PRISMA"
    definition: "Preferred Reporting Items for Systematic Reviews and Meta-Analyses, a protocol for systematic review reporting."
  - term: "BNPL"
    definition: "Buy Now, Pay Later, a digital credit service allowing deferred payments."
  - term: "fintech"
    definition: "Financial technology that provides digital tools for financial services."
  - term: "MMAT"
    definition: "Mixed Methods Appraisal Tool, used for quality appraisal of studies."
critical_citations:
  - "[Lusardi & Mitchell, 2020] — Foundational link between literacy and retirement planning."
  - "[Shim, Serido, & Tang, 2019] — Key evidence on financial socialization and saving."
  - "[OJK, 2022] — Critical Indonesian data on literacy-inclusion gap."
  - "[Bhattacharya et al., 2022] — Core warning on finfluencer-driven speculation."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "contextual"
      justification: "Review covers youth and emerging economy contexts with indirect applicability."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "contextual"
      justification: "Discusses income, debt, and saving patterns relevant to financial structure."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "medium"
      justification: "Provides behavioral patterns like saving and budgeting applicable to this group."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "medium"
      justification: "Budgeting as a foundational behavior informs categorization frameworks."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      relevance: "low"
      justification: "Mentions budgeting but not specific category design."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews fintech apps, budgeting apps, and digital financial tools."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Identifies gaps in longitudinal evidence and digital tool effectiveness."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Discusses self-efficacy, present bias, and peer influence as behavioral drivers."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "low"
      justification: "Does not address cold-start directly but notes early socialization effects."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "contextual"
      justification: "Mentions behavioral mechanisms without classification methodologies."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "low"
      justification: "No predictive modeling; focuses on behavioral synthesis."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "high"
      justification: "Budgeting is identified as the foundational behavior for PFM."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "low"
      justification: "No specific recommendation algorithms discussed."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "low"
      justification: "No anomaly detection focus; general spending patterns mentioned."
    - code: "9.A"
      name: "Mobile‑First Design Principles and Rationale"
      relevance: "medium"
      justification: "Highlights mobile banking and budgeting apps as significant enablers."
    - code: "9.B"
      name: "Mobile UX Design for Personal Finance"
      relevance: "low"
      justification: "Mentions app usage but not specific UX design principles."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "low"
      justification: "No explicit focus on privacy; security implied in fintech context."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "low"
      justification: "Does not analyze engagement metrics."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "contextual"
      justification: "Systematic review methodology is an evaluation framework itself."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "high"
      justification: "Saving behavior is a primary focus, linked to budgeting and digital tools."
  contribution: "This paper validates that financial literacy is the core driver across budgeting, saving, investment, and debt management modules in Odin. It supports the need for integrated PFM features that connect budgeting to saving goals. The review justifies incorporating behavioral self-efficacy and early socialization into user profiling. It provides empirical evidence that digital financial tools must be paired with literacy safeguards. The paper's systematic approach offers a benchmark for Odin's evaluation framework."
  directly_justifies:
    - "Financial literacy significantly correlates with improved saving behavior among youth."
    - "Mobile-based budgeting apps significantly increase financial control among millennials."
    - "Digital financial tools are effective only when users possess a threshold of digital literacy."
    - "Budgeting is a significant predictor of financial well-being across cultures."
    - "Self-efficacy and early financial socialization predict long-term saving habits."
  limits:
    - "The review is based on secondary data from 47 studies, not primary empirical research on Filipino users."
    - "Longitudinal evidence on behavioral change over time is lacking."
    - "Experimental studies comparing digital vs. traditional approaches are scarce."
    - "Regional comparability is limited; Western-centric models dominate."
  mapping_rationale: "All 12 functional domains were systematically scanned. The strongest relevance was found in Behavioral Profiling (5.A, high), Budget Recommendation (7.A, high), and Savings & Debt Management (13.A, high) due to the paper's focus on financial literacy, budgeting, saving, and debt. Medium relevance was assigned to Expense Categorization (3.A) for its budgeting focus, Existing Systems (4.A, 4.B) for reviewing fintech apps, and Mobile-First Design (9.A) for digital tool discussion. Low relevance was assigned to Prediction (6.A), Anomaly Detection (8.A), UX Design (9.B), Privacy (10.A), and Engagement (11.A) due to lack of direct coverage. Contextual relevance was noted for topics like Filipino demographics (1.A, 1.B) and Evaluation Frameworks (12.A) through the review methodology. Borderline cases like seasonal spending (2.B) and culturally specific practices (2.A) were rejected due to absence of data. Overall, the paper provides foundational behavioral insights that inform Odin's design but is not algorithmically specific."
limitations:
  - "Limited primary data on Filipino-specific PFM behaviors."
  - "Cross-sectional nature of most reviewed studies limits causal inference."
  - "Potential publication bias favoring positive results."
  - "Digital finance focus may become outdated rapidly. [unacknowledged]"
remember_this:
  - "Financial literacy is the most consistent driver of PFM behaviors."
  - "Budgeting is the foundational behavior enabling saving and investment."
  - "Digital tools amplify financial behavior but require literacy safeguards."
  - "Self-efficacy and early socialization predict long-term saving success."
  - "Financial education explains 26% of the variance in saving behavior."
```
---

## Paper 31: Nasih & Adam_summarized.md

**Source File:** `Nasih & Adam_summarized.md`

```yaml
paper_id: 3b8e5a1c-8c3d-5791-a3f5-8b2c9d1e4f7a
designation: international
title: How do young people perceive financial literacy, and what role do they believe it plays in their future success?
authors: Nasih, M.; Adam, A. S.
year: 2025
venue: International Journal of Emerging Issues in Management, Accounting and Technology
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.D
  - 4.A
  - 5.A
  - 7.A
  - 7.D
  - 10.A
  - 11.A
  - 12.A
  - 13.B
tldr: Young adults universally recognize financial literacy's importance for future success but exhibit a knowledge-confidence paradox, with family socialization dominating formal education and digital finance creating both opportunities and risks.
problem_and_motivation: While extensive research exists on youth financial knowledge and behavior, systematic evidence on how young people perceive financial literacy and its connection to future success is fragmented, particularly in developing countries. The rapid digital transformation of financial services and recent economic crises have created new dynamics that existing reviews have not adequately addressed.
approach:
  - Systematic literature review following PRISMA 2020 guidelines.
  - Searched seven academic databases (JSTOR, ERIC, Scopus, Google Scholar, OECD iLibrary, World Bank, ProQuest) for studies published 2015-2025.
  - Included 47 empirical studies from 25 countries with over 250,000 participants aged 18-30.
  - Employed two-stage screening with inter-rater reliability (κ=0.82 for abstracts, 0.91 for full-text).
  - Used thematic synthesis (Thomas & Harden, 2008) with subgroup analyses by geographic context, gender, and educational level.
findings:
  - num: 78% of German university students rated their financial knowledge as "good" but only 34% answered basic questions correctly.
  - Family financial discussions correlated with 45% higher financial confidence scores regardless of parents' actual literacy.
  - num: 71% of EU youth felt "paralyzed by too many options" when learning about investments.
  - num: 76% of youth across studies used social media for financial information but expressed skepticism about reliability.
  - num: Youth from high-income families showed "financial cushion confidence"; low-income youth showed heightened awareness with fatalism.
  - num: Young women were 40% more likely to respond "don't know" to financial questions they could answer correctly.
  - num: 85% of participants planned to learn more about investing, but only 15-20% took concrete steps.
  - num: Crisis experiences increased financial literacy awareness scores by 28% in a U.S. longitudinal study.
  - Gender gaps narrowed by 35% when financial tasks were framed as "life planning" rather than "mathematical tests."
  - num: Having one close friend who invests increased an individual's likelihood of opening an investment account by 340%.
key_figures_tables:
  - Table 1: PRISMA flow diagram showing study selection from 1,847 records to 47 included studies.
  - Table 2: Summary of included studies by region and methodology, showing 38% from developing nations and 17% multi-country.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: PFMS
    definition: Personal Finance Management System
  - term: PRISMA
    definition: Preferred Reporting Items for Systematic Reviews and Meta-Analyses
  - term: FOMO
    definition: Fear of missing out
  - term: CASP
    definition: Critical Appraisal Skills Programme
  - term: PICOS
    definition: Population, Intervention, Comparison, Outcomes, Study design
critical_citations:
  - "[Lusardi & Mitchell, 2014] — Foundational theory on financial literacy and economic importance."
  - "[Gudmunson & Danes, 2011] — Core framework for family financial socialization."
  - "[OECD, 2020] — Key international survey on adult financial literacy."
  - "[Shim et al., 2010] — Established role of parents in youth financial socialization."
  - "[Kaiser et al., 2021] — Major meta-analysis on financial education effectiveness."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Systematic review of youth (18-30) financial perceptions directly informs understanding of the target demographic.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Discusses income, debt, and financial challenges relevant to understanding financial structures.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly examines youth financial behavior, including confidence-action gaps and risk-taking.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Reveals cultural variations in financial perceptions, family socialization, and success conceptualizations.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: Mentions cultural factors and family obligations influencing financial behavior, relevant to spending cycles.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews existing financial education systems and their limitations in shaping youth perceptions.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies gaps in formal financial education and the dominance of informal family influences.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Documents awareness-confidence paradox and behavioral intention patterns essential for profiling.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: Mentions how financial shocks trigger learning, relevant to dynamic profile changes.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: low
      justification: Discusses digital tools but not predictive modeling specifically.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Examines youth perceptions of budgeting skills and their importance for financial security.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: contextual
      justification: Mentions how youth feel "paralyzed by too many options" when making financial decisions, relevant to constraint handling.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Not directly addressed; no discussion of anomaly detection.
    - code: 9.A
      name: Mobile‑First Design Principles and Rationale
      relevance: medium
      justification: Digital natives' comfort with financial apps and need for explainable AI are highly relevant to mobile-first design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Discusses youth's trust issues with financial education sources and need for digital literacy.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: Reveals engagement patterns: intention-action gaps, social influence, and crisis-driven behavior changes.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: Findings on gamification and social proof inform retention strategies.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Critiques existing evaluation methods (knowledge vs. perceptions) and suggests new assessment approaches.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: low
      justification: Not directly discussed; no algorithmic evaluation.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: medium
      justification: Discusses youth's emphasis on financial literacy for debt avoidance and security.
    - code: 13.C
      name: End‑of‑Period Surplus as a Savings Input
      relevance: contextual
      justification: Mentions savings goals and family security, indirectly relevant to surplus management.
  contribution: This systematic review provides foundational evidence on youth financial literacy perceptions, directly justifying Odin's user research and behavioral profiling modules. The awareness-confidence paradox informs the design of confidence-building features and personalized financial education. The dominance of family socialization supports Odin's need for social and collaborative features, while the digital dual nature guides UX design for transparency and explainability.
  directly_justifies:
    - "Young adults universally recognize financial literacy's importance but overestimate their competence."
    - "Family financial socialization dominates formal education in shaping youth financial perceptions."
    - "Digital finance creates both opportunities and risks requiring dedicated digital financial literacy."
    - "Structural inequalities along gender, socioeconomic, and geographic lines persist in financial perceptions."
    - "Crisis-driven learning suggests reactive rather than proactive financial capability development."
  limits:
    - "English-language publication bias may underrepresent research from non-English speaking countries."
    - "Heterogeneity of financial literacy definitions and measures complicates synthesis."
    - "Rapid financial innovation may render some findings outdated quickly."
    - "Most studies are cross-sectional, limiting understanding of perception evolution over time."
    - "Limited intervention effectiveness studies with perception outcomes."
  mapping_rationale: The systematic scan across all 12 functional domains and their associated topic codes identified the paper as highly relevant to Odin. The paper directly informs domains like Filipino Cultural Context (themes of family socialization and cultural variation), Existing Systems & Gaps (critique of formal education), Behavioral Profiling (awareness-confidence paradox), and User Retention (engagement patterns). Borderline cases included the paper's relevance to Budget Recommendation (youth perceptions of budgeting importance) and Mobile Design (digital natives' use of financial apps). Domains considered but rejected included Predictive Modeling and Anomaly Detection, as the paper does not discuss algorithmic techniques. The paper offers strong foundational justification for Odin's user-centered design and behavioral insights.
limitations:
  - "English-language publication bias may underrepresent research from non-English speaking countries. [unacknowledged]"
  - "Heterogeneity of financial literacy definitions and measures complicates synthesis. [acknowledged]"
  - "Rapid financial innovation may render some findings outdated quickly. [acknowledged]"
  - "Most studies are cross-sectional, limiting understanding of perception evolution over time. [acknowledged]"
  - "Limited intervention effectiveness studies with perception outcomes. [acknowledged]"
remember_this:
  - "Young adults recognize financial literacy's importance but overestimate their competence."
  - "Family financial socialization dominates formal education in shaping youth financial perceptions."
  - "Digital finance creates both opportunities and risks for youth financial capability."
  - "Structural inequalities along gender and socioeconomic lines persist in financial perceptions."
  - "Only 15-20% of youth who plan to learn about finance actually take concrete steps."
```
---

## Paper 32: Estorba et al_summarized.md

**Source File:** `Estorba et al_summarized.md`

```yaml
paper_id: 10.47772/IJRISS.2025.91200252
designation: local
title: Ka-abag o Babag? Exploring the Lived Experiences in the Context of Financial Well-being of Microfinance Borrowers
authors: Estorba, V. L.; Relativo, J. L. C.; Rellon, S. B. S.; Regis, K. J. M.
year: 2025
venue: International Journal of Research and Innovation in Social Science
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.D
  - 4.A
  - 5.A
  - 5.C
  - 7.A
  - 7.D
  - 10.A
  - 10.B
  - 11.B
  - 13.A
  - 13.B
tldr: Microfinance provides short-term financial relief and promotes discipline but can also perpetuate debt cycles, stress, and psychological strain for female borrowers in the Philippines.
problem_and_motivation: Existing literature relies heavily on quantitative measures of borrower financial well-being, failing to capture the subjective lived experiences and meaning-making of how microfinance impacts financial and psychological health. This gap hinders the development of holistic interventions that address both financial and emotional needs of borrowers.
approach:
  - A transcendental phenomenological qualitative design was used to explore the lived experiences of fifteen female microfinance borrowers in Argao, Cebu.
  - Purposive criterion sampling selected participants with at least three years of borrowing experience and three active loan cycles.
  - Data were collected via semi-structured interviews adapted from the CFPB Financial Well-Being Scale, conducted in Cebuano.
  - Colaizzi's seven-step phenomenological method was used for data analysis.
  - The study is grounded in Lazarus and Folkman's Transactional Model of Stress and Coping and Sen's Capability Approach.
findings:
  - Microfinance has a dual nature, acting as both support and hindrance to financial well-being.
  - Borrowers experienced significant pre-borrowing financial difficulties, including poverty and unstable livelihoods.
  - Microfinance provided immediate resources and improved capabilities but also introduced repayment pressures and psychological strain.
  - Effective coping strategies included budgeting, income diversification, positive thinking, and reliance on faith.
  - num: 47% of Filipino adults maintain outstanding debt, predominantly for daily consumption.
key_figures_tables:
  - Table 1: Financial difficulties before microfinance → Shows poverty as persistent challenge.
  - Table 2: Effects of microfinance → Shows dual impact of relief and burden.
  - Table 3: Coping strategies → Shows adaptive and emotional management techniques.
  - Table 4: Outcomes of debt strategies → Shows transformation and cyclical entrapment.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Ka-abag
    definition: Support or assistance.
  - term: Babag
    definition: Hindrance or obstacle.
  - term: PFMS
    definition: Personal Finance Management System.
critical_citations:
  - "[Lazarus & Folkman, 1984] — Foundational theory for stress and coping."
  - "[Sen, 1999] — Foundational theory for capability and well-being."
  - "[De Silva & Gunawardana, 2023] — Highlights microfinance-induced debt cycles."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Focuses on female borrowers, not specifically young professionals.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: low
      justification: Provides context on financial fragility but not structure.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Details coping and financial management behaviors.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Explores Filipino cultural practices like informal lending.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: high
      justification: Describes how emergencies and family obligations drive spending.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Contextualizes microfinance as an existing system.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Profiles borrowers based on coping and stress responses.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Thematic classification can inform profile development.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Reveals real-world budgeting strategies and constraints.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: medium
      justification: Shows how borrowers prioritize essential needs over loans.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Not directly addressed.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Reveals borrower distrust due to aggressive collection.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: low
      justification: Highlights debt dependency, a retention challenge.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Shows difficulty in saving due to debt.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: Provides direct evidence on debt management challenges.
  contribution: This paper directly informs Odin's development by highlighting the emotional and psychological burden of debt, which is critical for designing empathetic and user-centered PFMS features. It underscores the need for integrated financial literacy and psychosocial support within budgeting tools. The findings on coping mechanisms (budgeting, income diversification) can guide the design of practical, actionable features for users. The dual nature of microfinance as both support and hindrance validates the need for systems that can handle financial volatility and user stress.
  directly_justifies:
    - "Odin should incorporate features that help users manage financial stress."
    - "Budgeting tools must account for irregular income and emergency spending."
    - "Debt management modules should offer flexible repayment planning."
    - "Systems must support users in distinguishing between survival and investment spending."
    - "User trust is eroded by aggressive collection practices, informing UX design."
  limits:
    - "The study is geographically bounded to Argao, Cebu, limiting generalizability."
    - "The sample consists exclusively of women, excluding male perspectives."
    - "Self-reported narratives may be subject to social desirability bias."
    - "The cross-sectional design cannot capture long-term financial trajectories."
    - "Excludes perspectives of microfinance officers and institutional representatives."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was conducted. The paper's primary relevance falls under Behavioral Profiling (5.A, 5.C), Savings & Debt Management (13.B), and Filipino Cultural Context (2.A, 2.D), rated high due to direct qualitative evidence on borrower psychology and culturally embedded practices like informal lending and family obligations. Medium relevance was assigned to topics like 1.C (financial behavior), 7.A (budgeting), and 10.B (trust), as the paper provides supporting evidence. Domains like Mobile-First Design (9.A, 9.B) and Algorithmic topics (6.A, 6.B) were rejected as the paper is qualitative and non-algorithmic. The paper strongly supports Odin's need for empathy-driven features and holistic financial health tracking.
limitations:
  - "Findings are not generalizable beyond the specific rural context of Argao. [unacknowledged]"
  - "Excludes male borrower perspectives, limiting understanding of gender differences in financial stress."
  - "Relies on self-reported narratives, which may be influenced by memory and social desirability."
  - "Cross-sectional design cannot observe how financial well-being evolves over multiple loan cycles."
  - "The dual role of women as financial managers and caretakers may create unique psychological burdens not explored in other demographics."
remember_this:
  - "Microfinance provides short-term relief but can create long-term debt dependency."
  - "Borrowers use budgeting, hustling, and faith to cope with financial stress."
  - "Debt stress spills into family relationships and erodes peace of mind."
  - "Many borrowers regret reliance on loans due to persistent debt cycles."
  - "Effective interventions must address both financial and emotional well-being."
```
---

## Paper 33: Zole & Wagh_summarized.md

**Source File:** `Zole & Wagh_summarized.md`

```yaml
paper_id: 10.36227/techrxiv.174909847.74844950/v1
designation: international-algorithm-specific
title: WELTH - AI FINANCE PLATFORM
authors: Zole, P. G.; Wagh, P.
year: 2025
venue: TechRxiv
odin_topics:
  - 3.A
  - 4.A
  - 4.B
  - 7.A
  - 7.B
  - 9.A
  - 10.A
  - 12.A
  - 12.B
tldr: An AI-driven finance platform automates budgeting, receipt scanning, and transaction parsing, achieving 40% time reduction and 95% categorization accuracy.
problem_and_motivation: Traditional financial management relies on manual entry and spreadsheets, which are error-prone and inefficient. Existing systems lack automation and fail to integrate personal and business finances, leading to fragmented tracking. An AI-powered solution is needed to provide real-time insights and reduce manual effort.
approach:
  - Built a web platform using React and ShadCN UI for a responsive interface.
  - Backend uses Next.js with Prisma and PostgreSQL for data storage.
  - Integrated Gemini AI for receipt scanning and transaction categorization via OCR and NLP.
  - Parsed SMS and email transactions using Twilio and Gmail APIs.
  - Provided AI-driven insights and recommendations based on spending patterns.
  - Secured user data with JWT authentication and Clerk for session management.
  - Evaluated the platform through user testing with feedback on efficiency and accuracy.
findings:
  - "num: 40% reduction in time spent on manual data entry due to AI receipt scanner."
  - "num: 95% accuracy in AI-based transaction categorization with minimal corrections."
  - "num: 85% of users felt more confident in financial decisions after using AI insights."
  - "num: 90% of users preferred unified personal and business finance management."
  - Platform improves financial accuracy and enables data-driven decisions.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: AI
    definition: Artificial Intelligence, the simulation of human intelligence in machines.
  - term: OCR
    definition: Optical Character Recognition, technology to extract text from images.
  - term: NLP
    definition: Natural Language Processing, AI field for understanding and generating human language.
critical_citations:
  - "[Verma & Nair, 2021] — Reviews AI trends in finance."
  - "[Chopra & Banerjee, 2022] — OCR and NLP for receipt extraction."
  - "[Thomas & Kulkarni, 2022] — AI insights for budgeting."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Uses AI to automatically categorize transactions with 95% accuracy.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews traditional and AI-based finance tools and their limitations.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Explicitly identifies inefficiencies and lack of integration in traditional systems.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Provides automated budgeting and real-time updates.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: Offers personalized AI-driven financial recommendations.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Built with responsive UI using React for mobile-friendly experience.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Implements JWT, Clerk, and secure data handling.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Conducts user testing and reports quantitative performance metrics.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Evaluates receipt scanner accuracy and categorization performance.
  contribution: The paper's AI-powered receipt scanning and transaction categorization directly inform Odin's expense categorization module (3.A) by demonstrating high accuracy with minimal manual effort. Its evaluation framework (12.A) provides metrics and methods for assessing system effectiveness, including time reduction and user satisfaction. The integration of personal and business accounts suggests a design approach for Odin's multi-account support and unified dashboard. The personalized insights and recommendations support budget recommendation features (7.B) and can guide Odin's AI-driven advisory capabilities.
  directly_justifies:
    - AI-powered receipt scanning reduces manual data entry time by 40%.
    - Transaction categorization achieves 95% accuracy using AI.
    - Unified personal and business finance management is preferred by 90% of users.
    - AI-generated insights increase user confidence in financial decisions by 85%.
  limits:
    - The study is based on a preprint and not peer-reviewed. [unacknowledged]
    - Sample size of user testing is not disclosed. [unacknowledged]
    - The platform's AI algorithms (Gemini AI) are not detailed, limiting reproducibility. [unacknowledged]
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was found directly relevant to Expense Categorization (3.A, high) and Budget Recommendation (7.B, high) because it implements AI-driven classification and personalized insights. It also strongly addresses Limitations and Gaps (4.B, high) and Evaluation Frameworks (12.A, high) through its problem statement and user testing. Medium relevance was assigned to Landscape of Existing Systems (4.A), Budgeting Strategies (7.A), Mobile-First Design (9.A), Data Privacy (10.A), and Algorithmic Evaluation (12.B). Domains such as Behavioral Profiling (5.A-C), Predictive Modeling (6.A-B), Infeasibility Handling (7.D), Anomaly Detection (8.A-C), Engagement (11.A-B), and Savings/Debt (13.A-C) were considered but rejected because the paper does not address profile classification, forecasting, anomaly detection, retention, or savings/debt management specifically. Borderline cases include Mobile UX (9.B) which is touched upon but not central, and Anomaly Detection (8.A) mentioned only in literature review; these were not selected as primary. Overall, the paper provides moderate to high relevance for Odin's expense categorization, budgeting, and evaluation modules, though it is not Filipino-specific.
limitations:
  - Preprint not yet peer-reviewed.
  - User testing sample size and demographics not provided.
  - Lacks comparison with state-of-the-art AI finance platforms.
  - No detailed description of the AI models used, limiting reproducibility.
remember_this:
  - Welth reduced manual data entry time by 40% using AI receipt scanning.
  - AI-based transaction categorization achieved 95% accuracy.
  - 85% of users reported increased confidence in financial decisions.
  - 90% of users preferred unified personal and business finance management.
```
---

## Paper 34: Imawan et al_summarized.md

**Source File:** `Imawan et al_summarized.md`

```yaml
paper_id: 10.58536/j-hytel.166
designation: international
title: Enhancing Financial Literacy in Young Adults: An Android-Based Personal Finance Management Tool
authors: Imawan, R.; Putra, W. P.; Alqahtani, R.; Milakis, E. D.; Dumchykov, M.
year: 2025
venue: Journal of Hypermedia & Technology-Enhanced Learning
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 9.A
  - 9.B
  - 11.A
  - 11.B
  - 12.A
  - 13.A
tldr: An Android PFM app using the Waterfall model achieved a 4.6/5 usability score, demonstrating that targeted digital tools can improve financial habits in young adults.
problem_and_motivation: Young adults face financial challenges from limited experience, yet existing tools often fail to engage them. There is a practical gap in using mobile-first solutions tailored to this demographic's needs.
approach:
  - The application was developed using the Waterfall model with Laravel (backend) and Flutter (frontend).
  - Requirements were gathered via interviews and surveys with young adults in higher education.
  - Features include income/expense tracking, budget projection, financial goal setting, and notifications.
  - Black-box testing verified the functionality of core modules including login, tracking, goals, budgets, reports, and notifications.
  - Usability was evaluated by 50 users on a 5-point Likert scale across six aspects: usability, user satisfaction, functionality, engagement, design, and feedback.
findings:
  - The application achieved an overall score of 4.6/5, rated 'Excellent'.
  - Users rated design satisfaction highly, with 74% giving a 5 for visual appeal and 70% for layout clarity.
  - Engagement was strong, with 78% of users likely to continue using the app and 76% feeling motivated to track finances.
  - Features like income/expense tracking and budget projections were highly rated for both functionality and satisfaction.
  - Users requested additional customization options and more detailed financial trend analysis.
key_figures_tables:
  - Figure 10: Average scores per evaluation aspect → All six aspects scored above 4.5/5, indicating consistent high performance.
key_equations:
  - equation: Aspect Score = (Sum(Indicator Scores)) / (Number of Indicators)
    explanation: Calculates average score for each evaluation aspect.
  - equation: Overall Application Score = (Sum(Aspect Scores)) / (Number of Aspects)
    explanation: Calculates the total average score across all aspects.
definitions:
  - term: Waterfall Model
    definition: A linear, sequential software development methodology with distinct phases.
  - term: Black-box Testing
    definition: A testing method that evaluates functionality without inspecting internal code.
critical_citations:
  - "[Lusardi & Messy, 2023] — Foundational work on financial literacy and wellbeing."
  - "[Petersen et al., 2009] — Contextualizes the Waterfall model in large-scale development."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: The study focuses on young adults in higher education, analogous to the Filipino target demographic.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: contextual
      justification: Discusses income and expense structures relevant to young adults.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: contextual
      justification: The study explicitly addresses financial habits and literacy, similar to the target behavior.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: The application includes a detailed expense categorization module.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: User feedback indicated a need for more customization in categories, directly informing design considerations.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: The introduction reviews existing tools and identifies a gap for young adults, directly mapping to this topic.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: The study explicitly states that existing tools overlook young users' needs, a key gap for Odin to address.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: The application aims to influence financial behaviors through engagement, touching on profiling.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: high
      justification: The study uses an Android-based app, providing evidence for the efficacy of mobile-first design for financial management.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: high
      justification: The high usability scores (4.6/5) validate the UX design choices made in the application.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: The study measures engagement and finds that notifications and progress tracking improve it.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: The notification module and goal-tracking features are cited as key retention and engagement mechanisms.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: The study uses a specific evaluation framework (Likert scale across six aspects) to assess its system.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: The financial goal module is a core feature, enabling users to set and track savings targets.
  contribution: "This paper provides a validated reference implementation for a mobile-first PFM app targeting young adults. The usability framework (six aspects with a Likert scale) offers a direct evaluation template for Odin's user testing. The findings on engagement drivers (notifications and goal progress) justify Odin's design for retention. The user feedback on customization and trend analysis highlights specific feature gaps that Odin should prioritize."
  directly_justifies:
    - "A mobile-first approach is effective for engaging young adults in personal finance management."
    - "Notification reminders and visual goal progress are key mechanisms for encouraging consistent financial tracking."
    - "User satisfaction is strongly correlated with intuitive design and accurate transaction recording."
    - "Young adults in higher education have specific financial management needs that generic tools fail to address."
    - "High usability scores are achievable with a well-designed PFM app, supporting the feasibility of Odin's development."
  limits:
    - "The study's evaluation period was short (two weeks), potentially not capturing long-term habit formation."
    - "The sample was limited to 50 university students from one institution, which may not be representative of all young adults."
    - "The paper does not evaluate the system's ability to handle infeasible budget constraints."
    - "The study does not incorporate predictive modeling or forecasting algorithms for spending."
    - "The evaluation was conducted in a beta testing environment, not a live production setting with real-world data."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper's focus on building and evaluating a PFM app made domains 3 (Expense Categorization), 4 (Existing Systems & Gaps), 9 (Mobile-First Design), 11 (User Retention & Engagement), 12 (System Evaluation), and 13 (Savings & Debt Management) highly relevant. Domains related to predictive modeling (6), anomaly detection (8), and data privacy (10) were considered and rejected as the paper does not implement algorithmic forecasting or anomaly detection, nor does it detail privacy mechanisms. The paper's discussion of financial behaviors and target demographics provided contextual support for domains 1 (Filipino Young Professionals) and 5 (Behavioral Profiling). The mapping resolved borderline cases by prioritizing direct feature implementations (e.g., 3.A and 13.A) over behavioral framing (e.g., 5.A), which was assigned a 'medium' or 'contextual' relevance. Overall, the paper is highly relevant for validating Odin's core design and evaluation approach but offers limited insight into its more advanced algorithmic and privacy-focused modules."
limitations:
  - "The evaluation was conducted in a controlled environment with a limited time frame, which may not reflect long-term usage patterns."
  - "The sample of 50 university students from a single institution may not be generalizable across different cultural or economic contexts. [unacknowledged]"
  - "The study does not assess the application's performance on older devices or under varying network conditions. [unacknowledged]"
  - "The paper lacks a rigorous statistical analysis of pre- and post-intervention financial literacy. [unacknowledged]"
remember_this:
  - "The app received an overall usability score of 4.6 out of 5."
  - "Notifications and goal tracking are key drivers for user engagement."
  - "Users frequently requested more customization and detailed spending analysis."
  - "A mobile-first design is validated as effective for young adult financial management."
  - "The evaluation framework covers usability, satisfaction, functionality, engagement, design, and feedback."
```
---

## Paper 35: Duvalla_summarized.md

**Source File:** `Duvalla_summarized.md`

```yaml
paper_id: 10.32996/jcsts.2025.7.4.12
designation: international
title: Human-AI Collaboration in Customer Behavior Research: Personalizing Financial Services
authors: Duvalla, V. R.
year: 2025
venue: Journal of Computer Science and Technology Studies
odin_topics:
  - 3.A
  - 4.A
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 7.B
  - 10.A
  - 10.B
  - 12.A
tldr: Human-AI collaboration enhances financial personalization by combining AI's pattern recognition with human contextual and ethical oversight.
problem_and_motivation: Financial institutions struggle to implement effective personalization due to fragmented data and the complexity of interpreting customer behavior. Purely algorithmic or human-driven approaches are insufficient for nuanced, culturally-aware financial advice. A framework that synergizes AI capabilities with human expertise is needed to address these gaps.
approach:
  - The paper reviews existing literature and industry reports on AI applications in financial services.
  - It proposes a human-in-the-loop (HITL) framework that integrates AI models with human expertise for knowledge collaboration and ethical oversight.
  - It details a data infrastructure including integrated platforms, real-time processing, and governance frameworks.
  - It discusses advanced AI models for customer segmentation, including multi-dimensional behavioral, temporal pattern, and neural network approaches.
  - It presents a case study of JP Morgan Chase's implementation of a human-AI collaborative platform.
findings:
  - num: 31% improvement in customer retention metrics for banks using advanced analytics.
  - Human-guided AI models achieve higher accuracy in predicting customer financial needs than fully automated systems.
  - Human-in-the-loop protocols improve model prediction accuracy compared to automated systems alone.
  - num: 59% higher customer satisfaction scores are achieved with unified omnichannel orchestration.
  - Federated learning can achieve predictive accuracy of centralized models while keeping customer data local.
  - Financial institutions with formal ethical review boards identify more potential adverse impacts during model development.
key_figures_tables:
  - Figure 1: Data Infrastructure for Behavioral Analysis → Shows integrated data, real-time processing, and governance layers.
  - Figure 2: Advanced AI Models for Customer Segmentation → Illustrates clustering, temporal mining, and neural network architectures.
  - Table 1: Comparative Analysis of Human-AI Collaboration Models → Compares collaboration models and their key characteristics.
  - Figure 3: Operationalizing Predictive Insights in Financial Services → Depicts insight deployment, omnichannel orchestration, and experimentation.
  - Figure 4: Future Directions and Ethical Considerations in Financial AI → Highlights explainable AI, privacy, and governance models.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: HITL
    definition: Human-in-the-loop, a paradigm where human expertise is integrated into AI systems.
  - term: XAI
    definition: Explainable Artificial Intelligence, techniques to make AI decisions interpretable.
  - term: PFMS
    definition: Personal Financial Management System, software for managing personal finances.
critical_citations:
  - "[Karangara et al., 2024] — foundational for HITL frameworks in fintech."
  - "[Kong et al., 2010] — essential for temporal pattern discovery."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Discusses behavioral segmentation for financial personalization.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides background on challenges in financial personalization.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly addresses behavioral segmentation and profiling using AI.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: Mentions the need for temporal patterns to predict future behaviors.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Details advanced clustering and neural network approaches for classification.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Focuses on AI models for predicting customer financial needs and churn.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Relates to personalization of financial advice, but does not specifically address budget recommendation.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Dedicated section on privacy-preserving technologies like federated learning.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Emphasizes explainability and ethical governance to build user trust.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Discusses continuous optimization through experimentation and A/B testing.
  contribution: The paper provides a comprehensive framework for human-AI collaboration that can inform the design of Odin's behavioral profiling module (5.A) by detailing advanced segmentation techniques. Its emphasis on privacy-preserving personalization (10.A) directly supports Odin's data handling requirements. The discussion on ethical oversight and explainability (10.B) justifies the need for transparent and trustworthy features in Odin. Furthermore, the case study on JP Morgan Chase offers a real-world example of operationalizing such a system, which can guide the architecture of Odin's predictive and recommendation engines (6.A, 7.B).
  directly_justifies:
    - Human-AI collaboration improves model prediction accuracy.
    - Advanced clustering identifies up to 15 distinct behavioral segments.
    - Federated learning enables personalization without centralizing sensitive data.
    - Real-time contextual awareness increases conversion rates on personalized offers.
    - Ethical governance frameworks are essential for responsible AI implementation.
  limits:
    - The paper is a review and does not present original experimental results.
    - It lacks a specific evaluation methodology for the proposed human-AI framework.
    - The case study is based on a single large institution and may not be generalizable to smaller contexts.
    - Discussion of budget recommendation systems is minimal.
  mapping_rationale: A systematic scan across all 12 functional domains was conducted. The paper's core focus on human-AI collaboration for financial personalization flagged the domains of Behavioral Profiling & Classification, Spending Forecasting, Data Privacy & User Trust, and System Evaluation as highly relevant. Specifically, topic codes 5.A (high) and 6.A (high) were selected for their direct focus on behavioral profiling and predictive modeling. Codes 10.A and 10.B (high) were chosen for their dedicated sections on privacy and trust, which are critical for Odin. 3.A (medium) was selected due to its relevance to segmentation, while 5.C (medium) and 12.A (medium) were included for their supporting discussions on classification and evaluation. 5.B (low) and 7.B (low) were considered but given lower relevance due to only tangential mentions of cold-start and budget recommendation. The domains of Filipino Cultural Context, Expense Categorization (beyond 3.A), Existing Systems & Gaps (beyond 4.A as contextual), Anomaly Detection, Mobile-First Design, and Savings & Debt Management were considered and rejected as the paper does not provide actionable insights for these specific Odin modules. Overall, the paper offers strong support for Odin's user modeling and trust/privacy features.
limitations:
  - The analysis is derived from secondary sources and industry reports.
  - Limited discussion on the specific algorithms for anomaly detection or budget allocation.
  - The paper does not address the cold-start problem in financial profiling. [unacknowledged]
  - No specific evaluation of user retention mechanisms for PFMS. [unacknowledged]
  - It does not cover mobile-first design principles. [unacknowledged]
remember_this:
  - Human-AI collaboration achieves 31% higher retention rates.
  - Federated learning maintains prediction accuracy while preserving privacy.
  - Real-time insights increase conversion rates on personalized offers by 59%.
  - Explainable AI is essential for building customer trust.
  - Ethical oversight is critical for fair and responsible personalization.
```
---

## Paper 36: Kowsar M. et al-2025_summarized.md

**Source File:** `Kowsar M. et al-2025_summarized.md`

```yaml
paper_id: 10.63125/cv50rf30
designation: international
title: Digitization in Retail Banking: A Review of Customer Engagement and Financial Product Adoption in South Asia
authors: Kowsar, M. M.; Islam, S.; Mohiuddin, M.; Siddiqui, N. A.
year: 2025
venue: 1st Global Research and Innovation Conference 2025
odin_topics:
  - 1.A
  - 2.A
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 9.A
  - 9.B
  - 10.A
  - 11.A
  - 11.B
  - 12.A
  - 13.A
tldr: A systematic review of how digitization, mobile infrastructure, and AI-driven personalization reshape customer engagement and financial product adoption across South Asia.
problem_and_motivation: Retail banking digitization is transforming customer engagement and product adoption globally, but a comprehensive, region-specific synthesis for South Asia is lacking. Understanding these dynamics is crucial for informing inclusive digital financial strategies.
approach:
  - Systematic review following the PRISMA 2020 framework.
  - Searched Scopus, Web of Science, JSTOR, EBSCOhost, ProQuest, Google Scholar, and institutional repositories.
  - Covered 84 peer-reviewed studies published between 2010 and 2024.
  - Synthesized findings on digital infrastructure, customer engagement, product adoption, and inclusion.
  - Analyzed the interplay of fintech innovation, regulatory frameworks, and socio-cultural determinants.
findings:
  - num: Mobile phone penetration exceeds 85% and mobile broadband reaches over 95% in countries like India and Sri Lanka.
  - num: Digitally engaged customers in India were 2.3 times more likely to open secondary financial products.
  - Personalization, interactivity, and user experience are critical determinants of engagement in digital banking.
  - AI and Big Data enable predictive analytics, behavioral modeling, and hyper-personalized services.
  - Digital inclusion is uneven; many new accounts are dormant, and usage is concentrated among urban, literate populations.
  - Product adoption is high for savings, microloans, and insurance, driven by simplified interfaces and automated workflows.
  - Customer engagement is a key differentiator for user retention and financial activity levels.
  - Regulatory support and fintech innovation must operate synergistically for sustainable digital banking.
  - Interface simplicity and automated onboarding can substitute for formal financial literacy.
  - Gender, age, and digital literacy remain significant barriers to equitable participation.
key_figures_tables:
  - Figure 1: Conceptual framework linking digitization to customer engagement and product adoption → Framework shows digitization as central driver.
  - Figure 2: Map of digitization enabling financial services delivery in South Asia → Highlights mobile, ID, and fintech as key enablers.
  - Figure 5: Drivers of customer engagement in digital banking → Personalization, UX, and behavioral nudges are key.
  - Figure 7: Pathways from financial exclusion to inclusion through digital banking → Shows JAM trinity and mobile models bridging access gaps.
  - Figure 8: Key findings from the review → Summarizes infrastructure, product adoption, and engagement outcomes.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Digitization
    definition: Conversion of analog information and manual processes into digital formats, enabling automation and real-time processing.
  - term: Financial Inclusion
    definition: Access to useful and affordable financial products and services delivered responsibly and sustainably.
  - term: Customer Engagement
    definition: Emotional and behavioral involvement of customers with digital banking services, extending beyond transactions.
  - term: Fintech
    definition: Technology-driven innovation in financial services, offering specialized solutions like peer-to-peer lending and robo-advisory.
  - term: JAM Trinity
    definition: India's policy framework linking Jan Dhan bank accounts, Aadhaar digital identity, and Mobile connectivity.
critical_citations:
  - "[Vrana & Singh, 2025] — Defines digitization and its transformative role in banking."
  - "[Lashitew et al., 2020] — Discusses mobile-enabled hybrid financial services in South Asia."
  - "[Koskelainen et al., 2023] — Links literacy to digital financial service adoption and trust."
  - "[Van Veldhoven & Vanthienen, 2022] — Examines fintech-regulatory interplay for digital ecosystem stability."
  - "[Kumar et al., 2019] — Provides foundational framework for multi-dimensional customer engagement."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Provides comparative insights on young, digitally-savvy users in South Asia.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: Discusses socio-cultural determinants of engagement, such as gender and collective decision-making.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Comprehensively reviews digital banking ecosystems and fintech platforms in South Asia.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Highlights urban-rural disparities, dormant accounts, and socio-demographic barriers.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Discusses behavioral determinants like literacy and trust influencing engagement profiles.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: low
      justification: Mentions AI-driven onboarding and behavioral nudges, but not cold-start profiling explicitly.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: References AI for behavioral modeling but does not detail classification methods.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: high
      justification: Emphasizes mobile-first ecosystems as primary access channels in South Asia.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: high
      justification: Identifies UX personalization, localization, and gamification as key engagement drivers.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Notes cybersecurity and biometric verification as critical for user trust and inclusion.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: Directly examines behavioral, cognitive, and emotional engagement in digital banking.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: high
      justification: Finds that personalized prompts and goal-setting features significantly enhance retention.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses a systematic review methodology (PRISMA) as an evaluation framework.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Reviews micro-savings products and gamified incentives for low-income users.
  contribution: This review provides a comprehensive, region-specific synthesis of digital banking transformation that directly informs Odin's understanding of mobile-first engagement in emerging markets. Its findings on AI-driven personalization, behavioral nudges, and UX design justify the development of Odin's recommendation and engagement modules. The paper's detailed examination of financial inclusion barriers and demographic disparities supports Odin's focus on inclusive, culturally-sensitive design for Filipino young professionals. The synthesis of fintech-regulatory interplay and user trust considerations provides a strategic foundation for Odin's architecture and data privacy approach.
  directly_justifies:
    - "Mobile-first design and interface localization are essential for retaining users in competitive fintech ecosystems."
    - "AI-powered behavioral nudges and personalized financial tools significantly increase adoption of savings and credit products."
    - "User engagement, driven by personalization and interactivity, is a critical determinant of platform loyalty and product uptake."
    - "Digitization lowers entry barriers but must be paired with inclusive design to bridge socio-demographic gaps."
  limits:
    - "Focuses on South Asia, limiting direct generalizability to the Philippines without adaptation."
    - "Synthesizes existing literature rather than presenting new primary empirical data."
    - "Does not deeply evaluate specific algorithm performance or computational techniques."
  mapping_rationale: A systematic scan across all 12 functional domains was conducted. The domains of "Existing Systems & Gaps," "Behavioral Profiling & Classification," "Mobile-First Design," and "User Retention & Engagement" were flagged as highly relevant, leading to the selection of topics 4.A, 4.B, 5.A, 9.A, 9.B, 11.A, and 11.B as high or medium relevance. The "Filipino Cultural Context" domain (topics 2.A, 2.B, 2.C, 2.D) was considered, but the paper's focus on South Asia limits its applicability; only 2.A (culturally specific practices) was deemed contextual. Domains like "Expense Categorization," "Spending Forecasting," "Budget Recommendation," and "Anomaly Detection" were considered but rejected as the paper does not address these specific technical modules. The "Savings & Debt Management" domain was partially relevant (topic 13.A) due to the review of micro-savings products. Overall, the paper provides strong justification for Odin's design in engagement, UX, and inclusion strategy, though its technical algorithmic contributions are minimal.
limitations:
  - "Limited direct applicability of South Asian findings to the Filipino context without further validation."
  - "Relies on secondary sources, which may inherit biases or gaps from the original studies."
  - "The rapid evolution of digital finance means some findings may become outdated quickly."
  - "Focuses on retail banking broadly, not specifically on personal finance management applications like Odin. [unacknowledged]"
remember_this:
  - "Digital engagement significantly increases cross-buying of financial products."
  - "Mobile-first design and personalization are critical for user retention in digital finance."
  - "AI and big data are central to enabling predictive, personalized banking services."
  - "Digitally engaged customers are 2.3 times more likely to adopt multiple financial products."
  - "Infrastructure alone does not guarantee inclusion; socio-demographic barriers persist."
```
---

## Paper 37: Polytarchos_summarized.md

**Source File:** `Polytarchos_summarized.md`

```yaml
paper_id: 10.47852/bonviewFSI52026108
designation: international-algorithm-specific
title: Credit Card Fraud Detection Through Deep Learning and Real-Time Data Streams: A Comparison and New Directions
authors: Polytarchos, E.
year: 2025
venue: FinTech and Sustainable Innovation
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
tldr: Compares deep learning and real-time data stream analysis for credit card fraud detection, finding deep learning more accurate but real-time clustering more adaptable and faster.
problem_and_motivation: Credit card fraud detection systems face a critical gap between high-accuracy batch-trained models and real-time adaptability needed for dynamic financial environments. Existing literature lacks a comprehensive empirical comparison of unsupervised stream-based methods against deep learning approaches. This comparison is essential for system designers to make informed deployment decisions.
approach:
  - Used two proprietary datasets: IND (17.5M individual transactions) and SUM (1.2M purchase summaries) for a single year.
  - Deep learning pipeline: trained LSTM and MLP models to classify customer labels and computed an ensemble-based Scale of Suspicious Transaction (SST).
  - Real-time pipeline: implemented the BEReTiC system using CluNN for clustering and KNN for classification on streaming data without preprocessing.
  - Injected 1000 synthetic fraudulent transactions into the IND dataset to evaluate detection capability.
  - Evaluated both approaches on accuracy, fraud detection rate, false positives, and adaptability.
findings:
  - LSTM achieved up to 92% accuracy in predicting total funds range, while real-time clustering achieved only 66% for the same label.
  - num: Deep learning detected 788 out of 1000 injected fraudulent transactions.
  - num: Real-time clustering detected 619 out of 1000 injected fraudulent transactions.
  - num: Real-time clustering produced fewer false positives (574) compared to deep learning (1340).
  - num: Real-time clustering had a lower misclassification rate (0.003%) than deep learning (0.007%).
  - Real-time clustering is inherently adaptive and can identify emerging fraud patterns without retraining.
  - Deep learning requires extensive preprocessing and frequent retraining, limiting real-time applicability.
  - A hybrid model integrating both techniques is proposed as a more effective solution.
key_figures_tables:
  - Table 1: Classification accuracy by label → LSTM highest at 92%, real-time clustering lower.
  - Table 2: Fraud detection performance → Deep learning detects more fraud (788 vs 619) but more false positives.
  - Table 3: Methodology trade-offs → Deep learning has high accuracy but high latency; real-time clustering has moderate accuracy but low latency.
key_equations:
  - equation: SST = percentage of classifiers that misclassified a transaction
    explanation: Scale of Suspicious Transaction for fraud scoring.
  - equation: CSST = product of accuracies of misclassifying classifiers
    explanation: Confidence of the SST score.
definitions:
  - term: BEReTiC
    definition: Best Effort Real-Time Clustering and Classification adapter for streaming data.
  - term: CluNN
    definition: Clustering algorithm used in the BEReTiC system.
  - term: SCoDe2
    definition: Sample collector and deviation detector module in BEReTiC.
  - term: SST
    definition: Scale of Suspicious Transaction, the percentage of classifiers that misclassified a transaction.
  - term: CSST
    definition: Confidence of the Scale of Suspicious Transaction.
  - term: Gower similarity
    definition: Metric combining categorical and numerical data for comparison.
critical_citations:
  - "[Polytarchos et al., 2024] — Patent for BEReTiC system."
  - "[Goodfellow et al., 2020] — Generative adversarial networks for fraud detection."
  - "[Li et al., 2022] — ECOD method for unsupervised outlier detection."
  - "[Huang et al., 2023] — Score-guided networks for anomaly detection."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Compares deep learning and real-time models for predictive fraud detection.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: LSTM networks are evaluated on sequential transaction data.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Core focus is anomaly detection for credit card fraud.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Compares LSTM and real-time clustering as anomaly detection algorithms.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides a comparative evaluation of two detection approaches.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Evaluates LSTM, MLP, and BEReTiC algorithmic modules.
  contribution: This paper provides a direct comparison between batch-trained deep learning models and real-time streaming algorithms for anomaly detection, a core function of Odin's fraud detection module. The evaluation metrics (accuracy, false positives, adaptability) are directly applicable to assessing Odin's algorithmic components. The finding that deep learning offers higher accuracy while real-time methods offer faster detection informs trade-offs in Odin's design. The proposed hybrid model suggests a potential architecture for balancing accuracy and responsiveness.
  directly_justifies:
    - Real-time clustering can detect anomalies in streaming data without preprocessing.
    - Deep learning models require extensive retraining to adapt to new fraud patterns.
    - A hybrid model can combine high accuracy with real-time adaptability.
    - False positive rates are a critical metric for user trust in anomaly detection systems.
  limits:
    - The study focuses on credit card fraud, not general personal finance anomaly detection.
    - Real-time clustering accuracy was substantially lower than deep learning.
    - The proprietary dataset limits reproducibility and generalizability.
    - The study does not address user-facing trust or explainability concerns.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated canonical topic codes was performed. The paper was flagged as relevant to the Anomaly Detection domain (8.A, 8.B) due to its primary focus on fraud detection algorithms. It also touches on Predictive Modeling (6.A, 6.B) through its use of LSTM networks and evaluation of forecasting approaches. The comparative evaluation framework (12.A, 12.B) is relevant for assessing Odin's algorithmic modules. Borderline cases included the paper's mention of gamified challenges (which touches 11.A) and customer profiling (5.A), but these were considered too tangential for inclusion. Domains such as Filipino Cultural Context, Expense Categorization, Data Privacy, and Mobile Design were rejected as the paper does not address these topics. Overall, the paper offers medium to high relevance for Odin's anomaly detection and evaluation modules, but low relevance for other domains.
limitations:
  - The study uses a proprietary dataset, limiting reproducibility. [unacknowledged]
  - Real-time clustering accuracy was substantially lower than deep learning. [acknowledged]
  - The paper does not address false positive impact on user trust or experience. [unacknowledged]
  - The hybrid model is proposed but not implemented or evaluated. [acknowledged]
remember_this:
  - Deep learning achieved 92% accuracy in classifying customer total funds range.
  - Real-time clustering detected 619 of 1000 injected frauds with fewer false positives.
  - A hybrid model integrating both approaches is suggested for optimal performance.
  - Real-time methods adapt to new fraud patterns without retraining.
  - Deep learning requires extensive preprocessing and is not ideal for real-time use.
```
---

## Paper 38: Efendi & Widagdo_summarized.md

**Source File:** `Efendi & Widagdo_summarized.md`

```yaml
paper_id: 10.59890/ijaeam.v3i3.18
designation: international
title: Simple Financial Management in Housewife Communities: A Qualitative Study on Daily Financial Management Patterns
authors: Efendi, M. I.; Widagdo, C. S.
year: 2025
venue: International Journal of Applied Economics, Accounting and Management
odin_topics:
  - 2.A
  - 2.B
  - 3.A
  - 4.A
  - 4.B
  - 5.A
  - 7.A
  - 9.A
  - 10.A
  - 11.A
  - 13.A
  - 13.B
tldr: Housewives in Salatiga develop sophisticated financial management practices including nuanced recording, community-based risk management, and social networks that challenge conventional financial literacy narratives.
problem_and_motivation: Housewives in Indonesia manage daily finances despite lower formal financial literacy rates, yet their sophisticated adaptive strategies remain understudied and undervalued. This research addresses the gap in understanding the daily financial management practices of housewives in resource-constrained communities.
approach:
  - This qualitative case study was conducted in Salatiga, Central Java, involving 25 housewives as primary financial managers.
  - Data was collected through in-depth semi-structured interviews, non-participant observation, and document analysis over two months.
  - Analysis was performed using ATLAS.ti software with open, axial, and selective coding procedures.
  - Member checking was employed to validate findings and ensure accurate representation of participants' experiences.
  - The study focused on daily financial practices, adaptation strategies, and community interactions within a middle to lower-income demographic.
findings:
  - num: 60% of informants perform routine expense recording using simple manual books, while 40% rely on mental monitoring systems.
  - num: Income diversification activities generate an additional Rp300,000 to Rp500,000 per month for some housewives.
  - num: Daily emergency fund contributions range from Rp5,000 to Rp10,000, held in physical containers like tins or envelopes.
  - Housewives develop sophisticated "mental accounting" strategies for prioritizing primary over secondary and tertiary needs.
  - Communities function as informal financial institutions through ROSCAs, jimpitan, and collective purchasing arrangements.
  - Financial communication patterns range from open collaborative to minimal, influenced by education and gender dynamics.
  - Social networks serve as informal insurance mechanisms, providing support during emergencies like illness or hospitalization.
  - Some housewives practice micro-scale savings diversification, including cash in multiple locations and small gold investments.
key_figures_tables:
  - "None."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: ROSCA
    definition: "Rotating Savings and Credit Association; a community-based savings mechanism where members contribute and receive a lump sum in rotation."
  - term: jimpitan
    definition: "A community-based micro-savings practice involving daily collection of rice or small change for social funds."
  - term: mental accounting
    definition: "The cognitive process of categorizing and mentally budgeting funds for specific purposes without physical segregation."
critical_citations:
  - "[Palupiningtyas et al., 2023] — Establishes women's role in domestic financial management despite structural disadvantages."
  - "[Siregar, 2019] — Defines housewives' role in family financial management as a key research area."
  - "[Rutherford] — Introduces concept of 'shadow banking' in community financial systems."
relevance:
  topics:
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: "Documents specific practices like arisan (ROSCAs) and jimpitan as culturally embedded financial mechanisms."
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: "Describes financial cycles synchronized with income patterns and community events, though not explicitly seasonal."
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: "Provides detailed insights into how housewives prioritize and categorize expenses into primary, secondary, and tertiary needs."
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: "Maps the landscape of informal financial systems (ROSCAs, jimpitan) used alongside formal systems in the community."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: "Highlights the gap between formal financial education and the practical needs of housewives."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: "Identifies behavioral profiles based on financial recording, communication, and risk management patterns."
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: "Provides a real-world case of budgeting strategies, including mental accounting and expenditure prioritization."
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: "Briefly mentions the potential for mobile applications but does not focus on design principles."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: "Mentions trust in informal community systems but does not address digital data privacy."
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: "Discusses community engagement but not engagement with digital PFMS."
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: "Documents micro-savings practices and goal-oriented savings like emergency funds and gold accumulation."
    - code: 13.B
      name: Debt Management in PFMS
      relevance: medium
      justification: "Describes rotation debt systems and community norms around borrowing for productive vs. consumptive needs."
  contribution: "This paper contributes to Odin's design by validating the sophistication of informal financial practices that a PFMS can build upon. It informs Odin's expense categorization module by demonstrating real-world mental accounting strategies. The findings on community-based financial networks justify Odin's potential for social or community features. The paper also highlights the importance of user trust and accessibility, aligning with Odin's mobile-first and data privacy considerations."
  directly_justifies:
    - "Housewives in resource-constrained environments develop sophisticated mental accounting systems that formal PFMS can emulate."
    - "Financial literacy in such contexts is experiential and embedded, requiring PFMS to be contextually adaptive."
    - "Community-based financial systems like ROSCAs demonstrate the value of social features within a PFMS."
  limits:
    - "The study is specific to Salatiga, Indonesia, and findings may not be generalizable to other cultural or economic contexts."
    - "Findings are based on self-reported data, which may be subject to social desirability bias."
    - "The study focuses on daily management and does not address long-term financial planning or investment." [unacknowledged]
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant for domains on Filipino Cultural Context (specifically 2.A), Expense Categorization (3.A), and Budget Recommendation (7.A) due to its detailed documentation of real-world financial practices. Medium relevance was assigned to Existing Systems & Gaps (4.A, 4.B), Behavioral Profiling (5.A), Savings & Debt Management (13.A, 13.B) as these are addressed indirectly. Low relevance was noted for Mobile-First Design (9.A) and Engagement Dynamics (11.A) as the paper does not discuss digital applications. Contextual relevance was assigned to Data Privacy (10.A) due to trust in informal systems. Domains related to Forecasting (6.A, 6.B), Anomaly Detection (8.A, 8.B, 8.C), and System Evaluation (12.A, 12.B, 12.C) were rejected as the paper does not address algorithmic or predictive modeling. Overall, the paper provides strong qualitative evidence for the design of user-centric and community-aware PFMS features."
limitations:
  - "The study does not acknowledge the potential for technology to support or replace the manual systems observed." [unacknowledged]
  - "The sample size of 25 housewives limits the generalizability of the findings." [unacknowledged]
remember_this:
  - "Housewives use mental accounting and physical segregation to manage daily finances."
  - "Community systems like ROSCAs act as informal financial institutions for saving and credit."
  - "Income diversification provides additional autonomy and financial resilience for housewives."
  - "num: 60% of housewives perform routine expense recording using simple manual books."
```
---

## Paper 39: Esperanza et al_summarized.md

**Source File:** `Esperanza et al_summarized.md`

```yaml
paper_id: "d3b07384-d9a0-5a1b-9f3c-7a8b9c0d1e2f"
designation: "local"
title: "Digital Lending Efficacy on Debt Management of Wage Earners"
authors: "Esperanza, D. N.; Bithay, L. L.; Jesus, J. B.; Ople-Alviola, C.; Sumilhig, J. M.; Basilisco, G. L."
year: 2025
venue: "ASEAN Journal of Management & Innovation"
odin_topics:
  - "1.C"
  - "4.B"
  - "5.A"
  - "7.A"
  - "10.A"
  - "10.B"
  - "13.B"
tldr: "Digital lending quality significantly predicts repayment and cautious borrowing, while frequent usage reduces budget restraint among Filipino wage earners."
problem_and_motivation: "The expansion of digital lending improves credit access but risks impulsive borrowing and over-indebtedness without adequate financial capability. The influence of digital lending dimensions on specific debt management behaviors remains underexplored. Understanding these relationships is essential for designing inclusive and responsible digital financial systems."
approach:
  - "Used a quantitative descriptive-correlational design with 100 wage earners in Cebu City, Philippines."
  - "Measured digital lending accessibility, usage, and perceived quality via a structured survey adapted from validated scales."
  - "Assessed debt management via STOP (budget restraint), PAY (repayment), and CAUTION (informed borrowing) strategies."
  - "Applied multiple linear regression to test predictive relationships, with Cronbach's alpha >0.80 and IOC=0.92."
  - "Simple random sampling and ethical protocols followed."
findings:
  - "num: Perceived quality significantly predicted PAY (B=0.364, p=0.021) and CAUTION (B=0.379, p=0.010)."
  - "num: Frequent usage negatively predicted STOP (B=-0.259, p=0.007)."
  - "Accessibility did not significantly predict any debt management strategy."
  - "Wage earners showed strong agreement with STOP (M=3.96), PAY (M=3.80), and CAUTION (M=4.20)."
  - "Overall perception of digital lending was favorable (M=3.52), with accessibility highest (M=3.83) and usage neutral (M=3.17)."
  - "Challenges included insufficient income, lack of savings, and impulsive spending."
key_figures_tables:
  - "Table 1: Demographic profile shows majority female, aged 26-35, college-educated, monthly income PHP 10k-20k."
  - "Table 2: Accessibility rated agree (M=3.83), with ease of access highest (M=4.04)."
  - "Table 3: Usage rated neutral (M=3.17), indicating cautious engagement."
  - "Table 4: Quality rated agree (M=3.57), but privacy and collection practices concerns."
  - "Table 11: Regression for STOP shows usage negative significant; overall model not significant."
  - "Table 12: Quality positive significant for PAY; overall model not significant."
  - "Table 13: Quality positive significant for CAUTION; overall model significant (p=0.023)."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "STOP strategy"
    definition: "Budgetary discipline and debt avoidance through planning and restraint."
  - term: "PAY strategy"
    definition: "Commitment to timely repayment and ethical debt settlement."
  - term: "CAUTION strategy"
    definition: "Informed borrowing through critical evaluation of loan terms and risks."
  - term: "TAM"
    definition: "Technology Acceptance Model, explaining technology adoption via perceived ease and usefulness."
critical_citations:
  - "[Putri et al., 2023] — TAM framework for fintech adoption."
  - "[Wanof, 2023] — Financial Capability Framework linking access with decision-making."
  - "[Kawai et al., 2022] — Transparency reduces information asymmetry in lending."
  - "[Yue et al., 2022] — Increased access can lead to debt trap without safeguards."
relevance:
  topics:
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "low"
      justification: "Wage earners are a subset of Filipino young professionals; paper examines their financial behaviors."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "low"
      justification: "Highlights gaps in digital lending (privacy, aggressive collection) relevant to PFMS system limitations."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Defines STOP, PAY, CAUTION as behavioral strategies that can inform financial profiles."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "medium"
      justification: "STOP strategy directly addresses budgeting restraint as a domain knowledge for PFMS."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "medium"
      justification: "Privacy concerns and data protection issues are identified as quality dimensions."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "high"
      justification: "Perceived quality (trust/transparency) significantly predicts repayment and cautious borrowing, directly informing user trust in PFMS."
    - code: "13.B"
      name: "Debt Management in PFMS"
      relevance: "high"
      justification: "Core focus on debt management strategies and their predictors, directly relevant to Odin's debt management module."
  contribution: "The paper's finding that platform quality significantly influences repayment and caution behaviors directly supports Odin's debt management module (13.B) by highlighting the importance of transparent loan terms and trust-building features. The negative effect of frequent usage on budgeting discipline informs Odin's need to incorporate behavioral nudges and spending limits to prevent over-reliance on credit. The emphasis on user education and consumer protection aligns with Odin's data privacy and user trust design considerations (10.A, 10.B). The study's identification of challenges like insufficient savings and impulsive spending underscores the value of integrating savings goal management (13.A) and expense categorization (3.A) into Odin's framework. Overall, the results justify embedding financial literacy content and transparency metrics within Odin's personal finance management system."
  directly_justifies:
    - "Perceived quality of digital lending positively influences repayment behavior (PAY) and cautious borrowing (CAUTION)."
    - "Frequent usage of digital lending weakens budget restraint (STOP)."
    - "Accessibility alone does not significantly affect debt management strategies."
    - "Privacy concerns and aggressive collection practices undermine borrower trust."
  limits:
    - "None identified."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The most directly relevant domains were Debt Management (13.B) and User Trust (10.B), both assigned high relevance because the paper's core findings directly link platform quality to repayment and cautious borrowing, and usage to budgeting discipline. Behavioral Profiling (5.A) and Budgeting Strategies (7.A) were assigned medium relevance as the STOP, PAY, CAUTION strategies offer behavioral frameworks. Data Privacy (10.A) was medium due to explicit privacy concerns. Financial Behavior (1.C) and Existing Systems Gaps (4.B) were low as they are tangentially related. Domains such as Expense Categorization, Forecasting, Anomaly Detection, Mobile-First Design, Engagement, and Evaluation were rejected because the paper does not address these areas. Borderline cases included the overlap between STOP budgeting and 7.A, resolved by including 7.A for its direct budgeting focus; and between privacy and trust, resolved by including both. Overall, the paper provides moderate direct relevance to Odin, with actionable insights for debt management and trust modules."
limitations:
  - "Cross-sectional design limits causal inference and cannot track behavioral changes over time."
  - "Sample size of 100 in urban Cebu City may not be generalizable to rural areas or other demographics."
  - "Self-reported data may introduce response bias, especially on sensitive financial topics."
  - "Quantitative approach does not explore deep psychological or contextual factors influencing debt decisions."
  - "The study focuses on digital lending rather than broader personal finance management systems."
remember_this:
  - "Perceived quality of digital lending significantly predicts repayment and cautious borrowing behaviors."
  - "Frequent digital borrowing reduces budgeting discipline among wage earners."
  - "Accessibility and usage are less influential than platform quality for responsible debt management."
  - "Quality positively predicted PAY (B=0.364) and CAUTION (B=0.379) in regression models."
  - "Wage earners demonstrate strong caution (M=4.20) but face income and savings challenges."
```
---

## Paper 40: Rastogi et al_summarized.md

**Source File:** `Rastogi et al_summarized.md`

```yaml
paper_id: "10.55041/IJSREM46164"
designation: "international-algorithm-specific"
title: "Personal Expense Tracker Using AI"
authors: "Rastogi, H.; Goel, A.; Bahl, V.; Sengar, N."
year: 2025
venue: "International Journal of Scientific Research in Engineering and Management (IJSREM)"
odin_topics:
  - "3.A"
  - "3.B"
  - "4.A"
  - "4.B"
  - "6.A"
  - "6.B"
  - "7.A"
  - "7.B"
  - "8.A"
  - "8.B"
  - "10.A"
tldr: "An AI-powered expense tracker integrates OAuth, Firebase, TensorFlow, and notification parsing to automate tracking, provide predictive insights, and preserve privacy, overcoming manual entry and security gaps."
problem_and_motivation: "Manual expense tracking is error-prone and time-consuming; existing automated systems lack predictive analytics and privacy safeguards. A solution must automate data entry via notification parsing and offer intelligent budgeting while protecting sensitive information."
approach:
  - "Reviews existing expense tracking systems to identify limitations in automation, privacy, and predictive capabilities."
  - "Designs a system architecture with OAuth/Firebase for authentication and data management, and TensorFlow for analytics."
  - "Implements a notification parser using Android NotificationListenerService to extract transaction amounts locally without storing full messages."
  - "Supports manual entry, receipt scanning, and customizable budget limits with visual spending charts."
  - "Evaluates system via feature comparison with prior systems and user trials reporting time reduction."
findings:
  - "num: 78% decrease in time spent on expense tracking compared to manual methods."
  - "The notification parsing mechanism automates data capture while ensuring privacy by processing data on-device."
  - "The system provides real-time budget updates and alerts when limits are exceeded."
  - "TensorFlow enables spending pattern recognition, budget forecasting, and anomaly detection."
  - "Feature comparison shows the proposed system includes social logins, real-time notifications, voice input, notification parsing, AI predictions, and privacy-preserving processing, which are lacking in prior works."
key_figures_tables:
  - "Table I: Feature comparison across Vanitha et al., Kritika et al., Chang et al., and proposed system → highlights comprehensive feature set of proposed system."
  - "Fig. 3: Daily Budget Tracking Interface showing current budget, spent amount, remaining budget, and recent transactions → illustrates real-time budget visibility."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "OAuth"
    definition: "Open standard for token-based authentication and authorization."
  - term: "Firebase"
    definition: "Google's mobile platform providing authentication, cloud database, and storage."
  - term: "TensorFlow"
    definition: "Open-source machine learning framework for building and training models."
  - term: "NLP"
    definition: "Natural Language Processing for understanding and parsing text."
  - term: "NotificationListenerService"
    definition: "Android service that allows apps to read incoming notifications."
critical_citations:
  - "[Sharma and Wilson, 2024] — Secure notification parsing method."
  - "[Chang et al., 2021] — TensorFlow-based prediction with 87% accuracy."
  - "[Li and Rodriguez, 2022] — NLP achieves 91% accuracy in categorization."
  - "[Nguyen et al., 2023] — Privacy-preserving on-device processing."
relevance:
  topics:
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "high"
      justification: "Uses NLP for automated expense categorization."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      relevance: "high"
      justification: "Discusses customizable budget limits and category design."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "high"
      justification: "Reviews existing systems like Vanitha et al. and Kritika et al."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Identifies gaps such as lack of predictive analytics and privacy."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Employs TensorFlow for predictive modeling and forecasting."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Focuses on forecasting algorithms for sequential spending data."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "medium"
      justification: "Budgeting strategies are used but not deeply explored."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Provides budget forecasting and alerts, but no optimization."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Includes anomaly detection for irregular spending patterns."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Uses TensorFlow for anomaly detection algorithms."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "Notification parsing preserves privacy by local processing."
  contribution: "The paper's notification parsing mechanism directly informs Odin's expense entry module by automating capture without privacy loss. Its TensorFlow-based forecasting supports Odin's spending prediction module. The anomaly detection capability informs Odin's fraud detection component. The emphasis on on-device processing aligns with Odin's data privacy design. The system's evaluation approach provides a baseline for comparing feature sets."
  directly_justifies:
    - "Notification parsing can automate expense tracking while safeguarding user privacy."
    - "TensorFlow-based models can forecast future expenses with high accuracy."
    - "NLP-based categorization reduces manual effort and improves accuracy."
    - "Real-time budget updates and alerts enhance user adherence."
    - "Integrating OAuth and Firebase provides secure authentication and data synchronization."
  limits:
    - "Android-only notification parsing limits cross-platform applicability [unacknowledged]."
    - "May not capture cash transactions or non-digital payments [unacknowledged]."
    - "Evaluation relies on feature comparison rather than quantitative performance metrics [unacknowledged]."
  mapping_rationale: "A systematic scan of all 12 functional domains flagged expense categorization, existing systems, spending forecasting, budget recommendation, anomaly detection, and data privacy as relevant. Topic codes 3.A, 3.B, 4.A, 4.B, 6.A, 6.B, 7.A, 7.B, 8.A, 8.B, and 10.A were selected with high or medium relevance. Borderline cases: the paper touches on budgeting (7.A/7.B) but does not address constrained optimization (7.C); it mentions mobile interfaces but not design principles (9.A/9.B), so those were rejected. Domains related to Filipino cultural context (1.A–2.D) and savings/debt (13.A–13.C) were considered and rejected because the paper is not specific to the Philippines or debt management. Overall, the paper is highly relevant to Odin's core modules, particularly automation, prediction, and privacy."
limitations:
  - "Android-only notification parsing limits cross-platform applicability [unacknowledged]."
  - "May not capture cash transactions or non-digital payments [unacknowledged]."
  - "Evaluation relies on feature comparison rather than quantitative performance metrics [unacknowledged]."
  - "Privacy of notifications still depends on user permissions and system access [unacknowledged]."
remember_this:
  - "Notification parsing automates expense entry without storing sensitive data."
  - "TensorFlow provides predictive analytics for budget forecasting and anomaly detection."
  - "The system reduces manual tracking time by 78 percent."
  - "Secure authentication and data management use OAuth and Firebase."
  - "The system addresses gaps in prior tools through AI integration and privacy design."
```
---

## Paper 41: Albert et al-2025_summarized.md

**Source File:** `Albert et al-2025_summarized.md`

```yaml
paper_id: 10.62986/dp2025.35
designation: local
title: Gender Equality, Disability, and Social Inclusion in the Philippines: Progress, Challenges, and Opportunities in SDG 5 and SDG 10
authors: Albert, J.R.G.; Dacuycuy, C.B.; Quisumbing, A.R.; Basillote, L.B.; Cabalfin, D.L.D.; Vargas, A.R.P.; Luzon, P.E.D.; Mahmoud, M.A.
year: 2025
venue: PIDS Discussion Paper Series
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 3.C
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 7.A
  - 7.D
  - 8.C
  - 9.A
  - 10.A
  - 10.B
  - 11.A
  - 12.A
  - 13.C
tldr: Legal progress on GEDSI in the Philippines masks persistent implementation gaps; intersectional analysis reveals compound marginalization for women, PWDs, and IPs, requiring integrated, data-driven policy reforms.
problem_and_motivation: The Philippines has strong GEDSI laws but struggles with implementation, leaving marginalized groups excluded. Existing single-identity policies fail to address compounded disadvantages from gender, disability, and ethnicity intersections, limiting progress toward SDG 5 and SDG 10.
approach:
  - Mixed-methods combining longitudinal analysis of PSA surveys (FIES, LFS, NDHS) with Shapley decomposition and intersectional analytics.
  - Qualitative data from key informant interviews and focus group discussions with government officials, CSOs, and marginalized communities.
  - Quantifies relative contributions of gender, education, and geography to inequality using decomposition of FIES-LFS merged data for 2018, 2021, and 2023.
  - Examines GEDSI outcomes across SDG 5 and SDG 10 targets, with cross-cutting analysis on education, employment, and transportation access.
  - Evaluates policy effectiveness and implementation gaps through stakeholder perspectives and administrative data from DSWD, PNP, and other agencies.
findings:
  - num: Female disability prevalence (15%) is 50% higher than male (10%), with rates reaching 55% among women with no formal education.
  - num: Income inequality decreased, with the Gini coefficient falling from 0.453 in 2015 to 0.406 in 2023.
  - num: Teenage pregnancy rates declined from 8.6% in 2017 to 5.4% in 2022, but remain high among poor (10.3%) and less-educated (19.1%) women.
  - Intersectional analysis shows that spatial inequalities often exceed ethnic disparities, while ethnic inequality in education strongly correlates with poverty.
  - Women's labor force participation (51.6%) lags behind men's (73.1%), with underemployment persistently higher for men, masking women's exclusion from quality work.
  - The GAD budget has become compliance-oriented, with weak enforcement and misuse limiting its transformational potential.
  - Approximately 37% of Indigenous Peoples live in Geographically Isolated and Disadvantaged Areas, compounding ethnic exclusion with geographic marginalization.
key_figures_tables:
  - Table 1: Philippines' WEF Global Gender Gap rankings (2006-2025) → Volatility in rankings reflects discretionary political appointments, not steady progress.
  - Figure 7: Teenage pregnancy rates by educational attainment → Low education is a major risk factor; rates are 19.1% for primary-educated vs. 1.9% for college-educated.
  - Table 15: Inequality decomposition using household per capita income → Education is the primary driver of between-group income inequality.
  - Figure 18: IP Population overlapping with GIDAs → 2.9 million IPs live in GIDAs, facing severe service access barriers.
  - Table 34: Methodological concordance between NDPS severe and Washington Group classifications → NDPS identifies additional PWDs through environmental context.
key_equations:
  - equation: Total Hours Worked = α + β(sex) + γ(education) + δ(wealth) + ζ(urban) + η(NCR) + ε
    explanation: Regression model identifying determinants of weekly working hours.
definitions:
  - term: GEDSI
    definition: Gender Equality, Disability, and Social Inclusion.
  - term: GAD
    definition: Gender and Development budget policy (5% of agency budgets).
  - term: IP
    definition: Indigenous Peoples.
  - term: PWD
    definition: Persons with Disabilities.
  - term: 4Ps
    definition: Pantawid Pamilyang Pilipino Program (conditional cash transfer).
  - term: GIDA
    definition: Geographically Isolated and Disadvantaged Areas.
  - term: FPIC
    definition: Free, Prior, and Informed Consent.
critical_citations:
  - "[Crenshaw, 1989] — Foundational intersectionality theory adapted for Philippine context."
  - "[UN, 2015] — Establishes SDG 5 and SDG 10 targets and indicators."
  - "[World Bank, 2023] — Documents persistent gender gaps in asset access in East Asia."
  - "[David et al., 2018] — Assesses Philippines' progress on SDG 5."
  - "[Pérez-Brito et al., 2024] — Provides comprehensive data on IP exclusion and 'statistical invisibility'."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Provides detailed demographic, income, and employment data on Filipino young adults and labor market patterns.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Analyzes income distribution, wealth quintiles, and employment sectors relevant to financial structure.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Discusses labor force participation, underemployment, and time use patterns that shape financial behaviors.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Documents family-based care work and resource sharing norms that influence financial practices.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Provides context on poverty cycles and pandemic impacts but not specific seasonal spending data.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: Provides background on care work and family obligations that drive spending cycles.
    - code: 3.C
      name: User-Defined Allocation Constraints
      relevance: contextual
      justification: Discusses constraints from care work and low income but not user-defined budget allocation.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews existing social protection systems (4Ps) and financial inclusion barriers.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Critically assesses implementation failures of GAD budget, disability laws, and social programs.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Provides behavioral data on labor participation, care work, and risk tolerance relevant to financial profiles.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: contextual
      justification: Discusses data gaps and "statistical invisibility" for PWDs and IPs, relevant to profile initialization challenges.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Evaluates GAD budget allocation and policy frameworks for inclusive budgeting.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: contextual
      justification: Discusses policy implementation gaps and resource constraints but not algorithmic feasibility.
    - code: 8.C
      name: Cold‑Start Baseline Strategies for Anomaly Detection
      relevance: contextual
      justification: Highlights data scarcity for marginalized groups, relevant to baseline challenges for anomaly detection.
    - code: 9.A
      name: Mobile‑First Design Principles and Rationale
      relevance: low
      justification: Discusses ICT access and digital divide but not mobile-first design specifically.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Discusses ethical data collection, privacy, and confidentiality for vulnerable populations.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Highlights mistrust in government systems and need for community engagement, relevant to trust.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: contextual
      justification: Notes program awareness and compliance gaps, relevant to engagement challenges.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a comprehensive evaluation of GEDSI policies using mixed-methods and SDG monitoring frameworks.
    - code: 13.C
      name: End‑of‑Period Surplus as a Savings Input
      relevance: contextual
      justification: Discusses income growth and poverty reduction among bottom 40%, relevant to surplus capacity.
  contribution: This paper provides a comprehensive, data-driven baseline for understanding intersectional financial exclusion in the Philippines, directly justifying Odin's need for culturally-aware profiling (topics 1.A, 1.B, 1.C) and highlighting the limitations of current systems (4.B). Its analysis of GAD budget failures (7.A) and "statistical invisibility" (5.B, 8.C) informs Odin's design for inclusive, data-driven personal finance management that must account for compound marginalization.
  directly_justifies:
    - "Single-identity approaches fail to capture compound disadvantages experienced by marginalized groups."
    - "The GAD budget has become compliance-oriented, requiring outcome-based reform for effective allocation."
    - "Data gaps and 'statistical invisibility' hinder evidence-based policy and service delivery for PWDs and IPs."
    - "Labor market inequalities are driven primarily by geographic location and education, not just gender."
    - "Unpaid care work significantly reduces women's economic participation and financial autonomy."
  limits:
    - Data limitations and "statistical invisibility" of IPs and PWDs underrepresent their experiences. [unacknowledged]
    - Lack of formal IRB approval for qualitative components. [acknowledged]
    - Rapid policy changes make it hard to isolate specific intervention effects. [acknowledged]
    - Findings are specific to the Philippine context and may not generalize to other settings. [unacknowledged]
    - The focus on SDG 5 and SDG 10 limits exploration of other SDG interlinkages. [unacknowledged]
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. Domains for Filipino Cultural Context (2.A, 2.B, 2.D) and Behavioral Profiling (5.A, 5.B) were flagged as highly relevant due to the paper's focus on cultural practices, seasonal patterns (like pandemic impacts), and labor market behaviors. The Existing Systems & Gaps domain (4.A, 4.B) is directly addressed through critiques of the GAD budget and social programs, assigned high relevance. Budget Recommendation (7.A, 7.D) is informed by the GAD budget analysis, though infeasibility handling is only contextual. Anomaly Detection (8.C) is contextual due to data scarcity discussions. Mobile-First (9.A) and Data Privacy (10.A, 10.B) are medium/low relevance. User Retention (11.A) and System Evaluation (12.A) are contextual/high respectively. Savings (13.C) is contextual. Borderline cases included seasonal spending (2.B, 2.D) which was resolved by assigning both as contextual. User-defined constraints (3.C) were considered rejected because the paper does not analyze user-defined budget allocation; the focus is on policy-level constraints. The overall relevance is high for informing Odin's design with evidence on structural barriers and the need for intersectional, data-sensitive approaches.
limitations:
  - Official statistics under-represent IPs and PWDs due to geographic and documentation barriers. [acknowledged]
  - Small sample sizes for highly marginalized intersectional categories limit robust statistical analysis. [acknowledged]
  - Lack of formal Institutional Review Board approval. [acknowledged]
  - Rapid policy changes during the research period complicate causal attribution. [acknowledged]
  - Comprehensive time-use survey data is lacking, limiting care work analysis. [unacknowledged]
remember_this:
  - Legal frameworks are progressive but implementation fails, especially for GAD budgets.
  - Women with disabilities face 50% higher prevalence and severe education-related disparities.
  - Income inequality decreased but remains high, with education as the key driver.
  - Intersectional analysis is essential; single-identity policies miss compounded marginalization.
  - Data gaps create "statistical invisibility" for IPs and PWDs, undermining policy design.
```
---

## Paper 42: Yaramolu_summarized.md

**Source File:** `Yaramolu_summarized.md`

```yaml
paper_id: 10.32996/jcsts.2025.7.3.3
designation: international
title: AI-Powered Portfolio Management: Transforming Wealth Management Through Intelligent Automation
authors: Yaramolu, L. S. K. G.
year: 2025
venue: Journal of Computer Science and Technology Studies
odin_topics:
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 12.A
tldr: AI-powered portfolio management leverages machine learning, NLP, and reinforcement learning to enhance investment decisions, personalization, and operational efficiency.
problem_and_motivation: Traditional portfolio management is limited by human cognitive capacity and the inability to process vast datasets in real-time. This necessitates a shift to AI-driven approaches for more effective investment strategies and client service.
approach:
  - Machine learning algorithms analyze historical market data and investor profiles to create nuanced risk assessments.
  - Natural language processing (NLP) extracts sentiment from news, earnings calls, and social media for market predictions.
  - Reinforcement learning continuously optimizes portfolio rebalancing to maintain risk exposure while minimizing costs.
  - The paper reviews literature and synthesizes findings from multiple studies on AI applications in wealth management.
findings:
  - num: Neural network-based portfolio construction achieved risk-adjusted returns approximately 2.5 times higher than traditional methods.
  - num: NLP-powered sentiment indices generated excess returns of 3.8% annually compared to models using only traditional market data.
  - num: Reinforcement learning-optimized rebalancing schedules reduced overall transaction costs by 27%.
  - AI has transformed personalization, enabling tailored strategies for individual investor profiles with 43% higher client retention.
  - Hybrid advisory models combine algorithmic efficiency with human emotional intelligence for complex planning.
key_figures_tables:
  - Table 1: Performance comparison shows AI-driven methods significantly outperform traditional methods in risk-adjusted returns, sector rotation anticipation, and client retention.
  - Figure 1: Architecture diagram of an AI-powered portfolio management platform shows integration of ML, NLP, and RL components.
  - Table 2: Performance metrics show ensemble ML reduces prediction error by 40%, and NLP sentiment analysis improves returns by 3.8%.
  - Table 3: Details implementation challenges, including data quality, algorithmic bias, and regulatory requirements for AI transparency.
  - Table 4: Outlines future trends in hybrid advisory models, predictive analytics, and personalization at scale.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "NLP"
    definition: "Natural language processing, technology for analyzing human language data."
  - term: "XAI"
    definition: "Explainable AI, frameworks that provide clear explanations for AI decisions."
  - term: "ESG"
    definition: "Environmental, social, and governance factors considered in investment decisions."
critical_citations:
  - "[Rizvi and Khalid, 2024] — Demonstrates DL model outperformance in portfolio construction."
  - "[Song et al., 2025] — Shows RL reduces transaction costs and improves rebalancing."
  - "[Turner Lee et al., 2019] — Addresses algorithmic bias and need for explainability."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly discusses AI and ML for market prediction and portfolio optimization.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: Covers predictive analytics for market disruptions, applicable to spending forecast models.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Discusses optimization strategies analogous to budget allocation, though focused on investments.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Provides framework for personalized algorithmic recommendations.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Mentions detecting market anomalies and stress patterns, relevant to transaction anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: Provides a broad view on anomaly detection in finance.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Discusses data quality and security concerns in AI systems.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Emphasizes importance of explainable AI (XAI) and transparency for user trust.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides metrics for evaluating performance of AI-driven financial systems.
  contribution: This paper justifies the use of machine learning for prediction and recommendation modules in Odin. It supports the integration of NLP for user preference analysis and reinforcement learning for dynamic budgeting. It also underscores the necessity of explainable AI to ensure user trust and regulatory compliance, which is critical for a PFMS.
  directly_justifies:
    - "Machine learning algorithms can analyze vast datasets to identify complex patterns for personalized predictions."
    - "Explainable AI frameworks are essential for transparency and building user trust in financial systems."
    - "Reinforcement learning can optimize rebalancing strategies by minimizing transaction costs, analogous to budget adjustments."
    - "Hybrid models combining AI with human oversight are effective for financial decision-making."
  limits:
    - "The paper is a review and does not present new experimental results specifically for personal finance management."
    - "Focus is on investment portfolios, not direct spending or budgeting for individuals."
  mapping_rationale: The systematic scan across all 12 functional domains and associated topic codes flagged several areas of relevance. High relevance was assigned to 6.A (Predictive Modeling) and 10.B (User Trust) due to the paper's direct discussion of ML for prediction and XAI for transparency. Medium relevance was assigned to 6.B (Forecasting), 7.A (Budgeting Strategies), 7.B (Budget Recommendation), 8.A (Anomaly Detection), 10.A (Data Privacy), and 12.A (Evaluation) as the paper provides supporting evidence, frameworks, or contextual examples. Low or contextual relevance was assigned to many topics like 1.A, 2.A, 3.A, etc., as the paper focuses on wealth management rather than Filipino personal finance, expense categorization, or behavioral profiling specific to consumer spending. The paper's broad AI application in finance directly justifies Odin's use of advanced algorithms for prediction, personalization, and trust-building, making it a strong reference for technical feasibility.
limitations:
  - "Focuses on wealth management, not personal finance management, limiting direct applicability."
  - "The review does not address cold-start scenarios common in personal finance apps. [unacknowledged]"
  - "Ethical considerations regarding algorithmic bias are discussed broadly without specific mitigation techniques for spending data. [unacknowledged]"
remember_this:
  - "AI models achieve 2.5 times higher risk-adjusted returns than traditional methods."
  - "NLP sentiment analysis can generate 3.8% annual excess returns."
  - "Reinforcement learning reduces transaction costs by 27%."
  - "Explainable AI is crucial for building user trust in financial systems."
  - "Hybrid models with human oversight are the future of automated financial advice."
```
---

## Paper 43: Lu, Yifei et al_summarized.md

**Source File:** `Lu, Yifei et al_summarized.md`

```yaml
paper_id: 10.51903/jtie.v4i3.466
designation: international-algorithm-specific
title: A Constrained, Data-Driven Budgeting Framework Integrating Macro Demand Forecasting and Marketing Response Modeling
authors: Lu, Y.; Zhou, H.; Zhang, Y.
year: 2025
venue: Journal of Technology Informatics and Engineering (JTIE)
odin_topics:
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 7.C
  - 7.D
  - 12.A
  - 12.B
  - 12.C
tldr: A framework integrating macro demand forecasting, marketing response modeling, and constrained optimization allocates marketing spend under SG&A and cash-flow constraints, demonstrating that optimal budgets often fall below ratio caps due to diminishing returns and demand uncertainty.
problem_and_motivation: Budgeting requires combining heterogeneous signals (macro demand, marketing effectiveness, accounting constraints) into a single auditable decision process. Existing approaches treat these components separately, leading to plans that violate ratio constraints under demand uncertainty. A unified pipeline linking forecasting, response modeling, and optimization is needed to produce defensible and constraint-aware recommendations.
approach:
  - Quarterly Personal Consumption Expenditures components from FRED (2010Q1-2025Q3) serve as macro demand proxy.
  - Four forecasting models are compared in a rolling backtest: seasonal naïve, SARIMAX, gradient boosting, and multivariate VAR.
  - Marketing response is estimated from the Advertising dataset (TV, radio, newspaper spend) using OLS, ridge, lasso, gradient boosting, and a Hill saturation model.
  - Constraints (gross margin, SG&A ratio, operating cash-flow coverage) are calibrated from Apple Inc.'s FY2025 Form 10-K.
  - Budget allocation is solved via grid search over channel shares and budget utilization, evaluated with 500 Monte Carlo scenarios under demand uncertainty.
  - Risk aversion is incorporated via a mean-risk objective with parameter λ to trade off expected profit and volatility.
findings:
  - "num: Multivariate VAR achieves ≈2.85% MAPE for aggregate demand, outperforming seasonal naïve (≈6.06% MAPE)."
  - "num: The Hill saturation model identifies newspaper spend as having near-zero marginal return (coefficient ≈0)."
  - "num: The risk-neutral optimizer allocates 25% to TV and 75% to radio, spending ≈0.97% of revenue, below the 1.5% SG&A cap."
  - "num: Spending at the deterministic cap would violate the SG&A constraint in ≈40% of scenarios due to revenue uncertainty, while the optimized spend maintains 100% satisfaction."
  - Marketing response curves exhibit strong diminishing returns, with radio saturating quickly and TV providing moderate marginal returns.
key_figures_tables:
  - "Table 7: Category-level forecast accuracy shows VAR achieves lowest RMSE for durables (97.24) and services (731.35) → multivariate models improve over seasonal baseline."
  - "Table 4: Marketing model comparison shows gradient boosting best predictive fit (CV_RMSE=0.661), but Hill model provides interpretable saturation curves."
  - "Figure 5: Hill-model marginal response curves show radio has highest marginal ROI at low spend, newspaper near-zero → allocate initial dollars to radio, then diversify."
  - "Figure 6: Profit-risk frontier under demand uncertainty shows trade-off between expected profit and volatility, with risk-neutral point highlighted."
  - "Table 12: Sensitivity to marketing cap shows optimizer spend unchanged for caps ≥1.5% due to diminishing returns binding before cap."
key_equations:
  - equation: "Sales(s) = β0 + Σ_i β_i h(s_i; α_i, γ_i)"
    explanation: Hill saturation function for diminishing returns per channel.
  - equation: "Π(b) = (g - o)(R + ΔR(b)) - Σ_i b_i"
    explanation: Operating profit equals margin on incremental revenue minus marketing spend.
  - equation: "ℙ(B ≤ κ R) ≥ 1 - δ"
    explanation: Chance constraint bounds violation probability for ratio-based caps.
definitions:
  - term: PCE
    definition: Personal Consumption Expenditures
  - term: FRED
    definition: Federal Reserve Economic Data
  - term: SARIMAX
    definition: Seasonal Autoregressive Integrated Moving Average with eXogenous regressors
  - term: VAR
    definition: Vector Autoregression
  - term: SG&A
    definition: Selling, General and Administrative expenses
  - term: FP&A
    definition: Financial Planning and Analysis
  - term: MMM
    definition: Marketing Mix Modeling
  - term: ROI
    definition: Return on Investment
  - term: MAPE
    definition: Mean Absolute Percentage Error
  - term: RMSE
    definition: Root Mean Squared Error
  - term: CFO
    definition: Cash Flow from Operations
critical_citations:
  - "[Box et al., 2015] — Foundational time series forecasting reference."
  - "[Hanssens et al., 2001] — Marketing response and saturation modeling."
  - "[Markowitz, 1952] — Mean-variance optimization for risk-return trade-off."
  - "[Bertsimas & Sim, 2004] — Robust optimization under uncertainty."
  - "[James et al., 2021] — Source of Advertising dataset and regression methods."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Compares SARIMAX, VAR, and gradient boosting for sequential demand forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Evaluates rolling-window forecasting algorithms with explicit accuracy metrics.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Directly addresses FP&A budgeting with constrained resource allocation.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: Provides an optimization framework that outputs recommended budget allocations.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: high
      justification: Solves a constrained portfolio problem with SG&A and cash-flow guardrails.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: medium
      justification: Discusses chance constraints and buffers but does not implement a formal reduction hierarchy.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses rolling backtests and Monte Carlo evaluation to assess forecast and recommendation performance.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Compares forecasting and response models using cross-validation and RMSE/MAPE.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Evaluates budget recommendations via constraint satisfaction rates and profit-risk trade-offs.
  contribution: For Odin's forecasting module (6.A/6.B), the paper provides a comparison of SARIMAX, VAR, and gradient boosting on quarterly time series, demonstrating that multivariate models improve accuracy over seasonal baselines. For the budget recommendation module (7.A/7.B/7.C), the paper offers a constrained optimization framework with explicit accounting constraints (SG&A ratio, cash-flow coverage) and shows that optimal budgets may fall below caps due to diminishing returns and demand uncertainty. For evaluation (12.A/12.B/12.C), the paper's rolling backtest protocol and Monte Carlo constraint-satisfaction analysis provide a template for assessing model performance and recommendation robustness. The paper's use of audited financial statements (Apple 10-K) to calibrate constraints also informs how Odin might incorporate user-specific financial ratios.
  directly_justifies:
    - "Multivariate VAR forecasting improves aggregate demand accuracy over seasonal naïve (≈2.85% vs 6.06% MAPE)."
    - "Marketing response curves exhibit strong diminishing returns; newspaper spend shows near-zero marginal ROI."
    - "Optimal budget may be below a ratio cap because spending at the cap violates constraints under demand uncertainty in ≈40% of scenarios."
    - "A risk-neutral optimizer allocates 25% to TV and 75% to radio under a 1.5% SG&A cap."
    - "Sensitivity to marketing effectiveness shows that higher ROI leads to cap-level spending, reducing SG&A satisfaction to ≈60%."
  limits:
    - "Data sources (PCE, Advertising.csv, Apple 10-K) are not internally consistent; sales-to-revenue normalization is stylized."
    - "Marketing response is treated as contemporaneous; real advertising carryover effects are omitted."
    - "The Advertising dataset is cross-sectional and small (N=200), limiting generalizability of response curves."
    - "Forecast evaluation uses latest-vintage PCE data, which may overstate real-time performance."
    - "Fiscal vs calendar quarter alignment is abstracted away."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The following domains were flagged as relevant: Spending Forecasting (6.A, 6.B) with high relevance because the paper compares four forecasting models (SARIMAX, VAR, gradient boosting) on sequential time series data and reports accuracy; Budget Recommendation (7.A, 7.B, 7.C) with high relevance because the paper directly addresses budget allocation optimization under constraints and evaluates recommended budgets; System Evaluation (12.A, 12.B, 12.C) with medium relevance because the paper uses rolling backtests, cross-validation, and Monte Carlo evaluation to assess models and recommendations. Topic 7.D (Infeasibility Handling) was assigned medium relevance because the paper discusses chance constraints and buffers but does not implement a formal reduction hierarchy. The following domains were considered and rejected: Filipino Cultural Context (2.A-2.D) because the paper is set in a generic corporate FP&A context with no Philippine focus; Expense Categorization (3.A-3.C) because it deals with marketing channels rather than personal expense categories; Behavioral Profiling (5.A-5.C) because no user behavior profiling is present; Mobile-First Design (9.A-9.B) and Data Privacy (10.A-10.B) are absent; Retention (11.A-11.B) is not addressed; Savings and Debt Management (13.A-13.C) is not relevant. Overall, the paper provides high relevance for forecasting and budget optimization modules, and medium relevance for evaluation methodologies.
limitations:
  - "Data sources (PCE, Advertising.csv, Apple 10-K) are not internally consistent; sales-to-revenue normalization is stylized."
  - "Marketing response is treated as contemporaneous; real advertising carryover effects are omitted."
  - "The Advertising dataset is cross-sectional and small (N=200), limiting generalizability of response curves."
  - "Forecast evaluation uses latest-vintage PCE data, which may overstate real-time performance."
  - "Fiscal vs calendar quarter alignment is abstracted away."
remember_this:
  - "num: Multivariate VAR achieves ≈2.85% MAPE for aggregate demand forecasting."
  - "num: Optimal spend is ≈0.97% of revenue, below the 1.5% SG&A cap due to diminishing returns."
  - "num: Spending at the deterministic cap violates SG&A constraints in ≈40% of scenarios under demand uncertainty."
  - "Marketing response curves show radio has highest marginal ROI at low spend, newspaper near-zero."
```
---

## Paper 44: Dewi_summarized.md

**Source File:** `Dewi_summarized.md`

```yaml
paper_id: 10.70764/gdpu-jbfi.2025.1(2)-09
designation: international
title: Financial Literacy and Digital Savings Behavior of Gen Z in the Fintech Era: A Systematic Literature Review
authors: Dewi, A. K.
year: 2025
venue: Journal of Banks and Financial Institutions
odin_topics:
  - 1.C
  - 2.A
  - 2.B
  - 3.B
  - 5.A
  - 6.A
  - 7.A
  - 13.A
tldr: Financial literacy and fintech synergistically shape Gen Z's saving behavior through cognitive foundations and digital facilitation, improving financial resilience.
problem_and_motivation: Gen Z exhibits high digital adoption but low financial literacy, creating a gap between fintech access and effective saving behavior. This paradox undermines long-term financial resilience and sustainable saving habits. Prior literature lacks a synthesized framework integrating financial literacy with fintech's role for this demographic.
approach:
  - Conducted a Systematic Literature Review (SLR) of articles from 2020–2025.
  - Searched Scopus, Emerald, Elsevier, MDPI, ProQuest, and Taylor & Francis databases.
  - Used keywords: financial literacy, digital savings, Gen Z, fintech, and related terms.
  - Applied title/abstract screening, full-text review, and eligibility analysis.
  - Retained 6 high-quality articles that met specific inclusion criteria.
findings:
  - Financial literacy is a cognitive and affective foundation for healthy financial decisions.
  - Fintech facilitates savings through auto-debit, transparency, gamification, and real-time tracking.
  - Synergy between financial literacy and fintech strengthens sustainable saving behavior.
  - Low financial literacy can lead to impulsive consumption despite fintech access.
  - Integration of financial education with fintech is more effective than either alone.
  - Digital financial literacy directly influences Gen Z's saving behavior.
  - Fintech adoption expands access but requires literacy for optimal use.
  - Gamification and automation in fintech apps encourage saving discipline.
key_figures_tables:
  - Figure 1: SLR Process diagram showing article reduction from 250 to 6 → highlights rigorous screening and specific focus.
  - Figure 2: Conceptual framework linking financial literacy, fintech features, and saving behavior → illustrates causal pathway.
  - Table 1: SLR Flow with exclusion reasons → demonstrates methodological transparency and selection criteria.
  - Table 2: Characteristics of 6 reviewed studies → summarizes key findings and methods.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Financial Literacy
    definition: Knowledge, skills, confidence, and motivation to manage finances wisely.
  - term: Fintech
    definition: Financial technology providing digital services like payments, savings, and investments.
  - term: Generation Z
    definition: Individuals born between 1997 and 2012, digital natives.
  - term: Digital Savings
    definition: Saving activities using fintech platforms for easy access and management.
  - term: SLR
    definition: Systematic Literature Review, a method for synthesizing empirical evidence.
critical_citations:
  - "[Huston, 2010] — foundational definition of financial literacy."
  - "[Morgan, 2022] — fintech's role in financial inclusion."
  - "[Andiani & Maria, 2023] — fintech and literacy impact on Gen Z behavior."
  - "[Mubarokah et al., 2024] — digital literacy influences saving behavior."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly addresses saving behavior and financial decision-making of Gen Z.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Discusses Indonesian context, applicable to Filipino cultural practices.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Mentions consumption patterns but does not focus on seasonal cycles.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: Informs design of fintech features like categorization and tracking.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Profiles Gen Z's saving behavior and literacy-driven profiles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: low
      justification: Does not discuss predictive modeling; focuses on behavioral correlates.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Implicitly supports budgeting through financial literacy and planning.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: Directly relevant to digital savings behavior and goal-setting.
  contribution: This paper provides a conceptual framework linking financial literacy and fintech to Gen Z's saving behavior, which justifies Odin's focus on integrating educational content with digital tools. It supports the design of behavioral profiling modules by identifying key determinants of saving habits. The findings validate Odin's approach to using gamification and real-time feedback for user engagement. It also underscores the importance of trust and transparency in fintech features, aligning with Odin's privacy and UX principles.
  directly_justifies:
    - "Financial literacy is a cognitive foundation for healthy saving behavior among Gen Z."
    - "Fintech features like gamification and auto-debit increase saving discipline."
    - "Synergy between literacy and fintech reduces reliance on high-cost loans."
    - "Digital financial literacy directly improves saving behavior and financial planning."
  limits:
    - "Systematic review synthesizes existing studies, not primary empirical data."
    - "Limited to 6 articles, reducing generalizability."
    - "Focus on Indonesian Gen Z, may not fully represent Filipino context."
    - "Does not evaluate specific algorithms or forecasting models."
    - "Lacks quantitative effect sizes for literacy-fintech interaction."
  mapping_rationale: The systematic scan across all 12 functional domains and their associated topic codes identified strong relevance to Financial Behavior (1.C), Behavioral Profiles (5.A), and Savings & Debt Management (13.A), all assigned high relevance due to direct discussion of saving behavior and fintech's role. Medium relevance was assigned to Culturally Specific Practices (2.A) and Expense Category Design (3.B) given the Indonesian context and fintech feature implications. Budgeting Strategies (7.A) received medium relevance for its implicit support of planning. Low relevance was assigned to Predictive Modeling (6.A) as the paper reviews behavioral correlates, not forecasting. Domains like Anomaly Detection (8.A), Mobile-First Design (9.A), Data Privacy (10.A), Retention (11.A), and Evaluation (12.A) were rejected as the paper does not address them. Borderline cases like seasonal spending (2.B) were noted but not selected due to lack of explicit focus. Overall, the paper provides a behavioral foundation for Odin's financial literacy and engagement modules but offers limited technical or algorithmic insights.
limitations:
  - "Limited to 6 articles, reducing generalizability of findings."
  - "Focus on Indonesian Gen Z may not fully represent Filipino context."
  - "Systematic review synthesizes existing studies, not primary empirical data."
  - "Does not evaluate specific algorithms or forecasting models."
  - "Lacks quantitative effect sizes for literacy-fintech interaction."
remember_this:
  - "Financial literacy and fintech synergistically improve Gen Z's saving behavior."
  - "Fintech features like gamification and automation encourage saving discipline."
  - "Digital financial literacy is a key determinant of saving behavior."
  - "Low literacy can negate fintech benefits, leading to impulsive consumption."
  - "Integrating education with fintech yields more effective financial behavior change."
```
---

## Paper 45: Mariano & Monreal_summarized.md

**Source File:** `Mariano & Monreal_summarized.md`

```yaml
paper_id: "10.1145/3785171.3785187"
designation: "local-algorithm-specific"
title: "Predict, Optimize, Deliver: Demand Forecasting and Resource Optimization for a Market Research Firm"
authors: "Mariano, M.T.G.; Monreal, R.N."
year: 2025
venue: "International Conference on Business and Information Management (ICBIM 2025)"
odin_topics:
  - "6.A"
  - "6.B"
  - "7.C"
  - "7.D"
  - "4.B"
tldr: "An integrated forecasting and optimization framework using Prophet and MILP improves resource allocation and cost efficiency in a market research firm."
problem_and_motivation: "Professional service firms face fluctuating demand and manual workforce planning fails to adapt, leading to inefficiencies. There is a need for a data-driven approach that selects appropriate forecasting methods and operationalizes them into optimal resource allocation under real-world constraints."
approach:
  - "Historical billable hours from a Manila-based service center (Jan 2018–Dec 2024) were used as the primary dataset."
  - "Four forecasting models (ARIMA, Holt-Winters, Prophet, LSTM) were tuned and evaluated using MAE, RMSE, and MAPE across multiple train-test splits and a 30-day holdout."
  - "Prophet achieved the lowest weighted error and was selected for its balance of accuracy, interpretability, and speed."
  - "A Pyomo-based MILP optimization model minimized excess resource hours subject to employee availability, work-hour caps, and client-specific demand constraints."
  - "Forecast bands derived from RMSE were incorporated to simulate over- and under-forecasting scenarios."
  - "The framework was deployed in an interactive PowerBI dashboard for dynamic workforce planning."
findings:
  - "num: Prophet achieved the lowest weighted error for Client 1 (13.038) and Client 2 (27.786) on a 30-day holdout."
  - "num: Prophet's overall weighted score (10.456) outperformed ARIMA (11.582), Holt-Winters (13.062), and LSTM (11.634)."
  - "The optimization model respected all constraints and achieved near-zero unmet demand across scenarios."
  - "Resource utilization averaged up to 106% for shared staff in over-forecasting scenarios, indicating tight capacity."
  - "Cumulative costs increased significantly with forecast errors, highlighting the value of accurate short-term forecasting."
key_figures_tables:
  - "Table 3: Summary of weighted error metrics for each model and client → Prophet has lowest error for both clients."
  - "Table 4: Overall model selection scores → Prophet ranks first due to accuracy and interpretability."
  - "Table 5: Optimized average resource utilization per employee under three scenarios → utilization varies widely, with S2 at 106% under over-forecast."
  - "Figure 5: Resource distribution by forecast scenario → shared resources absorb variability; dedicated analysts have fixed loads."
  - "Figure 6: Cumulative allocation cost by forecast scenario → small forecast errors compound into significant cost gaps."
  - "Figure 7: Resource mapping and utilization dashboard → interactive visualizations enable agile decision-making."
key_equations:
  - equation: "min \\sum_{t} (C_{regular} \\sum_{i} x_{i,C1,t} + C_{overtime} \\sum_i o_{i,t} + C_{penalty} (E_{1,t-1} + E_{2,t-1}))"
    explanation: "Minimizes total cost from regular hours, overtime, and penalties for unmet demand."
definitions:
  - term: "ARIMA"
    definition: "Autoregressive Integrated Moving Average, a classical time-series model for stationary data."
  - term: "LSTM"
    definition: "Long Short-Term Memory, a recurrent neural network for sequential data."
  - term: "Prophet"
    definition: "Open-source forecasting model from Facebook that decomposes trend, seasonality, and holiday effects."
  - term: "MILP"
    definition: "Mixed-Integer Linear Programming, an optimization method with integer and continuous variables."
  - term: "MAE"
    definition: "Mean Absolute Error, a metric for forecast accuracy."
  - term: "RMSE"
    definition: "Root Mean Squared Error, penalizing large errors."
  - term: "MAPE"
    definition: "Mean Absolute Percentage Error, relative error metric."
critical_citations:
  - "[Boadi-Sarpong et al., 2023] — resource allocation strategies for competitiveness."
  - "[Sharma & Singh, 2022] — forecasting resource fulfilment in IT consulting."
  - "[Wang et al., 2024] — network flow approach to scheduling."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Compares multiple predictive models (ARIMA, Prophet, LSTM) for demand forecasting, directly informing predictive modeling in PFMS."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Evaluates specific forecasting algorithms and their performance metrics, providing evidence for algorithm selection in spending forecasting."
    - code: "7.C"
      name: "Constrained Optimization Approaches for Budget Allocation"
      relevance: "high"
      justification: "Uses constrained MILP to allocate resources under demand and capacity constraints, analogous to budget allocation optimization."
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "medium"
      justification: "Introduces forecast bands from RMSE to handle demand uncertainty, simulating infeasibility and improving robustness."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "low"
      justification: "Critiques manual Excel-based planning and highlights gaps in adapting to demand volatility, relevant to limitations of existing PFMS."
  contribution: "The forecasting comparison (6.A, 6.B) provides a methodology for selecting models for spending prediction in Odin's forecasting module. The constrained optimization model (7.C) directly informs Odin's budget recommendation engine by demonstrating how to allocate limited resources under multiple constraints. The use of forecast bands (7.D) offers a strategy for handling infeasibility, which can be adapted for Odin's budget adjustment recommendations. The PowerBI dashboard visualization, though not mobile-focused, illustrates how interactive data exploration can support user engagement and decision transparency."
  directly_justifies:
    - "Prophet offers a balance of accuracy and interpretability suitable for operational forecasting in resource-constrained settings."
    - "Constrained optimization with MILP can allocate resources to meet demand while respecting work-hour caps and employee availability."
    - "Forecast bands derived from RMSE improve allocation resilience by simulating over- and under-forecasting."
  limits:
    - "The study focuses on resource allocation for a firm, not individual spending behavior or personal financial management."
    - "The optimization model assumes cost minimization, not personalized budget constraints or savings goals."
    - "Results are based on a single market research firm, limiting generalizability to other PFMS contexts."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains flagged as relevant were Spending Forecasting (6.A, 6.B) and Budget Recommendation (7.C, 7.D) due to the paper's focus on predictive modeling and constrained optimization. The Existing Systems domain (4.B) was also noted for its critique of manual planning, though with low relevance. Other domains (Filipino Cultural Context, Expense Categorization, Behavioral Profiling, Anomaly Detection, Mobile Design, Data Privacy, Retention, System Evaluation, Savings/Debt) were considered and rejected because the paper does not address those aspects. Borderline cases: seasonal spending patterns (2.B, 2.D) were touched upon via time-series decomposition but not emphasized, so they were excluded. Overall, the paper provides strong technical evidence for forecasting and optimization modules in Odin."
limitations:
  - "The analysis was restricted to output-based variables (billable hours) and did not include input-level factors like individual analyst skill."
  - "The forecasting model used internal historical data only and did not incorporate external economic indicators that may influence demand."
  - "Caution is warranted for long-range forecasting as the model does not account for rare high-impact events such as pandemics."
  - "The effectiveness of the proposed system is highly dependent on consistent and accurate updating of time-tracking data."
remember_this:
  - "Prophet achieved the lowest weighted error (10.456) among four models."
  - "MILP optimization respected all constraints and achieved near-zero unmet demand."
  - "Forecast errors compound costs significantly, emphasizing short-term planning."
  - "Interactive dashboards enable agile workforce planning."
```
---

## Paper 46: Compagnino et al_summarized.md

**Source File:** `Compagnino et al_summarized.md`

```yaml
paper_id: 10.3390/app152111787
designation: international
title: An Introduction to Machine Learning Methods for Fraud Detection
authors: Compagnino, A.A.; Maruccia, Y.; Cavuoti, S.; Riccio, G.; Tutone, A.; Crupi, R.; Pagliaro, A.
year: 2025
venue: Applied Sciences
odin_topics:
  - 8.A
  - 8.B
  - 8.C
  - 6.A
  - 6.B
  - 10.A
  - 10.B
  - 1.A
tldr: A systematic review of machine learning techniques for financial fraud detection, analyzing supervised, unsupervised, and deep learning approaches with case studies on real-world banking data.
problem_and_motivation: Financial fraud causes substantial economic damage and traditional detection methods are increasingly inadequate against evolving sophisticated schemes. A significant gap exists between academic research on ML-based fraud detection and its practical, operational application in real-world financial environments.
approach:
  - A systematic literature review was conducted across Scopus, IEEE Xplore, ACM Digital Library, and Web of Science.
  - The review synthesizes findings from over 120 peer-reviewed articles published between January 2014 and December 2023.
  - The paper categorizes financial fraud types, reviews ML approaches, and examines commonly used datasets and performance metrics.
  - Two case studies apply supervised models (Random Forest, XGBoost, ExtraTrees) to proprietary real-world banking datasets.
  - The experimental setup includes temporal splits, stratified k-fold cross-validation, and hyperparameter tuning via randomized search.
findings:
  - Supervised learning is the predominant approach, accounting for 57% of techniques employed in the reviewed literature.
  - Random Forest emerges as the most widely adopted technique, appearing in 34 studies with accuracy rates often exceeding 95%.
  - num: The case study on bank transfers achieved a fraud recall of only 0.36 on a test set with 3.39% fraud prevalence, even with class weights.
  - num: In the first case study, Random Forest achieved an AUPRC of 0.619 but a fraud recall of only 0.34 at the default threshold.
  - Extreme class imbalance is a fundamental challenge, with fraudulent transactions typically less than 1% of all transactions.
  - The study confirms that standard supervised models, even with hyperparameter tuning, are often insufficient for robust operational fraud detection.
key_figures_tables:
  - Table 1: Comparative analysis of ML approaches → Summarizes algorithm advantages, disadvantages, complexity, and interpretability.
  - Table 2: SOTA micro-benchmark on ULB 2013 → Shows XGBoost and RF lead AUPRC on a standard dataset.
  - Table 3: Summary of banking dataset characteristics → Shows 48,559 instances with ~1.43% fraud rate.
  - Table 4: Case Study 1 results → Shows Random Forest achieves best AUPRC of 0.619 and Recall@0.5% of 0.202.
  - Table 5: Case Study 2 results → Shows class_weight adjustments did not improve fraud recall significantly.
  - Figure 1: PR curve for Random Forest in Case Study 1 → Average precision (AUPRC) is 0.619.
  - Figure 2: PR curve for Random Forest in Case Study 2 → Average precision (AUPRC) is 0.697.
key_equations:
  - equation: "Accuracy = (TP + TN) / (TP + TN + FP + FN)"
    explanation: Measures overall correct predictions but is misleading for imbalanced data.
  - equation: "Precision = TP / (TP + FP)"
    explanation: Measures the proportion of flagged transactions that are actually fraudulent.
  - equation: "Recall = TP / (TP + FN)"
    explanation: Measures the proportion of actual frauds that are correctly detected.
  - equation: "F1-Score = (2 * Precision * Recall) / (Precision + Recall)"
    explanation: Harmonic mean balancing precision and recall, useful for imbalanced data.
  - equation: "AUC-ROC = ∫ TPR(FPR^-1(t)) dt"
    explanation: Evaluates model's discrimination ability across different thresholds.
  - equation: "OutputSize = floor((InputSize + 2*Padding - KernelSize) / Stride) + 1"
    explanation: Formula for calculating output dimensions after a convolution operation.
definitions:
  - term: XAI
    definition: Explainable Artificial Intelligence, methods for making model decisions transparent.
  - term: Concept Drift
    definition: The change in the relationship between features and target variable over time.
  - term: Federated Learning
    definition: Training a shared model across decentralized data sources without raw data exchange.
  - term: SMOTE
    definition: Synthetic Minority Over-sampling Technique to balance imbalanced datasets.
  - term: GAN
    definition: Generative Adversarial Network, two competing neural networks for generating synthetic data.
  - term: AUPRC
    definition: Area Under the Precision-Recall Curve, a metric for imbalanced classification.
  - term: SHAP
    definition: SHapley Additive exPlanations, a method for explaining model predictions.
critical_citations:
  - "[Dal Pozzolo et al., 2022] — Provides key lessons on concept drift and calibration in fraud detection."
  - "[Ahmed et al., 2016] — Foundational survey on anomaly detection techniques in the financial domain."
  - "[Saito and Rehmsmeier, 2015] — Establishes AUPRC as more informative than ROC for imbalanced data."
  - "[Lucas et al., 2020] — Covers automated feature engineering challenges for credit card fraud detection."
  - "[Fiore et al., 2019] — Demonstrates use of GANs for improving classification effectiveness in fraud detection."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly addresses anomaly detection for identifying fraudulent financial transactions.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Reviews and benchmarks specific algorithms like Isolation Forest and autoencoders.
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: medium
      justification: Discusses unsupervised methods like autoencoders that are relevant for cold-start scenarios.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Provides context on forecasting challenges due to concept drift and temporal data.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: Reviews LSTM and RNNs for sequential transaction data, applicable to spending forecasting.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Discusses federated learning and privacy concerns with centralized sensitive data.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: Mentions explainability and bias as trust factors but not as a primary focus.
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Provides general fraud detection context; no specific focus on Filipino demography.
  contribution: This review provides a comprehensive catalog of ML techniques for fraud detection, including a systematic performance comparison on standard datasets and a detailed evaluation of supervised models on proprietary banking data. The paper's analysis of concept drift and data imbalance is directly applicable to Odin's spending forecasting and anomaly detection modules. The case studies offer practical insights into model limitations, particularly the low recall challenge, which informs Odin's need for robust anomaly handling. The discussion on federated learning and XAI provides actionable guidance for Odin's data privacy and user trust design considerations.
  directly_justifies:
    - "Fraudulent transactions typically constitute less than 1% of all transactions, making it exceptionally difficult for models to learn discriminative features."
    - "Extreme class imbalance requires specialized techniques like SMOTE or cost-sensitive learning."
    - "Concept drift renders models trained on historical data obsolete as fraudsters continuously evolve tactics."
    - "Explainability is not just desirable but a critical compliance requirement for financial systems."
  limits:
    - "The case studies use proprietary banking data, limiting replicability and generalizability."
    - "The paper primarily reviews tree-based and traditional ML models, with less depth on graph-based or hybrid approaches."
    - "The systematic review excludes studies from 2024 and 2025."
    - "The paper does not address region-specific cultural or financial behaviors."
    - "The evaluation focuses on fraud detection, not personal finance management or budgeting."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The domain most directly relevant is Anomaly Detection, with topic codes 8.A, 8.B, and 8.C flagged as high relevance due to the paper's core focus on identifying fraudulent transactions. Predictive Modeling (6.A, 6.B) was flagged as medium relevance because the paper's discussion of temporal data and sequential models (LSTM, RNN) is directly applicable to spending forecasting. Data Privacy (10.A, 10.B) was assigned medium relevance due to substantial sections on federated learning and explainability. Filipino Cultural Context (2.A-D) and Behavioral Profiling (5.A-C) were rejected as the paper does not address cultural behaviors or user profiling. The topic 1.A (Demographic) was considered contextual only. Borderline cases included the overlap between anomaly detection and predictive modeling, resolved by classifying algorithm-specific discussions under 8.B and forecasting-specific challenges under 6.B.
limitations:
  - "The use of PCA-transformed features in many public datasets obscures interpretability and limits domain knowledge integration."
  - "Most studies report high accuracy but fail to address the critical operational trade-off between precision and recall."
  - "The adversarial nature of fraud is under-addressed; models are not evaluated against adaptive fraudsters."
  - "The case studies demonstrate that standard class_weight adjustments are insufficient for extreme imbalance."
  - "The field lacks standardized benchmarks and recent publicly accessible fraud datasets. [unacknowledged]"
remember_this:
  - "Random Forest models achieve high accuracy but low recall on imbalanced fraud data."
  - "Class weight adjustments alone do not solve the extreme class imbalance problem."
  - "Model interpretability is a legal and operational requirement in financial systems."
  - "Federated learning enables cross-institutional collaboration without sharing sensitive data."
  - "Concept drift requires adaptive models that can detect evolving fraud patterns in real-time."
```
---

## Paper 47: Mamun_summarized.md

**Source File:** `Mamun_summarized.md`

```yaml
paper_id: 10.63125/9b316w70
designation: international
title: Advancements in Machine Learning for Customer Retention: A Systematic Literature Review of Predictive Models and Churn Analysis
authors: Mamun, M. N. H.
year: 2025
venue: Journal of Sustainable Development and Policy
odin_topics:
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 8.A
  - 10.A
  - 10.B
  - 12.A
  - 12.B
  - 12.C
tldr: A systematic review of 112 studies finds ensemble and deep learning models consistently outperform traditional classifiers for churn prediction, especially when integrating behavioral and sentiment features.
problem_and_motivation: Customer churn leads to billions in annual revenue loss, yet traditional statistical models cannot capture the nonlinear relationships in modern behavioral data. Organizations need predictive tools that identify at-risk customers for proactive, cost-effective retention interventions in saturated markets.
approach:
  - Conducted a systematic literature review following PRISMA guidelines.
  - Searched six major academic databases for studies on ML-based churn prediction published between 2005 and 2025.
  - Retrieved 1,268 articles, screened to 116 empirical studies for meta-analysis.
  - Coded studies by algorithm type, evaluation metrics, dataset, and industry domain.
  - Used random-effects meta-analysis to pool performance metrics like AUC-ROC and F1-score.
findings:
  - num: Ensemble methods (gradient boosting, random forests) show the highest pooled AUC-ROC and F1-scores across industries.
  - num: Deep learning models (LSTM, CNN) significantly outperform classical algorithms on sequential behavioral data.
  - num: Feature engineering with RFM and engagement features improves model performance more than algorithmic choice alone.
  - num: Models using SMOTE and cost-sensitive learning achieve higher recall in imbalanced churn datasets.
  - num: Deep learning models can reduce false-negative churn predictions by up to 30% relative to static feature models.
  - num: AUC-ROC values for high-performing models consistently exceed 0.80, with F1-scores above 0.70.
  - num: Incorporating sentiment analysis features improves recall by over 8% in some studies.
  - num: Public datasets like IBM Telco Churn provide standardized benchmarks with reported AUC-ROC ranges of 0.75-0.90 for ensemble models.
  - num: CNN-based detectors have shown up to a ten-point gain in AUC-ROC over gradient boosting machines on unstructured log data.
  - Interpretability tools like SHAP and LIME are increasingly adopted to bridge transparency gaps in black-box models.
key_figures_tables:
  - "Figure 1: Theoretical Framework for ML-Based Retention → Shows data sources and ML models driving retention strategies."
  - "Figure 2: ML-Driven Churn Prediction Process → Illustrates the pipeline from data preprocessing to model deployment."
  - "Figure 3: ML-Driven Customer Retention and Churn Prediction → Highlights integration of ML into CRM systems."
  - "Figure 9: Key Metrics and Validation Techniques → Visualizes how AUC-ROC, F1, and lift charts are used to evaluate models."
  - "Figure 15: Pooled Performance Metrics → Compares AUC-ROC and F1-scores across different algorithm classes."
  - "Table: None specified in the text."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Churn
    definition: The cessation or significant reduction of a customer's commercial activity within a predefined observation window.
  - term: Customer Retention
    definition: A firm's capacity to sustain an ongoing commercial relationship with a buyer over time.
  - term: RFM
    definition: Recency, Frequency, Monetary value – a framework for customer segmentation and behavior analysis.
  - term: AUC-ROC
    definition: Area Under the Receiver Operating Characteristic Curve, measuring a model's ability to distinguish between classes.
  - term: SHAP
    definition: SHapley Additive exPlanations, a tool for explaining predictions of machine learning models.
  - term: LIME
    definition: Local Interpretable Model-agnostic Explanations, a technique to explain individual predictions.
  - term: SMOTE
    definition: Synthetic Minority Over-sampling Technique, used to address class imbalance by generating synthetic samples.
  - term: CLV
    definition: Customer Lifetime Value, the total worth of a customer to a business over the entire relationship.
  - term: GBM
    definition: Gradient Boosting Machine, an ensemble learning technique that builds models sequentially to correct errors.
  - term: XAI
    definition: Explainable Artificial Intelligence, a set of tools and techniques to make AI decisions understandable to humans.
critical_citations:
  - "[Jajam et al., 2023] — Demonstrates effectiveness of ensemble deep learning for churn prediction."
  - "[Zhu et al., 2023] — Shows bagging-based ensembles improve performance on imbalanced data."
  - "[Sikri et al., 2024] — Confirms ensemble models enhance customer retention in telecom."
  - "[Boozary et al., 2025] — Compares ensemble models for accurate churn prediction."
  - "[Coussement & De Bock, 2013] — Establishes ensemble learning benefits for customer churn prediction."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: "Reviews ML-based churn models widely used in financial services, contextualizing PFMS analytics."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: "Identifies gaps in traditional models and highlights need for real-time, privacy-preserving ML systems."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: "Directly addresses modeling customer behavior for classification and churn prediction."
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: contextual
      justification: "Mentions concept drift and need for retraining, but does not focus on cold-start scenarios."
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: "Comprehensively reviews supervised, unsupervised, and hybrid classification methods for churn."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: "Core focus on predictive modeling, forecasting churn using historical behavioral data."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: "Reviews LSTM, RNN, and TCN for time-series forecasting, directly applicable to spending data."
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: "Discusses feature engineering (RFM) which is foundational for budget allocation and strategy design."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: "Variational autoencoders are mentioned for anomaly detection, a key technique for early churn warnings."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: "Discusses privacy-preserving techniques (federated learning, differential privacy) for compliance."
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: "Emphasizes interpretability (SHAP, LIME) to build user and managerial trust in AI predictions."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: "Dedicates significant analysis to evaluation metrics (AUC-ROC, F1, lift) and cross-validation strategies."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: "Meta-analytically compares performance of various ML algorithms for churn prediction."
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: "Methods for evaluating classification models (calibration, profit-based metrics) translate to budget rec systems."
  contribution: "This review provides a meta-analytic benchmark for selecting ML models in Odin's Behavioral Profiling module. It directly justifies using ensemble or deep learning models for the Spending Forecasting module's predictive engine. The detailed evaluation framework can be adopted for Odin's System Evaluation module to ensure robust model validation. The analysis of feature engineering (RFM, sentiment) guides the design of Odin's Expense Categorization and User Profile modules."
  directly_justifies:
    - "Ensemble and deep learning models consistently outperform traditional classifiers on behavioral data."
    - "AUC-ROC and F1-score are more reliable metrics than accuracy for imbalanced churn datasets."
    - "Feature engineering with recency, frequency, and monetary metrics significantly improves prediction."
    - "Privacy-preserving techniques like federated learning are viable for compliance-focused PFMS."
    - "Interpretability tools (SHAP, LIME) are essential for building user trust in financial recommendations."
  limits:
    - "The review is not specifically focused on personal finance management systems for Filipino users."
    - "Most reviewed studies rely on proprietary data, potentially limiting generalizability to local spending patterns."
    - "Performance metrics are averaged across industries; context-specific tuning for PFMS may be required."
  mapping_rationale: "A systematic scan across all 12 functional domains identified the paper's strongest relevance to Behavioral Profiling & Classification (5.A, 5.C), Spending Forecasting (6.A, 6.B), and System Evaluation (12.A, 12.B). Topics under Filipino Cultural Context (2.A-D) were considered but rejected as the review is global, with no specific focus on Filipino practices. Expense Categorization (3.A-C) and Budget Recommendation (7.A-D) received medium relevance because the paper covers classification and feature engineering techniques foundational to these modules, though it does not directly address category design or allocation constraints. Anomaly Detection (8.A) was flagged for its discussion of autoencoders, and Data Privacy (10.A-B) for its coverage of federated learning and SHAP. User Retention (11.A-B) was considered but rejected as the paper is about modeling churn, not designing engagement mechanisms. Overall, the paper provides strong theoretical and empirical justification for Odin's predictive modeling and evaluation framework, but requires localization for the Philippine context."
limitations:
  - "The study is a literature review and does not provide novel empirical validation on a new dataset."
  - "The meta-analysis pools results from studies with heterogeneous preprocessing methods, which may affect comparability. [unacknowledged]"
  - "The review may have publication bias, as it includes only peer-reviewed studies from major databases. [unacknowledged]"
  - "The findings are based on customer churn in general, not specifically on financial behavior for personal budgeting. [unacknowledged]"
remember_this:
  - "Ensemble models (GBM, Random Forest) are the gold standard for churn prediction across sectors."
  - "Deep learning (LSTM, CNN) excels when modeling sequential behavioral data."
  - "AUC-ROC > 0.80 and F1 > 0.70 indicate robust model performance for imbalanced data."
  - "Feature engineering (RFM, engagement) often improves accuracy more than algorithm selection."
  - "Interpretability (SHAP/LIME) is critical for trust and adoption in regulated financial systems."
```
---

## Paper 48: Chowdhury A. et al_summarized.md

**Source File:** `Chowdhury A. et al_summarized.md`

```yaml
paper_id: 10.63125/mbbfw637
designation: international
title: A SYSTEMATIC REVIEW OF DEMAND FORECASTING MODELS FOR RETAIL E-COMMERCE ENHANCING ACCURACY IN INVENTORY AND DELIVERY PLANNING
authors: Chowdhury, A. R.; Paul, R.; Rozony, F. Z.
year: 2025
venue: International Journal of Scientific Interdisciplinary Research
odin_topics:
  - 4.A
  - 4.B
  - 6.A
  - 6.B
  - 12.B
tldr: A systematic review of 72 studies categorizes demand forecasting models for e-commerce into statistical, machine learning, deep learning, and hybrid approaches, assessing their impact on inventory and delivery planning.
problem_and_motivation: Retail e-commerce demand forecasting faces challenges from volatile consumer behavior and complex logistics. Despite growing academic interest, there is a lack of comprehensive synthesis on the comparative effectiveness of various forecasting models. This gap hinders decision-makers in selecting appropriate models to improve inventory accuracy and delivery efficiency.
approach:
  - A systematic review was conducted following PRISMA guidelines to ensure transparency and rigor.
  - A comprehensive search across Scopus, Web of Science, IEEE Xplore, and ScienceDirect identified 284 articles published between 2010 and 2024.
  - Studies were screened based on relevance to e-commerce forecasting and inclusion of empirical performance evaluations, resulting in 72 eligible studies.
  - Data was extracted using a structured coding framework covering forecasting technique, dataset characteristics, and operational focus.
  - The synthesis categorized models into traditional statistical, machine learning, deep learning, and hybrid frameworks.
findings:
  - num: Traditional statistical models (ARIMA, SARIMA, Holt-Winters) were used in 21 of 72 reviewed studies, performing well for stable, seasonal demand.
  - num: Machine learning models appeared in 31 studies, improving forecast accuracy metrics like RMSE and MAPE by up to 20% over statistical methods.
  - num: Deep learning models (LSTM, GRU, CNN) were featured in 22 studies, excelling at capturing nonlinear patterns in high-volume e-commerce data.
  - num: Hybrid models (ARIMA + ML/DL) were the focus of 18 studies, combining interpretability with enhanced accuracy during promotional periods.
  - num: Integrating external data (weather, sentiment, social media) in 27 studies significantly improved forecast accuracy in volatile categories.
  - num: A 10% improvement in forecast accuracy is associated with a potential 25% reduction in inventory costs.
  - num: Deep learning models reduced overstock rates in high-SKU environments by up to 15% compared to traditional baselines.
  - Advanced machine learning models demonstrate high adaptability for short-term and medium-term forecasting.
  - Ensemble and hybrid strategies enhance robustness across volatile demand cycles and promotional events.
key_figures_tables:
  - Figure 1: Components of global e-commerce forecasting operations → Highlights integrated data sources and logistics synchronization.
  - Figure 2: Classical time series methods for retail forecasting → Shows application of ARIMA and smoothing techniques.
  - Figure 3: Major forecasting techniques used in demand forecasting → Categorizes traditional, ML, and hybrid models.
  - Figure 4: Foundational time series forecasting models → Illustrates ARIMA and exponential smoothing structures.
  - Figure 5: Machine learning models for nonlinear demand forecasting → Lists decision trees, random forests, and SVR.
  - Figure 6: Deep learning networks in retail forecasting → Shows LSTM, GRU, and CNN architectures.
  - Figure 7: Hybrid and ensemble forecasting approaches → Depicts ARIMA and ML/DL combination strategies.
  - Figure 8: Incorporating external signals in demand forecasting → Shows integration of weather and social media data.
  - Figure 9: Impact of forecasting accuracy on inventory replenishment decisions → Links forecast accuracy with inventory costs.
  - Figure 10: PRISMA methodology flowchart for study selection → Outlines the systematic review process.
key_equations:
  - equation: "RMSE = sqrt( (1/n) * sum_{t=1}^{n} (y_t - ŷ_t)^2 )"
    explanation: Measures forecast error, heavily penalizing large deviations.
  - equation: "MAPE = (1/n) * sum_{t=1}^{n} |(y_t - ŷ_t) / y_t| * 100"
    explanation: Scale-independent accuracy metric, useful for comparing products.
definitions:
  - term: ARIMA
    definition: AutoRegressive Integrated Moving Average, a statistical model for time series forecasting.
  - term: SARIMA
    definition: Seasonal ARIMA, extends ARIMA to account for seasonality in time series data.
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network capable of learning long-term dependencies.
  - term: GRU
    definition: Gated Recurrent Unit, a simpler recurrent neural network variant compared to LSTM.
  - term: CNN
    definition: Convolutional Neural Network, a deep learning model effective for detecting local patterns in data.
  - term: RMSE
    definition: Root Mean Squared Error, a metric that penalizes larger forecast errors.
  - term: MAPE
    definition: Mean Absolute Percentage Error, a scale-independent forecast accuracy metric.
  - term: SVR
    definition: Support Vector Regression, a machine learning model for nonlinear regression tasks.
  - term: TFT
    definition: Temporal Fusion Transformer, an attention-based model for interpretable time-series forecasting.
  - term: SKU
    definition: Stock Keeping Unit, a unique identifier for each distinct product and service.
critical_citations:
  - "[Bandara et al., 2019] — Highlights e-commerce demand differs from traditional retail."
  - "[Mosavi et al., 2020] — Deep learning methods show superior performance in economics."
  - "[Goedhart et al., 2023] — Modeling influence of returns for omni-channel retailers."
  - "[Gong, 2023] — Digital transformation of supply chain in retail and e-commerce."
  - "[Frei et al., 2022] — Mapping product returns processes in multichannel retailing."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides a landscape of forecasting models relevant to PFMS systems.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies limitations of traditional models in volatile e-commerce settings.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly reviews predictive modeling techniques for forecasting demand.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Comprehensively evaluates forecasting algorithms including LSTM and ARIMA.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Emphasizes empirical evaluation of forecasting models using metrics like RMSE and MAPE.
  contribution: This paper provides a structured taxonomy of forecasting models (statistical, ML, DL, hybrid) that Odin can directly adopt for its spending forecasting module. The comparative analysis of model performance under different data conditions (volatility, seasonality, promotional events) informs Odin's algorithm selection strategy for different user segments. Furthermore, the review's emphasis on hybrid models and external data integration offers a blueprint for Odin to enhance its forecasting accuracy and robustness. The discussion on practical evaluation metrics guides Odin's system evaluation framework for algorithmic performance.
  directly_justifies:
    - "Machine learning models improve forecast accuracy by up to 20% over statistical methods."
    - "Hybrid models combining ARIMA and LSTM reduce forecasting error during volatile periods."
    - "Integrating external variables like weather and sentiment significantly enhances forecast precision."
    - "Deep learning models capture nonlinearities and long-term dependencies in financial data."
    - "A 10% increase in forecast accuracy can reduce inventory costs by up to 25%."
  limits:
    - "The review focuses on retail e-commerce, not personal finance, so direct transferability of findings requires validation."
    - "The performance of advanced models (DL) depends on large datasets, which may not be available for new Odin users."
    - "Complexity and computational demands of deep learning models may hinder their deployment in mobile-first environments."
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The paper was flagged as highly relevant for the Spending Forecasting domain (topics 6.A, 6.B) because it directly reviews and compares various forecasting algorithms. It was considered relevant for Evaluation (topic 12.B) due to its detailed discussion of performance metrics. It provides contextual information for the Landscape of Existing Systems (4.A) and their Limitations (4.B), though these are not the paper's primary focus. Domains like Filipino Cultural Context, Expense Categorization, and Behavioral Profiling were considered and rejected as the paper does not address user behavior, cultural spending, or PFMS-specific categorization. Overall, the paper is highly relevant as an authoritative source on forecasting algorithms, offering insights into model selection, evaluation, and integration with external data.
limitations:
  - "The study's scope is limited to e-commerce retail, making direct application to personal finance forecasting an extrapolation."
  - "The review does not address the cold-start problem, a critical issue for personal finance applications with new users."
  - "The analysis of deep learning models focuses on accuracy without deeply exploring computational costs for mobile deployment."
  - "The systematic review synthesizes existing studies but does not present novel empirical experiments in the PFMS context."
  - "The review may underrepresent studies on interpretability and user trust, which are crucial for financial applications. [unacknowledged]"
remember_this:
  - "A 10% improvement in forecast accuracy can yield a 25% reduction in inventory costs."
  - "Machine learning models can cut forecasting error by up to 20% compared to traditional methods."
  - "Hybrid models balance interpretability and accuracy effectively for dynamic financial data."
  - "Integrating external data like sentiment and seasonality significantly improves forecasting robustness."
  - "Deep learning excels at capturing complex patterns in high-volume sequential transaction data."
```
---

## Paper 49: Santiago_summarized.md

**Source File:** `Santiago_summarized.md`

```yaml
paper_id: 10.26483/ijarcs.v16i3.7256
designation: local-algorithm-specific
title: BUDGET AND FINANCIAL MANAGEMENT INFORMATION SYSTEM FOR PUBLIC ELEMENTARY SCHOOLS: ANALYTICS AND PREDICTIVE INSIGHTS FOR MOOE ALLOCATION USING LINEAR REGRESSION
authors: Santiago, R. L. T.; Villarica, M. V.; Bernardino, M. P.
year: 2025
venue: International Journal of Advanced Research in Computer Science
odin_topics:
  - 1.A
  - 1.B
  - 2.D
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 7.C
  - 7.D
  - 8.A
  - 8.B
  - 9.A
  - 10.A
  - 10.B
  - 11.A
  - 12.B
tldr: Develops an AI-driven financial management system for Philippine public schools that uses linear regression to forecast Maintenance and Other Operating Expenses allocations.
problem_and_motivation: Public elementary schools in the Philippines face significant challenges in managing financial resources due to reliance on manual processes that are prone to errors, inefficiencies, and a lack of transparency. There is a lack of dedicated, digital financial management systems tailored to the operational needs of these schools. This study addresses the need for an automated, accountable, and data-driven solution to improve budget allocation, expenditure tracking, and compliance with DepEd regulations.
approach:
  - The system was developed using an Agile methodology, incorporating continuous stakeholder feedback from school administrators and DepEd auditors.
  - The core AI feature uses a linear regression model built with Python and Scikit-learn to forecast future MOOE allocations based on historical spending data.
  - The system includes modules for budget allocation, expenditure tracking with real-time dashboards, and automated DepEd-compliant report generation.
  - The system was built using XAMPP for local server environment, PHP for dynamic pages, MySQL for database, and Dompdf/PhpSpreadsheet for report generation.
  - A black-box testing approach was employed, using equivalence partitioning to validate system functionality and robustness across key modules.
  - System quality was evaluated against ISO/IEC 25010 and ISO 27001 standards, and user acceptance was assessed using the Technology Acceptance Model.
findings:
  - num: The linear regression model achieved an R² score of 92.81%, indicating high explanatory power for budget variance.
  - num: The model's Mean Absolute Error was ₱1,532.75, and Root Mean Square Error was ₱2,126.84, confirming minimal prediction errors.
  - num: Black-box testing was conducted with 37 test cases, with most modules passing successfully and only minor UI and validation issues identified.
  - num: User acceptance evaluation showed strong approval with weighted means above 4.3 on a 5-point scale across all TAM dimensions.
  - The BFMIS enhances financial transparency and accountability through real-time dashboards and audit trails for school administrators and auditors.
  - AI-driven reporting automates the generation of financial summaries and variance analysis reports, reducing manual effort and aligning with DepEd policies.
  - The system's ability to generate predictive insights enables proactive, evidence-based decision-making for budget planning.
key_figures_tables:
  - Table 2: Black Box Test Case Table summarizes the functional coverage and test case execution across all system modules.
  - Table 4: Regression Model Performance presents MAE, RMSE, and R² score, confirming the predictive model's reliability.
  - Table 5: Summary of Evaluation Results shows high user ratings for system quality, ease of use, and satisfaction.
  - Figure 8: MOOE Prediction Page visualizes the comparison between predicted and actual budget allocations, highlighting data-driven insights.
  - Figure 10: Actual vs. Predicted MOOE Allocations per Category illustrates the model's accuracy in forecasting category-wise budgets.
key_equations:
  - equation: R^2 = 0.9281
    explanation: Indicates model explains 92.81% of budget variance.
  - equation: MAE = ₱1,532.75
    explanation: Represents the average absolute prediction error in pesos.
  - equation: RMSE = ₱2,126.84
    explanation: Confirms minimal large prediction errors enhancing reliability.
definitions:
  - term: MOOE
    definition: Maintenance and Other Operating Expenses, government-allocated funds for school operations.
  - term: BFMIS
    definition: Budget and Financial Management Information System developed in this study.
  - term: TAM
    definition: Technology Acceptance Model, a framework for assessing user acceptance of technology.
  - term: DepEd
    definition: Department of Education, the governing body for Philippine public schools.
  - term: AIP
    definition: Annual Implementation Plan, a tool for school-based management translating long-term goals into yearly actions.
critical_citations:
  - "[Pressman & Maxim, 2014] — Provides black-box testing guidelines for software validation."
  - "[Venkatesh & Davis, 2000] — Foundation for the Technology Acceptance Model used in UAT."
  - "[Byol & Foygel, 2023] — Insight on black box testing for financial systems."
  - "[Roustaei, 2024] — Justifies use of linear regression for predictive modeling with limited data."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: The study focuses on financial management within public schools, a context relevant to the financial environment of Filipino professionals.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: contextual
      justification: The paper analyzes budget allocation structures (MOOE) within the Philippine public school system, which is part of the financial landscape for professionals in education.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: The study mentions cyclical spending patterns for items like electricity and graduation programs, touching on seasonal school-related expenses.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: The BFMIS includes modules for categorizing MOOE expenses, providing a framework for organizing school expenditures.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: The design of the system's expense tracker and reporting module reflects considerations for effective financial data organization.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: The study explicitly reviews the landscape of existing financial management systems in Philippine public schools and their limitations.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: The research is motivated by identified gaps in manual financial processes, directly addressing limitations of current systems.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: The core contribution is the development of a predictive linear regression model for budget forecasting, a key predictive modeling application.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: The linear regression algorithm forecasts future MOOE allocations based on historical sequential spending data.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: The paper discusses participatory budgeting strategies and the use of the AIP, which are relevant domain knowledge for budget recommendation.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: While not strictly a recommendation system, the predictive module provides data-driven suggestions for future budget allocations.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: low
      justification: The system optimizes allocation based on historical trends, but not in a formal constrained optimization framework.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: contextual
      justification: The study touches on identifying misalignments and planning for reallocations, but does not detail infeasibility handling.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: The system has a feature for detecting misalignment between planned and predicted spending, which is a form of anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: The detection method is not based on a specialized anomaly detection algorithm but rather a comparison of planned vs. actual values.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: The system is designed for desktop use but includes UI considerations for usability, which is tangentially related to mobile-first design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: The system incorporates role-based access control and is evaluated against ISO 27001 standards for information security.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: High user acceptance and satisfaction ratings, as measured by TAM, indicate a positive perception of trustworthiness and reliability.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: The system includes features like real-time dashboards that can support user engagement, but this is not a primary focus of the study.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: The linear regression model's performance is rigorously evaluated using MAE, RMSE, and R² metrics.
  contribution: For Odin's spending forecasting module (6.A/6.B), the paper provides a validated linear regression approach for forecasting sequential spending data, with clear metrics (MAE, RMSE, R²). For the expense categorization module (3.A/3.B), it demonstrates a functional categorization framework for school expenses, including real-time tracking and reporting. The study also offers insights for Odin's budget recommendation module (7.B) by showing how predictive insights can inform data-driven budget planning. The evaluation against ISO standards (10.A/10.B) and use of TAM (11.A) provide a methodological framework for validating Odin's system quality and user acceptance. The paper's development process highlights the importance of user-centered design and stakeholder feedback for system adoption (11.B).
  directly_justifies:
    - "Linear regression can effectively forecast budget allocations with high accuracy (R² = 0.9281) for public schools."
    - "System-generated predictive insights support proactive financial decision-making and strategic planning."
    - "Automated, DepEd-compliant reporting reduces manual errors and enhances transparency in financial operations."
    - "User acceptance is positively influenced by perceived usefulness and ease of use in school financial systems."
  limits:
    - "The system's functionality is limited to desktop use and does not include a mobile-first design."
    - "The model's accuracy depends on the quality and completeness of historical data input."
    - "The study's focus is on public elementary schools in one Philippine province, limiting generalizability to other contexts."
    - "Basic security features and manual updates for policy changes are noted as limitations."
    - "The study does not include a formal comparison with other forecasting algorithms to justify the choice of linear regression."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The domains flagged as relevant are: Existing Systems & Gaps (high relevance to 4.A, 4.B), Spending Forecasting (high relevance to 6.A, 6.B), Expense Categorization (medium relevance to 3.A, 3.B), Budget Recommendation (medium relevance to 7.B), Data Privacy & User Trust (medium relevance to 10.A, 10.B), and System Evaluation (high relevance to 12.B). Borderline cases included: seasonal spending (2.D) which was assigned low relevance as it is not a primary focus; user constraints (3.C) and optimization approaches (7.C, 7.D) which were considered but not selected due to the paper's focus on predictive forecasting rather than constraint-based optimization. Domains like Mobile-First Design and Behavioral Profiling were rejected due to a lack of relevant content. The overall relevance of the paper to Odin is high, as it provides a concrete example of a linear regression-based predictive system for financial allocation, supported by rigorous evaluation and a user-centered development methodology.
limitations:
  - "The scope is limited to public elementary schools in one Philippine province, potentially limiting generalizability."
  - "The system's reliance on accurate historical data is a key limitation for the predictive model's performance."
  - "The system lacks a mobile-first design, which is a significant limitation for accessibility in a modern context. [unacknowledged]"
  - "The study did not compare the linear regression model with other machine learning techniques to justify its selection. [unacknowledged]"
  - "The evaluation of security was based on standards review rather than a formal security audit."
remember_this:
  - Linear regression achieved a 92.81% R² score for forecasting school budgets.
  - The BFMIS system automates budget allocation and expenditure tracking.
  - Users strongly agreed on the system's high usability and security features.
  - The system generates DepEd-compliant reports, automating financial submissions.
  - A phased implementation plan with risk mitigation ensures sustainable adoption.
```
---

## Paper 50: Adlermann_summarized.md

**Source File:** `Adlermann_summarized.md`

```yaml
paper_id: 10.15662/IJEETR.2024.0606008
designation: international-algorithm-specific
title: A GRA-Enhanced Cloud AI Framework for Petabyte-Scale Multi-Tenant Environments: Multivariate Classification for Credit Card Fraud Detection and Adaptive Risk Analytics
authors: Adlermann, J. F.
year: 2024
venue: International Journal of Engineering & Extended Technologies Research (IJEETR)
odin_topics:
  - 8.A
  - 8.B
  - 8.C
  - 10.A
  - 12.A
  - 12.B
tldr: Integrates Grey Relational Analysis with machine learning ensembles in a cloud-native, multi-tenant architecture to improve petabyte-scale credit card fraud detection accuracy and efficiency.
problem_and_motivation: Traditional fraud detection classifiers struggle with petabyte-scale data, heterogeneity, and concept drift; prior systems lack integration of lightweight relational signatures to prioritize and interpret complex ML models. There is a gap in combining interpretable relational analysis with scalable cloud infrastructure for multi-tenant environments.
approach:
  - Design an architecture coupling GRA preprocessor with streaming and batch ML pipelines, fusing relational signatures with transactional features.
  - Use standard transaction fields, temporal aggregates per card/account, and graph relationships, stored in a columnar lakehouse.
  - Compute GRA signatures by comparing sliding window sequences to reference baselines (per-card, tenant, global) using the distinguish coefficient.
  - Employ GRA signatures as a prefilter to reduce candidate sets for heavy inference, as input features, and as explanation attributes.
  - Construct hybrid ensemble with fast GBDT for instant scoring and temporal graph neural network for complex patterns, with calibrated probability fusion.
  - Address class imbalance with cost-sensitive learning and focal loss; monitor concept drift and trigger targeted retraining.
  - Integrate semi-supervised label propagation across transaction graph, constrained by tenant policies to prevent leakage.
  - Implement tenant policy engine for per-tenant thresholds, actions, and audit logs, supporting risk adaptation.
  - Store data in lakehouse with distributed compute, locality-aware caching, and partitioning by tenant and hot keys for low-latency retrieval.
  - Orchestrate with containerized microservices, resource quotas, logical isolation, encryption, and access controls; evaluate with detection and operational metrics.
findings:
  - num: GRA prefilter reduced heavy inference volume by 40-70% with <5% loss of true fraud events.
  - num: Combined GRA+ensemble improved ROC AUC by 3-6 percentage points over baselines.
  - num: Precision@1000 improved by 5-12%; false positives reduced up to 18% for low-risk tenants.
  - num: Streaming scoring latency met sub-300ms median at throughput of hundreds of thousands of transactions per second.
  - num: GRA signatures served as early drift indicators, reducing model degradation compared to periodic retraining.
  - Analysts reported GRA signatures improved triage efficiency in simulated review tasks.
  - Tenant policy engine lowered false declines for low-risk tenants while preserving detection for high-risk tenants.
  - Cost-benefit analysis showed positive ROI when heavy model cost is material.
key_figures_tables:
  - None.
key_equations:
  - equation: γ_i(k) = (min + ζ·max)/(Δ_i(k) + ζ·max)
    explanation: Grey relational coefficient for feature dimension k with distinguish coefficient ζ.
definitions:
  - term: GRA
    definition: Grey Relational Analysis, a method to assess similarity between sequences using relational coefficients.
  - term: GBDT
    definition: Gradient-Boosted Decision Tree, an ensemble of decision trees trained sequentially.
  - term: TGNN
    definition: Temporal Graph Neural Network, a neural network that processes graph-structured data with temporal dynamics.
  - term: MCC
    definition: Merchant Category Code, a standard code classifying merchant types.
  - term: SLO
    definition: Service Level Objective, a defined performance target for system operations.
critical_citations:
  - "[Deng, 1982] — Introduced grey systems and GRA."
  - "[Bolton and Hand, 2002] — Surveyed statistical fraud detection methods."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly addresses anomaly detection via GRA and ML ensembles for fraud detection, applicable to spending anomalies.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Proposes specific algorithms (GRA, GBDT, TGNN) and hybrid approaches that can be adapted for spending anomaly detection.
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: medium
      justification: GRA's effectiveness with sparse labels makes it a candidate for cold-start anomaly detection.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Discusses multi-tenant isolation, encryption, and privacy-preserving techniques, but not specific to PFMS.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides evaluation metrics and methodology for detection systems, relevant to evaluating Odin's modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Evaluates algorithmic modules (GRA, ML ensembles) with ablation and performance metrics.
  contribution: The paper's GRA-based anomaly detection approach provides a scalable and interpretable methodology for Odin's spending anomaly detection module. Its hybrid ensemble combining fast models with deep sequence models informs algorithm selection for Odin's forecasting and detection pipelines. The multi-tenant policy engine and privacy-preserving techniques offer design patterns for user-specific constraints and data protection in a PFMS. The emphasis on cost-efficiency and low-latency inference is directly applicable to mobile-first design constraints.
  directly_justifies:
    - GRA signatures provide compact relational scores that are computationally cheap and interpretable.
    - Integrating GRA as a prefilter reduces heavy model invocations by 40-70% with minimal loss of true fraud events.
    - Hybrid ensembles combining GBDT and temporal graph networks improve detection AUC by 3-6 percentage points.
    - Tenant-specific thresholds can reduce false positives by up to 18% for low-risk groups.
  limits:
    - The paper focuses on fraud detection, not general spending anomaly detection for personal finance.
    - Multi-tenant cloud context differs from single-user PFMS; some engineering patterns may not transfer.
    - The evaluation uses synthetic and benchmark datasets; real-world personal spending data may vary.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The anomaly detection domain (8) was flagged as highly relevant because the paper directly addresses detection of fraudulent transactions using GRA and ML ensembles, which maps to spending anomaly detection in Odin. Within 8, sub-topics 8.A, 8.B, and 8.C were assigned high or medium relevance: 8.A and 8.B are directly supported by the algorithm and architecture; 8.C is medium because GRA's sparse-label robustness helps with cold-start. The data privacy domain (10) received low relevance because while the paper discusses isolation and encryption, it is not tailored to PFMS. Evaluation domains (12.A, 12.B) were medium relevance because the paper provides a rigorous evaluation framework and metrics that can inform Odin's module assessment. Domains related to forecasting (6), budgeting (7), behavioral profiling (5), cultural context (2), expense categorization (3), existing systems (4), mobile design (9), retention (11), and savings/debt (13) were considered and rejected as they are not addressed by the paper's content. Overall, the paper is relevant to Odin primarily for its anomaly detection and evaluation methodologies.
limitations:
  - Approximation risk: GRA alone can miss sophisticated collusion and adversarial mimicry.
  - Engineering complexity and governance overhead increase with scale and tenant diversity.
  - Deep graph models may still incur higher inference latency, requiring trade-offs.
  - Cross-tenant graph propagation risks leakage unless strict policy and encryption enforced.
  - Real-world validation with actual user behavior and longitudinal effects is not provided. [unacknowledged]
remember_this:
  - GRA prefilter reduces heavy model invocations by 40-70% with minimal fraud loss.
  - GRA-enhanced ensemble improves ROC AUC by 3-6 percentage points over baselines.
  - GRA signatures provide interpretable relational cues for investigator triage.
  - The framework supports petabyte-scale with sub-300ms latency and tenant isolation.
  - GRA serves as an early drift indicator, enabling timely model retraining.
```
---


---

## Agent Instruction

If the agent reading this document believes further context about a paper is needed, it may request the original converted markdown file (with the '_marked' suffix) from the user for the relevant paper(s).
