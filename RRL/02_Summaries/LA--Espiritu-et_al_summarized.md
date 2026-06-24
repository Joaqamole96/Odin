```yaml
paper_id: 6c9e3b8a-4f5d-5a8e-9b2c-1f3a4b5c6d7e
designation: local-algorithm-specific
title: Data-Driven Decision Making in Scholarship Programs: Leveraging Decision Trees and Clustering Algorithms
authors: Espiritu, F. V.; Natividad, M. C. B.; Velasco, R. A.
year: 2024
venue: International Journal in Information Technology in Governance, Education and Business
odin_topics:
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 9.A
  - 9.B
  - 12.A
  - 12.B
tldr: Integrates decision trees and clustering with an online system to improve efficiency and decision-making for a Philippine scholarship program facing a massive application surge.
problem_and_motivation: The BRO-Ed scholarship program in Isabela province faces a 541.1% surge in applications, overwhelming its manual review process. This lack of systematic evaluation leads to inefficiency and risks missing key success factors, necessitating a data-driven solution to improve selection and resource allocation.
approach:
  - Historical scholarship application data from the PGI BRO Ed Scholarship program was integrated and preprocessed to ensure quality and integrity.
  - Decision tree (C4.5) and K-means clustering algorithms were implemented on the cleaned dataset for pattern recognition and insight extraction.
  - A user-friendly online registration platform was developed using Handlebars.js, Node.js with Express.js, and MySQL to enhance accessibility.
  - Algorithm performance was evaluated using accuracy, precision, recall, and F1-score metrics.
  - The system's impact was assessed through user satisfaction surveys and comparative success rate analysis against traditional methods.
findings:
  - Preprocessing identified parent occupation, academic performance, and financial need as high-impact factors influencing scholarship success.
  - num: 31% higher success rate was observed for applicants using the online system compared to traditional methods.
  - The implemented algorithms achieved an 80% predictive accuracy for successful scholarship applications.
  - User satisfaction surveys indicated a high preference for the online system due to its ease of use and accessibility.
  - The integration of data mining techniques revealed hidden patterns, enabling more informed and fairer selection decisions.
key_figures_tables:
  - Figure 4: Impact of online registration system on success rates → Demonstrates a 31% improvement over traditional methods.
  - Table 5: Factors influencing scholarship application success → Identifies parent occupation, academic performance, and financial need as high-impact factors.
  - Figure 5: Comparison of predictive accuracy for scholarship application outcomes → Shows 80% accuracy for predicting success vs. 70% for failure.
key_equations:
  - equation: "Accuracy = (TP + TN) / (TP + TN + FP + FN)"
    explanation: Proportion of correctly classified instances among all cases.
  - equation: "Precision = TP / (TP + FP)"
    explanation: Proportion of true positives among all positive predictions.
  - equation: "Recall = TP / (TP + FN)"
    explanation: Proportion of true positives identified correctly.
  - equation: "F1-score = 2 * (Precision * Recall) / (Precision + Recall)"
    explanation: Harmonic mean of precision and recall, balancing both metrics.
definitions:
  - term: C4.5 Algorithm
    definition: A well-known decision tree algorithm used to handle categorical and numerical data effectively.
  - term: K-Means Clustering
    definition: A simple and efficient algorithm for partitioning a dataset into groups with similar properties.
  - term: PII
    definition: Personally Identifiable Information, which was anonymized to protect applicant privacy.
critical_citations:
  - "[Yağcı, 2022] — Provides basis for predictive modeling using ML algorithms."
  - "[Alyahyan & Düştegör, 2020] — Offers literature review and best practices for predictive modeling."
  - "[Sugiyarti et al., 2018] — Demonstrates integration of data-driven approaches in scholarship administration."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides a case study of a public system (scholarship) transitioning to a data-driven approach.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly addresses operational challenges like manual review and processing bottlenecks.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: The method groups applicants (clustering), which is analogous to profiling.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses decision trees (classification) to predict success based on applicant features.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: Mentions a "user-friendly online platform" and improved accessibility for remote areas.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: Discusses front-end framework (Handlebars.js) and interface design but not finance-specific UX.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Evaluates system effectiveness using quantitative metrics (accuracy, user satisfaction).
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Explicitly evaluates the prediction algorithms using accuracy, precision, recall, and F1-score.
  contribution: "This paper directly informs Odin's System Evaluation module (12.B) by demonstrating a clear evaluation framework for algorithmic modules using accuracy, precision, recall, and F1-score. Its approach to handling a surge in applications via an online system and data mining provides a justification for Odin's mobile-first design and anomaly detection modules. The identification of key success factors (parental occupation, academic performance) offers a methodological example for feature importance analysis. Its emphasis on user accessibility and satisfaction supports the rationale for Odin's engagement and retention design."
  directly_justifies:
    - "Data mining techniques like decision trees and clustering can systematically evaluate a high volume of applications."
    - "An online system is critical for managing a large influx of applications and improving accessibility."
    - "User satisfaction and success rates are higher with a digital, data-driven system compared to traditional methods."
  limits:
    - "Focuses on scholarship selection, not personal finance management; direct applicability to spending behavior is limited."
    - "The evaluation metrics (accuracy, precision) are tied to classification tasks and may not fully capture the nuance of financial behavior." [unacknowledged]
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to 'Existing Systems & Gaps' (topics 4.A, 4.B) because it directly addresses the operational challenges of a manual system handling a massive application surge. It was also flagged as relevant to 'System Evaluation' (12.A, 12.B) due to its explicit use of quantitative metrics to evaluate algorithmic performance. Relevance to 'Behavioral Profiling & Classification' (5.A, 5.C) was assessed as contextual/medium, as the clustering and classification approach is methodologically similar to profiling but applied to scholarship applicants rather than financial behavior. The domains of 'Expense Categorization', 'Spending Forecasting', 'Budget Recommendation', 'Anomaly Detection', 'Data Privacy & User Trust', 'User Retention & Engagement', and 'Savings & Debt Management' were considered and rejected due to the paper's focus on scholarship administration, which provides no direct insights or citations for these personal finance areas. Overall, the paper's relevance to Odin is primarily methodological and evaluative, providing a strong example of system evaluation and gap identification, rather than providing domain-specific financial behavior insights."
limitations:
  - "The study is specific to scholarship programs, not personal finance management, limiting the generalizability of its findings."
  - "The evaluation is based on a single case study (BRO-Ed scholarship), lacking cross-program validation." [unacknowledged]
  - "The long-term impact on user retention and engagement beyond initial application is not assessed." [unacknowledged]
  - "The paper does not address the cold-start problem or other dynamic aspects of the system." [unacknowledged]
remember_this:
  - "Manual review of 34,426 applications is inefficient and error-prone."
  - "Decision trees and clustering can automate and improve selection accuracy."
  - "Online systems increase accessibility and user satisfaction significantly."
  - "num: The online system achieved a 31% higher success rate than traditional methods."
```