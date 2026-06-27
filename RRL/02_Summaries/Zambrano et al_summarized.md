```yaml
paper_id: 10.1016/j.wds.2023.100081
designation: international
title: Rotating savings and credit associations: A scoping review
authors: Zambrano, A.F.; Giraldo, L.F.; Perdomo, M.T.; Hernández, I.D.; Godoy, J.M.
year: 2023
venue: World Development Sustainability
odin_topics:
  - 2.A
  - 13.A
  - 13.B
  - 5.A
  - 4.A
  - 4.B
  - 7.A
tldr: A scoping review of ROSCA research finds these informal savings groups provide financial access and social capital, and suggests design improvements like diversification and reputation systems.
problem_and_motivation: Informal financial cooperation, like ROSCAs, is vital for low-income communities, but a systematic synthesis of recent findings on their structure, benefits, and risks has been lacking to inform design and policy.
approach:
  - Conducted a scoping review using the PRISMA-ScR protocol on 96 peer-reviewed articles from 2000-2022.
  - Extracted data on study location, methodological approaches, and keywords for trend analysis.
  - Grouped findings into categories including origin, participants, benefits, risks, operation, and penalties.
  - Analyzed the co-occurrence of keywords to identify thematic connections within the literature.
  - Reviewed mathematical, computational, and technological applications for modeling and supporting ROSCAs.
findings:
  - Asia and Africa are the most studied continents for ROSCAs, with limited research in South America.
  - ROSCAs provide non-financial benefits like social capital, empowerment, and improved health for members.
  - Defection of members, driven by loss of motivation, is a primary risk factor for ROSCA failure.
  - Strategies like diversification (joining multiple ROSCAs) and smaller groups can increase resilience.
  - num: Multi-agent simulations and web applications are emerging to test improvements and support ROSCA operations.
key_figures_tables:
  - Figure 1: Continent of data collection → Asia and Africa are the most studied regions.
  - Figure 2: Country of data collection → Kenya, India, and Japan are frequently studied.
  - Figure 3: Published year and continent → An increasing trend in publications until 2019, with a recent decline.
  - Figure 4: Methodological approaches → Interviews and surveys are the most common methods.
  - Figure 6: Number of occurrences of most common keywords → ROSCA, Finance, and Social are the most frequent concepts.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: ROSCA
    definition: Rotating Savings and Credit Association, an informal group where members contribute periodically to a pot allocated to one member each cycle.
  - term: Bidding ROSCA
    definition: A type where the pot is allocated to members who bid the highest premium for early turns.
  - term: Fixed ROSCA
    definition: A type where the order of receiving the pot remains fixed across cycles.
  - term: Random ROSCA
    definition: A type where the order of receiving the pot is randomly determined each cycle.
critical_citations:
  - "[Anderson et al., 2009] — ROSCAs are unsustainable without external sanctions."
  - "[Besley et al., 1993] — Foundational economics of ROSCAs."
  - "[Geertz, 1962] — Early influential description of ROSCAs as development tools."
  - "[Levenson & Besley, 1996] — Key analysis of ROSCA participation determinants."
  - "[Sedai et al., 2021] — Links ROSCAs to women's empowerment in India."
relevance:
  topics:
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: ROSCAs are a quintessential example of culturally embedded financial practices studied globally.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: Directly analyzes ROSCAs as a mechanism for collective savings and achieving financial goals.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: Examines ROSCAs as an alternative to formal debt for financing needs.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Discusses member motivations like self-control and trust, which relate to behavioral profiles.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Maps the landscape of informal finance (ROSCAs) as an alternative to formal systems.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies gaps in formal finance that ROSCAs fill, and limitations of ROSCAs themselves.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: Provides background on savings strategies but does not detail algorithmic budgeting.
  contribution: This paper provides a comprehensive review of ROSCAs, offering validated domain knowledge for Odin's design. Its findings on savings discipline, social capital, and default risks directly inform the design of Odin's savings and social features. The review's emphasis on community trust and cultural specificity justifies Odin's focus on Filipino cultural practices. The identified strategies for increasing ROSCA resilience, such as diversification and reputation systems, can be adapted for Odin's recommendation and anomaly detection modules.
  directly_justifies:
    - "ROSCAs help members save money by imposing discipline and social pressure."
    - "Participation in ROSCAs provides non-financial benefits like social capital and empowerment."
    - "Defection and loss of motivation are primary risks that can be mitigated by reputation and economic penalties."
    - "Diversifying participation across multiple small groups reduces risk for members."
    - "Technological tools can improve transparency and security in informal savings groups."
  limits:
    - "Scoping review, not a meta-analysis; does not quantify effect sizes of strategies."
    - "The review excludes non-English literature, potentially missing regional insights."
    - "Focuses on ROSCAs, which are distinct from typical PFMS, limiting direct applicability."
    - "Proposed computational models are theoretical and not validated with real user data."
    - "Does not address the specific financial landscape or user behaviors of Filipino young professionals."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to domains of Culturally Specific Financial Practices (2.A) and Savings & Debt Management (13.A, 13.B) as it directly analyzes ROSCAs as informal financial tools used in various cultures. Medium relevance was assigned to Behavioral Profiling (5.A) and Existing Systems & Gaps (4.A, 4.B) due to its discussion of participant motivations, limitations of formal finance, and the role of social capital. Contextual relevance was noted for Budget Recommendation (7.A) as it provides domain knowledge but not algorithmic approaches. Other domains like Anomaly Detection (8.A, 8.B, 8.C) and Mobile-First Design (9.A, 9.B) were considered and rejected because the paper does not touch on these topics. Overall, the paper offers valuable background on informal savings behavior and community-based financial management, which can inform Odin's design by highlighting the importance of social features, trust, and culturally relevant savings mechanisms.
limitations:
  - "Limited to studies published in English."
  - "Data collection from real-world ROSCAs was restricted due to pandemic conditions after 2020."
  - "The review does not include a meta-analysis to quantify the effectiveness of strategies like diversification."
  - "Computational models and technological applications discussed are mostly theoretical and not tested at scale."
  - "Findings are synthesized from a broad global context, which may not be directly generalizable to the Philippines."
remember_this:
  - "ROSCAs provide both financial access and social capital to underprivileged communities."
  - "Discipline and social pressure are key mechanisms for successful savings in ROSCAs."
  - "Defection is a major risk, but diversification across groups can increase resilience."
  - "Non-financial benefits like empowerment and health are significant for members."
  - "num: 96 articles reviewed from 2000 to 2022 to synthesize ROSCA knowledge."
```