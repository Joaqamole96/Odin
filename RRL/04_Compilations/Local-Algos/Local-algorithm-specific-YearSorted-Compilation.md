# Compiled Research Summaries

## Filters Applied

- Designation: `local-algorithm-specific`

**Total Papers:** 21

**Note:** Sorted by year.

---

## Paper 1: Delena et al_summarized.md

**Source File:** `Delena et al_summarized.md`

```yaml
paper_id: 10.1016/j.sasc.2025.200352
designation: local-algorithm-specific
title: Predicting student retention: A comparative study of machine learning approach utilizing sociodemographic and academic factors
authors: Delen˜a, R. D.; Dia, N. J.; Sacayan, R. R.; Sieras, J. C.; Khalid, S. A.; Macatotong, A. H. T.; Gulam, S. B.
year: 2025
venue: Systems and Soft Computing
odin_topics:
  - 4.A
  - 5.C
  - 6.A
  - 6.B
  - 12.A
  - 12.B
tldr: Comparative evaluation of ten machine learning models for predicting student dropout using sociodemographic and academic data, with XGBoost achieving the highest cross-validated accuracy.
problem_and_motivation: Student attrition in higher education, particularly in developing regions, remains a persistent challenge due to limited institutional intervention resources and high socioeconomic disparities. Existing approaches often rely on short-term datasets or limited algorithm selection, leaving a gap for context-specific, scalable early warning systems.
approach:
  - Secondary data from 482 student records spanning 2012-2022 was sourced from Mindanao State University.
  - Data was preprocessed using Power BI and modeled in Jupyter Notebook following the CRISP-DM methodology.
  - Ten supervised machine learning algorithms were evaluated, including XGBoost, Gradient Boosting, ANN, and Decision Tree.
  - Models were assessed using a 70/30 train-test split and 5-fold cross-validation.
  - Six evaluation metrics were applied: Accuracy, Precision, Recall, F1 Score, MSE, and Log Loss.
findings:
  - XGBoost outperformed all models with the highest cross-validated accuracy of 90.66% and F1 Score of 90.72.
  - XGBoost also achieved low error values with MSE of 9.34 and Log Loss of 0.26.
  - Gradient Boosting and ANN followed closely, demonstrating strong balance between precision and recall.
  - Naïve Bayes showed high recall but excessive false positives, limiting practical use.
  - Ensemble methods like XGBoost and Gradient Boosting proved more stable and generalizable than individual classifiers like Decision Tree.
key_figures_tables:
  - Figure 2a: Sociodemographic factors used in retention studies → Gender and marital status are the most frequently used predictors.
  - Figure 2b: Academic factors used in retention studies → Expected graduation year and GPA are the most common academic predictors.
  - Figure 6: Confusion matrices for each model → XGBoost had the lowest total misclassification (9 errors out of 145 test instances).
  - Figure 7: Model performance with 5-fold cross-validation → XGBoost maintained the highest accuracy and lowest error across all metrics.
  - Table 6: Confusion matrix components → XGBoost achieved the highest dropout detection rate (94.5%).
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "XGBoost"
    definition: "Extreme Gradient Boosting, an optimized implementation of gradient boosting with built-in regularization and early stopping."
  - term: "CRISP-DM"
    definition: "Cross-Industry Standard Process for Data Mining, a six-phase methodology for data mining projects."
  - term: "EDM"
    definition: "Educational Data Mining, the application of machine learning to educational data to predict student outcomes."
  - term: "ITE"
    definition: "Information Technology Education, the academic program from which student data was drawn."
critical_citations:
  - "[Alhazmi & Sheneamer, 2023] — Benchmark for XGBoost in large-scale student performance prediction."
  - "[Niyogisubizo et al., 2022] — Reference for two-layer ensemble ML approach in dropout prediction."
  - "[Rodríguez-Hernández et al., 2021] — Reference for ANN implementation in academic prediction."
  - "[Ghorbani & Ghousi, 2020] — Reference for comparing resampling methods in student performance prediction."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides a comparative benchmarking methodology applicable to financial systems.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: contextual
      justification: Demonstrates classification model evaluation, transferable to financial profile classification.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: contextual
      justification: Establishes a predictive modeling framework for risk identification, analogous to spending forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: contextual
      justification: Evaluates sequential and non-sequential ML algorithms, relevant to forecasting module design.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: contextual
      justification: Provides a structured evaluation framework with multiple metrics and cross-validation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: contextual
      justification: Offers a comparative evaluation methodology for selecting optimal algorithms.
  contribution: "The paper offers a reproducible comparative methodology for evaluating machine learning models on structured demographic and performance data. Its approach to cross-validation and multi-metric evaluation is directly transferable to Odin's algorithmic modules for forecasting, anomaly detection, and user profiling. The study also emphasizes interpretability and institutional deployment, aligning with Odin's goal of practical, action-oriented system design."
  directly_justifies:
    - "XGBoost demonstrates superior performance on structured tabular data with both categorical and numeric features."
    - "Cross-validation is essential to correct overestimation from single train-test splits in ML evaluations."
    - "Ensemble methods like Gradient Boosting provide better generalization than individual classifiers like Decision Tree."
  limits:
    - "Single-institution dataset limits external generalizability."
    - "No behavioral or engagement features were included, which are known significant predictors."
    - "Model interpretability remains a challenge for high-stakes deployment."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes identified the following relevant domains: Existing Systems & Gaps, Behavioral Profiling & Classification, Spending Forecasting, and System Evaluation. From these, topic codes 4.A, 5.C, 6.A, 6.B, 12.A, and 12.B were selected as contextual, as the paper provides methodological framing rather than direct financial insights. Domains such as Filipino Cultural Context, Expense Categorization, Budget Recommendation, and Data Privacy were rejected as the paper does not address financial behaviors, budget allocation, or privacy. Overall, the paper is relevant to Odin primarily for its rigorous model evaluation methodology and comparative analysis of ML algorithms, which can inform the selection and validation of predictive modules."
limitations:
  - "Data sourced from a single institution, limiting external validity."
  - "Behavioral and psychosocial dimensions (e.g., LMS engagement, motivation) were not included."
  - "Model interpretability remains a challenge for sensitive domains like education. [unacknowledged]"
  - "Only a 5-fold cross-validation was used; more advanced strategies like stratified nested CV could strengthen generalization. [unacknowledged]"
remember_this:
  - "XGBoost achieved the highest cross-validated accuracy at 90.66%."
  - "Cross-validation corrects overestimation from single train-test splits."
  - "Ensemble methods provide better generalization than individual classifiers."
  - "Model evaluation requires multiple metrics: accuracy, F1, precision, recall, and error."
  - "Context-specific institutional data is vital for effective predictive modeling."
```
---

## Paper 2: de Goma et al_summarized.md

**Source File:** `de Goma et al_summarized.md`

```yaml
paper_id: "10.1145/3779657.3779698"
designation: "local-algorithm-specific"
title: "Using Item Personality-Based Profiling in Music Recommender Systems"
authors: "de Goma, J.; Anonuevo, J. N.; Pangan, G. N.; Deang, J. J.; Villaluz, A."
year: 2025
venue: "The 7th World Symposium on Software Engineering (WSSE2025)"
odin_topics:
  - "5.A"
  - "5.B"
  - "5.C"
  - "6.A"
  - "6.B"
  - "12.A"
  - "12.B"
tldr: "Incorporating Big Five personality profiles into a hybrid LightFM model improves music recommendation accuracy and mitigates cold-start issues compared to pure collaborative filtering."
problem_and_motivation: "Traditional recommendation algorithms struggle with user variability and the cold-start problem, leading to inaccurate music suggestions. Integrating personality profiles can address these issues by providing a richer user model, but existing work has shown biases and limited exploration in music domains."
approach:
  - "Data was collected via a survey from 208 Mapua University students, gathering Big Five personality scores, genre preferences, and song ratings (likes/dislikes) for a 100-song list."
  - "The Million Song Dataset was also used, with playcounts normalized via min-max scaling to create weighted interactions for model training."
  - "A hybrid recommender was developed using the LightFM library, integrating user features (personality T-scores, genre) and item features (sonic attributes, Item Personality Profiles)."
  - "The hybrid model was evaluated against a pure collaborative filtering (CF) baseline using offline metrics (AUC, Precision@10, Recall@10, F1) and an online user study with 20 new users."
  - "Two loss functions, BPR and WARP, were tested for the hybrid model, with WARP selected for final evaluation due to its superior performance on ranking tasks."
findings:
  - "num: The hybrid WARP model achieved a Precision of 0.46, Recall of 0.64, and AUC of 0.57 on the validation set, outperforming the BPR variant."
  - "num: The pure collaborative filtering model showed signs of severe overfitting, with a drop in Recall from 0.86 (train) to 0.74 (validation)."
  - "The hybrid models demonstrated better generalizability, with no large discrepancy between training and validation metrics, indicating they can adapt to unseen data."
  - "num: In online evaluation, the hybrid model (Model A) scored higher on Recommendation Quality (mean 3.7 vs 3.4) and User Satisfaction (4.15 vs 3.55) than the pure CF model."
  - "The hybrid model achieved a better balance between relevance and diversity by leveraging personality features alongside genre and sonic features."
  - "num: Model A had an average precision 0.13 higher than Model B, indicating greater accuracy in ranking items based on user preferences."
key_figures_tables:
  - "Table 1: Model metrics on training set → Hybrid WARP shows competitive precision and recall with pure CF."
  - "Table 2: Model metrics on validation set → Hybrid WARP outperforms BPR variant and is more generalizable."
  - "Table 3: User feedback means → Hybrid model rated higher for recommendation quality and user satisfaction."
  - "Table 5: Precision/Recall/F1 comparison → Hybrid model (0.57, 0.62, 0.58) outperforms pure CF (0.41, 0.46, 0.40)."
key_equations:
  - equation: "Proportion = (totalNumber of Users who liked the Item and has the same BF degree) / (totalNumber of Users who Liked the Item)"
    explanation: "Computes Item Personality Profile feature values."
definitions:
  - term: "LightFM"
    definition: "A hybrid recommendation library combining collaborative and content-based filtering."
  - term: "Item Personality Profile (IPP)"
    definition: "A vector representing the personality traits of users who like an item."
  - term: "BPR"
    definition: "Bayesian Personalized Ranking, a pairwise loss function for optimizing AUC."
  - term: "WARP"
    definition: "Weighted Approximate-Rank Pairwise loss, optimizing for top-k recommendation lists."
  - term: "Cold-start problem"
    definition: "The difficulty of recommending items to new users with no interaction history."
critical_citations:
  - "[Kleć et al., 2023] — personality facets influence recommendation error."
  - "[Lu & Tintarev, 2018] — personality integration improves diversity and satisfaction."
  - "[Alharthi, 2015] — foundational work on Item Personality Profiles."
  - "[Liu & Hu, 2020] — personality predicts music taste, informing model design."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Demonstrates use of personality profiles (Big Five) for user classification."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "high"
      justification: "Directly addresses the cold-start problem using personality profiles."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "Uses T-scores and degrees to classify personality profiles."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Applies predictive modeling (recommendations) based on user features."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "low"
      justification: "Study focuses on non-sequential recommendation, not forecasting."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Uses offline and online evaluation with standard metrics (Precision, Recall, F1)."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Compares a hybrid model to a pure collaborative filtering baseline."
  contribution: "This paper demonstrates a methodology for addressing the cold-start problem by integrating personality profiles, which is directly applicable to Odin's profile dynamics module. The offline and online evaluation framework provides a template for assessing recommender system performance. The hybrid modeling approach, combining collaborative and content-based features, can inform Odin's expense forecasting and budget recommendation algorithms. The comparison of loss functions (BPR vs. WARP) offers a valuable insight for optimizing top-k recommendations."
  directly_justifies:
    - "The hybrid LightFM model outperforms pure collaborative filtering, especially in cold-start scenarios."
    - "Using WARP loss is more effective than BPR for optimizing top-k recommendations in sparse data."
    - "A two-stage evaluation (offline metrics and online user study) provides a robust assessment of system performance."
  limits:
    - "Limited song dataset (100 songs) from survey may restrict model variation and generalization."
    - "Dataset skewness and sparsity, especially with less than 20% of users having complete personality data, impacts performance."
    - "The study focuses on music, not personal finance, requiring translation of findings to Odin's financial domain. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains revealed the paper's primary relevance lies in Behavioral Profiling & Classification (5.A, 5.B, 5.C) and System Evaluation (12.A, 12.B). The paper's core contribution—using personality profiles to mitigate the cold-start problem—directly addresses topic 5.B. Its predictive modeling approach and use of implicit feedback align with topics under Spending Forecasting (6.A, 6.B), though the forecasting aspect is tangential. The evaluation framework using offline metrics and user studies is highly relevant to System Evaluation (12.A, 12.B). Domains like Expense Categorization (3.A-C), Budget Recommendation (7.A-D), and Anomaly Detection (8.A-C) were considered but rejected as the paper does not address financial data or budgeting constraints. The paper offers methodological insights for Odin's profile and evaluation modules, but its application to finance requires domain adaptation."
limitations:
  - "Small dataset size (208 students, 100 songs) limits generalizability."
  - "Dataset skewness and sparsity, especially with less than 20% of users having complete personality data."
  - "Focus on music recommendation requires significant adaptation for financial behavior prediction. [unacknowledged]"
  - "Limited exploration of alternative recommender frameworks (e.g., scikit-learn) that could yield better performance. [unacknowledged]"
remember_this:
  - "Hybrid models using personality profiles outperform pure collaborative filtering in recommendations."
  - "The WARP loss function is better for optimizing top-k recommendations than BPR."
  - "Offline metrics and online user studies together provide a robust system evaluation."
  - "Integrating user features addresses the cold-start problem effectively."
  - "The hybrid model achieved a 0.13 higher precision than the pure collaborative filter."
```
---

## Paper 3: Hassine et al_summarized.md

**Source File:** `Hassine et al_summarized.md`

```yaml
paper_id: 10.62345/jads.2025.14.3.1
designation: local-algorithm-specific
title: Inequality, Education and Occupational Change in the Philippines
authors: Belhaj Hassine, N.; Fernandez, F. C.; Lavin, B. A.
year: 2025
venue: Journal of Asian Development Studies
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 12.A
tldr: Slow growth in college-educated labor supply sustains high wage premiums, while shifts in occupational structure, particularly growth in middle-skill jobs from 2012-2016, have recently narrowed wage inequality.
problem_and_motivation: The Philippines has persistently high income inequality despite poverty reduction and economic growth. The relationship between education, employment structure, and wage inequality remains underexplored. This study analyzes how changes in skill supply and occupational composition have shaped wage distribution over two decades.
approach:
  - Data from Philippine Labor Force Survey (2002-2024), covering wage workers aged 15+.
  - Constructed an occupation crosswalk harmonizing PSOC 1992 and 2012 to create 22 consistent occupation codes.
  - Classified occupations into high-, middle-skill routine, middle-skill nonroutine, and low-skill categories.
  - Used Recentered Influence Function (RIF) regressions to estimate returns to education and occupation across wage quantiles.
  - Applied DiNardo-Fortin-Lemieux (DFL) reweighting to isolate the impact of occupational changes on wage distributions.
findings:
  - num: College wage premium declined from 88% in 2013 to 59% in 2024, but college graduates still earned 80% more than high school graduates.
  - num: Returns to college education and high-skill occupations rise monotonically across wage quantiles, with college coefficients increasing over time.
  - num: Real wages for non-college workers grew 32% from 2012-2024 versus 5% for college workers, narrowing inequality.
  - num: Middle-skill employment share grew by 3.6 percentage points from 2002-2016 but declined by 2.8 points from 2016-2024.
  - Occupational reallocation explains a significant share of non-college wage growth after 2012, particularly for men.
  - num: Youth college graduates (25-34) had 6.7% unemployment in 2024, higher than the 4.4% for non-college peers.
key_figures_tables:
  - "Figure 1: Income and wage Gini trends 2002-2024 → Inequality declined from 2012 onward, with wage Gini falling to 32% by 2024."
  - "Figure 5: College wage premium trend → Premium peaked at 88% in 2013, declined to 59% by 2024."
  - "Figure 8: Returns to education by quantile → College returns increase monotonically across income distribution, widening gaps."
  - "Table 1A: RIF regression on wage Gini → College education has positive and increasing effect on wage inequality over time."
key_equations:
  - equation: "f_{x_{t0}}(w) = ∫ f(w | x, t_w=t0) dF(x | t_x=t0)"
    explanation: "Observed wage density as joint distribution of wages and covariates."
  - equation: "f_{x_{t1}}(w) = ∫ f(w | x, t_w=t0) * ψ_x(x) dF(x | t_x=t0)"
    explanation: "Counterfactual wage density reweighting covariates from t0 to t1."
  - equation: "ψ̂_x = [Pr(t_x=t1 | x)/Pr(t_x=t0 | x)] * [Pr(t_x=t0)/Pr(t_x=t1)]"
    explanation: "Reweighting function estimated via logit model for DFL decomposition."
definitions:
  - term: RIF Regression
    definition: "Recentered Influence Function regression for unconditional quantile effects on wage distribution."
  - term: DFL Reweighting
    definition: "DiNardo-Fortin-Lemieux semiparametric method to decompose wage distribution changes."
  - term: PSOC
    definition: "Philippine Standard Occupational Classification, versions 1992 (ISCO-88) and 2012 (ISCO-08)."
  - term: LFS
    definition: "Labor Force Survey, quarterly nationwide household survey by Philippine Statistics Authority."
  - term: Wage Premium
    definition: "Percentage wage gap between college graduates and high school graduates, reflecting skill valuation."
critical_citations:
  - "[Acemoglu and Autor, 2011] — Framework for skill-task-occupation classification."
  - "[Firpo et al., 2018] — Methodological basis for RIF regression approach."
  - "[DiNardo et al., 1996] — Foundation for DFL decomposition technique."
  - "[Autor, 2019] — Framework for analyzing job polarization and wage inequality."
  - "[World Bank, 2022] — Comprehensive prior analysis of Philippine inequality drivers."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: Provides wage and employment data for prime-age workers (25-54), including youth unemployment trends.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Documents wage distribution and returns to education, directly relevant to income structure.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Highlights unemployment and labor market outcomes shaping financial behavior.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: Context on labor market structure and wage inequality in Philippine context.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: low
      justification: Mentions COVID-19 cyclical disruption but not seasonal spending patterns.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Discusses cyclical labor market shifts, not spending cycles.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides macroeconomic context for personal finance system design.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: low
      justification: Identifies skills mismatch and occupational polarization as systemic gaps.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Documents wage premium persistence and occupational shifts that differentiate worker profiles.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Uses occupational and education classifications that inform behavioral profile segmentation.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides RIF regression and DFL decomposition methodologies applicable to system evaluation.
  contribution: "This paper provides empirical methods (RIF regression, DFL decomposition) applicable to evaluating Odin's algorithmic modules. Its analysis of education and occupational returns offers a framework for segmenting user financial profiles based on income trajectories. The findings on wage premium persistence inform Odin's expense categorization and forecasting modules. The documentation of occupational shifts and skill supply constraints justifies behavioral profiling approaches. The paper's methodological rigor supports system evaluation frameworks for algorithmic modules."
  directly_justifies:
    - "RIF regression methods can evaluate inequality impacts of algorithmic modules."
    - "Occupational classification informs behavioral profile segmentation for PFMS."
    - "Wage premium trends provide baseline for income-based user segmentation."
    - "DFL decomposition methods apply to counterfactual evaluation of financial advice."
  limits:
    - "Focus on wage workers excludes self-employed and informal sector, limiting generalizability to all Filipino workers."
    - "Paper does not address individual-level financial behavior or spending patterns."
    - "Analysis aggregates to 22 occupation codes, which may oversimplify occupational diversity."
    - "DFL decomposition holds wages within occupations fixed, abstracting from within-occupation wage dynamics."
  mapping_rationale: "Systematic scan across all 12 functional domains and 38 topic codes flagged the following as relevant: Filipino Cultural Context (2.A contextual, 2.B low, 2.D low) for the Philippine-specific labor market analysis; Existing Systems & Gaps (4.A contextual, 4.B low) for identifying skills mismatch; Behavioral Profiling (5.A high, 5.C high) as the paper directly uses occupational and education classifications to differentiate worker types; and System Evaluation (12.A high) for its RIF regression and DFL decomposition methodologies. Domains on expense categorization (3.A-3.C), spending forecasting (6.A-6.B), budget recommendation (7.A-7.D), anomaly detection (8.A-8.C), mobile design (9.A-9.B), data privacy (10.A-10.B), user retention (11.A-11.B), savings and debt (13.A-13.C) were considered but rejected as the paper does not address these PFMS-specific functions. The paper is highly relevant methodologically for evaluating algorithmic modules and informing user segmentation, but does not directly address personal finance system design. Its empirical framework for analyzing inequality and occupational shifts provides foundation for behavioral profiling and evaluation modules."
limitations:
  - "Wage data only available from 2002 onward, limiting historical context."
  - "Analysis excludes non-wage workers (self-employed, family workers), missing significant portion of workforce."
  - "LFS occupational classifications changed in 2016, requiring crosswalk that may introduce harmonization errors."
  - "Does not explicitly examine within-occupation wage heterogeneity beyond education grouping."
  - "COVID-19 pandemic effects may confound recent structural trend identification. [unacknowledged]"
remember_this:
  - "College wage premium declined to 59% by 2024 from 88% in 2013."
  - "Non-college wages grew 32% from 2012-2024, outpacing college-educated workers."
  - "Middle-skill employment expanded from 2002-2016 but declined after 2016."
  - "Occupational reallocation explains non-college wage growth after 2012."
  - "Young college graduates face 6.7% unemployment, higher than less-educated peers."
```
---

