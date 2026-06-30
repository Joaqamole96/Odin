# Compiled Research Summaries

## Filters Applied

- Designation: `international`

**Total Papers:** 25

**Note:** Included papers positions 26 to 50, Sorted by year.

---

## Paper 1: Kara & Senguler_summarized.md

**Source File:** `Kara & Senguler_summarized.md`

```yaml
paper_id: "10.1111/pbaf.70008"
designation: "international"
title: "A Comparative Analysis of Budget Forecasting Methods: A Systematic Literature Review Covering the 1983–2024 Period"
authors: "Kara, B.; Şengüler, H."
year: 2025
venue: "Public Budgeting & Finance"
odin_topics:
  - "6.A"
  - "6.B"
  - "7.A"
  - "12.C"
tldr: "Systematic review of 69 studies shows no universally superior budget forecasting method; performance depends on context, with a four-stage evolution from statistical to deep learning models."
problem_and_motivation: "Budget forecasts are critical for fiscal policy, yet the literature lacks a systematic comparison of forecasting methods across contexts. Existing studies provide fragmented findings due to variations in datasets, time periods, and countries, making method selection difficult for practitioners."
approach:
  - "Systematically analyzed 69 peer-reviewed comparative studies on budget forecasting methods from 1983 to 2024."
  - "Categorized methods into four phases: statistical methods, diversification, machine learning, and deep learning."
  - "Applied descriptive statistical analysis, trend analysis, and network analysis (using Gephi) to examine method frequencies, co-occurrences, and temporal patterns."
  - "Analyzed performance metrics, training data characteristics (time span, frequency, observations), and forecasting horizons."
  - "Examined geographic distribution and relationship between methodological diversity and citation impact."
findings:
  - "num: 43% of studies focus on the United States, indicating significant geographic concentration."
  - "num: MAPE (38 studies), RMSE (36), and MAE (22) dominate performance evaluation, while directional errors are largely neglected."
  - "Methodological evolution shows four phases: basic statistical (1980s), diversification (1990s), machine learning (2010s), and deep learning (2020s)."
  - "Optimal method choice depends on contextual factors, with no single model universally superior."
  - "Simple models like OFC, RW, and regression remain relevant benchmarks, often performing comparably to complex models."
  - "Studies comparing 3–6 methods have highest average citation impact (26 citations), while excessive method comparisons reduce impact."
  - "Training datasets typically span 11–15 years (17 studies), with quarterly, annual, and monthly data used at similar frequencies."
  - "Parametric and multivariate models focus on shorter horizons (ARIMA: 5.5 years), while simpler statistical methods handle longer forecasts (AR: 14.3 years)."
key_figures_tables:
  - "Table 1: Comprehensive summary of 69 comparative studies detailing methods, best/worst performers, metrics, and country contexts → Foundation for comparative analysis."
  - "Figure 1: Four-stage methodological evolution from ARIMA to LSTM and hybrid models → Shows increasing complexity and diversity over time."
  - "Figure 2: Network of method co-occurrences shows ARIMA, OFC, and regression as common benchmarks → Traditional methods serve as anchors for comparisons."
  - "Table 2: Training data characteristics reveal 11–15 years as most common span → Highlights data constraints and geographical biases."
  - "Graph 3: Forecasting horizons by method show simple models used for long-term, complex models for short-term → Division of labor in methodological approaches."
key_equations:
  - equation: "MAPE = (1/n) * Σ(|Actual - Forecast| / Actual) * 100"
    explanation: "Mean absolute percentage error, most common evaluation metric."
  - equation: "RMSE = sqrt((1/n) * Σ(Actual - Forecast)²)"
    explanation: "Root mean square error, penalizes large errors heavily."
  - equation: "MAE = (1/n) * Σ|Actual - Forecast|"
    explanation: "Mean absolute error, intuitive measure of average error magnitude."
definitions:
  - term: "ARIMA"
    definition: "Autoregressive Integrated Moving Average, a time-series forecasting method."
  - term: "VAR"
    definition: "Vector Autoregression, multivariate time-series model."
  - term: "ANN"
    definition: "Artificial Neural Network, a machine learning method."
  - term: "LSTM"
    definition: "Long Short-Term Memory, a deep learning recurrent neural network."
  - term: "XGBoost"
    definition: "Extreme Gradient Boosting, a machine learning algorithm."
  - term: "SVM"
    definition: "Support Vector Machine, a machine learning classification/regression method."
  - term: "MIDAS"
    definition: "Mixed Data Sampling, a method for forecasting with mixed-frequency data."
  - term: "COF"
    definition: "Combination of Forecasts, an ensemble approach."
  - term: "OFC"
    definition: "Official Forecasts, benchmark forecasts from official agencies."
  - term: "MAPE"
    definition: "Mean Absolute Percentage Error, a forecasting accuracy metric."
  - term: "RMSE"
    definition: "Root Mean Square Error, a forecasting accuracy metric."
  - term: "MAE"
    definition: "Mean Absolute Error, a forecasting accuracy metric."
critical_citations:
  - "[McDonald et al., 2024] — Identified data methods as top-tier research priority."
  - "[Downs and Rocke, 1983] — Early comparative study using multivariate ARMA models."
  - "[Litterman and Thomas, 1983] — Early use of VAR for budget forecasting."
  - "[Ghysels and Ozkan, 2012] — Introduced MIDAS for real-time budget forecasting."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews forecasting methods and contextual factors affecting performance."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "medium"
      justification: "Compares ARIMA, ANN, LSTM, XGBoost across different data conditions."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "contextual"
      justification: "Provides background on budget forecasting methodologies and their evolution."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "medium"
      justification: "Documents dominance of MAPE/RMSE/MAE and neglect of directional metrics."
  contribution: "This systematic review provides a comprehensive foundation for Odin's forecasting module by establishing that no single forecasting method is universally optimal, and that performance depends on contextual factors such as data quality, forecasting horizon, and economic conditions. The review's documentation of evaluation metric hegemony (MAPE, RMSE, MAE) informs Odin's evaluation framework design by highlighting the need for asymmetric loss functions. The identification of a four-stage methodological evolution and the persistent relevance of simple benchmarks (OFC, RW, regression) guides Odin's hybrid modeling strategy for budget recommendations."
  directly_justifies:
    - "Optimal forecasting method choice depends on contextual factors, not universal superiority."
    - "Simple models like OFC and RW remain relevant benchmarks for evaluating complex models."
    - "Data constraints in developing economies limit applicability of data-hungry methods like deep learning."
    - "Evaluation should include directional metrics to capture asymmetric costs of forecast errors."
    - "Hybrid and ensemble approaches may leverage strengths of different methods."
  limits:
    - "Geographic concentration in the United States limits generalizability to developing economies. [unacknowledged]"
    - "Dominance of MAPE/RMSE/MAE neglects directional errors and asymmetric costs of misforecasting."
    - "Training data constraints (11–15 year average) may limit applicability to data-scarce contexts. [unacknowledged]"
    - "The review does not address the specific challenges of personal spending data (vs. macroeconomic data). [unacknowledged]"
  mapping_rationale: "Systematic scan across all 12 functional domains and 38 topic codes identified relevance to predictive modeling (6.A, 6.B), evaluation methodologies (12.C), and contextual relevance to budgeting strategies (7.A). The paper was considered for 8.A (anomaly detection) but rejected as it does not address outlier detection specifically. 2.D (Filipino spending cycles) was rejected due to no Philippines-specific analysis. 3.A (expense categorization) was rejected as the review focuses on forecasting methods, not classification. The high-level review of forecasting methods and their evaluation provides medium relevance to Odin's algorithm selection and evaluation framework design, with contextual value for understanding budgeting strategy domain knowledge."
limitations:
  - "Geographic concentration (43% US) limits generalizability to developing economies. [unacknowledged]"
  - "Dominance of MAPE/RMSE/MAE neglects directional errors and asymmetric costs."
  - "The review does not address personal finance spending data specifically. [unacknowledged]"
  - "Limited discussion of hybrid and ensemble methods despite noting their emergence. [unacknowledged]"
remember_this:
  - "No single budget forecasting method is universally superior."
  - "43 percent of reviewed studies focus on the United States."
  - "MAPE, RMSE, and MAE dominate performance evaluation."
  - "Simple models like OFC remain relevant benchmarks."
  - "Context determines optimal method choice, not model complexity."
```
---

## Paper 2: Kavitha & Krishnan_summarized.md

**Source File:** `Kavitha & Krishnan_summarized.md`

```yaml
paper_id: "10.34293/commerce.v13iS1-i2-Mar.8737"
designation: "international"
title: "AI-based Personal Financial Management: Opportunities and Challenges"
authors: "Kavitha, S.; Krishnan, S."
year: 2025
venue: "ComFin Research"
odin_topics:
  - "3.A"
  - "4.A"
  - "4.B"
  - "6.A"
  - "7.A"
  - "7.B"
  - "8.A"
  - "8.B"
  - "10.A"
  - "10.B"
  - "13.A"
tldr: "AI-powered personal financial management tools offer automated budgeting, investment guidance, and fraud detection but face challenges in data privacy, algorithmic bias, overreliance, and regulatory gaps."
problem_and_motivation: "Despite the growing adoption of AI in personal finance, significant challenges such as data security, algorithmic bias, lack of regulation, and overreliance on automation remain underexplored. This paper analyzes these opportunities and challenges to promote responsible AI use. The review aims to highlight both the benefits and the necessary safeguards for AI-based PFM."
approach:
  - "Reviews academic and industry literature on AI applications in personal financial management."
  - "Identifies key opportunities including automated tracking, investment guidance, fraud detection, and financial literacy enhancement."
  - "Identifies key challenges: data privacy, algorithmic bias, overreliance on AI, regulatory gaps, and user trust issues."
  - "Suggests recommendations such as enhanced security, bias auditing, transparency via XAI, regulatory frameworks, and human-AI collaboration."
  - "Synthesizes findings from prior studies to provide a balanced overview."
findings:
  - "AI-powered apps like Mint and YNAB automate spending tracking and categorization."
  - "Robo-advisors provide data-driven, low-cost investment strategies."
  - "Fraud detection using machine learning identifies irregularities in transactions."
  - "Data privacy is a major concern due to access to sensitive financial information."
  - "Algorithmic bias can lead to unfair credit scoring and lending decisions."
  - "Overreliance on AI may reduce users' financial literacy."
  - "Lack of regulatory frameworks raises ethical and accountability concerns."
  - "User trust is hindered by lack of transparency and control."
  - "Combining AI with human advisors can alleviate trust and complexity issues."
  - "Explainable AI is critical for improving transparency and adoption."
key_figures_tables:
  - "None."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "AI"
    definition: "Artificial Intelligence"
  - term: "PFM"
    definition: "Personal Financial Management"
  - term: "XAI"
    definition: "Explainable Artificial Intelligence"
  - term: "GDPR"
    definition: "General Data Protection Regulation"
  - term: "CCPA"
    definition: "California Consumer Privacy Act"
critical_citations:
  - "[Smith and Johnson, 2020] — AI improves budgeting and savings."
  - "[Williams, 2019] — AI financial tools are susceptible to cyber fraud."
  - "[Lee and Kim, 2022] — AI credit scoring can inherit biases."
  - "[Brown, 2020] — Overreliance lowers financial literacy."
  - "[Thompson and White, 2023] — Regulatory challenges in AI finance."
relevance:
  topics:
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "low"
      justification: "Mentions automated categorization in budgeting apps but does not detail frameworks."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "high"
      justification: "Reviews existing AI-powered PFM tools and applications."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Identifies key gaps: data privacy, bias, regulation, and overreliance."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "low"
      justification: "Mentions predictive analytics for expense forecasting but lacks algorithmic detail."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "low"
      justification: "Discusses automated budgeting but not specific strategies."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "low"
      justification: "Mentions personalized budgeting advice but no recommendation algorithm."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses fraud detection as an application of anomaly detection."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "medium"
      justification: "Mentions machine learning models for detecting irregularities."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "Data privacy and security are major challenges discussed in detail."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "high"
      justification: "User trust and transparency are key barriers to adoption discussed."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "medium"
      justification: "Discusses automated savings apps and goal-based planning."
  contribution: "This paper provides a broad overview of AI-based PFM, highlighting both opportunities and challenges that inform Odin's design decisions regarding automation, privacy, and user trust. The identified challenges, such as algorithmic bias and data security, directly justify Odin's need for transparent and secure systems. The review of existing tools suggests features like automated categorization and fraud detection that Odin can incorporate. The discussion on overreliance underscores the importance of balancing AI with user education. The lack of regulation reinforces the need for Odin to adopt ethical AI practices."
  directly_justifies:
    - "AI-powered budgeting apps can automate spending categorization."
    - "Data privacy is a critical concern for AI financial tools."
    - "Algorithmic bias can lead to unfair financial outcomes."
    - "Overreliance on AI may reduce user financial literacy."
    - "Regulatory frameworks for AI in finance are currently lacking."
  limits:
    - "Not specific to Filipino young professionals."
    - "Does not provide empirical evaluation of AI algorithms."
    - "Lacks detailed implementation guidance for system design."
    - "Focuses on general challenges without proposing novel solutions."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains flagged as relevant include Expense Categorization (3.A, low), Existing Systems & Gaps (4.A high, 4.B high), Spending Forecasting (6.A low), Budget Recommendation (7.A low, 7.B low), Anomaly Detection (8.A medium, 8.B medium), Data Privacy & User Trust (10.A high, 10.B high), and Savings & Debt Management (13.A medium). Borderline cases: the discussion on fraud detection touches both anomaly detection and security, but we assigned to anomaly detection because it explicitly mentions machine learning for irregularity detection; the discussion on budgeting touches both strategy and recommendation, but as low due to lack of specificity. Domains/topics considered and rejected: Filipino cultural context (1.A, 2.A, etc.) because the paper is international; Mobile-First Design (9.A, 9.B) because mobile UX is not discussed; System Evaluation (12.A, 12.B, 12.C) because no evaluation methodologies are mentioned; Behavioral Profiling (5.A, 5.B, 5.C) because no profiling is discussed. Overall, the paper is highly relevant for understanding the landscape and challenges of AI in PFM, providing justification for Odin's focus on privacy, trust, and transparent algorithms."
limitations:
  - "Limited to a literature review with no primary data. [unacknowledged]"
  - "Does not address specific algorithmic choices for implementation. [unacknowledged]"
  - "Not tailored to the Filipino financial context. [unacknowledged]"
  - "Recommendations are high-level and lack actionable details. [unacknowledged]"
remember_this:
  - "AI automates spending tracking and budgeting tasks."
  - "Data privacy and security are critical challenges for AI in finance."
  - "Algorithmic bias can perpetuate financial exclusion."
  - "Regulatory frameworks for AI in personal finance are lacking."
  - "Human-AI collaboration enhances financial decision-making."
```
---

## Paper 3: Misiurek et al_summarized.md

**Source File:** `Misiurek et al_summarized.md`

```yaml
paper_id: 10.3390/en18154032
designation: international
title: Review of Methods and Models for Forecasting Electricity Consumption
authors: Misiurek, K.; Olkuski, T.; Zyśk, J.
year: 2025
venue: Energies
odin_topics:
  - 6.A
  - 6.B
  - 8.C
  - 12.A
  - 12.B
tldr: A structured review of electricity load forecasting methods categorizes models by time horizon and evaluates classical statistical, machine learning, and deep learning techniques.
problem_and_motivation: Accurate electricity load forecasting is critical for grid stability and cost reduction, but the increasing complexity from renewable integration and variable consumption patterns challenges existing methods. A systematic comparison across time horizons is needed to guide model selection for different operational and strategic planning contexts.
approach:
  - A comprehensive literature review categorizes forecasting methods into very short-term, short-term, medium-term, and long-term horizons.
  - Classical statistical models (ARIMA/SARIMA, exponential smoothing, linear regression) are contrasted with modern AI techniques (ANN, LSTM, CNN, Transformer).
  - The review synthesizes findings from recent studies and evaluates methods based on input data, forecast horizon, and accuracy metrics (e.g., MAPE, RMSE).
  - A comparative analysis is provided for each time horizon, summarizing the advantages and limitations of each approach in tabular form.
  - The paper concludes with a mapping of forecasting methods to data types and applications.
findings:
  - num: LSTM models show high effectiveness for very short-term forecasting, achieving up to a 10-15% improvement in RMSE over traditional ML models for residential loads.
  - num: Hybrid CNN-LSTM models reduce MSE significantly, achieving values as low as 0.3738, by extracting spatial and temporal features.
  - num: Transformer-based models demonstrate comparable accuracy to RNNs but are up to five times faster in inference, with RMSE near 2.0 for short-term forecasts.
  - num: Hybrid statistical and machine learning models can achieve high accuracy (96.83%) for national-level hourly forecasting over a two-year period.
  - Classical ARIMA models remain competitive for structured seasonal data, often outperforming more complex models in data-scarce environments.
  - The study confirms that no universal forecasting approach exists and that hybrid models combining interpretability with high accuracy are a key research need.
key_figures_tables:
  - Table 1: Summary of very short-term load forecasting methods → Compares IT-1FIS, LSTM, CNN-LSTM, and Transformer models.
  - Table 2: Summary of short-term load forecasting methods → Details ARIMA, ANN, hybrid, and GAM models.
  - Table 3: Summary of medium-term load forecasting methods → Presents ARIMA, ANN, hybrid, and Grey models.
  - Table 4: Summary of long-term load forecasting methods → Reviews regression, ANN, LSTM, and Bayesian models.
  - Table 5: Mapping of forecasting methods to data types and applications → Connects model families to specific operational contexts.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: ARIMA
    definition: AutoRegressive Integrated Moving Average, a classical time-series forecasting model.
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network architecture for sequence prediction.
  - term: CNN
    definition: Convolutional Neural Network, a deep learning model for feature extraction.
  - term: MAPE
    definition: Mean Absolute Percentage Error, a common forecast accuracy metric.
  - term: RMSE
    definition: Root Mean Square Error, a common forecast accuracy metric.
critical_citations:
  - "[Azeem et al., 2021] — Provides categorization of electrical load forecasting."
  - "[Klyuev et al., 2022] — Reviews methods for forecasting electric energy consumption."
  - "[Singh et al., 2019] — Quantifies economic impact of forecasting error."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: contextual
      justification: Provides foundational concepts of predictive modeling but focused on electricity, not PFMS.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: contextual
      justification: Reviews algorithms (LSTM, Transformer) applicable to time-series forecasting for general sequential data.
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: low
      justification: Discusses data scarcity issues relevant to cold-start contexts but not directly in anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: low
      justification: Discusses model evaluation metrics (MAPE, RMSE) relevant to any forecasting system evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: low
      justification: Compares model performances, analogous to evaluating algorithmic modules.
  contribution: The paper offers a systematic taxonomy of forecasting methods by time horizon, which can inform the selection of algorithms for predicting financial inflows and outflows. The comparison of statistical and deep learning techniques highlights trade-offs between interpretability and accuracy, guiding module design for forecasting in Odin. The discussion of data variability and external factors is relevant for handling irregular spending patterns. The review's structured evaluation approach provides a methodological reference for assessing Odin's own forecasting modules.
  directly_justifies:
    - LSTM models are effective for capturing complex temporal dependencies in high-volatility data.
    - Hybrid models combining statistical and machine learning techniques often provide superior forecasting accuracy.
    - No universal forecasting method exists; model selection must be tailored to the specific data and forecast horizon.
  limits:
    - Focuses exclusively on electricity consumption, not personal financial transaction data.
    - Does not provide implementation details or code for the reviewed methods.
    - Does not address user privacy, interpretability, or user trust in the context of personal finance. [unacknowledged]
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. This paper is primarily a review of forecasting methods in the energy sector. Domains related to Filipino cultural context, expense categorization, existing systems, behavioral profiling, budget recommendation, anomaly detection, mobile design, privacy, retention, savings, and debt were all considered and rejected as they are outside the paper's scope. Topics under 'Predictive Modeling & Forecasting' (6.A, 6.B) were flagged as 'contextual' because the paper reviews algorithms and modeling concepts that are domain-agnostic and could be relevant to financial forecasting. Topic 8.C (Cold-Start Baseline Strategies) was given 'low' relevance due to the paper's discussion of data scarcity challenges. Topics 12.A and 12.B (Evaluation) were also noted as 'low' relevance for their discussion of general model evaluation metrics and approaches. The paper does not offer direct, actionable insights for Odin's specific financial domain but provides foundational knowledge on forecasting techniques. Overall relevance is low but provides a methodological starting point.
limitations:
  - Focuses exclusively on electricity consumption, not personal financial transaction data.
  - Does not provide implementation details or code for the reviewed methods.
  - Does not address user privacy, interpretability, or user trust in the context of personal finance. [unacknowledged]
remember_this:
  - The choice of forecasting model is highly dependent on the time horizon and data characteristics.
  - Hybrid models combining statistical and machine learning techniques often outperform standalone approaches.
  - Deep learning models like LSTM and Transformer are effective but require large datasets and computational resources.
  - Evaluation metrics like MAPE and RMSE are standard for comparing forecasting model performance.
```
---

## Paper 4: Praveen et al_summarized.md

**Source File:** `Praveen et al_summarized.md`

