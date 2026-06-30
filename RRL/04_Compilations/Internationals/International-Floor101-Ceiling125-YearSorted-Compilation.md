# Compiled Research Summaries

## Filters Applied

- Designation: `international`

**Total Papers:** 16

**Note:** Included papers positions 101 to 125 (clipped to 116 available), Sorted by year.

---

## Paper 1: Thundiyil et al_summarized.md

**Source File:** `Thundiyil et al_summarized.md`

```yaml
paper_id: 10.48550/arXiv.2304.06183
designation: international
title: Transformer Architectures in Time Series Analysis: A Review
authors: Thundiyil, S.; Picone, J.; McKenzie, S.
year: 2023
venue: arXiv
odin_topics:
  - 3.A
  - 4.A
  - 5.C
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 9.A
  - 9.B
  - 12.A
  - 12.B
  - 12.C
  - 1.A
  - 1.B
  - 1.C
  - 2.B
tldr: A review of transformer-based architectures for time series analysis, highlighting their superior performance in capturing long-term dependencies for forecasting, classification, and anomaly detection.
problem_and_motivation: Traditional time series methods like ARIMA and LSTMs struggle to capture long-term dependencies critical for accurate forecasting and classification. The emergence of transformer architectures offers a powerful solution, but a comprehensive review of their variants and applications is needed to guide adoption. This paper fills that gap by synthesizing the state of the art in transformer-based time series modeling.
approach:
  - This is a comprehensive review paper that surveys and synthesizes existing literature on transformer architectures for time series analysis.
  - The review covers 11 transformer-based architectures, including LogTrans, TFT, Informer, Autoformer, and FEDformer.
  - It systematically compares traditional methods (ARIMA, LSTM) with modern transformer variants across healthcare, finance, and climate applications.
  - The analysis focuses on architectures addressing segmentation, forecasting, and classification challenges.
  - The paper provides a structured comparison of key features, application areas, and quantitative performance improvements.
findings:
  - num: Autoformer achieved a 38% averaged MSE reduction across six benchmark datasets compared to existing methods.
  - num: FEDformer delivered an overall 14.8% relative MSE reduction compared to Autoformer on six datasets.
  - num: Transformer-XL reduced perplexity from 20.5 to 18.3 on WikiText-103, demonstrating superior long-term dependency modeling.
  - num: Pyraformer decreased MSE by 24.8%, 28.9%, and 26.2% for prediction lengths of 168, 336, and 720 on the ETTh1 dataset.
  - num: W-Transformers achieved superior RMSE performance across multiple datasets, significantly outperforming WARIMA and LSTM models.
  - num: In the ETTm2 dataset, InParformer achieved an MSE of 0.260 and an MAE of 0.323 for a prediction length of 192, outperforming FEDformer.
  - num: On ImageNet, CrossFormer++-B achieved 84.2% accuracy, surpassing existing vision transformers.
  - num: TFT improved MAPE by 2% to 8% in district heating load forecasting during spring and fall seasons.
  - num: CrossFormer++ surpassed CrossFormer by at least 0.5% average precision (AP) on the COCO 2017 dataset.
  - Transformer architectures consistently outperform traditional RNN-based methods for modeling long-term temporal dependencies.
key_figures_tables:
  - Figure 1: Dow Jones performance from Jan 2023 to Feb 2024 → Illustrates trend and seasonality in financial time series.
  - Figure 2: Satellite images of glacier shrinkage from 1985 to 2021 → Demonstrates spatial context in time series data.
  - Figure 3: Recording of a 10-second EEG signal → Shows multichannel temporal and spatial dependencies.
  - Table 1: Comparison of traditional methods → Summarizes advantages and disadvantages of classical approaches.
  - Table 2: Comparison of modern approaches → Highlights strengths and weaknesses of contemporary methods.
  - Table 3: Ablation study of LogTrans framework → Shows incremental improvements from SeCo and ReSD modules.
  - Table 4: Comparison of W-Transformer with other architectures → Demonstrates superior RMSE and MAE across datasets.
  - Table 5: Summary of transformer architectures → Provides a comprehensive overview of models and their applications.
key_equations:
  - equation: R(τ) = E[(x(t) - μ)(x(t + τ) - μ)] / σ²
    explanation: Defines autocorrelation of time series at lag τ.
  - equation: Attention(Q,K,V) = softmax(QK^T / √d_k) V
    explanation: Core scaled dot-product attention mechanism.
  - equation: Multihead(Q,K,V) = Concat(head1,...,headh)W_O
    explanation: Multi-head attention concatenates multiple attention outputs.
definitions:
  - term: Autocorrelation
    definition: Correlation between a time series and a lagged version of itself.
  - term: Seasonality
    definition: Regular fluctuations at specific intervals like daily or yearly.
  - term: Stationarity
    definition: Statistical properties like mean and variance are constant over time.
  - term: Self-Attention
    definition: Mechanism assigning importance weights to different parts of an input sequence.
  - term: Transformer
    definition: Deep learning architecture using self-attention to process sequential data.
critical_citations:
  - "[Vaswani et al., 2017] — Introduced the original Transformer architecture with self-attention."
  - "[Zhou et al., 2021] — Proposed Informer with ProbSparse attention for efficient long-sequence forecasting."
  - "[Wu et al., 2022] — Developed Autoformer with autocorrelation mechanism for improved periodicity modeling."
  - "[Lim et al., 2019] — Introduced Temporal Fusion Transformer for interpretable multi-horizon forecasting."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Provides general context on time series applications in finance and healthcare relevant to YPs.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: contextual
      justification: Discusses time series analysis in financial domains indirectly relevant to financial structure.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: contextual
      justification: General background on forecasting and anomaly detection useful for understanding spending behavior.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: Review covers seasonality in time series, supporting modeling of cyclical spending patterns.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: low
      justification: General techniques for time series classification inform categorization but are not directly applied.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides context on traditional methods but not direct PFMS system analysis.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Classification methods like CNNs and SVMs are discussed, but not specific to financial profiling.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: This paper directly reviews and evaluates advanced forecasting models applicable to PFMS.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Detailed analysis of transformer-based algorithms specifically for time series forecasting.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Reviews anomaly detection methods applicable to identifying unusual spending patterns.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Discusses One-Class SVM and autoencoders, which are relevant for spending anomaly detection.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: Model efficiency considerations are relevant for mobile deployment but not explicitly discussed.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: contextual
      justification: Resource-constrained model discussions relate to mobile implementation constraints.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides comprehensive evaluation methodologies and metrics (MSE, MAE, MAPE).
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Offers detailed performance comparisons of transformer-based algorithm modules.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: high
      justification: Forecasting accuracy metrics and evaluation setups are directly transferable to budget recommendation evaluation.
  contribution: This review provides Odin with a comprehensive catalogue of state-of-the-art transformer architectures suitable for forecasting and anomaly detection modules. It establishes performance benchmarks for predictive modeling (6.A/6.B) and evaluation frameworks (12.A/12.B/12.C). The paper validates the choice of transformers over traditional methods for capturing long-term spending patterns and seasonal cycles (2.B). It also highlights key considerations for model selection (e.g., efficiency for mobile deployment, handling irregular data) that inform Odin's design decisions.
  directly_justifies:
    - "Transformer architectures significantly outperform RNNs and LSTMs for long-term time series forecasting tasks."
    - "Autoformer and FEDformer provide state-of-the-art accuracy with 38% and 14.8% MSE reductions, respectively."
    - "Attention mechanisms effectively capture seasonal and cyclical patterns in time series data."
    - "Temporal Fusion Transformer integrates static metadata and handles missing data, suitable for personal finance."
    - "Efficiency improvements (e.g., Informer, Pyraformer) enable deployment in resource-constrained environments."
  limits:
    - The review does not evaluate models specifically on personal finance spending data.
    - Most benchmarks focus on energy, traffic, and climate data, not financial transactions.
    - No discussion of cold-start problems or user-specific profile dynamics in forecasting.
    - The paper is a review and does not propose new algorithms or provide empirical results for PFMS contexts.
    - Focuses primarily on univariate and multivariate forecasting, not budget recommendation optimization.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated canonical topic codes was performed. The paper's relevance was identified primarily in four domains: Spending Forecasting (codes 6.A, 6.B), Anomaly Detection (8.A, 8.B), System Evaluation (12.A, 12.B, 12.C), and Behavioral Profiling & Classification (5.C). Codes 6.A and 6.B were assigned 'high' relevance because the paper directly reviews and compares state-of-the-art forecasting algorithms applicable to Odin's predictive module. Codes 12.A, 12.B, and 12.C were assigned 'high' relevance as the paper provides comprehensive evaluation frameworks and performance metrics transferable to Odin's system evaluation. Code 2.B (Seasonal and Cyclical Spending Patterns) was assigned 'medium' relevance due to its detailed treatment of seasonality in time series. Codes 8.A and 8.B received 'medium' relevance as the review covers anomaly detection methods applicable to spending data. Codes 3.A, 5.C, and 9.A were assigned 'low' relevance as they touch on general classification and efficiency considerations but lack specific focus on Odin's requirements. The Filipino Cultural Context domain (2.A, 2.C, 2.D) and domains like Savings & Debt Management (13.A, 13.B, 13.C) were considered but rejected due to the paper's technical focus on modeling rather than cultural or financial management specifics. The overall relevance is high for Odin's algorithmic and evaluation frameworks, providing a robust foundation for selecting and justifying transformer-based approaches for forecasting and anomaly detection.
limitations:
  - "The review does not specifically address personal finance spending data, limiting direct applicability. [unacknowledged]"
  - "Performance benchmarks are primarily on energy, traffic, and climate datasets, not financial transaction sequences. [unacknowledged]"
  - "Cold-start scenarios and user-specific profile dynamics are not discussed, which are critical for Odin. [unacknowledged]"
  - "No analysis of budget recommendation or constrained optimization approaches (7.A-7.D) is provided. [unacknowledged]"
  - "Model interpretability and user trust (10.A/10.B) are not addressed, though TFT mentions interpretability features. [unacknowledged]"
remember_this:
  - "Transformer architectures achieve 38% average MSE reduction over traditional methods for long-term forecasting."
  - "Autoformer and FEDformer are state-of-the-art for capturing periodicity and seasonality in time series data."
  - "Model efficiency variants like Informer and Pyraformer are suitable for resource-constrained mobile deployment."
  - "Temporal Fusion Transformer handles missing data and provides interpretable forecasts with uncertainty estimates."
  - "Evaluation frameworks using MSE, MAE, and MAPE are well-established for time series model comparison."
```
---

## Paper 2: Ao & Fayek_summarized.md

**Source File:** `Ao & Fayek_summarized.md`

```yaml
paper_id: 10.3390/s23167167
designation: international
title: Continual Deep Learning for Time Series Modeling
authors: Ao, S.-I.; Fayek, H.
year: 2023
venue: Sensors
odin_topics:
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 9.A
  - 12.A
  - 12.B
tldr: A systematic review of deep learning applications for sensor time series, highlighting the need for preprocessing and continual learning to address non-stationary data and catastrophic forgetting.
problem_and_motivation: Real-world time series data often exhibit non-stationary distributions, causing deep learning models to suffer from catastrophic forgetting. This limits the practical deployment of these models in dynamic environments where data distributions shift over time. A systematic review of techniques to address these challenges is needed to guide the development of more robust systems.
approach:
  - Surveys recent deep learning methods (MLP, RNN, LSTM, CNN, GNN) for sensor time series classification and forecasting.
  - Reviews advanced preprocessing techniques including EMD, wavelet transform, and data augmentation.
  - Examines continual learning strategies (regularization, replay, parameter isolation) to mitigate catastrophic forgetting.
  - Evaluates the performance and applicability of these methods across diverse sensor time series datasets.
  - Discusses limitations of current CL research, including a focus on classification over regression and scalability issues.
findings:
  - "num: LSTM achieved superior forecasting performance with 4.82% MAPE vs. 20.97% for ARIMA on traffic flow data."
  - "num: Attention and DCN models work best with wavelet and FFT preprocessing for wind prediction."
  - "num: MC-SGD reduced forgetting by nearly 29% compared to joint-task training for activity recognition."
  - "num: Bidirectional LSTM achieved 94.75% accuracy for classifying resting vs. working states using EEG data."
  - "num: ConvLSTM outperformed persistence, SVR, and LSTM models for SST prediction."
  - "num: 2D CNN was the most reliable model for structural damage detection from raw time series data."
  - "num: Preprocessing with EMD improved CNN validation accuracy from 94.22% to 99.73% for gesture classification."
key_figures_tables:
  - "Table 1: Summary of DL techniques for sensor time series → Shows a wide variety of models and their applications."
  - "Table 2: Advanced preprocessing for DL applications → Demonstrates that preprocessing can significantly boost performance."
  - "Table 3: Continual learning techniques for time series → Highlights CL as a solution for non-stationary data."
  - "Figure 1: Tree diagram of DL methods for sensor time series → Provides a taxonomy of key DL architectures."
  - "Figure 2: Tree diagram of popular preprocessing methods → Categorizes techniques like EMD and wavelet transform."
  - "Figure 3: Taxonomy of continual learning methods → Groups CL strategies into regularization, replay, and isolation."
key_equations:
  - equation: "E(y_t) = E(y_{t-1}) = μ, Var(y_t) = σ^2 < ∞, Cov(y_t, y_{t-k}) = γ(k)"
    explanation: "Definition of weak stationarity for a time series."
  - equation: "L_i = (1/N_i) Σ_{r=1}^{N_i} L(y_{i,r}, ŷ_{i,r}; θ_i) + (q/( (i-1)N )) Σ_{j=1}^{i-1} Σ_{r=1}^{N_j} L( y_{j,r}, M(x̂_{j,r}; θ_i); θ_i )"
    explanation: "Continual learning objective combining current and previous task losses."
definitions:
  - term: "Continual Learning (CL)"
    definition: "A machine learning paradigm to handle non-stationary data by learning sequentially without forgetting."
  - term: "Catastrophic Forgetting (CF)"
    definition: "The abrupt loss of previously learned knowledge when a neural network is trained on new data."
  - term: "Non-stationary Time Series"
    definition: "A time series whose statistical properties, like mean and variance, change over time."
  - term: "Empirical Mode Decomposition (EMD)"
    definition: "A preprocessing technique that decomposes a signal into intrinsic mode functions (IMFs)."
critical_citations:
  - "[Kirkpatrick et al., 2017] — Introduced Elastic Weight Consolidation (EWC) to overcome catastrophic forgetting."
  - "[Hochreiter & Schmidhuber, 1997] — Developed the LSTM architecture to handle long-term dependencies."
  - "[LeCun et al., 2015] — Provided a foundational overview of deep learning and its capabilities."
  - "[De Lange et al., 2022] — Offered a comprehensive survey on continual learning for classification."
relevance:
  topics:
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Provides a general overview of DL/CL applications but not specific PFMS."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Directly discusses limitations of DL (forgetting, non-stationarity) and gaps in CL research."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "contextual"
      justification: "Focuses on technical modeling rather than financial behavior itself."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "low"
      justification: "CL addresses dynamic data, but not explicitly user profile cold-start."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Reviews many forecasting models (LSTM, CNN, etc.) directly applicable to spending prediction."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Evaluates algorithms (LSTM, GRU, etc.) for time series forecasting tasks."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews DL and CL methods for anomaly detection in time series."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "medium"
      justification: "Discusses specific algorithms like Graph Deviation Networks and VAE for anomaly detection."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "contextual"
      justification: "Mentions resource constraints for embedded/mobile sensing, informing design trade-offs."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides evaluation approaches for DL and CL models, including accuracy and forgetting metrics."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Empirically compares different DL and CL algorithms on various tasks and datasets."
  contribution: "This paper provides a foundational review of deep learning and continual learning techniques for time series modeling. It informs Odin's forecasting module by comparing the performance of various models like LSTM and CNN. The review of continual learning is crucial for Odin's anomaly detection and personalization, as it highlights methods to adapt to changing user behavior. The discussion of preprocessing techniques is relevant for ensuring data quality in Odin's expense categorization pipeline. Finally, the analysis of mobile and embedded sensing constraints can guide Odin's mobile-first design choices."
  directly_justifies:
    - "LSTM networks are a strong choice for sequential spending forecasting due to their superior performance over ARIMA."
    - "Continual learning is necessary to prevent catastrophic forgetting when adapting to a user's evolving financial patterns."
    - "Advanced preprocessing, like wavelet transforms and EMD, can significantly improve the accuracy of DL models on time series data."
    - "Replay-based continual learning methods are effective for mobile/embedded devices, balancing performance and resource use."
    - "Graph neural networks can be used for anomaly detection by modeling relationships between different spending categories."
  limits:
    - "The survey focuses on sensor time series, which may not perfectly replicate the noise and patterns of financial transaction data."
    - "Most reviewed CL methods are evaluated on classification tasks, with less focus on regression problems like spending prediction [unacknowledged]."
    - "The paper does not address the unique challenges of personal finance data, such as user privacy and sparse, irregular transactions [unacknowledged]."
    - "Specific guidance on integrating CL with constraint-based budget optimization is not provided [unacknowledged]."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains most directly relevant were 'Spending Forecasting' (6.A, 6.B) and 'Anomaly Detection' (8.A, 8.B) due to the paper's central focus on time series modeling techniques. 'System Evaluation' (12.A, 12.B) was also relevant as the paper compares different algorithms. 'Behavioral Profiling' (5.A) and 'Existing Systems' (4.A, 4.B) were assessed as medium or contextual because the paper discusses model limitations but not financial behavior or systems specifically. Domains like 'Filipino Cultural Context' (2.A-D), 'Savings & Debt Management' (13.A-C), and 'User Retention' (11.A-B) were considered and rejected as the paper provides no direct claims or evidence for these areas. The overall relevance is high for Odin's technical modules (forecasting, anomaly detection) but contextual for its domain-specific aspects, as the paper is a general methodology review."
limitations:
  - "The survey focuses on sensor time series, which may not perfectly replicate the noise and patterns of financial transaction data."
  - "Most reviewed CL methods are evaluated on classification tasks, with less focus on regression problems like spending prediction. [unacknowledged]"
  - "The paper does not address the unique challenges of personal finance data, such as user privacy and sparse, irregular transactions. [unacknowledged]"
  - "Specific guidance on integrating CL with constraint-based budget optimization is not provided. [unacknowledged]"
remember_this:
  - "Continual learning is essential for adapting to non-stationary time series data."
  - "LSTM and CNN are strong baselines for time series forecasting tasks."
  - "Preprocessing can significantly enhance deep learning model performance, with up to 99.73% accuracy."
  - "Deep learning models without CL suffer from catastrophic forgetting in dynamic environments."
  - "Replay-based CL methods balance performance and resource constraints for mobile deployment."
```
---

