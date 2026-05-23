## Source: `1.B/AL--Apus_et-al_2023_summarized.md`

**Title:** Predicting the Filipino Household Income Using Naive Bayes Classification Algorithm

### TL;DR

Naive Bayes with bagging ensemble achieved **93% accuracy** predicting Filipino household income classes from expenditure patterns, outperforming boosting (89%).

### Findings

1. Bagging ensemble (Model I) achieved **93% accuracy**, with weighted precision of 0.93, recall of 0.94, and F1-score of 0.94.
2. Boosting ensemble (Model II) achieved 89% accuracy, with weighted precision of 0.90, recall of 0.93, and F1-score of 0.91.
3. Poor income class had the highest number of true positives; rich class had the lowest due to fewer instances in the dataset.
- Total food expenditure, transportation expenditure, and education expenditure were among the top predictive features (scores: 7.23, 5.54, 5.23 respectively).
- Bagging reduced variance more effectively than boosting for the Naive Bayes classifier on this dataset.

### Relevance to Odin

**Topics:**

1.B — Financial Structure of Filipino Young Professionals

3.A — Expense Categorization Frameworks

5.C — Financial Behavioral Profile Classification Algorithm

**Contribution to Odin:**

This paper directly informs Odin's financial behavioral profiling module by demonstrating that expenditure-based features (not just income or demographics) can effectively classify Filipino households into income classes using a simple, fast algorithm (Naive Bayes). The 93% accuracy on real FIES data justifies using similar classification approaches for Odin's user income typology, especially given Odin's manual transaction input — expenditure patterns are the primary data available. The feature selection results (food, transport, education as top predictors) provide empirical grounding for Odin's essential expense categories and their relative importance in determining financial capacity.

**Directly justifies:**

- "Naive Bayes with bagging ensemble achieves 93% accuracy classifying Filipino household income from expenditure data alone, using 41,545 FIES households."
- "Total food expenditure, transportation, and education spending are the three strongest expenditure-based predictors of income class in the Philippine setting."
- "Expenditure features outperform purely socio-demographic variables for income classification, supporting Odin's use of transaction history over user-declared demographic data."
- "Bagging reduces variance in Naive Bayes predictions more effectively than boosting on imbalanced income class data (93% vs 89% accuracy)."

**Limits of relevance:**

- Paper predicts static income class (annual survey), not dynamic behavioral profiles that change over time — Odin requires progressive reclassification.
- Income classes are seven broad brackets; Odin's typology for young professionals may require finer or different segmentation.
- Data is household-level, not individual young professional — spending patterns differ between household heads and individual budgeters.
- No evaluation of cold-start performance — unknown how Naive Bayes performs with sparse or short transaction histories.

### Limitations

- Dataset is from 2018; spending patterns and income distributions may have shifted post-pandemic. [unacknowledged]
- Class imbalance (few rich households) reduces precision for higher income classes — a limitation for Odin's potential high-income users.
- Missing data handling used mode/mean imputation, which may introduce bias; no sensitivity analysis reported.
- No comparison against other algorithms (random forest, SVM, logistic regression) to establish Naive Bayes as optimal.
- Paper does not address temporal or sequential spending patterns — only static snapshot classification.

---

## Source: `1.B/AL--Onsay_&_Rabajante_2024a_summarized.md`

**Title:** Measuring the unmeasurable multidimensional poverty for economic development: Datasets, algorithms, and models from the poorest region of Luzon, Philippines

### TL;DR

Logistic regression applied to 14,021 households in rural Philippines predicts multidimensional poverty with 73.29% accuracy using health, housing, water, education, and disaster indicators.

### Findings

1. Municipality-wide poverty incidence is **63.70%** (headcount ratio) — ranges from 21.38% to 98.45% across barangays.
2. Logistic regression achieved **73.29% correctly classified** predictions for poverty status.
3. **77.48% sensitivity** (correctly identified poor households) and 66.31% specificity.
- Household size, informal settler status, and lack of water/sanitation access are strong positive predictors of poverty (p < 0.001).
- Disaster preparedness reduces poverty probability; typhoon and drought exposure increase it.

### Relevance to Odin

**Topics:**

1.B — Financial Structure of Filipino Young Professionals

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

8.A — Anomaly Detection in Personal Finance Systems

**Contribution to Odin:**

This paper provides a validated methodological template for Odin's classification module, demonstrating that logistic regression on complete enumeration household data achieves 73% accuracy in predicting binary financial outcomes (poor/non-poor). The interaction-term approach (e.g., informal settlers × household members) is directly applicable to Odin's profile classification, where income stability interacts with dependency ratios. Although the outcome variable is poverty status rather than spending behavior, the same logistic regression framework can classify users into financial behavioral profiles using Odin's transaction and declaration data.

**Directly justifies:**

- "Complete enumeration household data eliminates sampling error entirely, a property relevant to Odin's user-level classification where each user is their own population."
- "Logistic regression on 19 multidimensional indicators achieved 73.29% classification accuracy for poverty status, providing a baseline benchmark for Odin's behavioral profile classifier."
- "Interaction terms (e.g., household size × informal settlement) significantly improved model fit — analogous to Odin using income stability × dependency ratio interactions in profile classification."
- "The poverty gap index measures depth, not just incidence — Odin's anomaly detection can similarly measure deviation magnitude, not just binary overage."
- "Predictive power varied substantially across four sectors within the same municipality — Odin must expect and handle geographic and cultural heterogeneity in spending patterns."

**Limits of relevance:**

- Paper predicts poverty (income < threshold), not per-category spending or budget adherence — the dependent variable differs from Odin's forecasting targets.
- Rural agricultural population (Goa, Camarines Sur) differs demographically from Metro Manila young professionals.
- Data is complete enumeration census (no sampling), but Odin operates on individual user data with cold-start sparsity.
- Logistic regression is simpler than LSTM or sequential models Odin may use for spending forecasting; relevance is primarily to classification, not time-series prediction.

### Limitations

- Time restriction: data covers 2018–2020 only; no update cycle specified for longitudinal analysis.
- Geography-specific: rural Bicol region findings may not generalize to urban Metro Manila context. [unacknowledged]
- No validation of model performance on holdout data or alternative time periods — classification accuracy reported on training data only. [unacknowledged]
- Binary poverty outcome (poor/non-poor) collapses continuous variation in financial health.
- Authors state "no known limitations due to complete enumeration," but sampling error is not the only validity threat — omitted variable bias remains.

---

## Source: `10.A/AL--Espiritu_et-al_2024_summarized.md`

**Title:** Data-Driven Decision Making in Scholarship Programs: Leveraging Decision Trees and Clustering Algorithms

### TL;DR

Decision trees (C4.5) and K-means clustering improved scholarship application success rates by 31% and achieved 80% predictive accuracy in a Philippine government program.

### Findings

1. Predictive accuracy for successful scholarship outcomes reached **80%** , while failure prediction accuracy was 70%.
2. Online registration system improved success rates by **31%** compared to traditional manual methods.
3. Duplicate removal eliminated 3,100 duplicate entries, improving dataset quality and integrity.
4. High-impact success factors: parental occupation (small farmer), academic performance (GPA), and financial need.
5. User satisfaction surveys showed high preference for the online system due to ease of use and accessibility.

### Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

10.A — Data Privacy and Security in Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper demonstrates the implementation of decision tree (C4.5) and K-means clustering algorithms for classification and pattern recognition in a Philippine government context — directly applicable to Odin's financial behavioral profiling module. Its use of accuracy, precision, recall, and F1-score provides a ready‑to‑cite evaluation framework for Odin's classifier selection and benchmarking. Most importantly, the paper's explicit adherence to the Philippine Data Privacy Act (RA 10173), including data anonymization, informed consent, and security measures, offers a practical precedent for Odin's privacy‑by‑design requirements under local law.