```yaml
paper_id: e8a6b3e8-0b4d-563b-9f1f-8c1f5a4b9c7d
designation: international
title: Enhancing Financial Literacy and Personal Investment Decisions Through AI and Machine Learning
authors: Praveen, R.V.S.; Vemuri, H.K.; Peri, S.S.S.R.G.; Sista, S.; Saxena, V.; Saxena, P.
year: 2025
venue: Journal of Marketing & Social Research
odin_topics:
  - 1.C
  - 2.D
  - 5.A
  - 6.A
  - 7.A
  - 8.A
  - 9.A
  - 10.A
  - 11.A
  - 12.A
tldr: AI and machine learning tools significantly improve financial literacy and investment confidence by providing personalized, interactive, and data-driven insights for individual financial decision-making.
problem_and_motivation: Many individuals lack the financial literacy needed to make sound investment decisions, leading to mismanagement and insecurity. Traditional financial education has largely failed to produce lasting behavioral changes. AI and ML offer a scalable way to bridge this knowledge gap by providing personalized and accessible financial guidance.
approach:
  - A mixed-methods approach combined a tool analysis of 20 AI financial platforms with a survey of 524 users and 33 qualitative interviews.
  - The study assessed financial literacy using adapted OECD/INFE core competencies and measured investment confidence on a 5-point Likert scale.
  - Quantitative analysis used paired t-tests, regression, and cluster analysis in SPSS and Python to evaluate literacy score changes and behavioral impacts.
  - Qualitative data from interviews was thematically analyzed using NVivo to extract themes on trust, usability, and learning outcomes.
  - The research design included pre- and post-intervention measurements to directly compare the effect of AI tool usage on financial knowledge.
findings:
  - "num: Participants showed a statistically significant mean increase of 1.1 points in financial literacy scores on a 10-point scale (p < 0.01)."
  - "num: Over 65% of users reported high post-intervention investment confidence, rating themselves at level 4 or 5."
  - "num: A moderate positive correlation (r = 0.31) was observed between AI engagement levels and literacy score gains."
  - "num: Users with high AI engagement (71-100 range) achieved a mean score gain of 1.38, compared to 0.72 for low engagement users."
  - "num: Frequent users with more than 5 weekly sessions experienced an average literacy gain of 1.46 points."
  - AI-driven tools act as effective educational supplements by providing personalized and interactive learning environments.
  - Higher engagement and usage frequency are key predictors of greater learning outcomes and behavioral improvement.
  - Investment confidence improved notably, particularly for frequent users of AI financial tools.
key_figures_tables:
  - "Table 2: Participant demographics → Shows the sample was predominantly younger (26-35), educated, and experienced with AI tools."
  - "Table 4.1: Financial Literacy Score Summary → Literacy scores improved from a mean of 5.5 to 6.6 post-AI tool use."
  - "Table 4.2: Investment Confidence Ratings → 65.1% of participants reported confidence levels of 4 or 5 after using AI tools."
  - "Table 4.3: Correlation Matrix → Positive correlations among AI engagement, usage frequency, and literacy scores (r up to 0.44)."
  - "Figure 3: Engagement vs Score Gain → Higher AI engagement correlates with a greater improvement in literacy scores."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "AI"
    definition: "Artificial Intelligence"
  - term: "ML"
    definition: "Machine Learning"
  - term: "FinTech"
    definition: "Financial Technology"
  - term: "XAI"
    definition: "Explainable Artificial Intelligence"
critical_citations:
  - "[Fernandes, Lynch, & Netemeyer, 2014] — Found financial literacy significantly affects financial behaviors."
  - "[Gupta and Lopez, 2020] — Demonstrated reinforcement learning optimizes portfolio selection based on user risk preferences."
  - "[Williams and Das, 2019] — Highlighted robo-advisors as a disruptive, accessible innovation."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: contextual
      justification: Discusses general financial behavior and decision-making challenges relevant to this demographic.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Does not specifically address Filipino spending cycles but notes AI can identify spending patterns.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Discusses how AI-driven tools can influence user financial behavior and decision-making confidence.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly evaluates the use of predictive analytics and ML models for investment forecasting.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Mentions AI budgeting assistants that use pattern recognition, which relates to budgeting strategies.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: AI tools for risk assessment are mentioned, which is tangentially related to anomaly detection.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: contextual
      justification: The study focuses on digital tools, but does not specifically analyze mobile-first design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Actively addresses data privacy and algorithmic transparency as key concerns for AI adoption.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: Provides empirical data on how AI engagement and usage frequency correlate with positive financial outcomes.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: contextual
      justification: The mixed-methods study provides a framework for evaluating AI tools but is not the paper's primary focus.
  contribution: "This paper provides empirical evidence that AI-powered tools can enhance financial literacy and investment confidence, justifying the development of similar modules in Odin. It validates the use of predictive analytics and personalized feedback to improve user engagement and decision-making. The findings support Odin's design for interactive, data-driven financial education. The study's mixed-methods approach offers a template for evaluating the effectiveness of Odin's algorithmic modules. It underscores the importance of addressing ethical concerns like transparency to build user trust."
  directly_justifies:
    - "AI-driven financial tools significantly improve financial literacy scores."
    - "Higher AI engagement correlates with greater learning outcomes and investment confidence."
    - "Frequent use of AI financial platforms is a strong predictor of knowledge gain."
    - "Users show a high receptiveness to AI as a co-pilot in financial planning."
  limits:
    - "Sample was primarily digitally literate, which may not reflect the experiences of older or tech-averse demographics."
    - "Financial literacy and confidence were assessed shortly after engagement, not long-term. [unacknowledged]"
    - "Confidence levels and some usage statistics were self-reported, which could introduce response bias. [unacknowledged]"
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The study's core contribution to predictive modeling and user engagement flagged topics 6.A and 11.A as high relevance. Domains 5.A (behavioral profiles), 10.A (data privacy), and 7.A (budgeting) were assessed as medium relevance, as the paper provides supporting evidence but not a core contribution. Topic 1.C and 9.A were marked contextual, as the study focuses on general users, not specifically Filipino young professionals, and does not address mobile design specifically. Topics like 2.A (cultural practices), 3.A (categorization), and 13.A (savings) were rejected as they are not addressed. The study is broadly relevant to Odin for its empirical validation of AI's educational and behavioral impact, though it is international and non-algorithmic in its primary contribution."
limitations:
  - "Sample was primarily digitally literate, not reflecting the experiences of older or tech-averse demographics. [unacknowledged]"
  - "Financial literacy and confidence were assessed shortly after engagement; long-term retention and behavior were not measured. [unacknowledged]"
  - "Self-reported confidence and some usage metrics may introduce response bias. [unacknowledged]"
remember_this:
  - "AI tools increased financial literacy scores by an average of 1.1 points."
  - "Over 65% of users reported high investment confidence after using AI tools."
  - "Higher AI engagement directly correlates with better learning outcomes."
  - "Frequent platform use is a strong predictor of financial knowledge gains."
  - "Responsible AI integration requires attention to transparency and data privacy."
```
---

## Paper 5: Felbermayr et al_summarized.md

**Source File:** `Felbermayr et al_summarized.md`

```yaml
paper_id: e4b96a7c-7c2e-5f4a-9d1c-1f3a5f2e1b9d
designation: international
title: OeNB Financial Literacy Evaluation Series – Collected Articles from 2024–2025
authors: Felbermayr, K.; Kaczkó, É.; Lorenz, T.; Mauser, S.; Voith, V.; Zieser, M.; Anyfantaki, S.
year: 2025
venue: Oesterreichische Nationalbank Financial Literacy Evaluation Series
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.C
  - 2.D
  - 3.A
  - 3.B
  - 3.C
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 7.C
  - 7.D
  - 8.A
  - 8.B
  - 8.C
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 12.A
  - 12.B
  - 12.C
tldr: A multi-article series synthesizing financial literacy research, pedagogical frameworks, and evaluation methodologies to guide rigorous assessment of financial education programs across diverse populations and contexts.
problem_and_motivation: Financial literacy research and education are fragmented by inconsistent definitions, measurement approaches, and evaluation standards. Policymakers and practitioners lack cohesive guidance to design, implement, and assess interventions that demonstrably improve financial behavior and well-being.
approach:
  - Reviews conceptual evolution of financial literacy across OECD, World Bank, and national strategies.
  - Conducts thematic review of 68 (quasi-)experimental impact evaluations from 2010-2024.
  - Proposes pedagogical continuum from individual- to socially-oriented financial education.
  - Provides guidelines for process and impact evaluation, including theory of change development.
  - Details qualitative (interviews, focus groups, observation) and quantitative (survey, statistical inference) methods.
  - Outlines mixed-methods integration techniques for comprehensive evaluation.
findings:
  - "num: financial education interventions consistently improve short-term financial knowledge across contexts."
  - "num: evidence on behavior and attitude change remains mixed and dependent on intervention design."
  - School-based programs show robust knowledge gains but limited behavioral impact without experiential elements.
  - Adult interventions for vulnerable groups show short-term improvements, but long-term effects are uncertain.
  - Digital and nudge-based approaches can enhance engagement and behavior but require careful design.
  - Causal mechanisms linking financial literacy to well-being remain largely unestablished.
key_figures_tables:
  - "Table 1: Theory of change components → illustrates inputs, activities, outputs, and outcomes framework."
  - "Chart 1: ISAFL vs S&P survey comparison → shows low correlation between different financial literacy assessments."
  - "Figure 1: Evaluation cycle → visualizes four-phase process from planning to communication."
  - "Table 10: Qualitative analysis methods → categorizes enumerative, descriptive, hermeneutic, explanatory approaches."
key_equations:
  - equation: "SE = s / √n"
    explanation: "Standard error of the mean decreases with larger sample size."
  - equation: "t = (x̄ - μ) / SE"
    explanation: "t-statistic tests if sample mean differs from a hypothesized population mean."
  - equation: "r = Cov(x,y) / (s_x * s_y)"
    explanation: "Correlation coefficient measures linear association between two variables."
definitions:
  - term: "Financial literacy"
    definition: "Combination of financial awareness, knowledge, skills, attitudes, and behaviors to make sound financial decisions and achieve financial well-being."
  - term: "Theory of change"
    definition: "Logical, sequential argument for how and why an intervention will deliver desired results, including underlying assumptions."
  - term: "Impact evaluation"
    definition: "Assessment of the causal effect of a program on outcomes, measuring attribution and magnitude of change."
  - term: "Process evaluation"
    definition: "Examination of program implementation, delivery, and mechanisms to understand how and why it works."
  - term: "Mixed methods"
    definition: "Research combining qualitative and quantitative elements for breadth, depth, and integration of understanding."
  - term: "Sampling bias"
    definition: "Systematic error in sample statistics due to nonrandom selection, not reduced by increasing sample size."
critical_citations:
  - "[Fernandes et al., 2014] — meta-analysis shows financial education effects decay over time."
  - "[Kaiser et al., 2022] — randomized experiments confirm positive but modest behavioral effects."
  - "[Lusardi & Mitchell, 2014] — seminal framework defining financial literacy around knowledge and decision-making."
  - "[Biesta, 2010] — foundational educational philosophy distinguishing qualification, socialization, and subjectification functions."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: Provides general frameworks adaptable to Filipino context, but no specific Filipino data.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Discusses income, debt, and saving patterns relevant to financial management for young adults.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Reviews behavioral determinants and outcomes applicable to understanding Filipino financial habits.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: Mentions cultural norms and social context as factors influencing financial literacy, but not specific to Filipino culture.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: References inflation and economic cycles, but does not explicitly address seasonal spending.
    - code: 2.C
      name: User-Declared Financial Preferences
      relevance: low
      justification: Discusses attitudes and behaviors, but not specifically user-declared preferences.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: No direct mention of Filipino-specific occasions or spending cycles.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Reviews frameworks like OECD/INFE and World Bank approaches for categorizing financial behavior and knowledge.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: high
      justification: Discusses design of survey instruments and measurement of financial literacy components.
    - code: 3.C
      name: User-Defined Allocation Constraints
      relevance: medium
      justification: Mentions constraints in budgeting and financial management, relevant to user-defined allocations.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Comprehensive review of existing financial education programs and evaluation systems globally.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies gaps in evaluation rigor, definitional inconsistency, and integration of qualitative methods.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Discusses behavioral profiles and their implications for financial literacy and intervention design.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: Addresses dynamics of behavior change and challenges in initial assessment.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Reviews classification methods including those used by OECD and World Bank.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Discusses forecasting and predictive aspects of financial behavior and knowledge.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: General discussion of data analysis, but not specific forecasting algorithms.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Reviews effectiveness of budgeting and financial planning interventions.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Discusses recommendation logic through evaluation of intervention outcomes.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: low
      justification: No specific focus on optimization approaches.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: low
      justification: Not addressed.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Discusses behavioral deviations and detection through evaluation studies.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: No specific algorithm discussion.
    - code: 8.C
      name: Cold‑Start Baseline Strategies for Anomaly Detection
      relevance: low
      justification: Not addressed.
    - code: 9.A
      name: Mobile‑First Design Principles and Rationale
      relevance: medium
      justification: Discusses digital delivery modes and implications for accessibility and engagement.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Reviews digital and mobile interventions, emphasizing user experience and adoption.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Dedicated section on GDPR compliance and data protection in evaluation research.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Mentions trust as a factor in financial literacy and institutional engagement.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: Reviews engagement through intervention design, incentives, and participant retention.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: high
      justification: Discusses strategies like gamification, personalization, and behavioral nudges for retention.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Entire series is dedicated to evaluation frameworks for financial literacy and education.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Reviews quantitative and mixed-methods approaches applicable to algorithm evaluation.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Discusses methods relevant for evaluating recommendation and intervention effectiveness.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Reviews interventions targeting saving behavior and goal setting.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: medium
      justification: Discusses debt management interventions and their evaluation.
    - code: 13.C
      name: End‑of‑Period Surplus as a Savings Input
      relevance: low
      justification: Not directly addressed.
  contribution: The OeNB Financial Literacy Evaluation Series provides a comprehensive methodological toolkit for designing, implementing, and evaluating financial education interventions. It synthesizes conceptual definitions, pedagogical frameworks, and evaluation designs – including qualitative, quantitative, and mixed-methods approaches – which directly inform Odin's modules for expense categorization, behavioral profiling, forecasting, budget recommendation, and anomaly detection. The series also provides critical guidance on data privacy, user engagement, and mobile-first design principles essential for a PFMS targeting young professionals.
  directly_justifies:
    - "Financial education interventions consistently improve short-term financial knowledge across diverse populations and contexts."
    - "Evaluation designs must integrate both process and impact assessment to understand causal mechanisms and effectiveness."
    - "Data privacy and ethical considerations are paramount in personal finance research, requiring compliance with GDPR-like frameworks."
    - "Mixed-methods approaches enhance the depth and reliability of evaluation findings by combining statistical analysis with contextual insights."
  limits:
    - "The synthesis is based on international studies (OECD countries) and may not fully account for specific Filipino cultural and economic contexts."
    - "Implementation of recommended methods may require specialized skills and resources not always available in low- or middle-income settings."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was conducted. The highest relevance (high) was assigned to topics directly addressed by the series' core focus on evaluation methodology (3.A, 3.B, 4.A, 4.B, 5.A, 5.C, 7.A, 9.A, 10.A, 11.A, 11.B, 12.A, 12.B, 12.C). Medium relevance was given to topics that provide supporting evidence or contextual frameworks (1.A, 1.B, 1.C, 3.C, 5.B, 6.A, 7.B, 8.A, 9.B, 10.B, 13.A, 13.B). Low or contextual relevance was assigned where the paper only tangentially touches a topic (2.A, 2.B, 2.C, 2.D, 6.B, 7.C, 7.D, 8.B, 8.C, 13.C). Borderline cases included topics on seasonal spending (2.B, 2.D) where the paper discusses cyclical behavior but not specifically Filipino patterns; and topics on constrained optimization (7.C) or anomaly algorithms (8.B) where the paper focuses on evaluation design rather than algorithmic specifics. Overall, the series is highly relevant to Odin's design and evaluation needs, offering validated methods and frameworks for building and assessing PFMS functionalities.
limitations:
  - "Findings are based on OECD country studies and may not generalize to low- and middle-income contexts without adaptation. [unacknowledged]"
  - "The series emphasizes evaluation of existing programs but provides limited guidance on developing original intervention content. [unacknowledged]"
  - "Practical implementation of rigorous evaluation designs may be constrained by resource limitations in real-world settings. [unacknowledged]"
remember_this:
  - "Financial education consistently improves knowledge but effects on behavior are weaker."
  - "Mixed-methods evaluation provides the most robust and actionable insights for program improvement."
  - "Theory of change frameworks are essential for aligning program design with measurable outcomes."
  - "Data privacy and research ethics must be integrated into every stage of evaluation."
  - "Qualitative methods reveal causal mechanisms often missed by quantitative analysis alone."
```
---

## Paper 6: Rodriguez-Correa et al_summarized.md

**Source File:** `Rodriguez-Correa et al_summarized.md`

```yaml
paper_id: 10.12688/f1000research.159085.3
designation: international
title: Financial literacy among young college students: Advancements and future directions
authors: Rodriguez-Correa, P. A.; Arias García, S.; Bermeo-Giraldo, M. C.; Valencia-Arias, A.; Martínez Rojas, E.; Aurora Vigo, E. F.; Gallegos, A.
year: 2025
venue: F1000Research
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.C
  - 3.A
  - 3.C
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 7.A
  - 8.A
  - 9.A
  - 9.B
  - 10.A
  - 11.A
  - 12.A
tldr: A systematic review of 44 studies identifies financial knowledge and behavior as dominant but unevenly explored themes among college students, with gaps in budgeting, credit, and fintech.
problem_and_motivation: Young adults face increasing financial responsibilities and are vulnerable to poor financial decisions. Existing research on financial literacy for this group is fragmented and focuses on broad categories. A structured overview of specific subtopics is needed to guide educational and policy interventions.
approach:
  - A systematic literature review was conducted following the PRISMA-2020 methodology.
  - The search was performed in Scopus and Web of Science using title-specific keywords.
  - Inclusion criteria required studies on higher education students with statistical analysis of financial literacy variables.
  - A quality assessment checklist scored documents from 1 to 3, with only score 3 included.
  - The analysis synthesized data from 44 peer-reviewed studies published between 2003 and 2023.
findings:
  - num: 44 peer-reviewed studies were analyzed, with 34% using regression analysis.
  - Financial literacy is the most evaluated construct, but its definition varies widely across studies.
  - Financial knowledge and financial behavior are the most frequently examined themes.
  - Budgeting, credit/debt management, and fintech adoption are underexplored subtopics.
  - Socio-demographic variables like gender and parental education are commonly measured but cultural factors are often overlooked.
  - Financial self-efficacy emerges as a key moderating factor between knowledge and behavior.
  - The literature shows a shift towards broader concepts like financial capability and financial well-being.
  - Emerging economies and Eastern Europe are identified as underrepresented regions in research.
  - The relationship between fintech and financial literacy is identified as a major research gap.
  - A future research agenda highlights financial knowledge, behavior, inclusion, and budgeting as key areas.
key_figures_tables:
  - Figure 1: PRISMA flow diagram showing selection of 44 studies from 350 initial records → Systematic process yielded 44 relevant studies.
  - Figure 2: Bar chart showing most recurring financial literacy variables → Financial literacy, knowledge, and behavior are the top three constructs.
  - Figure 3: Research agenda with keyword trends → Financial knowledge and behavior are currently active and future topics.
  - Table 2: Summary of 44 studies with objectives, methods, and countries → Regression analysis and SEM are dominant methods.
  - Table 3: Research gaps categorized by theme, geography, and temporality → Social class, fintech impact, and emerging markets need study.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Financial Literacy
    definition: The ability to understand and manage personal finances, including budgeting, saving, and using credit responsibly.
  - term: Financial Knowledge
    definition: Familiarity with financial terms and concepts needed for daily financial functioning.
  - term: Financial Behavior
    definition: Actions and patterns exhibited by individuals in managing their financial resources.
  - term: Financial Attitude
    definition: An individual's state of mind, opinion, and judgment regarding financial decisions.
  - term: Financial Self-Efficacy
    definition: Confidence in one's ability to acquire information and make effective financial decisions.
critical_citations:
  - "[Lusardi & Mitchell, 2023] — Defines financial literacy's core concepts and importance."
  - "[Xiao et al., 2022] — Introduces financial capability as an expanded framework."
  - "[Blanco et al., 2024] — Highlights social determinants and disparities in financial knowledge."
  - "[Bartholomae & Fox, 2021] — Reviews college student financial behavior and well-being."
  - "[Goyal & Satish, 2021] — Provides a systematic review and bibliometric analysis of financial literacy."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Focuses on college students, a key sub-demographic of young professionals.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: contextual
      justification: Discusses income sources (scholarships, jobs) and financial responsibilities.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Directly reviews financial behavior patterns in college students.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: Mentions cultural norms but lacks specific focus on Filipino practices.
    - code: 2.C
      name: User-Declared Financial Preferences
      relevance: low
      justification: Addresses financial attitudes and self-efficacy, not explicit user preferences.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: low
      justification: Discusses budgeting but not specific categorization frameworks.
    - code: 3.C
      name: User-Defined Allocation Constraints
      relevance: low
      justification: Mentions budgeting but not user-defined constraints.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Reviews the literature but not specific existing systems.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Systematically identifies research gaps in financial literacy for college students.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Reviews financial behavior as a key variable.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: low
      justification: Does not address profile dynamics or cold-start issues.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Does not focus on classification approaches.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: contextual
      justification: Mentions predictive approaches but not specific modeling.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Highlights budgeting as a core thematic gap.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: No direct mention of anomaly detection.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: contextual
      justification: Mentions fintech and digital tools but not mobile-first design specifically.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: contextual
      justification: Mentions fintech and digital tools but not UX design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: No direct mention of data privacy.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: Mentions behavior but not engagement dynamics.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: low
      justification: Discusses review methodology but not system evaluation.
  contribution: This paper provides a systematic overview of financial literacy research relevant to young professionals, which can inform Odin's design by identifying key behavioral and knowledge domains. The identification of research gaps in budgeting, credit, and fintech use directly justifies the need for Odin's features in these areas. The findings on financial behavior and attitudes can guide the development of behavioral profiling modules. The paper's emphasis on digital tools and financial self-efficacy supports the rationale for a mobile-first, user-empowering PFMS.
  directly_justifies:
    - "Budgeting skills are a recurring theme, but students are least interested in this process."
    - "Students with low financial knowledge may misuse credit cards and incur uncontrollable debt."
    - "Financial self-efficacy emerges as a moderating factor between knowledge and behavior."
    - "There is a gap in assessing the actual effectiveness of digital financial tools in improving literacy."
    - "Gender, parental education, and income significantly influence financial literacy levels."
  limits:
    - "The search was limited to Scopus and Web of Science, possibly excluding relevant studies."
    - "Search terms were restricted to titles, potentially missing studies using different keywords."
    - "The review focuses primarily on financial literacy and may not fully capture financial capability/wellbeing."
    - "The use of specific bibliometric tools may have constrained the analysis."
    - "The search did not include related terms like 'financial knowledge' or 'financial skills'."
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The paper was flagged as relevant primarily for domains related to Behavioral Profiling & Classification, Existing Systems & Gaps, and Budget Recommendation. Topic codes 1.A, 1.B, 1.C, 2.A, 2.C, 3.A, 3.C, 4.A, 4.B, 5.A, 7.A, 9.A, and 9.B were assigned medium or contextual relevance because the paper provides foundational evidence on demographics, behavior, and system gaps but does not directly address Odin's algorithmic or design specifics. Codes 6.A, 8.A, 10.A, 11.A, and 12.A were considered low or contextual as the paper does not cover predictive modeling, anomaly detection, privacy, or engagement mechanics. The borderline case of 2.A (cultural practices) was marked contextual due to the lack of a specific Filipino focus. The overall relevance to Odin is medium, providing a strong literature foundation for several modules, especially behavioral profiling and identifying system gaps.
limitations:
  - "The search strategy was limited to Scopus and Web of Science."
  - "Only titles were searched, not abstracts or full texts."
  - "The review covers up to 2023, missing very recent studies."
  - "Related terms like 'financial knowledge' were not included in the initial search."
  - "Only documents with a score of 3 (correlational studies) were included, excluding descriptive works."
  - "The search did not include 'University' or 'College' as separate terms in the title search."
  - "Potential language bias exists as only English articles were included."
remember_this:
  - "Financial literacy definitions vary widely across studies."
  - "Budgeting, credit, and fintech use are key research gaps."
  - "Financial self-efficacy mediates the knowledge-behavior link."
  - "Gender and parental education significantly influence financial literacy."
  - "The field is shifting from literacy to capability and well-being."
```
---

## Paper 7: Sanhosh & Singh_summarized.md

