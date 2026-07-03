```yaml
paper_id: 10.51483/IJAIML.6.2s.2026.754-762
designation: international-algorithm-specific
title: Robust Learning Under Distribution Shifts for Non-Stationary Data Environments
authors: "D, Rekha; Vairavan, Shanthi; MP, Sunil; Katariya, Jitendra Kumar; Parikh, Swapnil Maheshkumar; Shanthi, T.; Shanthi, R."
year: 2026
venue: International Journal of Artificial Intelligence and Machine Learning
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 12.B
tldr: Introduces an adaptive learning framework combining drift detection, online incremental learning, and AHO optimization to maintain robust classification performance under sudden, gradual, and recurrent distribution shifts.
problem_and_motivation: Non-stationary data environments cause performance degradation in static ML models due to concept drift. Existing approaches treat drift detection, adaptation, and optimization separately, limiting robustness. A unified framework is needed to handle diverse drift types while maintaining computational efficiency.
approach:
  - Uses PaySim mobile money transaction dataset with 743 time steps and five transaction types.
  - Proposes AHO-InDNN combining an incremental deep neural network with archerfish hunting optimization for parameter tuning.
  - Integrates drift detection module to identify sudden, gradual, and recurrent concept drift using statistical divergence.
  - Employs online and incremental learning to update model parameters without full retraining upon drift detection.
  - Applies Lévy flight reinitialization to avoid stagnation and an LDP-based optimization for stability and uncertainty reduction.
  - Compares against KNN, SMOTEBoost with cost-sensitive learning, and MH-DRNN using accuracy, precision, recall, F1.
findings:
  - "num: AHO-InDNN achieved 98.74% accuracy, 98.42% precision, 98.52% recall, and 98.37% F1-score."
  - "num: Outperformed MH-DRNN by 0.24% in accuracy and 0.37% in F1."
  - Demonstrated superior robustness across sudden, gradual, and recurrent drift scenarios.
  - LDP-based optimization reduced false alarms and improved stability under distribution shifts.
key_figures_tables:
  - "Figure 2: Illustrates sudden, gradual, and recurrent concept drift patterns in fraud rate → demonstrates need for adaptive learning."
  - "Table 2: Performance comparison of models under dynamic shifts → AHO-InDNN achieves highest metrics."
  - "Figure 3: Recall and F1 comparison → proposed model outperforms baselines."
key_equations:
  - equation: "y' = (y - y_min) / (y_max - y_min)"
    explanation: Min-max normalization scales features to [0,1].
  - equation: "F(θ) = - (1/M) ∑_m ∑_p s_mp log x_mp"
    explanation: Regularized loss function mitigates overfitting under drift.
  - equation: "θ_s = θ_{s-1} - α * (β1*m_{s-1} + (1-β1)*∇θ F(θ_{s-1})) / (sqrt(β2*v_{s-1} + (1-β2)*(∇θ F(θ_{s-1}))^2) + ε)"
    explanation: Adaptive moment-based gradient optimization for dynamic environments.
  - equation: "lim_{s→∞} (1/s) log P(X_s ∈ A) = - inf_{x∈A} I(x)"
    explanation: LDP detects rare distributional shifts in streaming data.
definitions:
  - term: AHO
    definition: Archerfish Hunting Optimization, a metaheuristic for parameter tuning balancing exploration and exploitation.
  - term: InDNN
    definition: Incremental Deep Neural Network with dynamic depth and neuron structure for non-stationary data.
  - term: LDP
    definition: Large Deviations Principle, a framework for estimating probabilities of rare events in streaming data.
  - term: Concept Drift
    definition: Change in the input-output relationship over time, causing model performance decay.
  - term: Distribution Shift
    definition: Change in the data distribution between training and testing phases.
critical_citations:
  - "[Liu et al., 2024] — Introduces deep reinforcement learning in nonstationary environments."
  - "[Halstead et al., 2022] — Analyzes concept drift adaptation in data streams."
  - "[Ma et al., 2023] — Discusses transfer learning under domain shift."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: low
      justification: Paper uses predictive modeling for fraud, not personal finance, but concept is transferable.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: Handles sequential transaction data and concept drift, relevant to spending forecasting.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Fraud detection is a form of anomaly detection; framework can inform spending anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Proposes a novel drift-adaptive algorithm for detecting fraudulent anomalies in transaction streams.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Provides comparative evaluation metrics and baselines useful for assessing Odin's modules.
  contribution: The paper's drift-adaptive framework informs Odin's anomaly detection module (8.B) by providing a robust online learning approach to detect unusual spending patterns. Its incremental learning capability supports forecasting module (6.B) for adapting to evolving user behavior. The evaluation methodology offers a baseline for assessing Odin's algorithmic modules (12.B). The LDP-based optimization could enhance stability in rare anomaly detection. Overall, the adaptive principles are applicable to Odin's real-time adjustment to shifting user financial behavior.
  directly_justifies:
    - "Adaptive models are necessary to maintain accuracy when spending patterns shift over time."
    - "Incremental updating without full retraining reduces computational cost while preserving performance."
    - "LDP-based optimization enhances stability under rare anomalous events."
    - "Drift detection enables timely model updates without manual intervention."
  limits:
    - "Relies on synthetic PaySim data rather than real-world financial transactions."
    - "Computational complexity of AHO optimization may need optimization for mobile deployment."
    - "Generalization to other financial domains (e.g., savings, budgeting) not evaluated. [unacknowledged]"
  mapping_rationale: "All 12 functional domains and their associated topic codes were systematically scanned. The paper is relevant to Anomaly Detection (8.A, 8.B) and Spending Forecasting (6.A, 6.B) because it addresses concept drift in sequential transaction data, a core challenge for personal finance systems. Evaluation methodologies (12.B) are also flagged due to the comparative benchmarking. Domains such as Filipino Cultural Context (2.A–D), Expense Categorization (3.A–C), Existing Systems (4.A–B), Behavioral Profiling (5.A–C), Budget Recommendation (7.A–D), Mobile-First Design (9.A–B), Data Privacy (10.A–B), User Retention (11.A–B), and Savings/Debt (13.A–C) were considered but rejected because the paper does not address these aspects; it focuses solely on algorithmic robustness under drift. Relevance levels: 8.B = high (direct algorithm for anomaly detection), 8.A and 6.B = medium (contextual but transferable), 6.A and 12.B = low/medium. Borderline cases: 6.A (predictive modeling) overlaps with 6.B but the paper is more about forecasting sequential data than general predictive modeling; we selected 6.B as more specific. Overall, the paper offers actionable insights for Odin's adaptive learning and anomaly detection modules but is not directly applicable to other domains."
limitations:
  - "Synthetic dataset may not capture real-world noise and variability."
  - "AHO optimization adds computational overhead not quantified for edge devices. [unacknowledged]"
  - "Framework tested only on fraud detection; applicability to spending categorization or budgeting not explored. [unacknowledged]"
remember_this:
  - "AHO-InDNN achieves 98.74% accuracy on fraud detection under concept drift."
  - "Incremental learning adapts to sudden, gradual, and recurrent drifts without full retraining."
  - "LDP optimization reduces false alarms and stabilizes model updates."
  - "Drift detection and online adaptation are key for maintaining performance in non-stationary environments."
```