## Metadata

```json
{
   "document-type": "chapter",
   "chapter": 1,
   "title": "Introduction",
   "version": 0.1.0,
   "date": "2026.08.05",
   "authors": [
      "Gabion, Stefanie S.",
      "Guevarra, Joaquin Luis T.",
      "San Jose, Alexa Joanne Paula G.",
      "Togle, Charles Nathaniel B."
   ]
}
```

---

**UNIVERSITY OF MAKATI**

**DEVELOPMENT OF ODIN: A PERSONAL FINANCE MANAGEMENT**   
**APPLICATION FOR FILIPINO WORKING YOUNG ADULTS USING**  
**RANDOM FOREST, LSTM, AND ISOLATION FOREST**

A thesis submitted to the faculty of College of Computing  
and Information Sciences in candidacy for the Degree of  
Bachelor of Science in Computer Science  
(Application Development Elective Track)

DEPARTMENT OF COMPUTER SCIENCE

BY

**STEFANIE S. GABION**  
**JOAQUIN LUIS T. GUEVARRA**  
**ALEXA JOANNE PAULA G. SAN JOSE**  
**CHARLES NATHANIEL B. TOGLE**

In Partial Fulfillment  
of the Requirements for the Degree  
BACHELOR OF SCIENCE IN COMPUTER SCIENCE

**\[Month and Year of Approval\]**  
The THESIS entitled:

**DEVELOPMENT OF ODIN: A PERSONAL FINANCE MANAGEMENT**   
**APPLICATION FOR FILIPINO WORKING YOUNG ADULTS USING**  
**RANDOM FOREST, LSTM, AND ISOLATION FOREST**

submitted by Stefanie S. Gabion, Joaquin Luis T. Guevarra, Alexa Joanne Paula G. San Jose, and  Charles Nathaniel B. Togle has been examined and is recommended for Oral Defense.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
**Prof. CHRISTIAN MICHAEL MANSUETO**  
Technical Advisor  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
**Prof. ERA MARIE F. GANNABAN**  
Course Advisor

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
**Prof. DANIEL P. DELLOSA**  
Department Chair

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
**Dr. JOEL B. MANGABA, DT**  
Dean  
College of Computing and Information Sciences  
The Faculty of the Department of Computer Science, College of Computing and Information Sciences, University of Makati, ACCEPTS THE THESIS entitled:

**DEVELOPMENT OF ODIN: A PERSONAL FINANCE MANAGEMENT**   
**APPLICATION FOR FILIPINO WORKING YOUNG ADULTS USING**  
**RANDOM FOREST, LSTM, AND ISOLATION FOREST**

submitted by Stefanie S. Gabion, Joaquin Luis T. Guevarra, Alexa Joanne Paula G. San Jose, and  Charles Nathaniel B. Togle, in partial fulfillment of the requirements for the degree of Bachelor of Science in Computer Science (Application Development Track).

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
**Prof. JOMARISS B. PLAN**  
Panel Member  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
**Prof. JANICE CONGZON**  
Panel Member

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
**\[PANEL CHAIR\]**  
Panel Chair

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
**Prof. DANIEL P. DELLOSA**  
Department Chair

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
**Dr. JOEL B. MANGABA, DT**  
Dean  
College of Computing and Information Sciences

**TABLE OF CONTENTS**  
Page