## Paper 3: Xiang et al_summarized.md

**Source File:** `Xiang et al_summarized.md`

```yaml
paper_id: 10.3390/app13116515
designation: international
title: Concept Drift Adaptation Methods under the Deep Learning Framework: A Literature Review
authors: Xiang, Q.; Zi, L.; Cong, X.; Wang, Y.
year: 2023
venue: Applied Sciences
odin_topics:
  - 4.B
  - 5.B
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 12.A
tldr: A literature review that systematically categorizes concept drift adaptation methods within the deep learning framework, covering discriminative, generative, hybrid, and other learning approaches for dynamic data streams.
problem_and_motivation: Deep learning models degrade when data distributions change due to concept drift, particularly in dynamic environments like epidemics and big data. Existing surveys lack a focused review of adaptation methods specifically under the deep learning framework. This gap hinders decision-makers from effectively utilizing deep learning for timely and accurate predictions amidst evolving data streams.
approach:
  - The paper provides a formal definition of concept drift, distinguishing between real, virtual, and hybrid drift, and outlines their causes.
  - It establishes a general process for concept drift adaptation, explaining update modes (parameter vs. structure) and detection modes (active vs. passive).
  - A taxonomy is built to classify adaptation methods into discriminative learning, generative learning, hybrid learning, and other deep learning paradigms.
  - For each category, the review details representative algorithms, their specific update/detection modes, the types of drift they address, and their application domains.
  - The paper summarizes common datasets and evaluation metrics used for benchmarking, and concludes with a discussion of current challenges and future research directions.
findings:
  - Discriminative learning-based methods, particularly MLPs and RNNs, are the most widely used for handling concept drift in streaming data.
  - Active detection combined with parameter updates is the most common strategy for adapting deep learning models to concept drift.
  - Hybrid models, especially LSTM combined with other architectures, are prevalent for capturing long-term dependencies and adapting to drifts in time-series data.
  - Deep reinforcement learning and deep transfer learning are emerging areas for adapting to concept drift in complex, non-stationary environments.
  - num: The review analyzes over 40 different algorithms, highlighting that abrupt drift is the most frequently addressed type, while recurring drift receives the least attention.
key_figures_tables:
  - Figure 1: Visualization of causes for virtual, real, and hybrid concept drift → Illustrates how data distribution changes affect the decision boundary.
  - Figure 2: Types of concept drift over time → Shows abrupt, incremental, gradual, and recurring drift patterns.
  - Figure 3: General process of concept drift adaptation under deep learning → Outlines the steps from data input to model update.
  - Figure 4: A taxonomy of concept drift adaptation methods → Categorizes methods into discriminative, generative, hybrid, and other deep learning techniques.
  - Table 1: Summary of discriminative learning-based methods → Provides an overview of algorithms, detection modes, update modes, adaptation drift types, and limitations.
  - Table 2: Summary of generative learning-based methods → Details methods using autoencoders, GANs, RBMs, and SOMs for drift adaptation.
  - Table 3: Summary of hybrid learning-based methods → Highlights combined models like LSTM+CNN and their characteristics.
  - Table 4: Summary of other concept drift adaptation methods → Covers deep transfer learning and deep reinforcement learning approaches.
key_equations:
  - equation: $P_{t0}(x,y) \neq P_{t1}(x,y)$
    explanation: Formal definition of concept drift as a change in joint probability distribution over time.
  - equation: $P(y|x) = \frac{P(y) * P(x|y)}{P(x)}$
    explanation: Bayes theorem showing how real concept drift can be indirectly caused by changes in prior or likelihood.
  - equation: $T(v_o, v_r, n_o, n_r) = \frac{|v_o/n_o - v_r/n_r| - 0.5 \times (1/n_o + 1/n_r)}{\sqrt{\mu + (1-\mu) \times (1/n_o + 1/n_r)}}$
    explanation: Statistical test used in STEPD to compare accuracies between two windows for drift detection.
  - equation: $MCC = \frac{TP \times TN - FP \times FN}{\sqrt{(TP+FP)(TP+FN)(TN+FP)(TN+FN)}}$
    explanation: Matthews correlation coefficient, a balanced measure for classification performance on imbalanced data.
definitions:
  - term: Concept Drift
    definition: The change in the underlying data stream distribution over time, which can degrade the performance of a predictive model.
  - term: Real Concept Drift
    definition: A change in the conditional probability P(y|x), which directly affects the decision boundary and model predictions.
  - term: Virtual Concept Drift
    definition: A change in the distribution of input features P(x) without affecting the decision boundary P(y|x).
  - term: Parameter Update
    definition: Updating the weights of a deep learning model to adapt to new data without changing its architecture.
  - term: Structural Update
    definition: Modifying the architecture of a deep learning model, such as by adding or removing nodes or layers.
  - term: Active Detection
    definition: A mode where a separate algorithm is used to explicitly detect concept drift before triggering a model update.
  - term: Passive Detection
    definition: A mode where the model is continuously updated in response to incoming data without an explicit drift detection step.
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network variant designed to handle long-term dependencies in sequence data.
  - term: GAN
    definition: Generative Adversarial Network, a deep learning framework for generating new data instances that resemble the training data.
  - term: DRL
    definition: Deep Reinforcement Learning, which combines deep learning's perceptual abilities with reinforcement learning's decision-making capabilities.
critical_citations:
  - "[Schlimmer and Granger, 1986] — First proposed the concept of concept drift in machine learning."
  - "[Gama et al., 2014] — A comprehensive survey on concept drift adaptation covering four key aspects."
  - "[Lu et al., 2018] — A broad review on learning under concept drift, covering multiple dimensions like drift type and imbalance."
  - "[Webb et al., 2016] — Characterizes concept drift and provides a framework for analyzing its different types."
relevance:
  topics:
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly addresses the limitation of deep learning models degrading under concept drift, a key gap in PFMS.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: medium
      justification: Discusses the challenge of adapting to recurring drift, which parallels the cold-start problem and the need for dynamic user profiles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: The entire paper is a review of predictive modeling techniques (deep learning) that are essential for forecasting in PFMS.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Reviews RNNs and LSTMs, which are core algorithms for forecasting sequential financial data like spending.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Covers concept drift adaptation methods specifically applied to anomaly detection, a core function for identifying fraudulent or unusual transactions.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Reviews algorithms like I-LSTM, MemStream, and ARCUS that are directly applicable to anomaly detection in data streams.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Summarizes evaluation metrics (accuracy, MCC, RMSE) and datasets (KDD Cup, Electricity) that can be used to benchmark PFMS modules.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides a general landscape of concept drift adaptation methods, which is foundational to understanding potential integrations into PFMS.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: low
      justification: No direct mention of handling infeasible recommendations, a key aspect of budget allocation.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Mentions federated learning (FedHAR) as a method that can handle concept drift while preserving privacy, but this is not a primary focus.
  contribution: This review paper contributes a comprehensive taxonomy of concept drift adaptation methods under the deep learning framework. Its categorization into discriminative, generative, hybrid, and other learning approaches provides a clear structure for understanding the landscape of available techniques. For Odin, this is crucial as it helps us identify state-of-the-art deep learning algorithms for key modules. Specifically, it guides our selection of RNNs/LSTMs for the spending forecasting module and GANs/autoencoders for the anomaly detection module. Furthermore, its detailed discussion of update and detection modes informs the design of our online learning strategy for adapting to new user spending patterns in real-time.
  directly_justifies:
    - "Deep learning models are susceptible to performance degradation when concept drift occurs."
    - "Active detection methods can provide decision-makers with knowledge of dynamic concept changes."
    - "Parameter updates, such as adjusting weights, are a common and efficient way to adapt to abrupt concept drift."
    - "LSTM-based methods are suitable for processing and forecasting events with relatively long intervals in time series."
    - "Hybrid learning models that combine LSTM and CNN are effective for capturing spatial and temporal features in data."
  limits:
    - "The review does not provide an empirical comparison of the performance of different concept drift adaptation methods."
    - "The effectiveness of many algorithms is demonstrated on specific datasets, and their generalizability to diverse financial data is not fully explored. [unacknowledged]"
    - "The review focuses on deep learning methods and does not compare them against traditional machine learning approaches for concept drift."
    - "Specific guidance on implementing these complex deep learning models in a mobile-first application like Odin is not provided. [unacknowledged]"
    - "The review does not address the unique challenges of applying these algorithms to noisy, sparse, or class-imbalanced personal financial data, which is a common reality in PFMS. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed for this paper. Domains flagged as relevant were: Predictive Modeling, Anomaly Detection, and System Evaluation. For the Predictive Modeling domain (6.A, 6.B), relevance was high, as the paper is a review of deep learning forecasting algorithms (RNNs, LSTMs) which are directly applicable to spending prediction. For Anomaly Detection (8.A, 8.B), relevance was high, given the paper's specific coverage of anomaly detection methods (I-LSTM, ARCUS, MemStream) that adapt to concept drift. For System Evaluation (12.A), relevance was medium because it summarizes metrics and datasets that can be used for testing. The topic 'Limitations and Gaps in Existing Systems' (4.B) was assigned high relevance as the paper explicitly frames the problem of model degradation as a key limitation. 'Profile Dynamics' (5.B) was considered a medium relevance case because the concept of recurring drift relates to the challenge of maintaining accurate user profiles over time. Domains rejected included those focused on Filipino cultural context (2.A, 2.B, 2.C, 2.D), Expense Categorization (3.A, 3.B, 3.C), Budget Recommendation (7.A, 7.B, 7.C, 7.D), Mobile-First Design (9.A, 9.B), User Retention (11.A, 11.B), and Savings & Debt Management (13.A, 13.B, 13.C), as the paper does not provide direct, citeable claims for these specific areas. The concept of 'cold-start' (5.B) was considered but rejected as the paper's discussion of recurring drift is a related but separate challenge. Overall, the paper provides a strong, high-level justification for incorporating advanced deep learning techniques into Odin's predictive and anomaly detection modules to ensure their robustness over time."
limitations:
  - "The review lacks an empirical comparison of the discussed algorithms, making it difficult to select the most effective method for a specific task."
  - "The surveyed methods are not evaluated on personal finance data, limiting the direct transferability of the findings to Odin's context. [unacknowledged]"
  - "The computational cost and resource requirements of many deep learning methods, especially hybrid models, are a significant limitation for mobile deployment. [unacknowledged]"
  - "The review does not address the challenge of dealing with sparse or missing data, which is common in real-world financial datasets. [unacknowledged]"
  - "Some algorithms discussed (e.g., DCA-DNN) suffer from model update latency, which could be critical for real-time applications like fraud detection."
remember_this:
  - "Concept drift causes deep learning models to produce poor predictions as data distributions change."
  - "Active detection methods can identify and explain concept drift, aiding in better decision-making."
  - "LSTM-based methods are crucial for forecasting sequential spending data in personal finance."
  - "Num: The review finds that abrupt drift is the most frequently addressed type in the literature."
  - "Autoencoders and GANs are powerful generative models for unsupervised anomaly detection in dynamic data streams."
```
---

## Paper 4: Koskelainen et al_summarized.md

**Source File:** `Koskelainen et al_summarized.md`

