# Compiled Research Summaries

## Filters Applied

- Designation: `international`

**Total Papers:** 25

**Note:** Included papers positions 51 to 75, Sorted by year.

---

## Paper 1: Saghafi et al_summarized.md

**Source File:** `Saghafi et al_summarized.md`

```yaml
paper_id: 10.1016/j.dss.2025.114499
designation: international
title: Impact of categorization autonomy on effective use and adoption intentions
authors: Saghafi, A.; Medappa, P.; Debrliev, A.
year: 2025
venue: Decision Support Systems
odin_topics:
  - 3.A
  - 5.A
  - 5.C
  - 9.B
  - 10.B
  - 11.A
tldr: User-defined categorization schemes improve search precision and usage intentions compared to fixed hierarchies, particularly for exploratory tasks.
problem_and_motivation: Predefined categorization trees may not align with individual users' cognitive schemas, potentially hindering effective information assimilation and decision-making. The impact of allowing users to create their own categorization hierarchies from base object types remains unexplored. This gap limits the potential for designing decision support systems that better fit users' mental models and task demands.
approach:
  - Conducted an online laboratory experiment with 201 Amazon Mechanical Turk workers as surrogates for e-commerce users.
  - Developed a functional experimental website with over 10,000 products scraped from a major North American e-retailer.
  - Manipulated categorization autonomy at three levels: fixed (control), partial autonomy (fixed top two levels), and full autonomy (user-defined hierarchy).
  - Task flexibility was manipulated as a moderator via closed-ended (exploitive) and open-ended (exploratory) search scenarios.
  - Search precision was measured as the ratio of correctly identified items to the total required items, while usage intentions were measured via survey scales.
findings:
  - num: Categorization autonomy led to significantly higher search precision (full autonomy outperformed fixed categorization by 0.155, p < 0.01).
  - num: Task flexibility significantly moderated the effect, with categorization autonomy being more beneficial for high-flexibility tasks (interaction effect 0.179, p < 0.01).
  - num: Full categorization autonomy increased usage intentions compared to fixed categorization (0.359, p < 0.01).
  - Perceived restrictiveness mediated the relationship between categorization autonomy and usage intentions for fixed vs. full autonomy comparisons.
  - num: Users' self-defined category trees were highly diverse, with a maximum cosine similarity of 0.58 between participants, and a mean similarity of 0.36 to the baseline retailer's scheme.
  - The openness personality trait was a significant predictor of greater dissimilarity from the baseline category scheme.
key_figures_tables:
  - Figure 1: Nomological research model → Shows hypothesized relationships among categorization autonomy, task flexibility, restrictiveness, and outcomes.
  - Table 2: Regression analysis for impact of categorization autonomy on search precision → Confirms main effect of autonomy on precision.
  - Table 3: Regression analysis for moderation effect of task flexibility → Shows autonomy's effect is stronger for flexible tasks.
  - Table 4: Regression analysis for effect on usage intentions → Confirms autonomy increases usage intentions.
  - Table 5: Analysis on mediation effect of restrictiveness → Shows restrictiveness mediates autonomy's effect on usage intentions.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Categorization autonomy
    definition: The extent to which users have the ability to define their own categorization schemes from a base level of object types.
  - term: Task flexibility
    definition: The extent to which a task allows for multiple ways of achieving the desired outcome.
  - term: Effective use
    definition: Using a system in a way that helps attain the goals for using the system, operationally assessed by performance.
  - term: Perceived restrictiveness
    definition: The extent to which a system constrains the user's decision-making processes to a particular subset of all possible processes.
critical_citations:
  - "[Burton-Jones & Grange, 2013] — Defines effective use as goal-attainment performance."
  - "[Vessey, 1991] — Establishes Cognitive Fit Theory linking representation to task performance."
  - "[Goodhue & Thompson, 1995] — Task-Technology Fit theory explaining system performance."
  - "[Wang & Benbasat, 2009] — Links perceived restrictiveness to usage intentions."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Directly investigates how user-defined categorization schemes improve performance and perceptions.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Provides evidence that individual cognitive schemas (profiles) lead to divergent category structures.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Demonstrates that allowing user-driven classification improves outcomes compared to fixed, one-size-fits-all approaches.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Categorization autonomy is a UX design principle directly applicable to PFMS interface design.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Shows autonomy increases trust, which mediates satisfaction and usage intentions (Appendix D).
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Autonomy increases usage intentions and satisfaction, key drivers of engagement.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: While not directly about Filipino spending, the concept of user-defined categories could support tracking cyclical or occasion-based spending.
    - code: 3.C
      name: User-Defined Allocation Constraints
      relevance: low
      justification: Autonomy in categorization is a prerequisite for user-defined allocation but not directly studied.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: contextual
      justification: Categorization autonomy is foundational for personalized recommendations but not the focus.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Mentions YNAB as an example but does not systematically review PFMS landscape.
  contribution: "This paper provides strong empirical justification for designing Odin with user-defined expense categories (3.A, 5.A). It validates that allowing users to structure their own financial data aligns with their cognitive schemas, improving both objective task performance (search precision) and subjective perceptions like trust and satisfaction, which are critical for Odin's adoption. The findings directly support Odin's mobile-first design (9.B) by demonstrating that personalized information structures enhance user experience. Furthermore, the mediating role of trust (10.B) and the impact on usage intentions (11.A) are foundational for Odin's retention and engagement strategies. The results also inform Odin's approach to behavioral profiling (5.C) by showing that profiles should be inferred from user-defined structures rather than imposed from the system."
  directly_justifies:
    - "User-defined categorization improves search precision compared to fixed taxonomies (Saghafi et al., 2025)."
    - "Categorization autonomy leads to higher usage intentions (Saghafi et al., 2025)."
    - "The benefits of categorization autonomy are stronger for exploratory, high-flexibility tasks (Saghafi et al., 2025)."
    - "Perceived restrictiveness mediates the effect of autonomy on usage intentions (Saghafi et al., 2025)."
    - "Users with higher openness create categorization trees more dissimilar to baseline schemes (Saghafi et al., 2025)."
  limits:
    - "Study was conducted in an e-commerce context, not a personal finance management system."
    - "Participants were US/Canadian AMT workers, not specifically Filipino young professionals."
    - "The experimental setting involved a one-time task, not longitudinal use which may affect cognitive fit."
    - "Search function was disabled to isolate the effect of categorization, limiting generalizability to real-world systems where both search and browse are available."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to Expense Categorization Frameworks (3.A), Financial Behavioral Profiles (5.A), and Classification Approaches (5.C), as its core contribution directly addresses how user-defined categorization improves performance and aligns with individual cognitive schemas. Medium relevance was assigned to Mobile UX Design (9.B), User Trust (10.B), and Engagement Dynamics (11.A), as the findings on autonomy, trust, satisfaction, and usage intentions have clear implications for these areas. Low relevance was noted for Filipino Spending Cycles (2.D) and User-Defined Allocation Constraints (3.C), as the paper does not directly address these but provides conceptual groundwork. Domains such as Forecasting (6), Budget Recommendation (7), Anomaly Detection (8), and System Evaluation (12) were considered and rejected, as the paper does not address these algorithmic functions. The paper's overall relevance to Odin is high, providing foundational evidence for user-controlled categorization, which is central to Odin's behavioral profiling and user experience design."
limitations:
  - "The study was conducted in an e-commerce context, limiting direct generalizability to PFMS. [unacknowledged]"
  - "Participants were not Filipino young professionals, reducing cultural relevance. [unacknowledged]"
  - "The experimental task was a one-time interaction, not capturing longitudinal effects of categorization autonomy. [unacknowledged]"
  - "Search functionality was removed, which may not reflect real-world mixed-use systems. [unacknowledged]"
  - "The simplification of tasks may not capture the full spectrum of information requirements for financial management."
remember_this:
  - "User-defined categories improve search precision by 0.155 over fixed hierarchies."
  - "Autonomy is more effective for flexible, exploratory tasks than rigid ones."
  - "Categorization autonomy increases usage intentions and trust in the system."
  - "Individuals create unique category trees that differ from vendor baselines."
  - "Openness personality trait predicts greater divergence from predefined schemes."
```
---

## Paper 2: Guo_summarized.md

**Source File:** `Guo_summarized.md`

```yaml
paper_id: d444c8a2-9d6b-5be2-8c4c-4a2d8f7b1e3f
designation: international
title: Machine Learning Methods in Customer Segmentation and Recommendation Systems
authors: Guo, Y.
year: 2025
venue: SHS Web of Conferences
odin_topics:
  - 5.B
  - 6.A
  - 7.B
  - 8.A
  - 8.B
  - 10.A
tldr: A survey of machine learning segmentation and recommendation methods, comparing collaborative filtering, content-based filtering, and hybrid models across e-commerce, banking, and healthcare applications.
problem_and_motivation: Traditional customer segmentation methods fail to handle modern data complexity and scale, missing business opportunities. Machine learning offers scalable, automated solutions but faces challenges in data quality, privacy, and bias that limit real-world effectiveness.
approach:
  - "Reviews collaborative filtering, content-based filtering, and hybrid recommendation models."
  - "Examines K-means, DBSCAN, and PCA for segmentation with applications in e-commerce, banking, and healthcare."
  - "Presents case studies: Amazon uses collaborative filtering and DBSCAN for fraud detection."
  - "Presents case studies: Banks use machine learning segmentation with PCA improving anomaly detection."
  - "Discusses challenges including cold-start, data quality, privacy risks, and algorithmic bias."
findings:
  - "num: DBSCAN improves Amazon's recommendation accuracy by 12% compared to K-Means on noisy data."
  - "num: PCA improves banking fraud detection accuracy by 15% through dimensionality reduction."
  - "num: K-Means improves healthcare patient classification accuracy by 18% for personalized treatment."
  - "Collaborative filtering suffers from cold-start and scalability limitations."
  - "Content-based filtering performance depends heavily on metadata quality."
  - "Hybrid models combining collaborative and content-based filtering offer more robust recommendations."
key_figures_tables:
  - "None."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "DBSCAN"
    definition: "Density-Based Spatial Clustering of Applications with Noise; groups points based on density and identifies outliers."
  - term: "PCA"
    definition: "Principal Component Analysis; reduces dimensionality while preserving variance."
  - term: "Collaborative Filtering"
    definition: "Recommends items based on user-item interaction patterns and similar user behaviors."
critical_citations:
  - "[Owolabi et al., 2024] — Foundational review of ML models in banking segmentation."
  - "[Johnson et al., 2021] — Customer segmentation in digital banking using ML."
  - "[Chen et al., 2022] — Comprehensive review of ML for fraud detection."
  - "[Lee et al., 2021] — Clustering for diabetes patient risk profiling and treatment."
relevance:
  topics:
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "high"
      justification: "Directly discusses cold-start limitations of collaborative filtering for new users."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews predictive recommendation models transferable to spending forecasting."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Recommendation system techniques (collaborative, content, hybrid) are analogous to budget recommendation methods."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses DBSCAN and PCA for anomaly detection in transactional data."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "medium"
      justification: "Reviews DBSCAN and PCA as anomaly detection techniques in banking fraud contexts."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "medium"
      justification: "Explicitly addresses privacy risks and encryption needs, citing the Equifax breach."
  contribution: "This paper provides a broad survey of ML segmentation and recommendation techniques that can inform Odin's user profiling and spending categorization modules. Its review of collaborative filtering and cold-start challenges directly supports the behavioral profiling module's need for cold-start strategies. The discussion of DBSCAN and PCA for anomaly detection informs the design of Odin's spending anomaly detection module. The paper's emphasis on data privacy and bias highlights considerations for Odin's data handling and user trust components. Overall, it offers a foundational overview of ML methods applicable across multiple Odin functional areas."
  directly_justifies:
    - "Cold-start problem in collaborative filtering limits recommendations for new users."
    - "DBSCAN improves anomaly detection accuracy by 12% in noisy e-commerce data."
    - "PCA enhances anomaly detection by 15% in banking transaction data."
    - "Data quality issues lead to inaccurate segmentation and recommendation outcomes."
  limits:
    - "Survey paper; does not provide novel algorithmic contributions for Odin to directly adopt."
    - "Performance metrics (12%, 15%, 18%) are reported from case studies, not the paper's own experiments."
    - "Findings are aggregated from diverse domains (e-commerce, banking, healthcare) and may not generalize directly to personal finance management."
  mapping_rationale: "A systematic scan across all 12 functional domains identified relevance primarily in Behavioral Profiling (5.B), Forecasting (6.A), Budget Recommendation (7.B), Anomaly Detection (8.A, 8.B), and Data Privacy (10.A). Topic 5.B was rated high due to explicit discussion of the cold-start problem in collaborative filtering. Topics 6.A, 7.B, 8.A, and 8.B were rated medium because the paper reviews algorithmic techniques (collaborative filtering, DBSCAN, PCA) that are transferable to Odin's predictive, recommendation, and anomaly detection modules but does not apply them to personal finance data. Topic 10.A was rated medium due to explicit privacy considerations. Borderline cases: The paper's segmentation discussion touches on 5.A (Financial Behavioral Profiles) but was assigned to 5.B because cold-start is the more specific actionable insight. Domains rejected: Cultural Context (2.A-D) and Mobile-First Design (9.A-B) were not addressed. User Retention (11.A-B) and System Evaluation (12.A-C) were not addressed. Overall, the paper provides a broad but non-specific survey that offers contextual and methodological background for several Odin modules."
limitations:
  - "Paper is a survey, not an empirical study; lacks validation of claims specific to PFMS. [unacknowledged]"
  - "Does not address personal finance or budgeting contexts directly; generalizes from e-commerce, banking, and healthcare. [unacknowledged]"
  - "Performance improvements (12%, 15%, 18%) are cited from external studies, not independently verified. [unacknowledged]"
remember_this:
  - "Collaborative filtering faces cold-start problems for new users and items."
  - "DBSCAN handles noisy data and irregular clusters better than K-Means."
  - "PCA improves anomaly detection by 15% in high-dimensional transaction data."
  - "Data quality and privacy are critical challenges for ML-based segmentation systems."
  - "Hybrid recommendation models combine collaborative and content-based filtering."
```
---

## Paper 3: Yuttama_summarized.md

**Source File:** `Yuttama_summarized.md`

```yaml
paper_id: 10.34001/jmer.2025.12.06.4-80
designation: international
title: Behavioral Shifts in Digital Finance: How E-Payment Influences Consumer Spending and Financial Literacy
authors: Yuttama, F.
year: 2025
venue: Journal of Management and Entrepreneurship Research
odin_topics:
  - 1.C
  - 2.A
  - 2.B
  - 5.B
  - 5.C
  - 6.B
  - 7.A
  - 7.B
  - 10.B
  - 11.A
tldr: E-payment adoption in Indonesia exerts a dual effect on financial behavior, increasing spending propensity while enhancing cash management, with financial literacy moderating these effects.
problem_and_motivation: The influence of e-payment on consumer spending and financial discipline is inconclusive, with studies suggesting both impulsive spending and improved financial tracking. Existing research often treats e-payment as a direct driver without examining conditional factors like financial literacy. This gap is critical in emerging markets where digital payment adoption is rapidly transforming financial behavior.
approach:
  - A quantitative survey was administered to 400 active e-payment users in Central Java, Indonesia.
  - Constructs for e-payment usage, consumer behavior, cash management, and financial literacy were measured using validated Likert-scale items.
  - The hypothesized relationships were analyzed using Partial Least Squares Structural Equation Modeling (PLS-SEM) with SmartPLS 4.
  - Moderation analysis via PLS-SEM assessed the interactive effect of financial literacy on the relationships between e-payment usage and both consumer behavior and cash management.
  - Bootstrapping with 5,000 resamples was used to determine the statistical significance of path coefficients and moderation effects.
findings:
  - num: E-payment usage has a significant positive effect on consumer behavior (β = 0.731, p < 0.000).
  - num: E-payment usage has a significant positive effect on cash management (β = 0.493, p < 0.000).
  - num: Financial literacy significantly attenuates the positive relationship between e-payment and consumer behavior (β = -0.082, p < 0.000).
  - num: Financial literacy significantly strengthens the positive relationship between e-payment and cash management (β = -0.065, p = 0.005).
  - E-payment facilitates impulsive spending by lowering the psychological friction of payment.
  - Built-in transaction records and dashboards in e-payment systems improve expense tracking and budgeting.
  - The impact of e-payment is contingent on users' financial knowledge and self-regulation.
key_figures_tables:
  - Figure 1: E-payment transaction value growth in Central Java → shows rapid adoption of digital payments like QRIS and e-wallets.
  - Figure 2: PLS-SEM structural model results → illustrates significant paths and moderation effects of financial literacy.
  - Table 2: Demographic profile of respondents → shows majority are female, aged 25-34, with a bachelor's degree.
  - Table 4: Reliability and validity of measurement model → confirms all constructs meet thresholds for Cronbach's alpha and AVE.
  - Table 6: Structural model path coefficients → details the t-statistics and p-values for all hypothesized relationships.
key_equations:
  - equation: \eta = \frac{N}{1 + N e^2}
    explanation: Slovin's formula for determining sample size.
definitions:
  - term: PLS-SEM
    definition: Partial Least Squares Structural Equation Modeling, a variance-based method for analyzing complex cause-effect relationships.
  - term: AVE
    definition: Average Variance Extracted, a measure of convergent validity.
  - term: HTMT
    definition: Heterotrait-Monotrait ratio, a criterion for assessing discriminant validity.
critical_citations:
  - "[Hampson et al., 2021] — e-payment lowers psychological barriers, boosting impulse spending."
  - "[Liu & Zhang, 2021] — e-payment tools enhance financial tracking and management."
  - "[Lusardi & Mitchell, 2014] — financial literacy improves self-control and planning."
  - "[Thaler & Sunstein, 2008] — concept of 'pain of paying' in digital transactions."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Paper examines financial behavior in an emerging market context, providing comparative insights.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: low
      justification: Focuses on Indonesian context, offering limited but relevant cultural parallels for SE Asia.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: low
      justification: Touch on spending cycles but not a core focus of the study.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: Financial literacy is treated as a key moderating variable that differentiates user behavior.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Demonstrates how financial literacy can be used to classify and predict user responses to e-payment systems.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: Provides behavioral data (spending patterns) that could inform forecasting models, but no algorithms are proposed.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Paper directly investigates how e-payment tools and financial literacy facilitate budgeting and cash management.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: Findings directly support the need for in-app budgeting and monitoring features in PFMS like Odin.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Implications discuss building trust through features that promote financial discipline and user well-being.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Suggests features like spending alerts and goal tracking to maintain user engagement and financial discipline.
  contribution: This paper validates the dual nature of e-payment adoption, which Odin can leverage to design behavioral nudges and budgeting features. It emphasizes the crucial moderating role of financial literacy, informing Odin's user profiling and personalization engine. The study's empirical evidence from an emerging market supports Odin's mobile-first design for Filipino users, showing that app features can both encourage spending and aid cash management. The findings justify integrating financial literacy assessments to tailor budget recommendations and anomaly detection for users.
  directly_justifies:
    - "E-payment usage significantly increases consumer spending propensity."
    - "E-payment tools enhance users' ability to monitor and plan finances."
    - "Higher financial literacy attenuates the positive effect of e-payment on spending."
    - "Financially literate individuals use e-payment features more effectively for financial discipline."
  limits:
    - "Findings are based on a survey in Central Java, Indonesia, which may not be generalizable to other developing countries like the Philippines."
    - "Reliance on self-reported data may introduce social desirability bias."
    - "Study focuses on financial literacy as a moderator, excluding other contextual variables."
  mapping_rationale: A systematic scan across all 12 functional domains was performed for this paper. The domain of 'Budget Recommendation' (7) was flagged as high relevance because the paper directly examines how e-payment tools and financial literacy enable effective budgeting and cash management. 'Behavioral Profiling' (5) was assigned medium relevance, as financial literacy is shown to differentiate user behavior, which is crucial for the cold-start problem. 'Spending Forecasting' (6) and 'User Retention' (11) received low to medium relevance, as the behavioral patterns and feature suggestions (e.g., goal tracking, alerts) provide supporting evidence. Other domains like 'Expense Categorization' (3), 'Anomaly Detection' (8), and 'Data Privacy' (10) were considered but rejected as the paper does not directly address these technical aspects. The paper's overall relevance to Odin is moderate, providing valuable behavioral and cognitive evidence to inform budgeting, user profiling, and engagement strategies for the Filipino context.
limitations:
  - "Geographic focus on Central Java limits generalizability to the Philippines."
  - "Self-reported data may introduce social desirability bias."
  - "Excludes other behavioral and contextual variables like digital literacy or income."
  - "Cross-sectional design captures behavior at a single point in time. [unacknowledged]"
  - "Does not differentiate between types of e-payment (e.g., bank transfer vs. e-wallet) in the analysis. [unacknowledged]"
remember_this:
  - "E-payment adoption both increases spending and improves financial tracking."
  - "Financial literacy is a critical buffer against impulsive digital spending."
  - "Higher literacy strengthens the positive link between e-payment and cash management."
  - "In-app features like budgets and alerts can promote financial discipline."
  - "Moderation effect of literacy on spending is significant (β = -0.082, p < 0.000)."
```
---

## Paper 4: Yoganandham_summarized.md

