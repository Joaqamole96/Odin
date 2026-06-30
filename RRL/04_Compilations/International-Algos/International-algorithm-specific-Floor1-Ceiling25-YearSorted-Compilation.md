# Compiled Research Summaries

## Filters Applied

- Designation: `international-algorithm-specific`

**Total Papers:** 25

**Note:** Included papers positions 1 to 25, Sorted by year.

---

## Paper 1: Jayaprakashnarayan et al_summarized.md

**Source File:** `Jayaprakashnarayan et al_summarized.md`

```yaml
paper_id: 10.15662/IJEETR.2026.0802073
designation: international-algorithm-specific
title: AI-Enabled NLP Framework for Automated Expense Management and Financial Analysis
authors: Jayaprakashnarayan, N.; Sakthivel, M.; Sachidhanandam, P.; Devi, N. Kanjana; Mughilan, T.S. Manivel
year: 2026
venue: International Journal of Engineering & Extended Technologies Research
odin_topics:
  - 3.A
  - 3.B
  - 3.C
  - 5.C
  - 6.A
  - 8.A
  - 8.B
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
tldr: A multi-task NLP framework using MuRIL and ensemble fraud detection automates expense tracking from financial SMS with 96.8% extraction accuracy and 91.7% fraud sensitivity.
problem_and_motivation: Digital payment proliferation generates fragmented financial notifications that overwhelm manual tracking. Existing systems fail to handle code-mixed languages, evolving message formats, and personalized spending patterns. A unified, adaptive NLP framework is needed for accurate, privacy-preserving expense management.
approach:
  - Framework integrates transformer-based language model (MuRIL) for contextual understanding of financial messages.
  - Multi-task learning architecture performs simultaneous entity extraction and transaction classification using shared representations.
  - Ensemble anomaly detection combines rule-based screening, statistical outlier detection, and LSTM autoencoders for fraud identification.
  - Online learning enables on-device personalization from user corrections without transmitting financial data.
  - Uncertainty-aware processing flags low-confidence extractions for human review, ensuring accuracy.
findings:
  - num: Entity extraction achieved 96.8% F1-score overall, with amount and date extraction exceeding 98%.
  - num: Transaction classification reached 94.9% weighted F1-score across 14 expense categories.
  - num: Ensemble fraud detection attained 91.7% sensitivity with 3.8% false positive rate.
  - num: On-device processing achieved 43-127ms latency with 0.9-2.0% hourly battery impact on commodity smartphones.
  - num: Multi-task learning improved entity extraction by 1.2% over single-task MuRIL fine-tuning.
  - Multi-layered security protocol includes account matching, duplicate detection, and encrypted local storage.
  - The framework processes code-mixed Hinglish text effectively, a challenge for English-only models.
  - Federated learning with differential privacy enables global model improvement without compromising user data.
key_figures_tables:
  - Table I: Dataset characteristics (124,583 messages, 42 banks, 18 UPI apps) → Diverse financial SMS corpus.
  - Table II: Entity extraction by type → Merchants hardest (95.2% F1), amounts easiest (98.8% F1).
  - Table IV: Classification per category → Shopping hardest (92.4% F1), income easiest (98.6% F1).
  - Table V: Fraud detection comparison → Ensemble best (91.7% sensitivity, 95.6% AUC).
  - Figure 2: Entity-level performance by type → Visualizes extraction difficulty variation.
key_equations:
  - equation: L = λ_entity L_entity + λ_class L_class
    explanation: Multi-task objective balancing entity and classification losses.
  - equation: H_token = -∑ p(t|x) log p(t|x)
    explanation: Token-level uncertainty measured as entropy of tag distribution.
  - equation: Margin = p(c1|x) - p(c2|x)
    explanation: Classification uncertainty via gap between top probabilities.
definitions:
  - term: MuRIL
    definition: Multilingual Representations for Indian Languages, a BERT model pre-trained on 17 Indian languages.
  - term: UPI
    definition: Unified Payments Interface, India's real-time payment system.
  - term: NLP
    definition: Natural Language Processing, enabling computers to understand human language.
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network for sequence modeling.
  - term: CRF
    definition: Conditional Random Field, a statistical modeling method for structured prediction.
critical_citations:
  - "[Devlin et al., 2019] — BERT transformer architecture for language understanding."
  - "[Khanuja et al., 2021] — MuRIL multilingual model for Indian languages."
  - "[Hochreiter and Schmidhuber, 1997] — LSTM foundations for sequence modeling."
  - "[Liu et al., 2023] — Financial named entity recognition benchmarks."
  - "[Ahmed and Mahmood, 2020] — Hybrid fraud detection ensemble methodology."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Proposes a multi-task classification system for 14 expense categories with 94.9% F1.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: high
      justification: Defines and evaluates a detailed 14-category taxonomy for personal finance.
    - code: 3.C
      name: User-Defined Allocation Constraints
      relevance: medium
      justification: Online learning enables personalization of category boundaries via user corrections.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Transaction classification and fraud detection infer spending behavior.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: low
      justification: Framework foundation for future predictive modules via sequential transaction modeling.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Ensemble fraud detection module directly addresses transaction anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Compares rule-based, statistical, and LSTM autoencoder anomaly detection methods.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: high
      justification: On-device processing and optimization for mobile constraints (latency, battery, memory).
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Uncertainty-aware UI and interactive dashboards enhance user experience.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: On-device processing, encryption, and differential privacy prevent data leakage.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Explainable AI and uncertainty flags build user trust and enable informed overrides.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Phased evaluation (component, end-to-end, longitudinal, UX) provides a rigorous framework.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Detailed component-level benchmarking of entity extraction, classification, and fraud detection.
  contribution: The paper directly informs Odin's expense categorization engine by providing a validated multi-task NLP architecture for parsing financial messages and classifying transactions into a detailed category taxonomy. Its ensemble fraud detection module offers a template for Odin's anomaly detection subsystem, incorporating rule-based, statistical, and deep learning components with uncertainty quantification. The privacy-preserving on-device processing and federated learning approach provide a blueprint for Odin's data security and personalization mechanisms. The rigorous component-level and longitudinal evaluation frameworks establish benchmarks for Odin's own algorithmic module testing. The mobile optimization strategies (quantization, pruning, latency/battery analysis) offer practical guidance for deploying Odin on resource-constrained devices in the Philippines.
  directly_justifies:
    - "Transformer-based models significantly outperform rule-based and recurrent baselines for financial entity extraction (F1 0.968 vs 0.888)."
    - "Multi-task learning with shared representations improves both entity extraction and classification performance."
    - "Ensemble fraud detection achieves 91.7% sensitivity with 3.8% false positive rate on personal transaction data."
    - "On-device deployment with quantization achieves 4× size reduction while preserving 98.7% accuracy."
    - "Uncertainty-aware processing prevents automation errors in ambiguous cases."
  limits:
    - "Dataset focused on Indian financial ecosystem; generalization to Philippine banks and payment systems untested."
    - "Model compression (quantization/pruning) sacrifices 1.3% accuracy for mobile deployment."
    - "Longitudinal adaptation study limited to 6 months; longer-term concept drift effects unexplored."
    - "Battery impact scales with transaction volume; heavy users may experience significant drain."
  mapping_rationale: Systematic scanning of all 12 functional domains and their associated topic codes flagged relevance primarily in Expense Categorization (3.A, 3.B, 3.C), Anomaly Detection (8.A, 8.B), Mobile-First Design (9.A, 9.B), Data Privacy (10.A, 10.B), and System Evaluation (12.A, 12.B). High relevance was assigned for topics directly addressed by core algorithms: 3.A (categorization framework), 8.A (anomaly detection system), 9.A (mobile optimization), 10.A (privacy architecture), and 12.B (algorithm evaluation). Medium relevance for 5.C (classification informing profiles), 3.C (personalization), 9.B (UX), 10.B (trust), and 12.A (evaluation framework). Low relevance for 6.A because predictive modeling is discussed as future work, not a primary contribution. Domains like Filipino Cultural Context (2.A-D), Behavioral Profiling (5.A-B), Budget Recommendation (7.A-D), Retention (11.A-B), and Savings/Debt (13.A-C) were rejected as not addressed. Borderline cases: 6.A was considered due to sequential modeling but is not a central prediction engine; 5.C was included for its classification methodology though not directly user profiling. Overall, the paper is highly relevant for Odin's algorithmic core, especially NLP-based parsing, classification, anomaly detection, and mobile-first secure architecture.
limitations:
  - "Geographic generalizability to Philippine banks and payment systems is untested. [unacknowledged]"
  - "Long-term performance after 6+ months without retraining is not evaluated. [unacknowledged]"
  - "Heavy transaction volumes may cause significant battery drain on low-end devices."
  - "Loss of 1.3% accuracy due to quantization may affect millions of transactions annually."
  - "Shopping category classification remains challenging (92.4% F1) due to merchant diversity."
remember_this:
  - "96.8% entity extraction accuracy using MuRIL multi-task learning on financial SMS."
  - "94.9% classification F1 across 14 expense categories with on-device personalization."
  - "91.7% fraud sensitivity with only 3.8% false positives via ensemble detection."
  - "Quantized models achieve 4× size reduction with 98.7% accuracy preservation."
  - "Uncertainty-aware processing flags low-confidence decisions for user review."
```
---

## Paper 2: Vinitha et al_summarized.md

**Source File:** `Vinitha et al_summarized.md`

```yaml
paper_id: 1b4e3c2d-5a6f-7b8c-9d0e-1f2a3b4c5d6e
designation: international-algorithm-specific
title: AI-Driven Personal Finance Management: Predictive Expense Forecasting and Behavioural Clustering
authors: Vinitha, C.; Krishna, A. H.; Reddy, E. M.; Javari, P.
year: 2026
venue: International Journal of Data Science and IoT Management System
odin_topics:
  - 3.A
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 7.B
  - 8.A
  - 12.B
  - 13.A
tldr: Combines LSTM forecasting and K-Means clustering to provide personalized expense predictions and spending behavior insights for improved financial decision-making.
problem_and_motivation: Manual financial tracking and basic budgeting tools fail to capture complex temporal dependencies and spending patterns, making accurate future expense prediction difficult. This leads to inefficient financial decisions and a lack of personalized, actionable insights for users. There is a need for an intelligent system that analyzes historical data to forecast expenses and understand underlying spending behavior.
approach:
  - Developed a Django-based web application with a MySQL database and email OTP authentication for secure access.
  - Applied K-Means clustering to expense categories and amounts to group similar spending behaviors and identify financial patterns.
  - Implemented an LSTM deep learning model to analyze historical daily expense data and generate future expense predictions, addressing non-linear trends and temporal dependencies.
  - Integrated VADER sentiment analysis to evaluate user feedback, classifying it as positive, negative, or neutral for continuous system improvement.
  - Used the predicted expenses to compute a surplus against a generated income approximation, providing investment or savings recommendations.
findings:
  - num: The LSTM model achieved an accuracy of 99.93% with a Mean Squared Error of 35.41 for predicting future expenses.
  - num: K-Means clustering successfully grouped transaction records into distinct expense behavior patterns based on category and amount.
  - The combined approach of prediction and clustering enables users to make informed budgeting and investment planning decisions.
  - The proposed system automates financial insights and provides personalized recommendations, addressing limitations of traditional financial tools.
key_figures_tables:
  - Figure 4: K-Means clustering results for expense behavior patterns → Identifies distinct spending clusters for better financial understanding.
  - Figure 5: LSTM model evaluation comparing predicted vs. actual expenses → Demonstrates high accuracy in forecasting.
  - Figure 6: Budget recommendation screen showing surplus calculation → Provides actionable investment suggestions based on predictions.
  - Figure 7: VADER sentiment analysis of user feedback → Classifies feedback to improve user interaction.
key_equations:
  - equation: "MSE = \\frac{1}{n} \\sum_{i=1}^{n} (y_i - \\hat{y}_i)^2"
    explanation: Loss function for evaluating LSTM prediction accuracy.
definitions:
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network capable of learning long-term dependencies in sequential data.
  - term: K-Means Clustering
    definition: An unsupervised learning algorithm that groups data points into k distinct clusters based on similarity.
  - term: VADER
    definition: Valence Aware Dictionary and sEntiment Reasoner, a rule-based sentiment analysis tool.
  - term: SMTP
    definition: Simple Mail Transfer Protocol, used for sending OTP authentication emails.
  - term: OTP
    definition: One-Time Password, a temporary passcode for user verification.
critical_citations:
  - "[Sirisha et al., 2022] — Benchmarks LSTM for profit prediction."
  - "[Shiyyab et al., 2023] — Discusses AI adoption and financial performance."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Uses K-Means clustering to categorize and group expenses.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Clustering analysis identifies distinct spending behavior patterns.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: K-Means is applied to classify expenses and uncover user financial profiles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Core contribution is the LSTM model for expense prediction.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: LSTM is specifically used for time-series forecasting of daily expenses.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: System provides a budget recommendation based on predicted expenses and estimated income.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Mentions detecting anomalies but does not focus on it as a primary feature.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Reports performance metrics (MSE and accuracy) for the LSTM module.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Surplus from predicted expenses is recommended as potential savings or investment.
  contribution: This paper provides a practical implementation of an LSTM model for expense forecasting, which can directly inform the design of Odin's predictive engine. The use of K-Means clustering for expense categorization offers a viable approach for behavioral profiling. The integration of these predictive and clustering techniques demonstrates a feasible pipeline for generating personalized financial insights and recommendations. The sentiment analysis module provides a model for incorporating user feedback into system iteration. The evaluation metrics presented validate the accuracy of the algorithmic components.
  directly_justifies:
    - An LSTM model can accurately forecast daily expenses, achieving 99.93% accuracy on test data.
    - K-Means clustering is effective for categorizing expenses into meaningful behavioral groups.
    - Combining expense prediction with surplus calculation can generate actionable investment or savings recommendations.
    - Secure authentication (OTP via SMTP) is a necessary feature for a personal finance management system.
  limits:
    - The evaluation is performed on a single dataset; generalizability to diverse spending patterns may be limited.
    - The paper does not thoroughly discuss the handling of infeasible budget recommendations or user-defined constraints.
    - The system's recommendation is based on a simple surplus calculation, lacking nuanced optimization strategies.
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The domains of Spending Forecasting (6), Behavioral Profiling & Classification (5), Budget Recommendation (7), and System Evaluation (12) were flagged as highly relevant due to the paper's focus on LSTM forecasting, K-Means clustering, and the reporting of model accuracy. The Expense Categorization (3) and Savings & Debt Management (13) domains were marked as medium, as the paper addresses expense grouping and mentions savings recommendations. The Anomaly Detection (8) domain was considered low because it is only briefly referenced. Domains related to Filipino Cultural Context (2), Mobile-First Design (9), Data Privacy (10), and User Retention (11) were rejected as they were not addressed in the paper. The paper's overall relevance to Odin is high as it provides concrete, algorithm-specific evidence for building a predictive and profiling system.
limitations:
  - The paper does not discuss the model's performance on irregular spending patterns or its robustness to data sparsity. [unacknowledged]
  - The integration of sentiment analysis is superficial and not directly linked to improving the core predictive modules. [unacknowledged]
  - The budget recommendation is simplistic and does not account for user-defined allocation constraints.
remember_this:
  - LSTM achieved 99.93% accuracy for financial expense prediction.
  - K-Means clustering groups expenses into meaningful behavioral categories.
  - Predictive insights are used to generate investment or savings recommendations.
  - System integrates secure OTP authentication via SMTP for user access.
  - User feedback is analyzed with VADER for continuous system improvement.
```
---

## Paper 3: Montagna_summarized.md

**Source File:** `Montagna_summarized.md`

```yaml
paper_id: 70d5269c-1cbd-5b71-afa6-86550a29e2e4
designation: international-algorithm-specific
title: Integration of Explainability in Recommender Systems to Enhance Enterprise Value Strategies
authors: Montagna, A.
year: 2026
venue: University of Padova
odin_topics:
  - 4.A
  - 4.B
  - 7.A
  - 7.B
  - 7.D
  - 9.A
  - 9.B
  - 10.A
  - 10.B
tldr: A comprehensive thesis that surveys Value-Aware Recommender Systems, proposes an explainable value-aware matrix factorization model, and critiques the evaluation of explanations in graph-based recommenders for enterprise contexts.
problem_and_motivation: Recommender systems are widely used but often lack transparency and fail to align with business value objectives. Value-aware systems exist but have not been systematically surveyed, and a key gap remains in balancing the generation of business value with the need for explainable, trustworthy recommendations. This research addresses this gap by creating a bridge between these perspectives through novel models and evaluation frameworks.
approach:
  - A systematic literature review following PRISMA guidelines was conducted to survey and classify Value-Aware Recommender Systems (VARSs), analyzing 109 studies.
  - A novel model, Explainable Value-aware Matrix Factorization (XVMF), is proposed to balance explainability and business value by integrating both terms into a unified objective function.
  - The model is evaluated on Yelp and Amazon datasets using NDCG, E-NDCG, and a novel NDCV metric to assess accuracy, explainability, and business value trade-offs.
  - A critical analysis of Graph-Based Explainable Recommender Systems (GxRSs) is performed, highlighting the lack of quantitative evaluation methods for explanation quality.
findings:
  - num: The systematic review identified 109 relevant studies on VARSs, which are classified into in-processing and post-processing techniques.
  - The proposed XVMF model successfully balances explainability and business value, achieving performance that exceeds baseline MF and EMF models on the Yelp dataset.
  - num: For the Yelp dataset, the XVMF model achieved an NDCV of 0.5042% and an E-NDCG of 1.9954%, outperforming the baseline models.
  - num: On the Amazon dataset, the XVMF-e model achieved an E-NDCG of 0.1723%, a significant improvement over EMF, while the XVMF-v model achieved an NDCV of 0.1154%.
  - A key finding is that the optimal balance between explainability and value is achieved at low regularization parameter values, after which performance degrades quickly.
  - The analysis of GxRSs reveals that most papers rely on qualitative case-based analyses, with only a few employing quantitative metrics for explanation evaluation.
  - The thesis proposes that future work on GxRSs should adopt standardized quantitative metrics to ensure comparability and rigorous evaluation.
key_figures_tables:
  - "Figure 2.1: PRISMA flow diagram summarizing the systematic literature review process → 109 studies were included in the final review."
  - "Figure 2.2: Taxonomy of value-aware recommender algorithms → Divides VARSs into in-processing and post-processing methods."
  - "Table 2.1: Application domains of value-aware recommender systems → Shows product, advertising, news, and media as key domains."
  - "Figure 3.1-3.4: Performance analysis for Yelp and Amazon datasets → Show the trade-off and optimal balance between explainability and value regularization."
  - "Table 3.5 and 3.6: Evaluation metrics for MF, EMF, and XVMF → XVMF outperforms baselines, particularly on the Yelp dataset."
key_equations:
  - equation: |
      G_{expl} = \sum_{u,i \in R} (r_{ui} - a_u b_i^T)^2 + \frac{\beta}{2} (\| a_u \|^2 + \| b_i \|^2) + \lambda \| a_u - b_i \|^2 E_{ui}
    explanation: Objective function for explainable matrix factorization, incorporating an explainability regularization term.
  - equation: |
      L = \sum_{(u,i) \in S} (r_{u,i} - p_u \cdot q_i^T)^2 + \frac{\beta}{2} (\| p_u \|^2 + \| q_i \|^2) + \| p_u - q_i \|^2 (\lambda W_{u,i} + \delta v_i)
    explanation: Objective function for the proposed XVMF model, balancing explainability and business value.
  - equation: |
      \text{NDCV} = \sum_{i=1}^{k} \frac{2^{rel_i} - 1}{\log_2 (i+1)}
    explanation: Novel metric to evaluate the business value of a recommendation list, based on the gain from the item's value.
definitions:
  - term: VARS
    definition: Value-Aware Recommender System, designed to directly maximize the economic value of recommendations.
  - term: xRS
    definition: Explainable Recommender System, which provides reasons or evidence for its recommendations.
  - term: XVMF
    definition: Explainable Value-aware Matrix Factorization, a novel model proposed in this thesis to balance explainability and business value.
  - term: E-NDCG
    definition: Explainable Normalized Discounted Cumulative Gain, a metric for evaluating the explainability quality of a ranked recommendation list.
  - term: NDCV
    definition: Normalized Discounted Cumulative Value, a novel metric proposed to evaluate the business value generated by a recommendation list.
  - term: GxRS
    definition: Graph-Based Explainable Recommender System, a system that uses graph structures to generate and explain recommendations.
  - term: MEP
    definition: Mean Explainability Precision, a quantitative metric to evaluate the explainability of recommendations.
critical_citations:
  - "[Page et al., 2021] — PRISMA guidelines for systematic reviews."
  - "[Ricci et al., 2022] — Overview of recommender systems techniques."
  - "[Abdollahi and Nasraoui, 2016] — Basis for explainable matrix factorization (EMF)."
  - "[Coba et al., 2019] — Basis for E-NDCG and NEMF model."
  - "[De Biasio et al., 2023] — The first systematic review of VARSs."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Surveys existing VARSs, providing a landscape of systems optimizing business value.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies the gap between business value optimization and explainability in current systems.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: Discusses business value optimization, a key driver for budget recommendation strategies.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: The thesis focuses on recommender systems in general, but the principles are transferable to budget recommendations.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: low
      justification: The XVMF model involves trade-offs between objectives, related to handling competing priorities.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Emphasizes the importance of human-centered design and trust in user adoption of AI systems.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: Discusses interface design for explanations, which is relevant to UX in general.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Focuses on trustworthy AI principles, including privacy and security.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: A central theme of the thesis is that explainability builds user trust and system adoption.
  contribution: "This thesis contributes to Odin's design by providing a systematic survey of value-aware systems, which can inform the development of Odin's budget recommendation and anomaly detection modules. The proposed XVMF model offers a concrete, data-driven approach for balancing user preference accuracy with business value, directly applicable to Odin's core functionality of generating personalized financial plans. Furthermore, the critical analysis of explanation evaluation in graph-based systems provides a methodological blueprint for ensuring that Odin's recommendations are not only accurate but also transparent and trustworthy. Finally, the emphasis on human-centered evaluation and user interfaces is crucial for designing Odin's mobile-first application to foster user engagement and trust."
  directly_justifies:
    - "The proposed XVMF model can be adapted to balance recommendation accuracy with Odin's business goals of user retention and savings growth."
    - "Systematic review of VARSs identifies key algorithms and datasets relevant for building Odin's value-optimization modules."
    - "Analysis of GxRSs highlights the need for quantitative explainability metrics, guiding Odin's evaluation framework."
  limits:
    - "The experimental validation of XVMF is limited to Yelp and Amazon datasets, which may not fully represent the financial behavior of Filipino young professionals."
    - "The qualitative limitations of existing explainability evaluations in GxRSs are noted, but a new comprehensive metric is not proposed."
    - "The thesis focuses on algorithm performance and does not include an end-to-end user study in a real-world business setting."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The 'Existing Systems & Gaps' domain was flagged as highly relevant (topics 4.A, 4.B), as the thesis directly surveys VARSs and identifies the specific gap in explainable value-aware systems. The 'Budget Recommendation' domain (topics 7.A, 7.B, 7.D) was considered relevant due to the focus on optimizing economic value and balancing competing objectives, though the application is not specific to budgeting. The 'Mobile-First Design' and 'Data Privacy & User Trust' domains (topics 9.A, 9.B, 10.A, 10.B) are medium to low relevance, as the thesis discusses trust and interface design in the context of explainability, which is a key principle for Odin. Domains like 'Filipino Cultural Context' (2.A-D), 'Expense Categorization' (3.A-C), 'Behavioral Profiling' (5.A-C), 'Spending Forecasting' (6.A-B), 'Anomaly Detection' (8.A-C), 'Engagement & Retention' (11.A-B), 'System Evaluation' (12.A-C), and 'Savings & Debt Management' (13.A-C) were considered and rejected as the thesis does not directly address these specific areas, focusing instead on recommender system algorithms and their evaluation in a general enterprise context. The overall relevance to Odin is high, as it provides both a foundational survey of value-aware systems and a novel model for balancing key performance objectives."
limitations:
  - "The systematic review is based on articles from specific databases and excludes non-English and unpublished works. [unacknowledged]"
  - "The datasets used for XVMF (Yelp, Amazon) do not contain Filipino user data, limiting direct applicability to the target demographic. [unacknowledged]"
  - "The evaluation of XVMF is offline and does not include online A/B testing or user studies to validate real-world performance. [unacknowledged]"
  - "The thesis criticizes the lack of quantitative evaluation in GxRSs but does not itself propose a new, comprehensive metric to address this gap."
remember_this:
  - "Value-aware recommender systems are a distinct class that directly optimize economic value."
  - "The XVMF model successfully balances explainability and business value on benchmark datasets."
  - "Offline evaluation metrics for business value and explainability are critical for model selection."
  - "Current graph-based explainable recommenders lack rigorous quantitative evaluation of their explanations."
  - "Balancing user trust and system adoption is a key challenge for enterprise recommender systems."
```
---

