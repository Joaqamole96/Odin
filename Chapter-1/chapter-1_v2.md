# **CHAPTER I** **INTRODUCTION**

| This section discusses what parts or subsections are expected in the first chapter. Commonly, the introduction of a research paper is a critical section that sets the stage for the entire study. vvv |
| ----- |

## **Project Context**

| In the opening paragraph, it is essential to provide an introduction to the broader field of study, setting the stage for your specific research focus. This context establishes the relevance of your research within a larger domain. You may begin by outlining the significance of the overarching topic, discussing its contemporary relevance, and highlighting the key issues or trends. vvv |
| ----- |

The intersection of financial technology and machine learning has reshaped how individuals manage personal finances. Mobile and web-based budgeting applications have moved from passive expense recording toward intelligent systems capable of forecasting future spending and delivering personalized financial guidance (D'Acunto & Rossi, 2023; Ellyana et al., 2025). Long Short-Term Memory (LSTM) networks have demonstrated strong performance in modeling financial time series data, enabling accurate spending predictions based on historical patterns (Bhavana et al., 2025). Ensemble classification methods such as Random Forest have been applied to profile users based on behavioral and financial features, enabling systems to adapt their recommendations to individual financial circumstances (Zlobin & Bazylevych, 2025; Bader & Haraty, 2025). Anomaly detection algorithms, particularly Isolation Forest, have been applied to identify spending deviations from established behavioral baselines in financial transaction streams without requiring labeled training data (D'Souza et al., 2026; Bader & Haraty, 2025). Together, these techniques represent an expanding frontier of what personal finance management systems can offer.

| In the second paragraph, you can delve deeper into your specific research area within the broader field. Explain why this particular aspect of the topic is worth investigating. Discuss the relevant literature and existing research that has laid the foundation for your research focus. This should help the reader understand why your specific angle on the topic is important and the knowledge gaps or unanswered questions it addresses. vvv |
| ----- |

Within the broader domain of machine learning-driven personal finance and budget management, the specific focus of this study is the application of Random Forest for financial behavioral profile classification, LSTM for forecasting, Isolation Forest for anomaly detection, and Linear Programming for budget recommendation to the digital budgeting needs of Filipino working young adults in Metro Manila. The income structures, spending patterns, financial behavioral profiles, and cultural nuances of this demographic differ substantially from those of users in foreign countries, for which the aforementioned intelligent budgeting tools were designed (Cho, 2024; Casalhay et al., 2025). Filipino working young adults operate within a financial landscape shaped by a mix of stable and variable income sources, including salaried employment, freelance work, and platform-based labor, alongside an array of culturally specific financial obligations that have no direct equivalent in Western personal finance frameworks (Jandoc et al., 2026; Donato et al., 2023). These obligations include family remittances, informal rotating savings arrangements (*paluwagan*), community and religious contributions, and government-mandated statutory contributions, which function as non-negotiable expense floors rather than discretionary choices (Bongalonta et al., 2024; Bayangos & Lubangco, 2024; Casino et al., 2025). Compounding this, behavioral evidence consistently shows that among Filipino working young adults, demographic and structural factors such as income type, employment category, and obligation weight are stronger predictors of financial behavior than financial literacy, and that knowledge-focused interventions consistently fail to bridge the literacy-to-behavior gap without structural behavioral support (Dimaunahan et al., 2025; Lim & Cordova, 2024). This creates a need for a context-specific system that adapts its intelligent techniques to local financial realities rather than importing foreign behavioral assumptions wholesale.

| In the third paragraph, transition to a clear and concise presentation of your main research problem or questions. State your problem in a straightforward manner, emphasizing its significance. This paragraph should provide a seamless transition from the general topic to the specific problem your study seeks to address. vvv |
| ----- |

The core problem this research aims to address is the absence of a locally developed, machine learning-driven personal budget management system tailored to Filipino working young adults aged 20 to 40 residing or working in Metro Manila. While commercial budgeting applications and academic prototypes have demonstrated the technical feasibility of algorithms such as LSTM in forecasting, none have been designed to accommodate the specific financial behavioral profiles, culturally grounded expense structures, and income volatility patterns that characterize this demographic. This gap means that Filipino working young adults who wish to benefit from intelligent budgeting tools must either adapt to systems built for foreign financial contexts or forgo such tools entirely.