```yaml
paper_id: 10.1111/joca.12510
designation: international
title: Financial literacy in the digital age — A research agenda
authors: Koskelainen, T.; Kalmi, P.; Scornavacca, E.; Vartiainen, T.
year: 2023
venue: Journal of Consumer Affairs
odin_topics:
  - 1.B
  - 1.C
  - 3.A
  - 4.A
  - 5.A
  - 7.A
  - 9.B
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 12.A
tldr: Digitalization transforms financial services and personal money management, requiring a redefinition of financial literacy to include digital competencies, new behavioral risks, and novel interventions.
problem_and_motivation: Traditional financial literacy frameworks, developed for an analog world, are inadequate in the current complex digital financial landscape. The pervasive diffusion of digital financial services (DFS) creates both opportunities and new risks that users must navigate. There is a critical gap in understanding how digitalization affects financial literacy and capability.
approach:
  - Used an integrative literature review methodology following Torraco (2005).
  - Systematic search conducted in ProQuest, EBSCO, ACM Digital Library, and Google Scholar during fall 2020.
  - Applied a two-stage selection process, starting with 603 papers and narrowing to 29 peer-reviewed papers.
  - Adopted a concept-centric approach for analysis, categorizing papers into three themes: Fintech, Financial behavior in digital environments, and Behavioral interventions.
  - Analyzed papers from finance, economics, and information systems disciplines.
findings:
  - Digital financial literacy requires updating financial literacy curricula with new skills like cybersecurity awareness and understanding of algorithmic influence.
  - Digital nudging can both help (e.g., via smartphone apps for tracking spending) and potentially harm (e.g., via persuasive design for sales) consumer financial outcomes.
  - Loss of tangibility in digital payments tends to increase spending, as evidenced by literature starting from the 1980s.
  - Older, lower-income, and disabled consumers are less likely to use mobile payment apps, risking digital exclusion.
  - The use of digital financial management services makes consumers less aware of their spending.
key_figures_tables:
  - Figure 1: Conceptual description of financial literacy and capability → Foundation for the paper's proposed digital framework.
  - Figure 2: Conceptual description of digital financial literacy and capability → Illustrates how digitalization affects all elements of financial literacy.
  - Table 1: Research on digital financial literacy → Categorizes literature into Fintech, financial behavior, and behavioral interventions.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Fintech
    definition: Technologically enabled financial innovation resulting in new business models, applications, processes, or products.
  - term: Digital Financial Literacy
    definition: The knowledge, skills, and awareness needed to use digital financial services and understand their risks and benefits.
  - term: Financial Capability
    definition: Broader concept than financial literacy, including the ability and opportunity to act and gain access to financial products.
  - term: Digital Nudging
    definition: Influencing choices through algorithms and user-interface design in digital environments.
critical_citations:
  - "[Lusardi & Mitchell, 2014] — Foundational work on financial literacy measurement and economic importance."
  - "[Thaler & Sunstein, 2008] — Introduced the concept of nudging, central to the behavioral interventions theme."
  - "[Gomber et al., 2017] — Key paper on digital finance and Fintech research directions."
  - "[OECD, 2018] — Provides policy guidance on digitalisation and financial literacy."
  - "[Huston, 2010] — Seminal paper on measuring financial literacy."
relevance:
  topics:
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: contextual
      justification: Discusses how digitalization changes access and structure of financial services.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Directly addresses how digital environments alter financial behaviors like spending.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: low
      justification: Mentions personal finance apps for account management, implying categorization.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews Fintech and mobile banking apps, providing a landscape overview.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: Discusses behavioral economics and psychological biases influencing financial decisions.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Highlights digital tools and nudges that can assist in budgeting and keeping track of finances.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Reviews research on mobile banking usage, noting that design can influence engagement and financial decisions.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Extensively discusses risks including data confidentiality, digital profiling, and cybersecurity threats.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Highlights how use, perceived security, and ethical issues relate to user trust in digital financial services.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Discusses how digital nudging and app features can influence user engagement and behavior.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: Explores how tools like smartphone apps and text messages can be used for sustained behavioral change.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: low
      justification: Critiques of nudging suggest a need for evaluating outcomes and ethical frameworks.
  contribution: "This review paper provides a foundational framework for understanding digital financial literacy, which is essential for designing the educational and behavioral components of Odin. It directly informs the need for a 'digital' component in Odin's behavioral profiling, as traditional financial literacy metrics are insufficient in a digital-first app. The paper's analysis of Fintech and digital behaviors provides the context for Odin's core functionalities, such as expense tracking, budgeting, and anomaly detection, by outlining the new risks and opportunities in the digital financial landscape. Its discussion of digital nudging and behavioral interventions offers a theoretical basis for Odin's user engagement and retention strategies. The explicit call for updated measurement frameworks for digital financial literacy justifies Odin's approach to classifying user financial behavior based on digital interactions rather than solely on static knowledge tests."
  directly_justifies:
    - "Traditional financial literacy measures are insufficient for a digital world, necessitating new approaches to user profiling."
    - "Digitalization changes the financial behavior of young professionals, making them less aware of spending."
    - "Data privacy and security are primary concerns in personal finance apps, requiring robust design."
    - "Digital nudging can be used to improve financial behavior and should be incorporated into app design."
  limits:
    - "The paper is a literature review and does not present new empirical data on digital financial literacy interventions."
    - "Focuses on papers from finance, economics, and information systems, potentially missing relevant HCI or design literature."
    - "Provides high-level themes but not specific algorithmic or implementation details for a PFMS."
  mapping_rationale: "All 12 functional domains were systematically scanned against the paper's content. The paper was flagged as highly relevant to Data Privacy & User Trust (10.A, 10.B) due to its extensive discussion of risks like data profiling and fraud. It was also deemed highly relevant to User Retention & Engagement (11.A, 11.B) because of its detailed exploration of behavioral interventions and digital nudging. Medium relevance was assigned to Expense Categorization (3.A, as part of PFMS landscape), Existing Systems (4.A, providing a landscape of Fintech), Behavioral Profiling (5.A, discussing behavioral economics), Budget Recommendation (7.A, mentioning tools for saving and budgeting), and Mobile-First Design (9.B, reviewing mobile banking usage). The domains of Forecasting (6.A, 6.B) and Anomaly Detection (8.A-C) were rejected as the paper does not discuss predictive algorithms. The Savings & Debt Management domains (13.A-C) were considered contextual due to mentions of over-indebtedness and saving, but the paper does not provide specific management strategies. Overall, the paper provides a broad contextual and motivational framework for Odin, justifying the need for a comprehensive, digitally-aware PFMS that addresses user behavior, trust, and engagement."
limitations:
  - "The literature review is limited to papers published only in finance, economics, and information systems. [unacknowledged]"
  - "Excluding conference proceedings may have led to missing new technological developments. [acknowledged]"
  - "The sample is from 2020, and the digital finance landscape changes rapidly, so some findings may be less current. [unacknowledged]"
remember_this:
  - "Digital payments reduce spending tangibility and can increase consumption."
  - "Fintech innovations introduce new risks like data profiling and fraud."
  - "Digital nudging can improve financial behaviors but raises ethical concerns."
  - "80% of millennial smartphone owners use their device for transactional financial purposes."
  - "Financial literacy measurement must evolve to include digital competencies."
```
---

## Paper 5: George et al_summarized.md

**Source File:** `George et al_summarized.md`

```yaml
paper_id: "10.63125/913ksy63"
designation: "international"
title: "Machine Learning for Fraud Detection in Digital Banking: A Systematic Literature Review"
authors: "George, M.Z.H.; Alam, M.K.; Hasan, M.T."
year: 2023
venue: "ASRC Procedia: Global Perspectives in Science and Scholarship"
odin_topics:
  - "8.A"
  - "8.B"
  - "8.C"
  - "10.A"
  - "10.B"
  - "12.A"
  - "12.B"
  - "12.C"
tldr: "A systematic review of 118 studies on machine learning for fraud detection in digital banking reveals dominance of supervised learning, rising deep learning and hybrid models, and importance of evaluation metrics and interpretability, with cross-regional regulatory differences shaping adoption."
problem_and_motivation: "Fraud detection literature in digital banking is fragmented across methods, regions, and regulatory contexts, lacking a consolidated synthesis that integrates supervised, unsupervised, deep learning, and hybrid approaches. A comprehensive review is needed to identify methodological gaps, deployment challenges, and cross-regional variations to guide both research and practice."
approach:
  - "Applied PRISMA guidelines for systematic review, searching Scopus, Web of Science, IEEE Xplore, ACM Digital Library, and ScienceDirect."
  - "Screened 2,346 initial records, applied inclusion/exclusion criteria, resulting in 118 peer-reviewed studies and institutional reports for final synthesis."
  - "Extracted data on algorithms, datasets, evaluation metrics, and regional contexts using structured coding sheets."
  - "Conducted thematic synthesis across supervised, unsupervised, deep learning, hybrid, and evaluation/interpretability categories."
  - "Performed cross-regional comparison of regulatory and infrastructural influences on fraud detection adoption."
findings:
  - "num: Supervised learning studies (36) accumulated over 9,200 citations, remaining the dominant paradigm."
  - "num: Unsupervised anomaly detection studies (27) received over 6,800 citations, increasingly valued for novel fraud patterns."
  - "num: Deep learning studies (21) garnered over 7,300 citations, demonstrating rapid emergence in transaction monitoring."
  - "num: Hybrid approach studies (19) accounted for over 5,600 citations, showing superior adaptability."
  - "num: Evaluation and interpretability studies (15) received over 4,500 citations, underscoring their centrality."
  - "Cross-regional analysis reveals PSD2/SCA in Europe, fintech-led innovation in North America, and infrastructure-dependent approaches in emerging economies."
  - "Methodological gaps include inconsistent handling of class imbalance, limited reproducibility, and insufficient robustness checks."
key_figures_tables:
  - "Figure 1: Digital Banking Fraud Detection Framework → shows integration of data, ML models, and alert systems."
  - "Figure 4: Fraud Detection Machine Learning Framework → contrasts supervised, unsupervised, and hybrid paradigms."
  - "Figure 6: Data Imbalance and Real-Time Processing Challenges → highlights SMOTE, cost-sensitive learning, and latency constraints."
  - "Figure 8: Global Fraud Detection Regulatory Framework → compares EU, North America, and emerging markets."
  - "Figure 11: PRISMA methodology flow diagram → illustrates systematic review screening process."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "PR-AUC"
    definition: "Precision-Recall Area Under the Curve, preferred for imbalanced classification."
  - term: "ROC-AUC"
    definition: "Receiver Operating Characteristic Area Under the Curve, commonly used but can mislead under skew."
  - term: "SHAP"
    definition: "SHapley Additive exPlanations, a framework for model interpretability."
  - term: "LIME"
    definition: "Local Interpretable Model-agnostic Explanations, another interpretability tool."
  - term: "SMOTE"
    definition: "Synthetic Minority Over-sampling Technique, used to address class imbalance."
  - term: "PSD2"
    definition: "Revised Payment Services Directive, EU regulation mandating strong authentication and open banking."
  - term: "GDPR"
    definition: "General Data Protection Regulation, EU privacy law affecting data processing and explainability."
  - term: "F1-score"
    definition: "Harmonic mean of precision and recall, balancing both metrics."
critical_citations:
  - "[Ngai et al., 2011] — early application of supervised learning in fraud detection."
  - "[Susto et al., 2018] — anomaly detection for imbalanced data."
  - "[Carcillo et al., 2021] — hybrid supervised-unsupervised approach."
  - "[Lundberg & Lee, 2017] — SHAP for model interpretability."
relevance:
  topics:
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Reviews anomaly detection methods including unsupervised and hybrid approaches for transactional data."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Covers supervised, unsupervised, deep learning, and hybrid algorithms applicable to spending anomalies."
    - code: "8.C"
      name: "Cold‑Start Baseline Strategies for Anomaly Detection"
      relevance: "high"
      justification: "Discusses imbalanced learning and evaluation metrics that inform baseline strategies."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "medium"
      justification: "Addresses GDPR/PSD2 and privacy constraints that shape feature engineering and data access."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "medium"
      justification: "Emphasizes interpretability and transparency as essential for user trust and regulatory compliance."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Provides detailed guidance on metrics (precision, recall, F1, PR-AUC) and cost-sensitive evaluation."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Discusses trade-offs between accuracy and interpretability, and the use of PR-AUC over ROC-AUC."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "high"
      justification: "Imbalanced learning and cost-sensitive evaluation are directly applicable to budget recommendation performance assessment."
  contribution: "The systematic review offers a comprehensive taxonomy of anomaly detection algorithms—supervised, unsupervised, and hybrid—that directly informs the design of Odin's anomaly detection module (8.A/8.B/8.C). Its detailed treatment of evaluation metrics (PR-AUC, F1, cost curves) and imbalanced learning strategies provides a foundation for evaluating Odin's algorithmic modules (12.B/12.C). The emphasis on interpretability via SHAP/LIME supports the need for explainable outputs in Odin's budget recommendation and anomaly alerts. Cross-regional regulatory insights (GDPR/PSD2) contextualize data privacy and trust considerations (10.A/10.B) for Odin's Philippine context, though direct applicability is limited."
  directly_justifies:
    - "Precision-recall AUC is more informative than ROC-AUC for imbalanced fraud datasets."
    - "Hybrid models combining supervised and unsupervised learning reduce false positives while improving recall."
    - "SHAP and LIME provide post-hoc interpretability essential for regulatory compliance."
    - "Real-time processing constraints require lightweight feature engineering and optimized models."
  limits:
    - "The review focuses on banking fraud, not personal spending anomaly detection; behavioral patterns differ."
    - "The regulatory context (GDPR/PSD2) is European, not directly applicable to Philippines."
    - "The paper does not address cold-start problems or user-defined constraints specific to PFMS."
    - "Findings are based on literature up to 2023, missing recent advances."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. Domains flagged as relevant include Anomaly Detection (codes 8.A, 8.B, 8.C) with high relevance due to the paper's extensive coverage of anomaly detection algorithms for transactional data; System Evaluation (12.A, 12.B, 12.C) with high relevance due to detailed discussion of evaluation metrics (PR-AUC, F1) and interpretability frameworks; and Data Privacy & User Trust (10.A, 10.B) with medium relevance due to regulatory and trust considerations. Borderline cases: the paper's discussion of behavioral patterns in fraud detection touches on 5.A but does not address financial behavioral profiles, so it was considered but rejected as contextual only. Domains such as Filipino Cultural Context, Expense Categorization, Spending Forecasting, Budget Recommendation, Mobile-First Design, and Savings/Debt Management were considered and rejected as they are not addressed. The paper's overall relevance to Odin is moderate, providing strong methodological guidance for anomaly detection and evaluation but limited direct applicability to personal finance management."
limitations:
  - "Limited reproducibility due to private datasets and opaque feature pipelines."
  - "Inconsistent handling of class imbalance across studies."
  - "Lack of standardized theoretical integration with criminological frameworks."
  - "Robustness to adversarial manipulation and concept drift is insufficiently assessed."
  - "The review does not address cold-start baseline strategies for anomaly detection in new users [unacknowledged]."
remember_this:
  - "Supervised learning remains dominant with 36 studies and 9,200+ citations."
  - "Deep learning studies have surged, accumulating 7,300+ citations across 21 studies."
  - "PR-AUC is preferred over ROC-AUC for imbalanced fraud detection."
  - "Hybrid models outperform single methods by balancing precision and recall."
  - "Regulatory contexts (PSD2, GDPR) significantly shape model design and adoption."
```
---

## Paper 6: Shaikh et al_summarized.md

**Source File:** `Shaikh et al_summarized.md`