**Source File:** `Yoganandham_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international
title: MASTERING ECONOMIC AND FINANCIAL SOURCES WITH REFERENCE TO BUDGETING, SAVINGS, EARLY INVESTING, DEBT MANAGEMENT AND THE POWER OF FINANCIAL PLANNING - A COMPREHENSIVE ANALYSIS
authors: Yoganandham, G.
year: 2025
venue: Degres Journal
odin_topics:
  - 3.A
  - 3.B
  - 13.A
  - 13.B
tldr: A comprehensive overview of foundational personal finance principles including budgeting, saving, early investing, debt management, and financial planning for achieving long-term stability and independence.
problem_and_motivation: Individuals and households often struggle with financial stability due to inadequate knowledge, financial illiteracy, and poor management practices in budgeting, saving, investing, and debt control. This gap underscores the need to explore strategies that promote economic literacy and empower individuals to take control of their financial futures.
approach:
  - This study employs a descriptive and diagnostic methodology, relying on secondary data and statistical tools.
  - It leverages established theoretical frameworks to examine key concepts within their contextual settings.
  - The research is grounded in credible secondary sources, including academic discussions, expert analyses, books, journals, and official records.
  - The data is systematically organized and presented to offer meaningful insights and actionable policy recommendations.
findings:
  - Prioritizing needs over wants is fundamental to wise spending, budgeting, and personal finance management.
  - Saving, maintaining emergency funds, and early investing are crucial for building financial resilience and harnessing compound growth.
  - Effective debt management strategies, such as consolidating high-interest debts and timely repayments, are critical for financial health.
  - Strategic investments and emergency savings create a balanced approach to financial security and independence.
  - Tax planning, credit score management, and emergency planning are foundational pillars of financial stability.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Debt Avalanche Method
    definition: A debt repayment strategy that prioritizes paying off high-interest debts first.
  - term: Debt Snowball Method
    definition: A debt repayment strategy that focuses on paying off smallest debts first to build momentum.
critical_citations:
  - "[Gibert et al., 2024] — culturally relevant financial literacy programs."
  - "[Jumady et al., 2024] — financial planning's effect on debt management."
  - "[Ramsey, 2020] — guide on money management and financial independence."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: low
      justification: Discusses budgeting and distinguishing needs vs. wants, a foundational concept for expense categorization.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: low
      justification: Mentions the 50/30/20 rule, which is a category design consideration.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: Extensively covers saving for goals like buying a home, education, and retirement.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: low
      justification: Provides detailed strategies for debt management, including methods and consolidation.
  contribution: This paper provides a general theoretical and educational foundation for personal finance principles. It offers a comprehensive overview of budgeting, saving, investing, and debt management, which can serve as high-level domain knowledge for Odin. The concepts of distinguishing needs from wants and the 50/30/20 rule can inform the design of expense categorization and budget recommendation features. The discussion on debt repayment strategies and the importance of emergency funds supports the development of savings and debt management modules.
  directly_justifies:
    - The 50/30/20 rule provides a simple heuristic for budget allocation.
    - Early investing leverages compounding for wealth creation.
    - An emergency fund covering 3-6 months of expenses is a key savings goal.
    - The Debt Snowball and Avalanche methods are structured debt repayment strategies.
  limits:
    - The paper is non-empirical and offers no quantitative data or algorithm-specific insights. [unacknowledged]
    - It does not consider the specific cultural or financial context of Filipino young professionals. [unacknowledged]
    - The approach is purely descriptive and provides no evaluation of the proposed strategies. [unacknowledged]
    - The paper lacks any focus on mobile-first design, data privacy, or system evaluation.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains of Expense Categorization, Savings & Debt Management were flagged as having low relevance due to the paper's general, conceptual coverage of budgeting and financial planning principles. Topics like 3.A and 3.B (Expense Categorization) and 13.A and 13.B (Savings & Debt Management) were selected because the paper directly discusses budgeting rules and debt strategies. Borderline cases, such as the paper's mention of financial discipline (potentially 1.A/1.C) and financial education (10.B), were considered but rejected as the discussion is too general and lacks actionable insights for Odin's specific design. All other domains, including Forecasting, Anomaly Detection, Mobile-First Design, and User Retention, were deemed irrelevant as the paper provides no technical or design-specific information for these areas. Overall, the paper's relevance to Odin is low, serving primarily as foundational, non-algorithmic background.
limitations:
  - The paper does not provide empirical evidence to support its claims. [unacknowledged]
  - It lacks an algorithmic or computational approach relevant to PFMS development. [unacknowledged]
  - The study does not address the specific needs of a Filipino demographic or PFMS users. [unacknowledged]
  - No evaluation of financial planning strategies is conducted.
remember_this:
  - Budgeting is the foundation of financial discipline and stability.
  - Early investing harnesses the power of compounding for wealth creation.
  - An emergency fund of 3 to 6 months of expenses is a key financial safety net.
  - Prioritizing needs over wants is a core principle of wise spending.
  - The 50/30/20 rule provides a simple structure for budget allocation.
```
---

## Paper 5: Oyeyemi et al_summarized.md

**Source File:** `Oyeyemi et al_summarized.md`

```yaml
paper_id: http://doi.org/10.37502/IJSMR.2025.81004
designation: international
title: From Borrowing to Building: A Systematic Literature Review of Data-Driven Strategies for Cultivating Better Money Habits through Consumer Credit
authors: Oyeyemi, D. O.; Moussa, A. H.; Abioye, V. O.
year: 2025
venue: International Journal of Scientific and Management Research
odin_topics:
  - 1.C
  - 2.B
  - 2.D
  - 4.A
  - 5.A
  - 5.B
  - 5.C
  - 6.B
  - 7.A
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 12.A
tldr: Data-driven credit strategies using alternative data and machine learning expand financial inclusion and enable personalized behavioral interventions, but raise privacy and bias concerns.
problem_and_motivation: Consumer credit systems have evolved into data-driven platforms that can influence financial behavior, yet a comprehensive synthesis of how these strategies cultivate better money habits is lacking. Understanding this integration is essential for designing systems that promote financial wellbeing while mitigating risks.
approach:
  - Systematic literature review following a predefined methodology with structured search and explicit inclusion criteria.
  - Searched Scopus, Web of Science, IEEE Xplore, and Google Scholar using keywords related to data-driven credit and financial habits.
  - Included peer-reviewed journal articles, conference papers, and book chapters in English that address data analytics or machine learning in consumer credit.
  - Extracted data using a standardized protocol, synthesizing findings thematically across recurring concepts.
  - Assessed quality of included studies for methodological rigor, bias, and generalizability.
  - Focused on alternative data, behavioral drivers, technological innovations, and information design as core domains.
findings:
  - Alternative data sources (social, behavioral, transactional) expand credit access for individuals lacking traditional credit histories.
  - Machine learning ensemble models like XGBoost outperform traditional logistic regression in credit risk prediction accuracy.
  - Personality traits such as conscientiousness and self-control are strong predictors of responsible credit management.
  - The "statement effect" shows that visibility and timing of financial information can temporarily alter spending patterns.
  - Behavioral nudges and personalized feedback loops show stronger short-term impacts on financial behavior than mandatory disclosures.
  - Financial incentives alone demonstrate limited long-term effectiveness for sustained habit formation.
  - Technological feedback mechanisms like credit score monitoring services can improve financial literacy and encourage positive adjustments.
  - Concerns about data privacy, algorithmic bias, and "off-label" use of credit scores are critical and require regulatory attention.
  - num: XGBoost consistently achieves superior accuracy, precision, recall, and AUC compared to logistic regression in credit classification tasks.
  - The interaction between personality, literacy, and intervention effectiveness requires further exploration across diverse contexts.
key_figures_tables:
  - Figure 1: Timeline of consumer credit evolution from traditional banking to AI-driven platforms → Highlights increasing complexity and systemic risks.
  - Figure 2: Conceptual model linking personality, self-control, literacy, and demographics to credit behaviors → Shows psychological and demographic drivers of credit use.
  - Figure 3: Framework from alternative data to ML models to habit formation → Illustrates iterative role of data-driven interventions in building habits.
  - Figure 4: Feedback loop of consumer action, data capture, ML analysis, and personalized feedback → Depicts adaptive cycle for continuous habit reinforcement.
  - Table 1: Comparative overview of alternative data types (social, behavioral, transactional) with advantages and risks → Identifies trade-offs in data source reliability and privacy.
  - Table 2: Key behavioral and demographic factors influencing credit use → Shows predictors of responsible vs. risky credit behavior.
  - Table 3: Comparison of statistical and ML models in credit risk evaluation → Demonstrates accuracy-transparency trade-off in model selection.
  - Table 4: Comparative effectiveness of data-driven interventions → Shows stronger short-term effects for nudges and feedback than for disclosures.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Alternative Data
    definition: Nontraditional data sources beyond credit reports, including social, behavioral, and transactional information.
  - term: Mental Accounting
    definition: Cognitive partitioning of financial resources into separate categories, influencing spending and saving decisions.
  - term: Statement Effect
    definition: Temporary reduction in spending or increase in payment activity following receipt of a credit card statement.
  - term: Off-Label Use
    definition: Application of credit scores for non-lending purposes such as employment or housing decisions.
critical_citations:
  - "[Nwaimo et al., 2024] — Predictive analytics for financial inclusion using ML."
  - "[Zhao et al., 2022] — Factors affecting online consumer credit behavior in China."
  - "[Suhadolnik et al., 2023] — ML for enhanced credit risk assessment."
  - "[Hershfield et al., 2015] — Psychological insights for responsible credit use."
  - "[Blanke, 2020] — Legal comparison of inferences drawn under GDPR and CCPA."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Reviews behavioral drivers (personality, self-control, literacy) that directly shape credit and spending behavior.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: Discusses cyclical spending tied to credit card statements and mental accounting, relevant to spending cycles.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: Provides general temporal patterns but lacks specific focus on Filipino cultural occasions.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Surveys digital lending platforms and Fintech innovations as part of the credit ecosystem.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Reviews personality traits, self-control, and financial literacy as key determinants of credit behavior.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: contextual
      justification: Addresses use of alternative data for inclusion but does not explicitly tackle cold-start profiling.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Reviews ML classification models (e.g., XGBoost) for risk profiling, relevant to behavioral classification.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: Mentions ML models for credit risk but not explicitly forecasting sequential spending.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: Discusses information design and feedback but not specific budgeting strategy formulation.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Mentions ML for risk assessment but not explicitly anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Does not specifically address anomaly detection algorithms for spending.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Raises critical privacy concerns regarding alternative data collection and use.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Emphasizes need for transparent AI and ethical data use to build consumer trust.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Discusses feedback mechanisms and personalized interventions to engage users.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: low
      justification: Mentions sustained support for habit formation but not explicit retention strategies.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Systematic review methodology provides a framework for evaluating interventions.
  contribution: This systematic review provides Odin with a comprehensive evidence base for integrating behavioral economics and machine learning into credit and spending management modules. It directly justifies the use of alternative data for financial inclusion and personalized behavioral nudges. The review also underscores the necessity of transparent AI and privacy safeguards, which are critical for Odin's trust and compliance modules. Its synthesis of intervention effectiveness informs the design of feedback loops and adaptive learning systems. The identified gaps in long-term habit formation research provide a roadmap for Odin's evaluation and improvement strategies.
  directly_justifies:
    - Alternative data sources (mobile, transactional) can expand credit access for underserved populations lacking traditional histories.
    - Machine learning ensemble models like XGBoost provide superior risk prediction compared to traditional logistic regression.
    - Behavioral nudges and personalized feedback show stronger short-term impacts on financial behavior than mandatory disclosures.
    - Privacy and algorithmic bias concerns necessitate transparent AI and robust regulatory frameworks in personal finance systems.
    - Financial incentives alone have limited long-term effectiveness, requiring sustained behavioral support for habit formation.
  limits:
    - The review is a secondary synthesis and does not present new empirical data.
    - Most included studies are from developed markets, with limited focus on developing economies like the Philippines.
    - Long-term behavioral impacts of data-driven interventions are underexplored due to lack of longitudinal studies.
    - Comparative analysis of intervention types across diverse cultural and economic contexts is limited.
  mapping_rationale: The systematic scan across all 12 functional domains and their associated topic codes flagged several areas of relevance. High relevance was assigned to 1.C (Financial Behavior) due to extensive coverage of personality, self-control, and literacy; 5.A (Behavioral Profiles) for the same reason; and 10.A (Data Privacy) due to critical ethical concerns. Medium relevance was assigned to 4.A (Existing Systems) for surveying digital lending, 5.C (Classification) for ML models, 10.B (User Trust) for transparency emphasis, 11.A (Engagement) for feedback mechanisms, and 12.A (Evaluation) for the systematic methodology. Low relevance was assigned to 6.B (Forecasting) and 8.A/B (Anomaly Detection) as these are not directly addressed. Contextual relevance was noted for 2.B (Cyclical Spending) and 2.D (Filipino Occasions) which lack specific cultural focus, and for 7.A (Budgeting) which is not the primary focus. Domains 3.A-C (Expense Categorization), 7.B-D (Budget Recommendation), 9.A-B (Mobile Design), and 13.A-C (Savings/Debt) were rejected as they are not addressed. Overall, the paper provides high-value behavioral and ethical insights for Odin's profiling, engagement, and privacy modules.
limitations:
  - The review is a secondary synthesis and does not present new empirical data. [unacknowledged]
  - Most included studies are from developed markets, with limited focus on developing economies like the Philippines. [unacknowledged]
  - Long-term behavioral impacts of data-driven interventions are underexplored due to lack of longitudinal studies. [acknowledged]
  - Comparative analysis of intervention types across diverse cultural and economic contexts is limited. [acknowledged]
remember_this:
  - XGBoost consistently outperforms logistic regression in credit risk prediction tasks.
  - Personality traits like conscientiousness and self-control predict responsible credit management.
  - Behavioral nudges have stronger short-term impacts than mandatory financial disclosures.
  - Privacy and algorithmic bias are critical ethical concerns in data-driven credit systems.
  - Financial incentives alone show limited long-term effectiveness for sustained habit change.
```
---

## Paper 6: Nasih & Adam_summarized.md

**Source File:** `Nasih & Adam_summarized.md`

```yaml
paper_id: 3b8e5a1c-8c3d-5791-a3f5-8b2c9d1e4f7a
designation: international
title: How do young people perceive financial literacy, and what role do they believe it plays in their future success?
authors: Nasih, M.; Adam, A. S.
year: 2025
venue: International Journal of Emerging Issues in Management, Accounting and Technology
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.D
  - 4.A
  - 5.A
  - 7.A
  - 7.D
  - 10.A
  - 11.A
  - 12.A
  - 13.B
tldr: Young adults universally recognize financial literacy's importance for future success but exhibit a knowledge-confidence paradox, with family socialization dominating formal education and digital finance creating both opportunities and risks.
problem_and_motivation: While extensive research exists on youth financial knowledge and behavior, systematic evidence on how young people perceive financial literacy and its connection to future success is fragmented, particularly in developing countries. The rapid digital transformation of financial services and recent economic crises have created new dynamics that existing reviews have not adequately addressed.
approach:
  - Systematic literature review following PRISMA 2020 guidelines.
  - Searched seven academic databases (JSTOR, ERIC, Scopus, Google Scholar, OECD iLibrary, World Bank, ProQuest) for studies published 2015-2025.
  - Included 47 empirical studies from 25 countries with over 250,000 participants aged 18-30.
  - Employed two-stage screening with inter-rater reliability (κ=0.82 for abstracts, 0.91 for full-text).
  - Used thematic synthesis (Thomas & Harden, 2008) with subgroup analyses by geographic context, gender, and educational level.
findings:
  - num: 78% of German university students rated their financial knowledge as "good" but only 34% answered basic questions correctly.
  - Family financial discussions correlated with 45% higher financial confidence scores regardless of parents' actual literacy.
  - num: 71% of EU youth felt "paralyzed by too many options" when learning about investments.
  - num: 76% of youth across studies used social media for financial information but expressed skepticism about reliability.
  - num: Youth from high-income families showed "financial cushion confidence"; low-income youth showed heightened awareness with fatalism.
  - num: Young women were 40% more likely to respond "don't know" to financial questions they could answer correctly.
  - num: 85% of participants planned to learn more about investing, but only 15-20% took concrete steps.
  - num: Crisis experiences increased financial literacy awareness scores by 28% in a U.S. longitudinal study.
  - Gender gaps narrowed by 35% when financial tasks were framed as "life planning" rather than "mathematical tests."
  - num: Having one close friend who invests increased an individual's likelihood of opening an investment account by 340%.
key_figures_tables:
  - Table 1: PRISMA flow diagram showing study selection from 1,847 records to 47 included studies.
  - Table 2: Summary of included studies by region and methodology, showing 38% from developing nations and 17% multi-country.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: PFMS
    definition: Personal Finance Management System
  - term: PRISMA
    definition: Preferred Reporting Items for Systematic Reviews and Meta-Analyses
  - term: FOMO
    definition: Fear of missing out
  - term: CASP
    definition: Critical Appraisal Skills Programme
  - term: PICOS
    definition: Population, Intervention, Comparison, Outcomes, Study design
critical_citations:
  - "[Lusardi & Mitchell, 2014] — Foundational theory on financial literacy and economic importance."
  - "[Gudmunson & Danes, 2011] — Core framework for family financial socialization."
  - "[OECD, 2020] — Key international survey on adult financial literacy."
  - "[Shim et al., 2010] — Established role of parents in youth financial socialization."
  - "[Kaiser et al., 2021] — Major meta-analysis on financial education effectiveness."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Systematic review of youth (18-30) financial perceptions directly informs understanding of the target demographic.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Discusses income, debt, and financial challenges relevant to understanding financial structures.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly examines youth financial behavior, including confidence-action gaps and risk-taking.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Reveals cultural variations in financial perceptions, family socialization, and success conceptualizations.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: Mentions cultural factors and family obligations influencing financial behavior, relevant to spending cycles.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews existing financial education systems and their limitations in shaping youth perceptions.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies gaps in formal financial education and the dominance of informal family influences.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Documents awareness-confidence paradox and behavioral intention patterns essential for profiling.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: Mentions how financial shocks trigger learning, relevant to dynamic profile changes.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: low
      justification: Discusses digital tools but not predictive modeling specifically.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Examines youth perceptions of budgeting skills and their importance for financial security.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: contextual
      justification: Mentions how youth feel "paralyzed by too many options" when making financial decisions, relevant to constraint handling.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Not directly addressed; no discussion of anomaly detection.
    - code: 9.A
      name: Mobile‑First Design Principles and Rationale
      relevance: medium
      justification: Digital natives' comfort with financial apps and need for explainable AI are highly relevant to mobile-first design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Discusses youth's trust issues with financial education sources and need for digital literacy.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: Reveals engagement patterns: intention-action gaps, social influence, and crisis-driven behavior changes.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: Findings on gamification and social proof inform retention strategies.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Critiques existing evaluation methods (knowledge vs. perceptions) and suggests new assessment approaches.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: low
      justification: Not directly discussed; no algorithmic evaluation.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: medium
      justification: Discusses youth's emphasis on financial literacy for debt avoidance and security.
    - code: 13.C
      name: End‑of‑Period Surplus as a Savings Input
      relevance: contextual
      justification: Mentions savings goals and family security, indirectly relevant to surplus management.
  contribution: This systematic review provides foundational evidence on youth financial literacy perceptions, directly justifying Odin's user research and behavioral profiling modules. The awareness-confidence paradox informs the design of confidence-building features and personalized financial education. The dominance of family socialization supports Odin's need for social and collaborative features, while the digital dual nature guides UX design for transparency and explainability.
  directly_justifies:
    - "Young adults universally recognize financial literacy's importance but overestimate their competence."
    - "Family financial socialization dominates formal education in shaping youth financial perceptions."
    - "Digital finance creates both opportunities and risks requiring dedicated digital financial literacy."
    - "Structural inequalities along gender, socioeconomic, and geographic lines persist in financial perceptions."
    - "Crisis-driven learning suggests reactive rather than proactive financial capability development."
  limits:
    - "English-language publication bias may underrepresent research from non-English speaking countries."
    - "Heterogeneity of financial literacy definitions and measures complicates synthesis."
    - "Rapid financial innovation may render some findings outdated quickly."
    - "Most studies are cross-sectional, limiting understanding of perception evolution over time."
    - "Limited intervention effectiveness studies with perception outcomes."
  mapping_rationale: The systematic scan across all 12 functional domains and their associated topic codes identified the paper as highly relevant to Odin. The paper directly informs domains like Filipino Cultural Context (themes of family socialization and cultural variation), Existing Systems & Gaps (critique of formal education), Behavioral Profiling (awareness-confidence paradox), and User Retention (engagement patterns). Borderline cases included the paper's relevance to Budget Recommendation (youth perceptions of budgeting importance) and Mobile Design (digital natives' use of financial apps). Domains considered but rejected included Predictive Modeling and Anomaly Detection, as the paper does not discuss algorithmic techniques. The paper offers strong foundational justification for Odin's user-centered design and behavioral insights.
limitations:
  - "English-language publication bias may underrepresent research from non-English speaking countries. [unacknowledged]"
  - "Heterogeneity of financial literacy definitions and measures complicates synthesis. [acknowledged]"
  - "Rapid financial innovation may render some findings outdated quickly. [acknowledged]"
  - "Most studies are cross-sectional, limiting understanding of perception evolution over time. [acknowledged]"
  - "Limited intervention effectiveness studies with perception outcomes. [acknowledged]"
remember_this:
  - "Young adults recognize financial literacy's importance but overestimate their competence."
  - "Family financial socialization dominates formal education in shaping youth financial perceptions."
  - "Digital finance creates both opportunities and risks for youth financial capability."
  - "Structural inequalities along gender and socioeconomic lines persist in financial perceptions."
  - "Only 15-20% of youth who plan to learn about finance actually take concrete steps."
```
---

## Paper 7: Isaga_summarized.md

**Source File:** `Isaga_summarized.md`