**Directly justifies:**

- "C4.5 decision trees achieved 80% predictive accuracy on a binary classification task using mixed categorical and numerical data in a Philippine government program."
- "K-means clustering revealed underlying applicant groups and common success characteristics, supporting unsupervised pattern discovery in classification pipelines."
- "Compliance with RA 10173 (Data Privacy Act of 2012) was operationalized through data anonymization, access controls, encryption, and transparent communication with stakeholders."
- "Accuracy, precision, recall, and F1‑score were jointly reported as evaluation metrics for a classification algorithm in a resource‑constrained Philippine setting."

**Limits of relevance:**

- Domain is scholarship applicant selection, not personal financial behavior or spending patterns — classification features differ substantially.
- No comparison of decision trees against other classifiers (e.g., logistic regression, random forest, LSTM) — limits algorithm justification strength.
- Dataset is administrative scholarship records, not user transaction histories — cold‑start and concept drift dynamics are unaddressed.
- The online system is web‑based, not mobile‑first; mobile‑specific constraints (offline sync, low bandwidth) are not considered.

### Limitations

- Generalizability to personal finance domains is untested — scholarship applicant features (GPA, parental occupation) do not map to spending behavior.
- No cross‑validation or train/test split reported — reported 80% accuracy may be optimistic. [unacknowledged]
- The study does not compare C4.5 or K‑means against alternative algorithms (e.g., random forest, hierarchical clustering) to justify selection.
- Ethical discussion of data anonymization does not address re‑identification risks in small‑population contexts like Isabela province. [unacknowledged]
- User satisfaction and success rate improvements conflate the online system's effect with data mining — causal attribution is unclear.

---

## Source: `10.B/AL--Abadam_et-al_2026_summarized.md`

**Title:** Development of A Cross-Platform Application Blue-Collar Marketplace with Prescriptive Analytics Using Linear Programming Algorithm

### TL;DR

A cross-platform job marketplace with linear programming‑based prescriptive pricing achieved a **4.98/6** ISO 25010 rating, demonstrating effective use of optimization and trust features in a Philippine blue‑collar context.

### Findings

1. Overall ISO/IEC 25010 mean rating was **4.98 out of 6** (interpreted as “Agree”), indicating high user satisfaction.
2. Regular users rated functionality at 5.44/6 (“Strongly Agree”), while IT professionals rated usability at 5.13/6 (“Agree”).
3. Performance efficiency and reliability both scored above 5.1/6 from regular users.
- The LP‑based pricing recommendation successfully generated fair, market‑aligned job prices within employer budgets.
- Identity verification and messaging features were cited as trust‑enhancing by both freelancers and employers.

### Relevance to Odin

**Topics:**

9.A — Mobile-First Design Principles and Rationale

10.B — User Trust in Personal Finance Systems

12.A — Evaluation Frameworks for Personal Finance Systems

**Contribution to Odin:**

This paper provides a concrete, locally‑implemented example of linear programming applied to a constrained optimization problem in a Philippine digital platform, directly supporting Odin’s budget recommendation module which also uses constraint‑based allocation. The successful deployment of ISO/IEC 25010 as an evaluation framework—achieving a 4.98/6 rating—demonstrates that this quality model is practical and well‑received by both IT professionals and regular users in the Philippine context, justifying its use for Odin. Furthermore, the identity verification and rating system’s positive effect on user trust offers empirical grounding for Odin’s privacy‑by‑design and trust‑building features, despite the domain difference (job marketplace vs. personal finance).

**Directly justifies:**

- “Linear programming can provide optimized, fair recommendations under multiple constraints (minimum price, employer budget, demand ceiling) in a Philippine digital platform context.”
- “ISO/IEC 25010 evaluation of a locally‑developed cross‑platform application produced a 4.98/6 mean rating, confirming the framework’s applicability and user acceptance in the Philippines.”
- “Government‑ID‑based identity verification and post‑transaction rating systems improve perceived trust and reduce informal hiring risks in a two‑sided marketplace.”
- “Rapid Application Development (RAD) with iterative user feedback successfully delivered a functional, usable system for Philippine blue‑collar workers and employers.”

**Limits of relevance:**

- Domain mismatch: job price optimization for a marketplace vs. spending budget allocation for personal finance; the objective (maximize price vs. constrain spending) differs.
- User population: blue‑collar freelancers and employers, not young professionals managing personal budgets.
- LP model is extremely simple (single decision variable, no temporal dynamics) compared to Odin’s per‑category forecasting and reclassification needs.
- Evaluation does not include cold‑start scenarios or longitudinal behavioral drift, which are critical for Odin.

### Limitations

- No statistical test reported for the ISO 25010 ratings (e.g., confidence intervals or p‑values), making the 4.98/6 a descriptive average only.
- Evaluation sample size and demographics are not disclosed, limiting generalizability to Odin’s target population of Filipino young professionals. [unacknowledged]
- The LP model’s single variable (price) ignores multidimensional trade‑offs (e.g., quality, urgency, worker reputation) present in real job matching.
- No comparison with alternative algorithms (e.g., rule‑based, regression, or other optimization methods) to justify LP choice.
- The paper does not evaluate system performance under high concurrency or with sparse user activity (cold‑start), both relevant to Odin’s early adoption phase. [unacknowledged]

---

## Source: `12.A/AL--de-Goma_et-al_2025b_summarized.md`

**Title:** Using Item Personality-Based Profiling in Music Recommender Systems

### TL;DR

A hybrid recommender using personality-based item profiles and LightFM outperforms pure collaborative filtering, achieving 0.57 precision and 0.62 recall in cold-start scenarios.

### Findings

1. Hybrid model with WARP loss achieved **0.46 precision, 0.64 recall, and 0.54 F1** on validation set — no severe overfitting unlike pure CF.
2. In online evaluation, the hybrid model (Model A) scored higher than pure CF (Model B): precision 0.57 vs 0.41, recall 0.62 vs 0.46, F1 0.58 vs 0.40.
- Users rated hybrid model higher on recommendation quality (3.7 vs 3.4) and user satisfaction (4.15 vs 3.55), but pure CF was perceived as more diverse (3.95 vs 3.75).
- Chi-square test showed statistically significant preference for hybrid model’s recommendation quality (p < 0.05).

### Relevance to Odin

**Topics:**

5.B — Profile Dynamics and the Cold-Start Problem

5.C — Financial Behavioral Profile Classification Algorithm

12.A — Evaluation Frameworks for Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly informs Odin’s approach to cold-start profiling by demonstrating that hybrid models (combining user features with interaction data) outperform pure collaborative filtering when user history is sparse. The LightFM architecture with WARP loss provides a concrete algorithmic template for Odin’s financial behavioral profile classification module, where new users have no spending history. The evaluation framework — combining offline metrics (precision/recall/AUC/F1) with online user-centric assessment (ResQue) — maps directly to Odin’s planned evaluation strategy under ISO 25010 and SUS.

**Directly justifies:**

- “Hybrid recommender systems incorporating user feature embeddings (personality, preferences) achieve 16 percentage points higher precision than pure collaborative filtering in cold-start scenarios (0.57 vs 0.41).”
- “WARP loss function outperforms BPR for top-k recommendation on sparse, imbalanced interaction data — applicable to Odin’s budget recommendation cold-start problem.”
- “Item personality profiles constructed from user-item affinity proportions enable content-based cold-start recommendations without requiring extensive interaction history.”
- “Offline metrics (precision@k, recall@k, AUC, F1) combined with user-reported quality and satisfaction produce a complete evaluation picture — aligns with Odin’s ISO 25010 + SUS design.”

