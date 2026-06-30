# Compiled Research Summaries

## Filters Applied

- Designation: `international-algorithm-specific`

**Total Papers:** 25

**Note:** Included papers positions 51 to 75, Sorted by year.

---

## Paper 1: Lee C. et al_summarized.md

**Source File:** `Lee C. et al_summarized.md`

```yaml
paper_id: 10.1145/3706598.3714113
designation: international-algorithm-specific
title: VeriPlan: Integrating Formal Verification and LLMs into End-User Planning
authors: Lee, C. P.; Porfirio, D.; Wang, X. J.; Zhao, K. C.; Mutlu, B.
year: 2025
venue: CHI Conference on Human Factors in Computing Systems
odin_topics:
  - 4.A
  - 4.B
  - 5.A
  - 6.A
  - 7.A
  - 7.C
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 12.A
  - 12.B
tldr: Formal verification via model checking improves LLM reliability and user satisfaction in end-user planning by enforcing user-defined temporal constraints through a rule translator, flexibility sliders, and iterative feedback.
problem_and_motivation: Everyday users lack effective tools for complex planning tasks. LLMs show promise but produce unreliable outputs that violate user constraints, undermining trust and usability. A system is needed to verify LLM-generated plans against user-defined rules while keeping users in the loop.
approach:
  - VeriPlan combines an LLM planner with a rule translator that converts natural language constraints into Linear Temporal Logic (LTL) properties using a six-category template.
  - Flexibility sliders allow users to adjust constraint strictness, enabling soft and hard constraints to guide verification.
  - A model checker (PRISM/Stormpy) verifies LLM-generated plans against LTL properties and provides feedback on violations.
  - Users review and confirm translated rules, then iteratively refine plans through up to three verification cycles based on model checker feedback.
  - A user study with 12 participants across three planning scenarios evaluated four conditions: full system, without sliders, without translator, and without verification.
findings:
  - num: Full VeriPlan significantly outperformed no-translator and no-verification conditions in perceived performance (p=.0011 and p=.0013).
  - num: Usefulness scores were significantly higher for full system vs. no-slider (p=.047), no-translator (p=.009), and no-verification (p=.0257) conditions.
  - num: Satisfaction was significantly higher for full system vs. no-translator (p=.007) and no-verification (p=.0101) conditions.
  - Rule verification helped align user expectations, refine prompts, and provided deterministic boundaries that improved LLM accuracy.
  - Flexibility sliders enabled adaptive personalization but users found the impact of strictness percentages ambiguous.
  - Model checker feedback improved efficiency, transparency, and enabled creative exploration by acting as a safety net.
  - The mind-map interface supported understanding, feedback application, and plan organization based on user preferences.
key_figures_tables:
  - Figure 1: Comparison of LLM interaction without VeriPlan (left) and with VeriPlan (right) → VeriPlan adds rule extraction, verification, and iterative refinement.
  - Figure 6: Bar graphs of perceived performance, usefulness, ease, and satisfaction across conditions → Full system consistently outperforms ablated versions.
key_equations:
  - equation: G (¬ brownMeatballs U mixingMeatballIngredients)
    explanation: LTL formula for strict sequential order constraint.
  - equation: G (F cookingDinner → F homeworkAssistance ∧ F dogWalking ∧ F eveningCleanup)
    explanation: LTL formula for concurrent events after a precondition.
  - equation: ¬ ( ((P3_waitingRoom ∧ P2_waitingRoom) ∨ (P3_waitingRoom ∧ P4_waitingRoom)) ∧ ¬ (P3_waitingRoom ∧ P1_waitingRoom) ) U (P3_waitingRoom ∧ P2_waitingRoom ∧ P4_waitingRoom ∧ P1_waitingRoom)
    explanation: LTL formula for exclusive constraints preventing pair conflicts.
definitions:
  - term: LTL
    definition: Linear Temporal Logic; a formal logic for expressing temporal properties over sequences of states.
  - term: Model Checking
    definition: A formal verification technique that exhaustively checks if a system model satisfies specified properties.
  - term: PRISM
    definition: A probabilistic model checker used to verify systems against temporal logic properties.
  - term: Stormpy
    definition: Python API for the Storm model checker, enabling programmatic verification.
  - term: Hallucination
    definition: LLM-generated text that is coherent but factually incorrect or nonsensical.
  - term: Flexibility Sliders
    definition: User interface controls to adjust strictness of constraints from soft to hard.
critical_citations:
  - "[Kambhampati et al., 2024] — Position paper on LLM-Modulo frameworks for planning."
  - "[Valmeekam et al., 2023] — Critical evaluation of LLM planning abilities showing 12% success rate for GPT-4."
  - "[Achiam et al., 2023] — GPT-4 technical report; powers VeriPlan's LLM agents."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides background on automated planning tools and accessibility barriers.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies LLM limitations in planning accuracy, consistency, and user trust.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: low
      justification: General user preference specification relevant but not finance-specific.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: contextual
      justification: Verification approach could be applied to forecasting models indirectly.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Rule-based constraints and flexibility mapping parallel budget allocation constraints.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: medium
      justification: Model checking enforces constraints analogous to budget optimization.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: contextual
      justification: Interface design implications are generalizable to mobile contexts.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: UX insights on mind-map layouts and feedback could inform mobile PFMS design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Verification improves reliability but privacy not directly addressed.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Directly shows verification improves user trust, satisfaction, and perceived reliability.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Iterative refinement and user control features enhance engagement.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: User control and transparency features support retention through improved experience.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a structured ablation study methodology applicable to PFMS evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Directly evaluates algorithmic modules (rule translator, model checker) via user study.
  contribution: "VeriPlan demonstrates that integrating formal verification (model checking) with LLMs enhances planning reliability and user satisfaction. The rule translator lowers barriers by converting natural language constraints to LTL, enabling non-experts to specify rules. Flexibility sliders allow users to balance constraint strictness, supporting adaptive personalization. The model checker provides deterministic feedback, improving transparency and trust. These design patterns are directly applicable to Odin's budget recommendation, anomaly detection, and user constraint modules."
  directly_justifies:
    - "Formal verification significantly improves perceived performance and satisfaction in LLM-based planning systems."
    - "User-defined constraints and iterative verification enhance trust and alignment with personal goals."
    - "Flexibility sliders enable users to prioritize and adapt rules based on evolving preferences."
    - "Visual, interactive interfaces improve understanding and feedback application in LLM systems."
    - "Model checking acts as an external guardrail, reducing cognitive burden and error detection."
  limits:
    - "User study limited to 12 participants and three planning scenarios; finance-specific validation needed."
    - "Temporal constraint template covers six categories; Odin may require additional finance-specific constraints."
    - "System does not handle ambiguous or evolving constraints beyond slider adjustments."
    - "No proactive suggestions or automated repair; users must manually adjust constraints."
    - "Model checker state space may not scale to complex financial planning with many transactions."
  mapping_rationale: "A systematic scan across all 12 functional domains and 38 topic codes was performed. Domains flagged as relevant include: Existing Systems & Gaps (4.A, 4.B) for LLM limitations and planning tool accessibility; Behavioral Profiling (5.A) for user preference specification; Spending Forecasting (6.A) for potential application of verification to predictive models; Budget Recommendation (7.A, 7.C) for constraint-based optimization parallels; Mobile-First Design (9.A, 9.B) for UX insights; Data Privacy & Trust (10.A, 10.B) as verification directly improves trust; User Retention & Engagement (11.A, 11.B) via iterative user control; and System Evaluation (12.A, 12.B) for the ablation study methodology. Borderline cases: seasonal spending (2.B, 2.D) was rejected as the paper does not address temporal patterns in spending. Expense categorization (3.A) was rejected as VeriPlan focuses on action sequences, not transaction classification. Savings/debt management (13.A, 13.B) were rejected as financial goals are not modeled. The paper's core contribution—applying model checking to enforce user-defined constraints in LLM-generated plans—most directly justifies topics 10.B (user trust), 12.A (evaluation frameworks), and 12.B (algorithmic evaluation), with medium relevance to 7.C (constrained optimization) and 11.A/B (engagement/retention). Overall relevance is high for Odin's needs in user-controlled verification and trust-building."
limitations:
  - "Temporal constraint types are limited to six categories; Odin may need more finance-specific constraints. [unacknowledged]"
  - "User sample (n=12) is small and not representative of Filipino young professionals. [unacknowledged]"
  - "System only supports single interactions without contextual memory for iterative rule refinement."
  - "Impact of slider strictness percentages was ambiguous for users."
  - "No automated or proactive suggestions for constraint adjustment or repair."
remember_this:
  - "Model checking improves LLM performance, usefulness, and satisfaction in planning tasks."
  - "User-defined constraints and iterative verification build trust and alignment with personal goals."
  - "Flexibility sliders enable adaptive personalization but strictness impact was ambiguous."
  - "Visual mind-map interfaces improve understanding and feedback application."
  - "num: Full VeriPlan showed significant performance gains (p<.01) over no-verification conditions."
```
---

## Paper 2: Song et al_summarized.md

**Source File:** `Song et al_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international-algorithm-specific
title: Deep learning-based time series forecasting
authors: Song, X.; Deng, L.; Wang, H.; Zhang, Y.; He, Y.; Cao, W.
year: 2025
venue: Artificial Intelligence Review
odin_topics:
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
  - 12.C
tldr: A comprehensive survey of deep learning time series forecasting models (2014-2024) analyzing temporal and variable correlations, computational efficiency, and loss functions, with findings that simpler linear models often outperform complex ones.
problem_and_motivation: Accurate time series forecasting is critical for domains like energy, finance, and health, but existing deep learning models face challenges in capturing complex temporal patterns and computational efficiency. A systematic review and comparison of these models is needed to guide both research and practical application.
approach:
  - The paper surveys over 30 deep learning forecasting models developed between 2014 and 2024, including RNNs, CNNs, Transformers, and linear models.
  - It introduces a novel classification based on the logic of time series information mining, distinguishing approaches that model time-step dependencies from those modeling variable correlations.
  - It analyzes methods for long-term forecasting optimization, including sequence shortening and attention sparsification, to address the quadratic complexity of standard Transformers.
  - The study categorizes loss functions into single-objective (MAE, MSE, quantile) and hybrid (negative log-likelihood, adversarial) types, explaining their suitability for different prediction tasks.
  - It provides an extensive empirical evaluation on five real-world datasets (ETT, Electricity, Exchange, Traffic, ILI) and an artificial dataset, comparing models on prediction accuracy, information mining, and computational complexity.
findings:
  - num: DLinear, a simple linear model, often outperforms sophisticated deep learning models in prediction accuracy, demonstrating that complex architectures may not effectively capture temporal dependencies.
  - num: Shuffling input sequences for models like DLinear and PatchTST caused prediction accuracy drops of up to 1092.50% (MSE) on the Exchange dataset, while many complex models showed minimal change, indicating overfitting and poor utilization of temporal order.
  - num: Extending the lookback window for complex models (e.g., ETSformer, Autoformer) did not consistently improve accuracy, suggesting overfitting and noise interference, whereas PatchTST and DLinear benefited from longer sequences.
  - Models using frequency-domain methods for seasonal information extraction (Fedformer, ETSformer, TDformer) outperformed time-domain methods (LSTnet, DLinear) on an artificial dataset, with Fedformer showing up to 44.17% lower MSE for seasonal term prediction.
  - The patch-slicing approach (PatchTST, Pyraformer) effectively reduces attention mechanism complexity while improving accuracy, with PatchTST achieving 28.83% lower MAE and 42.09% lower MSE than LogTrans on the ETTh1 dataset for a prediction length of 336.
key_figures_tables:
  - Table 5: Multivariate forecasting results → DLinear and PatchTST consistently achieve top performance across datasets and horizons.
  - Table 7: Input shuffling experiment → Complex models show significantly lower performance drops, indicating weaker use of temporal order than simpler models.
  - Table 8: Lookback window extension → Performance of complex models often degrades with longer inputs, while DLinear and PatchTST benefit.
  - Table 9: Trend and season prediction on artificial data → Fedformer and TDformer excel at trend terms, while frequency-domain models excel at season terms.
  - Figure 20: Inference time comparison → Reformer has the lowest inference time, followed by PatchTST.
  - Figure 21: Memory occupation comparison → PatchTST has the lowest memory usage, especially for long-term forecasting.
key_equations:
  - equation: "LSTM: i_t = σ(W_xi x_t + W_hi h_{t-1} + b_i), f_t = σ(W_xf x_t + W_hf h_{t-1} + b_f), c_t = f_t * c_{t-1} + i_t * tanh(W_xc x_t + W_hc h_{t-1} + b_c), h_t = o_t * tanh(c_t)"
    explanation: LSTM gating mechanisms for long-term dependency capture.
  - equation: "Attention: O = V Softmax(Q^T K / √D_k)"
    explanation: Core transformer attention mechanism for similarity computation.
  - equation: "Auto-Correlation: τ_1,...,τ_k = arg Top_{τ∈{1,...,L}} R(τ), Auto-Correlation(X) = Σ Roll(X,τ_i) * R_hat(τ_i)"
    explanation: Autoformer's method for extracting seasonal patterns via time-delay similarity.
definitions:
  - term: Time-step dependency
    definition: Correlations between consecutive and distant time steps in a sequence.
  - term: Variable correlation
    definition: Interdependencies among different univariate time series in a multivariate dataset.
  - term: Patch slicing
    definition: Dividing a long time series into fixed-length segments for efficient attention computation.
  - term: Frequency domain analysis
    definition: Transforming time series to frequencies using Fourier transforms to extract periodic patterns.
  - term: Non-stationary information
    definition: Variations in statistical properties (mean, variance) of a time series over time.
critical_citations:
  - "[Vaswani et al., 2017] — Introduced Transformer architecture."
  - "[Wu et al., 2021] — Proposed Autoformer with time series decomposition."
  - "[Zhou et al., 2021] — Developed Informer for efficient long-term forecasting."
  - "[Nie et al., 2022] — Introduced PatchTST with patch-slicing attention."
  - "[Goodfellow et al., 2014] — Foundation for adversarial loss functions."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Provides comprehensive review of deep learning models for time series forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Evaluates and compares numerous forecasting algorithms applicable to spending data.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Informs the choice of forecasting models that can be used in budget recommendation systems.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Findings on model performance inform algorithm selection for budget recommendation.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Forecasting accuracy and uncertainty measures are relevant for anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Models evaluated are applicable to anomaly detection in spending patterns.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides rigorous evaluation methodology (MAE, MSE, MAPE, R2) for forecasting modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Extensive comparison of different algorithms (DLinear, PatchTST, Transformer variants) on multiple datasets.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Evaluation metrics and experimental setups can be adapted for budget recommendation evaluation.
  contribution: "The paper provides Odin with a systematic, evidence-based evaluation of state-of-the-art time series forecasting models, directly informing algorithm selection for its core spending forecasting and budget recommendation modules. Its demonstration that simpler linear models (DLinear) can outperform complex Transformers challenges assumptions about model complexity and suggests a more efficient architecture for Odin's deployment. The detailed analysis of model behavior under input shuffling and lookback window extension reveals critical overfitting and noise-handling limitations, guiding Odin's development team on potential pitfalls. The classification of loss functions and their suitability for different data characteristics (e.g., outlier-heavy vs. information-rich points) provides design guidance for Odin's optimization objectives. Overall, this survey serves as a foundational technical reference for implementing, evaluating, and justifying Odin's algorithmic core."
  directly_justifies:
    - "DLinear's linear layer effectively captures sequential information for time series forecasting."
    - "PatchTST's patch-slicing method reduces attention complexity while improving prediction accuracy."
    - "Frequency domain methods (Fedformer, ETSformer) excel at extracting seasonal spending patterns."
    - "Complex models (Autoformer, ETSformer) suffer from overfitting and poor utilization of temporal order."
    - "Extending lookback windows does not consistently improve complex models, suggesting noise interference."
  limits:
    - "The survey is general and does not address the specific characteristics of personal financial spending data, such as user-defined categories or irregular transaction timing."
    - "Findings on overfitting and model selection are based on benchmark datasets (e.g., Electricity, Traffic) that may not fully represent the financial behavior of Filipino young professionals."
    - "The paper does not evaluate models under mobile-first design constraints like latency or limited on-device compute."
    - "Recommendations for probabilistic forecasting are mentioned but not deeply explored in the empirical evaluation."
  mapping_rationale: "The systematic scan across all 12 functional domains and 38 canonical topic codes flagged the core technical domains (Spending Forecasting, Budget Recommendation, Anomaly Detection, and System Evaluation) as highly relevant. Within these, topics 6.A, 6.B, 12.A, and 12.B were assigned 'high' relevance due to the paper's direct focus on evaluating and comparing forecasting algorithms. Topics 7.B and 8.B received 'medium' relevance because while the paper does not directly address recommendation or detection, its findings on model performance are directly transferable to those modules. Borderline cases included 2.B (Seasonal and Cyclical Spending Patterns), which was considered but rejected (low relevance) because the paper does not address cultural or domain-specific seasonality—it focuses on generic periodic patterns in electricity, traffic, and finance. Similarly, 3.A (Expense Categorization Frameworks) was considered and rejected (contextual) as the paper does not discuss category design or user-defined constraints. Topics related to privacy, engagement, and behavioral profiling were deemed irrelevant (not selected) due to a complete lack of coverage. The paper's overall relevance to Odin is high as a comprehensive technical reference for algorithm selection, evaluation, and optimization."
limitations:
  - "Does not address specific financial data challenges like irregular intervals or user-defined categories. [unacknowledged]"
  - "Evaluation datasets are from energy, traffic, and healthcare, not personal finance. [unacknowledged]"
  - "Does not consider model deployment constraints like latency or on-device inference for mobile applications. [unacknowledged]"
  - "The paper acknowledges that most models are designed for fixed input/output lengths, limiting flexibility for on-demand forecasting."
  - "Does not provide guidance on handling missing or sparse data, common in personal finance. [unacknowledged]"
remember_this:
  - "DLinear often outperforms complex deep learning models in time series forecasting."
  - "Patch slicing effectively reduces attention complexity while maintaining high accuracy."
  - "Simple linear models better utilize sequential order than sophisticated architectures."
  - "Frequency domain methods excel at extracting seasonal patterns from time series data."
  - "Extending lookback windows does not consistently improve complex models due to overfitting."
```
---

## Paper 3: Ao et al_summarized.md

**Source File:** `Ao et al_summarized.md`

```yaml
paper_id: "10.1109/ACCESS.2025.3602791"
designation: "international-algorithm-specific"
title: "A Review of Time Series Prediction Models Based on Deep Learning"
authors: "Ao, X.; Gong, Y.; He, A."
year: 2025
venue: "IEEE Access"
odin_topics:
  - "6.A"
  - "6.B"
  - "8.A"
  - "8.B"
  - "12.A"
  - "12.B"
tldr: "Reviews deep learning time series models (CNNs, RNNs, Transformers, GNNs, hybrids) and provides a task-oriented selection framework based on sequence length, multivariate support, and efficiency."
problem_and_motivation: "Real-world time series are nonlinear and non-stationary, making traditional statistical models inadequate. Deep learning offers nonlinear modeling and feature extraction but lacks systematic, application-oriented selection guidelines. This survey addresses the gap by structuring model comparison and selection based on task requirements."
approach:
  - "Systematically reviews prominent DL model families: CNNs, RNNs (LSTM/GRU), Transformer variants (Informer, Autoformer, iTransformer), GNNs, and hybrid models."
  - "Analyzes core principles, strengths, limitations, and key architectural innovations (e.g., dilated convolutions in TCN, gating in LSTM/GRU, ProbSparse attention in Informer)."
  - "Proposes a task-oriented framework evaluating models across sequence length handling, multivariate support, interpretability, computational efficiency, and real-time performance."
  - "Provides in-depth comparative analysis of model categories using tabulated attributes and cross-model trend analysis from benchmark studies."
  - "Discusses emerging challenges: interpretability, efficiency optimization, and integration of multi-source data/domain knowledge."
findings:
  - "num: Informer reduces self-attention complexity from O(L^2) to O(L log L)."
  - "num: ETSformer reduces inference latency by 37% compared to Autoformer on ETT data."
  - "num: PatchTST achieves 23% lower MSE than Informer with 60% less GPU memory."
  - "num: ARIMA-RNN hybrid achieved 15% MAE reduction on Electricity Load Dataset compared to standalone models."
  - "Transformer variants dominate ultra-long horizon forecasting (>1000 steps) in multivariate settings."
  - "GNNs excel when strong spatial/relational dependencies exist (e.g., traffic, supply chains)."
  - "Hybrid models (e.g., N-BEATS, ETSformer) enhance accuracy and interpretability by combining statistical decomposition with deep learning."
  - "iTransformer's inverted architecture (variables as tokens) shows strong multivariate generalization."
  - "Model selection depends on trade-offs between modeling power, efficiency, sequential fidelity, and interpretability."
  - "Emerging trend: simpler unified architectures (iTransformer, PatchTST) reduce complex, custom-designed components."
key_figures_tables:
  - "Figure 1: Structure of one-dimensional CNN → CNN extracts local spatial patterns via convolution and pooling."
  - "Figure 2: Dilated causal convolution in TCN → Expands receptive field without increasing depth."
  - "Figure 3: TCN residual block → Residual connections improve training stability in deep networks."
  - "Table 1: Analysis of CNN-based algorithms → Compares CNN, TCN, WaveNet-CNN, Kmeans-CNN, SCINet."
  - "Table 6: Comparative analysis of model categories → Summarizes strengths and limitations of CNN, RNN, Transformer, GNN, Hybrid models."
  - "Figure 12: Task-driven model selection framework → Matches problem characteristics (sequence length, dependencies) to optimal model classes."
key_equations:
  - equation: "TCN = 1DFCN + causal convolutions"
    explanation: "Simplified formula for Temporal Convolutional Network structure."
definitions:
  - term: "CNN"
    definition: "Convolutional Neural Network, excels at extracting local spatial features."
  - term: "TCN"
    definition: "Temporal Convolutional Network, uses dilated causal convolutions for long-range dependencies."
  - term: "RNN"
    definition: "Recurrent Neural Network, processes sequential data with hidden state memory."
  - term: "LSTM"
    definition: "Long Short-Term Memory, RNN variant with gating mechanisms for long-term dependencies."
  - term: "GRU"
    definition: "Gated Recurrent Unit, simplified LSTM with update and reset gates."
  - term: "GNN"
    definition: "Graph Neural Network, models relational dependencies using graph structures."
  - term: "GCN"
    definition: "Graph Convolutional Network, performs convolution on graph data for spatial dependencies."
  - term: "STGCN"
    definition: "Spatio-Temporal Graph Convolutional Network, joint spatial and temporal modeling."
  - term: "MTGNN"
    definition: "Multivariate Time Series Graph Neural Network, learns dynamic graph structures."
  - term: "ARIMA"
    definition: "Autoregressive Integrated Moving Average, classical statistical model for linear time series."
critical_citations:
  - "[Vaswani et al., 2017] — Introduced Transformer with self-attention, foundational for many models."
  - "[Hochreiter & Schmidhuber, 1997] — Introduced LSTM, solving gradient vanishing for long sequences."
  - "[Bai et al., 2018] — Proposed TCN for efficient sequence modeling with causal convolutions."
  - "[Zhou et al., 2021] — Informer with ProbSparse attention for efficient long-sequence forecasting."
  - "[Wu et al., 2021] — Autoformer integrating series decomposition and auto-correlation."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Core survey on deep learning predictive models directly applicable to Odin's forecasting modules."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Reviews RNNs, Transformers, and hybrids specifically for sequential data forecasting."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses models (e.g., CNN, LSTM) applicable to anomaly detection in spending sequences."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "medium"
      justification: "Provides algorithmic foundations (TCN, LSTM) that can be adapted for anomaly detection."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides comparative analysis framework and task-driven selection relevant for evaluation."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Discusses evaluation across dimensions (accuracy, efficiency, interpretability) relevant to module assessment."
  contribution: "This survey directly informs Odin's predictive modeling and anomaly detection modules by providing a structured comparison of DL algorithms suitable for spending data. The task-oriented selection framework helps choose models (e.g., LSTM/GRU for sequential spending, GNN for multivariate dependencies, hybrids for accuracy) based on Odin's specific requirements. The analysis of efficiency trade-offs informs mobile-first implementation choices and real-time constraints. The discussion on model interpretability guides Odin's need for explainable predictions to build user trust. The coverage of emerging challenges like computational efficiency and domain knowledge integration aligns with Odin's practical deployment needs."
  directly_justifies:
    - "LSTM and GRU effectively capture long-term dependencies in sequential spending data."
    - "Transformer variants like Informer enable efficient long-sequence forecasting for spending patterns."
    - "Hybrid models combining statistical methods with DL improve forecasting accuracy and robustness."
    - "Model selection should match sequence length, multivariate dependencies, and efficiency constraints."
    - "Attention mechanisms provide a basis for model interpretability in financial predictions."
  limits:
    - "Focuses on algorithmic capabilities without addressing financial domain-specific constraints (e.g., user allocation rules)."
    - "Does not evaluate models on PFMS-specific data like Philippine spending cycles. [unacknowledged]"
    - "Lacks detailed discussion on cold-start scenarios common in personal finance apps. [unacknowledged]"
    - "Computational benchmarks are not directly applicable to mobile-device resource constraints. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains was conducted. The paper was flagged as highly relevant to the Predictive Modeling (6.A) and Forecasting Algorithms (6.B) domains because it is a comprehensive review of DL models for time series prediction, directly applicable to Odin's spending forecasting. It also provided medium relevance to Anomaly Detection (8.A, 8.B) as the reviewed models can be adapted for this purpose, and to System Evaluation (12.A, 12.B) through its proposed comparison framework. Borderline cases included the discussion of GNNs for multivariate dependencies, which primarily supports 6.B but also touches on 8.B for network-based anomaly detection. Domains related to user behavior (1.A-C, 5.A-C), cultural context (2.A-D), expense categorization (3.A-C), system landscape (4.A-B), budgeting (7.A-D), mobile design (9.A-B), privacy (10.A-B), retention (11.A-B), and savings/debt (13.A-C) were considered and rejected as the paper is purely algorithmic and does not address user, cultural, design, or financial domain-specific constraints. Overall, the paper provides strong foundational knowledge for Odin's predictive and detection algorithms but requires supplementation with domain-specific and contextual research."
limitations:
  - "Interpretability remains challenging across all Transformer variants."
  - "High computational complexity demands substantial resources for large-scale data. [unacknowledged]"
  - "The performance of specialized models depends on matching design assumptions to data characteristics."
  - "General models need more data to achieve robustness compared to specialized ones. [unacknowledged]"
  - "Decomposition-based hybrids incur computational redundancy from iterative operations. [unacknowledged]"
remember_this:
  - "Informer reduces self-attention complexity to O(L log L) for long sequences."
  - "ETSformer cuts inference latency by 37% versus Autoformer."
  - "PatchTST achieves 23% lower MSE than Informer with 60% less memory."
  - "Model selection must balance modeling power, efficiency, and interpretability."
  - "Hybrid models combining statistics and deep learning enhance accuracy and explainability."
```
---