```yaml
paper_id: 10.20525/ijrbs.v14i7.4383
designation: international
title: Financial literacy and financial wellbeing of youth entrepreneurs: The mediating role of financial behaviour
authors: Isaga, N.
year: 2025
venue: International Journal of Research in Business and Social Science
odin_topics:
  - 1.A
  - 1.C
  - 5.A
  - 5.B
  - 7.A
  - 13.B
tldr: Financial literacy positively affects financial well-being of youth entrepreneurs, with financial behaviour partially mediating this relationship.
problem_and_motivation: Financial well-being among youth entrepreneurs in developing economies is critical yet understudied. The mechanisms linking financial literacy to financial well-being, particularly the role of financial behaviour, remain unclear.
approach:
  - Data were collected from 455 youth entrepreneurs in urban Tanzania using structured questionnaires.
  - The study employed a cross-sectional design and utilized Structural Equation Modelling (SEM) for analysis.
  - The research model examined direct and indirect relationships between financial literacy, financial behaviour, and financial well-being.
  - Financial behaviour was assessed as a mediating variable between financial literacy and financial well-being.
  - The study draws on human capital theory and behavioural economics as theoretical frameworks.
findings:
  - Financial literacy significantly and positively affects the financial well-being of youth entrepreneurs.
  - Financial literacy significantly influences financial behaviour.
  - Financial behaviour partially mediates the relationship between financial literacy and financial well-being.
key_figures_tables:
  - "None."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: Financial Well-Being
    definition: A multidimensional construct reflecting objective indicators and subjective ability to manage finances and plan for the future.
  - term: Financial Literacy
    definition: The ability to understand, process, and apply financial information for effective decision-making.
  - term: Financial Behaviour
    definition: Daily financial practices including budgeting, saving, and debt management that apply financial knowledge.
  - term: SEM
    definition: Structural Equation Modelling, a statistical technique for analyzing structural relationships between variables.
critical_citations:
  - "[Lusardi & Mitchell, 2014] — Foundational work on financial literacy and behavior."
  - "[Lusardi & Messy, 2023] — Links financial literacy to positive financial outcomes."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Provides context on youth entrepreneurs in developing economies, analogous to young professionals.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Directly investigates financial behaviour and its link to financial well-being.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: The study's core focus is on financial behaviour and its mediating role, informing profile design.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: Findings on behaviour as a mediator support the need for dynamic profiles based on behaviour.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Emphasizes budgeting as a key financial behaviour linked to positive outcomes.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: low
      justification: Mentions debt management as part of financial behaviour, providing secondary support.
  contribution: This paper provides empirical evidence that financial behaviour mediates the link between financial literacy and financial well-being, which can inform Odin's behavioral profiling module. It justifies the need for Odin to track not just financial knowledge but also users' actual budgeting, saving, and debt management practices. The findings support the design of Odin's engagement mechanisms, as reinforcing positive behavior is shown to improve financial outcomes. This contributes to Odin's evaluation framework by highlighting behavioural metrics as key indicators of success. The study also reinforces the importance of educational content within Odin, linking knowledge to practice.
  directly_justifies:
    - "Financial behaviour partially mediates the relationship between financial literacy and financial well-being."
    - "Consistent application of financial knowledge through daily practices leads to improved financial outcomes."
    - "Financial literacy is foundational for enhancing economic decision-making among youth."
  limits:
    - "Cross-sectional design limits causal inferences about behaviour and well-being."
    - "Sample limited to urban areas in Tanzania may not generalize to other contexts." [unacknowledged]
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was conducted. The paper was flagged as relevant to the 'Behavioral Profiling & Classification' domain (codes 5.A, 5.B) due to its focus on financial behaviour as a mediator, with 5.A assigned high relevance and 5.B medium. It also touches on 'Filipino Cultural Context' (codes 1.A, 1.C) through its study of youth entrepreneurs, with 1.A contextual and 1.C medium. 'Budget Recommendation' (7.A) and 'Savings & Debt Management' (13.B) were assigned medium and low relevance respectively, as budgeting and debt management are key behaviours discussed. Domains such as 'Expense Categorization', 'Spending Forecasting', 'Anomaly Detection', and 'Mobile-First Design' were considered and rejected as the paper does not address these technical or design aspects. The paper's overall relevance to Odin is moderate, providing theoretical and empirical justification for the importance of behavioural tracking and reinforcement.
limitations:
  - "Cross-sectional design limits causal inferences about behaviour and well-being."
  - "Self-reported data may introduce response bias."
  - "Focus on Tanzanian youth entrepreneurs may limit generalizability to Filipino young professionals." [unacknowledged]
remember_this:
  - "Financial literacy alone is insufficient without consistent financial behaviour."
  - "Behaviour mediates the link between financial knowledge and well-being."
  - "Budgeting, saving, and debt management are key practices linking literacy to outcomes."
  - "Partial mediation confirms knowledge and practice together enhance financial well-being."
```
---

## Paper 8: Imawan et al_summarized.md

**Source File:** `Imawan et al_summarized.md`

```yaml
paper_id: 10.58536/j-hytel.166
designation: international
title: Enhancing Financial Literacy in Young Adults: An Android-Based Personal Finance Management Tool
authors: Imawan, R.; Putra, W. P.; Alqahtani, R.; Milakis, E. D.; Dumchykov, M.
year: 2025
venue: Journal of Hypermedia & Technology-Enhanced Learning
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 9.A
  - 9.B
  - 11.A
  - 11.B
  - 12.A
  - 13.A
tldr: An Android PFM app using the Waterfall model achieved a 4.6/5 usability score, demonstrating that targeted digital tools can improve financial habits in young adults.
problem_and_motivation: Young adults face financial challenges from limited experience, yet existing tools often fail to engage them. There is a practical gap in using mobile-first solutions tailored to this demographic's needs.
approach:
  - The application was developed using the Waterfall model with Laravel (backend) and Flutter (frontend).
  - Requirements were gathered via interviews and surveys with young adults in higher education.
  - Features include income/expense tracking, budget projection, financial goal setting, and notifications.
  - Black-box testing verified the functionality of core modules including login, tracking, goals, budgets, reports, and notifications.
  - Usability was evaluated by 50 users on a 5-point Likert scale across six aspects: usability, user satisfaction, functionality, engagement, design, and feedback.
findings:
  - The application achieved an overall score of 4.6/5, rated 'Excellent'.
  - Users rated design satisfaction highly, with 74% giving a 5 for visual appeal and 70% for layout clarity.
  - Engagement was strong, with 78% of users likely to continue using the app and 76% feeling motivated to track finances.
  - Features like income/expense tracking and budget projections were highly rated for both functionality and satisfaction.
  - Users requested additional customization options and more detailed financial trend analysis.
key_figures_tables:
  - Figure 10: Average scores per evaluation aspect → All six aspects scored above 4.5/5, indicating consistent high performance.
key_equations:
  - equation: Aspect Score = (Sum(Indicator Scores)) / (Number of Indicators)
    explanation: Calculates average score for each evaluation aspect.
  - equation: Overall Application Score = (Sum(Aspect Scores)) / (Number of Aspects)
    explanation: Calculates the total average score across all aspects.
definitions:
  - term: Waterfall Model
    definition: A linear, sequential software development methodology with distinct phases.
  - term: Black-box Testing
    definition: A testing method that evaluates functionality without inspecting internal code.
critical_citations:
  - "[Lusardi & Messy, 2023] — Foundational work on financial literacy and wellbeing."
  - "[Petersen et al., 2009] — Contextualizes the Waterfall model in large-scale development."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: The study focuses on young adults in higher education, analogous to the Filipino target demographic.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: contextual
      justification: Discusses income and expense structures relevant to young adults.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: contextual
      justification: The study explicitly addresses financial habits and literacy, similar to the target behavior.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: The application includes a detailed expense categorization module.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: User feedback indicated a need for more customization in categories, directly informing design considerations.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: The introduction reviews existing tools and identifies a gap for young adults, directly mapping to this topic.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: The study explicitly states that existing tools overlook young users' needs, a key gap for Odin to address.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: The application aims to influence financial behaviors through engagement, touching on profiling.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: high
      justification: The study uses an Android-based app, providing evidence for the efficacy of mobile-first design for financial management.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: high
      justification: The high usability scores (4.6/5) validate the UX design choices made in the application.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: The study measures engagement and finds that notifications and progress tracking improve it.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: The notification module and goal-tracking features are cited as key retention and engagement mechanisms.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: The study uses a specific evaluation framework (Likert scale across six aspects) to assess its system.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: The financial goal module is a core feature, enabling users to set and track savings targets.
  contribution: "This paper provides a validated reference implementation for a mobile-first PFM app targeting young adults. The usability framework (six aspects with a Likert scale) offers a direct evaluation template for Odin's user testing. The findings on engagement drivers (notifications and goal progress) justify Odin's design for retention. The user feedback on customization and trend analysis highlights specific feature gaps that Odin should prioritize."
  directly_justifies:
    - "A mobile-first approach is effective for engaging young adults in personal finance management."
    - "Notification reminders and visual goal progress are key mechanisms for encouraging consistent financial tracking."
    - "User satisfaction is strongly correlated with intuitive design and accurate transaction recording."
    - "Young adults in higher education have specific financial management needs that generic tools fail to address."
    - "High usability scores are achievable with a well-designed PFM app, supporting the feasibility of Odin's development."
  limits:
    - "The study's evaluation period was short (two weeks), potentially not capturing long-term habit formation."
    - "The sample was limited to 50 university students from one institution, which may not be representative of all young adults."
    - "The paper does not evaluate the system's ability to handle infeasible budget constraints."
    - "The study does not incorporate predictive modeling or forecasting algorithms for spending."
    - "The evaluation was conducted in a beta testing environment, not a live production setting with real-world data."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper's focus on building and evaluating a PFM app made domains 3 (Expense Categorization), 4 (Existing Systems & Gaps), 9 (Mobile-First Design), 11 (User Retention & Engagement), 12 (System Evaluation), and 13 (Savings & Debt Management) highly relevant. Domains related to predictive modeling (6), anomaly detection (8), and data privacy (10) were considered and rejected as the paper does not implement algorithmic forecasting or anomaly detection, nor does it detail privacy mechanisms. The paper's discussion of financial behaviors and target demographics provided contextual support for domains 1 (Filipino Young Professionals) and 5 (Behavioral Profiling). The mapping resolved borderline cases by prioritizing direct feature implementations (e.g., 3.A and 13.A) over behavioral framing (e.g., 5.A), which was assigned a 'medium' or 'contextual' relevance. Overall, the paper is highly relevant for validating Odin's core design and evaluation approach but offers limited insight into its more advanced algorithmic and privacy-focused modules."
limitations:
  - "The evaluation was conducted in a controlled environment with a limited time frame, which may not reflect long-term usage patterns."
  - "The sample of 50 university students from a single institution may not be generalizable across different cultural or economic contexts. [unacknowledged]"
  - "The study does not assess the application's performance on older devices or under varying network conditions. [unacknowledged]"
  - "The paper lacks a rigorous statistical analysis of pre- and post-intervention financial literacy. [unacknowledged]"
remember_this:
  - "The app received an overall usability score of 4.6 out of 5."
  - "Notifications and goal tracking are key drivers for user engagement."
  - "Users frequently requested more customization and detailed spending analysis."
  - "A mobile-first design is validated as effective for young adult financial management."
  - "The evaluation framework covers usability, satisfaction, functionality, engagement, design, and feedback."
```
---

## Paper 9: Duvalla_summarized.md

**Source File:** `Duvalla_summarized.md`

```yaml
paper_id: 10.32996/jcsts.2025.7.4.12
designation: international
title: Human-AI Collaboration in Customer Behavior Research: Personalizing Financial Services
authors: Duvalla, V. R.
year: 2025
venue: Journal of Computer Science and Technology Studies
odin_topics:
  - 3.A
  - 4.A
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 7.B
  - 10.A
  - 10.B
  - 12.A
tldr: Human-AI collaboration enhances financial personalization by combining AI's pattern recognition with human contextual and ethical oversight.
problem_and_motivation: Financial institutions struggle to implement effective personalization due to fragmented data and the complexity of interpreting customer behavior. Purely algorithmic or human-driven approaches are insufficient for nuanced, culturally-aware financial advice. A framework that synergizes AI capabilities with human expertise is needed to address these gaps.
approach:
  - The paper reviews existing literature and industry reports on AI applications in financial services.
  - It proposes a human-in-the-loop (HITL) framework that integrates AI models with human expertise for knowledge collaboration and ethical oversight.
  - It details a data infrastructure including integrated platforms, real-time processing, and governance frameworks.
  - It discusses advanced AI models for customer segmentation, including multi-dimensional behavioral, temporal pattern, and neural network approaches.
  - It presents a case study of JP Morgan Chase's implementation of a human-AI collaborative platform.
findings:
  - num: 31% improvement in customer retention metrics for banks using advanced analytics.
  - Human-guided AI models achieve higher accuracy in predicting customer financial needs than fully automated systems.
  - Human-in-the-loop protocols improve model prediction accuracy compared to automated systems alone.
  - num: 59% higher customer satisfaction scores are achieved with unified omnichannel orchestration.
  - Federated learning can achieve predictive accuracy of centralized models while keeping customer data local.
  - Financial institutions with formal ethical review boards identify more potential adverse impacts during model development.
key_figures_tables:
  - Figure 1: Data Infrastructure for Behavioral Analysis → Shows integrated data, real-time processing, and governance layers.
  - Figure 2: Advanced AI Models for Customer Segmentation → Illustrates clustering, temporal mining, and neural network architectures.
  - Table 1: Comparative Analysis of Human-AI Collaboration Models → Compares collaboration models and their key characteristics.
  - Figure 3: Operationalizing Predictive Insights in Financial Services → Depicts insight deployment, omnichannel orchestration, and experimentation.
  - Figure 4: Future Directions and Ethical Considerations in Financial AI → Highlights explainable AI, privacy, and governance models.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: HITL
    definition: Human-in-the-loop, a paradigm where human expertise is integrated into AI systems.
  - term: XAI
    definition: Explainable Artificial Intelligence, techniques to make AI decisions interpretable.
  - term: PFMS
    definition: Personal Financial Management System, software for managing personal finances.
critical_citations:
  - "[Karangara et al., 2024] — foundational for HITL frameworks in fintech."
  - "[Kong et al., 2010] — essential for temporal pattern discovery."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Discusses behavioral segmentation for financial personalization.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides background on challenges in financial personalization.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly addresses behavioral segmentation and profiling using AI.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: Mentions the need for temporal patterns to predict future behaviors.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Details advanced clustering and neural network approaches for classification.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Focuses on AI models for predicting customer financial needs and churn.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Relates to personalization of financial advice, but does not specifically address budget recommendation.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Dedicated section on privacy-preserving technologies like federated learning.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Emphasizes explainability and ethical governance to build user trust.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Discusses continuous optimization through experimentation and A/B testing.
  contribution: The paper provides a comprehensive framework for human-AI collaboration that can inform the design of Odin's behavioral profiling module (5.A) by detailing advanced segmentation techniques. Its emphasis on privacy-preserving personalization (10.A) directly supports Odin's data handling requirements. The discussion on ethical oversight and explainability (10.B) justifies the need for transparent and trustworthy features in Odin. Furthermore, the case study on JP Morgan Chase offers a real-world example of operationalizing such a system, which can guide the architecture of Odin's predictive and recommendation engines (6.A, 7.B).
  directly_justifies:
    - Human-AI collaboration improves model prediction accuracy.
    - Advanced clustering identifies up to 15 distinct behavioral segments.
    - Federated learning enables personalization without centralizing sensitive data.
    - Real-time contextual awareness increases conversion rates on personalized offers.
    - Ethical governance frameworks are essential for responsible AI implementation.
  limits:
    - The paper is a review and does not present original experimental results.
    - It lacks a specific evaluation methodology for the proposed human-AI framework.
    - The case study is based on a single large institution and may not be generalizable to smaller contexts.
    - Discussion of budget recommendation systems is minimal.
  mapping_rationale: A systematic scan across all 12 functional domains was conducted. The paper's core focus on human-AI collaboration for financial personalization flagged the domains of Behavioral Profiling & Classification, Spending Forecasting, Data Privacy & User Trust, and System Evaluation as highly relevant. Specifically, topic codes 5.A (high) and 6.A (high) were selected for their direct focus on behavioral profiling and predictive modeling. Codes 10.A and 10.B (high) were chosen for their dedicated sections on privacy and trust, which are critical for Odin. 3.A (medium) was selected due to its relevance to segmentation, while 5.C (medium) and 12.A (medium) were included for their supporting discussions on classification and evaluation. 5.B (low) and 7.B (low) were considered but given lower relevance due to only tangential mentions of cold-start and budget recommendation. The domains of Filipino Cultural Context, Expense Categorization (beyond 3.A), Existing Systems & Gaps (beyond 4.A as contextual), Anomaly Detection, Mobile-First Design, and Savings & Debt Management were considered and rejected as the paper does not provide actionable insights for these specific Odin modules. Overall, the paper offers strong support for Odin's user modeling and trust/privacy features.
limitations:
  - The analysis is derived from secondary sources and industry reports.
  - Limited discussion on the specific algorithms for anomaly detection or budget allocation.
  - The paper does not address the cold-start problem in financial profiling. [unacknowledged]
  - No specific evaluation of user retention mechanisms for PFMS. [unacknowledged]
  - It does not cover mobile-first design principles. [unacknowledged]
remember_this:
  - Human-AI collaboration achieves 31% higher retention rates.
  - Federated learning maintains prediction accuracy while preserving privacy.
  - Real-time insights increase conversion rates on personalized offers by 59%.
  - Explainable AI is essential for building customer trust.
  - Ethical oversight is critical for fair and responsible personalization.
```
---

## Paper 10: Efendi & Widagdo_summarized.md

**Source File:** `Efendi & Widagdo_summarized.md`

```yaml
paper_id: 10.59890/ijaeam.v3i3.18
designation: international
title: Simple Financial Management in Housewife Communities: A Qualitative Study on Daily Financial Management Patterns
authors: Efendi, M. I.; Widagdo, C. S.
year: 2025
venue: International Journal of Applied Economics, Accounting and Management
odin_topics:
  - 2.A
  - 2.B
  - 3.A
  - 4.A
  - 4.B
  - 5.A
  - 7.A
  - 9.A
  - 10.A
  - 11.A
  - 13.A
  - 13.B
tldr: Housewives in Salatiga develop sophisticated financial management practices including nuanced recording, community-based risk management, and social networks that challenge conventional financial literacy narratives.
problem_and_motivation: Housewives in Indonesia manage daily finances despite lower formal financial literacy rates, yet their sophisticated adaptive strategies remain understudied and undervalued. This research addresses the gap in understanding the daily financial management practices of housewives in resource-constrained communities.
approach:
  - This qualitative case study was conducted in Salatiga, Central Java, involving 25 housewives as primary financial managers.
  - Data was collected through in-depth semi-structured interviews, non-participant observation, and document analysis over two months.
  - Analysis was performed using ATLAS.ti software with open, axial, and selective coding procedures.
  - Member checking was employed to validate findings and ensure accurate representation of participants' experiences.
  - The study focused on daily financial practices, adaptation strategies, and community interactions within a middle to lower-income demographic.
findings:
  - num: 60% of informants perform routine expense recording using simple manual books, while 40% rely on mental monitoring systems.
  - num: Income diversification activities generate an additional Rp300,000 to Rp500,000 per month for some housewives.
  - num: Daily emergency fund contributions range from Rp5,000 to Rp10,000, held in physical containers like tins or envelopes.
  - Housewives develop sophisticated "mental accounting" strategies for prioritizing primary over secondary and tertiary needs.
  - Communities function as informal financial institutions through ROSCAs, jimpitan, and collective purchasing arrangements.
  - Financial communication patterns range from open collaborative to minimal, influenced by education and gender dynamics.
  - Social networks serve as informal insurance mechanisms, providing support during emergencies like illness or hospitalization.
  - Some housewives practice micro-scale savings diversification, including cash in multiple locations and small gold investments.
key_figures_tables:
  - "None."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: ROSCA
    definition: "Rotating Savings and Credit Association; a community-based savings mechanism where members contribute and receive a lump sum in rotation."
  - term: jimpitan
    definition: "A community-based micro-savings practice involving daily collection of rice or small change for social funds."
  - term: mental accounting
    definition: "The cognitive process of categorizing and mentally budgeting funds for specific purposes without physical segregation."
critical_citations:
  - "[Palupiningtyas et al., 2023] — Establishes women's role in domestic financial management despite structural disadvantages."
  - "[Siregar, 2019] — Defines housewives' role in family financial management as a key research area."
  - "[Rutherford] — Introduces concept of 'shadow banking' in community financial systems."
relevance:
  topics:
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: "Documents specific practices like arisan (ROSCAs) and jimpitan as culturally embedded financial mechanisms."
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: "Describes financial cycles synchronized with income patterns and community events, though not explicitly seasonal."
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: "Provides detailed insights into how housewives prioritize and categorize expenses into primary, secondary, and tertiary needs."
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: "Maps the landscape of informal financial systems (ROSCAs, jimpitan) used alongside formal systems in the community."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: "Highlights the gap between formal financial education and the practical needs of housewives."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: "Identifies behavioral profiles based on financial recording, communication, and risk management patterns."
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: "Provides a real-world case of budgeting strategies, including mental accounting and expenditure prioritization."
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: "Briefly mentions the potential for mobile applications but does not focus on design principles."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: "Mentions trust in informal community systems but does not address digital data privacy."
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: "Discusses community engagement but not engagement with digital PFMS."
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: "Documents micro-savings practices and goal-oriented savings like emergency funds and gold accumulation."
    - code: 13.B
      name: Debt Management in PFMS
      relevance: medium
      justification: "Describes rotation debt systems and community norms around borrowing for productive vs. consumptive needs."
  contribution: "This paper contributes to Odin's design by validating the sophistication of informal financial practices that a PFMS can build upon. It informs Odin's expense categorization module by demonstrating real-world mental accounting strategies. The findings on community-based financial networks justify Odin's potential for social or community features. The paper also highlights the importance of user trust and accessibility, aligning with Odin's mobile-first and data privacy considerations."
  directly_justifies:
    - "Housewives in resource-constrained environments develop sophisticated mental accounting systems that formal PFMS can emulate."
    - "Financial literacy in such contexts is experiential and embedded, requiring PFMS to be contextually adaptive."
    - "Community-based financial systems like ROSCAs demonstrate the value of social features within a PFMS."
  limits:
    - "The study is specific to Salatiga, Indonesia, and findings may not be generalizable to other cultural or economic contexts."
    - "Findings are based on self-reported data, which may be subject to social desirability bias."
    - "The study focuses on daily management and does not address long-term financial planning or investment." [unacknowledged]
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant for domains on Filipino Cultural Context (specifically 2.A), Expense Categorization (3.A), and Budget Recommendation (7.A) due to its detailed documentation of real-world financial practices. Medium relevance was assigned to Existing Systems & Gaps (4.A, 4.B), Behavioral Profiling (5.A), Savings & Debt Management (13.A, 13.B) as these are addressed indirectly. Low relevance was noted for Mobile-First Design (9.A) and Engagement Dynamics (11.A) as the paper does not discuss digital applications. Contextual relevance was assigned to Data Privacy (10.A) due to trust in informal systems. Domains related to Forecasting (6.A, 6.B), Anomaly Detection (8.A, 8.B, 8.C), and System Evaluation (12.A, 12.B, 12.C) were rejected as the paper does not address algorithmic or predictive modeling. Overall, the paper provides strong qualitative evidence for the design of user-centric and community-aware PFMS features."
limitations:
  - "The study does not acknowledge the potential for technology to support or replace the manual systems observed." [unacknowledged]
  - "The sample size of 25 housewives limits the generalizability of the findings." [unacknowledged]
remember_this:
  - "Housewives use mental accounting and physical segregation to manage daily finances."
  - "Community systems like ROSCAs act as informal financial institutions for saving and credit."
  - "Income diversification provides additional autonomy and financial resilience for housewives."
  - "num: 60% of housewives perform routine expense recording using simple manual books."
```
---

