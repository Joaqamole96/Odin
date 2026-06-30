# Compiled Research Summaries

## Filters Applied

- Designation: `international-algorithm-specific`

**Total Papers:** 25

**Note:** Included papers positions 26 to 50, Sorted by year.

---

## Paper 1: Yunita et al_summarized.md

**Source File:** `Yunita et al_summarized.md`

```yaml
paper_id: 10.1016/j.mex.2025.103462
designation: international-algorithm-specific
title: Performance analysis of neural network architectures for time series forecasting: A comparative study of RNN, LSTM, GRU, and hybrid models
authors: Yunita, A.; Pratama, M. I.; Almuzakki, M. Z.; Ramadhan, H.; Akhir, E. A. P.; Mansur, A. B. F.; Basori, A. H.
year: 2025
venue: MethodsX
odin_topics:
  - 6.A
  - 6.B
  - 8.B
  - 8.C
  - 12.A
  - 12.B
  - 12.C
tldr: Benchmarks nine RNN, LSTM, GRU, and hybrid architectures using Monte Carlo simulation across three datasets; Friedman test shows no statistically significant performance differences despite descriptive advantages for LSTM-based hybrids.
problem_and_motivation: The inherent variability in neural network performance due to random weight initialization raises concerns about the reliability and consistency of these architectures for time series analysis. Previous studies proposing hybrid models often train them only once, failing to account for performance variance. A systematic benchmark that evaluates model stability across multiple runs is needed to guide reliable architecture selection.
approach:
  - Evaluated nine architectures: vanilla RNN, LSTM, GRU, and six hybrids (RNN-LSTM, RNN-GRU, LSTM-RNN, GRU-RNN, LSTM-GRU, GRU-LSTM).
  - Used three real-world time series datasets: sunspot activity (monthly, n=3625), Indonesian COVID-19 cases (daily, n=634), and dissolved oxygen readings (daily, n=1033).
  - Implemented Monte Carlo simulation with 100 independent iterations per model, each with 100 training epochs, using a 70:30 or 80:20 train-test split.
  - Evaluated performance using MAE, MAPE, RMSE, and computation time, with results analyzed via 95% confidence interval trimming.
  - Applied the Friedman test as a non-parametric statistical comparison to assess performance differences across architectures and datasets.
findings:
  - num: The Friedman test revealed no statistically significant differences among the nine architectures (χ²=12.593, df=8, p=.127).
  - num: LSTM-GRU achieved the lowest mean rank (2.23) across all datasets, while vanilla RNN showed the highest (8.57).
  - num: For sunspot forecasting, LSTM-GRU had the lowest RMSE (23.205 ± 0.827), and GRU-LSTM achieved the best MAPE (36.242% ± 3.627%).
  - num: For COVID-19 case prediction, standalone LSTM performed best with the lowest MAPE (9.036% ± 0.778%) and competitive MAE (0.903 ± 0.091).
  - num: For dissolved oxygen forecasting, LSTM-RNN achieved the lowest MAE (2.970 ± 0.229) and RMSE (4.041 ± 0.242).
  - LSTM-based hybrid architectures consistently demonstrated superior descriptive performance and stability across datasets compared to single architectures.
  - Vanilla RNN exhibited the fastest computation time but showed the highest error rates and largest variance across all datasets.
  - The LSTM-RNN hybrid offered an optimal balance between prediction accuracy and computational efficiency.
  - Hybrid architectures generally outperformed single-architecture models in descriptive analysis.
key_figures_tables:
  - Table 1: Dataset characteristics including record counts, interval types, and value ranges → Provides context for evaluating model performance across diverse data distributions.
  - Table 2: Detailed architecture specifications with layer types and parameter counts → Shows the structural design and complexity of each benchmarked model.
  - Table 3: Performance comparison across all architectures with mean ranks → Demonstrates relative performance tiers despite non-significant statistical differences.
  - Table 4: Overall model rankings based on Friedman test → Shows LSTM-GRU as best performer (rank 2.23) and vanilla RNN as worst (rank 8.57).
  - Figure 4: Box plots of error metrics for sunspot dataset → Visualizes performance stability and variance across architectures.
  - Figure 6: Benchmark results for COVID-19 dataset → Shows vanilla LSTM's superior performance for epidemiological forecasting.
  - Figure 8: Evaluation metrics for oxygen dataset → Demonstrates LSTM-RNN's balanced accuracy and stability.
key_equations:
  - equation: "MAE = (1/n) Σ |y_i - ŷ_i|"
    explanation: Average magnitude of prediction errors in original units.
  - equation: "MAPE = (100/n) Σ |(y_i - ŷ_i) / y_i|"
    explanation: Scale-independent percentage error for comparing across magnitudes.
  - equation: "RMSE = sqrt((1/n) Σ (y_i - ŷ_i)²)"
    explanation: Penalizes larger errors heavily, sensitive to outliers.
  - equation: "h_t^R = g(W · x_t + U · h_{t-1}^R + b)"
    explanation: RNN hidden state update with activation function.
  - equation: "z_t = σ(W_xz x_t + W_hz h_{t-1} + b_z)"
    explanation: GRU update gate controlling information retention.
definitions:
  - term: RNN
    definition: Recurrent Neural Network; processes sequential data using hidden states that capture temporal dependencies.
  - term: LSTM
    definition: Long Short-Term Memory; RNN variant with cell state and three gates to address vanishing gradient and long-term dependencies.
  - term: GRU
    definition: Gated Recurrent Unit; LSTM variant with two gates (update and reset) offering simpler architecture.
  - term: Monte Carlo simulation
    definition: Probabilistic evaluation method using repeated random sampling to quantify model performance uncertainty.
  - term: Hybrid model
    definition: Neural network combining two different recurrent architectures in stacked configuration.
  - term: MAE
    definition: Mean Absolute Error; average absolute difference between predicted and actual values.
  - term: MAPE
    definition: Mean Absolute Percentage Error; relative error measure expressed as percentage.
  - term: RMSE
    definition: Root Mean Square Error; square root of average squared differences, penalizing larger errors.
  - term: Friedman test
    definition: Non-parametric statistical test comparing multiple models across datasets using rank-based analysis.
critical_citations:
  - "[Demšar, 2006] — Standard reference for statistical comparisons of classifiers."
  - "[Chung et al., 2014] — Empirical evaluation of GRU architecture and parameter efficiency."
  - "[Hochreiter & Schmidhuber, 1997] — Original LSTM paper establishing the architecture."
  - "[Le et al., 2024] — Prior use of Monte Carlo evaluation for neural network benchmarking."
  - "[Shewalkar et al., 2019] — Comparative analysis of RNN, LSTM, and GRU for speech recognition."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly benchmarks forecasting architectures applicable to spending prediction.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Evaluates RNN, LSTM, GRU, and hybrids specifically for time series forecasting.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Provides methodology for evaluating time series prediction stability that could extend to anomaly detection.
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: medium
      justification: Monte Carlo evaluation addresses model stability concerns relevant to cold-start scenarios.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Demonstrates systematic benchmarking methodology with multiple metrics and statistical testing.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides rigorous comparative evaluation of different neural network architectures.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Monte Carlo and Friedman test methodology applicable to budget recommendation evaluation.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Uses LSTM and RNN architectures that could be adapted for behavioral classification.
  contribution: This paper provides a validated benchmarking methodology for evaluating time series forecasting architectures that can directly inform Odin's spending forecasting module selection. The Monte Carlo evaluation framework offers a reliable approach to assess model stability, which is critical for financial prediction systems where prediction consistency is as important as accuracy. The comparative analysis shows that while statistical differences may be non-significant, LSTM-based hybrids offer practical advantages in stability across diverse data patterns, guiding Odin's architectural decisions for its predictive engine. The study's methodology for handling performance variance due to random initialization provides a template for Odin's model evaluation pipeline.
  directly_justifies:
    - Odin's forecasting module should evaluate models using Monte Carlo simulation across multiple runs to assess stability.
    - LSTM-based hybrid architectures offer practical advantages for spending prediction despite statistical equivalence.
    - The Friedman test provides an appropriate statistical framework for comparing forecasting architectures.
    - Vanilla RNN architectures are less reliable for time series forecasting in financial applications.
    - Hybrid LSTM-RNN and LSTM-GRU configurations provide optimal balance of accuracy and efficiency.
  limits:
    - The study uses only three datasets, limiting the generalizability of findings to spending data specifically.
    - The COVID-19 and oxygen datasets are non-financial, reducing direct applicability to personal finance forecasting.
    - Models were evaluated only on univariate time series, whereas financial data often includes multiple features.
    - The study did not investigate optimal hyperparameter tuning for each architecture individually. [unacknowledged]
    - The computational constraints of the hybrid models in mobile-first applications were not explored. [unacknowledged]
    - Only two hidden layers were used for all architectures, potentially limiting performance of deeper models.
  mapping_rationale: The systematic scan across all 12 functional domains identified high relevance primarily in Predictive Modeling (6.A, 6.B) and System Evaluation (12.A, 12.B, 12.C) because the paper directly benchmarks forecasting architectures and provides rigorous evaluation methodology. Medium relevance was assigned to Anomaly Detection (8.B, 8.C) due to the shared methodological concerns of temporal pattern prediction and cold-start stability. Low relevance was assigned to Behavioral Profiling (5.C) as the architectures could be adapted for classification tasks. Domains concerning Filipino cultural context (2.A-D), expense categorization (3.A-C), existing systems (4.A-B), budgeting strategies (7.A-D), mobile design (9.A-B), data privacy (10.A-B), user retention (11.A-B), and savings/debt management (13.A-C) were rejected because the paper focuses solely on algorithmic performance without addressing financial context, user behavior, or practical financial management applications. The overall relevance is medium: the paper provides valuable methodological guidance for evaluating forecasting models but lacks direct application to Filipino young professional spending or financial management tasks. Borderline cases included the applicability to cold-start scenarios (8.C) due to the stability assessment, and to classification approaches (5.C) due to potential adaptation of the same neural architectures.
limitations:
  - Statistical significance was not achieved due to limited sample size of only three datasets.
  - Findings are based on non-financial datasets (sunspot, COVID-19, oxygen), limiting direct applicability to spending data.
  - Only two hidden layers were used for all architectures based on minimal requirements, not optimized per model.
  - The study did not investigate hyperparameter optimization for each architecture. [unacknowledged]
  - Computational constraints and suitability for mobile-first applications were not evaluated. [unacknowledged]
  - The study focuses only on univariate forecasting, whereas personal finance predictions often require multivariate inputs. [unacknowledged]
remember_this:
  - LSTM-GRU hybrid achieved the best mean rank of 2.23 across all datasets.
  - Monte Carlo simulation across 100 iterations provides reliable model stability assessment.
  - Vanilla RNN showed consistently the highest error rates and most variability.
  - LSTM-RNN hybrid offers the best balance of accuracy and computational efficiency.
  - Statistical equivalence across architectures suggests practical considerations should guide selection.
```
---

## Paper 2: Gulbakyt et al_summarized.md

**Source File:** `Gulbakyt et al_summarized.md`

```yaml
paper_id: "10.47738/jads.v6i4.935"
designation: "international-algorithm-specific"
title: "Dynamic Model for Budget Allocation in via Multi-Criteria Optimization"
authors: "Gulbakyt, S.; Abdualiyev, A.; Sagnayeva, S.; Yoldash, S."
year: 2025
venue: "Journal of Applied Data Sciences"
odin_topics:
  - "7.C"
  - "7.D"
  - "12.B"
tldr: "A dynamic multi-criteria optimization framework using SQP and GA allocates a constrained regional budget across seven activity areas in Kazakhstan's Almaty region, achieving equitable distribution with a Gini coefficient of 0.223."
problem_and_motivation: "Local executive bodies in Kazakhstan lack transparent, data-driven tools for budget allocation, leading to socioeconomic disparities and declining public trust. Existing approaches fail to balance strategic priorities, citizen preferences, and basic needs while ensuring equitable distribution across districts."
approach:
  - "Formulates budget allocation as a quadratic programming problem with four weighted criteria: citizen satisfaction (0.2), strategic priorities (0.2), basic needs (0.3), and urbanization (0.3)."
  - "Applies Sequential Quadratic Programming (SQP) in MATLAB's fmincon solver, converging within 100 iterations to an objective value of 18,519,864.85 thousand tenge."
  - "Implements a Genetic Algorithm (GA) using Python's DEAP library with population size 200, 500 generations, 80% crossover, and 5% mutation rate."
  - "Uses synthetic citizen voting data derived from demographic statistics and official data from Kazakhstan's Bureau of National Statistics."
  - "Enforces constraints including total budget equality, minimum/maximum bounds per sector, and regional limits."
findings:
  - "num: SQP achieved an objective value of 18,519,864.85 thousand tenge, while GA reached 18,520,000.00, a negligible difference of 135.15 thousand tenge (0.0007% of total budget)."
  - "num: The Gini coefficient of 0.223 indicates equitable distribution across sectors, with a standard deviation of 5.69% and coefficient of variation of 0.398."
  - "num: Healthcare (22.05%) and transport (21.11%) received the largest allocations, while education (7.03%) received the smallest."
  - "All seven activity areas received funding, demonstrating comprehensive sectoral coverage without exclusion."
  - "SQP converged rapidly within 100 iterations, whereas GA required 500 generations to stabilize but offered robustness against local optima."
  - "num: SQP completed optimization with a final feasibility violation of 865,100 tenge (0.47% of budget), indicating a trade-off between strict feasibility and utility maximization."
key_figures_tables:
  - "Figure 1: Conceptual framework of the dynamic budget allocation model → Shows data flow from inputs through optimization to evaluation."
  - "Figure 2: Budget allocation result → Displays balanced distribution across seven sectors and four districts."
  - "Figure 3: Feasible budget allocation region for Healthcare and Transport → Validates optimized allocations lie within constraints."
  - "Figure 4: Optimization process output parameters → Confirms convergence with Func-count 128 and first-order optimality 0.7016."
  - "Figure 5: Convergence of objective function value during SQP optimization → Shows rapid improvement from 16.5 to 18.52 million tenge."
  - "Figure 6: Distribution of budget using GA → Demonstrates similar allocation patterns to SQP across districts."
  - "Table 1: Distributed votes of citizens → Provides synthetic voting data used as input criteria across seven activity areas."
  - "Table 2: Unique strategic priorities → Lists priority multipliers (1.0–2.1) across sectors and four districts."
  - "Table 3: Demographic data and urbanization coefficients → Shows population, income, and urbanization for four Almaty districts."
  - "Table 4: Numerical results (thousands tenge) → Presents the optimized budget allocation values for each district and sector."
  - "Table 5: Comparative analysis of models → Compares level balance, linear programming, and multi-criteria optimization across four criteria."
  - "Table 6: Comparative characteristics of SQP and GA methods → Contrasts method type, objective values, convergence, and constraints."
key_equations:
  - equation: "min(½xᵀQx + cᵀx) subject to A_eq·x = b_eq, A_ineq·x ≤ b_ineq"
    explanation: "Defines quadratic programming problem with equality and inequality constraints."
  - equation: "Objective = α·∑(V_ij/max(V))·B_ij + β·∑(W_ij/max(W))·B_ij + γ·∑1(B_ij ≥ B_min_ij) + δ·∑(U_i/max(U))·B_ij"
    explanation: "Maximizes weighted sum of citizen satisfaction, strategic priorities, basic needs, and urbanization."
  - equation: "A_eq × B_vec = Total budget"
    explanation: "Enforces equality constraint that total allocation equals 42,656,543 thousand tenge."
  - equation: "B_min ≤ B_vec ≤ B_max"
    explanation: "Sets minimum and maximum bounds on budget variables for each sector."
definitions:
  - term: "SQP"
    definition: "Sequential Quadratic Programming, a gradient-based optimization method for constrained nonlinear problems."
  - term: "GA"
    definition: "Genetic Algorithm, a stochastic population-based optimization technique inspired by natural selection."
  - term: "AA"
    definition: "Areas of Activity, the seven sectors receiving budget allocations (education, healthcare, transport, infrastructure, digitalization, culture, ecology)."
  - term: "CU"
    definition: "Urbanization coefficient, the ratio of urban to total population used as a weighted criterion."
  - term: "Maslikhats"
    definition: "Local elected councils in Kazakhstan responsible for regional budget allocation and public fund distribution."
critical_citations:
  - "[Gulbakyt and Abdualiyev, 2024] — Previous linear programming model for budget allocation."
  - "[Mazelis et al., 2021] — Dynamic model for human capital investment distribution."
  - "[Bartocci et al., 2023] — Systematic review of participatory budgeting."
  - "[Schugurensky and Mook, 2024] — Participatory budgeting and local development impacts."
relevance:
  topics:
    - code: "7.C"
      name: "Constrained Optimization Approaches for Budget Allocation"
      relevance: "high"
      justification: "Directly applies SQP and GA to solve constrained multi-criteria budget allocation with equality and inequality constraints."
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "medium"
      justification: "Demonstrates constraint violation handling through penalty-based fitness and minimum/maximum bounds."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Compares SQP and GA performance through objective values, convergence speed, and fairness metrics."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "contextual"
      justification: "Addresses resource allocation optimization but for regional government, not personal finance."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "low"
      justification: "Uses weighted criteria and constraints but does not explore budgeting strategy taxonomies."
  contribution: "This paper's constrained optimization framework informs Odin's budget recommendation module (7.C) by demonstrating how SQP and GA can allocate limited resources across multiple weighted criteria with equality and inequality constraints. The handling of minimum/maximum bounds and penalty-based infeasibility management (7.D) directly applies to Odin's allocation problem with user-defined constraints (3.C). The fairness evaluation using Gini coefficient, standard deviation, and coefficient of variation provides a template for assessing Odin's allocation equity. The comparative analysis of deterministic (SQP) versus stochastic (GA) optimization methods guides algorithm selection for Odin's budget optimization engine. The participatory budgeting simulation using citizen voting data offers a model for incorporating user preferences into allocation decisions."
  directly_justifies:
    - "Multi-criteria optimization can balance multiple objectives including user preferences, needs, and constraints."
    - "SQP provides rapid convergence for well-defined constrained optimization problems."
    - "GA offers robustness for complex problem structures with uncertainty."
    - "Constrained optimization with minimum bounds ensures all categories receive baseline funding."
  limits:
    - "The study uses synthetic citizen voting data rather than real participatory budget records."
    - "The model is designed for regional government budgets, not personal finance allocation."
    - "Weight coefficients lack formal sensitivity analysis or stakeholder validation."
  mapping_rationale: "After systematically scanning all 12 functional domains and their associated topic codes, three domains were flagged as relevant. The Budget Recommendation domain (7.A, 7.B, 7.C, 7.D) is most relevant, with 7.C receiving 'high' relevance because the paper directly applies SQP and GA to solve a constrained multi-criteria budget allocation problem with weighted criteria, equality constraints, and bounds, mirroring Odin's allocation engine. Topic 7.D received 'medium' for its treatment of constraint infeasibility via penalty functions and bounds. Topic 12.B from the System Evaluation domain received 'medium' for the comparative analysis of SQP versus GA using objective values, convergence metrics, and fairness indicators. Topic 7.B was marked 'contextual' as the paper addresses public sector rather than personal finance, but the optimization structure is transferable. Topics 7.A and 4.A were considered and rejected as the paper does not explore budgeting strategy taxonomies or existing PFMS systems. The Filipino Cultural Context and Behavioral Profiling domains were rejected as the paper focuses on Kazakhstan's regional planning with no cultural or behavioral financial analysis. Overall, the paper's optimization framework is structurally relevant to Odin's budget recommendation module despite the different application domain, providing validated techniques for constrained multi-criteria allocation."
limitations:
  - "The paper uses synthetic citizen voting data rather than actual participatory budget records. [unacknowledged]"
  - "Weight coefficients for criteria (0.2, 0.2, 0.3, 0.3) were set via expert judgment without formal sensitivity analysis."
  - "The model remains at conceptual phase with pilot testing pending approval from Kazakhstan's Ministry of Digital Development."
  - "Quantitative comparison with baseline models lacks empirical validation due to unavailable disaggregated budget data."
  - "Constraint violations (0.47% of budget) indicate a trade-off between feasibility and utility maximization that is acknowledged but not fully resolved."
remember_this:
  - "SQP and GA achieved nearly identical objective values with only 0.0007% difference."
  - "Gini coefficient of 0.223 indicates equitable budget distribution across seven sectors."
  - "Healthcare and transport received 22.05% and 21.11% of the total budget respectively."
  - "SQP converged rapidly while GA required 500 generations but offered global search robustness."
  - "All seven activity areas received funding through constrained optimization with minimum bounds."
```
---

## Paper 3: Martinez_summarized.md

**Source File:** `Martinez_summarized.md`

```yaml
paper_id: 10.21203/rs.3.rs-7893661/v1
designation: international-algorithm-specific
title: A Review of Machine Learning and Deep Learning Approaches for Fraud Detection Across Financial and Supply Chain Domains
authors: Martínez, Ó.
year: 2025
venue: Systematic Review (Preprint)
odin_topics:
  - "8.A"
  - "8.B"
  - "5.A"
  - "5.C"
  - "12.A"
  - "12.B"
  - "12.C"
tldr: A systematic review of machine learning and deep learning for fraud detection, evaluating traditional, ensemble, and semi-supervised methods across financial and supply chain domains.
problem_and_motivation: Fraud detection is critical yet challenging due to sophisticated schemes and extreme class imbalance. Traditional rule-based systems are inadequate, and a gap exists in comprehensive reviews bridging financial and supply chain fraud with modern ML/DL techniques.
approach:
  - "Conducted a systematic literature review following PRISMA guidelines."
  - "Searched multiple academic databases for studies published between 2015 and 2025."
  - "Screened 1,847 publications, resulting in a final corpus of 97 high-quality studies."
  - "Categorized methodologies into traditional ML, deep learning, ensemble, semi-supervised, and emerging technologies."
  - "Evaluated approaches based on performance metrics, imbalance handling, interpretability, and computational efficiency."
findings:
  - "num: Ensemble methods and tree-based models consistently achieve superior performance in credit card fraud detection, with AUC-ROC often exceeding 0.95."
  - "num: Semi-supervised approaches, such as two-phase frameworks combining Isolation Forest and self-training SVM, achieve an F1-score of 0.817 with a false positive rate under 3% in supply chain contexts."
  - "Deep learning methods like LSTM excel at capturing temporal dependencies but do not consistently outperform optimized gradient boosting on tabular data."
  - "Extreme class imbalance and concept drift remain fundamental challenges, with Borderline-SMOTE and ensemble methods offering the most effective mitigation."
  - "Explainable AI (XAI) techniques like SHAP and LIME are critical for regulatory compliance and can improve fraud analyst efficiency by 35%."
key_figures_tables:
  - "Table 8: Traditional ML performance → Random Forest offers the best balance for general-purpose fraud detection."
  - "Table 12: Training time comparison on IEEE-CIS scale → LightGBM is fastest among high-performance algorithms."
  - "Table 13: Inference latency per transaction → XGBoost and LightGBM meet sub-100ms real-time requirements."
  - "Table 15: Interpretability requirements by context → Regulatory and customer-facing contexts demand high interpretability."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "ML"
    definition: "Machine learning."
  - term: "DL"
    definition: "Deep learning."
  - term: "AUC-ROC"
    definition: "Area under the receiver operating characteristic curve."
  - term: "AUC-PR"
    definition: "Area under the precision-recall curve."
  - term: "SMOTE"
    definition: "Synthetic minority over-sampling technique."
  - term: "XAI"
    definition: "Explainable artificial intelligence."
  - term: "GNN"
    definition: "Graph neural network."
  - term: "LSTM"
    definition: "Long short-term memory network."
critical_citations:
  - "[Chawla et al., 2002] — Introduces SMOTE for handling class imbalance."
  - "[Chen & Guestrin, 2016] — Proposes XGBoost, a top-performing algorithm."
  - "[Moradi et al., 2025] — Comprehensive study on ensemble methods for fraud detection."
relevance:
  topics:
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Paper reviews anomaly detection as a core fraud detection technique."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Evaluates algorithms like Isolation Forest, Autoencoders, and LOF for anomaly detection."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "contextual"
      justification: "Discusses behavioral features but not in the context of profiling."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "contextual"
      justification: "Reviews classification approaches generally, not specifically for profile building."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides a comprehensive overview of evaluation metrics and protocols."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Compares performance of various algorithmic modules across domains."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "contextual"
      justification: "Focuses on fraud detection, not budget recommendation."
  contribution: "This review informs Odin's anomaly detection module by identifying state-of-the-art algorithms (e.g., Isolation Forest, XGBoost) and best practices for handling class imbalance. It supports the design of Odin's evaluation framework by detailing appropriate metrics (AUC-PR) and validation protocols. The findings justify the use of semi-supervised approaches for Odin in data-scarce scenarios. It provides a foundation for selecting the most effective and computationally efficient algorithms for real-time detection. It also highlights the importance of interpretability, guiding the integration of XAI techniques into Odin's decision-making process."
  directly_justifies:
    - "Ensemble methods like XGBoost and Random Forest are top performers for imbalanced tabular fraud data."
    - "A two-phase framework of unsupervised pre-filtering and semi-supervised refinement is effective with minimal labeled data."
    - "AUC-PR is the preferred metric for evaluating models on extremely imbalanced datasets."
    - "Concept drift necessitates frequent model retraining or online learning strategies."
    - "Explainable AI is essential for regulatory compliance and user trust."
  limits:
    - "The review's primary focus is on credit card and supply chain fraud, with less emphasis on other domains."
    - "Findings are based on public benchmarks, which may not fully represent proprietary industry data patterns."
  mapping_rationale: "The paper was systematically scanned against all 12 functional domains. Domains related to Anomaly Detection (8.A, 8.B) were flagged as high relevance due to the paper's core subject. System Evaluation (12.A, 12.B, 12.C) was assessed as medium relevance because it provides extensive benchmarking and evaluation frameworks. Behavioral Profiling (5.A, 5.C) was considered contextual, as the paper discusses behavioral features and general classification but does not focus on building user profiles for financial management. Domains concerning Filipino cultural context, expense categorization, existing systems, forecasting, budgeting, mobile design, privacy, retention, and savings/debt management were considered and rejected as the paper does not address these specific Odin concerns. The overall relevance is high for informing the technical design of anomaly detection and evaluation components within Odin."
limitations:
  - "Reliance on public benchmarks may limit generalizability to proprietary industry data."
  - "Deep learning for fraud is covered, but practical deployment details are often abstracted away."
  - "The review does not provide a novel algorithmic contribution, only a synthesis of existing work."
remember_this:
  - "Ensemble methods like XGBoost and stacking are the current state-of-the-art."
  - "Semi-supervised learning is highly effective when fraud labels are scarce."
  - "Concept drift requires continuous model adaptation for sustained performance."
  - "Explainable AI is crucial for regulatory compliance and building user trust."
  - "Borderline-SMOTE is a top choice for addressing extreme class imbalance."
```
---

