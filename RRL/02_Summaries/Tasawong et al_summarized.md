```yaml
paper_id: 10.48550/arXiv.2602.01618
designation: international-algorithm-specific
title: "SEA-Guard: Culturally Grounded Multilingual Safeguard for Southeast Asia"
authors: "Tasawong, P.; Ngui, J. G.; Aji, A. F.; Cohn, T.; Limkonchotiwat, P."
year: 2026
venue: arXiv
odin_topics:
  - 4.B
  - 5.C
  - 12.B
tldr: "Proposes SEA-Guard, a multilingual safeguard family for Southeast Asian languages and cultures, trained on an agentic data synthesis framework generating 870k culturally grounded safety samples per language across 8 SEA languages."
problem_and_motivation: "Existing safeguards are English-centric and fail to capture cultural nuances in Southeast Asian contexts, leading to weak performance on culturally sensitive content. Machine translation of English datasets misses regional subtleties, and native annotator scarcity limits data availability."
approach:
  - "Proposes an agentic data-generation framework with five components: input formulation, prompt/response generation, data annotation with MCRE, quality assurance, and model training."
  - "Uses Monte Carlo Reasoning Ensemble (MCRE) with N=10 stochastic reasoning passes for robust zero-shot safety classification, mapping a 5-way ordinal space to 3-way labels."
  - "Generates 870k samples per language across 8 SEA languages and 53 cultural categories using four LLMs for response diversity."
  - "Employs culture, topic, and usage classifiers for quality assurance, plus a bag-of-words deduplication procedure to remove lexically redundant samples."
  - "Trains three model variants (4B, 8B, 12B) via supervised fine-tuning on 870k samples per language with context length 8,192, batch size 6, and learning rate 5e-6."
  - "Evaluates on SEA-SafeguardBench (ITW and CG subsets), SEALS, SafeQA, and vision-text benchmarks using AUPRC as the primary metric."
findings:
  - "num: SEA-Guard-12B achieves 99.5% prompt and 75.2% response AUPRC on SEA-SafeguardBench, outperforming SOTA safeguards."
  - "num: SEA-Guard-12B outperforms Qwen3Guard-Gen 8B by 1.1 points on prompt classification and trails by only 0.6 points on response classification on generic benchmarks without training on generic safety data."
  - "num: SEA-Guard improves baseline vision-text safety performance in 6 out of 7 zero-shot settings."
  - "SEA-Guard models exhibit stronger human alignment (higher Spearman and Pearson correlations) than competing safeguards across severity levels."
  - "num: SEA-Guard remains robust under adversarial whitespace insertion attacks, maintaining high harmfulness scores while competitors degrade monotonically."
  - "num: Deduplication achieves comparable performance to the full 1M dataset with only 870k samples, reducing redundant patterns."
key_figures_tables:
  - "Table 1: SEA-Guard-12B achieves 79.5 prompt and 75.2 response AUPRC on SEA-SafeguardBench → outperforms all competitors."
  - "Table 2: SEA-Guard generalizes to generic safety benchmarks without training on generic data → competitive with SOTA."
  - "Table 3: SEA-Guard improves zero-shot vision-text safety in 6 of 7 benchmarks → emergent multimodal capability."
  - "Figure 3: SEA-Guard shows clearer separation across severity levels than competitors → better human alignment."
  - "Figure 4: SEA-Guard maintains high harmfulness under adversarial attacks → robust to surface-level perturbations."
  - "Figure 5: Performance scales with dataset size; deduplication matches full 1M performance at 870k → data efficiency."
key_equations:
  - equation: "h(x) = \\sum_{c \\in C_{safety}} s_c \\cdot P(\\hat{y}_{final} = c | R, x)"
    explanation: "Expected harmfulness score over ordinal safety labels."
  - equation: "P(C = c) \\propto 1 / \\text{freq}(c)"
    explanation: "Inverse-frequency sampling for balanced metadata coverage."
  - equation: "w_v = \\text{LMI}(v, y) = p(v,y) \\log(p(v,y) / (p(v) p(y)))"
    explanation: "Local mutual information for identifying lexically redundant training samples."
definitions:
  - term: "MCRE"
    definition: "Monte Carlo Reasoning Ensemble; robust zero-shot classification via multiple stochastic reasoning passes."
  - term: "SEA"
    definition: "Southeast Asia; region encompassing 11 countries with diverse languages and cultures."
  - term: "AUPRC"
    definition: "Area Under the Precision-Recall Curve; primary evaluation metric for safety classification."
  - term: "ITW"
    definition: "In-the-Wild; subset of SEA-SafeguardBench containing natural prompts."
  - term: "CG"
    definition: "Content Generation; subset of SEA-SafeguardBench containing generated prompts and responses."
critical_citations:
  - "[Zeng et al., 2024] — ShieldGemma baseline for safety moderation."
  - "[Inan et al., 2023] — LlamaGuard foundational safeguard model."
  - "[Shan et al., 2025] — SEALGuard for multilingual SEA safety."
  - "[Kumar et al., 2025] — PolyGuard for multilingual safety moderation."
  - "[Tan et al., 2025] — LionGuard-2 lightweight content moderator."
relevance:
  topics:
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Paper identifies gaps in existing safeguards for SEA languages and cultures, paralleling gaps in PFMS."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "contextual"
      justification: "MCRE classification methodology could inform financial behavioral profiling approaches."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Comprehensive evaluation framework (AUPRC, human alignment, adversarial robustness) is transferable to Odin module evaluation."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "contextual"
      justification: "Cultural grounding methodology for safety data can inform culturally aware financial practice modeling."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "contextual"
      justification: "Safeguards build user trust; paper's approach to safety and trust in AI systems is relevant."
  contribution: "This paper contributes a culturally grounded data synthesis framework and MCRE labeling methodology that can inform Odin's user classification and anomaly detection modules. The evaluation framework (AUPRC, human alignment, adversarial robustness) provides a template for assessing Odin's algorithmic modules. The deduplication approach offers a strategy for cleaning training data for financial behavior classification. The paper's treatment of cultural context in safety systems parallels the need for culturally aware financial recommendations in Odin."
  directly_justifies:
    - "MCRE provides a robust classification method for borderline cases in financial behavior profiling."
    - "Deduplication via bag-of-words reduces redundant patterns in training data without sacrificing coverage."
    - "Adversarial robustness testing is essential for anomaly detection systems in PFMS."
    - "Human alignment metrics (Spearman, Pearson) are critical for evaluating recommendation systems."
  limits:
    - "Paper focuses on content safety, not financial behavior or personal finance management."
    - "Cultural categories are broad (food, festivals, traditions) not specific to Filipino financial practices."
    - "Model evaluation does not include financial datasets or PFMS-specific tasks."
    - "Findings are specific to LLM safeguards and may not directly translate to classification of financial transactions."
  mapping_rationale: "Systematic scan of all 12 functional domains and their associated topic codes was performed. Domains flagged as relevant include: Existing Systems & Gaps (4.B, medium) due to the paper's explicit identification of limitations in current safeguards; Behavioral Profiling & Classification (5.C, contextual) because MCRE offers a classification approach transferable to financial profiling; and System Evaluation (12.B, medium) as the paper's multi-dimensional evaluation framework directly informs Odin module testing. The Filipino Cultural Context domain (2.A-D) was considered and rejected as low/contextual because the paper addresses general SEA cultural safety, not specifically Filipino financial practices. The Data Privacy & User Trust domain (10.A-B) was rated contextual—the paper discusses trust in AI safety but not PFMS-specific privacy. All other domains (Expense Categorization, Spending Forecasting, Budget Recommendation, Anomaly Detection, Mobile-First Design, User Retention, Savings & Debt Management) were rejected as not addressed. Overall, the paper provides methodological insights for culturally aware system design and evaluation rather than domain-specific PFMS contributions."
limitations:
  - "Covers only 8 of 700+ SEA languages and dialects, excluding Khmer, Lao, and Telugu."
  - "Did not experiment with 0.5B models; performance of smaller models may be unreliable for safety-critical applications."
  - "Vision-text benchmarks are English-only, limiting evaluation of multilingual vision capabilities."
  - "MCRE requires N=10 stochastic passes, incurring substantial computational overhead unsuitable for real-time use."
  - "Synthetic dataset may contain harmful content generated during data synthesis. [unacknowledged]"
remember_this:
  - "SEA-Guard-12B achieves 99.5% prompt AUPRC on cultural safety benchmarks."
  - "MCRE with N=10 stochastic passes improves human alignment over single-pass reasoning."
  - "Deduplication with bag-of-words achieves full 1M performance using only 870k samples."
  - "SEA-Guard generalizes to vision-text safety in 6 of 7 zero-shot benchmarks."
  - "Culturally grounded data synthesis is critical for multilingual safety systems."
```