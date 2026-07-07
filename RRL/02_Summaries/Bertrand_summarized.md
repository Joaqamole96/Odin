```yaml
paper_id: 10.70675/216d3647z78bcz4c68z9ba9z2d0a029cf1b4
designation: international
title: Misplaced trust in AI: the explanation paradox and the human-centric path
authors: Bertrand, A.
year: 2024
venue: Institut Polytechnique de Paris
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 7.B
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 12.A
  - 12.B
  - 12.C
tldr: Explanations in AI systems can paradoxically increase user trust, including unwarranted trust, and require human-centric design to support appropriate trust calibration and regulatory compliance in financial applications.
problem_and_motivation: The opacity of AI systems, particularly deep learning models, creates challenges for user trust and regulatory compliance. Existing explainability methods have not been adequately evaluated for their ability to foster warranted trust in highly regulated financial environments. This thesis investigates the cognitive challenges and potential of explainability to enable appropriate trust and compliance.
approach:
  - Conducted two detailed scoping literature reviews on cognitive biases and interactive explanations in explainable AI.
  - Developed Robex, a fictional robo-advisor for life-insurance, using rule-based algorithms and SHAP for feature explanations.
  - Performed co-design sessions with regulatory supervisors and end-users to refine explanation prototypes.
  - Conducted a deception-based between-subjects experiment with 256 participants to test different explanation formats.
  - Used scenario-based workshops with 13 supervisors and 6 bank practitioners to elicit needs for AI justifications in AML-CFT.
  - Combined HCI methods with a qualitative compliance assessment of AML-CFT legal requirements.
findings:
  - num: Explanations tend to increase trust, including overtrust, depending on user knowledge and explanation design.
  - num: Interactive explanations increase perceived usefulness but not usability compared to static ones.
  - num: In life-insurance robo-advisors, feature-based explanations did not significantly improve appropriate reliance or understanding.
  - Dialogic explanations increased unwarranted trust in robo-advisor recommendations.
  - Supervisors need justifications to verify human-AI alignment, business expert understanding, and control of AI-specific risks.
  - Explanations serve as "trial evidence" for justifications, which must also be grounded in external norms.
key_figures_tables:
  - Figure 3.3: Summary of cognitive constraints and biases in XAI → Highlights explanation paradox where explanations increase overtrust.
  - Figure 4.19: Quantitative evaluations of interactive vs. static explanations → Shows interactive explanations improve usefulness but not ease of use.
  - Figure 5.11: Results of Study 2 on robo-advisor explanations → Demonstrates dialogic explanations significantly increase subjective trust.
  - Table 6.3: Supervisors' needs for model justifiability → Details seven needs including performance measurement and human alignment.
key_equations:
  - equation: "P(C|E) = P(C) * P(E|C) / P(E)"
    explanation: Bayesian approach to updating belief in an explanation given AI prediction.
definitions:
  - term: Explainable AI (XAI)
    definition: A field aimed at providing explanations for AI system behavior to stakeholders.
  - term: Warranted trust
    definition: Trust that is caused by the trustworthiness of a system.
  - term: Justification
    definition: An argumentative process referring to external norms to show a decision or system is adequate.
critical_citations:
  - "[Miller, 2019] — Provides foundational insights from social sciences for XAI."
  - "[Jacovi et al., 2021] — Formalizes prerequisites for trust in AI and distinguishes warranted trust."
  - "[Bhatt et al., 2021] — Explores uncertainty as a form of transparency in AI."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly addresses cognitive biases affecting trust calibration with AI systems.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: Discusses user expertise and prior knowledge as factors in trust calibration.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Reviews classification of user groups and their cognitive characteristics.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Examines the role of explanations in forecasting and predictive systems.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: Discusses challenges of explaining sequential data forecasts.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: Directly tests the effectiveness of explanations for budget-related recommendations.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Case study in AML-CFT directly involves anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Reviews AI techniques for anomaly detection in financial crime.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Discusses trust and privacy concerns in AI-enhanced financial systems.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Core focus of the thesis on trust calibration in financial AI.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Explores user engagement and curiosity as factors for effective explanations.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: low
      justification: Briefly touches on engagement design for explanations.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Proposes and applies human-grounded evaluation frameworks for XAI.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Evaluates different explanation modules (e.g., SHAP) and their effects.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Applies application-grounded evaluation to life-insurance recommender system.
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Paper does not specifically focus on Filipino demographics but its findings are broadly applicable.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: contextual
      justification: The behavioral insights are general and not specific to Filipino young professionals.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: Not addressed in the paper.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Not addressed in the paper.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: Not directly addressed.
    - code: 3.C
      name: User-Defined Allocation Constraints
      relevance: contextual
      justification: Not directly addressed.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Briefly references existing systems but does not survey them.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: contextual
      justification: Discusses limitations of current XAI methods but not specifically for Odin.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: Not the primary focus.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: contextual
      justification: Not addressed.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: contextual
      justification: Not addressed.
    - code: 8.C
      name: Cold‑Start Baseline Strategies for Anomaly Detection
      relevance: contextual
      justification: Not a main focus, though the cold-start problem is mentioned.
    - code: 9.A
      name: Mobile‑First Design Principles and Rationale
      relevance: contextual
      justification: Not discussed.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: contextual
      justification: Not discussed.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: contextual
      justification: Not addressed.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: contextual
      justification: Not addressed.
    - code: 13.C
      name: End‑of‑Period Surplus as a Savings Input
      relevance: contextual
      justification: Not addressed.
  contribution: "The paper provides a comprehensive analysis of the cognitive challenges to appropriate trust in explainable AI, directly informing Odin's user trust and engagement modules. It offers a taxonomy of interactive explanations that can guide the design of Odin's user interfaces for budget recommendations and anomaly detection. The empirical findings on explanation effectiveness in financial decision-making are critical for validating Odin's proposed XAI features. The investigation of supervisor needs in AML-CFT provides a framework for Odin's compliance and auditability requirements."
  directly_justifies:
    - "Explanations tend to increase trust, including overtrust, depending on user knowledge and explanation completeness."
    - "Interactive explanations improve perceived usefulness but may take longer and are not always easy to use."
    - "Feature-based explanations may not significantly improve appropriate reliance in financial decision-making."
    - "Dialogic explanations can increase unwarranted trust in AI recommendations."
  limits:
    - "The quantitative experiments used a simplified, fictional robo-advisor, limiting generalizability to complex real-world systems."
    - "The study on supervisor needs was conducted in France and may not be generalizable to other regulatory contexts."
    - "The research on interactive XAI did not find a clear effect on overtrust, indicating a need for more controlled experiments."
    - "The compliance assessment was conducted by a non-lawyer, though validated with legal experts."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. Topics related to cognitive biases (5.A, 5.B, 5.C), forecasting (6.A, 6.B), budget recommendation (7.B), anomaly detection (8.A, 8.B), user trust (10.B), engagement (11.A), and evaluation (12.A, 12.B, 12.C) were flagged as highly to moderately relevant due to the paper's direct focus on trust calibration in AI decision-making, its empirical tests on explanation effectiveness in financial contexts (life insurance and AML-CFT), and its review of evaluation methodologies. Topics related to Filipino cultural context (1.A, 1.C, 2.A, 2.B) were considered and rejected as contextual because the paper does not specifically address Filipino demographics or cultural practices, though its general behavioral findings may be applicable. Topics like mobile-first design (9.A, 9.B) and savings/debt management (13.A, 13.B, 13.C) were not addressed. The paper's core contributions on the 'explanation paradox' and the human-centric approach for financial compliance directly justify its high relevance for Odin's design, particularly in user trust, explanation design, and regulatory auditability."
limitations:
  - "The literature reviews are scoping reviews, not systematic reviews, which may have missed some relevant papers."
  - "The quantitative study on robo-advisors used crowd-sourced participants who may not be representative of real users."
  - "The workshop findings on supervisor needs are based on early-stage regulatory thinking and may evolve."
  - "The legal compliance assessment is based on French law, limiting generalizability."
  - "The research did not test curiosity-driven explanations designed to improve user engagement."
remember_this:
  - "Explanations tend to increase trust, including overtrust."
  - "Interactive explanations are more useful but less easy to use."
  - "Feature-based explanations may not improve reliance in finance."
  - "Dialogic explanations can lead to unwarranted trust."
  - "Supervisors need justifications, not just explanations, for compliance."
```