## Paper 4: Al-E'mari et al_summarized.md

**Source File:** `Al-E'mari et al_summarized.md`

```yaml
paper_id: "e7b7b7b7-7b7b-7b7b-7b7b-7b7b7b7b7b7b"
designation: "international-algorithm-specific"
title: "The Role of Artificial Intelligence in Enhancing Financial Decision-Making and Administrative Efficiency: A Systematic Review"
authors: "Al-E'mari, S.; Sanjalawe, Y.; Al-E'mari, A."
year: 2025
venue: "Al-Basaer Journal of Business Research"
odin_topics:
  - "4.A"
  - "8.A"
  - "8.B"
  - "10.A"
  - "12.A"
tldr: "A systematic review of AI applications in finance and administration, highlighting predictive analytics, machine learning, and RPA for enhanced decision-making, risk management, and operational efficiency."
problem_and_motivation: "Despite growing AI adoption in finance and administration, a comprehensive understanding of its systemic benefits and challenges across both domains remains lacking. Existing research often neglects the ethical, regulatory, and security implications of AI-driven decision-making. This review addresses this gap by providing a holistic analysis of AI's impact."
approach:
  - "Systematic literature review following established guidelines for transparency and replicability."
  - "Searched IEEE Xplore, PubMed, Scopus, Web of Science, and ScienceDirect for relevant studies."
  - "Used Boolean search strings combining terms like 'Financial Decision-Making,' 'AI,' and 'Predictive Analytics.'"
  - "Applied inclusion criteria: peer-reviewed articles from 2014-2024, focusing on AI in finance and administration."
  - "Used a two-reviewer process for screening titles, abstracts, and full texts to minimize bias."
  - "Extracted data on AI application type, process impact, methodology, and key findings."
  - "Employed a structured evaluation framework with KPIs like time savings and cost reductions."
  - "Included real-world case studies from JPMorgan Chase, BlackRock, Ant Financial, and UiPath."
  - "Analyzed performance correlations between AI applications and decision-making speed."
findings:
  - "num: JPMorgan Chase's COiN platform achieved a 99% reduction in manual legal document review time."
  - "num: BlackRock's Aladdin system improved forecasting accuracy by 20% and reduced market reaction time by 30%."
  - "num: Ant Financial's AI fraud detection improved detection rates by 35% compared to rule-based systems."
  - "num: UiPath RPA in healthcare led to an 80% reduction in billing processing times and a 60% increase in operational efficiency."
  - "AI enhances administrative functions through RPA for automating routine tasks and AI-powered tools for data management."
  - "Broad AI use shows a 0.61 correlation with speed and a 0.48 correlation with decision-making."
  - "Predictive analytics is essential for portfolio management and algorithmic trading."
  - "AI enhances risk management and fraud detection by analyzing vast datasets for suspicious patterns."
  - "AI helps with regulatory compliance by automating transaction monitoring and updating protocols."
  - "AI-driven data management reduces manual effort and improves reporting accuracy."
key_figures_tables:
  - "Figure 1: Efficiency gains from AI in data reporting → Shows improvements in time saved, reporting accuracy, and error reduction."
  - "Figure 2: Performance impact of AI on improved decision-making → Correlates AI applications with speed and decision-making benefits."
  - "Figure 3: Comparison of AI case studies → Quantifies time saved and accuracy improvements across case studies."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "RPA"
    definition: "Robotic Process Automation, the use of AI-driven software bots to replicate human actions for routine tasks."
  - term: "NLP"
    definition: "Natural Language Processing, a field of AI that enables computers to understand and process human language."
  - term: "XAI"
    definition: "Explainable Artificial Intelligence, techniques to make AI decisions transparent and understandable to humans."
critical_citations:
  - "[Biloslavo et al., 2024] — Provides context on AI in strategic planning."
  - "[Farayola, 2024] — Discusses AI in banking security."
  - "[Cohen, 2022] — Details algorithmic trading with AI."
  - "[Bao, Hilary & Ke, 2022] — Covers AI and fraud detection."
  - "[Rane, Choudhary & Rane, 2023] — Highlights AI for security in finance."
relevance:
  topics:
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Provides a broad overview of AI applications, not specific PFMS landscape."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Directly addresses fraud detection, a core anomaly detection use case in finance."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "medium"
      justification: "Discusses machine learning for identifying suspicious patterns in financial data."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "Extensively discusses data privacy and security challenges of AI, referencing GDPR."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Uses KPIs like time savings and accuracy to evaluate AI impact, relevant to system evaluation."
  contribution: "This paper provides a high-level framework for evaluating AI's role in financial decision-making, which can inform the design of Odin's anomaly detection and risk assessment modules. Its discussion of data privacy and security considerations directly supports the development of Odin's user trust and data governance strategies. The quantitative performance metrics from case studies offer benchmarks for evaluating Odin's algorithmic modules. The paper's analysis of AI's impact on administrative efficiency can guide the design of Odin's user-facing features for expense tracking and reporting. Its emphasis on ethical challenges highlights the need for transparent and accountable AI within Odin."
  directly_justifies:
    - "AI-powered systems can detect anomalies and flag suspicious transactions faster than rule-based systems."
    - "Machine learning models can identify patterns in market data and predict risks associated with investments."
    - "RPA can automate routine administrative tasks, reducing manual effort and human error."
    - "Data privacy and security are critical challenges in AI adoption, requiring compliance with regulations like GDPR."
  limits:
    - "The review is broad and not specifically tailored to personal finance management systems for young professionals."
    - "The findings are based on systematic review and may not represent a single, controlled empirical study."
    - "The paper focuses on general AI applications, not specific algorithms for spending data."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains of 'Anomaly Detection' and 'Data Privacy & User Trust' were flagged as highly relevant, as the paper extensively covers fraud detection and data security. 'Existing Systems & Gaps' was marked contextual, as the paper provides a landscape review. 'System Evaluation' was marked medium due to its use of KPIs for evaluating AI impact. The domain of 'Expense Categorization' was rejected as the paper does not discuss expense classification. The domain of 'Behavioral Profiling' was rejected as it does not cover user profiling or cold-start problems. The domain of 'Spending Forecasting' was rejected as it does not discuss forecasting algorithms for spending. The overall relevance is medium; while the paper provides strong support for general AI capabilities and challenges, it lacks specific guidance on PFMS design for Filipino users."
limitations:
  - "Focuses on general AI applications in finance and administration, not specifically on PFMS. [unacknowledged]"
  - "Does not address the cold-start problem or behavioral profiling for new users. [unacknowledged]"
  - "Limited discussion of constrained optimization for budget allocation. [unacknowledged]"
remember_this:
  - "AI in finance improves risk management and fraud detection through pattern recognition."
  - "RPA automates administrative tasks, increasing operational efficiency and reducing errors."
  - "Data privacy and security are critical challenges requiring regulatory compliance."
  - "Broad AI use shows a 0.61 correlation with speed and 0.48 with decision-making."
```
---

## Paper 5: Badiger et al_summarized.md

**Source File:** `Badiger et al_summarized.md`

```yaml
paper_id: 10.17148/IJARCCE.2025.14364
designation: international-algorithm-specific
title: Next.js-Powered AI Platform for Smart Expense Tracking, Budgeting and Insights
authors: Badiger, R.; Robin, R.; Moraas, T.; Naik, V. G.; Karthikeyan A N, P.
year: 2025
venue: International Journal of Advanced Research in Computer and Communication Engineering
odin_topics:
  - 3.A
  - 4.A
  - 4.B
  - 6.A
  - 8.A
  - 12.A
tldr: An AI-powered personal finance platform integrating machine learning categorization, large language model insights, and time-series forecasting within a Next.js full-stack architecture.
problem_and_motivation: Existing personal finance tools lack automated real-time categorization, personalized natural-language insights, and predictive budgeting capabilities. This gap is particularly acute for users navigating multi-channel digital payment ecosystems, leading to poor financial decision-making.
approach:
  - The system is built on Next.js 14, Prisma ORM, Supabase PostgreSQL, and Clerk authentication.
  - Automated transaction categorization uses an XGBoost classifier trained on labelled transaction data.
  - Natural-language financial insights are generated using Google's Gemini LLM with a RAG pattern.
  - Expense forecasting is implemented using Meta's Prophet time-series model per spending category.
  - The platform supports multi-modal data ingestion including manual entry, CSV import, and receipt scanning.
  - Evaluation was performed on a held-out test set of 4,200 transactions from anonymized datasets.
findings:
  - "num: The XGBoost categorization model achieves a weighted F1-score of 0.913 across 18 spending categories."
  - "num: Server response times average 420ms for dashboard loads, with AI insight generation adding 800-1,400ms."
  - "num: The system reduces manual expense-logging effort by approximately 78% compared to conventional approaches."
  - Categories with high linguistic diversity show lower precision, while frequent categories achieve F1-scores above 0.95.
  - User feedback indicated that 84% of participants found the AI-generated insights useful for guiding financial decisions.
key_figures_tables:
  - "Figure 1: End-to-End User Workflow of Spend AI → visualizes the seven-stage process from authentication to budget alerts."
  - "Figure 2: Five-Layer System Architecture of Spend AI → illustrates the modular presentation, business, AI, data, and authentication layers."
  - "Figure 3: Technology Stack Overview → summarizes the complete technology stack from frontend to AI components."
  - "Figure 4: AI Insight Generation Pipeline (RAG Pattern) → shows the RAG-based prompt construction for the Gemini LLM."
  - "Figure 5: XGBoost Transaction Categorisation F1-Scores → displays per-category performance of the classification model."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "LLM"
    definition: "Large Language Model, used for natural-language insight generation."
  - term: "RAG"
    definition: "Retrieval-Augmented Generation, a pattern for grounding LLM responses in specific data."
  - term: "XGBoost"
    definition: "Extreme Gradient Boosting, a gradient-boosted tree classifier used for transaction categorization."
  - term: "UPI"
    definition: "Unified Payments Interface, India's real-time payment system."
  - term: "RLS"
    definition: "Row-Level Security, a database feature for enforcing per-user data isolation."
critical_citations:
  - "[Verma et al., 2024] — demonstrated Next.js viability but lacked AI categorization."
  - "[Kotios et al., 2022] — provided benchmarks for hybrid transaction classification."
  - "[Hean et al., 2025] — evaluated Gemini's capability for personal finance tasks."
  - "[Pancholi et al., 2026] — proposed multi-agent AI system for personal finance."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: "Implements an XGBoost model achieving 91.3% F1-score for transaction categorization."
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: "Reviews existing PFM systems and identifies gaps in automation and personalization."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: "Explicitly addresses limitations of prior systems and motivates the development of Spend AI."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: "Uses Prophet for time-series forecasting of monthly expenses by category."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: "Includes anomaly detection as a core feature, flagging transactions exceeding statistical thresholds."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: "Evaluates system performance through categorization accuracy and user experience feedback."
  contribution: "The paper's architecture for integrating ML categorization, LLM insights, and time-series forecasting directly informs Odin's design for the Categorization Engine, AI Insight Module, and Forecasting Module. Its use of a full-stack framework with row-level security provides a production-ready template for Odin's Mobile-First Design and Data Privacy & User Trust considerations. The experimental evaluation methodology offers a framework for evaluating Odin's algorithmic modules."
  directly_justifies:
    - "A gradient-boosted tree classifier can achieve over 91% accuracy for transaction categorization tasks."
    - "LLM-based insights grounded in user data via RAG can generate useful and validated financial guidance."
    - "Time-series forecasting with Prophet is feasible for personal spending prediction using limited historical data."
    - "Row-level security is a critical architectural property for systems handling sensitive financial data."
  limits:
    - "Categorization accuracy is lower for new users with fewer than 50 historical transactions (cold-start problem)."
    - "LLM hallucination risk remains, though mitigated by RAG-style prompting."
    - "Forecasting accuracy requires at least 3 months of historical data for reliable predictions."
    - "Data residency and regulatory compliance (e.g., DPDP Act) require further attention. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes flagged four domains as highly relevant: Expense Categorization (3.A), Existing Systems & Gaps (4.A, 4.B), Spending Forecasting (6.A), and Anomaly Detection (8.A). The paper's core contribution is algorithmic, justifying the 'algorithm-specific' designation, with direct implications for Odin's predictive and categorization modules. The System Evaluation domain (12.A) was considered relevant as the paper provides a performance evaluation framework. The Behavioral Profiling & Classification (5.A) domain was considered but rejected as the paper does not develop or utilize user financial profiles. The Savings & Debt Management domain (13.A, 13.B) was also considered but rejected as the paper's primary focus is on expense tracking and budgeting rather than savings or debt-specific features. Overall, the paper provides strong, directly applicable evidence for building an AI-powered PFMS, particularly its core algorithmic components."
limitations:
  - "LLM hallucination risk remains; critical recommendations should be verified."
  - "Manual data entry dependency persists in the absence of direct banking API integration."
  - "Data residency and regulatory compliance require further attention. [unacknowledged]"
  - "Forecasting accuracy requires at least 3 months of historical data for reliable predictions."
remember_this:
  - "XGBoost achieved 91.3% F1-score for transaction categorization across 18 categories."
  - "Platform reduces manual expense-logging effort by approximately 78%."
  - "84% of pilot users found Gemini-generated insights useful for financial decisions."
  - "System architecture separates presentation, business, AI, data, and authentication layers."
  - "RAG-based prompting grounds LLM insights in verifiable user data to reduce hallucination."
```
---

## Paper 6: Pakarinen_summarized.md

**Source File:** `Pakarinen_summarized.md`

```yaml
paper_id: 1b3c4a5d-6e7f-8a9b-0c1d-2e3f4a5b6c7d
designation: international-algorithm-specific
title: Optimizing Banking Application Interfaces: A User-Centric Perspective on Consent Management in Digital Banking Environments
authors: Pakarinen, O.
year: 2025
venue: JAMK Master's Thesis
odin_topics:
  - 10.A
  - 10.B
  - 9.A
  - 9.B
  - 11.A
  - 11.B
  - 12.A
  - 3.A
tldr: Consent interfaces designed with category overviews and detailed controls improved user understanding, control perception, and decision confidence compared to traditional dense legal text approaches.
problem_and_motivation: Consent management in digital banking is often implemented with complex legal language and confusing formats, which undermines user understanding and informed decision-making. This gap between regulatory requirements and practical user comprehension poses risks to trust and autonomy. There is a need for consent interfaces that are transparent, accessible, and supportive of user control.
approach:
  - The study employed a mixed-methods approach, including a preliminary exploratory survey (n=6) to guide design.
  - A consent management prototype with a two-level structure (category-based overview and detailed consent view) was designed using Figma and the MEAN stack.
  - Two rounds of usability testing were conducted with participants interacting with the prototype, followed by semi-structured interviews.
  - Usability testing measured task completion time, error rate, user hesitations, and confidence levels.
  - Feedback from the first round informed iterative design improvements, such as breaking text into smaller segments and adding visual cues.
findings:
  - Participants interacting with the new consent flow showed increased confidence in their consent decisions.
  - Category-based overviews and explicit labels significantly improved users' ability to understand the consent structure.
  - Traditional consent screens with lengthy legal text were often ignored or skimmed, leading to user uncertainty.
  - Providing immediate feedback after a consent setting change reinforces user understanding and control.
  - Progressive disclosure of information (from category overview to detailed view) reduced cognitive load and improved comprehension.
  - The AI-powered "Smart Summary" feature was found helpful by participants for confirming their decisions.
key_figures_tables:
  - Figure 6.1: Revolut's category-based privacy settings → Illustrates a user-centric, mobile-first approach to consent.
  - Figure 6.2: ING Spain's Didomi consent interface → Shows standardized consent presentation across channels.
  - Figure 6.3: Nordea's open banking authorization flow → Demonstrates secure, in-app consent for third-party data access.
  - Figure 7.1: Consent management flow diagram → Visualizes the step-by-step user journey in the prototype.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: GDPR
    definition: General Data Protection Regulation, a legal framework that sets guidelines for the collection and processing of personal information.
  - term: CCPA
    definition: California Consumer Privacy Act, a state statute intended to enhance privacy rights and consumer protection.
  - term: Consent Management
    definition: The process of how users accept or decline the processing of personal information and how that consent is managed.
critical_citations:
  - "[Nouwens et al., 2020] — Demonstrated how consent pop-ups can influence user decisions."
  - "[EDPB, 2022] — Provided guidelines on dark patterns and consent clarity."
relevance:
  topics:
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: The study directly addresses the design of consent interfaces for managing personal data privacy.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Findings show that clear consent interfaces improve user confidence and trust.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: The prototype and case studies (e.g., Revolut) emphasize mobile-first design for consent.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: The usability testing focuses on user experience and interaction design for consent management.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: The research explores how consent design affects user engagement and decision-making.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: low
      justification: While not a primary focus, improved consent management is framed as supporting long-term customer loyalty.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: The study uses usability testing and interviews, aligning with system evaluation methodologies.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: The paper references consent categories for data usage, not for expense categorization.
  contribution: The research demonstrates that applying user-centered design principles—such as empathy, accessibility, and flexibility—can transform consent management from a formal regulatory requirement into a clearer and more approachable user experience. The proposed two-layer consent interface and evaluation results provide actionable evidence for improving user understanding and control in PFMS. The findings directly inform the design of Odin's consent and privacy-related modules, particularly in enhancing user trust.
  directly_justifies:
    - "Category-based consent overviews improve user orientation and understanding."
    - "Concise language and explicit labels increase user confidence in consent decisions."
    - "Providing a clear consent state (active/inactive/partial) reduces user uncertainty."
    - "Gradual disclosure of consent information lowers cognitive load."
    - "An AI-powered summary can effectively support users in confirming their choices."
  limits:
    - "Small sample size limits the generalizability of the usability findings."
    - "The study was conducted in a controlled environment, not a real banking system."
    - "The prototype simplified certain backend functions, which might influence user perceptions."
    - "Findings are primarily derived from a Finnish/European context and may not fully represent Filipino user behavior." [unacknowledged]
  mapping_rationale: A systematic scan of all 12 functional domains and their associated canonical topic codes was performed. The domains of "Data Privacy & User Trust" (topics 10.A, 10.B), "Mobile-First Design" (9.A, 9.B), and "User Retention & Engagement" (11.A, 11.B) were flagged as highly or moderately relevant, as the paper directly addresses consent interface design and its impact on user control, trust, and interaction. The "System Evaluation" domain (12.A) received medium relevance due to the study's methodology. The "Expense Categorization" domain (3.A) was considered contextual as the paper discusses consent categories but not for expenses. Domains like "Spending Forecasting" and "Budget Recommendation" were considered and rejected as the paper does not address predictive algorithms or allocation constraints. Borderline cases, such as the paper's discussion of user engagement touching both 11.A and 11.B, were resolved by identifying 11.A (engagement dynamics) as more directly applicable. Overall, the paper provides strong evidence for the design of consent and privacy modules, which are foundational to building user trust in Odin.
limitations:
  - "Small sample size for the survey and usability tests."
  - "Controlled testing environment may not reflect real-world banking interactions."
  - "The prototype was simplified and not integrated with a live banking system."
  - "Limited exploration of long-term user engagement with the consent model."
  - "Potential cultural bias as the study was conducted in a European context, which may not apply to Filipino users." [unacknowledged]
remember_this:
  - "Usability testing showed increased user confidence with the improved consent interface."
  - "Category-based overviews are more effective than long legal text for consent comprehension."
  - "Iterative design based on user feedback significantly reduced task completion time."
  - "Clear consent status visibility reduces user uncertainty and hesitation."
```
---

## Paper 7: Aboud_summarized.md

**Source File:** `Aboud_summarized.md`