| To establish the existence of the problem, the fourth paragraph should present evidence or data that supports the claim that the problem you've identified is real and substantial. Cite relevant statistics, studies, or real-world examples that illustrate the issue's prevalence or impact. This evidence not only reinforces the importance of your research but also helps convince the reader of the problem's validity. vvv |
| ----- |

The existence of this problem is substantiated by national financial data, academic research, and a pilot survey conducted among the target demographic. The Bangko Sentral ng Pilipinas reported that while 57.4% of total retail transactions were conducted digitally in 2024, structural gaps in financial management behavior persist (Mesina-Romero et al., 2024). Only 2% of Filipino adults correctly answered all six financial literacy assessment items, and 41% borrow money not for emergencies but to meet regular spending needs (Cacnio & Romarate, 2024). Even among those who engage with digital financial tools, adoption does not necessarily translate into sound financial behavior: Bongado et al. (2025) found that digital wallet usage among Filipino students did not correspond to improved financial discipline, and Calanog et al. (2025) documented the prevalence of impulsive buy-now-pay-later behavior facilitated by digital platforms. The pilot survey of Filipino working young adults in Metro Manila (N=45) found that the majority rely on no formal budgeting tool, with 51% reporting that their income is insufficient to cover expenses and 27% citing difficulty tracking expenses. These findings confirm that the target population not only struggles with basic budgeting, but also lacks access to intelligent digital tools adapted to their financial realities.

| In the fifth paragraph, delve into a discussion of the causes and effects of the main problem. Explain what factors contribute to the problem's existence and why it persists. Discuss the consequences or implications of the problem, both on a broader scale and within specific contexts. This analysis helps the reader grasp the complexity and significance of the issue. vvv |
| ----- |

The persistence of this problem can be attributed to two reinforcing factors. The first is behavioral and attitudinal: research documents a tendency among Filipino working young adults to prioritize immediate needs over long-term planning, with payday-cycle dynamics predictably shaping spending peaks and troughs: first-trip-after-payday spending runs measurably higher than spending in later periods, and the petsa de peligro pre-payday scarcity period follows as a structural consequence (Ma et al., 2026; Canete & Liwanag, 2024). The second is structural: the financial obligations of Filipino working young adults extend well beyond the categories captured by most personal financial tools, encompassing statutory government contributions, family remittances, community collections, religious donations, and paluwagan arrangements (Casino et al., 2025; Donato et al., 2023; Bayangos & Lubangco, 2024). These factors cause existing intelligent budgeting systems to produce generic and contextually irrelevant forecasts and recommendations, which discourages sustained use. Consequently, working young adults remain trapped in reactive spending cycles, unable to leverage machine learning-driven tools that could otherwise support structured financial planning, savings accumulation, and debt management (Ataza et al., 2024; Espiritu, 2025). Developing a system grounded in the actual income patterns, obligation structures, and behavioral profiles of this demographic can address these gaps in ways that imported solutions cannot.

## **Purpose and Description of the Study**

| In this section, you will introduce the perceived solution to the problem addressed in your research. Explain the strategy or approach that your study will take to address the problem. Additionally, highlight the key system features or components that will be integral to this solution. Start by discussing the identified problem briefly. You have already established this problem's existence and significance in previous sections. Introduce the perceived solution. This could be the development of a specialized system, a novel methodology, or an innovative approach to tackling the problem. Outline the core strategy or methodology you plan to employ. Explain how this strategy aligns with the specific problem you're addressing. This provides context for the reader, helping them understand how your solution is tailored to the problem. Detail the key system features or components that are central to your solution. This can include technology, algorithms, or methods that make your approach unique and effective. These features should directly support the proposed solution. vvv |
| ----- |

