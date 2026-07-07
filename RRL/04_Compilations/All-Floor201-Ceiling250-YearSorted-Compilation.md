# Compiled Research Summaries

**Total Papers:** 50

**Note:** Included papers positions 201 to 250, Sorted by year.

---

## Paper 1: Kim K. et al_summarized.md

**Source File:** `Kim K. et al_summarized.md`

```yaml
paper_id: 10.1109/ACCESS.2025.3529023
designation: international-algorithm-specific
title: RFMVDA: An Enhanced Deep Learning Approach for Customer Behavior Classification in E-Commerce Environments
authors: Kim, K.; Jo, M.; Ra, I.; Park, S.
year: 2025
venue: IEEE Access
odin_topics:
  - 4.A
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 12.A
  - 12.B
tldr: Extends RFM with Visits, Durations, and Actions to classify purchasing customers, and proposes VDAR for non-purchasers, achieving 92.98% accuracy using a DNN.
problem_and_motivation: Traditional RFM models are inadequate for e-commerce because they only classify purchasing customers, fail to capture continuous online interactions, and omit crucial behavioral data like browsing and cart actions. A more comprehensive model is needed to segment both purchasing and non-purchasing customers based on their complete digital footprint.
approach:
  - Data from 9,416 customers over three months from a South Korean e-commerce site was used.
  - The RFMVDA model adds Visits, Durations, and Actions to the traditional RFM attributes for purchasing customers.
  - The VDAR model was proposed to segment non-purchasing customers using Visits, Durations, Actions, and Referral Keyword.
  - A Deep Neural Network with two hidden layers of 128 neurons each was implemented for classification.
  - The model was validated using Repeated Stratified K-Fold Cross-Validation and hyperparameter grid search.
findings:
  - num: The RFMVDA model achieved a prediction accuracy of 92.98% and a training accuracy of 99.54%.
  - num: Cross-validation yielded an average accuracy of 96.9%, indicating strong generalization.
  - The RFMVDA model refined the LRFM's four customer segments into 14 more detailed categories.
  - The VDAR model effectively segmented 4,742 non-purchasing customers, identifying 36% as high-potential for conversion.
  - Session duration, first action time, and desktop visits were identified as the most influential features for segmentation.
key_figures_tables:
  - Table 6: Customer segmentation using RFMVDA yields 14 distinct segments, offering more nuance than the LRFM model.
  - Table 8: VDAR model segmentation of non-purchasers shows 1,711 customers in top segments likely to convert.
  - Figure 7: Training and validation loss over 200 epochs show minimal fluctuation, confirming good generalization.
  - Figure 9: SHAP analysis reveals session duration and first action time as the top features driving segmentation.
key_equations:
  - equation: L = -1/N \sum_{i=1}^{N} \sum_{j=1}^{C} t_{ij} log(y_{ij})
    explanation: Categorical cross-entropy loss for multi-class classification.
definitions:
  - term: RFMVDA
    definition: Recency, Frequency, Monetary, Visits, Durations, Actions model for customer classification.
  - term: VDAR
    definition: Visits, Durations, Actions, Referral Keyword model for non-purchasing customer segmentation.
  - term: CDP
    definition: Customer Data Platform for continuously storing and managing customer data.
  - term: DNN
    definition: Deep Neural Network used for classification.
  - term: SHAP
    definition: SHapley Additive exPlanations for feature importance analysis.
critical_citations:
  - "[Wei et al., 2010] — Reviews the application of the RFM model."
  - "[Wu et al., 2014] — Introduces the LRFM model for customer segmentation."
  - "[Sakar et al., 2019] — Uses LSTM for online shopper purchase prediction."
  - "[Wang, 2022] — Uses deep learning with swarm intelligence for customer segmentation."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Provides a benchmarking case for how traditional models (RFM) are adapted for modern digital platforms.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly addresses classifying customer behavior into detailed behavioral profiles for purchasing and non-purchasing users.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Proposes a DNN-based classification approach for customer segmentation using behavioral data.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: The model's segmentation can be used as a feature for predictive spending or churn models.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: contextual
      justification: While not forecasting, the modeling of sequential customer actions (sessions) provides a framework for handling sequential data.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides a rigorous evaluation methodology using metrics like accuracy, RMSE, and F1 scores.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Offers a comparative analysis (LRFM vs. RFMVDA) and robust cross-validation for evaluating the algorithmic module.
  contribution: The RFMVDA model provides a framework for behavioral segmentation in Odin, enabling detailed user profiling beyond simple transaction history. Its DNN-based classifier can be adapted for Odin's spending categorization and anomaly detection modules. The VDAR model offers a blueprint for handling cold-start users who have no transaction data. The study's emphasis on features like session duration and actions informs Odin's approach to user engagement and churn prediction.
  directly_justifies:
    - The RFMVDA model's integration of behavioral attributes enhances customer segmentation for e-commerce platforms.
    - Deep Neural Networks are well-suited for customer classification tasks involving multiple behavioral dimensions.
    - Including non-purchasing behavioral data is crucial for a complete understanding of customer journeys.
    - Session duration and page actions are critical indicators of customer intent and potential conversion.
  limits:
    - The analysis is based on a three-month dataset, which may not capture seasonal or long-term behavioral trends.
    - Direct comparisons with other machine learning algorithms (e.g., Random Forest) were not performed.
    - The applicability of the model to other domains, such as personal finance, is not directly validated.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was deemed most relevant to Behavioral Profiling & Classification (5.A, 5.C) and System Evaluation (12.A, 12.B) due to its core contribution of a new classification model and its rigorous evaluation. It offers medium relevance to Existing Systems & Gaps (4.A) by showing how traditional models are adapted. The paper's work on session-based behavior provides contextual relevance to Predictive Modeling (6.A, 6.B), as it frames how sequential data can be structured. Topics related to Filipino cultural context (2.A-D) were rejected as the study was conducted in South Korea and not culturally specific. Similarly, topics on budget recommendation, anomaly detection, and savings/debt management were rejected as they are not the focus of this customer segmentation research. Overall, the paper is highly relevant for informing Odin's user profiling and classification modules.
limitations:
  - The study only uses data from a single South Korean e-commerce platform over a short period.
  - The proposed model was not compared against other state-of-the-art deep learning architectures.
  - The paper lacks a direct discussion of how the DNN model handles imbalanced datasets.
  - The computational cost and scalability of the DNN model for real-time classification are not addressed. [unacknowledged]
remember_this:
  - Extended RFM with behavioral attributes improves classification accuracy.
  - The RFMVDA model achieved 92.98% prediction accuracy using a DNN.
  - Non-purchasing customers can be effectively segmented using the VDAR model.
  - Session duration and actions are key predictors of customer behavior.
  - Deep learning is suitable for modeling complex e-commerce customer interactions.
```
---

## Paper 2: Quindoza et al_summarized.md

**Source File:** `Quindoza et al_summarized.md`

```yaml
paper_id: 10.1108/SEAMJ-09-2024-0063
designation: local
title: Ang tagapagtaguyod na anak for Filipino adults: an exploratory research
authors: Quindoza, T.L.V.; Malcampo, M.C.; Rungduin, T.
year: 2025
venue: Southeast Asia: A Multidisciplinary Journal
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 4.A
  - 5.A
  - 5.B
  - 13.A
tldr: Explores the "tagapagtaguyod na anak" role in Filipino families as providing financial, emotional, and social support shaped by parental expectations and child volition.
problem_and_motivation: The breadwinner role in Filipino families lacks contextualization and is viewed narrowly as financial provision. There is a paucity of research on the broader responsibilities and cultural underpinnings of this role.
approach:
  - Explored perceptions of 16 Filipino adults in Metro Manila using semi-structured interviews.
  - Participants included single adult children aged 18-29 and middle-aged parents aged 40-60.
  - Thematic analysis was applied to identify patterns in understanding the phenomenon.
  - The study used an exploratory qualitative design to define the role and its influencing factors.
  - Findings were validated through participant and peer review.
findings:
  - "num: Majority of participants define tagapagtaguyod as nagbibigay (providing basic needs)."
  - The role involves financial, emotional, and social support, extending beyond a purely financial provider.
  - Eldest children are typically seen as fulfilling the role, but some participants associate it with middle children.
  - The role is influenced by extrinsic factors like poverty, parental incapacity, and intrinsic factors like volition and sense of responsibility.
  - Single adult children view the phenomenon negatively as unjust and mentally taxing, while parents view it positively as a sign of responsibility.
  - The phenomenon is rooted in Filipino values of family-orientedness and utang na loob.
key_figures_tables:
  - "Figure 1: Thematic map of understanding → Defines role via providing, bearing, leading, lifting."
  - "Figure 2: Thematic map of influencing factors → Shows extrinsic (poverty) and intrinsic (volition) factors."
  - "Figure 3: Thematic map of perspectives → Contrasts negative child views with positive parent views."
  - "Figure 4: Thematic map of Filipino values → Links role to family-orientedness and utang na loob."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Tagapagtaguyod na anak
    definition: A Filipino child who provides financial, emotional, and social support to their family.
  - term: Tagasalo
    definition: A personality or syndrome where a family member assumes caregiving or leadership roles.
  - term: Utang na loob
    definition: A Filipino value of gratitude or reciprocity towards family and others.
critical_citations:
  - "[Carandang, 1987] — Foundation for tagasalo theory used as study basis."
  - "[Udarbe, 2001] — Defines tagasalo personality themes for comparison."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Directly studies Filipino adults aged 18-29 as breadwinners.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Describes financial support roles and obligations within families.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Explores attitudes and motivations behind financial provision.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Examines the culturally rooted practice of familial financial support.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Mentions poverty as a driver, but not specific seasonal patterns.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Family needs context may imply spending cycles, but not central.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Mentions breadwinner phenomenon but not technology systems.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Profiles the tagapagtaguyod role and associated personality traits.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: low
      justification: Discusses role formation but not cold-start computational issues.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: Mentions financial support for family, but not savings goal systems.
  contribution: This paper informs Odin's user profiling module by describing the cultural and behavioral profile of a Filipino young professional who acts as a family financial provider. It directly supports the design of expense categorization by defining the types of support (financial, emotional) that shape spending. The findings on utang na loob and family-orientedness justify features that accommodate familial financial obligations in budget recommendations.
  directly_justifies:
    - "Filipino young adults often provide financial, emotional, and social support to their families."
    - "Cultural values like utang na loob and family-orientedness are central to financial behavior."
    - "The role is influenced by parental expectations and the child's sense of responsibility."
  limits:
    - "Findings are based on a small sample from Metro Manila only. [unacknowledged]"
    - "Predominance of female participants may have biased perceptions of gender roles. [unacknowledged]"
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The paper was found highly relevant to the Filipino Cultural Context domain (2.A, 2.D) and Behavioral Profiling (5.A) due to its detailed description of the culturally specific breadwinner role. It provided medium relevance to Financial Structure (1.B) and Financial Behavior (1.C) as it outlines the financial support dynamics. Low relevance was assigned to Expense Categorization (3.A) and Landscape of Existing Systems (4.A) because the paper focuses on the role itself rather than categorization systems or technology. Domains like Forecasting (6), Budget Recommendation (7), Anomaly Detection (8), and Mobile Design (9) were rejected as the paper does not address predictive modeling, algorithmic budget allocation, or UX design. The overall relevance to Odin lies in its rich contextual data on Filipino financial behavior and familial obligations.
limitations:
  - "Small sample size from Metro Manila limits generalizability. [unacknowledged]"
  - "Predominance of female participants may have biased perceptions. [unacknowledged]"
  - "The study captures perceptions, not lived experiences of tagapagtaguyod."
remember_this:
  - "Tagapagtaguyod na anak provides financial, emotional, and social support."
  - "Poverty and parental incapacity are key drivers of the role."
  - "Single adult children view the role as unjust and mentally taxing."
  - "The role is rooted in family-orientedness and utang na loob."
  - "Perceptions of the role differ significantly between generations."
---

## Paper 3: Yusuf et al_summarized.md

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

## Paper 4: Wang F. et al_summarized.md

**Source File:** `Wang F. et al_summarized.md`

```yaml
paper_id: 10.3390/s25010190
designation: international-algorithm-specific
title: A Survey of Deep Anomaly Detection in Multivariate Time Series: Taxonomy, Applications, and Directions
authors: Wang, F.; Jiang, Y.; Zhang, R.; Wei, A.; Xie, J.; Pang, X.
year: 2025
venue: Sensors
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
tldr: Comprehensive survey classifying deep learning MTSAD methods into forecasting, reconstruction, and contrastive paradigms with a taxonomy of anomaly types and application domains.
problem_and_motivation: Multivariate time series anomaly detection requires modeling complex temporal and inter-variable dependencies, which traditional statistical and machine learning methods struggle with. Deep learning offers powerful tools but lacks a unified, structured overview of techniques, paradigms, and applications to guide researchers and practitioners.
approach:
  - Proposes a new taxonomy for MTSAD methods based on learning paradigms (unsupervised, semi-supervised, self-supervised) and deep learning architectures.
  - Organizes methods into three primary strategies: forecasting-based, reconstruction-based, and contrastive-based anomaly detection.
  - Reviews and discusses 46 deep learning models including CNN, RNN, GNN, Transformer, VAE, GAN, and Diffusion-based approaches.
  - Compiles and organizes public MTSAD datasets, detailing their source, samples, dimensions, anomaly rate, and application domains.
  - Identifies open research issues, including contrastive learning, domain knowledge integration, benchmarking, and leveraging LLMs.
findings:
  - num: Transformers, GNNs, and hybrid models show superior performance in capturing spatio-temporal dependencies in MTS data.
  - num: Forecasting and reconstruction are the most common anomaly detection strategies, each with distinct advantages and drawbacks.
  - num: The survey covers 46 deep learning models across 10 application domains, highlighting the field's rapid expansion.
  - num: Contrastive learning and LLM-based methods are emerging as promising directions for improving anomaly detection accuracy and interpretability.
  - The taxonomy provides a structured framework that helps in selecting appropriate models based on data characteristics and application requirements.
key_figures_tables:
  - Figure 1: Classification of MTS anomaly types into intra-metric (temporal) and inter-metric anomalies → Anomalies occur within or between metrics.
  - Figure 2: Examples of point-wise and pattern-wise anomalies in MTS → Anomalies can be single-point spikes or unusual subsequences.
  - Figure 3: Examples of global and local inter-metric anomalies → Inter-metric anomalies involve broken correlations between variables.
  - Figure 4: General pipeline for MTSAD using deep learning models → Pipeline includes data processing, representation learning, and anomaly scoring.
  - Table 1: Overview of 46 deep learning models for MTSAD → Models are categorized by backbone, learning paradigm, and input type.
  - Table 2: Comprehensive list of public MTSAD datasets with application domains → Datasets span aerospace, cybersecurity, healthcare, and finance.
key_equations:
  - equation: X = (x1, x2, ..., xC)
    explanation: MTS X is defined as a collection of C univariate time series.
  - equation: S = (s1, s2, ..., sT)
    explanation: Anomaly scores S are computed for each time point t.
  - equation: |x_t - \hat{x}_t| > \delta
    explanation: Global point anomaly detection where deviation exceeds threshold.
  - equation: X_k = \sum_{t=0}^{T-1} x_t e^{-i2\pi kt/T}
    explanation: Discrete Fourier Transform for frequency domain analysis.
definitions:
  - term: MTSAD
    definition: Multivariate Time Series Anomaly Detection, identifying unusual patterns in multi-dimensional time series data.
  - term: Forecasting-based
    definition: Anomaly detection by comparing predicted future values with actual observations.
  - term: Reconstruction-based
    definition: Anomaly detection by measuring the error in reconstructing input data from a latent representation.
  - term: Contrastive-based
    definition: Anomaly detection by learning representations that maximize similarity between normal instances and dissimilarity with anomalies.
  - term: Intra-metric anomaly
    definition: Temporal anomaly occurring within a single metric or variable.
  - term: Inter-metric anomaly
    definition: Anomaly arising from broken relationships or correlations between multiple metrics.
critical_citations:
  - "[Hundman et al., 2018] — Introduced LSTM-NDT for spacecraft anomaly detection."
  - "[Deng & Hooi, 2021] — Proposed GDN using GNNs for MTS anomaly detection."
  - "[Xu et al., 2022] — Developed AnomalyTransformer with association discrepancy."
  - "[Su et al., 2019] — Proposed OmniAnomaly for robust MTS anomaly detection."
  - "[Audibert et al., 2020] — Introduced USAD for fast unsupervised MTS anomaly detection."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Reviews forecasting-based anomaly detection methods directly applicable to predicting spending anomalies.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Evaluates RNN, Transformer, and GNN models for sequential data forecasting.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Provides a comprehensive taxonomy and methods for anomaly detection in multivariate time series.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Reviews deep learning algorithms (VAE, GAN, Transformer) applicable to spending pattern anomalies.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Mentions privacy in cybersecurity datasets but does not focus on user financial data privacy.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: contextual
      justification: Discusses interpretability via XAI but not user trust specifically.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Reviews benchmarking datasets and evaluation metrics for anomaly detection.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Compares performance of various deep learning models on public datasets.
  contribution: "This survey directly informs Odin's predictive modeling and anomaly detection modules by providing a structured taxonomy of state-of-the-art deep learning methods for multivariate time series. The review of forecasting, reconstruction, and contrastive approaches offers design choices for implementing spending prediction and anomaly detection. The compiled dataset list and evaluation metrics can guide Odin's system evaluation framework. The discussion of open challenges, such as leveraging LLMs and integrating domain knowledge, suggests future enhancements for Odin's algorithmic modules."
  directly_justifies:
    - "Forecasting-based models can predict future spending and flag deviations as anomalies."
    - "Reconstruction-based models can detect anomalies by identifying patterns that do not conform to normal spending behavior."
    - "Contrastive learning can improve anomaly detection by learning discriminative representations of normal versus abnormal spending."
    - "LLMs can be adapted for time series anomaly detection in PFMS with appropriate prompting and fine-tuning."
  limits:
    - "Survey does not provide empirical comparisons or performance benchmarks across all reviewed models."
    - "Focuses on general MTSAD without specific application to personal finance or spending data."
    - "Limited discussion on real-time deployment considerations and computational resource constraints for mobile PFMS."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. High relevance was assigned to Predictive Modeling (6.A, 6.B) and Anomaly Detection (8.A, 8.B) because the paper's core contribution is a comprehensive review of deep learning methods for these tasks in MTS data. Medium relevance was assigned to System Evaluation (12.A, 12.B) as the paper reviews datasets and benchmarking practices. Contextual relevance was assigned to Data Privacy (10.A) and User Trust (10.B) due to passing mentions of security and interpretability, but no direct focus on user financial data or trust mechanisms. Domains like Filipino Cultural Context (2.A–2.D), Expense Categorization (3.A–3.C), Behavioral Profiling (5.A–5.C), and Savings/Debt Management (13.A–13.C) were considered but rejected as the paper does not address cultural, behavioral, or PFMS-specific financial management aspects. The paper's overall relevance to Odin lies in providing a foundational review of anomaly detection algorithms that can be adapted for spending anomaly detection and forecasting."
limitations:
  - "Survey does not provide empirical comparisons or performance benchmarks across all reviewed models."
  - "Focuses on general MTSAD without specific application to personal finance or spending data."
  - "Limited discussion on real-time deployment considerations and computational resource constraints for mobile PFMS. [unacknowledged]"
  - "Does not address the integration of user-declared financial preferences or constraints in anomaly detection. [unacknowledged]"
remember_this:
  - "MTSAD methods are classified into forecasting, reconstruction, and contrastive paradigms."
  - "Transformers and GNNs are leading architectures for capturing complex spatio-temporal dependencies."
  - "Contrastive learning and LLMs are emerging trends for improved anomaly detection."
  - "Anomalies can be point-wise, pattern-wise, or inter-metric, requiring diverse detection strategies."
  - "46 deep learning models reviewed across 10 application domains."
```
---

## Paper 5: Agrawal et al_summarized.md

**Source File:** `Agrawal et al_summarized.md`

```yaml
paper_id: 10.1007/s44196-025-00899-0
designation: international-algorithm-specific
title: Analyzing and Rewarding Credit Card Spending Habits in India: a Machine Learning Approach
authors: Agrawal, R.; Khanna, A.; Hamdare, S.
year: 2025
venue: International Journal of Computational Intelligence Systems
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 7.C
  - 12.A
  - 12.B
  - 12.C
tldr: Machine learning segments users and predicts spending to optimize credit card reward allocation, achieving an R2 of 0.99.
problem_and_motivation: Traditional credit card reward programs use static, one-size-fits-all structures that fail to personalize incentives for diverse spending behaviors. This lack of adaptability misses opportunities to retain high-value customers and encourage discretionary spending in profitable categories. A tailored, data-driven system is needed to optimize reward allocation and enhance customer engagement.
approach:
  - K-Means clustering segments users by spending behavior and card type (Platinum, Gold, Silver, Signature) using features like monthly spend and transaction frequency.
  - Synthetic data generation using Faker and feature engineering creates a rich dataset with attributes such as expense type, income, and attrition risk.
  - A custom reward points formula incorporates card type, promotion date, expense type, income, number of cards, and attrition risk to calculate personalized points.
  - Linear Regression, Random Forest, and XGBoost models predict reward points to validate the proposed formula's effectiveness.
  - Model performance is evaluated using R2, RMSE, and MAE to compare predictive accuracy.
findings:
  - "num: K-Means achieved a Silhouette Score of 0.42, outperforming DBSCAN and GMM for user segmentation by card type."
  - "num: Random Forest and XGBoost achieved an R2 value of 0.99, indicating near-perfect fit for reward point prediction."
  - "num: The synthetic dataset's reward points distribution ranged from 0 to 3500, compared to 0 to 1000 for the limited original dataset."
  - Clustering analysis clearly separated users into four distinct groups corresponding to Platinum, Gold, Silver, and Signature cardholders.
  - The proposed personalized reward formula allocated higher points for discretionary spending like travel and luxury, incentivizing profitable categories.
  - Including additional features like attrition risk and income category led to a more systematic and justified reward calculation process.
key_figures_tables:
  - "Figure 5: 3D visualization of K-Means clusters → Clear separation of four card-type based user segments."
  - "Figure 6: Reward point distribution comparison → Synthetic data enables broader and more justified point allocation."
  - "Figure 7: Cumulative distribution of reward points → Spending type influences reward allocation systematically."
  - "Table 4: Base reward points by card type → Platinum earns 5 points, Silver earns 2 points per 500 spent."
  - "Table 6: Expense type bonus points → Travel/Dining earns +3.0, Groceries/Bills earns +0.5."
key_equations:
  - equation: "RewardPoints(Olddataset) = (PointsScored(BasedonCardType) * AmountSpentMonthly) / 500"
    explanation: "Calculates points using only card type and amount spent."
  - equation: "RewardPoints(SyntheticDataset) = (ScoredPoints * AmountSpent) / 500, where ScoredPoints = [RCT + CPD + ET + IC + NoC + AR]"
    explanation: "Multi-factor formula for personalized reward point calculation."
definitions:
  - term: "RCT"
    definition: "Base multiplier based on Card Type for reward calculation."
  - term: "CPD"
    definition: "Card Promotion Date bonus for reward points."
  - term: "ET"
    definition: "Expense Type bonus based on spending category."
  - term: "IC"
    definition: "Income Category bonus for reward calculation."
  - term: "NoC"
    definition: "Number of Cards penalty for holding multiple cards."
  - term: "AR"
    definition: "Attrition Risk bonus to incentivize loyalty."
  - term: "DBI"
    definition: "Davies-Bouldin Index, a clustering validation metric."
critical_citations:
  - "[Cheema & Van der Stede, 2019] — Reward programs tailored to high-spending categories enhance engagement."
  - "[Li, Ngai, & Hu, 2021] — ML applications in finance include K-Means for segmentation."
  - "[Gan, Xu, & Chen, 2021] — Ensemble models like XGBoost predict consumer behavior in high-value categories."
  - "[Sun & Vasarhelyi, 2018] — Deep neural networks applied to predict credit card delinquencies."
  - "[Sadat Akash, 2024] — Credit Card Transaction Dataset used for training predictive models."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Directly segments users into behavioral profiles (e.g., luxury spenders) using clustering."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "medium"
      justification: "Synthetic data generation addresses data limitations for profile initialization."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Compares K-Means, DBSCAN, and GMM for behavioral profile classification."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Applies Linear Regression, Random Forest, and XGBoost to predict reward points."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "medium"
      justification: "Monthly spending trends analysis with synthetic data for forecasting."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "contextual"
      justification: "Reward optimization provides a framework analogous to budget allocation."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Reward structure offers a basis for personalized recommendation systems."
    - code: "7.C"
      name: "Constrained Optimization Approaches for Budget Allocation"
      relevance: "low"
      justification: "Reward points formula incorporates constraints like penalty for multiple cards."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Uses R2, RMSE, MAE to evaluate predictive model performance."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Evaluates clustering (Silhouette, DBI) and prediction (R2) modules."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "medium"
      justification: "Model performance comparison informs evaluation of recommendation systems."
  contribution: "This paper provides a data-driven framework for user segmentation and personalized incentive design applicable to Odin's expense categorization and budget recommendation modules. The K-Means clustering approach can inform Odin's behavioral profiling to classify users by spending habits. The multi-factor reward formula demonstrates a method for optimizing allocation based on user attributes, which parallels Odin's budget recommendation logic. The model evaluation metrics (R2, RMSE) offer a standard for assessing Odin's predictive modules. The framework's focus on incentivizing discretionary spending provides insights into engagement and retention mechanisms."
  directly_justifies:
    - "K-Means clustering effectively segments users by card type and spending behavior."
    - "Multi-factor reward formulas can personalize incentives based on user attributes."
    - "Random Forest achieves superior accuracy for predicting reward points."
    - "Synthetic data enables robust model development when real data is limited."
    - "Including attrition risk in reward calculation can support customer retention."
  limits:
    - "Study uses synthetic data, not real credit card transaction data."
    - "Reward points multipliers are subjective and not based on real industry data."
    - "Generalizability to other financial domains or countries is not evaluated."
    - "Real-time adaptability of the reward system is proposed but not implemented."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was conducted. The paper was flagged as highly relevant to Behavioral Profiling & Classification (5.A, 5.C) due to its K-Means user segmentation, and to Spending Forecasting (6.A, 6.B) for its predictive modeling. It also showed high relevance to System Evaluation (12.A, 12.B) through its use of R2, RMSE, and MAE. Medium relevance was assigned to Budget Recommendation (7.B) for the personalized reward formula's parallel to allocation logic, and Profile Dynamics (5.B) for its synthetic data approach addressing the cold-start problem. Low relevance was noted for Constrained Optimization (7.C) due to the simple penalty structure. Contextual relevance was assigned to Budgeting Strategies (7.A). Domains like Filipino Cultural Context (2.A-D), Expense Categorization (3.A-C), Existing Systems (4.A-B), Mobile-First Design (9.A-B), Data Privacy (10.A-B), User Retention (11.A-B), and Savings & Debt Management (13.A-C) were considered and rejected because the paper does not address cultural practices, expense categorization frameworks, PFMS landscape, mobile design, privacy concerns, engagement dynamics, or savings/debt management specifically. Overall, the paper's machine learning approach to user segmentation and personalized incentive optimization is highly relevant to Odin's core modules for behavioral profiling, forecasting, and recommendation."
limitations:
  - "Reliance on synthetically generated data limits real-world applicability. [unacknowledged]"
  - "Reward point multipliers are arbitrary and may not reflect actual credit card company practices. [unacknowledged]"
  - "The study does not validate the reward formula's impact on actual customer retention or spending. [unacknowledged]"
  - "Generalizability to Philippine financial context or Filipino young professionals is not addressed."
remember_this:
  - "K-Means clustering achieved 0.42 Silhouette Score for user segmentation."
  - "Random Forest and XGBoost both achieved R2 of 0.99 for reward prediction."
  - "Personalized rewards incentivize discretionary spending like travel and luxury."
  - "Synthetic data enables robust model development with limited real data."
  - "Multi-factor formulas enable dynamic and fair reward allocation."
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

## Paper 7: Mandaleeka_summarized.md

**Source File:** `Mandaleeka_summarized.md`

```yaml
paper_id: 10.63282/3050-922X.ICRCEDA25-143
designation: international-algorithm-specific
title: Explainable and Context-Aware Financial Nudges via Event-Driven Microservices
authors: Mandaleeka, A. P.
year: 2025
venue: International Journal of Emerging Research in Engineering and Technology, ICRCEDA2025 Conference Proceeding
odin_topics:
  - 3.A
  - 3.C
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 8.A
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 13.A
tldr: A microservices framework delivers real-time financial nudges enhanced by SHAP-based explanations, increasing user engagement and trust.
problem_and_motivation: Existing financial alerts are generic and lack transparency, causing user distrust and low engagement. There is a gap in integrating real-time personalization with explainable AI in scalable fintech architectures. The paper addresses this by proposing a modular system that combines context-awareness with interpretable decision-making.
approach:
  - Data ingestion from bank APIs, user behavior logs, and optional geolocation via Kafka topics.
  - Context processor enriches transactions with historical spending, budget goals, and temporal patterns.
  - Nudge decision engine uses rule-based logic or a trained ML model to classify events as nudge-worthy.
  - XAI module applies SHAP to generate feature attributions and convert them into natural-language explanations.
  - Notification service delivers formatted alerts via in-app, email, or chatbot with optional SHAP visualizations.
  - System is evaluated on synthetic and anonymized datasets to simulate diverse user behaviors.
findings:
  - Contextual triggers such as time, location, and prior habits increase user engagement.
  - Explainability boosts users' perceived relevance and trust in the system.
  - The modular architecture enables scalability, fault isolation, and data minimization.
  - SHAP provides local interpretability and supports model debugging and bias detection.
key_figures_tables:
  - Figure 1: Overview of the nudge system architecture → shows high-level data flow and services.
  - Figure 2: Detailed microservices and Kafka topics → illustrates modular, event-driven design.
  - Figure 3: Data ingestion pipeline → demonstrates transaction flow through context processor and nudge engine.
  - Table 1: SHAP attribution values for features → example of how spending and budget features contribute to nudge decision.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: SHAP
    definition: SHapley Additive exPlanations, a model-agnostic method for interpreting predictions by attributing contributions to input features.
  - term: XAI
    definition: Explainable Artificial Intelligence, techniques that make AI decisions understandable to humans.
  - term: Kafka
    definition: A distributed event-streaming platform for building real-time data pipelines and streaming applications.
critical_citations:
  - "[Lundberg and Lee, 2017] — foundational SHAP framework for model interpretability."
  - "[Kreps et al., 2011] — Kafka distributed messaging system for log processing."
  - "[Kim and Woo, 2021] — XAI framework for financial rating models."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Paper uses transaction categories for budget tracking, informing categorization frameworks.
    - code: 3.C
      name: User-Defined Allocation Constraints
      relevance: medium
      justification: User-defined budget thresholds and goals are central to nudge logic.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Paper reviews existing fintech systems like Cleo and Revolut, establishing the landscape.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies lack of explainability and generic alerts as key gaps.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Behavioral signals inform personalization, relevant to profiling.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: ML classification of nudge-worthy events aligns with behavioral classification approaches.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Spending spikes and threshold violations detected as anomalies trigger nudges.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Dedicated security and privacy section with OAuth, encryption, and consent management.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Explainability directly builds user trust; user study evidence cited.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: Focus on engagement dynamics through personalized, timely nudges.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: Nudges serve as retention mechanisms; system designed for repeated interaction.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Savings opportunities and goal reminders align with savings goal management.
  contribution: |
    The paper's microservices-based architecture with SHAP directly informs Odin's notification and explanation modules, enabling transparent spending alerts. The context-aware data pipeline, integrating transaction history, geolocation, and behavioral signals, can be adapted for Odin's behavioral profiling and anomaly detection. The emphasis on user trust via explainability and data privacy mechanisms supports Odin's design for ethical AI. The use of Kafka for event-driven scalability provides a blueprint for Odin's real-time processing and modular deployment.
  directly_justifies:
    - Explainability boosts users' perceived relevance and trust in financial nudges.
    - Contextual triggers (time, location, prior habits) increase user engagement.
    - Event-driven microservices enable scalable, fault-tolerant real-time processing.
    - SHAP provides transparent, individualized explanations for nudge decisions.
  limits:
    - Evaluation performed on synthetic and anonymized datasets, not real-world user studies.
    - SHAP computational cost requires optimizations like caching; may be expensive at scale.
    - The paper does not address cold-start scenarios for new users.
  mapping_rationale: |
    A systematic scan across all 12 functional domains and associated topics identified strong relevance to Engagement & Retention, Data Privacy & User Trust, and Existing Systems & Gaps. The paper directly addresses user trust (10.B) and privacy (10.A) through dedicated sections, and engagement (11.A) via nudging; it also reviews existing systems (4.A) and their limitations (4.B). Moderate relevance was found for Expense Categorization (3.A) and User-Defined Allocation (3.C) as the system uses budget thresholds and categories. Behavioral profiling (5.A) and classification (5.C) are touched via behavioral signals and ML decisioning; anomaly detection (8.A) is applicable due to spending spike detection. Savings management (13.A) is partially covered via savings opportunities and goal reminders. Topics related to Filipino cultural context (2.A-2.D), spending forecasting (6.A-6.B), budget recommendation optimization (7.A-7.D), mobile-first design (9.A-9.B), and system evaluation (12.A-12.C) were considered but rejected due to lack of emphasis or specificity. Borderline cases included seasonal spending (2.B) mentioned in passing but not culturally specific, and budget recommendation (7.A) referenced only as budget goals, not recommendation algorithms. Overall, the paper provides strong support for Odin's trust, engagement, and architectural modularity.
limitations:
  - Evaluation performed on synthetic and anonymized datasets, not real-world user studies.
  - SHAP computational cost requires optimizations like caching; may be expensive at scale.
  - The paper does not address cold-start scenarios for new users.
remember_this:
  - Explainable nudges increase user trust and perceived relevance.
  - Context-aware triggers boost engagement compared to generic alerts.
  - Modular microservices with Kafka enable scalable real-time financial advice.
```
---

## Paper 8: Chen & Tan_summarized.md

**Source File:** `Chen & Tan_summarized.md`

```yaml
paper_id: "10.1145/3785706.3785906"
designation: "international-algorithm-specific"
title: "LSTM-Based Consumer Behavior Prediction Model Research"
authors: "Chen, S.; Tan, W."
year: 2025
venue: "2025 2nd International Conference on Digital Economy and Computer Science (DECS 2025)"
odin_topics:
  - "6.A"
  - "6.B"
  - "5.C"
  - "12.B"
tldr: "An LSTM-based model with self-attention predicts consumer purchase intention using sequential behavioral data, achieving 94.2% accuracy."
problem_and_motivation: "Traditional consumer behavior analysis methods like regression and decision trees struggle with large-scale, multi-dimensional data and fail to capture temporal dependencies. Deep learning techniques have shown promise in complex pattern recognition, but a robust model for e-commerce purchase prediction is lacking. This study addresses the gap by leveraging LSTM networks to accurately forecast consumer purchasing behavior."
approach:
  - "Data preprocessing uses Apache Spark on 500,000 users with 80 million interaction records, applying sliding windows (30 days, 50% overlap) and extracting 128-dimensional features."
  - "The model architecture includes an embedding layer, bidirectional LSTM with 512 hidden units, self-attention with adaptive temporal weighting (alpha_t = softmax(e_t)), and a softmax output for five-class purchase intention."
  - "Optimization employs Adam with cosine annealing learning rate (0.001 to 0.0001), weighted cross-entropy loss, L2 regularization (λ=0.001), and gradient clipping (threshold 1.0)."
  - "Dropout scheduling starts at 0.5 for first 30 epochs, then linearly decreases to 0.3 for remaining training to balance regularization and fine-tuning."
  - "Training uses batch size 128, early stopping with patience 10, mixed-precision FP16, and data augmentation (temporal jitter, noise injection) to enhance robustness."
  - "Evaluation compares against logistic regression, random forest, SVM, basic RNN, and standard LSTM using accuracy, precision, recall, F1-score, and 10-fold cross-validation."
findings:
  - "num: The proposed LSTM achieves 94.2% accuracy, 93.8% precision, 94.7% recall, and 94.2% F1-score."
  - "num: It outperforms the best baseline (standard LSTM) by 3.0 percentage points and traditional ML methods by 10.7 percentage points on average."
  - "num: Statistical significance testing (p < 0.001) confirms performance improvements across user segments."
  - "num: High-frequency users achieve 96.1% accuracy, new users 91.8% (23.6% improvement over traditional methods), and high-value customers 96.7%."
  - "num: The self-attention mechanism improves key feature identification accuracy by 12.5%."
  - "Behavioral features (purchase frequency, browsing duration, price sensitivity) dominate predictive power with cumulative importance score 0.521."
  - "Ablation experiments show removing any Top-5 feature causes a 3.2 percentage point performance drop."
key_figures_tables:
  - "Table 2: Performance comparison across models → Proposed LSTM achieves highest metrics across all categories."
  - "Table 3: Performance by user groups → Model generalizes well, with new users at 91.8% accuracy."
  - "Figure 3: Training loss curves → Proposed LSTM converges faster and with lower final loss than traditional methods."
  - "Figure 4: Attention weight visualization → Recent behaviors and behavioral features receive highest attention weights."
key_equations:
  - equation: "α_t = softmax(e_t)"
    explanation: "Attention weight for timestep t based on score e_t."
definitions:
  - term: "LSTM"
    definition: "Long Short-Term Memory, a recurrent neural network architecture with gating mechanisms to capture long-term dependencies."
  - term: "RNN"
    definition: "Recurrent Neural Network, a class of neural networks for sequential data."
  - term: "SVM"
    definition: "Support Vector Machine, a supervised learning model for classification."
  - term: "AUC-ROC"
    definition: "Area Under the Receiver Operating Characteristic curve, a performance metric for binary classification."
  - term: "SHAP"
    definition: "SHapley Additive exPlanations, a method for interpreting model predictions."
critical_citations:
  - "None."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "The paper presents a predictive model for consumer behavior using LSTM, directly applicable to spending forecasting in Odin."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "The LSTM with self-attention is designed for sequential data forecasting, matching Odin's need for spending prediction."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "The model classifies users into purchase intention levels, informing profile classification methods."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "The paper provides extensive evaluation metrics and comparisons, useful for evaluating Odin's forecasting modules."
  contribution: "The LSTM-based forecasting approach can directly inform Odin's spending prediction module (6.A). The self-attention mechanism for temporal weighting could enhance Odin's ability to capture seasonal and cyclical spending patterns. The evaluation methodology using accuracy, precision, recall, and F1-score provides a template for Odin's algorithmic evaluation. The handling of new users with limited data offers strategies for Odin's cold-start problem in behavioral profiling."
  directly_justifies:
    - "LSTM networks effectively capture long-term dependencies in consumer behavior sequences."
    - "The model achieves 94.2% accuracy in predicting purchase intention using sequential data."
    - "Attention mechanisms improve key feature identification by 12.5%."
    - "Behavioral features like purchase frequency are more predictive than demographic features."
  limits:
    - "The paper focuses on e-commerce purchase prediction, not personal finance spending, limiting direct transferability."
    - "Error analysis reveals challenges with impulsive purchasing and external event-driven consumption, which Odin may also face."
    - "The model requires large-scale data and may not perform as well with sparse data typical of new users in Odin."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was found directly relevant to spending forecasting (6.A and 6.B) with high relevance, as it proposes an LSTM-based model for sequential purchase prediction. It also informs behavioral profiling (5.C) with medium relevance via its classification of users into intention levels, and evaluation frameworks (12.B) with medium relevance due to its comprehensive performance metrics. Borderline cases: the paper touches on seasonal patterns (2.B) but lacks Filipino cultural context, so was rejected; it mentions traditional method limitations (4.B) but does not review PFMS systems, so rejected; it does not address budget allocation (7.A–D) or anomaly detection (8.A–C), so those were rejected. Overall, the paper provides strong methodological support for Odin's predictive modules, though it is not domain-specific to Filipino young professionals."
limitations:
  - "The model is evaluated on e-commerce data, not personal financial transactions, limiting direct applicability to Odin's spending data. [unacknowledged]"
  - "The paper does not address real-time prediction constraints or mobile deployment, which are critical for Odin. [unacknowledged]"
  - "The reliance on large-scale data may not generalize to low-data scenarios common in early adoption of Odin. [unacknowledged]"
  - "The study does not consider privacy-preserving techniques, which are essential for Odin. [unacknowledged]"
  - "The model's performance on new users (91.8%) is reported but not deeply analyzed for cold-start issues. [unacknowledged]"
remember_this:
  - "LSTM with attention achieves 94.2% accuracy for purchase prediction."
  - "Behavioral features like frequency and duration are most predictive."
  - "The model generalizes well to new users with 91.8% accuracy."
  - "Attention weighting highlights recent behaviors and seasonal patterns."
  - "Dropout scheduling from 0.5 to 0.3 improves training stability."
```
---

## Paper 9: Espiritu M.-2025_summarized.md

**Source File:** `Espiritu M.-2025_summarized.md`

```yaml
paper_id: 10.69569/jip.2025.063a
designation: local
title: Knowledge, Attitudes, and Practices in Financial Literacy among Business Administration Students in Urban College in the Philippines
authors: Espiritu, M. J.
year: 2025
venue: Journal of Interdisciplinary Perspectives
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 3.A
  - 5.A
  - 10.A
tldr: Assesses financial knowledge, attitudes, and practices of business students in a Philippine urban college, finding significant links between demographics and financial literacy.
problem_and_motivation: Filipino young adults, particularly business students, exhibit low financial literacy, yet their specific knowledge, attitudes, and practices remain underexplored. Understanding these factors is critical for designing effective financial education. This study addresses this gap by examining these dimensions within a local urban college context.
approach:
  - Conducted a survey-based quantitative study with 2,313 Business Administration students at a college in Quezon City.
  - Employed a structured questionnaire to measure financial knowledge, attitudes, and practices across five concepts: income, expenses, debt, credit, and savings.
  - Used descriptive statistics to assess mean scores and inferential statistics (ANOVA) to analyze differences based on demographic profiles.
  - Examined the relationship between knowledge, attitudes, and practices using Pearson correlation.
findings:
  - num: Students generally agreed on their financial knowledge, with mean scores ranging from 2.98 to 3.13 for income, expenses, debt, credit, and savings.
  - num: A significant relationship exists between financial knowledge, attitudes, and practices (R=0.697, p=0.000).
  - Financial knowledge and attitudes varied significantly by age, sex, and year level, but monthly family income showed no significant effect on knowledge.
  - Financial practices varied significantly across all demographic variables: age, sex, monthly income, and year level.
  - Monthly family income significantly influenced attitudes but not knowledge, suggesting resource access affects attitudes more than comprehension.
key_figures_tables:
  - Table 1: Distribution of 2,313 respondents by age, sex, income, and year level → Majority are male (65.9%), aged 18-20 (48.9%), with income of 10,001-20,000 PHP.
  - Table 5: ANOVA results for demographic differences in KAP → Knowledge and attitudes vary by age and year level; practices vary by all demographics.
  - Table 6: Correlation among knowledge, attitude, and practice → Strong significant relationship, R=0.697, justifying the KAP framework.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: KAP
    definition: Knowledge, Attitudes, and Practices framework for assessing financial literacy.
  - term: PFMS
    definition: Personal Financial Management System.
critical_citations:
  - "[Lusardi, 2019] — Highlights the need for financial literacy due to complex financial products."
  - "[Chen & Volpe, 1998] — Foundational study on low financial literacy among college students."
  - "[Martinez, 2024] — Reports low financial literacy rates among Filipinos, providing context."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Directly studies Filipino college students, a primary demographic for Odin.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Provides baseline data on income, expenses, and debt understanding of students.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Assesses financial practices and attitudes, core to understanding behavior.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Grounds financial literacy in a Philippine urban college context, reflecting local norms.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: The study assesses understanding of fixed/variable expenses, informing category design.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly measures financial attitudes and practices, which are key for behavioral profiling.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Mentioned in introduction regarding cybersecurity risks, but not a focus.
  contribution: The paper provides empirical evidence on the financial literacy levels of Filipino business students, a key target demographic for Odin. It validates the KAP framework for understanding financial behavior in this population. The findings on demographic differences (age, sex, income) can inform how Odin personalizes its expense categorization and behavioral profiling modules. The strong correlation between knowledge and practices underscores the need for Odin's educational and feedback features to drive better financial outcomes.
  directly_justifies:
    - "Business students in the Philippines show significant variation in financial knowledge and practices by age and year level, requiring personalized system inputs."
    - "The strong relationship between financial knowledge, attitudes, and practices supports Odin's integrated approach to education and behavior change."
    - "Monthly family income significantly affects financial attitudes and practices, indicating a need for adaptive budgeting and savings recommendations in Odin."
  limits:
    - "The study uses self-reported data, which may not reflect actual financial behaviors."
    - "The sample is limited to business administration students, reducing generalizability to all young professionals."
    - "Focuses on knowledge assessment rather than testing actual financial decision-making skills."
  mapping_rationale: A systematic scan across all 12 functional domains was conducted. The paper was flagged as highly relevant to the 'Behavioral Profiling & Classification' and 'Filipino Cultural Context' domains due to its direct measurement of financial knowledge, attitudes, and practices among Filipino students. It provides medium relevance to 'Expense Categorization' as it assesses understanding of expense types, and low relevance to 'Data Privacy' due to a brief mention. Domains like 'Spending Forecasting', 'Budget Recommendation', and 'Anomaly Detection' were rejected as the paper does not address predictive modeling or algorithmic approaches. The paper's overall relevance to Odin is high, as it offers foundational behavioral data essential for profiling and personalizing the system for its Filipino user base.
limitations:
  - "Self-reported data may not accurately reflect actual financial practices."
  - "Sample limited to business students in one urban college, limiting generalizability."
  - "Cross-sectional design captures a snapshot, not longitudinal behavior change."
  - "The instrument's internal consistency for financial knowledge (0.459) is low, suggesting potential measurement issues [unacknowledged]."
remember_this:
  - "Financial literacy levels among Filipino business students vary significantly by age, sex, and year level."
  - "Strong correlation exists between financial knowledge, attitudes, and practices in this population."
  - "Monthly family income affects financial attitudes and practices but not knowledge, highlighting a critical insight for financial education."
  - "The KAP framework is validated for assessing financial literacy among Filipino students."
```
---

## Paper 10: Caroprese et al_summarized.md

**Source File:** `Caroprese et al_summarized.md`

```yaml
paper_id: 10.1145/3707693
designation: international-algorithm-specific
title: Modelling Concept Drift in Dynamic Data Streams for Recommender Systems
authors: Caroprese, L.; Pisani, F. S.; Veloso, B. M.; Konig, M.; Manco, G.; Hoos, H.; Gama, J.
year: 2025
venue: ACM Transactions on Recommender Systems
odin_topics:
  - 5.A
  - 5.B
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
tldr: A stream-based data generator models user preferences with latent embeddings and simulates concept drift via tripartite graph changes, enabling realistic synthetic data for recommender system evaluation.
problem_and_motivation: Recommender systems assume static user preferences, but real-world data streams exhibit concept drift. Public datasets are limited and lack dynamic characteristics, hindering algorithm development and evaluation.
approach:
  - The model uses Bayesian Personalized Ranking (BPR) with latent embeddings for users and items to infer preferences based on geometric closeness.
  - Concept drift is detected using HDDM_W, a drift detection method based on Hoeffding's bounds with moving average.
  - Upon drift, the model is extended with new latent dimensions and retrained on current data while penalizing deviation from the previous model.
  - Synthetic data is generated by sampling from the learned model, using user and item popularity distributions (Zipf).
  - A general generator is proposed with six drift policies (user drift, new trends, new users/items, churn, obsolescence) to create controllable drift scenarios.
findings:
  - num: HR@5 on MIND dataset ranges from 0.6 to 0.7, with performance recovering after drift detection and retraining.
  - The synthetic data's frequency distribution closely matches the real data, confirmed by Kolmogorov-Smirnov test on MIND.
  - When users and items are inverted (more users than items), the generator fidelity improves significantly.
  - The adaptive BPR model outperforms a non-adaptive variational autoencoder when the item catalog grows over time.
  - Drift detection triggers structural model updates (adding latent dimensions) to adapt to changing preferences.
key_figures_tables:
  - Figure 3: Loss on test set for MIND dataset → Drifts are visible as spikes in loss, triggering model updates.
  - Figure 5: Comparison of real and synthetic frequency distributions for MIND → Synthetic matches real closely.
  - Figure 8: Comparison for Amazon Video Games → Poor match due to insufficient item preferences per user.
  - Figure 13: Improved match after inverting roles → Sufficient preferences per item improve generation.
key_equations:
  - equation: "\mathcal{L}_{bpr}(M|V) = \sum_{u}\sum_{i \succ_u j} \log \sigma(p_u^T(q_i - q_j))"
    explanation: BPR loss for optimizing user and item embeddings from pairwise preferences.
  - equation: "L_c(M;R) = \mathcal{L}_{bpr}(M|R) + \lambda(||P||_\infty + ||Q||_\infty)"
    explanation: Regularized loss for drift detection, bounding matrix weights.
  - equation: "L_d(M';M,R^{(t)}) = L_c(M';R^{(t)}) + \delta\sum_{u,k}|p'_{u,k}-p_{u,k}| + ..."
    explanation: Loss for adapting model after drift, penalizing embedding changes.
definitions:
  - term: BPR
    definition: Bayesian Personalized Ranking, a pairwise ranking optimization method for implicit feedback.
  - term: MF
    definition: Matrix Factorization, a collaborative filtering technique using latent factors.
  - term: HDDM_W
    definition: Hoeffding Drift Detection Method with weighted moving average, a concept drift detector.
critical_citations:
  - "[Rendle et al., 2009] — Foundation for BPR model used."
  - "[Frías-Blanco et al., 2015] — HDDM_W drift detection method."
  - "[Gama et al., 2004] — Early drift detection method (DDM) referenced."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Models user preference dynamics, directly applicable to profiling spending behavior.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: high
      justification: Addresses concept drift and changing user preferences, key for evolving profiles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Provides methods to handle concept drift in predictive models for spending forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Discusses sequential data and drift adaptation, relevant to spending forecasting.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Concept drift detection can inform anomaly detection by distinguishing normal changes from outliers.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Proposes drift detection algorithms that could be adapted for anomaly detection in spending.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Synthetic data generation aids evaluation of PFMS algorithms under dynamic conditions.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: The generator can be used to evaluate algorithmic robustness to concept drift.
  contribution: This paper's concept drift modeling can inform Odin's spending forecasting module by enabling adaptation to changing user spending patterns. Its drift detection methods can be integrated into anomaly detection to distinguish between genuine anomalies and normal preference shifts. The synthetic data generation approach provides a framework for evaluating Odin's algorithmic modules under realistic dynamic conditions. The emphasis on implicit feedback and user/item embeddings is relevant for profiling user financial behavior.
  directly_justifies:
    - Concept drift in user preferences can be modeled via latent embedding changes.
    - Drift detection methods like HDDM_W can trigger model retraining to maintain performance.
    - Synthetic data streams with controlled drift can be used to evaluate system robustness.
    - Adaptive models outperform static models when new items appear over time.
  limits:
    - None identified.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The following domains were flagged as relevant: Behavioral Profiling & Classification (codes 5.A, 5.B) because the paper explicitly models user preference dynamics and drift; Spending Forecasting (6.A, 6.B) because concept drift directly impacts prediction accuracy; Anomaly Detection (8.A, 8.B) because drift detection techniques are core to the paper; and System Evaluation (12.A, 12.B) due to the synthetic data generator for evaluation. These were assigned high relevance except 8.A and 12.A/12.B which are medium as they are secondary. Domains like Expense Categorization, Budget Recommendation, Mobile Design, Privacy, and Retention were considered and rejected because the paper does not address these aspects. Borderline cases: the paper's discussion of user preference changes could relate to seasonal spending (2.B), but it does not specifically address cyclical patterns, so we did not assign that. Overall, the paper is highly relevant to Odin's algorithmic modules that deal with dynamic user behavior and evaluation.
limitations:
  - The model assumes geometric closeness in latent space, which may not capture all preference dynamics.
  - Synthetic data fidelity drops with sparse item preferences.
  - New user/item strategies are not fully developed. [unacknowledged]
remember_this:
  - num: HR@5 on MIND dataset ranges from 0.6 to 0.7 after adaptation.
  - Drift detection triggers model retraining to maintain recommendation accuracy.
  - Synthetic data can replicate real frequency distributions when enough interactions exist.
  - Adaptive models outperform static models under concept drift.
```
---

## Paper 11: Mehta et al_summarized.md

**Source File:** `Mehta et al_summarized.md`

```yaml
paper_id: 0e6b8a1c-6c3c-53df-9b34-a8fa8b7f9d91
designation: international-algorithm-specific
title: "Clustering and Similarity Learning in Financial Markets: A Tutorial for the Practitioners"
authors: "Mehta, D.; Thompson, J.R.J.; Lee, H.; Lee, Y."
year: 2025
venue: Unknown
odin_topics:
  - 1.A
  - 2.A
  - 2.B
  - 3.A
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
  - 8.A
  - 8.B
  - 9.A
  - 9.B
  - 10.A
  - 12.B
tldr: This tutorial synthesizes clustering and similarity learning methods, demonstrating their application in investment workflows to build adaptive neighborhoods of securities, funds, companies, and investors for improved decision-making.
problem_and_motivation: Traditional peer-grouping methods such as industry codes or static style boxes are coarse, rigid, and fail to capture actual risk and thematic exposures. There is a need for adaptive, data-driven similarity systems that can integrate heterogeneous data to support real-world financial decision-making.
approach:
  - Reviews clustering methods across modalities: tabular (k-means, hierarchical), time-series, text, graphs, and images.
  - Covers similarity learning methods including metric learning, random forest proximities, Siamese networks, graph neural networks, and multimodal fusion.
  - Focuses on methodologies for fixed income, mutual funds, companies, and investors, emphasizing supervised and semi-supervised learning approaches.
  - Discusses evaluation protocols like substitution fidelity, neighborhood stability, and segment utility to align with fiduciary objectives.
  - Provides practical guidelines for design choices, including metric selection, normalization, and ensuring interpretability through feature importance or SHAP values.
findings:
  - Supervised similarity frameworks allow funds to be quantified against their declared categories and flag outliers transparently.
  - Random forest proximities enable bond substitution by aligning distances with desk use cases like relative value and surveillance.
  - Multimodal pipelines that combine tabular, text, and graph data produce robust company similarity comparable sets for valuation and strategy.
  - Graph neural networks using fund-bond bipartite structures improve price and yield prediction, supporting peer retrieval.
  - num: Nearly one-fifth of U.S. investment-grade volume now trades in baskets, necessitating robust portfolio-level similarity metrics like STRAPSim.
  - The tutorial identifies that traditional academic metrics like Silhouette or ARI are insufficient; practitioner validation (e.g., substitution fidelity) is critical.
key_figures_tables:
  - "Exhibit 1: Usecases of Clustering and Similarity Learning in Financial Markets → Highlights broad applications from risk to personalization."
  - "Exhibit 5: Evaluation methodologies: academic vs. practitioner perspectives → Shows shift from abstract metrics to operational validity."
  - "Exhibit 10: Clustering and similarity applications for investors across data modalities → Illustrates how transaction and profile data create client segments."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "SR 11-7"
    definition: "A regulatory guidance emphasizing model risk management, requiring documentation and reproducibility."
  - term: "GICS"
    definition: "Global Industry Classification Standard, a common but static taxonomy for company sectors."
  - term: "DTW"
    definition: "Dynamic Time Warping, a distance metric for measuring similarity between two time series with varying speeds."
  - term: "KYC"
    definition: "Know-Your-Client, a regulatory process involving client identification and risk profiling."
critical_citations:
  - "[Jeyapaulraj et al., 2022] — Demonstrates supervised similarity for corporate bonds."
  - "[Mehta et al., 2020] — Shows fund categories are reproducible using supervised learning."
  - "[Barberis et al., 2005] — Documents return co-movement being better explained by data than GICS/SIC."
  - "[Thompson et al., 2021] — Applies clustering to understand investor behavioral types."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "contextual"
      justification: "Paper discusses general investor profiling, applicable but not specific to Filipino context."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "low"
      justification: "General financial behavior analysis; lacks cultural specificity to Filipino customs."
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "medium"
      justification: "Discusses regime identification and time-series patterns, applicable to seasonal spending."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "low"
      justification: "Focuses on financial securities clustering, not transactional expense categorization."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Provides overview of traditional financial data analysis methods, informing system landscape."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Directly critiques static taxonomies and heuristic peer groups, justifying data-driven systems."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Provides methodologies for classifying investor types based on behavior and risks."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "medium"
      justification: "Addresses regime shifts and adaptability in profiles but does not explicitly solve cold-start."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Reviews supervised and unsupervised classification methods (e.g., K-means, metric learning)."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Discusses time-series forecasting and regime prediction using clustering."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Covers DTW, correlation, and deep learning methods for sequential data."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "medium"
      justification: "Provides context on how expert input (e.g., risk tolerance) shapes similarity models."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "low"
      justification: "Does not directly address budget recommendation, but uses constraints in related domains."
    - code: "7.C"
      name: "Constrained Optimization Approaches for Budget Allocation"
      relevance: "contextual"
      justification: "Mentions scenario reduction and constraints implicitly but not directly for budgets."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Discusses open-set recognition and outlier detection for funds and transactions."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Reviews density-based clustering and open-set learning, applicable to detecting fraudulent transactions."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "contextual"
      justification: "Focuses on algorithmic and analytical workflows, not UI/UX design."
    - code: "9.B"
      name: "Mobile UX Design for Personal Finance"
      relevance: "contextual"
      justification: "Not a focus of the paper."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "contextual"
      justification: "Mentions governance but does not address specific security or privacy algorithms."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Dedicated section on evaluating similarity models with operational criteria (substitution fidelity, stability)."
  contribution: "This tutorial provides a comprehensive framework for building adaptive similarity systems that can be directly adapted for Odin's behavioral profiling module. Its detailed review of evaluation methodologies, particularly the shift from academic to operational validity, justifies Odin's focus on user-validated performance metrics. The integration of multimodal data (transactions, user profiles, and text) informs Odin's architecture for constructing robust user profiles and forecasting spending. Furthermore, the discussion of open-set recognition directly supports Odin's anomaly detection capabilities."
  directly_justifies:
    - "Adaptive, data-driven similarity systems are required to replace coarse, rigid peer-grouping methods."
    - "Evaluation of financial algorithms must focus on substitution fidelity and neighborhood stability, not abstract indices."
    - "Multimodal pipelines (tabular, text, graph) are essential for robust peer discovery in sparse data environments."
    - "Supervised and semi-supervised learning frameworks provide transparent mechanisms for flagging outliers and category drift."
  limits:
    - "The tutorial focuses on investment and securities, not direct personal expense management."
    - "The evaluation metrics discussed (e.g., substitution fidelity) are not directly transferable to PFMS without adaptation."
    - "Many advanced models (e.g., GNNs) sacrifice interpretability, a key requirement for Odin's user-facing analytics."
  mapping_rationale: "A systematic scan of all 12 functional domains was performed. The paper's core contribution on adaptive similarity and clustering directly aligns with high relevance to Behavioral Profiling (5.A, 5.C), Spending Forecasting (6.A, 6.B), and Anomaly Detection (8.A, 8.B), as it provides the theoretical and algorithmic foundation for these modules. The domain of Existing Systems (4.A, 4.B) is highly relevant due to the paper's strong critique of static heuristic methods, justifying Odin's data-driven approach. Evaluation (12.B) is directly supported. For domains like Expense Categorization (3) and Budget Recommendation (7), the paper offers context (e.g., on constrained optimization) but lacks specific application to PFMS, hence relevance is low/contextual. The paper's focus on financial instruments, rather than Filipino young professionals, means topics under Domain 1 are contextual. Borderline cases like seasonal spending (2.B) are touched upon via regime detection, but the paper does not focus on personal cycles. Overall, the paper is highly relevant for Odin's core algorithmic modules but only contextual or not applicable to UI/UX, privacy, or cultural specifics."
limitations:
  - "Paper is a tutorial and thus does not present a novel algorithm or empirical validation of a specific system."
  - "The applicability of the discussed 'operational validity' metrics to a PFMS like Odin is not explicitly explored. [unacknowledged]"
  - "Does not address the specific cold-start problem of a new user in a PFMS, despite mentioning similar challenges."
remember_this:
  - "Static peer groups are obsolete; adaptive data-driven similarity systems are required for modern analytics."
  - "Evaluation of similarity systems must prioritize operational validity over academic metrics."
  - "Multimodal data integration is the key to achieving robust peer discovery and user profiling."
  - "Supervised similarity frameworks can transparently flag outliers and category drift in user behavior."
  - "Deep learning methods often sacrifice interpretability, necessitating governance frameworks like SR 11-7."
```
---

## Paper 12: Bader & Haraty_summarized.md

**Source File:** `Bader & Haraty_summarized.md`

```yaml
paper_id: 10.12785/ijcds/1571107231
designation: international-algorithm-specific
title: Bridging AI and Emotion: Enhanced Models for Personal Finance Manager Applications
authors: Bader, S.; Haraty, R. A.
year: 2025
venue: International Journal of Computing and Digital Systems
odin_topics:
  - 3.A
  - 4.B
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 7.B
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
  - 13.B
tldr: Integrates deep learning and sentiment analysis into a .NET Core-based financial advisor application for enhanced anomaly detection, spending prediction, and personalized merchant recommendations.
problem_and_motivation: Existing financial platforms process structured data but fail to leverage unstructured user inputs and emotional context, leading to generic and ineffective financial recommendations. This gap limits user satisfaction and the potential for truly personalized financial guidance. A solution is needed that analyzes user behavior, sentiment, and transaction patterns to provide adaptive financial advice.
approach:
  - Developed a .NET Core 6 application integrating Python-based AI modules for anomaly detection, forecasting, and sentiment analysis.
  - Used TensorFlow/Keras to implement Transformer, Temporal Convolutional Network (TCN), and N-BEATS models for predictive modeling of spending behavior.
  - Implemented anomaly detection using Isolation Forest, Local Outlier Factor (LOF), and One-Class SVM algorithms on transactional data.
  - Incorporated Natural Language Processing (NLP) using fine-tuned BERT and GPT models for sentiment analysis on transaction descriptions to categorize user emotions.
  - Evaluated models with and without sentiment analysis using MAPE, accuracy, precision, recall, and ROC-AUC metrics, and compared against traditional fintech solutions.
findings:
  - num: Integrating sentiment analysis improved predictive accuracy, reducing MAPE from 10.5% to 7.8% across models.
  - num: The Transformer model achieved the lowest RMSE of 0.062 with sentiment, while N-BEATS was the best performer at 0.057.
  - num: Anomaly detection system achieved 92% accuracy, with 90% precision and 85% recall, yielding an F1-score of 87.5%.
  - num: Predictive models incorporating sentiment analysis achieved 88% alignment with actual user behavior within a 90% confidence interval.
  - The N-BEATS model excelled at breaking down time-series data into trends and seasonality, providing interpretable forecasts.
key_figures_tables:
  - Figure 1: System architecture showing integration of transaction, merchant, and account data with AI analytics layers.
  - Figure 13: Transformer model predictions without sentiment analysis, showing it captures actual spending behavior.
  - Figure 16: Transformer model predictions with sentiment analysis, showing improved accuracy and closer fit to actual spending data.
  - Table 1: Comparison showing our approach's superior anomaly detection precision (90% vs. 70-80%) and predictive accuracy (MAPE 7.8% vs. 10-12%) over existing fintech solutions.
key_equations:
  - equation: MAPE = (1/n) * Σ(|(Actual - Predicted)| / Actual) * 100
    explanation: Measures average prediction error as a percentage.
  - equation: Precision = TP / (TP + FP)
    explanation: Ratio of correctly identified positive instances.
  - equation: Recall = TP / (TP + FN)
    explanation: Ratio of actual positives correctly identified.
definitions:
  - term: MCC
    definition: Merchant Category Code, a standardized classification for businesses.
  - term: MAPE
    definition: Mean Absolute Percentage Error, a metric for forecasting accuracy.
  - term: ROC-AUC
    definition: Receiver Operating Characteristic - Area Under the Curve, measures model discrimination ability.
  - term: N-BEATS
    definition: Neural Basis Expansion Analysis for Interpretable Time Series Forecasting.
  - term: TCN
    definition: Temporal Convolutional Network, a model for sequence prediction.
critical_citations:
  - "[Chollet, 2017] — Deep learning with Python framework used."
  - "[Bollen et al., 2011] — Demonstrated social media sentiment's impact on stock markets."
  - "[Goodfellow et al., 2016] — Foundational deep learning text referenced for methodology."
  - "[Johnson, 2024] — Integration of sentiment and knowledge graphs for fintech decision support."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Uses MCC and user-defined categories to structure transaction data for AI analysis.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Explicitly identifies that existing financial platforms fail to use unstructured user data and emotional context.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Builds user profiles using transaction history, sentiment, and spending behavior for personalized advice.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Categorizes users into emotional and behavioral segments (e.g., Health-Focused, Adventurous) using sentiment analysis.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Core contribution involves implementing deep learning models (Transformer, TCN, N-BEATS) for financial forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Specifically evaluates TCN, N-BEATS, and Transformers on sequential transaction data for spending prediction.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Predictions are used to generate personalized budgeting recommendations and financial forecasts.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: The application provides budget creation and tracking features based on predictive insights.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: A primary objective is to implement AI-driven anomaly detection to improve financial transaction security.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Uses Isolation Forest, LOF, and One-Class SVM to detect fraudulent and irregular transactions.
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: contextual
      justification: Discusses training models on historical data to establish baselines for anomaly detection.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: Mentions web/mobile front-end but does not focus on mobile-first principles.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: Discusses dashboards and user interface but not UX design principles specifically.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Mentions vulnerability assessments and secure integration using .NET Core, but not a deep focus.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Security alerts and transparent anomaly detection aim to build user confidence.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Personalization and merchant recommendations are designed to enhance user engagement.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: low
      justification: Suggests feedback loops and continuous learning to improve recommendations over time.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Employs MAPE, precision, recall, and ROC-AUC to rigorously evaluate algorithmic modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides a comparative analysis of anomaly detection and predictive models with and without sentiment integration.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: contextual
      justification: Mentions credit cards and high-yield savings accounts in a supporting, but not central, context.
  contribution: This paper provides a comprehensive blueprint for integrating sentiment analysis with deep learning (Transformer, TCN, N-BEATS) and anomaly detection (Isolation Forest, LOF) in a personal finance application. The methodology and comparative results offer direct justification for Odin's predictive analytics module and its anomaly detection engine. The discussion on personalized merchant recommendations provides a model for Odin's user engagement features. The evaluation framework using MAPE, precision, recall, and ROC-AUC can guide Odin's system evaluation strategy. The discussion of real-time adaptability and user feedback loops informs Odin's design for continuous learning and retention.
  directly_justifies:
    - "The system architecture integrates transaction, merchant, and account data for holistic financial analysis."
    - "Deep learning models (Transformer, TCN, N-BEATS) can effectively forecast user spending patterns."
    - "Sentiment analysis of transaction data and merchant matching significantly improves the accuracy of personalized financial recommendations."
    - "Anomaly detection using Isolation Forest and One-Class SVM achieved 92% accuracy in identifying fraudulent transactions."
    - "Continuous model retraining based on user feedback and new data is essential for maintaining prediction accuracy."
  limits:
    - "Results are based on a limited dataset which may not represent all user demographics."
    - "Computational efficiency of deep learning models remains a concern for real-time, high-volume applications."
    - "User trust and adoption of AI-driven financial advice are not directly studied in this work."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant for domains related to Behavioral Profiling (5.A, 5.C), Spending Forecasting (6.A, 6.B), Anomaly Detection (8.A, 8.B), and System Evaluation (12.A, 12.B) because it provides specific algorithmic implementations and evaluations. Medium relevance was assigned to Expense Categorization (3.A) due to its use of MCC codes, and to Data Privacy (10.A) and User Trust (10.B) where security and confidence are mentioned but not central. Low relevance was assigned to Mobile-First Design (9.A, 9.B) as the paper focuses on backend AI rather than UX principles. Domains not explicitly supported include Savings & Debt Management (13.A, 13.C) and User-Declared Preferences (2.C), which are mentioned contextually but lack substantive contribution. The overall contribution is highly relevant to Odin's design, offering validated models and an evaluation framework for several core algorithmic modules.
limitations:
  - "The performance of the models is evaluated on a specific dataset, which may not be generalizable across diverse populations and financial behaviors."
  - "The computational resources required for training and deploying Transformer and TCN models could be a barrier for resource-constrained environments. [unacknowledged]"
  - "Potential for bias in sentiment analysis models based on the language and context of transaction data was not explicitly addressed. [unacknowledged]"
  - "The study does not include user studies to measure the real-world impact on financial well-being or user satisfaction."
  - "Real-time processing of unstructured data (e.g., social media sentiment) is identified as a future challenge but not fully addressed."
remember_this:
  - "Integrating sentiment analysis into financial models improves spending prediction accuracy."
  - "The N-BEATS model was the best performer for interpretable time-series forecasting."
  - "Anomaly detection system achieved 92% accuracy in identifying fraudulent transactions."
  - "AI-driven merchant recommendations are a key feature for user engagement."
  - "Continuous learning from user feedback is vital for maintaining model performance."
```
---

## Paper 13: Romero_summarized.md

**Source File:** `Romero_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: local
title: Buy-Now-Pay-Later Adoption, Debt Stress, and Repurchase Intention among Filipinos Gen Z Consumers: The Mediating Role of Budgeting Self-Efficacy
authors: Romero, M. A.
year: 2025
venue: Oikonomia Review: Journal of Economics, Management, and Accounting
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.C
  - 3.C
  - 5.A
  - 5.B
  - 5.C
  - 7.A
  - 7.B
  - 7.D
  - 8.A
  - 11.A
  - 11.B
  - 13.A
  - 13.B
tldr: BNPL adoption among Filipino Gen Z is driven by convenience and promotions, increasing repurchase intention but also debt stress, while budgeting self-efficacy and transparency reduce negative outcomes.
problem_and_motivation: BNPL services can simultaneously drive commerce growth and create consumer welfare risks, yet the psychological mechanisms linking adoption to repurchase intention remain unclear. Understanding how debt stress and budgeting self-efficacy mediate this relationship is essential for designing platforms that support sustainable use. The role of transparency in fostering self-efficacy and reducing stress has not been adequately examined in the Filipino Gen Z context.
approach:
  - Quantitative explanatory design using cross-sectional survey data from 602 Filipino Gen Z consumers aged 18-27 who had used BNPL at least twice in three months.
  - Partial Least Squares Structural Equation Modeling (PLS-SEM) tested direct and mediated effects among perceived convenience, promotional attractiveness, transparency, BNPL adoption intensity, debt stress, budgeting self-efficacy, and repurchase intention.
  - All constructs measured with validated multi-item five-point Likert scales; bootstrapping supported inference for indirect effects.
findings:
  - Perceived convenience and promotional attractiveness positively associated with BNPL adoption intensity.
  - Perceived transparency positively associated with BNPL adoption intensity and budgeting self-efficacy.
  - BNPL adoption intensity positively associated with repurchase intention and debt stress.
  - Debt stress negatively associated with repurchase intention.
  - Budgeting self-efficacy negatively associated with debt stress and positively associated with repurchase intention.
  - Budgeting self-efficacy mediates the transparency-debt stress relationship; debt stress partially mediates the adoption-repurchase intention relationship; serial mediation via self-efficacy and stress is supported.
key_figures_tables:
  - Table 1: Measurement model summary establishing reliability, convergent validity, and discriminant validity for all constructs.
  - Table 2: Hypotheses testing summary confirming all direct and mediated relationships, with partial mediation for debt stress.
  - Table 3: Mechanism summary interpreting convenience/promotions, adoption-stress-repurchase, and transparency-self-efficacy-stress pathways.
  - Figure 1: SEM path diagram specifying the theory-driven structure of BNPL adoption, stress, self-efficacy, and repurchase intention relationships.
  - Figure 2: Mediation model illustrating dual pathways from adoption to repurchase intention via debt stress, with transparency and budgeting self-efficacy as protective levers.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: BNPL
    definition: Buy-Now-Pay-Later, a short-term consumer credit embedded in digital checkout.
  - term: Debt Stress
    definition: Psychological burden from repayment obligations, late fees, and perceived loss of financial control.
  - term: Budgeting Self-Efficacy
    definition: Confidence in tracking installments, planning cashflow, and resisting impulsive use.
  - term: Perceived Transparency
    definition: Clarity of fees, due dates, penalties, and total repayment amounts.
  - term: PLS-SEM
    definition: Partial Least Squares Structural Equation Modeling, a variance-based SEM method.
critical_citations:
  - "[Schomburgk & Hoffmann, 2023] — Mindfulness reduces BNPL usage and improves well-being."
  - "[Simiyu et al., 2025] — Self-efficacy and facilitating conditions influence BNPL borrowing."
  - "[Widayati et al., 2024] — Promotions and design features drive Gen Z BNPL behavior."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Focuses specifically on Filipino Gen Z consumers aged 18-27, a core Odin demographic.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Examines income irregularity, liquidity constraints, and short-term smoothing needs of young Filipinos.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly investigates spending behavior, BNPL usage, repurchase intention, and debt stress in the target segment.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Provides empirical data on BNPL use within the Filipino cultural and digital commerce context.
    - code: 2.C
      name: User-Declared Financial Preferences
      relevance: medium
      justification: Captures self-reported perceptions of convenience, transparency, and promotional appeal, informing preference modeling.
    - code: 3.C
      name: User-Defined Allocation Constraints
      relevance: medium
      justification: Budgeting self-efficacy reflects user-perceived ability to allocate and constrain spending, relevant to constraint handling.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Identifies behavioral profiles via stress and self-efficacy levels, relevant to classification.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: contextual
      justification: Discusses heterogeneity and segmentation; provides background for profile dynamics but no cold-start methods.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Uses PLS-SEM for hypothesis testing, not classification; tangential to classification approaches.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Budgeting self-efficacy is a core construct, providing domain knowledge on how confidence affects financial outcomes.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Findings on transparency and self-efficacy can inform design of budget recommendations that reduce stress and support healthy use.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: contextual
      justification: Discusses infeasibility when repayment congestion occurs; provides context but not algorithmic handling methods.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Tangential; debt stress and repayment congestion could inform anomaly signals but not directly about detection.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: Repurchase intention and stress-driven avoidance directly relate to engagement dynamics and sustainability.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: high
      justification: Transparency and self-efficacy are identified as mechanisms to reduce churn and support retention, directly informing engagement design.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: Tangential; budgeting self-efficacy relates to spending control, not explicit savings goal management.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: Directly studies debt stress and strategies to manage BNPL obligations, informing debt management features.
  contribution: The paper's mechanism-based account of BNPL behavior provides empirical justification for Odin's design to incorporate budgeting self-efficacy as a protective factor. The finding that transparency strengthens self-efficacy directly supports Odin's need for clear, legible information displays. The dual pathway model (adoption→repurchase vs. adoption→stress→reduced repurchase) informs Odin's anomaly detection and engagement modules by highlighting stress as a predictor of churn. The emphasis on micro-interventions and contextual nudges justifies Odin's mobile-first approach to delivering decision aids at the point of purchase.
  directly_justifies:
    - "Budgeting self-efficacy reduces debt stress and supports healthier repurchase behavior."
    - "Transparency strengthens budgeting self-efficacy and reduces harmful outcomes."
    - "BNPL adoption increases repurchase intention but also elevates debt stress, which reduces future engagement."
    - "Micro-interventions embedded in app interfaces can strengthen self-efficacy and reduce stress."
  limits:
    - "Cross-sectional design restricts temporal inference; stress may accumulate over time [unacknowledged]."
    - "Self-reported adoption intensity may not align with objective transaction data [unacknowledged]."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to domains related to Filipino Cultural Context (Topic 2.A), Expense Categorization (3.C via self-efficacy), Behavioral Profiling (5.A), Budget Recommendation (7.A), Engagement (11.A, 11.B), and Debt Management (13.B). It provides medium relevance to Seasonal Patterns (2.B, 2.D) and User Preferences (2.C) through its discussion of promotions and transparency, though not directly addressing cyclicality. Domain 6 (Forecasting) and Domain 12 (Evaluation) were rejected as the paper does not address predictive modeling or system evaluation frameworks. Borderline cases included Topic 7.D (infeasibility handling), which was marked contextual because the paper discusses repayment congestion but not algorithmic reduction hierarchies. Topic 5.B (profile dynamics) was also marked contextual as it mentions segmentation but does not address cold-start issues. Topic 8.A (anomaly detection) was marked low due to tangential relevance to stress as an outcome signal. The overall relevance is high for informing Odin's behavioral, engagement, and debt management modules, though the paper is primarily a behavioral study rather than a computational systems paper.
limitations:
  - "Cross-sectional design restricts temporal causal inference. [unacknowledged]"
  - "Self-reported adoption and stress measures may introduce common method bias. [unacknowledged]"
  - "Sample limited to university and online panel networks, may not fully represent all Filipino Gen Z consumers. [unacknowledged]"
  - "No objective transaction data to validate self-reported BNPL adoption intensity. [unacknowledged]"
remember_this:
  - "BNPL adoption increases repurchase intention but also elevates debt stress."
  - "Budgeting self-efficacy reduces stress and supports healthier BNPL use."
  - "Transparency strengthens self-efficacy, serving as a protective mechanism."
  - "Debt stress partially mediates the adoption-repurchase intention relationship."
  - "Micro-interventions can enhance self-efficacy and reduce repayment congestion."
```
---

## Paper 14: Hasan et al_summarized.md

**Source File:** `Hasan et al_summarized.md`

```yaml
paper_id: "10.59324/ejsmt.2026.2(1).05"
designation: "international-algorithm-specific"
title: "Continuous Data Curation and Valuation for Long-Term Machine Learning Model Health: A Comprehensive Review"
authors: "Hasan, M.; Shifa, S.I.; Niaz, K.; Shuvo, M.M.H."
year: 2025
venue: "European Journal of Science and Modern Technologies"
odin_topics:
  - "4.A"
  - "4.B"
  - "6.A"
  - "6.B"
  - "8.A"
  - "8.B"
  - "12.A"
  - "12.B"
  - "12.C"
tldr: "Machine learning models degrade over time due to data drift, necessitating continuous curation, valuation, drift detection, and active learning integrated into MLOps pipelines."
problem_and_motivation: "ML models suffer performance decay over time due to changing data distributions, known as AI ageing. Existing systems lack integrated automation for data quality monitoring and adaptive retraining. This gap undermines long-term reliability and trust in deployed ML systems."
approach:
  - "Surveys literature on data curation, data valuation, drift detection, active learning, and MLOps."
  - "Proposes a taxonomy of continuous curation tasks divided into data integrity and data relevance."
  - "Introduces DataSphere, a unified framework for autonomous data lifecycle management."
  - "Formalises model health as a time-dependent function of accuracy, robustness, fairness, and drift."
  - "Reviews Shapley value and influence functions for data valuation, with approximations."
  - "Discusses drift detection algorithms (DDM, ADWIN, Page-Hinkley) and their integration."
  - "Explores active learning strategies: uncertainty sampling, diversity sampling, and reinforcement learning."
  - "Presents a Data Health Index with structural and statistical metrics for monitoring."
  - "Compares industrial MLOps platforms (Vertex AI, SageMaker, MLflow, Kubeflow)."
  - "Provides a practical deployment checklist for foundation, monitoring, and adaptation phases."
findings:
  - "num: 91% of ML models experience performance decay in production, sometimes within days."
  - "Continuous curation and periodic retraining maintain model performance near peak levels (sawtooth pattern)."
  - "Automated label correction significantly improves accuracy under label noise, as shown in Figure 3."
  - "Data Shapley values identify outliers and mislabeled data, with a left tail of detrimental points."
  - "Active learning with uncertainty sampling can reach target accuracy with up to 50% less labelled data."
  - "Drift detection coupled with valuation and curation enables closed-loop adaptive retraining."
  - "Unified frameworks like DataSphere reduce manual hand-offs and accelerate adaptation cycles."
  - "Open challenges include unified theory of data value and fully automated curation without human rules."
key_figures_tables:
  - "Figure 1: High-level ML data lifecycle pipeline → shows cyclical data acquisition, curation, training, and monitoring."
  - "Figure 2: Model performance degradation over time (AI ageing) → decay accelerates with concept drift; continuous curation flattens decline."
  - "Figure 3: Impact of label noise on model accuracy → automated label correction maintains higher accuracy than standard training."
  - "Figure 4: Taxonomy of curation tasks → divides into Data Integrity (schema, value, uniqueness) and Data Relevance (label quality, distributional consistency)."
  - "Figure 5: Distribution of Data Shapley values → most points have low positive value; a tail of high-value data and negative-value outliers exist."
  - "Figure 7: Drift–Curation–Valuation feedback loop → drift alert triggers valuation and curation, leading to retraining and redeployment."
  - "Figure 8: Active learning learning curve → uncertainty sampling outperforms random sampling, reaching target accuracy with less data."
  - "Figure 10: Unified DataSphere architecture → central feature store, curation pipeline, training/valuation, deployment/monitoring, orchestration."
  - "Table 1: Master taxonomy of methods for long-term model health → maps dimensions (data quality, importance, environment change, adaptation) to methods and trade-offs."
  - "Table 3: Summary of major data valuation techniques → compares Shapley, influence functions, gradient similarity, RL, Beta Shapley, active learning."
key_equations:
  - equation: "H(t) = f(A(t), R(t), F(t), D(t))"
    explanation: "Model health as function of accuracy, robustness, fairness, and drift."
  - equation: "R(t) = E_{(x,y)\\sim P_t}[\\mathbb{I}(M(x) = M(x + \\epsilon))]"
    explanation: "Robustness under small input perturbations."
  - equation: "F(t) = |P(\\hat{Y}=1 | Z=0) - P(\\hat{Y}=1 | Z=1)|"
    explanation: "Fairness disparity measured by equalised odds difference."
  - equation: "D(t) = D_{KL}(P_{train} \\parallel P_t)"
    explanation: "Distributional drift via KL divergence between training and current data."
  - equation: "V_i = \\frac{1}{|S|} \\sum_{S' \\subseteq S \\setminus \\{i\\}} \\binom{|S|-1}{|S'|}^{-1} [U(S' \\cup \\{i\\}) - U(S')]"
    explanation: "Shapley value for data point i as marginal contribution over subsets."
definitions:
  - term: "Model health"
    definition: "Sustained ability of an ML model to deliver accurate, fair, and reliable predictions over its operational lifecycle."
  - term: "Data drift"
    definition: "Change in statistical properties of data over time, including covariate, concept, and label drift."
  - term: "Concept drift"
    definition: "Change in the relationship between input variables and the target variable P(y|X)."
  - term: "Covariate drift"
    definition: "Change in the distribution of input variables P(X)."
  - term: "Continuous data curation"
    definition: "Automated process of cleansing, enriching, and maintaining data quality throughout the ML lifecycle."
  - term: "Data valuation"
    definition: "Quantifying the contribution of each data point to model performance using methods like Shapley value or influence functions."
  - term: "Active learning"
    definition: "Iterative process where a model selects the most informative unlabeled data points for labelling to improve performance efficiently."
  - term: "MLOps"
    definition: "Set of practices for automating and integrating ML development, deployment, and monitoring."
  - term: "Data Shapley"
    definition: "Game-theoretic framework assigning value to data points based on their average marginal contribution across subsets."
  - term: "Influence functions"
    definition: "Robust statistics technique to approximate the effect of upweighting a training point on model parameters and predictions."
critical_citations:
  - "[Vela et al., 2022] — Defines AI ageing and performance decay over time."
  - "[Lu et al., 2018] — Comprehensive review of concept drift."
  - "[Ghorbani & Zou, 2019] — Introduces Data Shapley for equitable data valuation."
  - "[Koh & Liang, 2017] — Develops influence functions for black-box model interpretation."
  - "[Northcutt et al., 2021] — Presents confident learning for automated label correction."
relevance:
  topics:
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews existing MLOps tools and general data management systems, providing context for PFMS landscape."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Identifies gaps in integration of data curation, valuation, and drift detection, applicable to PFMS shortcomings."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses model decay and drift, which directly affects forecasting accuracy in spending prediction."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "medium"
      justification: "Reviews drift detection and retraining strategies that are essential for sequential forecasting models."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Covers data quality monitoring and outlier detection techniques relevant to identifying spending anomalies."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "medium"
      justification: "Surveys drift detection and data valuation methods that can enhance anomaly detection algorithms."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Provides comprehensive metrics (accuracy, robustness, fairness, drift) and monitoring frameworks for system evaluation."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Formalises model health and offers evaluation protocols (e.g., performance degradation curves) applicable to any algorithmic module."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "medium"
      justification: "While not specific to budget recommendation, the proposed evaluation methodologies (drift, health index) are transferable."
  contribution: "This review provides a systematic framework for maintaining model health via continuous data curation and valuation, which directly supports Odin's anomaly detection module (8.A/B) by offering drift detection and outlier identification techniques. Its formalisation of model health as a multi-dimensional function (accuracy, robustness, fairness, drift) justifies Odin's system evaluation framework (12.A/B) with quantifiable metrics. The active learning and data valuation strategies inform Odin's forecasting module (6.A/B) for efficient retraining and data prioritisation. The practical deployment checklist offers actionable steps for implementing Odin's data pipelines and monitoring systems."
  directly_justifies:
    - "Continuous curation and periodic retraining maintain model performance near peak levels, preventing decay."
    - "Data Shapley identifies mislabeled or outlier data, which can be used to clean training sets and improve anomaly detection."
    - "Drift detection triggers adaptive feedback loops that are essential for forecasting models to remain accurate over time."
    - "Active learning with uncertainty sampling can achieve target performance with significantly less labelled data, reducing annotation costs."
    - "A unified MLOps framework with central feature store and monitoring enables automated retraining and error diagnosis."
  limits:
    - "The review is general and does not address personal finance or spending data specifically."
    - "Proposed algorithms (Shapley, influence functions) are computationally expensive and may not scale to large PFMS datasets without approximations."
    - "Empirical validation of the unified DataSphere framework in real-world financial applications is not provided."
  mapping_rationale: "A systematic scan across all 12 functional domains was performed. Domains related to Filipino cultural context (2.A-2.D), expense categorization (3.A-3.C), behavioral profiling (5.A-5.C), budget recommendation (7.A-7.D), mobile-first design (9.A-9.B), data privacy (10.A-10.B), user retention (11.A-11.B), and savings/debt management (13.A-13.C) were deemed irrelevant because the paper does not discuss cultural practices, spending categories, user profiles, budget allocation, mobile UX, privacy, engagement, or savings/debt. Domains on existing systems (4.A-4.B) were flagged medium because the paper reviews general MLOps tools and gaps. Forecasting (6.A-6.B) and anomaly detection (8.A-8.B) were flagged medium due to relevance of drift detection and data valuation to these predictive tasks. System evaluation (12.A-12.C) was flagged high because the paper provides formal evaluation frameworks and metrics for model health over time. Borderline cases included 10.B (user trust) considered but rejected because trust is mentioned only peripherally regarding reliability, not as a central theme. Overall, the paper offers foundational data-centric techniques that are broadly applicable to Odin's algorithmic modules and evaluation systems."
limitations:
  - "The review is qualitative and does not present new empirical results or benchmarks."
  - "Computational complexity of exact Shapley value remains prohibitive; approximations may introduce bias. [unacknowledged]"
  - "Integration of the proposed unified framework is not demonstrated in a production system. [unacknowledged]"
  - "Automated label correction can itself introduce bias if the correction model is flawed, a limitation noted in the paper."
  - "Fairness metrics are discussed but not deeply integrated with valuation and curation processes."
remember_this:
  - "91% of ML models degrade in production, often within days of deployment."
  - "Continuous curation and retraining create a sawtooth pattern that sustains performance."
  - "Data Shapley identifies outliers and mislabeled data, enabling targeted cleaning."
  - "Active learning with uncertainty sampling can reduce labelling needs by up to 50%."
  - "Unified MLOps frameworks automate drift detection, valuation, and retraining for long-term health."
```
---

## Paper 15: Zlobin & Bazylevych_summarized.md

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

## Paper 16: Carillo & Serra_summarized.md

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

## Paper 17: Tjostheim_summarized.md

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

## Paper 18: Tabak et al_summarized.md

**Source File:** `Tabak et al_summarized.md`

```yaml
paper_id: 10.3390/su17209219
designation: international-algorithm-specific
title: Assessing the Drivers of Financial Vulnerability and Fraud in Brazil: The Critical Role of Financial Planning over Literacy
authors: Tabak, B.M.; Cardoso, D.H.; Silva, C.C.
year: 2025
venue: Sustainability
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 7.A
  - 7.B
  - 7.D
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
  - 13.A
  - 13.C
  - 4.A
  - 4.B
tldr: Financial planning more strongly predicts reduced vulnerability and fraud than financial literacy does, with machine learning confirming planning as the dominant driver over knowledge.
problem_and_motivation: Financial literacy research is fragmented, with studies examining knowledge, behavior, and cognitive biases in isolation. This fragmentation leaves unclear how these forces interact to impact financial resilience and sustainability. A unified framework is needed to simultaneously examine these interconnected components.
approach:
  - Data from 256 respondents in Brazil's Federal District using convenience sampling at urban focal points.
  - Developed and validated a six-factor measurement instrument using Confirmatory Factor Analysis (CFA).
  - Evaluated seven machine learning algorithms in a horse race, selecting Random Forest as the best performer.
  - Applied SHAP and LIME for model interpretability to identify key predictors of financial vulnerability and fraud.
  - Used multiple linear regression (OLS) with robust standard errors to assess relationships between variables.
findings:
  - num: Financial Planning had a −0.642 correlation with Financial Vulnerability and −0.375 with Fraud, stronger than Financial Literacy.
  - num: Random Forest achieved the lowest RMSE in predicting financial vulnerability, outperforming other algorithms.
  - Financial Planning was identified as the strongest predictor of financial vulnerability and fraud by both SHAP and LIME.
  - num: The Cognitive Reflection Test (CRT) showed a strong positive relationship with financial literacy (coef. 0.502).
  - Black respondents were more financially vulnerable (coef. 0.156), indicating social inequality.
  - Women had lower levels of financial literacy (coef. −0.140), reflecting social barriers.
  - num: High-income individuals had higher levels of financial literacy (coef. 0.348).
  - Converging evidence confirms planning practices are more important than financial knowledge in reducing financial distress.
  - The six-factor CFA model showed excellent fit (CFI = 0.954, TLI = 0.950, RMSEA = 0.039).
key_figures_tables:
  - Figure 2: Horse racing outcomes comparing seven ML algorithms → Random Forest achieved lowest RMSE for financial vulnerability.
  - Figure 3: SHAP feature importance for financial literacy → CRT and Financial Planning are the most influential predictors.
  - Figure 4: SHAP feature importance for financial vulnerability → Financial Planning is the dominant predictor.
  - Figure 5: SHAP feature importance for financial fraud → Financial Planning and Financial Literacy are key predictors.
  - Table A3: Model fit indices and latent factor correlations → CFA model shows excellent global fit and discriminant validity.
  - Table A4: Standardized factor loadings → All factor loadings are statistically significant at p < 0.001.
key_equations:
  - equation: FL_i = β_0^FL + β_1^FL CRT_i + β_2^FL Female_i + ... + ε_{i,FL}
    explanation: Regression model for financial literacy with CRT and demographic controls.
  - equation: FV_i = β_0^FV + β_1^FV FL_i + β_2^FV FP_i + ... + ε_{i,FV}
    explanation: Regression model for financial vulnerability including FL and FP.
  - equation: FF_i = β_0^FF + β_1^FF FL_i + β_2^FF FP_i + ... + ε_{i,FF}
    explanation: Regression model for financial fraud including FL and FP.
definitions:
  - term: PFMS
    definition: Personal Financial Management System
  - term: CFA
    definition: Confirmatory Factor Analysis
  - term: FL
    definition: Financial Literacy
  - term: FP
    definition: Financial Planning
  - term: FV
    definition: Financial Vulnerability
  - term: FF
    definition: Financial Fraud
  - term: CRT
    definition: Cognitive Reflection Test
  - term: SHAP
    definition: Shapley Additive Explanations
  - term: LIME
    definition: Local Interpretable Model-Agnostic Explanation
  - term: XAI
    definition: Explainable Artificial Intelligence
  - term: OLS
    definition: Ordinary Least Squares
  - term: IRT
    definition: Item Response Theory
  - term: AVE
    definition: Average Variance Extracted
  - term: CR
    definition: Composite Reliability
  - term: RMSE
    definition: Root Mean Square Error
critical_citations:
  - "[Lusardi & Mitchell, 2011] — Foundational work on financial literacy measurement and retirement planning."
  - "[Kahneman & Tversky, 1979] — Prospect theory foundation for understanding cognitive biases in financial decisions."
  - "[Anderloni et al., 2012] — Provided the financial vulnerability index framework used in this study."
  - "[Frederick, 2005] — Cognitive Reflection Test methodology for measuring analytical versus intuitive thinking."
  - "[Breiman, 2001] — Random Forest algorithm foundation for machine learning analysis."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly compares knowledge-based vs. behavior-based dimensions (planning) for predicting financial outcomes.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: medium
      justification: Demonstrates that behavioral dimensions (planning) are more predictive than knowledge metrics for new users.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Uses Random Forest classification to identify key behavioral and demographic predictors of financial profiles.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Establishes financial planning as a critical behavior that reduces vulnerability, directly informing budget strategies.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Provides evidence that planning behaviors should be prioritized in budget recommendation algorithms.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: contextual
      justification: Contextual relevance for understanding how to handle cases where users lack planning behaviors.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly compares multiple ML algorithms (Random Forest, SVM, XGBoost) for predicting financial outcomes.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: contextual
      justification: Provides methodological foundation for forecasting but not focused on sequential spending data.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Links financial planning to fraud prevention, relevant to anomaly detection for fraud identification.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: Uses machine learning for fraud prediction, though not specifically for spending anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides rigorous validation methodology (CFA, horse race) applicable to evaluating PFMS modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Compares multiple algorithms using RMSE and XAI methods (SHAP, LIME) for model evaluation.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Shows planning reduces vulnerability, which enables better savings behavior.
    - code: 13.C
      name: End-of-Period Surplus as a Savings Input
      relevance: low
      justification: Tangentially related through the finding that planners are less vulnerable and more likely to save.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Contextual relevance for understanding gaps in current PFMS approaches.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies the gap of not integrating behavioral/planning dimensions in financial literacy assessments.
  contribution: This paper provides empirical validation that financial planning behaviors are more critical than knowledge for reducing financial vulnerability and fraud. This finding directly informs Odin's behavioral profiling module (5.A) by indicating that observed planning behaviors should be prioritized over self-reported knowledge. The machine learning methodology, including the horse race comparison and SHAP/LIME interpretation, offers a template for Odin's algorithm selection and evaluation framework (12.A, 12.B). The strong predictive power of planning variables justifies their integration as key features in Odin's forecasting and recommendation modules (6.A, 7.A). The identification of demographic inequalities (gender, race, income) in financial outcomes provides critical context for Odin's cold-start and personalization strategies (5.B).
  directly_justifies:
    - Behavioral profiling should prioritize observed planning behaviors over declared financial knowledge.
    - Random Forest with SHAP/LIME is effective for identifying key predictors in personal finance datasets.
    - Financial planning is a stronger predictor of positive financial outcomes than literacy alone.
    - Demographic factors like gender, race, and income must be considered in financial profiling systems.
    - Cognitive reflection capacity correlates with financial literacy and should be considered in user modeling.
  limits:
    - Sample limited to urban Federal District of Brazil, not generalizable to other regions or rural populations.
    - Convenience sampling may introduce selection bias despite attempts at demographic diversity.
    - Cross-sectional design prevents causal inference despite strong correlational evidence. [unacknowledged]
    - Small sample size for nonbinary and other race groups limited statistical power for these categories.
    - Financial literacy factor showed borderline reliability (CR=0.695), suggesting measurement refinement needed. [unacknowledged]
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was conducted. The Behavioral Profiling domain (5.A, 5.B, 5.C) was flagged as highly relevant because the paper directly compares knowledge-based and behavior-based dimensions, showing planning behavior is the dominant predictor. The Budget Recommendation domain (7.A, 7.B, 7.D) was flagged for its evidence that planning behaviors should inform budget strategies and its relevance to constraint handling. The Predictive Modeling domain (6.A) was flagged high for its rigorous algorithm comparison and XAI application. The Anomaly Detection domain (8.A, 8.B) was flagged medium/contextual for its fraud prediction component. The System Evaluation domain (12.A, 12.B) was flagged for providing a template for algorithmic evaluation. The Savings domain (13.A, 13.C) was flagged medium/low through the link between planning and vulnerability reduction. The Existing Systems domain (4.A, 4.B) was flagged contextual for identifying gaps in current approaches. Domains considered but rejected included: Filipino Cultural Context (2.A-D) as the study is Brazilian and culture-specific practices are not examined; Expense Categorization (3.A-C) as no expense categorization framework is discussed; Mobile-First Design (9.A-B) as no mobile design considerations are present; Data Privacy (10.A-B) as privacy is not discussed; User Retention (11.A-B) as retention mechanisms are not examined; and Evaluation Methodologies for Budget Recommendation (12.C) as the evaluation is algorithm-focused rather than recommendation-specific. Overall relevance is high for Odin's behavioral profiling, forecasting, and evaluation modules, providing empirical justification for prioritizing behavioral dimensions over knowledge metrics in PFMS design.
limitations:
  - Sample limited to urban Federal District of Brazil, not generalizable to other regions or rural populations.
  - Convenience sampling may introduce selection bias despite attempts at demographic diversity.
  - Cross-sectional design prevents causal inference despite strong correlational evidence. [unacknowledged]
  - Small sample size for nonbinary and other race groups limited statistical power for these categories.
  - Financial literacy factor showed borderline reliability (CR=0.695), suggesting measurement refinement needed. [unacknowledged]
remember_this:
  - Financial planning is more predictive of reduced vulnerability than financial literacy.
  - Random Forest with SHAP/LIME identified planning as the dominant predictor of financial outcomes.
  - Financial planning has a −0.642 correlation with vulnerability, stronger than literacy's −0.380.
  - Women and Black respondents showed higher financial vulnerability, indicating systemic inequalities.
  - Cognitive reflection capacity strongly correlates with financial literacy (coef. 0.502).
```
---

## Paper 19: Balog et al_summarized.md

**Source File:** `Balog et al_summarized.md`

```yaml
paper_id: "10.1145/3726302.3731697"
designation: "international"
title: "Theory and Toolkits for User Simulation in the Era of Generative AI: User Modeling, Synthetic Data Generation, and System Evaluation"
authors: "Balog, K.; Bernard, N.; Zerhoudi, S.; Zhai, C."
year: 2025
venue: "Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval"
odin_topics:
  - "5.A"
  - "9.A"
  - "12.A"
  - "12.B"
  - "12.C"
tldr: "Provides a comprehensive overview of user simulation techniques for interactive AI, covering system evaluation, synthetic data generation, and user modeling with a focus on LLM-based approaches and practical toolkits."
problem_and_motivation: "Evaluating interactive AI systems and training them with interaction data is challenging, costly, and often irreproducible. Effective personalization demands precise user modeling, while robust algorithm training requires extensive interaction data. User simulation addresses these interconnected challenges by enabling repeatable, scalable, and controlled experimentation."
approach:
  - "Covers foundational behavior models (cognitive, process, strategic) and formalisms (MDPs) for simulating user decisions."
  - "Discusses models for specific user actions like query formulation, clicks, effort, and stopping, extending to conversational contexts."
  - "Describes simulator architectures (modular vs. end-to-end) and techniques like agenda-based and sequence-to-sequence simulation."
  - "Surveys open-source toolkits (SimIIR, UserSimCRS) and frameworks for implementing user simulators."
  - "Addresses validation methods (quantitative comparisons, sensitivity analysis) and available benchmark datasets."
findings:
  - "User simulation provides a versatile methodology for evaluation, training, and user modeling, with these uses being deeply interconnected."
  - "LLMs introduce new possibilities for simulation but also present challenges regarding validity and interpretability."
  - "The adoption of user simulation is hindered by scarce accessible resources and skepticism about outcome validity."
  - "Validation requires quantitative comparisons against real logs, sensitivity analysis, and task-based assessments."
  - "Simulation principles underpin traditional IR metrics like Precision, Recall, and NDCG@k as representing implicit user models."
key_figures_tables:
  - "None."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "MDP"
    definition: "Markov Decision Process, a mathematical framework for formalizing sequential decision-making used to construct user simulators."
  - term: "LLM"
    definition: "Large Language Model, used in simulation frameworks to generate human-like interactions and responses."
  - term: "PFMS"
    definition: "Personal Finance Management System, the target system for Odin."
critical_citations:
  - "[Balog and Zhai, 2024] — Foundational survey on user simulation for information access."
  - "[Schatzmann et al., 2006] — Survey of statistical user simulation techniques for dialogue systems."
  - "[Zhang and Balog, 2020] — User simulation for evaluating conversational recommender systems."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Provides the theoretical framework and methodologies for modeling user behavior and creating behavioral profiles."
    - code: "9.A"
      name: "Mobile‑First Design Principles and Rationale"
      relevance: "low"
      justification: "Discusses user interaction simulation, which can inform design principles but is not specific to mobile."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Directly addresses evaluation methodologies using simulation, which is a core component of system evaluation."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Provides methods for simulating user interactions that are essential for evaluating algorithmic modules like recommenders."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "medium"
      justification: "While not specific to budgets, the simulation frameworks can be adapted to evaluate recommendation components."
  contribution: "This paper provides a comprehensive methodology for evaluating interactive AI systems through user simulation. For Odin, it justifies the use of simulated users to test and refine the budget recommendation and anomaly detection modules. It offers a framework for generating synthetic interaction data, which is crucial for training and validating Odin's behavioral classification and forecasting algorithms. The documented toolkits and validation protocols provide a practical pathway for implementing robust offline evaluations. It reinforces the need for a systematic, reproducible approach to evaluating the entire PFMS pipeline."
  directly_justifies:
    - "User simulation enables repeatable, low-cost evaluation of interactive systems."
    - "Simulated interactions can be used for training algorithms and developing user models."
    - "Validation of simulators requires quantitative comparison against real user logs."
  limits:
    - "The tutorial focuses on general information access systems, not specifically on personal finance management."
    - "Validation of simulated user behavior for financial decisions remains an open challenge."
  mapping_rationale: "A systematic scan of all 12 functional domains was performed. The domain 'System Evaluation' (12.A, 12.B, 12.C) was flagged as highly relevant, as the paper is entirely dedicated to evaluation methodologies. The domain 'Behavioral Profiling & Classification' (5.A) was flagged as medium relevance, as it provides the underpinning theory for modeling user behavior. The domain 'Mobile‑First Design' (9.A) was considered but rejected due to the lack of mobile-specific focus. The domain 'User Retention & Engagement' (11.A) was considered but rejected as the paper focuses on system evaluation, not engagement strategies. The domain 'Spending Forecasting' (6.A) was considered but rejected as the paper does not address predictive modeling for spending. The paper is highly relevant to Odin by providing a proven, methodological foundation for evaluating and iterating on its core algorithms."
limitations:
  - "The paper is a tutorial overview, not a primary research study with novel empirical findings for PFMS."
  - "Generalizability of simulation findings to real user financial behavior is not established. [unacknowledged]"
  - "The specific applicability of the discussed toolkits to Odin's unique constraints (e.g., cold-start, mobile-first) requires further investigation."
remember_this:
  - "User simulation enables repeatable, low-cost system evaluation."
  - "LLMs offer new capabilities for generating realistic simulated user interactions."
  - "Validation against real interaction data is crucial for simulator fidelity."
  - "Simulation serves evaluation, training, and user modeling simultaneously."
```
---

## Paper 20: Thakur & Jadhav_summarized.md

**Source File:** `Thakur & Jadhav_summarized.md`

```yaml
paper_id: 10.14744/sigma.2025.00119
designation: international-algorithm-specific
title: Expense tracker management system using machine learning
authors: Thakur, R. S.; Jadhav, A.
year: 2025
venue: Sigma Journal of Engineering and Natural Sciences
odin_topics:
  - 3.A
  - 3.B
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 7.C
  - 8.A
  - 8.B
  - 9.A
  - 9.B
  - 12.A
  - 12.B
  - 12.C
tldr: An expense tracker system using machine learning and ensemble methods to predict future expenses based on historical transaction data.
problem_and_motivation: Manual expense tracking is time-consuming and error-prone, and existing digital tools often lack predictive analytics for proactive financial management. A system that automates expense tracking and forecasts spending can help users make better financial decisions.
approach:
  - Used the "Daily Household Transactions" dataset from Kaggle with fields like date, category, amount, and income/expense flags.
  - Preprocessed data using MinMax scaling, log1p transformation for the amount, and TF-IDF vectorization for text fields.
  - Evaluated individual models: XGBoost, Random Forest, SVM, MLP, KNN, Decision Tree, Extra Tree, and CatBoost.
  - Evaluated ensemble models: Bagging, Boosting, Stacking, Voting, and Blending.
  - Evaluated performance using R-squared, Mean Absolute Error, Mean Square Error, and Relative Absolute Error.
findings:
  - XGBoost achieved the highest R-squared (77.89%) among individual models.
  - The Voting Ensemble Regressor outperformed all other models with an R-squared of 78.11%.
  - num: The Voting Ensemble Regressor achieved the lowest Relative Absolute Error of 0.1765.
  - num: The Voting Ensemble Regressor achieved the lowest Mean Absolute Error of 0.6121.
  - The system's web application is built with Django and PostgreSQL, featuring interactive dashboards and expense categorization.
key_figures_tables:
  - Table 1: Summary of prior expense tracking systems → Highlights gaps like manual entry and limited analysis.
  - Table 2: Performance comparison of machine learning models → Shows Voting Ensemble as the best performer.
  - Figure 3: Expense summary dashboard → Displays total expenses, category breakdown, and monthly trends.
  - Figure 7: Expense categorization interface → Shows predefined categories like food, rent, and shopping.
key_equations:
  - equation: R^2 = 1 - (SS_res / SS_tot)
    explanation: Measures variance explained by the model.
  - equation: MAE = (1/n) * Σ|y_i - ŷ_i|
    explanation: Average magnitude of prediction errors.
  - equation: MSE = (1/n) * Σ(y_i - ŷ_i)^2
    explanation: Average squared difference between actual and predicted.
definitions:
  - term: XGBoost
    definition: Extreme Gradient Boosting, an efficient sequential decision tree ensemble.
  - term: Ensemble Learning
    definition: Combining multiple models to improve overall predictive performance.
  - term: TF-IDF
    definition: Term Frequency-Inverse Document Frequency, a text vectorization technique.
critical_citations:
  - "[Doan & Kalita, 2015] — Provides context on selecting ML algorithms."
  - "[Mienye & Sun, 2022] — Surveys ensemble learning concepts and applications."
  - "[Jadhav et al., 2023] — Discusses data transformation as a preprocessing stage."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Directly proposes and implements an expense categorization system.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: Discusses predefined categories like food, transport, and custom categories.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Core contribution is using ML for expense prediction.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Evaluates multiple forecasting algorithms on spending data.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Mentions budget forecasting and overspending alerts.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Touches on budget forecasting but not on optimization.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: contextual
      justification: Not a focus; the paper is on prediction, not allocation.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Mentions deviation alerts but does not implement anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: Not a focus; system only flags deviations.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: Mentions cross-device access but does not focus on mobile-first design.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: Web application focus, not mobile UX.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses standard regression metrics (R2, MAE, MSE, RAE).
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Systematic evaluation of individual and ensemble models.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: low
      justification: More about prediction accuracy than budget recommendation evaluation.
  contribution: This paper demonstrates that ensemble methods, particularly voting regressors, outperform individual models for expense prediction, providing a basis for Odin's forecasting module. Its application of data transformation techniques (e.g., log1p) and text vectorization can inform data preprocessing for Odin's categorization and prediction algorithms. The web application architecture built with Django offers a reference for Odin's backend design, especially in handling user authentication and expense entry. The evaluation framework using R-squared and MAE provides a template for assessing Odin's predictive performance.
  directly_justifies:
    - Voting ensemble regressors improve expense prediction accuracy over single models.
    - Data transformations like log1p and TF-IDF are effective preprocessing steps for spending data.
    - R-squared and Mean Absolute Error are appropriate metrics for evaluating spending forecast models.
  limits:
    - Dataset is from India, which may not generalize to Filipino cultural or spending contexts. [unacknowledged]
    - Does not address the cold-start problem or behavioral profiling for new users. [unacknowledged]
    - No comparison with deep learning methods like LSTMs for sequential data. [unacknowledged]
    - The system relies on manual expense entry, not automated bank transaction syncing.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. High relevance was assigned to domains directly addressed by the paper's core contribution of ML-based expense prediction and categorization (6.A, 6.B, 3.A, 12.B). Medium relevance was assigned to broader budgeting and evaluation topics (7.A, 12.A). Low relevance was assigned to anomaly detection and mobile design, as these are only superficially mentioned. The topic of constrained optimization (7.C) was considered but rejected as the paper does not address allocation algorithms. The topic of Filipino cultural context (2.A, 2.B) was considered and rejected as the paper uses a non-Philippine dataset. Overall, the paper provides strong empirical justification for using ensemble regression for spending forecasting, which directly supports Odin's algorithmic design.
limitations:
  - The dataset is from India, which may not generalize to Filipino cultural or spending contexts. [unacknowledged]
  - Does not address the cold-start problem or behavioral profiling for new users. [unacknowledged]
  - No comparison with deep learning methods like LSTMs for sequential data. [unacknowledged]
  - The system relies on manual expense entry, not automated bank transaction syncing. [unacknowledged]
remember_this:
  - Voting ensemble regressor achieved the highest R-squared of 78.11%.
  - The voting ensemble achieved the lowest relative absolute error of 0.1765.
  - XGBoost outperformed other individual models with an R-squared of 77.89%.
  - Data preprocessing with log1p and TF-IDF is crucial for expense prediction.
  - The system uses Django for backend and PostgreSQL for database management.
```
---

## Paper 21: Rad et al_summarized.md

**Source File:** `Rad et al_summarized.md`

```yaml
paper_id: 10.3390/electronics14081505
designation: international-algorithm-specific
title: Modeling Investment Decisions Through Decision Tree Regression—A Behavioral Finance Theory Approach
authors: Rad, D.; Cuc, L.D.; Croitoru, G.; Gomoi, B.C.; Mazuru, L.; Bilti, R.S.; Rusu, S.; Sinaci, M.; Barbu, F.S.
year: 2025
venue: Electronics
odin_topics:
  - 5.A
  - 5.C
  - 10.B
  - 12.B
tldr: Decision tree regression identifies investment attitudes, decision-making behaviors, and financial education as key predictors of investment interest, with behavioral factors outweighing demographics.
problem_and_motivation: Classical finance models assume rational decision making, but psychological factors systematically influence investment behavior. Existing predictive models often ignore hierarchical interactions among behavioral, cognitive, and demographic predictors. This leaves a gap in understanding how these factors collectively shape investment interest.
approach:
  - Data came from a survey of 548 Romanian financial professionals using validated Likert-scale instruments.
  - Decision tree regression was applied with default hyperparameters and an 80/20 train-test split.
  - Model evaluation used MSE, RMSE, MAE, MAPE, and R2; feature importance quantified predictor contributions.
  - The tree structure reveals hierarchical splits based on behavioral and attitudinal variables.
findings:
  - "num: Investment attitudes are the most important predictor (25.88% relative importance)."
  - "num: Decision-making behaviors in investments contribute 19.53%, and financial education 16.69%."
  - "num: The model achieved R2=0.185 and MAPE=172.96% on test data, indicating modest predictive power."
  - Demographic variables such as age, income, and education have low importance (<2% each).
  - Trust in AI-based financial systems shows 6.78% importance and appears in deeper tree splits.
key_figures_tables:
  - "Figure 1: Scatterplot of observed vs. predicted investment interest → general alignment but with dispersion at extremes."
  - "Figure 2: Decision tree plot showing hierarchical splits → investment attitudes and financial education are top-level splitters."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: DTR
    definition: Decision tree regression, a non-parametric supervised learning method.
  - term: AI
    definition: Artificial intelligence, used in financial systems for recommendations.
critical_citations:
  - "[Kahneman and Tversky, 1992] — Prospect theory explains asymmetric risk attitudes."
  - "[Ritter, 2003] — Behavioral finance challenges rational decision assumptions."
  - "[Shiller, 2003] — Behavioral finance framework for financial decisions."
  - "[Lusardi and Mitchell, 2007] — Financial literacy importance for retirement decisions."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Paper identifies hierarchical behavioral profiles influencing investment interest.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Uses decision tree regression to classify investors based on behavioral predictors.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Measures trust in AI-based financial systems as a predictor of investment interest.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Evaluates decision tree regression performance with multiple metrics.
  contribution: This paper supports the development of Odin's behavioral profiling module by demonstrating that decision tree regression can effectively model hierarchical relationships among attitudes, decision-making, and education. It justifies incorporating trust in AI as a feature in user models, relevant to Odin's AI-driven advisory components. The evaluation methodology provides a benchmark for assessing predictive algorithms in personal finance contexts. The findings highlight that behavioral factors dominate demographics, guiding feature selection for Odin's classification systems.
  directly_justifies:
    - Investment attitudes (25.88% importance) are the strongest predictor of financial engagement.
    - Decision tree regression captures non-linear interactions among behavioral predictors.
    - Trust in AI-based systems (6.78% importance) is a significant factor in investment decisions.
    - Financial education is more influential than income or age in predicting investment interest.
  limits:
    - Self-reported data may introduce response biases such as social desirability.
    - Non-random convenience sample limits generalizability to broader populations.
    - Single algorithm (DTR) may not capture all complex interactions; ensemble methods could improve.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes identified relevance primarily in behavioral profiling (5.A, 5.C) and user trust (10.B), with secondary relevance in algorithm evaluation (12.B). Domains related to expense categorization (3.A-C), spending patterns (2.B, 2.D), budgeting (7.A-D), anomaly detection (8.A-C), and savings/debt management (13.A-C) were rejected as the paper focuses on investment decisions rather than spending or budgeting. The Filipino cultural context domains (1.A, 1.B, 1.C, 2.A) were considered but deemed low relevance due to the international sample; however, the behavioral findings may be contextual for general financial behavior. The decision tree approach provides a classification method useful for Odin's profiling, while the trust in AI result informs design considerations for user trust. Overall, the paper offers moderate relevance to Odin's behavioral and trust modules.
limitations:
  - Self-reported data may introduce social desirability or recall bias. [unacknowledged]
  - Convenience sampling limits representativeness of the findings. [unacknowledged]
  - The model's low R2 (0.185) indicates that many unmeasured factors affect investment interest. [unacknowledged]
  - The study does not account for potential interactions between variables beyond the tree structure.
remember_this:
  - Investment attitudes are 25.88% of the predictive importance.
  - Behavioral factors dominate demographics in predicting investment interest.
  - Trust in AI systems matters but is secondary to attitudes and decision-making.
  - Decision tree regression offers an interpretable hierarchy of financial predictors.
  - Financial education has higher importance than income or age.
```
---

## Paper 22: Aldrees et al_summarized.md

**Source File:** `Aldrees et al_summarized.md`

```yaml
paper_id: 10.1007/s44196-025-00776-w
designation: international-algorithm-specific
title: Behavioral Patterns in Micro‑lending: Enhancing Credit Risk Assessment with Collaborative Filtering and Federated Learning
authors: Aldrees, A.; Shahab, S.; Dutta, A. K.; Ahmad, W.; Anjum, M.
year: 2025
venue: International Journal of Computational Intelligence Systems
odin_topics:
  - 6.A
  - 6.B
  - 7.D
  - 8.A
  - 8.B
  - 8.C
  - 10.A
  - 12.A
tldr: A collaborative filtering method using lending pattern analysis and federated learning improves credit risk assessment for micro-lending by evaluating borrower behaviour patterns across repayment tenures.
problem_and_motivation: Micro-lending platforms face substantial challenges in credit risk assessment due to limited borrower data and fluctuating financial patterns. Traditional credit scoring algorithms depend on centralized data collection and lack privacy-preserving methods, while current machine learning techniques often fail to capture the diverse behavioural patterns and security requirements of decentralized financial ecosystems.
approach:
  - A Collaborative Filtering Method using Lending Pattern Analysis (CFM-LPA) is introduced for credit risk assessment.
  - The method is enhanced with federated learning to enable decentralized analysis of lending patterns across institutions.
  - It evaluates return rates, credit limits, and consumer response behaviours to identify behavioural factors.
  - The behavioural factor is updated for each return period, influencing credit risk for subsequent periods.
  - The model is trained individually on identified factors, allowing the behavioural factor to be filtered for new credit risk identification.
findings:
  - num: The proposed method enhances risk detection accuracy by 14.03% compared to existing methods.
  - num: The method improves return rate analysis by 13.28% across financed amounts.
  - num: The CFM-LPA achieves a risk detection rate of 95.21%.
  - num: The return rate analysis achieves 0.97.
  - Federated learning allows continuous updates to lending patterns, ensuring accurate predictions while preserving data privacy.
key_figures_tables:
  - Figure 1: Data used for evaluation from Kaggle dataset → Dataset features for behavior factor analysis.
  - Figure 2: Return rate and credit limit relation → Relationship influences credit risk assessment.
  - Figure 3: Credit risk analysis over time → Risk factors and credit limits monitored over lending periods.
  - Figure 4: Lending pattern analysis → Patterns used to predict credit risk and repayment defaults.
  - Figure 5: Behaviour factor estimation using federated learning → Federated learning assesses behaviour patterns.
  - Figure 6: Behaviour factor analysis across credit periods → Behaviour factor values reflect positive or negative financial behavior.
  - Figure 7: Filtering ratio analysis → High filtering ratio indicates effective separation of risk-prone borrowers.
  - Figure 8: New risk detection over tenure → Proposed method minimizes emergence of new risks.
  - Figure 9: Return rate analysis across limits → Proposed method improves return rate stability.
  - Table 1: Summary of existing models and their limitations → Highlights gaps in current approaches.
key_equations:
  - equation: L(t) = C_lm + Br_C × I_rate + B_fact + C_risk × (1 + B_fact(t+1))
    explanation: Measures micro-lending factors to monitor and predict environmental risk over time.
  - equation: R_rate = R_amt−tot / R_amt × exp(C_lm × Br_C + M_L(t))
    explanation: Computes the ratio of return amount to borrowed amount, adjusting for credit limit.
  - equation: C_lm = B_fact × Br_risk + (1 + C_hist) × C_risk / E_con
    explanation: Measures the credit limit based on borrower risk, credit history, and environmental factors.
  - equation: Len_pat = Σ (amt×C_risk / (1−(1+I_rate))) + (1−Dr_i) × C_lm + H_res(t)
    explanation: Analyzes lending patterns for credit risk using return rate, credit limit, and response rate.
definitions:
  - term: CFM-LPA
    definition: Collaborative Filtering Method using Lending Pattern Analysis for credit risk assessment.
  - term: Federated Learning
    definition: Decentralized machine learning approach that trains models across multiple institutions without sharing raw data.
  - term: Micro-lending
    definition: Provision of small loans to individuals or businesses, often in underserved markets.
  - term: Behavioural Factor
    definition: A metric derived from borrower repayment patterns and credit history used to assess credit risk.
  - term: Return Rate
    definition: The proportion of loan amount that is repaid by the borrower over a given period.
  - term: Credit Limit
    definition: The maximum amount of credit extended to a borrower.
  - term: Collaborative Filtering
    definition: A method that uses historical patterns and similarities between borrowers to predict credit risk.
  - term: FedAvg
    definition: Federated Averaging, an algorithm used to aggregate local model updates in federated learning.
  - term: SMOTE-ENN
    definition: Synthetic Minority Over-sampling Technique with Edited Nearest Neighbour, a method for balancing class distribution.
  - term: LightGBM-GAN
    definition: Light Gradient Boosting Machine with Generative Adversarial Networks, a hybrid credit risk model.
critical_citations:
  - "[Zhuang et al., 2024] — GAN-LightGBM model for credit risk assessment."
  - "[Aruleba et al., 2024] — Ensemble classifiers with SMOTE-ENN for credit risk prediction."
  - "[Yang et al., 2024] — Feature enhanced ensemble modeling for credit risk assessment."
  - "[Rao et al., 2023] — PSO-XGBoost model for personal auto loan credit risk."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Proposes a collaborative filtering method with federated learning for predictive credit risk assessment.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Evaluates forecasting of return rates and risk patterns across sequential repayment periods.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: medium
      justification: Addresses risk factor filtering and reduction through pattern analysis and federated learning.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Detects risky borrower behaviour patterns as anomalies in credit risk assessment.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Uses collaborative filtering and pattern analysis to identify risky repayment anomalies.
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: medium
      justification: Addresses limited borrower data challenges using federated learning for new borrower risk assessment.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Employs federated learning to ensure data privacy by training models locally without sharing raw data.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides comparative analysis with existing models using risk detection and return rate metrics.
  contribution: The paper contributes a novel credit risk assessment method (CFM-LPA) that integrates collaborative filtering and federated learning, which can directly inform Odin's risk detection and forecasting modules. Its privacy-preserving approach supports Odin's data security requirements, while the pattern-based behavioural analysis provides a foundation for user profiling and anomaly detection. The federated learning framework offers a scalable architecture for distributed financial data analysis, relevant to Odin's system evaluation and forecasting components.
  directly_justifies:
    - Federated learning enables privacy-preserving analysis of borrowing patterns across decentralized financial data sources.
    - Continuous behavioural factor updates improve risk detection accuracy by 14.03%.
    - Collaborative filtering effectively identifies lending patterns from historical repayment data.
    - Behavioural pattern analysis enhances return rate predictions across varying financial conditions.
  limits:
    - The model's reliance on collaborative filtering may introduce biases with sparse or imbalanced lending data.
    - Federated learning requires significant computational resources and robust synchronization across institutions.
    - Model drift due to changing data distributions over time is not fully addressed.
    - The approach focuses on micro-lending and may not generalize directly to broader personal finance contexts.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper is directly relevant to Predictive Modeling (6.A, 6.B) and Anomaly Detection (8.A, 8.B, 8.C) due to its CFM-LPA method for credit risk prediction and anomaly identification. It also addresses Data Privacy (10.A) through federated learning, and its evaluation framework relates to System Evaluation (12.A). The budgeting and savings domains were considered but rejected, as the paper focuses on credit risk rather than budget allocation or savings management. The Filipino cultural context domains (1, 2) were rejected as the study uses international data and does not address specific Filipino financial practices. The paper provides medium relevance to Infeasibility Handling (7.D) through its risk filtering process and Cold-Start strategies (8.C) through federated learning for new borrower assessment. Overall, the paper offers actionable insights for Odin's risk assessment, privacy-preserving modeling, and predictive analytics modules.
limitations:
  - The model's collaborative filtering may introduce biases with sparse or imbalanced data. [unacknowledged]
  - Federated learning requires significant computational resources and synchronization, posing scalability challenges. [unacknowledged]
  - Model drift from changing data distributions over time is not thoroughly addressed. [unacknowledged]
  - The approach focuses on micro-lending, potentially limiting generalizability to broader PFMS contexts. [unacknowledged]
remember_this:
  - The CFM-LPA method improves risk detection accuracy by 14.03%.
  - Federated learning enables privacy-preserving analysis of lending patterns.
  - Behavioural factors are updated each return period to refine risk assessment.
  - The method improves return rate analysis by 13.28% across financed amounts.
  - Collaborative filtering identifies patterns to predict credit risk and repayment defaults.
```
---

## Paper 23: Templa et al_summarized.md

**Source File:** `Templa et al_summarized.md`

```yaml
paper_id: "10.70838/pemj.380810"
designation: "local"
title: "The Influence of Financial Literacy on the Budgeting Practices among College Students in a Private Catholic School: Input for Student Literacy Program"
authors: "Templa, E. L.; Andea, R. J. B.; Bagahansol, J. D. M.; Carreon, R. B.; Comendador, L. G.; Labrador, J. G.; Miscreola, D. J. V.; Tapay, A. J. D.; Uson, P. G. R. A."
year: 2025
venue: "Psychology and Education: A Multidisciplinary Journal"
odin_topics:
  - "1.A"
  - "1.B"
  - "1.C"
  - "2.A"
  - "2.B"
  - "2.D"
  - "3.A"
  - "4.A"
  - "4.B"
  - "5.A"
  - "7.A"
  - "7.B"
  - "7.D"
  - "10.A"
  - "10.B"
  - "12.A"
  - "12.B"
  - "12.C"
tldr: "Financial literacy shows a strong positive correlation with budgeting practices among Filipino college students, explaining 75% of the variance in their budgeting behaviors."
problem_and_motivation: "Many college students in the Philippines demonstrate poor budgeting methods and struggle to manage limited funds, indicating a gap between financial knowledge and practical application. While financial literacy is recognized as crucial for sound financial decisions, there is limited research on smaller institutions like private Catholic schools with unique socioeconomic contexts. Understanding this relationship is essential for developing targeted educational interventions to improve student budgeting skills and financial well-being."
approach:
  - "The study employed a quantitative descriptive-correlational research design with 225 randomly selected college students from a private Catholic school in Davao City."
  - "Data were collected using a validated researcher-constructed survey instrument measuring five dimensions of financial literacy and four aspects of budgeting practices."
  - "The survey instrument underwent face validation, pilot testing, and internal reliability testing using Cronbach's alpha, achieving excellent reliability (α = .998 overall)."
  - "Statistical analyses included descriptive statistics (mean, standard deviation), Pearson's R correlation, and linear regression to examine relationships and influences."
findings:
  - "num: Students demonstrated a high overall level of financial literacy (M = 3.95, SD = 0.82), with attitudes toward finance and money being the strongest dimension (M = 4.03)."
  - "Managing financial risk was identified as the area requiring the most improvement among financial literacy dimensions (M = 3.82)."
  - "Students exhibited effective budgeting practices (M = 3.91), with decision-making as the strongest dimension (M = 4.03) and financial control as the weakest (M = 3.77)."
  - "A strong, statistically significant positive correlation exists between financial literacy and budgeting practices (r = 0.85, p < 0.001)."
  - "num: Financial literacy accounts for approximately 75% of the variance in budgeting practices (R² = .723, Adjusted R² = .722)."
  - "Regression analysis revealed financial literacy significantly enhances budgeting behavior (Beta = 0.896, T-value = 24.12, P-value = 0.000)."
  - "Students favored immediate financial needs over long-term planning, reflecting a gap between knowledge and consistent application of budgeting skills."
  - "Financial awareness was high (M = 4.00), but variability in scores indicates inconsistent financial understanding among some students."
key_figures_tables:
  - "Table 1: Financial literacy levels across indicators → Overall mean of 3.95 (High), with risk management lowest at 3.82."
  - "Table 2: Budgeting practices across indicators → Overall mean of 3.91 (High), with decision-making highest at 4.03."
  - "Table 3: Correlation analysis between financial literacy and budgeting skills → Strong positive correlation r = 0.85, p < 0.001."
  - "Table 4: Regression analysis → Financial literacy accounts for 75.1% of variance in budgeting practices, Beta = 0.896, p = 0.000."
key_equations:
  - equation: "r = 0.85, p < 0.001"
    explanation: "Strong positive correlation between financial literacy and budgeting practices."
  - equation: "R² = 0.723, Adjusted R² = 0.722"
    explanation: "Financial literacy explains 72.3% of variance in budgeting behavior."
definitions:
  - term: "Financial Literacy"
    definition: "The set of knowledge and skills necessary to make sound and practical financial choices, encompassing financial awareness, attitudes, risk management, culture, and knowledge."
  - term: "Budgeting Practices"
    definition: "The financial management behaviors involving goal setting, financial control, decision-making, and financial behavior."
  - term: "Theory of Planned Behavior (TPB)"
    definition: "A theory explaining that behavior is influenced by intentions shaped by attitudes, subjective norms, and perceived behavioral control."
  - term: "Financial Literacy Theory"
    definition: "A framework positing that financial literacy equips individuals to make informed decisions about spending, saving, and investing."
critical_citations:
  - "[Lusardi & Mitchell, 2020] — Emphasizes importance of financial education for promoting sound financial behaviors."
  - "[Sanjeev, 2023] — Budgeting is fundamental to financial literacy, requiring allocation of income."
  - "[Huston, 2010] — Financial literacy involves both understanding and application of financial concepts."
  - "[Ajzen, 1991] — Theory of Planned Behavior explains how attitudes and control influence financial intentions."
  - "[Klapper & Lusardi, 2020] — Financial literacy and risk management skills are essential for financial resilience."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "high"
      justification: "Study directly examines Filipino college students as the target demographic for Odin's young professional users."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "medium"
      justification: "Provides data on financial literacy and budgeting behaviors of Filipino students entering the workforce."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Directly measures financial behavior and budgeting practices among Filipino college students."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "high"
      justification: "Study context is a private Catholic school in Davao City, reflecting culturally specific financial practices."
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "low"
      justification: "Mentions challenges with unpredictable expenses and impulsive spending, but does not focus on seasonal cycles specifically."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "low"
      justification: "Discusses spending habits and financial behavior in a Philippine context but does not specifically analyze 'occasions'."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "contextual"
      justification: "Provides background on budgeting practices but does not propose specific expense categorization methods."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Reviews financial literacy landscape in the Philippines, including BSP initiatives, but not specific systems."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "low"
      justification: "Identifies gap in financial literacy education and application, relevant to system design gaps."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "contextual"
      justification: "Provides foundational understanding of financial behaviors that could inform profiling approaches."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "medium"
      justification: "Documents budgeting strategies and practices among students, providing domain knowledge for budget recommendation systems."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "contextual"
      justification: "Findings on budgeting practices could inform how budget recommendations might be tailored to students."
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "contextual"
      justification: "Students' struggles with financial control and unpredictable expenses suggest need for flexible handling mechanisms."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "contextual"
      justification: "Study's ethical considerations mention Data Privacy Act of 2012, relevant to data privacy in PFMS."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "contextual"
      justification: "Implications for building trust through effective financial education and support, relevant to system adoption."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Uses correlation and regression analysis methodologies that could inform evaluation frameworks for Odin modules."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "low"
      justification: "Methodology of correlational analysis could apply to evaluating behavioral profiling or forecasting modules."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "low"
      justification: "Correlational and regression approach could inform evaluation of budget recommendation effectiveness."
  contribution: "This study demonstrates that financial literacy is a key determinant of budgeting practices among Filipino college students, with the relationship being strong and statistically significant. The findings validate the Financial Literacy Theory and Theory of Planned Behavior in a Philippine context, providing empirical support for integrating financial education into Odin's design. The study's quantitative framework can inform the evaluation of Odin's recommendation and forecasting modules, particularly in measuring the impact of behavioral interventions on user outcomes."
  directly_justifies:
    - "Financial literacy explains 75% of the variance in budgeting practices among Filipino college students."
    - "Students with higher financial literacy demonstrate stronger goal setting, financial control, and decision-making skills."
    - "Managing financial risk is an area requiring improvement, suggesting need for targeted educational content in Odin."
    - "Positive financial attitudes correlate with responsible budgeting behaviors, supporting behavior-focused system features."
  limits:
    - "The study uses self-reported data, which may introduce biases in respondents' assessments of their financial literacy and budgeting practices. [unacknowledged]"
    - "The study does not account for external factors such as socioeconomic background or exposure to financial education outside the classroom. [unacknowledged]"
    - "The sample is limited to students from a single private Catholic school in Davao City, which may limit generalizability to other demographics. [unacknowledged]"
    - "The study does not explore the influence of emerging technologies like AI or machine learning on budgeting practices, representing a gap in the literature. [acknowledged]"
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was conducted. The paper was flagged as highly relevant to Filipino Cultural Context (Topics 2.A, 2.D) as it studies Filipino students, and to Behavioral Profiling & Classification (Topics 1.A, 1.C) through its detailed measurement of financial behaviors. Medium relevance was assigned to Budget Recommendation (Topics 7.A, 7.B) and System Evaluation (Topic 12.A) due to the study's quantitative analysis that can inform Odin's recommendation and evaluation modules. Contextual relevance was identified for Expense Categorization (Topic 3.A) and Data Privacy (Topics 10.A, 10.B) due to mentions of privacy considerations. Low relevance was assigned to Seasonal Spending (Topics 2.B, 2.D) and Algorithmic Forecasting (Topics 6.A, 6.B) as the study does not address predictive modeling. Borderline cases included Topics 1.A and 2.A, which were both selected due to the dual demographic and cultural focus. Topics related to Anomaly Detection (Topics 8.A, 8.B, 8.C), User Retention (Topics 11.A, 11.B), and Savings & Debt Management (Topics 13.A, 13.B, 13.C) were considered and rejected as the paper does not address these specific PFMS functionalities. Overall, the paper is moderately relevant to Odin, providing foundational empirical evidence on Filipino financial behaviors that can inform multiple design and evaluation aspects."
limitations:
  - "Self-reported data may introduce biases in respondents' assessments of their financial literacy and budgeting practices. [unacknowledged]"
  - "The study does not account for external factors such as socioeconomic background or exposure to financial education outside the classroom. [unacknowledged]"
  - "The sample is limited to students from a single private Catholic school in Davao City, which may limit generalizability to other demographics. [unacknowledged]"
  - "The study does not explore the influence of emerging technologies like AI or machine learning on budgeting practices, representing a gap in the literature. [acknowledged]"
remember_this:
  - "Financial literacy explains 75% of the variance in student budgeting behavior."
  - "Students show strong financial attitudes but struggle with consistent budget application."
  - "Decision-making is the strongest budgeting skill among Filipino college students."
  - "Risk management is the weakest financial literacy dimension requiring improvement."
  - "Correlation between financial literacy and budgeting practices is r = 0.85, p < 0.001."
```
---

## Paper 24: Ghonaim & El-Sharawy_summarized.md

**Source File:** `Ghonaim & El-Sharawy_summarized.md`

```yaml
paper_id: 10.21608/IJTAR.2025.427658.1148
designation: international-algorithm-specific
title: An Intelligent Budget Management Mobile Application Based on a Recurrent Neural Network
authors: Ghonaim, W. A.; El-Sharawy, E. E.
year: 2025
venue: International Journal of Theoretical and Applied Research
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 9.A
  - 9.B
tldr: Develops a bilingual mobile budget app using an RNN to classify financial transaction risk, achieving 97.45% accuracy across low, medium, and high risk categories.
problem_and_motivation: Existing budgeting apps often lack Arabic language support and AI-based forecasting features. This paper addresses the gap by developing a mobile application that combines RNN-based risk prediction with a user-friendly interface for Arabic and English speakers.
approach:
  - Dataset of 1,048,576 financial transactions from Kaggle was used, split 70/15/15 for training, validation, and testing.
  - A bidirectional LSTM with two hidden layers (128 units each) and ReLU activation was implemented.
  - Risk labels (low/medium/high) were constructed using a scoring method based on income, debt, transaction frequency, and budget adherence.
  - The model was deployed via a Flask API with Firebase Firestore, integrating with a React Native mobile frontend.
  - Evaluation used precision, recall, F1-score, and accuracy, comparing predictions to actual risk levels.
findings:
  - num: 97.45% overall accuracy was achieved on the test set.
  - num: Precision, recall, and F1-score all exceeded 0.97 for each risk category.
  - The model demonstrated high reliability in detecting both low and high-risk financial behaviors.
  - The mobile application successfully integrated AI predictions with real-time user alerts.
  - Functional testing confirmed the stability and usability of the application for key features like registration and transaction entry.
key_figures_tables:
  - Table 2: Classification report showing precision, recall, and F1-score per risk level → All metrics exceed 0.97.
  - Table 3: Confusion matrix illustrating prediction alignment across risk categories → Strong diagonal values with minor overlaps in medium risk.
  - Figure 5: Report and Add Account interfaces → Visualizes the user workflow for managing financial accounts.
  - Figure 6: My Budget and Add Budget interfaces → Shows the interface for setting and managing budget categories.
key_equations:
  - equation: Precision = TP / (TP + FP)
    explanation: Measures the accuracy of positive predictions.
  - equation: Recall = TP / (TP + FN)
    explanation: Measures the ability to find all positive instances.
  - equation: F1 = 2 * (Precision * Recall) / (Precision + Recall)
    explanation: Harmonic mean of precision and recall.
definitions:
  - term: RNN
    definition: Recurrent Neural Network, a class of neural networks for sequential data.
  - term: LSTM
    definition: Long Short-Term Memory, an advanced RNN variant for long-term dependencies.
  - term: GRU
    definition: Gated Recurrent Unit, a simplified LSTM variant.
  - term: Firestore
    definition: Firebase's NoSQL cloud database for real-time data synchronization.
  - term: Flask
    definition: A Python microframework for building web APIs.
critical_citations:
  - "[Hochreiter & Schmidhuber, 1997] — Introduces LSTM architecture."
  - "[Cho et al., 2014] — Introduces GRU architecture."
  - "[Pascanu et al., 2013] — Discusses vanishing gradient problem in RNNs."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: App includes expense tracking and categorization.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: low
      justification: Mentions categories like necessities and discretionary spending.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Extensively reviews and compares existing budgeting applications.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies lack of Arabic support and AI features as key gaps.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses RNN to classify transactions into risk profiles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Core contribution is RNN-based risk prediction.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Applies RNN (LSTM) to sequential financial transaction data.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: App provides budgeting features and strategies.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Offers personalized financial plans and recommendations.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Risk prediction can alert users to potential financial issues.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Model detects high-risk spending patterns as anomalies.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Developed as a mobile-first application using React Native.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Designed over 27 interfaces with a focus on user experience.
  contribution: The paper provides a complete implementation of an RNN-based risk classifier that can be integrated into Odin's Anomaly Detection module to flag high-risk spending. The comparative analysis of existing apps informs Odin's competitive positioning and feature prioritization, particularly the need for AI-driven insights and multilingual support. The study's validation methodology, including precision, recall, and F1, offers a template for evaluating Odin's classification modules. The system's architecture combining Firebase, Flask, and React Native provides a blueprint for Odin's mobile-first, cloud-backed design. Finally, the user-centric features like real-time alerts and budget tracking directly justify similar components in Odin's Mobile UX and Budget Recommendation modules.
  directly_justifies:
    - Bilingual support and AI forecasting are critical gaps in existing PFMS apps.
    - RNNs can effectively classify financial risk from sequential transaction data.
    - 97.45% accuracy validates the reliability of deep learning for spending risk assessment.
    - Real-time budget alerts improve user financial awareness and decision-making.
  limits:
    - The risk labeling process was heuristic and may not generalize to all user contexts.
    - The study lacks longitudinal user studies to assess real-world impact on financial behavior.
    - No comparison with baseline or alternative ML models (e.g., GRU, XGBoost) for risk prediction.
  mapping_rationale: The paper was systematically scanned against all 12 functional domains and their associated topic codes. The "Expense Categorization" domain was flagged as medium relevance (3.A, 3.B) due to the app's transaction categorization. "Existing Systems & Gaps" was high relevance (4.A, 4.B) from the comprehensive literature review and comparative analysis. "Behavioral Profiling" was medium (5.C) via risk profile classification. "Spending Forecasting" was high (6.A, 6.B) due to the core RNN prediction task. "Budget Recommendation" was medium (7.A, 7.B) from the personalized planning features. "Anomaly Detection" was high (8.A, 8.B) through risk detection. "Mobile-First Design" was medium (9.A, 9.B) given the app's development focus. Domains like "Filipino Cultural Context" and "Savings & Debt Management" were considered but rejected as the paper is Egypt-based and does not address specific Filipino practices or advanced savings/debt features. The paper's primary relevance to Odin lies in its practical demonstration of AI-driven risk classification within a mobile PFMS context, offering a validated approach for the Forecasting and Anomaly Detection modules.
limitations:
  - Risk labels were artificially constructed from financial indicators, not verified against real-world financial distress outcomes. [unacknowledged]
  - The model was trained on fraud detection data, which may not fully represent general spending behavior for budget management. [unacknowledged]
  - No long-term user study was conducted to measure the app's actual impact on budgeting behavior or financial health.
remember_this:
  - The RNN model achieved 97.45% accuracy in classifying spending risk levels.
  - Arabic and English language support was a primary design requirement for the app.
  - The system provides real-time risk alerts based on transaction patterns.
  - The application architecture uses Firebase for backend and React Native for frontend.
  - Personal financial plans and recommendations are generated using AI predictions.
```
---

## Paper 25: Stylianou & Pantelidou_summarized.md

**Source File:** `Stylianou & Pantelidou_summarized.md`

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
---

## Paper 26: Levi_summarized.md

**Source File:** `Levi_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international-algorithm-specific
title: Personal Financial Information Presentation and Consumer Spending
authors: Levi, Y.
year: 2025
venue: Unknown
odin_topics:
  - 2.B
  - 5.B
  - 6.B
  - 7.B
  - 8.B
  - 9.B
  - 11.A
  - 12.B
tldr: Consumers exposed to a consumption-oriented frame and a salient comparison of a personalized net-worth index with past spending reduced discretionary spending by 15%.
problem_and_motivation: Individuals interact with finances digitally, but the influence of information presentation on spending behavior is underexplored. A gap exists in understanding if simple design changes can overcome strong spending habits. This study tests if framing and salience of financial information can prompt consumers to adjust spending.
approach:
  - Randomized field experiment with 3,138 users of an online account aggregation app.
  - Personalized index presented net worth as lifetime monthly cash flow from an annuity.
  - Treatments varied index name: Financial Sustainability Index (FSI, consumption frame) vs. Life Annuity Index (LAI, neutral frame).
  - Salience manipulated by providing a context plot comparing the index to historical monthly spending.
  - Difference-in-differences analysis with individual and event-month fixed effects.
findings:
  - num: FSI-Plot group reduced discretionary spending by 15% relative to control during the 8-month experiment.
  - num: Effect persisted for 8 months after treatment removal, with a gradual return to baseline.
  - num: Spending decreased in restaurants (14%), clothing (20%), entertainment (14%), travel (24%), and cash withdrawals (25%).
  - No significant change in non-discretionary spending categories like gas, groceries, and utilities.
  - No effect from the index name or context plot alone; both consumption frame and salient context were necessary.
  - Login frequency increased similarly across all treated groups, controlling for attention effects.
key_figures_tables:
  - Figure 3: Monthly logins by treatment group → All treated groups increased logins similarly.
  - Figure 4: Monthly discretionary spending by treatment group → FSI-Plot groups diverged lower immediately at experiment start.
  - Table 5: Treatment effects on discretionary spending → FSI-Plot groups show 15% decrease during intra period.
  - Table 7: Spending category effects → Reductions largest in restaurants, clothing, entertainment, travel, and cash.
key_equations:
  - equation: y_{i,t} = \sum_{j=2}^{5} \beta_j TG_{j,i} Intra_t + \sum_{j=2}^{5} \gamma_j TG_{j,i} Post_t + \delta_i + \theta_j + \epsilon_{i,t}
    explanation: Main diff-in-diff specification with individual and month fixed effects.
definitions:
  - term: FSI
    definition: Financial Sustainability Index, the consumption-framed name for the personalized index.
  - term: LAI
    definition: Life Annuity Index, the neutral-framed name for the personalized index.
  - term: Personalized Index
    definition: Net worth presented as the equivalent inflation-protected lifetime monthly cash flow.
  - term: Context Plot
    definition: Time series plot directly comparing the index level with the user's historical monthly spending.
critical_citations:
  - "[Benartzi et al., 2011] — Annuitization puzzles and framing effects on annuity valuation."
  - "[Goldstein et al., 2016] — Illusion of wealth from lump-sum vs. cash-flow presentation."
  - "[Karlan et al., 2016] — Salient reminders promote staying within means."
  - "[Sussman and Alter, 2012] — Underestimation of exceptional expenses leads to overspending."
relevance:
  topics:
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: Provides evidence of spending adjustments in response to information, not seasonal drivers.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: Results suggest behavioral response to a reference point, but not directly profile classification.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: Uses historical spending data, but does not develop or test forecasting algorithms.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: Directly tests how presenting a benchmark (the index) influences spending, a core budget recommendation mechanism.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Examines spending changes in categories, but not anomaly detection methods.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Tests information presentation within a digital (app) environment, relevant to UX design choices.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Measures login behavior as a proxy for attention, relevant to engagement.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides a rigorous experimental evaluation framework (RCT, diff-in-diff) applicable to evaluating Odin's modules.
  contribution: This paper provides a rigorous experimental framework for testing information presentation effects, directly applicable to evaluating Odin's budget recommendation module. The finding that a salient benchmark reduces spending offers a design principle for Odin's interface to encourage savings. The persistence of the effect beyond treatment exposure informs retention strategies for Odin. The detailed spending category analysis can guide Odin's expense categorization and anomaly detection design by highlighting responsive categories.
  directly_justifies:
    - A consumption-oriented frame combined with a salient context can reduce discretionary spending by 15%.
    - Information design can influence spending behavior without changing economic variables.
    - Effects persist for months after treatment removal, suggesting habit formation.
    - Non-discretionary spending is less responsive to information interventions.
  limits:
    - Sample consists of relatively wealthy users (top 20% income), limiting generalizability to lower-income Filipino young professionals.
    - Data may be incomplete if users did not link all financial accounts to the app.
    - The experiment was conducted in 2014, before pre-registration became common.
    - The study population is U.S.-based, which may not fully reflect Filipino cultural and financial contexts.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated canonical topic codes was conducted. The paper was flagged as relevant primarily for the "Budget Recommendation" (7.B) and "System Evaluation" (12.B) domains, receiving a 'high' relevance assignment, as the experimental design directly tests a benchmark-based spending adjustment mechanism and provides a rigorous evaluation framework. It also touches on "User Retention & Engagement" (11.A) and "Mobile UX Design" (9.B) with a 'medium' relevance, as the study measures attention effects and manipulates in-app information presentation. Topics related to "Seasonal Spending" (2.B) and "Profile Dynamics" (5.B) were considered but assigned 'low' relevance, as the paper does not directly model seasonality or user profiles. Domains like "Anomaly Detection" (8.B) and "Forecasting" (6.B) were rejected for direct inclusion, as the paper does not propose or evaluate algorithms in these areas. The paper's overall relevance is moderate, providing a foundational experimental paradigm and evidence of behavioral responsiveness to information design, but its U.S.-based, high-income sample limits direct applicability to the Filipino young professional demographic.
limitations:
  - Sample consists of relatively wealthy U.S. users, limiting generalizability to Filipino young professionals. [unacknowledged]
  - Potential incompleteness of transaction data from account aggregation. [unacknowledged]
  - Experiment was conducted in 2014, before pre-registration became common.
  - The study does not explore the exact psychological mechanism (e.g., anchoring vs. reference point updating).
remember_this:
  - Presenting a consumption-framed benchmark with a context plot reduced discretionary spending by 15%.
  - The spending reduction persisted for eight months after the intervention was removed.
  - Largest decreases occurred in restaurants, clothing, entertainment, travel, and cash withdrawals.
  - Information design effects require both a relevant frame and a salient comparison context.
  - Login frequency increased similarly across all treatments, ruling out attention as the primary driver.
```
---

## Paper 27: Shakhovska & Pukach_summarized.md

**Source File:** `Shakhovska & Pukach_summarized.md`

```yaml
paper_id: 10.3390/ai6110279
designation: international-algorithm-specific
title: Severity-Aware Drift Adaptation for Cost-Efficient Model Maintenance
authors: Shakhovska, K.; Pukach, P.
year: 2025
venue: AI
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 7.B
  - 12.B
tldr: A severity-aware framework quantifies data drift using KS, Wasserstein, and JS divergences, triggering incremental updates for moderate drift and full retraining for severe drift, reducing costs while maintaining model accuracy.
problem_and_motivation: Data distributions in real-world systems change over time, degrading model accuracy, yet existing drift-handling methods often retrain unnecessarily, incurring high computational costs. A principled way to distinguish drift severity and adapt proportionally is missing. This paper addresses that gap by introducing a severity-aware adaptation mechanism.
approach:
  - The framework maintains short-term and long-term windows over streaming data.
  - It computes a severity score as a weighted combination of KS, Wasserstein, and Jensen-Shannon divergences between window distributions.
  - Based on score thresholds, it applies no update, incremental fine-tuning, or full retraining.
  - Quantile transformation is tested as a lightweight preprocessing step to align new data to the historical baseline.
  - Experiments are conducted on salary, housing, and gas sensor datasets to evaluate drift detection and transformation effectiveness.
  - Time and memory complexity are analyzed, showing efficiency compared to ensemble methods like ROSE.
findings:
  - num: The KS statistic between 2023 and 2024 salaries decreased from 0.0559 to 0.0072 after quantile transformation.
  - num: Combined drift scores showed no drift for 2023 vs 2024, low drift for 2022 vs 2024, and significant drift for 2021 vs 2024 after normalization.
  - num: In the gas sensor dataset, 93% of features exhibited significant drift across batches.
  - The severity-aware policy reduces unnecessary retraining by responding proportionally to drift magnitude.
  - Subgroup-level analysis can reveal drift masked by pooled aggregation, as seen in housing data where 44 of 45 areas showed significant drift despite overall no drift.
key_figures_tables:
  - Figure 2: Salary trend over time with 95% CI → salaries increased, indicating temporal drift.
  - Figure 3: Boxplot of salary by year and experience level → drift magnitude varies by seniority.
  - Figure 6: Stacked bar of drift categories across gas sensor batches → significant drift dominates after early batches.
  - Table 6: Normalized combined scores for year comparisons → scores differentiate no, low, and significant drift.
  - Table 9: Top 5 most and least drifted features in gas data → identifies unstable sensors.
key_equations:
  - equation: d_m = m(P_s, P_l)
    explanation: Metric between short-term and long-term distributions.
  - equation: S = α d_KS + β d_W + γ d_JS
    explanation: Weighted aggregation of three drift metrics.
  - equation: x_new_transformed = F_old^{-1}(F_new(x_new))
    explanation: Quantile transformation maps new data to reference distribution.
definitions:
  - term: KS statistic
    definition: Maximum difference between two empirical cumulative distribution functions.
  - term: Wasserstein distance
    definition: Average displacement between two probability distributions.
  - term: Jensen-Shannon divergence
    definition: Symmetric and bounded measure of similarity between two distributions.
  - term: Quantile transformation
    definition: Non-parametric mapping that aligns the quantiles of one distribution to another.
critical_citations:
  - "[Gama et al., 2014] — Survey on concept drift adaptation."
  - "[Cano and Krawczyk, 2022] — ROSE ensemble for drifting imbalanced streams."
  - "[Yang et al., 2021] — Lightweight drift detection for IoT."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Provides a general model maintenance framework for predictive modules.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Directly addresses drift adaptation to preserve forecasting accuracy.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Drift affects anomaly detection; adaptation improves system robustness.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Offers algorithmic methods to adjust anomaly detection under distributional shifts.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Budget recommendations benefit from adaptive updates based on changing spending patterns.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: The evaluation methodology for drift severity can inform Odin's module assessments.
  contribution: The severity-aware drift adaptation framework can be integrated into Odin's spending forecasting module (6.B) to maintain prediction accuracy over time, as spending patterns drift. It also supports anomaly detection (8.B) by enabling dynamic adjustment of detection thresholds when distributional shifts occur, reducing false alarms. For budget recommendation (7.B), the framework provides a mechanism to update allocation constraints in response to evolving user expenses, improving personalization. The quantile transformation offers a lightweight preprocessing step to reduce distributional shifts before retraining, saving computational resources in Odin's real-time pipeline. Additionally, the evaluation approach (12.B) offers a methodology for assessing model maintenance strategies in Odin's algorithmic modules.
  directly_justifies:
    - Quantile transformation reduced the KS statistic from 0.0559 to 0.0072, effectively mitigating covariate drift.
    - The severity score enables selective adaptation, avoiding full retraining for minor drift and reducing computational cost.
    - Subgroup-level drift analysis can detect localized changes that pooled analysis misses, informing targeted model updates.
    - The framework's time complexity is O(d(w log w + b)), making it suitable for streaming environments.
  limits:
    - Datasets may not fully reflect real-world distributions, affecting metric stability.
    - Pooled analysis may mask subgroup-level drift, requiring stratified detection.
    - The method is sensitive to temporal window size; small windows produce noise, large windows obscure short-term shifts.
    - Small-sample effects can yield unreliable statistical outputs, overestimating drift.
    - Current implementation is restricted to continuous variables; categorical drift is not handled.
  mapping_rationale: All 12 functional domains and their associated topic codes were systematically scanned. The following domains were flagged as relevant: Spending Forecasting (6.A, 6.B) because the paper directly addresses model maintenance under data drift, which is critical for forecasting accuracy; Anomaly Detection (8.A, 8.B) because drift affects anomaly detection performance and the proposed adaptation improves robustness; Budget Recommendation (7.B) because budget suggestions must adapt to changing spending patterns; and System Evaluation (12.B) because the paper provides an evaluation framework for model updates. Relevance levels: 6.B and 8.B high, 6.A and 8.A medium, 7.B and 12.B medium. Borderline cases: the paper's drift detection could also relate to Behavioral Profiling (5.A) as user behavior changes over time, but it does not classify profiles, so it was rejected as low. Seasonal spending (2.B) was considered but the paper does not address seasonality specifically. Cultural practices (2.A) and expense categorization (3.A) were not relevant. Overall, the paper offers a general adaptation mechanism applicable to multiple Odin modules that rely on time-series data.
limitations:
  - Datasets may not fully reflect real-world distributions, affecting metric stability.
  - Pooled analysis may mask subgroup-level drift, requiring stratified detection.
  - The method is sensitive to temporal window size; small windows produce noise, large windows obscure short-term shifts.
  - Small-sample effects can yield unreliable statistical outputs, overestimating drift.
  - Current implementation is restricted to continuous variables; categorical drift is not handled. [unacknowledged]
remember_this:
  - Quantile transformation reduced KS statistic from 0.0559 to 0.0072.
  - Severity-aware adaptation avoids full retraining for minor drift, saving computational resources.
  - Subgroup-level drift analysis reveals localized changes masked by aggregate statistics.
  - The framework uses three complementary metrics to quantify drift severity robustly.
  - Lightweight preprocessing can delay costly retraining in streaming environments.
```
---

## Paper 28: Pritam & Pramod_summarized.md

**Source File:** `Pritam & Pramod_summarized.md`

```yaml
paper_id: "10.56352/sei/8.3.501"
designation: "international-algorithm-specific"
title: "Recommender System for Banking Industry with Collaborative Filtering and XGBoost Classifier"
authors: "Pritam, A.; Pramod, D."
year: 2025
venue: "Science, Education and Innovations in the Context of Modern Problems"
odin_topics:
  - "4.B"
  - "5.B"
  - "5.C"
  - "8.C"
tldr: "A hybrid recommendation system combining XGBoost multilabel classification and collaborative filtering predicts banking product uptake and recommends complementary products to customers."
problem_and_motivation: "Existing recommendation systems are not widely used in banking, limiting customer engagement and revenue. Banks need personalized product recommendations to improve satisfaction and loyalty. A hybrid approach can address cold-start and sparsity issues in banking recommenders."
approach:
  - "Collected primary data via structured questionnaire from personal banking customers across India, capturing user demographics and product usage/ratings."
  - "Applied XGBoost multilabel classifier on user features to predict whether a customer will opt for each banking product."
  - "Implemented item-to-item collaborative filtering using KNN with cosine similarity on the rating matrix to recommend additional products."
  - "Evaluated the XGBoost model using F1-score and ROC AUC; used clustering (K-Means+PCA) to visualize user segments."
  - "Addressed user cold-start by using XGBoost predictions for new customers when collaborative filtering lacks ratings."
findings:
  - "num: XGBoost classifier achieved an F1-score of 0.73 for product uptake prediction."
  - "num: ROC AUC was 0.76, indicating good discriminative ability."
  - "Collaborative filtering with KNN (k=20) produced sample recommendations such as mutual funds and savings accounts for fixed deposit holders."
  - "The hybrid approach mitigates the user cold-start problem by enabling predictions for new customers without rating history."
key_figures_tables:
  - "Figure 1: Age distribution of respondents shows peaks at 24-28 and 45-55 years."
  - "Figure 2: Classification report for XGBoost showing precision, recall, and F1-score per product class."
  - "Figure 3: PCA-reduced clusters of customers based on product ratings, indicating distinct user segments."
  - "Figure 4: Sample recommendation output for a fixed deposit customer, suggesting mutual funds, savings account, and recurring deposit."
key_equations:
  - equation: "Cosine Similarity = (A·B) / (||A|| ||B||)"
    explanation: "Measures similarity between item rating vectors for collaborative filtering."
definitions:
  - term: "Collaborative Filtering"
    definition: "Recommends items based on similarity between users or items using ratings."
  - term: "XGBoost"
    definition: "Gradient boosted decision tree algorithm used for classification."
  - term: "KNN"
    definition: "K-Nearest Neighbors algorithm for classification and similarity-based recommendation."
  - term: "Cold-start"
    definition: "Problem of making recommendations for new users or items with no prior data."
critical_citations:
  - "[Adeniyi et al., 2016] — Automated web usage recommendation using KNN."
  - "[Davidson et al., 2010] — YouTube video recommendation system, basis for collaborative filtering."
  - "[Chirkina & Rankov, 2018] — Recommender system for private banking, relevant domain."
relevance:
  topics:
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Paper discusses gaps like cold-start and sparsity in banking recommenders."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "high"
      justification: "Proposes XGBoost to handle user cold-start when collaborative filtering fails."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Uses XGBoost multilabel classification to predict product uptake based on user attributes."
    - code: "8.C"
      name: "Cold‑Start Baseline Strategies for Anomaly Detection"
      relevance: "medium"
      justification: "Cold-start solution via classification can inform anomaly detection baselines for new users."
  contribution: "The paper's cold-start handling via XGBoost directly informs Odin's user profiling module (5.B) and can be adapted for initial budget recommendations. The classification approach (5.C) provides a method to predict user financial behaviors, supporting Odin's behavioral classification. The collaborative filtering technique offers a foundation for recommending savings products or budget allocations in Odin. The evaluation metrics (F1, ROC) serve as benchmarks for Odin's machine learning modules. The discussion of sparsity and cold-start issues highlights important design considerations for Odin's recommendation and anomaly detection systems."
  directly_justifies:
    - "Hybrid recommendation models can mitigate cold-start problems in personal finance systems."
    - "XGBoost classification can predict product adoption based on user demographics."
    - "Collaborative filtering with cosine similarity can recommend complementary financial products."
    - "Evaluation with F1-score and ROC AUC is effective for multi-label classification in finance."
  limits:
    - "Dataset limited to metro and urban Indian cities, not representative of all populations."
    - "Popularity bias and sparsity of rating matrix affect recommendation quality."
    - "Item cold-start problem remains unresolved."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant to the Existing Systems & Gaps domain (topic 4.B) because it identifies limitations in banking recommendation systems. It strongly aligns with Behavioral Profiling & Classification (5.B and 5.C) as it explicitly addresses cold-start and uses classification for user profiling. It also touches on Anomaly Detection (8.C) through its cold-start handling, which could inform baseline strategies. Domains such as Filipino Cultural Context, Expense Categorization, Spending Forecasting, Budget Recommendation (except maybe indirectly), Mobile-First Design, Data Privacy (only mentioned briefly), User Retention (only general), and Savings/Debt Management were considered but rejected due to lack of direct evidence. The paper's overall relevance to Odin is moderate, providing a methodological example for classification and cold-start handling that can be adapted to personal finance management."
limitations:
  - "Dataset limited to metro and urban cities, not covering rural India. [unacknowledged]"
  - "Popularity bias and sparsity of rating matrix remain issues."
  - "Item cold-start problem persists."
  - "Scalability not tested on big data platforms; requires HDFS for large-scale use."
  - "Data privacy and security concerns are mentioned but not addressed in the model. [unacknowledged]"
remember_this:
  - "XGBoost classifier achieved F1-score of 0.73 for product uptake prediction."
  - "Collaborative filtering recommends complementary products based on item similarity."
  - "Hybrid approach addresses user cold-start via classification when ratings are missing."
  - "Evaluation showed ROC AUC of 0.76, indicating good predictive performance."
  - "The model is a proof of concept for banking product recommendations in India."
```
---

## Paper 29: Zhang & Duan_summarized.md

**Source File:** `Zhang & Duan_summarized.md`

```yaml
paper_id: "10.3389/fams.2025.1628652"
designation: "international-algorithm-specific"
title: "Accounting data anomaly detection and prediction based on self-supervised learning"
authors: "Zhang, Y.; Duan, B."
year: 2025
venue: "Frontiers in Applied Mathematics and Statistics"
odin_topics:
  - "8.A"
  - "8.B"
  - "8.C"
  - "12.A"
  - "12.B"
tldr: "A hierarchical fusion self-supervised learning framework detects accounting anomalies with 0.820 F1, 0.726 early detection rate, and 0.068 false alarm rate using CSMAR data from 2000-2020."
problem_and_motivation: "Traditional anomaly detection methods depend on scarce labeled data and fail to capture complex multidimensional interactions in accounting data. The dynamic evolution of financial fraud techniques renders static rule-based and supervised approaches inadequate for early warning. A self-supervised framework that leverages unlabeled data and domain knowledge is needed to address these gaps."
approach:
  - "Used CSMAR database financial data from Chinese listed companies (2000-2020), with 28,569 valid observations after cleaning."
  - "Proposed Hierarchical Fusion Self-Supervised Learning (HFSL) with three layers: feature representation via temporal contrastive learning, relationship reasoning via dual-channel LSTM autoencoder, and anomaly detection via reconstruction error and rule violation scoring."
  - "Employed industry calibration, seasonal adjustment using X-13 ARIMA-SEATS, and noise suppression as adaptive data preprocessing."
  - "Trained using only normal samples in self-supervised paradigm with reconstruction and contrastive loss combination; optimized via Bayesian hyperparameter search."
  - "Compared against Z-score, One-Class SVM, Isolation Forest, LSTM-AE, and VAE baselines on 5,098 test observations."
findings:
  - "num: 0.836 precision, 0.805 recall, and 0.820 F1-score for anomaly detection."
  - "num: 0.726 early detection rate within first two quarters and 0.068 false alarm rate."
  - "num: 0.883 AUC-ROC and 0.772 AUC-PR demonstrating strong classification capability."
  - "ROE (0.196 SHAP) and ROA (0.179 SHAP) are the most important features for anomaly identification."
  - "Identified five fraud patterns: revenue inflation (38.6%, 87.3% detection), expense concealment (21.7%, 84.5%), asset overvaluation (17.4%, 79.8%), liability understatement (15.2%, 82.1%), and composite manipulation (7.1%, 68.2%)."
  - "Detected three temporal evolution patterns: progressive deterioration (64%), sudden anomalies (22%), and cyclical fluctuations (15%)."
  - "Feature interaction analysis revealed enhancing effects between ROE-ROA (0.087) and Current-Leverage ratios (0.082), improving F1 by 3.5% when incorporated."
  - "Outperformed LSTM-AE by 7% F1, Isolation Forest by 15%, and Z-score by 35% on F1-score."
  - "Cross-industry performance best in Finance (0.872 F1) and weakest in Construction/Real Estate (0.776 F1), with industry calibration improving cross-industry early detection by 14.6%."
key_figures_tables:
  - "Figure 1: HFSL architecture diagram → Shows three-tier cascaded structure from feature learning to anomaly detection."
  - "Figure 4: Performance comparison across six metrics → HFSL achieves highest F1 (0.820) and lowest false alarm rate (0.068)."
  - "Figure 5: Radar chart of anomaly type performance → Best on mutation anomalies (0.892), weakest on temporal patterns (0.791)."
  - "Figure 6: Detection performance across anomaly types → Confirms model's sensitivity hierarchy from sudden to complex anomalies."
  - "Table 3: Industry-specific performance → Finance highest at 0.872, Construction/Real Estate lowest at 0.776 F1."
key_equations:
  - equation: "L_con = -log(exp(sim(z_i,z_j)/τ) / Σ_{k≠i} exp(sim(z_i,z_k)/τ))"
    explanation: "Contrastive loss for temporal feature learning in first layer."
  - equation: "z = α·f_s(X^{w_s}) + (1-α)·f_l(X^{w_l})"
    explanation: "Attention-fused dual-channel LSTM representation."
  - equation: "Score(X) = λ·((E_recon-μ_recon)/σ_recon) + (1-λ)·((E_rule-μ_rule)/σ_rule)"
    explanation: "Final anomaly score combining reconstruction and rule violations."
  - equation: "θ = μ_high + γ·σ_high"
    explanation: "Adaptive threshold from GMM high-variance component."
  - equation: "Score_final(X) = w_p·Score_p(X) + w_s·Score_s(X) + w_r·Score_r(X)"
    explanation: "Multi-scale scoring: point, sequence, and relationship anomalies."
definitions:
  - term: "HFSL"
    definition: "Hierarchical Fusion Self-Supervised Learning framework for anomaly detection."
  - term: "LSTM"
    definition: "Long Short-Term Memory, a recurrent neural network architecture."
  - term: "SHAP"
    definition: "SHapley Additive exPlanations, for feature importance attribution."
  - term: "GMM"
    definition: "Gaussian Mixture Model for adaptive threshold determination."
  - term: "CSMAR"
    definition: "China Stock Market and Accounting Research database."
  - term: "ROE"
    definition: "Return on Equity, a profitability indicator."
  - term: "ROA"
    definition: "Return on Assets, a profitability indicator."
  - term: "EDR"
    definition: "Early Detection Rate, proportion detected within first two quarters."
  - term: "FAR"
    definition: "False Alarm Rate, proportion of normal samples incorrectly classified."
  - term: "X-13 ARIMA-SEATS"
    definition: "Seasonal adjustment method for time series decomposition."
  - term: "MAD"
    definition: "Median Absolute Deviation, a robust scale estimator."
  - term: "MCD"
    definition: "Minimum Covariance Determinant, a robust covariance estimator."
critical_citations:
  - "[Ellili et al., 2024] — SEC fraud cases increased 30% 2020-2023."
  - "[Altman, 1968] — Foundational Z-score bankruptcy prediction method."
  - "[Beneish, 1999] — M-score detection of earnings manipulation."
  - "[Dechow et al., 2011] — Predicting material accounting misstatements."
  - "[Perols, 2011] — Statistical vs ML for financial fraud detection."
  - "[Bao et al., 2020] — Machine learning approach for US fraud detection."
relevance:
  topics:
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Core contribution: novel self-supervised framework specifically for anomaly detection."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Provides LSTM-based deep learning algorithm for time-series anomaly detection."
    - code: "8.C"
      name: "Cold-Start Baseline Strategies for Anomaly Detection"
      relevance: "high"
      justification: "Self-supervised learning directly addresses labeled data scarcity in cold-start scenarios."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Comprehensive multi-metric evaluation including precision, recall, F1, AUC, EDR, FAR."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Comparative evaluation against multiple baseline algorithms including LSTM-AE and VAE."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "low"
      justification: "Evaluation focuses on anomaly detection, not budget recommendation specifically."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "contextual"
      justification: "Uses anonymized CSMAR data but does not discuss privacy mechanisms."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "low"
      justification: "No user interaction or engagement analysis; purely technical detection."
    - code: "11.B"
      name: "Retention Mechanisms and Engagement Design"
      relevance: "low"
      justification: "No user retention or engagement design components."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "low"
      justification: "Does not address savings goals or management."
    - code: "13.B"
      name: "Debt Management in PFMS"
      relevance: "low"
      justification: "Does not address debt management."
    - code: "13.C"
      name: "End-of-Period Surplus as a Savings Input"
      relevance: "low"
      justification: "No savings or surplus concepts addressed."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "contextual"
      justification: "Uses Chinese data but does not analyze cultural financial practices."
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "contextual"
      justification: "Seasonal adjustment applied as preprocessing, not a primary finding."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "low"
      justification: "Not about expense categorization."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      relevance: "low"
      justification: "Not about category design."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "low"
      justification: "Not a survey of existing PFMS, focuses on detection technique."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "low"
      justification: "Critiques existing detection methods but not PFMS systems."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "low"
      justification: "No user behavioral profiling."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "contextual"
      justification: "Self-supervised learning can address cold-start but not profiling-focused."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "low"
      justification: "Not about behavioral classification."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "contextual"
      justification: "Uses prediction as a self-supervised auxiliary task, not primary focus."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "contextual"
      justification: "Uses LSTM for sequential data but forecasting is auxiliary."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "low"
      justification: "Not about budgeting strategies."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "low"
      justification: "No budget recommendation."
    - code: "7.C"
      name: "Constrained Optimization Approaches for Budget Allocation"
      relevance: "low"
      justification: "No allocation optimization."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "low"
      justification: "No mobile design or UX."
    - code: "9.B"
      name: "Mobile UX Design for Personal Finance"
      relevance: "low"
      justification: "No mobile UX."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "low"
      justification: "Does not address trust."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "low"
      justification: "Evaluation is for anomaly detection, not budget recommendation."
  contribution: "The HFSL framework provides a ready-to-adapt anomaly detection module for Odin's system evaluation layer, directly addressing the cold-start challenge through self-supervised learning without requiring labeled fraud data. Its multi-scale scoring mechanism (point, sequence, relationship) can enhance Odin's spending anomaly detection capabilities. The feature importance analysis (ROE/ROA as top indicators) informs which financial ratios to monitor in Filipino user data. The temporal evolution patterns (progressive, sudden, cyclical) offer guidance for designing Odin's alert escalation and early warning systems. The cross-industry calibration approach suggests that Odin should account for sector-specific spending patterns."
  directly_justifies:
    - "Self-supervised learning can detect anomalies with 0.820 F1 without requiring labeled fraudulent data."
    - "Multi-scale anomaly scoring (point, sequence, relationship) improves detection of complex financial manipulations."
    - "Feature interaction analysis shows that combining related indicators increases anomaly detection accuracy."
    - "Early detection rate of 0.726 enables proactive risk warning within two quarters of anomaly onset."
    - "Dual-channel LSTM architecture effectively captures both short-term and long-term temporal patterns."
  limits:
    - "Evaluation uses Chinese listed company data; applicability to individual Filipino spending data unvalidated [unacknowledged]."
    - "Self-supervised approach requires sufficient unlabeled normal data for training; cold-start with no data remains challenging [unacknowledged]."
    - "Model assumes quarterly reporting cycles; daily personal spending may have different temporal characteristics [unacknowledged]."
    - "Regulatory environment and fraud patterns differ substantially from personal finance misuse contexts [unacknowledged]."
  mapping_rationale: "Systematic scan of all 12 functional domains and 34 topic codes identified strong relevance primarily to Anomaly Detection (8.A, 8.B, 8.C) and Evaluation (12.A, 12.B). The paper directly addresses labeled data scarcity (8.C) through self-supervised learning, proposes a novel detection algorithm (8.B), and provides comprehensive multi-metric evaluation (12.A, 12.B). The Filipino Cultural Context domains (2.A, 2.B, 2.C, 2.D) were considered but rejected as the paper uses Chinese listed company data and does not analyze cultural financial practices or spending cycles—seasonal adjustment is purely preprocessing. Expense Categorization (3.A, 3.B, 3.C) was rejected as the paper categorizes financial ratios, not personal expenses. Forecasting (6.A, 6.B) was marked contextual since prediction appears as an auxiliary self-supervised task, not the primary contribution. Budget Recommendation (7.A-7.D) was rejected entirely as no budgeting or allocation is addressed. Behavioral Profiling (5.A-5.C) was rejected as no user profiling occurs. Mobile-First (9.A, 9.B) and Data Privacy (10.A, 10.B) were rejected as irrelevant. The paper is highly relevant as an algorithmic foundation for Odin's anomaly detection module but requires domain adaptation from corporate accounting to personal finance."
limitations:
  - "Tested only on Chinese listed company financial data; applicability to personal finance spending patterns remains unverified [unacknowledged]."
  - "Self-supervised approach requires sufficient unlabeled data for training; purely cold-start scenarios without transaction history are not addressed [unacknowledged]."
  - "Model complexity (1.8M parameters) and 18-hour training time may be impractical for lightweight PFMS deployment [unacknowledged]."
  - "Assumes quarterly reporting cycles; does not handle irregular or daily transaction data common in personal finance [unacknowledged]."
  - "Concept drift detection is reactive rather than preventive; adaptation lag during sudden regime changes could miss early fraud signals."
remember_this:
  - "HFSL achieves 0.820 F1 for anomaly detection using self-supervised learning without labeled data."
  - "Early detection rate of 0.726 enables proactive risk warnings within two quarters."
  - "ROE and ROA are the most important features for identifying financial anomalies."
  - "Five fraud patterns identified, with revenue inflation as the most common at 38.6%."
  - "Feature interaction analysis improves detection by 3.5% F1 when incorporated."
```
---

## Paper 30: Yachamaneni et al_summarized.md

**Source File:** `Yachamaneni et al_summarized.md`

```yaml
paper_id: 10.63282/3050-9262.IJAIDSML-V6I1P118
designation: international-algorithm-specific
title: Credit Card Customer Profiling Using Self-Supervised Representation Learning on Multi-Source Financial Data
authors: Yachamaneni, T.; Kotadiya, U.; Arora, A. S.
year: 2025
venue: International Journal of Artificial Intelligence, Data Science, and Machine Learning
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
tldr: Self-supervised learning on multi-source financial data creates robust customer representations that outperform supervised models in profiling, credit risk, and churn prediction.
problem_and_motivation: Traditional supervised customer profiling requires costly labeled data and fails to capture complex patterns from heterogeneous financial sources. The emergence of self-supervised learning enables label-efficient representation learning from unlabeled data, addressing privacy and scalability concerns.
approach:
  - Integrates transaction logs, demographics, credit bureau reports, and web activity from 100,000 records into a single model.
  - Uses separate encoders per modality, including temporal encoders for sequences and feedforward layers for static features.
  - Employs a transformer encoder with self-attention to capture temporal dependencies in sequential data.
  - Trains on pretext tasks: masked attribute forecasting, temporal order prediction, and augmented view prediction.
  - Applies contrastive learning to maximize similarity between augmented views and minimize similarity between different instances.
findings:
  - "num: The proposed SSL model achieved a Silhouette Score of 0.56, compared to 0.35 for K-Means and 0.41 for XGBoost."
  - "num: The model attained an AUC of 0.91 for credit risk prediction, versus 0.71 for K-Means and 0.84 for XGBoost."
  - "num: For churn prediction, the SSL model achieved an F1-score of 0.81, outperforming K-Means (0.58) and XGBoost (0.69)."
  - "num: Removing temporal encoding caused the largest performance drop of 4.2% in AUC, underscoring its importance."
  - "num: Web activity features contributed a 3.8% AUC drop when removed, while pretext tasks contributed a 2.7% drop."
key_figures_tables:
  - "Figure 1: Credit Card Fraud Detection System → conceptual framework for fraud scoring."
  - "Figure 2: Emergence of Self-Supervised Learning → SSL principles and benefits for financial data."
  - "Figure 3: Challenges in Traditional Approaches → data labeling, isolated sources, limited generalization."
  - "Figure 4: System Architecture → end-to-end pipeline from preprocessing to downstream tasks."
  - "Figure 5: Data Sources → transaction logs, demographics, credit reports, web activity."
  - "Figure 6: Feature Engineering → temporal encoding, normalization, categorical embeddings."
  - "Figure 7: Self-Supervised Learning Design → contrastive objective and pretext tasks."
  - "Figure 8: Model Architecture → transformer encoder, MLP head, clustering layer."
  - "Table 1: Quantitative Results → performance comparison across all methods and metrics."
  - "Table 2: Ablation Study Results → AUC drop from removing each module."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: SSL
    definition: Self-Supervised Learning - a paradigm that learns representations from unlabeled data using pretext tasks.
  - term: AUC
    definition: Area Under the Receiver Operating Characteristic Curve - a threshold-free measure of classification performance.
  - term: PFMS
    definition: Personal Finance Management System - a software application for managing personal finances.
  - term: K-Means
    definition: A clustering algorithm that partitions data into K distinct, non-overlapping subgroups.
  - term: XGBoost
    definition: Extreme Gradient Boosting - an optimized distributed gradient boosting library for supervised learning.
critical_citations:
  - "[Chen et al., 2020] — foundation for contrastive learning (SimCLR)."
  - "[Devlin et al., 2019] — BERT-style masked prediction pretext task inspiration."
  - "[MacQueen, 1967] — original K-Means algorithm used as baseline."
  - "[Chen & Guestrin, 2016] — XGBoost baseline implementation."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly proposes customer profiling using SSL to identify behavioral patterns from financial data.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: high
      justification: SSL addresses cold-start by learning representations from unlabeled data without requiring initial labels.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Compares SSL against supervised baselines (XGBoost) for classification of customer profiles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Demonstrates predictive modeling for credit risk and churn, relevant to Odin's forecasting needs.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: Uses temporal encoding and transformer architectures suitable for sequential spending data.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: The SSL framework can be adapted for anomaly detection through learned representations.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Provides a basis for anomaly detection via contrastive learning and reconstruction-based pretext tasks.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses standard evaluation metrics (Silhouette, AUC, F1) applicable to Odin's evaluation needs.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Conducts ablation studies to evaluate the contribution of each module, relevant to Odin's modular evaluation.
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: General customer profiling framework not specific to Filipino young professionals.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Reviews traditional and supervised approaches but does not survey PFMS specifically.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: contextual
      justification: Identifies general limitations of supervised learning but not specific to PFMS gaps.
  contribution: "The self-supervised learning framework provides a label-efficient approach for customer profiling that can be adapted for Odin's behavioral profiling module (5.A, 5.C). The multi-modal integration strategy informs Odin's data aggregation design across heterogeneous financial sources. The ablation study's emphasis on temporal encoding directly supports Odin's forecasting module (6.B) by showing the critical role of sequential patterns. The evaluation metrics (Silhouette, AUC, F1) provide a template for Odin's system evaluation framework (12.B). The demonstrated outperformance of SSL over supervised methods justifies Odin's adoption of self-supervised techniques for cold-start scenarios (5.B)."
  directly_justifies:
    - "Self-supervised learning can generate robust customer profiles from unlabeled financial data without manual annotation."
    - "Integrating temporal encoding significantly improves predictive performance for financial behavior modeling."
    - "Web activity logs provide valuable behavioral signals that enhance profiling accuracy beyond transactional data."
    - "Contrastive learning objectives yield more coherent and separable customer clusters than traditional clustering."
    - "The transformer architecture effectively captures long-range dependencies in sequential spending data."
  limits:
    - "Paper uses a proprietary dataset from a private banking company, limiting reproducibility."
    - "The study focuses on credit card customers, not general PFMS users, limiting direct applicability."
    - "Interpretability of SSL representations remains a challenge for regulated financial applications."
    - "No explicit handling of infeasibility or budget constraints, which are core to Odin's recommendation module."
    - "Evaluation does not include user satisfaction or engagement metrics, only algorithmic performance."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant for Behavioral Profiling & Classification (5.A, 5.B, 5.C) because it directly proposes a novel SSL-based customer profiling framework with empirical validation. It shows medium relevance for Spending Forecasting (6.A, 6.B) due to its temporal modeling components, and for Anomaly Detection (8.A, 8.B) through its representation learning approach suitable for outlier detection. System Evaluation (12.A, 12.B) was rated medium because it provides a comprehensive evaluation setup with ablation studies and standard metrics. Borderline cases included 2.B (Seasonal Patterns) and 2.D (Spending Cycles), which the paper does not explicitly address; these were rejected as purely contextual. The domains of Filipino Cultural Context, Expense Categorization, Budget Recommendation, Mobile-First Design, Data Privacy, User Retention, and Savings/Debt Management were considered and rejected as they are not addressed by the paper. Overall, the paper is highly relevant to Odin's core algorithmic modules for profiling and forecasting."
limitations:
  - "The dataset is from a single private bank, which may not generalize to the Philippine financial context."
  - "Interpretability of SSL-generated representations is not addressed, a key requirement for regulated PFMS."
  - "Does not address real-time deployment considerations or latency requirements for mobile-first applications."
  - "The paper does not discuss infeasibility handling or constrained optimization, central to Odin's budget recommendation."
  - "Privacy-preserving aspects of the SSL framework are not explored, despite multi-source data integration. [unacknowledged]"
remember_this:
  - "SSL achieved 0.91 AUC for credit risk, outperforming XGBoost's 0.84."
  - "Temporal encoding contributed the largest performance gain of 4.2%."
  - "Multi-source data integration significantly improves customer profiling quality."
  - "Contrastive learning produces more coherent and separable customer clusters."
  - "Self-supervised learning reduces dependence on costly labeled financial data."
```
---

## Paper 31: Japinye & Adedugbe_summarized.md

**Source File:** `Japinye & Adedugbe_summarized.md`

```yaml
paper_id: 10.5281/zenodo.17155174
designation: international-algorithm-specific
title: Explainable AI for Credit Scoring with SHAP-Calibrated Ensembles: A Multi-Market Evaluation on Public Lending Data
authors: Japinye, A. O.; Adedugbe, A. A.
year: 2025
venue: SSR Journal of Artificial Intelligence
odin_topics:
  - 4.A
  - 4.B
  - 5.C
  - 6.A
  - 8.A
  - 10.A
  - 12.A
  - 12.B
tldr: XGBoost with SHAP explanations, isotonic calibration, and fairness-constrained thresholding achieves high predictive accuracy, stable explanations, and significant bias reduction across diverse lending datasets.
problem_and_motivation: Machine learning credit scoring models improve accuracy but create opacity and fairness concerns. Existing systems lack integrated explainability, calibration, and fairness mechanisms for regulatory compliance. A unified framework is needed to balance predictive performance with transparency and equity.
approach:
  - Data: Three public lending datasets (Home Credit, Credit Card, LendingClub) with varying data-richness and default rates.
  - Method: XGBoost and LightGBM with TreeSHAP explanations, LIME for comparison, and isotonic regression for probability calibration.
  - Design: Integrated framework coupling SHAP/LIME, cost-aware threshold selection, and multi-criteria fairness monitoring.
  - Evaluation: Five-fold stratified cross-validation with borrower-level grouping and out-of-time validation for temporal splits.
  - Baselines: Logistic regression, decision tree, random forest, and neural network models were compared.
  - Fairness: Constrained threshold optimisation applied to demographic parity, equalised odds, and predictive parity.
findings:
  - num: XGBoost with SHAP achieved an AUC of 0.892±0.009 to 0.923±0.008 across datasets.
  - num: Isotonic calibration improved Brier scores significantly, with XGBoost achieving 0.119±0.003 to 0.154±0.004.
  - num: SHAP explanations demonstrated high stability with a mean Kendall τ of 0.930±0.033.
  - num: Fairness-constrained thresholding reduced demographic-parity gaps by 59-67% with cost increases of 3.2±0.8% to 5.8±1.3%.
  - num: Alternative data features provided 5.3× more predictive value in limited-bureau environments compared to data-rich settings.
  - num: XGBoost achieved a mean AUC advantage of +0.163 over logistic regression across all datasets.
  - num: Intersectional fairness analysis showed consistent bias reduction across gender and age combinations.
  - XAI-enhanced models scored substantially higher on regulatory compliance readiness for adverse action requirements.
  - Traditional credit features showed 3.2× greater importance in data-rich environments compared to limited-bureau settings.
  - Out-of-time validation showed modest performance degradation of 1-3% over 24-96 months.
key_figures_tables:
  - Table 2: Model AUC performance across datasets → XGBoost significantly outperforms all baselines.
  - Table 3: Calibration metrics after isotonic regression → XGBoost achieves superior Brier scores and calibration slopes.
  - Table 4: Explanation stability analysis → SHAP demonstrates high Kendall τ stability exceeding 0.90 threshold.
  - Table 5: Fairness constraint optimisation → Reduces demographic parity gaps by 59-67% at low cost.
  - Table 7: Feature family ablation analysis → Alternative signals provide most value in limited-bureau environments.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: XGBoost
    definition: Extreme Gradient Boosting, a scalable tree boosting system.
  - term: SHAP
    definition: SHapley Additive exPlanations, a game-theoretic approach to explaining model predictions.
  - term: LIME
    definition: Local Interpretable Model-agnostic Explanations, a perturbation-based explanation method.
  - term: AUC
    definition: Area Under the Receiver Operating Characteristic Curve.
  - term: ECE
    definition: Expected Calibration Error, a measure of probability calibration quality.
critical_citations:
  - "[Lundberg & Lee, 2017] — Foundational SHAP framework for model explanations."
  - "[Chen & Guestrin, 2016] — XGBoost algorithm for gradient boosting."
  - "[Hardt et al., 2016] — Fairness-constrained optimisation methodology."
  - "[Niculescu-Mizil & Caruana, 2005] — Isotonic regression for probability calibration."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Benchmarks machine learning credit scoring systems against traditional approaches.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies opacity, calibration, and fairness gaps in current scoring systems.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Evaluates classification performance of gradient boosting models for credit risk.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Demonstrates predictive modelling techniques applicable to spending and risk forecasting.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Framework could be adapted for anomaly detection in spending patterns.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Mentions data privacy considerations but not a primary focus.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Comprehensive evaluation methodology with AUC, calibration, fairness, and stability metrics.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Rigorous evaluation of explanation stability and fairness-constrained optimisation.
  contribution: This paper provides a methodological template for integrating explainability and fairness into predictive financial systems. It directly justifies the use of gradient-boosting models with SHAP explanations for Odin's core forecasting and anomaly detection modules. The fairness-constrained thresholding approach offers a practical technique for Odin's budget recommendation system to ensure equitable treatment. The comprehensive evaluation framework with calibration and stability metrics can be adopted for Odin's system evaluation and algorithmic module testing. The empirical finding on alternative data value in limited-bureau environments supports Odin's design for Filipino young professionals with varying financial histories.
  directly_justifies:
    - XGBoost with SHAP explanations maintains high predictive accuracy while providing stable local explanations.
    - Isotonic regression effectively calibrates gradient-boosting model probabilities for improved decision-making.
    - Fairness-constrained thresholding reduces demographic parity gaps by 59-67% with cost increases under 6%.
    - Alternative data signals provide substantial predictive value in environments with limited traditional credit data.
    - Explanation stability (Kendall τ = 0.93) enables reliable adverse action reasoning and regulatory compliance.
  limits:
    - Public datasets may not reflect operational lending complexity, including real-time data streams.
    - Cross-sectional design cannot assess explanation stability under model retraining cycles or economic regime changes.
    - Protected attribute availability varies significantly across datasets, limiting comprehensive fairness analysis.
    - Alternative data features may encode protected characteristics as proxies, requiring ongoing monitoring.
    - Fairness metrics may not capture all relevant equity dimensions, particularly for intersectional identities with small sample sizes.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. Domains flagged as relevant include Existing Systems & Gaps (4.A, 4.B - high/medium), Behavioral Profiling (5.C - medium), Spending Forecasting (6.A - medium), Anomaly Detection (8.A - contextual), Data Privacy (10.A - low), and System Evaluation (12.A, 12.B - high). The paper's primary relevance lies in its comprehensive evaluation framework, explanation stability methodology, and fairness-constrained optimisation, directly informing Odin's algorithmic evaluation and design considerations for equity. Borderline cases include the paper's applicability to Anomaly Detection (8.A) and Budget Recommendation (7.B), where the techniques are transferable but not directly demonstrated. Topics related to Filipino Cultural Context (2.A-D), Mobile-First Design (9.A-B), and Savings/Debt Management (13.A-C) were considered and rejected as the paper does not address these culturally or design-specific domains. Overall, the paper provides strong methodological and empirical justification for Odin's algorithmic choices, evaluation standards, and fairness implementation.
limitations:
  - Public datasets may not reflect operational lending complexity, including real-time data streams, adversarial behaviour, and regulatory constraints specific to individual institutions. [unacknowledged]
  - The cross-sectional design cannot assess explanation stability under model retraining cycles or economic regime changes. [unacknowledged]
  - Protected attribute availability varies significantly across datasets, limiting comprehensive fairness analysis.
  - Alternative data features may encode protected characteristics as proxies, requiring ongoing monitoring for disparate impact despite explicit fairness constraints.
  - Current fairness metrics may not capture all relevant equity dimensions, particularly for intersectional identities with small sample sizes.
remember_this:
  - XGBoost with SHAP achieved AUC of 0.892-0.923 across diverse credit datasets.
  - SHAP explanations demonstrated high stability with Kendall tau of 0.930.
  - Fairness constraints reduced demographic parity gaps by 59-67% with cost increases under 6%.
  - Alternative data provided 5.3 times more value in limited-bureau environments.
  - Integrated explainability and fairness frameworks enable regulatory compliance without sacrificing accuracy.
```
---

## Paper 32: Vijayanand & Smrithy_summarized.md

**Source File:** `Vijayanand & Smrithy_summarized.md`

```yaml
paper_id: 10.1177/18724981241289751
designation: international-algorithm-specific
title: Explainable AI - enhanced ensemble learning for financial fraud detection in mobile money transactions
authors: Vijayanand, D.; Smrithy, G.S.
year: 2025
venue: Intelligent Decision Technologies
odin_topics:
  - 4.B
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 12.B
tldr: Integrates ensemble machine learning with SHAP-based explainable AI to detect financial fraud in mobile money transactions, achieving 99.904% accuracy on a synthetic PaySim dataset.
problem_and_motivation: Financial fraud in digital banking is a growing threat, with global fraud losses reaching 5% of annual income. Existing machine learning models for fraud detection operate as black boxes, undermining trust and creating regulatory challenges. There is a need for systems that combine high accuracy with interpretability to foster transparency and accountability.
approach:
  - Uses PaySim simulator to generate 6,362,620 synthetic mobile money transaction records covering multiple transaction types.
  - Evaluates six classifiers: Logistic Regression, Decision Tree, Random Forest, XGBoost, LightGBM, and Neural Network.
  - Implements an ensemble Voting Classifier combining the six base models with soft voting to improve predictive performance.
  - Employs SHAP (SHapley Additive exPlanations) to provide global and local interpretability of model predictions.
  - Uses stratified 5-fold cross-validation and Friedman's statistical test with Nemenyi post-hoc for robust model comparison.
findings:
  - num: The ensemble learning model achieved 99.904% accuracy, 0.814 F1 score, and 0.990 ROC AUC score.
  - num: The Decision Tree model achieved the highest individual accuracy at 99.937% with an F1 score of 0.893.
  - num: Cash Out transactions comprised 81% of transaction types, while Transfer transactions comprised 19%.
  - num: OldBalanceOrg had the highest mean SHAP value of 0.065, indicating the strongest impact on model output.
  - num: The dataset contained 6,354,407 valid transactions (99.87%) and 8,213 fraudulent transactions (0.13%).
  - num: Fraudulent transactions were only found in the Transfer type, with flagged transactions totaling 16 all marked as TRANSFER.
key_figures_tables:
  - Figure 1: Architecture of proposed methodology → High-level system design for fraud detection with XAI integration.
  - Figure 2: Pie chart of transaction types → Cash Out (81%) and Transfer (19%) dominate transaction categories.
  - Figure 3: Total amount per transaction type → Transfer transactions have higher total monetary value than Cash Out.
  - Figure 4: Fraudulent transaction types by category → Transfer transactions show higher fraud frequency than Cash Out.
  - Figure 5: Proposed ensemble model → Voting Classifier combining XGBoost, LightGBM, Neural Network, Decision Tree, and Random Forest.
  - Figure 6: Process of Explainable AI → XAI pipeline from input data through model prediction to explanation interface.
  - Figure 7: Mean SHAP value bar chart → OldBalanceOrg has the highest average impact (0.065) on model output.
  - Figure 8: SHAP value and feature value scatter plot → Visualizes relationship between feature values and their SHAP impacts.
  - Table 1: Comparative analysis of research works → Summary of prior ML and DL studies on financial fraud detection.
  - Table 2: Dataset attributes → Description of 11 features including step, type, amount, and balance fields.
  - Table 3: Cross-validation results on accuracy → Accuracy per fold for all six base models.
  - Table 4: Cross-validation results on F1 scores → F1 per fold for all six base models.
  - Table 5: Cross-validation results on ROC AUC scores → ROC AUC per fold for all six base models.
  - Table 6: Performance metrics of classification models → Summary table of accuracy, F1, and ROC AUC for each model.
  - Table 7: Nemenyi Post-Hoc Test Results → Pairwise comparison p-values indicating statistically significant performance differences.
  - Table 8: Cross-validation results of ensemble learning classifier → Accuracy, F1, and ROC AUC across 5 folds.
  - Table 9: Performance measure of ensemble learning classifier → Final metrics: 99.904% accuracy, 0.814 F1, 0.990 ROC AUC.
  - Table 10: Average impact of attributes on model output → Mean SHAP values for key features.
key_equations:
  - equation: S(x) = 1 ÷ (1 + e^(-x))
    explanation: Sigmoid function used by logistic regression for probability estimation.
definitions:
  - term: SHAP
    definition: SHapley Additive exPlanations, a game-theoretic approach to explain model predictions by attributing feature importance.
  - term: XAI
    definition: Explainable Artificial Intelligence, AI systems designed to be transparent and interpretable to users.
  - term: Ensemble Learning
    definition: Combining multiple machine learning models to improve predictive performance beyond any single model.
  - term: PaySim
    definition: A financial mobile money simulator that generates synthetic transaction data for fraud detection research.
  - term: Voting Classifier
    definition: An ensemble method that combines predictions from multiple classifiers using majority or soft voting.
  - term: LightGBM
    definition: A gradient boosting framework using tree-based learning with histogram-based methods for efficient training.
critical_citations:
  - "[Hall & Gill, 2019] — Foundational work on machine learning interpretability and transparency."
  - "[Lopez-Rojas et al., 2016] — Introduced the PaySim dataset used in this study."
  - "[Ali et al., 2022] — Systematic literature review of ML techniques for financial fraud detection."
  - "[Awosika et al., 2023] — Combined XAI and federated learning for transparent fraud detection."
  - "[Al-Hashedi & Magalingam, 2021] — Comprehensive review of data mining for financial fraud from 2009-2019."
relevance:
  topics:
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies lack of interpretability in black-box fraud detection models as a critical gap.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly addresses anomaly detection for fraudulent transactions in financial systems.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Uses ensemble learning and XAI to detect fraud patterns in transaction data.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Fraud detection protects financial security, though privacy is not the primary focus.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: XAI via SHAP enhances transparency, which fosters user trust in financial systems.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Provides rigorous cross-validation and statistical testing of ML models for fraud detection.
  contribution: The paper's ensemble learning approach with SHAP explainability directly informs Odin's anomaly detection module (Topic 8.A) by providing a high-accuracy fraud detection framework with interpretable outputs. The Voting Classifier methodology offers a template for combining multiple anomaly detection algorithms to improve robustness in Odin's spending pattern analysis. The SHAP-based feature importance analysis provides a precedent for making Odin's anomaly alerts transparent to users, supporting the trust-building goal in Topic 10.B. The cross-validation and statistical testing framework offers a rigorous evaluation methodology for Odin's algorithmic modules in Topic 12.B.
  directly_justifies:
    - Ensemble learning achieves 99.904% accuracy for fraud detection on mobile money transaction data.
    - SHAP analysis reveals OldBalanceOrg as the most influential attribute for detecting fraudulent transactions.
    - Interpretability through XAI is essential for regulatory compliance and user trust in financial systems.
    - Decision Tree models achieve higher individual F1 scores than ensemble methods on imbalanced fraud data.
  limits:
    - Uses synthetic PaySim data, which may not fully represent real-world fraud patterns.
    - Dataset is highly imbalanced (0.13% fraud), potentially overestimating model performance on balanced data. [unacknowledged]
    - Limited to mobile money transactions; applicability to broader personal finance contexts is unclear. [unacknowledged]
  mapping_rationale: I systematically scanned all 12 functional domains and their associated topic codes from the Canonical Odin Topic List. Domains flagged as relevant include Anomaly Detection (8.A and 8.B with high relevance), Existing Systems & Gaps (4.B with medium relevance), Data Privacy & User Trust (10.A with medium and 10.B with medium relevance), and System Evaluation (12.B with medium relevance). Borderline cases included Behavioral Profiling (5.A-5.C) — while fraud detection involves behavioral patterns, the paper focuses on transaction-level anomaly detection rather than user profiling, so it was rejected. Mobile-First Design (9.A-9.B) was considered but rejected as the paper does not address mobile UX. Forecasting (6.A-6.B) and Budget Recommendation (7.A-7.D) were rejected as the paper does not address predictive spending or budgeting. Expense Categorization (3.A-3.C) and Filipino Cultural Context (2.A-2.D) were deemed irrelevant. The paper's overall relevance to Odin is strong for its anomaly detection methodology and XAI approach, providing a validated framework for detecting unusual spending patterns with interpretable outputs.
limitations:
  - Uses synthetic PaySim data rather than real financial transaction data, limiting real-world validation.
  - The highly imbalanced dataset (0.13% fraud) may overestimate model performance on balanced real-world data. [unacknowledged]
  - The study does not address cold-start scenarios or model adaptation to new fraud patterns over time. [unacknowledged]
  - Limited discussion of computational cost or deployment constraints for real-time mobile applications. [unacknowledged]
remember_this:
  - Ensemble Voting Classifier achieved 99.904% fraud detection accuracy.
  - SHAP analysis identified OldBalanceOrg as the most influential fraud indicator.
  - Interpretable AI models are essential for user trust and regulatory compliance.
  - PaySim synthetic dataset contained 0.13% fraudulent transactions among 6.36 million records.
  - Decision Tree outperformed individual models with 99.937% accuracy.
```
---

## Paper 33: Schipper_summarized.md

**Source File:** `Schipper_summarized.md`

```yaml
paper_id: 10.47852/bonviewFSI52025696
designation: local
title: Navigating Innovation, Inclusion, and Ethical Challenges in AI-Driven Fintech: The Philippines
authors: Schipper, T.
year: 2025
venue: FinTech and Sustainable Innovation
odin_topics:
  - 1.A
  - 1.B
  - 2.A
  - 2.D
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 13.B
tldr: AI-driven social fintech in the Philippines expands financial access via mobile-first platforms and alternative credit scoring but introduces critical ethical risks requiring stronger regulation and consumer protection.
problem_and_motivation: Fintech adoption in the Philippines rapidly increases financial inclusion but creates new ethical risks due to low financial literacy, data privacy gaps, and uneven consumer protections. The balance between innovation-driven access and responsible AI integration remains poorly understood in low-capacity digital environments.
approach:
  - A qualitative multiple case study methodology using desk research and purposive sampling of nine Philippine fintech companies.
  - Reviewed industry reports, regulatory documents, and firm-level data across digital banking, lending, and payments sectors.
  - Companies selected based on declared commitment to financial inclusion and demonstrated use of AI or digital innovations.
  - Data sources included company websites, regulatory filings, policy documents, and academic literature.
  - Analyzed common trends, strategies, and obstacles in advancing inclusive finance with emphasis on technological, ethical, and legal dimensions.
findings:
  - AI-enabled mobile-first platforms allow rapid expansion into underserved areas without conventional banking infrastructure.
  - Alternative credit scoring using mobile data and behavioral analytics expands credit access to unbanked populations.
  - High-interest lending (e.g., Tonik up to 7% monthly) targets vulnerable users, blurring inclusion and exploitative debt.
  - Data privacy violations (e.g., JuanHand improper data collection) highlight gaps in informed consent and regulatory enforcement.
  - num: GCash has 81 million active users and 2.5 million merchants, reflecting deep market penetration.
  - num: Cybersecurity incidents caused P76.49 million in consumer fraud losses in 2024.
  - Ownbank circumvented digital banking moratorium by acquiring a rural bank, exposing regulatory gaps.
  - Plastic Bank uses blockchain and AI to incentivize waste collection, integrating financial inclusion with environmental sustainability.
  - Cropital's AI credit scoring for farmers uses farm productivity and behavioral data but faces default risks from climate hazards.
  - Digital literacy gaps persist, with Filipino borrowers readily sharing personal data without understanding implications.
key_figures_tables:
  - Figure 1: ATMs per 100,000 adults in the Philippines (2011-2021) → Slow physical infrastructure growth compared to regional peers.
  - Figure 2: Account ownership (15+ years) in the Philippines (2011-2021) → Rapid growth from 27% to 53% driven by fintech and mobile money.
  - Table 1: Traditional Fintech vs. Social Fintech comparison → Social fintech prioritizes inclusion and community-oriented solutions.
  - Table 2: AI applications in Philippine financial services → Examples include credit scoring, biometric verification, and anomaly detection.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Social Fintech
    definition: Application of digital financial innovations to advance financial inclusion and meet marginalized populations' needs.
  - term: FATE
    definition: Acronym for Fairness, Accountability, Transparency, and Ethics in AI systems.
  - term: XAI
    definition: Explainable Artificial Intelligence, ensuring user consent and data privacy.
  - term: ESG
    definition: Environmental, Social, and Governance factors for socially responsible investment decisions.
  - term: P2P Lending
    definition: Peer-to-peer lending platform connecting individual lenders and borrowers without traditional financial intermediaries.
critical_citations:
  - "[Russell & Norvig, 2021] — Defines AI as agents perceiving and acting upon their environment."
  - "[Bahoo et al., 2024] — AI making financial services faster and more inclusive."
  - "[ADB, 2022] — Highlights regulatory compliance challenges for fintech in ASEAN."
  - "[Quimba et al., 2021] — Analyzes profitability obstacles for Philippine fintech companies."
  - "[Aldboush & Ferdous, 2023] — Emphasizes responsible innovation and consumer data protection."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Focuses on Filipino fintech adoption and digital engagement trends relevant to this demographic.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Discusses financial inclusion metrics and account ownership trends in the Philippines.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Examines social fintech practices including blockchain-based waste-to-cash and P2P lending.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: References seasonal and occasion-based financial needs though not the primary focus.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Maps the Philippine fintech ecosystem including digital banks, lending apps, and payments.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies gaps in infrastructure, literacy, privacy, and consumer protection.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: AI-driven behavior analysis and alternative credit scoring as profiling examples.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Discusses AI classification for creditworthiness based on behavioral indicators.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: high
      justification: All case studies use mobile-first platforms to reach underserved populations.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Mobile app interfaces and user experiences in GCash, Tonik, and Tala.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Detailed discussion of data privacy violations and cybersecurity threats.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Trust-building mechanisms and risks of algorithm opacity.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: User engagement through personalized financial insights and recommendations.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: Financial literacy programs and user retention strategies discussed.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: High-interest lending, non-performing loans, and debt cycles explicitly addressed.
  contribution: This paper justifies Odin's need for robust data privacy and security modules by documenting widespread privacy violations in Philippine fintech. It informs Odin's behavioral profiling approach by showing how AI credit scoring uses alternative data for financial inclusion. The findings on high-interest lending and debt cycles directly support Odin's debt management features and user protection mechanisms. The case for mobile-first, culturally contextualized design is reinforced by examples of successful fintech adoption across diverse Filipino communities.
  directly_justifies:
    - "AI-driven financial inclusion must be balanced with robust consumer protection to prevent exploitative lending."
    - "Algorithmic transparency is essential to build and maintain user trust in AI-powered financial systems."
    - "Data privacy violations occur when fintech apps collect excessive personal data without informed consent."
    - "Digital literacy gaps lead users to share sensitive data without understanding the implications."
    - "Regulatory sandboxes can safely test fintech innovations while ensuring compliance and consumer safety."
  limits:
    - "Lacks longitudinal data to track long-term socioeconomic impacts of fintech initiatives."
    - "No empirical assessment of the 'social investment life-course multiplier' effect across age or income groups."
    - "Focuses primarily on Philippines, limiting generalizability to other Global South contexts."
    - "Does not include direct user surveys, relying on desk research and secondary data sources."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was conducted. The paper was flagged as highly relevant for Filipino Cultural Context (2.A), Existing Systems & Gaps (4.A, 4.B), Behavioral Profiling (5.A), Mobile-First Design (9.A), Data Privacy (10.A, 10.B), and Debt Management (13.B) due to its detailed case studies and ethical risk analysis. Medium relevance was assigned to Financial Structure (1.B), Classification Approaches (5.C), Mobile UX (9.B), Engagement Dynamics (11.A, 11.B), and Retention Mechanisms (11.B). Low relevance was assigned to Spending Forecasting (6.A, 6.B) and Algorithmic-specific topics (8.A, 8.B, 8.C) as the paper does not focus on predictive models. Contextual relevance was assigned to Seasonal Spending (2.D). Topics rejected included Budget Recommendation (7.A–D), Optimization (7.C, 7.D), Evaluation Frameworks (12.A–C), and Savings Goals (13.A, 13.C) as the paper does not address these technical or evaluation topics. The overall relevance to Odin is high, providing critical justification for data privacy, debt management, and mobile-first design modules while highlighting regulatory gaps that Odin's design should address.
limitations:
  - "Lacks longitudinal data to track long-term socioeconomic impacts of fintech initiatives. [unacknowledged]"
  - "No empirical assessment of the 'social investment life-course multiplier' effect. [unacknowledged]"
  - "Focuses primarily on Philippines, limiting generalizability to other Global South contexts. [unacknowledged]"
  - "Does not include direct user surveys, relying on desk research and secondary data sources."
  - "Does not evaluate the long-term socioeconomic effects of fintech initiatives in the Philippines. [unacknowledged]"
remember_this:
  - "AI-driven fintech expands financial access but introduces ethical risks in low-literacy environments."
  - "GCash's 81 million users demonstrate fintech's potential for rapid adoption in the Philippines."
  - "High-interest lending can blur the line between inclusion and exploitation of vulnerable users."
  - "Algorithmic opacity undermines trust and accountability in AI-powered credit scoring."
  - "Regulatory gaps enable circumvention of digital banking restrictions through rural bank acquisitions."
```
---

## Paper 34: Danach et al_summarized.md

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

## Paper 35: Simeonov et al_summarized.md

**Source File:** `Simeonov et al_summarized.md`

```yaml
paper_id: 10.1038/s41598-025-14364-7
designation: international-algorithm-specific
title: Analysing community-level spending behaviour contributing to high carbon emissions using stochastic block models
authors: Simeonov, O.; Restocchi, V.; Goddard, B. D.
year: 2025
venue: Scientific Reports
odin_topics:
  - 5.A
  - 5.C
  - 12.B
  - 12.A
  - 13.A
  - 7.A
  - 4.A
tldr: Stochastic block models on bipartite spending networks identify consumer communities with similar spending and emission patterns, enabling targeted sustainability interventions.
problem_and_motivation: Designing effective group-level carbon reduction interventions requires understanding consumer spending patterns across categories. Existing studies often focus on single purchase types or rely on self-reported data, and there is a gap in scalable methods to identify large consumer groups with shared emission profiles from transaction data.
approach:
  - Constructs a bipartite network connecting customers to Merchant Category Codes (MCCs) based on transaction history.
  - Applies a degree-corrected nonparametric hierarchical Stochastic Block Model (SBM) for community detection.
  - Introduces a weighted SBM variant that normalizes spending amounts by category averages to keep average community spending constant.
  - Runs the SBM algorithm 100 times and selects the partition with the highest posterior probability for stable community detection.
  - Validates the approach on an artificial dataset of one million transactions to test scalability.
findings:
  - num: The weighted SBM approach results in 71 out of 80 cluster-category spending percentages falling within one Median Absolute Deviation of the population median.
  - num: Unweighted SBM had fewer than half of clusters within one MAD, compared to over 88% for weighted SBM.
  - Communities identified by the SBM exhibit homogeneous spending patterns and distinct carbon emission profiles across merchant categories.
  - Weighted SBM creates customer groups with consistent spending proportions across categories, enabling ceteris paribus analysis of external factors.
  - The SBM method is scalable, with analysis of datasets with less than one million transactions completing in seconds.
key_figures_tables:
  - Figure 4: Heatmap of carbon emissions per MCC across clusters → Reveals dominant emission categories (e.g., groceries, taxis, service stations) for each consumer community.
  - Figure 5: Heatmap of weighted SBM spending percentages → Shows cluster spending aligns with population averages within one MAD.
  - Figure 7: Cluster emissions and spending for Taxicabs category → Identifies clusters 17 and 18 as targets for transaction-count versus amount-based interventions.
  - Table in Appendix: Age and IMD distribution → Customer base is predominantly younger and from more deprived areas.
  - Figure 9: Logistic regression for client retention → Younger and more deprived customers have higher dropout probability.
key_equations:
  - equation: MAD = median(|X_i - median(X)|)
    explanation: Median Absolute Deviation used to measure spending consistency across clusters.
definitions:
  - term: SBM
    definition: Stochastic Block Model, a probabilistic model for detecting community structures in networks.
  - term: MCC
    definition: Merchant Category Code, a four-digit code used by card providers to classify transactions.
  - term: MAD
    definition: Median Absolute Deviation, a robust measure of statistical dispersion.
  - term: IMD
    definition: Index of Multiple Deprivation, a UK measure of relative deprivation for small areas.
  - term: LCFS
    definition: Living Costs and Food Survey, a UK household expenditure survey.
critical_citations:
  - "[Trendl et al., 2023] — Provides the carbon multipliers used to estimate emissions from transactions."
  - "[Wells et al., 2025] — Demonstrates segmentation of households by carbon footprint using transaction data."
  - "[Di Clemente et al., 2018] — Shows that purchase sequences follow a Zipf-like distribution and can cluster consumers."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Core contribution is identifying consumer communities with similar spending and emission profiles.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Directly proposes and validates SBM as a classification method for spending behaviour.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Presents a quantitative evaluation of SBM performance and compares weighted vs. unweighted variants.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides a methodology for evaluating clustering results and their implication for targeted interventions.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: contextual
      justification: Mentions targeted interventions could encourage sustainable spending, indirectly relevant to savings.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: Discusses using cluster insights for behavioural nudges, a budgeting-related strategy.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews existing segmentation methods (k-means, MST-kNN) and positions SBM as an alternative.
  contribution: The paper provides a validated SBM-based methodology for identifying consumer communities with similar spending and carbon emission patterns. This methodology can be adapted for Odin's behavioral profiling module to group Filipino users for targeted financial recommendations. The weighted SBM variant offers a way to control for spending levels, allowing for cleaner analysis of how other factors influence emission or spending behavior. The hierarchical nature of the SBM supports analysis at different levels of granularity, which is useful for Odin's cold-start problem. The paper's emphasis on using only transaction data aligns with Odin's mobile-first design, avoiding reliance on demographic data that may not be available.
  directly_justifies:
    - "Stochastic block models effectively identify communities of consumers with homogeneous spending patterns."
    - "Weighted SBM can create consumer groups with consistent spending proportions across categories."
    - "Targeting clusters rather than individuals allows scalable implementation of behavioural interventions."
    - "SBM mitigates bias by clustering based on network properties, not socio-demographic attributes."
  limits:
    - "The SBM is static and does not account for time-varying data or evolving consumer behaviour."
    - "The model can be computationally expensive with large datasets."
    - "The probabilistic framework can make interpretation more difficult for non-technical audiences."
    - "The analysis relies on a sustainability-oriented subsample, limiting representativeness."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant for domains related to behavioral profiling and classification (5.A, 5.C) and system evaluation (12.B), as its core contribution is a novel classification method (SBM) and its quantitative evaluation. It also provided medium relevance for the existing systems landscape (4.A) by reviewing prior segmentation methods, and for evaluation frameworks (12.A) by outlining a validation process. The topics of savings (13.A) and budgeting strategies (7.A) were considered contextual, as the paper discusses behavioural interventions but does not directly address savings goals or budget allocation algorithms. Domains like expense categorization (3.A, 3.B), anomaly detection (8.A, 8.B), data privacy (10.A, 10.B), and engagement (11.A, 11.B) were considered and rejected because the paper does not provide actionable claims for these specific Odin modules. The overall relevance is high for algorithmic and methodological aspects of user profiling, with moderate relevance for framing the problem and evaluation.
limitations:
  - "Financial transaction data is often constrained by privacy and commercial restrictions, limiting dataset representativeness."
  - "The dataset reflects a sustainability-oriented subsample, limiting generalisability to the broader population."
  - "Carbon footprint estimates assume uniform carbon intensity within merchant categories, masking product-level variations."
  - "Utility payments and cash expenditures are often missing from transaction data."
  - "The SBM is static and does not account for evolving consumer behaviour over time. [unacknowledged]"
remember_this:
  - "Stochastic block models effectively identify consumer communities with similar spending patterns."
  - "Weighted SBM creates clusters with spending aligned to population averages within one Median Absolute Deviation."
  - "Targeting consumer groups enables scalable implementation of financial and sustainability interventions."
  - "SBM mitigates bias by clustering solely on transaction patterns, not socio-demographic attributes."
  - "The paper demonstrates a 31% improvement in cluster spending consistency using weighted SBM."
```
---

## Paper 36: Li & Gautam_summarized.md

**Source File:** `Li & Gautam_summarized.md`

```yaml
paper_id: "10.1145/3787120.3787130"
designation: "international-algorithm-specific"
title: "Segmented Confidence Sequences and Multi-Scale Adaptive Confidence Segments for Anomaly Detection in Nonstationary Time Series"
authors: "Li, M.; Gautam, A."
year: 2025
venue: "2025 5th International Conference on Artificial Intelligence and Application Technologies (AIAT2025)"
odin_topics:
  - "8.A"
  - "8.B"
  - "8.C"
  - "12.B"
tldr: "Presents two adaptive thresholding frameworks, Segmented Confidence Sequences and Multi-Scale Adaptive Confidence Segments, that improve anomaly detection in nonstationary time series by localizing statistical estimation and multi-scale attention, significantly outperforming static percentile baselines."
problem_and_motivation: "Traditional static thresholds fail under regime shifts and concept drift in nonstationary time series. Existing adaptive methods often struggle with multiple temporal scales or sudden changes. There is a need for statistically principled, unsupervised thresholds that adapt locally and maintain false alarm guarantees."
approach:
  - "Uses autoencoder reconstruction errors as anomaly scores on six public benchmark datasets with ground-truth labels."
  - "Segmented Confidence Sequences (SCS) partitions time series into locally stationary segments using APCA or K-means, then maintains Hoeffding-style confidence bounds per segment."
  - "Multi-Scale Adaptive Confidence Segments (MACS) maintains three rolling windows (short, medium, long) with independent confidence sequences and an attention mechanism that weights scales by local variance."
  - "MACS also performs regime change detection using CUSUM-like statistics and applies dual detection (threshold violation and attention-weighted bounds) during regime shifts."
  - "Both methods apply a global percentile filter as a conservative post-processing step."
  - "Compares against a fixed 99th percentile threshold baseline and evaluates F1-score, precision, recall, and accuracy."
findings:
  - "num: On Wafer Manufacturing, MACS increases F1-score by 2.17 points and recall by 3.99 compared to static percentile at alpha=0.99."
  - "num: At alpha=0.95, SCS APCA improves F1-score by 2.13 and recall by 6.16 on the same dataset."
  - "Both SCS and MACS outperform rolling quantile methods, particularly on datasets with pronounced regime shifts."
  - "The trade-off is higher recall at the cost of moderate precision loss."
  - "num: Across six datasets, SCS and MACS show positive F1-score deltas, with the largest gains on Wafer, GCP, MSL, and SMD."
key_figures_tables:
  - "Figure 3: F1-score comparison on Wafer dataset at alpha=0.99 → SCS and MACS outperform baseline significantly."
  - "Table 2: Cross-dataset F1-score delta vs. baseline → MACS and SCS show positive deltas across all six datasets."
  - "Table 3: Performance delta on Wafer Manufacturing → MACS achieves the highest F1 improvement."
key_equations:
  - equation: "lower_bound = \\bar{x} - bound\\_width"
    explanation: "Confidence interval lower bound based on local mean."
  - equation: "upper_bound = \\bar{x} + bound\\_width"
    explanation: "Confidence interval upper bound."
  - equation: "combined\\_bound = \\sum weight_i \\cdot bound_i"
    explanation: "Weighted sum of multi-scale bounds."
definitions:
  - term: "SCS"
    definition: "Segmented Confidence Sequences: adaptive thresholding by segmenting time series."
  - term: "MACS"
    definition: "Multi-Scale Adaptive Confidence Segments: multi-scale adaptive thresholding."
  - term: "APCA"
    definition: "Adaptive Piecewise Constant Approximation: segmentation method."
  - term: "Confidence sequence"
    definition: "Time-uniform interval guaranteeing coverage."
critical_citations:
  - "[Howard et al., 2021] — Provides foundation for confidence sequences."
  - "[Blázquez-García et al., 2021] — Reviews anomaly detection in time series."
relevance:
  topics:
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Directly proposes adaptive thresholding algorithms for anomaly detection in time series, applicable to PFMS."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Introduces SCS and MACS as novel algorithms for detecting anomalies."
    - code: "8.C"
      name: "Cold-Start Baseline Strategies for Anomaly Detection"
      relevance: "medium"
      justification: "Discusses static percentile baseline and adaptive methods that could inform cold-start strategies."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Provides comprehensive evaluation on benchmark datasets with metrics including F1, precision, recall."
  contribution: "The adaptive thresholding frameworks can be integrated into Odin's anomaly detection module to identify irregular spending patterns. The multi-scale attention mechanism of MACS can help detect both sudden spikes and gradual changes in user spending. The segmentation approach of SCS provides interpretable regime-specific thresholds, aiding in behavioral analysis. The evaluation methodology offers a template for assessing Odin's anomaly detection performance."
  directly_justifies:
    - "Adaptive thresholding improves recall over static methods in nonstationary data."
    - "Multi-scale analysis captures anomalies at different temporal resolutions."
    - "Confidence sequences provide statistical guarantees on false alarm rates."
    - "Unsupervised methods reduce reliance on labeled anomaly data."
  limits:
    - "Not validated on personal finance data."
    - "Requires tuning of confidence level and segmentation parameters."
  mapping_rationale: "I systematically scanned all 12 functional domains. Only domains related to anomaly detection and algorithmic evaluation were found relevant. The paper directly addresses anomaly detection (8.A and 8.B) with novel adaptive algorithms and provides evaluation (12.B). The cold-start topic (8.C) is tangentially related via baseline comparison. Other domains—cultural context, expense categorization, existing systems, behavioral profiling, forecasting, budget recommendation, mobile design, privacy, engagement, savings/debt—were rejected as the paper does not address financial specifics or PFMS design. Overall, the paper offers strong algorithmic contributions for Odin's anomaly detection module."
limitations:
  - "Performance depends on segmentation quality and may degrade on highly noisy data."
  - "Requires tuning of confidence levels and attention weights."
  - "Does not address computational efficiency for mobile deployment [unacknowledged]."
  - "Not tested on personal finance data [unacknowledged]."
remember_this:
  - "MACS improves F1 by up to 2.17 points over static percentile on Wafer dataset."
  - "SCS and MACS boost recall significantly with moderate precision loss."
  - "Confidence sequences provide statistical false alarm guarantees."
  - "Adaptive thresholds adapt to regime shifts and multi-scale changes."
```
---

## Paper 37: Lee C. et al_summarized.md

**Source File:** `Lee C. et al_summarized.md`

```yaml
paper_id: 10.1145/3706598.3714113
designation: international-algorithm-specific
title: VeriPlan: Integrating Formal Verification and LLMs into End-User Planning
authors: Lee, C. P.; Porfirio, D.; Wang, X. J.; Zhao, K. C.; Mutlu, B.
year: 2025
venue: CHI Conference on Human Factors in Computing Systems
odin_topics:
  - 4.A
  - 4.B
  - 5.A
  - 6.A
  - 7.A
  - 7.C
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 12.A
  - 12.B
tldr: Formal verification via model checking improves LLM reliability and user satisfaction in end-user planning by enforcing user-defined temporal constraints through a rule translator, flexibility sliders, and iterative feedback.
problem_and_motivation: Everyday users lack effective tools for complex planning tasks. LLMs show promise but produce unreliable outputs that violate user constraints, undermining trust and usability. A system is needed to verify LLM-generated plans against user-defined rules while keeping users in the loop.
approach:
  - VeriPlan combines an LLM planner with a rule translator that converts natural language constraints into Linear Temporal Logic (LTL) properties using a six-category template.
  - Flexibility sliders allow users to adjust constraint strictness, enabling soft and hard constraints to guide verification.
  - A model checker (PRISM/Stormpy) verifies LLM-generated plans against LTL properties and provides feedback on violations.
  - Users review and confirm translated rules, then iteratively refine plans through up to three verification cycles based on model checker feedback.
  - A user study with 12 participants across three planning scenarios evaluated four conditions: full system, without sliders, without translator, and without verification.
findings:
  - num: Full VeriPlan significantly outperformed no-translator and no-verification conditions in perceived performance (p=.0011 and p=.0013).
  - num: Usefulness scores were significantly higher for full system vs. no-slider (p=.047), no-translator (p=.009), and no-verification (p=.0257) conditions.
  - num: Satisfaction was significantly higher for full system vs. no-translator (p=.007) and no-verification (p=.0101) conditions.
  - Rule verification helped align user expectations, refine prompts, and provided deterministic boundaries that improved LLM accuracy.
  - Flexibility sliders enabled adaptive personalization but users found the impact of strictness percentages ambiguous.
  - Model checker feedback improved efficiency, transparency, and enabled creative exploration by acting as a safety net.
  - The mind-map interface supported understanding, feedback application, and plan organization based on user preferences.
key_figures_tables:
  - Figure 1: Comparison of LLM interaction without VeriPlan (left) and with VeriPlan (right) → VeriPlan adds rule extraction, verification, and iterative refinement.
  - Figure 6: Bar graphs of perceived performance, usefulness, ease, and satisfaction across conditions → Full system consistently outperforms ablated versions.
key_equations:
  - equation: G (¬ brownMeatballs U mixingMeatballIngredients)
    explanation: LTL formula for strict sequential order constraint.
  - equation: G (F cookingDinner → F homeworkAssistance ∧ F dogWalking ∧ F eveningCleanup)
    explanation: LTL formula for concurrent events after a precondition.
  - equation: ¬ ( ((P3_waitingRoom ∧ P2_waitingRoom) ∨ (P3_waitingRoom ∧ P4_waitingRoom)) ∧ ¬ (P3_waitingRoom ∧ P1_waitingRoom) ) U (P3_waitingRoom ∧ P2_waitingRoom ∧ P4_waitingRoom ∧ P1_waitingRoom)
    explanation: LTL formula for exclusive constraints preventing pair conflicts.
definitions:
  - term: LTL
    definition: Linear Temporal Logic; a formal logic for expressing temporal properties over sequences of states.
  - term: Model Checking
    definition: A formal verification technique that exhaustively checks if a system model satisfies specified properties.
  - term: PRISM
    definition: A probabilistic model checker used to verify systems against temporal logic properties.
  - term: Stormpy
    definition: Python API for the Storm model checker, enabling programmatic verification.
  - term: Hallucination
    definition: LLM-generated text that is coherent but factually incorrect or nonsensical.
  - term: Flexibility Sliders
    definition: User interface controls to adjust strictness of constraints from soft to hard.
critical_citations:
  - "[Kambhampati et al., 2024] — Position paper on LLM-Modulo frameworks for planning."
  - "[Valmeekam et al., 2023] — Critical evaluation of LLM planning abilities showing 12% success rate for GPT-4."
  - "[Achiam et al., 2023] — GPT-4 technical report; powers VeriPlan's LLM agents."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides background on automated planning tools and accessibility barriers.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies LLM limitations in planning accuracy, consistency, and user trust.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: low
      justification: General user preference specification relevant but not finance-specific.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: contextual
      justification: Verification approach could be applied to forecasting models indirectly.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Rule-based constraints and flexibility mapping parallel budget allocation constraints.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: medium
      justification: Model checking enforces constraints analogous to budget optimization.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: contextual
      justification: Interface design implications are generalizable to mobile contexts.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: UX insights on mind-map layouts and feedback could inform mobile PFMS design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Verification improves reliability but privacy not directly addressed.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Directly shows verification improves user trust, satisfaction, and perceived reliability.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Iterative refinement and user control features enhance engagement.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: User control and transparency features support retention through improved experience.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a structured ablation study methodology applicable to PFMS evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Directly evaluates algorithmic modules (rule translator, model checker) via user study.
  contribution: "VeriPlan demonstrates that integrating formal verification (model checking) with LLMs enhances planning reliability and user satisfaction. The rule translator lowers barriers by converting natural language constraints to LTL, enabling non-experts to specify rules. Flexibility sliders allow users to balance constraint strictness, supporting adaptive personalization. The model checker provides deterministic feedback, improving transparency and trust. These design patterns are directly applicable to Odin's budget recommendation, anomaly detection, and user constraint modules."
  directly_justifies:
    - "Formal verification significantly improves perceived performance and satisfaction in LLM-based planning systems."
    - "User-defined constraints and iterative verification enhance trust and alignment with personal goals."
    - "Flexibility sliders enable users to prioritize and adapt rules based on evolving preferences."
    - "Visual, interactive interfaces improve understanding and feedback application in LLM systems."
    - "Model checking acts as an external guardrail, reducing cognitive burden and error detection."
  limits:
    - "User study limited to 12 participants and three planning scenarios; finance-specific validation needed."
    - "Temporal constraint template covers six categories; Odin may require additional finance-specific constraints."
    - "System does not handle ambiguous or evolving constraints beyond slider adjustments."
    - "No proactive suggestions or automated repair; users must manually adjust constraints."
    - "Model checker state space may not scale to complex financial planning with many transactions."
  mapping_rationale: "A systematic scan across all 12 functional domains and 38 topic codes was performed. Domains flagged as relevant include: Existing Systems & Gaps (4.A, 4.B) for LLM limitations and planning tool accessibility; Behavioral Profiling (5.A) for user preference specification; Spending Forecasting (6.A) for potential application of verification to predictive models; Budget Recommendation (7.A, 7.C) for constraint-based optimization parallels; Mobile-First Design (9.A, 9.B) for UX insights; Data Privacy & Trust (10.A, 10.B) as verification directly improves trust; User Retention & Engagement (11.A, 11.B) via iterative user control; and System Evaluation (12.A, 12.B) for the ablation study methodology. Borderline cases: seasonal spending (2.B, 2.D) was rejected as the paper does not address temporal patterns in spending. Expense categorization (3.A) was rejected as VeriPlan focuses on action sequences, not transaction classification. Savings/debt management (13.A, 13.B) were rejected as financial goals are not modeled. The paper's core contribution—applying model checking to enforce user-defined constraints in LLM-generated plans—most directly justifies topics 10.B (user trust), 12.A (evaluation frameworks), and 12.B (algorithmic evaluation), with medium relevance to 7.C (constrained optimization) and 11.A/B (engagement/retention). Overall relevance is high for Odin's needs in user-controlled verification and trust-building."
limitations:
  - "Temporal constraint types are limited to six categories; Odin may need more finance-specific constraints. [unacknowledged]"
  - "User sample (n=12) is small and not representative of Filipino young professionals. [unacknowledged]"
  - "System only supports single interactions without contextual memory for iterative rule refinement."
  - "Impact of slider strictness percentages was ambiguous for users."
  - "No automated or proactive suggestions for constraint adjustment or repair."
remember_this:
  - "Model checking improves LLM performance, usefulness, and satisfaction in planning tasks."
  - "User-defined constraints and iterative verification build trust and alignment with personal goals."
  - "Flexibility sliders enable adaptive personalization but strictness impact was ambiguous."
  - "Visual mind-map interfaces improve understanding and feedback application."
  - "num: Full VeriPlan showed significant performance gains (p<.01) over no-verification conditions."
```
---

## Paper 38: Dela Torre et al_summarized.md

**Source File:** `Dela Torre et al_summarized.md`

```yaml
paper_id: 10.61424/rjbe.v3.i3.574
designation: local
title: The Impact of Personal Budgeting Skills on College Students' Financial Stability
authors: Dela Torre, J. M. Y.; Jangao, J. P. P.; Maghilum, J. T.; Man-onan, R. J. H.; Pepito, S. G.; Rapirap, G. P.; Cervantes, J. Z.
year: 2025
venue: Research Journal in Business and Economics
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 3.A
  - 7.A
  - 12.A
  - 13.A
tldr: Personal budgeting skills, particularly in planning, goal setting, and expense tracking, strongly correlate with improved financial stability among college students.
problem_and_motivation: College students frequently face financial stress and instability due to limited resources and inadequate financial management skills. The specific relationship between structured budgeting practices and financial stability for students managing daily expenses remains underexplored.
approach:
  - The study used a descriptive-correlational design with 213 randomly sampled students from a total population of 457 at a Philippine higher education institution.
  - Data were collected using a structured questionnaire adapted from Bhovi (2024) assessing budget planning, financial goal setting, and expense tracking.
  - Financial stability was measured through self-reported financial stress, savings, and monthly expense management using a four-point Likert scale.
  - Correlation analysis (Pearson R) was performed to test the relationship between budgeting skills and financial stability.
  - T-Test and ANOVA were used to examine differences in the effect of budgeting skills based on demographic profiles.
findings:
  - num: 86% of respondents have an average monthly allowance of ₱1,000.00 or below.
  - Students demonstrate very high competency in budget planning (mean 3.49), financial goal setting (mean 3.52), and expense tracking (mean 3.45).
  - The study found a strong positive correlation (r = 0.7247, p < 0.01) between personal budgeting skills and financial stability.
  - Students who practice better budgeting habits report lower financial stress and greater savings.
  - Significant differences in financial management capacity were observed across age, year level, program, and average monthly allowance.
key_figures_tables:
  - Table 1: Respondent demographic profile → Majority are female with monthly allowance below ₱1,000.
  - Table 2: Assessment of budgeting skills → Students show very high skills in all three subscales.
  - Table 3: Assessment of financial stability → Students report very high financial stability across all measures.
  - Table 4: Correlation analysis → Strong significant relationship between budgeting and financial stability.
  - Table 5: Demographic differences → Significant differences exist based on age, year, program, and allowance.
key_equations:
  - equation: r = 0.7247
    explanation: Pearson correlation coefficient for budgeting skills and financial stability.
definitions:
  - term: Financial Stability
    definition: The ability to manage expenses, maintain savings, and experience low financial stress.
  - term: Personal Budgeting Skills
    definition: Competency in budget planning, goal setting, and expense tracking.
critical_citations:
  - "[Xiao & O'Neill, 2019] — Budgeting enables efficient resource allocation and debt avoidance."
  - "[Galperti, 2019] — Self-regulation and disciplined planning improve financial outcomes."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: Focuses on college students, a precursor demographic to young professionals in the Philippines.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Provides local data on student allowances and financial constraints relevant to future professionals.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly investigates budgeting behaviors and their link to financial stability among students.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: Mentions tracking expenses but does not propose a specific categorization framework.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Validates the importance of structured budgeting strategies for financial stability.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: low
      justification: Uses a survey-based evaluation approach applicable to system design.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Links effective budgeting to improved savings behavior.
  contribution: This paper provides empirical evidence that strong budgeting skills correlate with reduced financial stress, which supports Odin's focus on behavior-tracking modules. The findings justify the development of budget planning and expense tracking features in a PFMS like Odin. The strong correlation between planning and stability highlights the need for personalized budgeting tools.
  directly_justifies:
    - Budget planning, goal setting, and expense tracking are key determinants of financial stability for users with limited income.
    - A strong positive relationship exists between structured budgeting practices and reduced financial stress.
    - Students who engage in consistent budgeting maintain small but consistent savings even with minimal income.
  limits:
    - The study's context is a single higher education institution in Baungon, limiting generalizability to other socioeconomic groups.
    - Reliance on self-administered questionnaires may introduce response bias.
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The domains of "Filipino Cultural Context," "Expense Categorization," "Budget Recommendation," and "Savings & Debt Management" were flagged as relevant due to the paper's focus on local student financial behaviors and budgeting practices. Specifically, topics 1.A, 1.B, and 1.C were assigned high relevance as the paper directly addresses the financial demographics and behavior of Filipino students. Topic 7.A was also deemed highly relevant as it validates budgeting strategies as essential domain knowledge. Topics 3.A and 13.A were assigned contextual and medium relevance respectively, as the paper touches on expense tracking and savings but does not propose novel frameworks. The domains of "Forecasting," "Anomaly Detection," "Mobile-First Design," and "Data Privacy" were considered and rejected as the paper does not address algorithmic, predictive, or technical design aspects. Overall, the paper provides foundational behavioral evidence for Odin's user profiling and budgeting modules.
limitations:
  - The study is limited to one higher education institution in Baungon, which may not represent the broader Filipino young professional demographic. [unacknowledged]
  - The findings rely on self-reported data, which may be subject to social desirability bias. [unacknowledged]
  - The study does not account for external factors like family support or part-time employment that could influence financial stability. [unacknowledged]
remember_this:
  - Budgeting skills show a strong positive correlation with financial stability among Filipino students.
  - Students with better budgeting habits experience less financial stress and save more.
  - Most students manage a monthly allowance of ₱1,000 or below.
  - Effective budget planning and goal setting are key to financial well-being.
  - The findings support the integration of financial literacy programs in educational curricula.
```
---

## Paper 39: Saeedian_summarized.md

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

## Paper 40: Dimaranan & Dy_summarized.md

**Source File:** `Dimaranan & Dy_summarized.md`

```yaml
paper_id: 10.29244/jfs.v10i1.62925
designation: local
title: Financial Management and Commitment to Sending Remittances of Filipina Wives in Virginia, United States
authors: Dimaranan, C. F. D.; Dy, M. F. R.
year: 2025
venue: Journal of Family Sciences
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 3.A
  - 13.A
  - 13.C
tldr: Examines how nine Filipina wives in Virginia manage finances and sustain remittances to the Philippines, revealing that unplanned emergency requests strain budgets and savings.
problem_and_motivation: Research on the financial management of Filipina wives residing overseas with their families of procreation while sending remittances to their families of orientation is scarce. Understanding this dual financial responsibility is crucial to assess household stability and the sustainability of transnational support.
approach:
  - Conducted face-to-face in-depth interviews with nine Filipina wives in Virginia, USA, from 2018-2020.
  - Used purposive and snowball sampling to recruit participants who are married, have children, and send remittances.
  - Employed thematic analysis to analyze qualitative data on household finances, budgeting, and remittance practices.
  - Interview guide was validated by three family studies experts and covered socio-demographics, income, expenditures, financial management, and remittance patterns.
  - Performed within-case and across-case analyses to identify themes and compare cases.
findings:
  - num: All nine households have sufficient income to cover expenses and savings, with total monthly household incomes ranging from $5,000 to $22,500.
  - num: The Philippines set a new record of $3.6 billion in personal remittances in 2023.
  - All households practice financial management through clear goals, monthly budgets, proactive decision-making, and savings.
  - Remittances are sent monthly to cover household bills, education, food, and medical expenses, with amounts ranging from $40 to $500+.
  - Emergency requests for additional remittances disrupt monthly budgets and savings, creating potential financial mismanagement.
  - Filipina wives who are dependent homemakers still send remittances, showing commitment is personal, not solely income-dependent.
key_figures_tables:
  - Table 1: Socio-demographics of participants → Shows diverse migration histories and visa pathways.
  - Table 2: Work status of Filipina participants → Highlights variation from full-time to dependent homemakers.
  - Table 4: Monthly household income → Demonstrates income sufficiency across all households.
  - Table 5: Breakdown of monthly expenses → Details fixed, variable, and loan expenditures.
  - Table 6: Monthly remittances sent → Illustrates regularity and recipient relationships.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Family of procreation
    definition: The family one establishes through marriage and having children.
  - term: Family of orientation
    definition: The family into which one is born or raised.
  - term: Remittance
    definition: Money sent by a migrant to family in their country of origin.
  - term: Balikbayan box
    definition: A box of gifts and goods sent by overseas Filipinos to family in the Philippines.
  - term: Pakikipagkapwatao
    definition: A Filipino core value of shared humanity and treating others as fellow human beings.
  - term: Utang-na-loob
    definition: A Filipino value of debt of gratitude, motivating reciprocity and support.
critical_citations:
  - "[Alampay, 2014] — Defines Filipino family-centeredness and values."
  - "[Jalagat Jr. & Dalluay, 2016] — Provides OFW financial management context."
  - "[McCallum, 2021] — Discusses remittances in Filipino transnational families."
  - "[Medina, 2015] — Outlines Filipino family structures and dynamics."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: Focuses on Filipina wives as a specific demographic subset.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Directly details household income, expenses, budgeting, and financial management.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Explores financial practices, decision-making, and commitment to remittances.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Examines "utang-na-loob" and family-centeredness driving remittance behavior.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: low
      justification: Mentions occasional and emergency remittances, but not systematic cycles.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: medium
      justification: Remittances cover special occasions and emergencies, reflecting cultural spending triggers.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Provides a detailed breakdown of variable, fixed, loan, and subscription expenses.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Identifies savings for children's education, emergency funds, and future investments.
    - code: 13.C
      name: End-of-Period Surplus as a Savings Input
      relevance: low
      justification: Alludes to savings from income surplus but does not explicitly model surplus allocation.
  contribution: This paper provides qualitative evidence on the financial management practices of Filipina wives with transnational obligations, which can inform Odin's budgeting modules by highlighting the impact of unplanned remittances on household stability. The findings on shared versus sole budget-holding can guide design for collaborative financial planning features. The culturally motivated remittance behavior underscores the need for Odin's expense categorization to accommodate family support obligations. This research directly justifies the inclusion of emergency fund and savings goal modules within Odin.
  directly_justifies:
    - The practice of mental budgeting suggests Odin should support both manual and automated tracking.
    - Emergency remittance requests disrupt monthly budgets, justifying need for flexible reallocation.
    - Savings for children's education and retirement are key financial goals that require dedicated modules.
    - Joint financial decision-making supports Odin's design for collaborative household budgeting.
    - The regularity of monthly remittances indicates a need for recurring expense features in Odin.
  limits:
    - Small sample size (n=9) limits generalizability to all Filipina wives in the US.
    - Income and expense data are based on participant estimates, not verified financial records.
    - The study focuses only on Virginia, which may not represent Filipinas in other states.
    - Husbands' perspectives on financial management and remittances were not collected.
    - Numerical data are approximations for households where husbands are sole budget holders.
  mapping_rationale: A systematic scan across all 12 functional domains was conducted for this paper. The domains most relevant are Filipino Cultural Context (2.A, 2.D), Expense Categorization (3.A), and Savings & Debt Management (13.A, 13.C). Topic 2.A (Culturally Specific Practices) was rated high due to the paper's direct treatment of "utang-na-loob" and family-centeredness as drivers of remittances. Topic 1.B (Financial Structure) and 1.C (Financial Behavior) were rated high for their detailed accounts of household income, expenditure patterns, and budgeting practices. Topic 3.A was rated medium for its useful expense categorization. Topics 2.B and 13.C were rated low/medium as the paper touches on them but does not focus on cyclical patterns or surplus modeling. Domains such as Behavioral Profiling, Forecasting, Anomaly Detection, and UX Design were rejected as the paper is purely qualitative and does not address algorithmic or system-level design. Overall, the paper offers strong qualitative insights into the financial realities of Filipino migrants, which can contextualize the design needs for a PFMS like Odin.
limitations:
  - Small sample size (n=9) limits generalizability.
  - Income and expense values are estimations, not exact figures. [unacknowledged]
  - Study only covers Virginia, not other U.S. states. [unacknowledged]
  - Husbands' perspectives on financial management were not included. [unacknowledged]
remember_this:
  - Monthly remittances are a fixed expense, not an optional extra.
  - Emergency requests disrupt budgets, causing financial strain.
  - Savings for children's education is a top priority.
  - Income sufficiency does not eliminate budget vulnerability.
  - Cultural values strongly sustain remittance commitment.
```
---

## Paper 41: Song et al_summarized.md

**Source File:** `Song et al_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international-algorithm-specific
title: Deep learning-based time series forecasting
authors: Song, X.; Deng, L.; Wang, H.; Zhang, Y.; He, Y.; Cao, W.
year: 2025
venue: Artificial Intelligence Review
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
tldr: A comprehensive survey of deep learning time series forecasting models (2014-2024) analyzing temporal and variable correlations, computational efficiency, and loss functions, with findings that simpler linear models often outperform complex ones.
problem_and_motivation: Accurate time series forecasting is critical for domains like energy, finance, and health, but existing deep learning models face challenges in capturing complex temporal patterns and computational efficiency. A systematic review and comparison of these models is needed to guide both research and practical application.
approach:
  - The paper surveys over 30 deep learning forecasting models developed between 2014 and 2024, including RNNs, CNNs, Transformers, and linear models.
  - It introduces a novel classification based on the logic of time series information mining, distinguishing approaches that model time-step dependencies from those modeling variable correlations.
  - It analyzes methods for long-term forecasting optimization, including sequence shortening and attention sparsification, to address the quadratic complexity of standard Transformers.
  - The study categorizes loss functions into single-objective (MAE, MSE, quantile) and hybrid (negative log-likelihood, adversarial) types, explaining their suitability for different prediction tasks.
  - It provides an extensive empirical evaluation on five real-world datasets (ETT, Electricity, Exchange, Traffic, ILI) and an artificial dataset, comparing models on prediction accuracy, information mining, and computational complexity.
findings:
  - num: DLinear, a simple linear model, often outperforms sophisticated deep learning models in prediction accuracy, demonstrating that complex architectures may not effectively capture temporal dependencies.
  - num: Shuffling input sequences for models like DLinear and PatchTST caused prediction accuracy drops of up to 1092.50% (MSE) on the Exchange dataset, while many complex models showed minimal change, indicating overfitting and poor utilization of temporal order.
  - num: Extending the lookback window for complex models (e.g., ETSformer, Autoformer) did not consistently improve accuracy, suggesting overfitting and noise interference, whereas PatchTST and DLinear benefited from longer sequences.
  - Models using frequency-domain methods for seasonal information extraction (Fedformer, ETSformer, TDformer) outperformed time-domain methods (LSTnet, DLinear) on an artificial dataset, with Fedformer showing up to 44.17% lower MSE for seasonal term prediction.
  - The patch-slicing approach (PatchTST, Pyraformer) effectively reduces attention mechanism complexity while improving accuracy, with PatchTST achieving 28.83% lower MAE and 42.09% lower MSE than LogTrans on the ETTh1 dataset for a prediction length of 336.
key_figures_tables:
  - Table 5: Multivariate forecasting results → DLinear and PatchTST consistently achieve top performance across datasets and horizons.
  - Table 7: Input shuffling experiment → Complex models show significantly lower performance drops, indicating weaker use of temporal order than simpler models.
  - Table 8: Lookback window extension → Performance of complex models often degrades with longer inputs, while DLinear and PatchTST benefit.
  - Table 9: Trend and season prediction on artificial data → Fedformer and TDformer excel at trend terms, while frequency-domain models excel at season terms.
  - Figure 20: Inference time comparison → Reformer has the lowest inference time, followed by PatchTST.
  - Figure 21: Memory occupation comparison → PatchTST has the lowest memory usage, especially for long-term forecasting.
key_equations:
  - equation: "LSTM: i_t = σ(W_xi x_t + W_hi h_{t-1} + b_i), f_t = σ(W_xf x_t + W_hf h_{t-1} + b_f), c_t = f_t * c_{t-1} + i_t * tanh(W_xc x_t + W_hc h_{t-1} + b_c), h_t = o_t * tanh(c_t)"
    explanation: LSTM gating mechanisms for long-term dependency capture.
  - equation: "Attention: O = V Softmax(Q^T K / √D_k)"
    explanation: Core transformer attention mechanism for similarity computation.
  - equation: "Auto-Correlation: τ_1,...,τ_k = arg Top_{τ∈{1,...,L}} R(τ), Auto-Correlation(X) = Σ Roll(X,τ_i) * R_hat(τ_i)"
    explanation: Autoformer's method for extracting seasonal patterns via time-delay similarity.
definitions:
  - term: Time-step dependency
    definition: Correlations between consecutive and distant time steps in a sequence.
  - term: Variable correlation
    definition: Interdependencies among different univariate time series in a multivariate dataset.
  - term: Patch slicing
    definition: Dividing a long time series into fixed-length segments for efficient attention computation.
  - term: Frequency domain analysis
    definition: Transforming time series to frequencies using Fourier transforms to extract periodic patterns.
  - term: Non-stationary information
    definition: Variations in statistical properties (mean, variance) of a time series over time.
critical_citations:
  - "[Vaswani et al., 2017] — Introduced Transformer architecture."
  - "[Wu et al., 2021] — Proposed Autoformer with time series decomposition."
  - "[Zhou et al., 2021] — Developed Informer for efficient long-term forecasting."
  - "[Nie et al., 2022] — Introduced PatchTST with patch-slicing attention."
  - "[Goodfellow et al., 2014] — Foundation for adversarial loss functions."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Provides comprehensive review of deep learning models for time series forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Evaluates and compares numerous forecasting algorithms applicable to spending data.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Informs the choice of forecasting models that can be used in budget recommendation systems.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Findings on model performance inform algorithm selection for budget recommendation.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Forecasting accuracy and uncertainty measures are relevant for anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Models evaluated are applicable to anomaly detection in spending patterns.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides rigorous evaluation methodology (MAE, MSE, MAPE, R2) for forecasting modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Extensive comparison of different algorithms (DLinear, PatchTST, Transformer variants) on multiple datasets.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Evaluation metrics and experimental setups can be adapted for budget recommendation evaluation.
  contribution: "The paper provides Odin with a systematic, evidence-based evaluation of state-of-the-art time series forecasting models, directly informing algorithm selection for its core spending forecasting and budget recommendation modules. Its demonstration that simpler linear models (DLinear) can outperform complex Transformers challenges assumptions about model complexity and suggests a more efficient architecture for Odin's deployment. The detailed analysis of model behavior under input shuffling and lookback window extension reveals critical overfitting and noise-handling limitations, guiding Odin's development team on potential pitfalls. The classification of loss functions and their suitability for different data characteristics (e.g., outlier-heavy vs. information-rich points) provides design guidance for Odin's optimization objectives. Overall, this survey serves as a foundational technical reference for implementing, evaluating, and justifying Odin's algorithmic core."
  directly_justifies:
    - "DLinear's linear layer effectively captures sequential information for time series forecasting."
    - "PatchTST's patch-slicing method reduces attention complexity while improving prediction accuracy."
    - "Frequency domain methods (Fedformer, ETSformer) excel at extracting seasonal spending patterns."
    - "Complex models (Autoformer, ETSformer) suffer from overfitting and poor utilization of temporal order."
    - "Extending lookback windows does not consistently improve complex models, suggesting noise interference."
  limits:
    - "The survey is general and does not address the specific characteristics of personal financial spending data, such as user-defined categories or irregular transaction timing."
    - "Findings on overfitting and model selection are based on benchmark datasets (e.g., Electricity, Traffic) that may not fully represent the financial behavior of Filipino young professionals."
    - "The paper does not evaluate models under mobile-first design constraints like latency or limited on-device compute."
    - "Recommendations for probabilistic forecasting are mentioned but not deeply explored in the empirical evaluation."
  mapping_rationale: "The systematic scan across all 12 functional domains and 38 canonical topic codes flagged the core technical domains (Spending Forecasting, Budget Recommendation, Anomaly Detection, and System Evaluation) as highly relevant. Within these, topics 6.A, 6.B, 12.A, and 12.B were assigned 'high' relevance due to the paper's direct focus on evaluating and comparing forecasting algorithms. Topics 7.B and 8.B received 'medium' relevance because while the paper does not directly address recommendation or detection, its findings on model performance are directly transferable to those modules. Borderline cases included 2.B (Seasonal and Cyclical Spending Patterns), which was considered but rejected (low relevance) because the paper does not address cultural or domain-specific seasonality—it focuses on generic periodic patterns in electricity, traffic, and finance. Similarly, 3.A (Expense Categorization Frameworks) was considered and rejected (contextual) as the paper does not discuss category design or user-defined constraints. Topics related to privacy, engagement, and behavioral profiling were deemed irrelevant (not selected) due to a complete lack of coverage. The paper's overall relevance to Odin is high as a comprehensive technical reference for algorithm selection, evaluation, and optimization."
limitations:
  - "Does not address specific financial data challenges like irregular intervals or user-defined categories. [unacknowledged]"
  - "Evaluation datasets are from energy, traffic, and healthcare, not personal finance. [unacknowledged]"
  - "Does not consider model deployment constraints like latency or on-device inference for mobile applications. [unacknowledged]"
  - "The paper acknowledges that most models are designed for fixed input/output lengths, limiting flexibility for on-demand forecasting."
  - "Does not provide guidance on handling missing or sparse data, common in personal finance. [unacknowledged]"
remember_this:
  - "DLinear often outperforms complex deep learning models in time series forecasting."
  - "Patch slicing effectively reduces attention complexity while maintaining high accuracy."
  - "Simple linear models better utilize sequential order than sophisticated architectures."
  - "Frequency domain methods excel at extracting seasonal patterns from time series data."
  - "Extending lookback windows does not consistently improve complex models due to overfitting."
```
---

## Paper 42: Ao et al_summarized.md

**Source File:** `Ao et al_summarized.md`

```yaml
paper_id: "10.1109/ACCESS.2025.3602791"
designation: "international-algorithm-specific"
title: "A Review of Time Series Prediction Models Based on Deep Learning"
authors: "Ao, X.; Gong, Y.; He, A."
year: 2025
venue: "IEEE Access"
odin_topics:
  - "6.A"
  - "6.B"
  - "8.A"
  - "8.B"
  - "12.A"
  - "12.B"
tldr: "Reviews deep learning time series models (CNNs, RNNs, Transformers, GNNs, hybrids) and provides a task-oriented selection framework based on sequence length, multivariate support, and efficiency."
problem_and_motivation: "Real-world time series are nonlinear and non-stationary, making traditional statistical models inadequate. Deep learning offers nonlinear modeling and feature extraction but lacks systematic, application-oriented selection guidelines. This survey addresses the gap by structuring model comparison and selection based on task requirements."
approach:
  - "Systematically reviews prominent DL model families: CNNs, RNNs (LSTM/GRU), Transformer variants (Informer, Autoformer, iTransformer), GNNs, and hybrid models."
  - "Analyzes core principles, strengths, limitations, and key architectural innovations (e.g., dilated convolutions in TCN, gating in LSTM/GRU, ProbSparse attention in Informer)."
  - "Proposes a task-oriented framework evaluating models across sequence length handling, multivariate support, interpretability, computational efficiency, and real-time performance."
  - "Provides in-depth comparative analysis of model categories using tabulated attributes and cross-model trend analysis from benchmark studies."
  - "Discusses emerging challenges: interpretability, efficiency optimization, and integration of multi-source data/domain knowledge."
findings:
  - "num: Informer reduces self-attention complexity from O(L^2) to O(L log L)."
  - "num: ETSformer reduces inference latency by 37% compared to Autoformer on ETT data."
  - "num: PatchTST achieves 23% lower MSE than Informer with 60% less GPU memory."
  - "num: ARIMA-RNN hybrid achieved 15% MAE reduction on Electricity Load Dataset compared to standalone models."
  - "Transformer variants dominate ultra-long horizon forecasting (>1000 steps) in multivariate settings."
  - "GNNs excel when strong spatial/relational dependencies exist (e.g., traffic, supply chains)."
  - "Hybrid models (e.g., N-BEATS, ETSformer) enhance accuracy and interpretability by combining statistical decomposition with deep learning."
  - "iTransformer's inverted architecture (variables as tokens) shows strong multivariate generalization."
  - "Model selection depends on trade-offs between modeling power, efficiency, sequential fidelity, and interpretability."
  - "Emerging trend: simpler unified architectures (iTransformer, PatchTST) reduce complex, custom-designed components."
key_figures_tables:
  - "Figure 1: Structure of one-dimensional CNN → CNN extracts local spatial patterns via convolution and pooling."
  - "Figure 2: Dilated causal convolution in TCN → Expands receptive field without increasing depth."
  - "Figure 3: TCN residual block → Residual connections improve training stability in deep networks."
  - "Table 1: Analysis of CNN-based algorithms → Compares CNN, TCN, WaveNet-CNN, Kmeans-CNN, SCINet."
  - "Table 6: Comparative analysis of model categories → Summarizes strengths and limitations of CNN, RNN, Transformer, GNN, Hybrid models."
  - "Figure 12: Task-driven model selection framework → Matches problem characteristics (sequence length, dependencies) to optimal model classes."
key_equations:
  - equation: "TCN = 1DFCN + causal convolutions"
    explanation: "Simplified formula for Temporal Convolutional Network structure."
definitions:
  - term: "CNN"
    definition: "Convolutional Neural Network, excels at extracting local spatial features."
  - term: "TCN"
    definition: "Temporal Convolutional Network, uses dilated causal convolutions for long-range dependencies."
  - term: "RNN"
    definition: "Recurrent Neural Network, processes sequential data with hidden state memory."
  - term: "LSTM"
    definition: "Long Short-Term Memory, RNN variant with gating mechanisms for long-term dependencies."
  - term: "GRU"
    definition: "Gated Recurrent Unit, simplified LSTM with update and reset gates."
  - term: "GNN"
    definition: "Graph Neural Network, models relational dependencies using graph structures."
  - term: "GCN"
    definition: "Graph Convolutional Network, performs convolution on graph data for spatial dependencies."
  - term: "STGCN"
    definition: "Spatio-Temporal Graph Convolutional Network, joint spatial and temporal modeling."
  - term: "MTGNN"
    definition: "Multivariate Time Series Graph Neural Network, learns dynamic graph structures."
  - term: "ARIMA"
    definition: "Autoregressive Integrated Moving Average, classical statistical model for linear time series."
critical_citations:
  - "[Vaswani et al., 2017] — Introduced Transformer with self-attention, foundational for many models."
  - "[Hochreiter & Schmidhuber, 1997] — Introduced LSTM, solving gradient vanishing for long sequences."
  - "[Bai et al., 2018] — Proposed TCN for efficient sequence modeling with causal convolutions."
  - "[Zhou et al., 2021] — Informer with ProbSparse attention for efficient long-sequence forecasting."
  - "[Wu et al., 2021] — Autoformer integrating series decomposition and auto-correlation."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Core survey on deep learning predictive models directly applicable to Odin's forecasting modules."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Reviews RNNs, Transformers, and hybrids specifically for sequential data forecasting."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses models (e.g., CNN, LSTM) applicable to anomaly detection in spending sequences."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "medium"
      justification: "Provides algorithmic foundations (TCN, LSTM) that can be adapted for anomaly detection."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides comparative analysis framework and task-driven selection relevant for evaluation."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Discusses evaluation across dimensions (accuracy, efficiency, interpretability) relevant to module assessment."
  contribution: "This survey directly informs Odin's predictive modeling and anomaly detection modules by providing a structured comparison of DL algorithms suitable for spending data. The task-oriented selection framework helps choose models (e.g., LSTM/GRU for sequential spending, GNN for multivariate dependencies, hybrids for accuracy) based on Odin's specific requirements. The analysis of efficiency trade-offs informs mobile-first implementation choices and real-time constraints. The discussion on model interpretability guides Odin's need for explainable predictions to build user trust. The coverage of emerging challenges like computational efficiency and domain knowledge integration aligns with Odin's practical deployment needs."
  directly_justifies:
    - "LSTM and GRU effectively capture long-term dependencies in sequential spending data."
    - "Transformer variants like Informer enable efficient long-sequence forecasting for spending patterns."
    - "Hybrid models combining statistical methods with DL improve forecasting accuracy and robustness."
    - "Model selection should match sequence length, multivariate dependencies, and efficiency constraints."
    - "Attention mechanisms provide a basis for model interpretability in financial predictions."
  limits:
    - "Focuses on algorithmic capabilities without addressing financial domain-specific constraints (e.g., user allocation rules)."
    - "Does not evaluate models on PFMS-specific data like Philippine spending cycles. [unacknowledged]"
    - "Lacks detailed discussion on cold-start scenarios common in personal finance apps. [unacknowledged]"
    - "Computational benchmarks are not directly applicable to mobile-device resource constraints. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains was conducted. The paper was flagged as highly relevant to the Predictive Modeling (6.A) and Forecasting Algorithms (6.B) domains because it is a comprehensive review of DL models for time series prediction, directly applicable to Odin's spending forecasting. It also provided medium relevance to Anomaly Detection (8.A, 8.B) as the reviewed models can be adapted for this purpose, and to System Evaluation (12.A, 12.B) through its proposed comparison framework. Borderline cases included the discussion of GNNs for multivariate dependencies, which primarily supports 6.B but also touches on 8.B for network-based anomaly detection. Domains related to user behavior (1.A-C, 5.A-C), cultural context (2.A-D), expense categorization (3.A-C), system landscape (4.A-B), budgeting (7.A-D), mobile design (9.A-B), privacy (10.A-B), retention (11.A-B), and savings/debt (13.A-C) were considered and rejected as the paper is purely algorithmic and does not address user, cultural, design, or financial domain-specific constraints. Overall, the paper provides strong foundational knowledge for Odin's predictive and detection algorithms but requires supplementation with domain-specific and contextual research."
limitations:
  - "Interpretability remains challenging across all Transformer variants."
  - "High computational complexity demands substantial resources for large-scale data. [unacknowledged]"
  - "The performance of specialized models depends on matching design assumptions to data characteristics."
  - "General models need more data to achieve robustness compared to specialized ones. [unacknowledged]"
  - "Decomposition-based hybrids incur computational redundancy from iterative operations. [unacknowledged]"
remember_this:
  - "Informer reduces self-attention complexity to O(L log L) for long sequences."
  - "ETSformer cuts inference latency by 37% versus Autoformer."
  - "PatchTST achieves 23% lower MSE than Informer with 60% less memory."
  - "Model selection must balance modeling power, efficiency, and interpretability."
  - "Hybrid models combining statistics and deep learning enhance accuracy and explainability."
```
---

## Paper 43: Singh U. et al_summarized.md

**Source File:** `Singh U. et al_summarized.md`

```yaml
paper_id: d3b07384-d9a1-11f0-9d8a-00155d0e6b4c
designation: international-algorithm-specific
title: A Predictive Framework for Annual Financial Planning using Deep Learning Models
authors: Singh, U.; Anand, U.; Singh, V.
year: 2025
venue: Journal of Scientific Innovation and Advanced Research (JSIAR)
odin_topics:
  - 6.A
  - 6.B
  - 4.B
  - 7.B
tldr: Deep learning models, particularly LSTM, outperform traditional statistical methods for annual expense forecasting by capturing complex temporal dependencies in financial data.
problem_and_motivation: Traditional forecasting methods like ARIMA and linear regression fail to capture the non-linear and dynamic nature of real-world financial data, limiting accuracy for long-term planning. There is a need for a more accurate and adaptive framework for annual expense forecasting to support proactive fiscal decision-making.
approach:
  - Financial datasets were collected from public expenditure portals and augmented with synthetic data.
  - Data was preprocessed with missing value imputation, min-max normalization, and sliding window sequence creation.
  - LSTM and GRU models were designed and compared against a baseline RNN for annual expense forecasting.
  - Hyperparameters were tuned using grid search and Bayesian optimization, with dropout and early stopping to prevent overfitting.
  - Models were evaluated using MAE, RMSE, and MAPE metrics on a temporal split of the dataset.
findings:
  - "num: LSTM achieved the lowest MAE of 1872.56, compared to 2450.13 for RNN."
  - "num: LSTM's RMSE was 2614.32, demonstrating superior stability over the RNN (3120.88)."
  - "num: The MAPE for LSTM was 7.02%, outperforming both GRU (7.48%) and RNN (9.85%)."
  - LSTM forecasts closely followed the true trend of annual spending with minimal deviation, validating its applicability for long-term planning.
  - The use of dropout layers and early stopping effectively mitigated overfitting during LSTM training.
  - GRU provided a computationally efficient alternative with comparable accuracy to LSTM.
  - Deep learning models demonstrated strong generalization and stability across the training and validation phases.
  - The framework enables better resource allocation and risk assessment for organizational financial planning.
key_figures_tables:
  - "Figure 1: System architecture of the proposed framework → Shows the layered, modular design for financial forecasting."
  - "Figure 2: Data processing and forecasting pipeline → Illustrates the sequential workflow from ingestion to prediction."
  - "Figure 4: LSTM predicted vs. actual expenses → Forecasts closely follow the true annual expenditure trend."
  - "Figure 5: Training and validation loss per epoch for LSTM → Smooth convergence indicates robustness without overfitting."
  - "Table II: Performance comparison of models → LSTM outperforms RNN and GRU across all error metrics."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "LSTM"
    definition: "Long Short-Term Memory, a recurrent neural network architecture designed to capture long-term dependencies."
  - term: "GRU"
    definition: "Gated Recurrent Unit, a simplified recurrent neural network variant with computational efficiency."
  - term: "MAE"
    definition: "Mean Absolute Error, a metric measuring the average magnitude of prediction errors."
  - term: "RMSE"
    definition: "Root Mean Squared Error, a metric that penalizes larger errors more heavily."
  - term: "MAPE"
    definition: "Mean Absolute Percentage Error, a metric expressing prediction accuracy as a percentage."
critical_citations:
  - "[Siami-Namini et al., 2019] — LSTM outperforms ARIMA in accuracy."
  - "[Fischer and Krauss, 2018] — Deep nets achieve higher returns than econometric models."
relevance:
  topics:
    - code: 6.A
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: high
      justification: "Paper proposes and evaluates a deep learning framework for annual expense forecasting."
    - code: 6.B
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: high
      justification: "Paper benchmarks LSTM and GRU, which are key algorithms for sequential data, against traditional methods."
    - code: 4.B
      name: "Limitations and Gaps in Existing Systems"
      relevance: medium
      justification: "Explicitly identifies limitations of traditional statistical methods like ARIMA and linear regression."
    - code: 7.B
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: contextual
      justification: "Establishes the predictive foundation that is a prerequisite for effective budget recommendation systems."
  contribution: "The paper provides a validated LSTM-based framework that can serve as a core predictive module for Odin's spending forecasting. Its comparative analysis justifies the selection of deep learning over classical methods for Odin's forecasting component. The demonstrated ability to capture seasonal patterns directly supports Odin's need to model Filipino spending cycles. The emphasis on long-term annual forecasting aligns with Odin's goal of providing annual budget recommendations."
  directly_justifies:
    - "LSTM significantly outperforms ARIMA and linear regression in forecasting accuracy."
    - "Deep learning models can capture non-linear patterns that traditional methods miss."
    - "The proposed framework is robust for long-term (annual) financial planning."
  limits:
    - "The study focuses on annual forecasting, while Odin may require monthly or weekly predictions for granular insights."
    - "The framework's dependency on high-quality data is a limitation for real-world deployment with potentially noisy data."
  mapping_rationale: "A systematic scan was performed across all 12 functional domains and their associated topic codes. The domains of 'Spending Forecasting' (6.A, 6.B) were flagged as highly relevant, as the paper's core contribution is a predictive framework for annual expenses. The 'Existing Systems & Gaps' domain (4.B) was flagged as medium relevance because the paper explicitly critiques the limitations of traditional statistical methods like ARIMA, which directly informs Odin's design choices. The 'Budget Recommendation' domain (7.B) was considered contextual, as accurate forecasting is a prerequisite for budget recommendations, but the paper does not directly address recommendation algorithms. Domains such as 'Filipino Cultural Context', 'Behavioral Profiling', and 'Mobile-First Design' were considered and rejected, as the paper does not address these aspects and its data originates from public expenditure sources, not the Philippines. The paper's overall relevance to Odin is high for its algorithmic contributions to forecasting, providing a validated baseline for the system's predictive engine."
limitations:
  - "The paper does not address the cold-start problem, which is critical for new users in a PFMS. [unacknowledged]"
  - "The proposed models are evaluated on a specific financial domain; their generalizability to personal finance data may be limited. [unacknowledged]"
  - "The framework's performance with noisy or incomplete data, a common real-world scenario, is not discussed. [unacknowledged]"
remember_this:
  - "LSTM achieved 7.02% MAPE for annual expense forecasting."
  - "LSTM and GRU outperform ARIMA and linear regression for sequential financial data."
  - "Deep learning captures non-linear patterns that traditional methods fail to model."
  - "The study validates deep learning for long-term annual financial planning."
  - "Model robustness is ensured through techniques like dropout and early stopping."
```
---

## Paper 44: Tambuli & Villarba_summarized.md

**Source File:** `Tambuli & Villarba_summarized.md`

```yaml
paper_id: f7c8a2e4-5b6a-4c1e-9d3f-8a2b4c6d8e0f
designation: local
title: PERSONAL FINANCIAL MANAGEMENT BEHAVIOR AND FINANCIAL PLANNING AS KEY DRIVERS OF RETIREMENT PREPAREDNESS AMONG LGU's CONTRACTUAL PERSONNEL
authors: Tambuli, A. P.; Villarba, L. O.
year: 2025
venue: ISRG Journal of Economics and Finance
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 4.A
  - 4.B
  - 5.A
  - 7.A
  - 7.D
  - 13.A
  - 13.B
tldr: Financial management behavior and financial planning significantly drive retirement preparedness among LGU contractual personnel in the Philippines.
problem_and_motivation: Contractual employees face income instability and limited saving opportunities, creating gaps in retirement preparedness. Understanding the specific financial behaviors and planning practices of this demographic is essential for developing targeted interventions. Prior research has not adequately examined this population's unique retirement planning challenges.
approach:
  - Data were collected from 200 LGU contractual personnel in Nabunturan using simple random sampling.
  - A descriptive-correlational research design was employed with an adapted and validated survey questionnaire.
  - Statistical analyses included mean scores, standard deviations, Pearson's r, and multiple regression.
  - The study measured personal financial management behavior across cash management, credit management, and savings/investment.
  - Financial planning was assessed through retirement savings and financial planning abilities indicators.
findings:
  - num: Retirement preparedness was high (mean=3.62, SD=0.90) across asset acquisition, budgeting, and decision-making domains.
  - num: Personal financial management behavior was high (mean=3.62, SD=0.93) with cash management showing the highest mean (3.75).
  - num: Financial planning status was high (mean=3.62, SD=0.91) but retirement savings was only moderately evident (mean=3.37).
  - num: Both PFMB (r=.701, p<.001) and financial planning (r=.739, p<.001) had strong significant correlations with retirement preparedness.
  - num: PFMB (β=.350, p<.001) and financial planning (β=.485, p<.001) jointly predicted 61.5% of variance in retirement preparedness (R²=.615).
  - Respondents demonstrated high budgeting awareness but limited translation to regular retirement savings behavior.
key_figures_tables:
  - "Table 1: Level of retirement preparedness across domains → Overall high preparedness with moderate consistency (SD=0.90)."
  - "Table 2: Status of personal financial management behavior → High overall status (3.62) with strongest performance in cash management."
  - "Table 3: Status of financial planning → High overall (3.62) but retirement savings domain only moderate (3.37)."
  - "Table 4: Correlation between variables → Both PFMB and financial planning show strong significant correlations (r>.70)."
  - "Table 5: Drivers of retirement preparedness → PFMB and financial planning are significant predictors with β=.350 and .485 respectively."
key_equations:
  - equation: "RP = β₀ + β₁(PFMB) + β₂(FP) + ε"
    explanation: "Regression model predicting retirement preparedness from two predictors."
  - equation: "R² = .615"
    explanation: "Model explains 61.5% of retirement preparedness variance."
definitions:
  - term: LGU
    definition: Local Government Unit.
  - term: PFMB
    definition: Personal Financial Management Behavior.
  - term: RP
    definition: Retirement Preparedness.
  - term: FP
    definition: Financial Planning.
  - term: Theory of Planned Behavior
    definition: "Psychological theory explaining behavior through attitudes, norms, and perceived control."
  - term: Financial Literacy Theory
    definition: "Framework linking financial knowledge to improved financial outcomes."
critical_citations:
  - "[Sturr et al., 2021] — PFMB directly influences retirement preparedness."
  - "[Ajzen, 1991] — Theory of Planned Behavior provides behavioral framework."
  - "[Lusardi & Mitchell, 2013] — Financial literacy theory underpins saving behaviors."
  - "[Nam & Loibl, 2020] — Financial planning predicts retirement readiness."
  - "[Ingale & Paluri, 2023] — Long-term planning resolves retirement preparedness gaps."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "medium"
      justification: "Study focuses on Filipino contractual workers in Davao region."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "high"
      justification: "Examines income instability and limited saving opportunities of contractual personnel."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Measures actual financial behaviors including budgeting and credit management."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "contextual"
      justification: "Philippine LGU context provides cultural specificity but not main focus."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "low"
      justification: "References existing literature on financial planning but no system analysis."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Identifies gap in research on contractual employee retirement preparation."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Directly measures and classifies financial management behaviors."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "high"
      justification: "Examines budgeting practices and their relationship to retirement readiness."
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "contextual"
      justification: "Discusses challenges of saving with limited income but no algorithmic approach."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "high"
      justification: "Focuses on retirement savings goals and regular saving behavior."
    - code: "13.B"
      name: "Debt Management in PFMS"
      relevance: "medium"
      justification: "Includes credit management and loan repayment behaviors."
  contribution: "This paper provides empirical evidence that personal financial management behavior and financial planning are the strongest predictors of retirement preparedness among Filipino contractual employees. It validates the Theory of Planned Behavior in the context of retirement saving decisions. The findings support Odin's module for behavioral profiling by establishing measurable indicators of financial behavior. The strong correlation between budgeting practices and retirement readiness justifies Odin's budget recommendation and savings goal management features. The identification of implementation gaps between financial awareness and actual saving behavior informs Odin's design for behavioral nudges and automatic savings features."
  directly_justifies:
    - "Financial management behavior and financial planning are key drivers of retirement preparedness."
    - "Budgeting practices show strong correlation with retirement readiness."
    - "Cash management is the most prominent component of personal financial management behavior."
    - "Retirement savings implementation lags behind financial planning awareness."
    - "Financial planning abilities are high but translation to regular savings is moderate."
  limits:
    - "Focus on one LGU in Davao de Oro may limit generalizability to other regions."
    - "Cross-sectional design cannot establish causal relationships."
    - "Self-reported measures may be subject to social desirability bias."
    - "Excludes permanent employees, limiting comparison with other employment types."
    - "Does not explore underlying psychological or structural barriers to saving. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was conducted for this paper. The domains of Behavioral Profiling & Classification (5.A, 5.B, 5.C), Budget Recommendation (7.A, 7.B, 7.C, 7.D), and Savings & Debt Management (13.A, 13.B, 13.C) were flagged as highly relevant because the paper directly measures financial behaviors and planning as drivers of retirement preparedness. The Filipino Cultural Context domain (2.A, 2.B, 2.C, 2.D) was considered medium relevance for 2.A due to the Philippine LGU context, but codes 2.B, 2.C, and 2.D were rejected as the paper does not address seasonal spending or user-declared preferences. Existing Systems & Gaps (4.A, 4.B) was assigned medium relevance for 4.B as the paper identifies a research gap but does not analyze existing systems. Expense Categorization (3.A, 3.B, 3.C) and Anomaly Detection (8.A, 8.B, 8.C) were rejected as the paper does not address these algorithmic modules. Mobile-First Design (9.A, 9.B), Data Privacy (10.A, 10.B), User Retention (11.A, 11.B), and System Evaluation (12.A, 12.B, 12.C) were all rejected as not addressed. The paper's overall relevance to Odin is high for foundational behavioral insights, but it lacks algorithmic or systems design contributions."
limitations:
  - "Sample limited to one municipality in Davao de Oro, reducing generalizability."
  - "Cross-sectional design prevents causal inference."
  - "Self-reported survey data may introduce social desirability bias."
  - "Does not examine the role of financial education or literacy programs."
  - "Lacks longitudinal tracking of retirement savings behavior. [unacknowledged]"
  - "Does not address the influence of household or family financial dynamics. [unacknowledged]"
remember_this:
  - "Financial management behavior and financial planning predict 61.5% of retirement preparedness variance."
  - "Cash management is the strongest component of personal financial management behavior."
  - "Retirement savings implementation lags behind financial planning awareness."
  - "Budgeting practices correlate strongly with retirement readiness."
  - "Contractual employees show high financial awareness but limited saving behavior."
```
---

## Paper 45: Huang A. et al_summarized.md

**Source File:** `Huang A. et al_summarized.md`

```yaml
paper_id: 10.4018/JGIM.395852
designation: international-algorithm-specific
title: Dynamic Calibration of Decision Thresholds for Financial Anomaly Detection: Verification With Payment Platform Information and Data
authors: Huang, A.; Zhang, X.; Wang, Y.; Tsai, S.; Zhou, P.; Chen, L.
year: 2025
venue: Journal of Global Information Management
odin_topics:
  - 8.A
  - 8.B
  - 8.C
  - 12.B
tldr: Proposes a Temporal-Attention Isolation Forest with Dynamic Calibration that adapts the anomaly decision threshold online and incorporates temporal context to improve fraud detection in payment streams.
problem_and_motivation: Existing Isolation Forest-based fraud detectors rely on static thresholds that fail under shifting transaction distributions, causing high false alarms or missed fraud. Real-world payment streams are non-stationary and require adaptive mechanisms. Prior work lacks a principled, unsupervised approach to threshold calibration and temporal modeling.
approach:
  - Uses a sliding window to segment transaction streams for online processing.
  - Applies a temporal attention encoder to capture short-range dependencies and periodic patterns.
  - Computes anomaly scores using an Isolation Forest ensemble on attended transaction representations.
  - Dynamically calibrates the decision threshold via a quantile-based update smoothed with a learning rate.
  - Optionally incorporates delayed labels to correct thresholds using false positive/negative feedback.
  - Evaluates on five real and synthetic datasets (IEEE-CIS, PaySim, CCFD, SFD-FD, BankSim).
  - Compares against six baselines including Online-iForest, GNN-IF, SSR-RVFL, and XGB-Anomaly.
  - Reports precision, recall, F1, AUC, and per-transaction latency under streaming protocols.
  - Ablates dynamic threshold and attention components to isolate their contributions.
findings:
  - "num: TA-IFDC achieved F1=0.927 and AUC=0.974 on IEEE-CIS, outperforming all baselines."
  - "num: Dynamic threshold calibration improved recall from 0.835 to 0.918 and F1 from 0.852 to 0.927."
  - "num: Under concept drift, TA-IFDC F1 dropped only 0.012 versus 0.085 for Online-iForest and 0.067 for SSR-RVFL."
  - "num: On CCFD minority fraud detection, TA-IFDC attained F1=0.896, surpassing SSR-RVFL (0.857) and XGB-Anomaly (0.764)."
  - "num: Cross-dataset transfer from PaySim to CCFD yielded F1=0.841 and AUC=0.904, the highest among comparators."
  - "num: Inference latency stayed at 29 ms per transaction, within real-time constraints and faster than all deep/hybrid baselines."
  - Removing temporal attention reduced AUC from 0.968 to 0.938 on PaySim, confirming its value.
  - Dynamic calibration maintains stable alert rates during seasonal traffic shifts without manual retuning.
  - Temporal attention helps detect sequences of small anomalies that appear benign in isolation.
key_figures_tables:
  - "Figure 2: Bar charts comparing F1 and latency on IEEE-CIS → TA-IFDC achieves highest F1 (0.927) and second-lowest latency (29 ms)."
  - "Figure 3: Ablation of dynamic threshold on IEEE-CIS → removing it drops recall by 8.3 percentage points, confirming calibration's importance."
  - "Figure 4: ROC curves on PaySim → TA-IFDC with attention (AUC 0.968) clearly outperforms without attention (AUC 0.938)."
  - "Figure 5: F1 before/after concept drift on SFD-FD → TA-IFDC shows the smallest drop (−0.012), demonstrating robustness."
  - "Figure 7: Minority class detection and cross-dataset generalization → TA-IFDC leads in both F1 (0.896) and transfer performance (0.841)."
key_equations:
  - equation: s(z)=2^{-E(h(z))/c(n)}
    explanation: Anomaly score from Isolation Forest; shorter path implies higher anomaly likelihood.
  - equation: θ_k = (1-λ)θ_{k-1} + λ Quantile_β(𝒮_k)
    explanation: Smoothed quantile-based update of the decision threshold using current score distribution.
  - equation: Δθ_k = η (α FP_k/W - (1-α) FN_k/W)
    explanation: Feedback correction term to balance false positives and negatives when labels are available.
definitions:
  - term: IF
    definition: Isolation Forest, an unsupervised anomaly detection algorithm based on random partitioning.
  - term: TA-IFDC
    definition: Temporal-Attention Isolation Forest with Dynamic Calibration, the proposed framework.
  - term: DTC
    definition: Dynamic Threshold Calibration module that adapts the decision boundary online.
  - term: AUC
    definition: Area Under the ROC Curve, a threshold-independent ranking metric.
critical_citations:
  - "[Liu et al., 2008] — Original Isolation Forest algorithm, foundational to the approach."
  - "[Zhang et al., 2022] — Context on fraud losses and the need for adaptive detection."
  - "[Vanini et al., 2023] — Discusses online payment fraud and the shift to risk management."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly presents an anomaly detection framework for financial transactions, applicable to PFMS fraud/overspending detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Proposes and evaluates a specific algorithmic enhancement (adaptive threshold + temporal attention) for transaction anomaly scoring.
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: medium
      justification: Dynamic calibration operates without requiring labels, offering a baseline strategy for new users or data streams with sparse feedback.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Provides extensive experimental evaluation of the proposed algorithm against baselines across multiple datasets and metrics.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: contextual
      justification: Discusses the limitation of static thresholds in prior fraud detectors, which motivates the work, but does not focus on PFMS specifically.
  contribution: "TA-IFDC offers a modular anomaly detection component that can be integrated into Odin's spending monitor to flag irregular transactions. Its dynamic thresholding directly addresses the need for adaptive alerting under changing user behavior and seasonal spending patterns. The temporal attention module enhances detection of sequential fraud patterns, which is valuable for identifying suspicious spending cascades. The framework's unsupervised nature aligns with Odin's goal of working with limited labeled data, and its low latency supports mobile-first real-time feedback. Together, these features make the method a strong candidate for Odin's anomaly detection subsystem."
  directly_justifies:
    - "Adaptive threshold calibration improves recall and reduces false alarms in non-stationary transaction streams."
    - "Incorporating temporal context (attention) captures short-range dependencies and boosts detection of contextual anomalies."
    - "Unsupervised anomaly scoring with online calibration can operate without ground-truth labels, suitable for cold-start scenarios."
    - "Latency below 30 ms per transaction meets real-time processing requirements for mobile payment alerts."
  limits:
    - "Assumes continuous, time-stamped transaction streams with consistent logging; legacy systems may require preprocessing."
    - "Feedback loop relies on delayed labels or model-derived signals; direct expert annotations are not yet incorporated."
    - "Performance may degrade under extreme class imbalance if feedback is very sparse, though fallback quantile adaptation remains stable."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes flagged Anomaly Detection as the primary area of relevance, with high relevance for topics 8.A and 8.B because the paper directly proposes and evaluates a novel anomaly detection algorithm for payment data. Topic 8.C was assigned medium relevance because the dynamic calibration mechanism provides an unsupervised cold-start baseline by adjusting thresholds without requiring labels. Topic 12.B received medium relevance due to the comprehensive algorithmic evaluation methodology. Topic 4.B was considered contextual because the paper notes limitations of static thresholds in existing systems but does not focus on PFMS gaps. Other domains—Expense Categorization, Budget Recommendation, Mobile-First Design, Data Privacy, User Retention, Savings & Debt Management—were rejected as the paper does not address them. The overall relevance to Odin is strong for its anomaly detection module, offering a practical, low-latency approach that can be adapted to personal spending alerts."
limitations:
  - "The method requires transaction timestamps and temporal ordering, which may not be available in all banking APIs. [unacknowledged]"
  - "Feedback calibration uses model-derived signals; incorporating actual user or analyst feedback could further improve adaptability. [unacknowledged]"
  - "Extreme class imbalance (e.g., fraud rates below 0.2%) may require additional safeguards to prevent threshold overcorrection."
  - "The attention mechanism adds some overhead, though latency remains within acceptable bounds."
remember_this:
  - "Dynamic threshold calibration raised recall from 83.5% to 91.8% on IEEE-CIS."
  - "TA-IFDC maintained F1 near 0.91 across varying window sizes with latency under 32 ms."
  - "Under concept drift, TA-IFDC lost only 1.2% F1 versus >8% for static baselines."
  - "Temporal attention increased AUC by 0.03 on PaySim by capturing sequential anomalies."
  - "Cross-dataset transfer achieved F1 0.841, showing good generalization to unseen payment patterns."
```
---

## Paper 46: Patiu et al_summarized.md

**Source File:** `Patiu et al_summarized.md`

```yaml
paper_id: 3187f7d0-7d47-530b-8c3e-492a21f406bb
designation: local
title: Unraveling the Investment Puzzle: Do Behavioral Biases and Financial Literacy Matter?
authors: Patiu, L. S.; Ang, L. K. C.; Masanque, J. A. A.; Nacario, J. M. C.; Paguntalan, R. M. M.
year: 2025
venue: Review of Integrative Business and Economics Research
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 5.A
  - 5.B
  - 5.C
  - 7.A
  - 7.B
  - 10.A
  - 10.B
tldr: Filipino Gen Y and Gen Z investment decisions are significantly influenced by behavioral biases, with financial literacy moderating these effects and exhibiting a negative direct impact on Generation Y.
problem_and_motivation: Investors in emerging markets often make irrational decisions due to low financial literacy and behavioral biases, yet the specific interplay of these factors for Filipino young professionals remains underexplored. Understanding these dynamics is crucial for designing effective financial advisory and educational interventions.
approach:
  - A structured survey was administered online to 385 Filipino retail investors in Metro Manila, using Google Forms.
  - The study employed a quantitative explanatory design and utilized the Ordinary Least Square method for regression analysis.
  - Hierarchical regression was applied to measure the unique variance added by each behavioral bias (overconfidence, herding, disposition effect, risk aversion) to investment decisions.
  - Moderation analysis was conducted to measure the influence of the interaction between behavioral biases and financial literacy.
  - The study used adapted scales from Adil et al. (2022) for behavioral biases, financial literacy, and investment decisions, with reliability confirmed via Cronbach's Alpha.
findings:
  - Herding bias significantly and positively affects investment decisions for both Generation Y (β=0.189***) and Generation Z (β=0.213***).
  - Risk aversion significantly affects Generation Y (β=0.245***) but not Generation Z, while overconfidence is significant for Generation Z (β=0.199**) but not Generation Y.
  - Financial literacy has a significant negative influence on Generation Y's investment decisions (β=-0.391*), but an insignificant negative influence on Generation Z.
  - The inclusion of herding bias (∆R2=0.2189 for Gen Y) and disposition effect bias (∆R2=0.0554 for Gen Y) significantly improved predictive power for both groups.
  - Risk aversion added significant variance (∆R2=0.0561) for Generation Y but not for Generation Z (∆R2=0.0008).
  - Financial literacy significantly moderates the effect of overconfidence (β=1.111**) and disposition effect (β=0.696*) on Generation Y's investment decisions, but shows no significant moderation for Generation Z.
  - num: The addition of risk aversion bias in Model 4 accounted for 5.61% of the variance in investment decisions for Generation Y.
  - num: Herding bias added a 21.89% variance in investment decisions for Generation Y investors, compared to 15.87% for Gen Z.
  - The study found that 50.3% of respondents were Millennials (Gen Y) and 49.7% were Gen Z, with a majority being female (54.6%) and employees (60.5%).
key_figures_tables:
  - "Table 1: Demographic profile showing 196 Gen Y and 194 Gen Z respondents, majority female and employees → sample is predominantly employed females from two generations."
  - "Table 2: Regression results showing that herding and disposition effect are significant for both generations, while overconfidence and risk aversion differ → behavioral biases impact varies across generations."
  - "Table 3: Hierarchical regression model fits for Gen Y and Gen Z, showing R^2 values from 0.021 to 0.352 → adding biases improves model explanatory power."
  - "Table 4: Model comparisons showing ∆R^2 and p-values for each step of hierarchical regression → risk aversion only adds significant variance for Gen Y."
  - "Table 5: Regression results for financial literacy, showing a negative significant effect for Gen Y only → financial literacy has a different effect between the two generations."
  - "Table 6: Moderation results showing that financial literacy significantly moderates only two biases for Gen Y → moderation effect is limited to the older cohort."
key_equations:
  - equation: Investment Decision = β0 + β1OB + β2HB + β3DB + β4RAB + β5FL
    explanation: Regression model measuring impact of four behavioral biases and financial literacy.
definitions:
  - term: Overconfidence bias
    definition: Tendency to overestimate one's ability and knowledge to predict future information.
  - term: Herding bias
    definition: Investor's tendency to imitate the investment decisions of others.
  - term: Disposition effect
    definition: Tendency to sell winning stocks too early and hold losing stocks too long.
  - term: Risk aversion
    definition: Investor's preference to avoid risk or losses, favoring safer investments.
  - term: Financial literacy
    definition: Ability and skills to manage personal finances to decrease potential errors in financial decisions.
critical_citations:
  - "[Adil et al., 2022] — Found herding bias negatively impacts Pakistani millennial investors."
  - "[Almansour et al., 2023] — Found herding and risk aversion positively affect Saudi investors."
  - "[Mahmood et al., 2024] — Found negative impact of risk aversion on investment decisions."
  - "[Prasetyo et al., 2023] — Found negative moderation of FL on herding/overconfidence."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Directly studies Filipino Gen Y and Z retail investors as its core population.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Investigates investment decisions, a key aspect of financial structure for these cohorts.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: The entire study is an empirical investigation of investment behavior and its drivers.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: low
      justification: Focuses on behavioral biases and literacy, not uniquely Filipino cultural practices.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Does not directly examine spending cycles; provides context on investor behavior.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: Provides background on financial behavior but does not study spending cycles.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly profiles investors by four key behavioral biases (overconfidence, herding, disposition, risk aversion).
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: Does not address cold-start problems, but confirms that different biases affect decisions.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses regression to classify and measure the impact of each bias, providing data for profile classification.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: Provides knowledge on investor decision-making behavior, but not budgeting strategies.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: contextual
      justification: Offers insights on biases and literacy that could inform recommendation systems, but not directly.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Does not address data privacy, but its findings on literacy and behavior are relevant to user trust.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: Does not examine trust but provides context on factors influencing financial decisions.
  contribution: This paper's findings on behavioral biases are foundational for Odin's user behavioral profiling module (Topic 5.A), providing empirical evidence that overconfidence, herding, disposition effect, and risk aversion significantly influence Filipino young professionals' financial decisions. The significant moderating role of financial literacy on these biases, particularly for Generation Y, directly informs Odin's cold-start profiling (Topic 5.B) and suggests that an initial financial literacy assessment is crucial for accurate user classification. The observed generational differences in the influence of overconfidence and risk aversion justify the need for dynamic, age-aware behavioral models that can adapt to different user profiles. Moreover, the negative impact of financial literacy on Generation Y's investment decisions challenges simple assumptions and highlights the importance of nuanced, non-prescriptive design in financial applications.
  directly_justifies:
    - Odin's behavioral profiling module must measure overconfidence, herding, disposition effect, and risk aversion for Filipino users.
    - Financial literacy is a significant moderator of behavioral biases and should be part of the user profiling process.
    - Generation-specific differences in behavioral bias impact require adaptive models in a PFMS.
    - A low financial literacy score may not predict poor financial decisions, requiring careful interpretation in system design.
  limits:
    - The sample is limited to Filipino retail investors in Metro Manila, potentially limiting generalizability.
    - The study uses a self-reported online survey, which is subject to social desirability and recall bias.
    - The analysis is correlational and does not establish causal relationships between biases and investment decisions.
    - The study does not investigate the user's actual financial behavior, only their reported decisions.
  mapping_rationale: A systematic scan of all 12 functional domains revealed that the paper's core contribution directly aligns with Domain 5 (Behavioral Profiling) and Domain 2 (Cultural Context). The paper's empirical findings on the influence of overconfidence, herding, disposition effect, and risk aversion on Filipino Gen Y and Z investors provide high-relevance evidence for Topic 5.A (Financial Behavioral Profiles) and Topic 1.C (Financial Behavior of Filipino Young Professionals). The significant moderating effect of financial literacy offers medium relevance to Topic 5.B (Profile Dynamics) and Topic 5.C (Classification Approaches) by informing how initial user states can be estimated. The contextual relevance to Domains 7 (Budget Recommendation) and 10 (Data Privacy) is noted, as the insights on user behavior can inform system design and trust, but the paper does not directly address those topics. Other domains (3, 4, 6, 8, 9, 11, 12, 13) were considered and rejected as the paper does not cover expense categorization, forecasting, anomaly detection, or engagement mechanisms. Overall, this paper provides strong empirical justification for integrating behavioral bias measurement into Odin's user profiling and is moderately relevant for designing classification and cold-start strategies.
limitations:
  - The sample of 385 Filipino retail investors from Metro Manila may not represent all Filipino young professionals. [unacknowledged]
  - The study relies on self-reported data, which may be subject to social desirability bias. [unacknowledged]
  - The cross-sectional design prevents establishing causality between biases, literacy, and decisions. [unacknowledged]
  - The research instrument was adapted, but its full validity for the Philippine context was not extensively discussed.
remember_this:
  - Herding bias significantly drives investment decisions for both Gen Y and Gen Z in the Philippines.
  - Risk aversion impacts Gen Y investment decisions but not Gen Z's.
  - Financial literacy negatively influences Gen Y's investment decisions in this sample.
  - Financial literacy moderates overconfidence and disposition effect only for Generation Y.
  - Overconfidence significantly impacts Gen Z but not Gen Y investment decisions.
```
---

## Paper 47: Pisal et al_summarized.md

**Source File:** `Pisal et al_summarized.md`

```yaml
paper_id: 10.1038/s41598-025-17604-y
designation: international-algorithm-specific
title: An integrated TOPSIS and ARAS method multi-criteria decision-making approach for optimizing investment portfolios using goal programming and genetic algorithm model
authors: Pisal, P.; Reddy, K. K.; Kishore, J.; Jonnalagadda, R. R.; Kumar, M.; Band, G.; Joshi, B. P.
year: 2025
venue: Scientific Reports
odin_topics:
  - 4.A
  - 4.B
  - 5.A
  - 6.A
  - 6.B
  - 7.B
  - 7.C
  - 7.D
  - 8.B
  - 12.A
  - 12.B
  - 12.C
  - 13.A
  - 13.B
tldr: A hybrid framework integrates TOPSIS-ARAS ranking with goal programming and genetic algorithms to optimize investment portfolios, achieving a Sharpe ratio of 2.241 on the FAR-Trans dataset.
problem_and_motivation: Existing portfolio optimization models either rank assets without allocating capital or optimize allocations without integrating investor preferences. This separation leads to suboptimal plans that fail to balance multiple objectives like return, risk, and diversification. A unified framework combining preference modeling with constrained optimization is critically needed.
approach:
  - Data from the FAR-Trans dataset (359,128 transactions, 2018-2022) is preprocessed using min-max scaling and one-hot encoding.
  - A two-layer MCDM framework fuses TOPSIS closeness coefficients and ARAS utility scores via a convex combination to rank assets.
  - A goal programming model encodes investor-specific return targets, risk thresholds, and budget constraints as deviation variables.
  - A genetic algorithm with tournament selection, SBX crossover, and Gaussian mutation explores the feasible space to refine portfolio weights.
  - The framework is benchmarked against Markowitz, NSGA-III, MOPSO, and other state-of-the-art models using Sharpe ratio, ROI, diversification, and budget adherence.
findings:
  - num: The proposed model achieved a Sharpe ratio of 2.241 and an annualized return of 4.6%.
  - num: The diversification score was 0.845 across 79 assets and 13 sectors.
  - num: A 0.729 correlation was found between TOPSIS-ARAS rankings and GP-configured portfolio returns.
  - The GA module converged within 80 generations, demonstrating computational efficiency.
  - Sensitivity analysis showed high rank stability (Kendall's τ > 0.89) across different MCDM fusion weights.
  - Investor segmentation revealed that 59% of transactions were purchases, indicating a bullish accumulation trend.
  - The model maintained a budget deviation of €36.2M while achieving over 30% returns in validation portfolios.
key_figures_tables:
  - Figure 3: Transaction distribution showing 59% purchases → Indicates alignment with stable asset selection.
  - Figure 4: Investor segmentation showing 61% "Mass" customers → Supports capital-based constraint modeling in GP.
  - Figure 9: ROI distribution across Stocks, Bonds, MTFs → Highlights equities achieving outlier returns >80%.
  - Figure 12: Top 10 asset allocations with Financial Services dominating → Reflects high MCDM scores for return-risk profile.
  - Table 4: Performance comparison vs. state-of-the-art → Confirms proposed model's superiority across all metrics.
key_equations:
  - equation: \phi_i = \alpha \cdot C_i^{TOPSIS} + (1-\alpha) \cdot U_i^{ARAS}
    explanation: Convex fusion of TOPSIS and ARAS scores for hybrid ranking.
  - equation: \text{Min} \sum_{j=1}^{n} (d_j^+ + d_j^-)
    explanation: Goal programming objective minimizing deviations from investor targets.
  - equation: \text{Fitness} = \sum x_i r_i - \lambda \left| \sum x_i \sigma_i - \sigma^* \right|
    explanation: GA fitness function balancing return and risk penalty.
definitions:
  - term: TOPSIS
    definition: Technique for Order Preference by Similarity to Ideal Solution, ranks alternatives by geometric distance to ideal and anti-ideal points.
  - term: ARAS
    definition: Additive Ratio Assessment, ranks alternatives using additive normalization and utility scores.
  - term: GP
    definition: Goal Programming, an optimization method that minimizes deviations from multiple, possibly conflicting, objectives.
  - term: GA
    definition: Genetic Algorithm, an evolutionary metaheuristic that iteratively improves solutions via selection, crossover, and mutation.
  - term: MCDM
    definition: Multi-Criteria Decision Making, a set of methods for evaluating alternatives based on multiple conflicting criteria.
  - term: FAR-Trans
    definition: Financial Asset Recommendation Transactions dataset, containing anonymized investor and asset data from a European institution.
critical_citations:
  - "[Vásquez et al., 2021] — AHP-TOPSIS benchmark for stock portfolio investments."
  - "[Anadani et al., 2023] — GA approach for portfolio optimization baseline."
  - "[Mwamba et al., 2025] — NSGA-III application for multi-objective portfolio selection."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Reviews traditional MCDM and optimization systems but not specific PFMS.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Explicitly identifies the gap between preference modeling and allocation optimization.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: low
      justification: Segments investors by risk tolerance but does not define behavioral profiles for PFMS.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: contextual
      justification: Uses historical returns and risk but not predictive spending models.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: Applies GA/GP to asset allocation, not to sequential spending forecasting.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Provides a general optimization framework that could inform budget recommendations.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: high
      justification: Directly presents a GP-GA model for constrained asset allocation.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: low
      justification: Penalty-based handling of risk constraints is mentioned but not a primary focus.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: The method uses deviation minimization, conceptually related to anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: low
      justification: Uses Sharpe ratio and ROI for evaluation, not PFMS-specific metrics.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Ablation study and comparative baselines validate each module's contribution.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: low
      justification: Evaluation is for investment portfolios, not budget recommendation systems.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: contextual
      justification: Return maximization could relate to savings growth but is not the core focus.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: low
      justification: Does not address debt; focuses on asset allocation for return.
  contribution: The paper provides a validated, modular framework for multi-objective portfolio optimization that can inform Odin's budget allocation and optimization modules. Its dual MCDM ranking (TOPSIS-ARAS) offers a stable asset pre-selection method that could be adapted for expense category prioritization. The GP-GA hybrid demonstrates how investor-specific constraints (return, risk, budget) can be encoded into a solvable optimization problem, relevant to Odin's budget recommendation engine. The ablation study and sensitivity analysis offer best practices for evaluating algorithmic modules and handling parameter uncertainty.
  directly_justifies:
    - "A hybrid MCDM-GP-GA framework can effectively balance multiple financial objectives with investor constraints."
    - "Integrating TOPSIS and ARAS via convex fusion reduces ranking sensitivity and stabilizes asset selection."
    - "Genetic algorithms are computationally feasible for portfolio optimization with early convergence under 100 generations."
    - "Sensitivity analysis with Kendall's τ can validate the robustness of ranking systems against parameter changes."
  limits:
    - "The model assumes single-period static optimization, which limits adaptability to dynamic market conditions."
    - "Computational time scales with portfolio size, requiring optimization for high-frequency use cases."
    - "Investor constraints are modeled as linear goals, ignoring fuzzy or utility-based preferences."
    - "Regulatory constraints, transaction costs, and tax implications are not included."
  mapping_rationale: A systematic scan across all 12 functional domains revealed that this paper most directly informs the System Evaluation domain (12.A, 12.B, 12.C) through its comprehensive evaluation framework. It also provides strong methodological insights for Budget Recommendation via Constrained Optimization (7.C) with its GP-GA model. The paper's explicit discussion of the gap between preference modeling and allocation (4.B) offers supporting evidence for the limitations of existing personal finance systems. Topics related to Behavioral Profiling (5.A) and Forecasting (6.A, 6.B) were flagged with low or contextual relevance because the paper uses general investor risk profiles and historical returns, not the specific Filipino behavioral or spending patterns relevant to Odin. The domains of Filipino Cultural Context (2.A-D) and Mobile-First Design (9.A-B) were considered and rejected as they are not addressed. Data Privacy (10.A-B) and User Retention (11.A-B) were also not within the paper's scope. The paper's overall relevance to Odin is medium, as it offers a robust, validated methodological template for building an optimization engine, but requires significant adaptation to the PFMS context.
limitations:
  - The model assumes single-period static optimization, not dynamic market conditions or multi-period planning. [unacknowledged]
  - Genetic algorithm convergence time may become a bottleneck for high-frequency portfolio recommendations.
  - The framework uses linear investor goals, but real-world preferences are often fuzzy or utility-based. [unacknowledged]
  - Regulatory constraints, transaction costs, and tax considerations are absent from the model. [unacknowledged]
  - The model's interpretability is enhanced by visualizations but lacks formal XAI modules like SHAP or LIME. [unacknowledged]
remember_this:
  - Hybrid MCDM-GP-GA achieved a Sharpe ratio of 2.241 and ROI of 4.6%.
  - Dual TOPSIS-ARAS ranking via convex fusion enhances asset selection stability.
  - GP encodes investor-specific return, risk, and budget constraints as deviations.
  - GA optimization converged within 80 generations with a population size of 100.
  - The framework outperformed NSGA-III and MOPSO across all key portfolio metrics.
```
---

## Paper 48: Takayanagi et al_summarized.md

**Source File:** `Takayanagi et al_summarized.md`

```yaml
paper_id: 10.1145/3726302.3729897
designation: international-algorithm-specific
title: Are Generative AI Agents Effective Personalized Financial Advisors?
authors: Takayanagi, T.; Izumi, K.; Sanz-Cruzado, J.; McCreadie, R.; Ounis, I.
year: 2025
venue: Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR '25)
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 10.B
  - 11.A
  - 12.A
  - 12.B
  - 12.C
  - 4.B
tldr: LLM-based conversational agents can effectively elicit investor preferences and personalize advice, but their influence depends on elicitation quality, and users may trust agents that provide worse advice.
problem_and_motivation: Human financial advisors are costly, excluding many; automated systems often ignore personalization and trust-building. Existing conversational agents have not been tested in high-stakes financial advisory where users lack expertise and mistakes carry risk. This paper investigates whether LLM-advisors can effectively elicit preferences, provide personalized guidance, and leverage personality to foster trust.
approach:
  - Conducted a lab-based user study with 64 participants acting as three archetypal investor profiles (growth-oriented, conservative income, risk-taking).
  - Divided interaction into two stages: preference elicitation (System-Ask-User-Respond paradigm) and advisory discussion for four assets per profile.
  - Compared non-personalized baseline, personalized (using elicited preferences), and two personality-injected variants (extroverted and conscientious) using Llama-3.1 8B.
  - Evaluated elicitation accuracy against a human expert and decision-making effectiveness via Spearman's rank correlation between participant and expert asset rankings.
  - Collected user perceptions across 7 dimensions (personalization, trust, satisfaction, etc.) using 7-point Likert scales.
findings:
  - num: Elicitation accuracy averaged 0.70 across profiles, close to expert's 0.85 for growth and conservative, but dropped to 0.53 for risk-taking (40.5% lower).
  - Personalized advice improved decision-making correlation from 0.11 (baseline) to 0.31, but only when elicitation was successful (0.481); unsuccessful elicitation caused negative correlation (-0.228).
  - Users rated personalized and non-personalized advisors similarly on most dimensions except information provision; they could not distinguish good from bad advice.
  - Extroverted personality led to lower decision quality (0.122 vs 0.26 for conscientious) but higher intention to use and emotional trust.
  - Sentiment analysis showed extroverted advisors used more positive language, while conscientious advisors used more negative and uncertain terms.
key_figures_tables:
  - Table 3: Elicitation accuracy by profile and advisor variant → LLM matches expert for 2/3 profiles but fails for risk-taking.
  - Table 4: Spearman's rho between investor and expert rankings → personalization improves only with successful elicitation.
  - Table 5: Average participant responses to advisor assessment → users cannot distinguish personalized from non-personalized, and prefer extroverted despite worse advice.
  - Figure 4: Average sentiment scores by advisor personality → extroverted uses more positive language, conscientious more negative/uncertain.
key_equations:
  - equation: ElicitationAccuracy(i) = 1/n * sum_{j=1}^{n} (|i_LLM_j ∩ i_pref| / |i_pref|)
    explanation: Proportion of correctly captured investor preferences averaged over sessions.
definitions:
  - term: LLM
    definition: Large Language Model
  - term: SAUR
    definition: System-Ask-User-Respond, a conversational paradigm where the system asks questions and the user responds.
  - term: Big Five
    definition: A personality model comprising five traits: openness, conscientiousness, extraversion, agreeableness, neuroticism.
critical_citations:
  - [Radlinski et al., 2019] — foundational for conversational preference elicitation.
  - [Komiak and Benbasat, 2006] — trust and adoption of recommendation agents.
  - [Jiang et al., 2024] — method for injecting personality into LLMs.
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Defines and uses investor profiles (growth, conservative, risk-taking) as behavioral profiles for financial decision-making.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: high
      justification: Preference elicitation stage addresses the cold-start problem by collecting investor preferences through conversation.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses predefined profile categories and evaluates elicitation accuracy, contributing to classification approaches.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Measures emotional trust and trust in competence, showing personality affects trust even when advice quality differs.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Measures user satisfaction and intention to use, relevant to engagement dynamics.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Proposes a user study evaluation framework with multiple metrics (accuracy, ranking correlation, questionnaires).
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Evaluates the LLM-advisor as an algorithmic module for financial advice.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Uses Spearman's rho and questionnaires, similar to evaluation methodologies for recommendation systems.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: contextual
      justification: Discusses limitations of existing automated financial systems that ignore personalization and trust.
  contribution: This paper directly informs Odin's preference elicitation module by showing that LLM-based conversation can capture user preferences, but highlights the need for robust handling of contradictory statements. It validates the importance of accurate user profiling for personalized recommendations, as poor elicitation leads to adverse outcomes. The findings on trust and personality inform Odin's design of conversational interfaces that balance advice quality and user satisfaction. The evaluation framework (ranking correlation, questionnaires) provides a methodology for testing Odin's advisory components.
  directly_justifies:
    - LLM-advisors can match human experts in preference elicitation for straightforward investor profiles.
    - Personalization of advice improves investment decisions only when preferences are accurately elicited.
    - Users cannot distinguish between good and bad advice and may trust more personable but less accurate advisors.
  limits:
    - The study uses synthetic investor profiles, not real investors; participants may not fully internalize profiles.
    - Only two personality variants tested; other traits may differ.
    - Participants were university students, not representative of all investors.
  mapping_rationale: A systematic scan across all 12 functional domains and their topic codes was performed. Domains flagged as relevant include Behavioral Profiling & Classification (codes 5.A, 5.B, 5.C) with high relevance because the paper directly studies investor profiles and cold-start elicitation; Data Privacy & User Trust (10.B) high due to explicit trust measurements; User Retention & Engagement (11.A) medium for satisfaction and intention measures; System Evaluation (12.A, 12.B, 12.C) medium for the user study and evaluation metrics; and Existing Systems & Gaps (4.B) contextual for background. Borderline cases: the preference elicitation touches on 2.C (user-declared preferences) but was rejected because the context is investment advice, not PFMS expense preferences; similarly, budgeting topics (7.A-D) were considered but rejected as the paper focuses on asset selection, not budget allocation. Domains like Filipino cultural context, expense categorization, forecasting, anomaly detection, mobile design, and savings/debt management were deemed not applicable. Overall, the paper is highly relevant to Odin's user profiling, personalization, and trust-building aspects, while providing an evaluation methodology applicable to its modules.
limitations:
  - The study uses synthetic investor profiles rather than real investors, limiting external validity.
  - Only two personality variants were tested; other personality traits or combinations may yield different outcomes.
  - Participants were university students, which may not represent the broader investor population.
  - The LLM used (Llama-3.1 8B) may not generalize to other models.
  - The study does not explore long-term effects or repeated interactions.
remember_this:
  - LLM-advisors match human experts in preference elicitation for 2/3 profiles.
  - Successful preference elicitation improves decision-making correlation from 0.11 to 0.481.
  - Unsuccessful elicitation leads to negative correlation (-0.228), directing investors to wrong assets.
  - Users prefer extroverted advisors despite worse advice, increasing trust and intention to use.
  - Extroverted advisors use more positive language, while conscientious ones use more negative/uncertain language.
```
---

## Paper 49: Pretnar et al_summarized.md

**Source File:** `Pretnar et al_summarized.md`

```yaml
paper_id: 10.21203/rs.3.rs-7730348/v1
designation: international-algorithm-specific
title: Mental Accounting Through Two-stage Budgeting Under Bounded Rationality
authors: Pretnar, N.; Olivola, C. Y.; Montgomery, A.
year: 2025
venue: Research Square
odin_topics:
  - 3.A
  - 5.A
  - 6.A
  - 7.A
  - 7.C
  - 8.A
  - 10.B
tldr: A structural model generalizes two-stage budgeting with cognitive frictions to quantify mental accounting behavior from expenditure data alone.
problem_and_motivation: Classical two-stage budgeting assumes perfect fungibility and ex-post budget adherence, yet consumers exhibit mental accounting and sticky budgets due to cognitive costs. There is a lack of empirical, agent-level quantification of how bounded rationality manifests in budgeting. This gap prevents the design of effective financial interventions that account for heterogeneous consumer decision-making.
approach:
  - Proposes a dynamic, two-stage budgeting model where a planner sets ex-ante budgets subject to cognitive constraints and a doer realizes expenditure shocks.
  - Incorporates narrow choice bracketing via probabilistic budget re-evaluation (ψ) and numeracy constraints that prevent trivial budget changes.
  - Mental accounting is captured by a state variable (over/under-spending from prior periods) that influences future budget adjustments via a parameter γ.
  - Estimates the structural model using a hierarchical MH-within-Gibbs MCMC algorithm on weekly expenditure data from 2,509 low-income prepaid debit card users.
  - Compares model variants with absolute ($1) and relative (%) numeracy thresholds, and tests counterfactuals by fully relaxing cognitive constraints.
findings:
  - num: 80% of consumer-week combinations exhibit bounded rationality, with an average of 2.11 budget updates per week under the $1-threshold model.
  - num: A $1 numeracy threshold reduces budget updates by 14.9%, while relative thresholds of 1%, 5%, and 10% reduce updates by 41.8%, 64%, and 70% respectively.
  - Ex-ante budgeting behavior is largely consistent with mental accounting (78.7% are budget prioritizers), but ex-post spending behavior is mixed, with 46.8% classified as spendthrifts.
  - num: 22.3% of consumers are ex-ante budget prioritizers but ex-post habitual over-spenders (type ii), exhibiting a "planning fallacy" pattern after over-spending.
  - Counterfactual relaxation of cognitive constraints makes 68.4% of consumers worse off, and 3.3% go bankrupt under the $1-threshold model.
  - num: Consumers who go bankrupt when constraints are relaxed have significantly lower estimated updates (1.25/week) and are more likely to be ex-ante type (i) but ex-post type (ii).
key_figures_tables:
  - "Table 1: Summary statistics of agent-level means → Shows low-income sample (median weekly income $460) with substantial spending variation."
  - "Table 2: Posterior summary statistics for baseline and $1-threshold models → Reports estimated means and standard deviations for all key behavioral parameters."
  - "Table 3: Marginal distributions of ex-ante and ex-post types → Ex-ante most are budget prioritizers, ex-post plurality are spendthrifts."
  - "Table 4: Joint distributions of ex-ante and ex-post types → Reveals 37.5% are budget prioritizers ex-ante but spendthrifts ex-post."
  - "Figure 2: Time series of actual vs. predicted spending → Demonstrates the model's fit for a median-income agent across categories."
  - "Figure 3: Posterior density of budget updates per week → Shows distribution of k under different numeracy thresholds."
  - "Figure 4: Density of k conditional on counterfactual type → Bankrupt consumers have significantly fewer budget updates."
key_equations:
  - equation: $x_{ijt} = \omega_{ijt} + \zeta_{ijt}$
    explanation: Doer's expenditure is budget plus shock.
  - equation: $a_{ijt} = \omega_{ij,t-1} - x_{ij,t-1} = -\zeta_{ij,t-1}$
    explanation: Mental account balance equals negative prior shock.
  - equation: $\omega_{ijt} = \theta_{ijt} \ell_{it} + \gamma_i a_{ijt}$
    explanation: Budget is income share plus anchored mental account.
  - equation: $\Gamma_{ijt} \sim \text{Bernoulli}(\psi_{ij})$
    explanation: Probability of re-evaluating a specific budget.
  - equation: $\vartheta_{iyt}^* = \frac{\alpha_{i,\iota_{iyt}} \ell_{it} - \alpha_{i,\iota_{iyt}} \sum_{s<y} \ell_{it} \theta_{i,\iota_{ist},t} + \gamma_i a_{i,\iota_{iyt},t} + \zeta_{i,\iota_{iyt},t}}{\ell_{it}(\alpha_{i,\iota_{iyt}} + \alpha_{i,J+1})} \dots$
    explanation: Analytical expression for optimal candidate budget share.
definitions:
  - term: Mental Accounting
    definition: A book-keeping mechanism where past over/under-spending informs future budgets.
  - term: Narrow Choice Bracketing
    definition: Consumers re-evaluate only a subset of budgets per period due to cognitive constraints.
  - term: Numeracy Constraint
    definition: A threshold (absolute or relative) that a budget change must exceed to be implemented.
  - term: Budget Prioritizer
    definition: Consumer type that reduces budget after over-spending and increases after under-spending.
  - term: Spendthrift
    definition: Consumer type that increases spending regardless of prior over or under-spending.
critical_citations:
  - "[Thaler, 1985] — Foundational theory of mental accounting."
  - "[Deaton and Muellbauer, 1980] — Classical two-stage budgeting framework."
  - "[Shefrin and Thaler, 1981] — Planner/doer model of self-control."
  - "[Gabaix, 2014] — Sparse maximization and bounded rationality."
  - "[Kőszegi and Matějka, 2020] — Mental budgeting with attention costs."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: The model operationalizes budget categories and estimates category-specific expenditure shares.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Empirically classifies consumers into ex-ante and ex-post behavioral types (budget prioritizers, spendthrifts).
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Develops a structural forecasting model for spending based on budgets, mental accounts, and shocks.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Models the strategic process of setting and updating budgets under cognitive frictions.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: high
      justification: Formulates budget selection as a constrained optimization problem with cognitive and numeracy constraints.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Expenditure shocks (ζ) are modeled as deviations from budgets, which is foundational for anomaly detection.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: contextual
      justification: Counterfactual analysis shows that nudging via apps can harm certain users, affecting trust.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: low
      justification: The model captures spending spikes and trends but does not focus on seasonality.
  contribution: "The paper provides a structurally estimated model for inferring latent budgeting behavior from expenditure data, which can be used to enhance Odin's spending forecasting module (6.A) by incorporating cognitive constraints. It offers a methodology for dynamically classifying users into behavioral profiles (5.A) based on their budget-updating and spending responses, enabling adaptive budgeting strategies. The counterfactual analysis reveals critical insights for Odin's nudging features (11.A): increasing attentiveness can have adverse effects for some users, implying that interventions should be personalized and cautious. The model's framework for budget updating and mental accounting directly informs the design of Odin's budget recommendation (7.B) and anomaly detection (8.A) algorithms, providing a theoretical basis for handling infeasibility and user inertia. Finally, the identification of distinct consumer types (e.g., budget prioritizers vs. spendthrifts) supports the development of tailored financial advice and savings/debt management strategies (13.A, 13.B)."
  directly_justifies:
    - "Budget updates occur for approximately half of consumption categories each period, supporting a sparse-max approach for Odin's budget recommendation."
    - "A $1 numeracy threshold is a better fit than no threshold, justifying the inclusion of an 'inertia' parameter in Odin's budget adjustment logic."
    - "Relaxing cognitive constraints makes 68% of consumers worse off, suggesting Odin should avoid over-nudging and prioritize user autonomy."
    - "Ex-ante budgeting behavior is distinct from ex-post spending, indicating Odin should track both planned budgets and actual expenditure separately."
    - "Consumers who are ex-ante budget prioritizers but ex-post spendthrifts are most vulnerable to adverse outcomes, requiring targeted support."
  limits:
    - "Results are model-dependent and rely on unobserved latent variables, limiting the certainty of individual-type classifications."
    - "Data is from low-income, underbanked prepaid card users in North America, which may not generalize to Filipino young professionals."
    - "Assumes strong separability of utility, which may oversimplify substitution patterns across broad expenditure categories."
    - "Does not explicitly model price variation, aggregating prices into indices, which may miss important consumption adjustments."
  mapping_rationale: "A systematic scan across all 12 functional domains was conducted. The paper's core theoretical and empirical contributions on modeling bounded rationality in budgeting directly map to high relevance for domains: Expense Categorization (3.A, 3.B), Behavioral Profiling (5.A, 5.B, 5.C), Spending Forecasting (6.A, 6.B), and Budget Recommendation (7.A, 7.B, 7.C, 7.D). The structural estimation approach and consumer typing also offer medium relevance to Anomaly Detection (8.A) and System Evaluation (12.A, 12.B, 12.C). The counterfactual simulations on attentiveness inform Engagement & Retention (11.A) and Data Privacy/Trust (10.B), albeit with contextual or low relevance as the paper does not directly study app design or trust. Topics like Filipino Cultural Context (2.A, 2.B, 2.C) and Savings/Debt (13.A, 13.B) were considered but rejected as the paper's empirical setting is North American and its primary contribution is methodological, though findings on overspending cycles are tangentially relevant to debt management. Borderline cases included the mental accounting state variable (a), which relates to both expense categorization (3.A) and behavioral profiles (5.A); it was assigned to 5.A for its role in defining consumer types. The paper's overall relevance to Odin is high, providing a quantitative, micro-founded framework for modeling key user behaviors that directly informs the design of adaptive and personalized financial management features."
limitations:
  - "Findings are based on a model-dependent estimation of latent budgets, not directly observed." [unacknowledged]
  - "The dataset is from a specific low-income, underbanked population in North America; applicability to other demographics (e.g., Filipino YPs) is not tested." [acknowledged]
  - "Assumes strong separability in utility, which may not capture complex category interactions."
  - "The model does not incorporate explicit price effects, relying on aggregated price indices." [acknowledged]
  - "Counterfactual simulations of 'full rationality' may not reflect real-world behavioral changes from app nudges."
remember_this:
  - "Consumers update only about half their budgets per week, showing bounded rationality."
  - "Most consumers are budget prioritizers ex-ante but spendthrifts ex-post."
  - "Relaxing cognitive constraints makes 68% of consumers worse off."
  - "3.3% of consumers go bankrupt if all budgets are updated weekly."
  - "Sticky budgets can serve as a disciplinary tool for vulnerable consumers."
```
---

## Paper 50: Anes & Abreu_summarized.md

**Source File:** `Anes & Abreu_summarized.md`

```yaml
paper_id: 10.3390/app15074044
designation: international-algorithm-specific
title: Adaptive Cluster-Based Normalization for Robust TOPSIS in Multicriteria Decision-Making
authors: Anes, V.; Abreu, A.
year: 2025
venue: Applied Sciences
odin_topics:
  - 3.A
  - 7.C
  - 8.A
  - 8.B
  - 12.A
  - 12.B
  - 12.C
tldr: Proposes a cluster-based logarithmic normalization for TOPSIS that uses fuzzy numbers for uncertainty and expert-defined centroids to improve ranking stability and outlier robustness.
problem_and_motivation: Traditional TOPSIS normalization techniques like Min-Max and Z-score are sensitive to outliers and large variance, which can distort rankings. Clustering methods also often rely on rigid, data-driven classifications that fail to capture uncertainty or expert intent. There is a need for a more flexible and robust normalization and clustering framework.
approach:
  - Defines cluster centroids a priori using fuzzy numbers based on expert judgment and ideal conditions for each criterion.
  - Converts each alternative's fuzzy criterion scores into crisp centroids using the average of (a, b, c) values.
  - Assigns each alternative to the cluster with the nearest Euclidean distance to its predefined centroid.
  - Applies logarithmic normalization within each cluster to compress extreme values and stabilize variance.
  - Uses the cluster centroids to derive criterion weights and then applies the standard TOPSIS procedure.
  - Validates the approach using a case study on selecting a host city based on cost, infrastructure, safety, and accessibility.
findings:
  - The proposed fuzzy clustering method produced classifications nearly identical to Fuzzy K-Means but with a more logically coherent assignment for a borderline case (City K).
  - The proposed method is computationally simpler and more deterministic than iterative Fuzzy K-Means.
  - Logarithmic normalization provided more balanced and stable TOPSIS scores, especially in clusters with high variance, compared to Min-Max normalization.
  - Top-ranked alternatives (City K and City C) were consistent across both normalization methods, reinforcing the robustness of the overall framework.
key_figures_tables:
  - Table 5: Distances to cluster centroids → Used to assign each city to its most appropriate cluster based on Euclidean distance.
  - Table 8: Logarithmic normalization results → Shows how extreme cost values are compressed within each cluster.
  - Table 11: TOPSIS results using logarithmic normalization → City K (0.89), City C (1.00), and City E (0.89) are top-ranked in their clusters.
key_equations:
  - equation: C_{cwj} = (a_w + b_w + c_w) / 3
    explanation: Calculates the crisp centroid of a cluster for a criterion.
  - equation: C_{Aij} = (a_i + b_i + c_i) / 3
    explanation: Calculates the crisp centroid of an alternative for a criterion.
  - equation: X' = (log(X) - log(X_min)) / (log(X_max) - log(X_min))
    explanation: Logarithmic normalization formula to scale data and reduce outlier impact.
definitions:
  - term: TOPSIS
    definition: Technique for Order of Preference by Similarity to Ideal Solution, a multi-criteria decision-making method.
  - term: MCDM
    definition: Multi-criteria decision-making, a field for evaluating multiple conflicting factors.
  - term: Fuzzy Number
    definition: A representation of uncertainty using a triplet (a, b, c) for lower, central, and upper bounds.
  - term: Cluster Centroid
    definition: The ideal point representing the optimal position for a cluster across all criteria.
critical_citations:
  - "[Vafaei et al., 2021] — Compares normalization techniques on data with outliers."
  - "[Zavadskas & Turskis, 2008] — Introduces a novel logarithmic normalization method in game theory."
  - "[Štilic´ & Puška, 2023] — Comprehensive review of MCDM methods in sustainable engineering."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: Provides a methodological framework for categorizing alternatives (cities) based on cost and other criteria.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: low
      justification: The case study involves budget allocation (cost criterion), but the method does not address constraint optimization.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: The method mitigates the effect of outliers, which is conceptually similar to handling anomalies in financial data.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Focuses on algorithmic robustness to outliers, a key challenge in anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: The paper presents a novel evaluation methodology (TOPSIS with cluster-based normalization) that can be used to rank financial options.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Directly evaluates the performance of the proposed clustering and normalization algorithms within the TOPSIS framework.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: high
      justification: The TOPSIS-based ranking methodology can be applied to evaluate and rank budget recommendation strategies for Odin.
  contribution: The paper provides a methodological framework for evaluating and ranking alternatives under uncertainty, which can be directly applied to Odin's recommendation system. Its cluster-based normalization approach can enhance the robustness of the Budget Recommendation (7.B) and Anomaly Detection (8.A) modules by mitigating the impact of outliers in financial data. The use of expert-defined profiles offers a way to incorporate Filipino cultural context and user preferences into the ranking process. Finally, the deterministic clustering method provides a computationally efficient and transparent approach for grouping users with similar financial behavior profiles.
  directly_justifies:
    - "Cluster-based normalization improves ranking stability by reducing the influence of outliers."
    - "Logarithmic normalization is effective for datasets with high variance and non-linear distributions."
    - "Using predefined cluster centroids allows for expert judgment to guide the classification process."
    - "The proposed TOPSIS framework is computationally simple and easy to implement."
  limits:
    - "The definition of cluster centroids is based on expert judgment, introducing subjectivity."
    - "The method's performance on large-scale, high-dimensional datasets remains untested."
    - "The study does not compare its method against a wide array of modern optimization or machine learning baselines. [unacknowledged]"
    - "The applicability of the method to streaming or real-time data is not explored. [unacknowledged]"
  mapping_rationale: A systematic scan of all 12 functional domains was performed to map the paper's contributions to Odin's topics. The paper's core contribution is algorithmic and methodological, leading to the selection of topics under `12.A`, `12.B`, and `12.C` as `high` relevance, as it provides a framework for evaluating systems and algorithms. The case study's context of selecting an option based on multiple criteria (like cost) relates to `3.A` (`contextual`) and `7.A` (`low`). The method's ability to handle outliers directly informs the principles for anomaly detection (`8.A`, `8.B` - both `low`). The domain of "Behavioral Profiling" (`5.A`) was considered but rejected because the paper does not classify individuals. "Filipino Cultural Context" (`2.A`, `2.B`, `2.C`, `2.D`) was rejected as the case study is not culturally specific. The "Data Privacy" (`10.A`, `10.B`) and "Engagement" (`11.A`, `11.B`) domains were not addressed. The paper's overall relevance to Odin is high in its capacity to provide a robust, outlier-resistant, and expert-guided evaluation framework, which can be adapted for modules like budget recommendation and anomaly detection, despite its abstract, algorithm-focused nature.
limitations:
  - "The definition of ideal cluster centroids is based on expert judgment, introducing subjectivity."
  - "The method's performance on large-scale, high-dimensional datasets remains untested."
  - "The study does not compare its method against a wide array of modern optimization or machine learning baselines. [unacknowledged]"
  - "The applicability of the method to streaming or real-time data is not explored. [unacknowledged]"
remember_this:
  - "Logarithmic normalization in TOPSIS improves ranking stability with high-variance data."
  - "Fuzzy numbers enable the representation of uncertainty in expert-defined cluster profiles."
  - "The proposed clustering method is computationally simpler than Fuzzy K-Means."
  - "City K was more logically assigned to a cluster by the proposed method than by Fuzzy K-Means."
```
---


---

## Agent Instruction

If the agent reading this document believes further context about a paper is needed, it may request the original converted markdown file (with the '_marked' suffix) from the user for the relevant paper(s).