```yaml
paper_id: 10.21070/acopen.10.2025.12858
designation: international-algorithm-specific
title: Goal Programming Model in Financial Planning of the International Development Bank
authors: Aboud, M.M.S.F.
year: 2025
venue: Academia Open
odin_topics:
  - 7.C
  - 12.C
tldr: Goal programming optimizes conflicting financial objectives in banking under resource constraints, achieving near-optimal solutions with minimal deviations.
problem_and_motivation: Financial institutions struggle to balance multiple conflicting objectives like profitability, cost control, and liquidity. Traditional planning models lack the capability to handle these competing goals, especially in resource-constrained environments. A quantitative method is needed to reconcile these trade-offs and improve decision-making.
approach:
  - A weighted-preemptive hybrid goal programming model is formulated for bank financial planning.
  - The model incorporates multiple objectives: revenue, expenses, net profit, fixed assets, loans, and equity.
  - WINQSB software is used to solve the model with prioritized goals and assigned weights.
  - The case study uses annual financial data from the International Development Bank for 2016-2024.
  - The model is evaluated by comparing actual and target values across all financial goals.
findings:
  - The GP model achieved near-optimal solutions for all prioritized goals.
  - Revenue goal was slightly underachieved with a negative deviation of 0.1884.
  - Expense goal was slightly underachieved with a negative deviation of 0.1873.
  - Net profit goal was underachieved with a negative deviation of 0.3006.
  - Fixed assets goal was overachieved with a positive deviation of 0.7833.
  - Equity goal was underachieved with a negative deviation of 0.2956.
  - The model demonstrates flexible prioritization of goals in a multi-objective setting.
key_figures_tables:
  - Table 1: Financial data summary 2016-2024 → Provides raw data for the model.
  - Table 2: Scaled financial data in billion IQD → Enables analysis with smaller numbers.
key_equations:
  - equation: Min Z = Σ(w_i^- d_i^- + w_i^+ d_i^+)
    explanation: Minimizes weighted deviations from multiple goals.
  - equation: Σ a_ij X_j + d_i^- - d_i^+ = b_i
    explanation: Defines goal constraints with deviation variables.
definitions:
  - term: Goal Programming
    definition: A mathematical model for solving multi-objective problems with competing goals.
  - term: Negative Deviation
    definition: The amount by which an actual value is below the aspiration level.
  - term: Positive Deviation
    definition: The amount by which an actual value exceeds the aspiration level.
  - term: Weighted Method
    definition: Assigns weights to goals and minimizes total weighted deviation.
  - term: Preemptive Method
    definition: Prioritizes goals, satisfying higher-priority ones first.
  - term: WINQSB
    definition: Software used to solve the goal programming model.
critical_citations:
  - "[Alam, 2022] — Foundational GP model for financial planning."
  - "[Lakshmi et al., 2021] — GP application in financial planning case study."
  - "[Nyor et al., 2022] — GP for financial management in Nigeria."
relevance:
  topics:
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: high
      justification: Applies goal programming to optimize multi-objective financial planning.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Demonstrates a method for evaluating optimal solutions against target values.
  contribution: "The paper provides a practical optimization framework that can inform Odin's budget recommendation module by demonstrating how conflicting objectives (e.g., maximizing savings while minimizing expenses) can be balanced using a weighted-preemptive goal programming approach. The solution method, using WINQSB, offers a reproducible technique for solving multi-objective financial planning problems with prioritized constraints. The case study results, including deviation analysis, provide a benchmark for evaluating optimization models. The model's flexibility suggests it can be adapted for personalized budget allocation based on user-defined financial goals. The research validates the use of constrained optimization for complex financial planning in resource-limited settings, directly applicable to Odin's budget recommendation engine."
  directly_justifies:
    - "Goal programming can optimize financial planning with conflicting objectives."
    - "The model achieves near-optimal solutions with minimal goal deviations."
    - "Prioritization of goals allows flexible decision-making in resource allocation."
    - "The approach is applicable to banking and personal finance contexts."
  limits:
    - "The model is demonstrated on a single bank's data and may not generalize."
    - "User preferences and behavioral factors are not incorporated."
    - "The study focuses on a bank, not individual personal finance management."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to the 'Budget Recommendation' domain (Topic 7.C) because it directly applies constrained optimization (goal programming) to balance multiple, conflicting financial objectives. It is also relevant to 'System Evaluation' (Topic 12.C) because it demonstrates an evaluation methodology based on comparing actual outcomes to target values and analyzing deviations. The paper touches on 'Savings & Debt Management' (Topic 13.A and 13.B) tangentially through its objectives but does not focus on user-level savings goals or debt management strategies. The following domains/topics were considered and rejected: 'Filipino Cultural Context' (Topics 2.A-2.D) because the case study is based on an Iraqi bank and does not address Filipino-specific practices; 'Expense Categorization' (Topic 3.A-3.C) because the paper does not deal with categorizing expenses; 'Behavioral Profiling' (Topics 5.A-5.C) because it does not involve user behavior or profiles; 'Anomaly Detection' (Topics 8.A-8.C) because it does not address detecting outliers. Overall, the paper is most relevant for its constrained optimization methodology, which can be adapted for Odin's budget recommendation algorithm."
limitations:
  - "The model is based on historical data from a single bank, limiting generalizability."
  - "The study does not consider dynamic changes in user behavior or financial conditions."
  - "Behavioral and psychological factors influencing financial decisions are not incorporated. [unacknowledged]"
  - "The approach is applied to banking rather than individual personal finance. [unacknowledged]"
remember_this:
  - "Goal programming balances conflicting financial objectives effectively."
  - "The model achieved near-optimal solutions with minimal deviations."
  - "Prioritization allows flexible resource allocation in financial planning."
  - "Multi-objective optimization is feasible for complex financial systems."
  - "The method can be adapted for personalized budget recommendation."
```
---

## Paper 8: Singh A. et al_summarized.md

**Source File:** `Singh A. et al_summarized.md`

```yaml
paper_id: 9b8b4c3a-8f2d-5a1e-9b4c-3d8e9f2a1b5c
designation: international-algorithm-specific
title: A Smart Personal Finance Assistant for Budget Management and Expense Tracking
authors: Singh, A.; Rastogi, G.; Singh, J. N.
year: 2025
venue: HYPOTHESIS - National Journal of Research in Higher Studies
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 5.C
  - 7.A
  - 7.B
  - 7.C
  - 9.A
  - 9.B
  - 12.A
  - 13.B
tldr: A web-based personal finance assistant integrates income/expense entry, auto-categorization using text analysis and KMeans clustering, and data visualization dashboards to enhance budgeting and spending awareness.
problem_and_motivation: Individuals struggle with improper expense tracking, budgeting, and saving due to the complexity of manual methods and the lack of simple, insightful financial tools. Existing finance applications often lack the simplicity or effective interfaces needed to provide users with actionable insights into their financial activities.
approach:
  - The system is designed as a responsive web application using React with TypeScript for the user interface.
  - Cloud services are used to host authentication and secure data storage functionalities for user accounts.
  - A lightweight natural language processing algorithm analyzes transaction descriptions for auto-categorization.
  - KMeans clustering is applied to segregate financial spending into viable categories based on spending patterns.
  - The application provides data representation through UI dashboards and charts to visualize financial data.
findings:
  - The system effectively handles personal finance by increasing user awareness regarding expenditure.
  - Segmentation of expenses and graphical data presentation significantly helped users better understand their own spending patterns.
  - Charts and monthly summaries enabled users to quickly detect key spending categories and points of unnecessary spending.
  - The system was effective in providing insightful financial reports in real-time through monthly income-expenditure comparisons.
  - Users were able to keep proper records of income and expenditure, maintaining organized financial documentation.
key_figures_tables:
  - Figure 1: Research methodology and financial data processing model → Shows the design-focused methodology for creating the technological system.
  - Figure 2: Workflow of the Smart Personal Finance Assistant → Illustrates income/expense data entry, processing, and financial analysis workflow.
  - Figure 3: Expense tracking and budget analysis process → Demonstrates transaction categorization, visualization, and insight generation.
  - Figure 4: Conceptual Comparison of Traditional Budgeting and Smart Personal Finance Assistant → Highlights the assistant's advantages in providing insights.
  - Figure 5: Expense Tracking and Budget Analysis Over Time → Shows system's capability for tracking and analysis over a period.
  - Figure 6: Future Scope of the Smart Personal Finance Assistant → Depicts planned enhancements like advanced analytics and mobile support.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: K-Means Clustering
    definition: An unsupervised learning algorithm used to partition spending data into groups based on similar expenditure patterns.
  - term: PFMS
    definition: Personal Finance Management System.
critical_citations:
  - "[Kim, 2019] — foundational for user behavior analysis in PFMS."
  - "[Singh and Sharma, 2020] — supports digital expense tracking and budget planning applications."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: The paper's primary contribution is an auto-categorization system using text analysis and clustering.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: It discusses categorizing expenses into groups like Food, Transport, Rent, etc., which informs design.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: The literature review briefly mentions existing digital tools and their limitations.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: KMeans clustering is used to derive spending patterns, a form of behavioral classification.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: The paper's motivation is based on the importance of budgeting strategies for financial stability.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Mentions future work on personal budget suggestion tools.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: contextual
      justification: Does not address constrained optimization, but is related to budget management.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: Future scope mentions mobile application support, indicating awareness of the importance.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: contextual
      justification: The application's responsive UI is designed for user-friendliness, a key UX principle.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: The paper presents a design and implementation, implying an evaluation of its effectiveness.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: contextual
      justification: Indirectly relevant as effective budgeting and tracking prevent debt accumulation.
  contribution: The paper presents a web-based personal finance assistant that combines expense tracking and budgeting with text-based auto-categorization and KMeans clustering. This design directly informs Odin's expense categorization module (3.A) by providing a practical implementation of a lightweight NLP algorithm. It also offers a foundational approach for the budget recommendation module (7.B) by demonstrating how to analyze spending patterns and visualize them for users. The use of clustering for spending pattern analysis (5.C) provides a methodology relevant to Odin's behavioral profiling.
  directly_justifies:
    - "A system with auto-categorization and visualization increases financial awareness among users."
    - "KMeans clustering can effectively segregate spending into meaningful categories for budget analysis."
    - "Real-time financial reports help users monitor their financial condition and make informed decisions."
    - "User-friendly design and organized analysis are crucial for improving financial decision-making."
  limits:
    - "The paper describes a system design and implementation but provides no quantitative evaluation of its effectiveness."
    - "The auto-categorization algorithm is described as 'lightweight' and rule-based, which may lack accuracy for complex descriptions."
    - "User testing or a formal usability study is not presented to validate the user interface claims."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was conducted. The domains deemed most relevant were Expense Categorization (3.A, 3.B), Budget Recommendation (7.A, 7.B), and Behavioral Profiling (5.C), as the paper's core contribution involves a system for these tasks. The domain of Existing Systems & Gaps (4.A) was flagged as low relevance for its brief literature review. Mobile-First Design (9.A, 9.B) and System Evaluation (12.A) were flagged as contextual or low relevance due to being mentioned in future work or implied rather than a central focus. Domains like Filipino Cultural Context (2.A-D), Savings & Debt Management (13.A-C), and Anomaly Detection (8.A-C) were considered but rejected due to a lack of any mention, as the paper presents a general-purpose system without cultural, savings-specific, or anomaly detection features. The overall relevance of the paper to Odin is medium, as it provides a practical implementation of several core modules (categorization, clustering, visualization) but lacks deep technical depth and rigorous evaluation that would make it a high-relevance source.
limitations:
  - "The study is presented as a system design with no quantitative performance metrics or comparative analysis against other tools."
  - "The effectiveness of the auto-categorization and clustering algorithms is asserted but not empirically validated. [unacknowledged]"
  - "User adoption, retention, and engagement are not measured, limiting claims of real-world impact. [unacknowledged]"
remember_this:
  - "KMeans clustering groups expenses into patterns like low recurring or high occasional payments."
  - "Text analysis of transaction descriptions automates expense categorization for users."
  - "Graphical dashboards help users quickly identify key spending categories and unnecessary expenses."
  - "Real-time income-expenditure comparisons support effective financial decision-making."
  - "Future features include advanced analytics, mobile app support, and budget suggestion tools."

```
---

## Paper 9: Wang F. et al_summarized.md

**Source File:** `Wang F. et al_summarized.md`

```yaml
paper_id: 10.3390/s25010190
designation: international-algorithm-specific
title: A Survey of Deep Anomaly Detection in Multivariate Time Series: Taxonomy, Applications, and Directions
authors: Wang, F.; Jiang, Y.; Zhang, R.; Wei, A.; Xie, J.; Pang, X.
year: 2025
venue: Sensors
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
tldr: Comprehensive survey classifying deep learning MTSAD methods into forecasting, reconstruction, and contrastive paradigms with a taxonomy of anomaly types and application domains.
problem_and_motivation: Multivariate time series anomaly detection requires modeling complex temporal and inter-variable dependencies, which traditional statistical and machine learning methods struggle with. Deep learning offers powerful tools but lacks a unified, structured overview of techniques, paradigms, and applications to guide researchers and practitioners.
approach:
  - Proposes a new taxonomy for MTSAD methods based on learning paradigms (unsupervised, semi-supervised, self-supervised) and deep learning architectures.
  - Organizes methods into three primary strategies: forecasting-based, reconstruction-based, and contrastive-based anomaly detection.
  - Reviews and discusses 46 deep learning models including CNN, RNN, GNN, Transformer, VAE, GAN, and Diffusion-based approaches.
  - Compiles and organizes public MTSAD datasets, detailing their source, samples, dimensions, anomaly rate, and application domains.
  - Identifies open research issues, including contrastive learning, domain knowledge integration, benchmarking, and leveraging LLMs.
findings:
  - num: Transformers, GNNs, and hybrid models show superior performance in capturing spatio-temporal dependencies in MTS data.
  - num: Forecasting and reconstruction are the most common anomaly detection strategies, each with distinct advantages and drawbacks.
  - num: The survey covers 46 deep learning models across 10 application domains, highlighting the field's rapid expansion.
  - num: Contrastive learning and LLM-based methods are emerging as promising directions for improving anomaly detection accuracy and interpretability.
  - The taxonomy provides a structured framework that helps in selecting appropriate models based on data characteristics and application requirements.
key_figures_tables:
  - Figure 1: Classification of MTS anomaly types into intra-metric (temporal) and inter-metric anomalies → Anomalies occur within or between metrics.
  - Figure 2: Examples of point-wise and pattern-wise anomalies in MTS → Anomalies can be single-point spikes or unusual subsequences.
  - Figure 3: Examples of global and local inter-metric anomalies → Inter-metric anomalies involve broken correlations between variables.
  - Figure 4: General pipeline for MTSAD using deep learning models → Pipeline includes data processing, representation learning, and anomaly scoring.
  - Table 1: Overview of 46 deep learning models for MTSAD → Models are categorized by backbone, learning paradigm, and input type.
  - Table 2: Comprehensive list of public MTSAD datasets with application domains → Datasets span aerospace, cybersecurity, healthcare, and finance.
key_equations:
  - equation: X = (x1, x2, ..., xC)
    explanation: MTS X is defined as a collection of C univariate time series.
  - equation: S = (s1, s2, ..., sT)
    explanation: Anomaly scores S are computed for each time point t.
  - equation: |x_t - \hat{x}_t| > \delta
    explanation: Global point anomaly detection where deviation exceeds threshold.
  - equation: X_k = \sum_{t=0}^{T-1} x_t e^{-i2\pi kt/T}
    explanation: Discrete Fourier Transform for frequency domain analysis.
definitions:
  - term: MTSAD
    definition: Multivariate Time Series Anomaly Detection, identifying unusual patterns in multi-dimensional time series data.
  - term: Forecasting-based
    definition: Anomaly detection by comparing predicted future values with actual observations.
  - term: Reconstruction-based
    definition: Anomaly detection by measuring the error in reconstructing input data from a latent representation.
  - term: Contrastive-based
    definition: Anomaly detection by learning representations that maximize similarity between normal instances and dissimilarity with anomalies.
  - term: Intra-metric anomaly
    definition: Temporal anomaly occurring within a single metric or variable.
  - term: Inter-metric anomaly
    definition: Anomaly arising from broken relationships or correlations between multiple metrics.
critical_citations:
  - "[Hundman et al., 2018] — Introduced LSTM-NDT for spacecraft anomaly detection."
  - "[Deng & Hooi, 2021] — Proposed GDN using GNNs for MTS anomaly detection."
  - "[Xu et al., 2022] — Developed AnomalyTransformer with association discrepancy."
  - "[Su et al., 2019] — Proposed OmniAnomaly for robust MTS anomaly detection."
  - "[Audibert et al., 2020] — Introduced USAD for fast unsupervised MTS anomaly detection."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Reviews forecasting-based anomaly detection methods directly applicable to predicting spending anomalies.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Evaluates RNN, Transformer, and GNN models for sequential data forecasting.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Provides a comprehensive taxonomy and methods for anomaly detection in multivariate time series.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Reviews deep learning algorithms (VAE, GAN, Transformer) applicable to spending pattern anomalies.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Mentions privacy in cybersecurity datasets but does not focus on user financial data privacy.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: contextual
      justification: Discusses interpretability via XAI but not user trust specifically.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Reviews benchmarking datasets and evaluation metrics for anomaly detection.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Compares performance of various deep learning models on public datasets.
  contribution: "This survey directly informs Odin's predictive modeling and anomaly detection modules by providing a structured taxonomy of state-of-the-art deep learning methods for multivariate time series. The review of forecasting, reconstruction, and contrastive approaches offers design choices for implementing spending prediction and anomaly detection. The compiled dataset list and evaluation metrics can guide Odin's system evaluation framework. The discussion of open challenges, such as leveraging LLMs and integrating domain knowledge, suggests future enhancements for Odin's algorithmic modules."
  directly_justifies:
    - "Forecasting-based models can predict future spending and flag deviations as anomalies."
    - "Reconstruction-based models can detect anomalies by identifying patterns that do not conform to normal spending behavior."
    - "Contrastive learning can improve anomaly detection by learning discriminative representations of normal versus abnormal spending."
    - "LLMs can be adapted for time series anomaly detection in PFMS with appropriate prompting and fine-tuning."
  limits:
    - "Survey does not provide empirical comparisons or performance benchmarks across all reviewed models."
    - "Focuses on general MTSAD without specific application to personal finance or spending data."
    - "Limited discussion on real-time deployment considerations and computational resource constraints for mobile PFMS."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. High relevance was assigned to Predictive Modeling (6.A, 6.B) and Anomaly Detection (8.A, 8.B) because the paper's core contribution is a comprehensive review of deep learning methods for these tasks in MTS data. Medium relevance was assigned to System Evaluation (12.A, 12.B) as the paper reviews datasets and benchmarking practices. Contextual relevance was assigned to Data Privacy (10.A) and User Trust (10.B) due to passing mentions of security and interpretability, but no direct focus on user financial data or trust mechanisms. Domains like Filipino Cultural Context (2.A–2.D), Expense Categorization (3.A–3.C), Behavioral Profiling (5.A–5.C), and Savings/Debt Management (13.A–13.C) were considered but rejected as the paper does not address cultural, behavioral, or PFMS-specific financial management aspects. The paper's overall relevance to Odin lies in providing a foundational review of anomaly detection algorithms that can be adapted for spending anomaly detection and forecasting."
limitations:
  - "Survey does not provide empirical comparisons or performance benchmarks across all reviewed models."
  - "Focuses on general MTSAD without specific application to personal finance or spending data."
  - "Limited discussion on real-time deployment considerations and computational resource constraints for mobile PFMS. [unacknowledged]"
  - "Does not address the integration of user-declared financial preferences or constraints in anomaly detection. [unacknowledged]"
remember_this:
  - "MTSAD methods are classified into forecasting, reconstruction, and contrastive paradigms."
  - "Transformers and GNNs are leading architectures for capturing complex spatio-temporal dependencies."
  - "Contrastive learning and LLMs are emerging trends for improved anomaly detection."
  - "Anomalies can be point-wise, pattern-wise, or inter-metric, requiring diverse detection strategies."
  - "46 deep learning models reviewed across 10 application domains."
```
---

## Paper 10: Agrawal et al_summarized.md

**Source File:** `Agrawal et al_summarized.md`

```yaml
paper_id: 10.1007/s44196-025-00899-0
designation: international-algorithm-specific
title: Analyzing and Rewarding Credit Card Spending Habits in India: a Machine Learning Approach
authors: Agrawal, R.; Khanna, A.; Hamdare, S.
year: 2025
venue: International Journal of Computational Intelligence Systems
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 7.C
  - 12.A
  - 12.B
  - 12.C
tldr: Machine learning segments users and predicts spending to optimize credit card reward allocation, achieving an R2 of 0.99.
problem_and_motivation: Traditional credit card reward programs use static, one-size-fits-all structures that fail to personalize incentives for diverse spending behaviors. This lack of adaptability misses opportunities to retain high-value customers and encourage discretionary spending in profitable categories. A tailored, data-driven system is needed to optimize reward allocation and enhance customer engagement.
approach:
  - K-Means clustering segments users by spending behavior and card type (Platinum, Gold, Silver, Signature) using features like monthly spend and transaction frequency.
  - Synthetic data generation using Faker and feature engineering creates a rich dataset with attributes such as expense type, income, and attrition risk.
  - A custom reward points formula incorporates card type, promotion date, expense type, income, number of cards, and attrition risk to calculate personalized points.
  - Linear Regression, Random Forest, and XGBoost models predict reward points to validate the proposed formula's effectiveness.
  - Model performance is evaluated using R2, RMSE, and MAE to compare predictive accuracy.
findings:
  - "num: K-Means achieved a Silhouette Score of 0.42, outperforming DBSCAN and GMM for user segmentation by card type."
  - "num: Random Forest and XGBoost achieved an R2 value of 0.99, indicating near-perfect fit for reward point prediction."
  - "num: The synthetic dataset's reward points distribution ranged from 0 to 3500, compared to 0 to 1000 for the limited original dataset."
  - Clustering analysis clearly separated users into four distinct groups corresponding to Platinum, Gold, Silver, and Signature cardholders.
  - The proposed personalized reward formula allocated higher points for discretionary spending like travel and luxury, incentivizing profitable categories.
  - Including additional features like attrition risk and income category led to a more systematic and justified reward calculation process.
key_figures_tables:
  - "Figure 5: 3D visualization of K-Means clusters → Clear separation of four card-type based user segments."
  - "Figure 6: Reward point distribution comparison → Synthetic data enables broader and more justified point allocation."
  - "Figure 7: Cumulative distribution of reward points → Spending type influences reward allocation systematically."
  - "Table 4: Base reward points by card type → Platinum earns 5 points, Silver earns 2 points per 500 spent."
  - "Table 6: Expense type bonus points → Travel/Dining earns +3.0, Groceries/Bills earns +0.5."
key_equations:
  - equation: "RewardPoints(Olddataset) = (PointsScored(BasedonCardType) * AmountSpentMonthly) / 500"
    explanation: "Calculates points using only card type and amount spent."
  - equation: "RewardPoints(SyntheticDataset) = (ScoredPoints * AmountSpent) / 500, where ScoredPoints = [RCT + CPD + ET + IC + NoC + AR]"
    explanation: "Multi-factor formula for personalized reward point calculation."
definitions:
  - term: "RCT"
    definition: "Base multiplier based on Card Type for reward calculation."
  - term: "CPD"
    definition: "Card Promotion Date bonus for reward points."
  - term: "ET"
    definition: "Expense Type bonus based on spending category."
  - term: "IC"
    definition: "Income Category bonus for reward calculation."
  - term: "NoC"
    definition: "Number of Cards penalty for holding multiple cards."
  - term: "AR"
    definition: "Attrition Risk bonus to incentivize loyalty."
  - term: "DBI"
    definition: "Davies-Bouldin Index, a clustering validation metric."
critical_citations:
  - "[Cheema & Van der Stede, 2019] — Reward programs tailored to high-spending categories enhance engagement."
  - "[Li, Ngai, & Hu, 2021] — ML applications in finance include K-Means for segmentation."
  - "[Gan, Xu, & Chen, 2021] — Ensemble models like XGBoost predict consumer behavior in high-value categories."
  - "[Sun & Vasarhelyi, 2018] — Deep neural networks applied to predict credit card delinquencies."
  - "[Sadat Akash, 2024] — Credit Card Transaction Dataset used for training predictive models."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Directly segments users into behavioral profiles (e.g., luxury spenders) using clustering."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "medium"
      justification: "Synthetic data generation addresses data limitations for profile initialization."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Compares K-Means, DBSCAN, and GMM for behavioral profile classification."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Applies Linear Regression, Random Forest, and XGBoost to predict reward points."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "medium"
      justification: "Monthly spending trends analysis with synthetic data for forecasting."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "contextual"
      justification: "Reward optimization provides a framework analogous to budget allocation."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Reward structure offers a basis for personalized recommendation systems."
    - code: "7.C"
      name: "Constrained Optimization Approaches for Budget Allocation"
      relevance: "low"
      justification: "Reward points formula incorporates constraints like penalty for multiple cards."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Uses R2, RMSE, MAE to evaluate predictive model performance."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Evaluates clustering (Silhouette, DBI) and prediction (R2) modules."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "medium"
      justification: "Model performance comparison informs evaluation of recommendation systems."
  contribution: "This paper provides a data-driven framework for user segmentation and personalized incentive design applicable to Odin's expense categorization and budget recommendation modules. The K-Means clustering approach can inform Odin's behavioral profiling to classify users by spending habits. The multi-factor reward formula demonstrates a method for optimizing allocation based on user attributes, which parallels Odin's budget recommendation logic. The model evaluation metrics (R2, RMSE) offer a standard for assessing Odin's predictive modules. The framework's focus on incentivizing discretionary spending provides insights into engagement and retention mechanisms."
  directly_justifies:
    - "K-Means clustering effectively segments users by card type and spending behavior."
    - "Multi-factor reward formulas can personalize incentives based on user attributes."
    - "Random Forest achieves superior accuracy for predicting reward points."
    - "Synthetic data enables robust model development when real data is limited."
    - "Including attrition risk in reward calculation can support customer retention."
  limits:
    - "Study uses synthetic data, not real credit card transaction data."
    - "Reward points multipliers are subjective and not based on real industry data."
    - "Generalizability to other financial domains or countries is not evaluated."
    - "Real-time adaptability of the reward system is proposed but not implemented."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was conducted. The paper was flagged as highly relevant to Behavioral Profiling & Classification (5.A, 5.C) due to its K-Means user segmentation, and to Spending Forecasting (6.A, 6.B) for its predictive modeling. It also showed high relevance to System Evaluation (12.A, 12.B) through its use of R2, RMSE, and MAE. Medium relevance was assigned to Budget Recommendation (7.B) for the personalized reward formula's parallel to allocation logic, and Profile Dynamics (5.B) for its synthetic data approach addressing the cold-start problem. Low relevance was noted for Constrained Optimization (7.C) due to the simple penalty structure. Contextual relevance was assigned to Budgeting Strategies (7.A). Domains like Filipino Cultural Context (2.A-D), Expense Categorization (3.A-C), Existing Systems (4.A-B), Mobile-First Design (9.A-B), Data Privacy (10.A-B), User Retention (11.A-B), and Savings & Debt Management (13.A-C) were considered and rejected because the paper does not address cultural practices, expense categorization frameworks, PFMS landscape, mobile design, privacy concerns, engagement dynamics, or savings/debt management specifically. Overall, the paper's machine learning approach to user segmentation and personalized incentive optimization is highly relevant to Odin's core modules for behavioral profiling, forecasting, and recommendation."
limitations:
  - "Reliance on synthetically generated data limits real-world applicability. [unacknowledged]"
  - "Reward point multipliers are arbitrary and may not reflect actual credit card company practices. [unacknowledged]"
  - "The study does not validate the reward formula's impact on actual customer retention or spending. [unacknowledged]"
  - "Generalizability to Philippine financial context or Filipino young professionals is not addressed."
remember_this:
  - "K-Means clustering achieved 0.42 Silhouette Score for user segmentation."
  - "Random Forest and XGBoost both achieved R2 of 0.99 for reward prediction."
  - "Personalized rewards incentivize discretionary spending like travel and luxury."
  - "Synthetic data enables robust model development with limited real data."
  - "Multi-factor formulas enable dynamic and fair reward allocation."
```
---