## Paper 4: Singh U. et al_summarized.md

**Source File:** `Singh U. et al_summarized.md`

```yaml
paper_id: d3b07384-d9a1-11f0-9d8a-00155d0e6b4c
designation: international-algorithm-specific
title: A Predictive Framework for Annual Financial Planning using Deep Learning Models
authors: Singh, U.; Anand, U.; Singh, V.
year: 2025
venue: Journal of Scientific Innovation and Advanced Research (JSIAR)
odin_topics:
  - 6.A
  - 6.B
  - 4.B
  - 7.B
tldr: Deep learning models, particularly LSTM, outperform traditional statistical methods for annual expense forecasting by capturing complex temporal dependencies in financial data.
problem_and_motivation: Traditional forecasting methods like ARIMA and linear regression fail to capture the non-linear and dynamic nature of real-world financial data, limiting accuracy for long-term planning. There is a need for a more accurate and adaptive framework for annual expense forecasting to support proactive fiscal decision-making.
approach:
  - Financial datasets were collected from public expenditure portals and augmented with synthetic data.
  - Data was preprocessed with missing value imputation, min-max normalization, and sliding window sequence creation.
  - LSTM and GRU models were designed and compared against a baseline RNN for annual expense forecasting.
  - Hyperparameters were tuned using grid search and Bayesian optimization, with dropout and early stopping to prevent overfitting.
  - Models were evaluated using MAE, RMSE, and MAPE metrics on a temporal split of the dataset.
findings:
  - "num: LSTM achieved the lowest MAE of 1872.56, compared to 2450.13 for RNN."
  - "num: LSTM's RMSE was 2614.32, demonstrating superior stability over the RNN (3120.88)."
  - "num: The MAPE for LSTM was 7.02%, outperforming both GRU (7.48%) and RNN (9.85%)."
  - LSTM forecasts closely followed the true trend of annual spending with minimal deviation, validating its applicability for long-term planning.
  - The use of dropout layers and early stopping effectively mitigated overfitting during LSTM training.
  - GRU provided a computationally efficient alternative with comparable accuracy to LSTM.
  - Deep learning models demonstrated strong generalization and stability across the training and validation phases.
  - The framework enables better resource allocation and risk assessment for organizational financial planning.
key_figures_tables:
  - "Figure 1: System architecture of the proposed framework → Shows the layered, modular design for financial forecasting."
  - "Figure 2: Data processing and forecasting pipeline → Illustrates the sequential workflow from ingestion to prediction."
  - "Figure 4: LSTM predicted vs. actual expenses → Forecasts closely follow the true annual expenditure trend."
  - "Figure 5: Training and validation loss per epoch for LSTM → Smooth convergence indicates robustness without overfitting."
  - "Table II: Performance comparison of models → LSTM outperforms RNN and GRU across all error metrics."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "LSTM"
    definition: "Long Short-Term Memory, a recurrent neural network architecture designed to capture long-term dependencies."
  - term: "GRU"
    definition: "Gated Recurrent Unit, a simplified recurrent neural network variant with computational efficiency."
  - term: "MAE"
    definition: "Mean Absolute Error, a metric measuring the average magnitude of prediction errors."
  - term: "RMSE"
    definition: "Root Mean Squared Error, a metric that penalizes larger errors more heavily."
  - term: "MAPE"
    definition: "Mean Absolute Percentage Error, a metric expressing prediction accuracy as a percentage."
critical_citations:
  - "[Siami-Namini et al., 2019] — LSTM outperforms ARIMA in accuracy."
  - "[Fischer and Krauss, 2018] — Deep nets achieve higher returns than econometric models."
relevance:
  topics:
    - code: 6.A
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: high
      justification: "Paper proposes and evaluates a deep learning framework for annual expense forecasting."
    - code: 6.B
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: high
      justification: "Paper benchmarks LSTM and GRU, which are key algorithms for sequential data, against traditional methods."
    - code: 4.B
      name: "Limitations and Gaps in Existing Systems"
      relevance: medium
      justification: "Explicitly identifies limitations of traditional statistical methods like ARIMA and linear regression."
    - code: 7.B
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: contextual
      justification: "Establishes the predictive foundation that is a prerequisite for effective budget recommendation systems."
  contribution: "The paper provides a validated LSTM-based framework that can serve as a core predictive module for Odin's spending forecasting. Its comparative analysis justifies the selection of deep learning over classical methods for Odin's forecasting component. The demonstrated ability to capture seasonal patterns directly supports Odin's need to model Filipino spending cycles. The emphasis on long-term annual forecasting aligns with Odin's goal of providing annual budget recommendations."
  directly_justifies:
    - "LSTM significantly outperforms ARIMA and linear regression in forecasting accuracy."
    - "Deep learning models can capture non-linear patterns that traditional methods miss."
    - "The proposed framework is robust for long-term (annual) financial planning."
  limits:
    - "The study focuses on annual forecasting, while Odin may require monthly or weekly predictions for granular insights."
    - "The framework's dependency on high-quality data is a limitation for real-world deployment with potentially noisy data."
  mapping_rationale: "A systematic scan was performed across all 12 functional domains and their associated topic codes. The domains of 'Spending Forecasting' (6.A, 6.B) were flagged as highly relevant, as the paper's core contribution is a predictive framework for annual expenses. The 'Existing Systems & Gaps' domain (4.B) was flagged as medium relevance because the paper explicitly critiques the limitations of traditional statistical methods like ARIMA, which directly informs Odin's design choices. The 'Budget Recommendation' domain (7.B) was considered contextual, as accurate forecasting is a prerequisite for budget recommendations, but the paper does not directly address recommendation algorithms. Domains such as 'Filipino Cultural Context', 'Behavioral Profiling', and 'Mobile-First Design' were considered and rejected, as the paper does not address these aspects and its data originates from public expenditure sources, not the Philippines. The paper's overall relevance to Odin is high for its algorithmic contributions to forecasting, providing a validated baseline for the system's predictive engine."
limitations:
  - "The paper does not address the cold-start problem, which is critical for new users in a PFMS. [unacknowledged]"
  - "The proposed models are evaluated on a specific financial domain; their generalizability to personal finance data may be limited. [unacknowledged]"
  - "The framework's performance with noisy or incomplete data, a common real-world scenario, is not discussed. [unacknowledged]"
remember_this:
  - "LSTM achieved 7.02% MAPE for annual expense forecasting."
  - "LSTM and GRU outperform ARIMA and linear regression for sequential financial data."
  - "Deep learning captures non-linear patterns that traditional methods fail to model."
  - "The study validates deep learning for long-term annual financial planning."
  - "Model robustness is ensured through techniques like dropout and early stopping."
```
---

## Paper 5: Lu et al_summarized.md

**Source File:** `Lu et al_summarized.md`

```yaml
paper_id: 10.51903/jtie.v4i3.466
designation: international-algorithm-specific
title: A Constrained, Data-Driven Budgeting Framework Integrating Macro Demand Forecasting and Marketing Response Modeling
authors: Lu, Y.; Zhou, H.; Zhang, Y.
year: 2025
venue: Journal of Technology Informatics and Engineering (JTIE)
odin_topics:
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 7.C
  - 7.D
  - 12.A
  - 12.B
  - 12.C
tldr: A framework integrating macro demand forecasting, marketing response modeling, and constrained optimization allocates marketing spend under SG&A and cash-flow constraints, demonstrating that optimal budgets often fall below ratio caps due to diminishing returns and demand uncertainty.
problem_and_motivation: Budgeting requires combining heterogeneous signals (macro demand, marketing effectiveness, accounting constraints) into a single auditable decision process. Existing approaches treat these components separately, leading to plans that violate ratio constraints under demand uncertainty. A unified pipeline linking forecasting, response modeling, and optimization is needed to produce defensible and constraint-aware recommendations.
approach:
  - Quarterly Personal Consumption Expenditures components from FRED (2010Q1-2025Q3) serve as macro demand proxy.
  - Four forecasting models are compared in a rolling backtest: seasonal naïve, SARIMAX, gradient boosting, and multivariate VAR.
  - Marketing response is estimated from the Advertising dataset (TV, radio, newspaper spend) using OLS, ridge, lasso, gradient boosting, and a Hill saturation model.
  - Constraints (gross margin, SG&A ratio, operating cash-flow coverage) are calibrated from Apple Inc.'s FY2025 Form 10-K.
  - Budget allocation is solved via grid search over channel shares and budget utilization, evaluated with 500 Monte Carlo scenarios under demand uncertainty.
  - Risk aversion is incorporated via a mean-risk objective with parameter λ to trade off expected profit and volatility.
findings:
  - "num: Multivariate VAR achieves ≈2.85% MAPE for aggregate demand, outperforming seasonal naïve (≈6.06% MAPE)."
  - "num: The Hill saturation model identifies newspaper spend as having near-zero marginal return (coefficient ≈0)."
  - "num: The risk-neutral optimizer allocates 25% to TV and 75% to radio, spending ≈0.97% of revenue, below the 1.5% SG&A cap."
  - "num: Spending at the deterministic cap would violate the SG&A constraint in ≈40% of scenarios due to revenue uncertainty, while the optimized spend maintains 100% satisfaction."
  - Marketing response curves exhibit strong diminishing returns, with radio saturating quickly and TV providing moderate marginal returns.
key_figures_tables:
  - "Table 7: Category-level forecast accuracy shows VAR achieves lowest RMSE for durables (97.24) and services (731.35) → multivariate models improve over seasonal baseline."
  - "Table 4: Marketing model comparison shows gradient boosting best predictive fit (CV_RMSE=0.661), but Hill model provides interpretable saturation curves."
  - "Figure 5: Hill-model marginal response curves show radio has highest marginal ROI at low spend, newspaper near-zero → allocate initial dollars to radio, then diversify."
  - "Figure 6: Profit-risk frontier under demand uncertainty shows trade-off between expected profit and volatility, with risk-neutral point highlighted."
  - "Table 12: Sensitivity to marketing cap shows optimizer spend unchanged for caps ≥1.5% due to diminishing returns binding before cap."
key_equations:
  - equation: "Sales(s) = β0 + Σ_i β_i h(s_i; α_i, γ_i)"
    explanation: Hill saturation function for diminishing returns per channel.
  - equation: "Π(b) = (g - o)(R + ΔR(b)) - Σ_i b_i"
    explanation: Operating profit equals margin on incremental revenue minus marketing spend.
  - equation: "ℙ(B ≤ κ R) ≥ 1 - δ"
    explanation: Chance constraint bounds violation probability for ratio-based caps.
definitions:
  - term: PCE
    definition: Personal Consumption Expenditures
  - term: FRED
    definition: Federal Reserve Economic Data
  - term: SARIMAX
    definition: Seasonal Autoregressive Integrated Moving Average with eXogenous regressors
  - term: VAR
    definition: Vector Autoregression
  - term: SG&A
    definition: Selling, General and Administrative expenses
  - term: FP&A
    definition: Financial Planning and Analysis
  - term: MMM
    definition: Marketing Mix Modeling
  - term: ROI
    definition: Return on Investment
  - term: MAPE
    definition: Mean Absolute Percentage Error
  - term: RMSE
    definition: Root Mean Squared Error
  - term: CFO
    definition: Cash Flow from Operations
critical_citations:
  - "[Box et al., 2015] — Foundational time series forecasting reference."
  - "[Hanssens et al., 2001] — Marketing response and saturation modeling."
  - "[Markowitz, 1952] — Mean-variance optimization for risk-return trade-off."
  - "[Bertsimas & Sim, 2004] — Robust optimization under uncertainty."
  - "[James et al., 2021] — Source of Advertising dataset and regression methods."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Compares SARIMAX, VAR, and gradient boosting for sequential demand forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Evaluates rolling-window forecasting algorithms with explicit accuracy metrics.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Directly addresses FP&A budgeting with constrained resource allocation.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: Provides an optimization framework that outputs recommended budget allocations.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: high
      justification: Solves a constrained portfolio problem with SG&A and cash-flow guardrails.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: medium
      justification: Discusses chance constraints and buffers but does not implement a formal reduction hierarchy.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses rolling backtests and Monte Carlo evaluation to assess forecast and recommendation performance.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Compares forecasting and response models using cross-validation and RMSE/MAPE.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Evaluates budget recommendations via constraint satisfaction rates and profit-risk trade-offs.
  contribution: For Odin's forecasting module (6.A/6.B), the paper provides a comparison of SARIMAX, VAR, and gradient boosting on quarterly time series, demonstrating that multivariate models improve accuracy over seasonal baselines. For the budget recommendation module (7.A/7.B/7.C), the paper offers a constrained optimization framework with explicit accounting constraints (SG&A ratio, cash-flow coverage) and shows that optimal budgets may fall below caps due to diminishing returns and demand uncertainty. For evaluation (12.A/12.B/12.C), the paper's rolling backtest protocol and Monte Carlo constraint-satisfaction analysis provide a template for assessing model performance and recommendation robustness. The paper's use of audited financial statements (Apple 10-K) to calibrate constraints also informs how Odin might incorporate user-specific financial ratios.
  directly_justifies:
    - "Multivariate VAR forecasting improves aggregate demand accuracy over seasonal naïve (≈2.85% vs 6.06% MAPE)."
    - "Marketing response curves exhibit strong diminishing returns; newspaper spend shows near-zero marginal ROI."
    - "Optimal budget may be below a ratio cap because spending at the cap violates constraints under demand uncertainty in ≈40% of scenarios."
    - "A risk-neutral optimizer allocates 25% to TV and 75% to radio under a 1.5% SG&A cap."
    - "Sensitivity to marketing effectiveness shows that higher ROI leads to cap-level spending, reducing SG&A satisfaction to ≈60%."
  limits:
    - "Data sources (PCE, Advertising.csv, Apple 10-K) are not internally consistent; sales-to-revenue normalization is stylized."
    - "Marketing response is treated as contemporaneous; real advertising carryover effects are omitted."
    - "The Advertising dataset is cross-sectional and small (N=200), limiting generalizability of response curves."
    - "Forecast evaluation uses latest-vintage PCE data, which may overstate real-time performance."
    - "Fiscal vs calendar quarter alignment is abstracted away."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The following domains were flagged as relevant: Spending Forecasting (6.A, 6.B) with high relevance because the paper compares four forecasting models (SARIMAX, VAR, gradient boosting) on sequential time series data and reports accuracy; Budget Recommendation (7.A, 7.B, 7.C) with high relevance because the paper directly addresses budget allocation optimization under constraints and evaluates recommended budgets; System Evaluation (12.A, 12.B, 12.C) with medium relevance because the paper uses rolling backtests, cross-validation, and Monte Carlo evaluation to assess models and recommendations. Topic 7.D (Infeasibility Handling) was assigned medium relevance because the paper discusses chance constraints and buffers but does not implement a formal reduction hierarchy. The following domains were considered and rejected: Filipino Cultural Context (2.A-2.D) because the paper is set in a generic corporate FP&A context with no Philippine focus; Expense Categorization (3.A-3.C) because it deals with marketing channels rather than personal expense categories; Behavioral Profiling (5.A-5.C) because no user behavior profiling is present; Mobile-First Design (9.A-9.B) and Data Privacy (10.A-10.B) are absent; Retention (11.A-11.B) is not addressed; Savings and Debt Management (13.A-13.C) is not relevant. Overall, the paper provides high relevance for forecasting and budget optimization modules, and medium relevance for evaluation methodologies.
limitations:
  - "Data sources (PCE, Advertising.csv, Apple 10-K) are not internally consistent; sales-to-revenue normalization is stylized."
  - "Marketing response is treated as contemporaneous; real advertising carryover effects are omitted."
  - "The Advertising dataset is cross-sectional and small (N=200), limiting generalizability of response curves."
  - "Forecast evaluation uses latest-vintage PCE data, which may overstate real-time performance."
  - "Fiscal vs calendar quarter alignment is abstracted away."
remember_this:
  - "num: Multivariate VAR achieves ≈2.85% MAPE for aggregate demand forecasting."
  - "num: Optimal spend is ≈0.97% of revenue, below the 1.5% SG&A cap due to diminishing returns."
  - "num: Spending at the deterministic cap violates SG&A constraints in ≈40% of scenarios under demand uncertainty."
  - "Marketing response curves show radio has highest marginal ROI at low spend, newspaper near-zero."
```
---

## Paper 6: Huang A. et al_summarized.md

**Source File:** `Huang A. et al_summarized.md`

```yaml
paper_id: 10.4018/JGIM.395852
designation: international-algorithm-specific
title: Dynamic Calibration of Decision Thresholds for Financial Anomaly Detection: Verification With Payment Platform Information and Data
authors: Huang, A.; Zhang, X.; Wang, Y.; Tsai, S.; Zhou, P.; Chen, L.
year: 2025
venue: Journal of Global Information Management
odin_topics:
  - 8.A
  - 8.B
  - 8.C
  - 12.B
tldr: Proposes a Temporal-Attention Isolation Forest with Dynamic Calibration that adapts the anomaly decision threshold online and incorporates temporal context to improve fraud detection in payment streams.
problem_and_motivation: Existing Isolation Forest-based fraud detectors rely on static thresholds that fail under shifting transaction distributions, causing high false alarms or missed fraud. Real-world payment streams are non-stationary and require adaptive mechanisms. Prior work lacks a principled, unsupervised approach to threshold calibration and temporal modeling.
approach:
  - Uses a sliding window to segment transaction streams for online processing.
  - Applies a temporal attention encoder to capture short-range dependencies and periodic patterns.
  - Computes anomaly scores using an Isolation Forest ensemble on attended transaction representations.
  - Dynamically calibrates the decision threshold via a quantile-based update smoothed with a learning rate.
  - Optionally incorporates delayed labels to correct thresholds using false positive/negative feedback.
  - Evaluates on five real and synthetic datasets (IEEE-CIS, PaySim, CCFD, SFD-FD, BankSim).
  - Compares against six baselines including Online-iForest, GNN-IF, SSR-RVFL, and XGB-Anomaly.
  - Reports precision, recall, F1, AUC, and per-transaction latency under streaming protocols.
  - Ablates dynamic threshold and attention components to isolate their contributions.
findings:
  - "num: TA-IFDC achieved F1=0.927 and AUC=0.974 on IEEE-CIS, outperforming all baselines."
  - "num: Dynamic threshold calibration improved recall from 0.835 to 0.918 and F1 from 0.852 to 0.927."
  - "num: Under concept drift, TA-IFDC F1 dropped only 0.012 versus 0.085 for Online-iForest and 0.067 for SSR-RVFL."
  - "num: On CCFD minority fraud detection, TA-IFDC attained F1=0.896, surpassing SSR-RVFL (0.857) and XGB-Anomaly (0.764)."
  - "num: Cross-dataset transfer from PaySim to CCFD yielded F1=0.841 and AUC=0.904, the highest among comparators."
  - "num: Inference latency stayed at 29 ms per transaction, within real-time constraints and faster than all deep/hybrid baselines."
  - Removing temporal attention reduced AUC from 0.968 to 0.938 on PaySim, confirming its value.
  - Dynamic calibration maintains stable alert rates during seasonal traffic shifts without manual retuning.
  - Temporal attention helps detect sequences of small anomalies that appear benign in isolation.
key_figures_tables:
  - "Figure 2: Bar charts comparing F1 and latency on IEEE-CIS → TA-IFDC achieves highest F1 (0.927) and second-lowest latency (29 ms)."
  - "Figure 3: Ablation of dynamic threshold on IEEE-CIS → removing it drops recall by 8.3 percentage points, confirming calibration's importance."
  - "Figure 4: ROC curves on PaySim → TA-IFDC with attention (AUC 0.968) clearly outperforms without attention (AUC 0.938)."
  - "Figure 5: F1 before/after concept drift on SFD-FD → TA-IFDC shows the smallest drop (−0.012), demonstrating robustness."
  - "Figure 7: Minority class detection and cross-dataset generalization → TA-IFDC leads in both F1 (0.896) and transfer performance (0.841)."
key_equations:
  - equation: s(z)=2^{-E(h(z))/c(n)}
    explanation: Anomaly score from Isolation Forest; shorter path implies higher anomaly likelihood.
  - equation: θ_k = (1-λ)θ_{k-1} + λ Quantile_β(𝒮_k)
    explanation: Smoothed quantile-based update of the decision threshold using current score distribution.
  - equation: Δθ_k = η (α FP_k/W - (1-α) FN_k/W)
    explanation: Feedback correction term to balance false positives and negatives when labels are available.
definitions:
  - term: IF
    definition: Isolation Forest, an unsupervised anomaly detection algorithm based on random partitioning.
  - term: TA-IFDC
    definition: Temporal-Attention Isolation Forest with Dynamic Calibration, the proposed framework.
  - term: DTC
    definition: Dynamic Threshold Calibration module that adapts the decision boundary online.
  - term: AUC
    definition: Area Under the ROC Curve, a threshold-independent ranking metric.
critical_citations:
  - "[Liu et al., 2008] — Original Isolation Forest algorithm, foundational to the approach."
  - "[Zhang et al., 2022] — Context on fraud losses and the need for adaptive detection."
  - "[Vanini et al., 2023] — Discusses online payment fraud and the shift to risk management."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly presents an anomaly detection framework for financial transactions, applicable to PFMS fraud/overspending detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Proposes and evaluates a specific algorithmic enhancement (adaptive threshold + temporal attention) for transaction anomaly scoring.
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: medium
      justification: Dynamic calibration operates without requiring labels, offering a baseline strategy for new users or data streams with sparse feedback.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Provides extensive experimental evaluation of the proposed algorithm against baselines across multiple datasets and metrics.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: contextual
      justification: Discusses the limitation of static thresholds in prior fraud detectors, which motivates the work, but does not focus on PFMS specifically.
  contribution: "TA-IFDC offers a modular anomaly detection component that can be integrated into Odin's spending monitor to flag irregular transactions. Its dynamic thresholding directly addresses the need for adaptive alerting under changing user behavior and seasonal spending patterns. The temporal attention module enhances detection of sequential fraud patterns, which is valuable for identifying suspicious spending cascades. The framework's unsupervised nature aligns with Odin's goal of working with limited labeled data, and its low latency supports mobile-first real-time feedback. Together, these features make the method a strong candidate for Odin's anomaly detection subsystem."
  directly_justifies:
    - "Adaptive threshold calibration improves recall and reduces false alarms in non-stationary transaction streams."
    - "Incorporating temporal context (attention) captures short-range dependencies and boosts detection of contextual anomalies."
    - "Unsupervised anomaly scoring with online calibration can operate without ground-truth labels, suitable for cold-start scenarios."
    - "Latency below 30 ms per transaction meets real-time processing requirements for mobile payment alerts."
  limits:
    - "Assumes continuous, time-stamped transaction streams with consistent logging; legacy systems may require preprocessing."
    - "Feedback loop relies on delayed labels or model-derived signals; direct expert annotations are not yet incorporated."
    - "Performance may degrade under extreme class imbalance if feedback is very sparse, though fallback quantile adaptation remains stable."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes flagged Anomaly Detection as the primary area of relevance, with high relevance for topics 8.A and 8.B because the paper directly proposes and evaluates a novel anomaly detection algorithm for payment data. Topic 8.C was assigned medium relevance because the dynamic calibration mechanism provides an unsupervised cold-start baseline by adjusting thresholds without requiring labels. Topic 12.B received medium relevance due to the comprehensive algorithmic evaluation methodology. Topic 4.B was considered contextual because the paper notes limitations of static thresholds in existing systems but does not focus on PFMS gaps. Other domains—Expense Categorization, Budget Recommendation, Mobile-First Design, Data Privacy, User Retention, Savings & Debt Management—were rejected as the paper does not address them. The overall relevance to Odin is strong for its anomaly detection module, offering a practical, low-latency approach that can be adapted to personal spending alerts."
limitations:
  - "The method requires transaction timestamps and temporal ordering, which may not be available in all banking APIs. [unacknowledged]"
  - "Feedback calibration uses model-derived signals; incorporating actual user or analyst feedback could further improve adaptability. [unacknowledged]"
  - "Extreme class imbalance (e.g., fraud rates below 0.2%) may require additional safeguards to prevent threshold overcorrection."
  - "The attention mechanism adds some overhead, though latency remains within acceptable bounds."
remember_this:
  - "Dynamic threshold calibration raised recall from 83.5% to 91.8% on IEEE-CIS."
  - "TA-IFDC maintained F1 near 0.91 across varying window sizes with latency under 32 ms."
  - "Under concept drift, TA-IFDC lost only 1.2% F1 versus >8% for static baselines."
  - "Temporal attention increased AUC by 0.03 on PaySim by capturing sequential anomalies."
  - "Cross-dataset transfer achieved F1 0.841, showing good generalization to unseen payment patterns."
```
---

