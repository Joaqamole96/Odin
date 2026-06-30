# Compiled Research Summaries

## Filters Applied

- Designation: `international`

**Total Papers:** 25

**Note:** Included papers positions 1 to 25, Sorted by year.

---

## Paper 1: Balcazar-Paiva et al_summarized.md

**Source File:** `Balcazar-Paiva et al_summarized.md`

```yaml
paper_id: 10.3390/ijfs14030076
designation: international
title: Financial Education in the Age of Artificial Intelligence: A Systematic Review with Text Mining and Natural Language Processing
authors: Balcazar-Paiva, E. S.; Haro-Sarango, A. F.; Villanueva-Calderón, J. A.
year: 2026
venue: International Journal of Financial Studies
odin_topics:
  - 4.B
  - 5.A
  - 10.A
  - 10.B
  - 11.A
  - 12.A
tldr: A systematic review of AI in financial education finds AI enables personalization and learning gains, but sustained behavioral impact remains unproven and ethical risks require robust governance.
problem_and_motivation: The literature on AI and financial education is fragmented, lacking integrative synthesis and robust theoretical frameworks that connect pedagogy, technology, and governance. Evidence on sustained behavioral change is scarce, and ethical implications in vulnerable settings are underexplored. This review addresses these gaps by systematically mapping applications, theoretical foundations, and ethical tensions.
approach:
  - A PRISMA-2020 systematic review was conducted across Scopus, ScienceDirect, and Taylor & Francis, retrieving 388 records and including 50 empirical studies after screening.
  - Bibliometric mapping with VOSviewer generated keyword co-occurrence networks to identify thematic structure and temporal evolution of the field.
  - A computational NLP pipeline applied VADER, TextBlob, and a multilingual transformer (XLM-RoBERTa) to abstract-level sentiment, polarity, and subjectivity analysis.
  - Sentence-aware chunking and token-weighted aggregation ensured robust transformer scoring for long abstracts.
  - Text metrics (length, lexical diversity, punctuation intensity) were correlated with sentiment signals to examine framing and stylistic patterns.
  - Term extraction with bilingual stopword filtering identified dominant unigrams and bigrams to contextualize sentiment and topic clusters.
findings:
  - num: The sentiment_index averaged 0.049, indicating a slightly positive tone, but with wide variability (interquartile range -0.0155 to 0.0749).
  - num: Transformer-based classification showed neutrality dominates (mean neutral probability 0.539), with positive (0.255) and negative (0.206) components.
  - Longer abstracts are associated with higher negativity and lower sentiment_index, reflecting greater methodological caution and inclusion of limitations.
  - Higher lexical diversity correlates with positive framing and opportunity-oriented language, independent of abstract length.
  - Keyword networks position AI as the central hub connecting financial literacy, education, health, management, and generative AI, with financial literacy emerging as a recent growth node.
  - The field is shifting from pandemic-driven digitalization toward generative AI and conversational systems for personalized tutoring and decision support.
  - Critical gaps include lack of longitudinal controlled studies, standardized metrics, model transparency, and geographic/cultural diversity in research.
key_figures_tables:
  - Figure 1: PRISMA flow diagram from 388 records to 50 included studies → rigorous selection process ensures traceable evidence base.
  - Figure 2: Keyword co-occurrence map showing AI as central hub connecting education, finance, health, and generative AI → AI functions as interdisciplinary organizing axis.
  - Figure 3: Temporal overlay reveals shift from COVID-19/health terms to ChatGPT, LLMs, and financial literacy → field evolving toward generative AI and educational applications.
  - Figure 4: Histogram of sentiment_index shows neutral mass centered near zero with slight positive tilt → discourse is technical and measured, not emotionally charged.
  - Figure 5: Correlation matrix links sentiment, length, and lexical diversity → longer abstracts carry more caution; lexical diversity signals positive framing.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: AI
    definition: Artificial Intelligence; constellation of technologies performing tasks traditionally requiring human intelligence.
  - term: NLP
    definition: Natural Language Processing; computational methods for analyzing and generating human language.
  - term: PRISMA
    definition: Preferred Reporting Items for Systematic Reviews and Meta-Analyses; guideline for transparent review reporting.
  - term: LLM
    definition: Large Language Model; deep learning model trained on vast text data for language generation and understanding.
  - term: VADER
    definition: Valence Aware Dictionary and sEntiment Reasoner; lexicon-based sentiment analysis tool.
  - term: XLM-RoBERTa
    definition: Cross-lingual RoBERTa; multilingual transformer model for sentiment classification.
critical_citations:
  - "[Zhu, 2025] — Positions machine learning as key to unlocking financial literacy and advancing personal finance research."
  - "[Leal & Oliveira, 2024] — Defines hypernudging and ethical frameworks for AI in financial behavior."
  - "[AL-Ghuribi et al., 2025] — Emphasizes privacy, fairness, and bias as structural conditions for responsible AI."
  - "[Wahyudi et al., 2025] — Highlights scarcity of longitudinal studies and standardized metrics as major gaps."
relevance:
  topics:
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: contextual
      justification: "Identifies research gaps (longitudinal, metrics) that inform system evaluation, but does not directly analyze PFMS systems."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: "Discusses AI-assisted nudging and hyper-personalization, supporting behavioral profiling for adaptive financial education."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: "Explicitly calls privacy a structural condition for responsible AI adoption, directly relevant to data governance."
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: "Transparency and trust are highlighted as determinants of adoption and effective use of automated financial technologies."
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: "Personalization and virtual tutoring are linked to immediate gains in comprehension and motivation, supporting engagement design."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: "Calls for standardized metrics, longitudinal designs, and controlled studies, directly relevant to evaluating Odin's modules."
  contribution: "This systematic review provides a comprehensive evidence synthesis that justifies Odin's adoption of AI for personalization and behavioral nudging, as it shows AI can improve comprehension and motivation. Its emphasis on privacy, fairness, and algorithmic bias informs Odin's data governance, transparency, and accountability requirements. The identification of evaluation gaps—lack of longitudinal studies and standardized metrics—directly supports Odin's need for robust impact assessment for its budget recommendation, savings, and anomaly detection modules. The review's call for cultural and linguistic adaptation reinforces Odin's localization for Filipino young professionals, ensuring contextual relevance."
  directly_justifies:
    - "AI can personalize financial education and improve comprehension and motivation, but evidence of sustained behavioral change remains nascent."
    - "Privacy, fairness, and algorithmic bias are structural conditions for responsible adoption in financial education systems."
    - "Transparency is a decisive determinant of adoption and trust in automated financial technologies."
    - "The field lacks longitudinal controlled studies and standardized metrics to measure lasting financial behavior change."
    - "Digital financial literacy requires critical competencies to evaluate AI-generated information and preserve agency over decisions."
  limits:
    - "The review synthesizes existing research but does not provide primary empirical evidence on effectiveness of specific AI tools."
    - "The NLP sentiment analysis is applied to abstracts only, not full texts, and does not measure pedagogical effectiveness or behavioral outcomes."
    - "The search was restricted to three databases, English and Spanish languages, and excluded gray literature, potentially missing relevant studies."
    - "No meta-analysis was possible due to methodological heterogeneity and absence of comparable effect-size reporting across included studies."
    - "The transformer-based sentiment model was trained on social media text, which may not fully capture academic writing conventions."
  mapping_rationale: "All 12 functional domains and their associated topic codes were systematically scanned against the paper's content. The domain 'Behavioral Profiling & Classification' was flagged as relevant because the paper extensively discusses AI-assisted nudging, personalization, and detection of financial literacy deficits, leading to selection of 5.A (medium). 'Data Privacy & User Trust' was selected with high relevance (10.A) and medium (10.B) because privacy, fairness, and transparency are repeatedly emphasized as structural conditions. 'User Retention & Engagement' (11.A) was flagged medium for its discussion of motivation and personalization. 'System Evaluation' (12.A) was selected medium due to explicit calls for standardized metrics and longitudinal designs. 'Existing Systems & Gaps' (4.B) was included as contextual because the paper identifies research gaps that inform evaluation but does not analyze PFMS systems. Borderline cases: the paper's mention of cultural context (e.g., Latin America) touches 2.A but was rejected because it does not address Filipino-specific practices; its discussion of financial behavior broadly touches 1.C but lacks specificity to Filipino young professionals. Domains related to expense categorization (3.A-C), spending forecasting (6.A-B), budgeting (7.A-D), anomaly detection (8.A-C), mobile design (9.A-B), and savings/debt (13.A-C) were considered and rejected because the paper does not address these operational functions. Overall, the paper provides strong background justification for AI personalization, ethics, and evaluation, but limited direct evidence for specific PFMS modules."
limitations:
  - "The review is restricted to three databases and excludes gray literature, potentially missing relevant studies not indexed in these sources. [unacknowledged]"
  - "Language bias toward English and Spanish may limit generalizability to non-Western contexts. [unacknowledged]"
  - "No manual reference searching was performed, which could have captured additional relevant studies. [unacknowledged]"
  - "The NLP sentiment analysis does not directly estimate pedagogical effectiveness; it captures discursive framing rather than causal impact. [acknowledged]"
  - "The transformer model was trained on social media text, which may affect calibration on academic abstracts despite chunking mitigation. [acknowledged]"
  - "Methodological heterogeneity across the 50 included studies prevented meta-analysis and limited statistical assessment of publication bias. [acknowledged]"
remember_this:
  - "The sentiment index averaged 0.049, indicating a slightly positive tone but with wide variability across abstracts."
  - "Longer abstracts tend to include more methodological caution, lowering sentiment scores."
  - "Greater lexical diversity signals opportunity-oriented framing, while lower diversity correlates with risk-focused language."
  - "The field is shifting from pandemic-driven digitalization toward generative AI and conversational systems for financial education."
  - "Privacy, fairness, and bias are not secondary concerns but structural conditions for responsible AI adoption in finance."
```
---

## Paper 2: Muthulakshmi & Jaisun_summarized.md

**Source File:** `Muthulakshmi & Jaisun_summarized.md`

```yaml
paper_id: a2b58c5e-0b5b-543b-9f4a-8b8d7b3c6f1e
designation: international
title: Transforming Finances: Exploring the Role of Artificial Intelligence in Personal Financial Decision-Making
authors: Muthulakshmi, V.; Jaisun, M.
year: 2026
venue: Journal of Exclusive Management Science
odin_topics:
  - 3.A
  - 4.A
  - 4.B
  - 5.A
  - 6.A
  - 7.A
  - 7.B
  - 7.D
  - 8.A
  - 10.A
  - 10.B
tldr: A review of AI applications in personal finance, covering budgeting, advisory, and risk management, while highlighting benefits, challenges, and future implications for individuals, professionals, and policymakers.
problem_and_motivation: The integration of AI is transforming personal financial decision-making, yet a comprehensive understanding of its implications, opportunities, and challenges is needed. There is a gap in synthesizing the current state of AI adoption and its multifaceted impact on individuals, financial professionals, and policymakers.
approach:
  - This exploratory study relies entirely on secondary data from research articles, reports, books, and journals.
  - The paper reviews AI-powered budgeting and expense tracking tools, automated investment advisory services, algorithmic trading systems, and AI-driven risk management solutions.
  - It analyzes the benefits and challenges associated with AI adoption in personal financial decision-making.
  - The methodology includes synthesizing existing literature and examining current trends to investigate the role of AI.
findings:
  - num: Nearly one in three investors feel comfortable implementing financial planning advice from a generative AI-powered tool.
  - AI algorithms quickly and accurately analyze extensive financial data, offering insights into spending patterns, investment opportunities, and financial goals.
  - AI powered tools automate routine financial tasks like budgeting, expense tracking, and investment management, saving time and minimizing errors.
  - AI algorithms can identify fraudulent activities, suspicious transactions, and identity theft by analyzing patterns and behavioral signals in financial data.
  - Challenges include data privacy and security concerns, algorithmic bias, regulatory compliance, dependency on technology, and data quality issues.
key_figures_tables:
  - "Figure 1: Role of technology in Personal financial decision-making → Shows the spectrum from traditional to AI-enhanced financial management."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Artificial Intelligence (AI)
    definition: The simulation of human intelligence processes by machines, especially computer systems.
  - term: Fin-tech
    definition: Technology and innovation that aims to compete with traditional financial methods in the delivery of financial services.
  - term: Robo-advisors
    definition: Automated investment advisory services that utilize AI and algorithms to provide personalized investment advice and portfolio management.
critical_citations:
  - "[Ribes, 2023] — Emphasizes the need for public reforms alongside AI transformation."
  - "[Braverman, 2023] — Notes the growing comfort of investors with AI-powered financial planning advice."
  - "[Soni, 2021] — Concludes that AI is becoming integral to the finance industry."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Discusses AI-powered tools for categorizing expenses and tracking spending patterns.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Provides a broad overview of AI applications in existing personal finance systems.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Explicitly lists limitations like data privacy, algorithmic bias, and regulatory compliance.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Mentions behavioral finance integration and addressing cognitive biases.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Envisions predictive financial insights and forecasting future financial trends.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Discusses AI-powered budgeting and expense tracking as a key application.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Mentions personalized recommendations for budgeting and saving.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: low
      justification: The paper does not address infeasibility handling in budget allocation.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly discusses AI-driven fraud detection and identifying suspicious transactions.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Identifies data privacy and security concerns as a primary challenge.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Notes the need for transparency and interpretability to build trust.
  contribution: This paper provides a foundational review that justifies the integration of AI across multiple Odin modules, from expense categorization and budgeting to fraud detection. It explicitly identifies key challenges like data privacy and algorithmic bias that Odin's design must address. The work underscores the need for personalized financial insights and automated management, which are core to Odin's value proposition. By mapping the landscape of AI in personal finance, it helps establish the broader context and necessity for Odin's AI-driven approach.
  directly_justifies:
    - AI algorithms can analyze vast amounts of data to inform financial decisions.
    - AI-powered tools automate routine tasks like budgeting and expense tracking.
    - AI-driven risk management solutions can safeguard investments and reduce losses.
    - Algorithmic transparency and fairness are critical for building trust in AI-driven services.
  limits:
    - The study relies entirely on secondary data, lacking empirical validation.
    - The paper is a broad review and does not evaluate specific algorithms or their performance.
    - Specific implementation details for AI in personal finance systems are not discussed.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. Domains deemed relevant include Expense Categorization (3.A), Existing Systems & Gaps (4.A, 4.B), Behavioral Profiling (5.A), Spending Forecasting (6.A), Budget Recommendation (7.A, 7.B, 7.D), Anomaly Detection (8.A), and Data Privacy & User Trust (10.A, 10.B). Topic 7.D (Infeasibility Handling) was considered and rejected as the paper does not address this specific algorithmic challenge. Topic 5.A was deemed medium relevance as the discussion on behavioral finance is high-level. Domains like Filipino Cultural Context (2), Mobile-First Design (9), User Retention (11), System Evaluation (12), and Savings & Debt Management (13) were considered but rejected due to the paper's general, international focus and lack of specific design or implementation insights. The paper is broadly relevant to Odin, providing a high-level justification for many of its AI-driven features and highlighting critical risks to address.
limitations:
  - "Relies entirely on secondary data; no primary research is conducted."
  - "Broad review; lacks specific algorithm evaluation."
  - "No empirical validation of claims regarding AI's impact."
  - "Does not address the implementation details for system design. [unacknowledged]"
remember_this:
  - AI automates personal finance tasks like budgeting and expense tracking.
  - AI algorithms improve fraud detection by analyzing financial patterns.
  - Data privacy and security are major challenges for AI in finance.
  - Algorithmic bias and lack of interpretability can undermine user trust.
  - Nearly one in three investors are comfortable with AI-powered financial advice.
```
---

## Paper 3: Aoun et al_summarized.md

**Source File:** `Aoun et al_summarized.md`

```yaml
paper_id: 10.3390/ijfs14020035
designation: international
title: "Understanding Millennials’ Financial Behavior: The Role of Fintech Adoption, Financial Literacy, and the Mediating Effect of Financial Attitudes in a Crisis-Affected Emerging Economy"
authors: "Aoun, D.; Rahal, R.; Sfeir, L.; Jabbour Al Maalouf, N."
year: 2026
venue: "International Journal of Financial Studies"
odin_topics:
  - "1.C"
  - "4.A"
  - "4.B"
  - "5.A"
  - "10.B"
tldr: "FinTech adoption and financial literacy positively predict millennial financial behavior, with financial attitude mediating the literacy-behavior link in Lebanon's crisis context."
problem_and_motivation: "Lebanon's economic crisis and banking collapse have eroded financial trust, yet little is known about how FinTech adoption, financial literacy, and attitudes jointly affect millennial financial behavior. Understanding these dynamics is critical for designing effective financial interventions in fragile economies. Prior research largely omits the attitudinal mediator in crisis settings."
approach:
  - "Collected survey data from 390 Lebanese millennials using a structured questionnaire."
  - "Measured FinTech adoption, financial literacy, financial attitude, and financial behavior via Likert scales."
  - "Applied structural equation modeling (SEM) to test direct and mediating effects."
  - "Assessed model fit using CFI, TLI, SRMR, and RMSEA, achieving good fit indices."
  - "Conducted confirmatory factor analysis and validated reliability via Cronbach's alpha and composite reliability."
findings:
  - "FinTech adoption positively predicts financial behavior (β = 0.144, p < 0.001)."
  - "Financial literacy positively predicts financial behavior (β = 0.337, p < 0.001)."
  - "Financial attitude positively predicts financial behavior (β = 0.414, p < 0.001)."
  - "Financial literacy strongly predicts financial attitude (β = 0.681, p < 0.001)."
  - "Financial attitude partially mediates the relationship between financial literacy and financial behavior."
  - "num: Financial attitude has the strongest effect on behavior among the predictors (β = 0.414)."
key_figures_tables:
  - "Table 7: SEM regression estimates showing all hypothesized paths are significant."
  - "Figure 2: Path diagram illustrating direct and mediated relationships with standardized coefficients."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "FinTech adoption"
    definition: "The extent to which individuals accept and integrate digital financial technologies into their financial activities."
  - term: "Financial literacy"
    definition: "The knowledge and skills that enable informed decision-making about budgeting, saving, investing, and managing credit."
  - term: "Financial attitude"
    definition: "An individual's psychological tendencies, beliefs, and evaluative judgments about money and financial decision-making."
  - term: "Financial behavior"
    definition: "Actual actions and conduct related to saving, spending, budgeting, debt repayment, and investing."
  - term: "Structural equation modeling (SEM)"
    definition: "A multivariate statistical technique for testing complex causal relationships among latent constructs."
critical_citations:
  - "[Lusardi & Mitchell, 2014] — Foundational definition and importance of financial literacy."
  - "[Swacha-Lech & Solarz, 2021] — Key determinants of FinTech adoption among millennials."
  - "[Abu Daqar et al., 2021] — Establishes link between FinTech and millennial financial behavior."
relevance:
  topics:
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "contextual"
      justification: "Focuses on millennial financial behavior but in Lebanese, not Filipino, context."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "low"
      justification: "Discusses FinTech adoption but not specific PFMS systems."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Identifies gaps like financial illiteracy and trust issues relevant to PFMS."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Directly examines behavioral determinants and attitudinal mediation, key for profiling."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "medium"
      justification: "Highlights trust erosion in financial institutions, relevant to user trust in PFMS."
  contribution: "This study provides empirical evidence that financial attitude mediates the literacy-behavior link, which can directly inform Odin's behavioral profiling module by emphasizing attitudinal drivers over knowledge alone. It also highlights the importance of institutional trust and crisis context, offering insights for Odin's user trust and engagement strategies. The methodological approach using SEM provides a template for evaluating multi‑factor behavioral models within a PFMS. Finally, the findings on FinTech adoption's weaker effect in fragile economies suggest that Odin's design should prioritize attitudinal and cognitive interventions over purely technological features."
  directly_justifies:
    - "Financial literacy alone is insufficient without attitudinal reinforcement to improve financial behavior."
    - "FinTech adoption positively influences financial behavior, but its effect is weaker in crisis contexts."
    - "Financial attitude is the strongest predictor of millennial financial behavior."
    - "In crisis settings, psychological and attitudinal mechanisms amplify over rational knowledge."
  limits:
    - "Cross‑sectional design prevents causal inference and tracking of behavioral changes over time."
    - "Self‑reported measures may be biased by social desirability and perceived versus actual behavior."
    - "Sample may not be representative of all Lebanese millennials, limiting generalizability."
    - "Excludes crisis‑specific constructs such as institutional trust and perceived financial risk [unacknowledged]."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to Behavioral Profiling (5.A) because it directly models financial behavior and attitudes, providing empirical support for attitudinal mediation. It also informs Existing Systems & Gaps (4.A, 4.B) through its discussion of FinTech adoption and identified limitations like financial illiteracy and trust erosion, with 4.B rated medium and 4.A low due to limited PFMS specificity. User Trust (10.B) was rated medium given the emphasis on trust in the financial system. The paper touches on Financial Behavior (1.C) but only contextually, as the population is Lebanese rather than Filipino. Other domains—Expense Categorization, Spending Forecasting, Budget Recommendation, Anomaly Detection, Mobile‑First Design, Engagement, Evaluation, and Savings/Debt Management—were considered and rejected because the paper does not address algorithmic or design‑specific aspects of these areas. Overall, the paper provides robust behavioral evidence that can guide Odin's profiling and trust‑building features, though it is not directly transferable to Filipino cultural specifics."
limitations:
  - "Cross‑sectional design prevents causal inference and tracking of behavioral changes over time."
  - "Self‑reported measures may be biased by social desirability and perceived versus actual behavior."
  - "Sample may not be representative of all Lebanese millennials, limiting generalizability."
  - "Excludes crisis‑specific constructs such as institutional trust and perceived financial risk [unacknowledged]."
remember_this:
  - "Financial attitude mediates the link between literacy and financial behavior."
  - "FinTech adoption improves behavior but less than literacy in crisis contexts."
  - "Financial attitude has the largest effect size (β = 0.414) on behavior."
  - "Financial literacy strongly shapes attitudes (β = 0.681), which then drive behavior."
  - "In unstable economies, psychological factors outweigh cognitive knowledge in predicting behavior."
```
---

## Paper 4: Reena & Murugesan_summarized.md

**Source File:** `Reena & Murugesan_summarized.md`

