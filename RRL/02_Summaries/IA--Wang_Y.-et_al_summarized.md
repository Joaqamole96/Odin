```yaml
paper_id: 10.XXXX/XXXXXXX
designation: international
title: Conv-FinRe: A Conversational and Longitudinal Benchmark for Utility-Grounded Financial Recommendation
authors: Wang, Y.; Han, Y.; Qian, L.; He, Y.; Peng, X.; Feng, D.; Xie, Z.; Zhang, V. J.; Guo, R.; Mo, F.; Huang, J.; Chen, Y.; Liu, X.; Nie, J.
year: 2018
venue: Unknown
odin_topics:
  - 5.A
  - 6.A
  - 9.A
  - 9.B
  - 10.B
  - 11.A
  - 12.A
  - 12.B
  - 12.C
tldr: A conversational and longitudinal benchmark evaluates LLMs for stock recommendation using multi-view reference rankings grounded in investor-specific utility rather than mere behavioral imitation.
problem_and_motivation: Existing recommendation benchmarks equate user actions with optimal decisions, which is problematic in finance where behavior is noisy and short-sighted. There is a need for evaluation that distinguishes rational decision quality from simple behavioral alignment.
approach:
  - Constructs a stock universe of ten S&P 500 stocks with balanced sector and beta exposure.
  - Collects static user profiles via questionnaire and longitudinal decision trajectories via a custom simulation.
  - Generates structured multi-turn advisory conversations from user profiles and behavioral traces.
  - Evaluates LLM-generated rankings against four reference views: User Choice, Rational Utility, Market Momentum, and Risk Sensitivity.
  - Uses inverse optimization to infer latent user risk preferences (volatility and downside risk sensitivity) from observed choices.
findings:
  - num: High utility-based NDCG scores (0.92-0.97) across models indicate strong baseline ranking according to rational utility.
  - num: Llama3-XuanYuan3-70B-Chat achieved the highest MRR (0.65) and HR@3 (0.69), indicating better behavioral mimicry.
  - A persistent tension exists between rational decision quality and behavioral alignment.
  - Models that perform well on utility-based ranking often fail to match user choices, while behaviorally aligned models may overfit noise.
  - Alignment with Rational Utility and Market Momentum is strongly coupled, suggesting models struggle to decouple these signals.
  - Conversation history provides heterogeneous utility gains, with some models showing clear improvement and others degrading due to over-sensitivity to user noise.
key_figures_tables:
  - Table 2: Summary of ten-stock universe grouped by volatility tier → Ensures balanced exposure to systematic risk.
  - Table 3: Structural statistics of benchmark (10 users, 230 instances, 4,320 avg tokens) → Highlights substantial longitudinal context complexity.
  - Table 4: Overall performance of LLMs on uNDCG, MRR, HR@1, HR@3 → Demonstrates trade-off between utility alignment and behavioral mimicry.
  - Table 5: Alignment of models with Utility, Momentum, and Risk expert views → Reveals coupling between utility and momentum alignment.
  - Figure 2: Step-wise improvement in utility-based alignment from conversational history → Shows heterogeneous preference discovery dynamics.
  - Figure 3: Average utility alignment with and without conversational history → Identifies three archetypes: adaptive advisors, transaction-driven analysts, and behavioral overfitters.
key_equations:
  - equation: U_i,t(s) = \\tilde{\\mu}_{s,t} - \\lambda_i \\tilde{\\sigma}_{s,t}^2 - \\gamma_i \\text{Drawdown}_{s,t}
    explanation: Utility function balancing return, volatility, and downside risk.
  - equation: P(s^*|\\lambda_i,\\gamma_i,M_t) = \\frac{\\exp(U_{i,t}(s^*))}{\\sum_{s \\in S_t} \\exp(U_{i,t}(s))}
    explanation: Multinomial logit model for stock selection probability.
  - equation: L_i(\\lambda_i,\\gamma_i) = -\\sum_{t=1}^T \\log P(s^*_{i,t}|\\lambda_i,\\gamma_i,M_t) + \\alpha\\|(\\lambda_i,\\gamma_i)\\|_2^2
    explanation: Regularized negative log-likelihood for inverse preference optimization.
definitions:
  - term: uNDCG
    definition: Utility-based normalized discounted cumulative gain using calibrated utility as relevance.
  - term: MRR
    definition: Mean reciprocal rank of the user's chosen stock in the model's ranking.
  - term: HR@K
    definition: Hit rate at top-K, indicating if the user's choice appears in the top K recommendations.
  - term: EAS
    definition: Expert alignment score using Kendall's tau to measure agreement with reference views.
critical_citations:
  - "[Bertsimas et al., 2012] — Foundational for inverse optimization in finance."
  - "[Bertsimas et al., 2015] — Data-driven estimation via inverse optimization."
  - "[Magdon-Ismail & Atiya, 2004] — Defines maximum drawdown as a risk metric."
  - "[Rubinstein, 2002] — Reviews Markowitz's portfolio selection framework."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Paper explicitly models latent user risk preferences as a behavioral profile.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Evaluates LLMs on sequential stock recommendation, a predictive task.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: contextual
      justification: Conversational setting implies mobile-first interaction, but not explicitly addressed.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: contextual
      justification: Simulated conversational UX is relevant but not the core focus.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Alignment with user psychology is linked to trust, though not directly measured.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Longitudinal setting and conversational history examine user engagement over time.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Proposes a novel multi-view evaluation framework for financial recommendation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Empirically evaluates state-of-the-art LLMs as algorithmic modules.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Shares methodological concerns for evaluating personalized financial recommendations.
  contribution: This paper's framework for evaluating LLMs against multi-view references can be adapted to assess Odin's budget and forecasting modules. The use of inverse optimization to infer latent user preferences provides a methodology for grounding Odin's behavioral profiling. The distinction between rational utility and behavioral alignment directly justifies Odin's need for a utility-grounded evaluation strategy. The analysis of how models integrate conversational history over time informs Odin's design for handling longitudinal user data and improving personalization.
  directly_justifies:
    - "Financial recommendation evaluation should ground assessment in investor-specific utility rather than only behavioral imitation."
    - "Models that excel at rational ranking often fail to match observed user choices, revealing a fundamental trade-off."
    - "Conversational history provides non-uniform gains in utility alignment, with some models overfitting to noisy user actions."
    - "Aligning with Rational Utility and Market Momentum are coupled, indicating a need to decouple return-driven and risk-aware signals."
  limits:
    - "Small sample size of 10 users limits generalizability of behavioral findings."
    - "Conversational simulation, while validated, may not fully capture the complexity of real-world free-form dialogue."
    - "Stock universe is limited to 10 S&P 500 stocks, restricting the benchmark's scope."
    - "Longitudinal horizon is only 30 days, which may not reflect long-term investment dynamics."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was conducted. The paper was flagged as highly relevant to Behavioral Profiling (5.A) because it explicitly models and evaluates models against inferred latent user risk preferences, a core component of Odin's profiling. It is also highly relevant to Predictive Modeling (6.A) as the core task is sequential recommendation of financial assets. The paper's primary contribution is a novel multi-view evaluation framework, making it highly relevant to System Evaluation (12.A, 12.B). Medium relevance was assigned to User Trust (10.B) and Engagement (11.A) due to the conversational, longitudinal interaction setting which informs trust and engagement design. Contextual relevance was assigned to Mobile-First Design (9.A, 9.B) as the conversational environment is inherently mobile-suitable, but this is not a focus. Topics related to Expense Categorization (3.A, 3.B, 3.C) and Budget Recommendation (7.A, 7.B, 7.C, 7.D) were considered and rejected as the paper focuses on stock investment, not expense management or budgeting. Similarly, Anomaly Detection (8.A, 8.B, 8.C) and Savings & Debt Management (13.A, 13.B, 13.C) are not addressed. Overall, the paper provides a foundational evaluation methodology and behavioral modeling approach that is highly relevant to Odin's design and justification, particularly for its profiling, forecasting, and evaluation modules.
limitations:
  - "Small sample size of 10 users, limiting generalizability. [unacknowledged]"
  - "Simulated conversations may lack the full realism of free-form human dialogue. [unacknowledged]"
  - "Limited to a 30-day horizon for longitudinal study, potentially missing long-term patterns. [unacknowledged]"
  - "Stock universe of only 10 assets, restricting the recommendation task's complexity. [unacknowledged]"
remember_this:
  - "Utility-grounding in evaluation distinguishes rational advice from behavior mimicry."
  - "High utility alignment often couples with high market momentum alignment."
  - "Conversational history improves utility alignment for some but degrades it for others."
  - "Domain-specific models can exhibit stronger behavioral mimicry than general-purpose ones."
  - "Inverse optimization effectively infers latent risk preferences from user choices."
```