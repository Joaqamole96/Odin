```yaml
paper_id: "10.3390/informatics10010032"
designation: "local"
title: "Affective Design Analysis of Explainable Artificial Intelligence (XAI): A User-Centric Perspective"
authors: "Bernardo, E.; Seva, R."
year: 2023
venue: "Informatics"
odin_topics:
  - "10.B"
  - "11.A"
  - "11.B"
tldr: "End-user trust in AI is calibrated through both cognitive and affective routes, with XAI design attributes significantly influencing trust via these routes, moderated by user anxiety and incidental emotions."
problem_and_motivation: "Current XAI research focuses on developers, neglecting end-user perspectives, which limits trust and adoption. This study addresses the gap by investigating how end-users calibrate trust from XAI through affective design, aiming to fill the lack of end-user understanding."
approach:
  - "Conducted a pre-study survey with 312 AI users to identify important XAI design attributes (explanation form, communication style, supplementary information)."
  - "Designed a between-subject experiment with 202 participants using an image classification AI testbed with 64 design configurations (2 levels each of three design attributes, plus AI reliability, learning capability, brand, and time)."
  - "Measured emotions using XAI emotion set (XES), trust, perceived usefulness, and reliance, with moderators including AI anxiety, incidental emotions, trust disposition, and experience."
  - "Analyzed data using structural equation modeling (SEM) to test mediation, direct, and moderation effects on trust calibration."
findings:
  - "Affective route (emotions) mediates trust calibration alongside cognitive route; interestingly surprised and trusting emotions positively affect trust, while fearfully dismayed negatively affects it."
  - "Example-based explanations increase interestingly surprised and trusting emotions, while human-like communication reduces fearfully dismayed and anxiously suspicious emotions."
  - "Supplementary information reduces fearfully dismayed emotions; logic-robotic communication style increases fearfully dismayed and anxiously suspicious emotions."
  - "AI anxiety, incidental emotions, AI reliability, and user experience moderate the trust calibration process, with high anxiety and low reliability dampening positive effects."
  - "num: Perceived trust significantly predicts reliance (β=0.439, p<0.001), and affective mediation paths showed significant indirect effects (e.g., trusting emotion mediation: β=0.171, p=0.001)."
key_figures_tables:
  - "Table 1: Experimental design configurations with 6 variables → 64 design combinations tested."
  - "Table 8: Mediation effect analysis showing significant affective and cognitive paths → Affective mediation is confirmed."
  - "Table 9: Direct effects of design elements on emotions and perceived usefulness → Example-based explanation boosts positive emotions."
  - "Table 13: Summary of affect and cognitive change per design element → Clear mapping for design choices."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "XAI"
    definition: "Explainable Artificial Intelligence, techniques that provide human-level explanations of AI decisions."
  - term: "Affective design"
    definition: "Design approach that elicits emotions from users to trigger specific behavior."
  - term: "Trust calibration"
    definition: "Process of adjusting trust in a system based on experience and information."
critical_citations:
  - "[Lee & See, 2004] — Foundational framework for trust calibration routes."
  - "[Norman, 2004] — Three levels of processing for affective design."
  - "[Bernardo & Seva, 2022] — XAI emotion set used in this study."
relevance:
  topics:
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "high"
      justification: "Directly addresses trust calibration from XAI, which is critical for user trust in AI-driven PFMS."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "medium"
      justification: "Trust influences engagement; findings on trust calibration can inform engagement strategies."
    - code: "11.B"
      name: "Retention Mechanisms and Engagement Design"
      relevance: "medium"
      justification: "Trust is a key factor in retention; design attributes affecting trust can be leveraged for retention."
  contribution: "This paper provides a user-centric framework for trust calibration in XAI, demonstrating that both cognitive and affective routes are viable. It identifies specific design attributes (explanation form, communication style, supplementary information) that can be directly applied to Odin's explanation interfaces for budget recommendations. The moderation effects of user anxiety and incidental emotions suggest that Odin should adapt its explanations based on user state. These insights can guide Odin's UX design to foster trust, thereby improving user adoption and retention."
  directly_justifies:
    - "XAI should be designed to elicit positive emotions (e.g., interestingly surprised) to enhance trust."
    - "Example-based explanations increase trust and positive emotions, suitable for financial advice."
    - "Human-like communication style reduces negative emotions and increases perceived usefulness."
    - "User anxiety and incidental emotions moderate trust calibration; Odin should monitor user affect."
  limits:
    - "Study uses image recognition AI, not financial domain; generalizability to PFMS needs verification."
    - "Experiment is short-term (2 days); long-term trust dynamics not captured."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper's primary focus on user trust calibration from explainable AI directly maps to Topic 10.B (User Trust), assigned high relevance because it provides empirical evidence on how XAI design influences trust via affective and cognitive routes. Topics 11.A (Engagement) and 11.B (Retention) were flagged as medium relevance because trust is a foundational driver of engagement and retention in PFMS; the paper's insights on design attributes can inform engagement strategies. Other domains such as expense categorization, forecasting, anomaly detection, savings, and debt management were considered but rejected as the paper does not address these specific financial functions. The paper's findings on affective design and user moderators are contextually relevant to mobile-first design (9.A) but not explicitly; thus, 9.A was not selected. Overall, the paper offers strong guidance for building trust in AI-driven financial management systems."
limitations:
  - "The study uses image recognition AI, which differs from financial recommendation AI; domain-specific validity is untested. [unacknowledged]"
  - "The sample may not fully represent the Filipino young professional demographic targeted by Odin. [unacknowledged]"
  - "Long-term trust calibration and retention effects are not investigated, though authors acknowledge this limitation."
remember_this:
  - "Trust in XAI is calibrated via both cognitive and affective routes."
  - "Example-based explanations and human-like communication boost positive emotions and trust."
  - "User anxiety and incidental emotions moderate the effectiveness of XAI design."
  - "Affective design of explanations can directly influence user reliance on AI systems."
  - "Explanations should be tailored to user state for optimal trust calibration."
```