## Paper 4: Pandiin & Matias_summarized.md

**Source File:** `Pandiin & Matias_summarized.md`

```yaml
paper_id: "4a3f2b1c-5d6e-7f8a-9b0c-1d2e3f4a5b6c"
designation: "local-algorithm-specific"
title: "Predictive Modeling for Loan Eligibility Assessment: A Comparative Study of Logistic Regression, Random Forest, and Support Vector Machine with Detailed Oversampling"
authors: "Pandiin, J. D.; Matias, J. B."
year: 2025
venue: "AEIS"
odin_topics:
  - "6.A"
  - "12.B"
tldr: "Compares Logistic Regression, Random Forest, and SVM for loan approval prediction using oversampling and GA feature selection, with Random Forest achieving the highest balanced accuracy."
problem_and_motivation: "Manual loan approval processes are inefficient and error‑prone; existing ML approaches lack robust feature selection and fail to handle class imbalance, limiting predictive performance and fairness. This study addresses these gaps by comparing classifiers with advanced feature selection and oversampling."
approach:
  - "Data sourced from Kaggle loan dataset; categorical encoding and missing value imputation applied."
  - "Oversampling via resampling of minority class to balance the target variable."
  - "Feature selection methods: Correlation‑Based, RFE, SelectKBest, Lasso, and Genetic Algorithm (GA) optimized for each classifier."
  - "Classifiers: Logistic Regression, Random Forest, and Support Vector Machine (SVM) with hyperparameters tuned via GA."
  - "Model evaluation using accuracy, precision, recall, F1, AUC, and 5‑fold cross‑validation."
  - "Deployment via a user‑friendly web application for operational use."
findings:
  - "num: Random Forest achieved accuracy 85%, precision 86%, recall 84%, and F1 85%."
  - "num: 5‑fold cross‑validation mean accuracy for Random Forest was 92%, demonstrating robustness."
  - "num: SVM attained recall 99% but lower precision 63% and accuracy 71%."
  - "num: Logistic Regression showed accuracy 67%, with high recall (90%) but low precision (62%)."
  - "Feature importance: Credit_History (26.8%), ApplicantIncome (19.7%), LoanAmount (19.2%) as top predictors; demographic features had minimal impact."
  - "Random Forest provided the best balance between false positives and false negatives, making it suitable for risk management."
key_figures_tables:
  - "Figure 2: Distribution of loan status before and after oversampling → imbalance corrected."
  - "Table 1: Accuracy of classifiers with four feature selection methods → Random Forest + Lasso best (88.5%)."
  - "Table 2: Variable importance percentages → Credit_History dominates."
  - "Table 3: Comparative performance matrix → Random Forest has highest AUC (0.94)."
  - "Figure 8: 5‑fold cross‑validation scores → Random Forest consistently above 0.90."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "GA"
    definition: "Genetic Algorithm, an optimization technique inspired by natural selection."
  - term: "RFE"
    definition: "Recursive Feature Elimination, an iterative feature selection method."
  - term: "SVM"
    definition: "Support Vector Machine, a supervised learning algorithm for classification."
  - term: "Oversampling"
    definition: "Resampling the minority class to balance the dataset."
critical_citations:
  - "[Ruud & Nilsen, 2021] — comparative study on loan eligibility prediction."
  - "[Chawla et al., 2002] — SMOTE oversampling technique."
  - "[Mehrabi et al., 2021] — bias and fairness in ML."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Compares classifiers for predictive modeling of financial outcomes, informing Odin's forecasting module design."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Provides a comparative evaluation methodology with metrics and cross‑validation for algorithmic modules, applicable to Odin's evaluation."
  contribution: "The comparative evaluation of classifiers informs Odin's predictive modeling module selection. The use of Genetic Algorithms for feature selection can optimize forecasting inputs. The cross‑validation and metrics framework provides a template for evaluating algorithmic performance in Odin. The emphasis on handling class imbalance is relevant to financial data. The feature importance analysis guides feature engineering for spending prediction."
  directly_justifies:
    - "Random Forest outperforms other classifiers on imbalanced financial data."
    - "Feature selection via GA improves predictive accuracy."
    - "Credit history and income are dominant predictors in financial decisions."
    - "Oversampling is critical for fair classification in unbalanced datasets."
  limits:
    - "Dataset is from Kaggle and not Filipino‑specific, limiting direct applicability to Odin's target population. [unacknowledged]"
    - "Study focuses on loan approval, not spending or budgeting, so direct transferability is limited. [unacknowledged]"
    - "No real‑world deployment evaluation beyond a web prototype."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. Only topics related to predictive modeling and system evaluation were flagged as relevant: 6.A (Predictive Modeling) is assigned medium because the paper compares classifiers that could inform Odin's forecasting module; 12.B (Evaluation of Algorithmic Modules) is medium because the study provides a rigorous comparison methodology with metrics and cross‑validation. Domains such as cultural context, expense categorization, behavioral profiling, budgeting, anomaly detection, mobile design, privacy, retention, and savings/debt were considered and rejected because the paper does not address them. The paper's focus on loan eligibility rather than personal financial management makes it contextual for most Odin modules, but the algorithmic comparison and evaluation techniques offer actionable insights for predictive and evaluative components."
limitations:
  - "The dataset is not from the Philippines, so findings may not generalize to Filipino young professionals. [unacknowledged]"
  - "Only three classifiers and a limited set of feature selection methods were tested."
  - "Oversampling via simple resampling may introduce overfitting; other techniques like SMOTE were not explored."
remember_this:
  - "Random Forest achieved 85% accuracy and 92% cross‑validation mean, outperforming SVM and Logistic Regression."
  - "Credit History, Applicant Income, and Loan Amount are the most influential predictors."
  - "SVM achieved 99% recall but low precision, making it unsuitable for strict risk management."
  - "Genetic Algorithm optimized feature selection significantly improved Random Forest performance."
  - "Balancing the dataset via oversampling is essential for fair loan approval predictions."
```
---

## Paper 5: Alunen et al_summarized.md

**Source File:** `Alunen et al_summarized.md`

```yaml
paper_id: 10.46254/FA6.20250062
designation: local-algorithm-specific
title: Comparing Machine Learning Forecasting Models Based on Accuracy and Efficiency for Predicting Demand in a Food and Beverage Company
authors: Alunen, R. B.; Molina, C. F.; Quesada, R. F.; Reyes, C. N.; Jacob, D.
year: 2025
venue: Proceedings of the 6th African International Conference on Industrial Engineering and Operations Management
odin_topics:
  - 2.B
  - 2.D
  - 4.B
  - 6.A
  - 6.B
  - 12.A
  - 12.B
  - 12.C
tldr: Machine learning models, especially XGBoost, outperform traditional methods in demand forecasting for alcoholic beverages in the Philippines by capturing non-linear relationships and external factors.
problem_and_motivation: The Philippine food and beverage industry lacks sophisticated forecasting tools, leading to inefficiencies like overstocking and waste. Traditional methods fail to capture the influence of external factors such as holidays and weather on demand, particularly for alcoholic beverages where consumption patterns are complex.
approach:
  - Historical sales data from a Quezon City restobar (2021-2024) was merged with external data on unemployment, temperature, holidays, and day of week.
  - Four algorithms were evaluated: Random Forest, Gradient Boosting, XGBoost, and AdaBoost, using 80/20 train-test split with 10-fold cross-validation.
  - Feature selection via Pearson correlation and hyperparameter tuning via Grid Search and Random Search were applied to optimize model performance.
  - Accuracy was measured using MAE, MSE, RMSE, and R², while computational efficiency was measured by execution time.
  - The best-performing framework was identified by balancing accuracy and speed across multiple products.
findings:
  - XGBoost provided the best balance between high forecasting accuracy and computational efficiency.
  - Feature selection using correlation analysis improved computational efficiency but led to a slight reduction in forecast accuracy.
  - Random Search for hyperparameter tuning outperformed Grid Search in both accuracy and execution time.
  - num: Machine learning models reduced prediction errors by 22-33% in RMSE compared to heuristic forecasts.
  - num: R² values for ML models were around 0.42, significantly higher than exponential smoothing's 0.07, indicating better explanatory power.
  - While XGBoost and Random Forest showed highest accuracy, AdaBoost was fastest in execution for certain products.
key_figures_tables:
  - Table 2: Comparison of feature selection impact → Feature selection slightly reduces MAE but increases execution time.
  - Table 3: Comparison of hyperparameter tuning → Random Search is faster and often more accurate than Grid Search.
  - Figure 3: Visual comparison of ML algorithms → XGBoost and AdaBoost are computationally efficient while maintaining low errors.
  - Figure 5: Feature selection impact graph → Feature selection lowers MAE and MSE but not R².
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: XGBoost
    definition: Extreme Gradient Boosting, a scalable tree boosting algorithm.
  - term: MAE
    definition: Mean Absolute Error, the average magnitude of prediction errors.
  - term: MSE
    definition: Mean Squared Error, penalizes larger errors by squaring them.
  - term: RMSE
    definition: Root Mean Squared Error, sensitive to outliers.
  - term: R²
    definition: Coefficient of Determination, explains the proportion of variance captured by the model.
critical_citations:
  - "[Groene and Zakharov, 2024] — ML models reduce forecast error vs heuristics by 22-33%."
  - "[Liashchynskyi and Liashchynskyi, 2021] — Random search is more practical than grid search."
  - "[Venkatesh and Anuradha, 2019] — Pearson correlation is a common feature selection method."
relevance:
  topics:
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: The paper explicitly models holidays, day-of-week, and weather as predictors of alcoholic beverage demand.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: medium
      justification: Uses Philippine holiday data and local restobar sales to capture culturally specific spending cycles.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly identifies traditional forecasting heuristics and their failure to capture non-linear external factors.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Benchmarks ML algorithms (XGBoost, RF) for demand prediction, directly relevant to spending forecasting in PFMS.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Compares XGBoost, Random Forest, AdaBoost, and Gradient Boosting on time-series sales data.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses MAE, MSE, RMSE, R², and execution time, a comprehensive framework applicable to Odin's forecasting modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Provides a structured comparison of algorithmic performance (feature selection, tuning) for forecasting tasks.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: contextual
      justification: While not directly about budget recommendations, the evaluation approach is methodologically analogous.
  contribution: This paper provides a methodology for evaluating forecasting algorithms that can be adapted for Odin's spending prediction module. The comparison of XGBoost against other tree-based methods, along with the analysis of feature selection and hyperparameter tuning, offers actionable insights for designing Odin's forecasting engine. The paper's emphasis on balancing accuracy and computational efficiency is directly applicable to Odin's mobile-first, real-time constraints. The findings that XGBoost provides the best trade-off can justify its selection for Odin's core prediction functions.
  directly_justifies:
    - "XGBoost balances high forecasting accuracy and computational efficiency, making it suitable for real-time PFMS applications."
    - "Random Search for hyperparameter tuning provides better accuracy and speed than Grid Search for tree-based models."
    - "Feature selection using correlation improves efficiency at a small cost to accuracy, useful for resource-constrained mobile systems."
    - "External factors like holidays and weather significantly improve demand forecasting accuracy over pure historical sales data."
  limits:
    - "Single product category (alcoholic beverages) limits generalizability to other spending categories."
    - "Dataset is from a single restobar in Quezon City, not representative of national Filipino spending patterns."
    - "Does not address concept drift or model retraining, critical for adaptive PFMS systems."
    - "Privacy and ethical considerations of using macroeconomic data for personal forecasting are not discussed. [unacknowledged]"
  mapping_rationale: The systematic scan across all 12 functional domains identified strong relevance to Forecasting Algorithms (6.A, 6.B) and System Evaluation (12.A, 12.B, 12.C) due to the paper's core contribution of comparing ML models for demand forecasting. The paper's use of Philippine holiday and sales data links it to Seasonal Spending (2.B, 2.D) and its critique of traditional heuristics connects to Existing Systems Gaps (4.B). The paper was rejected for topics related to Behavioral Profiling (5), Budget Recommendation (7), Anomaly Detection (8), Mobile Design (9), Privacy (10), or Engagement (11) as it does not address these domains. The relevance of Filipino Demographic (1.A) is contextual, as the study uses Filipino data but does not analyze the demographic itself. Overall, the paper is highly relevant for Odin's forecasting module but has limited applicability to other functional areas.
limitations:
  - "Single product category (alcoholic beverages) limits generalizability to other spending types."
  - "Single source (one restobar) limits national applicability."
  - "Models were not evaluated for concept drift or retraining needs."
  - "Does not explore deep learning approaches like LSTM, which may be superior for sequential data. [unacknowledged]"
  - "The paper does not discuss the ethical or privacy implications of using external macroeconomic data. [unacknowledged]"
remember_this:
  - "XGBoost offers the best trade-off between prediction accuracy and execution time."
  - "Random Search is computationally superior to Grid Search for hyperparameter tuning."
  - "Feature selection with correlation improves speed but can slightly reduce accuracy."
  - "num: ML models reduce forecasting error by 22% to 33% compared to heuristic methods."
  - "External factors (holidays, weather, employment) are critical for accurate demand forecasting."
```
---

## Paper 6: Ram & Agoylo_summarized.md

**Source File:** `Ram & Agoylo_summarized.md`