**Source File:** `Sanhosh & Singh_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international
title: Digital Persona Modeling for Context-Aware Financial Decisioning
authors: Sanhosh, S. R.; Singh, A. K.
year: 2025
venue: International Journal of Research in Mulidisciplinary Technology
odin_topics:
  - 5.A
  - 6.A
  - 9.A
  - 10.A
  - 10.B
  - 7.B
  - 8.A
  - 1.A
  - 2.A
  - 2.B
  - 3.A
  - 4.A
  - 4.B
  - 12.A
  - 12.B
  - 13.A
tldr: Digital Persona Modeling integrates behavioral and contextual data to enable adaptive, context-aware financial decisioning systems.
problem_and_motivation: Static demographic profiles are insufficient for addressing real-time and contextual financial needs. There is a need for intelligent systems that can understand and adapt to individual user behaviors and contexts. This paper proposes a digital persona framework to fill this gap.
approach:
  - The system architecture has five layers: Data Acquisition, Context Engine, Persona Builder, Decisioning Model, and Decision Delivery & Feedback.
  - A simulated hybrid dataset was used, combining transactional logs, mobile contextual logs, user profiles, and feedback labels.
  - Random Forest is used for interpretable classification of financial decisions based on contextual features.
  - LSTM Neural Network captures sequential patterns in user behavior for personalized decision-making.
  - K-Means Clustering segments users into distinct persona groups based on contextual traits.
findings:
  - num: LSTM achieved the highest accuracy of 93.6% and F1-score of 92.9%.
  - num: Random Forest achieved 91.2% accuracy and a 90.1% F1-score.
  - num: K-Means Clustering performed lower with 75.0% accuracy and a 71.8% F1-score.
  - The LSTM model's superiority is due to its ability to model temporal dependencies in user behavior.
  - The proposed framework demonstrates that contextual integration improves decision relevance and user alignment.
key_figures_tables:
  - Table 2: Model Performance Comparison → Shows LSTM outperforms Random Forest and K-Means on all metrics.
  - Figure 2: System Architecture of Proposed Framework → Visualizes the five-layer data flow from acquisition to feedback.
key_equations:
  - equation: S(u,p) = (1/n) * Σ_{i=1}^{n} ( |x_{u,i} - x_{p,i}| / max(x_i) )
    explanation: Similarity score matching a user to a persona group.
  - equation: R = α1*C_location + α2*C_time + α3*C_device + β*T
    explanation: Real-time decision risk function based on context and transaction amount.
definitions:
  - term: DPM
    definition: Digital Persona Modeling
  - term: XAI
    definition: Explainable Artificial Intelligence
critical_citations:
  - "[Richardson, 2024] — Foundational for real-time payment system challenges."
  - "[Rautaray & Tayagi, 2023] — Supports AI applications in telecom and finance."
  - "[De Roure, 2024] — Provides basis for AI in industrial and financial IoT."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Core focus on modeling dynamic behavioral profiles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Uses LSTM and other models for predictive financial decisions.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Discusses data from mobile apps and device context.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Addresses privacy via federated learning and local processing.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Highlights explainability and interpretability for trust.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Mentions automated budgeting as a key use case.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Lists fraud intent detection as a use case.
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Mentions underserved entrepreneurs but not Filipino-specific.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: Discusses diversity but not culturally specific practices.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Temporal analysis could inform cyclical patterns.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: Persona modeling could support categorization.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Mentions gaps in static systems.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Explicitly addresses limitations of static profiles.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides a multi-metric evaluation (accuracy, F1, PRL).
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Compares RF, LSTM, and K-Means.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: Mentions investment recommendations tangentially.
  contribution: The paper provides a conceptual and architectural foundation for DPM in intelligent finance. This directly supports Odin's development of dynamic user profiles. The proposed multi-layered architecture can inform Odin's system design for real-time personalization. The privacy-preserving modeling approach using federated learning is relevant to Odin's data governance. The integration of behavioral and contextual data can enhance Odin's decision support modules.
  directly_justifies:
    - Dynamic user profiles can improve financial recommendation relevance.
    - Integrating contextual data enhances real-time financial decision accuracy.
    - Privacy-preserving techniques are essential for user trust in PFMS.
    - LSTM models are effective for capturing sequential spending behaviors.
  limits:
    - The paper uses a synthetic dataset, not real-world data.
    - Model generalizability may be limited across diverse populations.
    - Interpretability challenges remain for deep learning components.
    - Context drift over time is not fully addressed.
    - No specific implementation or deployment details are provided.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. High relevance was found for Behavioral Profiling (5.A) and Predictive Modeling (6.A), as the paper's core is modeling dynamic digital personas for financial decisions. Medium relevance was assigned to Mobile-First Design (9.A) due to its mobile data focus, Data Privacy (10.A) for its emphasis on privacy-preserving modeling, and User Trust (10.B) via explainability. Other topics like 1.A, 2.A, 2.B, 3.A, 4.A, 4.B, 7.B, 8.A, 12.A, 12.B, and 13.A received low, contextual, or medium relevance due to being tangential but cited in the paper. The paper was considered and rejected for topics like 2.C, 3.C, 6.B, 7.A, 7.C, 7.D, 8.B, 8.C, 9.B, 11.A, 11.B, 12.C, 13.B, and 13.C due to a lack of specific discussion on those aspects. Overall, the paper is highly relevant to Odin's goal of building a dynamic user model.
limitations:
  - Data Privacy Concerns: Heavy reliance on sensitive user data increases breach risk. [unacknowledged]
  - Limited Dataset Diversity: Synthetic data may introduce bias and limit generalizability. [unacknowledged]
  - Model Generalizability: Models may not generalize well to unseen patterns in evolving ecosystems. [unacknowledged]
  - Interpretability Challenges: Deep learning models like LSTM can act as black boxes. [unacknowledged]
  - Context Drift Over Time: User behavior evolves, requiring continuous adaptation not fully addressed. [unacknowledged]
remember_this:
  - LSTM achieved the highest accuracy at 93.6% for decision classification.
  - Digital personas enable context-aware adaptation beyond static profiles.
  - Privacy-preserving modeling via federated learning is a key design focus.
  - Multi-source data fusion is essential for creating accurate user personas.
  - The proposed architecture supports real-time, personalized financial decisions.
```
---

## Paper 8: Ramagiri_summarized.md

**Source File:** `Ramagiri_summarized.md`

```yaml
paper_id: 10.5281/zenodo.16883459
designation: international
title: "Tuning AML Detection Rules: A Quantitative Approach to Reducing False Positives"
authors: "Ramagiri, V."
year: 2025
venue: "Sarcouncil Journal of Engineering and Computer Sciences"
odin_topics:
  - 4.A
  - 4.B
  - 8.A
  - 8.B
  - 11.A
  - 11.B
tldr: "A data-driven framework optimizes AML detection rules using statistical calibration, customer segmentation, and predictive modeling to reduce false positive alerts while maintaining risk coverage."
problem_and_motivation: "Financial institutions face overwhelming false positive alerts that consume compliance resources and mask genuine financial crime risks. Existing rules-based systems employ fixed parameters that fail to adapt to changing customer behaviors. A quantitative, data-driven approach is needed to transform monitoring sensitivity and align it with actual risk profiles."
approach:
  - "Applies statistical threshold calibration using kernel density estimation, extreme value theory, and time-series decomposition to improve anomaly detection."
  - "Implements customer segmentation via multivariate clustering (k-means, hierarchical, Gaussian mixture) to enable targeted rule parameterization."
  - "Develops predictive models using random forests, gradient boosting, and deep neural networks to estimate suspicious activity probability."
  - "Uses alert disposition analysis and conversion metrics to assess rule effectiveness and identify improvement opportunities."
  - "Employs backtesting methodologies including historical replay and simulation to validate rule changes before production deployment."
  - "Establishes performance measurement frameworks with survival analysis and risk-based evaluation weights for multidimensional assessment."
  - "Proposes phased implementation strategies starting with lower-risk segments to minimize operational disruption."
  - "Designs cross-functional governance structures with compliance, operations, and technology stakeholders to oversee optimization."
findings:
  - "num: High false positive rates are reported across the financial services industry, creating significant operational burdens."
  - "num: Alert backlogs develop when monitoring systems generate volumes exceeding investigative capacity."
  - "num: Advanced segmentation reveals natural customer groupings not aligned with traditional classifications."
  - "Machine learning models demonstrate superior discrimination capabilities compared to traditional rules-based methods."
  - "Unsupervised anomaly detection identifies novel typologies not captured by existing rules."
  - "Explainable AI techniques address regulatory concerns regarding model interpretability and audibility."
  - "Phased deployment strategies result in higher stakeholder confidence and fewer operational disruptions."
  - "Documentation quality is a primary determinant of both governance effectiveness and regulatory acceptance."
key_figures_tables:
  - "Figure 1: AML False Positive Challenge → Illustrates the operational burden of excessive false positive alerts on compliance teams."
  - "Figure 2: False Positive Challenges in Modern AML Programs → Depicts the multifaceted impact across financial institutions."
  - "Figure 3: Quantitative Methodologies → Shows statistical, segmentation, and machine learning techniques for rule optimization."
  - "Figure 4: Implementation Strategies → Outlines regulatory engagement, documentation, phased deployment, and governance approaches."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "AML"
    definition: "Anti-Money Laundering"
  - term: "SAR"
    definition: "Suspicious Activity Report"
critical_citations:
  - "[Aidoo, 2025] — Evaluates effectiveness of AML regulations and false positive challenge."
  - "[Ketenci, et al., 2021] — Provides time-frequency suspicious activity detection for AML."
  - "[Jensen & Iosifidis, 2023] — Surveys statistics and machine learning for AML monitoring."
  - "[Kuzmenko, et al., 2023] — Applies survival analysis to AML system effectiveness assessment."
  - "[Moromoke, et al., 2024] — Discusses regulatory challenges and operational impacts of false positives."
relevance:
  topics:
    - code: 4.A
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Describes legacy rules-based monitoring systems and their limitations."
    - code: 4.B
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Documents false positive burdens, rigid parameters, and adaptability gaps."
    - code: 8.A
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Directly addresses optimization of detection rules to reduce false positives."
    - code: 8.B
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Reviews statistical and machine learning methods for anomaly detection."
    - code: 11.A
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "contextual"
      justification: "Alert fatigue and high false positives undermine user engagement and trust."
    - code: 11.B
      name: "Retention Mechanisms and Engagement Design"
      relevance: "low"
      justification: "Mentions efficiency improvements but does not directly discuss retention design."
  contribution: "The framework provides a quantitative methodology for tuning detection rules that Odin can adopt for its anomaly detection module. The customer segmentation techniques enable Odin to personalize spending anomaly baselines. The backtesting and phased deployment strategies inform Odin's evaluation and rollout of algorithmic changes. The performance measurement framework, including risk-based weighting, supports Odin's system evaluation and continuous improvement. The principles of reducing false positives are directly applicable to Odin's goal of maintaining user trust through accurate alerts."
  directly_justifies:
    - "Quantitative threshold calibration improves anomaly detection precision compared to arbitrary settings."
    - "Customer segmentation enables personalized rule tuning based on observed spending behavior."
    - "Predictive modeling can estimate the probability of suspicious or anomalous transactions."
    - "Phased implementation with validation controls minimizes disruption during system changes."
    - "Performance measurement must balance efficiency (alert reduction) with risk coverage."
  limits:
    - "The paper focuses on AML compliance in banking, which has different risk thresholds than personal finance."
    - "The proposed machine learning models require labeled alert data, which may not exist for personal spending anomalies."
    - "Regulatory engagement strategies are specific to financial crime compliance, not personal finance apps."
    - "The framework does not address user privacy concerns specific to personal financial data. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper directly supports 'Existing Systems & Gaps' (4.A, 4.B) by describing limitations of rules-based monitoring and the operational burden of false positives. It has high relevance to 'Anomaly Detection' (8.A, 8.B) through its focus on optimizing detection rules and applying quantitative methods to reduce false alerts. The discussion of alert fatigue and compliance resource allocation touches on 'User Retention & Engagement' (11.A) contextually, as excessive false positives undermine user trust and engagement, though it is not directly studied. Domains like 'Filipino Cultural Context' (2.A-D), 'Expense Categorization' (3.A-C), 'Behavioral Profiling' (5.A-C), 'Spending Forecasting' (6.A-B), 'Budget Recommendation' (7.A-D), and 'Mobile-First Design' (9.A-B) were considered but rejected as the paper does not address personal spending, cultural factors, or mobile UX. 'Data Privacy' (10.A-B) and 'Savings & Debt' (13.A-C) are also not covered. The paper offers a high-level framework for reducing false positives that can inform Odin's anomaly detection approach but is not directly applicable to the Filipino context or PFMS specifics."
limitations:
  - "Focuses on AML compliance for financial institutions, not personal finance management. [unacknowledged]"
  - "Assumes access to labeled historical alert data for supervised learning, often unavailable in PFMS. [unacknowledged]"
  - "Lacks empirical validation of the proposed framework in a real-world setting. [unacknowledged]"
  - "Does not address user privacy or data security implications of profiling and anomaly detection."
  - "Regulatory engagement strategies are specific to financial crime, not applicable to consumer apps."
remember_this:
  - "False positive alerts consume substantial compliance resources and mask genuine risks."
  - "Quantitative methods outperform experience-based threshold tuning for anomaly detection."
  - "Customer segmentation enables personalized and more accurate detection rule calibration."
  - "Backtesting and phased deployment are essential for validating rule changes safely."
  - "Performance measurement must balance alert reduction with maintaining risk coverage."
```
---

## Paper 9: Jamal & Hashmat_summarized.md

**Source File:** `Jamal & Hashmat_summarized.md`

```yaml
paper_id: "10.5281/zenodo.15478961"
designation: "international"
title: "Innovations in UI/UX Design of Mobile Applications: Trends, Practices and Challenges"
authors: "Jamal, A.; Hashmat, S."
year: 2025
venue: "Spectrum of Engineering Sciences"
odin_topics:
  - "9.A"
  - "9.B"
  - "11.A"
  - "11.B"
tldr: "A PRISMA-guided review of 20 peer-reviewed studies (2017–2024) synthesizes current trends, best practices, and challenges in mobile UI/UX design."
problem_and_motivation: "Rapid mobile technology advancements have outpaced conventional interface capabilities, creating a gap between user expectations for seamless, intuitive interactions and what standard designs provide. A comprehensive synthesis of emerging trends, best practices, and persistent challenges is needed to guide designers and developers."
approach:
  - "A review methodology guided by the PRISMA framework was employed."
  - "Systematic literature search was conducted across Google Scholar, IEEE Xplore, ACM Digital Library, ScienceDirect, and SpringerLink using Boolean keyword combinations."
  - "Initial screening of 243 records was performed, with duplicates removed leaving 230 unique records for title and abstract screening."
  - "Full-text eligibility assessment of 45 articles against inclusion/exclusion criteria (peer-reviewed, 2017–2024, mobile UI/UX focus) was conducted."
  - "A final set of 20 studies were selected and thematically synthesized into categories: usability, personalization, accessibility, and immersive technologies."
findings:
  - "num: 20 peer-reviewed publications from 2017-2024 were included in the final synthesis."
  - "Key trends include AI-driven personalization, AR/VR integration, Voice User Interfaces, and dark mode/minimalist design."
  - "User-Centered Design (UCD), iterative testing, and performance optimization remain core best practices for mobile UI/UX."
  - "Major challenges include limited screen real estate, cognitive load, cross-platform consistency, and evolving user expectations."
  - "Design thinking and AI-driven automation represent complementary emerging approaches, with hybrid models balancing empathy and efficiency."
  - "Inclusive design features like screen readers and adjustable text sizes are under-prioritized in practice, despite being recognized as essential."
  - "Cross-platform frameworks (Flutter, React Native) are preferred for consistency and scalability but present performance tuning challenges."
  - "Gestural interactions reduce visual clutter and improve task efficiency, though effectiveness depends on user familiarity."
key_figures_tables:
  - "Table 1: Inclusion and Exclusion Criteria → Defines selection parameters for systematic review."
  - "Table 2: Emerging Trends and Approaches → Summarizes key trends and design implications."
  - "Table 3: Design Approaches in Mobile UI/UX → Compares core characteristics and design implications."
  - "Table 4: Best Practices and Implementation → Details core principles and real-world application challenges."
  - "Table 5: Challenges in Mobile UI/UX Practice → Outlines key challenges and their design impact."
  - "Table 6: Implications for Designers and Developers → Provides actionable recommendations for practice."
  - "Table 7: Selected Literature → Lists key studies reviewed, their themes, and publication details."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "AI"
    definition: "Artificial Intelligence."
  - term: "AR"
    definition: "Augmented Reality."
  - term: "ML"
    definition: "Machine Learning."
  - term: "PRISMA"
    definition: "Preferred Reporting Items for Systematic Reviews and Meta-Analyses."
  - term: "UCD"
    definition: "User-Centered Design."
  - term: "UI"
    definition: "User Interface."
  - term: "UX"
    definition: "User Experience."
  - term: "VR"
    definition: "Virtual Reality."
  - term: "VUI"
    definition: "Voice User Interface."
critical_citations:
  - "[Azuma, 1997] — Foundational AR technology survey."
  - "[Krug, 2014] — Established usability heuristics for interfaces."
  - "[Marcotte, 2010] — Originated responsive web design concepts."
  - "[Norman, 2013] — Core principles of user-centered design and everyday usability."
  - "[Shneiderman, 2016] — Established strategies for human-computer interaction design."
relevance:
  topics:
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "high"
      justification: "Paper explicitly discusses mobile-first design as a core principle."
    - code: "9.B"
      name: "Mobile UX Design for Personal Finance"
      relevance: "high"
      justification: "Review synthesizes best practices directly applicable to PFMS UX design."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "medium"
      justification: "Discusses personalization and feedback loops that drive user engagement."
    - code: "11.B"
      name: "Retention Mechanisms and Engagement Design"
      relevance: "medium"
      justification: "Findings on micro-interactions and continuous feedback directly inform retention strategies."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "contextual"
      justification: "Discusses user behavior analysis at a general level, not specific to financial profiles."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "low"
      justification: "Only tangentially mentioned; no substantive discussion on data privacy."
  contribution: "This paper provides a comprehensive, evidence-based framework for mobile UX design that directly supports Odin's mobile-first architecture. Its systematic synthesis of personalization and adaptive interface trends justifies implementing data-driven customization in Odin's dashboard. The identified best practices for iterative testing and user-centered design validate Odin's planned usability testing methodology. The discussion of cross-platform consistency challenges informs Odin's choice of development frameworks. The findings on performance optimization and accessibility are directly relevant to Odin's goal of serving a diverse Filipino user base with varying device capabilities."
  directly_justifies:
    - "A mobile-first design approach is essential for optimizing usability on small screens and ensuring core functionality is accessible."
    - "Implementing personalization and adaptive interfaces enhances user engagement by tailoring content and interactions to individual preferences."
    - "Iterative testing and continuous feedback loops are critical for refining mobile UI/UX and aligning with user expectations."
    - "Addressing challenges such as cognitive load and cross-platform consistency is key to developing effective and inclusive mobile applications."
  limits:
    - "The review is limited to 20 studies, potentially omitting other relevant UI/UX literature."
    - "Findings are qualitative and synthesized thematically, with no quantitative meta-analysis."
    - "Study selection is constrained to publications from 2017-2024, possibly excluding earlier foundational work."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated canonical topic codes was performed. Domains flagged as relevant were Mobile-First Design (9.A, 9.B) with high relevance due to the paper's direct focus on mobile UI/UX principles, and Engagement & Retention (11.A, 11.B) with medium relevance via its discussion of personalization and feedback mechanisms. Behavior Profiling (5.A) was considered contextual, as the paper discusses general user behavior analysis but not financial profiling. Domains like Expense Categorization, Spending Forecasting, Budget Recommendation, Anomaly Detection, Data Privacy, Savings, and Debt Management were rejected as the paper does not address these financial-specific areas. The overall relevance to Odin is high, providing foundational UX best practices essential for its mobile-first design."
limitations:
  - "The review's reliance on a small sample of 20 studies may limit the generalizability of findings."
  - "Lack of quantitative meta-analysis prevents statistical synthesis of effect sizes [unacknowledged]."
  - "The search strategy may have missed grey literature or industry reports not indexed in selected databases [unacknowledged]."
  - "Potential publication bias exists, as only peer-reviewed articles from 2017-2024 were included [unacknowledged]."
remember_this:
  - "Personalization and AR/VR are key trends shaping modern mobile UX."
  - "User-centered design and iterative testing remain essential best practices."
  - "Cross-platform consistency and performance optimization are major design challenges."
  - "Inclusive design features are under-prioritized in practice despite recognized importance."
  - "The review synthesized findings from 20 peer-reviewed studies (2017-2024)."
```
---

## Paper 10: Ranjan et al_summarized.md

**Source File:** `Ranjan et al_summarized.md`

```yaml
paper_id: 10.59256/ijsreat.20250505011
designation: international
title: Online Payment Fraud Detection Using Decission Tree and LSTM Neural Network
authors: Ranjan, A.; Jangir, A.K.; Abrol, K.; Saurav, S.
year: 2025
venue: International Journal of Scientific Research in Engineering & Technology
odin_topics:
  - 8.A
  - 8.B
tldr: A hybrid fraud detection system combines Decision Trees for rapid, interpretable screening with LSTM networks for sequential transaction analysis and temporal pattern recognition.
problem_and_motivation: Online payment fraud is escalating in sophistication, rendering traditional rule-based systems obsolete. There is a critical need for adaptive, data-driven frameworks that can learn evolving fraud patterns. Existing approaches lack the capacity to combine static, interpretable rules with the temporal intelligence required for modern fraud detection.
approach:
  - The study conducts a systematic literature review of machine learning and deep learning techniques for online payment fraud detection.
  - It synthesizes findings from peer-reviewed papers, focusing on Decision Trees, Random Forests, and LSTM neural networks.
  - The review analyzes common preprocessing steps including SMOTE for class imbalance and feature engineering for temporal data.
  - It describes a two-stage hybrid architecture where Decision Trees flag high-risk transactions for subsequent LSTM analysis.
  - The paper evaluates models using standard metrics such as precision, recall, F1-score, and ROC-AUC from the reviewed literature.
findings:
  - Decision Trees and Random Forests provide fast, interpretable baselines for fraud screening, often executing in less than one millisecond per transaction.
  - LSTM networks significantly outperform baseline models by effectively modeling temporal sequences and capturing long-term behavioral changes.
  - Hybrid models combining tree-based methods and LSTMs achieve superior results compared to standalone approaches by leveraging the strengths of each.
  - Addressing class imbalance via SMOTE is critical for improving model sensitivity to fraudulent transactions.
  - Feature engineering, including time-window aggregates and sequential encoding, substantially improves deep learning model accuracy.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network architecture designed to model sequential data and long-term dependencies.
  - term: SMOTE
    definition: Synthetic Minority Oversampling Technique, a method for addressing class imbalance by generating synthetic samples for the minority class.
  - term: ROC-AUC
    definition: Receiver Operating Characteristic - Area Under the Curve, a performance metric for binary classification that measures the model's ability to distinguish between classes.
critical_citations:
  - "[Jurgovsky et al., 2018] — Foundational for LSTM use in fraud detection."
  - "[Roy et al., 2018] — Key comparison of Decision Tree and Random Forest."
  - "[Nashaat and Khorasgani, 2021] — Key hybrid model architecture."
  - "[Fiore et al., 2019] — Key study on LSTM and feature engineering."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Provides general background on fraud as an anomaly detection problem.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Surveys algorithms like LSTM and Decision Trees applicable to anomaly detection.
  contribution: The paper surveys hybrid ML techniques for fraud detection, which could inform Odin's anomaly detection module (8.A, 8.B) for identifying unusual spending patterns. While the context is general online payments, the core algorithms (LSTM, Decision Trees) are transferable to personal finance transaction data. The review of SMOTE and feature engineering offers practical preprocessing strategies that could be adapted for Odin's spending data. The emphasis on real-time processing aligns with Odin's need for responsive anomaly detection.
  directly_justifies:
    - LSTM networks are effective for modeling temporal sequences in transaction data.
    - Hybrid models combining interpretable rules and deep learning achieve superior detection performance.
    - SMOTE is a standard technique to handle class imbalance in fraud detection.
  limits:
    - The paper is a survey and does not present original empirical results or a novel model.
    - The review is specific to fraud detection, which may not directly translate to all aspects of financial anomaly detection for personal budgeting.
    - The focus is on general online payments, not the specific spending patterns of a PFMS user.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The primary domain flagged as relevant was Anomaly Detection, as the paper focuses on a core problem of that domain (fraud identification). Within this domain, topic codes 8.A and 8.B were selected with a 'low' relevance level because the paper provides a broad survey of general algorithms (LSTM, Decision Trees) applicable to anomaly detection, but does not address the specific challenges of a PFMS like Odin. The domain was selected because the foundational concepts of fraud detection, such as identifying outliers and using temporal patterns, are directly transferable. All other functional domains (e.g., Filipino Cultural Context, Expense Categorization, Behavioral Profiling, etc.) were considered and rejected because the paper does not address cultural factors, user financial behavior, budgeting, system evaluation, or any other Odin-specific domain. The paper's focus is purely technical and domain-agnostic, providing only a general algorithmic background that could be a starting point for designing Odin's anomaly detection module but lacks any specific contextual or user-centric insights. Overall, the paper's relevance to Odin is limited to providing a high-level overview of potential algorithmic approaches for anomaly detection.
limitations:
  - The paper is a survey, not a primary research study with novel contributions. [unacknowledged]
  - It does not address the specific characteristics of personal finance data in a PFMS context. [unacknowledged]
  - The review does not cover the integration of anomaly detection with other PFMS modules like budgeting or forecasting. [unacknowledged]
remember_this:
  - Hybrid models combining Decision Trees and LSTMs are effective for fraud detection.
  - LSTM networks excel at capturing temporal patterns in sequential transaction data.
  - SMOTE is a standard technique for handling class imbalance in fraud detection.
  - Decision Trees offer fast, interpretable screening for real-time applications.
```
---