```yaml
paper_id: 6aebd210-1dcb-50c0-a1b1-9b3bcd54f3c6
designation: international
title: "Advances in mobile financial services: a review of the literature and future research directions"
authors: "Shaikh, A. A.; Alamoudi, H.; Alharthi, M.; Glavee-Geo, R."
year: 2023
venue: "International Journal of Bank Marketing"
odin_topics:
  - "1.A"
  - "2.A"
  - "4.A"
  - "4.B"
  - "5.A"
  - "5.C"
  - "9.A"
  - "10.A"
  - "10.B"
  - "11.A"
  - "11.B"
  - "12.A"
tldr: "A framework-based review of 115 MFS studies identifies three domains (mobile banking, payment, money) and proposes the TCMM framework to analyze theory, constructs, methods, and moderators."
problem_and_motivation: "Prior reviews of mobile financial services (MFS) are limited to specific domains like mobile banking or payments, lacking a holistic synthesis. A comprehensive framework is needed to organize the fragmented literature and guide future research across the entire MFS ecosystem."
approach:
  - "A structured literature review following Webster and Watson's (2002) three-step approach was conducted."
  - "Searches in five multidisciplinary databases (e.g., ScienceDirect, Web of Science) using 14 keywords identified 115 relevant journal articles from 2009–2020."
  - "The study introduces the Theory, Construct, Method, Moderator (TCMM) framework as an organizing model for synthesizing MFS research."
  - "Three major MFS domains were defined and delineated: mobile banking, mobile payments, and mobile money, each with distinct service characteristics and target segments."
  - "A 'Comprehensive framework of MFS domains' was developed, incorporating service, customer, demographic, and institutional dynamics."
findings:
  - "Perceived ease of use (or its equivalent) was the most frequently used construct, appearing in 81% of the reviewed studies."
  - "num: 90% of the studies used quantitative survey methods, while mixed methods were used in only 10%."
  - "num: The largest number of studies (14%) were conducted in China, followed by India (10%) and Taiwan (7%)."
  - "Trust was a significant construct in 59% of the studies, underscoring its importance in MFS adoption."
  - "Social influence was examined in 50% of the studies, indicating its role in shaping user behavior."
  - "The review identifies 14 distinct research themes for future MFS research, including AI-enabled services and the impact of COVID-19."
  - "Perceived risk was used as a construct in 37% of studies, typically showing a negative effect on adoption and use intention."
  - "Gender and age were the most frequently used demographic moderators in the reviewed literature."
  - "Mobile money is distinct for targeting unbanked populations, relying on agent networks, and facilitating high-volume, low-value transactions."
  - "The study proposes a segregation of mobile banking into financial and non-financial services."
key_figures_tables:
  - "Table 1: Summarizes differences between mobile banking, payment, and money → Provides a clear taxonomy for MFS domains."
  - "Table 5: Lists frequency of key constructs (e.g., PEOU, BI) used in 115 MFS studies → Highlights most critical variables."
  - "Figure 3: Shows distribution of MFS studies by country → Reveals research concentration in emerging markets."
  - "Figure 4: A comprehensive framework of MFS domains → Integrates service, customer, and institutional dynamics."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Mobile Financial Services (MFS)"
    definition: "An all-inclusive service portfolio for consumer segments accessing and using retail- and business-related banking and payment services on mobile devices."
  - term: "Mobile Banking"
    definition: "An innovative and cost-effective application of mobile commerce with extended capabilities, used virtually by bank account holders via web browser or downloadable app on smartphones or tablets."
  - term: "Mobile Payment"
    definition: "An anytime-anywhere payment mechanism offered by banking and non-banking entities, executed seamlessly in proximity or remote mode via handheld devices."
  - term: "Mobile Money"
    definition: "A financial inclusion tool used in developing countries by financially excluded communities to send and receive funds and make micropayments using a feature phone with SMS technology."
  - term: "TCMM Framework"
    definition: "An organizing framework proposed for MFS reviews, focusing on Theory, Constructs, Methods, and Moderators."
  - term: "FinTech"
    definition: "A non-banking entity that offers digital financial services, often acting as a disintermediation force."
  - term: "Unbanked"
    definition: "Adults who do not have a formal account at a financial institution or with a mobile money provider."
  - term: "De-banked"
    definition: "Consumers who refuse to access and use various alternative delivery channels despite their availability and refuse to maintain any formal relationship with a bank."
critical_citations:
  - "[Shaikh & Karjaluoto, 2015] — Foundational review of mobile banking adoption."
  - "[Baptista & Oliveira, 2015] — Examined cultural moderators in mobile banking acceptance."
  - "[Glavee-Geo et al., 2019] — Key empirical study on mobile money usage in Ghana."
  - "[Karjaluoto et al., 2019] — Examined perceived value drivers of MFS app use."
  - "[Venkatesh et al., 2003] — Originated UTAUT, widely used in MFS adoption studies."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "contextual"
      justification: "Mentions new demographic groups like Millennials and Gen Z as important future research areas."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "contextual"
      justification: "Discusses cultural moderators (e.g., collectivism) and regional differences in MFS adoption."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Provides a comprehensive taxonomy of MFS (banking, payment, money) and a framework of the service landscape."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Identifies limitations like the lack of studies on continuous use, agent-related fraud, and non-financial services."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "contextual"
      justification: "Discusses consumer segmentation (banked, unbanked, de-banked) and pre/post-adoption behavior."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "low"
      justification: "Mentions classification of consumers into domains based on choices and access but does not detail classification algorithms."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "medium"
      justification: "Conceptualizes MFS as mobile-first applications and distinguishes them from desktop/Internet banking."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "contextual"
      justification: "Discusses PSD2 and open banking, which raise data security and privacy challenges."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "high"
      justification: "Identifies trust as a key construct (59% of studies) affecting adoption and use of MFS."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "medium"
      justification: "Examines the shift from pre-adoption to post-adoption continuous use behavior."
    - code: "11.B"
      name: "Retention Mechanisms and Engagement Design"
      relevance: "medium"
      justification: "Highlights the need for strategies to ensure consumer sustained use of MFS for long-term relationship building."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "contextual"
      justification: "Presents TCMM as a new framework for evaluating and synthesizing MFS literature."
  contribution: "This review provides a foundational taxonomy for MFS, directly informing Odin's classification of financial data. The TCMM framework offers a structured approach for synthesizing literature that can be adapted for Odin's system evaluation. By identifying key behavioral constructs like trust and social influence, the paper guides the selection of critical variables for behavioral profiling. The proposed research directions, particularly on AI-enabled services and non-financial features, offer a roadmap for Odin's future feature development and research. The concept of segmenting users based on their financial relationship (banked/unbanked/de-banked) provides a preliminary basis for Odin's user classification."
  directly_justifies:
    - "Perceived usefulness and ease of use are primary drivers of behavioral intention to adopt MFS."
    - "Trust is a significant construct in the adoption and continuous use of mobile financial services."
    - "The long-term success of MFS depends on users' sustained use, not just initial adoption."
    - "Social influence affects consumer use intention and adoption of MFS."
    - "Research on continuous or sustained use of MFS is still limited."
  limits:
    - "The review excludes practitioner-oriented articles and non-survey studies (e.g., experiments), limiting the methodological scope of findings."
    - "The study does not include bibliometric or network analyses, which could provide additional insights into the field's structure."
    - "The TCMM framework's focus on quantitative survey studies may not fully capture qualitative or design-oriented research."
    - "The review does not provide a detailed analysis of specific forecasting or classification algorithms, which are central to Odin's core functions."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was conducted to assess the paper's relevance to Odin. The 'Existing Systems & Gaps' domain was flagged as highly relevant because the paper offers a comprehensive taxonomy of MFS and identifies research gaps. Within this domain, topic 4.A (Landscape) was assigned 'medium' as the paper provides a framework, and 4.B (Limitations) was 'medium' due to the explicit identification of research gaps. The 'Behavioral Profiling' domain (topics 5.A, 5.C) received 'low' and 'contextual' relevance, as while it discusses user segments and behavioral stages, it does not detail classification algorithms. Similarly, topics under 'Mobile-First Design' (9.A) and 'Data Privacy & User Trust' (10.B) were assigned 'medium' because the paper identifies mobile-first channels and highlights the critical role of trust, respectively. The 'User Retention' domain (11.A, 11.B) was marked 'medium' for identifying the importance of continuous use. Topics like 'Spending Forecasting' (6.A, 6.B) and 'Anomaly Detection' (8.A, 8.B) were considered and rejected as the paper is a broad review and does not cover specific algorithmic techniques for these areas. 'Budget Recommendation' topics were also rejected for the same reason. The overall relevance is moderate, as the paper provides a valuable overarching context and foundational concepts for Odin but lacks the technical depth needed to directly justify specific algorithms."
limitations:
  - "Only journal articles published between 2009–2020 were included; conference proceedings and recent publications (post-2020) are omitted."
  - "The review is heavily dominated by quantitative survey studies, potentially neglecting insights from qualitative or mixed-method research."
  - "The proposed TCMM framework is a literature organizing tool and is not empirically validated in this paper. [unacknowledged]"
  - "The future research agenda, while comprehensive, does not prioritize or offer specific design recommendations for algorithmic approaches. [unacknowledged]"
remember_this:
  - "MFS is segmented into mobile banking, payment, and money, each with distinct users and use cases."
  - "Perceived usefulness, ease of use, trust, and social influence are the most frequently studied constructs."
  - "Research has increasingly focused on MFS since 2017, with a shift towards downloadable apps and AI."
  - "The TCMM framework provides a structured way to analyze MFS literature across multiple dimensions."
  - "num: 90% of MFS adoption research relies on surveys, indicating a methodological gap in experimental studies."
```
---

## Paper 7: Cheng et al_summarized.md

**Source File:** `Cheng et al_summarized.md`

```yaml
paper_id: "10.3389/fpsyg.2023.1162916"
designation: "international"
title: "Influences of mental accounting on consumption decisions: asymmetric effect of a scarcity mindset"
authors: "Cheng, L.; Yu, Y.; Wang, Y.; Zheng, L."
year: 2023
venue: "Frontiers in Psychology"
odin_topics:
  - "1.C"
  - "3.B"
  - "5.A"
  - "5.B"
tldr: "Consumers prefer hedonic spending from windfall gains, but a high scarcity mindset diminishes this preference; hard-earned money consistently drives utilitarian spending."
problem_and_motivation: "The influence of mental accounting on hedonic versus utilitarian consumption is well-documented, yet the moderating role of a scarcity mindset remains unclear. Understanding this interaction is critical for predicting consumer choices under different income sources. Prior research has not systematically examined how perceived resource scarcity alters the mental accounting effect on spending preferences."
approach:
  - "Conducted two online between-subject experiments with student (N=319) and adult (N=294) samples."
  - "Manipulated mental account as windfall gains versus hard-earned money."
  - "Measured scarcity mindset using a three-item self-report scale (Pitesa and Thau, 2018)."
  - "Participants chose between hedonic (e.g., dinner at restaurant) and utilitarian (e.g., canteen card) products."
  - "Used chi-square tests to compare choice proportions and logistic regression to test moderation."
findings:
  - "Windfall gains significantly increased preference for hedonic over utilitarian consumption in both samples (student: χ²=33.45, p<0.001; adult: χ²=10.30, p=0.001)."
  - "num: Scarcity mindset moderated the windfall effect, reducing hedonic preference under high scarcity (student: B=-0.66, p=0.026; adult: B=-1.28, p<0.001)."
  - "No moderation was found for hard-earned money on hedonic vs utilitarian choice."
  - "Adults showed a stronger overall utilitarian preference, possibly due to larger windfall amounts and cultural thrift."
key_figures_tables:
  - "Figure 1: Bar charts of choice proportions by mental account and sample → Windfall boosts hedonic choice; hard-earned boosts utilitarian."
  - "Figure 2: Interaction plots of scarcity mindset and mental account → High scarcity reduces hedonic preference only for windfall gains."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Mental accounting"
    definition: "Cognitive operations that categorize and evaluate financial activities, treating money as nonfungible."
  - term: "Scarcity mindset"
    definition: "Belief that resources are limited, focusing attention on scarcity and influencing decisions."
  - term: "Hedonic consumption"
    definition: "Consumption aimed at pleasure and experiential enjoyment."
  - term: "Utilitarian consumption"
    definition: "Consumption aimed at functional, practical goals."
critical_citations:
  - "[Thaler, 1985] — foundational mental accounting theory."
  - "[Thaler, 1999] — formalized mental accounting framework."
  - "[Mani et al., 2013] — scarcity mindset impairs cognitive function."
  - "[Cheema and Soman, 2006] — malleable mental accounting."
relevance:
  topics:
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "contextual"
      justification: "General consumer behavior findings may inform understanding of Filipino spending patterns."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      relevance: "medium"
      justification: "Distinction between hedonic and utilitarian expenses is relevant for category design."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Directly examines how mental accounting and scarcity mindset shape spending preferences, key for profiling."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "medium"
      justification: "Shows that spending preferences vary with mindset, indicating dynamic profile factors useful for cold-start."
  contribution: "This paper informs Odin's user behavioral profiling module by demonstrating that mental accounting and scarcity mindset significantly influence spending choices. It supports the design of expense categorization that distinguishes hedonic from utilitarian purchases. The moderation effect suggests that Odin's recommendation algorithms should adapt to users' perceived scarcity levels. Additionally, the findings provide a basis for cold-start profiling by using income source and scarcity mindset as early indicators."
  directly_justifies:
    - "Windfall gains increase hedonic spending relative to utilitarian."
    - "Scarcity mindset reduces the tendency to spend windfalls on hedonic items."
    - "Hard-earned money is consistently allocated to utilitarian purchases, regardless of scarcity mindset."
  limits:
    - "The study uses self-reported scarcity mindset, not a direct manipulation."
    - "Samples are from China, limiting cultural generalizability to Filipinos."
    - "No field experiment to validate real-world spending behavior."
    - "Amount of windfall differs between student and adult samples, confounding comparisons. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains and associated topic codes identified three domains as relevant: Behavioral Profiling (5.A, 5.B), Expense Categorization (3.B), and Financial Behavior (1.C). The paper directly addresses how mental accounting and scarcity mindset affect spending choices, providing high relevance for 5.A and medium for 5.B and 3.B. The Filipino cultural context domains (2.A-D) were considered but rejected because the study was conducted in China and does not address Filipino-specific practices. Spending forecasting, budget recommendation, anomaly detection, mobile-first design, data privacy, retention, evaluation, and savings/debt domains were not directly informed by the paper's findings."
limitations:
  - "Self-reported scarcity mindset may not capture actual resource constraints."
  - "The experimental scenarios may not reflect real-world spending decisions."
  - "Cultural context (China) limits applicability to Philippine users. [unacknowledged]"
  - "The study does not examine long-term effects of scarcity mindset on budgeting behavior. [unacknowledged]"
remember_this:
  - "Windfall gains significantly boost hedonic spending over utilitarian."
  - "High scarcity mindset reduces hedonic preference for windfall money."
  - "Hard-earned money consistently favors utilitarian purchases."
  - "Adults show stronger utilitarian preference than students."
  - "Scarcity mindset moderates mental accounting effects with p<0.001."
```
---

## Paper 8: Zambrano et al_summarized.md

**Source File:** `Zambrano et al_summarized.md`