In response to the gap between Filipino working young adults' financial management needs and the capabilities of existing budgeting tools, this research proposes the development of Odin, a mobile and web personal budget management system that integrates Random Forest, LSTM, Isolation Forest, and Linear Programming. The core strategy of this solution involves classifying users into one of four financial behavioral profiles: Stable-Flexible, Stable-Obligated, Variable-Flexible, and Variable-Obligated, based on income stability and obligation weight during onboarding, with reclassification triggered by detected changes in spending and income behavior over time; training the LSTM model on historical transaction data to forecast future spending per category over daily, weekly, and monthly horizons, with a cold-start fallback for users with insufficient transaction history; applying Isolation Forest to detect spending patterns that deviate significantly from each user's established behavioral baseline, supplemented by rule-based budget overspending detection; and generating budget allocations through Linear Programming, anchored to the user's financial behavioral profile, transaction history, and declared preferences. These intelligent features are supported by manual income and expense transaction entry using a locally grounded spending category structure, savings goal tracking, and debt management guidance.

| In this section, you will clearly state the primary purpose of your research. Describe what you intend to achieve with your study and how it directly relates to the perceived solution presented in the first paragraph. Begin by explicitly stating the purpose of your study. This purpose should be specific and concise. Connect the purpose to the problem you identified earlier. Explain how achieving this purpose will contribute to addressing the problem or filling a knowledge gap. Highlight the desired outcomes or results that will indicate the successful accomplishment of your study's purpose. vvv |
| ----- |

The primary purpose of this study is to design, develop, and evaluate Odin as a functional mobile and web personal budget management system for Filipino working young adults aged 20 to 40 residing or working in Metro Manila. This purpose directly addresses the absence of a locally developed, machine learning-driven budgeting tool that accounts for the specific financial realities of this demographic, including variable income structures, culturally obligated expense categories, and spending patterns unique to the Filipino context. By achieving this purpose, the study aims to provide Filipino working young adults with an intelligent tool that delivers predictive, behavior-aware financial guidance, supporting structured budgeting discipline and progress toward savings and debt reduction goals.

| In this section, you will emphasize the significance of your research within the larger context of the field or industry it pertains to. Discuss the potential impact and benefits of your study, both theoretically and practically.Start by explaining why your study is significant. What makes it relevant and important? Consider the potential implications for the field, industry, or community. Discuss the practical applications or real-world relevance of your research. How might the findings or outcomes of your study be applied to solve real problems or improve existing systems? Mention any potential contributions to the academic field, such as advancing knowledge or methodologies in a particular area of study. vvv |
| ----- |

This study holds significant implications for its primary and secondary beneficiaries. For users, Odin offers a practical, accessible tool for structured personal budget management that accounts for their income variability, cultural financial obligations, and spending behavior, supporting progress toward savings accumulation, debt reduction, and long-term financial stability (Bai, 2023; Dela Torre et al., 2025). For researchers, this study contributes a financial behavioral profile framework grounded in Philippine institutional data, a locally validated spending category structure derived from FIES and BSP Consumer Finance Survey frameworks, and an evaluation approach combining ISO/IEC 25010:2023 and the System Usability Scale that may serve as a reference for future intelligent personal finance system research in the Philippine context and comparable emerging economies. For developers, this research provides a reference architecture that integrates Random Forest, LSTM, Isolation Forest, and Linear Programming within a single mobile-first personal budget management system, demonstrating how these algorithms can be composed and evaluated in a resource-constrained, manual-input financial application. For the financial technology industry, Odin demonstrates that intelligent budgeting systems can be designed to reflect the structural and cultural financial realities of Filipino users, contributing to the broader national agenda of financial inclusion and the development of locally relevant financial technology solutions (Albert et al., 2024; Akinyemi, 2025).

## **Objectives**

| Begin your objective with a clear and concise statement of purpose. In this case, the purpose is to create a web-based scoring application for Arnis techniques. Clearly specify what the study aims to cover. In this case, it's basic Arnis striking and blocking techniques. Include the method, algorithm or technology you will use to achieve your objective. Here, it's the HPE algorithm (Human Pose Estimation). State what you expect to achieve by implementing this web-based scoring application. In this case, the expected outcome is the automation of the scoring process and convenience in learning for all entities involved. Use action verbs to convey what you intend to do. In this case, verbs like "design," "develop," and "implement" indicate specific actions. vvv |
| ----- |

The study aims to design, develop, and evaluate Odin, a mobile and web personal finance management system for Filipino working young adults aged 20 to 40 residing or working in Metro Manila, using Random Forest, LSTM, Linear Programming, and Isolation Forest.