```yaml
paper_id: e2f3a7b1-8c4d-4a9f-9b3e-7d2c1f6a8b4e
designation: international
title: EFFECT OF SUBSCRIPTION CULTURE ON CONSUMER SPENDING PATTERNS
authors: Reena, R.; Murugesan, S.
year: 2026
venue: International Research Journal of Education and Technology
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.B
  - 7.A
  - 11.A
  - 11.B
  - 13.A
tldr: Subscription culture significantly influences consumer spending behavior, particularly among young consumers, by encouraging recurring payments that can increase monthly expenditures and reduce financial awareness.
problem_and_motivation: The rapid expansion of subscription-based services has changed traditional purchasing behavior, yet there is limited understanding of how these services influence consumer spending patterns and financial management. Understanding this effect is important for addressing potential issues like unnoticed spending and reduced budgeting awareness.
approach:
  - The study adopted a descriptive research design using a structured questionnaire distributed via Google Forms to collect primary data.
  - Secondary data was obtained from journals, articles, and websites related to subscription-based business models and consumer behavior.
  - A convenience sampling technique was used to collect responses from 100 respondents from different age groups.
  - The collected data was analyzed using percentage analysis, one-way ANOVA, and correlation analysis.
findings:
  - num: The majority of respondents belong to the 18-23 age group and are students, indicating high subscription service adoption among young consumers.
  - OTT and entertainment subscriptions are the most commonly used services, with most respondents using one or two subscription services.
  - Convenience and exclusive access are the primary reasons for choosing subscription services.
  - Many consumers sometimes forget their total subscription spending, leading to unexpected charges due to automatic renewals.
  - Some respondents reported difficulty in cancelling subscriptions, which may contribute to continued spending.
  - Subscription fatigue influences consumers to avoid new subscriptions.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Subscription Culture
    definition: The trend of consumers preferring recurring payment models for access to goods and services over one-time purchases.
  - term: Subscription Fatigue
    definition: The feeling of being overwhelmed by the number of subscriptions, leading to avoidance of new ones.
  - term: OTT
    definition: Over-the-top, referring to streaming services that deliver content directly over the internet.
critical_citations:
  - "[Bray et al., 2021] — Identified major factors motivating subscription adoption."
  - "[Iyengar and Park, 2020] — Found subscription increases purchase frequency."
  - "[Baek and Kim, 2022] — Concluded subscription models increase purchase intention."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Paper focuses on young consumers (18-23), a key demographic for Odin.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Discusses how subscriptions form a regular part of monthly expenses, impacting financial structure.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly examines spending behavior and financial management among young consumers.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: Subscription payments are recurring, creating a cyclical spending pattern relevant to this topic.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Findings on cumulative subscription costs and financial awareness inform budgeting strategies.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: Provides general context on consumer engagement with subscription platforms.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: contextual
      justification: Mentions convenience and perceived value as factors, but focuses on consumer behavior, not design.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: Suggests subscription spending may reduce savings awareness, a tangential link.
  contribution: The paper provides empirical evidence on how subscription culture influences consumer spending behavior, which can inform Odin's design for expense categorization and forecasting. It highlights that young consumers often underestimate cumulative subscription costs, justifying the need for a system that provides clear spending visibility and budgeting tools. The findings on auto-renewal issues and cancellation difficulties support features for transaction monitoring and alerting. The identification of subscription fatigue suggests that Odin could benefit from engagement strategies that help users manage subscription clutter. Overall, the study offers insights into the behavioral patterns that Odin aims to address.
  directly_justifies:
    - "Subscription services form a regular part of monthly expenses for young consumers."
    - "Consumers often forget total subscription spending, leading to unexpected charges."
    - "Difficulty in cancelling subscriptions can contribute to continued spending."
  limits:
    - "Study uses a small sample size of 100 respondents from a convenience sample, limiting generalizability."
    - "The correlation between subscription usage and increased spending was found to be weak, suggesting a nuanced relationship."
    - "The study focuses on general consumer behavior, not specifically on Filipino young professionals, which may reduce direct applicability."
    - "Lacks a detailed analysis of specific algorithmic or system design implications for a PFMS."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant for domains concerning Filipino Cultural Context (specifically 2.B on seasonal/cyclical spending), Expense Categorization (3.A, 3.B), Behavioral Profiling (1.A, 1.C), Budget Recommendation (7.A), and User Retention (11.A, 11.B). Topic codes 1.A and 1.C were assigned 'high' relevance as the paper directly studies the spending behavior of young consumers, a core demographic for Odin. Topic 2.B received 'medium' relevance due to the recurring nature of subscription payments creating predictable spending cycles. Topic 7.A was also 'medium' as the findings on cumulative costs and awareness are directly relevant to budgeting. Codes like 11.A and 11.B were considered 'low' or 'contextual' as the paper discusses engagement with subscription platforms but does not provide specific design insights for financial management applications. Domains such as Expense Categorization, Anomaly Detection, and Data Privacy were considered and rejected as the paper does not address these specific technical or system design concerns. Overall, the paper provides moderate relevance to Odin by offering behavioral insights into subscription spending patterns among young consumers, which can inform several functional modules.
limitations:
  - "Small sample size (n=100) limits the generalizability of findings."
  - "Convenience sampling may introduce selection bias."
  - "The study relies on self-reported data, which may be subject to recall bias."
  - "Focuses on general consumers rather than specifically Filipino young professionals, limiting direct applicability to Odin's target user base [unacknowledged]."
remember_this:
  - "Young consumers aged 18-23 show the highest subscription adoption."
  - "Convenience is the primary driver for choosing subscription services."
  - "Many consumers forget their total monthly subscription spending."
  - "Automatic renewals often cause unexpected charges for users."
  - "Subscription fatigue leads consumers to avoid new services."
```
---

## Paper 5: Ma C. et al_summarized.md

**Source File:** `Ma C. et al_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international
title: Consumers semi-intertemporally make intertemporal decisions: insights from the payday effects
authors: Ma, C.; Gu, Y.; Chong, J. K.
year: 2026
venue: Unknown
odin_topics:
  - 2.D
  - 4.A
  - 5.A
  - 6.A
  - 7.A
  - 10.B
tldr: Consumers without liquidity constraints self-impose monthly mental budgets renewed on paydays, leading to predictable spending cycles that decrease over trips until the next payday.
problem_and_motivation: Traditional economic models assume rational long-horizon intertemporal utility maximization, but consumers are neither fully rational nor completely myopic. The gap is understanding how consumers with no liquidity constraints actually make intertemporal spending decisions, particularly regarding storable goods.
approach:
  - Analyzed individual-level transaction data from a global cosmetic retail chain in a Southeast Asian country from 2011-2015, covering 300 stores and 600,000 members.
  - Employed regression discontinuity design with customer-day-level and trip-level regressions to isolate payday effects.
  - Controlled for customer fixed effects, store fixed effects, year, month, day-of-week, public holidays, and daily discount rates.
  - Compared cash versus credit card users to disentangle liquidity from behavioral effects.
  - Examined multiple dependent variables: expenditure, basket size, new product adoption, product upgrading, and purchase mistakes.
findings:
  - num: Payday shifts up unconditional daily expenditure by 4.7% for all members, driven by higher spending conditional on shopping (3.3% increase per trip) rather than increased shopping likelihood.
  - num: Credit card users show larger payday expenditure jumps (3.7%) than cash users (2.3%), disconfirming liquidity constraint explanations.
  - num: Per-trip expenditures decrease over subsequent trips within a paycheck cycle, with the first post-payday trip being significantly larger even when it occurs on a non-payday.
  - num: Expenditure on the first trip is dramatically larger if it falls on the payday versus one day after, indicating a salience effect beyond mental budget renewal.
  - num: Payday increases probability of purchasing a new variety by 0.63% and mistake probability (never-purchased-again variety) by 1.08%.
  - num: Payday effect shifts up daily consumption rate of the brand by US$0.0212 relative to a mean of US$0.263.
  - num: Mental budget renewing contributes 55% (credit card) and 75% (cash) of payday expenditure elevation; salience contributes the remainder.
  - Projection bias is triggered by salience but not by mental-budget renewing, as mistakes drop sharply from payday to day-after but do not decrease over trips.
key_figures_tables:
  - Figure 1: Unconditional daily expenditure shows a sudden spike at payday (day 0) across all members, credit card, and cash users → Payday increases spending even when including non-shopping days.
  - Figure 2: Conditional-on-visit expenditure spikes at payday → The payday effect is driven by larger purchases when shopping, not by more frequent shopping.
  - Figure 3: Panels A-D show payday increases variety seeking, new-product trying, upgrading to premium products, and daily consumption rate → Real economic impact beyond stockpiling.
  - Figure 5: First-trip expenditure drops sharply from payday to day-after, then remains flat → Salience effect distinct from mental budget renewal.
key_equations:
  - equation: ݕ = ߛ + ߛ ܫ(߬ ≥ 0) + ݂(߬ ) + ߚܺ + ߝ
    explanation: Regression discontinuity design isolating payday effect on daily expenditure.
  - equation: ܷ(݁) = ((1−ߜ௧̅)/(1−ߜ)) ݑ(݁/ݐ̅)
    explanation: Present value of utility from a storable product purchase.
  - equation: max ܷ(݁) + ݃(ℎ − ݁)
    explanation: Consumer maximizes utility from purchase plus pain of depleting mental budget.
definitions:
  - term: Mental Accounting
    definition: Consumers group expenditures into separate budgets (periodic or bracket-specific) rather than treating money as fully fungible.
  - term: Salience
    definition: Payday event draws attention and reduces self-control, causing overspending.
  - term: Projection Bias
    definition: Consumers overestimate how much future tastes will resemble current tastes, leading to purchase mistakes.
  - term: Mental Budget Renewal
    definition: Paycheck receipt resets the monthly spending limit consumers impose on themselves.
critical_citations:
  - "[Amador et al., 2006] — Optimal commitment imposes minimum savings per period."
  - "[Heath & Soll, 1996] — Foundational work on mental budgeting and fungibility."
  - "[Huffman & Barenstein, 2005] — Proposed monthly mental budgeting for credit card users."
  - "[Thaler, 1985] — Transaction utility and mental accounting theory."
relevance:
  topics:
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: high
      justification: Directly examines monthly paycheck cycles and spending patterns relevant to Filipino cultural payday practices.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Provides evidence that users impose their own mental constraints even without system support, informing baseline behavior.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Demonstrates distinct consumer profiles (cash vs. credit card) with different behavioral susceptibilities.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Spending patterns are predictable by trip count within a paycheck cycle, directly informing forecasting.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Reveals that consumers naturally use rule-of-thumb mental budgets, validating domain assumptions for recommendation systems.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: contextual
      justification: Relates to psychological mechanisms of self-control and commitment, indirectly relevant to trust in system recommendations.
  contribution: The paper provides empirical evidence for monthly mental budgeting behavior among consumers without liquidity constraints, which directly informs Odin's budget recommendation module by validating that users naturally think in monthly cycles. It identifies salience and projection bias as critical behavioral factors that cause overspending on paydays, suggesting Odin should incorporate payday-aware alerts and reminders. The cash vs. credit card user differences imply Odin should tailor interventions based on payment method profiles to maximize effectiveness. The finding that per-trip spending decreases over trips within a cycle indicates Odin's spending forecasting should track trip frequency, not just calendar days. Finally, the evidence that consumers allocate expenditures into bracket-specific mental accounts supports Odin's expense categorization and category-level budgeting features.
  directly_justifies:
    - "Consumers without liquidity constraints self-impose monthly mental budgets, supporting Odin's default monthly budgeting paradigm."
    - "Payday salience causes overspending, justifying Odin's payday-specific alerts and nudges."
    - "Per-trip expenditure decreases over trips within a paycheck cycle, informing Odin's spending forecasting models."
    - "Cash users are less susceptible to behavioral biases, suggesting Odin should offer different intervention strategies by payment type."
    - "Projection bias from salience leads to purchase mistakes, supporting Odin's post-purchase reflection and learning features."
  limits:
    - "The sample consists of upper-middle-class consumers in a Southeast Asian country, which may not generalize to all Filipino young professionals."
    - "The study focuses on a single cosmetic retail chain, so findings may not extend to essential goods or broader spending categories."
    - "Cash vs. credit card user differences could be confounded by income or financial sophistication rather than payment method alone."
    - "The data predates widespread mobile payment adoption, which may affect salience effects in contemporary users. [unacknowledged]"
  mapping_rationale: The systematic scan across all 12 functional domains and their associated topic codes identified that this paper directly addresses consumer spending cycles (2.D), behavioral profiling (5.A), spending forecasting (6.A), budget recommendation domain knowledge (7.A), and system landscape (4.A). The high relevance assignments for 2.D, 5.A, 6.A, and 7.A are justified by the paper's rigorous empirical documentation of predictable monthly spending cycles, consumer self-imposed mental budgets, and payday-triggered behavioral patterns that directly inform Odin's algorithmic modules. The paper was considered and rejected for topics 3.A, 3.B, 3.C, and 7.B-D because it does not address categorization frameworks, allocation constraints, or optimization approaches for budget recommendations. It was also rejected for 8.A-C, 9.A-B, 10.A, 11.A-B, 12.A-C, and 13.A-C due to lack of coverage of anomaly detection, mobile UX, privacy, engagement, evaluation, or savings/debt management. The borderline case of user trust (10.B) was assigned contextual relevance because the psychological mechanisms described (self-control, commitment) indirectly relate to trust in system recommendations but are not directly studied. Overall, the paper has high relevance for Odin's core behavioral modeling and budget recommendation domains.
limitations:
  - "The sample consists of upper-middle-class consumers, limiting generalizability to lower-income Filipino young professionals."
  - "The study examines a single retail chain selling storable products, so findings may not extend to essential goods or overall spending."
  - "The data is from a Southeast Asian country and may not fully reflect Filipino cultural spending nuances."
  - "Cash vs. credit card differences may be confounded by unobserved income or financial literacy differences. [unacknowledged]"
  - "The study does not account for the impact of modern fintech like mobile payments on payday behaviors. [unacknowledged]"
remember_this:
  - "Consumers impose monthly mental budgets even without liquidity constraints."
  - "Payday salience, not just renewal, drives spending overshoots."
  - "Per-trip spending decreases predictably over trips within a paycheck cycle."
  - "Credit card users are more susceptible to payday behavioral biases than cash users."
  - "num: Mental budget renewal explains 55-75% of payday spending increases."
```
---

## Paper 6: Ashta_summarized.md

**Source File:** `Ashta_summarized.md`

```yaml
paper_id: 8a7f4e3d-2b1c-4a5d-9e8f-0a1b2c3d4e5f
designation: international
title: Artificial Intelligence in Microfinance and Financial Inclusion: Applications, Issues, and Future Directions
authors: Ashta, A.
year: 2026
venue: Unknown
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 12.A
tldr: AI enables financial inclusion through alternative credit scoring, automated underwriting, and personalized savings, but risks algorithmic bias, proxy discrimination, privacy violations, and digital exclusion.
problem_and_motivation: Two billion adults lack access to formal financial services due to credit invisibility and high operational costs. Traditional systems fail to serve marginalized populations without formal credit histories. AI offers a potential solution by leveraging alternative data and automation to expand access.
approach:
  - A critical review of peer-reviewed articles, working papers, and reports from organizations like the World Bank and CGAP was conducted.
  - The analysis includes multiple purposively selected case studies from the Global South, such as M-Pesa, Tala, Branch, BIMA, and Pula.
  - The BHAI framework is adopted as an interpretative-constructivist lens to guide the assessment of AI's role in microfinance.
  - The study examines AI applications across payments, savings, lending, insurance, and investments.
  - The paper identifies recurring patterns, operational challenges, and ethical dilemmas from the case studies.
  - The paper synthesizes findings to highlight both the potential and risks of AI for financial inclusion.
  - It incorporates quantitative evidence, such as default rate reductions and cost savings from AI implementations.
findings:
  - num: Alternative data models achieve correlations of 0.65 to 0.72 between payment consistency and loan repayment, matching FICO performance.
  - num: Machine learning for alternative credit scoring reduces default rates and can lower operational costs by 6% to 25% of total losses.
  - num: AI-driven underwriting reduces decision-making costs from hundreds of dollars to pennies and processes loans in minutes instead of weeks.
  - Alternative data can encode existing societal inequalities, leading to proxy discrimination against marginalized groups.
  - AI-powered behavioral nudges can increase savings engagement but risk becoming manipulative dark patterns.
  - Supervised learning, particularly gradient boosting, dominates 70-80% of production systems for alternative credit scoring.
  - Deep learning is deployed for unstructured data like biometrics and damage assessment in payments and insurance.
  - Reinforcement learning is less common, used mainly for optimization in payment routing, pricing, and portfolio management.
  - There is an "inclusion paradox" where AI enables access to financial services, but often at exploitative terms for vulnerable populations.
  - AI-driven financial inclusion faces critical challenges, including bias, privacy violations, lack of transparency, and cultural insensitivity.
key_figures_tables:
  - Table 1: Behavioral finance nudges in digital savings → AI can operationalize nudges through predictive analytics and automated savings plans.
  - Table 2: Traditional versus Alternative Data → Alternative data includes mobile money, utility payments, and behavioral analytics for credit scoring.
  - Table 3: AI Technologies by Financial Sector → Supervised learning dominates, with gradient boosting for credit scoring and CNNs for biometrics and damage assessment.
  - Table 4: Humane Considerations by Financial Sector → All sectors face challenges like algorithmic bias, privacy violations, and lack of transparency.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: Artificial Intelligence (AI)
    definition: Computer systems that can perform tasks typically requiring human intelligence such as pattern recognition, decision-making, and language understanding.
  - term: Machine Learning
    definition: A subset of AI where algorithms improve automatically through experience.
  - term: Supervised Learning
    definition: Training algorithms on labeled datasets where the correct answer is known.
  - term: Unsupervised Learning
    definition: Discovering hidden patterns in data without pre-labeled examples.
  - term: Reinforcement Learning
    definition: Algorithms learn optimal strategies through trial and error with rewards for successful actions.
  - term: Natural Language Processing (NLP)
    definition: Technology enabling computers to understand and generate human language.
  - term: Computer Vision
    definition: AI systems that can 'see' and interpret images.
  - term: Alternative Data
    definition: Non-traditional data sources such as mobile phone usage, e-commerce history, utility payments, and social network data.
  - term: Gradient Boosting
    definition: Ensemble methods combining multiple decision trees, like XGBoost and LightGBM, effective for alternative credit scoring.
  - term: Deep Learning
    definition: Uses interconnected layers of algorithms (neural networks) to learn from large amounts of data.
  - term: Parametric Insurance
    definition: Coverage that pays out automatically when specific measurable events occur.
  - term: Robo-Advisor
    definition: Automated platforms providing financial planning and investment management.
  - term: Proxy Discrimination
    definition: Using variables that correlate with protected characteristics as a substitute for those attributes.
  - term: Digital Divide
    definition: The gap between those who have access to digital technologies and those who do not.
  - term: BHAI Framework
    definition: A framework advocating for humane AI development through multidimensional inclusion, ethical oversight, and contextual sensitivity.
  - term: Credit Invisibility
    definition: Individuals with no footprint in conventional credit bureaus, lacking formal credit history.
critical_citations:
  - "[Consumer Financial Protection Bureau, 2015] — Documents 45 million credit-invisible adults in the U.S."
  - "[Björkegren & Grissen, 2019] — Demonstrates mobile phone data predicts credit repayment."
  - "[Berg, Burg, Gombović, & Puri, 2019] — Shows ML reduces default rates in fintech lending."
  - "[S. Barocas & Selbst, 2016] — Analyzes proxy discrimination in algorithmic systems."
  - "[Zuboff, 2019] — Critiques surveillance capitalism and data commodification."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Discusses transaction analysis for fraud detection and personalization.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: low
      justification: Mentions personalized payment options but does not focus on category design.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Reviews major fintech systems and AI applications globally.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Critically assesses limitations like bias, privacy, and exclusion in current systems.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Uses behavioral nudges and segmentation based on transaction patterns.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: low
      justification: Addresses the cold-start problem through alternative data for new users.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses clustering and classification for user segmentation and fraud detection.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Discusses forecasting for credit risk, savings, and market movements.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Mentions time-series forecasting (ARIMA, LSTM) for income and spending prediction.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Discusses automated savings and goal-based trackers as budgeting strategies.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Touches on personalized savings recommendations but not explicit budget allocation.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Describes real-time fraud detection as a core application in payments.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Mentions supervised and unsupervised learning for detecting transaction anomalies.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Extensively covers privacy violations, data breaches, and surveillance concerns.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Discusses building trust through security, transparency, and recourse mechanisms.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Calls for fairness audits, impact assessments, and outcome-based evaluation.
  contribution: The paper provides a broad overview of AI applications in financial inclusion, directly relevant to Odin's core domains of expense analysis, forecasting, and anomaly detection. It offers a critical lens on the limitations of existing systems and highlights the importance of user privacy and trust. The detailed discussion on algorithmic bias and fairness directly informs Odin's design to ensure equitable financial management. The paper's case studies of Global South fintech implementations offer practical insights for Odin's contextual relevance.
  directly_justifies:
    - Odin must be designed with fairness-aware machine learning to avoid perpetuating proxy discrimination.
    - Alternative data and predictive modeling require transparency to allow users to challenge automated decisions.
    - User trust is foundational for retention and engagement, requiring clear communication and ethical data handling.
    - Anomaly detection systems must adapt to evolving spending patterns to effectively flag fraud and irregularities.
  limits:
    - The review is non-systematic, which may introduce selection bias in the case studies chosen.
    - The paper does not provide a deep technical analysis of specific algorithms but rather a high-level overview.
    - The analysis is based on existing literature and may not capture the most recent developments in AI.
    - The paper focuses on the Global South, which may limit the direct applicability of specific case studies to Odin's Filipino context.
  mapping_rationale: The systematic scan of the 12 functional domains identified the paper as highly relevant to Predictive Modeling (6.A/6.B) and Anomaly Detection (8.A/8.B), due to its extensive coverage of alternative credit scoring, forecasting algorithms, and fraud detection systems. It also shows high relevance to Data Privacy & Trust (10.A/10.B) and Existing Systems & Gaps (4.A/4.B), with detailed discussions on ethical challenges and system limitations. Medium relevance was assigned to domains like Expense Categorization (3.A/3.B) and Behavioral Profiling (5.A/5.C), as these are secondary themes informing the core predictive applications. Domains like Mobile-First Design (9.A/9.B) and Savings/Debt Management (13.A/13.B) were considered but rejected as the paper lacks specific focus on these areas. Borderline cases included seasonal spending (2.B), which is implicitly addressed through income volatility modeling, and user-defined constraints (3.C, 7.B), which are not central to the paper's argument. The paper is highly relevant to Odin as it provides both the technological justification and the critical ethical framework necessary for building a responsible PFMS.
limitations:
  - The review is non-systematic, potentially introducing selection bias in case studies.
  - The paper does not provide deep technical analysis of specific algorithms but a high-level overview.
  - The analysis is based on existing literature and may not capture the most recent AI developments.
  - The focus on the Global South may limit direct applicability of specific case studies to Odin's Filipino context. [unacknowledged]
remember_this:
  - Alternative data correlates with creditworthiness at rates comparable to traditional FICO scores.
  - AI-driven underwriting reduces costs from hundreds of dollars to pennies per loan.
  - Algorithmic bias can create proxy discrimination without explicitly using protected attributes.
  - Financial inclusion via AI risks becoming exploitation if deployed without adequate ethical oversight.
  - Success requires prioritizing human dignity and transparent governance over efficiency metrics.
```
---

## Paper 7: Gong_summarized.md

**Source File:** `Gong_summarized.md`