```yaml
paper_id: 10.1016/j.wds.2023.100081
designation: international
title: Rotating savings and credit associations: A scoping review
authors: Zambrano, A.F.; Giraldo, L.F.; Perdomo, M.T.; Hernández, I.D.; Godoy, J.M.
year: 2023
venue: World Development Sustainability
odin_topics:
  - 2.A
  - 13.A
  - 13.B
  - 5.A
  - 4.A
  - 4.B
  - 7.A
tldr: A scoping review of ROSCA research finds these informal savings groups provide financial access and social capital, and suggests design improvements like diversification and reputation systems.
problem_and_motivation: Informal financial cooperation, like ROSCAs, is vital for low-income communities, but a systematic synthesis of recent findings on their structure, benefits, and risks has been lacking to inform design and policy.
approach:
  - Conducted a scoping review using the PRISMA-ScR protocol on 96 peer-reviewed articles from 2000-2022.
  - Extracted data on study location, methodological approaches, and keywords for trend analysis.
  - Grouped findings into categories including origin, participants, benefits, risks, operation, and penalties.
  - Analyzed the co-occurrence of keywords to identify thematic connections within the literature.
  - Reviewed mathematical, computational, and technological applications for modeling and supporting ROSCAs.
findings:
  - Asia and Africa are the most studied continents for ROSCAs, with limited research in South America.
  - ROSCAs provide non-financial benefits like social capital, empowerment, and improved health for members.
  - Defection of members, driven by loss of motivation, is a primary risk factor for ROSCA failure.
  - Strategies like diversification (joining multiple ROSCAs) and smaller groups can increase resilience.
  - num: Multi-agent simulations and web applications are emerging to test improvements and support ROSCA operations.
key_figures_tables:
  - Figure 1: Continent of data collection → Asia and Africa are the most studied regions.
  - Figure 2: Country of data collection → Kenya, India, and Japan are frequently studied.
  - Figure 3: Published year and continent → An increasing trend in publications until 2019, with a recent decline.
  - Figure 4: Methodological approaches → Interviews and surveys are the most common methods.
  - Figure 6: Number of occurrences of most common keywords → ROSCA, Finance, and Social are the most frequent concepts.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: ROSCA
    definition: Rotating Savings and Credit Association, an informal group where members contribute periodically to a pot allocated to one member each cycle.
  - term: Bidding ROSCA
    definition: A type where the pot is allocated to members who bid the highest premium for early turns.
  - term: Fixed ROSCA
    definition: A type where the order of receiving the pot remains fixed across cycles.
  - term: Random ROSCA
    definition: A type where the order of receiving the pot is randomly determined each cycle.
critical_citations:
  - "[Anderson et al., 2009] — ROSCAs are unsustainable without external sanctions."
  - "[Besley et al., 1993] — Foundational economics of ROSCAs."
  - "[Geertz, 1962] — Early influential description of ROSCAs as development tools."
  - "[Levenson & Besley, 1996] — Key analysis of ROSCA participation determinants."
  - "[Sedai et al., 2021] — Links ROSCAs to women's empowerment in India."
relevance:
  topics:
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: ROSCAs are a quintessential example of culturally embedded financial practices studied globally.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: Directly analyzes ROSCAs as a mechanism for collective savings and achieving financial goals.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: Examines ROSCAs as an alternative to formal debt for financing needs.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Discusses member motivations like self-control and trust, which relate to behavioral profiles.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Maps the landscape of informal finance (ROSCAs) as an alternative to formal systems.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies gaps in formal finance that ROSCAs fill, and limitations of ROSCAs themselves.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: Provides background on savings strategies but does not detail algorithmic budgeting.
  contribution: This paper provides a comprehensive review of ROSCAs, offering validated domain knowledge for Odin's design. Its findings on savings discipline, social capital, and default risks directly inform the design of Odin's savings and social features. The review's emphasis on community trust and cultural specificity justifies Odin's focus on Filipino cultural practices. The identified strategies for increasing ROSCA resilience, such as diversification and reputation systems, can be adapted for Odin's recommendation and anomaly detection modules.
  directly_justifies:
    - "ROSCAs help members save money by imposing discipline and social pressure."
    - "Participation in ROSCAs provides non-financial benefits like social capital and empowerment."
    - "Defection and loss of motivation are primary risks that can be mitigated by reputation and economic penalties."
    - "Diversifying participation across multiple small groups reduces risk for members."
    - "Technological tools can improve transparency and security in informal savings groups."
  limits:
    - "Scoping review, not a meta-analysis; does not quantify effect sizes of strategies."
    - "The review excludes non-English literature, potentially missing regional insights."
    - "Focuses on ROSCAs, which are distinct from typical PFMS, limiting direct applicability."
    - "Proposed computational models are theoretical and not validated with real user data."
    - "Does not address the specific financial landscape or user behaviors of Filipino young professionals."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to domains of Culturally Specific Financial Practices (2.A) and Savings & Debt Management (13.A, 13.B) as it directly analyzes ROSCAs as informal financial tools used in various cultures. Medium relevance was assigned to Behavioral Profiling (5.A) and Existing Systems & Gaps (4.A, 4.B) due to its discussion of participant motivations, limitations of formal finance, and the role of social capital. Contextual relevance was noted for Budget Recommendation (7.A) as it provides domain knowledge but not algorithmic approaches. Other domains like Anomaly Detection (8.A, 8.B, 8.C) and Mobile-First Design (9.A, 9.B) were considered and rejected because the paper does not touch on these topics. Overall, the paper offers valuable background on informal savings behavior and community-based financial management, which can inform Odin's design by highlighting the importance of social features, trust, and culturally relevant savings mechanisms.
limitations:
  - "Limited to studies published in English."
  - "Data collection from real-world ROSCAs was restricted due to pandemic conditions after 2020."
  - "The review does not include a meta-analysis to quantify the effectiveness of strategies like diversification."
  - "Computational models and technological applications discussed are mostly theoretical and not tested at scale."
  - "Findings are synthesized from a broad global context, which may not be directly generalizable to the Philippines."
remember_this:
  - "ROSCAs provide both financial access and social capital to underprivileged communities."
  - "Discipline and social pressure are key mechanisms for successful savings in ROSCAs."
  - "Defection is a major risk, but diversification across groups can increase resilience."
  - "Non-financial benefits like empowerment and health are significant for members."
  - "num: 96 articles reviewed from 2000 to 2022 to synthesize ROSCA knowledge."
```
---

## Paper 9: Fei_summarized.md

**Source File:** `Fei_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international
title: Impact of Mental Representation on Consumer Behaviors: Implications for Mental Budgeting and Prediction Algorithm Preferences
authors: Fei, L.
year: 2023
venue: University of Chicago Booth School of Business
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 7.A
  - 7.D
  - 8.B
  - 12.A
tldr: Consumers represent expenditures in hierarchical taxonomies, and the taxonomic distance between items predicts spending adjustments when budgets deviate.
problem_and_motivation: Existing mental budgeting research assumes single-level categories, failing to capture how consumers naturally organize expenditures. Understanding this hierarchical representation is crucial for predicting spending adjustments and improving personal finance tools.
approach:
  - Recovered consumer expenditure taxonomies using a successive pile-sort method with 27 US participants.
  - Validated taxonomy consensus and stability across time using Cultural Consensus Model analysis.
  - Tested spending adjustment predictions using lab experiments with self-reported and consequential choices.
  - Analyzed over 7 million grocery shopping trips to examine real-world spending patterns in response to promotions.
  - Controlled for substitutability and complementarity to isolate the effect of taxonomic distance.
findings:
  - Consumers show consensus in their hierarchical representations of expenditures.
  - Taxonomic distance predicts spending adjustment: closer items are adjusted more than distant ones.
  - num: Spending adjustment increased by 0.5 units for each taxonomic level closer between items.
  - The taxonomy effect persists even when controlling for substitutability and complementarity.
  - num: Analysis of 7 million grocery trips shows consumers spend more on items when taxonomically close items are on sale.
  - People spontaneously recruit taxonomies for spending decisions without explicit category prompts.
key_figures_tables:
  - Figure 1.3: MDS plot shows clustered groups of expenditures → Reveals consensus in mental representation structure.
  - Figure 1.5: Bar chart of spending adjustment by taxonomic distance → Closer items show higher spending adjustment.
  - Figure 1.9: Regression coefficients for close vs. far focal items over years → Close items consistently drive higher spending.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: Taxonomic Distance
    definition: The level at which expenditures are categorized together in a consumer's hierarchy.
  - term: Cultural Consensus Model
    definition: A statistical framework to test agreement across individual mental representations.
critical_citations:
  - "[Thaler, 1985] — Foundation of mental accounting theory."
  - "[Heath and Soll, 1996] — Establishes mental budgeting with category-level adjustments."
  - "[Henderson and Peterson, 1992] — Preliminary evidence for hierarchical mental accounts."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Paper proposes hierarchical taxonomy for expenditure categorization.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: high
      justification: Provides empirical basis for designing multi-level spending categories.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Critiques single-level budgeting approaches as insufficient.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Highlights gap in capturing hierarchical mental accounts.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Taxonomy reflects individual spending patterns and profiles.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Directly tests and refines mental budgeting theory.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: medium
      justification: Hierarchical adjustment suggests structured reduction priorities.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Taxonomic context could inform anomaly baselines.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: contextual
      justification: Uses field data to evaluate taxonomy-based spending predictions.
  contribution: The paper provides a cognitive framework for understanding how consumers naturally categorize expenses, which can inform Odin's expense categorization engine by moving beyond flat category structures. It validates that taxonomic distance predicts real spending adjustments, offering a basis for Odin's budget recommendation module to model user behavior more accurately. The findings also support Odin's anomaly detection by providing a baseline for what constitutes typical spending relationships. Additionally, the paper demonstrates that consumers spontaneously recruit taxonomies, suggesting Odin can leverage implicit user structures without explicit input.
  directly_justifies:
    - Odin should implement a hierarchical expense categorization system based on taxonomic distance.
    - Budget recommendations should account for relative distance between expense items.
    - Spending adjustments follow predictable patterns tied to mental taxonomies.
    - Mobile UX can leverage hierarchical categories for intuitive budget tracking.
  limits:
    - Study population is US-based, limiting generalizability to Filipino young professionals.
    - Taxonomic recovery may vary across cultural contexts and financial literacy levels.
    - The field data focuses only on grocery purchases, not total spending.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes flagged several as relevant. The paper directly addresses expense categorization (3.A, 3.B) by proposing a hierarchical taxonomy, and critiques existing systems (4.A, 4.B) for their single-level assumptions. It supports behavioral profiling (5.A) by showing taxonomic consensus across consumers. The core contribution to budget recommendation (7.A) is high, as it tests and refines mental budgeting theory, with implications for infeasibility handling (7.D) through structured adjustment priorities. Anomaly detection (8.B) was considered low because the paper does not directly address detection algorithms, though taxonomic context could inform baselines. System evaluation (12.A) was deemed contextual due to the use of field data. Domains like Filipino cultural context (2.A-D), mobile-first design (9.A-B), data privacy (10.A-B), user retention (11.A-B), and savings/debt management (13.A-C) were rejected as they are not addressed. The paper overall provides foundational cognitive insights for Odin's expense management and budgeting modules.
limitations:
  - Taxonomic recovery may not capture all relevant spending categories for Filipino users. [unacknowledged]
  - Field data limited to grocery purchases, not validating total spending adjustments. [unacknowledged]
  - Spontaneous adjustment may be weaker when users are explicitly reminded of budgets.
remember_this:
  - Consumers mentally organize expenses in nested hierarchies, not just flat categories.
  - Spending adjustments are stronger for taxonomically closer items.
  - Hierarchical taxonomies predict real grocery spending based on promotions.
  - The taxonomy effect remains after controlling for substitutability and complementarity.
  - People spontaneously use taxonomies even without budget category prompts.
```
---

## Paper 10: Sinnewe & Nicholson_summarized.md

**Source File:** `Sinnewe & Nicholson_summarized.md`

```yaml
paper_id: "10.1111/joca.12512"
designation: "international"
title: "Healthy financial habits in young adults: An exploratory study of the relationship between subjective financial literacy, engagement with finances, and financial decision-making"
authors: "Sinnewe, E.; Nicholson, G."
year: 2023
venue: "Journal of Consumer Affairs"
odin_topics:
  - "1.C"
  - "5.A"
  - "7.A"
  - "11.A"
  - "13.A"
tldr: "Young adults' financial habits are more strongly influenced by social context and motivation than by subjective financial literacy, with romantic partnerships shifting focus to long-term goals and budgeting."
problem_and_motivation: "Financial education yields mixed results and fails to improve behavior consistently. Understanding how financial habits form during the transition to full-time work is critical, yet the roles of social context, motivation, and literacy remain unclear. This study addresses the gap by exploring the determinants of financial habits in young adults entering the workforce."
approach:
  - "Conducted 28 semi‑structured interviews with Australian university graduates aged 21–31 who had entered full‑time work within the last five years."
  - "Used grounded theory methodology with iterative open, axial, and selective coding by multiple coders."
  - "Applied Theory of Planned Behavior and Family Financial Socialization as theoretical lenses."
  - "Collected 16.1 hours of interview data, transcripts averaged 4,929 words each, totaling 252 pages."
  - "Coding involved constant comparison between data and theory, with debriefing sessions to mitigate researcher bias."
findings:
  - "num: 21 of 28 participants reported actively saving money."
  - "num: 10 of 28 used a formal budget; many others used bucket systems or expense tracking."
  - "num: 20 of 28 had investments in shares or property."
  - "Romantic partnerships were strongly associated with future‑oriented goals, formal budgeting, and strict bucket systems."
  - "Subjective financial literacy (mean self‑rating 6.4/10) did not predict daily financial engagement; motivation was the primary driver."
  - "Participants who experienced financial hardship exercised greater control over their finances."
  - "Parents served as primary financial role models; peers were rarely sources of advice."
  - "Debt avoidance (credit cards, buy‑now‑pay‑later) was a common perceived norm instilled by parents."
  - "num: Average financial satisfaction rating was 7.3 out of 10, with budgeting linked to higher satisfaction."
  - "Transition to work increased disposable income, often leading to more spending, but relationship status moderated this effect."
key_figures_tables:
  - "Table 1: Participant demographics and living situations → Sample is highly educated, mostly university graduates."
  - "Table 2: Major themes with occurrence counts → Socialization, attitudes, perceived norms, and habits form interconnected influences."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Financial habits"
    definition: "Patterns of action over time such as earning, saving, spending, and gifting; automated, cue‑prompted behaviors with minimal cognitive load."
  - term: "Subjective financial literacy"
    definition: "Self‑reported assessment of one's financial knowledge and confidence, as opposed to objective test scores."
  - term: "Theory of Planned Behavior (TPB)"
    definition: "Behavioral intention is predicted by attitude, perceived social norms, and perceived behavioral control."
  - term: "Family Financial Socialization (FFS)"
    definition: "Process of acquiring values, attitudes, norms, and behaviors that contribute to financial well‑being, primarily through family influences."
critical_citations:
  - "[Gudmunson & Danes, 2011] — Foundational framework for family financial socialization."
  - "[Ajzen & Fishbein, 2005] — Core theory of planned behavior underpinning motivation constructs."
  - "[Fernandes et al., 2014] — Meta‑analysis showing limited impact of financial education on behavior."
  - "[Mandell & Klein, 2009] — Evidence that financial literacy education does not improve financial behavior."
relevance:
  topics:
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Directly studies financial habits and decision‑making of young adults entering the workforce."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Provides behavioral profiles based on relationship status, motivation, and financial socialization."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "medium"
      justification: "Observes real‑world budgeting practices (formal budgets, bucket systems) used by young adults."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "high"
      justification: "Examines motivation and engagement with finances, showing that motivation outweighs literacy."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "high"
      justification: "Links relationship status and future orientation to explicit savings goals and goal setting."
  contribution: "This paper directly informs Odin's user profiling module by showing that relationship status and financial hardship experience are key behavioral drivers. It justifies a motivation‑first approach in engagement design, suggesting that budget recommendation should adapt to life‑stage changes. The findings support savings goal management features that leverage future‑oriented triggers, such as partnership milestones. Additionally, the emphasis on social context (parents, peers) guides the design of social features and norm‑based nudges. The evidence that subjective literacy does not drive daily engagement implies that Odin should focus on simplifying complex financial decisions rather than on literacy education."
  directly_justifies:
    - "Romantic partnerships significantly increase future‑oriented financial behavior and formal budgeting."
    - "Motivation, not financial literacy, is the primary driver of day‑to‑day financial engagement."
    - "Financial hardship experience enhances perceived control and leads to more disciplined saving."
    - "Parents are the dominant role model for financial norms and debt avoidance."
    - "Present‑biased individuals benefit more from automatic saving mechanisms than from education."
  limits:
    - "Sample is homogenous (university graduates), limiting generalizability to broader populations."
    - "Self‑selection bias may exclude individuals with poor financial habits or high debt."
    - "Self‑reported behavior may suffer from social desirability and recall bias."
    - "Qualitative design does not establish causality; findings are exploratory."
    - "Australian context may not directly transfer to Filipino cultural settings."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. Domains flagged as relevant include: Financial Behavior (1.C) due to direct focus on habits and spending patterns; Behavioral Profiling (5.A) for relationship‑based profiles and motivation drivers; Budgeting Strategies (7.A) for observed budgeting practices; Engagement Dynamics (11.A) for motivation and engagement; and Savings Goal Management (13.A) for future‑oriented savings. Relevance levels: high for 1.C, 5.A, 11.A, 13.A; medium for 7.A because it describes practices but does not propose new strategies. Borderline cases: 2.C (user‑declared preferences) was considered because money attitudes were reported, but these are not framed as user preferences for system design; rejected. 13.B (debt management) was considered but the paper focuses on avoidance rather than active management, so rejected. Domains like forecasting, anomaly detection, mobile design, privacy, and evaluation were not addressed and thus rejected. Overall, the paper provides strong behavioral insights relevant to user modeling, engagement, and savings features, though it is not directly algorithmic or Philippines‑specific."
limitations:
  - "Sample is homogenous (university graduates), limiting generalizability. [unacknowledged]"
  - "Self‑selection bias may exclude those with poor habits or high debt. [unacknowledged]"
  - "Self‑reported spending may be biased by social desirability. [unacknowledged]"
  - "Qualitative design prevents causal inference."
  - "Australian context may not generalize to Filipino young professionals."
remember_this:
  - "Romantic partnerships drive formal budgeting and long‑term savings goals."
  - "Motivation, not financial literacy, predicts daily financial engagement."
  - "Financial hardship experience increases financial control and saving discipline."
  - "Average financial satisfaction was 7.3 out of 10 among participants."
  - "Parents are the primary influence on financial norms and debt avoidance."
```
---

