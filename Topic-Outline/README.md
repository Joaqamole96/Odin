# Topic Outline
## Development of Odin: A Personal Budget Management System Using LSTM, Classification Algorithm, and Recommendation Algorithm

---

## A. Target Users and the Financial Problem [/Financial-Problem]

### A.1 Spending and Budgeting Behavior of Filipino Young Professionals [/Financial-Behavior]

- Income structure typology of Filipino young professionals [/Income-Structure]
  > *Scholar query: typology of income structures among Filipino young professionals including salaried employees, freelance workers, gig economy participants, and informal sector earners – personal finance behavior Philippines*

- Budgeting time horizons practiced by Filipino young professionals [/Budget-Horizons]
  > *Scholar query: common budgeting time horizons (weekly, bi-weekly, monthly, per paycheck) used by Filipino young adults and millennials in personal finance management – empirical study*

- Documented expenditure patterns by income stability type [/Expenditure-Patterns]
  > *Scholar query: expenditure patterns and consumption behavior differences among Filipino young professionals grouped by income stability (fixed salary vs. variable freelance vs. irregular informal) – household spending analysis*

- Budgeting behavior prevalence and methods in this demographic [/Habits-and-Prevalence]
  > *Scholar query: prevalence of budgeting habits and methods (envelope system, digital apps, spreadsheets, mental budgeting) among Filipino millennials and Gen Z – personal financial management survey*

- Failure points: irregular tracking, overspending, unplanned expenses [/Failure-Points]
  > *Scholar query: common financial management failure points among young adults including inconsistent transaction logging, overspending episodes, and unplanned emergency expenses – behavioral finance literature*

- Financial behavior differences across income stability types [/Variability-and-Differences]
  > *Scholar query: comparative financial behaviors between stable income earners and variable/irregular income earners in the Philippines – savings, spending, and budgeting adaptation strategies*

- Culturally specific obligations: remittances, paluwagan, religious contributions [/Cultural-Obligations]
  > *Scholar query: cultural financial obligations in Filipino households – remittances to family, paluwagan (rotating savings), religious contributions (church offerings, fiestas) – personal finance ethnography*

- Case for intelligent budgeting over financial literacy interventions [/Case-for-System]
  > *Scholar query: effectiveness comparison between intelligent adaptive budgeting systems and traditional financial literacy interventions for improving personal finance outcomes – systematic review*

---

### A.2 Existing Personal Finance and Budget Management Systems [/Existing-Systems]

- Classification and typology of PFMS/PBMS in literature [/Typology]
  > *Scholar query: literature review on classification and typology of personal finance management systems (PFMS) and personal budget management systems (PBMS) – feature-based categorization and design patterns*

- Dominant features of existing systems and their effectiveness [/Features]
  > *Scholar query: effectiveness evaluation of dominant features in personal budget management systems – transaction categorization, spending tracking, goal setting, alerts, reporting – user satisfaction metrics*

- Documented limitations: data entry burden, lack of intelligence, no forecasting, no anomaly detection [/Limitations]
  > *Scholar query: documented limitations of personal finance applications – manual data entry burden, absence of predictive forecasting, lack of intelligent anomaly detection, generic category structures – user reviews and usability studies*

- Budget recommendation approaches in existing systems [/Approaches]
  > *Scholar query: budget recommendation techniques implemented in personal finance systems – rule-based methods, algorithmic suggestions, user-configured strategies (e.g., 50/30/20, zero-based) – comparative analysis*

- Budgeting strategies technically implemented in existing systems [/Implementation]
  > *Scholar query: technical implementation of documented budgeting strategies (zero-based budgeting, envelope method, pay-yourself-first, proportional budgeting) in commercial personal finance applications*

- Gap between existing systems and an intelligent, adaptive, locally grounded system [/Gaps]
  > *Scholar query: research gap analysis – lack of intelligent, adaptive, and culturally localized personal finance management systems for emerging markets like the Philippines – comparative study*

---

## B. Mobile-First Design and Deployment Constraints [/Mobile-First-Design]

### B.1 Mobile-First Design in Personal Finance Systems [/Mobile-First-Design]

- Definition and distinction of mobile-first vs. desktop-first PFMS [/Definition]
  > *Scholar query: definition and distinction between mobile-first and desktop-first design approaches for personal finance management systems – usability, feature prioritization, deployment strategy*

