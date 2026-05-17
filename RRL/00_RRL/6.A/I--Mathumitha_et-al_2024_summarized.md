# Intelligent deep learning techniques for energy consumption forecasting in smart buildings: a review

## Metadata

```yaml
---
paper_id: "10.1007/s10462-023-10660-8"
designation: international
title: "Intelligent deep learning techniques for energy consumption forecasting in smart buildings: a review"
authors: "Mathumitha, R.; Rathika, P.; Manimala, K."
year: 2024
venue: "Artificial Intelligence Review"
odin_topics: ["6.A", "6.B"]
shorthand_tags: ["/forecasting-methods-survey", "/temporal-dependency", "/forecast-algo-candidates", "/forecast-algo-comparison", "/forecast-eval-metrics"]
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

Deep learning models, especially hybrid CNN-LSTM architectures, consistently outperform traditional time series methods for building energy forecasting by automatically learning temporal dependencies.

## Problem and Motivation

Accurate energy demand forecasting is critical for balancing electricity supply and demand, yet traditional linear models fail to capture nonlinear patterns and long-term dependencies. Poor forecasts lead to grid inefficiencies, higher CO₂ emissions from fossil fuel over-generation, and increased operational costs. No prior review systematically compared deep learning architectures for building energy forecasting across forecast horizons, input types, and evaluation metrics.

## Approach

- Dataset: Review of ~60 prior studies on smart building energy forecasting using deep learning.
- Methods surveyed: LSTM, GRU, CNN, RNN, hybrid CNN-LSTM, CNN-GRU, TCN, autoencoders, and ensemble models.
- Analysis dimensions: forecast horizon (short/medium/long), building type (residential/non-residential/both), input parameters (historical, calendar, weather, occupancy), and evaluation metrics (RMSE, MAE, MAPE, R², CV-RMSE).
- Benchmark comparisons: Hybrid models consistently beat single-architecture networks on accuracy.

## Findings

- **72% of reviewed studies focused on non-residential buildings**, 18% on residential, and 10% on both.
- **68% of studies used short-term forecasting (days to weeks)**; only 5% used medium-term.
- Hybrid CNN-LSTM models achieve the highest reported accuracy, reducing RMSE by up to 40% compared to standalone RNNs or ARIMA.
- LSTM and GRU effectively handle vanishing gradient problems that limit traditional RNNs.
- Weather variables (temperature, humidity) are the most influential external factors after historical consumption.
- Peak load prediction remains a persistent challenge — most ML models underperform during irregular demand spikes.

## Key Figures and Tables

- Figure 3: Forecasting horizon distribution → 68% short-term, 27% long-term, 5% medium-term.
- Figure 4: Building type distribution → 72% non-residential, 18% residential, 10% both.
- Table 3: Summary of deep learning methods → Hybrid CNN-LSTM reports RMSE as low as 0.4.
- Table 4: Evaluation metrics equations → RMSE, MAE, MAPE, CV-RMSE, R² defined.

## Key Equations

$$RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(x_{pred} - x_{act})^2}$$
*Root mean squared error penalizes large forecast errors more heavily.*

$$MAPE = \frac{1}{n}\sum_{i=1}^{n}\left|\frac{x_{pred} - x_{act}}{x_{act}}\right| \times 100\%$$
*Mean absolute percentage error gives interpretable relative error rate.*

## Definitions

| Term / Acronym | Plain-English Definition |
| --------------- | ------------------------ |
| LSTM | Long Short-Term Memory — a recurrent network with memory cells that learn what to forget and remember over long sequences. |
| GRU | Gated Recurrent Unit — a simpler LSTM variant with two gates instead of three. |
| CNN | Convolutional Neural Network — extracts spatial or local patterns from input data. |
| TCN | Temporal Convolutional Network — uses dilated convolutions to capture long-range time dependencies without recurrence. |
| ARIMA | Autoregressive Integrated Moving Average — a classical linear time series model. |
| RMSE | Root Mean Squared Error — measures average prediction error with emphasis on large deviations. |
| MAE | Mean Absolute Error — average absolute difference between predicted and actual values. |
| MAPE | Mean Absolute Percentage Error — error expressed as a percentage of actual values. |

## Critical Citations

- [Mocanu et al., 2016] — First large-scale comparison of deep CNN vs. ELM, ARIMA, and RNN for day-ahead load forecasting.
- [Khan et al., 2020a] — Proposed hybrid CNN-LSTM-AE framework that became a benchmark for building energy forecasting.
- [Ghimire et al., 2023] — Demonstrated CNN-ESN hybrid outperforms standalone LSTM on daily demand prediction.
- [Amasyali & El-Gohary, 2018] — Comprehensive review of data-driven building energy prediction methods, cited as foundational context.

## Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

**Contribution to Odin:**

This review directly informs Odin's spending forecasting module by systematically comparing time series forecasting algorithms. The finding that hybrid CNN-LSTM models achieve lower error than standalone RNNs or ARIMA justifies evaluating hybrid architectures for per-category spending prediction. The review's emphasis on LSTM's ability to handle long-term dependencies and irregular patterns is directly applicable to Odin's transaction sequences, which are sparse and exhibit weekly/monthly cycles. Although the domain is building energy, the methodological comparisons of forecast horizons, input features (historical + calendar + weather → analogous to historical spending + calendar events), and error metrics transfer cleanly to financial time series.

**Directly justifies:**

- "Hybrid CNN-LSTM architectures reduce RMSE by up to 40% compared to standalone RNNs or ARIMA in time series forecasting tasks with irregular patterns."
- "LSTM and GRU overcome the vanishing gradient problem that limits traditional RNNs, enabling effective learning of long-term dependencies in sequential transaction data."
- "Short-term forecasting (days to weeks) accounts for 68% of reviewed studies, reflecting its higher accuracy and immediate operational value — a principle applicable to Odin's per-month budget forecasting."
- "Weather variables are the most influential external factor after historical consumption; by analogy, calendar events (paydays, holidays, bill due dates) should be key inputs to spending forecasts."

**Limits of relevance:**

- Domain is building energy consumption, not personal financial transactions; spending patterns have different drivers (income, discretionary choice) than thermostatic loads.
- Review reports aggregated findings from many studies; no single controlled experiment comparing algorithms on financial data.
- Most reviewed datasets are high-frequency (minute/hourly) smart meter data; Odin uses daily or per-transaction manual entries, which are sparser.
- Peak load prediction challenges in energy may not directly parallel anomalous spending detection, which has different behavioral causes.

## Limitations

- Review does not conduct its own experiments; all performance claims are aggregated from primary studies with varying datasets and evaluation protocols.
- No critical assessment of publication bias — studies reporting positive results for deep learning may be overrepresented. [unacknowledged]
- Limited discussion of computational cost or mobile deployment constraints, which are critical for Odin's mobile-first design.
- All reviewed studies use automated smart meter data; none use manually entered transaction data, so cold-start and user entry friction are not addressed.
- Geographic scope is global; none of the datasets or building types reflect Philippine climate or occupancy patterns.

## Remember This

- 🔑 **72% of studies on non-residential buildings** — but residential (18%) better analog for personal finance.
- 📌 **68% use short-term forecasting (days–weeks)** — aligns with Odin's monthly budget horizon.
- 💡 Hybrid CNN-LSTM cuts RMSE by up to 40% over standalone RNNs — strong justification for exploring hybrids in spending forecasting.
- ⚠️ No evaluation on manually entered, sparse transaction data — Odin's input mode differs from smart meters.
- 🧠 Weather and calendar data are top external predictors — Odin should use calendar features (paydays, holidays) as key inputs.