```yaml
paper_id: 10.54554/jtec.2025.17.02.004
designation: local-algorithm-specific
title: Optimized Random Forest Classifier for Students Lifestyle Prediction Using Behavioral Data: A Machine Learning Approach
authors: Ram, M. L.; Agoylo, J. C. Jr.
year: 2025
venue: Journal of Telecommunication, Electronic and Computer Engineering
odin_topics:
  - 5.A
  - 5.C
  - 12.B
tldr: Random Forest classifier predicts lifestyle categories from behavioral data with 75.07% accuracy, highlighting the importance of parameter tuning and feature selection in behavioral analytics.
problem_and_motivation: Lifestyle classification using machine learning remains underexplored, with a gap in comprehensive approaches. The complexity and high dimensionality of behavioral data pose challenges for accurate categorization. This research addresses the gap by employing a Random Forest classifier to predict lifestyle categories from a large behavioral dataset.
approach:
  - The study utilized the Half a Million Lifestyle Dataset from Kaggle, containing 500,000 lifestyle entries.
  - Data preprocessing included deleting missing values and selecting relevant columns for lifestyle prediction.
  - Gender was converted to numerical values for effective model training.
  - A Random Forest classifier was implemented in Python, generating multiple decision trees and using majority voting for classification.
  - The model was evaluated on a test set and further validated using behavioral data from 93 students.
findings:
  - num: The model achieved an accuracy of 75.07%, precision of 75.16%, recall of 75.07%, and an F1 score of 74.40%.
  - Training accuracy reached 100% with 30 trees, indicating overfitting, while testing accuracy stabilized around 75%.
  - num: Among 93 students, the model classified 41 as Fitness Enthusiasts and 50 as Health-Conscious.
  - Model performance remained consistent when tested on real-world participant data.
  - The optimal number of trees for balancing performance and efficiency was found to be 30-40.
key_figures_tables:
  - Figure 1: Causal paradigm of behavioral patterns influencing lifestyle prediction → Framework for behavioral classification.
  - Figure 2: Diagram of the Random Forest classifier model architecture → Visual representation of the voting mechanism.
  - Figure 3: Model accuracy by number of trees → Shows overfitting and stabilization of testing accuracy at 75%.
  - Table 1: Model performance metrics (Accuracy, Precision, Recall, F1 Score) → Provides quantitative evaluation results.
  - Table 2: Prediction results from 93 students by lifestyle category → Demonstrates real-world classification distribution.
key_equations:
  - equation: "Accuracy = (TP+TN) / (TP+TN+FP+FN)"
    explanation: Accuracy is the ratio of correct predictions to total predictions.
  - equation: "Precision = TP / (TP+FP)"
    explanation: Precision measures the accuracy of positive predictions.
  - equation: "Recall = TP / (TP+FN)"
    explanation: Recall measures the ability to identify all positive instances.
  - equation: "F1 Score = 2 * (Precision * Recall) / (Precision + Recall)"
    explanation: F1 Score is the harmonic mean of precision and recall.
  - equation: "O(T * N * log N * F)"
    explanation: Time complexity of the Random Forest algorithm.
definitions:
  - term: Random Forest Classifier
    definition: An ensemble learning method that constructs multiple decision trees and outputs the majority class vote for classification.
  - term: Behavioral Analytics
    definition: The analysis of behavioral data to identify patterns and predict outcomes.
  - term: Overfitting
    definition: A modeling error where a model learns the training data too well, failing to generalize to new data.
  - term: Precision
    definition: The ratio of correctly predicted positive observations to the total predicted positives.
  - term: Recall
    definition: The ratio of correctly predicted positive observations to all actual positives.
critical_citations:
  - "[Jayaprakash et al., 2020] — Predicts academic performance using improved Random Forest."
  - "[Nachouki et al., 2023] — Course grade prediction with Random Forest."
  - "[Nachouki & Naaj, 2022] — Student performance prediction using Random Forest."
  - "[Rani & Gupta, 2024] — Predicts student anxiety and depression using Random Forest."
  - "[Ram et al., 2025] — Clustering student performance using machine learning."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: The study uses students, a demographic relevant to young professionals, but not specifically Filipino young professionals.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Demonstrates a machine learning framework for classifying behavioral patterns into distinct lifestyle profiles.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Directly employs a Random Forest classifier for behavioral classification, a key technique for financial profiling.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Provides a methodology for evaluating the performance of a classification algorithm on real-world data.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Mentions the potential for AI-driven categorization in wellness but not specifically personal finance systems.
  contribution: The paper provides a validated machine learning framework for behavioral classification that can be adapted for financial behavior profiling in Odin. The approach demonstrates how to process raw behavioral data into actionable lifestyle categories, which is directly relevant to Odin's goal of user classification. The emphasis on parameter tuning to mitigate overfitting is crucial for developing robust predictive models. The real-world validation with 93 students offers a template for testing Odin's algorithmic modules on local populations.
  directly_justifies:
    - The Random Forest classifier is effective for behavioral classification tasks, achieving 75.07% accuracy.
    - Parameter tuning is essential to balance model accuracy and generalization in classification algorithms.
    - Machine learning models can generalize from large datasets to make predictions on new, real-world inputs.
    - Behavioral features such as health consciousness and stress management are predictive of lifestyle categories.
  limits:
    - The study's lifestyle categories are predefined and may not fully capture the complexity of individual behaviors.
    - Behavioral data was self-reported, introducing potential bias.
    - The model was tested on a relatively small sample (93 students) for real-world validation.
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The paper's core contribution is algorithmic, placing it primarily within the Behavioral Profiling & Classification and System Evaluation domains. Topic 5.A was flagged as high relevance because the study provides a framework for classifying individuals into behavioral profiles. Topic 5.C received high relevance as it directly tests and validates a classification approach (Random Forest) applicable to financial behavioral profiling. Topic 12.B was marked medium as the evaluation metrics (accuracy, precision, recall, F1) provide a methodology for assessing algorithmic modules. Topic 1.A was considered contextual as the student demographic is somewhat related to young professionals, but the study does not focus on Filipino financial behaviors. Topic 4.A was considered low, as the research mentions general wellness applications but not PFMS or expense categorization. Domains like Expense Categorization, Spending Forecasting, Budget Recommendation, Anomaly Detection, Mobile-First Design, Data Privacy, User Retention, Savings & Debt Management, and Filipino-specific cultural practices (2.A, 2.B, etc.) were rejected as the paper does not address these areas. Overall, the paper is highly relevant for informing Odin's approach to behavioral classification and algorithm evaluation.
limitations:
  - The study relies on predefined lifestyle categories that may not encompass all behavioral variations.
  - The use of self-reported behavioral data introduces the potential for bias. [unacknowledged]
  - The sample of 93 students for real-world validation may not be representative of the broader population.
  - Generalizability is limited by the specific demographic (students) used for testing.
remember_this:
  - Random Forest achieved 75.07% accuracy in lifestyle classification.
  - Overfitting occurs with excessive decision trees, requiring careful tuning.
  - Behavioral patterns can be effectively generalized to classify new individuals.
  - Parameter optimization balances accuracy and computational efficiency.
  - Real-world validation confirms model predictive capability on new inputs.
```
---

## Paper 7: Carillo & Serra_summarized.md

**Source File:** `Carillo & Serra_summarized.md`

```yaml
paper_id: 10.29020/nybg.ejpam.v18i4.6875
designation: local-algorithm-specific
title: Optimized Nonlinear Grey Bernoulli Model for Nowcasting the Philippine Gross Domestic Product
authors: Carillo, S. K.; Serra, I. J.
year: 2025
venue: European Journal of Pure and Applied Mathematics
odin_topics:
  - 2.B
  - 6.A
  - 6.B
  - 7.D
  - 8.B
  - 12.B
tldr: PSO-optimized NGBM(1,1) achieved the lowest out-of-sample MAPE of 5.45% for Philippine GDP nowcasting, outperforming benchmark grey models.
problem_and_motivation: Quarterly GDP data are released with significant delays, disrupting planning for stakeholders. Existing grey models often struggle with parameter estimation in nonlinear systems, limiting forecast accuracy for the Philippines.
approach:
  - Data consists of quarterly Philippine GDP figures from 2021 Q1 to 2024 Q4, sourced from the Philippine Statistics Authority.
  - A harmonic regression simulation with a 70/30 training-testing split was used to determine the optimal data partitioning scheme.
  - The NGBM(1,1) model was optimized using Particle Swarm Optimization (PSO) to minimize out-of-sample MAPE.
  - An alternative optimization strategy using an exponential background value was also implemented for comparison.
  - Performance was evaluated against standard GM(1,1) and NGBM(1,1) benchmarks using out-of-sample MAPE and RMSE.
findings:
  - num: PSO-NGBM(1,1) achieved the lowest out-of-sample MAPE of 5.45% and RMSE of 362,077.8.
  - num: After seasonal adjustment, forecasting accuracy improved dramatically, with MAPE values falling below 1% for all models.
  - The PSO algorithm converged rapidly, stabilizing after approximately 30 iterations.
  - The exponential background value offered a modest advantage only for data with highly pronounced cyclical patterns.
  - PSO-NGBM(1,1) demonstrated superior generalization, maintaining lower out-of-sample errors than models with better in-sample fit.
key_figures_tables:
  - Table 1: Forecast accuracy grades based on MAPE → Provides benchmark for interpreting model performance.
  - Table 2: Best-performing models under 70/30 split → PSO-NGBM(1,1) dominated most simulation scenarios.
  - Figure 1: Convergence plot of PSO for NGBM(1,1) → Shows efficient optimization reaching near-optimal solution in ~30 iterations.
  - Table 5: Forecast results of all models → PSO-NGBM(1,1) had lowest out-of-sample MAPE and RMSE.
  - Figure 4: Seasonal-trend decomposition of Philippine GDP → Confirms strong seasonal pattern with Q1 decline and Q4 surge.
key_equations:
  - equation: MAPE = (1/(n-1)) \sum_{t=2}^n |(x^{(0)}(t) - \hat{x}^{(0)}(t)) / x^{(0)}(t)| \times 100\%
    explanation: Out-of-sample percentage error metric minimized by PSO.
  - equation: \hat{x}^{(1)}(k) = \left[ x^{(1)}(1)^{(1-m)} - \frac{b}{a} \right] e^{-a(1-m)(k-1)} + \frac{b}{a}
    explanation: Time response function for NGBM(1,1) AGO sequence.
  - equation: y(t) = \beta_0 t + \beta_1 \cos(\gamma t) + \beta_2 \sin(\gamma t), \gamma = 2\pi/4
    explanation: Harmonic regression for quarterly cycle simulation.
definitions:
  - term: NGBM(1,1)
    definition: Nonlinear Grey Bernoulli Model, a grey systems model incorporating a power index for nonlinearity.
  - term: PSO
    definition: Particle Swarm Optimization, a metaheuristic algorithm for parameter optimization.
  - term: MAPE
    definition: Mean Absolute Percentage Error, a scale-independent forecast accuracy metric.
  - term: RMSE
    definition: Root Mean Square Error, an absolute forecast error metric in original units.
  - term: AGO
    definition: Accumulated Generating Operation, a data transformation in grey models that smoothens sequences.
critical_citations:
  - "[Chen et al., 2006] — Introduced the NGBM(1,1) model framework."
  - "[Cheng et al., 2021] — Proposed exponential background value optimization method."
  - "[Zhou et al., 2008] — Applied PSO to optimize NGBM(1,1) parameters."
relevance:
  topics:
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: Paper analyzes seasonal patterns in Philippine GDP, applicable to spending cycles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly benchmarks forecasting models for economic time series.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Compares NGBM(1,1) variants and GM(1,1) on quarterly sequential data.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: contextual
      justification: Optimization strategies for parameter estimation are analogous to constraint handling.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Nowcasting detects deviations from expected trends, similar to anomaly detection.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides a rigorous evaluation framework using MAPE and RMSE for forecasting modules.
  contribution: "This paper demonstrates that PSO-optimized NGBM(1,1) provides a robust forecasting module for Odin's spending prediction engine. The seasonal decomposition approach directly informs how Odin should handle cyclical spending patterns in the Philippines. The comparative evaluation framework (MAPE, RMSE) can be adopted for Odin's algorithm testing. The finding that optimization techniques outperform background value adjustments guides Odin's choice of parameter tuning methods. Furthermore, the dramatic improvement after seasonal adjustment validates Odin's need for explicit seasonal modeling in its forecasting pipeline."
  directly_justifies:
    - "PSO optimization significantly improves forecasting accuracy over standard grey models."
    - "Seasonal adjustment reduces MAPE from over 5% to below 1% for quarterly data."
    - "70/30 train-test split is more effective than 80/20 for this data size and periodicity."
    - "Exponential background value offers limited benefit compared to PSO optimization."
  limits:
    - "The study uses only 16 quarterly observations, limiting generalizability for longer-term forecasts."
    - "None of the models fully captured sharp quarterly fluctuations, indicating a need for explicit seasonal components."
    - "Seasonal adjustment was applied as post-modeling analysis, not integrated into the grey models themselves [unacknowledged]."
  mapping_rationale: "A systematic scan across all 12 functional domains identified three domains with strong relevance: Spending Forecasting (6.A, 6.B) due to the paper's primary focus on GDP nowcasting, System Evaluation (12.B) due to the rigorous comparative methodology, and Anomaly Detection (8.B) because nowcasting inherently detects deviations from expected trends. The Filipino Cultural Context domain (2.B) was flagged as medium relevance because the paper analyzes seasonal patterns in Philippine data, which directly parallels spending cycles. The Algorithmic Optimization domain (7.D) was marked contextual as parameter optimization is analogous to constraint handling. Domains such as Expense Categorization (3.A-C), Behavioral Profiling (5.A-C), and Mobile Design (9.A-B) were considered and rejected as the paper contains no relevant citeable claims. The Budget Recommendation domain (7.A-C) was rejected despite optimization being mentioned, as the paper does not address allocation or constraint management. Overall, the paper is highly relevant to Odin's forecasting and evaluation modules but provides only indirect support for user-facing features."
limitations:
  - "Limited dataset size (16 quarterly observations) constrains model training."
  - "None of the grey models fully captured short-term volatility in GDP."
  - "Seasonal patterns were handled via preprocessing rather than integrated into the model."
  - "Statistical significance of performance differences between models was not tested [unacknowledged]."
remember_this:
  - "PSO-optimized NGBM(1,1) achieved a 5.45% out-of-sample MAPE for Philippine GDP."
  - "Seasonal adjustment reduced forecasting errors from over 5% to under 1%."
  - "PSO optimization outperformed exponential background value methods in forecast accuracy."
  - "Grey models show promise for short-term forecasting in data-constrained environments."
  - "Explicit seasonal modeling is needed to capture quarterly fluctuations in economic data."
```
---

## Paper 8: Ama_summarized.md

**Source File:** `Ama_summarized.md`