## Paper 11: Ma P. et al_summarized.md

**Source File:** `Ma P. et al_summarized.md`

```yaml
paper_id: 10.3390/en16155809
designation: international
title: Review of Family-Level Short-Term Load Forecasting and Its Application in Household Energy Management System
authors: "Ma, P.; Cui, S.; Chen, M.; Zhou, S.; Wang, K."
year: 2023
venue: Energies
odin_topics:
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 9.A
  - 12.A
  - 12.B
  - 12.C
  - 13.A
  - 13.B
tldr: Reviews deep learning and probabilistic methods for short-term household load forecasting, emphasizing their role in home energy management system scheduling and optimization.
problem_and_motivation: Individual household loads lack clear consistent patterns due to human behavior and weather variability, making system-level forecasting methods inadequate for household-level applications. Accurate short-term load forecasting is essential for effective home energy management and demand response, yet current approaches face challenges in accuracy, uncertainty quantification, and computational efficiency.
approach:
  - Surveys deep learning architectures including LSTM, CNN, and hybrid LSTM-CNN models for household load forecasting.
  - Reviews feature extraction techniques such as wavelet decomposition, PCA, and mutual information to improve prediction accuracy.
  - Examines adaptive learning methods including online learning and transfer learning for dynamic load pattern changes.
  - Discusses probabilistic forecasting methods using quantile regression and Bayesian deep learning to quantify uncertainty.
  - Explores bottom-up appliance-level forecasting and ultra-short-term (hourly) load prediction challenges.
  - Analyzes the integration of load forecasting with HEMS optimization and scheduling.
findings:
  - LSTM networks effectively capture long-term dependencies in sequential load data, outperforming traditional methods like ARIMA and SVR.
  - num: Hybrid LSTM-CNN models achieve 92.06% accuracy for small-range load prediction and reduce prediction time by 75%.
  - Probabilistic forecasting provides comprehensive uncertainty information essential for robust HEMS decision-making.
  - Bottom-up appliance-level forecasting improves accuracy over direct household-level prediction but faces efficiency challenges.
  - Adaptive online learning enables models to capture dynamic changes in consumption patterns, improving real-world performance.
  - Load prediction errors increase HEMS uncertainty and affect scheduling performance, requiring efficient forecasting modules.
key_figures_tables:
  - Figure 1: LSTM block structure and unrolled sequential architecture → illustrates memory cell and gate mechanisms.
  - Figure 2: LSTM-based load forecasting framework → shows workflow from input to prediction.
  - Figure 3: Weekly consumption load of a clothes washer → demonstrates appliance load variability across days.
  - Figure 4: Forecasting framework with preprocessing and feature extraction → highlights DWT and CRT for feature engineering.
  - Figure 5: Probabilistic and conditional probabilistic load forecasting frameworks → shows uncertainty quantification approach.
  - Figure 6: Appliance-level deep learning forecasting framework → illustrates bottom-up prediction architecture.
  - Figure 7: Load prediction results for different appliances → shows data-driven model performance on device-level peaks.
  - Figure 8: Home energy management system schematic → depicts HEMS components and data flow.
  - Table 1: Comparison of forecasting models → summarizes advantages and shortcomings of classical, LSTM, and CNN.
  - Table 2: Smart meter data segment → shows active power, reactive power, voltage, current, and total load samples.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: HEMS
    definition: Home Energy Management System; optimizes household energy use through scheduling and demand response.
  - term: STLF
    definition: Short-Term Load Forecasting; predicts electricity demand for time horizons from hours to days ahead.
  - term: LSTM
    definition: Long Short-Term Memory; recurrent neural network architecture for sequence learning with memory cells.
  - term: CNN
    definition: Convolutional Neural Network; deep learning model for feature extraction from spatial or temporal data.
  - term: NILM
    definition: Non-Intrusive Load Monitoring; disaggregates total household load into appliance-level consumption.
  - term: AMI
    definition: Advanced Metering Infrastructure; smart metering system for real-time energy data collection.
critical_citations:
  - "[Hochreiter and Schmidhuber, 1997] — foundational LSTM architecture for sequence learning."
  - "[Kong et al., 2023] — LSTM outperforms other ML algorithms for load prediction."
  - "[Zheng et al., 2019] — Kalman filter bottom-up approach outperforms LSTM in efficiency."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: "Comprehensive review of predictive models for household load forecasting."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: "Detailed analysis of LSTM, CNN, and hybrid algorithms for time-series load data."
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: "Discusses scheduling and optimization strategies informed by load forecasts."
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: "HEMS scheduling uses forecasts for cost optimization and demand response."
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: contextual
      justification: "Edge computing and real-time forecasting imply mobile-friendly system requirements."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: "Systematically evaluates forecasting models using accuracy metrics like R, MAE, and RMSE."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: "Compares performance of LSTM, CNN, ARIMA, SVR, and hybrid models."
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: "Discusses evaluation of forecasting accuracy and its impact on HEMS scheduling performance."
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: "HEMS optimization indirectly supports energy cost savings and efficiency."
    - code: 13.B
      name: Debt Management in PFMS
      relevance: low
      justification: "Load forecasting supports cost reduction but does not directly address debt."
  contribution: "This review paper directly informs Odin's forecasting module (Topic 6.A/6.B) by surveying state-of-the-art deep learning methods for time-series prediction. It supports the evaluation framework (Topic 12.A/12.B) by documenting accuracy metrics and comparative benchmarks. The discussion of HEMS scheduling (Topic 7.A/7.B) provides domain knowledge for budget recommendation systems. The analysis of adaptive learning and probabilistic forecasting offers insights for handling uncertainty and cold-start scenarios (Topic 8.C/6.A). The bottom-up forecasting framework (Topic 4.A/4.B) provides a methodological foundation for appliance-level prediction in personal finance applications."
  directly_justifies:
    - "LSTM networks are effective for load prediction due to memory units and forget gates."
    - "Probabilistic forecasting quantifies uncertainty essential for robust optimization in HEMS."
    - "Hybrid LSTM-CNN models improve accuracy by capturing both local and long-term patterns."
    - "Bottom-up appliance-level forecasting significantly reduces prediction errors compared to direct household-level forecasting."
    - "Adaptive online learning enables models to dynamically adjust to changing consumption patterns."
  limits:
    - "Review paper does not present original experimental validation or novel algorithm contributions."
    - "Focus on electricity load forecasting, not directly on personal finance spending data."
    - "Discussion of HEMS scheduling does not address user-defined budget constraints or allocation optimization."
    - "No specific analysis of Philippine or Southeast Asian consumption patterns."
    - "Limited treatment of mobile-first design and user experience considerations."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to Spending Forecasting (Domain 6) and System Evaluation (Domain 12) because it comprehensively reviews prediction algorithms (6.A, 6.B) and evaluation methodologies (12.A, 12.B, 12.C). Medium relevance was assigned to Budget Recommendation (Domain 7) due to the HEMS scheduling and optimization discussion, and to Mobile-First Design (Domain 9) for edge computing implications. Low relevance was noted for Savings & Debt Management (Domain 13) as energy cost reduction is a secondary benefit. Borderline cases included the overlap between 6.B (algorithmic forecasting) and 12.B (algorithm evaluation) which were both selected as high relevance. Domains such as Filipino Cultural Context (2), Expense Categorization (3), Behavioral Profiling (5), Anomaly Detection (8), Data Privacy (10), and User Retention (11) were considered and rejected as the paper does not address behavioral patterns, spending categories, privacy, or engagement. Overall, this paper provides strong foundational knowledge for forecasting and evaluation modules but is not directly applicable to cultural or behavioral aspects."
limitations:
  - "Limited discussion of real-time implementation constraints and computational costs of deep learning models."
  - "Does not address integration with user-defined financial constraints or spending goals."
  - "Focus on electricity data, not financial transaction data, limiting direct applicability to PFMS."
  - "Lack of analysis on forecasting performance in resource-constrained mobile environments."
  - "No validation of methods on Philippine or Southeast Asian household data. [unacknowledged]"
remember_this:
  - "LSTM networks effectively model long-term dependencies in sequential load data."
  - "Hybrid LSTM-CNN models achieve 92.06% accuracy with 75% time reduction for small-range loads."
  - "Probabilistic forecasting provides essential uncertainty quantification for robust HEMS scheduling."
  - "Bottom-up appliance-level forecasting reduces errors but requires efficient lightweight algorithms."
  - "Adaptive online learning enables models to capture dynamic changes in consumption patterns."
```
---

## Paper 12: Khandelwal & Chaudhary_summarized.md

**Source File:** `Khandelwal & Chaudhary_summarized.md`

```yaml
paper_id: b8e2c3d1-4f5a-6b7c-8d9e-0f1a2b3c4d5e
designation: international
title: The Psychology of Colors in UI/UX Design
authors: Khandelwal, P.; Chaudhary, N.
year: 2023
venue: Pratibodh A Journal for Engineering
odin_topics:
  - 9.A
  - 9.B
  - 10.A
  - 10.B
tldr: Color psychology in UI/UX design uses color as a strategic tool to influence user emotions, behavior, and satisfaction.
problem_and_motivation: The impact of color psychology on UI/UX design is underexplored, with a lack of universal guidelines and empirical frameworks for implementation. This gap is important because effective color use is critical for creating engaging interfaces that resonate emotionally with users, yet its application remains subjective.
approach:
  - A systematic review and analysis of 10 case studies from academic journals, blogs, and websites was conducted.
  - Case studies were selected based on relevance, validity, and reliability, covering domains like e-commerce, social media, and health.
  - Each case study was evaluated for its use of color psychology concepts including associations, emotions, and influences.
  - The analysis focused on identifying common patterns, challenges, and solutions in applying color psychology to UI/UX design.
  - The review synthesized findings to determine the overall impact of color choices on user behavior, emotion, and satisfaction.
findings:
  - Color psychology significantly influences user behavior, emotion, and satisfaction in UI/UX design.
  - num: Common patterns show red is used for excitement/urgency, blue for calm/trust, green for growth/harmony, and yellow for happiness/optimism.
  - The most common objective across case studies was improving user satisfaction.
  - Providing relevant and personalized user experiences was the most frequently cited challenge.
  - The most common solution was using color psychology to evoke emotions and influence users.
  - num: The most common result was an increase in user satisfaction scores, followed by increases in conversion rates, engagement rates, and achievement scores.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: UI
    definition: User Interface, the visual and interactive elements of a product.
  - term: UX
    definition: User Experience, the overall impression and satisfaction from using a product.
  - term: Color Psychology
    definition: The study of how colors affect human behavior, emotion, and perception.
critical_citations:
  - None.
relevance:
  topics:
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Discusses designing effective interfaces for user engagement, relevant to mobile-first approach.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Provides general UX principles like visual hierarchy and emotional design applicable to PFMS.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Mentions data privacy and security as challenges in UI/UX design, relevant but not central.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Highlights color's role in establishing trust, aligning with user trust in PFMS.
  contribution: This paper provides foundational knowledge on color psychology that can inform the visual design of Odin's mobile interface. Its principles on using color for emotional resonance and guiding user attention can be applied to enhance user engagement and trust. The discussion on user-specific and cultural considerations offers a starting point for tailoring Odin's color scheme to Filipino users. The findings on increasing user satisfaction through color choices support design decisions aimed at improving user retention.
  directly_justifies:
    - Color choices can significantly influence user satisfaction and behavior in digital interfaces.
    - Using color to create emotional design can help connect with users on an emotional level.
    - Color can be used to create cultural and personal relevance for target audiences.
  limits:
    - The study is a review of existing case studies and does not present new experimental data.
    - The research does not specifically address the Filipino cultural context or personal finance systems. [unacknowledged]
  mapping_rationale: A systematic scan across all 12 functional domains was conducted. The domains flagged as relevant were Mobile-First Design (9.A, 9.B) and Data Privacy & User Trust (10.A, 10.B), with medium relevance for design principles and trust aspects. The paper touches on cultural context (2.A, 2.B) in color associations but is not specific to the Philippines, so these were considered low relevance and not selected. No topics related to algorithms (6, 7, 8), user profiling (5), or financial management (3, 13) were relevant. The paper's overall relevance to Odin is contextual, providing general UX/UI design principles that can inform visual interface design and user trust considerations, but it lacks specific applicability to financial systems or the Filipino demographic.
limitations:
  - The paper relies on a review of case studies and does not provide primary experimental results.
  - It offers general guidance without specific application to personal finance systems or the Filipino cultural context. [unacknowledged]
remember_this:
  - Color psychology significantly affects user behavior, emotion, and satisfaction.
  - Warm colors like red and yellow evoke energy, while cool colors like blue and green evoke calm.
  - Red is commonly used to signal urgency and excitement in UI design.
  - num: The most common result was an increase in user satisfaction scores.
  - Designers must consider cultural and personal differences when applying color psychology.
```
---

## Paper 13: Garg et al-2023_summarized.md

**Source File:** `Garg et al-2023_summarized.md`

