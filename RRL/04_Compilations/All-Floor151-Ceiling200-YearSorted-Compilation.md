# Compiled Research Summaries

**Total Papers:** 50

**Note:** Included papers positions 151 to 200, Sorted by year.

---

## Paper 1: Karst et al_summarized.md

**Source File:** `Karst et al_summarized.md`

```yaml
paper_id: 10.1007/s12525-024-00746-8
designation: international-algorithm-specific
title: SynDEc: A Synthetic Data Ecosystem
authors: Karst, F. S.; Li, M. M.; Leimeister, J. M.
year: 2025
venue: Electronic Markets
odin_topics:
  - 4.A
  - 4.B
  - 7.D
  - 8.B
  - 10.A
  - 12.A
  - 12.B
tldr: A synthetic data sharing ecosystem using generative AI enables financial institutions to exchange transaction data while preserving privacy and improving fraud detection performance.
problem_and_motivation: Small and mid-sized banks lack sufficient high-quality data to leverage advanced AI for fraud detection and risk management. Existing solutions like open banking and federated learning face scalability, privacy, and model-architecture limitations. A privacy-preserving data ecosystem is needed to enable secure cross-institutional data sharing and unlock economic value.
approach:
  - The study employs design science research with four iterative design cycles in collaboration with two banks, including UnionBank of the Philippines.
  - Meta-requirements and design requirements were derived from a systematic literature review and nine semi-structured expert interviews.
  - Initial design principles and a modular system architecture were proposed, then refined through expert feedback and prototype evaluation.
  - Synthetic data generation algorithms (GAN, CTGAN, TimeGAN, TVAE, GMM) were compared on the IEEE-CIS credit card fraud dataset.
  - The ecosystem's effectiveness was validated on two large simulated financial transaction datasets (IBM-AML and IBM-CCF) for fraud and money laundering detection.
findings:
  - TVAE outperformed other generative models for financial transaction data, achieving an 89% ROC AUC score compared to 52-59% for alternatives.
  - Combining synthetic data with local real data increased fraud detection ROC AUC by 1%, translating to 2.14% more true positives detected.
  - Training synthetic data generators separately per class with pre-training on majority data outperformed other training schemes.
  - The ecosystem improved performance for both fraud detection (3.6%) and anti-money laundering (6.6%) tasks.
  - Smaller banks benefited disproportionately more from participation, with a -0.09 correlation between performance gain and institution size.
key_figures_tables:
  - Figure 4: Comparison of synthetic data generation algorithms → TVAE significantly outperforms GMM, CTGAN, and TimeGAN.
  - Figure 5: Synthetic data combined with local real data outperforms synthetic-only or real-only training → optimal mix-in percentage varies by bank.
  - Figure 8: Effect of synthetic data mix-in percentage → no universal optimal mix; banks should tune individually.
  - Figure 10: Performance gain by bank size → smaller banks see greater relative improvement from ecosystem participation.
  - Figure 11: Performance with partial participation → even 50% participation yields significant gains.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "GAN"
    definition: "Generative Adversarial Network, a model where a generator and discriminator compete to create realistic synthetic data."
  - term: "VAE"
    definition: "Variational Autoencoder, a generative model that learns a compressed representation to synthesize new data."
  - term: "TVAE"
    definition: "Tabular Variational Autoencoder, a VAE variant designed for tabular data."
  - term: "CTGAN"
    definition: "Conditional Tabular GAN, a GAN variant for tabular data with conditional generation."
  - term: "DP"
    definition: "Design Principle, a prescriptive guideline for artifact creation."
  - term: "DR"
    definition: "Design Requirement, a specific actionable specification for artifact features."
  - term: "MR"
    definition: "Meta-Requirement, a high-level generalized goal for artifact design."
  - term: "DSR"
    definition: "Design Science Research, a framework for iterative artifact development."
  - term: "DSRM"
    definition: "Design Science Research Methodology, the specific process by Peffers et al. used in this study."
critical_citations:
  - "[Jordon et al., 2018] — foundational for privacy-preserving synthetic data generation."
  - "[Gelhaar & Otto, 2020] — identifies cooperative challenges in data ecosystems."
  - "[Brée et al., 2024] — highlights data security and AI integration gaps in data ecosystems."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: "This paper evaluates open banking and federated learning as existing systems, identifying their limitations."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: "The paper systematically identifies scalability, privacy, and model-architecture constraints of current data-sharing approaches."
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: contextual
      justification: "The ecosystem's data rebalancing and oversampling techniques relate to handling data infeasibility, though not directly budget allocation."
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: "This paper benchmarks multiple generative algorithms (GAN, VAE, TVAE) for fraud detection performance on transaction data."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: "The core contribution is a privacy-preserving data sharing ecosystem using synthetic data to mitigate disclosure risks."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: "The paper provides a multi-cycle evaluation framework including privacy metrics (nearest neighbor, membership inference) and performance metrics (ROC AUC)."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: "The study rigorously evaluates different synthetic data generation algorithms and training schemes in a financial context."
  contribution: "This paper provides a validated set of design principles for a synthetic data-sharing ecosystem that directly addresses Odin's need for privacy-preserving cross-institutional data exchange. The modular architecture (DP1) and privacy-preserving generation (DP2) inform Odin's system design for handling sensitive financial data while enabling collaborative model training. The empirical finding that TVAE outperforms other generators on transaction data guides algorithm selection for Odin's anomaly detection and forecasting modules. The demonstration of performance gains for smaller institutions validates the ecosystem's value proposition for diverse financial actors."
  directly_justifies:
    - "Synthetic data generation with TVAE achieves high utility while maintaining privacy on financial transaction data."
    - "Smaller banks benefit disproportionately more from participating in a synthetic data ecosystem."
    - "Combining synthetic data with local real data improves fraud detection recall by 2.14%."
    - "A modular system design with separate local and global data layers preserves data privacy during cross-institutional sharing."
    - "Even partial ecosystem participation (50% of institutions) yields significant performance improvements."
  limits:
    - "Evaluation was conducted on simulated and public datasets, not real bank transaction data, limiting ecological validity."
    - "Privacy was tested but not fully guaranteed via differential privacy mechanisms; future work on PATEGAN is needed."
    - "Generalizability beyond fraud detection and money laundering was not empirically tested."
  mapping_rationale: "A systematic scan of all 12 functional domains was performed. The paper was flagged as relevant for Existing Systems & Gaps (4.A, 4.B) because it critically evaluates open banking and federated learning as current solutions. For Anomaly Detection (8.B), it directly benchmarks generative algorithms on fraud data. For Data Privacy (10.A), the core contribution is privacy-preserving synthetic data sharing. For System Evaluation (12.A, 12.B), the study provides a rigorous iterative evaluation framework. Budget Recommendation (7.D) was considered but rejected as borderline: the paper's data rebalancing is not about budget allocation optimization. Behavioral Profiling (5.A-5.C) and Spending Forecasting (6.A-6.B) were rejected as the paper does not address user profiling or time-series prediction directly. Mobile-First Design (9.A-9.B) and Retention (11.A-11.B) were also rejected as out of scope. Overall, the paper is highly relevant for informing Odin's data infrastructure, privacy architecture, and algorithm selection for anomaly detection."
limitations:
  - "Evaluation used simulated and public datasets, not real bank transaction data. [unacknowledged]"
  - "Privacy guarantees are not formally proven via differential privacy mechanisms."
  - "Only two financial use cases (fraud detection and AML) were evaluated."
  - "The ecosystem's practical deployment costs and incentives for real-world collaboration were not fully tested."
remember_this:
  - "TVAE generated synthetic financial data with 89% ROC AUC, outperforming GANs and GMMs."
  - "Synthetic data combined with real data increased fraud detection recall by 2.14%."
  - "Smaller banks see greater relative performance gains from ecosystem participation."
  - "The ecosystem improved performance even with only 50% of institutions participating."
  - "Privacy-preserving synthetic data sharing can overcome regulatory and trust barriers."
```
---

## Paper 2: Ashta_summarized.md

**Source File:** `Ashta_summarized.md`

```yaml
paper_id: 10.2139/ssrn.5739406
designation: international
title: Artificial Intelligence in Microfinance and Financial Inclusion: Applications, Issues, and Future Directions
authors: Ashta, A.
year: 2025
venue: SSRN
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 7.B
  - 8.A
  - 8.B
  - 9.A
  - 9.B
  - 10.A
tldr: AI enables financial inclusion for unbanked populations through alternative credit scoring, automated underwriting, and personalized services, but introduces risks of algorithmic bias, privacy violations, and digital exclusion requiring robust governance.
problem_and_motivation: Two billion adults globally lack access to formal financial services due to credit invisibility, high costs, and information asymmetries. Traditional credit scoring excludes those without formal credit histories, creating a barrier to first-time loans. AI offers a means to break these barriers by leveraging alternative data to assess creditworthiness and automate financial services.
approach:
  - This paper is a critical review of academic and gray literature, analyzing AI applications across payments, savings, lending, insurance, and investments.
  - The analysis draws on real-world case studies from the Global South, including M-Pesa, GCash, Tala, Branch, BIMA, and Pula.
  - The BHAI framework for humane AI development is adopted to evaluate ethical considerations and operational challenges.
  - The paper synthesizes findings from multiple sources to provide a nuanced assessment of AI's role in financial inclusion and its limitations.
  - The review uses an interpretative-constructivist approach to prioritize context-rich insights over universal generalizations.
findings:
  - AI-powered alternative credit scoring enables lending to credit-invisible populations, with mobile payment data showing correlations of 0.65-0.72 with repayment rates.
  - num: Alternative credit scoring models reduce default rates and can cut operational costs from 6-12% to under 2%.
  - num: AI-powered KYC verification can reduce onboarding time from weeks to minutes, expanding access for unbanked populations.
  - Gradient boosting methods (XGBoost, LightGBM) power 70-80% of alternative credit scoring production systems.
  - AI-driven fraud detection and personalized services enhance payment security and user engagement for platforms like GCash and M-Pesa.
  - AI enables parametric insurance and dynamic pricing, creating micro-insurance products for smallholder farmers and informal workers.
  - Algorithmic bias, proxy discrimination, and privacy violations are significant risks, requiring fairness audits and explainable AI.
  - The "inclusion paradox" reveals that AI provides access but often at exploitative terms, such as high-interest rates (30-40% APR).
key_figures_tables:
  - Table 1: Behavioral finance nudges in digital savings → AI can automate personalized savings nudges based on transaction patterns.
  - Table 2: Traditional versus Alternative Data → AI leverages mobile phone and digital wallet data for credit scoring.
  - Table 3: AI Technologies by Financial Sector → Supervised learning dominates across all sectors, particularly gradient boosting.
  - Table 4: Humane Considerations by Financial Sector → All sectors face challenges of bias, privacy, transparency, and manipulative practices.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Artificial Intelligence (AI)
    definition: Computer systems that can perform tasks typically requiring human intelligence, such as pattern recognition, decision-making, and language understanding.
  - term: Machine Learning (ML)
    definition: Algorithms that improve automatically through experience, learning patterns from data.
  - term: Supervised Learning
    definition: Training algorithms on labeled datasets to predict outcomes (e.g., classifying fraud or default risk).
  - term: Unsupervised Learning
    definition: Discovering hidden patterns in data without pre-labeled examples (e.g., clustering users by behavior).
  - term: Reinforcement Learning
    definition: Algorithms learn optimal strategies through trial and error, receiving rewards for successful actions.
  - term: Natural Language Processing (NLP)
    definition: Technology enabling computers to understand and generate human language.
  - term: Computer Vision
    definition: AI systems that can interpret and analyze images and visual data.
  - term: Gradient Boosting
    definition: An ensemble machine learning technique that combines multiple decision trees to improve predictive accuracy, used heavily in credit scoring.
  - term: Parametric Insurance
    definition: Insurance that pays out automatically when specific measurable events occur (e.g., rainfall reaching a threshold).
  - term: Credit Invisibility
    definition: Individuals having no footprint in conventional credit bureaus, lacking formal credit history.
  - term: Proxy Discrimination
    definition: Using variables that correlate with protected characteristics (e.g., race, gender) as proxies, leading to discriminatory outcomes.
  - term: Explainable AI (XAI)
    definition: AI systems designed to be transparent, allowing humans to understand how decisions are made.
critical_citations:
  - "[Consumer Financial Protection Bureau, 2015] — Quantifies credit invisibility in the US."
  - "[Björkegren & Grissen, 2019] — Shows mobile usage predicts credit repayment."
  - "[Solon Barocas & Selbst, 2016] — Foundational work on big data's disparate impact."
  - "[Berg, Burg, Gombović, & Puri, 2019] — Demonstrates fintech credit scoring using digital footprints."
  - "[Kalluri, 2020] — Argues AI shifts power, not just good or fair."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Provides a general framework for understanding financial inclusion challenges in developing economies, relevant to this demographic.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: contextual
      justification: Discusses informal income, gig economy, and lack of formal credit, relevant to financial structures.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: contextual
      justification: Addresses behavioral nudges and savings patterns, relevant to understanding financial behavior.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: Mentions family obligations and cultural insensitivity in AI models, relevant to culturally specific practices.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: Discusses irregular income for smallholder farmers and flexible loan products aligned with harvest cycles.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: Mentions income variability and cultural patterns in spending, relevant to spending cycles.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: low
      justification: Mentioned in the context of AI analyzing transaction patterns for personalization and savings.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: low
      justification: Implicitly relevant as AI personalization requires expense categorization.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews existing fintech, mobile money, and microfinance systems, providing a landscape overview.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies barriers like credit invisibility, high costs, and exclusion as key gaps that AI addresses.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Uses clustering and classification to segment users and personalize services based on behavior.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Employs classification models and gradient boosting for behavior prediction and credit scoring.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Core to the paper, detailing use of supervised learning, time-series forecasting, and reinforcement learning.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Discusses LSTM and ARIMA for market prediction and income volatility forecasting.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Savings nudges, automated savings, and pension optimization relate to budget recommendation.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Dedicated sections on AI-powered fraud detection using supervised and unsupervised learning.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Discusses algorithms for detecting novel fraud schemes and unusual transaction patterns.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Case studies like M-Pesa and GCash highlight mobile-first financial services.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: contextual
      justification: Mentions user segmentation and personalization, which relates to UX design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Dedicated humane considerations section on privacy violations, biometric data breaches, and data protection.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Discusses transparency, accountability, and the need for recourse to build trust.
  contribution: This paper justifies Odin's core modules by providing evidence for AI-driven personalization, forecasting, and anomaly detection, while also highlighting the critical need for ethical safeguards. It validates the use of alternative data for credit scoring and behavioral profiling, directly supporting Odin's approach to user classification and budget recommendation. The analysis of existing systems and their gaps informs Odin's design rationale, particularly in addressing the limitations of traditional financial tools. Furthermore, the paper's emphasis on privacy, fairness, and mobile-first design provides a framework for Odin's principles. Its case studies from the Global South, including examples from the Philippines, offer relevant context for Odin's target demographic.
  directly_justifies:
    - "AI-driven expense categorization and personalization improve user engagement and financial management."
    - "Mobile-first financial apps like GCash demonstrate the viability of digital platforms for the target demographic."
    - "Alternative credit scoring using mobile data can address credit invisibility for Filipino young professionals."
    - "Behavioral nudges and automated savings can help users with irregular income build emergency funds."
    - "Robust fraud detection systems are essential for user trust and security in mobile finance."
  limits:
    - "Non-systematic review approach limits generalizability of findings and may miss specific quantitative details."
    - "The analysis relies heavily on case studies, which may not be representative of all contexts."
    - "The paper provides a broad overview but lacks deep technical specifics on algorithm implementation."
    - "The focus is on general financial inclusion, not specifically on a PFMS for Filipino young professionals."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was conducted for this paper. The domains flagged as relevant were: Existing Systems & Gaps (high), Behavioral Profiling (medium), Spending Forecasting (high), Budget Recommendation (medium), Anomaly Detection (high), Mobile-First Design (medium), and Data Privacy (high). The paper's focus on alternative credit scoring, fraud detection, and predictive modeling directly justifies high relevance to topics 4.B, 6.A, 6.B, 8.A, and 8.B. Its discussion of behavioral nudges and segmentation supports topics 5.A and 5.C with medium relevance. The paper's emphasis on ethical challenges, privacy violations, and the need for transparency provides high relevance to topic 10.A. The paper touches on mobile-first case studies (9.A) and cultural practices (2.A) but does not provide deep insight, hence contextual relevance. Topics like 7.C (constrained optimization) and 13.A (savings goals) were considered but rejected as the paper does not provide specific methodologies or frameworks for these areas. The paper's overall relevance to Odin is high, as it validates the use of AI for core functionalities while providing a critical lens on necessary ethical and privacy safeguards.
limitations:
  - "The study is a non-systematic review, which may be subject to selection bias in the literature and case studies chosen. [unacknowledged]"
  - "Findings from Global South case studies may not be directly generalizable to the specific context of Filipino young professionals."
  - "The paper does not provide a comparative analysis of different AI algorithms or their performance metrics in detail."
  - "The analysis focuses on AI's potential but does not empirically measure the impact of these systems on financial wellbeing or inclusion outcomes."
  - "The discussion of ethical challenges is broad and lacks specific, actionable recommendations for implementation."
remember_this:
  - AI alternative credit scoring can reduce operational costs from 12% to under 2%.
  - Alternative data models achieve predictive power comparable to traditional FICO scores.
  - AI enables access to credit but often at exploitative rates of 30-40% APR.
  - Ethical AI requires fairness audits, transparency, and human oversight.
  - Mobile money platforms demonstrate AI's potential for reaching unbanked populations.
```
---

## Paper 3: Cabiles_summarized.md

**Source File:** `Cabiles_summarized.md`

```yaml
paper_id: d7b3f9a8-4c2e-5f1a-9d6b-8e7c4a9f2d1b
designation: local
title: Financial Management Practices of Employees at Bureau Of Internal Revenue
authors: Cabiles, S. L.
year: 2025
venue: United International Journal for Research & Technology
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 3.A
  - 3.B
  - 4.B
  - 5.A
  - 7.A
  - 13.A
  - 13.B
tldr: Employees exhibit strong budgeting and saving behaviors but inconsistent spending and investing practices, with debt accumulation and impulse spending as key barriers.
problem_and_motivation: The study addresses the need to understand the personal financial management practices of employees to identify gaps and propose targeted interventions. Effective financial management is essential for employees to navigate economic uncertainties and secure their financial future. The research specifically focuses on permanent employees of the Bureau of Internal Revenue to inform the development of financial literacy programs.
approach:
  - A quantitative descriptive research design was used to assess financial practices and literacy levels.
  - Data was collected using a Likert-scale questionnaire administered online and via pen-and-paper to permanent employees of BIR RDO 068.
  - Descriptive statistics including frequency count, percentage, ranking, and weighted mean were used for analysis.
  - The study focused on four financial domains: budgeting, spending, saving, and investing.
  - The research also identified challenges encountered in managing and planning finances through frequency distribution.
findings:
  - Employees demonstrate strong budgeting and saving behaviors, with high mean scores for emergency fund maintenance (4.32) and setting aside savings (4.37).
  - Spending practices are less consistent, with moderate engagement in aligning purchases with financial goals (3.50) and some impulse buying (3.20).
  - Investing practices are the weakest domain, with inconsistent engagement across all measured items and a value-action gap identified.
  - Financial literacy engagement is predominantly self-directed and moderate, with average mean scores ranging from 2.90 to 3.27 across domains.
  - Accumulation of debt and lack of awareness about interest rates are the most significant challenges, ranking first and second among identified barriers.
key_figures_tables:
  - "Table 1: Budgeting Practices: Mean scores for emergency fund (4.32) and expense tracking (4.03) indicate strong practices."
  - "Table 2: Spending Practices: Mean score for prioritizing quality (4.10) suggests disciplined spending, but impulse buying (3.20) remains a concern."
  - "Table 3: Saving Practices: High mean scores for regular saving (4.37) and emergency funds (4.20) reflect responsible habits."
  - "Table 4: Investing Practices: Low mean scores (2.66-3.51) indicate cautious behavior and a knowledge-action gap."
  - "Table 5: Financial Literacy Engagement: Low average means across domains highlight the need for structured programs."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Value-Action Gap (VAG)"
    definition: "The disparity between an individual's beliefs and their actual behavior."
  - term: "Mental Accounting"
    definition: "The way individuals categorize their expenses and perform cost-benefit analysis."
  - term: "Financial Well-being"
    definition: "A state where a person can fully meet current and ongoing financial obligations, feels secure in their financial future, and can make choices that allow enjoyment of life."
critical_citations:
  - "[Ali et al., 2024] — Links mental budgeting to better financial management."
  - "[Lusardi, 2019] — Highlights workplace financial education as effective."
  - "[Tamplin, 2025] — Emphasizes expense tracking for financial control."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "medium"
      justification: "Study focuses on Filipino employees, a subset relevant to the demographic."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "medium"
      justification: "Details salary, debt, and savings structures of Filipino employees."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Directly analyzes budgeting, spending, saving, and investing behaviors of Filipino employees."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "contextual"
      justification: "Mentions family socialization and cultural values as influences on financial behavior."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "medium"
      justification: "Investigates budgeting and spending practices, which are foundational to categorization."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      relevance: "low"
      justification: "Tangentially discusses expense tracking but not category design."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Identifies gaps in financial literacy engagement and application of knowledge."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Describes employee financial behaviors, which can inform profile construction."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "high"
      justification: "Directly examines budgeting strategies and their effectiveness."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "high"
      justification: "Directly analyzes saving practices and goals."
    - code: "13.B"
      name: "Debt Management in PFMS"
      relevance: "high"
      justification: "Identifies debt accumulation as a primary challenge."
  contribution: "This study provides empirical data on the financial behaviors of Filipino government employees, which can inform the design of the behavioral profiling and budgeting modules in Odin. The identified gaps in financial literacy and practical application highlight the need for personalized financial education and coaching features. The findings on debt accumulation and impulse spending support the development of debt management and anomaly detection components. The paper's recommendations for structured financial literacy programs justify the need for educational content within a PFMS."
  directly_justifies:
    - "Employees demonstrate strong budgeting but inconsistent investing, justifying behavioral profile calibration."
    - "Accumulation of debt due to unfamiliarity with interest rates supports a need for debt literacy modules."
    - "The value-action gap in investing indicates a need for behavioral nudges in financial planning features."
  limits:
    - "Focus on a single government office limits generalizability to other sectors or demographics."
    - "Relies on self-reported data, which may be subject to social desirability bias."
    - "Does not evaluate the effectiveness of specific financial literacy interventions."
  mapping_rationale: "A systematic scan of all 12 functional domains was conducted against the paper's content. Domains related to Filipino cultural context (2.A), expense categorization (3.A, 3.B), existing systems gaps (4.B), behavioral profiling (5.A), budgeting (7.A), and savings/debt management (13.A, 13.B) were flagged as relevant. The paper's focus on employee practices and challenges directly supports topics 1.C, 7.A, 13.A, and 13.B with high relevance. Topics 1.A, 1.B, 3.A, 4.B, and 5.A were assigned medium relevance for providing supporting context. Topic 2.A was deemed contextual due to its indirect mention of cultural influences. Other domains, including forecasting (6.A, 6.B), anomaly detection (8.A, 8.B), mobile-first design (9.A, 9.B), data privacy (10.A, 10.B), retention (11.A), and system evaluation (12.A, 12.B), were considered but rejected as the paper does not address these algorithmic or design-specific areas. The overall relevance is medium to high, providing foundational behavioral data but lacking in technical specifications for Odin's computational modules."
limitations:
  - "The study is limited to a single Revenue District Office, which may not represent all BIR employees."
  - "Cross-sectional design limits causal inference regarding the impact of financial literacy on practices."
  - "The study relies on self-reported data, which can introduce bias. [unacknowledged]"
  - "No direct measure of actual financial behavior was used, only reported practices. [unacknowledged]"
remember_this:
  - "Employees frequently set up emergency funds, indicating strong saving behavior."
  - "The value-action gap shows that investment knowledge does not translate to practice."
  - "Debt accumulation is the primary financial challenge for government employees."
  - "Financial literacy programs can improve saving habits and investment decisions."
  - "Structured financial education is needed to bridge the gap between knowledge and application."
```
---

## Paper 4: Rodriguez-Correa et al_summarized.md

**Source File:** `Rodriguez-Correa et al_summarized.md`

```yaml
paper_id: 10.12688/f1000research.159085.3
designation: international
title: Financial literacy among young college students: Advancements and future directions
authors: Rodriguez-Correa, P. A.; Arias García, S.; Bermeo-Giraldo, M. C.; Valencia-Arias, A.; Martínez Rojas, E.; Aurora Vigo, E. F.; Gallegos, A.
year: 2025
venue: F1000Research
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.C
  - 3.A
  - 3.C
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 7.A
  - 8.A
  - 9.A
  - 9.B
  - 10.A
  - 11.A
  - 12.A
tldr: A systematic review of 44 studies identifies financial knowledge and behavior as dominant but unevenly explored themes among college students, with gaps in budgeting, credit, and fintech.
problem_and_motivation: Young adults face increasing financial responsibilities and are vulnerable to poor financial decisions. Existing research on financial literacy for this group is fragmented and focuses on broad categories. A structured overview of specific subtopics is needed to guide educational and policy interventions.
approach:
  - A systematic literature review was conducted following the PRISMA-2020 methodology.
  - The search was performed in Scopus and Web of Science using title-specific keywords.
  - Inclusion criteria required studies on higher education students with statistical analysis of financial literacy variables.
  - A quality assessment checklist scored documents from 1 to 3, with only score 3 included.
  - The analysis synthesized data from 44 peer-reviewed studies published between 2003 and 2023.
findings:
  - num: 44 peer-reviewed studies were analyzed, with 34% using regression analysis.
  - Financial literacy is the most evaluated construct, but its definition varies widely across studies.
  - Financial knowledge and financial behavior are the most frequently examined themes.
  - Budgeting, credit/debt management, and fintech adoption are underexplored subtopics.
  - Socio-demographic variables like gender and parental education are commonly measured but cultural factors are often overlooked.
  - Financial self-efficacy emerges as a key moderating factor between knowledge and behavior.
  - The literature shows a shift towards broader concepts like financial capability and financial well-being.
  - Emerging economies and Eastern Europe are identified as underrepresented regions in research.
  - The relationship between fintech and financial literacy is identified as a major research gap.
  - A future research agenda highlights financial knowledge, behavior, inclusion, and budgeting as key areas.
key_figures_tables:
  - Figure 1: PRISMA flow diagram showing selection of 44 studies from 350 initial records → Systematic process yielded 44 relevant studies.
  - Figure 2: Bar chart showing most recurring financial literacy variables → Financial literacy, knowledge, and behavior are the top three constructs.
  - Figure 3: Research agenda with keyword trends → Financial knowledge and behavior are currently active and future topics.
  - Table 2: Summary of 44 studies with objectives, methods, and countries → Regression analysis and SEM are dominant methods.
  - Table 3: Research gaps categorized by theme, geography, and temporality → Social class, fintech impact, and emerging markets need study.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Financial Literacy
    definition: The ability to understand and manage personal finances, including budgeting, saving, and using credit responsibly.
  - term: Financial Knowledge
    definition: Familiarity with financial terms and concepts needed for daily financial functioning.
  - term: Financial Behavior
    definition: Actions and patterns exhibited by individuals in managing their financial resources.
  - term: Financial Attitude
    definition: An individual's state of mind, opinion, and judgment regarding financial decisions.
  - term: Financial Self-Efficacy
    definition: Confidence in one's ability to acquire information and make effective financial decisions.
critical_citations:
  - "[Lusardi & Mitchell, 2023] — Defines financial literacy's core concepts and importance."
  - "[Xiao et al., 2022] — Introduces financial capability as an expanded framework."
  - "[Blanco et al., 2024] — Highlights social determinants and disparities in financial knowledge."
  - "[Bartholomae & Fox, 2021] — Reviews college student financial behavior and well-being."
  - "[Goyal & Satish, 2021] — Provides a systematic review and bibliometric analysis of financial literacy."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Focuses on college students, a key sub-demographic of young professionals.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: contextual
      justification: Discusses income sources (scholarships, jobs) and financial responsibilities.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Directly reviews financial behavior patterns in college students.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: Mentions cultural norms but lacks specific focus on Filipino practices.
    - code: 2.C
      name: User-Declared Financial Preferences
      relevance: low
      justification: Addresses financial attitudes and self-efficacy, not explicit user preferences.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: low
      justification: Discusses budgeting but not specific categorization frameworks.
    - code: 3.C
      name: User-Defined Allocation Constraints
      relevance: low
      justification: Mentions budgeting but not user-defined constraints.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Reviews the literature but not specific existing systems.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Systematically identifies research gaps in financial literacy for college students.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Reviews financial behavior as a key variable.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: low
      justification: Does not address profile dynamics or cold-start issues.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Does not focus on classification approaches.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: contextual
      justification: Mentions predictive approaches but not specific modeling.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Highlights budgeting as a core thematic gap.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: No direct mention of anomaly detection.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: contextual
      justification: Mentions fintech and digital tools but not mobile-first design specifically.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: contextual
      justification: Mentions fintech and digital tools but not UX design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: No direct mention of data privacy.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: Mentions behavior but not engagement dynamics.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: low
      justification: Discusses review methodology but not system evaluation.
  contribution: This paper provides a systematic overview of financial literacy research relevant to young professionals, which can inform Odin's design by identifying key behavioral and knowledge domains. The identification of research gaps in budgeting, credit, and fintech use directly justifies the need for Odin's features in these areas. The findings on financial behavior and attitudes can guide the development of behavioral profiling modules. The paper's emphasis on digital tools and financial self-efficacy supports the rationale for a mobile-first, user-empowering PFMS.
  directly_justifies:
    - "Budgeting skills are a recurring theme, but students are least interested in this process."
    - "Students with low financial knowledge may misuse credit cards and incur uncontrollable debt."
    - "Financial self-efficacy emerges as a moderating factor between knowledge and behavior."
    - "There is a gap in assessing the actual effectiveness of digital financial tools in improving literacy."
    - "Gender, parental education, and income significantly influence financial literacy levels."
  limits:
    - "The search was limited to Scopus and Web of Science, possibly excluding relevant studies."
    - "Search terms were restricted to titles, potentially missing studies using different keywords."
    - "The review focuses primarily on financial literacy and may not fully capture financial capability/wellbeing."
    - "The use of specific bibliometric tools may have constrained the analysis."
    - "The search did not include related terms like 'financial knowledge' or 'financial skills'."
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The paper was flagged as relevant primarily for domains related to Behavioral Profiling & Classification, Existing Systems & Gaps, and Budget Recommendation. Topic codes 1.A, 1.B, 1.C, 2.A, 2.C, 3.A, 3.C, 4.A, 4.B, 5.A, 7.A, 9.A, and 9.B were assigned medium or contextual relevance because the paper provides foundational evidence on demographics, behavior, and system gaps but does not directly address Odin's algorithmic or design specifics. Codes 6.A, 8.A, 10.A, 11.A, and 12.A were considered low or contextual as the paper does not cover predictive modeling, anomaly detection, privacy, or engagement mechanics. The borderline case of 2.A (cultural practices) was marked contextual due to the lack of a specific Filipino focus. The overall relevance to Odin is medium, providing a strong literature foundation for several modules, especially behavioral profiling and identifying system gaps.
limitations:
  - "The search strategy was limited to Scopus and Web of Science."
  - "Only titles were searched, not abstracts or full texts."
  - "The review covers up to 2023, missing very recent studies."
  - "Related terms like 'financial knowledge' were not included in the initial search."
  - "Only documents with a score of 3 (correlational studies) were included, excluding descriptive works."
  - "The search did not include 'University' or 'College' as separate terms in the title search."
  - "Potential language bias exists as only English articles were included."
remember_this:
  - "Financial literacy definitions vary widely across studies."
  - "Budgeting, credit, and fintech use are key research gaps."
  - "Financial self-efficacy mediates the knowledge-behavior link."
  - "Gender and parental education significantly influence financial literacy."
  - "The field is shifting from literacy to capability and well-being."
```
---

## Paper 5: Sanhosh & Singh_summarized.md

**Source File:** `Sanhosh & Singh_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international-algorithm-specific
title: Digital Persona Modeling for Context-Aware Financial Decisioning
authors: Sanhosh, S. R.; Singh, A. K.
year: 2025
venue: International Journal of Research in Mulidisciplinary Technology
odin_topics:
  - 5.A
  - 6.A
  - 9.A
  - 10.A
  - 10.B
  - 7.B
  - 8.A
  - 1.A
  - 2.A
  - 2.B
  - 3.A
  - 4.A
  - 4.B
  - 12.A
  - 12.B
  - 13.A
tldr: Digital Persona Modeling integrates behavioral and contextual data to enable adaptive, context-aware financial decisioning systems.
problem_and_motivation: Static demographic profiles are insufficient for addressing real-time and contextual financial needs. There is a need for intelligent systems that can understand and adapt to individual user behaviors and contexts. This paper proposes a digital persona framework to fill this gap.
approach:
  - The system architecture has five layers: Data Acquisition, Context Engine, Persona Builder, Decisioning Model, and Decision Delivery & Feedback.
  - A simulated hybrid dataset was used, combining transactional logs, mobile contextual logs, user profiles, and feedback labels.
  - Random Forest is used for interpretable classification of financial decisions based on contextual features.
  - LSTM Neural Network captures sequential patterns in user behavior for personalized decision-making.
  - K-Means Clustering segments users into distinct persona groups based on contextual traits.
findings:
  - num: LSTM achieved the highest accuracy of 93.6% and F1-score of 92.9%.
  - num: Random Forest achieved 91.2% accuracy and a 90.1% F1-score.
  - num: K-Means Clustering performed lower with 75.0% accuracy and a 71.8% F1-score.
  - The LSTM model's superiority is due to its ability to model temporal dependencies in user behavior.
  - The proposed framework demonstrates that contextual integration improves decision relevance and user alignment.
key_figures_tables:
  - Table 2: Model Performance Comparison → Shows LSTM outperforms Random Forest and K-Means on all metrics.
  - Figure 2: System Architecture of Proposed Framework → Visualizes the five-layer data flow from acquisition to feedback.
key_equations:
  - equation: S(u,p) = (1/n) * Σ_{i=1}^{n} ( |x_{u,i} - x_{p,i}| / max(x_i) )
    explanation: Similarity score matching a user to a persona group.
  - equation: R = α1*C_location + α2*C_time + α3*C_device + β*T
    explanation: Real-time decision risk function based on context and transaction amount.
definitions:
  - term: DPM
    definition: Digital Persona Modeling
  - term: XAI
    definition: Explainable Artificial Intelligence
critical_citations:
  - "[Richardson, 2024] — Foundational for real-time payment system challenges."
  - "[Rautaray & Tayagi, 2023] — Supports AI applications in telecom and finance."
  - "[De Roure, 2024] — Provides basis for AI in industrial and financial IoT."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Core focus on modeling dynamic behavioral profiles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Uses LSTM and other models for predictive financial decisions.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Discusses data from mobile apps and device context.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Addresses privacy via federated learning and local processing.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Highlights explainability and interpretability for trust.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Mentions automated budgeting as a key use case.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Lists fraud intent detection as a use case.
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Mentions underserved entrepreneurs but not Filipino-specific.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: Discusses diversity but not culturally specific practices.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Temporal analysis could inform cyclical patterns.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: Persona modeling could support categorization.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Mentions gaps in static systems.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Explicitly addresses limitations of static profiles.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides a multi-metric evaluation (accuracy, F1, PRL).
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Compares RF, LSTM, and K-Means.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: Mentions investment recommendations tangentially.
  contribution: The paper provides a conceptual and architectural foundation for DPM in intelligent finance. This directly supports Odin's development of dynamic user profiles. The proposed multi-layered architecture can inform Odin's system design for real-time personalization. The privacy-preserving modeling approach using federated learning is relevant to Odin's data governance. The integration of behavioral and contextual data can enhance Odin's decision support modules.
  directly_justifies:
    - Dynamic user profiles can improve financial recommendation relevance.
    - Integrating contextual data enhances real-time financial decision accuracy.
    - Privacy-preserving techniques are essential for user trust in PFMS.
    - LSTM models are effective for capturing sequential spending behaviors.
  limits:
    - The paper uses a synthetic dataset, not real-world data.
    - Model generalizability may be limited across diverse populations.
    - Interpretability challenges remain for deep learning components.
    - Context drift over time is not fully addressed.
    - No specific implementation or deployment details are provided.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. High relevance was found for Behavioral Profiling (5.A) and Predictive Modeling (6.A), as the paper's core is modeling dynamic digital personas for financial decisions. Medium relevance was assigned to Mobile-First Design (9.A) due to its mobile data focus, Data Privacy (10.A) for its emphasis on privacy-preserving modeling, and User Trust (10.B) via explainability. Other topics like 1.A, 2.A, 2.B, 3.A, 4.A, 4.B, 7.B, 8.A, 12.A, 12.B, and 13.A received low, contextual, or medium relevance due to being tangential but cited in the paper. The paper was considered and rejected for topics like 2.C, 3.C, 6.B, 7.A, 7.C, 7.D, 8.B, 8.C, 9.B, 11.A, 11.B, 12.C, 13.B, and 13.C due to a lack of specific discussion on those aspects. Overall, the paper is highly relevant to Odin's goal of building a dynamic user model.
limitations:
  - Data Privacy Concerns: Heavy reliance on sensitive user data increases breach risk. [unacknowledged]
  - Limited Dataset Diversity: Synthetic data may introduce bias and limit generalizability. [unacknowledged]
  - Model Generalizability: Models may not generalize well to unseen patterns in evolving ecosystems. [unacknowledged]
  - Interpretability Challenges: Deep learning models like LSTM can act as black boxes. [unacknowledged]
  - Context Drift Over Time: User behavior evolves, requiring continuous adaptation not fully addressed. [unacknowledged]
remember_this:
  - LSTM achieved the highest accuracy at 93.6% for decision classification.
  - Digital personas enable context-aware adaptation beyond static profiles.
  - Privacy-preserving modeling via federated learning is a key design focus.
  - Multi-source data fusion is essential for creating accurate user personas.
  - The proposed architecture supports real-time, personalized financial decisions.
```
---

## Paper 6: Yang R. et al_summarized.md

**Source File:** `Yang R. et al_summarized.md`

```yaml
paper_id: 10.53941/tai.2025.100009
designation: international
title: Recent Advances in Artificial Intelligence for Management and Financial Technology
authors: Yang, R.; Wang, Y.; Luo, Y.; Yang, Z.; Zong, Z.; Wu, D.O.
year: 2025
venue: Transactions on Artificial Intelligence
odin_topics:
  - 1.A
  - 1.B
  - 3.A
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
tldr: Surveys AI applications in FinTech, focusing on recommendation systems, risk analysis, and AI-generated commercial content, while addressing challenges in data privacy, transparency, and cultural bias.
problem_and_motivation: Financial institutions face challenges including regulated environments, severe class-imbalance, extreme tail risks, and rapidly shifting consumer preferences. These challenges challenge the direct transplantation of generic AI techniques developed for other industries, necessitating domain-specific innovation and rigorous evaluation.
approach:
  - Reviews self-supervised learning and graph neural networks for financial product recommendation systems.
  - Examines large language models like GPT-4 and Llama 3 with prompt engineering for SME credit assessment and stress testing.
  - Surveys multimodal generative models such as DALL-E 3 for automated commercial advertising content generation.
  - Discusses regulatory restrictions, user trust mechanisms, and return-risk balance in financial recommendation systems.
  - Analyzes Chain of Thought prompting for breaking down complex financial risk issues into manageable problems.
  - Reviews Explainable AI (XAI) techniques for transparency in AI-driven financial risk analysis.
  - Surveys data governance, cultural sensitivity filters, and bias detection methods for AIGC in advertising.
findings:
  - "num: LLMs reduce risk analysis cycles from weeks to minutes for SMEs."
  - "num: Nestle’s AI recommendation system increased sales revenue by 6% in the first half of 2022."
  - "num: AIGC reduced design workload from five designers per week to two to three days."
  - Self-supervised learning mitigates data sparsity issues in deep recommendation models.
  - Advanced prompt engineering is essential for effective financial forecasting with LLMs.
  - AIGC significantly improves ad production efficiency and precision but poses copyright and cultural misuse risks.
  - Explainable AI is critical for building user trust and meeting regulatory compliance in fintech.
key_figures_tables:
  - "Figure 1: Workflow of AI recommendation system → Illustrates data collection, preprocessing, feature extraction, model training, and recommendation generation."
  - "Figure 2: Latent semantic model in recommendation system → Shows matrix factorization mapping users and content to latent space for similarity calculation."
  - "Table 1: Comparison of literature on key financial AI recommendation system themes → Summarizes approaches for regulatory restrictions, user trust, and return-risk balance."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "AIGC"
    definition: "Artificial Intelligence Generated Content; content created using generative AI technology."
  - term: "CoT"
    definition: "Chain of Thought; a prompting technique that breaks down complex problems into smaller, manageable steps."
  - term: "FinTech"
    definition: "Financial Technology; technology and innovation aimed at competing with traditional financial methods."
  - term: "LLM"
    definition: "Large Language Model; a type of AI model trained on vast text data to understand and generate human-like language."
  - term: "SME"
    definition: "Small and Medium-sized Enterprise; a business that maintains revenues, assets, or a number of employees below a certain threshold."
  - term: "SSL"
    definition: "Self-supervised Learning; a machine learning paradigm where models learn from unlabeled data."
  - term: "XAI"
    definition: "Explainable Artificial Intelligence; AI systems designed to be interpretable and transparent to human users."
critical_citations:
  - "[Covington et al., 2016] — Introduced DNNs for YouTube recommendations."
  - "[Wu et al., 2016] — Proposed collaborative denoising autoencoders for recommendations."
  - "[Bussmann et al., 2020] — Demonstrated explainable ML in fintech risk management."
  - "[Yu et al., 2023] — Leveraged GPT-4 for financial market news summarization and prediction."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "contextual"
      justification: "Provides general context on AI in FinTech, but does not specifically address Filipino YPs."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "low"
      justification: "Discusses SME financial risks, indirectly relevant to personal financial structures."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "medium"
      justification: "Reviews recommendation systems that analyze user behavior and preferences, relevant to categorization."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Surveys AI applications in FinTech, providing a broad view of the existing landscape."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Explicitly discusses data sparsity, cold-start, privacy, and transparency gaps in AI systems."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "low"
      justification: "Mentions analyzing user behavior for recommendations, tangentially related to profiling."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "medium"
      justification: "Identifies the cold-start problem as a key challenge for recommendation systems."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "low"
      justification: "Mentions machine learning for user classification, but not as a primary focus."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews predictive modeling for risk analysis and stock prediction."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "medium"
      justification: "Discusses time series forecasting for financial market prediction and cash flow risks."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "low"
      justification: "Mentions fraud detection in risk analysis context, tangentially related."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "low"
      justification: "References fraud detection as an application, but does not detail algorithms."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "Dedicates significant discussion to data privacy challenges in AIGC and recommendation systems."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "high"
      justification: "Discusses user trust mechanisms, transparency, and explainability as key factors for adoption."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Evaluates forecasting performance as a benchmark for financial NLP models."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Reviews evaluation of recommendation and forecasting models in financial contexts."
  contribution: "This survey provides a comprehensive overview of AI techniques applicable to Odin's recommendation, risk analysis, and content generation modules. It justifies the use of self-supervised learning to address data sparsity in user preference modeling, which is critical for Odin's expense categorization and forecasting. The discussion on prompt engineering with LLMs offers a methodology for automating financial insights and risk assessment, supporting Odin's budgeting and anomaly detection features. The analysis of AIGC highlights both opportunities and risks for user engagement content, directly informing Odin's design for user retention and trust."
  directly_justifies:
    - "Self-supervised learning mitigates data sparsity in recommendation systems, improving cold-start performance."
    - "Prompt engineering with large language models enables automated, explainable risk analysis."
    - "Explainable AI is essential for building user trust and meeting regulatory compliance in financial systems."
    - "Cultural sensitivity filters are necessary to prevent misuse and bias in AI-generated content."
  limits:
    - "The survey is broad and does not provide empirical validation of any specific technique."
    - "Focuses on international financial contexts, with limited applicability to Filipino-specific practices."
    - "Does not address the integration of multiple AI modules into a cohesive personal finance management system."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains flagged as relevant include: Existing Systems & Gaps (4.A, 4.B) with high relevance due to explicit discussion of system limitations; Data Privacy & User Trust (10.A, 10.B) with high relevance due to dedicated sections; Expense Categorization (3.A) and Behavioral Profiling (5.B) with medium relevance due to discussion of recommendation systems and cold-start; Predictive Modeling (6.A, 6.B) with medium relevance due to forecasting applications; and Evaluation (12.A, 12.B) with medium relevance due to benchmarking discussions. Domains such as Filipino Cultural Context (2.A-D) and Savings & Debt Management (13.A-C) were considered and rejected as the paper is international in scope and does not address these specific areas. A borderline case involved the discussion of recommendation systems, which touches both 3.A (categorization) and 5.B (cold-start), and was resolved by assigning medium relevance to both based on the degree of direct evidence. The paper offers broad, high-level insights into AI techniques applicable to Odin, but is not specifically tailored to the Filipino context or the PFMS domain."
limitations:
  - "No empirical validation of specific techniques."
  - "Focus on international financial contexts; may not generalize to Philippine-specific practices."
  - "Does not address integration of AI modules into a cohesive personal finance system."
  - "Assumes availability of large-scale data for training, which may not be feasible for Odin. [unacknowledged]"
  - "Potential cultural bias in AIGC models discussed, but solutions are not deeply evaluated. [unacknowledged]"
remember_this:
  - "LLMs reduce risk analysis cycles from weeks to minutes for SMEs."
  - "Self-supervised learning addresses data sparsity in recommendation systems."
  - "AIGC reduces design workload from five designers per week to two to three days."
  - "Explainable AI is critical for user trust and regulatory compliance."
  - "Data privacy and cultural sensitivity are key challenges for AI in FinTech."
```
---

## Paper 7: Ling & Weiling_summarized.md

**Source File:** `Ling & Weiling_summarized.md`

```yaml
paper_id: 10.1109/ACCESS.2025.3550339
designation: international-algorithm-specific
title: Enhancing Segmentation: A Comparative Study of Clustering Methods
authors: Ling, L. S.; Weiling, C. T.
year: 2025
venue: IEEE Access
odin_topics:
  - 5.C
  - 12.B
tldr: A comparative study of nine clustering methods for customer segmentation in e-marketing finds K-Means++ achieves the highest Silhouette Score (0.5012) and lowest Davies-Bouldin Index (0.7481).
problem_and_motivation: E-marketing businesses lack a structured customer segmentation plan, and traditional manual methods fail to capture dynamic online consumer behavior patterns at scale. Automated unsupervised clustering approaches are needed to enable targeted marketing and improve customer satisfaction.
approach:
  - Two Kaggle retail datasets (1.07M and 9,994 records) were preprocessed with missing value removal, date conversion, and transaction filtering.
  - RFM (Recency, Frequency, Monetary) analysis was performed, followed by IQR-based outlier removal and min-max normalization.
  - Nine clustering methods were compared: K-Means, K-Medoids, Agglomerative, DBSCAN, Fuzzy C-Means, K-Means++, Mini Batch K-Means, Mean Shift, and GMM.
  - Optimal cluster counts were determined using the Elbow Method, with validation via Silhouette Score and Davies-Bouldin Index.
  - CLV prediction was performed using Random Forests and Gradient Boosting with hyperparameter tuning via RandomizedSearchCV.
findings:
  - num: K-Means++ achieved the highest Silhouette Score of 0.5012 and lowest Davies-Bouldin Index of 0.7481 at K=4.
  - num: GMM performed poorly with a Silhouette Score of 0.0452 and Davies-Bouldin Index of 2.6394.
  - num: Gradient Boosting after hyperparameter tuning achieved MAE as low as 1.56 and R-squared of 0.9999 for CLV prediction.
  - K-Means++ demonstrated greater stability and consistency compared to standard K-Means across multiple executions.
  - Method 2 (proposed with K-Means++ and K-Medoids) outperformed Method 1 (standard K-Means) for K-Medoids clustering.
  - Mean Shift and K-Medoids produced intermediate results with Silhouette Scores of 0.4027 and 0.3894 respectively.
key_figures_tables:
  - Table 4: K-Means++ performance metrics across K values → Optimal clustering at K=4 with Silhouette 0.501 and Davies-Bouldin 0.748.
  - Table 24: Comparison of all clustering methods → K-Means++ is the most effective for customer segmentation.
  - Figure 10: Elbow Method for K-Means on Dataset 1 → Optimal number of clusters is K=4.
  - Figure 11: Elbow Method for K-Means on Dataset 2 → Optimal number of clusters is also K=4.
key_equations:
  - equation: Silhouette Score = (b - a) / max(a, b)
    explanation: Measures cluster cohesion and separation.
  - equation: Davies-Bouldin Index = average similarity between each cluster and its most similar cluster
    explanation: Lower values indicate better cluster separation.
definitions:
  - term: RFM
    definition: Recency, Frequency, Monetary analysis for customer segmentation.
  - term: CLV
    definition: Customer Lifetime Value, predicting long-term customer profitability.
  - term: IQR
    definition: Interquartile Range, used for outlier detection.
  - term: WCSS
    definition: Within-Cluster Sum of Squares, used in the Elbow Method.
critical_citations:
  - "[Mufarroha et al., 2022] — K-Means and K-Medoids clustering for online retail segmentation."
  - "[Zhao and Li, 2021] — K-Means++ for e-commerce customer segmentation."
  - "[Regmi et al., 2022] — Comparison of K-Means, Agglomerative, and DBSCAN clustering."
relevance:
  topics:
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Compares clustering methods for customer segmentation based on behavioral RFM data.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Systematically evaluates clustering algorithms using Silhouette Score and Davies-Bouldin Index.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: Segmentation of consumers by purchase behavior relates to behavioral profiling but is not PFMS-specific.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: contextual
      justification: Uses established clustering evaluation metrics applicable to PFMS module assessment.
  contribution: This paper validates K-Means++ as the preferred clustering algorithm for behavioral customer segmentation based on RFM features, which can inform Odin's user profiling module. The comparative evaluation framework using Silhouette Score and Davies-Bouldin Index provides a methodological template for assessing Odin's classification components. The CLV prediction pipeline using Gradient Boosting with hyperparameter tuning demonstrates an approach that could be adapted for Odin's user value estimation. However, the paper focuses on e-marketing rather than personal finance management, limiting direct applicability to Odin's core PFMS functionality.
  directly_justifies:
    - K-Means++ outperforms other clustering methods for customer segmentation with Silhouette Score of 0.5012.
    - Gradient Boosting with hyperparameter tuning achieves high accuracy (R-squared 0.9999) for CLV prediction.
    - The Silhouette Score and Davies-Bouldin Index are effective metrics for evaluating clustering quality.
    - Clustering based on RFM features enables identification of loyal, at-risk, and high-value customer segments.
  limits:
    - The study uses e-marketing retail data rather than personal finance transaction data, limiting direct transferability.
    - Clustering methods were evaluated on only two Kaggle datasets, both from retail contexts.
    - The study did not explore deep learning or neural network-based clustering approaches.
    - Performance may vary when applied to the distinct spending patterns of Filipino young professionals.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged for relevance primarily in the Behavioral Profiling & Classification domain (5.A, 5.C) and System Evaluation domain (12.A, 12.B). Topic 5.C was assigned medium relevance because the paper directly compares clustering algorithms for segmenting consumers based on behavioral data (RFM), which can inform Odin's classification of user financial behavior. Topic 12.B was assigned medium relevance because the paper provides a rigorous comparative evaluation of algorithmic modules with established metrics. Topic 5.A was assigned contextual relevance because while the paper segments consumers, it does not specifically address financial behavioral profiles in the PFMS context. Topic 12.A was assigned contextual relevance as the evaluation framework is generalizable but not PFMS-specific. The Filipino Cultural Context domain (2.A-D) was rejected as the paper does not address Philippine culture or seasonal spending patterns. Expense Categorization (3.A-C) was rejected as the paper segments customers, not expenses. Existing Systems (4.A-B), Spending Forecasting (6.A-B), Budget Recommendation (7.A-D), Anomaly Detection (8.A-C), Mobile Design (9.A-B), Data Privacy (10.A-B), User Retention (11.A-B), and Savings/Debt Management (13.A-C) were all rejected as the paper does not address these PFMS-specific areas. Overall, the paper offers methodological insights for behavioral classification and algorithmic evaluation but is not directly applicable to Odin's PFMS core functions.
limitations:
  - "Focus on e-marketing data limits generalizability to PFMS contexts."
  - "Only a limited selection of clustering methods was evaluated."
  - "Scalability of GMM and Mean Shift to large datasets was not thoroughly addressed."
  - "Sensitivity to initial parameters for K-Means and K-Means++ remains a concern."
  - "The analysis is based on data from 2010-2013, which may not reflect current consumer behavior. [unacknowledged]"
remember_this:
  - K-Means++ achieved the best segmentation with Silhouette Score 0.5012.
  - Gradient Boosting after tuning reached R-squared 0.9999 for CLV prediction.
  - RFM analysis enables identification of loyal and at-risk customer segments.
  - K-Means++ offers more stable clustering than standard K-Means across multiple runs.
  - Silhouette Score and Davies-Bouldin Index are effective for clustering evaluation.
```
---

## Paper 8: Metha_summarized.md

**Source File:** `Metha_summarized.md`

```yaml
paper_id: 10.21203/rs.3.rs-6951546/v1
designation: international-algorithm-specific
title: Autonomous AI Agents for Personalized Financial Negotiation in Consumer Banking
authors: Metha, S.
year: 2025
venue: Research Square
odin_topics:
  - 2.C
  - 3.C
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 7.C
  - 7.D
  - 8.C
  - 10.A
  - 10.B
  - 12.A
  - 12.B
  - 13.B
tldr: Autonomous AI agents using multi-agent reinforcement learning negotiate financial terms on behalf of consumers, improving utility and efficiency over advisor-assisted methods.
problem_and_motivation: Consumers lack true negotiation power in financial transactions, while institutions deploy sophisticated AI for optimization. Existing robo-advisors and chatbots are reactive, not strategic advocates. An autonomous agent that can dynamically negotiate on behalf of users is needed to restore balance.
approach:
  - Simulation environment based on POMDP for bilateral negotiation episodes between user and institutional agents.
  - Synthetic dataset generated from real-world APR distributions, institutional policies, and Monte‑Carlo user profiles.
  - MARL framework with self‑play and curriculum learning, using PPO for policy optimization.
  - Utility functions and counter‑offer generation with constrained optimization and concession strategies.
  - Evaluation across mortgage, credit card, insurance, and subscription products using win‑rate, utility gain, and fairness metrics.
findings:
  - num: 92% win rate for AI negotiator versus 76% for advisor‑assisted and 61% for user‑driven.
  - num: 42% higher average user utility gain compared to static advisor systems.
  - num: 30% fewer negotiation steps to reach agreement.
  - num: 65% first‑counteroffer acceptance rate, versus 34% for scripted advisors.
  - num: Zero‑shot generalization to new product types retained 83% performance, improving to 92% with domain calibration.
  - Explainability–performance trade‑off observed: rules‑based strategies underperform deep models in high‑stakes interactions.
  - Cold‑start problem reduces early performance without transfer learning or bootstrapped simulation.
key_figures_tables:
  - Figure 1: System architecture overview → Modular agent design with user modeling, negotiation engine, and communication layers.
  - Figure 4: Negotiation trajectory over interest rate and term → Convergence is achieved within 4–6 steps.
  - Table 1: Comparative performance metrics → AI agent outperforms advisor‑assisted and user‑driven across all metrics.
key_equations:
  - equation: "U_u(O) = -w_1 \\cdot r - w_2 \\cdot t / 60"
    explanation: User utility inversely proportional to interest rate and term length.
  - equation: "\\text{Offer}^* = \\arg\\max_{x \\in X} [ U_u(x) \\cdot P_{accept}(x) - \\lambda \\cdot C(x, x_{t-1}) ]"
    explanation: Optimal offer balances utility, acceptance probability, and concession cost.
definitions:
  - term: MARL
    definition: Multi‑Agent Reinforcement Learning; agents learn policies in environments with multiple interacting decision‑makers.
  - term: PPO
    definition: Proximal Policy Optimization; a policy gradient method for stable and sample‑efficient training.
  - term: POMDP
    definition: Partially Observable Markov Decision Process; models decision‑making with incomplete state information.
  - term: APR
    definition: Annual Percentage Rate; the yearly interest rate charged on borrowed funds.
  - term: NLG
    definition: Natural Language Generation; converting structured data into human‑readable text summaries.
critical_citations:
  - "[Faratin et al., 1998] — Foundational negotiation decision functions for autonomous agents."
  - "[Lowe et al., 2017] — MARL framework for mixed cooperative‑competitive environments."
  - "[Sutton & Barto, 2018] — Reinforcement learning principles and algorithms."
  - "[Rahwan et al., 2019] — Machine behaviour and ethical AI frameworks."
  - "[Ghosh et al., 2022] — Synthetic data generation techniques used for training."
relevance:
  topics:
    - code: 2.C
      name: User-Declared Financial Preferences
      relevance: high
      justification: Agent models user preferences and constraints to drive negotiation strategy.
    - code: 3.C
      name: User-Defined Allocation Constraints
      relevance: medium
      justification: Uses constraints such as budget ceilings and term limits in offer generation.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews robo‑advisors and chatbots, identifying their reactive nature.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Explicitly identifies lack of strategic negotiation capability as a major gap.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Builds multidimensional user profiles including risk tolerance and goal priorities.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: high
      justification: Discusses cold‑start challenges and proposes bootstrapping or transfer learning.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: high
      justification: Uses constrained utility maximization to generate counter‑offers.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: medium
      justification: Avoids proposing infeasible offers by integrating eligibility constraints.
    - code: 8.C
      name: Cold‑Start Baseline Strategies for Anomaly Detection
      relevance: medium
      justification: Cold‑start performance issues noted; suggests using similar agents for initialization.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Implements encryption, mTLS, RBAC, and GDPR‑compliant audit trails.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Emphasizes transparency, explainability (SHAP, LIME, NLG summaries), and user control.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Defines comprehensive metrics: win‑rate, utility gain, regret, fairness index.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Benchmarks MARL agent against advisor‑assisted and user‑driven baselines.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: Negotiates loan interest rates, credit card fees, and insurance premiums to reduce debt burden.
  contribution: "This work provides a blueprint for an autonomous negotiation agent that can be integrated into Odin's recommendation module, using user preference modeling (5.A) to tailor offers. Its constrained optimization approach (7.C) directly informs budget allocation under user-defined limits. The cold‑start handling strategies (5.B, 8.C) are applicable to new users with limited history. The emphasis on explainability and user control (10.B) aligns with Odin's trust requirements. Finally, the evaluation framework (12.A, 12.B) offers a template for assessing Odin's algorithmic components."
  directly_justifies:
    - "Autonomous agents can achieve 92% agreement rates and 42% higher utility than static advisors."
    - "Multi‑agent reinforcement learning enables dynamic adaptation to institutional counter‑offers."
    - "Explainability techniques such as SHAP and NLG summaries are essential for user trust and regulatory compliance."
    - "Cold‑start performance can be mitigated by transfer learning from similar agent profiles."
  limits:
    - "Results are based on synthetic data; real‑world validation is pending."
    - "Deep reinforcement learning models trade off explainability for performance, raising transparency concerns."
    - "Domain‑specific hyperparameter tuning is required for each financial product type."
    - "Adversarial institutional agents can force conservative suboptimal outcomes."
    - "Legal liability for autonomous agreements remains unresolved; proposed hybrid consent model requires further testing. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains flagged as relevant include: Filipino Cultural Context (only 2.C, high, due to explicit user preference modeling), Expense Categorization (3.C, medium, for constraint handling), Existing Systems & Gaps (4.A medium, 4.B high), Behavioral Profiling (5.A high, 5.B high, 5.C not selected because no classification approach), Budget Recommendation (7.C high for constrained optimization, 7.D medium for infeasibility handling), Anomaly Detection (8.C medium for cold‑start baselines), Data Privacy & User Trust (10.A high, 10.B high), System Evaluation (12.A high, 12.B high), and Savings & Debt Management (13.B high for debt negotiation). Domains considered and rejected: Spending Forecasting (6.A, 6.B) – the paper does not address forecasting spending; Mobile‑First Design (9.A, 9.B) – no mobile‑specific discussion; User Retention & Engagement (11.A, 11.B) – no explicit engagement or retention mechanisms; and 13.A, 13.C – savings goals and surplus are not covered. Borderline cases: 2.C overlaps with 5.A in user preferences, but 2.C was retained for its focus on declared preferences; 7.C and 7.D are closely linked but separated because the paper explicitly handles infeasibility through eligibility checks. Overall, the paper offers strong algorithmic and ethical insights relevant to Odin's design, particularly in personalization, optimization, trust, and evaluation."
limitations:
  - "Synthetic data may not capture real‑world negotiation dynamics fully."
  - "Deep model explainability trade‑off may hinder regulatory acceptance in high‑stakes scenarios."
  - "Hyperparameter sensitivity across different financial products limits plug‑and‑play deployment."
  - "Adversarial institutional strategies can reduce agent effectiveness."
  - "Legal and liability frameworks for autonomous agent‑executed agreements are not yet established. [unacknowledged]"
remember_this:
  - "AI negotiator achieved 92% win rate and 42% higher user utility than static advisors."
  - "MARL with self‑play enables dynamic adaptation and improved negotiation efficiency."
  - "Explainability and user control are critical for trust and regulatory compliance."
  - "Cold‑start performance can be improved via transfer learning from similar agents."
  - "Hybrid consent model balances automation with user oversight for legal defensibility."
```
---

## Paper 9: Abdullahi et al_summarized.md

**Source File:** `Abdullahi et al_summarized.md`

```yaml
paper_id: 10.1109/ACCESS.2025.3587231
designation: international
title: A Systematic Literature Review of Concept Drift Mitigation in Time-Series Applications
authors: Abdullahi, M.; Alhussian, H.; Aziz, N.; Abdulkadir, S. J.; Baashar, Y.; Alashhab, A. A.; Afrin, A.
year: 2025
venue: IEEE Access
odin_topics:
  - 4.A
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 9.A
  - 10.A
  - 12.A
  - 12.B
tldr: A systematic review identifying SVM as the most effective learner for detecting and adapting to concept drift in time-series classification and regression tasks.
problem_and_motivation: Concept drift continuously changes data statistical properties, degrading machine learning model performance in time-series applications. Existing research focuses on classification with minimal attention to regression, and efficient identification of changes and responses in a time-series context remains challenging.
approach:
  - A systematic literature review was conducted using PRISMA 2020 guidelines.
  - The search was performed across SCOPUS, ScienceDirect, IEEE Xplore, Web of Science, MDPI, and ACM databases.
  - A total of 60 studies published between 2013 and 2024 were selected for in-depth review.
  - Data extraction and synthesis focused on algorithms, evaluation metrics, problem scopes, and drift handling techniques.
  - A comparative analysis of baseline methods and a roadmap for AI-based drift detection were presented.
findings:
  - num: Support Vector Machines demonstrated high detection accuracy and effective memory for concept drift.
  - num: 60 studies were identified and surveyed, with the highest publication count in 2022.
  - num: 60% of the selected studies focused on classification tasks, while only 6% addressed regression.
  - Accuracy was the most common evaluation metric for assessing concept drift detection models.
  - Ensemble-based methods like ENSDS, SVR, and ELM are effective for detecting concept drift in time-series data.
  - ADWIN, HDDM, and DDM are the most frequently used algorithms for handling different drift types.
  - LSTM models are widely used due to their ability to capture temporal dependencies and adapt to gradual changes.
  - The TriLS system enables lightweight model tuning by offloading computationally intensive tasks to the cloud.
key_figures_tables:
  - Figure 2: SLR mapping process illustrating the four stages of screening → flow of study selection.
  - Figure 5: Publication trend from 2013 to 2024 showing a significant increase in 2021-2022 → growing research emphasis.
  - Figure 7: Distribution of ML problem scopes, with classification dominating at 60% → research gap in regression.
  - Figure 9: Frequency of learning algorithms, with SVM, LSTM, and k-NN being most common → preferred learners.
  - Table 8: Classification of studies by drift handling technique (e.g., ADWIN, HDDM) → commonly used methods.
key_equations:
  - equation: "Accuracy = (TP+TN) / (TP+TN+FP+FN)"
    explanation: Proportion of correctly identified instances.
  - equation: "Precision = TP / (TP+FP)"
    explanation: Proportion of detected drifts that are actual drifts.
  - equation: "Recall = TP / (TP+FN)"
    explanation: Proportion of actual drifts detected by the model.
  - equation: "F1 = 2 * (Precision * Recall) / (Precision + Recall)"
    explanation: Harmonic mean of precision and recall.
  - equation: "RMSE = sqrt( (1/n) * sum((y_i_hat - y_i)^2) )"
    explanation: Square root of average squared prediction error.
definitions:
  - term: Concept Drift
    definition: Continuous changes in the statistical properties of a dataset over time, degrading ML model performance.
  - term: Incremental Drift
    definition: Minimal and continuous change in the original data distribution.
  - term: Gradual Drift
    definition: Noticeable and gradual changes in the target data distribution.
  - term: Sudden Drift
    definition: Abrupt and significant change in the original data distribution at a specific time.
  - term: Recurring Drift
    definition: A situation in which an old concept reappears after a period of absence.
  - term: ADWIN
    definition: Adaptive Windowing algorithm that dynamically adjusts window size based on data variations.
  - term: DDM
    definition: Drift Detection Method based on monitoring prediction errors.
  - term: HDDM
    definition: Hoeffding Drift Detection Method using statistical measures for drift detection.
  - term: SVM
    definition: Support Vector Machine, a supervised learning model effective for detecting shifts in data structure.
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network for capturing temporal dependencies.
  - term: PRISMA
    definition: Preferred Reporting Items for Systematic Reviews and Meta-Analyses.
critical_citations:
  - "[Bayram et al., 2022] — Surveys performance-aware drift detectors."
  - "[Gama et al., 2014] — Comprehensive survey on concept drift adaptation."
  - "[Lima et al., 2022] — Systematic literature review on regression under concept drift."
  - "[Iwashita & Papa, 2019] — Overview of concept drift learning."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Reviews the broader landscape of ML systems affected by drift.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly addresses predictive modeling and performance degradation due to drift.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Reviews forecasting algorithms like LSTM and SVM for time-series data.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Discusses anomaly detection in the context of drift in time-series data.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Reviews algorithms like autoencoders for drift detection in multivariate streaming data.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Mentions edge computing and lightweight models like TML for on-device adaptation.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Discusses IoT and smart city applications, touching on data handling but not explicitly privacy.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a comprehensive evaluation framework with metrics for drift detection.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Compares algorithms like SVM and LSTM for predictive performance under drift.
  contribution: This systematic review provides a consolidated evaluation of algorithms for detecting concept drift, which is critical for maintaining the accuracy of predictive models like Odin's spending forecasts. Its identification of SVM and LSTM as effective learners informs the selection of core algorithms for Odin's forecasting and anomaly detection modules. The detailed mapping of evaluation metrics and experimental procedures offers a blueprint for rigorously testing Odin's machine learning components. The review's discussion of computational efficiency and edge-cloud architectures provides guidance for deploying Odin's algorithm modules in a mobile-first context.
  directly_justifies:
    - "SVM is the most effective learning algorithm for detecting concept drift in time-series data."
    - "LSTM models are effective in capturing temporal dependencies and adapting to gradual changes."
    - "ADWIN, HDDM, and DDM are the most frequently used algorithms for handling different drift types."
    - "Accuracy is the most common evaluation metric for assessing concept drift detection models."
  limits:
    - "The review focuses on classification and regression, potentially overlooking other learning paradigms like reinforcement learning."
    - "Most studies were evaluated on synthetic or limited real-world datasets, which may not reflect the complexity of personal finance data."
    - "The review does not provide an empirical benchmark or comparative analysis of the identified methods, relying instead on a synthesis of existing literature."
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The paper was flagged as highly relevant to Predictive Modeling (6.A, 6.B) because it directly addresses performance degradation in time-series forecasting, a core function of Odin. It is also highly relevant to System Evaluation (12.A, 12.B) for its detailed framework of evaluation metrics and algorithm comparison. Medium relevance was assigned to Anomaly Detection (8.A, 8.B) due to its focus on detecting changes in data distributions, and Mobile-First Design (9.A) for its discussion of edge computing and lightweight models. Contextual relevance was assigned to Landscape of Existing Systems (4.A) and Data Privacy (10.A) as the paper does not specifically address financial systems or privacy. While the paper touches on algorithm selection (12.B), its primary contribution is a synthesis of methods for drift handling, making it a foundational reference for Odin's algorithm evaluation and selection process.
limitations:
  - "The study analyzed only 60 research articles from a specific set of databases, potentially missing relevant studies."
  - "The search was limited to papers published in English between 2013 and 2024."
  - "Most of the currently proposed drift detection methods have not been fully solved, and reliance on simulation datasets may not capture real-world scenarios."
  - "Several studies tested their proposed methods using a single dataset, which may limit generalizability."
  - "Comparisons with state-of-the-art studies are limited."
  - "The study did not investigate similarity and dissimilarity-based methods for concept drift detection."
  - "The SLR focuses on algorithm review without a new empirical benchmark, limiting actionable design guidance without further testing on financial data. [unacknowledged]"
remember_this:
  - "Concept drift continuously degrades model performance in time-series forecasting."
  - "SVM is identified as the most effective learner for drift detection and adaptation."
  - "The number of concept drift publications has significantly increased, with 60 studies reviewed."
  - "Only 6% of reviewed studies focused on regression tasks, highlighting a gap."
  - "Accuracy was the most common metric for evaluating concept drift detection models."
```
---

## Paper 10: Du Y. et al_summarized.md

**Source File:** `Du Y. et al_summarized.md`

```yaml
paper_id: 10.1145/3746252.3761080
designation: international-algorithm-specific
title: "PAnDA: Combating Negative Augmentation via Large Language Models for User Cold-Start Recommendations"
authors: "Du, Y.; Chen, R.; Zhao, X.; Han, Q.; Qin, A. K."
year: 2025
venue: "Proceedings of the 34th ACM International Conference on Information and Knowledge Management (CIKM '25)"
odin_topics:
  - "5.A"
  - "5.B"
  - "5.C"
  - "6.B"
  - "8.A"
  - "8.B"
  - "12.B"
tldr: "PAnDA combats negative augmentation in cold-start recommendation using LLMs through preference-aligned augmentation and downstream-model-aware adaptation."
problem_and_motivation: "Existing LLM-based data augmentation for cold-start recommendation suffers from negative augmentation, characterized by incomplete augmentation that fails to capture user preferences and inaccurate augmentation that conflicts with user intent. These issues stem from the inability to effectively incorporate collaborative signals and the lack of awareness of downstream model learning dynamics."
approach:
  - "Proposes PAnDA, a preference-aligned and downstream-model-aware data augmentation framework."
  - "Uses a model-agnostic preference-aligned augmentation module with user-user preference matching and user-item preference coherence to guide an LLM augmentor."
  - "Employs a Meta-Masked Autoencoder (MetaMAE) to integrate collaborative signals and textual information for comprehensive user/item representations."
  - "Introduces a model-specific downstream-model-aware adaptation module that filters augmented samples based on gradient similarity with original user interactions."
  - "Evaluates on three real-world benchmark datasets (ML-1M, Netflix, Book-Crossing) against state-of-the-art cold-start and augmentation-based methods."
findings:
  - "num: PAnDA outperforms the best baseline LLMRec by 15.37% in Recall@10 and 16.47% in NDCG@10 on ML-1M."
  - "num: On the sparse Book-Crossing dataset, PAnDA achieves a 37.55% improvement in Recall@10 over the best baseline."
  - "num: PAnDA consistently shows significant improvements (p < 0.05) across all datasets and metrics."
  - "LLM-based augmentation (LLMRec) is the second-best performing method, highlighting the value of textual signals."
  - "The ablation study confirms the importance of TIA, CSA, and the downstream-model-aware filtering strategy for optimal performance."
key_figures_tables:
  - "Figure 1: Illustration of data augmentation methods → Shows PAnDA's approach to achieving complete and accurate augmentation."
  - "Table 1: Statistics of experimental datasets → Provides sparsity and interaction details for ML-1M, Netflix, and Book-Crossing."
  - "Table 2: Overall performance comparison → Demonstrates PAnDA's consistent superiority over all baseline groups."
  - "Table 3: Ablation study results → Validates the individual contribution of TIA, CSA, and DFS modules."
  - "Figure 4: Performance with varying augmented pairs → Shows optimal augmentation quantity varies with dataset sparsity."
key_equations:
  - equation: "L_{r e c}(u, j+, j-) = -log(sigma(y_hat_{u,j+} - y_hat_{u,j-}))"
    explanation: "BPR loss for training the downstream recommender."
  - equation: "sim({j+, j-}, V_u) = < nabla_theta L_rec(u, j+, j-), nabla_theta L(V_u) >"
    explanation: "Cosine similarity of gradients to filter mismatched samples."
  - equation: "z_u = (1 - alpha) h_u + alpha e_u"
    explanation: "Fuses profile-based and collaborative user representations."
  - equation: "theta_{AE}^{u, *} approx theta_AE - eta_1 nabla_{theta_AE} L_{fr}(u)"
    explanation: "One-step gradient descent for personalized autoencoder parameters."
definitions:
  - term: "Negative Augmentation"
    definition: "Generated interactions that fail to reflect user preferences or conflict with user intent, degrading model performance."
  - term: "Incomplete Augmentation"
    definition: "Augmented data that does not comprehensively capture user preferences, often due to missing multi-modal signals."
  - term: "Inaccurate Augmentation"
    definition: "Augmented data that conflicts with user intent, misleading the downstream recommendation model."
  - term: "MetaMAE"
    definition: "Meta-Masked Autoencoder used to integrate collaborative and textual signals for user/item representation learning."
  - term: "TIA"
    definition: "Textual Information Augmentation, using LLMs to generate user-item interactions from text."
critical_citations:
  - "[Kang et al., 2023] — Foundational for evaluating LLMs on user preference tasks."
  - "[Wei et al., 2024] — Proposes LLMRec, a key LLM-based augmentation baseline."
  - "[Wu & Zhou, 2023] — Introduces M2EU, a state-of-the-art meta-learning cold-start method."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "contextual"
      justification: "Provides a general framework for preference modeling."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "high"
      justification: "Directly addresses the user cold-start problem in a recommendation context."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "Uses classification-like approach to generate and filter preference-aligned augmentations."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "medium"
      justification: "The data augmentation and adaptation methods are analogous to improving forecasting by enriching sequential data."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "The downstream-model-aware filtering helps identify and remove 'anomalous' or mismatched augmentations."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "low"
      justification: "Gradient similarity filtering is a technique that could be adapted for anomaly detection."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "The paper presents a thorough evaluation of the algorithmic augmentation and filtering modules."
  contribution: "PAnDA can inform Odin's cold-start module for new users by generating synthetic spending data. Its adaptation mechanism is directly relevant for Odin's anomaly detection system, ensuring only relevant patterns are learned. The framework's evaluation methodology provides a template for testing Odin's recommendation and forecasting algorithms. Furthermore, its approach to integrating textual and collaborative signals can enhance Odin's expense categorization and user profiling capabilities."
  directly_justifies:
    - "Generating augmented data for cold-start users is essential for robust recommendation performance."
    - "Adaptively filtering augmented data based on model state prevents performance degradation from noisy samples."
    - "Integrating textual information with collaborative signals produces more comprehensive user representations."
    - "A meta-learning framework can personalize model parameters for each user in sparse-data scenarios."
  limits:
    - "The evaluation is not conducted on financial transaction data, limiting direct applicability to PFMS."
    - "The study does not explore the computational cost or latency of the bi-level optimization in a real-time setting."
    - "The effectiveness depends on the quality of the base recommender used to generate candidate item sets."
  mapping_rationale: "A systematic scan was conducted across all 12 functional domains and their associated topic codes. The paper was flagged as highly relevant to 'Behavioral Profiling & Classification' (5.B, 5.C) and 'System Evaluation' (12.B) due to its focus on the user cold-start problem and rigorous algorithmic evaluation. Medium relevance was assigned to 'Spending Forecasting' (6.B) as the data augmentation method is a precursor to forecasting, and to 'Anomaly Detection' (8.A, 8.B) because the downstream-model-aware filtering is a form of anomaly rejection. Low or contextual relevance was noted for domains like 'Filipino Cultural Context' (2.A-D) and 'Expense Categorization' (3.A-C), as the paper does not address these specific financial domains. The 'Existing Systems & Gaps' domain (4.A-B) was considered but rejected as the paper focuses on a new algorithmic solution rather than a survey. Overall, the paper's core contribution is algorithmic and methodological, making it most relevant to Odin's backend modules for cold-start handling and model evaluation."
limitations:
  - "The quality of augmented samples depends heavily on the performance of the base recommender used for candidate item selection. [unacknowledged]"
  - "The gradient similarity filter adds computational overhead that may not be feasible for all system architectures."
  - "The approach was validated on movie and book datasets, not on the specific context of personal financial transactions."
remember_this:
  - "LLM-generated data augmentation can harm model performance if not properly aligned."
  - "A gradient-based filter effectively removes mismatched augmented data samples."
  - "Combining textual and collaborative signals provides a 15-37% performance gain in cold-start tasks."
  - "Meta-learning personalizes the autoencoder to capture unique user preferences."
  - "PAnDA provides a framework for adaptive, high-quality synthetic data generation."
```
---

## Paper 11: Parameswaran & Saad_summarized.md

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

## Paper 12: Ramagiri_summarized.md

**Source File:** `Ramagiri_summarized.md`

```yaml
paper_id: 10.5281/zenodo.16883459
designation: international
title: "Tuning AML Detection Rules: A Quantitative Approach to Reducing False Positives"
authors: "Ramagiri, V."
year: 2025
venue: "Sarcouncil Journal of Engineering and Computer Sciences"
odin_topics:
  - 4.A
  - 4.B
  - 8.A
  - 8.B
  - 11.A
  - 11.B
tldr: "A data-driven framework optimizes AML detection rules using statistical calibration, customer segmentation, and predictive modeling to reduce false positive alerts while maintaining risk coverage."
problem_and_motivation: "Financial institutions face overwhelming false positive alerts that consume compliance resources and mask genuine financial crime risks. Existing rules-based systems employ fixed parameters that fail to adapt to changing customer behaviors. A quantitative, data-driven approach is needed to transform monitoring sensitivity and align it with actual risk profiles."
approach:
  - "Applies statistical threshold calibration using kernel density estimation, extreme value theory, and time-series decomposition to improve anomaly detection."
  - "Implements customer segmentation via multivariate clustering (k-means, hierarchical, Gaussian mixture) to enable targeted rule parameterization."
  - "Develops predictive models using random forests, gradient boosting, and deep neural networks to estimate suspicious activity probability."
  - "Uses alert disposition analysis and conversion metrics to assess rule effectiveness and identify improvement opportunities."
  - "Employs backtesting methodologies including historical replay and simulation to validate rule changes before production deployment."
  - "Establishes performance measurement frameworks with survival analysis and risk-based evaluation weights for multidimensional assessment."
  - "Proposes phased implementation strategies starting with lower-risk segments to minimize operational disruption."
  - "Designs cross-functional governance structures with compliance, operations, and technology stakeholders to oversee optimization."
findings:
  - "num: High false positive rates are reported across the financial services industry, creating significant operational burdens."
  - "num: Alert backlogs develop when monitoring systems generate volumes exceeding investigative capacity."
  - "num: Advanced segmentation reveals natural customer groupings not aligned with traditional classifications."
  - "Machine learning models demonstrate superior discrimination capabilities compared to traditional rules-based methods."
  - "Unsupervised anomaly detection identifies novel typologies not captured by existing rules."
  - "Explainable AI techniques address regulatory concerns regarding model interpretability and audibility."
  - "Phased deployment strategies result in higher stakeholder confidence and fewer operational disruptions."
  - "Documentation quality is a primary determinant of both governance effectiveness and regulatory acceptance."
key_figures_tables:
  - "Figure 1: AML False Positive Challenge → Illustrates the operational burden of excessive false positive alerts on compliance teams."
  - "Figure 2: False Positive Challenges in Modern AML Programs → Depicts the multifaceted impact across financial institutions."
  - "Figure 3: Quantitative Methodologies → Shows statistical, segmentation, and machine learning techniques for rule optimization."
  - "Figure 4: Implementation Strategies → Outlines regulatory engagement, documentation, phased deployment, and governance approaches."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "AML"
    definition: "Anti-Money Laundering"
  - term: "SAR"
    definition: "Suspicious Activity Report"
critical_citations:
  - "[Aidoo, 2025] — Evaluates effectiveness of AML regulations and false positive challenge."
  - "[Ketenci, et al., 2021] — Provides time-frequency suspicious activity detection for AML."
  - "[Jensen & Iosifidis, 2023] — Surveys statistics and machine learning for AML monitoring."
  - "[Kuzmenko, et al., 2023] — Applies survival analysis to AML system effectiveness assessment."
  - "[Moromoke, et al., 2024] — Discusses regulatory challenges and operational impacts of false positives."
relevance:
  topics:
    - code: 4.A
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Describes legacy rules-based monitoring systems and their limitations."
    - code: 4.B
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Documents false positive burdens, rigid parameters, and adaptability gaps."
    - code: 8.A
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Directly addresses optimization of detection rules to reduce false positives."
    - code: 8.B
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Reviews statistical and machine learning methods for anomaly detection."
    - code: 11.A
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "contextual"
      justification: "Alert fatigue and high false positives undermine user engagement and trust."
    - code: 11.B
      name: "Retention Mechanisms and Engagement Design"
      relevance: "low"
      justification: "Mentions efficiency improvements but does not directly discuss retention design."
  contribution: "The framework provides a quantitative methodology for tuning detection rules that Odin can adopt for its anomaly detection module. The customer segmentation techniques enable Odin to personalize spending anomaly baselines. The backtesting and phased deployment strategies inform Odin's evaluation and rollout of algorithmic changes. The performance measurement framework, including risk-based weighting, supports Odin's system evaluation and continuous improvement. The principles of reducing false positives are directly applicable to Odin's goal of maintaining user trust through accurate alerts."
  directly_justifies:
    - "Quantitative threshold calibration improves anomaly detection precision compared to arbitrary settings."
    - "Customer segmentation enables personalized rule tuning based on observed spending behavior."
    - "Predictive modeling can estimate the probability of suspicious or anomalous transactions."
    - "Phased implementation with validation controls minimizes disruption during system changes."
    - "Performance measurement must balance efficiency (alert reduction) with risk coverage."
  limits:
    - "The paper focuses on AML compliance in banking, which has different risk thresholds than personal finance."
    - "The proposed machine learning models require labeled alert data, which may not exist for personal spending anomalies."
    - "Regulatory engagement strategies are specific to financial crime compliance, not personal finance apps."
    - "The framework does not address user privacy concerns specific to personal financial data. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper directly supports 'Existing Systems & Gaps' (4.A, 4.B) by describing limitations of rules-based monitoring and the operational burden of false positives. It has high relevance to 'Anomaly Detection' (8.A, 8.B) through its focus on optimizing detection rules and applying quantitative methods to reduce false alerts. The discussion of alert fatigue and compliance resource allocation touches on 'User Retention & Engagement' (11.A) contextually, as excessive false positives undermine user trust and engagement, though it is not directly studied. Domains like 'Filipino Cultural Context' (2.A-D), 'Expense Categorization' (3.A-C), 'Behavioral Profiling' (5.A-C), 'Spending Forecasting' (6.A-B), 'Budget Recommendation' (7.A-D), and 'Mobile-First Design' (9.A-B) were considered but rejected as the paper does not address personal spending, cultural factors, or mobile UX. 'Data Privacy' (10.A-B) and 'Savings & Debt' (13.A-C) are also not covered. The paper offers a high-level framework for reducing false positives that can inform Odin's anomaly detection approach but is not directly applicable to the Filipino context or PFMS specifics."
limitations:
  - "Focuses on AML compliance for financial institutions, not personal finance management. [unacknowledged]"
  - "Assumes access to labeled historical alert data for supervised learning, often unavailable in PFMS. [unacknowledged]"
  - "Lacks empirical validation of the proposed framework in a real-world setting. [unacknowledged]"
  - "Does not address user privacy or data security implications of profiling and anomaly detection."
  - "Regulatory engagement strategies are specific to financial crime, not applicable to consumer apps."
remember_this:
  - "False positive alerts consume substantial compliance resources and mask genuine risks."
  - "Quantitative methods outperform experience-based threshold tuning for anomaly detection."
  - "Customer segmentation enables personalized and more accurate detection rule calibration."
  - "Backtesting and phased deployment are essential for validating rule changes safely."
  - "Performance measurement must balance alert reduction with maintaining risk coverage."
```
---

## Paper 13: Pandiin & Matias_summarized.md

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

## Paper 14: Li & Li_summarized.md

**Source File:** `Li & Li_summarized.md`

```yaml
paper_id: 10.1109/ACCESS.2025.3622358
designation: international-algorithm-specific
title: Exploring Factors Involved in Loan Approval Decision: Deep Insights and Data Analytics Techniques
authors: Li, X.; Li, J.
year: 2025
venue: IEEE Access
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 10.A
  - 12.A
tldr: An end-to-end pipeline for credit default prediction using consensus feature selection, a lightweight 1D-CNN, and SHAP explanations achieves high accuracy and operational efficiency for transparent, real-time lending decisions.
problem_and_motivation: Traditional credit scoring models struggle with non-linear interactions and high-dimensional data, while deep learning models face barriers of explainability and regulatory compliance. A framework is needed that balances predictive accuracy with transparency and operational efficiency for real-world deployment.
approach:
  - A three-way consensus feature selection ensemble is used, combining VarianceThreshold, Recursive Feature Elimination with logistic regression, and XGBoost gain ranking.
  - A lightweight one-dimensional convolutional neural network is designed for tabular data, optimizing for low-latency inference on standard CPUs.
  - Post-hoc explainability via KernelSHAP is embedded directly in the inference loop to provide global and local decision justifications.
  - The pipeline integrates continuous system-level profiling of CPU, RAM, GPU, and latency to quantify deployment feasibility.
  - The model is trained and evaluated on the GiveMeSomeCredit dataset, using a stratified 20% hold-out for validation and class weighting to handle imbalance.
findings:
  - num: The proposed method achieved a ROC-AUC of 0.862 and an F1-score of 0.55 on the validation set.
  - num: The model outperformed logistic regression and XGBoost baselines by 9% and 4% ROC-AUC, respectively.
  - num: Consensus feature selection contributed 57% of the total accuracy gain, while the 1D-CNN architecture contributed 38%.
  - num: Fairness assessment showed disparate-impact and equal-opportunity gaps below 5% across gender and age cohorts.
  - num: End-to-end inference averaged 18 milliseconds on CPU-only hardware, confirming real-time viability.
  - The consensus feature selection reduced the original feature space to a stable subset of five predictors.
  - The model demonstrated strong calibration with a ROC-AUC of 0.83 in extended validation.
key_figures_tables:
  - Figure 15: Comparison of imbalance handling techniques → Class weighting provided the most balanced F1-score.
  - Figure 20: Receiver operating characteristic curve → ROC-AUC of 0.83 reflects strong class separability.
  - Figure 26: SHAP summary plot → Age is the most influential feature in predicting default.
  - Table 3: Extended validation results → Consistent performance with ROC-AUC above 0.85 on a held-out subset.
key_equations:
  - equation: "Precision = TP / (TP + FP)"
    explanation: Measures proportion of true positives among positive predictions.
  - equation: "Recall = TP / (TP + FN)"
    explanation: Measures proportion of actual positives correctly identified.
  - equation: "F1-Score = 2 * (Precision * Recall) / (Precision + Recall)"
    explanation: Harmonic mean of precision and recall.
definitions:
  - term: ROC-AUC
    definition: Area under the receiver operating characteristic curve, measuring classifier separability.
  - term: 1D-CNN
    definition: One-dimensional convolutional neural network for processing sequential or ordered data.
  - term: SHAP
    definition: SHapley Additive exPlanations, a method for interpreting model predictions.
  - term: RFE
    definition: Recursive Feature Elimination, a feature selection method that recursively removes features.
  - term: XGBoost
    definition: Extreme Gradient Boosting, a scalable tree boosting system.
critical_citations:
  - "[Lundberg and Lee, 2017] — Foundation for SHAP-based model interpretability."
  - "[Chen and Guestrin, 2016] — Basis for XGBoost feature importance and baseline."
  - "[Guyon and Elisseeff, 2003] — Foundational work on feature selection strategies."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Paper proposes a complete predictive pipeline for default risk, directly applicable to spending forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Uses a 1D-CNN model optimized for tabular data, a technique applicable to sequential spending data.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Default prediction is a form of anomaly detection for loan repayment behavior.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: The 1D-CNN and ensemble feature selection are directly applicable to detecting anomalies in spending.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Mentions regulatory compliance (EU AI Act) as a motivator for transparent models.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides a comprehensive evaluation framework including ROC-AUC, F1, fairness, and calibration metrics.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Includes ablation studies to isolate contribution of feature selection and model architecture.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: CPU-only inference and profiling are relevant for mobile deployment.
  contribution: This paper provides a blueprint for building a transparent and efficient predictive system for financial risk, which is directly applicable to Odin's spending forecasting and anomaly detection modules. Its emphasis on explainability through SHAP directly supports Odin's need for user trust and regulatory compliance. The system-level profiling methodology offers a practical approach for validating deployment feasibility on mobile devices. The consensus feature selection technique provides a robust method for handling high-dimensional financial data, which is relevant for Odin's expense categorization. The paper's fairness assessment aligns with Odin's broader goals for equitable financial management.
  directly_justifies:
    - Odin's anomaly detection module can use 1D-CNNs to identify unusual spending patterns in real-time.
    - Odin can adopt consensus feature selection to reduce input dimensionality for its forecasting models.
    - Odin can integrate SHAP explanations to provide users with transparent justifications for budget recommendations.
    - Odin can use the profiling framework to ensure its predictive models are efficient for mobile deployment.
  limits:
    - The study is validated on a single public dataset, which may limit generalizability.
    - Fairness analysis was limited to gender and age cohorts, not covering other protected attributes.
    - Online drift handling and dynamic threshold calibration were not explored.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper's primary contribution is algorithmic and predictive, leading to high relevance for domains like Spending Forecasting (6.A, 6.B) and Anomaly Detection (8.A, 8.B). The paper's focus on system profiling and deployment also aligns with Mobile-First Design (9.A) and Data Privacy (10.A), which are assigned medium and contextual relevance, respectively. The paper's emphasis on interpretability and evaluation metrics provides support for System Evaluation (12.A, 12.B), assigned medium relevance. Domains such as Behavioral Profiling (5.A, 5.B, 5.C), Budget Recommendation (7.A-D), and Savings & Debt Management (13.A-C) were considered but rejected as the paper does not address the user-specific constraints or goal management found in Odin's problem space. The overall relevance is high for Odin's predictive core, offering a proven, efficient, and transparent methodology for financial risk assessment.
limitations:
  - The model achieved only modest recall for the minority default class.
  - The model was not validated under concurrent load or stress tests. [unacknowledged]
  - The approach was not tested for online drift handling. [unacknowledged]
remember_this:
  - Feature selection ensemble contributed 57% of accuracy gain.
  - End-to-end inference averages 18 milliseconds on CPU hardware.
  - Age is the most dominant predictor in the credit risk model.
  - SHAP explanations are embedded directly in the inference loop.
  - Model achieves 0.862 ROC-AUC with only five features.
```
---

## Paper 15: Theerthala_summarized.md

**Source File:** `Theerthala_summarized.md`

```yaml
paper_id: "c3f0a1b2-4d5e-6f7a-8b9c-0d1e2f3a4b5c"
designation: "international-algorithm-specific"
title: "Synthesizing Behaviorally-Grounded Reasoning Chains: A Data-Generation Framework for Personal Finance LLMs"
authors: "Theerthala, A."
year: 2025
venue: "Proceedings of The 10th Workshop on Financial Technology and Natural Language, EMNLP-2025"
odin_topics:
  - "1.A"
  - "1.B"
  - "1.C"
  - "2.A"
  - "2.C"
  - "3.A"
  - "3.B"
  - "3.C"
  - "4.A"
  - "4.B"
  - "5.A"
  - "5.B"
  - "5.C"
  - "6.A"
  - "6.B"
  - "7.A"
  - "7.B"
  - "7.C"
  - "7.D"
  - "8.A"
  - "8.B"
  - "8.C"
  - "10.A"
  - "10.B"
  - "11.A"
  - "11.B"
  - "12.A"
  - "12.B"
  - "12.C"
tldr: "A data-centric framework integrates behavioral finance cues into reasoning chains to fine-tune an 8B model, achieving performance comparable to 27-32B models at 80% lower cost for personal financial advice."
problem_and_motivation: "Current LLM-based financial advisors are often impractical due to high costs and reliance on complex agentic architectures that do not explicitly address user behavioral biases. A significant gap exists in creating smaller, trustworthy models that inherently integrate financial and psychological knowledge through high-quality supervision data, rather than relying on expensive live data or complex multi-agent systems."
approach:
  - "Collected 405k real-world personal finance questions from Reddit (pre-June 2023) and sampled 19k representative queries across eight thematic categories."
  - "Developed a four-phase chain-of-thought generation framework: Query Analysis, Context Analysis (modular RAG with financial and behavioral corpora), Psychological Cue Identification, and Response Rubric formulation."
  - "Used a modular RAG system to retrieve and condense context from a ~600k token financial corpus and a ~300k token behavioral corpus, employing text-embeddings-3-large and a cross-encoder for retrieval."
  - "Employed LLM-based juries (gemini-2.0-flash and o4-mini) within a three-shot evaluation framework to validate and rank generations at each phase."
  - "Fine-tuned a Qwen-3-8B model on the generated 19k sample dataset and evaluated its performance against larger baselines (14B to 32B parameters) on held-out test sets and through a blind LLM-jury study."
findings:
  - "num: The fine-tuned 8B model achieved semantic accuracy comparable to leading baselines, surpassing Gemma3-27B by 5% on BLEURT and showing only a 2% difference on BERTScore."
  - "num: The 8B model incurred 80% lower operational costs than models over 12B parameters, with a hosting cost of $0.8 per hour and an average inference time of 34.15 seconds."
  - "num: In a blind LLM-jury ranking on 504 unseen queries, the 8B system outperformed all other sub-14B models and approached the performance of 27-32B leaders."
  - "Qualitative analysis revealed the model's strength in providing well-structured, empathetic responses, but identified factual hallucination as a key weakness, particularly for jurisdiction-specific regulations."
  - "The study demonstrates that a well-curated, behavior-tuned finance dataset can elevate a mid-sized open model to achieve performance parity with models two to three times its size."
key_figures_tables: []
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "RAG"
    definition: "Retrieval-Augmented Generation, a framework that retrieves relevant information from a corpus to ground the response generation."
  - term: "CoT"
    definition: "Chain-of-Thought, a prompting technique that encourages the model to generate intermediate reasoning steps."
  - term: "PFMS"
    definition: "Personal Finance Management System, an application designed to help individuals manage their finances."
  - term: "LLM"
    definition: "Large Language Model, a type of artificial intelligence model trained on a massive dataset of text and code."
  - term: "API"
    definition: "Application Programming Interface, a set of rules and specifications for software programs to communicate with each other."
critical_citations:
  - "[Zhou et al., 2025] — Shows LLMs exhibit significant financial biases, which can be exacerbated by fine-tuning."
  - "[Takayanagi et al., 2025a] — Finds that users' trust is heavily influenced by advisor persona, not just advice accuracy."
  - "[Winder et al., 2024] — Reveals that LLM-generated advice can systematically increase portfolio risk by reinforcing investment biases."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "contextual"
      justification: "Paper focuses on general personal finance users, not specifically Filipino YPs, but provides a framework applicable to them."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "contextual"
      justification: "The financial structure is general and not specific to the Philippines, but the paper's methodology is transferable."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "contextual"
      justification: "The paper addresses general financial behavior, providing a framework for understanding user actions, which is relevant to Filipino YPs."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "low"
      justification: "The paper does not focus on culturally specific practices, but its methodology for integrating behavioral cues is relevant."
    - code: "2.C"
      name: "User-Declared Financial Preferences"
      relevance: "high"
      justification: "The framework is designed to tailor advice to user queries and constraints, directly addressing user-declared preferences."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "medium"
      justification: "The dataset includes categories like Budgeting & Cash-Flow Management, which implicitly involves expense categorization."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      relevance: "medium"
      justification: "The framework's design choices for dataset categories can inform how to design expense categories in a PFMS."
    - code: "3.C"
      name: "User-Defined Allocation Constraints"
      relevance: "high"
      justification: "The paper's final response formulation incorporates user-specific details (monetary amounts, timelines, constraints), directly aligning with user-defined allocation."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "The paper provides a landscape review of existing LLM-based and agentic systems, identifying their limitations and gaps."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "The paper explicitly identifies and addresses limitations of prior systems, such as high cost, lack of behavioral integration, and poor performance in deployment."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "A core contribution is integrating behavioral finance studies (biases, psychological cues) into the reasoning chain to construct supervision data."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "medium"
      justification: "The paper's behavioral analysis module identifies user state and cues, which is foundational for handling cold-start profile scenarios."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "The paper uses a psychological cue identification module that classifies user sentiment, emotion, and intent, informing profile classification."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "low"
      justification: "While not a forecasting paper, the framework can be used to generate data for downstream predictive tasks."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "low"
      justification: "This paper does not focus on forecasting algorithms, but its data-generation methodology could support training forecasting models."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "high"
      justification: "The framework creates supervision data for advice that includes specific budgeting and allocation recommendations."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "high"
      justification: "The paper's output is a framework for generating personalized financial advice, which directly includes budget recommendation."
    - code: "7.C"
      name: "Constrained Optimization Approaches for Budget Allocation"
      relevance: "medium"
      justification: "The advice generated respects user constraints (monetary amounts, timelines), aligning with the principles of constrained optimization."
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "medium"
      justification: "The framework is designed to provide actionable advice, implicitly handling infeasibility by generating practical, step-by-step plans."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "low"
      justification: "Not a direct focus, but the paper's emphasis on behavioral cues could inform anomaly detection by flagging unusual user states or requests."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "low"
      justification: "The paper does not discuss specific algorithms for anomaly detection in spending data."
    - code: "8.C"
      name: "Cold-Start Baseline Strategies for Anomaly Detection"
      relevance: "contextual"
      justification: "The psychological cue identification module can provide contextual signals helpful for establishing a baseline in the absence of user history."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "The study incorporates explicit privacy safeguards, including de-identification of Reddit data and release under Apache 2.0."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "high"
      justification: "The paper is explicitly motivated by findings that user trust is influenced by advisor persona, and it aims to build trust by generating empathetic and personalized advice."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "medium"
      justification: "The qualitative analysis shows the model generates user-responsive framing, which is key for user engagement."
    - code: "11.B"
      name: "Retention Mechanisms and Engagement Design"
      relevance: "medium"
      justification: "The framework's focus on personalization and empathetic framing are design choices that can improve user retention."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "The paper presents a comprehensive evaluation framework using both quantitative (BERTScore, BLEURT) and qualitative (LLM-as-a-judge) metrics."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "The paper evaluates the performance of the fine-tuned Qwen-3-8B model against multiple baselines, providing a clear methodology for module evaluation."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "medium"
      justification: "The LLM-jury study methodology is a valid evaluation approach for recommendation systems."
  contribution: "The paper provides a reproducible framework for generating high-quality financial reasoning data that integrates behavioral psychology. This directly supports Odin's personalization module by offering a method to create training data that accounts for user sentiment and cognitive biases. The cost analysis demonstrates a viable path to deploying efficient, trustworthy models, which is critical for Odin's goal of being a practical PFMS. The structured chain-of-thought methodology can inform how Odin designs its own reasoning and response generation pipelines. The explicit focus on user trust and empathy directly justifies design choices in Odin's conversational interface."
  directly_justifies:
    - "Integrating behavioral cues into training data is essential for building trustworthy financial advisors."
    - "A data-centric approach can produce smaller, more efficient models without sacrificing performance."
    - "Empathetic and personalized framing is key to user engagement and trust in financial advice systems."
    - "Factual grounding and verification are critical to mitigate hallucinations in regulation-heavy financial domains."
  limits:
    - "The dataset and model are primarily U.S.-centric, limiting generalizability to other jurisdictions like the Philippines."
    - "The psychological analysis is rudimentary, relying on simple sentiment cues rather than validated instruments."
    - "The framework's scope excludes multi-modal data and complex reasoning tasks, which are important for a comprehensive PFMS."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was conducted. The paper was found to be highly relevant to domains including Behavioral Profiling (5.A, 5.B, 5.C), Budget Recommendation (7.A, 7.B, 7.C, 7.D), Data Privacy (10.A), User Trust (10.B), and System Evaluation (12.A, 12.B, 12.C), due to its core contribution of a data-centric framework for integrating behavioral finance into LLM training for personalized advice. Medium relevance was assigned to domains like Expense Categorization (3.A, 3.B) and Existing Systems (4.A, 4.B) as it provides a landscape review and informs design choices. Low relevance was assigned to forecasting domains (6.A, 6.B) and anomaly detection (8.A, 8.B) as these are not the paper's focus, but the methodology could support them. Topics related specifically to the Filipino context (1.A, 1.B, 1.C, 2.A) were marked as contextual, as the paper provides a transferable framework but does not use Filipino data. Overall, the paper directly justifies a data-centric, behaviorally-aware approach for building effective and trustworthy personal finance systems, which is highly applicable to Odin's design."
limitations:
  - "The study uses only Reddit data, which may not represent all demographics or query formats. [unacknowledged]"
  - "The 19k dataset is insufficient to cover the full spectrum of real-world personal finance scenarios. [unacknowledged]"
  - "Psychological analysis is rudimentary, deriving only basic sentiment from phrases. [unacknowledged]"
  - "The framework excludes multi-modal data processing and advanced reasoning capabilities. [unacknowledged]"
  - "Geographic scope and privacy safeguards remain limitations for global deployment. [acknowledged]"
remember_this:
  - "Fine-tuned 8B model matched performance of 27-32B models on held-out tests."
  - "Achieved 80% lower operational costs than larger baselines."
  - "Integrating behavioral cues into training data improves model trustworthiness."
  - "Factual hallucination remains a key bottleneck for regulatory advice."
  - "Data-centric approach offers a cost-effective alternative to agentic systems."
```
---

## Paper 16: Onsay & Rabajante-2025_summarized.md

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

## Paper 17: Bachmann et al_summarized.md

**Source File:** `Bachmann et al_summarized.md`

```yaml
paper_id: "10.1371/journal.pone.0322690"
designation: "international-algorithm-specific"
title: "Adaptive political surveys and GPT-4: Tackling the cold start problem with simulated user interactions"
authors: "Bachmann, F.; Weijden, D. v. d.; Heitz, L.; Sarasua, C.; Bernstein, A."
year: 2025
venue: "PLOS ONE"
odin_topics:
  - "5.B"
  - "8.C"
  - "6.A"
  - "12.A"
  - "12.B"
  - "5.C"
tldr: "Uses GPT-4 to generate synthetic user interactions that pre-train adaptive questionnaire models, demonstrating significant early-stage error reduction and improved candidate recommendation accuracy."
problem_and_motivation: "Adaptive questionnaires require training data for effective question selection, which is often unavailable initially. This dependency creates a cold start problem that limits their widespread adoption. Prior solutions using heuristics or online learning yield unsatisfactory early performance."
approach:
  - "Generated synthetic training data by prompting GPT-4 to answer 75 political questions from the perspective of eight Swiss parties, repeated 50 times per party."
  - "Varied GPT-4 temperature from 1 to 2 to increase response variance and created interpolated datasets (GPTvoters) to mimic voter distributions using Dirichlet sampling."
  - "Simulated an adaptive questionnaire with a PCA and Logistic Regression statistical model, using uncertainty sampling (Gini impurity) for question selection."
  - "Evaluated model performance on two downstream tasks: missing value imputation (RMSE) and candidate recommendation accuracy (CRA) in a Voting Advice Application."
  - "Compared pre-trained models (with synthetic data) against random initialisation (cold start) and an oracle benchmark, with continuous model updates after every 5 users."
findings:
  - "GPT-4 generated answers closer to party-means than real candidates for most parties (p < 0.001), with an average distance of d̄_G = 0.165 vs. d̄_C = 0.186."
  - "num: Pre-training with the GPTvoters dataset reduced initial RMSE from 0.420 (cold start) to 0.315, and improved initial CRA from 24.8% to 43.2%."
  - "The break-even point for the GPTvoters model occurred after 175 users for RMSE and after 485 users for CRA (K=30)."
  - "num: For missing value imputation, the break-even point followed N * K = 4,500 user interactions, independent of K."
  - "Synthetic data introduced a bias towards moderate candidates, but this bias decreased as K increased and was not worse than the cold-start baseline."
key_figures_tables:
  - "Figure 2: Latent space of candidates and logistic regression decision boundaries → Shows political spectrum captured by the model."
  - "Figure 3: PCA projection of GPT-generated data compared to real candidates → GPT data clusters distinctly by party but is slightly more centred."
  - "Figure 5: RMSE and CRA over users for different initialisations → Pre-training with GPTvoters significantly improves early performance."
  - "Figure 6: Break-even points for varying K → Relationship between answer count and break-even point depends on the downstream task."
  - "Table 2: Distances of GPT samples to party-means vs. candidates → GPT samples are significantly closer for most parties."
key_equations:
  - equation: "L(v_p) = ||v_p - \\bar{y}_p||^2 - \\sum_{q \\neq p} ||v_p - \\bar{y}_q||^2"
    explanation: "Vertex for each party maximizing own distance to others."
  - equation: "f(w; \\alpha) = \\frac{1}{B(\\alpha)} \\prod_{p=1}^P w_p^{\\alpha_p - 1}"
    explanation: "Dirichlet distribution for generating voter weights."
definitions:
  - term: "Cold start problem"
    definition: "Difficulty in making accurate predictions or recommendations for new users or items with limited initial data."
  - term: "Adaptive questionnaire"
    definition: "A survey that dynamically selects the next question based on previous answers to maximise information gain."
  - term: "Voting Advice Application (VAA)"
    definition: "An online tool that recommends political parties or candidates based on user responses to policy questions."
  - term: "Ideal point estimation"
    definition: "Statistical method to estimate a person's or group's position in a low-dimensional ideological space from their responses."
  - term: "Uncertainty sampling"
    definition: "An active learning strategy where the model selects the question with the most uncertain prediction."
  - term: "GPT-4"
    definition: "A large language model developed by OpenAI used for generating synthetic data."
critical_citations:
  - "[Montgomery & Cutler, 2013] — Demonstrates adaptive testing for public opinion surveys."
  - "[Lika et al., 2014] — Defines and reviews the cold start problem in recommender systems."
  - "[Argyle et al., 2023] — Shows LLMs can emulate human response distributions."
  - "[Bachmann et al., 2024] — Proposes fast adaptive questionnaires for VAAs."
  - "[Clinton et al., 2004] — Provides the IDEAL framework for ideal point estimation."
relevance:
  topics:
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "high"
      justification: "Directly addresses the cold-start problem for user profiling using synthetic data."
    - code: "8.C"
      name: "Cold‑Start Baseline Strategies for Anomaly Detection"
      relevance: "high"
      justification: "Proposes a baseline strategy (synthetic pre-training) applicable to cold-start detection."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Uses predictive models for user responses, analogous to spending prediction."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides a rigorous evaluation framework (RMSE, CRA, break-even analysis)."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Evaluates the performance of the question-selection algorithm under different initialisations."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "low"
      justification: "Uses classification (logistic regression) for profile prediction but in a political domain."
  contribution: "This paper contributes a novel method for mitigating the cold-start problem in adaptive systems using LLM-generated synthetic user interactions. For Odin, this directly informs the design of the user profiling and cold-start module (5.B) by demonstrating a cost-effective pre-training strategy. The evaluation metrics (RMSE, CRA) and break-even analysis provide a template for evaluating Odin's own adaptive modules (12.A, 12.B). Furthermore, the paper's approach to generating diverse synthetic data via interpolation (GPTvoters) offers a concrete technique for creating robust initial models in the absence of real data."
  directly_justifies:
    - "LLM-generated synthetic data can significantly reduce prediction error for early users in adaptive questionnaires."
    - "Pre-training with synthetic data improves candidate recommendation accuracy by over 17% for initial users."
    - "The initial advantage of synthetic pre-training is eventually eroded by real user interactions after a break-even point."
    - "Break-even points depend on the amount of data collected per user and the specific downstream task."
    - "Synthetic data can introduce biases, but these can be managed and are not necessarily worse than cold-start baselines."
  limits:
    - "Method requires an LLM with sufficient domain knowledge; may not generalise to all domains like movie recommendations."
    - "Potential for path dependency where initial biases from synthetic data are reinforced by later question selection."
    - "Simulation is limited to a specific question-selection strategy (uncertainty sampling) and a two-dimensional latent space."
    - "Optimal replacement rate for synthetic data was determined heuristically, not learned or analytically derived. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. This paper was flagged as highly relevant to the 'Behavioral Profiling & Classification' domain, specifically topic 5.B (Profile Dynamics and the Cold‑Start Problem), as it directly tackles the cold-start issue using synthetic data. It also strongly relates to 8.C (Cold‑Start Baseline Strategies) for anomaly detection, as the pre-training method is a direct baseline. Topics under 'Spending Forecasting' (6.A) and 'System Evaluation' (12.A, 12.B) were deemed medium relevance, as the predictive modeling approach and the evaluation framework (RMSE, break-even analysis) are transferable. The paper's classification approach (5.C) was considered low relevance, as it is applied to political profiles, not financial ones. Other domains like 'Filipino Cultural Context' (2.A, 2.B) and 'Expense Categorization' (3.A) were rejected as the paper is domain-agnostic and does not address cultural or expense-specific contexts. The overall relevance to Odin is high for addressing cold-start problems in user profiling, providing a validated method for generating synthetic training data that can be adapted to financial behavior data."
limitations:
  - "Requires an LLM with domain knowledge; may not generalise to all recommender system domains."
  - "Potential for path dependency and bias reinforcement from synthetic data. [unacknowledged]"
  - "Simulation limited to one question-selection strategy and a two-dimensional latent space."
  - "Optimal replacement rate for synthetic data was not systematically derived or learned. [unacknowledged]"
  - "The approach may not address all types of cold-start problems, such as those with entirely new items. [unacknowledged]"
remember_this:
  - "GPT-4 generated synthetic data that was, on average, closer to party-means than real candidates."
  - "Pre-training with synthetic data reduced initial prediction error by 25% compared to cold start."
  - "The initial advantage of synthetic pre-training erodes after 85 to 895 real users."
  - "Synthetic data can improve initial recommendations but requires careful management of biases."
  - "A break-even point of 4,500 user interactions was observed for missing value imputation accuracy."
```
---

## Paper 18: Jamal & Hashmat_summarized.md

**Source File:** `Jamal & Hashmat_summarized.md`

```yaml
paper_id: "10.5281/zenodo.15478961"
designation: "international"
title: "Innovations in UI/UX Design of Mobile Applications: Trends, Practices and Challenges"
authors: "Jamal, A.; Hashmat, S."
year: 2025
venue: "Spectrum of Engineering Sciences"
odin_topics:
  - "9.A"
  - "9.B"
  - "11.A"
  - "11.B"
tldr: "A PRISMA-guided review of 20 peer-reviewed studies (2017–2024) synthesizes current trends, best practices, and challenges in mobile UI/UX design."
problem_and_motivation: "Rapid mobile technology advancements have outpaced conventional interface capabilities, creating a gap between user expectations for seamless, intuitive interactions and what standard designs provide. A comprehensive synthesis of emerging trends, best practices, and persistent challenges is needed to guide designers and developers."
approach:
  - "A review methodology guided by the PRISMA framework was employed."
  - "Systematic literature search was conducted across Google Scholar, IEEE Xplore, ACM Digital Library, ScienceDirect, and SpringerLink using Boolean keyword combinations."
  - "Initial screening of 243 records was performed, with duplicates removed leaving 230 unique records for title and abstract screening."
  - "Full-text eligibility assessment of 45 articles against inclusion/exclusion criteria (peer-reviewed, 2017–2024, mobile UI/UX focus) was conducted."
  - "A final set of 20 studies were selected and thematically synthesized into categories: usability, personalization, accessibility, and immersive technologies."
findings:
  - "num: 20 peer-reviewed publications from 2017-2024 were included in the final synthesis."
  - "Key trends include AI-driven personalization, AR/VR integration, Voice User Interfaces, and dark mode/minimalist design."
  - "User-Centered Design (UCD), iterative testing, and performance optimization remain core best practices for mobile UI/UX."
  - "Major challenges include limited screen real estate, cognitive load, cross-platform consistency, and evolving user expectations."
  - "Design thinking and AI-driven automation represent complementary emerging approaches, with hybrid models balancing empathy and efficiency."
  - "Inclusive design features like screen readers and adjustable text sizes are under-prioritized in practice, despite being recognized as essential."
  - "Cross-platform frameworks (Flutter, React Native) are preferred for consistency and scalability but present performance tuning challenges."
  - "Gestural interactions reduce visual clutter and improve task efficiency, though effectiveness depends on user familiarity."
key_figures_tables:
  - "Table 1: Inclusion and Exclusion Criteria → Defines selection parameters for systematic review."
  - "Table 2: Emerging Trends and Approaches → Summarizes key trends and design implications."
  - "Table 3: Design Approaches in Mobile UI/UX → Compares core characteristics and design implications."
  - "Table 4: Best Practices and Implementation → Details core principles and real-world application challenges."
  - "Table 5: Challenges in Mobile UI/UX Practice → Outlines key challenges and their design impact."
  - "Table 6: Implications for Designers and Developers → Provides actionable recommendations for practice."
  - "Table 7: Selected Literature → Lists key studies reviewed, their themes, and publication details."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "AI"
    definition: "Artificial Intelligence."
  - term: "AR"
    definition: "Augmented Reality."
  - term: "ML"
    definition: "Machine Learning."
  - term: "PRISMA"
    definition: "Preferred Reporting Items for Systematic Reviews and Meta-Analyses."
  - term: "UCD"
    definition: "User-Centered Design."
  - term: "UI"
    definition: "User Interface."
  - term: "UX"
    definition: "User Experience."
  - term: "VR"
    definition: "Virtual Reality."
  - term: "VUI"
    definition: "Voice User Interface."
critical_citations:
  - "[Azuma, 1997] — Foundational AR technology survey."
  - "[Krug, 2014] — Established usability heuristics for interfaces."
  - "[Marcotte, 2010] — Originated responsive web design concepts."
  - "[Norman, 2013] — Core principles of user-centered design and everyday usability."
  - "[Shneiderman, 2016] — Established strategies for human-computer interaction design."
relevance:
  topics:
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "high"
      justification: "Paper explicitly discusses mobile-first design as a core principle."
    - code: "9.B"
      name: "Mobile UX Design for Personal Finance"
      relevance: "high"
      justification: "Review synthesizes best practices directly applicable to PFMS UX design."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "medium"
      justification: "Discusses personalization and feedback loops that drive user engagement."
    - code: "11.B"
      name: "Retention Mechanisms and Engagement Design"
      relevance: "medium"
      justification: "Findings on micro-interactions and continuous feedback directly inform retention strategies."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "contextual"
      justification: "Discusses user behavior analysis at a general level, not specific to financial profiles."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "low"
      justification: "Only tangentially mentioned; no substantive discussion on data privacy."
  contribution: "This paper provides a comprehensive, evidence-based framework for mobile UX design that directly supports Odin's mobile-first architecture. Its systematic synthesis of personalization and adaptive interface trends justifies implementing data-driven customization in Odin's dashboard. The identified best practices for iterative testing and user-centered design validate Odin's planned usability testing methodology. The discussion of cross-platform consistency challenges informs Odin's choice of development frameworks. The findings on performance optimization and accessibility are directly relevant to Odin's goal of serving a diverse Filipino user base with varying device capabilities."
  directly_justifies:
    - "A mobile-first design approach is essential for optimizing usability on small screens and ensuring core functionality is accessible."
    - "Implementing personalization and adaptive interfaces enhances user engagement by tailoring content and interactions to individual preferences."
    - "Iterative testing and continuous feedback loops are critical for refining mobile UI/UX and aligning with user expectations."
    - "Addressing challenges such as cognitive load and cross-platform consistency is key to developing effective and inclusive mobile applications."
  limits:
    - "The review is limited to 20 studies, potentially omitting other relevant UI/UX literature."
    - "Findings are qualitative and synthesized thematically, with no quantitative meta-analysis."
    - "Study selection is constrained to publications from 2017-2024, possibly excluding earlier foundational work."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated canonical topic codes was performed. Domains flagged as relevant were Mobile-First Design (9.A, 9.B) with high relevance due to the paper's direct focus on mobile UI/UX principles, and Engagement & Retention (11.A, 11.B) with medium relevance via its discussion of personalization and feedback mechanisms. Behavior Profiling (5.A) was considered contextual, as the paper discusses general user behavior analysis but not financial profiling. Domains like Expense Categorization, Spending Forecasting, Budget Recommendation, Anomaly Detection, Data Privacy, Savings, and Debt Management were rejected as the paper does not address these financial-specific areas. The overall relevance to Odin is high, providing foundational UX best practices essential for its mobile-first design."
limitations:
  - "The review's reliance on a small sample of 20 studies may limit the generalizability of findings."
  - "Lack of quantitative meta-analysis prevents statistical synthesis of effect sizes [unacknowledged]."
  - "The search strategy may have missed grey literature or industry reports not indexed in selected databases [unacknowledged]."
  - "Potential publication bias exists, as only peer-reviewed articles from 2017-2024 were included [unacknowledged]."
remember_this:
  - "Personalization and AR/VR are key trends shaping modern mobile UX."
  - "User-centered design and iterative testing remain essential best practices."
  - "Cross-platform consistency and performance optimization are major design challenges."
  - "Inclusive design features are under-prioritized in practice despite recognized importance."
  - "The review synthesized findings from 20 peer-reviewed studies (2017-2024)."
```
---

## Paper 19: Andersson_summarized.md

**Source File:** `Andersson_summarized.md`

```yaml
paper_id: 10.1556/2006.2025.00013
designation: international-algorithm-specific
title: Insights into the temporal dynamics of identifying problem gambling on an online casino: A machine learning study on routinely collected individual account data
authors: Andersson, S.; Carlbring, P.; Lyon, K.; Bermell, M.; Lindner, P.
year: 2025
venue: Journal of Behavioral Addictions
odin_topics:
  - 5.B
  - 5.C
  - 8.B
  - 10.A
  - 10.B
tldr: Machine learning on online gambling account data enables stable and early classification of players into low-risk and higher-risk categories, supporting real-time intervention.
problem_and_motivation: Identifying problem gamblers is crucial for public health, but existing methods like self-report and cross-sectional behavioral tracking suffer from validity issues and fail to capture temporal dynamics. A robust, scalable, and temporally stable method for early identification is needed to enable timely interventions.
approach:
  - Analyzed a 4.5-year dataset from a Swedish online gambling provider covering 35,048 players with detailed behavioral and transactional data.
  - Extensive feature engineering captured gambling behavior dynamics such as loss chasing, betting frequency, session length, and spending patterns.
  - Trained an XGBoost classifier to distinguish low-risk from higher-risk players, using a binary label derived from manual risk assessments.
  - Evaluated temporal stability by truncating training data at 30, 60, and 90 days before the maximum timestamp and comparing holdout performance.
  - Used SHAP values for feature importance and a nested forward-chaining cross-validation strategy to avoid data leakage.
findings:
  - num: Precision decreased slightly with data truncation, with a 95% CI entirely below zero [(−0.005, −0.001)].
  - num: F1 score remained stable across truncations, with a 95% CI for its linear slope including zero [(−0.008, 0.035)].
  - Loss chasing behavior, net balance trend, max deposit, session sum, and total bets daily were the most influential features across all truncation periods.
  - The model consistently underestimated risk for the low-risk category, with the largest gap (0.337) in the full dataset.
  - The model performed well for medium- and high-risk categories, with predicted means closely matching true means.
key_figures_tables:
  - "Figure 2: SHAP summary plot of top features → Loss chasing and net balance trend are most influential."
  - "Figure 3: Temporal evaluation of prediction stability → Performance metrics remained stable across data truncations."
  - "Table 1: Model performance metrics for different truncation labels → Metrics like F1 and ROC AUC were consistent."
  - "Table 2: Risk category prediction table with difference → Model underestimates low-risk but performs well for high-risk."
  - "Figure 4: Difference between true and predicted means → Prediction gap is largest for low-risk and smallest for high-risk."
key_equations:
  - equation: None.
    explanation: No explicit equations are presented in the paper.
definitions:
  - term: SHAP
    definition: SHapley Additive exPlanations, a method to explain individual predictions by attributing contributions to each feature.
  - term: XGBoost
    definition: eXtreme Gradient Boosting, a scalable and efficient machine learning algorithm for classification and regression.
  - term: GMLVQ
    definition: Generalized Matrix Learning Vector Quantization, a supervised learning technique for discriminative feature relevance.
critical_citations:
  - "[Auer & Griffiths, 2022] — Demonstrates machine learning for predicting limit-setting behavior."
  - "[Perrot et al., 2022] — Develops a prediction model for online gambling problems using account data."
  - "[Braverman & Shaffer, 2012] — Identifies behavioral markers for high-risk internet gambling."
relevance:
  topics:
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: Evaluates temporal stability of risk classification, relevant to dynamic profile updating.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Directly applies XGBoost classification to behavioral data for risk profiling.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Loss-chasing and spending patterns are used as key features for anomaly/risk detection.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Context of responsible gambling and duty of care, but not focused on PFMS data privacy.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: contextual
      justification: Discusses timely interventions and duty of care, which relate to user trust.
  contribution: This paper demonstrates the feasibility of using machine learning for early and stable classification of at-risk individuals based on behavioral data, a concept directly transferable to Odin's anomaly detection module. The focus on temporal stability using truncated training data provides a methodology for evaluating and implementing dynamic behavioral profiling in a PFMS. The identification of key predictive features like spending trends and loss-chasing behavior offers concrete signals for Odin's spending forecasting and anomaly detection systems. Furthermore, the study's emphasis on real-world deployment and regulatory compliance aligns with Odin's need for a reliable and trusted system.
  directly_justifies:
    - "Machine learning can reliably classify behavioral risk profiles with stable performance over time."
    - "Features like loss chasing and spending trends are key predictors of problematic financial behavior."
    - "Predictive models can be effectively trained on historical data to enable early intervention."
    - "Temporal stability of predictions supports their use in real-time monitoring systems."
  limits:
    - "Dataset comes from a single gambling operator, limiting generalizability due to lack of a 'single customer view'."
    - "Risk labels used for training may have temporal biases and inconsistencies due to manual assessment."
    - "The truncation strategy may bias the model toward accounts with more extensive activity histories."
    - "Bootstrapping analysis for temporal trends was limited by a small sample size (four data points per metric)."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper's focus on machine learning for risk classification and temporal stability directly maps to the Behavioral Profiling & Classification (5) and Anomaly Detection (8) domains. Specifically, the paper was assigned `high` relevance to 5.C (Classification Approaches) and 8.B (Anomaly Detection Algorithms) due to its direct application of XGBoost for binary risk classification and its use of behavioral features like loss-chasing. A `medium` relevance was assigned to 5.B (Profile Dynamics) as the temporal stability analysis is relevant to how profiles change and are updated. Domains related to User Trust and Data Privacy (10) were considered but assigned `contextual` relevance, as the paper discusses duty of care and intervention in a gambling context, which is analogous to trust in PFMS but not a direct focus. Domains like Expense Categorization (3), Budget Recommendation (7), and Savings & Debt Management (13) were rejected as the paper does not address these specific personal finance functions. Overall, the paper provides strong evidence for the algorithmic core of Odin's risk and anomaly detection capabilities.
limitations:
  - "Temporal biases in risk labels may lead the model to capture historical patterns rather than genuine risk. [unacknowledged]"
  - "The analysis is limited to a single operator, lacking data on cross-operator gambling activity. [acknowledged]"
  - "The truncation strategy may inadvertently bias the model toward accounts with longer activity histories. [acknowledged]"
  - "The low-risk category was consistently underestimated, indicating a potential weakness in distinguishing low from moderate risk."
remember_this:
  - "Machine learning models can classify risk profiles with stable performance over time."
  - "Loss chasing and spending trends are the most predictive features for risk classification."
  - "Precision decreased slightly with less historical data, but overall metrics remained stable."
  - "The model effectively identifies high-risk individuals but struggles with low-risk classification."
  - "Temporal stability of predictions supports real-time monitoring and early intervention."
```
---

## Paper 20: Mannapur_summarized.md

**Source File:** `Mannapur_summarized.md`

```yaml
paper_id: 10.32628/CSEIT25111239
designation: international
title: Understanding Data Drift and Concept Drift in Machine Learning Systems
authors: Mannapur, S.
year: 2025
venue: International Journal of Scientific Research in Computer Science, Engineering and Information Technology
odin_topics:
  - 12.A
  - 12.B
  - 12.C
  - 6.A
  - 7.B
  - 8.A
  - 10.A
  - 11.A
tldr: Data and concept drift cause significant performance degradation in production ML systems, necessitating proactive detection and adaptive mitigation strategies.
problem_and_motivation: Production machine learning models face performance degradation from evolving data patterns, a phenomenon known as drift, which often goes undetected. This is a critical issue for system reliability, particularly in safety-critical domains like healthcare, where undetected drift can lead to increased misdiagnosis and patient risk. The problem is compounded by a lack of standardized, proactive monitoring, and mitigation frameworks across various industries.
approach:
  - This is a comprehensive review article analyzing data drift and concept drift in ML systems.
  - It synthesizes findings from real-world implementations across healthcare, manufacturing, and autonomous driving.
  - The paper examines different drift types, including covariate and prior probability shifts, and their impacts.
  - It presents advanced detection methodologies like KS tests, JSD, PSI, and algorithms such as DDM and ADWIN.
  - The review also explores mitigation strategies, including adaptive retraining, ensemble methods, and monitoring frameworks.
findings:
  - num: Undetected drift leads to an average model accuracy degradation of 31.7%, with healthcare applications seeing up to 52% degradation in the first year.
  - num: Concept drift affects 82.4% of production quality prediction models in manufacturing, with an average detection delay of 38 days.
  - num: KS-test-based monitoring systems successfully identified 91.3% of significant distribution changes in autonomous driving sensor data within 18 milliseconds.
  - Implementing adaptive retraining can improve model accuracy by up to 42.8% in dynamic maritime environments.
  - Combining multiple drift detection approaches improves accuracy by up to 53.2% compared to single-metric methods.
  - num: A five-tier escalation framework for drift response reduced mean time to resolution for critical events by 68.5% in manufacturing.
  - num: Energy-aware retraining systems reduced model degradation by 76.8% while decreasing carbon footprint by 52.4% in sustainable manufacturing.
  - num: Resource-aware feature selection improved model stability by 63.2% and reduced energy consumption by 47.8%.
key_figures_tables:
  - Table 1: Performance degradation analysis across different concept drift patterns → Shows varied impacts of drift types on model performance.
  - Table 2: Performance comparison of concept drift detection methods in edge computing → Highlights trade-offs between detection accuracy, computational cost, and resource usage.
  - Figure 1: Manufacturing Process Drift Analysis: Percentage Changes Across Different Drift Types → Visualizes the magnitude of changes caused by different drift types.
  - Figure 2: Performance Metrics of Different Drift Detection Approaches in Autonomous Driving → Compares effectiveness of KS, JSD, and PSI methods.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Data Drift
    definition: A shift in the statistical properties of input features over time.
  - term: Concept Drift
    definition: An evolution in the relationship between input features and target variables.
  - term: Covariate Shift
    definition: A type of data drift where the distribution of input features changes.
  - term: Prior Probability Shift
    definition: A change in the distribution of the target variable.
  - term: KS Test
    definition: Kolmogorov-Smirnov test, a non-parametric test for comparing distributions.
  - term: JSD
    definition: Jensen-Shannon Divergence, a method for measuring similarity between probability distributions.
  - term: PSI
    definition: Population Stability Index, a metric for monitoring distribution stability.
  - term: DDM
    definition: Drift Detection Method, an algorithm for identifying concept drift.
  - term: ADWIN
    definition: Adaptive Windowing, an algorithm for detecting drift in data streams.
  - term: OEE
    definition: Overall Equipment Effectiveness, a measure of manufacturing productivity.
critical_citations:
  - "[Kore, 2024] — Provides empirical data on drift in medical imaging."
  - "[Patchipala, 2024] — Details strategies for tackling data and model drift."
  - "[Zenisek, 2019] — Foundational work on concept drift in predictive maintenance."
  - "[Agrahari, 2022] — Comprehensive literature review on concept drift detection."
relevance:
  topics:
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides metrics and frameworks for evaluating system performance degradation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Offers quantitative data on how drift affects algorithmic performance (accuracy, etc.).
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Discusses backtesting and performance monitoring applicable to evaluating budget recommendations.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Highlights the need for monitoring prediction accuracy due to evolving spending patterns.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: contextual
      justification: The concepts of drift in user financial behavior are relevant but not directly addressed.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Drift can increase false positives in anomaly detection, a key concern for Odin.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: The paper discusses drift detection, not privacy, but model reliability impacts user trust.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: Performance degradation from drift can negatively impact user engagement and trust.
  contribution: This paper provides the core justification for Odin's need for a robust system evaluation and monitoring module (12.A, 12.B) to detect performance drift. It offers a comprehensive overview of drift types and detection methods that can be applied to Odin's forecasting (6.A) and anomaly detection (8.A) modules. The findings on proactive monitoring and mitigation strategies are directly relevant for designing Odin's automated retraining and alerting mechanisms. The paper emphasizes that continuous performance evaluation is not a one-time activity but a critical, ongoing operational requirement for any deployed personal finance management system.
  directly_justifies:
    - Continuous monitoring of forecasting accuracy is crucial to maintain system reliability.
    - Performance degradation should be quantified and tracked over time.
    - An automated escalation framework is needed to address significant model drift.
    - Drift detection can reduce the need for frequent, costly full system retraining.
  limits:
    - The review does not provide a specific implementation guide for drift detection in personal finance data.
    - The paper focuses on general ML systems, not PFMS-specific financial behavior drift (e.g., seasonal spending changes).
  mapping_rationale: A systematic scan of all 12 Odin functional domains was performed against this paper's content. The paper is most strongly relevant to the System Evaluation domain (12.A, 12.B, 12.C) as it provides the foundational concepts, metrics, and frameworks for assessing and maintaining model performance. It was also flagged for the Forecasting and Anomaly Detection domains (6.A, 8.A) because drift in user data will directly affect the accuracy of these modules. The paper is considered contextual for Budget Recommendation (7.B) as its core thesis on performance degradation applies, though it does not specifically address budgeting algorithms. Domains like Savings & Debt Management (13.A-C) or User-Declared Preferences (2.C) were considered and rejected as the paper does not discuss these financial concepts. The overall relevance is high because it justifies the need for a comprehensive evaluation and monitoring subsystem within Odin, which is a key architectural component.
limitations:
  - The paper is a review and does not present novel experimental results.
  - The findings are synthesized from various domains, which may not directly translate to personal finance. [unacknowledged]
  - The paper does not address the specific challenge of cold-start drift detection, which is a key issue for Odin. [unacknowledged]
remember_this:
  - Undetected drift degrades model accuracy by an average of 31.7%.
  - Concept drift affects 82.4% of production quality prediction models.
  - Proactive drift detection can reduce model degradation by up to 83.5%.
  - Continuous monitoring and adaptive retraining are essential for long-term system reliability.
  - Combining multiple drift detection methods improves overall detection accuracy.
```
---

## Paper 21: Dritsas & Trigka_summarized.md

**Source File:** `Dritsas & Trigka_summarized.md`

```yaml
paper_id: "10.1109/ACCESS.2025.3572865"
designation: "international"
title: "Machine Learning in E-Commerce: Trends, Applications, and Future Challenges"
authors: "Dritsas, E.; Trigka, M."
year: 2025
venue: "IEEE Access"
odin_topics:
  - "5.A"
  - "5.B"
  - "5.C"
  - "6.A"
  - "6.B"
  - "8.A"
  - "8.B"
  - "10.A"
  - "10.B"
  - "11.A"
  - "11.B"
tldr: "Surveys machine learning paradigms applied to e-commerce, including supervised, unsupervised, reinforcement, and hybrid learning, and identifies challenges and future research directions."
problem_and_motivation: "The literature on ML in e-commerce is fragmented across domains and often lacks technical depth or fails to incorporate emerging paradigms. Prior surveys focus on limited use cases or overlook system-level constraints like interpretability and privacy. A unified synthesis bridging foundational and frontier ML techniques with e-commerce-specific challenges is needed."
approach:
  - "Conducted a targeted literature search across IEEE Xplore, ACM Digital Library, SpringerLink, ScienceDirect, and Google Scholar for peer-reviewed studies from the last seven years."
  - "Applied inclusion criteria requiring peer-reviewed, English-language articles with technical insights on ML deployment in e-commerce."
  - "Classified selected literature across three dimensions: ML paradigms, functional domains, and cross-cutting challenges."
  - "Synthesized findings into a taxonomy with comparative tables and a research roadmap."
findings:
  - "Supervised learning remains the most extensively applied paradigm in e-commerce, underpinning fraud detection and demand forecasting."
  - "Reinforcement learning has emerged as a powerful tool for dynamic pricing and personalized recommendations."
  - "Hybrid models combining supervised and unsupervised techniques enhance generalization and robustness."
  - "Challenges include data privacy, interpretability, scalability, and real-time processing latency."
  - "Emerging directions include federated learning, neurosymbolic AI, quantum machine learning, and multimodal AI."
key_figures_tables:
  - "Figure 1: Synthesized map of survey's thematic scope → Illustrates interplay of learning strategies, operational roles, and challenges."
  - "Figure 2: Landscape of ML paradigms, techniques, and applications → Maps methodologies to e-commerce functions."
  - "Table 1: Taxonomy of ML paradigms → Contrasts supervised, unsupervised, RL, hybrid, and meta-learning with strengths and limitations."
  - "Table 2: Application domains and ML techniques → Maps functional scope, techniques, benefits, and gaps."
  - "Table 3: Challenges and limitations → Categorizes obstacles and potential solutions."
  - "Table 4: Future research directions → Outlines emerging areas, challenges, and expected impact."
  - "Table 5: Summary of prior surveys → Compares scope, depth, and foresight of existing reviews."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Supervised learning"
    definition: "ML paradigm using labelled data to train predictive models."
  - term: "Unsupervised learning"
    definition: "ML paradigm discovering latent structures in unlabeled data."
  - term: "Reinforcement learning"
    definition: "ML paradigm where an agent learns optimal actions through trial and error with rewards."
  - term: "Federated learning"
    definition: "Decentralized ML training across devices without sharing raw data."
  - term: "Quantum machine learning"
    definition: "ML leveraging quantum computing principles for accelerated optimization."
  - term: "Continual learning"
    definition: "ML that retains past knowledge while learning new information, avoiding catastrophic forgetting."
  - term: "Neuro-symbolic AI"
    definition: "Integration of deep neural networks with symbolic reasoning for interpretable models."
critical_citations:
  - "[Iqbal, 2022] — overview of ML applications in e-commerce."
  - "[Raman et al., 2025] — methodology for survey framework."
  - "[Achuthan et al., 2024] — cybersecurity and privacy trends."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Covers customer segmentation and behavioral clustering using ML."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "high"
      justification: "Discusses cold-start problems in recommendation systems."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Reviews classification methods for behavioral profiling."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Demand forecasting is predictive modeling analogous to spending prediction."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Covers LSTM, transformers for time-series forecasting."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Fraud detection is a core anomaly detection application."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Reviews autoencoders, isolation forests for anomaly detection."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "medium"
      justification: "Discusses federated learning and differential privacy for data protection."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "medium"
      justification: "Covers model interpretability and XAI techniques to build trust."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "medium"
      justification: "Addresses customer engagement through personalization."
    - code: "11.B"
      name: "Retention Mechanisms and Engagement Design"
      relevance: "medium"
      justification: "Discusses churn prediction and retention strategies."
  contribution: "The survey's review of anomaly detection algorithms informs Odin's fraud and anomaly detection module (8.A, 8.B). Its analysis of forecasting methods supports Odin's spending prediction module (6.A, 6.B). The discussion of behavioral clustering and cold-start problems guides Odin's user profiling and profile dynamics (5.A, 5.B, 5.C). Privacy-preserving techniques like federated learning provide a foundation for Odin's data privacy module (10.A). The survey's insights on engagement and retention inform Odin's user engagement design (11.A, 11.B)."
  directly_justifies:
    - "Supervised learning with ensemble methods improves fraud detection accuracy."
    - "Reinforcement learning enables adaptive pricing and personalized recommendations."
    - "Hybrid models enhance generalization and robustness in e-commerce applications."
    - "Federated learning allows privacy-preserving model training across distributed data."
    - "Explainable AI techniques like SHAP and LIME enhance model interpretability."
  limits:
    - "The survey does not provide empirical validation of the surveyed methods."
    - "It lacks detailed implementation guidance for specific e-commerce platforms."
    - "The focus on e-commerce may not fully translate to personal finance contexts without adaptation."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The domains most directly relevant to Odin are Behavioral Profiling & Classification (5.A, 5.B, 5.C), Spending Forecasting (6.A, 6.B), Anomaly Detection (8.A, 8.B), Data Privacy & User Trust (10.A, 10.B), and User Retention & Engagement (11.A, 11.B). These were assigned high or medium relevance based on the paper's coverage of customer segmentation, cold-start problems, predictive modeling, fraud detection, privacy-preserving ML, interpretability, and engagement dynamics. Borderline cases included Seasonal Spending (2.B) and Expense Categorization (3.A), which were rejected because the paper focuses on e-commerce demand forecasting rather than personal spending cycles and does not address category design. Existing Systems & Gaps (4.A, 4.B) were considered but rejected because the paper surveys e-commerce systems, not PFMS. The overall relevance is high for core algorithmic modules (forecasting, anomaly detection, profiling) and medium for privacy and engagement aspects, providing a broad foundation for Odin's design."
limitations:
  - "Does not address the specific cultural and financial context of Filipino young professionals."
  - "The survey is limited to e-commerce and may not directly apply to personal finance management."
  - "No empirical comparison of the surveyed algorithms is provided."
remember_this:
  - "Machine learning enhances personalization, fraud detection, and pricing in e-commerce."
  - "Challenges include data privacy, interpretability, scalability, and real-time processing."
  - "Emerging paradigms like federated learning and quantum ML offer future opportunities."
  - "Hybrid models and neurosymbolic AI bridge interpretability and predictive accuracy."
```
---

## Paper 22: Ibrahim et al_summarized.md

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

## Paper 23: Yunita et al_summarized.md

**Source File:** `Yunita et al_summarized.md`

```yaml
paper_id: 10.1016/j.mex.2025.103462
designation: international-algorithm-specific
title: Performance analysis of neural network architectures for time series forecasting: A comparative study of RNN, LSTM, GRU, and hybrid models
authors: Yunita, A.; Pratama, M. I.; Almuzakki, M. Z.; Ramadhan, H.; Akhir, E. A. P.; Mansur, A. B. F.; Basori, A. H.
year: 2025
venue: MethodsX
odin_topics:
  - 6.A
  - 6.B
  - 8.B
  - 8.C
  - 12.A
  - 12.B
  - 12.C
tldr: Benchmarks nine RNN, LSTM, GRU, and hybrid architectures using Monte Carlo simulation across three datasets; Friedman test shows no statistically significant performance differences despite descriptive advantages for LSTM-based hybrids.
problem_and_motivation: The inherent variability in neural network performance due to random weight initialization raises concerns about the reliability and consistency of these architectures for time series analysis. Previous studies proposing hybrid models often train them only once, failing to account for performance variance. A systematic benchmark that evaluates model stability across multiple runs is needed to guide reliable architecture selection.
approach:
  - Evaluated nine architectures: vanilla RNN, LSTM, GRU, and six hybrids (RNN-LSTM, RNN-GRU, LSTM-RNN, GRU-RNN, LSTM-GRU, GRU-LSTM).
  - Used three real-world time series datasets: sunspot activity (monthly, n=3625), Indonesian COVID-19 cases (daily, n=634), and dissolved oxygen readings (daily, n=1033).
  - Implemented Monte Carlo simulation with 100 independent iterations per model, each with 100 training epochs, using a 70:30 or 80:20 train-test split.
  - Evaluated performance using MAE, MAPE, RMSE, and computation time, with results analyzed via 95% confidence interval trimming.
  - Applied the Friedman test as a non-parametric statistical comparison to assess performance differences across architectures and datasets.
findings:
  - num: The Friedman test revealed no statistically significant differences among the nine architectures (χ²=12.593, df=8, p=.127).
  - num: LSTM-GRU achieved the lowest mean rank (2.23) across all datasets, while vanilla RNN showed the highest (8.57).
  - num: For sunspot forecasting, LSTM-GRU had the lowest RMSE (23.205 ± 0.827), and GRU-LSTM achieved the best MAPE (36.242% ± 3.627%).
  - num: For COVID-19 case prediction, standalone LSTM performed best with the lowest MAPE (9.036% ± 0.778%) and competitive MAE (0.903 ± 0.091).
  - num: For dissolved oxygen forecasting, LSTM-RNN achieved the lowest MAE (2.970 ± 0.229) and RMSE (4.041 ± 0.242).
  - LSTM-based hybrid architectures consistently demonstrated superior descriptive performance and stability across datasets compared to single architectures.
  - Vanilla RNN exhibited the fastest computation time but showed the highest error rates and largest variance across all datasets.
  - The LSTM-RNN hybrid offered an optimal balance between prediction accuracy and computational efficiency.
  - Hybrid architectures generally outperformed single-architecture models in descriptive analysis.
key_figures_tables:
  - Table 1: Dataset characteristics including record counts, interval types, and value ranges → Provides context for evaluating model performance across diverse data distributions.
  - Table 2: Detailed architecture specifications with layer types and parameter counts → Shows the structural design and complexity of each benchmarked model.
  - Table 3: Performance comparison across all architectures with mean ranks → Demonstrates relative performance tiers despite non-significant statistical differences.
  - Table 4: Overall model rankings based on Friedman test → Shows LSTM-GRU as best performer (rank 2.23) and vanilla RNN as worst (rank 8.57).
  - Figure 4: Box plots of error metrics for sunspot dataset → Visualizes performance stability and variance across architectures.
  - Figure 6: Benchmark results for COVID-19 dataset → Shows vanilla LSTM's superior performance for epidemiological forecasting.
  - Figure 8: Evaluation metrics for oxygen dataset → Demonstrates LSTM-RNN's balanced accuracy and stability.
key_equations:
  - equation: "MAE = (1/n) Σ |y_i - ŷ_i|"
    explanation: Average magnitude of prediction errors in original units.
  - equation: "MAPE = (100/n) Σ |(y_i - ŷ_i) / y_i|"
    explanation: Scale-independent percentage error for comparing across magnitudes.
  - equation: "RMSE = sqrt((1/n) Σ (y_i - ŷ_i)²)"
    explanation: Penalizes larger errors heavily, sensitive to outliers.
  - equation: "h_t^R = g(W · x_t + U · h_{t-1}^R + b)"
    explanation: RNN hidden state update with activation function.
  - equation: "z_t = σ(W_xz x_t + W_hz h_{t-1} + b_z)"
    explanation: GRU update gate controlling information retention.
definitions:
  - term: RNN
    definition: Recurrent Neural Network; processes sequential data using hidden states that capture temporal dependencies.
  - term: LSTM
    definition: Long Short-Term Memory; RNN variant with cell state and three gates to address vanishing gradient and long-term dependencies.
  - term: GRU
    definition: Gated Recurrent Unit; LSTM variant with two gates (update and reset) offering simpler architecture.
  - term: Monte Carlo simulation
    definition: Probabilistic evaluation method using repeated random sampling to quantify model performance uncertainty.
  - term: Hybrid model
    definition: Neural network combining two different recurrent architectures in stacked configuration.
  - term: MAE
    definition: Mean Absolute Error; average absolute difference between predicted and actual values.
  - term: MAPE
    definition: Mean Absolute Percentage Error; relative error measure expressed as percentage.
  - term: RMSE
    definition: Root Mean Square Error; square root of average squared differences, penalizing larger errors.
  - term: Friedman test
    definition: Non-parametric statistical test comparing multiple models across datasets using rank-based analysis.
critical_citations:
  - "[Demšar, 2006] — Standard reference for statistical comparisons of classifiers."
  - "[Chung et al., 2014] — Empirical evaluation of GRU architecture and parameter efficiency."
  - "[Hochreiter & Schmidhuber, 1997] — Original LSTM paper establishing the architecture."
  - "[Le et al., 2024] — Prior use of Monte Carlo evaluation for neural network benchmarking."
  - "[Shewalkar et al., 2019] — Comparative analysis of RNN, LSTM, and GRU for speech recognition."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly benchmarks forecasting architectures applicable to spending prediction.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Evaluates RNN, LSTM, GRU, and hybrids specifically for time series forecasting.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Provides methodology for evaluating time series prediction stability that could extend to anomaly detection.
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: medium
      justification: Monte Carlo evaluation addresses model stability concerns relevant to cold-start scenarios.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Demonstrates systematic benchmarking methodology with multiple metrics and statistical testing.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides rigorous comparative evaluation of different neural network architectures.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Monte Carlo and Friedman test methodology applicable to budget recommendation evaluation.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: Uses LSTM and RNN architectures that could be adapted for behavioral classification.
  contribution: This paper provides a validated benchmarking methodology for evaluating time series forecasting architectures that can directly inform Odin's spending forecasting module selection. The Monte Carlo evaluation framework offers a reliable approach to assess model stability, which is critical for financial prediction systems where prediction consistency is as important as accuracy. The comparative analysis shows that while statistical differences may be non-significant, LSTM-based hybrids offer practical advantages in stability across diverse data patterns, guiding Odin's architectural decisions for its predictive engine. The study's methodology for handling performance variance due to random initialization provides a template for Odin's model evaluation pipeline.
  directly_justifies:
    - Odin's forecasting module should evaluate models using Monte Carlo simulation across multiple runs to assess stability.
    - LSTM-based hybrid architectures offer practical advantages for spending prediction despite statistical equivalence.
    - The Friedman test provides an appropriate statistical framework for comparing forecasting architectures.
    - Vanilla RNN architectures are less reliable for time series forecasting in financial applications.
    - Hybrid LSTM-RNN and LSTM-GRU configurations provide optimal balance of accuracy and efficiency.
  limits:
    - The study uses only three datasets, limiting the generalizability of findings to spending data specifically.
    - The COVID-19 and oxygen datasets are non-financial, reducing direct applicability to personal finance forecasting.
    - Models were evaluated only on univariate time series, whereas financial data often includes multiple features.
    - The study did not investigate optimal hyperparameter tuning for each architecture individually. [unacknowledged]
    - The computational constraints of the hybrid models in mobile-first applications were not explored. [unacknowledged]
    - Only two hidden layers were used for all architectures, potentially limiting performance of deeper models.
  mapping_rationale: The systematic scan across all 12 functional domains identified high relevance primarily in Predictive Modeling (6.A, 6.B) and System Evaluation (12.A, 12.B, 12.C) because the paper directly benchmarks forecasting architectures and provides rigorous evaluation methodology. Medium relevance was assigned to Anomaly Detection (8.B, 8.C) due to the shared methodological concerns of temporal pattern prediction and cold-start stability. Low relevance was assigned to Behavioral Profiling (5.C) as the architectures could be adapted for classification tasks. Domains concerning Filipino cultural context (2.A-D), expense categorization (3.A-C), existing systems (4.A-B), budgeting strategies (7.A-D), mobile design (9.A-B), data privacy (10.A-B), user retention (11.A-B), and savings/debt management (13.A-C) were rejected because the paper focuses solely on algorithmic performance without addressing financial context, user behavior, or practical financial management applications. The overall relevance is medium: the paper provides valuable methodological guidance for evaluating forecasting models but lacks direct application to Filipino young professional spending or financial management tasks. Borderline cases included the applicability to cold-start scenarios (8.C) due to the stability assessment, and to classification approaches (5.C) due to potential adaptation of the same neural architectures.
limitations:
  - Statistical significance was not achieved due to limited sample size of only three datasets.
  - Findings are based on non-financial datasets (sunspot, COVID-19, oxygen), limiting direct applicability to spending data.
  - Only two hidden layers were used for all architectures based on minimal requirements, not optimized per model.
  - The study did not investigate hyperparameter optimization for each architecture. [unacknowledged]
  - Computational constraints and suitability for mobile-first applications were not evaluated. [unacknowledged]
  - The study focuses only on univariate forecasting, whereas personal finance predictions often require multivariate inputs. [unacknowledged]
remember_this:
  - LSTM-GRU hybrid achieved the best mean rank of 2.23 across all datasets.
  - Monte Carlo simulation across 100 iterations provides reliable model stability assessment.
  - Vanilla RNN showed consistently the highest error rates and most variability.
  - LSTM-RNN hybrid offers the best balance of accuracy and computational efficiency.
  - Statistical equivalence across architectures suggests practical considerations should guide selection.
```
---

## Paper 24: Guban et al_summarized.md

**Source File:** `Guban et al_summarized.md`

```yaml
paper_id: 13523fe0-2a2d-5e2f-9a5c-5b8c9d2e4f3a
designation: local # Published in Technological University of the Philippines - Manila
title: WEKA-BASED DECISION-TREE MODEL FOR USER SUBSCRIPTION PLAN PREDICTION
authors: Guban, J. C. R.; Menderico, C. D. R.; Montalban, D. M. G.
year: 2025
venue: Technological University of the Philippines - Manila
odin_topics:
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 6.A
tldr: A J48 decision-tree model achieves 72% accuracy predicting streaming subscription plans from user demographics and behavioral attributes, identifying country as the strongest predictor.
problem_and_motivation: Streaming platforms lack interpretable models to predict how demographic and behavioral attributes jointly influence subscription plan selection. This limits data-driven personalization and targeted marketing strategies. An accessible, rule-based approach is needed to bridge user behavior with platform optimization.
approach:
  - A supervised classification model using the J48 decision-tree algorithm was developed in WEKA.
  - The dataset comprised 2,500 anonymized user records with six attributes: country, age, gender, device type, subscription start month, and target plan.
  - An 80/20 train-test split was applied to evaluate out-of-sample performance.
  - Performance was assessed using accuracy, Kappa statistic, precision, recall, F-measure, and ROC area.
  - The model was validated against a held-out test set of 500 instances.
findings:
  - num: The model achieved an overall accuracy of 72% on the test set.
  - Country was identified as the most influential predictor of subscription type, followed by age and device type.
  - The decision tree generated interpretable rules showing that younger smartphone users subscribing later in the year often chose Premium plans.
  - Older users on Smart TVs tended toward Standard or Basic tiers.
  - The Standard category achieved the highest precision (0.793) and ROC area (0.871), indicating reliable identification.
  - Confusion matrix showed balanced performance across classes with 123 Basic, 119 Standard, and 118 Premium correct predictions.
key_figures_tables:
  - Table 1: Performance summary on test set → Accuracy 72%, Kappa 0.5797, MAE 0.2216.
  - Table 2: User profile combinations for each country → Country-specific rules reveal distinct segmentation patterns.
  - Table 3: Class-level metrics → Standard has highest precision (0.793) and ROC (0.871); all plans show balanced F-measures.
  - Table 4: Confusion matrix → Diagonal values (123,118,119) show balanced correct classifications across tiers.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: J48
    definition: An open-source Java implementation of the C4.5 decision-tree algorithm in WEKA.
  - term: WEKA
    definition: Waikato Environment for Knowledge Analysis, a suite of machine learning software.
  - term: ROC Area
    definition: Area under the Receiver Operating Characteristic curve, measuring classification discrimination ability.
  - term: Kappa Statistic
    definition: A measure of agreement between predicted and actual classifications, correcting for chance.
  - term: Confusion Matrix
    definition: A table showing correct and incorrect classifications for each class.
critical_citations:
  - "[Aouad et al., 2023] — Validates large decision trees can generalize with proper validation."
  - "[Hsiao, 2023] — Establishes 70% accuracy benchmark for commercial predictive models."
  - "[Garcia & Lee, 2022] — Supports use of decision trees for subscription plan prediction."
  - "[Orozco-Arias, 2020] — Provides rationale for using ROC area as a performance metric."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Demonstrates a classification approach applicable to PFMS user segmentation.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: low
      justification: Recommends incorporating behavioral indicators beyond demographics to improve prediction.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Shows how demographic and behavioral attributes can profile user groups.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Directly applies decision-tree classification to predict user plan choices from profile attributes.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Demonstrates a predictive model for user behavior that can be adapted for spending forecasting.
  contribution: The paper's decision-tree methodology provides a template for Odin's behavioral profiling module, enabling interpretable classification of users based on demographic and behavioral attributes. The feature importance analysis (country, age, device) informs which user attributes are most predictive for segmentation. The validation approach with an 80/20 split and multi-metric evaluation (precision, recall, ROC) offers a framework for Odin's system evaluation module. The interpretable rule extraction supports transparent decision-making for budget recommendation and anomaly detection modules.
  directly_justifies:
    - "Decision trees can predict user plan choices with 72% accuracy from demographic and behavioral attributes."
    - "Country, age, and device type are the most influential predictors of user classification."
    - "Interpretable decision rules reveal how attribute combinations map to specific user segments."
    - "An 80/20 train-test split with multi-metric evaluation provides reliable model validation."
  limits:
    - "Dataset was limited to five user attributes, excluding behavioral indicators like watch time or session frequency."
    - "The model was validated on a single dataset; cross-validation or external validation was not performed."
    - "Ensemble methods were not explored, potentially missing complex nonlinear interactions."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains flagged as relevant were: Existing Systems & Gaps (4.A, 4.B), Behavioral Profiling & Classification (5.A, 5.C), and Spending Forecasting (6.A). Topic 5.C was assigned high relevance because the paper directly applies a decision-tree classifier to predict user plan choices from profile attributes—a technique transferable to financial behavioral profile classification in Odin. Topic 6.A received high relevance as the paper demonstrates a predictive modeling approach for user behavior that can be adapted for spending forecasting. Topic 4.A was deemed contextual, as the paper illustrates a classification approach applicable to PFMS user segmentation. Topic 4.B was low relevance, as limitations were acknowledged but not deeply explored. Topic 5.A was medium relevance, as the paper profiles user groups based on demographic attributes, aligning with behavioral profiling goals. Other domains (e.g., Cultural Context, Mobile-First Design, Data Privacy, User Retention) were considered and rejected because the paper does not address Filipino cultural practices, mobile design considerations, privacy concerns, or engagement dynamics. The paper's overall relevance to Odin lies in its provision of a validated, interpretable classification framework and a feature importance analysis that can inform user segmentation and predictive modeling modules.
limitations:
  - "The dataset was limited to five user attributes, excluding behavioral indicators such as watch time, session frequency, or genre preferences, which may improve prediction accuracy."
  - "The model was validated using a single 80/20 split; k-fold cross-validation was not employed to assess variance in performance [unacknowledged]."
  - "Ensemble methods like Random Forests or Gradient Boosted Trees were not explored, potentially missing complex nonlinear interactions [unacknowledged]."
  - "The model was not tested on a different dataset or in a real-time deployment setting to assess generalizability and operational value."
remember_this:
  - "A decision tree achieved 72% accuracy predicting subscription plans from six user attributes."
  - "Country was the strongest predictor, followed by age and device type."
  - "The model generated interpretable rules linking user profiles to Basic, Standard, or Premium plans."
  - "Standard plan classification performed best with precision of 0.793 and ROC area of 0.871."
  - "Feature importance from decision trees can inform targeted user segmentation in personal finance systems."
```
---

## Paper 25: Gulbakyt et al_summarized.md

**Source File:** `Gulbakyt et al_summarized.md`

```yaml
paper_id: "10.47738/jads.v6i4.935"
designation: "international-algorithm-specific"
title: "Dynamic Model for Budget Allocation in via Multi-Criteria Optimization"
authors: "Gulbakyt, S.; Abdualiyev, A.; Sagnayeva, S.; Yoldash, S."
year: 2025
venue: "Journal of Applied Data Sciences"
odin_topics:
  - "7.C"
  - "7.D"
  - "12.B"
tldr: "A dynamic multi-criteria optimization framework using SQP and GA allocates a constrained regional budget across seven activity areas in Kazakhstan's Almaty region, achieving equitable distribution with a Gini coefficient of 0.223."
problem_and_motivation: "Local executive bodies in Kazakhstan lack transparent, data-driven tools for budget allocation, leading to socioeconomic disparities and declining public trust. Existing approaches fail to balance strategic priorities, citizen preferences, and basic needs while ensuring equitable distribution across districts."
approach:
  - "Formulates budget allocation as a quadratic programming problem with four weighted criteria: citizen satisfaction (0.2), strategic priorities (0.2), basic needs (0.3), and urbanization (0.3)."
  - "Applies Sequential Quadratic Programming (SQP) in MATLAB's fmincon solver, converging within 100 iterations to an objective value of 18,519,864.85 thousand tenge."
  - "Implements a Genetic Algorithm (GA) using Python's DEAP library with population size 200, 500 generations, 80% crossover, and 5% mutation rate."
  - "Uses synthetic citizen voting data derived from demographic statistics and official data from Kazakhstan's Bureau of National Statistics."
  - "Enforces constraints including total budget equality, minimum/maximum bounds per sector, and regional limits."
findings:
  - "num: SQP achieved an objective value of 18,519,864.85 thousand tenge, while GA reached 18,520,000.00, a negligible difference of 135.15 thousand tenge (0.0007% of total budget)."
  - "num: The Gini coefficient of 0.223 indicates equitable distribution across sectors, with a standard deviation of 5.69% and coefficient of variation of 0.398."
  - "num: Healthcare (22.05%) and transport (21.11%) received the largest allocations, while education (7.03%) received the smallest."
  - "All seven activity areas received funding, demonstrating comprehensive sectoral coverage without exclusion."
  - "SQP converged rapidly within 100 iterations, whereas GA required 500 generations to stabilize but offered robustness against local optima."
  - "num: SQP completed optimization with a final feasibility violation of 865,100 tenge (0.47% of budget), indicating a trade-off between strict feasibility and utility maximization."
key_figures_tables:
  - "Figure 1: Conceptual framework of the dynamic budget allocation model → Shows data flow from inputs through optimization to evaluation."
  - "Figure 2: Budget allocation result → Displays balanced distribution across seven sectors and four districts."
  - "Figure 3: Feasible budget allocation region for Healthcare and Transport → Validates optimized allocations lie within constraints."
  - "Figure 4: Optimization process output parameters → Confirms convergence with Func-count 128 and first-order optimality 0.7016."
  - "Figure 5: Convergence of objective function value during SQP optimization → Shows rapid improvement from 16.5 to 18.52 million tenge."
  - "Figure 6: Distribution of budget using GA → Demonstrates similar allocation patterns to SQP across districts."
  - "Table 1: Distributed votes of citizens → Provides synthetic voting data used as input criteria across seven activity areas."
  - "Table 2: Unique strategic priorities → Lists priority multipliers (1.0–2.1) across sectors and four districts."
  - "Table 3: Demographic data and urbanization coefficients → Shows population, income, and urbanization for four Almaty districts."
  - "Table 4: Numerical results (thousands tenge) → Presents the optimized budget allocation values for each district and sector."
  - "Table 5: Comparative analysis of models → Compares level balance, linear programming, and multi-criteria optimization across four criteria."
  - "Table 6: Comparative characteristics of SQP and GA methods → Contrasts method type, objective values, convergence, and constraints."
key_equations:
  - equation: "min(½xᵀQx + cᵀx) subject to A_eq·x = b_eq, A_ineq·x ≤ b_ineq"
    explanation: "Defines quadratic programming problem with equality and inequality constraints."
  - equation: "Objective = α·∑(V_ij/max(V))·B_ij + β·∑(W_ij/max(W))·B_ij + γ·∑1(B_ij ≥ B_min_ij) + δ·∑(U_i/max(U))·B_ij"
    explanation: "Maximizes weighted sum of citizen satisfaction, strategic priorities, basic needs, and urbanization."
  - equation: "A_eq × B_vec = Total budget"
    explanation: "Enforces equality constraint that total allocation equals 42,656,543 thousand tenge."
  - equation: "B_min ≤ B_vec ≤ B_max"
    explanation: "Sets minimum and maximum bounds on budget variables for each sector."
definitions:
  - term: "SQP"
    definition: "Sequential Quadratic Programming, a gradient-based optimization method for constrained nonlinear problems."
  - term: "GA"
    definition: "Genetic Algorithm, a stochastic population-based optimization technique inspired by natural selection."
  - term: "AA"
    definition: "Areas of Activity, the seven sectors receiving budget allocations (education, healthcare, transport, infrastructure, digitalization, culture, ecology)."
  - term: "CU"
    definition: "Urbanization coefficient, the ratio of urban to total population used as a weighted criterion."
  - term: "Maslikhats"
    definition: "Local elected councils in Kazakhstan responsible for regional budget allocation and public fund distribution."
critical_citations:
  - "[Gulbakyt and Abdualiyev, 2024] — Previous linear programming model for budget allocation."
  - "[Mazelis et al., 2021] — Dynamic model for human capital investment distribution."
  - "[Bartocci et al., 2023] — Systematic review of participatory budgeting."
  - "[Schugurensky and Mook, 2024] — Participatory budgeting and local development impacts."
relevance:
  topics:
    - code: "7.C"
      name: "Constrained Optimization Approaches for Budget Allocation"
      relevance: "high"
      justification: "Directly applies SQP and GA to solve constrained multi-criteria budget allocation with equality and inequality constraints."
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "medium"
      justification: "Demonstrates constraint violation handling through penalty-based fitness and minimum/maximum bounds."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Compares SQP and GA performance through objective values, convergence speed, and fairness metrics."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "contextual"
      justification: "Addresses resource allocation optimization but for regional government, not personal finance."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "low"
      justification: "Uses weighted criteria and constraints but does not explore budgeting strategy taxonomies."
  contribution: "This paper's constrained optimization framework informs Odin's budget recommendation module (7.C) by demonstrating how SQP and GA can allocate limited resources across multiple weighted criteria with equality and inequality constraints. The handling of minimum/maximum bounds and penalty-based infeasibility management (7.D) directly applies to Odin's allocation problem with user-defined constraints (3.C). The fairness evaluation using Gini coefficient, standard deviation, and coefficient of variation provides a template for assessing Odin's allocation equity. The comparative analysis of deterministic (SQP) versus stochastic (GA) optimization methods guides algorithm selection for Odin's budget optimization engine. The participatory budgeting simulation using citizen voting data offers a model for incorporating user preferences into allocation decisions."
  directly_justifies:
    - "Multi-criteria optimization can balance multiple objectives including user preferences, needs, and constraints."
    - "SQP provides rapid convergence for well-defined constrained optimization problems."
    - "GA offers robustness for complex problem structures with uncertainty."
    - "Constrained optimization with minimum bounds ensures all categories receive baseline funding."
  limits:
    - "The study uses synthetic citizen voting data rather than real participatory budget records."
    - "The model is designed for regional government budgets, not personal finance allocation."
    - "Weight coefficients lack formal sensitivity analysis or stakeholder validation."
  mapping_rationale: "After systematically scanning all 12 functional domains and their associated topic codes, three domains were flagged as relevant. The Budget Recommendation domain (7.A, 7.B, 7.C, 7.D) is most relevant, with 7.C receiving 'high' relevance because the paper directly applies SQP and GA to solve a constrained multi-criteria budget allocation problem with weighted criteria, equality constraints, and bounds, mirroring Odin's allocation engine. Topic 7.D received 'medium' for its treatment of constraint infeasibility via penalty functions and bounds. Topic 12.B from the System Evaluation domain received 'medium' for the comparative analysis of SQP versus GA using objective values, convergence metrics, and fairness indicators. Topic 7.B was marked 'contextual' as the paper addresses public sector rather than personal finance, but the optimization structure is transferable. Topics 7.A and 4.A were considered and rejected as the paper does not explore budgeting strategy taxonomies or existing PFMS systems. The Filipino Cultural Context and Behavioral Profiling domains were rejected as the paper focuses on Kazakhstan's regional planning with no cultural or behavioral financial analysis. Overall, the paper's optimization framework is structurally relevant to Odin's budget recommendation module despite the different application domain, providing validated techniques for constrained multi-criteria allocation."
limitations:
  - "The paper uses synthetic citizen voting data rather than actual participatory budget records. [unacknowledged]"
  - "Weight coefficients for criteria (0.2, 0.2, 0.3, 0.3) were set via expert judgment without formal sensitivity analysis."
  - "The model remains at conceptual phase with pilot testing pending approval from Kazakhstan's Ministry of Digital Development."
  - "Quantitative comparison with baseline models lacks empirical validation due to unavailable disaggregated budget data."
  - "Constraint violations (0.47% of budget) indicate a trade-off between feasibility and utility maximization that is acknowledged but not fully resolved."
remember_this:
  - "SQP and GA achieved nearly identical objective values with only 0.0007% difference."
  - "Gini coefficient of 0.223 indicates equitable budget distribution across seven sectors."
  - "Healthcare and transport received 22.05% and 21.11% of the total budget respectively."
  - "SQP converged rapidly while GA required 500 generations but offered global search robustness."
  - "All seven activity areas received funding through constrained optimization with minimum bounds."
```
---

## Paper 26: Siddiqui_summarized.md

**Source File:** `Siddiqui_summarized.md`

```yaml
paper_id: 10.71292/sdmi.v2i01.21
designation: international
title: Optimizing Business Decision-Making through AI-Enhanced Business Intelligence Systems: A Systematic Review of Data-Driven Insights in Financial and Strategic Planning
authors: Siddiqui, N. A.
year: 2025
venue: Strategic Data Management and Innovation
odin_topics:
  - 1.A
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 11.A
  - 12.A
  - 13.A
tldr: AI-enhanced BI systems improve forecasting accuracy by 32-45%, reduce fraud by 47%, and enhance supply chain efficiency by 23% but face challenges in data governance and algorithmic transparency.
problem_and_motivation: Traditional BI systems struggle with real-time data processing and unstructured data integration, limiting their ability to generate actionable insights for dynamic business environments. The increasing complexity of financial markets necessitates AI-powered solutions to enhance decision-making accuracy and efficiency.
approach:
  - A systematic literature review was conducted following PRISMA guidelines across Scopus, Web of Science, IEEE Xplore, ScienceDirect, and Google Scholar.
  - From an initial pool of 2,450 articles, 98 high-quality peer-reviewed studies published between 2012-2024 were selected for final analysis.
  - The review focused on AI-driven BI applications in financial forecasting, fraud detection, customer segmentation, and supply chain optimization.
  - Data extraction and thematic analysis were used to categorize findings and identify research gaps.
findings:
  - num: AI-powered BI improves financial forecasting accuracy by 32-45%.
  - num: AI-driven fraud detection reduces fraudulent transactions by 47% and false positives by up to 60%.
  - num: AI-enhanced BI increases customer engagement by 38% and conversion rates by 22%.
  - num: Supply chain optimization with AI-driven BI achieves a 23% increase in operational efficiency and a 17% reduction in logistics costs.
  - num: Organizations using AI for financial risk assessment see a 28% reduction in unexpected financial losses.
  - Data governance complexities and algorithmic bias are cited as major challenges, with 62% of organizations facing data integration issues.
  - The review identifies a research gap in long-term business impact studies of AI-powered BI.
key_figures_tables:
  - Figure 2: Benefits of AI-based Decision Making in Finance → Highlights improvements in forecasting, fraud detection, and risk assessment.
  - Table 1: Identified Gaps from the study → Summarizes key research gaps in financial planning, long-term impact, and cross-industry applications.
  - Figure 8: AI-Driven BI Findings - Stacked Area Chart → Visualizes quantitative improvements across forecasting, fraud detection, and customer engagement.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: BI
    definition: Business Intelligence
  - term: AI
    definition: Artificial Intelligence
  - term: ML
    definition: Machine Learning
  - term: NLP
    definition: Natural Language Processing
  - term: DL
    definition: Deep Learning
  - term: DDDM
    definition: Data-Driven Decision-Making
  - term: DSS
    definition: Decision Support Systems
  - term: PRISMA
    definition: Preferred Reporting Items for Systematic Reviews and Meta-Analyses
critical_citations:
  - "[Duan et al., 2019] — Framework for AI in decision-making."
  - "[Dwivedi et al., 2021] — Multidisciplinary perspective on AI challenges."
  - "[Sarker, 2022] — AI-based modeling techniques for business."
  - "[Cheng et al., 2020] — AI models for real-time forecasting."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: The paper discusses AI-driven BI for young professionals but does not specifically focus on the Filipino demographic.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: The paper extensively covers predictive analytics and forecasting models for financial applications.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Discusses ML and DL algorithms for financial forecasting, including LSTM and Random Forests.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Provides insights into how AI-driven BI supports strategic planning and resource allocation.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: The paper discusses AI's role in budget forecasting and capital allocation.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Reviews AI-driven anomaly detection methods for fraud detection in financial transactions.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Details ML algorithms like SVM and clustering for detecting anomalies in spending data.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Discusses how AI-driven BI enhances customer engagement through personalization.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses a systematic PRISMA framework for evaluating AI-driven BI systems.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: contextual
      justification: Touches on financial planning but does not explicitly address savings goal management.
  contribution: The paper provides a comprehensive systematic review of AI-enhanced BI systems, demonstrating significant improvements in financial forecasting, fraud detection, and customer engagement. It highlights key challenges such as data governance and algorithmic bias, which are critical for Odin's design. The findings justify the need for robust predictive analytics and anomaly detection modules in Odin. The review also underscores the importance of explainable AI and fairness-aware algorithms to ensure user trust and ethical decision-making.
  directly_justifies:
    - "AI-powered BI improves financial forecasting accuracy by 32-45%."
    - "AI-driven fraud detection reduces fraudulent transactions by 47%."
    - "AI-enhanced BI increases customer engagement by 38%."
    - "Data governance and algorithmic bias are major challenges in AI adoption."
  limits:
    - "The review is limited to studies published in English between 2012-2024."
    - "The paper is a systematic review and does not present new experimental data."
    - "The specific applicability of findings to the Filipino context is not addressed. [unacknowledged]"
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. Domains flagged as relevant include Expense Categorization (3), Predictive Modeling (6), Budget Recommendation (7), Anomaly Detection (8), and Engagement (11), as the paper directly discusses AI applications in these areas. Topic codes 6.A, 6.B, 8.A, and 8.B were assigned high relevance due to the paper's extensive coverage of predictive analytics and anomaly detection algorithms. Codes 7.A, 7.B, 11.A, and 12.A were assigned medium relevance for their supporting evidence on strategic planning and evaluation frameworks. Borderline cases such as the paper's discussion of customer segmentation (5.A) and financial behavior (1.C) were considered but not selected as they lack direct applicability to Odin's specific focus on Filipino young professionals. Domains like Cultural Context (2) and Mobile-First Design (9) were rejected due to no relevant content. Overall, the paper provides strong evidence for Odin's predictive and anomaly detection modules.
limitations:
  - "The paper is a systematic review and does not present new experimental data."
  - "The specific applicability of findings to the Filipino context is not addressed. [unacknowledged]"
  - "Potential publication bias is not discussed. [unacknowledged]"
remember_this:
  - "AI-powered BI improves forecasting accuracy by 32-45%."
  - "AI-driven fraud detection reduces fraudulent transactions by 47%."
  - "AI-enhanced BI increases customer engagement by 38%."
  - "Data governance and bias remain major challenges."
  - "The review follows PRISMA guidelines for rigorous analysis."
```
---

## Paper 27: Oktana & Sanjaya_summarized.md

**Source File:** `Oktana & Sanjaya_summarized.md`

```yaml
paper_id: "b8a7f0c3-9e4d-4a2b-9c1e-5f6d8a3b7c2e"
designation: "international-algorithm-specific"
title: "Binary Classification for Predicting the Investment Trends of The Younger Generation Based on Machine Learning"
authors: "Oktana, W. B. J.; Sanjaya, U. P."
year: 2025
venue: "Journal of Applied Informatics and Computing"
odin_topics:
  - "5.A"
  - "5.C"
  - "12.B"
tldr: "Feature-engineered survey data with binary classification predicts investment plans of Indonesian university students, achieving 85.2% accuracy via hybrid ML-business rule integration."
problem_and_motivation: "Traditional demographic segmentation fails to capture complex, non-linear investment behaviors of digitally-native young investors. Machine learning offers a paradigm shift to extract patterns from digital footprints and survey responses. Existing approaches lack interpretability and regulatory compliance for this demographic."
approach:
  - "Dataset of 115 Indonesian university students with nine attributes including demographic, behavioral, and literacy metrics."
  - "Feature engineering creates six composite variables: experience_score, literacy_score, info_seeking_score, capacity_score, risk_preference, and primary_motivation."
  - "Four classification algorithms evaluated: Logistic Regression, Random Forest, SVM, and Gradient Boosting with GridSearchCV 5-fold stratified cross-validation."
  - "Binary classification transformed target from five categories to three and finally to binary will_invest (84 vs 31)."
  - "Hybrid architecture integrates machine learning with business rules via confidence-based thresholding (high-confidence auto, medium human review, low rule-based fallback)."
findings:
  - "num: Logistic Regression achieved 82.6% binary classification accuracy with 0.818 precision and 0.826 recall."
  - "num: Random Forest achieved 69.6% multi-class accuracy with weighted F1-score 0.678."
  - "num: Hybrid ML-business rule model achieved peak accuracy of 85.2%."
  - "num: Binary classification improved performance over multi-class by 13 to 22 percent across all metrics."
  - "Inactive class consistently failed to classify in multi-class due to extreme imbalance with only 6 samples."
  - "Feature importance identified experience_score, literacy_score, and capacity_score as primary predictors."
key_figures_tables:
  - "Figure 2: Multi-class accuracy test comparison → Random Forest and SVM tie at 69.6 percent, Logistic Regression at 65.2 percent."
  - "Figure 3: Binary classification accuracy test comparison → Logistic Regression leads at 82.6 percent, Random Forest and Gradient Boosting at 78.3 percent."
  - "Table 1: Feature engineering conversion methods for six composite variables → domain knowledge transforms categorical responses into quantitative metrics."
  - "Table 2: Comprehensive comparison across multi-class and binary scenarios → binary approach shows superior weighted averages."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "ML"
    definition: "Machine learning, a subset of artificial intelligence enabling systems to learn from data."
  - term: "SVM"
    definition: "Support Vector Machine, a supervised learning algorithm for classification and regression."
  - term: "CRISP-DM"
    definition: "Cross-Industry Standard Process for Data Mining, a methodology for data mining projects."
  - term: "ROC-AUC"
    definition: "Receiver Operating Characteristic - Area Under Curve, a performance metric for binary classifiers."
  - term: "F1-score"
    definition: "Harmonic mean of precision and recall, balancing false positives and false negatives."
critical_citations:
  - "[Hidayatullah, 2025] — Random Forest achieved 89.2% accuracy on IPO classification, establishing precedent for RF in Indonesian finance."
  - "[Majid, 2024] — Bi-LSTM outperforms LSTM for IHSG prediction with 0.572% MAPE, demonstrating deep learning viability for financial forecasting."
  - "[Agung et al., 2025] — LSTM achieved F1-score 0.73 for stock sentiment classification, validating ML for financial text analysis."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Paper classifies investment behavior into Exploring, High_Commitment, and Inactive profiles directly applicable to Odin's behavioral profiling module."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Compares Logistic Regression, Random Forest, SVM, and Gradient Boosting for behavioral classification with explicit performance metrics."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Provides evaluation framework with accuracy, precision, recall, F1-score, and cross-validation for algorithmic module assessment."
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "contextual"
      justification: "Focuses on Indonesian university students, providing demographic parallels but not direct Filipino context."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "low"
      justification: "Mentions limitations of demographic segmentation but does not specifically address PFMS system gaps."
  contribution: "The paper's feature engineering framework can inform Odin's behavioral profiling module by demonstrating how categorical survey responses transform into quantitative behavioral metrics. The hybrid ML-business rule architecture offers a template for Odin's decision support system, balancing algorithmic prediction with interpretable business logic. The comparative evaluation methodology provides a baseline for Odin's system evaluation module when benchmarking alternative classification approaches for financial behavior prediction."
  directly_justifies:
    - "Machine learning classification can predict financial behavior with over 80% accuracy using feature-engineered survey data."
    - "Binary classification outperforms multi-class classification for behavioral prediction in small-sample survey datasets."
    - "Hybrid ML-business rule systems improve accuracy and interpretability over pure ML approaches."
    - "Feature engineering based on domain knowledge significantly enhances predictive power for investment behavior modeling."
  limits:
    - "Small sample size of 115 respondents limits generalizability to broader young professional populations."
    - "Indonesian context and student-specific cohort may not transfer directly to Filipino young professionals."
    - "Binary target simplification may lose nuance in multi-category behavioral profiles."
    - "The paper does not address spending behavior, which is Odin's primary focus."
  mapping_rationale: "All 12 functional domains and their associated topic codes were systematically scanned. The Behavioral Profiling domain was flagged as highly relevant via topics 5.A and 5.C, as the paper directly classifies investment behavior profiles and compares classification algorithms. The System Evaluation domain was flagged as medium via topic 12.B due to the thorough evaluation methodology. The Filipino Cultural Context domain (topics 2.A-2.D) was considered and rejected because the paper focuses on Indonesian students, not Filipino-specific practices; however, topic 1.A was marked contextual for demographic parallels. The Spending Forecasting, Budget Recommendation, Anomaly Detection, Mobile-First Design, Data Privacy, Retention, and Savings/Debt domains were considered and rejected as the paper does not address those topics. The borderline case of topic 4.B (gaps in existing systems) was considered but assigned low relevance because the paper critiques demographic segmentation broadly rather than PFMS-specific limitations. Overall, the paper provides strong methodological contributions for behavioral profiling and algorithm evaluation but limited direct applicability to Odin's spending-centric PFMS."
limitations:
  - "Small sample size (n=115) limits statistical power and generalizability."
  - "Survey-based self-report data may suffer from social desirability and recall biases."
  - "No external validation on held-out or real-world transactional data. [unacknowledged]"
  - "Binary target simplification loses nuance of multi-class behavioral segmentation."
  - "Indonesian student cohort may not represent Filipino young professional demographics."
remember_this:
  - "Logistic Regression achieved 82.6% accuracy for binary investment behavior prediction."
  - "Hybrid ML-business rule integration reached 85.2% accuracy, surpassing isolated approaches."
  - "Feature engineering of experience, literacy, and capacity scores drives predictive performance."
  - "Binary classification substantially outperforms multi-class for small-sample survey data."
  - "Six composite behavioral finance variables transform categorical responses into quantitative predictors."
```
---

## Paper 28: Martinez_summarized.md

**Source File:** `Martinez_summarized.md`

```yaml
paper_id: 10.21203/rs.3.rs-7893661/v1
designation: international-algorithm-specific
title: A Review of Machine Learning and Deep Learning Approaches for Fraud Detection Across Financial and Supply Chain Domains
authors: Martínez, Ó.
year: 2025
venue: Systematic Review (Preprint)
odin_topics:
  - "8.A"
  - "8.B"
  - "5.A"
  - "5.C"
  - "12.A"
  - "12.B"
  - "12.C"
tldr: A systematic review of machine learning and deep learning for fraud detection, evaluating traditional, ensemble, and semi-supervised methods across financial and supply chain domains.
problem_and_motivation: Fraud detection is critical yet challenging due to sophisticated schemes and extreme class imbalance. Traditional rule-based systems are inadequate, and a gap exists in comprehensive reviews bridging financial and supply chain fraud with modern ML/DL techniques.
approach:
  - "Conducted a systematic literature review following PRISMA guidelines."
  - "Searched multiple academic databases for studies published between 2015 and 2025."
  - "Screened 1,847 publications, resulting in a final corpus of 97 high-quality studies."
  - "Categorized methodologies into traditional ML, deep learning, ensemble, semi-supervised, and emerging technologies."
  - "Evaluated approaches based on performance metrics, imbalance handling, interpretability, and computational efficiency."
findings:
  - "num: Ensemble methods and tree-based models consistently achieve superior performance in credit card fraud detection, with AUC-ROC often exceeding 0.95."
  - "num: Semi-supervised approaches, such as two-phase frameworks combining Isolation Forest and self-training SVM, achieve an F1-score of 0.817 with a false positive rate under 3% in supply chain contexts."
  - "Deep learning methods like LSTM excel at capturing temporal dependencies but do not consistently outperform optimized gradient boosting on tabular data."
  - "Extreme class imbalance and concept drift remain fundamental challenges, with Borderline-SMOTE and ensemble methods offering the most effective mitigation."
  - "Explainable AI (XAI) techniques like SHAP and LIME are critical for regulatory compliance and can improve fraud analyst efficiency by 35%."
key_figures_tables:
  - "Table 8: Traditional ML performance → Random Forest offers the best balance for general-purpose fraud detection."
  - "Table 12: Training time comparison on IEEE-CIS scale → LightGBM is fastest among high-performance algorithms."
  - "Table 13: Inference latency per transaction → XGBoost and LightGBM meet sub-100ms real-time requirements."
  - "Table 15: Interpretability requirements by context → Regulatory and customer-facing contexts demand high interpretability."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "ML"
    definition: "Machine learning."
  - term: "DL"
    definition: "Deep learning."
  - term: "AUC-ROC"
    definition: "Area under the receiver operating characteristic curve."
  - term: "AUC-PR"
    definition: "Area under the precision-recall curve."
  - term: "SMOTE"
    definition: "Synthetic minority over-sampling technique."
  - term: "XAI"
    definition: "Explainable artificial intelligence."
  - term: "GNN"
    definition: "Graph neural network."
  - term: "LSTM"
    definition: "Long short-term memory network."
critical_citations:
  - "[Chawla et al., 2002] — Introduces SMOTE for handling class imbalance."
  - "[Chen & Guestrin, 2016] — Proposes XGBoost, a top-performing algorithm."
  - "[Moradi et al., 2025] — Comprehensive study on ensemble methods for fraud detection."
relevance:
  topics:
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Paper reviews anomaly detection as a core fraud detection technique."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Evaluates algorithms like Isolation Forest, Autoencoders, and LOF for anomaly detection."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "contextual"
      justification: "Discusses behavioral features but not in the context of profiling."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "contextual"
      justification: "Reviews classification approaches generally, not specifically for profile building."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides a comprehensive overview of evaluation metrics and protocols."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Compares performance of various algorithmic modules across domains."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "contextual"
      justification: "Focuses on fraud detection, not budget recommendation."
  contribution: "This review informs Odin's anomaly detection module by identifying state-of-the-art algorithms (e.g., Isolation Forest, XGBoost) and best practices for handling class imbalance. It supports the design of Odin's evaluation framework by detailing appropriate metrics (AUC-PR) and validation protocols. The findings justify the use of semi-supervised approaches for Odin in data-scarce scenarios. It provides a foundation for selecting the most effective and computationally efficient algorithms for real-time detection. It also highlights the importance of interpretability, guiding the integration of XAI techniques into Odin's decision-making process."
  directly_justifies:
    - "Ensemble methods like XGBoost and Random Forest are top performers for imbalanced tabular fraud data."
    - "A two-phase framework of unsupervised pre-filtering and semi-supervised refinement is effective with minimal labeled data."
    - "AUC-PR is the preferred metric for evaluating models on extremely imbalanced datasets."
    - "Concept drift necessitates frequent model retraining or online learning strategies."
    - "Explainable AI is essential for regulatory compliance and user trust."
  limits:
    - "The review's primary focus is on credit card and supply chain fraud, with less emphasis on other domains."
    - "Findings are based on public benchmarks, which may not fully represent proprietary industry data patterns."
  mapping_rationale: "The paper was systematically scanned against all 12 functional domains. Domains related to Anomaly Detection (8.A, 8.B) were flagged as high relevance due to the paper's core subject. System Evaluation (12.A, 12.B, 12.C) was assessed as medium relevance because it provides extensive benchmarking and evaluation frameworks. Behavioral Profiling (5.A, 5.C) was considered contextual, as the paper discusses behavioral features and general classification but does not focus on building user profiles for financial management. Domains concerning Filipino cultural context, expense categorization, existing systems, forecasting, budgeting, mobile design, privacy, retention, and savings/debt management were considered and rejected as the paper does not address these specific Odin concerns. The overall relevance is high for informing the technical design of anomaly detection and evaluation components within Odin."
limitations:
  - "Reliance on public benchmarks may limit generalizability to proprietary industry data."
  - "Deep learning for fraud is covered, but practical deployment details are often abstracted away."
  - "The review does not provide a novel algorithmic contribution, only a synthesis of existing work."
remember_this:
  - "Ensemble methods like XGBoost and stacking are the current state-of-the-art."
  - "Semi-supervised learning is highly effective when fraud labels are scarce."
  - "Concept drift requires continuous model adaptation for sustained performance."
  - "Explainable AI is crucial for regulatory compliance and building user trust."
  - "Borderline-SMOTE is a top choice for addressing extreme class imbalance."
```
---

## Paper 29: Vidal-Sarahina_summarized.md

**Source File:** `Vidal-Sarahina_summarized.md`

```yaml
paper_id: 10.69569/jip.2025.483
designation: local
title: Financial Literacy of Department of Education Teachers in the Philippines
authors: Vidal-Sarahina, M.E.
year: 2025
venue: Journal of Interdisciplinary Perspectives
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 5.A
  - 7.A
  - 13.A
tldr: Study reveals gap between financial knowledge and behavior among DepEd teachers due to cultural obligations, low salaries, and behavioral biases, advocating for comprehensive financial education.
problem_and_motivation: Teachers face financial instability despite financial literacy, with external pressures, cultural expectations, and behavioral biases hindering practical application of knowledge. Limited research on DepEd teachers in Guihulngan City exists, requiring a holistic assessment of financial knowledge, attitudes, and behaviors.
approach:
  - Mixed-methods design with quantitative survey of 30 teachers and qualitative interviews with 10 teachers from Guihulngan City Division.
  - Quantitative data used weighted means, standard deviations, and Spearman's rank-order correlation for financial knowledge, attitude, and behavior.
  - Qualitative data analyzed using Braun and Clarke's reflexive thematic analysis to identify factors contributing to knowledge-behavior gap.
  - Lincoln and Guba's trustworthiness criteria applied for rigor in qualitative component.
  - Purposive sampling selected teachers with at least ten years of service in the Department of Education.
findings:
  - num: Mean financial knowledge score was 2.15, indicating moderate understanding.
  - num: Mean financial attitude score was 3.02, showing generally positive outlook.
  - num: Mean financial behavior score was 2.80, reflecting moderately acceptable practices.
  - num: Very weak positive correlation between knowledge and attitude (r = 0.09, p = 0.62).
  - num: No significant correlation between knowledge and behavior (r = 0.01, p = 0.96).
  - num: Weak correlation between attitude and behavior (r = 0.06, p = 0.75).
  - Qualitative analysis revealed themes: Knowledge-Action Gap, Cultural and Familial Expectations, Economic Realities, and Behavioral Biases.
  - Financial behavior is shaped by complex interplay of knowledge, culture, economic pressures, and psychology.
  - Emotional spending and overconfidence contribute to suboptimal financial decisions among teachers.
  - Systemic issues like low salaries and loan dependence constrain financial freedom.
key_figures_tables:
  - Table 1: Respondents' Financial Knowledge, Attitude, and Behavior means and standard deviations → Shows moderate scores with knowledge lowest (2.15) and attitude highest (3.02).
  - Table 2: Correlation between variables → Reveals weak and non-significant relationships among knowledge, attitude, and behavior.
  - Table 3: Thematic analysis themes → Lists Knowledge-Action Gap, Cultural & Familial Expectations, Economic Realities, and Behavioral Biases with categories and descriptions.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Financial Literacy
    definition: Ability to apply financial knowledge, attitudes, and behaviors to achieve financial well-being and resilience.
  - term: DepEd
    definition: Department of Education in the Philippines.
  - term: Knowledge-Action Gap
    definition: Disconnect between possessing financial knowledge and translating it into actual financial behavior.
  - term: Utang na Loob
    definition: Filipino cultural concept of a profound debt of gratitude that influences financial decision-making.
critical_citations:
  - "[OECD/INFE, 2023] — Defines financial literacy as knowledge, attitudes, and behaviors."
  - "[Lusardi & Messy, 2023] — Emphasizes financial literacy for navigating complex systems."
  - "[Casingal & Ancho, 2021] — Highlights financial instability among Filipino teachers."
  - "[Variacion et al., 2024] — Identifies disparity between knowledge and behavior in teachers."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Study focuses on Filipino teachers as a professional demographic with financial challenges.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Examines financial structures like salaries, loan dependence, and budgeting constraints.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly analyzes financial behavior, knowledge, and attitudes of Filipino teachers.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Highlights cultural obligations and utang na loob impacting financial decisions.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: Discusses budget constraints and economic pressures that may relate to cyclical spending.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: medium
      justification: Cultural and familial expectations may influence spending during occasions and obligations.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Identifies behavioral biases like impulsivity and overconfidence affecting financial profiles.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Discusses budgeting as a survival skill and the need for structured savings programs.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Addresses savings challenges and the need for support systems to achieve savings goals.
  contribution: Provides empirical evidence of the knowledge-behavior gap among Filipino teachers, emphasizing cultural and behavioral barriers. This directly informs Odin's user profiling (5.A) by highlighting behavioral biases like overconfidence and impulsivity. The study's cultural insights (2.A) support Odin's need for culturally aware categorization and recommendation systems. Findings on economic constraints (1.B) justify Odin's focus on realistic budgeting and debt management (13.A). The research validates Odin's approach to integrating behavioral finance principles into financial education.
  directly_justifies:
    - "Financial knowledge alone does not predict behavior among Filipino teachers."
    - "Cultural obligations and familial expectations significantly override personal financial goals."
    - "Behavioral biases such as impulsive spending and overconfidence lead to poor financial decisions."
    - "Economic realities like low salaries and loan dependence constrain financial freedom."
    - "Financial education must address socio-economic, cultural, and behavioral barriers."
  limits:
    - "Sample limited to 40 teachers from a single city division, limiting generalizability."
    - "Cross-sectional design cannot capture long-term behavioral changes."
    - "Self-reported data may be subject to social desirability bias."
    - "Focus on teachers may not directly generalize to other Filipino young professionals."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes identified strong relevance to Filipino Cultural Context (2.A, 2.B, 2.D), Financial Structure (1.B), and Behavioral Profiling (5.A). The paper directly addresses financial behavior, knowledge, and attitudes of Filipino teachers, making high relevance for 1.A, 1.B, 1.C, 2.A, and 5.A. Seasonal spending (2.B) and spending cycles (2.D) are touched upon through discussions of economic pressures and cultural obligations, assigned medium relevance. Budgeting strategies (7.A) and savings management (13.A) are relevant through the need for structured programs, assigned medium. Topics like 3.A (Expense Categorization), 3.B (Category Design), 4.A (Existing Systems), 6.A (Forecasting), 8.A (Anomaly Detection), 9.A (Mobile Design), 10.A (Data Privacy), 11.A (Engagement), and 12.A (Evaluation) were considered but rejected as the paper does not directly address algorithmic, system design, or PFMS-specific implementation concerns. The study's primary value to Odin lies in understanding user context, behavioral drivers, and cultural factors affecting financial management.
limitations:
  - "Sample limited to 40 teachers from a single city division, limiting generalizability."
  - "Cross-sectional design cannot capture long-term behavioral changes."
  - "Self-reported data may be subject to social desirability bias."
  - "Focus on teachers may not directly generalize to other Filipino young professionals."
  - "Limited discussion of specific financial products or technologies relevant to PFMS."
remember_this:
  - "Financial knowledge does not translate to behavior for Filipino teachers."
  - "Cultural obligations and family support strongly influence financial decisions."
  - "Behavioral biases like overconfidence and impulsivity hinder sound financial management."
  - "Low salaries and loan dependence create significant economic constraints."
  - "Effective financial programs must address behavioral and systemic barriers."
```
---

## Paper 30: Chahar et al_summarized.md

**Source File:** `Chahar et al_summarized.md`

```yaml
paper_id: 10.2139/ssrn.6377518
designation: international
title: Artificial Intelligence Powered Personal Finance Management System
authors: Chahar, P.; Vishwakarma, Y.; Mishra, R.; Paliwal, G.
year: 2025
venue: International Conference on Innovative Computing and Communication
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 6.A
  - 7.A
  - 7.B
  - 8.A
  - 10.A
  - 11.A
tldr: Proposes an AI-powered personal finance assistant using ML and NLP for dynamic, user-specific financial insights, budget recommendations, and financial education.
problem_and_motivation: Existing personal finance solutions rely on static budgeting and generic advice, lacking adaptability and personalization. Individuals struggle with financial planning due to complex financial systems and limited literacy. This paper aims to address these gaps with an intelligent, adaptive, and educational system.
approach:
  - The system architecture comprises six modules: data collection, expense classification, predictive analytics, recommendation, NLP interface, and security.
  - Expense classification uses supervised ML (Random Forest, SVM, LSTM) on transaction metadata and text descriptions, employing TF-IDF and word embeddings.
  - Predictive analytics applies time series forecasting (ARIMA, LSTM) to predict future expenses and income for proactive planning.
  - A recommendation system provides personalized financial advice and budgeting tips based on user behavior, goals, and predictive insights.
  - The system is implemented with React.js for the frontend, Flask for the backend and ML operations, and MongoDB for data storage.
  - Security is addressed with end-to-end encryption, role-based access control, and anonymization for training data, complying with GDPR.
findings:
  - num: The system achieved a user satisfaction rating of 4.4/5, with high scores for ease of use (4.5/5) and goal-setting functionality (4.3/5).
  - num: Transaction categorization accuracy was rated 4.2/5, though some users noted issues with ambiguous or vendor-specific transactions.
  - The system effectively provides a comprehensive financial overview through automated data aggregation and analysis.
  - Adaptive budgets based on spending habits and income sources were successfully generated using ML techniques.
  - Incorporating educational modules was identified as a key feature for improving financial literacy.
  - The system performed well for users with stable incomes but struggled with irregular income streams and highly variable expenses.
  - Model adaptability was a challenge, particularly for users with fluctuating earnings or atypical spending patterns.
  - Data quality and accessibility were identified as critical factors influencing the accuracy of predictions and recommendations.
  - User trust and adoption remain significant challenges, requiring transparent interfaces and clear explanations of AI decision-making.
  - Regulatory compliance and risk management, including algorithmic bias and model drift, require ongoing attention.
key_figures_tables:
  - "Figure 1: Real-time budget display → Shows a dashboard for current budget tracking."
  - "Figure 2: Jinja2 HTML template for expense data submission and visualization → Displays a user interface for expense input and chart rendering."
  - "Figure 3: SQL view for monthly financial summary → Defines a database view for calculating income, expenses, and savings per user."
  - "Figure 4: Data flow diagram → Illustrates the flow from user data input to the AI engine and back to the UI."
  - "Figure 6: Distribution of expenses across transaction types → Pie chart showing percentage breakdown of spending categories."
  - "Table 1: AI-powered finance management tools → Summarizes features, AI techniques, strengths, and limitations of existing tools like Mint, YNAB, Digit, and Tally."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "PFMS"
    definition: "Personal Finance Management System"
  - term: "NLP"
    definition: "Natural Language Processing"
  - term: "ML"
    definition: "Machine Learning"
  - term: "GDPR"
    definition: "General Data Protection Regulation"
  - term: "ARIMA"
    definition: "Autoregressive Integrated Moving Average"
  - term: "LSTM"
    definition: "Long Short-Term Memory"
  - term: "SVM"
    definition: "Support Vector Machine"
critical_citations:
  - "[Zhang et al., 2007] — Uses decision trees and SVM for classification."
  - "[Siami-Namini et al., 2018] — Compares ARIMA and LSTM for forecasting."
  - "[Luef et al., 2020] — Applies recommendation systems in finance."
  - "[Galperti, 2019] — Provides a theory of personal budgeting."
  - "[Paliwal et al., 2025] — Discusses trust in AI systems."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: "Proposes ML models (RF, SVM, LSTM) for automated expense categorization."
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: "Discusses categorization into meaningful groups like food, transport, utilities."
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: "Reviews existing tools (Mint, YNAB, Digit) and their limitations."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: "Critiques static, rule-based designs and lack of personalization in current systems."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: "Applies ARIMA and LSTM for expense and income forecasting."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: contextual
      justification: "Mentions LSTM for sequential analysis but does not detail the algorithm."
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: "Discusses goal-based and adaptive budgeting strategies."
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: "Generates personalized budget recommendations based on spending behavior."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: "Mentions fraud and anomaly detection but does not specify the approach."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: "Describes encryption, access control, and GDPR compliance for data protection."
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: "Mentions user satisfaction and engagement as key to system success."
  contribution: "This paper provides a high-level blueprint for an AI-powered PFMS, justifying the integration of ML and NLP to address the limitations of static budgeting tools. It directly supports Odin's rationale for using predictive analytics and expense classification as core modules by reviewing relevant techniques and their applications. The paper's discussion of user trust and data security underlines the importance of these non-functional requirements for Odin's design. The systematic literature review and proposed architecture offer a foundation for building Odin's recommendation and classification engines, although it does not provide deep algorithmic details. The evaluation using user satisfaction metrics provides a benchmark for assessing Odin's user-centered design goals."
  directly_justifies:
    - "AI systems can learn from individual spending patterns to provide predictive insights and tailored advice."
    - "Expense classification models using ML are fundamental for budget management and visualizing spending habits."
    - "Predictive analytics enable users to plan budgets proactively and anticipate financial shortfalls."
    - "Recommendation systems enhance engagement by tailoring financial guidance to individual user profiles and goals."
    - "Security and privacy measures like encryption and anonymization are critical for user trust in PFMS."
  limits:
    - "The paper is a proposal and literature review, lacking empirical evaluation of its own AI models."
    - "The proposed system's performance for users with irregular income is acknowledged as a challenge, but not fully resolved."
    - "The paper does not provide a detailed comparison of the proposed system against existing state-of-the-art AI techniques."
    - "The security and privacy measures are mentioned at a high level, without implementation details or validation."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The domains of 'Expense Categorization' (3.A, 3.B), 'Existing Systems & Gaps' (4.A, 4.B), and 'Budget Recommendation' (7.A, 7.B) were flagged as high relevance because the paper directly addresses these with proposed ML solutions and reviews existing tools. 'Spending Forecasting' (6.A) was medium relevance as the paper discusses forecasting methods. 'Data Privacy & User Trust' (10.A) and 'User Retention & Engagement' (11.A) were low/medium relevance, as they are mentioned but not the core focus. Topics like 'Anomaly Detection' (8.A) and 'Forecasting Algorithms for Sequential Spending Data' (6.B) were considered but rejected or given low/contextual relevance due to the paper's lack of algorithmic depth. The paper was also considered for 'Savings & Debt Management' (13.A-C), but it only briefly mentions savings, not in a specific module, so it was rejected. Overall, the paper provides a strong high-level justification for the core modules of an AI-powered PFMS but lacks the technical specificity required for direct implementation of Odin's algorithms."
limitations:
  - "As a proposal paper, it does not present empirical results for its own proposed system, limiting the validation of its claims."
  - "The evaluation is based on a literature review and preliminary prototype feedback, not a fully deployed system."
  - "The paper acknowledges challenges with data quality and adaptability for irregular incomes but does not offer concrete solutions."
  - "The discussion of AI techniques is high-level and lacks the detail necessary for a direct implementation in Odin."
  - "User trust and adoption challenges are identified but the paper does not propose novel methods to address these beyond transparency."
remember_this:
  - "Achieved a 4.4/5 user satisfaction rating for its PFMS prototype."
  - "Uses ML for expense classification and LSTM for spending prediction."
  - "Identifies user trust and data quality as key adoption barriers."
  - "Recommends adaptive budgeting based on income and spending habits."
  - "Emphasizes financial literacy education as a core system feature."
```
---

## Paper 31: Alunen et al_summarized.md

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

## Paper 32: Begum_summarized.md

**Source File:** `Begum_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8_1a2b3c4d5e6f7g8h9i0j
designation: international-algorithm-specific
title: Machine Learning in Financial Risk and Behavior Analysis: Predictive Insights on Bankruptcy, Fraud, and Consumer Trends in the USA
authors: Begum, M.
year: 2025
venue: Journal of Data & Digital Innovation
odin_topics:
  - 4.A
  - 4.B
  - 5.A
  - 6.A
  - 8.A
  - 12.A
tldr: Machine learning models, particularly ensembles and LSTMs, improve bankruptcy prediction, fraud detection, and consumer trend forecasting compared to traditional methods.
problem_and_motivation: Financial systems are increasingly complex, with nonlinear patterns and real-time anomalies that traditional statistical methods struggle to capture. This creates a critical need for intelligent, data-driven approaches to assess and mitigate risks like bankruptcy and fraud. The paper aims to provide predictive insights to enhance decision-making and personalize financial services.
approach:
  - A framework using six models (Logistic Regression, Random Forest, Gradient Boosting, SVM, ANN, LSTM) for bankruptcy prediction.
  - Unsupervised (Isolation Forest) and supervised (Logistic Regression, Random Forest, XGBoost) classifiers, plus ensemble and RNN methods for fraud detection.
  - K-Means and DBSCAN for behavioral segmentation, and ARIMA and LSTM for forecasting financial activities.
  - SMOTE applied to address data imbalance, particularly in fraud detection and bankruptcy prediction.
  - PCA and feature engineering employed to improve model generalization and reduce dimensionality.
  - Models evaluated using Accuracy, Precision, Recall, F1-Score, AUC, and MAE metrics.
findings:
  - num: XGBoost and LightGBM achieved the highest AUC scores (0.93 and 0.91) for bankruptcy prediction.
  - num: The stacking ensemble model for fraud detection achieved the highest F1 score of 0.89.
  - num: LSTM outperformed ARIMA in consumer forecasting, with a lower MAE of 2.8 compared to 4.2.
  - K-Means clustering achieved a silhouette score of 0.68, indicating well-separated customer segments.
  - DBSCAN achieved a lower Davies-Bouldin score of 0.52, reflecting good cluster separation but with parameter sensitivity.
  - GRU-RNN outperformed static models in recall (0.89 vs. 0.81) for fraud detection.
  - Logistic Regression lagged behind other models in bankruptcy prediction with an AUC of 0.76.
  - Isolation Forest suffered from low precision (0.65) due to false positives in fraud detection.
  - ARIMA struggled with volatile sales periods, as shown in residual plots.
  - Debt/Equity ratio and Profit Margin were identified as important non-redundant predictors for bankruptcy.
key_figures_tables:
  - "Figure 10: Bankruptcy AUC comparison and learning curves → Gradient boosting models (XGBoost, LightGBM) achieve highest AUC."
  - "Figure 11: Fraud detection precision-F1 comparison and GRU recall → Stacking ensemble and GRU-RNN show high performance."
  - "Figure 12: ARIMA vs. LSTM error metrics → LSTM significantly outperforms ARIMA in forecasting accuracy."
  - "Figure 13: Silhouette analysis and DBSCAN sensitivity → K-Means shows good cluster separation; DBSCAN performance is parameter-dependent."
  - "Figure 14: K-Means vs. DBSCAN visual comparison → K-Means identifies spherical clusters; DBSCAN finds non-spherical clusters and noise."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: SMOTE
    definition: Synthetic Minority Over-sampling Technique, used to address class imbalance.
  - term: PCA
    definition: Principal Component Analysis, used for dimensionality reduction.
  - term: RNN
    definition: Recurrent Neural Network, used for sequence-based anomaly detection.
  - term: AUC
    definition: Area Under the Curve, a performance metric for classification models.
  - term: MAE
    definition: Mean Absolute Error, a metric for evaluating forecasting accuracy.
critical_citations:
  - "[Sizan et al., 2025] — Foundational for bankruptcy prediction and fraud detection frameworks."
  - "[Al Montaser et al., 2025] — Provides basis for sentiment and behavioral analysis."
  - "[Mohaimin et al., 2025] — Supports churn prediction and customer retention strategies."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Provides a comprehensive review of ML systems for financial risk and behavior analysis.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies gaps like model interpretability, data imbalance, and real-time adaptability in current systems.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Uses clustering (K-Means, DBSCAN) to segment consumers, informing behavioral profiles.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Focuses on predictive modeling for bankruptcy, fraud, and consumer trends, directly applicable to Odin's forecasting modules.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Dedicated section on fraud detection using anomaly detection algorithms like Isolation Forest.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Rigorously evaluates multiple models using metrics like AUC, F1-score, and MAE.
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: The paper's focus on US consumers provides generalizable insights but not specific to Filipino demographics.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: low
      justification: Mentions seasonality in retail sales forecasting but does not deeply analyze cyclical spending.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Notes data privacy as a gap but does not focus on privacy-preserving techniques.
  contribution: "The paper's framework for bankruptcy prediction using gradient-boosting and LSTM models can directly inform Odin's financial health assessment module. Its ensemble approach for fraud detection offers a blueprint for Odin's anomaly detection system. The consumer segmentation and forecasting methods provide a basis for Odin's behavioral profiling and spending forecasting features. The evaluation metrics and validation strategies outlined are directly applicable to Odin's system evaluation protocols."
  directly_justifies:
    - "Gradient boosting models (XGBoost, LightGBM) are effective for bankruptcy prediction from financial ratios."
    - "Stacking ensemble models improve F1 scores in fraud detection by combining classifiers."
    - "LSTM networks outperform ARIMA for forecasting consumer spending with nonlinear trends."
  limits:
    - "Models rely on static, pre-collected datasets, which may not reflect rapidly changing market dynamics."
    - "The study does not integrate real-time data pipelines, limiting responsiveness and accuracy."
    - "Generalizability of models to other sectors or evolving market dynamics is limited."
    - "Ethical concerns and data privacy issues remain unchecked in the AI-based applications."
  mapping_rationale: "A systematic scan of all 12 functional domains was performed. High relevance was assigned to domains directly addressed by the paper's core contributions. The paper strongly aligns with 'Existing Systems & Gaps' (4.A, 4.B) as it reviews and identifies limitations in current ML applications. 'Behavioral Profiling' (5.A) is supported via clustering, and 'Spending Forecasting' (6.A) is a primary focus. 'Anomaly Detection' (8.A) is a dedicated pillar. 'System Evaluation' (12.A) is demonstrated through a comprehensive performance comparison. Borderline cases include 'Seasonal and Cyclical Spending' (2.B), which is mentioned but not a core focus, thus rated 'low.' Similarly, 'Data Privacy' (10.A) is noted as a gap but not a design feature, rated 'low.' Domains like 'Filipino Cultural Context' (2.A) and 'Mobile-First Design' (9.A) were considered but rejected as the paper is US-centric and not focused on mobile UX. The paper provides a broad, high-level overview of ML techniques applicable to multiple Odin modules, making its overall relevance to the project 'high.'"
limitations:
  - "The study does not address the interpretability of complex models like neural networks, which is critical for user trust."
  - "Models are not evaluated for performance on live data streams or their ability to adapt over time. [unacknowledged]"
  - "The findings are based on US data and may not generalize to other cultural or economic contexts, such as the Philippines. [unacknowledged]"
  - "The paper lacks a discussion on the implementation cost or computational resources required for the proposed models."
remember_this:
  - "XGBoost and LightGBM achieve AUC scores above 0.90 for bankruptcy prediction."
  - "Stacking ensemble models significantly improve fraud detection F1 scores."
  - "LSTM networks reduce forecasting error (MAE) by over 30% compared to ARIMA."
  - "K-Means clustering effectively segments customers for targeted strategies."
  - "Data imbalance and model interpretability remain key challenges in practice."
```
---

## Paper 33: Li et al_summarized.md

**Source File:** `Li et al_summarized.md`

```yaml
paper_id: "9a4b5c6d-7e8f-4a3b-9c2d-1e2f3a4b5c6d"
designation: "international-algorithm-specific"
title: "LLM-based Personalized Portfolio Recommender: Integrating Large Language Models and Reinforcement Learning for Intelligent Investment Strategy Optimization"
authors: "Li, B.; Gu, B.; Ding, Z."
year: 2025
venue: "Unknown"
odin_topics:
  - "5.A"
  - "5.C"
  - "7.B"
  - "12.A"
tldr: "Combines large language model-based risk profiling with reinforcement learning optimization to deliver personalized investment portfolio recommendations, achieving higher returns and lower drawdown than baselines."
problem_and_motivation: "Traditional investment models rely on static assumptions and cannot adapt to individual preferences or dynamic markets. Existing AI advisory systems lack personalization and real-time adaptability. There is a need for a framework that integrates natural language understanding with adaptive optimization."
approach:
  - "Constructs a multi-asset portfolio simulation environment using historical market data from 2015 to 2025 covering over 1,200 assets."
  - "Uses a fine-tuned LLM (GPT-4/Llama-3) to extract user risk preferences from multi-turn dialogues and produces a structured risk vector."
  - "Employs Proximal Policy Optimization (PPO) with a composite reward function balancing return, risk, and user alignment to learn personalized allocation policies."
  - "Deploys a conversational investment agent that collects feedback and updates risk profile via a closed human-in-the-loop mechanism."
  - "Evaluates against MVO, DRL-PPO, and BERT-FA baselines using annualized return, Sharpe ratio, maximum drawdown, and user alignment score."
findings:
  - "num: L-PPR achieves 73.8% higher annualized return and 33.2% lower maximum drawdown than MVO."
  - "num: L-PPR records the highest Sharpe Ratio (1.45), Information Ratio (0.78), and User Alignment Score (0.89)."
  - "L-PPR demonstrates superior personalization and conversational satisfaction (0.93) over all baselines."
  - "The loss curve converges around 0.12 after 950 epochs, indicating stable learning."
key_figures_tables:
  - "Table 1: Comparison of portfolio performance and personalization metrics across models → L-PPR outperforms all baselines on every metric."
  - "Figure 2: Training and testing loss curve over epochs → Loss converges to 0.12 after 950 epochs with fluctuations."
key_equations:
  - equation: "$h_t = LLM_\\theta(u_t, h_{t-1})$"
    explanation: "LLM embedding of user dialogue turn."
  - equation: "$\\mathbf{r} = f_{\\text{risk}}(h_t) = \\sigma(W_r h_t + b_r)$"
    explanation: "Maps dialogue embedding to risk vector."
  - equation: "$R_t = \\alpha \\cdot r_t^{\\text{return}} - \\beta \\cdot r_t^{\\text{risk}} + \\eta \\cdot \\text{sim}(\\mathbf{r}, \\mathbf{a}_t)$"
    explanation: "Composite reward balancing return, risk, and user alignment."
  - equation: "$L^{\\text{PPO}}(\\phi) = \\mathbb{E}_t[\\min(r_t(\\phi)\\hat{A}_t, \\text{clip}(r_t(\\phi), 1-\\epsilon, 1+\\epsilon)\\hat{A}_t)]$"
    explanation: "PPO clipped surrogate objective for policy update."
  - equation: "$\\pi_{\\text{conv}}(u_{t+1}|s_t, \\mathbf{a}_t) = \\text{softmax}(W_c[h_t; \\mathbf{a}_t])$"
    explanation: "Conversational policy generating user-facing utterances."
definitions:
  - term: "LLM"
    definition: "Large Language Model, used for natural language understanding and generation."
  - term: "RL"
    definition: "Reinforcement Learning, a machine learning paradigm for sequential decision-making."
  - term: "PPO"
    definition: "Proximal Policy Optimization, a policy gradient algorithm for reinforcement learning."
  - term: "MVO"
    definition: "Mean-Variance Optimization, a classical portfolio optimization method."
  - term: "UAS"
    definition: "User Alignment Score, metric for how well recommendations match user preferences."
  - term: "CSS"
    definition: "Conversational Satisfaction Score, metric for user satisfaction with dialogue."
critical_citations:
  - "[Jiang et al., 2017] — first deep RL for portfolio management."
  - "[Moody & Saffell, 2001] — recurrent RL for trading."
  - "[Wang et al., 2025] — risk-sensitive DRL for portfolio optimization."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "This paper models investor risk preferences via LLM dialogue, directly informing user profiling."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Uses LLM to classify risk tolerance from natural language, applicable to profile classification."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "The RL-based optimization framework is analogous to budget allocation recommendation, though for investments."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Provides comprehensive evaluation metrics (SR, MDD, UAS) that can inform Odin's evaluation."
  contribution: "The L-PPR's user risk profiling module demonstrates how LLMs can extract financial preferences from dialogue, which can be adapted for Odin's user preference elicitation in expense categorization and budgeting. The reinforcement learning optimizer with PPO shows a method for dynamically adjusting allocation constraints, relevant for Odin's budget recommendation under user-defined constraints. The conversational agent provides a model for engaging users and collecting feedback, supporting Odin's retention and engagement design. The evaluation metrics (Sharpe, drawdown, alignment) offer a framework for assessing Odin's algorithmic modules and user satisfaction."
  directly_justifies:
    - "LLM-based dialogue can effectively infer user financial risk preferences from natural language."
    - "Reinforcement learning with PPO can optimize personalized allocation policies under dynamic conditions."
    - "Combining user embeddings with market state improves both financial performance and user satisfaction."
    - "Conversational feedback loops enable continuous adaptation to changing user preferences."
  limits:
    - "The study relies on simulated market environments, not real-world trading, limiting external validity."
    - "The dataset includes simulated investor dialogues, not actual user data, affecting generalizability."
    - "The framework is evaluated on investment portfolios, not directly on personal finance management tasks."
  mapping_rationale: "A systematic scan of all 12 functional domains and associated topic codes identified relevance in behavioral profiling (5.A, 5.C), budget recommendation (7.B), and evaluation (12.A). The paper's focus on LLM-driven risk preference modeling and RL-based optimization directly addresses user profiling and classification, with medium relevance to budget recommendation due to the analogy of allocation optimization. Evaluation frameworks are relevant due to comprehensive metrics. Other domains—Filipino cultural context, expense categorization, existing systems, spending forecasting, anomaly detection, mobile design, data privacy, retention, and savings/debt—were considered and rejected because the paper does not address these PFMS-specific areas. Overall, the paper provides transferable techniques for user preference modeling and adaptive optimization, though its investment context limits direct applicability."
limitations:
  - "Relies on simulated market environments rather than real-world trading data. [unacknowledged]"
  - "Uses synthetic investor dialogues instead of real user interactions, affecting realism. [unacknowledged]"
  - "Does not address privacy or security considerations in personal finance systems. [unacknowledged]"
  - "The paper does not discuss mobile-first design or user retention mechanisms. [unacknowledged]"
remember_this:
  - "Integrating LLM risk profiling with PPO optimization yields 73.8% higher returns than MVO."
  - "L-PPR achieves a Sharpe ratio of 1.45 and user alignment score of 0.89."
  - "Conversational feedback loops enable real-time personalization and user satisfaction."
  - "Personalized policies outperform static or non-personalized approaches in both return and drawdown."
```
---

## Paper 34: Vyas_summarized.md

**Source File:** `Vyas_summarized.md`

```yaml
paper_id: 10.2139/ssrn.5224657
designation: "international"
title: "Revolutionizing Risk: The Role of Artificial Intelligence in Financial Risk Management, Forecasting, and Global Implementation"
authors: "Vyas, A."
year: 2025
venue: "Unknown"
odin_topics:
  - "6.A"
  - "6.B"
  - "8.A"
  - "8.B"
  - "4.A"
  - "4.B"
  - "5.A"
  - "5.B"
  - "7.A"
  - "7.B"
  - "9.A"
  - "9.B"
  - "10.A"
  - "10.B"
  - "11.A"
  - "11.B"
tldr: "AI transforms financial risk management through predictive analytics, anomaly detection, and real-time decision-making, but adoption faces challenges in bias, transparency, and regulatory lag."
problem_and_motivation: "Traditional rule-based risk systems struggle with volatile economic shifts and novel threats. AI offers a solution by processing millions of data points in real-time to flag vulnerabilities. The adoption is uneven globally, with concerns around bias and transparency."
approach:
  - "Hybrid research methodology combining qualitative case study analysis and quantitative data evaluation."
  - "Comparative case studies of JPMorgan Chase and PayPal to evaluate AI-driven risk management outcomes."
  - "Use of Python (Scikit-learn, Pandas) for predictive risk modeling and time-series analysis."
  - "NLP tools (BERT, GPT) for sentiment analysis and financial text interpretation."
  - "ARIMA time-series forecasting to project AI investment growth and fraud loss reduction."
findings:
  - "num: JPMorgan's COIN platform saved over 360,000 work hours annually by automating legal document review."
  - "num: PayPal reduced fraud losses from 0.32% to 0.23% of transaction volume between 2019 and 2023 (28% reduction)."
  - "num: AI-driven fraud detection saved PayPal an estimated $1.4 billion in potential losses in 2022."
  - "num: Over 75% of large financial institutions globally have integrated AI into risk infrastructure."
  - "AI models enable real-time credit scoring and early warning systems for portfolio risk."
key_figures_tables:
  - "Figure 1: Fraud loss percentage trend for PayPal (2019-2023) → AI reduced fraud rates by 28% over four years."
  - "Table 1: Regional AI adoption comparison in financial risk management → North America leads in technological depth; Europe in ethical frameworks."
  - "Figure 2: AI investment growth projection in banking → Over 70% of Tier 1 banks will operate on dynamic AI risk engines by 2027."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "AI"
    definition: "Artificial Intelligence, machine-based systems that replicate human decision-making."
  - term: "ML"
    definition: "Machine Learning, algorithms that improve through experience and data."
  - term: "NLP"
    definition: "Natural Language Processing, AI for understanding and generating human language."
  - term: "FAT Framework"
    definition: "Fairness, Accountability, and Transparency framework for ethical AI."
critical_citations:
  - "[Barocas et al., 2019] — Provides FAT framework for algorithmic fairness."
  - "[Huang et al., 2004] — Found neural networks outperform logistic regression in credit risk."
  - "[Loughran & McDonald, 2011] — Laid foundation for financial sentiment dictionaries."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Extensively discusses predictive analytics and machine learning models for risk forecasting."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Covers time-series forecasting models like ARIMA for financial data."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Directly addresses fraud detection and anomaly detection systems in finance."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "high"
      justification: "Describes neural networks and behavioral analytics for fraud detection."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews existing risk management systems and their limitations."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Identifies gaps in traditional rule-based systems compared to AI."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Discusses behavioral risk scoring and user profiling in fraud detection."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "contextual"
      justification: "Mentions behavioral profiling challenges in new user scenarios."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "contextual"
      justification: "Discusses credit scoring and underwriting, not direct budgeting."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "low"
      justification: "Tangentially related through credit and risk assessment."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "medium"
      justification: "Regional analysis includes mobile banking AI applications."
    - code: "9.B"
      name: "Mobile UX Design for Personal Finance"
      relevance: "medium"
      justification: "References behavioral biometrics and mobile transaction analysis."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "Extensive discussion of data privacy, GDPR, and ethical AI deployment."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "high"
      justification: "Emphasizes trust as a central concern for AI-driven financial systems."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "contextual"
      justification: "Mentions user experience and behavioral engagement in fintech."
    - code: "11.B"
      name: "Retention Mechanisms and Engagement Design"
      relevance: "contextual"
      justification: "Customer satisfaction mentioned in fraud detection context."
  contribution: "The paper provides a comprehensive overview of AI techniques (ML, NLP, neural networks) that can be directly applied to Odin's predictive modeling and anomaly detection modules. It offers empirical evidence (e.g., PayPal's 28% fraud reduction) that justifies investment in similar AI capabilities for spending forecasting and fraud detection in Odin. The discussion of ethical AI, bias, and transparency directly informs Odin's data privacy and user trust design requirements. Regional adoption patterns offer insights for Odin's mobile-first design and localization for the Filipino context. The forecasting models and trend analysis support Odin's long-term system evaluation and feature roadmap planning."
  directly_justifies:
    - "AI-driven fraud detection can significantly reduce financial losses in payment systems."
    - "Real-time risk scoring using behavioral data improves accuracy over static models."
    - "Explainability and bias auditing are essential for regulatory compliance and user trust."
    - "Mobile-based behavioral analytics (e.g., device ID, location) enhance fraud prevention."
  limits:
    - "Data reliance on historical patterns may fail during black swan events or novel crises."
    - "Lack of model interpretability in deep learning systems creates accountability gaps."
    - "Regulatory frameworks for AI are still evolving, creating compliance uncertainty."
  mapping_rationale: "A systematic scan across all 12 functional domains and their 43 associated topic codes was conducted. The following domains were flagged as relevant: Predictive Modeling (6.A, 6.B) and Anomaly Detection (8.A, 8.B) were assigned 'high' relevance due to the paper's focus on forecasting algorithms and fraud detection systems. Existing Systems & Gaps (4.A, 4.B) received 'medium' relevance for reviewing traditional risk management limitations. Behavioral Profiling & Classification (5.A) was 'medium' for discussing user behavior analysis, while 5.B was 'contextual' for brief mentions of cold-start profiling. Data Privacy & User Trust (10.A, 10.B) were 'high' for extensive coverage of GDPR, bias, and accountability. Mobile-First Design (9.A, 9.B) received 'medium' for regional examples of mobile banking AI. Budget Recommendation (7.A, 7.B) and Engagement Dynamics (11.A, 11.B) were deemed 'contextual' or 'low' as they are tangential to the main risk management focus. Topics like Filipino Cultural Context (2.A-D), Expense Categorization (3.A-C), Savings & Debt Management (13.A-C), and Evaluation Frameworks (12.A-C) were considered and rejected for lacking direct evidence or application to Odin's specific modules. Overall, the paper is highly relevant to Odin's AI-driven forecasting, anomaly detection, and privacy/trust modules."
limitations:
  - "Limited access to proprietary model weights and real-time operational data from financial institutions."
  - "Possible regional bias in data availability (U.S. and Europe are more documented than Africa or Latin America)."
  - "Forecasting projections rely on trend extrapolation, which may not fully account for exogenous shocks such as sudden regulation or black-swan events. [unacknowledged]"
remember_this:
  - "AI reduced PayPal's fraud losses by 28% over four years from 2019 to 2023."
  - "JPMorgan's COIN platform automated legal review saving 360,000 work hours annually."
  - "Explainability and bias auditing are critical for regulatory compliance in AI systems."
  - "Regional AI adoption varies, with North America leading in technology and Europe in ethics."
  - "AI models are vulnerable to adversarial attacks and require robust governance frameworks."
```
---

## Paper 35: Bukovski et al_summarized.md

**Source File:** `Bukovski et al_summarized.md`

```yaml
paper_id: "10.17868/strath.00094718"
designation: "international-algorithm-specific"
title: "From Crisis to Prosperity: AI and Open Finance for Holistic Financial Health and Smart Future Planning"
authors: "Bukovski, K.; Jain, K.; Cummins, M.; Bowden, J.; Tetteh, G. K.; Lin, Z."
year: 2025
venue: "Financial Regulation Innovation Lab White Paper Series"
odin_topics:
  - "1.A"
  - "1.B"
  - "1.C"
  - "2.A"
  - "2.B"
  - "3.A"
  - "3.B"
  - "4.A"
  - "4.B"
  - "5.A"
  - "5.B"
  - "5.C"
  - "6.A"
  - "6.B"
  - "7.A"
  - "7.B"
  - "7.C"
  - "7.D"
  - "8.A"
  - "10.A"
tldr: "Open Finance data combined with AI/ML enables holistic financial health evaluation, moving beyond credit scores to support resilience, personalised guidance, and dynamic planning."
problem_and_motivation: "Traditional credit-score systems fail to capture dynamic financial realities, leaving consumers vulnerable to income shocks and unable to plan effectively. A holistic, resilience-focused approach is needed to address the limitations of static, one-dimensional risk models. The regulatory advice gap highlights the urgent need for scalable, personalised financial guidance."
approach:
  - "Proposes a framework integrating Open Finance data (current accounts, mortgages, savings, pensions, insurance) with AI/ML for holistic financial health assessment."
  - "Uses supervised and unsupervised ML, including clustering (K-means, DBSCAN) and predictive models (XGBoost, LSTMs), to segment customers and forecast cash flows."
  - "Employs privacy-preserving techniques like synthetic data generation (GANs, VAEs) and differential privacy to enable development while protecting customer data."
  - "Implements a hierarchical, sequential optimisation engine that prioritises financial stability before wealth accumulation, based on a Maslow-like needs framework."
  - "Integrates explainable AI (SHAP, LIME) to ensure transparency and regulatory compliance, aligning with the FCA's Advice Guidance Boundary Review."
findings:
  - "Open Finance provides a richer dataset than Open Banking, enabling a truly holistic view of financial health across credit, savings, pensions, and insurance products."
  - "Clustering analysis identifies distinct customer personas (e.g., 'Emerging Professionals with Debt', 'Vulnerable and Delinquent Renters'), each requiring tailored guidance strategies."
  - "num: Approximately one quarter of UK adults (12.9 million people) were affected by low financial resilience in 2022."
  - "Predictive models can identify early warning indicators of financial distress, such as increasing credit utilisation and payment delays, enabling proactive intervention."
  - "Integrating behavioural finance principles, like soft goal setting and nudges, can significantly improve savings rates and financial behaviour change."
key_figures_tables:
  - "Figure 1: Consumer support options → Shows the 'targeted support' gap between generic guidance and full advice."
  - "Figure 2: Open Finance as an extension of Open Banking → Illustrates the expanded scope of data from various financial products."
  - "Figure 3: Main pillars of financial health → Visualises the four pillars: Spend, Save, Borrow, Plan."
  - "Figure 6: Wealth & Assets Medians → Highlights significant regional variation in wealth across Great Britain."
  - "Figure 10: Maslow’s theory in financial needs context → Provides the framework for hierarchical financial planning."
key_equations:
  - equation: "Buffer ratio = Liquid Assets / Essential Monthly Outflows"
    explanation: "Measures resilience against unexpected expenses."
  - equation: "Cashflow Volatility = Rolling Standard Deviation of Net Inflows"
    explanation: "Quantifies income and expense variability over time."
definitions:
  - term: "Open Finance"
    definition: "Consent-driven sharing of comprehensive financial data beyond current accounts."
  - term: "Financial Resilience"
    definition: "The capacity to absorb income shocks and maintain essential spending."
  - term: "Targeted Support"
    definition: "Tailored suggestions for groups of consumers with similar circumstances."
  - term: "SHAP"
    definition: "SHapley Additive exPlanations; a method to explain the output of machine learning models."
  - term: "GAN"
    definition: "Generative Adversarial Network; an AI model that generates realistic synthetic data."
  - term: "VAE"
    definition: "Variational Autoencoder; an AI model that learns to generate new data similar to input data."
critical_citations:
  - "[Bukovski et al., 2025] — Defines the consumer-centric financial health evaluation framework."
  - "[FCA, 2025] — Outlines the Advice Guidance Boundary Review and targeted support."
  - "[Sahay et al., 2020] — Explores ML and alternative data for fairer credit access."
  - "[Gu et al., 2020] — Provides foundational work on ML in empirical asset pricing."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "contextual"
      justification: "Framework can be applied to any demographic, but no specific Filipino data."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "low"
      justification: "Addresses general financial structure, not specific to the Philippines."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "low"
      justification: "Behavioural insights are general, not culturally specific to the Philippines."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "contextual"
      justification: "Generic framework, does not address specific Filipino cultural practices."
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "high"
      justification: "Explicitly mentions seasonal spending variations and cashflow volatility."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "high"
      justification: "Proposes hierarchical categorisation of spending, debt, and income."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      relevance: "medium"
      justification: "Discusses designing categories to capture financial health dimensions."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "high"
      justification: "Reviews current PFM landscape, highlighting limitations of credit-score-centric systems."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Critiques traditional models for failing to capture holistic financial health."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Creates distinct customer personas through clustering (e.g., 'Crisis-Prone and Underbanked')."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "medium"
      justification: "Addresses adaptation and continuous learning for changing circumstances."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Uses K-means, DBSCAN, and SOMs for customer segmentation."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Uses ML for dynamic risk assessment and forecasting cash flow."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Recommends LSTMs and Monte Carlo simulations for sequential data."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "high"
      justification: "Uses hierarchical financial needs to guide budgeting strategies."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "high"
      justification: "Framework generates tiered recommendations based on financial health."
    - code: "7.C"
      name: "Constrained Optimization Approaches for Budget Allocation"
      relevance: "high"
      justification: "Optimisation engine handles constraints and prioritises stability."
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "high"
      justification: "Sequential layers address infeasibility by solving higher-priority layers first."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Mentions detecting unusual patterns for fraud and financial distress."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "Dedicated section on privacy-preserving data techniques and ethics."
  contribution: "This paper provides a comprehensive framework for building a PFMS that uses Open Finance and AI. It directly informs Odin's architecture by detailing how to integrate diverse financial data for holistic health scoring. The hierarchical optimisation engine offers a blueprint for Odin's budget recommendation module. The emphasis on explainability and persona-based segmentation aligns with Odin's need for transparent, user-centric design. Furthermore, its discussion of behavioural finance provides a foundation for Odin's engagement and retention strategies."
  directly_justifies:
    - "Open Finance enables a holistic view of financial health beyond traditional credit scoring."
    - "Machine learning can identify distinct customer personas for personalised financial guidance."
    - "A sequential optimisation engine should prioritise cash flow stability before wealth accumulation."
    - "Explainable AI (SHAP) is necessary for transparent and trustworthy financial recommendations."
    - "Behavioural nudges can improve user engagement and savings outcomes."
  limits:
    - "The framework is presented conceptually without a full empirical validation on real-world UK consumer data."
    - "Practical implementation challenges, such as data standardisation across diverse financial products, are acknowledged but not fully resolved."
    - "The paper is a white paper, not a peer-reviewed study; empirical claims rely on cited literature."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was conducted. The paper was found to be highly relevant to multiple domains. High relevance was assigned to 'Spending Forecasting' (6.A, 6.B) due to its dedicated section on predictive modelling and cash flow, and to 'Budget Recommendation' (7.A-D) because of its core contribution: a hierarchical optimisation engine for financial planning. The 'Existing Systems & Gaps' domain (4.A, 4.B) also received high relevance as the paper's primary motivation is to address the limitations of current credit-score systems. 'Behavioral Profiling' (5.A-C) is highly relevant due to the detailed persona construction via clustering. 'Data Privacy' (10.A) was flagged as highly relevant because of the dedicated section on privacy-preserving techniques like synthetic data and differential privacy. Borderline cases included the discussion of seasonal spending, which touches on both 'Seasonal and Cyclical Spending Patterns' (2.B) and general 'Behavioral Profiling' (5.A); the paper was deemed to contribute more directly to the algorithmic detection of such patterns (6.B). Domains like 'Anomaly Detection' (8.A-C) were considered but only given medium relevance as the paper mentions it in the context of fraud detection but does not propose a novel algorithm. The 'Mobile-First Design' (9.A, 9.B) and 'Savings & Debt' (13.A-C) domains were considered but only given contextual or low relevance as the paper focuses on the backend data and algorithmic framework rather than specific UX or savings/debt mechanisms. Overall, the paper is highly relevant to Odin as it provides a conceptual and technical blueprint for an AI-driven, data-centric PFMS."
limitations:
  - "The proposed framework is a high-level architecture; implementation details for specific algorithms are not fully provided."
  - "The paper relies on existing literature for claims about ML efficacy and does not present new empirical results from the proposed system. [unacknowledged]"
  - "Potential biases in the training data for the persona-based clustering are acknowledged but not addressed with a concrete mitigation strategy. [unacknowledged]"
remember_this:
  - "Open Finance enables a holistic view beyond traditional credit scores."
  - "Clustering identifies personas like 'Vulnerable and Delinquent Renters' for tailored guidance."
  - "A hierarchical engine prioritises financial stability before wealth accumulation."
  - "Explainable AI is crucial for transparency and user trust in financial advice."
  - "Behavioural nudges, like goal setting, can effectively increase savings rates."
```
---

## Paper 36: Veldurthi_summarized.md

**Source File:** `Veldurthi_summarized.md`

```yaml
paper_id: 10.32996/jcsts.2025.7.4.88
designation: international
title: The Role of AI and Machine Learning in Fraud Detection for Financial Services
authors: Veldurthi, A. K.
year: 2025
venue: Journal of Computer Science and Technology Studies
odin_topics:
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 5.A
  - 5.C
  - 12.A
  - 12.B
tldr: A comprehensive review of AI/ML fraud detection techniques, spanning from supervised learning to behavioral biometrics and explainable AI, highlighting implementation challenges and future trends.
problem_and_motivation: Financial institutions face escalating fraud risks as digital ecosystems expand, but traditional rule-based systems are inadequate due to their static nature, high false positives, and limited contextual awareness. AI and ML have emerged as transformative technologies that enable real-time, adaptive fraud detection with improved accuracy and efficiency.
approach:
  - This is a survey and review article, not a primary research study. It synthesizes findings from academic literature and industry reports on AI/ML fraud detection.
  - It traces the chronological evolution of fraud detection from manual reviews (1960s) to rule-based, statistical, and current AI/ML systems.
  - It categorizes core ML techniques into supervised (Random Forests, SVMs, Neural Networks), unsupervised (Isolation Forests, Autoencoders), and hybrid/ensemble methods.
  - It details the architectural components of real-time transaction monitoring systems, including data ingestion, feature engineering, and model execution.
  - It discusses Explainable AI (XAI) techniques like LIME and SHAP for regulatory compliance, and analyzes implementation challenges such as data quality, false positives, and adversarial attacks.
findings:
  - num: AI systems can detect 95% of fraudulent transactions compared to 50% for rule-based systems.
  - num: False positives can be reduced by up to 50% with AI systems.
  - Behavioral biometrics like keystroke dynamics and mouse movement analysis can achieve up to 95% accuracy in distinguishing legitimate users from impostors after capturing modest typing behavior.
  - num: Anomaly detection and network analysis can uncover fraud rings involving over 100 accounts per network.
  - num: Risk-based authentication can reduce false positives by up to 60% compared to uniform authentication.
  - num: LSTM models demonstrate particularly strong performance in detecting sequential fraud patterns like credential stuffing.
  - num: Hybrid systems combining rule-based and ML models can reduce implementation costs by up to 40%.
  - num: Effective XAI techniques can reduce regulatory examination time by up to 60%.
  - Machine learning models identify most suspicious cross-border transactions compared to a much smaller percentage for rule-based approaches when evaluated against consistent test datasets.
  - Adversarially trained models detect a much higher percentage of sophisticated evasion attempts compared to conventionally trained alternatives.
key_figures_tables:
  - "Table 1: Evolution of Fraud Detection Systems → AI/ML offers real-time detection and adaptive learning, overcoming limitations of previous eras."
  - "Table 2: Machine Learning Techniques for Fraud Detection → Supervised, unsupervised, and hybrid methods each have distinct strengths for different fraud types."
  - "Table 3: Real-Time Monitoring Components → Data ingestion, feature engineering, and feedback loops are critical for effective fraud detection platforms."
  - "Table 4: Behavioral Biometrics and Device Intelligence → Keystroke dynamics, mouse analysis, and device fingerprinting provide complementary security layers."
  - "Table 5: Future Fraud Detection Trends → Federated learning, reinforcement learning, and cross-industry collaboration are emerging trends."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: AI (Artificial Intelligence)
    definition: Simulation of human intelligence processes by machines, especially computer systems.
  - term: ML (Machine Learning)
    definition: A subset of AI that enables systems to learn and improve from experience without explicit programming.
  - term: XAI (Explainable AI)
    definition: AI systems designed to be transparent and understandable to humans, explaining their decision-making processes.
  - term: LIME (Local Interpretable Model-agnostic Explanations)
    definition: A technique that explains predictions of any classifier in an interpretable and faithful manner.
  - term: SHAP (SHapley Additive exPlanations)
    definition: A method based on game theory to explain the output of any machine learning model.
  - term: RNN (Recurrent Neural Network)
    definition: A class of neural networks designed for sequential data analysis, with connections that form cycles.
  - term: LSTM (Long Short-Term Memory)
    definition: A type of RNN capable of learning long-term dependencies, ideal for processing sequences.
  - term: SVM (Support Vector Machine)
    definition: A supervised learning model that classifies data by finding the optimal hyperplane in a high-dimensional space.
  - term: GDPR (General Data Protection Regulation)
    definition: A regulation in EU law on data protection and privacy in the European Union and the European Economic Area.
  - term: FCRA (Fair Credit Reporting Act)
    definition: A U.S. federal law that promotes accuracy, fairness, and privacy of information in consumer credit reports.
  - term: BSA/AML (Bank Secrecy Act/Anti-Money Laundering)
    definition: A set of laws and regulations requiring financial institutions to assist government agencies in detecting and preventing money laundering.
  - term: API (Application Programming Interface)
    definition: A set of rules and protocols for building and interacting with software applications.
critical_citations:
  - "[Chandola et al., 2010] — Foundational review on anomaly detection for discrete sequences."
  - "[Lopez-Rojas et al., 2016] — Presented PAYSIM simulator for fraud detection."
  - "[Pan, 2024] — Overview of ML in financial transaction fraud detection."
  - "[Bolton & Hand, 2002] — Seminal review on statistical fraud detection methods."
  - "[Yan et al., 2018] — Broad survey on ML and deep learning for cybersecurity."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly reviews anomaly detection techniques (Isolation Forests, Autoencoders).
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Discusses core algorithms like Isolation Forests and Autoencoders for detecting outliers in financial data.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Covers XAI for regulatory compliance and mentions federated learning as a privacy-preserving trend.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Argues that transparent models and reducing false positives are critical for building customer trust.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Discusses behavioral biometrics and profiling to distinguish legitimate users from impostors.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Reviews classification methods like Random Forests and SVMs for identifying behavioral patterns.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: low
      justification: Mentions evaluation metrics like precision, recall, and false positive rates but does not provide a specific framework.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: low
      justification: Discusses model performance comparisons (e.g., Random Forests vs. Neural Networks).
  contribution: This paper provides a comprehensive survey of AI/ML techniques that can be directly applied to Odin's anomaly detection module, specifically in selecting and justifying algorithms for detecting unusual spending patterns. Its discussion of behavioral biometrics and profiling offers a foundation for Odin's user behavioral profiling capabilities. The paper's analysis of XAI and regulatory compliance provides critical insights for building user trust and ensuring transparency in Odin's decision-making.
  directly_justifies:
    - "Random Forests effectively handle the class imbalance inherent in fraud detection."
    - "Isolation Forests are computationally efficient for real-time anomaly detection."
    - "Explainable AI techniques like LIME and SHAP are necessary for regulatory compliance and user trust."
    - "Behavioral biometrics enhance user authentication without increasing friction."
    - "Ensemble methods combine models to maximize detection capabilities."
  limits:
    - "Lack of specific empirical evaluation or case study data for Odin's context."
    - "No discussion of how to implement these systems on mobile-first platforms."
    - "Primarily focused on fraud detection, not on the broader range of personal finance management tasks like budgeting."
  mapping_rationale: A systematic scan across all 12 functional domains was performed. The paper's core contribution on anomaly detection techniques maps directly to domain 8.A and 8.B with high relevance. Its coverage of explainable AI and data privacy aligns with domain 10.A and 10.B (medium). Behavioral profiling discussions relate to domain 5.A and 5.C (medium). While the paper covers evaluation (12.A, 12.B), it is general and offers low direct value for Odin's specific evaluation needs. Domains related to forecasting, budgeting, and mobile design were rejected as the paper contains no relevant claims. Overall, the paper is highly relevant for informing Odin's anomaly detection engine and user trust considerations but provides only foundational or contextual insights for other domains.
limitations:
  - "This is a survey paper, not primary research, offering no novel empirical contributions. [unacknowledged]"
  - "The paper does not address the specific financial behaviors and cultural contexts of Filipino young professionals. [unacknowledged]"
  - "Implementation challenges such as data quality and adversarial attacks are discussed but not quantified for specific contexts."
  - "The focus is on transaction fraud, a different domain than personal spending behavior analysis."
remember_this:
  - "AI systems can detect 95% of fraud vs. 50% for rule-based systems."
  - "Behavioral biometrics provide continuous authentication through typing and mouse patterns."
  - "Explainable AI is critical for regulatory compliance and user trust."
  - "A layered defense strategy reduces fraud losses through multiple detection mechanisms."
  - "Hybrid systems combine rule-based and ML models to reduce implementation costs."
```
---

## Paper 37: Hall & Rasheed_summarized.md

**Source File:** `Hall & Rasheed_summarized.md`

```yaml
paper_id: 10.3390/app15115957
designation: international
title: A Survey of Machine Learning Methods for Time Series Prediction
authors: Hall, T.; Rasheed, K.
year: 2025
venue: Applied Sciences
odin_topics:
  - 6.A
  - 6.B
  - 12.A
  - 12.B
  - 5.C
  - 7.D
  - 8.B
  - 9.A
  - 5.A
  - 10.A
tldr: Tree-based and recurrent neural network models show comparable predictive performance, with tree-based methods offering significant computational efficiency advantages.
problem_and_motivation: Existing literature reviews on time series prediction fail to draw meaningful comparisons between models due to heterogeneous experimental setups. This prevents robust conclusions about the relative strengths of tree-based and deep learning approaches.
approach:
  - A systematic review was conducted on 79 papers published between 2017 and 2024 from Web of Science.
  - Inclusion required studies comparing at least one tree-based and one deep learning model on identical datasets.
  - Models were evaluated using a First Place Aggregation (FPA) score and a Weighted Rank Aggregation (WRA) score.
  - Analysis investigated performance variations based on task category, dataset size, time interval, and research focus.
  - Training time and hyperparameter optimization techniques were also examined for the reviewed models.
findings:
  - Tree-based models outperform deep learning models in 54.55% of tasks, achieving a WRA score of 0.6910.
  - Recurrent neural networks are the strongest deep learning models, while SPTB (XGBoost, LightGBM, CatBoost) models lead for tree-based methods.
  - num: Tree-based models are on average 126,934.94% faster to train than deep learning models, with a median speed advantage of 5603.43%.
  - num: In the largest dataset range (206,573–11,275,200 samples), SPTB models outperform RNNs with a WRA advantage of 0.3833.
  - num: In the M5 Accuracy Competition, 4 of the top 5 submissions relied on LightGBM models.
  - LightGBM and CatBoost emerge as top performers, but the limited representation of CatBoost calls for further validation.
  - Research focus introduces bias, with papers favoring deep learning or tree-based methods showing inflated performance for their preferred model class.
  - Bayesian Optimization and OPTUNA are computationally efficient alternatives to the frequently used but expensive Grid Search.
key_figures_tables:
  - Figure 3: FPA and WRA scores comparing TBML and DL classes → TBML has a slight edge over DL overall.
  - Figure 5: FPA scores for each model → CatBoost, Transformers, LSTMs, and LightGBM are top performers.
  - Figure 6: WRA scores for each model → CatBoost and LSTM show strong and consistent performance.
  - Table 3: Best-performing models by dataset size, task, time interval, and efficiency → Practical guide for model selection.
  - Table 2: Training time advantage of TBML models → TBML can be orders of magnitude faster than DL.
key_equations:
  - equation: FPA = (N_first / N_total) * 100
    explanation: Percentage of comparisons where a model ranks first.
  - equation: WRA = 1 - (N_rank - 1) / (N_total - 1)
    explanation: Normalized score based on a model's rank in each comparison.
definitions:
  - term: TBML
    definition: Tree-Based Machine Learning, including Random Forests and GBDT.
  - term: DL
    definition: Deep Learning, using neural networks with multiple layers.
  - term: SPTB
    definition: Specialized Tree-Based models like XGBoost, LightGBM, and CatBoost.
  - term: RNN
    definition: Recurrent Neural Network, designed for sequential data.
  - term: LSTM
    definition: Long Short-Term Memory, a popular RNN variant with memory gates.
  - term: FPA
    definition: First Place Aggregation, the frequency a model is the top performer.
  - term: WRA
    definition: Weighted Rank Aggregation, a normalized score based on average rank.
  - term: ARIMA
    definition: Autoregressive Integrated Moving Average, a traditional statistical model.
critical_citations:
  - "[Chen, 2016] — Introduced XGBoost as a scalable tree boosting system."
  - "[Ke, 2017] — Developed LightGBM, known for its computational efficiency."
  - "[Prokhorenkova, 2018] — Created CatBoost for handling categorical data effectively."
  - "[Sherstinsky, 2020] — Fundamental overview of RNN and LSTM networks."
  - "[Vaswani, 2017] — Introduced the Transformer model with a self-attention mechanism."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: This paper is a comprehensive survey of predictive ML models directly relevant to Odin's core forecasting functions.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: It provides a detailed evaluation of LSTM, GRU, XGBoost, and LightGBM, which are prime candidates for spending forecasting.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: The paper extensively analyzes error metrics (RMSE, MAE, MAPE, etc.) and proposes a methodology for comparing model performance.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: The survey's systematic comparison of TBML vs. DL models provides a framework for evaluating Odin's individual algorithms.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: While not about user profiles, the review of classification models and metrics can inform behavioral profile classification.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: contextual
      justification: The paper's discussion of hybrid models provides context for more robust, ensemble-based systems, but does not address infeasibility.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: contextual
      justification: The survey includes models and metrics applicable to anomaly detection, such as classification techniques.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: contextual
      justification: The paper's findings on computational efficiency (training time) are critical for mobile-first deployment, but does not discuss UX.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: low
      justification: The paper is a methodological survey, not a study of user behavior, making its relevance to profiling only indirect.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: The paper does not address privacy or security. It mentions data quality but not the sensitivity of personal data.
  contribution: The paper provides a high-level comparison of tree-based and deep learning models for time series prediction, establishing a broad performance baseline for Odin's forecasting module. Its detailed analysis of model performance across task types, dataset sizes, and computational costs directly informs the selection of algorithms for spending forecasting and anomaly detection. The extensive review of error metrics and evaluation methodologies provides a standard framework against which Odin's system evaluation can be validated. The findings on hybrid models and the importance of ensemble methods suggest a robust architectural direction for improving the system's predictive reliability. The paper's explicit identification of LightGBM and LSTM as top performers provides strong justification for prioritizing these algorithms in the system's development roadmap.
  directly_justifies:
    - "LightGBM and LSTM are among the best-performing models for time series forecasting."
    - "Tree-based models offer a significant computational advantage over deep learning models."
    - "The choice of data and feature engineering is as critical as the choice of the forecasting model."
    - "Hybrid models, particularly those combining SPTB and RNNs, often yield superior predictive performance."
    - "Bayesian Optimization and OPTUNA are efficient alternatives to Grid Search for hyperparameter tuning."
  limits:
    - "The survey covers papers only up to 2024, limiting insight into the latest state-of-the-art transformer models."
    - "The analysis groups diverse model variants (e.g., all RNNs), which may obscure specific advantages of models like Bi-LSTM."
    - "The findings on domain-specific performance are based on a small number of samples for some task categories, limiting their generalizability."
    - "The paper's analysis of research bias highlights potential methodological flaws in comparative model studies, which should be considered when evaluating the source literature."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated canonical topic codes was performed. The domains of `Spending Forecasting`, `System Evaluation`, and `Behavioral Profiling & Classification` were flagged as highly relevant. Within `Spending Forecasting`, topic codes 6.A and 6.B were assigned a `high` relevance because the paper is a direct survey of predictive models for sequential data. For `System Evaluation`, codes 12.A and 12.B were rated `high` as the paper's methodology for evaluating and comparing algorithms provides a practical framework for Odin's testing. Code 5.C was rated `medium` because the survey covers classification approaches that could be adapted for user profiling. Topic codes 7.D (Infeasibility Handling), 8.B (Anomaly Detection), and 9.A (Mobile-First Design) were rated `contextual`; the paper discusses model ensembles and anomaly detection methods but does not directly address Odin's specific challenges in these areas. Codes 5.A and 10.A were considered and rejected due to the paper's exclusive focus on computational methods rather than user behavior or privacy. The survey's overall relevance to Odin is high as it serves as a foundational guide for selecting and evaluating the core forecasting and classification algorithms.
limitations:
  - "The survey's classification of model categories (e.g., grouping all RNNs) may obscure the nuanced performance of specific architectures like Bi-LSTM or GRU."
  - "The analysis of temporal resolution did not reveal clear trends, suggesting that time interval may be less important than domain-specific data characteristics."
  - "The findings on bias based on research focus reveal a potential weakness in the methodology of the surveyed papers themselves."
remember_this:
  - "LightGBM and LSTM are top-performing models for time series prediction."
  - "Tree-based models are orders of magnitude faster to train than deep learning models."
  - "Model combination and ensemble methods consistently improve predictive performance."
  - "Data quality and feature engineering can be more important than the choice of the model."
  - "Research focus bias can significantly affect reported comparative model performance."
```
---

## Paper 38: Garcia_summarized.md

**Source File:** `Garcia_summarized.md`

```yaml
paper_id: 10.69569/jip.2025.324
designation: local
title: Financial Literacy and Financial Health of Public Junior High School Teachers
authors: Garcia, E.
year: 2025
venue: Journal of Interdisciplinary Perspectives
odin_topics:
  - 1.B
  - 1.C
  - 2.A
  - 4.B
  - 10.A
  - 10.B
  - 13.A
  - 13.B
tldr: Public junior high school teachers demonstrate high financial literacy but remain financially coping, with notable gaps in emergency savings, debt management, and retirement planning.
problem_and_motivation: Public school teachers in the Philippines face financial insecurity due to low wages and rising costs, yet localized research on their financial literacy and health is scarce. This study addresses that gap to inform targeted financial training programs for educators.
approach:
  - A descriptive-quantitative research design was used.
  - Data were collected from 241 randomly selected teachers in District VI, Quezon City.
  - Validated questionnaires measured financial literacy and health across multiple dimensions.
  - Non-parametric tests (Mann-Whitney U, Kruskal-Wallis H) were used to compare groups.
  - Demographic factors were analyzed for their influence on financial outcomes.
findings:
  - num: Overall financial literacy mean score was 4.02 (High), with retirement planning scoring lowest at 3.75.
  - num: Overall financial health mean score was 61.2, categorizing teachers as "Financially Coping."
  - num: Spending scored highest in financial health at 63.17, while saving scored lowest at 51.87.
  - num: Only 38.07% of respondents expressed confidence in their savings being sufficient for the future.
  - Significant differences in financial literacy were found based on sex, age, number of children, income, education, position, experience, and specialization.
  - Significant differences in financial health were observed for sex, age, civil status, number of children, education, position, experience, and specialization.
  - Teachers demonstrated strong budgeting practices but weaker engagement with tax and estate planning.
key_figures_tables:
  - "Table 1: Financial knowledge scores → Knowledge of borrowing costs (4.02) was lower than general awareness (4.49)."
  - "Table 10: Spending health scores → Bill payment (86.41) was healthy, but month-end surplus (39.00) was vulnerable."
  - "Table 13: Planning health scores → Insurance confidence (57.14) was lower than overall planning engagement (63.94)."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Financially Coping
    definition: Able to meet basic needs but lacks surplus for savings or investments.
  - term: Financial Literacy
    definition: Ability to make informed decisions about budgeting, saving, investing, and planning.
critical_citations:
  - "[Lusardi & Mitchell, 2011] — Links education and experience to financial literacy."
  - "[Villagonzalo & Mibato, 2020] — Found good financial management but poor attitudes in teachers."
  - "[Burgonio, 2023] — Reported low take-home pay for entry-level teachers."
relevance:
  topics:
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Provides income and debt profiles of teachers, a key PFMS target.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly measures financial behavior, attitudes, and health of teachers.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Examines financial practices within a Filipino public-sector context.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies training gaps and the need for targeted financial programs.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Discusses ethical data handling but does not address PFMS-specific privacy.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: contextual
      justification: Mentions ethical compliance but lacks focus on trust-building mechanisms.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: Directly reports savings challenges, including emergency fund deficits.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: Details borrowing patterns and debt-to-income ratios of teachers.
  contribution: This paper informs Odin's savings and debt management modules by providing empirical baseline data on the financial behaviors and challenges of Filipino public school teachers. The findings on savings deficits justify the need for automatic savings features and goal-setting tools. The detailed borrowing and debt repayment data support the design of debt management and reduction features. The study also validates the importance of demographic-aware profiling, as significant differences were observed across various groups.
  directly_justifies:
    - "Teachers allocate a large portion of income to debt repayment (78.44 mean score), indicating need for debt management tools."
    - "Only 39.00 mean score for month-end surplus highlights the need for surplus allocation features."
    - "Savings concerns (38.07 mean score) justify automated savings and emergency fund features."
    - "Significant demographic differences justify personalized behavioral profiling in Odin."
  limits:
    - "Sample is limited to public junior high school teachers in one district of Quezon City, limiting generalizability."
    - "Self-reported data may be subject to social desirability bias."
    - "Cross-sectional design does not allow for causal inferences."
    - "Does not evaluate specific PFMS features or digital financial tools."
  mapping_rationale: A systematic scan of all 12 functional domains identified primary relevance to Financial Structure (1.B), Financial Behavior (1.C), Savings & Debt Management (13.A, 13.B), and Existing Systems Gaps (4.B). The paper's focus on financial literacy and health directly aligns with 1.B and 1.C (high relevance), providing concrete numerical data on teacher income, spending, and savings. Culturally Specific Practices (2.A) is medium relevance as it examines Filipino public-sector financial behavior but does not address unique cultural practices like "utang" or "paluwagan." Data Privacy (10.A) and User Trust (10.B) are contextual, as the study discusses ethical compliance but not PFMS-specific privacy features. Domains like Anomaly Detection, Forecasting, and Mobile Design were rejected as the paper does not discuss computational methods or digital interfaces. The overall relevance is high for foundational financial behavior data, moderate for contextual cultural insights, and low for algorithmic or system design.
limitations:
  - "Self-reported measures may introduce bias."
  - "Cross-sectional design limits causal interpretations."
  - "Sample restricted to one district, limiting generalizability."
  - "Does not evaluate digital PFMS or algorithmic approaches."
remember_this:
  - "Teachers scored high on financial literacy (4.02) but were only financially coping (61.2)."
  - "Only 39.00 mean score for month-end surplus indicates severe savings constraints."
  - "Debt repayment consumes a large portion of teacher income (78.44 mean score)."
  - "Significant demographic differences exist in both financial literacy and health."
  - "Retirement planning (3.75) and emergency fund (3.72) literacy were the lowest areas."
```
---

## Paper 39: Sabiri et al_summarized.md

**Source File:** `Sabiri et al_summarized.md`

```yaml
paper_id: 10.3390/jimaging11010012
designation: international
title: Hybrid Quality-Based Recommender Systems: A Systematic Literature Review
authors: Sabiri, B.; Khtira, A.; El Asri, B.; Rhanoui, M.
year: 2025
venue: Journal of Imaging
odin_topics:
  - 6.A
  - 6.B
  - 7.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
tldr: A systematic review of hybrid recommender systems identifies key hybridization techniques, evaluation metrics, and research gaps, with a significant focus on addressing the cold-start problem and improving recommendation quality through algorithmic combinations.
problem_and_motivation: Recommender systems struggle with issues like information overload, data sparsity, and the cold-start problem, which limit their effectiveness. The motivation is to synthesize recent advances in hybrid approaches that combine multiple recommendation techniques to overcome these limitations and provide more accurate, personalized suggestions. There is a need for a comprehensive review to guide future research and practical implementations in the field.
approach:
  - Conducted a systematic literature review following the Cochrane Handbook and Kitchenham and Charters guidelines.
  - Searched five academic databases (ACM, Google Scholar, Scopus, Springer, Web of Science) using a defined search string.
  - Applied inclusion and exclusion criteria to screen papers, focusing on those published between 2020 and 2024.
  - Employed the ASReview tool, an open-source machine learning application, to assist in the efficient filtering and selection of relevant articles.
  - Performed both quantitative and qualitative analyses of the 52 selected primary studies to categorize challenges, hybridization strategies, datasets, and evaluation methods.
findings:
  - 75% of the reviewed studies on hybrid recommender systems were published within the last three years, indicating growing research interest.
  - num: Hybrid systems demonstrated a precision of 0.80, recall of 0.92, and an F1-score of 0.86, outperforming single-strategy approaches.
  - num: A hybrid approach combining collaborative filtering and sequential pattern analysis achieved the best performance with a CF-based weight of 0.1.
  - num: The study identified a 'watershed moment' in 2020 with the number of papers on the topic jumping to seven, with a subsequent surge to fifteen in 2022.
  - The cold-start problem and data sparsity are identified as the most critical challenges addressed by hybridization techniques.
key_figures_tables:
  - Figure 10: PRISMA flowchart detailing study selection process → Shows 52 articles were finally selected for review.
  - Figure 11: Spread of research based on publication year → Shows a significant increase in publications after 2020.
  - Figure 17: Confusion matrix for articles selected for the study → Summarizes the performance of the selection process with precision, recall, and F1-score.
  - Table A1: Recapitulative table of the selected articles → Provides a comprehensive overview of each study's issue, strategy, dataset, and results.
key_equations:
  - equation: "Evaluation = \\frac{\\sum_{i=1}^{N} q_{w_i} * a_{r_i}}{N}"
    explanation: Formula for calculating a paper's quality score in the systematic review.
definitions:
  - term: Hybrid Recommender System
    definition: A system that combines two or more recommendation techniques to improve accuracy and overcome individual method limitations.
  - term: Collaborative Filtering
    definition: A recommendation method that suggests items based on the preferences of similar users.
  - term: Content-Based Filtering
    definition: A recommendation method that suggests items based on the characteristics of items a user has liked in the past.
  - term: Cold-Start Problem
    definition: The difficulty of making recommendations for new users or items due to a lack of historical data.
  - term: Data Sparsity
    definition: The problem where limited user-item interactions make it difficult to find patterns for accurate recommendations.
critical_citations:
  - "[Kitchenham and Charters, 2007] — Foundational guidelines for conducting systematic literature reviews."
  - "[Higgins et al., 2023] — Provided the Cochrane Handbook standards for systematic reviews."
  - "[Page et al., 2021] — Standardized the reporting of systematic reviews through the PRISMA 2020 statement."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: The paper reviews algorithms like collaborative and content-based filtering, foundational for predictive modeling in PFMS.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: It analyzes forecasting algorithms such as sequential pattern analysis and deep learning models used in hybrid systems for sequential data.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: The review covers hybrid recommendation techniques that can be adapted for personalized budget recommendations.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Discusses evaluation methods and model performance, which are directly relevant to designing evaluation frameworks for anomaly detection modules.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Reviews algorithms that, while for recommender systems, use similar machine learning approaches (e.g., deep learning) applicable to anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a detailed methodology for evaluating recommender systems, directly applicable to evaluating Odin's algorithmic modules.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: The study uses metrics like precision, recall, F1-score, diversity, and novelty, which are key for evaluating individual algorithmic modules in a system like Odin.
  contribution: The paper provides a systematic methodology for evaluating hybrid recommender systems that can be directly applied to Odin's development. The discussion of cold-start and data sparsity challenges is crucial for Odin's early-stage user onboarding and forecasting. The review's categorization of hybridization techniques offers a framework for integrating multiple algorithms in Odin's recommendation and anomaly detection modules. It also identifies evaluation metrics and future research directions that inform the design and validation of Odin's financial planning features.
  directly_justifies:
    - Combining collaborative and content-based filtering can improve recommendation accuracy for new users (cold-start).
    - Hybrid systems generally outperform single-strategy approaches in precision and recall.
    - Metrics like novelty and diversity are critical for improving user engagement and satisfaction.
    - Data sparsity remains a key challenge that requires advanced techniques like matrix factorization to mitigate.
  limits:
    - The review focuses on general recommender systems, not specifically on the domain of personal finance management.
    - The findings are based on studies from 2020-2024, which may not cover the most recent algorithmic developments.
    - The review's scope is limited to English-language, peer-reviewed journal articles, potentially missing relevant gray literature.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated canonical topics was performed. The paper's content on algorithmic combinations, evaluation, and challenges was most relevant to the 'Predictive Modeling' (6.A), 'Forecasting' (6.B), 'Budget Recommendation' (7.B), 'Anomaly Detection' (8.A, 8.B), and 'System Evaluation' (12.A, 12.B) domains, yielding 'high' relevance for these topics due to direct applicability. Topics related to Filipino Cultural Context (2.A-D), Expense Categorization (3.A-C), and Mobile-First Design (9.A-B) were considered but rejected as the paper does not address these domain-specific aspects. The paper's focus on systematic review methodology and quantitative performance metrics makes its contribution most valuable to Odin's algorithmic and evaluation design phases, providing a solid foundation for developing and testing its core modules.
limitations:
  - The quality of the review depends on the completeness of the selected databases and search strategy. [unacknowledged]
  - The manual screening process prior to using ASReview may have introduced selection bias.
  - Publication bias may lead to an overestimation of effects, as top-tier journals tend to publish positive results.
  - The findings on algorithmic performance are derived from various domains (e-commerce, music, etc.) and may not directly generalize to PFMS.
remember_this:
  - Hybrid systems can achieve 92% recall in relevant item retrieval.
  - The cold-start problem is a primary challenge addressed by hybridization.
  - Springer was the source for 40% of reviewed papers on this topic.
  - Evaluation metrics like F1-score are crucial for assessing system performance.
  - Research output on hybrid recommenders surged after 2020.
```
---

## Paper 40: Flores_summarized.md

**Source File:** `Flores_summarized.md`

```yaml
paper_id: 2b8f6e7a-3c4d-4e5f-8a9b-0c1d2e3f4a5b
designation: local
title: Financial freedom of Filipinos in personal finance management
authors: Flores, C. A. R.
year: 2025
venue: Unknown
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.C
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 13.A
  - 13.B
tldr: Filipino financial behaviors are shaped by traditional saving methods, low literacy, and cultural attitudes, leading to poor emergency preparedness and high debt reliance.
problem_and_motivation: Most Filipinos lack financial literacy and do not understand the purpose of key financial instruments for achieving true financial wellness. This leads to poor spending habits, reliance on traditional saving methods, and lack of emergency fund preparedness. The study addresses this gap by examining cash, debt, risk, and wealth management practices among Filipino corporate employees.
approach:
  - Descriptive study using survey questionnaires distributed to 150 respondents from 10 major Philippine corporations.
  - Data collected on demographic profiles, work profiles, and personal finance management practices in four areas.
  - Weighted mean analysis used to assess the degree of financial freedom in each management area.
  - Linear regression analysis performed to determine the significant contribution of each finance variable to overall financial freedom.
  - Respondents included top management, middle management, and rank-and-file staff from companies like SM Prime and Ayala Corporation.
findings:
  - Most respondents were male (57%), married (63%), aged 31-40 (43%), with 1-2 children (57%).
  - Majority held rank-and-file positions (40%) with 11-18 years of work experience (50%) and monthly income of ₱30,000 or above (40%).
  - Respondents agreed on the risks of keeping cash at home (WM=3.73) and the importance of paying high-interest debt first (WM=3.7).
  - Risk management had the highest overall weighted mean (3.65) among finance variables.
  - Linear regression showed that cash, debt, risk, and wealth management do not significantly contribute to financial freedom.
  - Cultural attitudes like the "come-what-may" mindset and reliance on traditional alkansya (bamboo savings) hinder effective financial planning.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: CDRW
    definition: Cash, Debt, Risk, Wealth management – the four areas of personal finance.
  - term: PDIC
    definition: Philippine Deposit Insurance Corporation – insures bank deposits.
  - term: NFIS
    definition: Negative Finding Information System – tracks credit standing.
  - term: GDP
    definition: Gross Domestic Product – total value of goods produced in a country.
critical_citations:
  - "[Lusardi, 2004] — Foundational work on savings and financial education."
  - "[Lusardi & Beeler, 2007] — Examines saving behavior across cohorts and planning."
  - "[Lusardi, Keller, & Keller, 2008] — Social marketing approaches to increase savings."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: The study surveys Filipino corporate employees, a key demographic for Odin.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Details income, work position, and financial practices of this group.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Describes spending, saving, and debt behaviors directly relevant to PFMS.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Identifies traditional alkansya and "come-what-may" attitudes shaping Filipino finance.
    - code: 2.C
      name: User-Declared Financial Preferences
      relevance: medium
      justification: Provides survey-based insights into user attitudes towards cash, debt, and insurance.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Discusses budgeting and allocation, foundational for expense categorization.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: Highlights need for categories like emergency funds and debt payments.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Provides background on financial practices but not on PFMS systems per se.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies gaps in financial literacy and awareness that PFMS could address.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly profiles Filipino financial behaviors (e.g., spending, saving, debt) for behavioral classification.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: contextual
      justification: Discusses behavioral patterns but does not address cold-start profiling.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: Emphasizes emergency fund preparedness and saving habits, core to savings goals.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: Provides specific debt management strategies relevant to Odin's debt modules.
  contribution: "This paper provides empirical evidence on Filipino financial behaviors that informs Odin's user profiling module. It identifies specific cultural practices, like traditional saving and high debt reliance, that Odin must accommodate in its expense categorization and behavioral models. The findings on emergency fund gaps support Odin's savings goal management features. The identified lack of financial literacy highlights the need for Odin's educational nudges and simplified budget recommendations. Overall, the paper justifies a PFMS that is culturally aware and focuses on foundational financial practices."
  directly_justifies:
    - "Filipinos exhibit low emergency fund preparedness, suggesting Odin should prioritize emergency savings goals."
    - "Traditional saving methods like alkansya indicate a need for digital alternatives that build trust."
    - "Debt management strategies like paying highest interest first should be incorporated into Odin's recommendation engine."
    - "Financial literacy gaps in the Philippines justify Odin's educational and simplified budgeting features."
  limits:
    - "The study is limited to 150 respondents from 10 large corporations, not representative of all Filipino young professionals."
    - "The linear regression showed no significant contribution of the four finance variables to financial freedom, suggesting other unmeasured factors are at play."
    - "The study does not evaluate any existing PFMS, only general financial practices."
  mapping_rationale: "The systematic scan across all 12 functional domains identified strong relevance for domains related to Filipino cultural context, expense categorization, behavioral profiling, and savings/debt management. Topics 1.A, 1.B, 1.C, 2.A, 5.A, 13.A, and 13.B were assigned 'high' relevance as the paper directly characterizes the financial structure, culturally specific practices, and behavioral profiles of Filipino employees, while also offering specific strategies for savings and debt management that directly inform Odin's modules. Topics 2.C and 3.A/B were assigned 'medium' as they provide contextual evidence for user preferences and expense categorization. Topic 4.B was 'medium' for identifying gaps in financial literacy and awareness. The domains related to forecasting (6.A/B), budget recommendation algorithms (7.A-D), anomaly detection (8.A-C), mobile-first design (9.A/B), data privacy (10.A/B), retention (11.A/B), and system evaluation (12.A-C) were rejected as the paper does not address these algorithmic or design topics. The paper's focus is on descriptive analysis of current financial practices, not on building or evaluating PFMS systems."
limitations:
  - "Sample limited to 150 employees from 10 large corporations, not representative. [unacknowledged]"
  - "Linear regression showed no significant contribution of the four finance variables to financial freedom. [unacknowledged]"
  - "Study does not account for regional variations in Filipino financial practices."
remember_this:
  - "Low financial literacy and traditional saving habits characterize Filipino young professionals."
  - "Emergency fund preparedness is critically low, with most relying on debt for unexpected expenses."
  - "Paying high-interest debt first is a key strategy for financial freedom."
  - "Risk management had the highest agreement score, indicating awareness of insurance importance."
  - "Cash, debt, risk, and wealth management did not significantly predict financial freedom in this sample."
```
---

## Paper 41: Bongado et al_summarized.md

**Source File:** `Bongado et al_summarized.md`

```yaml
paper_id: 7ad48f82-1c9f-5238-93f8-8878e2720d96
designation: local
title: Influence of Digital Wallets on the Financial Behavior of HEI’s Students
authors: Bongado, M. B. B.; Magallanes, A. R.; Semaña, C. M.
year: 2025
venue: Unknown
odin_topics:
  - 2.A
  - 5.A
  - 9.A
  - 10.A
tldr: Digital wallet usage positively influences financial behavior among Filipino HEI students, explaining 45.4% of variance in financial practices.
problem_and_motivation: The influence of digital wallet usage on financial behavior, particularly cash management and budgeting, remains underexplored among Filipino HEI students despite widespread adoption. Understanding this relationship is critical to determining whether digital financial tools support or hinder responsible financial habits among young Filipinos.
approach:
  - A quantitative descriptive-correlational design was employed with 219 randomly selected students from a Philippine state university.
  - Data were collected using a validated structured questionnaire adapted from Belmonte et al. (2024) measuring determinants of digital wallet adoption and financial behavior.
  - Determinants included perceived ease of use, perceived usefulness, perceived value, social influence, attractiveness of alternatives, perceived trust, perceived security, and intention to use.
  - Financial behavior was assessed through cash management and financial planning and budgeting dimensions using a 4-Point Likert scale.
  - Pearson correlation and regression analysis were used to test the influence of digital wallet usage on financial behavior at a 0.05 significance level.
findings:
  - Students perceived digital wallet determinants positively, with mean scores ranging from 2.91 to 2.99 across all factors.
  - Perceived trust exhibited the highest variability (SD = 1.24), indicating diverse opinions on platform reliability.
  - Financial behavior scores were high (M = 2.99), with strong agreement on responsible cash management and budgeting practices.
  - num: Digital wallet usage significantly predicted financial behavior, accounting for 45.4% of the variance (R² = 0.454, F = 180.136, p < .001).
  - num: The beta coefficient (β = 0.673) indicates a positive relationship between digital wallet usage and improved financial behavior.
  - The regression model confirmed digital wallet usage as a significant predictor of financial behavior among student respondents.
key_figures_tables:
  - Table 1: Determinants of digital wallet usage means and SDs → Students generally agree on all adoption factors, with trust showing most variability.
  - Table 2: Financial behavior determinants means and SDs → Students demonstrate responsible financial practices with moderate consensus on cash management and budgeting.
  - Table 3: Regression analysis results → Digital wallet usage significantly influences financial behavior, explaining 45.4% of variance.
key_equations:
  - equation: "R² = 0.454"
    explanation: "45.4% of financial behavior variance explained by digital wallet usage."
definitions:
  - term: FinTech
    definition: Financial technology that revolutionizes payment systems and financial services through digital innovations.
  - term: Digital Wallet
    definition: A digital substitute for cash and bank accounts allowing users to store, transfer, and pay through mobile devices.
  - term: TAM
    definition: Technology Acceptance Model explaining user adoption based on perceived usefulness and ease of use.
  - term: HEI
    definition: Higher Education Institution offering tertiary education programs.
  - term: PFMS
    definition: Personal Finance Management System for tracking and managing individual finances.
critical_citations:
  - "[Belmonte et al., 2024] — Validated TAM instrument for Filipino e-wallet adoption context."
  - "[Scheresberg et al., 2020] — Found mobile payment users overspend and save less."
  - "[Amanda et al., 2023] — Digital wallets promote impulsive spending among Generation Z."
relevance:
  topics:
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Examines digital wallet adoption and financial behavior specifically among Filipino HEI students.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Assesses financial behavior dimensions including cash management and budgeting practices.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Digital wallets are mobile-first platforms; findings inform design for student financial management.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Perceived trust and security were significant determinants of adoption and usage.
    - code: 2.C
      name: User-Declared Financial Preferences
      relevance: low
      justification: Touchs on financial behavior but does not deeply explore user-declared preferences.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: Mentioned in financial planning and budgeting context but not focused on categorization frameworks.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: References digital wallets as existing systems but does not survey the landscape.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: contextual
      justification: Budgeting is a dimension of financial behavior but no recommendation system is evaluated.
  contribution: This study provides empirical evidence that digital wallet usage positively influences financial behavior among Filipino HEI students, directly informing Odin's user profiling and behavioral classification modules. The validated TAM-based instrument offers a framework for understanding adoption determinants that can be adapted for Odin's onboarding and personalization features. The significant relationship between digital wallet usage and responsible financial practices supports the development of mobile-first financial management tools that promote budgeting and cash management. The findings on perceived trust and security variability highlight the importance of Odin's data privacy and user trust components. The study's focus on Filipino young professionals aligns with Odin's target demographic and validates the need for culturally relevant financial behavior assessment.
  directly_justifies:
    - "Digital wallet usage positively predicts financial behavior among Filipino students."
    - "Perceived ease of use and usefulness are key determinants of financial tool adoption."
    - "Financial behavior includes cash management and budgeting as measurable dimensions."
    - "Trust and security perceptions vary among users and affect adoption rates."
  limits:
    - "Focus on a single university in one municipality limits generalizability to broader Filipino young professional populations."
    - "Cross-sectional design cannot establish causal relationships between digital wallet usage and financial behavior."
    - "Self-reported survey data may be subject to social desirability bias."
    - "Does not control for income level, digital literacy, or parental influence on financial behavior."
    - "Financial behavior assessment limited to cash management and budgeting, excluding savings and debt management."
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains flagged as relevant include: Filipino Cultural Context (2.A, 2.B, 2.C, 2.D) due to the study's focus on Filipino HEI students and their specific financial practices; Behavioral Profiling & Classification (5.A, 5.B, 5.C) as the paper directly assesses financial behavior dimensions; Mobile-First Design (9.A, 9.B) because digital wallets are mobile platforms; and Data Privacy & User Trust (10.A, 10.B) through its examination of perceived trust and security. Topic codes selected with high relevance: 2.A (culturally specific practices), 5.A (financial behavioral profiles). Medium relevance: 9.A (mobile-first principles), 10.A (data privacy). Low relevance: 2.C (user-declared preferences). Contextual relevance: 3.A (expense categorization), 4.A (existing systems landscape), 7.B (budget recommendation). Borderline cases included the paper's coverage of both 2.A and 2.C, resolved by assigning 2.A as the primary code since the focus is on actual practices rather than stated preferences. Domains rejected included Expense Categorization (3.A, 3.B, 3.C) as the paper does not examine categorization frameworks; Existing Systems & Gaps (4.A, 4.B) as it does not survey the PFMS landscape; Spending Forecasting (6.A, 6.B) as no predictive modeling is conducted; Anomaly Detection (8.A, 8.B, 8.C) as no anomaly detection is evaluated; Engagement & Retention (11.A, 11.B) as the study does not examine engagement dynamics; System Evaluation (12.A, 12.B, 12.C) as no system evaluation framework is used; and Savings & Debt Management (13.A, 13.B, 13.C) as these are not assessed. Overall, the paper provides moderate to high relevance for Odin's behavioral profiling and cultural contextualization modules, while offering contextual insights for design and trust considerations.
limitations:
  - "Convenience sampling may limit representativeness of all Filipino HEI students."
  - "Cross-sectional design prevents establishing causality between digital wallet usage and financial behavior."
  - "Self-reported measures may be subject to response bias and overestimation of responsible behavior."
  - "Study limited to one geographic location (Talisayan, Misamis Oriental), reducing generalizability. [unacknowledged]"
  - "No qualitative data to capture deeper motivations and challenges in digital wallet usage. [unacknowledged]"
  - "Does not account for income or parental influence as confounding variables. [unacknowledged]"
remember_this:
  - "Digital wallet usage explains 45.4% of financial behavior variance in Filipino students."
  - "Perceived trust shows the widest variation among adoption determinants."
  - "Students demonstrate responsible cash management and budgeting practices."
  - "Digital wallets serve as enablers of financial discipline beyond transactional tools."
  - "Security and trust perceptions significantly affect digital wallet adoption."
```
---

## Paper 42: Al-E'mari et al_summarized.md

**Source File:** `Al-E'mari et al_summarized.md`

```yaml
paper_id: "e7b7b7b7-7b7b-7b7b-7b7b-7b7b7b7b7b7b"
designation: "international-algorithm-specific"
title: "The Role of Artificial Intelligence in Enhancing Financial Decision-Making and Administrative Efficiency: A Systematic Review"
authors: "Al-E'mari, S.; Sanjalawe, Y.; Al-E'mari, A."
year: 2025
venue: "Al-Basaer Journal of Business Research"
odin_topics:
  - "4.A"
  - "8.A"
  - "8.B"
  - "10.A"
  - "12.A"
tldr: "A systematic review of AI applications in finance and administration, highlighting predictive analytics, machine learning, and RPA for enhanced decision-making, risk management, and operational efficiency."
problem_and_motivation: "Despite growing AI adoption in finance and administration, a comprehensive understanding of its systemic benefits and challenges across both domains remains lacking. Existing research often neglects the ethical, regulatory, and security implications of AI-driven decision-making. This review addresses this gap by providing a holistic analysis of AI's impact."
approach:
  - "Systematic literature review following established guidelines for transparency and replicability."
  - "Searched IEEE Xplore, PubMed, Scopus, Web of Science, and ScienceDirect for relevant studies."
  - "Used Boolean search strings combining terms like 'Financial Decision-Making,' 'AI,' and 'Predictive Analytics.'"
  - "Applied inclusion criteria: peer-reviewed articles from 2014-2024, focusing on AI in finance and administration."
  - "Used a two-reviewer process for screening titles, abstracts, and full texts to minimize bias."
  - "Extracted data on AI application type, process impact, methodology, and key findings."
  - "Employed a structured evaluation framework with KPIs like time savings and cost reductions."
  - "Included real-world case studies from JPMorgan Chase, BlackRock, Ant Financial, and UiPath."
  - "Analyzed performance correlations between AI applications and decision-making speed."
findings:
  - "num: JPMorgan Chase's COiN platform achieved a 99% reduction in manual legal document review time."
  - "num: BlackRock's Aladdin system improved forecasting accuracy by 20% and reduced market reaction time by 30%."
  - "num: Ant Financial's AI fraud detection improved detection rates by 35% compared to rule-based systems."
  - "num: UiPath RPA in healthcare led to an 80% reduction in billing processing times and a 60% increase in operational efficiency."
  - "AI enhances administrative functions through RPA for automating routine tasks and AI-powered tools for data management."
  - "Broad AI use shows a 0.61 correlation with speed and a 0.48 correlation with decision-making."
  - "Predictive analytics is essential for portfolio management and algorithmic trading."
  - "AI enhances risk management and fraud detection by analyzing vast datasets for suspicious patterns."
  - "AI helps with regulatory compliance by automating transaction monitoring and updating protocols."
  - "AI-driven data management reduces manual effort and improves reporting accuracy."
key_figures_tables:
  - "Figure 1: Efficiency gains from AI in data reporting → Shows improvements in time saved, reporting accuracy, and error reduction."
  - "Figure 2: Performance impact of AI on improved decision-making → Correlates AI applications with speed and decision-making benefits."
  - "Figure 3: Comparison of AI case studies → Quantifies time saved and accuracy improvements across case studies."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "RPA"
    definition: "Robotic Process Automation, the use of AI-driven software bots to replicate human actions for routine tasks."
  - term: "NLP"
    definition: "Natural Language Processing, a field of AI that enables computers to understand and process human language."
  - term: "XAI"
    definition: "Explainable Artificial Intelligence, techniques to make AI decisions transparent and understandable to humans."
critical_citations:
  - "[Biloslavo et al., 2024] — Provides context on AI in strategic planning."
  - "[Farayola, 2024] — Discusses AI in banking security."
  - "[Cohen, 2022] — Details algorithmic trading with AI."
  - "[Bao, Hilary & Ke, 2022] — Covers AI and fraud detection."
  - "[Rane, Choudhary & Rane, 2023] — Highlights AI for security in finance."
relevance:
  topics:
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Provides a broad overview of AI applications, not specific PFMS landscape."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "high"
      justification: "Directly addresses fraud detection, a core anomaly detection use case in finance."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "medium"
      justification: "Discusses machine learning for identifying suspicious patterns in financial data."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "Extensively discusses data privacy and security challenges of AI, referencing GDPR."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "Uses KPIs like time savings and accuracy to evaluate AI impact, relevant to system evaluation."
  contribution: "This paper provides a high-level framework for evaluating AI's role in financial decision-making, which can inform the design of Odin's anomaly detection and risk assessment modules. Its discussion of data privacy and security considerations directly supports the development of Odin's user trust and data governance strategies. The quantitative performance metrics from case studies offer benchmarks for evaluating Odin's algorithmic modules. The paper's analysis of AI's impact on administrative efficiency can guide the design of Odin's user-facing features for expense tracking and reporting. Its emphasis on ethical challenges highlights the need for transparent and accountable AI within Odin."
  directly_justifies:
    - "AI-powered systems can detect anomalies and flag suspicious transactions faster than rule-based systems."
    - "Machine learning models can identify patterns in market data and predict risks associated with investments."
    - "RPA can automate routine administrative tasks, reducing manual effort and human error."
    - "Data privacy and security are critical challenges in AI adoption, requiring compliance with regulations like GDPR."
  limits:
    - "The review is broad and not specifically tailored to personal finance management systems for young professionals."
    - "The findings are based on systematic review and may not represent a single, controlled empirical study."
    - "The paper focuses on general AI applications, not specific algorithms for spending data."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains of 'Anomaly Detection' and 'Data Privacy & User Trust' were flagged as highly relevant, as the paper extensively covers fraud detection and data security. 'Existing Systems & Gaps' was marked contextual, as the paper provides a landscape review. 'System Evaluation' was marked medium due to its use of KPIs for evaluating AI impact. The domain of 'Expense Categorization' was rejected as the paper does not discuss expense classification. The domain of 'Behavioral Profiling' was rejected as it does not cover user profiling or cold-start problems. The domain of 'Spending Forecasting' was rejected as it does not discuss forecasting algorithms for spending. The overall relevance is medium; while the paper provides strong support for general AI capabilities and challenges, it lacks specific guidance on PFMS design for Filipino users."
limitations:
  - "Focuses on general AI applications in finance and administration, not specifically on PFMS. [unacknowledged]"
  - "Does not address the cold-start problem or behavioral profiling for new users. [unacknowledged]"
  - "Limited discussion of constrained optimization for budget allocation. [unacknowledged]"
remember_this:
  - "AI in finance improves risk management and fraud detection through pattern recognition."
  - "RPA automates administrative tasks, increasing operational efficiency and reducing errors."
  - "Data privacy and security are critical challenges requiring regulatory compliance."
  - "Broad AI use shows a 0.61 correlation with speed and 0.48 with decision-making."
```
---

## Paper 43: Tiongco & Gangan_summarized.md

**Source File:** `Tiongco & Gangan_summarized.md`

```yaml
paper_id: 8c7b8f4a-2e5d-4c9f-8a3b-1e2d4c6f8a9b
designation: local
title: Moving Beyond the Php500 Noche Buena Illusion
authors: Tiongco, M. M.; Gañgan, F. Y. D.
year: 2025
venue: DLSU-Angelo King Institute Policy Brief
odin_topics:
  - 2.A
  - 2.B
  - 2.D
  - 3.C
  - 4.B
  - 5.A
  - 13.A
tldr: Inflation and shrinkflation have eroded the purchasing power of the Php500 Noche Buena basket, which now costs Php643–670, placing an undue burden on low-income Filipino households.
problem_and_motivation: The persistent promotion of a Php500 holiday basket obscures the real cost of food due to inflation and shrinkflation. This misrepresentation undermines the dignity and financial well-being of Filipino families, especially low-income households, by setting unrealistic expectations for holiday spending.
approach:
  - Analyzed PSA Food CPI data from 2018 to 2025 to calculate the real cost of a Php500 basket.
  - Compared the contents of commercial Php500 holiday baskets from 2018 and 2025 to demonstrate shrinkflation and product substitution.
  - Used FIES data to illustrate food expenditure shares across income deciles.
  - Assessed affordability by comparing the basket cost to the daily minimum wage in NCR.
findings:
  - num: A Php500 food basket from 2018 now costs Php669.80 in NCR and Php643.28 outside NCR in November 2025.
  - num: Food inflation has risen faster than general inflation, with essential holiday items experiencing 8-10% annual inflation during 2023–2024.
  - Retailers maintain the Php500 price by reducing product sizes (shrinkflation) and substituting cheaper ingredients.
  - num: The Php500 basket represents 77% of the daily minimum wage (Php645) in NCR.
  - num: Food comprises 43% of total household spending, and up to 60% among the poorest 30% of households.
  - num: Poverty incidence among farmers and fisherfolk remains high at 27.0% and 27.4%, respectively, in 2023.
key_figures_tables:
  - Table 1: Food CPI in NCR (2018-2025) → A Php500 basket now costs Php669.80, a 33.96% increase from 2018.
  - Table 2: Food CPI outside NCR (2018-2025) → A Php500 basket now costs Php643.28, a 28.66% increase from 2018.
  - Table 3: Commercial Php500 holiday basket (2018 vs 2025) → Product sizes reduced and ingredients substituted to maintain price.
  - Figure 1: Poverty incidence among basic sectors (2023) → Farmers and fisherfolk have the highest poverty incidence.
  - Figure 2: Household food expenditure share by income decile → Lowest income decile spends ~60% of income on food.
key_equations:
  - equation: Adjusted Cost = 500 × (CPI_current / CPI_base)
    explanation: Adjusts 2018 basket cost to current prices.
definitions:
  - term: Shrinkflation
    definition: The practice of reducing product size while maintaining the same price.
  - term: Product Substitution
    definition: Replacing higher-cost ingredients with lower-cost alternatives.
  - term: CPI
    definition: Consumer Price Index, a measure of the average change in prices over time.
  - term: FIES
    definition: Family Income and Expenditure Survey.
  - term: 4Ps
    definition: Pantawid Pamilyang Pilipino Program, a conditional cash transfer program.
critical_citations:
  - "[PSA, 2025b] — Provides the primary CPI data for the analysis."
  - "[Rojas et al., 2024] — Quantifies the impact of shrinkflation on food inflation."
  - "[Dekimpe & van Heerde, 2023] — Provides a research agenda on retailing and inflation."
relevance:
  topics:
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Directly analyzes the cultural tradition of Noche Buena and its financial implications.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: high
      justification: Focuses on holiday-specific spending and price inflation during the Noche Buena season.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: high
      justification: Examines the cost of a specific Filipino occasion (Noche Buena) and its affordability.
    - code: 3.C
      name: User-Defined Allocation Constraints
      relevance: medium
      justification: Highlights the financial constraint of a fixed Php500 budget for a specific purpose.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Critiques the flawed metric of a fixed price point as a policy benchmark.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: Provides context on the spending burden for low-income and minimum-wage earners.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: The pressure of holiday spending impacts a household's ability to save and manage goals.
  contribution: This policy brief directly informs Odin's design by providing empirical evidence on the erosion of purchasing power for Filipino households, particularly regarding culturally significant spending events. It justifies the need for Odin's expense categorization to account for seasonal price fluctuations and the impact of inflation. The findings on shrinkflation and product substitution highlight the importance of tracking item-level data and unit prices. Furthermore, the brief underscores the necessity for Odin's budget recommendation module to be sensitive to the real cost of living and to assist users in setting realistic, inflation-adjusted savings goals. It provides a strong foundation for contextualizing user financial data within the broader economic reality.
  directly_justifies:
    - The Php500 Noche Buena basket is a culturally significant financial benchmark for Filipino families.
    - Seasonal inflation and shrinkflation significantly distort the real value of holiday spending.
    - Low-income households dedicate a disproportionate share of their income to food, limiting other financial flexibility.
    - A budget recommendation system must account for regional price differences.
  limits:
    - None identified.
  mapping_rationale: A systematic scan across all 12 functional domains was conducted. The domains of 'Filipino Cultural Context' (2.A, 2.B, 2.D) were flagged as highly relevant, as the brief directly analyzes the cost of the culturally significant Noche Buena meal and its seasonal spending patterns. 'Expense Categorization' (3.C) was flagged as medium relevance, as it provides evidence for the need to track budget constraints. 'Existing Systems & Gaps' (4.B) was also medium, as it critiques the use of a static price point as a benchmark. 'Behavioral Profiling' (5.A) and 'Savings & Debt Management' (13.A) were assessed as contextual and medium, respectively, as they provide insights into user financial stress but are not the primary focus. Domains like 'Forecasting', 'Anomaly Detection', and 'Mobile-First Design' were considered and rejected as the brief does not address algorithmic or design methodologies. The brief's overall relevance to Odin is high, as it provides essential socio-economic context and data that directly justifies the need for a personalized, context-aware PFMS for Filipino young professionals.
limitations:
  - The analysis primarily uses CPI data and a single commercial basket as an example, which may not represent all variations in household consumption patterns.
remember_this:
  - A Php500 Noche Buena basket now costs Php643 to Php670 due to inflation.
  - Retailers use shrinkflation to keep prices low while reducing real value.
  - Food spending consumes 43% of household budgets and 60% for the poor.
  - The Php500 benchmark is unrealistic for minimum-wage earners.
  - Policy must shift to real cost-of-living data for holiday assistance.
```
---

## Paper 44: Carmona_summarized.md

**Source File:** `Carmona_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: local
title: Empowering Financial Well-Being: A Comprehensive Approach to Managing Personal Finances of Employees of San Pablo Colleges Medical Center
authors: Carmona, K. N.
year: 2025
venue: Journal of Third World Economics
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 7.A
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 13.A
  - 13.B
tldr: Employees at San Pablo Colleges Medical Center exhibit awareness of budgeting but lack consistent saving and debt management practices, highlighting a need for targeted financial literacy programs.
problem_and_motivation: Many individuals lack financial literacy, leading to impulsive spending and poor income management, which is exacerbated by rising living costs. Healthcare employees at SPCMC require tailored financial management strategies to meet essential needs and prepare for emergencies. Existing financial education efforts are insufficient to address the gap between awareness and consistent application of sound financial practices.
approach:
  - The study employed a mixed-methods approach combining surveys and interviews to gather data from SPCMC employees.
  - A quantitative research method was used with weighted mean as the statistical treatment for data analysis.
  - Participants were 150 employees selected through stratified random sampling to ensure a representative sample.
  - Data was analyzed to assess current financial practices, issues, and needs across budgeting, saving, spending, and debt management.
findings:
  - num: Most respondents (65%) do not engage in regular saving habits, saving only when money is leftover.
  - num: 65% of respondents have no existing financial liabilities, yet awareness of maintaining an emergency fund is very low (mean 1.70).
  - Respondents show strong awareness of budgeting (mean 4.03) but only some awareness of saving (mean 2.57) and debt management (mean 2.96).
  - Family and social factors significantly influence financial behaviors, with families often avoiding debt and social groups exerting peer influence on spending.
  - num: Respondents rarely keep savings intact for emergencies (mean 2.21) and often borrow to pay off existing debt (mean 4.34), indicating a debt cycle.
  - The overall application of personal finance strategies is inconsistent, with budgeting practiced often (mean 3.65) and saving rarely practiced (mean 2.33).
key_figures_tables:
  - Table 1: Knowledge of Personal Finance Management Strategies → Shows budgeting awareness is high (4.03) but emergency fund knowledge is very low (1.70).
  - Table 7: Application of Saving Strategies → Reveals emergency fund saving is never practiced (1.23) and overall saving is rare (2.33).
  - Table 9: Application of Debt Management Strategies → Indicates respondents often borrow to pay off debt (4.34) yet rarely have loans exceeding 10% of salary (2.16).
  - Table 10: Summary of Application of Strategies → Overall financial management application is sometimes practiced (3.23), with saving being the weakest area.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Financial well-being
    definition: An individual's perception of their ability to meet current and future consumption demands and remain self-sufficient in financial matters.
  - term: Weighted mean
    definition: A statistical treatment used to interpret the average of responses based on assigned weights in Likert scale surveys.
  - term: SDT
    definition: Self-Determination Theory, a framework for understanding motivation and its influence on financial behavior.
critical_citations:
  - "[Brüggen et al., 2017] — Defines financial well-being as subjective perception of financial ability."
  - "[Lusardi and Mitchell, 2017] — Links higher financial literacy to better long-term financial outcomes."
  - "[Strömbäck et al., 2017] — Explains how self-control predicts financial behavior and well-being."
  - "[Di Domenico et al., 2022] — Applies Self-Determination Theory to personal financial management motivation."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: The study focuses on Filipino employees (healthcare workers) who are a subset of the young professional demographic.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: It details income brackets (e.g., 15,001-20,000 pesos) and saving habits of this professional group.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly examines financial behaviors including budgeting, saving, spending, and debt management practices.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Discusses family and social influences on financial decisions, reflecting cultural norms around debt and spending.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: Mentions the 50-30-20 rule as a spending guideline, providing a framework for categorization.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: low
      justification: Touches on spending categories (needs vs. wants) but does not deeply explore design.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides background on the general state of financial literacy and management practices in the Philippines.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies a significant gap between financial awareness and consistent application of saving and debt management strategies.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Profiles behaviors such as thriftiness and peer-influenced spending, indicating behavioral patterns.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: low
      justification: Implicitly touches on initial financial habits but does not directly address the cold-start problem.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: The study assesses awareness and application of budgeting strategies as a core financial management practice.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Not directly addressed, but the context of a workplace financial wellness program implies data handling.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: Not directly addressed, though trust in micro-financing institutions is implied through their frequent use.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: contextual
      justification: The proposed financial literacy program suggests a need for engagement, but the study does not analyze engagement dynamics.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: low
      justification: Not addressed, though a comprehensive program could include such mechanisms.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: Directly investigates saving behaviors, the lack of emergency funds, and inconsistent saving practices.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: Extensively analyzes debt management strategies, including borrowing habits and loan repayment practices.
  contribution: This study provides empirical evidence on the financial literacy and management gaps among Filipino healthcare employees, which can inform the design of a financial literacy module within Odin. The findings on the inconsistency between budgeting awareness and saving application directly justify the need for a proactive savings feature in Odin that nudges users to save first. The data on borrowing to pay off debt highlights the importance of an integrated debt management feature that can break this cycle. The identification of strong family and social influences suggests Odin's social features could be designed to promote positive financial norms. The recommended comprehensive program aligns with Odin's goal of providing a holistic PFMS for Filipino young professionals.
  directly_justifies:
    - "Employees demonstrate awareness of budgeting but lack consistent saving and debt management application."
    - "A significant gap exists in maintaining emergency funds equivalent to four to seven months of expenses."
    - "Social and family factors significantly influence individual financial behaviors and decisions."
    - "A structured financial literacy program is recommended to address gaps in knowledge and practice."
    - "Regular saving is often a reactive behavior dependent on leftover income rather than a planned strategy."
  limits:
    - "The study is limited to employees of a single medical center, limiting generalizability to all Filipino young professionals."
    - "Relies on self-reported data, which may be subject to social desirability bias."
    - "The cross-sectional design captures a snapshot in time and does not track changes in financial behavior over time."
    - "Does not evaluate specific algorithmic or technological solutions for personal finance management."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was conducted. The paper was found to be highly relevant to Domain 1 (Filipino Cultural Context) through topics 1.A, 1.B, and 1.C, as it profiles Filipino healthcare employees' financial structure and behaviors. Domain 3 (Expense Categorization) was flagged as contextual via 3.A and low via 3.B, as the paper mentions the 50-30-20 rule but does not deeply explore category design. Domain 4 (Existing Systems & Gaps) received high relevance via 4.B, as the study identifies a clear gap in saving and debt management application. Domain 5 (Behavioral Profiling) was considered medium for 5.A due to the behavioral patterns identified and low for 5.B, as the cold-start problem is not addressed. Domain 7 (Budget Recommendation) was flagged as medium via 7.A, as budgeting strategy knowledge is a key finding. Domain 10 (Data Privacy) and Domain 11 (Retention) were assigned low or contextual relevance as they are not directly addressed but are implied in the context of workplace programs. Domains 6 (Forecasting), 8 (Anomaly Detection), 9 (Mobile-First Design), and 12 (Evaluation) were considered and rejected as the study does not address algorithmic prediction, anomaly detection, mobile UX, or system evaluation frameworks. The borderline case of seasonal spending (2.B and 2.D) was considered but rejected as the study focuses on general financial behavior rather than seasonal patterns. The paper provides a foundational understanding of financial behaviors and gaps among a key target demographic for Odin, justifying the inclusion of modules for budgeting, saving, and debt management.
limitations:
  - "The study's findings are based on a sample from a single institution, which may not represent the broader population of Filipino young professionals."
  - "The methodology relies heavily on self-reported awareness and practices, which may not align with actual financial behaviors."
  - "The study does not propose or evaluate a specific technological intervention for financial management."
  - "The long-term effectiveness of the proposed financial literacy program is not empirically tested."
  - "Potential confounding variables such as education level or financial background were not thoroughly controlled."
remember_this:
  - "Budgeting awareness is high among Filipino healthcare employees."
  - "Saving and emergency fund practices are critically weak."
  - "Debt management is often cyclical, with borrowing used to pay off existing debt."
  - "Family and social influences are strong drivers of financial behavior."
  - "A comprehensive financial literacy program is needed to bridge the awareness-action gap."
```
---

## Paper 45: Aggarwal et al_summarized.md

**Source File:** `Aggarwal et al_summarized.md`

```yaml
paper_id: 10.2139/ssrn.5906744
designation: international
title: DIGITAL BANKING AND THE FUTURE OF EMBEDDED FINANCE: HOW WILL AI-POWERED FRAUD DETECTION AND ALGORITHMIC CREDIT SCORING IN CROSS-BORDER RAILS RESHAPE SYSTEMIC RISK?
authors: Aggarwal, L.; Saravanan, T.; Loana, A.; Alisa,; Shreshta,
year: 2025
venue: Unknown
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 13.A
tldr: AI integration in digital banking, embedded finance, and cross-border payments enhances fraud detection and credit access but introduces new systemic risks like algorithmic herding and model opacity.
problem_and_motivation: The digitization of finance has created high-velocity payment rails and globalized platforms. Traditional risk controls cannot keep pace. A framework is needed to manage the new systemic vulnerabilities introduced by the reliance on AI for critical financial functions.
approach:
  - Analysis of international regulatory guidance (BIS, Bank of England, FSB) and cross-market pilots (Project Nexus, Project Aurora).
  - Examination of commercial case studies, including Nubank, Tala, Mifundo, and Nova Credit.
  - Qualitative synthesis of industry reports and white papers to identify both opportunities and risks of AI in finance.
  - Framework analysis focusing on systemic, operational, data, governance, and cybersecurity risk dimensions.
  - Assessment of AI techniques such as Graph Neural Networks, Federated Learning, and ISO 20022 data enrichment.
findings:
  - AI and machine learning outperform traditional rule-based systems in detecting complex fraud patterns.
  - Algorithmic credit scoring using alternative data expands financial inclusion for unbanked and underbanked populations.
  - Digital banking has become a primary financial access point, with over 3.6 billion users globally.
  - AI enables scalable interoperability for real-time cross-border payments but introduces operational vulnerabilities.
  - num: Graph-based models identified approximately twice the number of potential money laundering networks than standard methods.
  - Embedded finance and shared AI models create a risk of algorithmic herding and correlated market failures.
  - Model opacity in 'black box' AI systems limits auditability and can perpetuate historical biases.
  - num: Financial firms faced a 25% surge in advanced cyberattacks in 2024 compared to the previous year.
  - The sector lacks robust macro-prudential governance frameworks to manage AI-driven systemic risk.
key_figures_tables:
  - Table 1: Comparison of traditional vs. AI-based fraud detection → AI offers adaptive, real-time, and higher-accuracy fraud detection.
  - Picture 1: Tala's mobile data scoring process → Behavioral phone data can effectively predict creditworthiness for the unbanked.
  - Picture 2: BIS Project Nexus hub-and-spoke model → AI enables standardized interoperability between domestic instant payment systems.
  - Picture 3: Systemic risks of Artificial Intelligence → Model reliance creates new interconnected technological vulnerabilities.
  - Picture 4: Concentration risk illustration → Heavy reliance on a few AI providers increases systemic vulnerability.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Embedded Finance
    definition: The seamless integration of financial services into non-financial platforms.
  - term: Graph Neural Networks
    definition: AI models that analyze relationships in payment networks to detect complex fraud like money laundering rings.
  - term: Federated Learning
    definition: An AI technique that trains models across institutions without sharing raw customer data, enhancing privacy.
  - term: ISO 20022
    definition: A global messaging standard for payments that provides richer, structured data for better transaction processing.
  - term: Algorithmic Herding
    definition: The risk of many institutions using similar AI models, leading to correlated errors and market instability.
  - term: Macro-prudential
    definition: A regulatory approach focused on the stability of the entire financial system rather than individual institutions.
critical_citations:
  - "[Bank for International Settlements, 2024b] — Provides evidence for AI-enabled cross-border payments infrastructure."
  - "[Bank for International Settlements, Innovation Hub Nordic Centre, 2023] — Demonstrates GNN effectiveness in fraud detection."
  - "[Bank of England, 2025] — Discusses AI-induced systemic and algorithmic risks."
  - "[Financial Stability Board, 2024] — Analyzes AI's impact on systemic risk and financial stability."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: The paper discusses credit scoring and fraud, not direct categorization but context.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: low
      justification: Mentions data enrichment (ISO 20022) which could inform category design but not directly.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Provides a comprehensive overview of digital banking, embedded finance, and cross-border payment landscapes.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly identifies gaps in legacy correspondent banking, credit data portability, and existing fraud detection methods.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: low
      justification: Tala case study analyzes behavioral data for credit scoring, relevant to profiling.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: medium
      justification: Discusses 'thin file' and migrant 'credit passport' problems, which are cold-start issues for credit profiles.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Reviews algorithmic credit scoring methods that classify creditworthiness based on behavioral data.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: contextual
      justification: Mentions AI models for predicting payment failure rates and liquidity needs.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Core topic is AI-based fraud detection as a form of anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Specifically examines algorithms like Graph Neural Networks for fraud pattern detection.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Addresses cross-border data privacy, security measures, and the use of Federated Learning for privacy.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Security and fraud are key to user trust; discusses how breaches can lead to loss of trust.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: Digital banking adoption trends and the demand for seamless, instant experiences are noted.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: low
      justification: The paper focuses on infrastructure and risk, not specific retention mechanisms.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: The 'end-of-period surplus' concept is not directly mentioned.
  contribution: This paper provides a macro-level argument for the integration of AI in global finance, highlighting the mutual dependency between digital banking and AI. It supports the need for robust anomaly detection systems (module 8) by showing the limitations of rule-based methods. It justifies investment in data privacy and security (module 10) by detailing cyber risks and regulatory challenges. The paper also advocates for a 'macro-prudential' regulatory approach, which is essential for modules that rely on external data or are part of a larger interconnected system.
  directly_justifies:
    - Algorithmic credit scoring expands financial access for previously unbanked populations.
    - AI-based fraud detection using graph networks significantly outperforms traditional rule-based systems.
    - Real-time cross-border payments are scalable but introduce new operational vulnerabilities.
    - Model homogeneity creates a risk of correlated algorithmic failures and systemic instability.
    - Heavy reliance on a few providers creates concentration risk.
  limits:
    - The study is based on a qualitative synthesis of secondary sources and not primary quantitative research.
    - The findings are limited to the specific initiatives and case studies reviewed (e.g., Project Nexus, Tala).
    - The paper does not perform a detailed cost-benefit analysis of implementing specific AI models.
    - The discussion of bias is acknowledged but not deeply explored in terms of concrete mitigation strategies.
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was found to be most relevant to domains covering existing systems and gaps (4.A, 4.B) and anomaly detection (8.A, 8.B), where it provides detailed analysis of AI models and their benefits. The paper also offers high relevance to data privacy and user trust (10.A, 10.B) through its discussion of cross-border data challenges. Medium relevance was assigned to behavioral profiling and classification (5.A, 5.B, 5.C) and user retention (11.A, 11.B) based on its discussion of credit scoring and user adoption. Low or contextual relevance was assigned to expense categorization (3.A, 3.B) and savings/debt management (13.A), as these were not primary foci. Domains such as forecasting (6.A, 6.B) and budget recommendation (7.A-D) were considered and rejected as they were not directly addressed. The paper's overall relevance lies in its synthesis of AI's dual role as an enabler and a source of risk, providing foundational justification for Odin's core systems.
limitations:
  - The paper relies on secondary industry reports and case studies rather than primary data.
  - The analysis is broad and does not delve into the technical specifics of algorithm implementation.
  - Potential biases in the cited industry sources are not discussed. [unacknowledged]
  - The paper lacks a rigorous methodology for comparing the effectiveness of different AI models. [unacknowledged]
remember_this:
  - AI-based fraud detection systems outperform traditional rule-based methods.
  - Graph Neural Networks identified twice the money laundering networks.
  - Algorithmic credit scoring uses alternative data to serve the unbanked.
  - Shared AI models create risk of systemic algorithmic failure.
  - Financial firms saw a 25% surge in cyberattacks in 2024.
```
---

## Paper 46: Velez_summarized.md

**Source File:** `Velez_summarized.md`

```yaml
paper_id: 10.69569/jip.2025.056
designation: local
title: A Systematic Review of Mobile Banking, Fintech Innovations, and Regulatory Gaps to Achieve Financial Inclusion in the Philippines
authors: Velez, G.
year: 2025
venue: Journal of Interdisciplinary Perspectives
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 7.B
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 11.A
  - 12.A
  - 13.A
tldr: Mobile banking and fintech have expanded financial access in the Philippines but persistent digital, gender, and literacy gaps continue to exclude marginalized populations.
problem_and_motivation: Financial inclusion in the Philippines remains low, with 68% of adults unbanked, despite the growth of mobile banking and fintech. A comprehensive synthesis of how these technologies, along with regulatory frameworks, affect marginalized communities is lacking. This review addresses that gap to inform more equitable policy and design.
approach:
  - The study conducted a systematic literature review following PRISMA guidelines.
  - Searches were performed in ProQuest and Google Scholar using Boolean strings for digital financial inclusion in the Philippines.
  - Inclusion criteria covered peer-reviewed articles, policy papers, and grey literature from 2014 to 2024 focusing on the Philippines.
  - Data extraction and synthesis used narrative synthesis and thematic analysis to identify recurring themes.
  - The review analyzed 26 studies meeting quality criteria, comprising journal articles, policy papers, institutional reports, and a thesis.
findings:
  - num: Mobile banking adoption surged 18-35% post-2019, driven by platforms like GCash and pandemic-induced digitization.
  - num: GCash reduced cash dependency by 41% in urban and 29% in rural areas.
  - num: Women-owned MSMEs comprise only 22% of fintech borrowers despite being 39% of entrepreneurs.
  - num: Only 34% of low-income users understand digital payment security features.
  - The National Retail Payment System drove a 19% increase in digital transaction volumes but struggles with fragmentation and rural implementation.
  - Rural adoption rates are 1.8 times lower than urban areas due to infrastructure and connectivity gaps.
  - The pandemic accelerated digitization but increased exclusion for 28% of low-literacy users.
key_figures_tables:
  - Table 4: Summary of 26 studies on digital financial inclusion → Highlights key findings on access, barriers, and demographic disparities.
  - Figure 1: PRISMA flow diagram of study selection → Documents the systematic review process from 1,296 records to 26 included studies.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: MSMEs
    definition: Micro, small, and medium-sized enterprises.
  - term: NRPS
    definition: National Retail Payment System, a Philippine regulatory framework for digital transactions.
  - term: PRISMA
    definition: Preferred Reporting Items for Systematic Reviews and Meta-Analyses, a guideline for conducting systematic reviews.
  - term: Fintech
    definition: Financial technology used to deliver financial services digitally.
critical_citations:
  - "[BSP, 2023] — Provides baseline unbanked rate of 68% for the Philippines."
  - "[Molina, 2024] — Documents specific cash dependency reductions by GCash."
  - "[ADB, 2024] — Reports gender disparity in fintech borrowing among women-owned MSMEs."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: Provides demographic context on unbanked adults and digital adoption trends.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Discusses income, urbanization, and remittance factors influencing financial access.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: low
      justification: Touches on adoption behaviors but not specifically for young professionals.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Identifies gender norms and remittance reliance as cultural financial practices.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Mentions weather-related income fluctuations in fishing communities but not a central focus.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: References remittance-driven financial behavior but does not detail spending cycles.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: low
      justification: Discusses digital payments broadly, without specific categorization frameworks.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: low
      justification: Not directly addressed; the focus is on access, not categorization.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Reviews the Philippine fintech landscape, specifically platforms like GCash and Maya.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Documents persistent digital divide, gender gaps, and literacy barriers as system limitations.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: low
      justification: Mentions demographic and socioeconomic factors but does not construct behavioral profiles.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Discusses fintech use of alternative data for credit scoring, a form of behavioral classification.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Implicitly relevant through financial inclusion but not focused on budget recommendation.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: high
      justification: Highlights smartphone penetration and mobile banking as primary access channels.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Notes that low-literacy users struggle with digital interfaces, implying UX gaps.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Reports that only 34% of low-income users understand digital security features.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Security, trust, and reliability are identified as key factors for adoption and continued use.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: low
      justification: Mentions adoption surge but does not analyze engagement dynamics.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: contextual
      justification: Uses systematic review methodology rather than evaluating a specific system.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: low
      justification: Remittances and bank account holding are mentioned but not savings goal management.
  contribution: This review provides a comprehensive evidence base on the barriers to digital financial inclusion in the Philippines, which can inform Odin's design for targeting underserved demographics. It directly justifies the need for mobile-first solutions that address the digital divide, particularly for rural and low-income users. The findings on gender disparities and low financial literacy support the development of inclusive behavioral profiling and personalized financial education within Odin. The documented limitations of existing regulatory frameworks and fintech platforms highlight opportunities for Odin to differentiate itself through better user support and trust-building mechanisms.
  directly_justifies:
    - Rural adoption rates are 1.8 times lower than urban areas, necessitating mobile-first design for low-connectivity environments.
    - Only 34% of low-income users understand digital security, justifying simplified security communication in app interfaces.
    - Women-owned MSMEs represent only 22% of fintech borrowers despite comprising 39% of entrepreneurs, supporting gender-sensitive product design.
    - The digital divide in regions like Visayas and Mindanao creates unique challenges for financial behavior profiling.
  limits:
    - The review primarily synthesizes cross-sectional studies (80%), limiting causal inference for Odin's forecasting modules. [unacknowledged]
    - The review does not evaluate specific algorithms for expense categorization, anomaly detection, or budget recommendation. [unacknowledged]
    - The focus on financial inclusion may not directly translate to behavioral profiling or spending forecasting for young professionals.
  mapping_rationale: A systematic scan across all 12 functional domains identified the strongest relevance to Existing Systems & Gaps (high), Mobile-First Design (high), and User Trust (high), as the paper directly reviews the Philippine fintech landscape, documents adoption barriers, and identifies trust as a key adoption factor. Medium relevance was assigned to Filipino Cultural Context for its discussion of gender norms and remittance reliance, and to Behavioral Profiling for its mention of alternative credit scoring. Low relevance was assigned to Expense Categorization and Budget Recommendation due to the absence of specific frameworks. Contextual relevance was assigned to Seasonal Spending and Evaluation Frameworks, as these are mentioned but not central. Domains such as Anomaly Detection, Forecasting, and Savings/Debt Management were considered but rejected due to lack of direct coverage. The paper's overall relevance to Odin is moderate, providing foundational context on user demographics and systemic gaps rather than algorithmic or design-specific insights.
limitations:
  - The review relies on secondary sources, not primary data collection.
  - A small number of studies (26) were included after screening.
  - The methodological quality of included studies varies.
  - The focus is on financial inclusion broadly, not specifically on young professionals or PFMS. [unacknowledged]
  - The review does not provide a detailed analysis of specific fintech algorithms or system architectures. [unacknowledged]
remember_this:
  - Mobile banking adoption surged 18-35% post-2019 in the Philippines.
  - Women-owned MSMEs are underrepresented in fintech borrowing at 22%.
  - Only 34% of low-income users understand digital payment security.
  - Rural adoption rates are 1.8 times lower than in urban areas.
  - The digital divide and low literacy are key barriers to financial inclusion.
```
---

## Paper 47: Badiger et al_summarized.md

**Source File:** `Badiger et al_summarized.md`

```yaml
paper_id: 10.17148/IJARCCE.2025.14364
designation: international-algorithm-specific
title: Next.js-Powered AI Platform for Smart Expense Tracking, Budgeting and Insights
authors: Badiger, R.; Robin, R.; Moraas, T.; Naik, V. G.; Karthikeyan A N, P.
year: 2025
venue: International Journal of Advanced Research in Computer and Communication Engineering
odin_topics:
  - 3.A
  - 4.A
  - 4.B
  - 6.A
  - 8.A
  - 12.A
tldr: An AI-powered personal finance platform integrating machine learning categorization, large language model insights, and time-series forecasting within a Next.js full-stack architecture.
problem_and_motivation: Existing personal finance tools lack automated real-time categorization, personalized natural-language insights, and predictive budgeting capabilities. This gap is particularly acute for users navigating multi-channel digital payment ecosystems, leading to poor financial decision-making.
approach:
  - The system is built on Next.js 14, Prisma ORM, Supabase PostgreSQL, and Clerk authentication.
  - Automated transaction categorization uses an XGBoost classifier trained on labelled transaction data.
  - Natural-language financial insights are generated using Google's Gemini LLM with a RAG pattern.
  - Expense forecasting is implemented using Meta's Prophet time-series model per spending category.
  - The platform supports multi-modal data ingestion including manual entry, CSV import, and receipt scanning.
  - Evaluation was performed on a held-out test set of 4,200 transactions from anonymized datasets.
findings:
  - "num: The XGBoost categorization model achieves a weighted F1-score of 0.913 across 18 spending categories."
  - "num: Server response times average 420ms for dashboard loads, with AI insight generation adding 800-1,400ms."
  - "num: The system reduces manual expense-logging effort by approximately 78% compared to conventional approaches."
  - Categories with high linguistic diversity show lower precision, while frequent categories achieve F1-scores above 0.95.
  - User feedback indicated that 84% of participants found the AI-generated insights useful for guiding financial decisions.
key_figures_tables:
  - "Figure 1: End-to-End User Workflow of Spend AI → visualizes the seven-stage process from authentication to budget alerts."
  - "Figure 2: Five-Layer System Architecture of Spend AI → illustrates the modular presentation, business, AI, data, and authentication layers."
  - "Figure 3: Technology Stack Overview → summarizes the complete technology stack from frontend to AI components."
  - "Figure 4: AI Insight Generation Pipeline (RAG Pattern) → shows the RAG-based prompt construction for the Gemini LLM."
  - "Figure 5: XGBoost Transaction Categorisation F1-Scores → displays per-category performance of the classification model."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "LLM"
    definition: "Large Language Model, used for natural-language insight generation."
  - term: "RAG"
    definition: "Retrieval-Augmented Generation, a pattern for grounding LLM responses in specific data."
  - term: "XGBoost"
    definition: "Extreme Gradient Boosting, a gradient-boosted tree classifier used for transaction categorization."
  - term: "UPI"
    definition: "Unified Payments Interface, India's real-time payment system."
  - term: "RLS"
    definition: "Row-Level Security, a database feature for enforcing per-user data isolation."
critical_citations:
  - "[Verma et al., 2024] — demonstrated Next.js viability but lacked AI categorization."
  - "[Kotios et al., 2022] — provided benchmarks for hybrid transaction classification."
  - "[Hean et al., 2025] — evaluated Gemini's capability for personal finance tasks."
  - "[Pancholi et al., 2026] — proposed multi-agent AI system for personal finance."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: "Implements an XGBoost model achieving 91.3% F1-score for transaction categorization."
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: "Reviews existing PFM systems and identifies gaps in automation and personalization."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: "Explicitly addresses limitations of prior systems and motivates the development of Spend AI."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: "Uses Prophet for time-series forecasting of monthly expenses by category."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: "Includes anomaly detection as a core feature, flagging transactions exceeding statistical thresholds."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: "Evaluates system performance through categorization accuracy and user experience feedback."
  contribution: "The paper's architecture for integrating ML categorization, LLM insights, and time-series forecasting directly informs Odin's design for the Categorization Engine, AI Insight Module, and Forecasting Module. Its use of a full-stack framework with row-level security provides a production-ready template for Odin's Mobile-First Design and Data Privacy & User Trust considerations. The experimental evaluation methodology offers a framework for evaluating Odin's algorithmic modules."
  directly_justifies:
    - "A gradient-boosted tree classifier can achieve over 91% accuracy for transaction categorization tasks."
    - "LLM-based insights grounded in user data via RAG can generate useful and validated financial guidance."
    - "Time-series forecasting with Prophet is feasible for personal spending prediction using limited historical data."
    - "Row-level security is a critical architectural property for systems handling sensitive financial data."
  limits:
    - "Categorization accuracy is lower for new users with fewer than 50 historical transactions (cold-start problem)."
    - "LLM hallucination risk remains, though mitigated by RAG-style prompting."
    - "Forecasting accuracy requires at least 3 months of historical data for reliable predictions."
    - "Data residency and regulatory compliance (e.g., DPDP Act) require further attention. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes flagged four domains as highly relevant: Expense Categorization (3.A), Existing Systems & Gaps (4.A, 4.B), Spending Forecasting (6.A), and Anomaly Detection (8.A). The paper's core contribution is algorithmic, justifying the 'algorithm-specific' designation, with direct implications for Odin's predictive and categorization modules. The System Evaluation domain (12.A) was considered relevant as the paper provides a performance evaluation framework. The Behavioral Profiling & Classification (5.A) domain was considered but rejected as the paper does not develop or utilize user financial profiles. The Savings & Debt Management domain (13.A, 13.B) was also considered but rejected as the paper's primary focus is on expense tracking and budgeting rather than savings or debt-specific features. Overall, the paper provides strong, directly applicable evidence for building an AI-powered PFMS, particularly its core algorithmic components."
limitations:
  - "LLM hallucination risk remains; critical recommendations should be verified."
  - "Manual data entry dependency persists in the absence of direct banking API integration."
  - "Data residency and regulatory compliance require further attention. [unacknowledged]"
  - "Forecasting accuracy requires at least 3 months of historical data for reliable predictions."
remember_this:
  - "XGBoost achieved 91.3% F1-score for transaction categorization across 18 categories."
  - "Platform reduces manual expense-logging effort by approximately 78%."
  - "84% of pilot users found Gemini-generated insights useful for financial decisions."
  - "System architecture separates presentation, business, AI, data, and authentication layers."
  - "RAG-based prompting grounds LLM insights in verifiable user data to reduce hallucination."
```
---

## Paper 48: Pakarinen_summarized.md

**Source File:** `Pakarinen_summarized.md`

```yaml
paper_id: 1b3c4a5d-6e7f-8a9b-0c1d-2e3f4a5b6c7d
designation: international-algorithm-specific
title: Optimizing Banking Application Interfaces: A User-Centric Perspective on Consent Management in Digital Banking Environments
authors: Pakarinen, O.
year: 2025
venue: JAMK Master's Thesis
odin_topics:
  - 10.A
  - 10.B
  - 9.A
  - 9.B
  - 11.A
  - 11.B
  - 12.A
  - 3.A
tldr: Consent interfaces designed with category overviews and detailed controls improved user understanding, control perception, and decision confidence compared to traditional dense legal text approaches.
problem_and_motivation: Consent management in digital banking is often implemented with complex legal language and confusing formats, which undermines user understanding and informed decision-making. This gap between regulatory requirements and practical user comprehension poses risks to trust and autonomy. There is a need for consent interfaces that are transparent, accessible, and supportive of user control.
approach:
  - The study employed a mixed-methods approach, including a preliminary exploratory survey (n=6) to guide design.
  - A consent management prototype with a two-level structure (category-based overview and detailed consent view) was designed using Figma and the MEAN stack.
  - Two rounds of usability testing were conducted with participants interacting with the prototype, followed by semi-structured interviews.
  - Usability testing measured task completion time, error rate, user hesitations, and confidence levels.
  - Feedback from the first round informed iterative design improvements, such as breaking text into smaller segments and adding visual cues.
findings:
  - Participants interacting with the new consent flow showed increased confidence in their consent decisions.
  - Category-based overviews and explicit labels significantly improved users' ability to understand the consent structure.
  - Traditional consent screens with lengthy legal text were often ignored or skimmed, leading to user uncertainty.
  - Providing immediate feedback after a consent setting change reinforces user understanding and control.
  - Progressive disclosure of information (from category overview to detailed view) reduced cognitive load and improved comprehension.
  - The AI-powered "Smart Summary" feature was found helpful by participants for confirming their decisions.
key_figures_tables:
  - Figure 6.1: Revolut's category-based privacy settings → Illustrates a user-centric, mobile-first approach to consent.
  - Figure 6.2: ING Spain's Didomi consent interface → Shows standardized consent presentation across channels.
  - Figure 6.3: Nordea's open banking authorization flow → Demonstrates secure, in-app consent for third-party data access.
  - Figure 7.1: Consent management flow diagram → Visualizes the step-by-step user journey in the prototype.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: GDPR
    definition: General Data Protection Regulation, a legal framework that sets guidelines for the collection and processing of personal information.
  - term: CCPA
    definition: California Consumer Privacy Act, a state statute intended to enhance privacy rights and consumer protection.
  - term: Consent Management
    definition: The process of how users accept or decline the processing of personal information and how that consent is managed.
critical_citations:
  - "[Nouwens et al., 2020] — Demonstrated how consent pop-ups can influence user decisions."
  - "[EDPB, 2022] — Provided guidelines on dark patterns and consent clarity."
relevance:
  topics:
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: The study directly addresses the design of consent interfaces for managing personal data privacy.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Findings show that clear consent interfaces improve user confidence and trust.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: The prototype and case studies (e.g., Revolut) emphasize mobile-first design for consent.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: The usability testing focuses on user experience and interaction design for consent management.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: The research explores how consent design affects user engagement and decision-making.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: low
      justification: While not a primary focus, improved consent management is framed as supporting long-term customer loyalty.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: The study uses usability testing and interviews, aligning with system evaluation methodologies.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: The paper references consent categories for data usage, not for expense categorization.
  contribution: The research demonstrates that applying user-centered design principles—such as empathy, accessibility, and flexibility—can transform consent management from a formal regulatory requirement into a clearer and more approachable user experience. The proposed two-layer consent interface and evaluation results provide actionable evidence for improving user understanding and control in PFMS. The findings directly inform the design of Odin's consent and privacy-related modules, particularly in enhancing user trust.
  directly_justifies:
    - "Category-based consent overviews improve user orientation and understanding."
    - "Concise language and explicit labels increase user confidence in consent decisions."
    - "Providing a clear consent state (active/inactive/partial) reduces user uncertainty."
    - "Gradual disclosure of consent information lowers cognitive load."
    - "An AI-powered summary can effectively support users in confirming their choices."
  limits:
    - "Small sample size limits the generalizability of the usability findings."
    - "The study was conducted in a controlled environment, not a real banking system."
    - "The prototype simplified certain backend functions, which might influence user perceptions."
    - "Findings are primarily derived from a Finnish/European context and may not fully represent Filipino user behavior." [unacknowledged]
  mapping_rationale: A systematic scan of all 12 functional domains and their associated canonical topic codes was performed. The domains of "Data Privacy & User Trust" (topics 10.A, 10.B), "Mobile-First Design" (9.A, 9.B), and "User Retention & Engagement" (11.A, 11.B) were flagged as highly or moderately relevant, as the paper directly addresses consent interface design and its impact on user control, trust, and interaction. The "System Evaluation" domain (12.A) received medium relevance due to the study's methodology. The "Expense Categorization" domain (3.A) was considered contextual as the paper discusses consent categories but not for expenses. Domains like "Spending Forecasting" and "Budget Recommendation" were considered and rejected as the paper does not address predictive algorithms or allocation constraints. Borderline cases, such as the paper's discussion of user engagement touching both 11.A and 11.B, were resolved by identifying 11.A (engagement dynamics) as more directly applicable. Overall, the paper provides strong evidence for the design of consent and privacy modules, which are foundational to building user trust in Odin.
limitations:
  - "Small sample size for the survey and usability tests."
  - "Controlled testing environment may not reflect real-world banking interactions."
  - "The prototype was simplified and not integrated with a live banking system."
  - "Limited exploration of long-term user engagement with the consent model."
  - "Potential cultural bias as the study was conducted in a European context, which may not apply to Filipino users." [unacknowledged]
remember_this:
  - "Usability testing showed increased user confidence with the improved consent interface."
  - "Category-based overviews are more effective than long legal text for consent comprehension."
  - "Iterative design based on user feedback significantly reduced task completion time."
  - "Clear consent status visibility reduces user uncertainty and hesitation."
```
---

## Paper 49: Sipila_summarized.md

**Source File:** `Sipila_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international
title: Proof of concept of centralized personal finance application
authors: Sipilä, M.
year: 2025
venue: Unknown
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 9.A
  - 10.A
  - 11.A
  - 12.A
tldr: A proof-of-concept personal finance application was developed using DSRM to consolidate fragmented financial tracking, automate data retrieval, and generate integrated reports for a stakeholder.
problem_and_motivation: Stakeholders managing finances over a decade rely on fragmented tools like spreadsheets and third-party apps, leading to scalability issues, high manual effort, and error-prone reporting. Existing PFM tools lack comprehensive integration and automation, failing to meet the needs of sophisticated users with specific asset tracking requirements.
approach:
  - The Design Science Research Methodology (DSRM) was followed, involving six iterative phases from problem identification to evaluation.
  - A structured questionnaire identified stakeholder challenges, including complexity, lack of automation, and reporting inefficiencies.
  - The application was built using Flutter for a cross-platform UI, ASP.NET Core for the backend API, and MongoDB for data storage.
  - Key features include asset tracking (shares, cash, real estate), categorized cash flow monitoring, and automated PDF report generation.
  - External integrations were implemented using Google Sheets API for stock prices and HexaRate API for exchange rates, with a focus on automating data retrieval.
findings:
  - num: The PoC application significantly reduced manual work and human error by centralizing financial data and automating calculations.
  - num: The stakeholder reported a reduction in manual effort and increased trust in data accuracy, validated through task-based user testing.
  - num: The system successfully replaced a multi-step manual reporting process with one integrated, automated PDF report generation feature.
  - The stakeholder found the interface intuitive and the visualizations (pie charts, trend graphs) clear and informative for gaining financial insights.
  - The application effectively addressed the core "Must have" requirements, such as data visualization and asset tagging, as defined in the design phase.
  - User feedback highlighted the need for refinements in tooltips, label clarity, and a clearer definition of the cash flow module's purpose.
key_figures_tables:
  - Figure 3: Interactive doughnut chart of shares → Visualizes portfolio distribution.
  - Figure 4: Editable tables of assets with summary stats → Enables data review and modification.
  - Figure 5: User net worth over time → Tracks historical asset growth trends.
  - Figure 7: Multi-layered pie charts of share distribution → Shows categorization by type, country, and subcategory.
  - Figure 9: Cash flow tracking charts and timeline → Compares monthly income and expenses.
  - Figure 10: User-generated financial report → Consolidates key metrics into a PDF.
  - Table 9: Baseline vs. PoC system comparison → Highlights improvements in automation and centralization.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: DSRM
    definition: Design Science Research Methodology
  - term: PFM
    definition: Personal Finance Management
  - term: PoC
    definition: Proof-of-concept
  - term: FR
    definition: Functional Requirement
  - term: QA
    definition: Quality Attribute
critical_citations:
  - "[Cederberg, 2013] — Highlights user preference for automation and visual clarity."
  - "[Torno et al., 2021] — Identifies lack of holistic integration in PFM apps."
  - "[Stefanov et al., 2024] — Notes need for localized and centralized PFM solutions."
  - "[Herrala et al., 2023] — Links tool complexity to user stress and distrust."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: The system implements categorization for transactions and assets, aligning with this topic.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: User tagging and categorization of cash flow and assets are core to the design.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: The thesis provides a detailed literature review and analysis of PFM landscape limitations.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Directly addresses fragmentation, manual effort, and scalability gaps in current tools.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: contextual
      justification: Flutter was used for cross-platform support, but mobile optimization was not completed.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: The lack of authentication is identified as a major limitation, highlighting its importance.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Discusses how automation and visualization can improve user engagement and motivation.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Used a structured DSRM evaluation with task-based testing and stakeholder questionnaires.
  contribution: "This research contributes a practical proof-of-concept that demonstrates how centralized financial data, automated retrieval, and integrated reporting can significantly reduce manual workload and errors for a sophisticated user. The application's design directly informs Odin's architecture for asset tracking and reporting modules. The DSRM-based iterative development and stakeholder evaluation provide a validated framework for building user-centric PFM tools. The findings on automation and data centralization justify Odin's focus on these features to address similar gaps in the Filipino context."
  directly_justifies:
    - "A centralized platform can solve the problem of fragmented financial data from multiple sources."
    - "Automating data retrieval for share prices and exchange rates significantly reduces manual effort and errors."
    - "Integrated reporting replaces time-consuming manual processes with on-demand summaries."
    - "User-centered design and iterative feedback are critical for developing effective PFM tools."
    - "Stakeholders value systems that are reliable, automated, and provide clear visual insights."
  limits:
    - "The study is based on a single stakeholder, limiting generalizability to broader populations."
    - "Full automation through bank and broker APIs was not achieved, relying on manual entry and workarounds."
    - "No authentication or authorization mechanisms were implemented, posing data security risks."
    - "Mobile-specific UI optimization was not completed, focusing primarily on desktop and web platforms."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. Domains directly relevant to the thesis's core contribution (expense categorization, existing systems/gaps, and system evaluation) were flagged as high priority. The paper's literature review and problem analysis strongly support topics like 3.A, 3.B, 4.A, and 4.B (high). Its practical evaluation using a DSRM framework provides a direct contribution to 12.A (high). The discussion on user engagement and motivation links to 11.A (medium). The mention of mobile-first design (9.A) and data security (10.A) is purely contextual, as these were not primary implementation focuses due to the PoC scope. Topics related to Filipino cultural context (2.A-D), behavioral profiling (5.A-C), forecasting (6.A-B), budget recommendation (7.A-D), anomaly detection (8.A-C), and savings/debt management (13.A-C) were considered but rejected as the thesis does not address these specific problem domains. The paper's overall relevance to Odin is high as it provides a validated blueprint for a centralized PFM system with automated reporting, addressing gaps found in many existing tools."
limitations:
  - "The system was only tested with one stakeholder, limiting generalizability of usability findings. [unacknowledged]"
  - "User authentication and data privacy were not implemented, making it unsuitable for multi-user deployment."
  - "Full automation via bank/broker APIs was not achieved, requiring manual data entry for some transactions."
  - "Mobile UI optimization was not completed, limiting the 'mobile-first' aspect of the design."
  - "Performance was not formally tested under load, and no unit/integration tests were documented."
  - "The study's findings may be biased due to the stakeholder's high financial literacy."
remember_this:
  - "Centralized PFM tools reduce manual work and improve data reliability."
  - "Automated reporting saves significant time compared to manual quarterly reviews."
  - "Stakeholder feedback confirmed a reduction in manual effort and increased trust in data."
  - "The PoC addressed core requirements but lacked authentication and mobile optimization."
  - "DSRM provides an effective framework for developing user-centered financial applications."
```
---

## Paper 50: Aboud_summarized.md

**Source File:** `Aboud_summarized.md`

```yaml
paper_id: 10.21070/acopen.10.2025.12858
designation: international-algorithm-specific
title: Goal Programming Model in Financial Planning of the International Development Bank
authors: Aboud, M.M.S.F.
year: 2025
venue: Academia Open
odin_topics:
  - 7.C
  - 12.C
tldr: Goal programming optimizes conflicting financial objectives in banking under resource constraints, achieving near-optimal solutions with minimal deviations.
problem_and_motivation: Financial institutions struggle to balance multiple conflicting objectives like profitability, cost control, and liquidity. Traditional planning models lack the capability to handle these competing goals, especially in resource-constrained environments. A quantitative method is needed to reconcile these trade-offs and improve decision-making.
approach:
  - A weighted-preemptive hybrid goal programming model is formulated for bank financial planning.
  - The model incorporates multiple objectives: revenue, expenses, net profit, fixed assets, loans, and equity.
  - WINQSB software is used to solve the model with prioritized goals and assigned weights.
  - The case study uses annual financial data from the International Development Bank for 2016-2024.
  - The model is evaluated by comparing actual and target values across all financial goals.
findings:
  - The GP model achieved near-optimal solutions for all prioritized goals.
  - Revenue goal was slightly underachieved with a negative deviation of 0.1884.
  - Expense goal was slightly underachieved with a negative deviation of 0.1873.
  - Net profit goal was underachieved with a negative deviation of 0.3006.
  - Fixed assets goal was overachieved with a positive deviation of 0.7833.
  - Equity goal was underachieved with a negative deviation of 0.2956.
  - The model demonstrates flexible prioritization of goals in a multi-objective setting.
key_figures_tables:
  - Table 1: Financial data summary 2016-2024 → Provides raw data for the model.
  - Table 2: Scaled financial data in billion IQD → Enables analysis with smaller numbers.
key_equations:
  - equation: Min Z = Σ(w_i^- d_i^- + w_i^+ d_i^+)
    explanation: Minimizes weighted deviations from multiple goals.
  - equation: Σ a_ij X_j + d_i^- - d_i^+ = b_i
    explanation: Defines goal constraints with deviation variables.
definitions:
  - term: Goal Programming
    definition: A mathematical model for solving multi-objective problems with competing goals.
  - term: Negative Deviation
    definition: The amount by which an actual value is below the aspiration level.
  - term: Positive Deviation
    definition: The amount by which an actual value exceeds the aspiration level.
  - term: Weighted Method
    definition: Assigns weights to goals and minimizes total weighted deviation.
  - term: Preemptive Method
    definition: Prioritizes goals, satisfying higher-priority ones first.
  - term: WINQSB
    definition: Software used to solve the goal programming model.
critical_citations:
  - "[Alam, 2022] — Foundational GP model for financial planning."
  - "[Lakshmi et al., 2021] — GP application in financial planning case study."
  - "[Nyor et al., 2022] — GP for financial management in Nigeria."
relevance:
  topics:
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: high
      justification: Applies goal programming to optimize multi-objective financial planning.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Demonstrates a method for evaluating optimal solutions against target values.
  contribution: "The paper provides a practical optimization framework that can inform Odin's budget recommendation module by demonstrating how conflicting objectives (e.g., maximizing savings while minimizing expenses) can be balanced using a weighted-preemptive goal programming approach. The solution method, using WINQSB, offers a reproducible technique for solving multi-objective financial planning problems with prioritized constraints. The case study results, including deviation analysis, provide a benchmark for evaluating optimization models. The model's flexibility suggests it can be adapted for personalized budget allocation based on user-defined financial goals. The research validates the use of constrained optimization for complex financial planning in resource-limited settings, directly applicable to Odin's budget recommendation engine."
  directly_justifies:
    - "Goal programming can optimize financial planning with conflicting objectives."
    - "The model achieves near-optimal solutions with minimal goal deviations."
    - "Prioritization of goals allows flexible decision-making in resource allocation."
    - "The approach is applicable to banking and personal finance contexts."
  limits:
    - "The model is demonstrated on a single bank's data and may not generalize."
    - "User preferences and behavioral factors are not incorporated."
    - "The study focuses on a bank, not individual personal finance management."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to the 'Budget Recommendation' domain (Topic 7.C) because it directly applies constrained optimization (goal programming) to balance multiple, conflicting financial objectives. It is also relevant to 'System Evaluation' (Topic 12.C) because it demonstrates an evaluation methodology based on comparing actual outcomes to target values and analyzing deviations. The paper touches on 'Savings & Debt Management' (Topic 13.A and 13.B) tangentially through its objectives but does not focus on user-level savings goals or debt management strategies. The following domains/topics were considered and rejected: 'Filipino Cultural Context' (Topics 2.A-2.D) because the case study is based on an Iraqi bank and does not address Filipino-specific practices; 'Expense Categorization' (Topic 3.A-3.C) because the paper does not deal with categorizing expenses; 'Behavioral Profiling' (Topics 5.A-5.C) because it does not involve user behavior or profiles; 'Anomaly Detection' (Topics 8.A-8.C) because it does not address detecting outliers. Overall, the paper is most relevant for its constrained optimization methodology, which can be adapted for Odin's budget recommendation algorithm."
limitations:
  - "The model is based on historical data from a single bank, limiting generalizability."
  - "The study does not consider dynamic changes in user behavior or financial conditions."
  - "Behavioral and psychological factors influencing financial decisions are not incorporated. [unacknowledged]"
  - "The approach is applied to banking rather than individual personal finance. [unacknowledged]"
remember_this:
  - "Goal programming balances conflicting financial objectives effectively."
  - "The model achieved near-optimal solutions with minimal deviations."
  - "Prioritization allows flexible resource allocation in financial planning."
  - "Multi-objective optimization is feasible for complex financial systems."
  - "The method can be adapted for personalized budget recommendation."
```
---


---

## Agent Instruction

If the agent reading this document believes further context about a paper is needed, it may request the original converted markdown file (with the '_marked' suffix) from the user for the relevant paper(s).