```yaml
paper_id: 10.20944/preprints202508.0349.v1
designation: local-algorithm-specific
title: Analysis of the Food and Income Expenditure Survey 2023 Among Filipino Households
authors: Ama, N. A.
year: 2025
venue: Preprints.org
odin_topics:
  - 2.A
  - 2.B
  - 2.D
  - 3.A
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 6.A
  - 7.A
  - 8.A
  - 12.A
  - 13.A
tldr: Filipino household food spending is income-inelastic, spatially clustered, and higher in rural areas, with household size, income, and location as key nonlinear predictors of food insecurity.
problem_and_motivation: Understanding drivers of food expenditure among Filipino households is fundamental to shaping effective social, agricultural, and economic policies, yet detailed analysis of 2023 FIES data remains limited. This study addresses the gap by using advanced statistical methods to assess how income, geography, livelihood sources, and household characteristics shape food spending patterns and food insecurity.
approach:
  - Data from 163,268 households in the 2023 Philippine Family Income and Expenditure Survey (FIES) were analyzed using RStudio v4.5.1.
  - Principal Component Analysis (PCA) identified dominant income sources, supported by scree plots and loading scores.
  - Spatial clustering was evaluated via regional mapping using GADM shapefiles and visualizations.
  - Rural-urban differences were tested using the non-parametric Mann-Whitney U test due to normality violations.
  - A Generalized Additive Model (GAM) was employed to predict food insecurity, incorporating smooth terms for continuous predictors and a parametric term for urban-rural residence.
  - Log-log Engel curves and a beta regression model were used to analyze income elasticity and the proportion of food spent outside the home, respectively.
findings:
  - num: Food expenditure has an income elasticity of 0.58, confirming food as a necessity good under Engel's Law.
  - num: Rural households spend more on food (Median = ₱102,467) than urban households (Median = ₱80,700).
  - PCA identified retail, transport, and agriculture as dominant income source clusters.
  - Spatial clustering shows Leyte and Bohol have the highest mean food expenditure (≥₱120,000).
  - The GAM explained 27.2% of deviance in food insecurity, with RPCINC as the strongest nonlinear predictor.
  - num: The GAM achieved 90.02% accuracy and an AUC of 0.86 in predicting food insecurity.
  - Urban residence (β = -0.51) was associated with a lower likelihood of food insecurity.
  - Household size showed a significant nonlinear positive association with food insecurity risk.
  - Bread (29.5%) and meat (14.8%) account for the largest shares of food expenditure.
  - Higher-income and rural households spend a larger proportion of food outside the home.
key_figures_tables:
  - Figure 1: Lorenz curve of food expenditure → Food spending is more evenly distributed than income.
  - Figure 2: Histogram of food expenditure per member → Distribution is right-skewed with concentration at lower values.
  - Figure 5: Spatial map of mean food expenditure → High-spending clusters in Leyte and Bohol.
  - Figure 8: GAM partial effect plots → Income and household size show strong nonlinear effects on food insecurity.
  - Figure 10: Engel curve log-log plot → Positive but inelastic relationship between income and food spending.
key_equations:
  - equation: U = n1 * n2 + (n1(n1+1))/2 - R1
    explanation: Mann-Whitney U test statistic for group comparisons.
  - equation: g(E(Y)) = β0 + f1(x1) + ... + fm(xm)
    explanation: Generalized Additive Model with logit link function.
  - equation: log(FOOD_i) = β0 + β1 * log(TINC_i) + ε_i
    explanation: Log-log Engel curve for estimating income elasticity.
  - equation: logit(μ_i) = β0 + β1 * log(INCOME_i) + β2 * URB_i + β3 * FSIZE_i
    explanation: Beta regression model for proportion of food spent outside home.
definitions:
  - term: FIES
    definition: Family Income and Expenditure Survey conducted by the Philippine Statistics Authority.
  - term: PCA
    definition: Principal Component Analysis, a dimensionality reduction technique.
  - term: GAM
    definition: Generalized Additive Model, a flexible regression framework for nonlinear effects.
  - term: RPCINC
    definition: Real per capita income, adjusted for household size.
  - term: Engel's Law
    definition: As income rises, the proportion of income spent on food declines.
  - term: Beta regression
    definition: A regression model for proportions bounded between 0 and 1.
critical_citations:
  - "[Valera et al., 2022] — Found inelastic demand for rice and flexible preferences for meat and dairy."
  - "[Briones, 2022] — Examined food price shocks and cash transfer effects on nutrient intake."
  - "[Bairagi et al., 2022] — Identified structural shifts in rural vs. urban food basket composition."
  - "[Cigaral, 2025] — Reported food as the largest expenditure share (57.2%) in 2021."
relevance:
  topics:
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Highlights dominance of bread and meat in spending, reflecting local dietary patterns.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: Spatial and rural-urban spending variations suggest cyclical/geographic influences.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Mentions spending outside home, but not explicitly tied to festive occasions.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Provides empirical distribution of spending across major food categories.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: References BSP survey and PSA FIES as data sources for understanding spending.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: low
      justification: Acknowledges cross-sectional nature and lack of dietary/nutritional detail.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: PCA-based livelihood segmentation offers a proxy for behavioral profiles.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: contextual
      justification: Segmentation by income sources can inform initial profile estimation.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: GAM and Engel curve analysis demonstrate predictive modeling of food spending.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Income elasticity and food share patterns inform budget allocation strategies.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Identifies spending clusters and outliers in food expenditure distribution.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses accuracy, AUC, and R² to evaluate GAM classification performance.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: contextual
      justification: Food spending patterns indirectly relate to surplus available for savings.
  contribution: "The paper provides empirical benchmarks for income elasticity of food (0.58) and food expenditure distributions that can calibrate Odin's budget recommendation module. Its GAM framework for predicting food insecurity offers a methodological template for Odin's behavioral risk assessment. The PCA-derived livelihood segmentation can inform Odin's cold-start profiling for new users. The rural-urban spending differences provide contextual data for Odin's geographic customization. The beta regression for out-of-home food spending supports Odin's expense categorization logic."
  directly_justifies:
    - "Income elasticity of 0.58 establishes food as a necessity for Filipino households."
    - "Rural households exhibit higher median food spending (₱102,467) than urban (₱80,700)."
    - "Household size and income are significant nonlinear predictors of food insecurity."
    - "Bread and meat account for 29.5% and 14.8% of food expenditure, respectively."
    - "GAM models can achieve 90% accuracy in predicting household financial vulnerability."
  limits:
    - "Cross-sectional FIES data limits causal inference on spending dynamics. [unacknowledged]"
    - "Lack of nutritional/dietary diversity measures restricts analysis of food quality."
    - "Provincial-level aggregation obscures intra-regional disparities."
    - "Self-reported income may suffer from recall bias, especially in informal sectors."
    - "No detailed evaluation of algorithmic modules for budget recommendation is provided."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes identified relevant connections. Domains flagged as relevant include Filipino Cultural Context (2.A, 2.B, 2.D), Expense Categorization (3.A), Existing Systems (4.A, 4.B), Behavioral Profiling (5.A, 5.B), Forecasting (6.A), Budget Recommendation (7.A), Anomaly Detection (8.A), and Evaluation (12.A). High relevance was assigned to 6.A due to the predictive GAM and Engel curve modeling. Medium relevance was assigned to 2.A, 2.B, 3.A, 5.A, 7.A, 12.A, and 13.A based on empirical spending patterns. Borderline cases include 2.D (spending cycles) and 7.C (constrained optimization) — the paper discusses Engel curves but not optimization, so 7.C was rejected. Domains 9.A, 9.B, 10.A, 10.B, 11.A, 11.B, and 13.C were rejected as the paper does not address mobile design, privacy, retention, or surplus mechanisms. Overall, the paper provides strong empirical grounding for Odin's core financial understanding modules."
limitations:
  - "Cross-sectional design cannot establish causal relationships between income and food spending. [unacknowledged]"
  - "Lack of detailed nutritional and dietary diversity measures limits holistic food security assessment. [unacknowledged]"
  - "Spatial analysis limited to provincial aggregates, hiding intra-provincial disparities."
  - "Reliance on self-reported data may introduce recall bias among informal sector households."
  - "Beta regression pseudo-R² of 0.1403 indicates limited explanatory power for out-of-home food spending. [unacknowledged]"
remember_this:
  - "Food expenditure income elasticity is 0.58, confirming Engel's Law for Filipino households."
  - "Rural households spend more on food and face higher food insecurity risk."
  - "GAM achieved 90% accuracy in predicting food insecurity from household characteristics."
  - "Bread (29.5%) and meat (14.8%) dominate Filipino household food spending."
  - "Household size and income exhibit strong nonlinear associations with food insecurity."
```
---

## Paper 9: Cucio & Hennig_summarized.md

**Source File:** `Cucio & Hennig_summarized.md`

```yaml
paper_id: "10.5089/9798400295125.001"
designation: "local-algorithm-specific"
title: "Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and Complementarity"
authors: "Cucio, M.; Hennig, T."
year: 2025
venue: "IMF Working Paper"
odin_topics:
  - "1.A"
  - "1.B"
  - "1.C"
  - "2.A"
  - "2.D"
  - "4.A"
  - "4.B"
  - "6.A"
  - "8.A"
  - "9.A"
  - "10.A"
tldr: "One-third of Philippine workers are highly exposed to AI, with 61% of those in high-complementarity roles suggesting augmentation rather than displacement."
problem_and_motivation: "Rapid AI advancements may significantly transform labor markets, but the specific impact on the Philippine workforce, particularly its large BPO sector, remains underexplored. Understanding this impact is crucial for informing policy to harness benefits and mitigate job displacement."
approach:
  - "Merged AI exposure (Felten et al., 2021) and complementarity (Pizzinelli et al., 2023) scores with microdata from the Philippine Statistics Authority's October 2022 Labor Force Survey (183,602 observations)."
  - "Classified occupations into high exposure/high complementarity, high exposure/low complementarity, and low exposure categories based on median scores."
  - "Analyzed correlations between AI exposure/complementarity and demographic indicators like age, gender, education, wage, and sector."
  - "Compared Philippine results to other Asian economies using ILO employment data for a regional context."
  - "Assessed AI preparedness using the AI Preparedness Index (AIPI) covering digital infrastructure, human capital, innovation, and regulation."
findings:
  - "num: 36% of the Philippine workforce is highly exposed to AI."
  - "num: Of the highly exposed workers, 61% (22% of total workforce) are in high-complementarity roles, indicating potential augmentation."
  - "num: 39% of highly exposed workers (14% of total workforce) are in low-complementarity jobs, at risk of displacement."
  - "College-educated, young, urban, female, and well-paid service sector workers are most exposed to AI."
  - "The BPO sector has the highest proportion of jobs at risk (73% high exposure/low complementarity), though it represents only 3% of total employment."
  - "Government workers are the most exposed class of worker, driven by clerical roles."
  - "The Philippines scores well on human capital but lags in digital infrastructure compared to regional peers."
  - "The government has introduced a National AI Strategy Roadmap and pending legislation, but a comprehensive legal framework is lacking."
key_figures_tables:
  - "Figure 1: Philippine labor force summary statistics → Sets demographic context for AI exposure analysis."
  - "Figure 6: Exposure and complementarity across occupations → Visualizes how different occupational groups are categorized."
  - "Figure 8: Exposure and complementarity by demographic factors → Shows AI exposure correlates with gender, education, and wage."
  - "Table 2: AI exposure and complementarity in the Philippines → Provides key percentages for each category."
  - "Figure 9: AI preparedness across Asia → Indicates Philippines lags in digital infrastructure."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "AIOE"
    definition: "AI Occupational Exposure, a measure of overlap between AI capabilities and occupational tasks."
  - term: "Complementarity"
    definition: "The extent to which AI augments rather than replaces human labor in an occupation."
  - term: "BPO"
    definition: "Business Process Outsourcing, a key service sector in the Philippines."
  - term: "AIPI"
    definition: "AI Preparedness Index, a composite measure of a country's readiness for AI adoption."
critical_citations:
  - "[Felten et al., 2021] — Developed the AI exposure index used in this analysis."
  - "[Pizzinelli et al., 2023] — Developed the complementarity score used in this analysis."
  - "[Cazzaniga et al., 2024] — Provided the methodological framework and AI Preparedness Index."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "high"
      justification: "Analysis specifically examines Filipino workforce by age, education, and sector."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "medium"
      justification: "Discusses wage inequality and BPO sector dynamics relevant to financial structure."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "contextual"
      justification: "Provides labor market context that informs financial behavior, but does not directly study it."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "contextual"
      justification: "Focus on Filipino BPO and service sectors, but not on specific financial practices."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "contextual"
      justification: "Analysis of BPO sector exposure provides context for spending cycles, but is not the focus."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "low"
      justification: "Tangentially mentions digital infrastructure but does not review PFMS."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "low"
      justification: "Identifies gaps in digital infrastructure and skills, relevant to PFMS design but not directly."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses forecasting of AI impact on employment, analogous to forecasting spending."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "low"
      justification: "Mentions bias and errors in AI, relevant to anomaly detection but not central."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "low"
      justification: "Discusses digital infrastructure gaps, a prerequisite for mobile-first design."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "low"
      justification: "Mentions AI regulation and data privacy as a gap, but does not analyze PFMS data privacy."
  contribution: "This paper provides a granular, data-driven mapping of AI exposure and complementarity across the Philippine labor force, quantifying that 36% of workers are highly exposed, with 14% at displacement risk. It uniquely identifies the BPO sector as most vulnerable (73% high risk), despite its small workforce share, highlighting macro-critical spillover risks. The study correlates exposure with demographic factors (e.g., college-educated, female, young workers are most exposed), which can inform targeted policy interventions. By linking occupational AI scores with local LFS microdata and assessing AI preparedness (noting digital infrastructure gaps), the findings directly justify Odin's need for robust digital infrastructure and user-centric design."
  directly_justifies:
    - "College-educated and young service sector workers are most exposed to AI, indicating a need for financial tools tailored to this demographic."
    - "The BPO sector's high displacement risk (73% of its workers) underscores the importance of financial resilience features for affected users."
    - "Gaps in digital infrastructure suggest that Odin's mobile-first design must be robust and work under connectivity constraints."
    - "AI preparedness gaps in regulation and ethics support Odin's focus on data privacy and user trust."
    - "The potential for AI to augment high-complementarity jobs (22% of workforce) justifies Odin's predictive modeling to enhance user productivity."
  limits:
    - "The analysis is static and does not account for workforce retraining or new job creation over the medium term."
    - "Assumes task content of occupations in the Philippines is identical to the U.S. O*NET database, potentially underestimating exposure."
    - "AIPI does not capture all relevant dimensions for AI adoption, such as the importance of the BPO sector."
  mapping_rationale: "A systematic scan across all 12 functional domains was performed. The paper was flagged as highly relevant to the Filipino Demographics domain (1.A, 1.B) because it provides a detailed socio-economic breakdown of the Filipino workforce by age, education, and sector, directly informing the target user profile for Odin. It was also highly relevant to Predictive Modeling (6.A) and Behavioral Profiling (5.A, 5.B), as it presents a methodology for classifying workers into risk categories based on a combination of metrics (exposure and complementarity), analogous to classifying users by financial behavior. The paper's detailed analysis of the BPO sector and its vulnerability was considered a borderline case for Existing Systems (4.A) and Spending Cycles (2.D), but relevance was rated as low/contextual because the paper does not review specific PFMS software or spending patterns. Domains like Budget Recommendation (7.A-D) and Savings/Debt Management (13.A-C) were considered and rejected as the paper does not address financial allocation or goal management. The analysis of AI regulation and infrastructure gaps was deemed contextual for Data Privacy (10.A) and Mobile-First Design (9.A). Overall, the paper is highly relevant to Odin's understanding of its user base and the economic pressures that drive financial behavior, providing a strong justification for a predictive, user-centric financial management system."
limitations:
  - "Static analysis does not capture future workforce adaptation or job creation. [unacknowledged]"
  - "Relies on U.S. O*NET data, which may not perfectly reflect task content in Philippine occupations."
  - "Does not quantify the magnitude of potential productivity gains or wage effects."
  - "Does not account for spillover effects from BPO sector changes to the broader economy."
  - "AI Preparedness Index may not capture all relevant dimensions for Philippines-specific adoption."
remember_this:
  - "One-third of Philippine workers are highly exposed to AI."
  - "14% of the workforce is in low-complementarity roles at displacement risk."
  - "BPO workers are most at risk, with 73% in high-exposure, low-complementarity jobs."
  - "College-educated, young, and female service workers are most exposed but also most complementary."
  - "Philippines lags in digital infrastructure, a key barrier to AI adoption."
```
---

## Paper 10: Mariano & Monreal_summarized.md

**Source File:** `Mariano & Monreal_summarized.md`

```yaml
paper_id: "10.1145/3785171.3785187"
designation: "local-algorithm-specific"
title: "Predict, Optimize, Deliver: Demand Forecasting and Resource Optimization for a Market Research Firm"
authors: "Mariano, M.T.G.; Monreal, R.N."
year: 2025
venue: "International Conference on Business and Information Management (ICBIM 2025)"
odin_topics:
  - "6.A"
  - "6.B"
  - "7.C"
  - "7.D"
  - "4.B"
tldr: "An integrated forecasting and optimization framework using Prophet and MILP improves resource allocation and cost efficiency in a market research firm."
problem_and_motivation: "Professional service firms face fluctuating demand and manual workforce planning fails to adapt, leading to inefficiencies. There is a need for a data-driven approach that selects appropriate forecasting methods and operationalizes them into optimal resource allocation under real-world constraints."
approach:
  - "Historical billable hours from a Manila-based service center (Jan 2018–Dec 2024) were used as the primary dataset."
  - "Four forecasting models (ARIMA, Holt-Winters, Prophet, LSTM) were tuned and evaluated using MAE, RMSE, and MAPE across multiple train-test splits and a 30-day holdout."
  - "Prophet achieved the lowest weighted error and was selected for its balance of accuracy, interpretability, and speed."
  - "A Pyomo-based MILP optimization model minimized excess resource hours subject to employee availability, work-hour caps, and client-specific demand constraints."
  - "Forecast bands derived from RMSE were incorporated to simulate over- and under-forecasting scenarios."
  - "The framework was deployed in an interactive PowerBI dashboard for dynamic workforce planning."
findings:
  - "num: Prophet achieved the lowest weighted error for Client 1 (13.038) and Client 2 (27.786) on a 30-day holdout."
  - "num: Prophet's overall weighted score (10.456) outperformed ARIMA (11.582), Holt-Winters (13.062), and LSTM (11.634)."
  - "The optimization model respected all constraints and achieved near-zero unmet demand across scenarios."
  - "Resource utilization averaged up to 106% for shared staff in over-forecasting scenarios, indicating tight capacity."
  - "Cumulative costs increased significantly with forecast errors, highlighting the value of accurate short-term forecasting."
key_figures_tables:
  - "Table 3: Summary of weighted error metrics for each model and client → Prophet has lowest error for both clients."
  - "Table 4: Overall model selection scores → Prophet ranks first due to accuracy and interpretability."
  - "Table 5: Optimized average resource utilization per employee under three scenarios → utilization varies widely, with S2 at 106% under over-forecast."
  - "Figure 5: Resource distribution by forecast scenario → shared resources absorb variability; dedicated analysts have fixed loads."
  - "Figure 6: Cumulative allocation cost by forecast scenario → small forecast errors compound into significant cost gaps."
  - "Figure 7: Resource mapping and utilization dashboard → interactive visualizations enable agile decision-making."
key_equations:
  - equation: "min \\sum_{t} (C_{regular} \\sum_{i} x_{i,C1,t} + C_{overtime} \\sum_i o_{i,t} + C_{penalty} (E_{1,t-1} + E_{2,t-1}))"
    explanation: "Minimizes total cost from regular hours, overtime, and penalties for unmet demand."
definitions:
  - term: "ARIMA"
    definition: "Autoregressive Integrated Moving Average, a classical time-series model for stationary data."
  - term: "LSTM"
    definition: "Long Short-Term Memory, a recurrent neural network for sequential data."
  - term: "Prophet"
    definition: "Open-source forecasting model from Facebook that decomposes trend, seasonality, and holiday effects."
  - term: "MILP"
    definition: "Mixed-Integer Linear Programming, an optimization method with integer and continuous variables."
  - term: "MAE"
    definition: "Mean Absolute Error, a metric for forecast accuracy."
  - term: "RMSE"
    definition: "Root Mean Squared Error, penalizing large errors."
  - term: "MAPE"
    definition: "Mean Absolute Percentage Error, relative error metric."
critical_citations:
  - "[Boadi-Sarpong et al., 2023] — resource allocation strategies for competitiveness."
  - "[Sharma & Singh, 2022] — forecasting resource fulfilment in IT consulting."
  - "[Wang et al., 2024] — network flow approach to scheduling."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Compares multiple predictive models (ARIMA, Prophet, LSTM) for demand forecasting, directly informing predictive modeling in PFMS."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Evaluates specific forecasting algorithms and their performance metrics, providing evidence for algorithm selection in spending forecasting."
    - code: "7.C"
      name: "Constrained Optimization Approaches for Budget Allocation"
      relevance: "high"
      justification: "Uses constrained MILP to allocate resources under demand and capacity constraints, analogous to budget allocation optimization."
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "medium"
      justification: "Introduces forecast bands from RMSE to handle demand uncertainty, simulating infeasibility and improving robustness."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "low"
      justification: "Critiques manual Excel-based planning and highlights gaps in adapting to demand volatility, relevant to limitations of existing PFMS."
  contribution: "The forecasting comparison (6.A, 6.B) provides a methodology for selecting models for spending prediction in Odin's forecasting module. The constrained optimization model (7.C) directly informs Odin's budget recommendation engine by demonstrating how to allocate limited resources under multiple constraints. The use of forecast bands (7.D) offers a strategy for handling infeasibility, which can be adapted for Odin's budget adjustment recommendations. The PowerBI dashboard visualization, though not mobile-focused, illustrates how interactive data exploration can support user engagement and decision transparency."
  directly_justifies:
    - "Prophet offers a balance of accuracy and interpretability suitable for operational forecasting in resource-constrained settings."
    - "Constrained optimization with MILP can allocate resources to meet demand while respecting work-hour caps and employee availability."
    - "Forecast bands derived from RMSE improve allocation resilience by simulating over- and under-forecasting."
  limits:
    - "The study focuses on resource allocation for a firm, not individual spending behavior or personal financial management."
    - "The optimization model assumes cost minimization, not personalized budget constraints or savings goals."
    - "Results are based on a single market research firm, limiting generalizability to other PFMS contexts."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains flagged as relevant were Spending Forecasting (6.A, 6.B) and Budget Recommendation (7.C, 7.D) due to the paper's focus on predictive modeling and constrained optimization. The Existing Systems domain (4.B) was also noted for its critique of manual planning, though with low relevance. Other domains (Filipino Cultural Context, Expense Categorization, Behavioral Profiling, Anomaly Detection, Mobile Design, Data Privacy, Retention, System Evaluation, Savings/Debt) were considered and rejected because the paper does not address those aspects. Borderline cases: seasonal spending patterns (2.B, 2.D) were touched upon via time-series decomposition but not emphasized, so they were excluded. Overall, the paper provides strong technical evidence for forecasting and optimization modules in Odin."
limitations:
  - "The analysis was restricted to output-based variables (billable hours) and did not include input-level factors like individual analyst skill."
  - "The forecasting model used internal historical data only and did not incorporate external economic indicators that may influence demand."
  - "Caution is warranted for long-range forecasting as the model does not account for rare high-impact events such as pandemics."
  - "The effectiveness of the proposed system is highly dependent on consistent and accurate updating of time-tracking data."
remember_this:
  - "Prophet achieved the lowest weighted error (10.456) among four models."
  - "MILP optimization respected all constraints and achieved near-zero unmet demand."
  - "Forecast errors compound costs significantly, emphasizing short-term planning."
  - "Interactive dashboards enable agile workforce planning."
```
---