## Paper 4: Chandana et al_summarized.md

**Source File:** `Chandana et al_summarized.md`

```yaml
paper_id: 549d7af6-15d6-5c3f-b483-6c0f6de1b738
designation: international-algorithm-specific
title: PERSONAL FINANCE TRACKER WITH AI BASED EXPENSE PREDICTION
authors: Chandana, M.; Reddy, E. M.; Reddy, E. P.; Vaishnavi, I. S.; Vaishnavi, K.
year: 2026
venue: AMERICAN JOURNAL OF MANAGEMENT AND IOT MEDICAL COMPUTING
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 9.A
  - 9.B
  - 12.A
  - 12.B
tldr: An AI-powered finance tracker using Flask, MySQL, Random Forest, and LSTM to forecast expenses, detect anomalies, and automatically categorize transactions for enhanced user financial awareness.
problem_and_motivation: Existing expense trackers passively record data without providing predictive insights or personalized budgeting guidance. Users need intelligent systems that analyze behavioral patterns to offer actionable financial foresight. This project addresses the gap between simple tracking and proactive financial management.
approach:
  - The system is built with Python and Flask for the backend, MySQL for data storage, and a frontend using HTML, CSS, and JavaScript with Chart.js.
  - Historical transaction data is preprocessed to remove nulls, encode categorical features, and normalize numerical values for model input.
  - A Random Forest classifier is used to automatically categorize transactions into predefined groups such as food, travel, and bills.
  - An LSTM neural network is applied for time-series forecasting to predict future monthly expenses based on past spending behavior.
  - Anomaly detection algorithms analyze spending trends to identify unusual patterns or sudden spikes in expenditure.
  - A real-time dashboard visualizes income, expense distribution, and predictions through charts and graphs to improve user understanding.
  - User authentication and session management secure access and isolate individual financial data within the MySQL database.
  - The system was tested on both sample and real transaction datasets to evaluate the performance of its core modules.
findings:
  - The LSTM model achieved approximately 85% accuracy in forecasting next-month expenses.
  - The Random Forest classifier achieved over 90% accuracy in automatically categorizing financial transactions.
  - The anomaly detection module successfully identified sudden spending spikes and irregular transactions with good accuracy.
  - Users found the dashboard interface easy to understand and the visual insights improved their financial awareness.
  - Predicted values from the LSTM model closely matched actual spending patterns for most categories.
  - The system proved more effective than manual or static trackers by providing accurate predictions and helpful alerts for unusual expenses.
key_figures_tables:
  - Figure 1: System architecture overview of the AI-powered tracker → Shows the integration of modules with LSTM and Random Forest.
  - Figure 2: Flask-based ML dashboard flow → Illustrates the technical workflow from user input to insights and storage.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network used for time-series forecasting in this system.
  - term: AI
    definition: Artificial Intelligence, used for predictive analysis and automation in the finance tracker.
critical_citations:
  - "[Kaur and Singh, 2022] — AI-based expense prediction using ML."
  - "[Patel and Sinha, 2021] — Random Forest and LSTM for expenditure analysis."
  - "[Bhattacharya, 2023] — Automated finance tracking with data analytics."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Implements Random Forest for automated expense classification.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: Uses predefined categories (food, travel) and visualizes them.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Reviews limitations of traditional static trackers as a baseline.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly addresses the lack of predictive and analytical features in existing systems.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Core contribution is forecasting future expenses using LSTM.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Uses LSTM specifically for time-series expense prediction.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Includes a module to identify unusual spending patterns and generate alerts.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Mentions anomaly detection techniques but provides limited algorithmic detail.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: contextual
      justification: The web-based system could inform mobile-first design but is not the focus.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: Mentions an intuitive dashboard but focuses on web, not mobile UX specifically.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Presents accuracy results and user-friendliness evaluations.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides quantitative accuracy metrics for both classification and prediction modules.
  contribution: The paper provides a practical implementation of a predictive finance tracker, demonstrating how LSTM and Random Forest can be integrated into a web application. It justifies the use of these algorithms for Odin's expense prediction (6.A, 6.B) and categorization modules (3.A). Its evaluation framework (12.A, 12.B) offers a template for testing similar modules, while its anomaly detection component (8.A, 8.B) validates the need for proactive spending alerts.
  directly_justifies:
    - The LSTM model achieves 85% accuracy in forecasting monthly expenses.
    - The Random Forest classifier attains over 90% accuracy in automated transaction categorization.
    - Anomaly detection can effectively identify sudden spending spikes for user alerts.
    - Users respond positively to dashboards that present predictive and categorized financial insights.
  limits:
    - The dataset used for testing is not clearly described, making reproducibility difficult. [unacknowledged]
    - Lack of comparison against a robust set of baseline or state-of-the-art models. [unacknowledged]
    - No explicit discussion of privacy-preserving techniques for handling sensitive financial data. [unacknowledged]
    - The system is a web application, and no discussion is provided on how its design translates to a mobile-first experience. [unacknowledged]
  mapping_rationale: A systematic scan was conducted across all 12 functional domains for this paper. The domain of 'Expense Categorization' was flagged as highly relevant (3.A, 3.B) due to the Random Forest classifier. 'Spending Forecasting' was also high (6.A, 6.B) given the LSTM model. 'Anomaly Detection' (8.A, 8.B) was relevant due to the dedicated module. 'Existing Systems & Gaps' (4.A, 4.B) was identified as contextual/high as the motivation explicitly critiques traditional systems. 'System Evaluation' (12.A, 12.B) was medium/high due to reported accuracy metrics. The 'Mobile-First Design' domain (9.A, 9.B) was considered but rejected to low/contextual as the work is web-focused and does not address mobile-specific challenges. 'Data Privacy' and 'User Retention' were considered and rejected as they are not discussed. The paper's overall relevance to Odin is moderate, as it validates the technical feasibility and impact of predictive and categorical modules, which are core components of the system.
limitations:
  - The paper does not specify the size or source of the dataset used for validation. [unacknowledged]
  - No comparison is made with other forecasting models like XGBoost or Transformer-based networks. [unacknowledged]
  - The anomaly detection method lacks algorithmic detail, making its performance difficult to assess. [unacknowledged]
  - The evaluation focuses on accuracy and usability but does not test the system's performance under varying data distributions. [unacknowledged]
remember_this:
  - LSTM achieved 85% accuracy in forecasting monthly expenses.
  - Random Forest automatically categorized transactions with over 90% accuracy.
  - Anomaly detection provided effective early warnings for unusual spending.
  - The system transformed a passive tracker into an intelligent predictive assistant.
  - The dashboard improved user financial awareness through clear visualizations.
```
---

## Paper 5: Patel & Singh_summarized.md

**Source File:** `Patel & Singh_summarized.md`

```yaml
paper_id: 5c8f3d6e-8b1a-5a2b-9c4d-7e6f8a9b0c1d
designation: international-algorithm-specific
title: An Intelligent AI-Based Framework for Automated Personal Financial Management
authors: Patel, A.; Singh, A.
year: 2026
venue: International Conference on Multidisciplinary Perspectives in Advanced Computing and Technology (IMPACT 2026)
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 9.A
  - 9.B
  - 10.A
  - 11.A
  - 11.B
tldr: Integrates AI and full-stack technology to aggregate financial data, classify transactions, forecast spending, and deliver personalized budgeting recommendations and alerts.
problem_and_motivation: Digital financial services generate fragmented personal data that manual tracking cannot efficiently manage. Existing applications lack intelligent automation and personalized decision support, creating a gap between raw data and informed financial decisions, especially for young professionals.
approach:
  - Collects financial data from multiple digital sources like UPI and banking records using secure APIs.
  - Preprocesses and normalizes raw transaction data for consistency and analysis.
  - Classifies transactions automatically using a hybrid of rule-based logic and machine learning algorithms.
  - Employs statistical and time-series methods to analyze spending patterns and forecast future expenditures.
  - Implements an event-driven background workflow for periodic report generation and AI analysis.
findings:
  - AI-driven classification enhanced accuracy in categorizing transactions compared to manual procedures.
  - The system aggregates financial information from different platforms into a unified real-time interface.
  - The budgeting module analyzes previous spending to generate personalized budget limits.
  - Alert notifications inform users when spending approaches or exceeds predefined thresholds.
  - Predictive insights enable users to anticipate future expenditures and improve financial planning.
  - Interactive dashboards and simplified statements improved user financial understanding and engagement.
key_figures_tables:
  - Figure 1: Monthly expense breakdown by category → Shows automated categorization and spending distribution.
  - Figure 2: Income and expense analysis dashboard → Visualizes aggregated financial data for user insights.
  - Table 1: Methodology phases → Outlines data collection, preprocessing, categorization, and visualization steps.
  - Table 2: Result analysis comparison → Demonstrates performance improvements over traditional tools.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: None.
    definition: ""
critical_citations:
  - "[Grass & Lynch, 1982] — foundational resource for financial workshop proceedings."
  - "[Naik et al., 2024] — discusses automated expense tracking systems."
  - "[Stefanov et al., 2024] — covers personal finance management application design."
  - "[Fernández, 2019] — reviews AI applications in financial services."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Proposes ML and rule-based automated transaction categorization.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: Discusses classification into categories like food, travel, bills.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Reviews traditional systems and identifies their limitations.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Explicitly outlines lack of intelligence, automation, and integration.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Implements forecasting of future expenditures based on historical data.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Uses time-series analysis and regression for expense prediction.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Provides adaptive budgeting based on spending behavior analysis.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Generates personalized budget limits and recommendations.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Mentions detection of anomalies in spending patterns indirectly.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Does not focus on a specific anomaly detection algorithm.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: Suggests future deployment as a cross-platform mobile application.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: Mentions user engagement but not specific mobile UX design details.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Emphasizes secure storage and management of financial information.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Claims improved user engagement through alerts and analytics.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: low
      justification: Discusses notifications but not specific retention mechanisms.
  contribution: The paper provides a modular architecture integrating AI for automated transaction categorization and predictive analytics, which directly informs Odin's expense tracking module. Its emphasis on aggregating fragmented data from multiple digital payment sources supports Odin's data integration layer design. The adaptive budgeting and alert system offers a blueprint for Odin's recommendation engine. The discussion of security and privacy considerations provides foundational justification for Odin's data protection protocols. Overall, the framework demonstrates how AI can enhance user financial awareness and decision support.
  directly_justifies:
    - Automated transaction categorization using rule-based and ML techniques is feasible and improves accuracy.
    - Aggregating financial data from multiple sources into a single platform enhances financial awareness.
    - Predictive analytics on historical spending data can enable effective future expense forecasting.
    - Personalized budget recommendations based on spending behavior promote better financial discipline.
    - Real-time alerts and visual analytics increase user engagement and sound financial decision-making.
  limits:
    - The system's performance depends on the quality of input data and reliability of third-party services. [unacknowledged]
    - Direct bank API integration for real-time synchronization is not fully implemented and is noted as future work.
    - The study does not provide quantitative performance metrics from a large-scale user study.
    - Security measures are discussed generally, without detailing specific encryption or blockchain implementations.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was conducted. Domains relevant to expense categorization (3.A, 3.B), existing systems (4.A, 4.B), forecasting (6.A, 6.B), and budgeting (7.A, 7.B) were flagged as high relevance because the paper directly addresses these with proposed algorithms and system features. Domains like anomaly detection (8.A, 8.B) and engagement (11.A, 11.B) were assigned medium or low relevance, as they are mentioned but not the core focus. The paper's general nature led to rejecting culturally specific domains (2.A-D) and Filipino demographic topics (1.A-C). The paper's contribution is overall highly relevant to Odin's architectural and algorithmic modules.
limitations:
  - Direct bank API-UPI gateway integration for real-time synchronization is not fully implemented. [unacknowledged]
  - Deep learning algorithms for expense forecasting are suggested but not incorporated in the current framework. [unacknowledged]
  - Features like investment analysis, credit score evaluation, and debt management are outside the system's scope. [unacknowledged]
  - The system has not been deployed as a cross-platform mobile application for large-scale testing. [unacknowledged]
  - Relies on the accuracy and availability of third-party AI and data ingestion services.
remember_this:
  - Integrates rule-based and ML for accurate automated transaction categorization.
  - Aggregates fragmented data from multiple digital payment platforms into one view.
  - Uses historical spending to forecast future expenses and personalize budgets.
  - Real-time alerts and interactive dashboards enhance financial discipline and awareness.
  - Reduces manual effort and improves financial transparency compared to traditional tools.
```
---

## Paper 6: Rafiaei_summarized.md

**Source File:** `Rafiaei_summarized.md`

```yaml
paper_id: 2d8a3b1c-5e4f-4a2b-9c7d-8f1e3a5b7c9d
designation: international-algorithm-specific
title: Keyword Matching vs. LLM-Based Classification for Personal Finance Transaction Categorization: A Benchmark Study on Real Canadian Bank Data
authors: Rafiaei, M.
year: 2026
venue: Unknown
odin_topics:
  - 3.A
  - 5.C
  - 6.A
  - 12.A
  - 12.B
  - 4.A
  - 8.A
tldr: A benchmark study of transaction classification on Canadian bank data finds LLMs outperform keyword matching by 51 percentage points and resolve structural limitations including context blindness and coverage decay.
problem_and_motivation: Automatic transaction categorization is central to personal finance software, yet the dominant keyword-based approach exhibits uneven performance across account types. No prior work has studied the performance gap on real Canadian bank data or provided a statistically validated comparison with LLMs.
approach:
  - Constructed a labeled dataset of 7,152 transactions from two account holders, five accounts across two Canadian banks (CIBC and BMO), spanning 4.5 years (September 2021 – April 2026).
  - Implemented a priority-ordered keyword dictionary classifier with 45 patterns, routed by account type, following the inverted-index retrieval model.
  - Experiment 1: Controlled benchmark on 200 CIBC chequing transactions comparing keyword matching to Claude (claude-3-5-sonnet-20241022) in a zero-shot regime.
  - Experiment 2: Exploratory scale-up on all 7,152 transactions using Llama-3.1-8B and Llama-3.3-70B via Groq API, with ground-truth labels generated by the MonIQ rule-based import parser.
  - Conducted formal structural analysis of three keyword classifier limitations and proposed a hybrid cascade architecture.
findings:
  - num: Keyword classifier achieved 96.3% category F1 on credit card but only 27.5% on chequing, a 69 percentage point structural gap.
  - num: In the controlled benchmark, Claude achieved 96.5% type accuracy versus 45.5% for keyword matching, a +51.0 percentage point improvement (McNemar's χ²=81.06, p<0.001).
  - num: Claude raised Transfer F1 from 0% to 99.0%, Fees F1 from 13.7% to 100%, and Insurance F1 from 0% to 100%.
  - num: Llama-3.3-70B achieved 71.9% type accuracy and 42.8% category accuracy on the full dataset, with Transfer F1 rising from 40.1% (8B) to 57.9% (70B), establishing Transfer classification as the single most diagnostic metric.
  - Three root causes account for all chequing keyword errors: transfer-fee ambiguity (67.1%), income-expense context dependence (12.6%), and incomplete merchant coverage (20.4%).
  - LLMs resolve all three structural limitations of keyword matching: context blindness, coverage decay, and priority collision.
key_figures_tables:
  - Figure 1: Precision, recall, and F1 definitions with numerical example from Transfer category data → Defines metrics used in the evaluation.
  - Figure 2: Per-category F1 scores, keyword classifier, CIBC evaluation subset (N=2,222) → Visualization of the 69pp gap between credit card and chequing.
  - Figure 3: Failure mode breakdown of 868 errors in keyword classification → Identifies transfer-fee ambiguity as dominant (67.1%).
  - Figure 4: Hybrid cascade classifier architecture → Keyword handles high-confidence cases; LLM escalates ambiguous chequing transactions (~20-30%).
  - Table VI: Llama model size comparison on full dataset (Exploratory) → Shows model-size effect on Transfer F1 (40.1% to 57.9%).
key_equations:
  - equation: f(d) = γ(k_i*) where i* = min{i : k_i ⊆ d}; f(d) = c_default if no match
    explanation: Keyword classifier definition: priority-ordered dictionary matching.
  - equation: F1 = 2·TP/(2·TP+FP+FN)
    explanation: F1 calculation for imbalanced category distributions.
definitions:
  - term: PFMS
    definition: Personal Finance Management System
  - term: LLM
    definition: Large Language Model
  - term: F1
    definition: Harmonic mean of precision and recall, ranges from 0 to 1
  - term: Transfer F1
    definition: F1 score specifically for the Transfer category classification
critical_citations:
  - "[Lesner et al., 2019] — Large-scale production system for personalized categorization"
  - "[García-Méndez et al., 2020] — SVM for banking transaction descriptions"
  - "[Kotios et al., 2022] — Hybrid rule-based and ML categorization model"
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Directly benchmarks and compares categorization methods (keyword vs. LLM) for personal finance transactions.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Evaluates classification approaches (keyword matching and LLMs) for categorizing financial transactions, which underpin behavioral profiling.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Provides a foundation for accurate transaction data that informs predictive modeling, though not directly about forecasting.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Offers a benchmark methodology and statistical validation framework for evaluating classification modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Directly evaluates and compares algorithmic modules (keyword classifier and LLMs) with statistical rigor.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Mentions existing systems (Mint, YNAB, Monarch Money) and their reliance on keyword matching.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: The formal analysis of classification failures could inform anomaly detection by identifying ambiguous or misclassified transactions.
  contribution: This paper provides a labeled dataset and benchmark for transaction classification on Canadian bank data, with a statistically validated comparison showing LLMs outperform keyword matching. The findings justify Odin's adoption of LLM-based or hybrid classification for chequing accounts to improve accuracy. The formal analysis of keyword limitations provides a theoretical foundation for designing robust categorization modules. The identification of Transfer classification as the most diagnostic metric directly informs Odin's evaluation strategy for classification algorithms. The cost-accuracy tradeoff analysis and hybrid cascade proposal offer a practical design pathway for Odin's expense categorization module.
  directly_justifies:
    - LLMs resolve structural limitations of keyword matching including context blindness and coverage decay.
    - Transaction classification accuracy on chequing accounts is fundamentally limited by description format, not tuning.
    - A hybrid cascade architecture can achieve high accuracy with acceptable latency and cost.
    - Transfer category F1 is the single most diagnostic metric for evaluating classification performance.
  limits:
    - Controlled benchmark uses a 200-transaction stratified sample from one CIBC chequing account.
    - Experiment 2 ground-truth labels were generated by a keyword parser, introducing circular dependence for Llama evaluation.
    - Results may not generalize across all Canadian banks or account holder demographics.
    - No cross-user generalization tests were performed on the BMO accounts.
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The Expense Categorization (3.A) and Classification Approaches (5.C) domains were flagged as high relevance due to the paper's direct benchmarking of transaction classification methods. Behavioral Profiling (5.A) and Forecasting (6.A) were considered medium relevance as accurate categorization is foundational but not the primary focus. System Evaluation (12.A/B) was flagged as high because the paper provides a rigorous evaluation framework with statistical validation. Existing Systems (4.A) was considered low as the paper only references them. Anomaly Detection (8.A) was contextual because while failure analysis could inform anomaly detection, it is not explicitly addressed. Budget Recommendation (7.A-D), Savings & Debt Management (13.A-C), Mobile-First Design (9.A-B), Data Privacy (10.A-B), User Retention (11.A-B), and Filipino Cultural Context (2.A-D) were rejected as they are not addressed. The paper's overall relevance to Odin is high for its classification module design and evaluation methodology.
limitations:
  - Controlled benchmark uses a 200-transaction stratified sample from one CIBC chequing account [unacknowledged].
  - Experiment 2 ground-truth labels were generated by a keyword parser, introducing circular dependence for Llama evaluation [unacknowledged].
  - Results may not generalize across all Canadian banks or account holder demographics.
  - No cross-user generalization tests were performed.
  - Hybrid cascade architecture is estimated, not empirically validated [unacknowledged].
remember_this:
  - Keyword matching achieves 96.3% F1 on credit cards but only 27.5% on chequing.
  - Claude achieves 96.5% type accuracy versus 45.5% for keyword matching.
  - Transfer classification is the most diagnostic metric for this task.
  - LLMs resolve all three structural limitations of keyword matching.
  - A hybrid cascade can balance accuracy, latency, and cost.
```
---

## Paper 7: Sireesha et al_summarized.md

**Source File:** `Sireesha et al_summarized.md`

