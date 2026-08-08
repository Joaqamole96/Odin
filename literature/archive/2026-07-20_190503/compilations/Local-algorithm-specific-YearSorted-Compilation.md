# Compiled Research Summaries

## Filters Applied

- Designation: `local-algorithm-specific`

**Total Papers:** 34

**Note:** Sorted by year.

---

## Paper 1: Olabintan_summarized.md

**Source File:** `Olabintan_summarized.md`

```yaml
paper_id: 10.2139/ssrn.6837665
designation: local-algorithm-specific
title: FairLend-Africa: An Explainable Machine Learning Framework for Alternative Credit Scoring Using Behavioral Financial Data in Financially Excluded African Communities
authors: Olabintan, I.
year: 2026
venue: SSRN
odin_topics:
  - 1.A
  - 1.C
  - 2.B
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 7.B
  - 7.C
  - 8.A
  - 8.B
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
  - 12.C
tldr: An explainable ML framework for alternative credit scoring using mobile money behavioral data, achieving ROC-AUC of 0.714 on synthetic data with SHAP explanations and fairness auditing.
problem_and_motivation: Billions of adults globally lack formal credit histories, making them invisible to conventional scoring systems. Behavioral financial data from mobile money offers a potential proxy for creditworthiness, but integration into fair and explainable frameworks remains limited.
approach:
  - Synthetic dataset of 10,000 borrower records with 16 raw behavioral features from mobile money and credit history was generated.
  - XGBoost classifier was trained with hyperparameter optimization via RandomizedSearchCV and evaluated against logistic regression.
  - SHAP provided global feature importance and local explanations for individual credit decisions.
  - Systematic fairness audit assessed demographic parity, equal opportunity, and predictive parity across regional and gender subgroups.
  - System was implemented as a REST API with an interactive React dashboard for loan officers.
findings:
  - Tuned XGBoost achieved a held-out test ROC-AUC of 0.714, matching the logistic regression baseline of 0.713.
  - Wallet balance trend and savings consistency were the dominant creditworthiness signals.
  - Fairness audit found no demographic disparities under the synthetic data's independence assumption.
  - num: The optimal classification threshold was 0.151, substantially below the conventional 0.5.
  - Engineered composite features provided no measurable predictive improvement over raw features.
key_figures_tables:
  - Table 1: 16 raw behavioral features with domain and rationale → Features cover mobile money, airtime, savings, credit, social, and payment domains.
  - Table 3: Model comparison test set performance → Tuned XGBoost ROC-AUC 0.714 vs logistic regression 0.713.
  - Table 5: Fairness disparity ratios → All groups exceed 0.80 for selection rate, TPR, and precision.
  - Table 6: Selection rate disparity ratios across thresholds → All ratios exceed 0.80, with West Africa lowest at 0.818.
  - Figure 7: Global feature importance by mean SHAP value → Wallet balance trend dominates by factor of 1.74.
key_equations:
  - equation: f(x_i) = ∅_0 + ∑_{j=1}^p ∅_{ij}
    explanation: SHAP decomposition of prediction into base rate plus feature contributions.
definitions:
  - term: ROC-AUC
    definition: Area under the receiver operating characteristic curve, measuring discrimination ability.
  - term: SHAP
    definition: SHapley Additive exPlanations, a game-theoretic approach for explaining model predictions.
  - term: Demographic parity
    definition: Equal positive prediction rates across demographic groups.
  - term: Equal opportunity
    definition: Equal true positive rates across demographic groups.
  - term: MNAR
    definition: Missing Not At Random, where missingness depends on unobserved values.
critical_citations:
  - "[Björkegren and Grissen, 2018] — Mobile phone metadata predicts loan repayment with AUC ~0.70."
  - "[Suri and Jack, 2016] — Mobile money enables households to navigate income shocks."
  - "[Lundberg and Lee, 2017] — Unified framework for model explanation using SHAP values."
  - "[Chouldechova, 2017] — Impossibility theorem for simultaneously satisfying fairness criteria."
  - "[Baesens et al., 2003] — Ensemble methods outperform single classifiers in credit scoring."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Provides general context on financially excluded populations in Africa, analogous to unbanked Filipinos.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: contextual
      justification: Demonstrates use of behavioral transaction data as a proxy for creditworthiness, relevant to understanding financial behavior.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Mentions temporal dynamics and seasonal patterns as a limitation, not a focus.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Reviews digital credit systems like M-Shwari, Tala, Branch, providing context for PFMS landscape.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly addresses lack of explainability and fairness in existing alternative credit scoring systems.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Framework creates behavioral profiles from mobile money features to predict creditworthiness.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Uses XGBoost and logistic regression to classify borrowers into repayment risk categories.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Core contribution is a predictive model for credit scoring using behavioral data.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: Uses predictive modeling on behavioral features, though not explicitly sequential time-series forecasting.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Framework is for credit scoring, not budget recommendation; methodology could be adapted.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: contextual
      justification: Not directly addressed; threshold tuning relates to cost asymmetry.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Not addressed; focusing on credit classification.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: XGBoost could potentially be used for anomaly detection, but not the focus.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Mentions dashboard for loan officer use, but system is not explicitly mobile-first.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: Dashboard design is for loan officers, not end-user PFMS.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Discusses privacy barriers, data protection acts, and synthetic data for privacy.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Addresses trust through explainability (SHAP) and fairness auditing.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides evaluation protocol including ROC-AUC, fairness metrics, and threshold analysis.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Evaluates XGBoost, logistic regression, and SHAP explainability module.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: contextual
      justification: Evaluation metrics are general ML metrics, not specific to budget recommendation.
  contribution: FairLend-Africa provides a blueprint for Odin's predictive module using behavioral data, demonstrating that XGBoost with SHAP explanations can achieve reasonable predictive performance. The fairness audit framework directly maps to Odin's need for transparent and equitable algorithms, particularly important for a Filipino audience concerned with social justice. The emphasis on explainability supports Odin's design goal of building user trust through interpretable decisions. The open-source implementation and REST API design offer a practical template for Odin's system architecture.
  directly_justifies:
    - "Behavioral financial data from mobile money transactions carries sufficient predictive signal for creditworthiness classification."
    - "XGBoost with SHAP explanations provides a coherent method for predictive modeling and interpretability in personal finance systems."
    - "Systematic fairness auditing using demographic parity and equal opportunity is feasible and necessary for equitable algorithmic systems."
    - "Missing data in financial profiles is informative and requires careful handling (e.g., MNAR with missingness indicators)."
    - "Ablation studies are essential to validate feature engineering contributions."
  limits:
    - "Results are based on synthetic data, not real Filipino behavioral data."
    - "Fairness properties are derived under a synthetic independence assumption that may not hold in real settings."
    - "XGBoost performance matches logistic regression, indicating linear structure in synthetic data; real data may show non-linear benefits."
    - "Engineered composite features provided no measurable lift, questioning their practical value."
    - "SHAP explanations assume feature independence, which may misrepresent contributions when features are correlated."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to Predictive Modeling (6.A, 6.B), Behavioral Profiling (5.A, 5.C), and Evaluation Frameworks (12.A, 12.B) as its core contribution is an ML framework for credit scoring. It also has high relevance to Existing Systems (4.A, 4.B) as it reviews digital credit systems and their limitations, and to Data Privacy (10.A) and User Trust (10.B) as it discusses privacy barriers and uses explainability/fairness. Medium relevance was assigned to Mobile-First Design (9.A) due to the dashboard and Filipino Demographic (1.A, 1.C) due to contextual parallels in financial exclusion. Low or contextual relevance was assigned to Budget Recommendation (7.B, 12.C), Anomaly Detection (8.A, 8.B), and Seasonal Spending (2.B) as the paper does not directly address these topics. Borderline cases included the paper touching on both predictive modeling and fairness, which were both selected as high relevance. The overall relevance is high for Odin's algorithmic and evaluation modules, providing a methodological template.
limitations:
  - "Synthetic dataset not validated on real Filipino mobile money data. [unacknowledged]"
  - "Fairness audit assumes demographic-behavioral independence, which may not hold in real Philippines data."
  - "Engineered features provided no predictive improvement; practical value on real data is unproven."
  - "SHAP explanations assume feature independence, which can misrepresent correlated feature contributions."
  - "System has not been evaluated for temporal stability or concept drift."
  - "Near-identical XGBoost and logistic regression performance suggests primarily linear structure in data; non-linear benefits need real data validation."
remember_this:
  - "Behavioral data achieves 0.714 AUC for credit scoring, matching logistic regression on synthetic data."
  - "Wallet balance trend and savings consistency are the strongest creditworthiness signals."
  - "Fairness audit found no disparities, but this is contingent on synthetic data independence."
  - "SHAP explanations provide interpretability but assume feature independence, a known limitation."
  - "Feature ablation showed engineered features provided no measurable lift in predictive performance."
```
---

## Paper 2: Chowdhury T. et al-2026_summarized.md

**Source File:** `Chowdhury T. et al-2026_summarized.md`

```yaml
paper_id: 10.1016/j.chbr.2025.100926
designation: local-algorithm-specific
title: Modeling financial literacy through explainable machine learning and behavioral segmentation in emerging economies
authors: Chowdhury, T. A.; Chowdhury, M. A. H.; Rahman, M. T.; Ahmed, I.; Ahmed, N.; Tuhin, M. A. I.; Kafy, A. A.
year: 2026
venue: Computers in Human Behavior Reports
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.D
  - 3.A
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 9.A
  - 10.A
  - 10.B
  - 12.A
tldr: Machine learning and behavioral segmentation reveal that institutional trust and digital comfort, not education or demographics, are key predictors of financial literacy in Bangladesh.
problem_and_motivation: Traditional demographic methods fail to capture the complexity of digital financial behavior, hampering effective intervention design in emerging economies. Understanding the complex links between demographic traits, digital access, and financial literacy is crucial for shaping policy. A significant gap exists in using advanced analytics to map financial literacy across behavioral groups for targeted strategies.
approach:
  - Analyzed survey data from 1067 Bangladeshi adults collected via stratified random sampling.
  - Used Random Forest, XGBoost, and Decision Tree models to classify financial literacy.
  - Employed SHAP analysis for model interpretability and feature importance ranking.
  - Applied k-means clustering with silhouette score validation for behavioral segmentation.
  - Addressed class imbalance using SMOTE and ADASYN resampling techniques.
findings:
  - num: XGBoost achieved a macro F1-score of 0.52, a 58% improvement over random guessing.
  - Institutional trust (SHAP importance 0.18) was a stronger predictor than education (0.09).
  - num: Rural participants had 7.3% higher financial literacy scores than urban participants.
  - num: Three behavioral clusters were identified: Digitally Literate Planners (34%), Informally Active but Underskilled (41%), and Digitally Excluded Traditionalists (25%).
  - num: The Digitally Excluded Traditionalists cluster had a mean financial knowledge score of 3.1/10 and a trust score of 1.9/5.
  - Weak correlations (r < 0.10) were found between financial knowledge and actual behaviors.
  - Gender-education interaction effects were significant only for women, benefiting from tertiary education.
  - Formal education level did not significantly impact literacy scores across the sample.
key_figures_tables:
  - Figure 9: Model performance comparison → XGBoost outperforms Random Forest and Decision Tree.
  - Figure 11: SHAP feature importance → Income, trust, and age are top predictors.
  - Figure 13: Behavioral profiles across clusters → Distinct patterns in digital engagement and formal banking use.
  - Table 1: Cluster profiles and interventions → Differentiated strategies for each behavioral segment.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: ML
    definition: Machine Learning
  - term: SHAP
    definition: SHapley Additive exPlanations
  - term: SMOTE
    definition: Synthetic Minority Over-sampling Technique
  - term: ADASYN
    definition: Adaptive Synthetic Sampling
  - term: BDT
    definition: Bangladeshi Taka
  - term: ROC
    definition: Receiver Operating Characteristic
  - term: AUC
    definition: Area Under the Curve
  - term: PCA
    definition: Principal Component Analysis
critical_citations:
  - "[Lusardi & Messy, 2023] — Foundational framework for financial literacy assessment."
  - "[Koskelainen et al., 2023] — Digital age financial literacy research agenda."
  - "[Singh et al., 2020] — Application of AI in behavioral finance."
  - "[Choung et al., 2023] — Digital financial literacy and financial well-being."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Provides a framework for analyzing demographic groups in emerging economies.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: contextual
      justification: Discusses income levels and digital access relevant to financial structures.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly analyzes financial behaviors and literacy using ML and clustering.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Identifies behavioral clusters and informal practices like ROSCAs.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: medium
      justification: The concept of behavioral segments and informal financial networks is analogous to understanding spending cycles.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Segmentation analysis can inform how to design categories for different user types.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: The core contribution is the creation of behavioral profiles via clustering.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: Identifies transitional segments (Cluster 1) relevant to profile dynamics.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Uses Random Forest and XGBoost to classify literacy and behavioral segments.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Employs ML models to predict financial literacy outcomes.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: The study is cross-sectional and does not forecast sequential spending data.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Behavioral segments show varying budgeting and savings capabilities.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: The segmentation framework can be used to tailor budget recommendations.
    - code: 9.A
      name: Mobile‑First Design Principles and Rationale
      relevance: medium
      justification: Digital comfort and access are key predictors, informing mobile design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Institutional trust is a key predictor, which relates to data privacy concerns.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Trust in institutions is a primary finding, with importance value of 0.18.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Evaluates ML model performance with F1-score and other metrics.
  contribution: This study provides a validated machine learning framework for predicting financial literacy in emerging economies, directly applicable to Odin's user profiling and behavioral segmentation modules. Its demonstration of SHAP analysis offers a methodological blueprint for making Odin's algorithmic decisions interpretable and trustworthy for Filipino users. The identification of institutional trust and digital comfort as top predictors has direct implications for Odin's design and user onboarding, emphasizing trust-building over demographic assumptions.
  directly_justifies:
    - "Financial literacy is best predicted by institutional trust and digital comfort, not formal education."
    - "Behavioral segmentation reveals three distinct user groups requiring differentiated interventions."
    - "Machine learning models like XGBoost provide meaningful, interpretable improvements for user classification."
    - "Rural users demonstrate financial literacy levels comparable to or exceeding urban users."
  limits:
    - "Self-reported data may introduce social desirability and recall bias."
    - "Digital-only survey excludes the most financially vulnerable populations without internet access."
    - "Cross-sectional design prevents causal inferences about literacy development."
    - "Unmeasured psychological traits like financial anxiety may improve model accuracy."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to Behavioral Profiling & Classification (Domain 5) due to its core use of k-means clustering and ML classification. It was also highly relevant to Data Privacy & User Trust (Domain 10) because institutional trust emerged as a top predictor (SHAP 0.18). Relevance was assigned to Filipino Cultural Context (Domain 2) due to the discussion of informal financial practices like ROSCAs, which are culturally analogous. For Spending Forecasting (Domain 6), relevance was lower as the study is cross-sectional, but the predictive modeling approach (6.A) is directly relevant. For Budget Recommendation (Domain 7), the segmentation provides a basis for tailored strategies (7.B). The study did not directly address Anomaly Detection (Domain 8), Savings & Debt Management (Domain 13) in detail, or System Evaluation (Domain 12) beyond model metrics, so these were considered low or contextual. Overall, the paper is highly relevant for informing Odin's user profiling, personalization algorithms, and trust-building mechanisms.
limitations:
  - "Self-reported data may be subject to social desirability bias. [unacknowledged]"
  - "Online survey method excludes digitally excluded populations, potentially biasing results."
  - "Cross-sectional design prevents causal inference regarding financial literacy development."
  - "The modest F1-score (0.52) indicates that significant variance in literacy remains unexplained by the selected features."
  - "Cultural bias may exist as the survey instrument was adapted from Western frameworks."
remember_this:
  - "Institutional trust (SHAP 0.18) predicts literacy more than education (SHAP 0.09)."
  - "Rural users showed 7.3% higher financial literacy than urban users."
  - "Three behavioral clusters were identified: Planners, Underskilled, and Traditionalists."
  - "Financial knowledge and actual behavior showed negligible correlation (r < 0.10)."
  - "60% of intervention resources should target the Digitally Excluded Traditionalist cluster."
```
---

## Paper 3: Tia et al_summarized.md

**Source File:** `Tia et al_summarized.md`