- Evidence of mobile-first dominance among younger users in emerging markets [/Adoption]
  > *Scholar query: adoption rates and usage patterns of mobile-first personal finance applications among young adults in emerging markets (Southeast Asia, Philippines) – market survey and behavioral data*

- Technical constraints: compute, connectivity, screen real estate, battery [/Constraints]
  > *Scholar query: technical constraints of mobile platforms for personal finance applications – limited computational resources, intermittent network connectivity, small screen size, battery life optimization strategies*

- Influence of mobile constraints on ML algorithm selection [/ML-Selection]
  > *Scholar query: how mobile deployment constraints (compute, memory, energy) influence machine learning algorithm selection for forecasting and anomaly detection in on-device personal finance systems*

- Mobile UX patterns minimizing transaction input burden [/UX-and-Input]
  > *Scholar query: mobile user experience patterns that minimize manual transaction entry burden in personal finance apps – voice input, photo receipt scanning, predictive text, template shortcuts*

---

## C. Budget Recommendation [/Budget-Recommendation]

### C.1 Budget Recommendation Theory and Fundamentals [/Fundamentals]

- Core mechanics of documented budgeting strategies [/Core-Mechanics]
  > *Scholar query: core mechanics and operational definitions of major budgeting strategies – zero-based budgeting (assign every peso), envelope system (physical/virtual categories), pay-yourself-first, proportional (50/30/20) – comparative analysis*

- Strengths and weaknesses per strategy by income type [/Strengths-and-Weaknesses]
  > *Scholar query: comparative strengths and weaknesses of budgeting strategies (zero-based, envelope, proportional) when applied to stable salary vs. variable freelance vs. irregular income types – personal finance literature*

- Multi-strategy distillation into one unified technical configuration [/Distillation-and-Configuration]
  > *Scholar query: methods to distill multiple budgeting strategies into a single unified technical configuration (hybrid approach) for a budget recommendation system – algorithmic integration techniques*

- Technical implementation of budget recommendation in existing systems [/Implementation]
  > *Scholar query: technical implementation approaches for budget recommendation in existing personal finance systems – rule-based logic, user-configurable parameters, machine learning suggestions – case studies*

- Algorithmic approaches: constraint optimization, MCDM, reinforcement learning, recommender systems [/Approaches]
  > *Scholar query: algorithmic approaches for budget recommendation – constraint optimization, multi-criteria decision making (MCDM), reinforcement learning, collaborative filtering recommender systems – applied personal finance*

- Budget period resetting: surplus reset vs. carryforward by income type [/Resetting]
  > *Scholar query: budget period resetting rules – surplus reset (start fresh each period) vs. surplus carryforward (accumulate unused budget) – appropriateness for stable vs. variable income earners*

- Budget recommendation behavior under absent or lump-sum income [/Lump-Sum-Handling]
  > *Scholar query: budget recommendation system behavior during cold-start or lump-sum income scenarios (e.g., bonuses, freelance payments, irregular remittances) – handling missing or intermittent income data*

- Minimum user input requirements for accurate budget recommendation [/Minimum-Input]
  > *Scholar query: trade-off between minimum user input and budget recommendation accuracy in intelligent personal finance systems – cold-start strategies, onboarding question design, early transaction history needs*

---

### C.2 Budget Recommendation Algorithm and Application [/Application]

- Problem formulation: optimization, ranking, prediction, or recommendation [/Problem-Formulation]
  > *Scholar query: problem formulation for budget recommendation – is it an optimization problem (resource allocation), ranking problem (priority ordering), prediction problem (future spending), or recommendation problem (personalized suggestion)? – literature review*

- Algorithms applied to resource allocation and budget distribution problems [/Allocation]
  > *Scholar query: algorithms documented for resource allocation and budget distribution problems in personal finance – linear programming, evolutionary algorithms, heuristic rules – comparative performance*

- Algorithmic approaches documented in PFMS/PBMS contexts specifically [/PFMS]
  > *Scholar query: specific algorithmic approaches used in personal finance management systems for budget recommendation – examples from academic papers and commercial apps (e.g., Mint, YNAB, Goodbudget)*