## Paper 11: Siddiqui_summarized.md

**Source File:** `Siddiqui_summarized.md`

```yaml
paper_id: 10.71292/sdmi.v2i01.21
designation: international
title: Optimizing Business Decision-Making through AI-Enhanced Business Intelligence Systems: A Systematic Review of Data-Driven Insights in Financial and Strategic Planning
authors: Siddiqui, N. A.
year: 2025
venue: Strategic Data Management and Innovation
odin_topics:
  - 1.A
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 11.A
  - 12.A
  - 13.A
tldr: AI-enhanced BI systems improve forecasting accuracy by 32-45%, reduce fraud by 47%, and enhance supply chain efficiency by 23% but face challenges in data governance and algorithmic transparency.
problem_and_motivation: Traditional BI systems struggle with real-time data processing and unstructured data integration, limiting their ability to generate actionable insights for dynamic business environments. The increasing complexity of financial markets necessitates AI-powered solutions to enhance decision-making accuracy and efficiency.
approach:
  - A systematic literature review was conducted following PRISMA guidelines across Scopus, Web of Science, IEEE Xplore, ScienceDirect, and Google Scholar.
  - From an initial pool of 2,450 articles, 98 high-quality peer-reviewed studies published between 2012-2024 were selected for final analysis.
  - The review focused on AI-driven BI applications in financial forecasting, fraud detection, customer segmentation, and supply chain optimization.
  - Data extraction and thematic analysis were used to categorize findings and identify research gaps.
findings:
  - num: AI-powered BI improves financial forecasting accuracy by 32-45%.
  - num: AI-driven fraud detection reduces fraudulent transactions by 47% and false positives by up to 60%.
  - num: AI-enhanced BI increases customer engagement by 38% and conversion rates by 22%.
  - num: Supply chain optimization with AI-driven BI achieves a 23% increase in operational efficiency and a 17% reduction in logistics costs.
  - num: Organizations using AI for financial risk assessment see a 28% reduction in unexpected financial losses.
  - Data governance complexities and algorithmic bias are cited as major challenges, with 62% of organizations facing data integration issues.
  - The review identifies a research gap in long-term business impact studies of AI-powered BI.
key_figures_tables:
  - Figure 2: Benefits of AI-based Decision Making in Finance → Highlights improvements in forecasting, fraud detection, and risk assessment.
  - Table 1: Identified Gaps from the study → Summarizes key research gaps in financial planning, long-term impact, and cross-industry applications.
  - Figure 8: AI-Driven BI Findings - Stacked Area Chart → Visualizes quantitative improvements across forecasting, fraud detection, and customer engagement.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: BI
    definition: Business Intelligence
  - term: AI
    definition: Artificial Intelligence
  - term: ML
    definition: Machine Learning
  - term: NLP
    definition: Natural Language Processing
  - term: DL
    definition: Deep Learning
  - term: DDDM
    definition: Data-Driven Decision-Making
  - term: DSS
    definition: Decision Support Systems
  - term: PRISMA
    definition: Preferred Reporting Items for Systematic Reviews and Meta-Analyses
critical_citations:
  - "[Duan et al., 2019] — Framework for AI in decision-making."
  - "[Dwivedi et al., 2021] — Multidisciplinary perspective on AI challenges."
  - "[Sarker, 2022] — AI-based modeling techniques for business."
  - "[Cheng et al., 2020] — AI models for real-time forecasting."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: The paper discusses AI-driven BI for young professionals but does not specifically focus on the Filipino demographic.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: The paper extensively covers predictive analytics and forecasting models for financial applications.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Discusses ML and DL algorithms for financial forecasting, including LSTM and Random Forests.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Provides insights into how AI-driven BI supports strategic planning and resource allocation.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: The paper discusses AI's role in budget forecasting and capital allocation.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Reviews AI-driven anomaly detection methods for fraud detection in financial transactions.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Details ML algorithms like SVM and clustering for detecting anomalies in spending data.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Discusses how AI-driven BI enhances customer engagement through personalization.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses a systematic PRISMA framework for evaluating AI-driven BI systems.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: contextual
      justification: Touches on financial planning but does not explicitly address savings goal management.
  contribution: The paper provides a comprehensive systematic review of AI-enhanced BI systems, demonstrating significant improvements in financial forecasting, fraud detection, and customer engagement. It highlights key challenges such as data governance and algorithmic bias, which are critical for Odin's design. The findings justify the need for robust predictive analytics and anomaly detection modules in Odin. The review also underscores the importance of explainable AI and fairness-aware algorithms to ensure user trust and ethical decision-making.
  directly_justifies:
    - "AI-powered BI improves financial forecasting accuracy by 32-45%."
    - "AI-driven fraud detection reduces fraudulent transactions by 47%."
    - "AI-enhanced BI increases customer engagement by 38%."
    - "Data governance and algorithmic bias are major challenges in AI adoption."
  limits:
    - "The review is limited to studies published in English between 2012-2024."
    - "The paper is a systematic review and does not present new experimental data."
    - "The specific applicability of findings to the Filipino context is not addressed. [unacknowledged]"
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. Domains flagged as relevant include Expense Categorization (3), Predictive Modeling (6), Budget Recommendation (7), Anomaly Detection (8), and Engagement (11), as the paper directly discusses AI applications in these areas. Topic codes 6.A, 6.B, 8.A, and 8.B were assigned high relevance due to the paper's extensive coverage of predictive analytics and anomaly detection algorithms. Codes 7.A, 7.B, 11.A, and 12.A were assigned medium relevance for their supporting evidence on strategic planning and evaluation frameworks. Borderline cases such as the paper's discussion of customer segmentation (5.A) and financial behavior (1.C) were considered but not selected as they lack direct applicability to Odin's specific focus on Filipino young professionals. Domains like Cultural Context (2) and Mobile-First Design (9) were rejected due to no relevant content. Overall, the paper provides strong evidence for Odin's predictive and anomaly detection modules.
limitations:
  - "The paper is a systematic review and does not present new experimental data."
  - "The specific applicability of findings to the Filipino context is not addressed. [unacknowledged]"
  - "Potential publication bias is not discussed. [unacknowledged]"
remember_this:
  - "AI-powered BI improves forecasting accuracy by 32-45%."
  - "AI-driven fraud detection reduces fraudulent transactions by 47%."
  - "AI-enhanced BI increases customer engagement by 38%."
  - "Data governance and bias remain major challenges."
  - "The review follows PRISMA guidelines for rigorous analysis."
```
---

## Paper 12: Whitaker_summarized.md

**Source File:** `Whitaker_summarized.md`

```yaml
paper_id: d3918c1d-5e2e-5c28-9c6e-5de2c9a55894
designation: international
title: The Role of Big Data Analytics in Behavioral Finance: Understanding Dynamics of Consumer Spending and Saving
authors: Whitaker, K.
year: 2025
venue: Unknown
odin_topics:
  - 1.C
  - 2.A
  - 3.A
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 11.A
  - 12.A
tldr: Big data analytics reveals psychological and behavioral drivers of consumer spending and saving, enabling personalized financial strategies.
problem_and_motivation: Traditional financial models overlook psychological biases and emotional factors that shape consumer financial behavior. A gap exists in understanding how multidimensional drivers like cognitive biases and social influences affect spending and saving decisions. Big data offers a way to analyze these factors at scale to improve financial decision-making.
approach:
  - Integrated structured financial datasets with unstructured digital footprints like transaction histories and social media data.
  - Applied machine learning and predictive analytics to identify hidden determinants of financial decision-making.
  - Used descriptive, predictive, and prescriptive analytics to summarize, forecast, and recommend financial actions.
  - Employed clustering algorithms to segment consumers based on spending and saving behaviors.
  - Used sentiment analysis on social media to gauge public sentiment regarding economic conditions.
findings:
  - Consumer behavior is shaped by psychological biases, socio-demographic characteristics, and contextual influences.
  - Big data techniques enable more accurate segmentation of consumer groups.
  - Big data can identify spending triggers like economic conditions or social influences.
  - Analyzing saving behaviors reveals temporal patterns and the influence of economic factors.
  - Big data analytics can be used to predict future spending and saving behaviors.
  - Insights from big data enable the development of personalized financial products and services.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Big Data
    definition: Vast volumes of structured and unstructured data characterized by volume, velocity, and variety.
  - term: Behavioral Finance
    definition: Field combining psychology and economics to explain irrational financial decisions due to cognitive biases and emotions.
  - term: Cognitive Biases
    definition: Systematic patterns of deviation from rationality in judgment, such as overconfidence and loss aversion.
  - term: Predictive Analytics
    definition: Use of statistical models and ML to forecast future behaviors based on historical data.
critical_citations:
  - "[Kahneman & Tversky, 1979] — foundational work on cognitive biases."
  - "[Thaler, 1980] — mental accounting and behavioral economics."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: contextual
      justification: Provides general framework for understanding financial behavior.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: Discusses social and demographic influences on financial decisions.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Discusses using transaction data to understand spending patterns.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Segmentation of consumers based on behavioral patterns.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Mentions clustering and segmentation techniques.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Discusses predictive modeling for spending and saving behaviors.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: General mention of predictive models for forecasting.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: Mentions developing personalized financial strategies.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Mentions identifying unusual spending patterns.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: General reference to identifying unusual patterns.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Explicitly addresses privacy and security concerns.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Privacy and transparency are linked to consumer trust.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: Mentions personalized services and targeted marketing.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: contextual
      justification: General discussion of evaluating financial products.
  contribution: The paper provides a high-level overview of how big data analytics can be used to understand consumer spending and saving behavior. It offers a conceptual framework for integrating behavioral finance principles with big data analytics to develop personalized financial products and services. The paper's contribution is primarily contextual, providing theoretical justification for using data-driven approaches to understand and predict consumer financial behavior. It does not offer specific algorithms or system designs but advocates for the use of machine learning and predictive analytics to enhance financial decision-making. The paper's main value is in framing the problem and highlighting the potential of big data in behavioral finance.
  directly_justifies:
    - "Consumer behavior is shaped by psychological biases and contextual influences, not just rational economic factors."
    - "Big data techniques enable more accurate segmentation of consumer groups based on behavior."
    - "Predictive models can forecast future spending and saving behaviors using historical data."
  limits:
    - "The paper is a high-level review with no empirical data or specific algorithmic implementations."
    - "It lacks specific details on how to operationalize big data analytics in a personal finance system."
    - "Does not address the unique challenges of the Philippine financial context. [unacknowledged]"
    - "No evaluation of the proposed techniques is provided. [unacknowledged]"
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant for domains related to Behavioral Profiling (5.A, 5.C), Spending Forecasting (6.A, 6.B), Budget Recommendation (7.A), Anomaly Detection (8.A, 8.B), Data Privacy (10.A, 10.B), and User Retention (11.A). However, the relevance is primarily contextual or low because the paper provides a general overview rather than specific, actionable insights for Odin's design. The topic 10.A (Data Privacy) was assigned high relevance because the paper directly addresses privacy and security concerns. Topics 3.A (Expense Categorization) and 5.A (Behavioral Profiles) were assigned medium relevance due to direct mentions of transaction analysis and consumer segmentation. Other topics like 2.A (Cultural Practices) and 7.A (Budgeting Strategies) were considered but rejected for higher relevance due to the lack of Philippine-specific focus or algorithmic detail. Overall, the paper provides a broad theoretical justification for using data analytics in personal finance but does not offer specific evidence for Odin's modules.
limitations:
  - "No empirical data or specific case studies are presented to support claims."
  - "The paper does not address algorithmic implementation details or performance metrics."
  - "It is not specific to the Filipino context or Odin's target demographic. [unacknowledged]"
remember_this:
  - "Big data analytics can uncover hidden psychological and emotional drivers of spending."
  - "Consumer behavior is influenced by cognitive biases, social factors, and external triggers."
  - "Predictive analytics and machine learning are key tools for forecasting financial behaviors."
  - "Data privacy and security are critical for maintaining consumer trust in financial apps."
```
---

## Paper 13: Begum_summarized.md

**Source File:** `Begum_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8_1a2b3c4d5e6f7g8h9i0j
designation: international
title: Machine Learning in Financial Risk and Behavior Analysis: Predictive Insights on Bankruptcy, Fraud, and Consumer Trends in the USA
authors: Begum, M.
year: 2025
venue: Journal of Data & Digital Innovation
odin_topics:
  - 4.A
  - 4.B
  - 5.A
  - 6.A
  - 8.A
  - 12.A
tldr: Machine learning models, particularly ensembles and LSTMs, improve bankruptcy prediction, fraud detection, and consumer trend forecasting compared to traditional methods.
problem_and_motivation: Financial systems are increasingly complex, with nonlinear patterns and real-time anomalies that traditional statistical methods struggle to capture. This creates a critical need for intelligent, data-driven approaches to assess and mitigate risks like bankruptcy and fraud. The paper aims to provide predictive insights to enhance decision-making and personalize financial services.
approach:
  - A framework using six models (Logistic Regression, Random Forest, Gradient Boosting, SVM, ANN, LSTM) for bankruptcy prediction.
  - Unsupervised (Isolation Forest) and supervised (Logistic Regression, Random Forest, XGBoost) classifiers, plus ensemble and RNN methods for fraud detection.
  - K-Means and DBSCAN for behavioral segmentation, and ARIMA and LSTM for forecasting financial activities.
  - SMOTE applied to address data imbalance, particularly in fraud detection and bankruptcy prediction.
  - PCA and feature engineering employed to improve model generalization and reduce dimensionality.
  - Models evaluated using Accuracy, Precision, Recall, F1-Score, AUC, and MAE metrics.
findings:
  - num: XGBoost and LightGBM achieved the highest AUC scores (0.93 and 0.91) for bankruptcy prediction.
  - num: The stacking ensemble model for fraud detection achieved the highest F1 score of 0.89.
  - num: LSTM outperformed ARIMA in consumer forecasting, with a lower MAE of 2.8 compared to 4.2.
  - K-Means clustering achieved a silhouette score of 0.68, indicating well-separated customer segments.
  - DBSCAN achieved a lower Davies-Bouldin score of 0.52, reflecting good cluster separation but with parameter sensitivity.
  - GRU-RNN outperformed static models in recall (0.89 vs. 0.81) for fraud detection.
  - Logistic Regression lagged behind other models in bankruptcy prediction with an AUC of 0.76.
  - Isolation Forest suffered from low precision (0.65) due to false positives in fraud detection.
  - ARIMA struggled with volatile sales periods, as shown in residual plots.
  - Debt/Equity ratio and Profit Margin were identified as important non-redundant predictors for bankruptcy.
key_figures_tables:
  - "Figure 10: Bankruptcy AUC comparison and learning curves → Gradient boosting models (XGBoost, LightGBM) achieve highest AUC."
  - "Figure 11: Fraud detection precision-F1 comparison and GRU recall → Stacking ensemble and GRU-RNN show high performance."
  - "Figure 12: ARIMA vs. LSTM error metrics → LSTM significantly outperforms ARIMA in forecasting accuracy."
  - "Figure 13: Silhouette analysis and DBSCAN sensitivity → K-Means shows good cluster separation; DBSCAN performance is parameter-dependent."
  - "Figure 14: K-Means vs. DBSCAN visual comparison → K-Means identifies spherical clusters; DBSCAN finds non-spherical clusters and noise."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: SMOTE
    definition: Synthetic Minority Over-sampling Technique, used to address class imbalance.
  - term: PCA
    definition: Principal Component Analysis, used for dimensionality reduction.
  - term: RNN
    definition: Recurrent Neural Network, used for sequence-based anomaly detection.
  - term: AUC
    definition: Area Under the Curve, a performance metric for classification models.
  - term: MAE
    definition: Mean Absolute Error, a metric for evaluating forecasting accuracy.
critical_citations:
  - "[Sizan et al., 2025] — Foundational for bankruptcy prediction and fraud detection frameworks."
  - "[Al Montaser et al., 2025] — Provides basis for sentiment and behavioral analysis."
  - "[Mohaimin et al., 2025] — Supports churn prediction and customer retention strategies."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Provides a comprehensive review of ML systems for financial risk and behavior analysis.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies gaps like model interpretability, data imbalance, and real-time adaptability in current systems.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Uses clustering (K-Means, DBSCAN) to segment consumers, informing behavioral profiles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Focuses on predictive modeling for bankruptcy, fraud, and consumer trends, directly applicable to Odin's forecasting modules.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Dedicated section on fraud detection using anomaly detection algorithms like Isolation Forest.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Rigorously evaluates multiple models using metrics like AUC, F1-score, and MAE.
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: The paper's focus on US consumers provides generalizable insights but not specific to Filipino demographics.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: low
      justification: Mentions seasonality in retail sales forecasting but does not deeply analyze cyclical spending.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Notes data privacy as a gap but does not focus on privacy-preserving techniques.
  contribution: "The paper's framework for bankruptcy prediction using gradient-boosting and LSTM models can directly inform Odin's financial health assessment module. Its ensemble approach for fraud detection offers a blueprint for Odin's anomaly detection system. The consumer segmentation and forecasting methods provide a basis for Odin's behavioral profiling and spending forecasting features. The evaluation metrics and validation strategies outlined are directly applicable to Odin's system evaluation protocols."
  directly_justifies:
    - "Gradient boosting models (XGBoost, LightGBM) are effective for bankruptcy prediction from financial ratios."
    - "Stacking ensemble models improve F1 scores in fraud detection by combining classifiers."
    - "LSTM networks outperform ARIMA for forecasting consumer spending with nonlinear trends."
  limits:
    - "Models rely on static, pre-collected datasets, which may not reflect rapidly changing market dynamics."
    - "The study does not integrate real-time data pipelines, limiting responsiveness and accuracy."
    - "Generalizability of models to other sectors or evolving market dynamics is limited."
    - "Ethical concerns and data privacy issues remain unchecked in the AI-based applications."
  mapping_rationale: "A systematic scan of all 12 functional domains was performed. High relevance was assigned to domains directly addressed by the paper's core contributions. The paper strongly aligns with 'Existing Systems & Gaps' (4.A, 4.B) as it reviews and identifies limitations in current ML applications. 'Behavioral Profiling' (5.A) is supported via clustering, and 'Spending Forecasting' (6.A) is a primary focus. 'Anomaly Detection' (8.A) is a dedicated pillar. 'System Evaluation' (12.A) is demonstrated through a comprehensive performance comparison. Borderline cases include 'Seasonal and Cyclical Spending' (2.B), which is mentioned but not a core focus, thus rated 'low.' Similarly, 'Data Privacy' (10.A) is noted as a gap but not a design feature, rated 'low.' Domains like 'Filipino Cultural Context' (2.A) and 'Mobile-First Design' (9.A) were considered but rejected as the paper is US-centric and not focused on mobile UX. The paper provides a broad, high-level overview of ML techniques applicable to multiple Odin modules, making its overall relevance to the project 'high.'"
limitations:
  - "The study does not address the interpretability of complex models like neural networks, which is critical for user trust."
  - "Models are not evaluated for performance on live data streams or their ability to adapt over time. [unacknowledged]"
  - "The findings are based on US data and may not generalize to other cultural or economic contexts, such as the Philippines. [unacknowledged]"
  - "The paper lacks a discussion on the implementation cost or computational resources required for the proposed models."
remember_this:
  - "XGBoost and LightGBM achieve AUC scores above 0.90 for bankruptcy prediction."
  - "Stacking ensemble models significantly improve fraud detection F1 scores."
  - "LSTM networks reduce forecasting error (MAE) by over 30% compared to ARIMA."
  - "K-Means clustering effectively segments customers for targeted strategies."
  - "Data imbalance and model interpretability remain key challenges in practice."
```
---

## Paper 14: Hall & Rasheed_summarized.md

**Source File:** `Hall & Rasheed_summarized.md`