```yaml
paper_id: 3b5f9c8e-6d4a-4f2e-8b1c-9a7d6e5f4c3b
designation: international-algorithm-specific
title: AI-Based Personal Finance Manager
authors: Sireesha, B.; Kumar, K. K.; Lavanya, O.; Keshan, S.; Ramsai, N.; Kumar, K. L.
year: 2026
venue: International Journal of AI Electronics and Nexus Energy
odin_topics:
  - 3.A
  - 3.B
  - 4.B
  - 6.A
  - 6.B
  - 7.B
  - 8.A
  - 8.B
  - 12.A
  - 10.A
  - 10.B
  - 11.A
tldr: An AI-based personal finance manager uses machine learning and deep learning to automate expense categorization, forecast spending, and provide personalized financial recommendations.
problem_and_motivation: Users struggle to monitor spending and make informed financial decisions due to limited time, financial literacy, and analytical tools. AI provides an effective solution by enabling automated, personalized, and data-driven financial management.
approach:
  - Data is collected from banking statements, e-commerce receipts, and user inputs.
  - Preprocessing includes cleaning, normalization, tokenization, and category mapping.
  - Random Forest and neural networks classify transactions into categories like food and rent.
  - An LSTM model predicts future expenses and revenue based on historical patterns.
  - The system uses Isolation Forest for anomaly detection and a hybrid model combining rule-based logic, supervised ML, and reinforcement learning for recommendations.
findings:
  - num: The Random Forest expense classifier achieved 93–96% accuracy.
  - num: Traditional rule-based systems plateau at around 75–80% accuracy.
  - num: The LSTM forecasting model achieved a Mean Absolute Error (MAE) of 4.7%.
  - num: Anomaly detection demonstrated a precision of 92%.
  - num: 84% of users reported better spending awareness, and 78% claimed increased savings control.
key_figures_tables:
  - "Table 1: Accuracy comparison of ML models → Random Forest outperforms traditional rule-based systems."
  - "Table 2: LSTM forecasting performance → MAE of 4.7% for monthly expenditure prediction."
key_equations:
  - equation: "MAE = (1/n) * Σ|y_i - ŷ_i|"
    explanation: "Mean Absolute Error for LSTM forecasting accuracy."
definitions:
  - term: "LSTM"
    definition: "Long Short-Term Memory, a recurrent neural network for time-series prediction."
  - term: "Random Forest"
    definition: "An ensemble learning method for classification and regression."
  - term: "Isolation Forest"
    definition: "An anomaly detection algorithm that isolates outliers."
critical_citations:
  - "[Patel and Kumar, 2022] — AI-driven personal finance automation."
  - "[Chen et al., 2022] — Deep learning for financial forecasting."
  - "[Singh and Sharma, 2021] — LSTM for expense prediction."
  - "[Zhao, 2021] — Isolation Forest for financial anomaly detection."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: "Evaluates Random Forest and neural networks for classifying transactions."
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: "Discusses mapping transactions to categories like food, rent, and utilities."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: "Explicitly compares AI system against static, rule-based tools and their limited personalization."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: "Uses LSTM for time-series financial prediction."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: "Applies LSTM to forecast monthly expenditures and recurring payments."
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: "Recommendation engine suggests savings, budget adherence, and expense reduction."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: "Uses Isolation Forest to detect unusual transactions and overspending."
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: "Evaluates Isolation Forest precision for fraud prevention."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: "Presents usability study with 50 participants and quantitative metrics."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: "Mentions security concerns and blockchain for tamper-proof logs as future work."
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: "Uses explainable AI to improve transparency and user trust."
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: "Reports improved user engagement and satisfaction metrics."
  contribution: "This paper directly justifies the use of a hybrid AI architecture (Random Forest, LSTM, and reinforcement learning) for Odin's predictive modeling and recommendation modules. The high accuracy of expense classification (93–96%) provides a strong empirical basis for Odin's categorization engine. The LSTM forecasting results (MAE 4.7%) support the development of a reliable forecasting module for cash flow prediction. The usability study findings validate the need for personalized, real-time financial insights to enhance user engagement and retention."
  directly_justifies:
    - "Random Forest classifiers can achieve 93–96% accuracy in expense categorization."
    - "LSTM models provide reliable forecasts with a 4.7% MAE for monthly expenditures."
    - "Anomaly detection using Isolation Forest can achieve 92% precision."
    - "Real-time alerts help users avoid unnecessary spending."
    - "User satisfaction increases with personalized budget recommendations."
  limits:
    - "The study was conducted with a limited dataset and 50 participants for usability. [unacknowledged]"
    - "Long-term performance and adaptability of the models are not evaluated. [unacknowledged]"
    - "The paper does not address cold-start scenarios for new users. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains identified the Expense Categorization, Forecasting, and Recommendation domains as highly relevant due to the paper's direct evaluation of ML models for these tasks. The Anomaly Detection domain was flagged as medium relevance due to the evaluation of Isolation Forest. The System Evaluation domain was deemed high relevance because of the reported quantitative metrics (accuracy, MAE, precision) and usability study. Data Privacy and User Trust were considered low to medium relevance because the paper mentions explainable AI and security only briefly, without detailed analysis. Domains like Filipino Cultural Context, Behavioral Profiling, Savings & Debt Management, and Mobile-First Design were rejected as the paper does not address these specific aspects. Overall, the paper is highly relevant to Odin's algorithmic core."
limitations:
  - "The dataset size and diversity are not fully specified, which may affect generalizability. [unacknowledged]"
  - "The study does not address the cold-start problem for new users. [unacknowledged]"
  - "There is no discussion of model fairness or bias across different user demographics. [unacknowledged]"
remember_this:
  - "Random Forest achieved 93–96% accuracy for expense categorization."
  - "LSTM forecasting achieved a 4.7% Mean Absolute Error."
  - "Anomaly detection precision reached 92% with Isolation Forest."
  - "84% of users reported better spending awareness."
  - "The system combines supervised, deep, and reinforcement learning."
```
---

## Paper 8: Rabinovich et al_summarized.md

**Source File:** `Rabinovich et al_summarized.md`

```yaml
paper_id: "5f4e3d2c-1b0a-9f8e-7d6c-5b4a3f2e1d0c"
designation: "international-algorithm-specific"
title: "Mapping Financial Mindsets: A Two-Stage Unsupervised Framework for Behavioral Profiling Using High-Dimensional Psychometric Data"
authors: "Rabinovich, I.; Rabinovich, R.; Ashburn, N.; DeGeare, M."
year: 2026
venue: "Unknown"
odin_topics:
  - "5.A"
  - "5.B"
  - "5.C"
  - "10.B"
  - "12.A"
  - "12.B"
tldr: "A two-stage unsupervised framework combining manifold learning and spectral clustering identifies psychologically interpretable financial behavioral profiles from psychometric data."
problem_and_motivation: "Financial well-being is multidimensional, yet segmentation approaches overlook psychological traits. There is a gap in modeling interactions across psychometric domains to reveal latent financial mindsets. This limits personalized financial tools and interventions that account for behavioral heterogeneity."
approach:
  - "Stage 1 derives unidimensional domain scores via anchor-based projection, weighted averages, or simple averages depending on domain structure."
  - "Stage 2 applies UMAP to domain scores followed by spectral clustering to identify behavioral profiles."
  - "The framework is evaluated on a proprietary psychometric dataset (N=337) and the nationally representative CFPB Financial Well-Being Survey (N=5,897)."
  - "Hyperparameters are tuned via randomized search optimizing trustworthiness, continuity, silhouette score, Calinski-Harabasz index, and Davies-Bouldin index."
  - "Cluster stability is assessed via 100 random seeds and subsampling, and external validity is tested against independent outcomes."
findings:
  - "num: 79.2% accuracy achieved in assigning new individuals to learned profiles using a soft-voting classifier."
  - "num: Cluster membership explains 19-61% of variance in life satisfaction, psychological well-being, and financial health in the proprietary dataset."
  - "num: Cluster membership explains 14-44% of variance in life satisfaction, material hardship, and financial health in the CFPB dataset."
  - "Demographic variables alone provide limited predictive power for cluster membership (McFadden pseudo-R² = .061-.091)."
  - "The framework reveals interpretable, psychologically coherent profiles that are not captured by linear or demographic segmentation approaches."
key_figures_tables:
  - "Figure 1: UMAP projections show clear cluster separation in both datasets → Clusters are spatially distinct and interpretable."
  - "Figure 3: Heatmaps of mean domain scores reveal distinctive cluster-level profiles across domains → Profiles are psychologically coherent."
  - "Figure 5: Variance explained by clusters exceeds that of demographics for subjective outcomes → Profiles capture behavioral-psychological structure beyond SES."
  - "Figure 6: Cluster centroids align along a global functioning axis across datasets → Framework captures shared latent structure."
  - "Table 5a/5b: Descriptive cluster profiles range from low capability to highly resourced → Profiles reflect distinct behavioral pathways."
key_equations:
  - equation: "s_i = [(p_i - v_min^e) · (v_max^e - v_min^e)] / ||v_max^e - v_min^e||^2"
    explanation: "Orthogonal projection of participant embedding onto anchor axis for domain scoring."
  - equation: "CPSI_{i,j} = 1 / (1 + d(i,j))"
    explanation: "Normalized inverse-distance measure for cross-dataset cluster similarity."
definitions:
  - term: "UMAP"
    definition: "Uniform Manifold Approximation and Projection, a nonlinear dimensionality reduction technique."
  - term: "Spectral Clustering"
    definition: "A graph-based clustering method that uses eigenvalues of a similarity matrix."
  - term: "Anchor-based projection"
    definition: "Scoring method projecting participant embeddings onto an axis defined by theoretical anchor profiles."
  - term: "CFPB"
    definition: "Consumer Financial Protection Bureau, a U.S. government agency."
critical_citations:
  - "[Kahneman & Tversky, 1979] — Foundational for behavioral finance and non-rational decision-making."
  - "[Lusardi & Mitchell, 2011] — Provides validated financial literacy measurement items."
  - "[Ryan & Deci, 2017] — Theoretical basis for motivation domain in the proprietary dataset."
  - "[McInnes et al., 2018] — Introduces UMAP, the core dimensionality reduction method."
  - "[Ng et al., 2002] — Foundational for spectral clustering algorithm used."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "The paper's core contribution is identifying distinct financial behavioral profiles using unsupervised learning."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "high"
      justification: "Section 4.8 addresses cold-start assignment of new individuals to learned profiles using a classifier."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "The framework uses a two-stage unsupervised approach and validates classification performance."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "medium"
      justification: "Interpretable profiles can support trust by providing transparent explanations for personalization."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "The study uses internal validation metrics and external outcome associations, providing an evaluation framework."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Cluster stability is assessed via random seeds and subsampling, validating algorithmic reproducibility."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Background section reviews existing financial well-being assessments and their limitations."
    - code: "9.A"
      name: "Mobile‑First Design Principles and Rationale"
      relevance: "contextual"
      justification: "The framework is discussed as applicable to fintech platforms, but mobile-specific design is not addressed."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "contextual"
      justification: "Profiles could inform engagement strategies, but the paper does not directly study engagement dynamics."
  contribution: "This paper directly informs Odin's behavioral profiling module (5.A, 5.B, 5.C) by providing a validated two-stage unsupervised framework for identifying financial mindsets. The classifier for assigning new users to profiles supports Odin's cold-start problem (5.B). The interpretable profiles can inform personalized budget recommendations (7.B) and engagement strategies (11.A) by aligning system behavior with user psychology. The framework's validation methodology also provides a template for evaluating Odin's algorithmic modules (12.B)."
  directly_justifies:
    - "A two-stage unsupervised framework can identify psychologically interpretable financial behavioral profiles."
    - "Demographic variables alone do not substantially account for the clustering structure."
    - "Cluster membership explains more variance in financial health and life satisfaction than demographics alone."
    - "A supervised classifier can assign new users to learned profiles with 79.2% accuracy."
    - "The framework reveals shared latent structure across different instruments and populations."
  limits:
    - "Both datasets are cross-sectional, preventing assessment of profile dynamics over time."
    - "All measures are self-reported, which may introduce response biases."
    - "The proprietary dataset is modest in size and drawn from a convenience sample."
    - "The framework involves analytic design choices that can influence the resulting structure."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated canonical topic codes was performed. Domains directly related to behavioral profiling (5.A, 5.B, 5.C) were flagged as high relevance because the paper's core contribution is identifying financial behavioral profiles using unsupervised learning and addressing cold-start assignment. Domains related to system evaluation (12.A, 12.B) were assigned medium relevance due to the comprehensive validation framework used. The data privacy domain (10.A) was considered but rejected because the paper does not address privacy mechanisms. The expense categorization (3.A, 3.B, 3.C) and budget recommendation (7.A-D) domains were rejected as the paper focuses on profiling rather than categorization or optimization. The forecasting domain (6.A, 6.B) was rejected because the paper does not model spending sequences. The mobile-first design domain (9.A, 9.B) was considered contextual because the framework is discussed as applicable to fintech but mobile-specific considerations are absent. The Filipino cultural context (2.A-D) was not applicable given the U.S.-focused datasets. Overall, the paper provides strong methodological support for behavioral profiling and moderate support for evaluation frameworks, but limited direct relevance to other Odin modules."
limitations:
  - "Both datasets are cross-sectional, precluding assessment of profile dynamics over time. [unacknowledged]"
  - "All measures are self-reported, which may be influenced by response styles. [unacknowledged]"
  - "The proprietary dataset is modest in size and drawn from a convenience sample. [acknowledged]"
  - "The framework involves analytic design choices that can influence the resulting structure. [acknowledged]"
  - "The framework's generalizability to other populations and domains requires further validation. [acknowledged]"
remember_this:
  - "Two-stage framework with UMAP and spectral clustering reveals interpretable financial profiles."
  - "Cluster membership explains up to 61% of variance in financial health outcomes."
  - "Demographics alone explain only 6-9% of cluster membership variance."
  - "A classifier can assign new individuals to profiles with 79.2% accuracy."
  - "The framework captures shared latent structure across different survey instruments."
```
---

## Paper 9: Balbal & Birant_summarized.md

**Source File:** `Balbal & Birant_summarized.md`

```yaml
paper_id: 10.3390/app16052223
designation: international-algorithm-specific
title: RFM-Net: A Convolutional Neural Network for Customer Segment Classification
authors: Balbal, K.F.; Birant, D.
year: 2026
venue: Applied Sciences
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 12.A
  - 12.B
tldr: Integrates RFM analysis with a custom CNN to classify customers into predefined behavioral segments using structured transactional data.
problem_and_motivation: Traditional RFM-based segmentation relies on rule-based logic that may not capture nonlinear patterns in customer behavior. Existing statistical and clustering approaches often lack the adaptability required for dynamic markets. There is a need for a robust, intelligent, and scalable technique that combines domain knowledge with data-driven learning.
approach:
  - Uses the UCI Online Retail dataset with 541,909 records from a UK-based retailer.
  - Transforms raw transactional data into Recency, Frequency, and Monetary (RFM) features.
  - Discretizes continuous RFM values into 1-5 scores using user-defined thresholds.
  - Applies a rule-based scheme to label customers into seven segments (e.g., Champions, At Risk) using RFM scores.
  - Trains a custom, lightweight CNN (RFM-Net) on the labeled data to learn the mapping from RFM values to segments.
  - Evaluates model performance using 10-fold cross-validation and metrics like accuracy, precision, recall, and F-measure.
findings:
  - num: The proposed RFM-Net achieved a classification accuracy of 94.33% on the test set.
  - num: RFM-Net demonstrated a relative average increase of 13.17% in accuracy compared to previous studies on the same dataset.
  - Recency was identified as the most important feature for prediction, followed by Frequency and Monetary.
  - The lightweight CNN architecture with only 6,823 parameters proved efficient and prevented overfitting.
  - Model performance was consistent across two different retail datasets (Online Retail I and II), showing robustness.
key_figures_tables:
  - Table 7: Performance metrics across 10 folds → Average accuracy of 94.33% with high precision and recall.
  - Figure 3: Distribution of customer segments → Potential Loyalists form the largest group (23.70%).
  - Figure 4: Feature importance analysis → Recency is the most significant predictor of customer segment.
  - Figure 5: Confusion matrix → High classification accuracy for most segments, with minor confusion between adjacent groups.
  - Figure 6: Training and validation loss → Loss curves converge, indicating effective learning and generalization.
key_equations:
  - equation: R_c = (d_ref - d_last^c).days
    explanation: Calculates days since customer's last purchase.
  - equation: F_c = | {x.InvoiceNo | ∀x ∈ T_c } |
    explanation: Counts distinct purchase events per customer.
  - equation: M_c = ∑_{x∈T_c} (x.Quantity × x.UnitPrice)
    explanation: Sums total spending per customer.
definitions:
  - term: RFM
    definition: Recency, Frequency, and Monetary; a framework for customer behavior analysis.
  - term: CNN
    definition: Convolutional Neural Network; a deep learning model for feature extraction.
  - term: RFM-Net
    definition: Proposed CNN model designed for customer segmentation using RFM features.
  - term: Champions
    definition: Most active and profitable customers with high R, F, and M scores.
critical_citations:
  - "[Christy et al., 2021] — Introduces RFM ranking for customer segmentation."
  - "[Chen et al., 2012] — Source of the UCI Online Retail dataset used in the study."
  - "[Talaat et al., 2023] — Previous work on RFM and deep learning for segmentation."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: The paper's core task is classifying customers into behavioral profiles (e.g., Champions, At Risk).
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: contextual
      justification: While not explicitly on cold-start, the method uses rule-based labels, indirectly addressing the challenge of initial profile creation.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: The paper proposes a novel classification approach (CNN) for financial behavioral profiles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Customer segment prediction is a form of predictive modeling applicable to spending behavior.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: contextual
      justification: The RFM features are derived from sequential transaction data, though the paper focuses on classification rather than forecasting.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: The paper uses standard metrics (accuracy, precision, recall) applicable to evaluating system modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: The paper provides a detailed evaluation of the proposed RFM-Net algorithm against baseline models.
  contribution: "RFM-Net provides a methodological template for classifying users into strategic behavioral segments using only RFM features, which can be integrated into Odin's behavioral profiling engine. The high accuracy of the model (94.33%) justifies the use of supervised learning for personal finance categorization tasks where ground-truth labels are derived from expert-defined rules. The lightweight CNN architecture demonstrates that effective segmentation is possible with minimal computational resources, supporting Odin's mobile-first design principle. The feature importance analysis, showing Recency as the strongest predictor, guides the design of Odin's engagement and retention features."
  directly_justifies:
    - "A lightweight CNN can achieve high accuracy (94.33%) for segmenting users based on RFM features."
    - "Recency is the most important behavioral indicator for predicting future engagement."
    - "Supervised learning can effectively learn expert-defined segmentation rules from structured financial data."
    - "The CNN architecture acts as an implicit regularizer, improving generalization on tabular data."
  limits:
    - "The study relies on predefined thresholds for discretizing RFM values, which may not be optimal for all user populations."
    - "The model was evaluated on retail transaction data, not on personal finance management logs, so generalizability to Odin's context is not directly established."
    - "The labels are derived from the same RFM scores used as features, introducing a degree of circularity in the modeling process."
  mapping_rationale: "The systematic scan across Odin's 12 functional domains flagged three domains as highly relevant: Behavioral Profiling & Classification (Topic 5), Spending Forecasting (Topic 6), and System Evaluation (Topic 12). The paper's central contribution—a CNN model for customer segmentation—directly informs Topics 5.A, 5.B, and 5.C, with 'high' relevance assigned due to its novel classification approach for behavioral profiles. Topic 6 (Predictive Modeling & Forecasting) was considered relevant but only at a 'medium' or 'contextual' level, as the paper focuses on classification rather than sequence forecasting, though its RFM features derive from temporal data. Topic 12 (System Evaluation) received 'high' relevance for its evaluation framework and 'medium' for its comparison against baselines. Domains like Filipino Cultural Context (2), Expense Categorization (3), Mobile-First Design (9), and Data Privacy (10) were considered and rejected, as the paper does not address cultural practices, categorization taxonomies, mobile constraints, or privacy concerns. The paper's overall relevance to Odin is significant for its behavioral modeling and classification methodologies, offering a computationally efficient approach to segmenting users based on spending patterns."
limitations:
  - "Circularity: Segment labels are derived from the same RFM scores that serve as model input. [unacknowledged]"
  - "Threshold generalizability: The optimal RFM thresholds were empirically determined for the specific retail dataset and may not generalize to other domains or user populations. [unacknowledged]"
  - "Domain gap: The dataset is from a retail e-commerce context, which may not fully represent the complexities of personal financial management. [unacknowledged]"
  - "Interpretability: The 'black box' nature of the CNN may present challenges for explaining model decisions to end-users, despite being more interpretable than deeper networks. [unacknowledged]"
remember_this:
  - The RFM-Net achieves 94.33% accuracy in customer classification.
  - Recency is the most important feature for segment prediction.
  - A lightweight CNN prevents overfitting on low-dimensional data.
  - Rule-based labeling enables supervised learning of behavioral profiles.
  - The model performs effectively on structured, tabular data.
```
---

## Paper 10: Han & Lai_summarized.md

**Source File:** `Han & Lai_summarized.md`

```yaml
paper_id: 10.69987/JACS.2026.60403
designation: international-algorithm-specific
title: Temporal Feature Engineering and Threshold Optimization for Early Warning in Healthcare Claims Anomaly Detection
authors: Han, M.; Lai, J.
year: 2026
venue: Journal of Advanced Computing Systems
odin_topics:
  - 6.B
  - 8.B
  - 12.A
  - 10.A
  - 9.A
tldr: Systematic temporal feature engineering and adaptive threshold optimization significantly improve early-warning anomaly detection in healthcare claims.
problem_and_motivation: Healthcare fraud causes massive financial losses, but existing detection methods often miss subtle temporal patterns or generate excessive false alarms. The temporal dimension of claims data remains underutilized, limiting early warning capabilities.
approach:
  - This paper develops a framework to extract 127 temporal features from Medicare Part B claims, including service intervals, submission patterns, and frequency distributions.
  - Feature construction combines statistical analysis, functional principal component analysis, and LSTM autoencoder embeddings to capture multi-scale temporal dependencies.
  - The paper proposes an adaptive threshold optimization methodology that dynamically adjusts detection boundaries based on performance feedback and concept drift.
  - The approach is evaluated on a dataset with 47.3 million claims from 892,450 providers, comparing against baseline statistical and RFM features.
  - The framework includes cost-sensitive optimization, Pareto frontier analysis, and context-aware adjustments for seasonal and specialty variations.
findings:
  - num: The proposed framework achieved a detection rate of 0.87 and false positive rate of 0.06, improving over baseline rates of 0.73 and 0.14.
  - num: The adaptive threshold framework outperformed static approaches, maintaining stable performance (detection rate variation within 0.03) over 12 months.
  - num: The cost-benefit analysis identified an optimal threshold at 0.60, generating net annual savings of 8.2 million dollars in the study's setting.
  - Service-to-submission lag standard deviation and weekend submission ratio were the most important temporal features for fraud detection.
  - LSTM autoencoder embeddings provided a 0.06 improvement in detection rate over statistical features alone.
  - The adaptive framework responded to concept drift with an average latency of 8.3 days, preventing performance degradation seen in fixed thresholds.
key_figures_tables:
  - Figure 1: Temporal billing frequency distributions for legitimate, early-stage, and sophisticated fraud providers → Fraud patterns show distinct frequency spikes and periodicities.
  - Figure 2: LSTM autoencoder embedding space visualization → Fraudulent providers cluster at the periphery, distinct from legitimate providers.
  - Figure 3: Threshold performance trade-off curves → Optimal cost-savings balance occurs at threshold 0.60 with 79% detection rate and 3% false positive rate.
  - Figure 4: Adaptive threshold evolution and performance tracking → Dynamic adjustments maintain performance within acceptable ranges across drift events.
  - Table 7: Cost-benefit analysis for threshold selection → Threshold 0.60 yields the highest net benefit at 315.6 million dollars.
key_equations:
  - equation: D_KL(P||Q) = Σ P(x)·log(P(x)/Q(x))
    explanation: KL divergence measures difference between provider and reference temporal distributions.
  - equation: EWMA_t = α·x_t + (1-α)·EWMA_{t-1}
    explanation: Exponentially weighted moving average emphasizes recent billing patterns.
definitions:
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network for sequential data.
  - term: FPCA
    definition: Functional Principal Component Analysis, for capturing dominant modes of temporal variation.
  - term: ROC
    definition: Receiver Operating Characteristic, a curve showing detection trade-offs.
  - term: RFM
    definition: Recency-Frequency-Monetary features, measuring recent activity and spending.
  - term: CMS
    definition: Centers for Medicare & Medicaid Services, the US federal agency.
critical_citations:
  - "[Ahmed et al., 2016] — Survey of temporal anomaly detection methods."
  - "[Malhotra et al., 2015] — LSTM networks for time-series anomaly detection."
  - "[Bauder & Khoshgoftaar, 2023] — Cost-sensitive learning for insurance fraud."
relevance:
  topics:
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: This paper evaluates forecasting-relevant temporal modeling techniques like LSTM for anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Core contribution is an anomaly detection framework for temporal claims data, directly applicable to spending patterns.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides a rigorous evaluation methodology with cost-benefit analysis and ROC curves.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Discusses de-identified data use but does not focus on privacy-preserving techniques.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: contextual
      justification: Mentions real-time processing but does not address mobile-specific design.
  contribution: This paper's temporal feature engineering framework can inform Odin's anomaly detection module by providing a methodology for extracting patterns from sequential spending data. The adaptive threshold optimization approach offers a strategy for Odin to balance detection sensitivity with user alert fatigue. The cost-sensitive evaluation framework provides a template for assessing the financial impact of Odin's recommendations. The importance of features like service intervals and frequency distributions can guide the selection of attributes for Odin's behavioral profiling. The concept drift handling methods are relevant for Odin's adaptation to changing user spending habits over time.
  directly_justifies:
    - "Temporal features like service-to-submission lag are critical for identifying anomalous patterns in sequential data."
    - "Adaptive thresholding based on performance feedback improves detection stability over time."
    - "Cost-benefit analysis is essential for optimizing alert thresholds in resource-constrained settings."
    - "LSTM-based embeddings can capture complex dependencies in spending sequences."
  limits:
    - "The evaluation is limited to Medicare Part B fee-for-service data and may not generalize to other payment models."
    - "The fraud labels depend on completed investigations, introducing a temporal lag that may affect early warning evaluation."
    - "The ground-truth labels may reflect enforcement priorities and could miss novel fraud schemes."
  mapping_rationale: This paper was systematically scanned against all 12 functional domains and their associated topic codes. The core contribution on anomaly detection algorithms (8.B) and forecasting algorithms (6.B) was flagged as high relevance, as the paper directly addresses predictive modeling for sequential claims data. The evaluation framework (12.A) was assigned medium relevance, as the paper provides rigorous performance and cost-benefit analysis methods. Data privacy (10.A) was considered low relevance, as the paper uses de-identified data but does not focus on privacy techniques. Mobile-first design (9.A) was flagged as contextual only, as the paper mentions real-time processing but does not address mobile UX. Other domains like Filipino cultural context, expense categorization, and savings/debt management were rejected as not applicable. The paper's overall relevance to Odin is moderate: its methodological contributions on temporal feature engineering and adaptive thresholding for anomaly detection are directly transferable to Odin's core modules, but the specific domain context differs.
limitations:
  - "The evaluation relies on a single payer's (Medicare) claims data and may not generalize to other contexts."
  - "The ground-truth fraud labels introduce temporal lag and selection bias. [unacknowledged]"
  - "Computational requirements for deep learning features may limit accessibility for smaller organizations. [unacknowledged]"
  - "Threshold optimization assumes stable cost parameters which may vary in practice. [unacknowledged]"
  - "Interpretability of deep learning representations remains challenging. [unacknowledged]"
remember_this:
  - "Temporal features significantly improve anomaly detection over baseline methods."
  - "Adaptive thresholds maintain stable performance under concept drift."
  - "Feature importance analysis identifies submission lag as the most critical signal."
  - "Cost-benefit analysis is crucial for practical threshold selection."
  - "num: The framework improved detection rate by 0.14 over baseline approaches."
```
---