```yaml
paper_id: 10.48550/arXiv.2505.22125
designation: "local-algorithm-specific"
title: "Sentiment Simulation Using Generative AI Agents"
authors: "Tia, M.; Lanuzo, J. S.; Baltazar, L. R.; Lopez-Relente, M. J.; Quiñones, D. M.; Albia, J."
year: 2026
venue: "Unknown"
odin_topics:
  - "1.A"
  - "5.A"
  - "5.B"
  - "5.C"
  - "12.A"
  - "12.B"
tldr: "A generative AI agent framework with contextualized psychographic profiles achieves up to 92% alignment in replicating survey responses and 81-86% accuracy in sentiment simulation, demonstrating scalable sentiment modeling grounded in behavioral science."
problem_and_motivation: "Traditional sentiment analysis relies on surface linguistic patterns and retrospective data, failing to capture psychological drivers and limiting predictive insight for policy testing and behavioral forecasting. This constrains applications like narrative framing and synthetic focus groups. The paper aims to enable prospective sentiment simulation through psychographically grounded AI agents."
approach:
  - "The framework uses Llama 3.1 70B to instantiate agents from a nationally representative survey of 2,485 Filipino respondents with sociodemographic and psychological variables (personality, values, beliefs, attitudes)."
  - "Two encoding strategies are compared: categorical labels (e.g., Low, Moderate, High) and contextualized narrative descriptions of psychological traits."
  - "Agents are exposed to real-world socio-political and economic scenarios (wage policies, budget transparency, inflation, justice system, political dynasties) with positive or negative framing."
  - "Agents generate sentiment ratings on a 5-point Likert scale accompanied by explanatory rationales, followed by a self-assessment for coherence."
  - "Performance is evaluated using Quadratic Weighted Accuracy (QWA) and statistical tests (Wilcoxon signed-rank, paired t-test, Cohen's d) across repeated trials."
findings:
  - "num: Contextualized encoding achieved 92% alignment in survey replication, significantly outperforming categorical encoding (p<0.0001, Cohen's d=0.70)."
  - "num: Sentiment simulation accuracy ranged from 81% to 86% across five scenarios, with contextualized encoding outperforming categorical in four scenarios."
  - "num: Simulation outputs were stable across repeated trials with standard deviations of 0.17% to 0.51%."
  - "num: Scenario framing did not significantly affect accuracy (p=0.9676, Cohen's d=0.02), indicating robustness."
  - "Contextualized encoding improved accuracy most for political dynasties (+12.8%) and inflation (+6.9%)."
  - "The justice system scenario showed near-identical performance between encodings, suggesting less reliance on psychological traits."
key_figures_tables:
  - "Figure 2: Cumulative distribution of QWA scores by encoding strategy → Contextualized encoding shifts distribution rightward, indicating higher alignment."
  - "Figure 3: Per-agent comparison of QWA scores → Most agents show improved alignment with contextualized encoding."
  - "Figure 4: QWA across positive and negative framing → Scores remain high and similar across framing, with negligible effect size."
  - "Table 3: Sentiment simulation accuracy across scenarios → Contextualized encoding consistently outperforms categorical except in justice system."
key_equations:
  - equation: "w_{ij} = 1 - (d_{ij} / d_{max})^2"
    explanation: "Quadratic weight for ordinal alignment, penalizing distant misclassifications."
  - equation: "t = \\bar{d} / (s_d / \\sqrt{n})"
    explanation: "Paired t-test for comparing framing conditions."
definitions:
  - term: "QWA"
    definition: "Quadratic Weighted Accuracy; metric for ordinal classification that weights errors quadratically by distance."
  - term: "Contextualized encoding"
    definition: "Narrative description of psychological traits integrated into prompts to enhance agent realism."
  - term: "Categorical encoding"
    definition: "Discrete labels (Low, Moderate, High) used to represent psychological variables in prompts."
  - term: "LLM"
    definition: "Large Language Model; here, Llama 3.1 70B used as the generative agent engine."
critical_citations:
  - "[Aher et al., 2023] — LLMs can replicate human subject studies across domains."
  - "[Park et al., 2023] — Generative agents exhibit emergent human-like behavior."
  - "[Park et al., 2024] — LLM-based agents replicate survey responses with ≈85% accuracy."
  - "[Xie et al., 2024] — LLM agents simulate human trust behavior."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "low"
      justification: "Provides nationally representative Filipino sample including young adults but not exclusively young professionals."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Directly demonstrates creating psychographically grounded agent profiles that can inform financial behavioral profiling."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "medium"
      justification: "Agent embodiment from survey data offers a method for initializing profiles in cold-start scenarios."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "The LLM-based sentiment simulation approach could be adapted to classify financial behavioral profiles."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "low"
      justification: "Uses QWA and statistical tests for evaluation, providing general methodological insights for system evaluation."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Evaluates the simulation algorithm with rigorous metrics, applicable to evaluating Odin's algorithmic components."
  contribution: "The paper's agent simulation framework can directly inform Odin's behavioral profiling module (Topic 5.A) by providing a data-driven approach to characterize user attitudes and preferences based on validated psychological constructs. Its use of QWA and statistical significance testing offers a rigorous evaluation framework that can be applied to assess Odin's recommendation and anomaly detection modules (Topics 12.A and 12.B). The robustness of agent responses to framing suggests that such simulations can provide stable baselines for cold-start scenarios (Topic 5.B) where user data is limited. The paper's reliance on nationally representative Filipino data provides contextual grounding for Odin's target demographic (Topic 1.A), though it does not focus exclusively on young professionals."
  directly_justifies:
    - "Contextualized encoding of psychological profiles significantly improves agent-human alignment over categorical encoding."
    - "Agent simulations can replicate survey responses with up to 92% accuracy."
    - "Sentiment simulation accuracy remains stable across alternative scenario framings."
    - "The framework provides a scalable approach for synthetic population simulation in behavioral science."
  limits:
    - "The paper does not address personal finance scenarios or spending behavior specifically."
    - "The framework uses a generic LLM without fine-tuning for financial domain; performance on financial tasks is untested."
    - "The sample includes all adult age groups, not specifically young professionals, limiting direct applicability to Odin's target demographic."
  mapping_rationale: "A systematic scan across all 12 functional domains and associated topic codes was performed. The paper was flagged as relevant to Behavioral Profiling & Classification (topics 5.A, 5.B, 5.C) because it demonstrates the creation of psychographically grounded agent profiles from survey data and uses them to simulate responses, directly supporting the development of behavioral profiles. It also contributes to System Evaluation (topics 12.A, 12.B) due to its rigorous use of QWA and statistical tests for evaluating simulation alignment. Topic 1.A was considered low relevance because while the data is Filipino, it does not focus on young professionals; this borderline case was resolved by including it with low relevance due to demographic overlap. All other domains—Expense Categorization, Spending Forecasting, Budget Recommendation, Anomaly Detection, Mobile-First Design, Data Privacy, User Retention, and Savings & Debt Management—were rejected as the paper does not provide citeable claims or methods that inform Odin's design or implementation in those areas. Overall, the paper's primary relevance to Odin lies in its methodology for behavioral profiling and evaluation, offering a foundation for simulating user attitudes and validating system outputs."
limitations:
  - "The simulation relies on self-reported survey data, which may contain response biases. [unacknowledged]"
  - "The framework does not model temporal dynamics of sentiment or behavior. [unacknowledged]"
  - "Generalizability to other cultural contexts or financial domains is not established."
  - "The use of Llama 3.1 70B may introduce proprietary or computational constraints."
remember_this:
  - "Contextualized psychographic profiles yield 92% alignment in replicating survey responses."
  - "Sentiment simulation accuracy ranges from 81% to 86% across scenarios."
  - "Framing effects are negligible with Cohen's d of 0.02."
  - "The framework provides a scalable method for synthetic population simulation."
  - "Contextualized encoding outperforms categorical in most scenarios, especially for complex issues."
```
---

## Paper 4: Ng et al_summarized.md

**Source File:** `Ng et al_summarized.md`

```yaml
paper_id: "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d"
designation: "local-algorithm-specific"
title: "AI-BAAM: AI-Driven Bank Statement Analytics as Alternative Data for Malaysian MSME Credit Scoring"
authors: "Ng, C. C.; Chu, Z. H.; Lim, J. Y.; Boon, Y. Y.; Low, W. Z.; Tan, J. K."
year: 2026
venue: "ICLR 2026"
odin_topics:
  - "3.A"
  - "4.A"
  - "4.B"
  - "5.A"
  - "5.B"
  - "5.C"
  - "6.A"
  - "10.A"
  - "12.A"
  - "12.B"
  - "13.B"
tldr: "Bank statement transaction data substantially improves MSME credit scoring in Malaysia, with a blended logistic regression model achieving AUROC 0.806, a 24.6% gain over application-only models."
problem_and_motivation: "Traditional credit scoring relies on credit bureau data, excluding MSMEs with thin credit files and creating a MYR90 billion funding gap in Malaysia. Real-time cash flow signals and alternative indicators are overlooked, limiting financial inclusion. There is a need for verifiable, up-to-date financial data to assess creditworthiness for underserved MSMEs."
approach:
  - "Proposes an end-to-end cash flow underwriting workflow with six modules: OCR-based key information and transaction extraction, fraud detection, network analysis, cash flow analysis, and credit scoring."
  - "Constructs the first Malaysian bank statement dataset of 611 MSME loan applicants, with 518 non-default and 93 default cases, split 60/40 for training/validation."
  - "Benchmarks Logistic Regression, Random Forest, Gradient Boosting, and AdaBoost using application information and bank statement-derived features (account behavior and business demographics)."
  - "Uses WOE/IV framework for feature transformation and supervised monotonic binning to handle class imbalance and ensure interpretability."
  - "Evaluates over 30 OCR and LLM configurations for key information and transaction table extraction across six Malaysian banks, comparing with template matching."
  - "Applies CRISP-DM methodology for systematic data mining and model development."
findings:
  - "num: Blended Logistic Regression achieves validation AUROC of 0.806, a 24.6% relative improvement over application-only models."
  - "num: Bank statement features alone yield validation AUROC of 0.763, while application-only yields 0.647."
  - "num: Log growth rate of average balance has the highest IV of 0.484, outperforming the top application feature (business duration, IV 0.213)."
  - "num: Template matching achieves 100% exact match accuracy on key information fields and 98.08% matching NED on transaction tables, with zero API cost and sub-second latency (0.01s key info, 0.11s table)."
  - "num: Rejected applicant analysis shows 96.97% classified as high risk, validating alignment with original underwriting decisions."
key_figures_tables:
  - "Figure 1: Proposed end-to-end workflow for credit scoring using bank statement data → workflow comprises six modules from extraction to scoring."
  - "Figure 2: AUROC across algorithms and feature sets → blended features consistently outperform application-only and bank-only, with LR best at 0.806."
  - "Figure 3: Information Value of features → bank statement features dominate top positions, with log growth rate of average balance highest."
  - "Table 1: Dataset statistics showing 611 applicants with 15.2% default rate → stratified split preserves class distribution."
  - "Table 2: Summary of extraction performance, latency, and cost → template matching achieves best accuracy-efficiency trade-off."
key_equations:
  - equation: "WOE_{jk} = log( (n_{gjk}/N_g) / (n_{bjk}/N_b) )"
    explanation: "Measures relative risk of feature bin jk; positive indicates lower default risk."
  - equation: "IV_j = sum_{k=1}^{K_j} (Dist(g)_{jk} - Dist(b)_{jk}) * WOE_{jk}"
    explanation: "Summarizes predictive power of feature j; higher IV means stronger discrimination."
  - equation: "P(y_i=1|x_i;β) = σ(β_0 + x_i^T β)"
    explanation: "Logistic regression models default probability as sigmoid of linear combination."
definitions:
  - term: "AUROC"
    definition: "Area Under the Receiver Operating Characteristic Curve, measures discrimination ability (0.5 random, 1 perfect)."
  - term: "MSME"
    definition: "Micro, Small, and Medium Enterprises, backbone of Malaysian economy."
  - term: "OCR"
    definition: "Optical Character Recognition, extracts text from images/PDFs."
  - term: "IV"
    definition: "Information Value, quantifies predictive strength of a feature in credit scoring."
  - term: "WOE"
    definition: "Weight of Evidence, log-odds transformation of feature bins for logistic regression."
  - term: "NED"
    definition: "Normalized Edit Distance, measures string similarity (1 perfect match)."
critical_citations:
  - "[Breiman, 2001] — Introduced Random Forest used as ensemble baseline."
  - "[Friedman, 2001] — Gradient Boosting baseline."
  - "[Bunker et al., 2016] — Showed bank statement features improve credit scoring."
  - "[Lessmann et al., 2015] — Benchmarking classification algorithms for credit scoring."
relevance:
  topics:
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "medium"
      justification: "Paper uses NLP to classify transaction descriptions into categories, relevant for expense tracking."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Reviews traditional credit scoring and alternative data, but not PFMS landscape."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Directly identifies shortcomings of bureau-based credit scoring for thin-file MSMEs."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Derives behavioral features from transaction data to profile credit risk."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "high"
      justification: "Addresses cold-start for MSMEs lacking credit history; uses bank statements as alternative."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Compares Logistic Regression, Random Forest, Gradient Boosting, AdaBoost for default classification."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Builds predictive models for default probability using transaction-derived features."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "Discusses data masking, anonymization, compliance with Malaysia's PDPA."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "low"
      justification: "Evaluates model performance via AUROC but not specifically PFMS evaluation frameworks."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Thoroughly evaluates OCR extraction and credit scoring models with multiple metrics."
    - code: "13.B"
      name: "Debt Management in PFMS"
      relevance: "medium"
      justification: "Assesses default risk and repayment capacity, relevant to debt management."
  contribution: "This paper provides a validated approach for transaction categorization (module 3.A) and behavioral profiling (5.A) using bank statement data, which can be adapted for Odin's expense tracking and user profiling. Its evaluation of cold-start strategies (5.B) informs Odin's handling of new users with limited history. The privacy-preserving data handling practices (10.A) align with Odin's requirements for user trust. The benchmarking of algorithmic modules (12.B) offers a template for evaluating Odin's machine learning components."
  directly_justifies:
    - "Bank statement transaction data improves default prediction by 24.6% over application-only data."
    - "Transaction-derived features have higher discriminatory power than static application information."
    - "Template matching outperforms LLM-based extraction for structured financial documents in terms of accuracy, latency, and cost."
    - "Rejected applicant analysis validates that bank statement features capture genuine credit risk signals."
  limits:
    - "Dataset is limited to 611 applications from a single Malaysian consulting firm, potentially limiting generalizability."
    - "Class imbalance (15.2% default) reflects real-world lending but may affect minority class prediction."
    - "Module-level evaluation is constrained by proprietary methods; only overall scoring performance is reported."
    - "Validation across different institutions and economic cycles is needed."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was found highly relevant to the following domains: Expense Categorization (3.A) due to its transaction classification, Limitations of Existing Systems (4.B) for its critique of bureau-based scoring, Behavioral Profiling and Classification (5.A, 5.B, 5.C) for deriving and modeling behavioral features, Predictive Modeling (6.A) for default prediction, Data Privacy (10.A) for ethical handling, and Evaluation of Algorithmic Modules (12.B) for extensive benchmarking. Domains related to budgeting (7.A-D), mobile-first design (9.A-B), and engagement (11.A-B) were considered but rejected as the paper focuses on credit scoring rather than PFMS features. Seasonal spending (2.B, 2.D) and savings goals (13.A, 13.C) were also not addressed. The paper provides strong justification for using transaction data to address cold-start issues and improve predictive accuracy, with moderate relevance to debt management (13.B). Overall, the paper offers actionable insights for Odin's core modules in behavioral modeling and evaluation, while its privacy practices and rejection analysis provide supporting evidence for trust and robustness."
limitations:
  - "Dataset size is limited (611 applicants) from a single institution."
  - "Class imbalance is inherent but not addressed with resampling techniques."
  - "Module-level assessment is constrained by proprietary methods; only overall scoring performance is reported."
  - "Generalizability across different banks and regions is not tested."
  - "Focus on credit scoring rather than full PFMS features like savings goals or budgeting. [unacknowledged]"
remember_this:
  - "Blended bank statement and application features yield AUROC 0.806, 24.6% gain over application-only."
  - "Bank statement features dominate predictive power, with log growth of average balance IV 0.484."
  - "Template matching outperforms LLM-based extraction with 100% accuracy and zero cost."
  - "Transaction data provides strong signals for cold-start credit assessment of thin-file MSMEs."
  - "Privacy-preserving data handling is critical for adoption in financial systems."
```
---

## Paper 5: Noel et al_summarized.md

**Source File:** `Noel et al_summarized.md`