## Paper 11: Koswar et al_summarized.md

**Source File:** `Koswar et al_summarized.md`

```yaml
paper_id: 10.63125/cv50rf30
designation: international
title: Digitization in Retail Banking: A Review of Customer Engagement and Financial Product Adoption in South Asia
authors: Kowsar, M. M.; Islam, S.; Mohiuddin, M.; Siddiqui, N. A.
year: 2025
venue: 1st Global Research and Innovation Conference 2025
odin_topics:
  - 1.A
  - 2.A
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 9.A
  - 9.B
  - 10.A
  - 11.A
  - 11.B
  - 12.A
  - 13.A
tldr: A systematic review of how digitization, mobile infrastructure, and AI-driven personalization reshape customer engagement and financial product adoption across South Asia.
problem_and_motivation: Retail banking digitization is transforming customer engagement and product adoption globally, but a comprehensive, region-specific synthesis for South Asia is lacking. Understanding these dynamics is crucial for informing inclusive digital financial strategies.
approach:
  - Systematic review following the PRISMA 2020 framework.
  - Searched Scopus, Web of Science, JSTOR, EBSCOhost, ProQuest, Google Scholar, and institutional repositories.
  - Covered 84 peer-reviewed studies published between 2010 and 2024.
  - Synthesized findings on digital infrastructure, customer engagement, product adoption, and inclusion.
  - Analyzed the interplay of fintech innovation, regulatory frameworks, and socio-cultural determinants.
findings:
  - num: Mobile phone penetration exceeds 85% and mobile broadband reaches over 95% in countries like India and Sri Lanka.
  - num: Digitally engaged customers in India were 2.3 times more likely to open secondary financial products.
  - Personalization, interactivity, and user experience are critical determinants of engagement in digital banking.
  - AI and Big Data enable predictive analytics, behavioral modeling, and hyper-personalized services.
  - Digital inclusion is uneven; many new accounts are dormant, and usage is concentrated among urban, literate populations.
  - Product adoption is high for savings, microloans, and insurance, driven by simplified interfaces and automated workflows.
  - Customer engagement is a key differentiator for user retention and financial activity levels.
  - Regulatory support and fintech innovation must operate synergistically for sustainable digital banking.
  - Interface simplicity and automated onboarding can substitute for formal financial literacy.
  - Gender, age, and digital literacy remain significant barriers to equitable participation.
key_figures_tables:
  - Figure 1: Conceptual framework linking digitization to customer engagement and product adoption → Framework shows digitization as central driver.
  - Figure 2: Map of digitization enabling financial services delivery in South Asia → Highlights mobile, ID, and fintech as key enablers.
  - Figure 5: Drivers of customer engagement in digital banking → Personalization, UX, and behavioral nudges are key.
  - Figure 7: Pathways from financial exclusion to inclusion through digital banking → Shows JAM trinity and mobile models bridging access gaps.
  - Figure 8: Key findings from the review → Summarizes infrastructure, product adoption, and engagement outcomes.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Digitization
    definition: Conversion of analog information and manual processes into digital formats, enabling automation and real-time processing.
  - term: Financial Inclusion
    definition: Access to useful and affordable financial products and services delivered responsibly and sustainably.
  - term: Customer Engagement
    definition: Emotional and behavioral involvement of customers with digital banking services, extending beyond transactions.
  - term: Fintech
    definition: Technology-driven innovation in financial services, offering specialized solutions like peer-to-peer lending and robo-advisory.
  - term: JAM Trinity
    definition: India's policy framework linking Jan Dhan bank accounts, Aadhaar digital identity, and Mobile connectivity.
critical_citations:
  - "[Vrana & Singh, 2025] — Defines digitization and its transformative role in banking."
  - "[Lashitew et al., 2020] — Discusses mobile-enabled hybrid financial services in South Asia."
  - "[Koskelainen et al., 2023] — Links literacy to digital financial service adoption and trust."
  - "[Van Veldhoven & Vanthienen, 2022] — Examines fintech-regulatory interplay for digital ecosystem stability."
  - "[Kumar et al., 2019] — Provides foundational framework for multi-dimensional customer engagement."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Provides comparative insights on young, digitally-savvy users in South Asia.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: Discusses socio-cultural determinants of engagement, such as gender and collective decision-making.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Comprehensively reviews digital banking ecosystems and fintech platforms in South Asia.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Highlights urban-rural disparities, dormant accounts, and socio-demographic barriers.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Discusses behavioral determinants like literacy and trust influencing engagement profiles.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: low
      justification: Mentions AI-driven onboarding and behavioral nudges, but not cold-start profiling explicitly.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: References AI for behavioral modeling but does not detail classification methods.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: high
      justification: Emphasizes mobile-first ecosystems as primary access channels in South Asia.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: high
      justification: Identifies UX personalization, localization, and gamification as key engagement drivers.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Notes cybersecurity and biometric verification as critical for user trust and inclusion.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: Directly examines behavioral, cognitive, and emotional engagement in digital banking.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: high
      justification: Finds that personalized prompts and goal-setting features significantly enhance retention.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses a systematic review methodology (PRISMA) as an evaluation framework.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Reviews micro-savings products and gamified incentives for low-income users.
  contribution: This review provides a comprehensive, region-specific synthesis of digital banking transformation that directly informs Odin's understanding of mobile-first engagement in emerging markets. Its findings on AI-driven personalization, behavioral nudges, and UX design justify the development of Odin's recommendation and engagement modules. The paper's detailed examination of financial inclusion barriers and demographic disparities supports Odin's focus on inclusive, culturally-sensitive design for Filipino young professionals. The synthesis of fintech-regulatory interplay and user trust considerations provides a strategic foundation for Odin's architecture and data privacy approach.
  directly_justifies:
    - "Mobile-first design and interface localization are essential for retaining users in competitive fintech ecosystems."
    - "AI-powered behavioral nudges and personalized financial tools significantly increase adoption of savings and credit products."
    - "User engagement, driven by personalization and interactivity, is a critical determinant of platform loyalty and product uptake."
    - "Digitization lowers entry barriers but must be paired with inclusive design to bridge socio-demographic gaps."
  limits:
    - "Focuses on South Asia, limiting direct generalizability to the Philippines without adaptation."
    - "Synthesizes existing literature rather than presenting new primary empirical data."
    - "Does not deeply evaluate specific algorithm performance or computational techniques."
  mapping_rationale: A systematic scan across all 12 functional domains was conducted. The domains of "Existing Systems & Gaps," "Behavioral Profiling & Classification," "Mobile-First Design," and "User Retention & Engagement" were flagged as highly relevant, leading to the selection of topics 4.A, 4.B, 5.A, 9.A, 9.B, 11.A, and 11.B as high or medium relevance. The "Filipino Cultural Context" domain (topics 2.A, 2.B, 2.C, 2.D) was considered, but the paper's focus on South Asia limits its applicability; only 2.A (culturally specific practices) was deemed contextual. Domains like "Expense Categorization," "Spending Forecasting," "Budget Recommendation," and "Anomaly Detection" were considered but rejected as the paper does not address these specific technical modules. The "Savings & Debt Management" domain was partially relevant (topic 13.A) due to the review of micro-savings products. Overall, the paper provides strong justification for Odin's design in engagement, UX, and inclusion strategy, though its technical algorithmic contributions are minimal.
limitations:
  - "Limited direct applicability of South Asian findings to the Filipino context without further validation."
  - "Relies on secondary sources, which may inherit biases or gaps from the original studies."
  - "The rapid evolution of digital finance means some findings may become outdated quickly."
  - "Focuses on retail banking broadly, not specifically on personal finance management applications like Odin. [unacknowledged]"
remember_this:
  - "Digital engagement significantly increases cross-buying of financial products."
  - "Mobile-first design and personalization are critical for user retention in digital finance."
  - "AI and big data are central to enabling predictive, personalized banking services."
  - "Digitally engaged customers are 2.3 times more likely to adopt multiple financial products."
  - "Infrastructure alone does not guarantee inclusion; socio-demographic barriers persist."
```
---

## Paper 12: Compagnino et al_summarized.md

**Source File:** `Compagnino et al_summarized.md`

```yaml
paper_id: 10.3390/app152111787
designation: international
title: An Introduction to Machine Learning Methods for Fraud Detection
authors: Compagnino, A.A.; Maruccia, Y.; Cavuoti, S.; Riccio, G.; Tutone, A.; Crupi, R.; Pagliaro, A.
year: 2025
venue: Applied Sciences
odin_topics:
  - 8.A
  - 8.B
  - 8.C
  - 6.A
  - 6.B
  - 10.A
  - 10.B
  - 1.A
tldr: A systematic review of machine learning techniques for financial fraud detection, analyzing supervised, unsupervised, and deep learning approaches with case studies on real-world banking data.
problem_and_motivation: Financial fraud causes substantial economic damage and traditional detection methods are increasingly inadequate against evolving sophisticated schemes. A significant gap exists between academic research on ML-based fraud detection and its practical, operational application in real-world financial environments.
approach:
  - A systematic literature review was conducted across Scopus, IEEE Xplore, ACM Digital Library, and Web of Science.
  - The review synthesizes findings from over 120 peer-reviewed articles published between January 2014 and December 2023.
  - The paper categorizes financial fraud types, reviews ML approaches, and examines commonly used datasets and performance metrics.
  - Two case studies apply supervised models (Random Forest, XGBoost, ExtraTrees) to proprietary real-world banking datasets.
  - The experimental setup includes temporal splits, stratified k-fold cross-validation, and hyperparameter tuning via randomized search.
findings:
  - Supervised learning is the predominant approach, accounting for 57% of techniques employed in the reviewed literature.
  - Random Forest emerges as the most widely adopted technique, appearing in 34 studies with accuracy rates often exceeding 95%.
  - num: The case study on bank transfers achieved a fraud recall of only 0.36 on a test set with 3.39% fraud prevalence, even with class weights.
  - num: In the first case study, Random Forest achieved an AUPRC of 0.619 but a fraud recall of only 0.34 at the default threshold.
  - Extreme class imbalance is a fundamental challenge, with fraudulent transactions typically less than 1% of all transactions.
  - The study confirms that standard supervised models, even with hyperparameter tuning, are often insufficient for robust operational fraud detection.
key_figures_tables:
  - Table 1: Comparative analysis of ML approaches → Summarizes algorithm advantages, disadvantages, complexity, and interpretability.
  - Table 2: SOTA micro-benchmark on ULB 2013 → Shows XGBoost and RF lead AUPRC on a standard dataset.
  - Table 3: Summary of banking dataset characteristics → Shows 48,559 instances with ~1.43% fraud rate.
  - Table 4: Case Study 1 results → Shows Random Forest achieves best AUPRC of 0.619 and Recall@0.5% of 0.202.
  - Table 5: Case Study 2 results → Shows class_weight adjustments did not improve fraud recall significantly.
  - Figure 1: PR curve for Random Forest in Case Study 1 → Average precision (AUPRC) is 0.619.
  - Figure 2: PR curve for Random Forest in Case Study 2 → Average precision (AUPRC) is 0.697.
key_equations:
  - equation: "Accuracy = (TP + TN) / (TP + TN + FP + FN)"
    explanation: Measures overall correct predictions but is misleading for imbalanced data.
  - equation: "Precision = TP / (TP + FP)"
    explanation: Measures the proportion of flagged transactions that are actually fraudulent.
  - equation: "Recall = TP / (TP + FN)"
    explanation: Measures the proportion of actual frauds that are correctly detected.
  - equation: "F1-Score = (2 * Precision * Recall) / (Precision + Recall)"
    explanation: Harmonic mean balancing precision and recall, useful for imbalanced data.
  - equation: "AUC-ROC = ∫ TPR(FPR^-1(t)) dt"
    explanation: Evaluates model's discrimination ability across different thresholds.
  - equation: "OutputSize = floor((InputSize + 2*Padding - KernelSize) / Stride) + 1"
    explanation: Formula for calculating output dimensions after a convolution operation.
definitions:
  - term: XAI
    definition: Explainable Artificial Intelligence, methods for making model decisions transparent.
  - term: Concept Drift
    definition: The change in the relationship between features and target variable over time.
  - term: Federated Learning
    definition: Training a shared model across decentralized data sources without raw data exchange.
  - term: SMOTE
    definition: Synthetic Minority Over-sampling Technique to balance imbalanced datasets.
  - term: GAN
    definition: Generative Adversarial Network, two competing neural networks for generating synthetic data.
  - term: AUPRC
    definition: Area Under the Precision-Recall Curve, a metric for imbalanced classification.
  - term: SHAP
    definition: SHapley Additive exPlanations, a method for explaining model predictions.
critical_citations:
  - "[Dal Pozzolo et al., 2022] — Provides key lessons on concept drift and calibration in fraud detection."
  - "[Ahmed et al., 2016] — Foundational survey on anomaly detection techniques in the financial domain."
  - "[Saito and Rehmsmeier, 2015] — Establishes AUPRC as more informative than ROC for imbalanced data."
  - "[Lucas et al., 2020] — Covers automated feature engineering challenges for credit card fraud detection."
  - "[Fiore et al., 2019] — Demonstrates use of GANs for improving classification effectiveness in fraud detection."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly addresses anomaly detection for identifying fraudulent financial transactions.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Reviews and benchmarks specific algorithms like Isolation Forest and autoencoders.
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: medium
      justification: Discusses unsupervised methods like autoencoders that are relevant for cold-start scenarios.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Provides context on forecasting challenges due to concept drift and temporal data.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: Reviews LSTM and RNNs for sequential transaction data, applicable to spending forecasting.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Discusses federated learning and privacy concerns with centralized sensitive data.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: Mentions explainability and bias as trust factors but not as a primary focus.
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Provides general fraud detection context; no specific focus on Filipino demography.
  contribution: This review provides a comprehensive catalog of ML techniques for fraud detection, including a systematic performance comparison on standard datasets and a detailed evaluation of supervised models on proprietary banking data. The paper's analysis of concept drift and data imbalance is directly applicable to Odin's spending forecasting and anomaly detection modules. The case studies offer practical insights into model limitations, particularly the low recall challenge, which informs Odin's need for robust anomaly handling. The discussion on federated learning and XAI provides actionable guidance for Odin's data privacy and user trust design considerations.
  directly_justifies:
    - "Fraudulent transactions typically constitute less than 1% of all transactions, making it exceptionally difficult for models to learn discriminative features."
    - "Extreme class imbalance requires specialized techniques like SMOTE or cost-sensitive learning."
    - "Concept drift renders models trained on historical data obsolete as fraudsters continuously evolve tactics."
    - "Explainability is not just desirable but a critical compliance requirement for financial systems."
  limits:
    - "The case studies use proprietary banking data, limiting replicability and generalizability."
    - "The paper primarily reviews tree-based and traditional ML models, with less depth on graph-based or hybrid approaches."
    - "The systematic review excludes studies from 2024 and 2025."
    - "The paper does not address region-specific cultural or financial behaviors."
    - "The evaluation focuses on fraud detection, not personal finance management or budgeting."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The domain most directly relevant is Anomaly Detection, with topic codes 8.A, 8.B, and 8.C flagged as high relevance due to the paper's core focus on identifying fraudulent transactions. Predictive Modeling (6.A, 6.B) was flagged as medium relevance because the paper's discussion of temporal data and sequential models (LSTM, RNN) is directly applicable to spending forecasting. Data Privacy (10.A, 10.B) was assigned medium relevance due to substantial sections on federated learning and explainability. Filipino Cultural Context (2.A-D) and Behavioral Profiling (5.A-C) were rejected as the paper does not address cultural behaviors or user profiling. The topic 1.A (Demographic) was considered contextual only. Borderline cases included the overlap between anomaly detection and predictive modeling, resolved by classifying algorithm-specific discussions under 8.B and forecasting-specific challenges under 6.B.
limitations:
  - "The use of PCA-transformed features in many public datasets obscures interpretability and limits domain knowledge integration."
  - "Most studies report high accuracy but fail to address the critical operational trade-off between precision and recall."
  - "The adversarial nature of fraud is under-addressed; models are not evaluated against adaptive fraudsters."
  - "The case studies demonstrate that standard class_weight adjustments are insufficient for extreme imbalance."
  - "The field lacks standardized benchmarks and recent publicly accessible fraud datasets. [unacknowledged]"
remember_this:
  - "Random Forest models achieve high accuracy but low recall on imbalanced fraud data."
  - "Class weight adjustments alone do not solve the extreme class imbalance problem."
  - "Model interpretability is a legal and operational requirement in financial systems."
  - "Federated learning enables cross-institutional collaboration without sharing sensitive data."
  - "Concept drift requires adaptive models that can detect evolving fraud patterns in real-time."
```
---

## Paper 13: Chishti_summarized.md

**Source File:** `Chishti_summarized.md`

```yaml
paper_id: "10.15662/IJEETR.2025.0704003"
designation: "international"
title: "Hybrid Deep Learning Architectures for Time-Series Forecasting"
authors: "Chishti, S."
year: 2025
venue: "International Journal of Engineering & Extended Technologies Research (IJEETR)"
odin_topics:
  - "6.A"
  - "6.B"
tldr: "Hybrid deep learning models combining CNNs, RNNs, transformers, and GNNs improve time-series forecasting accuracy by capturing complex temporal and spatial dependencies."
problem_and_motivation: "Traditional statistical models and standalone deep learning architectures are insufficient for capturing complex non-linear and long-range dependencies in time-series data. Hybrid models that combine complementary strengths are needed to overcome these limitations and enhance predictive performance. This survey reviews the latest hybrid architectures and their effectiveness across multiple domains."
approach:
  - "Systematic literature review of peer-reviewed articles published from January to August 2024."
  - "Searched IEEE Xplore, ACM Digital Library, SpringerLink, and Google Scholar using keywords including hybrid deep learning and time-series forecasting."
  - "Included only studies with empirical validation on benchmark datasets and novel hybrid model designs."
  - "Categorized architectures into CNN-RNN hybrids, transformer-based hybrids, and GNN-integrated hybrids."
  - "Compared performance using RMSE, MAE, and MAPE against standalone models."
  - "Also assessed model interpretability, computational complexity, and emerging trends like federated learning."
findings:
  - "num: CNN-RNN hybrids improve RMSE by 5-15% on energy load forecasting datasets."
  - "num: GNN-CNN-LSTM hybrid achieves up to 12% accuracy improvement in traffic flow prediction."
  - "Multi-Scale Hybrid Transformer achieves state-of-the-art results on financial and weather forecasting."
  - "Hybrid models outperform single-architecture deep learning and traditional statistical models."
  - "Attention mechanisms provide some interpretability but overall model transparency remains limited."
  - "Federated learning shows promise for privacy-preserving forecasting but faces communication overhead."
key_figures_tables:
  - "None."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "RNN"
    definition: "Recurrent neural network, designed for sequential data."
  - term: "CNN"
    definition: "Convolutional neural network, extracts local patterns."
  - term: "LSTM"
    definition: "Long short-term memory, a type of RNN with gated cells."
  - term: "GRU"
    definition: "Gated recurrent unit, a simplified RNN variant."
  - term: "GNN"
    definition: "Graph neural network, models spatial dependencies."
  - term: "Transformer"
    definition: "Architecture based on self-attention for long-range dependencies."
critical_citations:
  - "[Zhou et al., 2024] — CNN-LSTM hybrid for energy forecasting."
  - "[Li et al., 2024] — Multi-Scale Hybrid Transformer for finance."
  - "[Xu and Zhang, 2024] — GNN-CNN-LSTM for traffic forecasting."
  - "[Patel and Kumar, 2024] — Federated learning for hybrid models."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "The paper reviews state-of-the-art forecasting architectures directly applicable to spending prediction."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "The survey covers hybrid models that combine CNNs, RNNs, and transformers, which are suitable for sequential spending data."
  contribution: "This paper provides a comprehensive survey of hybrid deep learning architectures that can inform the design of Odin's spending forecasting module. The comparison of CNN-RNN, transformer-based, and GNN-integrated models offers guidance on selecting appropriate algorithms for capturing both short-term and long-term spending patterns. The discussion of computational trade-offs and interpretability helps prioritize models suitable for a mobile-first personal finance system. The survey also highlights emerging federated learning techniques that could address data privacy concerns in Odin. Overall, this review serves as a foundational reference for implementing robust forecasting capabilities."
  directly_justifies:
    - "Hybrid CNN-RNN models improve RMSE by 5-15% over standalone models."
    - "Multi-scale hybrid transformers achieve state-of-the-art performance on financial time-series."
    - "GNN integration captures spatial correlations in multi-variate forecasting."
    - "Federated learning enables privacy-preserving training on decentralized data."
  limits:
    - "The review does not evaluate models on personal finance spending data."
    - "It does not address cold-start problems common in new user scenarios."
    - "Computational requirements may be prohibitive for mobile deployment."
    - "Interpretability techniques are only briefly mentioned."
  mapping_rationale: "All 12 functional domains were systematically scanned. The paper was found most relevant to Spending Forecasting (domains 6.A and 6.B) due to its focus on time-series forecasting algorithms, with high relevance assigned because Odin's core prediction module directly relies on such techniques. Other domains such as Anomaly Detection (8.A, 8.B) were considered but rejected as the paper does not explicitly address anomaly detection tasks. Data Privacy (10.A) was noted as contextual because federated learning is mentioned, but the paper does not provide actionable insights for Odin's privacy design. System Evaluation (12.A) was also considered but deemed low because the paper does not propose an evaluation framework for personal finance systems. Overall, the paper's primary contribution is to inform the algorithmic choices for Odin's forecasting engine, making 6.A and 6.B the only highly relevant topics."
limitations:
  - "The review is limited to publications from January to August 2024, potentially missing earlier or later developments."
  - "It does not provide a unified empirical comparison across all hybrid models."
  - "Focuses on general time-series, not tailored to financial or personal spending data."
  - "Model interpretability and computational efficiency are discussed qualitatively without concrete benchmarks."
remember_this:
  - "Hybrid CNN-RNN models improve RMSE by 5-15% over single architectures."
  - "Multi-scale transformers achieve state-of-the-art on financial forecasting."
  - "GNN integration boosts accuracy up to 12% in spatial-temporal tasks."
  - "Federated learning addresses privacy but adds communication overhead."
```
---

