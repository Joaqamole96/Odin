```yaml
paper_id: 10.62718/vmca.tech-gjtdsi.7.1.SC-0226-025
designation: international-algorithm-specific
title: Hybrid Recommendation System for Patient-Centric Traditional Chinese Medicine E-Commerce: A Rule-Based Approach with Nlp And K-Nn Integration
authors: Wang, J.; Escober, R. E.
year: 2026
venue: Technologique: A Global Journal on Technological Developments and Scientific Innovations
odin_topics:
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 7.B
  - 7.C
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 9.A
  - 9.B
tldr: A hybrid recommendation system integrates NLP and K-NN to provide clinically aligned product suggestions for Traditional Chinese Medicine e-commerce.
problem_and_motivation: Existing TCM e-commerce platforms lack personalization, relying on generic recommendations that fail to leverage patient-specific clinical data. This gap leads to patient non-adherence, suboptimal health outcomes, and a disconnect between online purchasing and clinical care, especially in the Philippine context where trust is a significant concern.
approach:
  - The study used Design Science Research (DSR) with a mixed-methods framework.
  - A hybrid model combines Content-Based Filtering (CBF) as a clinical gatekeeper with Collaborative Filtering (CF) for personalization.
  - The system uses a Drools Business Rules Management System for clinical logic with 247 rules.
  - The technical stack includes PostgreSQL, Redis, Vue.js, and a microservices architecture.
  - Primary data comprised 100 anonymized health records and survey responses from 159 participants.
  - The system was evaluated using ISO 25010 quality standards and the Technology Acceptance Model (TAM).
findings:
  - num: Integration with Clinical Care was the most critical failure in current systems, with a mean score of 4.40.
  - num: The system achieved an overall ISO 25010 quality score of 4.23/5.00.
  - num: Security (4.48) and Functional Suitability (4.47) were the highest-rated ISO characteristics.
  - Compatibility (3.65) was identified as a primary weakness for the system.
  - num: The overall TAM acceptance composite score was 3.91/5.00, indicating a strong positive reception.
  - num: Behavioral Intention scored highest at 3.96, with Recommendation Willingness at 4.00.
  - Practitioner alignment scored 4.45/5.00, highlighting strong trust in the system’s clinical basis.
  - Users expressed hesitation about replacing in-person care (3.75), aligning with the system's design as a complement.
  - The study found that rule-based systems can achieve 71% diagnostic accuracy with limited data.
  - The hybrid system achieved 88% accuracy in herbal formula selection in related work.
key_figures_tables:
  - Figure 1: Conceptual Framework → Shows integration of patient records and e-commerce behavior.
  - Table 4: Challenges in Current TCM Purchasing Systems → Highlights severe gaps in clinical integration and education.
  - Table 5: ISO 25010 Quality Assessment Results → Security and Functional Suitability scored highest.
  - Table 6: Technology Acceptance Model Results → Behavioral Intention was the highest-scoring dimension.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: TCM
    definition: Traditional Chinese Medicine
  - term: NLP
    definition: Natural Language Processing
  - term: K-NN
    definition: k-nearest neighbours
  - term: CBF
    definition: Content-Based Filtering
  - term: CF
    definition: Collaborative Filtering
  - term: XAI
    definition: Explainable AI
  - term: DSR
    definition: Design Science Research
  - term: TAM
    definition: Technology Acceptance Model
  - term: EHR
    definition: Electronic Health Record
critical_citations:
  - "[Ricci et al., 2021] — CF accuracy only 61% for medical products."
  - "[Sutton et al., 2020] — Rule-based systems improve protocol adherence by 23%."
  - "[Holzinger et al., 2021] — 78% of clinicians prefer rule-based over black-box AI."
  - "[Dela Cruz et al., 2023] — 85% of Filipino patients demand TCM-grounded explanations."
  - "[Wong et al., 2023] — Hybrid system achieved 88% accuracy for herbal formula selection."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: This paper analyzes the landscape of TCM e-commerce systems, identifying critical failures and gaps.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: The study specifically addresses limitations like lack of personalization and the cold-start problem.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Using similar patient profiles (via K-NN) is analogous to creating behavioral profiles for spending.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: high
      justification: The system directly tackles the cold-start problem by prioritizing clinical data for new users.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: The K-NN algorithm is a classification approach for identifying similar patient profiles.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: contextual
      justification: The concept of a "clinical gatekeeper" is analogous to constrained recommendation, similar to budget allocation.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: low
      justification: The paper does not focus on optimization, but the rule-based approach acts as a constraint.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: The paper's focus on contraindications is related to anomaly detection, but not a core topic.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Rule-based logic for safety is similar to anomaly detection but not the paper's primary focus.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: The study adheres to the Philippine Data Privacy Act (RA 10173) and emphasizes data anonymization.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: The paper's emphasis on explainability and clinical relevance directly addresses user trust.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: The system includes a mobile interface (React Native), addressing mobile-first design.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: The study includes a multilingual (English/Tagalog) UI, which is a mobile UX consideration.
  contribution: The paper provides a concrete framework for building a hybrid recommendation system that balances clinical rules with collaborative filtering. This framework can be adapted for Odin's budget recommendation module, where clinical relevance is analogous to financial health. The evaluation using ISO 25010 and TAM offers a validated methodology for assessing both the technical quality and user acceptance of such a system. The focus on explainability and data privacy directly informs Odin's design principles for building user trust.
  directly_justifies:
    - Rule-based systems are essential for maintaining therapeutic integrity and safety in clinical contexts.
    - Hybrid approaches that combine explicit rules with collaborative filtering are essential for building trust in AI-driven systems.
    - Integrating user feedback loops is critical for continuous algorithmic improvement.
    - High user acceptance is achievable when systems are designed to complement, not replace, professional expertise.
  limits:
    - The study is limited to the Philippine context and TCM, which may not generalize to other domains.
    - Compatibility with existing EHR systems was identified as a weakness [unacknowledged].
    - The study did not address long-term user retention or engagement dynamics.
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The domains "Existing Systems & Gaps" (4.A, 4.B), "Behavioral Profiling & Classification" (5.A, 5.B, 5.C), "Data Privacy & User Trust" (10.A, 10.B), and "Mobile-First Design" (9.A, 9.B) were flagged as highly relevant. The paper directly addresses the limitations of current systems and proposes a classification approach that mitigates the cold-start problem, with a strong emphasis on privacy and trust. The "Budget Recommendation" (7.B, 7.C) and "Anomaly Detection" (8.A, 8.B) domains were deemed contextual or low relevance because the paper focuses on product recommendation rather than financial allocation or spending anomalies, though the concepts are analogous. The domains "Filipino Cultural Context" (2.A-D) and "Savings & Debt Management" (13.A-C) were considered and rejected as they are not central to the paper's contribution. Overall, the paper is highly relevant to Odin for its methodological approach to personalized recommendation and its validated framework for building user trust through explainability and data privacy.
limitations:
  - The study is limited to the Philippine context and TCM domain.
  - Compatibility with existing EHR systems was identified as a weakness.
  - The study did not address long-term user retention or engagement dynamics.
  - The sample size of 159 participants may limit the generalizability of the TAM results.
remember_this:
  - Rule-based systems achieved 71% diagnostic accuracy with limited data.
  - Hybrid recommendation systems balance algorithmic precision with interpretability.
  - User trust is built through explainability and clinical relevance in healthcare AI.
  - Compatibility with existing clinical systems is a critical challenge for adoption.
  - TAM results show strong user acceptance, with Behavioral Intention scoring 3.96/5.00.
```