```yaml
paper_id: 10.3389/frai.2026.1705245
designation: local-algorithm-specific
title: Small LLMs can be good coldstart recommenders
authors: Noel, J.; Monterola, C.; Tan, D. S.
year: 2026
venue: Frontiers in Artificial Intelligence
odin_topics:
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 8.C
  - 9.A
  - 12.B
tldr: Fine-tuned small language models with under 2B parameters using LoRA achieve competitive or superior sequential recommendation performance compared to standard models, especially in cold-start settings.
problem_and_motivation: Standard sequential recommendation models suffer in cold-start scenarios due to limited user interaction histories. Large language models (LLMs) have shown promise for recommendation but are computationally infeasible for most organizations.
approach:
  - Fine-tuned two small open-source LLMs, Danube-1.8B and Gemma-2B, using Low-Rank Adaptation (LoRA) for sequential recommendation.
  - The models were evaluated on the MovieLens10M and Yoochoose-clicks datasets, using only item IDs from short interaction sequences of length 5.
  - LoRA was used to update less than 0.5% of the original model parameters, enabling fine-tuning on consumer-grade GPUs.
  - Converted sequential interaction data into prompts for causal language modeling.
  - Compared performance against GRU4Rec, SASRec, and BERT4Rec in a cold-start scenario.
findings:
  - num: Fine-tuned LLMs achieved up to 8.7% higher HitRate@1 compared to the best baseline (Danube vs. BERT4Rec on MovieLens).
  - LLMs predict item IDs that are textually and numerically closer to input sequence IDs, as measured by lower average Hamming distance and deviation.
  - The tokenization of numeric item IDs into digit-level tokens creates a numeric bias that the LLMs exploit for predictions.
  - Despite digit-level bias, the LLMs also learn meaningful sequential co-occurrence patterns beyond simple numeric proximity.
  - LLMs scale independently of catalog size as they avoid a separate, linearly growing item-embedding matrix.
key_figures_tables:
  - Table 4: Comparison of HitRate@1, average distance, and deviation → LLMs outperform baselines on both datasets in cold-start settings.
  - Table 5: Example of tokenization for Gemma and Danube → Item IDs are tokenized into digit-level tokens, not atomic symbols.
  - Table 6: Sample correct predictions not numerically close to inputs → LLMs learn non-trivial sequential patterns beyond numeric bias.
  - Table 7: Results of different input sequence lengths on MovieLens → Unlike GRU4Rec, small LLM performance does not improve with longer histories.
key_equations:
  - equation: \max_{\theta} \sum_{(x,y) \in Z} \sum_{t=1}^{|y|} \log(P_\theta(y_t | x, y_{<t}))
    explanation: Standard causal language modeling objective for LLM fine-tuning.
  - equation: \max_{\Phi} \sum_{(x,y) \in Z} \sum_{t=1}^{|y|} \log(P_{\theta+\Phi}(y_t | x, y_{<t}))
    explanation: LoRA fine-tuning objective updating only low-rank matrix Phi.
definitions:
  - term: LoRA
    definition: Low-Rank Adaptation, a parameter-efficient fine-tuning technique that adds trainable low-rank matrices to a pretrained model.
  - term: Cold-start
    definition: A recommendation scenario where new users or items have limited historical interaction data.
  - term: Sequential Recommendation
    definition: Predicting the next item a user will interact with based on their sequence of past interactions.
critical_citations:
  - "[Singer et al., 2024] — Defines the Danube-1.8B small LLM architecture."
  - "[Team et al., 2024] — Defines the Gemma-2B small LLM architecture."
  - "[Hu et al., 2022] — Introduces LoRA used for efficient fine-tuning."
  - "[Hidasi et al., 2016] — Defines the GRU4Rec baseline model."
  - "[Wang-Cheng Kang, 2018] — Defines the SASRec baseline model."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: Provides a general context for cold-start problems in user profiling.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Shows that small LLMs can classify user behavior from short sequences, akin to profile classification.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Demonstrates a predictive modeling approach (LLM-based) for sequential spending-like data.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Evaluates LLMs as forecasting algorithms for sequential item prediction, analogous to spending prediction.
    - code: 8.C
      name: Cold‑Start Baseline Strategies for Anomaly Detection
      relevance: high
      justification: The paper's core focus on cold-start recommendation directly informs baseline strategies for anomaly detection.
    - code: 9.A
      name: Mobile‑First Design Principles and Rationale
      relevance: medium
      justification: The use of small, efficient models aligns with the computational constraints of mobile deployment.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: The paper provides a direct evaluation framework (HitRate, tokenization analysis) for an algorithmic module (LLM-based recommender).
  contribution: "This paper directly validates the use of small LLMs (under 2B parameters) for the sequential recommendation task, a key component of Odin's forecasting module. It shows that these models, fine-tuned with LoRA, are computationally feasible on consumer hardware, which supports Odin's mobile-first design. The findings that LLMs perform well in cold-start scenarios offer a concrete strategy for Odin's cold-start baselines for both recommendation and anomaly detection."
  directly_justifies:
    - "Fine-tuned small LLMs under 2B parameters can be effective for sequential recommendation."
    - "LoRA enables efficient fine-tuning of LLMs with less than 0.5% of parameters trainable."
    - "LLMs avoid a separate item-embedding matrix, maintaining a constant memory footprint regardless of catalog size."
    - "Short historical sequences (length 5) are sufficient for small LLMs to make good predictions in a cold-start setting."
  limits:
    - "The study only uses two datasets (MovieLens, Yoochoose) which may not fully represent financial spending data. [unacknowledged]"
    - "The LLM's reliance on numeric ID tokenization may be a limitation if item IDs are not numeric or sequentially ordered. [unacknowledged]"
    - "Inference latency (34-59 ms/token) is slower than traditional models like GRU4Rec, which could be a constraint for real-time mobile applications. [acknowledged]"
    - "The study does not compare with state-of-the-art large LLMs (e.g., PaLM, Llama-3) to benchmark performance loss."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant primarily for the 'Spending Forecasting' (6.A, 6.B) domain due to its focus on sequential prediction, the 'Behavioral Profiling & Classification' (5.A, 5.C) domain for its cold-start recommendation which is analogous to user profile classification, and the 'Anomaly Detection' (8.C) domain for its direct treatment of the cold-start problem. It also touches on 'Mobile‑First Design' (9.A) due to the efficiency of the small models and 'System Evaluation' (12.B) for its empirical methodology. The paper was rejected for domains like 'Expense Categorization' (3.A) as it does not deal with categorizing items, and 'Data Privacy & User Trust' (10.A) as it offers no insights on those topics. Its relevance is high for the cold-start aspects of forecasting and anomaly detection, and medium for informing mobile deployment and evaluation frameworks."
limitations:
  - "Generalizability to non-numeric or non-sequential item IDs is not discussed. [unacknowledged]"
  - "The computational cost of fine-tuning is not compared to the cost of training baselines from scratch. [unacknowledged]"
  - "The study does not explore the use of LLMs for feature augmentation or dataset augmentation."
remember_this:
  - "Small LLMs can outperform standard recommenders in cold-start settings."
  - "LoRA fine-tuning updates less than 0.5% of small LLM parameters."
  - "LLMs maintain a fixed memory footprint independent of item catalog size."
  - "Small LLMs achieved up to 8.7% higher HitRate@1 on MovieLens."
  - "Short interaction histories are sufficient for effective cold-start predictions."
```
---

## Paper 6: Yang & Zhang_summarized.md

**Source File:** `Yang & Zhang_summarized.md`

```yaml
paper_id: 10.70393/6a6574626d.333932
designation: local-algorithm-specific
title: Offline Conservative RL for Transaction Authorization: Smartly Balancing Fraud Risk and Customer Friction
authors: Yang, X.; Zhang, Y.
year: 2026
venue: Journal of Economic Theory and Business Management
odin_topics:
  - 3.A
  - 4.A
  - 4.B
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 7.D
  - 8.A
  - 8.B
  - 12.A
  - 12.B
  - 12.C
tldr: Offline conservative RL jointly optimizes fraud loss, manual review operations, and customer friction in transaction authorization, outperforming cost-sensitive supervised baselines.
problem_and_motivation: Existing credit authorization methods either rely on static rules or ignore customer friction, treating risk and user impact as a binary trade-off. There is no unified framework to co-optimize fraud loss, operational review burden, and false-positive delays in real time while using only historical data. This study addresses the gap by formalizing transaction authorization as an offline MDP with a cost-sensitive objective.
approach:
  - Data source: 284,807 transactions from a public credit-card dataset with 492 fraud cases (0.172%), split chronologically into 70/15/15%.
  - State space: concatenates PCA-transformed transaction features V1–V28, Time, and Amount, with optional cluster and macro factors.
  - Action space: {Approve, Review, Decline}, with a cost-sensitive reward penalizing false positives, false negatives, and manual review operations.
  - Algorithm: Conservative Q-Learning (CQL) with a deep Q-network to mitigate out-of-distribution overestimation in offline learning.
  - Evaluation: compared against supervised classifiers (LightGBM, Logistic Regression) under asymmetric cost metrics, using cost reduction and precision-recall.
findings:
  - num: CQL-based policy achieves superior fraud recall and balanced accuracy relative to supervised baselines under asymmetric cost conditions.
  - The cost-sensitive RL framework directly minimizes expected misclassification cost L = cfp × FP + cfn × FN.
  - Offline RL eliminates the need for costly real-time experimentation while preserving operational safety and regulatory compliance.
  - V14, V17, and transaction Amount show significant predictive power, enabling the RL agent to detect high-risk patterns overlooked by conventional classifiers.
  - The learned policy adapts to contextual transaction signals, dynamically adjusting authorization thresholds based on risk.
key_figures_tables:
  - Figure 2: class distribution showing extreme imbalance with 0.172% fraud → motivates cost-sensitive evaluation and chronologically splits.
  - Figure 3: density of transactions over time by class → diurnal cycles justify including time-of-day in the RL state.
  - Figure 4: total amount aggregated by hour → fraud exhibits narrower and more irregular peaks, supporting time-based state features.
  - Figure 5: total amount of fraud transactions by hour → bimodal fraud amount distribution suggests micro-fraud and high-stakes fraud archetypes.
  - Figure 6: amount by class raw vs log-scaled boxplots → fraudulent transactions show wider variance and higher median amounts.
  - Figure 7: scatter plot of amount vs time → fraud appears as isolated high-value spikes, indicating non-stationary patterns.
  - Table 1: dataset overview with 284,807 records and 492 frauds → confirms extreme imbalance and motivates cost-sensitive modeling.
key_equations:
  - equation: C = c_{fp} × FP + c_{fn} × FN
    explanation: Total cost from false positives and false negatives.
  - equation: R_t = -(c_{fp} × FP_t × c_{fn} × FN_t)
    explanation: Reward is negative total cost for each transaction.
  - equation: L = c_{fp} × FP × c_{fn} × FN
    explanation: Expected misclassification cost minimized by the RL policy.
definitions:
  - term: CQL
    definition: Conservative Q-Learning, an offline RL algorithm that penalizes overestimation of unseen actions.
  - term: MDP
    definition: Markov Decision Process, a mathematical framework for sequential decision-making under uncertainty.
  - term: FP
    definition: False positive, a legitimate transaction incorrectly rejected or reviewed.
  - term: FN
    definition: False negative, a fraudulent transaction incorrectly approved.
  - term: PCA
    definition: Principal Component Analysis, used to anonymize and transform original transaction features.
critical_citations:
  - "[Khraishi & Okhrati, 2022] — Offline RL for dynamic credit pricing baseline."
  - "[So & Thomas, 2011] — MDP framework for credit card profitability modeling."
  - "[Kumar et al., 2020] — Conservative Q-Learning foundational algorithm."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: Contextual framing of transaction-level decision categories but not explicit expense categorization.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Surveys traditional credit authorization and pricing systems, situating RL as an alternative.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly identifies myopic risk-based and profit-based pricing limitations and transaction-level gaps.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Uses supervised score models (LR/LGBM) as state features for sequential policy learning.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Offline RL (CQL) learns sequential authorization policies from chronological transaction data.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: General framing of cost-sensitive optimization but not specific to budget allocation.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Tangential; focuses on authorization, not budget recommendations.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: medium
      justification: Customer friction and review actions relate to handling infeasibility constraints in decision-making.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Fraud detection is the primary anomaly detection use case addressed by the policy.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: CQL is evaluated as an anomaly detection algorithm for rare fraudulent transactions.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses cost-sensitive metrics and confusion matrices for offline evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Directly evaluates the CQL algorithmic module against supervised baselines.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: low
      justification: Not directly applicable to budget recommendation evaluation.
  contribution: "This paper contributes a cost-sensitive offline RL framework (CQL) for transaction authorization that directly integrates with Odin's anomaly detection module by providing a learning-based policy for fraud flagging. It also informs Odin's constraint-handling mechanisms by modeling action feasibility (approve/review/decline) and user friction as explicit costs, which parallels infeasibility handling in budget allocation. The multi-objective reward design offers a template for Odin to combine financial risk, operational burden, and user experience into a single optimization objective."
  directly_justifies:
    - "Offline RL can learn transaction-level policies without online experimentation, suitable for PFMS deployment."
    - "Cost-sensitive reward design enables explicit trade-off between fraud risk and customer friction."
    - "CQL mitigates out-of-distribution overestimation, improving policy robustness in offline settings."
    - "Transaction amount and PCA components V14, V17 are key features for fraud detection."
  limits:
    - "Dataset is from European cardholders, limiting generalizability to Filipino spending behavior and cultural contexts."
    - "No explicit Philippine data or institution involvement beyond the first author's affiliation."
    - "Does not address budget recommendation, savings, or debt management domains directly."
  mapping_rationale: "The systematic scan across all 12 functional domains flagged the following as relevant: Existing Systems & Gaps (4.A, 4.B) at medium/high for its critique of traditional models; Predictive Modeling (6.A, 6.B) at medium/high for its use of sequential spending data; Anomaly Detection (8.A, 8.B) at high as fraud detection is the core application; and Algorithm Evaluation (12.A, 12.B, 12.C) at medium/high for its benchmarking approach. Budget Recommendation (7.A, 7.B, 7.D) was considered but assigned low/medium because the paper focuses on authorization rather than allocation, though customer friction constraints are relevant to 7.D. Expense Categorization (3.A) and Behavioral Profiling (5.A–5.C) were rejected as contextual-only because they are not directly addressed. Filipino Cultural Context domains (2.A–2.D) were considered but the dataset is European, so relevance is minimal except for the general concept of user friction (2.D). Savings and Debt Management (13.A–13.C) and Mobile-First Design (9.A, 9.B) were considered and rejected due to no direct content. Overall, the paper provides strong methodological justification for Anomaly Detection and Evaluation modules, and moderate support for Understanding Existing Systems."
limitations:
  - "Dataset is European, not Filipino, limiting cultural and spending-behavior generalizability. [unacknowledged]"
  - "No online deployment or A/B testing validation; results are offline only. [unacknowledged]"
  - "Action labels (e.g., review) are not present in the dataset; actions are policy decisions modeled in evaluation only. [unacknowledged]"
  - "Does not address interpretability of the RL policy beyond feature importance, which may be insufficient for regulatory compliance."
remember_this:
  - "CQL-based policy achieves superior fraud recall compared to supervised baselines under asymmetric costs."
  - "Offline RL eliminates the need for real-time experimentation in transaction authorization."
  - "V14, V17, and Amount are the most predictive features for fraud detection in this dataset."
  - "Cost-sensitive reward design allows direct balancing of fraud risk and customer friction."
  - "Chronological splitting is essential to emulate sequential deployment and avoid data leakage."
```
---

## Paper 7: Delena et al_summarized.md

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

## Paper 8: de Goma et al_summarized.md

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

## Paper 9: Hassine et al_summarized.md

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

## Paper 10: Hartomo et al_summarized.md

**Source File:** `Hartomo et al_summarized.md`

```yaml
paper_id: 10.1109/ACCESS.2025.3541878
designation: local-algorithm-specific
title: A Novel Weighted Loss TabTransformer Integrating Explainable AI for Imbalanced Credit Risk Datasets
authors: Hartomo, K. D.; Arthur, C.; Nataliani, Y.
year: 2025
venue: IEEE Access
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 8.C
  - 10.A
  - 10.B
tldr: Weighted loss and TabTransformer improve credit risk classification on imbalanced datasets, with SHAP providing transparent feature importance for fairness and trust.
problem_and_motivation: Financial institutions struggle with information asymmetry when assessing creditworthiness, particularly for MSMEs lacking audited statements. This creates higher perceived risks and hinders financial inclusivity. Existing AI methods suffer from data imbalance and limited transparency, eroding trust and making it difficult to provide fair and efficient credit evaluations.
approach:
  - The framework combines a TabTransformer model with a weighted loss function to handle class imbalance.
  - Class weights are calculated inversely proportional to class frequencies to penalize misclassifications of minority classes more heavily.
  - The model is applied to two datasets: the BISAID dataset with 2,563 records and the German Credit dataset with 1,000 records.
  - Performance is evaluated using accuracy, precision, recall, F2-score, and AUC, with a focus on improvements for minority classes.
  - SHAP (SHapley Additive exPlanations) is used post-modeling for model-agnostic interpretability, providing local and global feature importance.
  - The TabTransformer architecture uses embeddings for categorical features and multi-head attention to capture complex interactions.
findings:
  - num: On the BISAID dataset, weighted loss increased overall accuracy from 86.35% to 89.27%.
  - num: AUC for minority classes in BISAID improved from 0.88 to 0.91 for one class and from 0.86 to 0.91 for another.
  - num: For the German Credit dataset, accuracy improved from 93% to 95%.
  - num: Minority class precision and recall in German Credit rose from 0.85 and 0.93 to 0.88 and 0.97, respectively.
  - Weighted loss effectively addresses class imbalance without degrading performance on the majority class.
  - SHAP identified "Financing Needs" and "Credit Amount" as the most influential predictors in the respective datasets.
  - The proposed framework mitigates bias and enhances model performance while providing actionable insights.
  - The weighted loss function helps produce an equitable and transparent credit evaluation system.
key_figures_tables:
  - Figure 1: Proposed framework utilizing TabTransformer and weighted loss for credit risk prediction and explainability → Provides an overview of the end-to-end pipeline.
  - Figure 5: Train vs Val loss for BISAID dataset before and after weighted loss → Shows stabilization of training after applying weighted loss.
  - Figure 7: ROC curves comparing weighted and non-weighted multiclass model performance on BISAID database → Demonstrates improved AUC for minority classes.
  - Figure 9: Feature importance analysis with SHAP on BISAID dataset → Identifies "Financing Needs" as the most critical feature.
  - Table 5: Classification metrics comparison before and after applying weighted loss on BISAID dataset → Details performance gains for each class.
key_equations:
  - equation: w_i = N / N_i
    explanation: Weight for class i inversely proportional to its sample count.
  - equation: L = -Σ w_i * y_i * log(ŷ_i)
    explanation: Weighted cross-entropy loss for class imbalance mitigation.
  - equation: φ_i = Σ_{S⊆N\{i}} (|S|!(|N|-|S|-1)!)/|N|! [f(S∪{i}) - f(S)]
    explanation: Shapley value for feature i, quantifying its contribution.
definitions:
  - term: TabTransformer
    definition: Transformer architecture adapted for tabular data with embeddings for categorical features.
  - term: XAI
    definition: Explainable Artificial Intelligence techniques for model interpretability.
  - term: SHAP
    definition: SHapley Additive exPlanations, a game-theoretic approach for feature attribution.
  - term: Weighted Loss
    definition: Loss function with class-specific weights to address data imbalance.
critical_citations:
  - "[Huang et al., 2020] — Introduced TabTransformer for tabular data."
  - "[Lundberg & Lee, 2017] — Proposed SHAP for unified model interpretation."
  - "[Ahadian et al., 2024] — Applied weighted loss for maize disease classification."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: The paper classifies borrowers by credit risk, which can inform financial behavioral profiling.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: The study uses existing data but does not explicitly address cold-start scenarios.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: This paper evaluates a deep learning classification approach (TabTransformer) for credit risk prediction.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: The paper uses TabTransformer for predictive modeling on credit risk datasets.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: contextual
      justification: While the data is tabular and not explicitly sequential, the methods are relevant for forecasting.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: The paper focuses on classification, not anomaly detection, but the methods are related.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: The paper does not directly apply anomaly detection algorithms.
    - code: 8.C
      name: Cold‑Start Baseline Strategies for Anomaly Detection
      relevance: contextual
      justification: The paper does not address cold-start problems in anomaly detection.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: The paper discusses data from official sources but does not focus on privacy/security mechanisms.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: By using SHAP to provide transparency, the paper directly addresses user trust and interpretability in financial systems.
  contribution: "This work provides a robust methodology for imbalanced credit risk classification using a weighted TabTransformer, which can be directly adapted for Odin's expense anomaly detection and behavioral classification modules. The use of SHAP aligns with Odin's need for explainable AI to build user trust and provide transparent justifications for financial decisions. The approach's focus on fairness for minority classes is critical for ensuring equitable financial management features in Odin. Furthermore, the evaluation framework and performance metrics offer a template for assessing Odin's predictive modules."
  directly_justifies:
    - "Weighted loss significantly improves recall for minority classes, which is essential for detecting risky spending patterns."
    - "SHAP provides a clear and human-readable explanation of feature importance for credit risk decisions."
    - "The TabTransformer model handles a mix of categorical and numerical tabular data, similar to Odin's data structure."
  limits:
    - "The paper primarily focuses on credit risk, not on general personal finance spending behavior."
    - "The datasets used are relatively small and may not generalize to diverse user populations."
    - "The work does not address the dynamic or sequential nature of spending data in a PFMS." [unacknowledged]
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant for 'Behavioral Profiling & Classification' (specifically 5.C) and 'Spending Forecasting' (6.A) due to its deep learning classification approach for credit risk. It was also deemed highly relevant for 'Data Privacy & User Trust' (10.B) because it employs XAI to enhance transparency and trust. Medium relevance was assigned to 5.A (Financial Behavioral Profiles) as the paper classifies borrowers, which can inform behavioral profiles, and low relevance to several other topics like 5.B (Cold-Start Problem) and 8.A (Anomaly Detection) as they are not directly addressed. Borderline cases included 6.B (Forecasting Algorithms) and 8.A (Anomaly Detection), which were considered contextual or low because the paper is not focused on sequential or anomaly detection. The paper's core contribution in algorithmic classification and fairness justifies its inclusion in the relevant topics listed. Overall, the paper provides strong support for Odin's need for accurate, fair, and transparent predictive models for financial behavior analysis and user trust."
limitations:
  - "The model is evaluated on two specific credit datasets, which may not represent the full diversity of Filipino young professionals."
  - "The paper does not discuss the computational cost or deployment constraints of the TabTransformer in a mobile-first setting." [unacknowledged]
  - "The weighted loss approach is static and does not adapt to changing class distributions over time." [unacknowledged]
remember_this:
  - "Weighted loss improved accuracy from 86% to 89% on the BISAID dataset."
  - "SHAP enables transparent and fair credit risk predictions."
  - "The TabTransformer effectively handles mixed tabular data types."
  - "Weighted loss prevents model bias towards the majority class."
  - "AUC for minority classes improved from 0.88 to 0.91 with weighted loss."
```
---