## Paper 7: Pisal et al_summarized.md

**Source File:** `Pisal et al_summarized.md`

```yaml
paper_id: 10.1038/s41598-025-17604-y
designation: international-algorithm-specific
title: An integrated TOPSIS and ARAS method multi-criteria decision-making approach for optimizing investment portfolios using goal programming and genetic algorithm model
authors: Pisal, P.; Reddy, K. K.; Kishore, J.; Jonnalagadda, R. R.; Kumar, M.; Band, G.; Joshi, B. P.
year: 2025
venue: Scientific Reports
odin_topics:
  - 4.A
  - 4.B
  - 5.A
  - 6.A
  - 6.B
  - 7.B
  - 7.C
  - 7.D
  - 8.B
  - 12.A
  - 12.B
  - 12.C
  - 13.A
  - 13.B
tldr: A hybrid framework integrates TOPSIS-ARAS ranking with goal programming and genetic algorithms to optimize investment portfolios, achieving a Sharpe ratio of 2.241 on the FAR-Trans dataset.
problem_and_motivation: Existing portfolio optimization models either rank assets without allocating capital or optimize allocations without integrating investor preferences. This separation leads to suboptimal plans that fail to balance multiple objectives like return, risk, and diversification. A unified framework combining preference modeling with constrained optimization is critically needed.
approach:
  - Data from the FAR-Trans dataset (359,128 transactions, 2018-2022) is preprocessed using min-max scaling and one-hot encoding.
  - A two-layer MCDM framework fuses TOPSIS closeness coefficients and ARAS utility scores via a convex combination to rank assets.
  - A goal programming model encodes investor-specific return targets, risk thresholds, and budget constraints as deviation variables.
  - A genetic algorithm with tournament selection, SBX crossover, and Gaussian mutation explores the feasible space to refine portfolio weights.
  - The framework is benchmarked against Markowitz, NSGA-III, MOPSO, and other state-of-the-art models using Sharpe ratio, ROI, diversification, and budget adherence.
findings:
  - num: The proposed model achieved a Sharpe ratio of 2.241 and an annualized return of 4.6%.
  - num: The diversification score was 0.845 across 79 assets and 13 sectors.
  - num: A 0.729 correlation was found between TOPSIS-ARAS rankings and GP-configured portfolio returns.
  - The GA module converged within 80 generations, demonstrating computational efficiency.
  - Sensitivity analysis showed high rank stability (Kendall's τ > 0.89) across different MCDM fusion weights.
  - Investor segmentation revealed that 59% of transactions were purchases, indicating a bullish accumulation trend.
  - The model maintained a budget deviation of €36.2M while achieving over 30% returns in validation portfolios.
key_figures_tables:
  - Figure 3: Transaction distribution showing 59% purchases → Indicates alignment with stable asset selection.
  - Figure 4: Investor segmentation showing 61% "Mass" customers → Supports capital-based constraint modeling in GP.
  - Figure 9: ROI distribution across Stocks, Bonds, MTFs → Highlights equities achieving outlier returns >80%.
  - Figure 12: Top 10 asset allocations with Financial Services dominating → Reflects high MCDM scores for return-risk profile.
  - Table 4: Performance comparison vs. state-of-the-art → Confirms proposed model's superiority across all metrics.
key_equations:
  - equation: \phi_i = \alpha \cdot C_i^{TOPSIS} + (1-\alpha) \cdot U_i^{ARAS}
    explanation: Convex fusion of TOPSIS and ARAS scores for hybrid ranking.
  - equation: \text{Min} \sum_{j=1}^{n} (d_j^+ + d_j^-)
    explanation: Goal programming objective minimizing deviations from investor targets.
  - equation: \text{Fitness} = \sum x_i r_i - \lambda \left| \sum x_i \sigma_i - \sigma^* \right|
    explanation: GA fitness function balancing return and risk penalty.
definitions:
  - term: TOPSIS
    definition: Technique for Order Preference by Similarity to Ideal Solution, ranks alternatives by geometric distance to ideal and anti-ideal points.
  - term: ARAS
    definition: Additive Ratio Assessment, ranks alternatives using additive normalization and utility scores.
  - term: GP
    definition: Goal Programming, an optimization method that minimizes deviations from multiple, possibly conflicting, objectives.
  - term: GA
    definition: Genetic Algorithm, an evolutionary metaheuristic that iteratively improves solutions via selection, crossover, and mutation.
  - term: MCDM
    definition: Multi-Criteria Decision Making, a set of methods for evaluating alternatives based on multiple conflicting criteria.
  - term: FAR-Trans
    definition: Financial Asset Recommendation Transactions dataset, containing anonymized investor and asset data from a European institution.
critical_citations:
  - "[Vásquez et al., 2021] — AHP-TOPSIS benchmark for stock portfolio investments."
  - "[Anadani et al., 2023] — GA approach for portfolio optimization baseline."
  - "[Mwamba et al., 2025] — NSGA-III application for multi-objective portfolio selection."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Reviews traditional MCDM and optimization systems but not specific PFMS.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Explicitly identifies the gap between preference modeling and allocation optimization.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: low
      justification: Segments investors by risk tolerance but does not define behavioral profiles for PFMS.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: contextual
      justification: Uses historical returns and risk but not predictive spending models.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: Applies GA/GP to asset allocation, not to sequential spending forecasting.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Provides a general optimization framework that could inform budget recommendations.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: high
      justification: Directly presents a GP-GA model for constrained asset allocation.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: low
      justification: Penalty-based handling of risk constraints is mentioned but not a primary focus.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: The method uses deviation minimization, conceptually related to anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: low
      justification: Uses Sharpe ratio and ROI for evaluation, not PFMS-specific metrics.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Ablation study and comparative baselines validate each module's contribution.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: low
      justification: Evaluation is for investment portfolios, not budget recommendation systems.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: contextual
      justification: Return maximization could relate to savings growth but is not the core focus.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: low
      justification: Does not address debt; focuses on asset allocation for return.
  contribution: The paper provides a validated, modular framework for multi-objective portfolio optimization that can inform Odin's budget allocation and optimization modules. Its dual MCDM ranking (TOPSIS-ARAS) offers a stable asset pre-selection method that could be adapted for expense category prioritization. The GP-GA hybrid demonstrates how investor-specific constraints (return, risk, budget) can be encoded into a solvable optimization problem, relevant to Odin's budget recommendation engine. The ablation study and sensitivity analysis offer best practices for evaluating algorithmic modules and handling parameter uncertainty.
  directly_justifies:
    - "A hybrid MCDM-GP-GA framework can effectively balance multiple financial objectives with investor constraints."
    - "Integrating TOPSIS and ARAS via convex fusion reduces ranking sensitivity and stabilizes asset selection."
    - "Genetic algorithms are computationally feasible for portfolio optimization with early convergence under 100 generations."
    - "Sensitivity analysis with Kendall's τ can validate the robustness of ranking systems against parameter changes."
  limits:
    - "The model assumes single-period static optimization, which limits adaptability to dynamic market conditions."
    - "Computational time scales with portfolio size, requiring optimization for high-frequency use cases."
    - "Investor constraints are modeled as linear goals, ignoring fuzzy or utility-based preferences."
    - "Regulatory constraints, transaction costs, and tax implications are not included."
  mapping_rationale: A systematic scan across all 12 functional domains revealed that this paper most directly informs the System Evaluation domain (12.A, 12.B, 12.C) through its comprehensive evaluation framework. It also provides strong methodological insights for Budget Recommendation via Constrained Optimization (7.C) with its GP-GA model. The paper's explicit discussion of the gap between preference modeling and allocation (4.B) offers supporting evidence for the limitations of existing personal finance systems. Topics related to Behavioral Profiling (5.A) and Forecasting (6.A, 6.B) were flagged with low or contextual relevance because the paper uses general investor risk profiles and historical returns, not the specific Filipino behavioral or spending patterns relevant to Odin. The domains of Filipino Cultural Context (2.A-D) and Mobile-First Design (9.A-B) were considered and rejected as they are not addressed. Data Privacy (10.A-B) and User Retention (11.A-B) were also not within the paper's scope. The paper's overall relevance to Odin is medium, as it offers a robust, validated methodological template for building an optimization engine, but requires significant adaptation to the PFMS context.
limitations:
  - The model assumes single-period static optimization, not dynamic market conditions or multi-period planning. [unacknowledged]
  - Genetic algorithm convergence time may become a bottleneck for high-frequency portfolio recommendations.
  - The framework uses linear investor goals, but real-world preferences are often fuzzy or utility-based. [unacknowledged]
  - Regulatory constraints, transaction costs, and tax considerations are absent from the model. [unacknowledged]
  - The model's interpretability is enhanced by visualizations but lacks formal XAI modules like SHAP or LIME. [unacknowledged]
remember_this:
  - Hybrid MCDM-GP-GA achieved a Sharpe ratio of 2.241 and ROI of 4.6%.
  - Dual TOPSIS-ARAS ranking via convex fusion enhances asset selection stability.
  - GP encodes investor-specific return, risk, and budget constraints as deviations.
  - GA optimization converged within 80 generations with a population size of 100.
  - The framework outperformed NSGA-III and MOPSO across all key portfolio metrics.
```
---

## Paper 8: Pretnar et al_summarized.md

**Source File:** `Pretnar et al_summarized.md`

```yaml
paper_id: 10.21203/rs.3.rs-7730348/v1
designation: international-algorithm-specific
title: Mental Accounting Through Two-stage Budgeting Under Bounded Rationality
authors: Pretnar, N.; Olivola, C. Y.; Montgomery, A.
year: 2025
venue: Research Square
odin_topics:
  - 3.A
  - 5.A
  - 6.A
  - 7.A
  - 7.C
  - 8.A
  - 10.B
tldr: A structural model generalizes two-stage budgeting with cognitive frictions to quantify mental accounting behavior from expenditure data alone.
problem_and_motivation: Classical two-stage budgeting assumes perfect fungibility and ex-post budget adherence, yet consumers exhibit mental accounting and sticky budgets due to cognitive costs. There is a lack of empirical, agent-level quantification of how bounded rationality manifests in budgeting. This gap prevents the design of effective financial interventions that account for heterogeneous consumer decision-making.
approach:
  - Proposes a dynamic, two-stage budgeting model where a planner sets ex-ante budgets subject to cognitive constraints and a doer realizes expenditure shocks.
  - Incorporates narrow choice bracketing via probabilistic budget re-evaluation (ψ) and numeracy constraints that prevent trivial budget changes.
  - Mental accounting is captured by a state variable (over/under-spending from prior periods) that influences future budget adjustments via a parameter γ.
  - Estimates the structural model using a hierarchical MH-within-Gibbs MCMC algorithm on weekly expenditure data from 2,509 low-income prepaid debit card users.
  - Compares model variants with absolute ($1) and relative (%) numeracy thresholds, and tests counterfactuals by fully relaxing cognitive constraints.
findings:
  - num: 80% of consumer-week combinations exhibit bounded rationality, with an average of 2.11 budget updates per week under the $1-threshold model.
  - num: A $1 numeracy threshold reduces budget updates by 14.9%, while relative thresholds of 1%, 5%, and 10% reduce updates by 41.8%, 64%, and 70% respectively.
  - Ex-ante budgeting behavior is largely consistent with mental accounting (78.7% are budget prioritizers), but ex-post spending behavior is mixed, with 46.8% classified as spendthrifts.
  - num: 22.3% of consumers are ex-ante budget prioritizers but ex-post habitual over-spenders (type ii), exhibiting a "planning fallacy" pattern after over-spending.
  - Counterfactual relaxation of cognitive constraints makes 68.4% of consumers worse off, and 3.3% go bankrupt under the $1-threshold model.
  - num: Consumers who go bankrupt when constraints are relaxed have significantly lower estimated updates (1.25/week) and are more likely to be ex-ante type (i) but ex-post type (ii).
key_figures_tables:
  - "Table 1: Summary statistics of agent-level means → Shows low-income sample (median weekly income $460) with substantial spending variation."
  - "Table 2: Posterior summary statistics for baseline and $1-threshold models → Reports estimated means and standard deviations for all key behavioral parameters."
  - "Table 3: Marginal distributions of ex-ante and ex-post types → Ex-ante most are budget prioritizers, ex-post plurality are spendthrifts."
  - "Table 4: Joint distributions of ex-ante and ex-post types → Reveals 37.5% are budget prioritizers ex-ante but spendthrifts ex-post."
  - "Figure 2: Time series of actual vs. predicted spending → Demonstrates the model's fit for a median-income agent across categories."
  - "Figure 3: Posterior density of budget updates per week → Shows distribution of k under different numeracy thresholds."
  - "Figure 4: Density of k conditional on counterfactual type → Bankrupt consumers have significantly fewer budget updates."
key_equations:
  - equation: $x_{ijt} = \omega_{ijt} + \zeta_{ijt}$
    explanation: Doer's expenditure is budget plus shock.
  - equation: $a_{ijt} = \omega_{ij,t-1} - x_{ij,t-1} = -\zeta_{ij,t-1}$
    explanation: Mental account balance equals negative prior shock.
  - equation: $\omega_{ijt} = \theta_{ijt} \ell_{it} + \gamma_i a_{ijt}$
    explanation: Budget is income share plus anchored mental account.
  - equation: $\Gamma_{ijt} \sim \text{Bernoulli}(\psi_{ij})$
    explanation: Probability of re-evaluating a specific budget.
  - equation: $\vartheta_{iyt}^* = \frac{\alpha_{i,\iota_{iyt}} \ell_{it} - \alpha_{i,\iota_{iyt}} \sum_{s<y} \ell_{it} \theta_{i,\iota_{ist},t} + \gamma_i a_{i,\iota_{iyt},t} + \zeta_{i,\iota_{iyt},t}}{\ell_{it}(\alpha_{i,\iota_{iyt}} + \alpha_{i,J+1})} \dots$
    explanation: Analytical expression for optimal candidate budget share.
definitions:
  - term: Mental Accounting
    definition: A book-keeping mechanism where past over/under-spending informs future budgets.
  - term: Narrow Choice Bracketing
    definition: Consumers re-evaluate only a subset of budgets per period due to cognitive constraints.
  - term: Numeracy Constraint
    definition: A threshold (absolute or relative) that a budget change must exceed to be implemented.
  - term: Budget Prioritizer
    definition: Consumer type that reduces budget after over-spending and increases after under-spending.
  - term: Spendthrift
    definition: Consumer type that increases spending regardless of prior over or under-spending.
critical_citations:
  - "[Thaler, 1985] — Foundational theory of mental accounting."
  - "[Deaton and Muellbauer, 1980] — Classical two-stage budgeting framework."
  - "[Shefrin and Thaler, 1981] — Planner/doer model of self-control."
  - "[Gabaix, 2014] — Sparse maximization and bounded rationality."
  - "[Kőszegi and Matějka, 2020] — Mental budgeting with attention costs."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: The model operationalizes budget categories and estimates category-specific expenditure shares.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Empirically classifies consumers into ex-ante and ex-post behavioral types (budget prioritizers, spendthrifts).
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Develops a structural forecasting model for spending based on budgets, mental accounts, and shocks.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Models the strategic process of setting and updating budgets under cognitive frictions.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: high
      justification: Formulates budget selection as a constrained optimization problem with cognitive and numeracy constraints.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Expenditure shocks (ζ) are modeled as deviations from budgets, which is foundational for anomaly detection.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: contextual
      justification: Counterfactual analysis shows that nudging via apps can harm certain users, affecting trust.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: low
      justification: The model captures spending spikes and trends but does not focus on seasonality.
  contribution: "The paper provides a structurally estimated model for inferring latent budgeting behavior from expenditure data, which can be used to enhance Odin's spending forecasting module (6.A) by incorporating cognitive constraints. It offers a methodology for dynamically classifying users into behavioral profiles (5.A) based on their budget-updating and spending responses, enabling adaptive budgeting strategies. The counterfactual analysis reveals critical insights for Odin's nudging features (11.A): increasing attentiveness can have adverse effects for some users, implying that interventions should be personalized and cautious. The model's framework for budget updating and mental accounting directly informs the design of Odin's budget recommendation (7.B) and anomaly detection (8.A) algorithms, providing a theoretical basis for handling infeasibility and user inertia. Finally, the identification of distinct consumer types (e.g., budget prioritizers vs. spendthrifts) supports the development of tailored financial advice and savings/debt management strategies (13.A, 13.B)."
  directly_justifies:
    - "Budget updates occur for approximately half of consumption categories each period, supporting a sparse-max approach for Odin's budget recommendation."
    - "A $1 numeracy threshold is a better fit than no threshold, justifying the inclusion of an 'inertia' parameter in Odin's budget adjustment logic."
    - "Relaxing cognitive constraints makes 68% of consumers worse off, suggesting Odin should avoid over-nudging and prioritize user autonomy."
    - "Ex-ante budgeting behavior is distinct from ex-post spending, indicating Odin should track both planned budgets and actual expenditure separately."
    - "Consumers who are ex-ante budget prioritizers but ex-post spendthrifts are most vulnerable to adverse outcomes, requiring targeted support."
  limits:
    - "Results are model-dependent and rely on unobserved latent variables, limiting the certainty of individual-type classifications."
    - "Data is from low-income, underbanked prepaid card users in North America, which may not generalize to Filipino young professionals."
    - "Assumes strong separability of utility, which may oversimplify substitution patterns across broad expenditure categories."
    - "Does not explicitly model price variation, aggregating prices into indices, which may miss important consumption adjustments."
  mapping_rationale: "A systematic scan across all 12 functional domains was conducted. The paper's core theoretical and empirical contributions on modeling bounded rationality in budgeting directly map to high relevance for domains: Expense Categorization (3.A, 3.B), Behavioral Profiling (5.A, 5.B, 5.C), Spending Forecasting (6.A, 6.B), and Budget Recommendation (7.A, 7.B, 7.C, 7.D). The structural estimation approach and consumer typing also offer medium relevance to Anomaly Detection (8.A) and System Evaluation (12.A, 12.B, 12.C). The counterfactual simulations on attentiveness inform Engagement & Retention (11.A) and Data Privacy/Trust (10.B), albeit with contextual or low relevance as the paper does not directly study app design or trust. Topics like Filipino Cultural Context (2.A, 2.B, 2.C) and Savings/Debt (13.A, 13.B) were considered but rejected as the paper's empirical setting is North American and its primary contribution is methodological, though findings on overspending cycles are tangentially relevant to debt management. Borderline cases included the mental accounting state variable (a), which relates to both expense categorization (3.A) and behavioral profiles (5.A); it was assigned to 5.A for its role in defining consumer types. The paper's overall relevance to Odin is high, providing a quantitative, micro-founded framework for modeling key user behaviors that directly informs the design of adaptive and personalized financial management features."
limitations:
  - "Findings are based on a model-dependent estimation of latent budgets, not directly observed." [unacknowledged]
  - "The dataset is from a specific low-income, underbanked population in North America; applicability to other demographics (e.g., Filipino YPs) is not tested." [acknowledged]
  - "Assumes strong separability in utility, which may not capture complex category interactions."
  - "The model does not incorporate explicit price effects, relying on aggregated price indices." [acknowledged]
  - "Counterfactual simulations of 'full rationality' may not reflect real-world behavioral changes from app nudges."
remember_this:
  - "Consumers update only about half their budgets per week, showing bounded rationality."
  - "Most consumers are budget prioritizers ex-ante but spendthrifts ex-post."
  - "Relaxing cognitive constraints makes 68% of consumers worse off."
  - "3.3% of consumers go bankrupt if all budgets are updated weekly."
  - "Sticky budgets can serve as a disciplinary tool for vulnerable consumers."
```
---

## Paper 9: Kalideen_summarized.md

**Source File:** `Kalideen_summarized.md`

