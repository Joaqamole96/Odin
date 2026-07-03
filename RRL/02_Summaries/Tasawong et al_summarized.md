```yaml
paper_id: 10.48550/arXiv.2602.01618
designation: international-algorithm-specific
title: SEA-Guard: Culturally Grounded Multilingual Safeguard for Southeast Asia
authors: Tasawong, P.; Ngui, J. G.; Aji, A. F.; Cohn, T.; Limkonchotiwat, P.
year: 2026
venue: Unknown
odin_topics:
  - 5.A
  - 5.C
  - 6.B
  - 8.B
  - 8.C
  - 9.A
  - 9.B
  - 10.A
tldr: SEA-Guard is a multilingual AI safety safeguard trained on a novel culturally-grounded dataset for 8 Southeast Asian languages, achieving state-of-the-art performance on cultural safety benchmarks.
problem_and_motivation: Existing AI safeguards are primarily designed for English and fail to capture cultural nuances or perform reliably in low-resource Southeast Asian languages. This gap poses safety risks when deployed in regions with diverse cultural values and norms, as harmful content may bypass moderation.
approach:
  - Proposed a multi-agent data synthesis framework to generate 870k culturally grounded safety samples per language across 53 SEA cultural categories.
  - Developed MCRE, an ensemble technique with multiple stochastic reasoning passes, for robust zero-shot labeling and quality assurance of generated data.
  - Trained three safeguard model variants (4B, 8B, 12B) using supervised fine-tuning on Qwen-SEA-LION and Gemma base models.
  - Evaluated models on three benchmarks: a SEA cultural safety benchmark, a generic multilingual safety benchmark, and zero-shot vision-text safety benchmarks.
  - Compared performance against existing safeguards including ShieldGemma, LlamaGuard, PolyGuard, Qwen3Guard, and commercial APIs.
findings:
  - num: SEA-Guard-12B achieved a 19.9-point AUPRC improvement over ShieldGemma on response classification (75.2 vs 55.2) and scored 80.0 on cultural prompt classification.
  - The model demonstrated strong cross-lingual robustness with performance gaps below one point across all 8 SEA languages for prompt classification.
  - SEA-Guard generalized effectively to generic safety benchmarks, with a 95.9 AUPRC on English prompt classification, despite not being trained on generic safety data.
  - Zero-shot performance on vision-text safety benchmarks improved the baseline in 6 out of 7 settings, indicating emergent cross-modal capabilities.
  - SEA-Guard maintained robust performance under adversarial white-space insertion attacks, with larger variants showing the most stable harmfulness scores.
key_figures_tables:
  - "Figure 3: Model alignment with human-severity judgments → SEA-Guard achieves higher Spearman/Pearson correlations and clearer separation across severity levels than baselines."
  - "Figure 4: Robustness to adversarial attack → SEA-Guard models maintain high harmfulness scores under white-space perturbations, unlike Qwen3Guard and LlamaGuard which degrade."
  - "Table 1: Performance on SEA-SafeguardBench → SEA-Guard-12B scores 80.0 AUPRC on prompt and 75.2 on response classification, outperforming all competitors."
  - "Table 2: Generic safety performance → SEA-Guard-12B reaches 95.9 AUPRC on English prompt classification, generalizing well without generic training data."
key_equations:
  - equation: "h(x) = \\sum_{c \\in C_{safety}} s_c \\cdot P(\\hat{y}_{final} = c | R, x)"
    explanation: "Computes a continuous harmfulness score from MCRE class probabilities."
definitions:
  - term: MCRE
    definition: "Monte Carlo Reasoning Ensemble; a zero-shot classification method using multiple stochastic reasoning passes to estimate robust class probabilities."
  - term: SEA
    definition: "Southeast Asia."
  - term: PFMS
    definition: "Personal Finance Management System."
  - term: SFT
    definition: "Supervised Fine-Tuning."
  - term: AUPRC
    definition: "Area Under the Precision-Recall Curve."
critical_citations:
  - "[Tasawong et al., 2025b] — Defines the SEA-SafeguardBench used for evaluation."
  - "[Zeng et al., 2024] — Introduces ShieldGemma, a primary baseline model."
  - "[Inan et al., 2023] — Introduces LlamaGuard, a primary baseline model."
  - "[Kumar et al., 2025] — Introduces PolyGuard, a multilingual safety tool."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: "Provides a multi-agent data synthesis framework applicable to profile generation."
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: "Directly proposes MCRE, a robust classification ensemble method, relevant for behavioral profiling."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: "The data synthesis and evaluation methodology for time-series patterns is relevant."
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: "The safeguard classification task is analogous to anomaly detection in user transactions."
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: high
      justification: "Addresses cold-start issues in low-resource contexts via synthetic data generation."
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: high
      justification: "Emphasizes multilingual and culturally-aware systems, foundational for mobile-first design."
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: "Provides a framework for designing user-friendly, culturally-sensitive mobile interfaces."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: "Moderation framework aligns with user trust and data privacy needs in financial systems."
  contribution: "The paper's data synthesis framework and MCRE technique offer a scalable method for generating culturally-grounded safety data. This can be directly adapted to create behavioral profile and anomaly detection datasets for Odin. The robust classification approach (MCRE) is applicable to user behavior classification and cold-start problem-solving. The evaluation methodology provides a blueprint for benchmarking PFMS modules."
  directly_justifies:
    - "The MCRE technique can be used for robust classification of financial behaviors in Odin."
    - "The multi-agent data synthesis framework can generate synthetic user spending data for Odin."
    - "Cross-lingual robustness techniques are essential for a PFMS serving Filipino young professionals."
  limits:
    - "The paper focuses on safety moderation, not financial behavior prediction, requiring translation of methods."
    - "The models are trained on text data, not financial transaction data, so direct application is limited."
    - "Performance on specific PFMS tasks (like anomaly detection) needs further validation."
  mapping_rationale: "A systematic scan across all 12 domains and associated topic codes was performed. The paper's focus on multilingual AI safety and cultural grounding directly informs behavioral profiling (5.A, 5.C), forecasting (6.B), and anomaly detection (8.B, 8.C). The data synthesis and classification methodology are relevant to mobile-first design (9.A, 9.B) and data privacy/trust (10.A). Domains like Expense Categorization (3.A, etc.) and Savings/Debt Management (13.A, etc.) were rejected as they are not directly addressed. Borderline cases like cultural practices (2.A, etc.) were considered but not selected, as the paper's cultural grounding is on safety, not financial practices. Overall, the paper provides high-value methodological contributions for building robust, culturally-aware classifiers for a PFMS like Odin."
limitations:
  - "The study did not cover over 700 SEA dialects and languages, limiting generalizability."
  - "The paper did not experiment with 0.5B models due to performance reliability concerns."
  - "Safety evaluation benchmarks for SEA languages are still needed."
  - "The potential for generated datasets to be misused for harmful content generation is acknowledged. [unacknowledged]"
remember_this:
  - "Multilingual safeguards perform poorly without culturally-grounded training data."
  - "MCRE improves classification robustness by aggregating multiple stochastic reasoning passes."
  - "SEA-Guard generalizes to unseen vision-text tasks despite text-only training."
  - "A 19.9-point AUPRC gap was observed between SEA-Guard and ShieldGemma on response classification."
  - "Data deduplication and scale (870k samples per language) are critical for robust performance."
```