## Paper 11: Pandiin & Matias_summarized.md

**Source File:** `Pandiin & Matias_summarized.md`

```yaml
paper_id: "10.54610/aeis.v1i1.178"
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

## Paper 12: Onsay & Rabajante-2025_summarized.md

**Source File:** `Onsay & Rabajante-2025_summarized.md`

```yaml
paper_id: 10.1016/j.socimp.2025.100138
designation: local-algorithm-specific
title: From data to decision: Alleviating poverty and promoting development through measuring the unmeasurable economic numbers
authors: Onsay, E. A.; Rabajante, J. F.
year: 2025
venue: Societal Impacts
odin_topics:
  - 5.C
  - 6.A
  - 6.B
  - 8.B
  - 12.A
  - 12.B
tldr: Integrates machine learning with econometrics to predict multidimensional poverty and generate localized policy targeting tools from CBMS data.
problem_and_motivation: Traditional poverty measurement relies on costly, time-intensive surveys, and current regression-based analyses often lack predictive precision. There is a critical need for more accurate, localized, and data-driven tools to inform poverty alleviation policies in the Philippines.
approach:
  - Used Community-Based Monitoring System (CBMS) data from 34 localities in Camarines Sur, Philippines.
  - Combined descriptive, diagnostic, and multidimensional statistical analysis with econometric models like logit/probit regression.
  - Applied machine learning regression (Random Forest, XGBoost, CatBoost, LightGBM, SVR) and classification (Random Forest, AdaBoost, SVM, etc.) algorithms.
  - Conducted 273 regression and 468 classification ensemble runs to predict poverty incidence, gap, and severity.
  - Generated policy maps and a three-round classification system to prioritize interventions for the most vulnerable populations.
findings:
  - num: Random Forest classification achieved a prediction accuracy of 92.60–98.00%.
  - num: The proposed model reduced traditional survey and data processing costs by up to 70%.
  - Random Forest regressor and classifier outperformed other models for poverty prediction.
  - A set of 27 multidimensional socioeconomic variables were identified as significant predictors of poverty.
  - Distinct poverty configurations exist across different localities and indigenous tribes, requiring context-specific policies.
key_figures_tables:
  - Figure 1: Sample results of statistical and econometric analyses showing poverty proportions by locality → Poverty outcomes vary significantly and are influenced by multidimensional variables.
  - Figure 2: Results of machine learning regression and classification → Random Forest models show superior performance and consistency.
  - Table 1: Theory of Change, hypotheses, and results chain → Provides a framework linking inputs, processes, outputs, and impact indicators.
  - Table 2: Proposed intervention programs and policy initiatives → Details targeted policies for nutrition, housing, education, and livelihood.
  - Table 3: Multidimensional poverty indicators and target areas → Maps indicators to recommended interventions and priority groups.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: CBMS
    definition: Community-Based Monitoring System, a data collection system for local poverty and socioeconomic indicators.
  - term: Random Forest
    definition: An ensemble learning method that constructs multiple decision trees and outputs the average or mode of predictions.
  - term: XGBoost
    definition: eXtreme Gradient Boosting, an optimized algorithm for gradient boosting known for speed and performance.
critical_citations:
  - "[Onsay & Rabajante, 2024] — Details the dataset and initial models used for poverty prediction."
  - "[Sobreviñas, 2020] — Provides a framework for analyzing chronic and transient poverty using CBMS data."
  - "[Haughton & Khandker, 2009] — Standard reference for poverty and inequality measurement techniques."
relevance:
  topics:
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: contextual
      justification: Applies classification algorithms to categorize poverty levels, analogous to profiling financial behavior.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly employs predictive machine learning models (Random Forest, XGBoost) for forecasting socioeconomic outcomes.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: contextual
      justification: Uses similar forecasting algorithms (Random Forest, etc.) though applied to poverty data, not spending sequences.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: Classification models used could be adapted for anomaly detection, though not the paper's focus.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a clear evaluation framework using accuracy, cost reduction, and policy targeting metrics.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Systematically evaluates and compares 7 regression and 12 classification algorithms.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: low
      justification: The paper profiles poverty and vulnerability, which are analogous but not directly about financial behavior profiles.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: low
      justification: Policy recommendations are similar to budget allocation strategies in a public policy context.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: Related to financial management for poverty alleviation, but not specifically about savings goals.
  contribution: This paper provides a robust methodological framework for predictive classification that can inform Odin's behavioral profiling and forecasting modules. Its use of ensemble methods and systematic evaluation offers a blueprint for Odin's algorithmic architecture. The focus on localized targeting and cost-efficiency is directly relevant to Odin's design as a PFMS for Filipino users. The paper's emphasis on data-driven policy recommendations justifies Odin's core function of providing actionable financial insights.
  directly_justifies:
    - "Machine learning models, specifically Random Forest, can predict financial states with up to 98% accuracy."
    - "A systematic comparison of multiple algorithms is essential for selecting the optimal module."
    - "A three-round classification system can prioritize users based on vulnerability."
    - "Using local data is critical for developing context-specific financial tools."
  limits:
    - "The study focuses on poverty prediction, not personal spending, so direct applicability to Odin's core tasks is limited."
    - "The dataset is regional (Bicol), which may limit generalizability to other Filipino demographics."
  mapping_rationale: A systematic scan of the 12 functional domains revealed that the paper's primary relevance lies in its algorithmic and evaluative contributions. The domains of Spending Forecasting (6.A, 6.B) and System Evaluation (12.A, 12.B) were flagged as having high relevance because the paper directly compares and validates machine learning models for prediction, which is analogous to Odin's forecasting needs. The Behavioral Profiling domain (5.C) is contextually relevant due to its classification approach. Other domains like Expense Categorization (3.A-C) and Mobile-First Design (9.A-B) were considered and rejected as the paper does not address them. Similarly, domains like Data Privacy (10) and Engagement (11) were rejected for lacking discussion. The financial domains (1, 2, 7, 13) were rejected as the paper's scope is macroeconomic poverty, not personal finance. The final assessment is that the paper offers high-value methodological and evaluation strategies that can be adapted for Odin's algorithmic core.
limitations:
  - "Focuses on macroeconomic poverty, not personal financial behavior."
  - "Models are region-specific and may not generalize to the broader Filipino young professional demographic."
  - "Does not address real-time data processing or mobile application constraints."
  - "The ethical statement notes that ethical clearance was not required, but using socioeconomic data in a PFMS requires careful privacy handling [unacknowledged]."
remember_this:
  - "Random Forest achieved 92.60-98.00% accuracy in classifying poverty states."
  - "Systematic comparison of 12 classification algorithms is essential for performance validation."
  - "Using 27 socioeconomic variables improved prediction and policy targeting."
  - "The framework enables localized policy targeting and cost-efficient data analysis."
```
---

## Paper 13: Alunen et al_summarized.md

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

## Paper 14: Ram & Agoylo_summarized.md

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

## Paper 15: Carillo & Serra_summarized.md

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

## Paper 16: Cabrera et al_summarized.md

**Source File:** `Cabrera et al_summarized.md`

```yaml
paper_id: 10.1057/s41599-025-05205-z
designation: local-algorithm-specific
title: Plastic to apparel: an analysis of sustainable purchasing intention using a machine learning ensemble
authors: Cabrera, C. A. L.; Ong, A. K. S.; Diaz, J. F. T.; Cahigas, M. M. L.; Gumasing, M. J. J.
year: 2025
venue: Humanities and Social Sciences Communications
odin_topics:
  - 1.A
  - 1.C
  - 2.A
  - 2.D
  - 5.A
  - 5.B
  - 5.C
tldr: Customer perceived value and perceived behavioral control are the primary factors influencing Filipino consumers' purchase intentions for apparel made from recycled plastic.
problem_and_motivation: Despite the environmental benefits of recycled apparel, a significant gap exists in understanding the key drivers of sustainable purchasing behavior. This is particularly relevant in the Philippines, a major contributor to ocean plastic pollution, yet behavioral intentions remain underexplored. The study addresses this gap by establishing the Sustainability Theory of Planned Behavior (STPB) model.
approach:
  - A survey of 500 Filipino respondents was conducted to evaluate eight factors from the STPB model on purchase intention for recycled plastic apparel.
  - The study employed a machine learning ensemble comprising Random Forest Classifier (RFC) and Artificial Neural Network (ANN) for analysis.
  - Data preprocessing involved feature selection and correlation analysis to validate and aggregate the data.
  - RFC was optimized with parameters including tree depth, criterion (gini/entropy), and splitter choice across multiple iterations.
  - ANN optimization was performed with varying activation functions (tanh, relu, elu), optimizers, and hidden layer nodes over 150 epochs.
findings:
  - num: RFC achieved a 92% accuracy rate with the optimum parameters of gini and best at a 90:10 training-testing ratio.
  - num: ANN achieved a 91% R-squared test value with the Elu activation function at 30 hidden layer nodes.
  - Customer Perceived Value (CPV) is the most important factor, with a 100% normalized importance score.
  - Perceived Behavioral Control (PBC), Attitude (AT), and Subjective Norm (SN) closely follow CPV with 94.7%, 87.4%, and 82.6% importance, respectively.
  - Perceived Authority Support (PAS) had the lowest importance among factors at 71.5%.
key_figures_tables:
  - Figure 3: Theoretical framework of the STPB model with eight factors → Framework for the study's hypothesis build-up.
  - Table 2: Demographic profile of the 500 respondents (e.g., age, gender, income) → Provides context for the sample population.
  - Table 3: Random Forest Classifier results showing accuracy rates for different parameters and splits → Demonstrates the best model configuration (92% at 90:10 split with gini).
  - Figure 4: Optimum classification model with RFC → Shows the decision tree for predicting purchase intention.
  - Figure 5: Optimum ANN classification model → Visualizes the neural network architecture with 30 nodes.
key_equations:
  - equation: f(x) = x if x > 0 else α(e^x - 1)
    explanation: The Elu activation function used for the ANN hidden layer.
definitions:
  - term: STPB
    definition: Sustainability Theory of Planned Behavior, an extension of TPB integrating all sustainability domains.
  - term: RFC
    definition: Random Forest Classifier, an ensemble machine learning algorithm for classification.
  - term: ANN
    definition: Artificial Neural Network, a machine learning algorithm with connected nodes for classification.
  - term: CPV
    definition: Customer Perceived Value, a customer's holistic evaluation of a product's utility.
  - term: PBC
    definition: Perceived Behavioral Control, the perception of how easy or challenging it is to perform an activity.
  - term: PECC
    definition: Perceived Economic Concern, a customer's inclination to allocate additional funds towards sustainable products.
  - term: PENC
    definition: Perceived Environmental Concern, a measurement of how a person perceives effects on the environment.
  - term: PAS
    definition: Perceived Authority Support, an individual's comprehension of support from authoritative entities.
critical_citations:
  - "[German et al., 2022] — Established the PEPB model used as the base for STPB."
  - "[Ajzen, 1991] — The foundational TPB theory is cited for the behavioral framework."
  - "[Ong et al., 2023] — Justified the inclusion of PECC as a necessary variable."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: The study's sample is Filipino, but not specifically focused on young professionals.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: low
      justification: While it assesses purchasing behavior, it does not specifically analyze the financial management behavior of Filipino young professionals.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: The paper touches on Filipino environmental context, but not on specific cultural financial practices like 'utang'.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: The study mentions purchase frequency intervals but does not link them to Filipino-specific spending cycles or occasions like 'fiestas' or '13th-month pay'.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: low
      justification: The study classifies behavioral intentions using machine learning but does not create distinct, actionable financial profiles for personal finance management.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: The study's machine learning model classifies behavior but does not address how to handle a new user with no history (cold-start).
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: The study uses RFC and ANN for classification, which is a relevant methodology but applied to sustainable purchasing, not directly to financial behavior profiling.
  contribution: The study contributes a validated STPB framework and a machine learning ensemble model (RFC and ANN) that can be adapted by Odin to analyze user financial behavior. The identification of CPV and PBC as the most significant drivers of intention provides a direct justification for Odin's expense categorization and user engagement modules to emphasize perceived value and user control over finances. The high accuracy of the RFC model at 92% supports the use of similar classification algorithms for Odin's behavioral profiling and anomaly detection modules.
  directly_justifies:
    - Customer Perceived Value (CPV) is the most significant driver of behavioral intention.
    - Perceived Behavioral Control is the second most significant factor influencing intention.
    - Machine learning ensembles like RFC and ANN provide high accuracy (92% and 91%) for analyzing complex behavioral relationships.
    - Authority support (PAS) is the least influential factor, suggesting a focus on peer influence and personal value over institutional endorsement.
  limits:
    - The study's sample is skewed towards younger demographics (55.4% aged 18-25) and urban residents (80.6%).
    - The model does not differentiate between online and in-person purchase intentions.
    - Demographic data was not directly correlated with specific behavioral outcomes.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was conducted. The paper was flagged as most relevant to the 'Behavioral Profiling & Classification' domain, as it employs classification algorithms (RFC, ANN) to analyze behavioral factors. Topics 5.A, 5.B, and 5.C were selected with 'medium' relevance because the paper classifies purchase intention, which is a form of behavioral profiling, though not specifically for financial management within a PFMS. The 'Filipino Cultural Context' domain was considered, with topic 2.A and 2.D receiving 'low' or 'contextual' relevance because the study uses Filipino respondents but doesn't explicitly analyze culturally specific spending practices like 'utang' or 'fiesta' cycles. Domains like 'Expense Categorization', 'Spending Forecasting', 'Budget Recommendation', 'Anomaly Detection', and 'Mobile-First Design' were rejected as the paper does not address these specific technical or design aspects of a PFMS. The overall relevance to Odin is moderate, providing methodological justification for using machine learning in behavioral analysis rather than direct technical implementation for its core functions.
limitations:
  - "The sample is heavily skewed towards younger demographics (18-25 years old) and urban areas. [unacknowledged]"
  - "The study does not differentiate between online and in-person purchase intentions for sustainable apparel. [unacknowledged]"
  - "The research did not correlate demographic data with specific behavioral outcomes to provide a comprehensive overview. [unacknowledged]"
  - "The model's findings are based on stated intentions, which may not perfectly reflect actual purchasing behavior."
remember_this:
  - Customer Perceived Value is the most critical factor for sustainable purchase intention.
  - Perceived Behavioral Control and Attitude are the second and third most important factors.
  - RFC achieved a 92% accuracy rate in predicting behavioral intention.
  - Authority support was the least influential factor on sustainable apparel purchase decisions.
  - The STPB framework can holistically assess sustainable consumption behavior.