## Paper 14: Majumder_summarized.md

**Source File:** `Majumder_summarized.md`

```yaml
paper_id: 10.48175/IJARSCT-25619
designation: international
title: A Review of Anomaly Identification in Finance Frauds Using Machine Learning Systems
authors: Majumder, R. Q.
year: 2025
venue: International Journal of Advanced Research in Science, Communication and Technology
odin_topics:
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
  - 5.A
  - 5.C
tldr: A review of machine learning methods for financial fraud detection, covering supervised, unsupervised, and graph-based techniques, with a focus on challenges like imbalanced data and adversarial attacks.
problem_and_motivation: Financial fraud has increased significantly with digital payments, undermining institutional integrity and causing economic losses. Traditional fraud detection methods are not adaptable to contemporary dishonest methods. There is a need for robust, transparent, and privacy-preserving machine learning systems for anomaly identification.
approach:
  - This is a review paper that surveys machine learning methodologies for anomaly detection in finance.
  - It categorizes techniques into supervised, semi-supervised, and unsupervised learning approaches.
  - The review examines specific algorithms including Logistic Regression, Support Vector Machines, Decision Trees, Random Forest, K-Nearest Neighbors, and Graph Neural Networks.
  - It evaluates challenges associated with imbalanced data distributions, adversarial attacks, and real-time processing.
  - The study also explores future directions such as Explainable AI, continuous learning, and hybrid models.
findings:
  - num: The paper references a study that trained an anomaly detection model on over 12 million financial records.
  - Machine learning enables faster and more efficient detection of fraudulent patterns compared to manual review.
  - Graph Neural Networks show superior performance in capturing complex relationships in financial transactions for fraud detection.
  - Key challenges include imbalanced datasets, adversarial fraudulent activities, and scalability for real-time processing.
key_figures_tables:
  - Figure 1: Classification of anomaly detection techniques (Supervised, Semi-supervised, Unsupervised) → Provides a taxonomy for selecting appropriate methods.
  - Figure 3: Overview of common machine learning models for fraud detection → Lists standard algorithms used in the field.
  - Table 1: Summary of recent studies on anomaly detection in financial fraud → Offers a structured comparison of approaches, findings, and future directions.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: XAI
    definition: Explainable Artificial Intelligence; aims to make AI model decisions transparent and understandable.
critical_citations:
  - "[Ashtiani and Raahemi, 2022] — Systematic literature review on intelligent fraud detection."
  - "[Al-Hashedi and Magalingam, 2021] — Comprehensive review of data mining for financial fraud."
  - "[Pourhabibi et al., 2020] — Systematic literature review of graph-based anomaly detection."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Core focus of the paper is on anomaly detection techniques for financial fraud.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: The paper reviews various algorithms (e.g., Isolation Forest, Autoencoders, GNNs) applicable to spending data.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Discusses privacy preservation as a future direction for fraud detection systems.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Highlights the importance of transparency (XAI) to foster trust among users and regulators.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides an overview of challenges (e.g., imbalanced data) that impact evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Reviews performance of different ML algorithms (LR, SVM, RF, GNN) in fraud detection contexts.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: Anomaly detection is used to identify deviant behavior, which is foundational for profiling.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: contextual
      justification: Discusses classification techniques (e.g., logistic regression) that can be used for behavioral classification.
  contribution: This review paper supports Odin's anomaly detection module by providing a comprehensive overview of applicable machine learning techniques (8.B). It identifies key challenges like imbalanced data and adversarial attacks, informing the design of robust detection algorithms. The discussion of Explainable AI (10.B) is relevant for building user trust in Odin's alerts. The review's analysis of real-time processing requirements is critical for Odin's mobile-first design.
  directly_justifies:
    - "Machine learning enables faster detection of anomalous financial patterns than manual review."
    - "Graph Neural Networks are effective for capturing complex relationships in transactional data."
    - "Addressing imbalanced datasets is crucial for improving fraud detection model performance."
  limits:
    - None identified.
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The most direct relevance is to the "Anomaly Detection" domain, where topics 8.A and 8.B are assigned `high` relevance because the paper is centered on reviewing algorithms and techniques for this purpose. Topic 8.C is also indirectly supported. The domain "Data Privacy & User Trust" (10.A, 10.B) is marked `medium` as the paper touches on privacy-preserving methods and the need for transparent AI, which is key for building user trust in systems like Odin. Similarly, "System Evaluation" (12.A, 12.B) is `medium` because the review discusses challenges that affect evaluation. Topics like 5.A and 5.C are only `contextual` as the paper discusses behavioral patterns in the context of fraud, not personal finance profiling per se. Domains such as "Budget Recommendation," "Spending Forecasting," and "Filipino Cultural Context" were considered and rejected because the paper does not address savings, budgeting, forecasting, or culturally specific financial practices. The paper is internationally focused and provides foundational knowledge for implementing a robust anomaly detection module within Odin.
limitations:
  - None.
remember_this:
  - Supervised, unsupervised, and graph-based learning are key approaches for financial anomaly detection.
  - Data imbalance remains a major challenge for training effective fraud detection models.
  - Future systems will integrate real-time analysis with Explainable AI for greater transparency.
  - num: One cited study trained an anomaly detection model on over 12 million records.
  - Graph Neural Networks are particularly effective for detecting fraud in linked transaction networks.
```
---

## Paper 15: Ramos-2024b_summarized.md

**Source File:** `Ramos-2024b_summarized.md`

```yaml
paper_id: 5c9b8b1e-3a6b-4e8b-9a7c-4d6f2a8b9c7e
designation: international
title: Essays on the Causes and Demographic Consequences of Employment Uncertainty
authors: Ramos, V. J. R.
year: 2024
venue: Hertie School
odin_topics:
  - 1.A
  - 1.C
  - 2.A
  - 2.B
  - 2.C
  - 2.D
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 13.C
tldr: Employment uncertainty is a multi-dimensional phenomenon that is both caused by economic shocks and state policies, and a key determinant of fertility behavior and intentions across different life course stages.
problem_and_motivation: Existing research lacks a unified framework to conceptualize the multifaceted nature of employment uncertainty, and its role as both a determined outcome of crises and a determinant of demographic behavior. This dissertation addresses this gap by systematically expanding the typology of employment uncertainty and empirically demonstrating its causes and consequences on fertility in different country contexts.
approach:
  - Analyzes the gendered informalization of employment in the Philippines due to extreme COVID-19 lockdowns using a difference-in-differences design on pooled Labor Force Surveys.
  - Investigates the persistent effects of initial employment conditions on fertility in Germany using a two-step identification strategy combining optimal full matching and event history modeling on the German Socio-Economic Panel.
  - Examines the relationship between social class, economic uncertainty, and second-birth fertility in Germany using piecewise constant and cure fraction event history models.
  - Assesses the causal impact of future caregiving responsibilities and employment uncertainties on ascribed fertility intentions in Germany using a factorial survey experiment fielded in the SOEP Innovation Sample.
findings:
  - num: Extreme lockdowns in the Philippines increased the probability of informal employment by 1.7 percentage points for all workers, but the effect was significant and larger (2.2 pp) only for women.
  - num: Female labor market entrants with a fixed-term contract have a 19% lower first-birth hazard within the first decade of entry compared to permanent entrants.
  - num: Male labor market entrants during a recession have a 23% lower first-birth hazard within the first decade of entry compared to non-recession entrants.
  - num: Men and women in the upper service class have elevated second birth rates, with semi-/unskilled workers having 42% (men) and 36% (women) lower rates compared to the upper service class.
  - num: The absence of future caregiving responsibilities and employment uncertainty increases ascribed fertility intentions by 2.8 and 1.9 units (on a 0-10 scale), respectively.
key_figures_tables:
  - Figure 1.1: Global unemployment trends show pronounced cyclicality in high-income economies, spiking during the 2008 financial crisis and COVID-19 pandemic.
  - Figure 1.4: Global total fertility rates have declined remarkably over the past 60 years, with low-income countries showing the steepest recent decreases.
  - Table 1.2: Fixed effects regressions show a robust negative association between lagged unemployment rates and total fertility rates across 187 countries.
  - Figure 3.1: Fixed-term labor market entry has a persistent negative effect on first-birth probabilities, reaching up to a 5 pp reduction within 10 years post-entry.
key_equations:
  - equation: F_{c,t} = α + γ U_{c,t-1} + δD_{c,t-1} + ωM_{c,t-1} + θZ_{c,t} + ε_{c,t}
    explanation: Models country-level fertility as a function of lagged unemployment and controls.
  - equation: h_p(t) = h_0(t)exp(β_p X_p + β_q X_q)
    explanation: Cox proportional hazards model for first birth hazard after labor market entry.
  - equation: h(t|X) = h_0(t) × exp(βx)
    explanation: Piecewise constant hazard model for transition to second birth.
definitions:
  - term: Employment Uncertainty
    definition: An umbrella term for labor market positions characterized by imperfect, incomplete, or unknown information regarding job security, duration, or conditions.
  - term: Survivalist Motive
    definition: The strategy of engaging in informal work out of necessity during economic downturns to avoid unemployment, due to a lack of social safety nets.
  - term: Ascribed Fertility Intentions
    definition: The likelihood a respondent assigns to a hypothetical couple having a child, as measured in a vignette experiment.
critical_citations:
  - "[Blossfeld et al., 2006] — Provides foundational schema for employment uncertainty dimensions."
  - "[Vignoli et al., 2020a] — Introduces the Narrative Framework for future-oriented fertility decisions."
  - "[Alderotti et al., 2021] — Meta-analysis showing negative effects of employment instability on fertility."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Chapter 2 focuses specifically on the Philippine labor market and its young workforce.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Analyzes informalization of employment which is a key aspect of financial behavior.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Analyzes Filipino household coping mechanisms during the pandemic.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: The business cycle is a key determinant of employment uncertainty and fertility.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: medium
      justification: The dissertation analyzes Filipino employment patterns during COVID-19 lockdowns.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Provides a global context but does not directly survey PFMS.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: low
      justification: Implicitly discusses gaps in social protection systems in the Philippines.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Class-based profiles are a central operationalization of employment uncertainty.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: Discusses effects of initial employment conditions, analogous to cold-start.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses EGP class schema to classify occupational profiles.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: Does not use forecasting algorithms, but discusses predictive factors of fertility.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: The survivalist motive discusses household coping strategies, which could inform budgeting.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Does not directly discuss budget recommendations.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: The dissertation does not address anomaly detection.
    - code: 9.A
      name: Mobile‑First Design Principles and Rationale
      relevance: low
      justification: Does not directly address mobile design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Does not address data privacy.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: Does not address user trust.
    - code: 13.C
      name: End‑of‑Period Surplus as a Savings Input
      relevance: contextual
      justification: The survivalist motive and lack of savings are key mechanisms discussed.
  contribution: The dissertation provides a comprehensive framework for understanding the multi-dimensional nature of employment uncertainty and its causal role in fertility decisions. Findings on the Philippine informalization and gendered labor market shocks can inform Odin's design for expense categorization and behavioral profiling of Filipino users. The analysis of future-oriented uncertainties directly justifies the importance of incorporating predictive and scenario-based features in a PFMS to enhance user retention and engagement.
  directly_justifies:
    - "Extreme lockdowns increase informal employment for women, particularly mothers."
    - "Female fixed-term entrants have a 19% lower first-birth hazard."
    - "Male recession entrants have a 23% lower first-birth hazard."
    - "Service class occupations are associated with elevated second birth rates."
    - "Future caregiving and employment uncertainties lower fertility intentions."
  limits:
    - "Context-specific findings in Germany and the Philippines may not generalize."
    - "Limited discussion on underlying mechanisms in Chapter 3."
    - "Operationalization of variables may benefit from fine-tuning or alternative measures."
  mapping_rationale: A systematic scan across all 12 functional domains and their canonical topic codes was conducted. Domains with high relevance included Filipino Cultural Context (2.A, 2.B, 2.D) due to the focus on Philippine labor market dynamics, and Behavioral Profiling & Classification (5.A, 5.C) through the use of class-based and profile-based analyses. Borderline cases were encountered for topics like 5.B (Profile Dynamics) and 7.A (Budgeting Strategies), where the dissertation's discussion of initial conditions and survivalist motives provides contextual relevance but not direct actionable insights. Domains like Mobile-First Design (9.A, 9.B), Data Privacy (10.A, 10.B), and Anomaly Detection (8.A) were rejected as the dissertation does not address them. Overall, the dissertation offers high relevance for understanding the determinants and consequences of employment uncertainty, which is foundational for designing a PFMS like Odin for Filipino young professionals.
limitations:
  - "Context-specific estimates in Germany and the Philippines may not be generalizable."
  - "Limited discussion of underlying mechanisms in Chapter 3 due to sample size."
  - "The operationalization of some variables might benefit from fine-tuning."
  - "Chapter 5's outcome is ascribed intentions, not actual behavior."
remember_this:
  - "Employment uncertainty is multi-dimensional and context-dependent."
  - "Lockdowns informalized women's employment in the Philippines."
  - "Initial fixed-term employment reduces female fertility in Germany."
  - "Recession entry lowers male fertility in Germany."
  - "Future uncertainties and caregiving reduce fertility intentions by up to 2.8 points."
```
---

## Paper 16: Nie et al_summarized.md

**Source File:** `Nie et al_summarized.md`

```yaml
paper_id: 10.48550/arXiv.2406.13478
designation: international
title: A Survey of Large Language Models for Financial Applications: Progress, Prospects and Challenges
authors: Nie, Y.; Kong, Y.; Dong, X.; Mulvey, J. M.; Poor, H. V.; Wen, Q.; Zohren, S.
year: 2024
venue: arXiv preprint
odin_topics:
  - "5.B"
  - "6.A"
  - "6.B"
  - "7.B"
  - "8.B"
  - "9.A"
  - "10.A"
  - "11.A"
  - "12.A"
tldr: This survey reviews the application of large language models across financial tasks, summarizing models, datasets, and benchmarks, while highlighting practical challenges for deployment.
problem_and_motivation: While existing surveys cover financial LLMs, they often lack a deep dive into domain-specific practical challenges, such as lookahead bias, legal concerns, and data pollution. This survey aims to bridge the gap between academic research and real-world implementation, providing a holistic view for both researchers and practitioners.
approach:
  - Categorizes financial LLM applications into linguistic tasks, sentiment analysis, time series analysis, financial reasoning, and agent-based modeling.
  - Reviews specialized financial LLMs like BloombergGPT, FinBERT, FinGPT, and InvestLM, discussing their architectures and training strategies.
  - Provides a comprehensive collection of datasets, benchmarks, and code resources for financial NLP research.
  - Analyzes challenges including data issues, modeling limitations, benchmarking difficulties, and ethical concerns.
  - Discusses future opportunities like hybrid inference for cost-efficiency and mitigation of lookahead bias with point-in-time models.
findings:
  - "num: Fine-tuned LLMs like FinBERT show enhanced resilience against adversarial attacks compared to traditional keyword-based sentiment methods."
  - "LLMs demonstrate significant potential in zero-shot financial sentiment analysis, with GPT-4 outperforming BERT on news headline classification for stock return prediction."
  - "The application of LLMs for direct time series forecasting remains debated, with some studies showing underperformance compared to traditional ML models in zero-shot settings."
  - "Agent-based models using LLMs can effectively simulate market behaviors and economic activities, producing realistic trading and investment strategies."
  - "Instruction-tuned models, such as PIXIU's FinMA, provide a robust framework for multi-task financial NLP evaluation."
key_figures_tables:
  - "Table 1: Comparison of surveys → This survey uniquely provides comprehensive coverage of models, benchmarks, applications, and challenges."
  - "Figure 2: Overview of financial LLMs from 2019 → Visualizes the evolution and categorization of specialized financial language models."
  - "Figure 4: Sentiment analysis papers by data source → Categorizes LLM applications in sentiment analysis across diverse financial texts."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "LLM"
    definition: "Large Language Model, a deep learning model pre-trained on vast text data for language understanding and generation."
  - term: "RAG"
    definition: "Retrieval-Augmented Generation, a technique for enhancing LLMs by retrieving external information."
  - term: "NER"
    definition: "Named Entity Recognition, a task to identify and classify key entities in text."
  - term: "ABM"
    definition: "Agent-Based Modeling, a simulation technique using autonomous agents to model complex systems."
  - term: "FSA"
    definition: "Financial Sentiment Analysis, the task of quantifying sentiment from financial texts."
critical_citations:
  - "[Wu et al., 2023] — Introduces BloombergGPT, a key financial LLM trained on proprietary data."
  - "[Yang et al., 2023] — Introduces FinGPT, highlighting open-source accessibility for financial modeling."
  - "[Xie et al., 2023] — Introduces PIXIU, a comprehensive benchmark and model framework for financial LLMs."
  - "[Kim et al., 2024] — Demonstrates LLMs outperforming human analysts on financial statement analysis."
relevance:
  topics:
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "contextual"
      justification: "Discusses zero-shot capabilities and domain adaptation challenges relevant to new user profiles."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Reviews LLM-based forecasting techniques for financial time series."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Examines algorithms for market trend forecasting and return prediction."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Explores LLMs for financial planning and investment recommendation."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "medium"
      justification: "Covers anomaly detection methods in financial time series."
    - code: "9.A"
      name: "Mobile‑First Design Principles and Rationale"
      relevance: "contextual"
      justification: "Discusses accessibility and user engagement via conversational AI."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "Addresses data privacy concerns and legal responsibility in financial AI."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "contextual"
      justification: "Touches on user trust and the need for interpretability."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Provides a comprehensive survey of benchmarks (FLUE, PIXIU) for financial NLP."
  contribution: "This survey justifies Odin's adoption of instruction-tuned models for multi-task personal financial analysis, supports the use of RAG for enriching contextual data, and provides evidence for integrating sentiment analysis to forecast spending behaviors. It highlights the need for specific evaluation benchmarks like FLARE for Odin's module assessment, and informs Odin's design decisions regarding handling data privacy and mitigating lookahead bias."
  directly_justifies:
    - "Instruction-tuned models demonstrate superior financial sentiment analysis and numerical reasoning."
    - "Agent-based modeling with LLMs can simulate complex financial decision-making processes."
    - "Benchmarks like FLUE and PIXIU provide standardized frameworks for evaluating financial NLP tasks."
    - "Implementing hybrid inference can reduce computational costs significantly without losing performance."
    - "Mitigating lookahead bias requires point-in-time training datasets."
  limits:
    - "This survey is a review and does not provide an empirical evaluation of proposed models in a live environment."
    - "The paper primarily focuses on high-level financial tasks and may not address the specific constraints of a personal finance management system for Filipino users."
  mapping_rationale: "The systematic scan of all 12 functional domains identified several relevant areas for Odin. For Predictive Modeling (6.A/B), the survey's extensive review of forecasting algorithms provides high relevance, justifying Odin's potential use of LLMs for spending prediction. Similarly, for Evaluation Frameworks (12.A), the detailed examination of benchmarks like FLUE and PIXIU is highly relevant for designing Odin's module testing. For Anomaly Detection (8.B) and Budget Recommendation (7.B), the review offers medium relevance, providing contextual examples of how LLMs can be applied in these areas. Domains like Data Privacy (10.A) are highly relevant due to the detailed discussion of legal and ethical challenges. Topics related to specific Filipino cultural context (2.A-D) were considered but not found, as the survey is general. The overall relevance of the paper to Odin is high, as it provides a foundational understanding of the capabilities and pitfalls of financial LLMs, guiding design choices and justifying the technology's integration into the system."
limitations:
  - "The authors note challenges with inference speed and cost for real-time deployment."
  - "The paper acknowledges the risk of hallucinations and inaccurate outputs in financial documents."
  - "Lookahead bias in backtesting is identified as a significant challenge requiring mitigation strategies."
  - "Ethical issues like incentive alignment and legal responsibility are discussed but lack concrete solutions."
  - "The review may not cover the latest advancements in the rapidly evolving field of LLMs [unacknowledged]."
remember_this:
  - "Fine-tuning LLMs on financial corpora significantly improves sentiment analysis over general models."
  - "Agent-based models can simulate complex market behaviors using LLM-driven decisions."
  - "Instruction tuning enhances LLM performance for specialized financial tasks."
  - "Benchmarking financial LLMs requires multi-task datasets like PIXIU to ensure robust evaluation."
  - "Data pollution and hallucinations remain key risks when deploying LLMs in finance."
```
---

## Paper 17: Mienye et al-2024_summarized.md

**Source File:** `Mienye et al-2024_summarized.md`

