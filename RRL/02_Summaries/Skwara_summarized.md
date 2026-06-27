```yaml
paper_id: 10.1002/cb.2193
designation: international
title: Effects of mental accounting on purchase decision processes: A systematic review and research agenda
authors: Skwara, F.
year: 2023
venue: Journal of Consumer Behaviour
odin_topics:
  - 3.A
  - 3.B
  - 7.A
  - 7.B
  - 5.A
  - 5.B
  - 9.B
tldr: Mental accounting influences purchase decisions through four themes: source of funds, intended use, pricing, and payment methods, affecting willingness to pay and the pain of paying.
problem_and_motivation: Consumers often deviate from rational economic behavior in spending decisions, violating the principle of money's fungibility. A systematic overview conceptualizing the diverse research outcomes on mental accounting's effects on purchase decisions was lacking.
approach:
  - A systematic literature review was conducted following the three-stage approach by Tranfield et al.
  - The review extracted 786 publications from EBSCO host, ResearchGate, and ScienceDirect using keywords like mental accounting and mental budgeting.
  - After screening titles, abstracts, and full texts, 110 papers were selected for the final sample.
  - A coding sheet was used for data extraction, and a narrative synthesis approach grouped findings into themes.
  - The analysis structured the literature into four main theoretical themes: source of funds, intended use of funds, pricing, and payments.
findings:
  - Consumers categorize income into mental accounts (current income, assets, future income) and spend differently from each.
  - Windfall gains are spent more readily and on luxury goods compared to regular income.
  - Mental budgeting involves grouping expenses into categories with caps, but can also lead to under- or over-consumption.
  - num: 72.73% of the reviewed papers applied a quantitative research type, with experiments being the predominant method (60.91%).
  - The framing of promotions and price points significantly alters consumer perception and willingness to pay.
  - Payment methods with higher transparency, like cash, induce a greater pain of paying compared to credit cards.
  - Consumers often prefer flat-rate pricing despite pay-per-use being cheaper for their usage, to avoid budgeting disruption.
  - The "silver-lining effect" shows consumers prefer a small gain isolated from a larger loss over a larger overall discount.
  - Advance payment systems that result in refunds can reduce price awareness and churn.
  - Research gaps exist on long-term effects of mental budgeting on wealth and the impact of new financial technologies.
key_figures_tables:
  - Table 1: Number of publications per journal between 1970 and 2022 → Journal of Consumer Research has the most publications (16.36%).
  - Figure 2: Structure of the findings with its four main themes → The four themes follow a chronological sequence in decision processes.
  - Table 7: Directions for future research and their potential themes → Future research should examine product categories, budgeting flexibility, and technology's impact.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Mental Accounting
    definition: The set of cognitive operations used by individuals to organize, evaluate, and keep track of financial activities.
  - term: Pain of Paying
    definition: The feeling similar to pain that a consumer experiences when paying for a product or service.
  - term: Mental Budgeting
    definition: The grouping of expenses into categories and constraining each budget with an implicit or explicit cap.
  - term: In-store Slack
    definition: Funds in a shopper's total budget not earmarked for specific items but available for in-store purchase decisions.
critical_citations:
  - "[Thaler, 1999] — Foundational paper defining mental accounting."
  - "[Shefrin & Thaler, 1988] — Introduced the behavioral life-cycle model."
  - "[Prelec & Loewenstein, 1998] — Explained the pain of paying and decoupling."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: The entire review structures how consumers categorize income and expenses into mental accounts, directly informing categorization frameworks.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: high
      justification: The findings on mental budgeting and how consumers assign expenses (e.g., broad vs. narrow) are core design considerations for expense categories.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: The paper provides extensive evidence on mental budgeting behaviors, including goal setting, temporal frames, and its role in financial discipline.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: The review's insights into how consumers set and track budgets are directly applicable to designing effective budget recommendation engines.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: The paper notes that consumer characteristics like education, income, and self-control affect mental accounting, supporting the need for behavioral profiling.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: medium
      justification: The discussion on different responses to budgets and promotions based on consumer traits is relevant for handling cold-start profiling.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: The paper identifies the impact of increased financial transparency through technology as a research gap, which is relevant for mobile UX design.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: The paper discusses exceptional expenses (e.g., birthdays) and seasonal patterns, which are relevant to the concept of "occasions" in a Filipino context.
  contribution: "The paper's systematic review of mental accounting effects directly justifies Odin's need for sophisticated expense categorization (3.A) and budget setting (7.A) modules. The findings on how consumers track spending and the pain of paying (Payments) inform the design of Odin's user experience for expense entry and budget monitoring (9.B). The identification of consumer characteristics influencing mental accounting behavior supports the development of behavioral profiles (5.A) within Odin to personalize recommendations. The discussion on integration-segregation in pricing provides foundational knowledge for how users might perceive budget allocations and recommendations."
  directly_justifies:
    - "Mental accounting explains why users may treat money from different sources differently, affecting budget allocation."
    - "The pain of paying varies by payment method and transparency, influencing user engagement with expense tracking."
    - "Consumers use mental budgets to exercise self-control, but budget rigidity can lead to overconsumption."
    - "Temporal framing affects spending, suggesting that budget periods must be flexible and user-defined."
    - "The impact of technology on mental accounting is a key area for future research relevant to Odin's design."
  limits:
    - "The review is limited to the effects on purchase decision processes and does not cover other financial behaviors like investing."
    - "Most reviewed studies used short-term experiments, limiting insights on long-term effects of mental accounting."
    - "The influence of new technologies like budgeting apps on mental accounting is identified as a research gap."
  mapping_rationale: "A systematic scan of all 12 functional domains was conducted. The domain of Expense Categorization (3.A, 3.B) was flagged as highly relevant because the paper's core finding is how consumers categorize and assign funds to mental accounts. The domain of Budget Recommendation (7.A, 7.B) was also highly relevant, given the extensive evidence on mental budgeting strategies and goal setting. Behavioral Profiling (5.A, 5.B) was assessed as medium relevance because the paper notes that individual characteristics (e.g., self-control) influence mental accounting, supporting the need for personalized profiles. Mobile-First Design (9.B) was deemed medium relevance because the paper identifies the impact of financial technology (e.g., apps, notifications) on consumer behavior, directly informing UX design. Filipino Cultural Context domains (2.A, 2.B, 2.C, 2.D) were considered and rejected as the paper does not examine cultural or seasonal spending patterns specifically. Existing Systems (4.A, 4.B) was rejected as the paper does not analyze other PFMS. Anomaly Detection (8.A-C) and Savings & Debt Management (13.A-C) were rejected due to lack of direct mention. The paper's overall relevance to Odin is high, as it provides a comprehensive theoretical foundation for understanding user spending behavior, which is central to Odin's personal finance management functions."
limitations:
  - "The sample may have omitted some relevant papers despite a broad database search."
  - "The review focuses only on mental accounting's impact on purchase decisions, excluding other financial areas. [unacknowledged]"
  - "The findings are largely based on experimental studies, which may not fully reflect real-world behavior."
remember_this:
  - "Mental accounting theory explains how consumers categorize income and expenses."
  - "Windfall gains are spent more readily than regular income on luxury goods."
  - "Payment method transparency affects the pain of paying and spending behavior."
  - "Consumer characteristics like self-control influence mental budgeting success."
  - "Mental budgeting can both enforce financial discipline and lead to overconsumption."
```