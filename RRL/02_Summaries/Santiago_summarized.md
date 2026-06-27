```yaml
paper_id: 10.26483/ijarcs.v16i3.7256
designation: local-algorithm-specific
title: BUDGET AND FINANCIAL MANAGEMENT INFORMATION SYSTEM FOR PUBLIC ELEMENTARY SCHOOLS: ANALYTICS AND PREDICTIVE INSIGHTS FOR MOOE ALLOCATION USING LINEAR REGRESSION
authors: Santiago, R. L. T.; Villarica, M. V.; Bernardino, M. P.
year: 2025
venue: International Journal of Advanced Research in Computer Science
odin_topics:
  - 1.A
  - 1.B
  - 2.D
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 7.C
  - 7.D
  - 8.A
  - 8.B
  - 9.A
  - 10.A
  - 10.B
  - 11.A
  - 12.B
tldr: Develops an AI-driven financial management system for Philippine public schools that uses linear regression to forecast Maintenance and Other Operating Expenses allocations.
problem_and_motivation: Public elementary schools in the Philippines face significant challenges in managing financial resources due to reliance on manual processes that are prone to errors, inefficiencies, and a lack of transparency. There is a lack of dedicated, digital financial management systems tailored to the operational needs of these schools. This study addresses the need for an automated, accountable, and data-driven solution to improve budget allocation, expenditure tracking, and compliance with DepEd regulations.
approach:
  - The system was developed using an Agile methodology, incorporating continuous stakeholder feedback from school administrators and DepEd auditors.
  - The core AI feature uses a linear regression model built with Python and Scikit-learn to forecast future MOOE allocations based on historical spending data.
  - The system includes modules for budget allocation, expenditure tracking with real-time dashboards, and automated DepEd-compliant report generation.
  - The system was built using XAMPP for local server environment, PHP for dynamic pages, MySQL for database, and Dompdf/PhpSpreadsheet for report generation.
  - A black-box testing approach was employed, using equivalence partitioning to validate system functionality and robustness across key modules.
  - System quality was evaluated against ISO/IEC 25010 and ISO 27001 standards, and user acceptance was assessed using the Technology Acceptance Model.
findings:
  - num: The linear regression model achieved an R² score of 92.81%, indicating high explanatory power for budget variance.
  - num: The model's Mean Absolute Error was ₱1,532.75, and Root Mean Square Error was ₱2,126.84, confirming minimal prediction errors.
  - num: Black-box testing was conducted with 37 test cases, with most modules passing successfully and only minor UI and validation issues identified.
  - num: User acceptance evaluation showed strong approval with weighted means above 4.3 on a 5-point scale across all TAM dimensions.
  - The BFMIS enhances financial transparency and accountability through real-time dashboards and audit trails for school administrators and auditors.
  - AI-driven reporting automates the generation of financial summaries and variance analysis reports, reducing manual effort and aligning with DepEd policies.
  - The system's ability to generate predictive insights enables proactive, evidence-based decision-making for budget planning.
key_figures_tables:
  - Table 2: Black Box Test Case Table summarizes the functional coverage and test case execution across all system modules.
  - Table 4: Regression Model Performance presents MAE, RMSE, and R² score, confirming the predictive model's reliability.
  - Table 5: Summary of Evaluation Results shows high user ratings for system quality, ease of use, and satisfaction.
  - Figure 8: MOOE Prediction Page visualizes the comparison between predicted and actual budget allocations, highlighting data-driven insights.
  - Figure 10: Actual vs. Predicted MOOE Allocations per Category illustrates the model's accuracy in forecasting category-wise budgets.
key_equations:
  - equation: R^2 = 0.9281
    explanation: Indicates model explains 92.81% of budget variance.
  - equation: MAE = ₱1,532.75
    explanation: Represents the average absolute prediction error in pesos.
  - equation: RMSE = ₱2,126.84
    explanation: Confirms minimal large prediction errors enhancing reliability.
definitions:
  - term: MOOE
    definition: Maintenance and Other Operating Expenses, government-allocated funds for school operations.
  - term: BFMIS
    definition: Budget and Financial Management Information System developed in this study.
  - term: TAM
    definition: Technology Acceptance Model, a framework for assessing user acceptance of technology.
  - term: DepEd
    definition: Department of Education, the governing body for Philippine public schools.
  - term: AIP
    definition: Annual Implementation Plan, a tool for school-based management translating long-term goals into yearly actions.
critical_citations:
  - "[Pressman & Maxim, 2014] — Provides black-box testing guidelines for software validation."
  - "[Venkatesh & Davis, 2000] — Foundation for the Technology Acceptance Model used in UAT."
  - "[Byol & Foygel, 2023] — Insight on black box testing for financial systems."
  - "[Roustaei, 2024] — Justifies use of linear regression for predictive modeling with limited data."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: The study focuses on financial management within public schools, a context relevant to the financial environment of Filipino professionals.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: contextual
      justification: The paper analyzes budget allocation structures (MOOE) within the Philippine public school system, which is part of the financial landscape for professionals in education.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: The study mentions cyclical spending patterns for items like electricity and graduation programs, touching on seasonal school-related expenses.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: The BFMIS includes modules for categorizing MOOE expenses, providing a framework for organizing school expenditures.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: The design of the system's expense tracker and reporting module reflects considerations for effective financial data organization.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: The study explicitly reviews the landscape of existing financial management systems in Philippine public schools and their limitations.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: The research is motivated by identified gaps in manual financial processes, directly addressing limitations of current systems.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: The core contribution is the development of a predictive linear regression model for budget forecasting, a key predictive modeling application.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: The linear regression algorithm forecasts future MOOE allocations based on historical sequential spending data.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: The paper discusses participatory budgeting strategies and the use of the AIP, which are relevant domain knowledge for budget recommendation.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: While not strictly a recommendation system, the predictive module provides data-driven suggestions for future budget allocations.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: low
      justification: The system optimizes allocation based on historical trends, but not in a formal constrained optimization framework.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: contextual
      justification: The study touches on identifying misalignments and planning for reallocations, but does not detail infeasibility handling.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: The system has a feature for detecting misalignment between planned and predicted spending, which is a form of anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: The detection method is not based on a specialized anomaly detection algorithm but rather a comparison of planned vs. actual values.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: The system is designed for desktop use but includes UI considerations for usability, which is tangentially related to mobile-first design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: The system incorporates role-based access control and is evaluated against ISO 27001 standards for information security.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: High user acceptance and satisfaction ratings, as measured by TAM, indicate a positive perception of trustworthiness and reliability.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: The system includes features like real-time dashboards that can support user engagement, but this is not a primary focus of the study.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: The linear regression model's performance is rigorously evaluated using MAE, RMSE, and R² metrics.
  contribution: For Odin's spending forecasting module (6.A/6.B), the paper provides a validated linear regression approach for forecasting sequential spending data, with clear metrics (MAE, RMSE, R²). For the expense categorization module (3.A/3.B), it demonstrates a functional categorization framework for school expenses, including real-time tracking and reporting. The study also offers insights for Odin's budget recommendation module (7.B) by showing how predictive insights can inform data-driven budget planning. The evaluation against ISO standards (10.A/10.B) and use of TAM (11.A) provide a methodological framework for validating Odin's system quality and user acceptance. The paper's development process highlights the importance of user-centered design and stakeholder feedback for system adoption (11.B).
  directly_justifies:
    - "Linear regression can effectively forecast budget allocations with high accuracy (R² = 0.9281) for public schools."
    - "System-generated predictive insights support proactive financial decision-making and strategic planning."
    - "Automated, DepEd-compliant reporting reduces manual errors and enhances transparency in financial operations."
    - "User acceptance is positively influenced by perceived usefulness and ease of use in school financial systems."
  limits:
    - "The system's functionality is limited to desktop use and does not include a mobile-first design."
    - "The model's accuracy depends on the quality and completeness of historical data input."
    - "The study's focus is on public elementary schools in one Philippine province, limiting generalizability to other contexts."
    - "Basic security features and manual updates for policy changes are noted as limitations."
    - "The study does not include a formal comparison with other forecasting algorithms to justify the choice of linear regression."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The domains flagged as relevant are: Existing Systems & Gaps (high relevance to 4.A, 4.B), Spending Forecasting (high relevance to 6.A, 6.B), Expense Categorization (medium relevance to 3.A, 3.B), Budget Recommendation (medium relevance to 7.B), Data Privacy & User Trust (medium relevance to 10.A, 10.B), and System Evaluation (high relevance to 12.B). Borderline cases included: seasonal spending (2.D) which was assigned low relevance as it is not a primary focus; user constraints (3.C) and optimization approaches (7.C, 7.D) which were considered but not selected due to the paper's focus on predictive forecasting rather than constraint-based optimization. Domains like Mobile-First Design and Behavioral Profiling were rejected due to a lack of relevant content. The overall relevance of the paper to Odin is high, as it provides a concrete example of a linear regression-based predictive system for financial allocation, supported by rigorous evaluation and a user-centered development methodology.
limitations:
  - "The scope is limited to public elementary schools in one Philippine province, potentially limiting generalizability."
  - "The system's reliance on accurate historical data is a key limitation for the predictive model's performance."
  - "The system lacks a mobile-first design, which is a significant limitation for accessibility in a modern context. [unacknowledged]"
  - "The study did not compare the linear regression model with other machine learning techniques to justify its selection. [unacknowledged]"
  - "The evaluation of security was based on standards review rather than a formal security audit."
remember_this:
  - Linear regression achieved a 92.81% R² score for forecasting school budgets.
  - The BFMIS system automates budget allocation and expenditure tracking.
  - Users strongly agreed on the system's high usability and security features.
  - The system generates DepEd-compliant reports, automating financial submissions.
  - A phased implementation plan with risk mitigation ensures sustainable adoption.
```