```yaml
paper_id: 1b9f8a2c-7d3e-5b2a-9c4d-8e6f1a3b7c5d
designation: international
title: "Recurrent Neural Networks: A Comprehensive Review of Architectures, Variants, and Applications"
authors: "Mienye, I. D.; Swart, T. G.; Obaido, G."
year: 2024
venue: "Information"
odin_topics:
  - "6.A"
  - "6.B"
  - "8.A"
  - "8.B"
  - "5.C"
  - "7.B"
  - "7.A"
  - "9.A"
  - "10.A"
  - "12.A"
tldr: "This review comprehensively surveys RNN architectures, variants, and applications, highlighting their role in modeling sequential data for domains relevant to personal finance systems."
problem_and_motivation: "RNNs are powerful for sequential data, but a comprehensive, up-to-date review covering recent architectural innovations and broad applications is lacking. This gap hinders researchers from effectively leveraging the latest RNN advancements across diverse fields."
approach:
  - "This paper is a comprehensive literature review of RNNs, covering fundamental architectures, advanced variants, and innovations."
  - "It systematically categorizes RNN types including LSTM, GRU, BiLSTM, ESNs, and IndRNN, detailing their mechanisms and equations."
  - "The review surveys applications across diverse domains such as NLP, speech recognition, time series forecasting, and anomaly detection."
  - "It discusses recent innovations like hybrid CNN-RNN models, attention mechanisms, and transformer integrations."
  - "The paper also covers training challenges, optimization techniques, and future research directions for RNNs."
findings:
  - "num: LSTM and GRU architectures effectively mitigate the vanishing gradient problem, enabling learning of long-term dependencies."
  - "num: Bidirectional RNNs improve performance in tasks requiring context from both past and future by processing sequences in both directions."
  - "num: Hybrid models combining CNNs and RNNs, or RNNs with attention, achieve state-of-the-art results in complex sequence tasks."
  - "RNNs have been successfully applied to time series forecasting, anomaly detection, and natural language processing, areas relevant to PFMS."
  - "Challenges including scalability, interpretability, and data dependency remain open research problems for RNNs."
key_figures_tables:
  - "Figure 1: Basic RNN architecture → Shows recurrent connections enabling sequence processing."
  - "Figure 2: LSTM cell architecture → Illustrates input, forget, and output gates for long-term memory."
  - "Figure 3: BiLSTM architecture → Depicts forward and backward processing for full context."
  - "Figure 4: Stacked LSTM → Shows hierarchical feature learning via multiple LSTM layers."
  - "Figure 5: GRU architecture → Demonstrates simplified gating with update and reset gates."
key_equations:
  - equation: "h_t = σ_h(W_xh x_t + W_hh h_{t-1} + b_h)"
    explanation: "Standard RNN hidden state update equation."
  - equation: "i_t = σ(W_xi x_t + W_hi h_{t-1} + b_i)"
    explanation: "LSTM input gate controls new information flow."
  - equation: "f_t = σ(W_xf x_t + W_hf h_{t-1} + b_f)"
    explanation: "LSTM forget gate regulates memory retention."
  - equation: "c_t = f_t ⊙ c_{t-1} + i_t ⊙ g_t"
    explanation: "LSTM cell state update combining old and new memory."
  - equation: "z_t = σ(W_xz x_t + W_hz h_{t-1} + b_z)"
    explanation: "GRU update gate balances old and new hidden states."
definitions:
  - term: "RNN"
    definition: "Recurrent Neural Network, a class of neural networks designed to process sequential data by maintaining a hidden state."
  - term: "LSTM"
    definition: "Long Short-Term Memory, an RNN variant with gating mechanisms to handle long-term dependencies."
  - term: "GRU"
    definition: "Gated Recurrent Unit, a simplified LSTM variant with fewer gates."
  - term: "BiLSTM"
    definition: "Bidirectional LSTM, processes sequences in both forward and backward directions for better context."
  - term: "ESN"
    definition: "Echo State Network, an RNN with a fixed, randomly connected reservoir and only the output layer trained."
  - term: "BPTT"
    definition: "Backpropagation Through Time, the algorithm used to train RNNs by unrolling the network through time."
  - term: "IndRNN"
    definition: "Independently Recurrent Neural Network, uses independent recurrent units to address gradient issues."
critical_citations:
  - "[Hochreiter and Schmidhuber, 1997] — Introduced LSTM to solve vanishing gradient problem."
  - "[Cho et al., 2014] — Proposed GRU as a simplified alternative to LSTM."
  - "[Vaswani et al., 2017] — Introduced Transformer architecture, impacting RNN applications."
  - "[Greff et al., 2016] — Provided extensive comparison of LSTM variants."
  - "[Bahdanau et al., 2014] — Introduced attention mechanisms for RNNs in translation."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Directly reviews time series forecasting algorithms applicable to spending prediction."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Discusses LSTM and GRU for sequential data, core to forecasting."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews anomaly detection applications using RNNs on time series data."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "medium"
      justification: "Covers BiLSTM and other models for detecting deviations in sequential data."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "contextual"
      justification: "Relevant as a background for classification using RNNs, though not PFMS-specific."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "low"
      justification: "Provides general background on RNNs but no specific budgeting strategies."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "contextual"
      justification: "Provides general context on sequential data modeling which is foundational."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "low"
      justification: "Not directly addressed; papers focuses on algorithms not UX."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "contextual"
      justification: "Discusses data dependency but not privacy specifically."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "contextual"
      justification: "Mentions evaluation but does not provide PFMS-specific frameworks."
  contribution: "This review provides a foundational understanding of RNN architectures, directly justifying the selection of LSTM and GRU for Odin's spending forecasting module. The detailed comparison of algorithms supports the design of Odin's anomaly detection system by identifying suitable sequence models. It also informs the behavioral profiling module by reviewing classification approaches for sequential data. Furthermore, the discussion of training challenges and innovations offers guidance for implementing robust forecasting and detection algorithms within Odin."
  directly_justifies:
    - "LSTM and GRU networks are well-suited for time series forecasting of spending data."
    - "Bidirectional LSTM can enhance anomaly detection by capturing context from both past and future spending patterns."
    - "Hybrid models combining CNN and RNN can be used for feature extraction and temporal modeling."
    - "Attention mechanisms can improve forecasting accuracy by focusing on relevant spending periods."
  limits:
    - "The review does not provide empirical comparisons or benchmarks specific to personal finance datasets."
    - "The discussion of user behavior and cold-start problems is limited, as it is a general review."
    - "Implementation details or specific parameter tuning for PFMS are not addressed."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. Domains related to algorithmic core functions were flagged as relevant. Specifically, 'Spending Forecasting' (6.A, 6.B) received high relevance due to the paper's extensive review of LSTM, GRU, and hybrid models for time series prediction, which are directly applicable to Odin's forecasting module. 'Anomaly Detection' (8.A, 8.B) was assessed as medium relevance because the review covers RNN applications for detecting deviations in sequential data, supporting Odin's anomaly detection feature. 'Behavioral Profiling' (5.C) was deemed contextual, as the paper reviews classification approaches for sequences but lacks PFMS-specific user profiling. 'Budget Recommendation' (7.A, 7.B) was considered low relevance as the paper does not discuss budgeting strategies or optimization constraints. Domains like 'Filipino Cultural Context', 'Expense Categorization', 'User Retention', and 'Savings & Debt Management' were considered and rejected as the paper does not address these socio-technical or PFMS-specific design aspects. The paper's overall relevance lies in providing a strong algorithmic foundation for Odin's core predictive and detection capabilities, though it lacks direct application to the Filipino context or specific PFMS design challenges."
limitations:
  - "The review does not include a systematic meta-analysis of performance metrics across studies. [unacknowledged]"
  - "It focuses on algorithmic advancements and does not deeply address user-centric issues like trust or mobile-first design."
  - "The paper is a high-level review and lacks specific implementation guidance for personal finance systems."
  - "Potential biases in RNN models and their impact on fairness are mentioned but not thoroughly explored. [unacknowledged]"
remember_this:
  - "LSTM and GRU are key RNN variants for long-term dependency modeling."
  - "Hybrid models with attention mechanisms enhance performance in sequence tasks."
  - "RNNs are effective for time series forecasting and anomaly detection in spending data."
  - "BiLSTM processes context from both past and future for improved accuracy."
  - "Challenges include scalability, interpretability, and data quality issues."
```
---

## Paper 18: Kolambe & Arora_summarized.md

**Source File:** `Kolambe & Arora_summarized.md`

```yaml
paper_id: a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d
designation: international
title: "Forecasting the Future: A Comprehensive Review of Time Series Prediction Techniques"
authors: "Kolambe, M.; Arora, S."
year: 2024
venue: "J. Electrical Systems"
odin_topics:
  - "6.A"
  - "6.B"
  - "8.A"
  - "8.B"
  - "12.A"
tldr: "Reviews time series forecasting methods from classical to deep learning and hybrid approaches, discussing challenges and evaluation metrics."
problem_and_motivation: "Accurate time series forecasting is critical across domains, yet classical methods struggle with complex patterns and non‑linearities. A comprehensive review is needed to guide researchers and practitioners in selecting appropriate methods for diverse applications and to highlight emerging trends."
approach:
  - "Categorizes forecasting techniques into classical statistical methods, machine learning, deep learning, and hybrid approaches."
  - "Surveys popular models including ARIMA, Exponential Smoothing, LSTM, GRU, Transformer, and ensemble methods."
  - "Discusses data‑related challenges (noise, missing values, non‑stationarity) and model‑related issues (overfitting, interpretability, hyperparameter tuning)."
  - "Reviews evaluation metrics such as MAE, MSE, RMSE, MAPE, bias, and coverage probability."
  - "Outlines future directions including explainable AI, probabilistic forecasting, scalability, and advanced feature engineering."
findings:
  - "num: Classical methods like ARIMA and exponential smoothing are widely used for simple trends and seasonality."
  - "num: Deep learning models, particularly LSTMs, excel at capturing long‑term dependencies in sequential data."
  - "Hybrid approaches that combine classical, ML, and DL methods often yield improved accuracy by leveraging complementary strengths."
  - "Key challenges include handling missing data, outliers, non‑stationarity, and evolving patterns over time."
  - "Evaluation metrics are essential for quantifying forecast accuracy and uncertainty, with MAE and RMSE being most common."
key_figures_tables:
  - "Table 1: Application domains and number of methods used → forecasting techniques are applied across finance, supply chain, energy, weather, healthcare, and traffic."
  - "Table 2: Methods and their characteristics → classical methods suit simple patterns; deep learning handles complex temporal dependencies; hybrids combine multiple strengths."
key_equations:
  - equation: "MAE = (1/n) * Σ|y_i - ŷ_i|"
    explanation: "Average absolute forecast error."
  - equation: "MSE = (1/n) * Σ(y_i - ŷ_i)^2"
    explanation: "Average squared error, penalizes large errors."
  - equation: "RMSE = sqrt((1/n) * Σ(y_i - ŷ_i)^2)"
    explanation: "Square root of MSE, in original units."
  - equation: "MAPE = (1/n) * Σ|(y_i - ŷ_i)/y_i| * 100"
    explanation: "Percentage average absolute error."
  - equation: "Bias = (1/n) * Σ(y_i - ŷ_i)"
    explanation: "Systematic over‑ or under‑forecasting."
definitions:
  - term: "ARIMA"
    definition: "Autoregressive Integrated Moving Average, a classical time series model for stationary data."
  - term: "LSTM"
    definition: "Long Short‑Term Memory, a type of recurrent neural network that handles long‑term dependencies."
  - term: "RNN"
    definition: "Recurrent Neural Network, a neural network for sequential data, suffers from vanishing gradients."
  - term: "GRU"
    definition: "Gated Recurrent Unit, a simpler variant of LSTM with comparable performance."
  - term: "STL"
    definition: "Seasonal‑Trend decomposition using LOESS, decomposes series into trend, seasonal, and remainder."
critical_citations:
  - "[Box & Jenkins, 1970] — foundational methodology for ARIMA modelling."
  - "[Hochreiter & Schmidhuber, 1997] — introduced LSTM for long‑range dependencies."
  - "[Vapnik, 1995] — support vector machines for regression and forecasting."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Provides comprehensive review of predictive models directly applicable to spending forecasting."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Surveys algorithms including LSTM, GRU, ARIMA, and hybrids that are central to spending forecasting."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "low"
      justification: "Mentions outliers as a challenge but does not detail anomaly detection algorithms."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "low"
      justification: "Discusses outlier detection only as a data quality issue, not as a core technique."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Devotes a section to evaluation metrics (MAE, RMSE, MAPE) that are relevant for assessing forecasting modules."
  contribution: "This review informs Odin's spending forecasting module by cataloging state‑of‑the‑art algorithms and their trade‑offs. It provides a foundation for selecting between LSTM, GRU, and hybrid models for sequential spending data. The discussion on evaluation metrics directly supports the design of performance benchmarks for Odin’s predictive components. The survey of challenges such as non‑stationarity and missing data guides data preprocessing strategies. Future directions like probabilistic forecasting and explainable AI offer pathways for enhancing Odin's transparency and uncertainty quantification."
  directly_justifies:
    - "LSTM networks outperform classical models in capturing long‑term dependencies in time series data."
    - "Hybrid models that combine ARIMA with neural networks often yield higher accuracy than either alone."
    - "Evaluation metrics such as MAE and RMSE are standard for measuring forecast error in financial applications."
  limits:
    - "The review is general and does not focus on personal finance or spending patterns specifically."
    - "No empirical comparison of methods on real‑world spending data is provided."
    - "Lacks discussion on the cold‑start problem or user‑specific profile adaptation."
  mapping_rationale: "Systematically scanned all 12 functional domains and their associated topic codes. The paper is directly relevant to Forecasting (6.A, 6.B) as it reviews predictive models and algorithms; assigned high relevance. It touches on Anomaly Detection (8.A, 8.B) only through outlier handling, so assigned low. The evaluation metrics section supports System Evaluation (12.A), assigned medium. Other domains (Filipino cultural context, expense categorization, behavioral profiling, budget recommendation, mobile design, privacy, retention) were considered but rejected because the paper does not address them. The overall relevance is moderate for Odin, providing foundational knowledge for forecasting but lacking domain‑specific insights."
limitations:
  - "The paper is a survey and does not present new empirical results. [unacknowledged]"
  - "No attention is given to personal finance or spending data characteristics. [unacknowledged]"
  - "Does not address real‑time or mobile‑specific constraints. [unacknowledged]"
remember_this:
  - "Forecasting methods evolved from ARIMA to deep learning and hybrid ensembles."
  - "LSTM and GRU effectively capture long‑term dependencies in sequential data."
  - "Hybrid approaches combining classical and ML often improve predictive accuracy."
  - "Challenges include missing data, seasonality, and model interpretability."
  - "Evaluation metrics like MAE, RMSE, and MAPE are essential for model selection."
```
---

## Paper 19: Hovakimyan & Bravo_summarized.md

**Source File:** `Hovakimyan & Bravo_summarized.md`

```yaml
paper_id: "10.3390/info15120786"
designation: "international"
title: "Evolving Strategies in Machine Learning: A Systematic Review of Concept Drift Detection"
authors: "Hovakimyan, G.; Bravo, J.M."
year: 2024
venue: "Information"
odin_topics:
  - "2.B"
  - "5.C"
  - "6.A"
  - "6.B"
  - "8.A"
  - "8.B"
  - "12.A"
  - "12.B"
tldr: "A systematic review of concept drift detection methods over two decades, categorizing them into drift detection, window-based, unsupervised, ensemble, and neural network approaches, and highlighting strengths, weaknesses, and future challenges."
problem_and_motivation: "Machine learning models often assume static data distributions, yet real-world streams exhibit concept drift that degrades accuracy. Despite numerous methods, there is no unified synthesis of their strengths and weaknesses across diverse drift types and application domains. This review systematically categorizes existing detection strategies to provide a resource for researchers and practitioners."
approach:
  - "Followed PRISMA guidelines for systematic review process and reporting."
  - "Searched IEEE and ScienceDirect APIs, identifying 490 studies, with 40 added from reference lists."
  - "Used T5 model for abstract screening to assess relevance, narrowing to 254 studies."
  - "Conducted full-text eligibility assessment and quality assessment using adapted Newcastle-Ottawa Scale and CASP checklists."
  - "Synthesized 65 high-impact studies, categorizing methods into DDM, WBM, USSM, EM, and NN categories."
findings:
  - "DDMs are cost-effective and easy to apply in real-time, but may produce false positives in noisy environments."
  - "WBMs balance accuracy and computational cost, with ADWIN being sensitive to noise but effective for sudden drift."
  - "USSMs excel in novel class detection but are computationally expensive and prone to false positives."
  - "Ensemble methods and neural networks achieve very high accuracy but incur high computational costs."
  - "num: 45% of reviewed studies are of high methodological quality, 41% moderate, and 14% low."
  - "Challenges include handling imbalanced data, computational efficiency, regression tasks, and non-tabular data."
  - "Common evaluation metrics include prequential error, detection delay, and false alarm rates."
key_figures_tables:
  - "Figure 1: Distribution-based drift types (virtual, real, novel class) → illustrates changes in data distribution and class relationships."
  - "Figure 2: Pattern-based drift types (sudden, incremental, gradual, recurrent) → shows how data distribution changes over time."
  - "Figure 3: PRISMA flow diagram → summarizes study selection stages and reasons for exclusion."
  - "Table 2: Summary of concept drift types with real-world examples → provides a taxonomy of drift types."
  - "Table 3: Characteristics of included studies (drift type, method, findings) → overview of key studies and their contributions."
  - "Table 4: Comparison of methods (accuracy, cost, applicability) → highlights trade-offs between accuracy and computational efficiency."
  - "Table 5: Summary of datasets used for concept drift detection → lists synthetic and real-world benchmark datasets."
key_equations:
  - equation: "$CR = \\frac{\\text{Total Citations}}{\\text{Years Since Publication}}$"
    explanation: "Adjusted citation rate to measure impact."
  - equation: "$p_t + s_t \\ge p_{\\min} + 2 s_{\\min}$"
    explanation: "DDM warning level for potential drift."
  - equation: "$p_t + s_t \\ge p_{\\min} + 3 s_{\\min}$"
    explanation: "DDM drift level confirming concept drift."
  - equation: "$Acc_{t+1} = \\frac{t \\times Acc_t + \\delta_{t+1}}{t+1}$"
    explanation: "Incremental prequential accuracy calculation."
definitions:
  - term: "Concept Drift"
    definition: "Change in the statistical properties of the target variable over time, degrading model performance."
  - term: "Virtual Drift"
    definition: "Changes in input feature distribution without affecting the target variable."
  - term: "Real Drift"
    definition: "Changes in the conditional probability P(Y|X), impacting model accuracy."
  - term: "Sudden Drift"
    definition: "Abrupt, instantaneous change in data distribution."
  - term: "Gradual Drift"
    definition: "Slow, continuous change over an extended period."
  - term: "Incremental Drift"
    definition: "Progressive evolution of data distribution over time."
  - term: "Recurrent Drift"
    definition: "Cyclical changes in data distribution that reappear."
  - term: "DDM"
    definition: "Drift Detection Method, monitors error rate using statistical process control."
  - term: "WBM"
    definition: "Window-Based Mechanism, uses sliding or adaptive windows to compare historical and current data."
  - term: "USSM"
    definition: "Unsupervised and Semi-Supervised Methods, detect drift via clustering or density estimation with sparse labels."
  - term: "EM"
    definition: "Ensemble Method, combines multiple models to improve detection robustness and accuracy."
  - term: "NN"
    definition: "Neural Network, uses deep learning architectures like ELM and LSTM for drift detection."
  - term: "PRISMA"
    definition: "Preferred Reporting Items for Systematic Reviews and Meta-Analyses, a guideline for systematic reviews."
  - term: "T5"
    definition: "Text-to-Text Transfer Transformer, an NLP model used for abstract screening."
  - term: "MOA"
    definition: "Massive Online Analysis, an open-source framework for data stream mining."
critical_citations:
  - "[Gama et al., 2004] — Introduced the foundational DDM algorithm."
  - "[Bifet, 2007] — Proposed ADWIN for adaptive windowing."
  - "[Brzezinski & Stefanowski, 2014] — Developed OAUE ensemble method."
  - "[Barros et al., 2018] — Conducted large-scale comparison of drift detectors."
relevance:
  topics:
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "contextual"
      justification: "Discusses recurrent drift as cyclical changes, relevant to seasonal spending."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "Reviews classification methods that handle drift, applicable to behavioral profiling."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Concept drift affects predictive models; reviews adaptive modeling techniques."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "medium"
      justification: "Reviews forecasting algorithms like LSTM and ELM for time-series with drift."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Drift detection methods are closely related to anomaly detection; surveys detection techniques."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "medium"
      justification: "Reviews algorithms like isolation forest and statistical tests for anomaly detection with drift."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses evaluation metrics such as accuracy, detection delay, and false alarm rates."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Compares methods based on accuracy, computational cost, and applicability for module evaluation."
  contribution: "The systematic review provides a comprehensive taxonomy of drift detection methods, which can guide the selection of forecasting (6.A) and anomaly detection (8.B) modules in Odin. The comparison of ensemble and neural network methods informs trade-offs between accuracy and computational cost for adaptive spending forecasting (6.B). The discussion of evaluation metrics like detection delay and false alarm rate directly supports the design of evaluation frameworks (12.A) for algorithmic modules. The identification of recurrent drift patterns (2.B) justifies incorporating seasonal adjustment in spending prediction. Overall, the review offers a methodological foundation for handling evolving user spending behaviors."
  directly_justifies:
    - "Window-based methods like ADWIN are effective for real-time drift detection."
    - "Ensemble methods provide high accuracy but are computationally expensive."
    - "Unsupervised methods are suitable for novel class detection with sparse labels."
    - "DDMs offer cost-effective real-time detection with minimal overhead."
    - "Neural networks like LSTM excel in detecting drift in sequential data."
  limits:
    - "The review focuses on classification tasks, with limited coverage of regression."
    - "Most methods are designed for tabular data; non-tabular data like images are underexplored."
    - "Computational efficiency remains a challenge for ensemble and neural methods."
    - "The review identifies a lack of standardized evaluation protocols."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was found relevant to algorithmic domains: predictive modeling (6.A, 6.B), anomaly detection (8.A, 8.B), and evaluation (12.A, 12.B), all assigned medium relevance because the paper provides methodological surveys but not finance-specific applications. The domain of Filipino cultural context (2) was considered: recurrent drift types (2.B) are mentioned as cyclical changes, providing contextual framing for seasonal spending, hence contextual. Behavioral profiling (5.C) was flagged as medium because classification under drift directly applies to user profile classification. Domains related to expense categorization (3), existing systems (4), budget recommendation (7), mobile design (9), privacy (10), retention (11), and savings/debt (13) were rejected as the paper does not address these topics. Overall, the paper's systematic review of drift detection methods is broadly relevant to Odin's adaptive algorithm modules."
limitations:
  - "The review does not address personal finance or Filipino context directly."
  - "It relies on synthetic and controlled datasets, which may not capture real-world spending complexities."
  - "The comparison of methods is qualitative rather than a quantitative meta-analysis."
  - "Some limitations like computational efficiency are acknowledged, but the review does not propose solutions."
  - "The use of T5 for screening may introduce language model biases."
remember_this:
  - "DDMs provide cost-effective real-time drift detection with minimal overhead."
  - "Ensemble and neural methods achieve high accuracy but require substantial computational resources."
  - "45% of reviewed studies are of high methodological quality."
  - "Challenges persist with imbalanced data and non-tabular data types."
  - "Recurrent drift patterns motivate handling seasonal spending changes."
```
---

## Paper 20: Harris & Austin_summarized.md

**Source File:** `Harris & Austin_summarized.md`