## Paper 11: Unde et al_summarized.md

**Source File:** `Unde et al_summarized.md`

```yaml
paper_id: 10.1555/ijarp.6353
designation: international-algorithm-specific
title: AI-BASED REAL-TIME PERSONAL FINANCE DASHBOARD
authors: Unde, S. P.; Ghule, A. B.; Jaware, R. S.; Kanawade, S. N.; Koli, Y. K.
year: 2026
venue: International Journal Advanced Research Publication
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.B
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 9.A
  - 9.B
  - 10.A
  - 11.A
  - 12.A
  - 12.B
  - 12.C
tldr: An AI-driven dashboard integrates real-time data ingestion, BERT-based categorization, and autoencoder anomaly detection to automate personal finance management and provide predictive insights.
problem_and_motivation: Digital payment proliferation fragments financial data across platforms, while manual tracking tools are time-consuming and error-prone. Existing systems lack real-time, proactive intelligence for automated categorization, anomaly detection, and forecasting. An integrated, automated dashboard is needed to unify data and enable intelligent financial oversight.
approach:
  - Data is ingested via banking APIs, webhooks, and an OCR module using CNNs (YOLOv4) for receipt digitization.
  - A preprocessing pipeline cleans data, normalizes features, and applies NLP tokenization to transaction descriptions.
  - A fine-tuned BERT model is used for automated expense categorization into domains like utilities and groceries.
  - A dual anomaly detection engine uses Isolation Forests and Conditional Autoencoders to flag point and contextual outliers.
  - LSTM networks forecast cash flows, and linear programming or LLM optimization generates dynamic savings recommendations.
findings:
  - num: Fine-tuned BERT model achieves 90-95% categorization accuracy, outperforming traditional keyword-based systems.
  - num: The system reduces manual data entry effort by over 80% through automated API and OCR integration.
  - Conditional Autoencoders successfully identify contextual outliers (e.g., duplicate subscriptions) with a low false-positive rate.
  - LSTM-based forecasts provide superior predictive accuracy for future savings trajectories and cash flows.
  - Users of the AI dashboard exhibit more disciplined spending habits due to automated alerts and real-time goal progress visualization.
key_figures_tables:
  - Figure 1: System architecture diagram illustrating four-layer pipeline → Overview of data flow from ingestion to presentation.
  - Figure 2: Project plan timeline → Visual representation of development phases and milestones.
  - Table 1: Performance comparison between traditional systems and proposed dashboard → Proposed AI dashboard metrics show higher accuracy, lower effort, and proactive functionality.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: API
    definition: Application Programming Interface, used for secure data ingestion from financial institutions.
  - term: BERT
    definition: Bidirectional Encoder Representations from Transformers, a deep learning model for natural language understanding.
  - term: CNN
    definition: Convolutional Neural Network, used for image feature extraction in OCR.
  - term: LSTM
    definition: Long Short-Term Memory network, a recurrent neural network for time-series forecasting.
  - term: NLP
    definition: Natural Language Processing, used for processing transaction text descriptions.
  - term: OCR
    definition: Optical Character Recognition, technology for digitizing text from physical receipts.
  - term: UPI
    definition: Unified Payments Interface, a real-time payment system in India.
critical_citations:
  - "[Patil and Jadhav, 2025] — Hybrid ML for automated expense classification."
  - "[Kharat, 2025] — Validates BERT for categorization and LSTM for forecasting."
  - "[Inzirillo and De Villelongue, 2023] — Autoencoder for anomaly detection."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Directly proposes BERT-based automated categorization of transactions.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: high
      justification: Discusses categorization into domains like utilities and groceries for dashboard design.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews existing systems and their limitations (manual tracking, fragmentation).
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies gaps like lack of real-time insights and intelligent automation.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: low
      justification: Touch on user behavior and spending habits, but does not address cold-start.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Uses LSTM for predictive cash flow forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: LSTM specifically chosen for sequential spending data forecasting.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Discusses budget monitoring and goal-based savings automation.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: LLM/linear programming for optimizing savings and adjusting spending limits.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Proactive anomaly detection is a core feature.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Implements Isolation Forest and Conditional Autoencoders for this purpose.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: Mentions a web interface but does not focus on mobile-first principles.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: Lacks detailed discussion on mobile UX design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Addresses secure API data flow and integrity, but not extensively.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Automated alerts and visualization foster engagement and awareness.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides a comparative analysis between traditional and proposed systems.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Evaluates categorization accuracy and anomaly detection performance.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Evaluates budget management and savings adherence improvements.
  contribution: This paper directly justifies Odin's core modules by demonstrating the effectiveness of a unified, automated dashboard. The BERT-based categorization validates Odin's expense classification approach. The dual autoencoder/Isolation Forest anomaly detection engine supports Odin's proactive security layer. The LSTM forecasting and LLM-optimized savings modules align with Odin's predictive budgeting and recommendation features. Overall, the proposed architecture provides a blueprint for Odin's integrated, real-time financial management system.
  directly_justifies:
    - Automated expense categorization using BERT can achieve over 90% accuracy.
    - Conditional Autoencoders are effective for detecting contextual outliers in spending data.
    - LSTM networks provide superior accuracy for forecasting future cash flows.
    - Reducing manual data entry by over 80% significantly improves user engagement.
    - An AI-driven dashboard can directly improve savings adherence through automated alerts.
  limits:
    - The performance of the OCR module is dependent on receipt image quality.
    - Accuracy of categorization is reliant on the consistency of bank API data.
    - The study does not address the cold-start problem for new users with no historical data.
  mapping_rationale: A systematic scan across all 12 functional domains was executed. The paper was flagged as highly relevant for Expense Categorization (3.A, 3.B), Existing Systems (4.B), Predictive Modeling (6.A, 6.B), Budget Recommendation (7.B), and Anomaly Detection (8.A, 8.B) due to its direct proposal of BERT, LSTM, and autoencoder-based solutions. Medium relevance was assigned to domains like Landscape (4.A), Engagement (11.A), and Evaluation (12.A, 12.B, 12.C) for its review context and comparative analysis. Topics like Filipino Cultural Context (2.A-D) and Mobile-First Design (9.A, 9.B) were considered but rejected as the paper is geographically unbound and focuses on a general web interface rather than mobile-specific UX. The paper's overall relevance to Odin is high as it provides empirical evidence for several core algorithmic modules, though it is from a general international context.
limitations:
  - Performance depends on receipt image quality and API data consistency. [unacknowledged]
  - Does not address the cold-start problem for new users.
remember_this:
  - BERT-based categorization achieves 90-95% accuracy.
  - The system reduces manual effort by over 80%.
  - Conditional Autoencoders detect contextual outliers effectively.
  - LSTM forecasting enables dynamic budget adjustments.
  - An AI dashboard promotes disciplined spending through automation.
```
---

## Paper 12: Liu et al_summarized.md

**Source File:** `Liu et al_summarized.md`

```yaml
paper_id: "00000000-0000-0000-0000-000000000000"
designation: "international-algorithm-specific"
title: "Proteus: Shapeshifting Desktop Visualizations for Mobile via Multi-level Intelligent Adaptation"
authors: "Liu, C.; Cheng, S.; Liang, F.; Jiang, Z.; Huang, L.; Athapaththu, K.; Wang, Y."
year: 2026
venue: "ACM Designing Interactive Systems Conference (DIS'26)"
odin_topics:
  - "4.A"
  - "4.B"
  - "9.A"
  - "9.B"
  - "12.A"
  - "12.B"
tldr: "Proteus automates desktop-to-mobile visualization adaptation using a multi-level design space and LLM-driven multi-agent system, improving readability and interaction on small screens."
problem_and_motivation: "Desktop visualizations are designed for large screens, but mobile consumption is growing. Existing responsive techniques treat adaptation as a layout puzzle, lacking semantic understanding and hierarchical constraint handling. An automated approach that re-authors visualizations for mobile is needed."
approach:
  - "Constructed a multi-level design space (global topology, reference frame, visual elements) to model hierarchical adaptation constraints."
  - "Developed Proteus, an LLM-driven multi-agent system with Semantic Parser, Data Extractor, Design Planner, Frontend Engineer, and Visual Critic agents."
  - "The system parses desktop HTML/SVG, recovers data, plans transformations, generates TypeScript components, and iteratively refines based on critic feedback."
  - "Evaluated on 67 real-world web visualizations from Vega, Vega-Lite, Altair, and D3 galleries."
  - "Conducted a user study with 12 participants comparing Proteus to a strong multi-agent LLM baseline without the design space knowledge."
findings:
  - "num: Proteus achieved a render success rate of 91.8% compared to 87.8% for the baseline."
  - "num: Proteus significantly outperformed the baseline in data fidelity (p<0.05) and text readability (p<0.05)."
  - "num: Interaction reasonableness and visual aesthetics were significantly better (p<0.001)."
  - "The multi-level design space enables semantic re-authoring, such as converting static small multiples into interactive carousels."
  - "The critic agent is essential for convergence; without it, the system often fails to produce functional mobile variants."
  - "The system preserves data fidelity and improves readability by applying operations like tick decimation, label externalization, and layout serialization."
key_figures_tables:
  - "Figure 1: Multi-level design space (global topology, reference frame, visual elements) → hierarchical adaptation constraints."
  - "Figure 2: Proteus multi-agent architecture → automated adaptation pipeline with iterative refinement."
  - "Figure 3: Case studies on five real-world visualizations → effective adaptation across chart types."
  - "Figure 4: User study results → significant improvements over baseline in all five dimensions."
  - "Figure 5: Comparison examples → Proteus better preserves data and provides more reasonable interactions."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "LLM"
    definition: "Large Language Model"
  - term: "SVG"
    definition: "Scalable Vector Graphics"
  - term: "DOM"
    definition: "Document Object Model"
critical_citations:
  - "[Hoffswell et al., 2020] — established design space for responsive visualization."
  - "[Wu et al., 2020] — MobileVisFixer automates SVG layout repair."
  - "[Kim et al., 2022] — Cicero declarative grammar for responsive visualization."
relevance:
  topics:
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Surveys responsive visualization techniques and automated systems relevant to PFMS UI."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Identifies gaps in geometry-centric, flat-taxonomy approaches and proposes semantic re-authoring."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "high"
      justification: "Proposes a multi-level design space specifically for mobile adaptation, informing mobile-first UI design."
    - code: "9.B"
      name: "Mobile UX Design for Personal Finance"
      relevance: "contextual"
      justification: "Provides general mobile visualization UX principles, applicable to PFMS but not domain-specific."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "User study methodology with comparative evaluation can inform evaluation of PFMS systems."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Evaluates the algorithmic adaptation pipeline, relevant for assessing PFMS algorithmic components."
  contribution: "The paper's multi-level design space provides a framework for mobile-first design in Odin's UI. Its identification of gaps in existing responsive visualization techniques justifies Odin's need for semantic re-authoring. The iterative agent-based approach can inspire Odin's design for adaptive and intelligent user interfaces. The evaluation methodology offers a template for assessing Odin's mobile UX and algorithmic modules."
  directly_justifies:
    - "Geometry-centric adaptation fails to preserve semantic meaning on mobile screens."
    - "Hierarchical constraint propagation is needed to handle cross-level dependencies in mobile adaptation."
    - "Automated semantic re-authoring improves readability and interaction over simple resizing."
    - "LLM-driven multi-agent systems can effectively automate complex design tasks."
  limits:
    - "The study focuses on web visualizations, not specifically on personal finance data or Filipino context."
    - "Task-oriented analytical equivalence was not evaluated; only perceptual and usability metrics were used."
    - "Long-tail bespoke visualizations may not decompose cleanly into the proposed operators."
  mapping_rationale: "Systematic scan across all 12 functional domains: flagged 4.A (landscape) and 4.B (gaps) because the paper surveys existing responsive techniques and identifies limitations; 9.A (mobile-first design) and 9.B (mobile UX) because the paper proposes a design space and principles for mobile adaptation; 12.A and 12.B (evaluation) because the paper includes a user study and algorithmic evaluation. Borderline cases: 9.B is contextual as it is not specific to personal finance. Rejected domains: 1,2,3,5,6,7,8,10,11,13 as no mention of Filipino culture, spending, forecasting, budget, anomaly, privacy, engagement, or savings/debt. Overall, the paper is highly relevant to Odin's mobile UI design and evaluation methodology."
limitations:
  - "The current implementation operates on vector-based specifications, not raster images."
  - "Long-tail of bespoke designs may not be handled well by the predefined operators."
  - "User study focuses on perceived quality, not task completion or analytical outcomes."
  - "No direct comparison with MobileVisFixer or Cicero due to different task settings."
remember_this:
  - "Proteus achieved 91.8% render success on 67 real-world visualizations."
  - "Multi-level design space enables semantic re-authoring beyond geometric resizing."
  - "LLM-driven multi-agent system with critic feedback iteratively refines mobile adaptations."
  - "Significant improvements in readability, interaction, and aesthetics over baseline."
```
---

## Paper 13: Wu Y. et al_summarized.md

**Source File:** `Wu Y. et al_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international-algorithm-specific
title: "Test-Time Adaptation for Non-stationary Time Series: From Synthetic Regime Shifts to Financial Markets"
authors: "Wu, Y.; Deng, Q.; Chung, W.; Li, M."
year: 2026
venue: "Unknown"
odin_topics:
  - "6.A"
  - "6.B"
  - "8.A"
  - "12.B"
  - "5.B"
  - "12.A"
tldr: "Evaluates small-footprint test-time adaptation for time series forecasting under non-stationarity, finding that batch-normalization statistics refresh is a safe default while aggressive norm-only updates can hurt financial market predictions."
problem_and_motivation: "Real-world time series are non-stationary, causing forecasting models trained on past data to lose accuracy during deployment. Existing test-time adaptation methods lack clear guidance for streaming time series, especially in noisy financial markets where aggressive adaptation can degrade performance. A practical framework that balances adaptation benefit with stability is needed."
approach:
  - "Freezes backbone model and updates only normalization affine parameters (gamma, beta) using recent unlabeled windows."
  - "For classification, minimizes entropy and enforces temporal consistency via weak time-preserving augmentations."
  - "For regression, minimizes prediction variance across augmentations and optionally distills from an EMA teacher."
  - "Adds quadratic drift penalty to constrain inter-day parameter changes and uses uncertainty-triggered fallback to batch-normalization statistics refresh."
  - "Evaluates on synthetic regime shifts on ETT benchmarks and daily equity/FX series (SPY, QQQ, EUR/USD) across pandemic, high-inflation, and recovery regimes."
findings:
  - "num: Batch-normalization statistics refresh (bn_stats) improves direction accuracy on QQQ by 2.2 percentage points and on EUR/USD by 0.4 percentage points."
  - "num: Norm-only adaptation improves forecast error on ETT synthetic gradual drift but decreases direction accuracy on QQQ from 0.503 to 0.463."
  - "Diebold-Mariano tests show bn_stats significantly outperforms no_tta on SPY (DM=-2.781, p=0.0054) and QQQ (DM=-2.290, p=0.0220)."
  - "Structuralswitches in periodic components remain challenging, with norm-only updates yielding R2 of -0.02 and bn_stats yielding -20.80 on ETTh1."
  - "Uncertainty-triggered fallback mitigates harmful norm-only updates, improving stability in noisy financial regimes."
  - "EMA-teacher self-distillation reduces variance of adapted parameters, complementing augmentation-variance minimization for regression."
  - "Norm-only updates are effective for smooth low-order moment shifts but overfit short noisy windows in financial markets."
  - "Backtest shows bn_stats achieves highest Sharpe ratio (1.930 on SPY, 4.080 on QQQ) while norm_only underperforms the frozen baseline."
key_figures_tables:
  - "Table 1: Representative ETTh1 results under synthetic shifts → Norm-only improves gradual drift but fails on structural switches."
  - "Table 2: Directional accuracy on equity/FX → bn_stats has best average rank (1.66), norm_only second (2.00), no_tta worst (2.33)."
  - "Table 3: Diebold-Mariano tests → bn_stats significantly better than no_tta on all markets; norm_only worse on SPY/QQQ."
  - "Table 4-5: SPY/QQQ backtest performance → bn_stats yields higher Sharpe ratios; norm_only underperforms no_tta."
  - "Figure 2: Rolling forecast metrics on ETTh1 under gradual drift → norm-only reduces errors in later horizon segments."
  - "Figure 3: Rolling direction accuracy and RMSE for SPY/QQQ/EURUSD → TTA gains concentrated in pandemic and early recovery periods."
key_equations:
  - equation: "L_ent = -1/|B| sum_{X in B} sum_c p_c(X) log p_c(X)"
    explanation: "Entropy minimization sharpens classification posteriors."
  - equation: "L_cons = 1/|B| sum_{X in B} ||p(X) - p(T(X))||^2"
    explanation: "Consistency penalizes sensitivity to weak time-preserving transforms."
  - equation: "L_var = 1/|B| sum_{X in B} Var({y(T_k(X))}_{k=1}^K)"
    explanation: "Variance minimization reduces local Lipschitz constant of regressor."
  - equation: "L_sd = 1/|B| sum_{X in B} ||y_theta(X) - y_tilde(X)||^2"
    explanation: "Self-distillation anchors predictions to EMA teacher."
  - equation: "L_drift = gamma ||theta(t) - theta(t-1)||^2"
    explanation: "Drift penalty shrinks inter-day parameter changes."
definitions:
  - term: "TTA"
    definition: "Test-time adaptation, updating model parameters using unlabeled test inputs."
  - term: "BN"
    definition: "Batch normalization, normalizes hidden activations using batch statistics."
  - term: "RevIN"
    definition: "Reversible instance normalization, standardizes sequences and reverses before output."
  - term: "EMA"
    definition: "Exponential moving average, used for teacher model in self-distillation."
  - term: "DM test"
    definition: "Diebold-Mariano test, compares predictive accuracy of two forecasts."
critical_citations:
  - "[Wang et al., 2021] — Foundational TTA via entropy minimization."
  - "[Wang et al., 2022] — Stabilizers for streaming TTA."
  - "[Kim et al., 2022] — RevIN for distribution shift in time series."
  - "[Schneider et al., 2020] — BN statistics refresh improves robustness."
  - "[Diebold & Mariano, 1995] — Standard test for forecast comparison."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Directly evaluates forecasting models under distribution shift, core to Odin's predictive module."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Tests TTA algorithms on sequential financial time series, informing Odin's forecasting choices."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Uncertainty-triggered fallback provides baseline strategy for detecting and handling anomalous shifts."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Provides regime-wise evaluation framework and statistical tests (DM, NW) for comparing algorithms."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "medium"
      justification: "Addresses adaptation to changing user behavior over time, analogous to cold-start profile dynamics."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Uses rolling metrics, backtests, and statistical significance tests relevant to Odin's evaluation."
  contribution: "Provides empirical guidance for deploying test-time adaptation in Odin's forecasting module, recommending batch-normalization statistics refresh as a safe default. Informs the design of anomaly detection fallbacks when uncertainty is high. Offers a regime-wise evaluation framework with statistical tests (Diebold-Mariano, Newey-West) that Odin can adopt for rigorous module comparison. Quantifies the trade-off between adaptation benefit and stability, directly applicable to Odin's cold-start and profile dynamics challenges. The drift penalty and EMA-teacher stabilization techniques can be integrated into Odin's budget recommendation and forecasting systems to prevent overfitting to recent noisy spending patterns."
  directly_justifies:
    - "Batch-normalization statistics refresh is a safe default for adapting to spending pattern shifts."
    - "Aggressive norm-only updates can harm forecast accuracy on volatile spending data."
    - "Uncertainty-triggered fallback mitigates harmful updates in high-variance periods."
    - "Regime-wise evaluation with Diebold-Mariano tests is recommended for comparing forecasting modules."
  limits:
    - "Experiments focus on daily financial series; spending data may have different seasonality and autocorrelation."
    - "Synthetic shifts are stylized and may not capture all real-world non-stationarities in personal finance."
    - "TTA framework tested on TCN and Transformer backbones; Odin may use different architectures."
    - "Classification task is direction prediction, not directly applicable to Odin's spending forecasting needs."
  mapping_rationale: "Systematic scan across all 12 functional domains and canonical topics identified the paper's primary relevance to Forecasting (6.A, 6.B) and Anomaly Detection (8.A) due to its test-time adaptation framework for non-stationary time series. Algorithmic Evaluation (12.B) was flagged medium for its rigorous statistical testing methodology. Behavioral Profiling (5.B) was deemed medium because adaptation to shifting distributions parallels cold-start profile dynamics. System Evaluation (12.A) was marked medium for the regime-wise and backtest evaluation frameworks. Expense Categorization (3.A-C) and Budget Recommendation (7.A-D) were rejected as the paper does not address categorization or constrained optimization. Savings & Debt Management (13.A-C) was rejected as the focus is on forecasting, not savings/debt. Mobile-First Design (9.A-B), Data Privacy (10.A-B), and User Retention (11.A-B) were rejected as the paper is algorithmic and does not discuss UX, privacy, or engagement. User-Declared Preferences (2.C) and Culturally Specific Practices (2.A) were not addressed. The paper's overall relevance to Odin is high for forecasting and anomaly detection modules, providing both algorithmic choices and evaluation best practices."
limitations:
  - "Aggressive norm-only adaptation can overfit short windows and degrade performance on noisy financial data."
  - "The uncertainty threshold is estimated on validation data, which may not generalize to new regimes."
  - "Synthetic shift generators are stylized and may not capture all real-world distribution changes."
  - "Backtest strategies are simple and do not account for transaction costs or market impact. [unacknowledged]"
  - "The study does not explore adaptation for multi-horizon spending forecasts beyond 96-step horizons. [unacknowledged]"
remember_this:
  - "Batch-normalization statistics refresh is a safe default for test-time adaptation."
  - "Aggressive norm-only updates can significantly hurt forecast accuracy on volatile data."
  - "Uncertainty-triggered fallback prevents harmful gradient updates in high-variance periods."
  - "Regime-wise evaluation reveals that adaptation gains are concentrated during strong distribution shifts."
  - "Drift penalties and EMA teachers stabilize adaptation, preventing overreaction to noisy windows."
```
---