**Limits of relevance:**

- Domain is music recommendation, not financial budgeting — the user-item interaction structure differs (likes vs. spending amounts).
- Personality traits (Big Five) are not equivalent to financial behavioral profiles — Odin profiles based on income stability and spending patterns, not psychological traits.
- Dataset size (208 users, 100 items) is small; scaling to Odin’s expected user base may require validation.
- No explicit temporal dynamics; Odin’s spending forecasting requires sequential data, which this paper does not address.

### Limitations

- Small sample (208 students) from a single university — not representative of Filipino young professionals broadly.
- Only 100 songs in the dataset; limited item diversity may inflate precision and recall artificially. [unacknowledged]
- Personality data was self-reported via survey; no validation against ground-truth listening behavior.
- No comparison against non-hybrid content-based methods; only pure CF baseline.
- Online evaluation used only 20 new users — too small for robust statistical inference beyond chi-square.

---

## Source: `12.B/AL--Delena_et-al_2025_summarized.md`

**Title:** Predicting student retention: A comparative study of machine learning approach utilizing sociodemographic and academic factors

### TL;DR

XGBoost achieved **90.66% cross-validated accuracy** predicting student dropout from sociodemographic and academic data, outperforming nine other ML algorithms on a Philippine university dataset.

### Findings

1. XGBoost achieved the **highest cross-validated accuracy (90.66%)** and F1 Score (90.72), with low error (MSE = 9.34, Log Loss = 0.26).
2. GB and ANN followed closely: GB at 89.42% accuracy, ANN at 88.39% accuracy, both with strong precision-recall balance.
3. Naïve Bayes had the highest recall (97.21%) but excessive false positives (31), limiting practical use.
- Decision Tree overfit: dropped from 90.34% (train-test) to 84.44% (cross-validation) accuracy.
- Ensemble models (XGBoost, GB) showed stable generalization; nonparametric models (KNN, DT) required more tuning.

### Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

8.B — Anomaly Detection Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper provides a direct benchmark for algorithm selection in Odin's binary classification tasks, specifically financial behavioral profiling (e.g., income stability type) and anomalous spending detection (dropout vs. retained analog). The rigorous comparison of ten algorithms using both train-test split and 5-fold cross-validation demonstrates that XGBoost consistently outperforms alternatives on structured tabular data with mixed sociodemographic and performance features — a data structure similar to Odin's user transaction and profile attributes. Although the domain is student retention, the methodological finding (XGBoost > GB > ANN > others) and the use of Log Loss as a calibration metric directly inform Odin's classification module design and evaluation protocol.

**Directly justifies:**

- "XGBoost achieves 90.66% cross-validated accuracy and F1 of 90.72 on a binary classification task with balanced classes, outperforming GB (89.42%) and ANN (88.39%)."
- "Cross-validation reduced Decision Tree accuracy by ~6 percentage points (90.34% → 84.44%), demonstrating that single train-test splits overestimate performance — Odin must use k-fold validation for module evaluation."
- "Log Loss (0.26 for XGBoost) provides a more nuanced calibration measure than accuracy alone; Odin's anomaly detection module should report Log Loss alongside F1 to capture false positive costs."
- "Naïve Bayes produces high recall (97%) but excessive false positives (31), making it unsuitable for high-stakes classification where false alarms erode user trust."

**Limits of relevance:**

- Domain mismatch: student dropout prediction vs. personal finance anomaly detection; financial transaction patterns may differ in feature distribution and class imbalance.
- Small dataset (n=482); Odin may have larger user bases or different data sparsity characteristics.
- No temporal or sequential data; Odin's spending forecasting requires time-series models not evaluated here.
- No explainability analysis; deployment in financial systems may require interpretable models, which XGBoost provides only via SHAP (not discussed).

### Limitations

- Single institution dataset (MSU-Marawi) limits external validity to other Philippine HEIs, let alone personal finance users. [unacknowledged]
- No behavioral or engagement features (LMS activity, peer interaction) were included, which are known predictors of retention; Odin similarly lacks such data.
- 5-fold cross-validation used but not stratified or nested; class balance was natural, but more rigorous validation could improve generalizability estimates. [unacknowledged]
- Model interpretability not addressed; black-box nature of XGBoost may hinder adoption in contexts requiring explainability (e.g., financial alerts).
- Manual hyperparameter tuning was used; automated optimization might alter relative algorithm rankings.

---

## Source: `12.B/AL--Fernando_&_Ballera_2024_summarized.md`

**Title:** Balancing Efficiency and Accuracy: A Hybrid Approach to Solving the 0/1 Knapsack Problem

### TL;DR

A hybrid Greedy-Dynamic Programming algorithm for the 0/1 knapsack problem achieves near-optimal solutions (within 0.5% of optimum) while running 48% faster and using 30% less memory than pure DP on large datasets.

### Findings

1. Hybrid algorithm achieved **solutions within 0.5% of DP optimal value** across all dataset sizes (10 to 5,000 items).
2. Execution time for hybrid was 48% faster than DP on average for datasets >1,000 items (e.g., 13.5s vs 26.0s at 5,000 items).
3. Memory usage of hybrid was ~30% lower than DP due to pruning (see Figure 2).
- Greedy was fastest but suboptimal (e.g., 280 vs optimal 300 on 10 items).
- DP delivered optimal results but became impractical for large datasets (26 seconds at 5,000 items).

### Relevance to Odin

**Topics:**

7.B — Budget Recommendation in Personal Finance Systems

7.C — Budget Recommendation Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly informs Odin’s budget recommendation module by quantifying the trade-off between solution optimality and computational cost in a resource‑allocation optimization problem. Although the 0/1 knapsack is binary, the hybrid principle—use a fast heuristic to bound the search then refine with an exact method—applies directly to constrained budget allocation across spending categories. The explicit performance metrics (48% faster, 30% less memory, 0.5% accuracy loss) provide a defendable benchmark for choosing a hybrid over pure DP on mobile devices where CPU and memory are limited. Because the authors are from Philippine institutions, the algorithm’s viability in a local academic context supports its practical deployment in a Philippine‑focused app like Odin.

**Directly justifies:**

- "A hybrid Greedy‑DP algorithm for the 0/1 knapsack problem achieves solutions within 0.5% of optimal while running 48% faster than pure DP on datasets of 5,000 items."
- "Hybrid memory usage is approximately 30% lower than DP due to pruning, making it suitable for memory‑constrained mobile environments."
- "Greedy alone is suboptimal (e.g., 280 vs optimal 300 on 10 items), so a pure heuristic is insufficient for budget allocation where precision matters."
- "The hybrid approach requires no complex parameter tuning, unlike genetic or metaheuristic hybrids, easing implementation in a production system."

**Limits of relevance:**

- The paper solves a binary (0/1) selection problem, whereas Odin’s budget recommendation allocates continuous or integer amounts across categories.
- Datasets are synthetic and not drawn from personal financial transactions; real spending patterns may have different constraints.
- The knapsack capacity and item weights are static; Odin’s budget constraints update monthly with income changes.
- Algorithm tested up to 5,000 items, but Odin’s category count is small (<50), so extreme scaling not needed.

### Limitations