| ABSTRACT | ……………………………… |  | \[\#\] |
| :---- | :---- | :---: | :---: |
| ACKNOWLEDGEMENTS | ……………………………… |  | \[\#\] |
| LIST OF FIGURES | ……………………………… |  | \[\#\] |
| LIST OF TABLES | ……………………………… |  | \[\#\] |
| LIST OF ABBREVIATIONS | ………………………………. |  | \[\#\] |
| **CHAPTER I: INTRODUCTION** |  |  |  |
| Project Context | ……………………………… |  | \[\#\] |
| Purpose and Description of the Study | ……………………………… |  | \[\#\] |
| Objectives of the Study | ……………………………… |  | \[\#\] |
| Scope and Limitations | ……………………………… |  | \[\#\] |
| Definition of Terms | ……………………………… |  | \[\#\] |
| **CHAPTER II: REVIEW OF RELATED LITERATURE AND STUDIES** |  |  |  |
| Review of Related Literature and Studies | ……………………………… |  | \[\#\] |
| Synthesis | ……………………………… |  | \[\#\] |
| Conceptual Model of the Study | ……………………………… |  | \[\#\] |
| **CHAPTER III: DESIGN AND METHODOLOGY** |  |  |  |
| Research Design | ……………………………… |  | \[\#\] |
| Research Methodology | ……………………………… |  | \[\#\] |
| **CHAPTER IV: RESULTS AND DISCUSSION** |  |  |  |
| Model Evaluation Result | ……………………………… |  | \[\#\] |
| Application Output | ……………………………… |  | \[\#\] |
| Project Evaluation | ……………………………… |  | \[\#\] |
| Testing Results | ……………………………… |  | \[\#\] |
| Application Evaluation | ……………………………… |  | \[\#\] |
| **CHAPTER V: SUMMARY OF FINDINGS, CONCLUSIONS, AND RECOMMENDATIONS** |  |  |  |
| Summary of Findings | ……………………………… |  | \[\#\] |
| Conclusion | ……………………………… |  | \[\#\] |
| Recommendations | ……………………………… |  | \[\#\] |
| **APPENDICES** |  |  |  |
| Algorithm Source Code | ……………………………… |  | \[\#\] |
| Test Plan | ……………………………… |  | \[\#\] |
| Evaluation Tool | ……………………………… |  | \[\#\] |
| Sample Inputs/Outputs and Reports | ……………………………… |  | \[\#\] |
| Certifications and CUR Requirements | ……………………………… |  | \[\#\] |
| User’s Manual | ……………………………… |  | \[\#\] |
| Curriculum Vitae | ……………………………… |  | \[\#\] |
| **REFERENCES** | ……………………………… |  | \[\#\] |

# 

# **ABSTRACT**

Drafting an effective abstract is vital for encapsulating the essence of your research paper concisely and informatively. With a length typically limited to 150-250 words, it should provide a structured overview of your study, including the background, objective, methods, results, and conclusions. Use clear, specific language devoid of jargon to ensure comprehensibility. Emphasize key findings and contributions while incorporating relevant keywords for discoverability. Avoid repetition with the main paper, proofread meticulously, and tailor your abstract to the intended audience. Seek feedback, follow any specific guidelines, and remember that your abstract is often one of the last sections to be written, refined to reflect the final results and conclusions accurately.

# 

# **ACKNOWLEDGEMENTS**

When drafting the acknowledgments for your work, begin by expressing your gratitude towards individuals and institutions who contributed directly or indirectly to your research or project. Start with formal acknowledgments, such as funding agencies, institutions, mentors, and advisors, followed by specific mentions of colleagues, collaborators, or friends who provided support, feedback, or resources. Keep the tone sincere and concise, and be sure to acknowledge anyone who had a meaningful impact on your work while respecting their privacy and preferences. Always use 3rd person.

LIST OF FIGURES  
								Page 

| Figure 1: \[Title\] | …………………………… | \[\#\] |
| :---- | :---- | :---- |

 LIST OF TABLES  
								Page 

| Table 1: \[Title\] | …………………………… | \[\#\] |
| :---- | :---- | :---- |

LIST OF ABBREVIATIONS

| PFM | Personal Finance Management |
| :---: | :---- |

# **CHAPTER I**  **INTRODUCTION**

Personal finance management has evolved in the modern era, from manual tracking and ledger-keeping to sophisticated digital financial management. The popularity of digital transactional services such as online banking, e-wallets, and digital loans has introduced a level of complexity to personal finance that is difficult to manage using traditional and manual methods. This has created an opportunity for intelligent digital tools designed to assist users in the management of their finances. The opportunity has led to the creation of expense trackers, budgeting applications, and wealth managers. However, it is slowly moving towards more intelligent systems that go beyond tracking past and present finances and into leveraging financial data to adapt according to user behavior and provide smart financial insights and guidance.

While the global landscape has seen strides in innovative and intelligent personal finance management, the Philippine landscape has yet to catch up. The Filipino population is characterized by a variety in demographics, culture, socioeconomic status, digital presence, and personal financial circumstances. A good percentage of Filipinos live and work in urban and highly modern cities. Despite that, a large number of those Filipinos are in the low- to medium-income bracket. Filipinos vary in cultural practices and habits, such as supporting their primary families and using informal financial practices. Most Filipinos are technologically adept, owning mobile devices and being able to proficiently navigate and utilize the internet and digital spaces. A large number of Filipinos are reported to have poor financial circumstances. On average, their financial knowledge and literacy were found to be below the baseline. Their financial behavior is deeply affected by their circumstances and background. The local market is saturated with numerous personal finance solutions such as bank-integrated apps, budgeting apps, expense trackers, and investment trackers. However, many of these are limited by a lack of local and personal contextualization and a lack of intelligent insights that cater to the specific and varying financial habits and goals of the Filipino user.

In response to these identified gaps and limitations, the design and development of Odin is conceptualized. Odin is designed to be an intelligent PFM system specifically tailored to each Filipino working young adult's financial background, circumstances, and behavior. It aims to improve upon the current state of local PFM systems by offering an intelligent, holistic, localized, and behaviorally tailored approach to Filipino personal finance. Furthermore, Odin aligns itself with and contributes to the United Nations' Sustainable Development Goals, namely SDG 1 (No Poverty) and SDG 8 (Decent Work and Economic Growth). By intelligently fostering holistic financial well-being and planning, Odin can assist individuals in building financial resilience, sustainability, and potential, ultimately contributing to a more stable and prosperous economy.

## **Project Context**

Personal financial management, originating from the fundamental need to track income and expenses, has evolved into a sophisticated discipline in the modern digital era. Accurate and intelligent financial management, particularly for budgeting, expense tracking, and financial planning, is crucial for various applications, including personal financial literacy, economic stability, and even national economic development. The growing complexity of financial products, the prevalence of digital transactions, and the increasing need for individuals to take control of their financial well-being have created an opportune intersection for research in this domain.

Within the broader domain of financial technology and personal finance, the specific focus of this study revolves around the development of an intelligent PFM system tailored to the unique context of Filipino working young adults. A PFM system is considered "intelligent" when it incorporates data analytics, machine learning, and automation to provide users with predictive insights, automated categorization, and personalized financial recommendations. Previous research in PFM systems has primarily concentrated on general financial behaviors and Western financial contexts. Foundational work in financial technology has established the technical architecture for these systems, while academic literature has explored user behavior, identifying key features such as spending visualization, goal-setting, and real-time notifications as primary drivers of user engagement and financial literacy. However, the nuances of Filipino financial behaviors, characterized by informal savings practices, family-oriented spending, and a diverse financial ecosystem, necessitate a specialized approach. This niche research area addresses the need for a more accurate, context-specific PFM system that can enhance financial literacy and promote better financial habits among Filipino working young adults.

The core problem that this research endeavors to tackle is the lack of an accessible, localized, and intelligent PFM system that is behaviorally tailored to Filipino working young adults, capable of accounting for their varying financial backgrounds and circumstances, as well as their varying financial problems and behaviors, rather than treating them as a single, uniform user base. This system aims to precisely capture, analyze, and provide insights into the financial behaviors of Filipino individuals. By doing so, we aim to contribute to the broader field of financial technology by providing a tool that can improve financial literacy, analyze the effectiveness of different savings and spending strategies, and assist in real-time financial decision-making for practitioners.

Existing research in financial technology and personal finance management showcases a lack of tailored solutions for Filipino users. Studies in other developing economies have highlighted the challenges posed by diverse financial ecosystems and the need for localized PFM solutions. Statistics from the World Bank and the Bangko Sentral ng Pilipinas consistently highlight that a significant portion of the Filipino adult population remains unbanked or underbanked, with many individuals lacking the basic financial literacy skills to budget effectively or plan for the future. Furthermore, interviews and surveys with financial literacy advocates and Filipino users have indicated a strong desire for a dedicated PFM system to enhance financial management methodologies and performance assessment.

The complexity of Filipino financial behaviors, characterized by informal financial practices, a diverse range of financial platforms, and varying financial backgrounds, circumstances, problems, and behaviors, presents challenges in traditional PFM systems. The lack of specialized, behaviorally tailored models for the Filipino context hinders progress in financial literacy and economic stability. Consequently, individuals may struggle to manage their finances effectively, and financial educators may face limitations in providing tailored guidance. On a broader scale, this problem contributes to low savings rates, high household debt, and a lack of investment in productive assets, hindering national economic growth. For the individual user, it manifests as stress from financial insecurity, a lack of progress towards personal goals, and a vulnerability to predatory lending or harmful financial decisions. Addressing this problem has the potential to significantly impact the effectiveness and accessibility of financial management, making it more engaging and accessible to a broader audience.

## **Purpose and Description of the Study**

In response to the lack of an intelligent PFM system that is behaviorally tailored to Filipino working young adults with varying financial backgrounds, circumstances, problems, and behaviors, this research proposes the design, development, and implementation of Odin, a novel intelligent Personal Finance Management (PFM) system. This system will employ state-of-the-art financial technology techniques, data analytics, and machine learning algorithms to precisely track, interpret, and provide insights into the financial activities exhibited in the Filipino context. The core strategy of this solution involves the collection of a diverse dataset of Filipino financial behaviors, the design of a tailored financial analysis algorithm, and the integration of user-friendly interfaces and real-time feedback mechanisms. Key system features include automated transaction categorization, spending visualization, financial goal tracking, and predictive analytics to enhance financial management and literacy.

The primary purpose of this study is to design, develop, and validate a specialized intelligent PFM system, named Odin, tailored explicitly to the distinctive financial behaviors, challenges, and needs of Filipino working young adults in the National Capital Region (NCR). This purpose aligns with the need to address the limitations in existing PFM technologies when applied to the unique financial ecosystem of the Philippines. By achieving this purpose, we aim to provide Filipino individuals, financial educators, and policymakers with a valuable tool for enhancing financial literacy, refining financial strategies, and objectively assessing financial well-being.

This study holds significant implications both within the realm of financial technology and the broader field of data science and user experience design. The proposed Odin PFM system has the potential to revolutionize personal financial management in the Philippines by offering real-time, precise, and context-specific financial insights to users. Moreover, it contributes to the field of FinTech by addressing the challenges posed by diverse and dynamic financial behaviors in developing economies. The development of this system may also extend to other domains with similar financial analysis requirements, such as microfinance, financial inclusion initiatives, and economic policy planning. Ultimately, this research seeks to bridge the gap between traditional financial practices and cutting-edge technology, enhancing the practice and understanding of personal finance in the Philippines while advancing the field of intelligent PFM systems.

## **Objectives**

The general objective of the study is to design, develop, and implement an intelligent Personal Finance Management (PFM) system, named Odin, which leverages data analytics to provide behaviorally tailored, automated financial insights, which may assist users in making informed financial decisions and improve their overall financial well-being.

## **Specific Objectives**

	In order to fulfill the main objective of this project, the authors constructed the following specific objectives:

1. Examine and understand the fundamental financial management behaviors, challenges, and needs of the target demographic.  
2. Explore existing systems and applications of intelligent PFM systems, analyzing their features, architectures, and limitations to inform the design of Odin.  
3. Analyze, understand, and perform preprocessing activities on financial data sources to ensure data is suitable for ingestion and analysis by the PFM system.  
4. Train and evaluate Odin's four models, the Personal Financial Profile (PFP) Classification, Budget Optimization, Financial Forecasting, and Anomalous Transaction Detection models, using the following evaluation metrics:  
   1. Personal Financial Profile Classification  
      1. Accuracy  
      2. Precision  
      3. Recall  
      4. F1-Score  
   2. Budget Optimization  
      1. Constraint Satisfaction Rate (adherence to hard constraints such as budget ceiling, minimum floors, profile rules)  
      2. Budget Utilization Rate (proportion of available funds allocated)  
      3. Deviation from User Preferences (deviation of the allocation from the user's category priorities and preferences)  
   3. Financial Forecasting  
      1. Mean Absolute Error (MAE)  
      2. Symmetric Mean Absolute Percentage Error (SMAPE)  
      3. Mean Directional Accuracy (MDA)  
      4. Root Mean Square Error (RMSE)  
   4. Anomalous Transaction Detection  
      1. Accuracy  
      2. Precision  
      3. Recall  
      4. F1-Score  
5. Design and develop the Odin mobile-based application with the following key features:  
   1. Personal Financial Profile (PFP) classification via questionnaire, or triggered by detected changes in financial behavior;  
   2. Dashboard providing a quick display of expense forecasts, transaction entries, budget plan and health, and anomalous transaction alerts;  
   3. Transaction entry with predefined income and expense categories, plus scheduled transactions for recurring automatic logging;  
   4. Personalized financial forecasting, showing the predicted total and per-category spending for the upcoming time horizon (weekly, semi-monthly, or monthly), active once sufficient transaction history has accumulated;  
   5. Cold-start fallback forecasting, showing a profile-average baseline forecast derived from pre-trained model priors when the user's transaction history is insufficient for personalized forecasting, with a visible indicator that the forecast is not yet personalized;  
   6. Budget optimization and recommendation anchored to the user's profile, preferences, and transaction history;  
   7. Anomalous transaction detection that identifies spending patterns deviating significantly from the user's established behavioral baseline;  
   8. Rule-based budget overspending detection that alerts the user whenever spending has exceeded a category allocation;  
   9. Savings goals management, defining savings and fund targets and monitoring cumulative progress based on transaction data, with long-term goal projection; and  
   10. Debt management presenting debt repayment strategies.  
6. Test the functionality and non-functionality of the system based on the following test cases:  
   1. Functional requirements:  
      1. Login module  
      2. Registration module  
      3. Questionnaire module  
      4. User account module  
      5. Financial profile module  
      6. Financial account module  
      7. Dashboard module  
      8. Transaction entry module  
      9. Transaction template module  
      10. Transaction history module  
      11. Budget planning module  
      12. Budget tracking and health module  
      13. Budget report and analysis module  
      14. Financial forecasting module  
      15. Anomaly detection module  
      16. Reports and statistics module  
   2. Non-Functional requirements:  
      1. Response time standards (≤ 2–3 seconds)  
      2. Latency thresholds (≤ 500–800ms delay in normal conditions; ≤ 800–1000ms  delay under load)  
      3. Throughput standards;  
      4. Concurrent users stability under expected peak usage (15–100 concurrent users);  
      5. Load testing and stress testing;  
      6. Error rate standards (0-2%), and;  
      7. Test duration (5–15mins sustained load)  
7. Evaluate the system using a set of metrics based on the ISO 25010 standards, which focuses on:  
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
8. Implement and deploy the personal finance management application to the mobile platform.

## **Scope and Limitations**

The primary focus of this research is the utilization of machine learning algorithms for the design and development of the Odin application, spanning four models: Personal Financial Profile Classification, Budget Optimization, Financial Forecasting, and Anomalous Transaction Detection. Consistent with the study's experimental algorithm methodology, the specific algorithm best suited to each model is not predetermined; candidate algorithms are evaluated during the data modeling phase, and the best-performing candidate per model is selected based on the study's evaluation metrics. These models serve as the foundational technology driving the core financial analysis and insight generation functionalities of the application.

The study discusses system features that the application incorporates to address its intended objectives. While not detailed in this section, these features guide the application's functionality and user experience and will be elaborated upon in later chapters.

The geographical scope of this research extends to the National Capital Region (NCR), Philippines. Data collection, testing, and user interaction are expected to occur within this defined geographical region, focusing on the financial context and user base of Filipino working young adults in NCR.

The study encompasses data collection and system development activities conducted during the period from the start of the 1st Semester, A.Y. 2026-2027 to the end of the 2nd Semester, A.Y. 2026-2027. It acknowledges that technological advancements beyond this temporal scope may not be considered in the study.

The study employs a range of tools and technologies for the design and development of the application. These tools include:

1. React Native and Expo SDK as the primary frontend development technologies that will be used to build the application on mobile;  
2. TypeScript as the language for writing the frontend and the main backend;  
3. Node.js and Express.js as the primary backend development technology that will be used to develop backend-processes;  
4. FastAPI as a secondary backend that will be used to develop the microservice for the machine learning;  
5. Python as the secondary language for writing processes that concern ML;  
6. TensorFlow and scikit-learn as the machine learning libraries that will be used for development, training, and inference;  
7. PostgreSQL and Supabase as the database and backend service deployment that will be used for authentication and data storage;  
8. Google Cloud Run, Docker, and Uvicorn as the DevOps and deployment technologies used for containerization, application serving, and cloud deployment of the backend and machine learning services;  
9. NativeWind, Tailwind CSS, and React Native Paper as the styling, iconography, and component libraries that will be used for designing and development of the application's interface;  
10. Git and GitHub as the version control and repository management technologies used for tracking source code changes and supporting collaborative development;  
11. Jest, React Native Testing Library, Supertest, Pytest, and FastAPI Test Client, as primary testing technologies used for end-to-end, unit, component, and API testing across the frontend, backend, and machine learning service.

**Delimitations**  
The following are explicitly outside the scope of this study:  
Bank, e-wallet, and investment API integrations are excluded due to third-party registration requirements; all transaction data is entered manually by the user.  
Multi-currency support is not included; the system operates exclusively in Philippine Peso (PHP).

## **Limitations**

	Despite the study's objectives, there are certain limitations that should be acknowledged:

This study heavily relies on the machine learning algorithms selected through its experimental modeling process for its success. The effectiveness of the application is contingent on the performance and accuracy of whichever algorithm is ultimately selected per model in processing and analyzing financial data. Any limitations or constraints of these algorithms may consequently impact the application's performance and the reliability of its insights.

The findings and outcomes of this research are specific to the context, geographical area, and time frame defined in the scope. The generalizability of the application's performance and its findings to other regions or periods may be limited.

External factors such as network connectivity, hardware constraints, and user-specific behaviors are beyond the study's control and may influence the application's performance and user experience.

## **Definition of Terms**

Personal Financial Management (PFM) refers to a system or application that helps individuals and families manage their personal finances, including budgeting, tracking expenses, planning, and setting financial goals. PFM systems aggregate financial data from various sources to provide a consolidated view of an individual's financial health.

Intelligent PFM is a PFM system or application that incorporates advanced technologies, such as machine learning and data analytics, to provide automated, personalized, and behaviorally tailored insights. This includes automatic transaction categorization, prediction of future cash flow, and the identification of unusual spending patterns.

Personal Financial Profile (PFP) refers to the classification assigned to a user based on their financial standing, capturing dimensions of their financial behavior relevant to how Odin tailors its insights and recommendations to that user.

Machine Learning (ML) is a subset of artificial intelligence that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. In the context of PFM, ML algorithms are used for tasks like categorizing transactions, detecting anomalies, and predicting spending behavior.

Financial Behavior refers to the actions individuals take in managing their financial resources, including spending, saving, borrowing, and investing, and is shaped by a combination of structural, psychological, and cultural factors rather than financial knowledge alone. In this study, financial behavior is the primary lens through which Odin interprets user transaction data, informing profile classification, anomaly detection thresholds, and budget recommendation logic.