```yaml
paper_id: 10.3390/app15115957
designation: international
title: A Survey of Machine Learning Methods for Time Series Prediction
authors: Hall, T.; Rasheed, K.
year: 2025
venue: Applied Sciences
odin_topics:
  - 6.A
  - 6.B
  - 12.A
  - 12.B
  - 5.C
  - 7.D
  - 8.B
  - 9.A
  - 5.A
  - 10.A
tldr: Tree-based and recurrent neural network models show comparable predictive performance, with tree-based methods offering significant computational efficiency advantages.
problem_and_motivation: Existing literature reviews on time series prediction fail to draw meaningful comparisons between models due to heterogeneous experimental setups. This prevents robust conclusions about the relative strengths of tree-based and deep learning approaches.
approach:
  - A systematic review was conducted on 79 papers published between 2017 and 2024 from Web of Science.
  - Inclusion required studies comparing at least one tree-based and one deep learning model on identical datasets.
  - Models were evaluated using a First Place Aggregation (FPA) score and a Weighted Rank Aggregation (WRA) score.
  - Analysis investigated performance variations based on task category, dataset size, time interval, and research focus.
  - Training time and hyperparameter optimization techniques were also examined for the reviewed models.
findings:
  - Tree-based models outperform deep learning models in 54.55% of tasks, achieving a WRA score of 0.6910.
  - Recurrent neural networks are the strongest deep learning models, while SPTB (XGBoost, LightGBM, CatBoost) models lead for tree-based methods.
  - num: Tree-based models are on average 126,934.94% faster to train than deep learning models, with a median speed advantage of 5603.43%.
  - num: In the largest dataset range (206,573–11,275,200 samples), SPTB models outperform RNNs with a WRA advantage of 0.3833.
  - num: In the M5 Accuracy Competition, 4 of the top 5 submissions relied on LightGBM models.
  - LightGBM and CatBoost emerge as top performers, but the limited representation of CatBoost calls for further validation.
  - Research focus introduces bias, with papers favoring deep learning or tree-based methods showing inflated performance for their preferred model class.
  - Bayesian Optimization and OPTUNA are computationally efficient alternatives to the frequently used but expensive Grid Search.
key_figures_tables:
  - Figure 3: FPA and WRA scores comparing TBML and DL classes → TBML has a slight edge over DL overall.
  - Figure 5: FPA scores for each model → CatBoost, Transformers, LSTMs, and LightGBM are top performers.
  - Figure 6: WRA scores for each model → CatBoost and LSTM show strong and consistent performance.
  - Table 3: Best-performing models by dataset size, task, time interval, and efficiency → Practical guide for model selection.
  - Table 2: Training time advantage of TBML models → TBML can be orders of magnitude faster than DL.
key_equations:
  - equation: FPA = (N_first / N_total) * 100
    explanation: Percentage of comparisons where a model ranks first.
  - equation: WRA = 1 - (N_rank - 1) / (N_total - 1)
    explanation: Normalized score based on a model's rank in each comparison.
definitions:
  - term: TBML
    definition: Tree-Based Machine Learning, including Random Forests and GBDT.
  - term: DL
    definition: Deep Learning, using neural networks with multiple layers.
  - term: SPTB
    definition: Specialized Tree-Based models like XGBoost, LightGBM, and CatBoost.
  - term: RNN
    definition: Recurrent Neural Network, designed for sequential data.
  - term: LSTM
    definition: Long Short-Term Memory, a popular RNN variant with memory gates.
  - term: FPA
    definition: First Place Aggregation, the frequency a model is the top performer.
  - term: WRA
    definition: Weighted Rank Aggregation, a normalized score based on average rank.
  - term: ARIMA
    definition: Autoregressive Integrated Moving Average, a traditional statistical model.
critical_citations:
  - "[Chen, 2016] — Introduced XGBoost as a scalable tree boosting system."
  - "[Ke, 2017] — Developed LightGBM, known for its computational efficiency."
  - "[Prokhorenkova, 2018] — Created CatBoost for handling categorical data effectively."
  - "[Sherstinsky, 2020] — Fundamental overview of RNN and LSTM networks."
  - "[Vaswani, 2017] — Introduced the Transformer model with a self-attention mechanism."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: This paper is a comprehensive survey of predictive ML models directly relevant to Odin's core forecasting functions.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: It provides a detailed evaluation of LSTM, GRU, XGBoost, and LightGBM, which are prime candidates for spending forecasting.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: The paper extensively analyzes error metrics (RMSE, MAE, MAPE, etc.) and proposes a methodology for comparing model performance.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: The survey's systematic comparison of TBML vs. DL models provides a framework for evaluating Odin's individual algorithms.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: While not about user profiles, the review of classification models and metrics can inform behavioral profile classification.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: contextual
      justification: The paper's discussion of hybrid models provides context for more robust, ensemble-based systems, but does not address infeasibility.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: The survey includes models and metrics applicable to anomaly detection, such as classification techniques.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: contextual
      justification: The paper's findings on computational efficiency (training time) are critical for mobile-first deployment, but does not discuss UX.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: low
      justification: The paper is a methodological survey, not a study of user behavior, making its relevance to profiling only indirect.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: The paper does not address privacy or security. It mentions data quality but not the sensitivity of personal data.
  contribution: The paper provides a high-level comparison of tree-based and deep learning models for time series prediction, establishing a broad performance baseline for Odin's forecasting module. Its detailed analysis of model performance across task types, dataset sizes, and computational costs directly informs the selection of algorithms for spending forecasting and anomaly detection. The extensive review of error metrics and evaluation methodologies provides a standard framework against which Odin's system evaluation can be validated. The findings on hybrid models and the importance of ensemble methods suggest a robust architectural direction for improving the system's predictive reliability. The paper's explicit identification of LightGBM and LSTM as top performers provides strong justification for prioritizing these algorithms in the system's development roadmap.
  directly_justifies:
    - "LightGBM and LSTM are among the best-performing models for time series forecasting."
    - "Tree-based models offer a significant computational advantage over deep learning models."
    - "The choice of data and feature engineering is as critical as the choice of the forecasting model."
    - "Hybrid models, particularly those combining SPTB and RNNs, often yield superior predictive performance."
    - "Bayesian Optimization and OPTUNA are efficient alternatives to Grid Search for hyperparameter tuning."
  limits:
    - "The survey covers papers only up to 2024, limiting insight into the latest state-of-the-art transformer models."
    - "The analysis groups diverse model variants (e.g., all RNNs), which may obscure specific advantages of models like Bi-LSTM."
    - "The findings on domain-specific performance are based on a small number of samples for some task categories, limiting their generalizability."
    - "The paper's analysis of research bias highlights potential methodological flaws in comparative model studies, which should be considered when evaluating the source literature."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated canonical topic codes was performed. The domains of `Spending Forecasting`, `System Evaluation`, and `Behavioral Profiling & Classification` were flagged as highly relevant. Within `Spending Forecasting`, topic codes 6.A and 6.B were assigned a `high` relevance because the paper is a direct survey of predictive models for sequential data. For `System Evaluation`, codes 12.A and 12.B were rated `high` as the paper's methodology for evaluating and comparing algorithms provides a practical framework for Odin's testing. Code 5.C was rated `medium` because the survey covers classification approaches that could be adapted for user profiling. Topic codes 7.D (Infeasibility Handling), 8.B (Anomaly Detection), and 9.A (Mobile-First Design) were rated `contextual`; the paper discusses model ensembles and anomaly detection methods but does not directly address Odin's specific challenges in these areas. Codes 5.A and 10.A were considered and rejected due to the paper's exclusive focus on computational methods rather than user behavior or privacy. The survey's overall relevance to Odin is high as it serves as a foundational guide for selecting and evaluating the core forecasting and classification algorithms.
limitations:
  - "The survey's classification of model categories (e.g., grouping all RNNs) may obscure the nuanced performance of specific architectures like Bi-LSTM or GRU."
  - "The analysis of temporal resolution did not reveal clear trends, suggesting that time interval may be less important than domain-specific data characteristics."
  - "The findings on bias based on research focus reveal a potential weakness in the methodology of the surveyed papers themselves."
remember_this:
  - "LightGBM and LSTM are top-performing models for time series prediction."
  - "Tree-based models are orders of magnitude faster to train than deep learning models."
  - "Model combination and ensemble methods consistently improve predictive performance."
  - "Data quality and feature engineering can be more important than the choice of the model."
  - "Research focus bias can significantly affect reported comparative model performance."
```
---

## Paper 15: Sipila_summarized.md

**Source File:** `Sipila_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international
title: Proof of concept of centralized personal finance application
authors: Sipilä, M.
year: 2025
venue: Unknown
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 9.A
  - 10.A
  - 11.A
  - 12.A
tldr: A proof-of-concept personal finance application was developed using DSRM to consolidate fragmented financial tracking, automate data retrieval, and generate integrated reports for a stakeholder.
problem_and_motivation: Stakeholders managing finances over a decade rely on fragmented tools like spreadsheets and third-party apps, leading to scalability issues, high manual effort, and error-prone reporting. Existing PFM tools lack comprehensive integration and automation, failing to meet the needs of sophisticated users with specific asset tracking requirements.
approach:
  - The Design Science Research Methodology (DSRM) was followed, involving six iterative phases from problem identification to evaluation.
  - A structured questionnaire identified stakeholder challenges, including complexity, lack of automation, and reporting inefficiencies.
  - The application was built using Flutter for a cross-platform UI, ASP.NET Core for the backend API, and MongoDB for data storage.
  - Key features include asset tracking (shares, cash, real estate), categorized cash flow monitoring, and automated PDF report generation.
  - External integrations were implemented using Google Sheets API for stock prices and HexaRate API for exchange rates, with a focus on automating data retrieval.
findings:
  - num: The PoC application significantly reduced manual work and human error by centralizing financial data and automating calculations.
  - num: The stakeholder reported a reduction in manual effort and increased trust in data accuracy, validated through task-based user testing.
  - num: The system successfully replaced a multi-step manual reporting process with one integrated, automated PDF report generation feature.
  - The stakeholder found the interface intuitive and the visualizations (pie charts, trend graphs) clear and informative for gaining financial insights.
  - The application effectively addressed the core "Must have" requirements, such as data visualization and asset tagging, as defined in the design phase.
  - User feedback highlighted the need for refinements in tooltips, label clarity, and a clearer definition of the cash flow module's purpose.
key_figures_tables:
  - Figure 3: Interactive doughnut chart of shares → Visualizes portfolio distribution.
  - Figure 4: Editable tables of assets with summary stats → Enables data review and modification.
  - Figure 5: User net worth over time → Tracks historical asset growth trends.
  - Figure 7: Multi-layered pie charts of share distribution → Shows categorization by type, country, and subcategory.
  - Figure 9: Cash flow tracking charts and timeline → Compares monthly income and expenses.
  - Figure 10: User-generated financial report → Consolidates key metrics into a PDF.
  - Table 9: Baseline vs. PoC system comparison → Highlights improvements in automation and centralization.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: DSRM
    definition: Design Science Research Methodology
  - term: PFM
    definition: Personal Finance Management
  - term: PoC
    definition: Proof-of-concept
  - term: FR
    definition: Functional Requirement
  - term: QA
    definition: Quality Attribute
critical_citations:
  - "[Cederberg, 2013] — Highlights user preference for automation and visual clarity."
  - "[Torno et al., 2021] — Identifies lack of holistic integration in PFM apps."
  - "[Stefanov et al., 2024] — Notes need for localized and centralized PFM solutions."
  - "[Herrala et al., 2023] — Links tool complexity to user stress and distrust."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: The system implements categorization for transactions and assets, aligning with this topic.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: User tagging and categorization of cash flow and assets are core to the design.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: The thesis provides a detailed literature review and analysis of PFM landscape limitations.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly addresses fragmentation, manual effort, and scalability gaps in current tools.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: contextual
      justification: Flutter was used for cross-platform support, but mobile optimization was not completed.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: The lack of authentication is identified as a major limitation, highlighting its importance.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Discusses how automation and visualization can improve user engagement and motivation.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Used a structured DSRM evaluation with task-based testing and stakeholder questionnaires.
  contribution: "This research contributes a practical proof-of-concept that demonstrates how centralized financial data, automated retrieval, and integrated reporting can significantly reduce manual workload and errors for a sophisticated user. The application's design directly informs Odin's architecture for asset tracking and reporting modules. The DSRM-based iterative development and stakeholder evaluation provide a validated framework for building user-centric PFM tools. The findings on automation and data centralization justify Odin's focus on these features to address similar gaps in the Filipino context."
  directly_justifies:
    - "A centralized platform can solve the problem of fragmented financial data from multiple sources."
    - "Automating data retrieval for share prices and exchange rates significantly reduces manual effort and errors."
    - "Integrated reporting replaces time-consuming manual processes with on-demand summaries."
    - "User-centered design and iterative feedback are critical for developing effective PFM tools."
    - "Stakeholders value systems that are reliable, automated, and provide clear visual insights."
  limits:
    - "The study is based on a single stakeholder, limiting generalizability to broader populations."
    - "Full automation through bank and broker APIs was not achieved, relying on manual entry and workarounds."
    - "No authentication or authorization mechanisms were implemented, posing data security risks."
    - "Mobile-specific UI optimization was not completed, focusing primarily on desktop and web platforms."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. Domains directly relevant to the thesis's core contribution (expense categorization, existing systems/gaps, and system evaluation) were flagged as high priority. The paper's literature review and problem analysis strongly support topics like 3.A, 3.B, 4.A, and 4.B (high). Its practical evaluation using a DSRM framework provides a direct contribution to 12.A (high). The discussion on user engagement and motivation links to 11.A (medium). The mention of mobile-first design (9.A) and data security (10.A) is purely contextual, as these were not primary implementation focuses due to the PoC scope. Topics related to Filipino cultural context (2.A-D), behavioral profiling (5.A-C), forecasting (6.A-B), budget recommendation (7.A-D), anomaly detection (8.A-C), and savings/debt management (13.A-C) were considered but rejected as the thesis does not address these specific problem domains. The paper's overall relevance to Odin is high as it provides a validated blueprint for a centralized PFM system with automated reporting, addressing gaps found in many existing tools."
limitations:
  - "The system was only tested with one stakeholder, limiting generalizability of usability findings. [unacknowledged]"
  - "User authentication and data privacy were not implemented, making it unsuitable for multi-user deployment."
  - "Full automation via bank/broker APIs was not achieved, requiring manual data entry for some transactions."
  - "Mobile UI optimization was not completed, limiting the 'mobile-first' aspect of the design."
  - "Performance was not formally tested under load, and no unit/integration tests were documented."
  - "The study's findings may be biased due to the stakeholder's high financial literacy."
remember_this:
  - "Centralized PFM tools reduce manual work and improve data reliability."
  - "Automated reporting saves significant time compared to manual quarterly reviews."
  - "Stakeholder feedback confirmed a reduction in manual effort and increased trust in data."
  - "The PoC addressed core requirements but lacked authentication and mobile optimization."
  - "DSRM provides an effective framework for developing user-centered financial applications."
```
---

## Paper 16: Yusuf et al_summarized.md

**Source File:** `Yusuf et al_summarized.md`

```yaml
paper_id: 10.23887/jet.v9i4.103004
designation: international
title: Does Technology Reduce or Amplify Financial Stress? A Cognitive-Behavioral Perspective on Nigerian Postgraduate Students
authors: Yusuf, J.; Bolaji, H. O.; Ahmed, M. S.; Abdulkareem, H. B.
year: 2025
venue: Journal of Education Technology
odin_topics:
  - 1.C
  - 2.A
  - 2.B
  - 4.A
  - 5.A
  - 5.C
  - 7.A
  - 10.A
  - 10.B
  - 11.A
  - 11.B
tldr: Digital financial tools have a dual role, both alleviating and amplifying financial stress depending on students' cognitive interpretations, behavioral responses, and financial literacy.
problem_and_motivation: Financial stress among postgraduate students is increasing in Nigeria due to economic pressures and digital financial technology adoption, yet the psychological mechanisms linking technology use to stress are underexplored. Existing literature emphasizes structural economic factors but neglects how cognitive-behavioral processes and fintech environments interact to shape financial well-being. This gap necessitates an integrated framework to understand whether technology reduces or exacerbates financial vulnerability.
approach:
  - A conceptual and analytical research design was employed to synthesize and critically evaluate existing knowledge.
  - The study used a qualitative, theory-driven approach grounded in Cognitive-Behavioral Theory (CBT).
  - Data were collected from secondary sources, including approximately 70 peer-reviewed articles, policy documents, and empirical studies published between 2015 and 2024.
  - Literature was retrieved from Scopus, Web of Science, Google Scholar, and JSTOR using targeted keyword searches.
  - Analysis involved thematic and comparative analysis, followed by theory-driven interpretation based on CBT principles.
findings:
  - num: The reviewed literature included 22 studies on financial stress in higher education, 18 on fintech adoption, 15 on financial literacy, and 15 on psychological perspectives.
  - Digital financial technologies such as budgeting apps, mobile banking, and savings platforms enhance financial awareness, self-efficacy, and emotional regulation.
  - Misuse of fintech services, impulsive digital borrowing, exposure to fraud, and information overload trigger cognitive distortions that exacerbate anxiety and maladaptive financial behaviors.
  - Financial stress is shaped more by students' cognitive interpretations and coping strategies than by technology itself.
  - Digital financial tools can reduce financial stress only when accompanied by adequate cognitive-behavioral skills and financial literacy.
key_figures_tables:
  - Table 3: Distribution of reviewed literature by theme → Financial stress and fintech adoption are dominant research themes.
  - Table 4: Categories of digital financial technologies used by students → Tools include mobile banking, savings platforms, budgeting apps, and lending apps.
  - Table 5: Cognitive-behavioral patterns associated with financial stress → Catastrophizing and negative self-evaluation lead to avoidance and impulsive borrowing.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: CBT
    definition: Cognitive-Behavioral Theory, a psychological framework emphasizing how thoughts and beliefs influence emotions and behaviors.
  - term: Fintech
    definition: Financial technology, digital tools and platforms for managing financial transactions and services.
critical_citations:
  - "[Beck, 1976] — Foundational work on Cognitive-Behavioral Theory."
  - "[Dobson & Dozois, 2019] — Comprehensive overview of CBT principles and applications."
  - "[Lusardi & Mitchell, 2014] — Established the economic importance of financial literacy."
  - "[Adediran & Okonkwo, 2023] — Links fintech adoption to financial stress among Nigerian students."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly addresses financial behavior and stress among postgraduate students.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Discusses financial practices in the Nigerian context, offering parallels for Filipino cultural adaptation.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: low
      justification: Touches on economic pressures and irregular income, but does not explicitly focus on seasonal cycles.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Mentions digital financial tools but does not provide a systematic review of existing PFMS.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Analyzes cognitive-behavioral patterns (e.g., catastrophizing) that inform behavioral profiling.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Identifies behavioral responses like impulsive borrowing that could be used for classification.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Discusses budgeting applications as tools for financial management and stress reduction.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Mentions exposure to online fraud, a privacy/security concern, but not as a primary focus.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: Implicitly relevant through fraud risk, but trust is not directly examined.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: Discusses fintech usage patterns but not engagement dynamics specifically.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: low
      justification: Does not address retention mechanisms.
  contribution: This paper provides a psychological framework (CBT) for understanding how user cognition mediates the impact of digital financial tools on financial stress, directly informing Odin's behavioral profiling module (5.A, 5.C). It highlights the dual role of technology as both a stress reducer and amplifier, which is critical for designing budget recommendation (7.A) and anomaly detection systems that account for user psychology. The emphasis on cognitive-behavioral interventions suggests that Odin's user engagement (11.A) and retention strategies (11.B) could benefit from incorporating financial literacy and coping mechanisms. The paper's findings on impulsive digital borrowing and fraud exposure underscore the need for Odin's data privacy (10.A) and user trust (10.B) features to mitigate psychological distress.
  directly_justifies:
    - "Financial stress is shaped more by cognitive interpretations than by technology alone."
    - "Digital financial tools can reduce stress only when paired with adequate financial literacy."
    - "Maladaptive cognitive patterns like catastrophizing intensify financial anxiety."
  limits:
    - "Conceptual and literature-based methodology limits direct measurement of student experiences."
    - "Evidence reflects patterns from existing literature rather than primary empirical data."
    - "Rapid fintech changes may introduce behaviors not yet documented in current research."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant to the Filipino Cultural Context (2.A, 2.B) due to its focus on Nigerian postgraduate students, offering cultural parallels for Filipino young professionals. It directly informs Behavioral Profiling (5.A, 5.C) by detailing cognitive-behavioral patterns and their role in financial stress, with high relevance. The paper's discussion of budgeting apps and financial literacy supports Budget Recommendation (7.A) with medium relevance. It also touches on Existing Systems (4.A), Data Privacy (10.A), User Trust (10.B), and Engagement (11.A, 11.B), but these are tangential (low/contextual) as they are not the primary focus. Domains like Expense Categorization (3.A-C), Spending Forecasting (6.A-B), Anomaly Detection (8.A-C), Mobile-First Design (9.A-B), System Evaluation (12.A-C), and Savings/Debt Management (13.A-C) were rejected as the paper does not provide actionable claims for these areas. Overall, the paper offers high relevance for understanding the psychological drivers of financial behavior, which is foundational for Odin's user-centric design.
limitations:
  - "Conceptual and literature-based methodology limits direct measurement of student experiences."
  - "Evidence reflects patterns from existing literature rather than primary empirical data."
  - "Rapid fintech changes may introduce behaviors not yet documented in current research."
  - "Findings are context-specific to Nigeria and may not generalize to other cultural settings. [unacknowledged]"
remember_this:
  - "Digital financial tools both reduce and amplify financial stress depending on user psychology."
  - "Cognitive interpretations mediate the relationship between technology use and financial stress."
  - "Financial literacy and cognitive-behavioral skills are essential for technology to reduce stress."
  - "Maladaptive patterns like catastrophizing lead to impulsive borrowing and financial anxiety."
  - "The dual role of fintech requires user-centric design that addresses psychological vulnerabilities."
```
---

## Paper 17: Zlobin & Bazylevych_summarized.md

**Source File:** `Zlobin & Bazylevych_summarized.md`