## Paper 11: Mandaleeka_summarized.md

**Source File:** `Mandaleeka_summarized.md`

```yaml
paper_id: 10.63282/3050-922X.ICRCEDA25-143
designation: international-algorithm-specific
title: Explainable and Context-Aware Financial Nudges via Event-Driven Microservices
authors: Mandaleeka, A. P.
year: 2025
venue: International Journal of Emerging Research in Engineering and Technology, ICRCEDA2025 Conference Proceeding
odin_topics:
  - 3.A
  - 3.C
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 8.A
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 13.A
tldr: A microservices framework delivers real-time financial nudges enhanced by SHAP-based explanations, increasing user engagement and trust.
problem_and_motivation: Existing financial alerts are generic and lack transparency, causing user distrust and low engagement. There is a gap in integrating real-time personalization with explainable AI in scalable fintech architectures. The paper addresses this by proposing a modular system that combines context-awareness with interpretable decision-making.
approach:
  - Data ingestion from bank APIs, user behavior logs, and optional geolocation via Kafka topics.
  - Context processor enriches transactions with historical spending, budget goals, and temporal patterns.
  - Nudge decision engine uses rule-based logic or a trained ML model to classify events as nudge-worthy.
  - XAI module applies SHAP to generate feature attributions and convert them into natural-language explanations.
  - Notification service delivers formatted alerts via in-app, email, or chatbot with optional SHAP visualizations.
  - System is evaluated on synthetic and anonymized datasets to simulate diverse user behaviors.
findings:
  - Contextual triggers such as time, location, and prior habits increase user engagement.
  - Explainability boosts users' perceived relevance and trust in the system.
  - The modular architecture enables scalability, fault isolation, and data minimization.
  - SHAP provides local interpretability and supports model debugging and bias detection.
key_figures_tables:
  - Figure 1: Overview of the nudge system architecture → shows high-level data flow and services.
  - Figure 2: Detailed microservices and Kafka topics → illustrates modular, event-driven design.
  - Figure 3: Data ingestion pipeline → demonstrates transaction flow through context processor and nudge engine.
  - Table 1: SHAP attribution values for features → example of how spending and budget features contribute to nudge decision.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: SHAP
    definition: SHapley Additive exPlanations, a model-agnostic method for interpreting predictions by attributing contributions to input features.
  - term: XAI
    definition: Explainable Artificial Intelligence, techniques that make AI decisions understandable to humans.
  - term: Kafka
    definition: A distributed event-streaming platform for building real-time data pipelines and streaming applications.
critical_citations:
  - "[Lundberg and Lee, 2017] — foundational SHAP framework for model interpretability."
  - "[Kreps et al., 2011] — Kafka distributed messaging system for log processing."
  - "[Kim and Woo, 2021] — XAI framework for financial rating models."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Paper uses transaction categories for budget tracking, informing categorization frameworks.
    - code: 3.C
      name: User-Defined Allocation Constraints
      relevance: medium
      justification: User-defined budget thresholds and goals are central to nudge logic.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Paper reviews existing fintech systems like Cleo and Revolut, establishing the landscape.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies lack of explainability and generic alerts as key gaps.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Behavioral signals inform personalization, relevant to profiling.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: ML classification of nudge-worthy events aligns with behavioral classification approaches.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Spending spikes and threshold violations detected as anomalies trigger nudges.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Dedicated security and privacy section with OAuth, encryption, and consent management.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Explainability directly builds user trust; user study evidence cited.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: Focus on engagement dynamics through personalized, timely nudges.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: Nudges serve as retention mechanisms; system designed for repeated interaction.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Savings opportunities and goal reminders align with savings goal management.
  contribution: |
    The paper's microservices-based architecture with SHAP directly informs Odin's notification and explanation modules, enabling transparent spending alerts. The context-aware data pipeline, integrating transaction history, geolocation, and behavioral signals, can be adapted for Odin's behavioral profiling and anomaly detection. The emphasis on user trust via explainability and data privacy mechanisms supports Odin's design for ethical AI. The use of Kafka for event-driven scalability provides a blueprint for Odin's real-time processing and modular deployment.
  directly_justifies:
    - Explainability boosts users' perceived relevance and trust in financial nudges.
    - Contextual triggers (time, location, prior habits) increase user engagement.
    - Event-driven microservices enable scalable, fault-tolerant real-time processing.
    - SHAP provides transparent, individualized explanations for nudge decisions.
  limits:
    - Evaluation performed on synthetic and anonymized datasets, not real-world user studies.
    - SHAP computational cost requires optimizations like caching; may be expensive at scale.
    - The paper does not address cold-start scenarios for new users.
  mapping_rationale: |
    A systematic scan across all 12 functional domains and associated topics identified strong relevance to Engagement & Retention, Data Privacy & User Trust, and Existing Systems & Gaps. The paper directly addresses user trust (10.B) and privacy (10.A) through dedicated sections, and engagement (11.A) via nudging; it also reviews existing systems (4.A) and their limitations (4.B). Moderate relevance was found for Expense Categorization (3.A) and User-Defined Allocation (3.C) as the system uses budget thresholds and categories. Behavioral profiling (5.A) and classification (5.C) are touched via behavioral signals and ML decisioning; anomaly detection (8.A) is applicable due to spending spike detection. Savings management (13.A) is partially covered via savings opportunities and goal reminders. Topics related to Filipino cultural context (2.A-2.D), spending forecasting (6.A-6.B), budget recommendation optimization (7.A-7.D), mobile-first design (9.A-9.B), and system evaluation (12.A-12.C) were considered but rejected due to lack of emphasis or specificity. Borderline cases included seasonal spending (2.B) mentioned in passing but not culturally specific, and budget recommendation (7.A) referenced only as budget goals, not recommendation algorithms. Overall, the paper provides strong support for Odin's trust, engagement, and architectural modularity.
limitations:
  - Evaluation performed on synthetic and anonymized datasets, not real-world user studies.
  - SHAP computational cost requires optimizations like caching; may be expensive at scale.
  - The paper does not address cold-start scenarios for new users.
remember_this:
  - Explainable nudges increase user trust and perceived relevance.
  - Context-aware triggers boost engagement compared to generic alerts.
  - Modular microservices with Kafka enable scalable real-time financial advice.
```
---

## Paper 12: Chen & Tan_summarized.md

**Source File:** `Chen & Tan_summarized.md`

```yaml
paper_id: "10.1145/3785706.3785906"
designation: "international-algorithm-specific"
title: "LSTM-Based Consumer Behavior Prediction Model Research"
authors: "Chen, S.; Tan, W."
year: 2025
venue: "2025 2nd International Conference on Digital Economy and Computer Science (DECS 2025)"
odin_topics:
  - "6.A"
  - "6.B"
  - "5.C"
  - "12.B"
tldr: "An LSTM-based model with self-attention predicts consumer purchase intention using sequential behavioral data, achieving 94.2% accuracy."
problem_and_motivation: "Traditional consumer behavior analysis methods like regression and decision trees struggle with large-scale, multi-dimensional data and fail to capture temporal dependencies. Deep learning techniques have shown promise in complex pattern recognition, but a robust model for e-commerce purchase prediction is lacking. This study addresses the gap by leveraging LSTM networks to accurately forecast consumer purchasing behavior."
approach:
  - "Data preprocessing uses Apache Spark on 500,000 users with 80 million interaction records, applying sliding windows (30 days, 50% overlap) and extracting 128-dimensional features."
  - "The model architecture includes an embedding layer, bidirectional LSTM with 512 hidden units, self-attention with adaptive temporal weighting (alpha_t = softmax(e_t)), and a softmax output for five-class purchase intention."
  - "Optimization employs Adam with cosine annealing learning rate (0.001 to 0.0001), weighted cross-entropy loss, L2 regularization (λ=0.001), and gradient clipping (threshold 1.0)."
  - "Dropout scheduling starts at 0.5 for first 30 epochs, then linearly decreases to 0.3 for remaining training to balance regularization and fine-tuning."
  - "Training uses batch size 128, early stopping with patience 10, mixed-precision FP16, and data augmentation (temporal jitter, noise injection) to enhance robustness."
  - "Evaluation compares against logistic regression, random forest, SVM, basic RNN, and standard LSTM using accuracy, precision, recall, F1-score, and 10-fold cross-validation."
findings:
  - "num: The proposed LSTM achieves 94.2% accuracy, 93.8% precision, 94.7% recall, and 94.2% F1-score."
  - "num: It outperforms the best baseline (standard LSTM) by 3.0 percentage points and traditional ML methods by 10.7 percentage points on average."
  - "num: Statistical significance testing (p < 0.001) confirms performance improvements across user segments."
  - "num: High-frequency users achieve 96.1% accuracy, new users 91.8% (23.6% improvement over traditional methods), and high-value customers 96.7%."
  - "num: The self-attention mechanism improves key feature identification accuracy by 12.5%."
  - "Behavioral features (purchase frequency, browsing duration, price sensitivity) dominate predictive power with cumulative importance score 0.521."
  - "Ablation experiments show removing any Top-5 feature causes a 3.2 percentage point performance drop."
key_figures_tables:
  - "Table 2: Performance comparison across models → Proposed LSTM achieves highest metrics across all categories."
  - "Table 3: Performance by user groups → Model generalizes well, with new users at 91.8% accuracy."
  - "Figure 3: Training loss curves → Proposed LSTM converges faster and with lower final loss than traditional methods."
  - "Figure 4: Attention weight visualization → Recent behaviors and behavioral features receive highest attention weights."
key_equations:
  - equation: "α_t = softmax(e_t)"
    explanation: "Attention weight for timestep t based on score e_t."
definitions:
  - term: "LSTM"
    definition: "Long Short-Term Memory, a recurrent neural network architecture with gating mechanisms to capture long-term dependencies."
  - term: "RNN"
    definition: "Recurrent Neural Network, a class of neural networks for sequential data."
  - term: "SVM"
    definition: "Support Vector Machine, a supervised learning model for classification."
  - term: "AUC-ROC"
    definition: "Area Under the Receiver Operating Characteristic curve, a performance metric for binary classification."
  - term: "SHAP"
    definition: "SHapley Additive exPlanations, a method for interpreting model predictions."
critical_citations:
  - "None."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "The paper presents a predictive model for consumer behavior using LSTM, directly applicable to spending forecasting in Odin."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "The LSTM with self-attention is designed for sequential data forecasting, matching Odin's need for spending prediction."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "The model classifies users into purchase intention levels, informing profile classification methods."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "The paper provides extensive evaluation metrics and comparisons, useful for evaluating Odin's forecasting modules."
  contribution: "The LSTM-based forecasting approach can directly inform Odin's spending prediction module (6.A). The self-attention mechanism for temporal weighting could enhance Odin's ability to capture seasonal and cyclical spending patterns. The evaluation methodology using accuracy, precision, recall, and F1-score provides a template for Odin's algorithmic evaluation. The handling of new users with limited data offers strategies for Odin's cold-start problem in behavioral profiling."
  directly_justifies:
    - "LSTM networks effectively capture long-term dependencies in consumer behavior sequences."
    - "The model achieves 94.2% accuracy in predicting purchase intention using sequential data."
    - "Attention mechanisms improve key feature identification by 12.5%."
    - "Behavioral features like purchase frequency are more predictive than demographic features."
  limits:
    - "The paper focuses on e-commerce purchase prediction, not personal finance spending, limiting direct transferability."
    - "Error analysis reveals challenges with impulsive purchasing and external event-driven consumption, which Odin may also face."
    - "The model requires large-scale data and may not perform as well with sparse data typical of new users in Odin."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was found directly relevant to spending forecasting (6.A and 6.B) with high relevance, as it proposes an LSTM-based model for sequential purchase prediction. It also informs behavioral profiling (5.C) with medium relevance via its classification of users into intention levels, and evaluation frameworks (12.B) with medium relevance due to its comprehensive performance metrics. Borderline cases: the paper touches on seasonal patterns (2.B) but lacks Filipino cultural context, so was rejected; it mentions traditional method limitations (4.B) but does not review PFMS systems, so rejected; it does not address budget allocation (7.A–D) or anomaly detection (8.A–C), so those were rejected. Overall, the paper provides strong methodological support for Odin's predictive modules, though it is not domain-specific to Filipino young professionals."
limitations:
  - "The model is evaluated on e-commerce data, not personal financial transactions, limiting direct applicability to Odin's spending data. [unacknowledged]"
  - "The paper does not address real-time prediction constraints or mobile deployment, which are critical for Odin. [unacknowledged]"
  - "The reliance on large-scale data may not generalize to low-data scenarios common in early adoption of Odin. [unacknowledged]"
  - "The study does not consider privacy-preserving techniques, which are essential for Odin. [unacknowledged]"
  - "The model's performance on new users (91.8%) is reported but not deeply analyzed for cold-start issues. [unacknowledged]"
remember_this:
  - "LSTM with attention achieves 94.2% accuracy for purchase prediction."
  - "Behavioral features like frequency and duration are most predictive."
  - "The model generalizes well to new users with 91.8% accuracy."
  - "Attention weighting highlights recent behaviors and seasonal patterns."
  - "Dropout scheduling from 0.5 to 0.3 improves training stability."
```
---

## Paper 13: Caroprese et al_summarized.md

**Source File:** `Caroprese et al_summarized.md`

```yaml
paper_id: 10.1145/3707693
designation: international-algorithm-specific
title: Modelling Concept Drift in Dynamic Data Streams for Recommender Systems
authors: Caroprese, L.; Pisani, F. S.; Veloso, B. M.; Konig, M.; Manco, G.; Hoos, H.; Gama, J.
year: 2025
venue: ACM Transactions on Recommender Systems
odin_topics:
  - 5.A
  - 5.B
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
tldr: A stream-based data generator models user preferences with latent embeddings and simulates concept drift via tripartite graph changes, enabling realistic synthetic data for recommender system evaluation.
problem_and_motivation: Recommender systems assume static user preferences, but real-world data streams exhibit concept drift. Public datasets are limited and lack dynamic characteristics, hindering algorithm development and evaluation.
approach:
  - The model uses Bayesian Personalized Ranking (BPR) with latent embeddings for users and items to infer preferences based on geometric closeness.
  - Concept drift is detected using HDDM_W, a drift detection method based on Hoeffding's bounds with moving average.
  - Upon drift, the model is extended with new latent dimensions and retrained on current data while penalizing deviation from the previous model.
  - Synthetic data is generated by sampling from the learned model, using user and item popularity distributions (Zipf).
  - A general generator is proposed with six drift policies (user drift, new trends, new users/items, churn, obsolescence) to create controllable drift scenarios.
findings:
  - num: HR@5 on MIND dataset ranges from 0.6 to 0.7, with performance recovering after drift detection and retraining.
  - The synthetic data's frequency distribution closely matches the real data, confirmed by Kolmogorov-Smirnov test on MIND.
  - When users and items are inverted (more users than items), the generator fidelity improves significantly.
  - The adaptive BPR model outperforms a non-adaptive variational autoencoder when the item catalog grows over time.
  - Drift detection triggers structural model updates (adding latent dimensions) to adapt to changing preferences.
key_figures_tables:
  - Figure 3: Loss on test set for MIND dataset → Drifts are visible as spikes in loss, triggering model updates.
  - Figure 5: Comparison of real and synthetic frequency distributions for MIND → Synthetic matches real closely.
  - Figure 8: Comparison for Amazon Video Games → Poor match due to insufficient item preferences per user.
  - Figure 13: Improved match after inverting roles → Sufficient preferences per item improve generation.
key_equations:
  - equation: "\mathcal{L}_{bpr}(M|V) = \sum_{u}\sum_{i \succ_u j} \log \sigma(p_u^T(q_i - q_j))"
    explanation: BPR loss for optimizing user and item embeddings from pairwise preferences.
  - equation: "L_c(M;R) = \mathcal{L}_{bpr}(M|R) + \lambda(||P||_\infty + ||Q||_\infty)"
    explanation: Regularized loss for drift detection, bounding matrix weights.
  - equation: "L_d(M';M,R^{(t)}) = L_c(M';R^{(t)}) + \delta\sum_{u,k}|p'_{u,k}-p_{u,k}| + ..."
    explanation: Loss for adapting model after drift, penalizing embedding changes.
definitions:
  - term: BPR
    definition: Bayesian Personalized Ranking, a pairwise ranking optimization method for implicit feedback.
  - term: MF
    definition: Matrix Factorization, a collaborative filtering technique using latent factors.
  - term: HDDM_W
    definition: Hoeffding Drift Detection Method with weighted moving average, a concept drift detector.
critical_citations:
  - "[Rendle et al., 2009] — Foundation for BPR model used."
  - "[Frías-Blanco et al., 2015] — HDDM_W drift detection method."
  - "[Gama et al., 2004] — Early drift detection method (DDM) referenced."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Models user preference dynamics, directly applicable to profiling spending behavior.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: high
      justification: Addresses concept drift and changing user preferences, key for evolving profiles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Provides methods to handle concept drift in predictive models for spending forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Discusses sequential data and drift adaptation, relevant to spending forecasting.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Concept drift detection can inform anomaly detection by distinguishing normal changes from outliers.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Proposes drift detection algorithms that could be adapted for anomaly detection in spending.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Synthetic data generation aids evaluation of PFMS algorithms under dynamic conditions.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: The generator can be used to evaluate algorithmic robustness to concept drift.
  contribution: This paper's concept drift modeling can inform Odin's spending forecasting module by enabling adaptation to changing user spending patterns. Its drift detection methods can be integrated into anomaly detection to distinguish between genuine anomalies and normal preference shifts. The synthetic data generation approach provides a framework for evaluating Odin's algorithmic modules under realistic dynamic conditions. The emphasis on implicit feedback and user/item embeddings is relevant for profiling user financial behavior.
  directly_justifies:
    - Concept drift in user preferences can be modeled via latent embedding changes.
    - Drift detection methods like HDDM_W can trigger model retraining to maintain performance.
    - Synthetic data streams with controlled drift can be used to evaluate system robustness.
    - Adaptive models outperform static models when new items appear over time.
  limits:
    - None identified.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The following domains were flagged as relevant: Behavioral Profiling & Classification (codes 5.A, 5.B) because the paper explicitly models user preference dynamics and drift; Spending Forecasting (6.A, 6.B) because concept drift directly impacts prediction accuracy; Anomaly Detection (8.A, 8.B) because drift detection techniques are core to the paper; and System Evaluation (12.A, 12.B) due to the synthetic data generator for evaluation. These were assigned high relevance except 8.A and 12.A/12.B which are medium as they are secondary. Domains like Expense Categorization, Budget Recommendation, Mobile Design, Privacy, and Retention were considered and rejected because the paper does not address these aspects. Borderline cases: the paper's discussion of user preference changes could relate to seasonal spending (2.B), but it does not specifically address cyclical patterns, so we did not assign that. Overall, the paper is highly relevant to Odin's algorithmic modules that deal with dynamic user behavior and evaluation.
limitations:
  - The model assumes geometric closeness in latent space, which may not capture all preference dynamics.
  - Synthetic data fidelity drops with sparse item preferences.
  - New user/item strategies are not fully developed. [unacknowledged]
remember_this:
  - num: HR@5 on MIND dataset ranges from 0.6 to 0.7 after adaptation.
  - Drift detection triggers model retraining to maintain recommendation accuracy.
  - Synthetic data can replicate real frequency distributions when enough interactions exist.
  - Adaptive models outperform static models under concept drift.
```
---

## Paper 14: Mehta et al_summarized.md

**Source File:** `Mehta et al_summarized.md`