```
---

## Paper 17: Peykani et al_summarized.md

**Source File:** `Peykani et al_summarized.md`

```yaml
paper_id: 10.3390/math13030368
designation: local-algorithm-specific
title: Evaluation of Cost-Sensitive Learning Models in Forecasting Business Failure of Capital Market Firms
authors: Peykani, P.; Peymany Foroushany, M.; Tanasescu, C.; Sargolzaei, M.; Kamyabfar, H.
year: 2025
venue: Mathematics
odin_topics:
  - 4.A
  - 5.A
  - 6.A
  - 8.A
  - 8.B
  - 12.A
tldr: Cost-sensitive machine learning models, particularly CatBoost, effectively identify failing businesses in an imbalanced Iranian capital market dataset, achieving high sensitivity but low precision.
problem_and_motivation: Credit datasets are inherently imbalanced, causing standard machine learning models to achieve high accuracy but low sensitivity in identifying failing firms, which is costly. Existing cost-sensitive methods have been underexplored for business failure prediction, especially in emerging markets like Iran.
approach:
  - Applied CorrOV-CSEn, a correlation-based oversampling with cost-sensitive ensemble learning, to an Iranian capital market dataset of 2987 training and 1240 test instances from 2015-2022.
  - Evaluated six algorithms: Multi-Layer Perceptron (MLP), Random Forest, Gradient Boosting, XGBoost, AdaBoost, and CatBoost.
  - Used nine financial and stock price-based features derived from Altman and Carton & Hofer models.
  - Compared CorrOV-CSEn performance against the standard SMOTE resampling method.
  - Assessed models using sensitivity, precision, and F1-score, with statistical significance evaluated via the Friedman–Nemenyi test.
findings:
  - num: CorrOV-CSEn CatBoost achieved the highest sensitivity of 0.909 on the test data.
  - num: SMOTE CatBoost achieved the highest F1-score of 0.733 and precision of 0.717.
  - num: Across four datasets, CatBoost consistently showed perfect sensitivity (1.00) in two subsets.
  - All models exhibited relatively low precision when using the CorrOV-CSEn method.
  - The Friedman test revealed CatBoost had significantly higher sensitivity but significantly lower precision than AdaBoost and Gradient Boosting.
  - X1 (Net Working Capital/Total Assets) was the most important feature across all models except MLP.
key_figures_tables:
  - Table 2: Dataset features and their formulas used for prediction → Defines the nine financial and stock-price features.
  - Table 6: Performance metrics for CorrOV-CSEn and SMOTE across all models → Shows CatBoost's sensitivity advantage and precision trade-off.
  - Table 7: Model performance across four data subsets → Highlights variability and CatBoost's consistent high sensitivity.
  - Figure 2: Percentage of firms failing under Article 141 from 2015 to 2022 → Shows the yearly proportion of failed firms in the dataset.
  - Figure 3: Feature importance across models → Indicates X1 as the most influential feature for most algorithms.
key_equations:
  - equation: "Sensitivity = TP / (TP + FN)"
    explanation: "Measures the model's ability to identify actual failures."
  - equation: "Precision = TP / (TP + FP)"
    explanation: "Measures accuracy of positive predictions for failures."
  - equation: "F1Score = (2 * Precision * Sensitivity) / (Precision + Sensitivity)"
    explanation: "Harmonic mean balancing precision and sensitivity."
  - equation: "X2_F = 12 / (nk(k+1)) * sum(R_i^2) - 3n(k+1)"
    explanation: "Friedman statistic for comparing multiple model performances."
definitions:
  - term: Business Failure
    definition: "A firm facing significant operational challenges, broader than default or bankruptcy."
  - term: CorrOV-CSEn
    definition: "Correlation-based Oversampling aided Cost-Sensitive Ensemble learning technique."
  - term: Sensitivity
    definition: "True positive rate, measuring success in identifying failing firms."
  - term: Precision
    definition: "Proportion of predicted failures that are actual failures."
  - term: Article 141
    definition: "Iranian regulation requiring recovery plans for companies with losses exceeding equity."
critical_citations:
  - "[Barboza et al., 2017] — Comprehensive baseline for ML in bankruptcy prediction."
  - "[Devi et al., 2022] — Introduced the CorrOV-CSEn method used in this study."
  - "[Breiman, 2001] — Foundational work for the Random Forest algorithm."
  - "[Chen & Guestrin, 2016] — Foundational work for the XGBoost algorithm."
  - "[Friedman, 1937] — Provides the statistical test for model comparison."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: "Provides examples of ML models used for credit risk in capital markets."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: "Classifies firms into 'failed' and 'healthy', analogous to financial behavior profiling."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: "Demonstrates the application of predictive models (ML) for financial risk."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: "Directly models the detection of failing (anomalous) firms using cost-sensitive learning."
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: "Evaluates multiple ML algorithms (XGBoost, Random Forest, CatBoost) specifically for detecting rare failure events."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: "Uses sensitivity, precision, F1-score, and the Friedman–Nemenyi test for a rigorous model comparison."
  contribution: "This paper justifies Odin's use of cost-sensitive learning algorithms for anomaly detection (8.B) by demonstrating their effectiveness in identifying rare financial distress events. It provides a comparative framework (12.A) for evaluating such algorithms using metrics like sensitivity and precision. The study's focus on detecting 'business failure' directly supports Odin's core functionality of identifying anomalous spending patterns. Furthermore, its emphasis on high sensitivity over raw accuracy validates the design goal of prioritizing the detection of financially risky behavior in users. The findings also highlight the critical trade-off between sensitivity and precision, informing Odin's algorithm selection and performance-tuning strategies."
  directly_justifies:
    - "Cost-sensitive learning is necessary to effectively detect rare but costly financial anomalies in imbalanced datasets."
    - "CatBoost can achieve superior sensitivity in detecting failure cases, making it suitable for anomaly detection modules."
    - "Feature importance analysis can identify the most predictive variables for financial risk assessment."
    - "There is a significant performance trade-off between sensitivity and precision in anomaly detection models."
  limits:
    - "The study focuses on corporate business failure, not individual spending behavior, limiting direct applicability to PFMS."
    - "Precision was notably low for high-sensitivity models like CatBoost, suggesting a high false-positive rate."
    - "The findings are based on the Iranian capital market, which has unique political and economic conditions, limiting generalizability."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domain of 'Anomaly Detection' (8.A, 8.B) was flagged as highly relevant because the core task of the paper is identifying failing firms, which is analogous to detecting anomalies in a financial system. The 'Existing Systems & Gaps' (4.A) domain was considered contextual as the paper provides a landscape of ML models in finance. The 'Behavioral Profiling' (5.A) domain was assigned medium relevance because the binary classification of firms parallels profiling user financial behavior. 'Predictive Modeling' (6.A) was also medium for the same reason. The 'System Evaluation' (12.A) domain was deemed medium due to its detailed performance comparison framework. Topics related to Filipino cultural context (2.A-D), expense categorization (3.A-C), and others like mobile-first design (9.A-B) were rejected as they are not addressed. The paper is highly relevant for its contributions to algorithmic approaches for anomaly detection and the quantitative evaluation of such methods."
limitations:
  - "Data is from a single country's capital market, limiting generalizability to individual PFMS users."
  - "Precision was very low for CatBoost, which is a significant limitation for practical use."
  - "The paper does not account for the potential impact of the COVID-19 pandemic on the dataset."
  - "Models were not optimized with hyperparameter tuning (e.g., grid search). [unacknowledged]"
  - "The study uses 'business failure' under Article 141, not actual default, which may not perfectly reflect financial distress. [unacknowledged]"
remember_this:
  - "Cost-sensitive learning is critical for detecting rare financial anomalies."
  - "CatBoost achieved 90.9% sensitivity but at only 20.1% precision."
  - "A trade-off exists between maximizing detection and minimizing false alarms."
  - "Feature X1 was the most important predictor across all models."
  - "SMOTE improved precision but often reduced sensitivity compared to CorrOV-CSEn."
```
---

## Paper 18: Aribe_summarized.md

**Source File:** `Aribe_summarized.md`

```yaml
paper_id: 10.14445/22315381/IJETT-V73I10P104
designation: local-algorithm-specific
title: Spiking Neural Networks: The Future of Brain-Inspired Computing
authors: Aribe Jr., S. G.
year: 2025
venue: International Journal of Engineering Trends and Technology
odin_topics:
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
  - 12.C
tldr: Surrogate gradient-trained spiking neural networks achieve accuracy within 1-2% of artificial neural networks while reducing energy consumption by up to 97%.
problem_and_motivation: Traditional artificial neural networks are extremely energy inefficient and biologically unrealistic, creating a bottleneck for mobile and edge computing applications. Existing studies examine SNN training paradigms in isolation, obscuring the practical tradeoffs between accuracy, latency, energy, and convergence that matter for deployment.
approach:
  - A unified evaluation protocol was established comparing surrogate-trained, ANN-to-SNN converted, and STDP-based SNNs across five metrics.
  - Experiments used Brian2 for surrogate gradient SNNs, BindsNET for conversion pipelines, and NEST for large-scale spiking models.
  - LIF neuron model with τ=20 ms, Vth=1.0, and 5 ms refractory period served as the default configuration.
  - Datasets included MNIST with rate coding, DVS128 Gesture with temporal coding, and SHD/SSC audio datasets.
  - Training was performed on an NVIDIA RTX GPU with 32 GB RAM across 20 epochs with five independent runs.
findings:
  - num: Surrogate gradient SNNs achieved 97.8% accuracy on MNIST and 85.7% on CIFAR-10, within 1-2% of ANN baselines.
  - num: Surrogate gradient SNNs converged by the 20th epoch with training loss dropping from 0.9 to 0.44.
  - num: STDP-based SNNs consumed as low as 5 millijoules per inference, the lowest energy among all models.
  - num: Converted SNNs cut energy use by 90% compared to ANNs while maintaining competitive accuracy.
  - num: Surrogate gradient SNNs achieved inference latency as low as 10 milliseconds.
  - Surrogate gradient-trained models offered the best balance between accuracy, latency, and convergence speed.
  - STDP-based SNNs exhibited slower convergence, stabilizing around 0.75 training loss after 20 epochs.
  - ANNs achieved 99.2% accuracy on MNIST and 92.3% on CIFAR-10 but consumed 200 mJ per inference.
  - Event-driven computation in SNNs enables real-time processing with on-the-fly spike-based responses.
  - Neuromorphic platforms like Intel Loihi and IBM TrueNorth demonstrate large-scale SNN feasibility with ultra-low power.
key_figures_tables:
  - Table 1: SNN performance summary comparing accuracy and energy → SNNs match ANN accuracy with 90-97% lower energy.
  - Table 2: Latency comparison across models → Surrogate gradient SNNs achieve lowest latency at 10 ms.
  - Table 3: Energy efficiency summary → STDP-based SNNs consume only 5 mJ per inference.
  - Table 4: Training loss across epochs → Surrogate gradient SNNs show fastest convergence.
  - Figure 1: LIF neuron model illustrates membrane potential dynamics → LIF provides efficient spiking behavior for SNNs.
  - Figure 2: Conceptual SNN architecture shows input encoding, spike processing, and output decoding → SNNs mimic biological asynchronous computation.
  - Figure 3: Performance and energy comparison → SNNs offer 90-97% energy savings over ANNs.
  - Figure 4: Latency comparison → Surrogate gradient SNNs achieve 10 ms inference time.
  - Figure 5: Energy and spike count comparison → STDP-based SNNs have lowest energy and spike counts.
  - Figure 6: Convergence behavior → Surrogate gradient SNNs converge fastest by epoch 20.
  - Figure 7: Learning curves → Surrogate gradient SNNs show steepest accuracy gains and stable optimization.
key_equations:
  - equation: Accuracy = (Number of Correct Predictions / Total Number of Predictions) × 100%
    explanation: Standard classification performance metric.
  - equation: Latency = t_decision - t_0
    explanation: Time from input to output decision.
  - equation: Total Spikes = ∑_{i=1}^N ∑_{t=1}^T s_i(t)
    explanation: Aggregate spike count across neurons and timesteps.
  - equation: E_total = E_spike * S + E_synapse * C
    explanation: Total energy as sum of spike and synaptic operations.
  - equation: Energy Efficiency = Accuracy / Energy Consumption (Joules)
    explanation: Normalized energy efficiency metric.
  - equation: Convergence Time = Epoch where Accuracy ≥ Target Accuracy
    explanation: Epoch count to reach target accuracy.
definitions:
  - term: SNN
    definition: Spiking Neural Network, a neural network that uses discrete spike events for computation.
  - term: LIF
    definition: Leaky Integrate-and-Fire, a neuron model that accumulates input current and fires when threshold is reached.
  - term: STDP
    definition: Spike-Timing Dependent Plasticity, a biologically inspired unsupervised learning rule based on spike timing.
  - term: ANN
    definition: Artificial Neural Network, traditional neural network using continuous-valued signals.
  - term: CNN
    definition: Convolutional Neural Network, a neural network for spatial feature extraction.
  - term: DVS
    definition: Dynamic Vision Sensor, an event-based camera that captures brightness changes as spikes.
  - term: SHD
    definition: Spiking Heidelberg Digits, a spike-based audio digit recognition dataset.
  - term: SSC
    definition: Spiking Speech Commands, a spike-based speech recognition dataset.
  - term: NEST
    definition: Neural Simulation Tool, a simulator for spiking neural networks.
  - term: BindsNET
    definition: A Python library for spiking neural networks built on PyTorch.
critical_citations:
  - "[Roy et al., 2019] — Foundational SNN neuromorphic computing survey."
  - "[Davies et al., 2018] — Loihi neuromorphic processor enabling low-power SNNs."
  - "[Neftci et al., 2019] — Surrogate gradient learning for SNN training."
  - "[Diehl et al., 2015] — ANN-to-SNN conversion for high-accuracy spiking networks."
  - "[Merolla et al., 2014] — IBM TrueNorth million-neuron neuromorphic chip."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: contextual
      justification: Provides modeling frameworks for predictive systems using SNNs.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: contextual
      justification: SNNs' temporal processing capabilities relevant to sequential data forecasting.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: low
      justification: Mentions optimization concepts but not directly applied to budgeting.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Not directly about budget recommendation systems.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: SNN event-driven processing could inform anomaly detection approaches.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: Algorithmic discussion may be transferable to spending anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a multi-dimensional evaluation framework applicable to Odin.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Directly compares multiple algorithmic paradigms using unified metrics.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Offers methodological insights for evaluating algorithmic components.
  contribution: "This paper provides a unified multi-metric evaluation protocol for comparing neural network paradigms across accuracy, latency, energy, spike count, and convergence. The framework directly informs Odin's evaluation strategy for algorithmic modules in spending forecasting and anomaly detection. The emphasis on energy efficiency and real-time performance aligns with Odin's mobile-first deployment constraints. The findings on training convergence and hardware tradeoffs guide selection criteria for Odin's predictive models. The comprehensive comparison methodology can be adapted to validate Odin's budget recommendation and anomaly detection components."
  directly_justifies:
    - "Evaluation of algorithmic modules requires multi-dimensional metrics beyond accuracy alone."
    - "Energy efficiency is a critical constraint for mobile-first personal finance applications."
    - "Real-time inference latency below 10 ms is achievable with optimized spiking models."
    - "Surrogate gradient training offers the best balance between performance and efficiency."
    - "Unified evaluation protocols enable principled model selection for deployment."
  limits:
    - "Findings rely primarily on benchmark datasets which may not reflect real-world financial data complexity."
    - "Hardware-specific results are drawn from literature rather than direct implementation on Odin's target platforms."
    - "Hyperparameter sensitivity in surrogate-gradient training requires further exploration for financial applications."
    - "The applicability of SNN architectures to structured financial transaction data is not directly validated."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was conducted. The most relevant domain is System Evaluation (12.A, 12.B, 12.C) due to the paper's multi-dimensional comparison framework and unified evaluation protocol. The Predictive Modeling (6.A, 6.B) and Anomaly Detection (8.A, 8.B) domains are flagged as contextual because SNN temporal processing and event-driven computation could inform these Odin modules, though the paper does not directly address financial data. The Budgeting Strategies (7.A, 7.B) domain is considered low relevance since the paper focuses on classification rather than optimization or allocation. Other domains including Filipino Cultural Context, Expense Categorization, Mobile Design, Data Privacy, User Retention, and Savings/Debt Management were rejected because the paper makes no mention of cultural practices, user interfaces, privacy concerns, engagement dynamics, or financial goal management. The paper's primary contribution is algorithmic evaluation methodology, making it most valuable for Odin's system evaluation and algorithmic module validation."
limitations:
  - "Evaluation relies primarily on benchmark datasets which may not fully capture real-world complexity. [unacknowledged]"
  - "Hardware-specific results are drawn from literature rather than direct implementation. [unacknowledged]"
  - "Hyperparameter sensitivity in surrogate-gradient training requires further exploration."
  - "Convergence instability in STDP highlights ongoing training challenges."
  - "No unified standard for model evaluation or neuromorphic implementation exists."
  - "Limited accessibility and scalability of neuromorphic chips restrict practical deployment."
  - "Scalability on high-dimensional tasks and robustness under noisy conditions remain unexplored. [unacknowledged]"
remember_this:
  - "Surrogate gradient SNNs achieve 97.8% accuracy with 10 ms latency."
  - "SNNs reduce energy consumption by 90-97% compared to ANNs."
  - "STDP-based SNNs consume only 5 millijoules per inference."
  - "Surrogate gradient SNNs converge fastest by epoch 20."
  - "Multi-metric evaluation reveals critical accuracy-latency-energy tradeoffs."