```yaml
paper_id: "5b6d4f4e-8f0f-5b1e-9e5a-1c7f8f3f5f5a"
designation: "international-algorithm-specific"
title: "Detection of Fraudulent Transaction Issues in the Payment Card Industry using Machine Learning: A Comprehensive Survey"
authors: "Kalideen, M. R."
year: 2025
venue: "Journal of Information and Communication Technology"
odin_topics:
  - "4.A"
  - "4.B"
  - "5.A"
  - "5.B"
  - "5.C"
  - "8.A"
  - "8.B"
  - "8.C"
  - "10.A"
  - "10.B"
  - "12.A"
  - "12.B"
  - "12.C"
tldr: "A comprehensive survey of machine learning and deep learning techniques for payment card fraud detection, addressing challenges like imbalanced data and model interpretability, and exploring emerging trends such as explainable AI and privacy-preserving methods."
problem_and_motivation: "The rapid growth of digital payment card transactions has been paralleled by a surge in fraudulent activities, posing significant challenges to the financial industry. Traditional rule-based fraud detection methods are often static and inflexible, struggling to adapt to the ever-evolving tactics of fraudsters. There is a critical need for more advanced, adaptable, and accurate solutions like machine learning to safeguard financial systems."
approach:
  - "A systematic literature search was conducted in IEEE Xplore, Scopus, and PubMed using keywords related to credit card fraud, machine learning, and anomaly detection."
  - "The search was limited to English-language studies published between 2010 and 2024, with 49 studies meeting the final inclusion criteria after screening."
  - "The review covers a diverse array of algorithms including supervised, unsupervised, and hybrid learning methods, as well as deep learning architectures like DNNs, RNNs, Autoencoders, and GANs."
  - "Strengths and limitations of models are discussed in the context of challenges like imbalanced datasets, model interpretability, scalability, and security."
  - "Emerging trends such as explainable AI (XAI), privacy-preserving machine learning, and blockchain technology are also examined."
findings:
  - "num: Fraudulent transactions typically make up less than 1% of all transactions, leading to severe class imbalance."
  - "Deep learning models have exhibited exceptional performance in fraud detection, often outperforming conventional methods."
  - "Imbalanced datasets cause models to be biased toward the majority class, resulting in low recall for fraudulent transactions."
  - "Model interpretability is a major challenge for deep learning, as they function as 'black boxes,' hindering trust and regulatory compliance."
  - "Explainable AI is crucial for transparency, helping to build trust, meet regulatory requirements, and improve model accuracy."
  - "Privacy-preserving machine learning techniques are becoming critical to address privacy concerns and ensure compliance with laws like GDPR."
  - "Ensemble methods are particularly effective, offering higher overall accuracy, robustness to noise, and better generalization."
  - "Adversarial attacks pose a significant threat, where small changes to input data can lead to model misclassification."
  - "Federated learning allows for collaborative model training across institutions without sharing raw data, preserving privacy."
  - "The review provides actionable recommendations for practitioners and identifies promising future research directions."
key_figures_tables:
  - "Table I: Traditional Fraud Detection vs. Machine Learning in Fraud Detection → Compares adaptability, accuracy, and scalability of approaches."
  - "Table II: Widely Used Supervised Learning Algorithms for Fraud Detection → Summarizes logistic regression, SVM, decision trees, random forests, and neural networks."
  - "Table III: Deep Learning Techniques Used in Fraud Detection → Outlines DNN, RNN, Autoencoders, and GANs with their applications."
  - "Table IV: Ensemble Methods Used in Fraud Detection → Describes bagging, boosting, random forests, and stacking."
  - "Table V: Comparison of Machine Learning Techniques Used in Fraud Detection → Contrasts supervised, unsupervised, semi-supervised/hybrid, deep learning, and ensemble methods."
  - "Table VI: Comparison of Different Evaluation Metrics Used in Machine Learning → Analyzes accuracy, precision, recall, F1-score, AUC-ROC, and average precision."
key_equations:
  - equation: "Precision = True Positives / (True Positives + False Positives)"
    explanation: "Measures accuracy of positive predictions."
  - equation: "Recall = True Positives / (True Positives + False Negatives)"
    explanation: "Measures ability to find all positive instances."
  - equation: "F1-Score = 2 * (Precision * Recall) / (Precision + Recall)"
    explanation: "Harmonic mean of precision and recall."
definitions:
  - term: "XAI"
    definition: "Explainable Artificial Intelligence, a set of processes and methods that allows human users to understand and trust the results and output created by machine learning algorithms."
  - term: "PPML"
    definition: "Privacy-Preserving Machine Learning, techniques to train models on sensitive data without compromising individual privacy."
  - term: "GAN"
    definition: "Generative Adversarial Network, a class of machine learning frameworks where two neural networks contest with each other to generate new, synthetic instances of data."
  - term: "AUC-ROC"
    definition: "Area Under the Receiver Operating Characteristic curve, a performance metric that summarizes the trade-off between true positive and false positive rates."
critical_citations:
  - "[Yundong, 2023] — Foundational overview of logistic regression and random forest for fraud detection."
  - "[Kumar & Dwivedi, 2020] — Key study on unsupervised learning for fraud detection."
  - "[Rudin, 2019] — Seminal paper arguing for interpretable models over black boxes for high-stakes decisions."
  - "[Phua et al., 2010] — Comprehensive early survey on data mining-based fraud detection research."
relevance:
  topics:
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Provides context for traditional fraud detection methods within existing financial systems."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Explicitly details the limitations of traditional rule-based systems and the need for machine learning."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Discusses how ML models learn spending patterns to identify anomalies, which relates to behavioral profiling."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "low"
      justification: "Mentions the challenge of imbalanced datasets but not directly the cold-start problem for new users."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "Reviews supervised and unsupervised classification algorithms for fraud, which parallel profile classification."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "The core topic is anomaly detection for fraudulent transactions in payment systems."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Provides a comprehensive survey and comparison of various algorithms, including deep learning and ensembles."
    - code: "8.C"
      name: "Cold‑Start Baseline Strategies for Anomaly Detection"
      relevance: "low"
      justification: "Discusses imbalanced data but not specifically cold-start baseline strategies."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses privacy concerns and adversarial attacks, which are key to security."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "medium"
      justification: "Highlights the importance of model interpretability for building trust."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses evaluation metrics like precision, recall, F1-score, and AUC-ROC."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Compares the performance of different ML algorithms for fraud detection."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "contextual"
      justification: "Relevant to evaluation methodologies in general, though not specific to budget recommendation."
  contribution: "This survey provides a comprehensive review of machine learning techniques for fraud detection, which is directly applicable to Odin's anomaly detection module. The analysis of algorithm strengths and weaknesses informs the selection of techniques for identifying irregular spending. The discussion on evaluation metrics is crucial for assessing Odin's detection performance. The exploration of privacy-preserving methods guides the design of secure and trustworthy financial systems."
  directly_justifies:
    - "Machine learning can learn intricate patterns and relationships from extensive datasets to identify subtle indicators of fraud."
    - "Ensemble methods like Random Forest and XGBoost are inherently better suited for handling imbalanced datasets."
    - "Explainable AI (XAI) is crucial for transparency and building user trust in automated financial decisions."
    - "Federated learning enables collaborative model training without compromising customer privacy."
    - "Adversarial attacks pose a significant threat to machine learning models in finance."
  limits:
    - "The survey does not provide empirical results or benchmark specific algorithms on a common dataset."
    - "The specific details of the datasets used in the reviewed studies are often not provided due to privacy concerns."
    - "The review is limited to studies published up to 2024, potentially missing very recent developments."
    - "The paper focuses on payment card fraud and may not be directly transferable to other types of personal finance anomalies."
  mapping_rationale: "A systematic scan across all 12 functional domains was performed. The domains 'Anomaly Detection' and 'Existing Systems & Gaps' were flagged as highly relevant because the paper directly addresses machine learning for fraud detection and critiques traditional methods. Domains like 'Behavioral Profiling & Classification', 'Data Privacy & User Trust', and 'System Evaluation' were deemed medium relevance, as the paper discusses classification approaches, privacy (PPML), trust (XAI), and performance metrics. The 'Savings & Debt Management' and 'Budget Recommendation' domains were considered not applicable. Borderline cases included the discussion of spending patterns for anomaly detection, which was mapped to 5.A, while topics like 2.D were rejected because the analysis is not culturally specific to the Philippines. The overall relevance to Odin is high for the anomaly detection module and offers supporting insights for privacy, trust, and evaluation."
limitations:
  - "Relies on secondary sources (surveys) rather than primary experimental data. [unacknowledged]"
  - "Findings are based on general international literature and may not fully reflect the Filipino context."
  - "The survey does not propose a novel algorithm or system."
remember_this:
  - "Fraudulent transactions comprise less than 1% of all transactions."
  - "Deep learning models offer superior accuracy but suffer from a lack of interpretability."
  - "Explainable AI is essential for building trust in automated financial systems."
  - "Federated learning offers a path to privacy-preserving collaborative model training."
  - "Ensemble methods like Random Forest are robust and handle imbalanced data well."
```
---

## Paper 10: Patra et al_summarized.md

**Source File:** `Patra et al_summarized.md`

```yaml
paper_id: 10.71443/er.ar16
designation: international-algorithm-specific
title: AI-Driven Goal Based Financial Planning System: A Framework for Contextual Feasibility Validation
authors: Patra, B.; Sarkar, S.; Pal, S.; Ghosh, S.; Datta, S.
year: 2025
venue: Engineering Research
odin_topics:
  - 3.A
  - 5.A
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 7.C
  - 7.D
  - 8.A
  - 13.A
  - 13.B
  - 13.C
tldr: An AI framework integrates predictive modeling, reinforcement learning, and Monte Carlo simulation to validate the feasibility of achieving personal financial goals under uncertainty.
problem_and_motivation: Conventional financial planning relies on static assumptions and fails to adapt to dynamic economic conditions and individual behavioral factors. A gap exists in integrating real-time data, adaptive decision-making, and probabilistic feasibility validation into a single goal-oriented system.
approach:
  - Financial factors, including income, expenditure, savings, risk, and market dynamics, are modeled as a multi-dimensional vector for holistic analysis.
  - Time-series forecasting using LSTM networks predicts future income, expenses, and savings from historical data.
  - A reinforcement learning agent optimizes investment allocation strategies by interacting with financial simulations and receiving rewards for goal progress.
  - Monte Carlo simulations generate probabilistic distributions of future wealth by varying return rates and economic parameters.
  - The framework comprises data, AI, and decision layers, enabling modularity and real-time updates based on new data.
  - Feasibility of goals is computed as the proportion of simulated scenarios where final wealth exceeds a target.
findings:
  - The proposed AI system increases forecasting accuracy, adaptability, and goal feasibility evaluations compared to traditional rule-based approaches.
  - num: The integration of contextual awareness significantly enhances the system's performance in providing personalized financial plans.
  - Reinforcement learning enables dynamic strategy adaptation, improving decision-making in response to changing financial circumstances.
  - Incorporating behavioral factors (e.g., risk tolerance) and macroeconomic data leads to more realistic and relevant financial advice.
  - The framework provides quantitative feasibility scores and actionable recommendations, supporting informed financial decision-making.
key_figures_tables:
  - Figure 2: Monthly income-expense dynamics → Highlights cash flow variability, crucial for time-series modeling.
  - Figure 3: Monthly savings variability → Savings fluctuate significantly, including deficits, impacting goal feasibility.
  - Figure 6: Income distribution → Income is not stable, supporting the need for probabilistic forecasting.
  - Figure 7: Risk score distribution → Risk tolerance is dynamic, requiring adaptive behavioral profiling.
  - Table 1: Monthly income and expense data → Quantifies the variability used for LSTM forecasting and simulation.
key_equations:
  - equation: S_t = I_t - E_t - C_t
    explanation: Savings model adjusted for contextual factors like inflation.
  - equation: X_t = [I_t, E_t, S_t, R_t, B_t, M_t]
    explanation: Financial state as a vector for machine learning models.
  - equation: W_{t+1} = W_t + S_t + A_t * r_t
    explanation: Wealth evolution from savings and investment returns.
  - equation: P(G) = (1/N) * sum_{i=1}^N I(W_T^(i) >= G)
    explanation: Probability of achieving a financial goal via simulation.
definitions:
  - term: LSTM
    definition: Long Short-Term Memory network for time-series forecasting.
  - term: Reinforcement Learning
    definition: A method for adaptive decision-making through reward-based learning.
  - term: Monte Carlo Simulation
    definition: A technique to model uncertainty by generating multiple random scenarios.
  - term: Feasibility Score
    definition: A probabilistic measure of the likelihood of achieving a financial goal.
critical_citations:
  - "[Kahneman and Tversky, 1979] — Basis for behavioral biases in finance."
  - "[Hochreiter and Schmidhuber, 1997] — Introduced LSTM for temporal data."
  - "[Markowitz, 1952] — Foundation for Modern Portfolio Theory."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Provides empirical expense distribution data (Figure 8, Table 4) relevant for categorization.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly models risk tolerance and behavioral factors as input variables.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Proposes LSTM-based forecasting for income and expenses.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Uses LSTM specifically for time-series forecasting of financial data.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Offers a goal-based planning framework that informs budgeting decisions.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Generates recommendations on savings, investment, and goal timelines.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: medium
      justification: Uses reinforcement learning for optimization under user constraints.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: high
      justification: Core focus on feasibility validation and providing corrective recommendations.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Mentions risk assessment but not explicit anomaly detection algorithms.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: Explicitly models savings and evaluates goal achievement probabilities.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: low
      justification: Briefly mentions liabilities but focuses more on savings and investments.
    - code: 13.C
      name: End-of-Period Surplus as a Savings Input
      relevance: high
      justification: Uses surplus (savings) as the primary driver for wealth accumulation and feasibility.
  contribution: The paper directly justifies Odin's goal-based financial planning module by providing a framework for feasibility validation. Its approach to using LSTM for forecasting supports Odin's predictive analytics component. The reinforcement learning method for investment allocation can inform Odin's budget recommendation and optimization algorithms. The Monte Carlo simulation for scenario analysis provides a methodology for Odin's feasibility assessment and risk evaluation. The emphasis on integrating behavioral factors validates Odin's need for behavioral profiling within its system.
  directly_justifies:
    - Dynamic financial planning requires AI-driven models for forecasting and adaptation.
    - Feasibility validation should be probabilistic, using simulation to handle uncertainty.
    - Incorporating behavioral factors and risk tolerance is essential for personalization.
    - Reinforcement learning can optimize financial strategies by learning from dynamic environments.
    - A layered, modular architecture is suitable for building intelligent and scalable PFMS.
  limits:
    - The empirical evaluation is limited to a small, illustrative dataset rather than a large-scale real-world user base.
    - The paper does not provide a detailed comparative analysis against state-of-the-art baseline algorithms.
    - The framework's practical deployment aspects, such as latency and data privacy, are not addressed. [unacknowledged]
  mapping_rationale: A systematic scan of all 12 functional domains was conducted. Domains 6 (Spending Forecasting), 7 (Budget Recommendation), and 13 (Savings & Debt Management) were flagged with high relevance due to the paper's core contribution on feasibility validation and goal-based planning. Domain 5 (Behavioral Profiling) was assessed as medium relevance because risk tolerance is modeled as a key variable. Domain 3 (Expense Categorization) was marked medium due to the presentation of expense distribution data. Domain 8 (Anomaly Detection) was considered contextual as the paper discusses risk but not explicit anomaly detection. Domains 1 (Filipino Context), 2 (Cultural Practices), 4 (Existing Systems), 9 (Mobile-First), 10 (Data Privacy), 11 (Retention), and 12 (Evaluation) were rejected as they are not the subject of the paper. The overall relevance is high, providing a methodological foundation for Odin's algorithmic modules.
limitations:
  - The empirical validation uses a limited synthetic dataset, not real-world user data.
  - The paper does not discuss the computational cost or scalability of the integrated AI models.
  - Integration with existing mobile or web-based applications is not explored. [unacknowledged]
  - Data privacy and security concerns in a real fintech deployment are not addressed. [unacknowledged]
remember_this:
  - Integrating predictive, adaptive, and probabilistic models enhances financial planning realism.
  - Feasibility validation via Monte Carlo simulation provides quantitative goal success probabilities.
  - LSTM forecasting captures non-linear patterns in income and expense data.
  - Dynamic risk profiling is essential for tailoring investment strategies effectively.
  - num: The proposed system outperforms traditional rule-based approaches in accuracy and adaptability.
```
---

## Paper 11: Pahuja_summarized.md

**Source File:** `Pahuja_summarized.md`

```yaml
paper_id: 10.5281/zenodo.16628566
designation: international-algorithm-specific
title: "AI: Proactive Workforce and Financial Guardians – Transforming Enterprise Systems from Reactive to Predictive"
authors: "Pahuja, H."
year: 2025
venue: "Sarcouncil Journal of Engineering and Computer Sciences"
odin_topics:
  - "4.A"
  - "4.B"
  - "5.A"
  - "6.A"
  - "6.B"
  - "7.B"
  - "8.A"
  - "9.A"
  - "10.A"
  - "11.A"
  - "12.A"
tldr: "Proposes an architectural framework using Generative AI, NLP, and agentic AI to transform reactive enterprise HR and financial systems into predictive, human-centered platforms."
problem_and_motivation: "Traditional HCM and FinTech platforms operate in silos, provide retrospective insights, and require manual intervention for routine tasks. This fragmentation creates friction in employee experiences and impedes effective financial decision-making."
approach:
  - "Qualitative analysis of enterprise AI implementations across industries, assessing performance metrics and integration patterns with legacy systems."
  - "Proposes multi-layered architecture for digital HR assistants with front-end conversation management, intent recognition middleware, and backend HRIS integrations."
  - "Recommends reinforcement learning-based micro-savings automation that adapts to changing financial situations, optimizing savings timing and amount."
  - "Advocates for distributed microservice architectures with redundant processing for always-on financial monitoring and intervention."
  - "Outlines integration strategies including API-based, event-driven, data virtualization, and hybrid platforms for enterprise financial systems."
  - "Emphasizes MLOps practices, Centers of Excellence, and cloud-native implementations for scalable AI deployment."
  - "Recommends phased deployment models with initial high-value use cases, followed by comprehensive capability expansion."
  - "Proposes multidimensional ROI frameworks capturing direct efficiency gains and indirect organizational benefits."
  - "Advocates for proactive technical debt management including model drift detection and data quality monitoring."
  - "Emphasizes structured change management addressing both rational and emotional aspects of AI adoption."
findings:
  - "Organizations implementing AI-driven workforce planning benefit from enhanced decision-making through advanced topic modeling."
  - "num: Digital HR assistants significantly reduce response times for employee inquiries compared to traditional ticketing systems."
  - "Reinforcement learning-based approaches to micro-savings generate more accumulated savings than fixed percentage transfers or standard round-up mechanisms."
  - "Proactive interventions from continuous financial monitoring substantially reduce overdraft incidents and late payment penalties."
  - "Organizations following structured implementation methodologies report higher success rates compared to ad-hoc approaches."
  - "Phased deployment models significantly outperform all-at-once approaches across adoption rates, user satisfaction, and technical stability metrics."
  - "Effective privacy-preserving architectures employ data minimization, pseudonymization, and differential privacy to maintain employee confidentiality."
  - "Successful enterprise AI deployments typically begin with focused high-value use cases before expanding to comprehensive capabilities."
  - "Proactive technical debt management practices demonstrate greater success in maintaining system performance and reliability during scaling."
  - "AI-powered HR assistants report substantial reductions in query resolution times and corresponding decreases in administrative costs."
key_figures_tables:
  - "Figure 1: Multi-layered architecture of digital HR assistants → Shows interaction between conversational interfaces, intent recognition, and backend HR system integrations."
  - "Figure 2: Conceptual framework for AI Financial Co-Pilots → Illustrates predictive analytics, micro-savings automation, and continuous monitoring for financial guardianship."
  - "Figure 3: Comprehensive implementation roadmap → Emphasizes iterative phases, continuous ROI analysis, and integrated change management strategies."
  - "Table 1: Key Considerations for AI-Powered Enterprise Architecture → Summarizes infrastructure, resource management, governance, MLOps, security, integration, and performance tuning."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "HCM"
    definition: "Human Capital Management"
  - term: "FinTech"
    definition: "Financial Technology"
  - term: "NLP"
    definition: "Natural Language Processing"
  - term: "MLOps"
    definition: "Machine Learning Operations"
  - term: "CoE"
    definition: "Center of Excellence"
critical_citations:
  - "[Venugopal et al., 2024] — Demonstrates AI topic modeling for workforce planning."
  - "[Ramamoorthy, 2025] — Addresses AI infrastructure for large-scale financial systems."
  - "[Votto et al., 2021] — Systematic review of AI in tactical HR management."
  - "[Pandey & Awasthi, 2025] — Shows reinforcement learning for personalized financial wellness."
  - "[Abikoye et al., 2024] — Covers real-time financial monitoring systems."
relevance:
  topics:
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Discusses limitations of traditional financial platforms."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Identifies fragmentation and lack of predictive analytics in current systems."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "low"
      justification: "Mentions behavioral economics in micro-savings but not explicit profiling."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Directly addresses predictive analytics frameworks for financial forecasting."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Discusses deep learning and ensemble methods for time-series financial data."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Covers personalized financial recommendations via reinforcement learning."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "contextual"
      justification: "Mentions anomaly detection in sentiment analysis but not financial anomalies."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "low"
      justification: "Implicit in 'always-on' but not explicitly addressed."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses privacy-preserving architectures and data governance."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "low"
      justification: "Mentions engagement with AI recommendations but not dynamics."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Proposes multidimensional ROI frameworks for AI systems."
  contribution: "Provides a conceptual blueprint for AI-powered HR and financial systems relevant to Odin's predictive modules. Its discussion of predictive analytics and reinforcement learning directly informs Odin's forecasting and budget recommendation components. The emphasis on microservice architectures and continuous monitoring supports Odin's anomaly detection and real-time financial oversight. The paper's analysis of privacy-preserving architectures directly applies to Odin's data privacy module. Its ROI frameworks and implementation roadmaps offer a methodological basis for evaluating Odin's system components."
  directly_justifies:
    - "Predictive analytics frameworks enable evidence-based financial forecasting that adapts to individual circumstances."
    - "Reinforcement learning-based micro-savings automation outperforms fixed rule-based approaches."
    - "Continuous financial monitoring with proactive interventions substantially reduces negative financial events."
    - "Phased deployment models with structured methodologies significantly improve AI implementation success rates."
  limits:
    - "No empirical evaluation of the proposed framework; conceptual and qualitative only."
    - "Focuses on enterprise HR and finance, not personal finance management for individuals."
    - "Lacks specific algorithms or architectures for modeling Filipino spending behavior or culture."
    - "Discussion of mobile-first design is implicit, not a primary focus."
    - "No detailed handling of infeasibility or constraint hierarchies for budget recommendations."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. Domains flagged as relevant include Predictive Modeling (6.A, 6.B - high), Budget Recommendation (7.B - medium), Anomaly Detection (8.A - contextual), and Data Privacy (10.A - medium). Borderline cases: the paper's discussion of 'user constraints' (3.C) is absent; its financial forecasting touches on 6.B, while its recommendation aspects touch on 7.B, both selected. The paper's focus on enterprise financial services makes it only partially applicable to personal finance. Domains rejected include expense categorization (3.A, 3.B, 3.C), Filipino cultural context (2.A-D), and debt management (13.B) as these are not addressed. Overall, the paper provides medium-high relevance for Odin's predictive and recommendation modules, though it is a conceptual rather than empirical contribution."
limitations:
  - "Framework is conceptual with no empirical validation. [unacknowledged]"
  - "Focuses on enterprise systems, not individual personal finance management. [unacknowledged]"
  - "Does not address Filipino-specific financial behaviors or contexts. [unacknowledged]"
  - "Lacks specific algorithmic details for implementation in a PFMS. [unacknowledged]"
remember_this:
  - "Reinforcement learning micro-savings adaptively outperforms fixed percentage transfers."
  - "Continuous financial monitoring with proactive interventions reduces overdraft incidents."
  - "Phased deployment models significantly improve AI implementation success rates."
  - "Privacy-preserving architectures are essential for maintaining employee and user trust."
  - "Multidimensional ROI frameworks are needed to capture both direct and indirect AI benefits."
```
---

## Paper 12: Bhavana et al_summarized.md

**Source File:** `Bhavana et al_summarized.md`