- Only synthetic datasets were used; no validation on real-world financial or spending data.
- Comparison limited to Greedy and DP; does not benchmark against modern metaheuristics (e.g., genetic algorithms, particle swarm) that may offer different trade-offs. [unacknowledged]
- Assumes static item set and capacity; dynamic or streaming scenarios (e.g., new transactions arriving over time) are not evaluated.
- No analysis of how item correlations or constraints (e.g., mutually exclusive categories) affect performance.
- The 0.5% accuracy loss is reported but the absolute financial impact of such error in a budget context is not discussed.

---

## Source: `12.B/AL--Guban_et-al_2025_summarized.md`

**Title:** WEKA-BASED DECISION-TREE MODEL FOR USER SUBSCRIPTION PLAN PREDICTION

### TL;DR

A J48 decision tree predicts streaming subscription plans with **72% accuracy**, identifying country, age, and device type as the most influential predictors.

### Findings

1. Overall classification accuracy: **72%** on the 500‑instance test set.
2. Country was the most influential predictor, followed by age and device type (gender and start month had weaker effects).
3. Standard plan achieved highest precision (0.793) and ROC area (0.871); Basic and Premium had ROC areas >0.81.
- United Kingdom users all defaulted to Standard plan (195 training instances), indicating extreme market homogeneity.
- Young smartphone users who subscribed later in the year preferred Premium; older Smart TV users leaned toward Basic or Standard.

### Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper demonstrates a complete supervised classification pipeline (J48 decision tree) for predicting user plan choices from demographic and behavioral attributes. The methodology directly informs Odin’s financial behavioral profile classification module, showing how an interpretable tree-based model can produce actionable rules (e.g., “age ≤31 and device=smartphone → Premium”). Although the domain is streaming subscriptions, the classification approach and evaluation framework (accuracy, precision, recall, F-measure, ROC area, confusion matrix) are transferable to predicting user spending behavior or budget preference profiles in Odin. The paper also reinforces that country/geography can be a strong predictor—relevant when Odin expands beyond Metro Manila.

**Directly justifies:**

- “J48 decision trees achieve 72% accuracy on multi‑class user classification with 2,500 records and five attributes using an 80/20 train‑test split.”
- “Country, age, and device type are the most influential predictors in user tier choice, demonstrating that geography and demographics drive subscription decisions.”
- “Standard plan classification reached precision 0.793 and ROC area 0.871, showing strong discriminative power for balanced classes.”
- “Per‑class precision, recall, and F‑measure provide more nuanced evaluation than accuracy alone, especially when class distributions differ.”

**Limits of relevance:**

- Domain is streaming subscription plans, not personal spending or budgeting behavior.
- Dataset lacks financial variables (income, expenses, savings) essential for Odin’s core tasks.
- The paper is a student course project, not peer‑reviewed; methodology lacks rigorous validation (e.g., cross‑validation, hyperparameter tuning).
- Findings are based on a streaming platform dataset, not Philippine financial data.

### Limitations

- The original data source is not specified, and real‑world validity is unconfirmed [unacknowledged].
- No comparison to other algorithms (Random Forest, SVM, logistic regression) to justify J48 selection.
- Single 80/20 split without cross‑validation increases risk of overfitting; tree depth and leaf count not reported.
- External validity limited to streaming platforms; not tested on financial transaction data.
- No analysis of class imbalance or handling of rare subscription tiers (all three tiers appear roughly balanced in the confusion matrix).

---

## Source: `12.B/AL--Gumasing_et-al_2023_summarized.md`

**Title:** A machine learning ensemble approach to predicting factors affecting the intention and usage behavior towards online groceries applications in the Philippines

### TL;DR

Random Forest and Artificial Neural Network ensembles predicted online grocery usage behavior with 96% accuracy, identifying perceived benefits and vulnerability as top factors.

### Findings

1. ANN ranked perceived benefit as most important factor (importance score 0.270), followed by perceived vulnerability (0.265), behavioral intention (0.258), performance expectancy (0.248), and perceived severity (0.244).
2. Random Forest decision tree showed that perceived benefit and perceived vulnerability lead to **very high usage behavior**; perceived benefit, behavioral intention, and perceived severity lead to high usage behavior.
3. All 12 hypotheses were accepted (p < 0.05); facilitating conditions had the lowest importance (0.158) but still significant.
- Cronbach's alpha for all constructs >0.8, VIF <5 (no multicollinearity).
- Taylor diagram confirmed consistency between ANN and RF results (correlation >0.9, RMSE <20%).

### Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper demonstrates that Random Forest and Artificial Neural Network ensembles achieve high accuracy (96–97%) in classifying behavioral intention and usage patterns from survey data. For Odin's financial behavioral profiling module, this justifies using ensemble machine learning (specifically RF or ANN) over traditional statistical methods like SEM, as ML captures nonlinear relationships better. The paper's Filipino respondent base (though for groceries) provides a precedent for ML-based classification of technology acceptance in the local context, which can be transferred to personal finance apps. The evaluation metrics (accuracy, standard deviation, Taylor diagram) offer a template for Odin's module-level algorithm validation.

**Directly justifies:**

- "Random Forest Classifier achieved 96% accuracy with 0.00 standard deviation in predicting usage behavior, demonstrating stable classification performance for consumer technology adoption."
- "Artificial Neural Network achieved 96.63% testing accuracy in ranking factor importance for behavioral intention, outperforming traditional SEM in capturing nonlinear relationships."
- "Perceived benefit, perceived vulnerability, and behavioral intention are the top three predictors of usage behavior, suggesting that health-related threat appraisal drives technology adoption during a pandemic."
- "Ensemble of RF and ANN provides a reliable framework for predicting human behavior, with Taylor diagram confirming consistency (correlation >0.9)."

**Limits of relevance:**

- Paper focuses on online grocery shopping, not personal financial management; behavioral drivers may differ.
- Study conducted during COVID-19 pandemic; findings about threat perception may not generalize to normal conditions.
- Data collected via convenience sampling from urban areas; rural Filipino young professionals underrepresented.
- No longitudinal validation; classification model tested on single survey, not on actual transaction behavior over time.

### Limitations

- Respondents mainly from highly urbanized cities, limiting generalizability to rural Filipinos. (acknowledged)
- Socio-economic factors not analyzed via clustering; future work needed for customer segmentation. (acknowledged)
- No validation of ML predictions against actual behavioral outcomes (self-reported usage only). [unacknowledged]
- Cold-start scenario not considered; model requires survey data, not transaction histories. [unacknowledged]
- The 373 sample size may not capture full diversity of Filipino young professionals. [unacknowledged]

---

## Source: `12.B/AL--Laspinas_&_Murcia_2024_summarized.md`

**Title:** Machine Learning Approaches in Classifying Income Levels

### TL;DR

RandomForest and Random Tree achieved ~98% accuracy in predicting adult income levels, outperforming Logistic, J48, k‑NN, and NaiveBayes on a US census dataset.

### Findings

1. RandomForest and Random Tree achieved **98.35% and 98.37% accuracy** respectively – the highest among all classifiers.
2. RandomForest F‑measure = 0.983; Random Tree F‑measure = 0.984, indicating excellent precision‑recall balance.
3. J48 accuracy increased with confidence factor: 87.21% (C=0.25) → 90.85% (C=0.75).
4. k‑NN accuracy decreased as k increased: 89.11% (k=3) → 85.74% (k=9), contradicting the assumption that larger k always improves performance.
- Logistic regression (85.82%) and NaiveBayes (82.24%) performed adequately but lagged behind ensemble methods.

### Relevance to Odin

**Topics:**

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly informs Odin’s financial behavioral profiling module by benchmarking six supervised classifiers on income‑level prediction – a core dimension of user financial profiles (e.g., income stability and obligation weight). The finding that RandomForest and Random Tree achieve near‑98% accuracy on a large demographic dataset provides strong justification for considering ensemble methods when Odin’s classification module is implemented. Although the dataset is US‑based and the target is binary (>$50K), the methodological framework (tuning, cross‑validation, multi‑metric evaluation) is directly transferable to evaluating Odin’s profile classification algorithms.

