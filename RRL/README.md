# Topic Outline
## Development of Odin: A Personal Budget Management System Using LSTM, Classification Algorithm, and Recommendation Algorithm

---

## A. Target Users and the Financial Problem

### A.1 Spending and Budgeting Behavior of Filipino Young Professionals

- Income structure typology of Filipino young professionals
  > *Scholar query: income structure Filipino young professionals salaried freelance informal*

- Budgeting time horizons practiced by Filipino young professionals
  > *Scholar query: budgeting time horizon weekly monthly Filipino young adults personal finance*

- Documented expenditure patterns by income stability type
  > *Scholar query: expenditure patterns Filipino young professionals income type*

- Budgeting behavior prevalence and methods in this demographic
  > *Scholar query: budgeting behavior Filipino millennials Gen Z personal finance habits*

- Failure points: irregular tracking, overspending, unplanned expenses
  > *Scholar query: financial management failure points irregular tracking overspending Filipino*

- Financial behavior differences across income stability types
  > *Scholar query: financial behavior income stability variable irregular earners Philippines*

- Culturally specific obligations: remittances, paluwagan, religious contributions
  > *Scholar query: paluwagan remittances religious spending Filipino cultural financial obligations*

- Case for intelligent budgeting over financial literacy interventions
  > *Scholar query: intelligent budgeting system vs financial literacy intervention effectiveness*

---

### A.2 Existing Personal Finance and Budget Management Systems

- Classification and typology of PFMS/PBMS in literature
  > *Scholar query: personal finance management system classification typology literature review*

- Dominant features of existing systems and their effectiveness
  > *Scholar query: personal budget management system features evaluation effectiveness*

- Documented limitations: data entry burden, lack of intelligence, no forecasting, no anomaly detection
  > *Scholar query: personal finance app limitations manual entry no forecasting generic categories*

- Budget recommendation approaches in existing systems
  > *Scholar query: budget recommendation rule-based algorithmic personal finance systems*

- Budgeting strategies technically implemented in existing systems
  > *Scholar query: budgeting strategies zero-based envelope 50-30-20 implemented finance app*

- Gap between existing systems and an intelligent, adaptive, locally grounded system
  > *Scholar query: gap existing PFMS intelligent adaptive localized personal finance Philippines*

---

## B. Mobile-First Design and Deployment Constraints

### B.1 Mobile-First Design in Personal Finance Systems

- Definition and distinction of mobile-first vs. desktop-first PFMS
  > *Scholar query: mobile-first personal finance app design definition deployment approach*

- Evidence of mobile-first dominance among younger users in emerging markets
  > *Scholar query: mobile-first personal finance emerging market Philippines young users adoption*

- Technical constraints: compute, connectivity, screen real estate, battery
  > *Scholar query: mobile app technical constraints limited compute bandwidth personal finance ML*

- Influence of mobile constraints on ML algorithm selection
  > *Scholar query: algorithm selection mobile constraints lightweight model forecasting anomaly detection*

- Mobile UX patterns minimizing transaction input burden
  > *Scholar query: mobile UX design minimize input burden personal finance transaction logging*

---

## C. Budget Recommendation Theory and Algorithm

### C.1 Budgeting Strategies and Budget Recommendation

- Core mechanics of documented budgeting strategies
  > *Scholar query: budgeting strategies zero-based envelope pay-yourself-first proportional mechanics comparison*

- Strengths and weaknesses per strategy by income type
  > *Scholar query: budgeting strategy effectiveness stable variable irregular income comparison*

- Multi-strategy distillation into one unified technical configuration
  > *Scholar query: hybrid budgeting strategies unified system distillation technical implementation*

- Technical implementation of budget recommendation in existing systems
  > *Scholar query: budget recommendation system implementation rule-based algorithmic user-configured*

- Algorithmic approaches: constraint optimization, MCDM, reinforcement learning, recommender systems
  > *Scholar query: budget recommendation algorithm constraint optimization MCDM reinforcement learning*

- Budget period resetting: surplus reset vs. carryforward by income type
  > *Scholar query: budget surplus carryforward reset period variable stable income personal finance*