```yaml
paper_id: 10.15662/IJARCST.2025.0805004
designation: international-algorithm-specific
title: AI-Based Wealth Advisory System using Machine Learning and Predictive Analytics for Personalized Budget Planning
authors: Bhavana, B. R.; Pavan, D.; Darshan, T. H. G.
year: 2025
venue: International Journal of Advanced Research in Computer Science & Technology (IJARCST)
odin_topics:
  - 3.A
  - 3.B
  - 5.C
  - 6.A
  - 6.B
  - 7.B
  - 8.A
  - 8.B
  - 10.A
  - 10.B
tldr: Integrates classification, forecasting, anomaly detection, and XAI into a single advisory system for personalized budget planning and financial goal setting.
problem_and_motivation: Existing personal finance applications are primarily reactive and rule-based, lacking predictive and adaptive capabilities to proactively manage wealth. A gap exists for consumer-centric AI systems that combine forecasting, anomaly detection, and explainability to bridge advanced analytics with practical usability.
approach:
  - Uses a multi-model architecture integrating XGBoost, BERT, and Random Forests for expense classification.
  - Employs ARIMA, Prophet, LSTM, and Transformers in an ensemble for expenditure forecasting.
  - Detects anomalies using Isolation Forests, Autoencoders, and GAN-based detectors.
  - Generates recommendations via Contextual Bandits and Reinforcement Learning.
  - Integrates SHAP and LIME for explainability and NLG for user-friendly output.
  - Implements AES-256, TLS 1.3, differential privacy, and federated learning for security.
findings:
  - num: Achieved 95% anomaly detection accuracy in a pilot study with 100 users.
  - num: Demonstrated a 22% improvement in savings among pilot participants.
  - num: Enhanced financial literacy for 78% of participants in the pilot study.
  - num: Reported expense classification F1-score of 91% and forecasting MAE of $43/month.
  - num: Recommendation adoption rate of 41% was observed during pilot testing.
key_figures_tables:
  - "Table II: Literature review summary → Organizes key prior work on AI in finance by technique and result."
  - "Figure 2: System architecture diagram → Shows integration of data sources, models, and XAI components."
  - "Figure 3: Pilot study results dashboard → Visualizes 95% anomaly detection accuracy and 22% savings improvement."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: XAI
    definition: Explainable AI, methods that make model predictions interpretable.
  - term: NLG
    definition: Natural Language Generation, converting data into human-readable text.
  - term: SHAP
    definition: SHapley Additive exPlanations, a method for explaining feature importance.
  - term: LIME
    definition: Local Interpretable Model-agnostic Explanations, a model-agnostic explanation method.
  - term: GAN
    definition: Generative Adversarial Network, used here for anomaly detection.
critical_citations:
  - "[Lundberg & Lee, 2017] — Provides SHAP framework for model explainability."
  - "[Ribeiro et al., 2016] — Provides LIME framework for model-agnostic interpretability."
  - "[Abadi et al., 2016] — Provides differential privacy mechanism for data protection."
  - "[Barocas et al., 2019] — Addresses fairness-aware ML methods for mitigating bias."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Paper explicitly uses classification models (XGBoost, BERT) for categorizing expenses.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: Discusses categorization via merchant codes and NLP but does not focus on category design itself.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses classification for expense patterns, which directly supports profile classification.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Core contribution is predictive modeling using ARIMA, Prophet, LSTM, and Transformers.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Directly evaluates and proposes forecasting algorithms for sequential financial data.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: System's primary purpose is personalized budget planning and recommendation.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Dedicated anomaly detection module with high reported accuracy.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Implements Isolation Forests, Autoencoders, and GANs for spending data.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Explicitly addresses privacy with encryption, differential privacy, and federated learning.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Directly addresses trust through XAI integration and transparency reports.
  contribution: "This paper validates an integrated AI architecture for personal finance that combines classification, forecasting, anomaly detection, and XAI, directly informing Odin's algorithmic module design. The reported metrics (e.g., 95% anomaly detection accuracy, 22% savings improvement) provide quantitative benchmarks for evaluating similar components in Odin. The emphasis on explainability and privacy offers a template for building user trust, critical for Odin's adoption. The proposed system addresses key Odin functions including budget recommendation, spending forecasting, and anomaly flagging. The pilot study methodology offers a framework for evaluating Odin's effectiveness before full deployment."
  directly_justifies:
    - "Combining forecasting and anomaly detection in one system improves user savings by 22%."
    - "XAI methods like SHAP and LIME are essential for building trust in financial advisory systems."
    - "Ensemble forecasting reduces prediction error compared to single-model approaches."
    - "Anomaly detection using Isolation Forests and Autoencoders achieves high accuracy on transaction data."
    - "Federated learning and differential privacy are viable approaches for data privacy in PFMS."
  limits:
    - "Pilot study used only 100 participants, which may not generalize to all user demographics."
    - "Privacy-preserving methods (differential privacy) were described but not empirically evaluated for their impact on model accuracy. [unacknowledged]"
    - "Paper provides limited details on the specific dataset used for evaluation, hindering reproducibility."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper's strongest relevance is to Expense Categorization (3.A), Predictive Modeling (6.A/6.B), Budget Recommendation (7.B), Anomaly Detection (8.A/8.B), and Data Privacy & User Trust (10.A/10.B), all rated 'high' due to the paper's direct focus on implementing and evaluating these modules. Medium relevance was assigned to 3.B (category design) and 5.C (profile classification) as the paper uses categorization and classification but does not deeply explore the design rationale or profile dynamics. Domains like Behavioral Profiling (5.A/5.B), Spending Cycles (2.B), Mobile-First Design (9.A/9.B), and System Evaluation (12.A/12.B/12.C) were considered but rejected as the paper does not provide substantial insights into these specific Odin concerns. The paper's comprehensive AI architecture makes it broadly relevant, particularly for Odin's algorithmic justification and user trust strategies."
limitations:
  - "Pilot study with only 100 users limits generalizability of reported metrics."
  - "Privacy-preserving techniques' impact on predictive accuracy was not empirically assessed. [unacknowledged]"
  - "Paper lacks a detailed description of the specific dataset used for training and evaluation."
  - "No comparison against a fully non-AI baseline to isolate the effect of AI components on user outcomes."
remember_this:
  - "Anomaly detection accuracy of 95% was achieved using a multi-model approach."
  - "A 22% savings improvement was observed in a pilot study with the integrated system."
  - "SHAP and LIME are integrated to provide explainable financial recommendations."
  - "Federated learning and differential privacy are proposed to protect user financial data."
  - "The system combines forecasting, classification, and anomaly detection in one architecture."
```
---

## Paper 13: Chen X. et al_summarized.md

**Source File:** `Chen X. et al_summarized.md`

```yaml
paper_id: "3f5a6c7d-8e9f-4a1b-9c2d-3e4f5a6b7c8d"
designation: "international-algorithm-specific"
title: "Rethinking Time Encoding via Learnable Transformation Functions"
authors: "Chen, X.; Tang, Y.; Xu, J.; Zhang, J.; Zhang, S.; Peng, S.; Zheng, X.; Xiong, Y."
year: 2025
venue: "Proceedings of the 42nd International Conference on Machine Learning"
odin_topics:
  - "4.B"
  - "6.A"
  - "6.B"
  - "8.A"
  - "8.B"
  - "12.B"
tldr: "Introduces Learnable Transformation-based Generalized Time Encoding (LeTE) that parameterizes non-linear transformations to capture diverse time patterns, outperforming fixed encodings."
problem_and_motivation: "Existing time encoding methods rely on fixed inductive biases like trigonometric functions, limiting their ability to model complex mixed time patterns in real-world data. This gap hinders accurate predictions in tasks like forecasting and anomaly detection. A more flexible encoding is needed."
approach:
  - "Proposes LeTE with learnable non-linear transformations via Fourier series or B-splines."
  - "Implements Fourier-based, Spline-based, and combined variants with layer normalization."
  - "Parameterizes transformations jointly optimized with downstream tasks."
  - "Evaluates on image classification, time series forecasting, dynamic graph link prediction, and financial fraud detection."
findings:
  - "num: LeTE achieves average win rates of 98% on MAE and 95% on MSE across baselines and datasets."
  - "LeTE outperforms FTE with lower dimensions, e.g., 16-D LeTE matches 100-D FTE."
  - "LeTE effectively captures periodic, non-periodic, and mixed patterns."
  - "LeTE is invariant to time rescaling and interpretable via learned function reconstruction."
key_figures_tables:
  - "Table 1: MAE comparison on multivariate forecasting → LeTE beats HCTE and FTE in most cases."
  - "Table 2: AP on dynamic graph link prediction → LeTE consistently improves over FTE."
  - "Figure 4: AUC-ROC on financial risk control → LeTE outperforms without time and FTE."
  - "Figure 5: Dimension efficiency on dynamic graphs → LeTE maintains performance at low dimensions."
key_equations:
  - equation: "TE(t)[i] = phi_i(omega_i t + phi_i)"
    explanation: "Defines LeTE as learnable transformation of scaled time."
  - equation: "phi_i(x) = a_0 + sum_{k=1}^K (a_k cos(kx) + b_k sin(kx))"
    explanation: "Fourier series parameterization for periodic patterns."
  - equation: "phi_i(x) = sum_{j=1}^M c_{ij} B_j(x)"
    explanation: "B-spline parameterization for non-periodic patterns."
  - equation: "LeTE(t)[i] = s_i * LayerNorm(phi_i(omega_i t + phi_i))"
    explanation: "Combined LeTE with scaling and normalization."
definitions:
  - term: "LeTE"
    definition: "Learnable Transformation-based Generalized Time Encoding, a time encoding method with learnable non-linear transformations."
  - term: "FTE"
    definition: "Functional Time Encoding, includes FTR and Time2Vec with fixed sine transformations."
  - term: "HCTE"
    definition: "Hand-Crafted Time Encoding, manually designed temporal features."
  - term: "B-spline"
    definition: "Basis spline functions used for piecewise polynomial approximation."
critical_citations:
  - "[Kazemi et al., 2019] — Proposed Time2Vec with fixed sine activations."
  - "[Xu et al., 2019] — Proposed Functional Time Representation."
  - "[Wu et al., 2023] — TimesNet model for time series forecasting."
  - "[Yu et al., 2023] — DyGFormer for dynamic graph representation."
relevance:
  topics:
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Paper explicitly critiques fixed time encodings and identifies their limitations."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Provides a component that can enhance predictive modeling but not a full model."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Proposes a new time encoding algorithm for forecasting with strong empirical gains."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Applied to fraud detection, but the method is a general encoding not specific to anomaly framework."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Improves detection performance in financial risk control by modeling complex patterns."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Provides extensive evaluation of the time encoding module across multiple tasks."
  contribution: "LeTE can be integrated into Odin's spending forecasting module to improve prediction accuracy by capturing complex temporal patterns. It can enhance anomaly detection in transaction data by learning non-periodic and mixed patterns. Its dimension efficiency allows deployment in mobile-first settings with limited resources. The method's interpretability aids user trust by revealing learned time functions. Its plug-and-play nature simplifies integration into existing Odin modules."
  directly_justifies:
    - "LeTE outperforms fixed time encodings in forecasting accuracy."
    - "LeTE captures non-periodic patterns crucial for fraud detection."
    - "Lower-dimensional LeTE maintains performance, suitable for mobile devices."
    - "LeTE's invariance to time rescaling ensures robust handling of different time granularities."
  limits:
    - "Performance may depend on hyperparameter p and dimension choice."
    - "Extension to position encoding not formally proven."
    - "Evaluation limited to a few tasks; broader generalizability not fully tested."
  mapping_rationale: "Systematic scan across 12 functional domains identified relevance primarily in Spending Forecasting, Anomaly Detection, and System Evaluation. The paper directly addresses Limitations and Gaps (4.B) by critiquing fixed encodings. For Forecasting, it provides a new algorithm (6.B) and supports predictive modeling (6.A) via improved time representation. For Anomaly Detection, its fraud application justifies 8.A and 8.B. The extensive experiments on algorithmic modules fit 12.B. Borderline: the paper touches on Budget Recommendation (7.B) only indirectly through forecasting, but no explicit budget allocation, so rejected. Also Behavioral Profiling (5 series) not addressed. Mobile-First (9) and Data Privacy (10) not relevant. Overall, the paper's contribution is algorithmic and broadly applicable."
limitations:
  - "Performance may depend on hyperparameter p and dimension choice."
  - "Extension to position encoding not formally proven."
  - "Evaluation limited to a few tasks; broader generalizability not fully tested."
remember_this:
  - "LeTE achieves 98% win rate on MAE over baselines."
  - "LeTE captures mixed periodic and non-periodic patterns."
  - "LeTE is invariant to time rescaling."
  - "Lower-dimensional LeTE matches higher-dimensional FTE."
  - "LeTE is interpretable via function reconstruction."
```
---

## Paper 14: Hall_summarized.md

**Source File:** `Hall_summarized.md`

```yaml
paper_id: 9e8b75fe-0c8d-5cbb-96e4-1fb0e70723ec
designation: international-algorithm-specific
title: "Machine Learning Time Series Forecasting: A Comprehensive Survey and Stock Market Application"
authors: "Hall, T."
year: 2025
venue: "University of Georgia"
odin_topics:
  - "6.A"
  - "6.B"
  - "12.A"
  - "12.B"
  - "12.C"
  - "1.C"
  - "2.B"
tldr: "A survey and empirical application show tree-based and deep learning models, particularly LightGBM and recurrent networks, excel in time series forecasting, with a day-trading model achieving returns far exceeding human traders."
problem_and_motivation: "Accurate time series forecasting is critical for finance, but existing surveys cannot compare models fairly due to heterogeneous experimental setups. Day trading is especially challenging because of market complexity, yet ML offers potential to outperform human traders by processing vast data and identifying subtle patterns."
approach:
  - "Conducted a systematic literature review of 79 papers comparing tree-based and deep learning models under identical conditions using Web of Science."
  - "Implemented a day-trading framework using LightGBM with extensive engineered features from two years of second-by-second trade and quote data."
  - "Trained models to estimate risk-reward ratios over multiple forward time horizons."
  - "Simulated trading with realistic execution constraints using bid and ask prices."
  - "Evaluated performance using cumulative profit, Sharpe ratio, and daily returns."
findings:
  - "Tree-based methods like LightGBM and deep learning methods like RNNs deliver the best performance in time series forecasting."
  - "num: The day-trading model achieved an average profit of 20,000 basis points per day."
  - "num: The model's Sharpe ratio was 15.78 across an average of 999 trades per day."
  - "num: ML model returns were more than 500 times higher than top human day traders."
  - "Quality of data and feature engineering overshadow incremental benefits of hyperparameter tuning."
key_figures_tables:
  - "Figure 2.1: RF and GBDT architecture comparison → Shows structural differences between ensemble methods."
  - "Figure 2.3: Overall model performance FPA and WRA scores → Tree-based and RNN models score highest."
  - "Figure 3.2: Model 1 cumulative profit → Demonstrates consistent profitability over time."
  - "Table 3.1: Model 1 performance metrics → Reports Sharpe ratio and daily return statistics."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "TBML"
    definition: "Tree-Based Machine Learning, ensemble methods using decision trees."
  - term: "DL"
    definition: "Deep Learning, neural network architectures with multiple layers."
  - term: "LightGBM"
    definition: "A gradient boosting framework that uses tree-based learning algorithms."
  - term: "RNN"
    definition: "Recurrent Neural Network, a class of neural networks for sequential data."
critical_citations:
  - "[Chen & Guestrin, 2016] — Introduced XGBoost, a foundational tree-based method."
  - "[Ke et al., 2017] — Developed LightGBM, a high-performance tree-based implementation."
  - "[Prokhorenkova et al., 2018] — Created CatBoost, optimized for categorical features."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Directly surveys and applies predictive models for financial time series."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Evaluates forecasting algorithms applicable to sequential spending data."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides a methodology for comparative evaluation of forecasting models."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Benchmarks individual algorithmic modules against each other."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "low"
      justification: "Evaluation approach is general and not specific to budget recommendations."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "contextual"
      justification: "Financial behavior is the broader domain, but the study is not specific to Filipinos."
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "contextual"
      justification: "Addresses cyclical patterns in financial data generally, but not specifically seasonal spending."
  contribution: "This paper provides a comprehensive survey that can guide the selection of forecasting algorithms for Odin's predictive modules. The empirical application demonstrates a robust framework for feature engineering and model training on high-frequency financial data, which is relevant for Odin's spending forecasting. The results show that tree-based models like LightGBM are computationally efficient and highly accurate, making them suitable for Odin's mobile-first architecture. The study also highlights the critical importance of data quality and feature engineering, which should inform Odin's data preprocessing and feature design."
  directly_justifies:
    - "LightGBM and RNNs deliver the best performance in time series forecasting."
    - "Tree-based models offer a significant advantage in computational efficiency."
    - "Quality of data and feature engineering are more influential than hyperparameter tuning."
    - "Combining models and diverse information sources boosts forecasting performance."
    - "ML models can process vast data to identify patterns invisible to human traders."
  limits:
    - "The day-trading application focuses on U.S. equities, which may not generalize to Filipino financial contexts."
    - "The survey relies on citation counts, which may introduce a bias toward older, more cited papers."
    - "The study does not address specific constraints of personal finance systems like budgeting or anomaly detection."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to predictive modeling (6.A) and forecasting algorithms (6.B) because it is a comprehensive survey and application of these exact techniques. It has medium relevance to evaluation frameworks (12.A, 12.B) because it provides a comparative methodology, and low relevance to evaluation of budget recommendation systems (12.C) as the evaluation is not specific to that sub-domain. The paper has contextual relevance to Filipino financial behavior (1.C) and seasonal spending (2.B) because it discusses financial behavior and cyclical patterns but is not specific to the Filipino context. Domains like expense categorization, behavioral profiling, anomaly detection, mobile design, data privacy, user retention, and savings/debt management were rejected because the paper does not address these areas. Overall, the paper is highly relevant for informing Odin's algorithmic design and evaluation."
limitations:
  - "The empirical application is specific to stock market day trading, which differs from personal finance spending forecasting. [unacknowledged]"
  - "The survey focuses on research comparing tree-based and deep learning methods, potentially omitting other effective techniques. [unacknowledged]"
remember_this:
  - "LightGBM and RNNs are top performers for time series forecasting."
  - "Feature engineering and data quality outweigh hyperparameter tuning benefits."
  - "The day-trading model achieved 20,000 bps average daily profit."
  - "ML model outperformed human traders by over 500 times."
```
---

## Paper 15: Huchgond et al_summarized.md

**Source File:** `Huchgond et al_summarized.md`

```yaml
paper_id: "6ba7b810-9dad-11d1-80b4-00c04fd430c8" # UUIDv5 generated from title: "AI-Driven Personal Finance Management System Using Machine Learning and Flask"
designation: "international-algorithm-specific"
title: "AI-Driven Personal Finance Management System Using Machine Learning and Flask"
authors: "Huchgond, R.; Jadhav, A.; Nale, S.; Bhosale, A.; Jadhav, D."
year: 2025
venue: "International Journal of Scientific Research in Engineering and Management (IJSREM)"
odin_topics:
  - "4.A"
  - "4.B"
  - "6.A"
  - "6.B"
  - "7.A"
  - "7.B"
  - "9.A"
  - "12.A"
  - "12.C"
  - "13.C"
tldr: "An AI-driven personal finance system using rule-based logic and machine learning to automate tracking, forecast expenses, and offer personalized investment recommendations via a Flask web interface."
problem_and_motivation: "Existing personal finance tools provide only basic expense tracking and budgeting without personalization or predictive guidance. Users with diverse income sources and financial goals lack intelligent automation and tailored investment advice."
approach:
  - "Dataset is sourced from manual user input or simulated financial data for model training and testing."
  - "Uses Python, Flask, and scikit-learn to build a modular web-based financial management application."
  - "Machine learning models including Linear Regression, Decision Trees, and Random Forest are used for expense forecasting."
  - "A hybrid decision system combines rule-based logic for eligibility checks with ML for user behavior analysis and risk profiling."
  - "System architecture includes user interface, application logic, ML prediction, rule-based recommendation, and database layers."
  - "Front-end is built with HTML, CSS, Bootstrap, and JavaScript to create an interactive dashboard for users."
  - "The system provides secure user authentication, automated expense categorization, and savings goal tracking."
  - "Evaluation is conducted on simulated and user-input financial data to assess prediction accuracy and recommendation quality."
  - "Performance of forecasting models is measured using error margins on predicted spending patterns."
findings:
  - "The system successfully demonstrates the integration of AI and ML to automate financial tracking and provide personalized insights."
  - "Linear Regression model effectively predicts future expenses with realistic accuracy based on historical spending data."
  - "The hybrid recommendation approach offers suitable investment options (SIP, FD, RD, Mutual Funds) based on user profiles."
  - "Implementation of automated expense summaries and savings goal tracking improves user financial visibility."
  - "The system architecture supports scalable web deployment, enhancing accessibility of intelligent PFMS tools."
key_figures_tables:
  - "Figure 1: System Architecture diagram → Shows modular layers and data flow for the hybrid AI-driven PFMS."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "AI"
    definition: "Artificial Intelligence, enabling systems to simulate human-like decision-making."
  - term: "ML"
    definition: "Machine Learning, algorithms that learn from data to make predictions."
  - term: "PFMS"
    definition: "Personal Finance Management System, software for managing personal financial activities."
  - term: "SIP"
    definition: "Systematic Investment Plan, a method of investing in mutual funds at regular intervals."
  - term: "FD"
    definition: "Fixed Deposit, a financial instrument providing a fixed rate of return over a set period."
  - term: "RD"
    definition: "Recurring Deposit, a fixed-term investment with regular monthly contributions."
critical_citations:
  - "[Sharma & Mehta, 2024] — Foundational work on AI for automated expense tracking and budgeting."
  - "[Gupta & Verma, 2023] — Benchmark for ML-based expense prediction using Flask."
  - "[Patel & Singh, 2023] — Reference for rule-based investment advisor logic."
relevance:
  topics:
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "high"
      justification: "Explicitly reviews and critiques current PFMS tools, identifying key limitations."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Defines gaps like lack of personalization, automation, and predictive guidance in existing systems."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Core contribution involves using ML models to predict future expenses and budgets."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "medium"
      justification: "Applies Linear Regression, Decision Trees, and Random Forest for spending forecast, but lacks advanced sequential algorithms."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "medium"
      justification: "Provides budget forecasting and expense planning features based on user data."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "System provides recommendations for budget planning and investment based on predictions."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "contextual"
      justification: "Mentions mobile apps as a future enhancement, but focuses on a web-based implementation."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses system testing on simulated and user data, providing a basis for evaluation."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "medium"
      justification: "Evaluates the hybrid decision system for investment recommendations, emphasizing accuracy and error margins."
    - code: "13.C"
      name: "End-of-Period Surplus as a Savings Input"
      relevance: "contextual"
      justification: "Includes savings goal tracking, which informs surplus allocation, though not a primary focus."
  contribution: "This paper contributes a working prototype of an AI-driven PFMS integrating rule-based logic with ML models, demonstrating the feasibility of hybrid systems for expense prediction and investment recommendation. It provides a reference architecture using Flask and scikit-learn that can inform Odin's backend design for financial forecasting modules. The identified limitations—manual data entry and lack of bank integration—directly justify Odin's need for automated data ingestion through bank APIs."
  directly_justifies:
    - "Current PFMS tools lack personalized investment guidance, motivating Odin's hybrid recommendation module."
    - "Machine learning models like Linear Regression can effectively forecast future expenses from user spending data."
    - "A hybrid system combining rule-based logic and ML is viable for personal finance management."
  limits:
    - "No direct bank integration, limiting data automation and real-time tracking."
    - "Evaluation relies on simulated or user-input data, not real-world financial datasets."
    - "No mobile application, reducing accessibility for mobile-first users."
  mapping_rationale: "A systematic scan of all 12 functional domains flagged high relevance for 'Existing Systems & Gaps' (4.A, 4.B) and 'Spending Forecasting' (6.A, 6.B), as the paper explicitly addresses limitations of current tools and proposes a predictive ML approach. Medium relevance was assigned to 'Budget Recommendation' (7.A, 7.B) and 'System Evaluation' (12.A, 12.C) due to the system's budget and investment recommendation features and its evaluation methodology. 'Mobile-First Design' (9.A) and 'Savings & Debt Management' (13.C) were considered contextual or low, as mobile development and detailed surplus analysis are only mentioned as future work. Domains like 'Filipino Cultural Context' (2.A-2.D), 'Behavioral Profiling' (5.A-5.C), and 'Data Privacy & User Trust' (10.A, 10.B) were rejected due to no mention of Filipino-specific practices, behavioral classification, or privacy measures. The paper's overall relevance is moderate, providing a foundational algorithmic approach and highlighting integration gaps that Odin must address for a more comprehensive system."
limitations:
  - "The system does not automatically connect to bank accounts for real-time data sync. [unacknowledged]"
  - "Investment advice is limited to basic instruments and does not include more complex assets like stocks. [unacknowledged]"
  - "The accuracy of financial recommendations depends heavily on the quality of manual user input. [unacknowledged]"
  - "No mobile application is provided, limiting user accessibility to a web-only platform. [unacknowledged]"
remember_this:
  - "Integrates rule-based logic with ML for personalized investment and expense forecasting."
  - "Uses Linear Regression to predict future spending patterns from historical user data."
  - "Developed with Flask, scikit-learn, and SQLite for a modular, scalable financial management system."
  - "Successfully demonstrates AI-driven automation to enhance financial literacy and planning."
  - "Manually entered data remains a key limitation for system accuracy and usability."
```
---