**Directly justifies:**

- “RandomForest achieved 98.35% accuracy on binary income classification using demographic and employment features, outperforming Logistic, J48, k‑NN, and NaiveBayes.”
- “Ensemble methods (RandomForest, Random Tree) consistently deliver higher F‑measure (>0.98) and kappa (>0.95) than single classifiers on income prediction tasks.”
- “Hyperparameter tuning (J48 confidence factor, k‑NN’s k) significantly changes classifier performance – J48 accuracy rose from 87.2% to 90.8% as confidence increased.”
- “k‑NN accuracy decreases as neighborhood size grows beyond k=3 on the income dataset, contradicting the general assumption that larger k improves performance.”

**Limits of relevance:**

- Dataset is US Census data, not Filipino; income thresholds ($50K) and demographic distributions differ substantially.
- Target variable is binary (above/below $50K), whereas Odin may require multi‑class income typology or continuous estimation.
- No evaluation on sequential spending data or cold‑start conditions – Odin’s profiling must handle sparse early transactions.
- The paper does not address computational constraints on mobile devices, where ensemble methods may be heavier than simpler classifiers.

### Limitations

- Dataset is US‑based; findings may not generalize to Filipino income structures or cultural‑economic contexts. [unacknowledged]
- No comparison of ensemble methods against deep learning (e.g., LSTM) or recent boosting algorithms (XGBoost, LightGBM).
- Evaluation uses only 10‑fold CV on a single dataset; no external validation or out‑of‑sample testing on a separate holdout.
- Class imbalance not discussed – the dataset’s original proportion of >$50K earners is not reported, which affects precision/recall interpretation. [unacknowledged]
- Hyperparameter search limited to confidence factor and k; no optimization of tree depth, number of trees, or other critical parameters.

---

## Source: `12.B/AL--Mariano_&_Monreal_2025_summarized.md`

**Title:** Predict, Optimize, Deliver: Demand Forecasting and Resource Optimization for a Market Research Firm

### TL;DR

Prophet outperformed ARIMA, Holt-Winters, and LSTM in demand forecasting for a market research firm, balancing accuracy, interpretability, and speed for short-term workforce planning.

### Findings

1. Prophet achieved the lowest weighted error for Client 1 (**13.038**) and Client 2 (27.786) on the 30-day holdout, outperforming ARIMA (21.164 and 24.664) and LSTM (16.703 and 27.833).
2. Prophet’s overall weighted score (10.456) ranked #1, followed by ARIMA (11.582), LSTM (11.634), and Holt-Winters (13.062).
3. Larger training sizes consistently improved ARIMA and Holt-Winters MAE/RMSE but MAPE remained volatile for volatile clients.
- LSTM showed stable absolute accuracy across splits but higher complexity and data requirements reduced practical viability.
- Optimization achieved near-zero demand gaps under baseline, over‑forecast, and under‑forecast scenarios, respecting all capacity constraints.

### Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly informs Odin’s spending forecasting module by benchmarking four time‑series models (ARIMA, Holt-Winters, Prophet, LSTM) on real operational demand data using MAE, RMSE, and MAPE – metrics Odin will use to evaluate its own forecasting algorithms. The finding that Prophet balances accuracy, interpretability, and training speed (weighted score 10.456 vs. LSTM’s 11.634) justifies considering Prophet alongside LSTM for Odin’s short‑term per‑category spending forecasts, especially given Odin’s mobile‑first constraints where model simplicity and speed matter. Although the domain is workforce demand rather than personal spending, the methodological comparison of sequential forecasting algorithms and the weighted multi‑metric evaluation framework are directly transferable to Odin’s algorithm selection process.

**Directly justifies:**

- “Prophet achieved the lowest weighted error (13.038) on a 30‑day holdout, combining MAE, RMSE, and MAPE with interpretability and speed weights.”
- “LSTM showed stable performance across training splits but higher complexity and slower training reduced its practical viability for resource‑constrained environments.”
- “Larger training datasets improve ARIMA and Holt‑Winters accuracy, but MAPE remains volatile for irregular demand patterns – a limitation relevant to variable‑income users.”
- “A weighted evaluation score that includes interpretability (0.25) and training speed (0.25) alongside error metrics provides a more operational model selection criterion than accuracy alone.”

**Limits of relevance:**

- Domain is B2B workforce demand forecasting, not personal spending; patterns of seasonality and volatility may differ.
- Dataset is daily aggregated hours; Odin’s spending data is transaction‑level with potentially different temporal granularity.
- The paper does not address cold‑start forecasting (no historical data) – a critical challenge for new Odin users.
- No evaluation of per‑category forecasting; Odin requires separate models for each spending category.

### Limitations

- Data is from a single market research firm; generalizability to other service or personal finance contexts is unknown. [unacknowledged]
- Forecast evaluation excludes cold‑start scenarios; models assume sufficient historical data (multiple years). [unacknowledged]
- MAPE can exaggerate errors when actual values are small; the paper acknowledges this but still includes MAPE in weighted score.
- External economic indicators (e.g., inflation, remittance flows) were not incorporated, though they may affect demand.
- Optimization costs ($5/h regular, $10/h overtime) are hypothetical; real costs may alter allocation outcomes.

---

## Source: `12.B/AL--Ong_et-al_2023_summarized.md`

**Title:** Purchasing Intentions Analysis of Hybrid Cars Using Random Forest Classifier and Deep Learning

### TL;DR

Random Forest (94% accuracy) and Deep Learning (96.6% accuracy) identified perceived environmental concern, attitude, and perceived behavioral control as the top predictors of Filipino drivers’ intention to purchase hybrid cars.

### Findings

1. DLNN achieved **96.6% accuracy** — the highest among algorithms tested, validating its suitability for nonlinear behavioral models.
2. RFC achieved 94% accuracy with zero standard deviation at depth 5, producing a stable optimal tree.
3. Top 5 normalized importance scores (DLNN): PENC (100%), AT (96.3%), PBC (94.5%), SN (92.1%), PE (90.2%).
4. PENC was the root node in the optimal RFC tree, directly influencing AT, PBC, and PE to drive “very high” behavioral intention.
5. MLA results diverged from prior SEM results: PENC ranked 1st vs 5th, PECC ranked 10th vs 1st, and FC/EE/HB were significant in MLA but insignificant in SEM — demonstrating MLA’s advantage for mediated, nonlinear frameworks.

### Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper provides empirical evidence that Random Forest and Deep Learning Neural Networks achieve high accuracy (94–96.6%) in classifying behavioral intention from multi‑latent variable frameworks — directly supporting Odin’s choice of ML algorithms for financial behavioral profiling. Although the target behavior is hybrid car purchase, the methodological approach (survey‑derived latent variables → classification of intention levels) maps cleanly to Odin’s need to classify users into financial profiles (e.g., stable vs. variable income, high vs. low spending adherence). The finding that DLNN outperforms RFC on nonlinear, mediated relationships (e.g., PENC → AT/PBC/SN → BI) justifies Odin’s use of deep learning for profiling when behavioral drivers have indirect effects. Additionally, the paper’s validation using a Taylor diagram establishes a replicable evaluation framework (RMSE ≤20%, correlation ≥90%) that Odin can adopt for module‑level performance assessment.

**Directly justifies:**

