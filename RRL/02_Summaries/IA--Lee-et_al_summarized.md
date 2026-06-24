```yaml
paper_id: 10.1080/13696998.2026.2630598
designation: international
title: Comparing deep learning and classical regression approaches for predicting healthcare expenditure and spending: a systematic review
authors: Lee, J. T.; Yeh, M. H.-S.; Li, V. C.-S.; Chen, H.-H.; Liu, Y.-H.; Chen, Y.-C.; Wu, D. B.-C.
year: 2026
venue: Journal of Medical Economics
odin_topics:
  - 3.A
  - 4.A
  - 5.A
  - 6.A
  - 6.B
  - 7.A
  - 8.B
  - 12.A
  - 12.B
  - 12.C
tldr: Deep learning excels in longitudinal, sequence-rich cost forecasting, while tree-based methods remain highly competitive for cross-sectional tabular prediction.
problem_and_motivation: Accurate prediction of individual healthcare costs is crucial for insurance underwriting, risk adjustment, budget planning, and value-based payment strategies. Traditional statistical approaches often struggle to capture complex nonlinear interactions in health data, but a clear understanding of when deep learning offers a meaningful advantage over classical methods is lacking.
approach:
  - A preregistered systematic review (PROSPERO CRD420251129440) was conducted.
  - Searches were performed in Web of Science, PubMed, Embase, and Scopus through August 2025.
  - Eight studies were included that used real-world individual-level data and directly compared a deep learning architecture with a classical regression comparator.
  - Data were extracted on population, predictors, outcome horizon, model type, validation strategy, and performance metrics.
  - Findings were synthesized narratively, leading to the proposal of a Complexity-Performance Hypothesis.
findings:
  - "num: Sequential deep learning models showed approximately 10-20% reductions in RMSE/MAE over classical methods in longitudinal designs."
  - "num: R² improvements from deep learning ranged from 0.01 to 0.15 in various studies."
  - "num: Deep learning models achieved AUROC values up to 0.78 for high-risk classification of preventable hospitalizations."
  - Prior costs and utilization were consistently the strongest predictors across all studies.
  - For low-dimensional, structured, cross-sectional data, generalized linear models and tree-based approaches remain robust baselines.
  - A conceptual Complexity-Performance Hypothesis was formulated, linking model capacity to data complexity.
key_figures_tables:
  - "Figure 2: Conceptual model performance by data complexity → Deep learning excels in complex settings, while regression is best for simple data."
  - "Table 1: Characteristics of identified studies → Summary of study design, population, and models for all 8 included papers."
  - "Table 2: Model performance and features of included studies → Detailed comparative results for all studies."
  - "Table 3: Neural network architectures applied → Categorization of models by data type used."
  - "Table 4: Challenges of deep learning in spending prediction → Future strategies for interpretability, benchmarking, and generalizability."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: LSTM
    definition: Long short-term memory, a recurrent neural network architecture.
  - term: CNN
    definition: Convolutional neural network.
  - term: RNN
    definition: Recurrent neural network.
  - term: GLM
    definition: Generalized linear model.
  - term: RMSE
    definition: Root mean square error.
  - term: MAE
    definition: Mean absolute error.
  - term: AUROC
    definition: Area under the receiver operating characteristic curve.
  - term: EMR
    definition: Electronic medical records.
  - term: EHR
    definition: Electronic health records.
  - term: XAI
    definition: Explainable artificial intelligence.
critical_citations:
  - "[Drewe-Boss et al., 2022] — Provided a strong example of deep learning outperforming ridge regression."
  - "[Yang et al., 2018] — Showed RNN gains for high-cost patient forecasting."
  - "[Lewis et al., 2021] — Demonstrated LSTM and CNN superiority for preventable care prediction."
  - "[Esteva et al., 2019] — Cited for the promise of deep learning in healthcare."
  - "[Topol, 2019] — Cited for contextualizing the convergence of human and AI in medicine."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: The review discusses different outcome variables like total cost and pharmacy expenditure.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Reviews the predictive modeling landscape, which is relevant to PFMS.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Discusses predicting high-cost patients, analogous to financial profiling.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly compares forecasting models for expenditure, informing Odin's predictor selection.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Focuses on algorithms like LSTM and CNN-LSTM for sequential data, directly applicable to spending forecasting.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Finding on data complexity ties to optimal model choice for budget recommendation.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Discussion of identifying high-cost outliers relates to anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a systematic framework for comparing algorithmic modules, a core part of system evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Directly evaluates the performance of different algorithmic modules (deep learning vs. regression).
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: high
      justification: The systematic review methodology and metrics (RMSE, MAE, R²) are directly transferable to evaluating budget recommendation.
  contribution: This systematic review provides a clear, evidence-based framework for selecting between deep learning, tree-based, and regression models for spending prediction tasks. It directly informs Odin's algorithmic module selection by establishing that LSTM and CNN-LSTM models are best for longitudinal data, while simpler models are sufficient for cross-sectional data. The proposed Complexity-Performance Hypothesis can guide the design of Odin's forecasting and anomaly detection components.
  directly_justifies:
    - "Sequential deep learning models (LSTM, CNN-LSTM) offer clear predictive advantages for longitudinal spending data."
    - "Tree-based methods remain highly competitive for cross-sectional, tabular spending prediction."
    - "Prior costs and utilization are consistently the strongest predictors of future spending."
    - "The complexity of the data should dictate the choice of the forecasting model."
  limits:
    - "Review based on a small and heterogeneous set of eight studies, limiting generalizability."
    - "None of the studies performed full external validation across independent datasets."
    - "The review's findings are based on healthcare data, not personal finance data, which may have different characteristics."
    - "The Complexity-Performance Hypothesis is a conceptual framework requiring further systematic validation."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to the 'Spending Forecasting' domain (codes 6.A, 6.B) as it is a systematic review directly comparing forecasting algorithms. It also has high relevance to the 'System Evaluation' domain (codes 12.A, 12.B, 12.C) due to its focus on comparative performance metrics and evaluation frameworks. The paper provides medium relevance to 'Behavioral Profiling & Classification' (5.A) through its discussion of predicting high-cost populations, and 'Anomaly Detection' (8.B) via high-cost outlier identification. It offers contextual relevance to 'Expense Categorization' (3.A) and the 'Existing Systems' landscape (4.A). Domains such as Filipino Cultural Context, Mobile-First Design, and Data Privacy were considered and rejected because the paper does not address these topics. The 'Budget Recommendation' domain (7.A) is considered medium relevance as the findings on data complexity guide model choice for such recommendations. Overall, the paper provides strong empirical justification for model selection in Odin's forecasting and evaluation modules.
limitations:
  - "The evidence base is small (n=8) and heterogeneous in design and data sources."
  - "Prediction horizons are predominantly short-term (one year), limiting assessment of long-term performance. [unacknowledged]"
  - "Social determinants of health and behavioral predictors are rarely incorporated into the models. [unacknowledged]"
  - "None of the studies performed full external validation. [unacknowledged]"
  - "Assessments of calibration, fairness, and economic interpretability were sparse or absent. [unacknowledged]"
  - "The Complexity-Performance Hypothesis is a working hypothesis derived from a limited set of studies, not a definitive causal mechanism. [acknowledged]"
remember_this:
  - "Deep learning excels for longitudinal, sequence-rich cost forecasting."
  - "Tree-based methods are highly competitive for cross-sectional tabular data."
  - "Model accuracy is maximized when capacity is matched to data complexity."
  - "Prior costs and utilization are the strongest predictors of future spending."
  - "LSTM and CNN-LSTM hybrids reduced forecasting error by up to 20% in some studies."
```