- Budget recommendation behavior under absent or lump-sum income
  > *Scholar query: budget recommendation lump-sum income irregular earner cold-start personal finance*

- Minimum user input requirements for accurate budget recommendation
  > *Scholar query: minimum user input budget recommendation accuracy tradeoff intelligent system*

---

### C.2 Budget Recommendation Algorithm

- Problem formulation: optimization, ranking, prediction, or recommendation
  > *Scholar query: budget recommendation problem formulation optimization ranking classification literature*

- Algorithms applied to resource allocation and budget distribution problems
  > *Scholar query: resource allocation budget distribution algorithm financial personal literature*

- Algorithmic approaches documented in PFMS/PBMS contexts specifically
  > *Scholar query: budget recommendation algorithm personal finance management system applied*

- Tradeoffs: mobile feasibility, explainability, adaptability, cold-start performance
  > *Scholar query: budget algorithm tradeoffs explainability mobile feasibility cold-start adaptability*

- Justification of chosen algorithm over alternatives for Odin's use case
  > *Scholar query: budget recommendation algorithm justification mobile personal finance Filipino context*

---

## D. Spending Forecasting

### D.1 Predictive Modeling in Personal Finance Systems

- Forecasting methods applied to personal finance spending data
  > *Scholar query: forecasting methods ARIMA LSTM XGBoost personal finance spending prediction comparison*

- Characterization of personal finance data as sequential time-series vs. tabular
  > *Scholar query: personal finance spending data time-series sequential structure characterization*

- Temporal dependency in spending: evidence that prior periods influence subsequent periods
  > *Scholar query: temporal dependency spending behavior sequential influence personal finance*

- Interaction between mobile deployment constraints and forecasting model choice
  > *Scholar query: forecasting algorithm mobile deployment constraints lightweight model personal finance*

- Cold-start fallback mechanisms for forecasting without sufficient transaction history
  > *Scholar query: cold-start forecasting fallback personal finance transaction history insufficient*

- Per-category forecasting across multiple simultaneous spending categories
  > *Scholar query: per-category spending forecasting multiple categories personal finance model*

---

### D.2 LSTM as the Spending Forecasting Algorithm

- LSTM architecture and the class of sequential dependency problems it solves
  > *Scholar query: LSTM architecture sequential dependency time-series modeling overview*

- LSTM strengths and weaknesses relative to alternative forecasting models
  > *Scholar query: LSTM vs ARIMA XGBoost Random Forest forecasting comparison strengths weaknesses*

- LSTM applied to household expenditure and personal spending data
  > *Scholar query: LSTM household expenditure personal spending budget forecasting applied*

- LSTM for simultaneous multi-category forecasting
  > *Scholar query: LSTM multi-output multi-category forecasting simultaneous spending categories*

- LSTM feasibility on mobile and resource-constrained systems
  > *Scholar query: LSTM mobile deployment resource-constrained lightweight compression inference*

- Justification of LSTM over surveyed alternatives for Odin's data and system context
  > *Scholar query: LSTM justified sequential personal finance mobile spending Filipino context*

---

## E. Anomaly and Overage Detection

### E.1 Anomaly Detection in Personal Finance Systems (Domain)

- Definition and taxonomy of detectable financial anomalies and overage events
  > *Scholar query: financial anomaly definition taxonomy personal finance detectable events*

- Threshold-based overage alerting vs. behavioral baseline deviation: distinction and appropriateness
  > *Scholar query: threshold budget overage vs behavioral anomaly detection personal finance distinction*

- Detection approaches applied to personal finance data and their results
  > *Scholar query: anomaly detection personal finance Isolation Forest One-Class SVM rule-based results*

- Tradeoffs between rule-based and algorithmic detection: complexity, explainability, accuracy
  > *Scholar query: rule-based vs algorithmic anomaly detection explainability accuracy tradeoff*

- Detection output feeding back into subsequent budget recommendation
  > *Scholar query: anomaly detection feedback loop budget recommendation PFMS documented*

- Filipino culturally specific spending recognized as expected, not anomalous
  > *Scholar query: cultural spending Filipino remittances paluwagan festival anomaly detection protected*

