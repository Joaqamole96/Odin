```yaml
paper_id: 10.62986/dp2025.60
designation: local
title: Election-Year Stimuli and Economic Performance: Evidence from a Macroeconometric Model of the Philippines
authors: Ruiz, M. G. C.; Miral, R. M. L.; Rivera, J. P. R.
year: 2025
venue: PIDS Discussion Paper Series
odin_topics:
  - 2.B
  - 4.B
  - 6.A
  - 7.A
  - 8.A
  - 12.A
  - 12.B
tldr: Election years generate short-term, demand-driven expansions in the Philippine economy, but these effects are transitory and revert to baseline levels post-election.
problem_and_motivation: Existing macroeconometric models for the Philippines lack explicit integration of political and institutional shocks, particularly election-induced fluctuations. This limits policymakers' ability to distinguish between temporary election-driven booms and sustainable growth drivers. The study addresses this gap by augmenting a model to quantify how election shocks transmit through the economy.
approach:
  - Augmented a small macroeconometric model for the Philippines using quarterly data from 2002Q1 to 2023Q4.
  - Behavioral equations were estimated using the ARDL method in ECM form with lag lengths selected via AIC.
  - Cointegration was tested using the bounds test approach; specifications were chosen to align with economic theory.
  - Included a dummy variable for the COVID-19 pandemic period (2020Q2-2021Q2) to control for structural disruption.
  - Introduced election spending shocks as impulse shocks to private consumption and government consumption equations, simulating pre-election demand surges.
findings:
  - Election shocks generate short-term expansions in private consumption (8-18% above baseline), employment (~2.7%), investment (4-11%), and government consumption (7-15%).
  - These effects are transitory; economic activity reverts near baseline levels post-election as fiscal impulses fade.
  - Pre-election spending boosts are driven by fiscal frontloading, campaign activities, and temporary job creation, aligning with political business cycle theory.
  - Election-driven growth is cyclical rather than structural and may induce inefficiencies in expenditure allocation and fiscal discipline.
  - The model demonstrates reasonable predictive accuracy with MAPEs for GDP components ranging from 2% to 10%, and MAEs for rates within acceptable margins.
key_figures_tables:
  - Figure 2: In-sample simulations tracking actual vs. forecasted macroeconomic variables → Model tracks actual data well across most aggregates.
  - Table 2: Forecast accuracy metrics for 2021Q1-2023Q4 → MAPEs under 10% for most level variables; MAEs for rates remain modest.
  - Figure 3: Election spending shock scenario simulations → Consumption and employment spike temporarily, then revert to baseline.
  - Table 3: Validation of empirical results against scholarly literature → Results align with PBC theory on magnitude, timing, and persistence.
key_equations:
  - equation: \log C_t = f(\log(YD_t), \pi_t^e, r_t - \pi_t, \pi_t)
    explanation: Household consumption depends on disposable income, expected inflation, real rate, and inflation.
  - equation: \log I_t = f(\log(Y_t), \Delta(r_t - \pi_t), \pi_t)
    explanation: Investment depends on output, change in real rate, and inflation.
  - equation: \Delta \log(CPI_t) = f(\Delta \log(p_t^{oil}), \Delta \log(p_t^{rice}), \Delta \log(D_t), \Delta \log(xrr_t))
    explanation: CPI inflation is a function of oil prices, rice prices, debt, and real exchange rate.
  - equation: PB_t \equiv RV_t - XP_t
    explanation: Primary balance is revenues minus primary expenditures.
definitions:
  - term: PBC
    definition: Political business cycles; electoral manipulation of fiscal/monetary tools for reelection.
  - term: ARDL
    definition: Autoregressive Distributed Lag; econometric method for cointegration analysis.
  - term: ECM
    definition: Error Correction Model; captures short-run dynamics and long-run equilibrium.
  - term: MAPE
    definition: Mean absolute percentage error; forecast accuracy metric for level variables.
  - term: MAE
    definition: Mean absolute error; forecast accuracy metric for rate/percentage variables.
  - term: PPP
    definition: Public-Private Partnership; infrastructure projects exempt from election spending ban.
critical_citations:
  - "[Rogoff and Sibert, 1988] — Foundational PBC theory on pre-election fiscal expansions."
  - "[Brender and Drazen, 2005] — Political budget cycles differ across established vs. new democracies."
  - "[Drazen and Eslava, 2010] — Electoral manipulation via voter-friendly spending in developing economies."
  - "[Shi and Svensson, 2006] — Cross-country evidence on political budget cycles and determinants."
  - "[Debuque-Gonzales and Corpus, 2023, 2024] — Base macroeconometric model framework for the Philippines."
relevance:
  topics:
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: high
      justification: Directly models election-driven cyclical spending surges in the Philippine economy.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Explicitly addresses the gap in Philippine models regarding election shocks.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Uses macroeconometric forecasting to simulate election shock effects.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Provides evidence on fiscal policy impacts relevant to budget recommendations.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Election shocks are fiscal anomalies; provides context for detecting abnormal spending patterns.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Demonstrates model evaluation with MAPE/MAE and in-sample simulations.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Evaluates the performance of the macroeconometric model's forecasting accuracy.
  contribution: This paper provides a validated macroeconometric framework that can inform Odin's forecasting module (6.A) by demonstrating how exogenous shocks like elections propagate through demand-side variables. It offers empirical justification for incorporating political cycle signals into predictive models, supporting Odin's behavioral profiling and anomaly detection features. The finding that election effects are transitory and demand-driven directly justifies the need for Odin to distinguish between cyclical anomalies and structural spending changes in user data. The paper's emphasis on fiscal transparency and counter-cyclical policies aligns with Odin's design for user trust and long-term stability.
  directly_justifies:
    - "Election shocks generate short-term demand-driven expansions in consumption, investment, and employment."
    - "Election-related economic activity is cyclical and reverts to baseline post-election."
    - "Government consumption expands by 7-15% in pre-election quarters and normalizes afterward."
    - "Pre-election fiscal expansions may distort expenditure allocation and fiscal discipline."
  limits:
    - "Model stability issues due to structural breaks like GFC and COVID-19 may affect long-run relationships."
    - "Simplified dummy variable for COVID-19 may not fully capture pandemic-induced behavioral shifts."
    - "Post-COVID structural changes (digital transformation, altered spending patterns) may not be fully reflected."
    - "Sectoral-level impacts are not disaggregated; only aggregate GDP components are analyzed."
    - "Qualitative influence of election outcomes (candidate characteristics) is not modeled."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The Filipino Cultural Context domain was flagged as relevant via 2.B (Seasonal and Cyclical Spending Patterns) with high relevance, as the paper directly models election cycles—a recurring seasonal phenomenon in the Philippines. The Existing Systems & Gaps domain was flagged via 4.B (Limitations and Gaps) with high relevance, as the paper explicitly identifies and addresses the gap in Philippine macroeconometric models regarding political shocks. Spending Forecasting was flagged via 6.A (Predictive Modeling) with medium relevance due to the use of forecasting to simulate shock effects. Budget Recommendation was flagged via 7.A (Budgeting Strategies) with medium relevance because the paper provides empirical evidence on fiscal policy impacts. Anomaly Detection was flagged via 8.A (Anomaly Detection) with contextual relevance, as election shocks provide a context for identifying abnormal fiscal patterns. System Evaluation was flagged via 12.A and 12.B with medium relevance, as the paper evaluates model performance. Domains such as Expense Categorization (3), Behavioral Profiling (5), Mobile-First Design (9), Data Privacy (10), User Retention (11), and Savings/Debt Management (13) were considered but rejected as the paper does not address these specific operational aspects of personal finance systems. Borderline cases: the paper touches on both 2.B (cyclical patterns) and 2.D (Filipino spending cycles/occasions), but 2.B was chosen as the primary code since the analysis focuses on cyclical timing rather than cultural occasion-specific practices. Overall, the paper is highly relevant for Odin's understanding of macroeconomic context and political-economic signals that can influence individual spending behavior, but its direct applicability is limited to informing model calibration and contextual awareness rather than end-user features.
limitations:
  - "Model stability and specification issues due to structural breaks like GFC and COVID-19 may have introduced parameter instability. [unacknowledged]"
  - "Simplified dummy variable treatment of COVID-19 may not fully capture the depth and persistence of pandemic-induced disruptions. [unacknowledged]"
  - "Post-pandemic structural changes (digital transformation, altered spending patterns) may not be fully reflected in the model calibrated on pre-2020 relationships. [acknowledged]"
  - "Sectoral-level impacts are not estimated; only aggregate GDP components are analyzed. [acknowledged]"
  - "Qualitative influence of election outcomes, such as leadership attributes, is not modeled. [acknowledged]"
  - "The model's usability for real-time private-sector decision-making is limited relative to simpler forecasting tools. [acknowledged]"
remember_this:
  - "Election-year consumption surges 8-18% above baseline but quickly reverts."
  - "Employment rises ~2.7% during election quarters, then normalizes post-election."
  - "Government spending increases 7-15% before elections, followed by fiscal contraction."
  - "Election-driven growth is cyclical and demand-driven, not structural."
  - "Fiscal frontloading may distort expenditure allocation and long-term development."
```