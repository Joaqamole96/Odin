```yaml
paper_id: 10.3390/electronics14112252
designation: international
title: Cybersecurity Analytics for the Enterprise Environment: A Systematic Literature Review
authors: Le, T.D.; Le-Dinh, T.; Uwizeyemungu, S.
year: 2025
venue: Electronics
odin_topics:
  - 4.A
  - 4.B
  - 9.A
  - 12.A
  - 12.C
tldr: A systematic review of 65 studies reveals a shift from traditional security tools to AI-powered analytics, with adoption concentrated in large enterprises and a significant research gap for SMEs.
problem_and_motivation: The escalating sophistication of cyber threats renders traditional signature-based defenses inadequate for modern enterprises. However, a lack of consolidated knowledge on the efficacy and evolution of advanced cybersecurity analytics impedes informed strategic adoption and research prioritization.
approach:
  - The study is a systematic literature review (SLR) following the PRISMA protocol, not a primary algorithmic study.
  - It screened 1491 records from six databases (IEEE Xplore, Scopus, Web of Science, ScienceDirect, ACM, Proquest) for peer-reviewed studies from 2013-2023.
  - A tripartite keyword grouping was used for security analytics, implementation methods, and enterprise context.
  - 60 studies were identified through database searches, and an additional 5 via snowballing, resulting in a final set of 65 studies.
  - The team performed a full-text assessment for relevance, clarity, and detail to synthesize ten thematic observations.
findings:
  - num: 65 peer-reviewed studies on enterprise cybersecurity analytics were analyzed, with a peak in publications in 2015, 2016, and 2020.
  - A significant transition is occurring from traditional signature-based tools to cloud-enabled, big-data, and AI-powered techniques.
  - Machine learning and graph-based models are increasingly prominent analytical approaches in recent works.
  - Large organizations in finance, ICT, and critical utilities spearhead adoption; however, dedicated research for SMEs is notably limited.
  - A clear strategic evolution is observed from reactive measures towards proactive and predictive security postures.
  - Ten thematic observations were synthesized, encapsulating drivers, technological shifts, and persistent challenges.
  - Significant barriers include data integration issues, skills shortages, financial costs, and the complexity of modern IT environments.
  - The review identifies critical open research avenues, including real-time scalable analytics, unified policy languages, and SME-oriented solutions.
key_figures_tables:
  - "Figure 1: Relationship between research questions and cybersecurity analytics tasks → Maps RQs to input, processing, and output stages."
  - "Figure 2: PRISMA-2020 flow diagram of the study selection process → Documents the rigorous identification, screening, and inclusion process."
  - "Figure 3: Annual distribution of 65 primary studies (2013-2023) → Shows a trend of initial growth followed by a recent decrease, suggesting a shift to more complex studies."
  - "Figure 4: Distribution of primary technologies cited in the literature → Highlights the foundational role of ML (22 studies), Big Data (16), and Cloud Computing (11)."
  - "Table 3: Security adoption of analytics across industries and enterprise size → Reveals concentrated adoption in large enterprises and critical sectors like finance and ICT."
  - "Table 4: Selected studies on security analytics in the enterprise context → Provides a detailed breakdown of frameworks, techniques, and evaluation strategies."
  - "Table 5: Enterprise security analytic evaluation methods → Categorizes how the effectiveness of security solutions is assessed, often via experiments/simulations."
  - "Table 6: Common sources and types of data for security analytics → Lists critical data sources like system logs, network traffic, and user activity data."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: APT
    definition: Advanced Persistent Threat
  - term: ML
    definition: Machine Learning
  - term: DL
    definition: Deep Learning
  - term: SIEM
    definition: Security Information and Event Management
  - term: SME
    definition: Small and Medium-sized Enterprise
  - term: PRISMA
    definition: Preferred Reporting Items for Systematic Reviews and Meta-Analyses
critical_citations:
  - "[Page et al., 2020] — PRISMA 2020 guideline for systematic reviews."
  - "[Xiong et al., 2021] — MITRE ATT&CK framework for threat modeling."
  - "[González-Granadillo et al., 2021] — Analysis of SIEM tools usage and trends."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides a systematic review framework analogous to evaluating PFMS tools.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies significant gaps in existing enterprise security analytics that parallel PFMS gaps.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: Mentions mobile platform research but does not focus on mobile-first design or UX.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: The paper critically evaluates research methodologies and identifies a lack of standardized evaluation metrics.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Discusses evaluation of algorithmic modules and the need for objective comparisons, relevant to evaluating budget recommenders.
  contribution: This paper provides a robust meta-analysis framework (PRISMA) that can be directly applied to systematically evaluate the landscape of PFMS for Filipino YPs. Its identified barriers to adoption, such as data integration issues, skills shortages, and financial constraints, are directly analogous to the challenges Odin faces in developing a cost-effective and accessible system for its target demographic. The review's emphasis on the need for standardized evaluation metrics and real-world validation serves as a critical guide for designing and assessing Odin's algorithmic modules, ensuring they are not just theoretically sound but practically effective.
  directly_justifies:
    - "A systematic literature review is essential for consolidating knowledge on PFMS design and implementation."
    - "Evaluating existing PFMS requires a structured framework to identify gaps and best practices."
    - "Adoption of new financial technologies is often hindered by financial and technical skill constraints."
    - "There is a significant research gap in addressing the unique needs of SMEs, similar to the underserved Filipino YP demographic."
    - "The lack of standardized evaluation metrics complicates the comparison of different algorithmic approaches."
  limits:
    - "The review focuses on enterprise cybersecurity, not personal financial management systems."
    - "The study was conducted in a general international context, with no specific focus on the Philippines."
    - "Only studies published in English and up to December 2023 were included, potentially missing more recent, region-specific research."
    - "The review did not perform a formal critical appraisal of the methodological soundness of the included primary studies."
  mapping_rationale: A systematic scan of all 12 functional domains against the paper's content reveals that its primary relevance is indirect but structurally valuable. The domain "Existing Systems & Gaps" (topics 4.A, 4.B) is highly relevant as the paper's methodology and findings on barriers directly mirror challenges in PFMS adoption and evaluation. The "System Evaluation" domain (topics 12.A, 12.C) is highly relevant due to the paper's detailed discussion of research methodologies, evaluation frameworks, and the crucial need for standardized benchmarks and real-world validation. The "Mobile-First Design" domain was considered but rejected due to the paper's limited focus on mobile-specific research. The "Data Privacy" domain was considered but was not a central theme, making its relevance contextual at best. This paper is not about PFMS, but its comprehensive review methodology and its identification of universal challenges in technology adoption provide a powerful blueprint for assessing the state of PFMS for Odin, justifying its selection as a critical methodological reference.
limitations:
  - "The temporal scope (2013-2023) may exclude foundational earlier work and recent developments from 2024-2025."
  - "The focus on peer-reviewed English publications may introduce a language and publication bias."
  - "Potential for publication bias, as studies with positive results are more likely to be published."
  - "Variation in the extent of real-world validation and methodological rigor among the 65 primary studies."
  - "Lack of standardized evaluation metrics in the reviewed field hinders direct comparison of results. [unacknowledged]"
remember_this:
  - "Machine learning and graph-based models are the dominant analytical approaches."
  - "The shift is from reactive security to proactive and predictive strategies."
  - "A significant research gap exists for SMEs in cybersecurity analytics."
  - "Data integration, skills shortages, and cost are the main barriers to implementation."
  - "num: 65 peer-reviewed studies were synthesized in this systematic review."

```