## Paper 11: Santiago_summarized.md

**Source File:** `Santiago_summarized.md`

```yaml
paper_id: 10.26483/ijarcs.v16i3.7256
designation: local-algorithm-specific
title: BUDGET AND FINANCIAL MANAGEMENT INFORMATION SYSTEM FOR PUBLIC ELEMENTARY SCHOOLS: ANALYTICS AND PREDICTIVE INSIGHTS FOR MOOE ALLOCATION USING LINEAR REGRESSION
authors: Santiago, R. L. T.; Villarica, M. V.; Bernardino, M. P.
year: 2025
venue: International Journal of Advanced Research in Computer Science
odin_topics:
  - 1.A
  - 1.B
  - 2.D
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 7.C
  - 7.D
  - 8.A
  - 8.B
  - 9.A
  - 10.A
  - 10.B
  - 11.A
  - 12.B
tldr: Develops an AI-driven financial management system for Philippine public schools that uses linear regression to forecast Maintenance and Other Operating Expenses allocations.
problem_and_motivation: Public elementary schools in the Philippines face significant challenges in managing financial resources due to reliance on manual processes that are prone to errors, inefficiencies, and a lack of transparency. There is a lack of dedicated, digital financial management systems tailored to the operational needs of these schools. This study addresses the need for an automated, accountable, and data-driven solution to improve budget allocation, expenditure tracking, and compliance with DepEd regulations.
approach:
  - The system was developed using an Agile methodology, incorporating continuous stakeholder feedback from school administrators and DepEd auditors.
  - The core AI feature uses a linear regression model built with Python and Scikit-learn to forecast future MOOE allocations based on historical spending data.
  - The system includes modules for budget allocation, expenditure tracking with real-time dashboards, and automated DepEd-compliant report generation.
  - The system was built using XAMPP for local server environment, PHP for dynamic pages, MySQL for database, and Dompdf/PhpSpreadsheet for report generation.
  - A black-box testing approach was employed, using equivalence partitioning to validate system functionality and robustness across key modules.
  - System quality was evaluated against ISO/IEC 25010 and ISO 27001 standards, and user acceptance was assessed using the Technology Acceptance Model.
findings:
  - num: The linear regression model achieved an R² score of 92.81%, indicating high explanatory power for budget variance.
  - num: The model's Mean Absolute Error was ₱1,532.75, and Root Mean Square Error was ₱2,126.84, confirming minimal prediction errors.
  - num: Black-box testing was conducted with 37 test cases, with most modules passing successfully and only minor UI and validation issues identified.
  - num: User acceptance evaluation showed strong approval with weighted means above 4.3 on a 5-point scale across all TAM dimensions.
  - The BFMIS enhances financial transparency and accountability through real-time dashboards and audit trails for school administrators and auditors.
  - AI-driven reporting automates the generation of financial summaries and variance analysis reports, reducing manual effort and aligning with DepEd policies.
  - The system's ability to generate predictive insights enables proactive, evidence-based decision-making for budget planning.
key_figures_tables:
  - Table 2: Black Box Test Case Table summarizes the functional coverage and test case execution across all system modules.
  - Table 4: Regression Model Performance presents MAE, RMSE, and R² score, confirming the predictive model's reliability.
  - Table 5: Summary of Evaluation Results shows high user ratings for system quality, ease of use, and satisfaction.
  - Figure 8: MOOE Prediction Page visualizes the comparison between predicted and actual budget allocations, highlighting data-driven insights.
  - Figure 10: Actual vs. Predicted MOOE Allocations per Category illustrates the model's accuracy in forecasting category-wise budgets.
key_equations:
  - equation: R^2 = 0.9281
    explanation: Indicates model explains 92.81% of budget variance.
  - equation: MAE = ₱1,532.75
    explanation: Represents the average absolute prediction error in pesos.
  - equation: RMSE = ₱2,126.84
    explanation: Confirms minimal large prediction errors enhancing reliability.
definitions:
  - term: MOOE
    definition: Maintenance and Other Operating Expenses, government-allocated funds for school operations.
  - term: BFMIS
    definition: Budget and Financial Management Information System developed in this study.
  - term: TAM
    definition: Technology Acceptance Model, a framework for assessing user acceptance of technology.
  - term: DepEd
    definition: Department of Education, the governing body for Philippine public schools.
  - term: AIP
    definition: Annual Implementation Plan, a tool for school-based management translating long-term goals into yearly actions.
critical_citations:
  - "[Pressman & Maxim, 2014] — Provides black-box testing guidelines for software validation."
  - "[Venkatesh & Davis, 2000] — Foundation for the Technology Acceptance Model used in UAT."
  - "[Byol & Foygel, 2023] — Insight on black box testing for financial systems."
  - "[Roustaei, 2024] — Justifies use of linear regression for predictive modeling with limited data."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: The study focuses on financial management within public schools, a context relevant to the financial environment of Filipino professionals.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: contextual
      justification: The paper analyzes budget allocation structures (MOOE) within the Philippine public school system, which is part of the financial landscape for professionals in education.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: The study mentions cyclical spending patterns for items like electricity and graduation programs, touching on seasonal school-related expenses.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: The BFMIS includes modules for categorizing MOOE expenses, providing a framework for organizing school expenditures.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: The design of the system's expense tracker and reporting module reflects considerations for effective financial data organization.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: The study explicitly reviews the landscape of existing financial management systems in Philippine public schools and their limitations.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: The research is motivated by identified gaps in manual financial processes, directly addressing limitations of current systems.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: The core contribution is the development of a predictive linear regression model for budget forecasting, a key predictive modeling application.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: The linear regression algorithm forecasts future MOOE allocations based on historical sequential spending data.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: The paper discusses participatory budgeting strategies and the use of the AIP, which are relevant domain knowledge for budget recommendation.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: While not strictly a recommendation system, the predictive module provides data-driven suggestions for future budget allocations.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: low
      justification: The system optimizes allocation based on historical trends, but not in a formal constrained optimization framework.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: contextual
      justification: The study touches on identifying misalignments and planning for reallocations, but does not detail infeasibility handling.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: The system has a feature for detecting misalignment between planned and predicted spending, which is a form of anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: The detection method is not based on a specialized anomaly detection algorithm but rather a comparison of planned vs. actual values.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: The system is designed for desktop use but includes UI considerations for usability, which is tangentially related to mobile-first design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: The system incorporates role-based access control and is evaluated against ISO 27001 standards for information security.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: High user acceptance and satisfaction ratings, as measured by TAM, indicate a positive perception of trustworthiness and reliability.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: The system includes features like real-time dashboards that can support user engagement, but this is not a primary focus of the study.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: The linear regression model's performance is rigorously evaluated using MAE, RMSE, and R² metrics.
  contribution: For Odin's spending forecasting module (6.A/6.B), the paper provides a validated linear regression approach for forecasting sequential spending data, with clear metrics (MAE, RMSE, R²). For the expense categorization module (3.A/3.B), it demonstrates a functional categorization framework for school expenses, including real-time tracking and reporting. The study also offers insights for Odin's budget recommendation module (7.B) by showing how predictive insights can inform data-driven budget planning. The evaluation against ISO standards (10.A/10.B) and use of TAM (11.A) provide a methodological framework for validating Odin's system quality and user acceptance. The paper's development process highlights the importance of user-centered design and stakeholder feedback for system adoption (11.B).
  directly_justifies:
    - "Linear regression can effectively forecast budget allocations with high accuracy (R² = 0.9281) for public schools."
    - "System-generated predictive insights support proactive financial decision-making and strategic planning."
    - "Automated, DepEd-compliant reporting reduces manual errors and enhances transparency in financial operations."
    - "User acceptance is positively influenced by perceived usefulness and ease of use in school financial systems."
  limits:
    - "The system's functionality is limited to desktop use and does not include a mobile-first design."
    - "The model's accuracy depends on the quality and completeness of historical data input."
    - "The study's focus is on public elementary schools in one Philippine province, limiting generalizability to other contexts."
    - "Basic security features and manual updates for policy changes are noted as limitations."
    - "The study does not include a formal comparison with other forecasting algorithms to justify the choice of linear regression."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The domains flagged as relevant are: Existing Systems & Gaps (high relevance to 4.A, 4.B), Spending Forecasting (high relevance to 6.A, 6.B), Expense Categorization (medium relevance to 3.A, 3.B), Budget Recommendation (medium relevance to 7.B), Data Privacy & User Trust (medium relevance to 10.A, 10.B), and System Evaluation (high relevance to 12.B). Borderline cases included: seasonal spending (2.D) which was assigned low relevance as it is not a primary focus; user constraints (3.C) and optimization approaches (7.C, 7.D) which were considered but not selected due to the paper's focus on predictive forecasting rather than constraint-based optimization. Domains like Mobile-First Design and Behavioral Profiling were rejected due to a lack of relevant content. The overall relevance of the paper to Odin is high, as it provides a concrete example of a linear regression-based predictive system for financial allocation, supported by rigorous evaluation and a user-centered development methodology.
limitations:
  - "The scope is limited to public elementary schools in one Philippine province, potentially limiting generalizability."
  - "The system's reliance on accurate historical data is a key limitation for the predictive model's performance."
  - "The system lacks a mobile-first design, which is a significant limitation for accessibility in a modern context. [unacknowledged]"
  - "The study did not compare the linear regression model with other machine learning techniques to justify its selection. [unacknowledged]"
  - "The evaluation of security was based on standards review rather than a formal security audit."
remember_this:
  - Linear regression achieved a 92.81% R² score for forecasting school budgets.
  - The BFMIS system automates budget allocation and expenditure tracking.
  - Users strongly agreed on the system's high usability and security features.
  - The system generates DepEd-compliant reports, automating financial submissions.
  - A phased implementation plan with risk mitigation ensures sustainable adoption.
```
---

## Paper 12: Onsay & Rabajante-2024b_summarized.md

**Source File:** `Onsay & Rabajante-2024b_summarized.md`

```yaml
paper_id: "10.1016/j.sctalk.2024.100387"
designation: "local-algorithm-specific"
title: "When machine learning meets econometrics: Can it build a better measure to predict multidimensional poverty and examine unmeasurable economic conditions?"
authors: "Onsay, E. A.; Rabajante, J. F."
year: 2024
venue: "Science Talks"
odin_topics:
  - "6.A"
  - "6.B"
  - "12.A"
  - "12.B"
  - "12.C"
tldr: "Combines machine learning and econometrics to predict multidimensional poverty in Philippine indigenous communities, finding random forest outperforms other algorithms with high accuracy and R-square."
problem_and_motivation: "Poverty measurement is costly and time-consuming, and existing methods suffer from sampling errors. Indigenous communities have complex socioeconomic conditions that are often studied qualitatively, lacking disaggregated quantitative measures. This gap hinders effective policy targeting."
approach:
  - "Uses census data from Goa, Camarines Sur, covering all households including indigenous communities, with 15 multidimensional socioeconomic indicators."
  - "Applies econometric models (logit and probit) to establish causal relationships between predictors and poverty status."
  - "Trains and compares multiple machine learning regressors and classifiers: random forest, XGBoost, LightGBM, SVM, AdaBoost, GaussianNB, and others."
  - "Evaluates model performance using RMSE, MSE, R-square, and accuracy, and uses pipeline algorithms for classification."
  - "Conducts causality tests to identify key poverty predictors, including household size, informal settler status, and indicators of health, education, and income."
findings:
  - "num: Random forest achieved the highest R-square of 0.9208 and accuracy of 0.9108 for poverty prediction."
  - "num: For the general population, 63.70% live in poverty and 51.10% lack food access."
  - "num: For indigenous communities, 82% live in poverty and 71% lack food access."
  - "Household size and informal settler status are strong positive predictors of poverty."
  - "num: Random forest had the lowest RMSE (0.3298) compared to XGBoost (0.4001) and LightGBM (0.3642) for regressors."
  - "num: In pipeline classification, random forest achieved 94.89% accuracy for indigenous communities."
key_figures_tables:
  - "Figure 2: Multidimensional poverty evaluation results → Shows deprivation across education, income, and health indicators."
  - "Figure 4: RMSE of regressors → Random forest has lowest RMSE (0.3298)."
  - "Figure 6: R-square of regressors → Random forest highest R-square (0.9208)."
  - "Figure 7: Performance evaluation classifiers → Random forest accuracy 0.9108, pipeline 94.89%."
  - "Figure 13: R-square for indigenous communities → Random forest 0.9208."
  - "Figure 14: Accuracy for indigenous communities → Random forest 90.69% random, 94.89% pipeline."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Multidimensional poverty"
    definition: "Poverty measured across multiple dimensions such as education, health, income, and living standards."
  - term: "Indigenous People (IP)"
    definition: "Members of indigenous communities in the Philippines, often marginalized."
  - term: "Deprivation"
    definition: "Lack of access to basic necessities or indicators."
critical_citations:
  - "[Alkire, 2005] — Capability approach to poverty measurement."
  - "[Foster et al., 1984] — Decomposable poverty measures."
  - "[Sobreviñas, 2020] — CBMS data for poverty dynamics."
  - "[Onsay & Rabajante, 2024] — Data brief and dataset."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Uses ML to predict poverty, demonstrating predictive modeling for financial vulnerability."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Compares multiple forecasting algorithms (RF, XGBoost, LightGBM) on socioeconomic data."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Provides systematic evaluation of ML models using RMSE, R-square, and accuracy."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Specifically evaluates classification and regression modules for predictive accuracy."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "medium"
      justification: "Methodology of model comparison can inform evaluation of recommendation systems."
  contribution: "This paper demonstrates the feasibility of using machine learning for predictive classification of economic vulnerability, which can inform spending forecasting and anomaly detection modules in Odin. The systematic evaluation framework comparing multiple algorithms provides a template for selecting optimal models for Odin's algorithmic components. The causal identification of poverty predictors using econometrics can guide feature engineering for user profiling and budget recommendation. The replicable methodology using publicly available census data supports data-driven policy targeting, which aligns with Odin's goal of personalized financial management."
  directly_justifies:
    - "Random forest can achieve over 90% accuracy in classifying poverty status."
    - "Household size and informal settler status are strong predictors of economic status."
    - "Econometric causal testing can identify relevant predictors for ML models."
    - "The methodology is replicable for other regions with available data."
  limits:
    - "The paper focuses on poverty, not spending behavior, limiting direct applicability to expenditure forecasting."
    - "The data is cross-sectional, not time-series, so temporal spending patterns are not modeled."
    - "Models are trained on rural indigenous communities, which may not generalize to urban young professionals."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was conducted. Domains flagged as relevant include Spending Forecasting (6) and System Evaluation (12), as the paper directly addresses predictive modeling and algorithm evaluation. Specifically, topic 6.A and 6.B were assigned high relevance due to the use of ML for prediction and comparison of algorithms. Topics 12.A and 12.B were assigned high relevance for the evaluation frameworks and module assessment; 12.C received medium relevance as the evaluation methodology could inform budget recommendation systems. Domains related to Filipino cultural context (2), expense categorization (3), existing systems (4), behavioral profiling (5), budget recommendation (7), anomaly detection (8), mobile-first design (9), data privacy (10), user retention (11), and savings/debt management (13) were considered but rejected because the paper does not address these topics; it focuses on poverty measurement rather than personal finance management. The overall relevance to Odin is moderate, providing methodological inspiration for predictive modules rather than direct content."
limitations:
  - "Cross-sectional data limits temporal forecasting capabilities. [unacknowledged]"
  - "Models are not validated on external datasets, reducing generalizability. [unacknowledged]"
  - "The paper does not address real-time or sequential data, which are central to PFMS. [unacknowledged]"
  - "The focus on indigenous communities may not represent the broader Filipino young professional demographic. [unacknowledged]"
remember_this:
  - "Random forest achieved 0.9208 R-square and 0.9108 accuracy for poverty prediction."
  - "Household size and informal settler status are key poverty predictors."
  - "The study demonstrates cost-effective poverty measurement using ML."
  - "Causal econometric testing identifies robust predictors for ML models."
  - "Methodology is replicable with available census data."
```
---

## Paper 13: Espiritu et al_summarized.md