- “Deep Learning Neural Networks achieved 96.6% accuracy in classifying behavioral intention from 12 latent predictors, outperforming Random Forest (94%) in a nonlinear mediated framework.”
- “Perceived Environmental Concern (100% normalized importance) and Attitude (96.3%) were the strongest predictors — demonstrating that external beliefs and affective evaluations dominate intention classification.”
- “Machine learning algorithms (RFC/DLNN) identified FC, EE, and HB as significant predictors where SEM found them insignificant, confirming MLA’s advantage for models with mediating variables and nonlinear relationships.”
- “A Taylor diagram validation standard (RMSE ≤20%, correlation ≥0.90) provides a replicable acceptance threshold for comparing classification models in behavioral studies.”

**Limits of relevance:**

- Domain is hybrid car purchase intention, not personal spending behavior — but the classification methodology (intention level from survey items) is transferable to financial profiling.
- Survey data is cross‑sectional (self‑reported intention), whereas Odin requires dynamic profiling from transaction histories — cold‑start and temporal drift are not addressed.
- All predictors are attitudinal (PENC, AT, SN, etc.) — no behavioral transaction data; Odin’s profiling will rely on actual spending patterns, not stated intentions.
- Sample is 86% male and skewed toward employed adults (98.8%) — not fully representative of Filipino young professionals (ages 20–40, both genders).

### Limitations

- Convenience and snowball sampling — results may not generalize to all Filipino drivers; potential self‑selection bias.
- Only two ML algorithms (RFC, DLNN) were optimized; other candidates (Naïve Bayes, SVM, XGBoost) were not compared. [unacknowledged]
- No temporal validation — the model predicts intention at a single point; cannot assess how profiles change over time or after purchase.
- Self‑administered online survey excludes non‑internet users and may overrepresent younger, tech‑savvy demographics. [unacknowledged]
- Dependent variable is behavioral intention, not actual purchase behavior — intention‑behavior gap is not measured.

---

## Source: `12.B/AL--Pandiin_&_Matias_2025_summarized.md`

**Title:** Predictive Modeling for Loan Eligibility Assessment: A Comparative Study of Logistic Regression, Random Forest, and Support Vector Machine with Detailed Oversampling

### TL;DR

Random Forest achieves **85% accuracy** and 0.94 AUC for loan eligibility prediction, outperforming Logistic Regression and SVM after Genetic Algorithm feature selection.

### Findings

1. Random Forest achieved the highest balanced performance: **accuracy 85%**, precision 86%, recall 84%, F1 85%, AUC 0.94.
2. Cross-validation mean accuracy for Random Forest was 92% (range 0.87–0.94), confirming robustness.
3. Lasso feature selection boosted Random Forest to 88.48% accuracy; same method dropped SVM to 52.73%.
4. SVM had very high recall (99%) but low precision (63%), minimizing false negatives at cost of many false positives.
- Logistic Regression showed consistent but lower accuracy (67%) and poor ability to capture non-linear patterns.
- Feature importance: Credit History (26.8%), Applicant Income (19.7%), Loan Amount (19.2%); Gender and Education had minimal impact (<2.5%).

### Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly informs Odin's choice of classifier for financial behavioral profiling by benchmarking Random Forest against Logistic Regression and SVM on a balanced financial dataset. The demonstration that Random Forest balances precision and recall (86% and 84%) while achieving high AUC (0.94) supports its selection over SVM (high recall but low precision, risking false profile assignments) for Odin's profiling module, where misclassification could erode user trust. Although the domain is loan eligibility rather than spending behavior, the methodological framework — feature selection via GA, oversampling for class balance, and multi-metric evaluation (accuracy, precision, recall, F1, AUC, cross-validation) — applies directly to Odin's algorithm evaluation under ISO 25010:2023.

**Directly justifies:**

- "Random Forest achieved 85% accuracy and 0.94 AUC on a balanced financial classification task, outperforming Logistic Regression (67%) and SVM (71%)."
- "Lasso-based feature selection combined with Random Forest raised accuracy to 88.48%, demonstrating that aggressive feature reduction benefits ensemble methods more than linear models or SVMs."
- "Credit history (26.8%), applicant income (19.7%), and loan amount (19.2%) dominated predictive importance, while demographic attributes (gender, education) contributed under 2.5% — a pattern that may generalize to financial behavior profiling."
- "5-fold cross-validation mean accuracy for Random Forest was 92%, confirming robust generalization beyond a single train-test split."

**Limits of relevance:**

- Loan eligibility prediction (binary approval/denial) differs from spending forecasting or multi-class behavioral profiling, so classifier performance may not translate directly.
- Dataset is from Kaggle (not Philippine-specific), and no Filipino demographic or cultural spending data was used.
- Oversampling via resample (not SMOTE) may cause overfitting; temporal patterns in transaction sequences are absent.
- No mobile-first or privacy constraints were considered; paper assumes batch processing on structured loan applications.

### Limitations

- The dataset is from Kaggle, not real-world bank data, limiting external validity to actual financial institutions. [unacknowledged]
- Oversampling with replacement may introduce overfitting; no comparison with SMOTE or other advanced balancing techniques.
- Hyperparameter tuning for classifiers is not described in depth; GA focused on feature selection, not model parameters. [unacknowledged]
- No evaluation of model explainability or fairness metrics beyond accuracy/precision/recall, despite citing fairness in ML.
- The study does not address temporal dynamics or sequential data, making it less applicable to recurring spending pattern detection.

---

## Source: `12.B/AL--Ram_&_Agoylo_2025_summarized.md`

**Title:** Optimized Random Forest Classifier for Students Lifestyle Prediction Using Behavioral Data: A Machine Learning Approach

### TL;DR

Random Forest with 30–40 trees predicts lifestyle categories from behavioral data with **75.07% accuracy** on real-world student responses, but perfectly overfits training data beyond 30 trees.

### Findings

1. Model achieved **75.07% accuracy** on 93 real-world student predictions, with precision 75.16%, recall 75.07%, and F1 74.40%.
2. Training accuracy reached 100% with ≥30 trees, indicating severe overfitting; test accuracy plateaued at ~75% regardless of more trees.
3. Optimal tree count was 30–40, balancing computational efficiency and generalization.
4. Classification distribution among 93 students: 50 Health-Conscious, 41 Fitness Enthusiast, 1 Eco-Friendly, 1 Social Media Influencer.
- Random Forest trained in 2.5 minutes on standard hardware, demonstrating practical feasibility for large-scale behavioral classification.

### Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly supports Odin’s financial behavioral profiling module by demonstrating how a Random Forest classifier can be optimized to predict user categories from behavioral features. The analysis of overfitting (100% training accuracy vs. 75% test accuracy) provides a concrete caution: Odin’s classification module must limit tree depth or number of trees to avoid memorizing user histories instead of learning general patterns. The use of standard evaluation metrics (accuracy, precision, recall, F1) aligns with Odin’s planned module evaluation framework. Although the domain is lifestyle rather than finance, the methodology for tuning a classifier on user-reported behavioral data transfers directly to profiling Filipino young professionals by spending behavior.

**Directly justifies:**

- "Random Forest with 30–40 trees achieves 75.07% accuracy on behavioral classification, but exceeding 30 trees causes perfect training overfitting without test accuracy gain."
- "Testing accuracy plateaus at ~75% after 20 trees while training accuracy climbs to 100% — increasing trees beyond an optimal threshold does not improve generalization."
- "Precision (75.16%) and recall (75.07%) remained closely balanced, indicating the classifier did not favor false positives over false negatives."
- "A Random Forest model trained on 500,000 records processed 93 real-world user inputs within 2.5 minutes, confirming practical deployability on standard hardware."
- "Self-reported behavioral data carries inherent bias; future work must address this limitation when deploying classification models in production."