```yaml
paper_id: 10.63282/3050-9262.IJAIDSML-V4I3P107
designation: international
title: Leveraging IoT-Driven Customer Intelligence for Adaptive Financial Services
authors: Garg, A.; Mishra, S.; Jain, A.
year: 2023
venue: International Journal of Artificial Intelligence, Data Science, and Machine Learning
odin_topics:
  - 3.A
  - 4.A
  - 4.B
  - 5.A
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
tldr: IoT-enabled real-time data collection and machine learning create hyper-personalized, context-aware financial services that enhance customer engagement and operational efficiency.
problem_and_motivation: Traditional banking offers rigid, one-size-fits-all products that fail to meet modern expectations for personalization. A shift toward context-aware, real-time banking is necessary to compete with fintech disruptors and satisfy digitally savvy customers.
approach:
  - A hybrid methodology blending qualitative synthesis of academic and industrial sources with systems architecture modeling is used.
  - The conceptual framework follows a layered architecture: Perception, Network, Data Processing, Service, and Feedback Loop.
  - The framework integrates IoT sensor data with AI inference layers to adapt banking interfaces dynamically.
  - The system architecture is designed for modular scalability and integration with future technologies like blockchain.
  - Data flow from IoT devices to analytics platforms and personalized services is depicted via end-to-end pipelines.
findings:
  - num: 40% higher conversion rates were observed for geofenced credit card offers compared to generic email campaigns.
  - Contextual data from wearables can be used to trigger positive financial behaviors, such as savings deposits tied to fitness goals.
  - AI-powered anomaly detection using biometric and behavioral data enables faster fraud prevention.
  - IoT-driven personalization leads to a 20-30% reduction in branch operational costs through smart infrastructure.
  - Smart ATMs using biometrics and contextual menus reduce transaction time and maintenance costs.
key_figures_tables:
  - Figure 1: End-to-end IoT to banking services pipeline → Illustrates the modular system architecture for data flow and service personalization.
  - Figure 2: IoT device data flow for personalized services → Shows how raw sensor data is processed into actionable banking insights.
  - Figure 3: Cost vs. Benefit Analysis of IoT Use Cases → Demonstrates positive ROI across various IoT banking applications.
  - Figure 4: Event-Driven Architecture for IoT-Powered Banking → Depicts a responsive system catering to real-world financial events.
  - Table 1: Summary of IoT Use Cases in Global Banking → Lists concrete examples of IoT applications by major financial institutions.
  - Table 2: IoT Technologies Used for Personalization in Banking → Maps specific technologies to their functions and banking applications.
  - Table 3: Core Components of the Conceptual Framework → Defines the essential layers of an IoT personalization system.
  - Table 4: IoT Applications and Customer Benefits → Links personalization features to customer benefits and enabling technologies.
  - Table 5: Tangible Benefits of IoT-Driven Personalization → Provides quantified benefits like +35% app engagement and 45% faster fraud detection.
  - Table 6: Summary of Key Challenges in IoT-Based Personalized Banking → Outlines infrastructure, interoperability, and regulatory hurdles.
key_equations:
  - equation: \(PScore_i = \sum_{j=1}^{n} w_j \cdot x_{ij}\)
    explanation: Personalization score as weighted sum of contextual features for a customer.
  - equation: \(S_i = \beta_0 + \beta_1 \cdot A_i + \beta_2 \cdot T_i + \epsilon_i\)
    explanation: Models savings likelihood from wearable activity and time since last nudge.
  - equation: \(AnomalyScore = \frac{(x - \mu)^2}{\sigma^2}\)
    explanation: Standardized anomaly score for detecting fraud from transaction patterns.
definitions:
  - term: IoT
    definition: Internet of Things, a network of connected devices with sensors and software.
  - term: MEC
    definition: Multi-Access Edge Computing, processing data closer to the device to reduce latency.
  - term: EDA
    definition: Event-Driven Architecture, a system that responds to specific real-world events.
  - term: Zero-trust architecture
    definition: A security model requiring continuous verification of all users and devices.
  - term: Geofencing
    definition: Using GPS to trigger notifications or offers when a user enters a defined area.
critical_citations:
  - "[Atzori et al., 2010] — Foundational survey on IoT architecture for large-scale applications."
  - "[Perera et al., 2014] — Defines context-aware computing for IoT systems."
  - "[Bose, 2022] — Describes AI-powered personalization using IoT data streams for banking."
  - "[Taleb et al., 2017] — Advocates for edge computing to reduce latency in IoT services."
  - "[Maamar et al., 2015] — Highlights challenges in data privacy and consent for IoT financial services."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: IoT data provides rich contextual information that can enhance expense categorization.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: The paper reviews the landscape of IoT applications in banking and fintech, serving as a survey of existing personalization systems.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: It explicitly identifies infrastructure, interoperability, privacy, and legacy system limitations in current banking models.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: The paper directly addresses the creation of financial behavioral profiles using real-time IoT data and machine learning.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: It discusses predictive offers and financial advice using advanced analytics and machine learning models on IoT data.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: It implies forecasting through AI personalization, though specific sequential algorithms are not detailed.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Real-time anomaly detection for fraud prevention is a core use case discussed in the paper.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: The paper provides a specific formula for anomaly scoring and highlights algorithms for detecting fraud.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: The paper strongly emphasizes mobile apps and wearables, justifying a mobile-first approach through IoT integration.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: high
      justification: It discusses responsive UI, voice banking, and context-aware adaptivity, which are core to mobile UX design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: A dedicated section addresses data privacy, security vulnerabilities, and regulatory compliance for IoT banking systems.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Building customer trust through transparency and security is identified as a critical success factor.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: The paper provides metrics (e.g., +40% offer conversion) on how personalization increases user engagement.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: high
      justification: Retention is linked to personalized experiences, voice assistants, and proactive financial nudges.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: Not specifically on Filipino culture, but the general concept of culturally-tailored services is implied.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Mentioned as a generic data point for time-based offers, not a central focus.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: The paper is international, but the concept of "occasions" (geofenced events) is relevant.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: Nudges for savings and budget alerts are mentioned, but not the focus.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: contextual
      justification: Not directly addressed.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: The paper discusses evaluating ROI, customer satisfaction, and engagement as metrics.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: It proposes using fitness data to automatically trigger savings deposits, which is a novel approach for savings management.
  contribution: |
    This paper provides a strong justification for Odin's reliance on real-time data streams by demonstrating how IoT-driven intelligence creates highly personalized financial services. It supports the use of contextual data (location, device, behavior) for modules like behavioral profiling and dynamic spending forecasts. The discussion of AI-powered fraud detection validates Odin's anomaly detection module, while the emphasis on security and privacy directly informs the system's data governance and user trust strategies. Its conceptual framework for layered data processing offers a model for Odin's own architecture, from data ingestion to personalized service delivery.
  directly_justifies:
    - "Contextual data from devices can be used to create dynamic financial behavioral profiles."
    - "Real-time anomaly detection algorithms can effectively prevent fraud in personal finance systems."
    - "Personalized, proactive financial advice increases customer engagement and loyalty."
    - "Geofencing and location-based triggers can improve the relevance of financial offers."
    - "Integrating data from wearables can link physical activity to financial goal achievement."
  limits:
    - "The proposed framework is conceptual and lacks empirical validation in a full-stack bank deployment."
    - "The study acknowledges the fast-changing nature of IoT standards and regulatory compliance as a limitation."
    - "The research is conducted in a US context and may not be directly applicable to developing economies without significant infrastructure investment."
    - "Cost-benefit analyses are based on early pilot data and may not generalize to all banking environments."
  mapping_rationale: |
    A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper is most relevant to the "Existing Systems & Gaps" (Topics 4.A, 4.B), "Behavioral Profiling" (5.A), "Spending Forecasting" (6.A, 6.B), "Anomaly Detection" (8.A, 8.B), "Mobile-First Design" (9.A, 9.B), and "Data Privacy & User Trust" (10.A, 10.B) domains, all assigned high relevance due to its direct treatment of these subjects. The "User Retention & Engagement" domain (11.A, 11.B) was also flagged as high relevance because the paper explicitly links personalization to engagement metrics. The "Expense Categorization" (3.A) domain was assigned medium relevance because IoT data can enhance categorization, though it is not the primary focus. "Savings & Debt Management" (13.A) received medium relevance due to the novel concept of activity-based savings triggers. The "Filipino Cultural Context" domain (2.A, 2.B, 2.D) was considered contextual and only loosely related via generic "occasions" and seasonal spending concepts; these were not prioritized as the paper is international and does not focus on the Philippines. The "Budget Recommendation" domain (7.A, 7.C) was considered contextual as the paper mentions budgeting but does not delve into optimization algorithms or infeasibility handling. Overall, the paper provides a strong, technology-focused justification for a highly personalized, context-aware, and secure financial system, which aligns with Odin's core technological pillars.
limitations:
  - "The proposed framework is not empirically validated in a real banking environment. [unacknowledged]"
  - "The paper does not account for the specific digital infrastructure challenges of developing countries like the Philippines."
  - "Security and privacy solutions are discussed at a high level without detailing specific implementation or testing against real-world attack vectors. [unacknowledged]"
  - "The cost-benefit analysis is based on early-stage data and may not be representative of long-term ROI."
  - "The paper does not address the challenge of user onboarding and the cold-start problem for new users. [unacknowledged]"
remember_this:
  - "Geofenced offers achieved 40% higher conversion rates than generic campaigns."
  - "IoT-enabled smart branches can reduce operational costs by 20-30%."
  - "Real-time anomaly scoring can detect fraud 45% faster than traditional methods."
  - "Personalization requires a robust security and privacy framework to maintain user trust."
  - "Context-aware banking shifts financial services from reactive to predictive engagement."
```
---

## Paper 14: Morris et al_summarized.md

**Source File:** `Morris et al_summarized.md`

```yaml
paper_id: 9f8b7c6d-5e4f-3a2b-1c0d-9e8f7a6b5c4d
designation: international
title: Understanding financial professionals' perceptions of their clients' financial behaviors
authors: Morris, T.; Kamano, L.; Maillet, S.
year: 2023
venue: International Journal of Bank Marketing
odin_topics:
  - 1.A
  - 1.C
  - 2.A
  - 3.A
  - 4.A
  - 5.A
  - 5.B
  - 6.A
  - 7.A
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 13.A
  - 13.B
tldr: Financial professionals perceive client financial behaviors as driven by psychological factors, habits, and system flexibility, with knowledge playing a key role in investment decisions.
problem_and_motivation: Suboptimal financial decisions persist despite financial literacy interventions, and the role of psychological factors and habits is underexplored. Financial professionals offer a unique perspective on underlying behavioral drivers.
approach:
  - Semi-structured interviews were conducted with 26 financial professionals in New Brunswick, Canada.
  - Participants included loan managers, advisers, and accountants from diverse financial institutions.
  - An inductive thematic analysis was applied to the interview transcripts using NVivo 12.
  - The study focused on professionals' perceptions of client behaviors regarding debt, savings, and investment.
findings:
  - num: 90% of clients lack adequate retirement savings, often using savings for unexpected expenses.
  - num: Clients continually refinance homes every two to three years, extracting equity without repayment.
  - num: Only 43% of Americans spend less than disposable income and only 43% can access $2,000 quickly.
  - num: The average debt-to-income ratio in the Eurozone is 96.3%, with ratios as high as 214.6%.
  - num: Canadian household debt is 177% of disposable income, and only 49% budget.
  - num: Only 10% of clients save specifically for retirement, with many starting too late.
  - Psychological factors like instant gratification and lack of discipline outweigh knowledge in debt and savings behaviors.
  - Investment behaviors are more strongly linked to financial knowledge and understanding of products.
  - System flexibility in credit access encourages clients to borrow beyond their means.
  - Financial professionals observe that many clients misuse credit for daily expenses rather than asset purchases.
key_figures_tables:
  - Table 1: Profile of 26 financial professionals by position, institution, age, and gender → Diverse sample across financial sectors.
  - Figure 1: Conceptual framework of financial literacy → Shows financial behavior as an outcome of knowledge, attitudes, and past behaviors.
  - Figure 2: Financial behaviors related to borrowing → Categorizes credit abuse, insistence on credit, and product misuse.
  - Figure 3: Debt repayment behaviors → Highlights insufficient payments and abuse of credit to pay debt.
  - Figure 4: Savings behaviors → Emphasizes lack of savings and starting to save late in life.
  - Figure 5: Investment behaviors → Covers underuse of government programs, risk aversion, and excessive risk-taking.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Financial literacy
    definition: A combination of awareness, knowledge, skills, attitudes, and behaviors needed to make sound financial decisions and achieve financial well-being.
  - term: Financial behavior
    definition: Human action associated with the management of money in cash, credit, and savings.
  - term: Instant gratification
    definition: The desire for immediate consumption at the expense of long-term financial well-being.
  - term: Overconfidence bias
    definition: A psychological bias where individuals overestimate their financial knowledge or skills.
  - term: Self-attribution bias
    definition: The tendency to attribute successes to one's own skills and failures to external factors.
  - term: Disposition bias
    definition: The tendency to sell profitable investments too soon and hold onto depreciating assets too long.
  - term: RRSP
    definition: Registered Retirement Savings Plan, a Canadian government program for retirement savings.
  - term: TFSA
    definition: Tax-Free Savings Account, a Canadian government program for tax-efficient savings.
  - term: RESP
    definition: Registered Education Savings Plan, a Canadian government program for education savings.
critical_citations:
  - "[Allgood and Walstad, 2016] — Links financial knowledge to better financial behaviors."
  - "[Gathergood and Weber, 2017] — Shows short-term biases influence mortgage choices."
  - "[Lusardi and Tufano, 2015] — Links low financial literacy to higher debt accumulation."
  - "[Kaiser and Menkhoff, 2017] — Meta-analysis showing mixed effectiveness of financial education."
  - "[Davies, 2015] — Argues financial literacy responsibility should include industry and government."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Paper focuses on Canadian professionals, but findings on financial behavior are broadly applicable.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: contextual
      justification: Insights on debt, savings, and investment behavior apply to similar demographic groups.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: Highlights psychological and habitual factors, which can be culturally influenced.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Provides qualitative insights into how financial behavior relates to categorizing debt, savings, and investments.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Critiques the flexibility of the financial system and credit access, directly relevant to system design.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly identifies psychological factors and habits that form the basis of behavioral profiling.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: Discusses how behaviors change over time, relevant to dynamic profiling.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: low
      justification: Mentions the lack of planning as a behavior, indirectly relevant to forecasting needs.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Highlights the lack of budgeting as a key problem, directly justifying the need for budget recommendations.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Mentions ethical considerations for financial professionals, but not directly about system privacy.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: contextual
      justification: Discusses client-adviser trust, indirectly relevant to user trust in PFMS.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Discusses the challenge of getting clients to follow advice, relevant to engagement.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: Highlights the importance of early savings and habit formation, relevant to retention.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: Directly addresses the lack of savings and the importance of planning for retirement and emergencies.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: Directly addresses credit abuse, inadequate repayment, and misuse of debt products.
  contribution: The paper provides a qualitative framework for understanding the psychological and habitual drivers behind poor financial behaviors, which can inform Odin's behavioral profiling module. It identifies the need for systems to address instant gratification and lack of discipline, directly supporting Odin's budget recommendation and savings goal management features. The findings on debt misuse and system flexibility justify Odin's anomaly detection and constraint-based budgeting. The study's emphasis on the role of financial professionals highlights the importance of user trust and engagement mechanisms in Odin's design.
  directly_justifies:
    - "Psychological factors like instant gratification are core drivers of debt accumulation."
    - "Lack of financial discipline and planning leads to poor budgeting and savings habits."
    - "System flexibility in credit access encourages users to borrow beyond their means."
    - "Users often misuse credit products due to a lack of financial knowledge."
    - "Early savings and habit formation are critical to long-term financial well-being."
  limits:
    - "Findings are based on perceptions of Canadian financial professionals, not actual client data."
    - "Qualitative methodology limits generalizability to other populations or regions."
    - "The sample may not represent all financial professionals or client demographics."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to Behavioral Profiling (5.A) due to its detailed exploration of psychological factors and habits. It also provides high relevance to Debt Management (13.B) and Savings Management (13.A) through its direct observations of credit abuse and lack of savings. The paper's critique of existing financial systems and credit access makes it highly relevant to Existing Systems & Gaps (4.A). It offers medium relevance to Expense Categorization (3.A) by linking behaviors to financial product use, and to Engagement and Retention (11.A, 11.B) through discussions of client follow-through and habit formation. Borderline cases included the paper's discussion of investment behaviors, which touched on both Financial Behavior (1.C) and Forecasting (6.A), but was ultimately coded under 1.C due to its focus on behavioral drivers. Domains like Mobile-First Design (9.A, 9.B) and Algorithmic Modules (6.B, 8.B, 7.C, 7.D) were considered but rejected as the paper does not address computational methods. The paper's overall relevance to Odin is substantial, providing a rich qualitative foundation for understanding user behaviors that the system aims to improve.
limitations:
  - "Only 26 professionals from one Canadian province were interviewed, limiting geographic diversity."
  - "Client perspectives were not directly obtained, relying solely on professional perceptions."
  - "The study does not generalize to non-Canadian or non-professional populations."
  - "The qualitative design prevents quantitative validation of the identified behavioral drivers."
  - "The study did not explore the effectiveness of specific interventions, focusing instead on perceptions."
remember_this:
  - "Psychological factors and habits outweigh financial knowledge in debt and savings behaviors."
  - "Only 10% of clients save for retirement, indicating a critical need for savings tools."
  - "Financial professionals see system flexibility as a key enabler of client over-indebtedness."
  - "Investment decisions are more strongly tied to financial knowledge than debt or savings."
  - "Lack of budgeting and planning is a fundamental problem across all financial behaviors."
```
---

