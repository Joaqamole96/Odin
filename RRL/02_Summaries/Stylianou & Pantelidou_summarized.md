```yaml
paper_id: 10.3934/QFE.2025024
designation: international-algorithm-specific
title: Big data and consumer behavior: A macroeconomic perspective through supermarket analytics
authors: Stylianou, T.; Pantelidou, A.
year: 2025
venue: Quantitative Finance and Economics
odin_topics:
  - 5.A
  - 5.C
  - 6.A
  - 6.B
tldr: Supermarket transaction data analyzed with machine learning and ARIMA models reveals consumer behavior patterns that serve as real-time indicators of economic sentiment and household financial health.
problem_and_motivation: Most big data retail studies focus on firm-level outcomes like personalization and operational efficiency, overlooking the potential of aggregated consumer transaction data to signal macroeconomic conditions. There is a gap in linking micro-level purchasing patterns to macro-level economic interpretations such as consumer confidence and inflation expectations. This study addresses this gap by applying advanced analytics to supermarket data to inform both retail strategy and economic policy.
approach:
  - Used a Kaggle dataset of 2,019,501 online supermarket transactions from a multinational chain operating in 10 countries.
  - Applied K-means clustering to segment customers based on purchasing behavior, with the optimal number of clusters determined using the elbow method.
  - Implemented the Apriori algorithm for frequent itemset mining and association rule discovery with a minimum support of 0.01 and confidence of 0.6.
  - Evaluated five recommendation algorithms, selecting item-based collaborative filtering for its balance of precision, recall, and practical execution time.
  - Employed an ARIMA(2,1,1) model for time series forecasting, selected based on AIC/BIC criteria and significant autocorrelation in the data.
findings:
  - num: 6.3% mean absolute percentage error for the ARIMA(2,1,1) forecast, indicating high accuracy for short-term demand prediction.
  - AR(1) coefficient of 0.61 confirmed that consumer behavior is largely habitual and strongly influenced by recent purchases.
  - The Apriori algorithm identified 2317 valid association rules, with fresh vegetables as a frequent consequent in rules with confidence above 92%.
  - K-means clustering produced five distinct customer segments, revealing heterogeneous preferences for departments like produce and dairy/eggs across clusters.
  - Item-based collaborative filtering demonstrated superior performance for recommendations, balancing precision and recall with manageable computational overhead.
  - Purchasing patterns showed bimodal order intervals with peaks at 7 and 30 days, indicating both weekly and monthly shopping cycles.
key_figures_tables:
  - Figure 2: Order distribution by day → Mondays and Tuesdays account for 35% of all orders.
  - Figure 4: Product department preferences → Produce and dairy/eggs comprise nearly half of all purchases.
  - Figure 5: ARIMA(2,1,1) forecast → Forecast closely aligns with preceding trajectory, validating short-term trend extension.
  - Figure 7: Ten association rules with highest lift → Fresh vegetables appear as consequent in all high-lift rules.
  - Figure 11: Department preference per cluster → Produce is top choice in three clusters, dairy/eggs in one.
key_equations:
  - equation: "Y_t = c + φ_1 y_{t-1} + φ_2 y_{t-2} + θ_1 ε_{t-1} + ε_t"
    explanation: ARIMA(2,1,1) captures autoregressive lags and a moving average term.
  - equation: "Support(I) = (Number of transactions containing I) / (Total number of transactions)"
    explanation: Support measures frequency of an itemset in transaction data.
  - equation: "Confidence(A → B) = Support(A ∪ B) / Support(A)"
    explanation: Confidence indicates conditional probability of B given A.
definitions:
  - term: ARIMA
    definition: Autoregressive Integrated Moving Average, a time series forecasting model.
  - term: BDA
    definition: Big Data Analytics, the process of examining large datasets to uncover patterns.
  - term: CLV
    definition: Customer Lifetime Value, a prediction of the net profit from a customer relationship.
  - term: CJA
    definition: Customer Journey Analytics, the analysis of customer paths across channels.
  - term: NCF
    definition: Neural Collaborative Filtering, a deep learning-based recommendation approach.
  - term: MAPE
    definition: Mean Absolute Percentage Error, a measure of prediction accuracy in forecasting.
  - term: CRISP-DM
    definition: Cross-Industry Standard Process for Data Mining, a widely used data mining framework.
critical_citations:
  - "[Einav and Levin, 2014] — Establishes economic relevance of big data for policy insights."
  - "[Gandomi and Haider, 2015] — Defines core 5Vs characteristics of big data."
  - "[Chen et al., 2012] — Demonstrates BDA's role in business intelligence and predictive analytics."
  - "[He et al., 2017] — Validates neural collaborative filtering for recommendation systems."
  - "[Fayyad et al., 1996] — Foundational work on knowledge discovery in databases."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Paper directly performs customer segmentation via K-means clustering, identifying distinct behavioral profiles.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Applies clustering and collaborative filtering to classify customer purchasing behaviors.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Uses ARIMA time series forecasting to model and predict spending patterns.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Employs ARIMA(2,1,1) specifically for sequential transaction data, achieving MAPE of 6.3%.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Identifies weekly and bimodal purchase cycles, but does not address Filipino-specific seasonality.
  contribution: The study's framework directly justifies Odin's behavioral profiling module by demonstrating that K-means clustering can segment users into distinct financial profiles. Its ARIMA forecasting approach validates Odin's predictive spending module, providing a method to anticipate user cash flow. The item-based collaborative filtering supports Odin's expense categorization and recommendation features by showing how collaborative techniques improve personalization. The paper's dual focus on retail analytics and macroeconomic insight provides a broader justification for Odin's design to help users understand their financial health in context.
  directly_justifies:
    - "K-means clustering can segment users into distinct purchasing profiles."
    - "ARIMA(2,1,1) achieves 6.3% MAPE for forecasting short-term spending patterns."
    - "Item-based collaborative filtering balances precision and recall for product recommendations."
    - "Consumer transaction data reflects habitual behavior, with AR(1) coefficient of 0.61."
  limits:
    - "The study uses a single supermarket chain's dataset, limiting generalizability to other retail contexts."
    - "The dataset is derived from online transactions only, not capturing offline or in-store behavior."
    - "Ethical considerations like privacy and algorithmic bias are discussed qualitatively but not empirically addressed."
    - "The focus is on short-term forecasting; long-term trend modeling is not explored."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was conducted. The domains flagged as relevant were Behavioral Profiling & Classification (high relevance for 5.A and 5.C), Spending Forecasting (high relevance for 6.A and 6.B), and Filipino Cultural Context (contextual relevance for 2.B due to general seasonal patterns). The paper's direct application of clustering for customer segmentation and ARIMA for forecasting strongly aligns with Odin's need for behavioral profiling and spending prediction. Borderline cases included the paper's mention of seasonal patterns (touching 2.B and 2.D) and user constraints (touching 3.C and 7.B), but these were not developed with sufficient depth to warrant inclusion as high relevance topics. Domains such as Expense Categorization, Budget Recommendation, Anomaly Detection, and Mobile-First Design were considered but rejected as the paper does not address their core concerns. The paper's international algorithmic focus makes it relevant primarily for Odin's algorithmic modules rather than its Filipino cultural contextualization.
limitations:
  - "Focus on a single supermarket chain may limit generalizability. [unacknowledged]"
  - "Analysis is based solely on transactional data, lacking demographic or psychographic customer attributes."
  - "Ethical considerations are discussed qualitatively without empirical evaluation or mitigation strategies."
  - "The study does not address integration challenges with external economic data sources."
remember_this:
  - "ARIMA(2,1,1) achieved 6.3% MAPE for forecasting short-term supermarket demand."
  - "K-means clustering identified five distinct customer segments with varying department preferences."
  - "Recent purchases (AR(1) = 0.61) are the strongest predictor of future buying behavior."
  - "Item-based collaborative filtering was the most practical recommendation approach."
  - "Transaction data can serve as an early indicator of economic sentiment."
```