**Limits of relevance:**

- Domain is lifestyle (health, fitness, social media) not financial spending — behavioral patterns may not transfer directly to budget adherence or expense categorization.
- Study population is students (age ~18–25), whereas Odin targets young professionals aged 20–40; income stability and financial obligations differ.
- Data came from a global Kaggle dataset plus 93 Filipino students; the classification categories (Fitness Enthusiast, etc.) have no financial analogue.
- Model was not tested on cold-start conditions (users with no history); all 93 students provided full behavioral inputs at once.

### Limitations

- Self-reported behavioral data introduces potential bias and inaccuracy; no objective validation of user responses. [unacknowledged]
- Predefined lifestyle categories (Fitness Enthusiast, Health-Conscious, Eco-Friendly, Social Media Influencer) may not capture the full complexity of individual behaviors.
- Student sample size of 93 is small for generalizing to broader Filipino population; no demographic breakdown beyond gender conversion.
- No comparison against alternative classifiers (e.g., SVM, neural networks) to establish Random Forest’s relative advantage.
- Model was tested only on students from a single university (Southern Leyte State University), limiting geographic generalizability.

---

## Source: `12.B/AL--Salvador_2024_summarized.md`

**Title:** Use of Boosting Algorithms in Household-Level Poverty Measurement: A Machine Learning Approach to Predict and Classify Household Wealth Quintiles in the Philippines

### TL;DR

CatBoost achieved **90.93% accuracy** across five wealth quintiles on 20,679 Philippine households, outperforming XGBoost (89.41%), GBM (89.05%), LightGBM (88.52%), and AdaBoost (80.39%).

### Findings

1. CatBoost achieved **90.93% accuracy** — highest among all models, followed by XGBoost (89.41%), GBM (89.05%), LightGBM (88.52%), and AdaBoost (80.39%).
2. Precision, recall, and F1‑scores followed the same ranking: CatBoost ≈ 90.9%, XGBoost ≈ 89.4%, GBM ≈ 89.0%, LightGBM ≈ 88.5%, AdaBoost ≈ 80–83%.
3. AUC‑ROC for CatBoost/GBM/LightGBM/XGBoost exceeded 0.98 across all quintiles; AdaBoost scored as low as 0.73 for the “Poorer” class.
- Top predictive features (from Table 1): source of drinking water, toilet type, television, refrigerator, bicycle, motorcycle, car, floor/wall/roof materials, and 4Ps beneficiary status.
- Computational trade‑offs: AdaBoost trained fastest (4.48s) but tested slowest (0.23s); CatBoost trained slowest (69.29s) with largest model (30.5 MB) but fastest testing (0.01s); LightGBM and XGBoost balanced speed and size well.

### Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly informs Odin’s classification module by benchmarking five boosting algorithms on a multi‑class prediction task using Philippine household data. Although the target (wealth quintile) differs from Odin’s financial behavioral profiles, the methodology — feature selection, handling class imbalance with SMOTE, and comparing accuracy/precision/recall/F1/AUC — is directly transferable to Odin’s user classification problem. The finding that CatBoost delivers top accuracy while LightGBM and XGBoost offer better computational efficiency provides a concrete trade‑off for Odin’s algorithm selection: accuracy‑critical modules may prefer CatBoost, while mobile‑constrained real‑time classification may favor LightGBM or XGBoost.

**Directly justifies:**

- “CatBoost achieved 90.93% accuracy on a 5‑class Philippine household classification task, outperforming XGBoost (89.41%), GBM (89.05%), and LightGBM (88.52%) — establishing CatBoost as a strong candidate for Odin’s financial profile classifier.”
- “LightGBM and XGBoost balance high accuracy (≥88.5%) with small model sizes (2.5–3.1 MB) and sub‑3‑second training times, making them suitable for mobile‑first deployment where computational resources are constrained.”
- “SMOTE (synthetic oversampling) effectively addresses class imbalance in household survey data and is directly applicable to Odin’s cold‑start problem where majority spending patterns may overwhelm minority behavioral profiles.”
- “AUC‑ROC scores near 1.0 for top boosting algorithms indicate excellent class separability — a desirable property for Odin’s profile classification to avoid ambiguous user assignments.”

**Limits of relevance:**

- The task is poverty/wealth classification using asset indicators (appliances, housing materials), not financial transaction‑based behavioral profiling — the feature space differs substantially from Odin’s spending data.
- The paper does not address temporal dynamics or profile updating over time, which is critical for Odin’s progressive reclassification.
- Dataset size (20,679 households) is larger than Odin’s expected early user base; cold‑start performance with sparse data is not evaluated.
- Evaluation metrics focus on static classification accuracy, not on interpretability or user trust, which are priorities for Odin’s classification module.

### Limitations

- The paper uses DHS asset‑based wealth index as ground truth, not actual income or spending data — limits direct transfer to financial behavior classification. [unacknowledged]
- No evaluation of model performance under cold‑start conditions (very few transactions per user), which is Odin’s core challenge.
- Feature selection retained 36 asset variables, but Odin’s classification would rely on transaction history, not household durable goods — feature engineering approach is not portable.
- Computational efficiency metrics are from a server environment; mobile inference times are not reported.
- The paper does not address concept drift (changing spending behavior over time), which Odin’s profiling module must handle.

---

## Source: `12.B/AL--Velasco_2026_summarized.md`

**Title:** A Decade of Applied Quantitative Analytics for Philippine Policy: Forecasting, Statistical Forensics, and Predictive Modeling Across Education, Energy, Agriculture, Health, and Finance

### TL;DR

A review of Philippine policy analytics across five sectors shows a progression from classical time series toward machine learning, Benford-based anomaly detection, and explainable AI, with uneven validation rigor.

### Findings

1. **Random forests outperformed other ML models for quarterly rice and corn production forecasting** in the Philippines.
2. NNAR achieved the best performance for measles incidence forecasting among SARIMA, Holt–Winters, ESN, and NNAR.
3. Holt–Winters gave lower RMSE and MAPE than SARIMA for quarterly rice and corn.
- Benford-based anomaly detection identified unusual first-digit patterns in dengue and crop statistics, providing a low-cost data-quality screen.
- LSTM with Takens embedding improved Philippine Stock Exchange Index prediction over linear models.
- Validation rigor is uneven: some studies use explicit holdout, others rely on residual diagnostics only.

### Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This review directly informs Odin’s forecasting module by surveying candidate algorithms (ARIMA, LSTM, random forests) and documenting their comparative performance on Philippine time-series data — justifying algorithm selection for spending prediction. The Benford-based anomaly detection work provides a precedent for unsupervised, cold-start anomaly screening that Odin could adapt to detect irregular manual transaction entries or data-quality issues. The paper’s critique of validation practices (holdout vs. residual diagnostics) and its call for rolling-origin evaluation and uncertainty quantification establish a benchmark for how Odin’s algorithmic modules should be rigorously tested before deployment.

**Directly justifies:**

- "LSTM with state-space reconstruction captures nonlinear temporal dependencies in Philippine financial time series, outperforming linear models on the PSE index."
- "Random forests achieved superior forecast accuracy for quarterly production data compared to ARIMA and SARIMA, supporting their use in spending forecasting."
- "Benford-based anomaly detection provides a low-cost unsupervised screening method for identifying unusual patterns in administrative data without labeled training examples."
- "Validation using holdout sets and error metrics (RMSE, MAE, MAPE) is standard, but rolling-origin evaluation and uncertainty quantification are recommended for operational policy analytics."

**Limits of relevance:**

