```yaml
paper_id: 10.36227/techrxiv.173091273.31877417/v1
designation: local-algorithm-specific
title: Pitik: A Cebuano-Binisaya Intent-Based Chatbot for Cardiovascular Disease Patient Profiling and Risk Factor Recommendations
authors: Cedeño, J. G.; Manteza, A. E.; Nacar, N. C.; Umbukan, M. P.; Muaña, C. G.; Vasay, M. J.; Benablo, C. I. P.; Adlaon, K. M. M.
year: 2024
venue: TechRxiv
odin_topics:
  - 2.A
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
tldr: A Cebuano-Binisaya chatbot for cardiovascular risk assessment and patient profiling, using intent-based NLP and Gricean Maxims to enhance communication in underserved Philippine communities.
problem_and_motivation: Manual patient profiling in rural Philippine community health programs leads to fragmented data and hinders accurate diagnosis. Existing healthcare apps lack Cebuano-Binisaya support, excluding millions. A culturally and linguistically appropriate digital tool is needed to bridge this gap and improve cardiovascular care access.
approach:
  - Iterative software development with three iterations guided by Action Research and expert collaboration.
  - Utilized DialogFlow for intent matching, incorporating Pre-Intent and Post-Intent Matching algorithms.
  - Applied Gricean Maxims of conversation to detect communication violations and guide effective interaction design.
  - Evaluated Naive Bayes, SVM, MLP, and RNN for post-intent matching, selecting SVM for its superior performance.
  - Assessed chatbot quality using Analytic Hierarchy Process (AHP) with categories of Performance, Humanness, and Accessibility.
findings:
  - Iteration 3 significantly improved performance (65% to 79%) and accessibility (22% to 96%) via suggestion chips and tooltips.
  - SVM outperformed other models in the Smoking/Alcohol category with 73% accuracy and balanced precision/recall.
  - Suggestion chips and tooltips effectively addressed user unfamiliarity with medical terminology like HBA1C and Systolic Blood Pressure.
  - Users expressed dissatisfaction with lengthy conversational format and lack of medical tips, indicating areas for future development.
  - Gricean Maxim violations decreased from the second to third iteration across all categories (e.g., Manner: 44 to 22 violations).
key_figures_tables:
  - Figure 1: Iterative software development process of Pitik → Enabled continuous enhancements and refinements over three iterations.
  - Figure 2: Example of Grice Maxim occurrences in Pitik → Illustrates how violations (quantity, quality, relation, manner) were identified.
  - Figure 6: Hierarchical structure for Pitik chatbot evaluation → AHP criteria breakdown: Performance, Humanness, Accessibility.
  - Table 2: Gricean Maxims Violations → Showed reduction in violations from iteration 2 to 3 (e.g., Manner: 44 to 22).
  - Table 3: Model Performances for diet/exercise and smoking/alcohol areas → SVM achieved the highest accuracy (73%) for smoking/alcohol.
key_equations:
  - equation: "Risk Factors = (ln(Age) * 3.06117) + (ln(Total cholesterol) * 1.12370) - (ln(HDL cholesterol) * 0.93263) + (ln(Systolic blood pressure) * On blood pressure medication) + Cigarette smoker + Diabetes present - 23.9802"
    explanation: Framingham formula for computing cardiovascular risk factors from user data.
  - equation: "Risk = 100 * (1 - 0.88936e(Risk Factors))"
    explanation: Converts risk factors to a percentage risk score.
definitions:
  - term: CVD
    definition: Cardiovascular diseases, the leading cause of death in the Philippines.
  - term: Gricean Maxims
    definition: Four conversational principles (quantity, quality, relation, manner) for effective communication.
  - term: AHP
    definition: Analytic Hierarchy Process, a structured technique for complex decision-making.
  - term: DialogFlow
    definition: Google's natural language understanding platform for building conversational interfaces.
  - term: SVM
    definition: Support Vector Machine, a supervised machine learning model for classification.
critical_citations:
  - "[Cacciata et al., 2021] — CVD remains a leading cause of death in the Philippines."
  - "[D'Agostino et al., 2008] — Provides Framingham formula used for risk assessment."
  - "[Radziwill & Benton, 2017] — AHP method recommended for evaluating chatbot quality."
  - "[Reyes et al., 2023] — Community outreach programs in rural areas are key to healthcare access."
relevance:
  topics:
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: Provides a model for designing culturally and linguistically appropriate digital health tools.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews existing health apps (KonsultaMD) and their limitations, analogous to financial app landscape.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies gaps in existing systems, including lack of local language support and fragmented data.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: Methods for patient profiling (CVD risk) can be adapted for financial behavioral profiling.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Compares classification algorithms (SVM, NB, MLP, RNN) for user response intent, relevant to profile classification.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Addresses user accessibility and design for underserved communities, relevant to mobile-first considerations.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: UI/UX improvements like suggestion chips and tooltips are directly applicable to mobile app design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Mentions data collection and storage but does not focus on privacy/security mechanisms.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: Focuses on effectiveness and accessibility rather than trust-building mechanisms.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Uses AHP, a structured evaluation framework for assessing chatbot quality.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Rigorously evaluates intent matching algorithms using precision, recall, F1, accuracy.
  contribution: "Pitik demonstrates the successful implementation of a localized conversational AI for health profiling, offering a template for culturally adapted digital tools. Its iterative development and AHP-based evaluation framework provide a robust methodology for assessing system quality across multiple dimensions. The integration of Gricean Maxims offers a novel approach to enhancing communication in chatbot interactions, which can be applied to financial advisory contexts. The specific comparison of machine learning models for intent matching (SVM vs. Naive Bayes, etc.) provides actionable insights for selecting classification algorithms for user profiling tasks in Odin."
  directly_justifies:
    - "Culturally and linguistically appropriate tools are essential for user adoption in underserved communities."
    - "Iterative development with user feedback is critical for improving system performance and accessibility."
    - "SVM is a robust classifier for intent-based user responses, outperforming Naive Bayes and RNN on small datasets."
    - "Suggestion chips and tooltips significantly enhance user experience and data collection success rates."
    - "Performance should be prioritized over humanness and accessibility in system evaluation for functional effectiveness."
  limits:
    - "Limited to 100 participants, primarily accessible via social media, not strictly rural."
    - "Focus on CVD health profiling; direct transferability to personal finance requires validation."
    - "Specific evaluation tools (AHP, Gricean Maxims) may not be standard in all domains."
    - "No long-term user engagement or behavior change data provided."
    - "Model performance was tested on a balanced dataset of only 40 records; limited generalizability."
  mapping_rationale: "A systematic scan across all 12 functional domains identified three primary areas of relevance for Odin. The 'Existing Systems & Gaps' domain (topics 4.A, 4.B) is flagged as high relevance because the paper explicitly reviews current health apps and identifies missing local-language support and fragmented data—directly analogous to financial app gaps. The 'Behavioral Profiling & Classification' domain (topics 5.A, 5.C) is highly relevant because the study profiles users based on health risk and compares classification algorithms (SVM, NB) for intent matching, which maps directly to financial profile classification. The 'System Evaluation' domain (topics 12.A, 12.B) is flagged as high relevance for its rigorous AHP evaluation framework and algorithm benchmarking (precision, recall, F1). 'Mobile-First Design' (topics 9.A, 9.B) is flagged as medium relevance for its UX enhancements (suggestion chips, tooltips). 'Filipino Cultural Context' (topic 2.A) is contextual, providing a model for cultural adaptation. Topics related to 'Spending Forecasting' (6.A, 6.B), 'Budget Recommendation' (7.A-D), 'Anomaly Detection' (8.A-C), 'Savings & Debt' (13.A-C), and 'Engagement' (11.A, 11.B) were considered and rejected as the paper does not address spending, budgeting, anomalies, savings, debt, or engagement dynamics. Overall, the paper is highly relevant for its methodologies in localized system development, user profiling, and algorithmic evaluation, which can directly inform Odin's design and testing phases."
limitations:
  - "Small sample size (n=100) limits generalizability. [unacknowledged]"
  - "The study was conducted on a preprint and not yet peer-reviewed."
  - "SVM performance was only tested on 40 records, which is insufficient to draw strong conclusions."
  - "Focus on health, not finance, requiring adaptation of profiling and classification methods."
  - "Humanness and accessibility were less prioritized, which may not align with all user experience goals."
remember_this:
  - "SVM achieved 73% accuracy for intent classification on a small dataset."
  - "Iteration 3 boosted accessibility from 22% to 96% using suggestion chips and tooltips."
  - "Performance was weighted 0.79, far outweighing humanness and accessibility in evaluation."
  - "Gricean Maxims were used to identify communication violations and improve chatbot interaction."
  - "Culturally adapted, localized chatbots can significantly improve data collection in underserved areas."
```