```yaml
paper_id: 7b8c9d0e-1f2a-3b4c-5d6e-7f8a9b0c1d2e
designation: international-algorithm-specific
title: Recurrent Neural Networks and Long Short-Term Memory Networks: Tutorial and Survey
authors: Ghojogh, B.; Ghodsi, A.
year: 2022
venue: Unknown
odin_topics:
  - 6.A
  - 6.B
  - 8.B
  - 5.C
tldr: This tutorial surveys RNNs and LSTM networks, covering BPTT, gradient issues, architectural variants, and bidirectional processing for sequence modeling.
problem_and_motivation: RNNs suffer from vanishing and exploding gradients during backpropagation, which hinders learning long-term dependencies. A robust architecture was needed to control information flow and selectively retain or forget past states.
approach:
  - Defines RNN as a dynamical system with parameter sharing and describes BPTT for training.
  - Analyzes gradient vanishing/explosion through eigenvalue decomposition of the state transition matrix.
  - Reviews solutions like close-to-identity weight matrices, long delays, leaky units, and echo state networks.
  - Presents LSTM with input, forget, and output gates, peepholes, and memory cells to control information flow.
  - Describes GRU as a simplified LSTM variant with reset and update gates, and the minimal gated unit.
  - Introduces bidirectional RNNs and LSTMs that process sequences in both directions, and the ELMo network.
findings:
  - num: Gradient vanishing is more common than exploding in RNNs with long sequences.
  - num: Using a weight matrix with largest eigenvalue slightly less than one (λ ≲ 1) helps mitigate gradient issues.
  - num: GRU simplifies LSTM without significant performance loss for many tasks.
  - The forget gate in LSTM allows the network to learn when to clear the state.
  - Bidirectional processing outperforms unidirectional LSTM for offline tasks like speech recognition.
key_figures_tables:
  - Figure 1: Folded/unfolded RNN structure showing parameter sharing across time steps → RNN processes sequences via recurrent connections.
  - Figure 5: LSTM cell with input, forget, output gates and memory cell → Gating controls information retention and update.
  - Figure 6: GRU cell with reset and update gates → Simplified gating mechanism for sequence learning.
  - Figure 9: ELMo architecture with multiple bidirectional LSTM layers → Deep contextualized word representations.
key_equations:
  - equation: h_t = tanh(W h_{t-1} + U x_t + b_i)
    explanation: RNN state update uses input and previous hidden state.
  - equation: c_t = (f_t ⊙ c_{t-1}) + (i_t ⊙ \tilde{c}_t)
    explanation: LSTM memory combines old and new controlled by gates.
  - equation: h_t = (1 - z_t) ⊙ h_{t-1} + z_t ⊙ \tilde{h}_t
    explanation: GRU hidden state uses update gate to merge old and new.
definitions:
  - term: RNN
    definition: Recurrent Neural Network; a neural network with connections forming cycles to process sequences.
  - term: LSTM
    definition: Long Short-Term Memory; a type of RNN with gated cells to learn long-term dependencies.
  - term: GRU
    definition: Gated Recurrent Unit; a simplified LSTM variant with fewer gates.
  - term: BPTT
    definition: Backpropagation Through Time; the training algorithm for RNNs that unrolls the network across time steps.
  - term: Gradient Vanishing
    definition: Problem where gradients become very small during backpropagation, preventing learning of long-term dependencies.
critical_citations:
  - "[Hochreiter & Schmidhuber, 1997] — Introduced LSTM with input and output gates."
  - "[Gers et al., 2000] — Added forget gate and peephole connections to LSTM."
  - "[Cho et al., 2014] — Proposed GRU as a simplified LSTM variant."
  - "[Graves & Schmidhuber, 2005a] — Developed bidirectional LSTM and vanilla LSTM."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Covers RNN/LSTM architectures essential for forecasting financial sequences.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Discusses algorithms (LSTM, GRU) suitable for predicting sequential spending patterns.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: LSTM can be used to model normal spending patterns for anomaly detection.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: RNNs can classify sequences of transactions into behavioral profiles.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: RNNs are designed to capture temporal patterns, applicable to seasonality.
  contribution: |
    The paper provides a comprehensive theoretical foundation for RNN and LSTM architectures, including their training dynamics and variants. This directly informs the choice of sequence models for Odin's spending forecasting module (Topic 6.B). The analysis of gradient issues and gating mechanisms justifies the adoption of LSTM/GRU over vanilla RNNs for capturing long-term financial dependencies. The survey of bidirectional processing suggests potential improvements for offline analysis of transaction histories.
  directly_justifies:
    - "RNNs can model sequential spending data due to their recurrent structure."
    - "LSTM's forget gate allows the model to learn when to ignore past spending patterns."
    - "GRU provides a simpler alternative with comparable performance to LSTM."
    - "Bidirectional LSTM can leverage future transaction context in offline analysis."
  limits:
    - "The paper is a tutorial/survey and does not provide new empirical results."
    - "No specific evaluation on financial time-series data is presented."
  mapping_rationale: |
    A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper's primary contribution to sequence modeling algorithms was deemed highly relevant to Predictive Modeling (6.A) and Forecasting Algorithms (6.B), as it provides the theoretical basis for using RNNs/LSTMs for sequential data, which is directly applicable to spending forecasts. It was also considered medium relevance to Anomaly Detection (8.B) and Behavioral Classification (5.C), as these modules can leverage sequence models for identifying outliers or classifying user behavior patterns. The paper touches on seasonal spending (2.B) and mobile design (9.A) only in a contextual manner, as these are not the focus; no concrete design principles or Filipino-specific insights are offered. Topics related to privacy (10), evaluation frameworks (12), and savings/debt (13) were considered and rejected, as the paper does not address these areas. Overall, this paper serves as a core algorithmic reference for Odin's forecasting and detection modules.
limitations:
  - "The tutorial focuses on conceptual explanations and does not include empirical comparisons on specific datasets. [unacknowledged]"
  - "The paper does not address the computational efficiency or deployability on mobile devices. [unacknowledged]"
  - "Limited discussion on handling missing data or irregularly sampled time series, common in personal finance. [unacknowledged]"
remember_this:
  - "RNN training faces gradient vanishing or explosion for long sequences."
  - "LSTM gates enable learning when to retain or forget information."
  - "GRU is a simplified LSTM variant with comparable performance."
  - "Bidirectional processing improves sequence modeling for offline tasks."
  - "Largest eigenvalue of weight matrix should be slightly less than one."
```