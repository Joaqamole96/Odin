```yaml
paper_id: 10.1109/TPAMI.2023.3331846
designation: international
title: Towards Human-Centered Explainable AI: A Survey of User Studies for Model Explanations
authors: Rong, Y.; Leemann, T.; Nguyen, T.; Fiedler, L.; Qian, P.; Unhelkar, V.; Seidel, T.; Kasneci, G.; Kasneci, E.
year: 2024
venue: IEEE Transactions on Pattern Analysis and Machine Intelligence
odin_topics:
  - 4.A
  - 4.B
  - 5.A
  - 12.A
  - 12.C
tldr: A systematic review of 97 user studies in XAI reveals inconsistent effectiveness of explanations on trust and usability, highlighting the need for more rigorous human-centered evaluations.
problem_and_motivation: The behavior of modern AI systems is often not understandable, which presents a dilemma in safety-critical domains. Evaluating the quality of explanations requires human-centered assessments, yet existing user studies are sparse and lack insights from cognitive or social sciences.
approach:
  - Conducted a systematic literature review of user studies in XAI from top-tier venues over five years.
  - Identified 97 core papers that deploy explainable models or techniques and conduct assessments with human subjects.
  - Categorized the papers based on measured characteristics of explanatory methods: trust, understanding, usability, and human-AI collaboration performance.
  - Analyzed the core papers' foundational works and application domains using a data-driven bibliometric approach.
  - Synthesized the findings to propose practical guidelines for designing and conducting effective XAI user studies.
findings:
  - XAI research is spreading more rapidly in certain domains, such as recommender systems, but user evaluations remain sparse.
  - The effectiveness of explanations on user trust is mixed, with about half of the studies showing a positive impact.
  - Explanations improve subjective understanding but often fail to improve objective understanding, revealing an illusion of explanatory depth.
  - The impact of explanations on usability metrics such as satisfaction and perceived fairness is inconsistent and often non-significant.
  - Explanations can improve human-AI collaboration performance, especially for novices, but may decrease performance for experts.
  - num: Around 55% of user studies use a between-subjects design, with participant numbers typically starting around 30.
key_figures_tables:
  - Figure 1: Roadmap of the literature analysis → Shows the process from foundational works to future directions in human-centered XAI.
  - Figure 2: Distribution of participant numbers in surveyed user studies → Indicates common sample sizes for different experimental designs.
  - Table I: Overview of core papers grouped by categories of measurements → Lists papers according to trust, understanding, usability, and human-AI collaboration.
  - Table II: Keywords for the paper search query → Details the search strategy used to identify core papers.
  - Table III: Models and explanations in core papers → Cross-tabulates model types with explanation techniques.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "XAI"
    definition: "Explainable Artificial Intelligence, a research area focused on making AI systems more interpretable and transparent."
  - term: "LIME"
    definition: "Local Interpretable Model-agnostic Explanations, a method for explaining individual predictions."
  - term: "SHAP"
    definition: "SHapley Additive exPlanations, a game-theoretic approach to explain the output of any machine learning model."
  - term: "HCI"
    definition: "Human-Computer Interaction, the study of how people interact with computers and to design technologies that let users interact with computers in novel ways."
critical_citations:
  - "[Doshi-Velez and Kim, 2017] — Introduced the three categories of XAI evaluation: functionally-grounded, application-grounded, and human-grounded."
  - "[Liao et al., 2021] — Discussed human-centered XAI and the importance of evaluating from a user perspective."
  - "[Molnar, 2020] — Provided a taxonomy of explanation methods used in the field."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Survey of user studies in XAI provides a landscape of how evaluations are conducted, which can inform PFMS system design.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly identifies limitations in current user evaluations of AI systems, such as sparse human-subject experiments and mixed effectiveness of explanations.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: low
      justification: Discusses user mental models and understanding, which is tangentially related to how users might perceive their financial profiles.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: This paper is a survey of evaluation methodologies, specifically for XAI, offering a framework that can be adapted for PFMS evaluation.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: contextual
      justification: Provides general guidelines for user studies (e.g., proxy tasks, measures) that are applicable to evaluating any recommendation system, including budgeting.
  contribution: This survey provides a comprehensive framework for evaluating user-centric aspects of AI systems, which is directly applicable to Odin's need to build trust and understanding. Its guidelines on measuring user trust, understanding, and usability can inform Odin's evaluation of its recommendation and forecasting modules. The identification of mixed effects of explanations on user trust underscores the need for Odin to test its explanations rigorously. The synthesis of experimental design patterns offers a practical checklist for Odin's future user studies.
  directly_justifies:
    - "User evaluations in XAI are still rather sparse and incorporate hardly any insights from cognitive or social sciences."
    - "Explanations have mixed effects on user trust and often fail to improve objective understanding."
    - "The effectiveness of model explanations depends on factors such as model accuracy and the user's level of expertise."
    - "Proxies tasks used in evaluations may not reflect real-world performance, necessitating careful design."
  limits:
    - "The survey is based on literature up to 2022, potentially missing very recent developments in XAI user studies."
    - "The analysis is limited to papers from selected top-tier venues and may not represent all XAI research."
    - "The guidelines proposed are based on a review of existing work and have not been empirically validated."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. Domains related to system evaluation (12.A, 12.C) and limitations of existing systems (4.B) were flagged as highly relevant because the paper directly provides a framework for evaluating AI systems and identifies gaps in current practices. The domain of existing systems (4.A) was marked medium as the survey describes the landscape of XAI user studies, which can serve as a point of reference. Behavioral profiling (5.A) was considered low because while the paper discusses user mental models, it does not address financial behavioral profiling specifically. Domains like Filipino Cultural Context (2.A-D), Spending Forecasting (6.A-B), Anomaly Detection (8.A-C), and Data Privacy (10.A) were rejected as the paper does not address these PFMS-specific functional areas. The paper's overall relevance is as a methodological guide for how Odin should evaluate its user-facing features, rather than providing direct content for those features.
limitations:
  - "User studies are mostly conducted in controlled lab settings, which may not reflect real-world usage. [unacknowledged]"
  - "The paper does not propose a new evaluation metric but synthesizes existing ones. [unacknowledged]"
  - "The long-term effects of explanations on user behavior are not studied in the surveyed works. [unacknowledged]"
  - "None."
remember_this:
  - Explanations often increase perceived understanding but not actual objective understanding.
  - The effectiveness of XAI on user trust is mixed and depends on context.
  - User studies in XAI frequently lack grounding in cognitive or psychological theories.
  - A comparison with a no-explanation baseline is crucial to prove XAI effectiveness.
  - num: Only about 20% of XAI evaluation projects include human subjects.
```