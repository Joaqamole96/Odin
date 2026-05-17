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
odin_topics: ["4.B", "5.C", "6.A", "6.B", "8.B", "12.A", "12.B"]
shorthand_tags: ["/pfms-limitations", "/classifier-candidates", "/forecasting-methods-survey", "/forecast-algo-candidates", "/anomaly-ml-families", "/eval-frameworks-survey", "/eval-ml-design"]
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

Deep learning models (MLP, CNN, RNN, Transformer, GNN) beat traditional credit scoring on large behavioral datasets, but evaluation integrity, interpretability, and deployment governance remain unsolved.

## Problem and Motivation

Prior surveys on credit risk either treat deep learning as one among many model families or focus narrowly on tabular scorecards, lacking systematic coverage of sequential, transformer, and graph architectures for borrower-level prediction. Systematic understanding of when and why specific DL architectures work for credit risk is essential for regulatory adoption and reliable deployment. No existing review synthesizes model families, data modalities, and deployment challenges together in a unified taxonomy.

## Approach

- Search across IEEE Xplore, Scopus, ACM, ScienceDirect, SpringerLink, Web of Science, and Google Scholar (2015–2025).
- Screening: 380 initial records → 208 after de-duplication → 140 DL application studies + 18 survey/guideline papers included.
- Taxonomy organized by model class: MLP, CNN, RNN/LSTM/GRU, TCN, Transformer, GNN, and hybrid architectures.
- Extracted data modality (tabular, sequential, textual, relational), credit segment (consumer, SME, corporate), prediction target (PD, LGD, EAD), and evaluation metrics.
- Evaluation integrity assessed: temporal leakage, calibration metrics (Brier, ECE), cost-sensitive scoring, and reject inference.

## Findings

1. HDNN with L1–L2 regularization achieved **80.12% accuracy** for corporate credit, outperforming LR (AUC=0.717) and SVM (AUC=0.738).
2. LSTM for monthly default rate forecasting reduced **MAE from 0.095 to 0.072** and RMSE from 0.119 to 0.093 versus ARIMA, SVM, and ANN.
3. CNN–LSTM–attention model reached AUC=0.92 and F1=0.91 for enterprise credit, beating CNN-only and LSTM-only baselines.
4. RGAT on SME relational graphs achieved AUC=0.799 and KS=0.528; multi-head extension reached AUC=0.799, KS=0.528.
5. TabNet-stacking ensemble on Tianchi dataset (≈800k cases) achieved **AUC=0.941** and accuracy=0.979.

- Transformers (TabTransformer, FT-Transformer) match or exceed XGBoost/CatBoost on high-cardinality tabular data.
- Most studies use random k-fold cross-validation, causing temporal leakage; calibration (Brier, ECE) and cost-sensitive metrics are rarely reported.
- Interpretability (SHAP, attention) and fairness (equalized odds) are treated as post hoc add-ons, not training objectives.

## Key Figures and Tables

- Figure 2: MLP architecture → feed-forward with hidden layers learns nonlinear feature interactions for tabular credit data.
- Figure 3: LSTM gating mechanism → forget, input, output gates preserve long-term repayment patterns.
- Table 3: DL architectures for credit risk → maps each model class to input modality, strengths, and limitations.
- Table 4: Summary of DL applications → collates 30+ studies with datasets, architectures, and reported metrics.
- Table 5: Challenges and research directions → links evaluation integrity, imbalance, interpretability, robustness, and governance to concrete future work.

## Key Equations

$$P(y=1|x)=\frac{1}{1+\exp(-w^\top x-b)}$$
*Logistic regression — baseline credit scoring model with linear log-odds.*

$$f_t=\sigma(W_f[h_{t-1},x_t]+b_f),\quad i_t=\sigma(W_i[h_{t-1},x_t]+b_i),\quad C_t=f_t\odot C_{t-1}+i_t\odot\tilde{C}_t,\quad h_t=o_t\odot\tanh(C_t)$$
*LSTM gates (forget, input, output) control long-term memory in repayment sequences.*

