# Deep Learning for Credit Risk Prediction: A Survey of Methods, Applications, and Challenges

## Metadata

```yaml
---
paper_id: "10.3390/info17040395"
designation: international
title: "Deep Learning for Credit Risk Prediction: A Survey of Methods, Applications, and Challenges"
authors: "Mienye, I. D.; Esenogho, E.; Modisane, C."
year: 2026
venue: "Information"
odin_topics: ["5.C", "6.A", "6.B", "8.A", "8.B", "12.A", "12.B"]
shorthand_tags: ["/forecasting-methods-survey", "/temporal-dependency", "/forecast-algo-candidates", "/forecast-algo-comparison", "/forecast-eval-metrics", "/classification-vs-clustering", "/classifier-candidates", "/anomaly-algo-candidates", "/anomaly-eval-metrics", "/eval-frameworks-survey", "/eval-ml-design"]
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[X]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---
```

## TL;DR

Deep learning architectures (MLP, CNN, RNN, transformer, GNN) improve credit risk prediction over classical models on large datasets but face unresolved challenges in temporal evaluation, calibration, interpretability, fairness, and operational deployment.

## Problem and Motivation

Prior surveys on credit risk prediction either treat deep learning as one model family among many or focus narrowly on tabular scorecard settings, lacking systematic coverage of sequential, transformer, and graph-based architectures. Credit risk prediction is central to financial stability and regulatory compliance, yet the rapid adoption of data-driven lending demands a unified synthesis of deep learning methods and their deployment challenges. No existing review provides a modality-aware taxonomy linking model families to borrower-level data structures while critically assessing evaluation integrity, interpretability, and governance gaps.

## Approach

- Searched IEEE Xplore, Scopus, ACM, ScienceDirect, SpringerLink, Web of Science, and Google Scholar for peer-reviewed studies (2015–2025).
- Queries paired credit‑risk terms (credit scoring, default prediction) with deep learning terms (CNN, RNN, LSTM, transformer, GNN).
- Screened 380 records down to 140 application studies and 18 surveys after de‑duplication and title/abstract filtering.
- Extracted data modality (tabular, sequential, textual, relational), model architecture, credit product segment, prediction target, and evaluation metrics.
- Synthesized challenges and research directions through narrative analysis, not formal meta‑analysis.

## Findings

1. LSTM reduced MAE from 0.095 to 0.072 (**24% improvement**) on monthly default‑rate forecasting, outperforming ARIMA, SVM, and ANN on the Lending Club dataset.
2. TabNet‑stacking ensemble achieved AUC = 0.941 and accuracy = 0.979 on the Tianchi dataset (≈800,000 cases), substantially outperforming single‑model baselines.
3. Multi‑head RGAT on SME relational graphs reached AUC = 0.799 and KS = 0.528, surpassing non‑graph models without using transactional features.

- Deep models systematically outperform logistic regression and tree ensembles only when trained on large, temporally rich, and high‑cardinality datasets.
- Most studies rely on random k‑fold cross‑validation, causing temporal leakage and overoptimistic performance estimates.
- Calibration metrics (Brier score, expected calibration error) and cost‑sensitive evaluation are rarely reported despite being central to decision‑making.
- Interpretability and fairness are treated as post‑hoc add‑ons; only a small fraction incorporate explainability or fairness constraints in training.

## Key Figures and Tables

- Figure 1: PRISMA flowchart → 380 initial records → 140 application studies after screening.
- Table 2: Benchmark datasets → German Credit (1k rows), Home Credit (300k+ rows); larger datasets better approximate industrial settings.
- Table 3: DL architecture summary → matches each model class to input modality, strength, and limitation.
- Table 4: Deep learning applications → 30+ studies organized by model family, reporting AUC, accuracy, MAE, etc.
- Table 5: Challenges and directions → maps evaluation integrity, imbalance, interpretability, robustness, and governance to research pathways.

## Key Equations

$$EL = PD \times LGD \times EAD$$
*Expected loss = product of default probability, loss severity, and exposure.*

$$\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V$$
*Self-attention computes pairwise relevance across all sequence positions in parallel.*