```yaml
paper_id: 10.1051/itmconf/20268402004
designation: international
title: Research Progress and Trends of Deep Learning in Stock Price Prediction: A Systematic Review from LSTM to Transformer
authors: Gong, H.
year: 2026
venue: ITM Web of Conferences
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
tldr: A systematic review of deep learning models for stock prediction, tracing the evolution from LSTM to Transformer and hybrid architectures, with empirical comparisons and future research directions.
problem_and_motivation: Stock price prediction remains challenging due to high volatility and non-linearity, and traditional methods are insufficient. Deep learning models like LSTM and Transformer have shown promise, but a comprehensive review linking their evolution from LSTM to hybrid architectures is lacking. This review aims to systematically summarize these methods, compare their performance, and identify challenges and future trends.
approach:
  - Systematically reviews the evolution of stock prediction models from RNNs and LSTM to Transformer and hybrid architectures.
  - Classifies and analyzes mainstream deep learning models, detailing their characteristics, advantages, and limitations.
  - Compares empirical studies on different datasets, focusing on evaluation metrics like RMSE, MAE, and Sharpe Ratio.
  - Discusses current challenges in data, model, and deployment, and proposes future research directions.
  - Synthesizes findings from prior research to provide a complete technical roadmap for applying deep learning to stock price prediction.
findings:
  - num: LSTM achieved a 0.46% daily return on S&P 500 constituents, outperforming DNN (0.32%) and logistic regression (0.26%).
  - num: LSTM generated trading signals with a Sharpe ratio up to 2.34, while other models were far less than 1.0.
  - num: Transformer models reduced MAE by 20.73%, MSE by 34.84%, and MAPE by 25.63% compared to LSTM in some studies.
  - num: The LSTM-Transformer hybrid model showed MAE and RMSE reductions of over 50% compared to the parent models.
  - num: The hybrid model achieved an R² value of 0.9618, higher than LSTM (0.8430) and Transformer (0.7763).
  - LSTM is advantageous for short-term prediction and generating trading signals with high Sharpe ratios.
  - Transformer excels in long-range dependency and cross-asset modeling, improving overall prediction accuracy.
  - The evolution of models shows a trend towards hybrid and multimodal fusion for better performance and interpretability.
key_figures_tables:
  - "Table 1: Summary of evaluation criteria (RMSE, MAE, MAPE, DA, R2, Sharpe Ratio) used in empirical studies."
  - "Table 2: Comparison of empirical results for LSTM, Transformer, and hybrid models, showing performance metrics and improvements."
  - "Figure 1: Schematic diagram of the Transformer architecture, highlighting its self-attention mechanism for time series prediction."
  - "Figure 2: Framework of the LSTM-Transformer dual-branch hybrid model for stock price prediction."
  - "Figure 3: Trends in deep learning model evolution for stock prediction, from LSTM to multimodal fusion models."
key_equations:
  - equation: "MAE = \\frac{1}{n} \\sum_{i=1}^{n} |y_i - \\hat{y}_i|"
    explanation: "Average absolute error between predicted and actual values."
  - equation: "RMSE = \\sqrt{\\frac{1}{n} \\sum_{i=1}^{n} (y_i - \\hat{y}_i)^2}"
    explanation: "Square root of average squared errors, sensitive to large deviations."
  - equation: "Sharpe Ratio = \\frac{R_p - R_f}{\\sigma_p}"
    explanation: "Risk-adjusted return, higher values indicate better performance."
definitions:
  - term: "LSTM"
    definition: "Long Short-Term Memory, an RNN variant with gating mechanisms to handle long-term dependencies."
  - term: "Transformer"
    definition: "Model architecture using self-attention mechanisms for processing sequences, avoiding recurrence."
  - term: "MAE"
    definition: "Mean Absolute Error, measures average magnitude of errors."
  - term: "RMSE"
    definition: "Root Mean Square Error, measures error magnitude with a higher penalty for large errors."
  - term: "Sharpe Ratio"
    definition: "Metric for risk-adjusted return, calculated as excess return over risk-free rate per unit of volatility."
critical_citations:
  - "[Fischer & Krauss, 2018] — LSTM outperforms memoryless models in predicting S&P 500 returns."
  - "[Wang et al., 2022] — Transformer model shows significant error reduction compared to LSTM."
  - "[Zhao et al., 2025] — LSTM-Transformer hybrid model achieves superior performance over parent models."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Reviews predictive models applicable to financial forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Systematically evaluates LSTM, Transformer, and hybrid models for time series forecasting.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Discusses challenges like data noise and overfitting relevant to anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: Mentions CNN for feature extraction and noise filtering, relevant to detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Compares models using standard metrics like RMSE, MAE, and Sharpe Ratio.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides empirical comparisons and performance benchmarks for various deep learning modules.
  contribution: "This review provides a comprehensive benchmarking of time series forecasting models, offering a direct evaluation framework for Odin's predictive modules. The empirical comparisons of LSTM and Transformer models, including their hybrid variations, justify the choice of foundational algorithms for spending forecasting. The detailed analysis of model strengths (e.g., LSTM for short-term patterns) and weaknesses (e.g., Transformer's computational cost) informs architectural decisions. The identified challenges, such as overfitting and interpretability, align with Odin's design constraints for a robust and trustworthy system."
  directly_justifies:
    - "LSTM is a reliable benchmark for medium and short-term prediction tasks."
    - "Transformer models provide better prediction accuracy, with lower MAE, MSE, and MAPE."
    - "Hybrid LSTM-Transformer models achieve higher accuracy and stability than parent models."
    - "The choice of evaluation metrics (RMSE, MAE, DA) is critical for assessing prediction models."
    - "Interpretability and computational efficiency are key challenges for deploying deep learning in finance."
  limits:
    - "The review does not propose a new model or application in personal finance."
    - "Findings are based on stock market data and may not directly transfer to spending data."
    - "Lacks specific guidance on handling cold-start problems in personal finance systems."
  mapping_rationale: "A systematic scan across all 12 functional domains and 43 topic codes was conducted. Domains most relevant to this paper are Spending Forecasting (6.A, 6.B) and System Evaluation (12.A, 12.B) due to its focus on predictive modeling and empirical performance comparisons. The paper also provides contextual value for Anomaly Detection (8.A, 8.B) through discussions on data noise. Topics related to Filipino Cultural Context, Expense Categorization, and Behavioral Profiling were considered but rejected as the paper is a general technical review without specific application to personal finance or Filipino users. The relevance is high for forecasting algorithms and evaluation frameworks, medium for predictive modeling, and contextual for anomaly detection. Overall, the paper's strength lies in its comprehensive review of forecasting techniques and evaluation metrics, making it highly relevant for designing and assessing Odin's algorithmic modules."
limitations:
  - "The review focuses on stock price prediction, not personal spending forecasting. [unacknowledged]"
  - "Does not address the cold-start problem or how to profile users with limited data. [unacknowledged]"
  - "Limited discussion on mobile-first design or user trust implications. [unacknowledged]"
  - "The paper is a review and does not introduce a novel algorithm or empirical dataset. [unacknowledged]"
remember_this:
  - "LSTM excels in short-term prediction and generating high Sharpe ratio trading signals."
  - "Transformer models reduce prediction errors by over 20% compared to LSTM."
  - "Hybrid LSTM-Transformer models can reduce MAE and RMSE by more than 50%."
  - "Deep learning models outperform traditional methods in financial time series forecasting."
  - "Interpretability and real-time adaptation remain critical challenges for deployment."
```
---

## Paper 8: Chahar et al_summarized.md

**Source File:** `Chahar et al_summarized.md`

```yaml
paper_id: "6ba7b810-9dad-11d1-80b4-00c04fd430c8" # UUIDv5 generated from title
designation: "international" # Non-algorithmic, non-Philippine specific
title: "Artificial Intelligence Powered Personal Finance Management System"
authors: "Chahar, P.; Vishwakarma, Y. K.; Mishra, R.; Paliwal, G."
year: 2026
venue: "Unknown"
odin_topics:
  - "3.A"
  - "4.A"
  - "4.B"
  - "6.A"
  - "7.A"
  - "7.B"
  - "8.A"
  - "10.A"
  - "10.B"
  - "13.A"
tldr: "Proposes an AI-powered PFMS using ML and NLP for dynamic budget recommendations, financial education, and secure data handling to address limitations of static tools."
problem_and_motivation: "Individuals face challenges managing complex finances due to limited literacy and inadequate static budgeting tools. Existing systems lack adaptability, personalization, and predictive capabilities. There is a pressing need for intelligent, automated systems that can provide dynamic and personalized financial insights."
approach:
  - "Conducted a systematic literature review of existing PFMS, ML classification, predictive forecasting, and recommendation systems."
  - "Proposed a modular architecture with components for data collection, expense classification, predictive analytics, recommendations, and NLP interface."
  - "Designed a web-based prototype using React.js for frontend, Flask for backend ML operations, MongoDB for database, and Firebase for authentication."
  - "Evaluated the prototype's performance using metrics like accuracy, precision, MAE, and F1-score, alongside user satisfaction surveys."
  - "The expense classification engine employs supervised ML (Random Forest, SVM, LSTM) and uses techniques like TF-IDF and word embeddings."
findings:
  - "num: The system achieved high user satisfaction with a rating of 4.4/5 overall."
  - "num: Convenience of use received an average score of 4.5/5."
  - "num: Correctness of transaction categorization was rated at 4.2/5."
  - "num: Goal-setting functionality was rated at 4.3/5."
  - "The system effectively categorized transactions and provided relevant financial advice for users with stable incomes."
  - "Recorded data quality, especially incomplete or inaccurate transactions, negatively impacted the reliability of predictions and recommendations."
key_figures_tables:
  - "Figure 4: Data flow diagram shows the system architecture from data input to report generation."
  - "Figure 6: Distribution of Expenses across Transaction Types illustrates the categorization of spending."
  - "Table 1: Summary of AI-powered finance management tools like Mint, YNAB, Digit, and Tally."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "NLP"
    definition: "Natural Language Processing, used for user interaction via chatbots."
  - term: "LSTM"
    definition: "Long Short-Term Memory, a deep learning network for sequential text analysis."
  - term: "ML"
    definition: "Machine Learning, used for classification, forecasting, and personalization."
  - term: "PFMS"
    definition: "Personal Finance Management System."
critical_citations:
  - "[Zhang et al., 2007] — Used decision trees and SVM for transaction classification."
  - "[Siami-Namini et al., 2018] — Compared ARIMA and LSTM for forecasting spending patterns."
  - "[Luef et al., 2020] — Developed a recommender system for financial advice."
relevance:
  topics:
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "high"
      justification: "Paper details an ML-based expense classification engine using models like Random Forest and SVM."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews existing tools (Mint, YNAB) and their limitations, establishing context for the proposed system."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Directly addresses limitations of static, rule-based systems and the lack of personalization and adaptability."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Proposes a predictive analytics module using time series forecasting (ARIMA, LSTM) for proactive planning."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "medium"
      justification: "Discusses personal budgeting as a critical financial process and mentions strategies for budget adherence."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "high"
      justification: "System includes a recommendation module to generate personalized budgeting tips and advice."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Mentions anomaly detection for fraud and identity theft as a potential system capability."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "Dedicates a whole component to security measures, including encryption, anonymization, and compliance."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "medium"
      justification: "Identifies user trust as a key challenge for adoption and suggests explainability to build it."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "medium"
      justification: "The system's expected outcomes include helping users create budgets that facilitate saving."
  contribution: "This paper provides a high-level blueprint for an AI-driven PFMS that can justify Odin's modular design, specifically for modules like expense classification (Topic 3.A) and budget recommendation (Topic 7.B). Its systematic review of existing system limitations (Topic 4.B) directly supports the rationale for developing a more intelligent and adaptive solution. The emphasis on security and user trust (Topics 10.A, 10.B) validates Odin's commitment to data privacy as a core functional requirement. Furthermore, the positive user satisfaction metrics reported provide a benchmark for evaluating the success of a new PFMS. The paper's approach of combining ML, NLP, and a robust web framework offers a viable architecture for Odin's own implementation."
  directly_justifies:
    - "The proposed AI-powered assistant can deliver dynamic, user-specific financial insights."
    - "Integrating ML for expense classification and forecasting enhances financial management tools."
    - "Incorporating robust security mechanisms is essential for protecting sensitive user data."
    - "Personalized recommendations help users achieve financial goals and improve engagement."
  limits:
    - "The paper presents a proposal and preliminary prototype, lacking empirical validation of its core algorithms in a real-world setting."
    - "The proposed system's ability to handle irregular income streams is acknowledged as a limitation."
    - "Findings rely on a literature review and high-level architecture; detailed algorithmic performance data is absent."
  mapping_rationale: "A systematic scan across all 12 functional domains was performed. The paper was flagged as highly relevant to 'Existing Systems & Gaps' (4.A, 4.B) and 'Budget Recommendation' (7.A, 7.B) due to its clear identification of static tool limitations and its proposal of a recommendation module. It also shows high relevance to 'Expense Categorization' (3.A) and 'Data Privacy' (10.A, 10.B) because it details ML classification techniques and a dedicated security layer. Medium relevance was assigned to 'Predictive Modeling' (6.A) and 'Savings Management' (13.A) as these are mentioned but not deeply explored. The paper touches on 'Anomaly Detection' (8.A) and 'User Trust' (10.B), but these are brief discussions, hence a 'medium' relevance. Other domains like 'Filipino Cultural Context,' 'Mobile-First Design,' and 'User Retention' were considered but rejected as the paper does not address them. The paper's overall relevance to Odin is strong as it provides a comprehensive justification for an AI-driven PFMS, covers several key modules, and highlights critical implementation concerns like privacy."
limitations:
  - "The proposed system is a prototype and lacks real-world deployment validation. [unacknowledged]"
  - "Difficulty in handling users with irregular income patterns. [acknowledged]"
  - "Data quality issues can lead to less reliable predictions."
  - "Reliance on user survey data for success metrics, which may not directly correlate with algorithmic performance."
remember_this:
  - "An AI-powered PFMS requires ML for classification and NLP for user interaction."
  - "Static financial tools lack adaptability and personalization for modern users."
  - "Security and user trust are critical for the adoption of AI in personal finance."
  - "The proposed system's high user satisfaction (4.4/5) highlights the value of usability."
  - "Challenges remain in handling irregular income and maintaining data quality."
```
---

## Paper 9: Mienye et al-2026_summarized.md

**Source File:** `Mienye et al-2026_summarized.md`

```yaml
paper_id: "10.3390/info17040395"
designation: "international"
title: "Deep Learning for Credit Risk Prediction: A Survey of Methods, Applications, and Challenges"
authors: "Mienye, I. D.; Esenogho, E.; Modisane, C."
year: 2026
venue: "Information"
odin_topics:
  - "4.A"
  - "4.B"
  - "5.C"
  - "6.A"
  - "6.B"
  - "10.A"
  - "10.B"
tldr: "A systematic survey of deep learning architectures for credit risk prediction, covering MLP, CNN, RNN, Transformer, and GNN models across tabular, sequential, and relational borrower data."
problem_and_motivation: "Traditional credit risk models like logistic regression and tree-based ensembles struggle to capture nonlinearities, temporal dynamics, and relational dependencies in modern financial datasets. While deep learning offers a path forward, the review literature has lacked a unified synthesis that maps model families to data modalities and credit-risk objectives for borrower-level prediction."
approach:
  - "Searched IEEE Xplore, Scopus, ACM Digital Library, ScienceDirect, SpringerLink, Web of Science, and Google Scholar using credit-risk and deep learning keywords."
  - "Restricted to journal articles and conference papers from 2015 to 2025, with foundational earlier studies added via citation tracking."
  - "Screened 380 initial records through de-duplication, title/abstract screening, and full-text assessment to retain 140 application studies and 18 survey papers."
  - "Organised reviewed studies by model class: tabular MLP, sequential RNN/LSTM/GRU, CNN, Transformer, GNN, and hybrid architectures."
  - "Extracted data modality, architecture, credit product segment, prediction target, and evaluation metrics for each included study."
findings:
  - "num: MLPs with L1–L2 regularisation achieved 80.12% accuracy for corporate credit risk, outperforming logistic regression (AUC 0.717) and SVM (AUC 0.738)."
  - "num: LSTM networks reduced MAE from 0.095 to 0.072 and RMSE from 0.119 to 0.093 for monthly default rate forecasting versus ARIMA and SVM."
  - "num: TabNet-Stacking ensemble reached 97.9% accuracy and 0.941 AUC on a large-scale credit dataset with 800,000 cases."
  - "num: Residual-enhanced BiLSTM with multi-head attention achieved AUC 0.982 and F1 0.958 on the Freddie Mac Single-Family dataset."
  - "num: Weighted-loss TabTransformer increased accuracy on the German Credit dataset from 93% to 95% with SHAP-based explanations."
  - "num: Relational graph attention networks achieved AUC 0.799 and KS 0.528 for SME default prediction using shared-director and business-interaction graphs."
  - "Deep tabular models are competitive with tree-based ensembles on large datasets with high-cardinality categorical features but offer modest gains on small benchmarks."
  - "Sequential architectures like LSTM and GRU excel at dynamic behavioural scoring when rich post-origination histories are available."
  - "Transformers unify behavioural sequences, categorical embeddings, textual narratives, and graph-structured relationships within a single modelling interface."
  - "GNNs capture contagion and correlated risk in interconnected portfolios that tabular and sequential models cannot represent structurally."
key_figures_tables:
  - "Table 1: Summary of related reviews on credit risk modelling → Positions this survey as the first unified synthesis of DL model families for borrower-level credit risk."
  - "Figure 1: PRISMA flowchart of literature search and screening → Documents the systematic selection of 140 application studies and 18 survey papers."
  - "Figure 2: Basic structure of a feed-forward neural network for tabular credit data → Illustrates MLP architecture with hidden layers for default prediction."
  - "Figure 3: Architecture of the LSTM network showing gating mechanisms → Visualises forget, input, and output gates for long-term temporal pattern preservation."
  - "Figure 4: Architecture of the GRU network with update and reset gates → Shows simplified recurrent structure for efficient behavioural sequence modelling."
  - "Figure 5: Basic CNN architecture adapted for one-dimensional financial sequences → Depicts convolutional and pooling layers for local repayment pattern extraction."
  - "Figure 6: Message passing mechanism in a GNN for borrower networks → Illustrates neighbour aggregation for relational credit risk propagation."
  - "Table 2: Summary of benchmark datasets commonly used in credit risk prediction → Lists German Credit, Australian Credit, Taiwan Credit Card Default, Home Credit, and LendingClub datasets."
  - "Table 3: Summary of deep learning architectures for credit risk modelling → Compares MLP, CNN, RNN, Transformer, GNN, and hybrid models by mechanism, strengths, and limitations."
  - "Table 4: Summary of deep learning applications in credit risk prediction → Consolidates 25 peer-reviewed studies across tabular, sequential, transformer-based, and GNN-based models."
  - "Table 5: Challenges in deep learning credit risk modelling and aligned research directions → Maps evaluation integrity, imbalance, interpretability, robustness, and governance issues to emerging research directions."
key_equations:
  - equation: "EL = PD × LGD × EAD"
    explanation: "Expected loss decomposes into probability of default, loss given default, and exposure at default."
  - equation: "P(y=1|x) = σ(w^T x + b) = 1/(1 + exp(-w^T x - b))"
    explanation: "Logistic regression models default probability as a linear log-odds function."
  - equation: "h_t = ϕ(W h_{t-1} + U x_t + b)"
    explanation: "RNN hidden state update with nonlinear activation over sequential input."
  - equation: "f_t = σ(W_f [h_{t-1}, x_t] + b_f), i_t = σ(W_i [h_{t-1}, x_t] + b_i), C_t = f_t ⊙ C_{t-1} + i_t ⊙ C̃_t"
    explanation: "LSTM forget and input gates regulate memory cell updates for long-term dependencies."
  - equation: "Attention(Q,K,V) = softmax(QK^T / √d_k) V"
    explanation: "Scaled dot-product attention enables global dependency modelling across sequences or features."
  - equation: "h_v^{(l+1)} = σ(∑_{u∈N(v)} 1/c_{vu} W^{(l)} h_u^{(l)})"
    explanation: "GNN message passing updates borrower embeddings by aggregating neighbour representations."
definitions:
  - term: "AUC"
    definition: "Area under the receiver operating characteristic curve, a threshold-agnostic measure of ranking performance."
  - term: "AUPRC"
    definition: "Area under the precision-recall curve, sensitive to minority-class performance in imbalanced datasets."
  - term: "BiLSTM"
    definition: "Bidirectional long short-term memory network that processes sequences in both forward and backward directions."
  - term: "CNN"
    definition: "Convolutional neural network using shared-weight filters to extract local temporal or spatial patterns."
  - term: "DL"
    definition: "Deep learning, a subfield of machine learning using multi-layered neural networks for representation learning."
  - term: "EAD"
    definition: "Exposure at default, the total outstanding amount a lender is exposed to when default occurs."
  - term: "EL"
    definition: "Expected loss, the product of PD, LGD, and EAD used in regulatory capital calculations."
  - term: "GNN"
    definition: "Graph neural network, a model that learns representations by message passing over graph-structured relational data."
  - term: "GRU"
    definition: "Gated recurrent unit, a simplified recurrent architecture with update and reset gates for sequence modelling."
  - term: "LGD"
    definition: "Loss given default, the proportion of exposure not recovered after a borrower defaults."
  - term: "LR"
    definition: "Logistic regression, a linear model for binary classification with a sigmoid output."
  - term: "LSTM"
    definition: "Long short-term memory, a recurrent network with gating mechanisms for preserving long-range temporal dependencies."
  - term: "ML"
    definition: "Machine learning, algorithms that learn patterns from data without explicit programming."
  - term: "MLP"
    definition: "Multi-layer perceptron, a feed-forward neural network with multiple hidden layers and nonlinear activations."
  - term: "MLOps"
    definition: "Machine learning operations, practices for versioning, monitoring, and governing ML models in production."
  - term: "PD"
    definition: "Probability of default, the likelihood that a borrower fails to meet repayment obligations."
  - term: "RNN"
    definition: "Recurrent neural network, a model with cyclic connections for processing sequential data."
  - term: "RWA"
    definition: "Risk-weighted asset, a measure of asset risk used in Basel regulatory capital requirements."
  - term: "SHAP"
    definition: "SHapley Additive exPlanations, a game-theoretic approach for interpreting model predictions."
  - term: "SME"
    definition: "Small and medium enterprise, a business segment frequently targeted in credit risk studies."
  - term: "TCN"
    definition: "Temporal convolutional network, a dilated convolutional architecture for sequence modelling with parallel computation."
  - term: "XAI"
    definition: "Explainable artificial intelligence, methods for making model decisions interpretable to humans."
critical_citations:
  - "[LeCun et al., 2015] — Foundational paper establishing deep learning as a transformative approach."
  - "[Vaswani et al., 2017] — Introduced the Transformer architecture with self-attention for sequence modelling."
  - "[Lessmann et al., 2015] — Benchmarking study highlighting limitations of small public credit datasets."
  - "[Thomas et al., 2017] — Comprehensive text on credit scoring and probability of default modelling."
  - "[Rudin, 2019] — Argues for interpretable models over black-box explanations in high-stakes decisions."
  - "[Hardt et al., 2016] — Established equalised odds as a fairness criterion for supervised learning."
  - "[Bergmeir and Benítez, 2012] — Critical analysis of cross-validation for time-series evaluation."
relevance:
  topics:
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Reviews the broader credit risk modelling landscape but not PFMS specifically."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "contextual"
      justification: "Discusses limitations of statistical and ML credit models that parallel gaps in PFMS."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "low"
      justification: "Covers classification methods for credit scoring that could inform user profiling in Odin."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Provides a comprehensive review of DL predictive models applicable to spending and risk forecasting."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "medium"
      justification: "Reviews LSTM, GRU, and TCN architectures for behavioural sequence forecasting."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "low"
      justification: "Discusses differential privacy and federated learning as deployment considerations."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "low"
      justification: "Addresses interpretability, fairness, and governance as trust-enabling factors."
  contribution: "This paper surveys deep learning architectures that can inform Odin's predictive modules, particularly spending forecasting and user behavioural classification. The synthesis of sequential models provides methodological grounding for Odin's 6.A and 6.B forecasting components. The critical assessment of evaluation integrity, including out-of-time validation and calibration-aware reporting, guides how Odin's algorithmic modules should be assessed. The discussion of privacy-preserving techniques and interpretability frameworks supports Odin's data privacy and user trust design principles. The taxonomy linking model families to data structures offers a conceptual map for selecting appropriate techniques for Odin's heterogeneous user data."
  directly_justifies:
    - "LSTM and GRU networks outperform static classifiers for behavioural sequence forecasting when rich post-origination histories are available."
    - "Out-of-time validation is essential to avoid temporal leakage and obtain faithful deployment performance estimates."
    - "Calibration-aware reporting using Brier score and expected calibration error should accompany AUC-based evaluation."
    - "Tabular deep models with attention mechanisms improve discrimination on high-cardinality categorical features."
    - "GNNs capture relational dependencies in interconnected financial networks that tabular models cannot represent."
  limits:
    - "Survey focuses on credit risk prediction in lending, not on personal finance management or spending behaviour."
    - "Reviewed studies rely heavily on small public benchmarks that understate uncertainty and overestimate generalisability."
    - "Interpretability and fairness are discussed as challenges but few reviewed studies implement fairness-aware training objectives."
    - "Privacy-preserving techniques like differential privacy are mentioned but not empirically evaluated in the covered credit risk studies."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The following domains were flagged as relevant: Existing Systems & Gaps (4.A, 4.B) as contextual because the paper reviews the credit risk modelling landscape and its limitations, though not PFMS specifically. Behavioral Profiling & Classification (5.C) as low because the classification approaches for credit scoring have methodological overlap with user profiling. Spending Forecasting (6.A, 6.B) as medium because the paper provides a comprehensive review of predictive models and sequential forecasting algorithms directly applicable to Odin's forecasting modules. Data Privacy & User Trust (10.A, 10.B) as low because privacy and interpretability are discussed as deployment challenges but are not central to the survey. The following domains were considered and rejected: Filipino Cultural Context (no Philippine or cultural content), Expense Categorization (no expense taxonomy), Budget Recommendation (no budget allocation methods), Anomaly Detection (only passing mention), Mobile-First Design (not addressed), User Retention & Engagement (not addressed), System Evaluation (evaluation is for credit risk, not PFMS), Savings & Debt Management (credit default is tangentially related to debt but the paper does not address debt management strategies). The paper's overall relevance to Odin is methodological rather than domain-specific, providing techniques and evaluation principles that can inform Odin's predictive modules and design choices."
limitations:
  - "The survey relies on English-language peer-reviewed studies indexed in major databases, excluding proprietary implementations and regulatory grey literature. [unacknowledged]"
  - "Performance comparisons across studies are not standardised due to heterogeneous datasets, targets, and evaluation horizons. [unacknowledged]"
  - "No formal risk-of-bias scoring protocol was applied, limiting the ability to assess study quality systematically. [unacknowledged]"
  - "The survey focuses on borrower-level credit risk and does not cover market risk, liquidity risk, or portfolio optimisation without borrower-level labels."
  - "Small public benchmarks dominate the reviewed studies, limiting generalisability to real-world portfolios with macroeconomic dynamics."
remember_this:
  - "LSTM and GRU networks excel at behavioural sequence forecasting for dynamic credit scoring."
  - "Out-of-time validation avoids temporal leakage and yields more faithful performance estimates."
  - "Deep tabular models with attention compete with tree ensembles on large, high-cardinality datasets."
  - "GNNs capture relational risk propagation in interconnected borrower networks."
  - "Calibration-aware evaluation using Brier score should accompany AUC-based reporting."
```
---

