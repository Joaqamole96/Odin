```yaml
paper_id: 10.59431/jda.v4i1.660
designation: local
title: Development of Budget Management System Using Visual Basic .NET and MySQL Database: A Desktop Application for Personal Financial Tracking
authors: Janobe, J.
year: 2025
venue: Journal Dekstop Application
odin_topics:
  - 3.A
  - 4.A
  - 4.B
  - 9.A
  - 10.A
  - 12.A
  - 13.A
  - 13.B
tldr: A desktop budget system using Visual Basic .NET and MySQL enables offline income and expense tracking with automatic balance summaries and local data storage.
problem_and_motivation: Many individuals lack accessible, reliable tools for consistent financial record-keeping and analysis. Manual methods and spreadsheets are error-prone and time-consuming, while cloud-based solutions raise privacy and connectivity concerns.
approach:
  - The system was developed using Visual Basic .NET 2015 with a MySQL database, following the Software Development Life Cycle (SDLC) framework.
  - It uses a two-tier client-server architecture with ADO.NET and MySQL Connector/NET for secure data communication.
  - The interface includes input forms, action buttons for CRUD operations, a DataGridView for transaction display, and a summary panel.
  - SQL aggregate functions calculate total income, total expenses, and balance, with color-coded indicators for surplus or deficit.
  - Testing included unit, integration, functional, usability, and performance evaluations with datasets up to 5,000 records.
findings:
  - The system provides an intuitive, visually organized dashboard for efficient data entry, modification, and analysis.
  - Transaction insertion, modification, and deletion completed in under half a second during performance testing.
  - Data retrieval and aggregation queries remained responsive at under one second for databases containing up to 5,000 entries.
  - Users completed all tasks successfully with minimal guidance, indicating high usability across diverse technical backgrounds.
  - The offline capability and local data storage ensure user privacy and eliminate dependency on internet connectivity.
key_figures_tables:
  - "Figure 1: Budget Management System Interface in Visual Basic .NET → Shows the main dashboard with input fields, action buttons, data table, and summary panel."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: ADO.NET
    definition: A data access technology from Microsoft .NET framework for connecting applications to databases.
  - term: CRUD
    definition: An acronym for Create, Read, Update, and Delete, representing the four basic database operations.
  - term: DataGridView
    definition: A Windows Forms control used for displaying and editing tabular data in a .NET application.
  - term: MySQL Connector/NET
    definition: A driver that enables connectivity between .NET applications and MySQL databases.
  - term: SDLC
    definition: Software Development Life Cycle, a structured process for planning, creating, testing, and deploying software.
critical_citations:
  - "[Lusardi & Mitchell, 2014] — Establishes link between active financial management and stability."
  - "[Patel & Patel, 2016] — Demonstrates integration of .NET and databases for personal finance."
  - "[Thaler & Sunstein, 2008] — Highlights accessible tools encourage deliberate spending behavior."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: low
      justification: The system uses a basic transaction type classification (Received/Expense).
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Reviews commercial and open-source financial management applications.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: contextual
      justification: Identifies gaps in offline, privacy-focused, and low-cost personal finance tools.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: Mentions mobile development as a future direction, not a current feature.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: The system's local data storage model directly addresses user privacy concerns.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Describes a testing methodology including performance and usability testing.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: The system calculates balance but lacks explicit goal-setting features.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: low
      justification: Tracks expenses and balance, but does not specifically manage debt.
  contribution: "This paper provides a concrete example of a functional, offline personal finance system that prioritizes user privacy and simplicity. Its design and evaluation methodology can inform the development of Odin's core transaction management and local data storage modules. The system's focus on usability and accessibility aligns with Odin's goal for a mobile-first application. The identified limitations and future directions, such as cross-platform compatibility and advanced visualization, offer valuable insights for Odin's roadmap."
  directly_justifies:
    - "Storing financial data locally addresses user privacy and security concerns prevalent in cloud-based applications."
    - "A desktop-based system eliminates recurring subscription costs and dependence on internet connectivity."
    - "Intuitive interfaces and real-time feedback are crucial for encouraging consistent financial tracking behavior."
  limits:
    - "The system does not incorporate any predictive modeling or forecasting algorithms."
    - "User-defined allocation constraints or budgeting strategies are not implemented. [unacknowledged]"
    - "The single-user design restricts collaborative or household budgeting scenarios."
    - "The manual installation process for the database may be challenging for non-technical users."
    - "The application lacks advanced visual analytics such as charts or trend graphs."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as most relevant to 'Data Privacy & User Trust' (10.A) with medium relevance, as its offline, local storage model directly addresses privacy. It was also considered of medium relevance for 'System Evaluation' (12.A) due to its detailed testing methodology. Low relevance was assigned to 'Expense Categorization' (3.A) due to its basic income/expense classification, 'Savings & Debt Management' (13.A, 13.B) for tracking only balance without goals, and 'Mobile-First Design' (9.A) as mobile development is only mentioned as future work. Contextual relevance was assigned to 'Existing Systems & Gaps' (4.A, 4.B) because the paper reviews existing systems but does not focus on Odin's specific context. Domains like Behavioral Profiling, Forecasting, and Anomaly Detection were rejected as the paper does not address these algorithmic components. Overall, the paper offers a foundational example of a functional offline PFMS, with limited direct insight into Odin's more advanced modules."
limitations:
  - "Manual database installation may be complex for non-technical users."
  - "System is limited to single-user operation, restricting household or group use."
  - "Data backup must be performed manually, creating potential data loss risks."
  - "No expense categorization beyond basic income/expense types is provided. [unacknowledged]"
  - "No predictive or analytical features, such as forecasting or anomaly detection, are included. [unacknowledged]"
remember_this:
  - "The system performs transaction operations in under half a second."
  - "Offline capability and local storage are key differentiators from cloud-based apps."
  - "User testing confirmed high usability across diverse technical backgrounds."
  - "Data retrieval remains responsive under one second for up to 5,000 records."
  - "The application prioritizes privacy and user control over feature abundance."
```