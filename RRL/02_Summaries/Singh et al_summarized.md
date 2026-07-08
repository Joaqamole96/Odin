```yaml
paper_id: 10.1145/3579363
designation: international-algorithm-specific
title: Directive Explanations for Actionable Explainability in Machine Learning Applications
authors: Singh, R.; Miller, T.; Lyons, H.; Sonenberg, L.; Velloso, E.; Vetere, F.; Howe, P.; Dourish, P.
year: 2023
venue: ACM Transactions on Interactive Intelligent Systems
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
  - 12.C
tldr: Directive explanations that suggest specific or generic actions are significantly preferred over non-directive counterfactual explanations for enabling recourse in machine learning decisions.
problem_and_motivation: Existing counterfactual explanations describe what must change for a different outcome but fail to provide actionable guidance on how to achieve that change, limiting user recourse. This gap reduces the practical utility of explainable AI for individuals seeking to alter decisions. The work addresses the need for explanations that explicitly recommend actions to reach a desired counterfactual state.
approach:
  - Defines directive explanations as those offering specific or generic actions to achieve recourse.
  - Formalizes directive generation using a Markov Decision Process (MDP) to model sequential actions and outcomes.
  - Implements the MDP using Monte-Carlo Tree Search to generate policies that transition a user from a factual state to a counterfactual state.
  - Conducts two online user studies (quantitative ranking and qualitative reasoning) in credit scoring and employee satisfaction domains.
  - Compares three explanation types: non-directive, directive-specific, and directive-generic across multiple scenarios.
findings:
  - num: 69% of credit scoring and 86% of employee satisfaction participants chose a directive explanation as most preferred.
  - num: Directive-specific explanations were strongly preferred when the outcome was unfavorable (e.g., loan denied, p < 0.001).
  - Directive-generic explanations were most preferred in the employee satisfaction domain (51% first preference).
  - Non-directive explanations were least preferred overall, but more suitable when the outcome was favorable.
  - Explanation preferences are influenced by individual, social, and contextual factors, not just scenario type.
key_figures_tables:
  - Figure 1: Bar charts of explanation type preferences by domain → Directive explanations are strongly preferred over non-directive.
  - Figure 2: Thematic coding results from qualitative study → Action-related and usefulness/practical factors most influence choice.
key_equations:
  - equation: c = argmin_y_loss(f(c), y) + |x - c|
    explanation: Formulation for counterfactual state as a perturbation of input.
  - equation: r = r_decision + r_distance
    explanation: Multi-objective reward for MDP to guide search toward counterfactuals.
definitions:
  - term: Directive Explanation
    definition: Explanation that offers specific actions an individual can take to achieve their desired outcome.
  - term: MDP
    definition: Markov Decision Process, a mathematical framework for modeling sequential decision-making under uncertainty.
  - term: Counterfactual Explanation
    definition: Statement of how the world would need to differ for a desirable outcome to occur.
critical_citations:
  - "[Wachter et al., 2017] — Foundational work on counterfactual explanations."
  - "[Utsun et al., 2019] — Proposed method for actionable recourse in linear models."
  - "[Karimi et al., 2021] — Argued for causal models to improve counterfactual actionability."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: Studies general user preferences for explanation types, informing profile design.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: contextual
      justification: Findings on preference variability support need for dynamic profiling.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Does not propose classification methods, but informs design of profile attributes.
    - code: 9.A
      name: Mobile‑First Design Principles and Rationale
      relevance: medium
      justification: Findings on explanation preference directly inform mobile UX for financial apps.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Results on explanation clarity and actionability are key for mobile interface design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Mentions user trust and personalization, but not privacy/security directly.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Preference for explanations that are not condescending links to building user trust.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a concrete methodology (user studies) for evaluating explanation modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Directly evaluates the preference and perception of different explanation algorithms.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: The user study design (ranking, qualitative analysis) is transferable to evaluating budget recommendations.
  contribution: "This paper provides a validated user-centered methodology for evaluating explanation types, which is directly applicable to Odin's recommendation and anomaly detection modules. Its formal MDP model for generating directive explanations offers a computational framework that can be adapted for Odin's budget recommendation and forecasting components. The finding that users prefer specific actions when outcomes are unfavorable informs Odin's design for providing actionable feedback on rejected budgets or flagged anomalies. The qualitative insights on explanation preferences (e.g., avoiding condescending advice) are crucial for designing Odin's user interface and interaction flow to build trust and engagement."
  directly_justifies:
    - "Directive explanations are significantly preferred over non-directive ones in decision scenarios."
    - "Explanation preference varies by outcome favorability and domain context."
    - "Generic directives are preferred when users desire autonomy over specific actions."
    - "Feasibility and social factors influence user acceptance of generated directives."
  limits:
    - "Study participants were from the US, limiting cultural generalizability to Filipino users."
    - "Actions in the model were sourced from public websites and may not reflect all real-world possibilities."
    - "Study used an intermediary role (loan officer) which may not reflect end-user preferences directly."
    - "The model was tested on only two domains (credit scoring, employee satisfaction)."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to System Evaluation (12.A, 12.B) due to its rigorous user study methodology for comparing explanation types. It provides medium relevance to Mobile-First Design (9.A, 9.B) and User Trust (10.B), as the findings on explanation clarity and tone directly inform UX principles and trust-building. Contextual relevance was assigned to Behavioral Profiling (5.A, 5.B) because the study explores individual preference variability, which supports dynamic profiling. Topics related to forecasting (6.A, 6.B), budgeting (7.A-D), anomaly detection (8.A-C), savings/debt (13.A-C), and Filipino cultural context (1.A, 2.A-D, 3.A-C) were considered and rejected as the paper does not address these functional areas. Borderline cases included the paper's connection to user constraints (3.C), but since the study focuses on explanation preferences rather than user-defined budget allocations, it was not selected. Overall, the paper is highly relevant to Odin's evaluation and user experience design, particularly for its explanation and feedback mechanisms."
limitations:
  - "Study participants were from the United States, which may not generalize to Filipino cultural context. [unacknowledged]"
  - "The study used an intermediary role, not the end-user, which may affect preference results. [unacknowledged]"
  - "The cost and feasibility of actions were not directly controlled in the scenarios."
  - "The MDP model was demonstrated only on categorical features."
remember_this:
  - "69% of participants preferred directive explanations over counterfactuals."
  - "Users prefer specific actions when the decision is unfavorable."
  - "Generic directives are preferred when users want to retain autonomy."
  - "Explanation preferences are subjective and context-dependent."
  - "Feasibility and social factors influence acceptance of directives."
```