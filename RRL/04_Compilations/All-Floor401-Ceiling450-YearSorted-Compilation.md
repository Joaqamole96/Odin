# Compiled Research Summaries

**Total Papers:** 50

**Note:** Included papers positions 401 to 450, Sorted by year.

---

## Paper 1: Meka_summarized.md

**Source File:** `Meka_summarized.md`

```yaml
paper_id: 10.15662/IJRAI.2023.0602003
designation: international
title: Building Digital Banking Foundations: Delivering End-to-End FinTech Solutions with Enterprise-Grade Reliability
authors: Meka, S.
year: 2023
venue: International Journal of Research and Applied Innovations
odin_topics:
  - 4.A
  - 4.B
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
tldr: An enterprise-scale digital banking backbone for community banks was developed using a full-stack FinTech ecosystem, significantly improving production stability and engineering velocity.
problem_and_motivation: Community banks face the challenge of delivering modern, cloud-native digital banking functionality with limited budgets and aging infrastructure while maintaining high reliability and security. A sustainable enterprise-level digital banking core is needed to serve as a strategic enabler for the future of financial services. This project aimed to provide end-to-end solutions that balance innovation with operational stability.
approach:
  - The project used a Scrum-based Agile methodology with 2-week sprints, JIRA for tracking, and CI/CD automation via Jenkins.
  - The architecture was built on RESTful microservices (Java, Spring), a dynamic Angular frontend, and a SQL Server database.
  - Cloud-native deployment was performed on AWS with Docker containers, supported by centralized logging and automated rollback procedures.
  - A multi-layered testing strategy was implemented, including unit, integration, UI, regression, performance, and user acceptance testing.
  - Proofs-of-concept were conducted for new technologies like Flowable workflow engine and different caching strategies to de-risk development decisions.
findings:
  - num: Monthly production incidents decreased by 39.6% to 29.
  - num: Mean Time to Resolve (MTTR) was reduced by 47.2% to 9.5 hours.
  - num: High-severity defects per quarter decreased by 47.6% to 11.
  - num: System uptime availability increased from 98.1% to 99.4%.
  - num: Average sprint velocity improved by 76% to 150 story points, with a story completion rate of 91%.
  - The implementation of new digital capabilities was successfully delivered alongside the stabilization of existing systems.
  - Improved logging, root cause analysis, and team coordination contributed to faster problem resolution.
  - A focus on code quality and technical governance resulted in better maintainability and reduced defect leakage.
key_figures_tables:
  - "Table 1: Production Stability Metrics Before and After Implementation → Shows significant improvements in incident rate, MTTR, high-severity defects, and uptime."
  - "Table 2: Agile Velocity and Delivery Metrics → Demonstrates consistent increases in sprint velocity and story completion rates across three quarters."
  - "Figure 1: Result Comparison- Monthly Production Incidents → Visualizes the 39.6% reduction in incidents."
  - "Figure 2: Result Comparison- Mean Time to Resolution (MTTR) → Visualizes the 47.2% reduction in resolution time."
  - "Figure 3: Result Comparison- Uptime Availability → Visualizes the increase to 99.4% availability."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: FinTech
    definition: Financial technology, used to describe new tech that seeks to improve and automate the delivery and use of financial services.
  - term: SDLC
    definition: Software Development Life Cycle, a process for planning, creating, testing, and deploying software.
  - term: CI/CD
    definition: Continuous Integration and Continuous Deployment, a method to frequently deliver apps to customers by introducing automation into the stages of app development.
  - term: MTTR
    definition: Mean Time to Resolve, the average time taken to resolve a system failure or incident.
  - term: MTBF
    definition: Mean Time Between Failures, the average time between system failures.
  - term: RTO
    definition: Recovery Time Objective, the maximum acceptable time to restore a system after a failure.
  - term: POC
    definition: Proof-of-Concept, a realization of a certain method or idea to demonstrate its feasibility.
  - term: REST
    definition: Representational State Transfer, an architectural style for designing networked applications.
  - term: RegTech
    definition: Regulatory Technology, a term for solutions that help businesses comply with regulations efficiently.
critical_citations:
  - "[Anifa et al., 2022] — Foundational for FinTech's impact on the financial service industry."
  - "[Kulkarni, 2021] — Provides rationale for microservices in high-performance banking."
  - "[Olden, 2025] — Supports the use of multi-cloud strategies for resilience in financial services."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides context on how community banks are modernizing legacy systems with enterprise FinTech solutions.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly addresses the limitations of aging infrastructure and the need for a new, reliable digital banking core.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Discusses responsive web portals and customer-facing applications, which aligns with mobile-first design principles.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Mentions creating interactive, responsive user interfaces and onboarding experiences for digital banking.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Highlights the use of Spring Security, encryption, and audit trails to ensure data privacy and security.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Implies that high uptime and reliable service are crucial for maintaining customer trust in FinTech platforms.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Uses a framework of metrics (MTTR, incidents, velocity, defects) to evaluate the impact of their engineering process.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: low
      justification: Briefly mentions potential future integration of AI/ML for fraud detection, but does not evaluate such modules now.
  contribution: The paper's case study on building a reliable digital banking backbone directly informs Odin's design by demonstrating enterprise-grade practices in system architecture, CI/CD, and operational monitoring. The quantitative metrics for production stability and engineering velocity provide a benchmark for evaluating Odin's performance and reliability. The structured approach to full-stack development and technical governance offers a template for Odin's own development lifecycle. Furthermore, the paper's discussion of future AI/ML integrations justifies Odin's potential for incorporating predictive features.
  directly_justifies:
    - "A full-stack approach integrating Java/Spring, Angular, and AWS enables scalable and secure financial applications."
    - "CI/CD automation and a multi-layered testing strategy are critical for maintaining production stability."
    - "Systematic incident management and root cause analysis are essential for achieving high uptime and user trust."
    - "Engineering velocity and code quality are key indicators of a successful and sustainable development process."
  limits:
    - "The system is designed for community banks in a Western context; applicability to Filipino young professionals may differ."
    - "The paper focuses on the engineering process rather than user-facing behavioral or financial profiling aspects."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The domain "Existing Systems & Gaps" was flagged as highly relevant (4.A, 4.B) because the paper directly addresses the need to modernize legacy infrastructure. "Mobile-First Design" (9.A, 9.B) and "Data Privacy & User Trust" (10.A, 10.B) were judged medium relevance, as the paper describes creating responsive digital interfaces and emphasizes security, but these are not the paper's primary focus. "System Evaluation" (12.A, 12.B) was flagged as high and low respectively: 12.A is central to the paper's reporting of quantitative outcomes, while 12.B is only mentioned as a future direction. Domains like "Filipino Cultural Context," "Behavioral Profiling," and "Spending Forecasting" were considered and rejected, as the paper offers no insights into user behavior, cultural financial practices, or predictive modeling for spending. Overall, the paper provides strong, citable evidence for building reliable, secure financial software platforms, which is directly relevant to Odin's foundational infrastructure and evaluation metrics.
limitations:
  - "The study is a single case study, which may limit the generalizability of its findings to all community banks."
  - "The paper does not provide a detailed analysis of cost implications of the implemented cloud-native architecture."
  - "Long-term user satisfaction or adoption metrics are not evaluated, which is critical for user retention."
remember_this:
  - "Implementing a robust SDLC and CI/CD pipeline reduced production incidents by 39.6%."
  - "MTTR was nearly halved from 18 hours to 9.5 hours through improved monitoring and triage."
  - "System uptime availability exceeded 99.4%, ensuring high reliability for banking operations."
  - "Sprint velocity doubled to 150 story points, indicating a significant increase in engineering productivity."
  - "A disciplined Agile approach and architectural governance are essential for FinTech quality."
```
---

## Paper 2: Kowsar M. et al-2023_summarized.md

**Source File:** `Kowsar M. et al-2023_summarized.md`

```yaml
paper_id: 10.63125/1hh4q770
designation: international
title: Credit Decision Automation in Commercial Banks: A Review of AI and Predictive Analytics in Loan Assessment
authors: Kowsar, M. M.; Mohiuddin, M.; Mohna, H. A.
year: 2023
venue: American Journal of Interdisciplinary Studies
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 5.A
  - 5.C
  - 7.A
  - 12.B
  - 4.B
  - 10.A
tldr: Systematic review shows AI models outperform traditional credit scoring, enabling faster, more inclusive loan assessments but raising significant ethical and regulatory challenges.
problem_and_motivation: Traditional credit assessment is slow, subjective, and excludes unbanked populations. AI and predictive analytics offer faster, more consistent, and more inclusive alternatives, yet their integration introduces challenges in transparency and fairness.
approach:
  - Followed PRISMA guidelines for a systematic review of 102 peer-reviewed studies from 2000-2023.
  - Searched major databases including Scopus, Web of Science, IEEE Xplore, and Google Scholar.
  - Applied inclusion criteria focusing on AI and predictive analytics in commercial and digital banking environments.
  - Performed a narrative synthesis of findings on algorithmic performance, inclusion, and ethics.
findings:
  - num: 78 out of 86 comparison studies found AI models outperform traditional methods in AUC and Gini metrics.
  - num: AI models improve predictive accuracy by 10-25% compared to traditional credit scoring models.
  - num: Automation reduces loan processing time by 60-80% and cuts origination costs by 20-35%.
  - num: AI-driven fintech platforms cut decision time from days to seconds.
  - Alternative data (mobile metadata, utility bills, psychometrics) enables accurate credit assessment for thin-file borrowers.
  - num: Approval rates for thin-file applicants rose by 25-40% using alternative data with no increase in default risk.
  - Concerns about algorithmic bias and "black-box" model opacity were raised in 48 reviewed studies.
  - num: AI investments in credit automation are typically recouped within 1-2 years, yielding up to 5x returns.
  - Explainable AI (XAI) tools like SHAP and LIME are recommended to enhance transparency and regulatory compliance.
  - num: Real-time credit scoring systems are associated with significantly lower non-performing loan ratios.
key_figures_tables:
  - "Figure 1: AI-Enabled Credit Decision Automation Framework → Illustrates the end-to-end AI decisioning pipeline."
  - "Figure 3: Drivers and Limitations of Traditional Credit Scoring Models → Highlights key advantages and shortcomings."
  - "Figure 5: Workflow of Machine Learning-Based Credit Decisioning → Shows the process from input to task automation."
  - "Figure 9: AI-Powered Loan Decisions with Explainability → Demonstrates the link between XAI and consumer trust."
  - "Figure 11: PRISMA-Based Methodological Framework → Shows the systematic review screening process."
key_equations:
  - equation: "AUC = ∫_0^1 TPR(FPR^{-1}(x)) dx"
    explanation: "Area under ROC curve, a key metric for model discrimination performance."
definitions:
  - term: "AI"
    definition: "Artificial Intelligence, simulating human decision-making in banking via ML, NLP, and expert systems."
  - term: "AUC"
    definition: "Area Under the ROC Curve, a measure of a model's ability to distinguish between classes."
  - term: "ECOA"
    definition: "Equal Credit Opportunity Act, a U.S. law requiring non-discriminatory lending practices."
  - term: "GDPR"
    definition: "General Data Protection Regulation, an EU law enshrining the right to explanation for algorithmic decisions."
  - term: "PRISMA"
    definition: "Preferred Reporting Items for Systematic Reviews and Meta-Analyses, a guideline for transparent review."
  - term: "SHAP"
    definition: "SHapley Additive exPlanations, a technique for explaining the output of machine learning models."
  - term: "XAI"
    definition: "Explainable Artificial Intelligence, techniques to make AI models transparent and interpretable."
critical_citations:
  - "[Bhatore et al., 2020] — Systematic review on ML for credit risk."
  - "[Boot et al., 2021] — Foundational comparison of traditional and AI lending models."
  - "[Lessmann et al., 2015] — Benchmarking study showing ML superiority."
  - "[Sadok et al., 2022] — Reviews AI applications in bank credit analysis."
  - "[Tzougas & Kutzkov, 2023] — Demonstrated ML improves default prediction by over 25%."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: "Directly reviews predictive models for credit risk, analogous to spending prediction."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: "Covers advanced methods like LSTMs and ensembles that are foundational for forecasting."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: "Discusses real-time scoring and fraud detection, core to anomaly identification."
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: "Reviews algorithms like RF and GBMs that are also used in transaction anomaly detection."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: "Discusses borrower segmentation using behavioral and transactional data."
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: "Reviews classifiers that can be applied to profile classification."
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: "Provides context on how financial data can be used for decision-making, but no specific strategy."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: "Extensively evaluates algorithm performance using metrics like AUC and Gini."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: "Specifically analyzes the limitations of traditional manual and statistical credit systems."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: "Raises concerns about data privacy and consent in the use of behavioral data."
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: "Discusses mobile platforms briefly as a deployment vector but not as a primary design focus."
  contribution: "This paper directly justifies Odin's use of predictive models for financial forecasting by providing systematic evidence of their superiority over traditional methods. It supports the development of behavioral profiles (Topic 5.C) by reviewing classification approaches using transactional and alternative data. The findings on operational efficiency gains justify Odin's mobile-first design (Topic 9.A) by demonstrating the business case for real-time, automated decision-making."
  directly_justifies:
    - "Machine learning models consistently outperform traditional methods in predicting financial outcomes."
    - "Automation reduces processing time by over 60% and substantially lowers operational costs."
    - "Alternative data can expand financial inclusion without increasing default risk."
    - "Explainable AI (XAI) tools are essential for maintaining user trust and regulatory compliance."
  limits: "None identified."
  mapping_rationale: "A systematic scan across all 12 functional domains was performed to assess the paper's relevance to Odin. The review's core contributions directly address the domains of 'Spending Forecasting' (topics 6.A, 6.B) and 'Anomaly Detection' (8.A, 8.B), making them high relevance. It also provides strong support for 'System Evaluation' (12.B) by extensively benchmarking predictive algorithms. Borderline cases were considered: the paper's discussion of behavioral patterns touches on 'Behavioral Profiling' (5.A, 5.C) but is not the central theme, thus assigned medium relevance. The focus on user trust and data privacy (10.A) was flagged as medium due to the explicit discussion of regulatory and ethical concerns. Domains such as 'Budget Recommendation' (7.B, 7.C) and 'User Retention' (11.A) were considered and rejected, as the paper does not address constrained allocation, savings, or engagement strategies specific to PFMS, but rather focuses on the core predictive engine. The paper is highly relevant to Odin's foundational infrastructure for prediction and risk assessment, though its scope is broader than the personal finance domain."
limitations:
  - "The systematic review is limited to studies published in English, potentially excluding relevant non-English research."
  - "The synthesis does not include a formal meta-analysis due to methodological heterogeneity in the included studies."
  - "It primarily focuses on commercial banking, with limited direct focus on the personal finance management context of Odin. [unacknowledged]"
remember_this:
  - "AI models improve credit risk prediction accuracy by 10-25% over traditional methods."
  - "Loan processing time can be reduced by 60-80% through automation."
  - "Alternative data sources are critical for assessing thin-file and unbanked populations."
  - "Explainable AI is essential for regulatory compliance and user trust in automated decisions."
  - "Ensemble methods like XGBoost and random forests dominate in predictive performance."
```
---

## Paper 3: Casolaro et al_summarized.md

**Source File:** `Casolaro et al_summarized.md`

```yaml
paper_id: 10.3390/info14110598
designation: international
title: Deep Learning for Time Series Forecasting: Advances and Open Problems
authors: Casolaro, A.; Capone, V.; Iannuzzo, G.; Camastra, F.
year: 2023
venue: Information
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
tldr: Comprehensive review of deep learning architectures for time series forecasting, covering CNNs, RNNs, GNNs, Transformers, GANs, and diffusion models with benchmarks.
problem_and_motivation: Existing reviews on deep learning for time series forecasting lack coverage of recent architectures like Transformers, Graph Neural Networks, and diffusion models. They also fail to provide a clear distinction between models suited for short-term versus long-term forecasting.
approach:
  - Surveys deep learning architectures for short-term forecasting including CNNs, TCNs, RNNs, GNNs, Deep Gaussian Processes, GANs, and Diffusion Models.
  - Surveys architectures for long-term forecasting, focusing on the Transformer and its variants like Informer, Autoformer, and FEDformer.
  - Reviews other heterogeneous models including continuous recurrent units and MLP-based forecasters.
  - Presents benchmark datasets for both short-term (e.g., M4) and long-term (e.g., ETT, Traffic, Weather) forecasting.
  - Compares performance of Transformer variants on long-term benchmarks using MSE and MAE metrics.
findings:
  - Transformer variants like PatchTST and Crossformer achieve state-of-the-art performance on long-term forecasting benchmarks.
  - num: LSTM and GRU networks are widely applied for short-term forecasting but suffer from vanishing gradients and inability to capture very long-range dependencies.
  - Graph Neural Networks effectively model spatial dependencies in multivariate time series forecasting.
  - Diffusion models like TimeGrad and ScoreGrad show promise for probabilistic short-term forecasting.
  - All deep learning models, except Deep Gaussian Processes, lack inherent uncertainty quantification for predictions.
  - Deep learning models are prone to overfitting, especially with complex architectures, and often require adequately long time series for training.
  - Many models assume dynamical stationarity, leading to performance degradation under concept drift.
key_figures_tables:
  - Table 5: LSTM applications on time series forecasting → Widely used for diverse domains like finance, energy, and health.
  - Table 13: Multivariate long-term forecasting benchmarks among Transformer variants → PatchTST and Crossformer generally achieve lowest MSE and MAE across datasets.
  - Figure 12: Composition of the M4 dataset → M4-Monthly and M4-Quarterly are the largest components of the benchmark.
key_equations:
  - equation: y(t) = ∑_{a=1}^{q} w(a)X(t-a)
    explanation: Definition of causal 1D convolution for TCNs.
  - equation: Y = softmax(QK^T/√D_k)V
    explanation: Scaled dot-product attention mechanism in Transformers.
definitions:
  - term: TCN
    definition: Temporal Convolutional Network using causal and dilated convolutions.
  - term: LSTM
    definition: Long Short-Term Memory network with gating mechanisms to control information flow.
  - term: GNN
    definition: Graph Neural Network handling spatial dependencies via graph structure.
  - term: DGP
    definition: Deep Gaussian Process providing predictive uncertainty.
  - term: GAN
    definition: Generative Adversarial Network with generator and discriminator trained adversarially.
  - term: DDPM
    definition: Denoising Diffusion Probabilistic Model using forward and reverse Markov chains.
  - term: SDE
    definition: Stochastic Differential Equation for continuous diffusion processes.
critical_citations:
  - "[Vaswani et al., 2017] — Introduced Transformer architecture with self-attention."
  - "[Hochreiter & Schmidhuber, 1997] — Proposed LSTM for mitigating vanishing gradients."
  - "[Goodfellow et al., 2014] — Pioneered Generative Adversarial Networks."
  - "[Makridakis et al., 2020] — Presented M4 competition benchmark for forecasting."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: The paper surveys state-of-the-art forecasting models directly applicable to spending prediction.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Reviews specific algorithms like LSTM, TCN, and Transformers for time series forecasting.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Forecasting methods inform budget recommendation by providing future spending estimates.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Accurate forecasting is a prerequisite for effective budget recommendations.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Forecasting models can be used as a baseline for detecting anomalies in spending.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: Mentions models like LSTM and GANs which are also used for anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Discusses evaluation metrics (MSE, MAE) and benchmark datasets for forecasting models.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Provides extensive empirical comparison of various forecasting algorithms on standard benchmarks.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: low
      justification: While not directly about budget recommendation, the forecasting evaluation methods are relevant.
  contribution: "This paper provides a comprehensive taxonomy of deep learning models for time series forecasting. It systematically categorizes models for short-term and long-term forecasting, which directly informs Odin's architecture selection. The survey of Transformer variants and their benchmarks offers actionable insights for designing Odin's forecasting module. The discussion of open problems like uncertainty quantification and concept drift highlights key challenges for Odin's robustness. Overall, the paper serves as a foundational reference for Odin's predictive analytics engine."
  directly_justifies:
    - "LSTM and GRU networks are suitable for short-term spending prediction due to their ability to handle sequential data."
    - "Transformer variants like Informer and Autoformer can be adapted for long-term forecasting of user spending trends."
    - "Graph Neural Networks can model correlations between different spending categories in multivariate time series."
    - "Benchmark datasets like M4 and ETT provide standards for evaluating Odin's forecasting accuracy."
    - "Deep Gaussian Processes can provide uncertainty estimates crucial for Odin's risk-aware budget recommendations."
  limits:
    - "The paper is a survey and does not present empirical results on personal finance-specific data."
    - "Focus is on general time series forecasting, not specifically tailored to individual-level spending behavior."
    - "Models reviewed require large amounts of data which may not be available for cold-start users."
    - "Does not address privacy-preserving or federated learning for forecasting, relevant for Odin."
  mapping_rationale: "A systematic scan of all 12 Odin functional domains was performed. The paper's primary focus on time series forecasting algorithms maps directly to the 'Spending Forecasting' domain (codes 6.A, 6.B). The review of model evaluation and benchmarks is relevant to the 'System Evaluation' domain (12.A, 12.B, 12.C). It also provides contextual support for 'Budget Recommendation' (7.A, 7.B) as forecasting is a core component, and 'Anomaly Detection' (8.A, 8.B) as forecasting can be used for baseline prediction. The paper is not directly relevant to domains like 'Filipino Cultural Context', 'Mobile-First Design', or 'Data Privacy'. The 'Behavioral Profiling' domain is only tangentially touched upon through forecasting user behavior. The 'Savings & Debt Management' domain is not addressed. Borderline cases included the relevance to 'Budget Recommendation' (medium) because forecasting informs the budget, and 'Anomaly Detection' (contextual) because the paper doesn't explicitly address anomaly detection. Ultimately, the paper offers a high-level technical foundation for Odin's forecasting and evaluation modules but lacks specific application to the Filipino personal finance context."
limitations:
  - "No specific application to personal finance or Filipino context. [unacknowledged]"
  - "Does not address cold-start scenarios prevalent in new PFMS users. [unacknowledged]"
  - "Does not provide guidelines for real-time or resource-constrained forecasting on mobile devices. [unacknowledged]"
  - "The discussion on concept drift does not provide practical mitigation strategies for personal finance data. [unacknowledged]"
remember_this:
  - "PatchTST and Crossformer are state-of-the-art for long-term forecasting."
  - "Deep Gaussian Processes uniquely provide uncertainty quantification."
  - "Forecasting models are prone to overfitting and require adequate data length."
  - "Concept drift significantly degrades prediction accuracy over time."
  - "num: Transformer variants can reduce MSE by over 50% compared to simpler RNNs on benchmarks."
```
---

## Paper 4: Gerzon et al_summarized.md

**Source File:** `Gerzon et al_summarized.md`

```yaml
paper_id: 10.52006/main.v6i2.752
designation: local
title: Financial Literacy and Financial Well-Being of Nurses of a First-Class Province in the Philippines
authors: Gerzon, R. A.; Lopena, G. L.
year: 2023
venue: Philippine Social Science Journal
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 10.A
  - 11.A
tldr: Financial literacy correlates strongly with financial well-being among Filipino public health nurses, with higher monthly income linked to greater financial literacy.
problem_and_motivation: Filipino nurses face low pay, financial stress, and poor work performance, yet their financial literacy and well-being are underexplored. Understanding these factors is critical for designing targeted financial programs to improve their economic resilience and job outcomes.
approach:
  - Descriptive-correlational design with 178 randomly stratified public health nurses from a first-class Philippine province.
  - Researcher-made 52-item questionnaire measuring financial literacy (knowledge and behavior) and financial well-being (discipline, security, resilience) on a four-point Likert scale.
  - Instrument validity (Lawshe's CVR=0.91) and reliability (Cronbach's alpha: financial literacy=0.945, financial well-being=0.904) were established.
  - Data collected via web-based and printed surveys with informed consent and ethical clearance.
  - Pearson, Point Biserial, Rank Biserial, and Spearman Rank correlations used for analysis.
findings:
  - num: Overall financial literacy was high (M=3.22, SD=0.39), with financial knowledge (M=3.22, SD=0.43) and behavior (M=3.21, SD=0.40) both rated high.
  - num: Financial well-being was rated as great (M=3.03, SD=0.46), with discipline (M=3.26, SD=0.52) very great, security (M=2.96, SD=0.55) great, and resilience (M=2.88, SD=0.55) great.
  - num: Monthly income had a significant positive correlation with financial literacy (r=0.223, p=0.003), while age, sex, civil status, and dependents did not.
  - num: No demographic factor significantly correlated with financial well-being.
  - num: Financial literacy and financial well-being showed a strong positive correlation (rs=0.660, p=0.000), supporting the conceptual model.
  - Higher-income nurses demonstrated very high financial knowledge and behavior.
  - Nurses with 2 or more dependents had very high financial knowledge.
key_figures_tables:
  - Table 1: Financial literacy levels by demographics → Older, higher-income nurses with more dependents have higher knowledge.
  - Table 2: Financial well-being levels by demographics → Discipline is very great across all groups.
  - Table 3: Correlation between demographics and financial literacy → Only monthly income is significantly related.
  - Table 4: Correlation between demographics and financial well-being → No significant relationships found.
  - Table 5: Correlation between financial literacy and well-being → Strong positive relationship.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Financial Literacy
    definition: Combination of financial knowledge and financial behaviors essential for sound monetary decisions.
  - term: Financial Well-Being
    definition: State of financial discipline, security, and resilience enabling present and future financial satisfaction.
critical_citations:
  - "[Joo, 1998] — Conceptual model for personal financial wellness."
  - "[Parcia & Estimo, 2017] — Financial literacy, behavior, stress, and wellness among employees."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Directly studies Filipino public health nurses as a professional demographic.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Provides income, dependency, and financial behavior data for this demographic.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Assesses financial knowledge and behaviors of nurses.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: Highlights financial practices like savings and debt management in Philippine context.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Mentions Data Privacy Act compliance but no system design implications.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: Implies engagement through financial literacy programs but no UX/engagement study.
  contribution: This paper provides baseline evidence that financial literacy is a significant predictor of financial well-being among Filipino public health nurses. It directly informs Odin's behavioral profiling module (5.A, 5.B) by demonstrating demographic and income-related variations in financial literacy and well-being. The strong correlation supports Odin's design assumption that improving financial literacy via personalized recommendations can enhance user financial health. The findings also justify the inclusion of income and dependency status as critical features for user profiling and budget recommendation systems. However, the paper does not address algorithmic or system-specific aspects.
  directly_justifies:
    - "Financial literacy significantly predicts financial well-being among Filipino nurses."
    - "Monthly income is positively correlated with financial literacy level."
    - "Demographic factors like age, sex, and civil status do not significantly affect financial well-being."
    - "Higher financial literacy is associated with better financial discipline, security, and resilience."
  limits:
    - "Sample restricted to nurses in one province, limiting generalizability."
    - "Self-reported measures may introduce response bias."
    - "Cross-sectional design prevents causal inference."
    - "Demographic variables limited to age, sex, civil status, income, and dependents."
  mapping_rationale: Systematic scan of all 12 functional domains and their associated topic codes was performed. Domains flagged as relevant: Filipino Cultural Context (2.A, 2.B, 2.C, 2.D) for the cultural and demographic setting; Behavioral Profiling (5.A, 5.B, 5.C) for financial literacy and well-being measures; Existing Systems (4.A, 4.B) considered but rejected as no system comparison is made; Budget Recommendation (7.A–7.D) rejected as no algorithmic or budget allocation content; Anomaly Detection (8.A–8.C) rejected; Mobile-First Design (9.A, 9.B) rejected; Data Privacy (10.A) considered low due to methodological mention only; User Retention (11.A, 11.B) considered low due to no engagement study; System Evaluation (12.A–12.C) rejected; Savings/Debt (13.A–13.C) considered contextual due to discussion of savings and debt behaviors. Overall relevance is high for demographic and behavioral profiling domains, contextual for culturally specific practices, and low for privacy/engagement. The paper provides foundational evidence for Odin's behavioral and demographic modules.
limitations:
  - "Sample size limits generalizability beyond one province."
  - "Self-reported questionnaire may be subject to social desirability bias."
  - "No qualitative data to explain quantitative findings."
remember_this:
  - "Financial literacy strongly predicts financial well-being among Filipino nurses."
  - "Monthly income is the only demographic factor linked to financial literacy."
  - "Nurses reported high financial literacy and great financial well-being overall."
  - "The correlation between literacy and well-being is r=0.660, indicating a strong relationship."
  - "Higher-income nurses demonstrate very high financial knowledge and behavior."
```
---

## Paper 5: Yashwanth et al_summarized.md

**Source File:** `Yashwanth et al_summarized.md`

```yaml
paper_id: "4a8e6c7d-5f4e-4d3c-9b2a-1f0e2d3c4b5a"
designation: "international-algorithm-specific"
title: "DataStream Adapt: Unified Detection Framework for Gradual and Abrupt Concept Drifts"
authors: "Yashwanth, M.; Sandeepa, D.; Shareef, S.K."
year: 2023
venue: "Synthesis: A Multidisciplinary Research Journal"
odin_topics:
  - "6.A"
  - "6.B"
  - "8.A"
  - "8.B"
  - "8.C"
  - "12.A"
  - "12.B"
tldr: "Presents DataStream Adapt, a unified framework integrating hybrid drift detection, adaptive thresholding, and ensemble learning to detect and respond to both abrupt and gradual concept drifts, outperforming existing methods."
problem_and_motivation: "Existing drift detectors struggle to simultaneously handle abrupt and gradual drifts, rely on fixed thresholds causing false positives or delayed adaptation, and decouple detection from model updating, limiting robustness in evolving data streams."
approach:
  - "Uses the Hyperplane synthetic dataset with controlled drift scenarios for benchmarking."
  - "Combines error-rate monitoring and statistical divergence (KL) for hybrid detection."
  - "Employs CUSUM for abrupt drift detection and moving average for gradual drift."
  - "Implements an adaptive threshold controller that adjusts sensitivity based on stream volatility."
  - "Integrates a drift certainty scoring mechanism to quantify confidence in detected drifts."
  - "Uses a drift-aware ensemble classifier with weighted majority voting and dynamic learner replacement."
  - "Evaluates against DDM, ADWIN, and EDDM baselines in a prequential streaming setup."
findings:
  - "num: Achieves detection delay of 31.2 instances for abrupt drift and 64.8 for gradual drift."
  - "num: False positive rate of 0.041, significantly lower than ADWIN's 0.147."
  - "num: F1-score of 0.89 on post-drift classification, outperforming all baselines."
  - "Demonstrates robust performance under both drift types with low latency and high noise resistance."
key_figures_tables:
  - "Table 1: Performance comparison under abrupt drift → shows DataStream Adapt lowest delay and FPR."
  - "Table 2: Performance under gradual drift → confirms lowest delay and highest F1."
  - "Figure 2: Comparative performance bar charts → visualizes delay, FPR, and F1 across methods."
key_equations:
  - equation: "S_t = max(0, S_{t-1} + (\\epsilon_t - \\epsilon_0 - \\delta))"
    explanation: "CUSUM statistic for abrupt drift detection."
  - equation: "\\bar{x}_t = \\frac{1}{k} \\sum_{i=t-k+1}^{t} x_i"
    explanation: "Moving average for gradual drift detection."
  - equation: "\\mathcal{C}_t = \\alpha \\cdot I_{\\text{abrupt}} + (1-\\alpha) \\cdot I_{\\text{gradual}}"
    explanation: "Drift certainty score combining detectors."
  - equation: "h_t = h_0 \\cdot (1 + \\lambda \\cdot \\nu_t)"
    explanation: "Adaptive threshold based on volatility."
  - equation: "\\hat{y} = \\arg\\max_y \\sum_i w_i \\cdot \\mathbb{I}[h_i(x)=y]"
    explanation: "Weighted majority voting for ensemble."
definitions:
  - term: "Concept Drift"
    definition: "Change in data distribution over time that degrades model performance."
  - term: "CUSUM"
    definition: "Cumulative sum control chart for detecting abrupt changes."
  - term: "ADWIN"
    definition: "Adaptive Windowing algorithm for drift detection using statistical hypothesis testing."
critical_citations:
  - "[Gama et al., 2004] — DDM baseline for drift detection."
  - "[Bifet and Gavaldà, 2007] — ADWIN baseline."
  - "[Baena-García et al., 2006] — EDDM baseline."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Provides adaptive modeling techniques applicable to spending prediction."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "medium"
      justification: "Offers drift adaptation methods for time-series forecasting."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Directly addresses detection of unexpected changes in data streams."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Proposes a novel detection framework that can be adapted for spending anomalies."
    - code: "8.C"
      name: "Cold‑Start Baseline Strategies for Anomaly Detection"
      relevance: "low"
      justification: "Adaptive thresholding may inform baseline setting but not directly."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides evaluation metrics (delay, FPR, F1) applicable to PFMS modules."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Benchmarks detection and classification performance useful for assessing PFMS algorithms."
  contribution: "DataStream Adapt's hybrid detection engine can inform Odin's anomaly detection module to identify irregular spending patterns. Its adaptive threshold controller can be leveraged to reduce false alarms in volatile financial data. The drift-aware ensemble learning approach can enhance Odin's forecasting models by adapting to changes in user behavior. The evaluation metrics and benchmarking methodology can guide the assessment of Odin's algorithmic components."
  directly_justifies:
    - "DataStream Adapt detects abrupt drift with 31.2 instance delay, enabling rapid response to sudden spending changes."
    - "It maintains a false positive rate of 0.041, supporting reliable anomaly detection without overwhelming users."
    - "The framework achieves an F1-score of 0.89, indicating robust classification after drift, which can be applied to spending categorization."
  limits:
    - "None identified."
  mapping_rationale: "A systematic scan across all 12 functional domains and associated topic codes was performed. The algorithmic nature of the paper flagged domains related to predictive modeling (6.A, 6.B), anomaly detection (8.A, 8.B, 8.C), and system evaluation (12.A, 12.B) as relevant, with high relevance assigned to 8.A and 8.B because the paper directly proposes detection algorithms. Medium relevance was given to 6.A, 6.B, 12.A, and 12.B as they provide supporting techniques and evaluation frameworks. Low relevance to 8.C as it only tangentially touches cold-start strategies. Domains such as Filipino cultural context, expense categorization, budget recommendation, user retention, and savings/debt management were considered and rejected because the paper does not address financial behavior, user constraints, or personal finance applications. Borderline cases like behavioral profiling (5.A) were rejected as the paper does not discuss user profiles or cold-start classification. The overall relevance is moderate: while not finance-specific, the algorithmic contributions are directly applicable to Odin's adaptive and anomaly detection modules."
limitations:
  - "Relies on synthetic Hyperplane dataset, which may not capture all real-world complexities."
  - "Currently supports only binary classification, limiting direct use in multi-class spending categorization."
  - "Assumes a fixed feature set; may require feature engineering for financial data."
  - "Initial parameter sensitivity and lack of automated tuning may hinder deployment without calibration [unacknowledged]."
remember_this:
  - "DataStream Adapt reduces abrupt drift detection delay by 62% compared to DDM."
  - "It achieves a false positive rate of 0.041, significantly lower than baselines."
  - "The adaptive threshold controller dynamically adjusts to stream volatility."
  - "Ensemble adaptation improves post-drift classification F1-score to 0.89."
  - "Framework supports both abrupt and gradual drifts in a unified pipeline."
```
---

## Paper 6: Yuan & Hernandez_summarized.md

**Source File:** `Yuan & Hernandez_summarized.md`

```yaml
paper_id: "10.1109/ACCESS.2023.3338705"
designation: "local" # National University, Philippines
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

## Paper 7: Apus et al_summarized.md

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

## Paper 8: Hu X. et al_summarized.md

**Source File:** `Hu X. et al_summarized.md`

```yaml
paper_id: "3c6e0b8a-9c3d-5b8a-9c3d-5b8a9c3d5b8a"
designation: "international-algorithm-specific"
title: "Two-Stage Predict+Optimize for Mixed Integer Linear Programs with Unknown Parameters in Constraints"
authors: "Hu, X.; Lee, J. C. H.; Lee, J. H. M."
year: 2023
venue: "NeurIPS 2023"
odin_topics:
  - "4.B"
  - "6.A"
  - "6.B"
  - "7.B"
  - "7.C"
  - "7.D"
  - "12.A"
  - "12.B"
tldr: "Proposes a two-stage predict+optimize framework for MILPs with unknown parameters in constraints, with a general training algorithm using interior-point gradient approximations that outperforms prior methods on multiple benchmarks."
problem_and_motivation: "Prior Predict+Optimize frameworks handle unknown parameters only in the objective, and the only extension to constraints is ad-hoc and limited to packing/covering linear programs. A simpler, more general framework is needed for all MILPs, allowing correction when the estimated solution is feasible but suboptimal. Additionally, a general training algorithm is required to enable end-to-end learning for such problems."
approach:
  - "Introduces a Two-Stage framework where Stage 1 solves with estimated parameters, and Stage 2 solves with true parameters plus a penalty for changes from Stage 1."
  - "Provides an end-to-end training algorithm using a surrogate loss based on interior-point relaxation to differentiate through MILPs."
  - "Applies the method to three benchmarks: alloy production, 0-1 knapsack with unknown weights/prices, and nurse scheduling."
  - "Compares with classical regression methods (Ridge, k-NN, CART, RF, NN) and state-of-the-art (IntOpt-C, CombOptNet)."
  - "Demonstrates superior post-hoc regret performance across all benchmarks."
  - "Evaluates using the proposed Two-Stage framework, with Stage 2 optimization applied at test time for all methods."
findings:
  - "num: On brass alloy, 2S achieves 6.18%-35.63% lower mean post-hoc regret than Hu et al. across penalty factors."
  - "num: On 0-1 knapsack with capacity 100 and penalty 0.21, 2S obtains 1.26 regret vs CombOptNet's 9.45."
  - "num: On nurse scheduling, 2S reduces regret by at least 7.61% to 62.49% compared to classical methods."
  - "The Two-Stage framework consistently outperforms the prior Hu et al. framework in all settings."
  - "The proposed training method generalizes to all MILPs, unlike prior work restricted to packing/covering LPs."
key_figures_tables:
  - "Table 2: Comparison of Two-Stage vs Hu et al. framework on alloy production → Two-Stage always yields lower regret."
  - "Table 3: Post-hoc regret for alloy production across training methods → 2S best, outperforms all baselines."
  - "Table 4: Post-hoc regret for 0-1 knapsack → 2S significantly outperforms CombOptNet and classical methods."
  - "Table 5: Post-hoc regret for nurse scheduling → 2S achieves best performance across penalty factors."
key_equations:
  - equation: "PReg(θ̂, θ) = obj(x_corr^*, θ) - obj(x^*(θ), θ) + Pen(x^*(θ̂) → x_corr^*)"
    explanation: "Post-hoc regret for correction-based framework."
  - equation: "x_2^* = argmin obj(x, θ) + Pen(x_1^* → x, θ) s.t. C(x, θ)"
    explanation: "Stage 2 optimization with penalty."
  - equation: "dPReg/dw_e = (∂PReg/∂x_2^*) (∂x_2^*/∂x_1^*) (∂x_1^*/∂θ̂) (∂θ̂/∂w_e) + ..."
    explanation: "Chain rule for gradient computation."
definitions:
  - term: "Predict+Optimize"
    definition: "Framework for training prediction models to minimize regret of downstream optimization decisions."
  - term: "Post-hoc regret"
    definition: "Loss function comparing quality of final solution to true optimal, including penalties."
  - term: "Two-Stage Predict+Optimize"
    definition: "Proposed framework with soft commitment in Stage 1 and correction in Stage 2 via optimization."
  - term: "MILP"
    definition: "Mixed Integer Linear Program."
  - term: "Interior-point relaxation"
    definition: "Convex relaxation of MILP using logarithmic barriers to enable gradient computation."
critical_citations:
  - "[Elmachtoub and Grigas, 2017] — Introduced Predict+Optimize framework."
  - "[Hu et al., 2022] — Prior work on constraints, limited to packing/covering LPs."
  - "[Mandi and Guns, 2020] — Interior-point differentiation for LPs used in training."
relevance:
  topics:
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Identifies and addresses the limitation of prior frameworks that only handle packing/covering LPs, proposing a general MILP solution."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Provides a training method for neural networks to predict unknown parameters from features, directly applicable to spending forecasting."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Offers a forecasting algorithm that optimizes for downstream decision quality, relevant for sequential spending prediction."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "The two-stage optimization can be adapted for budget recommendation by solving allocation problems with penalties, though not explicitly explored."
    - code: "7.C"
      name: "Constrained Optimization Approaches for Budget Allocation"
      relevance: "high"
      justification: "The framework is a constrained optimization approach that models budget allocation with multiple constraints and uncertainties."
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "high"
      justification: "Explicitly handles infeasibility of first-stage solutions via second-stage corrections with penalties, addressing budget infeasibility."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Introduces the post-hoc regret as an evaluation metric for decision-focused learning, useful for assessing PFMS modules."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Performs extensive benchmarking against classical and state-of-the-art methods, providing a robust evaluation of algorithmic modules."
  contribution: "The proposed two-stage framework can directly inform Odin's budget recommendation module (7.C, 7.D) by providing a principled method for handling unknown constraints and correcting infeasible allocations. The training algorithm enhances Odin's spending forecasting capabilities (6.A, 6.B) by learning predictors that optimize for actual budget outcomes rather than parameter accuracy. The evaluation methodology (12.B) offers a rigorous way to test Odin's algorithmic components. The identification of limitations in existing systems (4.B) justifies the need for Odin's innovative approach."
  directly_justifies:
    - "The two-stage framework outperforms prior methods in handling unknown constraints, supporting Odin's use of similar optimization for budget allocation."
    - "Training predictors with post-hoc regret improves decision quality, which is crucial for Odin's spending forecasts."
    - "The approach handles infeasibility via penalty functions, aligning with Odin's need for robust budget recommendations under uncertainty."
    - "The generalized MILP capability enables Odin to model complex constraints like savings goals and debt payments."
  limits:
    - "The paper does not directly address Filipino financial behaviors or expense categorization."
    - "It assumes penalty functions are known and linear, which may not hold for all PFMS contexts."
  mapping_rationale: "A systematic scan across all 12 functional domains identified relevance primarily in algorithmic and evaluation topics. Domains related to Filipino cultural context, expense categorization, behavioral profiling, mobile design, data privacy, retention, and savings/debt management were rejected as the paper does not address these. The domains of Existing Systems & Gaps, Spending Forecasting, Budget Recommendation, and System Evaluation were flagged. Topic 4.B (Limitations and Gaps) was selected as high because the paper explicitly addresses the limitation of prior work and proposes a general solution. Topics 6.A and 6.B (predictive modeling and forecasting algorithms) were selected as high because the paper provides a training method for forecasting parameters optimized for decision outcomes. Topics 7.C (constrained optimization) and 7.D (infeasibility handling) were selected as high because the two-stage framework directly models these aspects for budget recommendation. Topic 12.B (evaluation of algorithmic modules) was selected as high due to extensive benchmarking. Topics 7.B (budget recommendation) and 12.A (evaluation frameworks) were assigned medium because the paper does not explicitly focus on budget recommendation but the methods are applicable. Borderline cases: the paper's application to nurse scheduling could touch on resource allocation but not directly financial, so not selected. The overall relevance is high for informing Odin's algorithmic design and evaluation."
limitations:
  - "Requires both stages to be expressible as MILPs, limiting non-linear penalty functions, though some non-linearities can be handled with extra variables."
  - "The surrogate gradient computation is an approximation and may not yield exact gradients."
  - "Computational cost is higher than classical regression methods, especially for large-scale problems. [unacknowledged]"
remember_this:
  - "Two-stage framework reduces post-hoc regret by up to 35% over prior methods."
  - "Generalizes Predict+Optimize to all MILPs with unknown constraints."
  - "End-to-end training improves prediction accuracy for decision-focused objectives."
  - "Handles infeasibility via penalty-based second-stage optimization."
  - "Outperforms classical and state-of-the-art methods across three benchmarks."
```
---

## Paper 9: Leibiker & Talmon_summarized.md

**Source File:** `Leibiker & Talmon_summarized.md`

```yaml
paper_id: 10.5555/3635637.3635953
designation: international-algorithm-specific
title: A Recommendation System for Participatory Budgeting
authors: Leibiker, G.; Talmon, N.
year: 2023
venue: International Conference on Autonomous Agents and Multiagent Systems
odin_topics:
  - 5.A
  - 7.A
  - 7.B
  - 7.C
  - 12.A
  - 12.C
tldr: Machine learning and recommender systems predict missing voter preferences from partial ballots to reduce cognitive burden in participatory budgeting.
problem_and_motivation: Participatory budgeting processes face information overload as voters must consider many projects. This increases cognitive burden and reduces participation. Existing systems lack methods to estimate complete voter preferences from partial ballots.
approach:
  - Formulates participatory budgeting with partial ballots and defines three algorithmic tasks: random, offline, and online preference elicitation.
  - Uses real-world PB datasets from Warsaw with voter and project attributes.
  - Implements prediction models: collaborative filtering via matrix factorization, factorization machines, and binary classification with XGBoost.
  - Evaluates prediction accuracy using precision, recall, F1, and bundle quality using Symmetric Distance and Fractional Allocation score.
  - Compares proposed sampling strategies (popularity, consensus, controversial) against a naive random sampling baseline.
findings:
  - num: Proposed solutions outperform naive sampling for low sampling degrees (0.1 and 0.15).
  - num: Classification-based prediction achieves the highest Fractional Allocation scores across all sampling degrees.
  - num: Online and offline popularity sampling strategies yield superior bundle prediction compared to random sampling.
  - The adaptive controversial online strategy shows improved performance over static offline methods.
  - Increasing both sampling degree and LV degree (number of full-ballot voters) improves prediction accuracy.
key_figures_tables:
  - Table 1: Description of real-world PB datasets → Provides dataset characteristics used in experiments.
  - Figure 5: Heatmap of FA scores vs sampling and LV degree → Shows FA score increases with more data.
  - Figure 6: Heatmap of SD vs sampling and LV degree → Shows SD decreases with more data.
key_equations:
  - equation: "FA = \\lambda / B, \\lambda = \\sum_{p \\in pb \\cap rb} cost(p)"
    explanation: "Fraction of budget correctly allocated to winning projects."
definitions:
  - term: "Participatory Budgeting"
    definition: "Democratic process where community members decide how to spend a public budget."
  - term: "Partial Ballot"
    definition: "A vote where a voter expresses preferences for only a subset of projects."
  - term: "Approval Score"
    definition: "Number of voters who approve a given project."
  - term: "Consensus Level"
    definition: "Absolute difference between approvals and disapprovals for a project."
critical_citations:
  - "[Aziz & Shah, 2021] — Foundational survey of PB models."
  - "[Ricci et al., 2011] — Standard reference for recommender systems."
  - "[Talmon & Faliszewski, 2019] — Defines greedy approval voting rule for PB."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Predicts voter preferences using behavior patterns, analogous to financial profiling.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Directly addresses preference elicitation for budget allocation decisions.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: Proposes a recommendation system for project selection, similar to budget item recommendation.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: medium
      justification: Uses budget constraint as a hard limit in the voting rule, akin to allocation optimization.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Proposes Fractional Allocation score and Symmetric Distance for evaluating allocation quality.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: high
      justification: Evaluates recommendation accuracy and downstream budget allocation performance.
  contribution: "This paper provides a framework for preference elicitation that can inform Odin's budget recommendation module. The classification-based prediction approach can be adapted to predict user spending categories or savings allocations from partial inputs. The Fractional Allocation score offers a direct evaluation metric for budget recommendation quality. The study of online vs offline preference collection informs Odin's UX design for progressive disclosure."
  directly_justifies:
    - "Machine learning can effectively predict missing user preferences from partial data."
    - "Classification models outperform matrix factorization for preference prediction in this domain."
    - "Sampling strategies that target controversial items improve prediction accuracy."
    - "Increasing data collection from users improves overall system performance."
  limits:
    - "Dataset is from civic PB, not personal finance; spending vs voting preferences differ."
    - "Assumes voters have consistent preferences, which may not hold for financial behavior."
    - "Limited to approval-based preferences; Odin uses numeric/percentage allocations."
    - "Does not address cold-start scenarios where no prior user data exists. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains identified high relevance for Budget Recommendation (7.B) and Evaluation (12.A, 12.C), as the paper directly proposes and evaluates a recommendation system for constrained allocation. Medium relevance was assigned to Financial Behavioral Profiles (5.A) because preference prediction is analogous to financial profiling, and to Budgeting Strategies (7.A) and Constrained Optimization (7.C) as background. Domains like Expense Categorization (3.A), Mobile-First Design (9.A), and Data Privacy (10.A) were considered and rejected as the paper does not address these topics. Borderline cases included 7.A (preference elicitation) and 7.B (recommendation system), both selected. Overall, the paper is relevant for Odin's prediction and evaluation modules but requires adaptation from civic to personal finance contexts."
limitations:
  - "Dataset from civic PB may not generalize to personal finance contexts."
  - "Assumes static preferences; financial behavior is dynamic."
  - "Does not address user trust or privacy concerns in preference collection."
  - "Cold-start performance not evaluated. [unacknowledged]"
remember_this:
  - "Classification models achieved highest prediction accuracy for missing preferences."
  - "Online preference elicitation outperforms static sampling strategies."
  - "Increasing collected data by 30% improved Fractional Allocation score by up to 15%."
  - "Sampling controversial items yields better predictions than random or popularity-based sampling."
  - "Machine learning reduces cognitive burden in participatory budgeting decisions."
```
---

## Paper 10: Mareedu_summarized.md

**Source File:** `Mareedu_summarized.md`

```yaml
paper_id: "10.63282/3050-922X.IJERET-V4I4P106"
designation: "international"
title: "Zero Trust before the Hype: Foundational Concepts and Early AI-Driven Implementations"
authors: "Mareedu, A."
year: 2023
venue: "International Journal of Emerging Research in Engineering and Technology"
odin_topics:
  - "5.A"
  - "5.B"
  - "5.C"
  - "8.A"
  - "8.B"
  - "10.A"
  - "10.B"
  - "6.A"
  - "12.A"
tldr: "Reviews AI integration in early Zero Trust architectures, covering behavioral authentication, adaptive trust scoring, federated learning, and smart contracts for dynamic access control."
problem_and_motivation: "Traditional perimeter-based security models fail in cloud, mobile, and IoT environments due to implicit trust of internal networks. Organizations transitioning to distributed systems need continuous verification and dynamic access controls. Early implementations lacked adaptive capabilities and AI-driven decision-making."
approach:
  - "Reviews foundational Zero Trust concepts and early enterprise implementations before mainstream adoption."
  - "Synthesizes literature on AI-driven mechanisms including behavioral authentication, federated learning, and smart contracts."
  - "Analyzes enabling technologies such as edge computing, microservices, and service meshes for ZT enforcement."
  - "Examines challenges in model performance, policy governance, data security, and infrastructure constraints."
  - "Distills lessons for modern DevSecOps-integrated and quantum-aware Zero Trust designs."
findings:
  - "Early AI-ZT systems improved access control by using adaptive trust scores based on user behavior, device posture, and geolocation."
  - "Behavioral authentication reduced reliance on static credentials by monitoring typing patterns, mouse dynamics, and session activity."
  - "Predictive access modeling flagged anomalous actions such as unusual file transfers or access to rarely used servers."
  - "Smart contracts combined with AI risk engines enabled decentralized, self-enforcing policy execution."
  - "Event tokenization and SCIM profiles standardized security logs for real-time AI ingestion and rule adaptation."
  - "Early deployments suffered from overfitting, policy drift, lack of explainability, and training data leakage."
  - "Edge computing constraints limited real-time AI inference, requiring offloading to central cloud systems."
  - "Federated learning mitigated some privacy risks but introduced poisoning and tampering vulnerabilities."
  - "Explainable AI and auditability remained open challenges in regulated sectors such as finance and healthcare."
  - "Lessons from early AI-ZT informed context-aware agents, DevSecOps integration, and quantum-resilient cryptographic planning."
key_figures_tables:
  - "Figure 1: Contrast of perimeter-based security vs Zero Trust architecture → shift from trusted zones to identity-centric verification."
  - "Figure 2: Conceptual design of AI-enabled edge nodes with Zero Trust enforcement → local trust anchors and federated learning."
  - "Figure 3: Timeline of Zero Trust evolution from static perimeters to AI-enhanced quantum-aware frameworks → increasing dynamism."
  - "Table 1: Comparison of traditional security vs Zero Trust across trust model, segmentation, and authentication → identity-driven and continuous."
  - "Table 2: Common limitations of AI-powered Zero Trust deployments → overfitting, policy drift, explainability gaps, data leakage, and infrastructure limits."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "ZT"
    definition: "Zero Trust, a security model that eliminates implicit trust and requires continuous verification."
  - term: "ZTA"
    definition: "Zero Trust Architecture, a formal framework for implementing Zero Trust principles."
  - term: "AI"
    definition: "Artificial Intelligence, used for adaptive decision-making in access control."
  - term: "ML"
    definition: "Machine Learning, a subset of AI for behavioral modeling and anomaly detection."
  - term: "IAM"
    definition: "Identity and Access Management, the discipline of managing user identities and permissions."
  - term: "RBAC"
    definition: "Role-Based Access Control, granting permissions based on predefined roles."
  - term: "ABAC"
    definition: "Attribute-Based Access Control, granting permissions based on user, resource, and environment attributes."
  - term: "RAAC"
    definition: "Risk-Adaptive Access Control, adjusting permissions based on real-time risk scores."
  - term: "UEBA"
    definition: "User and Entity Behavior Analytics, systems that detect anomalies in user and device behavior."
  - term: "MFA"
    definition: "Multifactor Authentication, requiring multiple verification factors for access."
  - term: "XAI"
    definition: "Explainable AI, a field focused on making AI decisions interpretable to humans."
critical_citations:
  - "[Gilman & Barth, 2017] — Foundational Zero Trust architecture and continuous verification principles."
  - "[Forrester Research, 2010] — Formal introduction of the Zero Trust concept by John Kindervag."
  - "[NIST, 2018] — Standardized Zero Trust framework via NIST SP 800-207."
  - "[Google, 2014] — Early real-world enterprise Zero Trust implementation via BeyondCorp."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles of Filipino Young Professionals"
      relevance: "high"
      justification: "Discusses behavioral authentication and user baselines that map to financial behavioral profiling."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "medium"
      justification: "Addresses generalization issues and overfitting to limited datasets, relevant to cold-start challenges."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Reviews ML models for anomaly detection and behavioral classification in access control."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Anomaly detection in access patterns provides methods applicable to spending anomaly detection."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Covers ML algorithms and event tokenization for real-time anomaly identification."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "Extensively discusses training data leakage, model integrity, and secure distributed training."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "high"
      justification: "Highlights explainability, auditability, and regulatory compliance as trust prerequisites."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Predictive access modeling techniques are transferable to spending forecasting."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "contextual"
      justification: "Discusses evaluation challenges but does not provide a formal framework for PFMS."
  contribution: "This paper informs Odin's behavioral profiling module (5.A/5.C) by demonstrating how adaptive trust scoring and anomaly detection can be implemented using ML models. It directly guides Odin's anomaly detection subsystem (8.A/8.B) through coverage of event tokenization, risk scoring, and rule adaptation. The paper's detailed treatment of data privacy and model security (10.A) provides foundational justification for Odin's secure data handling and federated learning strategies. Its discussion of explainability and auditability (10.B) supports Odin's transparency requirements for user trust. Finally, the lessons on cold-start generalization (5.B) and predictive modeling (6.A) inform Odin's approach to new user profiling and spending forecasts."
  directly_justifies:
    - "Adaptive trust scoring using behavioral, device, and contextual signals can replace static rule-based access decisions."
    - "Federated learning enables model training without exposing raw sensitive user data."
    - "Lack of explainability in AI-driven decisions undermines user trust and regulatory compliance."
    - "Overfitting to narrow datasets limits generalization to novel behavioral patterns."
    - "Edge computing constraints require lightweight models for real-time inference."
  limits:
    - "The paper is a survey and does not present original empirical validation of specific algorithms."
    - "Focus on enterprise security rather than personal finance systems, requiring domain adaptation."
    - "Quantitative performance metrics for AI-ZT systems are not provided."
  mapping_rationale: "All 12 functional domains and their associated topic codes were systematically scanned. The following domains were flagged as relevant: Behavioral Profiling & Classification (high for 5.A, 5.C; medium for 5.B), Anomaly Detection (high for 8.A, 8.B), Data Privacy & User Trust (high for 10.A, 10.B), Spending Forecasting (medium for 6.A), and System Evaluation (contextual for 12.A). Borderline cases: the paper's discussion of behavioral baselines and anomaly detection in access patterns maps cleanly to 5.A/5.C and 8.A/8.B; its emphasis on model generalization issues relates to 5.B's cold-start problem; and its coverage of predictive modeling of access patterns maps to 6.A. The following domains were considered and rejected: Filipino Cultural Context (no Philippines-specific content), Expense Categorization (not about expense labels), Existing Systems & Gaps (focus is on security architectures, not PFMS systems), Budget Recommendation (access control policies are not budget allocation), Mobile-First Design (no mobile UX discussion), User Retention & Engagement (no engagement mechanisms), and Savings & Debt Management (not relevant). Overall, the paper provides strong foundational insights for behavioral profiling, anomaly detection, and trust/privacy in Odin, while its enterprise security framing requires adaptation to personal finance contexts."
limitations:
  - "Paper is a review, not primary research; lacks empirical validation of AI-ZT performance metrics. [unacknowledged]"
  - "Focus on enterprise and cloud environments; direct applicability to personal finance systems requires domain translation. [unacknowledged]"
  - "No discussion of mobile-first or consumer-facing financial applications. [unacknowledged]"
  - "Early AI-ZT models often overfit to narrow enterprise datasets, limiting generalization to novel user behaviors."
  - "Training data leakage and model poisoning present significant privacy and security risks in distributed ZT deployments."
remember_this:
  - "Behavioral authentication reduces reliance on static passwords by monitoring user interaction patterns."
  - "Adaptive trust scores dynamically adjust access based on device, location, and behavior."
  - "Explainability is critical for auditability and regulatory compliance in AI-driven security decisions."
  - "Edge computing and federated learning enable privacy-preserving, low-latency anomaly detection."
  - "Early AI-ZT models faced overfitting, policy drift, and infrastructure constraints that inform future system design."
```
---

## Paper 11: Espiritu P. et al_summarized.md

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

## Paper 12: Sabri et al_summarized.md

**Source File:** `Sabri et al_summarized.md`

```yaml
paper_id: 10.1057/s41264-023-00234-8
designation: international
title: Impact of financial behaviour on financial well-being: evidence among young adults in Malaysia
authors: Sabri, M. F.; Anthony, M.; Law, S. H.; Rahim, H. A.; Burhan, N. A. S.; Ithnin, M.
year: 2023
venue: Journal of Financial Services Marketing
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 3.B
  - 4.B
  - 5.A
  - 5.C
  - 7.A
  - 10.A
tldr: Financial behaviour mediates the relationships between financial literacy, socialisation, self-control, fintech, and financial well-being among young Malaysian adults during COVID-19.
problem_and_motivation: Young Malaysian adults face declining financial well-being due to COVID-19, including job loss, housing issues, and increased debt. The determinants of financial well-being, especially the mediating role of financial behaviour, remain unclear for this demographic, which constitutes a significant portion of the population.
approach:
  - Multi-stage random sampling collected 360 responses from young adults aged 18-29 across five Malaysian regions.
  - Structural equation modelling (SEM) was used to analyse the relationships between financial literacy, socialisation, self-control, fintech, financial behaviour, and well-being.
  - Financial behaviour was modelled as a mediator between four exogenous factors and financial well-being.
  - Sobel-Goodman mediation tests were used as a robustness check for the mediation effects.
findings:
  - num: Financial behaviour was the most important element influencing financial well-being (β = 0.48, t = 3.10, p < 0.05).
  - Financial behaviour significantly mediated the relationships between financial literacy, financial socialisation, self-control, financial technology, and financial well-being.
  - Financial literacy and self-control did not have a significant direct influence on financial well-being.
  - Financial technology and financial literacy were the factors most highly mediated by financial behaviour.
  - num: The model explained 74% of the variation in financial behaviour and 61% in financial well-being.
key_figures_tables:
  - Table 2: Reliability analysis of scales (Cronbach's alpha) for pilot and actual study → All constructs achieved acceptable reliability (>0.77).
  - Table 3: Average variance extracted (AVE) and composite reliability (CR) for constructs → All constructs met convergent validity and reliability thresholds (AVE > 0.5, CR > 0.6).
  - Table 4: Discriminant validity index summary for all constructs → The square root of AVE exceeded inter-construct correlations, confirming discriminant validity.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Financial well-being
    definition: A young adult's assessment of their quality of life based on their financial situation, including the ability to meet current commitments and have buffers for the future.
  - term: Financial behaviour
    definition: The actions of young adults regarding budgeting, cash flow management, spending plans, credit management, and long-term financial planning.
  - term: Financial technology (FinTech)
    definition: Innovative financial services that use new technologies to allow consumers to conduct financial activities through digital means.
  - term: Financial socialisation
    definition: The process by which young adults learn financial values, norms, and practices from agents like parents and family members.
  - term: Self-control
    definition: The ability to control oneself and overcome immediate needs for better future outcomes, including in financial matters.
critical_citations:
  - "[CFPB, 2015a] — Defines factors influencing financial well-being."
  - "[Deacon & Firebaugh, 1988] — Provides the systems theory underpinning the research model."
  - "[Xiao & Porto, 2017] — Supports the mediating role of financial behaviour."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: Studies young adults in Malaysia, a comparable ASEAN demographic, providing regional context.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Discusses income levels, debt (student loans, credit cards), and household size of young adults.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Core focus is on financial behaviour (budgeting, saving, credit use) and its direct influence on well-being.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Highlights the role of parental financial socialisation and family as key cultural influences on financial behaviour.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: low
      justification: Tangentially relevant as it discusses financial behaviour components like budgeting and spending, but not specific category design.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: contextual
      justification: Provides background on the financial struggles of young adults but does not evaluate existing PFMS.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly examines financial behaviour as a mediator and its classification through SEM, relevant to profiling.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses SEM to classify and validate the relationships between behaviour and its determinants.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Mentions financial behaviour components like having a budget and cash flow management as key to well-being.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Does not address data privacy, but contextual relevance for user trust is minimal.
  contribution: This paper provides empirical evidence that financial behaviour is a critical mediator for financial well-being, which directly supports the development of Odin's behavioral profiling module (5.A). The finding that financial technology only improves well-being when mediated by positive financial behaviour justifies Odin's focus on nudging users towards good behaviour rather than solely providing tools. The study's emphasis on financial socialisation and its impact on behaviour informs the design of culturally relevant onboarding and engagement strategies within Odin.
  directly_justifies:
    - "Financial behaviour is a significant predictor of financial well-being among young adults."
    - "Financial literacy alone does not directly improve financial well-being; it requires positive financial behaviour."
    - "Financial technology must be combined with good financial behaviour to be effective."
    - "Self-control impacts financial well-being through its influence on financial behaviour."
  limits:
    - "Survey sample is restricted to young adults aged 18-29 only."
    - "Study uses a subjective measure of financial well-being."
    - "Sampling method focused on youth organisations, which may not represent all young adults."
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The paper was found directly relevant to the Behavioral Profiling & Classification domain, with high relevance to topic 5.A (Financial Behavioral Profiles) and medium relevance to 5.C (Classification Approaches), as it uses SEM to model and validate financial behaviour's mediating role. It also provides supporting evidence for the Filipino Cultural Context domain, specifically topic 1.A, 1.B, and 1.C, by studying the financial structure and behaviour of Malaysian young adults, a comparable demographic. The paper's findings on the importance of financial literacy, socialisation, and self-control offer contextual insights for Expense Categorization (3.B) and Budget Recommendation (7.A) by highlighting the behaviours that lead to good financial management. Topics related to algorithm-specific areas like forecasting (6.A, 6.B), anomaly detection (8.A), or system evaluation (12.A) were rejected as the paper does not address computational methods. The overall relevance is high for informing Odin's core design around behavioural intervention and user profiling.
limitations:
  - "Sample restricted to ages 18-29, limiting generalisability to broader adult population."
  - "Subjective measure of financial well-being was used."
  - "Multi-stage random sampling may not have captured all socio-economic backgrounds."
  - "Cross-sectional design does not establish causality over time [unacknowledged]."
  - "Relies on self-reported data, which may be subject to social desirability bias [unacknowledged]."
remember_this:
  - "Financial behaviour is the strongest predictor of financial well-being."
  - "Financial literacy and self-control do not directly improve well-being."
  - "Fintech is only beneficial when paired with positive financial behaviour."
  - "Financial behaviour mediates the effect of socialisation and literacy."
  - "The model explains 61% of the variance in financial well-being."
```
---

## Paper 13: Mendoza et al_summarized.md

**Source File:** `Mendoza et al_summarized.md`

```yaml
paper_id: b9c0c8e3-2c9b-5e8d-9a1b-8c6f4e3a2d7e
designation: local
title: Big Five Personality Traits and Financial Literacy: Effect on Risk Tolerance of Filipino Investors from Higher Education Institutions in Metro Manila
authors: Mendoza, D. M.; Padernal, A. M. G.; Pante, E. M. S.; Magbata, E. V. S.; Mandigma, M. B. S.
year: 2023
venue: Review of Integrative Business and Economics Research
odin_topics:
  - 1.C
  - 5.A
  - 5.B
  - 5.C
tldr: Extraversion, openness, neuroticism, and financial literacy positively influence risk tolerance among Filipino investors, while agreeableness and conscientiousness do not.
problem_and_motivation: Understanding the factors that influence investor risk tolerance is critical for financial decision-making, yet the combined effect of personality traits and financial literacy on Filipino investors remains underexplored. This gap hinders the development of tailored financial advice and educational programs in the Philippine context.
approach:
  - Surveyed 320 students and faculty from Metro Manila higher education institutions using a four-point Likert scale.
  - Measured risk tolerance, Big Five personality traits, and financial literacy via adapted and modified questionnaires.
  - Employed multiple regression analysis to determine the influence of independent variables on risk tolerance.
  - Used snowball sampling to reach participants who invest at least PHP 1,000 in stocks, bonds, or cryptocurrency.
  - Controlled for age and monthly family income in a subsequent regression model.
findings:
  - Extraversion, openness to experience, and neuroticism significantly and positively influence risk tolerance.
  - Financial literacy has a significant positive influence on risk tolerance, with the highest standardized coefficient (Beta = 0.504).
  - Agreeableness and conscientiousness do not have a significant influence on risk tolerance.
  - num: The regression model with personality traits and financial literacy explains 43.6% of the variance in risk tolerance (R² = 0.436).
  - num: Including age and income as control variables increases the explained variance to 45.1% (R² = 0.451).
  - Monthly family income has a significant negative influence on risk tolerance when controls are added.
  - Age is not a significant predictor of risk tolerance in the model with controls.
  - The study provides empirical evidence from a Filipino sample, a demographic often underrepresented in behavioral finance research.
  - The findings support the Prospect Theory by showing differential risk attitudes based on personal factors.
key_figures_tables:
  - Table 1: Cronbach's Alpha values for Big Five (.913), Financial Literacy (.918), and Risk Tolerance (.881) → All constructs have high internal consistency.
  - Table 2: Demographic profile of respondents → Majority are female (68.75%), aged 18-25 (92.81%), and students (89.06%).
  - Table 3: Descriptive statistics → Openness has the highest mean (3.18) among personality traits, indicating high agreement.
  - Table 4: Multiple regression results → Extraversion, openness, neuroticism, and financial literacy are significant predictors of risk tolerance.
  - Table 5: Regression with controls → Income negatively influences risk tolerance; age is insignificant.
key_equations:
  - equation: Risk Tolerance = 0.882 + 0.091E + 0.086O + 0.089N + 0.474FL
    explanation: Predicts risk tolerance from significant personality traits and financial literacy.
definitions:
  - term: Risk Tolerance
    definition: The maximum uncertainty an investor is willing to accept before making a financial decision.
  - term: Financial Literacy
    definition: Knowledge and ability to manage personal finances effectively.
  - term: Big Five Personality Traits
    definition: Five broad domains of personality: openness, conscientiousness, extraversion, agreeableness, and neuroticism.
critical_citations:
  - "[Pak & Mahmood, 2015] — Foundational for personality trait measurement in this context."
  - "[Hamza & Arif, 2019] — Basis for financial literacy questionnaire used."
  - "[Ainia & Lutfi, 2019] — Source of risk tolerance scale adapted for this study."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly examines financial behavior (risk tolerance) of Filipino investors.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Links personality traits to financial risk tolerance, a key behavioral profile.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: Provides empirical basis for initial user profiling using personality and literacy.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Demonstrates regression analysis to classify/explain risk tolerance based on predictors.
  contribution: This paper provides a validated model linking personality traits and financial literacy to risk tolerance, directly informing Odin's user profiling module for Filipino young professionals. The significant influence of extraversion, openness, neuroticism, and financial literacy on risk tolerance offers a foundation for building behavioral profiles. The finding that agreeableness and conscientiousness are non-significant can refine feature selection for classification algorithms. The negative influence of income on risk tolerance, when controlled for, adds a layer of socioeconomic nuance to user modeling. Overall, the study's empirical framework and localized data directly support the design of Odin's behavioral assessment and personalization features.
  directly_justifies:
    - Odin's behavioral profiling module can use extraversion, openness, neuroticism, and financial literacy scores to estimate user risk tolerance.
    - Financial literacy is a crucial predictor of risk behavior and should be a core component of user onboarding assessment.
    - The non-significance of agreeableness and conscientiousness suggests these traits may be deprioritized in Odin's initial risk tolerance models.
    - The negative influence of income on risk tolerance, after accounting for other factors, indicates a complex relationship to be incorporated into user models.
    - The study's use of a Filipino sample provides culturally relevant data for calibrating Odin's algorithms for the target demographic.
  limits:
    - The sample is limited to students and faculty, not fully representing all Filipino investor groups.
    - Data was collected online, which may introduce selection bias.
    - The cross-sectional design cannot establish causation between personality/literacy and risk tolerance.
    - Reliance on self-reported measures may be subject to social desirability bias.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The domain "Behavioral Profiling & Classification" was flagged as directly relevant, leading to the selection of codes 5.A (high), 5.B (medium), and 5.C (medium) because the paper empirically establishes personality and literacy as predictors of risk tolerance, which is a core behavioral profile. The domain "Filipino Cultural Context" was considered but only code 1.C (Financial Behavior) was selected as high relevance due to the focus on Filipino investor behavior. Other domains such as "Spending Forecasting" (6.A, 6.B), "Budget Recommendation" (7.A-D), "Anomaly Detection" (8.A-C), "Mobile-First Design" (9.A, 9.B), "Data Privacy" (10.A, 10.B), and "System Evaluation" (12.A-C) were rejected as the paper does not address these algorithmic or design aspects. The domain "Existing Systems & Gaps" (4.A, 4.B) was rejected because the paper does not review existing systems. The domain "User Retention & Engagement" (11.A, 11.B) was rejected. The domain "Savings & Debt Management" (13.A-C) was rejected. The paper's overall relevance to Odin is moderate, providing foundational knowledge for user profiling but lacking direct application to Odin's core algorithmic functions.
limitations:
  - Sample demographics skew young and female, limiting generalizability to all Filipino investors. [unacknowledged]
  - Causality cannot be inferred due to the correlational design.
  - The study did not control for other potential confounding variables like financial experience or risk perception.
  - The use of a convenience sample (snowball) may introduce bias.
  - Generalizing findings to other economic or political contexts may not be valid.
remember_this:
  - Financial literacy has the strongest positive influence on risk tolerance.
  - Extraversion, openness, and neuroticism significantly increase risk tolerance.
  - Agreeableness and conscientiousness do not significantly affect risk tolerance.
  - num: Personality traits and literacy explain 43.6% of risk tolerance variance.
  - Monthly family income negatively affects risk tolerance when controlled for.
```
---

## Paper 14: Wang Y._summarized.md

**Source File:** `Wang Y._summarized.md`

```yaml
paper_id: a8f5f167-0d6e-5f6a-8b1d-4e7b2c3d9e8f
designation: international-algorithm-specific
title: New developments in sequential change point detection for time series and spatio-temporal analysis
authors: Wang, Y.
year: 2023
venue: Worcester Polytechnic Institute
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
  - 3.A
  - 4.A
  - 5.A
  - 7.A
tldr: Develops ensemble non-parametric, Bayesian hierarchical, and Bayesian online spatio-temporal frameworks for sequential change point detection in financial durations and public health surveillance data.
problem_and_motivation: Abrupt aberrations in stochastic systems often result from external factors of interest but monitoring complex streaming data requires efficient methods. Existing approaches either assume independence or Gaussian properties, limiting applicability to modern high-dimensional, interdependent data. There is a need for innovative methodologies that can handle time-dependence and spatio-temporal interdependence for timely detection.
approach:
  - Proposes an ensemble penalized estimating function (E-PEF) method for online structural break detection in financial durations using log ACD models.
  - Develops a Bayesian hierarchical framework (BVAR(1)-LCM) with bivariate temporal and latent level-correlated effects for multivariate count time series using INLA.
  - Introduces BOSTON-PUPA, an iterative sequential outbreak detection procedure with prior updating and p-value adaptation for spatio-temporal count data using a generalized Poisson model.
  - Utilizes block bootstrap resampling and Mahalanobis distance thresholds to handle non-Gaussian detector statistics and spillover effects.
  - Employs Integrated Nested Laplace Approximation (INLA) for fast, scalable Bayesian inference on latent Gaussian models with sparse precision matrices.
findings:
  - num: E-PEF method controls type I error under 5% and achieves detection probabilities exceeding 80% within short delays after structural breaks.
  - num: BVAR(1)-LCM demonstrates superior computational efficiency, with INLA being over ten times faster than STAN while maintaining comparable parameter recovery and prediction accuracy.
  - num: BOSTON-PUPA achieves up to 75% sensitivity at SNR=1.25 and near 100% at SNR=2, with controlled false detection rates below 5% for most regions.
  - num: Prior Updating with discounting factor 0.25 improves parameter recovery rates by 5-10% compared to cumulative fitting.
  - The overdispersion parameter in GPD models serves as an effective global aberration indicator for outbreak detection.
key_figures_tables:
  - Figure 4: Detection probability over monitoring horizon → E-PEF controls false detection and spikes power after true break.
  - Figure 11: Estimated temporal correlation ρωωω across sectors → Strong positive correlation (>0.75) justifies bivariate AR modeling.
  - Figure 19: Aggregated performance vs SNR → P-value Adaptation significantly improves Sensitivity and Global Error.
  - Table 12: Model comparison percentages → BVRW(1)-LCM favored in 88-90% of datasets for out-of-sample prediction.
  - Table 20: Detection frequencies by location → HMP and CCT methods show better false control in less populated areas.
key_equations:
  - equation: "GGG_{M_2}(k) = (G_{M_2,1}(k), ..., G_{M_2,d}(k))'"
    explanation: Standardized PEF detector statistic for break detection.
  - equation: "\\eta_{j,st} = \\log\\lambda_{j,st} = ZZZ_j \\beta\\beta\\beta_j + \\gamma_{j,t} + \\alpha_{j,st}"
    explanation: BVAR(1)-LCM link function for Poisson lognormal count model.
  - equation: "\\Pr(Y_{s,t}=y|\\theta_{s,t},\\lambda) = \\frac{\\theta_{s,t}(\\theta_{s,t}+\\lambda y)^{y-1}}{y!}\\exp(-(\\theta_{s,t}+\\lambda y))"
    explanation: Generalized Poisson distribution mass function for surveillance counts.
  - equation: "Q_{s,T+k} = Q_{s,T+k-1} + g(p^*_{s,T+k})"
    explanation: Cumulative detector statistic for combined p-value methods.
definitions:
  - term: E-PEF
    definition: Ensemble Penalized Estimating Function, a non-parametric online change point detection method.
  - term: INLA
    definition: Integrated Nested Laplace Approximation, a fast Bayesian inference method for latent Gaussian models.
  - term: GMRF
    definition: Gaussian Markov Random Field, a finite-dimensional random vector with a sparse precision matrix.
  - term: BVAR(1)-LCM
    definition: Bivariate AR(1) model with Latent Level Correlation for multivariate count time series.
  - term: BOSTON-PUPA
    definition: Bayesian Online Spatio-Temporal Outbreak Detection with Prior Updating and P-value Adaptation.
  - term: HMP
    definition: Harmonic Mean P-value, a method for combining dependent p-values.
  - term: CCT
    definition: Cauchy Combination Test, a method for combining dependent p-values.
  - term: SNR
    definition: Signal-to-Noise Ratio, a measure of outbreak magnitude relative to baseline variability.
  - term: MAE
    definition: Mean Absolute Error, a measure of prediction accuracy.
critical_citations:
  - "[Engle and Russell, 1998] — Foundation for ACD duration models."
  - "[Rue et al., 2009] — Introduced INLA for fast Bayesian inference."
  - "[Page, 1954] — Developed CUSUM, basis for sequential change detection."
  - "[Berkes et al., 2004] — Quasi-likelihood approach for sequential change detection."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Develops forecasting algorithms for sequential financial duration and count data.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Proposes E-PEF and BVAR(1)-LCM for forecasting and detecting changes in financial time series.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Outbreak detection framework provides methods for detecting anomalies in spatio-temporal count data.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Discusses CUSUM, Bayesian HMM, and combined p-value methods applicable to spending data anomalies.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Evaluates detection performance using sensitivity, specificity, and error metrics.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Compares INLA vs MCMC for parameter recovery and prediction accuracy.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Count data modeling with risk levels is analogous to categorizing transaction types.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews traditional methods (SPC, ARIMA) and their limitations, informing system design.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Behavioral changes in durations and counts relate to spending behavior profiling.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: General forecasting and anomaly detection concepts are foundational for budgeting.
  contribution: "The E-PEF method can directly inform Odin's anomaly detection module (8.B) by providing a non-parametric, online approach for detecting spending pattern changes. The BVAR(1)-LCM framework supports Odin's expense categorization (3.A) by modeling correlated transaction types. The BOSTON-PUPA procedure offers a robust template for Odin's forecasting (6.A) and anomaly detection (8.A) modules, especially for handling spatio-temporal dependencies. The comprehensive evaluation methodology (12.A, 12.B) provides metrics for assessing Odin's algorithmic performance. The INLA implementation demonstrates how Odin can achieve scalable Bayesian inference for complex models."
  directly_justifies:
    - "Online change point detection can be achieved via ensemble non-parametric methods without distributional assumptions."
    - "Latent correlation models effectively capture dependencies between multiple financial time series."
    - "Bayesian hierarchical models with INLA provide fast, scalable inference for spatio-temporal count data."
    - "Prior updating techniques improve model stability and inference quality in streaming data contexts."
    - "Combined p-value methods like HMP and CCT control false detection rates under arbitrary dependency."
  limits:
    - "E-PEF method's monitoring horizon is finite, requiring resetting for long-term surveillance."
    - "BVAR(1)-LCM assumes linearity in the log link and may not capture extreme non-linearities."
    - "BOSTON-PUPA's performance degrades in regions with very small populations due to inflated false positives."
    - "The framework relies on user-defined thresholds for SNR and aberration indicators."
    - "Real-time applicability depends on computational resources, though INLA mitigates this concern."
  mapping_rationale: "A systematic scan across all 12 functional domains and associated topic codes was performed. Domains flagged as relevant include Predictive Modeling (6.A, 6.B), Anomaly Detection (8.A, 8.B), and System Evaluation (12.A, 12.B) due to the paper's direct development of forecasting and detection algorithms. Expense Categorization (3.A) and Existing Systems (4.A) received medium relevance as the paper models categorical transaction data and reviews traditional methods. Behavioral Profiling (5.A) and Budgeting (7.A) were deemed contextual, as the paper provides general predictive techniques but does not directly address user behavior or budget recommendations. Domains related to Filipino cultural context (2.A-D), Mobile-First Design (9.A-B), Data Privacy (10.A-B), User Retention (11.A-B), Savings (13.A-C), and Classification (5.B-C) were rejected as they were not addressed. Borderline cases include temporal patterns (2.B) which are implicitly modeled but not culturally specific, and user-defined constraints (3.C) which are not discussed. Overall, the paper provides strong methodological contributions for anomaly detection and forecasting modules within Odin but lacks direct focus on user-centric design or Filipino-specific financial practices."
limitations:
  - "E-PEF assumes stationarity in the training period, which may not hold for volatile financial data. [unacknowledged]"
  - "BVAR(1)-LCM's performance relies on correct specification of the precision matrix for latent effects. [unacknowledged]"
  - "BOSTON-PUPA's false detection control in small populations requires further investigation. [acknowledged]"
  - "Computational time for INLA can be irregular depending on initial values and model complexity. [acknowledged]"
  - "The framework does not address multiple change points or resetting mechanisms. [unacknowledged]"
  - "Model selection for combined p-value methods may require domain-specific tuning. [unacknowledged]"
remember_this:
  - "E-PEF achieves robust structural break detection without distributional assumptions on innovations."
  - "INLA provides over tenfold speedup compared to MCMC for multivariate count time series."
  - "BOSTON-PUPA controls false detections at 5% while achieving 75-100% sensitivity for outbreaks."
  - "Latent correlation between risk-level counts consistently exceeds 0.75 across financial sectors."
  - "Generalized Poisson overdispersion parameter serves as a reliable global outbreak indicator."
```
---

## Paper 15: Kontopoulou et al_summarized.md

**Source File:** `Kontopoulou et al_summarized.md`

```yaml
paper_id: "10.3390/fi15080255"
designation: "international"
title: "A Review of ARIMA vs. Machine Learning Approaches for Time Series Forecasting in Data Driven Networks"
authors: "Kontopoulou, V.I.; Panagopoulos, A.D.; Kakkos, I.; Matsopoulos, G.K."
year: 2023
venue: "Future Internet"
odin_topics:
  - "6.A"
  - "6.B"
  - "8.A"
  - "8.B"
  - "12.A"
  - "12.B"
tldr: "Reviews comparisons of ARIMA, machine learning, and hybrid models for time series forecasting across finance, health, weather, utilities, and networks, finding ML generally outperforms ARIMA but with notable exceptions and hybrid models best."
problem_and_motivation: "The scientific literature lacks a comprehensive comparison of ARIMA and machine learning methods for time series forecasting across diverse applications. There is uncertainty about which approach is superior and under what conditions, hindering informed model selection. This review addresses this gap by systematically comparing performance across multiple domains."
approach:
  - "Conducted a systematic literature review of studies explicitly comparing ARIMA, machine learning, and hybrid models for time series forecasting."
  - "Organized selected papers by model category (SVM, decision trees, deep learning) and application domain (finance, health, weather, utilities, networks)."
  - "Extracted performance metrics (RMSE, MAPE, MAE, etc.) from each study for quantitative comparison."
  - "Analyzed conditions under which ARIMA outperforms ML, such as small datasets, linear patterns, and specific seasonality."
  - "Evaluated hybrid models that combine ARIMA and ML, which consistently improve forecasting accuracy."
findings:
  - "Machine learning models generally outperform ARIMA in forecasting accuracy across most application domains."
  - "num: Hybrid ARIMA-NARNN reduced RMSE by 35.3% compared to ARIMA alone in COVID-19 case prediction."
  - "ARIMA is superior when data is linear, small, or has strong seasonality with limited range."
  - "Deep learning models require larger datasets to achieve their advantage over ARIMA."
  - "Decision tree-based models like XGBoost often beat ARIMA in competitions and infectious disease forecasting."
  - "num: In Bitcoin price forecasting, ARIMA achieved MAPE of 2.76% vs LSTM 3.97% in one study, showing ARIMA can be competitive."
key_figures_tables:
  - "Table 2: Summary of ARIMA vs SVM studies → SVM generally better but ARIMA better in drought forecasting."
  - "Table 3: ARIMA vs decision tree models → XGBoost often outperforms ARIMA, but ARIMA can be more practical for long-term forecasts."
  - "Table 4: ARIMA vs deep learning → LSTM usually superior, but ARIMA wins for small, linear, or seasonal datasets."
  - "Table 5: Hybrid models → consistently outperform individual ARIMA and ML models."
key_equations:
  - equation: "MSE = (1/N) ∑ (y_t - ŷ_t)^2"
    explanation: "Mean squared error for forecast accuracy."
  - equation: "MAPE = (1/N) ∑ |(y_t - ŷ_t)/y_t|"
    explanation: "Mean absolute percentage error."
  - equation: "ARIMA(p,d,q): ∇^d x_t = c + ∑ φ_i ∇^d x_{t-i} + ∑ θ_i ε_{t-i}"
    explanation: "General ARIMA model with autoregressive and moving average terms."
definitions:
  - term: "ARIMA"
    definition: "AutoRegressive Integrated Moving Average, a statistical model for time series forecasting."
  - term: "SVM"
    definition: "Support Vector Machine, a supervised learning model used for classification and regression."
  - term: "LSTM"
    definition: "Long Short-Term Memory, a recurrent neural network architecture for sequential data."
  - term: "XGBoost"
    definition: "Extreme Gradient Boosting, an optimized gradient boosting decision tree algorithm."
  - term: "SARIMA"
    definition: "Seasonal ARIMA, an extension of ARIMA that handles seasonality."
critical_citations:
  - "[Box et al., 2015] — Standard reference for ARIMA models."
  - "[Zhang, 2003] — Foundational hybrid ARIMA-NN model."
  - "[Makridakis et al., 2018] — Raises concerns about ML forecasting methods."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Directly compares forecasting algorithms applicable to spending prediction."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Reviews ARIMA, LSTM, XGBoost, and hybrids for time series, relevant to spending sequences."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Includes studies on anomaly detection (e.g., IoT) and discusses outlier handling in time series."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "medium"
      justification: "Discusses ARIMA and ML for identifying anomalies; provides comparative performance insights."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Summarizes evaluation metrics (RMSE, MAPE) and comparison methodologies."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Provides empirical comparisons of forecasting algorithms, useful for module evaluation."
  contribution: "The review directly informs Odin's selection of forecasting algorithms for spending prediction (6.A) and anomaly detection (8.B) by summarizing comparative performance across diverse datasets. It highlights that hybrid ARIMA-ML models consistently outperform single approaches, suggesting Odin should consider hybrid architectures for budget recommendation. The findings on ARIMA's effectiveness for small or linear datasets guide cold-start strategies and baseline selection. The evaluation metrics discussed (RMSE, MAPE) can be adopted for Odin's system evaluation framework (12.A). The paper also provides evidence that deep learning requires large data, influencing Odin's data acquisition and training plans."
  directly_justifies:
    - "Machine learning models generally outperform ARIMA for nonlinear time series forecasting."
    - "Hybrid ARIMA-ML models improve prediction accuracy over individual models."
    - "ARIMA remains competitive for short-term, linear, or small-sample forecasting tasks."
    - "Evaluation metrics like RMSE and MAPE are standard for assessing forecasting accuracy."
  limits:
    - "The review is based on a selected sample of studies, not exhaustive meta-analysis."
    - "It does not provide new empirical results or algorithm development."
    - "Findings may be influenced by publication bias favoring positive ML results."
  mapping_rationale: "A systematic scan across all 12 functional domains and their canonical topic codes was performed. The domains of Spending Forecasting (6) and Anomaly Detection (8) were flagged as highly relevant because the paper directly compares time series forecasting algorithms applicable to these Odin modules. System Evaluation (12) was also flagged as medium relevance due to the extensive discussion of evaluation metrics and comparison methodologies. The domains of Filipino Cultural Context, Expense Categorization, Existing Systems, Behavioral Profiling, Budget Recommendation (except indirectly), Mobile-First Design, Data Privacy, User Retention, and Savings/Debt Management were rejected as they are not addressed by the paper's focus on algorithmic forecasting. Borderline cases: Budget Recommendation (7.B) could be informed by forecasting accuracy but the paper does not discuss budget allocation; assigned low relevance and not included in odin_topics due to lack of direct evidence. Anomaly Detection (8.A, 8.B) was included as medium because the paper includes some anomaly detection studies, but it is not the main focus. Overall, the paper provides strong empirical evidence for choosing forecasting algorithms, making it highly relevant to Odin's predictive modules."
limitations:
  - "The review does not meta-analyze results across studies, limiting quantitative synthesis."
  - "Selection criteria may exclude relevant studies not explicitly comparing ARIMA and ML."
  - "The paper does not discuss computational costs in detail, which is critical for mobile deployment. [unacknowledged]"
  - "The applicability of findings to personal finance data is inferred, not directly tested. [unacknowledged]"
remember_this:
  - "Machine learning models generally beat ARIMA but ARIMA wins on small or linear data."
  - "Hybrid ARIMA-ML models consistently outperform individual models in forecasting."
  - "num: Hybrid ARIMA-NARNN reduced RMSE by 35.3% over ARIMA alone."
  - "Deep learning requires larger datasets to outperform statistical methods."
  - "Evaluation metrics like RMSE and MAPE are standard for forecasting comparison."
```
---

## Paper 16: Bai_summarized.md

**Source File:** `Bai_summarized.md`

```yaml
paper_id: "10.1371/journal.pone.0294466"
designation: "international"
title: "Impact of financial literacy, mental budgeting and self control on financial wellbeing: Mediating impact of investment decision making"
authors: "Bai, R."
year: 2023
venue: "PLOS ONE"
odin_topics:
  - "1.C"
  - "3.A"
  - "5.A"
  - "7.A"
tldr: "Financial literacy, mental budgeting, and self-control positively influence financial wellbeing, partially mediated by investment decision-making behavior."
problem_and_motivation: "Financial stress is a public health concern, and understanding cognitive factors that improve financial wellbeing is critical. While financial literacy is known to help, the roles of mental budgeting and self-control, and the mediating mechanism of investment decisions, remain underexplored. This study investigates these relationships to inform interventions."
approach:
  - "Convenience sample of 449 Chinese university students (55% male, 60% business majors)."
  - "Used validated scales for financial wellbeing, financial literacy, mental budgeting, self-control, and investment decision-making behavior."
  - "Employed PLS-SEM to test direct and indirect effects via path analysis and mediation."
  - "Assessed measurement model via factor loadings, composite reliability, and AVE; structural model via path coefficients."
findings:
  - "num: Financial literacy has a direct positive effect on financial wellbeing (β=0.299, p<0.001)."
  - "num: Mental budgeting has a direct positive effect (β=0.102, p<0.001)."
  - "num: Self-control has a direct positive effect (β=0.182, p<0.001)."
  - "num: Investment decision-making partially mediates the effects of all three independent variables (indirect effects: 0.017, 0.016, 0.019)."
  - "All constructs met reliability and validity criteria (CR>0.70, AVE>0.50)."
key_figures_tables:
  - "Table 1: Demographic distribution of sample → Majority male and business majors."
  - "Table 2: Factor loadings, CR, alpha, AVE → All constructs are reliable and valid."
  - "Table 3: Path coefficients and significance → All direct effects are significant except DMB→FWB at p=0.059."
  - "Table 4: Mediation analysis results → Partial mediation for all three paths."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Financial literacy"
    definition: "Knowledge of financial concepts and ability to make informed financial decisions."
  - term: "Mental budgeting"
    definition: "Cognitive process of categorizing and tracking income and expenses mentally."
  - term: "Self-control"
    definition: "Ability to regulate impulses and behavior to achieve long-term goals."
  - term: "Investment decision-making"
    definition: "Process of making choices about financial investments influenced by various factors."
  - term: "Financial wellbeing"
    definition: "Subjective evaluation of one's present and future financial situation."
  - term: "PLS-SEM"
    definition: "Partial Least Squares Structural Equation Modeling, a variance-based SEM technique."
critical_citations:
  - "[Thaler, 1999] — introduced mental accounting theory."
  - "[Shefrin & Thaler, 1988] — proposed behavioral life-cycle hypothesis."
  - "[Tangney et al., 2004] — developed Brief Self-Control Scale."
  - "[Baron & Kenny, 1986] — established mediation testing framework."
relevance:
  topics:
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "low"
      justification: "Paper studies general financial behavior but not Filipino-specific."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "contextual"
      justification: "Mental budgeting involves categorization but is not a system framework."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "low"
      justification: "Identifies self-control and financial literacy as behavioral traits relevant to profiling."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "medium"
      justification: "Directly examines mental budgeting as a strategy influencing wellbeing."
  contribution: "This paper supports Odin's budgeting module by emphasizing mental budgeting as a behavior that improves financial wellbeing. It informs user profiling by linking self-control and financial literacy to financial outcomes. The mediating role of investment decisions suggests that Odin's decision support features could enhance user trust and engagement. Additionally, the findings justify incorporating financial education content within the app to boost literacy and self-control."
  directly_justifies:
    - "Mental budgeting practice is positively associated with financial wellbeing."
    - "Self-control is a significant predictor of financial security and wellbeing."
    - "Investment decision-making mediates the effect of cognitive factors on financial wellbeing."
    - "Financial literacy directly improves financial wellbeing."
  limits:
    - "Sample of Chinese university students limits generalizability to Filipino young professionals. [unacknowledged]"
    - "Cross-sectional design prevents causal inference (acknowledged)."
    - "Self-reported measures may introduce social desirability bias (acknowledged)."
  mapping_rationale: "A systematic scan of all 12 functional domains and associated topic codes was performed. The domains of Financial Behavior, Expense Categorization, Behavioral Profiling, and Budgeting Strategies were flagged as relevant. Specifically, topic 1.C (Financial Behavior) was assigned low relevance because the paper studies general financial behavior but not Filipino context. Topic 3.A (Expense Categorization) was contextual because mental budgeting is a cognitive categorization process, not a system framework. Topic 5.A (Behavioral Profiles) received low relevance as it identifies traits (self-control, literacy) but does not classify profiles. Topic 7.A (Budgeting Strategies) was medium relevance because mental budgeting is a core budgeting strategy directly studied. Domains such as Forecasting, Anomaly Detection, Mobile Design, Privacy, and Retention were rejected as the paper contains no content on those topics. Overall, the paper provides background behavioral insights but limited direct applicability to Odin's algorithmic modules."
limitations:
  - "Sample comprised solely of Chinese university students, limiting generalizability."
  - "Cross-sectional design restricts causal inferences."
  - "Reliance on self-reported measures may introduce response biases."
  - "The study does not examine cultural or contextual factors relevant to Filipino users. [unacknowledged]"
remember_this:
  - "Mental budgeting directly improves financial wellbeing (β=0.102)."
  - "Self-control is a strong predictor of financial security (β=0.182)."
  - "Investment decisions partially mediate cognitive effects on wellbeing."
  - "Financial literacy has the largest direct effect on wellbeing (β=0.299)."
```
---

## Paper 17: Maceda et al_summarized.md

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

## Paper 18: Gotehus_summarized.md

**Source File:** `Gotehus_summarized.md`

```yaml
paper_id: 10.1080/13229400.2022.2074869
designation: international
title: "'She's Like Family': transnational Filipino families, voluntary kin and the circulation of care"
authors: Gotehus, A.
year: 2023
venue: Journal of Family Studies
odin_topics:
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 4.A
  - 5.A
  - 11.A
  - 11.B
tldr: Filipino nurses in Norway engage in multidirectional care circulation, relying on remittances, siblings, and voluntary kin to bridge gaps created by distance and welfare regime differences.
problem_and_motivation: Transnational caregiving research often focuses on unidirectional care drain and remittances, overlooking the complexity of multidirectional care and the role of non-kin. There is a gap in understanding how migration and welfare regimes in both origin and destination countries shape care needs, capacity, and the emergence of voluntary kin networks.
approach:
  - Multi-sited qualitative fieldwork conducted in Oslo, Norway and five regions in the Philippines between April 2017 and April 2019.
  - In-depth interviews with 22 Filipino nurses (18 women, 4 men) in Norway, aged 27-48, who arrived between 2000 and 2013 via various visa types.
  - Follow-up interviews and observations with four families of the nurses in the Philippines to capture perspectives from both sides of the transnational family.
  - Applied the care circulation framework to analyze multidirectional, multigenerational, and multidimensional care exchanges across borders.
  - Thematic analysis was used to identify patterns in how migration policies and welfare regimes affect caregiving practices and the formation of voluntary kin.
findings:
  - "num: Nurses reduced remittances from 7,000 NOK to half after having children in Norway."
  - Differences in welfare regimes (Norwegian service state vs. limited Philippine social protection) create asymmetric care needs and capacities, with migrants providing financial care for medical needs in the Philippines.
  - Caregiving roles are dynamic and fluctuate over the life and migration cycles, with migrants often being both givers and receivers of care simultaneously.
  - Norwegian immigration regulations, which prioritize nuclear family reunification, effectively prevent aging parents from migrating, forcing proximate care to be managed by siblings and hired helpers in the Philippines.
  - Migrant nurses create and rely on voluntary kin relationships within Filipino communities in Norway for emotional, practical, and childcare support, filling gaps left by absent family networks.
  - Filipino churches in Norway serve as crucial arenas for forming voluntary kin relationships and providing material, informational, and emotional support to newly arrived migrants.
key_figures_tables:
  - "None."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Care circulation"
    definition: "The reciprocal, multidirectional, and asymmetrical exchange of care that fluctuates over the life course within transnational family networks."
  - term: "Voluntary kin"
    definition: "Individuals to whom migrants are not formally related but with whom they construct familial relationships to provide emotional and practical care."
  - term: "Utang na loob"
    definition: "A Filipino cultural concept of a debt of gratitude, often expressed through reciprocal care and support for parents."
critical_citations:
  - "[Baldassar & Merla, 2014] — Defines care circulation framework used in the study."
  - "[Yeates, 2004] — Critiques care chain approach for overlooking extended family forms."
  - "[Merla et al., 2020] — Highlights how migration regimes shape proximate care access."
relevance:
  topics:
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "medium"
      justification: "Illustrates how nurses manage and adjust remittances based on life stages in the Philippines and Norway."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "high"
      justification: "Provides rich empirical data on utang na loob and its role in motivating remittances and care obligations."
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "contextual"
      justification: "Describes how remittances and care provision change with family life cycles and emergencies, but not explicitly seasonal spending."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "low"
      justification: "Mentions visits and family gatherings as occasions for care exchange, but spending cycles are not the focus."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Provides background on the Filipino family as an informal social protection and finance system."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "The paper profiles migrants as remittance-senders and family supporters, demonstrating key behavioral drivers for personal finance."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "medium"
      justification: "Highlights how emotional and practical support from networks (kin and voluntary) drives financial engagement and well-being."
    - code: "11.B"
      name: "Retention Mechanisms and Engagement Design"
      relevance: "low"
      justification: "Suggests that social support networks are key to retention in migration, but not directly applicable to app retention."
  contribution: "This paper directly informs Odin's design by establishing the cultural and structural context for Filipino financial behavior. It justifies the need for Odin to account for remittance obligations and utang na loob as key drivers of spending. It highlights the importance of social support networks, suggesting features that could facilitate financial goal-sharing or group support. It validates the need for Odin to understand family-centric financial decisions, which is crucial for behavioral profiling. Finally, it underscores the impact of welfare regimes, implying Odin must adapt to users in contexts with weak public social safety nets."
  directly_justifies:
    - "Remittances are a primary financial behavior for Filipino migrant professionals."
    - "Spending adjustments are driven by family needs and life events, not just personal consumption."
    - "Social networks (voluntary kin) provide financial and emotional support, impacting financial decisions."
    - "Welfare system differences create asymmetric care needs affecting spending patterns."
  limits:
    - "Study focuses on nurses in Norway, a specific and relatively privileged migrant group, limiting generalizability to all Filipino YPs."
    - "Small sample size for family interviews in the Philippines (n=4) limits depth of understanding on the receiving side."
    - "Focus on care circulation does not provide quantitative data on spending patterns or financial behaviors."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was conducted. The paper was flagged as relevant for the 'Filipino Cultural Context' domain, specifically codes 2.A (high) and 2.D (low), and 1.C (medium) for financial behavior. It was also relevant for 'Behavioral Profiling' (5.A, medium) by showing social motivations. 'User Retention' (11.A/B) is touched upon contextually via social support. The domains of 'Expense Categorization', 'Forecasting', 'Budget Recommendation', 'Anomaly Detection', and 'Mobile-First Design' were considered and rejected, as the paper does not address algorithmic or system-level design. The domains of 'Existing Systems' (4.A) and 'Data Privacy' were deemed contextual. The paper is highly relevant for understanding the cultural and social drivers of financial behavior, which are foundational for Odin."
limitations:
  - "Study focuses on a specific migrant group (nurses) with relatively stable employment and legal status in Norway."
  - "Data collection primarily occurred in Norway, with limited family interviews in the Philippines."
  - "Does not quantify the financial impact of remittances or voluntary kin support on budgets."
  - "Limited discussion on how users might engage with a digital tool alongside their existing practices. [unacknowledged]"
  - "No longitudinal data to assess how care patterns evolve over longer periods. [unacknowledged]"
remember_this:
  - "Filipino nurses reduce remittances by half after having children in Norway."
  - "Migrants simultaneously give and receive care from family and voluntary kin."
  - "Voluntary kin networks fill gaps left by absent family and inadequate welfare states."
  - "Norwegian policy allows only nine-month visits for parents, preventing their migration."
  - "Siblings in the Philippines perform proximate care for aging parents in exchange for childcare."
```
---

## Paper 19: Krstev et al_summarized.md

**Source File:** `Krstev et al_summarized.md`

```yaml
paper_id: 10.17559/TV-20220430111309
designation: international-algorithm-specific
title: An Overview of Forecasting Methods for Monthly Electricity Consumption
authors: Krstev, S.; Forcan, J.; Krneta, D.
year: 2023
venue: Technical Gazette
odin_topics:
  - 6.A
  - 6.B
  - 12.A
  - 12.B
  - 12.C
  - 2.B
  - 5.A
  - 5.B
tldr: Compares twelve statistical and machine learning forecasting models for monthly electricity consumption, finding neural network autoregression achieves the highest accuracy.
problem_and_motivation: Accurate mid-term electricity load forecasting is crucial for utility operations and deregulated markets, yet research on this time horizon is limited compared to short-term forecasting. The challenge is compounded by the influence of both consumption habits and external random factors.
approach:
  - Data is monthly electricity consumption (kWh) from 60,000 metering points in Bosnia and Herzegovina from 2000 to 2020.
  - Classical time series models include seasonal naïve, ARIMA, ETS, and structural models with Kalman filter.
  - Machine learning methods include linear regression, elastic net, KNN, random forest, XGBM, and SVM with lm and PCA feature selection.
  - A neural network autoregression (NNAR) with lagged values and a three-layer architecture is also applied.
  - Model performance is evaluated using Mean Absolute Percentage Error (MAPE) on a hold-out test set of the last 15 months.
findings:
  - "num: Neural network autoregression (NNAR) achieves the lowest MAPE of 2.67%."
  - "num: Classical time series methods (ETS at 3.28%, ARIMA at 3.36%) outperform most machine learning models."
  - "num: The best machine learning model, PCA+KNN, achieves a MAPE of 4.38%."
  - "num: The seasonal naïve method serves as a baseline with a MAPE of 4.16%."
  - Classical methods are more accurate than machine learning methods for this small sample size dataset.
key_figures_tables:
  - "Figure 4: Forecasts from classical models → ETS shows best fit visually."
  - "Figure 5 & 6: Forecasts from ML with lm and PCA → PCA feature selection slightly improves performance."
  - "Figure 7: Forecast from NNAR → Predictions closely follow the test data pattern."
  - "Figure 8: MAPE comparison bar chart → NNAR has the lowest MAPE, followed by ETS."
  - "Table 2: MAPE for ML methods → PCA+KNN is the best ML approach at 4.38%."
  - "Table 3: Monthly absolute relative errors → NNAR is most accurate for the majority of test months."
key_equations:
  - equation: "y'_{T+h|T} = y_{T+h-m(k+1)}"
    explanation: "Seasonal naive forecast equals value from previous season."
  - equation: "MAPE = 100/n * Σ(|(y_t - y'_t) / y_t|)"
    explanation: "Mean absolute percentage error as accuracy measure."
definitions:
  - term: "MTLF"
    definition: "Mid-term load forecast, for a time horizon from two weeks to two years."
  - term: "MAPE"
    definition: "Mean absolute percentage error, a measure of prediction accuracy."
  - term: "DSO"
    definition: "Distribution System Operator, the utility company managing the distribution network."
  - term: "NNAR"
    definition: "Neural network autoregression, a model using lagged values as inputs to a neural network."
critical_citations:
  - "[Makridakis et al., 2018] — Classical methods outperform ML for univariate series."
  - "[Cerqueira et al., 2019] — Sample size influences performance of statistical vs ML methods."
  - "[Hyndman & Athanasopoulos, 2014] — Source for time series forecasting methodologies."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: "Compares multiple predictive models for a sequential time series forecasting problem."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: "Evaluates classical and ML forecasting algorithms on monthly consumption data, a parallel to spending."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: "Provides a structured evaluation framework using MAPE and out-of-sample testing."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: "Provides a benchmark of algorithmic performance for forecasting modules."
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: low
      justification: "The comparative methodology for selecting a forecasting model can inform budget recommendation evaluation."
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: "The electricity consumption data demonstrates strong seasonality, analogous to spending cycles."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: low
      justification: "Briefly touches on consumption habits as a factor but does not profile users."
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: low
      justification: "The challenge of limited data for MTLF is analogous to the cold-start problem in profiling."
  contribution: "This paper provides a direct comparison of twelve forecasting models, which can guide the selection of a predictive engine for Odin's spending forecast module. The finding that neural networks excel with sufficient data supports the choice of algorithm for a core Odin feature. The rigorous evaluation using MAPE and a rolling forecast origin offers a template for testing Odin's own forecasting accuracy. The conclusion that data quality and pre-processing are critical validates the emphasis on data cleaning in Odin's pipeline."
  directly_justifies:
    - "Neural network autoregression is a high-accuracy method for monthly time series forecasting."
    - "Classical time series models like ETS are strong baselines for data with seasonal patterns."
    - "A rolling forecasting origin is a robust evaluation technique for time series models."
    - "For small datasets, classical methods can outperform more complex machine learning approaches."
  limits:
    - "The paper focuses on a single dataset (electricity) and may not generalize to all spending patterns."
    - "It does not address the integration of forecasting into a broader personal finance management system."
    - "The study does not explore real-time or user-interactive forecasting, which is key for Odin."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper's primary relevance is to the 'Spending Forecasting' domain (6.A, 6.B), as its core contribution is comparing forecasting methods for monthly data. It also provides a methodological framework for 'System Evaluation' (12.A, 12.B, 12.C), specifically for comparing algorithmic performance. The paper's mention of seasonal patterns (2.B) and consumption habits (5.A, 5.B) is contextual but does not provide actionable insights for user profiling. Domains like 'Expense Categorization' (3.A), 'Budget Recommendation' (7.A), and 'Anomaly Detection' (8.A) were considered but rejected as the paper focuses solely on forecasting, not on categorization, optimization, or anomaly identification. The paper's overall relevance is high for the forecasting module, medium for evaluation methodologies, and low or contextual for other domains. This contributes primarily to the technical design and evaluation strategy for Odin's predictive components."
limitations:
  - "Small sample size (228 training points) limits generalizability to data-rich environments. [unacknowledged]"
  - "The study does not compare hybrid models, which current research suggests may improve accuracy."
  - "Data is limited to a single geographic region and type of consumption, which may not represent PFMS spending data."
  - "The paper does not address computational cost, a key constraint for mobile-first systems."
  - "It does not evaluate the explainability of the models, crucial for user trust in PFMS."
remember_this:
  - "NNAR achieved the best forecasting accuracy with a MAPE of 2.67%."
  - "Classical time series models like ETS are robust baselines for seasonal data."
  - "Model performance is highly dependent on data quality and pre-processing."
  - "For small datasets, simpler models can outperform complex neural networks."
  - "Seasonal patterns are a critical component of monthly consumption forecasting."
```
---

## Paper 20: Hoang & Wiegratz_summarized.md

**Source File:** `Hoang & Wiegratz_summarized.md`

```yaml
paper_id: 10.1111/eufm.12408
designation: international-algorithm-specific
title: Machine learning methods in finance: Recent applications and prospects
authors: Hoang, D.; Wiegratz, K.
year: 2023
venue: European Financial Management
odin_topics:
  - 4.A
  - 5.A
  - 6.A
  - 6.B
  - 7.B
  - 8.A
  - 10.A
  - 10.B
  - 12.A
tldr: A survey and taxonomy of machine learning applications in finance, classifying uses into constructing superior measures, reducing prediction errors, and extending econometric toolsets.
problem_and_motivation: Despite the rapid growth of ML publications in finance, there is a lack of clarity on how and where to apply ML to solve research problems. This paper aims to provide a systematic taxonomy and guide for financial economists to leverage ML effectively.
approach:
  - Provides a high-level primer on supervised and unsupervised learning and their differences from traditional econometrics.
  - Develops a taxonomy of ML applications in finance based on methodological purpose: superior/novel measures, prediction error reduction, and econometric tool extension.
  - Conducts a bibliometric analysis of 346 ML papers published in 45 major finance journals from 2010 to 2021.
  - Analyzes publication success by research field, journal rank, and application type using distribution and citation data.
  - Illustrates ML benefits with a real estate price prediction application using over four million German listings and comparing OLS to various ML methods.
findings:
  - num: The number of ML publications in finance grew almost elevenfold by 2021 compared to the 2010-2017 average.
  - ML publications account for approximately 3%-4% of publications in top finance journals in 2021, similar to lower-ranked journals.
  - Most ML publications (69.1%) are for economic prediction problems, while superior/novel measures are more common in higher-ranked journals.
  - Applications of ML to construct superior and novel measures receive 10.2 more citations on average than general finance publications.
  - The field of corporate finance/governance shows particularly high potential for ML-based superior/novel measures, receiving 24.2 more citations.
  - num: In a real estate pricing application, boosted regression trees achieved an out-of-sample R² of 77%, compared to 40% for OLS.
key_figures_tables:
  - Figure 1: Comparison of OLS and ML real estate price predictions → ML predictions are much closer to actual prices, especially at the upper end.
  - Figure 4: Prediction performance and average pricing errors of OLS vs. ML methods → Boosted regression trees outperform OLS, reducing average pricing error from 44% to 27%.
  - Table 5: Yearly number and relative share of ML publications in major finance journals by journal rank → ML share grew to 3-4% by 2021 across all ranks.
  - Table 7: Distribution of ML applications by application type and journal rank → Superior/novel measures are more prevalent in A+ journals (56.4%) than in B-ranked journals (18.4%).
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: Supervised Learning
    definition: ML method that makes predictions from labelled data.
  - term: Unsupervised Learning
    definition: ML method that infers data structure from unlabelled data.
  - term: LASSO
    definition: Regularized linear regression that shrinks coefficients and can drive irrelevant ones to zero.
  - term: Boosted Regression Trees
    definition: An ensemble method that iteratively builds trees, focusing on observations previous trees predicted poorly.
  - term: Causal Forests
    definition: A tree-based ML method used to estimate heterogeneous treatment effects.
critical_citations:
  - "[Mullainathan and Spiess, 2017] — Identifies prediction as main ML use in economics."
  - "[Athey and Imbens, 2019] — Reviews ML methods from an econometric perspective."
  - "[Gu et al., 2020] — Predicts stock returns using various ML methods."
  - "[Fuster et al., 2022] — Finds ML can increase bias in credit decisions."
  - "[Bianchi et al., 2021] — Predicts bond risk premiums using machine learning."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Provides a broad overview of ML applications, including those in credit risk and fraud detection relevant to PFMS.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Discusses limitations of traditional econometrics and highlights ML's potential to overcome them.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: low
      justification: Mentions ML for investor profiling and detecting credit risk, but not specifically for behavioral profiling.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly reviews ML methods for forecasting asset prices, volatility, and credit risk, applicable to spending forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Reviews algorithms like LSTM and boosted trees that are directly applicable to forecasting sequential financial data.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: contextual
      justification: Provides a general framework for prediction problems, which is foundational for budget recommendation.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Discusses ML for fraud detection and outlier detection, relevant to anomaly detection modules.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Briefly mentions algorithmic bias in credit decisions, related to trust and fairness, but not privacy.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: Mentions interpretability as a limitation of ML, which is key for user trust.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Uses bibliometric analysis to evaluate publication success and provides methods for comparing model performance.
  contribution: "This paper provides a foundational taxonomy for categorizing ML applications, which can be directly applied to evaluate Odin's algorithmic modules. The bibliometric analysis offers insights into the publication success of different ML approaches, guiding the selection of methods that are both effective and credible. The real estate pricing example demonstrates a concrete methodology for evaluating predictive models against traditional baselines, a process essential for Odin's own model validation."
  directly_justifies:
    - "Machine learning methods can reduce prediction error in economic prediction problems by leveraging high-dimensional data."
    - "ML applications are most successful in top journals when used to construct superior and novel measures, not just for prediction."
    - "The field of corporate finance and governance shows the highest potential for ML-based superior measures."
    - "Regularized linear methods like LASSO and tree-based methods like boosted regression trees are state-of-the-art for numerical data."
    - "Unsupervised learning methods such as clustering can be used to infer data structure in financial applications."
  limits:
    - "The survey's classification is based on a manual review and may not capture all nuances of ML applications."
    - "The bibliometric analysis is limited to papers published up to 2021 and may not reflect the most current trends."
    - "The real estate pricing example is illustrative and not generalizable to all prediction problems."
    - "The paper does not provide a practical implementation guide for applying ML in a production system."
  mapping_rationale: "A systematic scan across all 12 functional domains was performed. Domains related to predictive modeling (6.A, 6.B) and evaluation (12.A) were flagged as high relevance due to the paper's direct focus on forecasting algorithms and performance comparison. Domains concerning existing systems (4.A, 4.B) and anomaly detection (8.A) were assigned medium relevance because the paper reviews the landscape of ML applications and discusses fraud detection. Behavioral profiling (5.A), budget recommendation (7.B), data privacy (10.A), and user trust (10.B) were deemed low or contextual as the paper mentions them but does not provide design-specific insights for a PFMS. Domains like Filipino cultural context, expense categorization, and user retention (1.A-3.C, 11.A-11.B) were considered and rejected as the paper does not address these topics. The paper is overall highly relevant to Odin's design as it establishes the state-of-the-art in ML methods and their evaluation, providing a methodological blueprint for Odin's predictive and classification modules."
limitations:
  - "The illustrative application of ML to real estate pricing is conducted on German data and may not generalize to other markets or contexts."
  - "The paper's taxonomy is based on a manual review, which introduces some subjectivity." [unacknowledged]
  - "The study does not provide a detailed cost-benefit analysis of implementing ML versus traditional methods in a production setting." [unacknowledged]
  - "The paper acknowledges the low interpretability of complex ML models as a limitation."
  - "The paper acknowledges that ML generally requires large datasets and high computational costs."
remember_this:
  - "ML publications in finance grew almost elevenfold from 2010-2017 to 2021."
  - "Superior and novel measures are the most successful ML application type in top finance journals."
  - "Boosted regression trees achieved 77% R² in real estate pricing, far exceeding OLS at 40%."
  - "ML offers benefits over traditional methods for high-dimensional prediction problems."
  - "Algorithmic bias is a potential concern when ML influences credit or lending decisions."
```
---

## Paper 21: Lu, Yingzhou et al_summarized.md

**Source File:** `Lu, Yingzhou et al_summarized.md`

```yaml
paper_id: 10.48550/arXiv.2302.04062
designation: international
title: "Machine Learning for Synthetic Data Generation: A Review"
authors: "Lu, Y.; Chen, L.; Zhang, Y.; Shen, M.; Wang, H.; Wang, X.; van Rechem, C.; Fu, T.; Wei, W."
year: 2023
venue: "Journal of Latex Class Files"
odin_topics:
  - "5.A"
  - "5.B"
  - "5.C"
  - "8.A"
  - "8.B"
  - "8.C"
  - "10.A"
  - "10.B"
  - "12.B"
tldr: "Reviews machine learning methods for generating synthetic data, addressing issues of data scarcity, privacy, and quality across multiple domains."
problem_and_motivation: "Machine learning faces significant hurdles including poor data quality, insufficient data points leading to under-fitting, and difficulties in data access due to privacy and safety concerns. These challenges hinder the development and deployment of robust models across various sectors. Synthetic data generation emerges as a promising solution to enable data sharing and utilization in ways real-world data cannot facilitate."
approach:
  - "Conducted a systematic review of existing studies that employ machine learning models for synthetic data generation."
  - "Surveyed applications across computer vision, speech, NLP, healthcare, and business domains."
  - "Explored various deep generative models including VAEs, GANs, reinforcement learning, and diffusion models."
  - "Addressed the crucial aspects of privacy and fairness concerns related to synthetic data generation."
  - "Identified current technological advancements, limitations, and outlined potential avenues for future research."
findings:
  - "Synthetic data has been proven effective across a diverse array of tasks and domains, including healthcare, finance, and NLP."
  - "Generative models like GANs, VAEs, and diffusion models are central to producing high-quality synthetic data."
  - "num: MedGAN demonstrated close-to-real-time performance in generating realistic patient records and classification tasks."
  - "Synthetic data from parametric 3D face models achieved comparable accuracy to real data for landmark localization and face parsing."
  - "Differentially private synthetic data generation does not introduce unfairness into the data generation process but can amplify existing majority subgroup influence."
approach:
  - "Surveyed privacy-preserving techniques including differential privacy, local differential privacy, and plausible deniability applied to generative models."
  - "Explored fairness in synthetic data through preprocessing, in-processing, and post-processing methods."
  - "Outlined evaluation strategies such as human evaluation, statistical difference, TSTR, and application-specific metrics."
findings:
  - "Privacy-preserving synthetic data generation methods often involve adding noise to gradients or using frameworks like PATE-GAN."
  - "Differential privacy significantly reduces the quality of generated images from GANs, decreasing utility in downstream tasks."
  - "Fairness-aware data synthesis methods leverage preprocessing and in-processing techniques to mitigate bias inherited from real-world data."
  - "Challenges persist in the evaluation of synthetic data, including a lack of standard tools and the difference between synthetic and real data."
  - "num: Deduplicating training data that appears multiple times mitigates privacy risks in language models, as sequences appearing more often are more likely to be generated."
key_figures_tables:
  - "Figure 1: Diagram of synthetic data generation process → Shows how generative models learn from real data to produce synthetic data."
  - "Table I: Summarization of representative works in synthetic data generation → Lists key papers, their applications, and generative AI methods used."
  - "Table II: Comparison of all the generative AI methods from different aspects → Compares LM, SSL, VAE, GAN, diffusion, and RL models."
  - "Table III: Summarization of privacy prevention strategies in synthetic data generation → Categorizes works by their privacy-enhancing technique and generative AI."
key_equations:
  - equation: "N p(X) = p([x_1,...,x_N]) = ∏_{i=1}^{N} p(x_i|x_1,...,x_{i-1})"
    explanation: "Decomposes sequence probability into conditional probabilities for language models."
  - equation: "min_G max_D L(D,G) = E_{x∼training set}[log D(x)] + E_{z∼p(z)}[log(1 - D(G(z)))]"
    explanation: "Minimax objective function for training Generative Adversarial Networks."
  - equation: "q(x_t|x_{t-1}) = N(x_t; sqrt(1-β_t) x_{t-1}, β_t I)"
    explanation: "Forward diffusion process gradually adds Gaussian noise to data."
  - equation: "L_{VLB} = KL[q(x_T|x_0)||p_θ(x_T)] + Σ_{t=2}^{T} KL[q(x_{t-1}|x_t, x_0)||p_θ(x_{t-1}|x_t)] - E_q[log p_θ(x_0|x_1)]"
    explanation: "Variational lower bound objective for training diffusion models."
definitions:
  - term: "Synthetic Data"
    definition: "Artificially annotated information generated by computer algorithms or simulations, often used when real data is unavailable or private."
  - term: "GAN (Generative Adversarial Network)"
    definition: "A generative model with a generator and discriminator trained adversarially to produce realistic data."
  - term: "VAE (Variational Autoencoder)"
    definition: "A generative model that learns a continuous latent representation of data to generate new samples."
  - term: "Differential Privacy"
    definition: "A framework that provides mathematical guarantees on privacy by adding noise to data or model parameters."
  - term: "TSTR (Training on Synthetic, Testing on Real)"
    definition: "An evaluation strategy where a model is trained on synthetic data and tested on real data to assess utility."
critical_citations:
  - "[Goodfellow et al., 2014] — Introduced the foundational GAN architecture for generative modeling."
  - "[Choi et al., 2017] — Proposed MedGAN for generating realistic synthetic patient records using GANs."
  - "[Dwork et al., 2014] — Established the algorithmic foundations of differential privacy for data protection."
  - "[Sellam et al., 2020] — Developed BLEURT, a metric for text generation, using synthetic data for pre-training."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "contextual"
      justification: "Discusses behavioral classification methods but not specifically for financial profiles."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "contextual"
      justification: "Addresses the general cold-start problem in ML, which is relevant to profile initialization."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "contextual"
      justification: "Reviews classification approaches in general ML, potentially applicable to financial profiles."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews generative models that can be applied to detect anomalies in spending data."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "medium"
      justification: "Discusses algorithms for detecting outliers which are applicable to anomaly detection in finance."
    - code: "8.C"
      name: "Cold‑Start Baseline Strategies for Anomaly Detection"
      relevance: "medium"
      justification: "Discusses strategies for generating baselines, relevant for cold-start anomaly detection in finance."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "Extensively covers differential privacy and privacy-preserving techniques for sensitive data."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "high"
      justification: "Addresses how privacy-preserving synthetic data can build trust by enabling secure data sharing."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Discusses evaluation strategies like TSTR, applicable to evaluating forecasting or classification modules."
  contribution: "This comprehensive review of synthetic data generation provides Odin with foundational knowledge for several core modules. For anomaly detection, it surveys algorithms and generative models that can be adapted to identify irregularities in user spending patterns. On privacy and user trust, it details differential privacy techniques crucial for handling sensitive financial data and building user confidence. The evaluation strategies discussed, such as TSTR, are directly applicable to assessing the performance of Odin's predictive models."
  directly_justifies:
    - "Differential privacy techniques can be integrated into generative models to protect user financial data."
    - "Generative adversarial networks are effective for generating realistic synthetic data for training predictive models."
    - "Evaluating models on synthetic data and testing on real data (TSTR) is a robust validation strategy."
  limits:
    - "The review is general and does not provide domain-specific implementations for personal finance."
    - "Practical deployment challenges of synthetic data for highly dynamic and irregular spending patterns are not addressed."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed for the entire paper. Domains related to Filipino cultural context (2.A-D) and expense categorization (3.A-C) were flagged as contextual only, as the paper does not address cultural financial practices or category design. The domains on existing systems (4.A-B) are not relevant as the paper does not review PFMS specifically. For behavioral profiling (5.A-C), the paper's review of ML-based profiling methods is considered contextual, as it lacks specific application to financial behaviors. The domains of spending forecasting (6.A-B) and budget recommendation (7.A-D) are considered low relevance, as the paper focuses on general generation rather than forecasting or optimization. The anomaly detection domain (8.A-C) is assigned medium relevance because the paper reviews outlier detection methods and generative models for identifying anomalies. Mobile-first design (9.A-B) is considered not applicable. Data privacy (10.A) and user trust (10.B) are assigned high relevance due to the extensive coverage of differential privacy and privacy-preserving synthetic data generation. System evaluation (12.A-C) is considered medium relevance due to the discussion on evaluation strategies like TSTR. Savings and debt management (13.A-C) is not relevant. Overall, the paper is highly relevant to Odin's privacy and anomaly detection modules, providing foundational knowledge and specific techniques."
limitations:
  - "Evaluation metrics for synthetic data are not standardized, particularly in specialized domains like healthcare. [unacknowledged]"
  - "The review does not provide a comparative analysis of the generative models specifically for time-series financial data. [unacknowledged]"
  - "There is a lack of discussion on the computational cost and scalability of these models for mobile-first applications. [unacknowledged]"
  - "The practical implementation details for deploying these models in production systems are not covered. [unacknowledged]"
remember_this:
  - "Synthetic data generation addresses data scarcity and privacy issues in machine learning."
  - "GANs, VAEs, and diffusion models are key for generating realistic synthetic data."
  - "Differential privacy is a central technique for protecting sensitive data in generation."
  - "num: MedGAN achieved close-to-real-time performance for generating synthetic patient records."
  - "Evaluating synthetic data quality remains a significant challenge."
---

## Paper 22: Eigenschink et al_summarized.md

**Source File:** `Eigenschink et al_summarized.md`

```yaml
paper_id: 10.1109/ACCESS.2023.3275134
designation: international-algorithm-specific
title: Deep Generative Models for Synthetic Data: A Survey
authors: Eigenschink, P.; Reutterer, T.; Vamosi, S.; Vamosi, R.; Sun, C.; Kalcher, K.
year: 2023
venue: IEEE Access
odin_topics:
  - 12.A
  - 12.B
  - 12.C
tldr: A survey proposing a data-driven evaluation framework for deep generative models for synthetic sequential data using five criteria: representativeness, novelty, realism, diversity, and coherence.
problem_and_motivation: Evaluating deep generative models for sequential data is challenging due to data heterogeneity and conflicting requirements across domains. Existing metrics are often domain- or model-specific, making cross-domain comparison difficult. A common, abstract evaluation framework is needed to guide research and enable knowledge transfer between fields.
approach:
  - The paper proposes a domain- and model-agnostic evaluation framework based on five high-level criteria relative to the original data: representativeness, novelty, realism, diversity, and coherence.
  - It critically reviews applications of deep generative models across NLP, speech/audio, video, healthcare, and mobility domains.
  - The review analyzes models based on their architectures (GANs, VAEs, RNNs/LSTMs, CNNs) and the metrics used for evaluation.
  - The paper evaluates each domain against the proposed criteria, identifying which criteria are prioritized and how they are measured.
  - It summarizes the prevalence of different architectural elements across domains and provides overview tables of representative contributions and evaluation metrics.
findings:
  - num: Realism and coherence are more important for synthetic data in natural language, speech, and audio processing tasks.
  - num: Novelty and representativeness are more important for healthcare and mobility data.
  - Representativeness is often measured with statistical metrics like MMD or NLL, while realism is frequently assessed by human judgement.
  - Novelty is often evaluated using privacy tests, particularly in sensitive domains like healthcare.
  - GANs are the most frequently used architecture, often in combination with CNNs or RNNs to ensure coherent generation of sequential data.
key_figures_tables:
  - Figure 1: Data heterogeneity in sequential data by cardinality and dimensionality → Shows why a common framework is needed.
  - Figure 2: High-level structure of the article → Outlines the survey's organization and objectives.
  - Figure 3: Illustration of synthetic data scoring high/low on the five criteria → Clarifies the meaning of each evaluation criterion.
  - Figure 4: Prevalence of architectural elements in five domains → Highlights the popularity of GANs, CNNs, and RNNs.
  - Table 6: Overview of domains and metrics for the five criteria → Summarizes domain-specific priorities and measurement approaches.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Representativeness
    definition: The ability of a model to capture population-level properties of the original data.
  - term: Novelty
    definition: The degree to which synthetic data-points are entirely new and not closely resembling any original data-point.
  - term: Realism
    definition: The indistinguishability of an individual synthetic data-point from an original one.
  - term: Diversity
    definition: The uniqueness of data-points within the synthetic dataset.
  - term: Coherence
    definition: The internal consistency and logical structure of a single synthetic data-point.
  - term: GAN
    definition: Generative Adversarial Network.
  - term: VAE
    definition: Variational Autoencoder.
  - term: RNN
    definition: Recurrent Neural Network.
  - term: LSTM
    definition: Long Short-Term Memory network.
  - term: CNN
    definition: Convolutional Neural Network.
  - term: NLL
    definition: Negative Log-Likelihood.
  - term: MMD
    definition: Maximum Mean Discrepancy.
  - term: IS
    definition: Inception Score.
  - term: BLEU
    definition: Bilingual Evaluation Understudy.
  - term: EHR
    definition: Electronic Health Record.
  - term: TSTR
    definition: Train on Synthetic, Test on Real.
  - term: TRTS
    definition: Train on Real, Test on Synthetic.
critical_citations:
  - "[Borji, 2019] — Reviews pros and cons of GAN evaluation measures."
  - "[Theis et al., 2016] — Discusses limitations of general-purpose metrics like NLL."
  - "[Goodfellow et al., 2016] — Foundational reference for deep learning architectures."
relevance:
  topics:
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Proposes a general framework for evaluating generative models, directly applicable to assessing Odin's recommendation modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides a structured approach and criteria (representativeness, novelty, realism, diversity, coherence) for evaluating algorithmic modules in Odin.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: The framework's criteria can be adapted to evaluate the quality of budget recommendations (e.g., realism, diversity of plans).
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: The concept of generating synthetic user data could be used for profile testing, but the paper doesn't directly address behavioral profiling.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: contextual
      justification: The review covers models for sequential data, which is relevant to forecasting, but focuses on generation rather than prediction.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: contextual
      justification: The discussion of privacy and synthetic data in healthcare could be analogous to handling sensitive financial data for savings goals.
  contribution: |
    This paper provides Odin with a formal, high-level evaluation framework for any algorithmic module that generates or recommends data, such as budget plans, spending forecasts, or savings allocations. The criteria of representativeness and realism can be used to assess how well a recommended budget reflects a user's actual historical spending patterns. The criteria of novelty and coherence are essential for ensuring that generated recommendations are not just copies of past behavior but are internally consistent and provide new, actionable insights.
  directly_justifies:
    - "The proposed framework enables systematic comparison of different generative models for sequential data, such as those used for spending forecasting."
    - "Evaluation of representativeness and realism in synthetic data corresponds to validating the accuracy and plausibility of generated spending forecasts or budget plans."
    - "Assessing novelty and coherence in synthetic data is analogous to evaluating the actionability and internal logic of new budget recommendations."
  limits:
    - The framework is conceptual and does not provide specific implementation guidelines or benchmarks for Odin's modules.
    - The survey focuses on generative models for creating synthetic data, not on recommendation systems or optimization algorithms directly.
    - The criteria are high-level and may require further operationalization for application to PFMS-specific tasks like budget allocation.
  mapping_rationale: |
    A systematic scan of all 12 functional domains was conducted. The paper's primary contribution is a methodological framework for evaluating generative models, which maps directly to the "System Evaluation" domain (12.A, 12.B, 12.C) with high relevance. The criteria and concepts discussed are also contextually relevant to domains involving modeling user behavior (5.A) and making predictions (6.A), as the paper focuses on sequential data generation which underpins many predictive and profiling techniques. However, the paper does not address the specific financial contexts of budgeting, savings, or expense categorization (e.g., 3.A, 7.A), nor does it cover user design, privacy, or engagement, as it is a purely methodological survey on algorithmic evaluation. Borderline cases like 5.A were considered because the evaluation of generated behavioral profiles is relevant, but the paper's core contribution remains in evaluation methodology. Therefore, the primary relevance is to the evaluation framework domain, with contextual ties to algorithm performance.
limitations:
  - "The survey does not provide a unified, prescriptive evaluation protocol."
  - "It focuses on unconditional generation, not conditional generation which is more common in applied systems. [unacknowledged]"
  - "The framework's criteria are abstract and may conflict, with no guidance on balancing them. [unacknowledged]"
  - "The review's domain coverage is limited to five areas, leaving out other potential applications. [unacknowledged]"
remember_this:
  - "Evaluate generative models using five criteria: representativeness, novelty, realism, diversity, and coherence."
  - "Realism and coherence are prioritized for NLP/audio; novelty and representativeness for healthcare/mobility."
  - "GANs, combined with CNNs and RNNs, are the most prevalent architecture for synthetic sequential data."
  - "The proposed framework offers a common basis for comparing models across different domains."
  - "Current evaluations show a trade-off between novelty and representativeness in privacy-sensitive domains."
---

## Paper 23: Alenazi & Sas_summarized.md

**Source File:** `Alenazi & Sas_summarized.md`

```yaml
paper_id: 10.14236/ewic/BCSHCI2023.1
designation: international
title: Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking
authors: Alenazi, M.; Sas, C.
year: 2023
venue: BCS HCI 2023
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 9.A
tldr: A functionality review of 45 budgeting apps reveals limited budgeting support and a lack of grounding in mental accounting theory.
problem_and_motivation: Prior HCI research on financial practices has focused on exploratory studies, showing limited use of digital tools. However, there is little understanding of how mobile budgeting apps actually support tracking and budgeting. This gap motivates a systematic evaluation of top-rated budgeting apps to identify their functionalities and limitations.
approach:
  - Searched Google Play and Apple Store using keywords budget, budgeting, and finance.
  - Identified 1335 apps, removing duplicates, non-free apps, and irrelevant ones.
  - Retained 45 top-rated apps with average rating ≥4.0 and ≥1000 reviews.
  - Performed expert evaluation of app functionalities using mental accounting theory as an analytical lens.
  - Iteratively identified and clarified key functionalities such as accounts, transactions, and budgets.
findings:
  - One third of top-rated budgeting apps do not support budgeting informed by money envelopes.
  - Only two apps explicitly mention money envelope systems in their descriptions.
  - Most apps use inconsistent terminology for accounts, drawn from banking or everyday practices.
  - All apps support tracking transactions, but only 26 support multiple budgets aligned with mental accounting.
  - Few apps support saving accounts (11) or automatic import from bank accounts (7).
key_figures_tables:
  - Figure 1: PRISMA diagram of app selection process → 45 apps selected from 1335 initial candidates.
  - Table 1: Main functionalities for funds and expenses → majority support basic tracking but not envelope budgeting.
  - Table 2: Transaction accounts and budget types → only 26 apps support multiple budgets.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Mental accounting
    definition: Behavioral economics theory where people partition money into mental accounts for specific purposes.
  - term: Money envelopes
    definition: Physical or digital representation of mental accounts for allocating budgets to expense categories.
  - term: Single budget
    definition: One main budget for all expenses, not categorized by expense type.
  - term: Multiple budgets
    definition: Separate budgets for each expense category, akin to money envelopes.
  - term: Transaction
    definition: Movement of money from a source to a destination, including income, expense, and transfer.
critical_citations:
  - "[Thaler, 1999] — Foundational theory for mental accounting and money envelopes."
  - "[Kaye et al., 2014] — Prior HCI work on analogue financial tools."
  - "[Snow and Vyas, 2015a] — Reports on limited digital tool use for budgeting."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Directly evaluates how apps categorize income and expenses.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: high
      justification: Identifies limitations in category support and subcategory options.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Provides a systematic review of top-rated budgeting app functionalities.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Highlights gaps such as lack of mental accounting and limited budgeting support.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Discusses budgeting as a cognitive process tied to actual behavior.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Reviews mobile app functionalities but focuses on features over UX principles.
  contribution: "This paper provides a systematic functionality review of budgeting apps, directly informing Odin's module for expense categorization by identifying gaps in existing category support. It contributes to Odin's understanding of existing systems by mapping current limitations and terminological inconsistencies. The review highlights the absence of mental accounting theory in most apps, justifying Odin's design of multiple budgets. It also offers design implications for improved budgeting support, which can guide Odin's user-defined allocation constraints. The findings directly support Odin's requirement for a clear differentiation between tracking and budgeting functionalities."
  directly_justifies:
    - "Budgeting apps lack theoretical grounding in mental accounting, limiting their effectiveness."
    - "Most apps do not support multiple budgets per expense category, a key feature for Odin."
    - "Inconsistent terminology for accounts and transactions creates user confusion."
    - "Automatic import from bank accounts is rare, indicating low integration with actual financial behavior."
    - "Transfer transactions without sufficient funds are often allowed, a design flaw to avoid."
  limits:
    - "The review is limited to top-rated apps, which may not represent the full range of available tools."
    - "The analysis is based on expert evaluation rather than user studies, so actual usage patterns are not captured."
    - "The findings are based on apps available in the UK market, which may not generalize to other regions."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was conducted. Domains flagged as relevant: Existing Systems & Gaps (topic 4.A, 4.B high), Expense Categorization (3.A, 3.B high), Behavioral Profiling (5.A medium), and Mobile-First Design (9.A medium). The paper directly addresses the landscape of existing PFMS and their limitations, making 4.A and 4.B highly relevant. Expense categorization is central to the findings, so 3.A and 3.B are also high. Behavioral profiling (5.A) is touched upon through the discussion of budgeting as a cognitive process, but not in depth, hence medium. Mobile-First Design (9.A) is relevant due to the review of mobile apps, but the focus is on functionality rather than design principles, so medium. Borderline cases: The paper touches on user-defined categories (3.C) but does not focus on constraints, so 3.C was rejected. Budget recommendation (7.A-7.D) and forecasting (6.A-6.B) are not addressed, so rejected. Anomaly detection (8.A-8.C), savings/debt (13.A-13.C), and evaluation (12.A-12.C) are not covered. Overall, the paper is highly relevant for understanding the state of budgeting app functionalities and their gaps, providing foundational knowledge for Odin's design."
limitations:
  - "The study only includes free apps, excluding paid apps that may offer advanced features."
  - "The analysis relies on expert evaluation, which may not capture user perceptions or actual behavior."
  - "The sample is limited to UK app stores, potentially missing region-specific tools or designs."
  - "The paper does not evaluate the effectiveness of budgeting features through user studies. [unacknowledged]"
  - "The review does not assess the accuracy or reliability of transaction tracking. [unacknowledged]"
remember_this:
  - "One third of top-rated apps do not support envelope-based budgeting."
  - "Only 26 out of 45 apps support multiple budgets for different expense categories."
  - "Most apps lack theoretical grounding in mental accounting theory."
  - "Inconsistent account terminology is a common usability issue in budgeting apps."
  - "Automatic bank integration is available in only 7 out of 45 apps."
```
---

## Paper 24: Alejandrino et al_summarized.md

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

## Paper 25: Zhang et al_summarized.md

**Source File:** `Zhang et al_summarized.md`

```yaml
paper_id: 10.14778/3632093.3632110
designation: international-algorithm-specific
title: An Experimental Evaluation of Anomaly Detection in Time Series
authors: Zhang, A.; Deng, S.; Cui, D.; Yuan, Y.; Wang, G.
year: 2023
venue: Proceedings of the VLDB Endowment
odin_topics:
  - 8.A
  - 8.B
  - 8.C
  - 12.A
  - 12.B
  - 6.A
tldr: A comprehensive experimental evaluation of 17 time-series anomaly detection algorithms, analyzing effectiveness, efficiency, and robustness across multiple factors.
problem_and_motivation: The diversity and complexity of time-series data, coupled with a lack of standardized comparative evaluations, make it difficult for users to select appropriate anomaly detection methods for real-world applications. This is especially critical in personal finance, where inaccurate anomaly detection can erode user trust.
approach:
  - Presents a taxonomy of anomaly detection methods based on data dimension, processing technique, and anomaly type, with six inner classes.
  - Conducts systematic intra- and inter-class comparisons of 17 state-of-the-art algorithms on real and synthetic datasets.
  - Evaluates algorithms using both point and range metrics, analyzing effectiveness, efficiency, and robustness to anomaly rates, data sizes, dimensions, patterns, and thresholds.
  - Tests algorithm performance under different application scenarios, including false positive/negative rates and early detection capabilities.
  - Provides a practical guide for selecting anomaly detection methods based on experimental findings.
findings:
  - "num: Online methods can be ten times slower than simple batch methods when the window size is large."
  - "num: The point-adjust method can inflate F-measure by an average of 27.0% for point datasets and 31.2% for subsequence datasets under point metrics."
  - "num: Using range metrics on subsequence datasets leads to a negative average promotion of -67.6% when using the point-adjust method."
  - Point methods can perform well for global subsequence anomalies with extreme values, potentially relaxing the need for length input.
  - No single algorithm is suitable for all cases; optimal selection depends on dataset characteristics and application requirements.
key_figures_tables:
  - "Figure 1: Taxonomy of anomaly detection algorithms based on three facets (data dimension, processing technique, anomaly type) → Provides a structured framework for method classification."
  - "Table 2: Properties of considered anomaly detection algorithms (algorithm, multi-dimensional, process, anomaly type, threshold, code, speedup) → Summarizes key characteristics and implementation details."
  - "Table 4: Accuracy over various datasets for point and subsequence methods → Shows that NETS performs best in many point cases, while PBAD and BeatGAN have better overall accuracy for subsequence anomalies."
  - "Figure 15: Varying thresholds on ECG and Uni-sub-g datasets → Demonstrates the robustness of NormA and IDK compared to other methods, with IDK showing the best overall performance."
  - "Figure 18: Practical guide for timeseries anomaly detection → Provides a decision flowchart for method selection based on anomaly type, dimensionality, and application needs."
key_equations:
  - equation: "Precision = TP / (TP + FP)"
    explanation: "Metric for point anomaly detection accuracy."
  - equation: "Recall = TP / (TP + FN)"
    explanation: "Metric for point anomaly detection completeness."
  - equation: "F-measure = 2 * Precision * Recall / (Precision + Recall)"
    explanation: "Harmonic mean of precision and recall."
definitions:
  - term: "Point Anomaly"
    definition: "An individual data point that deviates significantly from the majority of the data."
  - term: "Subsequence Anomaly"
    definition: "A consecutive set of data points that is inconsistent with the rest of the time series."
  - term: "Range Metric"
    definition: "An evaluation metric for subsequence anomalies that focuses on the overlap between predicted and true anomaly ranges."
  - term: "Point-adjust"
    definition: "A method that converts false negatives to true positives within an anomaly segment if any point in the segment is detected as anomalous."
critical_citations:
  - "[Tatbul et al., 2018] — Introduced range metrics for subsequence anomalies."
  - "[Lai et al., 2021] — Provides definitions and benchmarks for time series outlier detection."
  - "[Schmidl et al., 2022] — Comprehensive evaluation of anomaly detection methods."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly addresses anomaly detection in time series, a core module of Odin.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Evaluates 17 state-of-the-art algorithms, many applicable to spending data.
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: medium
      justification: Discusses threshold robustness and parameter search, relevant for cold-start scenarios.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides a systematic evaluation methodology applicable to Odin's modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Directly compares effectiveness, efficiency, and robustness of anomaly detection algorithms.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Many anomaly detection methods rely on prediction models, and the paper's findings on LSTM and GAN are relevant.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: The paper discusses seasonal anomalies in a general sense, but not specifically Filipino contexts.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Provides a landscape of TAD, but not PFMS specifically.
  contribution: "This paper provides an experimental framework and baseline comparisons that can directly inform the selection of anomaly detection algorithms for Odin's spending monitoring module. The findings on point-adjust method biases are critical for ensuring Odin does not overstate its detection accuracy. The practical guide (Figure 18) offers a decision-making tool for integrating a suitable algorithm, and the analysis of efficiency and robustness helps in balancing accuracy with mobile-first constraints. The paper's taxonomy and evaluation metrics can also be adopted for Odin's system evaluation to benchmark its anomaly detection performance against established methods."
  directly_justifies:
    - "The point-adjust method can inflate F-measure by an average of 27.0% for point datasets."
    - "Online methods can be ten times slower than simple batch methods when the window size is large."
    - "No single anomaly detection algorithm is suitable for all cases; optimal selection depends on data characteristics."
    - "NP performs best for global subsequence anomalies, while NormA is more robust to threshold settings."
    - "Using range metrics on subsequence anomalies leads to more reasonable and robust results than point metrics."
  limits:
    - "The study focuses on a specific set of algorithms and does not cover all possible anomaly detection techniques."
    - "The evaluation is primarily on synthetic and benchmark datasets, which may not fully capture the nuances of real-world Filipino spending data."
    - "The practical guide is based on current findings and may not be exhaustive for all future scenarios."
    - "The paper does not address the specific contextual and cultural factors relevant to Filipino young professionals."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains of Anomaly Detection (8) and System Evaluation (12) were flagged as highly relevant, with codes 8.A, 8.B, 8.C, 12.A, and 12.B assigned. The paper directly evaluates algorithms and provides a framework for assessing their performance, which is directly applicable to Odin's anomaly detection module. The code 6.A was also selected as medium relevance because many TAD methods use predictive models, and the paper's findings on deep learning architectures (LSTM, GAN) are relevant to forecasting. Borderline cases were considered: while the paper discusses seasonal anomalies (2.D), it is not specific to Filipino cultural contexts; the discussion of existing systems (4.A) is at a TAD level, not PFMS. Domains like Mobile-First Design (9), Data Privacy (10), and User Retention (11) were considered and rejected as the paper does not address these aspects. The overall relevance to Odin is high, as it provides a critical evaluation of a core algorithmic component for the PFMS."
limitations:
  - "The study does not consider the specific characteristics of Filipino financial data, such as high variability and unique cultural spending patterns."
  - "The parameter search is conducted per dataset, which may not be feasible in a real-time mobile-first application like Odin."
  - "The practical guide, while useful, requires expertise to interpret and adapt to specific application contexts. [unacknowledged]"
  - "The evaluation of deep learning methods did not compare their efficiency, which is a key constraint for mobile applications. [unacknowledged]"
  - "The study uses anomaly-free training sets, which may not be available in real-world scenarios for Odin. [unacknowledged]"
remember_this:
  - "No single anomaly detection algorithm fits all cases."
  - "Point-adjust methods can inflate reported accuracy by 27-31%."
  - "NETS is the most efficient point anomaly method."
  - "NP performs best for global subsequence anomalies."
  - "Range metrics are more robust than point metrics for subsequence anomalies."
```
---

## Paper 26: Thundiyil et al_summarized.md

**Source File:** `Thundiyil et al_summarized.md`

```yaml
paper_id: 10.48550/arXiv.2304.06183
designation: international
title: Transformer Architectures in Time Series Analysis: A Review
authors: Thundiyil, S.; Picone, J.; McKenzie, S.
year: 2023
venue: arXiv
odin_topics:
  - 3.A
  - 4.A
  - 5.C
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 9.A
  - 9.B
  - 12.A
  - 12.B
  - 12.C
  - 1.A
  - 1.B
  - 1.C
  - 2.B
tldr: A review of transformer-based architectures for time series analysis, highlighting their superior performance in capturing long-term dependencies for forecasting, classification, and anomaly detection.
problem_and_motivation: Traditional time series methods like ARIMA and LSTMs struggle to capture long-term dependencies critical for accurate forecasting and classification. The emergence of transformer architectures offers a powerful solution, but a comprehensive review of their variants and applications is needed to guide adoption. This paper fills that gap by synthesizing the state of the art in transformer-based time series modeling.
approach:
  - This is a comprehensive review paper that surveys and synthesizes existing literature on transformer architectures for time series analysis.
  - The review covers 11 transformer-based architectures, including LogTrans, TFT, Informer, Autoformer, and FEDformer.
  - It systematically compares traditional methods (ARIMA, LSTM) with modern transformer variants across healthcare, finance, and climate applications.
  - The analysis focuses on architectures addressing segmentation, forecasting, and classification challenges.
  - The paper provides a structured comparison of key features, application areas, and quantitative performance improvements.
findings:
  - num: Autoformer achieved a 38% averaged MSE reduction across six benchmark datasets compared to existing methods.
  - num: FEDformer delivered an overall 14.8% relative MSE reduction compared to Autoformer on six datasets.
  - num: Transformer-XL reduced perplexity from 20.5 to 18.3 on WikiText-103, demonstrating superior long-term dependency modeling.
  - num: Pyraformer decreased MSE by 24.8%, 28.9%, and 26.2% for prediction lengths of 168, 336, and 720 on the ETTh1 dataset.
  - num: W-Transformers achieved superior RMSE performance across multiple datasets, significantly outperforming WARIMA and LSTM models.
  - num: In the ETTm2 dataset, InParformer achieved an MSE of 0.260 and an MAE of 0.323 for a prediction length of 192, outperforming FEDformer.
  - num: On ImageNet, CrossFormer++-B achieved 84.2% accuracy, surpassing existing vision transformers.
  - num: TFT improved MAPE by 2% to 8% in district heating load forecasting during spring and fall seasons.
  - num: CrossFormer++ surpassed CrossFormer by at least 0.5% average precision (AP) on the COCO 2017 dataset.
  - Transformer architectures consistently outperform traditional RNN-based methods for modeling long-term temporal dependencies.
key_figures_tables:
  - Figure 1: Dow Jones performance from Jan 2023 to Feb 2024 → Illustrates trend and seasonality in financial time series.
  - Figure 2: Satellite images of glacier shrinkage from 1985 to 2021 → Demonstrates spatial context in time series data.
  - Figure 3: Recording of a 10-second EEG signal → Shows multichannel temporal and spatial dependencies.
  - Table 1: Comparison of traditional methods → Summarizes advantages and disadvantages of classical approaches.
  - Table 2: Comparison of modern approaches → Highlights strengths and weaknesses of contemporary methods.
  - Table 3: Ablation study of LogTrans framework → Shows incremental improvements from SeCo and ReSD modules.
  - Table 4: Comparison of W-Transformer with other architectures → Demonstrates superior RMSE and MAE across datasets.
  - Table 5: Summary of transformer architectures → Provides a comprehensive overview of models and their applications.
key_equations:
  - equation: R(τ) = E[(x(t) - μ)(x(t + τ) - μ)] / σ²
    explanation: Defines autocorrelation of time series at lag τ.
  - equation: Attention(Q,K,V) = softmax(QK^T / √d_k) V
    explanation: Core scaled dot-product attention mechanism.
  - equation: Multihead(Q,K,V) = Concat(head1,...,headh)W_O
    explanation: Multi-head attention concatenates multiple attention outputs.
definitions:
  - term: Autocorrelation
    definition: Correlation between a time series and a lagged version of itself.
  - term: Seasonality
    definition: Regular fluctuations at specific intervals like daily or yearly.
  - term: Stationarity
    definition: Statistical properties like mean and variance are constant over time.
  - term: Self-Attention
    definition: Mechanism assigning importance weights to different parts of an input sequence.
  - term: Transformer
    definition: Deep learning architecture using self-attention to process sequential data.
critical_citations:
  - "[Vaswani et al., 2017] — Introduced the original Transformer architecture with self-attention."
  - "[Zhou et al., 2021] — Proposed Informer with ProbSparse attention for efficient long-sequence forecasting."
  - "[Wu et al., 2022] — Developed Autoformer with autocorrelation mechanism for improved periodicity modeling."
  - "[Lim et al., 2019] — Introduced Temporal Fusion Transformer for interpretable multi-horizon forecasting."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Provides general context on time series applications in finance and healthcare relevant to YPs.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: contextual
      justification: Discusses time series analysis in financial domains indirectly relevant to financial structure.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: contextual
      justification: General background on forecasting and anomaly detection useful for understanding spending behavior.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: Review covers seasonality in time series, supporting modeling of cyclical spending patterns.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: low
      justification: General techniques for time series classification inform categorization but are not directly applied.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides context on traditional methods but not direct PFMS system analysis.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Classification methods like CNNs and SVMs are discussed, but not specific to financial profiling.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: This paper directly reviews and evaluates advanced forecasting models applicable to PFMS.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Detailed analysis of transformer-based algorithms specifically for time series forecasting.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Reviews anomaly detection methods applicable to identifying unusual spending patterns.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Discusses One-Class SVM and autoencoders, which are relevant for spending anomaly detection.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: Model efficiency considerations are relevant for mobile deployment but not explicitly discussed.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: contextual
      justification: Resource-constrained model discussions relate to mobile implementation constraints.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides comprehensive evaluation methodologies and metrics (MSE, MAE, MAPE).
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Offers detailed performance comparisons of transformer-based algorithm modules.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: high
      justification: Forecasting accuracy metrics and evaluation setups are directly transferable to budget recommendation evaluation.
  contribution: This review provides Odin with a comprehensive catalogue of state-of-the-art transformer architectures suitable for forecasting and anomaly detection modules. It establishes performance benchmarks for predictive modeling (6.A/6.B) and evaluation frameworks (12.A/12.B/12.C). The paper validates the choice of transformers over traditional methods for capturing long-term spending patterns and seasonal cycles (2.B). It also highlights key considerations for model selection (e.g., efficiency for mobile deployment, handling irregular data) that inform Odin's design decisions.
  directly_justifies:
    - "Transformer architectures significantly outperform RNNs and LSTMs for long-term time series forecasting tasks."
    - "Autoformer and FEDformer provide state-of-the-art accuracy with 38% and 14.8% MSE reductions, respectively."
    - "Attention mechanisms effectively capture seasonal and cyclical patterns in time series data."
    - "Temporal Fusion Transformer integrates static metadata and handles missing data, suitable for personal finance."
    - "Efficiency improvements (e.g., Informer, Pyraformer) enable deployment in resource-constrained environments."
  limits:
    - The review does not evaluate models specifically on personal finance spending data.
    - Most benchmarks focus on energy, traffic, and climate data, not financial transactions.
    - No discussion of cold-start problems or user-specific profile dynamics in forecasting.
    - The paper is a review and does not propose new algorithms or provide empirical results for PFMS contexts.
    - Focuses primarily on univariate and multivariate forecasting, not budget recommendation optimization.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated canonical topic codes was performed. The paper's relevance was identified primarily in four domains: Spending Forecasting (codes 6.A, 6.B), Anomaly Detection (8.A, 8.B), System Evaluation (12.A, 12.B, 12.C), and Behavioral Profiling & Classification (5.C). Codes 6.A and 6.B were assigned 'high' relevance because the paper directly reviews and compares state-of-the-art forecasting algorithms applicable to Odin's predictive module. Codes 12.A, 12.B, and 12.C were assigned 'high' relevance as the paper provides comprehensive evaluation frameworks and performance metrics transferable to Odin's system evaluation. Code 2.B (Seasonal and Cyclical Spending Patterns) was assigned 'medium' relevance due to its detailed treatment of seasonality in time series. Codes 8.A and 8.B received 'medium' relevance as the review covers anomaly detection methods applicable to spending data. Codes 3.A, 5.C, and 9.A were assigned 'low' relevance as they touch on general classification and efficiency considerations but lack specific focus on Odin's requirements. The Filipino Cultural Context domain (2.A, 2.C, 2.D) and domains like Savings & Debt Management (13.A, 13.B, 13.C) were considered but rejected due to the paper's technical focus on modeling rather than cultural or financial management specifics. The overall relevance is high for Odin's algorithmic and evaluation frameworks, providing a robust foundation for selecting and justifying transformer-based approaches for forecasting and anomaly detection.
limitations:
  - "The review does not specifically address personal finance spending data, limiting direct applicability. [unacknowledged]"
  - "Performance benchmarks are primarily on energy, traffic, and climate datasets, not financial transaction sequences. [unacknowledged]"
  - "Cold-start scenarios and user-specific profile dynamics are not discussed, which are critical for Odin. [unacknowledged]"
  - "No analysis of budget recommendation or constrained optimization approaches (7.A-7.D) is provided. [unacknowledged]"
  - "Model interpretability and user trust (10.A/10.B) are not addressed, though TFT mentions interpretability features. [unacknowledged]"
remember_this:
  - "Transformer architectures achieve 38% average MSE reduction over traditional methods for long-term forecasting."
  - "Autoformer and FEDformer are state-of-the-art for capturing periodicity and seasonality in time series data."
  - "Model efficiency variants like Informer and Pyraformer are suitable for resource-constrained mobile deployment."
  - "Temporal Fusion Transformer handles missing data and provides interpretable forecasts with uncertainty estimates."
  - "Evaluation frameworks using MSE, MAE, and MAPE are well-established for time series model comparison."
```
---

## Paper 27: Ahmed & Dey_summarized.md

**Source File:** `Ahmed & Dey_summarized.md`

```yaml
paper_id: 10.63125/ee5eas98
designation: international-algorithm-specific
title: Neural Network–Based Customer Retention Forecasting in Mobile Wallet Services Using 200k Historical User Profiles
authors: Ahmed, I.; Dey, B.
year: 2023
venue: Review of Applied Science and Technology
odin_topics:
  - 1.C
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 11.A
  - 12.A
  - 12.B
tldr: A neural network model using 200,000 user profiles forecasts mobile wallet retention, achieving superior discrimination (AUC 0.86) over regression baselines.
problem_and_motivation: Mobile wallet providers lack accurate, data-driven tools to predict which users will disengage, especially given complex, non-linear spending patterns and episodic usage. Existing systems often rely on simple heuristics, missing early signals of churn. This gap hinders effective retention strategies in a critical digital finance sector.
approach:
  - Analyzed 200,000 historical mobile wallet user profiles with transaction and session logs.
  - Engineered features capturing behavioral intensity (RFM), diversity (merchant variety), and stability (inter-transaction gaps, trends).
  - Developed a feedforward neural network with embedding layers for categorical variables.
  - Trained and validated models using strict time-based forward-chaining splits to prevent data leakage.
  - Evaluated against logistic, regularized regression, random forest, and gradient boosting baselines.
findings:
  - num: The neural network achieved an AUC of 0.86 and PR-AUC of 0.74, outperforming the best regression baseline (AUC 0.80, PR-AUC 0.67).
  - num: The neural network produced a lift of 3.5 in the top 10% risk segment, meaning it captured churners 3.5 times better than random selection.
  - Retained users demonstrated higher average merchant diversity (M=6.8) than churned users (M=2.9).
  - Stability measures, such as mean inter-transaction gaps, were significantly shorter for retained users (11.2 days) than for churned users (34.7 days).
  - Segment-level performance was stable, with AUC remaining high for both new users (0.84) and mature users (0.88).
  - Behavioral diversity and stability constructs provided incremental predictive value beyond traditional RFM features.
  - The study demonstrated that a combination of intensity, diversity, and stability features is crucial for accurate retention forecasting.
key_figures_tables:
  - Table 1: Profile characteristics of mobile wallet users showing dominant digital self-registration (61.2%). → Highlights demographic heterogeneity in the sample.
  - Table 2: User engagement-level distribution showing 41% medium activity users. → Confirms the need for models that handle varied transaction densities.
  - Figure 7: Framework illustrating churn imbalance in mobile wallets. → Visualizes the class imbalance challenge inherent in retention prediction.
  - Table 10: Comparative performance and segment stability showing neural network AUC 0.86 and stable across segments. → Key evidence for the model's superior and robust performance.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: Retention
    definition: Continued transactional activity within a defined post-observation horizon.
  - term: Churn
    definition: The absence of any meaningful activity for a predefined number of days or billing cycles.
  - term: Forward-Chaining Validation
    definition: A temporal validation method where models are trained on earlier periods and tested on later periods.
  - term: RFM
    definition: Recency, Frequency, and Monetary value features engineered from transaction histories.
  - term: PR-AUC
    definition: Area under the Precision-Recall curve, a metric sensitive to class imbalance.
critical_citations:
  - "[Devriendt et al., 2021] — Foundational for uplift modeling vs. churn prediction."
  - "[Coussement et al., 2017] — Key reference for baseline model comparisons in churn."
  - "[Ascarza et al., 2018] — Seminal review on customer retention management."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: contextual
      justification: Provides a general framework for analyzing financial behavior patterns.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Directly uses behavioral features (intensity, diversity, stability) to create and classify user profiles.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: The neural network and baselines are specific classification approaches for profiling users by churn risk.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: The core of the paper is developing a predictive model for future user behavior (retention).
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Evaluates a neural network forecasting algorithm on sequential spending data for churn prediction.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: The study's findings on behavioral features like stability and diversity directly inform understanding engagement dynamics.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a rigorous evaluation framework (AUC, PR-AUC, lift, calibration) for a PFMS module.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Directly evaluates and compares the performance of different algorithmic modules (neural net vs. baselines) for a forecasting task.
  contribution: This paper offers a data-driven, validated methodology for building a retention forecasting module in Odin's system. It proves that a neural network can effectively identify users at risk of churn by analyzing their spending intensity, diversity, and temporal stability. The findings justify incorporating a predictive analytics layer that can alert users or trigger interventions. The paper's emphasis on forward-chaining validation and feature engineering provides a blueprint for implementing a robust forecasting pipeline. This directly supports the development of Odin's behavioral profiling and anomaly detection functions.
  directly_justifies:
    - "A neural network-based model significantly improves retention forecasting accuracy over traditional regression methods."
    - "Behavioral diversity and stability metrics are critical for predicting user churn in mobile financial applications."
    - "A multi-feature approach combining RFM, diversity, and temporal stability yields the best predictive performance."
    - "Temporal validation is essential for realistic model evaluation in user retention forecasting."
  limits:
    - "The dataset is from a single mobile wallet platform, limiting generalizability to Odin's target Filipino context."
    - "The study does not capture psychological drivers like trust or satisfaction, which may be significant factors."
    - "The operational definition of churn may misclassify episodic users, introducing label noise."
    - "Sparse histories for new users remain a predictive challenge, highlighting the cold-start problem. [unacknowledged]"
  mapping_rationale: A systematic scan of all 12 functional domains was performed. The paper was flagged as highly relevant to the 'Spending Forecasting' (6.A, 6.B), 'System Evaluation' (12.A, 12.B), and 'Behavioral Profiling & Classification' (5.C) domains due to its core focus on predictive modeling and algorithm evaluation. It also offers medium relevance to 'Behavioral Profiling' (5.A) and 'User Retention & Engagement' (11.A) through its analysis of user profile dynamics and engagement signals. Domains like 'Filipino Cultural Context' (2.A-D) and 'Expense Categorization' (3.A-C) were considered and rejected as the paper focuses on behavioral intensity and temporal patterns, not cultural practices or the design of spending categories. The 'Mobile-First Design' (9.A, 9.B) domain was rejected as the study does not address UX design principles. The 'Data Privacy' domain was rejected as the paper mentions anonymization but does not investigate privacy mechanisms. The paper provides a strong, algorithmically-focused contribution useful for designing Odin's prediction and evaluation components, though it is international in origin and lacks specific Filipino cultural context.
limitations:
  - "Retention was based on activity thresholds, not user declarations, introducing potential label ambiguity."
  - "Unobserved external factors like promotions or regulatory changes could affect the stability of predictive relationships over time."
  - "The feature engineering framework may have reduced fidelity to fine-grained event order."
  - "The neural network model introduces interpretability challenges compared to regression baselines."
  - "The dataset represents a single platform, limiting direct external generalizability to other contexts."
  - "Sparse histories remain a challenge for new users and low-activity segments."
remember_this:
  - "Neural networks significantly outperform regression for wallet churn prediction."
  - "Behavioral diversity is just as important as transaction frequency for retention."
  - "Temporal validation prevents overoptimistic performance estimates in forecasting models."
  - "A lift of 3.5 in the top 10% means precise targeting of high-risk users."
  - "Retained users have shorter and more regular inter-transaction gaps."
```
---

## Paper 28: Ao & Fayek_summarized.md

**Source File:** `Ao & Fayek_summarized.md`

```yaml
paper_id: 10.3390/s23167167
designation: international
title: Continual Deep Learning for Time Series Modeling
authors: Ao, S.-I.; Fayek, H.
year: 2023
venue: Sensors
odin_topics:
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 9.A
  - 12.A
  - 12.B
tldr: A systematic review of deep learning applications for sensor time series, highlighting the need for preprocessing and continual learning to address non-stationary data and catastrophic forgetting.
problem_and_motivation: Real-world time series data often exhibit non-stationary distributions, causing deep learning models to suffer from catastrophic forgetting. This limits the practical deployment of these models in dynamic environments where data distributions shift over time. A systematic review of techniques to address these challenges is needed to guide the development of more robust systems.
approach:
  - Surveys recent deep learning methods (MLP, RNN, LSTM, CNN, GNN) for sensor time series classification and forecasting.
  - Reviews advanced preprocessing techniques including EMD, wavelet transform, and data augmentation.
  - Examines continual learning strategies (regularization, replay, parameter isolation) to mitigate catastrophic forgetting.
  - Evaluates the performance and applicability of these methods across diverse sensor time series datasets.
  - Discusses limitations of current CL research, including a focus on classification over regression and scalability issues.
findings:
  - "num: LSTM achieved superior forecasting performance with 4.82% MAPE vs. 20.97% for ARIMA on traffic flow data."
  - "num: Attention and DCN models work best with wavelet and FFT preprocessing for wind prediction."
  - "num: MC-SGD reduced forgetting by nearly 29% compared to joint-task training for activity recognition."
  - "num: Bidirectional LSTM achieved 94.75% accuracy for classifying resting vs. working states using EEG data."
  - "num: ConvLSTM outperformed persistence, SVR, and LSTM models for SST prediction."
  - "num: 2D CNN was the most reliable model for structural damage detection from raw time series data."
  - "num: Preprocessing with EMD improved CNN validation accuracy from 94.22% to 99.73% for gesture classification."
key_figures_tables:
  - "Table 1: Summary of DL techniques for sensor time series → Shows a wide variety of models and their applications."
  - "Table 2: Advanced preprocessing for DL applications → Demonstrates that preprocessing can significantly boost performance."
  - "Table 3: Continual learning techniques for time series → Highlights CL as a solution for non-stationary data."
  - "Figure 1: Tree diagram of DL methods for sensor time series → Provides a taxonomy of key DL architectures."
  - "Figure 2: Tree diagram of popular preprocessing methods → Categorizes techniques like EMD and wavelet transform."
  - "Figure 3: Taxonomy of continual learning methods → Groups CL strategies into regularization, replay, and isolation."
key_equations:
  - equation: "E(y_t) = E(y_{t-1}) = μ, Var(y_t) = σ^2 < ∞, Cov(y_t, y_{t-k}) = γ(k)"
    explanation: "Definition of weak stationarity for a time series."
  - equation: "L_i = (1/N_i) Σ_{r=1}^{N_i} L(y_{i,r}, ŷ_{i,r}; θ_i) + (q/( (i-1)N )) Σ_{j=1}^{i-1} Σ_{r=1}^{N_j} L( y_{j,r}, M(x̂_{j,r}; θ_i); θ_i )"
    explanation: "Continual learning objective combining current and previous task losses."
definitions:
  - term: "Continual Learning (CL)"
    definition: "A machine learning paradigm to handle non-stationary data by learning sequentially without forgetting."
  - term: "Catastrophic Forgetting (CF)"
    definition: "The abrupt loss of previously learned knowledge when a neural network is trained on new data."
  - term: "Non-stationary Time Series"
    definition: "A time series whose statistical properties, like mean and variance, change over time."
  - term: "Empirical Mode Decomposition (EMD)"
    definition: "A preprocessing technique that decomposes a signal into intrinsic mode functions (IMFs)."
critical_citations:
  - "[Kirkpatrick et al., 2017] — Introduced Elastic Weight Consolidation (EWC) to overcome catastrophic forgetting."
  - "[Hochreiter & Schmidhuber, 1997] — Developed the LSTM architecture to handle long-term dependencies."
  - "[LeCun et al., 2015] — Provided a foundational overview of deep learning and its capabilities."
  - "[De Lange et al., 2022] — Offered a comprehensive survey on continual learning for classification."
relevance:
  topics:
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Provides a general overview of DL/CL applications but not specific PFMS."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Directly discusses limitations of DL (forgetting, non-stationarity) and gaps in CL research."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "contextual"
      justification: "Focuses on technical modeling rather than financial behavior itself."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "low"
      justification: "CL addresses dynamic data, but not explicitly user profile cold-start."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Reviews many forecasting models (LSTM, CNN, etc.) directly applicable to spending prediction."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Evaluates algorithms (LSTM, GRU, etc.) for time series forecasting tasks."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews DL and CL methods for anomaly detection in time series."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "medium"
      justification: "Discusses specific algorithms like Graph Deviation Networks and VAE for anomaly detection."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "contextual"
      justification: "Mentions resource constraints for embedded/mobile sensing, informing design trade-offs."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides evaluation approaches for DL and CL models, including accuracy and forgetting metrics."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Empirically compares different DL and CL algorithms on various tasks and datasets."
  contribution: "This paper provides a foundational review of deep learning and continual learning techniques for time series modeling. It informs Odin's forecasting module by comparing the performance of various models like LSTM and CNN. The review of continual learning is crucial for Odin's anomaly detection and personalization, as it highlights methods to adapt to changing user behavior. The discussion of preprocessing techniques is relevant for ensuring data quality in Odin's expense categorization pipeline. Finally, the analysis of mobile and embedded sensing constraints can guide Odin's mobile-first design choices."
  directly_justifies:
    - "LSTM networks are a strong choice for sequential spending forecasting due to their superior performance over ARIMA."
    - "Continual learning is necessary to prevent catastrophic forgetting when adapting to a user's evolving financial patterns."
    - "Advanced preprocessing, like wavelet transforms and EMD, can significantly improve the accuracy of DL models on time series data."
    - "Replay-based continual learning methods are effective for mobile/embedded devices, balancing performance and resource use."
    - "Graph neural networks can be used for anomaly detection by modeling relationships between different spending categories."
  limits:
    - "The survey focuses on sensor time series, which may not perfectly replicate the noise and patterns of financial transaction data."
    - "Most reviewed CL methods are evaluated on classification tasks, with less focus on regression problems like spending prediction [unacknowledged]."
    - "The paper does not address the unique challenges of personal finance data, such as user privacy and sparse, irregular transactions [unacknowledged]."
    - "Specific guidance on integrating CL with constraint-based budget optimization is not provided [unacknowledged]."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains most directly relevant were 'Spending Forecasting' (6.A, 6.B) and 'Anomaly Detection' (8.A, 8.B) due to the paper's central focus on time series modeling techniques. 'System Evaluation' (12.A, 12.B) was also relevant as the paper compares different algorithms. 'Behavioral Profiling' (5.A) and 'Existing Systems' (4.A, 4.B) were assessed as medium or contextual because the paper discusses model limitations but not financial behavior or systems specifically. Domains like 'Filipino Cultural Context' (2.A-D), 'Savings & Debt Management' (13.A-C), and 'User Retention' (11.A-B) were considered and rejected as the paper provides no direct claims or evidence for these areas. The overall relevance is high for Odin's technical modules (forecasting, anomaly detection) but contextual for its domain-specific aspects, as the paper is a general methodology review."
limitations:
  - "The survey focuses on sensor time series, which may not perfectly replicate the noise and patterns of financial transaction data."
  - "Most reviewed CL methods are evaluated on classification tasks, with less focus on regression problems like spending prediction. [unacknowledged]"
  - "The paper does not address the unique challenges of personal finance data, such as user privacy and sparse, irregular transactions. [unacknowledged]"
  - "Specific guidance on integrating CL with constraint-based budget optimization is not provided. [unacknowledged]"
remember_this:
  - "Continual learning is essential for adapting to non-stationary time series data."
  - "LSTM and CNN are strong baselines for time series forecasting tasks."
  - "Preprocessing can significantly enhance deep learning model performance, with up to 99.73% accuracy."
  - "Deep learning models without CL suffer from catastrophic forgetting in dynamic environments."
  - "Replay-based CL methods balance performance and resource constraints for mobile deployment."
```
---

## Paper 29: Sonkavde et al_summarized.md

**Source File:** `Sonkavde et al_summarized.md`

```yaml
paper_id: 10.3390/ijfs11030094
designation: international-algorithm-specific
title: Forecasting Stock Market Prices Using Machine Learning and Deep Learning Models: A Systematic Review, Performance Analysis and Discussion of Implications
authors: Sonkavde, G.; Dharrao, D. S.; Bongale, A. M.; Deokate, S. T.; Doreswamy, D.; Bhat, S. K.
year: 2023
venue: International Journal of Financial Studies
odin_topics:
  - 6.A
  - 6.B
  - 7.B
  - 12.B
  - 12.C
tldr: A systematic review and comparative analysis of machine learning and deep learning models for stock price forecasting, including an ensemble model that achieves superior performance.
problem_and_motivation: Accurately forecasting stock prices remains challenging due to market volatility and limitations of traditional analysis. While many ML/DL models have been proposed, there is a need for a structured summary and practical comparative analysis of their performance.
approach:
  - This review systematically examines supervised, unsupervised, ensemble, time series, and deep learning algorithms for stock price prediction.
  - A generic machine learning pipeline for stock price prediction and classification is described, covering data collection, pre-processing, and evaluation.
  - An ensemble model combining Random Forest, XG-Boost, and LSTM is implemented and tested on TAINIWALCHM and AGROPHOS stock data.
  - Performance is evaluated using RMSE and R² scores, comparing the ensemble against standalone models like SVR, MLPR, KNN, and LSTM.
  - Hyperparameter tuning via grid search is employed to optimize the ensemble model's configuration.
findings:
  - num: The ensemble model (Random Forest + XG-Boost + LSTM) achieved the lowest RMSE (2.0247 for TANIWALCHM, 1.2658 for AGROPHOS) and highest R² scores (0.9921 and 0.9897, respectively).
  - XG-Boost outperformed ARIMA and LSTM in a prior study, with an MSE of 360.0 for a specific dataset.
  - The review identified hyperparameter tuning as a crucial step for maximizing model performance in stock forecasting.
  - Ensemble techniques generally provide superior performance over standalone models for stock price prediction.
  - The study found that sentiment analysis, when combined with price data, can improve prediction accuracy.
key_figures_tables:
  - Table 1: Ensemble model parameter configuration → Details the settings for Random Forest, XG-Boost, and LSTM in the implemented model.
  - Figure 7: TANIWALCHM stock price forecasting → Visual comparison shows ensemble model fits actual prices most closely.
  - Figure 8: AGROPHOS stock price forecasting → Ensemble model demonstrates superior fit over individual algorithms.
  - Table 2: RMSE and R² scores of algorithms → Ensemble achieves best performance with RMSE 2.0247 (TANIWALCHM) and 1.2658 (AGROPHOS).
key_equations:
  - equation: O = S_x + K
    explanation: Linear regression equation for stock price prediction.
  - equation: D(h_i, p_r) = sqrt(Σ_{l=1}^{n} (P_r - h_i)^2)
    explanation: Euclidean distance calculation for KNN.
  - equation: y'_t = k + β_p * ωD y'_{t-1} + ... + θ_q * ε_{t-q} + ε_t
    explanation: ARIMA model formula combining AR and MA components.
  - equation: Y_t = l(t) + sp(t) + v(t) + ε_t
    explanation: FBProphet model combining trend, seasonality, and holiday effects.
definitions:
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network variant with gating mechanisms.
  - term: GRU
    definition: Gated Recurrent Unit, a simpler RNN variant with two gates.
  - term: XG-Boost
    definition: Extreme Gradient Boosting, an optimized distributed gradient boosting library.
  - term: ARIMA
    definition: Autoregressive Integrated Moving Average, a classical time series forecasting model.
  - term: RMSE
    definition: Root Mean Square Error, a metric for regression model performance.
critical_citations:
  - "[Zhu and He, 2022] — Compared XG-Boost, ARIMA, and LSTM, finding XG-Boost superior."
  - "[Li and Pan, 2021] — Presented a blending ensemble of LSTM and GRU for stock prediction."
  - "[Xu et al., 2020] — Proposed E-SVR-RF ensemble algorithm for financial stock forecasting."
  - "[Di Persio and Honchar, 2017] — Demonstrated RNN, LSTM, and GRU for Google stock forecasting."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Reviews forecasting models applicable to spending prediction in PFMS.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Compares LSTM, GRU, ARIMA, and ensemble methods for sequential data.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: The forecasting techniques could be adapted for budget recommendation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Discusses RMSE and R2 for evaluating forecasting algorithms.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: low
      justification: Evaluation metrics (RMSE, R2) are transferable to budget systems.
  contribution: This paper provides a comprehensive systematic review of machine learning and deep learning models for financial forecasting, which informs the selection of predictive algorithms for Odin's spending forecasting module. It demonstrates the effectiveness of ensemble methods (Random Forest + XG-Boost + LSTM) in improving forecast accuracy, which could enhance Odin's budget recommendation and anomaly detection capabilities. The comparative analysis of evaluation metrics (RMSE, R²) establishes a benchmark for assessing Odin's algorithmic modules.
  directly_justifies:
    - "Ensemble models combining Random Forest, XG-Boost, and LSTM achieve superior forecast accuracy."
    - "Hyperparameter tuning is critical for maximizing model performance in forecasting."
    - "LSTM and GRU can capture long-term dependencies in sequential financial data."
  limits:
    - "The experimental validation is limited to two Indian stock datasets, which may not generalize."
    - "The study does not address cold-start scenarios, which are relevant to Odin's anomaly detection."
    - "Privacy and user trust implications of using ML models in finance are not discussed."
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The paper was flagged as highly relevant to the "Spending Forecasting" domain (6.A, 6.B) due to its extensive review of forecasting algorithms like LSTM, GRU, and ARIMA, as well as ensemble techniques. It was deemed relevant to "System Evaluation" (12.B, 12.C) because of its detailed discussion of evaluation metrics (RMSE, R2). A low relevance was assigned to "Budget Recommendation" (7.B) and "Anomaly Detection" (8.B) because the paper focuses on stock price prediction, not personal budget allocation or anomaly detection. The paper was rejected for all other domains (e.g., Filipino Cultural Context, Behavioral Profiling, Mobile-First Design, Data Privacy) as it does not address these areas. Overall, the paper's primary contribution to Odin lies in its methodological review of algorithms and evaluation approaches for time-series forecasting.
limitations:
  - "The study focuses only on stock market data, which may not fully represent personal spending patterns."
  - "The implemented ensemble model's performance was not compared against more recent transformer-based models."
  - "The impact of data privacy and security on model performance was not investigated [unacknowledged]."
  - "The review does not address the deployment and computational constraints of mobile-first applications [unacknowledged]."
remember_this:
  - "An ensemble of Random Forest, XG-Boost, and LSTM achieved the highest R² score of 0.9921."
  - "Hyperparameter tuning significantly enhances the performance of forecasting models."
  - "Ensemble learning techniques generally outperform individual machine learning models."
  - "LSTM and GRU are suitable for capturing long-term dependencies in sequential data."
```
---

## Paper 30: Donato et al_summarized.md

**Source File:** `Donato et al_summarized.md`

```yaml
paper_id: 10.55927/fjss.v2i3.4572
designation: local
title: The Concept of Utang Na Loob Among Filipino Working Millenials
authors: Donato, A. M.; Panotan, G. V.; Castro, J. M.; Gavino, R. M.
year: 2023
venue: Formosa Journal of Social Sciences
odin_topics:
  - "1.A"
  - "1.C"
  - "2.A"
  - "5.A"
tldr: Filipino working millennials perceive utang na loob as a self-imposed moral obligation rooted in reciprocity and shared identity, extending beyond family to include workplace relationships and evolving toward experiential and meaningful expressions of gratitude.
problem_and_motivation: There is a lack of empirical, up-to-date research on the cultural value of utang na loob, with most studies dating to the 1900s and early 2000s. This gap limits understanding of how a core Filipino value manifests and evolves among the contemporary generation of working millennials. The study aims to explore their perceptions and experiences to provide a modern contextualization of this distinct cultural construct.
approach:
  - A basic qualitative design was employed, involving semi-structured interviews with 30 employed Filipino millennials residing in Tuguegarao City, Cagayan.
  - Participants aged 26-41 were recruited via purposive sampling using social media, and data were collected through one-on-one in-person or online interviews.
  - Thematic analysis was utilized to analyze the interview data, identifying recurring themes and sub-themes from the participants' responses.
findings:
  - num: 30 employed Filipino millennials aged 26-41 from Tuguegarao City participated in the study.
  - Participants perceive utang na loob as an inner, self-imposed obligation to reciprocate kindness, rooted in the Filipino values of pakikiramdam and pakikipagkapwa.
  - The experience of utang na loob is expressed primarily through financial support for family, which generates both a strong sense of fulfillment and increased work motivation, but also feelings of burden and personal sacrifice.
  - Millennials manifest utang na loob not just through financial support but also through creating quality experiences, acts of service, and loyalty in workplace relationships.
key_figures_tables:
  - "Table 1: Summary of Informants' Demographic Profile → Shows diverse professions and age distribution among the 30 participants."
  - "Figure 1: Themes on the Concept of Utang Na Loob → Visualizes the core themes of obligation, kagandahang loob, love for family, fulfillment, and loyalty."
  - "Figure 2: Themes on the Manifestations of Utang Na Loob → Depicts how the value is expressed in familial and workplace trends."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Utang na loob"
    definition: "A core Filipino value meaning a 'debt of goodwill,' involving reciprocity and moral obligation when one person assists another."
  - term: "Kapwa"
    definition: "A Filipino concept of 'shared self' or 'shared identity,' linking an individual's inner self with others."
  - term: "Kagandahang loob"
    definition: "Genuine concern and readiness to assist others, embodying inner goodness or generosity."
  - term: "Kusang loob"
    definition: "Voluntary willingness or inner motivation to act, free from external compulsion or expectation of reward."
  - term: "Pakikiramdam"
    definition: "A Filipino cultural concept of empathy and sensitivity, sensing others' emotions to adjust behavior for social harmony."
  - term: "Pakikipagkapwa"
    definition: "A Filipino value emphasizing a sense of shared identity and treating others as equals."
critical_citations:
  - "[Hollnsteiner, 1961] — Foundational definition of utang na loob as debt of gratitude."
  - "[Pe-Pua & Marcelino, 2000] — Contextualizes utang na loob within Sikolohiyang Pilipino."
  - "[Reyes, 2015] — Explains utang na loob as central to Filipino virtue ethics."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "high"
      justification: "The study focuses directly on the perceptions and experiences of Filipino working millennials, a core user group for Odin."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Provides insights into how a core cultural value (utang na loob) directly influences the financial behavior of providing for family."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "high"
      justification: "Directly examines the Filipino value of utang na loob and its role in shaping financial obligations, a key cultural practice."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Offers a behavioral profile of Filipino working millennials driven by utang na loob, influencing their financial priorities and motivations."
  contribution: "This paper directly justifies the need for Odin to incorporate culturally specific behavioral drivers like utang na loob within its user profiling (domain 5.A). It provides empirical grounding for understanding the financial 'love for family' motivation (domain 1.C) that drives Filipino young professionals' savings and spending habits. The findings support designing financial management features that help users balance family obligations with personal financial goals (domain 13.A). Furthermore, the study highlights the potential for financial stress and 'blind loyalty' (domain 4.B), which justifies the need for Odin's budgeting and anomaly detection features to safeguard user well-being."
  directly_justifies:
    - "Utang na loob is a self-imposed obligation to reciprocate support, often expressed through financial support for family."
    - "Millennials derive fulfillment from providing for family, which can increase work motivation."
    - "Strong family obligations can lead to personal financial burden and compromise of well-being."
  limits:
    - "The study is geographically limited to Tuguegarao City, Cagayan, and may not represent the broader Filipino millennial population."
    - "The qualitative sample size (n=30) is small, limiting the generalizability of the findings."
  mapping_rationale: "A systematic scan of all 12 functional domains was performed. The paper was flagged as highly relevant to the 'Filipino Cultural Context' domain due to its direct examination of utang na loob, a core cultural value. It also strongly informs 'Expense Categorization' (domain 3) and 'Behavioral Profiling' (domain 5) by providing a cultural lens for understanding the motivations behind financial behavior. Specifically, topic codes 1.A (Filipino Young Professionals), 1.C (Financial Behavior), and 2.A (Culturally Specific Financial Practices) were deemed high relevance. Code 5.A (Financial Behavioral Profiles) was rated medium because the paper describes a profile driven by cultural obligation but does not propose a classification approach. Topics related to forecasting (6), algorithms (7, 8), system design (9), and evaluation (12) were rejected as the paper is a qualitative cultural study without technical content. The study's findings on financial burden and family obligation provide critical cultural context for designing Odin's features, such as savings goals (13.A) and anomaly detection (8.A), to be sensitive to these cultural drivers."
limitations:
  - "The study uses a qualitative design with a small, region-specific sample, limiting generalizability."
  - "Relies on self-reported data from interviews, which may be subject to social desirability bias."
  - "Does not explore the potential negative effects of utang na loob on mental health or personal financial security in depth. [unacknowledged]"
  - "Lacks a comparative analysis with other Filipino generational cohorts or demographic groups. [unacknowledged]"
  - "The study's focus on 'working millennials' does not capture the perspectives of unemployed or younger cohorts. [unacknowledged]"
remember_this:
  - "Filipino working millennials view utang na loob as a self-imposed moral obligation."
  - "Providing for family due to utang na loob leads to both fulfillment and significant personal sacrifice."
  - "The value is evolving, with millennials valuing experiential and quality-time reciprocation over purely material support."
  - "Family obligations can create financial strain, potentially requiring support from siblings and peers."
  - "The concept of utang na loob significantly shapes the financial behavior and priorities of Filipino young professionals."
```
---

## Paper 31: Xiang et al_summarized.md

**Source File:** `Xiang et al_summarized.md`

```yaml
paper_id: 10.3390/app13116515
designation: international
title: Concept Drift Adaptation Methods under the Deep Learning Framework: A Literature Review
authors: Xiang, Q.; Zi, L.; Cong, X.; Wang, Y.
year: 2023
venue: Applied Sciences
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 7.B
  - 7.C
  - 11.A
  - 12.A
  - 12.B
tldr: A literature review systematically classifying concept drift adaptation methods within deep learning, covering discriminative, generative, hybrid, and other frameworks.
problem_and_motivation: Deep learning models degrade when data distributions change (concept drift). Existing reviews on concept drift lack a dedicated focus on methods under the deep learning framework, which is crucial for modern AI-driven decision systems.
approach:
  - The paper conducts a literature review of concept drift adaptation methods.
  - It classifies methods into four deep learning categories: discriminative, generative, hybrid, and others (deep reinforcement/transfer learning).
  - For each category, it details update modes (parameter/structure), detection modes (active/passive), and types of drift handled.
  - It synthesizes findings from representative algorithms (e.g., SEOA, OARNN, ARCUS, HSN-LSTM, DeepPocket).
  - The review also covers common datasets, evaluation metrics, and identifies future research directions.
findings:
  - num: Discriminative and hybrid learning methods are most prevalent in concept drift adaptation.
  - num: Parameter updates are more common than structural updates due to faster convergence.
  - Active detection modes are widely used for explaining drift occurrence and saving computational resources.
  - Abrupt drift is the most frequently adapted type, while recurring drift is the least addressed.
  - Common challenges include high computational cost, slow convergence, and handling imbalanced data streams.
key_figures_tables:
  - "Figure 2: Types of concept drift (abrupt, incremental, gradual, recurring) → Visual classification of drift patterns."
  - "Table 1: Discriminant learning methods summary → Overview of MLP, RNN, LSTM, CNN methods and their limitations."
  - "Table 2: Generative learning methods summary → Overview of AE, GAN, RBM, SOM methods and their limitations."
  - "Table 3: Hybrid learning methods summary → Overview of LSTM+CNN, RNN+ARIMA etc., and their limitations."
key_equations:
  - equation: $P_{t0}(x,y) \neq P_{t1}(x,y)$
    explanation: Formal definition of concept drift occurrence.
  - equation: $MCC = \frac{TP \times TN - FP \times FN}{\sqrt{(TP+FP)(TP+FN)(TN+FP)(TN+FN)}}$
    explanation: Matthews correlation coefficient for imbalanced data evaluation.
definitions:
  - term: Concept Drift
    definition: Change in the underlying data stream distribution over time.
  - term: Virtual Concept Drift
    definition: Change in feature space distribution without affecting decision boundaries.
  - term: Real Concept Drift
    definition: Change in conditional probability distribution, affecting the prediction model.
  - term: Active Detection
    definition: Using a dedicated algorithm to trigger model updates upon detecting drift.
  - term: Passive Detection
    definition: Continuously adjusting the model without explicit drift detection.
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network variant for sequence data.
  - term: GAN
    definition: Generative Adversarial Network, for generating new data similar to training data.
  - term: DRL
    definition: Deep Reinforcement Learning, combining deep learning with reinforcement learning.
  - term: DTL
    definition: Deep Transfer Learning, transferring knowledge from one model to another.
  - term: AE
    definition: Autoencoder, for unsupervised feature learning and dimensionality reduction.
critical_citations:
  - "[Gama et al., 2014] — Foundational survey on concept drift adaptation."
  - "[Lu et al., 2018] — Comprehensive review of learning under concept drift."
  - "[Webb et al., 2016] — Characterized concept drift types."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly discusses forecasting models and adapting to changing data distributions.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Reviews RNN/LSTM-based algorithms for time-series prediction under drift.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly discusses anomaly detection in data streams with concept drift.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Reviews algorithms like I-LSTM and MemStream for anomaly detection under drift.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Provides a framework for adapting recommendations to changing user behavior.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: medium
      justification: Concept drift adaptation is a form of constrained optimization in dynamic environments.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: contextual
      justification: Maintaining model accuracy through adaptation is key to sustained user engagement.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Reviews evaluation metrics like accuracy, F1, MAE, and RMSE for streaming data.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides a detailed evaluation of algorithmic modules for drift adaptation.
  contribution: This review provides a taxonomy of concept drift adaptation methods that directly informs Odin's forecasting and anomaly detection modules. For Odin's spending forecasting (6.A), the review of LSTM-based online adaptive models offers a methodological baseline for dynamic prediction. For anomaly detection (8.A/8.B), the surveyed algorithms like I-LSTM and MemStream provide approaches for detecting irregular spending patterns. The paper's discussion on parameter vs. structural updates (7.C) is directly relevant to Odin's budget allocation and recommendation systems, which must adapt to user-defined constraints. The review's summary of evaluation metrics (12.A/12.B) for streaming data offers a framework for assessing Odin's algorithmic modules.
  directly_justifies:
    - "Online adaptive RNN models are effective for load forecasting under concept drift."
    - "LSTM-based anomaly detection algorithms can be enhanced with drift detection."
    - "Parameter updates reduce convergence time for abrupt concept drift."
    - "Active drift detection modes explain the occurrence of drift and save computing resources."
  limits:
    - "The paper is a literature review and does not present new empirical results."
    - "It does not specifically evaluate concept drift adaptation methods on financial spending data."
    - "The review is focused on deep learning methods and omits classical statistical or shallow methods."
  mapping_rationale: A systematic scan was performed across all 12 functional domains and their associated topic codes. The domains of 'Spending Forecasting' (6.A, 6.B) and 'Anomaly Detection' (8.A, 8.B) were flagged as highly relevant because the paper directly reviews deep learning methods designed to handle concept drift in streaming data for these exact tasks. The 'Budget Recommendation' domain (7.B, 7.C) was assigned medium relevance as the paper's discussion of model update strategies (parameter vs. structure) informs how a recommender system can adapt to changing user financial behavior. 'Engagement Dynamics' (11.A) was considered contextual, as accurate adaptive models would likely improve user trust and retention, though this is not a focus. 'System Evaluation' (12.A, 12.B) was also deemed highly relevant due to its comprehensive review of evaluation metrics for streaming algorithms. Topics related to 'Filipino Cultural Context' (2.A-D) and 'Data Privacy' (10.A) were considered and rejected as they are not addressed in the paper's scope, which is purely methodological. The overall relevance to Odin is high for its forecasting and detection modules, but contextual for user-centric or cultural aspects.
limitations:
  - "Does not provide empirical validation of the reviewed methods on financial data."
  - "Lacks a comparative analysis of the different adaptation methods' performance in a unified setting. [unacknowledged]"
  - "Focuses exclusively on deep learning, potentially overlooking simpler or more interpretable methods. [unacknowledged]"
  - "Does not discuss the practical implementation challenges of these methods in a mobile-first environment."
remember_this:
  - "Concept drift causes deep learning model degradation, affecting prediction accuracy."
  - "Parameter updates are faster than structural updates for adapting to concept drift."
  - "Abrupt drift is the most commonly addressed type in the reviewed literature."
  - "A common challenge is balancing old and new data during online model updates."
  - "Active detection modes are useful for explaining drift but add computational overhead."
```
---

## Paper 32: Mencias-Tabernilla_summarized.md

**Source File:** `Mencias-Tabernilla_summarized.md`

```yaml
paper_id: 8c5e7b12-31b4-5b9f-9d11-2c1a6e7f8d9a
designation: local
title: THE STORY BEHIND "LONDON" (LOAN DITO, LOAN DOON): EXPLORING TEACHERS' EXPENDITURE PATTERNS AND DEBT PROFILE
authors: Mencias-Tabernilla, M. C.
year: 2023
venue: Universal Journal of Educational Research
odin_topics:
  - 1.B
  - 1.C
  - 2.A
  - 2.D
  - 4.A
  - 4.B
  - 5.A
  - 13.A
  - 13.B
tldr: Filipino public school teachers' high regard for education and health drives debt acquisition, with over half of income used for loan payments, necessitating better financial management.
problem_and_motivation: Filipino public school teachers face a persistent issue of indebtedness, with combined debts reaching P319 billion, exacerbated by low take-home pay and easy access to loans. Understanding their expenditure patterns, debt profiles, and underlying reasons is crucial for developing interventions to improve their financial well-being.
approach:
  - Descriptive correlational design with 276 regular-permanent public-school teachers in Aklan.
  - Researcher-made instrument covering socio-demographics, expenditure patterns, and debt profiles.
  - Data analyzed using SPSS version 26 with descriptive statistics, t-tests, and ANOVA.
  - Focus Group Discussions informed instrument development and provided qualitative insights.
  - Data collection occurred in 2018-2019 with updates in 2021-2022 for salary and price changes.
findings:
  - num: Teachers' mean take-home pay was Php16,184.54, only more than half of their gross income.
  - num: Mean monthly family expenditure was Php22,265.00, while mean savings were only Php1,200.00, with 57.25% having no savings.
  - num: Mean cumulative debt from banks was Php156,117.76, and from GSIS was Php125,617.15.
  - num: Almost one-half of teachers' income was used to pay debts through automatic deductions and personal transactions.
  - Household size, family income, and spouse's income were positively correlated with higher expenditure.
  - Age, civil status, household size, number of children, position, length of service, and income significantly affected cumulative debt.
  - Education and professional growth, illness and death, and house construction were top reasons for acquiring debt.
  - Sound financial management and salary increase were perceived as the top ways to avoid debt.
key_figures_tables:
  - Table 1: Average monthly family expenditure pattern → Food is the largest expense at 25.26% of total expenditure.
  - Table 2: Total monthly expenditure and savings → 57.25% of teachers have no savings at all.
  - Table 3: Cumulative debt profile → Bank loans have the highest mean outstanding balance (Php156,117.76).
  - Table 4: Difference in expenditure by demographics → Household size and family income have highly significant effects.
  - Table 5: Difference in cumulative debt by demographics → Age, household size, and length of service significantly affect debt.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: APDS
    definition: Automatic Payroll Deduction System, a mechanism for loan payments directly from salaries.
  - term: GSIS
    definition: Government Service Insurance System, a social insurance institution for government employees.
  - term: NTHP
    definition: Net Take Home Pay, the salary received after all deductions.
  - term: OFW
    definition: Overseas Filipino Worker, a Filipino employed outside the country.
  - term: PERA
    definition: Personnel Economic Relief Allowance, a monthly allowance for government employees.
  - term: PAG-IBIG
    definition: A government agency providing savings and loan programs for Filipino workers.
critical_citations:
  - "[Ferrer, 2017] — Documents the long-standing debt issue among public school teachers."
  - "[Reysio-Cruz, 2019] — Reports P319 billion in teacher debts as per DepEd data."
relevance:
  topics:
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Provides specific income and debt data for teachers, a key professional demographic.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly studies expenditure patterns, debt profiles, and reasons for borrowing among teachers.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Highlights "utang" (debt) as a common practice and the cultural value of education driving borrowing.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Mentions celebrations and occasions as reasons for spending and debt, but not a primary focus.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Describes the ecosystem of lenders, including GSIS, banks, cooperatives, and loan sharks.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: contextual
      justification: Implicitly critiques APDS and loan sharks, but does not evaluate PFMS specifically.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Identifies behavioral triggers for debt (e.g., education, health) and links to TRA/TPB.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: Notes low savings rates, but no discussion of savings goal management systems.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: Directly addresses debt profiles, causes, and perceived solutions, relevant to debt management features.
  contribution: This paper provides empirical evidence on the spending and debt patterns of Filipino public school teachers, a key user group for Odin. It identifies high debt levels and low savings, justifying the need for robust budgeting and debt management features. The study's findings on the cultural drivers of debt, such as education and family obligations, inform Odin's culturally-sensitive design. The data on income and expenditure gaps supports the need for accurate forecasting and budget recommendation modules. The paper's focus on teachers, a financially vulnerable but tech-savvy demographic, validates Odin's target user focus.
  directly_justifies:
    - Teachers allocate a significant portion of income to debt repayment, highlighting the need for debt management tools in Odin.
    - High regard for education and health are primary drivers of debt, which should be considered in Odin's category design.
    - Many teachers have no savings, underscoring the necessity of features that promote savings goals.
    - The prevalence of multiple loan sources (GSIS, banks, cooperatives) suggests Odin should support debt consolidation or tracking.
    - Expenditure increases with household size and family income, a pattern Odin's forecasting module should account for.
  limits:
    - Sample limited to teachers in Aklan province, which may not be nationally representative.
    - Data collection started pre-pandemic with updates, potentially introducing recall bias.
    - Does not evaluate any specific PFMS algorithm, only provides user-level data.
  mapping_rationale: A systematic scan across all 12 functional domains and associated topic codes was conducted. The paper was flagged as relevant to the domains of Filipino Cultural Context (codes 2.A, 2.D), Existing Systems & Gaps (4.A, 4.B), Behavioral Profiling (5.A), and Savings & Debt Management (13.A, 13.B). The topic codes 1.B and 1.C were selected as high/medium relevance because the paper provides detailed financial structure and behavior data for teachers. Codes 2.A and 2.D were selected for cultural practices and spending cycles. Codes 4.A and 4.B were selected for describing the lending landscape. Code 13.B was rated high for its direct debt analysis. Codes related to algorithms (6.A, 7.D, 8.B), mobile design (9.A, 9.B), privacy (10.A, 10.B), and evaluation (12.A-C) were rejected as the paper is a descriptive study of user behavior, not a computational or UX design paper. The paper's primary contribution is empirical financial data on a key Filipino professional group, making it contextually relevant to Odin's user understanding.
limitations:
  - Sample restricted to one division in the Philippines, limiting generalizability. [unacknowledged]
  - Reliance on self-reported expenditure and debt data, prone to social desirability bias.
  - Cross-sectional design prevents causal inferences about debt accumulation.
  - Does not address the role of financial literacy programs or interventions.
remember_this:
  - Mean teacher take-home pay was Php16,184.54, with 57.25% having no savings.
  - The top reasons for debt were education and health, reflecting Filipino cultural values.
  - Sound financial management and salary increase were seen as top solutions to avoid debt.
  - Household size and family income were significant predictors of higher expenditure.
  - num: 37.00% of teachers received a gross income between Php22,000 and Php25,999.
```
---

## Paper 33: Koskelainen et al_summarized.md

**Source File:** `Koskelainen et al_summarized.md`

```yaml
paper_id: 10.1111/joca.12510
designation: international
title: Financial literacy in the digital age — A research agenda
authors: Koskelainen, T.; Kalmi, P.; Scornavacca, E.; Vartiainen, T.
year: 2023
venue: Journal of Consumer Affairs
odin_topics:
  - 1.B
  - 1.C
  - 3.A
  - 4.A
  - 5.A
  - 7.A
  - 9.B
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 12.A
tldr: Digitalization transforms financial services and personal money management, requiring a redefinition of financial literacy to include digital competencies, new behavioral risks, and novel interventions.
problem_and_motivation: Traditional financial literacy frameworks, developed for an analog world, are inadequate in the current complex digital financial landscape. The pervasive diffusion of digital financial services (DFS) creates both opportunities and new risks that users must navigate. There is a critical gap in understanding how digitalization affects financial literacy and capability.
approach:
  - Used an integrative literature review methodology following Torraco (2005).
  - Systematic search conducted in ProQuest, EBSCO, ACM Digital Library, and Google Scholar during fall 2020.
  - Applied a two-stage selection process, starting with 603 papers and narrowing to 29 peer-reviewed papers.
  - Adopted a concept-centric approach for analysis, categorizing papers into three themes: Fintech, Financial behavior in digital environments, and Behavioral interventions.
  - Analyzed papers from finance, economics, and information systems disciplines.
findings:
  - Digital financial literacy requires updating financial literacy curricula with new skills like cybersecurity awareness and understanding of algorithmic influence.
  - Digital nudging can both help (e.g., via smartphone apps for tracking spending) and potentially harm (e.g., via persuasive design for sales) consumer financial outcomes.
  - Loss of tangibility in digital payments tends to increase spending, as evidenced by literature starting from the 1980s.
  - Older, lower-income, and disabled consumers are less likely to use mobile payment apps, risking digital exclusion.
  - The use of digital financial management services makes consumers less aware of their spending.
key_figures_tables:
  - Figure 1: Conceptual description of financial literacy and capability → Foundation for the paper's proposed digital framework.
  - Figure 2: Conceptual description of digital financial literacy and capability → Illustrates how digitalization affects all elements of financial literacy.
  - Table 1: Research on digital financial literacy → Categorizes literature into Fintech, financial behavior, and behavioral interventions.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Fintech
    definition: Technologically enabled financial innovation resulting in new business models, applications, processes, or products.
  - term: Digital Financial Literacy
    definition: The knowledge, skills, and awareness needed to use digital financial services and understand their risks and benefits.
  - term: Financial Capability
    definition: Broader concept than financial literacy, including the ability and opportunity to act and gain access to financial products.
  - term: Digital Nudging
    definition: Influencing choices through algorithms and user-interface design in digital environments.
critical_citations:
  - "[Lusardi & Mitchell, 2014] — Foundational work on financial literacy measurement and economic importance."
  - "[Thaler & Sunstein, 2008] — Introduced the concept of nudging, central to the behavioral interventions theme."
  - "[Gomber et al., 2017] — Key paper on digital finance and Fintech research directions."
  - "[OECD, 2018] — Provides policy guidance on digitalisation and financial literacy."
  - "[Huston, 2010] — Seminal paper on measuring financial literacy."
relevance:
  topics:
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: contextual
      justification: Discusses how digitalization changes access and structure of financial services.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Directly addresses how digital environments alter financial behaviors like spending.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: low
      justification: Mentions personal finance apps for account management, implying categorization.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews Fintech and mobile banking apps, providing a landscape overview.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: Discusses behavioral economics and psychological biases influencing financial decisions.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Highlights digital tools and nudges that can assist in budgeting and keeping track of finances.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Reviews research on mobile banking usage, noting that design can influence engagement and financial decisions.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Extensively discusses risks including data confidentiality, digital profiling, and cybersecurity threats.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Highlights how use, perceived security, and ethical issues relate to user trust in digital financial services.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Discusses how digital nudging and app features can influence user engagement and behavior.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: Explores how tools like smartphone apps and text messages can be used for sustained behavioral change.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: low
      justification: Critiques of nudging suggest a need for evaluating outcomes and ethical frameworks.
  contribution: "This review paper provides a foundational framework for understanding digital financial literacy, which is essential for designing the educational and behavioral components of Odin. It directly informs the need for a 'digital' component in Odin's behavioral profiling, as traditional financial literacy metrics are insufficient in a digital-first app. The paper's analysis of Fintech and digital behaviors provides the context for Odin's core functionalities, such as expense tracking, budgeting, and anomaly detection, by outlining the new risks and opportunities in the digital financial landscape. Its discussion of digital nudging and behavioral interventions offers a theoretical basis for Odin's user engagement and retention strategies. The explicit call for updated measurement frameworks for digital financial literacy justifies Odin's approach to classifying user financial behavior based on digital interactions rather than solely on static knowledge tests."
  directly_justifies:
    - "Traditional financial literacy measures are insufficient for a digital world, necessitating new approaches to user profiling."
    - "Digitalization changes the financial behavior of young professionals, making them less aware of spending."
    - "Data privacy and security are primary concerns in personal finance apps, requiring robust design."
    - "Digital nudging can be used to improve financial behavior and should be incorporated into app design."
  limits:
    - "The paper is a literature review and does not present new empirical data on digital financial literacy interventions."
    - "Focuses on papers from finance, economics, and information systems, potentially missing relevant HCI or design literature."
    - "Provides high-level themes but not specific algorithmic or implementation details for a PFMS."
  mapping_rationale: "All 12 functional domains were systematically scanned against the paper's content. The paper was flagged as highly relevant to Data Privacy & User Trust (10.A, 10.B) due to its extensive discussion of risks like data profiling and fraud. It was also deemed highly relevant to User Retention & Engagement (11.A, 11.B) because of its detailed exploration of behavioral interventions and digital nudging. Medium relevance was assigned to Expense Categorization (3.A, as part of PFMS landscape), Existing Systems (4.A, providing a landscape of Fintech), Behavioral Profiling (5.A, discussing behavioral economics), Budget Recommendation (7.A, mentioning tools for saving and budgeting), and Mobile-First Design (9.B, reviewing mobile banking usage). The domains of Forecasting (6.A, 6.B) and Anomaly Detection (8.A-C) were rejected as the paper does not discuss predictive algorithms. The Savings & Debt Management domains (13.A-C) were considered contextual due to mentions of over-indebtedness and saving, but the paper does not provide specific management strategies. Overall, the paper provides a broad contextual and motivational framework for Odin, justifying the need for a comprehensive, digitally-aware PFMS that addresses user behavior, trust, and engagement."
limitations:
  - "The literature review is limited to papers published only in finance, economics, and information systems. [unacknowledged]"
  - "Excluding conference proceedings may have led to missing new technological developments. [acknowledged]"
  - "The sample is from 2020, and the digital finance landscape changes rapidly, so some findings may be less current. [unacknowledged]"
remember_this:
  - "Digital payments reduce spending tangibility and can increase consumption."
  - "Fintech innovations introduce new risks like data profiling and fraud."
  - "Digital nudging can improve financial behaviors but raises ethical concerns."
  - "80% of millennial smartphone owners use their device for transactional financial purposes."
  - "Financial literacy measurement must evolve to include digital competencies."
```
---

## Paper 34: Gao et al_summarized.md

**Source File:** `Gao et al_summarized.md`

```yaml
paper_id: 10.1145/3539618.3591774
designation: international-algorithm-specific
title: Leveraging Transferable Knowledge Concept Graph Embedding for Cold-Start Cognitive Diagnosis
authors: Gao, W.; Wang, H.; Liu, Q.; Wang, F.; Lin, X.; Yue, L.; Zhang, Z.; Lv, R.; Wang, S.
year: 2023
venue: Proceedings of the 46th International ACM SIGIR Conference on Research and Development in Information Retrieval
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 8.C
  - 12.A
  - 12.B
tldr: A two-stage framework using a knowledge concept graph enables zero-shot cognitive diagnosis by transferring student states from source to target domains via GCN-learned embeddings.
problem_and_motivation: Existing cognitive diagnosis models fail in domain-level zero-shot scenarios where target domains lack student-exercise interactions. This prevents intelligent systems from launching new businesses or operating under privacy constraints. A method to diagnose student proficiency without target-domain interaction data is critically missing.
approach:
  - The TechCD framework uses a pedagogical knowledge concept graph (KCG) as an intermediary to connect source and target domains.
  - A graph convolutional network (GCN) learns entity embeddings from the KCG, which includes concepts, exercises, and their relations.
  - Bottom-layer discarding operation extracts universal and transferable student states from the GCN's upper layers.
  - The framework is instantiated with IRT, MIRT, and NeuralCD as diagnostic adaptors for domain-adaptive diagnosis.
  - Training is performed on source domain data to predict student performance, then applied to zero-shot target domains.
findings:
  - num: TechCD outperforms NLP-based and GCN-based baselines by up to 10% in AUC on zero-shot student performance prediction.
  - num: Discarding bottom-layer GCN outputs for students improves performance, but discarding for exercises weakens it.
  - The KCG effectively bridges different domains, enabling transfer of cognitive signals even when students partially overlap.
  - num: Using out-domain datasets improves TechCD's performance, achieving up to 56.73% ACC when source data is unavailable.
  - Diagnostic reports generated by TechCD are interpretable and show meaningful prerequisite-based proficiency patterns.
  - Exercise recommendations from TechCD balance difficulty and engagement, avoiding too easy or too hard items.
  - The framework provides both classification (ACC, AUC) and regression (RMSE) performance gains over baselines.
key_figures_tables:
  - Figure 1: Knowledge concept graph linking Math and Programming domains → KCG bridges isolated domains for state propagation.
  - Figure 2: TechCD architecture overview → Framework consists of KCG embedding and domain-adaptive diagnosis stages.
  - Figure 3: ACC and RMSE comparisons for bottom-layer discarding → Discarding student layers best, discarding both weakens performance.
  - Figure 4: Diagnostic report and cognitive graph example → TechCD diagnoses cold-start domain concepts while NeuralCD cannot.
  - Table 2: KCG statistics (17,793 entities, 23,395 triples) → Large-scale graph connects multiple educational datasets.
  - Table 3: Performance comparison across IRT, MIRT, NeuralCD → TechCD consistently outperforms baselines in zero-shot settings.
key_equations:
  - equation: \hat{y}_{uv} = F_{\text{CDM}}(\boldsymbol{u}, \boldsymbol{v}, \Theta^*)
    explanation: General form of cognitive diagnosis models predicting student performance.
  - equation: \boldsymbol{z}_i^{(l)} = \sum_{r \in \mathcal{R}_i} \frac{1}{|\mathcal{P}_i^r|} \sum_{(e_j, r, e_i) \in \mathcal{P}_i^r} \mathbf{W}_r \boldsymbol{z}_j^{(l-1)}
    explanation: GCN aggregation over KCG relations to update entity embeddings.
  - equation: \boldsymbol{p}_u = (p_{u1}; p_{u2}; \cdots; p_{u|\mathcal{C}|}), \quad p_{uc} = f_u(\boldsymbol{h}_u \oplus \boldsymbol{h}_c) \in (0,1)
    explanation: Student proficiency trait modeled by fusing student and concept embeddings.
  - equation: \Theta^* = \arg\min_{\Theta} \mathcal{L}(y(\mathbf{L}_S), \mathcal{G})
    explanation: Optimization objective trained on source domain data for zero-shot transfer.
definitions:
  - term: CD
    definition: Cognitive Diagnosis - profiling student proficiency on knowledge concepts.
  - term: DZCD
    definition: Domain-level zero-shot cognitive diagnosis - diagnosing in a new domain without student-exercise interactions.
  - term: KCG
    definition: Knowledge Concept Graph - graph linking concepts and exercises with educational relations.
  - term: GCN
    definition: Graph Convolutional Network - neural network for learning graph-structured embeddings.
  - term: IRT
    definition: Item Response Theory - unidimensional logistic model for student-exercise interaction.
  - term: MIRT
    definition: Multidimensional Item Response Theory - multidimensional extension of IRT.
  - term: NeuralCD
    definition: Neural Cognitive Diagnosis - deep learning-based CD using MLP interaction functions.
  - term: ACC
    definition: Accuracy - classification metric for correct/incorrect prediction.
  - term: AUC
    definition: Area Under the ROC Curve - ranking metric for prediction performance.
  - term: RMSE
    definition: Root Mean Square Error - regression metric for predicted vs. actual scores.
critical_citations:
  - "[Wang et al., 2020] — NeuralCD is the base deep CD model used for instantiation."
  - "[Zhuo et al., 2022] — Tiger framework inspired bottom-layer discarding for cross-domain transfer."
  - "[Liu et al., 2019] — EKT uses exercise text as intermediary, a baseline for comparison."
  - "[Gao et al., 2021] — RCD uses relation maps, similar KCG-based CD but not zero-shot."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly analogous to diagnosing student proficiency profiles across domains.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: high
      justification: Addresses domain-level cold-start, directly parallel to new user financial profiling.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses GCN-based classification, applicable to financial profile categorization.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Student performance prediction is analogous to spending behavior prediction.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: GCN and transfer learning methods are relevant for sequential financial forecasting.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Provides background on cold-start baselines, relevant for anomaly detection initialization.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Not directly about anomaly detection, but transfer learning can inform anomaly baselines.
    - code: 8.C
      name: Cold‑Start Baseline Strategies for Anomaly Detection
      relevance: medium
      justification: The zero-shot framework is directly applicable to cold-start anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: ACC, AUC, RMSE are standard for evaluating financial prediction modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Extensive experimental evaluation comparing multiple diagnostic adaptors.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: contextual
      justification: The recommendation application parallels budget recommendation evaluation.
  contribution: "This paper introduces a transferable knowledge concept graph embedding framework that directly addresses the cold-start problem in cognitive diagnosis. For Odin's behavioral profiling module, it provides a methodology to infer user financial profiles without historical spending data in a new domain. The two-stage approach of learning universal student states and domain-specific exercise traits can be adapted to model user spending behavior and expense categorization. The framework's ability to leverage out-domain datasets offers a strategy for Odin to bootstrap profiling using external financial data sources. The diagnostic report generation demonstrates how such models can provide interpretable insights, crucial for user trust in financial management."
  directly_justifies:
    - "A knowledge graph can bridge domains to enable zero-shot profiling of new users."
    - "Bottom-layer discarding in GCNs extracts transferable user states for cold-start scenarios."
    - "Combining a transferable embedding stage with a domain-adaptive diagnosis stage is effective."
    - "Out-domain datasets can improve performance when target domain data is unavailable."
    - "Diagnostic reports can be generated from refined student and exercise traits."
  limits:
    - "The KCG construction requires domain expertise and may not fully capture all financial concept relations."
    - "The method relies on source domain data with similar student populations, which may not hold across different user demographics."
    - "The GCN-based approach may not scale to very large, dynamic graphs typical of financial transactions. [unacknowledged]"
    - "The paper does not explore privacy-preserving transfer learning, a key concern for financial data. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains was conducted. The paper was flagged as highly relevant to Behavioral Profiling & Classification (5.A, 5.B, 5.C) because its core problem—domain-level zero-shot cognitive diagnosis—directly parallels cold-start user profiling in personal finance. For Spending Forecasting (6.A, 6.B), the predictive modeling and transfer learning techniques are directly applicable to forecasting user spending patterns. Anomaly Detection (8.A, 8.B, 8.C) benefits from the cold-start baseline strategies discussed, though the paper does not focus on anomaly detection itself. System Evaluation (12.A, 12.B, 12.C) is relevant due to the rigorous experimental methodology and metrics used. Domains like Filipino Cultural Context (2.A-D), Expense Categorization (3.A-C), and Savings & Debt Management (13.A-C) were considered but rejected because the paper does not address cultural practices, category design, or savings behavior. The overall relevance to Odin is strong, providing algorithmic frameworks for user profiling and prediction in zero-shot scenarios."
limitations:
  - "Relies on a knowledge concept graph which may not exist for personal finance domains. [unacknowledged]"
  - "Assumes student populations overlap across domains, which may not hold in financial contexts. [unacknowledged]"
  - "The bottom-layer discarding hyper-parameter λ requires tuning and may not generalize across datasets."
  - "The paper does not address real-time adaptation or incremental learning, crucial for financial tracking. [unacknowledged]"
  - "The exercise recommendation application assumes difficulty and proficiency thresholds, which may not directly translate to financial goal setting. [unacknowledged]"
remember_this:
  - "Knowledge concept graphs can bridge domains for zero-shot user profiling."
  - "GCNs with bottom-layer discarding extract transferable user states for cold-start."
  - "A two-stage framework achieves superior zero-shot prediction accuracy."
  - "Out-domain datasets improve performance when target data is unavailable."
  - "Diagnostic reports from such models are interpretable and support decision-making."
```
---

## Paper 35: George et al_summarized.md

**Source File:** `George et al_summarized.md`

```yaml
paper_id: "10.63125/913ksy63"
designation: "international"
title: "Machine Learning for Fraud Detection in Digital Banking: A Systematic Literature Review"
authors: "George, M.Z.H.; Alam, M.K.; Hasan, M.T."
year: 2023
venue: "ASRC Procedia: Global Perspectives in Science and Scholarship"
odin_topics:
  - "8.A"
  - "8.B"
  - "8.C"
  - "10.A"
  - "10.B"
  - "12.A"
  - "12.B"
  - "12.C"
tldr: "A systematic review of 118 studies on machine learning for fraud detection in digital banking reveals dominance of supervised learning, rising deep learning and hybrid models, and importance of evaluation metrics and interpretability, with cross-regional regulatory differences shaping adoption."
problem_and_motivation: "Fraud detection literature in digital banking is fragmented across methods, regions, and regulatory contexts, lacking a consolidated synthesis that integrates supervised, unsupervised, deep learning, and hybrid approaches. A comprehensive review is needed to identify methodological gaps, deployment challenges, and cross-regional variations to guide both research and practice."
approach:
  - "Applied PRISMA guidelines for systematic review, searching Scopus, Web of Science, IEEE Xplore, ACM Digital Library, and ScienceDirect."
  - "Screened 2,346 initial records, applied inclusion/exclusion criteria, resulting in 118 peer-reviewed studies and institutional reports for final synthesis."
  - "Extracted data on algorithms, datasets, evaluation metrics, and regional contexts using structured coding sheets."
  - "Conducted thematic synthesis across supervised, unsupervised, deep learning, hybrid, and evaluation/interpretability categories."
  - "Performed cross-regional comparison of regulatory and infrastructural influences on fraud detection adoption."
findings:
  - "num: Supervised learning studies (36) accumulated over 9,200 citations, remaining the dominant paradigm."
  - "num: Unsupervised anomaly detection studies (27) received over 6,800 citations, increasingly valued for novel fraud patterns."
  - "num: Deep learning studies (21) garnered over 7,300 citations, demonstrating rapid emergence in transaction monitoring."
  - "num: Hybrid approach studies (19) accounted for over 5,600 citations, showing superior adaptability."
  - "num: Evaluation and interpretability studies (15) received over 4,500 citations, underscoring their centrality."
  - "Cross-regional analysis reveals PSD2/SCA in Europe, fintech-led innovation in North America, and infrastructure-dependent approaches in emerging economies."
  - "Methodological gaps include inconsistent handling of class imbalance, limited reproducibility, and insufficient robustness checks."
key_figures_tables:
  - "Figure 1: Digital Banking Fraud Detection Framework → shows integration of data, ML models, and alert systems."
  - "Figure 4: Fraud Detection Machine Learning Framework → contrasts supervised, unsupervised, and hybrid paradigms."
  - "Figure 6: Data Imbalance and Real-Time Processing Challenges → highlights SMOTE, cost-sensitive learning, and latency constraints."
  - "Figure 8: Global Fraud Detection Regulatory Framework → compares EU, North America, and emerging markets."
  - "Figure 11: PRISMA methodology flow diagram → illustrates systematic review screening process."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "PR-AUC"
    definition: "Precision-Recall Area Under the Curve, preferred for imbalanced classification."
  - term: "ROC-AUC"
    definition: "Receiver Operating Characteristic Area Under the Curve, commonly used but can mislead under skew."
  - term: "SHAP"
    definition: "SHapley Additive exPlanations, a framework for model interpretability."
  - term: "LIME"
    definition: "Local Interpretable Model-agnostic Explanations, another interpretability tool."
  - term: "SMOTE"
    definition: "Synthetic Minority Over-sampling Technique, used to address class imbalance."
  - term: "PSD2"
    definition: "Revised Payment Services Directive, EU regulation mandating strong authentication and open banking."
  - term: "GDPR"
    definition: "General Data Protection Regulation, EU privacy law affecting data processing and explainability."
  - term: "F1-score"
    definition: "Harmonic mean of precision and recall, balancing both metrics."
critical_citations:
  - "[Ngai et al., 2011] — early application of supervised learning in fraud detection."
  - "[Susto et al., 2018] — anomaly detection for imbalanced data."
  - "[Carcillo et al., 2021] — hybrid supervised-unsupervised approach."
  - "[Lundberg & Lee, 2017] — SHAP for model interpretability."
relevance:
  topics:
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Reviews anomaly detection methods including unsupervised and hybrid approaches for transactional data."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Covers supervised, unsupervised, deep learning, and hybrid algorithms applicable to spending anomalies."
    - code: "8.C"
      name: "Cold‑Start Baseline Strategies for Anomaly Detection"
      relevance: "high"
      justification: "Discusses imbalanced learning and evaluation metrics that inform baseline strategies."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "medium"
      justification: "Addresses GDPR/PSD2 and privacy constraints that shape feature engineering and data access."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "medium"
      justification: "Emphasizes interpretability and transparency as essential for user trust and regulatory compliance."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Provides detailed guidance on metrics (precision, recall, F1, PR-AUC) and cost-sensitive evaluation."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Discusses trade-offs between accuracy and interpretability, and the use of PR-AUC over ROC-AUC."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "high"
      justification: "Imbalanced learning and cost-sensitive evaluation are directly applicable to budget recommendation performance assessment."
  contribution: "The systematic review offers a comprehensive taxonomy of anomaly detection algorithms—supervised, unsupervised, and hybrid—that directly informs the design of Odin's anomaly detection module (8.A/8.B/8.C). Its detailed treatment of evaluation metrics (PR-AUC, F1, cost curves) and imbalanced learning strategies provides a foundation for evaluating Odin's algorithmic modules (12.B/12.C). The emphasis on interpretability via SHAP/LIME supports the need for explainable outputs in Odin's budget recommendation and anomaly alerts. Cross-regional regulatory insights (GDPR/PSD2) contextualize data privacy and trust considerations (10.A/10.B) for Odin's Philippine context, though direct applicability is limited."
  directly_justifies:
    - "Precision-recall AUC is more informative than ROC-AUC for imbalanced fraud datasets."
    - "Hybrid models combining supervised and unsupervised learning reduce false positives while improving recall."
    - "SHAP and LIME provide post-hoc interpretability essential for regulatory compliance."
    - "Real-time processing constraints require lightweight feature engineering and optimized models."
  limits:
    - "The review focuses on banking fraud, not personal spending anomaly detection; behavioral patterns differ."
    - "The regulatory context (GDPR/PSD2) is European, not directly applicable to Philippines."
    - "The paper does not address cold-start problems or user-defined constraints specific to PFMS."
    - "Findings are based on literature up to 2023, missing recent advances."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. Domains flagged as relevant include Anomaly Detection (codes 8.A, 8.B, 8.C) with high relevance due to the paper's extensive coverage of anomaly detection algorithms for transactional data; System Evaluation (12.A, 12.B, 12.C) with high relevance due to detailed discussion of evaluation metrics (PR-AUC, F1) and interpretability frameworks; and Data Privacy & User Trust (10.A, 10.B) with medium relevance due to regulatory and trust considerations. Borderline cases: the paper's discussion of behavioral patterns in fraud detection touches on 5.A but does not address financial behavioral profiles, so it was considered but rejected as contextual only. Domains such as Filipino Cultural Context, Expense Categorization, Spending Forecasting, Budget Recommendation, Mobile-First Design, and Savings/Debt Management were considered and rejected as they are not addressed. The paper's overall relevance to Odin is moderate, providing strong methodological guidance for anomaly detection and evaluation but limited direct applicability to personal finance management."
limitations:
  - "Limited reproducibility due to private datasets and opaque feature pipelines."
  - "Inconsistent handling of class imbalance across studies."
  - "Lack of standardized theoretical integration with criminological frameworks."
  - "Robustness to adversarial manipulation and concept drift is insufficiently assessed."
  - "The review does not address cold-start baseline strategies for anomaly detection in new users [unacknowledged]."
remember_this:
  - "Supervised learning remains dominant with 36 studies and 9,200+ citations."
  - "Deep learning studies have surged, accumulating 7,300+ citations across 21 studies."
  - "PR-AUC is preferred over ROC-AUC for imbalanced fraud detection."
  - "Hybrid models outperform single methods by balancing precision and recall."
  - "Regulatory contexts (PSD2, GDPR) significantly shape model design and adoption."
```
---

## Paper 36: Gumasing et al_summarized.md

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

## Paper 37: Shaikh et al_summarized.md

**Source File:** `Shaikh et al_summarized.md`

```yaml
paper_id: 6aebd210-1dcb-50c0-a1b1-9b3bcd54f3c6
designation: international
title: "Advances in mobile financial services: a review of the literature and future research directions"
authors: "Shaikh, A. A.; Alamoudi, H.; Alharthi, M.; Glavee-Geo, R."
year: 2023
venue: "International Journal of Bank Marketing"
odin_topics:
  - "1.A"
  - "2.A"
  - "4.A"
  - "4.B"
  - "5.A"
  - "5.C"
  - "9.A"
  - "10.A"
  - "10.B"
  - "11.A"
  - "11.B"
  - "12.A"
tldr: "A framework-based review of 115 MFS studies identifies three domains (mobile banking, payment, money) and proposes the TCMM framework to analyze theory, constructs, methods, and moderators."
problem_and_motivation: "Prior reviews of mobile financial services (MFS) are limited to specific domains like mobile banking or payments, lacking a holistic synthesis. A comprehensive framework is needed to organize the fragmented literature and guide future research across the entire MFS ecosystem."
approach:
  - "A structured literature review following Webster and Watson's (2002) three-step approach was conducted."
  - "Searches in five multidisciplinary databases (e.g., ScienceDirect, Web of Science) using 14 keywords identified 115 relevant journal articles from 2009–2020."
  - "The study introduces the Theory, Construct, Method, Moderator (TCMM) framework as an organizing model for synthesizing MFS research."
  - "Three major MFS domains were defined and delineated: mobile banking, mobile payments, and mobile money, each with distinct service characteristics and target segments."
  - "A 'Comprehensive framework of MFS domains' was developed, incorporating service, customer, demographic, and institutional dynamics."
findings:
  - "Perceived ease of use (or its equivalent) was the most frequently used construct, appearing in 81% of the reviewed studies."
  - "num: 90% of the studies used quantitative survey methods, while mixed methods were used in only 10%."
  - "num: The largest number of studies (14%) were conducted in China, followed by India (10%) and Taiwan (7%)."
  - "Trust was a significant construct in 59% of the studies, underscoring its importance in MFS adoption."
  - "Social influence was examined in 50% of the studies, indicating its role in shaping user behavior."
  - "The review identifies 14 distinct research themes for future MFS research, including AI-enabled services and the impact of COVID-19."
  - "Perceived risk was used as a construct in 37% of studies, typically showing a negative effect on adoption and use intention."
  - "Gender and age were the most frequently used demographic moderators in the reviewed literature."
  - "Mobile money is distinct for targeting unbanked populations, relying on agent networks, and facilitating high-volume, low-value transactions."
  - "The study proposes a segregation of mobile banking into financial and non-financial services."
key_figures_tables:
  - "Table 1: Summarizes differences between mobile banking, payment, and money → Provides a clear taxonomy for MFS domains."
  - "Table 5: Lists frequency of key constructs (e.g., PEOU, BI) used in 115 MFS studies → Highlights most critical variables."
  - "Figure 3: Shows distribution of MFS studies by country → Reveals research concentration in emerging markets."
  - "Figure 4: A comprehensive framework of MFS domains → Integrates service, customer, and institutional dynamics."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Mobile Financial Services (MFS)"
    definition: "An all-inclusive service portfolio for consumer segments accessing and using retail- and business-related banking and payment services on mobile devices."
  - term: "Mobile Banking"
    definition: "An innovative and cost-effective application of mobile commerce with extended capabilities, used virtually by bank account holders via web browser or downloadable app on smartphones or tablets."
  - term: "Mobile Payment"
    definition: "An anytime-anywhere payment mechanism offered by banking and non-banking entities, executed seamlessly in proximity or remote mode via handheld devices."
  - term: "Mobile Money"
    definition: "A financial inclusion tool used in developing countries by financially excluded communities to send and receive funds and make micropayments using a feature phone with SMS technology."
  - term: "TCMM Framework"
    definition: "An organizing framework proposed for MFS reviews, focusing on Theory, Constructs, Methods, and Moderators."
  - term: "FinTech"
    definition: "A non-banking entity that offers digital financial services, often acting as a disintermediation force."
  - term: "Unbanked"
    definition: "Adults who do not have a formal account at a financial institution or with a mobile money provider."
  - term: "De-banked"
    definition: "Consumers who refuse to access and use various alternative delivery channels despite their availability and refuse to maintain any formal relationship with a bank."
critical_citations:
  - "[Shaikh & Karjaluoto, 2015] — Foundational review of mobile banking adoption."
  - "[Baptista & Oliveira, 2015] — Examined cultural moderators in mobile banking acceptance."
  - "[Glavee-Geo et al., 2019] — Key empirical study on mobile money usage in Ghana."
  - "[Karjaluoto et al., 2019] — Examined perceived value drivers of MFS app use."
  - "[Venkatesh et al., 2003] — Originated UTAUT, widely used in MFS adoption studies."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "contextual"
      justification: "Mentions new demographic groups like Millennials and Gen Z as important future research areas."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "contextual"
      justification: "Discusses cultural moderators (e.g., collectivism) and regional differences in MFS adoption."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Provides a comprehensive taxonomy of MFS (banking, payment, money) and a framework of the service landscape."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Identifies limitations like the lack of studies on continuous use, agent-related fraud, and non-financial services."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "contextual"
      justification: "Discusses consumer segmentation (banked, unbanked, de-banked) and pre/post-adoption behavior."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "low"
      justification: "Mentions classification of consumers into domains based on choices and access but does not detail classification algorithms."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "medium"
      justification: "Conceptualizes MFS as mobile-first applications and distinguishes them from desktop/Internet banking."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "contextual"
      justification: "Discusses PSD2 and open banking, which raise data security and privacy challenges."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "high"
      justification: "Identifies trust as a key construct (59% of studies) affecting adoption and use of MFS."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "medium"
      justification: "Examines the shift from pre-adoption to post-adoption continuous use behavior."
    - code: "11.B"
      name: "Retention Mechanisms and Engagement Design"
      relevance: "medium"
      justification: "Highlights the need for strategies to ensure consumer sustained use of MFS for long-term relationship building."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "contextual"
      justification: "Presents TCMM as a new framework for evaluating and synthesizing MFS literature."
  contribution: "This review provides a foundational taxonomy for MFS, directly informing Odin's classification of financial data. The TCMM framework offers a structured approach for synthesizing literature that can be adapted for Odin's system evaluation. By identifying key behavioral constructs like trust and social influence, the paper guides the selection of critical variables for behavioral profiling. The proposed research directions, particularly on AI-enabled services and non-financial features, offer a roadmap for Odin's future feature development and research. The concept of segmenting users based on their financial relationship (banked/unbanked/de-banked) provides a preliminary basis for Odin's user classification."
  directly_justifies:
    - "Perceived usefulness and ease of use are primary drivers of behavioral intention to adopt MFS."
    - "Trust is a significant construct in the adoption and continuous use of mobile financial services."
    - "The long-term success of MFS depends on users' sustained use, not just initial adoption."
    - "Social influence affects consumer use intention and adoption of MFS."
    - "Research on continuous or sustained use of MFS is still limited."
  limits:
    - "The review excludes practitioner-oriented articles and non-survey studies (e.g., experiments), limiting the methodological scope of findings."
    - "The study does not include bibliometric or network analyses, which could provide additional insights into the field's structure."
    - "The TCMM framework's focus on quantitative survey studies may not fully capture qualitative or design-oriented research."
    - "The review does not provide a detailed analysis of specific forecasting or classification algorithms, which are central to Odin's core functions."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was conducted to assess the paper's relevance to Odin. The 'Existing Systems & Gaps' domain was flagged as highly relevant because the paper offers a comprehensive taxonomy of MFS and identifies research gaps. Within this domain, topic 4.A (Landscape) was assigned 'medium' as the paper provides a framework, and 4.B (Limitations) was 'medium' due to the explicit identification of research gaps. The 'Behavioral Profiling' domain (topics 5.A, 5.C) received 'low' and 'contextual' relevance, as while it discusses user segments and behavioral stages, it does not detail classification algorithms. Similarly, topics under 'Mobile-First Design' (9.A) and 'Data Privacy & User Trust' (10.B) were assigned 'medium' because the paper identifies mobile-first channels and highlights the critical role of trust, respectively. The 'User Retention' domain (11.A, 11.B) was marked 'medium' for identifying the importance of continuous use. Topics like 'Spending Forecasting' (6.A, 6.B) and 'Anomaly Detection' (8.A, 8.B) were considered and rejected as the paper is a broad review and does not cover specific algorithmic techniques for these areas. 'Budget Recommendation' topics were also rejected for the same reason. The overall relevance is moderate, as the paper provides a valuable overarching context and foundational concepts for Odin but lacks the technical depth needed to directly justify specific algorithms."
limitations:
  - "Only journal articles published between 2009–2020 were included; conference proceedings and recent publications (post-2020) are omitted."
  - "The review is heavily dominated by quantitative survey studies, potentially neglecting insights from qualitative or mixed-method research."
  - "The proposed TCMM framework is a literature organizing tool and is not empirically validated in this paper. [unacknowledged]"
  - "The future research agenda, while comprehensive, does not prioritize or offer specific design recommendations for algorithmic approaches. [unacknowledged]"
remember_this:
  - "MFS is segmented into mobile banking, payment, and money, each with distinct users and use cases."
  - "Perceived usefulness, ease of use, trust, and social influence are the most frequently studied constructs."
  - "Research has increasingly focused on MFS since 2017, with a shift towards downloadable apps and AI."
  - "The TCMM framework provides a structured way to analyze MFS literature across multiple dimensions."
  - "num: 90% of MFS adoption research relies on surveys, indicating a methodological gap in experimental studies."
```
---

## Paper 38: Cortez_summarized.md

**Source File:** `Cortez_summarized.md`

```yaml
paper_id: "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
designation: "local"
title: "Personal Financial Management Practices Among Selected Personnel of the Bureau of the Treasury – Central Office"
authors: "Cortez, D. D."
year: 2023
venue: "Guild of Educators in TESOL International Research"
odin_topics:
  - "1.A"
  - "1.B"
  - "1.C"
  - "2.A"
  - "2.D"
  - "3.A"
  - "3.B"
  - "4.A"
  - "5.A"
  - "7.A"
  - "13.A"
  - "13.B"
tldr: "Selected personnel of the Bureau of the Treasury demonstrate prudent financial management, with high agreement on financial planning, money management, and income protection, but only moderate engagement in investments."
problem_and_motivation: "Financial mismanagement among personnel threatens organizational success. This study addresses the gap in research on personal financial practices within the Bureau of the Treasury, providing a baseline assessment."
approach:
  - "A descriptive research design was employed to gather data from 183 personnel across 35 divisions of the Bureau of the Treasury."
  - "Simple random probability sampling was used to select the study respondents."
  - "A researcher-made questionnaire, validated with a Cronbach's Alpha of 0.896, was the primary instrument."
  - "Data collection involved survey administration over three weeks, supplemented by informal interviews."
  - "Analysis included descriptive statistics (frequency, percentage, weighted mean, ranking) and inferential statistics (T-test and one-way ANOVA)."
findings:
  - "num: 37.7% of respondents are aged 26 to 35 years old."
  - "num: 60.1% of respondents are female."
  - "num: 63.9% of respondents are single."
  - "num: 78.7% hold a bachelor's degree."
  - "num: 78.1% are rank-and-file employees."
  - "num: 86.9% are permanent employees."
  - "num: 53.0% have been in the agency for 5 years or less."
  - "num: 38.8% have a monthly compensation of P15,001-P30,000."
  - "Financial planning had the highest overall weighted mean of 4.26 among financial management aspects."
  - "Significant differences were found in financial practices based on age, civil status, employment status, and monthly compensation."
key_figures_tables:
  - "Table 10: Financial Planning practices → Highest rating for setting short- and long-term goals (WM=4.39)."
  - "Table 11: Money Management practices → Highest rating for saving to avoid borrowing (WM=4.47)."
  - "Table 12: Income and Asset Protection practices → Highest rating for considering future uncertainties (WM=4.30)."
  - "Table 13: Investments practices → Highest rating for purchasing government securities (WM=3.56)."
  - "Table 14: Summary of PFM practices → Financial Planning ranked first (WM=4.26), Investments last (WM=2.91)."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "PFMS"
    definition: "Personal Financial Management System"
  - term: "Bureau of the Treasury"
    definition: "National government agency responsible for managing government finances."
critical_citations:
  - "[Brounen et al., 2016] — Urges proactive personal financial planning."
  - "[Kassim et al., 2019] — Links saving ability to reduced financial stress."
  - "[Adeoye, 2019] — Finds compensation management does not affect motivation in Nigerian insurance sector."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "medium"
      justification: "The study's sample of government personnel provides a proxy for understanding the financial practices of a specific Filipino workforce segment."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "high"
      justification: "Provides detailed data on income, savings, and spending behaviors of Filipino government employees."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Directly measures and reports on financial planning, money management, and investment behaviors."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "medium"
      justification: "Highlights practices like saving to avoid borrowing and dependency on social media for financial influence, reflecting cultural financial norms."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "contextual"
      justification: "Mentions day-to-day cost of living as a primary concern, providing a backdrop for understanding spending patterns."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "low"
      justification: "The study groups financial practices into broad categories (planning, management, protection, investments) which can inform categorization."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      relevance: "low"
      justification: "The identified practices (e.g., buying necessities over wants) can be used to inform the design of spending categories."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "low"
      justification: "Provides context on current financial behaviors which any PFMS would need to address or improve."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "The study's findings on saving and spending habits (e.g., saving to avoid borrowing) are inputs for creating behavioral profiles."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "low"
      justification: "The reported practice of following a budget plan (WM=4.10) confirms budgeting as a key user activity."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "low"
      justification: "The emphasis on saving for emergencies and to avoid borrowing aligns with savings goal management features."
    - code: "13.B"
      name: "Debt Management in PFMS"
      relevance: "medium"
      justification: "The strong aversion to credit and borrowing directly informs the need for debt management features."
  contribution: "This study provides a baseline understanding of the financial management practices of Filipino government personnel. It identifies specific behaviors within financial planning, money management, income protection, and investments. These findings can inform the design of Odin's modules by highlighting user priorities, such as avoiding debt and planning for uncertainties, and revealing gaps like limited investment knowledge."
  directly_justifies:
    - "Financial planning, especially goal-setting, is a highly prioritized activity."
    - "Saving is a primary financial strategy used to avoid borrowing from others."
    - "Government employees are cautious about using credit and incurring debt."
    - "There is a gap in knowledge and engagement with investment products beyond basic securities."
    - "Demographic factors like age and civil status influence financial practices."
  limits:
    - "The study is limited to a single government agency (Bureau of the Treasury) in the Philippines. [unacknowledged]"
    - "The findings are based on self-reported data, which may be subject to social desirability bias. [unacknowledged]"
    - "The study does not employ a longitudinal design to understand how these practices evolve over time. [unacknowledged]"
    - "The research does not compare these practices to those of other demographics, limiting generalizability. [unacknowledged]"
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was conducted. The domains of 'Filipino Cultural Context', 'Expense Categorization', 'Existing Systems & Gaps', 'Behavioral Profiling', 'Budget Recommendation', and 'Savings & Debt Management' were flagged as relevant. Topic codes 1.B, 1.C, 2.A, and 5.A were assigned a 'high' relevance because the paper directly provides data on the financial behaviors and profile of Filipino workers. Codes 1.A, 2.D, 3.A, 3.B, 4.A, 7.A, 13.A, and 13.B were assigned 'medium' or 'low' relevance as they offer contextual or supporting insights. Domains related to algorithms (6.A/B, 7.C/D, 8.A/B/C, 12.B/C), mobile design (9.A/B), privacy (10.A/B), engagement (11.A/B), and system evaluation (12.A) were considered but rejected as the paper is a descriptive behavioral study, not an algorithmic or design-oriented paper. The paper's overall relevance to Odin lies in its provision of foundational behavioral data that can inform the user profile, budgeting strategies, and savings/debt management modules."
limitations:
  - "The study is limited to a single government agency, which restricts the generalizability of findings to all Filipino young professionals."
  - "The reliance on self-reported survey data may introduce bias and inaccuracies in measuring financial behaviors."
  - "The cross-sectional design prevents analysis of financial management dynamics and changes over time."
  - "The study does not explore the effectiveness of specific PFMS tools or interventions."
remember_this:
  - "Financial planning has the highest engagement among government personnel."
  - "Saving to avoid borrowing is a core money management strategy."
  - "Investment knowledge and participation are areas of significant weakness."
  - "Single and younger personnel show less engagement in financial management."
  - "The study provides a behavioral baseline for designing a Filipino PFMS."
```
---

## Paper 39: Martin et al_summarized.md

**Source File:** `Martin et al_summarized.md`

```yaml
paper_id: "6ba7b810-9dad-51d1-80b4-00c04fd430c8"
designation: "international-algorithm-specific"
title: "Adaptive Learning Architectures for Evolving Data Streams: Challenges and Advances"
authors: "Martin, C. E.; Lefèvre, H. A.; Dubois, C. R."
year: 2023
venue: "Adaptive Intelligence and Lifelong Systems"
odin_topics:
  - "5.A"
  - "5.B"
  - "6.A"
  - "6.B"
  - "7.B"
  - "8.A"
  - "8.B"
  - "12.A"
tldr: "Surveys adaptive learning for evolving data streams, addressing concept drift and catastrophic forgetting, and presents a drift-aware framework with selective memory replay that improves accuracy and retention."
problem_and_motivation: "Static models fail under non-stationary data distributions in real-world applications. Lifelong learning must balance plasticity and stability while retaining knowledge. Existing methods struggle with efficient drift detection and scalable memory management."
approach:
  - "Uses stream preprocessing with normalization and mini-batching for smooth intake."
  - "Detects drift via ADWIN statistical test and embedding cosine distance between hidden representations."
  - "Optimizes incrementally using a regularized loss with Elastic Weight Consolidation to prevent forgetting."
  - "Maintains a bounded rehearsal buffer with exemplar selection and similarity-based replay for recurring drift."
  - "Evaluates on RotatingMNIST, CIFAR-100 split, Electricity Pricing, and Airline Delay datasets."
  - "Compares against Naïve, EWC, LwF, GEM, and Experience Replay baselines."
findings:
  - "num: Our method achieves final average accuracies of 77.9%, 64.2%, 82.4%, and 77.3% on the four benchmarks."
  - "num: Backward transfer is -5.6% on RotatingMNIST and -7.2% on CIFAR-100, outperforming all baselines."
  - "num: Removing drift detection lowers accuracy by 3.1–5.7% in non-stationary settings."
  - "The framework maintains training time and memory usage comparable to Experience Replay and EWC."
  - "The combination of representation-based drift detection and selective replay yields a superior stability-plasticity balance."
key_figures_tables:
  - "Table 3: Final average accuracy (%) across tasks → Our method consistently outperforms baselines across all datasets."
  - "Table 4: Backward Transfer (BWT%) → Our method has the least negative BWT, indicating strong knowledge retention."
  - "Figure 3: Adaptive learning rate in dynamical environments → Dynamic drift-aware adjustment improves adaptation over static schedules."
key_equations:
  - equation: '\mathcal{L}_{total} = \mathcal{L}_{task} + \lambda \cdot \Omega'
    explanation: "Total loss with regularization term for stability."
  - equation: '\Omega = \frac{1}{2} \sum_i F_i (\theta_i - \theta_i^*)^2'
    explanation: "EWC penalty to prevent catastrophic forgetting."
  - equation: 'Drift_{rep} = \frac{1}{k} \sum_{t=k-d}^{k} (1 - \frac{h_t \cdot h_{k-d}}{\|h_t\|\|h_{k-d}\|})'
    explanation: "Embedding drift as cosine distance over a window."
  - equation: 'BWT = \frac{1}{T-1} \sum_{i=1}^{T-1} (A_{T,i} - A_{i,i})'
    explanation: "Backward transfer measures forgetting on previous tasks."
definitions:
  - term: "Concept drift"
    definition: "Change in the underlying data distribution over time."
  - term: "Catastrophic forgetting"
    definition: "Loss of performance on previously learned tasks when learning new ones."
  - term: "ADWIN"
    definition: "Adaptive sliding window algorithm for detecting change in data streams."
  - term: "EWC"
    definition: "Elastic Weight Consolidation; a regularization method to prevent forgetting."
  - term: "BWT"
    definition: "Backward transfer; a metric for forgetting."
  - term: "LwF"
    definition: "Learning without Forgetting; a method to retain knowledge."
  - term: "GEM"
    definition: "Gradient Episodic Memory; a continual learning algorithm."
  - term: "ER"
    definition: "Experience Replay; a memory rehearsal technique."
critical_citations:
  - "[Kirkpatrick et al., 2017] — Introduces EWC as a regularization method."
  - "[Gama et al., 2014] — Comprehensive survey on concept drift adaptation."
  - "[Lopez-Paz and Ranzato, 2017] — Proposes GEM for continual learning."
  - "[Rolnick et al., 2019] — Experience replay for continual learning."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Adaptive modeling can capture evolving spending habits over time."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "medium"
      justification: "Incremental learning techniques help initialize profiles from limited data."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Directly addresses forecasting under changing data distributions."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Proposed methods for sequential stream learning are applicable to spending sequences."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Adaptive recommendations can adjust to shifting income and expense patterns."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Drift-aware detection is critical for identifying new types of anomalies."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "The paper's algorithms can be adapted for spending anomaly detection."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides evaluation metrics like backward transfer suitable for adaptive systems."
  contribution: "This paper's drift detection and adaptive optimization can inform Odin's spending forecasting module to handle seasonal changes. Its memory replay strategy may enhance anomaly detection by retaining knowledge of past normal behavior while adapting to new patterns. The evaluation framework with backward transfer metrics offers a way to test Odin's recommendation system over time. The proposed modular architecture supports efficient updates on mobile devices, aligning with Odin's mobile-first design."
  directly_justifies:
    - "Adaptive models with drift detection improve accuracy by 3-5% in non-stationary data."
    - "Selective memory replay reduces catastrophic forgetting by up to 60% compared to naive incremental learning."
    - "Embedding-based drift detection is effective for gradual and recurring concept drift."
  limits:
    - "None identified."
  mapping_rationale: "A systematic scan across all 12 functional domains identified relevance primarily in Forecasting (6.A, 6.B) and Anomaly Detection (8.A, 8.B) due to the paper's focus on concept drift and sequential learning. Behavioral Profiling (5.A, 5.B) and Budget Recommendation (7.B) were deemed medium relevance as the methods support dynamic user modeling. Evaluation (12.A) is medium because the paper includes performance metrics. Domains related to Filipino cultural context, expense categorization, existing systems, mobile design, data privacy, retention, savings, and debt were rejected because the paper does not address these aspects. Borderline cases included 5.C (classification approaches) and 8.C (cold-start baselines), but these were not directly discussed, so they were excluded. Overall, the paper provides strong algorithmic foundations for adaptive modules in Odin."
limitations:
  - "Tested only on non-financial benchmarks; applicability to personal spending data is unvalidated. [unacknowledged]"
  - "Assumes labeled data; Odin may rely on user-labeled categories but also has unlabeled transactions. [unacknowledged]"
  - "Computational overhead of drift detection may be high for mobile deployment; not addressed."
remember_this:
  - "Adaptive learning with drift detection improves accuracy in non-stationary environments."
  - "Our method reduces backward transfer error by 78% relative to naive incremental learning."
  - "Embedding-based drift detection captures gradual and recurring changes effectively."
  - "The framework maintains competitive efficiency suitable for online deployment."
```
---

## Paper 40: Williams et al_summarized.md

**Source File:** `Williams et al_summarized.md`

```yaml
paper_id: 10.1109/ACCESS.2023.3317791
designation: international-algorithm-specific
title: Anomaly Detection in Multi-Seasonal Time Series Data
authors: Williams, A. T.; Sperl, R. E.; Chung, S. M.
year: 2023
venue: IEEE Access
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 2.B
tldr: Extends SARIMA to model multiple seasonal patterns, improving anomaly detection accuracy in time series data with two seasonalities.
problem_and_motivation: Most forecasting models for anomaly detection incorporate only one seasonal component, failing to capture multiple known seasonal patterns common in real-world data. This limitation reduces anomaly detection accuracy in datasets with multiple seasonalities, such as daily and weekly cycles.
approach:
  - Proposes multi-SARIMA, a model that extends SARIMA to incorporate two seasonal periods using a derived equation combining two SARIMA models.
  - Evaluates on three datasets containing two meaningful seasonal trends: NYC Taxi, a synthetic dataset, and a smaller version of Numenta's HotGym.
  - Compares multi-SARIMA against MA, SIMA, SARIMA, HTM, and TBATS in single-step and two-step (with MA/SIMA as first step) anomaly detection settings.
  - Uses a dynamic anomaly score threshold based on Mean Absolute Deviation (MAD) to label data points.
  - Validates seasonal components in datasets using Multiple Seasonal-Trend decomposition using Loess (MSTL).
findings:
  - num: Multi-SARIMA achieved the highest true positives for every dataset while maintaining fewer false positives than SARIMA.
  - num: Multi-SARIMA doubled the true positive rate of HTM and TBATS for the HotGym dataset.
  - num: Multi-SARIMA had the highest runtime among models due to training on two seasonal periods.
  - num: Two-step approach with MA + multi-SARIMA significantly reduced false positives compared to standalone multi-SARIMA for all datasets.
  - num: TBATS outperformed SARIMA and HTM but was outperformed by multi-SARIMA in two of three datasets.
key_figures_tables:
  - "Table 1: Overview of datasets → Shows datasets with two meaningful seasonal trends and hand-labeled anomalies."
  - "Figure 1: MSTL decomposition of NYC Taxi dataset → Confirms daily and weekly seasonal patterns in taxi traffic."
  - "Figure 2: MSTL decomposition of Synthetic dataset → Confirms daily and weekly seasonal patterns simulating a work schedule."
  - "Figure 3: MSTL decomposition of HotGym dataset → Confirms daily and weekly patterns in gym energy consumption."
  - "Table 2: Single-step experimental results → Multi-SARIMA has highest true positives and competitive false positives across datasets."
  - "Table 3: Two-step experimental results → Multi-SARIMA as second step reduces false positives while maintaining true positives."
key_equations:
  - equation: |
      X_t = ∇_{m_2}^{d_2} X_t + \sum_{i=0}^{d_2-1} B^{m_2} \nabla_{m_2}^{i} X_t
    explanation: "Reconstructs original time series from the differenced series."
  - equation: |
      \nabla_{m_2}^{d_2} X_t = (\sum_{i=1}^{p_1} a_{1,i} B^{m_1 i}) \nabla_{m_2}^{d_2} X_t + (\sum_{i=1}^{p_2} a_{2,i} B^{m_2 i}) \nabla_{m_2}^{d_2} X_t - (\sum_{j=1}^{p_2} \sum_{i=1}^{p_1} a_{1,i} a_{2,j} B^{m_1 i + m_2 j}) \nabla_{m_2}^{d_2} X_t + \epsilon_t
    explanation: "Multi-SARIMA equation combining two seasonal AR and MA components."
definitions:
  - term: Multi-SARIMA
    definition: Extension of SARIMA that incorporates two seasonal components to improve anomaly detection.
  - term: TBATS
    definition: Trigonometric seasonality, Box-Cox transformation, ARMA errors, Trend, and Seasonal components model for multi-seasonal forecasting.
  - term: MAD (Mean Absolute Deviation)
    definition: A robust metric for calculating dynamic anomaly threshold, insensitive to outliers.
  - term: MSTL (Multiple Seasonal-Trend decomposition using Loess)
    definition: Decomposition method for time series with multiple seasonal patterns.
  - term: SDR (Sparse Distributed Representations)
    definition: Vectors with thousands of bits representing semantic properties, used in HTM.
critical_citations:
  - "[Bandara et al., 2021] — Source for MSTL decomposition algorithm."
  - "[De Livera et al., 2011] — Source for TBATS forecasting model."
  - "[Sperl and Chung, 2019] — Proposed the two-step anomaly detection approach."
  - "[Hyndman and Athanasopoulos, 2021] — Standard reference for SARIMA models."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: "Directly addresses forecasting models for sequential spending data."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: "Proposes multi-SARIMA, a novel forecasting algorithm for multi-seasonal data."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: "Core focus is anomaly detection in time series data with multiple seasonalities."
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: "Evaluates and compares multiple anomaly detection algorithms including the proposed multi-SARIMA."
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: "The paper focuses on multi-seasonal patterns, applicable to cyclical spending in personal finance."
  contribution: "The multi-SARIMA model provides a mathematical framework for Odin's anomaly detection module to handle user spending data with multiple seasonal cycles (e.g., daily and weekly). The two-step approach with multi-SARIMA offers a strategy to optimize Odin's prediction engine for accuracy and runtime, balancing performance and resource constraints for mobile users. The experimental methodology demonstrates how to validate seasonal components and evaluate forecasting models, guiding Odin's model selection and tuning. The paper's findings on TBATS and SARIMA inform the choice of baseline algorithms for comparison in Odin's system evaluation."
  directly_justifies:
    - "Multi-seasonal forecasting improves anomaly detection accuracy in time series data."
    - "Two-step anomaly detection can reduce false positives while maintaining true positive rates."
    - "SARIMA can be extended to incorporate multiple seasonal patterns using the derived multi-SARIMA equation."
  limits:
    - "Increased processing time for multi-SARIMA due to training on two seasonal periods."
    - "Multi-SARIMA is designed for two seasonal periods; performance with more than two is not evaluated."
    - "The two-step approach is limited by the true positive rate of the first-step model. [unacknowledged]"
  mapping_rationale: "All 12 functional domains and their associated topic codes were systematically scanned. The paper was flagged as highly relevant to the 'Spending Forecasting' and 'Anomaly Detection' domains, specifically topics 6.A, 6.B, 8.A, and 8.B, due to its core contribution of a novel multi-seasonal forecasting model for anomaly detection. Topic 2.B (Seasonal and Cyclical Spending Patterns) was marked as medium relevance because the paper's focus on multiple seasonalities provides a contextual basis for understanding spending cycles, but it does not directly address Filipino cultural practices. The 'Budget Recommendation' domain (topics 7.A-7.D) was considered but rejected because the paper does not involve budget allocation or optimization. The 'Mobile-First Design' and 'Data Privacy' domains were rejected as they are not addressed. The overall relevance is high because the paper provides a directly applicable algorithmic approach for detecting anomalies in multi-seasonal spending data, a key requirement for Odin's core functionality."
limitations:
  - "Multi-SARIMA has higher runtime compared to single-season models."
  - "The model assumes pre-determined seasonal periods, which may not be known a priori for all datasets."
  - "Performance is not guaranteed if seasonal patterns are insignificant or datasets have more than two seasonalities."
  - "Experimental evaluation limited to three datasets, two of which are from the Numenta Anomaly Benchmark. [unacknowledged]"
  - "Comparison with deep learning methods like TCN is noted as future work, leaving a gap in benchmarking against state-of-the-art neural approaches. [unacknowledged]"
remember_this:
  - "Multi-SARIMA extends SARIMA to model two seasonal patterns for better anomaly detection."
  - "It achieved the highest true positives while maintaining fewer false positives than SARIMA."
  - "The two-step approach with multi-SARIMA significantly reduces false positives."
  - "Multi-SARIMA doubled the true positive rate of HTM and TBATS on the HotGym dataset."
  - "Increased accuracy comes with higher runtime due to training on two seasonal periods."
```
---

## Paper 41: Cheng et al_summarized.md

**Source File:** `Cheng et al_summarized.md`

```yaml
paper_id: "10.3389/fpsyg.2023.1162916"
designation: "international"
title: "Influences of mental accounting on consumption decisions: asymmetric effect of a scarcity mindset"
authors: "Cheng, L.; Yu, Y.; Wang, Y.; Zheng, L."
year: 2023
venue: "Frontiers in Psychology"
odin_topics:
  - "1.C"
  - "3.B"
  - "5.A"
  - "5.B"
tldr: "Consumers prefer hedonic spending from windfall gains, but a high scarcity mindset diminishes this preference; hard-earned money consistently drives utilitarian spending."
problem_and_motivation: "The influence of mental accounting on hedonic versus utilitarian consumption is well-documented, yet the moderating role of a scarcity mindset remains unclear. Understanding this interaction is critical for predicting consumer choices under different income sources. Prior research has not systematically examined how perceived resource scarcity alters the mental accounting effect on spending preferences."
approach:
  - "Conducted two online between-subject experiments with student (N=319) and adult (N=294) samples."
  - "Manipulated mental account as windfall gains versus hard-earned money."
  - "Measured scarcity mindset using a three-item self-report scale (Pitesa and Thau, 2018)."
  - "Participants chose between hedonic (e.g., dinner at restaurant) and utilitarian (e.g., canteen card) products."
  - "Used chi-square tests to compare choice proportions and logistic regression to test moderation."
findings:
  - "Windfall gains significantly increased preference for hedonic over utilitarian consumption in both samples (student: χ²=33.45, p<0.001; adult: χ²=10.30, p=0.001)."
  - "num: Scarcity mindset moderated the windfall effect, reducing hedonic preference under high scarcity (student: B=-0.66, p=0.026; adult: B=-1.28, p<0.001)."
  - "No moderation was found for hard-earned money on hedonic vs utilitarian choice."
  - "Adults showed a stronger overall utilitarian preference, possibly due to larger windfall amounts and cultural thrift."
key_figures_tables:
  - "Figure 1: Bar charts of choice proportions by mental account and sample → Windfall boosts hedonic choice; hard-earned boosts utilitarian."
  - "Figure 2: Interaction plots of scarcity mindset and mental account → High scarcity reduces hedonic preference only for windfall gains."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Mental accounting"
    definition: "Cognitive operations that categorize and evaluate financial activities, treating money as nonfungible."
  - term: "Scarcity mindset"
    definition: "Belief that resources are limited, focusing attention on scarcity and influencing decisions."
  - term: "Hedonic consumption"
    definition: "Consumption aimed at pleasure and experiential enjoyment."
  - term: "Utilitarian consumption"
    definition: "Consumption aimed at functional, practical goals."
critical_citations:
  - "[Thaler, 1985] — foundational mental accounting theory."
  - "[Thaler, 1999] — formalized mental accounting framework."
  - "[Mani et al., 2013] — scarcity mindset impairs cognitive function."
  - "[Cheema and Soman, 2006] — malleable mental accounting."
relevance:
  topics:
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "contextual"
      justification: "General consumer behavior findings may inform understanding of Filipino spending patterns."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      relevance: "medium"
      justification: "Distinction between hedonic and utilitarian expenses is relevant for category design."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Directly examines how mental accounting and scarcity mindset shape spending preferences, key for profiling."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "medium"
      justification: "Shows that spending preferences vary with mindset, indicating dynamic profile factors useful for cold-start."
  contribution: "This paper informs Odin's user behavioral profiling module by demonstrating that mental accounting and scarcity mindset significantly influence spending choices. It supports the design of expense categorization that distinguishes hedonic from utilitarian purchases. The moderation effect suggests that Odin's recommendation algorithms should adapt to users' perceived scarcity levels. Additionally, the findings provide a basis for cold-start profiling by using income source and scarcity mindset as early indicators."
  directly_justifies:
    - "Windfall gains increase hedonic spending relative to utilitarian."
    - "Scarcity mindset reduces the tendency to spend windfalls on hedonic items."
    - "Hard-earned money is consistently allocated to utilitarian purchases, regardless of scarcity mindset."
  limits:
    - "The study uses self-reported scarcity mindset, not a direct manipulation."
    - "Samples are from China, limiting cultural generalizability to Filipinos."
    - "No field experiment to validate real-world spending behavior."
    - "Amount of windfall differs between student and adult samples, confounding comparisons. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains and associated topic codes identified three domains as relevant: Behavioral Profiling (5.A, 5.B), Expense Categorization (3.B), and Financial Behavior (1.C). The paper directly addresses how mental accounting and scarcity mindset affect spending choices, providing high relevance for 5.A and medium for 5.B and 3.B. The Filipino cultural context domains (2.A-D) were considered but rejected because the study was conducted in China and does not address Filipino-specific practices. Spending forecasting, budget recommendation, anomaly detection, mobile-first design, data privacy, retention, evaluation, and savings/debt domains were not directly informed by the paper's findings."
limitations:
  - "Self-reported scarcity mindset may not capture actual resource constraints."
  - "The experimental scenarios may not reflect real-world spending decisions."
  - "Cultural context (China) limits applicability to Philippine users. [unacknowledged]"
  - "The study does not examine long-term effects of scarcity mindset on budgeting behavior. [unacknowledged]"
remember_this:
  - "Windfall gains significantly boost hedonic spending over utilitarian."
  - "High scarcity mindset reduces hedonic preference for windfall money."
  - "Hard-earned money consistently favors utilitarian purchases."
  - "Adults show stronger utilitarian preference than students."
  - "Scarcity mindset moderates mental accounting effects with p<0.001."
```
---

## Paper 42: Polinar et al_summarized.md

**Source File:** `Polinar et al_summarized.md`

```yaml
paper_id: "e3f4c9a2-1b5c-4d8e-9f0a-7c6b5d4e3f2a"
designation: "local"
title: "Knowledge and Practice of Personal Finance of Non-Teaching Staff in a Private University in Cebu City"
authors: "Rico, M. E.; Polinar, M. A. N.; Celada, J. A."
year: 2023
venue: "International Journal of Multidisciplinary: Applied Business and Education Research"
odin_topics:
  - "1.A"
  - "1.B"
  - "1.C"
  - "2.A"
  - "3.A"
  - "3.B"
  - "4.A"
  - "4.B"
  - "5.A"
  - "5.B"
  - "13.A"
  - "13.B"
tldr: "Non-teaching staff in a Cebu private university demonstrate moderate personal finance knowledge and practice, with weak emergency fund and investment behaviors showing no correlation with knowledge."
problem_and_motivation: "Filipinos demonstrate low financial literacy, with only 25% understanding basic concepts, and the pandemic has worsened financial instability. Limited research exists on the personal finance practices of non-teaching staff in Philippine universities, leaving a gap in understanding their financial behaviors and needs."
approach:
  - "Descriptive-correlational design with 50 non-teaching staff respondents selected via simple random sampling from a private Cebu university."
  - "Adopted survey questionnaire measuring knowledge and practice across budgeting, saving/spending, emergency funds, debt, insurance, and investment using a 4-point Likert scale."
  - "Data collected through printed and Google Forms questionnaires during the COVID-19 pandemic, with ethical protocols followed."
  - "Statistical analysis employed weighted means for descriptive measures and Pearson correlation for relationships between knowledge and practice."
  - "Respondents were permanent staff with at least one year of service, ensuring relevant work tenure."
findings:
  - "num: Respondents demonstrated moderate overall personal finance knowledge (grand mean: 3.10) and practice (grand mean: 2.71)."
  - "Budgeting and saving/spending knowledge were rated 'Highly Knowledgeable' (means: 3.29, 3.32), while investment knowledge was lowest (2.56)."
  - "Emergency fund and investment practice were 'Less Practiced' (means: 2.42, 2.20), indicating weak behavioral execution."
  - "Significant positive correlations existed between knowledge and practice for budgeting (r=0.939), saving/spending (r=0.839), insurance (r=0.969), and investment (r=0.973)."
  - "No significant relationship was found between knowledge and practice for emergency funds (r=0.875, p=0.052) and debt management (r=0.806, p=0.053)."
  - "The researchers developed an action plan called 'Solidifying Personal Finance in a Teknoy Way' to address weak areas."
  - "Recommendations include seminars, workshops, and using prior outputs like 'Every Centavo Counts' to enhance financial literacy."
  - "Potential future research directions include qualitative exploration and studying other variables like money mindset and retirement planning."
key_figures_tables:
  - "Table 3: Knowledge means for six indicators → Emergency fund and investment knowledge are moderate, investment knowledge is lowest."
  - "Table 4: Practice means for six indicators → Emergency fund and investment practice are poor, indicating weak execution."
  - "Table 5: Pearson correlations for all six variables → Strong correlations for budgeting, saving/spending, insurance, and investment; no correlation for emergency fund and debt management."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "BSP"
    definition: "Bangko Sentral ng Pilipinas, the central bank of the Philippines."
  - term: "MSMEs"
    definition: "Micro, Small, and Medium Enterprises."
  - term: "PFMS"
    definition: "Personal Finance Management System."
  - term: "COVID-19"
    definition: "Coronavirus disease 2019, a global pandemic."
critical_citations:
  - "[Polinar et al., 2022] — Found significant correlation between financial knowledge and practice among public school teachers."
  - "[Bangko Sentral ng Pilipinas, 2021] — Revealed low financial literacy rates and poor emergency saving habits in the Philippines."
  - "[Guliman, 2015] — Showed low financial knowledge among MSME owners, supporting the need for targeted interventions."
  - "[Mouna & Anis, 2016] — Established that financial literacy significantly influences investment decisions."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "medium"
      justification: "Studies non-teaching staff, a subset of Filipino professionals, providing demographic context."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "medium"
      justification: "Examines budgeting, saving, and spending behaviors relevant to financial structure."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "medium"
      justification: "Assesses actual financial practices, offering insights into behavioral patterns."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "medium"
      justification: "Discusses Filipino cultural practices like 'paluwagan' and spending-before-saving mentality."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "low"
      justification: "Mentions budgeting and spending categories but does not propose a categorization framework."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      relevance: "low"
      justification: "Briefly touches on expense categories without deep design analysis."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "References BSP surveys and national financial literacy levels, providing macro-context."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Identifies gaps in financial knowledge and practice among non-teaching staff."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Examines knowledge-practice relationships, informing behavioral profiling."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "low"
      justification: "Provides baseline knowledge and practice data useful for initial user profiling."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "medium"
      justification: "Addresses saving and spending practices, directly relevant to savings goal management."
    - code: "13.B"
      name: "Debt Management in PFMS"
      relevance: "medium"
      justification: "Includes debt management as a key variable, with findings on knowledge-practice correlation."
  contribution: "This paper provides empirical baseline data on Filipino non-teaching staff's financial knowledge and practice, directly informing Odin's user profiling and behavioral assessment modules. The finding that knowledge and practice are correlated for budgeting and saving supports Odin's educational feature design, while the weak correlation for emergency funds and investment highlights areas needing behavioral nudges and simplified goal-setting interfaces. The identified gaps in emergency savings and investment practices justify Odin's focus on automated savings features and investment literacy tools. The action plan framework suggests concrete design directions for engagement and retention mechanisms."
  directly_justifies:
    - "Knowledge of budgeting and saving is significantly correlated with practice among Filipino non-teaching staff."
    - "Emergency fund and investment knowledge do not translate to practice, requiring targeted behavioral interventions."
    - "Financial literacy programs should address both knowledge and behavioral execution for effective PFMS design."
    - "Non-teaching staff exhibit weak investment practices, justifying simplified investment guidance in PFMS."
  limits:
    - "Small sample size (n=50) from a single private university limits generalizability to all Filipino professionals."
    - "Cross-sectional design prevents causal inference between knowledge and practice."
    - "Focus on non-teaching staff excludes teaching faculty and other professional groups."
    - "Self-reported data may introduce social desirability bias in financial responses."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant to the Filipino Cultural Context domain (codes 2.A, 2.B, 2.C, 2.D) due to its focus on Filipino spending practices and cultural financial behaviors. It also maps to Expense Categorization (3.A, 3.B) through its budgeting and spending indicators, and to Existing Systems & Gaps (4.A, 4.B) by referencing national financial literacy surveys. The Behavioral Profiling domain (5.A, 5.B) is relevant given the knowledge-practice correlation analysis. Savings & Debt Management (13.A, 13.B) is directly addressed through emergency fund and debt indicators. The paper was considered for Forecasting (6.A, 6.B) and Anomaly Detection (8.A, 8.B) but rejected as it does not involve predictive algorithms. Similarly, Budget Recommendation (7.A-D) and Mobile-First Design (9.A-B) were rejected due to no discussion of budget optimization or UX. Data Privacy (10.A-B) and Retention (11.A-B) were not addressed. Overall relevance is medium, providing foundational behavioral insights for Odin's profiling and educational modules, though not directly contributing to algorithmic design."
limitations:
  - "Small sample size from a single university limits generalizability [unacknowledged]."
  - "Cross-sectional design prevents establishing causation between knowledge and practice."
  - "Self-reported data may be subject to social desirability bias."
  - "No qualitative exploration of reasons behind weak emergency fund and investment practices [unacknowledged]."
remember_this:
  - "Knowledge and practice are correlated for budgeting, saving, insurance, and investment."
  - "Emergency fund and investment knowledge do not predict practice among respondents."
  - "Investment practice was lowest, with a mean score of 2.20 out of 4."
  - "Moderate financial literacy requires targeted behavioral interventions, not just education."
  - "Action plans should address the gap between knowledge and execution for emergency funds."
```
---

## Paper 43: Co & Centeno_summarized.md

**Source File:** `Co & Centeno_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: local
title: Effects of Filipino Consumers' Financial Attitudes, Subjective Norms, and Perceived Behavioral Control on Intentions to Formal Banking: Towards Financial Inclusion
authors: Co, M.; Centeno, D.D.G.
year: 2023
venue: Philippine Management Review
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.D
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 7.A
  - 7.B
  - 12.A
  - 12.B
  - 13.A
  - 13.C
tldr: Subjective norms and perceived behavioral control significantly predict Filipino intentions to save surplus money in formal banks, while general attitudes do not.
problem_and_motivation: Financial exclusion among Filipinos is often attributed to supply-side factors like cost and access, but the psychological and behavioral drivers on the demand side remain underexplored in local research. This gap limits the effectiveness of financial inclusion strategies that fail to address individual attitudes, social influences, and perceived behavioral control over saving. The paper aims to quantify how these factors affect intentions to use formal banking services.
approach:
  - Data from the 2014 Bangko Sentral ng Pilipinas Consumer Finance Survey with 15,503 households was analyzed.
  - A logistic regression model was constructed to predict the intention to deposit surplus money in a bank.
  - Independent variables included attitudes, subjective norms, perceived behavioral control, and demographic factors.
  - Subjective norm was proxied by the presence of a banked household member, and behavioral control by two survey items on saving capability.
  - Marginal effects were estimated using the delta method to interpret the predictors' influence.
findings:
  - num: Presence of a banked household member increases the probability of banking intention by 10.16 percentage points.
  - num: Perceived behavioral control statements significantly affect intention, with one item increasing probability by 1.42% and another decreasing it by 2.54%.
  - num: College graduates are 7.95 percentage points more likely to intend banking than non-graduates.
  - num: Males are 2.02 percentage points more likely to intend banking than females.
  - num: Middle-income individuals are 3.18 percentage points more likely than low-income to intend banking, while high-income individuals are 10.14 percentage points less likely.
  - Attitudes towards banking, though directionally consistent, were not a statistically significant predictor of intention.
  - Older generations (Baby Boomers) showed lower intention compared to Millennials.
  - Employment status was negatively associated with banking intention, contrasting with initial hypotheses.
key_figures_tables:
  - Table 1: Response rates of the household survey → 86.1% overall response rate from a sample of 18,000 households.
  - Table 2: Descriptive statistics of the sample → 87.6% of respondents are unbanked, but 41.2% express deposit intention.
  - Table 3: Logistic regression results → Subjective norms and perceived behavioral control are significant predictors of banking intention.
  - Table 4: Marginal effects of independent variables → Presence of a banked household member has the strongest marginal effect (10.16%).
key_equations:
  - equation: 'Logit(P(Bank)) = α + β1X1 + β2X2 + … + βkXk'
    explanation: Logistic model predicting probability of banking intention from independent variables.
definitions:
  - term: Theory of Planned Behavior
    definition: Framework linking attitudes, subjective norms, and perceived behavioral control to behavioral intentions.
  - term: Subjective norm
    definition: Perceived social pressure to perform or not perform a behavior, proxied by the presence of a banked family member.
  - term: Perceived behavioral control
    definition: One's perception of ease or difficulty in performing a behavior, measured through statements about earning and saving.
  - term: Financial inclusion
    definition: State of effective access to quality, responsive financial products and services for all sectors.
critical_citations:
  - '[Ajzen, 1991] — Foundational theory linking behavioral control to intention.'
  - '[BSP, 2014] — Primary data source for the nationwide consumer finance survey.'
  - '[Croson & Gneezy, 2009] — Documented gender differences in financial risk and behavior.'
  - '[Bandura, 1971] — Social learning theory underpinning the role of household influence.'
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Paper analyzes banking intentions across age, income, and education, directly profiling this demographic.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Examines income, employment, and household size as predictors of banking behavior.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly investigates the financial behavioral intentions of Filipinos towards formal banking.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Discusses social norms and family influence in a collectivist Filipino context.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Tangentially related through the focus on surplus money, but not a primary focus.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Describes the current status of financial inclusion and banking penetration in the Philippines.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies supply-side barriers (cost, access) and the gap in understanding demand-side psychological factors.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Uses TPB to segment and predict behavioral intentions based on psychological variables.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: low
      justification: Provides baseline demographic and behavioral data relevant to profiling, but not directly about cold-start dynamics.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses logistic regression to classify individuals based on their intention to use banking services.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: Provides background on saving behavior, a prerequisite for budgeting, but does not discuss specific strategies.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Offers insight into determinants of saving, which could inform budget recommendation systems.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: low
      justification: The logistic model serves as an evaluation framework for understanding banking behavior.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: low
      justification: The logistic regression can be considered a module for behavioral prediction.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: Directly studies the intention to save surplus money, the core input for savings goal management.
    - code: 13.C
      name: End-of-Period Surplus as a Savings Input
      relevance: medium
      justification: The dependent variable is precisely the intention to allocate end-of-period surplus to a bank.
  contribution: "The paper provides empirical evidence linking the Theory of Planned Behavior to banking intentions, which justifies Odin's use of behavioral factors in its profiling module. Findings on the predictive power of subjective norms and perceived behavioral control over general attitudes will directly inform Odin's survey design and initial user segmentation. The study's focus on surplus money as a primary savings input validates Odin's core assumption that identifying surplus is the first step in budget recommendation. The methodology using nationwide survey data offers a baseline for evaluating Odin's own recommendation algorithms against real-world behavioral patterns."
  directly_justifies:
    - "Subjective norms, proxied by the presence of a banked family member, are a strong predictor of banking intention."
    - "Perceived behavioral control over earning and saving significantly influences the intention to save surplus money."
    - "Higher educational attainment, being male, and younger age are associated with increased banking intention."
    - "Middle-income individuals have higher banking intentions than low or high-income groups."
  limits:
    - "The study uses intention as the dependent variable, not actual banking behavior, which limits the direct prediction of user actions."
    - "Data is from 2014, which may not reflect current post-pandemic digital banking adoption trends."
    - "The cross-sectional design cannot establish causality between psychological factors and banking intentions."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to the 'Behavioral Profiling & Classification' (5.A) and 'Filipino Cultural Context' (2.A) domains because it applies the Theory of Planned Behavior to a Filipino sample, providing a validated behavioral model. It also offers medium relevance to 'Expense Categorization' (3.A) and 'Savings & Debt Management' (13.A) through its focus on surplus money as the financial input for banking. The topics 6.A (Forecasting) and 8.A (Anomaly Detection) were considered but rejected as the paper does not involve predictive modeling or anomaly detection. Topic 4.A (Existing Systems) was selected for its detailed description of the Philippine financial landscape. Topic 9.A (Mobile-First Design) was rejected, as mobile design is not discussed. The overall relevance is high for informing Odin's behavioral profiling, user segmentation, and the initial design of the budgeting module based on actual Filipino behavioral predictors."
limitations:
  - "The study relies on self-reported behavioral intentions rather than observed financial behaviors, limiting the predictive validity for actual actions."
  - "Data are from 2014 and may not capture changes in financial behavior or attitudes due to post-pandemic digital financial services."
  - "The logistic model has a low Pseudo R2 (0.0094), indicating that many other unmeasured factors influence banking intentions."
  - "The study does not account for the potential mediating role of financial literacy or trust in the relationship between attitudes and intentions. [unacknowledged]"
  - "The treatment of perceived behavioral control uses only two items, which may not fully capture the construct's multi-dimensional nature. [unacknowledged]"
remember_this:
  - "Family influence is a 10.16% stronger predictor of banking intention than general attitudes."
  - "Perceived control over earning and saving is more important than positive attitudes towards banking."
  - "College graduates are 7.95 percentage points more likely to intend to use formal banking."
  - "Unbanked middle-income Filipinos have higher banking intentions than low or high-income groups."
  - "Attitude-intention inconsistency suggests behavioral control and social norms mediate the link."
```
---

## Paper 44: Asemi et al-2023_summarized.md

**Source File:** `Asemi et al-2023_summarized.md`

```yaml
paper_id: 10.1186/s40537-023-00784-7
designation: international-algorithm-specific
title: Adaptive neuro-fuzzy inference system for customizing investment type based on the potential investors' demographics and feedback
authors: Asemi, A.; Asemi, A.; Ko, A.
year: 2023
venue: Journal of Big Data
odin_topics:
  - 1.A
  - 1.B
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 6.A
  - 7.A
  - 7.B
tldr: An ANFIS-based recommender system uses investor demographics and feedback to suggest personalized investment types through clustering and fuzzy inference.
problem_and_motivation: Existing investment recommender systems often overlook the combination of demographic data and investor feedback for personalization. A gap exists in utilizing adaptive neuro-fuzzy inference to dynamically recommend investment types based on these factors. This study addresses the need for a more tailored and expert-informed investment advisory tool.
approach:
  - Data was collected via an online questionnaire from 1,542 potential investors, covering six demographic attributes and investment type preferences.
  - K-Means clustering in JMP grouped investment types into three clusters based on respondent answers to investment product questions.
  - Demographic data (gender, age, location, education, job, income) served as six inputs to an Adaptive Neuro-Fuzzy Inference System (ANFIS).
  - The ANFIS, designed with a Sugeno-type FIS and hybrid learning algorithm, generated 1,296 fuzzy rules to map demographics to investment type clusters.
  - The system was trained and tested using MATLAB, with provisions for incorporating expert rules and user feedback to refine recommendations.
findings:
  - num: 1,296 fuzzy rules were generated by the ANFIS system to recommend investment types based on demographic inputs.
  - num: The system achieved an average testing error of 0.86683 after 3 training epochs with 1,542 data pairs.
  - Three distinct investor clusters were identified, each with unique investment product preferences, such as stocks, mutual funds, and government bonds.
  - Demographic factors like age, income, and location were shown to influence investment type cluster membership in 3D surface plots.
  - The system allows for manual addition, modification, or deletion of rules by experts and based on investor feedback, enabling continuous improvement.
key_figures_tables:
  - Table 1: Conceptual stages of research → Outlines data collection, clustering, ANFIS, and feedback phases.
  - Table 2: Questions and answers for investment type → Maps survey responses to coded data for clustering.
  - Table 3: MFs of the Demographic ANFIS inputs → Lists membership functions for each demographic input.
  - Figure 13: Training DemographicANFIS → Shows the training process and final error of 0.8668.
  - Figure 15: The rule viewer → Displays the 1,296 generated fuzzy rules.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: ANFIS
    definition: Adaptive Neuro-Fuzzy Inference System, a hybrid system combining neural networks and fuzzy logic.
  - term: Membership Function (MF)
    definition: A function that maps an input value to a degree of membership in a fuzzy set.
  - term: K-Means Clustering
    definition: An unsupervised machine learning algorithm used to partition data into K distinct clusters.
  - term: Sugeno Fuzzy Model
    definition: A fuzzy inference system where the output is a constant or linear function of the inputs.
critical_citations:
  - "[Jang, 1993] — Introduced the ANFIS methodology used in this study."
  - "[Asemi & Ko, 2021] — Previous work on business recommender systems using feedback."
  - "[Kanaujia et al., 2017] — Established the need for tailored recommender systems."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Provides a general framework for using demographics in recommender systems, which can be adapted to Filipino context.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: contextual
      justification: The focus on demographic factors like income and education is relevant to understanding financial structure.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Reviews existing investment recommender systems, providing a baseline for comparison.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Explicitly identifies the gap of not using ANFIS and demographics together for investment recommendations.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly uses demographic and investment preference data to create clusters (behavioral profiles).
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Employs K-Means clustering and ANFIS as specific classification approaches for investor profiles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: The ANFIS model is a predictive system that recommends investment types based on input data.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: The paper's use of expert knowledge to generate rules parallels the incorporation of domain knowledge in budgeting.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: The recommendation logic (IF-THEN rules) can be adapted for budget recommendations, though not the paper's focus.
  contribution: "The paper provides a validated methodology for creating a demographic-based recommendation engine using ANFIS, which can be directly adapted for Odin's behavioral profiling module (5.A, 5.C). Its approach to integrating expert rules and user feedback offers a design pattern for Odin's budget recommendation system (7.B) to handle infeasibility (7.D) and user constraints (3.C). The clustering technique (5.C) can serve as a foundation for classifying Filipino users into financial profiles, addressing the cold-start problem (5.B). The system's ability to operate with incomplete data is crucial for a mobile-first PFMS (9.A) that must function with limited initial user input. The study's emphasis on iterative improvement through user feedback aligns with Odin's need for user retention and engagement (11.A)."
  directly_justifies:
    - "Demographic data can be used to cluster investors into distinct groups with different financial product preferences."
    - "An ANFIS system can generate a large set of IF-THEN rules to map user attributes to recommendations."
    - "Incorporating expert knowledge into the rule base improves the personalization of a recommender system."
    - "The system can be improved iteratively based on user feedback regarding the relevance of its suggestions."
    - "An ANFIS-based recommender system can function effectively even with incomplete or inaccurate initial data."
  limits:
    - "The study only considered six demographic variables; other personal and behavioral factors were excluded [unacknowledged]."
    - "The system's recommendations are limited to a specific set of investment types and may not generalize to other financial products."
    - "The model was tested on a Hungarian dataset; its applicability to other cultural contexts like the Philippines requires further validation."
    - "The paper does not address the cold-start problem in detail, assuming demographic data is readily available."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. Domains flagged as relevant included: Behavioral Profiling (5.A, 5.C) for using demographics and clustering to define investor types; Existing Systems (4.A, 4.B) for reviewing prior work and identifying gaps; Predictive Modeling (6.A) for the ANFIS-based recommendation approach; and Budget Recommendation (7.A, 7.B) for the rule-based expert knowledge integration, which is analogous to generating budget rules. Topic 5.A and 5.C were assigned `high` relevance as the paper's core contribution is profiling users via clustering and classification. Topics 4.B and 6.A received `medium` relevance for identifying a gap and providing a predictive model framework, respectively. Topics 1.A and 1.B were considered `contextual` as they provide a demographic framework not specific to Filipinos. Domains like Mobile-First Design (9), Data Privacy (10), and Savings & Debt Management (13) were rejected as the paper does not address them. The borderline case was topic 7.B (Budget Recommendation) vs. 6.A (Forecasting); the paper was categorized under 6.A as its primary output is a recommendation based on current data, not a time-series forecast, but it still informs 7.B through its rule-based recommendation logic. Overall, the paper provides a strong methodological foundation for Odin's user profiling and recommendation modules."
limitations:
  - "Data is limited to Hungarian respondents, affecting generalizability to the Filipino context [unacknowledged]."
  - "Only six demographic inputs were used, potentially overlooking other influential factors."
  - "The system's performance was not compared against other baseline recommendation algorithms [unacknowledged]."
  - "The long-term impact of the feedback loop on recommendation accuracy was not evaluated [unacknowledged]."
remember_this:
  - "ANFIS generates 1296 fuzzy rules for investment recommendations based on demographics."
  - "The system achieved an average testing error of 0.86683 in predicting investment type clusters."
  - "User feedback and expert knowledge are integrated to refine the recommendation rules."
  - "The model uses six demographic inputs to cluster users into three investment preference groups."
  - "This approach provides a framework for profile-based recommendation in financial systems."
```
---

## Paper 45: Zambrano et al_summarized.md

**Source File:** `Zambrano et al_summarized.md`

```yaml
paper_id: 10.1016/j.wds.2023.100081
designation: international
title: Rotating savings and credit associations: A scoping review
authors: Zambrano, A.F.; Giraldo, L.F.; Perdomo, M.T.; Hernández, I.D.; Godoy, J.M.
year: 2023
venue: World Development Sustainability
odin_topics:
  - 2.A
  - 13.A
  - 13.B
  - 5.A
  - 4.A
  - 4.B
  - 7.A
tldr: A scoping review of ROSCA research finds these informal savings groups provide financial access and social capital, and suggests design improvements like diversification and reputation systems.
problem_and_motivation: Informal financial cooperation, like ROSCAs, is vital for low-income communities, but a systematic synthesis of recent findings on their structure, benefits, and risks has been lacking to inform design and policy.
approach:
  - Conducted a scoping review using the PRISMA-ScR protocol on 96 peer-reviewed articles from 2000-2022.
  - Extracted data on study location, methodological approaches, and keywords for trend analysis.
  - Grouped findings into categories including origin, participants, benefits, risks, operation, and penalties.
  - Analyzed the co-occurrence of keywords to identify thematic connections within the literature.
  - Reviewed mathematical, computational, and technological applications for modeling and supporting ROSCAs.
findings:
  - Asia and Africa are the most studied continents for ROSCAs, with limited research in South America.
  - ROSCAs provide non-financial benefits like social capital, empowerment, and improved health for members.
  - Defection of members, driven by loss of motivation, is a primary risk factor for ROSCA failure.
  - Strategies like diversification (joining multiple ROSCAs) and smaller groups can increase resilience.
  - num: Multi-agent simulations and web applications are emerging to test improvements and support ROSCA operations.
key_figures_tables:
  - Figure 1: Continent of data collection → Asia and Africa are the most studied regions.
  - Figure 2: Country of data collection → Kenya, India, and Japan are frequently studied.
  - Figure 3: Published year and continent → An increasing trend in publications until 2019, with a recent decline.
  - Figure 4: Methodological approaches → Interviews and surveys are the most common methods.
  - Figure 6: Number of occurrences of most common keywords → ROSCA, Finance, and Social are the most frequent concepts.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: ROSCA
    definition: Rotating Savings and Credit Association, an informal group where members contribute periodically to a pot allocated to one member each cycle.
  - term: Bidding ROSCA
    definition: A type where the pot is allocated to members who bid the highest premium for early turns.
  - term: Fixed ROSCA
    definition: A type where the order of receiving the pot remains fixed across cycles.
  - term: Random ROSCA
    definition: A type where the order of receiving the pot is randomly determined each cycle.
critical_citations:
  - "[Anderson et al., 2009] — ROSCAs are unsustainable without external sanctions."
  - "[Besley et al., 1993] — Foundational economics of ROSCAs."
  - "[Geertz, 1962] — Early influential description of ROSCAs as development tools."
  - "[Levenson & Besley, 1996] — Key analysis of ROSCA participation determinants."
  - "[Sedai et al., 2021] — Links ROSCAs to women's empowerment in India."
relevance:
  topics:
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: ROSCAs are a quintessential example of culturally embedded financial practices studied globally.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: Directly analyzes ROSCAs as a mechanism for collective savings and achieving financial goals.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: Examines ROSCAs as an alternative to formal debt for financing needs.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Discusses member motivations like self-control and trust, which relate to behavioral profiles.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Maps the landscape of informal finance (ROSCAs) as an alternative to formal systems.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies gaps in formal finance that ROSCAs fill, and limitations of ROSCAs themselves.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: Provides background on savings strategies but does not detail algorithmic budgeting.
  contribution: This paper provides a comprehensive review of ROSCAs, offering validated domain knowledge for Odin's design. Its findings on savings discipline, social capital, and default risks directly inform the design of Odin's savings and social features. The review's emphasis on community trust and cultural specificity justifies Odin's focus on Filipino cultural practices. The identified strategies for increasing ROSCA resilience, such as diversification and reputation systems, can be adapted for Odin's recommendation and anomaly detection modules.
  directly_justifies:
    - "ROSCAs help members save money by imposing discipline and social pressure."
    - "Participation in ROSCAs provides non-financial benefits like social capital and empowerment."
    - "Defection and loss of motivation are primary risks that can be mitigated by reputation and economic penalties."
    - "Diversifying participation across multiple small groups reduces risk for members."
    - "Technological tools can improve transparency and security in informal savings groups."
  limits:
    - "Scoping review, not a meta-analysis; does not quantify effect sizes of strategies."
    - "The review excludes non-English literature, potentially missing regional insights."
    - "Focuses on ROSCAs, which are distinct from typical PFMS, limiting direct applicability."
    - "Proposed computational models are theoretical and not validated with real user data."
    - "Does not address the specific financial landscape or user behaviors of Filipino young professionals."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to domains of Culturally Specific Financial Practices (2.A) and Savings & Debt Management (13.A, 13.B) as it directly analyzes ROSCAs as informal financial tools used in various cultures. Medium relevance was assigned to Behavioral Profiling (5.A) and Existing Systems & Gaps (4.A, 4.B) due to its discussion of participant motivations, limitations of formal finance, and the role of social capital. Contextual relevance was noted for Budget Recommendation (7.A) as it provides domain knowledge but not algorithmic approaches. Other domains like Anomaly Detection (8.A, 8.B, 8.C) and Mobile-First Design (9.A, 9.B) were considered and rejected because the paper does not touch on these topics. Overall, the paper offers valuable background on informal savings behavior and community-based financial management, which can inform Odin's design by highlighting the importance of social features, trust, and culturally relevant savings mechanisms.
limitations:
  - "Limited to studies published in English."
  - "Data collection from real-world ROSCAs was restricted due to pandemic conditions after 2020."
  - "The review does not include a meta-analysis to quantify the effectiveness of strategies like diversification."
  - "Computational models and technological applications discussed are mostly theoretical and not tested at scale."
  - "Findings are synthesized from a broad global context, which may not be directly generalizable to the Philippines."
remember_this:
  - "ROSCAs provide both financial access and social capital to underprivileged communities."
  - "Discipline and social pressure are key mechanisms for successful savings in ROSCAs."
  - "Defection is a major risk, but diversification across groups can increase resilience."
  - "Non-financial benefits like empowerment and health are significant for members."
  - "num: 96 articles reviewed from 2000 to 2022 to synthesize ROSCA knowledge."
```
---

## Paper 46: Das et al_summarized.md

**Source File:** `Das et al_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international-algorithm-specific
title: Recurrent Neural Networks (RNNs): Architectures, Training Tricks, and Introduction to Influential Research
authors: Das, S.; Tariq, A.; Santos, T.; Kantareddy, S. S.; Banerjee, I.
year: 2023
venue: Machine Learning for Brain Disorders
odin_topics:
  - "6.B"
  - "8.B"
  - "7.B"
  - "7.D"
  - "9.A"
  - "10.A"
tldr: Survey of RNN architectures (LSTM, GRU, bidirectional, deep, attention) and training strategies for sequential data modeling.
problem_and_motivation: Long-term dependencies in sequential data are difficult for simple RNNs to learn. The vanishing and exploding gradient problems hinder effective training. Gated architectures like LSTM and GRU were introduced to capture long-range patterns.
approach:
  - "Reviews six RNN architectures: SimpleRNN, LSTM, GRU, bidirectional RNN, deep RNN, and encoder-decoder with attention."
  - "Describes training fundamentals including BPTT and challenges with long-term dependencies."
  - "Discusses practical training techniques: skip connections, leaky units, and gradient clipping."
  - "Summarizes RNN applications in language modeling: text classification, summarization, machine translation, and image-to-text."
  - "Covers attention mechanisms and the Transformer as a parallelizable alternative to sequential decoding."
findings:
  - "LSTM and GRU mitigate vanishing gradients via gating units that add past information to present state."
  - "GRU has fewer gates than LSTM, reducing computation time while capturing long-term dependencies."
  - "Bidirectional RNNs improve sequence tasks by using both past and future context."
  - "Attention mechanisms allow models to focus on relevant parts of the input, improving performance on long sequences."
  - "The Transformer uses self-attention to enable parallel processing, reducing computation time."
  - "num: Gradient clipping constrains gradient norms to predetermined thresholds, preventing exploding gradients."
  - "num: Skip connections speed learning by reducing the impact of vanishing gradients."
  - "Leaky units use linear self-connections with weights near one to retain long-term information."
key_figures_tables:
  - "Figure 4: LSTM cell architecture with input, forget, and output gates → Gating controls information flow for long-term memory."
  - "Figure 5: GRU architecture with reset and update gates → Simplified gating reduces parameters versus LSTM."
  - "Figure 6: Bidirectional RNN with forward and backward sub-RNNs → Enables context from both past and future."
  - "Figure 8: Transformer with stacked encoder-decoder layers → Self-attention enables parallel processing."
key_equations:
  - equation: "h^{(t)} = f(h^{(t-1)}, x^{(t)}; W)"
    explanation: "State update rule for SimpleRNN."
  - equation: "f^{(t)}_i = \\sigma(U_f x^{(t)} + W_f h^{(t-1)} + b_f)_i"
    explanation: "Forget gate computation in LSTM."
  - equation: "Attention(Q,K,V) = softmax(QK^T / \\sqrt{d_k}) V"
    explanation: "Scaled dot-product attention in Transformers."
definitions:
  - term: "RNN"
    definition: "Recurrent neural network with hidden state and feedback loops for sequential data."
  - term: "LSTM"
    definition: "Long short-term memory, a gated RNN for long-term dependencies."
  - term: "GRU"
    definition: "Gated recurrent unit, a simplified LSTM with fewer gates."
  - term: "BPTT"
    definition: "Back-propagation through time, the training algorithm for RNNs."
  - term: "Attention"
    definition: "Mechanism to focus on relevant parts of input during decoding."
  - term: "Transformer"
    definition: "Model based on self-attention, enabling parallel sequence processing."
critical_citations:
  - "[Hochreiter & Schmidhuber, 1997] — Proposed LSTM for long-term dependencies."
  - "[Cho et al., 2014] — Introduced GRU and encoder-decoder."
  - "[Bahdanau et al., 2014] — Added attention to encoder-decoder."
  - "[Vaswani et al., 2017] — Introduced Transformer with self-attention."
  - "[Pascanu et al., 2013] — Analyzed difficulty of training RNNs."
relevance:
  topics:
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Provides foundational RNN architectures (LSTM, GRU) directly applicable to spending sequence forecasting."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "RNNs and attention models are commonly used for anomaly detection in time-series."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Encoder-decoder and attention architectures inform sequence-to-sequence prediction for budget generation."
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "low"
      justification: "Training tricks like gradient clipping may be adapted for constraint handling, but not directly addressed."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "contextual"
      justification: "Efficient architectures (GRU, attention) are relevant for mobile deployment but design is not discussed."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "contextual"
      justification: "Not addressed; privacy is outside scope."
  contribution: "This survey establishes RNNs and attention as core tools for sequential spending prediction. LSTM and GRU provide the algorithmic foundation for Odin's forecasting module. Attention mechanisms offer a path to explainable budget recommendations. Training strategies like gradient clipping ensure stable optimization on noisy spending data."
  directly_justifies:
    - "LSTM and GRU capture long-term dependencies in sequential spending data."
    - "Attention mechanisms improve sequence-to-sequence prediction by focusing on relevant past transactions."
    - "Bidirectional RNNs can leverage both past and future spending patterns for anomaly detection."
    - "Gradient clipping stabilizes training on irregular spending sequences."
    - "Encoder-decoder architectures support variable-length input-output mapping for budget generation."
  limits:
    - "The survey does not address personal finance data or spending patterns."
    - "No experimental results on spending data are provided."
    - "Privacy, trust, and mobile UX are not discussed."
  mapping_rationale: "All 12 functional domains and associated topic codes were systematically scanned. Domains 6 (Forecasting) and 8 (Anomaly Detection) were flagged as highly relevant because the paper provides core algorithms (LSTM, GRU, attention) for sequential data modeling. Domain 7 (Budget Recommendation) was marked medium due to the relevance of encoder-decoder for sequence mapping, but no direct budget constraints are discussed. Domain 9 (Mobile-First Design) and 10 (Data Privacy) were marked contextual because efficient architectures are relevant for mobile deployment, but the paper does not address design or privacy. Domains 2 (Cultural Context), 3 (Expense Categorization), 4 (Existing Systems), 5 (Behavioral Profiling), 11 (Retention), 12 (Evaluation), and 13 (Savings/Debt) were rejected as the paper does not touch these topics. Overall, the paper provides strong algorithmic foundations for forecasting and anomaly detection but is not specific to personal finance."
limitations:
  - "No empirical validation on real-world spending data."
  - "Does not address privacy or security concerns."
  - "Focuses on general NLP and time-series, not PFMS-specific constraints."
  - "Not a primary research paper; survey of existing architectures."
remember_this:
  - "LSTM and GRU are core architectures for forecasting sequential spending data."
  - "Attention mechanisms enable focus on relevant past transactions."
  - "Gradient clipping prevents training instability on irregular data."
  - "The Transformer enables parallel processing but is computationally intensive."
  - "Bidirectional RNNs use past and future context for anomaly detection."
```
---

## Paper 47: Prasetyo et al_summarized.md

**Source File:** `Prasetyo et al_summarized.md`

```yaml
paper_id: 9f0b6d7c-8a3b-5e1f-9c4d-2a7e8b3c5d1f
designation: international
title: Integrating Financial Management and Gamification: A Systematic Literature Review and Future Research Agenda
authors: Prasetyo, A. P.; Santoso, H. B.; Putra, P. O. H.
year: 2023
venue: Indonesian Journal of Computer Science
odin_topics:
  - 4.A
  - 4.B
  - 5.A
  - 11.A
  - 11.B
  - 12.A
tldr: A systematic literature review synthesizing research on financial behavior and gamification-related behavioral intention using the TCCM framework.
problem_and_motivation: Low public financial behavior levels cause long-term problems, yet gamification research in finance is limited. This review bridges the gap between financial behavior and gamification to inform future design and research.
approach:
  - Utilized the Theory, Context, Characteristics, and Methodology (TCCM) framework for a systematic literature review.
  - Searched four databases for articles published between 2018 and 2022.
  - Analyzed 53 articles on financial behavior and gamification-related behavioral intention.
  - Extracted data on theories, contexts, characteristics, and methodologies from the selected studies.
  - Synthesized findings into integrated conceptual models of financial behavior and gamification-related behavioral intention.
findings:
  - Theory of Planned Behavior is the most used theory in financial behavior research (50%), while Self-Determination Theory is prominent in gamification research (14.3%).
  - Gamification research in finance is limited, with most studies focusing on education or general contexts.
  - Financial contexts studied include general behavior, literacy, satisfaction, and well-being, while gamification contexts include finance, education, and health.
  - Antecedents of financial behavior include financial literacy, socio-demographics, and psychological traits; gamification antecedents include psychological and gamification-related constructs.
  - The review identifies habit as a key mediator in financial behavior and attitudinal factors as key mediators in gamification-related behavioral intention.
  - Gamification elements like badges and points are widely investigated, but research on elements like narrative and cooperation is sparse.
  - Quantitative methods dominate both fields, with questionnaires and SEM being the primary tools.
  - num: The global PFM application market is expected to reach $3,338 million by 2025 with an annual growth rate of 12.65%.
key_figures_tables:
  - Figure 1: Study selection process flowchart → 53 articles were analyzed after a multi-step screening.
  - Figure 2: Number of articles by year of publication → Research interest in both domains has been increasing from 2018 to 2022.
  - Figure 3: Integrated conceptual model of financial behavior → Synthesizes antecedents, mediators, moderators, and consequences.
  - Figure 4: Integrated conceptual model of gamification-related behavioral intention → Synthesizes antecedents, mediators, moderators, and consequences.
  - Table 3: Theories used in financial behavior research → Theory of Planned Behavior is the most frequent (50%).
  - Table 4: Theories used in gamification-related behavioral intention research → Self-Determination Theory is the most frequent (14.3%).
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: TCCM
    definition: Theory, Context, Characteristics, and Methodology framework used for systematic literature reviews.
  - term: PFM
    definition: Personal Financial Management, apps designed to help individuals manage their finances.
  - term: SDT
    definition: Self-Determination Theory, a theory of motivation focusing on autonomy, competence, and relatedness.
  - term: TPB
    definition: Theory of Planned Behavior, a theory predicting behavioral intention based on attitudes, norms, and perceived control.
  - term: PLS-SEM
    definition: Partial Least Squares Structural Equation Modeling, a statistical technique for analyzing complex cause-effect relationships.
critical_citations:
  - "[Goyal et al., 2021] — Reviews antecedents and consequences of personal financial management behavior."
  - "[Koivisto & Hamari, 2019] — Reviews gamification research and suggests future directions."
  - "[Bitrián et al., 2021] — Examines the gamification of personal financial management apps."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews existing research on PFM apps and gamification in finance.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Explicitly identifies the gap in gamification research within the financial domain.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Synthesizes research on financial behavior, including antecedents like psychological traits.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: high
      justification: Directly investigates gamification as a tool to enhance user engagement and behavioral intention.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: high
      justification: Reviews gamification elements and their impact on continuance intention and retention.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Reviews methodologies used to evaluate behavioral models, providing a framework for system evaluation.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: Mentions financial behavior contexts but does not focus on categorization frameworks.
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Provides general demographic findings but is not specific to Filipino young professionals.
  contribution: This review provides a synthesized understanding of the research landscape at the intersection of financial behavior and gamification. It offers integrated conceptual models that can inform the design of PFM systems like Odin. The identified theories, constructs, and methodologies provide a foundation for building Odin's behavioral profiling, engagement, and evaluation modules. The paper directly justifies the need for gamification to improve user engagement in PFM apps. It also highlights the importance of considering psychological and demographic antecedents for personalized financial systems.
  directly_justifies:
    - Gamification in PFM apps can foster behavioral intention toward positive financial behaviors.
    - Self-Determination Theory and Theory of Planned Behavior are relevant for understanding user motivation in financial contexts.
    - PFM apps should investigate gamification elements beyond common ones like badges and points.
    - Understanding psychological and socio-demographic antecedents is key to designing effective behavioral interventions.
    - There is a need for more research on gamification in the financial domain, providing an opportunity for Odin to contribute.
  limits:
    - The review is limited to articles published between 2018 and 2022, potentially excluding older relevant work.
    - The analysis is based on the TCCM framework, which may not capture all nuances of the research domain.
    - The review focuses on behavioral intention rather than actual observed financial behavior for gamification studies.
  mapping_rationale: A systematic scan was performed across all 12 functional domains and their associated canonical topic codes. The paper was flagged as highly relevant for topics related to engagement dynamics (11.A), retention mechanisms (11.B), and financial behavioral profiles (5.A), as it directly synthesizes research on these areas. It was deemed medium relevance for the landscape of existing systems (4.A) and system evaluation (12.A), as it provides a broad overview and methodological insights. Contextual relevance was assigned to topics like expense categorization (3.A) and the Filipino demographic (1.A), as the paper's context is general and not specific to the Philippines. Topics such as budget recommendation (7.A-D), anomaly detection (8.A-C), and debt management (13.A-C) were rejected because they are not covered in the paper. The review provides a foundational understanding of the intersection of financial behavior and gamification, which is directly applicable to Odin's design for engagement and behavioral profiling.
limitations:
  - The review does not include a meta-analysis of the effect sizes of gamification on financial behavior. [unacknowledged]
  - The search was limited to four databases and specific search terms, which might have introduced selection bias. [unacknowledged]
remember_this:
  - Gamification research in personal finance is an emerging field with significant potential.
  - Self-Determination Theory is the most frequently used theory in gamification research.
  - Theory of Planned Behavior is the dominant theory in financial behavior research.
  - The global PFM market is projected to reach $3.338 billion by 2025.
  - Future research should explore dynamic gamification and negative consequences.
```
---

## Paper 48: Ong  A. et al_summarized.md

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

## Paper 49: Fei_summarized.md

**Source File:** `Fei_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international
title: Impact of Mental Representation on Consumer Behaviors: Implications for Mental Budgeting and Prediction Algorithm Preferences
authors: Fei, L.
year: 2023
venue: University of Chicago Booth School of Business
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 7.A
  - 7.D
  - 8.B
  - 12.A
tldr: Consumers represent expenditures in hierarchical taxonomies, and the taxonomic distance between items predicts spending adjustments when budgets deviate.
problem_and_motivation: Existing mental budgeting research assumes single-level categories, failing to capture how consumers naturally organize expenditures. Understanding this hierarchical representation is crucial for predicting spending adjustments and improving personal finance tools.
approach:
  - Recovered consumer expenditure taxonomies using a successive pile-sort method with 27 US participants.
  - Validated taxonomy consensus and stability across time using Cultural Consensus Model analysis.
  - Tested spending adjustment predictions using lab experiments with self-reported and consequential choices.
  - Analyzed over 7 million grocery shopping trips to examine real-world spending patterns in response to promotions.
  - Controlled for substitutability and complementarity to isolate the effect of taxonomic distance.
findings:
  - Consumers show consensus in their hierarchical representations of expenditures.
  - Taxonomic distance predicts spending adjustment: closer items are adjusted more than distant ones.
  - num: Spending adjustment increased by 0.5 units for each taxonomic level closer between items.
  - The taxonomy effect persists even when controlling for substitutability and complementarity.
  - num: Analysis of 7 million grocery trips shows consumers spend more on items when taxonomically close items are on sale.
  - People spontaneously recruit taxonomies for spending decisions without explicit category prompts.
key_figures_tables:
  - Figure 1.3: MDS plot shows clustered groups of expenditures → Reveals consensus in mental representation structure.
  - Figure 1.5: Bar chart of spending adjustment by taxonomic distance → Closer items show higher spending adjustment.
  - Figure 1.9: Regression coefficients for close vs. far focal items over years → Close items consistently drive higher spending.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: Taxonomic Distance
    definition: The level at which expenditures are categorized together in a consumer's hierarchy.
  - term: Cultural Consensus Model
    definition: A statistical framework to test agreement across individual mental representations.
critical_citations:
  - "[Thaler, 1985] — Foundation of mental accounting theory."
  - "[Heath and Soll, 1996] — Establishes mental budgeting with category-level adjustments."
  - "[Henderson and Peterson, 1992] — Preliminary evidence for hierarchical mental accounts."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Paper proposes hierarchical taxonomy for expenditure categorization.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: high
      justification: Provides empirical basis for designing multi-level spending categories.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Critiques single-level budgeting approaches as insufficient.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Highlights gap in capturing hierarchical mental accounts.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Taxonomy reflects individual spending patterns and profiles.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Directly tests and refines mental budgeting theory.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: medium
      justification: Hierarchical adjustment suggests structured reduction priorities.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Taxonomic context could inform anomaly baselines.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: contextual
      justification: Uses field data to evaluate taxonomy-based spending predictions.
  contribution: The paper provides a cognitive framework for understanding how consumers naturally categorize expenses, which can inform Odin's expense categorization engine by moving beyond flat category structures. It validates that taxonomic distance predicts real spending adjustments, offering a basis for Odin's budget recommendation module to model user behavior more accurately. The findings also support Odin's anomaly detection by providing a baseline for what constitutes typical spending relationships. Additionally, the paper demonstrates that consumers spontaneously recruit taxonomies, suggesting Odin can leverage implicit user structures without explicit input.
  directly_justifies:
    - Odin should implement a hierarchical expense categorization system based on taxonomic distance.
    - Budget recommendations should account for relative distance between expense items.
    - Spending adjustments follow predictable patterns tied to mental taxonomies.
    - Mobile UX can leverage hierarchical categories for intuitive budget tracking.
  limits:
    - Study population is US-based, limiting generalizability to Filipino young professionals.
    - Taxonomic recovery may vary across cultural contexts and financial literacy levels.
    - The field data focuses only on grocery purchases, not total spending.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes flagged several as relevant. The paper directly addresses expense categorization (3.A, 3.B) by proposing a hierarchical taxonomy, and critiques existing systems (4.A, 4.B) for their single-level assumptions. It supports behavioral profiling (5.A) by showing taxonomic consensus across consumers. The core contribution to budget recommendation (7.A) is high, as it tests and refines mental budgeting theory, with implications for infeasibility handling (7.D) through structured adjustment priorities. Anomaly detection (8.B) was considered low because the paper does not directly address detection algorithms, though taxonomic context could inform baselines. System evaluation (12.A) was deemed contextual due to the use of field data. Domains like Filipino cultural context (2.A-D), mobile-first design (9.A-B), data privacy (10.A-B), user retention (11.A-B), and savings/debt management (13.A-C) were rejected as they are not addressed. The paper overall provides foundational cognitive insights for Odin's expense management and budgeting modules.
limitations:
  - Taxonomic recovery may not capture all relevant spending categories for Filipino users. [unacknowledged]
  - Field data limited to grocery purchases, not validating total spending adjustments. [unacknowledged]
  - Spontaneous adjustment may be weaker when users are explicitly reminded of budgets.
remember_this:
  - Consumers mentally organize expenses in nested hierarchies, not just flat categories.
  - Spending adjustments are stronger for taxonomically closer items.
  - Hierarchical taxonomies predict real grocery spending based on promotions.
  - The taxonomy effect remains after controlling for substitutability and complementarity.
  - People spontaneously use taxonomies even without budget category prompts.
```
---

## Paper 50: Machireddy_summarized.md

**Source File:** `Machireddy_summarized.md`

```yaml
paper_id: 4c5e4b1a-4c5e-4b1a-8c5e-4b1a8c5e4b1a
designation: international-algorithm-specific
title: Data Science and Business Analytics Approaches to Financial Wellbeing: Modeling Consumer Habits and Identifying At-Risk Individuals in Financial Services
authors: Machireddy, J. R.
year: 2023
venue: Journal of Applied Big Data Analytics, Decision-Making, and Predictive Modelling Systems
odin_topics:
  - 1.C
  - 2.A
  - 2.B
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 7.B
  - 7.C
  - 7.D
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 11.A
  - 12.A
  - 13.A
tldr: A review of data science methods for modeling consumer financial behavior, segmenting populations by vulnerability, and applying explainable AI for transparent risk assessment in financial services.
problem_and_motivation: Traditional credit scoring uses limited variables and lags behind real-time financial behavior, failing to capture dynamic consumer risk or provide early warnings. Financial institutions lack robust, ethical frameworks to leverage detailed transaction data and digital footprints for proactive consumer financial well-being management. This gap leads to missed opportunities for early intervention and can exacerbate consumer financial distress.
approach:
  - Extracts behavioral features from transaction histories, including expense-to-income ratio, income volatility, and liquidity trends.
  - Applies machine learning models like gradient boosting and recurrent neural networks for risk classification and sequence prediction.
  - Incorporates psychological traits and contextual life events into financial profiles using surveys and inferred behavioral proxies.
  - Uses clustering and supervised classification to segment consumers into groups based on financial health and vulnerability.
  - Employs explainable AI techniques like SHAP to provide transparency in model predictions and risk scores.
  - Discusses real-time analytics pipelines for continuous monitoring and immediate intervention triggers.
findings:
  - num: Segmentation into three distinct clusters (Financially Secure, Stretched, Vulnerable) enables targeted interventions and product design.
  - num: 72% faster stress detection is achieved through real-time pattern analysis compared to traditional methods.
  - num: 68% reduction in defaults is observed through proactive interventions based on segmentation and early warnings.
  - Incorporating psychological and contextual factors enhances the explanatory power and empathy of financial risk models.
  - Explainable AI is critical for regulatory compliance, bias detection, and building consumer trust in automated decisions.
  - Open banking and real-time data streams enable dynamic, proactive risk assessment rather than periodic static reviews.
key_figures_tables:
  - Figure 1: Challenges in Financial Well-being → Maps systemic risks and analytical limitations affecting consumer financial health.
  - Table 1: Segment profiles based on behavioral financial traits → Defines Financially Healthy, Coping, and Vulnerable segments using income, debt, savings, and credit usage.
  - Table 5: Comparative overview of modeling techniques for financial behavior → Compares Logistic Regression, Decision Trees, Gradient Boosting, RNNs, and Autoencoders on temporal awareness and interpretability.
  - Figure 6: Financial Vulnerability Segmentation Pipeline → Shows the process from raw data to risk cohorts and targeted actions, including clustering and XGBoost.
  - Table 10: Consumer segments defined by key financial behavior traits → Details traits for Financially Secure, Stretched, and Vulnerable segments.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: XAI
    definition: Explainable Artificial Intelligence, techniques that make algorithm decision-making interpretable by humans.
  - term: SHAP
    definition: SHapley Additive exPlanations, a method to explain the output of machine learning models.
  - term: PFMS
    definition: Personal Financial Management System, a software application that helps users manage their finances.
critical_citations:
  - "[Salignac et al., 2019] — Defines financial well-being as a multi-dimensional concept."
  - "[Heiskanen, 2016] — Links problem gambling with declining financial well-being and distress signals."
  - "[Xiao, 2016] — Explores the relationship between consumer financial capability and well-being."
  - "[Tahir & Ahmed, 2021] — Analyzes Australian household debt and financial well-being."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: contextual
      justification: Provides generic behavioral patterns that can be applied to the target demographic.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: low
      justification: Discusses global cultural differences in financial data usage, indirectly relevant.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: Mentions external economic context and seasonal spending, relevant for modeling cyclical patterns.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews current use of analytics in financial institutions and fintechs.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Critiques traditional credit scoring and lack of real-time, explainable models.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Core focus on modeling consumer financial habits and creating behavioral profiles.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: medium
      justification: Discusses dynamic profiles and segmentation, relevant for cold-start issues.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Details clustering and supervised classification for customer segmentation.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly discusses predictive models for financial distress and behavior.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Covers sequence analysis using Hidden Markov Models and RNNs for spending data.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Mentions dynamic budgeting and tailored financial advice as outcomes of segmentation.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: low
      justification: Implicitly relevant through the discussion of managing financial constraints.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: medium
      justification: Discusses handling financial distress and infeasibility through interventions and hardship programs.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Explicitly discusses identifying outliers and sudden behavioral changes as warning signs.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Mentions autoencoders and unsupervised learning for anomaly detection.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Dedicated section on ethical frameworks, privacy, and regulatory compliance (GDPR).
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Emphasizes explainable AI and transparency as key to building user trust.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Discusses proactive customer engagement and feedback loops to improve financial well-being.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Mentions model monitoring, performance tracking, and fairness audits as operational requirements.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: contextual
      justification: Discusses savings profiles and resilience as part of financial health, but not goal management specifically.
  contribution: The paper provides a comprehensive framework for integrating behavioral data science into financial risk management. It directly justifies Odin's need for a dynamic behavioral profiling module (5.A, 5.C) that moves beyond static credit scores. The emphasis on real-time analytics (6.A, 8.B) supports Odin's requirement for immediate feedback on user spending. The detailed discussion of explainable AI (10.B) and ethical deployment (10.A) validates Odin's design principles for transparency and user trust. The segmentation approach (5.A) offers a template for Odin's user classification, enabling personalized budgeting and savings recommendations (7.B, 13.A).
  directly_justifies:
    - "Financial institutions can create dynamic, real-time portraits of consumer financial health using transaction data."
    - "Combining psychological and contextual factors with transactional data enhances the explanatory power of risk models."
    - "Explainable AI is critical for building consumer trust and ensuring regulatory compliance in automated decisions."
    - "Financial vulnerability segmentation allows for targeted interventions, improving customer outcomes and reducing defaults."
    - "Real-time analytics enable early detection of financial distress, allowing for proactive assistance and prevention."
  limits:
    - "The paper is a conceptual review and lacks empirical validation of the proposed frameworks in a specific context."
    - "Psychological and contextual data integration introduces significant privacy and measurement challenges not fully addressed."
    - "The discussion of algorithms is high-level and does not provide specific details for implementation in a PFMS like Odin."
    - "Cross-jurisdictional regulatory differences complicate the universal application of the proposed data practices."
  mapping_rationale: A systematic scan across all 12 functional domains was performed. Domains related to behavioral profiling (5), predictive modeling (6), budgeting (7), anomaly detection (8), and data privacy/ethics (10) were flagged as highly relevant. Topics concerning Filipino cultural specifics (2) were marked low or contextual as the paper offers a global perspective but not localized insights. The domains of expense categorization (3) and mobile-first design (9) were considered but rejected as the paper focuses on modeling and risk assessment rather than UI/UX or category design. The paper is highly relevant to Odin as it provides a theoretical and methodological foundation for its core analytical modules, emphasizing the need for dynamic, explainable, and ethically-grounded consumer risk models.
limitations:
  - "The paper is a conceptual review and lacks empirical testing of the proposed models on real-world data. [unacknowledged]"
  - "Specific implementation details for integrating psychological and contextual data are not provided. [unacknowledged]"
  - "The discussion of bias and fairness is general and does not offer concrete algorithmic solutions for Odin's context."
remember_this:
  - "Real-time analytics can detect financial distress 72% faster than traditional methods."
  - "Explainable AI is essential for building consumer trust and regulatory compliance."
  - "Consumer segmentation enables proactive interventions that reduce defaults by 68%."
  - "Psychological and contextual factors are crucial for accurate financial behavior modeling."
  - "Data-driven risk assessment is shifting from static snapshots to continuous, dynamic monitoring."
```
---


---

## Agent Instruction

If the agent reading this document believes further context about a paper is needed, it may request the original converted markdown file (with the '_marked' suffix) from the user for the relevant paper(s).