```
---

## Paper 19: Mariano & Monreal_summarized.md

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

## Paper 20: Santiago_summarized.md

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

## Paper 21: Gomez et al_summarized.md

**Source File:** `Gomez et al_summarized.md`

```yaml
paper_id: "d9b7e3c4-8f6a-4d2e-b1c3-9f8e7d6c5b4a"
designation: "local-algorithm-specific"
title: "Modeling Personality Traits by Predicting Questionnaire Responses as an Alternative Approach to Filipino Automatic Personality Recognition"
authors: "Gomez, A. P. I.; Kahil, I. D.; Ong, S. V. N.; Tighe, E. P."
year: 2024
venue: "Unknown"
odin_topics:
  - "5.C"
  - "5.B"
  - "12.B"
  - "1.A"
  - "2.A"
tldr: "Predicting BFI item responses from Filipino Twitter text and aggregating to estimate trait scores achieved low accuracy, with hierarchical classification slightly improving Conscientiousness but not Extraversion."
problem_and_motivation: "Direct automatic personality recognition from Filipino social media text yields poor results due to cultural linguistic nuances and data scarcity. An alternative item-based prediction approach may better account for these intricacies, but its effectiveness remains unproven."
approach:
  - "Used the PagkataoKo dataset of 2,168 Filipino Twitter users with BFI responses."
  - "Preprocessed tweets with tokenization (Pinoy TweetTokenizer) and extracted n-grams."
  - "Applied TF-IDF and term occurrence with min_df/max_df filtering, then chi-square or PCA for feature reduction."
  - "Trained logistic regression, SVM, and XGBoost classifiers per BFI item in a direct and a two-phase hierarchical scheme."
  - "Aggregated item predictions to estimate Extraversion and Conscientiousness trait scores and evaluated with RMSE and R2."
findings:
  - "num: Best item-level test F1 reached 0.4334 for Extraversion and 0.5416 for Conscientiousness."
  - "All item models underperformed majority class baselines, indicating poor classification accuracy."
  - "Hierarchical classification improved item-level broad classification for Conscientiousness but not Extraversion."
  - "num: Trait-level R2 for Extraversion was 0.1240, and for Conscientiousness was -0.2273 with the original pipeline."
  - "Data imbalance and overfitting were evident, as validation F1 scores were near 1.0 while test scores were low."
key_figures_tables:
  - "Table 2: Best Extraversion item models achieved test F1 0.3196–0.4334, favoring term occurrence → performance is modest and inconsistent."
  - "Table 3: Best Conscientiousness item models varied widely, test F1 0.2426–0.5416 → some items show better classification but others perform poorly."
  - "Table 4: Proposed approach for Extraversion had test RMSE 0.6714 and R2 0.1240 → slightly better than baselines but still weak."
  - "Table 5: Proposed approach for Conscientiousness had test RMSE 0.6760 and negative R2 -0.2273 → worse than linear regression baseline."
  - "Figure 2: Comparison of Extraversion item models vs majority class baselines → all item models underperform baselines."
  - "Figure 3: Comparison of Conscientiousness item models vs baselines → item models underperform baselines."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "BFI"
    definition: "Big Five Inventory, a personality questionnaire measuring five traits."
  - term: "APR"
    definition: "Automatic Personality Recognition, inferring personality from digital data."
  - term: "TF-IDF"
    definition: "Term Frequency-Inverse Document Frequency, a text feature weighting method."
  - term: "SVM"
    definition: "Support Vector Machine, a supervised learning algorithm."
  - term: "XGBoost"
    definition: "Extreme Gradient Boosting, an ensemble tree-based algorithm."
  - term: "PCA"
    definition: "Principal Component Analysis, a dimensionality reduction technique."
critical_citations:
  - "[Tighe and Cheng, 2018] — Found Extraversion and Conscientiousness easiest to model."
  - "[Tighe et al., 2022] — Curated the PagkataoKo dataset used in this study."
  - "[Mushtaq and Kumar, 2022] — Overview of text-based APR developments."
relevance:
  topics:
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "This paper evaluates classification models (LR, SVM, XGBoost) for personality trait prediction, which directly parallels financial behavioral profile classification."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "medium"
      justification: "Discusses data scarcity and cold-start challenges in modeling Filipino user profiles, relevant to profile initialization in PFMS."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Provides a detailed evaluation framework (F1, RMSE, R2) for item-level and trait-level prediction models, applicable to PFMS module evaluation."
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "contextual"
      justification: "Uses Filipino social media users, primarily young adults (mean age 21), providing demographic context but not specific to professionals."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "low"
      justification: "Mentions Filipino linguistic nuances and multilingualism but does not address financial practices, only personality recognition."
  contribution: "This paper contributes a methodological framework for item-based personality prediction that can be adapted to financial behavior profiling in Odin. Its evaluation of classification models on sparse Filipino text data informs the design of behavioral profile classifiers. The hierarchical classification scheme offers a way to handle ordinal response data, which could be applied to user preference or constraint tiers. The identified challenges of data imbalance and overfitting provide cautionary insights for Odin's cold-start and profile dynamics modules."
  directly_justifies:
    - "Machine learning classifiers can be trained on Filipino social media text to predict user responses."
    - "Hierarchical classification can improve accuracy for ordinal data by grouping similar classes first."
    - "Data imbalance severely degrades model performance, requiring careful class weighting or oversampling."
    - "Feature selection and reduction are critical for managing high-dimensional text data."
  limits:
    - "The paper focuses on personality, not financial behavior, so direct transferability is limited."
    - "Performance metrics are low, suggesting the approach is not yet viable for production use."
    - "Only two of five Big Five traits were tested; applicability to other traits is unknown."
  mapping_rationale: "A systematic scan of all 12 functional domains was performed. Domains related to expense categorization (3), existing systems (4), forecasting (6), budgeting (7), anomaly detection (8), mobile design (9), privacy (10), retention (11), and savings/debt (13) were rejected as the paper does not address financial topics. The behavioral profiling domain (5) was flagged as highly relevant, specifically 5.C (classification approaches) because the paper compares multiple classifiers for predicting user attributes from text, and 5.B (profile dynamics) for its discussion of cold-start and data scarcity. The system evaluation domain (12.B) was considered medium relevance because the paper includes a thorough evaluation of algorithmic modules (item-level and trait-level). Filipino cultural context domains (1.A, 2.A) were considered contextual/low due to the use of Filipino data and mention of linguistic nuances, but the content is not financial. Overall, the paper's relevance to Odin lies in its methodological contributions to behavioral profile classification and evaluation, albeit in a non-financial domain."
limitations:
  - "The study only used Twitter data; generalizability to other social media or text sources is untested. [unacknowledged]"
  - "Only Extraversion and Conscientiousness were modeled; other Big Five traits were not explored."
  - "The best models still performed worse than simple baselines, indicating limited practical utility."
  - "Data imbalance was not addressed with resampling or cost-sensitive learning."
  - "The hierarchical classification improved broad-level but not fine-grained accuracy."
remember_this:
  - "Predicting BFI item responses from text and aggregating yields low accuracy for personality traits."
  - "Hierarchical classification improved Conscientiousness item-level broad classification but not Extraversion."
  - "All item models underperformed majority class baselines, indicating severe data imbalance issues."
  - "Trait-level R2 scores were near zero or negative, showing the approach poorly explains variance."
  - "Data imbalance and overfitting were major challenges, requiring better balancing strategies."
```
---

## Paper 22: Almonteros et al_summarized.md

**Source File:** `Almonteros et al_summarized.md`

```yaml
paper_id: "10.12785/ijcds/150151"
designation: "local-algorithm-specific"
title: "Forecasting Students’ Success To Graduate Using Predictive Analytics"
authors: "Almonteros, J. R.; Matias, J. B.; Pitao, J. V. S."
year: 2024
venue: "International Journal of Computing and Digital Systems"
odin_topics:
  - "1.A"
  - "1.B"
  - "1.C"
  - "2.A"
  - "3.A"
  - "4.A"
  - "4.B"
  - "5.A"
  - "5.B"
  - "5.C"
  - "6.A"
  - "6.B"
  - "7.D"
  - "8.B"
  - "12.A"
  - "12.B"
  - "12.C"
tldr: "Genetic algorithm feature selection with logistic regression predicts student on-time graduation with 79% accuracy and 71% AUC using pre-admission data from a Philippine university."
problem_and_motivation: "Existing student success prediction studies identify many potential predictors but lack consensus on which are most effective for a given context. Real-world data from Caraga State University, a Philippine institution implementing K-12, offers an opportunity to determine optimal predictors and models to support admissions policy. The current admission process based primarily on entrance exam scores may be insufficient to forecast graduation success."
approach:
  - "Dataset of 2,207 student records from Caraga State University containing demographics, prior academic achievement (SHS track, GPA), and college admission test scores."
  - "Missing numerical values imputed using KNN, categorical values using mode; all nominal categorical features encoded via binary encoding to prevent ordinal bias."
  - "Feature selection methods applied separately: LASSO (L1), Ridge (L2), and Genetic Algorithm (GA) with 150 generations."
  - "Seven classifiers evaluated: Decision Tree, Random Forest, Ensemble, KNN, Logistic Regression, SVM, and Naïve Bayes."
  - "Models trained on 70% of data, tested on 30%; performance measured by accuracy, precision, recall, and AUC."
  - "Best-performing model (Logistic Regression with GA feature selection) deployed as a web application using Django."
findings:
  - "num: Genetic Algorithm feature selection with Logistic Regression achieved the highest accuracy (79%) and AUC (71%)."
  - "num: GA selected 33 features and increased AUC by 21% compared to using all 64 features with the same classifier."
  - "num: LASSO (L1) selected only 5 features, resulting in the lowest accuracy (58%) and AUC (50%) with Decision Tree."
  - "Admission exam result was the most frequently selected feature across all methods, followed by sex, mother income, English, math, and GPA."
  - "Abstract score and father income were the least selected features, indicating lower predictive importance."
  - "Ridge (L2) performed better than LASSO (L1) but was outperformed by GA in all classifiers."
  - "SVM with L2 achieved 77% accuracy and 66% AUC, outperforming L2's other classifiers."
  - "Random Forest with all features (NFS) achieved 78% accuracy and 67% AUC, comparable to GA but with lower AUC."
  - "GA feature selection improved AUC for Logistic Regression from 50% to 71%, demonstrating its effectiveness in this context."
key_figures_tables:
  - "Table V: Evaluation metrics for all classifiers across feature selection methods → GA with Logistic Regression yields best accuracy (79%) and AUC (71%)."
  - "Figure 2: Frequency of feature selection across all methods → Admission result is the most selected predictor."
  - "Table VI: Detailed binary-encoded feature selection by L1, L2, and each GA classifier → Shows which specific sub-features were selected."
key_equations:
  - equation: "Errorrate = 1 - (TP+TN) / (TP+TN+FP+FN)"
    explanation: "Measures incorrect predictions, used with other metrics for evaluation."
  - equation: "Accuracy = (TP+TN) / (TP+TN+FP+FN)"
    explanation: "Proportion of correct predictions by the model."
  - equation: "Recall = TP / (TP+FN)"
    explanation: "Proportion of actual positives correctly identified."
  - equation: "Precision = TP / (TP+FP)"
    explanation: "Proportion of positive predictions that are actually positive."
definitions:
  - term: "Predictive Analytics"
    definition: "Process of forecasting outcomes based on historical data."
  - term: "Feature Selection"
    definition: "Technique to identify the most significant predictors to reduce computational load and improve accuracy."
  - term: "LASSO (L1) Regression"
    definition: "Regularization method that shrinks less important feature coefficients to zero, selecting a subset of features."
  - term: "Ridge (L2) Regression"
    definition: "Regularization method that shrinks all feature coefficients but not to zero."
  - term: "Genetic Algorithm (GA)"
    definition: "Wrapper-based feature selection method inspired by natural selection, iteratively selecting optimal feature subsets."
  - term: "AUC"
    definition: "Area Under the ROC Curve, a metric evaluating model performance independent of class imbalance."
  - term: "KNN Imputation"
    definition: "Method to estimate missing numerical values using the mean of k-nearest neighbors."
  - term: "Binary Encoding"
    definition: "Technique to convert nominal categorical data into numerical columns of log2(n) dimensions."
critical_citations:
  - "[Alyahyan & Düştegör, 2020] — Literature review establishing prior academic achievement and demographics as key predictors."
  - "[Lumboy, 2019] — Shows STEM strand students outperform others, justifying SHS track inclusion."
  - "[Mweshi, 2019] — Summarizes GA's success as a feature selector, supporting its use."
  - "[Cui et al., 2019] — Review identifying Decision Tree and Random Forest as most used algorithms."
  - "[Patacsil, 2020] — Demonstrates ensemble models predict student dropout, similar approach to this study."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "contextual"
      justification: "Focuses on Filipino students, a key demographic that transitions to young professionals."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "contextual"
      justification: "Predictors like family income and parental occupation relate to financial background."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "low"
      justification: "Not directly about financial behavior, but student success has indirect financial implications."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "low"
      justification: "Uses Philippine data and discusses SHS strand mismatch, a local educational policy issue."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "contextual"
      justification: "The feature selection and classification approaches are analogous to categorizing financial data."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Provides an example of a predictive system, relevant to the landscape of PFMS."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "contextual"
      justification: "Highlights limitations of single-criterion admission, similar to gaps in PFMS."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "The concept of student profiles based on demographic and academic data is analogous to user profiles."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "medium"
      justification: "Addresses prediction using only pre-admission data, similar to cold-start profile generation."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Compares classification algorithms for profile prediction, directly relevant to profile classification."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Core paper contribution is predictive modeling for student success."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "contextual"
      justification: "Applies forecasting algorithms to education data; methods are transferable."
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "contextual"
      justification: "Feature selection reduces the feature space, analogous to constraint reduction."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "low"
      justification: "Prediction of 'needs intervention' is related to anomaly detection in student outcomes."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Uses accuracy, precision, recall, and AUC, standard evaluation metrics for PFMS modules."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Compares multiple algorithms and feature selection methods, a core algorithmic evaluation."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "medium"
      justification: "The evaluation methodology (hold-out, AUC, accuracy) is analogous to evaluating budget recommender systems."
  contribution: "This paper provides a methodological template for predictive classification in Odin's profile module (5.C), demonstrating how feature selection (GA) significantly improves performance over baseline classifiers (6.A). The evaluation framework using accuracy and AUC (12.A, 12.B) offers a validated approach to comparing Odin's recommendation algorithms. The concept of predicting 'needs intervention' from pre-enrollment data relates to cold-start profiling (5.B) and can inform how Odin generates initial user savings and spending recommendations before sufficient transaction history exists. The use of local Philippine data (2.A) and handling of encoding and missing values provides a practical implementation reference for Odin's data preprocessing pipeline."
  directly_justifies:
    - "GA feature selection improves Logistic Regression AUC by 21% compared to using all features."
    - "Genetic Algorithm outperforms LASSO and Ridge for feature selection in predictive classification."
    - "Pre-admission data alone can predict student outcomes, relevant for cold-start profiling."
    - "Admission exam scores are the most important single predictor among available features."
    - "Prior academic achievement (GPA) and specific exam subjects are strong predictors."
  limits:
    - "Findings are specific to a single Philippine university (Caraga State University) and may not generalize."
    - "Data is limited to pre-admission features; behavioral and environmental predictors are excluded."
    - "The best-performing model's precision (0.73) indicates moderate false positive risk."
    - "The study does not validate the model on newer cohorts (post-2018) for temporal generalizability."
    - "Deep learning methods are not compared, limiting the state-of-the-art comparison."
  mapping_rationale: "A systematic scan was performed across all 12 Odin functional domains and their associated 39 topic codes. Domains flagged as relevant include: Behavioral Profiling & Classification (5.A, 5.B, 5.C) because the paper builds classification models to predict student outcomes based on profiles; Spending Forecasting (6.A, 6.B) due to its focus on predictive analytics and algorithm comparison; and System Evaluation (12.A, 12.B, 12.C) for its detailed evaluation metrics and methodology. Topic 5.C (classification approaches) and 6.A (predictive modeling) are assigned 'high' relevance as the paper directly compares classification algorithms for prediction. 5.B (cold-start) is 'medium' because prediction is from initial pre-admission data, analogous to cold-start profile generation. 12.A and 12.B are 'high' for the evaluation framework. Topic 7.D (infeasibility) is 'contextual' because feature selection reduces complexity, similar to constraint reduction. Domains considered but rejected: Savings & Debt Management (13.A, 13.B, 13.C) as student graduation success is not directly about savings or debt; Mobile-First Design (9.A, 9.B) as the paper mentions a web app but does not address mobile design; Data Privacy & User Trust (10.A, 10.B) is not discussed; and Engagement & Retention (11.A, 11.B) are not relevant. The paper's overall relevance to Odin is high for its methodological contributions to predictive profiling, classification algorithm comparison, and evaluation practices."
limitations:
  - "Dataset size (2,207 samples) is moderate; larger datasets may yield different results."
  - "The study uses only pre-admission data; future work with post-enrollment data could improve accuracy."
  - "The web application (Django) is presented but not evaluated for usability or real-world impact."
  - "Feature importance is based solely on occurrence counts, not on model-specific importance values." [unacknowledged]
  - "The study does not compare against deep learning or transformer-based models." [unacknowledged]
remember_this:
  - "Genetic Algorithm feature selection improved AUC by 21% over the full dataset."
  - "Logistic Regression with GA achieved the highest accuracy at 79%."
  - "Admission exam results were the most consistently selected predictor."
  - "Pre-admission data alone can predict student success with reasonable accuracy."
  - "GA selected more features than L1 or L2, leading to superior performance."
