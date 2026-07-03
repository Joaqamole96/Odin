```yaml
paper_id: 10.1145/3708985
designation: international-algorithm-specific
title: User Behavior Simulation with Large Language Model-based Agents
authors: Wang, L.; Zhang, J.; Yang, H.; Chen, Z.; Tang, J.; Zhang, Z.; Chen, X.; Lin, Y.; Sun, H.; Song, R.; Zhao, X.; Xu, J.; Dou, Z.; Wang, J.; Wen, J.
year: 2025
venue: ACM Transactions on Information Systems
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 11.A
  - 11.B
  - 12.A
  - 12.B
  - 12.C
  - 9.A
  - 10.A
tldr: LLM-based agents with profile, memory, and action modules simulate realistic user behaviors in recommendation and social network environments.
problem_and_motivation: Simulating high-quality user behavior data is challenging due to the intricate mechanisms of human decision-making. Existing data-driven and model-driven simulation methods face limitations regarding privacy, scalability, and realism. There is a need for an innovative simulation approach that balances adaptability, scalability, and realism without relying on sensitive user data.
approach:
  - Develops LLM-based agents with three core modules: profiling (for diverse user personas), memory (sensory, short-term, and long-term), and action (recommendation, chatting, broadcasting).
  - Designs a multi-agent sandbox environment where agents interact with a recommendation system and with each other via social features.
  - Simulator operates in a round-by-round manner, with agent activity levels modeled using a Pareto distribution.
  - Evaluation includes subjective human assessment and objective comparison against baselines like Embedding, BERT, and RecSim using overlap ratio and adversarial methods.
  - Demonstrates potential applications by simulating information cocoons and user conformity behaviors.
findings:
  - RecAgent surpasses the best baseline by 45.8% in predicting user preferences, with performance only 8.7% lower than real human evaluations.
  - "num: 45.0% win rate" in adversarial evaluation for behavior sequence believability, significantly outperforming RecSim's 33.3%.
  - Both increasing recommendation randomness and adding friends with different interests effectively alleviate information cocoons, but randomness can lower user satisfaction.
  - Agents with more friends are more likely to exhibit conformity behaviors and change their opinions.
  - The complete memory module achieves the best relevance scores, and removing short-term or long-term memory significantly reduces informativeness or relevance.
key_figures_tables:
  - Figure 5: Overlap ratio comparison for recommendation behaviors → RecAgent's performance is closest to real humans.
  - Figure 6: Adversarial evaluation of behavior sequences → RecAgent achieves higher win rates than RecSim.
  - Figure 9: Evaluation of memory module variants → Complete memory module achieves highest relevance score.
  - Figure 10: Efficiency analysis → Time cost and monetary cost scale with the number of agents, API keys, and simulation rounds.
key_equations:
  - equation: p(x) = α * x_min^α / x^(α+1)
    explanation: Pareto distribution models agent activity levels in a long-tail distribution.
  - equation: g(M_i) = 1 - (s_i + r_i)/2 * max(r_i^β, δ)
    explanation: Power function models forgetting probability in long-term memory based on recency and importance.
definitions:
  - term: LLM-based Agent
    definition: An autonomous entity powered by a large language model with profile, memory, and action modules for behavior simulation.
  - term: Information Cocoon
    definition: A phenomenon where users are exposed only to information similar to their existing preferences, limiting diversity.
  - term: User Conformity
    definition: The tendency of users to align their behaviors or opinions with those of their friends or social group.
critical_citations:
  - "[Park et al., 2023] — Foundational work on generative agents for human behavior simulation."
  - "[Piao et al., 2023] — Provides framework for measuring information cocoons with entropy."
  - "[Zhang and Balog, 2020] — Establishes user simulation for conversational systems."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: The paper's profiling module directly informs the creation and use of financial behavioral profiles.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: high
      justification: The simulation approach provides a method to generate initial profiles, addressing the cold-start problem.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: The action module and behavior simulation can be adapted to classify and analyze financial profiles.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: The study on information cocoons and conformity provides insights into how recommendations affect user engagement and exploration.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: Findings on the trade-off between recommendation diversity and user satisfaction are directly relevant to retention strategies.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: The paper's evaluation methodology, including adversarial subjective evaluation, offers a template for evaluating Odin's modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: The approach of comparing agent behavior to ground truth and baselines is highly relevant for evaluating Odin's algorithmic modules.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: The paper's agent-based simulation framework can be adapted to evaluate the dynamics of budget recommendations over time.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: The paper's motivation mentions privacy regulations, which indirectly support a mobile-first, privacy-preserving design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: The paper is motivated by the need to avoid sensitive user data, providing a rationale for simulation-based approaches that align with privacy.
  contribution: "This paper establishes a viable methodology for simulating user behavior using LLM-based agents, which can be directly applied to Odin's user behavior modeling. The profiling and memory modules provide a concrete framework for creating and evolving user financial personas. The multi-agent environment offers a sandbox for testing Odin's recommendation and anomaly detection modules without real user data. The study on information cocoons and conformity behaviors provides a template for simulating and understanding complex financial decision-making dynamics in a social context."
  directly_justifies:
    - "LLM-based agents can simulate realistic user behaviors through profile, memory, and action modules."
    - "Agent memory mechanisms are crucial for producing consistent and believable behavior sequences."
    - "Introducing randomness in recommendations can alleviate information cocoons but may lower user satisfaction."
  limits:
    - "Evaluation relies on subjective human assessment, which may not capture all nuances of real-world behavior."
    - "The simulation environment is discrete and round-based, which is a simplification of continuous real-world interactions."
  mapping_rationale: "A systematic scan of all 12 functional domains was performed. The paper was flagged as highly relevant to 'Behavioral Profiling & Classification' (5.A, 5.B, 5.C) due to its detailed agent framework and simulation of user behaviors, directly addressing the cold-start problem. It is also highly relevant to 'System Evaluation' (12.A, 12.B, 12.C) because it provides a robust methodology for evaluating simulation fidelity and module performance. 'User Retention & Engagement' (11.A, 11.B) is a medium relevance domain, as the simulated phenomena of information cocoons and conformity directly inform engagement and retention mechanisms. 'Mobile-First Design' (9.A) and 'Data Privacy & User Trust' (10.A) were considered 'contextual' and 'low' because the paper mentions privacy as a motivator but does not specifically address mobile UX. All other domains, including 'Filipino Cultural Context', 'Expense Categorization', 'Existing Systems', 'Spending Forecasting', 'Budget Recommendation', 'Anomaly Detection', and 'Savings & Debt Management' were considered and rejected as the paper does not address them. The overall relevance is high as it provides a foundational methodology for simulating user behavior, which is central to Odin's design and evaluation."
limitations:
  - "Round-by-round simulation discretizes continuous real-world time, limiting flexibility. [unacknowledged]"
  - "The simulation may overlook various real-world factors that influence user decisions, such as external commitments. [unacknowledged]"
  - "LLMs are not fine-tuned for behavior analysis, and prompting may not be robust across different models. [unacknowledged]"
  - "Subjective evaluation remains a challenge and may miss subtle nuances of real-world interactions. [acknowledged]"
  - "Security and privacy concerns exist regarding the handling of generated data, though the system relies on LLM safeguards. [acknowledged]"
remember_this:
  - LLM-based agents with memory modules can simulate believable and consistent user behaviors.
  - RecAgent's performance in predicting user preferences is only 8.7% lower than real humans.
  - Both recommendation randomness and social diversity can alleviate information cocoons.
  - User conformity behaviors are more pronounced in agents with a greater number of social connections.
  - The simulation framework provides a valuable, privacy-preserving platform for evaluating system dynamics.
```