```yaml
paper_id: 10.25140/2411-5363-2025-1(39)-184-195
designation: international
title: Systematic Review of Deep and Machine Learning for Financial Modeling
authors: Zlobin, M.; Bazylevych, V.
year: 2025
venue: Technical Sciences and Technologies
odin_topics:
  - 5.C
  - 6.A
  - 6.B
  - 7.D
  - 8.A
  - 8.B
  - 12.A
  - 12.B
  - 12.C
tldr: A systematic review of machine and deep learning applications in finance, comparing models for classification and regression tasks, and identifying challenges like interpretability and data quality.
problem_and_motivation: Financial institutions face challenges processing large datasets and complex market dynamics with traditional methods, necessitating advanced ML/DL for improved predictive accuracy and risk assessment. The rapid evolution of these technologies creates a need for a systematic synthesis of current methodologies and performance comparisons. Existing literature lacks a consolidated analysis of both classification and regression applications, their trade-offs, and practical implementation gaps.
approach:
  - The paper conducts a systematic literature review of 41 studies on ML/DL in financial analytics.
  - It categorizes financial applications into classification problems like credit scoring and fraud detection.
  - It also categorizes applications into regression problems such as stock price prediction and option pricing.
  - The review evaluates model performance using metrics like AUC, accuracy, F1-score, and RMSE across various datasets.
  - It compares traditional models, deep learning architectures, and hybrid approaches with a focus on interpretability and computational cost.
findings:
  - num: Random forest and XGBoost achieve up to 99.6% accuracy in fraud detection, with XGBoost outperforming deep networks in credit scoring.
  - num: LSTM networks demonstrate 93% accuracy in stock price trend prediction, outperforming linear regression for sequential data.
  - num: CNN models reduce fraud detection failure cost by 30% and achieve an AUC of 87.64% on benchmark datasets.
  - num: Hybrid GRU-CA models reduce anomaly detection RMSE from 13.28 to 9.74 on S&P 500 data.
  - num: Fairness interventions in credit scoring can cause a profit drop of 4.91% to over 35%, highlighting a trade-off between fairness and profitability.
  - num: GCN models outperform CNN in fraud detection with 94.5% accuracy, improving recall by 10% through graph-based relationship analysis.
  - Hybrid CNN-AdaBoost models achieve 96.35% accuracy in electricity theft detection, improving upon standalone models.
  - Traditional Black-Scholes models had lower pricing errors (RMSE 0.385-0.650) than ML models (RMSE 5.097-21.351) for option pricing, but ML models identified mispriced options more profitably.
  - AI personalization in fintech increases user engagement by 27%, retention by 15%, and conversion rates by 20%.
  - The MyFinanceAI platform reduced financial stress scores by 43% and increased monthly savings by 22% in a pilot study.
key_figures_tables:
  - Table 1: Comparative analysis of ML and DL models for credit scoring, fraud detection, and personalization → Highlights performance metrics and application-specific trade-offs.
  - Table 2: Comparative analysis of ML/DL models for option pricing and anomaly detection → Shows regression models perform differently from classification models, with traditional methods better for pricing accuracy and ML for profitability.
key_equations:
  - equation: RMSE = sqrt((1/n) * sum_{i=1}^{n} (y_i - \hat{y}_i)^2)
    explanation: Root Mean Square Error evaluates prediction accuracy.
definitions:
  - term: ML
    definition: Machine Learning, algorithms that learn from data.
  - term: DL
    definition: Deep Learning, neural networks with multiple layers.
  - term: AUC
    definition: Area Under the Receiver Operating Characteristic Curve.
  - term: RMSE
    definition: Root Mean Square Error, measures prediction error.
  - term: GCN
    definition: Graph Convolutional Network, processes graph-structured data.
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network for sequences.
critical_citations:
  - "[Gunnarsson et al., 2021] — XGBoost outperforms deep learning for credit scoring."
  - "[Kozodoi et al., 2021] — Quantifies fairness-profit trade-off in credit scoring."
  - "[Mienye et al., 2024] — Comprehensive survey of DL applications in finance."
relevance:
  topics:
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Reviews classification models (DBN, CNN, RF, XGBoost) for credit scoring and fraud detection.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Provides a comprehensive review of predictive models for financial time series.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Reviews LSTM and other DL models for stock price and volatility forecasting.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: contextual
      justification: Discusses concept drift and model adaptability to changing data, relevant to dynamic constraints.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Reviews anomaly detection models, including GCN, GRU-CA, and clustering methods for fraud and risk.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Compares algorithms like random forest, CNN, and GCN for fraud detection in transactional data.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Compares models using standard metrics and discusses evaluation challenges like data imbalance.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides performance comparisons of various ML/DL modules using AUC, RMSE, and accuracy.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: contextual
      justification: Discusses trade-offs between accuracy, fairness, and computational cost, relevant to budget system evaluation.
  contribution: This systematic review provides a comprehensive benchmark of ML/DL models applicable to Odin's core modules. It justifies the selection of XGBoost over deep learning for initial credit scoring and recommends LSTM for spending forecasting. The review's analysis of fraud detection informs Odin's anomaly detection module, while its discussion on model interpretability and fairness sets constraints for Odin's user-facing explanations.
  directly_justifies:
    - XGBoost should be preferred for credit scoring tasks due to superior accuracy and efficiency.
    - LSTM networks are effective for capturing temporal dependencies in sequential financial data.
    - Graph Convolutional Networks can improve anomaly detection by modeling user relationships.
    - Model interpretability remains a key challenge for regulated financial applications like Odin.
    - A trade-off exists between model fairness and profitability in automated decision systems.
  limits:
    - The review is a high-level synthesis, not a detailed design study for a specific system like Odin.
    - It covers broad financial domains, not specifically Filipino young professionals' personal finance.
    - The comparative analysis is aggregated from different studies, not controlled experiments on a unified dataset.
  mapping_rationale: All 12 functional domains were systematically scanned against the review's content. The paper is a broad survey of ML/DL for financial modeling, making it highly relevant to Odin's algorithmic modules. Domains flagged as high relevance include Expense Categorization (3.A, 3.B), Behavioral Profiling (5.A, 5.C), Spending Forecasting (6.A, 6.B), Anomaly Detection (8.A, 8.B), and System Evaluation (12.A, 12.B, 12.C). It was considered for 7.A and 7.B but rejected as its focus is on model performance for classification/regression, not domain-specific budgeting strategies. Similarly, it was considered for 10.A and 10.B but rejected as the review only touches on data privacy tangentially. The paper's discussion of concept drift and fairness supports 7.D and provides contextual relevance. Overall, the paper is highly relevant as a methodological reference for selecting and evaluating models that will form the backbone of Odin's analytic engine.
limitations:
  - The review may suffer from publication bias, as it only includes studies from specific databases. [unacknowledged]
  - It does not provide a unified experimental framework for comparing all models on identical datasets. [unacknowledged]
  - The applicability of findings to non-Western financial contexts is not addressed. [unacknowledged]
remember_this:
  - XGBoost outperforms deep learning for credit scoring with higher efficiency.
  - LSTM networks achieve 93% accuracy in forecasting financial trends from sequences.
  - Hybrid CNN-AdaBoost models improve fraud detection accuracy to 96.35%.
  - A fairness-profit trade-off exists, with a 4.91% profit loss for moderate fairness improvements.
  - AI personalization increases user engagement by 27% and retention by 15%.
```
---

## Paper 18: Du et al_summarized.md

**Source File:** `Du et al_summarized.md`

```yaml
paper_id: 10.3390/math13040587
designation: international
title: Foundations and Innovations in Data Fusion and Ensemble Learning for Effective Consensus
authors: Du, K.-L.; Zhang, R.; Jiang, B.; Zeng, J.; Lu, J.
year: 2025
venue: Mathematics
odin_topics:
  - 5.A
  - 6.A
  - 8.A
  - 12.A
tldr: A comprehensive survey of ensemble learning and data fusion techniques, covering bagging, boosting, random forests, theoretical foundations, and integration with deep learning.
problem_and_motivation: Ensemble learning and data fusion enhance predictive performance but present challenges in computational complexity and integration with deep learning. Understanding trade-offs between strategies is crucial for real-world applications with large-scale, high-dimensional data.
approach:
  - Categorizes ensemble learning methods including bagging, boosting, random forests, and their theoretical foundations.
  - Discusses aggregation techniques, majority voting, and the Dempster-Shafer theory of evidence.
  - Explores multiview learning and multiple kernel learning (MKL) for heterogeneous data sources.
  - Compares ensemble learning with deep learning, highlighting respective strengths, limitations, and synergies.
  - Analyzes computational trade-offs related to training complexity, inference efficiency, and storage requirements.
  - Presents a structured comparative summary of key ensemble techniques with future research directions.
findings:
  - Bagging reduces variance and improves model stability, particularly effective for high-variance models like decision trees.
  - Boosting minimizes bias by converting weak learners into strong ones through sequential training and weighted voting.
  - Random forests consistently outperform most methods in predictive accuracy and exhibit resilience to outliers and noise.
  - Gradient-boosted decision trees (GBDTs) often surpass deep learning models on tabular data, offering strong performance and interpretability.
  - Shallow neural networks can have representational power equal to or greater than deep random forests or decision diagrams.
  - The C-bound provides a more accurate risk indicator for majority voting, enabling optimization through the MinCq algorithm.
key_figures_tables:
  - Table 1: Summary of popular ensemble learning methods strengths, weaknesses, and typical applications.
  - Table 2: Computational and storage complexity of popular ensemble learning methods including Bagging, Boosting, Random Forests, and XGBoost.
  - Table 3: Comparison between ensemble learning and deep learning across definition, data requirements, computational complexity, interpretability, and fusion method.
key_equations:
  - equation: L \\sum y = w d i j ji j=1
    explanation: Weighted sum of outputs for voting.
  - equation: H(x) = sign(\\sum_{t=1}^{T} \\alpha_t h_t(x))
    explanation: Boosting combines weak hypotheses with weighted contributions.
  - equation: m(A) = \\frac{1}{1-K} \\sum_{B \\cap C = A} m_1(B)m_2(C)
    explanation: Dempster's combination rule fuses evidence from two sources.
definitions:
  - term: Bagging
    definition: Bootstrap aggregating; trains multiple models on different subsets of data to reduce variance.
  - term: Boosting
    definition: Sequential ensemble method that trains weak learners, focusing on misclassified instances to reduce bias.
  - term: Random Forest
    definition: Ensemble of decision trees using random feature subsets and bootstrap samples, improving variance reduction.
  - term: Dempster-Shafer Theory
    definition: A framework for combining evidence using belief and plausibility functions, generalizing Bayesian probability.
  - term: Error-Correcting Output Codes (ECOC)
    definition: Framework for multiclass classification by encoding classes into binary codewords and using error-correcting codes.
critical_citations:
  - "[Breiman, 1996] — Introduced bagging, foundational to ensemble learning."
  - "[Freund and Schapire, 1997] — Introduced AdaBoost, key boosting algorithm."
  - "[Breiman, 2001] — Introduced random forests, a widely used ensemble method."
  - "[Schapire et al., 1998] — Margin theory explaining boosting's effectiveness."
  - "[Friedman, 2001] — Introduced gradient boosting machines (GBMs)."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Discusses ensemble methods for classification, which can be adapted for financial behavioral profiling.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Covers forecasting algorithms like boosting and random forests applicable to spending prediction.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Reviews ensemble techniques like isolation forests and boosting that are used for anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: contextual
      justification: Provides theoretical analysis and computational trade-offs relevant to evaluating system components.
  contribution: This survey provides a foundational understanding of ensemble learning methods, which can inform the design of Odin's algorithmic modules. It offers theoretical insights into bias-variance trade-offs and margin theory, directly applicable to Odin's behavioral profiling and forecasting. The comparative analysis of bagging, boosting, and random forests guides the selection of appropriate models for spending classification and anomaly detection. The discussion on computational complexity and storage requirements is critical for Odin's mobile-first, resource-constrained environment. The paper's review of evaluation methodologies and emerging challenges, such as interpretability and handling noisy data, directly supports the development of Odin's evaluation framework.
  directly_justifies:
    - "Bagging and random forests are effective for reducing variance and improving stability in high-variance models like decision trees."
    - "Boosting minimizes bias by sequentially training weak learners, making it suitable for adaptive spending prediction."
    - "Ensemble methods enhance generalization by expanding decision margins and reducing overfitting."
    - "GBDTs often outperform deep learning models on tabular data, providing strong performance with interpretability."
    - "Diversity among classifiers is crucial for ensemble performance, impacting overall prediction accuracy."
  limits:
    - "The survey is theoretical and does not provide empirical validation or direct application to financial data."
    - "The analysis of computational complexity is general and may not account for specific constraints of mobile PFMS."
    - "The paper does not address cold-start challenges or user-specific adaptation, which are critical for Odin."
  mapping_rationale: A systematic scan across all 12 functional domains identified relevance primarily in predictive modeling, behavioral classification, and anomaly detection. Domains like expense categorization (3.A-C) and budget recommendation (7.A-D) were considered but rejected because the paper focuses on general machine learning techniques without addressing financial category design or constrained optimization. The domain of mobile-first design (9.A-B) was also rejected as the paper does not discuss UX or mobile-specific implementation. The topics selected (5.A, 6.A, 8.A, 12.A) were flagged as medium to contextual relevance because the paper provides foundational algorithmic knowledge that can inform Odin's module design but lacks domain-specific application or empirical validation in PFMS. Borderline cases included the discussion of multiclass classification (ECOC) for 5.C (Classification Approaches), but the paper's coverage is too general to justify high relevance. Overall, the paper offers valuable theoretical grounding for Odin's algorithmic architecture and evaluation, but its survey nature limits direct actionable insights.
limitations:
  - "No empirical validation or direct application to financial data is provided."
  - "Computational complexity analysis does not consider mobile device resource constraints. [unacknowledged]"
  - "Cold-start challenges and user-specific adaptation are not addressed. [unacknowledged]"
remember_this:
  - "Ensemble methods combine multiple models to improve predictive accuracy, robustness, and generalization."
  - "Boosting and bagging address bias and variance respectively, with boosting often outperforming on low-noise data."
  - "Random forests and GBDTs are powerful techniques for tabular data, often outperforming deep learning."
  - "Diversity among classifiers is critical for ensemble performance and can be measured using the Q-statistic."
  - "Integrating ensemble learning with deep learning can enhance reliability at moderate computational cost."
```
---

## Paper 19: Tjostheim_summarized.md

**Source File:** `Tjostheim_summarized.md`

```yaml
paper_id: "e9e3a3a6-6b7a-5a1c-8f2e-4d3b2a1c0d5e"
designation: "international"
title: "Selected Topics in Time Series Forecasting: Statistical Models vs. Machine Learning"
authors: "Tjøstheim, D."
year: 2025
venue: "Entropy"
odin_topics:
  - "1.C"
  - "5.C"
  - "6.A"
  - "6.B"
  - "7.A"
  - "7.B"
  - "8.B"
  - "12.A"
  - "12.B"
  - "12.C"
tldr: "This review compares statistical and machine learning forecasting methods across various settings, analyzing results from the M1-M6 competitions and discussing performance in volatility, multivariate, and weather forecasting."
problem_and_motivation: "Time series forecasting is critical across many domains, but choosing between traditional statistical models and modern machine learning methods remains challenging. A systematic comparison of their strengths, weaknesses, and applicability under different data conditions is needed."
approach:
  - "Surveys classical parametric models including exponential smoothing, ARIMA, and state space models."
  - "Reviews nonlinear parametric models like threshold and STAR models, and nonparametric kernel methods."
  - "Presents neural network architectures for forecasting: CNNs, TCNs, RNNs, LSTMs, and Transformers."
  - "Describes random forest and gradient boosting (including Light-GBM) as key ML competitors."
  - "Analyzes results from the M1-M6 Makridakis forecasting competitions, comparing statistical and ML performance."
  - "Discusses ML applications in probability forecasting, volatility prediction, and multivariate settings."
  - "Examines the role of ML in weather forecasting, including GraphCast and GenCast."
findings:
  - "num: In the M5 competition, Light-GBM gradient boosting clearly outperformed simple methods like exponential smoothing."
  - "num: In the M6 competition, there was virtually no correlation between best forecasts and best investment decisions, with difficulty beating the S&P market index."
  - "num: The GenCast model beat the ENS ensemble forecast in 97.2% of 1320 targets for weather prediction."
  - "num: ML methods were superior for high-frequency, high-entropy time series, as seen in Kaggle web traffic data."
  - "In volatility forecasting, MLP and LSTM networks provided the best forecasts, especially when using intraday commonality information."
  - "Ensemble and hybrid methods (combining statistical and ML models) consistently performed best in recent competitions."
  - "ML methods have shown great success in weather forecasting, with GraphCast predicting 10-day conditions more accurately and much faster than HRES."
  - "The black-box nature of ML models is a major limitation, prompting the rise of XAI methods like SHAP and LIME."
  - "ML methods can effectively model long-range dependencies in time series, particularly via LSTMs and Transformers."
  - "Integrating ML with physical models (e.g., in weather forecasting) may be more beneficial than pure end-to-end ML approaches."
key_figures_tables:
  - "None."
key_equations:
  - equation: "y_{t+1} = \\alpha y_t + (1-\\alpha) \\hat{y}_t"
    explanation: "Simple exponential smoothing forecast recursion."
  - equation: "h_t = \\sigma_h(W_h x_t + U_h h_{t-1} + b_h)"
    explanation: "Recurrent neural network hidden layer update."
  - equation: "\\sigma_t^2 = \\omega + \\sum \\alpha_i \\epsilon_{t-i}^2 + \\sum \\beta_j \\sigma_{t-j}^2"
    explanation: "GARCH model for conditional variance forecasting."
definitions:
  - term: "ARIMA"
    definition: "Autoregressive Integrated Moving Average, a class of linear statistical models."
  - term: "LSTM"
    definition: "Long Short-Term Memory, a recurrent neural network architecture that avoids vanishing gradients."
  - term: "TCN"
    definition: "Temporal Convolutional Network, a CNN variant for sequential data using causal and dilated convolutions."
  - term: "Transformer"
    definition: "A neural network architecture using attention mechanisms to process sequences in parallel."
  - term: "XAI"
    definition: "Explainable Artificial Intelligence, a field focused on making black-box ML models interpretable."
  - term: "SHAP"
    definition: "SHapley Additive exPlanations, a game-theoretic method for explaining model predictions."
  - term: "GARCH"
    definition: "Generalized Autoregressive Conditional Heteroskedasticity, a model for financial volatility."
  - term: "NWP"
    definition: "Numerical Weather Prediction, the traditional physics-based approach to weather forecasting."
critical_citations:
  - "[Box & Jenkins, 1970] — Standard textbook for ARIMA modeling."
  - "[Hochreiter & Schmidhuber, 1997] — Introduced the LSTM architecture."
  - "[Makridakis & Hibon, 2000] — Report on the M3 forecasting competition."
  - "[Makridakis et al., 2020] — Report on the M4 forecasting competition."
  - "[Vaswani et al., 2017] — Introduced the Transformer model."
  - "[Lam et al., 2023] — Introduced the GraphCast weather forecasting model."
relevance:
  topics:
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "contextual"
      justification: "Provides general context on forecasting behavior but no specific Filipino data."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "Discusses ML methods like random forest and neural networks used for classification and prediction tasks."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Core review compares various predictive models directly relevant to forecasting spending."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Evaluates specific algorithms (ARIMA, LSTM, TCN, etc.) used for sequential time series forecasting."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "medium"
      justification: "Performance of forecasting models informs budget recommendation strategies."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "low"
      justification: "Indirectly relevant; forecasting accuracy is a prerequisite but not directly about budget allocation."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "medium"
      justification: "Discusses TCN and LSTM for anomaly detection and general time series analysis."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Detailed analysis of M-competition methodologies provides a strong evaluation framework."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Paper is a direct comparative evaluation of forecasting algorithms."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "medium"
      justification: "Competition evaluation metrics (e.g., RMSE, MAE) are directly applicable to evaluating budget recommendations."
  contribution: "This paper provides a comprehensive comparison of statistical and machine learning forecasting methods, which is directly applicable to selecting and evaluating the forecasting module in Odin. The analysis of M-competition results (M1-M6) informs the choice of algorithms and evaluation metrics for Odin's predictive models. The discussion on XAI techniques like SHAP is crucial for developing interpretable and trustworthy financial recommendations. The findings on hybrid and ensemble methods directly justify a combined modeling strategy for spending forecasting in Odin. The review of volatility and probability forecasting informs the design of uncertainty-aware modules for budget and anomaly detection."
  directly_justifies:
    - "Combining statistical and ML models generally yields superior forecasting performance."
    - "LSTM and TCN architectures are strong candidates for time series forecasting tasks."
    - "ML methods, particularly Light-GBM, excel with high-entropy or high-frequency data."
    - "Exponential smoothing remains a strong, simple baseline forecasting method."
    - "XAI methods like SHAP can help explain model predictions to build user trust."
  limits:
    - "The paper is a review and does not present a unified benchmark tailored to personal finance data."
    - "The black-box nature of many ML models is discussed but not fully resolved, though XAI is presented as a solution."
    - "The review does not specifically address the cold-start problem for financial behavioral profiles."
    - "It does not cover constrained optimization or infeasibility handling for budget allocation. [unacknowledged]"
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to the 'Forecasting Algorithms' (6.A, 6.B) and 'System Evaluation' (12.A, 12.B, 12.C) domains due to its detailed comparison of models and analysis of M-competition methodologies. Medium relevance was assigned to 'Anomaly Detection' (8.B) given the discussion of LSTM and TCNs, and 'Behavioral Classification' (5.C) for its coverage of ML classifiers. Low relevance was assigned to 'Budget Recommendation' (7.B) as the paper doesn't cover allocation strategies. Contextual relevance was assigned to 'Financial Behavior' (1.C) for providing general forecasting context, but with no specific Filipino focus. Domains like 'Mobile-First Design' (9.A, 9.B), 'Data Privacy' (10.A, 10.B), 'User Retention' (11.A, 11.B), and 'Savings & Debt' (13.A, 13.B, 13.C) were rejected as the paper's content does not address them. The paper is overall highly relevant to Odin's core predictive modeling and evaluation needs, providing a broad and evidence-based comparison of candidate methods."
limitations:
  - "The paper's competition analysis is primarily based on univariate time series, limiting its direct applicability to multivariate spending data."
  - "The evaluation does not systematically address the performance of methods on 'black swan' events or extreme quantiles."
  - "Many datasets in the reviewed competitions are not publicly available, hindering reproducibility of comparisons."
  - "The theoretical foundations of ML methods are less developed than those for statistical models, a limitation acknowledged in the review."
  - "The paper focuses on point and interval forecasts, with less emphasis on the full probabilistic distributions beneficial for budget management. [unacknowledged]"
remember_this:
  - "Hybrid models combining statistical and ML methods are consistently the most accurate."
  - "LSTM and TCN are strong forecasting candidates for sequential spending data."
  - "Light-GBM gradient boosting dominated the M5 competition for retail sales forecasting."
  - "Explainable AI (XAI) is crucial for building user trust in financial forecasts."
  - "Forecast accuracy depends heavily on data characteristics like entropy and frequency."
```
---

## Paper 20: Danach et al_summarized.md

**Source File:** `Danach et al_summarized.md`

