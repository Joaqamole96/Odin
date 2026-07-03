```yaml
paper_id: 10.48550/arXiv.2604.11290
designation: international-algorithm-specific
title: "Polyglot Teachers: Evaluating Language Models for Multilingual Synthetic Data Generation"
authors: "Miranda, L. J. V.; Vulic, I.; Korhonen, A."
year: 2026
venue: "Unknown"
odin_topics:
  - 5.C
  - 6.B
  - 7.D
  - 8.B
  - 12.B
  - 12.C
  - 2.A
  - 2.D
tldr: A systematic evaluation of language models as multilingual teachers for synthetic data generation reveals that model scale is less important than data quality metrics for student performance.
problem_and_motivation: Selecting teacher models for multilingual synthetic data generation is often ad hoc, defaulting to the largest models which may have capability gaps in non-English languages. This practice can produce poor-quality synthetic data, creating a need for a systematic way to measure teacher effectiveness.
approach:
  - Evaluated 10 teacher LMs across 6 typologically diverse languages by generating over 1.4M SFT examples.
  - Proposed POLYGLOT SCORE, a metric combining intrinsic data quality and extrinsic student model performance.
  - Measured intrinsic quality via prompt/response diversity, response perplexity, and a multilingual reward model score.
  - Assessed extrinsic performance by finetuning an OLMo 3 7B student model and evaluating on multilingual benchmarks.
  - Analyzed correlations between teacher model properties and data quality to identify factors driving effectiveness.
findings:
  - "num: Gemma 3 27B and Aya Expanse 32B are the most effective teachers, with PG-SCOREs of 0.726 and 0.706, respectively."
  - "num: Model scale does not significantly predict teacher effectiveness (p=0.507)."
  - "num: Data quality metrics (prompt diversity, length, response fluency) capture over 93.3% of variance in intrinsic quality."
  - "num: A linear model using principal components of intrinsic metrics predicts student performance with R2=0.664."
  - "num: Matching teacher-student model families yields at least a 20.5% increase in PG-SCORE."
  - For high-resource languages like German, the Generate method works best; for less-resourced languages, Respond or Translate methods are more effective.
  - Teacher performance varies significantly by language, likely due to pretraining data representation.
  - Teachers from the Gemma family consistently outperform others, including larger models from the Llama family.
key_figures_tables:
  - "Figure 1: Overview of POLYGLOT SCORE evaluation pipeline. → Pipeline combines intrinsic data quality and extrinsic student performance to assess teachers."
  - "Table 1: PG-SCORE of teacher models across 6 languages. → Gemma 3 27B and Aya Expanse 32B are top performers, regardless of size."
  - "Table 3: Regression results show model size and benchmark performance do not significantly predict PG-SCORE. → Common assumptions about teacher strength are insufficient."
  - "Figure 4: Linear regression of intrinsic PCs to predict extrinsic student performance. → Intrinsic data quality metrics are strong predictors of downstream performance."
key_equations:
  - equation: "PG-SCORET,ℓ = z-score(Intr.T,ℓ + Extr.T,ℓ)"
    explanation: "Combines intrinsic and extrinsic metrics into a single teacher effectiveness score."
  - equation: "Intr.T,ℓ = 1/|M| ∑_{m∈M} z-score(m(DT,ℓ))"
    explanation: "Averages normalized intrinsic quality metrics for a teacher on a language."
  - equation: "Extr.T,ℓ = 1/|B| ∑_{b∈B} (score_b(ST,ℓ) − score_b(Sϕ)) / (score_b(SREF) − score_b(Sϕ))"
    explanation: "Performance gain recovered by the student over a reference model."
definitions:
  - term: "POLYGLOT SCORE (PG-SCORE)"
    definition: "A metric to holistically assess a teacher model's effectiveness for multilingual synthetic data generation, combining intrinsic data quality and extrinsic student model performance."
  - term: "SFT"
    definition: "Supervised Fine-Tuning, a standard approach for adapting language models to specific tasks or languages."
  - term: "PGR"
    definition: "Performance Gap Recovered, a metric measuring the improvement of a finetuned student model over a base model relative to a reference."
  - term: "LLM-as-a-judge"
    definition: "Using a large language model to evaluate the quality of generated text based on a given rubric."
  - term: "CommonCrawl representation"
    definition: "The proportion of a language in the CommonCrawl dataset, used as a proxy for a language's presence in pretraining data."
critical_citations:
  - "[Kim et al., 2025] — Found model scale doesn't predict teacher effectiveness for English-based tasks."
  - "[Xu et al., 2025b] — Showed stronger models are not always better teachers for instruction tuning."
  - "[Pombal et al., 2025] — Introduced M-Prometheus, a strong multilingual reward model."
relevance:
  topics:
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "contextual"
      justification: "The paper's methodology of evaluating teacher models is analogous to selecting a model to generate training data for behavioral profile classification."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "The paper's evaluation framework for synthetic data generation can be directly adapted to select models for generating training data for spending forecasting modules."
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "medium"
      justification: "The principles of selecting effective 'teachers' for data generation can be applied to selecting models for generating training data for infeasibility handling in budget recommendations."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "The systematic approach to evaluating data generation quality is directly relevant for selecting teacher models to generate synthetic anomaly data for training detection algorithms."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "This paper provides a comprehensive evaluation framework (PG-SCORE) for algorithmic modules (teacher models) in a data generation pipeline."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "high"
      justification: "The structured, multi-metric evaluation methodology (intrinsic + extrinsic) can inform the design of evaluation frameworks for budget recommendation systems."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "contextual"
      justification: "The paper emphasizes the importance of cultural appropriateness in generated data, which is relevant to capturing culturally specific financial practices."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "contextual"
      justification: "The case study on Tagalog and the focus on cultural appropriateness in data generation are relevant to modeling Filipino-specific spending cycles."
  contribution: "This paper offers a systematic, data-centric approach to evaluating LMs as teachers, directly applicable to Odin's data generation needs for multiple modules. The POLYGLOT SCORE framework provides a blueprint for evaluating and selecting models for generating synthetic training data for forecasting, anomaly detection, and budget recommendation. Its finding that data quality metrics are more predictive than model scale offers a practical, cost-effective strategy for building these modules. The demonstrated effectiveness of model family matching provides a concrete heuristic for teacher selection. The case study on Tagalog validates the approach for a new language, suggesting adaptability to low-resource contexts."
  directly_justifies:
    - "The POLYGLOT SCORE framework offers a structured method to evaluate models for generating synthetic data."
    - "Model scale alone does not guarantee data generation quality, so small models can be effective."
    - "Data quality metrics such as prompt diversity and response fluency are predictive of student model performance."
    - "Matching teacher and student model families is a reliable heuristic for improving performance."
    - "For less-resourced languages, generating responses to existing prompts is more effective than few-shot generation."
  limits:
    - "The study evaluates only six languages, which limits the generalizability of findings to the full diversity of Odin's potential user base."
    - "The Translate method assumes access to English prompts that are meaningful for the target language, which may not always hold."
    - "The evaluation focuses on general-purpose benchmarks, not on financial or PFMS-specific tasks."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains of Spending Forecasting (6), Budget Recommendation (7), Anomaly Detection (8), and System Evaluation (12) were flagged as highly relevant due to the paper's direct contribution to selecting models for generating training data for these algorithmic modules. The domain of Behavioral Profiling & Classification (5) was assigned 'contextual' relevance as the methodology could be adapted. The domains of Filipino Cultural Context (2) were also marked 'contextual' due to the paper's focus on cultural appropriateness in data generation, which is relevant to modeling specific financial behaviors. The domains of Expense Categorization (3), Existing Systems (4), Mobile-First Design (9), Data Privacy (10), User Retention (11), and Savings & Debt Management (13) were considered but rejected as the paper does not provide citeable claims for these specific Odin domains. The paper's primary contribution is its evaluation framework and findings on synthetic data generation, which directly informs the development of data-centric algorithmic modules in Odin."
limitations:
  - "Language set limited to six typologically diverse languages, representing a small sample of the world's languages."
  - "Assumes access to English prompts for the Translate method, which may not always be culturally appropriate."
  - "Relies on automatic evaluation metrics that may not fully capture the nuances of human language quality."
  - "The computational cost of evaluating all teacher models via student finetuning is high. [unacknowledged]"
  - "Does not explore the potential for bias amplification in synthetic data pipelines, especially for low-resource languages. [unacknowledged]"
remember_this:
  - "Gemma 3 27B is an effective multilingual teacher for synthetic data generation."
  - "Model scale does not predict teacher effectiveness in multilingual settings."
  - "Data quality, not model size, is the primary driver of student performance."
  - "Teacher-student model family matching yields significant performance gains."
  - "For less-resourced languages, the Respond or Translate methods are most effective."
```