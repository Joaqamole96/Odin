```yaml
paper_id: 10.1145/3630106.3658997
designation: international-algorithm-specific
title: Actionable Recourse for Automated Decisions: Examining the Effects of Counterfactual Explanation Type and Presentation on Lay User Understanding
authors: VanNostrand, P. M.; Hofmann, D. M.; Ma, L.; Rundensteiner, E. A.
year: 2024
venue: The 2024 ACM Conference on Fairness, Accountability, and Transparency (FAccT’24)
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 8.A
  - 8.B
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 12.A
  - 12.B
tldr: Region-based counterfactual explanations significantly improve lay user understanding, confidence, and trust in automated loan approval decisions compared to point-based explanations, but presentation style affects response time only.
problem_and_motivation: Automated decision systems are deployed in consequential domains, yet counterfactual explanation design is driven by computational metrics that do not capture lay user needs. There is a critical gap in evaluating how different counterfactual explanation types and presentations affect user understanding and ability to take actionable recourse.
approach:
  - Conducted a crowd-sourced between-subjects user study with 252 participants on Prolific.
  - Used a loan approval scenario with a random forest classifier trained on Kaggle loan data.
  - Generated explanations using the state-of-the-art FACET algorithm for region-based and point-based counterfactuals.
  - Implemented six explanation configurations varying by type (point-based vs. region-based) and presentation (numeric, natural language, visual).
  - Evaluated objective understanding (12 task questions across three recourse areas), subjective understanding, response confidence, response time, satisfaction, and trust.
findings:
  - num: Region-based counterfactuals significantly increase objective understanding (F(1,252)=217.34, p<2e-16, η²_p=0.4694) over point-based.
  - num: Region-based explanations improve subjective understanding (F(1,252)=60.91, p=1.71e-13, η²_p=0.1984) and response confidence (F(1,252)=42.41, p=4.14e-10, η²_p=0.1474).
  - Presentation style moderates the effect of explanation type on response confidence (F(2,252)=6.18, p=2.41e-3, η²_p=0.0478).
  - Both subjective understanding and response confidence are significant positive predictors of objective understanding (R²=0.24, p=4.82e-16).
  - Visual presentations significantly reduce response time compared to natural language (p=3.94e-3).
  - Region-based explanations lead to significantly higher user satisfaction (p<8e-11) and trust (p<1.74e-4).
key_figures_tables:
  - Figure 1: Explanation user interface layout showing decision, factual values, and counterfactual explanation area.
  - Figure 2: Six counterfactual explanation configurations (point vs. region type, numeric vs. natural language vs. visual presentation).
  - Figure 3: Mean objective understanding, subjective understanding, and response confidence scores across configurations, showing region-based outperforms point-based.
  - Figure 4: Mean response time, satisfaction, and trust scores across configurations, showing visual presentation has fastest response time.
  - Table 1: Results of statistical tests for main hypotheses, showing significant effects for region-based type on all understanding and confidence metrics.
  - Table 2: Extracted quotes from open response questions illustrating qualitative themes.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Counterfactual Explanation
    definition: An explanation that describes alterations to an instance's features that would change a negative outcome to a positive one.
  - term: Point-based Counterfactual
    definition: A counterfactual explanation that provides a single set of exact feature values to achieve the desired outcome.
  - term: Region-based Counterfactual
    definition: A counterfactual explanation that provides a continuous bounded range for each feature within which any point is guaranteed the desired outcome.
critical_citations:
  - "[Wachter et al., 2017] — Establishes counterfactuals for GDPR legal compliance."
  - "[Karimi et al., 2022] — Surveys algorithmic recourse and contrastive explanations."
  - "[Guidotti, 2022] — Reviews counterfactual explanation methods and metrics."
  - "[Miller, 2019] — Links XAI to psychological theories of human reasoning."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Demonstrates that explanation type affects user confidence and perceived understanding, relevant to profile calibration.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: contextual
      justification: Provides a framework for evaluating user understanding, which informs dynamic profile updates.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: contextual
      justification: User understanding of model behavior is a prerequisite for accurate profile classification.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Understanding model behavior and decision boundaries is relevant to detecting anomalous spending.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: The paper uses counterfactual explanation methods, not anomaly detection algorithms.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: The study explicitly tests visual and natural language presentation styles, directly informing UI design choices.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: high
      justification: Findings that visual presentations reduce response time have direct implications for mobile app UX.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: The paper addresses user trust in automated decision systems, a component of data privacy concerns.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Finds that region-based counterfactuals significantly increase user trust in the automated decision system.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: User confidence and understanding are key drivers of engagement with explanation tools.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: low
      justification: Response time differences by presentation style can impact user retention and engagement.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a validated methodology (objective and subjective metrics) for evaluating explanation interfaces.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Directly compares two types of counterfactual explanation algorithms (point vs. region).
  contribution: This paper provides a rigorous, validated evaluation framework for user understanding of counterfactual explanations. Its finding that region-based explanations improve user confidence and trust directly justifies implementing such explanations in Odin to enhance user trust. The study's methodology for measuring objective understanding (feature alteration, instance prediction, feature sensitivity) can be adapted for evaluating Odin's explanation and anomaly detection modules. Results showing that visual presentation reduces response time inform Odin's mobile-first UX design to ensure efficient user interaction.
  directly_justifies:
    - "Region-based counterfactual explanations significantly improve user objective understanding (p<2e-16)."
    - "Region-based explanations increase user trust in automated systems (p<1.74e-4)."
    - "Visual presentation of explanations significantly reduces user response time (p=3.94e-3)."
    - "User response confidence is a significant positive predictor of objective understanding (p<2e-16)."
  limits:
    - "Findings are specific to a loan application scenario and may not generalize to other personal finance domains."
    - "Study uses a crowd-sourced population, not actual users of a PFMS system."
    - "The three presentation styles were designed to be consistent, which may not represent optimal designs for each modality."
    - "Does not evaluate the effect of explanations on actual user behavior or financial decision-making outcomes."
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The paper's core focus on user understanding of counterfactual explanations directly maps to Behavioral Profiling & Classification (5.A, 5.B, 5.C) and System Evaluation (12.A, 12.B). The explicit testing of presentation styles (visual vs. text) provides strong justification for Mobile-First Design (9.A, 9.B). Findings on trust and satisfaction are highly relevant to User Trust (10.B) and Engagement (11.A). The paper's discussion of how users interpret model behavior has contextual relevance to Anomaly Detection (8.A). Domains like Expense Categorization (3.A-C), Spending Forecasting (6.A-B), Budget Recommendation (7.A-D), and Savings & Debt Management (13.A-C) were considered but rejected as the paper does not address these specific financial functions. The overall relevance is high, providing actionable design guidelines and evaluation methods for Odin's explanation and user interface components.
limitations:
  - "Study scenario specific to loan applications; may not fully generalize to PFMS spending contexts."
  - "Crowd-sourced participants may not represent the Filipino young professional demographic."
  - "Presentation styles were limited to three specific designs; other visual or interactive formats may yield different results."
  - "Subjective understanding and confidence are self-reported and may not perfectly reflect actual internal states."
  - "The study does not measure long-term retention or behavioral change from explanations. [unacknowledged]"
  - "Potential confounding effects of participant assumptions about loan approval were controlled but may still persist. [unacknowledged]"
remember_this:
  - "Region-based counterfactuals improve objective understanding by 3.78 points on average."
  - "Users are more confident and trust automated decisions more with region-based explanations."
  - "Visual presentation of counterfactuals halves response time compared to natural language."
  - "User confidence is a stronger predictor of objective understanding than subjective understanding."
  - "Effective explanation design must consider both content type and presentation modality."