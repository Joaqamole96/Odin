```yaml
paper_id: 10.1007/s11257-025-09438-0
designation: international-algorithm-specific
title: Exploring the impact of explainable AI and cognitive capabilities on users' decisions
authors: Cau, F. M.; Spano, L. D.
year: 2026
venue: User Modeling and User-Adapted Interaction
odin_topics:
  - 8.B
  - 10.A
  - 5.A
  - 12.A
  - 12.B
  - 9.A
  - 10.B
  - 11.A
tldr: High AI confidence increases user reliance and reduces cognitive load, while counterfactual explanations improve accuracy and appropriate reliance despite being less understandable.
problem_and_motivation: The effectiveness of feature-based explanations in AI-assisted decision-making is inconclusive, and the influence of AI confidence on cognitive load is understudied. Additionally, the role of the Need for Cognition personality trait in prioritizing XAI information and explanation styles remains unclear.
approach:
  - Conducted an online user study with 288 participants on a loan approval task.
  - Used a Random Forest classifier with 83% test accuracy on a public loan dataset.
  - Compared six AI assistance conditions: no AI, AI with no explanation, and AI with example-based, feature-based, rule-based, and counterfactual explanations.
  - Measured participants' Need for Cognition (NFC) using the NCS-6 scale and split them into low and high groups.
  - Evaluated decision accuracy, reliance on AI, cognitive load (SEQ), and prioritization of interface elements.
findings:
  - num: High AI confidence significantly increases reliance on AI (Log-Odds=1.22) and reduces cognitive load (Log-Odds=-0.41).
  - Feature-based explanations did not improve user accuracy compared to other conditions.
  - num: Counterfactual explanations increased reliance on correct AI predictions (Log-Odds=0.98) and reduced cognitive load (Log-Odds=-0.48).
  - No significant differences were found between low and high NFC groups in accuracy, cognitive load, or the prioritization of explanations.
  - Both low and high NFC users prioritized loan attributes first, explanations second, and AI information third.
  - Counterfactual explanations were perceived as less understandable but still provided performance benefits.
  - The stated AI accuracy (83%) differed from the observed accuracy (62.5%) in the study instances.
key_figures_tables:
  - Figure 3: Reliance and cognitive load by AI confidence → High confidence increases reliance and lowers cognitive load.
  - Figure 4: Interface rank frequencies by NFC → Both groups ranked loan attributes first, explanations second.
  - Figure 6: Post-hoc analysis of AI correctness and interface ranking → Counterfactuals improve reliance and load when AI is correct.
  - Figure 7: Interface component understanding by condition → Counterfactuals lower explanation understandability.
  - Table 1: Instance settings for the study → Balanced selection of 8 tasks with controlled AI confidence and correctness.
  - Table 4: Metrics overview by task → Performance split shows over-reliance on high-confidence wrong AI predictions.
key_equations:
  - equation: "Log-Odds = 1.22, Std. error = 0.12, z-value = 10.40, p < .01"
    explanation: High AI confidence increases reliance on AI.
  - equation: "Log-Odds = -0.41, Std. error = 0.06, Wald = 54.57, p < .01"
    explanation: High AI confidence decreases cognitive load.
definitions:
  - term: Need for Cognition (NFC)
    definition: A personality trait reflecting an individual's tendency to engage in and enjoy effortful cognitive activities.
  - term: Explainable AI (XAI)
    definition: Techniques to help users understand how AI systems reach decisions.
  - term: Counterfactual Explanation
    definition: A "what-if" explanation showing changes needed to alter an AI's prediction.
  - term: Cognitive Load
    definition: The mental effort required to perform a task, measured via the Single Ease Question (SEQ).
critical_citations:
  - "[Zhang et al., 2020] — Found high AI confidence increases reliance."
  - "[Rechkemmer and Yin, 2022] — Showed AI confidence effects depend on stated accuracy."
  - "[Buçinca et al., 2021] — Found NFC differences with cognitive forcing functions."
  - "[Wang and Yin, 2022] — Showed feature contribution satisfies more XAI desiderata."
  - "[Chen et al., 2023] — Found example-based explanations improve accuracy with correct AI."
relevance:
  topics:
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Provides empirical evidence on how different XAI styles affect user behavior, relevant to explaining anomalies.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Discusses trust and reliance on AI, which are relevant to data privacy perceptions.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Explores individual differences (NFC) in decision-making, relevant to profiling.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a robust experimental framework for evaluating AI-assisted decision-making.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Evaluates the effectiveness of different explanation algorithms (SHAP, Anchors, DiCE) in user studies.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: contextual
      justification: Discusses user interface and cognitive load considerations applicable to mobile design.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Directly studies user reliance and trust calibration in AI systems.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: Mentions user engagement, but the study focuses primarily on decision accuracy and cognitive load.
  contribution: This study provides a rigorous empirical framework for evaluating explanation styles in high-stakes decision-making, directly applicable to Odin's design. It validates that counterfactual explanations, despite lower perceived understandability, can improve user accuracy and appropriate reliance. The findings on AI confidence's role in reducing cognitive load inform the design of Odin's feedback mechanisms. The study's methodology for measuring reliance and cognitive load can be adapted to evaluate Odin's algorithmic modules, such as budget recommendation and anomaly detection. It highlights the importance of user-centric personalization, suggesting that Odin should tailor explanations based on user characteristics beyond the NFC trait.
  directly_justifies:
    - Counterfactual explanations improve user accuracy and reduce cognitive load when AI predictions are correct.
    - High AI confidence increases user reliance and decreases cognitive load, which must be managed carefully in Odin.
    - Feature-based explanations do not consistently improve user accuracy over other explanation types.
    - NFC may not be a reliable differentiator for personalizing XAI in complex financial tasks.
    - System evaluation should include measures of user reliance, cognitive load, and interface element prioritization.
  limits:
    - The study used a one-stage AI paradigm, which may not separate user reasoning from AI anchoring.
    - AI confidence estimates were not calibrated, potentially affecting user reliance patterns.
    - The findings are based on a specific loan dataset and may not generalize to other financial tasks.
    - Only the NFC personality trait was examined, limiting conclusions about other user characteristics.
  mapping_rationale: A systematic scan was performed across all 12 functional domains and their associated topic codes. The paper was flagged as highly relevant to Anomaly Detection (8.B) and System Evaluation (12.A, 12.B) due to its experimental evaluation of XAI techniques and their impact on decision-making. It was deemed of medium relevance to Behavioral Profiling (5.A) and User Trust (10.B) because it explores individual differences (NFC) and reliance. The paper's focus on cognitive load and interface design provides contextual relevance to Mobile-First Design (9.A). Topics related to Expense Categorization (3), Budget Recommendation (7), and Savings & Debt Management (13) were considered but rejected as the paper does not address these specific functional concerns. Borderline cases included the overlap between user trust (10.B) and reliance behavior, which were both captured. The overall contribution is a validated methodology for evaluating XAI in financial decision-making, directly informing Odin's user experience and system evaluation strategies.
limitations:
  - The AI model used uncalibrated confidence estimates, which may have skewed user reliance patterns.
  - The one-stage decision paradigm limits the ability to disentangle independent user reasoning from AI influence.
  - The study only examined the Need for Cognition trait, potentially overlooking other important user characteristics.
  - Results may not generalize to expert users or other financial domains due to low participant familiarity with loan approval.
  - The selected dataset and specific explanation generation methods may limit the replicability of findings [unacknowledged].
  - The study design with a stated 83% accuracy but observed 62.5% accuracy may introduce behavioral inconsistencies [unacknowledged].
remember_this:
  - High AI confidence increases user reliance and reduces mental effort.
  - Counterfactual explanations improve accuracy but are less understandable to users.
  - Feature-based explanations do not guarantee better decision-making outcomes.
  - Need for Cognition differences may diminish as task complexity increases.
  - System evaluation must measure reliance, cognitive load, and interface prioritization.
```