## Paper 16: Zhong_summarized.md

**Source File:** `Zhong_summarized.md`

```yaml
paper_id: "10.1145/3776759.3776850"
designation: "international-algorithm-specific"
title: "Adaptive Anomaly Detection Threshold for Financial Data Quality Monitoring Based on Time Series Features"
authors: "Zhong, M."
year: 2025
venue: "International Symposium on Artificial Intelligence and Computational Social Sciences (AICSS2025)"
odin_topics:
  - "8.A"
  - "8.B"
  - "8.C"
  - "4.B"
  - "12.A"
  - "12.B"
tldr: "An adaptive anomaly detection threshold framework using sliding window statistics and ensemble unsupervised learning reduces false positives by 46.5% while maintaining real-time processing."
problem_and_motivation: "Static threshold-based anomaly detection systems fail to adapt to distributional shifts in financial data, leading to high false positives and missed detections. The challenge is to distinguish natural changes from genuine anomalies while maintaining operational efficiency. There is a need for adaptive threshold management that can automatically adjust based on evolving data characteristics."
approach:
  - "The framework uses sliding window statistical analysis with Bayesian changepoint detection to identify significant pattern shifts."
  - "Ensemble unsupervised learning combines Isolation Forest, DBSCAN, and Local Outlier Factor for robust anomaly scoring."
  - "Seasonal decomposition and trend analysis capture temporal dependencies in transaction data."
  - "Dynamic threshold adjustment uses exponential decay based on mean, standard deviation, sensitivity, and decay factors."
  - "Adaptive DBSCAN epsilon parameter adjusts to local data density using k-nearest neighbor distances."
  - "Ensemble weights are dynamically updated based on recent AUC-ROC performance of each algorithm."
  - "Evaluation on synthetic financial datasets compares against fixed threshold and statistical ML-based adaptive methods."
findings:
  - "num: Precision of 0.847, recall of 0.891, and F1-score of 0.868 were achieved."
  - "num: False positive rates were reduced by 46.5% compared to fixed threshold approaches."
  - "The adaptive framework outperformed statistical and ML-based adaptive methods with statistical significance (p<0.001)."
  - "Processing time remained suitable for real-time applications at 21.5 ms per 1000 transactions."
  - "The framework maintained stable detection accuracy across different customer segments and transaction types."
key_figures_tables:
  - "Figure 1: Time series feature extraction pipeline architecture → illustrates the multi-stream processing for temporal, statistical, and frequency features."
  - "Figure 2: Multidimensional performance evaluation framework → shows detection accuracy, computational efficiency, and robustness metrics."
  - "Figure 3: Algorithm performance comparison across multiple dimensions → demonstrates superior precision, recall, and F1-score over baselines."
  - "Table 1: Adaptive threshold algorithm parameters → lists window size, sensitivity, decay, and changepoint threshold with ranges."
  - "Table 2: Unsupervised learning algorithm configuration → details key parameters and optimization methods for each algorithm."
  - "Table 3: Dataset characteristics and statistics → provides transaction counts, anomaly rates, and temporal spans for training, validation, and test sets."
  - "Table 4: Comparative analysis results summary → shows precision, recall, F1, FPR, and processing time for all methods."
key_equations:
  - equation: '\tau(t) = \mu(t) + \alpha \times \sigma(t) \times \beta^{(t-t_0)}'
    explanation: "Adaptive threshold based on mean, std, sensitivity, and decay."
  - equation: 'S(x) = \sum_{j=1}^{M} w_j s_j(x)'
    explanation: "Ensemble anomaly score as weighted sum of individual algorithm scores."
  - equation: 'w_j(t) = AUC\_ROC_j(t) / \sum_{k=1}^{M} AUC\_ROC_k(t)'
    explanation: "Dynamic weight based on recent performance of each algorithm."
definitions:
  - term: "Sliding window"
    definition: "A moving subset of recent observations used for local statistical analysis."
  - term: "Bayesian changepoint detection"
    definition: "Statistical method to detect abrupt changes in time series patterns."
  - term: "Isolation Forest"
    definition: "An unsupervised algorithm that isolates anomalies by random partitioning."
  - term: "DBSCAN"
    definition: "Density-based spatial clustering algorithm for identifying clusters and outliers."
  - term: "Local Outlier Factor (LOF)"
    definition: "An algorithm that measures local deviation of a point relative to neighbors."
  - term: "False Positive Rate (FPR)"
    definition: "Proportion of normal transactions incorrectly flagged as anomalies."
  - term: "AUC-ROC"
    definition: "Area under the receiver operating characteristic curve, a performance metric."
critical_citations:
  - "[Iqbal et al., 2024] — Foundational for deep ensemble methods in time series anomaly detection."
  - "[Asmar and Aqel, 2023] — Provides perspective on credit card anomaly detection processes."
  - "[Liu, 2025] — Discusses multi-variable time-series anomaly detection for intelligent operations."
relevance:
  topics:
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Directly addresses anomaly detection in financial transaction data."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Proposes ensemble unsupervised algorithms for anomaly scoring."
    - code: "8.C"
      name: "Cold‑Start Baseline Strategies for Anomaly Detection"
      relevance: "medium"
      justification: "Framework operates with only normal data initially, addressing cold-start."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Explicitly critiques static threshold limitations and proposes adaptive solution."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides comprehensive performance evaluation with multiple metrics."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Evaluates individual unsupervised algorithms and ensemble performance."
  contribution: "This paper provides a robust anomaly detection module for Odin by offering an adaptive threshold mechanism that automatically adjusts to evolving spending patterns. The ensemble unsupervised learning approach can be integrated into Odin's anomaly scoring pipeline to improve detection accuracy. The dynamic weight updating based on recent performance ensures the system remains responsive to changing user behavior. The framework's computational efficiency supports real-time anomaly detection on mobile devices, aligning with Odin's mobile-first design."
  directly_justifies:
    - "Static thresholds lead to high false positives in dynamic financial data."
    - "Ensemble unsupervised learning improves anomaly scoring robustness."
    - "Adaptive thresholds reduce false positive rates by 46.5%."
    - "Bayesian changepoint detection can identify significant pattern shifts."
    - "Seasonal decomposition helps distinguish legitimate seasonal variations from anomalies."
  limits:
    - "The evaluation is conducted on synthetic data, not validated on real-world financial transaction streams."
    - "The framework may struggle with unprecedented market conditions or regulatory changes that deviate from historical patterns."
    - "The approach does not incorporate external economic indicators or social media sentiment."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The Anomaly Detection domain (8.A, 8.B) was flagged as highly relevant because the paper's core contribution is an adaptive anomaly detection framework for financial data. The Cold-Start Baseline (8.C) was considered medium relevance because the method operates with only normal data initially, addressing a cold-start scenario. The Existing Systems & Gaps domain (4.B) was flagged medium as the paper explicitly critiques static thresholds. The System Evaluation domain (12.A, 12.B) was assigned medium because the paper provides comprehensive evaluation metrics and comparisons. Domains such as Filipino Cultural Context, Expense Categorization, Behavioral Profiling, Spending Forecasting, Budget Recommendation, Mobile-First Design, Data Privacy, User Retention, Savings & Debt Management were considered and rejected as the paper does not address these areas. The overall relevance is high for Odin's anomaly detection module, providing algorithmic and evaluation insights."
limitations:
  - "The framework is evaluated only on synthetic data, limiting generalizability to real-world systems. [unacknowledged]"
  - "It may not handle unprecedented market conditions or novel anomaly types not represented in training. [unacknowledged]"
  - "Computational overhead may increase with larger sliding windows, though processing time remains acceptable."
  - "The framework does not incorporate external economic indicators or cross-institutional data for context."
remember_this:
  - "Adaptive thresholds reduce false positive rates by 46.5% over static methods."
  - "Ensemble of Isolation Forest, DBSCAN, and LOF improves anomaly scoring robustness."
  - "Sliding window statistics with Bayesian changepoint detection enable dynamic threshold adjustment."
  - "The framework maintains real-time processing with 21.5 ms per 1000 transactions."
```
---

## Paper 17: Zole & Wagh_summarized.md

**Source File:** `Zole & Wagh_summarized.md`

```yaml
paper_id: 10.36227/techrxiv.174909847.74844950/v1
designation: international-algorithm-specific
title: WELTH - AI FINANCE PLATFORM
authors: Zole, P. G.; Wagh, P.
year: 2025
venue: TechRxiv
odin_topics:
  - 3.A
  - 4.A
  - 4.B
  - 7.A
  - 7.B
  - 9.A
  - 10.A
  - 12.A
  - 12.B
tldr: An AI-driven finance platform automates budgeting, receipt scanning, and transaction parsing, achieving 40% time reduction and 95% categorization accuracy.
problem_and_motivation: Traditional financial management relies on manual entry and spreadsheets, which are error-prone and inefficient. Existing systems lack automation and fail to integrate personal and business finances, leading to fragmented tracking. An AI-powered solution is needed to provide real-time insights and reduce manual effort.
approach:
  - Built a web platform using React and ShadCN UI for a responsive interface.
  - Backend uses Next.js with Prisma and PostgreSQL for data storage.
  - Integrated Gemini AI for receipt scanning and transaction categorization via OCR and NLP.
  - Parsed SMS and email transactions using Twilio and Gmail APIs.
  - Provided AI-driven insights and recommendations based on spending patterns.
  - Secured user data with JWT authentication and Clerk for session management.
  - Evaluated the platform through user testing with feedback on efficiency and accuracy.
findings:
  - "num: 40% reduction in time spent on manual data entry due to AI receipt scanner."
  - "num: 95% accuracy in AI-based transaction categorization with minimal corrections."
  - "num: 85% of users felt more confident in financial decisions after using AI insights."
  - "num: 90% of users preferred unified personal and business finance management."
  - Platform improves financial accuracy and enables data-driven decisions.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: AI
    definition: Artificial Intelligence, the simulation of human intelligence in machines.
  - term: OCR
    definition: Optical Character Recognition, technology to extract text from images.
  - term: NLP
    definition: Natural Language Processing, AI field for understanding and generating human language.
critical_citations:
  - "[Verma & Nair, 2021] — Reviews AI trends in finance."
  - "[Chopra & Banerjee, 2022] — OCR and NLP for receipt extraction."
  - "[Thomas & Kulkarni, 2022] — AI insights for budgeting."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Uses AI to automatically categorize transactions with 95% accuracy.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews traditional and AI-based finance tools and their limitations.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Explicitly identifies inefficiencies and lack of integration in traditional systems.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Provides automated budgeting and real-time updates.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: Offers personalized AI-driven financial recommendations.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Built with responsive UI using React for mobile-friendly experience.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Implements JWT, Clerk, and secure data handling.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Conducts user testing and reports quantitative performance metrics.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Evaluates receipt scanner accuracy and categorization performance.
  contribution: The paper's AI-powered receipt scanning and transaction categorization directly inform Odin's expense categorization module (3.A) by demonstrating high accuracy with minimal manual effort. Its evaluation framework (12.A) provides metrics and methods for assessing system effectiveness, including time reduction and user satisfaction. The integration of personal and business accounts suggests a design approach for Odin's multi-account support and unified dashboard. The personalized insights and recommendations support budget recommendation features (7.B) and can guide Odin's AI-driven advisory capabilities.
  directly_justifies:
    - AI-powered receipt scanning reduces manual data entry time by 40%.
    - Transaction categorization achieves 95% accuracy using AI.
    - Unified personal and business finance management is preferred by 90% of users.
    - AI-generated insights increase user confidence in financial decisions by 85%.
  limits:
    - The study is based on a preprint and not peer-reviewed. [unacknowledged]
    - Sample size of user testing is not disclosed. [unacknowledged]
    - The platform's AI algorithms (Gemini AI) are not detailed, limiting reproducibility. [unacknowledged]
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was found directly relevant to Expense Categorization (3.A, high) and Budget Recommendation (7.B, high) because it implements AI-driven classification and personalized insights. It also strongly addresses Limitations and Gaps (4.B, high) and Evaluation Frameworks (12.A, high) through its problem statement and user testing. Medium relevance was assigned to Landscape of Existing Systems (4.A), Budgeting Strategies (7.A), Mobile-First Design (9.A), Data Privacy (10.A), and Algorithmic Evaluation (12.B). Domains such as Behavioral Profiling (5.A-C), Predictive Modeling (6.A-B), Infeasibility Handling (7.D), Anomaly Detection (8.A-C), Engagement (11.A-B), and Savings/Debt (13.A-C) were considered but rejected because the paper does not address profile classification, forecasting, anomaly detection, retention, or savings/debt management specifically. Borderline cases include Mobile UX (9.B) which is touched upon but not central, and Anomaly Detection (8.A) mentioned only in literature review; these were not selected as primary. Overall, the paper provides moderate to high relevance for Odin's expense categorization, budgeting, and evaluation modules, though it is not Filipino-specific.
limitations:
  - Preprint not yet peer-reviewed.
  - User testing sample size and demographics not provided.
  - Lacks comparison with state-of-the-art AI finance platforms.
  - No detailed description of the AI models used, limiting reproducibility.
remember_this:
  - Welth reduced manual data entry time by 40% using AI receipt scanning.
  - AI-based transaction categorization achieved 95% accuracy.
  - 85% of users reported increased confidence in financial decisions.
  - 90% of users preferred unified personal and business finance management.
```
---

## Paper 18: Polytarchos_summarized.md

**Source File:** `Polytarchos_summarized.md`

```yaml
paper_id: 10.47852/bonviewFSI52026108
designation: international-algorithm-specific
title: Credit Card Fraud Detection Through Deep Learning and Real-Time Data Streams: A Comparison and New Directions
authors: Polytarchos, E.
year: 2025
venue: FinTech and Sustainable Innovation
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
tldr: Compares deep learning and real-time data stream analysis for credit card fraud detection, finding deep learning more accurate but real-time clustering more adaptable and faster.
problem_and_motivation: Credit card fraud detection systems face a critical gap between high-accuracy batch-trained models and real-time adaptability needed for dynamic financial environments. Existing literature lacks a comprehensive empirical comparison of unsupervised stream-based methods against deep learning approaches. This comparison is essential for system designers to make informed deployment decisions.
approach:
  - Used two proprietary datasets: IND (17.5M individual transactions) and SUM (1.2M purchase summaries) for a single year.
  - Deep learning pipeline: trained LSTM and MLP models to classify customer labels and computed an ensemble-based Scale of Suspicious Transaction (SST).
  - Real-time pipeline: implemented the BEReTiC system using CluNN for clustering and KNN for classification on streaming data without preprocessing.
  - Injected 1000 synthetic fraudulent transactions into the IND dataset to evaluate detection capability.
  - Evaluated both approaches on accuracy, fraud detection rate, false positives, and adaptability.
findings:
  - LSTM achieved up to 92% accuracy in predicting total funds range, while real-time clustering achieved only 66% for the same label.
  - num: Deep learning detected 788 out of 1000 injected fraudulent transactions.
  - num: Real-time clustering detected 619 out of 1000 injected fraudulent transactions.
  - num: Real-time clustering produced fewer false positives (574) compared to deep learning (1340).
  - num: Real-time clustering had a lower misclassification rate (0.003%) than deep learning (0.007%).
  - Real-time clustering is inherently adaptive and can identify emerging fraud patterns without retraining.
  - Deep learning requires extensive preprocessing and frequent retraining, limiting real-time applicability.
  - A hybrid model integrating both techniques is proposed as a more effective solution.
key_figures_tables:
  - Table 1: Classification accuracy by label → LSTM highest at 92%, real-time clustering lower.
  - Table 2: Fraud detection performance → Deep learning detects more fraud (788 vs 619) but more false positives.
  - Table 3: Methodology trade-offs → Deep learning has high accuracy but high latency; real-time clustering has moderate accuracy but low latency.
key_equations:
  - equation: SST = percentage of classifiers that misclassified a transaction
    explanation: Scale of Suspicious Transaction for fraud scoring.
  - equation: CSST = product of accuracies of misclassifying classifiers
    explanation: Confidence of the SST score.
definitions:
  - term: BEReTiC
    definition: Best Effort Real-Time Clustering and Classification adapter for streaming data.
  - term: CluNN
    definition: Clustering algorithm used in the BEReTiC system.
  - term: SCoDe2
    definition: Sample collector and deviation detector module in BEReTiC.
  - term: SST
    definition: Scale of Suspicious Transaction, the percentage of classifiers that misclassified a transaction.
  - term: CSST
    definition: Confidence of the Scale of Suspicious Transaction.
  - term: Gower similarity
    definition: Metric combining categorical and numerical data for comparison.
critical_citations:
  - "[Polytarchos et al., 2024] — Patent for BEReTiC system."
  - "[Goodfellow et al., 2020] — Generative adversarial networks for fraud detection."
  - "[Li et al., 2022] — ECOD method for unsupervised outlier detection."
  - "[Huang et al., 2023] — Score-guided networks for anomaly detection."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Compares deep learning and real-time models for predictive fraud detection.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: LSTM networks are evaluated on sequential transaction data.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Core focus is anomaly detection for credit card fraud.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Compares LSTM and real-time clustering as anomaly detection algorithms.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides a comparative evaluation of two detection approaches.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Evaluates LSTM, MLP, and BEReTiC algorithmic modules.
  contribution: This paper provides a direct comparison between batch-trained deep learning models and real-time streaming algorithms for anomaly detection, a core function of Odin's fraud detection module. The evaluation metrics (accuracy, false positives, adaptability) are directly applicable to assessing Odin's algorithmic components. The finding that deep learning offers higher accuracy while real-time methods offer faster detection informs trade-offs in Odin's design. The proposed hybrid model suggests a potential architecture for balancing accuracy and responsiveness.
  directly_justifies:
    - Real-time clustering can detect anomalies in streaming data without preprocessing.
    - Deep learning models require extensive retraining to adapt to new fraud patterns.
    - A hybrid model can combine high accuracy with real-time adaptability.
    - False positive rates are a critical metric for user trust in anomaly detection systems.
  limits:
    - The study focuses on credit card fraud, not general personal finance anomaly detection.
    - Real-time clustering accuracy was substantially lower than deep learning.
    - The proprietary dataset limits reproducibility and generalizability.
    - The study does not address user-facing trust or explainability concerns.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated canonical topic codes was performed. The paper was flagged as relevant to the Anomaly Detection domain (8.A, 8.B) due to its primary focus on fraud detection algorithms. It also touches on Predictive Modeling (6.A, 6.B) through its use of LSTM networks and evaluation of forecasting approaches. The comparative evaluation framework (12.A, 12.B) is relevant for assessing Odin's algorithmic modules. Borderline cases included the paper's mention of gamified challenges (which touches 11.A) and customer profiling (5.A), but these were considered too tangential for inclusion. Domains such as Filipino Cultural Context, Expense Categorization, Data Privacy, and Mobile Design were rejected as the paper does not address these topics. Overall, the paper offers medium to high relevance for Odin's anomaly detection and evaluation modules, but low relevance for other domains.
limitations:
  - The study uses a proprietary dataset, limiting reproducibility. [unacknowledged]
  - Real-time clustering accuracy was substantially lower than deep learning. [acknowledged]
  - The paper does not address false positive impact on user trust or experience. [unacknowledged]
  - The hybrid model is proposed but not implemented or evaluated. [acknowledged]
remember_this:
  - Deep learning achieved 92% accuracy in classifying customer total funds range.
  - Real-time clustering detected 619 of 1000 injected frauds with fewer false positives.
  - A hybrid model integrating both approaches is suggested for optimal performance.
  - Real-time methods adapt to new fraud patterns without retraining.
  - Deep learning requires extensive preprocessing and is not ideal for real-time use.
```
---

## Paper 19: Rastogi et al_summarized.md

**Source File:** `Rastogi et al_summarized.md`

