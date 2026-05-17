# Review of Family-Level Short-Term Load Forecasting and Its Application in Household Energy Management System

## Metadata

```yaml
---
paper_id: "10.3390/en16155809"
designation: international
title: "Review of Family-Level Short-Term Load Forecasting and Its Application in Household Energy Management System"
authors: "Ma, P.; Cui, S.; Chen, M.; Zhou, S.; Wang, K."
year: 2023
venue: "Energies"
odin_topics: ["4.A", "5.A", "6.A", "6.B"]
shorthand_tags: ["/pfms-intelligent-features", "/profile-dimensions", "/forecasting-methods-survey", "/temporal-dependency", "/forecast-algo-candidates", "/forecast-algo-comparison"]
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

LSTM neural networks outperform classical time-series models for household-level load forecasting by learning long-term dependencies, and hybrid CNN-LSTM models further improve accuracy.

## Problem and Motivation

Individual household electricity loads lack the consistent patterns of aggregated system-level loads due to random human behavior, making accurate short-term forecasting difficult. Accurate household load forecasting is critical for home energy management systems (HEMS) to optimize energy use, reduce costs, and enable demand response. Prior forecasting methods (ARIMA, SVR, RF) struggle with non-linear, non-stationary household data, and no single review systematically compared deep learning approaches for this granularity.

## Approach

- **Scope:** Review of short-term (hours to days ahead) and ultra-short-term (hourly) household-level and appliance-level load forecasting methods.
- **Data sources:** Smart meter data (active/reactive power, voltage, current) plus contextual data (weather, calendar, occupant behavior patterns).
- **Deep learning models surveyed:** RNN, LSTM, CNN, hybrid LSTM-CNN, GRU, and stacked LSTM (SLSTM).
- **Feature extraction techniques:** Wavelet decomposition (DWT), collaborative representation (CRT), mutual information (MI), principal component analysis (PCA), and domain-specific time-series features.
- **Adaptive learning approaches:** Online learning, recursive learning, transfer learning, and edge-computing-compatible deep reservoir architectures.
- **Probabilistic forecasting:** Quantile regression neural networks (QRNN), Bayesian deep learning, and consumption-scenario-based methods to model forecast uncertainty.
- **Bottom-up forecasting:** Predict individual appliance loads first (via NILM and LSTM), then aggregate to household total – shown to reduce error versus direct household forecasting.

## Findings

1. LSTM-based frameworks achieve **higher prediction accuracy** than ARIMA, SVR, and Random Forest on household load data due to memory cells and gating mechanisms that capture long-term dependencies.
2. A hybrid SVR-LSTM model achieved the highest correlation coefficient (**R = 0.9901**) and lowest error on microgrid load data, outperforming standalone SVR and LSTM.
3. A CNN-GRU model with attention mechanism reached **92.06% accuracy** for small-range load prediction and reduced prediction time by **75%** compared to general deep learning models.

- Bottom-up forecasting (appliance-level then aggregation) improves accuracy over direct household-level forecasting, but LSTM in this mode is computationally expensive; Kalman filters offer a lighter alternative.
- Probabilistic load forecasting captures uncertainty (e.g., confidence intervals) better than single-value deterministic forecasts, essential for robust HEMS scheduling.
- Online adaptive RNNs that continuously learn from new data can handle concept drift caused by changing user behavior patterns.

## Key Figures and Tables

- Figure 2: LSTM-based forecasting framework → shows input sequence (historical load) passing through LSTM layers to produce future load prediction.
- Figure 5: Probabilistic load forecasting framework → illustrates how uncertainty intervals are generated alongside point forecasts.
- Table 1: Comparison of classical time-series, LSTM, and CNN models → LSTM excels at non-linear/non-stationary data; CNN works when historical data are sparse.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LSTM | Long Short-Term Memory – a recurrent neural network with memory cells that learn what to remember and forget [think: selective memory for time series]. |
| CNN | Convolutional Neural Network – extracts local patterns using sliding filters. |
| HEMS | Home Energy Management System – optimizes household electricity use via scheduling. |
| NILM | Non-Intrusive Load Monitoring – infers appliance-level consumption from a single meter reading. |
| ARIMA | AutoRegressive Integrated Moving Average – classical time-series model assuming linear stationarity. |
| RNN | Recurrent Neural Network – processes sequences by maintaining a hidden state across time steps. |

## Critical Citations

- [Hochreiter & Schmidhuber, 1997] — Original LSTM paper; solves gradient vanishing/exploding in RNNs, foundational to all subsequent load forecasting work.
- [Kong et al., 2023 (ref 11 in paper)] — Demonstrated LSTM outperforms other machine learning algorithms for household load prediction.
- [Zheng et al., 2019] — Showed bottom-up (appliance-first) LSTM forecasting reduces error compared to direct household prediction.
- [Brusaferri et al., 2022] — First comprehensive exploration of Bayesian deep learning for probabilistic load forecasting, combining uncertainty types.

## Relevance to Odin

**Topics:**

4.A — Landscape of Existing Personal Finance Systems

5.A — Financial Behavioral Profiles in Personal Finance

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

**Contribution to Odin:**

This review directly supports Odin's spending forecasting module by systematically comparing deep learning architectures (LSTM, CNN, hybrid) for time-series prediction on irregular, behavior-driven data – exactly the challenge Odin faces with manual transaction histories. The finding that LSTM captures long-term dependencies better than classical models (ARIMA, SVR) justifies selecting LSTM or a hybrid as the forecasting algorithm. The review's discussion of adaptive online learning to handle concept drift (changing user behavior) informs Odin's requirement that behavioral profiles update over time. Although the domain is electricity consumption, the methodological insights transfer directly to financial transaction sequences, which also exhibit temporal dependence and user-specific patterns.

**Directly justifies:**

- "LSTM networks achieve superior accuracy over ARIMA, SVR, and Random Forest on non-linear, non-stationary household time-series data, making them the preferred architecture for spending forecasting in personal finance systems."
- "Hybrid CNN-LSTM models can capture both short-term local patterns (via CNN) and long-term dependencies (via LSTM), improving forecast accuracy on irregular sequences."
- "Probabilistic forecasting methods (quantile regression, Bayesian deep learning) provide uncertainty intervals alongside point predictions, enabling risk-aware budget recommendations."
- "Online adaptive RNNs that continuously learn from new data can handle concept drift caused by changing user behavior, addressing the cold-start and profile-update problems in financial profiling."
- "Bottom-up forecasting – predicting category-level spending first then aggregating – reduces error compared to direct total spending prediction, analogous to appliance-level then household total in load forecasting."

**Limits of relevance:**

- Domain is electricity load, not financial spending; spending patterns have different drivers (income, prices, preferences vs. weather, appliance schedules).
- The review focuses on short-term forecasting (hours to days), while Odin primarily needs monthly and weekly budget forecasting.
- Data availability differs: smart meters provide high-frequency automatic readings; Odin relies on sparse, manual transaction entries.
- Many deep learning models discussed require substantial historical data; Odin's cold-start scenario (new users with little history) may need lighter algorithms (e.g., Kalman filters mentioned in the paper).

## Limitations

- The paper is a review, not a primary study; claimed performance numbers (e.g., 92.06% accuracy) come from cited works, not validated in a single controlled experiment.
- No direct comparison of forecasting algorithms on a standardized household load dataset; each study uses different data, time horizons, and evaluation metrics.
- Computational efficiency of LSTM and hybrid models for mobile deployment is not addressed – a critical constraint for Odin's mobile-first design. [unacknowledged]
- The review does not discuss handling of missing or sparse data (e.g., users who forget to log transactions), which is central to Odin's manual input model. [unacknowledged]
- All cited studies are from non-Philippine contexts; cultural spending patterns and income volatility in Metro Manila may alter forecasting performance.

## Remember This

- 🔑 LSTM beats ARIMA/SVR on irregular, behavior-driven sequences – the same pattern applies to spending transactions.
- 📌 **92% accuracy** with CNN-GRU + attention; 75% faster prediction – hybrid models balance speed and precision.
- 💡 Online adaptive RNNs handle concept drift as user behavior changes – directly supports Odin's dynamic profiling requirement.
- 🔍 Bottom-up (category-first) forecasting reduces error – Odin should predict per-category spending before summing to total.