## Paper 14: D'Souza et al_summarized.md

**Source File:** `D'Souza et al_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international-algorithm-specific
title: A Comprehensive Review of Machine Learning Techniques for Intelligent Personal Finance Management Systems
authors: D'Souza, M.; Bhegade, P.; Bhalekar, P.; Bhavsar, Y.
year: 2026
venue: Unknown
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 9.A
  - 12.B
tldr: A review of machine learning techniques for personal finance management systems, covering budgeting, forecasting, anomaly detection, and group expense management.
problem_and_motivation: Research on intelligent PFMS is fragmented across components like budgeting, forecasting, anomaly detection, and group finance, limiting cohesive solution development. Existing systems lack adaptability and predictive insights due to reliance on rigid, rule-based mechanisms. This fragmentation hinders the creation of integrated, explainable, and user-friendly intelligent finance systems.
approach:
  - Conducts a qualitative literature survey of PFMS components, including expense tracking, bill splitting, predictive budgeting, financial anomaly detection, and explainable AI methods.
  - Analyzes a range of approaches, including statistical methods, machine learning, deep learning, and hybrid techniques.
  - Offers a structured taxonomy of PFMS components and provides comparative insights across various learning methods.
  - Identifies gaps in current research to guide future work toward integrated intelligent finance systems.
findings:
  - Rule-based budgeting systems are transparent but lack adaptability to changing spending patterns.
  - EWMA and ARIMA models are effective for stable trends but struggle with non-linear changes and seasonal variations.
  - LSTM networks capture long-term dependencies but require substantial data and computational resources.
  - Hybrid ARIMA-LSTM frameworks improve forecasting robustness by combining linear and non-linear modeling.
  - Isolation Forest is effective for unsupervised anomaly detection but lacks inherent explanatory context.
  - num: The reviewed literature indicates a transition from static rule enforcement to adaptive and predictive budgeting formulations.
key_figures_tables:
  - Figure 1: Actual vs Predicted Values using LSTM → LSTM smooths volatile financial data to capture underlying trends.
  - Figure 3: Conceptual Architecture of the Budgeting Pipeline → Pipeline from data input to adaptive budget formulation with uncertainty buffer.
  - Figure 4: Visualization of budgeting techniques → EWMA, ARIMA, and LSTM provide complementary perspectives on spending data.
  - Figure 6: Anomaly detection using One-Class SVM → Visualization of anomaly detection through boundary-based classification.
  - Table 1: Qualitative Comparison of Budgeting Techniques → Trade-offs between interpretability, scalability, and adaptability for budgeting methods.
key_equations:
  - equation: Y_t = φ_1 Y_{t-1} + ... + θ_1 ϵ_{t-1} + ϵ_t
    explanation: ARIMA model combining autoregressive and moving average components.
  - equation: s(x,ψ) = 2^{-E(h(x))/c(ψ)}
    explanation: Isolation Forest anomaly score based on average path length.
definitions:
  - term: PFMS
    definition: Personal Finance Management Systems
  - term: EWMA
    definition: Exponentially Weighted Moving Averages
  - term: LSTM
    definition: Long Short-Term Memory networks
  - term: GRU
    definition: Gated Recurrent Units
  - term: XAI
    definition: Explainable Artificial Intelligence
critical_citations:
  - "[Hochreiter and Schmidhuber, 1997] — Foundational LSTM architecture paper."
  - "[Liu, Ting, and Zhou, 2008] — Introduces Isolation Forest for anomaly detection."
  - "[Box and Jenkins, 1970] — Foundational text on ARIMA time series modeling."
  - "[Zhang, 2003] — Hybrid ARIMA-neural network model for forecasting."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Review discusses expense categorization as part of PFMS pipelines.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: Mentions category-level forecasting for structured resource allocation.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Provides a comprehensive overview of existing PFMS and their limitations.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies fragmentation, lack of integration, and rule-based rigidity as key gaps.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Discusses behavior-oriented budgeting and clustering of spending patterns.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Reviews predictive modeling approaches for forecasting and budgeting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Analyzes ARIMA, LSTM, and hybrid methods for expenditure forecasting.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Reviews rule-based, EWMA, and behavior-oriented budgeting strategies.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Discusses adaptive budgeting aligned with evolving financial behavior.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Provides a comprehensive review of anomaly detection in PFMS.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Compares Isolation Forest, One-Class SVM, and autoencoder-based methods.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: Briefly mentions mobile deployment constraints for computationally intensive models.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Provides comparative analysis across budgeting, forecasting, and anomaly detection techniques.
  contribution: This comprehensive review provides a structured taxonomy of PFMS components, offering a systematic scan of machine learning applications across budgeting, forecasting, anomaly detection, and group expense management. The comparative analysis of techniques directly supports Odin's architectural decisions by highlighting trade-offs between interpretability, scalability, and adaptability for each module. The paper's identification of fragmentation in existing research justifies Odin's goal of creating an integrated PFMS platform. The review of unsupervised anomaly detection methods informs Odin's approach to identifying irregular spending without labeled data. The discussion of explainable AI requirements supports Odin's focus on user trust and transparency.
  directly_justifies:
    - "A transition from static rule enforcement to adaptive and predictive budgeting formulations."
    - "Hybrid ARIMA-LSTM frameworks improve forecast robustness across diverse financial conditions."
    - "Isolation Forest achieves superior detection capability relative to density-based alternatives."
    - "Explainable AI is a critical requirement for user trust in financial decision-support systems."
    - "There is a need for cohesive intelligent PFMS frameworks integrating multiple analytical components."
  limits:
    - "The review is qualitative and does not provide empirical benchmarks comparing techniques on standard datasets."
    - "The paper does not address cold-start problems in user profiling and anomaly detection."
    - "Data privacy and security concerns in PFMS are mentioned but not examined in detail."
    - "The review does not cover specific mobile-first design guidelines or UX considerations."
    - "Evaluation frameworks for budget recommendation systems are not discussed. [unacknowledged]"
  mapping_rationale: A systematic scan was performed across all 12 functional domains and their associated topic codes. The paper was flagged as highly relevant to domains related to expense categorization (3.A, 3.B), existing systems and gaps (4.A, 4.B), forecasting (6.A, 6.B), budgeting strategies (7.A, 7.B), and anomaly detection (8.A, 8.B). Medium relevance was assigned to behavioral profiling (5.A) and evaluation of algorithmic modules (12.B) due to the paper's comparative analysis. Low relevance was assigned to mobile-first design (9.A) as it was only mentioned in passing. The paper's discussion of group expense management touches on 4.A and 4.B as a system gap but does not directly address 3.C (user-defined constraints) or 7.C/7.D (optimization and infeasibility), so these were rejected. The paper provides an overview of existing PFMS but lacks depth on savings and debt management (13.A, 13.B), and does not address privacy and trust (10.A, 10.B) or retention mechanisms (11.A, 11.B), which were considered and rejected due to lack of actionable content. Overall, the paper is highly relevant to Odin's core analytical modules, serving as a foundational review that justifies the need for an integrated, intelligent PFMS.
limitations:
  - "The paper is a survey and does not provide empirical validation of the discussed techniques."
  - "The review focuses on algorithmic techniques but does not deeply address user-centric design considerations. [unacknowledged]"
  - "Data quality and availability challenges are acknowledged but not systematically analyzed."
  - "The paper does not discuss evaluation methodologies for user-facing system components. [unacknowledged]"
remember_this:
  - "Machine learning enables PFMS transition from descriptive reporting to adaptive decision support."
  - "Hybrid ARIMA-LSTM frameworks balance linear trend modeling with non-linear behavioral flexibility."
  - "Unsupervised anomaly detection is preferred in PFMS due to the absence of labeled spending data."
  - "Explainable AI is essential for maintaining user trust in complex financial systems."
  - "Research fragmentation across PFMS components justifies Odin's integrated architecture."
```
---

## Paper 15: Pagliaro_summarized.md

**Source File:** `Pagliaro_summarized.md`

```yaml
paper_id: 10.3390/electronics14091721
designation: international-algorithm-specific
title: Artificial Intelligence vs. Efficient Markets: A Critical Reassessment of Predictive Models in the Big Data Era
authors: Pagliaro, A.
year: 2025
venue: Electronics
odin_topics:
  - 5.B
  - 6.A
  - 6.B
  - 7.A
  - 7.D
  - 8.A
  - 8.B
  - 12.A
  - 12.B
  - 12.C
tldr: A critical review reconciling the Efficient Market Hypothesis with AI-driven predictability through an adaptive market framework and proposing a multi-dimensional evaluation methodology for predictive models.
problem_and_motivation: The literature on AI for stock prediction lacks rigorous cross-regime evaluation, comprehensive performance assessment beyond classification metrics, and a reconciliation of empirical predictability with theoretical market efficiency. This gap limits the practical application of academic findings and their integration into financial theory.
approach:
  - A critical review synthesizing findings across statistical methods, pattern recognition, machine learning, sentiment analysis, and hybrid systems.
  - A proposed adaptive market framework to reconcile the Efficient Market Hypothesis with empirical AI-driven predictability.
  - A proposed comprehensive evaluation methodology that extends beyond classification accuracy to include economic significance, robustness, and implementation feasibility.
  - Analysis of ensemble methods like Extra Trees, Random Forest, and XGBoost against single classifiers.
  - Examination of methodological challenges including backtest overfitting, regime changes, data snooping, and implementation constraints.
findings:
  - num: 86% directional accuracy achieved by ExtraTreesClassifier in specific market conditions, outperforming RandomForest at 73%.
  - num: Hybrid approaches demonstrate superior performance by capturing complementary market signals, with a 6% improvement in index prediction.
  - num: LSTM networks achieved 72% accuracy for five-day predictions, with performance highly sensitive to data preparation and market regimes.
  - num: Many models showing statistical significance fail to generate economic value after accounting for transaction costs, with net performance reductions of 15-40%.
  - num: 60-80% of published financial anomalies fail to replicate under more stringent statistical tests.
  - Tree-based ensemble methods consistently outperform single classifiers across various studies and market conditions.
  - The gap between statistical significance and economic relevance represents a critical limitation in current research.
  - Proper evaluation requires moving beyond simple accuracy metrics to consider financial performance under realistic constraints.
  - Model performance varies substantially across different time horizons and market regimes.
key_figures_tables:
  - Figure 1: Interrelations of AI methods → Shows hybrid methods integrating multiple techniques at the center.
  - Figure 2: Data flow in modern stock prediction systems → Key performance impact factors include feature engineering and evaluation methodologies.
  - Figure 3: Model evaluation framework → Emphasizes holistic assessment across statistical, financial, robustness, and implementation dimensions.
  - Figure 4: Evolution of prediction methodologies → Progression from statistical methods to advanced approaches like GNNs and RL.
  - Table 3: Performance metrics across key studies → Ensemble methods generally show higher directional accuracy than single classifiers.
key_equations:
  - equation: f_t = σ(W_f · [h_{t-1}, x_t] + b_f)
    explanation: LSTM forget gate equation controlling information retention.
  - equation: C_t = f_t ⊙ C_{t-1} + i_t ⊙ \tilde{C}_t
    explanation: LSTM cell state update balancing old and new information.
  - equation: Attention(Q,K,V) = softmax(QK^T/√d_k)V
    explanation: Transformer self-attention mechanism for sequence modeling.
definitions:
  - term: EMH
    definition: Efficient Market Hypothesis - theory that asset prices fully reflect all available information.
  - term: LSTM
    definition: Long Short-Term Memory - recurrent neural network architecture for sequential data.
  - term: PFMS
    definition: Personal Financial Management System - software for managing personal finances.
  - term: GCN
    definition: Graph Convolutional Network - neural network operating on graph-structured data.
  - term: RL
    definition: Reinforcement Learning - learning optimal actions through trial and error.
critical_citations:
  - "[Fischer and Krauss, 2018] — LSTM outperforms DNN, RF, and logistic regression on S&P500."
  - "[Gu et al., 2020] — ML systematically outperforms traditional approaches in predicting stock returns."
  - "[López de Prado, 2019] — Data science solution to the multiple-testing crisis in financial research."
  - "[Harvey et al., 2016] — 60-80% of published anomalies fail to replicate under stringent tests."
relevance:
  topics:
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: contextual
      justification: Discusses model adaptation to changing market regimes, analogous to user profile dynamics.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Core focus on evaluating predictive models for financial forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Comprehensive analysis of forecasting algorithms including LSTM, ARIMA, and ensemble methods.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: The adaptive market framework provides a theoretical basis for dynamic financial strategies.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: low
      justification: Evaluation framework and implementation constraints indirectly relate to feasibility handling.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Discussion of pattern recognition and outlier detection techniques is transferable.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Review of ML algorithms for detecting financial patterns is applicable to anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a comprehensive evaluation framework for financial prediction systems.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Rigorous methods for assessing algorithmic performance, including statistical and economic significance.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: high
      justification: Proposed multi-dimensional evaluation methodology is directly applicable to recommendation system assessment.
  contribution: The paper's adaptive market framework provides a theoretical foundation for Odin's dynamic budget recommendation module by reconciling predictable user behavior with market efficiency principles. Its multi-dimensional evaluation methodology, distinguishing statistical from economic significance, directly informs the design of Odin's system evaluation protocols. The comprehensive analysis of ensemble methods, particularly the finding that ExtraTreesClassifier outperforms RandomForest (86% vs 73% accuracy), guides Odin's choice of algorithms for spending forecasting. The emphasis on proper cross-validation techniques, including purged cross-validation, informs Odin's validation pipeline to prevent information leakage. The critical examination of implementation constraints, including the 15-40% performance reduction after accounting for real-world costs, shapes Odin's architecture to ensure practical viability.
  directly_justifies:
    - "Ensemble methods, particularly ExtraTrees and RandomForest, consistently outperform single classifiers in predictive accuracy."
    - "Models showing statistical significance frequently fail to generate economic value after accounting for transaction costs."
    - "A multi-dimensional evaluation framework is essential for assessing prediction models in personal finance systems."
    - "Proper cross-validation techniques must account for temporal dependencies to prevent overoptimistic performance estimates."
    - "The adaptive market framework reconciles predictable patterns with theoretical efficiency through evolutionary market dynamics."
  limits:
    - "None of the studies reviewed were conducted within a PFMS context for Filipino young professionals."
    - "The review synthesizes findings from stock market prediction rather than personal spending forecasting."
    - "No empirical validation of the proposed framework on PFMS data is provided."
    - "The paper does not address specific challenges of mobile-first design or user engagement in personal finance."
  mapping_rationale: A systematic scan was conducted across all 12 functional domains and their associated topic codes. The paper was found to be highly relevant to Predictive Modeling (6.A, 6.B), System Evaluation (12.A, 12.B, 12.C), and partially to Behavioral Profiling (5.B) for its discussion of regime adaptation. It also provides medium relevance to Budget Recommendation (7.A) through its adaptive framework, Anomaly Detection (8.A, 8.B) via pattern recognition algorithms, and contextual relevance to 7.D for infeasibility handling. Domains related to Filipino Cultural Context (2.A-D), Expense Categorization (3.A-C), Existing Systems (4.A-B), Mobile Design (9.A-B), Data Privacy (10.A-B), User Retention (11.A-B), and Savings/Debt (13.A-C) were considered and rejected as the paper does not address these topics. The paper's overall relevance to Odin lies in its rigorous evaluation framework, which can be adapted for PFMS algorithm assessment, though its stock market focus requires careful translation to personal finance contexts.
limitations:
  - "The review focuses on stock market prediction, not personal financial management."
  - "Most studies evaluated were conducted on developed markets, not the Philippine context."
  - "The proposed evaluation framework has not been empirically validated on PFMS data."
  - "Does not address user-specific constraints like spending limits or financial goals."
  - "Many reported performance metrics represent gross accuracy before accounting for real-world implementation costs."
remember_this:
  - "Ensemble methods like ExtraTreesClassifier achieve 86% directional accuracy in volatile market conditions."
  - "Models with statistical significance often fail to generate economic value after transaction costs."
  - "A multi-dimensional evaluation framework distinguishes statistical significance from economic relevance."
  - "Proper cross-validation must account for temporal dependencies to avoid overoptimistic performance estimates."
  - "The adaptive market framework reconciles predictable patterns with theoretical market efficiency."
```
---

## Paper 16: Akarlar_summarized.md

**Source File:** `Akarlar_summarized.md`

```yaml
paper_id: "b3e5c2d4-8a7b-4c1e-9f0d-8a7b6c5d4e3f"
designation: "international-algorithm-specific"
title: "Beyond Prompt Engineering: Neuro-Symbolic-Causal Architecture for Robust Multi-Objective AI Agents"
authors: "Akarlar, G. A."
year: 2025
venue: "Unknown"
odin_topics:
  - "6.A"
  - "6.B"
  - "7.C"
  - "7.D"
  - "8.A"
  - "8.B"
  - "10.B"
  - "12.A"
  - "12.B"
tldr: "A neuro-symbolic-causal architecture integrating LLM, formal verification, and causal inference achieves robust multi-objective decision-making, outperforming baselines in e-commerce simulations."
problem_and_motivation: "LLM agents exhibit catastrophic brittleness, producing wildly different outcomes depending on prompt framing and lacking hard safety guarantees. Existing approaches fail to balance competing objectives like profit and trust over long horizons. There is a need for architectural design that ensures reliable multi-objective optimization without relying on prompt engineering."
approach:
  - "Simulated 52-week e-commerce environment with price elasticity, trust dynamics, and seasonality."
  - "Used GPT-4o as neural strategist generating three diverse hypotheses per decision."
  - "Symbolic Guardian enforces hard constraints (price floors, margins, ad caps) with formal TLA+ verification."
  - "Causal engine (EconML CausalForestDML) predicts counterfactual profit and trust impacts for candidate actions."
  - "Evaluated three architectures: LLM-only, LLM+Guardian, and full Chimera across neutral and biased prompts."
  - "Benchmarked under volume-focused and margin-focused organizational biases to test robustness."
  - "Measured total profit, trust change, Sharpe ratio, and constraint violation rate."
findings:
  - "num: Chimera achieves $1.89M cumulative profit vs $1.69M (LLM+Guardian) and $1.34M (LLM-only) in neutral benchmark."
  - "num: Under volume bias, LLM-only loses $99K with 82.7% violation rate; Chimera achieves $1.52M with zero violations."
  - "num: Under margin bias, LLM-only destroys trust by 48.6% while Chimera improves trust by 10.8%."
  - "num: Chimera attains Sharpe ratio 6.18 vs 2.47 (LLM-only) in neutral benchmark."
  - "Guardian eliminates all constraint violations across 174 million verified states."
  - "Causal engine enables self-correction of biased instructions, maintaining consistent high performance."
key_figures_tables:
  - "Figure 5: Cumulative profit trajectories show Chimera leads with $1.89M vs others → architectural advantage in neutral settings."
  - "Figure 6: Risk-return scatter shows Chimera in optimal high-return low-risk quadrant (Sharpe 6.18) → superior risk-adjusted performance."
  - "Figure 11: Cross-strategy robustness shows Chimera delivers consistent profit and trust under both biases, while LLM-only is brittle → architectural robustness transcends prompt framing."
  - "Figure 2: TLA+ verification output shows zero violations across 174M states → formal safety guarantee."
key_equations:
  - equation: "\\tau(a, s) = E[Y | do(A=a), S=s] - E[Y | do(A=a_0), S=s]"
    explanation: "Causal effect of action a on outcome Y."
  - equation: "Q_t = D_{base} \\times f_{price}(p_t) \\times f_{trust}(\\tau_t) \\times f_{ad}(a_t) \\times f_{season}(t)"
    explanation: "Multiplicative demand model incorporating price, trust, ad, and season."
  - equation: "\\tau_{new} = \\tau + \\eta \\cdot \\Delta \\%"
    explanation: "Trust update based on price change sign and magnitude."
  - equation: "\\pi = (p - c) Q - fixed\\_cost - a"
    explanation: "Profit calculation from price, cost, quantity, and ad spend."
definitions:
  - term: "Guardian"
    definition: "Symbolic constraint engine that validates and repairs actions to enforce business rules."
  - term: "Causal Engine"
    definition: "Module that predicts counterfactual outcomes using EconML's causal forest."
  - term: "TLA+"
    definition: "Temporal Logic of Actions, a formal specification language for verifying concurrent systems."
  - term: "Chimera"
    definition: "The proposed neuro-symbolic-causal architecture integrating LLM, Guardian, and Causal Engine."
critical_citations:
  - "[Pearl, 2009] — Foundation for causal inference and do-calculus."
  - "[Lamport, 2002] — TLA+ specification for formal verification."
  - "[Yao et al., 2023] — ReAct framework for LLM reasoning and acting."
  - "[Chernozhukov et al., 2018] — Double/debiased machine learning for causal estimation."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Uses causal model to predict profit/trust impacts, transferable to spending prediction."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "medium"
      justification: "Forecasts counterfactual outcomes over multi-week horizons similar to spending forecasting."
    - code: "7.C"
      name: "Constrained Optimization Approaches for Budget Allocation"
      relevance: "high"
      justification: "Central focus on constraint enforcement and repair for multi-objective optimization."
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "high"
      justification: "Guardian repairs invalid actions, directly addressing infeasibility."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Guardian detects and prevents constraint-violating actions, akin to anomaly detection."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "low"
      justification: "Uses rule-based validation rather than algorithmic anomaly detection; tangentially relevant."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "medium"
      justification: "Models trust dynamics as a key objective, relevant to user trust in PFMS."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides structured evaluation with multiple metrics across scenarios."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Systematically compares three architectures, offering methodology for evaluating algorithmic modules."
  contribution: "Chimera's constraint validation and repair mechanism directly informs Odin's budget recommendation module by providing a formally verified method to handle infeasible allocations (7.C, 7.D). The causal forecasting approach can be applied to Odin's spending forecasting (6.A, 6.B) to predict the impact of spending decisions on future financial states. The architecture comparison and evaluation metrics offer a template for evaluating Odin's algorithmic modules (12.B). The trust modeling contributes to Odin's user trust management (10.B). Overall, the architectural principles enhance Odin's reliability and robustness in multi-objective decision-making."
  directly_justifies:
    - "Architectural design, not prompt engineering, determines agent reliability in high-stakes domains."
    - "Adding symbolic constraints prevents catastrophic failures but underperforms without causal foresight."
    - "Chimera achieves up to 130% higher profit than LLM-only baselines under organizational biases."
    - "Formal verification proves zero constraint violations across all scenarios."
  limits:
    - "Single-domain evaluation (e-commerce) limits generalizability to PFMS."
    - "Causal model relies on pre-trained data and may degrade under distribution shift."
    - "Computational overhead (3-5× latency) may be prohibitive for real-time applications."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes identified the following relevant areas: Budget Recommendation (7.C, 7.D) were flagged as high relevance because the paper directly addresses constrained optimization and infeasibility handling via a formally verified Guardian. Spending Forecasting (6.A, 6.B) and System Evaluation (12.A, 12.B) were marked medium to high because the paper provides predictive modeling and comparative benchmarking methodologies. Anomaly Detection (8.A, 8.B) and User Trust (10.B) were considered medium relevance due to the Guardian's violation detection and trust dynamics. Other domains such as Expense Categorization, Filipino Cultural Context, Mobile-First Design, Data Privacy, Retention, and Savings/Debt were considered and rejected as the paper does not address these topics. Borderline cases included trust, which is brand trust rather than user trust in PFMS, but the modeling approach is transferable; thus 10.B was included. Overall, the paper provides architectural insights that are broadly applicable to Odin's decision-support modules, particularly in ensuring safe and optimal recommendations."
limitations:
  - "Single-domain evaluation (e-commerce) limits generalizability."
  - "Causal model reliability under distribution shift is not fully addressed."
  - "Computational latency is higher than LLM-only agents."
  - "Experiments use a single random seed; multiple runs are needed for statistical robustness."
remember_this:
  - "Chimera achieves $1.89M profit vs $1.34M for LLM-only in neutral benchmark."
  - "Symbolic validation eliminates catastrophic failures across all scenarios."
  - "Causal reasoning enables robust multi-objective optimization under biased prompts."
  - "Architectural integration outperforms prompt engineering alone."
  - "Formal verification proves zero constraint violations across 174 million states."
```
---

