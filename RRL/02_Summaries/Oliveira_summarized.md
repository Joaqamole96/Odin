```yaml
paper_id: 10.66104/xkad2306
designation: international
title: Neural Networks for Real-Time Financial Fraud Detection
authors: Oliveira, D. N. O.
year: 2026
venue: Unknown
odin_topics:
  - 8.A
  - 8.B
  - 4.B
  - 10.A
  - 10.B
  - 12.B
tldr: Neural network architectures are redefining real-time fraud detection, yet their deployment faces significant challenges in latency, explainability, adversarial robustness, and cross-institutional collaboration.
problem_and_motivation: Conventional rule-based and statistical fraud detection methods are structurally inadequate for the complexity, volume, and adaptability of modern fraud operations. This detection gap necessitates fundamentally different solutions capable of real-time analysis and continuous adaptation.
approach:
  - The paper presents a narrative literature review of neural network architectures for fraud detection.
  - It covers theoretical foundations and six principal architectures: MLP, LSTM, GRU, CNN, Autoencoders, GNN, and Transformers.
  - The review analyzes critical operational challenges including concept drift, adversarial evasion, class imbalance, and explainability.
  - It examines production infrastructure requirements such as latency budgets and stream processing architectures.
  - Real-world implementations across credit card networks, PIX, AML, and insurance fraud are documented.
findings:
  - num: Global fraud losses were estimated at $485.6 billion in 2023, with $3.1 trillion in illicit funds flowing through the global financial system.
  - num: GNN-based models achieve recall of 0.89 on financial transaction data, compared to 0.78 for Random Forest and 0.81 for XGBoost.
  - num: PGD adversarial training reduces Attack Success Rate from 87.5% to 32.0%, delivering a 52.3% reduction in expected annual fraud loss.
  - num: Mastercard's AI-enhanced system detects three times the volume of fraudulent transactions while reducing false positives tenfold.
  - No single neural architecture dominates across all fraud typologies, making hybrid and ensemble frameworks the current performance frontier.
  - The integration of regulatory compliance, explainability, adversarial robustness, and data privacy alongside predictive accuracy is the defining challenge for production systems.
key_figures_tables:
  - "Table 1: Comparative performance of neural network architectures → Shows MLP F1 0.851, 1D-CNN F1 0.960, VAE+GAT+XGBoost AUC 0.995."
  - "Table 2: Computational profiles of architectures → MLP fastest, GNN and Transformer have high complexity/latency."
key_equations:
  - equation: "\\text{BCE}(y, \\hat{y}) = -[y \\log(\\hat{y}) + (1-y) \\log(1-\\hat{y})]"
    explanation: Binary Cross-Entropy loss for fraud classification.
  - equation: "\\text{ReLU}(x) = \\max(0, x)"
    explanation: Dominant activation function in fraud detection models.
definitions:
  - term: CNP Fraud
    definition: Card-not-present fraud, where stolen credentials are used in online or telephone transactions.
  - term: GNN
    definition: Graph Neural Network, which operates on relational data to detect fraud rings and network-level anomalies.
  - term: FL
    definition: Federated Learning, a training paradigm allowing cross-institutional model training without centralizing raw data.
  - term: DP
    definition: Differential Privacy, a technique providing formal guarantees against inferring individual data points from model outputs.
  - term: Concept Drift
    definition: The change in the relationship between input features and the target label over time.
critical_citations:
  - "[Ngo et al., 2025] — Comprehensive deep learning fraud detection survey."
  - "[Hilal et al., 2022] — Anomaly detection techniques review, defines real-time fraud as soft real-time."
  - "[Liu et al., 2024] — Systematic review of GNNs for financial fraud detection."
  - "[Černevičienė & Kabašinskas, 2024] — XAI in finance, highlights interpretability vs. opacity tension."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly reviews anomaly detection methods and their theoretical foundations applied to financial fraud.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Provides detailed comparative analysis of algorithms (LSTM, GNN, Autoencoders, Transformers) for fraud detection.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Extensively documents structural inadequacies of rule-based and statistical legacy systems.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Discusses Federated Learning and Differential Privacy as constraints and solutions for fraud detection.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: contextual
      justification: Indirectly relevant via discussion of false positives and algorithmic bias, which affect trust.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Critically assesses performance benchmarks and identifies overfitting, data leakage, and publication bias.
  contribution: "This paper provides a comprehensive, systems-level review of neural network architectures for real-time fraud detection. It directly justifies Odin's use of anomaly detection modules (8.A, 8.B) by demonstrating the necessity of moving beyond rule-based systems. The analysis of concept drift and adversarial attacks (8.B) informs the design of robust, adaptive ML components. The detailed review of GNNs and ensemble methods offers concrete architectural options for anomaly detection. The discussion of production constraints, including latency and feature stores, provides critical context for deployment."
  directly_justifies:
    - "Rule-based and statistical fraud detection systems are structurally inadequate for modern financial fraud."
    - "Real-time detection requires neural network inference within sub-100-millisecond latency budgets."
    - "Graph Neural Networks are uniquely capable of detecting fraud rings invisible to transaction-level classifiers."
    - "Federated Learning enables privacy-preserving cross-institutional model training for fraud detection."
  limits:
    - "The review is a narrative synthesis, not a systematic meta-analysis, introducing potential subjective bias in study selection."
    - "Benchmark performance metrics (e.g., AUC > 0.99) are optimistic upper bounds and may not generalize to production. [unacknowledged]"
    - "The review does not empirically compare architectures on a unified dataset, making direct performance claims difficult to validate. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to 'Anomaly Detection' (8.A, 8.B) as its core subject. It also provides strong evidence for 'Limitations and Gaps in Existing Systems' (4.B), justifying the need for Odin's ML-based approach. It touches on 'Data Privacy' (10.A, 10.B) at a medium level through discussions of Federated Learning and user trust via false positive analysis. Evaluation frameworks (12.B) are also relevant, as the paper critically reviews benchmarking methodologies. The paper was considered and rejected for topics like 'Spending Forecasting' (6.A) and 'Budget Recommendation' (7.A) as it does not directly address personal spending prediction or allocation, which are Odin's core functionalities. Borderline cases included concept drift (2.B, 2.D), which was rejected in favor of 8.B as the paper frames it as an ML operational challenge, not a cultural spending pattern. Overall, the paper is highly relevant for informing the design, justification, and evaluation of Odin's anomaly detection module."
limitations:
  - "Access to real financial transaction data is severely restricted by data protection regulations, limiting generalizability."
  - "The literature exhibits a publication bias toward positive results, creating a distorted picture of the state of the art. [unacknowledged]"
  - "Reproducibility poses a structural challenge due to proprietary datasets and omitted implementation details. [unacknowledged]"
  - "The review's narrative methodology may introduce subjective bias. [unacknowledged]"
remember_this:
  - "Neural networks structurally outperform rule-based systems for fraud detection."
  - "Real-time fraud detection must operate within a strict 100-millisecond latency budget."
  - "GNNs are uniquely effective at detecting fraud rings through relational analysis."
  - "Adversarial training can reduce fraud loss by 52.3% against evasion attacks."
  - "Federated Learning enables cross-institutional fraud model training without sharing raw data."
```
