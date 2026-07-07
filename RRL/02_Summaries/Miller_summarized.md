```yaml
paper_id: 10.1145/3593013.3594001
designation: international
title: "Explainable AI is Dead, Long Live Explainable AI!: Hypothesis-driven Decision Support using Evaluative AI"
authors: "Miller, T."
year: 2023
venue: "2023 ACM Conference on Fairness, Accountability, and Transparency (FAccT '23)"
odin_topics:
  - 10.B
  - 11.A
  - 11.B
  - 12.A
tldr: "A position paper proposing 'Evaluative AI', a conceptual framework for decision support that provides evidence for and against human hypotheses instead of providing machine recommendations, aiming to improve trust calibration and decision-making quality."
problem_and_motivation: "Current recommendation-driven XAI leads to over-reliance and under-reliance because it disrupts human cognitive processes and limits agency. A paradigm shift is needed to align decision support with how humans naturally reason, by supporting hypothesis-driven evaluation."
approach:
  - "The paper is a position paper, not presenting a specific algorithm or empirical study."
  - "It conducts a narrative review of cognitive decision-making processes, focusing on abductive reasoning and the Data/Frame Theory."
  - "It critically evaluates four paradigms of AI-assisted decision support: recommendations, recommendations with explanations, interpretable models, and cognitive forcing."
  - "It proposes a new conceptual framework called Evaluative AI, which is a machine-in-the-loop paradigm."
  - "This framework shifts from 'recommend and defend' to providing evidence for and against user-generated hypotheses."
findings:
  - "Recommendation-driven XAI often fails to improve decision making because users do not cognitively engage with it."
  - "Explainability tools can lead to over-confidence, even when explanations are placebic."
  - "Cognitive forcing strategies can mitigate over-reliance but are less preferred by users and still represent a recommendation-driven approach."
  - "Aligning decision support with abductive reasoning, where users generate and test hypotheses, is more effective."
  - "Evaluative AI frameworks can support option awareness, trade-off analysis, and maintain user agency, which are key for good decision support."
  - "The current XAI paradigm is considered 'dead' for certain decision-making contexts, but the principles and tools of XAI remain essential for the new paradigm."
key_figures_tables:
  - "Table 1: The 10 cardinal decision issues defined by Yates and Potworowski → Highlights issues like options, possibilities, and trade-offs that are central to decision support."
  - "Table 2: Six criteria for good decision support → Defines a framework for evaluating decision aids, including options, judgement, and understandability."
  - "Table 3: How Explainable AI and Evaluative AI align against the human abductive reasoning process → Compares how each paradigm maps to steps of human reasoning."
  - "Table 4: A summary of the decision support provided by different paradigms → Shows that Evaluative AI provides support for options, possibilities, judgement, trade-offs, and understanding."
  - "Figure 6: A model of Evaluative AI → Illustrates a new interaction model where users generate hypotheses and the AI provides evidence for and against them."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "XAI"
    definition: "Explainable artificial intelligence."
  - term: "DA"
    definition: "Decision aid."
  - term: "Evaluative AI"
    definition: "A conceptual framework for decision support that provides evidence for and against human hypotheses without providing recommendations."
  - term: "Cognitive forcing"
    definition: "A strategy that forces decision makers to engage with a decision by withholding a recommendation initially."
  - term: "Option awareness"
    definition: "The analysis and understanding of various options and their relative trade-offs."
critical_citations:
  - "[Buçinca et al., 2021] — Shows explainability did not mitigate over-reliance."
  - "[Gajos and Mamykina, 2022] — Shows people do not engage cognitively with AI assistance."
  - "[Hoffman et al., 2022] — Argues abductive reasoning is a foundational model for XAI."
  - "[Klein et al., 2007] — Presents Data/Frame Theory, a model of sensemaking."
  - "[Rudin, 2019] — Advocates for interpretable models over black-box explanations."
relevance:
  topics:
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "high"
      justification: "Directly addresses trust calibration and the causes of over- and under-reliance on AI systems."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "high"
      justification: "Discusses user engagement with explanations and the lack of cognitive engagement with current XAI tools."
    - code: "11.B"
      name: "Retention Mechanisms and Engagement Design"
      relevance: "medium"
      justification: "Proposes a new paradigm (Evaluative AI) designed to improve user engagement by aligning with cognitive processes."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides criteria (Table 2) for evaluating the quality of decision support, relevant for assessing Odin's modules."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Critiques the general landscape of AI decision support, providing a foundation for understanding limitations in any system, including PFMS."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "low"
      justification: "Critiques the 'recommend and defend' model, which is a core function of budget recommendation, suggesting a need for a different approach."
    - code: "9.B"
      name: "Mobile UX Design for Personal Finance"
      relevance: "contextual"
      justification: "The conceptual framework for user interaction is relevant to UX design, though the paper does not specifically address mobile contexts."
  contribution: "This position paper provides a foundational critique of the recommendation-driven approach to AI-based decision support, which is central to Odin's budget recommendation and anomaly detection modules. It offers a new conceptual paradigm, Evaluative AI, which shifts the focus from providing answers to supporting user hypotheses. For Odin, this justifies a design where the system presents evidence (e.g., spending patterns, comparative data) for and against a user's financial decisions rather than just giving a budget. It directly informs the design of the UX and user interaction models, aiming to improve trust calibration and user engagement by maintaining agency and aligning with how humans naturally reason about finances."
  directly_justifies:
    - "Current recommendation-driven decision support can lead to over-reliance and under-reliance on AI systems."
    - "People do not always engage with explainability information, leading to poor trust calibration."
    - "Decision support should align with abductive reasoning, where users generate and test hypotheses."
    - "Providing evidence for and against user hypotheses can mitigate the negative effects of over- and under-reliance."
    - "Maintaining user agency and control over which hypotheses to explore is a key design criterion for effective decision support."
  limits:
    - "The paper is a position paper and does not provide empirical evidence to validate the Evaluative AI framework."
    - "It does not offer specific, implementable algorithms for generating evaluative evidence."
    - "It acknowledges that Evaluative AI may increase cognitive load and may be less preferred by users who want to avoid mental effort."
    - "The focus is on decision support in general, not the specific domain of personal finance or a Filipino context."
    - "It does not address the computational challenges of generating evidence for and against user hypotheses in real-time."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The core contribution of this paper directly addresses the fundamental design of AI systems for supporting human decisions, which is highly relevant to several of Odin's modules. The domain of User Retention & Engagement (11.A, 11.B) was flagged as high relevance because the paper's critique of user disengagement from XAI is a primary motivation for its new paradigm. The User Trust domain (10.B) is highly relevant as it directly discusses trust calibration and its failures. The System Evaluation domain (12.A) was marked medium due to the paper's provision of evaluation criteria for decision aids. Other domains like Behavioral Profiling (5.A) and Spending Forecasting (6.A) were considered but rejected because the paper does not address specific computational techniques for these functions but rather the overarching interaction model. The domains of Mobile Design (9.B), Budget Recommendation (7.B), and Existing Systems (4.A) were deemed contextual or low because while the concepts apply to Odin, the paper is not specific to these areas. Overall, the paper's relevance to Odin lies in its foundational critique and proposed paradigm for human-AI interaction, which can justify a user-centered design that prioritizes user agency and evidence-based evaluation over automated recommendations."
limitations:
  - "No empirical validation of the Evaluative AI framework is provided."
  - "The paper focuses on a theoretical conceptualization and does not propose specific algorithms for implementation."
  - "The framework may not be suitable for all decision-making scenarios, particularly those with low stakes or time constraints. [unacknowledged]"
  - "The potential for increased cognitive load and user preference for less work is acknowledged but not solved."
  - "The paper does not address how to handle disagreements between the user's hypothesis and the AI's evidence. [unacknowledged]"
  - "The framework assumes users are motivated to engage with the system, which may not hold in all contexts."
remember_this:
  - "Recommendation-driven XAI often leads to over-reliance or under-reliance on AI."
  - "People do not always engage with explainability tools, leading to poor decision outcomes."
  - "Evaluative AI provides evidence for and against user hypotheses instead of giving recommendations."
  - "Supporting abductive reasoning aligns decision support with human cognitive processes."
  - "Maintaining user agency and control over option exploration is critical for effective decision support."
```