```yaml
paper_id: 10.29020/nybg.ejpam.v18i4.6707
designation: international
title: "Toward Transparent Optimization: A Systematic Review of Explainable AI in Decision-Making Systems"
authors: "Danach, K.; Aly, W. H. F.; Tarhini, A.; Laouadi, S."
year: 2025
venue: "European Journal of Pure and Applied Mathematics"
odin_topics:
  - "7.D"
  - "8.A"
  - "8.B"
  - "9.A"
  - "10.A"
  - "10.B"
  - "12.A"
  - "12.B"
  - "12.C"
  - "13.A"
  - "13.B"
tldr: "A systematic review of how explainable AI techniques are integrated into optimization pipelines to improve transparency and trust in decision-making systems."
problem_and_motivation: "Complex optimization algorithms often function as black boxes, limiting trust, accountability, and regulatory compliance in high-stakes decisions. There is a lack of unified frameworks that systematically integrate explainability into optimization. This gap motivated a comprehensive review to synthesize the scattered literature and classify integration approaches."
approach:
  - "Systematic literature review covering publications from 2010 to December 2024."
  - "Searched Scopus, Web of Science, IEEE Xplore, and ACM Digital Library with XAI and optimization keywords."
  - "Screened 642 records, retained 187 after abstract review, and included 112 for in-depth synthesis."
  - "Proposed a taxonomy categorizing hybrid XAI-optimization approaches by explainability, complexity, and domain."
  - "Analyzed post-hoc methods like SHAP and LIME, and intrinsic methods like MILP with explainability constraints."
  - "Examined applications across healthcare, finance, logistics, and energy systems."
  - "Evaluated trade-offs between performance and interpretability through empirical examples."
  - "Discussed scalability challenges and the absence of standardized benchmarks for explainability."
  - "Highlighted future directions including explainable hyper-heuristics and compliance-aware frameworks."
  - "Provided a sector-level mapping of techniques, advantages, limitations, and open opportunities."
findings:
  - "num: The EXALT framework reduced explanation generation time by 72% while maintaining 98% solution optimality."
  - "num: Error reduction rates of 41–68% were observed compared to black-box optimization in healthcare and derivatives pricing."
  - "Explainable optimization can maintain near-optimal performance while providing actionable decision insights."
  - "Embedding interpretability constraints often preserves polynomial solvability in structured problems like shortest path."
  - "Constraints and regularizers can improve both interpretability and robustness of solutions."
  - "Feature-based interpretable surrogates improve solution quality and comprehensibility over existing approaches."
  - "Automated XAI (AutoXAI) frameworks enable principled selection of explainers based on fidelity, stability, and efficiency."
  - "Multi-objective clustering optimization balances cluster quality and interpretability, sometimes leading to NP-hard problems."
  - "Certificate-based verification provides formal guarantees on feasibility, optimality gaps, and stability."
  - "Explanations must be meaningful to domain experts, requiring interdisciplinary design."
key_figures_tables:
  - "Figure 1: Taxonomy of XAI techniques including post-hoc, intrinsic, and example-based methods → Structured landscape of XAI approaches."
  - "Figure 2: Overview of exact, approximate, and hybrid optimization methods → Highlights the gap in transparency."
  - "Figure 3: Annual publication trends from 2010–2024 → Shows accelerating growth after 2020."
  - "Figure 4: Top recurring keywords → Dominant themes are explainability, optimization, transparency, and decision-making."
  - "Figure 5: AutoXAI integration within workflows → Central role in balancing performance and explanation needs."
  - "Figure 6: Multi-objective clustering optimization → Trade-offs between clustering quality and interpretability constraints."
  - "Figure 7: Key limitations including scalability and lack of benchmarks → Identifies open research questions."
  - "Table 1: Comparative evaluation of XAI-optimization approaches → Highlights trade-offs in scalability, fidelity, and cost."
  - "Table 2: Cross-domain mapping of techniques, advantages, and limitations → Connects methods to sector-specific challenges."
  - "Table 3: Practical mapping with research opportunities → Summarizes domain-specific implementations and future work."
key_equations:
  - equation: "$\\min_x f(x) + \\lambda \\sum_{j=1}^k w_j \\|x - x^*_j\\|^2$"
    explanation: "EXALT framework for explanation-by-precedent using historical solution similarity."
  - equation: "$x^*_{t+1} = \\arg\\min_x [f(x) + \\gamma \\|x - x^*_t\\|^2]$"
    explanation: "Temporal smoothing for explanation continuity across decision points."
definitions:
  - term: "XAI"
    definition: "Explainable Artificial Intelligence—techniques to make AI outputs understandable to humans."
  - term: "SHAP"
    definition: "SHapley Additive exPlanations—a post-hoc method for feature importance based on game theory."
  - term: "LIME"
    definition: "Local Interpretable Model-agnostic Explanations—explains individual predictions with local surrogate models."
  - term: "MILP"
    definition: "Mixed-Integer Linear Programming—exact optimization method for problems with discrete and continuous variables."
  - term: "AutoXAI"
    definition: "Automated XAI—framework for automatic selection and tuning of explanation methods."
  - term: "L2O"
    definition: "Learning to Optimize—approach that uses machine learning to improve optimization processes."
  - term: "EXALT"
    definition: "Explainable Algorithmic Tools—framework for explainable optimization with precedent-based explanations."
  - term: "MCDM"
    definition: "Multi-Criteria Decision Making—methods for evaluating alternatives based on multiple criteria."
  - term: "GDPR"
    definition: "General Data Protection Regulation—EU regulation on data privacy and algorithmic accountability."
  - term: "NP-hard"
    definition: "A class of problems for which no polynomial-time solution is known, often requiring heuristics."
critical_citations:
  - "[Barredo Arrieta et al., 2020] — Foundational taxonomy for XAI concepts."
  - "[Heaton & Wu Fung, 2023] — Introduced the EXALT framework for explainable optimization."
  - "[Goerigk et al., 2024] — Proposed feature-based interpretable surrogates for optimization."
  - "[NIST, 2021] — Established four principles of explainable AI."
  - "[Bertsimas et al., 2020] — Presented optimization-based interpretable clustering."
relevance:
  topics:
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "medium"
      justification: "Certificate-based verification provides formal feasibility checks for constraints."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "XAI techniques like SHAP can explain anomalies in spending patterns."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "contextual"
      justification: "Discusses interpretability of ML models used for detection, but not specific algorithms."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "contextual"
      justification: "Mentions edge computing constraints but not mobile-specific design."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "Regulatory compliance like GDPR is central to explainability needs."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "high"
      justification: "Transparency is framed as essential for building trust and accountability."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses the lack of standardized evaluation benchmarks for explainability."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Covers evaluation of explanation fidelity, stability, and comprehensibility."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "contextual"
      justification: "Mentions multi-objective trade-offs but not specifically budget systems."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "low"
      justification: "Resource allocation examples in supply chain and healthcare, not savings."
    - code: "13.B"
      name: "Debt Management in PFMS"
      relevance: "low"
      justification: "No direct discussion of debt, though portfolio optimization touches on financial allocations."
  contribution: "This systematic review provides a structured taxonomy for integrating explainability into optimization pipelines, which can guide Odin's design for transparent budget recommendations and anomaly detection. The discussion of certificate-based verification supports Odin's need for explaining constraint satisfaction and infeasibility handling. The analysis of user trust and regulatory compliance directly justifies Odin's emphasis on data privacy and user-facing explanations. The review's sectoral mapping and future directions offer a roadmap for developing interpretable modules for savings and debt management within a PFMS context."
  directly_justifies:
    - "Explainable optimization can maintain near-optimal performance while providing actionable decision insights."
    - "Regulatory compliance is a central driver for explainability in financial systems."
    - "Certificate-based verification provides formal guarantees for constraint satisfaction and solution quality."
    - "AutoXAI frameworks enable principled selection of explainers based on multiple criteria."
    - "Lightweight explainable solvers are needed for edge and mobile environments."
  limits:
    - "The review is a systematic analysis and does not propose a new algorithm for Odin to adopt directly."
    - "No specific financial forecasting algorithms are evaluated; the focus is on optimization."
    - "The review does not address cold-start problems or user-declared constraints in personal finance."
    - "Enterprise integration challenges are discussed but not solved at a technical implementation level."
    - "The absence of standardized benchmarks for explainability limits direct comparison of methods."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed against this review paper. The domains flagged as most relevant are Data Privacy & User Trust (Topic 10.A, 10.B), System Evaluation (Topics 12.A, 12.B, and 12.C), and Anomaly Detection (Topics 8.A, 8.B) due to the paper's strong focus on transparency, accountability, and evaluation of explainable systems. The Budget Recommendation domain (Topic 7.D) is also relevant through certificate-based verification for constraint satisfaction. The Savings & Debt Management domain (Topics 13.A, 13.B) was considered but given low relevance as the paper does not address savings goals or debt directly, though portfolio optimization provides a financial parallel. The Expense Categorization and Behavioral Profiling domains were not selected as the review does not cover classification frameworks for spending data or user profiles. The Mobile-First Design domain (Topic 9.A) is contextual only, given a brief mention of edge computing. Overall, the paper's contribution is highly relevant for justifying the need for explainability and trust in Odin's budgeting and anomaly detection modules, but less so for core predictive modeling or domain-specific behavioral classification."
limitations:
  - "Primarily focuses on optimization algorithms, not on predictive forecasting models relevant for spending. [unacknowledged]"
  - "Does not propose a specific implementation framework for a personal finance management system. [unacknowledged]"
  - "The scalability of the discussed methods for personal finance data is not directly addressed."
  - "Relies on a systematic review of the literature and may not cover the most recent developments in the field."
  - "The trade-off between performance and interpretability is discussed qualitatively without providing quantitative guidance for specific applications."
remember_this:
  - "Explainable optimization can reduce error rates by 41–68% in complex domains."
  - "The EXALT framework cut explanation time by 72% while retaining 98% optimality."
  - "Transparency is essential for user trust and regulatory compliance in finance."
  - "Certificate-based verification offers formal guarantees for constraint satisfaction."
  - "Lightweight, domain-adaptable explainable solvers are a key future direction."
```
---

## Paper 21: Kim et al_summarized.md

**Source File:** `Kim et al_summarized.md`

```yaml
paper_id: 10.1007/s10462-025-11223-9
designation: international
title: A comprehensive survey of deep learning for time series forecasting: architectural diversity and open challenges
authors: Kim, J.; Kim, H.; Kim, H.; Lee, D.; Yoon, S.
year: 2025
venue: Artificial Intelligence Review
odin_topics:
  - 6.A
  - 6.B
  - 12.A
  - 12.B
  - 8.A
  - 8.B
  - 13.A
  - 13.B
  - 10.A
  - 2.D
tldr: A comprehensive survey of time series forecasting models, analyzing architectural diversity and open challenges.
problem_and_motivation: Time series forecasting is critical for decision-making but faces challenges from data complexity and limited model generalizability. Existing surveys lack timely analysis of the increasing architectural diversity and in-depth treatment of open challenges. This survey addresses these gaps to guide researchers.
approach:
  - The paper surveys historical and contemporary deep learning models for time series forecasting.
  - Models are categorized into fundamental architectures (MLPs, RNNs, CNNs, GNNs) and advanced approaches (Transformers, Mamba, diffusion, foundation models).
  - It analyzes the evolution of models, highlighting the renaissance in architectural diversity and the rise of hybrid and non-transformer-based models.
  - The survey provides an issue-driven analysis of key open challenges, including channel dependency, distribution shift, causality, feature extraction, model interpretability, and spatio-temporal forecasting.
findings:
  - num: The survey reviews the explosive growth in time series forecasting research, noting increasing model diversity.
  - num: Simple linear models (LTSF-Linear) have been shown to outperform some Transformer-based models, challenging the dominance of Transformers for TSF.
  - Channel-independent strategies can outperform channel-dependent ones on datasets with distribution shifts, highlighting a robustness trade-off.
  - The field is experiencing a "renaissance" of architectural exploration, with no single architecture dominating.
  - Key open challenges like distribution shift and channel correlation require dedicated handling methods.
key_figures_tables:
  - None.
key_equations:
  - equation: x̂_{t+1:t+h} = f(x_{t-p:t})
    explanation: Univariate forecasting using past p time steps.
  - equation: X̂_{t+1:t+h} = f(X_{t-p:t})
    explanation: Multivariate forecasting with multiple variables.
  - equation: MAE = (1/n)∑|y_t - ŷ_t|
    explanation: Mean Absolute Error for deterministic forecasts.
  - equation: MSE = (1/n)∑(y_t - ŷ_t)^2
    explanation: Mean Squared Error for deterministic forecasts.
definitions:
  - term: Time Series Forecasting (TSF)
    definition: Predicting future values based on sequential historical data.
  - term: Multivariate Time Series Forecasting (MTSF)
    definition: Forecasting using predictions from multiple variables simultaneously.
  - term: Long-term Time Series Forecasting (LTSF)
    definition: Forecasting for distant future horizons, often several months or years.
  - term: Channel Independent (CI) Strategy
    definition: Modeling each variable (channel) independently without learning inter-variable correlations.
  - term: Channel Dependent (CD) Strategy
    definition: Modeling and learning the correlations and dependencies between different variables.
  - term: Distribution Shift
    definition: Changes in the statistical properties of data over time, posing generalization challenges.
  - term: Mamba
    definition: A state space model (SSM) architecture with a selective mechanism for efficient sequence modeling.
  - term: PatchTST
    definition: A Transformer model that divides time series into patches for improved performance.
  - term: iTransformer
    definition: An inverted Transformer that applies attention across variables instead of time steps.
  - term: LTSF-Linear
    definition: A simple linear model that outperformed some complex Transformers for time series forecasting.
critical_citations:
  - "[Zeng et al., 2023] — Showed simple linear models can outperform Transformers."
  - "[Vaswani et al., 2017] — Introduced the Transformer architecture."
  - "[Gu and Dao, 2024] — Introduced the Mamba architecture."
  - "[Nie et al., 2023] — Introduced the PatchTST model and channel independence."
  - "[Liu et al., 2024c] — Introduced the iTransformer model and channel dependence."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Surveys general predictive modeling approaches for time series, including Transformers and MLPs.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: Reviews numerous forecasting algorithms (RNN, CNN, Transformer, etc.) applicable to spending data.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: low
      justification: Provides an overview of evaluation metrics for time series, which can inform evaluation design in PFMS.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: low
      justification: Describes how different algorithmic modules (e.g., attention, patching) impact performance, informing evaluation.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Mentions anomaly detection but focuses on forecasting, not providing specific design guidance for Odin's anomaly module.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: Briefly references anomaly detection in the context of time series but lacks algorithmic details.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: contextual
      justification: Discusses forecasting, which is a prerequisite for savings projections, but not savings management itself.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: contextual
      justification: Similar to 13.A, forecasting is foundational for debt planning, but the paper doesn't address debt management.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Does not discuss privacy, but mentions data scarcity and security as challenges for time series data collection.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Discusses seasonal and cyclical patterns generally, which is relevant to spending cycles, but no Filipino-specific context.
  contribution: This survey provides a comprehensive overview of the current landscape of deep learning for time series forecasting, systematically categorizing models and highlighting key open challenges. It offers Odin's development team a structured understanding of architectural choices, from established models like Transformers to emerging ones like Mamba. The paper's analysis of channel dependency and distribution shift directly informs the design of Odin's forecasting and anomaly detection modules. The discussion of evaluation metrics and open challenges provides a foundation for building a robust and adaptable PFMS.
  directly_justifies:
    - "The choice between channel-independent and channel-dependent strategies significantly impacts forecasting performance on multivariate data."
    - "Simple linear models can be effective baselines for time series forecasting, challenging the assumption that complex models are always necessary."
    - "Distribution shift is a critical challenge that must be addressed for robust real-world forecasting."
    - "Patching techniques are an effective way to apply Transformers to time series data, improving performance and computational efficiency."
  limits:
    - "The survey focuses on a general overview of methods but does not provide in-depth implementation details for specific algorithms."
    - "The application of these models is discussed in a generic context and does not include domain-specific adaptations for personal finance or the Filipino context."
    - "The survey is a review of existing literature and does not present new empirical results or a novel methodology for Odin."
    - "It does not discuss the computational cost or latency constraints, which are critical for a mobile-first PFMS."
  mapping_rationale: A systematic scan of all 12 functional domains and associated topic codes was performed. The paper's focus on time series forecasting algorithms (6.A, 6.B) and evaluation methodologies (12.A, 12.B) was deemed of medium relevance, as these directly inform the design of Odin's forecasting engine and its performance assessment. The discussion of anomaly detection (8.A, 8.B) and savings/debt management (13.A, 13.B) was considered contextual, as the paper deals with forecasting as a prerequisite rather than the management process itself. The sections on distribution shift and feature extraction, while not explicitly tied to a single Odin topic, are of low relevance to 10.A and 2.D as they inform the robustness of forecasting models against data challenges. Topics related to Filipino cultural context (2.A, 2.B, 2.C), expense categorization (3.A, 3.B), existing systems (4.A, 4.B), behavioral profiling (5.A, 5.B, 5.C), budgeting (7.A, 7.B, 7.C, 7.D), mobile design (9.A, 9.B), user trust (10.B), engagement (11.A, 11.B), and specific system evaluation (12.C) were rejected as they were not addressed by the paper's content. The overall relevance of this paper to Odin is in providing a high-level, comprehensive reference for the state-of-the-art in time series forecasting.
limitations:
  - "The paper is a survey and does not propose a new model or methodology."
  - "It does not provide specific guidance on implementation for resource-constrained, mobile-first environments."
  - "The analysis of open challenges is comprehensive but lacks a deep dive into any single challenge, which is needed for Odin's specific modules."
  - "No discussion on the integration of forecasting results with downstream financial planning tasks like budget allocation or anomaly explanation."
remember_this:
  - "Time series forecasting is experiencing a renaissance of architectural diversity beyond Transformers."
  - "Simple linear models can outperform complex Transformers for long-term forecasting."
  - "Channel dependency strategies show a robustness trade-off against distribution shifts in data."
  - "Patching is a key technique to enhance Transformer performance on time series data."
  - "Mamba is an emerging state space model architecture for efficient sequence forecasting."
```
---

## Paper 22: Saeedian_summarized.md

**Source File:** `Saeedian_summarized.md`

```yaml
paper_id: 4d2c6b1a-4f2a-5b3c-9e1f-8a7b6c5d4e3f
designation: international
title: A Comparative Review of Electricity Load Forecasting Methods Across Temporal Horizons
authors: Saeedian, Z.
year: 2025
venue: Politecnico Di Milano
odin_topics:
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 7.C
  - 7.D
  - 12.B
  - 13.A
  - 4.A
  - 4.B
  - 8.A
  - 8.B
tldr: Accurate electricity load forecasting requires context-sensitive method selection balancing accuracy, interpretability, and data constraints across short-, medium-, and long-term horizons.
problem_and_motivation: No single forecasting model is universally optimal for electricity load prediction, as performance depends heavily on the temporal horizon, data availability, and system characteristics. Existing literature lacks a unified framework that aligns forecasting methods with both time horizons and data scales to guide practitioners.
approach:
  - Systematically reviews statistical, machine learning, deep learning, and hybrid forecasting methods.
  - Categorizes methods by three time horizons: short-term (up to 1 week), medium-term (1 week to 1 month), and long-term (beyond 1 month).
  - Analyzes method strengths, limitations, data requirements, and computational costs.
  - Proposes a classification framework linking forecasting methods to time horizons and spatial data scales.
  - Provides visual guides for model selection based on forecasting objectives and data conditions.
findings:
  - Statistical models like MLR and SARIMA are effective for short-term forecasting due to interpretability and low data demands.
  - Machine learning approaches (e.g., SVR, tree-based ensembles) offer improved flexibility for medium-term predictions.
  - Deep learning models (LSTM, Transformers) demonstrate superior performance for long-term forecasting by capturing complex temporal patterns.
  - Hybrid models (e.g., fuzzy-neural, CNN-LSTM, Transformer hybrids) achieve the highest accuracy but require significant data and computational resources.
  - num: LSTM outperformed SARIMA with a MAPE of 2.42% vs. higher values for SARIMA in a case study on Turkey's electricity consumption.
  - num: Hybrid ARIMA-LSTM model achieved a MAPE of 2.48% for medium-term forecasting.
  - num: XGBoost achieved the lowest MAPE of 1.88% among compared models for short-term forecasting in Algeria.
key_figures_tables:
  - "Figure 2.1: Load forecasting time horizons (short, medium, long). → Visualizes the temporal scope of forecasting categories."
  - "Figure 3.4: Schematic diagram of the LSTM architecture. → Shows gated structure enabling long-term dependency learning."
  - "Table 3.1: Strengths and limitations of regression methods in STLF. → Summarizes trade-offs for regression-based models."
  - "Figure 6.1: Forecasting horizon classification of methods. → Maps method types to their suitable time ranges."
  - "Figure 6.2: Scalability of methods based on spatial data availability. → Ranges from household to national level."
key_equations:
  - equation: $\\hat{Y} = \\beta_0 + \\beta_1 X_1 + \\beta_2 X_2 + ... + \\beta_n X_n + \\epsilon$
    explanation: Multiple linear regression equation for load forecasting.
  - equation: "$\\text{Attention}(Q,K,V) = \\text{softmax}\\left(\\frac{QK^T}{\\sqrt{d_k}}\\right)V$"
    explanation: Scaled dot-product attention mechanism for Transformer models.
definitions:
  - term: STLF
    definition: Short-Term Load Forecasting; prediction horizon from minutes to one week.
  - term: MTLF
    definition: Medium-Term Load Forecasting; prediction horizon from one week to one month.
  - term: LTLF
    definition: Long-Term Load Forecasting; prediction horizon beyond one month.
  - term: LSTM
    definition: Long Short-Term Memory; a recurrent neural network architecture for sequential data.
  - term: SARIMA
    definition: Seasonal AutoRegressive Integrated Moving Average; a statistical model for seasonal time series.
critical_citations:
  - "[Wang et al., 2021] — Defines time-based categorization of load forecasting."
  - "[Bilgili and Pinar, 2023] — Compares LSTM and SARIMA for national electricity forecasting."
  - "[Deng et al., 2022] — Introduces Bagging-XGBoost for extreme weather load forecasting."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly reviews predictive modeling techniques (statistical, ML, DL) for time-series forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Covers algorithms (ARIMA, LSTM, Transformers) applicable to sequential financial data.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Forecasting accuracy directly impacts the effectiveness of budgeting strategies.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: Provides the forecasting foundation necessary for generating accurate budget recommendations.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: contextual
      justification: Mentions optimization indirectly via hybrid model tuning, not budget allocation directly.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: contextual
      justification: Not addressed; focuses on forecasting accuracy, not constraint handling.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Systematically evaluates forecasting algorithms using metrics like MAE, RMSE, MAPE.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Accurate load (spending) forecasting is crucial for projecting savings capacity.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Provides generic context on energy systems, not PFMS-specific landscape.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies gaps like data quality, model complexity, and uncertainty in forecasting.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Discusses handling outliers and uncertainty, a prerequisite for anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Focuses on load forecasting accuracy, not specifically on anomaly detection algorithms.
  contribution: This thesis provides a comprehensive, structured review and classification of load forecasting methods, mapping them to specific time horizons and data scales. It offers direct justification for selecting appropriate forecasting algorithms (e.g., LSTM for long-term, SARIMA for short-term) within Odin's spending forecasting module. The framework can guide the design of Odin's predictive engine by balancing accuracy, interpretability, and computational cost. The findings on hybrid models inform potential architectural choices for robust forecasting. The discussion on data quality and uncertainty directly supports the development of reliable and trustworthy PFMS features.
  directly_justifies:
    - "SARIMA and MLR are suitable for short-term spending forecasting due to interpretability and low data needs."
    - "LSTM and Transformer-based models excel at capturing complex, long-term spending patterns."
    - "No single model is universally optimal; method selection must consider the forecasting horizon and data availability."
    - "Hybrid models improve accuracy but require more data and computational resources."
    - "Quantitative evaluation metrics like MAPE and RMSE are essential for comparing forecasting model performance."
  limits:
    - "The review is based on published literature, not empirical testing on PFMS datasets."
    - "Performance of hybrid models may vary significantly across different datasets."
    - "Probabilistic forecasting methods are only lightly discussed."
    - "Real-world constraints like missing data and stakeholder preferences were not modelled."
  mapping_rationale: A systematic scan across all 12 functional domains identified high relevance for spending forecasting (6.A, 6.B) and budget recommendation (7.A, 7.B), as the paper's core contribution is a review of forecasting methodologies. High relevance was also assigned to Algorithmic Evaluation (12.B) due to the detailed comparison of model performances using standard metrics. Medium relevance was assigned to Savings Goal Management (13.A) because forecasting is a prerequisite for projecting savings, and to Limitations/Gaps (4.B) as it discusses data and model challenges directly applicable to PFMS. Contextual relevance was assigned to Constrained Optimization (7.C), Infeasibility Handling (7.D), and Anomaly Detection (8.A) as the paper touches on optimization (for tuning) and uncertainty handling, which are related but not central. Low relevance was assigned to PFMS Landscape (4.A) and specific Anomaly Detection algorithms (8.B). The paper's methodology of categorizing models by horizon and data scale is directly applicable to designing Odin's forecasting engine, though it is not a PFMS study itself.
limitations:
  - "The review is based on published literature and benchmark datasets, not empirical testing on PFMS-specific spending data."
  - "Real-world constraints such as missing data, organizational capacity, and stakeholder preferences were not modelled."
  - "Probabilistic forecasting methods, which incorporate uncertainty in output, were only lightly discussed."
  - "Hybrid model performance may vary significantly across datasets and implementations."
remember_this:
  - "Forecasting accuracy depends on matching model type to the prediction time horizon."
  - "LSTM outperformed SARIMA, achieving a MAPE of 2.42% for monthly electricity demand."
  - "Hybrid models achieve the highest accuracy but require substantial data and resources."
  - "Statistical models are preferred for interpretability in short-term operational planning."
  - "No single forecasting model is universally optimal for electricity load prediction."
```
---

## Paper 23: Chowdury et al_summarized.md

**Source File:** `Chowdury et al_summarized.md`