**Source File:** `Espiritu et al_summarized.md`

```yaml
paper_id: 6c9e3b8a-4f5d-5a8e-9b2c-1f3a4b5c6d7e
designation: local-algorithm-specific
title: Data-Driven Decision Making in Scholarship Programs: Leveraging Decision Trees and Clustering Algorithms
authors: Espiritu, F. V.; Natividad, M. C. B.; Velasco, R. A.
year: 2024
venue: International Journal in Information Technology in Governance, Education and Business
odin_topics:
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 9.A
  - 9.B
  - 12.A
  - 12.B
tldr: Integrates decision trees and clustering with an online system to improve efficiency and decision-making for a Philippine scholarship program facing a massive application surge.
problem_and_motivation: The BRO-Ed scholarship program in Isabela province faces a 541.1% surge in applications, overwhelming its manual review process. This lack of systematic evaluation leads to inefficiency and risks missing key success factors, necessitating a data-driven solution to improve selection and resource allocation.
approach:
  - Historical scholarship application data from the PGI BRO Ed Scholarship program was integrated and preprocessed to ensure quality and integrity.
  - Decision tree (C4.5) and K-means clustering algorithms were implemented on the cleaned dataset for pattern recognition and insight extraction.
  - A user-friendly online registration platform was developed using Handlebars.js, Node.js with Express.js, and MySQL to enhance accessibility.
  - Algorithm performance was evaluated using accuracy, precision, recall, and F1-score metrics.
  - The system's impact was assessed through user satisfaction surveys and comparative success rate analysis against traditional methods.
findings:
  - Preprocessing identified parent occupation, academic performance, and financial need as high-impact factors influencing scholarship success.
  - num: 31% higher success rate was observed for applicants using the online system compared to traditional methods.
  - The implemented algorithms achieved an 80% predictive accuracy for successful scholarship applications.
  - User satisfaction surveys indicated a high preference for the online system due to its ease of use and accessibility.
  - The integration of data mining techniques revealed hidden patterns, enabling more informed and fairer selection decisions.
key_figures_tables:
  - Figure 4: Impact of online registration system on success rates → Demonstrates a 31% improvement over traditional methods.
  - Table 5: Factors influencing scholarship application success → Identifies parent occupation, academic performance, and financial need as high-impact factors.
  - Figure 5: Comparison of predictive accuracy for scholarship application outcomes → Shows 80% accuracy for predicting success vs. 70% for failure.
key_equations:
  - equation: "Accuracy = (TP + TN) / (TP + TN + FP + FN)"
    explanation: Proportion of correctly classified instances among all cases.
  - equation: "Precision = TP / (TP + FP)"
    explanation: Proportion of true positives among all positive predictions.
  - equation: "Recall = TP / (TP + FN)"
    explanation: Proportion of true positives identified correctly.
  - equation: "F1-score = 2 * (Precision * Recall) / (Precision + Recall)"
    explanation: Harmonic mean of precision and recall, balancing both metrics.
definitions:
  - term: C4.5 Algorithm
    definition: A well-known decision tree algorithm used to handle categorical and numerical data effectively.
  - term: K-Means Clustering
    definition: A simple and efficient algorithm for partitioning a dataset into groups with similar properties.
  - term: PII
    definition: Personally Identifiable Information, which was anonymized to protect applicant privacy.
critical_citations:
  - "[Yağcı, 2022] — Provides basis for predictive modeling using ML algorithms."
  - "[Alyahyan & Düştegör, 2020] — Offers literature review and best practices for predictive modeling."
  - "[Sugiyarti et al., 2018] — Demonstrates integration of data-driven approaches in scholarship administration."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides a case study of a public system (scholarship) transitioning to a data-driven approach.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly addresses operational challenges like manual review and processing bottlenecks.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: The method groups applicants (clustering), which is analogous to profiling.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses decision trees (classification) to predict success based on applicant features.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: Mentions a "user-friendly online platform" and improved accessibility for remote areas.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: Discusses front-end framework (Handlebars.js) and interface design but not finance-specific UX.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Evaluates system effectiveness using quantitative metrics (accuracy, user satisfaction).
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Explicitly evaluates the prediction algorithms using accuracy, precision, recall, and F1-score.
  contribution: "This paper directly informs Odin's System Evaluation module (12.B) by demonstrating a clear evaluation framework for algorithmic modules using accuracy, precision, recall, and F1-score. Its approach to handling a surge in applications via an online system and data mining provides a justification for Odin's mobile-first design and anomaly detection modules. The identification of key success factors (parental occupation, academic performance) offers a methodological example for feature importance analysis. Its emphasis on user accessibility and satisfaction supports the rationale for Odin's engagement and retention design."
  directly_justifies:
    - "Data mining techniques like decision trees and clustering can systematically evaluate a high volume of applications."
    - "An online system is critical for managing a large influx of applications and improving accessibility."
    - "User satisfaction and success rates are higher with a digital, data-driven system compared to traditional methods."
  limits:
    - "Focuses on scholarship selection, not personal finance management; direct applicability to spending behavior is limited."
    - "The evaluation metrics (accuracy, precision) are tied to classification tasks and may not fully capture the nuance of financial behavior." [unacknowledged]
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to 'Existing Systems & Gaps' (topics 4.A, 4.B) because it directly addresses the operational challenges of a manual system handling a massive application surge. It was also flagged as relevant to 'System Evaluation' (12.A, 12.B) due to its explicit use of quantitative metrics to evaluate algorithmic performance. Relevance to 'Behavioral Profiling & Classification' (5.A, 5.C) was assessed as contextual/medium, as the clustering and classification approach is methodologically similar to profiling but applied to scholarship applicants rather than financial behavior. The domains of 'Expense Categorization', 'Spending Forecasting', 'Budget Recommendation', 'Anomaly Detection', 'Data Privacy & User Trust', 'User Retention & Engagement', and 'Savings & Debt Management' were considered and rejected due to the paper's focus on scholarship administration, which provides no direct insights or citations for these personal finance areas. Overall, the paper's relevance to Odin is primarily methodological and evaluative, providing a strong example of system evaluation and gap identification, rather than providing domain-specific financial behavior insights."
limitations:
  - "The study is specific to scholarship programs, not personal finance management, limiting the generalizability of its findings."
  - "The evaluation is based on a single case study (BRO-Ed scholarship), lacking cross-program validation." [unacknowledged]
  - "The long-term impact on user retention and engagement beyond initial application is not assessed." [unacknowledged]
  - "The paper does not address the cold-start problem or other dynamic aspects of the system." [unacknowledged]
remember_this:
  - "Manual review of 34,426 applications is inefficient and error-prone."
  - "Decision trees and clustering can automate and improve selection accuracy."
  - "Online systems increase accessibility and user satisfaction significantly."
  - "num: The online system achieved a 31% higher success rate than traditional methods."
```
---

## Paper 14: Blancaflor et al_summarized.md

**Source File:** `Blancaflor et al_summarized.md`

```yaml
paper_id: 10.1145/3698062.3698088
designation: local-algorithm-specific
title: Exploring Machine Learning for Credit Card Fraud Detection from a Philippine Perspective
authors: Blancaflor, E.; Asuncion, K. D.; Reyes, H. J.; Verzosa, M.
year: 2024
venue: 2024 The 6th World Symposium on Software Engineering (WSSE)
odin_topics:
  - 8.A
  - 8.B
tldr: Examines machine learning techniques for credit card fraud detection tailored to the Philippine context, emphasizing SVM and ANN models.
problem_and_motivation: Credit card fraud in the Philippines has surged 21% since the pandemic, yet traditional fraud prevention systems are inadequate for securing e-commerce networks. There is a pressing need to evaluate and adapt machine learning models to the country's unique economic, technological, and social milieu to enhance financial security.
approach:
  - Reviews existing literature on fraud detection systems (FDS) and their limitations, such as imbalanced data and concept drift.
  - Assesses the efficacy of machine learning models including Logistic Regression, k-NN, Naïve Bayes, SVM, and ANN.
  - Compares the performance of ANN and Logistic Regression enhanced with Genetic Algorithm and SMOTE.
  - Evaluates models using metrics like accuracy, sensitivity, specificity, precision, Matthews Correlation Coefficient, and balanced classification rate.
  - Contextualizes findings within the Philippine financial sector, referencing local fraud cases and regulatory responses.
findings:
  - num: Credit card fraud in the Philippines increased by 21% since the COVID-19 outbreak.
  - num: Online fraud cost Filipino consumers over P540 million in 2021 alone.
  - num: ANN-SMOTE demonstrated the best performance in accuracy, precision, recall, and F1-score for fraud detection.
  - num: Logistic regression achieved an accuracy of 54.86%, while k-NN and Naïve Bayes achieved 97.69% and 97.92% respectively.
  - SVM shows promise for fraud detection, with potential for improved performance through meta-learning.
  - Machine learning models offer superior pattern detection and scalability, making them the future of fraud detection despite explainability trade-offs.
key_figures_tables:
  - Figure 1: Comparative performance of ANN and LR with GA/SMOTE enhancements → ANN-SMOTE outperforms all other models on key metrics.
  - Table 1: Evaluation of ML models for credit card fraud detection → Highlights accuracy and improvement strategies for each model.
key_equations:
  - equation: "MCC = (TP×TN - FP×FN) / √((TP+FP)(TP+FN)(TN+FP)(TN+FN))"
    explanation: Balanced measure for binary classification with imbalanced classes.
  - equation: "BCR = (Sensitivity + Specificity) / 2"
    explanation: Average recall or balanced accuracy for skewed datasets.
  - equation: "f(x) = sgn(x.w) + b"
    explanation: Decision function of SVM for binary classification.
definitions:
  - term: MCC
    definition: Matthews Correlation Coefficient, a balanced metric for binary classification.
  - term: BCR
    definition: Balanced Classification Rate, the average of sensitivity and specificity.
  - term: SMOTE
    definition: Synthetic Minority Over-sampling Technique, used to address imbalanced data.
  - term: FPS
    definition: Fraud Prevention System, a system designed to prevent fraudulent transactions.
  - term: FDS
    definition: Fraud Detection System, a system designed to detect fraudulent transactions.
critical_citations:
  - "[Awoyemi et al., 2017] — Comparative analysis of ML techniques for credit card fraud detection."
  - "[Abdallah et al., 2016] — Survey of fraud detection systems and their limitations."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly addresses fraud detection, a core anomaly detection application for Odin.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Reviews and evaluates algorithms (SVM, ANN) applicable to spending data anomaly detection.
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Provides context on the Philippine digital economy, which includes young professionals.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: low
      justification: Mentions the Philippine economic and social milieu but does not detail specific practices.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Briefly discusses existing fraud prevention systems but focuses on security, not personal finance management.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Discusses data security and privacy concerns in the context of fraud detection.
  contribution: This paper provides a foundational review of machine learning models for fraud detection, which directly informs Odin's Anomaly Detection module (8.A, 8.B). The comparative analysis of SVM and ANN with techniques like SMOTE offers a benchmark for algorithm selection. The findings on accuracy and performance metrics (MCC, BCR) guide the evaluation framework for Odin's detection capabilities. The emphasis on the Philippine context provides justification for tailoring anomaly detection algorithms to local spending patterns.
  directly_justifies:
    - "Machine learning models offer superior pattern detection for identifying fraudulent transactions in spending data."
    - "Support Vector Machines and Artificial Neural Networks are effective for binary classification of fraudulent and non-fraudulent patterns."
    - "SMOTE and other sampling techniques are crucial for handling imbalanced datasets common in anomaly detection."
    - "The trade-off between model explainability and accuracy must be considered when deploying fraud detection systems."
  limits:
    - "The paper is a literature review and does not present new empirical results from a Philippine dataset."
    - "The study does not specify the demographic profile (e.g., young professionals) of the fraud victims."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to the Anomaly Detection domain (topics 8.A and 8.B) because it directly evaluates ML algorithms for detecting credit card fraud, which is a key application of anomaly detection in PFMS. It was also flagged as medium relevance to Data Privacy & User Trust (10.A) due to its discussion of security and contextual for Filipino Cultural Context (1.A, 2.A) as it references the Philippine economic setting. Domains like Expense Categorization, Spending Forecasting, and Budget Recommendation were considered and rejected because the paper does not address spending patterns, income allocation, or financial planning. The overall relevance to Odin is primarily for its algorithmic insights into anomaly detection, particularly the choice of ML models and handling of imbalanced data.
limitations:
  - "The study is a literature review and does not include primary data collection or experimentation on Philippine fraud cases. [unacknowledged]"
  - "The comparison of model performance (e.g., Table 1) aggregates results from different studies, which may not be directly comparable due to varying datasets. [unacknowledged]"
  - "The paper does not address the cold-start problem for anomaly detection when user data is sparse. [unacknowledged]"
remember_this:
  - "Credit card fraud in the Philippines increased by 21% since the pandemic."
  - "ANN with SMOTE outperformed other models in detecting fraudulent transactions."
  - "Machine learning models are the future of fraud detection despite accuracy-explainability trade-offs."
  - "Traditional fraud prevention systems are inadequate for securing e-commerce networks."
```
---

## Paper 15: Laspinas & Murcia_summarized.md

**Source File:** `Laspinas & Murcia_summarized.md`

```yaml
paper_id: 10.5281/zenodo.10049652
designation: local-algorithm-specific
title: Machine Learning Approaches in Classifying Income Levels
authors: Laspiñas, E. L.; Murcia, J. V. B.
year: 2024
venue: TWIST
odin_topics:
  - 12.A
  - 12.B
  - 5.C
tldr: A comparison of six machine learning classifiers for income prediction shows RandomForest and Random Tree achieve 98% accuracy, underscoring the importance of model selection and tuning.
problem_and_motivation: Traditional econometric models fail to capture complex income dynamics due to linear assumptions. Machine learning offers a more sophisticated, data-driven approach. There is a research gap in applying ML to predict adult income levels accurately.
approach:
  - Used the Adult Income Prediction dataset with 16,281 instances and 13 attributes.
  - Applied six classifiers: Logistic, J48, RandomForest, Random Tree, IBk (k-NN), and NaiveBayes.
  - Evaluated using 10-fold cross-validation and metrics TP rate, FP rate, precision, recall, and F-measure.
  - Tuned J48 confidence factor (0.25, 0.50, 0.75) and k-NN k values (3,5,7,9).
  - Used Weka for implementation and feature selection via InfoGainAttributeEval.
findings:
  - "num: RandomForest and Random Tree achieved 98.35% and 98.37% accuracy, respectively."
  - "num: J48 accuracy improved from 87.21% to 90.84% as confidence increased from 0.25 to 0.75."
  - "num: k-NN accuracy decreased from 89.11% (k=3) to 85.74% (k=9)."
  - "num: NaiveBayes had the lowest accuracy at 82.24%."
  - RandomForest and Random Tree had F-measures of 0.983 and 0.984, indicating superior balance.
  - Feature selection identified 'Relationship' as most predictive (info gain 0.16575).
  - Ensemble methods reduce overfitting and generalize well.
key_figures_tables:
  - "Table 2: Classification accuracy for six classifiers → RandomForest and Random Tree highest at ~98%."
  - "Table 3: Performance metrics (TP, FP, precision, recall, F-measure) → RandomForest and Random Tree have highest F-measure."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: ML
    definition: Machine learning, a subset of AI enabling systems to learn from data.
  - term: k-NN
    definition: k-nearest neighbors, a classification algorithm based on majority vote of nearest neighbors.
  - term: J48
    definition: An implementation of the C4.5 decision tree algorithm in Weka.
  - term: TP rate
    definition: True positive rate, proportion of actual positives correctly identified.
  - term: FP rate
    definition: False positive rate, proportion of negatives incorrectly classified as positive.
  - term: Precision
    definition: Proportion of positive predictions that are correct.
  - term: Recall
    definition: Same as TP rate, proportion of actual positives identified.
  - term: F-measure
    definition: Harmonic mean of precision and recall.
critical_citations:
  - "[Athey, 2018] — Machine learning enhances economic analysis."
  - "[Delen et al., 2010] — ML can detect non-linear income indicators."
  - "[Atkinson et al., 2011] — Econometric models have limitations in income dynamics."
relevance:
  topics:
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides cross-validation and performance metrics applicable to evaluating Odin's modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Directly compares classifier performance and tuning, informing algorithm selection for Odin.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Income classification is a related predictive task but not specifically behavioral profiles.
  contribution: This paper's comparative evaluation of classifiers can guide Odin's selection of algorithms for spending forecasting and anomaly detection. Its emphasis on hyperparameter tuning (confidence factor, k) helps avoid overfitting in Odin's predictive modules. The use of 10-fold cross-validation and multiple performance metrics provides a robust template for evaluating Odin's system components. Additionally, the finding that ensemble methods (RandomForest) perform best supports their adoption for high-stakes predictions in personal finance.
  directly_justifies:
    - RandomForest and Random Tree classifiers achieve high accuracy and are suitable for income or spending prediction tasks.
    - Hyperparameter tuning significantly affects classifier performance, so Odin should tune its models.
    - Cross-validation with multiple metrics ensures reliable model evaluation.
  limits:
    - Dataset is from U.S. census, not Filipino, so generalizability to Filipino young professionals is limited. [unacknowledged]
    - Only binary income classification, not multi-level or continuous.
  mapping_rationale: The systematic scan across all 12 functional domains and their associated topic codes identified relevance in the System Evaluation domain (12.A, 12.B) due to the paper's comparative evaluation of classifiers and hyperparameter tuning, and to a lesser degree in Behavioral Profiling (5.C) as income classification is a related predictive task. The paper does not address Filipino cultural context, expense categorization, existing systems, forecasting, budgeting, anomaly detection, mobile design, privacy, retention, or savings/debt, so those topics were rejected. Borderline cases: the paper's methodology could inform spending forecasting (6.A) but it does not use spending data, so we classified 6.A as not selected; 5.C is included as low because classification approaches are relevant but not specific to financial behavior. Overall, the paper is most relevant for guiding the evaluation and selection of machine learning algorithms within Odin's predictive modules.
limitations:
  - Uses a single U.S.-based dataset, limiting applicability to Philippine context. [unacknowledged]
  - Only binary classification, not multi-class or regression.
  - Does not address temporal dynamics or spending behavior.
remember_this:
  - RandomForest and Random Tree outperform other classifiers with over 98% accuracy.
  - Hyperparameter tuning can improve J48 accuracy by over 3 percentage points.
  - Increasing k in k-NN reduces classification accuracy for this dataset.
  - Ensemble methods reduce overfitting and are recommended for predictive tasks.
  - 10-fold cross-validation provides robust performance estimates.
```
---