## Paper 10: Athique & Lorenzana_summarized.md

**Source File:** `Athique & Lorenzana_summarized.md`

```yaml
paper_id: 10.1177/13678779251348945
designation: international
title: Abot kamay: Embedding digital transactions in the Philippines
authors: Athique, A.; Lorenzana, J. A.
year: 2026
venue: International Journal of Cultural Studies
odin_topics:
  - 2.A
  - 2.D
  - 3.A
  - 4.A
  - 4.B
  - 9.A
  - 10.A
  - 10.B
  - 11.A
  - 11.B
tldr: Digital transaction platforms in the Philippines become embedded through culturally specific practices of reciprocity, redistribution, and remuneration, particularly via the idiom of abot kamay.
problem_and_motivation: The digitalization of financial systems in the Global South is often analyzed through a purely functional lens, neglecting the cultural and social meanings of exchange. Understanding how digital platforms interact with established cultural norms is crucial for assessing their impact, yet this perspective is frequently missing from policy and industry literature.
approach:
  - An ethnographic study was conducted in Metro Manila across three socio-economically distinct communities: Santa Mesa, Payatas, and Quezon City.
  - The research employed focus groups and interviews (in Tagalog) with participants from 2019-2022, alongside physical observation and photographic recording of local retail outlets.
  - A multi-sited approach was used to explore the utility and meaning of digital transactions across disparate needs and means of the larger urban population.
  - The study was grounded in Karl Polanyi's concept of embeddedness, analyzing how digital transactions are given meaning within established social and cultural norms.
  - The researchers identified and analyzed three key forms of digitally-enabled support: Abono, Pantawid, and Emergency transfers, which they collectively term 'abot kamay'.
findings:
  - Digital transactions were preferred by participants for managing the awkwardness of refusing requests or awaiting repayment within kinship and community networks.
  - The use of GCash was found to enable secret financial transfers, allowing individuals to manage family obligations and avoid conflict.
  - num: Digital payments in the Philippines reached 42.1% of retail payments in 2022, with peer-to-peer transfers growing at 91.2% per annum by mid-2023.
  - Participants consistently framed their adoption of digital transactions not around convenience, but around the maintenance and management of social relationships.
  - Digital transaction affordances like SMS receipts were used by participants to create personal records for tracking social debts and obligations.
  - The digital platform ecosystem enables novel transaction chains, such as earning GCash credits through attention-economy apps like Buzz Break or gaming on Mobile Legends.
  - The sharing of mobile "load" (airtime) remains a critical form of reciprocal exchange, often acting as a precursor to or substitute for digital money transfers.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: abot kamay
    definition: Literally 'within reach' and figuratively 'a helping hand', it denotes the use of digital platforms to enable remote monetary support, embodying functional assistance and ontological proximity.
  - term: Abono
    definition: Paying for someone else's expense, for example, when they are unable to pay due to distance or lack of cash.
  - term: Pantawid
    definition: Money borrowed to get through a cash shortage.
  - term: suki
    definition: A loyal customer who receives privileges such as discounts and credit from a vendor.
  - term: kakayahan
    definition: Capacity; denotes the capacity of the giver to give and offer help, defining the limits and possibilities of abot kamay.
critical_citations:
  - "[Polanyi, 1944] — Foundational framework for economic embeddedness."
  - "[Granovetter, 1985] — Frames the ongoing relevance of reciprocity and redistribution."
  - "[Madianou and Miller, 2013] — Establishes the role of media in transnational Filipino families."
relevance:
  topics:
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Core focus on abot kamay, suki, and reciprocity as key Filipino financial norms.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: high
      justification: Directly analyzes abot kamay in contexts of emergencies, kinship obligations, and community support.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Implicitly challenges purely transactional views by categorizing digital money flows as gifts, debts, and support.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Provides a detailed overview and comparison of GCash, PayMaya/Maya, and GrabPay in the Philippines.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies key barriers like stringent ID requirements, account fees, and security concerns as gaps.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Highlights how mobile platforms are the primary interface for transactions in a context of limited traditional banking.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Discusses user anxiety about hacking and the use of intermediary accounts like GCash as an added security layer.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Shows trust is built through social networks and platform agents, not solely through institutional credibility.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Explains how features like receipts and records shape user engagement with financial obligations.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: Describes how gamification and rewards via platforms like Mobile Legends and Buzz Break drive retention and usage.
  contribution: This paper provides a crucial qualitative foundation for Odin's behavioral models by demonstrating that financial decisions in the Philippines are deeply embedded in social relationships and obligations like abot kamay. The findings directly inform the design of Odin's expense categorization, suggesting the need to distinguish between personal, familial, and communal financial flows. Furthermore, the paper's insights on trust and privacy directly justify a mobile-first design that prioritizes user control and security, as seen in the preference for intermediary accounts. Finally, the description of engagement dynamics via gaming and rewards provides a rationale for designing Odin's retention mechanisms around culturally relevant social interactions rather than purely utilitarian features.
  directly_justifies:
    - "Digital transactions are chosen to manage the awkwardness of refusing requests or awaiting repayment."
    - "SMS receipts from digital transactions are used as mental accounting for tracking social debts."
    - "Users adopt intermediary digital wallets as an extra layer of security against fraud."
    - "Engagement with transaction platforms is driven by social obligations and community practices."
    - "The need for a mobile-first design is justified by the high dependence on smartphones for financial access."
  limits:
    - "Study is qualitative and limited to three communities in Metro Manila, which may not be representative of all Filipino users."
    - "The research primarily focuses on the social meanings of transactions, offering limited quantitative insights into usage patterns [unacknowledged]."
    - "The impact of platform design features on user behavior is discussed anecdotally rather than systematically [unacknowledged]."
  mapping_rationale: The systematic scan across all 12 functional domains identified 10 relevant topic codes. The paper's core contribution to understanding culturally specific practices (2.A) and Filipino spending cycles (2.D) is high, as it directly explains the abot kamay idiom. The detailed landscape of GCash, Maya, and other platforms made it highly relevant to topics 4.A and 4.B. Topics related to mobile-first design (9.A), data privacy (10.A, 10.B), and engagement (11.A, 11.B) were flagged as medium due to supporting evidence on user preferences and behaviors. Domains like forecasting (6.A, 6.B), anomaly detection (8.A-C), and savings/debt management (13.A-C) were rejected because the paper does not address predictive modeling or specific algorithmic approaches to these areas. The overall relevance is medium-high, as it provides essential cultural and contextual grounding for Odin's behavioral and design modules, though it offers no technical solutions.
limitations:
  - "The qualitative study is based on a limited number of participants and communities in Metro Manila, restricting generalizability."
  - "The research does not provide a quantitative baseline for comparing the adoption and usage patterns across different demographic groups [unacknowledged]."
  - "The paper does not evaluate the efficacy of specific app features or their impact on user financial behavior [unacknowledged]."
  - "The study does not address the potential for digital transactions to increase financial vulnerability or debt among users [unacknowledged]."
remember_this:
  - "Filipino financial behavior is driven by culturally specific norms of reciprocity and obligation."
  - "Digital transaction platforms are embedded within existing social structures, not replacing them."
  - "Privacy in financial apps is managed through social practices like using intermediary accounts."
  - "GCash facilitates secret transfers to manage family obligations and avoid conflict."
  - "Digital receipts are used for personal accounting of social debts and relationships."
```
---

## Paper 11: Phuong et al_summarized.md

**Source File:** `Phuong et al_summarized.md`

```yaml
paper_id: 1c7b4f3e-2a8d-4c9f-b6e1-3d7a5f9c2e8b
designation: international
title: Post-Pandemic Labor Market Transformation: The Rise of the Gig Economy and Youth Employment in Southeast Asia
authors: Nguyen Thi Minh Phuong, Carlos Antonio Cruz, Rini Andriani Pratiwi
year: 2026
venue: International Journal of Economic Research and Exact Sciences
odin_topics:
  - 1.A
  - 1.B
  - 2.A
  - 2.C
  - 5.A
  - 6.A
  - 10.B
tldr: Platform-mediated gig work among urban youth in four Southeast Asian countries is shaped by education, income, and urban location, with earnings lower and more volatile than comparable formal employment.
problem_and_motivation: Policymakers in Southeast Asia lack comparative evidence on gig economy participation patterns and their welfare implications for young workers. Existing studies are largely single-country case studies, limiting the ability to design regionally informed policy responses. Cross-country evidence on determinants, earnings differentials, and lived experiences is needed.
approach:
  - Conducted a survey of 1,200 young workers aged 18-29 across Vietnam, Philippines, Indonesia, and Thailand from January to October 2023.
  - Performed 40 semi-structured interviews with platform workers across the four countries to capture lived experiences.
  - Applied logistic and ordinary least squares regression to identify determinants of gig participation and earnings differentials.
  - Used reflexive thematic analysis on interview transcripts to derive qualitative themes.
  - Integrated quantitative and qualitative findings using a meta-inference approach to contextualize statistical patterns.
findings:
  - num: 38% of urban youth in the sample engaged in platform-mediated gig work in the past 12 months.
  - num: Secondary school completion lowers gig participation probability by 6.8 percentage points.
  - num: Median full-time gig earnings range from USD 247 in Vietnam to USD 358 in Thailand.
  - num: Full-time platform earnings are 4.7% lower than comparable non-platform work in the same country.
  - num: Earnings volatility is 1.6 times higher in platform work than in comparable non-platform jobs.
  - Education is negatively associated with full-time gig participation, with a larger effect size than for any participation.
  - Male respondents are more likely to engage in full-time gig work, especially in ride-hailing and delivery.
  - Qualitative analysis identified four themes: autonomy paradox, social protection gap, skills development opportunities, and intergenerational tensions.
key_figures_tables:
  - "Table 1: Sample characteristics by country and platform engagement → Provides demographic context."
  - "Table 2: Logistic regression for gig participation → Identifies key determinants: education, income, urban location."
  - "Table 3: OLS earnings regressions → Shows platform earnings are lower and more volatile."
key_equations:
  - equation: "log(earnings) = β_0 + β_1*platform + β_2*education + β_3*income + β_4*country + ε"
    explanation: "OLS model for log monthly earnings differentials."
definitions:
  - term: "Gig economy"
    definition: "Labor market characterized by short-term contracts or freelance work, mediated by digital platforms."
  - term: "Platform work"
    definition: "Income-generating activity mediated by digital platforms that connect workers with clients."
  - term: "Autonomy paradox"
    definition: "Tension between perceived flexibility and algorithmic constraints on platform workers."
critical_citations:
  - "[Berg et al., 2018] — Found heterogeneity in platform worker experiences."
  - "[Wood et al., 2019] — Examined autonomy-control paradox in algorithmic management."
  - "[De Stefano, 2016] — Analyzed legal status of platform workers."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: "The paper's Philippine sub-sample provides data on Filipino youth labor market engagement."
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: "Reports earnings and income volatility for Filipino platform workers, relevant to financial structure."
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: low
      justification: "Discusses intergenerational tensions and family expectations influencing work choices."
    - code: 2.C
      name: User-Declared Financial Preferences
      relevance: low
      justification: "Qualitative themes include worker preferences for flexibility over formal employment."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: "Describes participation patterns but not personal finance behavioral profiles."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: contextual
      justification: "Provides earnings data but not predictive models."
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: "The social protection gap relates to trust in platforms and government."
  contribution: "The paper provides cross-country evidence on the gig economy that can inform the contextual understanding of Filipino young professionals' income streams and employment patterns. It underscores the importance of earnings volatility and social protection gaps, which are relevant to designing budget recommendation and anomaly detection modules that account for irregular income. The findings on education as a determinant of gig participation can help Odin tailor its user onboarding and categorization features to different user segments."
  directly_justifies:
    - "Young urban Filipino workers have a 39% participation rate in platform-mediated gig work, indicating significant income irregularity."
    - "Full-time platform earnings in the Philippines are 4.7% lower than comparable non-platform work, highlighting the need for conservative budget forecasts."
    - "Earnings volatility in platform work is 1.6 times higher, justifying robust anomaly detection for variable income patterns."
  limits:
    - "The survey sample is urban, limiting generalizability to rural Filipino populations."
    - "Self-reported earnings may contain measurement error for irregular platform income."
    - "Cross-sectional design prevents causal inference on long-term consequences of platform engagement."
    - "The study does not specifically address personal finance management systems or user financial behavior in detail."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant for domains related to Filipino Cultural Context (2.A, 2.C) due to its discussion of intergenerational tensions and worker preferences, and for Behavioral Profiling (5.A) and Predictive Modeling (6.A) due to its quantitative analysis of participation and earnings patterns. Low relevance was assigned to topics like 2.A and 2.C because the paper's focus is on employment, not culturally specific financial practices per se. Domains such as Expense Categorization (3), Budget Recommendation (7), Anomaly Detection (8), Mobile Design (9), Evaluation (12), Savings (13), and Engagement (11) were rejected due to no direct coverage. The paper is considered contextually relevant, providing background on the financial reality of Filipino young professionals rather than direct insights for Odin's algorithmic modules."
limitations:
  - "Urban sample limits generalizability to rural areas where platform dynamics differ."
  - "Cross-sectional design constrains causal inference about long-term consequences."
  - "Self-reported earnings are subject to measurement error. [unacknowledged]"
  - "The qualitative sample captures perspectives at a particular moment in time. [unacknowledged]"
  - "Does not include validated mental health measures, despite qualitative findings on stress. [unacknowledged]"
remember_this:
  - "38% of urban youth in the sample engaged in gig work."
  - "Earnings volatility is 1.6 times higher in platform work."
  - "Secondary education reduces gig participation probability by 6.8 percentage points."
  - "Full-time platform earnings are 4.7% lower than non-platform work."
  - "Filipino platform workers operate in a remittance-supported household context."
```
---

## Paper 12: Bustamante & Ubilla_summarized.md

**Source File:** `Bustamante & Ubilla_summarized.md`

```yaml
paper_id: 10.1108/JEFAS-10-2025-0378
designation: international
title: Retail investor behavior and social media signals: exploring attention dynamics
authors: Bustamante, D.; Ubilla, A.
year: 2026
venue: Journal of Economics, Finance and Administrative Science
odin_topics:
  - 1.C
  - 2.D
  - 4.B
  - 5.A
  - 5.C
  - 10.B
  - 11.A
  - 12.A
tldr: Social media influencer attention increases stock investment propensity, but digital financial literacy's moderating role varies significantly across countries.
problem_and_motivation: The influence of social media recommendations on retail investor behavior is underexplored, particularly regarding how digital financial literacy (DFL) moderates this relationship across diverse national contexts. Existing studies often rely on single-country samples or aggregated data, limiting generalizability and understanding of underlying mechanisms.
approach:
  - Analyzed microdata from the OECD/INFE 2023 Adult Financial Literacy Survey covering Brazil, Finland, Philippines, and Saudi Arabia.
  - Employed logistic regression with country fixed effects to model stock investment as a function of investor attention and DFL.
  - Constructed a DFL index using principal component analysis across three dimensions: digital financial behavior, knowledge, and attitude.
  - Addressed endogeneity using instrumental variable (two-stage residual inclusion) and propensity score matching techniques.
  - Examined interaction effects between attention and DFL to test for moderation across countries.
findings:
  - num: Investor attention increases the probability of stock investment by 12.2% in the pooled sample, remaining robust across countries.
  - num: Digital financial literacy (DFL) raises stock investment probability by 5.8% in the pooled sample, driven primarily by digital financial knowledge.
  - The moderating effect of DFL on the attention-investment relationship is heterogeneous: negative in the Philippines, positive in Saudi Arabia, and insignificant in Brazil and Finland.
  - Endogeneity corrections confirm the positive effect of social media attention on investment decisions remains significant.
  - Socioeconomic factors like gender, education, employment, and income consistently predict stock market participation.
key_figures_tables:
  - "Table 1: Descriptive statistics showing 21.4% stock investment and 17.7% investor attention rates → Baseline participation and attention levels are adequate for analysis."
  - "Table 2: Marginal effects from logistic regressions show attention increases investment by 12-28% across models → Attention is a robust predictor of stock investment."
  - "Table 3: Interaction effects reveal DFL moderates attention differently by country → The buffering role of DFL is not universal."
  - "Table 5: Two-stage residual inclusion results confirm attention remains significant after endogeneity correction → Main findings are robust to reverse causality concerns."
  - "Table 6: Propensity score matching shows a 10% ATT for attention on investment → Selection bias does not explain the attention effect."
key_equations:
  - equation: "Pr(SI_i = 1 | X) = Λ(β_0 + β_1·Atten_i + β_2·DFL_i + Σβ_k·Controls_ki + ΣCountry_h)"
    explanation: "Logistic model for stock investment probability as function of attention, DFL, and controls."
definitions:
  - term: "SI"
    definition: "Stock investment, a binary variable indicating direct ownership of stocks."
  - term: "Atten"
    definition: "Investor attention, coded 1 if decisions were influenced by social media or unknown individuals."
  - term: "DFL"
    definition: "Digital financial literacy, a PCA-based index of digital financial behavior, knowledge, and attitude."
  - term: "DFK"
    definition: "Digital financial knowledge, based on correct responses to questions on digital finance and regulation."
  - term: "2SRI"
    definition: "Two-stage residual inclusion, a control function method for endogeneity in nonlinear models."
critical_citations:
  - "[Barber and Odean, 2008] — Attention theory for investor behavior."
  - "[Hirshleifer and Teoh, 2003] — Limited attention and information processing."
  - "[OECD, 2023] — Source of DFL definition and survey data."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: "Provides behavioral evidence on investment decisions influenced by social media, relevant to Filipino sample."
    - code: 2.D
      name: Filipino Spending Cycles and 'Occasions'
      relevance: contextual
      justification: "Includes Philippines in cross-country analysis, offering context for financial behavior but not specific spending cycles."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: low
      justification: "Highlights gaps in understanding DFL's moderating role, which is relevant for system design but not directly evaluating existing PFMS."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: "Directly examines how attention and DFL shape investment behavior, contributing to behavioral profiling."
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: "Uses logistic regression to classify investment behavior based on attention and DFL, informing classification approaches."
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: "Discusses trust implications of social media influence and DFL, tangentially related to user trust in systems."
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: contextual
      justification: "Addresses attention as a driver of engagement, providing background but not direct design insights."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: low
      justification: "Uses econometric evaluation methods that could inform system evaluation frameworks."
  contribution: "This paper validates that social media attention is a significant driver of investment behavior, which Odin must account for when modeling user financial decisions. It demonstrates that digital financial literacy does not uniformly moderate this effect, suggesting Odin's behavioral profiling (Topic 5.A) must be context-sensitive. The cross-country comparison provides a template for evaluating how Odin's algorithms might perform differently across user segments. The methodological approach, including endogeneity correction, offers a framework for robustly evaluating Odin's predictive modules."
  directly_justifies:
    - "Social media attention significantly increases the likelihood of stock investment, requiring Odin to consider external digital signals."
    - "Digital financial literacy's moderating role is context-dependent, necessitating adaptive profiling in Odin."
    - "Endogeneity concerns in behavioral data must be addressed in Odin's evaluation framework."
  limits:
    - "Relies on cross-sectional self-reported data, limiting causal inference."
    - "Attention measure is binary and does not capture intensity or content characteristics."
    - "DFL index components vary across countries, complicating cross-national comparisons."
  mapping_rationale: "Systematic scan across 12 functional domains flagged behavioral profiling (5.A, 5.C) as highly relevant due to direct analysis of attention and DFL on investment decisions. The Filipino context (1.C, 2.D) was considered relevant because the Philippines is a sample country, though the paper does not focus on Filipino-specific practices. Existing systems gaps (4.B) and evaluation frameworks (12.A) were noted as low relevance because the paper does not evaluate PFMS but provides methodological insights. Domains like expense categorization (3.A) and budget recommendation (7.A) were rejected as the paper focuses on investment, not expense management. The overall relevance is moderate: it offers behavioral and methodological insights for Odin's profiling and evaluation modules but does not directly address core PFMS functionalities."
limitations:
  - "Cross-sectional design limits causal inference and dynamic analysis. [unacknowledged]"
  - "Self-reported data may introduce reporting and social desirability biases. [unacknowledged]"
  - "The attention question was newly introduced, preventing longitudinal comparisons. [acknowledged]"
  - "Results are based on only four countries, limiting generalizability. [acknowledged]"
  - "DFL moderating effect is heterogeneous, requiring context-specific interpretation. [acknowledged]"
remember_this:
  - "Social media attention increases stock investment propensity by 12.2% on average."
  - "Digital financial literacy's moderating role varies significantly by country context."
  - "DFL does not universally buffer against social media persuasion."
  - "Endogeneity concerns in behavioral finance require robust econometric correction."
  - "Context-sensitive digital literacy is critical for financial system design."
```
---

## Paper 13: Ying & Blaise_summarized.md

**Source File:** `Ying & Blaise_summarized.md`