- Alert surfacing design: format, frequency, and framing to minimize alert fatigue
  > *Scholar query: anomaly alert design format frequency framing user experience finance app*

---

### E.2 Anomaly Detection Algorithm

- Anomaly detection as an ML problem: major algorithmic families
  > *Scholar query: anomaly detection machine learning families unsupervised supervised approaches overview*

- Isolation Forest: establishing per-user behavioral baselines without labeled data
  > *Scholar query: Isolation Forest unsupervised per-user baseline anomaly detection unlabeled data*

- Unsupervised anomaly detection applied to personal spending transaction data
  > *Scholar query: unsupervised anomaly detection personal finance transaction data Isolation Forest applied*

- Tradeoffs: mobile feasibility, false positive rates, user-facing explainability
  > *Scholar query: Isolation Forest mobile feasibility false positive explainability personal finance*

- Justification of chosen approach over alternatives for Odin's use case
  > *Scholar query: anomaly detection algorithm justification mobile personal finance behavioral Filipino*

---

## F. User Profiling and Classification

### F.1 User Behavioral Profiling in Filipino Personal Finance Contexts (Domain)

- Role of user profiling in budget recommendation, forecasting fallback, and personalization
  > *Scholar query: user profiling role budget recommendation personalization personal finance system*

- Inadequacy of Western financial behavioral taxonomies for Filipino users
  > *Scholar query: Western financial behavioral taxonomy inadequate Filipino context cultural differences*

- Filipino-specific financial behavioral patterns from BSP CFS and FIES
  > *Scholar query: Filipino financial behavior patterns BSP CFS FIES institutional data profiling*

- Documented Filipino financial archetypes or constructing profiles from institutional data
  > *Scholar query: Filipino financial behavioral archetypes segments FIES BSP profile construction*

- Behavioral dimensions as meaningful profile differentiators: income stability, obligation weight, savings disposition
  > *Scholar query: behavioral dimensions financial profiling income stability obligation savings flexibility*

- Concept drift as a framework for progressively updating user profiles over time
  > *Scholar query: concept drift user behavioral modeling profile update progressive personal finance*

- Behavioral signals that should trigger profile reassessment
  > *Scholar query: profile reassessment triggers spending shift income change obligation behavioral signals*

- Automatic vs. user-confirmed profile updates
  > *Scholar query: profile update automatic user confirmation behavioral system design*

- Cold-start problem and profile-average fallback approaches
  > *Scholar query: cold-start personalized financial system profile-average fallback approaches documented*

---

### F.2 Profile Classification Algorithm

- Supervised classification vs. clustering for predefined profile categories
  > *Scholar query: supervised classification vs clustering predefined categories financial user profiling*

- Classification algorithms documented for behavioral and financial user profiling
  > *Scholar query: classification algorithm behavioral financial user profiling logistic regression SVM Random Forest*

- Feature selection: onboarding questionnaire responses vs. early transaction history
  > *Scholar query: feature selection user profiling onboarding questionnaire transaction history classification*

- Cold-start classification: training without labeled user data at launch
  > *Scholar query: classification cold-start no labeled data launch synthetic training financial profiling*

- Progressive profile reclassification: periodic, continuous, or drift-triggered
  > *Scholar query: progressive reclassification profile update drift detection periodic continuous behavioral*

- Tradeoffs across candidate classifiers: accuracy, interpretability, mobile feasibility
  > *Scholar query: classification algorithm tradeoffs accuracy interpretability mobile feasibility comparison*

- Justification of chosen classifier for Odin's four-profile structure and context
  > *Scholar query: profile classifier justification four-class Filipino financial system mobile*

---

## G. Expense Categorization

### G.1 Expense Categorization in Filipino Personal Finance Contexts

- Approaches to expense categorization: user-defined, institutionally derived, ML-generated, hybrid
  > *Scholar query: expense categorization approaches user-defined institutional ML personal finance*

- Limitations of generic Western expense categories for Filipino spending
  > *Scholar query: Western expense categories limitations Filipino context personal finance*