## Paper 16: Salvador_summarized.md

**Source File:** `Salvador_summarized.md`

```yaml
paper_id: 3f7a1c8e-9b2d-5a4f-8e7c-1d2f3a4b5c6d
designation: local-algorithm-specific
title: Use of Boosting Algorithms in Household-Level Poverty Measurement: A Machine Learning Approach to Predict and Classify Household Wealth Quintiles in the Philippines
authors: Salvador, E. L. V.
year: 2024
venue: Unknown
odin_topics:
  - "5.A"
  - "6.A"
tldr: CatBoost achieved 90.93% accuracy in predicting Philippine household wealth quintiles, outperforming XGBoost, GBM, LightGBM, and AdaBoost using DHS data.
problem_and_motivation: Conventional econometric poverty measurements oversimplify poverty's multidimensional nature by relying on pre-selected features like income. Accurate poverty data is crucial for effective policy interventions, yet a gap exists in applying diverse machine learning methods to extensive Philippine household datasets.
approach:
  - Data from the 2022 Philippine Demographic and Health Survey was cleaned, reducing features from 2,099 to 396 and households from 30,372 to 20,679.
  - The dataset was split into 80% training and 20% testing, with 10% of training used for validation and hyperparameter tuning via manual and grid search.
  - Five boosting algorithms (AdaBoost, CatBoost, GBM, LightGBM, XGBoost) were implemented to classify wealth into five quintiles.
  - Feature selection using SelectFromModel identified 66 key features, with multicollinearity checked via Pearson correlation.
  - SMOTE addressed class imbalance, and models were evaluated on accuracy, precision, recall, F1-score, AUC-ROC, and computational efficiency metrics.
findings:
  - "num: CatBoost achieved the highest accuracy at 90.93%, followed by XGBoost (89.41%), GBM (89.05%), and LightGBM (88.52%)."
  - "num: AdaBoost performed significantly lower across all metrics, with an accuracy of 80.39% and F1-score of 80.15%."
  - CatBoost, GBM, LightGBM, and XGBoost achieved near-perfect AUC-ROC scores (0.98-1.00) for most wealth classes, effectively distinguishing poverty levels.
  - AdaBoost showed lower discriminative ability, especially for the "Poorest" and "Poorer" classes with AUC scores of 0.90 and 0.73 respectively.
  - "num: LightGBM and XGBoost exhibited a strong balance of performance and computational efficiency, with training times of 2.17 and 2.58 seconds and model sizes of 2.50 MB and 3.10 MB."
  - "num: CatBoost had the longest training time (69.29 seconds) and largest model size (30.50 MB) but was the most efficient during testing (0.01 seconds)."
  - AdaBoost had the shortest training time (4.48 seconds) but the longest testing time (0.23 seconds).
  - Feature selection highlighted household assets (e.g., television, refrigerator, vehicle) and housing characteristics as the most important predictors.
key_figures_tables:
  - "Figure 1: Distribution of missing values across features with threshold of 3,050 → Features with missing values exceeding the threshold were removed."
  - "Table 1: Description of 36 key features selected for poverty prediction → Key predictors include assets, housing materials, and utilities."
  - "Table 3: Performance metrics (Accuracy, Precision, Recall, F1) for five boosting models → CatBoost consistently outperformed all models across all metrics."
  - "Table 4: AUC-ROC scores per wealth class for each model → CatBoost, GBM, LightGBM, and XGBoost achieved near-perfect scores for most classes."
  - "Table 5: Computational efficacy (Training time, Testing time, Model size) → LightGBM and XGBoost offer the best balance of speed and size."
key_equations:
  - equation: "Accuracy = (TP + TN) / (TP + TN + FP + FN)"
    explanation: "Calculates overall correct predictions proportion."
  - equation: "Precision = TP / (TP + FP)"
    explanation: "Proportion of correct positive predictions."
  - equation: "Recall = TP / (TP + FN)"
    explanation: "Proportion of actual positives correctly identified."
  - equation: "F1 Score = 2 * (Precision * Recall) / (Precision + Recall)"
    explanation: "Harmonic mean of precision and recall."
definitions:
  - term: "AdaBoost"
    definition: "Adaptive Boosting, an ensemble method that combines weak learners sequentially."
  - term: "CatBoost"
    definition: "Gradient boosting algorithm designed to handle categorical features efficiently."
  - term: "DHS"
    definition: "Demographic and Health Survey, a nationally representative household survey."
  - term: "GBM"
    definition: "Gradient Boosting Machine, an ensemble method building models sequentially."
  - term: "LightGBM"
    definition: "Light Gradient Boosting Machine, a fast, distributed gradient boosting framework."
  - term: "SMOTE"
    definition: "Synthetic Minority Over-sampling Technique, addresses class imbalance by creating synthetic samples."
  - term: "XGBoost"
    definition: "Extreme Gradient Boosting, a scalable and efficient gradient boosting implementation."
critical_citations:
  - "[Li et al., 2022] — Identified underutilization of boosting in poverty prediction."
  - "[Tingzon et al., 2019] — Used machine learning with geospatial data for Philippine poverty mapping."
  - "[Bentéjac et al., 2021] — Comparative analysis shows boosting algorithms have improved speed and accuracy."
  - "[Alkire et al., 2015] — Supports multidimensional nature of poverty."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "low"
      justification: "Paper focuses on general household wealth classification, not financial behavior profiles."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "low"
      justification: "Demonstrates use of boosting algorithms for classification, a technique transferable to spending prediction."
  contribution: "This paper's comparative evaluation of boosting algorithms (CatBoost, XGBoost) for household classification provides a methodological reference for Odin's predictive modules. The use of SMOTE for class imbalance and feature selection techniques (SelectFromModel) can inform Odin's approach to handling sparse user data. The study's consideration of computational efficiency (training/testing time, model size) is directly relevant to Odin's mobile-first deployment constraints. However, the paper's application to poverty measurement, not personal finance, limits its direct applicability to Odin's forecasting or behavioral profiling tasks."
  directly_justifies:
    - "Boosting algorithms like CatBoost and XGBoost demonstrate high accuracy in classification tasks with structured data."
    - "Computational efficiency metrics are critical for selecting models for mobile-first applications."
    - "Feature selection and SMOTE can improve model performance on imbalanced datasets."
  limits:
    - "Paper predicts static wealth quintiles, not dynamic spending patterns or financial behaviors."
    - "The model is trained on DHS survey data, which differs significantly from app-generated transaction data."
    - "Analysis is for poverty classification, not regression-based forecasting of spending amounts."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. Domains related to Filipino cultural context (2.A-2.D), expense categorization (3.A-3.C), and user behavioral profiling (5.A-5.C) were considered. The paper was flagged as relevant for topic 5.A (Financial Behavioral Profiles) and 6.A (Predictive Modeling) due to its use of machine learning classification algorithms, but assigned a 'low' relevance because it addresses general poverty classification, not financial behavior. Domains such as budgeting (7.A-7.D), anomaly detection (8.A-8.C), and mobile-first design (9.A-9.B) were rejected as the paper does not address these areas. The overall relevance to Odin is contextual, providing methodological insights for model selection and evaluation rather than domain-specific knowledge."
limitations:
  - "Reliance on DHS data limits generalizability to other contexts."
  - "Further validation using alternative datasets is needed."
  - "Manual removal of interview-related features may introduce bias."
  - "Hyperparameter tuning was limited to manual and grid search."
  - "No error analysis for misclassifications per wealth class."
remember_this:
  - "CatBoost achieved the highest accuracy at 90.93%."
  - "LightGBM and XGBoost offer the best balance of speed and size."
  - "CatBoost had the longest training time but fastest testing."
  - "AdaBoost performed significantly worse than other boosting algorithms."
  - "Feature selection identified assets and housing as key poverty predictors."
```
---

## Paper 17: Apus et al_summarized.md

**Source File:** `Apus et al_summarized.md`

```yaml
paper_id: d2a3b4c5-6e7f-48a9-b0c1-d2e3f4a5b6c7
designation: local-algorithm-specific
title: Predicting the Filipino Household Income Using Naive Bayes Classification Algorithm
authors: Apus, J.O.; Mantalaba, K.D.V.; Mackno, A.J.B.; Bokingkito, P.B.
year: 2023
venue: International Journal of Computing and Digital Systems
odin_topics:
  - 3.A
  - 5.A
  - 5.C
  - 6.A
  - 12.B
tldr: Predicts Filipino household income class using Naive Bayes with expenditure and income features from FIES data, achieving 93% accuracy with bagging.
problem_and_motivation: Philippine poverty reduction requires accurate identification of vulnerable households. Existing predictive models rely mainly on socio-demographic variables, neglecting expenditure and income data. This gap limits the effectiveness of targeted interventions.
approach:
  - Used the 2018 FIES dataset with 41,545 households and 60 features, cleaning missing values using mode for categorical and mean/median for numeric.
  - Selected 13 features using univariate chi-squared feature selection based on correlation with income class.
  - Implemented Naive Bayes classifier with bagging and boosting ensemble techniques using Python's sklearn.
  - Split data 80-20 for training and testing; evaluated using confusion matrix, precision, recall, F1-score, and accuracy.
  - Compared bagging and boosting ensemble methods to determine best performance.
findings:
  - "num: Bagging ensemble achieved 93% accuracy, while boosting achieved 89% accuracy."
  - "num: Bagging model had precision 0.93, recall 0.94, and F1-score 0.94 weighted mean."
  - "num: Boosting model had precision 0.90, recall 0.93, F1-score 0.91."
  - Poor income class had the most true positives; rich class had the least.
  - Models with accuracy above 80% are considered good, indicating Naive Bayes is effective for this task.
key_figures_tables:
  - "Table III: Selected features with chi-squared scores → top features include total food and transportation expenditure."
  - "Figure 3: Confusion matrix for bagging model → shows strong diagonal performance across income classes."
  - "Table VI: Classification report for bagging ensemble → weighted averages above 0.93 for precision, recall, F1."
key_equations:
  - equation: "Precision = TP/(TP+FP)"
    explanation: "Measures accuracy of positive predictions."
  - equation: "Recall = TP/(TP+FN)"
    explanation: "Measures proportion of actual positives correctly identified."
  - equation: "F1 = 2*(Precision*Recall)/(Precision+Recall)"
    explanation: "Harmonic mean of precision and recall."
  - equation: "Accuracy = (TP+TN)/(P+N)"
    explanation: "Overall proportion of correct predictions."
definitions:
  - term: "FIES"
    definition: "Family Income and Expenditure Survey conducted by the Philippine Statistics Authority."
  - term: "PSA"
    definition: "Philippine Statistics Authority, the national statistical agency."
  - term: "Bagging"
    definition: "Bootstrap aggregating; an ensemble method to reduce variance."
  - term: "Boosting"
    definition: "An ensemble method that iteratively adjusts weights of misclassified instances."
critical_citations:
  - "None."
relevance:
  topics:
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "medium"
      justification: "Uses expenditure categories as predictive features, relevant to categorization design."
    - code: "5.A"
      name: "Financial Behavioral Profiles"
      relevance: "medium"
      justification: "Classifies households into income classes, a form of financial profile."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Directly applies a classification algorithm to financial data, relevant to profile classification module."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "low"
      justification: "Predicts income class, but not spending forecasting; general predictive modeling context."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Provides evaluation metrics and comparison of ensembles, useful for algorithm evaluation."
  contribution: "This paper's use of expenditure features for classification can inform Odin's expense categorization module by highlighting which spending categories are most discriminative of income class. The Naive Bayes algorithm and ensemble evaluation provide a baseline for Odin's behavioral profiling module. The feature selection method (chi-squared) can guide Odin's feature engineering for user profiles. The high accuracy suggests that expenditure data alone can predict financial class, which can be used for cold-start profiling in Odin."
  directly_justifies:
    - "Expenditure categories such as food and transportation are strong predictors of income class."
    - "Naive Bayes with bagging achieves 93% accuracy in classifying Filipino household income."
    - "Feature selection using chi-squared can identify relevant expenditure features."
    - "Models with accuracy above 80% are considered effective for classification tasks."
  limits:
    - "The model is trained on aggregated survey data, not individual spending transactions, limiting applicability to personal finance systems [unacknowledged]."
    - "Only uses 13 features; other relevant financial behaviors may be omitted [unacknowledged]."
    - "The dataset is from 2018; spending patterns may have changed [unacknowledged]."
  mapping_rationale: "Systematic scan of all 12 functional domains and their associated topic codes flagged the Expense Categorization (3.A, medium), Behavioral Profiling (5.A medium, 5.C high), Predictive Modeling (6.A low), and System Evaluation (12.B medium) domains as relevant. The paper's focus on classifying income using expenditure features directly maps to 5.C (classification approach) and 3.A (use of expense categories). The borderline case of predictive modeling was considered: although it is predictive, it does not forecast sequential spending, so 6.A is low. Domains such as Budget Recommendation, Anomaly Detection, Mobile-First, Data Privacy, and Retention were rejected as the paper does not address them. Overall, the paper provides moderate to high relevance for Odin's profiling and classification modules."
limitations:
  - "Only used 13 features; additional parameters like region and family size could improve accuracy."
  - "Explored only Naive Bayes; other algorithms may yield better performance."
  - "The study does not address real-time application or integration into a PFMS."
remember_this:
  - "Bagging Naive Bayes achieved 93% accuracy for income class prediction."
  - "Food and transportation expenditures are top predictors of income class."
  - "Naive Bayes is simple, fast, and robust to missing data."
  - "Feature selection using chi-squared improves model performance."
  - "Expenditure data alone can effectively classify Filipino household income."
```
---

## Paper 18: Yuan et al_summarized.md

**Source File:** `Yuan et al_summarized.md`