- Tradeoffs: mobile feasibility, explainability, adaptability, cold-start performance [/Tradeoffs]
  > *Scholar query: trade-offs among budget recommendation algorithms – mobile feasibility (compute/memory), explainability to users, adaptability to spending changes, cold-start performance with limited data*

- Justification of chosen algorithm over alternatives for Odin's use case [/Justification]
  > *Scholar query: justification framework for selecting a budget recommendation algorithm for mobile personal finance in Filipino context – compare rule-based, constrained optimization, and lightweight ML – criteria: local cultural obligations, variable income, minimal input*

---

## D. Spending Forecasting [/Spending-Forecasting]

### D.1 Predictive Modeling in Personal Finance Systems [/Predictive Modeling]

- Forecasting methods applied to personal finance spending data [/Methods]
  > *Scholar query: comparative review of forecasting methods for personal finance spending data – ARIMA, exponential smoothing, LSTM, XGBoost, Prophet – prediction accuracy and suitability*

- Characterization of personal finance data as sequential time-series vs. tabular [/Data Characterization]
  > *Scholar query: characterization of personal transaction data – is it inherently sequential time-series with temporal dependencies, or can it be treated as tabular (independent) data? – implications for model selection*

- Temporal dependency in spending: evidence that prior periods influence subsequent periods [/Temporal Dependency]
  > *Scholar query: empirical evidence of temporal dependency in household and personal spending – do prior spending periods significantly influence subsequent periods? – autocorrelation and time-series analysis*

- Interaction between mobile deployment constraints and forecasting model choice [/Mobile Forecasting Constraints]
  > *Scholar query: how mobile deployment constraints (limited compute, battery, storage) influence selection of spending forecasting models – trade-offs between model complexity, inference speed, and energy efficiency*

- Cold-start fallback mechanisms for forecasting without sufficient transaction history [/Cold Start Forecasting]
  > *Scholar query: cold-start fallback mechanisms for spending forecasting when transaction history is insufficient – demographic-based averages, rule-based defaults, transfer learning, hybrid approaches*

- Per-category forecasting across multiple simultaneous spending categories [/Multi Category Forecasting]
  > *Scholar query: methods for per-category spending forecasting across multiple categories simultaneously (e.g., food, transport, utilities) – multi-output models, separate models per category, hierarchical approaches*

---

### D.2 LSTM as the Spending Forecasting Algorithm [/LSTM Forecasting]

- LSTM architecture and the class of sequential dependency problems it solves [/LSTM Architecture]
  > *Scholar query: Long Short-Term Memory (LSTM) neural network architecture – how it models sequential dependencies and long-range temporal patterns – overview of gates, cell state, and backpropagation through time*

- LSTM strengths and weaknesses relative to alternative forecasting models [/LSTM vs Alternatives]
  > *Scholar query: comparative strengths and weaknesses of LSTM vs. ARIMA, XGBoost, Random Forest, and GRU for time-series forecasting – accuracy, training data requirements, interpretability, computational cost*

- LSTM applied to household expenditure and personal spending data [/LSTM Spending]
  > *Scholar query: applications of LSTM to household expenditure and personal spending forecasting – empirical studies on transaction sequences, daily/weekly spending patterns, prediction horizons*

- LSTM for simultaneous multi-category forecasting [/LSTM Multi Category]
  > *Scholar query: LSTM architectures for simultaneous multi-category spending forecasting – multi-output LSTM, sequence-to-sequence, attention mechanisms – handling category correlations*

- LSTM feasibility on mobile and resource-constrained systems [/LSTM Mobile]
  > *Scholar query: feasibility of deploying LSTM models on mobile and resource-constrained devices – model compression (pruning, quantization), lightweight LSTM variants, on-device inference benchmarks*

- Justification of LSTM over surveyed alternatives for Odin's data and system context [/LSTM Justification]
  > *Scholar query: justification for selecting LSTM as spending forecasting algorithm for Odin's mobile personal finance system in Filipino context – sequential nature of spending, variable income patterns, multi-category needs, mobile feasibility*

---

## E. Anomaly and Overage Detection [/Anomaly and Overage Detection]

### E.1 Anomaly Detection in Personal Finance Systems (Domain) [/Anomaly Detection Domain]