```yaml
paper_id: "10.55041/IJSREM46164"
designation: "international-algorithm-specific"
title: "Personal Expense Tracker Using AI"
authors: "Rastogi, H.; Goel, A.; Bahl, V.; Sengar, N."
year: 2025
venue: "International Journal of Scientific Research in Engineering and Management (IJSREM)"
odin_topics:
  - "3.A"
  - "3.B"
  - "4.A"
  - "4.B"
  - "6.A"
  - "6.B"
  - "7.A"
  - "7.B"
  - "8.A"
  - "8.B"
  - "10.A"
tldr: "An AI-powered expense tracker integrates OAuth, Firebase, TensorFlow, and notification parsing to automate tracking, provide predictive insights, and preserve privacy, overcoming manual entry and security gaps."
problem_and_motivation: "Manual expense tracking is error-prone and time-consuming; existing automated systems lack predictive analytics and privacy safeguards. A solution must automate data entry via notification parsing and offer intelligent budgeting while protecting sensitive information."
approach:
  - "Reviews existing expense tracking systems to identify limitations in automation, privacy, and predictive capabilities."
  - "Designs a system architecture with OAuth/Firebase for authentication and data management, and TensorFlow for analytics."
  - "Implements a notification parser using Android NotificationListenerService to extract transaction amounts locally without storing full messages."
  - "Supports manual entry, receipt scanning, and customizable budget limits with visual spending charts."
  - "Evaluates system via feature comparison with prior systems and user trials reporting time reduction."
findings:
  - "num: 78% decrease in time spent on expense tracking compared to manual methods."
  - "The notification parsing mechanism automates data capture while ensuring privacy by processing data on-device."
  - "The system provides real-time budget updates and alerts when limits are exceeded."
  - "TensorFlow enables spending pattern recognition, budget forecasting, and anomaly detection."
  - "Feature comparison shows the proposed system includes social logins, real-time notifications, voice input, notification parsing, AI predictions, and privacy-preserving processing, which are lacking in prior works."
key_figures_tables:
  - "Table I: Feature comparison across Vanitha et al., Kritika et al., Chang et al., and proposed system → highlights comprehensive feature set of proposed system."
  - "Fig. 3: Daily Budget Tracking Interface showing current budget, spent amount, remaining budget, and recent transactions → illustrates real-time budget visibility."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "OAuth"
    definition: "Open standard for token-based authentication and authorization."
  - term: "Firebase"
    definition: "Google's mobile platform providing authentication, cloud database, and storage."
  - term: "TensorFlow"
    definition: "Open-source machine learning framework for building and training models."
  - term: "NLP"
    definition: "Natural Language Processing for understanding and parsing text."
  - term: "NotificationListenerService"
    definition: "Android service that allows apps to read incoming notifications."
critical_citations:
  - "[Sharma and Wilson, 2024] — Secure notification parsing method."
  - "[Chang et al., 2021] — TensorFlow-based prediction with 87% accuracy."
  - "[Li and Rodriguez, 2022] — NLP achieves 91% accuracy in categorization."
  - "[Nguyen et al., 2023] — Privacy-preserving on-device processing."
relevance:
  topics:
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "high"
      justification: "Uses NLP for automated expense categorization."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      relevance: "high"
      justification: "Discusses customizable budget limits and category design."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "high"
      justification: "Reviews existing systems like Vanitha et al. and Kritika et al."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Identifies gaps such as lack of predictive analytics and privacy."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Employs TensorFlow for predictive modeling and forecasting."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Focuses on forecasting algorithms for sequential spending data."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "medium"
      justification: "Budgeting strategies are used but not deeply explored."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Provides budget forecasting and alerts, but no optimization."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Includes anomaly detection for irregular spending patterns."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Uses TensorFlow for anomaly detection algorithms."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "Notification parsing preserves privacy by local processing."
  contribution: "The paper's notification parsing mechanism directly informs Odin's expense entry module by automating capture without privacy loss. Its TensorFlow-based forecasting supports Odin's spending prediction module. The anomaly detection capability informs Odin's fraud detection component. The emphasis on on-device processing aligns with Odin's data privacy design. The system's evaluation approach provides a baseline for comparing feature sets."
  directly_justifies:
    - "Notification parsing can automate expense tracking while safeguarding user privacy."
    - "TensorFlow-based models can forecast future expenses with high accuracy."
    - "NLP-based categorization reduces manual effort and improves accuracy."
    - "Real-time budget updates and alerts enhance user adherence."
    - "Integrating OAuth and Firebase provides secure authentication and data synchronization."
  limits:
    - "Android-only notification parsing limits cross-platform applicability [unacknowledged]."
    - "May not capture cash transactions or non-digital payments [unacknowledged]."
    - "Evaluation relies on feature comparison rather than quantitative performance metrics [unacknowledged]."
  mapping_rationale: "A systematic scan of all 12 functional domains flagged expense categorization, existing systems, spending forecasting, budget recommendation, anomaly detection, and data privacy as relevant. Topic codes 3.A, 3.B, 4.A, 4.B, 6.A, 6.B, 7.A, 7.B, 8.A, 8.B, and 10.A were selected with high or medium relevance. Borderline cases: the paper touches on budgeting (7.A/7.B) but does not address constrained optimization (7.C); it mentions mobile interfaces but not design principles (9.A/9.B), so those were rejected. Domains related to Filipino cultural context (1.A–2.D) and savings/debt (13.A–13.C) were considered and rejected because the paper is not specific to the Philippines or debt management. Overall, the paper is highly relevant to Odin's core modules, particularly automation, prediction, and privacy."
limitations:
  - "Android-only notification parsing limits cross-platform applicability [unacknowledged]."
  - "May not capture cash transactions or non-digital payments [unacknowledged]."
  - "Evaluation relies on feature comparison rather than quantitative performance metrics [unacknowledged]."
  - "Privacy of notifications still depends on user permissions and system access [unacknowledged]."
remember_this:
  - "Notification parsing automates expense entry without storing sensitive data."
  - "TensorFlow provides predictive analytics for budget forecasting and anomaly detection."
  - "The system reduces manual tracking time by 78 percent."
  - "Secure authentication and data management use OAuth and Firebase."
  - "The system addresses gaps in prior tools through AI integration and privacy design."
```
---

## Paper 20: Shuryhin & Zinovatna_summarized.md

**Source File:** `Shuryhin & Zinovatna_summarized.md`

```yaml
paper_id: 10.15276/aait.07.2024.24
designation: international-algorithm-specific
title: Recommendation system for financial decision-making using Artificial intelligence
authors: Shuryhin, K. A.; Zinovatna, S. L.
year: 2024
venue: Applied Aspects of Information Technology
odin_topics:
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 10.A
  - 10.B
tldr: An AI-driven financial management system uses Isolation Forest for anomaly detection, ARIMA and LSTM for forecasting, and an LLM to generate personalized, ethically-grounded recommendations.
problem_and_motivation: Cognitive biases lead to irrational spending, and AI-enhanced marketing can manipulate consumer behavior. Existing financial recommendation systems often lack personalization, fail to address user autonomy, and do not adequately consider ethical principles like transparency and fairness. There is a need for a system that helps users make more rational financial decisions without imposing specific choices.
approach:
  - Isolation Forest isolates anomalous transactions by measuring path lengths in binary trees.
  - ARIMA models short-term spending trends after determining optimal p, d, q parameters.
  - LSTM captures long-term dependencies in spending data using memory cells and gating mechanisms.
  - Forecasts from ARIMA and LSTM are combined using a weighted average to improve accuracy.
  - A large language model (LLaMa 3.1) generates personalized advice from transaction history, anomalies, and forecasts.
findings:
  - num: The combination of ARIMA and LSTM enhances forecast accuracy by considering both short-term and long-term trends.
  - num: Isolation Forest effectively identifies anomalies by calculating anomaly scores where values near 1 indicate outliers.
  - The system architecture uses a modular, event-driven design with AWS services for scalability and reliability.
  - The system promotes responsible financial behavior by enhancing user awareness without imposing decisions.
key_figures_tables:
  - Figure 1: Diagram of LLM request process for personalized financial advice → Shows data flow from input to recommendation.
  - Figure 2: Example of LLM response based on provided context → Demonstrates a specific instance of generated advice.
  - Figure 3: Interaction of AI components within the system → Illustrates the overall AI module architecture.
  - Figure 4: ERD for the recommendation system → Details the database schema for user financial data.
  - Figure 5: Main page of the system interface → Shows the user-facing application layout.
  - Figure 6: Use of AI models for anomaly detection → Visualizes the anomaly detection workflow.
key_equations:
  - equation: s(x,n) = 2^{-E(h(x))/c(n)}
    explanation: Anomaly score where values near 1 indicate an anomaly.
  - equation: y_t = c + φ_1 y_{t-1} + ... + φ_p y_{t-p} + θ_1 ε_{t-1} + ... + θ_q ε_{t-q} + ε_t
    explanation: ARIMA model equation defining the time series forecast.
  - equation: f_t = σ(W_f ⋅ [h_{t-1}, x_t] + b_f)
    explanation: LSTM forget gate equation controlling information retention.
  - equation: \hat{y}_t = α⋅\hat{y}^{ARIMA}_t + (1−α)⋅\hat{y}^{LSTM}_t
    explanation: Weighted average combining ARIMA and LSTM forecasts.
definitions:
  - term: Isolation Forest
    definition: An anomaly detection algorithm that isolates outliers rather than profiling normal points.
  - term: ARIMA
    definition: AutoRegressive Integrated Moving Average model for time series forecasting.
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network for learning long-term dependencies.
  - term: LLM
    definition: Large Language Model, used here to generate natural language financial advice.
  - term: Cognitive biases
    definition: Systematic patterns of deviation from norm or rationality in judgment.
critical_citations:
  - "[Milano et al., 2020] — Survey of ethical challenges in recommender systems."
  - "[Chua et al., 2023] — Model for user acceptance of AI-generated investment advice."
  - "[Zatevakhina et al., 2019] — Recommender systems as foundation for intelligent financial platforms."
  - "[del Valle & Lara, 2024] — Analysis of personal autonomy in AI-powered recommender systems."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Provides an overview of financial recommendation systems and their applications.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies gaps such as lack of personalization and ethical considerations in current systems.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Uses user characteristics like risk level and goals to personalize recommendations.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: contextual
      justification: Discusses general user profiling but does not directly address cold-start.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Applies ARIMA and LSTM to forecast user spending.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Specifically compares and combines ARIMA and LSTM for spending forecasts.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Uses Isolation Forest to detect anomalous expenses.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Implements Isolation Forest as the core anomaly detection algorithm.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Emphasizes privacy and security using OAuth 2.0 and OWASP principles.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Stresses transparency and user autonomy to build trust.
  contribution: "This paper provides a blueprint for integrating multiple AI models (anomaly detection, forecasting, and LLM-based generation) into a modular financial advisory system. The architecture supports the development of Odin's recommendation and anomaly detection modules. The emphasis on ethical design, including user autonomy and transparency, aligns with Odin's need for user trust. The system's ability to generate personalized advice based on user-specific data directly informs Odin's budget recommendation and behavioral profiling components."
  directly_justifies:
    - "Combining ARIMA and LSTM improves forecast accuracy for user spending."
    - "Isolation Forest can effectively identify anomalous financial transactions."
    - "LLMs can generate personalized financial recommendations from structured user data."
    - "Ethical design principles are essential for user acceptance of AI financial advice."
    - "A modular architecture facilitates integration of different AI components."
  limits:
    - "The study does not provide empirical evaluation metrics (e.g., RMSE, F1-score) for the models used."
    - "User testing and validation of the recommendation system's effectiveness are not reported."
    - "The system's performance across diverse income levels is claimed but not empirically demonstrated."
    - "The LLM component's recommendation quality is not compared against other baselines."
    - "The paper lacks a discussion on the system's scalability with a large number of users."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. Domains flagged as relevant include 'Existing Systems & Gaps' (4.A, 4.B) due to the paper's review of financial RS and identified limitations; 'Behavioral Profiling & Classification' (5.A, 5.B) because it uses user characteristics for personalization; 'Spending Forecasting' (6.A, 6.B) as a core contribution; 'Anomaly Detection' (8.A, 8.B) as another core algorithmic contribution; and 'Data Privacy & User Trust' (10.A, 10.B) because of the strong ethical focus. The paper was considered and rejected for 'Filipino Cultural Context' (2.A-D) as it is international and does not discuss Filipino-specific practices. 'Budget Recommendation' (7.A-D) was noted as contextual because the LLM generates advice but does not formulate it as a constrained optimization problem. The paper is highly relevant for informing Odin's algorithmic design and ethical framework, providing concrete methods for forecasting and anomaly detection."
limitations:
  - "No quantitative evaluation of the system's performance is provided. [unacknowledged]"
  - "The effectiveness of the LLM-generated recommendations is not empirically validated with users. [unacknowledged]"
  - "The system is tested but results are not shared, limiting reproducibility. [unacknowledged]"
  - "The paper does not address potential biases in the AI models or training data. [unacknowledged]"
remember_this:
  - "Combines Isolation Forest, ARIMA, LSTM, and LLMs for financial advice."
  - "Emphasizes user autonomy and ethical AI design principles."
  - "Modular architecture ensures independence of AI and core modules."
  - "Aims to counter cognitive biases and manipulative marketing."
  - "Does not provide quantitative performance metrics for its models."
```
---

## Paper 21: Chatterjee & Das_summarized.md

**Source File:** `Chatterjee & Das_summarized.md`

```yaml
paper_id: 10.60087/jklst.v4.n1.012
designation: international-algorithm-specific
title: Adaptive Financial Recommendation Systems Using Generative AI and Multimodal Data
authors: Chatterjee, P.; Das, A.
year: 2024
venue: Journal of Knowledge Learning and Science Technology
odin_topics:
  - 1.C
  - 5.A
  - 6.A
  - 7.B
  - 8.A
  - 10.A
  - 10.B
  - 12.A
  - 12.B
  - 12.C
tldr: Generative AI framework using LLMs and multimodal data for personalized financial product recommendations, achieving up to 30% improvement in relevance and 25% increase in user engagement over traditional baselines.
problem_and_motivation: Traditional financial recommendation engines rely on static rules or shallow models that fail to adapt to dynamic consumer behavior, life events, and non-numeric signals like intent or financial literacy. There is a need for systems that are deeply personalized, context-aware, and responsive to real-time changes in user financial behavior.
approach:
  - Data ingestion layer processes structured data (transaction logs, credit history) and unstructured data (chat transcripts, surveys) from mobile apps and APIs.
  - User profiling engine uses unsupervised learning to cluster personas and dynamically account for financial volatility, risk perception, and behavioral shifts.
  - Generative model layer fine-tunes LLMs prompted with user context and financial goals to generate scenario-specific product narratives.
  - Recommendation refinement module uses GANs or policy-gradient models to evaluate and refine outputs for coherence, accuracy, and regulatory alignment.
  - Reinforcement learning loop implements RLHF using user feedback to tune model weights over time for personalization and drift correction.
  - Ethical and XAI layer applies SHAP, LIME, and counterfactual testing for fairness auditing and compliance, generating visual dashboards for interpretability.
  - System architecture supports modular integration with digital banking APIs and deployment across neobanks and financial wellness apps.
  - Evaluation uses synthetic yet realistic datasets from the AlphaCredit Persona Generator Toolkit, benchmarked against collaborative filtering and neural recommender baselines.
findings:
  - num: 28-35% improvement in Top-N precision and recall for the GenAI system compared to traditional models.
  - num: 22% increase in engagement duration for models trained with feedback loops.
  - num: 18% higher acceptance of recommended financial products with feedback integration.
  - num: 36% reduction in product rejection rate compared to models without feedback integration.
  - num: 23% reduction in disparate impact scores when fairness constraints are applied.
  - num: 18% increase in equal opportunity scores with fairness constraints versus unconstrained baseline.
  - Users exposed to transparent, data-backed recommendations showed a 40% higher engagement rate compared to those receiving opaque suggestions.
  - The system demonstrated high personalization accuracy in cold-start scenarios where traditional models often fail.
  - The proposed framework reduces bias and improves fairness metrics through preprocessing and optimization constraints.
  - Explainability modules enhance user trust and regulatory compliance in financial AI deployments.
key_figures_tables:
  - Figure 1: Simulated User Cohorts → Visualization of five distinct simulated user persona groups for testing.
  - Figure 2: Evaluation Metrics Performance Scores → Quantitative comparison of key performance metrics across evaluation dimensions.
  - Figure 3: Result and Analysis Metrics Overview → Summary of personalization accuracy, fairness, and transparency results.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: GenAI
    definition: Generative Artificial Intelligence; AI systems capable of generating new content based on training data.
  - term: LLM
    definition: Large Language Model; a type of AI model trained on vast text data to understand and generate human-like language.
  - term: RLHF
    definition: Reinforcement Learning from Human Feedback; a technique using human preferences as a reward signal to train AI models.
  - term: GAN
    definition: Generative Adversarial Network; a class of machine learning frameworks where two neural networks contest with each other.
  - term: XAI
    definition: Explainable AI; a set of processes and methods that allows human users to understand and trust the results and output created by machine learning algorithms.
  - term: SHAP
    definition: SHapley Additive exPlanations; a method based on cooperative game theory to explain the output of machine learning models.
  - term: LIME
    definition: Local Interpretable Model-agnostic Explanations; an algorithm to explain the predictions of any classifier or regressor.
  - term: EaaS
    definition: Explainability-as-a-Service; a modular deployment of explainability components as a separate microservice.
critical_citations:
  - "[Ribeiro et al., 2016] — Foundational for model-agnostic explainability (LIME)."
  - "[Mehrabi et al., 2021] — Core reference for bias and fairness in machine learning."
  - "[Chien et al., 2022] — Relevant for deep learning in financial product recommendations."
  - "[Ghosh et al., 2023] — Key for explainable AI techniques specifically in finance."
  - "[Das et al., 2020] — Critical for fairness metrics and explanation methods in financial services."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: contextual
      justification: Provides framework for behavioral profiling and spending analysis.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly proposes dynamic behavioral segmentation and user profiling engine.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Uses time-series modeling and user embeddings for adaptive forecasting.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: Proposes GenAI-based product recommendation akin to budget allocation advice.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Discusses detection of anomalous behaviors and cold-start handling.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Embeds differential privacy and federated learning principles for privacy.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Uses explainability and transparency to build and measure user trust.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Establishes comprehensive KPIs for quantitative and qualitative evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Benchmarks GenAI against collaborative filtering, matrix factorization, and neural networks.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Uses relevance scoring and engagement metrics applicable to budget recommendation.
  contribution: "This paper provides a full-stack blueprint for implementing a GenAI-powered financial recommendation engine for Odin, covering data ingestion, behavioral profiling, generative recommendation, reinforcement learning from feedback, and explainable AI layers. The architectural design directly informs the development of Odin's budget recommendation and personalization modules. The emphasis on ethical AI, privacy-preserving techniques, and bias mitigation aligns with Odin's need for user trust and regulatory compliance. The proposed XAI layer offers a method for generating user-friendly justifications for recommendations, which is crucial for Odin's transparency goals. The modular architecture supports integration with Odin's existing or planned mobile-first infrastructure."
  directly_justifies:
    - "Generative AI framework outperforms traditional models in cold-start scenarios for financial recommendations."
    - "User feedback loops improve long-term recommendation relevance and engagement by 18-36%."
    - "Explainability layers are critical for building user trust and ensuring regulatory compliance in fintech."
    - "Fairness-aware modeling reduces disparate impact by 23% in simulated financial recommendation settings."
    - "Multimodal data integration enhances contextual understanding of user financial behavior."
  limits:
    - "Use of synthetic datasets limits validation of privacy and fairness claims in real-world scenarios."
    - "Lack of real demographic identifiers in datasets constrains precise fairness validation."
    - "Trade-offs between model accuracy and fairness constraints remain underexplored in production environments."
    - "Intersectional fairness considering combined attributes needs further research."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant to domains including Filipino Financial Behavior, Spending Forecasting, Budget Recommendation, Anomaly Detection, Data Privacy, User Trust, and System Evaluation. Specific topic codes selected were: 1.C (contextual as it informs financial behavioral analysis), 5.A (high, direct proposal of a user profiling engine), 6.A (high, uses time-series modeling for prediction), 7.B (high, GenAI-based product recommendation akin to budget allocation), 8.A (medium, discusses anomaly behavior detection), 10.A (high, embeds privacy-preserving methods), 10.B (high, uses explainability for trust), 12.A (high, establishes comprehensive evaluation KPIs), 12.B (high, benchmarks against baselines), and 12.C (medium, uses relevance and engagement metrics). Borderline cases included the paper's financial behavior analysis touching 1.C and 5.A, resolved by selecting 5.A as primary and 1.C as contextual. The spending pattern analysis on seasonal spending could relate to 2.B, but the paper does not specifically address cyclical patterns or Filipino cultural context, so 2.B was rejected. Similarly, topics under Savings & Debt Management (13.A, 13.B, 13.C) were rejected as the paper focuses on product recommendations rather than goal management or surplus allocation. The overall relevance to Odin is high, providing a comprehensive architectural framework for personalization, recommendation, and ethical AI compliance."
limitations:
  - "Absence of real demographic identifiers in anonymized datasets limits precise fairness validation. [unacknowledged]"
  - "Trade-offs between model accuracy and fairness constraints need further exploration in production environments. [acknowledged]"
  - "More research is needed to account for intersectional fairness in bias assessment. [acknowledged]"
  - "Reliance on synthetic datasets may not fully capture the complexity of real-world financial behaviors. [unacknowledged]"
remember_this:
  - "Generative AI improves financial recommendation relevance by up to 30% over traditional methods."
  - "User feedback loops increase engagement duration by 22% and reduce rejection rates by 36%."
  - "Fairness constraints reduce disparate impact by 23% without sacrificing recommendation accuracy."
  - "Explainability and transparency are critical for building user trust and regulatory compliance."
  - "Modular architecture with RLHF enables continuous personalization and adaptation to user drift."
```
---

## Paper 22: Garg et al-2024_summarized.md

**Source File:** `Garg et al-2024_summarized.md`

```yaml
paper_id: 10.63282/3050-9246.IJETCSIT-V5I3P105
designation: international-algorithm-specific
title: A Multi-Layered AI-IoT Framework for Adaptive Financial Services
authors: Garg, A.; Pandey, M.; Pathak, A. R.
year: 2024
venue: International Journal of Emerging Trends in Computer Science and Information Technology
odin_topics:
  - 4.A
  - 4.B
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 12.A
  - 12.B
  - 13.A
tldr: An AI-IoT framework with input, intelligence, and experience layers provides real-time, adaptive, and personalized banking services using edge computing and federated learning.
problem_and_motivation: Traditional banking systems cannot effectively act upon rich contextual data from IoT devices. A unified framework for AI-IoT integration is missing, which hinders real-time personalization and fraud detection. This gap limits the delivery of intelligent and secure financial experiences.
approach:
  - The paper employs a design science methodology to construct a conceptual framework for AI-IoT integration in banking.
  - The framework consists of three layers: Input (IoT endpoints), Intelligence (AI analytics), and Experience (service delivery).
  - The architecture incorporates edge computing to reduce latency and federated learning to enhance privacy.
  - A zero-trust security model is integrated, and use cases are analyzed to demonstrate feasibility.
  - Evaluation is conducted via a comparative simulation of operational logs over a 12-month period.
findings:
  - num: Fraud detection accuracy improved from 60% to 89% after AI-IoT deployment.
  - num: False positive rate for fraud detection decreased from 39% to 11%.
  - num: Customer Satisfaction Index increased from 72 to 86 out of 100.
  - num: Average response latency for decisioning operations dropped from 2.3 seconds to 0.8 seconds.
  - The initial investment in the AI-IoT infrastructure was recovered within eight months.
  - The churn rate decreased by 14% following the implementation.
key_figures_tables:
  - Table 1: Applications of IoT and AI in Banking → Summarizes use cases like smart ATMs and fraud detection.
  - Table 2: Traditional Banking vs. AI-IoT Integrated Banking Systems → Highlights key differences in personalization and decision-making.
  - Figure 1: Architectural Model → Visualizes the three-layer Input, Intelligence, Experience framework.
  - Figure 2: Comparison of Fraud Incidents Before and After AI-IoT Implementation → Illustrates a hypothetical reduction in fraud cases.
  - Table 3: Real-World Applications of AI-IoT Convergence in Banking → Maps use cases to IoT role, AI enhancement, and banking impact.
key_equations:
  - equation: "$CRS_i = \sum_{j=1}^{n} w_j \cdot f_j(x_i)$"
    explanation: Defines a dynamic credit risk score based on weighted behavioral features.
  - equation: "$A(x) = \frac{||x - \mu||^2}{\sigma^2}$"
    explanation: Computes an anomaly score to detect potential fraud in transactions.
  - equation: "$\omega_t = \omega_{t-1} - \eta \cdot \frac{1}{K} \sum_{k=1}^{K} \nabla \iota_k(\omega)$"
    explanation: Shows federated learning update for model weights without centralizing data.
definitions:
  - term: IoT
    definition: Internet of Things, a network of physical devices that collect and exchange data.
  - term: AI
    definition: Artificial Intelligence, the simulation of human intelligence in machines.
  - term: Federated Learning
    definition: A machine learning approach that trains models across decentralized devices holding local data samples.
  - term: Zero-Trust Architecture
    definition: A security model that requires strict identity verification for every user and device trying to access resources.
  - term: Edge Computing
    definition: Data processing performed at the periphery of the network, closer to the data source.
critical_citations:
  - "[Baker and Georgakopoulos, 2019] — Foundational for IoT-enabled intelligent banking."
  - "[Yu et al., 2021] — Key for privacy-preserving federated learning in finance."
  - "[Wang and Xu, 2021] — Core reference for AI-enhanced fraud detection with IoT data."
  - "[Autade, 2023] — Cited for real-time anomaly detection in financial streams."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: The paper reviews the landscape of digital and IoT-driven banking systems.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies fragmentation and lack of integration as a key barrier to unified intelligent banking.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Discusses predictive analytics for credit scoring, fraud detection, and forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: contextual
      justification: Mentions transaction forecasting with predictive analytics but not as the central focus.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly addresses real-time fraud detection and anomaly detection in banking.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Applies ML anomaly detection algorithms to financial transaction data.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Framework supports mobile banking experiences with real-time, context-aware services.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: contextual
      justification: Mentions mobile push notifications and app interfaces but does not focus on UX design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Dedicated section on security and privacy issues like data breaches and AI ethics.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Emphasizes building trust through zero-trust architecture and explainable AI.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Hyper-personalization and emotion-aware support aim to increase engagement.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: Results show decreased churn rate due to personalization and proactive support.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses fraud detection, latency, and customer satisfaction as evaluation metrics.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: contextual
      justification: The paper evaluates AI modules like anomaly detection as part of the overall system.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: contextual
      justification: Mentions budgeting and spending suggestions but savings goals are not the focus.
  contribution: The paper provides a layered architectural blueprint for integrating AI and IoT into banking systems. This framework justifies Odin's need for a real-time, adaptive intelligence layer to process user data. The use of edge computing and federated learning offers a viable model for handling latency and privacy concerns. The emphasis on zero-trust security aligns with Odin's requirement for robust data protection. Finally, the paper's findings on fraud detection and personalization validate the strategic importance of these features.
  directly_justifies:
    - "A real-time anomaly detection system using IoT behavioral data and AI can achieve 89% fraud detection accuracy."
    - "Processing data at the edge reduces decision latency from 2.3 to 0.8 seconds for financial operations."
    - "Federated learning enables model training on user devices without moving sensitive raw data to central servers."
    - "Hyper-personalized, context-aware mobile notifications significantly improve customer satisfaction and reduce churn."
  limits:
    - "The framework is conceptual; its quantitative benefits are derived from a hypothetical simulation."
    - "Real-world challenges like legacy infrastructure integration are mentioned but not deeply analyzed."
    - "The security and privacy solutions are proposed but not empirically validated within the context of the framework."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was conducted. The domains of Existing Systems & Gaps (4.A, 4.B), Anomaly Detection (8.A, 8.B), and Data Privacy & User Trust (10.A, 10.B) were flagged as high relevance due to the paper's direct focus on system integration, real-time fraud detection, and security architecture. Medium relevance was assigned to Predictive Modeling (6.A), Mobile-First Design (9.A), and User Retention (11.A, 11.B) as the paper discusses these components but not as primary contributions. The paper was considered and rejected for codes under Behavioral Profiling & Classification (5.A-C) as its focus is on system architecture and fraud detection, not on classifying user financial profiles. The contribution is highly relevant to Odin as it validates the need for a layered, intelligent, and secure PFMS architecture with real-time capabilities.
limitations:
  - "The framework's validity is demonstrated primarily through hypothetical simulations and use cases."
  - "The paper focuses on a general banking context, not specifically on personal finance management for individuals."
  - "A detailed cost-benefit analysis for the framework in a PFMS setting is not provided. [unacknowledged]"
  - "The paper does not address the cold-start problem for anomaly detection or profiling. [unacknowledged]"
remember_this:
  - "An AI-IoT framework improved fraud detection accuracy by 48% in a simulated banking scenario."
  - "Edge computing is critical for reducing latency in real-time financial services."
  - "Federated learning is a promising technique for preserving data privacy in PFMS."
  - "The AI-IoT convergence is a strategic evolution towards adaptive and autonomous financial services."
  - "Zero-trust architecture and explainable AI are essential for building user trust."
```
---