```yaml
paper_id: 8e5a5f2b-1a2d-59c7-a4e8-7f9b3c6d2e1a
designation: international
title: Comparative Study of Supervised and Unsupervised Machine Learning Approaches in Banking Applications
authors: Harris, F.; Austin, V.
year: 2024
venue: Unknown
odin_topics:
  - 4.A
  - 5.C
  - 6.A
  - 7.A
  - 8.A
  - 8.B
  - 12.A
tldr: Compares supervised and unsupervised machine learning for banking, highlighting supervised learning's predictive accuracy and unsupervised learning's pattern discovery capabilities.
problem_and_motivation: Banks face the challenge of extracting actionable insights from vast and complex datasets. The choice between supervised and unsupervised learning approaches is critical for optimizing operations and customer experiences but lacks a systematic comparative framework. This study addresses the need for a clear understanding of when to apply each approach in banking.
approach:
  - Provides a comprehensive literature review and comparative analysis of supervised and unsupervised machine learning.
  - Details common algorithms including regression, decision trees, SVMs, neural networks for supervised, and clustering, PCA for unsupervised.
  - Discusses specific banking applications like credit scoring, fraud detection, and customer segmentation.
  - Identifies strengths and weaknesses of each approach based on data availability and problem nature.
  - Proposes hybrid models that combine both methodologies to leverage their complementary strengths.
findings:
  - Supervised learning excels in tasks requiring predictive accuracy, such as credit scoring and fraud detection, where labeled historical data is available.
  - Unsupervised learning is valuable for exploratory analysis, pattern discovery, and tasks like market segmentation and anomaly detection without predefined labels.
  - Supervised models offer higher interpretability than unsupervised models, which is crucial for regulatory compliance.
  - The choice of approach depends on data availability, problem definition, and desired outcomes.
  - Hybrid models combining both approaches can enhance overall decision-making and predictive performance.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Supervised Learning
    definition: Machine learning with labeled data to predict outcomes.
  - term: Unsupervised Learning
    definition: Machine learning with unlabeled data to find patterns.
  - term: Clustering
    definition: Grouping data points based on similarity.
  - term: Dimensionality Reduction
    definition: Reducing number of features while preserving information.
  - term: Hybrid Models
    definition: Models combining supervised and unsupervised techniques.
critical_citations:
  - "[Carcillo et al., 2019] — Combines unsupervised and supervised learning for fraud detection."
  - "[Lessmann et al., 2015] — Benchmarks classification algorithms for credit scoring."
  - "[Bose & Mahapatra, 2020] — Surveys machine learning for financial risk management."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Provides background on ML in banking, not specific PFMS.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Discusses supervised classification for customer segmentation and credit scoring.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Covers predictive modeling techniques like regression for credit scoring.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: General discussion of ML for financial applications, not budgeting specifically.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly addresses anomaly detection for fraud using supervised and unsupervised methods.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Discusses algorithms like clustering and isolation forests for anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: low
      justification: Compares evaluation metrics but not a formal framework.
  contribution: This paper provides a foundational comparative analysis of supervised versus unsupervised learning, which is directly applicable to Odin's algorithmic modules. The discussion of supervised learning informs Odin's classification and forecasting components (e.g., for spending pattern prediction). The analysis of unsupervised learning is crucial for designing Odin's anomaly detection and user profiling systems. The paper's emphasis on hybrid models justifies a modular design in Odin where different ML techniques can be combined.
  directly_justifies:
    - "Unsupervised learning is effective for anomaly detection by identifying outliers without labels."
    - "Supervised learning requires labeled datasets for predictive modeling."
    - "Hybrid models combine both approaches to improve overall performance."
    - "Clustering algorithms group users by behavior for targeted personalization."
    - "Interpretability is a key consideration for financial models."
  limits:
    - "The study is a high-level survey and lacks implementation details for specific algorithms."
    - "The comparative analysis does not provide empirical results on banking datasets."
    - "The paper focuses on banking broadly, not on personal finance management specifically."
  mapping_rationale: A systematic scan across all 12 functional domains identified the strongest relevance to Anomaly Detection (8.A, 8.B) and Classification Approaches (5.C). The paper's broad treatment of machine learning in banking provides contextual relevance to Predictive Modeling (6.A) and the Landscape of Existing Systems (4.A), but at a low level. The topics of Budgeting Strategies (7.A) and Evaluation Frameworks (12.A) were considered but rejected due to the paper's lack of specific focus on these areas. The paper was deemed highly relevant for its foundational insights into ML techniques that can be adapted for Odin's algorithmic core, especially for anomaly detection and user classification.
limitations:
  - "The study is a high-level survey and lacks implementation details. [unacknowledged]"
  - "The comparative analysis does not provide empirical results on banking datasets. [unacknowledged]"
  - "The paper focuses on banking broadly, not on personal finance management specifically. [unacknowledged]"
remember_this:
  - "Supervised learning excels in predictive accuracy for labeled data."
  - "Unsupervised learning is valuable for discovering hidden patterns."
  - "Hybrid models combine strengths of both approaches effectively."
  - "Data availability determines the choice between supervised and unsupervised learning."
  - "Interpretability is critical for financial machine learning models."
```
---

## Paper 21: Yin_summarized.md

**Source File:** `Yin_summarized.md`

```yaml
paper_id: 10.1037/xge0001541
designation: international
title: The Impact of Categorization on Consumption Behavior
authors: Yin, S.
year: 2024
venue: Journal of Experimental Psychology: General
odin_topics:
  - "3.A"
  - "3.B"
  - "4.A"
  - "7.D"
  - "13.A"
tldr: Used accounts reduce perceived resource value via within-account comparison, increasing spending likelihood versus unused accounts with equal absolute balances.
problem_and_motivation: Consumers often spend from accounts with prior use, yet it is unclear how the used versus unused status of an account affects subsequent spending decisions independently of absolute balance. This gap matters because understanding this psychological mechanism can inform the design of financial tools and nudge consumer behavior.
approach:
  - Seven experimental studies (N = 8,667) across gift cards, checking accounts, and credit card reward points.
  - Used account conditions manipulated relative to unused accounts, holding absolute remaining resources constant.
  - Within-account comparison theory tested against alternative explanations (e.g., external reference points).
  - Continuous manipulation of remaining proportion (60%, 40%, 20%) to test moderation.
  - Mediation analysis via bootstrap (10,000 samples) to test valuation as the mechanism.
  - Incentive-compatible behavioral experiments for online shopping and donation decisions.
findings:
  - num: Used accounts increased spending likelihood by 15.82 points on a 0-100 scale versus unused accounts without a reference point (Study 1).
  - num: Valuation of resources mediated the effect of account status on spending (indirect effect: -0.91, 95% CI [-1.96, -0.025]).
  - num: The proportion remaining moderates the effect; spending increased as the relative amount decreased in used accounts (b = -7.99, p < .001).
  - Used account effect holds for both endowed (gift cards, reward points) and earned resources (checking accounts).
  - Unspecified checking accounts are perceived as used, leading to similar spending likelihood as specified used accounts.
  - The effect generalizes from spending to donation decisions (charitable giving).
key_figures_tables:
  - "Figure 1: Likelihood of spending $5 on a drink across used vs. unused gift cards → Used accounts increase spending."
  - "Figure 2A: Spending likelihood from used, unused, and unspecified checking accounts → Unspecified mimics used."
  - "Figure 3A: Spending likelihood of 30,000 reward points → Used accounts increase points spending versus cash."
  - "Figure 4: Moderation by proportion remaining (60%, 40%, 20%) → Steeper spending increase in used accounts."
  - "Table S1 (Appendix): Summary of results across seven studies → Consistent main effect and mediation."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Used account
    definition: An account from which some resources have already been spent.
  - term: Unused account
    definition: An account from which no resources have been spent.
  - term: Within-account comparison
    definition: Comparing current remaining resources to the original amount in the same account.
  - term: Psychological value
    definition: Perception of importance, worth, or usefulness of a resource.
critical_citations:
  - "[Heath & Soll, 1996] — Mental accounting and earmarking effects."
  - "[Arkes et al., 1994] — Windfall gains are spent more readily."
  - "[Hsee, 1996] — Relative versus absolute judgments."
  - "[Cheema & Soman, 2008] — Partitioning resources reduces consumption."
  - "[Morewedge et al., 2007] — Context influences perceived magnitude."
relevance:
  topics:
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "high"
      justification: "Directly examines how account categorization (used vs. unused) influences spending behavior."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      relevance: "high"
      justification: "Provides evidence that category framing (used vs. unused) affects resource valuation and spending."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Informative for understanding how PFMS account presentation could influence user behavior."
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "low"
      justification: "Tangentially relevant via spending likelihood based on account status."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "contextual"
      justification: "Mentions savings goals in Essay 3; but paper primarily focuses on spending, not goal management."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "contextual"
      justification: "Not directly studied; contextual for understanding broad spending patterns."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "contextual"
      justification: "Behavioral tendency (spending from used accounts) could inform profiles but not directly studied."
  contribution: "This paper provides a direct causal mechanism—within-account comparison—that can inform Odin's expense categorization module (3.A) by demonstrating that presenting an account as 'used' versus 'unused' changes spending propensity. For budget recommendation (7.B), the finding that users may undervalue resources in used accounts suggests that Odin should consider account history when recommending spending adjustments. For user onboarding (5.B), the cold-start problem may be mitigated by framing new accounts as 'unused' to encourage more conservative spending until a user's behavior is learned. The moderation by proportion remaining (3.B) offers a concrete design lever: displaying remaining balance relative to the original amount can nudge spending behavior. These insights directly apply to Odin's goal of helping Filipino young professionals manage finances, especially in culturally relevant contexts where gift cards and reward points are common."
  directly_justifies:
    - "Used accounts decrease perceived resource value compared to unused accounts with equal balances."
    - "The proportion of resources remaining in an account moderates the spending effect; lower proportions increase spending."
    - "Unspecified checking accounts are naturally perceived as used, affecting spending decisions."
    - "Valuation mediates the effect of account status on spending likelihood."
  limits:
    - "Studies conducted primarily with U.S. participants; may not generalize to Filipino cultural context."
    - "Focuses on spending, not on savings or debt management directly."
    - "The effect may be attenuated in high-involvement or large-ticket decisions not tested."
  mapping_rationale: "All 12 functional domains and their associated topic codes were systematically scanned. The paper directly addresses Expense Categorization (3.A, 3.B) via its core manipulation of used vs. unused accounts and their impact on spending and valuation. It also informs Existing Systems (4.A) by demonstrating a behavioral bias that PFMS should account for. The third essay touches on Savings Goal Management (13.A), but the primary contribution is on spending, so this is marked contextual. The moderation by remaining proportion (3.B) is a key design insight. Domains like Anomaly Detection (8.A-C), Forecasting (6.A-B), and Mobile Design (9.A-B) were considered but rejected because the paper does not address algorithms, prediction, or interface design. Filipino-specific topics (1.A-C, 2.A-D) were rejected as the sample is U.S.-based, though the behavioral principle may be culturally transferable. Overall, the paper offers strong, directly actionable evidence for how account presentation influences user spending, making it highly relevant for Odin's expense categorization and budget recommendation modules."
limitations:
  - "The effect may not replicate outside the U.S. where gift card and reward point usage patterns differ. [unacknowledged]"
  - "The research does not examine long-term effects on savings or overall financial health. [unacknowledged]"
  - "Incentive-compatible studies were limited to online shopping; field studies are lacking. [unacknowledged]"
  - "The mechanism is measured via self-report; behavioral data on valuation is not directly observed."
  - "Potential demand effects in experimental scenarios may influence reported spending likelihood."
remember_this:
  - "Used accounts reduce perceived value and increase spending by up to 15.8 points."
  - "Account history framing is a powerful nudge in PFMS design."
  - "Unspecified accounts are automatically treated as used by default."
  - "Valuation mediates the link between account status and spending."
  - "Relative balance (e.g., 20% vs. 60% left) moderates the spending effect."
```
---

## Paper 22: Faisal et al_summarized.md

**Source File:** `Faisal et al_summarized.md`

```yaml
paper_id: "10.69593/faet.v1i01.NA"
designation: "international"
title: "The Role of Digital Banking Features in Bank Selection an Analysis of Customer Preferences for Online and Mobile Banking"
authors: "Faisal, N.; Nahar, J.; Waliullah, M.; Borna, R. S."
year: 2024
venue: "Frontiers in Applied Engineering and Technology"
odin_topics:
  - "9.A"
  - "9.B"
  - "10.A"
  - "10.B"
  - "7.B"
  - "4.A"
  - "4.B"
tldr: "A systematic review of 112 articles identifies convenience, security, personalization, and competitive innovation as key drivers of customer satisfaction and loyalty in digital banking."
problem_and_motivation: "Financial institutions need to understand which digital banking features most influence customer preferences to remain competitive. Prior literature lacked a consolidated synthesis of key drivers across convenience, security, and personalization. This review addresses the gap by systematically aggregating findings on customer preferences for online and mobile banking features."
approach:
  - "Conducted a systematic literature review following PRISMA guidelines to ensure transparency and rigor."
  - "Searched Scopus, Web of Science, ProQuest, and Google Scholar using combinations of keywords such as 'digital banking,' 'customer preferences,' 'online banking,' 'mobile banking,' 'blockchain,' and 'AI.'"
  - "Identified 3,284 initial articles, removed 326 duplicates, and screened 947 after title/abstract review."
  - "Full-text review of 947 articles resulted in a final selection of 112 peer-reviewed studies published between 2012 and 2023."
  - "Extracted and synthesized findings related to convenience, security, personalization, competitive innovation, and pandemic-driven adoption."
findings:
  - "num: 47 articles consistently highlighted ease of use and 24/7 availability as primary drivers of adoption."
  - "num: 38 studies identified mobile banking as the preferred platform due to intuitive interfaces."
  - "num: 42 articles emphasized security and privacy, with encryption and fraud detection as key trust-building factors."
  - "num: 36 studies found that personalization, driven by AI and data analytics, enhances customer satisfaction and retention."
  - "num: 29 articles highlighted competitive pressure as a driver of innovation, including blockchain and biometric authentication."
  - "num: 31 studies showed the COVID-19 pandemic accelerated digital adoption and reshaped customer expectations."
  - "Customers value transparency in data usage policies and proactive communication about security measures."
  - "Personalization must be balanced with privacy concerns, as excessive data collection can erode trust."
  - "Traditional banks adopting AI, blockchain, and biometrics are better positioned to compete with fintech firms."
  - "Strategic partnerships between banks and fintech companies, such as API integrations, can drive mutual growth."
key_figures_tables:
  - "None."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "TAM"
    definition: "Technology Acceptance Model, which posits that perceived usefulness and ease of use affect adoption."
  - term: "MFA"
    definition: "Multi-factor authentication, a security measure requiring multiple credentials."
  - term: "GDPR"
    definition: "General Data Protection Regulation, a data privacy regulation in the EU."
  - term: "API"
    definition: "Application Programming Interface, enabling software applications to communicate."
critical_citations:
  - "[Davis, 1989] — Foundational TAM theory for technology adoption."
  - "[Venkatesh et al., 2003] — Unified theory of acceptance and use of technology."
  - "[Chauhan et al., 2022] — Comprehensive review of customer experience in digital banking."
  - "[Gigante et al., 2022] — Analysis of digital banking preferences in Metro Manila."
  - "[Taylor et al., 2020] — Systematic review of blockchain cybersecurity in digital banking."
relevance:
  topics:
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "high"
      justification: "Paper highlights mobile banking as the preferred platform due to intuitive interfaces."
    - code: "9.B"
      name: "Mobile UX Design for Personal Finance"
      relevance: "high"
      justification: "Discusses user-friendly interfaces and 24/7 availability as key drivers of satisfaction."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "Paper emphasizes encryption, MFA, and fraud detection as critical determinants of trust."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "high"
      justification: "Transparency in data policies and proactive security communication foster trust."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Personalization and data analytics enable tailored financial advice, relevant to budgeting."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Provides an overview of digital banking features and competitive landscape."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Identifies gaps in research on underserved demographics and long-term loyalty."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "contextual"
      justification: "Mentions cultural influences on preferences but does not focus on Filipino context."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "low"
      justification: "Tangentially touches on engagement through personalization but not as a primary focus."
  contribution: "This review directly justifies the need for Odin's mobile-first design by showing that user-friendly interfaces and 24/7 availability are primary adoption drivers. It supports Odin's security module by confirming that encryption, MFA, and transparent data policies are critical for user trust. The findings on personalization and competitive innovation inform Odin's budget recommendation and anomaly detection modules, highlighting the importance of AI-driven insights and continuous improvement."
  directly_justifies:
    - "User-friendly interfaces and 24/7 availability are primary drivers of customer satisfaction and loyalty."
    - "Robust security measures, including encryption and multi-factor authentication, foster user trust."
    - "Personalization via AI and data analytics enhances user experience and retention in digital banking."
    - "Market competition drives innovation, including AI, blockchain, and biometrics in banking."
    - "The COVID-19 pandemic accelerated digital adoption, reshaping customer expectations for flexibility."
  limits:
    - "Findings are based on a broad international literature review; may not be fully generalizable to the Filipino context."
    - "Systematic review does not include primary empirical data; relies on the quality of reviewed studies."
    - "Focus is on general digital banking features, with limited depth on specific personal finance management modules."
    - "Cultural influences are mentioned but not systematically explored for Filipino young professionals."
    - "Long-term impact of specific technologies (e.g., AI, blockchain) on customer loyalty lacks direct empirical evidence." 
  mapping_rationale: "All 12 functional domains and their associated topic codes were systematically scanned. The paper was flagged as highly relevant for Mobile-First Design (9.A, 9.B) and Data Privacy & User Trust (10.A, 10.B) because it directly addresses user-friendly interfaces, security measures, and transparency. Medium relevance was assigned to Budget Recommendation (7.B) due to personalization and data analytics, and to Existing Systems (4.A, 4.B) for the landscape and gaps identified. Contextual relevance was noted for Culturally Specific Practices (2.A) due to a brief mention of cultural factors. Low relevance was assigned to Engagement Dynamics (11.A) as it is only tangentially touched upon. Domains like Filipino Cultural Context (2.B, 2.C, 2.D), Behavioral Profiling (5.A, 5.B, 5.C), Spending Forecasting (6.A, 6.B), Anomaly Detection (8.A, 8.B, 8.C), Evaluation Frameworks (12.A, 12.B, 12.C), and Savings & Debt Management (13.A, 13.B, 13.C) were considered but rejected as the paper does not provide citeable claims for Odin's design in these areas. Overall, the paper provides strong justification for Odin's focus on mobile-first design and security."
limitations:
  - "Geographic scope of the reviewed studies is predominantly Western or global, limiting applicability to Filipino young professionals."
  - "Systematic review methodology may be subject to publication bias; studies with positive findings are more likely to be published."
  - "The paper focuses on banking features but does not address personal finance management or budgeting specifically."
  - "Ethical implications and regulatory compliance like GDPR are mentioned but not deeply explored [unacknowledged]."
  - "Digital literacy and technology access are noted as barriers but not systematically analyzed for underserved populations [unacknowledged]."
remember_this:
  - "User-friendly interfaces and 24/7 availability are primary drivers of digital banking adoption."
  - "Encryption, MFA, and transparent data policies are critical for fostering customer trust."
  - "AI-driven personalization enhances customer satisfaction and retention in digital banking."
  - "The COVID-19 pandemic accelerated digital adoption and reshaped customer expectations for flexibility."
  - "47 out of 112 reviewed articles consistently highlighted ease of use as a key adoption factor."
```
---

## Paper 23: Nourallah et al_summarized.md

**Source File:** `Nourallah et al_summarized.md`