- Definition and taxonomy of detectable financial anomalies and overage events [/Anomaly Taxonomy]
  > *Scholar query: definition and taxonomy of detectable financial anomalies and overage events in personal finance – transaction outliers, category overspending, behavioral deviations, pattern breaks – classification framework*

- Threshold-based overage alerting vs. behavioral baseline deviation: distinction and appropriateness [/Threshold vs Behavioral]
  > *Scholar query: distinction between threshold-based overage alerting (fixed limit exceedance) and behavioral baseline deviation (statistical anomaly from user's norm) – when each is appropriate in personal finance systems*

- Detection approaches applied to personal finance data and their results [/Detection Approaches]
  > *Scholar query: anomaly detection methods applied to personal finance transaction data – Isolation Forest, One-Class SVM, autoencoders, rule-based heuristics – reported results on false positive rates and detection accuracy*

- Tradeoffs between rule-based and algorithmic detection: complexity, explainability, accuracy [/Rule vs Algorithmic Tradeoffs]
  > *Scholar query: trade-offs between rule-based anomaly detection (simple, explainable) and algorithmic detection (complex, adaptive) in personal finance – implementation complexity, user explainability, detection accuracy*

- Detection output feeding back into subsequent budget recommendation [/Detection Feedback Loop]
  > *Scholar query: feedback loop mechanisms where anomaly detection output (e.g., identified overspending events) informs subsequent budget recommendation adjustments – documented systems and algorithms*

- Filipino culturally specific spending recognized as expected, not anomalous [/Cultural Protection]
  > *Scholar query: handling culturally specific spending patterns (remittances, paluwagan, fiesta contributions, religious offerings) in anomaly detection – preventing false positives by excluding protected categories or events*

- Alert surfacing design: format, frequency, and framing to minimize alert fatigue [/Alert Design]
  > *Scholar query: user interface design for anomaly alerts in personal finance apps – optimal format (push, email, in-app), frequency (real-time, daily summary), framing (positive/neutral language) to minimize alert fatigue*

---

### E.2 Anomaly Detection Algorithm [/Anomaly Detection Algorithm]

- Anomaly detection as an ML problem: major algorithmic families [/ML Anomaly Families]
  > *Scholar query: anomaly detection as a machine learning problem – major algorithmic families (supervised, unsupervised, semi-supervised) and their applicability to personal finance transaction data*

- Isolation Forest: establishing per-user behavioral baselines without labeled data [/Isolation Forest]
  > *Scholar query: Isolation Forest algorithm for unsupervised anomaly detection – how it builds per-user behavioral baselines from unlabeled transaction data – isolation trees, anomaly score, threshold selection*

- Unsupervised anomaly detection applied to personal spending transaction data [/Unsupervised Spending Anomaly]
  > *Scholar query: unsupervised anomaly detection applied to personal spending transaction data – case studies using Isolation Forest, DBSCAN, autoencoders – handling categorical and numerical features*

- Tradeoffs: mobile feasibility, false positive rates, user-facing explainability [/Anomaly Tradeoffs]
  > *Scholar query: trade-offs for anomaly detection in mobile personal finance – computational feasibility on device, acceptable false positive rates (<5%), explainability for end users (why was this flagged?) – comparative analysis*

- Justification of chosen approach over alternatives for Odin's use case [/Anomaly Justification]
  > *Scholar query: justification for selecting Isolation Forest as anomaly detection algorithm for Odin's mobile Filipino personal finance system – unsupervised (no labeled anomalies), low memory footprint, explainable scores, handles mixed data types*

---

## F. User Profiling and Classification [/User Profiling and Classification]

### F.1 User Behavioral Profiling in Filipino Personal Finance Contexts (Domain) [/User Profiling Domain]

- Role of user profiling in budget recommendation, forecasting fallback, and personalization [/Profiling Role]
  > *Scholar query: role of user behavioral profiling in personal finance systems – enabling personalized budget recommendations, providing forecasting fallbacks during cold-start, adapting system behavior to user type*

- Inadequacy of Western financial behavioral taxonomies for Filipino users [/Western Taxonomy Inadequacy]
  > *Scholar query: critiques of applying Western financial behavioral taxonomies (e.g., US/European spending types) to Filipino users – cultural differences in obligations, savings norms, risk tolerance, social factors*

- Filipino-specific financial behavioral patterns from BSP CFS and FIES [/Filipino Institutional Data]
  > *Scholar query: financial behavioral patterns of Filipino households derived from institutional surveys – Bangko Sentral ng Pilipinas Consumer Finance Survey (BSP CFS) and Philippine Statistics Authority Family Income and Expenditure Survey (FIES)*

- Documented Filipino financial archetypes or constructing profiles from institutional data [/Filipino Archetypes]
  > *Scholar query: documented financial behavioral archetypes or segments in Filipino population – e.g., savers, spenders, remitters – constructed from FIES and BSP CFS data – cluster analysis or typology studies*

- Behavioral dimensions as meaningful profile differentiators: income stability, obligation weight, savings disposition [/Behavioral Dimensions]
  > *Scholar query: key behavioral dimensions for profiling personal finance users – income stability (fixed vs. variable), obligation weight (remittances, debt, family support), savings disposition (goal-oriented vs. residual) – empirical validation*

- Concept drift as a framework for progressively updating user profiles over time [/Concept Drift]
  > *Scholar query: concept drift as a framework for progressively updating user behavioral profiles in personal finance systems – detecting changes in spending patterns, income stability, life circumstances – adaptation mechanisms*

- Behavioral signals that should trigger profile reassessment [/Profile Triggers]
  > *Scholar query: behavioral signals that should trigger user profile reassessment in personal finance systems – significant spending shift, income change, new financial obligation, change in savings behavior – empirical thresholds*

- Automatic vs. user-confirmed profile updates [/Profile Update Method]
  > *Scholar query: design trade-offs between automatic user profile updates (silent adaptation) and user-confirmed updates (transparent, opt-in) in personal finance systems – user trust and engagement effects*

- Cold-start problem and profile-average fallback approaches [/Cold Start Profiling]
  > *Scholar query: cold-start problem in personalized personal finance systems – using profile-average or demographic-based fallback profiles when individual user history is insufficient – methods and evaluation*

---

### F.2 Profile Classification Algorithm [/Profile Classification Algorithm]

- Supervised classification vs. clustering for predefined profile categories [/Supervised vs Clustering]
  > *Scholar query: comparison between supervised classification (using predefined labels) and unsupervised clustering (discovering natural groups) for financial user profiling – which is appropriate when target profiles are defined a priori?*

- Classification algorithms documented for behavioral and financial user profiling [/Classification Algorithms]
  > *Scholar query: classification algorithms documented for behavioral and financial user profiling – logistic regression, support vector machines, random forest, gradient boosting, neural networks – comparative accuracy and interpretability*

- Feature selection: onboarding questionnaire responses vs. early transaction history [/Feature Selection]
  > *Scholar query: feature selection strategies for classifying personal finance user profiles – combining onboarding questionnaire responses (demographic, self-reported behavior) with early transaction history (spending patterns) – predictive power*

- Cold-start classification: training without labeled user data at launch [/Cold Start Classification]
  > *Scholar query: methods for training a user profile classifier without labeled data at system launch – synthetic data generation, transfer learning from institutional surveys (FIES/BSP), rule-based initial assignment*

- Progressive profile reclassification: periodic, continuous, or drift-triggered [/Progressive Reclassification]
  > *Scholar query: strategies for progressive reclassification of user profiles over time – periodic (e.g., monthly), continuous (real-time update), or drift-triggered (only when behavior changes significantly) – trade-offs*

- Tradeoffs across candidate classifiers: accuracy, interpretability, mobile feasibility [/Classifier Tradeoffs]
  > *Scholar query: trade-offs among candidate classifiers for mobile personal finance user profiling – prediction accuracy, model interpretability (explainable to user), mobile deployment feasibility (model size, inference speed)*

- Justification of chosen classifier for Odin's four-profile structure and context [/Classifier Justification]
  > *Scholar query: justification for selecting a specific classifier (e.g., random forest or lightweight gradient boosting) for Odin's four-profile Filipino personal finance system – accuracy on multi-class problem, feature importance interpretability, mobile on-device inference*

---

## G. Expense Categorization [/Expense Categorization]

### G.1 Expense Categorization in Filipino Personal Finance Contexts [/Expense Categorization Domain]

- Approaches to expense categorization: user-defined, institutionally derived, ML-generated, hybrid [/Categorization Approaches]
  > *Scholar query: approaches to expense categorization in personal finance systems – user-defined custom categories, institutionally derived standard taxonomies (e.g., COICOP), ML-generated from transaction descriptions, hybrid – strengths and weaknesses*

- Limitations of generic Western expense categories for Filipino spending [/Western Categories Limitation]
  > *Scholar query: limitations of applying generic Western expense categories (e.g., from US or European apps) to Filipino spending behavior – missing categories like remittances, paluwagan, tricycle fares, sari-sari store purchases*

- PSA FIES and BSP CFS expenditure categories and their mapping to Odin [/FIES BSP Mapping]
  > *Scholar query: expenditure classification systems used in Philippine Statistics Authority Family Income and Expenditure Survey (PSA FIES) and BSP Consumer Finance Survey (CFS) – mapping to personal finance app categories for Odin*

- Cultural expense types in literature: paluwagan, remittances, religious obligations [/Cultural Expenses]
  > *Scholar query: literature documenting culturally specific expense types in Filipino personal finance – paluwagan (rotating savings and credit association), remittances to family, religious obligations (church, fiestas) – categorization recommendations*

- Basis for protected categories and minimum spending floors [/Protected Categories]
  > *Scholar query: rationale for protected expense categories (essentials: food, utilities, housing) and minimum spending floors in budgeting systems – preventing harmful budget cuts – behavioral economics and best practices*

- Category design in existing PFMS serving Filipino users [/Filipino PFMS Categories]
  > *Scholar query: expense category design in personal finance management systems that serve Filipino users – local apps vs. international apps – comparison of category lists and user adaptation strategies*

- SSS and Pag-IBIG: automatic deductions for employees vs. voluntary inclusions for variable users [/SSS PagIBIG]
  > *Scholar query: categorization of mandatory and voluntary contributions to SSS (Social Security System) and Pag-IBIG (Home Development Mutual Fund) for Filipino personal finance – regular employees (automatic deductions) vs. freelancers/self-employed (voluntary)*

---

## H. Data Privacy, Security, and User Trust [/Data Privacy Security Trust]

### H.1 Data Privacy, Security, and User Trust in Personal Finance Systems [/Privacy Security Trust Domain]

- Sensitivity classification of financial data in literature [/Data Sensitivity]
  > *Scholar query: sensitivity classification of financial data in privacy literature – what constitutes personally identifiable financial information (PIFI) – transaction details, balances, income, spending habits – risk levels*

- Technical security standards for financial applications [/Security Standards]
  > *Scholar query: technical security standards and best practices for financial applications – encryption at rest and in transit (TLS, AES), authentication (biometric, 2FA), secure data storage, certificate pinning – OWASP Mobile Top 10*

- User trust in financial applications and its effect on data-sharing behavior [/User Trust]
  > *Scholar query: factors influencing user trust in personal finance applications – transparency, data control, perceived security, brand reputation – effect on willingness to share transaction data and maintain regular logging*

- Privacy concerns as a driver of inconsistent transaction logging [/Privacy Logging Inconsistency]
  > *Scholar query: how user privacy concerns lead to inconsistent transaction logging in personal finance apps – fear of data breach, reluctance to share detailed spending, resulting in incomplete data and degraded ML performance*

- Philippine regulatory framework: RA 10173, BSP guidelines, NPC issuances [/Philippine Regulations]
  > *Scholar query: Philippine regulatory framework for financial data privacy – Republic Act 10173 (Data Privacy Act of 2012), BSP Circulars on data protection (e.g., BSP 808, 1016), National Privacy Commission (NPC) issuances – compliance requirements for personal finance apps*

- Privacy-by-design applied in comparable financial system research [/Privacy by Design]
  > *Scholar query: privacy-by-design principles applied in financial system research – data minimization, purpose limitation, on-device processing, differential privacy, user consent – case studies in personal finance apps*

- Privacy implications of self-reported manual financial data without banking integration [/Self Reported Privacy]
  > *Scholar query: privacy implications of self-reported manual transaction logging (no bank API integration) in personal finance apps – reduced data exposure, user control over what is shared, potential for selective omission – trade-offs with system intelligence*

---

## I. User Retention and Engagement [/User Retention and Engagement]

### I.1 User Retention and Engagement in Personal Finance Systems [/Retention Engagement Domain]

- Relationship between data completeness and ML model performance in PFMS [/Data Completeness]
  > *Scholar query: relationship between transaction data completeness and machine learning model performance (forecasting, anomaly detection, budget recommendation) in personal finance systems – empirical studies on missing data impact*

- User drop-off patterns in personal finance applications: when and why users stop [/Drop Off Patterns]
  > *Scholar query: user drop-off and churn patterns in personal finance applications – typical time points (e.g., after 2 weeks, 1 month), reasons (manual entry fatigue, no perceived value, privacy concerns) – retention analysis studies*

- Primary friction point in PFMS engagement: manual data entry burden [/Manual Entry Friction]
  > *Scholar query: manual data entry as the primary friction point causing low engagement in personal finance management systems – user effort vs. perceived benefit – interaction cost and abandonment rates*

- Non-gamification retention mechanisms: notifications, frictionless entry, immediate feedback, goals [/Retention Mechanisms]
  > *Scholar query: non-gamification retention mechanisms for personal finance apps – smart notifications (timing, content), frictionless entry (templates, shortcuts, voice), immediate system feedback (savings progress, alerts), goal setting – effectiveness evidence*

- Minimum viable interaction frequency for a finance app to remain useful [/Minimum Interaction]
  > *Scholar query: minimum viable interaction frequency for a personal finance app to remain useful to users – daily, weekly, per paycheck, per transaction? – relationship between logging frequency and perceived value of insights*

- Demonstrated system value as a retention mechanism in itself [/System Value Retention]
  > *Scholar query: demonstrated system value (accurate forecasts, helpful alerts, useful recommendations) as a retention mechanism in personal finance systems – does perceived accuracy and usefulness drive continued engagement more than gamification?*

---

## J. System Evaluation [/System Evaluation]

### J.1 System Evaluation in Personal Finance and Budget Management Systems [/Evaluation Domain]

- Evaluation frameworks, metrics, and methodologies used for existing PFMS/PBMS [/Evaluation Frameworks]
  > *Scholar query: evaluation frameworks, metrics, and methodologies used in academic and industry studies of personal finance management systems – usability, effectiveness, user satisfaction, behavioral outcomes – systematic review*

- ISO/IEC 25010:2023 quality characteristics and their relevance to evaluating Odin [/ISO 25010]
  > *Scholar query: ISO/IEC 25010:2023 software quality characteristics (functional suitability, performance efficiency, compatibility, usability, reliability, security, maintainability, portability) – relevance to evaluating a mobile personal finance system*

- System Usability Scale: administration, measurement scope, and relevance to mobile-first systems [/SUS]
  > *Scholar query: System Usability Scale (SUS) – administration protocol (10-item questionnaire, 5-point Likert), scoring (0-100), interpretation – relevance and validation for evaluating mobile-first personal finance applications*

- Combining ISO 25010 and SUS in software system evaluations [/ISO SUS Combined]
  > *Scholar query: methodological approaches combining ISO/IEC 25010 quality characteristics assessment with System Usability Scale (SUS) scores for comprehensive software system evaluation – case studies in mobile apps*

- ISO 25010 and SUS applied to PFMS or comparable financial applications [/ISO SUS PFMS]
  > *Scholar query: studies applying ISO/IEC 25010 and/or System Usability Scale (SUS) to evaluate personal finance management systems or comparable financial applications (banking apps, expense trackers) – reported results and lessons*

- Documented limitations of SUS and ISO 25010 as evaluation frameworks [/Limitations SUS ISO]
  > *Scholar query: documented limitations of System Usability Scale (SUS) – small sample sensitivity, lack of diagnostic detail, cultural bias – and ISO/IEC 25010 – complexity, resource intensity – acknowledged in literature*

- Sample size and respondent profile appropriate for SUS evaluation [/SUS Sample Size]
  > *Scholar query: recommended sample size and respondent profile for conducting a System Usability Scale (SUS) evaluation – power analysis, minimum N (often 12-20 for formative, 30+ for summative), representation of target user group (Filipino young professionals)*

---