```yaml
paper_id: "10.1109/ACCESS.2023.3338705"
designation: "local-algorithm-specific"
title: "User Cold Start Problem in Recommendation Systems: A Systematic Review"
authors: "Yuan, H.; Hernandez, A. A."
year: 2023
venue: "IEEE Access"
odin_topics:
  - "5.A"
  - "5.B"
  - "5.C"
  - "12.A"
  - "12.B"
tldr: "A systematic review of literature from 2016 to 2023 categorizes approaches to the user cold start problem into data-driven and method-driven techniques."
problem_and_motivation: "Accurate recommendations for new users are hindered by a lack of historical data. This limits the utility and user experience of recommender systems. Existing systematic reviews are outdated or do not distinguish between user and item cold start problems."
approach:
  - "A systematic literature review was conducted following established guidelines for selecting and analyzing scientific papers."
  - "A search of IEEE, ACM, and Web of Science databases yielded 45 relevant papers published from January 2016 to April 2023."
  - "The study categorizes solution approaches into two main groups: data-driven technologies and approach-driven technologies."
  - "Data-driven techniques utilize additional user information like cross-domain data, social network data, and demographic data."
  - "Approach-driven techniques are further subdivided into five categories: meta-learning, deep learning, matrix factorization, improved collaborative filtering, and improved content-based approaches."
  - "The paper also analyzes the primary evaluation criteria used in the reviewed studies."
  - "Key future research directions are outlined, including collecting additional information and multi-task learning."
findings:
  - "num: 45 research papers from 35 venues were selected for in-depth analysis."
  - "num: The quantity of relevant literature peaked in 2020 with 11 papers."
  - "The user cold start problem has been a growing research area from 2016 to 2023."
  - "IEEE Access and ACM Transactions on Information Systems are the most common venues, each with 4 papers."
  - "Method-driven strategies are categorized into five main approaches: meta-learning, deep learning, matrix factorization, improved collaborative filtering, and improved content-based."
  - "Data-driven strategies primarily use cross-domain data, social network data, and user demographic data to build better user profiles."
  - "Commonly used evaluation metrics include Rating Prediction (RMSE, MAE), Classification Accuracy (AUC, Recall), and Ranking Metrics (NDCG@K, Hit@K)."
  - "Ranking Metrics, especially NDCG, are increasingly popular for evaluating user cold start solutions."
  - "Recommendation methods for films, music, and books are the most researched areas due to the availability of public datasets."
  - "Deep learning and graph neural networks are increasingly applied to solve the user cold start problem."
key_figures_tables:
  - "Figure 1: Flow diagram of the systematic literature review process → The seven steps for selecting and analyzing papers."
  - "Figure 2: The paper selection process → From 1480 initial papers to 45 final papers selected for the review."
  - "Figure 3: Number of papers per year → Shows a peak in publications on user cold start in 2020."
  - "Figure 7: Classification of user cold start recommendation strategies → Diagrams the data-driven and method-driven categories."
  - "Table 8: Classification of approaches for alleviating the user cold start problem → Provides a high-level summary of both main categories and their sub-approaches."
key_equations:
  - equation: "Y_s = W Y_t"
    explanation: "A general formulation for similarity-based models using a similarity matrix W."
definitions:
  - term: "User Cold Start Problem"
    definition: "The challenge of making accurate recommendations for new users due to a lack of historical interaction data."
  - term: "Item Cold Start Problem"
    definition: "The challenge of recommending newly added items for which no user rating or interaction history exists."
  - term: "Data-Driven Techniques"
    definition: "Approaches that solve the cold start problem by utilizing additional user or item information from various sources."
  - term: "Approach-Driven Techniques"
    definition: "Approaches that solve the cold start problem by proposing new algorithms or modifying existing ones."
  - term: "Meta-Learning"
    definition: "A machine learning approach that enables models to quickly adapt to new tasks with limited data, useful for new users."
  - term: "NDCG@K"
    definition: "Normalized Discounted Cumulative Gain, a ranking metric used to evaluate the quality of a top-K recommendation list."
critical_citations:
  - "[Panda & Ray, 2022] — A recent systematic review on cold-start mitigation strategies."
  - "[Son, 2016] — A comparative review of three approaches for the new user cold-start problem."
  - "[Abdullah et al., 2021] — A survey focused on eliciting auxiliary information for cold-start users."
  - "[Camacho & Alves-Souza, 2018] — A systematic review on using social network data to alleviate cold starts."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "contextual"
      justification: "Discusses user profiling as part of building user models to address cold starts."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "high"
      justification: "The paper is a systematic review directly addressing the user cold-start problem, which is the core of this topic."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "Reviews classification approaches like clustering and meta-learning, which are relevant for profile classification."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Dedicates a section to reviewing evaluation criteria (e.g., NDCG, RMSE) used in the literature."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "The review analyzes algorithmic solutions and their performance as measured by common metrics."
  contribution: "This systematic review provides Odin with a comprehensive taxonomy of user cold start solutions, categorizing them into data-driven and approach-driven methods. The review's analysis of evaluation metrics informs the design of robust testing protocols for Odin's behavioral profiling and recommendation modules. The categorization of deep learning, meta-learning, and other algorithmic approaches guides the selection of appropriate techniques for cold-start user modeling. The paper's insights into future research directions, like multi-task learning, can inspire advanced features for Odin. Overall, it serves as a foundational reference for Odin's approach to new user onboarding and initial budget recommendations."
  directly_justifies:
    - "The user cold start problem occurs when a new user cannot be appropriately suggested due to a lack of detailed preference information."
    - "Solving the user cold start problem is essential for the large-scale utility of recommender systems."
    - "Approaches to solve the user cold start problem can be categorized as data-driven or method-driven strategies."
  limits:
    - "The review is limited to a systematic analysis of existing literature and does not include an experimental validation or comparison of the reviewed methods."
    - "The study focuses on the user cold start problem and does not analyze solutions for item cold starts, which may have different optimal strategies."
  mapping_rationale: "In the systematic scan, the domains of 'Behavioral Profiling & Classification' and 'System Evaluation' were flagged as relevant. Under the 'Behavioral Profiling & Classification' domain, topic 5.B (Profile Dynamics and the Cold-Start Problem) was assigned high relevance because the paper is a comprehensive review directly focused on this issue. Topic 5.A (Financial Behavioral Profiles) was rated contextual as user profiling is a component of many reviewed solutions, but the paper does not specifically address financial profiles. Topic 5.C (Classification Approaches) was assigned medium relevance, as the review discusses various classification and learning methods used to build profiles. Under the 'System Evaluation' domain, topics 12.A (Evaluation Frameworks) and 12.B (Evaluation of Algorithmic Modules) were rated medium, as the paper provides a systematic analysis of evaluation metrics used in the literature. All other domains were considered and rejected. The 'Expense Categorization' domain was rejected because the paper does not discuss categorization frameworks. 'Spending Forecasting' and 'Budget Recommendation' were rejected as the paper focuses on user identification, not financial prediction. 'Anomaly Detection' was not relevant as the paper does not discuss identifying outliers in spending. In summary, while not directly about finance, the paper's structured review of cold start solutions and evaluation metrics is highly relevant for Odin's initial user modeling and module benchmarking."
limitations:
  - "No experimental validation was performed to compare the effectiveness of the different methods reviewed. [unacknowledged]"
  - "The authors acknowledge that the review is limited to a systematic literature review of 45 articles, which, while comprehensive, may not include all relevant studies."
  - "The paper notes that it does not address the item cold start problem, which is a distinct but related issue in recommender systems."
remember_this:
  - "User cold start solutions are categorized into data-driven and method-driven strategies."
  - "Data-driven approaches use cross-domain, social, and demographic user data."
  - "Method-driven approaches include meta-learning, deep learning, and improved collaborative filtering."
  - "num: 45 papers from 2016-2023 were systematically reviewed on this topic."
  - "Ranking metrics like NDCG are the most prevalent for evaluating cold start performance."
```
---

## Paper 19: Gumasing et al_summarized.md

**Source File:** `Gumasing et al_summarized.md`

```yaml
paper_id: 10.1016/j.heliyon.2023.e20644
designation: local-algorithm-specific
title: A machine learning ensemble approach to predicting factors affecting the intention and usage behavior towards online groceries applications in the Philippines
authors: Gumasing, M.J.J.; Ong, A.K.S.; Sy, M.A.P.C.; Prasetyo, Y.T.; Persada, S.F.
year: 2023
venue: Heliyon
odin_topics:
  - 1.A
  - 1.B
  - 2.A
  - 2.B
  - 2.D
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 11.A
  - 11.B
  - 12.A
  - 12.B
  - 12.C
tldr: Filipino consumers' intention and usage of online grocery apps during COVID-19 are driven by perceived benefits, vulnerability, behavioral intention, performance expectancy, and severity.
problem_and_motivation: Existing studies on online grocery acceptance show inconsistent results, often lacking a holistic measure of behavioral intention when health concerns are present. No prior study in the Philippines has established a comprehensive model for online grocery acceptance during a pandemic.
approach:
  - A conceptual framework integrating UTAUT2 and Protection Motivation Theory (PMT) was developed.
  - A 67-item survey was administered to 373 Filipino online grocery users via convenience sampling from August to December 2021.
  - Data preprocessing included correlation analysis, aggregation, and normalization.
  - A Random Forest Classifier was optimized across 6,400 runs with varying parameters and training-test splits.
  - An Artificial Neural Network (ANN) was optimized with Tanh/Softmax activations and Adam optimizer at 150 epochs.
findings:
  - The ANN achieved a high average accuracy of 96.63% with no overfitting.
  - The Random Forest Classifier achieved a high average accuracy of 96% with 0.00 standard deviation.
  - num: 96.63% accuracy from ANN and 96% from Random Forest Classifier were consistent.
  - Perceived Benefit was the most significant factor, followed by Perceived Vulnerability and Behavioral Intention.
  - Performance Expectancy was a top factor, indicating efficiency and time savings are key drivers.
  - All ten constructs were found to be significant predictors of behavioral intention and usage.
key_figures_tables:
  - Figure 1: E-commerce growth rate by sector → Food/beverage grew 170.8% during the pandemic.
  - Figure 2: Conceptual framework → Integrated UTAUT2 and PMT with 12 hypotheses.
  - Figure 4: Decision tree from Random Forest → Perceived Benefit is the root node for usage behavior.
  - Figure 5: Optimum ANN model → Achieved 96.63% accuracy with Tanh/Softmax and Adam optimizer.
  - Table 6: Score of importance → Perceived Benefit is the most influential factor at 100% score.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: UTAUT2
    definition: Unified Theory of Acceptance and Use of Technology 2, a model for technology acceptance.
  - term: PMT
    definition: Protection Motivation Theory, a model for health-related behavior.
  - term: ANN
    definition: Artificial Neural Network, a supervised machine learning algorithm.
  - term: Random Forest Classifier
    definition: A classification tool using an ensemble of decision trees.
  - term: Perceived Benefit
    definition: Belief that a course of action reduces disease risk and leads to positive results.
critical_citations:
  - "[Venkatesh et al., 2012] — Introduced UTAUT2 and its core constructs."
  - "[Chuenyindee et al., 2022] — Justified integrating PMT for health-related technology acceptance."
  - "[Ong et al., 2022] — Demonstrated machine learning ensemble for behavioral prediction."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: The study directly surveys Filipino consumers, establishing baseline demographics.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Provides income and spending data on groceries, relevant to financial structure.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Addresses the shift to online grocery in the Philippines, a culturally driven behavior.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Mentions pandemic-induced changes in grocery spending patterns.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: medium
      justification: Directly relevant to Filipino spending behavior during the pandemic.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Predicts factors affecting consumer behavior, directly contributing to profile understanding.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: contextual
      justification: Provides a framework for understanding initial behavioral intention.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Uses machine learning classification to categorize behavioral predictors.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Employs predictive modeling (ANN and Random Forest) to forecast usage behavior.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: The modeling approach could be extended to forecasting spending.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Directly addresses behavioral intention and usage, key engagement metrics.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: contextual
      justification: The findings can inform design for retention (e.g., highlighting benefits).
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses a systematic methodological framework for evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Specifically evaluates the performance of ANN and Random Forest classifiers.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: contextual
      justification: The evaluation methodology is relevant but not directly about budget recommendations.
  contribution: This study provides a validated machine learning ensemble framework for predicting behavioral intention and usage in the context of online grocery applications. It directly justifies the use of ANN and Random Forest classifiers for Odin's behavioral profiling and prediction modules. The integration of UTAUT2 and PMT offers a robust theoretical foundation for understanding user motivation, which can inform engagement strategies. The identification of perceived benefit and vulnerability as top predictors can guide Odin's user onboarding and feature prioritization. The high accuracy of the models demonstrates the feasibility of using similar techniques for Odin's forecasting and classification tasks.
  directly_justifies:
    - "Machine learning ensembles can achieve high accuracy (>96%) in predicting consumer behavior."
    - "Perceived benefit and vulnerability are the most significant drivers of behavioral intention."
    - "UTAUT2 and PMT can be effectively integrated to model technology acceptance in a health context."
    - "Filipino consumers are highly receptive to online services, indicating a strong market for PFMS."
  limits:
    - "Respondents were predominantly from highly urbanized areas, limiting generalizability to rural populations."
    - "The study did not consider socio-economic factors for clustering, which could refine user segmentation."
    - "Data was collected during the COVID-19 pandemic, which may not reflect post-pandemic baseline behavior."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant for domains related to Filipino context (2.A, 2.D), behavioral profiling (5.A, 5.C), predictive modeling (6.A, 6.B), and system evaluation (12.B). The paper's focus on machine learning for prediction directly justifies high relevance for 5.C, 6.A, 12.A, and 12.B. The integration of UTAUT2 and PMT provides a strong framework relevant to 5.A and 5.B. The study's context of Filipino consumer behavior is directly applicable to 2.A and 2.D. Domains like 1.A, 1.B were considered relevant as they provide demographic and financial structure data, assigned medium relevance. Domains like expense categorization (3.A, 3.B), anomaly detection (8.A, 8.B), and savings/debt (13.A, 13.B) were rejected as the paper does not address these specific functionalities. The overall relevance is high, as the paper provides a validated methodological approach for predicting user behavior, which is central to Odin's core functions.
limitations:
  - "The majority of respondents reside in highly urbanized cities, affecting generalizability to rural consumers."
  - "Lack of consideration of socio-economic factors (e.g., income, employment) for customer segmentation."
  - "Data was collected during COVID-19 lockdowns, which may not reflect behavior under normal conditions."
remember_this:
  - "Perceived benefit was the most significant driver of online grocery usage behavior."
  - "The Artificial Neural Network achieved a high accuracy of 96.63% for predicting usage behavior."
  - "The Random Forest Classifier achieved a consistent 96% accuracy with zero standard deviation."
  - "Filipino consumers were highly receptive to online grocery during the COVID-19 pandemic."
```
---

## Paper 20: Ong  A. et al_summarized.md

**Source File:** `Ong  A. et al_summarized.md`

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
---

## Paper 21: Deselo & Agner_summarized.md

**Source File:** `Deselo & Agner_summarized.md`

```yaml
paper_id: 10.5539/ijef.v15n6p27
designation: local-algorithm-specific
title: Financial Inclusion and the Role of Financial Literacy in the Philippines
authors: Desello, J. M. U.; Agner, M. G. R.
year: 2023
venue: International Journal of Economics and Finance
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.D
  - 4.A
  - 4.B
  - 5.A
  - 10.A
tldr: Financial literacy positively drives financial inclusion in the Philippines, increasing account ownership and service use likelihood.
problem_and_motivation: Philippine-based studies linking financial literacy and financial inclusion via nationally representative surveys are scarce. This gap limits evidence-based policy design to bridge the financial inclusion gap and raise literacy levels.
approach:
  - Data from the BSP's 2019 Financial Inclusion Survey, n = 1,200 respondents.
  - Used a three-item financial literacy quiz covering inflation and interest rates.
  - Applied OLS and probit regression models with robust standard errors.
  - Proxied financial inclusion via account ownership and use of financial services.
  - Modeled account types (bank, e-money, cooperative, microfinance) and services (credit, investment, insurance) separately.
findings:
  - "num: A one-standard-deviation increase in financial literacy scores increased the likelihood of holding at least one account by 3.7 to 4.2 percentage points."
  - "num: A one-point increase in financial literacy scores improved the likelihood of availing of a financial service by 4.9 to 6.0 percentage points."
  - "num: Financial literacy increased the likelihood of holding a bank account by 2.1 percentage points."
  - Age, gender, employment, income above PHP 40,000, and being the main financial decision-maker positively correlate with financial inclusion.
  - Being unemployed and having low income (below PHP 10,000) negatively correlate with account ownership and service use.
  - Awareness of BSP programs positively influences account ownership and investment holdings.
  - The positive effect of financial literacy on financial inclusion is consistent with findings from Cambodia, Vietnam, Kenya, and Tanzania.
key_figures_tables:
  - "Table 1: Financial literacy and ownership of at least one account → Literacy increases likelihood by 3.7-4.2 percentage points."
  - "Table 2: Financial literacy and ownership of specific accounts → Positive effect only for bank accounts, increasing likelihood by 2.1 percentage points."
  - "Table 3: Financial literacy and availing of financial services → Literacy increases likelihood by 4.9-6.0 percentage points."
  - "Table 4: Financial literacy and specific services → Positive effect for account and investment ownership only."
key_equations:
  - equation: "FA_i = β_0 + β_1 FL_i + β_2 X_i + u_i"
    explanation: Models impact of literacy on account ownership.
  - equation: "FS_i = β_0 + β_1 FL_i + β_2 X_i + u_i"
    explanation: Models impact of literacy on service use.
definitions:
  - term: BSP
    definition: Bangko Sentral ng Pilipinas, the Philippine central bank.
  - term: FIS
    definition: Financial Inclusion Survey, a biennial BSP survey.
  - term: OLS
    definition: Ordinary Least Squares, a linear regression method.
  - term: Probit
    definition: A regression model for binary dependent variables.
critical_citations:
  - "[Morgan & Trinh, 2017] — Found literacy drives inclusion in Cambodia/Vietnam."
  - "[Fanta & Kingston, 2021] — Reported literacy strongly predicts inclusion in Kenya/Tanzania."
  - "[Grohmann & Menkhoff, 2020] — Defined financial inclusion levels."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Provides demographic data on financial inclusion drivers relevant to young professionals.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: low
      justification: Offers general income and employment data points.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Links literacy to account ownership and service use as behavioral outcomes.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Highlights role of household financial decision-making in the Filipino context.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: Mentions remittance flows, which are linked to seasonal and occasion-based spending.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Reviews existing financial inclusion literature in the Philippines.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Explicitly identifies the scarcity of national-level studies linking literacy and inclusion.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Literacy is a key determinant of financial behavior (account ownership, service use).
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Uses BSP survey data, implies governance and trust mechanisms.
  contribution: "This paper directly justifies Odin's financial literacy module by establishing that higher literacy significantly increases financial account ownership in the Philippines. It validates the inclusion of a financial education component within Odin's onboarding or user engagement features. The paper's findings support Odin's behavioral profiling efforts by identifying key demographic drivers of financial inclusion. It provides empirical grounding for Odin's targeting and personalization algorithms, especially for users with lower literacy levels. Finally, it underscores the need for Odin to bridge the gap identified in the Philippine financial inclusion landscape."
  directly_justifies:
    - "Financial literacy is a positive driver of financial inclusion in the Philippines."
    - "Account ownership and financial service use increase with higher financial literacy scores."
    - "Demographic factors such as age, gender, and income influence financial inclusion."
    - "Awareness of financial programs correlates with greater financial inclusion."
  limits:
    - "The financial literacy measure uses only three quiz items, potentially limiting its robustness."
    - "The data is from 2019, which may not reflect post-pandemic financial behaviors."
    - "The study does not explore causality between literacy and inclusion, only correlation."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant for domains related to Filipino Cultural Context (2.A, 2.D), Existing Systems & Gaps (4.A, 4.B), and Behavioral Profiling (5.A). Topic 4.B was rated 'high' due to the paper's explicit identification of a research gap. Topics 1.C and 2.A were rated 'medium' as they provide supporting evidence for behavioral outcomes and cultural practices. Topics 1.A, 1.B, 4.A, and 10.A were rated 'low' or 'contextual' as they provide background framing or tangential data points. Borderline cases included the paper's mention of remittances (touching 2.B/2.D), which was resolved by assigning 2.D (contextual) and not 2.B. Topics related to algorithm-specific domains (e.g., 6.A, 7.A, 8.A) were considered and rejected because the paper uses standard econometric models (probit/OLS), not advanced PFMS algorithms. Overall, the paper provides foundational evidence for Odin's user education and behavioral profiling modules."
limitations:
  - "The financial literacy quiz used only three questions, which may not capture the full construct of financial literacy."
  - "The study relies on cross-sectional data, precluding causal inference between literacy and inclusion. [unacknowledged]"
  - "The survey data is from 2019, potentially limiting applicability to current financial behaviors post-pandemic. [unacknowledged]"
remember_this:
  - "Financial literacy increases the likelihood of account ownership by 3.7-4.2 percentage points."
  - "A one-point literacy increase raises financial service use likelihood by 4.9-6.0 percentage points."
  - "Being the main household financial decision-maker is strongly correlated with financial inclusion."
  - "Income above PHP 40,000 significantly increases the probability of owning a financial account."
  - "Awareness of BSP programs positively impacts account ownership and investment participation."
```
---


---

## Agent Instruction

If the agent reading this document believes further context about a paper is needed, it may request the original converted markdown file (with the '_marked' suffix) from the user for the relevant paper(s).