$$\text{Attention}(Q,K,V)=\text{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V$$
*Self-attention computes global dependencies across all time steps or features in parallel.*

$$h_v^{(l+1)}=\sigma\left(\sum_{u\in\mathcal{N}(v)}\frac{1}{c_{vu}}W^{(l)}h_u^{(l)}\right)$$
*GNN message passing — borrower node updates by aggregating neighbor representations.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| PD | Probability of default — likelihood a borrower fails to repay. |
| LGD | Loss given default — proportion of exposure not recovered after default. |
| EAD | Exposure at default — total amount outstanding when default occurs. |
| MLP | Multi-layer perceptron — basic feed-forward neural network with hidden layers. |
| CNN | Convolutional neural network — uses sliding filters to capture local temporal patterns. |
| RNN | Recurrent neural network — processes sequences stepwise with hidden state. |
| LSTM | Long short-term memory [think: memory cell with forget/input/output gates] — preserves long-range repayment patterns. |
| GRU | Gated recurrent unit [simplified LSTM with update and reset gates] — fewer parameters than LSTM. |
| TCN | Temporal convolutional network — uses dilated convolutions for parallel sequence processing. |
| GNN | Graph neural network — learns from relational structures (borrower networks) via message passing. |
| AUC | Area under ROC curve — threshold-agnostic ranking performance metric. |
| AUPRC | Area under precision–recall curve — better for imbalanced default datasets. |
| ECE | Expected calibration error — measures alignment between predicted probabilities and observed frequencies. |

## Critical Citations

- [Vaswani et al., 2017] — Introduced transformer self-attention, now adapted to credit risk via TabTransformer and FT-Transformer.
- [LeCun et al., 2015] — Foundational deep learning review establishing representation learning principles for tabular and sequential data.
- [Lessmann et al., 2015] — Benchmarking study showing tree ensembles (random forest, boosting) often outperform deep nets on small credit datasets.
- [Thomas et al., 2017] — Canonical credit scoring text defining PD, LGD, EAD and reject inference challenges.
- [Rudin, 2019] — Argues against black-box explanations for high-stakes decisions, motivating interpretable-by-design credit models.

## Relevance to Odin

**Topics:**

4.B — Limitations and Gaps in Existing Systems

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

8.B — Anomaly Detection Algorithm

12.A — Evaluation Frameworks for Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This survey directly informs Odin’s algorithm selection for spending forecasting (LSTM/GRU vs. CNN vs. transformer) and anomaly detection by benchmarking sequential deep learning architectures on financial time series. The paper’s critique of evaluation integrity—temporal leakage, calibration neglect, overreliance on AUC—provides a checklist for Odin’s module-level validation, especially given Odin’s manual transaction input and cold-start constraints. Its synthesis of interpretability (SHAP, attention) and fairness (equalized odds) offers practical guidance for Odin’s user trust and explainability requirements under Philippine data privacy law (RA 10173).

**Directly justifies:**

- "LSTM networks reduce MAE from 0.095 to 0.072 for monthly default forecasting, demonstrating that recurrent architectures capture behavioral drift better than static models."
- "Random k-fold cross-validation causes temporal leakage in credit risk studies; out-of-time splits and rolling-origin validation are required for realistic performance estimates."
- "Deep tabular models (MLP, TabNet) with attentive embeddings match gradient boosting on large datasets (≥300k records) with high-cardinality categorical features."
- "Most deep credit risk studies ignore probability calibration (Brier score, ECE), leading to miscalibrated PD estimates even when AUC improves."
- "GNNs (RGAT, GraphSAGE) capture relational risk propagation (co-applicant, director, supply-chain ties) that tabular models structurally cannot represent."

**Limits of relevance:**

- Survey focuses on credit default (borrower non-repayment), not personal spending budgeting; spending forecasting and anomaly detection in Odin share similar sequential modeling needs but different outcome definitions.
- All studies use banking/transaction data with rich historical sequences; Odin starts from manual input with sparse cold-start histories, limiting direct transfer of reported performance gains.
- No Filipino-specific demographic or income stability analysis; behavioral patterns of South African, US, and Chinese borrowers may not generalize.
- Many benchmark datasets (German Credit, Australian Credit) are small (≤1000 records) and static, unlike Odin’s per-user transaction stream.

## Limitations

- Only peer-reviewed English studies indexed in major databases; proprietary industry implementations and regulatory grey literature excluded.
- No formal risk-of-bias or meta-analysis; reported performance numbers are not standardized across datasets, horizons, or label definitions. [unacknowledged]
- Does not address cold-start profiling or spending forecasting for new users with no transaction history—central to Odin’s design problem.
- Survey’s evaluation recommendations (out-of-time splits, calibration metrics) are not applied to any original model, remaining prescriptive rather than demonstrative. [unacknowledged]
- Privacy-preserving methods (differential privacy, federated learning) are mentioned but not evaluated on credit tasks; practical utility–privacy trade-offs unknown.

## Remember This

- 🔑 **LSTM cut MAE by 24% (0.095→0.072)** — sequential models beat ARIMA/SVM for financial time series.
- 📌 Most credit DL papers use random splits → temporal leakage inflates results; use out-of-time validation.
- 💡 AUC alone is insufficient — report calibration (Brier, ECE) and AUPRC for imbalanced defaults.
- ⚠️ No cold-start evaluation in survey — Odin’s manual-entry users lack history, so reported gains may not apply.
- 🔍 GNNs capture hidden risk propagation (co-applicant networks) — relevant if Odin adds social/family obligation features.