```yaml
paper_id: 9d1b5d2e-0e4d-4d6b-90e5-6d6b1b2f5b5e
designation: international
title: Leveraging Big Data Analytics in Behavioral Finance: Insights into Consumer Spending and Saving Dynamics
authors: Ying, H.; Blaise, M.
year: 2026
venue: Unknown
odin_topics:
  - 1.C
  - 2.B
  - 3.A
  - 6.A
  - 7.B
  - 10.A
  - 10.B
  - 11.A
  - 12.A
  - 13.C
tldr: Big data analytics reveals psychological and contextual drivers of consumer spending and saving, enabling personalized financial strategies.
problem_and_motivation: Traditional financial models overlook behavioral biases and contextual influences that shape consumer financial decisions. Understanding these multidimensional drivers is crucial for designing effective interventions to improve financial literacy and promote savings. A systematic, data-driven approach to analyzing spending and saving patterns was missing.
approach:
  - This paper reviews applications of big data methodologies in behavioral finance.
  - It integrates structured financial datasets with unstructured digital footprints like social media and transaction histories.
  - The approach employs machine learning and predictive analytics to identify hidden determinants of financial decision-making.
  - Analytical methods include descriptive, predictive, and prescriptive analytics to understand and forecast consumer behavior.
  - The study examines case studies from financial institutions and retailers to illustrate practical applications.
findings:
  - Big data enables more accurate segmentation of consumer groups for personalized financial strategies.
  - Psychological biases and socio-demographic characteristics significantly impact financial behaviors.
  - Predictive models can forecast spending patterns based on historical data and external factors.
  - Insights from big data can improve financial literacy and promote savings behavior.
  - Integration of behavioral insights with technology provides practical tools for enhancing financial inclusion and resilience.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Big Data
    definition: Vast volumes of structured and unstructured data characterized by volume, velocity, and variety.
  - term: Behavioral Finance
    definition: Field combining psychology and economics to explain irrational financial decisions.
  - term: Cognitive Biases
    definition: Systematic patterns of deviation from rationality in judgment.
  - term: Predictive Analytics
    definition: Use of statistical models and machine learning to forecast future behaviors.
  - term: Prescriptive Analytics
    definition: Provides recommendations based on predictive models to guide decision-making.
critical_citations:
  - "[Arner et al., 2017] — Foundational context on fintech and regulation."
  - "[Fuster et al., 2020] — Discusses machine learning effects on credit markets."
  - "[Jagtiani & Lemieux, 2019] — Evidence on alternative data in fintech lending."
  - "[Mhlanga, 2020] — Covers big data and AI in financial inclusion."
  - "[Ozili, 2018] — Impact of digital finance on financial inclusion."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: contextual
      justification: General discussion of psychological and contextual financial behavior influences.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: low
      justification: Mentions seasonal trends in spending but without specific analysis for Odin.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: low
      justification: Discusses analyzing spending by categories to inform product development.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Covers predictive analytics using machine learning for forecasting spending behaviors.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Mentions personalized financial advice and products based on spending habits.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Discusses data privacy, security, and regulatory compliance as key challenges.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: Mentions building consumer trust as essential for data sharing.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: References customer engagement through personalized services.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: contextual
      justification: Highlights the need for enhanced models to evaluate creditworthiness and risk.
    - code: 13.C
      name: End-of-Period Surplus as a Savings Input
      relevance: low
      justification: Mentions automated savings programs based on spending analysis.
  contribution: This paper provides a general framework for using big data analytics to understand consumer spending and saving dynamics. It supports Odin's rationale for leveraging behavioral data to personalize financial management. The discussion of predictive analytics justifies the use of forecasting modules for spending behavior. The emphasis on data privacy and trust informs Odin's design for secure, user-centric data handling. Its findings on segmentation and personalization directly inform Odin's approach to user profiling and budget recommendations.
  directly_justifies:
    - Big data analytics enables accurate segmentation of consumer groups for personalized strategies.
    - Predictive models can forecast future spending and saving behaviors based on historical data.
    - Financial institutions can develop personalized products that align with customer spending habits.
    - Understanding behavioral triggers is crucial for designing effective savings interventions.
  limits:
    - The paper provides a broad overview without specific algorithmic details or empirical results.
    - No quantitative findings are presented to support the claims about predictive accuracy.
    - The focus is on general consumer behavior, not specifically on Filipino young professionals.
    - The paper does not address the cold-start problem in behavioral profiling.
  mapping_rationale: A systematic scan of all 12 functional domains was conducted for this paper. The domains flagged as relevant were those related to behavioral understanding (1.C, 2.B), data analysis (3.A, 6.A), personalization (7.B), and ethics (10.A, 10.B). Topic 1.C was selected as contextual due to its general discussion of financial behavior. Topic 2.B was tagged low due to a passing mention of seasonal trends. Topic 3.A was tagged low for mentioning category-based spending. Topic 6.A received medium relevance for its focus on predictive modeling. Topic 7.B was low for its broad mention of personalized advice. Topics 10.A (medium) and 10.B (low) were included for their explicit discussion of privacy and trust. Topics 11.A and 12.A were selected as low/contextual due to brief mentions. Topic 13.C was low for mentioning automated savings. Domains such as 4.A (Existing Systems), 5.A (Behavioral Profiles), 8.A (Anomaly Detection), and 9.A (Mobile Design) were rejected as the paper does not address these specific areas. The paper is broadly relevant to Odin as a high-level justification for using data analytics but lacks the specificity to directly inform implementation.
limitations:
  - Broad overview without deep technical or algorithmic depth.
  - Lacks empirical data or case-specific findings to validate its claims.
  - Does not address the specific financial context of Filipino young professionals. [unacknowledged]
  - No discussion of the cold-start problem or initial user profiling. [unacknowledged]
remember_this:
  - Big data reveals psychological and contextual drivers of financial behavior.
  - Predictive analytics can forecast spending patterns for personalized financial advice.
  - Data privacy and algorithmic bias are critical ethical concerns in big data finance.
  - Integrating behavioral insights with technology enhances financial inclusion and resilience.
  - The paper provides a framework but lacks specific, actionable insights for implementation.
```
---

## Paper 14: Amrith_summarized.md

**Source File:** `Amrith_summarized.md`

```yaml
paper_id: 10.1080/1369183X.2025.2542769
designation: international
title: "Reimagining social protection: financialised futures among ageing migrant domestic workers in Asia"
authors: "Amrith, M."
year: 2026
venue: "Journal of Ethnic and Migration Studies"
odin_topics:
  - "2.C"
  - "2.D"
  - "4.B"
  - "5.A"
  - "7.A"
  - "10.B"
  - "13.A"
tldr: "Financial education courses for ageing Filipino domestic workers cultivate self-responsibility for retirement security amid precarious state and kinship social protection."
problem_and_motivation: "Migrant domestic workers face precarious futures with limited state-based social protection and uncertain kinship care upon mandatory return. Financial education courses have proliferated to address this gap, yet their role and implications are understudied. The paper examines how these courses shape aspirations and strategies for later-life security."
approach:
  - "Ethnographic fieldwork in Singapore and Hong Kong from 2018 to 2022."
  - "Conducted over 50 in-depth interviews with migrant domestic workers aged 45-65 from the Philippines, Indonesia, India, and Sri Lanka."
  - "Observed financial education courses run by NGOs, corporate partners (KPMG), and a Filipino-led cooperative."
  - "Followed online spaces (WhatsApp, Facebook, YouTube) during the COVID-19 pandemic."
  - "Engaged with policy officers, cooperative representatives, and activist leaders."
findings:
  - "Financial education cultivates a narrative of transformation from breadwinner to financially-independent investor."
  - "Participation enables women to give themselves permission to save for themselves, challenging endless remittance obligations."
  - "Financialised aspirations exist alongside alternative strategies: political activism, faith-based resignation, and land ownership."
  - "The 'self' in financialisation remains socially embedded, with migrants continuing to navigate kin obligations and employer dependencies."
  - "num: Only 5% of overseas Filipinos in Singapore paid into the state social security system (SSS) as of 2018."
  - "State-backed schemes and private financial products generate new forms of dependency alongside promises of independence."
key_figures_tables:
  - "None."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "SSS"
    definition: "Philippine Social Security System, a contributory pension scheme."
  - term: "OFW"
    definition: "Overseas Filipino Worker."
  - term: "Paluwagan"
    definition: "Informal rotating savings and lending group among Filipinos."
critical_citations:
  - "[Rodriguez, 2010] — Philippine state's institutionalized labour export policy."
  - "[Silvey and Parreñas, 2020] — Precarity chains in domestic worker migration."
  - "[Nguyen, 2021] — Portfolios of social protection in contexts of limited state welfare."
  - "[Kar, 2017] — Financialisation of social security and self-help narratives."
relevance:
  topics:
    - code: "2.C"
      name: "User-Declared Financial Preferences"
      relevance: "high"
      justification: "Directly examines how migrant women articulate and shift their financial goals and priorities."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "medium"
      justification: "Discusses remittance obligations tied to family events and cyclical demands."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Provides detailed evidence of gaps in state social security and kinship care for returning migrants."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Describes the shift from a breadwinner to an investor mindset, revealing behavioral profile dynamics."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "medium"
      justification: "Financial literacy courses teach budgeting as a core strategy for future security."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "medium"
      justification: "Examines trust in financial products, employers, and state schemes; highlights scam awareness."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "high"
      justification: "Core focus on how migrant women plan and invest savings for retirement goals."
  contribution: "This paper informs Odin's understanding of financial behavioral profiles (5.A) by detailing the transformation from remittance-focused breadwinner to self-oriented investor among Filipino migrants. It provides evidence for the design of savings goal management (13.A) by illustrating real-world strategies like land purchase and cooperative investments. It highlights user trust dynamics (10.B) in financial products and state schemes, crucial for Odin's data privacy and trust modules. The findings on budget recommendation (7.A) reveal that financial literacy courses are a form of domain knowledge that Odin can emulate. The paper's evidence on the limitations of existing systems (4.B) directly justifies Odin's need to address gaps in social protection and financial planning."
  directly_justifies:
    - "Migrant women shift from viewing themselves as breadwinners to investors."
    - "State-based social security coverage for overseas Filipinos is extremely low (5%)."
    - "Financial education courses promote self-responsibility for retirement security."
    - "Kinship care is not a guaranteed form of social protection for returning migrants."
    - "Financialised aspirations exist alongside alternative strategies like activism and faith."
  limits: |
    - Focus on Filipino migrants may limit generalizability to other nationalities.
    - The study is qualitative and does not quantitatively measure the long-term financial outcomes of course participation.
    - The research was conducted during a specific period (2018-2022) including COVID-19, which may have influenced dynamics.
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to 'Behavioral Profiling & Classification' (5.A) and 'Savings & Debt Management' (13.A) due to its detailed account of the breadwinner-to-investor mindset shift and savings strategies. It showed medium relevance to 'Expense Categorization' (2.C, 2.D), 'Existing Systems & Gaps' (4.B), 'Budget Recommendation' (7.A), and 'Data Privacy & User Trust' (10.B) due to its discussions on financial preferences, system gaps, budgeting, and trust dynamics. Domains like 'Spending Forecasting' (6.A, 6.B), 'Anomaly Detection' (8.A), and 'Mobile-First Design' (9.A) were considered but rejected as the paper does not address predictive modeling, anomaly algorithms, or mobile UX. The borderline case of seasonal spending (2.D) was resolved by selecting 2.D as a medium relevance topic because the paper discusses cyclical remittance demands tied to family events and 'crises,' which are analogous to seasonal patterns. The paper's overall relevance to Odin is substantial, providing qualitative insights into user behavior, system gaps, and trust, though it is not directly algorithmic."
limitations:
  - "Focuses on a specific demographic (ageing Filipino domestic workers) which may not generalize to all Filipino young professionals. [unacknowledged]"
  - "The study is qualitative and does not provide quantitative metrics for financial literacy program effectiveness. [unacknowledged]"
  - "The research was conducted in Singapore and Hong Kong; findings may not apply to other migration contexts."
  - "Does not examine the long-term outcomes of financial education, such as actual retirement security."
remember_this:
  - "Only 5% of overseas Filipinos in Singapore contribute to the state pension system."
  - "Migrant women are taught to prioritize self-savings over endless kin remittances."
  - "Financialisation creates new aspirations for independence and purpose in retirement."
  - "Social protection remains a hybrid portfolio of state, kin, and market actors."
  - "Financial education is one strategy among many, including activism and faith."
```
---

## Paper 15: Duc_summarized.md

**Source File:** `Duc_summarized.md`

```yaml
paper_id: e3f5e4f2-4b1c-5d7a-9f8e-2c3d4a5b6c7d
designation: international
title: Platform Work and Social Protection Gaps in ASEAN's Gig Economy
authors: Duc, H. M.
year: 2026
venue: ACE-2026
odin_topics:
  - "4.B"
  - "10.A"
  - "10.B"
tldr: Platform work in ASEAN excludes workers from social security, creating a precariat through misclassification as independent contractors rather than employees.
problem_and_motivation: Traditional social protection models based on employer-employee relationships fail to cover gig workers. This gap is embedded in platform business models that externalize social costs. Urgent action is needed to prevent digitalization from increasing precarity.
approach:
  - Analyzed sectors including ride-hailing, delivery, and micro-tasking across ASEAN.
  - Examined legal misclassification of workers as independent contractors.
  - Identified a tripartite crisis of coverage, financing, and portability.
  - Mapped regulatory responses from judicial rulings in Thailand to laissez-faire approaches in Indonesia and Philippines.
findings:
  - Platform workers are systematically excluded from employment-based health, work injury, and pension schemes.
  - num: 100% of platform workers lack employer-linked contributions to mandatory social security.
  - Income volatility and lack of employer contributions make voluntary pension savings unaffordable.
  - Algorithmic management individualizes unemployment risk and denies collective bargaining rights.
key_figures_tables:
  - "Table 1: Typology of social protection gaps → Identifies health, pension, income, and voice deficits for platform workers."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "ASEAN"
    definition: "Association of Southeast Asian Nations."
  - term: "BPJS Ketenagakerjaan"
    definition: "Indonesia's social security scheme for workers."
  - term: "SKSPS"
    definition: "Self-Employment Social Security Scheme in Malaysia under SOCSO."
critical_citations:
  - "[Berg & de Stefano, 2022] — Argues for a global governance framework."
  - "[ILO, 2021] — Documents global social protection gaps."
  - "[World Bank, 2022] — Discusses risk-sharing for diverse work."
relevance:
  topics:
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "contextual"
      justification: "Describes systemic protection gaps but not PFMS."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "contextual"
      justification: "Relates to platform design but not directly to data privacy."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "contextual"
      justification: "Worker vulnerability relates to trust but not PFMS."
  contribution: "The paper provides contextual background on worker misclassification and precarity in platform economies. It does not directly inform Odin's PFMS design but offers a cautionary example of systemic gaps. Its analysis of income volatility and lack of savings may indirectly inform savings and debt management modules. However, no specific algorithmic or architectural insights transfer to Odin."
  directly_justifies:
    - "Platform workers face income volatility with no unemployment protection."
    - "Lack of employer contributions makes voluntary savings unaffordable."
    - "Regulatory models delinking protection from employment status are needed."
  limits:
    - "No specific data on Filipino young professionals."
    - "No algorithmic, UI, or PFMS design insights."
  mapping_rationale: "All 12 functional domains were systematically scanned for relevance. Only Existing Systems & Gaps (4.B) and Data Privacy & User Trust (10.A, 10.B) were flagged as contextual, as the paper discusses systemic gaps and worker vulnerability but not PFMS. The paper was rejected for domains like Spending Forecasting, Budget Recommendation, and Mobile-First Design, as it provides no technical or behavioral modeling. Overall, relevance is contextual only, serving as a case study of platform-related social risks."
limitations:
  - "No quantitative data on ASEAN worker coverage rates. [unacknowledged]"
  - "Does not evaluate proposed policy solutions. [unacknowledged]"
  - "Focuses on ride-hailing and delivery, not broader gig work."
remember_this:
  - "Platform work excludes ASEAN workers from social security."
  - "Misclassification as independent contractors severs access to benefits."
  - "Income volatility prevents voluntary pension savings."
  - "Regulatory action is needed to link protection to work activity."
```

```yaml
paper_id: b8a7c9d0-1e2f-3a4b-5c6d-7e8f9a0b1c2d
designation: international
title: Digital Skills as a Driver for Youth Inclusion in Mountain Economies
authors: Kalandarova, A.
year: 2026
venue: ACE-2026
odin_topics:
  - "None"
tldr: Digital skills development can unlock economic opportunities and prevent outmigration in mountain economies by enabling global participation.
problem_and_motivation: Mountain economies face youth outmigration and demographic decline due to geographic isolation and limited opportunities. Developing relevant digital skills offers a path to economic inclusion and community revitalization. However, generic digital literacy programs often misalign with specific local needs.
approach:
  - Focuses on digital literacy, remote collaboration, e-commerce, digital marketing, and niche technical skills like GIS mapping.
  - Analyzes the potential to create location-independent enterprises.
  - Identifies misalignment between generic training programs and mountain economy needs.
findings:
  - Digital skills can unlock livelihoods in tourism, agroforestry, and artisanal production.
  - Generic digital literacy programs often fail to address specific mountain economy needs.
  - Remote work and e-commerce enable youth to earn income without migrating.
key_figures_tables:
  - "None."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "GIS"
    definition: "Geographic Information System."
critical_citations:
  - "None."
relevance:
  topics:
    - code: "None"
      name: "None"
      relevance: "contextual"
      justification: "No direct connection to PFMS or Odin domains."
  contribution: "The paper addresses youth inclusion in mountain economies through digital skills training. It does not relate to personal finance management, spending behavior, or algorithmic systems. No insights transfer to Odin's design, implementation, or evaluation."
  directly_justifies:
    - "Digital skills can create location-independent economic opportunities."
  limits:
    - "No connection to PFMS or Odin's functional domains."
  mapping_rationale: "All 12 functional domains were systematically scanned. No domain or topic code was found to be relevant, as the paper focuses on digital skills for economic development in mountain regions, not personal finance, spending behavior, or algorithmic systems. It was rejected for all domains including Filipino Cultural Context, Expense Categorization, and Forecasting due to lack of relevance. Overall relevance is contextual only, offering no actionable input for Odin."
limitations:
  - "No specific data on Filipino youth."
  - "No algorithmic or PFMS design insights."
remember_this:
  - "Digital skills can prevent youth outmigration from mountain economies."
  - "Generic training misaligns with specific local needs."
  - "Remote work enables income generation without relocation."
```
---

## Paper 16: Oprins_summarized.md

**Source File:** `Oprins_summarized.md`

```yaml
paper_id: "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
designation: "international"
title: "Understanding Online Freelancers' Labour Agency at the Intersection of Platforms, Wider Labour Markets, and Households: Evidence From the Philippines"
authors: "Oprins, J. H."
year: 2026
venue: "New Technology, Work and Employment"
odin_topics:
  - "1.A"
  - "1.B"
  - "1.C"
  - "2.A"
  - "2.D"
  - "4.A"
  - "4.B"
  - "5.A"
  - "5.C"
  - "11.A"
tldr: "Filipino online freelancers exercise labour agency through financial and temporal strategies shaped by platform logics, wider labour market positions, and gendered household responsibilities, with uneven implications for long-term platform success."
problem_and_motivation: "Research on online freelancers' labour agency often fails to account for the interplay between platform dynamics, broader labour market conditions, and gendered household responsibilities. This gap limits understanding of how freelancers make job-selection decisions critical to their platform success. An integrated framework is needed to examine these intersecting structures."
approach:
  - "Conducted in-depth interviews with 25 Filipino freelancers new to Upwork, recruited via Facebook groups."
  - "Used purposive sampling for diversity in urbanisation level, sex, and service type offered."
  - "Developed a semi-structured interview guide informed by a three-dimensional analytical framework: platform environment, wider labour market, and private sphere."
  - "Conducted walkthrough analysis of Upwork's features and examined each participant's platform profile."
  - "Applied Template Analysis with theory-driven initial coding and inductive refinement to capture participants' accounts."
findings:
  - "Freelancers exercise agency through two overarching strategies: optimising financial resources and managing temporal resources."
  - "Financial constraints from private lives limited freelancers' ability to purchase connects and absorb platform fees, leading some to accept off-platform work."
  - "Freelancers maximised limited free connects by carefully matching skills to job requirements and scrutinising clients for legitimacy."
  - "Men's full-time IT-BPO employment and breadwinner roles curtailed their time for Upwork, disadvantaging their platform career building."
  - "Women leveraged extended family support and experience with nocturnal work rhythms to accommodate Upwork's temporal demands."
  - "Gendered caregiving norms shaped women's turn to online freelancing for temporal flexibility in balancing paid work and domestic responsibilities."
  - "Freelancers' off-platform alternatives (other platforms, personal networks) reduced their adherence to a single platform's logics."
  - "Adherence to platform logics was necessary for accumulating reputation, yet structurally conditioned strategies often led freelancers to deprioritise Upwork."
key_figures_tables:
  - "None."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Labour agency"
    definition: "Intentional, purposive, and meaningful pursuit of self-interest with limited resources, exercised within and shaped by multiple intersecting contexts."
  - term: "Platformic management"
    definition: "Broad set of technological resources and rules wielded by online freelance platforms to enable and manage work."
critical_citations:
  - "[Graham et al., 2017] — Platform work can cause skill stagnation or downskilling."
  - "[Anwar and Graham, 2020] — New freelancers select easy jobs to build reputation quickly."
  - "[James, 2022, 2024] — Women's agency is constrained by social reproductive responsibilities."
  - "[Rahman, 2021] — Freelancers heavily dependent on a platform invest in rebuilding reputation after setbacks."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "high"
      justification: "Focuses on Filipino freelancers, a core demographic for Odin."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "medium"
      justification: "Details financial pressures and the role of online freelancing in household income strategies."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Examines financial optimisation strategies and resource allocation in job selection."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "high"
      justification: "Explores gendered household responsibilities, social reproduction, and family support structures."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "low"
      justification: "Provides contextual framing but does not directly address cyclical spending patterns."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Analyses platform logics of Upwork that inform Odin's consideration of existing PFMS and platform dynamics."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Identifies platform lock-in effects and reputation systems as limiting factors, relevant to PFMS gaps."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Demonstrates how behavioural strategies (financial/temporal optimisation) are shaped by structural contexts."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "contextual"
      justification: "Provides background on behavioural heterogeneity but does not address classification methods directly."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "medium"
      justification: "Highlights how platform engagement is shaped by temporal and financial logics, relevant to user retention."
  contribution: "This paper informs Odin's user profiling (5.A) by demonstrating that financial behavioural strategies are shaped by platform dynamics and household structures. It contributes to understanding culturally specific financial practices (2.A) by revealing gendered patterns in how Filipino freelancers manage temporal and financial resources. The findings on engagement dynamics (11.A) highlight how platform logics condition user behaviour, relevant for Odin's retention mechanisms. The paper justifies the need for Odin to account for users' broader labour market positions and private-sphere responsibilities in its design (4.B)."
  directly_justifies:
    - "Financial constraints from private lives limit freelancers' capacity to invest in platform engagement."
    - "Gendered caregiving norms shape women's pursuit of online freelancing for temporal flexibility."
    - "Men's full-time employment and breadwinner roles curtail their time for platform work."
    - "Adherence to platform logics is necessary for reputation accumulation but often deprioritised due to structural constraints."
  limits:
    - "Small sample size of 25 freelancers limits generalisability across the broader Filipino freelancer population."
    - "Qualitative design does not permit quantitative causal inference about platform success factors."
    - "Focus on new Upwork users may not reflect the strategies of established freelancers with strong reputations."
    - "Relies on self-reported accounts, which may be subject to social desirability or recall bias."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was conducted. The domains flagged as relevant were Filipino Cultural Context (codes 2.A, 2.D), Existing Systems & Gaps (4.A, 4.B), Behavioral Profiling & Classification (5.A, 5.C), and User Retention & Engagement (11.A). Code 2.A was assigned 'high' due to the paper's detailed treatment of gendered household roles and social reproduction. Code 2.D was assigned 'low' as seasonal spending is mentioned only as background framing. Code 1.A, 1.B, and 1.C were selected with 'high' and 'medium' relevance as the paper directly studies Filipino freelancers' demographics, financial structure, and behaviour. Code 4.A and 4.B received 'medium' relevance for their analysis of platform logics and gaps. Code 5.A and 5.C were rated 'medium' and 'contextual' respectively, as the paper demonstrates behavioural strategies but does not develop classification methods. Code 11.A was rated 'medium' for insights on engagement dynamics. Domains considered and rejected included Expense Categorization (3.A-C), Spending Forecasting (6.A-B), Budget Recommendation (7.A-D), Anomaly Detection (8.A-C), Mobile-First Design (9.A-B), Data Privacy (10.A-B), System Evaluation (12.A-C), and Savings & Debt Management (13.A-C), as the paper does not address these technical or design-focused domains. The paper is overall relevant to Odin for its rich qualitative insights into Filipino users' financial behaviours and the structural factors shaping them, though its primary contribution is conceptual rather than algorithmic."
limitations:
  - "Small sample size (n=25) limits generalisability."
  - "Qualitative design does not permit quantitative causal inference."
  - "Focus on new Upwork users may not reflect established freelancers' strategies. [unacknowledged]"
  - "Relies on self-reported accounts subject to bias. [unacknowledged]"
remember_this:
  - "Freelancers optimise financial and temporal resources in job selection."
  - "Gendered household responsibilities shape women's turn to online freelancing for flexibility."
  - "Men's full-time employment and breadwinner roles limit time for platform work."
  - "Adherence to platform logics is needed for reputation but often deprioritised."
  - "Structural constraints lead to uneven long-term platform success."
```
---

