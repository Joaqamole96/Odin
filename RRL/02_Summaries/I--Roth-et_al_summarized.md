```yaml
paper_id: 10.1080/17489725.2023.2251423
designation: international
title: Making maps & visualizations for mobile devices: A research agenda for mobile-first and responsive cartographic design
authors: Roth, R. E.; Çöltekin, A.; Delazari, L.; Denney, B.; Mendonça, A.; Ricker, B. A.; Shen, J.; Stachoň, Z.; Wu, M.
year: 2024
venue: Journal of Location Based Services
odin_topics:
  - 9.A
  - 9.B
  - 4.A
  - 10.A
  - 11.A
  - 12.A
  - 12.B
tldr: Mobile-first and responsive cartographic design requires a fundamental rethinking of scale, projection, symbolization, toponymy, and interaction to address mobile constraints and enablements.
problem_and_motivation: The majority of maps are now viewed on mobile devices, yet the cartographic canon remains rooted in print design. This gap necessitates a comprehensive research agenda to adapt design practices for mobile contexts.
approach:
  - The research agenda was derived from a two-day workshop with 70 scholars from nine countries.
  - The paper establishes a partial design space for mobile-first and responsive maps.
  - The design space is organized into five dimensions of design decisions.
  - The paper reviews and synthesizes existing literature on mobile cartographic design.
  - The paper identifies and presents 20 specific research challenges.
findings:
  - num: More maps are viewed on mobile devices than any other format.
  - Generalization may be speed- or cost-dependent rather than solely scale-dependent.
  - Egocentric designs and oblique projections are highly relevant for mobile use.
  - Energy-aware color schemes can significantly reduce carbon footprint.
  - Cross-cultural and inclusive icon and label design is essential for mobile maps.
key_figures_tables:
  - Table 1: 20 research challenges for mobile-first and responsive cartographic design.
  - Table 2: Summary of evolving design guidelines for mobile-first and responsive cartography.
  - Figure 2: Mobile-first and responsive design illustrated with an SDG indicator map.
  - Figure 8: Energy-aware color schemes for mobile maps.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Mobile first"
    definition: "A design philosophy that prioritizes the most constrained mobile user experience."
  - term: "Responsive design"
    definition: "A strategy that adapts content and layout from mobile to non-mobile use cases."
  - term: "Visual hierarchy"
    definition: "The order that map symbols and elements are perceived visually."
  - term: "Focus+context"
    definition: "Visualization techniques that provide both a general overview and local detail."
  - term: "Glanceable visualization"
    definition: "A visualization designed to be understood within a few seconds."
critical_citations:
  - "[Bertin, 1967/1983] — Foundational theory of visual variables."
  - "[MacEachren, 1995] — Extended visual variable theory for maps."
  - "[Kraak et al., 2020] — Provided a framework for mapping for a sustainable world."
relevance:
  topics:
    - code: 9.A
      name: Mobile‑First Design Principles and Rationale
      relevance: high
      justification: "The paper's central thesis is a research agenda for mobile-first cartographic design."
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: high
      justification: "Directly addresses UI/UX design considerations for mobile maps and visualizations."
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: "Provides a benchmark study of existing mobile map UX and interaction strategies."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: "Discusses privacy and surveillance implications of location-based services."
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: "Addresses user interaction strategies and visual storytelling for engagement."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: "Proposes empirical research and design case studies to inform mobile map design."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: low
      justification: "Primarily focuses on design rather than algorithmic evaluation."
  contribution: "This paper provides a foundational framework for evaluating and designing mobile-first interfaces for Odin. It directly justifies prioritizing constrained mobile experiences in the app's UX strategy. The research challenges on scale, generalization, and user interaction offer a systematic basis for developing Odin's map-based spending visualizations. The agenda's emphasis on energy-aware and inclusive design aligns with Odin's goals for sustainable and equitable financial tools."
  directly_justifies:
    - "Mobile-first design should be the anchor point for Odin's responsive interface strategy."
    - "Odin's default map scale and level of detail should consider the user's mode of travel."
    - "Interaction strategies for Odin must be optimized for thumb-based, touchscreen use."
    - "Data privacy concerns necessitate explicit user trust mechanisms in Odin."
  limits:
    - "The research agenda is broad and conceptual, lacking specific implementation details."
    - "Most empirical studies cited are not specific to personal finance management."
    - "The paper does not provide quantitative performance benchmarks for mobile maps."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The domain 'Mobile‑First Design' (9.A, 9.B) was flagged as highly relevant because the paper is a dedicated research agenda for this very topic. The domain 'Existing Systems & Gaps' (4.A) was flagged as medium relevance due to the paper's benchmarking of existing mobile map UX. The domain 'Data Privacy & User Trust' (10.A) and 'User Retention & Engagement' (11.A) were considered medium relevance, as the paper discusses the consequences of mobile technology on privacy and user engagement strategies. The domain 'System Evaluation' (12.A, 12.B) was noted as medium relevance because the paper proposes empirical research and design case studies as evaluation methods. Borderline cases included the paper's discussion of seasonal spending (touching 2.B) which was rejected as it is not a core focus, and its mention of user constraints (3.C) which was rejected for being too general. The paper's overall relevance to Odin is high, providing a comprehensive theoretical and methodological foundation for its mobile-first and responsive design strategy."
limitations:
  - "The agenda is based on a workshop from 2019, and some technological references may be dated. [unacknowledged]"
  - "The paper does not provide a concrete implementation roadmap for the proposed research challenges."
remember_this:
  - "Mobile-first design prioritizes constrained user experiences for inclusivity."
  - "Generalization on mobile maps can be speed- or cost-dependent."
  - "Energy-aware design is crucial for both battery life and carbon footprint."
  - "Cross-cultural and inclusive iconography is essential for mobile maps."
  - "num: 91% of mobile maps sampled used light basemaps, missing energy-saving opportunities."
```