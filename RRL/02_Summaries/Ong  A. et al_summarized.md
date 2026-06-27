```yaml
paper_id: 10.3390/wevj14080227
designation: local-algorithm-specific
title: Purchasing Intentions Analysis of Hybrid Cars Using Random Forest Classifier and Deep Learning
authors: Ong, A.K.S.; Cordova, L.N.Z.; Longanilla, F.A.B.; Caprecho, N.L.; Javier, R.A.V.; Borres, R.D.; German, J.D.
year: 2023
venue: World Electric Vehicle Journal
odin_topics:
  - 1.A
  - 1.C
  - 2.A
  - 6.A
  - 6.B
  - 7.A
  - 8.A
  - 12.A
  - 12.B
tldr: Filipino drivers' purchasing intentions for hybrid cars are predicted using random forest and deep learning, revealing that environmental concern, attitude, perceived control, and performance expectancy are the most influential factors.
problem_and_motivation: Hybrid cars are essential for reducing carbon emissions, yet their adoption in developing countries like the Philippines remains low. There is a need to understand the behavioral factors driving purchasing intentions to support sustainable transportation transitions.
approach:
  - Data were gathered from 1048 Filipino drivers using an online survey employing convenience and snowball sampling.
  - The study developed the Sustainability Theory of Planned Behavior (STPB) by integrating PEPB and UTAUT2 frameworks.
  - Machine learning algorithms including Decision Tree, Random Forest Classifier, and Deep Learning Neural Network were applied.
  - Model optimization involved testing various training-testing ratios, tree depths, activation functions, and optimizers.
  - A Taylor diagram was used to validate the accuracy of the different MLA models.
findings:
  - The Deep Learning Neural Network achieved the highest accuracy at 96.60% for predicting purchasing intentions.
  - Perceived Environmental Concern was the most important factor, followed by Attitude, Perceived Behavioral Control, and Subjective Norm.
  - The random forest classifier generated an accuracy of 94% with the optimum tree output.
  - Machine learning approaches provided more accurate results than Structural Equation Modeling for the large, complex STPB model.
  - Facilitating Conditions, Effort Expectancy, and Habit were found to be significant factors, contrasting with SEM results which deemed them insignificant.
key_figures_tables:
  - Figure 3: Deep learning neural network model architecture with 3 hidden layers → Achieved 96.60% accuracy.
  - Table 6: MLA versus SEM results for latent variables → MLA provided a clearer ranking, with PENC as 1st vs. 5th in SEM.
  - Table 2: Decision Tree summarized results → Highest accuracy of 72.32% with depth 5 and 90:10 split.
  - Table 3: Random Forest Classifier summarized results → Highest accuracy of 94% with Gini and best splitter.
  - Figure 4: Taylor Diagram for validation → Confirmed MLA outputs were acceptable with RMSE within 20%.
key_equations:
  - equation: tanh(x) = 2/(1+e^{-2x}) - 1
    explanation: Activation function for hidden layers enabling nonlinear relationships.
  - equation: sigmoid(x) = 1/(1+e^{-x})
    explanation: Output layer activation for probability-based classification.
definitions:
  - term: STPB
    definition: Sustainability Theory of Planned Behavior, integrating PEPB, UTAUT2, and economic concerns.
  - term: PEPB
    definition: Pro-Environmental Theory of Planned Behavior, adding environmental and authority support to TPB.
  - term: UTAUT2
    definition: Unified Theory of Acceptance and Use of Technology 2, explaining technology acceptance.
  - term: PENC
    definition: Perceived Environmental Concern, an individual's worry about environmental issues.
  - term: RFC
    definition: Random Forest Classifier, an ensemble learning method for classification.
  - term: DLNN
    definition: Deep Learning Neural Network, a neural network with multiple hidden layers.
critical_citations:
  - "[Ong et al., 2023] — Basis for adopted survey instrument and STPB framework."
  - "[Venkatesh et al., 2012] — Foundational work for UTAUT2 model used."
  - "[German et al., 2022] — Source of PEPB model and integration approach."
  - "[Fan et al., 2016] — Justifies using MLA over SEM for large nonlinear models."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: The study focuses on Filipino drivers, with a majority being young professionals aged 23-36 and employed.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Analyzes factors influencing purchasing decisions, including economic concerns and price value.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: Provides background on hybrid car adoption in the Philippine context, referencing local market conditions.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Demonstrates the application of predictive MLAs to model behavioral intentions, a core module for Odin.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Uses RFC and DLNN for classification and prediction, relevant to forecasting user behavior.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Findings on PBC and PE (performance expectancy) can inform how users interact with budgeting strategies.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: The classification approach could be analogous to detecting anomalous spending patterns.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Uses Taylor diagrams and accuracy metrics (94%, 96.60%) for system evaluation, relevant to Odin.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Compares SEM vs. MLA performance, providing evidence for using MLA in Odin's modules.
  contribution: This paper validates the use of MLAs like Random Forest Classifier and Deep Learning Neural Network for predicting consumer behavior, which can be directly applied to Odin's behavioral profiling and forecasting modules. It provides a methodology for evaluating and comparing algorithmic modules (SEM vs. MLA) and identifies key latent factors (PENC, AT, PBC, PE) that are likely analogous to user engagement drivers. The framework developed (STPB) offers a structured approach to modeling complex behavioral and sustainability factors relevant to Odin's user financial contexts. The study's findings on factor importance ranking provide a potential template for prioritizing features in Odin's recommendation and anomaly detection systems.
  directly_justifies:
    - "Machine learning algorithms are superior to SEM for analyzing large, nonlinear behavioral models."
    - "Perceived environmental concern is the most significant predictor of behavioral intention in the Filipino context."
    - "Both Random Forest and Deep Learning can achieve high accuracy (>94%) in classification tasks."
    - "The integration of UTAUT2 and PEPB provides a comprehensive framework for evaluating technology acceptance."
  limits:
    - "The study uses convenience and snowball sampling, which may introduce bias and limit generalizability."
    - "The research only focuses on Filipino drivers, so its findings may not be directly transferable to other cultures."
    - "The model's accuracy was validated for a specific prediction task, but its robustness for other financial behaviors is unknown."
    - "Reliance on self-administered surveys may introduce common method bias."
  mapping_rationale: The systematic scan across all 12 functional domains identified the paper as highly relevant to Predictive Modeling (6.A, 6.B) and System Evaluation (12.A, 12.B) due to its core focus on applying and validating MLAs for behavior prediction. The study's Filipino context and demographic focus mapped directly to 1.A (Filipino Young Professionals) and tangentially to 1.C (Financial Behavior) and 2.A (Cultural Practices). The paper was also considered for Behavioral Profiling (5.A-C) and Forecasting (6.A-B) but was classified under predictive modeling and evaluation as it primarily demonstrates the application and comparison of algorithms rather than defining a new profiling taxonomy or forecasting method. The relevance was considered 'high' for topics related to algorithm application and evaluation (6.A, 6.B, 12.A, 12.B) and 'medium' or 'contextual' for topics like budgeting (7.A) or anomaly detection (8.A) due to the indirect applicability of its findings. Overall, the paper's primary value to Odin lies in its methodological demonstration of MLA efficacy and its identification of key behavioral drivers, providing a strong justification for using similar approaches in Odin's algorithm modules.
limitations:
  - "The survey instrument had limited constructs, which may constrain the depth of behavioral insight."
  - "The sample was skewed towards millennials and those active on social media, limiting generational diversity."
  - "The study only used two MLAs (RFC and DLNN); other algorithms like Naïve Bayes or K-Means could provide additional insights."
  - "The absence of qualitative interviews restricts a complete understanding of the motivations behind purchasing intentions."
remember_this:
  - "Deep Learning Neural Network achieved 96.60% accuracy in predicting purchasing intentions."
  - "PENC and Attitude were the two strongest predictors of hybrid car adoption."
  - "Machine learning outperformed SEM for the complex, nonlinear STPB framework."
  - "Young Filipino professionals are environmentally conscious and influence the green market."
  - "The STPB framework integrates environmental, behavioral, and technological factors."
```