## Paper 23: Wu X. et al_summarized.md

**Source File:** `Wu X. et al_summarized.md`

```yaml
paper_id: "10.3390/app14156578"
designation: "international-algorithm-specific"
title: "Optimizing Recurrent Neural Networks: A Study on Gradient Normalization of Weights for Enhanced Training Efficiency"
authors: "Wu, X.; Xiang, B.; Lu, H.; Li, C.; Huang, X.; Huang, W."
year: 2024
venue: "Applied Sciences"
odin_topics:
  - "6.A"
  - "6.B"
  - "8.A"
  - "8.B"
  - "12.B"
tldr: "Weight gradient normalization suppresses vanishing and exploding gradients in RNNs, improving training stability and convergence across language, time-series, and image tasks."
problem_and_motivation: "RNNs suffer from vanishing and exploding gradients due to weight reuse and nonlinear activations, hindering training. Existing solutions like gradient clipping and batch normalization have limitations in RNNs, lacking effective mathematical explanations. A gradient normalization method is needed to stabilize training without altering model structure."
approach:
  - "Proposes Weight Gradient Normalization (WGN) that subtracts gradient mean and divides by standard deviation per iteration, controlling the linear change of weight variance."
  - "Applies WGN to RNN and LSTM models with single and two layers, using tanh and ReLU activations."
  - "Evaluates on MNIST (image classification), PTB (language modeling), ETTm1 (time series forecasting), and UCR (time series classification) datasets."
  - "Compares against standard SGD, and uses a proposed LOE metric to quantify gradient anomaly severity."
  - "Analyzes hyperparameter sensitivity for η (0.0001–0.005) and δ (1e-7 to 1e-4)."
findings:
  - "num: WGN achieves perplexity 110.89 on PTB, an 11.48% improvement over SGD."
  - "num: On ETTm1, MAE values of 0.778 (24-step) and 0.592 (96-step) improve by 3.00% and 6.77% over SGD."
  - "num: UCR classification accuracy improves by 0.4% to 6.0% with WGN."
  - "WGN reduces LOE (loss explosion indicator) significantly, indicating fewer gradient anomalies."
  - "WGN stabilizes weight variance and neuron output variance, leading to smoother training curves."
  - "Ablation shows that normalizing all weights (W_ih, W_hh, W_fc) yields best LSTM accuracy on MNIST."
  - "WGN is sensitive to learning rate; optimal η ranges vary by model and dataset."
key_figures_tables:
  - "Table 1: Ablation accuracy for WGN on different weights → best performance when normalizing all weights in LSTM."
  - "Table 2: Hyperparameter sensitivity of η and δ → optimal η=0.001 for RNN, 0.005 for LSTM on MNIST."
  - "Figure 4: Variance of weights and neuron outputs with/without WGN → WGN yields linear variance increase."
  - "Figure 5: Training curves on MNIST → WGN reduces loss spikes and accelerates convergence."
key_equations:
  - equation: "params = params - η * (params.grad - params.grad_mean) / (params.grad_std + δ)"
    explanation: "WGN update rule normalizes gradients by mean and std."
  - equation: "LOE = |(loss_t - loss_{t-1}) / (loss_{t-1} + α)| * exp(epoch / total_epoch)"
    explanation: "Metric quantifies gradient problem severity."
definitions:
  - term: "WGN"
    definition: "Weight Gradient Normalization, a method that normalizes weight gradients by their mean and standard deviation."
  - term: "LOE"
    definition: "Loss Explosion Indicator, a metric for gradient problem severity."
  - term: "RNN"
    definition: "Recurrent Neural Network, a neural network with cyclic connections for sequential data."
  - term: "LSTM"
    definition: "Long Short-Term Memory, an RNN variant with gated memory cells."
  - term: "PTB"
    definition: "Penn Treebank, a language modeling dataset."
critical_citations:
  - "[Bengio et al., 1994] — foundational work on vanishing gradients in RNNs."
  - "[Pascanu et al., 2013] — formalized exploding gradients and clipping solutions."
  - "[Cooijmans et al., 2016] — showed batch normalization can benefit RNNs."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "contextual"
      justification: "Demonstrates RNN forecasting improvements but not on financial data."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "contextual"
      justification: "WGN enhances sequence prediction, applicable to spending forecasting."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "contextual"
      justification: "Improved RNN stability could benefit anomaly detection in spending."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "contextual"
      justification: "Provides algorithmic improvement for sequential anomaly detection."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "contextual"
      justification: "Introduces LOE metric for evaluating gradient stability in RNNs."
  contribution: "This paper does not directly address PFMS but provides a method for improving RNN training that could be integrated into Odin's spending forecasting and anomaly detection modules. Its LOE metric offers a way to evaluate training stability of sequential models. However, the absence of financial domain data limits direct applicability. The findings on convergence speed and accuracy may inform choice of training techniques for Odin's predictive models."
  directly_justifies:
    - "WGN reduces perplexity in language modeling, suggesting improved sequence prediction capability."
    - "WGN accelerates convergence and reduces loss spikes in time-series forecasting."
    - "The LOE metric can be used to monitor gradient stability during training of Odin's models."
    - "Hyperparameter sensitivity indicates careful tuning is needed for optimal performance."
  limits:
    - "Not evaluated on financial spending data, limiting direct translation to Odin."
    - "Computational overhead of WGN is 7-8 times that of SGD, impacting real-time use."
    - "May not perform well on small datasets due to batch size limitations, a concern for sparse financial data."
    - "Sensitivity to learning rate requires extensive tuning for each dataset and model."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was found relevant only to domains involving sequential modeling: predictive modeling (6.A, 6.B) and anomaly detection (8.A, 8.B) because it improves RNN/LSTM training for sequence tasks. The evaluation domain (12.B) was also flagged because the proposed LOE metric provides a new evaluation approach for algorithmic stability. All other domains—Filipino cultural context, expense categorization, existing systems, behavioral profiling, budget recommendation, mobile design, data privacy, user retention, savings/debt management—were considered and rejected because the paper does not address any of these aspects; it is purely a machine learning methodology paper. Borderline cases: the paper's time-series forecasting could touch on spending cycles (2.B) or seasonal patterns (2.D), but it does not use financial data or discuss cyclical spending, so those were excluded. Overall relevance to Odin is contextual, providing foundational training techniques that could be adapted but not directly applied."
limitations:
  - "WGN did not improve accuracy in single-layer RNN on MNIST, indicating limited benefit for shallow architectures."
  - "On small datasets (e.g., UCR subsets), WGN sometimes decreased accuracy or increased LOE, suggesting over-adjustment."
  - "Time complexity increases by 7-8 times compared to SGD, which may be prohibitive for real-time applications."
  - "The method's effectiveness depends heavily on hyperparameter tuning; no universal optimal settings are provided. [unacknowledged]"
  - "No evaluation on personal finance data, so transferability to Odin's spending datasets is unverified. [unacknowledged]"
remember_this:
  - "WGN improves PTB perplexity by 11.48% and ETTm1 MAE by up to 6.77%."
  - "Weight gradient normalization stabilizes variance and reduces training spikes."
  - "WGN is sensitive to learning rate and batch size, requiring careful tuning."
  - "The LOE metric quantifies gradient anomaly severity during training."
  - "WGN accelerates convergence in LSTM and RNN models across multiple tasks."
```
---

## Paper 24: Yadav et al_summarized.md

**Source File:** `Yadav et al_summarized.md`

```yaml
paper_id: 4b5a7d6e-8f9c-4a1b-9d3e-8f2a5c1e7d4b
designation: international-algorithm-specific
title: AI Wealth Navigator: An Integrated Platform for Smart Budgeting, Financial Learning, and Personalized Policy Guidance
authors: Yadav, A.; Prakash, R. S.; Iqubal, S. M.; Gebremicahea, M. G.
year: 2024
venue: Unknown
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 6.A
  - 7.A
  - 7.B
  - 8.A
  - 9.A
  - 9.B
  - 10.A
  - 11.A
  - 12.A
tldr: Integrates AI-driven budgeting, adaptive financial learning, and policy recommendations into a unified platform for personal finance management.
problem_and_motivation: Users face fragmented financial ecosystems where budgeting, education, and policy knowledge are disjointed. Low financial literacy in India exacerbates poor decision-making on savings, investments, and government benefits. A unified, intelligent platform is needed to bridge these gaps and promote financial inclusion.
approach:
  - System uses Next.js frontend with Supabase and Prisma for data management.
  - Inngest handles automated tasks and notifications for background processes.
  - Gemini LLM powers personalized financial recommendations and adaptive learning.
  - Policy recommendation engine uses hybrid data APIs to suggest government schemes.
  - Arcjet ensures secure data handling and transaction encryption.
  - Evaluation involved human assessment by 50 users and system performance metrics.
findings:
  - num: Receipt scanner achieved 94% accuracy on digital and physical receipts.
  - num: Average user ratings were 4.8/5 for budgeting insights, 4.7/5 for policy, and 4.6/5 for learning.
  - num: Over 70% of users discovered previously unknown government programs.
  - Arcjet blocked all simulated security threats during testing.
  - Integration of three domains into one platform eliminated the need for multiple apps.
key_figures_tables:
  - Figure 1.1: System layered architecture showing frontend, backend, AI, and security components → Modular design separates core functions for scalability.
  - Figure 1.2: Detailed architecture diagram with data flow between modules → Highlights integration of LLM, APIs, and user interface.
  - Figure 1.3: Sequence diagram of user interactions → Illustrates real-time data flow and response generation.
  - Figure 1.4: Dashboard interface → Shows visual spending analytics and budget tracking tools.
  - Figure 1.5: Transaction page with receipt scanner → Demonstrates OCR-based expense entry.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: LLM
    definition: Large Language Model used for generating personalized financial insights.
  - term: OCR
    definition: Optical Character Recognition used for scanning and digitizing receipts.
  - term: API
    definition: Application Programming Interface for data exchange between system components.
critical_citations:
  - "[Patel et al., 2023] — AI platforms improve financial literacy with personalized paths."
  - "[Kumar et al., 2023] — Dynamic budgeting systems enhance user engagement."
  - "[Lee et al., 2023] — AI suggests social benefits based on financial profiles."
  - "[Gupta et al., 2024] — AI secures transactions and detects fraud."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Provides AI-driven budget tracker with receipt scanning for automated categorization.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: Discusses receipt scanner accuracy and structured transaction logs.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Explicitly surveys fragmented existing systems and proposes a unified alternative.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies gaps in integration, literacy, and policy access in current apps.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: low
      justification: Mentions predictive financial planning as future work, not implemented.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Offers personalized savings alerts and dynamic recommendations based on spending habits.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: Gemini LLM provides tailored budgeting insights and investment advice.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Security evaluation mentions fraud detection but not as a primary focus.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Frontend uses responsive design for mobile and desktop, with dark/light mode.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Interface includes visual dashboards and interactive tools, but mobile-specific UX not detailed.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Arcjet ensures encryption, secure data handling, and threat prevention.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: User ratings (4.7–4.8/5) indicate trust in relevance and empathy of recommendations.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Gamified learning modules and real-time insights support sustained user engagement.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: Adaptive roadmap and policy alerts keep users returning for new recommendations.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Uses both quantitative performance metrics (response time, token efficiency) and human evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Evaluates receipt scanner accuracy and LLM response quality.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: contextual
      justification: Human ratings provide qualitative assessment but no benchmark comparison.
  contribution: "The paper directly supports Odin's Budget Recommendation module (7.B) by demonstrating a unified AI platform that integrates Gemini LLM for personalized budgeting insights and real-time spending analytics. For Expense Categorization (3.A/3.B), the receipt scanner with 94% accuracy provides a benchmark for automated transaction logging. The system's modular architecture and security measures (Arcjet) inform Odin's Mobile-First Design (9.A/9.B) and Data Privacy (10.A) considerations. Additionally, the evaluation framework using both system metrics and user ratings (4.8/5) offers a template for Odin's System Evaluation (12.A)."
  directly_justifies:
    - "AI-driven platforms can close financial literacy gaps and empower low-income communities."
    - "LLM-based systems provide context-aware, personalized financial recommendations."
    - "Integrating budgeting, education, and policy into one ecosystem improves user experience."
    - "Automated receipt scanning reduces manual entry errors and increases adoption."
    - "Multi-layer security is essential for protecting personal financial data."
  limits:
    - "Study conducted with only 50 Indian users, may not generalize to Filipino context."
    - "No longitudinal data on behavior change or retention over time."
    - "Dependence on full user profiles for policy matching may raise privacy concerns [unacknowledged]."
    - "Sporadic OCR errors mentioned as a drawback but not quantified in detail."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains of Expense Categorization, Existing Systems & Gaps, Budget Recommendation, Data Privacy, and System Evaluation were flagged as highly relevant, as the paper directly addresses these with algorithmic contributions and evaluation metrics. Behavioral Profiling (5.A) and Forecasting (6.A/6.B) were considered but rejected due to only cursory mentions (forecasting as future work, no behavioral classification). Anomaly Detection (8.A) was marked contextual because security evaluation touched on fraud prevention but without algorithmic detail. Mobile-First Design (9.A/9.B) was medium relevance due to the mention of responsive design but lack of in-depth UX analysis. Filipino-specific topics (2.A-2.D) were rejected entirely as the study is based in India and does not address Filipino cultural contexts. Overall, the paper is highly relevant for its integrated AI architecture, but its international algorithm-specific focus limits direct applicability to Odin's Philippine-centric design."
limitations:
  - "Limited user sample (n=50) and geographic scope (India)."
  - "No comparison against existing baseline systems or benchmarks."
  - "Relies on proprietary Gemini LLM, limiting reproducibility."
  - "Policy recommendation engine not evaluated for correctness or coverage."
  - "Long-term user retention and behavior change not assessed. [unacknowledged]"
remember_this:
  - "Unified platform combines budgeting, learning, and policy into one system."
  - "Receipt scanner achieves 94% accuracy on diverse receipt types."
  - "User ratings averaged 4.8/5 for budgeting insights and 4.7/5 for policy."
  - "Arcjet provides API-layer threat prevention and data encryption."
  - "Over 70% of users discovered new government programs through the engine."
```
---

## Paper 25: Pratama & Putri_summarized.md

**Source File:** `Pratama & Putri_summarized.md`

```yaml
paper_id: 10.47738/ijaim.v4i4.92
designation: international-algorithm-specific
title: User Profiling Based on Financial Transaction Patterns: A Clustering Approach for User Segmentation
authors: Pratama, S. F.; Putri, N. A.
year: 2024
venue: International Journal for Applied Information Management
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 12.B
tldr: Clustering financial transaction data by amount, time, and type reveals three user segments with distinct spending behaviors, supporting personalized financial services.
problem_and_motivation: Traditional user segmentation methods relying on historical data fail to capture evolving behaviors and the nuances of transaction patterns. This limits the effectiveness of personalized financial services and fraud detection. More advanced, data-driven techniques are needed to uncover hidden behavioral segments from transaction data.
approach:
  - Data from a Kaggle financial transactions dataset was preprocessed and features were extracted.
  - K-means clustering was applied using transaction amount, time, and type as key features.
  - Feature scaling and encoding were performed on numerical and categorical variables.
  - The Silhouette Score was used to evaluate cluster quality and the optimal number of clusters.
  - Clusters were visualized using 3D plots, PCA, and t-SNE projections for interpretation.
findings:
  - num: The clustering analysis revealed three distinct user clusters with a Silhouette Score of 0.33.
  - Cluster 0 performs moderate-value purchases (~1876.92) early in the week, around 11:15 AM.
  - Cluster 1 performs high-value transfers (~4147.06) mid-week, around 1:35 PM.
  - Cluster 2 performs moderate-value purchases (~1970.00) later in the week, around 11:20 AM.
  - The 3D, PCA, and t-SNE visualizations showed clear separation between the three clusters.
  - The moderate Silhouette Score indicates some overlap, suggesting room for improved clustering methodology.
  - The single-month dataset limits the generalizability of the findings to long-term trends.
key_figures_tables:
  - "Table 1: Cluster characteristics summary showing mean amount, hour, and day of week for each cluster → Three distinct behavioral segments identified."
  - "Figure 2: 3D clustering of users based on transaction patterns → Clusters are distinct in amount and time dimensions."
  - "Figure 3: Cluster distribution bar chart → Cluster 2 has the highest transaction volume, Cluster 0 the least."
  - "Figure 4: PCA projection of clustering results → Clusters show separation in reduced dimensional space."
  - "Figure 5: t-SNE projection of clustering results → Clusters demonstrate distinct groupings in a 2D space."
key_equations:
  - equation: d(x_i, C_j) = sqrt(sum_{k=1}^{n} (x_{i,k} - c_{j,k})^2)
    explanation: Euclidean distance used for K-means assignment.
  - equation: WCSS = sum_{i=1}^{K} sum_{x_i in C_k} (x_i, c_k)^2
    explanation: Objective function minimized by K-means.
definitions:
  - term: K-Means
    definition: A clustering algorithm that partitions data into K distinct clusters based on mean distances to centroids.
  - term: Silhouette Score
    definition: A metric evaluating cluster quality, ranging from -1 (poor) to 1 (excellent).
  - term: WCSS
    definition: Within-Cluster Sum of Squares, the objective function minimized in K-means.
  - term: PCA
    definition: Principal Component Analysis, a dimensionality reduction technique.
  - term: t-SNE
    definition: t-Distributed Stochastic Neighbor Embedding, a nonlinear dimensionality reduction technique.
critical_citations:
  - "[Zhao et al., 2021] — Proposes K-means for customer segmentation using transaction data."
  - "[Zhang et al., 2020] — Uses DBSCAN for fraud detection based on transaction patterns."
  - "[Komati, 2025] — Highlights the role of ML in real-time financial decision-making and segmentation."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly segments users into behavioral profiles based on transaction patterns.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: Discusses limitations of historical data, tangentially related to the cold-start issue.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Uses K-means clustering, a key classification approach for behavioral profiling.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Segmentation insights can inform predictive models for spending forecasting.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: low
      justification: Findings on spending patterns could inform budgeting strategies.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: User segmentation is a prerequisite for personalized budget recommendations.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Clustering can help establish baseline behaviors for anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Mentions fraud detection, but focuses on clustering, not anomaly detection specifically.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Evaluates the K-means clustering algorithm using the Silhouette Score.
  contribution: The paper provides a practical demonstration of K-means clustering for segmenting users based on financial transaction features, which directly supports the development of Odin's behavioral profiling module. Its findings on distinct spending patterns (e.g., high-value transfers vs. moderate purchases) offer a baseline for designing personalized budget recommendations and targeted financial advice. The identified limitations, such as the moderate Silhouette Score and single-month dataset, highlight areas for methodological improvement in Odin's clustering algorithms. This work justifies the use of unsupervised learning for initial user segmentation to overcome the cold-start problem in a PFMS.
  directly_justifies:
    - "Transaction amount, time, and type are key features for distinguishing user spending behavior."
    - "Clustering techniques like K-means can identify distinct user segments without predefined labels."
    - "A Silhouette Score of 0.33 indicates moderate cluster quality, suggesting a need for refinement."
    - "Limitations in clustering accuracy highlight the importance of exploring alternative algorithms like DBSCAN."
    - "Segmentation by transaction behavior enables the tailoring of personalized financial products and marketing."
  limits:
    - "The dataset's single-month duration limits the capture of seasonal or long-term behavior trends."
    - "The moderate Silhouette Score (0.33) suggests overlap between clusters and potential misclassification."
    - "The use of synthetic data from Kaggle may not fully represent real-world user behavior."
  mapping_rationale: "A systematic scan of all 12 functional domains and their topic codes was performed. The paper was flagged as highly relevant to 'Behavioral Profiling & Classification' (5.A, 5.C) due to its primary contribution of user segmentation via K-means. It shows medium relevance to 'Spending Forecasting' (6.A) and 'Budget Recommendation' (7.B) as segmentation is foundational for these tasks. Low relevance was assigned to 'Anomaly Detection' (8.A, 8.B) because clustering is discussed for segmentation, not for identifying outliers. The 'Evaluation' domain (12.B) is relevant as the study uses the Silhouette Score to assess its algorithmic module. Topics related to the Filipino cultural context, mobile design, data privacy, and debt management were considered and rejected, as the paper uses a generic international dataset and does not address these specific aspects. Overall, the paper is most valuable as a practical example of applying a specific clustering algorithm for user profiling, justifying its use in Odin's user onboarding and segmentation modules."
limitations:
  - "The dataset is limited to a single month, restricting the analysis of long-term trends and seasonality."
  - "The moderate Silhouette Score suggests cluster overlap and potential for improved separation."
  - "The study does not compare K-means with other clustering algorithms like DBSCAN or hierarchical clustering. [unacknowledged]"
  - "The use of synthetic data may limit the real-world applicability of the findings. [unacknowledged]"
remember_this:
  - "K-means clustering on transaction features reveals three distinct user spending segments."
  - "The Silhouette Score of 0.33 indicates moderate cluster quality, requiring methodological refinement."
  - "Transaction amount, time, and type are strong predictors of user behavior for segmentation."
  - "Segmentation by transaction patterns enables personalized financial services and marketing strategies."
```
---


---

## Agent Instruction

If the agent reading this document believes further context about a paper is needed, it may request the original converted markdown file (with the '_marked' suffix) from the user for the relevant paper(s).