```yaml
paper_id: 0e6b8a1c-6c3c-53df-9b34-a8fa8b7f9d91
designation: international-algorithm-specific
title: "Clustering and Similarity Learning in Financial Markets: A Tutorial for the Practitioners"
authors: "Mehta, D.; Thompson, J.R.J.; Lee, H.; Lee, Y."
year: 2025
venue: Unknown
odin_topics:
  - 1.A
  - 2.A
  - 2.B
  - 3.A
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 7.C
  - 8.A
  - 8.B
  - 9.A
  - 9.B
  - 10.A
  - 12.B
tldr: This tutorial synthesizes clustering and similarity learning methods, demonstrating their application in investment workflows to build adaptive neighborhoods of securities, funds, companies, and investors for improved decision-making.
problem_and_motivation: Traditional peer-grouping methods such as industry codes or static style boxes are coarse, rigid, and fail to capture actual risk and thematic exposures. There is a need for adaptive, data-driven similarity systems that can integrate heterogeneous data to support real-world financial decision-making.
approach:
  - Reviews clustering methods across modalities: tabular (k-means, hierarchical), time-series, text, graphs, and images.
  - Covers similarity learning methods including metric learning, random forest proximities, Siamese networks, graph neural networks, and multimodal fusion.
  - Focuses on methodologies for fixed income, mutual funds, companies, and investors, emphasizing supervised and semi-supervised learning approaches.
  - Discusses evaluation protocols like substitution fidelity, neighborhood stability, and segment utility to align with fiduciary objectives.
  - Provides practical guidelines for design choices, including metric selection, normalization, and ensuring interpretability through feature importance or SHAP values.
findings:
  - Supervised similarity frameworks allow funds to be quantified against their declared categories and flag outliers transparently.
  - Random forest proximities enable bond substitution by aligning distances with desk use cases like relative value and surveillance.
  - Multimodal pipelines that combine tabular, text, and graph data produce robust company similarity comparable sets for valuation and strategy.
  - Graph neural networks using fund-bond bipartite structures improve price and yield prediction, supporting peer retrieval.
  - num: Nearly one-fifth of U.S. investment-grade volume now trades in baskets, necessitating robust portfolio-level similarity metrics like STRAPSim.
  - The tutorial identifies that traditional academic metrics like Silhouette or ARI are insufficient; practitioner validation (e.g., substitution fidelity) is critical.
key_figures_tables:
  - "Exhibit 1: Usecases of Clustering and Similarity Learning in Financial Markets → Highlights broad applications from risk to personalization."
  - "Exhibit 5: Evaluation methodologies: academic vs. practitioner perspectives → Shows shift from abstract metrics to operational validity."
  - "Exhibit 10: Clustering and similarity applications for investors across data modalities → Illustrates how transaction and profile data create client segments."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "SR 11-7"
    definition: "A regulatory guidance emphasizing model risk management, requiring documentation and reproducibility."
  - term: "GICS"
    definition: "Global Industry Classification Standard, a common but static taxonomy for company sectors."
  - term: "DTW"
    definition: "Dynamic Time Warping, a distance metric for measuring similarity between two time series with varying speeds."
  - term: "KYC"
    definition: "Know-Your-Client, a regulatory process involving client identification and risk profiling."
critical_citations:
  - "[Jeyapaulraj et al., 2022] — Demonstrates supervised similarity for corporate bonds."
  - "[Mehta et al., 2020] — Shows fund categories are reproducible using supervised learning."
  - "[Barberis et al., 2005] — Documents return co-movement being better explained by data than GICS/SIC."
  - "[Thompson et al., 2021] — Applies clustering to understand investor behavioral types."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "contextual"
      justification: "Paper discusses general investor profiling, applicable but not specific to Filipino context."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "low"
      justification: "General financial behavior analysis; lacks cultural specificity to Filipino customs."
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "medium"
      justification: "Discusses regime identification and time-series patterns, applicable to seasonal spending."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "low"
      justification: "Focuses on financial securities clustering, not transactional expense categorization."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Provides overview of traditional financial data analysis methods, informing system landscape."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Directly critiques static taxonomies and heuristic peer groups, justifying data-driven systems."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Provides methodologies for classifying investor types based on behavior and risks."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "medium"
      justification: "Addresses regime shifts and adaptability in profiles but does not explicitly solve cold-start."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Reviews supervised and unsupervised classification methods (e.g., K-means, metric learning)."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Discusses time-series forecasting and regime prediction using clustering."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Covers DTW, correlation, and deep learning methods for sequential data."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "medium"
      justification: "Provides context on how expert input (e.g., risk tolerance) shapes similarity models."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "low"
      justification: "Does not directly address budget recommendation, but uses constraints in related domains."
    - code: "7.C"
      name: "Constrained Optimization Approaches for Budget Allocation"
      relevance: "contextual"
      justification: "Mentions scenario reduction and constraints implicitly but not directly for budgets."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Discusses open-set recognition and outlier detection for funds and transactions."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Reviews density-based clustering and open-set learning, applicable to detecting fraudulent transactions."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "contextual"
      justification: "Focuses on algorithmic and analytical workflows, not UI/UX design."
    - code: "9.B"
      name: "Mobile UX Design for Personal Finance"
      relevance: "contextual"
      justification: "Not a focus of the paper."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "contextual"
      justification: "Mentions governance but does not address specific security or privacy algorithms."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Dedicated section on evaluating similarity models with operational criteria (substitution fidelity, stability)."
  contribution: "This tutorial provides a comprehensive framework for building adaptive similarity systems that can be directly adapted for Odin's behavioral profiling module. Its detailed review of evaluation methodologies, particularly the shift from academic to operational validity, justifies Odin's focus on user-validated performance metrics. The integration of multimodal data (transactions, user profiles, and text) informs Odin's architecture for constructing robust user profiles and forecasting spending. Furthermore, the discussion of open-set recognition directly supports Odin's anomaly detection capabilities."
  directly_justifies:
    - "Adaptive, data-driven similarity systems are required to replace coarse, rigid peer-grouping methods."
    - "Evaluation of financial algorithms must focus on substitution fidelity and neighborhood stability, not abstract indices."
    - "Multimodal pipelines (tabular, text, graph) are essential for robust peer discovery in sparse data environments."
    - "Supervised and semi-supervised learning frameworks provide transparent mechanisms for flagging outliers and category drift."
  limits:
    - "The tutorial focuses on investment and securities, not direct personal expense management."
    - "The evaluation metrics discussed (e.g., substitution fidelity) are not directly transferable to PFMS without adaptation."
    - "Many advanced models (e.g., GNNs) sacrifice interpretability, a key requirement for Odin's user-facing analytics."
  mapping_rationale: "A systematic scan of all 12 functional domains was performed. The paper's core contribution on adaptive similarity and clustering directly aligns with high relevance to Behavioral Profiling (5.A, 5.C), Spending Forecasting (6.A, 6.B), and Anomaly Detection (8.A, 8.B), as it provides the theoretical and algorithmic foundation for these modules. The domain of Existing Systems (4.A, 4.B) is highly relevant due to the paper's strong critique of static heuristic methods, justifying Odin's data-driven approach. Evaluation (12.B) is directly supported. For domains like Expense Categorization (3) and Budget Recommendation (7), the paper offers context (e.g., on constrained optimization) but lacks specific application to PFMS, hence relevance is low/contextual. The paper's focus on financial instruments, rather than Filipino young professionals, means topics under Domain 1 are contextual. Borderline cases like seasonal spending (2.B) are touched upon via regime detection, but the paper does not focus on personal cycles. Overall, the paper is highly relevant for Odin's core algorithmic modules but only contextual or not applicable to UI/UX, privacy, or cultural specifics."
limitations:
  - "Paper is a tutorial and thus does not present a novel algorithm or empirical validation of a specific system."
  - "The applicability of the discussed 'operational validity' metrics to a PFMS like Odin is not explicitly explored. [unacknowledged]"
  - "Does not address the specific cold-start problem of a new user in a PFMS, despite mentioning similar challenges."
remember_this:
  - "Static peer groups are obsolete; adaptive data-driven similarity systems are required for modern analytics."
  - "Evaluation of similarity systems must prioritize operational validity over academic metrics."
  - "Multimodal data integration is the key to achieving robust peer discovery and user profiling."
  - "Supervised similarity frameworks can transparently flag outliers and category drift in user behavior."
  - "Deep learning methods often sacrifice interpretability, necessitating governance frameworks like SR 11-7."
```
---

## Paper 15: Bader & Haraty_summarized.md

**Source File:** `Bader & Haraty_summarized.md`

```yaml
paper_id: 10.12785/ijcds/1571107231
designation: international-algorithm-specific
title: Bridging AI and Emotion: Enhanced Models for Personal Finance Manager Applications
authors: Bader, S.; Haraty, R. A.
year: 2025
venue: International Journal of Computing and Digital Systems
odin_topics:
  - 3.A
  - 4.B
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 8.C
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 12.A
  - 12.B
  - 13.B
tldr: Integrates deep learning and sentiment analysis into a .NET Core-based financial advisor application for enhanced anomaly detection, spending prediction, and personalized merchant recommendations.
problem_and_motivation: Existing financial platforms process structured data but fail to leverage unstructured user inputs and emotional context, leading to generic and ineffective financial recommendations. This gap limits user satisfaction and the potential for truly personalized financial guidance. A solution is needed that analyzes user behavior, sentiment, and transaction patterns to provide adaptive financial advice.
approach:
  - Developed a .NET Core 6 application integrating Python-based AI modules for anomaly detection, forecasting, and sentiment analysis.
  - Used TensorFlow/Keras to implement Transformer, Temporal Convolutional Network (TCN), and N-BEATS models for predictive modeling of spending behavior.
  - Implemented anomaly detection using Isolation Forest, Local Outlier Factor (LOF), and One-Class SVM algorithms on transactional data.
  - Incorporated Natural Language Processing (NLP) using fine-tuned BERT and GPT models for sentiment analysis on transaction descriptions to categorize user emotions.
  - Evaluated models with and without sentiment analysis using MAPE, accuracy, precision, recall, and ROC-AUC metrics, and compared against traditional fintech solutions.
findings:
  - num: Integrating sentiment analysis improved predictive accuracy, reducing MAPE from 10.5% to 7.8% across models.
  - num: The Transformer model achieved the lowest RMSE of 0.062 with sentiment, while N-BEATS was the best performer at 0.057.
  - num: Anomaly detection system achieved 92% accuracy, with 90% precision and 85% recall, yielding an F1-score of 87.5%.
  - num: Predictive models incorporating sentiment analysis achieved 88% alignment with actual user behavior within a 90% confidence interval.
  - The N-BEATS model excelled at breaking down time-series data into trends and seasonality, providing interpretable forecasts.
key_figures_tables:
  - Figure 1: System architecture showing integration of transaction, merchant, and account data with AI analytics layers.
  - Figure 13: Transformer model predictions without sentiment analysis, showing it captures actual spending behavior.
  - Figure 16: Transformer model predictions with sentiment analysis, showing improved accuracy and closer fit to actual spending data.
  - Table 1: Comparison showing our approach's superior anomaly detection precision (90% vs. 70-80%) and predictive accuracy (MAPE 7.8% vs. 10-12%) over existing fintech solutions.
key_equations:
  - equation: MAPE = (1/n) * Σ(|(Actual - Predicted)| / Actual) * 100
    explanation: Measures average prediction error as a percentage.
  - equation: Precision = TP / (TP + FP)
    explanation: Ratio of correctly identified positive instances.
  - equation: Recall = TP / (TP + FN)
    explanation: Ratio of actual positives correctly identified.
definitions:
  - term: MCC
    definition: Merchant Category Code, a standardized classification for businesses.
  - term: MAPE
    definition: Mean Absolute Percentage Error, a metric for forecasting accuracy.
  - term: ROC-AUC
    definition: Receiver Operating Characteristic - Area Under the Curve, measures model discrimination ability.
  - term: N-BEATS
    definition: Neural Basis Expansion Analysis for Interpretable Time Series Forecasting.
  - term: TCN
    definition: Temporal Convolutional Network, a model for sequence prediction.
critical_citations:
  - "[Chollet, 2017] — Deep learning with Python framework used."
  - "[Bollen et al., 2011] — Demonstrated social media sentiment's impact on stock markets."
  - "[Goodfellow et al., 2016] — Foundational deep learning text referenced for methodology."
  - "[Johnson, 2024] — Integration of sentiment and knowledge graphs for fintech decision support."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Uses MCC and user-defined categories to structure transaction data for AI analysis.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Explicitly identifies that existing financial platforms fail to use unstructured user data and emotional context.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Builds user profiles using transaction history, sentiment, and spending behavior for personalized advice.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Categorizes users into emotional and behavioral segments (e.g., Health-Focused, Adventurous) using sentiment analysis.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Core contribution involves implementing deep learning models (Transformer, TCN, N-BEATS) for financial forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Specifically evaluates TCN, N-BEATS, and Transformers on sequential transaction data for spending prediction.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Predictions are used to generate personalized budgeting recommendations and financial forecasts.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: The application provides budget creation and tracking features based on predictive insights.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: A primary objective is to implement AI-driven anomaly detection to improve financial transaction security.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Uses Isolation Forest, LOF, and One-Class SVM to detect fraudulent and irregular transactions.
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: contextual
      justification: Discusses training models on historical data to establish baselines for anomaly detection.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: Mentions web/mobile front-end but does not focus on mobile-first principles.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: Discusses dashboards and user interface but not UX design principles specifically.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Mentions vulnerability assessments and secure integration using .NET Core, but not a deep focus.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Security alerts and transparent anomaly detection aim to build user confidence.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Personalization and merchant recommendations are designed to enhance user engagement.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: low
      justification: Suggests feedback loops and continuous learning to improve recommendations over time.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Employs MAPE, precision, recall, and ROC-AUC to rigorously evaluate algorithmic modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides a comparative analysis of anomaly detection and predictive models with and without sentiment integration.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: contextual
      justification: Mentions credit cards and high-yield savings accounts in a supporting, but not central, context.
  contribution: This paper provides a comprehensive blueprint for integrating sentiment analysis with deep learning (Transformer, TCN, N-BEATS) and anomaly detection (Isolation Forest, LOF) in a personal finance application. The methodology and comparative results offer direct justification for Odin's predictive analytics module and its anomaly detection engine. The discussion on personalized merchant recommendations provides a model for Odin's user engagement features. The evaluation framework using MAPE, precision, recall, and ROC-AUC can guide Odin's system evaluation strategy. The discussion of real-time adaptability and user feedback loops informs Odin's design for continuous learning and retention.
  directly_justifies:
    - "The system architecture integrates transaction, merchant, and account data for holistic financial analysis."
    - "Deep learning models (Transformer, TCN, N-BEATS) can effectively forecast user spending patterns."
    - "Sentiment analysis of transaction data and merchant matching significantly improves the accuracy of personalized financial recommendations."
    - "Anomaly detection using Isolation Forest and One-Class SVM achieved 92% accuracy in identifying fraudulent transactions."
    - "Continuous model retraining based on user feedback and new data is essential for maintaining prediction accuracy."
  limits:
    - "Results are based on a limited dataset which may not represent all user demographics."
    - "Computational efficiency of deep learning models remains a concern for real-time, high-volume applications."
    - "User trust and adoption of AI-driven financial advice are not directly studied in this work."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant for domains related to Behavioral Profiling (5.A, 5.C), Spending Forecasting (6.A, 6.B), Anomaly Detection (8.A, 8.B), and System Evaluation (12.A, 12.B) because it provides specific algorithmic implementations and evaluations. Medium relevance was assigned to Expense Categorization (3.A) due to its use of MCC codes, and to Data Privacy (10.A) and User Trust (10.B) where security and confidence are mentioned but not central. Low relevance was assigned to Mobile-First Design (9.A, 9.B) as the paper focuses on backend AI rather than UX principles. Domains not explicitly supported include Savings & Debt Management (13.A, 13.C) and User-Declared Preferences (2.C), which are mentioned contextually but lack substantive contribution. The overall contribution is highly relevant to Odin's design, offering validated models and an evaluation framework for several core algorithmic modules.
limitations:
  - "The performance of the models is evaluated on a specific dataset, which may not be generalizable across diverse populations and financial behaviors."
  - "The computational resources required for training and deploying Transformer and TCN models could be a barrier for resource-constrained environments. [unacknowledged]"
  - "Potential for bias in sentiment analysis models based on the language and context of transaction data was not explicitly addressed. [unacknowledged]"
  - "The study does not include user studies to measure the real-world impact on financial well-being or user satisfaction."
  - "Real-time processing of unstructured data (e.g., social media sentiment) is identified as a future challenge but not fully addressed."
remember_this:
  - "Integrating sentiment analysis into financial models improves spending prediction accuracy."
  - "The N-BEATS model was the best performer for interpretable time-series forecasting."
  - "Anomaly detection system achieved 92% accuracy in identifying fraudulent transactions."
  - "AI-driven merchant recommendations are a key feature for user engagement."
  - "Continuous learning from user feedback is vital for maintaining model performance."
```
---

## Paper 16: Qin_summarized.md

**Source File:** `Qin_summarized.md`

```yaml
paper_id: "10.21203/rs.3.rs-7351508/v1"
designation: international-algorithm-specific
title: Multimodal deep learning framework for shadowbanking risk prediction - dynamic decisionoptimization integrating knowledge graph andreinforcement learning
authors: "Qin, T."
year: 2025
venue: Research Square
odin_topics:
  - "6.A"
  - "6.B"
  - "8.A"
  - "8.B"
  - "12.A"
tldr: A multimodal deep learning framework combining graph neural networks and reinforcement learning predicts shadow banking risk with superior accuracy and policy compliance.
problem_and_motivation: Shadow banking poses systemic risks that traditional statistical and econometric models fail to capture due to static assumptions and limited interdependency modeling. Existing approaches lack regulatory interpretability and real-time scalability for complex financial ecosystems. A unified framework is needed that integrates structural learning, anomaly detection, and policy-aware optimization.
approach:
  - "Proposes GFA-Net, a graph-theoretic neural architecture that encodes financial systems as dynamic transaction graphs with semantic and regulatory features."
  - "Introduces PCS-Flow, a policy-aware strategic module with scenario perturbations, regulatory embeddings, and compliance-aware objectives."
  - "Uses four datasets: CRSP (transactional records), Compustat (account balances), WRDS (cash flows), and Quandl (expense submissions)."
  - "Employs a Transformer-based encoder with 4 layers, 8 attention heads, and 256 hidden dimensions for sequence modeling."
  - "Trains with AdamW optimizer, cosine decay schedule, batch size 64, and mixed precision on NVIDIA A100 GPUs."
  - "Evaluates against baselines including BPRMF, NCF, LightGCN, DGCF, SVD++, and GRU4Rec using Precision, Recall, NDCG, and MAP."
  - "Conducts ablation studies removing temporal encoding, hierarchical feature fusion, and residual attention to validate each component."
findings:
  - "num: On CRSP, the model achieves Precision 0.391, Recall 0.356, NDCG 0.403, and MAP 0.294, outperforming DGCF by 2.1–2.4 absolute points."
  - "num: On Compustat, the model improves NDCG by 2.7% and MAP by 1.5% over the next best baseline."
  - "num: On Quandl, the model achieves Precision 0.379 and NDCG 0.392, substantially outperforming GRU4Rec and DGCF."
  - "Removing temporal encoding reduces NDCG by 3.3 points on CRSP and 3.2 points on Compustat, confirming the importance of temporal dependencies."
  - "Hierarchical feature fusion and residual attention are both essential for precision-sensitive tasks like anomaly detection."
  - "The model maintains stable standard deviations across multiple runs, demonstrating robustness and generalization in dynamic financial environments."
key_figures_tables:
  - "Table 1: Benchmark on CRSP and Compustat → Model consistently outperforms all baselines across all four metrics."
  - "Table 2: Benchmark on WRDS and Quandl → Model maintains superior performance on noisier, more variable datasets."
  - "Table 3: Ablation on CRSP and Compustat → Each component contributes significantly, with residual attention most critical for MAP."
  - "Table 4: Ablation on WRDS and Quandl → Temporal encoding and hierarchical fusion are both essential for robust generalization."
  - "Figure 5: GFA-Net architecture → End-to-end pipeline from raw data to graph encoding, temporal modeling, and semantic alignment."
  - "Figure 6: Graph representation learning with multi-head attention → Multi-head attention integrates graph structures at varying receptive field radii."
  - "Figure 7: PCS-Flow strategy → Three-stage architecture with Conditional Residual Blocks and Dynamic Mixture-of-Experts for scenario simulation."
  - "Figure 8: Embedding policy conditions → Dual-path attention computation comparing optimal and saturation covariance conditions."
key_equations:
  - equation: "B(t+1) = B(t) + ∑_{k=1}^{K_t} e_k(t) + P(t)"
    explanation: "Dynamic evolution of account balances with transactions and policy adjustments."
  - equation: "L_id(t) = || C_a^T B(t) - (C_l^T B(t) + C_e^T B(t)) ||_2^2"
    explanation: "Quadratic penalty enforcing the fundamental balance sheet identity."
  - equation: "h_i^{(l+1)} = h_i^{(l)} + σ( W_2 · ∑_{j∈N(i)} ψ(h_j^{(l)}, F_{ji}^{(t)}) )"
    explanation: "Skip-connected GNN layer update for residual structure and gradient flow."
  - equation: "z(t+1) = GRU(H(t), z(t))"
    explanation: "Gated recurrent unit captures temporal dependencies across accounting periods."
  - equation: "L_policy = || r_{p_b}^{(t)} - Π_{p_a←p_b}(r_{p_b}^{(t)}) ||_2^2"
    explanation: "Policy-consistency constraint translating reporting semantics between regimes."
  - equation: "L_PCS = ∑_{t=1}^n ( λ_5 L_policy^{(t)} + λ_6 L_temporal-consistency^{(t)} ) + λ_7 ∑_{j=1}^r (1-γ_j)^2"
    explanation: "Integrated PCS-Flow objective balancing policy consistency, temporal smoothness, and compliance."
definitions:
  - term: "GFA-Net"
    definition: "Graph-Fused Accounting Network, a graph-theoretic neural architecture for encoding financial transactions."
  - term: "PCS-Flow"
    definition: "Policy-Consistent Scenario Flow Strategy, a regulatory-aware strategic framework for financial state evolution."
  - term: "GNN"
    definition: "Graph Neural Network, a class of neural networks operating on graph-structured data."
  - term: "RL"
    definition: "Reinforcement Learning, a learning paradigm where agents optimize policies through interaction with an environment."
  - term: "KG"
    definition: "Knowledge Graph, a structured representation of entities and their relationships."
  - term: "GRU"
    definition: "Gated Recurrent Unit, a recurrent neural network architecture for sequence modeling."
  - term: "NDCG"
    definition: "Normalized Discounted Cumulative Gain, a ranking quality metric."
  - term: "MAP"
    definition: "Mean Average Precision, a ranking and retrieval performance metric."
critical_citations:
  - "[Gennaioli, Shleifer & Vishny, 2013] — Foundational model of shadow banking dynamics."
  - "[Adrian & Ashcraft, 2012] — Framework for shadow banking regulation and systemic risk."
  - "[Huang, 2018] — Economic theory connecting banking and shadow banking."
  - "[Ricks, 2010] — Shadow banking and financial regulation in legal context."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "low"
      justification: "Paper focuses on systemic risk prediction, not personal spending forecasting."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "low"
      justification: "Uses forecasting for risk in shadow banking, not personal spending sequences."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "low"
      justification: "Paper includes anomaly detection, but for financial systemic risk, not personal transactions."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "low"
      justification: "Methods are algorithmic but applied to enterprise-level financial data."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "contextual"
      justification: "Evaluation methodology is for risk prediction, not PFMS modules."
  contribution: "This paper's graph-based neural architecture for financial transaction modeling could inform anomaly detection modules in Odin through its graph representation learning. The temporal encoding and hierarchical feature fusion techniques are transferable to forecasting spending behavior. However, the domain is shadow banking risk prediction, not personal finance management, so direct applicability is limited. The paper provides evidence that graph neural networks with policy-aware constraints can handle sequential financial data with irregular patterns."
  directly_justifies:
    - "Graph neural networks can model temporal and relational dependencies in financial transaction data."
    - "Temporal encoding is critical for capturing periodic and sequential patterns in financial flows."
    - "Anomaly detection in financial data benefits from hierarchical feature fusion and residual attention."
    - "Policy-consistent constraints improve compliance and interpretability of financial predictions."
  limits:
    - "Paper addresses shadow banking systemic risk, not personal finance for young professionals."
    - "Datasets are CRSP, Compustat, WRDS, Quandl—enterprise-level financial data, not individual spending."
    - "No user behavioral profiling or demographic analysis relevant to Odin's target population."
    - "Mobile-first design and user retention mechanisms are entirely absent."
    - "Evaluation is on risk prediction accuracy, not on user trust, engagement, or savings outcomes."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant to the Forecasting domain (topics 6.A, 6.B) due to its use of time-series prediction and sequential modeling, and to the Anomaly Detection domain (8.A, 8.B) due to its anomaly detection component. Topic 12.A (Evaluation Frameworks) was also flagged at contextual relevance for its experimental methodology. Borderline cases included topics 10.A and 10.B (Data Privacy and User Trust), which were considered due to the paper's compliance and policy-consistency emphasis, but rejected because the compliance refers to banking regulation, not user trust in PFMS. Topics under Filipino Cultural Context (2.A–2.D), Expense Categorization (3.A–3.C), Behavioral Profiling (5.A–5.C), Budget Recommendation (7.A–7.D), Mobile-First Design (9.A–9.B), User Retention (11.A–11.B), and Savings & Debt Management (13.A–13.C) were considered and rejected due to no mention of personal finance, Filipino demographics, or PFMS-specific concerns. Overall, the paper provides low-to-contextual relevance to Odin, offering algorithmic techniques transferable in principle but not directly applicable to the PFMS domain."
limitations:
  - "Single-author study without external validation or replication."
  - "Datasets are proprietary and not publicly described in sufficient detail."
  - "The shadow banking domain differs fundamentally from personal finance, limiting generalizability."
  - "No human-in-the-loop evaluation or user studies for interpretability claims."
  - "The paper does not address privacy-preserving mechanisms for financial data. [unacknowledged]"
  - "No discussion of real-time deployment constraints or latency requirements. [unacknowledged]"
remember_this:
  - "Graph neural networks with temporal encoding outperform static models on sequential financial data."
  - "Removing temporal encoding reduces NDCG by 3.3 points on CRSP."
  - "Hierarchical feature fusion and residual attention are both essential for precision-sensitive tasks."
  - "Policy-consistent constraints improve compliance and interpretability without sacrificing accuracy."
  - "The framework maintains stable performance across multiple runs, indicating robustness."
```
---

