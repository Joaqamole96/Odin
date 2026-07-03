```yaml
paper_id: 10.62951/ijamc.v1i1.3
designation: local-algorithm-specific # Published in UP Diliman
title: A Comparative Analysis of Machine Learning Models for Predictive Analytics in Finance
authors: Reyes, J. M.; Santos, L. P.; Perez, A.
year: 2024
venue: International Journal of Applied Mathematics and Computing
odin_topics:
  - 6.A
  - 6.B
  - 12.A
  - 12.B
tldr: Compares linear regression, decision trees, support vector machines, and deep learning for financial time-series forecasting, highlighting trade-offs among accuracy, computational cost, and interpretability.
problem_and_motivation: Financial predictive analytics requires robust modeling techniques to capture complex patterns in time-series data. There is a trade-off between model accuracy and interpretability, complicating model selection for practitioners. This paper addresses this by systematically comparing four common machine learning models on financial data.
approach:
  - Evaluates linear regression, decision trees, support vector machines, and deep learning on a dataset of historical stock prices and economic indicators.
  - Measures performance using accuracy, computational cost (training time), and interpretability.
  - Compares baselines across models and reports average accuracy and training durations.
  - Draws on case studies from hedge funds and banks to illustrate practical implications.
findings:
  - num: Deep learning achieved 92% average accuracy, outperforming SVM at 89%, decision trees at 83%, and linear regression at 78%.
  - num: Deep learning training averaged 48 hours, SVM about 1 hour, decision trees 30 minutes, and linear regression 15 minutes.
  - Deep learning offers superior accuracy but suffers from low interpretability.
  - Linear regression and decision trees are highly interpretable and computationally efficient.
  - The choice of model should align with organizational goals, regulatory requirements, and data complexity.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: SVM
    definition: Support Vector Machine, a model that finds the optimal hyperplane for classification or regression.
  - term: MAE
    definition: Mean Absolute Error, a metric measuring average prediction error magnitude.
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network architecture for sequential data.
  - term: RNN
    definition: Recurrent Neural Network, a neural network designed for sequence processing.
critical_citations:
  - "[Fischer and Krauss, 2018] — LSTM achieved 90% accuracy in stock prediction."
  - "[Chen et al., 2019] — SVM outperformed linear regression with 87% accuracy."
  - "[Lipton, 2016] — Lack of interpretability hinders trust in complex models."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Compares predictive models for time-series forecasting, relevant to Odin's forecasting module.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: Evaluates algorithms including deep learning and SVM, applicable to spending forecast.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Discusses evaluation metrics (accuracy, MAE) and trade-offs, informing Odin's system evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Provides comparative analysis of algorithm performance, useful for selecting Odin's algorithmic modules.
  contribution: The comparison of forecasting algorithms directly informs the selection of models for Odin's spending forecasting module. The trade-off analysis helps balance accuracy and interpretability in budget recommendation. The evaluation metrics (accuracy, MAE) are applicable to Odin's system evaluation. The guidelines for model selection can be adapted for Odin's cold-start and anomaly detection modules. This paper provides a foundational understanding of model performance that can guide Odin's algorithmic choices.
  directly_justifies:
    - Deep learning models achieved 92% accuracy on financial time-series data, suggesting potential for high-accuracy spending forecasts.
    - Training times for deep learning are substantially higher (48 hours), which may be prohibitive for real-time Odin updates.
    - Linear regression offers interpretability but lower accuracy, suitable for scenarios requiring transparency.
    - The trade-off between accuracy and interpretability is critical for designing user-trusted PFMS modules.
  limits:
    - Not specific to personal finance spending data; uses stock prices and economic indicators.
    - Does not address Filipino cultural practices or spending cycles.
    - Lacks analysis of user behavioral profiles or categorization constraints.
    - Evaluation does not consider cold-start or infeasibility scenarios.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The domains flagged as relevant were Spending Forecasting (6.A, 6.B) and System Evaluation (12.A, 12.B), each assigned medium relevance because the paper provides general comparative insights but does not address PFMS-specific spending data. Borderline cases: the paper touches on model interpretability, which could relate to user trust (10.B) but not explicitly, so it was rejected. Domains such as Filipino cultural context, expense categorization, budgeting, anomaly detection, mobile design, privacy, retention, and savings/debt were considered and rejected because the paper does not mention these topics. The paper's overall relevance to Odin is moderate; it offers methodological guidance for selecting and evaluating forecasting algorithms but lacks direct application to personal finance management in the Filipino context.
limitations:
  - The study does not specify the origin or composition of the dataset, limiting generalizability. [unacknowledged]
  - Results are based on stock and economic data, not personal spending patterns. [unacknowledged]
  - Interpretability is assessed qualitatively, without formal metrics. [unacknowledged]
  - The paper does not discuss model robustness or performance on irregular spending sequences.
remember_this:
  - Deep learning achieved 92% accuracy but required 48 hours of training.
  - Linear regression is interpretable and fast but only 78% accurate.
  - Model selection hinges on balancing accuracy, cost, and interpretability.
  - The trade-off analysis is directly applicable to Odin's module design choices.
```
