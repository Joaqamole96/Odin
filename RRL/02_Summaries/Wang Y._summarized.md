```yaml
paper_id: a8f5f167-0d6e-5f6a-8b1d-4e7b2c3d9e8f
designation: international-algorithm-specific
title: New developments in sequential change point detection for time series and spatio-temporal analysis
authors: Wang, Y.
year: 2023
venue: Worcester Polytechnic Institute
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
  - 3.A
  - 4.A
  - 5.A
  - 7.A
tldr: Develops ensemble non-parametric, Bayesian hierarchical, and Bayesian online spatio-temporal frameworks for sequential change point detection in financial durations and public health surveillance data.
problem_and_motivation: Abrupt aberrations in stochastic systems often result from external factors of interest but monitoring complex streaming data requires efficient methods. Existing approaches either assume independence or Gaussian properties, limiting applicability to modern high-dimensional, interdependent data. There is a need for innovative methodologies that can handle time-dependence and spatio-temporal interdependence for timely detection.
approach:
  - Proposes an ensemble penalized estimating function (E-PEF) method for online structural break detection in financial durations using log ACD models.
  - Develops a Bayesian hierarchical framework (BVAR(1)-LCM) with bivariate temporal and latent level-correlated effects for multivariate count time series using INLA.
  - Introduces BOSTON-PUPA, an iterative sequential outbreak detection procedure with prior updating and p-value adaptation for spatio-temporal count data using a generalized Poisson model.
  - Utilizes block bootstrap resampling and Mahalanobis distance thresholds to handle non-Gaussian detector statistics and spillover effects.
  - Employs Integrated Nested Laplace Approximation (INLA) for fast, scalable Bayesian inference on latent Gaussian models with sparse precision matrices.
findings:
  - num: E-PEF method controls type I error under 5% and achieves detection probabilities exceeding 80% within short delays after structural breaks.
  - num: BVAR(1)-LCM demonstrates superior computational efficiency, with INLA being over ten times faster than STAN while maintaining comparable parameter recovery and prediction accuracy.
  - num: BOSTON-PUPA achieves up to 75% sensitivity at SNR=1.25 and near 100% at SNR=2, with controlled false detection rates below 5% for most regions.
  - num: Prior Updating with discounting factor 0.25 improves parameter recovery rates by 5-10% compared to cumulative fitting.
  - The overdispersion parameter in GPD models serves as an effective global aberration indicator for outbreak detection.
key_figures_tables:
  - Figure 4: Detection probability over monitoring horizon → E-PEF controls false detection and spikes power after true break.
  - Figure 11: Estimated temporal correlation ρωωω across sectors → Strong positive correlation (>0.75) justifies bivariate AR modeling.
  - Figure 19: Aggregated performance vs SNR → P-value Adaptation significantly improves Sensitivity and Global Error.
  - Table 12: Model comparison percentages → BVRW(1)-LCM favored in 88-90% of datasets for out-of-sample prediction.
  - Table 20: Detection frequencies by location → HMP and CCT methods show better false control in less populated areas.
key_equations:
  - equation: "GGG_{M_2}(k) = (G_{M_2,1}(k), ..., G_{M_2,d}(k))'"
    explanation: Standardized PEF detector statistic for break detection.
  - equation: "\\eta_{j,st} = \\log\\lambda_{j,st} = ZZZ_j \\beta\\beta\\beta_j + \\gamma_{j,t} + \\alpha_{j,st}"
    explanation: BVAR(1)-LCM link function for Poisson lognormal count model.
  - equation: "\\Pr(Y_{s,t}=y|\\theta_{s,t},\\lambda) = \\frac{\\theta_{s,t}(\\theta_{s,t}+\\lambda y)^{y-1}}{y!}\\exp(-(\\theta_{s,t}+\\lambda y))"
    explanation: Generalized Poisson distribution mass function for surveillance counts.
  - equation: "Q_{s,T+k} = Q_{s,T+k-1} + g(p^*_{s,T+k})"
    explanation: Cumulative detector statistic for combined p-value methods.
definitions:
  - term: E-PEF
    definition: Ensemble Penalized Estimating Function, a non-parametric online change point detection method.
  - term: INLA
    definition: Integrated Nested Laplace Approximation, a fast Bayesian inference method for latent Gaussian models.
  - term: GMRF
    definition: Gaussian Markov Random Field, a finite-dimensional random vector with a sparse precision matrix.
  - term: BVAR(1)-LCM
    definition: Bivariate AR(1) model with Latent Level Correlation for multivariate count time series.
  - term: BOSTON-PUPA
    definition: Bayesian Online Spatio-Temporal Outbreak Detection with Prior Updating and P-value Adaptation.
  - term: HMP
    definition: Harmonic Mean P-value, a method for combining dependent p-values.
  - term: CCT
    definition: Cauchy Combination Test, a method for combining dependent p-values.
  - term: SNR
    definition: Signal-to-Noise Ratio, a measure of outbreak magnitude relative to baseline variability.
  - term: MAE
    definition: Mean Absolute Error, a measure of prediction accuracy.
critical_citations:
  - "[Engle and Russell, 1998] — Foundation for ACD duration models."
  - "[Rue et al., 2009] — Introduced INLA for fast Bayesian inference."
  - "[Page, 1954] — Developed CUSUM, basis for sequential change detection."
  - "[Berkes et al., 2004] — Quasi-likelihood approach for sequential change detection."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Develops forecasting algorithms for sequential financial duration and count data.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Proposes E-PEF and BVAR(1)-LCM for forecasting and detecting changes in financial time series.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Outbreak detection framework provides methods for detecting anomalies in spatio-temporal count data.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Discusses CUSUM, Bayesian HMM, and combined p-value methods applicable to spending data anomalies.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Evaluates detection performance using sensitivity, specificity, and error metrics.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Compares INLA vs MCMC for parameter recovery and prediction accuracy.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Count data modeling with risk levels is analogous to categorizing transaction types.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews traditional methods (SPC, ARIMA) and their limitations, informing system design.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Behavioral changes in durations and counts relate to spending behavior profiling.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: General forecasting and anomaly detection concepts are foundational for budgeting.
  contribution: "The E-PEF method can directly inform Odin's anomaly detection module (8.B) by providing a non-parametric, online approach for detecting spending pattern changes. The BVAR(1)-LCM framework supports Odin's expense categorization (3.A) by modeling correlated transaction types. The BOSTON-PUPA procedure offers a robust template for Odin's forecasting (6.A) and anomaly detection (8.A) modules, especially for handling spatio-temporal dependencies. The comprehensive evaluation methodology (12.A, 12.B) provides metrics for assessing Odin's algorithmic performance. The INLA implementation demonstrates how Odin can achieve scalable Bayesian inference for complex models."
  directly_justifies:
    - "Online change point detection can be achieved via ensemble non-parametric methods without distributional assumptions."
    - "Latent correlation models effectively capture dependencies between multiple financial time series."
    - "Bayesian hierarchical models with INLA provide fast, scalable inference for spatio-temporal count data."
    - "Prior updating techniques improve model stability and inference quality in streaming data contexts."
    - "Combined p-value methods like HMP and CCT control false detection rates under arbitrary dependency."
  limits:
    - "E-PEF method's monitoring horizon is finite, requiring resetting for long-term surveillance."
    - "BVAR(1)-LCM assumes linearity in the log link and may not capture extreme non-linearities."
    - "BOSTON-PUPA's performance degrades in regions with very small populations due to inflated false positives."
    - "The framework relies on user-defined thresholds for SNR and aberration indicators."
    - "Real-time applicability depends on computational resources, though INLA mitigates this concern."
  mapping_rationale: "A systematic scan across all 12 functional domains and associated topic codes was performed. Domains flagged as relevant include Predictive Modeling (6.A, 6.B), Anomaly Detection (8.A, 8.B), and System Evaluation (12.A, 12.B) due to the paper's direct development of forecasting and detection algorithms. Expense Categorization (3.A) and Existing Systems (4.A) received medium relevance as the paper models categorical transaction data and reviews traditional methods. Behavioral Profiling (5.A) and Budgeting (7.A) were deemed contextual, as the paper provides general predictive techniques but does not directly address user behavior or budget recommendations. Domains related to Filipino cultural context (2.A-D), Mobile-First Design (9.A-B), Data Privacy (10.A-B), User Retention (11.A-B), Savings (13.A-C), and Classification (5.B-C) were rejected as they were not addressed. Borderline cases include temporal patterns (2.B) which are implicitly modeled but not culturally specific, and user-defined constraints (3.C) which are not discussed. Overall, the paper provides strong methodological contributions for anomaly detection and forecasting modules within Odin but lacks direct focus on user-centric design or Filipino-specific financial practices."
limitations:
  - "E-PEF assumes stationarity in the training period, which may not hold for volatile financial data. [unacknowledged]"
  - "BVAR(1)-LCM's performance relies on correct specification of the precision matrix for latent effects. [unacknowledged]"
  - "BOSTON-PUPA's false detection control in small populations requires further investigation. [acknowledged]"
  - "Computational time for INLA can be irregular depending on initial values and model complexity. [acknowledged]"
  - "The framework does not address multiple change points or resetting mechanisms. [unacknowledged]"
  - "Model selection for combined p-value methods may require domain-specific tuning. [unacknowledged]"
remember_this:
  - "E-PEF achieves robust structural break detection without distributional assumptions on innovations."
  - "INLA provides over tenfold speedup compared to MCMC for multivariate count time series."
  - "BOSTON-PUPA controls false detections at 5% while achieving 75-100% sensitivity for outbreaks."
  - "Latent correlation between risk-level counts consistently exceeds 0.75 across financial sectors."
  - "Generalized Poisson overdispersion parameter serves as a reliable global outbreak indicator."
```