## Paper 17: Tabak et al_summarized.md

**Source File:** `Tabak et al_summarized.md`

```yaml
paper_id: 10.3390/su17209219
designation: international-algorithm-specific
title: Assessing the Drivers of Financial Vulnerability and Fraud in Brazil: The Critical Role of Financial Planning over Literacy
authors: Tabak, B.M.; Cardoso, D.H.; Silva, C.C.
year: 2025
venue: Sustainability
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 7.A
  - 7.B
  - 7.D
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
  - 13.A
  - 13.C
  - 4.A
  - 4.B
tldr: Financial planning more strongly predicts reduced vulnerability and fraud than financial literacy does, with machine learning confirming planning as the dominant driver over knowledge.
problem_and_motivation: Financial literacy research is fragmented, with studies examining knowledge, behavior, and cognitive biases in isolation. This fragmentation leaves unclear how these forces interact to impact financial resilience and sustainability. A unified framework is needed to simultaneously examine these interconnected components.
approach:
  - Data from 256 respondents in Brazil's Federal District using convenience sampling at urban focal points.
  - Developed and validated a six-factor measurement instrument using Confirmatory Factor Analysis (CFA).
  - Evaluated seven machine learning algorithms in a horse race, selecting Random Forest as the best performer.
  - Applied SHAP and LIME for model interpretability to identify key predictors of financial vulnerability and fraud.
  - Used multiple linear regression (OLS) with robust standard errors to assess relationships between variables.
findings:
  - num: Financial Planning had a −0.642 correlation with Financial Vulnerability and −0.375 with Fraud, stronger than Financial Literacy.
  - num: Random Forest achieved the lowest RMSE in predicting financial vulnerability, outperforming other algorithms.
  - Financial Planning was identified as the strongest predictor of financial vulnerability and fraud by both SHAP and LIME.
  - num: The Cognitive Reflection Test (CRT) showed a strong positive relationship with financial literacy (coef. 0.502).
  - Black respondents were more financially vulnerable (coef. 0.156), indicating social inequality.
  - Women had lower levels of financial literacy (coef. −0.140), reflecting social barriers.
  - num: High-income individuals had higher levels of financial literacy (coef. 0.348).
  - Converging evidence confirms planning practices are more important than financial knowledge in reducing financial distress.
  - The six-factor CFA model showed excellent fit (CFI = 0.954, TLI = 0.950, RMSEA = 0.039).
key_figures_tables:
  - Figure 2: Horse racing outcomes comparing seven ML algorithms → Random Forest achieved lowest RMSE for financial vulnerability.
  - Figure 3: SHAP feature importance for financial literacy → CRT and Financial Planning are the most influential predictors.
  - Figure 4: SHAP feature importance for financial vulnerability → Financial Planning is the dominant predictor.
  - Figure 5: SHAP feature importance for financial fraud → Financial Planning and Financial Literacy are key predictors.
  - Table A3: Model fit indices and latent factor correlations → CFA model shows excellent global fit and discriminant validity.
  - Table A4: Standardized factor loadings → All factor loadings are statistically significant at p < 0.001.
key_equations:
  - equation: FL_i = β_0^FL + β_1^FL CRT_i + β_2^FL Female_i + ... + ε_{i,FL}
    explanation: Regression model for financial literacy with CRT and demographic controls.
  - equation: FV_i = β_0^FV + β_1^FV FL_i + β_2^FV FP_i + ... + ε_{i,FV}
    explanation: Regression model for financial vulnerability including FL and FP.
  - equation: FF_i = β_0^FF + β_1^FF FL_i + β_2^FF FP_i + ... + ε_{i,FF}
    explanation: Regression model for financial fraud including FL and FP.
definitions:
  - term: PFMS
    definition: Personal Financial Management System
  - term: CFA
    definition: Confirmatory Factor Analysis
  - term: FL
    definition: Financial Literacy
  - term: FP
    definition: Financial Planning
  - term: FV
    definition: Financial Vulnerability
  - term: FF
    definition: Financial Fraud
  - term: CRT
    definition: Cognitive Reflection Test
  - term: SHAP
    definition: Shapley Additive Explanations
  - term: LIME
    definition: Local Interpretable Model-Agnostic Explanation
  - term: XAI
    definition: Explainable Artificial Intelligence
  - term: OLS
    definition: Ordinary Least Squares
  - term: IRT
    definition: Item Response Theory
  - term: AVE
    definition: Average Variance Extracted
  - term: CR
    definition: Composite Reliability
  - term: RMSE
    definition: Root Mean Square Error
critical_citations:
  - "[Lusardi & Mitchell, 2011] — Foundational work on financial literacy measurement and retirement planning."
  - "[Kahneman & Tversky, 1979] — Prospect theory foundation for understanding cognitive biases in financial decisions."
  - "[Anderloni et al., 2012] — Provided the financial vulnerability index framework used in this study."
  - "[Frederick, 2005] — Cognitive Reflection Test methodology for measuring analytical versus intuitive thinking."
  - "[Breiman, 2001] — Random Forest algorithm foundation for machine learning analysis."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly compares knowledge-based vs. behavior-based dimensions (planning) for predicting financial outcomes.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: medium
      justification: Demonstrates that behavioral dimensions (planning) are more predictive than knowledge metrics for new users.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Uses Random Forest classification to identify key behavioral and demographic predictors of financial profiles.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Establishes financial planning as a critical behavior that reduces vulnerability, directly informing budget strategies.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Provides evidence that planning behaviors should be prioritized in budget recommendation algorithms.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: contextual
      justification: Contextual relevance for understanding how to handle cases where users lack planning behaviors.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly compares multiple ML algorithms (Random Forest, SVM, XGBoost) for predicting financial outcomes.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: contextual
      justification: Provides methodological foundation for forecasting but not focused on sequential spending data.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Links financial planning to fraud prevention, relevant to anomaly detection for fraud identification.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: Uses machine learning for fraud prediction, though not specifically for spending anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides rigorous validation methodology (CFA, horse race) applicable to evaluating PFMS modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Compares multiple algorithms using RMSE and XAI methods (SHAP, LIME) for model evaluation.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Shows planning reduces vulnerability, which enables better savings behavior.
    - code: 13.C
      name: End-of-Period Surplus as a Savings Input
      relevance: low
      justification: Tangentially related through the finding that planners are less vulnerable and more likely to save.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Contextual relevance for understanding gaps in current PFMS approaches.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies the gap of not integrating behavioral/planning dimensions in financial literacy assessments.
  contribution: This paper provides empirical validation that financial planning behaviors are more critical than knowledge for reducing financial vulnerability and fraud. This finding directly informs Odin's behavioral profiling module (5.A) by indicating that observed planning behaviors should be prioritized over self-reported knowledge. The machine learning methodology, including the horse race comparison and SHAP/LIME interpretation, offers a template for Odin's algorithm selection and evaluation framework (12.A, 12.B). The strong predictive power of planning variables justifies their integration as key features in Odin's forecasting and recommendation modules (6.A, 7.A). The identification of demographic inequalities (gender, race, income) in financial outcomes provides critical context for Odin's cold-start and personalization strategies (5.B).
  directly_justifies:
    - Behavioral profiling should prioritize observed planning behaviors over declared financial knowledge.
    - Random Forest with SHAP/LIME is effective for identifying key predictors in personal finance datasets.
    - Financial planning is a stronger predictor of positive financial outcomes than literacy alone.
    - Demographic factors like gender, race, and income must be considered in financial profiling systems.
    - Cognitive reflection capacity correlates with financial literacy and should be considered in user modeling.
  limits:
    - Sample limited to urban Federal District of Brazil, not generalizable to other regions or rural populations.
    - Convenience sampling may introduce selection bias despite attempts at demographic diversity.
    - Cross-sectional design prevents causal inference despite strong correlational evidence. [unacknowledged]
    - Small sample size for nonbinary and other race groups limited statistical power for these categories.
    - Financial literacy factor showed borderline reliability (CR=0.695), suggesting measurement refinement needed. [unacknowledged]
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was conducted. The Behavioral Profiling domain (5.A, 5.B, 5.C) was flagged as highly relevant because the paper directly compares knowledge-based and behavior-based dimensions, showing planning behavior is the dominant predictor. The Budget Recommendation domain (7.A, 7.B, 7.D) was flagged for its evidence that planning behaviors should inform budget strategies and its relevance to constraint handling. The Predictive Modeling domain (6.A) was flagged high for its rigorous algorithm comparison and XAI application. The Anomaly Detection domain (8.A, 8.B) was flagged medium/contextual for its fraud prediction component. The System Evaluation domain (12.A, 12.B) was flagged for providing a template for algorithmic evaluation. The Savings domain (13.A, 13.C) was flagged medium/low through the link between planning and vulnerability reduction. The Existing Systems domain (4.A, 4.B) was flagged contextual for identifying gaps in current approaches. Domains considered but rejected included: Filipino Cultural Context (2.A-D) as the study is Brazilian and culture-specific practices are not examined; Expense Categorization (3.A-C) as no expense categorization framework is discussed; Mobile-First Design (9.A-B) as no mobile design considerations are present; Data Privacy (10.A-B) as privacy is not discussed; User Retention (11.A-B) as retention mechanisms are not examined; and Evaluation Methodologies for Budget Recommendation (12.C) as the evaluation is algorithm-focused rather than recommendation-specific. Overall relevance is high for Odin's behavioral profiling, forecasting, and evaluation modules, providing empirical justification for prioritizing behavioral dimensions over knowledge metrics in PFMS design.
limitations:
  - Sample limited to urban Federal District of Brazil, not generalizable to other regions or rural populations.
  - Convenience sampling may introduce selection bias despite attempts at demographic diversity.
  - Cross-sectional design prevents causal inference despite strong correlational evidence. [unacknowledged]
  - Small sample size for nonbinary and other race groups limited statistical power for these categories.
  - Financial literacy factor showed borderline reliability (CR=0.695), suggesting measurement refinement needed. [unacknowledged]
remember_this:
  - Financial planning is more predictive of reduced vulnerability than financial literacy.
  - Random Forest with SHAP/LIME identified planning as the dominant predictor of financial outcomes.
  - Financial planning has a −0.642 correlation with vulnerability, stronger than literacy's −0.380.
  - Women and Black respondents showed higher financial vulnerability, indicating systemic inequalities.
  - Cognitive reflection capacity strongly correlates with financial literacy (coef. 0.502).
```
---

## Paper 18: Kaarov &  Esenalieva_summarized.md

**Source File:** `Kaarov &  Esenalieva_summarized.md`

```yaml
paper_id: 10.20944/preprints202504.2615.v1
designation: international-algorithm-specific
title: Development of a Platform for Financial Dataanalysis and Adaptive Personal Finance Management
authors: Kaarov, A.; Esenalieva, G.
year: 2025
venue: Preprints.org
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 11.B
  - 12.B
  - 13.A
  - 13.B
tldr: Development of TYIYN, a multilingual mobile app using AI and visualization for adaptive personal finance management.
problem_and_motivation: Many individuals, especially in developing economies, lack smart tools for monitoring expenses and receiving context-appropriate financial advice. Traditional budgeting methods are inadequate for modern needs, leading to poor financial decisions. The paper aims to bridge this gap with an AI-driven mobile platform.
approach:
  - Built TYIYN with Flutter for cross-platform mobile development and Django REST Framework for the backend API.
  - Used PostgreSQL for relational data storage and Pandas/Matplotlib for data analysis and visualization.
  - Integrated machine learning models to categorize transactions and generate personalized budget recommendations.
  - Validated expense categorization models on simulated data from 100 test users over three months.
  - Evaluated AI recommendation impact by comparing savings rates of users who followed advice versus those who did not.
findings:
  - num: Expense categorization showed rent at 35%, food at 25%, transport at 15%, entertainment at 10%, and miscellaneous at 15%.
  - num: Over 60% of users allocated disproportionate income to discretionary spending, while fewer than 40% committed to savings.
  - num: Users following AI recommendations increased average monthly savings by 12-18%.
  - num: 45% of users reported reduced discretionary spending after using targeted reminders and visual recaps.
  - num: The recommendation engine achieved an estimated precision of roughly 85% in predicting potential overspending.
  - num: API returns averaged 200 milliseconds, providing a responsive user interface.
  - num: 87% of non-English speaking users appreciated the Russian and Kyrgyz interfaces, improving usability.
key_figures_tables:
  - Figure/Table: Expense distribution data → Shows rent and food are primary expenses, accounting for 60% of total spending.
  - Figure/Table: Savings improvement metrics → AI recommendations boost average savings by 12-18%.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: FinTech
    definition: Financial Technology.
  - term: AI
    definition: Artificial Intelligence.
  - term: DRF
    definition: Django REST Framework.
  - term: UI
    definition: User Interface.
  - term: UX
    definition: User Experience.
critical_citations:
  - "[Zhang & Liu, 2020] — Demonstrated ML can forecast consumer expenditure behavior."
  - "[Nguyen et al., 2021] — AI assistant improved budget adherence by 10-15%."
  - "[Chen et al., 2022] — Interactive dashboards improved comprehension by 40%."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Implements AI models to classify spending into categories like food and transport.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: Discusses heuristic grouping methods for expense categorization.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides background on FinTech evolution and the need for modern tools.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies gaps like lack of AI integration and manual data entry in existing tools.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Uses ML models to forecast spending behavior and optimize budgets.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: The system predicts future spending to adjust budgeting recommendations.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: The AI provides personalized budget advice based on spending patterns.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: Core contribution is generating adaptive budget recommendations via AI.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: high
      justification: The app is built with Flutter for a cross-platform mobile-first experience.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: User-centered iterative methodology was used to improve UI/UX.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Implements MFA, encryption, and token-based authorization for data security.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Security features are argued to boost user confidence and platform usage.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: contextual
      justification: Mentions that visual interfaces and multilingual support improve engagement.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Evaluates the precision of the AI recommendation engine at 85%.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: The system aims to improve savings rates through AI-driven advice.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: contextual
      justification: Savings improvement indirectly supports debt management.
  contribution: The paper contributes a complete system architecture (TYIYN) that integrates AI-driven budgeting with multilingual support for underserved markets, informing Odin's backend design and feature set. It validates that ML-based expense categorization and personalized recommendations can yield measurable savings improvements (12-18%). The security and UX considerations in TYIYN provide a benchmark for Odin's trust and engagement strategies. The use of Flutter and Django REST Framework offers a tech stack reference for Odin's cross-platform development.
  directly_justifies:
    - "AI-driven personalized financial guidance improves budgeting behavior and savings rates."
    - "Interactive data visualizations enhance user comprehension and engagement with financial data."
    - "Multilingual support significantly increases accessibility and adoption among non-English speakers."
    - "Strong security features like MFA and encryption are necessary to boost user trust and usage."
  limits:
    - "The paper is a preprint and not peer-reviewed."
    - "Recommendation engine performance relied on simulated data and may not fully reflect real-world complexity. [unacknowledged]"
    - "Lack of direct banking integration is a friction point for user adoption. [acknowledged]"
  mapping_rationale: A systematic scan of all 12 functional domains was performed. Domains flagged as relevant include: Expense Categorization (3.A, 3.B), Existing Systems & Gaps (4.A, 4.B), Spending Forecasting (6.A, 6.B), Budget Recommendation (7.A, 7.B), Mobile-First Design (9.A, 9.B), Data Privacy & User Trust (10.A, 10.B), User Retention & Engagement (11.B), System Evaluation (12.B), and Savings & Debt Management (13.A, 13.B). Topic 3.A and 6.B were assigned 'high' relevance as the paper directly implements and tests these algorithms. Topic 4.B and 7.B were assigned 'medium' for highlighting limitations and providing recommendation strategies. A borderline case was the paper touching on both 9.A (mobile-first design) and 9.B (UX), both flagged as relevant. Domains like Behavioral Profiling (5.A-C) and Infeasibility Handling (7.D) were considered but rejected as they are not central to the paper's contribution. Overall, the paper is highly relevant to Odin for its practical implementation and validation of core personal finance management features.
limitations:
  - "The paper is a preprint and not peer-reviewed."
  - "AI model validation was performed on simulated data, not real-world user data. [unacknowledged]"
  - "The recommendation engine's starting performance required real-world interaction data to mature. [acknowledged]"
remember_this:
  - "AI-driven budgeting recommendations improved average savings by 12-18%."
  - "Expense categorization showed rent and food as the top spending categories."
  - "87% of non-English users preferred the multilingual interface."
  - "Multilingual support and security features are critical for user trust."
  - "Manual data entry remains a significant adoption barrier for financial apps."
```
---

## Paper 19: Thakur & Jadhav_summarized.md

**Source File:** `Thakur & Jadhav_summarized.md`

```yaml
paper_id: 10.14744/sigma.2025.00119
designation: international-algorithm-specific
title: Expense tracker management system using machine learning
authors: Thakur, R. S.; Jadhav, A.
year: 2025
venue: Sigma Journal of Engineering and Natural Sciences
odin_topics:
  - 3.A
  - 3.B
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 7.C
  - 8.A
  - 8.B
  - 9.A
  - 9.B
  - 12.A
  - 12.B
  - 12.C
tldr: An expense tracker system using machine learning and ensemble methods to predict future expenses based on historical transaction data.
problem_and_motivation: Manual expense tracking is time-consuming and error-prone, and existing digital tools often lack predictive analytics for proactive financial management. A system that automates expense tracking and forecasts spending can help users make better financial decisions.
approach:
  - Used the "Daily Household Transactions" dataset from Kaggle with fields like date, category, amount, and income/expense flags.
  - Preprocessed data using MinMax scaling, log1p transformation for the amount, and TF-IDF vectorization for text fields.
  - Evaluated individual models: XGBoost, Random Forest, SVM, MLP, KNN, Decision Tree, Extra Tree, and CatBoost.
  - Evaluated ensemble models: Bagging, Boosting, Stacking, Voting, and Blending.
  - Evaluated performance using R-squared, Mean Absolute Error, Mean Square Error, and Relative Absolute Error.
findings:
  - XGBoost achieved the highest R-squared (77.89%) among individual models.
  - The Voting Ensemble Regressor outperformed all other models with an R-squared of 78.11%.
  - num: The Voting Ensemble Regressor achieved the lowest Relative Absolute Error of 0.1765.
  - num: The Voting Ensemble Regressor achieved the lowest Mean Absolute Error of 0.6121.
  - The system's web application is built with Django and PostgreSQL, featuring interactive dashboards and expense categorization.
key_figures_tables:
  - Table 1: Summary of prior expense tracking systems → Highlights gaps like manual entry and limited analysis.
  - Table 2: Performance comparison of machine learning models → Shows Voting Ensemble as the best performer.
  - Figure 3: Expense summary dashboard → Displays total expenses, category breakdown, and monthly trends.
  - Figure 7: Expense categorization interface → Shows predefined categories like food, rent, and shopping.
key_equations:
  - equation: R^2 = 1 - (SS_res / SS_tot)
    explanation: Measures variance explained by the model.
  - equation: MAE = (1/n) * Σ|y_i - ŷ_i|
    explanation: Average magnitude of prediction errors.
  - equation: MSE = (1/n) * Σ(y_i - ŷ_i)^2
    explanation: Average squared difference between actual and predicted.
definitions:
  - term: XGBoost
    definition: Extreme Gradient Boosting, an efficient sequential decision tree ensemble.
  - term: Ensemble Learning
    definition: Combining multiple models to improve overall predictive performance.
  - term: TF-IDF
    definition: Term Frequency-Inverse Document Frequency, a text vectorization technique.
critical_citations:
  - "[Doan & Kalita, 2015] — Provides context on selecting ML algorithms."
  - "[Mienye & Sun, 2022] — Surveys ensemble learning concepts and applications."
  - "[Jadhav et al., 2023] — Discusses data transformation as a preprocessing stage."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Directly proposes and implements an expense categorization system.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: Discusses predefined categories like food, transport, and custom categories.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Core contribution is using ML for expense prediction.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Evaluates multiple forecasting algorithms on spending data.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Mentions budget forecasting and overspending alerts.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Touches on budget forecasting but not on optimization.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: contextual
      justification: Not a focus; the paper is on prediction, not allocation.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Mentions deviation alerts but does not implement anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: Not a focus; system only flags deviations.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: Mentions cross-device access but does not focus on mobile-first design.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: Web application focus, not mobile UX.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses standard regression metrics (R2, MAE, MSE, RAE).
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Systematic evaluation of individual and ensemble models.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: low
      justification: More about prediction accuracy than budget recommendation evaluation.
  contribution: This paper demonstrates that ensemble methods, particularly voting regressors, outperform individual models for expense prediction, providing a basis for Odin's forecasting module. Its application of data transformation techniques (e.g., log1p) and text vectorization can inform data preprocessing for Odin's categorization and prediction algorithms. The web application architecture built with Django offers a reference for Odin's backend design, especially in handling user authentication and expense entry. The evaluation framework using R-squared and MAE provides a template for assessing Odin's predictive performance.
  directly_justifies:
    - Voting ensemble regressors improve expense prediction accuracy over single models.
    - Data transformations like log1p and TF-IDF are effective preprocessing steps for spending data.
    - R-squared and Mean Absolute Error are appropriate metrics for evaluating spending forecast models.
  limits:
    - Dataset is from India, which may not generalize to Filipino cultural or spending contexts. [unacknowledged]
    - Does not address the cold-start problem or behavioral profiling for new users. [unacknowledged]
    - No comparison with deep learning methods like LSTMs for sequential data. [unacknowledged]
    - The system relies on manual expense entry, not automated bank transaction syncing.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. High relevance was assigned to domains directly addressed by the paper's core contribution of ML-based expense prediction and categorization (6.A, 6.B, 3.A, 12.B). Medium relevance was assigned to broader budgeting and evaluation topics (7.A, 12.A). Low relevance was assigned to anomaly detection and mobile design, as these are only superficially mentioned. The topic of constrained optimization (7.C) was considered but rejected as the paper does not address allocation algorithms. The topic of Filipino cultural context (2.A, 2.B) was considered and rejected as the paper uses a non-Philippine dataset. Overall, the paper provides strong empirical justification for using ensemble regression for spending forecasting, which directly supports Odin's algorithmic design.
limitations:
  - The dataset is from India, which may not generalize to Filipino cultural or spending contexts. [unacknowledged]
  - Does not address the cold-start problem or behavioral profiling for new users. [unacknowledged]
  - No comparison with deep learning methods like LSTMs for sequential data. [unacknowledged]
  - The system relies on manual expense entry, not automated bank transaction syncing. [unacknowledged]
remember_this:
  - Voting ensemble regressor achieved the highest R-squared of 78.11%.
  - The voting ensemble achieved the lowest relative absolute error of 0.1765.
  - XGBoost outperformed other individual models with an R-squared of 77.89%.
  - Data preprocessing with log1p and TF-IDF is crucial for expense prediction.
  - The system uses Django for backend and PostgreSQL for database management.
```
---