$$\mathbf{h}_v^{(l+1)} = \sigma\left( \sum_{u \in \mathcal{N}(v)} \frac{1}{c_{vu}} \mathbf{W}^{(l)} \mathbf{h}_u^{(l)} \right)$$
*GNN message passing: neighbor embeddings are aggregated to update each node’s risk representation.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| AUC | Area under the ROC curve – rank‑based measure of class separation. |
| Calibration | How well predicted probabilities match observed default rates. |
| Concept drift | Change in the relationship between features and target over time. |
| DL | Deep learning – neural networks with multiple hidden layers. |
| EL | Expected loss – product of PD, LGD, and EAD. |
| GNN | Graph neural network – learns from relational borrower networks. |
| LSTM | Long short‑term memory [think: forget gate keeps long patterns, input gate adds new info]. |
| MLP | Multi‑layer perceptron – basic feed‑forward neural network. |
| Out‑of‑time validation | Training on past data, testing on strictly later data – prevents leakage. |
| PD | Probability of default – core credit scoring target. |
| RNN | Recurrent neural network – processes sequences stepwise with a hidden state. |
| TCN | Temporal convolutional network – uses dilated convolutions for parallel sequence processing. |

## Critical Citations

- [Vaswani et al., 2017] — Introduced transformer self‑attention, enabling parallel global dependency modelling in credit sequences.
- [Lessmann et al., 2015] — Established benchmark protocols for credit scoring, showing AUC alone masks operating‑region performance.
- [Rudin, 2019] — Argues against post‑hoc explanations for high‑stakes decisions, motivating interpretable‑by‑design architectures.

## Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

12.A — Evaluation Frameworks for Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This survey directly informs Odin’s forecasting and anomaly detection modules by providing a comparative analysis of deep learning architectures for sequential financial data. The documented superiority of LSTM/GRU over static models on repayment sequences justifies Odin’s choice of recurrent networks for spending forecasting, while the survey’s synthesis of temporal convolutional networks and transformers offers alternative candidates if Odin’s transaction histories grow long or multimodal. Importantly, the paper’s critical evaluation of random split versus out‑of‑time validation establishes a required evaluation standard for Odin’s module performance testing, and its discussion of calibration, concept drift, and class imbalance provides actionable design warnings even though the domain differs (credit default vs. personal spending).

**Directly justifies:**

- “LSTM reduces forecasting MAE from 0.095 to 0.072 (24% gain) on monthly financial sequences, outperforming ARIMA and SVM – directly applicable to Odin’s per‑category spending forecast module.”
- “Random k‑fold cross‑validation causes temporal leakage; out‑of‑time splits are mandatory for realistic evaluation of any sequential spending model in Odin.”
- “Deep tabular models (TabNet‑stacking) achieve AUC = 0.941 on large‑scale financial data, but gradient boosting remains competitive on small datasets – Odin must benchmark both families on its expected user scale.”
- “Graph neural networks capture risk propagation without transactional features (AUC = 0.799 on SME relational graphs) – relevant if Odin later adds household or group spending analytics.”
- “Calibration metrics (Brier score, expected calibration error) are rarely reported in deep credit studies, yet miscalibrated probabilities lead to poor budget alerts – Odin’s evaluation must mandate calibration reporting.”

**Limits of relevance:**

- Domain mismatch: credit default prediction (rare binary event, high cost of misclassification) vs. spending forecasting and anomaly detection (continuous, lower stakes) – methods transfer but performance expectations differ.
- Geography: all datasets and studies are non‑Filipino; spending patterns and income volatility in Metro Manila may not mirror Western or Chinese credit data.
- Data scale: most high‑performing DL studies use hundreds of thousands to millions of records; Odin’s per‑user transaction history will be far smaller, potentially favoring simpler models.
- No coverage of cold‑start or manual input constraints – Odin’s lack of banking API integration and initial user sparsity are not addressed.
- No discussion of mobile‑first design or on‑device inference constraints – the survey assumes server‑side deployment.

## Limitations

- Only peer‑reviewed English studies; excludes proprietary industrial models and grey literature (e.g., central bank reports) that may contain relevant Filipino context.
- No formal risk‑of‑bias scoring or meta‑analysis; performance claims from individual studies may not generalize across datasets or horizons. [unacknowledged]
- Temporal evaluation practices are critiqued but not quantitatively assessed across the surveyed literature (e.g., what fraction of papers use out‑of‑time splits). [unacknowledged]
- Fairness and interpretability are discussed at a high level, but the survey does not operationalize which techniques work for which model families in production.
- The survey’s recommendations focus on regulatory credit (Basel, SR 11-7) and do not map to personal finance system evaluation (ISO 25010, SUS) – Odin would need to adapt the evaluation integrity lessons to its own quality model.

## Remember This

- 🔑 **LSTM cut MAE by 24%** on financial sequences – sequential memory beats static models.
- 📌 Out‑of‑time validation is mandatory – random splits leak future information and overestimate performance.
- 💡 Deep models win only on large, rich datasets – tree ensembles remain strong small‑data baselines.
- ⚠️ Calibration (Brier/ECE) almost never reported – yet crucial for trustworthy budget alerts.
- 🔍 GNNs capture relational risk without transaction details – useful if Odin adds group spending.