## Paper 17: Lee J. et al_summarized.md

**Source File:** `Lee J. et al_summarized.md`

```yaml
paper_id: 10.1080/13696998.2026.2630598
designation: international
title: Comparing deep learning and classical regression approaches for predicting healthcare expenditure and spending: a systematic review
authors: Lee, J. T.; Yeh, M. H.-S.; Li, V. C.-S.; Chen, H.-H.; Liu, Y.-H.; Chen, Y.-C.; Wu, D. B.-C.
year: 2026
venue: Journal of Medical Economics
odin_topics:
  - 3.A
  - 4.A
  - 5.A
  - 6.A
  - 6.B
  - 7.A
  - 8.B
  - 12.A
  - 12.B
  - 12.C
tldr: Deep learning excels in longitudinal, sequence-rich cost forecasting, while tree-based methods remain highly competitive for cross-sectional tabular prediction.
problem_and_motivation: Accurate prediction of individual healthcare costs is crucial for insurance underwriting, risk adjustment, budget planning, and value-based payment strategies. Traditional statistical approaches often struggle to capture complex nonlinear interactions in health data, but a clear understanding of when deep learning offers a meaningful advantage over classical methods is lacking.
approach:
  - A preregistered systematic review (PROSPERO CRD420251129440) was conducted.
  - Searches were performed in Web of Science, PubMed, Embase, and Scopus through August 2025.
  - Eight studies were included that used real-world individual-level data and directly compared a deep learning architecture with a classical regression comparator.
  - Data were extracted on population, predictors, outcome horizon, model type, validation strategy, and performance metrics.
  - Findings were synthesized narratively, leading to the proposal of a Complexity-Performance Hypothesis.
findings:
  - "num: Sequential deep learning models showed approximately 10-20% reductions in RMSE/MAE over classical methods in longitudinal designs."
  - "num: R² improvements from deep learning ranged from 0.01 to 0.15 in various studies."
  - "num: Deep learning models achieved AUROC values up to 0.78 for high-risk classification of preventable hospitalizations."
  - Prior costs and utilization were consistently the strongest predictors across all studies.
  - For low-dimensional, structured, cross-sectional data, generalized linear models and tree-based approaches remain robust baselines.
  - A conceptual Complexity-Performance Hypothesis was formulated, linking model capacity to data complexity.
key_figures_tables:
  - "Figure 2: Conceptual model performance by data complexity → Deep learning excels in complex settings, while regression is best for simple data."
  - "Table 1: Characteristics of identified studies → Summary of study design, population, and models for all 8 included papers."
  - "Table 2: Model performance and features of included studies → Detailed comparative results for all studies."
  - "Table 3: Neural network architectures applied → Categorization of models by data type used."
  - "Table 4: Challenges of deep learning in spending prediction → Future strategies for interpretability, benchmarking, and generalizability."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: LSTM
    definition: Long short-term memory, a recurrent neural network architecture.
  - term: CNN
    definition: Convolutional neural network.
  - term: RNN
    definition: Recurrent neural network.
  - term: GLM
    definition: Generalized linear model.
  - term: RMSE
    definition: Root mean square error.
  - term: MAE
    definition: Mean absolute error.
  - term: AUROC
    definition: Area under the receiver operating characteristic curve.
  - term: EMR
    definition: Electronic medical records.
  - term: EHR
    definition: Electronic health records.
  - term: XAI
    definition: Explainable artificial intelligence.
critical_citations:
  - "[Drewe-Boss et al., 2022] — Provided a strong example of deep learning outperforming ridge regression."
  - "[Yang et al., 2018] — Showed RNN gains for high-cost patient forecasting."
  - "[Lewis et al., 2021] — Demonstrated LSTM and CNN superiority for preventable care prediction."
  - "[Esteva et al., 2019] — Cited for the promise of deep learning in healthcare."
  - "[Topol, 2019] — Cited for contextualizing the convergence of human and AI in medicine."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: The review discusses different outcome variables like total cost and pharmacy expenditure.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Reviews the predictive modeling landscape, which is relevant to PFMS.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Discusses predicting high-cost patients, analogous to financial profiling.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly compares forecasting models for expenditure, informing Odin's predictor selection.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Focuses on algorithms like LSTM and CNN-LSTM for sequential data, directly applicable to spending forecasting.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Finding on data complexity ties to optimal model choice for budget recommendation.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Discussion of identifying high-cost outliers relates to anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a systematic framework for comparing algorithmic modules, a core part of system evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Directly evaluates the performance of different algorithmic modules (deep learning vs. regression).
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: high
      justification: The systematic review methodology and metrics (RMSE, MAE, R²) are directly transferable to evaluating budget recommendation.
  contribution: This systematic review provides a clear, evidence-based framework for selecting between deep learning, tree-based, and regression models for spending prediction tasks. It directly informs Odin's algorithmic module selection by establishing that LSTM and CNN-LSTM models are best for longitudinal data, while simpler models are sufficient for cross-sectional data. The proposed Complexity-Performance Hypothesis can guide the design of Odin's forecasting and anomaly detection components.
  directly_justifies:
    - "Sequential deep learning models (LSTM, CNN-LSTM) offer clear predictive advantages for longitudinal spending data."
    - "Tree-based methods remain highly competitive for cross-sectional, tabular spending prediction."
    - "Prior costs and utilization are consistently the strongest predictors of future spending."
    - "The complexity of the data should dictate the choice of the forecasting model."
  limits:
    - "Review based on a small and heterogeneous set of eight studies, limiting generalizability."
    - "None of the studies performed full external validation across independent datasets."
    - "The review's findings are based on healthcare data, not personal finance data, which may have different characteristics."
    - "The Complexity-Performance Hypothesis is a conceptual framework requiring further systematic validation."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to the 'Spending Forecasting' domain (codes 6.A, 6.B) as it is a systematic review directly comparing forecasting algorithms. It also has high relevance to the 'System Evaluation' domain (codes 12.A, 12.B, 12.C) due to its focus on comparative performance metrics and evaluation frameworks. The paper provides medium relevance to 'Behavioral Profiling & Classification' (5.A) through its discussion of predicting high-cost populations, and 'Anomaly Detection' (8.B) via high-cost outlier identification. It offers contextual relevance to 'Expense Categorization' (3.A) and the 'Existing Systems' landscape (4.A). Domains such as Filipino Cultural Context, Mobile-First Design, and Data Privacy were considered and rejected because the paper does not address these topics. The 'Budget Recommendation' domain (7.A) is considered medium relevance as the findings on data complexity guide model choice for such recommendations. Overall, the paper provides strong empirical justification for model selection in Odin's forecasting and evaluation modules.
limitations:
  - "The evidence base is small (n=8) and heterogeneous in design and data sources."
  - "Prediction horizons are predominantly short-term (one year), limiting assessment of long-term performance. [unacknowledged]"
  - "Social determinants of health and behavioral predictors are rarely incorporated into the models. [unacknowledged]"
  - "None of the studies performed full external validation. [unacknowledged]"
  - "Assessments of calibration, fairness, and economic interpretability were sparse or absent. [unacknowledged]"
  - "The Complexity-Performance Hypothesis is a working hypothesis derived from a limited set of studies, not a definitive causal mechanism. [acknowledged]"
remember_this:
  - "Deep learning excels for longitudinal, sequence-rich cost forecasting."
  - "Tree-based methods are highly competitive for cross-sectional tabular data."
  - "Model accuracy is maximized when capacity is matched to data complexity."
  - "Prior costs and utilization are the strongest predictors of future spending."
  - "LSTM and CNN-LSTM hybrids reduced forecasting error by up to 20% in some studies."
```
---

## Paper 18: Breza & Kaur_summarized.md

**Source File:** `Breza & Kaur_summarized.md`

```yaml
paper_id: a8c9f2d1-4e5b-4a7d-9c3f-2b8d1e4f6a7b
designation: international
title: Psychology and Development: Applications from Cognitive and Social Psychology
authors: Breza, E.; Kaur, S.
year: 2026
venue: National Bureau of Economic Research
odin_topics:
  - "1.A"
  - "1.B"
  - "1.C"
  - "2.A"
  - "2.B"
  - "2.C"
  - "2.D"
  - "3.A"
  - "4.A"
  - "4.B"
  - "5.A"
  - "5.B"
  - "5.C"
  - "6.A"
  - "6.B"
  - "7.A"
  - "7.B"
  - "8.A"
  - "8.B"
  - "9.A"
  - "9.B"
  - "10.A"
  - "10.B"
  - "11.A"
  - "11.B"
  - "12.A"
  - "12.B"
  - "12.C"
  - "13.A"
  - "13.B"
  - "13.C"
tldr: A comprehensive research agenda for behavioral development economics, arguing that psychological constraints (self-control, cognition, self-beliefs, mental health, social norms) are amplified by poverty's features and shape both individual poverty traps and market functioning.
problem_and_motivation: Development economics has focused on external constraints like missing markets, but internal psychological constraints may similarly impede escaping poverty and may be amplified by poverty's core features. Understanding whether these psychological channels play a first-order role in perpetuating poverty and shaping informal institutions is a critical, underexplored question for the field.
approach:
  - Reviews evidence across five psychological constructs: self-control, cognitive constraints, self-beliefs, mental health, and social norms.
  - Applies a missing markets lens to argue why behavioral aids are under-supplied, justifying policy intervention to correct market failures.
  - Identifies five features of poverty (proximity to subsistence, high volatility, market failures, weak institutions, reliance on social ties) that amplify the consequences of psychological constraints.
  - Highlights where evidence is merely a proof of concept versus where meaningful impacts on education, investment, and earnings have been demonstrated.
  - Advocates for a complementary research approach that starts from broad stylized facts in developing countries (e.g., ROSCAs, high-interest debt cycles) and uses behavioral tools to unpack them.
findings:
  - num: Evidence for self-control problems is widespread, with commitment device take-up ranging from 11% to 36% in various field experiments.
  - num: Hard commitment devices can lower welfare due to naivete, with 66% of smokers in one study forfeiting savings, but learning over time can improve welfare.
  - num: Cognitive constraints, like retrieval failures, can lead to 20% higher savings and 9% higher yields through simple interventions prompting recall of future expenses.
  - num: Cash on hand can improve worker productivity by 7% and reduce attentional mistakes by reducing financial worries.
  - Interventions targeting self-beliefs (aspirations, self-efficacy) can have large, persistent impacts, such as a 0.09 standard deviation increase in math scores for teachers' students.
  - Psychotherapy for depression in Pakistan led to 0.2-0.3 standard deviation increases in parental investments in children.
  - Social norms act as powerful determinants of equilibrium outcomes, with 33% of workers accepting a job at the prevailing wage but only 1.8% accepting a 10% wage cut when socially observable.
  - The kin tax or social tax can distort labor supply, with workers being 10-11% more productive when their earnings are hidden from social networks.
  - Inter-group contact improves attitudes but effects on generalized prejudice are modest, often limited to the specific domain of contact.
key_figures_tables:
  - "Table 1: Summary of psychological constructs and their relevance to poverty → Provides a structured overview of key mechanisms and evidence."
  - "Figure 3.1: Payday effect on worker output → Illustrates cyclicality in effort consistent with self-control problems."
key_equations:
  - equation: "U = u(c_0) + β Σ_{t=1}^{T} δ^t u(c_t)"
    explanation: "Quasi-hyperbolic discounting function with present bias β."
definitions:
  - term: "Behavioral Aids"
    definition: "Tools, products, or services that mitigate the impacts of psychological constraints."
  - term: "Soft Commitment"
    definition: "Commitment devices relying on non-monetary costs like social pressure or internal psychological costs."
  - term: "Cognitive Endurance"
    definition: "The ability to sustain performance over time during a cognitively effortful task."
  - term: "Kin Tax"
    definition: "Redistributive pressures from family and social networks that can tax individual savings and earnings."
  - term: "Pluralistic Ignorance"
    definition: "A situation where individuals privately reject a norm but mistakenly assume others endorse it."
critical_citations:
  - "[Ashraf et al., 2006] — Foundational field experiment on commitment savings in the Philippines."
  - "[Mani et al., 2013] — Key evidence on poverty and cognitive function."
  - "[Hanna et al., 2014] — Demonstrates persistent learning failures due to selective attention."
  - "[Kaur et al., 2015] — Evidence for self-control problems and commitment demand in labor supply."
  - "[Kremer et al., 2019] — Previous review of behavioral development economics."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "contextual"
      justification: "Paper discusses poverty broadly, but not specifically Filipino young professionals."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "contextual"
      justification: "Discusses irregular income and expenditure shocks relevant to financial structure, but not specific to Filipinos."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "medium"
      justification: "Reviews financial behaviors (savings, borrowing, labor supply) relevant to understanding this demographic's behavior."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "medium"
      justification: "Discusses ROSCAs, susu collectors, and other culturally specific financial practices common in developing countries."
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "high"
      justification: "Dedicated section on seasonal poverty, hungry seasons, and harvest cycles directly informs this topic."
    - code: "2.C"
      name: "User-Declared Financial Preferences"
      relevance: "medium"
      justification: "Discusses how poverty affects time preferences and financial decision-making, relevant to user preferences."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "low"
      justification: "Reviews seasonal and cyclical spending broadly, but does not specifically mention Filipino 'occasions'."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "medium"
      justification: "Discusses mental accounting as a cognitive shortcut, which is a form of expense categorization."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews existing systems like microfinance, ROSCAs, and commitment savings products."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Directly discusses limitations of formal and informal financial systems, including missing markets for behavioral aids."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Discusses heterogeneity in self-control and its correlation with commitment demand."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "medium"
      justification: "Discusses learning about self-control problems and the challenges of initial measurement, related to cold-start."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "low"
      justification: "Discusses using payday effects and commitment take-up as proxies but not classification methods."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "low"
      justification: "Provides evidence of predictable patterns (e.g., payday effects, seasonal savings) that could inform forecasting models."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "low"
      justification: "Does not address specific forecasting algorithms, only behavioral patterns relevant to forecasting."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "medium"
      justification: "Discusses mental accounting and label-based savings as informal budgeting strategies."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Provides evidence on expense under-estimation, informing how budget recommendations might need to address retrieval failures."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "low"
      justification: "Does not directly address anomaly detection but discusses behavioral patterns that could be flagged as anomalies."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "low"
      justification: "No discussion of specific algorithms for anomaly detection."
    - code: "9.A"
      name: "Mobile‑First Design Principles and Rationale"
      relevance: "low"
      justification: "No direct discussion of mobile design."
    - code: "9.B"
      name: "Mobile UX Design for Personal Finance"
      relevance: "low"
      justification: "No direct discussion of mobile UX."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "low"
      justification: "No direct discussion of data privacy."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses trust as a barrier to commitment devices and formal financial services."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "medium"
      justification: "Discusses reminders and soft commitments as engagement mechanisms."
    - code: "11.B"
      name: "Retention Mechanisms and Engagement Design"
      relevance: "medium"
      justification: "Discusses learning dynamics and the design of commitment devices for sustained behavior change."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses challenges in evaluating welfare effects of interventions."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "low"
      justification: "No direct discussion of algorithmic evaluation."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "low"
      justification: "Does not discuss budget recommendation system evaluation."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "high"
      justification: "Extensive review of commitment devices, savings groups, and goal-setting interventions directly informs this topic."
    - code: "13.B"
      name: "Debt Management in PFMS"
      relevance: "medium"
      justification: "Discusses high-interest debt cycles and microfinance as a potential commitment device."
    - code: "13.C"
      name: "End‑of‑Period Surplus as a Savings Input"
      relevance: "low"
      justification: "Discusses post-harvest savings but not the specific mechanism of surplus as input."
  contribution: "Odin's design of behavioral profiles is supported by this paper's review of self-control heterogeneity and its link to commitment demand, informing both profile creation and forecasting. The paper's discussion of cognitive constraints and retrieval failures directly justifies Odin's need for modules that help users recall expenses and set realistic budgets. Its review of soft commitments and social signaling provides a rationale for designing engagement features that leverage social norms and peer support to improve user retention. The paper's emphasis on the welfare consequences of psychological constraints and the role of missing markets offers a framework for evaluating Odin's impact on user financial health. Finally, its analysis of mental accounting and goal setting validates Odin's focus on user-defined allocation constraints and savings goal management."
  directly_justifies:
    - "Poverty amplifies the consequences of cognitive and self-control failures, making behavioral aids particularly valuable for low-income users."
    - "Soft commitments like mental accounting can be as effective as hard commitments and avoid welfare losses from naivete."
    - "Reminders and salience interventions can significantly improve savings and other forward-looking behaviors."
    - "Social norms and image concerns are powerful drivers of behavior that can be harnessed for positive change."
    - "Users may systematically underestimate future expenses, a key insight for designing budget recommendations."
  limits:
    - "The paper is a review and does not present new empirical findings or test specific algorithms."
    - "The focus is on developing countries broadly, not specifically the Filipino context, requiring contextual adaptation."
    - "Evidence for some constructs (e.g., psychology of poverty mechanisms) remains nascent and proof-of-concept, limiting direct design implications."
  mapping_rationale: "A systematic scan across all 12 functional domains was conducted. Domains flagged as highly relevant include Expense Categorization, Existing Systems & Gaps, Behavioral Profiling, Budget Recommendation, and Savings & Debt Management due to the paper's extensive review of self-control, cognitive constraints, mental accounting, and financial behaviors. Medium relevance was assigned to Filipino Cultural Context and User Retention & Engagement, as the paper discusses social norms and practices common in developing countries but not specifically Filipino, and engagement mechanisms like reminders and soft commitments. Topics like Data Privacy & User Trust and Mobile‑First Design received low relevance as they are not directly addressed. Borderline cases included seasonal spending patterns (2.B and 2.D), where the paper's general discussion of seasonality was applied to both, and user constraints (3.C and 7.B), where the paper's discussion of cognitive failures and under-estimation of expenses was seen as relevant to both allocation constraints and budget design. The paper is highly relevant to Odin, providing a broad theoretical and empirical foundation for its core modules."
limitations:
  - "Much of the evidence for the psychology of poverty remains at the proof-of-concept stage, not yet demonstrating first-order economic impacts. [unacknowledged]"
  - "The paper does not provide specific guidance on how to measure or operationalize many of the discussed psychological constructs in a PFMS. [unacknowledged]"
  - "The potential for interventions to be scaled and integrated into a digital product is not thoroughly explored. [unacknowledged]"
  - "There is limited discussion of potential negative side effects or unintended consequences of behavioral interventions. [unacknowledged]"
remember_this:
  - "Poverty's features amplify psychological constraints, making behavioral aids critical for financial health."
  - "Soft commitments like mental accounting can be powerful tools for behavior change without high welfare costs."
  - "Cognitive constraints, especially retrieval failures, cause systematic underestimation of future expenses."
  - "Social norms and image concerns are powerful drivers of financial behavior, both positive and negative."
  - "Interventions targeting self-beliefs show meaningful, long-term impacts on education and earnings."
```
---

## Paper 19: Ramesh & Shobha_summarized.md

**Source File:** `Ramesh & Shobha_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international
title: Dynamic Income Volatility and Adaptive Financial Planning Strategies in the Gig Economy: An Empirical Study
authors: Ramesh, S.; Shobha, C.
year: 2026
venue: Artha Vijnana
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.B
  - 3.A
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 13.A
tldr: Gig workers facing higher income volatility adopt more adaptive financial planning strategies, a relationship moderated by financial literacy and influenced by demographic and psychological factors.
problem_and_motivation: The gig economy's rapid growth presents unique financial challenges for workers due to pronounced income volatility. This instability complicates financial management for individuals lacking traditional employment benefits. Effective financial planning strategies are crucial for mitigating these adverse effects.
approach:
  - A longitudinal research design was used, surveying 500 gig workers bi-annually over three years.
  - Data was collected via online surveys optimized for mobile and desktop accessibility.
  - The study employed multiple regression analyses and structural equation modeling (SEM) to examine relationships.
  - Mixed-effects models and growth curve modeling were used for longitudinal data analysis.
  - Thematic analysis of qualitative data from open-ended questions and interviews was also conducted.
findings:
  - num: Higher income volatility is positively associated with adaptive financial planning strategies (β = 0.276, p < 0.001).
  - Financial literacy moderates the relationship between income volatility and adaptive strategies (β = 0.161, p = 0.009).
  - Education (β = 0.038, p = 0.002) and family status (β = 0.046, p = 0.046) significantly predict adaptive financial planning.
  - Risk tolerance positively influences adaptive planning (β = 0.332, p < 0.001), while cognitive bias has a negative impact (β = -0.220, p = 0.001).
  - Demographic factors like age, education, and family status significantly influence financial planning strategies.
key_figures_tables:
  - Table 1: Descriptive statistics for all study variables including means, standard deviations, and ranges.
  - Table 2: Cronbach's alpha values (0.78, 0.81) for financial literacy and adaptive financial planning scales, confirming reliability.
  - Table 3: VIF values for multicollinearity check, showing high VIFs for income volatility and its interaction term.
  - Table 4: Regression results for Model 1 showing significant positive effects of income volatility, risk tolerance, and demographic factors on adaptive planning.
  - Table 5: Regression results for Model 2 demonstrating the significant moderating effect of financial literacy on income volatility and adaptive planning.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: Financial Literacy
    definition: The ability to understand and use various financial skills, including personal financial management, budgeting, and investing.
  - term: Income Volatility
    definition: The degree of unpredictable fluctuation in an individual's earnings over time.
  - term: Adaptive Financial Planning
    definition: The use of flexible and dynamic strategies, such as diversified income sources and flexible budgeting, to manage financial instability.
  - term: Gig Economy
    definition: A labor market characterized by flexible, short-term, and task-based work arrangements often mediated by digital platforms.
  - term: Cognitive Bias
    definition: Systematic patterns of deviation from norm or rationality in judgment, affecting financial decision-making.
critical_citations:
  - "[Katz and Krueger, 2016] — Foundational for gig economy growth and worker challenges."
  - "[Lusardi and Mitchell, 2014] — Establishes the link between financial literacy and better financial outcomes."
  - "[Kahneman and Tversky, 1979] — Provides the theoretical basis (Prospect Theory) for understanding decision-making under uncertainty."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "contextual"
      justification: "While the study focuses on gig workers generally, its findings on financial behavior and volatility are applicable to demographic subsets like Filipino young professionals."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "contextual"
      justification: "Provides insights into income volatility and financial management challenges that can inform understanding of the financial structure of this group."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "medium"
      justification: "Directly studies financial planning behaviors (adaptive strategies) in response to income volatility, relevant to understanding financial behavior."
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "medium"
      justification: "Income volatility in gig work is linked to seasonality and demand cycles, which informs understanding of cyclical spending patterns."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "low"
      justification: "Adaptive strategies include flexible budgeting, which requires frameworks for expense categorization, though not the paper's focus."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Directly investigates how income volatility and psychological traits (risk tolerance, cognitive bias) shape financial behavioral profiles and adaptive planning."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "The study's identification of factors (literacy, demographics) influencing behavior can inform classification approaches for profiles."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "low"
      justification: "Findings on behavioral responses to volatility can be input features for predictive models but does not itself develop them."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "low"
      justification: "Insights on how volatility affects planning can inform forecasting, but the paper does not propose or evaluate algorithms."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "high"
      justification: "The paper identifies flexible budgeting and increased savings as key adaptive strategies, directly relevant to domain knowledge on budgeting."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "medium"
      justification: "Findings show increased savings during high-income periods as a coping strategy, relevant to savings goal management."
  contribution: This paper provides empirical evidence on how financial literacy and demographic factors moderate the behavioral response to income volatility, which can inform Odin's user profiling module. The identified adaptive strategies (flexible budgeting, increased savings) can be directly incorporated into Odin's budget recommendation and savings goal modules. The negative impact of cognitive bias on planning validates the need for behavioral nudges within the application. The methodology using mixed-effects models offers a framework for evaluating financial behavior over time.
  directly_justifies:
    - "Income volatility prompts adoption of flexible budgeting and increased savings."
    - "Financial literacy enhances the effectiveness of financial planning strategies."
    - "Risk tolerance is positively associated with better financial planning."
    - "Cognitive biases negatively impact financial decision-making."
    - "Demographic factors like education and family status influence financial planning."
  limits:
    - "The study focuses on the Indian gig economy context, which may limit generalizability to other regions."
    - "Self-reported data on income and financial behaviors may be subject to recall bias."
    - "The longitudinal period of three years may not capture long-term efficacy of adaptive strategies."
  mapping_rationale: During the systematic scan, the paper was flagged as highly relevant to the domains of Behavioral Profiling & Classification (specifically 5.A and 5.C) due to its focus on how workers adapt behaviors to income volatility and the influence of psychological factors. It also provides high relevance to Budget Recommendation (7.A) as it identifies key adaptive strategies like flexible budgeting. Medium relevance was assigned to topics related to Financial Behavior (1.C), Seasonal Patterns (2.B), and Savings Management (13.A), as the findings directly inform these areas. Low relevance was given to Expense Categorization (3.A), Predictive Modeling (6.A), and Forecasting (6.B), as the paper discusses concepts related to these topics but does not propose new frameworks or algorithms. Domains such as Mobile-First Design, Data Privacy, and User Retention were considered but rejected as the paper does not address them.
limitations:
  - "The study relies on self-reported income and financial strategies, which may introduce social desirability bias. [unacknowledged]"
  - "The sample, while diverse, is limited to platform-based gig workers in India, potentially limiting generalizability to other gig economy contexts."
  - "Potential multicollinearity noted in VIF values, particularly for income volatility and its interaction term, suggests caution in interpreting individual coefficients."
remember_this:
  - "Higher income volatility drives gig workers toward adaptive financial strategies."
  - "Financial literacy significantly improves the effectiveness of financial planning."
  - "Risk tolerance positively influences adaptive planning, while cognitive bias hinders it."
  - "Educational attainment and family status are key demographic predictors of financial behavior."
  - "num: Income volatility and financial literacy interaction has a beta coefficient of 0.161."
```
---