```yaml
paper_id: 10.1016/j.gfj.2024.101008
designation: international
title: Financial technology and financial capability: Study of the European Union
authors: Nourallah, M.; Öhman, P.; Hamati, S.
year: 2024
venue: Global Finance Journal
odin_topics:
  - 1.C
  - 2.D
  - 3.C
  - 4.A
  - 5.A
  - 5.B
  - 7.B
  - 10.A
  - 13.A
  - 13.B
tldr: FinTech use positively and significantly affects financial capability across EU countries, with effects stronger in nations progressing well on the Europe 2020 strategy.
problem_and_motivation: Household financial capability is understudied in the European Union, and the role of FinTech in enhancing it remains ambiguous despite widespread adoption. Existing measures of financial capability are naive and lack a comprehensive framework incorporating skills, debt, saving, resilience, and well-being.
approach:
  - Uses balanced panel data from 24 EU countries across three waves (2014, 2017, 2021) from Global Findex and Eurostat.
  - Measures financial capability as the arithmetic mean of five constructs: skills, debt, saving, financial resilience, and financial well-being.
  - Employs fixed-effects regression with robust standard errors clustered by country, supplemented by IV and System-GMM for endogeneity.
  - Uses broadband Internet coverage as an instrumental variable for FinTech adoption.
  - Conducts robustness checks by replacing income with GDP per capita growth and adding control variables like rule of law and trade openness.
findings:
  - num: FinTech has a significant positive effect on financial capability (coefficient 0.277, p < 0.01) in the baseline fixed-effects model.
  - num: The Human Development Index positively affects financial capability (coefficient 1.189, p < 0.05).
  - num: EU countries vary greatly; Sweden, Netherlands, and Austria have the highest financial capability scores (0.684, 0.656, 0.652 out of 1).
  - num: Hungary and Latvia had the highest percentage growth in financial capability (34.3% and 25.5%) from 2014-2021.
  - num: The effect of FinTech is stronger in countries making good progress on the Europe 2020 strategy (coefficient 0.377) than in others (0.325).
  - Received wages and financial freedom show no significant relationship with financial capability.
key_figures_tables:
  - Figure 1: Financial capability scores (2014-2021) by country → Sweden leads at 0.684; Bulgaria and Greece lowest at 0.447.
  - Figure 3: FinTech scores (2014-2021) by country → Sweden, Finland, Estonia highest; Romania, Bulgaria lowest.
  - Table 2: Fixed-effects regression results → FinTech coefficient stable at ~0.277-0.334 across models.
  - Table 3: IV estimates → FinTech coefficient 0.344-0.425, confirming positive effect.
  - Table 8: Subsample analysis → FinTech effect larger in high-EU2020-strategy countries.
key_equations:
  - equation: Financialcapability = (skills + debt + saving + financialresilience + financialwellbeing) / 5
    explanation: Arithmetic mean of five constructs measuring financial capability.
  - equation: Financialcapability_{i,t} = α1 + α2 * financialtechnology_{i,t} + Σρ_n * X_{n,i,t} + u_{i,t}
    explanation: Baseline fixed-effects regression model with controls.
definitions:
  - term: Financial capability
    definition: Consumer ability to apply knowledge and perform desirable financial behavior to achieve financial well-being.
  - term: FinTech
    definition: Digital financial technology solutions enabling transaction tracking, payment scheduling, and savings management.
  - term: Financial resilience
    definition: Capacity to face unexpected financial expenses.
  - term: Financial well-being
    definition: Satisfaction with financial situation and perceived financial security.
critical_citations:
  - "[Lusardi, 2011] — Defines financial capability as making ends meet, planning ahead, and managing products."
  - "[French et al., 2020] — Shows smartphone apps improve financial behavior in the UK."
  - "[Demirgüç-Kunt et al., 2022] — Provides Global Findex data used for FinTech and debt measures."
  - "[Sen, 1993] — Capability approach foundation for measuring financial capability."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: contextual
      justification: Provides EU-level evidence on FinTech's role in financial behavior outcomes.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Mentions seasonal spending and financial resilience indirectly but not specific to Filipino cycles.
    - code: 3.C
      name: User-Defined Allocation Constraints
      relevance: low
      justification: Discusses saving and debt management as capability components, not user constraints.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Reviews FinTech solutions and their role in household finance management.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly links FinTech use to improved financial behaviors and capability outcomes.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: high
      justification: Suggests FinTech can help overcome initial capability gaps via reminders and planning tools.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Implies FinTech tools that track spending and savings support better budgeting.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Mentions FinTech security and trust in passing, not a central focus.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Uses saving as a core construct of financial capability.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: medium
      justification: Uses debt as a core construct of financial capability.
  contribution: This paper provides a validated multi-dimensional framework for measuring financial capability that can inform Odin's user profiling module. Its finding that FinTech use positively predicts financial capability justifies Odin's reliance on digital tools to enhance user financial behavior. The EU-level analysis offers benchmark comparisons for evaluating Odin's performance against international standards. The identification of income as non-significant challenges assumptions and supports Odin's focus on behavioral rather than purely income-based features.
  directly_justifies:
    - "FinTech solutions enable individuals to track transactions and manage savings plans."
    - "Use of mobile phones to pay bills is a valid proxy for FinTech engagement."
    - "FinTech has a significant positive effect on financial capability (p < 0.01)."
    - "Financial resilience improves with FinTech adoption."
    - "Saving behavior is enhanced by digital financial tools."
  limits:
    - "Data are limited to EU countries and may not generalize to the Philippines. [unacknowledged]"
    - "Socioeconomic variables were not explored due to data limitations. [acknowledged]"
    - "Potential negative effects of FinTech (overconsumption, fraud) are noted but not empirically tested. [acknowledged]"
    - "Cross-sectional design within waves limits causal claims. [unacknowledged]"
  mapping_rationale: All 12 functional domains and their 41 associated topic codes were systematically scanned. The domains flagged as relevant were: Behavioral Profiling & Classification (5.A, 5.B) due to the paper's direct evidence that FinTech use improves financial behaviors and capability; Expense Categorization (3.C) and Savings & Debt Management (13.A, 13.B) because capability is measured via saving and debt constructs; Budget Recommendation (7.B) via the implied role of tracking tools; Existing Systems & Gaps (4.A) via the FinTech landscape review; and Data Privacy & User Trust (10.A) via passing mentions. The Filipino Cultural Context domain (2.A-D) was considered but rejected because the study is EU-focused; however, topic 2.D (spending cycles) was flagged as low relevance because financial resilience relates to unexpected expenses. Topic 1.C was assigned contextual relevance. The paper does not address forecasting (6.A/B), anomaly detection (8.A-C), mobile-first design (9.A/B), user retention (11.A/B), or system evaluation (12.A-C), so these were rejected. Overall, the paper is highly relevant for justifying FinTech-enabled behavioral profiling and capability measurement in Odin.
limitations:
  - "Limited to EU countries; generalizability to Philippine context is uncertain. [unacknowledged]"
  - "Socioeconomic variables not explored due to data limitations. [acknowledged]"
  - "Potential unethical FinTech use (overconsumption, fraud) not empirically examined. [acknowledged]"
  - "Three-wave panel has limited time span for long-term capability trends. [acknowledged]"
  - "Instrumental variable (broadband coverage) may not fully isolate FinTech effects. [unacknowledged]"
remember_this:
  - "FinTech use significantly improves financial capability (coefficient 0.277)."
  - "Human Development Index strongly predicts higher financial capability."
  - "Income alone does not guarantee financial capability."
  - "EU northern countries lead in both FinTech and financial capability scores."
  - "Financial resilience and saving are key components of capability."
```
---

## Paper 24: Raya_summarized.md

**Source File:** `Raya_summarized.md`

```yaml
paper_id: 5917e8c4-2b8a-50a1-a9b5-4d943d5bb246
designation: international
title: Exploring the Influence of Financial Literacy and Lifestyle Choices on Financial Management Practices among Young Workers in Batam City's Urban Landscape
authors: Raya, S. I.
year: 2024
venue: Cebong Journal
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.D
  - 3.A
  - 4.A
  - 5.A
  - 5.C
tldr: Lifestyle choices and financial literacy jointly shape financial management behaviors among young urban workers, with higher literacy correlating with improved practices.
problem_and_motivation: Young urban workers face challenges in managing finances due to rising living costs and diverse lifestyle choices. Limited financial literacy exacerbates these challenges, leading to poor planning and debt. The interplay between lifestyle and literacy in this context is not well understood.
approach:
  - A mixed-methods approach was used combining quantitative surveys and qualitative interviews.
  - The quantitative phase surveyed a purposive sample of young workers in Batam City.
  - The survey collected data on demographics, lifestyle choices, financial literacy levels, and financial management practices.
  - The qualitative phase involved semi-structured interviews with a subset of survey participants.
  - Quantitative data were analyzed using descriptive statistics and regression analyses to identify correlations and patterns.
  - Qualitative data underwent thematic analysis to identify recurring themes and provide depth to statistical outcomes.
findings:
  - num: Higher financial literacy levels correlated positively with more robust savings habits.
  - An urban lifestyle was associated with increased challenges in debt management.
  - Lifestyle preferences for entertainment spending correlated with more conservative investment approaches.
  - Some individuals struggled to apply financial knowledge practically, despite possessing it.
  - Peer influence was cited as a significant factor shaping spending patterns among young workers.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Financial Literacy
    definition: The knowledge and understanding of financial concepts enabling informed financial decisions.
critical_citations:
  - "[Remund, 2010] — Defines financial literacy as essential for management."
  - "[Zalega, 2018] — Links lifestyle choices to financial management strategies."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Paper studies young workers in a similar Southeast Asian urban context.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: contextual
      justification: Examines financial challenges like debt and savings relevant to income structure.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Directly investigates financial management behaviors and decision-making.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: low
      justification: Touches on peer influence but lacks specific Filipino cultural practices.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: Urban lifestyle as a spending influence offers a parallel to spending cycles.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: Lifestyle choices as spending drivers can inform categorization.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Identifies financial management challenges but not existing PFMS.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly links lifestyle and literacy to distinct financial behaviors.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Provides evidence that literacy and lifestyle are key behavioral classifiers.
  contribution: This paper provides empirical evidence that lifestyle choices and financial literacy are significant determinants of financial management behaviors among young urban workers. The finding that higher financial literacy correlates with better savings and investment habits can justify Odin's focus on educational features. The observed gap between theoretical knowledge and practical application supports the need for Odin's hands-on, behavior-oriented tools. The influence of peer and urban lifestyle factors highlights the importance of social and contextual features within the app for engagement and relevance.
  directly_justifies:
    - Financial literacy positively correlates with prudent financial management practices among young workers.
    - Lifestyle choices significantly influence spending patterns and debt management.
    - There is a gap between financial knowledge and its practical application in daily decisions.
    - Peer influence is a strong factor in shaping financial behaviors.
  limits:
    - The study is based in Batam City, Indonesia, which limits direct generalizability to Filipinos.
    - The sample was purposive and may not be fully representative of all young workers.
    - Self-reporting biases may affect the accuracy of financial data.
    - Methodology lacks detail on model or algorithm specifics for direct implementation. [unacknowledged]
  mapping_rationale: All 12 functional domains were systematically scanned against the paper's content. The domains of Behavioral Profiling & Classification were flagged as highly relevant because the study directly investigates how lifestyle and literacy shape financial behavior (codes 5.A, 5.C). The Filipino Cultural Context and Expense Categorization domains were considered contextually relevant, with codes 1.A, 1.B, 1.C, 2.A, and 2.D flagged as low to medium relevance for providing background on young urban worker demographics and spending influences. The Existing Systems domain (4.A) was flagged as low, as the paper identifies financial management challenges but does not review PFMS. Domains like Spending Forecasting, Budget Recommendation, Anomaly Detection, Mobile-First Design, Data Privacy, User Retention, System Evaluation, and Savings & Debt Management were considered and rejected because the paper does not address predictive models, algorithmic approaches, mobile interfaces, privacy/trust metrics, engagement strategies, system evaluation frameworks, or specific savings/debt management mechanisms. The paper's overall relevance to Odin is moderate, providing foundational behavioral insights but lacking the algorithmic or system design focus needed for direct implementation.
limitations:
  - Results may not be generalizable to Filipino young professionals due to the Indonesian study context.
  - The sample was purposive and may not be fully representative of all young workers.
  - Self-reporting biases may affect the accuracy of financial data.
  - Methodology lacks detail on model or algorithm specifics for direct implementation. [unacknowledged]
remember_this:
  - Higher financial literacy is linked to better savings habits.
  - Urban lifestyles are associated with greater debt management challenges.
  - Peer influence significantly shapes spending behaviors.
  - There is a gap between financial knowledge and its practical application.
  - Lifestyle choices and financial literacy jointly determine financial management practices.
```
---

## Paper 25: Schwartz_summarized.md

**Source File:** `Schwartz_summarized.md`

```yaml
paper_id: 58b9e7a8-507f-5b70-8df8-9c7f07a1a5fe
designation: international
title: "The Rise of a Nudge: Field Experiment and Machine Learning on Minimum and Full Credit Card Payments"
authors: "Schwartz, D."
year: 2024
venue: "Unknown"
odin_topics:
  - "2.A"
  - "2.B"
  - "2.D"
  - "3.A"
  - "3.C"
  - "4.A"
  - "4.B"
  - "5.A"
  - "5.B"
  - "5.C"
  - "6.A"
  - "6.B"
  - "7.A"
  - "7.B"
  - "7.C"
  - "7.D"
  - "8.A"
  - "8.B"
  - "8.C"
  - "13.A"
tldr: "A field experiment on credit card payment warnings shows statement balance warnings increase full payments and reduce revolving interest, while minimum payment warnings reduce delinquency but do not increase full payments."
problem_and_motivation: "Minimum payment warnings, intended to reduce debt, may act as a perverse nudge by anchoring cardholders to lower payments, potentially increasing interest charges. A novel statement balance warning is proposed to help cardholders avoid interest by paying in full, but its effectiveness and heterogeneous effects are not well understood in real-world settings."
approach:
  - "A randomized controlled field experiment with 179,706 credit card debtors and 2.85 million observations, testing four email reminder conditions: control, minimum payment warning, statement balance warning, and both warnings."
  - "The experiment used a difference-in-differences design with individual fixed effects to estimate average treatment effects on payment behavior, interest charges, and delinquency."
  - "Causal random forests were applied to estimate heterogeneous treatment effects and to characterize subgroups with the largest responses to each warning."
  - "An online experiment with 400 participants replicated the field experiment to examine the role of financial knowledge, vulnerability, and cognitive reflection in warning effectiveness."
findings:
  - "num: Statement balance warnings increased the likelihood of paying in full by 0.9-1.1% (0.6-0.7 percentage points) compared to a simple reminder."
  - "num: Minimum payment warnings reduced the probability of not paying at least the minimum by 6.9-8.8% (0.7-0.9 percentage points) relative to the control."
  - "num: Both warnings reduced revolving interest by 9.0% and delinquent interest by 8.0% compared to the control condition."
  - "Causal forest analysis reveals significant heterogeneity; the top quintile of cardholders receiving the statement balance warning increased full payment likelihood by 2.4 percentage points."
  - "The warnings appear to act as target values rather than anchors, with cardholders shifting payments towards the salient amount (minimum or statement balance)."
  - "Effects are more pronounced for cardholders who vary their payment amounts, suggesting deliberation, and are not driven by liquidity constraints or income levels."
  - "The online experiment shows that the statement balance warning improves self-reported understanding of the statement balance, but effects are not moderated by financial literacy or cognitive reflection."
  - "The policy optimization analysis suggests that most cardholders should receive the statement balance warning or both warnings to minimize interest charges."
key_figures_tables:
  - "Figure 1: Payment distribution shifts → Warnings shift payments towards the salient target amount."
  - "Table II: Average treatment effects → All warnings increase payments and reduce delinquency, but only statement balance warnings increase full payments."
  - "Table IV: Sorted CATE per quintile → Top quintiles show much larger effects, revealing heterogeneity."
  - "Table VII: Effects based on previous behavior → Warnings are more effective for those who vary payments and have small gaps between minimum and statement balance."
  - "Table IX: Online experiment results → Statement balance warnings increase full payment likelihood by 18-25 percentage points in a hypothetical setting."
key_equations:
  - equation: "y_{it} = α + Σ_j β_j D_{ij} × P_t + δ P_t + X_{it} + μ_m + μ_y + a_i + ε_{it}"
    explanation: "Difference-in-differences model for estimating warning effects."
  - equation: "τ_D(x) = E[Y_i(1) - Y_i(0) | X_i = x]"
    explanation: "Conditional average treatment effect (CATE) for a warning D."
  - equation: "y_i = Σ_{k=1}^5 τ_{kD} w_{Di} × n_{ki} + Σ_{k=1}^5 ϑ_k n_{ki} + u_i"
    explanation: "Estimating CATEs for quintiles from causal random forest."
definitions:
  - term: "CATE"
    definition: "Conditional Average Treatment Effect; the expected treatment effect for an individual given their covariates."
  - term: "Causal Random Forest"
    definition: "A machine learning method for estimating heterogeneous treatment effects using random forests with a causal objective."
  - term: "Difference-in-Differences"
    definition: "A quasi-experimental design that compares changes in outcomes over time between treatment and control groups."
  - term: "Delinquent Interest"
    definition: "Interest charged when a cardholder fails to pay at least the minimum payment."
  - term: "Revolving Interest"
    definition: "Interest charged on the unpaid balance when a cardholder pays less than the full statement balance but at least the minimum."
  - term: "MAD"
    definition: "Mean Absolute Deviation; a measure of variability in payment amounts, used as a proxy for deliberation."
  - term: "Anchoring Bias"
    definition: "The tendency to rely heavily on an initial piece of information (an 'anchor') when making decisions."
critical_citations:
  - "[Wang and Keys, 2014] — Found minimum payment warnings can have a perverse effect."
  - "[Athey and Imbens, 2019] — Overview of machine learning methods for causal inference, including causal forests."
  - "[Tversky and Kahneman, 1974] — Seminal work on anchoring bias."
  - "[Navarro-Martinez et al., 2011] — Lab evidence on minimum payment salience reducing payments."
  - "[Agarwal et al., 2015] — Found no sizable effect of a minimum payment nudge in a field setting, contrasting lab results."
relevance:
  topics:
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "contextual"
      justification: "The study is set in Chile, but findings on warning effectiveness are broadly applicable, not culturally specific."
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "low"
      justification: "The experiment is conducted over one billing cycle, but post-treatment effects dissipate, hinting at cyclicality in response."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "low"
      justification: "The paper does not address Filipino-specific cycles, but the target-value finding could be relevant for understanding spending around occasions."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "contextual"
      justification: "The paper focuses on payment amounts, not categorization, but the concept of targets could inform categorization design."
    - code: "3.C"
      name: "User-Defined Allocation Constraints"
      relevance: "low"
      justification: "The findings on target values and deliberation are relevant for how users set their own allocation constraints."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "The paper reviews credit card statements and warnings, which are part of the PFMS landscape."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "The paper directly identifies the limitation of minimum payment warnings as a perverse nudge and proposes a solution."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "The causal forest analysis characterizes profiles based on payment history and response to warnings."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "low"
      justification: "The paper discusses heterogeneity but does not focus on cold-start profile estimation."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "Causal random forests are used to classify individuals based on treatment response, a form of behavioral profiling."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "contextual"
      justification: "The paper uses machine learning for causal inference, not forecasting, but the techniques are relevant."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "low"
      justification: "The paper does not forecast spending; it analyzes payment behavior."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "low"
      justification: "The paper's findings on target values can inform how to present budget targets."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "The policy optimization analysis is a form of recommending the best warning message for each user."
    - code: "7.C"
      name: "Constrained Optimization Approaches for Budget Allocation"
      relevance: "low"
      justification: "The paper does not use constrained optimization, but the two-target setting (minimum vs. full) is analogous."
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "medium"
      justification: "The paper shows users prioritize a target based on attainability, similar to handling infeasible budget constraints."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "contextual"
      justification: "Delinquency (not paying minimum) is an anomaly the warnings aim to prevent."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "low"
      justification: "The paper does not use anomaly detection algorithms."
    - code: "8.C"
      name: "Cold-Start Baseline Strategies for Anomaly Detection"
      relevance: "low"
      justification: "The paper does not address cold-start anomaly detection."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "medium"
      justification: "The statement balance warning encourages a savings-like behavior (avoiding interest) by paying a target amount."
  contribution: "This paper provides experimental evidence that a statement balance warning is an effective nudge for increasing credit card payments and reducing interest charges, offering a directly implementable design feature for Odin's payment reminder or bill-pay module. The use of causal random forests demonstrates a methodology for profiling users based on their heterogeneous responses, which can inform Odin's behavioral profiling and personalization engine. The finding that warnings act as target values rather than anchors has implications for how Odin presents budget goals and savings targets to users. The policy optimization framework provides a template for Odin to recommend personalized nudges or reminders based on user payment history. The paper also highlights the importance of testing behavioral interventions in field settings to overcome biases found in lab experiments."
  directly_justifies:
    - "Statement balance warnings increase full payments and reduce revolving interest, providing a justification for including such a feature in Odin's bill-pay reminders."
    - "Minimum payment warnings reduce delinquency, supporting the use of such warnings for users at risk of missing minimum payments."
    - "Causal random forests can be used to profile users and personalize nudges, supporting Odin's adaptive recommendation system."
    - "Warnings act as target values, suggesting that presenting clear, actionable financial targets can improve user behavior in Odin."
    - "Behavioral interventions can be designed to be scalable and palatable to financial institutions, supporting Odin's potential for real-world deployment."
  limits:
    - "The field experiment was conducted over one billing cycle; long-term effects and habituation to warnings are not assessed."
    - "The study is set in Chile with a specific credit card issuer; generalizability to other countries and financial products, including PFMS like Odin, requires validation."
    - "The online experiment is hypothetical, and stated intentions may not perfectly correlate with real payment behavior."
    - "The causal forest analysis, while robust, may not be easily interpretable for all stakeholders, posing a challenge for explaining personalized recommendations."
    - "The study does not address how warnings interact with other financial behaviors, such as budgeting or savings, which are central to Odin."
  mapping_rationale: "A systematic scan was performed across all 12 functional domains and their associated topic codes. The paper was flagged as most relevant to 'Existing Systems & Gaps' (4.A, 4.B) due to its direct critique of the minimum payment warning and proposal of a new solution. It is highly relevant to 'Behavioral Profiling & Classification' (5.A, 5.C) because of its use of causal forests to identify heterogeneous treatment effects and profile users based on payment history and response, and to 'Budget Recommendation' (7.A, 7.B, 7.D) through its policy optimization analysis and two-target setting which parallels constrained budget allocation. The paper also has medium relevance to 'Savings & Debt Management' (13.A) as the statement balance warning encourages debt reduction and interest avoidance akin to a savings goal, and 'Anomaly Detection' (8.A) indirectly through its focus on preventing delinquency. Topics related to 'Filipino Cultural Context' (2.A, 2.B, 2.D) were considered but deemed contextual or low relevance as the study is not specific to the Philippines, though its behavioral findings are broadly applicable. Topics like 'Expense Categorization' (3.A, 3.B) and 'Spending Forecasting' (6.A, 6.B) were considered rejected because the paper does not address categorization or predictive forecasting directly, though its methodology could be extended to those areas. The paper's overall relevance to Odin is substantial, providing evidence-based design principles for payment reminders, behavioral profiling, and personalized nudging, while also offering a cautionary tale about the potential perverse effects of poorly designed nudges."
limitations:
  - "The field experiment was conducted over a single billing cycle, leaving open questions about long-term effectiveness and habituation."
  - "The sample is from Chile, which has a unique financial landscape; findings may not generalize to Filipino young professionals without further validation."
  - "The online experiment is hypothetical, and intentions may not translate to actual behavior in a real PFMS context."
  - "The study does not explore how warnings interact with other PFMS features like budgeting or savings goals."
  - "The causal forest analysis, while powerful, relies on a specific implementation and may not be easily replicable in all settings. [unacknowledged]"
  - "The policy optimization analysis is a simulation and does not account for the dynamic nature of user preferences over time. [unacknowledged]"
  - "The potential for unintended consequences, such as users reducing other forms of saving to make larger credit card payments, is not examined. [unacknowledged]"
remember_this:
  - "Statement balance warnings increase full credit card payments by 0.9-1.1%."
  - "Minimum payment warnings reduce the probability of delinquency by 6.9-8.8%."
  - "Causal random forests reveal that 20-40% of cardholders significantly increase payments due to warnings."
  - "Warnings act as target values, not anchors, shifting payments towards the salient amount."
  - "The effect of warnings is not driven by income or liquidity constraints, but by payment variability."
```
---


---

## Agent Instruction

If the agent reading this document believes further context about a paper is needed, it may request the original converted markdown file (with the '_marked' suffix) from the user for the relevant paper(s).
