```yaml
paper_id: 10.1109/ACCESS.2023.3275134
designation: international-algorithm-specific
title: Deep Generative Models for Synthetic Data: A Survey
authors: Eigenschink, P.; Reutterer, T.; Vamosi, S.; Vamosi, R.; Sun, C.; Kalcher, K.
year: 2023
venue: IEEE Access
odin_topics:
  - 12.A
  - 12.B
  - 12.C
tldr: A survey proposing a data-driven evaluation framework for deep generative models for synthetic sequential data using five criteria: representativeness, novelty, realism, diversity, and coherence.
problem_and_motivation: Evaluating deep generative models for sequential data is challenging due to data heterogeneity and conflicting requirements across domains. Existing metrics are often domain- or model-specific, making cross-domain comparison difficult. A common, abstract evaluation framework is needed to guide research and enable knowledge transfer between fields.
approach:
  - The paper proposes a domain- and model-agnostic evaluation framework based on five high-level criteria relative to the original data: representativeness, novelty, realism, diversity, and coherence.
  - It critically reviews applications of deep generative models across NLP, speech/audio, video, healthcare, and mobility domains.
  - The review analyzes models based on their architectures (GANs, VAEs, RNNs/LSTMs, CNNs) and the metrics used for evaluation.
  - The paper evaluates each domain against the proposed criteria, identifying which criteria are prioritized and how they are measured.
  - It summarizes the prevalence of different architectural elements across domains and provides overview tables of representative contributions and evaluation metrics.
findings:
  - num: Realism and coherence are more important for synthetic data in natural language, speech, and audio processing tasks.
  - num: Novelty and representativeness are more important for healthcare and mobility data.
  - Representativeness is often measured with statistical metrics like MMD or NLL, while realism is frequently assessed by human judgement.
  - Novelty is often evaluated using privacy tests, particularly in sensitive domains like healthcare.
  - GANs are the most frequently used architecture, often in combination with CNNs or RNNs to ensure coherent generation of sequential data.
key_figures_tables:
  - Figure 1: Data heterogeneity in sequential data by cardinality and dimensionality → Shows why a common framework is needed.
  - Figure 2: High-level structure of the article → Outlines the survey's organization and objectives.
  - Figure 3: Illustration of synthetic data scoring high/low on the five criteria → Clarifies the meaning of each evaluation criterion.
  - Figure 4: Prevalence of architectural elements in five domains → Highlights the popularity of GANs, CNNs, and RNNs.
  - Table 6: Overview of domains and metrics for the five criteria → Summarizes domain-specific priorities and measurement approaches.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Representativeness
    definition: The ability of a model to capture population-level properties of the original data.
  - term: Novelty
    definition: The degree to which synthetic data-points are entirely new and not closely resembling any original data-point.
  - term: Realism
    definition: The indistinguishability of an individual synthetic data-point from an original one.
  - term: Diversity
    definition: The uniqueness of data-points within the synthetic dataset.
  - term: Coherence
    definition: The internal consistency and logical structure of a single synthetic data-point.
  - term: GAN
    definition: Generative Adversarial Network.
  - term: VAE
    definition: Variational Autoencoder.
  - term: RNN
    definition: Recurrent Neural Network.
  - term: LSTM
    definition: Long Short-Term Memory network.
  - term: CNN
    definition: Convolutional Neural Network.
  - term: NLL
    definition: Negative Log-Likelihood.
  - term: MMD
    definition: Maximum Mean Discrepancy.
  - term: IS
    definition: Inception Score.
  - term: BLEU
    definition: Bilingual Evaluation Understudy.
  - term: EHR
    definition: Electronic Health Record.
  - term: TSTR
    definition: Train on Synthetic, Test on Real.
  - term: TRTS
    definition: Train on Real, Test on Synthetic.
critical_citations:
  - "[Borji, 2019] — Reviews pros and cons of GAN evaluation measures."
  - "[Theis et al., 2016] — Discusses limitations of general-purpose metrics like NLL."
  - "[Goodfellow et al., 2016] — Foundational reference for deep learning architectures."
relevance:
  topics:
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Proposes a general framework for evaluating generative models, directly applicable to assessing Odin's recommendation modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides a structured approach and criteria (representativeness, novelty, realism, diversity, coherence) for evaluating algorithmic modules in Odin.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: The framework's criteria can be adapted to evaluate the quality of budget recommendations (e.g., realism, diversity of plans).
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: The concept of generating synthetic user data could be used for profile testing, but the paper doesn't directly address behavioral profiling.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: contextual
      justification: The review covers models for sequential data, which is relevant to forecasting, but focuses on generation rather than prediction.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: contextual
      justification: The discussion of privacy and synthetic data in healthcare could be analogous to handling sensitive financial data for savings goals.
  contribution: |
    This paper provides Odin with a formal, high-level evaluation framework for any algorithmic module that generates or recommends data, such as budget plans, spending forecasts, or savings allocations. The criteria of representativeness and realism can be used to assess how well a recommended budget reflects a user's actual historical spending patterns. The criteria of novelty and coherence are essential for ensuring that generated recommendations are not just copies of past behavior but are internally consistent and provide new, actionable insights.
  directly_justifies:
    - "The proposed framework enables systematic comparison of different generative models for sequential data, such as those used for spending forecasting."
    - "Evaluation of representativeness and realism in synthetic data corresponds to validating the accuracy and plausibility of generated spending forecasts or budget plans."
    - "Assessing novelty and coherence in synthetic data is analogous to evaluating the actionability and internal logic of new budget recommendations."
  limits:
    - The framework is conceptual and does not provide specific implementation guidelines or benchmarks for Odin's modules.
    - The survey focuses on generative models for creating synthetic data, not on recommendation systems or optimization algorithms directly.
    - The criteria are high-level and may require further operationalization for application to PFMS-specific tasks like budget allocation.
  mapping_rationale: |
    A systematic scan of all 12 functional domains was conducted. The paper's primary contribution is a methodological framework for evaluating generative models, which maps directly to the "System Evaluation" domain (12.A, 12.B, 12.C) with high relevance. The criteria and concepts discussed are also contextually relevant to domains involving modeling user behavior (5.A) and making predictions (6.A), as the paper focuses on sequential data generation which underpins many predictive and profiling techniques. However, the paper does not address the specific financial contexts of budgeting, savings, or expense categorization (e.g., 3.A, 7.A), nor does it cover user design, privacy, or engagement, as it is a purely methodological survey on algorithmic evaluation. Borderline cases like 5.A were considered because the evaluation of generated behavioral profiles is relevant, but the paper's core contribution remains in evaluation methodology. Therefore, the primary relevance is to the evaluation framework domain, with contextual ties to algorithm performance.
limitations:
  - "The survey does not provide a unified, prescriptive evaluation protocol."
  - "It focuses on unconditional generation, not conditional generation which is more common in applied systems. [unacknowledged]"
  - "The framework's criteria are abstract and may conflict, with no guidance on balancing them. [unacknowledged]"
  - "The review's domain coverage is limited to five areas, leaving out other potential applications. [unacknowledged]"
remember_this:
  - "Evaluate generative models using five criteria: representativeness, novelty, realism, diversity, and coherence."
  - "Realism and coherence are prioritized for NLP/audio; novelty and representativeness for healthcare/mobility."
  - "GANs, combined with CNNs and RNNs, are the most prevalent architecture for synthetic sequential data."
  - "The proposed framework offers a common basis for comparing models across different domains."
  - "Current evaluations show a trade-off between novelty and representativeness in privacy-sensitive domains."