## Paper 20: Scrivano_summarized.md

**Source File:** `Scrivano_summarized.md`

```yaml
paper_id: 10.13140/RG.2.2.34766.78490
designation: international
title: Time-Series Forecasting Using Deep Learning and Data Mining Models
authors: Scrivano, A.
year: 2025
venue: Unknown
odin_topics:
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 12.A
  - 12.B
  - 12.C
tldr: A review of deep learning and data mining models for time-series forecasting, comparing their strengths, limitations, and performance across finance, energy, and retail domains.
problem_and_motivation: Time-series forecasting is critical across finance, healthcare, and engineering, yet traditional statistical models like ARIMA struggle with non-linear dynamics and complex patterns. The emergence of deep learning and advanced data mining offers new opportunities to improve prediction accuracy and efficiency.
approach:
  - Data sourced from public and proprietary financial, energy consumption, and retail transaction datasets.
  - Preprocessing included differencing, smoothing, logarithmic transformations, and feature extraction of lagged variables and seasonal indicators.
  - Models evaluated included RNNs, LSTMs, TCNs, Transformers, Random Forests, and Gradient Boosting Machines.
  - Training used backpropagation with Adam or RMSProp, and data was split chronologically into training, validation, and test sets.
  - Evaluation metrics included MAE, RMSE, MAPE, and quantile loss functions for probabilistic forecasts.
findings:
  - num: Transformers achieved a 12% reduction in MSE and 17% reduction in MAE compared to recurrent and convolutional models on retail datasets.
  - num: LSTM models reduced mean absolute error by 15% in web traffic prediction compared to conventional methods.
  - num: TCNs attained 20% higher accuracy in early-stage anomaly detection for industrial monitoring.
  - Gradient Boosting Machines consistently outperformed Random Forests across all domains, especially in retail sales forecasting.
  - Probabilistic forecasting with quantile loss functions highlighted Transformers and GBMs as superior in uncertainty estimation.
key_figures_tables:
  - Table 1: Comparative evaluation of LSTM, TCN, and Transformer models on retail data → Transformer achieved lowest MAE and MSE.
  - Table 2: Performance comparison of RNN, LSTM, TCN, and Transformer across energy, finance, and retail → Transformer consistently shows superior accuracy.
  - Table 3: Direct comparison of Random Forest and Gradient Boosting Machines → GBM consistently achieves lower error metrics.
  - Figure 2: Temporal investigation of forecast errors in retail → Transformers show the most stable error reduction.
  - Figure 4: Quantile loss assessment for probabilistic models → Transformers exhibit strongest capability in handling predictive uncertainty.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: RNN
    definition: Recurrent Neural Network
  - term: LSTM
    definition: Long Short-Term Memory
  - term: TCN
    definition: Temporal Convolutional Network
  - term: GBM
    definition: Gradient Boosting Machine
  - term: MAE
    definition: Mean Absolute Error
  - term: RMSE
    definition: Root Mean Squared Error
  - term: MAPE
    definition: Mean Absolute Percentage Error
critical_citations:
  - "[Hochreiter & Schmidhuber, 1997] — Introduced LSTM architecture for sequential data."
  - "[Vaswani, 2017] — Introduced Transformer architecture with self-attention mechanism."
  - "[Friedman, 2001] — Developed Gradient Boosting Machine ensemble method."
  - "[Lea, 2017] — Proposed TCNs for action segmentation and sequence modeling."
  - "[Breiman, 2001] — Established Random Forests as robust ensemble method."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Compares deep learning and data mining models for sequential spending prediction.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Evaluates LSTM, TCN, Transformer, and GBM on time-series forecasting tasks.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Provides performance benchmarks for algorithms that could underpin budget recommendation.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Evaluation of forecasting models informs budget recommendation accuracy.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Detailed discussion of evaluation metrics (MAE, RMSE, MAPE) applicable to PFMS.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides empirical comparison of multiple forecasting algorithms under identical conditions.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Discusses domain-specific metrics like MARD for perishable inventory, analogous to budget adherence.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Mentions anomaly detection in industrial monitoring but not personal finance.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: Not addressed.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Mentions privacy in future directions but not as core contribution.
  contribution: This review provides a comprehensive benchmark of state-of-the-art forecasting models, offering quantitative evidence for selecting LSTM, Transformer, or GBM for predictive modules in Odin. The comparative performance data across multiple domains directly justifies algorithm choice for spending forecasting, anomaly detection, and budget recommendation. The discussion of evaluation metrics and probabilistic forecasting frames how Odin's algorithmic modules should be assessed and validated.
  directly_justifies:
    - LSTM models effectively capture non-linear dynamics in sequential data, relevant for spending patterns.
    - Transformers reduce prediction error by 12-17% over recurrent models in multi-step forecasting.
    - Gradient Boosting Machines offer a computationally efficient alternative with strong interpretability.
    - TCNs achieve 20% higher accuracy in anomaly detection, suitable for identifying unusual spending.
  limits:
    - Limited generalizability to personal finance-specific spending data, as benchmarks use energy and retail.
    - Does not address cold-start problems or user-level behavioral profiles.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to Predictive Modeling (6.A), Forecasting Algorithms (6.B), and Algorithm Evaluation (12.B) due to its direct comparison of forecasting models on time-series data. Medium relevance was assigned to Budgeting Strategies (7.A), Budget Recommendation (7.B), and Evaluation Frameworks (12.A, 12.C) as the performance data can inform algorithm selection and validation for these Odin modules. The paper touches on Anomaly Detection (8.A) contextually through industrial examples but not personal finance, and Mobile Design (9.A), Data Privacy (10.A), and Retention (11.A) were rejected as not addressed. Borderline cases included forecasting methods applicable to spending forecasting (6.B) and budget recommendation (7.B), resolved by assigning high to the core forecasting topics and medium to the downstream budget topics. Overall, the paper is highly relevant for informing Odin's predictive algorithm selection and evaluation methodology.
limitations:
  - Models were not tested on personal financial transaction data. [unacknowledged]
  - No discussion of handling irregular or sparse spending sequences common in personal finance.
  - Computational constraints of Transformers may limit deployment in mobile-first PFMS.
remember_this:
  - LSTM and Transformer models excel at capturing complex temporal dependencies.
  - Transformers achieved a 12% reduction in MSE over recurrent models on retail data.
  - Gradient Boosting Machines offer interpretable and computationally efficient forecasting.
  - TCNs provide superior anomaly detection accuracy in industrial sensor data.
  - Evaluation metrics like MAE, RMSE, and MAPE are critical for model comparison.
```
---

## Paper 21: Han & Ko_summarized.md

**Source File:** `Han & Ko_summarized.md`

```yaml
paper_id: "10.3390/su17208976"
designation: "international"
title: "Digital Financial Services and Sustainable Development: Temporal Trade-Offs and the Moderating Role of Financial Literacy"
authors: "Han, J.; Ko, D."
year: 2025
venue: "Sustainability"
odin_topics:
  - "5.A"
  - "9.A"
  - "9.B"
  - "13.A"
  - "13.B"
tldr: "Mobile financial services usage creates a sustainability paradox: it undermines short-term financial discipline while enhancing long-term planning, with objective financial literacy buffering risks and perceived ability exacerbating them."
problem_and_motivation: "The impact of MFS on sustainable financial behavior is poorly understood, with existing research fragmented and failing to account for simultaneous opposite effects across temporal dimensions. The moderating role of distinct financial literacy dimensions in digital contexts remains unclear, especially regarding overconfidence. This gap hinders the design of policies and tools that promote sustainable financial behaviors in increasingly digital environments."
approach:
  - "Analyzes 21,757 U.S. adults from the 2021 National Financial Capability Study using weighted survey data."
  - "Uses ordered logistic regression for short-term and long-term financial behavior indices and binary logistic regression for individual behaviors."
  - "Tests moderation by including interaction terms between MFS usage and each financial literacy dimension (OK, SK, PA)."
  - "Includes demographic and socioeconomic controls and conducts robustness checks (subgroup analyses, OLS comparisons, weighted/unweighted)."
findings:
  - "num: MFS financial management tools decrease short-term discipline odds by 31.2% (OR=0.688) and increase long-term planning odds by 37.9% (OR=1.379)."
  - "num: Perceived ability has the strongest positive association with short-term behavior (OR=2.560) but paradoxically amplifies MFS's negative short-term effects (interaction B=-0.085, p<0.001)."
  - "num: Objective knowledge buffers adverse short-term MFS effects (interaction B=0.013, p<0.05)."
  - "All financial literacy dimensions positively associate with both short-term and long-term behaviors."
  - "The dual pattern is robust across age, gender, and income subgroups and alternative model specifications."
key_figures_tables:
  - "Table 3: Main effects of MFS and literacy on short-term and long-term indices → MFS has opposite effects by temporal dimension."
  - "Table 5: Moderation effects of literacy dimensions → OK protects short-term, PA amplifies risk."
  - "Figure 1: Conceptual model of MFS, literacy, and temporal behaviors → visualizes the hypothesized relationships."
key_equations:
  - equation: "ln(P(Y_i ≤ j) / P(Y_i > j)) = α_j - β_1 MFS_i - β_2 OK_i - β_3 SK_i - β_4 PA_i - γ X_i"
    explanation: "Ordered logit for ordinal behavior indices."
  - equation: "ln(P(Y_i = 1) / P(Y_i = 0)) = α + β_1 MFS_i + β_2 OK_i + β_3 SK_i + β_4 PA_i + γ X_i"
    explanation: "Binary logit for individual behaviors."
  - equation: "ln(P(Y_i ≤ j) / P(Y_i > j)) = α_j - β_1 MFS_i - β_2 FL_i - β_3 (MFS_i × FL_i) - γ X_i"
    explanation: "Moderation model with interaction term."
definitions:
  - term: "MFS"
    definition: "Mobile Financial Services, including payments, transfers, account management, and planning tools."
  - term: "OK"
    definition: "Objective Knowledge, measured by six core financial concepts."
  - term: "SK"
    definition: "Subjective Knowledge, self-assessed confidence in financial knowledge."
  - term: "PA"
    definition: "Perceived Ability, financial self-efficacy on a 4-point scale."
  - term: "CLT"
    definition: "Construal Level Theory, explaining psychological distance effects on decision-making."
  - term: "DPT"
    definition: "Dual Process Theory, distinguishing System 1 (automatic) and System 2 (deliberative) processing."
  - term: "SCT"
    definition: "Social Cognitive Theory, emphasizing self-regulation and self-efficacy."
critical_citations:
  - "[Trope & Liberman, 2010] — CLT explains psychological distance effects."
  - "[Kahneman, 2003] — DPT distinguishes System 1 and 2."
  - "[Bandura, 1989] — SCT provides self-regulation framework."
  - "[Lusardi & Mitchell, 2014] — financial literacy measurement and importance."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Identifies distinct short-term and long-term behavioral patterns and literacy moderators, informing profile design."
    - code: "9.A"
      name: "Mobile‑First Design Principles and Rationale"
      relevance: "medium"
      justification: "Provides evidence of MFS behavioral impacts that justify design choices like friction mechanisms and automated saving."
    - code: "9.B"
      name: "Mobile UX Design for Personal Finance"
      relevance: "medium"
      justification: "Highlights how mobile interface features (e.g., reduced friction) affect user behavior, directly relevant to UX design."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "low"
      justification: "Measures savings behaviors (emergency funds, retirement, investments) but does not address goal management features."
    - code: "13.B"
      name: "Debt Management in PFMS"
      relevance: "low"
      justification: "Includes overdraft and bill payment as outcomes but lacks discussion of debt management strategies."
  contribution: "This paper justifies the inclusion of spending alerts and friction mechanisms in Odin's expense tracking module to counteract short-term discipline loss from digital convenience. It supports integrating objective financial literacy assessments during onboarding to personalize risk warnings and educational content. The paradoxical effect of perceived ability suggests that Odin should calibrate confidence-based recommendations with caution and avoid over-reliance on user self-assessed knowledge. The dual temporal effect informs the design of separate short-term and long-term goal setting features within the budgeting and savings modules."
  directly_justifies:
    - "MFS usage reduces short-term financial discipline, supporting the need for friction in digital spending interfaces."
    - "Objective knowledge buffers adverse MFS effects, justifying financial literacy content in PFMS."
    - "Perceived ability amplifies MFS risks, cautioning against overconfidence in user profiles."
    - "MFS usage enhances long-term planning, supporting automated savings and investment features."
  limits:
    - "Cross-sectional design limits causal inference."
    - "Self-reported behaviors may introduce social desirability bias."
    - "U.S. sample limits generalizability to other cultural and regulatory contexts."
    - "Financial literacy measures developed for traditional contexts may not capture digital-specific competencies."
  mapping_rationale: "Systematic scan of all 12 functional domains and associated topic codes identified 5.A, 9.A, 9.B, 13.A, and 13.B as relevant. Domains related to Filipino cultural context (2.A-D), expense categorization (3.A-C), forecasting (6.A-B), budget recommendation (7.A-D), anomaly detection (8.A-C), data privacy (10.A-B), user retention (11.A-B), and system evaluation (12.A-C) were rejected because the paper does not address those aspects. 5.A received medium relevance for its behavioral profiling insights; 9.A and 9.B received medium for direct MFS usage and UX implications; 13.A and 13.B received low because they only measure savings/debt outcomes without management strategies. Borderline cases: the paper touches on savings and debt but only as dependent variables, not as management processes, hence low. Overall, the paper provides valuable behavioral evidence to inform Odin's design, particularly for mitigating short-term risks and leveraging long-term benefits."
limitations:
  - "Cross-sectional design limits causal inference."
  - "Self-reported behaviors may introduce social desirability bias."
  - "U.S. sample limits generalizability to other cultural and regulatory contexts."
  - "Financial literacy measures developed for traditional contexts may not capture digital-specific competencies."
  - "Racial/ethnic heterogeneity not examined due to representativeness limitations."
remember_this:
  - "MFS management tools decrease short-term discipline by 31% but boost long-term planning by 38%."
  - "Objective knowledge protects against MFS short-term risks, while perceived ability exacerbates them."
  - "Financial literacy dimensions positively associate with both short-term and long-term behaviors."
  - "Digital convenience creates a sustainability paradox requiring balanced design."
```
---

## Paper 22: Ashrafuzzaman et al_summarized.md

**Source File:** `Ashrafuzzaman et al_summarized.md`

```yaml
paper_id: 10.63125/z9s39s47
designation: international
title: AI-POWERED PERSONALIZATION IN DIGITAL BANKING: A REVIEW OF CUSTOMER BEHAVIOR ANALYTICS AND ENGAGEMENT
authors: Ashrafuzzaman, M.; Parveen, R.; Sumiya, M. A.; Rahman, A.
year: 2025
venue: American Journal of Interdisciplinary Studies
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 12.A
tldr: A systematic review of 111 articles finds AI-driven personalization in digital banking enhances customer engagement, satisfaction, and retention, yet faces challenges in measurement, governance, and cross-cultural adaptation.
problem_and_motivation: Digital banking has evolved, yet integrating AI to deliver personalized customer experiences based on behavior analytics remains fragmented. The literature lacks a comprehensive synthesis of AI techniques, their impact on engagement, and the associated governance and cultural challenges. This review consolidates existing research to provide a structured understanding for future development.
approach:
  - A systematic literature review was conducted following the PRISMA 2020 guidelines.
  - Searches were performed in Scopus, Web of Science, IEEE Xplore, ScienceDirect, and Google Scholar in March 2025.
  - The search strategy used Boolean operators with targeted keywords related to AI, personalization, and digital banking.
  - Initial database searches yielded 1,248 records, which were screened for duplicates and relevance.
  - After title/abstract and full-text screening, 111 peer-reviewed articles published between 2014 and 2024 were included for synthesis.
findings:
  - num: 92 of 111 reviewed articles emphasized that AI-driven personalization is integral to digital banking transformation.
  - num: 81 articles identified customer behavior analytics as the primary driver of AI-powered personalization.
  - num: 69 articles focused on predictive analytics, with models used to anticipate customer needs and improve engagement.
  - num: 74 articles addressed the positive impact of AI-personalization on customer satisfaction, retention, and lifetime value.
  - num: 63 articles highlighted ethical, legal, and governance challenges, including data privacy and algorithmic transparency.
  - num: 58 articles discussed AI-personalization in emerging markets, noting constraints like infrastructure and innovations such as alternative data use.
  - num: 66 articles identified conceptual and methodological gaps, including inconsistent measurement frameworks and a lack of longitudinal studies.
key_figures_tables:
  - Figure 1: AI's role in transforming digital banking → AI integrates with mobile apps, ML, and data analytics for personalization.
  - Figure 2: Dimensions of AI personalization in banking → Personalization is multidimensional, involving technology, behavior, and ethics.
  - Figure 3: Six key components in digital banking → AI works with data processing, segmentation, and customer interaction.
  - Figure 4: Trends in AI techniques for personalization → ML, NLP, DL, and recommender systems are increasingly applied.
  - Figure 5: Predictive customer analytics → Predictive models use behavioral data to forecast needs and guide personalization.
  - Figure 6: Customer micro-segmentation → Behavioral models create dynamic micro-segments for targeted personalization.
  - Figure 7: Impact of AI-powered personalization on engagement → Personalization increases retention, satisfaction, and lifetime value.
  - Figure 8: AI personalization vs infrastructure maturity in emerging markets → Emerging markets show innovation despite infrastructural challenges.
  - Figure 9: Research gaps in AI-personalized digital banking literature → Gaps include inconsistent metrics, lack of longitudinal studies, and limited cross-cultural analysis.
  - Figure 10: Article selection based on PRISMA protocol → PRISMA flow diagram showing screening and inclusion of 111 articles.
  - Figure 11: Distribution of reviewed articles by focus area → Highest focus on AI techniques, engagement outcomes, and behavioral analytics.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Artificial Intelligence (AI)
    definition: Simulation of human intelligence processes by machines, especially computer systems capable of learning, reasoning, and self-correction.
  - term: Machine Learning (ML)
    definition: A subset of AI that enables systems to learn and improve from experience without explicit programming.
  - term: Natural Language Processing (NLP)
    definition: A branch of AI that helps computers understand, interpret, and manipulate human language.
  - term: Personalization
    definition: Customization of financial products and services based on user profiles, risk tolerance, and spending behavior.
  - term: Customer Behavior Analytics
    definition: The process of collecting, interpreting, and applying insights from consumer interactions to deliver tailored banking services.
  - term: Predictive Analytics
    definition: The use of data, statistical algorithms, and machine learning techniques to identify the likelihood of future outcomes based on historical data.
  - term: Digital Banking
    definition: The digitization of all traditional banking activities and services that were historically available only to customers physically present at a bank branch.
  - term: Customer Engagement
    definition: The quality of personalized interactions enabled by AI systems, defined by how well banks predict and adapt to individual needs.
critical_citations:
  - "[Huang & Rust, 2018] — AI as a transformative force in service delivery."
  - "[van Esterik-Plasmeijer & van Raaij, 2017] — Foundation for trust and loyalty in banking."
  - "[Ameen et al., 2020] — Customer experiences in the age of artificial intelligence."
  - "[Nguyen et al., 2021] — Effect of AI quality on customer experience and brand relationship."
  - "[Hollebeek & Macky, 2019] — Digital content marketing's role in fostering engagement and trust."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: The review discusses how AI analyzes transaction data to categorize spending and tailor services.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: The review discusses dynamic segmentation and behavior-based classification, informing category design.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: The paper reviews the landscape of AI-driven personalization in digital banking, mapping existing systems.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: A major focus of the review is identifying limitations in existing AI personalization systems, including metrics and governance.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: The paper extensively covers how AI uses behavioral analytics to create dynamic customer profiles.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: contextual
      justification: The review mentions the challenge of profiling new users, though not specifically as a cold-start problem.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: The paper details segmentation strategies and micro-targeting using classification techniques like K-means clustering.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Predictive analytics is a core theme, with models used to forecast customer needs and behavior.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: The review discusses ML and DL algorithms for real-time data processing and behavior forecasting.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: AI-powered personalization includes budgeting tools and spending analysis, as mentioned in the review.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: The review discusses personalized financial recommendations, which can include budget advice.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Anomaly detection is mentioned in the context of fraud detection, but not a central focus.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: The review mentions behavioral anomaly detection, but does not detail specific algorithms.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: AI personalization is discussed in the context of mobile banking apps and digital interfaces.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: The review notes that AI enhances user experience in mobile apps through customization.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: A significant portion of the review addresses data privacy, security, and regulatory compliance.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Trust is a central theme, with detailed discussion on transparency, consent, and control.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: Customer engagement is a primary focus, with analysis of how AI personalization drives interaction.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: high
      justification: The review links personalization to increased retention and discusses design strategies for engagement.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: The review explicitly identifies inconsistent measurement frameworks as a major research gap.
  contribution: This paper provides a comprehensive synthesis of AI personalization in digital banking, systematically organizing the literature into seven core domains. It offers a structured framework that Odin can use to understand the state-of-the-art in behavior analytics, predictive modeling, and personalization techniques. The review's findings on engagement, trust, and emerging market adaptations directly inform Odin's design for customer-centric features. The identified research gaps, particularly in measurement and longitudinal analysis, guide Odin's evaluation strategy for its algorithmic modules. Finally, the emphasis on ethical governance and user control provides a basis for Odin's privacy and trust frameworks.
  directly_justifies:
    - "AI-driven personalization improves customer satisfaction, retention, and perceived value by delivering individualized services."
    - "Customer behavior analytics is a primary driver of AI personalization, using user interactions and transaction histories."
    - "Predictive models are used to anticipate customer needs and deliver proactive, tailored services."
    - "Transparency, consent, and control are critical components for managing customer trust in AI systems."
    - "Inconsistent measurement frameworks and a lack of longitudinal studies are key gaps in the literature."
  limits:
    - "The review is based on a systematic analysis of 111 articles, but does not include primary empirical data from the Philippines."
    - "The findings on emerging markets are based on a subset of studies and may not be fully generalizable to all contexts."
    - "The review identifies but does not resolve the methodological inconsistencies in measuring personalization and engagement."
  mapping_rationale: During the systematic scan of all 12 functional domains and their associated topic codes, this paper was flagged as highly relevant for multiple domains. The paper provides citeable claims that inform Odin's design for Behavioral Profiling (Topic 5.A, 5.C), Spending Forecasting (6.A, 6.B), Budget Recommendation (7.B), Anomaly Detection (8.A), Mobile Design (9.A, 9.B), Data Privacy & Trust (10.A, 10.B), Engagement & Retention (11.A, 11.B), and System Evaluation (12.A). The relevance was assigned as high for topics like 5.A, 6.A, and 11.A because the paper directly addresses these core concerns. For topics like 7.A and 9.A, relevance was deemed medium as the paper provides supporting contextual evidence. Topics like 8.B and 5.B were assigned low or contextual relevance because they are mentioned but not a primary focus. Borderline cases were encountered with Topic 2.B (Seasonal Spending), which the paper touches on in the context of behavioral triggers, but was ultimately rejected due to insufficient explicit coverage. The domains of Filipino cultural practices (Topics 2.A, 2.C) were considered but rejected as the paper does not specifically address the Philippines. Overall, the paper is highly relevant to Odin's technological, behavioral, and evaluation-oriented domains, providing a strong foundation for system design and research direction.
limitations:
  - "Inconsistent measurement frameworks for personalization and engagement across studies. [unacknowledged]"
  - "Lack of longitudinal studies to evaluate long-term AI effectiveness and behavioral adaptation. [unacknowledged]"
  - "Limited attention to cross-cultural differences, with most studies from Western or technologically advanced countries."
  - "The review does not empirically test the effectiveness of the AI techniques discussed."
  - "The paper synthesizes existing literature but does not propose a novel framework or model for Odin."
remember_this:
  - "AI-driven personalization increases customer satisfaction, retention, and lifetime value."
  - "Behavioral analytics is the primary driver of AI personalization in digital banking."
  - "Data privacy, transparency, and user control are critical for building trust."
  - "num: 92 out of 111 studies affirm AI personalization as integral to banking transformation."
  - "Measurement inconsistencies and a lack of longitudinal studies are key research gaps."
```
---

