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