## Paper 15: Skwara_summarized.md

**Source File:** `Skwara_summarized.md`

```yaml
paper_id: 10.1002/cb.2193
designation: international
title: Effects of mental accounting on purchase decision processes: A systematic review and research agenda
authors: Skwara, F.
year: 2023
venue: Journal of Consumer Behaviour
odin_topics:
  - 3.A
  - 3.B
  - 7.A
  - 7.B
  - 5.A
  - 5.B
  - 9.B
tldr: Mental accounting influences purchase decisions through four themes: source of funds, intended use, pricing, and payment methods, affecting willingness to pay and the pain of paying.
problem_and_motivation: Consumers often deviate from rational economic behavior in spending decisions, violating the principle of money's fungibility. A systematic overview conceptualizing the diverse research outcomes on mental accounting's effects on purchase decisions was lacking.
approach:
  - A systematic literature review was conducted following the three-stage approach by Tranfield et al.
  - The review extracted 786 publications from EBSCO host, ResearchGate, and ScienceDirect using keywords like mental accounting and mental budgeting.
  - After screening titles, abstracts, and full texts, 110 papers were selected for the final sample.
  - A coding sheet was used for data extraction, and a narrative synthesis approach grouped findings into themes.
  - The analysis structured the literature into four main theoretical themes: source of funds, intended use of funds, pricing, and payments.
findings:
  - Consumers categorize income into mental accounts (current income, assets, future income) and spend differently from each.
  - Windfall gains are spent more readily and on luxury goods compared to regular income.
  - Mental budgeting involves grouping expenses into categories with caps, but can also lead to under- or over-consumption.
  - num: 72.73% of the reviewed papers applied a quantitative research type, with experiments being the predominant method (60.91%).
  - The framing of promotions and price points significantly alters consumer perception and willingness to pay.
  - Payment methods with higher transparency, like cash, induce a greater pain of paying compared to credit cards.
  - Consumers often prefer flat-rate pricing despite pay-per-use being cheaper for their usage, to avoid budgeting disruption.
  - The "silver-lining effect" shows consumers prefer a small gain isolated from a larger loss over a larger overall discount.
  - Advance payment systems that result in refunds can reduce price awareness and churn.
  - Research gaps exist on long-term effects of mental budgeting on wealth and the impact of new financial technologies.
key_figures_tables:
  - Table 1: Number of publications per journal between 1970 and 2022 → Journal of Consumer Research has the most publications (16.36%).
  - Figure 2: Structure of the findings with its four main themes → The four themes follow a chronological sequence in decision processes.
  - Table 7: Directions for future research and their potential themes → Future research should examine product categories, budgeting flexibility, and technology's impact.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Mental Accounting
    definition: The set of cognitive operations used by individuals to organize, evaluate, and keep track of financial activities.
  - term: Pain of Paying
    definition: The feeling similar to pain that a consumer experiences when paying for a product or service.
  - term: Mental Budgeting
    definition: The grouping of expenses into categories and constraining each budget with an implicit or explicit cap.
  - term: In-store Slack
    definition: Funds in a shopper's total budget not earmarked for specific items but available for in-store purchase decisions.
critical_citations:
  - "[Thaler, 1999] — Foundational paper defining mental accounting."
  - "[Shefrin & Thaler, 1988] — Introduced the behavioral life-cycle model."
  - "[Prelec & Loewenstein, 1998] — Explained the pain of paying and decoupling."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: The entire review structures how consumers categorize income and expenses into mental accounts, directly informing categorization frameworks.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: high
      justification: The findings on mental budgeting and how consumers assign expenses (e.g., broad vs. narrow) are core design considerations for expense categories.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: The paper provides extensive evidence on mental budgeting behaviors, including goal setting, temporal frames, and its role in financial discipline.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: The review's insights into how consumers set and track budgets are directly applicable to designing effective budget recommendation engines.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: The paper notes that consumer characteristics like education, income, and self-control affect mental accounting, supporting the need for behavioral profiling.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: medium
      justification: The discussion on different responses to budgets and promotions based on consumer traits is relevant for handling cold-start profiling.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: The paper identifies the impact of increased financial transparency through technology as a research gap, which is relevant for mobile UX design.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: The paper discusses exceptional expenses (e.g., birthdays) and seasonal patterns, which are relevant to the concept of "occasions" in a Filipino context.
  contribution: "The paper's systematic review of mental accounting effects directly justifies Odin's need for sophisticated expense categorization (3.A) and budget setting (7.A) modules. The findings on how consumers track spending and the pain of paying (Payments) inform the design of Odin's user experience for expense entry and budget monitoring (9.B). The identification of consumer characteristics influencing mental accounting behavior supports the development of behavioral profiles (5.A) within Odin to personalize recommendations. The discussion on integration-segregation in pricing provides foundational knowledge for how users might perceive budget allocations and recommendations."
  directly_justifies:
    - "Mental accounting explains why users may treat money from different sources differently, affecting budget allocation."
    - "The pain of paying varies by payment method and transparency, influencing user engagement with expense tracking."
    - "Consumers use mental budgets to exercise self-control, but budget rigidity can lead to overconsumption."
    - "Temporal framing affects spending, suggesting that budget periods must be flexible and user-defined."
    - "The impact of technology on mental accounting is a key area for future research relevant to Odin's design."
  limits:
    - "The review is limited to the effects on purchase decision processes and does not cover other financial behaviors like investing."
    - "Most reviewed studies used short-term experiments, limiting insights on long-term effects of mental accounting."
    - "The influence of new technologies like budgeting apps on mental accounting is identified as a research gap."
  mapping_rationale: "A systematic scan of all 12 functional domains was conducted. The domain of Expense Categorization (3.A, 3.B) was flagged as highly relevant because the paper's core finding is how consumers categorize and assign funds to mental accounts. The domain of Budget Recommendation (7.A, 7.B) was also highly relevant, given the extensive evidence on mental budgeting strategies and goal setting. Behavioral Profiling (5.A, 5.B) was assessed as medium relevance because the paper notes that individual characteristics (e.g., self-control) influence mental accounting, supporting the need for personalized profiles. Mobile-First Design (9.B) was deemed medium relevance because the paper identifies the impact of financial technology (e.g., apps, notifications) on consumer behavior, directly informing UX design. Filipino Cultural Context domains (2.A, 2.B, 2.C, 2.D) were considered and rejected as the paper does not examine cultural or seasonal spending patterns specifically. Existing Systems (4.A, 4.B) was rejected as the paper does not analyze other PFMS. Anomaly Detection (8.A-C) and Savings & Debt Management (13.A-C) were rejected due to lack of direct mention. The paper's overall relevance to Odin is high, as it provides a comprehensive theoretical foundation for understanding user spending behavior, which is central to Odin's personal finance management functions."
limitations:
  - "The sample may have omitted some relevant papers despite a broad database search."
  - "The review focuses only on mental accounting's impact on purchase decisions, excluding other financial areas. [unacknowledged]"
  - "The findings are largely based on experimental studies, which may not fully reflect real-world behavior."
remember_this:
  - "Mental accounting theory explains how consumers categorize income and expenses."
  - "Windfall gains are spent more readily than regular income on luxury goods."
  - "Payment method transparency affects the pain of paying and spending behavior."
  - "Consumer characteristics like self-control influence mental budgeting success."
  - "Mental budgeting can both enforce financial discipline and lead to overconsumption."
```
---

## Paper 16: Omotayo et al_summarized.md

**Source File:** `Omotayo et al_summarized.md`

```yaml
paper_id: 10.62225/2583049X.2023.3.6.4736
designation: international
title: Behavior-Driven Personalization Framework to Improve Repeat Usage in Mobile-Enabled Financial Ecosystems
authors: Omotayo, K. V.; Uzoka, A. C.; Okolo, C. H.; Olinmah, F. I.; Adanigbo, O. S.
year: 2023
venue: International Journal of Advanced Multidisciplinary Research and Studies
odin_topics:
  - 11.A
  - 11.B
  - 5.A
  - 9.A
  - 9.B
  - 10.B
tldr: A behavior-driven personalization framework uses real-time user actions, dynamic segmentation, and personalized triggers to increase repeat usage in mobile financial apps.
problem_and_motivation: Mobile financial platforms face a critical retention gap, with most users disengaging after initial adoption. This occurs because experiences are generic and fail to respond to evolving financial behaviors, goals, or constraints. A systematic framework placing behavioral data at the core of personalization is needed to enhance relevance and increase repeat usage.
approach:
  - The proposed framework has three core layers: Behavioral Data Capture, Segmentation Engine, and Personalized Trigger System.
  - Behavioral Data Capture collects high-frequency interactions and passive signals like screen transitions and feature usage.
  - The Segmentation Engine uses this data to dynamically categorize users into cohorts like habitual, casual, or value-seeking.
  - The Personalized Trigger System delivers tailored nudges, prompts, and adaptive UI elements based on segment and behavior.
  - A continuous feedback loop inspired by reinforcement learning refines personalization strategies based on observed user responses.
findings:
  - num: Most users abandon finance apps within the first month, with daily active usage declining sharply after onboarding.
  - num: User progression across financial goals is a richer measure of value creation than binary retention metrics.
  - Real-time behavioral personalization aligns more closely with user intent, promoting repeat interactions and deeper financial engagement.
  - A built-in feedback loop minimizes notification fatigue by suppressing irrelevant interactions and reducing cognitive overload.
  - Embedding behavior-driven intelligence transforms apps from transactional tools into relational platforms that evolve with user behavior.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Behavioral Data Capture
    definition: The layer responsible for collecting and organizing user activity data, including passive signals and interactions.
  - term: Segmentation Engine
    definition: A component that categorizes users into dynamic behavioral cohorts to tailor personalization strategies.
  - term: Personalized Trigger System
    definition: A layer that delivers tailored content like smart notifications, in-app nudges, and adaptive UI elements based on behavioral insights.
  - term: Feedback Loop
    definition: A continuous learning mechanism that refines personalization strategies based on observed user responses.
  - term: Nudge
    definition: A subtle change in the choice environment that steers users toward beneficial decisions without restricting freedom of choice.
critical_citations:
  - "[Kahneman and Tversky, 1979] — Foundational work on loss aversion and prospect theory."
  - "[Thaler and Sunstein, 2008] — Seminal work on nudges and choice architecture."
relevance:
  topics:
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: Directly proposes a framework to increase repeat usage and engagement through behavior-driven personalization.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: high
      justification: Provides specific mechanisms like dynamic segmentation, personalized triggers, and feedback loops for retention.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Uses real-time behavior to dynamically segment users, aligning with behavioral profile principles.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Grounds personalization within the context of mobile ecosystem dynamics and real-time data capabilities.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Describes adaptive UI elements and in-app nudges as key components of the mobile UX for engagement.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: contextual
      justification: Discusses ethical personalization, transparency, and goal-aligned nudging to build trust and long-term relationships.
  contribution: This paper provides a theoretical and practical blueprint for Odin's engagement module, justifying the use of real-time behavioral data to drive retention. It directly informs the design of a segmentation engine and personalized trigger system for nudging users. The framework's feedback loop supports the continuous learning required for Odin's adaptive personalization. Its emphasis on ethical, goal-aligned nudging aligns with Odin's mission to improve financial well-being, not just retention.
  directly_justifies:
    - Real-time behavioral data is essential for dynamic segmentation and personalization in financial apps.
    - Personalized nudges and adaptive UI can significantly improve feature adoption and habit formation.
    - A continuous feedback loop is necessary to refine personalization strategies and avoid user fatigue.
    - Behavioral science principles like loss aversion and heuristics should be embedded in personalization logic.
    - Ethical personalization, focused on user well-being, is crucial for building trust and long-term engagement.
  limits:
    - The paper presents a conceptual framework with limited empirical validation or experimental results.
    - It does not specify exact algorithms for segmentation or trigger optimization, remaining high-level.
    - The framework's applicability to specific cultural contexts like the Philippines is not addressed.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. Domains directly addressed include User Retention & Engagement (11.A, 11.B) with high relevance, as the paper's core contribution is a framework for repeat usage. Behavioral Profiling (5.A) and Mobile-First Design (9.A, 9.B) received medium relevance, as the framework uses behavioral data and is tailored to mobile contexts. Data Privacy & User Trust (10.B) was flagged as contextual, given the discussion of ethical design. Domains related to expense categorization (3.A-C), forecasting (6.A-B), budget recommendation (7.A-D), anomaly detection (8.A-C), system evaluation (12.A-C), and savings/debt management (13.A-C) were considered but rejected as the paper does not provide specific, citeable claims informing Odin's design in these areas. Overall, the paper is highly relevant for informing Odin's engagement and personalization strategy, but less so for its core algorithmic financial management modules.
limitations:
  - The framework is conceptual and lacks empirical validation from real-world implementations. [unacknowledged]
  - Specific algorithmic details for segmentation or trigger optimization are not provided, limiting direct technical applicability. [unacknowledged]
  - The paper does not address the unique financial behaviors or cultural context of Filipino young professionals. [unacknowledged]
remember_this:
  - Behavior-driven personalization increases repeat usage by adapting to real-time user actions.
  - A continuous feedback loop refines personalization strategies, minimizing notification fatigue.
  - Dynamic user segmentation enables tailored, contextually relevant interventions.
  - num: Most users abandon finance apps within the first month of onboarding.
  - Ethical, goal-aligned nudging is crucial for building trust and long-term financial well-being.
```
---


---

## Agent Instruction

If the agent reading this document believes further context about a paper is needed, it may request the original converted markdown file (with the '_marked' suffix) from the user for the relevant paper(s).