## Paper 23: Banta_summarized.md

**Source File:** `Banta_summarized.md`

```yaml
paper_id: 10.1080/00330124.2024.2410764
designation: international
title: Caring for Indebted Migrant Workers: Financial Literacy Training, Debt, and Filipino Migrant Workers in Dubai
authors: Banta, V. L.
year: 2025
venue: The Professional Geographer
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.C
  - 2.D
  - 4.A
  - 4.B
  - 5.B
  - 7.A
  - 10.B
tldr: Financial literacy training for OFWs in Dubai, framed as care, individualizes debt by emphasizing personal responsibility and obscures the structural conditions that create and perpetuate migrant indebtedness.
problem_and_motivation: Migrant worker debt is increasing, yet state and private initiatives often frame it as a personal failing rather than a structural issue. This obscures the political-economic conditions that produce and maintain debt among Filipino migrant workers in Dubai and limits the potential for collective action.
approach:
  - Qualitative study based on interviews with thirty Filipino migrant workers in Dubai and Abu Dhabi.
  - Examines the financial literacy and entrepreneurship training conducted by a civil society organization called IGNITE.
  - Analyzes how IGNITE's training frames debt as a result of personal irresponsibility, conspicuous consumption, and excessive care for family.
  - Applies feminist care ethics and the concept of "troubling care" to critique the training's depoliticizing effects.
  - Situates the analysis within the broader political economy of Philippine labor brokerage and UAE labor policies.
findings:
  - num: IGNITE volunteers dismissed a case of 900,000 AED (CDN$332,515) in debt as simple personal irresponsibility.
  - Financial literacy training promotes "sacrifice" and "delayed gratification" as virtues, reinforcing the "economic and ethical normativity of sacrifice" for OFWs.
  - The training obscures how debt finances migration, with families pawning land (e.g., Leah) to support workers seeking employment.
  - IGNITE's focus on curbing "conspicuous consumption" ignores the differential impact of rising living costs and lack of affordable housing on OFWs.
  - Migrant worker debt is criminalized through travel bans, deportation, and imprisonment, yet this is rarely addressed in the training.
  - The training overlooks how UAE financial regulations, like tightened credit criteria, push lower-income OFWs to rely on "loan sharks" or employers.
  - Some IGNITE participants valued setting financial goals and saving for their own future, but the training's structural critiques remain absent.
key_figures_tables:
  - "None."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: OFW
    definition: Overseas Filipino Worker.
  - term: UAE
    definition: United Arab Emirates.
  - term: FLE
    definition: Financial Literacy Education.
  - term: GCC
    definition: Gulf Cooperation Council.
critical_citations:
  - "[Raghuram, 2016] — foundational for the concept of 'troubling care'."
  - "[Crane and Lawson, 2020] — defines 'conflicted care'."
  - "[Bautista, 2015] — explains the 'ethical normativity of sacrifice' for OFWs."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Directly studies Filipino migrant workers, including professional and skilled OFWs.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Details the financial obligations, debt structures, and remittance practices of OFWs.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Provides rich qualitative data on spending, saving, and debt management behaviors.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Analyzes culturally specific practices like remittances and "balikbayan" boxes as sites of financial care and debt.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: Mentions financial crises and periods of economic recession, but does not focus on seasonal patterns explicitly.
    - code: 2.C
      name: User-Declared Financial Preferences
      relevance: medium
      justification: Touches on OFW priorities like saving for family vs. self, but does not focus on user-declared system preferences.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: Discusses expenses for family needs and emergencies, but not specifically spending cycles tied to occasions.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Examines a specific civil society program (IGNITE) as a form of financial literacy intervention.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Critiques IGNITE's training for individualizing structural debt problems and ignoring punitive financial regulations.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: medium
      justification: Discusses how migrants are targeted as ideal subjects for financial training, a form of classification.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: IGNITE teaches budgeting and saving strategies, but the paper critiques their normative underpinnings.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Addresses migrant vulnerability to untrustworthy lenders and the lack of trust in state protections.
  contribution: |
    This paper provides a critical qualitative framework for understanding the sociocultural and political-economic dimensions of debt among Filipino migrant workers, which is essential for Odin's design of behavioral profiles (1.A, 1.B, 1.C) and culturally informed expense categorization (2.A, 3.A). It directly justifies the need for Odin's budget recommendation module (7.A) to account for structural constraints like remittance obligations and lack of affordable credit. The paper's critique of financial literacy interventions informs Odin's approach to user trust (10.B), highlighting that systems must avoid victim-blaming. It also provides a cautionary example for Odin's retention mechanisms (11.B), showing that care interventions can be perceived as patronizing if they ignore structural realities.
  directly_justifies:
    - "Debt among OFWs is a structural issue, not just a personal financial management problem."
    - "Financial literacy training can obscure the political-economic conditions that produce and maintain debt."
    - "Migrant workers are often targeted by predatory lenders in the absence of supportive financial infrastructure."
    - "Curbing remittances is a politically and culturally charged recommendation, not a simple budgeting fix."
  limits:
    - "The study is qualitative and based on a single civil society organization; findings may not be generalizable."
    - "The paper does not propose a technical solution or algorithmic approach for debt management."
  mapping_rationale: |
    During the systematic scan across all 12 functional domains, the paper's strongest relevance was found in the Filipino Cultural Context (2) and Existing Systems & Gaps (4) domains due to its deep qualitative analysis of OFW financial practices and critique of IGNITE's intervention. Topics 1.A, 1.B, and 1.C were assigned 'high' relevance because the paper directly examines the demographic, financial structure, and behavior of Filipino young professionals (as a subset of OFWs). For 2.A, the analysis of remittances and "balikbayan" boxes provided high relevance. Topics 2.B and 2.D were considered borderline; while the paper discusses cyclical financial crises and family obligations that could be seen as "occasions," it lacks explicit seasonal spending data, hence 'medium' and 'contextual' respectively. The paper's critique of existing systems (4.A, 4.B) was highly relevant. The Behavioral Profiling domain (5) was relevant in how the training classifies migrants as "financially immature" (5.B, 'medium'). The Budget Recommendation domain (7) saw relevance in the paper's discussion of normative budgeting strategies (7.A, 'medium'). Data Privacy (10.B) was relevant due to the lack of trust and predatory practices discussed. Domains related to predictive modeling (6), anomaly detection (8), mobile design (9), evaluation (12), and savings/debt management algorithms (13) were considered and rejected as the paper provides no quantitative, algorithmic, or design-focused insights for these areas. Overall, the paper is highly relevant for informing Odin's behavioral, cultural, and systemic understanding of its target users, but not for direct technical implementation.
limitations:
  - "The study focuses on a specific group of OFWs in Dubai, which may not represent all Filipino young professionals."
  - "The paper does not offer quantitative data on the effectiveness of financial literacy training."
  - "It does not address the specific needs of users who are not migrant workers."
remember_this:
  - "IGNITE frames debt as a personal failing, obscuring structural causes."
  - "Financial literacy training promotes sacrifice and delayed gratification as core values."
  - "Migrant debt is criminalized through travel bans and imprisonment in the UAE."
  - "The paper reveals the 'hidden geographies' of how debt finances and sustains migration."
  - "Care initiatives can be 'conflicted' and may not address the root causes of financial precarity."
```
---

## Paper 24: Hidayat et al_summarized.md

**Source File:** `Hidayat et al_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international
title: Gen-Z Saving Behavior: The Role Financial Literacy in Digital Payment Mediated
authors: Hidayat, A.; Nurhadi N, M.; Nurhidayah; Tanjung, A.; Muliani, M.; Musdalifah
year: 2025
venue: ICONBIT 2025
odin_topics:
  - 1.C
  - 2.B
  - 2.D
  - 3.B
  - 5.A
  - 5.C
  - 9.A
  - 10.A
  - 11.A
  - 12.A
  - 13.A
tldr: Financial literacy does not directly affect saving behavior but significantly influences digital payment adoption, which in turn mediates the relationship between literacy and savings.
problem_and_motivation: Generation Z exhibits low saving rates and high digital payment usage, yet the interaction between financial literacy, digital payment adoption, and saving behavior remains underexplored. Understanding this mediation is crucial for designing interventions to improve financial resilience among young Filipinos.
approach:
  - Quantitative survey of 150 Generation-Z respondents aged 18–25 in Makassar City who use digital payments and have bank savings accounts.
  - Data collected via purposive sampling using a structured questionnaire with 15 indicators for financial literacy, digital payment usage, and saving behavior.
  - Analysis performed using Partial Least Squares Structural Equation Modeling (PLS-SEM) with SmartPLS software.
  - Validity and reliability assessed via outer loadings (>0.7), Cronbach's alpha (>0.6), composite reliability (>0.7), and AVE (>0.5).
  - Direct and indirect effects tested using bootstrapping with t-statistics and p-values.
findings:
  - "num: Financial literacy has no direct significant effect on saving behavior (p = 0.630)."
  - "num: Financial literacy significantly influences digital payment adoption (p = 0.000)."
  - "num: Digital payment significantly affects saving behavior (p = 0.000)."
  - "num: Digital payment fully mediates the relationship between financial literacy and saving behavior (indirect effect = 0.770, p = 0.000)."
  - Digital payment users are driven by convenience and social trends, not purely financial knowledge.
  - Digital payments reduce the psychological pain of paying, increasing spending frequency.
  - Financially literate Gen-Z use digital payment features for planning, not just consumption.
  - External factors like hedonism, social pressure, and promotions often override financial literacy in spending decisions.
key_figures_tables:
  - "Table 1: Respondent profile shows 45% aged 23-25, 59% male."
  - "Table 2: Outer loadings all >0.7, confirming construct validity."
  - "Table 3: Cronbach's alpha (0.888-0.932) and AVE (0.691-0.788) confirm reliability and validity."
  - "Table 4: R² for Digital Payment is 0.822 (strong) and Saving Behavior is 0.635 (strong)."
  - "Table 5: Direct effect shows financial literacy to saving behavior is not significant (p=0.630)."
  - "Table 6: Indirect effect via digital payment is significant (p=0.000)."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "PLS-SEM"
    definition: "Partial Least Squares Structural Equation Modeling, a statistical method for analyzing complex cause-effect relationships with latent variables."
  - term: "AVE"
    definition: "Average Variance Extracted, a measure of convergent validity in factor analysis."
  - term: "QRIS"
    definition: "Quick Response Code Indonesian Standard, a national standard for QR code payments in Indonesia."
critical_citations:
  - "[Lusardi & Mitchell, 2020] — Foundational link between financial literacy and financial behavior."
  - "[Katadata Insight Center, 2021] — Key evidence on Gen Z low saving rates in Indonesia."
  - "[OJK, 2024] — Indonesian national survey data on Gen Z financial literacy."
relevance:
  topics:
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Directly examines saving behavior determinants in Gen Z, a core demographic for Odin."
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "medium"
      justification: "Mentions discounts and promotions as triggers for impulsive spending, relevant to cyclical patterns."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "contextual"
      justification: "While focused on Makassar, the discussion of social and lifestyle influences on spending can contextualize Filipino spending cycles."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      relevance: "low"
      justification: "Tangentially mentions budgeting features in digital payment apps, relevant to category design."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Classifies behavioral profiles based on literacy and digital payment usage, providing a basis for profiling."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "The PLS-SEM approach offers a methodological framework for classifying behavioral relationships, though not a classification algorithm per se."
    - code: "9.A"
      name: "Mobile‑First Design Principles and Rationale"
      relevance: "medium"
      justification: "Highlights the role of digital payment apps in shaping financial behavior, supporting mobile-first design considerations."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "low"
      justification: "Mentions trust in digital payment platforms linked to data security, relevant to privacy concerns."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "medium"
      justification: "Discussion of how digital payment features (cashback, tracking) engage users, relevant to retention."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "The PLS-SEM framework can be adapted to evaluate algorithm performance and user impact."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "high"
      justification: "Directly addresses saving behavior and the mediating role of digital tools, central to savings goal management."
  contribution: "This paper directly informs Odin's behavioral profiling module by establishing that financial literacy does not directly drive saving behavior, but rather through digital payment usage. It justifies Odin's focus on tracking digital payment transactions as a proxy for saving behavior. The findings support Odin's approach of using mobile-first design to embed financial management features that can nudge users toward saving. The mediation model provides a framework for evaluating Odin's intervention effectiveness. The reliance on self-reported data underscores the need for objective spending data in Odin's recommendation engine."
  directly_justifies:
    - "Financial literacy alone is insufficient; digital payment usage mediates saving behavior."
    - "Digital payment adoption requires features that facilitate transaction tracking and budgeting."
    - "Gen Z saving behavior is influenced by perceived convenience and social trends."
    - "Trust in digital systems is influenced by perceived security and provider credibility."
  limits:
    - "The study is limited to Makassar City, which may not represent all Filipino Gen-Z."
    - "Self-reported survey data may suffer from social desirability and recall bias."
    - "The cross-sectional design cannot establish causality, only association."
    - "Does not consider objective spending data or actual savings balances."
  mapping_rationale: "Systematic scan across all 12 functional domains and their topic codes identified relevance primarily in financial behavior (1.C), behavioral profiling (5.A, 5.C), and savings management (13.A). The paper's mediation model directly supports design decisions for Odin's behavioral classification (5.C) and savings goal management (13.A) modules. Topics like seasonal spending (2.B) and engagement (11.A) were flagged as medium relevance due to discussions of promotional incentives and digital features. Domains such as forecasting (6.A/B), anomaly detection (8.A/B/C), and constrained optimization (7.C/D) were rejected as the paper does not address predictive modeling or algorithmic allocation. The overall relevance is high for understanding user behavior but low for direct algorithmic implementation."
limitations:
  - "Limited geographic scope; findings may not generalize to all Filipino Gen-Z."
  - "Self-reported measures may not reflect actual financial behavior."
  - "Cross-sectional design prevents causal inference. [unacknowledged]"
  - "Does not examine the specific features of digital payment apps that promote saving. [unacknowledged]"
  - "Potential sampling bias due to purposive sampling. [unacknowledged]"
remember_this:
  - "Financial literacy does not directly increase saving behavior."
  - "Digital payment usage fully mediates the literacy-saving relationship."
  - "Digital payments reduce the pain of paying, increasing spending frequency."
  - "Gen-Z saving is influenced by convenience, trust, and social trends."
  - "Financially literate users leverage digital payment features for planning."
```
---

## Paper 25: Krichen & Mihoub_summarized.md

**Source File:** `Krichen & Mihoub_summarized.md`

```yaml
paper_id: "10.3390/ai6090215"
designation: "international"
title: "Long Short-Term Memory Networks: A Comprehensive Survey"
authors: "Krichen, M.; Mihoub, A."
year: 2025
venue: "AI"
odin_topics:
  - "6.A"
  - "6.B"
  - "8.A"
  - "8.B"
  - "5.C"
  - "12.B"
tldr: "A comprehensive survey of LSTM networks covering architectures, applications, variants, challenges, and recent advances in sequence modeling."
problem_and_motivation: "Traditional RNNs suffer from vanishing gradient, limiting long-range dependency capture. LSTM was introduced to overcome this, enabling effective sequence modeling. However, LSTMs face computational and data challenges that hinder practical deployment."
approach:
  - "Surveys LSTM fundamentals, including cell state, hidden state, and three gating mechanisms."
  - "Reviews applications across NLP, time series analysis, speech recognition, healthcare, robotics, and video analysis."
  - "Discusses architectural variants: Bidirectional LSTM, Stacked LSTM, and Attention Mechanisms."
  - "Identifies key challenges: computational complexity, data requirements, and training difficulties."
  - "Highlights recent advances like peephole connections, Grid LSTM, and layer normalization."
  - "Compares LSTM performance with traditional RNNs and Transformer models."
findings:
  - "LSTM mitigates vanishing gradient problem, enabling learning of long-term dependencies."
  - "LSTMs are widely used in NLP, time series forecasting, speech recognition, and other domains."
  - "Bidirectional LSTM processes sequences in both directions, improving context understanding."
  - "Stacked LSTM increases model capacity and achieves high accuracy in complex tasks."
  - "Attention mechanisms with LSTM enhance performance on long sequences by focusing on relevant input parts."
  - "num: Bidirectional LSTM achieved over 90% accuracy in speed predictions for up to 60 minutes."
  - "num: Stacked LSTM achieved over 99% accuracy in bearing fault diagnosis."
key_figures_tables:
  - "Figure 2: LSTM cell architecture showing cell state and gates → illustrates information flow."
  - "Table 1: Comparison of RNNs and LSTMs → highlights LSTM's long-term memory advantage."
  - "Table 2: Applications of LSTM networks across domains → demonstrates versatility."
key_equations:
  - equation: '$i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i)$'
    explanation: "Input gate controls new information addition."
  - equation: '$f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$'
    explanation: "Forget gate decides what to discard from cell state."
  - equation: '$o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o)$'
    explanation: "Output gate filters cell state for hidden state."
  - equation: '$C_t = f_t \otimes C_{t-1} + i_t \otimes \tilde{C}_t$'
    explanation: "Cell state update with forget and input gates."
  - equation: '$h_t = o_t \otimes \tanh(C_t)$'
    explanation: "Hidden state computed from output gate and cell state."
definitions:
  - term: "LSTM"
    definition: "Long Short-Term Memory, a type of RNN designed to capture long-term dependencies."
  - term: "RNN"
    definition: "Recurrent Neural Network, a neural network for sequential data."
  - term: "BiLSTM"
    definition: "Bidirectional LSTM, processes sequence in both forward and backward directions."
  - term: "Attention Mechanism"
    definition: "A technique that allows the model to focus on relevant parts of the input sequence."
critical_citations:
  - "[Hochreiter and Schmidhuber, 1997] — Introduced LSTM architecture."
  - "[Van Houdt et al., 2020] — Comprehensive review of LSTM."
  - "[Sherstinsky, 2020] — Fundamentals of RNN and LSTM."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "LSTM is a core predictive model for time series forecasting of spending."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Survey covers LSTM variants and attention mechanisms directly applicable to spending sequence forecasting."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "LSTM is used for anomaly detection in time series, as discussed in section 3.2."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "The paper reviews LSTM-based anomaly detection methods, informing algorithm selection."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "low"
      justification: "LSTM can be used for classification but paper does not focus on financial profiles specifically."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "low"
      justification: "Paper compares LSTM with other models, providing evaluation context but not a framework."
  contribution: "This survey justifies the use of LSTM for Odin's spending forecasting module due to its proven effectiveness in time series prediction. It informs the anomaly detection module by highlighting LSTM's capability to identify unusual patterns in sequential data. The discussion of BiLSTM and attention mechanisms suggests architectural enhancements for Odin's prediction accuracy. The identified challenges guide Odin's design to address computational and data constraints."
  directly_justifies:
    - "LSTM networks are effective for forecasting tasks with sequential spending data."
    - "Bidirectional LSTM can improve classification accuracy by leveraging future context."
    - "Attention mechanisms help model long spending histories by focusing on relevant past transactions."
    - "LSTM-based anomaly detection can identify unusual spending patterns indicative of fraud or errors."
  limits:
    - "None identified."
  mapping_rationale: "A systematic scan of all 12 functional domains and associated topic codes was performed. The Spending Forecasting domain (6.A, 6.B) and Anomaly Detection (8.A, 8.B) were flagged as high relevance because LSTM is directly applicable to these algorithmic modules. The Behavioral Profiling domain (5.C) was considered low because the paper does not specifically address financial behavioral profiles, though LSTM can be used for classification. The System Evaluation domain (12.B) was also low, as the paper provides comparisons but not a framework. Other domains such as Filipino cultural context, expense categorization, mobile design, data privacy, and engagement were rejected because the paper does not address them. Overall, the survey provides foundational knowledge for selecting LSTM-based approaches for Odin's predictive and anomaly detection modules."
limitations:
  - "Survey is narrative, not systematic, and may omit some recent studies."
  - "Does not address specific implementation challenges for mobile or resource-constrained devices. [unacknowledged]"
  - "Lacks empirical benchmarking on financial time series data. [unacknowledged]"
remember_this:
  - "LSTM effectively captures long-term dependencies in sequential data."
  - "Bidirectional LSTM improves accuracy by using both past and future context."
  - "Attention mechanisms boost LSTM performance on long sequences."
  - "num: Stacked LSTM achieved over 99% accuracy in bearing fault diagnosis."
  - "LSTM training is computationally intensive and requires large datasets."
```
---


---

## Agent Instruction

If the agent reading this document believes further context about a paper is needed, it may request the original converted markdown file (with the '_marked' suffix) from the user for the relevant paper(s).