## Paper 17: Kozakova & Endeva_summarized.md

**Source File:** `Kozakova & Endeva_summarized.md`

```yaml
paper_id: "10.15421/322509"
designation: "international-algorithm-specific"
title: "SMART FINANCE MANAGEMENT SYSTEM BASED ON ARTIFICIAL INTELLIGENCE TECHNOLOGIES"
authors: "Kozakova, N.L.; Endeka, M.H."
year: 2025
venue: "Problems of Applied Mathematics and Mathematical Modeling"
odin_topics:
  - "3.A"
  - "4.B"
  - "6.A"
  - "6.B"
  - "7.B"
  - "8.A"
  - "8.B"
  - "12.A"
  - "12.B"
  - "12.C"
tldr: "Integrates classification, forecasting, anomaly detection, and LLM-generated advice into a personal finance management system, achieving high accuracy on transaction data."
problem_and_motivation: "Traditional manual budgeting methods cannot handle the complexity and volume of modern financial data, and existing systems lack adaptive, personalized analysis and actionable recommendations."
approach:
  - "Used a dataset of 1000 transactions with categories, amounts, timestamps, and merchant descriptions."
  - "Applied k-NN and decision trees for transaction classification using Euclidean distance and information gain."
  - "Used ARIMA and LSTM for expense forecasting, with LSTM capturing long-term dependencies."
  - "Employed Isolation Forest, autoencoders, and SVM for anomaly detection based on reconstruction error and decision boundaries."
  - "Generated personalized recommendations via matrix factorization and collaborative filtering."
  - "Integrated a large language model to produce real-time textual advice from aggregated financial data."
  - "Implemented in Python with pandas, scikit-learn, TensorFlow, statsmodels, and OpenAI libraries."
  - "Data stored in PostgreSQL, with REST API for module communication."
findings:
  - "num: Classification accuracy reached 91.2% using k-NN and decision trees."
  - "num: ARIMA achieved MAPE of 6.8%, while LSTM achieved 5.4% for expense forecasting."
  - "num: Anomaly detection F1-score was 0.86 using autoencoders and Isolation Forest."
  - "num: Recommendation precision was 0.89."
  - "The system generates user-friendly textual recommendations, e.g., suggesting a monthly pass for transportation."
  - "Combining statistical and neural models improves overall performance."
key_figures_tables:
  - "Figure 1: Raw transactional data before preprocessing → shows unprocessed input."
  - "Figure 2: Processed and normalized data ready for modeling → illustrates cleaned structured data."
  - "Figure 3: AI-generated feedback and recommendations → example of personalized textual advice."
key_equations:
  - equation: "d(p,q) = sqrt( sum_{i=1}^{m} (p_i - q_i)^2 )"
    explanation: "Distance metric for k-NN classification."
  - equation: "Gain(S,A) = Entropy(S) - sum_{v in Values(A)} |S_v|/|S| * Entropy(S_v)"
    explanation: "Criterion for decision tree splitting."
  - equation: "\\phi(B)(1-B)^d X_t = \\theta(B) \\epsilon_t"
    explanation: "ARIMA model for time series forecasting."
  - equation: "f_t = \\sigma(W_f \\cdot [h_{t-1}, x_t] + b_f)"
    explanation: "Forget gate in LSTM controls memory retention."
  - equation: "L = (1/n) sum_{i=1}^{n} (x_i - \\hat{x}_i)^2"
    explanation: "Autoencoder reconstruction loss for anomaly detection."
definitions:
  - term: "k-NN"
    definition: "k-Nearest Neighbors, a supervised learning algorithm for classification."
  - term: "ARIMA"
    definition: "AutoRegressive Integrated Moving Average, a statistical model for time series forecasting."
  - term: "LSTM"
    definition: "Long Short-Term Memory, a recurrent neural network for capturing long-term dependencies."
  - term: "SVM"
    definition: "Support Vector Machine, a supervised learning model for classification and anomaly detection."
  - term: "LLM"
    definition: "Large Language Model, a generative AI model for producing natural language text."
  - term: "MAPE"
    definition: "Mean Absolute Percentage Error, a metric for forecasting accuracy."
  - term: "F1-score"
    definition: "Harmonic mean of precision and recall, used for anomaly detection evaluation."
critical_citations:
  - "[Mienye, 2024] — Surveys deep learning applications in finance."
  - "[Li, Ding, and Chen, 2023] — Reviews LLM usage in financial analytics."
  - "[Kong et al., 2025] — Discusses LSTM and GRU for time series forecasting."
  - "[Su et al., 2024] — Reviews Transformer-based long-term forecasting."
relevance:
  topics:
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "high"
      justification: "Directly proposes and evaluates k-NN and decision trees for transaction categorization."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Motivates the system by citing insufficiency of traditional methods."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Implements ARIMA and LSTM for expense forecasting."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Compares ARIMA and LSTM specifically for financial time series."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Generates actionable spending recommendations, e.g., switching to monthly pass."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Includes anomaly detection as a core module using multiple algorithms."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Evaluates Isolation Forest, autoencoders, and SVM for anomaly detection."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Presents an experimental evaluation with accuracy, MAPE, F1, and precision."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Provides quantitative metrics for each algorithmic component."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "high"
      justification: "Reports recommendation precision, directly evaluating the recommender module."
  contribution: "The paper validates a hybrid AI architecture for personal finance that directly informs Odin's classification, forecasting, anomaly detection, and recommendation modules. The integration of LLMs for textual advice provides a template for Odin's user-facing communication layer. Empirical results offer baseline performance benchmarks for these core algorithms. The system's modular design and use of both statistical and neural methods support Odin's architecture decisions."
  directly_justifies:
    - "k-NN and decision trees can classify transactions with 91.2% accuracy."
    - "LSTM forecasting achieves lower MAPE (5.4%) than ARIMA (6.8%) on spending data."
    - "Autoencoders combined with Isolation Forest yield F1-score of 0.86 for anomaly detection."
    - "Collaborative filtering and matrix factorization achieve 0.89 precision in recommendations."
    - "LLMs can generate personalized, context-aware financial advice from aggregated data."
  limits:
    - "Dataset size is limited to 1000 transactions, which may not represent diverse spending patterns."
    - "No user study or longitudinal evaluation was conducted to assess real-world usability."
    - "Cold-start scenarios for new users are not addressed."
  mapping_rationale: "The systematic scan across all 12 functional domains flagged the algorithmic domains as highly relevant: Expense Categorization (3.A), Predictive Modeling (6.A, 6.B), Anomaly Detection (8.A, 8.B), and Evaluation (12.A, 12.B, 12.C). The paper's motivation about traditional limitations justified 4.B as medium. Budget Recommendation (7.B) was rated medium because recommendations are generated but not via constrained optimization. Domains related to Filipino context (1.x, 2.x), Mobile-First (9.x), Data Privacy (10.x), Retention (11.x), and Savings/Debt (13.x) were rejected because the paper does not address these aspects. Borderline cases: the paper's classification of transactions touches 5.C indirectly, but since it does not profile user behavior, 5.C was excluded. The overall relevance is strong for Odin's algorithmic core, providing validated methods and performance benchmarks."
limitations:
  - "Tested on only 1000 transactions, limiting generalizability [unacknowledged]."
  - "No user study on usability or satisfaction [unacknowledged]."
  - "Does not address cold-start scenarios for new users [unacknowledged]."
  - "Privacy and security considerations beyond OAuth2 are not discussed [unacknowledged]."
remember_this:
  - "LSTM outperforms ARIMA with MAPE of 5.4% versus 6.8%."
  - "Classification accuracy of 91.2% supports automated transaction tagging."
  - "Anomaly detection F1-score of 0.86 indicates reliable fraud detection."
  - "LLM integration enables natural-language financial advice."
  - "Modular architecture facilitates easy extension and integration."
```
---

## Paper 18: Liu_summarized.md

**Source File:** `Liu_summarized.md`

```yaml
paper_id: 10.1109/ACCESS.2025.3625441
designation: international-algorithm-specific
title: Deep Feature Extraction Method for Automatic Classification and Processing of Accounting Information
authors: Liu, F.
year: 2025
venue: IEEE Access
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 10.A
tldr: A deep feature extraction framework using convolutional autoencoders automates accounting classification by learning hierarchical representations directly from raw journal entries, eliminating manual feature engineering and enhancing performance for personal finance and anomaly detection tasks.
problem_and_motivation: Traditional accounting classification systems lack adaptability to evolving data and depend heavily on manual feature engineering. This reliance limits scalability and accuracy as financial data grows in volume and complexity, creating a need for automated, adaptive feature extraction.
approach:
  - A convolutional autoencoder framework learns multi-level hierarchical representations directly from raw journal entries.
  - A dual-objective design simultaneously performs input reconstruction and classification to preserve fidelity and promote discriminative learning.
  - An adversarial training component enhances robustness against class imbalance and input noise.
  - FinGraphNet encodes financial entities and interactions as a dynamic, directed multigraph with temporal-aware propagation.
  - Audit-Informed Reinforcement Planning (AIRP) integrates compliance constraints and historical audit data into a reinforcement learning framework.
findings:
  - num: 12 percentage points improvement in classification accuracy compared to logistic regression and decision trees.
  - num: 15 percentage points improvement in anomaly detection F1-score over traditional baselines.
  - num: Achieves MAE of 9.84 on Compustat and 0.869 R2 on EDGAR, outperforming transformer and LSTM baselines.
  - The FinGraphNet architecture demonstrates robust performance across diverse financial datasets and conditions.
  - The AIRP module enables strategic financial control under constraints and uncertainty.
key_figures_tables:
  - Figure 1: High-level architecture of FinGraphNet → Graph-based model integrating temporal data and regulatory logic.
  - Figure 2: Detailed view of dynamic graph encoder → Raw financial entities transformed into rich graph representations.
  - Figure 5: Evaluation on Compustat and EDGAR → Proposed method achieves lowest errors and highest R2.
  - Figure 6: Comparison on Orbis and CSMAR → Demonstrates superior forecasting accuracy across varying temporal granularities.
  - Table 2: Comparison on Compustat and EDGAR → Proposed method outperforms SOTA baselines on all metrics.
  - Table 3: Comparison on Orbis and CSMAR → Consistent performance gains across diverse datasets.
  - Table 4: Ablation on Compustat and EDGAR → Each core component contributes significantly to overall performance.
  - Table 5: Ablation on Orbis and CSMAR → Full model achieves best results, confirming synergistic integration.
key_equations:
  - equation: S_t = (A_t, L_t, R_t, C_t, E_t)
    explanation: Financial state tuple of assets, liabilities, revenue, cost, and equity.
  - equation: LQ_{t+1}=LQ_t+\left(\sum_{i=1}^n R_t^{(i)}-\sum_{j=1}^m C_t^{(j)}-D_t\right)
    explanation: Net cash transformation with debt servicing obligations.
  - equation: xˆ(t+1)=argmin_{x∈F} ||x−x˜(t+1)||_2^2
    explanation: Projects predicted flows to nearest feasible point under constraints.
definitions:
  - term: CNN
    definition: Convolutional neural network for spatial feature extraction.
  - term: RNN
    definition: Recurrent neural network for sequential data modeling.
  - term: LSTM
    definition: Long short-term memory, a gated RNN variant.
  - term: GRU
    definition: Gated recurrent unit, a simplified LSTM variant.
  - term: ERP
    definition: Enterprise resource planning systems.
  - term: RPA
    definition: Robotic process automation for automating routine tasks.
  - term: XAI
    definition: Explainable artificial intelligence for model interpretability.
  - term: AIRP
    definition: Audit-Informed Reinforcement Planning for compliance-aware decision-making.
  - term: EFM
    definition: Enterprise financial management.
  - term: ROE
    definition: Return on equity, a profitability metric.
  - term: LCR
    definition: Liquidity coverage ratio, a liquidity metric.
  - term: Assets
    definition: Resources owned by a business expected to provide future economic benefit.
  - term: Liabilities
    definition: Obligations of a business to transfer assets or provide services.
  - term: Equity
    definition: Residual interest in assets after deducting liabilities.
  - term: Liquidity
    definition: Ability to meet short-term financial obligations.
  - term: Audit Constraints
    definition: Regulatory and compliance rules governing financial actions.
critical_citations:
  - "[Zhang et al., 2020] — Deep learning outperforms rule-based methods in fraud detection."
  - "[Craja et al., 2020] — Deep learning superior for detecting financial statement fraud."
  - "[Zhang et al., 2022] — XAI techniques improve trust and regulatory alignment in financial systems."
  - "[Bushman & Smith, 2001] — Foundational work on financial accounting information and governance."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: The paper presents a deep learning framework for automatic classification of accounting transactions.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: The study addresses automated feature extraction for classifying diverse financial entries.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: The paper extensively reviews traditional and modern classification systems, providing context for Odin.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: The paper explicitly critiques limitations of rule-based and shallow ML methods, aligning with Odin's gap analysis.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: The paper classifies transactions but does not profile user behavior; provides contextual background.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: contextual
      justification: The paper's classification approach is algorithmic, offering contextual relevance for profiling methods.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: The paper presents a forecasting model with strong empirical results for spending prediction.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: The FinGraphNet and AIRP models are designed for sequential financial data forecasting.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: The paper explicitly evaluates anomaly detection, a core function for Odin.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: The deep feature extraction framework improves anomaly detection F1-score significantly.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: The paper mentions privacy and regulatory compliance as challenges for deep models.
  contribution: "This paper provides a robust deep feature extraction framework that can inform Odin's expense categorization module by enabling automatic, hierarchical learning from raw transaction data. Its anomaly detection performance improvements suggest a viable approach for Odin's anomaly detection module. The FinGraphNet architecture offers a methodological foundation for modeling temporal and relational aspects of spending behavior. The AIRP module's integration of compliance constraints can inspire Odin's handling of user-defined allocation constraints. The paper's forecasting approach directly justifies Odin's spending forecasting module with quantitative performance metrics."
  directly_justifies:
    - "The convolutional autoencoder framework improves classification accuracy by 12 percentage points, justifying its use for expense categorization."
    - "The anomaly detection F1-score improves by 15 percentage points, supporting the approach for Odin's anomaly detection."
    - "FinGraphNet's graph-based encoding captures temporal and relational dependencies in financial data."
    - "AIRP integrates compliance constraints directly into policy learning for interpretable decision-making."
    - "Adversarial training enhances robustness against noisy and imbalanced data, a common issue in personal finance."
  limits:
    - "The architecture may struggle with extremely sparse or irregular financial data lacking sufficient structure. [unacknowledged]"
    - "Adversarial training introduces computational complexity and hyperparameter sensitivity, hindering real-time deployment. [acknowledged]"
    - "Graph-based temporal encoding has quadratic time complexity (O(n^2)) in graph operations, a potential bottleneck for large-scale systems. [acknowledged]"
    - "Deep architecture may overfit when applied to small-scale or low-diversity datasets. [acknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains was performed. The following domains were flagged as relevant: Expense Categorization (3.A, 3.B - medium), Existing Systems & Gaps (4.A, 4.B - medium), Behavioral Profiling (5.A, 5.C - contextual), Spending Forecasting (6.A, 6.B - high), Anomaly Detection (8.A, 8.B - high), and Data Privacy (10.A - contextual). Borderline cases included 5.A/5.C, where the paper's classification approach is algorithmic but does not profile user behavior, hence assigned contextual. Domains such as Filipino Cultural Context (2.A-D), Mobile-First Design (9.A-B), User Retention (11.A-B), System Evaluation (12.A-C), and Savings & Debt (13.A-C) were considered and rejected due to a lack of relevant content. The paper is highly relevant to Odin's algorithmic modules for classification, forecasting, and anomaly detection."
limitations:
  - "The architecture may struggle with extremely sparse or irregular financial data lacking sufficient structure. [unacknowledged]"
  - "Adversarial training introduces computational complexity and hyperparameter sensitivity, hindering real-time deployment."
  - "Graph-based temporal encoding has quadratic time complexity (O(n^2)) in graph operations, a potential bottleneck for large-scale systems."
  - "Deep architecture may overfit when applied to small-scale or low-diversity datasets."
  - "The study uses proprietary and public datasets, but generalizability to Filipino-specific financial data is not directly tested. [unacknowledged]"
remember_this:
  - "12% improvement in classification accuracy over traditional baselines."
  - "15% improvement in anomaly detection F1-score over traditional baselines."
  - "FinGraphNet models financial entities as a dynamic graph with temporal attention."
  - "AIRP integrates compliance constraints into reinforcement learning for financial decisions."
  - "Deep feature extraction eliminates manual feature engineering for accounting data."
```
---

## Paper 19: Li Y. et al_summarized.md

**Source File:** `Li Y. et al_summarized.md`

```yaml
paper_id: "e5a8c6d4-3b2f-4a7e-9c1d-8f0e2b4a6c8d"
designation: "international-algorithm-specific"
title: "Machine Learning-Based Identification of Anomalous Trading Behavior Patterns Among Asia-Pacific Investors in U.S. Securities Markets"
authors: "Li, Y.; Fan, S.; Wang, H."
year: 2025
venue: "Spectrum of Research"
odin_topics:
  - "8.A"
  - "8.B"
  - "8.C"
  - "5.A"
  - "5.C"
  - "2.A"
  - "2.B"
tldr: "An ensemble machine learning framework detects anomalous trading behaviors among Asia-Pacific investors in U.S. markets, reducing false positives by 34.7% and achieving a 0.971 AUC-ROC."
problem_and_motivation: "Traditional rule-based surveillance systems generate excessive false positives and fail to capture regional behavioral differences among international investors, undermining financial crime detection efficiency. Culturally-aware models are needed to distinguish legitimate regional variations from suspicious activities."
approach:
  - "Collected high-frequency trading data from 847,293 accounts across 12 Asia-Pacific economies over 4 years, totaling over $3.2 trillion in transactions."
  - "Engineered multi-dimensional features including temporal, quantitative, network-based, and cultural indicators."
  - "Developed an ensemble learning framework combining random forest, gradient boosting, LSTM, and transformer architectures with dynamic weighting."
  - "Applied temporal modeling with LSTM and attention mechanisms to capture sequential patterns in trading behavior."
  - "Evaluated performance using precision, recall, F1-score, AUC-ROC, and cost-weighted accuracy under various market conditions."
findings:
  - "num: The ensemble model achieved an AUC-ROC of 0.971, outperforming individual algorithms by 23.4% and traditional methods by 47.8%."
  - "num: False positive rate was reduced to 4.2% under normal trading conditions, a 34.7% improvement over baseline."
  - "Unsupervised clustering identified seven distinct behavioral clusters with strong regional correlations, ranging from conservative institutional to high-frequency retail traders."
  - "Detection rates varied by market condition, from 96.2% in low volume to 85.4% during quarter-end periods."
  - "Coordinated trading schemes accounted for 34.7% of confirmed suspicious activities, often involving multiple accounts from the same jurisdiction."
key_figures_tables:
  - "Figure 3: ROC curve comparison across algorithms → Ensemble achieves highest AUC-ROC (0.971)."
  - "Table 4: Model performance comparison across algorithms → Ensemble shows best precision (0.923), recall (0.876), and F1 (0.899)."
  - "Table 5: Regional distribution of trading activity → Japan and China dominate volume; Philippines included."
  - "Table 6: Behavioral cluster characteristics → Seven clusters with varying risk scores and anomaly rates."
  - "Figure 4: Network visualization of coordinated trading activities → Reveals complex cross-border coordination patterns."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "AML"
    definition: "Anti-Money Laundering"
  - term: "SEC"
    definition: "Securities and Exchange Commission"
  - term: "FINRA"
    definition: "Financial Industry Regulatory Authority"
  - term: "LSTM"
    definition: "Long Short-Term Memory neural network"
  - term: "AUC-ROC"
    definition: "Area Under the Receiver Operating Characteristic curve"
  - term: "RegTech"
    definition: "Regulatory Technology"
critical_citations:
  - "[Yuan and Zhang, 2025] — foundational for culturally-aware anomaly detection"
  - "[Rao et al., 2025] — reinforcement learning approach to AML"
  - "[Levi, 2009] — background on money laundering risks"
relevance:
  topics:
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Directly proposes an anomaly detection framework for financial transactions."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Evaluates ensemble and deep learning algorithms for sequential trading data, applicable to spending patterns."
    - code: "8.C"
      name: "Cold-Start Baseline Strategies for Anomaly Detection"
      relevance: "medium"
      justification: "Provides baseline comparison with traditional methods, though cold-start not explicitly addressed."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Identifies behavioral clusters based on trading patterns, informing profile construction."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "Uses unsupervised clustering and supervised classification to categorize investor behaviors."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "contextual"
      justification: "Discusses cultural influences on investment behavior, but not specific to Filipino practices."
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "contextual"
      justification: "Analyzes seasonal trading patterns which may analogize to spending cycles."
  contribution: "This paper provides a robust ensemble-based anomaly detection framework that can be adapted for Odin's spending anomaly detection module (8.B). Its use of culturally-aware features supports Odin's need to account for Filipino cultural practices (2.A) when flagging unusual transactions. The empirical evaluation methodology offers a template for validating Odin's detection algorithms under varying conditions (12.B). The clustering approach for behavioral profiling (5.A) can inform Odin's user segmentation and cold-start strategies."
  directly_justifies:
    - "Ensemble learning with LSTM and attention achieves 0.971 AUC-ROC for anomaly detection in financial transaction data."
    - "Culturally-aware features reduce false positive rates by 34.7% compared to generic models."
    - "Behavioral clustering reveals distinct investor profiles that correlate with regional origins and risk scores."
  limits:
    - "The dataset is from securities trading, not personal spending, so direct applicability requires validation. [unacknowledged]"
    - "Computational cost of ensemble models may be high for mobile-first deployment. [unacknowledged]"
    - "Cultural features are based on broad regional categories, not individual-level preferences. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains flagged Anomaly Detection (8) as highly relevant due to the paper's core contribution of an ensemble learning framework for detecting suspicious transactions. Behavioral Profiling (5) was assessed as medium relevance because the paper identifies behavioral clusters and uses classification approaches, though not specifically for personal finance. Cultural Context (2) was marked contextual because the paper discusses cultural and seasonal influences on trading behavior but does not focus on Filipino-specific practices. Domains such as Budget Recommendation (7), Forecasting (6), Mobile Design (9), and Savings/Debt (13) were considered and rejected as the paper does not address these areas. Overall, the paper offers transferable anomaly detection methodologies and cultural awareness insights that can inform Odin's design, particularly in anomaly detection and user profiling, though direct application requires adaptation to personal spending data."
limitations:
  - "Data acquisition limitations restrict access to complete transaction data across all venues."
  - "Model generalization across different market environments requires ongoing validation."
  - "Real-time detection faces processing latency and scalability challenges."
  - "The paper does not address personal finance contexts, limiting direct applicability to Odin. [unacknowledged]"
remember_this:
  - "Ensemble model achieves 0.971 AUC-ROC for anomaly detection."
  - "Culturally-aware features reduce false positives by 34.7%."
  - "Seven distinct behavioral clusters emerge from trading data."
  - "Detection performance varies with market volatility and quarter-end periods."
```
---

