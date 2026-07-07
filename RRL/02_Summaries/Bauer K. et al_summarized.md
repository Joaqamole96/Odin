```yaml
paper_id: 10.1287/isre.2023.1199
designation: international-algorithm-specific
title: Expl(AI)ned: The Impact of Explainable Artificial Intelligence on Users' Information Processing
authors: Bauer, K.; von Zahn, M.; Hinz, O.
year: 2023
venue: Information Systems Research
odin_topics:
  - 4.A
  - 5.A
  - 5.C
  - 10.B
  - 11.A
tldr: Feature-based explanations change users' situational weighting of information and evoke mental model adjustments subject to confirmation bias, which can persist and create spillover effects.
problem_and_motivation: The widespread adoption of explainable AI (XAI) is mandated by regulation, but its effects on users' cognitive processes—specifically situational information processing and mental models—are not well understood. This gap is critical because explanations may fundamentally reshape how users understand the world and make decisions.
approach:
  - Two complementary incentivized experimental studies were conducted: Study 1 with 607 laypeople in an abstract investment game, and Study 2 with 153 real estate experts predicting apartment listing prices.
  - In both studies, participants were assigned to conditions with no AI, opaque AI predictions, or AI predictions plus feature-based explanations (LIME in Study 1, SHAP in Study 2).
  - Study 1 measured changes in participants' weighting of borrower traits and investment decisions across three stages, including a stage without AI support after the intervention.
  - Study 2 elicited prior and posterior beliefs about feature-label relationships to directly measure mental model adjustments and test for confirmation bias.
  - Study 2 also included a transfer task to a different market to test for spillover effects.
findings:
  - num: Observing explanations changed participants' situational weighting of features by an average of 73.9%.
  - num: Explanations reduced the weight placed on the overall prediction by 26.8%.
  - num: Explanation-driven mental model adjustments were asymmetric; participants reinforced priors confirmed by explanations but did not abandon conflicted priors.
  - num: In Study 2, posterior beliefs resembled SHAP values 25 percentage points more closely when explanations were provided.
  - num: Explanation-driven belief adjustments were subject to confirmation bias, with the influence of SHAP values being 50% stronger when they confirmed prior beliefs.
  - num: Mental model adjustments spilled over to related decisions, changing price estimates in a different market by approximately 20%.
  - In Study 1, the provision of explanations decreased investment performance by 8.9% (with explanations) and 9.8% (without) compared to opaque predictions.
key_figures_tables:
  - Figure 2: LIME values and estimated effects on situational information processing → The weighting of traits adjusted in the direction of the explanations.
  - Figure 3: Estimated prediction and explanation effects on mental models → Only explanations caused significant adjustments, reinforcing confirmed priors.
  - Figure 4: Distribution of absolute belief changes in Study 2 → XAI participants adjusted their beliefs significantly more than NoAid or AI participants.
  - Figure 5: Price distributions in Chemnitz → XAI participants' estimates differed significantly based on green voter share, demonstrating spillover effects.
key_equations:
  - equation: Y_{ijs} = β_1 · X_j + β_2 · (X_j × I_s) + β_3 · (X_j × Expl_i) + β_4 · (X_j × Expl_i × I_s) + γ + ϵ
    explanation: Regression model used in Study 1 to measure changes in investment probability.
  - equation: Post_{ijk} = β_1 · Pri_{ijk} + β_2 · (AI_i × Pri_{ijk}) + β_3 · (Expl_i × Pri_{ijk}) + β_4 · SV_{ij} + β_5 · (AI_i × SV_{ij}) + β_6 · (Expl_i × SV_{ij}) + γ_i + δ_k + ϵ
    explanation: Regression model for posterior belief formation in Study 2.
definitions:
  - term: XAI
    definition: Explainable Artificial Intelligence; methods that present in understandable terms why an AI system makes certain predictions.
  - term: LIME
    definition: Local Interpretable Model-agnostic Explanations; a feature-based XAI method that creates surrogate models for local explanations.
  - term: SHAP
    definition: SHapley Additive exPlanations; a feature-based XAI method using Shapley values from game theory.
  - term: Mental Model
    definition: Cognitive representations encoding beliefs, facts, and knowledge that guide information processing and decision-making.
  - term: Confirmation Bias
    definition: The tendency to selectively process information that confirms existing beliefs while discounting conflicting information.
  - term: Spillover Effect
    definition: The phenomenon where learning from XAI in one decision domain transfers to and affects behavior in a related but different domain.
critical_citations:
  - "[Doshi-Velez and Kim, 2017] — Defines XAI and interpretability."
  - "[Gregor and Benbasat, 1999] — Foundational theory on explanations in expert systems."
  - "[Ribeiro et al., 2016] — Introduces LIME."
  - "[Lundberg and Lee, 2017] — Introduces SHAP."
  - "[Agrawal et al., 2019] — Formal model of prediction and judgment."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Examines the integration of XAI into decision-support systems.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly investigates how XAI changes users' information processing and mental models.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Shows how explanations affect the classification of information by users.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Findings on mental model adjustments and confirmation bias have direct implications for trust dynamics.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: The asymmetric learning and spillover effects influence how users engage with the system over time.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: contextual
      justification: Provides background on cognitive effects but does not specifically address mobile UX.
  contribution: "This paper provides a foundational understanding of how XAI influences user cognition, which is directly applicable to Odin's behavioral profiling and user trust modules. The finding that explanations evoke mental model adjustments, subject to confirmation bias, informs how Odin should present explanations to users to avoid reinforcing misconceptions. The spillover effects documented highlight the need for careful design to prevent learned patterns from negatively impacting unrelated financial decisions. These insights are crucial for Odin's design to ensure that its explainability features improve, rather than hinder, user financial behavior."
  directly_justifies:
    - "Feature-based explanations change users' situational weighting of available information."
    - "Explanations evoke lasting mental model adjustments subject to confirmation bias."
    - "Mental model adjustments create spillover effects that alter user behavior in related domains."
    - "Providing explanations can lead to suboptimal decisions when they reinforce inaccurate preconceptions."
  limits:
    - "Studies did not provide feedback on decision outcomes, limiting understanding of learning dynamics over time."
    - "Findings are based on local feature-based explanations (LIME, SHAP); other explanation types may yield different effects."
    - "The abstract nature of Study 1's task may limit generalizability to more familiar financial contexts."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The domains flagged as relevant were Behavioral Profiling & Classification (5.A, 5.C), Existing Systems & Gaps (4.A), Data Privacy & User Trust (10.B), and User Retention & Engagement (11.A) because the paper directly investigates how XAI alters user information processing and mental models. Topic 5.A was assigned 'high' relevance as the paper's core contribution on mental model adjustments directly informs how behavioral profiles are formed and updated. Topics 4.A, 5.C, and 10.B were deemed 'medium' relevance as they provide supporting evidence on the design and consequences of XAI. Topic 9.B (Mobile UX) was considered 'contextual' because the cognitive effects discussed are relevant to UX design but the paper does not specifically address mobile contexts. Domains such as Expense Categorization, Spending Forecasting, and Budget Recommendation were rejected because the paper does not address these specific financial functions. Overall, the paper provides strong empirical evidence on the cognitive side effects of XAI, making it highly relevant to Odin's design, particularly in behavioral profiling and trust."
limitations:
  - "The lack of feedback on decision outcomes limits the generalizability of findings to real-world settings where feedback is available. [unacknowledged]"
  - "The study only examines local feature-based XAI methods; global or example-based explanations may produce different effects. [unacknowledged]"
  - "The artificial nature of the investment game in Study 1 may limit its external validity to more familiar financial decisions. [unacknowledged]"
  - "Participants were not given the opportunity to calibrate their trust based on the system's actual performance. [unacknowledged]"
remember_this:
  - "Explanations change how users weight information and update mental models."
  - "Mental model adjustments are asymmetric and subject to confirmation bias."
  - "Misconceptions can persist and accumulate, leading to suboptimal decisions."
  - "Explanations can create spillover effects, altering behavior in unrelated domains."
  - "Providing explanations decreased performance by 9.8% without explanations present."
```