## **Specific Objectives**

In order to fulfill the main objective of this project, the authors constructed the following specific objectives: 

| This objective aims to establish a strong foundational understanding of the key components related to Arnis poses and scoring. Ensure that the objective specifies what aspects of the business process are relevant to your research. If no business understanding is required then this objective may be optional. vvv |
| ----- |

1. Examine and understand the financial behavioral patterns, income structures, spending habits, expense categories, and cultural financial practices of Filipino working young adults, as well as the behavioral dimensions used in categorizing them into financial behavioral profiles.

| This objective outlines the need to review and analyze available systems, emphasizing the relevance of benchmarking but keeping it optional. Ensure the scope of relevant systems is defined. vvv |
| ----- |

2. Explore existing personal finance management systems and applications of LSTM, Random Forest, Isolation Forest, and Linear Programming that are relevant to the development of a personal finance management system.

| This objective focuses on data preparation, which is crucial for subsequent modeling. It ensures that the data is in a suitable format for algorithm development. vvv |
| ----- |

3. Analyze, understand, and perform preprocessing activities on the data gathered towards the development of a personal finance management system.

| This objective sets clear guidelines for model training and evaluation, emphasizing the use of specific metrics to measure the model's effectiveness. vvv |
| ----- |

4. Train and evaluate the four models and algorithms of the system using the following evaluation metrics:  
   1. Random Forest (Profile Classification)  
      1. Accuracy  
      2. Precision  
      3. Recall  
      4. F1-Score  
   2. LSTM (Forecasting)  
      1. MAE (Mean Absolute Error)  
      2. SMAPE (Symmetric Mean Absolute Percentage Error)  
      3. MDA (Mean Directional Accuracy)  
      4. RMSE (Root Mean Square Error)  
   3. Linear Programming (Budget Recommendation)  
      1. Constraint Satisfaction Rate (adherence to hard constraints such as budget ceiling, minimum floors, profile rules)  
      2. Budget Utilization Rate (proportion of available funds allocated)  
      3. Deviation from User Preferences (deviation of the allocation from the user's category priorities and preferences)  
   4. Isolation Forest (Anomaly Detection)  
      1. Precision  
      2. Recall  
      3. F1-Score

| This objective outlines the specific features the web application should have, ensuring clarity in the development process. vvv |
| ----- |

5. Design and develop a mobile and web-based application with the following key features:

| Use modules (key features) until integration. vvv |
| ----- |

   1. Financial behavioral profile classification into one of the four profiles (Stable-Flexible, Stable-Obligated, Variable-Flexible, Variable-Obligated) during onboarding, with reclassification triggered by detected changes in income and spending behavior;  
   2. Dashboard with a quick display of spending forecasts, transaction entry, budget plan and health, and overage alerts;  
   3. Manual income and spending transaction entry with predefined expense categories, plus scheduled transactions for recurring automatic logging;  
   4. LSTM-driven personalized forecasting, showing the predicted total and per-category spending for the upcoming time horizon (daily, weekly, monthly), active once sufficient transaction history has accumulated;  
   5. Cold-start fallback forecasting, showing a profile-average baseline forecast derived from pre-trained model priors when the user's transaction history is insufficient for personalized forecasting, with a visible indicator that the forecast is not yet personalized;  
   6. Linear Programming-driven budget recommendation anchored to the user's profile, preferences, and transaction history;  
   7. Isolation Forest-based anomaly detection that identifies spending patterns deviating significantly from the user's established behavioral baseline;  
   8. Rule-based budget overspending detection that alerts the user whenever spending has exceeded a category allocation;  
   9. Goals management, defining savings & fund targets and monitoring cumulative progress based on transaction data, with long-term goal projection, and;  
   10. Debt management presenting both the Avalanche and Snowball repayment strategies.

| This objective highlights the importance of system testing based on established quality standards, ensuring robust evaluation. Note that testing and test cases may vary depending on the software development methodology chosen by the researchers and developers. vvv |
| ----- |

6. Test the functionality (based on test cases) and non-functionality of the system:  
   1. Functional requirements:  
      1. Financial behavioral profile module;  
      2. Dashboard module;  
      3. Transaction entry module;  
      4. Forecasting module;  
      5. Budget recommendation module;  
      6. Anomaly detection module;  
      7. Overspending detection module;  
      8. Goals management module, and;  
      9. Debt management module.  
   2. Non-functional requirements:  
      1. Response time standards (≤ 2–3 seconds)  
      2. Latency thresholds (≤ 500–800ms delay in normal conditions; ≤ 800–1000ms  delay under load)  
      3. Throughput standards;  
      4. Concurrent users stability under expected peak usage (15–100 concurrent users);  
      5. Load testing and stress testing;  
      6. Error rate standards (0-2%), and;  
      7. Test duration (5–15mins sustained load)

| This objective reinforces the commitment to rigorous evaluation based on internationally recognized standards. vvv |
| ----- |

7. Evaluate the application using a set of metrics based on the ISO/IEC 25010:2023 standards which focuses on:  
   1. Visual layout  
      1. User interface aesthetics  
      2. Accessibility  
      3. Appropriateness recognizability  
   2. Interface element design  
      1. Operability  
      2. User error protection  
      3. Accessibility  
      4. Appropriateness recognizability  
   3. Behavior  
      1. Functional suitability  
      2. Operability  
      3. Performance efficiency  
      4. User error protection

| This objective signifies the culmination of the research, where the system is made ready for real-world application. vvv |
| ----- |

8. Implement and deploy the personal finance management application to the mobile and web platform.

| The "Scope and Limitations" section of your research study is essential for defining the boundaries and constraints within which your work operates. It helps readers understand what your study encompasses and what aspects it does not address. Here's how you can write this section, focusing on the key elements you mentioned: vvv |
| ----- |

## **Scope and Limitations**

### **Scope**

| Utilization of the Algorithm \- The primary focus of this research is the utilization of the algorithm for the design and development of an application. The algorithm serves as the foundational technology driving the core functionalities of the application. vvv |
| ----- |

The core focus of this research revolves around the application of Random Forest, LSTM, Isolation Forest, and Linear Programming to design the modules of a personal finance management system.

| List of System Features: The study discusses system features that the application incorporates to address its intended objectives. While not detailed in this section, these features guide the application's functionality and user experience. vvv |
| ----- |

The study outlines a comprehensive list of system features, which form the functional framework of the application. These features include financial behavioral profile classification, dashboard, income and spending transaction entry and history, spending forecasting, intelligent budget recommendation, anomaly detection, savings goal tracking, and debt management. While not detailed in this section, they guide the overall functionality and user experience of the application.

| Geographical Scope: The geographical scope of this research extends to \[Specify the geographic region or regions relevant to your study\]. Data collection, testing, and user interaction are expected to occur within this defined geographical region. vvv |
| ----- |

The geographical scope of this research extends to the four districts of the National Capital Region, also known as Metro Manila. Data collection, testing, and user interaction are expected to occur within this defined geographical region.

| Temporal Scope: The study encompasses data collected and system development activities conducted during the period from \[Specify the start date\] to \[Specify the end date\]. vvv |
| ----- |

The study encompasses data collected and system development activities conducted during the period from the start of the 1st Semester, A.Y. 2026-2027 to the end of the 2nd Semester, A.Y. 2026-2027. It acknowledges that technological advancements beyond this temporal scope may not be considered in the study.

| Tools for System Design and Development: The study employs a range of tools and technologies for the design and development of the application. These tools include \[Specify the tools or software used for system design and development\]. vvv |
| ----- |

The study employs a range of tools and technologies for the design and development of the application. These tools include:

1. React Native, React, React Native for Web, and Expo SDK as the primary frontend development technologies that will be used to build the application on mobile and web;  
2. TypeScript as the language for writing the frontend and the main backend;  
3. Node.js and Express.js as the primary backend development technology that will be used to develop backend-processes;  
4. FastAPI as a secondary backend that will be used to develop the microservice for the machine learning;  
5. Python as the secondary language for writing processes that concern ML;  
6. TensorFlow and scikit-learn as the machine learning libraries that will be used for development, training, and inference;  
7. PostgreSQL and Supabase as the database and backend service deployment that will be used for authentication and data storage;  
8. Google Cloud Run, Docker, and Uvicorn as the DevOps and deployment technologies used for containerization, application serving, and cloud deployment of the backend and machine learning services;  
9. NativeWind, Tailwind CSS, and React Native Paper as the styling, iconography, and component libraries that will be used for designing and development of the application's interface;  
10. Git and GitHub as the version control and repository management technologies used for tracking source code changes and supporting collaborative development;  
11. Playwright, Jest, React Native Testing Library, Supertest, Pytest, and FastAPI Test Client, as primary testing technologies used for end-to-end, unit, component, and API testing across the frontend, backend, and machine learning service.

### **Delimitations**

The following are explicitly outside the scope of this study:

1. Bank, e-wallet, and investment API integrations are excluded due to third-party registration requirements; all transaction data is entered manually by the user.  
2. Multi-currency support is not included; the system operates exclusively in Philippine Peso (PHP).

### **Limitations**

Despite the study's objectives, there are certain limitations that should be acknowledged:

| Algorithm Dependency: This study heavily relies on the specified algorithm for its success. The effectiveness of the application is contingent on the performance and accuracy of this algorithm. Any limitations or constraints of the algorithm may consequently impact the application's performance. vvv |
| ----- |

This study is heavily reliant on the performance of its machine learning algorithms: Random Forest for profile classification, LSTM for spending forecasting, Isolation Forest for anomaly detection, and Linear Programming for budget recommendation. LSTM requires a sufficient volume of historical transaction data before spending forecasts become reliable and personalized; users in the early stages of system use will receive the cold-start fallback forecast based on a profile-average baseline until adequate transaction history accumulates. Isolation Forest, while effective as an unsupervised behavioral deviation detector, is known to produce false positives on imbalanced or sparse transaction data, particularly during the early stages of user onboarding when the behavioral baseline has not yet been established (Begum, 2025). Its detection accuracy is also sensitive to culturally specific spending spikes, such as those driven by fiestas, holidays, remittances, and paluwagan cycles, which may be flagged as anomalous despite being expected and intentional expenditures. Furthermore, Isolation Forest's performance is dependent on the quality and consistency of transaction data entered by the user; incomplete or irregular logging will degrade the reliability of the behavioral baseline from which deviations are measured. Any inherent limitations of these algorithms directly constrain the system's intelligence.

| Generalization: The findings and outcomes of this research are specific to the context, geographical area, and time frame defined in the scope. The generalizability of the application's performance to other regions or periods may be limited. vvv |
| ----- |

The findings and outcomes of this research are specific to the context, geographical area, and time frame defined in the scope, namely Filipino working young adults aged 20 to 40 residing or working in Metro Manila. The system's financial behavioral profiles based on income stability and obligation weight, locally derived expense categories, and advisory logic may not generalize without modification to other demographics such as high school students, senior citizens, and overseas Filipino workers, other regions of the Philippines, or other countries with different financial cultures, income structures, and obligation structures.

| External Factors: External factors such as network connectivity, hardware constraints, and user-specific behaviors are beyond the study's control and may influence the application's performance. vvv |
| ----- |

The performance and accessibility of Odin are subject to external conditions beyond the research team. These include network connectivity availability on users' devices, compatibility constraints across Android device models and browser environments, and broader economic or policy changes — such as adjustments to contribution rates for SSS, PhilHealth, and Pag-IBIG — that may affect the accuracy or relevance of the system's spending categories or advisory logic over time. The study does not account for such changes beyond the defined temporal scope.

| Note: Multiple operational definitions of terms is a section where terminologies will be introduced and discussed how it will be used. The terminologies will be in a narrative format where terminologies are italicized. Example is presented below: vvv |
| ----- |

## **Definition of Terms**

*Decision Trees* are supervised learning models that partition data into subsets through a series of binary splits based on feature values, producing a tree-like structure of decisions that terminates in classification or regression outputs. In this study, decision trees serve as the base learner underlying both the Random Forest classifier used for financial behavioral profile classification and the Isolation Forest algorithm used for anomaly detection.

*Random Forest* is an ensemble machine learning algorithm that constructs a large number of decision trees during training and aggregates their outputs, through majority voting for classification tasks, to produce a final prediction that is more robust and accurate than any individual tree. In this study, Random Forest is used to classify Filipino working young adults into one of four financial behavioral profiles based on their income and spending characteristics.

*Recurrent Neural Networks (RNN)* are a class of deep learning models designed to process sequential data by maintaining a hidden state that carries information across time steps, enabling them to model temporal dependencies in time-series data. In this study, RNNs serve as the base architecture underlying the LSTM model used for spending forecasting.

*Long Short-Term Memory (LSTM)* is a variant of RNNs equipped with gating mechanisms, input, forget, and output gates, that enable it to selectively retain or discard information across long sequences, making it effective at modeling financial time-series data where both recent and distant historical patterns are relevant. In this study, LSTM is used to generate personalized spending forecasts across daily, weekly, and monthly horizons based on each user's transaction history.

*Isolation Forest* is an unsupervised anomaly detection algorithm that isolates observations by randomly selecting a feature and a split value, constructing an ensemble of isolation trees in which anomalous data points, or data points that deviate significantly from established patterns, are isolated closer to the root and thus receive lower anomaly scores. In this study, Isolation Forest is used to detect spending patterns that deviate significantly from a user's established financial behavioral baseline, triggering anomaly alerts for review.

*Linear Programming (LP)* is a mathematical optimization technique that seeks to maximize or minimize a linear objective function subject to a set of linear equality and inequality constraints. In this study, Linear Programming is used to generate budget allocations that optimize fund distribution across spending categories while satisfying hard constraints defined by the user's financial behavioral profile, declared preferences, and available income.

*Cold-Start Fallback* refers to the strategy employed when a machine learning model lacks sufficient historical data from a specific user to generate reliable personalized outputs. In this study, the cold-start fallback activates during the early stages of user onboarding, providing a profile-average baseline spending forecast derived from pre-trained model priors until the user's transaction history is sufficient for personalized LSTM forecasting.

*Walk-Forward Validation* is a time-series model evaluation technique in which the model is trained on a fixed historical window and tested on the immediately following period, with the window advancing forward incrementally to simulate real-world sequential prediction conditions. In this study, walk-forward validation is used to evaluate the LSTM spending forecasting model to ensure that performance metrics reflect realistic deployment conditions rather than in-sample fitting.

*Concept Drift* refers to the phenomenon in which the statistical properties of the target variable that a machine learning model was trained to predict change over time, causing model performance to degrade as the learned patterns become less representative of current behavior (Xiang et al., 2023; Liao, 2026). In this study, concept drift is a recognized limitation of the LSTM and Isolation Forest models, as users' financial behaviors may shift due to life events such as employment changes, income fluctuations, and the onset or cessation of financial obligations.

*Alert Fatigue* refers to the desensitization of users to system-generated notifications or warnings that occurs when alerts are too frequent, insufficiently relevant, or poorly contextualized, leading users to dismiss or ignore them over time (Bhavana et al., 2025). In this study, alert fatigue is a design concern for the anomaly detection module, motivating the use of explainability mechanisms to ensure that anomaly alerts are accompanied by clear, user-facing justifications that maintain their relevance and credibility.

*Personal Finance Management (PFM)* refers to a category of software systems designed to help individuals track income and expenses, manage budgets, monitor progress toward financial goals, and receive personalized financial guidance (Badiger et al., 2026). In this study, Odin is developed as a PFM tailored to the financial behavioral profiles, spending patterns, and cultural financial obligations of Filipino working young adults in Metro Manila.

Expense Forecast is a system feature that uses the LSTM model to predict a user's future spending across daily, weekly, and monthly horizons based on their historical transaction data, providing visibility into anticipated expenditure per category before it occurs. In this study, the expense forecast is a primary intelligent feature of Odin, with a cold-start fallback activated when transaction history is insufficient for personalized prediction.

*Recurring Transaction* refers to a financial transaction that repeats at regular intervals, such as rent payments, subscription fees, statutory contributions, and loan amortizations. In this study, recurring transactions are logged automatically by the system based on user-defined schedules, ensuring that predictable obligations are consistently captured in the transaction history used for forecasting, budget recommendation, and anomaly detection.

*Anomaly Detection* is the process of identifying data points, patterns, or observations that deviate significantly from expected behavior within a dataset. In this study, anomaly detection is implemented through Isolation Forest to identify spending deviations from each user's established financial behavioral baseline, supplemented by rule-based budget overage detection that alerts the user when spending has exceeded a category allocation.

*Financial Behavioral Profile* is a classification of a user's financial characteristics based on the stability of their income and the weight of their obligated expenses, used to personalize budget recommendations, forecasting baselines, and anomaly detection thresholds. Financial behavior encompasses how individuals make financial decisions and how those decisions affect their financial well-being. In this study, Odin classifies users into one of four profiles, Stable-Flexible, Stable-Obligated, Variable-Flexible, and Variable-Obligated, during onboarding, with reclassification triggered by detected changes in income and spending behavior over time.

*Income Stability* refers to the degree of consistency and predictability of an individual's income across pay periods, distinguishing between stable income sources such as fixed monthly salaries and variable income sources such as freelance earnings, commission-based pay, and platform work (Jandoc et al., 2026). In this study, income stability is one of the two primary dimensions used to classify users into financial behavioral profiles, with specific thresholds to be determined through the literature review and adviser consultation.

*Obligation Level* refers to the proportion of an individual's income that is committed to non-discretionary, culturally obligated, or contractually required expenses, including family remittances, paluwagan contributions, statutory government contributions, and loan amortizations, leaving a defined remainder available for discretionary spending and savings (Donato et al., 2023; Bongalonta et al., 2024). In this study, obligation level is the second primary dimension used to classify users into financial behavioral profiles, with specific thresholds to be determined through the literature review and adviser consultation.

*Financial Literacy* refers to an individual's knowledge and understanding of financial concepts, products, and practices sufficient to make informed financial decisions (Cacnio & Romarate, 2024). In this study, financial literacy serves as a contextual factor informing the design of Odin's user interface and advisory logic; research consistently shows that among Filipino working young adults, financial literacy alone does not predict financial behavior, motivating Odin's emphasis on behavioral infrastructure over educational content (Dimaunahan et al., 2025; Lim & Cordova, 2024).

*Financial Behavior* refers to the actions individuals take in managing their financial resources, including spending, saving, borrowing, and investing, and is shaped by a combination of structural, psychological, and cultural factors rather than financial knowledge alone. In this study, financial behavior is the primary lens through which Odin interprets user transaction data, informing profile classification, anomaly detection thresholds, and budget recommendation logic.

*Financial Obligation* refers to a recurring or non-discretionary commitment of financial resources that an individual is expected or required to fulfill, encompassing statutory contributions, loan repayments, family support arrangements, and community financial commitments (Donato et al., 2023). In this study, financial obligations are treated as protected spending categories within Odin's budget recommendation and anomaly detection logic, reflecting the non-negotiable nature of these expenditures in the Filipino financial context.

*Informal Financial Mechanisms* refer to financial services and arrangements that operate outside formal regulatory oversight, including peer-to-peer lending, group savings schemes, and informal money lending (Bongalonta et al., 2024). In this study, informal financial mechanisms — particularly paluwagan and informal loan arrangements — are recognized as structurally embedded features of Filipino working young adult financial behavior that Odin's transaction categorization and budget recommendation logic must accommodate.

*Paluwagan* is a Philippine informal rotating savings arrangement in which a group of participants each contribute a fixed amount at regular intervals, with the pooled sum distributed to one member per cycle on a rotating basis, relying entirely on mutual trust among participants in the absence of formal regulation (Bongalonta et al., 2024). In this study, paluwagan contributions and payouts are treated as a distinct transaction category within Odin's spending classification structure, recognizing their cyclical cash flow impact on the user's budget.

*Avalanche Strategy* is a debt repayment method that prioritizes obligations with the highest interest rates first, minimizing the total interest paid over the repayment period at the cost of a longer time before the first debt is fully cleared. In this study, the Avalanche Strategy is one of two debt management options presented to users within Odin's debt management module.

*Snowball Strategy* is a debt repayment method that prioritizes obligations with the smallest outstanding balances first, generating early repayment milestones that build motivation and momentum for tackling larger debts, at the cost of potentially higher total interest paid. In this study, the Snowball Strategy is one of two debt management options presented to users within Odin's debt management module.