- The paper is a review of policy analytics, not an original empirical study on personal finance systems; specific performance claims come from the cited primary studies, not the review itself.
- The finance domain is stock market prediction, not individual spending forecasting; transferability to personal transaction sequences is assumed but not tested.
- Benford analysis is used for data-quality auditing (e.g., crop statistics, disease counts), not for detecting anomalous spending deviations from a user’s budget.
- The reviewed studies use official aggregate datasets; Odin’s manual transaction input at the individual user level presents different sparsity and cold-start challenges not addressed.

### Limitations

- The corpus mixes journal articles, preprints, and SSRN papers with heterogeneous data frequencies, sample sizes, and validation designs — direct cross-sector comparisons are not appropriate.
- Some study characteristics were reconstructed from metadata when full texts were not equally accessible.
- No original empirical results are presented; the review synthesizes existing work, limiting the novelty of citable claims. [unacknowledged]
- The paper does not address mobile-first constraints, manual data entry, or personal finance user behavior — all central to Odin’s context. [unacknowledged]
- External validation across regions or periods is absent in most reviewed studies, a gap the paper itself acknowledges.

---

## Source: `5.C/AL--Onsay_&_Rabajante_2024b_summarized.md`

**Title:** When machine learning meets econometrics: Can it build a better measure to predict multidimensional poverty and examine unmeasurable economic conditions?

### TL;DR

Random forest achieved **0.9208 R²** and 95.94% accuracy for poverty prediction, outperforming XGBoost and LightGBM on Philippine indigenous community census data.

### Findings

1. Random forest regressor achieved the **highest R² of 0.9208** — linear regression scored only 0.4221.
2. Random forest classifier attained 95.94% accuracy in pipeline mode, with 90.69% at random split.
3. Lowest RMSE: random forest at 0.3298 vs. LightGBM 0.3642 and XGBoost 0.4001.
- Household size and informal settlement status are the strongest poverty predictors.
- 82% of indigenous people live in poverty; 71% are food-insecure.

### Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

**Contribution to Odin:**

This paper directly informs Odin's classification module (user financial profiling) by demonstrating that random forest outperforms boosting algorithms (XGBoost, LightGBM) on Philippine household data, achieving 0.92 R² and 95%+ accuracy. Although the target is poverty classification rather than spending behavior, the methodological framework — using econometric causality tests to select predictors before applying ML — maps directly to Odin's need to identify which user features (income stability, household size, spending patterns) causally drive financial behavior profiles. The paper's use of a full census (no sampling error) and local Philippine data provides strong justification for algorithm selection in Odin's cold-start profiling scenario.

**Directly justifies:**

- "Random forest achieves 0.9208 R² for binary poverty classification on Philippine census data, outperforming XGBoost (0.4722 MSE) and LightGBM (0.1242 MSE)."
- "Econometric causality testing (logit/probit) should precede ML feature selection to ensure predictors are causally linked to the target outcome, not merely correlated."
- "Household size and informal settlement status are the strongest predictors of poverty status in Philippine indigenous communities, suggesting these variables should be included in financial behavior profiles."
- "Random forest's ability to handle non‑linear relationships and estimate feature importance makes it suitable for classification tasks with multidimensional socioeconomic indicators."

**Limits of relevance:**

- Paper predicts poverty (binary low-income status), not spending behavior or budgeting adherence — the target outcome differs from Odin's forecasting and anomaly detection domains.
- Dataset is rural indigenous communities in Bicol, not Metro Manila young professionals; income patterns and spending structures may not generalize.
- No time-series or sequential data — the paper uses cross-sectional census data, whereas Odin requires longitudinal transaction sequences.
- Poverty classification uses a fixed monthly income threshold (PhP10,481 for a family of five), which does not account for individual‑level expense categorization or discretionary spending.

### Limitations

- No temporal validation — models are evaluated on cross-sectional data only; performance over time is untested. [unacknowledged]
- Paper claims “no known limits” due to full census, but generalizability outside Goa, Camarines Sur is not established.
- Model interpretability for end users is not addressed — only feature importance is reported.
- Binary poverty threshold (PhP10,481) is not adjusted for household size variation beyond the stated “family of five” assumption.
- The paper does not compare against deep learning methods (e.g., neural networks), which may be relevant for Odin's sequential forecasting.

---

## Source: `8.A/AL--Blancaflor_et-al_2024_summarized.md`

**Title:** Exploring Machine Learning for Credit Card Fraud Detection from a Philippine Perspective

### TL;DR

Credit card fraud in the Philippines rose 21% post-pandemic, and ML models—especially k‑NN (97.69%) and Naïve Bayes (97.92%)—outperform logistic regression (54.86%) on local transaction data.

### Findings

1. k‑NN achieved **97.69% accuracy** on Philippine credit card transaction data.  
2. Naïve Bayes reached **97.92% accuracy**, slightly outperforming k‑NN.  
3. Logistic regression performed poorly at **54.86% accuracy**.  
4. SVM accuracy varies up to 80%; ANN up to 98.44% depending on configuration.  
- ANN‑SMOTE outperformed all other model‑enhancement combinations (accuracy, precision, recall, F1).  
- Imbalanced data and concept drift remain key obstacles; hybrid sampling and meta‑learning are proposed as future improvements.

### Relevance to Odin

**Topics:**

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

**Contribution to Odin:**

This paper directly informs Odin’s anomalous spending detection module by benchmarking ML classifiers on imbalanced, real‑world transaction data from the Philippines. The finding that k‑NN and Naïve Bayes achieve >97% accuracy on highly skewed fraud data supports algorithm selection for detecting rare spending anomalies in Odin’s manual transaction logs. Although the domain is credit card fraud, the methodological lessons—handling class imbalance, evaluating with MCC/BCR, and the trade‑off between ANN accuracy and LR interpretability—apply directly to Odin’s need to flag unusual spending patterns without false‑alert fatigue.

**Directly justifies:**

- “k‑NN achieved 97.69% accuracy and Naïve Bayes 97.92% accuracy on Philippine credit card transaction data, outperforming logistic regression (54.86%) for imbalanced binary classification.”  
- “ANN with SMOTE enhancement outperformed all other model combinations on accuracy, precision, recall, and F1, making it a strong candidate for anomaly detection when interpretability is not the primary constraint.”  
- “Imbalanced data and concept drift are key challenges in transaction anomaly detection; hybrid sampling and meta‑learning are necessary to maintain real‑time performance.”  
- “MCC and BCR are more reliable than raw accuracy for evaluating detectors on highly skewed datasets where fraud (anomaly) cases are rare.”

**Limits of relevance:**

- The paper targets credit card fraud, not personal spending anomalies (e.g., overspending in a category). Fraud patterns may differ from legitimate but unusual spending.  
- No evaluation of cold‑start performance (new users with no transaction history), which is critical for Odin.  
- Dataset is not publicly described (size, features, class imbalance ratio), limiting replicability.  
- Algorithms compared are supervised; Odin’s anomaly detection may require unsupervised methods due to lack of labeled anomalies.

### Limitations

- Dataset size and exact class imbalance ratio are not reported, making it difficult to judge generalizability.  
- No comparison of supervised vs. unsupervised anomaly detection methods (e.g., Isolation Forest), which are more relevant when labeled fraud is unavailable. [unacknowledged]  
- The paper does not evaluate computational cost or latency for real‑time detection on mobile devices. [unacknowledged]  
- Concept drift is mentioned but not empirically tested; no longitudinal evaluation over changing fraud patterns.  
- Accuracy figures for SVM and ANN are reported as “varies up to” without specific dataset conditions, reducing precision.