## Paper 20: Ghonaim & El-Sharawy_summarized.md

**Source File:** `Ghonaim & El-Sharawy_summarized.md`

```yaml
paper_id: 10.21608/IJTAR.2025.427658.1148
designation: international-algorithm-specific
title: An Intelligent Budget Management Mobile Application Based on a Recurrent Neural Network
authors: Ghonaim, W. A.; El-Sharawy, E. E.
year: 2025
venue: International Journal of Theoretical and Applied Research
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 9.A
  - 9.B
tldr: Develops a bilingual mobile budget app using an RNN to classify financial transaction risk, achieving 97.45% accuracy across low, medium, and high risk categories.
problem_and_motivation: Existing budgeting apps often lack Arabic language support and AI-based forecasting features. This paper addresses the gap by developing a mobile application that combines RNN-based risk prediction with a user-friendly interface for Arabic and English speakers.
approach:
  - Dataset of 1,048,576 financial transactions from Kaggle was used, split 70/15/15 for training, validation, and testing.
  - A bidirectional LSTM with two hidden layers (128 units each) and ReLU activation was implemented.
  - Risk labels (low/medium/high) were constructed using a scoring method based on income, debt, transaction frequency, and budget adherence.
  - The model was deployed via a Flask API with Firebase Firestore, integrating with a React Native mobile frontend.
  - Evaluation used precision, recall, F1-score, and accuracy, comparing predictions to actual risk levels.
findings:
  - num: 97.45% overall accuracy was achieved on the test set.
  - num: Precision, recall, and F1-score all exceeded 0.97 for each risk category.
  - The model demonstrated high reliability in detecting both low and high-risk financial behaviors.
  - The mobile application successfully integrated AI predictions with real-time user alerts.
  - Functional testing confirmed the stability and usability of the application for key features like registration and transaction entry.
key_figures_tables:
  - Table 2: Classification report showing precision, recall, and F1-score per risk level → All metrics exceed 0.97.
  - Table 3: Confusion matrix illustrating prediction alignment across risk categories → Strong diagonal values with minor overlaps in medium risk.
  - Figure 5: Report and Add Account interfaces → Visualizes the user workflow for managing financial accounts.
  - Figure 6: My Budget and Add Budget interfaces → Shows the interface for setting and managing budget categories.
key_equations:
  - equation: Precision = TP / (TP + FP)
    explanation: Measures the accuracy of positive predictions.
  - equation: Recall = TP / (TP + FN)
    explanation: Measures the ability to find all positive instances.
  - equation: F1 = 2 * (Precision * Recall) / (Precision + Recall)
    explanation: Harmonic mean of precision and recall.
definitions:
  - term: RNN
    definition: Recurrent Neural Network, a class of neural networks for sequential data.
  - term: LSTM
    definition: Long Short-Term Memory, an advanced RNN variant for long-term dependencies.
  - term: GRU
    definition: Gated Recurrent Unit, a simplified LSTM variant.
  - term: Firestore
    definition: Firebase's NoSQL cloud database for real-time data synchronization.
  - term: Flask
    definition: A Python microframework for building web APIs.
critical_citations:
  - "[Hochreiter & Schmidhuber, 1997] — Introduces LSTM architecture."
  - "[Cho et al., 2014] — Introduces GRU architecture."
  - "[Pascanu et al., 2013] — Discusses vanishing gradient problem in RNNs."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: App includes expense tracking and categorization.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: low
      justification: Mentions categories like necessities and discretionary spending.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Extensively reviews and compares existing budgeting applications.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies lack of Arabic support and AI features as key gaps.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses RNN to classify transactions into risk profiles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Core contribution is RNN-based risk prediction.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Applies RNN (LSTM) to sequential financial transaction data.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: App provides budgeting features and strategies.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Offers personalized financial plans and recommendations.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Risk prediction can alert users to potential financial issues.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Model detects high-risk spending patterns as anomalies.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Developed as a mobile-first application using React Native.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Designed over 27 interfaces with a focus on user experience.
  contribution: The paper provides a complete implementation of an RNN-based risk classifier that can be integrated into Odin's Anomaly Detection module to flag high-risk spending. The comparative analysis of existing apps informs Odin's competitive positioning and feature prioritization, particularly the need for AI-driven insights and multilingual support. The study's validation methodology, including precision, recall, and F1, offers a template for evaluating Odin's classification modules. The system's architecture combining Firebase, Flask, and React Native provides a blueprint for Odin's mobile-first, cloud-backed design. Finally, the user-centric features like real-time alerts and budget tracking directly justify similar components in Odin's Mobile UX and Budget Recommendation modules.
  directly_justifies:
    - Bilingual support and AI forecasting are critical gaps in existing PFMS apps.
    - RNNs can effectively classify financial risk from sequential transaction data.
    - 97.45% accuracy validates the reliability of deep learning for spending risk assessment.
    - Real-time budget alerts improve user financial awareness and decision-making.
  limits:
    - The risk labeling process was heuristic and may not generalize to all user contexts.
    - The study lacks longitudinal user studies to assess real-world impact on financial behavior.
    - No comparison with baseline or alternative ML models (e.g., GRU, XGBoost) for risk prediction.
  mapping_rationale: The paper was systematically scanned against all 12 functional domains and their associated topic codes. The "Expense Categorization" domain was flagged as medium relevance (3.A, 3.B) due to the app's transaction categorization. "Existing Systems & Gaps" was high relevance (4.A, 4.B) from the comprehensive literature review and comparative analysis. "Behavioral Profiling" was medium (5.C) via risk profile classification. "Spending Forecasting" was high (6.A, 6.B) due to the core RNN prediction task. "Budget Recommendation" was medium (7.A, 7.B) from the personalized planning features. "Anomaly Detection" was high (8.A, 8.B) through risk detection. "Mobile-First Design" was medium (9.A, 9.B) given the app's development focus. Domains like "Filipino Cultural Context" and "Savings & Debt Management" were considered but rejected as the paper is Egypt-based and does not address specific Filipino practices or advanced savings/debt features. The paper's primary relevance to Odin lies in its practical demonstration of AI-driven risk classification within a mobile PFMS context, offering a validated approach for the Forecasting and Anomaly Detection modules.
limitations:
  - Risk labels were artificially constructed from financial indicators, not verified against real-world financial distress outcomes. [unacknowledged]
  - The model was trained on fraud detection data, which may not fully represent general spending behavior for budget management. [unacknowledged]
  - No long-term user study was conducted to measure the app's actual impact on budgeting behavior or financial health.
remember_this:
  - The RNN model achieved 97.45% accuracy in classifying spending risk levels.
  - Arabic and English language support was a primary design requirement for the app.
  - The system provides real-time risk alerts based on transaction patterns.
  - The application architecture uses Firebase for backend and React Native for frontend.
  - Personal financial plans and recommendations are generated using AI predictions.
```
---

## Paper 21: Levi_summarized.md

**Source File:** `Levi_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international-algorithm-specific
title: Personal Financial Information Presentation and Consumer Spending
authors: Levi, Y.
year: 2025
venue: Unknown
odin_topics:
  - 2.B
  - 5.B
  - 6.B
  - 7.B
  - 8.B
  - 9.B
  - 11.A
  - 12.B
tldr: Consumers exposed to a consumption-oriented frame and a salient comparison of a personalized net-worth index with past spending reduced discretionary spending by 15%.
problem_and_motivation: Individuals interact with finances digitally, but the influence of information presentation on spending behavior is underexplored. A gap exists in understanding if simple design changes can overcome strong spending habits. This study tests if framing and salience of financial information can prompt consumers to adjust spending.
approach:
  - Randomized field experiment with 3,138 users of an online account aggregation app.
  - Personalized index presented net worth as lifetime monthly cash flow from an annuity.
  - Treatments varied index name: Financial Sustainability Index (FSI, consumption frame) vs. Life Annuity Index (LAI, neutral frame).
  - Salience manipulated by providing a context plot comparing the index to historical monthly spending.
  - Difference-in-differences analysis with individual and event-month fixed effects.
findings:
  - num: FSI-Plot group reduced discretionary spending by 15% relative to control during the 8-month experiment.
  - num: Effect persisted for 8 months after treatment removal, with a gradual return to baseline.
  - num: Spending decreased in restaurants (14%), clothing (20%), entertainment (14%), travel (24%), and cash withdrawals (25%).
  - No significant change in non-discretionary spending categories like gas, groceries, and utilities.
  - No effect from the index name or context plot alone; both consumption frame and salient context were necessary.
  - Login frequency increased similarly across all treated groups, controlling for attention effects.
key_figures_tables:
  - Figure 3: Monthly logins by treatment group → All treated groups increased logins similarly.
  - Figure 4: Monthly discretionary spending by treatment group → FSI-Plot groups diverged lower immediately at experiment start.
  - Table 5: Treatment effects on discretionary spending → FSI-Plot groups show 15% decrease during intra period.
  - Table 7: Spending category effects → Reductions largest in restaurants, clothing, entertainment, travel, and cash.
key_equations:
  - equation: y_{i,t} = \sum_{j=2}^{5} \beta_j TG_{j,i} Intra_t + \sum_{j=2}^{5} \gamma_j TG_{j,i} Post_t + \delta_i + \theta_j + \epsilon_{i,t}
    explanation: Main diff-in-diff specification with individual and month fixed effects.
definitions:
  - term: FSI
    definition: Financial Sustainability Index, the consumption-framed name for the personalized index.
  - term: LAI
    definition: Life Annuity Index, the neutral-framed name for the personalized index.
  - term: Personalized Index
    definition: Net worth presented as the equivalent inflation-protected lifetime monthly cash flow.
  - term: Context Plot
    definition: Time series plot directly comparing the index level with the user's historical monthly spending.
critical_citations:
  - "[Benartzi et al., 2011] — Annuitization puzzles and framing effects on annuity valuation."
  - "[Goldstein et al., 2016] — Illusion of wealth from lump-sum vs. cash-flow presentation."
  - "[Karlan et al., 2016] — Salient reminders promote staying within means."
  - "[Sussman and Alter, 2012] — Underestimation of exceptional expenses leads to overspending."
relevance:
  topics:
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: Provides evidence of spending adjustments in response to information, not seasonal drivers.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: Results suggest behavioral response to a reference point, but not directly profile classification.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: Uses historical spending data, but does not develop or test forecasting algorithms.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: Directly tests how presenting a benchmark (the index) influences spending, a core budget recommendation mechanism.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Examines spending changes in categories, but not anomaly detection methods.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Tests information presentation within a digital (app) environment, relevant to UX design choices.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Measures login behavior as a proxy for attention, relevant to engagement.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides a rigorous experimental evaluation framework (RCT, diff-in-diff) applicable to evaluating Odin's modules.
  contribution: This paper provides a rigorous experimental framework for testing information presentation effects, directly applicable to evaluating Odin's budget recommendation module. The finding that a salient benchmark reduces spending offers a design principle for Odin's interface to encourage savings. The persistence of the effect beyond treatment exposure informs retention strategies for Odin. The detailed spending category analysis can guide Odin's expense categorization and anomaly detection design by highlighting responsive categories.
  directly_justifies:
    - A consumption-oriented frame combined with a salient context can reduce discretionary spending by 15%.
    - Information design can influence spending behavior without changing economic variables.
    - Effects persist for months after treatment removal, suggesting habit formation.
    - Non-discretionary spending is less responsive to information interventions.
  limits:
    - Sample consists of relatively wealthy users (top 20% income), limiting generalizability to lower-income Filipino young professionals.
    - Data may be incomplete if users did not link all financial accounts to the app.
    - The experiment was conducted in 2014, before pre-registration became common.
    - The study population is U.S.-based, which may not fully reflect Filipino cultural and financial contexts.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated canonical topic codes was conducted. The paper was flagged as relevant primarily for the "Budget Recommendation" (7.B) and "System Evaluation" (12.B) domains, receiving a 'high' relevance assignment, as the experimental design directly tests a benchmark-based spending adjustment mechanism and provides a rigorous evaluation framework. It also touches on "User Retention & Engagement" (11.A) and "Mobile UX Design" (9.B) with a 'medium' relevance, as the study measures attention effects and manipulates in-app information presentation. Topics related to "Seasonal Spending" (2.B) and "Profile Dynamics" (5.B) were considered but assigned 'low' relevance, as the paper does not directly model seasonality or user profiles. Domains like "Anomaly Detection" (8.B) and "Forecasting" (6.B) were rejected for direct inclusion, as the paper does not propose or evaluate algorithms in these areas. The paper's overall relevance is moderate, providing a foundational experimental paradigm and evidence of behavioral responsiveness to information design, but its U.S.-based, high-income sample limits direct applicability to the Filipino young professional demographic.
limitations:
  - Sample consists of relatively wealthy U.S. users, limiting generalizability to Filipino young professionals. [unacknowledged]
  - Potential incompleteness of transaction data from account aggregation. [unacknowledged]
  - Experiment was conducted in 2014, before pre-registration became common.
  - The study does not explore the exact psychological mechanism (e.g., anchoring vs. reference point updating).
remember_this:
  - Presenting a consumption-framed benchmark with a context plot reduced discretionary spending by 15%.
  - The spending reduction persisted for eight months after the intervention was removed.
  - Largest decreases occurred in restaurants, clothing, entertainment, travel, and cash withdrawals.
  - Information design effects require both a relevant frame and a salient comparison context.
  - Login frequency increased similarly across all treatments, ruling out attention as the primary driver.
```
---

## Paper 22: Zhang & Duan_summarized.md

**Source File:** `Zhang & Duan_summarized.md`

```yaml
paper_id: "10.3389/fams.2025.1628652"
designation: "international-algorithm-specific"
title: "Accounting data anomaly detection and prediction based on self-supervised learning"
authors: "Zhang, Y.; Duan, B."
year: 2025
venue: "Frontiers in Applied Mathematics and Statistics"
odin_topics:
  - "8.A"
  - "8.B"
  - "8.C"
  - "12.A"
  - "12.B"
tldr: "A hierarchical fusion self-supervised learning framework detects accounting anomalies with 0.820 F1, 0.726 early detection rate, and 0.068 false alarm rate using CSMAR data from 2000-2020."
problem_and_motivation: "Traditional anomaly detection methods depend on scarce labeled data and fail to capture complex multidimensional interactions in accounting data. The dynamic evolution of financial fraud techniques renders static rule-based and supervised approaches inadequate for early warning. A self-supervised framework that leverages unlabeled data and domain knowledge is needed to address these gaps."
approach:
  - "Used CSMAR database financial data from Chinese listed companies (2000-2020), with 28,569 valid observations after cleaning."
  - "Proposed Hierarchical Fusion Self-Supervised Learning (HFSL) with three layers: feature representation via temporal contrastive learning, relationship reasoning via dual-channel LSTM autoencoder, and anomaly detection via reconstruction error and rule violation scoring."
  - "Employed industry calibration, seasonal adjustment using X-13 ARIMA-SEATS, and noise suppression as adaptive data preprocessing."
  - "Trained using only normal samples in self-supervised paradigm with reconstruction and contrastive loss combination; optimized via Bayesian hyperparameter search."
  - "Compared against Z-score, One-Class SVM, Isolation Forest, LSTM-AE, and VAE baselines on 5,098 test observations."
findings:
  - "num: 0.836 precision, 0.805 recall, and 0.820 F1-score for anomaly detection."
  - "num: 0.726 early detection rate within first two quarters and 0.068 false alarm rate."
  - "num: 0.883 AUC-ROC and 0.772 AUC-PR demonstrating strong classification capability."
  - "ROE (0.196 SHAP) and ROA (0.179 SHAP) are the most important features for anomaly identification."
  - "Identified five fraud patterns: revenue inflation (38.6%, 87.3% detection), expense concealment (21.7%, 84.5%), asset overvaluation (17.4%, 79.8%), liability understatement (15.2%, 82.1%), and composite manipulation (7.1%, 68.2%)."
  - "Detected three temporal evolution patterns: progressive deterioration (64%), sudden anomalies (22%), and cyclical fluctuations (15%)."
  - "Feature interaction analysis revealed enhancing effects between ROE-ROA (0.087) and Current-Leverage ratios (0.082), improving F1 by 3.5% when incorporated."
  - "Outperformed LSTM-AE by 7% F1, Isolation Forest by 15%, and Z-score by 35% on F1-score."
  - "Cross-industry performance best in Finance (0.872 F1) and weakest in Construction/Real Estate (0.776 F1), with industry calibration improving cross-industry early detection by 14.6%."
key_figures_tables:
  - "Figure 1: HFSL architecture diagram → Shows three-tier cascaded structure from feature learning to anomaly detection."
  - "Figure 4: Performance comparison across six metrics → HFSL achieves highest F1 (0.820) and lowest false alarm rate (0.068)."
  - "Figure 5: Radar chart of anomaly type performance → Best on mutation anomalies (0.892), weakest on temporal patterns (0.791)."
  - "Figure 6: Detection performance across anomaly types → Confirms model's sensitivity hierarchy from sudden to complex anomalies."
  - "Table 3: Industry-specific performance → Finance highest at 0.872, Construction/Real Estate lowest at 0.776 F1."
key_equations:
  - equation: "L_con = -log(exp(sim(z_i,z_j)/τ) / Σ_{k≠i} exp(sim(z_i,z_k)/τ))"
    explanation: "Contrastive loss for temporal feature learning in first layer."
  - equation: "z = α·f_s(X^{w_s}) + (1-α)·f_l(X^{w_l})"
    explanation: "Attention-fused dual-channel LSTM representation."
  - equation: "Score(X) = λ·((E_recon-μ_recon)/σ_recon) + (1-λ)·((E_rule-μ_rule)/σ_rule)"
    explanation: "Final anomaly score combining reconstruction and rule violations."
  - equation: "θ = μ_high + γ·σ_high"
    explanation: "Adaptive threshold from GMM high-variance component."
  - equation: "Score_final(X) = w_p·Score_p(X) + w_s·Score_s(X) + w_r·Score_r(X)"
    explanation: "Multi-scale scoring: point, sequence, and relationship anomalies."
definitions:
  - term: "HFSL"
    definition: "Hierarchical Fusion Self-Supervised Learning framework for anomaly detection."
  - term: "LSTM"
    definition: "Long Short-Term Memory, a recurrent neural network architecture."
  - term: "SHAP"
    definition: "SHapley Additive exPlanations, for feature importance attribution."
  - term: "GMM"
    definition: "Gaussian Mixture Model for adaptive threshold determination."
  - term: "CSMAR"
    definition: "China Stock Market and Accounting Research database."
  - term: "ROE"
    definition: "Return on Equity, a profitability indicator."
  - term: "ROA"
    definition: "Return on Assets, a profitability indicator."
  - term: "EDR"
    definition: "Early Detection Rate, proportion detected within first two quarters."
  - term: "FAR"
    definition: "False Alarm Rate, proportion of normal samples incorrectly classified."
  - term: "X-13 ARIMA-SEATS"
    definition: "Seasonal adjustment method for time series decomposition."
  - term: "MAD"
    definition: "Median Absolute Deviation, a robust scale estimator."
  - term: "MCD"
    definition: "Minimum Covariance Determinant, a robust covariance estimator."
critical_citations:
  - "[Ellili et al., 2024] — SEC fraud cases increased 30% 2020-2023."
  - "[Altman, 1968] — Foundational Z-score bankruptcy prediction method."
  - "[Beneish, 1999] — M-score detection of earnings manipulation."
  - "[Dechow et al., 2011] — Predicting material accounting misstatements."
  - "[Perols, 2011] — Statistical vs ML for financial fraud detection."
  - "[Bao et al., 2020] — Machine learning approach for US fraud detection."
relevance:
  topics:
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Core contribution: novel self-supervised framework specifically for anomaly detection."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Provides LSTM-based deep learning algorithm for time-series anomaly detection."
    - code: "8.C"
      name: "Cold-Start Baseline Strategies for Anomaly Detection"
      relevance: "high"
      justification: "Self-supervised learning directly addresses labeled data scarcity in cold-start scenarios."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Comprehensive multi-metric evaluation including precision, recall, F1, AUC, EDR, FAR."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Comparative evaluation against multiple baseline algorithms including LSTM-AE and VAE."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "low"
      justification: "Evaluation focuses on anomaly detection, not budget recommendation specifically."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "contextual"
      justification: "Uses anonymized CSMAR data but does not discuss privacy mechanisms."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "low"
      justification: "No user interaction or engagement analysis; purely technical detection."
    - code: "11.B"
      name: "Retention Mechanisms and Engagement Design"
      relevance: "low"
      justification: "No user retention or engagement design components."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "low"
      justification: "Does not address savings goals or management."
    - code: "13.B"
      name: "Debt Management in PFMS"
      relevance: "low"
      justification: "Does not address debt management."
    - code: "13.C"
      name: "End-of-Period Surplus as a Savings Input"
      relevance: "low"
      justification: "No savings or surplus concepts addressed."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "contextual"
      justification: "Uses Chinese data but does not analyze cultural financial practices."
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "contextual"
      justification: "Seasonal adjustment applied as preprocessing, not a primary finding."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "low"
      justification: "Not about expense categorization."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      relevance: "low"
      justification: "Not about category design."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "low"
      justification: "Not a survey of existing PFMS, focuses on detection technique."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "low"
      justification: "Critiques existing detection methods but not PFMS systems."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "low"
      justification: "No user behavioral profiling."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "contextual"
      justification: "Self-supervised learning can address cold-start but not profiling-focused."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "low"
      justification: "Not about behavioral classification."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "contextual"
      justification: "Uses prediction as a self-supervised auxiliary task, not primary focus."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "contextual"
      justification: "Uses LSTM for sequential data but forecasting is auxiliary."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "low"
      justification: "Not about budgeting strategies."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "low"
      justification: "No budget recommendation."
    - code: "7.C"
      name: "Constrained Optimization Approaches for Budget Allocation"
      relevance: "low"
      justification: "No allocation optimization."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "low"
      justification: "No mobile design or UX."
    - code: "9.B"
      name: "Mobile UX Design for Personal Finance"
      relevance: "low"
      justification: "No mobile UX."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "low"
      justification: "Does not address trust."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "low"
      justification: "Evaluation is for anomaly detection, not budget recommendation."
  contribution: "The HFSL framework provides a ready-to-adapt anomaly detection module for Odin's system evaluation layer, directly addressing the cold-start challenge through self-supervised learning without requiring labeled fraud data. Its multi-scale scoring mechanism (point, sequence, relationship) can enhance Odin's spending anomaly detection capabilities. The feature importance analysis (ROE/ROA as top indicators) informs which financial ratios to monitor in Filipino user data. The temporal evolution patterns (progressive, sudden, cyclical) offer guidance for designing Odin's alert escalation and early warning systems. The cross-industry calibration approach suggests that Odin should account for sector-specific spending patterns."
  directly_justifies:
    - "Self-supervised learning can detect anomalies with 0.820 F1 without requiring labeled fraudulent data."
    - "Multi-scale anomaly scoring (point, sequence, relationship) improves detection of complex financial manipulations."
    - "Feature interaction analysis shows that combining related indicators increases anomaly detection accuracy."
    - "Early detection rate of 0.726 enables proactive risk warning within two quarters of anomaly onset."
    - "Dual-channel LSTM architecture effectively captures both short-term and long-term temporal patterns."
  limits:
    - "Evaluation uses Chinese listed company data; applicability to individual Filipino spending data unvalidated [unacknowledged]."
    - "Self-supervised approach requires sufficient unlabeled normal data for training; cold-start with no data remains challenging [unacknowledged]."
    - "Model assumes quarterly reporting cycles; daily personal spending may have different temporal characteristics [unacknowledged]."
    - "Regulatory environment and fraud patterns differ substantially from personal finance misuse contexts [unacknowledged]."
  mapping_rationale: "Systematic scan of all 12 functional domains and 34 topic codes identified strong relevance primarily to Anomaly Detection (8.A, 8.B, 8.C) and Evaluation (12.A, 12.B). The paper directly addresses labeled data scarcity (8.C) through self-supervised learning, proposes a novel detection algorithm (8.B), and provides comprehensive multi-metric evaluation (12.A, 12.B). The Filipino Cultural Context domains (2.A, 2.B, 2.C, 2.D) were considered but rejected as the paper uses Chinese listed company data and does not analyze cultural financial practices or spending cycles—seasonal adjustment is purely preprocessing. Expense Categorization (3.A, 3.B, 3.C) was rejected as the paper categorizes financial ratios, not personal expenses. Forecasting (6.A, 6.B) was marked contextual since prediction appears as an auxiliary self-supervised task, not the primary contribution. Budget Recommendation (7.A-7.D) was rejected entirely as no budgeting or allocation is addressed. Behavioral Profiling (5.A-5.C) was rejected as no user profiling occurs. Mobile-First (9.A, 9.B) and Data Privacy (10.A, 10.B) were rejected as irrelevant. The paper is highly relevant as an algorithmic foundation for Odin's anomaly detection module but requires domain adaptation from corporate accounting to personal finance."
limitations:
  - "Tested only on Chinese listed company financial data; applicability to personal finance spending patterns remains unverified [unacknowledged]."
  - "Self-supervised approach requires sufficient unlabeled data for training; purely cold-start scenarios without transaction history are not addressed [unacknowledged]."
  - "Model complexity (1.8M parameters) and 18-hour training time may be impractical for lightweight PFMS deployment [unacknowledged]."
  - "Assumes quarterly reporting cycles; does not handle irregular or daily transaction data common in personal finance [unacknowledged]."
  - "Concept drift detection is reactive rather than preventive; adaptation lag during sudden regime changes could miss early fraud signals."
remember_this:
  - "HFSL achieves 0.820 F1 for anomaly detection using self-supervised learning without labeled data."
  - "Early detection rate of 0.726 enables proactive risk warnings within two quarters."
  - "ROE and ROA are the most important features for identifying financial anomalies."
  - "Five fraud patterns identified, with revenue inflation as the most common at 38.6%."
  - "Feature interaction analysis improves detection by 3.5% F1 when incorporated."
```
---