```
---

## Paper 23: Onsay & Rabajante-2024_summarized.md

**Source File:** `Onsay & Rabajante-2024_summarized.md`

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

## Paper 24: Espiritu F. et al_summarized.md

**Source File:** `Espiritu F. et al_summarized.md`

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

## Paper 25: Cedeno et al_summarized.md

**Source File:** `Cedeno et al_summarized.md`

```yaml
paper_id: 10.36227/techrxiv.173091273.31877417/v1
designation: local-algorithm-specific
title: Pitik: A Cebuano-Binisaya Intent-Based Chatbot for Cardiovascular Disease Patient Profiling and Risk Factor Recommendations
authors: Cedeño, J. G.; Manteza, A. E.; Nacar, N. C.; Umbukan, M. P.; Muaña, C. G.; Vasay, M. J.; Benablo, C. I. P.; Adlaon, K. M. M.
year: 2024
venue: TechRxiv
odin_topics:
  - 2.A
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
tldr: A Cebuano-Binisaya chatbot for cardiovascular risk assessment and patient profiling, using intent-based NLP and Gricean Maxims to enhance communication in underserved Philippine communities.
problem_and_motivation: Manual patient profiling in rural Philippine community health programs leads to fragmented data and hinders accurate diagnosis. Existing healthcare apps lack Cebuano-Binisaya support, excluding millions. A culturally and linguistically appropriate digital tool is needed to bridge this gap and improve cardiovascular care access.
approach:
  - Iterative software development with three iterations guided by Action Research and expert collaboration.
  - Utilized DialogFlow for intent matching, incorporating Pre-Intent and Post-Intent Matching algorithms.
  - Applied Gricean Maxims of conversation to detect communication violations and guide effective interaction design.
  - Evaluated Naive Bayes, SVM, MLP, and RNN for post-intent matching, selecting SVM for its superior performance.
  - Assessed chatbot quality using Analytic Hierarchy Process (AHP) with categories of Performance, Humanness, and Accessibility.
findings:
  - Iteration 3 significantly improved performance (65% to 79%) and accessibility (22% to 96%) via suggestion chips and tooltips.
  - SVM outperformed other models in the Smoking/Alcohol category with 73% accuracy and balanced precision/recall.
  - Suggestion chips and tooltips effectively addressed user unfamiliarity with medical terminology like HBA1C and Systolic Blood Pressure.
  - Users expressed dissatisfaction with lengthy conversational format and lack of medical tips, indicating areas for future development.
  - Gricean Maxim violations decreased from the second to third iteration across all categories (e.g., Manner: 44 to 22 violations).
key_figures_tables:
  - Figure 1: Iterative software development process of Pitik → Enabled continuous enhancements and refinements over three iterations.
  - Figure 2: Example of Grice Maxim occurrences in Pitik → Illustrates how violations (quantity, quality, relation, manner) were identified.
  - Figure 6: Hierarchical structure for Pitik chatbot evaluation → AHP criteria breakdown: Performance, Humanness, Accessibility.
  - Table 2: Gricean Maxims Violations → Showed reduction in violations from iteration 2 to 3 (e.g., Manner: 44 to 22).
  - Table 3: Model Performances for diet/exercise and smoking/alcohol areas → SVM achieved the highest accuracy (73%) for smoking/alcohol.
key_equations:
  - equation: "Risk Factors = (ln(Age) * 3.06117) + (ln(Total cholesterol) * 1.12370) - (ln(HDL cholesterol) * 0.93263) + (ln(Systolic blood pressure) * On blood pressure medication) + Cigarette smoker + Diabetes present - 23.9802"
    explanation: Framingham formula for computing cardiovascular risk factors from user data.
  - equation: "Risk = 100 * (1 - 0.88936e(Risk Factors))"
    explanation: Converts risk factors to a percentage risk score.
definitions:
  - term: CVD
    definition: Cardiovascular diseases, the leading cause of death in the Philippines.
  - term: Gricean Maxims
    definition: Four conversational principles (quantity, quality, relation, manner) for effective communication.
  - term: AHP
    definition: Analytic Hierarchy Process, a structured technique for complex decision-making.
  - term: DialogFlow
    definition: Google's natural language understanding platform for building conversational interfaces.
  - term: SVM
    definition: Support Vector Machine, a supervised machine learning model for classification.
critical_citations:
  - "[Cacciata et al., 2021] — CVD remains a leading cause of death in the Philippines."
  - "[D'Agostino et al., 2008] — Provides Framingham formula used for risk assessment."
  - "[Radziwill & Benton, 2017] — AHP method recommended for evaluating chatbot quality."
  - "[Reyes et al., 2023] — Community outreach programs in rural areas are key to healthcare access."
relevance:
  topics:
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: Provides a model for designing culturally and linguistically appropriate digital health tools.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews existing health apps (KonsultaMD) and their limitations, analogous to financial app landscape.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies gaps in existing systems, including lack of local language support and fragmented data.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: Methods for patient profiling (CVD risk) can be adapted for financial behavioral profiling.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Compares classification algorithms (SVM, NB, MLP, RNN) for user response intent, relevant to profile classification.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Addresses user accessibility and design for underserved communities, relevant to mobile-first considerations.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: UI/UX improvements like suggestion chips and tooltips are directly applicable to mobile app design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Mentions data collection and storage but does not focus on privacy/security mechanisms.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: Focuses on effectiveness and accessibility rather than trust-building mechanisms.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Uses AHP, a structured evaluation framework for assessing chatbot quality.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Rigorously evaluates intent matching algorithms using precision, recall, F1, accuracy.
  contribution: "Pitik demonstrates the successful implementation of a localized conversational AI for health profiling, offering a template for culturally adapted digital tools. Its iterative development and AHP-based evaluation framework provide a robust methodology for assessing system quality across multiple dimensions. The integration of Gricean Maxims offers a novel approach to enhancing communication in chatbot interactions, which can be applied to financial advisory contexts. The specific comparison of machine learning models for intent matching (SVM vs. Naive Bayes, etc.) provides actionable insights for selecting classification algorithms for user profiling tasks in Odin."
  directly_justifies:
    - "Culturally and linguistically appropriate tools are essential for user adoption in underserved communities."
    - "Iterative development with user feedback is critical for improving system performance and accessibility."
    - "SVM is a robust classifier for intent-based user responses, outperforming Naive Bayes and RNN on small datasets."
    - "Suggestion chips and tooltips significantly enhance user experience and data collection success rates."
    - "Performance should be prioritized over humanness and accessibility in system evaluation for functional effectiveness."
  limits:
    - "Limited to 100 participants, primarily accessible via social media, not strictly rural."
    - "Focus on CVD health profiling; direct transferability to personal finance requires validation."
    - "Specific evaluation tools (AHP, Gricean Maxims) may not be standard in all domains."
    - "No long-term user engagement or behavior change data provided."
    - "Model performance was tested on a balanced dataset of only 40 records; limited generalizability."
  mapping_rationale: "A systematic scan across all 12 functional domains identified three primary areas of relevance for Odin. The 'Existing Systems & Gaps' domain (topics 4.A, 4.B) is flagged as high relevance because the paper explicitly reviews current health apps and identifies missing local-language support and fragmented data—directly analogous to financial app gaps. The 'Behavioral Profiling & Classification' domain (topics 5.A, 5.C) is highly relevant because the study profiles users based on health risk and compares classification algorithms (SVM, NB) for intent matching, which maps directly to financial profile classification. The 'System Evaluation' domain (topics 12.A, 12.B) is flagged as high relevance for its rigorous AHP evaluation framework and algorithm benchmarking (precision, recall, F1). 'Mobile-First Design' (topics 9.A, 9.B) is flagged as medium relevance for its UX enhancements (suggestion chips, tooltips). 'Filipino Cultural Context' (topic 2.A) is contextual, providing a model for cultural adaptation. Topics related to 'Spending Forecasting' (6.A, 6.B), 'Budget Recommendation' (7.A-D), 'Anomaly Detection' (8.A-C), 'Savings & Debt' (13.A-C), and 'Engagement' (11.A, 11.B) were considered and rejected as the paper does not address spending, budgeting, anomalies, savings, debt, or engagement dynamics. Overall, the paper is highly relevant for its methodologies in localized system development, user profiling, and algorithmic evaluation, which can directly inform Odin's design and testing phases."
limitations:
  - "Small sample size (n=100) limits generalizability. [unacknowledged]"
  - "The study was conducted on a preprint and not yet peer-reviewed."
  - "SVM performance was only tested on 40 records, which is insufficient to draw strong conclusions."
  - "Focus on health, not finance, requiring adaptation of profiling and classification methods."
  - "Humanness and accessibility were less prioritized, which may not align with all user experience goals."
remember_this:
  - "SVM achieved 73% accuracy for intent classification on a small dataset."
  - "Iteration 3 boosted accessibility from 22% to 96% using suggestion chips and tooltips."
  - "Performance was weighted 0.79, far outweighing humanness and accessibility in evaluation."
  - "Gricean Maxims were used to identify communication violations and improve chatbot interaction."
  - "Culturally adapted, localized chatbots can significantly improve data collection in underserved areas."
```
---

## Paper 26: Salvador_summarized.md

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

## Paper 27: Apus et al_summarized.md

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

## Paper 28: Espiritu P. et al_summarized.md

**Source File:** `Espiritu P. et al_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: local-algorithm-specific
title: Balarila: Deep Learning for Semantic Grammar Error Correction in Low-Resource Settings
authors: Espiritu, P.; Jadie, J.; Ponce, A.; Cheng, C.
year: 2023
venue: Proceedings of the First Workshop in South East Asian Language Processing
odin_topics:
  - "3.C"
  - "8.C"
tldr: Develops a transformer encoder-based model for Filipino grammar error correction using a synthetic dataset and iterative sequence tagging.
problem_and_motivation: Existing Filipino grammar checkers are limited to lexical errors and lack semantic error correction capabilities. There is no publicly available Filipino grammar checker addressing this complexity, motivating the development of a deep learning solution.
approach:
  - "Adopted the GECToR approach, framing grammar error correction as an iterative sequence tagging task using a transformer encoder."
  - "Created a synthetic dataset of error-free and error-filled Filipino sentences via an automated error generation pipeline from scraped news articles."
  - "Fine-tuned three pre-trained models: BERT-Base, RoBERTa-Base, and RoBERTa-Large, using a two-stage fine-tuning process."
  - "Used a dataset of 906,958 sentences split into train, dev, and test sets with a 70:15:15 ratio."
  - "Evaluated GEC performance using precision, recall, and F0.5 scores, and GED performance using a multi-class confusion matrix."
findings:
  - "num: RoBERTa-Large achieved the highest F0.5 score of 70.75, while RoBERTa-Base achieved a score of 69.00."
  - "num: RoBERTa-Base demonstrated cost-effectiveness with only a 1.75% F0.5 score difference compared to RoBERTa-Large."
  - "Models struggled with duplicate words, morphological errors, and missing word errors due to the error automation algorithm's vagueness."
  - "RoBERTa-Large outperformed others in GEC scores, producing corrections closest to the gold standard."
  - "BERT-Base had the poorest performance across all GEC metrics."
  - "All models faced difficulties with EMARK transformation tags due to a lack of common indicators for exclamation marks."
  - "Inconsistencies were observed in correcting the same erroneous sentence with multiple errors due to dataset limitations."
key_figures_tables:
  - "Figure 3: Bar charts comparing precision, recall, and F0.5 scores of three models → RoBERTa-Large shows the best GEC performance."
  - "Table 2: List of error types and their corresponding transformation tags → Defines the tagging schema for the GEC task."
  - "Table 3: Tagalog Verb Form Transformation Tags → Shows the morphological transformations for verbs."
  - "Table 6: Grouped GED performance results for error-free and error-filled datasets → RoBERTa-Large generally performs best across error types."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "GEC"
    definition: "Grammatical Error Correction"
  - term: "GED"
    definition: "Grammatical Error Detection"
  - term: "SMT"
    definition: "Statistical Machine Translation"
  - term: "GECToR"
    definition: "Grammatical Error Correction: Tag, Not Rewrite"
  - term: "BERT"
    definition: "Bidirectional Encoder Representations from Transformers"
  - term: "RoBERTa"
    definition: "Robustly optimized BERT approach"
critical_citations:
  - "[Omelianchuk et al., 2020] — Foundational approach adopted for the GEC model."
  - "[Cruz and Cheng, 2021] — Pre-trained Filipino RoBERTa models used in the study."
  - "[Cruz and Cheng, 2019] — Pre-trained Filipino BERT model used in the study."
relevance:
  topics:
    - code: "3.C"
      name: "User-Defined Allocation Constraints"
      relevance: "contextual"
      justification: "The study's synthetic data generation approach could inform handling of user constraints in natural language."
    - code: "8.C"
      name: "Cold-Start Baseline Strategies for Anomaly Detection"
      relevance: "low"
      justification: "The GECToR architecture used for error detection may inform cold-start baseline strategies for anomaly detection modules."
  contribution: "The paper's approach to synthetic dataset creation for low-resource languages provides a potential strategy for generating labeled data for Odin's cold-start challenges. The GECToR-inspired iterative sequence tagging architecture offers a potential method for detecting and correcting constraints or anomalies in user-declared inputs, such as budget categories or spending descriptions. The use of transformer encoders demonstrates a viable path for leveraging pre-trained models for financial natural language processing tasks, reducing reliance on large, domain-specific corpora."
  directly_justifies:
    - "Synthetic data generation is a viable strategy for low-resource natural language processing tasks."
    - "Transformer encoder-based models can effectively handle error detection and correction in the Filipino language."
    - "Iterative sequence tagging can refine predictions over multiple passes."
  limits:
    - "Limited to specific grammar and spelling errors; does not cover all possible Filipino language errors."
    - "The synthetic dataset may introduce biases due to the rule-based error automation pipeline."
    - "Training was hindered by GPU memory issues, particularly for the RoBERTa-Large model."
    - "The error automation algorithm introduced only one error per sentence, limiting model robustness."
    - "The study does not address financial domain-specific language or user constraints."
  mapping_rationale: "A systematic scan across all 12 functional domains and associated topic codes was performed. The primary contribution of the paper, being a deep learning model for grammar error correction in a low-resource setting, was assessed. The paper was flagged as potentially relevant to the 'Expense Categorization' domain, specifically topic 3.C (User-Defined Allocation Constraints), as the ability to parse and correct user input could inform how users specify their budget allocations. Additionally, the paper's architecture (GECToR) and its use of synthetic data were considered for topic 8.C (Cold-Start Baseline Strategies for Anomaly Detection), as the approach could inspire strategies for handling scarce labeled data. These were assigned 'contextual' and 'low' relevance, respectively. Topics related to forecasting, behavioral profiling, and system evaluation were rejected as the paper does not address financial data or PFMS design. Borderline cases were considered for topic 4.A (Landscape of Existing Systems) due to the mention of Gramatika, but this was rejected as the paper's focus is on building a new system, not analyzing the landscape. Overall, the paper's relevance to Odin is indirect, providing methodological inspiration for data generation and input processing rather than direct financial insights."
limitations:
  - "The Balarila model only covers a limited set of Filipino grammatical errors."
  - "The synthetic dataset was created using rule-based automation, which may introduce inaccuracies."
  - "Memory issues during training for the RoBERTa-Large model, especially due to GPU limitations."
  - "The dataset only contains one error per corrupted sentence, limiting the model's ability to correct multiple errors."
  - "The study does not address real-world user interactions or financial language. [unacknowledged]"
remember_this:
  - "RoBERTa-Large achieved the highest F0.5 score of 70.75 for Filipino grammar error correction."
  - "RoBERTa-Base is the most cost-effective model with only a 1.75% score difference from the large version."
  - "Synthetic dataset creation is a viable method for low-resource language tasks."
  - "Model performance is hampered by limited error types and the synthetic data generation approach."
```
---

## Paper 29: Dominguez et al_summarized.md

**Source File:** `Dominguez et al_summarized.md`

```yaml
paper_id: 10.63876/ijss.v1i2.73
designation: local-algorithm-specific
title: Adaptive Federated Learning for Privacy-Preserving Smart Applications
authors: Dominguez, B. L.; Emmanuel, R.; Montemayor, A. F.
year: 2023
venue: International Journal of Smart Systems
odin_topics:
  - 10.A
  - 10.B
  - 12.A
  - 12.B
tldr: An adaptive federated learning framework with differential privacy and secure aggregation improves convergence speed and communication efficiency for privacy-preserving smart applications.
problem_and_motivation: Conventional federated learning struggles with heterogeneous data, limited device resources, and dynamic network conditions, leading to degraded performance and communication overhead. Integrating adaptivity with strict privacy guarantees remains an open challenge for smart applications handling sensitive personal data.
approach:
  - The framework follows a client-server architecture where clients train local models on private data and share only masked updates.
  - A context-aware aggregation function uses adaptive weights based on data quality, model performance, and resource constraints.
  - Differential privacy adds Gaussian noise to local updates before transmission to prevent reconstruction of individual data.
  - Secure aggregation uses cryptographic masking to hide individual contributions from the server.
  - Communication overhead is minimized through dynamic client participation and update compression techniques.
findings:
  - AFL reached 92.3% accuracy on HAR dataset within 40 rounds, compared to FedAvg's 84.7% after 55 rounds.
  - num: 28% reduction in communication overhead achieved compared to FedAvg.
  - Membership inference attack success rate reduced to 18.4% with AFL, versus 42.1% for FedAvg.
  - Performance loss from differential privacy noise remained below 2%.
  - Active clients per round dropped by ~20% without harming accuracy.
key_figures_tables:
  - Table 1: Accuracy and convergence comparison for HAR, FEMNIST, OpenIoT → AFL converges faster and achieves higher accuracy than FedAvg and FedProx.
  - Figure 2: Communication efficiency comparison → AFL reduces overhead by up to 28% vs FedAvg.
  - Figure 3: Membership inference attack success rate → AFL reduces privacy leakage risk significantly.