- PSA FIES and BSP CFS expenditure categories and their mapping to Odin
  > *Scholar query: PSA FIES BSP CFS expenditure categories Filipino personal finance mapping*

- Cultural expense types in literature: paluwagan, remittances, religious obligations
  > *Scholar query: paluwagan remittances religious obligations expense category Filipino literature*

- Basis for protected categories and minimum spending floors
  > *Scholar query: protected expense categories minimum spending floor essentials investments BSP*

- Category design in existing PFMS serving Filipino users
  > *Scholar query: expense category design Filipino personal finance app local vs Western categories*

- SSS and Pag-IBIG: automatic deductions for employees vs. voluntary inclusions for variable users
  > *Scholar query: SSS Pag-IBIG expense categorization regular employee vs freelance personal finance*

---

## H. Data Privacy, Security, and User Trust

### H.1 Data Privacy, Security, and User Trust in Personal Finance Systems

- Sensitivity classification of financial data in literature
  > *Scholar query: financial data sensitivity classification personal information privacy literature*

- Technical security standards for financial applications
  > *Scholar query: financial app security encryption authentication data minimization best practices*

- User trust in financial applications and its effect on data-sharing behavior
  > *Scholar query: user trust financial app data sharing behavior design factors*

- Privacy concerns as a driver of inconsistent transaction logging
  > *Scholar query: privacy concerns transaction logging behavior personal finance app retention*

- Philippine regulatory framework: RA 10173, BSP guidelines, NPC issuances
  > *Scholar query: Republic Act 10173 Data Privacy Act BSP NPC financial data Philippines compliance*

- Privacy-by-design applied in comparable financial system research
  > *Scholar query: privacy by design financial system personal data application research*

- Privacy implications of self-reported manual financial data without banking integration
  > *Scholar query: self-reported financial data privacy manual input no banking integration*

---

## I. User Retention and Engagement

### I.1 User Retention and Engagement in Personal Finance Systems

- Relationship between data completeness and ML model performance in PFMS
  > *Scholar query: transaction data completeness ML model performance personal finance logging*

- User drop-off patterns in personal finance applications: when and why users stop
  > *Scholar query: user drop-off retention personal finance app logging cessation behavior*

- Primary friction point in PFMS engagement: manual data entry burden
  > *Scholar query: manual data entry friction personal finance app engagement barrier*

- Non-gamification retention mechanisms: notifications, frictionless entry, immediate feedback, goals
  > *Scholar query: non-gamification retention personal finance app notification frictionless entry value feedback*

- Minimum viable interaction frequency for a finance app to remain useful
  > *Scholar query: minimum interaction frequency personal finance app engagement usefulness*

- Demonstrated system value as a retention mechanism in itself
  > *Scholar query: perceived system value retention engagement personal finance forecast accuracy alert*

---

## J. System Evaluation

### J.1 System Evaluation in Personal Finance and Budget Management Systems

- Evaluation frameworks, metrics, and methodologies used for existing PFMS/PBMS
  > *Scholar query: personal finance management system evaluation framework metrics methodology*

- ISO/IEC 25010:2023 quality characteristics and their relevance to evaluating Odin
  > *Scholar query: ISO IEC 25010 2023 software quality characteristics evaluation application*

- System Usability Scale: administration, measurement scope, and relevance to mobile-first systems
  > *Scholar query: System Usability Scale SUS mobile application usability evaluation*

- Combining ISO 25010 and SUS in software system evaluations
  > *Scholar query: ISO 25010 SUS combined evaluation software system study*

- ISO 25010 and SUS applied to PFMS or comparable financial applications
  > *Scholar query: ISO 25010 SUS personal finance management system evaluation applied*

- Documented limitations of SUS and ISO 25010 as evaluation frameworks
  > *Scholar query: SUS ISO 25010 limitations evaluation framework acknowledged*

- Sample size and respondent profile appropriate for SUS evaluation
  > *Scholar query: SUS evaluation sample size respondent profile comparable study*

---

*Generated for Team Aesir (Group 4) — Odin Thesis, University of Makati*
*Adviser: Prof. Mary Ellaine R. Cervantes | SME: Dr. Pamela A. Go*