## Paper 23: Yachamaneni et al_summarized.md

**Source File:** `Yachamaneni et al_summarized.md`

```yaml
paper_id: 10.63282/3050-9262.IJAIDSML-V6I1P118
designation: international-algorithm-specific
title: Credit Card Customer Profiling Using Self-Supervised Representation Learning on Multi-Source Financial Data
authors: Yachamaneni, T.; Kotadiya, U.; Arora, A. S.
year: 2025
venue: International Journal of Artificial Intelligence, Data Science, and Machine Learning
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
tldr: Self-supervised learning on multi-source financial data creates robust customer representations that outperform supervised models in profiling, credit risk, and churn prediction.
problem_and_motivation: Traditional supervised customer profiling requires costly labeled data and fails to capture complex patterns from heterogeneous financial sources. The emergence of self-supervised learning enables label-efficient representation learning from unlabeled data, addressing privacy and scalability concerns.
approach:
  - Integrates transaction logs, demographics, credit bureau reports, and web activity from 100,000 records into a single model.
  - Uses separate encoders per modality, including temporal encoders for sequences and feedforward layers for static features.
  - Employs a transformer encoder with self-attention to capture temporal dependencies in sequential data.
  - Trains on pretext tasks: masked attribute forecasting, temporal order prediction, and augmented view prediction.
  - Applies contrastive learning to maximize similarity between augmented views and minimize similarity between different instances.
findings:
  - "num: The proposed SSL model achieved a Silhouette Score of 0.56, compared to 0.35 for K-Means and 0.41 for XGBoost."
  - "num: The model attained an AUC of 0.91 for credit risk prediction, versus 0.71 for K-Means and 0.84 for XGBoost."
  - "num: For churn prediction, the SSL model achieved an F1-score of 0.81, outperforming K-Means (0.58) and XGBoost (0.69)."
  - "num: Removing temporal encoding caused the largest performance drop of 4.2% in AUC, underscoring its importance."
  - "num: Web activity features contributed a 3.8% AUC drop when removed, while pretext tasks contributed a 2.7% drop."
key_figures_tables:
  - "Figure 1: Credit Card Fraud Detection System → conceptual framework for fraud scoring."
  - "Figure 2: Emergence of Self-Supervised Learning → SSL principles and benefits for financial data."
  - "Figure 3: Challenges in Traditional Approaches → data labeling, isolated sources, limited generalization."
  - "Figure 4: System Architecture → end-to-end pipeline from preprocessing to downstream tasks."
  - "Figure 5: Data Sources → transaction logs, demographics, credit reports, web activity."
  - "Figure 6: Feature Engineering → temporal encoding, normalization, categorical embeddings."
  - "Figure 7: Self-Supervised Learning Design → contrastive objective and pretext tasks."
  - "Figure 8: Model Architecture → transformer encoder, MLP head, clustering layer."
  - "Table 1: Quantitative Results → performance comparison across all methods and metrics."
  - "Table 2: Ablation Study Results → AUC drop from removing each module."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: SSL
    definition: Self-Supervised Learning - a paradigm that learns representations from unlabeled data using pretext tasks.
  - term: AUC
    definition: Area Under the Receiver Operating Characteristic Curve - a threshold-free measure of classification performance.
  - term: PFMS
    definition: Personal Finance Management System - a software application for managing personal finances.
  - term: K-Means
    definition: A clustering algorithm that partitions data into K distinct, non-overlapping subgroups.
  - term: XGBoost
    definition: Extreme Gradient Boosting - an optimized distributed gradient boosting library for supervised learning.
critical_citations:
  - "[Chen et al., 2020] — foundation for contrastive learning (SimCLR)."
  - "[Devlin et al., 2019] — BERT-style masked prediction pretext task inspiration."
  - "[MacQueen, 1967] — original K-Means algorithm used as baseline."
  - "[Chen & Guestrin, 2016] — XGBoost baseline implementation."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly proposes customer profiling using SSL to identify behavioral patterns from financial data.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: high
      justification: SSL addresses cold-start by learning representations from unlabeled data without requiring initial labels.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Compares SSL against supervised baselines (XGBoost) for classification of customer profiles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Demonstrates predictive modeling for credit risk and churn, relevant to Odin's forecasting needs.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: Uses temporal encoding and transformer architectures suitable for sequential spending data.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: The SSL framework can be adapted for anomaly detection through learned representations.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Provides a basis for anomaly detection via contrastive learning and reconstruction-based pretext tasks.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses standard evaluation metrics (Silhouette, AUC, F1) applicable to Odin's evaluation needs.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Conducts ablation studies to evaluate the contribution of each module, relevant to Odin's modular evaluation.
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: General customer profiling framework not specific to Filipino young professionals.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Reviews traditional and supervised approaches but does not survey PFMS specifically.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: contextual
      justification: Identifies general limitations of supervised learning but not specific to PFMS gaps.
  contribution: "The self-supervised learning framework provides a label-efficient approach for customer profiling that can be adapted for Odin's behavioral profiling module (5.A, 5.C). The multi-modal integration strategy informs Odin's data aggregation design across heterogeneous financial sources. The ablation study's emphasis on temporal encoding directly supports Odin's forecasting module (6.B) by showing the critical role of sequential patterns. The evaluation metrics (Silhouette, AUC, F1) provide a template for Odin's system evaluation framework (12.B). The demonstrated outperformance of SSL over supervised methods justifies Odin's adoption of self-supervised techniques for cold-start scenarios (5.B)."
  directly_justifies:
    - "Self-supervised learning can generate robust customer profiles from unlabeled financial data without manual annotation."
    - "Integrating temporal encoding significantly improves predictive performance for financial behavior modeling."
    - "Web activity logs provide valuable behavioral signals that enhance profiling accuracy beyond transactional data."
    - "Contrastive learning objectives yield more coherent and separable customer clusters than traditional clustering."
    - "The transformer architecture effectively captures long-range dependencies in sequential spending data."
  limits:
    - "Paper uses a proprietary dataset from a private banking company, limiting reproducibility."
    - "The study focuses on credit card customers, not general PFMS users, limiting direct applicability."
    - "Interpretability of SSL representations remains a challenge for regulated financial applications."
    - "No explicit handling of infeasibility or budget constraints, which are core to Odin's recommendation module."
    - "Evaluation does not include user satisfaction or engagement metrics, only algorithmic performance."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant for Behavioral Profiling & Classification (5.A, 5.B, 5.C) because it directly proposes a novel SSL-based customer profiling framework with empirical validation. It shows medium relevance for Spending Forecasting (6.A, 6.B) due to its temporal modeling components, and for Anomaly Detection (8.A, 8.B) through its representation learning approach suitable for outlier detection. System Evaluation (12.A, 12.B) was rated medium because it provides a comprehensive evaluation setup with ablation studies and standard metrics. Borderline cases included 2.B (Seasonal Patterns) and 2.D (Spending Cycles), which the paper does not explicitly address; these were rejected as purely contextual. The domains of Filipino Cultural Context, Expense Categorization, Budget Recommendation, Mobile-First Design, Data Privacy, User Retention, and Savings/Debt Management were considered and rejected as they are not addressed by the paper. Overall, the paper is highly relevant to Odin's core algorithmic modules for profiling and forecasting."
limitations:
  - "The dataset is from a single private bank, which may not generalize to the Philippine financial context."
  - "Interpretability of SSL-generated representations is not addressed, a key requirement for regulated PFMS."
  - "Does not address real-time deployment considerations or latency requirements for mobile-first applications."
  - "The paper does not discuss infeasibility handling or constrained optimization, central to Odin's budget recommendation."
  - "Privacy-preserving aspects of the SSL framework are not explored, despite multi-source data integration. [unacknowledged]"
remember_this:
  - "SSL achieved 0.91 AUC for credit risk, outperforming XGBoost's 0.84."
  - "Temporal encoding contributed the largest performance gain of 4.2%."
  - "Multi-source data integration significantly improves customer profiling quality."
  - "Contrastive learning produces more coherent and separable customer clusters."
  - "Self-supervised learning reduces dependence on costly labeled financial data."
```
---

## Paper 24: Simeonov et al_summarized.md

**Source File:** `Simeonov et al_summarized.md`

```yaml
paper_id: 10.1038/s41598-025-14364-7
designation: international-algorithm-specific
title: Analysing community-level spending behaviour contributing to high carbon emissions using stochastic block models
authors: Simeonov, O.; Restocchi, V.; Goddard, B. D.
year: 2025
venue: Scientific Reports
odin_topics:
  - 5.A
  - 5.C
  - 12.B
  - 12.A
  - 13.A
  - 7.A
  - 4.A
tldr: Stochastic block models on bipartite spending networks identify consumer communities with similar spending and emission patterns, enabling targeted sustainability interventions.
problem_and_motivation: Designing effective group-level carbon reduction interventions requires understanding consumer spending patterns across categories. Existing studies often focus on single purchase types or rely on self-reported data, and there is a gap in scalable methods to identify large consumer groups with shared emission profiles from transaction data.
approach:
  - Constructs a bipartite network connecting customers to Merchant Category Codes (MCCs) based on transaction history.
  - Applies a degree-corrected nonparametric hierarchical Stochastic Block Model (SBM) for community detection.
  - Introduces a weighted SBM variant that normalizes spending amounts by category averages to keep average community spending constant.
  - Runs the SBM algorithm 100 times and selects the partition with the highest posterior probability for stable community detection.
  - Validates the approach on an artificial dataset of one million transactions to test scalability.
findings:
  - num: The weighted SBM approach results in 71 out of 80 cluster-category spending percentages falling within one Median Absolute Deviation of the population median.
  - num: Unweighted SBM had fewer than half of clusters within one MAD, compared to over 88% for weighted SBM.
  - Communities identified by the SBM exhibit homogeneous spending patterns and distinct carbon emission profiles across merchant categories.
  - Weighted SBM creates customer groups with consistent spending proportions across categories, enabling ceteris paribus analysis of external factors.
  - The SBM method is scalable, with analysis of datasets with less than one million transactions completing in seconds.
key_figures_tables:
  - Figure 4: Heatmap of carbon emissions per MCC across clusters → Reveals dominant emission categories (e.g., groceries, taxis, service stations) for each consumer community.
  - Figure 5: Heatmap of weighted SBM spending percentages → Shows cluster spending aligns with population averages within one MAD.
  - Figure 7: Cluster emissions and spending for Taxicabs category → Identifies clusters 17 and 18 as targets for transaction-count versus amount-based interventions.
  - Table in Appendix: Age and IMD distribution → Customer base is predominantly younger and from more deprived areas.
  - Figure 9: Logistic regression for client retention → Younger and more deprived customers have higher dropout probability.
key_equations:
  - equation: MAD = median(|X_i - median(X)|)
    explanation: Median Absolute Deviation used to measure spending consistency across clusters.
definitions:
  - term: SBM
    definition: Stochastic Block Model, a probabilistic model for detecting community structures in networks.
  - term: MCC
    definition: Merchant Category Code, a four-digit code used by card providers to classify transactions.
  - term: MAD
    definition: Median Absolute Deviation, a robust measure of statistical dispersion.
  - term: IMD
    definition: Index of Multiple Deprivation, a UK measure of relative deprivation for small areas.
  - term: LCFS
    definition: Living Costs and Food Survey, a UK household expenditure survey.
critical_citations:
  - "[Trendl et al., 2023] — Provides the carbon multipliers used to estimate emissions from transactions."
  - "[Wells et al., 2025] — Demonstrates segmentation of households by carbon footprint using transaction data."
  - "[Di Clemente et al., 2018] — Shows that purchase sequences follow a Zipf-like distribution and can cluster consumers."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Core contribution is identifying consumer communities with similar spending and emission profiles.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Directly proposes and validates SBM as a classification method for spending behaviour.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Presents a quantitative evaluation of SBM performance and compares weighted vs. unweighted variants.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides a methodology for evaluating clustering results and their implication for targeted interventions.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: contextual
      justification: Mentions targeted interventions could encourage sustainable spending, indirectly relevant to savings.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: Discusses using cluster insights for behavioural nudges, a budgeting-related strategy.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews existing segmentation methods (k-means, MST-kNN) and positions SBM as an alternative.
  contribution: The paper provides a validated SBM-based methodology for identifying consumer communities with similar spending and carbon emission patterns. This methodology can be adapted for Odin's behavioral profiling module to group Filipino users for targeted financial recommendations. The weighted SBM variant offers a way to control for spending levels, allowing for cleaner analysis of how other factors influence emission or spending behavior. The hierarchical nature of the SBM supports analysis at different levels of granularity, which is useful for Odin's cold-start problem. The paper's emphasis on using only transaction data aligns with Odin's mobile-first design, avoiding reliance on demographic data that may not be available.
  directly_justifies:
    - "Stochastic block models effectively identify communities of consumers with homogeneous spending patterns."
    - "Weighted SBM can create consumer groups with consistent spending proportions across categories."
    - "Targeting clusters rather than individuals allows scalable implementation of behavioural interventions."
    - "SBM mitigates bias by clustering based on network properties, not socio-demographic attributes."
  limits:
    - "The SBM is static and does not account for time-varying data or evolving consumer behaviour."
    - "The model can be computationally expensive with large datasets."
    - "The probabilistic framework can make interpretation more difficult for non-technical audiences."
    - "The analysis relies on a sustainability-oriented subsample, limiting representativeness."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant for domains related to behavioral profiling and classification (5.A, 5.C) and system evaluation (12.B), as its core contribution is a novel classification method (SBM) and its quantitative evaluation. It also provided medium relevance for the existing systems landscape (4.A) by reviewing prior segmentation methods, and for evaluation frameworks (12.A) by outlining a validation process. The topics of savings (13.A) and budgeting strategies (7.A) were considered contextual, as the paper discusses behavioural interventions but does not directly address savings goals or budget allocation algorithms. Domains like expense categorization (3.A, 3.B), anomaly detection (8.A, 8.B), data privacy (10.A, 10.B), and engagement (11.A, 11.B) were considered and rejected because the paper does not provide actionable claims for these specific Odin modules. The overall relevance is high for algorithmic and methodological aspects of user profiling, with moderate relevance for framing the problem and evaluation.
limitations:
  - "Financial transaction data is often constrained by privacy and commercial restrictions, limiting dataset representativeness."
  - "The dataset reflects a sustainability-oriented subsample, limiting generalisability to the broader population."
  - "Carbon footprint estimates assume uniform carbon intensity within merchant categories, masking product-level variations."
  - "Utility payments and cash expenditures are often missing from transaction data."
  - "The SBM is static and does not account for evolving consumer behaviour over time. [unacknowledged]"
remember_this:
  - "Stochastic block models effectively identify consumer communities with similar spending patterns."
  - "Weighted SBM creates clusters with spending aligned to population averages within one Median Absolute Deviation."
  - "Targeting consumer groups enables scalable implementation of financial and sustainability interventions."
  - "SBM mitigates bias by clustering solely on transaction patterns, not socio-demographic attributes."
  - "The paper demonstrates a 31% improvement in cluster spending consistency using weighted SBM."
```
---

## Paper 25: Li & Gautam_summarized.md

**Source File:** `Li & Gautam_summarized.md`

```yaml
paper_id: "10.1145/3787120.3787130"
designation: "international-algorithm-specific"
title: "Segmented Confidence Sequences and Multi-Scale Adaptive Confidence Segments for Anomaly Detection in Nonstationary Time Series"
authors: "Li, M.; Gautam, A."
year: 2025
venue: "2025 5th International Conference on Artificial Intelligence and Application Technologies (AIAT2025)"
odin_topics:
  - "8.A"
  - "8.B"
  - "8.C"
  - "12.B"
tldr: "Presents two adaptive thresholding frameworks, Segmented Confidence Sequences and Multi-Scale Adaptive Confidence Segments, that improve anomaly detection in nonstationary time series by localizing statistical estimation and multi-scale attention, significantly outperforming static percentile baselines."
problem_and_motivation: "Traditional static thresholds fail under regime shifts and concept drift in nonstationary time series. Existing adaptive methods often struggle with multiple temporal scales or sudden changes. There is a need for statistically principled, unsupervised thresholds that adapt locally and maintain false alarm guarantees."
approach:
  - "Uses autoencoder reconstruction errors as anomaly scores on six public benchmark datasets with ground-truth labels."
  - "Segmented Confidence Sequences (SCS) partitions time series into locally stationary segments using APCA or K-means, then maintains Hoeffding-style confidence bounds per segment."
  - "Multi-Scale Adaptive Confidence Segments (MACS) maintains three rolling windows (short, medium, long) with independent confidence sequences and an attention mechanism that weights scales by local variance."
  - "MACS also performs regime change detection using CUSUM-like statistics and applies dual detection (threshold violation and attention-weighted bounds) during regime shifts."
  - "Both methods apply a global percentile filter as a conservative post-processing step."
  - "Compares against a fixed 99th percentile threshold baseline and evaluates F1-score, precision, recall, and accuracy."
findings:
  - "num: On Wafer Manufacturing, MACS increases F1-score by 2.17 points and recall by 3.99 compared to static percentile at alpha=0.99."
  - "num: At alpha=0.95, SCS APCA improves F1-score by 2.13 and recall by 6.16 on the same dataset."
  - "Both SCS and MACS outperform rolling quantile methods, particularly on datasets with pronounced regime shifts."
  - "The trade-off is higher recall at the cost of moderate precision loss."
  - "num: Across six datasets, SCS and MACS show positive F1-score deltas, with the largest gains on Wafer, GCP, MSL, and SMD."
key_figures_tables:
  - "Figure 3: F1-score comparison on Wafer dataset at alpha=0.99 → SCS and MACS outperform baseline significantly."
  - "Table 2: Cross-dataset F1-score delta vs. baseline → MACS and SCS show positive deltas across all six datasets."
  - "Table 3: Performance delta on Wafer Manufacturing → MACS achieves the highest F1 improvement."
key_equations:
  - equation: "lower_bound = \\bar{x} - bound\\_width"
    explanation: "Confidence interval lower bound based on local mean."
  - equation: "upper_bound = \\bar{x} + bound\\_width"
    explanation: "Confidence interval upper bound."
  - equation: "combined\\_bound = \\sum weight_i \\cdot bound_i"
    explanation: "Weighted sum of multi-scale bounds."
definitions:
  - term: "SCS"
    definition: "Segmented Confidence Sequences: adaptive thresholding by segmenting time series."
  - term: "MACS"
    definition: "Multi-Scale Adaptive Confidence Segments: multi-scale adaptive thresholding."
  - term: "APCA"
    definition: "Adaptive Piecewise Constant Approximation: segmentation method."
  - term: "Confidence sequence"
    definition: "Time-uniform interval guaranteeing coverage."
critical_citations:
  - "[Howard et al., 2021] — Provides foundation for confidence sequences."
  - "[Blázquez-García et al., 2021] — Reviews anomaly detection in time series."
relevance:
  topics:
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Directly proposes adaptive thresholding algorithms for anomaly detection in time series, applicable to PFMS."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Introduces SCS and MACS as novel algorithms for detecting anomalies."
    - code: "8.C"
      name: "Cold-Start Baseline Strategies for Anomaly Detection"
      relevance: "medium"
      justification: "Discusses static percentile baseline and adaptive methods that could inform cold-start strategies."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Provides comprehensive evaluation on benchmark datasets with metrics including F1, precision, recall."
  contribution: "The adaptive thresholding frameworks can be integrated into Odin's anomaly detection module to identify irregular spending patterns. The multi-scale attention mechanism of MACS can help detect both sudden spikes and gradual changes in user spending. The segmentation approach of SCS provides interpretable regime-specific thresholds, aiding in behavioral analysis. The evaluation methodology offers a template for assessing Odin's anomaly detection performance."
  directly_justifies:
    - "Adaptive thresholding improves recall over static methods in nonstationary data."
    - "Multi-scale analysis captures anomalies at different temporal resolutions."
    - "Confidence sequences provide statistical guarantees on false alarm rates."
    - "Unsupervised methods reduce reliance on labeled anomaly data."
  limits:
    - "Not validated on personal finance data."
    - "Requires tuning of confidence level and segmentation parameters."
  mapping_rationale: "I systematically scanned all 12 functional domains. Only domains related to anomaly detection and algorithmic evaluation were found relevant. The paper directly addresses anomaly detection (8.A and 8.B) with novel adaptive algorithms and provides evaluation (12.B). The cold-start topic (8.C) is tangentially related via baseline comparison. Other domains—cultural context, expense categorization, existing systems, behavioral profiling, forecasting, budget recommendation, mobile design, privacy, engagement, savings/debt—were rejected as the paper does not address financial specifics or PFMS design. Overall, the paper offers strong algorithmic contributions for Odin's anomaly detection module."
limitations:
  - "Performance depends on segmentation quality and may degrade on highly noisy data."
  - "Requires tuning of confidence levels and attention weights."
  - "Does not address computational efficiency for mobile deployment [unacknowledged]."
  - "Not tested on personal finance data [unacknowledged]."
remember_this:
  - "MACS improves F1 by up to 2.17 points over static percentile on Wafer dataset."
  - "SCS and MACS boost recall significantly with moderate precision loss."
  - "Confidence sequences provide statistical false alarm guarantees."
  - "Adaptive thresholds adapt to regime shifts and multi-scale changes."
```
---


---

## Agent Instruction

If the agent reading this document believes further context about a paper is needed, it may request the original converted markdown file (with the '_marked' suffix) from the user for the relevant paper(s).