key_equations:
  - equation: w_global = sum_{i=1}^N alpha_i * w_i
    explanation: Adaptive aggregation weights client updates by quality and resources.
  - equation: alpha_i = (lambda_1 D_i + lambda_2 A_i) / (lambda_3 R_i + epsilon)
    explanation: Weighting function based on data volume, accuracy, and resource constraints.
  - equation: w_i_tilde = w_i + N(0, sigma^2)
    explanation: Differential privacy adds Gaussian noise to local model updates.
definitions:
  - term: FL
    definition: Federated Learning, a distributed machine learning paradigm.
  - term: AFL
    definition: Adaptive Federated Learning, the proposed framework.
  - term: DP
    definition: Differential Privacy, a technique to protect individual data.
  - term: Non-IID
    definition: Non-independent and identically distributed data across clients.
  - term: FedAvg
    definition: Federated Averaging, a baseline FL algorithm.
  - term: FedProx
    definition: A proximal variant of FL for heterogeneous data.
critical_citations:
  - "[Zhang et al., 2020] — Foundational FL with adaptive compression."
  - "[Ahmad et al., 2023] — Robust FL under statistical heterogeneity."
  - "[Liu et al., 2022] — Differential privacy performance evaluation."
  - "[Lo et al., 2022] — Architectural patterns for FL systems."
relevance:
  topics:
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Directly evaluates differential privacy and secure aggregation for protecting sensitive user data.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Demonstrates reduced membership inference attack success, which supports user trust.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a comprehensive evaluation methodology including accuracy, convergence, and privacy metrics.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Benchmarks AFL against FedAvg and FedProx on multiple datasets and metrics.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: Mentions mobile devices as clients but does not focus on mobile UX.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: No direct discussion of user interface or experience design.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Broadly situates FL in financial smart applications but does not review PFMS.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: Does not address user engagement or behavioral dynamics.
  contribution: The AFL framework provides a directly applicable privacy-preserving architecture for Odin's distributed data processing module. Its adaptive aggregation can inform Odin's budget recommendation engine by weighting user inputs based on reliability. The communication optimization techniques can guide Odin's mobile-client design to reduce bandwidth usage. The privacy evaluation methodology offers a benchmark for Odin's security validation.
  directly_justifies:
    - "Differential privacy can protect individual user spending data in federated PFMS."
    - "Secure aggregation prevents server-side exposure of client financial contributions."
    - "Adaptive weighting improves model performance under heterogeneous user financial behavior."
    - "Resource-aware participation reduces battery and bandwidth usage on mobile devices."
  limits:
    - "Evaluation uses benchmark datasets (HAR, FEMNIST, OpenIoT) not specific to personal finance."
    - "Privacy-accuracy trade-off requires careful tuning not fully explored for financial data."
    - "System complexity overhead at server side may require optimization for PFMS scale."
  mapping_rationale: All 12 functional domains were systematically scanned. The highest relevance was found for Data Privacy & User Trust (10.A, 10.B) and System Evaluation (12.A, 12.B), as the paper directly evaluates privacy mechanisms and provides a rigorous benchmarking framework—assigned high relevance. Mobile-First Design (9.A, 9.B) was considered but rejected because the paper only mentions mobile devices as clients without UX discussion. Engagement (11.A) and Forecasting (6.A) were rejected for lacking behavioral or predictive content. The paper does not address expense categorization, budgeting, or anomaly detection, so those domains were rejected. Overall, the paper offers strong methodological support for privacy and evaluation modules in Odin.
limitations:
  - "Evaluation datasets are not financial spending data, limiting direct applicability to PFMS. [unacknowledged]"
  - "Privacy-accuracy trade-off dynamics are not fully characterized for heterogeneous financial datasets. [unacknowledged]"
  - "The framework assumes honest-but-curious server, not malicious adversarial settings. [acknowledged]"
  - "Scalability to thousands of PFMS users is not empirically tested."
remember_this:
  - "Differential privacy reduced inference attack success to 18.4 percent."
  - "Adaptive aggregation improved convergence speed on non-IID data."
  - "Communication overhead reduced by 28 percent through dynamic participation."
  - "Privacy preservation came with less than 2 percent accuracy loss."
```
---

## Paper 30: Maceda et al_summarized.md

**Source File:** `Maceda et al_summarized.md`

```yaml
paper_id: 10.1145/3639233.3639353
designation: local-algorithm-specific
title: Classifying Sentiments on Social Media Texts: A GPT-4 Preliminary Study
authors: Maceda, L. L.; Llovido, J. L.; Artiaga, M. B.; Abisado, M. B.
year: 2023
venue: 2023 7th International Conference on Natural Language Processing and Information Retrieval
odin_topics:
  - 5.C
  - 12.A
  - 12.B
tldr: Evaluates GPT-4 for sentiment classification on code-mixed social media texts, achieving substantial agreement with human annotations using one-shot prompts.
problem_and_motivation: Manual sentiment annotation of social media data is costly and time-consuming, especially for code-mixed low-resource languages. Automated methods are needed to scale sentiment analysis for public opinion tracking. Prior work lacks evaluation of GPT-4 on such data.
approach:
  - Used GPT-4 API with zero-shot and one-shot prompts (English and code-mixed) on 600 social media posts about Philippine UAQTE program.
  - Compared GPT-4 against fine-tuned mBERT, using Cohen's Kappa, accuracy, precision, and recall.
  - Employed batch processing to reduce API costs, with 30 and 15 samples per request for zero-shot and one-shot respectively.
  - Conducted error analysis to identify misclassifications due to slang and domain-specific language.
findings:
  - "num: One-shot English prompt achieved Cohen's Kappa 0.77 and accuracy 0.85."
  - "num: Code-mixed one-shot achieved Kappa 0.73 and accuracy 0.825."
  - "num: Zero-shot English achieved Kappa 0.50 and accuracy 0.668."
  - "num: Fine-tuned mBERT underperformed GPT-4 with accuracy 0.828."
  - Model sometimes returned textual responses instead of numeric codes, requiring post-processing.
  - Slang and domain-specific terms caused misclassifications.
key_figures_tables:
  - "Table 2: Performance of GPT-4 and mBERT on sentiment classification → one-shot English best with Kappa 0.77."
  - "Table 3: Examples of classified sentiments showing model errors → Model struggles with slang like 'cutie'."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "GPT-4"
    definition: "Large language model by OpenAI used for text generation and classification."
  - term: "mBERT"
    definition: "Multilingual BERT model pre-trained on 104 languages."
  - term: "Code-mixing"
    definition: "Use of multiple languages within a single sentence."
  - term: "UAQTE"
    definition: "Philippine Universal Access to Quality and Tertiary Education Act."
  - term: "Cohen's Kappa"
    definition: "Statistic measuring inter-rater agreement."
critical_citations:
  - "[OpenAI, 2023] — GPT-4 technical report and capabilities."
  - "[Devlin et al., 2019] — BERT and mBERT foundation."
  - "[Gilardi et al., 2023] — ChatGPT outperforms crowd workers for annotation."
relevance:
  topics:
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "low"
      justification: "Paper focuses on sentiment classification, not financial profiles, but provides a classification methodology."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "low"
      justification: "Uses evaluation metrics (Kappa, accuracy) that could inform Odin's evaluation design."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "low"
      justification: "Compares GPT-4 and mBERT, offering a template for evaluating classification algorithms."
  contribution: "The paper demonstrates a cost-effective approach to sentiment classification using GPT-4 without fine-tuning, which could be adapted to classify user intent or sentiment in Odin's feedback module. The evaluation metrics (Cohen's Kappa, accuracy) provide a benchmark for assessing Odin's own classification modules. The findings on prompt engineering (one-shot with persona) offer guidance for implementing LLM-based features in Odin. The error analysis highlights challenges with slang and domain-specific language, relevant to Odin's Filipino user base."
  directly_justifies:
    - "GPT-4 with one-shot prompts achieves substantial agreement with human annotators on code-mixed data."
    - "Fine-tuned mBERT underperforms GPT-4 on sentiment classification."
    - "Prompt design, including persona and examples, significantly improves classification accuracy."
    - "Zero-shot performance is notably lower, indicating the need for few-shot examples."
  limits:
    - "Limited sample size (600 posts) and single-run experiment due to API costs."
    - "Possible data contamination as GPT-4 may have seen similar social media data during training."
    - "Not tested on financial domain or spending-related texts."
    - "Error analysis shows sensitivity to slang and non-standard language."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. Domains related to financial practices, spending forecasting, budgeting, anomaly detection, mobile design, privacy, and savings/debt were rejected because the paper does not address financial behaviors or PFMS-specific tasks. The domain of Behavioral Profiling & Classification (5.C) was flagged as low relevance because the paper presents a classification approach (sentiment) that could be adapted for profiling. The System Evaluation domains (12.A and 12.B) were also flagged as low relevance because the paper uses standard evaluation metrics and compares algorithms, which could inform Odin's evaluation methodology. Borderline cases included 11.A (Engagement Dynamics) because sentiment analysis could gauge user engagement, but the paper does not link to engagement mechanisms. Ultimately, only 5.C, 12.A, and 12.B were selected with low relevance. Overall, the paper provides methodological insights for using LLMs in classification tasks but lacks direct application to PFMS, making its relevance contextual at best."
limitations:
  - "Small dataset and single experimental run due to cost constraints."
  - "Potential data contamination of GPT-4 training set."
  - "Not validated on financial or spending-related texts."
  - "Error analysis reveals sensitivity to slang and domain-specific terms. [unacknowledged]"
remember_this:
  - "One-shot English prompt achieved Kappa 0.77 and accuracy 0.85."
  - "GPT-4 outperforms fine-tuned mBERT on code-mixed sentiment data."
  - "Prompt design with persona and examples is critical for performance."
  - "Code-mixed prompts perform similarly to English ones when context is adequate."
```
---

## Paper 31: Alejandrino et al_summarized.md

**Source File:** `Alejandrino et al_summarized.md`

```yaml
paper_id: 7d8e9f2a-1b3c-4d5e-6f7a-8b9c0d1e2f3a
designation: local-algorithm-specific
title: Supervised and unsupervised data mining approaches in loan default prediction
authors: "Alejandrino, J. C.; Bolacoy, J. P.; Murcia, J. V. B."
year: 2023
venue: International Journal of Electrical and Computer Engineering
odin_topics:
  - "1.C"
  - "5.A"
  - "5.C"
  - "6.A"
  - "6.B"
  - "8.A"
  - "8.B"
  - "12.A"
  - "12.B"
tldr: Loan default prediction using supervised and unsupervised data mining approaches on a Philippine cooperative dataset identifies k-NN and logistic regression as top classifiers.
problem_and_motivation: Financial institutions in the Philippines lack clear, data-driven bases for predicting loan performance, leading to high default incidences and low collection efficiency. Strict laws like the Truth in Lending Act challenge the development of recommender systems, yet management believes machine learning could leverage crucial customer data to anticipate defaults and ensure institutional stability.
approach:
  - "Data from a Philippine cooperative contained 29 attributes with 1000 instances; 900 for training and cross-validation, 100 for unlabeled testing."
  - "Preprocessing included imputing missing values, removing irrelevant attributes, normalizing numeric data, and applying SMOTE to address class imbalance."
  - "Feature selection used correlation-based, information gain, and wrapper-based methods, reducing attributes to 23 relevant predictors."
  - "Four classifiers were used: J48 decision tree with varied confidence factors, k-NN with k values from 3 to 11, naïve Bayes, and logistic regression."
  - "Models were evaluated using 13-fold cross-validation on the balanced training set, measuring accuracy, F-measure, and kappa statistics."
findings:
  - "num: J48 at 0.50 confidence factor achieved 76.85% accuracy, the highest among its J48 variants."
  - "num: k-NN 3 achieved the highest accuracy (78.38%) among IBk variants, outperforming higher k values."
  - "num: Naïve Bayes achieved 76.65% accuracy, while logistic regression achieved 77.31% accuracy."
  - "num: k-NN 3 and logistic regression had the highest F-measures (0.780 and 0.773) and kappa statistics (0.5677 and 0.5462)."
  - "num: On the test set, k-NN 3 predicted 48 non-defaulters and 52 defaulters, while logistic predicted 44 and 56, respectively."
key_figures_tables:
  - "Table 1: Lists 29 loan prediction dataset attributes with descriptions and transformation indicators."
  - "Table 2: Shows classification accuracy of classifiers, with k-NN 3 and logistic regression performing best."
  - "Table 3: Compares F-measure, correctly classified instances, and kappa statistics, confirming k-NN 3 and logistic as top performers."
  - "Figure 2: Provides confusion matrices for all classifiers, detailing correct/incorrect classifications per class."
  - "Figure 3: Displays kappa statistics and mean absolute errors for J48 variants, with C.0.50 having the highest kappa."
  - "Figure 4: Shows average F-measure and mean absolute error for k-NN variants, with k=3 having the highest F-measure."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Data Mining"
    definition: "The process of discovering significant new patterns, correlations, and trends by filtering through large amounts of data stored in repositories."
  - term: "SMOTE"
    definition: "Synthetic Minority Over-sampling Technique that synthesizes new data from available instances to address class imbalance."
  - term: "Weka"
    definition: "A suite of machine learning software containing tools for data preprocessing, classification, clustering, and visualization."
critical_citations:
  - "[Lahsasna et al., 2010] — Found random forest outperforms other methods for loan prediction."
  - "[Zhu et al., 2019] — Highlights random forest for loan default prediction."
  - "[Hamid and Ahmed, 2016] — Found J48 algorithm has higher accuracy than Bayes Net and naive Bayes."
  - "[Sudhakar and Reddy, 2016] — Proposed two-step loan credibility system using decision trees."
  - "[Vimala and Sharmili, 2018] — Found SVM outperforms naïve Bayes on German credit data."
relevance:
  topics:
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "medium"
      justification: "Uses Philippine cooperative data to classify loan default, reflecting financial behavior of Filipino borrowers."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Directly classifies borrowers into 'default' or 'non-default' profiles based on financial data."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Compares several classification algorithms (J48, k-NN, Naïve Bayes, Logistic) for behavioral profiling."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Implements predictive models to forecast loan default, a core predictive task in PFMS."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "medium"
      justification: "Provides context on algorithms used for forecasting in financial systems, though data is not sequential spending."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Loan default can be viewed as an anomaly in repayment behavior; classification methods are relevant to detecting such events."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "medium"
      justification: "The supervised and unsupervised approaches are comparable to anomaly detection methodologies."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Provides a comprehensive evaluation framework using accuracy, F-measure, and kappa statistics."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Directly evaluates the performance of multiple algorithmic modules (J48, k-NN, Naïve Bayes, Logistic)."
  contribution: "This paper provides a methodological blueprint for Odin's classification engine by demonstrating how to preprocess financial data, address class imbalance, and select optimal classifiers for a Philippine context. It validates the use of k-NN and logistic regression for binary financial outcome prediction, offering benchmark performance metrics. The evaluation framework using accuracy, F-measure, and kappa statistics is directly applicable to Odin's module testing. The study's focus on Philippine data grounds Odin's design in local cultural and regulatory realities."
  directly_justifies:
    - "k-NN and logistic regression are viable classifiers for predicting financial default in a Filipino dataset."
    - "Data preprocessing steps like SMOTE and normalization are critical for improving classification accuracy."
    - "Evaluation metrics including F-measure and kappa are more informative than accuracy alone."
    - "Philippine financial institutions face data and regulatory challenges that machine learning can address."
  limits:
    - "The dataset is from a single cooperative, limiting generalizability to all Filipino young professionals."
    - "The study does not explore deep learning or ensemble methods beyond those tested."
    - "The cold-start problem for new borrowers is not addressed."
    - "Feature engineering is limited to attribute selection; no new derived features were created."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. Domains 5 (Behavioral Profiling & Classification), 6 (Spending Forecasting), 8 (Anomaly Detection), and 12 (System Evaluation) were flagged as highly relevant due to the paper's direct focus on classifying loan default using Philippine data. Domain 1 (Filipino Context) was flagged as medium, as the study uses a local dataset but does not delve into specific cultural practices. Domains 2 (Cultural Spending), 3 (Expense Categorization), 4 (Existing Systems), 7 (Budget Recommendation), 9 (Mobile-First Design), 10 (Data Privacy), 11 (Retention), and 13 (Savings/Debt) were rejected as they are not addressed by the paper. Borderline cases included topics 2.B (Seasonal Spending) and 2.D (Spending Cycles), which were rejected as the paper does not analyze temporal spending patterns, and topics 3.C (User-Defined Constraints) and 7.D (Infeasibility Handling), which were rejected as the paper does not discuss user preferences or optimization. Overall, the paper is highly relevant to Odin's predictive modeling, classification, and evaluation needs."
limitations:
  - "The use of a single cooperative's data limits the external validity of the findings."
  - "The study does not compare against deep learning or more advanced ensemble methods. [unacknowledged]"
  - "Potential issues with the SMOTE process regarding overfitting are not extensively discussed. [unacknowledged]"
remember_this:
  - "k-NN 3 and logistic regression achieved the highest accuracy of 78.38% and 77.31%."
  - "Addressing class imbalance via SMOTE is critical for unbiased classification."
  - "The study uses a local Philippine cooperative dataset for financial prediction."
  - "Cross-validation with F-measure and kappa provides a robust model evaluation."
  - "Feature selection reduces noise and improves classification performance."
```
---

## Paper 32: Gumasing et al_summarized.md

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

## Paper 33: Ong  A. et al_summarized.md

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

## Paper 34: Deselo & Agner_summarized.md

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
