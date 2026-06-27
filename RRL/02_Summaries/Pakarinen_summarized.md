```yaml
paper_id: 1b3c4a5d-6e7f-8a9b-0c1d-2e3f4a5b6c7d
designation: international-algorithm-specific
title: Optimizing Banking Application Interfaces: A User-Centric Perspective on Consent Management in Digital Banking Environments
authors: Pakarinen, O.
year: 2025
venue: JAMK Master's Thesis
odin_topics:
  - 10.A
  - 10.B
  - 9.A
  - 9.B
  - 11.A
  - 11.B
  - 12.A
  - 3.A
tldr: Consent interfaces designed with category overviews and detailed controls improved user understanding, control perception, and decision confidence compared to traditional dense legal text approaches.
problem_and_motivation: Consent management in digital banking is often implemented with complex legal language and confusing formats, which undermines user understanding and informed decision-making. This gap between regulatory requirements and practical user comprehension poses risks to trust and autonomy. There is a need for consent interfaces that are transparent, accessible, and supportive of user control.
approach:
  - The study employed a mixed-methods approach, including a preliminary exploratory survey (n=6) to guide design.
  - A consent management prototype with a two-level structure (category-based overview and detailed consent view) was designed using Figma and the MEAN stack.
  - Two rounds of usability testing were conducted with participants interacting with the prototype, followed by semi-structured interviews.
  - Usability testing measured task completion time, error rate, user hesitations, and confidence levels.
  - Feedback from the first round informed iterative design improvements, such as breaking text into smaller segments and adding visual cues.
findings:
  - Participants interacting with the new consent flow showed increased confidence in their consent decisions.
  - Category-based overviews and explicit labels significantly improved users' ability to understand the consent structure.
  - Traditional consent screens with lengthy legal text were often ignored or skimmed, leading to user uncertainty.
  - Providing immediate feedback after a consent setting change reinforces user understanding and control.
  - Progressive disclosure of information (from category overview to detailed view) reduced cognitive load and improved comprehension.
  - The AI-powered "Smart Summary" feature was found helpful by participants for confirming their decisions.
key_figures_tables:
  - Figure 6.1: Revolut's category-based privacy settings → Illustrates a user-centric, mobile-first approach to consent.
  - Figure 6.2: ING Spain's Didomi consent interface → Shows standardized consent presentation across channels.
  - Figure 6.3: Nordea's open banking authorization flow → Demonstrates secure, in-app consent for third-party data access.
  - Figure 7.1: Consent management flow diagram → Visualizes the step-by-step user journey in the prototype.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: GDPR
    definition: General Data Protection Regulation, a legal framework that sets guidelines for the collection and processing of personal information.
  - term: CCPA
    definition: California Consumer Privacy Act, a state statute intended to enhance privacy rights and consumer protection.
  - term: Consent Management
    definition: The process of how users accept or decline the processing of personal information and how that consent is managed.
critical_citations:
  - "[Nouwens et al., 2020] — Demonstrated how consent pop-ups can influence user decisions."
  - "[EDPB, 2022] — Provided guidelines on dark patterns and consent clarity."
relevance:
  topics:
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: The study directly addresses the design of consent interfaces for managing personal data privacy.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Findings show that clear consent interfaces improve user confidence and trust.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: The prototype and case studies (e.g., Revolut) emphasize mobile-first design for consent.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: The usability testing focuses on user experience and interaction design for consent management.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: The research explores how consent design affects user engagement and decision-making.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: low
      justification: While not a primary focus, improved consent management is framed as supporting long-term customer loyalty.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: The study uses usability testing and interviews, aligning with system evaluation methodologies.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: The paper references consent categories for data usage, not for expense categorization.
  contribution: The research demonstrates that applying user-centered design principles—such as empathy, accessibility, and flexibility—can transform consent management from a formal regulatory requirement into a clearer and more approachable user experience. The proposed two-layer consent interface and evaluation results provide actionable evidence for improving user understanding and control in PFMS. The findings directly inform the design of Odin's consent and privacy-related modules, particularly in enhancing user trust.
  directly_justifies:
    - "Category-based consent overviews improve user orientation and understanding."
    - "Concise language and explicit labels increase user confidence in consent decisions."
    - "Providing a clear consent state (active/inactive/partial) reduces user uncertainty."
    - "Gradual disclosure of consent information lowers cognitive load."
    - "An AI-powered summary can effectively support users in confirming their choices."
  limits:
    - "Small sample size limits the generalizability of the usability findings."
    - "The study was conducted in a controlled environment, not a real banking system."
    - "The prototype simplified certain backend functions, which might influence user perceptions."
    - "Findings are primarily derived from a Finnish/European context and may not fully represent Filipino user behavior." [unacknowledged]
  mapping_rationale: A systematic scan of all 12 functional domains and their associated canonical topic codes was performed. The domains of "Data Privacy & User Trust" (topics 10.A, 10.B), "Mobile-First Design" (9.A, 9.B), and "User Retention & Engagement" (11.A, 11.B) were flagged as highly or moderately relevant, as the paper directly addresses consent interface design and its impact on user control, trust, and interaction. The "System Evaluation" domain (12.A) received medium relevance due to the study's methodology. The "Expense Categorization" domain (3.A) was considered contextual as the paper discusses consent categories but not for expenses. Domains like "Spending Forecasting" and "Budget Recommendation" were considered and rejected as the paper does not address predictive algorithms or allocation constraints. Borderline cases, such as the paper's discussion of user engagement touching both 11.A and 11.B, were resolved by identifying 11.A (engagement dynamics) as more directly applicable. Overall, the paper provides strong evidence for the design of consent and privacy modules, which are foundational to building user trust in Odin.
limitations:
  - "Small sample size for the survey and usability tests."
  - "Controlled testing environment may not reflect real-world banking interactions."
  - "The prototype was simplified and not integrated with a live banking system."
  - "Limited exploration of long-term user engagement with the consent model."
  - "Potential cultural bias as the study was conducted in a European context, which may not apply to Filipino users." [unacknowledged]
remember_this:
  - "Usability testing showed increased user confidence with the improved consent interface."
  - "Category-based overviews are more effective than long legal text for consent comprehension."
  - "Iterative design based on user feedback significantly reduced task completion time."
  - "Clear consent status visibility reduces user uncertainty and hesitation."
```