## Paper 20: Bashshar et al_summarized.md

**Source File:** `Bashshar et al_summarized.md`

```yaml
paper_id: 9bc9e1b0-3b4f-5a6b-8c7d-9e1f2a3b4c5d
designation: international-algorithm-specific
title: ARTIFICIAL INTELLIGENCE-DRIVEN PERSONAL FINANCE SOLUTION
authors: Bashshar, S. A.; Imran, M.; Kumar, P. S.; Goud, E. S.; Venunath, M.; Prasad, M. L. M.
year: 2025
venue: International Journal of Engineering Science and Advanced Technology
odin_topics:
  - 3.A
  - 6.A
  - 6.B
  - 7.B
  - 9.A
  - 12.A
tldr: An AI-powered personal finance assistant using NLP for transaction categorization and ARIMA for expense forecasting is implemented and evaluated for accuracy and usability.
problem_and_motivation: Manual financial tracking fails to provide real-time insights or predictive capabilities, leading to poor budgeting and overspending. AI-driven automation can transform passive record-keeping into proactive financial planning.
approach:
  - Data is collected via user-uploaded CSV files containing transaction fields like date, description, and amount.
  - Preprocessing removes noise and normalizes fields to prepare data for NLP and time-series analysis.
  - NLP techniques via NLTK tokenize, remove stop words, and lemmatize transaction descriptions for automatic categorization.
  - An ARIMA model with parameters selected via AIC forecasts future expenses using historical spending data.
  - The system is implemented with Python, Django, SQLite, and Statsmodels, providing a responsive web interface.
findings:
  - num: Transaction categorization achieved 86.2% accuracy with precision 0.88, recall 0.85, and F1-score 0.86.
  - num: The ARIMA model produced a Mean Absolute Error (MAE) of 253.47 and Root Mean Square Error (RMSE) of 318.91.
  - The system effectively integrates NLP and time-series forecasting to support users in managing and understanding their financial behavior.
  - User feedback via a Likert scale questionnaire was mostly positive, confirming the interface’s usability and clarity.
  - The modular architecture ensures scalability and extensibility for future advancements.
  - The forecasting model captured main seasonal patterns and spending variations.
key_figures_tables:
  - Figure 3: Forecasts of expenses for the next 30 days → Shows close tie between predicted and actual historical expenses.
key_equations:
  - equation: Y_t = φ_1 Y_{t-1} + φ_2 Y_{t-2} + ⋯ + φ_p Y_{t-p} + ϵ_t
    explanation: Auto-regressive component of ARIMA.
  - equation: Y'_t = ∇^d Y_t = (1-B)^d Y_t
    explanation: Integrated component for stationarity.
  - equation: Y_t = ϵ_t + θ_1 ϵ_{t-1} + θ_2 ϵ_{t-2} + ⋯ + θ_q ϵ_{t-q}
    explanation: Moving average component of ARIMA.
definitions:
  - term: ARIMA
    definition: AutoRegressive Integrated Moving Average, a time-series forecasting model.
  - term: NLP
    definition: Natural Language Processing, used for transaction categorization.
  - term: NLTK
    definition: Natural Language Toolkit, a Python library for NLP.
  - term: MAE
    definition: Mean Absolute Error, a metric for forecast accuracy.
  - term: RMSE
    definition: Root Mean Square Error, a metric for forecast accuracy.
  - term: AIC
    definition: Akaike Information Criterion, used for model selection.
critical_citations:
  - "[Arrieta et al., 2019] — Similar study on AI-assisted financial forecasting."
  - "[Budiherwanto, 2025] — Comparative evaluation of commercial IPAs."
  - "[Buckley et al., 2021] — NLP in personal learning assistants."
  - "[Rane, 2023] — Generative AI in finance and accounting."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Directly implements and evaluates an NLP-based transaction categorization framework.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Core contribution involves predictive modeling (ARIMA) for expense forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Applies ARIMA, a forecasting algorithm, to sequential spending data.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Forecasting is intended to support proactive budgeting and planning decisions.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: contextual
      justification: Mentions a responsive web interface but does not focus on mobile-first design principles.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides an evaluation framework using accuracy metrics and user feedback for a PFM system.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: contextual
      justification: The system uses predefined categories (e.g., Food, Travel) without in-depth design discussion.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Briefly mentions limitations of manual methods and existing systems but does not provide a comprehensive survey.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: low
      justification: Mentions gaps like lack of automation and forecasting but does not systematically analyze them.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: low
      justification: Does not discuss financial behavioral profiles or user classification.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Does not address anomaly detection; this is noted as future work.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: Mentions user engagement via clear interface but does not analyze engagement dynamics.
  contribution: "This paper contributes an end-to-end AI system that automates expense categorization using NLP and predicts future spending with ARIMA, directly supporting Odin's expense management and forecasting modules. The modular implementation in Python with a web interface provides a practical reference for Odin's backend and frontend design. The positive user feedback on interface usability informs Odin's UI/UX priorities for user trust and adoption. The reported accuracy and error metrics offer baseline performance expectations for Odin's categorization and forecasting components. The identified future work areas, such as API integration and anomaly detection, align with Odin's roadmap for scalability and intelligence."
  directly_justifies:
    - "AI-driven automation can enhance personal finance management by promoting awareness and responsible spending."
    - "NLP-based transaction categorization can achieve over 86% accuracy, reducing manual effort."
    - "ARIMA modeling can provide reliable expense forecasts with an MAE of approximately 253."
    - "A responsive web interface with clear visualizations improves user engagement and financial insight."
  limits:
    - "The system uses simple keyword matching for NLP categorization, which may lack semantic depth."
    - "Evaluation was conducted on a dataset of 1,000 transactions, limiting generalizability."
    - "User feedback was collected from only ten participants."
    - "Integration with real-time banking APIs is not implemented."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant for Expense Categorization (Domain 3) due to its core NLP-based classification module, and for Spending Forecasting (Domain 6) and Budget Recommendation (Domain 7) due to its ARIMA-based predictive analytics and planning support. These were assigned a 'high' relevance. System Evaluation (Domain 12) was assigned 'medium' as the paper includes metrics and user feedback. Mobile-First Design (Domain 9) was deemed 'contextual' as the system has a web interface but doesn't emphasize mobile-first principles. The paper was considered and rejected for Behavioral Profiling (Domain 5), Anomaly Detection (Domain 8), and Savings & Debt Management (Domain 13) as these topics are not addressed. Borderline cases included its mention of user interfaces (touching 9.A) and engagement (11.A), which were either deemed contextual or low relevance. Overall, the paper is directly relevant to Odin's expense management and forecasting pillars, offering a concrete implementation and evaluation."
limitations:
  - "The NLP categorization relies on static keyword dictionaries and may not capture contextual nuances."
  - "Forecasting was tested on a limited dataset of six months, which may not reflect long-term patterns."
  - "The system requires manual data upload (CSV), lacking automatic synchronization with financial institutions."
  - "User evaluation had a small sample size (n=10)."
  - "No comparison with advanced deep learning models for forecasting was performed."
remember_this:
  - "NLP-based transaction categorization achieved 86.2% accuracy with 1,000 labeled transactions."
  - "ARIMA forecasting produced a Mean Absolute Error of 253.47 on financial data."
  - "The system successfully combined NLP and time-series forecasting for personal finance management."
  - "User feedback confirmed the clarity and responsiveness of the web interface."
  - "Future integrations with real-time APIs and anomaly detection are identified for enhancement."
```
---

## Paper 21: Musunuri_summarized.md

**Source File:** `Musunuri_summarized.md`

```yaml
paper_id: f4a4e9c0-8b6c-5a7d-9e1f-3c4d5e6f7a8b
designation: international-algorithm-specific
title: Intelligent UI's: Revolutionizing Financial Transaction Systems Through AI and Event-Driven Architecture
authors: Musunuri, H.
year: 2025
venue: International Journal on Science and Technology (IJSAT)
odin_topics:
  - "3.A"
  - "4.A"
  - "4.B"
  - "6.A"
  - "7.D"
  - "8.A"
  - "8.B"
  - "9.A"
  - "9.B"
  - "10.A"
  - "12.A"
tldr: AI-driven interfaces and event-driven architectures transform financial transaction systems by enhancing security, performance, and personalization simultaneously.
problem_and_motivation: Financial institutions struggle to balance security, performance, and user experience in transaction interfaces. Traditional systems with linear workflows, reactive security, and one-size-fits-all designs fail to meet modern expectations. A paradigm shift is needed to transcend these trade-offs.
approach:
  - "The paper reviews the evolution from legacy banking interfaces to AI-driven, event-driven architectures."
  - "It analyzes the limitations of traditional systems including linear workflows and reactive security."
  - "It examines predictive interface adaptation using machine learning models for behavior analysis."
  - "It discusses behavioral biometrics and zero-trust models for continuous authentication."
  - "It evaluates event-driven architectures that decouple front-end from back-end processing."
  - "It explores context-aware components and progressive disclosure for personalized UX."
  - "It synthesizes findings from multiple empirical studies and industry reports."
  - "It presents a business case with metrics from institutions implementing intelligent UIs."
findings:
  - "num: Mobile banking penetration in India grew from 10.7% to 42.6% from 2017 to 2023."
  - "num: Adaptive security policies resulted in 67% fewer successful breach attempts."
  - "num: Event-driven architectures reduced transaction latency by 64-78%."
  - "num: Behavioral biometrics achieved 97.6% user identification accuracy after 14 seconds."
  - "num: AI-driven interfaces reduced task completion time by 36% and error rates by 29%."
  - "num: Financial institutions with intelligent UIs reported a 31.6% increase in transaction completion rates."
  - "Context-aware components reduced input errors by 56.8% compared to static interfaces."
  - "Zero-trust models reduced successful account compromises by 94.3%."
key_figures_tables:
  - "Table 1: Key efficiency and security metrics in financial interface evolution → Modern interfaces outperform traditional in all categories."
  - "Table 2: Comparative metrics for traditional vs. modern financial interface approaches → Adaptive approaches show significant improvements."
  - "Table 3: Operational efficiency benefits of event-driven architectures → Event-driven systems reduce latency and improve deployment frequency."
  - "Table 4: Business impact of intelligent financial UIs → Intelligent interfaces improve fraud detection and reduce support calls."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Behavioral biometrics"
    definition: "Analysis of user interaction patterns like typing rhythm and pointer movement for authentication."
  - term: "Event-driven architecture"
    definition: "A system design where events trigger and communicate between decoupled services."
  - term: "Zero-trust model"
    definition: "Security framework assuming potential compromise, requiring continuous verification."
  - term: "Progressive disclosure"
    definition: "UI design technique that reveals advanced features only when needed."
  - term: "Context-aware components"
    definition: "UI elements that adapt based on user, device, and transaction context."
critical_citations:
  - "[Gupta, 2022] — Provides data on mobile banking adoption and growth."
  - "[Xiong and Bu, 2024] — Details adaptive security policy modeling for financial systems."
  - "[Xu et al., 2024] — Presents empirical research on AI-driven UX/UI design in FinTech."
relevance:
  topics:
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "contextual"
      justification: "Mentions predictive adaptation and personalization, but doesn't focus on categorization specifically."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "high"
      justification: "Comprehensively reviews the evolution and limitations of traditional financial interfaces."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Directly addresses linear workflows, reactive security, and one-size-fits-all designs as key gaps."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses predictive interface adaptation using ML models to anticipate user actions."
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "contextual"
      justification: "Discusses progressive security and adaptive measures but not specifically infeasibility."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Focuses on behavioral biometrics and real-time fraud detection as forms of anomaly detection."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "medium"
      justification: "Mentions algorithms for behavioral analysis, but doesn't specify spending-data algorithms."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "medium"
      justification: "Contextually references mobile banking growth and adaptation, but not explicitly mobile-first design."
    - code: "9.B"
      name: "Mobile UX Design for Personal Finance"
      relevance: "medium"
      justification: "Discusses adaptive interfaces and progressive disclosure, relevant to mobile UX."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "Extensively covers security models, zero-trust, and behavioral biometrics for data protection."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides metrics and business case analysis for evaluating intelligent UI impact."
  contribution: "This paper provides a comprehensive framework for designing intelligent, event-driven UIs that directly informs Odin's architecture. It justifies the adoption of behavioral biometrics and zero-trust models for the security module. The findings on predictive adaptation and progressive disclosure support Odin's personalization and user experience design. The paper's business case metrics provide a benchmark for evaluating Odin's potential impact. The discussion on context-aware components offers a blueprint for Odin's adaptive interface logic."
  directly_justifies:
    - "Implementing event-driven architectures can reduce transaction latency by 64-78%."
    - "Behavioral biometrics can achieve 97.6% user identification accuracy after 14 seconds of interaction."
    - "Context-aware components reduce input errors by 56.8% compared to static interfaces."
    - "Zero-trust models reduce successful account compromises by 94.3%."
    - "Progressive disclosure reduces visual search time by 41.8% and cognitive load by 37.2%."
  limits:
    - "The paper is a review and synthesis, not presenting novel empirical research."
    - "Focuses primarily on general financial interfaces, not specifically on personal finance management (PFM) systems."
    - "Does not address specific implementation challenges for resource-constrained mobile environments."
  mapping_rationale: "A systematic scan across all 12 functional domains identified the paper as highly relevant to 'Existing Systems & Gaps' (4.A, 4.B), 'Anomaly Detection' (8.A), and 'Data Privacy & User Trust' (10.A), as it directly critiques traditional financial interfaces and proposes advanced security solutions. It was deemed medium relevance for 'Expense Categorization' (3.A), 'Spending Forecasting' (6.A), 'Mobile-First Design' (9.A, 9.B), and 'System Evaluation' (12.A) due to related but not central discussions. Domains like 'Filipino Cultural Context' (2.A-D), 'Behavioral Profiling' (5.A-C), and 'Budget Recommendation' (7.A-D) were considered but rejected as the paper does not address these specific areas. The paper's overall relevance to Odin is high for informing its architectural design, security features, and user experience principles."
limitations:
  - "The paper does not address cultural-specific financial practices like 'utang' or 'paluwagan' [unacknowledged]."
  - "It does not discuss the cold-start problem for new users without interaction history [unacknowledged]."
  - "The paper's focus is on transaction systems, not comprehensive PFM features like savings goals or debt management [unacknowledged]."
remember_this:
  - "Event-driven architectures reduce financial transaction latency by 64-78%."
  - "Behavioral biometrics can identify users with 97.6% accuracy after 14 seconds."
  - "Intelligent UIs reduced task completion time by 36% and error rates by 29%."
  - "Zero-trust models decreased successful account compromises by 94.3%."
  - "Context-aware components can reduce input errors by over 56%."
```
---

## Paper 22: Pandey & Awasthi_summarized.md

**Source File:** `Pandey & Awasthi_summarized.md`

```yaml
paper_id: 10.30574/ijsra.2025.15.1.1244
designation: international-algorithm-specific
title: How reinforcement learning can drive personalized financial wellness
authors: Pandey, V.; Awasthi, V.
year: 2025
venue: International Journal of Science and Research Archive
odin_topics:
  - 4.B
  - 5.A
  - 5.C
  - 7.A
  - 7.B
  - 11.A
  - 12.A
  - 12.B
  - 13.A
  - 13.B
tldr: Integrates reinforcement learning, behavioral clustering, and conversational NLP to deliver real-time personalized financial recommendations.
problem_and_motivation: Many individuals struggle with saving and budgeting effectively, yet traditional tools and robo-advisors offer generic, one-size-fits-all advice that fails to adapt to individual behavior and needs. Existing solutions lack real-time personalization and proactive optimization for user goals. A system that learns from user behavior and continuously adapts recommendations is needed.
approach:
  - Formulates personal finance as a Markov Decision Process with state (savings, month) and discrete actions (savings amounts).
  - Uses Deep Q-Network (DQN) with experience replay and target networks to learn optimal saving policies.
  - Applies K-Means clustering on synthetic income and saving rate data to define three user personas for personalization.
  - Augments the RL state with persona context to condition policies on user type.
  - Integrates OpenAI GPT-4 API as a conversational agent to translate RL recommendations into natural language advice.
  - Evaluates on a simulated 12‑month environment with stochastic shocks and sparse end-of-episode reward.
findings:
  - num: Learned DQN policy achieved average final savings of approximately $450 in greedy execution, versus $0 for naive saving and $564 for an ideal always-save benchmark.
  - num: Training reward rose from near $20 to around $120 over 10,000 episodes (with exploration), indicating effective learning.
  - num: The RL agent consistently kept final savings positive, avoiding debt in most trials.
  - Clustering produced three interpretable personas (low/mid/high income and saving rates), enabling persona‑driven policy adaptation.
  - The conversational agent generated empathetic, personalized explanations, which are argued to boost user engagement and trust.
key_figures_tables:
  - Figure 1: Scatter plot of synthetic users clustered by income and saving rate → three distinct persona groups are visible.
  - Figure 2: Training curve of DQN average final reward over episodes → reward increases toward optimal saving behavior.
key_equations:
  - equation: $Q(s,a) \leftarrow Q(s,a) + \alpha [r + \gamma \max_{a'} Q(s',a') - Q(s,a)]$
    explanation: Standard Q‑learning update for discrete state‑action values.
  - equation: $L(\theta) = E_{(s,a,r,s') \sim D}\left[ (r + \gamma \max_{a'} Q_{\theta^{-}}(s',a') - Q_{\theta}(s,a) )^2 \right]$
    explanation: DQN loss using target network for stable training.
definitions:
  - term: RL
    definition: Reinforcement Learning – a machine learning paradigm for sequential decision‑making.
  - term: DQN
    definition: Deep Q‑Network – a value‑based RL algorithm using neural networks.
  - term: MDP
    definition: Markov Decision Process – mathematical framework for modeling sequential decisions.
  - term: PFWA
    definition: Personalized Financial Wellness Agent – the proposed system.
critical_citations:
  - "[Mnih et al., 2015] — foundational DQN algorithm used."
  - "[D'Acunto et al., 2019] — discusses robo‑advisor limitations."
  - "[Lo et al., 2024] — personalization increases client adherence."
relevance:
  topics:
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Paper explicitly critiques generic advice and lack of adaptation in current PFM tools.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Uses K‑Means to create user personas from behavioral data.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Applies unsupervised clustering (K‑Means) for persona classification.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: RL agent learns optimal saving and debt‑repayment strategies through trial and error.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: Agent provides concrete saving amount recommendations each month.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: Conversational interface is designed to boost user engagement and trust.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Compares RL performance against baseline strategies in a simulated environment.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Reports training curves and quantitative savings outcomes of the RL module.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: The system aims to maximize end‑of‑period savings and handles emergency shocks.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: medium
      justification: Mentions debt repayment as part of the reward and action considerations.
  contribution: "This paper provides a blueprint for integrating reinforcement learning into a PFMS to deliver personalized, adaptive financial advice, directly applicable to Odin's recommendation engine. The persona clustering approach offers a solution to cold‑start personalization, aligning with Odin's user profiling module. The conversational NLP integration demonstrates how to improve user trust and engagement, which is critical for Odin's retention strategies. The evaluation methodology (simulated environment with stochastic events) can inform Odin's testing framework for algorithmic modules."
  directly_justifies:
    - "Reinforcement learning can learn optimal financial policies from sequential user data."
    - "Clustering users into behavioral personas improves recommendation relevance from the start."
    - "Conversational interfaces increase user engagement and trust in financial advice systems."
    - "Stochastic shocks should be modeled to evaluate robustness of saving strategies."
  limits:
    - "Synthetic data and simplified environment may not capture real‑world financial complexity."
    - "Lacks validation with real user data or user studies on engagement and trust."
    - "Assumes users follow recommendations; does not model user non‑compliance explicitly. [unacknowledged]"
    - "Does not address data privacy or security concerns inherent in handling financial data. [unacknowledged]"
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. Domains flagged as relevant include: Existing Systems & Gaps (4.B) – the paper directly critiques generic advice; Behavioral Profiling (5.A, 5.C) – clustering and persona identification are central; Budget Recommendation (7.A, 7.B) – RL provides actionable savings advice; Engagement (11.A) – conversational agent targets user interaction; System Evaluation (12.A, 12.B) – quantitative performance metrics are reported; Savings & Debt (13.A, 13.B) – savings and debt are part of the reward model. Domains rejected: Filipino Cultural Context (2.*) – no cultural or regional specificity; Expense Categorization (3.*) – no categorization framework; Spending Forecasting (6.*) – RL optimizes actions, not forecasts; Anomaly Detection (8.*) – not addressed; Mobile‑First (9.*) – no mobile design discussion; Data Privacy (10.*) – security not discussed; Retention (11.B) – mentioned but not a focus; Constrained Optimization (7.C, 7.D) – no explicit infeasibility handling. Borderline: 5.B (cold‑start) – clustering helps bootstrap, so included as medium; 12.C (evaluation of recommendation) – relevant but we chose 12.A and 12.B instead. Overall, the paper offers high relevance for Odin's personalization and recommendation modules, with supporting evidence for evaluation and engagement design."
limitations:
  - "Synthetic data may not generalize to real‑world user behavior."
  - "Simple environment with only saving actions does not capture full PFM complexity (e.g., investments, multiple accounts)."
  - "RL reward design (sparse, final savings only) may not reflect user satisfaction or realistic trade‑offs."
  - "No user study to validate engagement and trust claims. [unacknowledged]"
  - "Does not address integration with bank APIs or regulatory compliance. [unacknowledged]"
remember_this:
  - "DQN learned policy achieved average final savings of $450 in a 12‑month simulation."
  - "Clustering users into three personas enables tailored reward shaping and policy selection."
  - "Conversational AI using GPT‑4 improves explanation quality and user trust."
  - "Reinforcement learning can adapt to stochastic financial shocks like emergency expenses."
  - "Personalized recommendations from RL outperform generic baseline advice."
```
---

## Paper 23: Huang et al_summarized.md

**Source File:** `Huang et al_summarized.md`