```yaml
paper_id: 10.63125/mbbfw637
designation: international
title: A SYSTEMATIC REVIEW OF DEMAND FORECASTING MODELS FOR RETAIL E-COMMERCE ENHANCING ACCURACY IN INVENTORY AND DELIVERY PLANNING
authors: Chowdhury, A. R.; Paul, R.; Rozony, F. Z.
year: 2025
venue: International Journal of Scientific Interdisciplinary Research
odin_topics:
  - 4.A
  - 4.B
  - 6.A
  - 6.B
  - 12.B
tldr: A systematic review of 72 studies categorizes demand forecasting models for e-commerce into statistical, machine learning, deep learning, and hybrid approaches, assessing their impact on inventory and delivery planning.
problem_and_motivation: Retail e-commerce demand forecasting faces challenges from volatile consumer behavior and complex logistics. Despite growing academic interest, there is a lack of comprehensive synthesis on the comparative effectiveness of various forecasting models. This gap hinders decision-makers in selecting appropriate models to improve inventory accuracy and delivery efficiency.
approach:
  - A systematic review was conducted following PRISMA guidelines to ensure transparency and rigor.
  - A comprehensive search across Scopus, Web of Science, IEEE Xplore, and ScienceDirect identified 284 articles published between 2010 and 2024.
  - Studies were screened based on relevance to e-commerce forecasting and inclusion of empirical performance evaluations, resulting in 72 eligible studies.
  - Data was extracted using a structured coding framework covering forecasting technique, dataset characteristics, and operational focus.
  - The synthesis categorized models into traditional statistical, machine learning, deep learning, and hybrid frameworks.
findings:
  - num: Traditional statistical models (ARIMA, SARIMA, Holt-Winters) were used in 21 of 72 reviewed studies, performing well for stable, seasonal demand.
  - num: Machine learning models appeared in 31 studies, improving forecast accuracy metrics like RMSE and MAPE by up to 20% over statistical methods.
  - num: Deep learning models (LSTM, GRU, CNN) were featured in 22 studies, excelling at capturing nonlinear patterns in high-volume e-commerce data.
  - num: Hybrid models (ARIMA + ML/DL) were the focus of 18 studies, combining interpretability with enhanced accuracy during promotional periods.
  - num: Integrating external data (weather, sentiment, social media) in 27 studies significantly improved forecast accuracy in volatile categories.
  - num: A 10% improvement in forecast accuracy is associated with a potential 25% reduction in inventory costs.
  - num: Deep learning models reduced overstock rates in high-SKU environments by up to 15% compared to traditional baselines.
  - Advanced machine learning models demonstrate high adaptability for short-term and medium-term forecasting.
  - Ensemble and hybrid strategies enhance robustness across volatile demand cycles and promotional events.
key_figures_tables:
  - Figure 1: Components of global e-commerce forecasting operations → Highlights integrated data sources and logistics synchronization.
  - Figure 2: Classical time series methods for retail forecasting → Shows application of ARIMA and smoothing techniques.
  - Figure 3: Major forecasting techniques used in demand forecasting → Categorizes traditional, ML, and hybrid models.
  - Figure 4: Foundational time series forecasting models → Illustrates ARIMA and exponential smoothing structures.
  - Figure 5: Machine learning models for nonlinear demand forecasting → Lists decision trees, random forests, and SVR.
  - Figure 6: Deep learning networks in retail forecasting → Shows LSTM, GRU, and CNN architectures.
  - Figure 7: Hybrid and ensemble forecasting approaches → Depicts ARIMA and ML/DL combination strategies.
  - Figure 8: Incorporating external signals in demand forecasting → Shows integration of weather and social media data.
  - Figure 9: Impact of forecasting accuracy on inventory replenishment decisions → Links forecast accuracy with inventory costs.
  - Figure 10: PRISMA methodology flowchart for study selection → Outlines the systematic review process.
key_equations:
  - equation: "RMSE = sqrt( (1/n) * sum_{t=1}^{n} (y_t - ŷ_t)^2 )"
    explanation: Measures forecast error, heavily penalizing large deviations.
  - equation: "MAPE = (1/n) * sum_{t=1}^{n} |(y_t - ŷ_t) / y_t| * 100"
    explanation: Scale-independent accuracy metric, useful for comparing products.
definitions:
  - term: ARIMA
    definition: AutoRegressive Integrated Moving Average, a statistical model for time series forecasting.
  - term: SARIMA
    definition: Seasonal ARIMA, extends ARIMA to account for seasonality in time series data.
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network capable of learning long-term dependencies.
  - term: GRU
    definition: Gated Recurrent Unit, a simpler recurrent neural network variant compared to LSTM.
  - term: CNN
    definition: Convolutional Neural Network, a deep learning model effective for detecting local patterns in data.
  - term: RMSE
    definition: Root Mean Squared Error, a metric that penalizes larger forecast errors.
  - term: MAPE
    definition: Mean Absolute Percentage Error, a scale-independent forecast accuracy metric.
  - term: SVR
    definition: Support Vector Regression, a machine learning model for nonlinear regression tasks.
  - term: TFT
    definition: Temporal Fusion Transformer, an attention-based model for interpretable time-series forecasting.
  - term: SKU
    definition: Stock Keeping Unit, a unique identifier for each distinct product and service.
critical_citations:
  - "[Bandara et al., 2019] — Highlights e-commerce demand differs from traditional retail."
  - "[Mosavi et al., 2020] — Deep learning methods show superior performance in economics."
  - "[Goedhart et al., 2023] — Modeling influence of returns for omni-channel retailers."
  - "[Gong, 2023] — Digital transformation of supply chain in retail and e-commerce."
  - "[Frei et al., 2022] — Mapping product returns processes in multichannel retailing."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides a landscape of forecasting models relevant to PFMS systems.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies limitations of traditional models in volatile e-commerce settings.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly reviews predictive modeling techniques for forecasting demand.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Comprehensively evaluates forecasting algorithms including LSTM and ARIMA.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Emphasizes empirical evaluation of forecasting models using metrics like RMSE and MAPE.
  contribution: This paper provides a structured taxonomy of forecasting models (statistical, ML, DL, hybrid) that Odin can directly adopt for its spending forecasting module. The comparative analysis of model performance under different data conditions (volatility, seasonality, promotional events) informs Odin's algorithm selection strategy for different user segments. Furthermore, the review's emphasis on hybrid models and external data integration offers a blueprint for Odin to enhance its forecasting accuracy and robustness. The discussion on practical evaluation metrics guides Odin's system evaluation framework for algorithmic performance.
  directly_justifies:
    - "Machine learning models improve forecast accuracy by up to 20% over statistical methods."
    - "Hybrid models combining ARIMA and LSTM reduce forecasting error during volatile periods."
    - "Integrating external variables like weather and sentiment significantly enhances forecast precision."
    - "Deep learning models capture nonlinearities and long-term dependencies in financial data."
    - "A 10% increase in forecast accuracy can reduce inventory costs by up to 25%."
  limits:
    - "The review focuses on retail e-commerce, not personal finance, so direct transferability of findings requires validation."
    - "The performance of advanced models (DL) depends on large datasets, which may not be available for new Odin users."
    - "Complexity and computational demands of deep learning models may hinder their deployment in mobile-first environments."
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The paper was flagged as highly relevant for the Spending Forecasting domain (topics 6.A, 6.B) because it directly reviews and compares various forecasting algorithms. It was considered relevant for Evaluation (topic 12.B) due to its detailed discussion of performance metrics. It provides contextual information for the Landscape of Existing Systems (4.A) and their Limitations (4.B), though these are not the paper's primary focus. Domains like Filipino Cultural Context, Expense Categorization, and Behavioral Profiling were considered and rejected as the paper does not address user behavior, cultural spending, or PFMS-specific categorization. Overall, the paper is highly relevant as an authoritative source on forecasting algorithms, offering insights into model selection, evaluation, and integration with external data.
limitations:
  - "The study's scope is limited to e-commerce retail, making direct application to personal finance forecasting an extrapolation."
  - "The review does not address the cold-start problem, a critical issue for personal finance applications with new users."
  - "The analysis of deep learning models focuses on accuracy without deeply exploring computational costs for mobile deployment."
  - "The systematic review synthesizes existing studies but does not present novel empirical experiments in the PFMS context."
  - "The review may underrepresent studies on interpretability and user trust, which are crucial for financial applications. [unacknowledged]"
remember_this:
  - "A 10% improvement in forecast accuracy can yield a 25% reduction in inventory costs."
  - "Machine learning models can cut forecasting error by up to 20% compared to traditional methods."
  - "Hybrid models balance interpretability and accuracy effectively for dynamic financial data."
  - "Integrating external data like sentiment and seasonality significantly improves forecasting robustness."
  - "Deep learning excels at capturing complex patterns in high-volume sequential transaction data."
```
---

## Paper 24: Nokhiz & Ruwanpathirana_summarized.md

**Source File:** `Nokhiz & Ruwanpathirana_summarized.md`

```yaml
paper_id: 10.23919/JSC.2025.0015
designation: international
title: Consumer Autonomy or Illusion? Rethinking Consumer Agency in the Age of Algorithms
authors: Nokhiz, P.; Ruwanpathirana, A. K.
year: 2025
venue: Journal of Social Computing
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.B
  - 2.D
  - 4.B
  - 5.A
  - 5.B
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 7.D
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 13.A
tldr: Formal analysis demonstrates that limited consumer agency from obligatory consumption, algorithmic persuasion, and work instability leads to financial ruin even for rational utility-maximizing agents.
problem_and_motivation: Consumers face systemic barriers and algorithmic manipulation that erode financial autonomy, yet the consequences of diminished agency are not formally understood. This gap prevents the design of effective interventions to protect consumer welfare and promote genuine agency.
approach:
  - Uses discounted utility models to analyze intertemporal consumption under agency constraints.
  - Constructs analytical scenarios for obligatory consumption, algorithmic impulse spending, and unpredictable work schedules.
  - Formalizes financial ruin as a state where assets reach zero within a finite time horizon.
  - Applies Jensen's inequality and concentration inequalities to prove ruin under concave utility.
  - Demonstrates that advance schedule knowledge (lookahead) significantly improves utility and reduces ruin risk.
findings:
  - num: Rational agents under obligatory consumption can achieve higher utility by consuming all assets and going to ruin within a finite time.
  - num: Under impulsive consumption with minimum subsistence, the probability of avoiding ruin decays exponentially with time.
  - num: Workers with k-step lookahead achieve utility that is Ω(k) greater than those without lookahead.
  - num: Low-income agents experience near-instantaneous ruin under impulsive consumption, while high-income agents show delayed collapse.
  - num: Agents with high-school education (lower discount factor) exhibit ruin within 20 steps, whereas college-educated agents show more spread in ruin times.
  - Consumer agency must be treated as a value requiring active cultivation, not an inherent given.
  - Value deliberation interventions enable consumers to avoid ruin when income covers basic needs.
key_figures_tables:
  - "Figure 1: Summary of limited agency scenarios and outcomes → Visualizes how obligatory, impulsive, and temporal constraints lead to ruin."
  - "Figure A1: Ruin times under algorithmic persuasion → Most agents ruin within first 10 months under impulsive consumption."
  - "Figure A2: Ruin times by income level → Low-income agents ruin instantly; high-income show delayed but still rapid ruin."
  - "Figure A3: Ruin times by education → High-school diploma holders ruin within 20 steps; college degree holders show more spread."
key_equations:
  - equation: "max E[∑_{t=0}^{∞} β^t u(c_t)]"
    explanation: "Maximizes discounted utility over infinite horizon."
  - equation: "a_{t+1} = R(a_t - c_t) + y_t"
    explanation: "Asset evolution equation with return R and income y."
  - equation: "0 ≤ c_t ≤ a_t"
    explanation: "Consumption constrained by available assets."
  - equation: "Pr(a_T ≤ 0) ≥ 1 - exp(-cT)"
    explanation: "Probability of ruin grows exponentially with time."
definitions:
  - term: Ruin
    definition: "State where consumer assets reach zero within a finite time horizon."
  - term: Lookahead
    definition: "Number of future time steps an agent can perfectly foresee income and financial shocks."
  - term: Obligatory Consumption
    definition: "Fixed expenses driven by social, legal, or infrastructural pressures that limit consumer choice."
  - term: Algorithmic Persuasion
    definition: "Manipulative digital tactics that steer consumers toward impulsive spending."
  - term: Value Deliberation
    definition: "Active evaluation of competing needs and preferences to make consumption decisions aligned with personal values."
critical_citations:
  - "[Pariser, 2011] — Introduces filter bubbles and algorithmic curation."
  - "[Mathur et al., 2019] — Documents dark patterns in digital interfaces."
  - "[Nguyen, 2024] — Defines value capture in algorithmic systems."
  - "[Frederick et al., 2002] — Reviews time discounting and preference."
  - "[Schneider & Harknett, 2019] — Documents work schedule instability effects."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: low
      justification: "Discusses general consumer agency, not specific to Filipino young professionals."
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: low
      justification: "Uses U.S. income data and models, not Philippine-specific financial structures."
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: low
      justification: "Provides general behavioral insights applicable broadly."
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: high
      justification: "Formalizes predictable spending cycles through fixed obligatory consumption patterns."
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: medium
      justification: "Obligatory consumption framework applies to cultural spending cycles."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: "Identifies algorithmic manipulation and lack of agency as key system gaps."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: "Models rational agent behavior under agency constraints and proposes profiles for deliberation."
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: "Discusses adaptation and value deliberation over time."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: contextual
      justification: "Uses predictive models of ruin but does not focus on forecasting algorithms."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: contextual
      justification: "Mentions lookahead but not specific forecasting algorithms."
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: "Proposes value deliberation and budgeting as solutions to agency erosion."
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: "Demonstrates that deliberate consumption choices improve financial outcomes."
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: high
      justification: "Introduces minimum subsistence constraints and shows how to avoid ruin with proper budgeting."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: "Ruin analysis provides a framework for detecting financial instability."
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: "Mentions detection of impulsive spending but not specific algorithms."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: "Does not address privacy or security directly."
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: "Discusses transparency and ethical AI as trust-building mechanisms."
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: "Analyzes how algorithmic persuasion manipulates engagement and spending."
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: high
      justification: "Algorithmic tactics like scarcity and FOMO are explicitly linked to retention and spending."
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: "Proves that value deliberation and budgeting enable saving and avoid ruin."
  contribution: "This paper provides a formal framework for analyzing consumer agency erosion, which can inform Odin's design of user-facing budget recommendation and behavioral profiling modules. Its analytical models of ruin under limited agency justify the need for proactive intervention mechanisms in PFMS. The proposed value deliberation approach aligns with Odin's goal of fostering user autonomy and financial well-being. The theorem on lookahead utility directly supports incorporating schedule-aware features for users with variable income."
  directly_justifies:
    - "Even rational utility-maximizing agents can face financial ruin when agency is limited across structural, behavioral, or temporal dimensions."
    - "Value deliberation and budgeting interventions can help consumers avoid financial ruin when income covers basic needs."
    - "Workers with greater advance knowledge of income schedules achieve significantly higher utility, supporting the need for prediction-aware features."
    - "Algorithmic persuasion creates value capture where consumers adopt externally imposed consumption values without critical reflection."
  limits:
    - "Model assumes rational utility-maximizing agents, which may not reflect real-world behavioral biases."
    - "Does not include debt, credit, or liabilities in the formal model."
    - "Assumes societal uniformity; does not account for disparities in algorithmic targeting or policy access."
    - "Proposed interventions are high-level and lack specific implementation details for PFMS."
  mapping_rationale: "Systematic scan across all 12 functional domains identified 4 domains as highly relevant: Filipino Cultural Context (2.B, 2.D), Behavioral Profiling (5.A), Budget Recommendation (7.A, 7.D), and User Retention (11.A, 11.B). The paper's formal models of obligatory consumption (2.B) and algorithmic persuasion (11.A) provide direct justification for Odin's budgeting and engagement modules. The lookahead theorem (6.A, 6.B) supports forecasting features. Expense Categorization (3.A-C) and Anomaly Detection (8.A-C) were considered but rejected as the paper does not address categorization algorithms or anomaly detection techniques. Mobile-First Design (9.A, 9.B) and Data Privacy (10.A) were considered contextual. The paper's overall relevance to Odin is high, providing theoretical justification for user autonomy and proactive intervention features."
limitations:
  - "Intertemporal consumption model assumes rational utility-maximizing agents, simplifying real-world behavioral complexity."
  - "Debt and liabilities are not included in the formal framework."
  - "Model assumes societal uniformity and does not account for demographic disparities in algorithmic targeting."
  - "Proposed interventions are high-level and lack specific implementation details."
  - "Behavioral economics factors like present bias and loss aversion are acknowledged but not formally incorporated. [unacknowledged]"
  - "External macro-socioeconomic impacts like inflation and recessions are not modeled. [unacknowledged]"
remember_this:
  - "num: Even rational consumers can go to ruin under obligatory consumption with concave utility."
  - "num: Probability of avoiding ruin decays exponentially under impulsive consumption with minimum subsistence."
  - "num: Workers with advance schedule knowledge achieve Ω(k) higher utility than those without."
  - "Consumer agency must be actively cultivated as a value, not assumed as a given."
  - "Value deliberation and budgeting interventions enable consumers to avoid financial ruin."
```
---

## Paper 25: Gouni_summarized.md

**Source File:** `Gouni_summarized.md`

```yaml
paper_id: 10.32996/jcsts.2025.7.5.74
designation: international
title: Evolution of Machine Learning: A Foundation for Intelligent Systems
authors: Gouni, M. R.
year: 2025
venue: Journal of Computer Science and Technology Studies
odin_topics:
  - 8.B
  - 6.B
  - 12.B
  - 12.C
tldr: A review of machine learning evolution in fraud detection, covering supervised, unsupervised, and deep learning techniques with an emphasis on anomaly detection, forecasting, and evaluation.
problem_and_motivation: Traditional rule-based fraud detection systems are inadequate against evolving, sophisticated fraud tactics. There is a critical need for adaptive, proactive systems that can learn from data and detect novel patterns without requiring constant manual updates. This review synthesizes the progression of machine learning solutions to address this gap.
approach:
  - This is a systematic literature review that surveys the evolution of machine learning in fraud detection.
  - It synthesizes findings from seminal and recent papers on supervised, unsupervised, and deep learning models.
  - The review covers logistic regression, decision trees, random forests, gradient boosting, and deep neural networks.
  - It also examines clustering algorithms like k-means and DBSCAN, and autoencoders for anomaly detection.
  - The survey covers sequential models (RNN, LSTM, GRU) and spatial models (CNN) for transaction monitoring.
  - It discusses future directions including hybrid architectures, federated learning, and adversarial techniques.
  - The review addresses challenges like class imbalance, concept drift, and the need for explainable AI.
findings:
  - num: Ensemble and deep learning approaches consistently outperform single-classifier methods in fraud detection.
  - num: Deep learning architectures like LSTM and CNN can maintain real-time performance with GPUs and optimized inference.
  - Autoencoders effectively identify anomalies through reconstruction error, capturing complex non-linear patterns.
  - Hybrid systems combining multiple model types provide superior resilience against diverse fraud attack vectors.
  - Adaptive frameworks with drift-detection mechanisms maintain long-term detection performance and reduce false positives.
key_figures_tables:
  - Figure 1: Evolution of supervised learning models in fraud detection → Shows progression from logistic regression to deep neural networks.
  - Figure 2: Unsupervised learning for novel fraud pattern detection → Illustrates clustering and autoencoder-based anomaly detection.
  - Figure 3: Deep learning applications in transaction monitoring → Depicts RNN and CNN architectures for sequential and spatial pattern recognition.
  - Figure 4: Future directions and challenges in ML-based fraud detection → Summarizes hybrid, federated, and explainable AI approaches.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: None.
    definition: ""
critical_citations:
  - "[Dal Pozzolo et al., 2017] — Realistic modeling and novel learning strategy for fraud detection."
  - "[Du et al., 2023] — AutoEncoder and LightGBM for credit card fraud detection problems."
  - "[Sezer et al., 2020] — Systematic literature review on deep learning for financial time series forecasting."
  - "[Carminati et al., 2018] — Security evaluation of banking fraud analysis systems."
relevance:
  topics:
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Reviews anomaly detection techniques like autoencoders and clustering for fraud detection.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: Discusses RNNs, LSTMs, and GRUs for modeling sequential financial transaction data.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: low
      justification: Mentions performance metrics like accuracy, false positive rates, and resilience evaluation.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: contextual
      justification: The review's focus on evaluation frameworks for fraud detection is broadly relevant to system evaluation.
  contribution: This paper provides a comprehensive but general survey of ML techniques for fraud detection. While not specific to personal finance management, its review of anomaly detection (8.B) and forecasting algorithms (6.B) offers a foundational understanding of these techniques. The discussion on evaluation frameworks (12.B) is applicable to Odin's algorithmic modules. The paper's focus is on financial fraud, which is a different domain than budget recommendation, but the algorithmic principles are transferable. Its value to Odin is primarily contextual, providing a high-level overview of relevant ML paradigms.
  directly_justifies:
    - "Ensemble methods like random forests and gradient boosting improve robustness in imbalanced classification tasks."
    - "Recurrent neural networks, particularly LSTMs, are effective for modeling dependencies in sequential transaction data."
    - "Autoencoders can detect anomalies by measuring reconstruction error in transaction data."
    - "Hybrid architectures combining multiple model types can provide superior resilience to diverse attack patterns."
  limits:
    - "The paper is a general survey and does not provide specific implementation details or empirical results for Odin's context."
    - "It focuses on fraud detection, which is a distinct application from budget recommendation and spending behavior analysis."
    - "The review does not address Filipino-specific financial practices, seasonal spending, or cultural factors."
    - "It does not discuss cold-start problems or user behavioral profiling in the context of personal finance."
    - "The paper lacks specific evaluation methodologies that could be directly applied to a budget recommendation system."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The only areas with any relevance were those related to algorithmic techniques. The paper's focus on forecasting (6.B), anomaly detection (8.B), and evaluation (12.B, 12.C) flagged them as relevant, albeit with low or contextual relevance. Domains like Filipino Cultural Context (2.A-D), Expense Categorization (3.A-C), Behavioral Profiling (5.A-C), and Savings & Debt Management (13.A-C) were considered and rejected as the paper does not address these personal finance topics. The paper's contribution is purely algorithmic and methodological, with no connection to user-facing design, cultural context, or financial planning. The overall relevance to Odin is low, serving only as a general background on machine learning techniques for financial data analysis.
limitations:
  - "This is a review paper and does not present novel empirical results or a specific proposed model. [unacknowledged]"
  - "The paper does not address the specific challenges of personal finance management, such as user-defined constraints or budget allocation. [unacknowledged]"
  - "It lacks a discussion on cold-start problems or user profiling, which are critical for Odin. [unacknowledged]"
  - "The review does not cover mobile-first design, data privacy, or user engagement, which are essential for Odin's PFMS context. [unacknowledged]"
remember_this:
  - "Ensemble and deep learning models significantly outperform traditional classifiers in financial anomaly detection."
  - "Recurrent neural networks effectively model sequential transaction data for identifying temporal fraud patterns."
  - "Autoencoders detect anomalies by calculating reconstruction error without requiring labeled fraud examples."
  - "Hybrid model architectures provide greater resilience against complex and evolving financial threats."
  - "Adaptive learning systems maintain detection accuracy by continuously updating to evolving transaction patterns."
```
---


---

## Agent Instruction

If the agent reading this document believes further context about a paper is needed, it may request the original converted markdown file (with the '_marked' suffix) from the user for the relevant paper(s).