```yaml
paper_id: "10.1145/3766918.3766944"
designation: "international-algorithm-specific"
title: "Wealth-Voyager: Navigating Intelligent Wealth Management with a Multi-Agent Framework"
authors: "Huang, R.; Zhao, Z.; Chen, S.; Wu, X.; Zhao, J. L."
year: 2025
venue: "2025 International Conference on Generative Artificial Intelligence for Business (GAIB 2025)"
odin_topics:
  - "5.A"
  - "5.B"
  - "7.B"
  - "9.A"
  - "9.B"
  - "10.B"
  - "12.A"
tldr: "A multi-agent LLM framework integrates behavioral profiling, real-time market intelligence, and portfolio optimization to deliver personalized, adaptive wealth management advice."
problem_and_motivation: "Traditional wealth management lacks scalability and personalization, while existing AI solutions are fragmented and fail to integrate long-term strategy with behavioral adaptation. A unified system is needed to address both quantitative performance and the cognitive biases that shape retail investor behavior."
approach:
  - "Wealth-Voyager coordinates four specialized agents: AssistHub (behavioral profiling), NewsCrawler (real-time intelligence), AlphaForge (portfolio optimization), and DualAdvisor (BDI-grounded advisory simulation)."
  - "The system uses a central LLM meta-controller to orchestrate agent collaboration via structured function calls and shared memory."
  - "Behavioral profiling quantifies nine cognitive biases (e.g., loss aversion, herding) to construct a user-specific behavioral vector."
  - "The DualAdvisor module simulates advisor-client dialogue with two LLM agents to uncover biases and promote reflective decision-making."
  - "AlphaForge employs constrained mean-variance optimization with liquidity caps and drawdown limits, augmented by Monte Carlo simulation."
  - "A proof-of-concept case study was conducted with a single mid-career participant over one month under live market conditions."
  - "The system compares a passive baseline, a behaviorally anchored portfolio, and a dynamically rebalanced tactical strategy."
findings:
  - "num: The tactical strategy outperformed the passive baseline by +1.62 percentage points in cumulative return during the evaluation period."
  - "num: Anchoring by behavioral signals improved annualized return from 3.72% to 6.53% and reduced annualized volatility from 18.08% to 9.42%."
  - "num: The tactical approach achieved a 1.86% cumulative return with 12.10% annualized volatility, compared to 0.24% and 13.70% for the anchored portfolio."
  - "The adaptive tactical adjustments effectively reduced losses during a tariff-induced shock (-2.56% vs. -2.79%) and captured greater upside during the rebound (3.24% vs. 2.16%)."
  - "Qualitative feedback indicated that the dual-agent simulation enhanced user trust and self-awareness by exposing cognitive biases."
key_figures_tables:
  - "Figure 1: Architecture of the Wealth-Voyager framework → System integrates four core modules orchestrated by an LLM meta-controller."
  - "Table 1: Comparison of user-declared baseline and AI-optimized allocation → AI optimization improved diversification and aligned with implicit risk profile."
  - "Figure 2: Segment-level returns for passive and tactical portfolios → Tactical strategy consistently outperformed across multiple market phases."
  - "Table 2: Performance comparison across strategies → Anchoring and tactical adjustments significantly improved risk-adjusted returns."
  - "Table 3: Capability comparison with market offerings → Wealth-Voyager uniquely supports real-time adjustment, personalization, and financial education."
key_equations:
  - equation: "L(w) = -Sharpe(w) + λ * IlliqPenalty(w)"
    explanation: "Objective function for portfolio optimization balancing Sharpe ratio and illiquidity."
  - equation: "None."
    explanation: ""
definitions:
  - term: "LLM"
    definition: "Large Language Model."
  - term: "BDI"
    definition: "Belief-Desire-Intention framework for modeling rational agency."
  - term: "SAA"
    definition: "Strategic Asset Allocation, the long-term policy portfolio."
  - term: "TAA"
    definition: "Tactical Asset Allocation, short-term adjustments to the SAA."
  - term: "PFMS"
    definition: "Personal Finance Management System."
critical_citations:
  - "[Brinson et al., 1986] — Asset allocation explains over 90% of performance variance."
  - "[Ibbotson & Kaplan, 2000] — Confirms asset allocation's dominant role in portfolio returns."
  - "[Pompian, 2016] — Risk profiling through a behavioral finance lens."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Directly proposes and implements a nine-dimensional behavioral vector for user profiling."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "high"
      justification: "Uses dynamic dialogue and BDI modeling to infer and adapt profiles, addressing cold-start."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Provides personalized portfolio allocation recommendations, a form of budget recommendation."
    - code: "9.A"
      name: "Mobile‑First Design Principles and Rationale"
      relevance: "contextual"
      justification: "The interactive, dialogue-based interface is relevant to mobile-first design but not a core focus."
    - code: "9.B"
      name: "Mobile UX Design for Personal Finance"
      relevance: "contextual"
      justification: "The system's conversational UX provides a relevant example but is not specifically mobile-first."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "medium"
      justification: "Explicitly addresses transparency, explainability, and trust through rationale tracing."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides an evaluation framework with quantitative performance and qualitative user feedback."
  contribution: "Wealth-Voyager contributes a modular architecture for PFMS that integrates behavioral profiling (relevant to modules 5.A, 5.B) with quantitative portfolio optimization. Its DualAdvisor module offers a novel method for bias-aware, interactive advisory that can inform the design of user engagement and trust-building features in Odin (modules 10.B, 11.A). The system's evaluation framework, comparing anchored and tactical strategies, provides a template for assessing Odin's algorithmic modules. The emphasis on transparent rationale generation directly informs Odin's requirements for user trust and explainability."
  directly_justifies:
    - "Multi-agent LLM frameworks can coordinate specialized financial tasks effectively."
    - "Incorporating behavioral biases into advisory dialogue improves user trust and engagement."
    - "Tactical asset allocation layered on strategic allocation improves risk-adjusted returns."
    - "Real-time market intelligence enables proactive portfolio rebalancing."
    - "Explainable, dialogue-based interfaces bridge the financial education-decision gap."
  limits:
    - "The proof-of-concept study was conducted on a single user, limiting generalizability."
    - "Performance is contingent on the underlying LLM, which may vary."
    - "The asset universe was limited, and the framework was not tested across diverse market regimes."
    - "The system's reliance on proprietary LLMs may raise cost and data privacy concerns. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes flagged the Behavioral Profiling & Classification, Budget Recommendation, Mobile-First Design, Data Privacy & User Trust, and System Evaluation domains as relevant. Topic 5.A (Financial Behavioral Profiles) and 5.B (Profile Dynamics) were rated high due to the paper's core contribution of a quantified behavioral vector and BDI-based dynamic profiling. Topic 7.B (Budget Recommendation) received medium relevance as the paper provides a method for personalized allocation, which is a form of budget recommendation. Topics 9.A and 9.B were rated contextual as the paper's dialogue interface is relevant to UX but not specifically mobile-first. Topic 10.B (User Trust) was rated medium due to the explicit focus on transparency and explainability. Topic 12.A (Evaluation Frameworks) was rated medium for its use of quantitative backtesting and qualitative feedback. Other domains, such as Expense Categorization (3.A-C), Existing Systems (4.A-B), Forecasting (6.A-B), Anomaly Detection (8.A-C), Savings & Debt Management (13.A-C), and others, were considered and rejected as the paper does not provide specific, citable claims informing those design areas for Odin. Overall, the paper is highly relevant for informing Odin's approach to behavioral profiling, interactive advisory design, and system evaluation."
limitations:
  - "Single-user pilot study, not statistically validated."
  - "Performance contingent on the underlying LLM model."
  - "Limited asset universe and market regime testing."
  - "Potential cost and data privacy concerns with proprietary LLM APIs. [unacknowledged]"
remember_this:
  - "A multi-agent LLM framework can coordinate behavioral profiling and portfolio optimization."
  - "Behavioral anchoring improved annual return by 2.81 percentage points in the case study."
  - "Tactical adjustments outperformed a passive baseline by 1.62 percentage points in cumulative return."
  - "Interactive, explainable dialogue enhances user trust and self-awareness."
  - "Integrating real-time news with BDI-based reasoning enables proactive portfolio management."
```
---

## Paper 24: Parameswaran & Saad_summarized.md

**Source File:** `Parameswaran & Saad_summarized.md`

```yaml
paper_id: "10.32890/jdsd2025.3.2.9"
designation: "international-algorithm-specific"
title: "Development and Evaluation of My Money Manager: An Intelligent Mobile App for Personalized Financial Insight"
authors: "Parameswaran, S.; Saad, S. Z."
year: 2025
venue: "Journal of Digital System Development"
odin_topics:
  - "3.A"
  - "3.B"
  - "4.A"
  - "4.B"
  - "7.A"
  - "7.B"
  - "8.A"
  - "8.B"
  - "9.A"
  - "9.B"
  - "10.A"
  - "10.B"
  - "12.A"
  - "13.A"
  - "13.C"
tldr: "My Money Manager is an Android app that distinguishes fixed and variable expenses, detects spending anomalies, and provides personalized savings recommendations based on 90-day spending patterns, evaluated with 35 users showing improved financial management."
problem_and_motivation: "Existing mobile finance apps lack intelligent personalization, failing to differentiate fixed versus variable expenses or adapt to individual spending patterns. Users need dynamic insights and anomaly detection to improve financial decisions. This app addresses the gap by providing tailored recommendations based on actual user behavior."
approach:
  - "Iterative and incremental development methodology with six phases: initiation, planning, design, development, testing, deployment."
  - "Android-based app using MVC architecture and Material Design principles."
  - "Algorithmic expense categorization distinguishes fixed (e.g., rent) from variable (e.g., dining) costs."
  - "Anomaly detection highlights unusual spending behaviors based on historical patterns."
  - "Personalized financial insights computed monthly from income, expenses, savings, ratio, and budget status."
  - "Visualizations include pie charts for expense distribution and trend analysis over time."
  - "Evaluation with 35 participants using six-point Likert-scale questionnaires across four dimensions."
findings:
  - "num: 82.8% of users confirmed income and expense tracking was efficient and reliable."
  - "num: 74.3% reported the app encouraged more effective financial management."
  - "num: 71.4% agreed financial insights helped guide financial decision-making."
  - "Ease of use was high for navigation, data entry, and budget setting (77.1% strongly agreed)."
  - "Understanding financial insights received lower ease ratings (37.1% strongly agreed, 14.3% somewhat difficult)."
  - "Security trust was a concern: only 11.4% strongly agreed data was safe, 31.4% somewhat disagreed."
key_figures_tables:
  - "Figure 2: Home screen dashboard showing balance, income, expenses, and quick actions → central financial overview."
  - "Figure 3: Add income/expense interfaces with streamlined forms → efficient data entry."
  - "Figure 4: Budget planning with progress bars and alerts → visual budget tracking."
  - "Figure 5: Financial summary with tabs and filters → organized transaction review."
  - "Figure 6: Financial insights with charts and anomaly detection → actionable intelligence from raw data."
  - "Figure 7: App experience responses → positive visual appeal and user-friendliness, mixed task completion independence."
  - "Figure 8: Perceived ease of use → core tasks rated easy, insights comprehension less so."
  - "Figure 9: Perceived usefulness → strong for tracking and habit improvement, moderate for insights."
  - "Figure 10: Perceived acceptance → high satisfaction, lower trust in accuracy and security."
  - "Tables 1-2: Detailed response percentages for ease and usefulness."
key_equations:
  - equation: "Monthly Income = Σ(all income entries for selected month)"
    explanation: "Sum of all income entries in the month."
  - equation: "Monthly Expenses = Σ(all expense entries for selected month)"
    explanation: "Sum of all expense entries in the month."
  - equation: "Monthly Savings = Monthly Income - Monthly Expenses"
    explanation: "Surplus for the month."
  - equation: "Income/Expense Ratio = Monthly Income ÷ Monthly Expenses"
    explanation: "Proportion of income to expenses."
  - equation: "Budget Status = Monthly Budget - Monthly Expenses"
    explanation: "Remaining budget amount."
  - equation: "Category Expense = Σ(all expenses for specific category in selected month)"
    explanation: "Total spending in a category."
  - equation: "Category Percentage = (Category Expense ÷ Monthly Expenses) × 100"
    explanation: "Share of total expenses by category."
definitions:
  - term: "None."
    definition: ""
critical_citations:
  - "[Shaikh et al., 2022] — identifies key drivers of mobile financial adoption."
  - "[Mijić & Ćebić, 2023] — applies UTAUT2 to personal finance app acceptance."
  - "[Carlin et al., 2022] — shows mobile apps improve financial behavior."
  - "[Forbes Advisor, 2024] — reviews existing apps like YNAB and PocketGuard."
relevance:
  topics:
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "high"
      justification: "Proposes algorithmic distinction between fixed and variable expenses."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      relevance: "high"
      justification: "Designs category selection with custom creation and predefined options."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews existing apps and their limitations."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Identifies gaps: lack of personalization, static advice, failure to differentiate costs."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "medium"
      justification: "Provides budget planning and alerts based on spending limits."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Offers personalized savings recommendations and budget adjustments."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Implements anomaly detection to highlight unusual spending behaviors."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "medium"
      justification: "Uses algorithmic analysis to detect anomalies but algorithm details are not specified."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "high"
      justification: "Follows mobile-first and material design principles for Android."
    - code: "9.B"
      name: "Mobile UX Design for Personal Finance"
      relevance: "high"
      justification: "Usability evaluation confirms intuitive navigation and user-friendly interfaces."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "medium"
      justification: "Evaluation reveals user concerns about data security, highlighting need for improvement."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "medium"
      justification: "Trust in accuracy and security was moderate, indicating areas for enhancement."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Conducts usability evaluation with Likert-scale questionnaires across multiple dimensions."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "medium"
      justification: "Provides savings recommendations and tracks savings as surplus."
    - code: "13.C"
      name: "End-of-Period Surplus as a Savings Input"
      relevance: "medium"
      justification: "Calculates monthly savings as income minus expenses, recommending savings strategies."
  contribution: "This paper directly supports Odin's expense categorization module by demonstrating a method to differentiate fixed and variable costs. Its anomaly detection feature informs Odin's anomaly detection subsystem. The usability evaluation framework can guide Odin's system evaluation approach. The findings on user trust and security concerns highlight critical design considerations for Odin's data privacy module. Finally, the savings recommendation logic informs Odin's budget recommendation and savings management functions."
  directly_justifies:
    - "Categorizing expenses into fixed and variable improves personalized financial insights."
    - "Anomaly detection can highlight unusual spending to prompt user awareness."
    - "Mobile-first design with intuitive interfaces enhances user adoption and satisfaction."
    - "User trust in data security is a significant factor for long-term retention."
    - "Usability evaluation with Likert scales effectively measures system acceptance."
  limits:
    - "Small sample size (n=35) limits generalizability [unacknowledged]."
    - "Algorithm for anomaly detection is not specified, hindering replication."
    - "Security and privacy measures are not detailed, despite user concerns."
    - "Long-term retention and engagement are not evaluated."
  mapping_rationale: "I systematically scanned all 12 functional domains and their associated topic codes. The paper directly addresses Expense Categorization (3.A, 3.B, high) and Anomaly Detection (8.A, high, 8.B, medium) through its algorithmic expense classification and anomaly highlighting features. It also provides strong support for Mobile-First Design (9.A, 9.B, high) and System Evaluation (12.A, high) through its iterative development and usability study. The paper's review of existing systems and gaps maps to 4.A and 4.B (medium). Budgeting strategies and recommendations (7.A, 7.B, medium) are evident in the budget planning and savings advice. Data privacy and trust (10.A, 10.B, medium) are surfaced by user concerns in the evaluation. Savings management (13.A, 13.C, medium) is touched upon via savings calculations and recommendations. Borderline cases include the distinction between expense categorization (3.A) and category design (3.B), both selected because the app designs categories and implements categorization logic. The paper does not address Filipino cultural context (domains 2.A-2.D) or behavioral profiling (5.A-5.C) beyond generic personalization, so those were rejected. Spending forecasting (6.A, 6.B) was not present as the app does not predict future spending. User retention (11.A, 11.B) and debt management (13.B) were not covered. Overall, the paper provides moderate to high relevance for several Odin modules, particularly in categorization, anomaly detection, mobile design, and evaluation."
limitations:
  - "Small sample size (n=35) limits generalizability [unacknowledged]."
  - "No long-term follow-up to assess sustained impact on financial habits [unacknowledged]."
  - "Algorithmic details for anomaly detection are not provided, preventing independent validation [unacknowledged]."
  - "Data security concerns identified in evaluation were not addressed in the design [unacknowledged]."
remember_this:
  - "82.8% of users rated income and expense tracking as efficient and reliable."
  - "74.3% reported improved financial management due to the app."
  - "Anomaly detection and expense categorization differentiate this app from basic trackers."
  - "User trust in data security emerged as a critical concern requiring attention."
  - "Iterative development with user feedback was effective for mobile app refinement."
```
---

## Paper 25: Ibrahim et al_summarized.md

**Source File:** `Ibrahim et al_summarized.md`

```yaml
paper_id: 10.1038/s41598-025-23116-6
designation: international-algorithm-specific
title: An equity aware recommender system for university admissions balancing operational constraints and strategic objectives
authors: Ibrahim, A.; Alarood, A.; Alsolami, E.
year: 2025
venue: Scientific Reports
odin_topics:
  - 7.D
  - 7.B
  - 12.C
  - 7.A
  - 5.B
  - 9.A
  - 10.A
  - 4.A
  - 4.B
tldr: Recommender system integrating CSP, goal programming, and Equity Theory to allocate university admissions under hard and soft constraints.
problem_and_motivation: Universities struggle to balance student demand against hard capacity limits and shifting soft policy goals, leading to over-enrolled programs, idle capacity, and inequitable access. Static planning and pure penalty-minimization approaches fail to adapt dynamically or maintain fairness. A method is needed that respects strict resource limits while making proportional, equitable adjustments as conditions change.
approach:
  - Models admissions as a dynamic CSP with hard constraints (faculty hours, room capacity) and soft constraints (performance, policy, balance) via adjustable penalty functions.
  - Introduces a penalty-based scaling that adjusts enrollments incrementally from a baseline, using normalized compliance scores to reward or reduce seats.
  - Incorporates Equity Theory to allow partially compliant programs controlled enrollments rather than outright exclusion.
  - Evaluates against Greedy and Simulated Annealing baselines using simulated data for 14 programs and 29,100 students over multiple cycles.
  - Measures performance via penalty scores, hard-constraint violations, Gini coefficient, and time to full compliance.
findings:
  - num: The approach maintains enrollment at 85–90% of total capacity, compared to 50–75% for Simulated Annealing and ~60% for Greedy.
  - num: Achieves a Gini coefficient of 0.067 for seat distribution, vs. 0.293 for SA and 0.387 for Greedy, with p<0.01 significance.
  - num: Institutions using this system reach full compliance in an average of 4.2 years, compared to 6.2 for SA and 7.6 for Greedy.
  - The approach prevents chronic underutilization and reduces violations more steadily than baselines.
  - The system achieves a robust balance between rapid violation reduction and stable enrollment figures.
  - Penalty-based scaling allows for proportional adjustments, preventing abrupt cuts that disrupt ongoing cohorts.
  - Sensitivity analysis shows moderate annual reductions of 10–20% significantly improve compliance without new violations.
key_figures_tables:
  - "Table 1: Summary of our method's performance across programs → Shows penalty scores and percentage change in admissions for 14 programs, with Medicine and Sports Science receiving increases and all others receiving reductions."
  - "Figure 1: Comparison of student allocations across different approaches → Illustrates that our method produces balanced adjustments, while SA and Greedy create extreme increases and cuts."
  - "Figure 2: Comparison of Gini Coefficients Across Methods → Our method has the lowest Gini (0.067), indicating superior fairness."
  - "Figure 3: Average Utilization of Hard Constraints Across Five Iterative Admission Cycles → Our recommender consistently achieves 85–90% utilization, preventing underutilization."
  - "Table 2: Average Time (Years) to Eliminate Violations Over Five Admission Cycles → Our recommender is fastest at 4.2 years."
  - "Table 3: Sensitivity analysis of admission reductions → Shows that 25% annual reduction yields 70% hard compliance and 50% soft compliance."
  - "Table 4: Reduction strategy → Compares large vs. gradual reduction strategies, showing trade-offs between speed and stability."
key_equations:
  - equation: C_p = ∑_{i=1}^n min(R_i, S_i) * α(i,p)
    explanation: Infrastructure capacity per program using room and section limits.
  - equation: ∑_{i ∈ C_p, dept(i)=d} (⌈X/S_i⌉ × H_i) ≤ T_{faculty,d}
    explanation: Faculty capacity constraint per department for a given enrollment X.
  - equation: S_p^{rec} = S_p^0 [1 + ((S_p^{max} - S_p^0)/S_p^0)(1 - 2(P_{soft}(p)/P_{max}))]
    explanation: Recommended admission formula integrating hard capacity and soft penalty.
definitions:
  - term: CSP
    definition: Constraint Satisfaction Problem; a framework for solving allocation problems with strict and flexible rules.
  - term: Equity Theory
    definition: A social psychology theory positing fairness as a ratio of inputs to outcomes, used here to justify proportional allocations.
  - term: Hard constraints
    definition: Non-negotiable limits like faculty hours and room capacity.
  - term: Soft constraints
    definition: Flexible institutional objectives like graduation rates and policy mandates.
  - term: Goal programming
    definition: An optimization technique for balancing multiple competing objectives.
critical_citations:
  - "[Minton et al., 1992] — Foundational CSP algorithm for minimizing conflicts."
  - "[Adams, 1965] — Introduced Equity Theory used to justify proportional allocations."
  - "[Kirkpatrick et al., 1983] — Simulated Annealing baseline for comparison."
  - "[Beyrouthy et al., 2009] — Highlights underutilization of university teaching space."
relevance:
  topics:
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: high
      justification: "Directly addresses hard vs. soft constraint trade-offs with penalty-based scaling."
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: "Framework for recommending allocations under constraints directly parallels budget recommendation."
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: high
      justification: "Uses multi-year simulations, Gini coefficient, and utilization metrics applicable to PFMS evaluation."
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: "Provides domain knowledge on allocating limited resources under multiple constraints."
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: "Warm-start optimization and iterative adjustments inform how profiles might evolve."
    - code: 9.A
      name: Mobile‑First Design Principles and Rationale
      relevance: contextual
      justification: "Mentions interpretability and transparency relevant for user-facing design, but not mobile-specific."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: "Discusses user trust and transparency of recommendations, but privacy is not a core focus."
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: "Reviews existing allocation methods, providing baseline context."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: contextual
      justification: "Identifies gaps in static planning and equity-blind algorithms."
  contribution: "Provides a formal methodology for constraint-based resource allocation that directly informs Odin's budget recommendation module. The iterative penalty-based adjustment mechanism offers a blueprint for how Odin can handle infeasible budget allocations (Topic 7.D). The paper's use of Equity Theory and proportional scaling justifies Odin's fairness-aware allocation design. Its evaluation framework, including multi-year simulations and Gini coefficient, sets a standard for assessing Odin's recommendation quality. The warm-start optimization concept is directly applicable to updating user budgets dynamically."
  directly_justifies:
    - "Hard constraints like income must be strictly enforced, while soft constraints like savings goals can be penalized."
    - "Incremental adjustments from a baseline prevent drastic, disruptive changes to user budgets."
    - "Equity-based scaling ensures partially compliant users are not excluded from budget recommendations."
    - "Multi-year simulations are a valid method for evaluating long-term budget adherence."
    - "Moderate, proportional adjustments (10-20%) improve compliance without introducing new violations."
  limits:
    - "Validated only on simulated data; real-world institutional complexity may differ."
    - "Assumes stable soft constraint targets; does not handle rapidly shifting external mandates dynamically."
    - "Evaluation focused on a single Saudi institutional context; generalizability to other settings, including the Philippines, is untested."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes flagged the Constraint Optimization domain as most relevant, particularly codes 7.D (high), 7.B (high), and 12.C (high), due to the paper's direct methodological contribution to handling infeasible allocations and evaluating them. Topics under Existing Systems (4.A, 4.B) and Behavioral Profiling (5.B) were considered contextual or medium, as the paper reviews static planning gaps and uses iterative adjustments analogous to profile updates. The Filipino cultural context (2.A-2.D), Expense Categorization (3.A-3.C), Forecasting (6.A-6.B), Anomaly Detection (8.A-8.C), Savings & Debt (13.A-13.C), and Retention (11.A-11.B) were rejected as the paper does not address those domains. The paper's algorithmic focus on penalty-based scaling and fairness provides strong justification for Odin's budget optimization module, though its admissions context requires translation to personal finance."
limitations:
  - "Based on simulated rather than real-world enrollment data. [unacknowledged]"
  - "Assumes stable policy objectives; rapid external shifts may outpace the model. [unacknowledged]"
  - "Fairness measured primarily via Gini; other equity dimensions may require additional metrics. [acknowledged]"
  - "Tested only on a single institutional dataset; generalizability to other universities or countries is untested. [unacknowledged]"
  - "One-factor-at-a-time sensitivity analysis overlooks interactions between multiple parameters. [acknowledged]"
remember_this:
  - "The recommender maintains enrollment at 85–90% of total capacity."
  - "It achieves a Gini coefficient of 0.067 for equitable seat distribution."
  - "Full compliance is reached in an average of 4.2 years."
  - "Moderate annual reductions of 10–20% improve compliance without new violations."
  - "The system integrates hard constraints, soft penalties, and equity theory."
```
---


---

## Agent Instruction

If the agent reading this document believes further context about a paper is needed, it may request the original converted markdown file (with the '_marked' suffix) from the user for the relevant paper(s).
