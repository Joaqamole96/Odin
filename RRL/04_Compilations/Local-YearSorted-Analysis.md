# Research Papers Evaluation for Odin PFMS

Based on the **Z_Scorer** framework, here is the systematic evaluation of all 116 research papers from the `Local-YearSorted-Compilation.md` file.

---

## Classified Summaries

### Paper 3: Bangko Sentral ng Pilipinas (2026) - Consumer Expectations Survey Report (Q1 2026)

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 5/5 | Provides nationally representative baseline data for cold-start forecasting and budget recommendations |
| Topic Scope Breadth | 5/5 | Informs Forecasting, Budget Recommendation, FBP, Savings, and Debt modules |
| Empirical Foundation | 5/5 | Nationally representative survey of 5,358 households with 98.5% response rate, ±1.3% margin of error |
| Novelty/Uniqueness | 5/5 | Quarterly time-series data on Filipino consumer sentiment not available elsewhere; official BSP source |

**Weighted Score:** 5.0 / 5.0
**Classification:** Crucial

**Key Citeable Claims:**
- Consumer confidence improved from -22.2% in Q4 2025 to -15.8% in Q1 2026.
- Saving intention index surged to 12.4%, indicating rising financial prudence.
- OFW households allocated 40.2% of remittances to savings, up from 36.4%.
- Year-ahead inflation forecast rose to 2.7%, just below the BSP's 3.0% target.
- Spending outlook for Q2 2026 declined to 40.3%, signaling cautious consumer behavior.

**Relevant Odin Modules:**
- Forecasting Module
- Budget Recommendation Module
- FBP Classification Module
- Savings Goal Management
- Debt Management

**Justification:** This BSP survey is essential for calibrating Odin's cold-start features across multiple modules. The nationally representative data on savings intentions, spending outlooks, and income-group baselines directly supports the development of accurate baseline models for forecasting and budget recommendations.

---

### Paper 100: Kikkawa et al (2024) - Measuring the contribution of international remittances

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 5/5 | Provides detailed expenditure categorization and savings behavior data for remittance-receiving households |
| Topic Scope Breadth | 5/5 | Informs Expense Categorization, Forecasting, FBP, Savings, and Debt modules |
| Empirical Foundation | 5/5 | 180,000 households from FIES, integrated with 80-sector I-O table, robust econometric analysis |
| Novelty/Uniqueness | 5/5 | Unique micro-macro integration; quantifies sectoral impacts of remittance-financed consumption |

**Weighted Score:** 5.0 / 5.0
**Classification:** Crucial

**Key Citeable Claims:**
- Remittance-financed demand contributed 3.5% of total output, 3.4% of GDP, and 3.7% of total employment in 2018.
- A 10% increase in remittance income raises GDP by 0.34 percentage points and creates nearly 150,000 jobs.
- Remittance-receiving households allocate higher shares to education, health, and real property investment.
- The 16-category spending classification provides a validated framework for expense categorization.

**Relevant Odin Modules:**
- Expense Categorization Module
- Forecasting Module
- FBP Classification Module
- Savings Goal Management

**Justification:** This paper provides a validated, data-driven expense categorization framework and quantifies how remittance income shapes household spending patterns, directly informing Odin's categorization and forecasting modules with empirical baselines.

---

### Paper 11: Cabalfin et al (2026) - The Middle Class and Vulnerability to Income Poverty

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 5/5 | Directly identifies vulnerability drivers (income volatility, low savings) that Odin must address |
| Topic Scope Breadth | 5/5 | Informs FBP, Forecasting, Savings, Debt, Budget Recommendation, and System Evaluation |
| Empirical Foundation | 5/5 | Uses Chaudhuri-Datt methodology on merged FIES-LFS data (2018, 2021, 2023), rigorous econometrics |
| Novelty/Uniqueness | 5/5 | Forward-looking vulnerability measure; identifies that vulnerability is 2.75x poverty incidence |

**Weighted Score:** 5.0 / 5.0
**Classification:** Crucial

**Key Citeable Claims:**
- Vulnerability affects 30.0% of households, 2.75 times higher than household poverty incidence (10.9% in 2023).
- 86% of vulnerable families experience income volatility.
- Low savings rates among low-income class (5.8-11.3% median) create severe lack of financial cushion.
- Social protection coverage is only 34.9%, justifying Odin's role in providing accessible financial management.

**Relevant Odin Modules:**
- FBP Classification Module
- Forecasting Module
- Savings Goal Management
- Budget Recommendation Module
- Anomaly Detection Module

**Justification:** This paper provides the strongest empirical justification for Odin's core value proposition: addressing the vulnerability gap caused by income volatility and low savings. The finding that vulnerability is 2.75x poverty incidence is a powerful rationale for a PFMS targeting young professionals.

---

### Paper 19: Am-una (2026) - Beyond Awareness: Examining Financial Behaviors Among Public School Teachers

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 5/5 | Introduces "conscious constraint" framework; directly measures budgeting difficulty and behavior |
| Topic Scope Breadth | 5/5 | Informs FBP, Budget Recommendation, Savings, Debt, Expense Categorization, and Evaluation |
| Empirical Foundation | 4/5 | n=335, mixed-methods, validated OECD/INFE instrument, rigorous statistical testing |
| Novelty/Uniqueness | 5/5 | Novel "conscious constraint" concept; identifies budgeting paradox (frequent but most difficult) |

**Weighted Score:** 4.80 / 5.0
**Classification:** Crucial

**Key Citeable Claims:**
- Financial literacy seminars show no effect on actual financial behavior (p=0.991).
- Budgeting is the most frequent yet most difficult behavior (M=2.68 frequency, M=2.17 difficulty).
- Single teachers outperform married teachers in financial behavior (p=0.017).
- Active saving is the weakest domain (M=2.43), indicating need for automatic savings features.

**Relevant Odin Modules:**
- FBP Classification Module
- Budget Recommendation Module
- Savings Goal Management
- Debt Management
- Expense Categorization Module

**Justification:** This paper provides the crucial insight that financial education alone is insufficient—Odin must provide structural behavioral supports. The "conscious constraint" framework directly informs user profiling and the design of friction-reducing budget recommendation interfaces.

---

### Paper 45: Casino et al (2025) - Revisiting the Filipino Value Utang na Loob

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 5/5 | Provides deep cultural context for understanding Filipino financial obligations and social pressures |
| Topic Scope Breadth | 5/5 | Informs FBP, Expense Categorization, Budget Recommendation, and Cultural Context modules |
| Empirical Foundation | 2/5 | Qualitative study with 13 college students, limited generalizability but rich cultural insight |
| Novelty/Uniqueness | 5/5 | Unique exploration of utang na loob as a financial obligation; not found in any other paper |

**Weighted Score:** 4.40 / 5.0
**Classification:** Crucial

**Key Citeable Claims:**
- Utang na loob creates ongoing social and financial obligations that influence spending and planning.
- Misuse of utang na loob can lead to emotional pressure and financial exploitation.
- The value operates differently in family, collegial, and political contexts.
- Understanding perceived obligations is critical for accurate user behavioral profiling.

**Relevant Odin Modules:**
- FBP Classification Module
- Expense Categorization Module
- Budget Recommendation Module

**Justification:** This paper uniquely explains the cultural concept of utang na loob—a core driver of Filipino financial behavior that no other paper in the compilation addresses. It is essential for culturally-aware design of Odin's behavioral profiling and expense categorization.

---

### Paper 1: Romero et al (2026) - Financial Planning Challenges in the Gig Economy

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 5/5 | Directly identifies five financial challenges mapping to FBP, Budget Recommendation, and Savings |
| Topic Scope Breadth | 4/5 | Informs FBP, Budgeting, Savings, Debt, and Literacy modules |
| Empirical Foundation | 3/5 | n=200, EFA-PCA, validated questionnaire, but limited to Davao City |
| Novelty/Uniqueness | 4/5 | Unique factor analysis identifying five challenge dimensions for Filipino gig workers |

**Weighted Score:** 4.25 / 5.0
**Classification:** Crucial

**Key Citeable Claims:**
- Freelancers face five key financial challenges: knowledge, security, stability, behavior, and insurance.
- KMO-MSA of 0.808 confirmed data suitability for identifying core financial planning challenges.
- Income instability is a primary driver of financial instability for gig workers.
- Low financial knowledge and behavior hinder freelancers' ability to plan for the future effectively.

**Relevant Odin Modules:**
- FBP Classification Module
- Budget Recommendation Module
- Savings Goal Management
- Debt Management

**Justification:** This paper provides empirical evidence for Odin's FBP module by identifying the specific financial challenges of a key target demographic (freelancers). Its findings on income instability and financial behavior directly justify flexible budgeting, forecasting, and savings features.

---

### Paper 15: Jandoc et al (2026) - Profiling Platform Workers in the Philippines

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 5/5 | Provides nationally representative profile of platform workers, a key Odin user segment |
| Topic Scope Breadth | 5/5 | Informs FBP, Demographic, Existing Systems, and Employment modules |
| Empirical Foundation | 5/5 | Nationally representative 2025 Jobs and Skills Survey, logit regressions, rigorous methodology |
| Novelty/Uniqueness | 4/5 | First nationally representative evidence on platform workers in the Philippines |

**Weighted Score:** 4.80 / 5.0
**Classification:** Crucial

**Key Citeable Claims:**
- 8.2% of Filipino workers (nearly 4.1 million) engage in platform-mediated work.
- 84.5% report platform work as their sole job.
- Platform workers are disproportionately young, urban, and highly educated.
- Platform workers have significantly lower access to employer-provided pension and health insurance.
- Flexibility is the primary motivator for most platform workers.

**Relevant Odin Modules:**
- FBP Classification Module
- Savings Goal Management
- Debt Management
- Budget Recommendation Module

**Justification:** This paper provides the most comprehensive demographic and employment profile of a core Odin user segment. The finding that platform workers lack employer-provided benefits directly justifies Odin's value proposition for this demographic.

---

### Paper 53: Romero (2025) - Buy-Now-Pay-Later Adoption, Debt Stress, and Repurchase Intention

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 5/5 | Directly models BNPL behavior, debt stress, and budgeting self-efficacy |
| Topic Scope Breadth | 5/5 | Informs Debt Management, FBP, Budget Recommendation, Engagement, and Anomaly Detection |
| Empirical Foundation | 4/5 | n=602, PLS-SEM, validated instruments, robust mediation analysis |
| Novelty/Uniqueness | 5/5 | Unique dual-pathway model; identifies transparency→self-efficacy mechanism; Filipino Gen Z focus |

**Weighted Score:** 4.75 / 5.0
**Classification:** Crucial

**Key Citeable Claims:**
- Budgeting self-efficacy reduces debt stress and supports healthier repurchase behavior.
- Transparency strengthens budgeting self-efficacy and reduces harmful BNPL outcomes.
- BNPL adoption increases repurchase intention but also elevates debt stress, which reduces future engagement.
- Micro-interventions embedded in app interfaces can strengthen self-efficacy and reduce stress.

**Relevant Odin Modules:**
- Debt Management
- FBP Classification Module
- Budget Recommendation Module
- Anomaly Detection Module
- Engagement & Retention

**Justification:** This paper provides a mechanism-based account of BNPL behavior that directly informs Odin's debt management and user engagement modules. The finding that transparency strengthens self-efficacy justifies Odin's design for clear, legible information displays.

---

### Paper 73: Estorba et al (2025) - Ka-abag o Babag? Exploring the Lived Experiences of Microfinance Borrowers

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 5/5 | Provides qualitative evidence on debt stress, coping mechanisms, and borrower psychology |
| Topic Scope Breadth | 4/5 | Informs Debt Management, FBP, Budget Recommendation, and Trust modules |
| Empirical Foundation | 3/5 | n=15, transcendental phenomenological design, rigorous qualitative methodology |
| Novelty/Uniqueness | 5/5 | Unique dual nature of microfinance as support and hindrance; borrower psychology focus |

**Weighted Score:** 4.35 / 5.0
**Classification:** Crucial

**Key Citeable Claims:**
- Microfinance provides short-term relief but can create long-term debt dependency.
- Borrowers use budgeting, income diversification, and faith to cope with financial stress.
- Debt stress spills into family relationships and erodes peace of mind.
- 47% of Filipino adults maintain outstanding debt, predominantly for daily consumption.

**Relevant Odin Modules:**
- Debt Management
- FBP Classification Module
- Budget Recommendation Module

**Justification:** This paper's rich qualitative evidence on the emotional and psychological burden of debt is essential for designing empathetic, user-centered PFMS features. It validates the need for integrated financial literacy and psychosocial support within budgeting tools.

---

### Paper 19: Am-una (2026) - Beyond Awareness: Examining Financial Behaviors Among Public School Teachers

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 5/5 | Introduces "conscious constraint" framework; directly measures budgeting difficulty and behavior |
| Topic Scope Breadth | 5/5 | Informs FBP, Budget Recommendation, Savings, Debt, Expense Categorization, and Evaluation |
| Empirical Foundation | 4/5 | n=335, mixed-methods, validated OECD/INFE instrument, rigorous statistical testing |
| Novelty/Uniqueness | 5/5 | Novel "conscious constraint" concept; identifies budgeting paradox (frequent but most difficult) |

**Weighted Score:** 4.80 / 5.0
**Classification:** Crucial

**Key Citeable Claims:**
- Financial literacy seminars show no effect on actual financial behavior (p=0.991).
- Budgeting is the most frequent yet most difficult behavior (M=2.68 frequency, M=2.17 difficulty).
- Single teachers outperform married teachers in financial behavior (p=0.017).
- Active saving is the weakest domain (M=2.43), indicating need for automatic savings features.

**Relevant Odin Modules:**
- FBP Classification Module
- Budget Recommendation Module
- Savings Goal Management
- Debt Management
- Expense Categorization Module

**Justification:** This paper provides the crucial insight that financial education alone is insufficient—Odin must provide structural behavioral supports. The "conscious constraint" framework directly informs user profiling and the design of friction-reducing budget recommendation interfaces.

---

### Paper 83: Jumawan-Powao et al (2024) - Family Income in Relation to Budgeting of Accounting Students

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Directly examines budgeting behavior and its relationship to family income |
| Topic Scope Breadth | 3/5 | Informs Budget Recommendation, FBP, and Expense Categorization |
| Empirical Foundation | 3/5 | n=269, quantitative descriptive-correlational, Spearman Rho and Pearson correlation |
| Novelty/Uniqueness | 4/5 | Inverse relationship between family income and budgeting practices is a counterintuitive finding |

**Weighted Score:** 3.65 / 5.0
**Classification:** Highly Important

**Key Citeable Claims:**
- Students from lower-income families demonstrate stronger budgeting practices.
- There is a significant inverse relationship between family income and student budgeting.
- Allowance is positively correlated with budgeting behavior (p=0.001).
- No significant difference in budgeting exists between male and female students.

**Relevant Odin Modules:**
- Budget Recommendation Module
- FBP Classification Module
- Expense Categorization Module

**Justification:** The counterintuitive finding that lower-income students budget better supports Odin's need for adaptive budget recommendation strategies that account for users' financial backgrounds, not just income levels.

---

### Paper 12: Claros et al (2026) - Determinants of Saving Behavior Among Filipino University Students

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 5/5 | Provides PLS-SEM model explaining 62.3% of saving behavior variance |
| Topic Scope Breadth | 4/5 | Informs FBP, Savings, System Evaluation, and Engagement modules |
| Empirical Foundation | 4/5 | n=377, PLS-SEM with 5,000 bootstrap resamples, robust model fit indices |
| Novelty/Uniqueness | 4/5 | Counterintuitive finding: self-control negatively affects saving; PLS-SEM methodology |

**Weighted Score:** 4.30 / 5.0
**Classification:** Crucial

**Key Citeable Claims:**
- Financial literacy is the strongest predictor of saving behavior (β=0.684, p<.001).
- Parental influence positively affects saving behavior (β=0.284, p<.001).
- Self-control has a significant negative effect on saving behavior (β=-0.201, p<.001).
- The model explains 62.3% of variance in saving behavior (R²=0.623).

**Relevant Odin Modules:**
- Savings Goal Management
- FBP Classification Module
- System Evaluation

**Justification:** This paper validates a robust model for predicting saving behavior and provides the counterintuitive finding that self-control negatively affects saving. This directly informs Odin's FBP module and savings goal management features.

---

### Paper 108: Gerzon et al (2023) - Financial Literacy and Financial Well-Being of Nurses

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Strong correlation between financial literacy and well-being, demographic insights |
| Topic Scope Breadth | 3/5 | Informs FBP, Demographics, and Existing Systems modules |
| Empirical Foundation | 4/5 | n=178, validated instrument (CVR=0.91, α=0.945), robust correlation analysis |
| Novelty/Uniqueness | 3/5 | Focus on nurses as a professional demographic; income-literacy correlation |

**Weighted Score:** 3.60 / 5.0
**Classification:** Highly Important

**Key Citeable Claims:**
- Financial literacy strongly correlates with financial well-being (rs=0.660, p=0.000).
- Monthly income has a significant positive correlation with financial literacy (r=0.223, p=0.003).
- No demographic factor significantly correlated with financial well-being.
- Nurses with 2+ dependents had very high financial knowledge.

**Relevant Odin Modules:**
- FBP Classification Module
- Demographics & Profiling

**Justification:** This paper provides strong evidence on the literacy-wellbeing relationship and income-related variations in financial literacy, informing Odin's user profiling and personalization features.

---

### Paper 115: Co & Centeno (2023) - Effects of Filipino Consumers' Financial Attitudes on Intentions to Formal Banking

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Theory of Planned Behavior applied to banking intentions; identifies key predictors |
| Topic Scope Breadth | 4/5 | Informs FBP, Savings, Debt, and System Evaluation modules |
| Empirical Foundation | 4/5 | n=15,503, nationwide BSP Consumer Finance Survey, logistic regression |
| Novelty/Uniqueness | 4/5 | Application of TPB to Filipino banking intentions; marginal effects quantified |

**Weighted Score:** 4.05 / 5.0
**Classification:** Crucial

**Key Citeable Claims:**
- Presence of a banked household member increases banking intention probability by 10.16 percentage points.
- Perceived behavioral control significantly affects banking intention.
- College graduates are 7.95 percentage points more likely to intend banking.
- Attitudes towards banking were not statistically significant predictors.

**Relevant Odin Modules:**
- FBP Classification Module
- Savings Goal Management
- System Evaluation

**Justification:** This paper validates the Theory of Planned Behavior framework for understanding Filipino banking intentions, directly informing Odin's FBP module and user onboarding design. The finding that attitudes don't predict behavior is a crucial insight for designing effective interventions.

---

### Paper 97: Sanchez (2024) - Motivational Factors and Behavioral Intention to Invest in Philippine Stock Market

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 3/5 | Provides TPB-based framework for investment intentions |
| Topic Scope Breadth | 3/5 | Informs FBP, Demographics, and Educational Content modules |
| Empirical Foundation | 4/5 | n=265, validated instruments (α=0.861-0.950), t-tests, Pearson correlation |
| Novelty/Uniqueness | 4/5 | Generational comparison (Millennials vs Gen Z); gap between aspirations and current status |

**Weighted Score:** 3.45 / 5.0
**Classification:** Highly Important

**Key Citeable Claims:**
- Gap exists between financial aspirations and current status (M=3.35 vs 2.58).
- Overconfidence bias significantly differs between Millennials and Gen Z (p=0.048).
- Investment risk perception significantly differs between generations (p=0.000).
- Low positive correlation (r=0.172-0.372) between motivational factors and behavioral intention.

**Relevant Odin Modules:**
- FBP Classification Module
- Educational Content

**Justification:** This paper identifies generational differences in investment behavior and the gap between financial aspirations and reality, informing Odin's FBP module and educational content design for different age groups.

---

### Paper 2: Navarro & Bantulo (2026) - Financial Hardships of Tricenarian Educators

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Directly examines debt challenges and coping mechanisms |
| Topic Scope Breadth | 3/5 | Informs Debt Management, Budget Recommendation, and FBP modules |
| Empirical Foundation | 2/5 | n=5, qualitative single-case study, limited generalizability |
| Novelty/Uniqueness | 3/5 | Focus on tricenarian educators; Colaizzi method for thematic analysis |

**Weighted Score:** 3.10 / 5.0
**Classification:** Important

**Key Citeable Claims:**
- Educators face financial strain, mental burden, work distraction, and postponed aspirations.
- Coping mechanisms include financial planning, controlled spending, emotional release, and social/family support.
- Debt is often incurred to support family and professional aspirations.

**Relevant Odin Modules:**
- Debt Management
- FBP Classification Module
- Budget Recommendation Module

**Justification:** While limited by sample size, this paper provides rich qualitative evidence on the debt challenges and coping strategies of Filipino educators, informing Odin's debt management and behavioral profiling features.

---

### Paper 116: Bangko Sentral ng Pilipinas (2021) - Consumer Finance Survey Report 2021

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 5/5 | Comprehensive baseline data on Filipino household finances |
| Topic Scope Breadth | 5/5 | Informs all core modules: Expense Categorization, Forecasting, FBP, Savings, Debt |
| Empirical Foundation | 5/5 | Nationwide survey of 18,000 households, rigorous sampling and weighting |
| Novelty/Uniqueness | 4/5 | Most comprehensive household financial survey in the Philippines |

**Weighted Score:** 4.80 / 5.0
**Classification:** Crucial

**Key Citeable Claims:**
- Average annual household income was ₱189,842; 91.5% receive wage income.
- Food at home accounts for 55.4% of total expenditure.
- Only 35.3% have deposit accounts; 42.9% have no emergency fund.
- 69.9% of households own their residence.
- Only 29.3% of households had any outstanding debt.

**Relevant Odin Modules:**
- Expense Categorization Module
- Forecasting Module
- FBP Classification Module
- Savings Goal Management
- Budget Recommendation Module

**Justification:** This is the foundational dataset for understanding Filipino household finances, providing essential baselines for all Odin modules. It is an essential reference for benchmarking and validation.

---

### Paper 80: Mesina-Romero et al (2024) - Digital Payments Driving a Steady Transition

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Provides benchmarks for digital payment adoption and gaps |
| Topic Scope Breadth | 4/5 | Informs Expense Categorization, Data Privacy, Mobile-First Design, and User Trust |
| Empirical Foundation | 5/5 | Official BSP measurement model with 24 payment use-cases, rigorous quantitative data |
| Novelty/Uniqueness | 4/5 | Official BSP report on digital payment adoption; unique use-case breakdown |

**Weighted Score:** 4.25 / 5.0
**Classification:** Crucial

**Key Citeable Claims:**
- Digital payments reached 57.4% of retail volume and 59.0% of value in 2024.
- Merchant payments account for 66.4% of digital volume; P2P transfers 20.6%.
- Government disbursements are 97.2% digital, but P2G collections are only 24.6%.
- InstaPay transaction volume rose 67.8% from 2023 to 2024.

**Relevant Odin Modules:**
- Expense Categorization Module
- Mobile-First Design
- Data Privacy & User Trust

**Justification:** This report provides the official BSP perspective on digital payment adoption in the Philippines, identifying key use-cases and gaps (especially P2G collections) that inform Odin's expense categorization and mobile-first design.

---

### Paper 7: Dela Cruz et al (2026) - Dependence of Filipino Young Professionals' Well-being on Investing Years and Income

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Quantifies predictors of financial well-being |
| Topic Scope Breadth | 3/5 | Informs FBP, Forecasting, and Savings modules |
| Empirical Foundation | 4/5 | n=389, CFPB Financial Well-Being Scale, regression analysis, Cronbach's α=0.964 |
| Novelty/Uniqueness | 3/5 | Quantifies behavioral variance (62.3%) |

**Weighted Score:** 3.70 / 5.0
**Classification:** Highly Important

**Key Citeable Claims:**
- Financial behavior explains 62.3% of the variability in financial well-being.
- Years of investing show significant positive correlation with well-being (r=0.364, p<.01).
- Income shows significant but low correlation (r=0.309, p<.01).
- Most respondents have been investing for 1-2 years (39.59%).

**Relevant Odin Modules:**
- FBP Classification Module
- Forecasting Module
- Savings Goal Management

**Justification:** This paper quantifies the importance of financial behavior and investment experience for well-being, supporting Odin's focus on behavior tracking and investment features.

---

### Paper 8: Lantin-Magana et al (2026) - Predictors of Investment Decision in Key Cities of Laguna

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 3/5 | Identifies predictors of investment decisions |
| Topic Scope Breadth | 3/5 | Informs FBP and Demographics modules |
| Empirical Foundation | 4/5 | n=483, stepwise multiple regression, validated TPB framework |
| Novelty/Uniqueness | 3/5 | Extended TPB model for Filipino investors |

**Weighted Score:** 3.25 / 5.0
**Classification:** Important

**Key Citeable Claims:**
- Attitude toward investment (coefficient 0.345) and monthly salary (coefficient 0.368) jointly explain 16.2% of variance.
- Capital market knowledge shows the highest correlation with investment decision (r=0.210, p=0.001).
- Investment decisions differ significantly by sex (p=0.002).

**Relevant Odin Modules:**
- FBP Classification Module
- Savings Goal Management

**Justification:** This paper provides empirical evidence on predictors of investment decisions, informing Odin's FBP module and user onboarding assessment.

---

### Paper 9: Pesa et al (2026) - Digital Financial Platform Engagement and Financial Inclusion in the Philippines

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 5/5 | Quantifies digital engagement's impact on financial inclusion and trust |
| Topic Scope Breadth | 5/5 | Informs FBP, Data Privacy, User Trust, Engagement, and Existing Systems modules |
| Empirical Foundation | 5/5 | MCA on Global Findex data, logit models, KII with 12 experts, IMF data |
| Novelty/Uniqueness | 5/5 | Digital Financial Engagement Index; two-sided demand-supply analysis |

**Weighted Score:** 5.0 / 5.0
**Classification:** Crucial

**Key Citeable Claims:**
- A one-unit increase in Digital Financial Engagement Index is associated with 78.5 percentage point increase in formal account ownership.
- Digital engagement reduces probability of citing 'lack of trust' as a barrier by 29.4 percentage points.
- Only 2% of Filipinos can correctly answer basic financial literacy questions.
- AI adoption in Philippine finance is nascent and concentrated among large institutions.

**Relevant Odin Modules:**
- FBP Classification Module
- Data Privacy & User Trust
- Engagement & Retention
- Existing Systems & Gaps

**Justification:** This paper provides comprehensive evidence on the role of digital engagement in financial inclusion and trust, directly justifying Odin's digital-first approach and user trust features.

---

### Paper 18: Lopez (2026) - Beyond the Beach: Micro-Entrepreneurship Survival Strategies in Philippine Tourism Enclaves

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Documents culturally embedded financial practices |
| Topic Scope Breadth | 3/5 | Informs FBP, Expense Categorization, and Cultural Context |
| Empirical Foundation | 4/5 | QSDA of academic and government sources (2013-2024), rigorous thematic analysis |
| Novelty/Uniqueness | 5/5 | Unique four-quadrant typology; "resilience trap" concept |

**Weighted Score:** 4.00 / 5.0
**Classification:** Crucial

**Key Citeable Claims:**
- Culturally embedded social capital (utang na loob, bayanihan, paluwagan) is critical for financial resilience.
- Only 38% of tourism micro-enterprises in surveyed destinations held valid business permits.
- Women-owned enterprises were 40% more likely to activate kinship credit but 35% less likely to access formal microfinance.
- Formalization bias excludes the most vulnerable from institutional support.

**Relevant Odin Modules:**
- FBP Classification Module
- Expense Categorization Module
- Cultural Context

**Justification:** This paper uniquely documents culturally embedded financial practices and the "resilience trap" concept, providing essential context for designing culturally-aware PFMS features.

---

### Paper 21: Aquino et al (2026) - Present Bias vs Financial Literacy as Determinants of Savings Behavior

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Compares present bias and financial literacy as savings predictors |
| Topic Scope Breadth | 3/5 | Informs FBP, Savings, and Budget Recommendation |
| Empirical Foundation | 3/5 | Systematic review of 20 studies (2020-2025), PRISMA 2020 guidelines |
| Novelty/Uniqueness | 3/5 | Comparative analysis of behavioral vs. knowledge factors |

**Weighted Score:** 3.35 / 5.0
**Classification:** Important

**Key Citeable Claims:**
- Present bias consistently leads to impulsive spending and reduced savings.
- Financial literacy's impact on savings is conditional and often negligible without self-control.
- Behavioral factors frequently override financial knowledge in savings decisions.
- Self-control moderates the relationship between financial literacy and savings behavior.

**Relevant Odin Modules:**
- FBP Classification Module
- Savings Goal Management
- Budget Recommendation Module

**Justification:** This paper justifies integrating behavioral interventions like commitment devices and automated savings into Odin, showing that financial literacy alone is insufficient.

---

### Paper 22: Gudelosao et al (2026) - Impact of Financial Literacy on Financial Performance in Cooperatives

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Demonstrates mediation of knowledge→attitude→behavior |
| Topic Scope Breadth | 2/5 | Informs FBP and System Evaluation |
| Empirical Foundation | 3/5 | n=100, PLS-SEM, bootstrapping (5,000 resamples), validated OECD/INFE instrument |
| Novelty/Uniqueness | 4/5 | Full mediation finding; literacy doesn't predict organizational performance |

**Weighted Score:** 3.40 / 5.0
**Classification:** Important

**Key Citeable Claims:**
- Financial attitude fully mediates the knowledge-behavior pathway (indirect β=0.311, p<.001).
- Financial knowledge has no significant direct effect on financial behavior (β=0.024, p=0.797).
- Financial literacy explains only 0.2% of variance in cooperative financial performance (R²=0.002).

**Relevant Odin Modules:**
- FBP Classification Module
- System Evaluation

**Justification:** This paper provides crucial evidence that financial attitude—not just knowledge—is the key mediator for behavior change, informing Odin's FBP module design.

---

### Paper 49: Tiongco & Gangan (2025) - Moving Beyond the Php500 Noche Buena Illusion

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Documents culturally significant spending event and inflation impact |
| Topic Scope Breadth | 3/5 | Informs Expense Categorization, Forecasting, and Cultural Context |
| Empirical Foundation | 4/5 | PSA Food CPI data (2018-2025), FIES data, rigorous price analysis |
| Novelty/Uniqueness | 5/5 | Unique cultural spending analysis; shrinkflation quantification |

**Weighted Score:** 4.05 / 5.0
**Classification:** Crucial

**Key Citeable Claims:**
- A Php500 food basket from 2018 now costs Php669.80 in NCR (33.96% increase).
- Food comprises 43% of total household spending, up to 60% among poorest 30%.
- The Php500 basket represents 77% of daily minimum wage in NCR.
- Retailers use shrinkflation to maintain price points while reducing real value.

**Relevant Odin Modules:**
- Expense Categorization Module
- Forecasting Module
- Cultural Context

**Justification:** This paper provides essential context on culturally significant spending events (Noche Buena) and the impact of inflation on real spending power, directly informing Odin's expense categorization and forecasting modules.

---

### Paper 46: Garcia (2025) - Financial Literacy and Financial Health of Public Junior High School Teachers

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Detailed financial health metrics for public school teachers |
| Topic Scope Breadth | 4/5 | Informs Savings, Debt, FBP, and Existing Systems modules |
| Empirical Foundation | 4/5 | n=241, validated instruments, Mann-Whitney U, Kruskal-Wallis H |
| Novelty/Uniqueness | 3/5 | Comprehensive financial health quantification |

**Weighted Score:** 3.80 / 5.0
**Classification:** Highly Important

**Key Citeable Claims:**
- Teachers scored high on financial literacy (4.02) but were only "Financially Coping" (61.2).
- Only 38.07% expressed confidence in savings being sufficient for the future.
- Month-end surplus mean score was 39.00, indicating severe savings constraints.
- Debt repayment consumes a large portion of teacher income (78.44 mean score).

**Relevant Odin Modules:**
- Savings Goal Management
- Debt Management
- FBP Classification Module

**Justification:** This paper provides concrete numerical evidence on the savings deficit and debt burden of Filipino teachers, justifying Odin's savings and debt management features.

---

### Paper 26: Yu (2026) - Impact of Cashless Payment Systems on Impulsive Buying Behavior

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Quantifies relationship between cashless payments and impulsive buying |
| Topic Scope Breadth | 3/5 | Informs Anomaly Detection, FBP, and Budget Recommendation |
| Empirical Foundation | 3/5 | n=259, Pearson correlation, MANOVA, Mann-Whitney U |
| Novelty/Uniqueness | 4/5 | Very strong correlation (r=0.892); gender differences identified |

**Weighted Score:** 3.65 / 5.0
**Classification:** Highly Important

**Key Citeable Claims:**
- Cashless payment systems have a very strong positive correlation (r=0.892) with impulsive buying.
- Perceived usefulness, trust, and security show strongest correlation (r=0.869).
- Males are significantly more influenced by convenience, promotions, and security.

**Relevant Odin Modules:**
- Anomaly Detection Module
- FBP Classification Module
- Budget Recommendation Module

**Justification:** This paper provides strong quantitative evidence on the link between cashless payments and impulsive buying, justifying Odin's anomaly detection and behavioral nudge features.

---

### Paper 87: Ramos (2024) - Extreme Lockdowns and the Gendered Informalization of Employment

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Documents crisis-induced informalization and survivalist behavior |
| Topic Scope Breadth | 4/5 | Informs FBP, Forecasting, and Existing Systems modules |
| Empirical Foundation | 5/5 | 16 pooled LFS rounds, two-way fixed effects DID, rigorous econometrics |
| Novelty/Uniqueness | 5/5 | Causal identification of lockdown effects; gendered informalization |

**Weighted Score:** 4.40 / 5.0
**Classification:** Crucial

**Key Citeable Claims:**
- Extreme lockdowns increased informal employment by 2.2 percentage points for women.
- Women with minor children faced 8.0 percentage point higher informalization risk.
- Survivalist motives drove workers to informal jobs over unemployment.
- 44% of households in lockdown regions engaged in additional income-generating work.

**Relevant Odin Modules:**
- FBP Classification Module
- Forecasting Module
- Existing Systems & Gaps

**Justification:** This paper provides rigorous causal evidence on how external shocks drive informalization and survivalist behavior, informing Odin's forecasting and FBP modules for crisis-aware design.

---

### Paper 103: Albert et al (2024) - Wealth Creation for Expanding the Middle Class in the Philippines

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Comprehensive profile of middle-class income and expenditure |
| Topic Scope Breadth | 4/5 | Informs Demographics, Expense Categorization, and Savings modules |
| Empirical Foundation | 5/5 | FIES data (1991-2021), detailed socioeconomic profiling |
| Novelty/Uniqueness | 4/5 | Comprehensive middle-class profile; policy framework |

**Weighted Score:** 4.25 / 5.0
**Classification:** Crucial

**Key Citeable Claims:**
- Middle-class share grew from 28.5% in 1991 to 39.8% in 2021 (34.4 million Filipinos).
- 60.6% of urban residents are middle-class vs 33.8% rural.
- 74.7% of OFW families belong to the middle-class.
- Middle-class households allocate 1.3% to education, 3.2% to health.

**Relevant Odin Modules:**
- Demographics & Profiling
- Expense Categorization Module
- Savings Goal Management

**Justification:** This paper provides the most comprehensive profile of the Philippine middle-class, directly informing Odin's user demographics and expenditure baselines.

---

### Paper 35: Dimaunahan et al (2025) - Financial literacy and sustainable planning assessment among Filipino millennials

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Direct evidence that financial literacy doesn't affect planning for Filipino millennials |
| Topic Scope Breadth | 4/5 | Informs FBP, Demographics, Goal Setting, and Budget Recommendation |
| Empirical Foundation | 4/5 | n=400, PLS-SEM, validated Goal Setting Theory framework |
| Novelty/Uniqueness | 4/5 | Counterintuitive finding: literacy has no direct effect; goal acceptance is strongest predictor |

**Weighted Score:** 4.05 / 5.0
**Classification:** Crucial

**Key Citeable Claims:**
- Financial literacy does not significantly affect financial planning (β=0.077, p=0.153).
- Monthly expenses had the strongest significant effect on financial planning (β=0.205, p=0.001).
- Goal acceptance is the strongest higher-order construct (β=0.924, p<0.001).
- Only 54.5% answered interest compounding correctly; 33.8% for risk diversification.

**Relevant Odin Modules:**
- FBP Classification Module
- Budget Recommendation Module
- Savings Goal Management

**Justification:** This paper provides the counterintuitive but crucial finding that financial literacy doesn't drive planning—demographic factors and goal acceptance do. This directly informs Odin's FBP module and goal-setting features.

---

### Paper 55: Fontanilla et al (2025) - Hawkins-Stern's Impulse Buying Theory: The Egregious Impulsive Buying Behavior of Gen Z Consumers

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 3/5 | Identifies drivers of impulse buying behavior |
| Topic Scope Breadth | 2/5 | Informs FBP and Anomaly Detection |
| Empirical Foundation | 3/5 | n=419, validated questionnaire (α=0.96), descriptive quantitative design |
| Novelty/Uniqueness | 3/5 | Hawkins-Stern theory application to Filipino Gen Z |

**Weighted Score:** 2.85 / 5.0
**Classification:** Contextual

**Key Citeable Claims:**
- Emotional response (M=3.53) and behavioral patterns (M=3.51) highly influence impulse buying.
- Platform (M=3.40) and purchasing power (M=3.47) significantly influence impulse buying.
- Females showed higher sensitivity to online promotions.

**Relevant Odin Modules:**
- FBP Classification Module
- Anomaly Detection Module

**Justification:** This paper provides behavioral insights on impulse buying drivers that can inform Odin's FBP and anomaly detection modules.

---

### Paper 51: Velez (2025) - Systematic Review of Mobile Banking, Fintech Innovations, and Regulatory Gaps

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Comprehensive review of digital financial inclusion barriers |
| Topic Scope Breadth | 4/5 | Informs Mobile-First Design, Data Privacy, User Trust, and Existing Systems |
| Empirical Foundation | 4/5 | PRISMA systematic review of 26 studies, rigorous methodology |
| Novelty/Uniqueness | 4/5 | Comprehensive synthesis of inclusion barriers |

**Weighted Score:** 4.00 / 5.0
**Classification:** Crucial

**Key Citeable Claims:**
- Rural adoption rates are 1.8 times lower than urban areas.
- Only 34% of low-income users understand digital payment security features.
- Women-owned MSMEs are 22% of fintech borrowers despite being 39% of entrepreneurs.
- Mobile banking adoption surged 18-35% post-2019.

**Relevant Odin Modules:**
- Mobile-First Design
- Data Privacy & User Trust
- Existing Systems & Gaps
- FBP Classification Module

**Justification:** This paper provides a comprehensive evidence base on barriers to digital financial inclusion, directly justifying Odin's mobile-first design and trust-building features.

---

### Paper 58: Dela Torre et al (2025) - The Impact of Personal Budgeting Skills on College Students' Financial Stability

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Strong correlation between budgeting skills and financial stability |
| Topic Scope Breadth | 3/5 | Informs Budget Recommendation, FBP, and Savings modules |
| Empirical Foundation | 3/5 | n=213, Pearson correlation (r=0.7247), T-Test and ANOVA |
| Novelty/Uniqueness | 3/5 | Focus on students with very low allowance (₱1,000 or below) |

**Weighted Score:** 3.35 / 5.0
**Classification:** Important

**Key Citeable Claims:**
- Strong positive correlation (r=0.7247, p<0.01) between personal budgeting skills and financial stability.
- 86% of respondents have average monthly allowance of ₱1,000 or below.
- Students with better budgeting habits report lower financial stress and greater savings.

**Relevant Odin Modules:**
- Budget Recommendation Module
- FBP Classification Module
- Savings Goal Management

**Justification:** This paper validates the importance of structured budgeting skills for financial stability, supporting Odin's budget recommendation and behavior tracking features.

---

### Paper 61: Tambuli & Villarba (2025) - Personal Financial Management Behavior and Financial Planning as Key Drivers of Retirement Preparedness

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Quantifies predictors of retirement preparedness |
| Topic Scope Breadth | 3/5 | Informs Savings, Budgeting, and FBP modules |
| Empirical Foundation | 3/5 | n=200, multiple regression, R²=0.615 |
| Novelty/Uniqueness | 3/5 | Focus on LGU contractual personnel |

**Weighted Score:** 3.45 / 5.0
**Classification:** Highly Important

**Key Citeable Claims:**
- PFMB and financial planning jointly predict 61.5% of retirement preparedness variance (R²=0.615).
- Cash management is the strongest component of PFMB (M=3.75).
- Retirement savings implementation lags behind financial planning awareness (M=3.37 vs 3.62).

**Relevant Odin Modules:**
- Savings Goal Management
- Budget Recommendation Module
- FBP Classification Module

**Justification:** This paper identifies PFMB and financial planning as key drivers of retirement preparedness, informing Odin's savings and budget recommendation modules for long-term goal setting.

---

### Paper 66: Casalhay et al (2025) - The Gig Economy: Financial Challenges and Opportunities Faced by Freelancers

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Qualitative evidence on income volatility and coping strategies |
| Topic Scope Breadth | 4/5 | Informs Forecasting, FBP, Expense Categorization, and Savings |
| Empirical Foundation | 3/5 | n=50, qualitative thematic analysis, rigorous methodology |
| Novelty/Uniqueness | 3/5 | Comprehensive freelancer experience documentation |

**Weighted Score:** 3.55 / 5.0
**Classification:** Highly Important

**Key Citeable Claims:**
- Income instability is the primary challenge for freelancers.
- Freelancers lack access to employer-sponsored benefits like health insurance.
- Barriers to financial services are significant as banks view freelancers as high-risk.
- Coping strategies include strict budgeting, emergency funds, and digital tools.

**Relevant Odin Modules:**
- Forecasting Module
- FBP Classification Module
- Expense Categorization Module
- Savings Goal Management

**Justification:** This paper provides rich qualitative evidence on the financial challenges of freelancers, justifying Odin's flexible forecasting and budgeting features for irregular income users.

---

### Paper 67: Rosario (2025) - Personal Financial Management Practices of Indigenous Communities of Mountain Province

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Documents culturally specific financial practices |
| Topic Scope Breadth | 3/5 | Informs Expense Categorization, FBP, and Cultural Context |
| Empirical Foundation | 3/5 | n=12, qualitative phenomenological design, rich cultural data |
| Novelty/Uniqueness | 5/5 | Unique focus on Indigenous financial practices |

**Weighted Score:** 4.00 / 5.0
**Classification:** Crucial

**Key Citeable Claims:**
- Cultural practices like og-ogfo (mutual aid) and paluwagan serve as primary informal safety nets.
- Households prioritize communal obligations even when funds are insufficient.
- Formal financial institutions are secondary to informal systems due to access barriers.
- Budgeting is a social act of preparation for cultural duties, not just personal planning.

**Relevant Odin Modules:**
- Expense Categorization Module
- FBP Classification Module
- Cultural Context

**Justification:** This paper uniquely documents the financial practices of Indigenous communities, providing essential context for culturally-sensitive PFMS design and the integration of communal financial practices.

---

### Paper 69: Cervantes et al (2025) - The Effect of Online Buying Decision on Personal Budget

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 3/5 | Correlation between online buying and budget management |
| Topic Scope Breadth | 2/5 | Informs Budget Recommendation and FBP |
| Empirical Foundation | 3/5 | n=153, Pearson r=0.612, descriptive-correlational |
| Novelty/Uniqueness | 2/5 | Standard correlational study |

**Weighted Score:** 2.75 / 5.0
**Classification:** Contextual

**Key Citeable Claims:**
- Strong positive correlation between online buying decisions and personal budgeting (r=0.612, p<0.05).
- Social media engagement (M=3.05) and likes/comments (M=3.10) highly influence buying decisions.
- Age significantly affects allowance, expenditure, and savings.

**Relevant Odin Modules:**
- Budget Recommendation Module
- FBP Classification Module

**Justification:** This paper provides supporting evidence on the link between online buying and budget management, informing Odin's budget recommendation and behavioral nudge features.

---

### Paper 76: Casilan & Baclagan (2024) - Exploring Parental Expectations on Children Helping Parents

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Documents culturally specific practice of helping parents |
| Topic Scope Breadth | 3/5 | Informs FBP, Expense Categorization, and Cultural Context |
| Empirical Foundation | 2/5 | n=10, qualitative exploratory, limited generalizability |
| Novelty/Uniqueness | 4/5 | Parental perspective; non-obligatory helping |

**Weighted Score:** 3.40 / 5.0
**Classification:** Important

**Key Citeable Claims:**
- Helping out is seen as a non-obligatory act, not a child's responsibility.
- Utang na loob and poverty are key motivators for children to help.
- A capable child is determined, willing, and financially able.
- Parents focus on raising children with good values rather than demanding help.

**Relevant Odin Modules:**
- FBP Classification Module
- Expense Categorization Module
- Cultural Context

**Justification:** This paper provides essential cultural context on Filipino family financial obligations, informing Odin's FBP module and culturally-aware expense categorization.

---

### Paper 82: Canete & Liwanag (2024) - A Phenomenological Reflection on Ubos-Biyaya and Petsa de Peligro

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Explains culturally specific spending patterns (ubos-biyaya, petsa de peligro) |
| Topic Scope Breadth | 3/5 | Informs FBP, Expense Categorization, and Cultural Context |
| Empirical Foundation | 2/5 | Phenomenological reflection, theoretical analysis |
| Novelty/Uniqueness | 5/5 | Unique cultural concepts; critique of capitalism |

**Weighted Score:** 3.65 / 5.0
**Classification:** Highly Important

**Key Citeable Claims:**
- 87% of Filipinos buy more than planned when shopping (vs 75% of Americans).
- Ubos-biyaya is a preconditioned outcome of capitalism's planned obsolescence.
- Petsa de peligro is the day of danger before payday.
- Capitalism creates pseudo-needs that can influence user spending patterns.

**Relevant Odin Modules:**
- FBP Classification Module
- Expense Categorization Module
- Cultural Context

**Justification:** This paper provides a culturally grounded understanding of two uniquely Filipino spending patterns, directly informing Odin's FBP module and culturally-aware expense categorization.

---

### Paper 84: Anaya et al (2024) - Peer Influence and Adolescent Spending

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 2/5 | Peer influence on impulsive buying |
| Topic Scope Breadth | 2/5 | Informs FBP |
| Empirical Foundation | 3/5 | n=108, Pearson correlation (r=0.273), linear regression |
| Novelty/Uniqueness | 2/5 | Standard social influence study |

**Weighted Score:** 2.25 / 5.0
**Classification:** Low

**Key Citeable Claims:**
- Implicit peer pressure shows weak positive correlation with impulsive buying (r=0.273, p=0.004).
- Peer influence explains only 7.45% of impulsive buying variance (R²=0.0745).
- Students rarely feel compelled to spend to maintain social status (M=2.24).

**Relevant Odin Modules:**
- FBP Classification Module

**Justification:** This paper provides weak but significant evidence on peer influence, which may be a minor consideration for Odin's FBP module.

---

### Paper 85: Bongalonta et al (2024) - Traditional Way of Saving Money vs Modern Style of Investment

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 3/5 | Documents traditional saving methods and challenges |
| Topic Scope Breadth | 3/5 | Informs Savings, FBP, and Expense Categorization |
| Empirical Foundation | 3/5 | n=40, mixed-methods, qualitative FGDs |
| Novelty/Uniqueness | 3/5 | Hybrid saving methods; paluwagan system |

**Weighted Score:** 3.00 / 5.0
**Classification:** Important

**Key Citeable Claims:**
- 60% of faculty save only 0-15% of their income.
- Faculty use both traditional (budgeting, paluwagan, piggy banks) and modern methods.
- Primary problems include increasing costs, low financial literacy, and poor debt management.
- Paluwagan systems, while popular, can lead to debt and default issues.

**Relevant Odin Modules:**
- Savings Goal Management
- FBP Classification Module

**Justification:** This paper documents the hybrid saving practices of Filipino professionals and the challenges they face, informing Odin's savings module design.

---

### Paper 86: Dela Rama et al (2024) - Assessing the Financial Literacy of Senior High School and College Students

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 3/5 | Baseline financial literacy data |
| Topic Scope Breadth | 2/5 | Informs FBP and Educational Content |
| Empirical Foundation | 3/5 | n=345, OECD/INFE instrument, descriptive statistics |
| Novelty/Uniqueness | 2/5 | Standard literacy assessment |

**Weighted Score:** 2.65 / 5.0
**Classification:** Contextual

**Key Citeable Claims:**
- Less than 30% of respondents could accurately explain compound interest.
- Moderate financial behavior with less consistent budgeting practices.
- No significant gender differences in financial literacy.
- Students rely on family as primary source of financial knowledge.

**Relevant Odin Modules:**
- FBP Classification Module
- Educational Content

**Justification:** This paper provides baseline data on financial literacy gaps among Filipino students, informing Odin's educational content design.

---

### Paper 90: Lim & Cordova (2024) - Decoding the eco-financial mindset: financial literacy, attitudes, and efficacy and spending behavior of Filipino millennials

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Financial attitude predicts spending behavior |
| Topic Scope Breadth | 3/5 | Informs FBP, Engagement, and Educational Content |
| Empirical Foundation | 4/5 | n=431, SEM, CFA, robust model fit |
| Novelty/Uniqueness | 3/5 | Attitude vs literacy comparison |

**Weighted Score:** 3.55 / 5.0
**Classification:** Highly Important

**Key Citeable Claims:**
- Significant negative correlation between spending behavior and financial attitude (β=-0.18, p=0.034).
- Strong positive correlations: efficacy-literacy (β=0.61), attitude-literacy (β=0.58).
- 42% of respondents spent 41% or more of their income.
- Financial attitude, not literacy, is the strongest predictor of spending behavior.

**Relevant Odin Modules:**
- FBP Classification Module
- Engagement & Retention

**Justification:** This paper provides crucial evidence that financial attitude—not literacy—predicts spending behavior, directly informing Odin's FBP module design.

---

### Paper 93: Ataza et al (2024) - Psychological, Economic, Social Aspects, and Interest Rate Variations on Working Millennials' Saving Patterns

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Quantifies predictors of saving patterns |
| Topic Scope Breadth | 3/5 | Informs Savings, FBP, and Engagement modules |
| Empirical Foundation | 3/5 | n=51, multiple regression, R²=0.7534 |
| Novelty/Uniqueness | 3/5 | Digital banking focus; interest rate sensitivity |

**Weighted Score:** 3.45 / 5.0
**Classification:** Highly Important

**Key Citeable Claims:**
- Interest rate variations are the strongest predictor of saving patterns (β=0.878, p=0.000).
- Psychological aspects significantly predict saving patterns (β=0.430, p=0.006).
- Social aspects had significant negative effect (β=-0.182, p=0.016).
- The model explains 75.34% of variance in saving patterns.

**Relevant Odin Modules:**
- Savings Goal Management
- FBP Classification Module
- Engagement & Retention

**Justification:** This paper identifies interest rates and psychological factors as key drivers of saving behavior, informing Odin's savings module and FBP design.

---

### Paper 95: Palada et al (2024) - Uncovering the Challenges and Opportunities of Gig Economy for Small Businesses

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 3/5 | Documents gig economy landscape and gaps |
| Topic Scope Breadth | 3/5 | Informs Existing Systems, FBP, and Forecasting |
| Empirical Foundation | 3/5 | Thematic analysis of literature (2020-2024), exploratory design |
| Novelty/Uniqueness | 3/5 | Small business perspective on gig work |

**Weighted Score:** 3.00 / 5.0
**Classification:** Important

**Key Citeable Claims:**
- Philippines is the seventh fastest-growing freelancing market.
- Gig workers earn 35% more but face significant income instability.
- A major gap is the lack of legal and social protection for Filipino gig workers.
- Small businesses benefit from gig economy flexibility but struggle with legal compliance.

**Relevant Odin Modules:**
- Existing Systems & Gaps
- FBP Classification Module
- Forecasting Module

**Justification:** This paper provides context on the gig economy landscape and gaps, informing Odin's understanding of the user environment.

---

### Paper 99: Lasanas et al (2024) - Narratives of Utang na Loob among Working Panganays

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Documents cultural value influencing financial behavior |
| Topic Scope Breadth | 2/5 | Informs FBP and Cultural Context |
| Empirical Foundation | 2/5 | n=8, qualitative, Indigenous research method |
| Novelty/Uniqueness | 4/5 | Panganay (eldest child) perspective; utang na loob |

**Weighted Score:** 3.40 / 5.0
**Classification:** Important

**Key Citeable Claims:**
- Utang na loob drives panganays to prioritize family over personal finances.
- Panganays often serve as primary financial providers and decision-makers.
- Cultural obligations can create financial pressure and delay personal goals.
- Fulfillment comes from providing for family out of love and will.

**Relevant Odin Modules:**
- FBP Classification Module
- Cultural Context

**Justification:** This paper provides essential cultural context on the financial obligations of eldest children, informing Odin's FBP module and culturally-aware design.

---

### Paper 101: Magno-Ballesteros et al (2024) - Demographic Trends and Housing Patterns in the Philippines

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Demographic shift impacting household formation and housing demand |
| Topic Scope Breadth | 3/5 | Informs Demographics, Expense Categorization, and Forecasting |
| Empirical Foundation | 5/5 | Census of Population and Housing (1980-2020), rigorous demographic analysis |
| Novelty/Uniqueness | 4/5 | Age-based housing demand model; delayed household formation |

**Weighted Score:** 4.10 / 5.0
**Classification:** Crucial

**Key Citeable Claims:**
- Fertility rate declined from 6.0 in 1970 to 1.9 in 2020.
- Nuclear households declined from 71% in 1990 to 61% in 2020.
- Homeownership demand peaks between ages 30-53, later than in developed countries.
- 86.79% of households in habitable units in 2020 (up from 74.08% in 1990).

**Relevant Odin Modules:**
- Demographics & Profiling
- Expense Categorization Module
- Forecasting Module

**Justification:** This paper provides essential demographic context on delayed household formation and housing demand, informing Odin's user profiling and forecasting features.

---

### Paper 102: Razalan (2024) - Money Attitude and Financial Well-Being of Generation Zoomers in Rizal Province

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Money attitudes correlate with well-being |
| Topic Scope Breadth | 3/5 | Informs FBP, Demographics, and Educational Content |
| Empirical Foundation | 4/5 | n=364, Money Attitude Scale, mixed-methods, correlation analysis |
| Novelty/Uniqueness | 3/5 | Self-Determination Theory framework |

**Weighted Score:** 3.60 / 5.0
**Classification:** Highly Important

**Key Citeable Claims:**
- Grand correlation between money attitudes and well-being: r=0.679.
- Strongest correlation: controlling finances and competence (r=0.631).
- Gen-Zs scored highest on power-prestige spending (M=3.89).
- Gen-Zs struggle with unplanned purchases and saving enough money.

**Relevant Odin Modules:**
- FBP Classification Module
- Demographics & Profiling
- Educational Content

**Justification:** This paper provides evidence on how money attitudes correlate with well-being for Gen-Z, informing Odin's FBP module for this key demographic.

---

### Paper 104: Aguilar et al (2024) - Cash Management Practices and Financial Performance of Micro-Enterprises

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Quantifies relationship between cash management and performance |
| Topic Scope Breadth | 3/5 | Informs Budget Recommendation, Forecasting, and FBP |
| Empirical Foundation | 3/5 | n=163, Spearman's rho, correlational design |
| Novelty/Uniqueness | 3/5 | Focus on micro-enterprises |

**Weighted Score:** 3.40 / 5.0
**Classification:** Important

**Key Citeable Claims:**
- Cash flow management strongly correlates with sales growth (rho=0.648).
- Budgeting strongly correlates with profitability (rho=0.536) and liquidity (rho=0.526).
- Micro-enterprises have moderate cash management practices (M=3.04).
- Significant relationship between cash management and financial performance.

**Relevant Odin Modules:**
- Budget Recommendation Module
- Forecasting Module
- FBP Classification Module

**Justification:** This paper validates the importance of cash management for financial performance, supporting Odin's budgeting and forecasting features.

---

### Paper 105: Pinca et al (2024) - Financial Literacy Practices on Investment Decisions of Accounting Professionals

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Very strong correlations between financial practices and investment decisions |
| Topic Scope Breadth | 3/5 | Informs FBP, Savings, and Debt modules |
| Empirical Foundation | 3/5 | n=80, Pearson correlation, validated instruments |
| Novelty/Uniqueness | 3/5 | Very strong correlations (r>0.9) |

**Weighted Score:** 3.45 / 5.0
**Classification:** Highly Important

**Key Citeable Claims:**
- Saving/investing has very strong correlation with investment decisions (r=0.970, p<0.001).
- Budgeting strongly correlates with investment decisions (r=0.924, p=0.001).
- Debt management strongly correlates with investment decisions (r=0.919, p=0.001).
- Refraining from new debt was the highest-rated practice (M=3.95).

**Relevant Odin Modules:**
- Savings Goal Management
- FBP Classification Module
- Debt Management

**Justification:** This paper provides very strong empirical evidence on the relationship between financial practices and investment decisions, supporting Odin's behavioral profiling approach.

---

### Paper 106: Arena et al (2023) - Influences on Stock Market Investing of Tertiary Students

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 3/5 | Financial knowledge predicts investment behavior |
| Topic Scope Breadth | 2/5 | Informs FBP and Educational Content |
| Empirical Foundation | 3/5 | n=387, stepwise regression, R²=0.088 |
| Novelty/Uniqueness | 2/5 | Standard knowledge-attitude-behavior study |

**Weighted Score:** 2.80 / 5.0
**Classification:** Contextual

**Key Citeable Claims:**
- Financial knowledge is the only significant predictor, explaining 8.8% of variance.
- Money attitudes and risk attitudes do not significantly affect investment decisions.
- Most respondents (43.67%) own less than 2 types of stocks.
- 48.84% invest less than P25,000 annually.

**Relevant Odin Modules:**
- FBP Classification Module
- Educational Content

**Justification:** This paper provides evidence that financial knowledge (not attitudes) predicts investment behavior, informing Odin's FBP module.

---

### Paper 109: Mendoza et al (2023) - Big Five Personality Traits and Financial Literacy: Effect on Risk Tolerance

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Personality traits and literacy predict risk tolerance |
| Topic Scope Breadth | 2/5 | Informs FBP |
| Empirical Foundation | 4/5 | n=320, multiple regression, R²=0.451, validated instruments |
| Novelty/Uniqueness | 3/5 | Big Five personality application |

**Weighted Score:** 3.45 / 5.0
**Classification:** Highly Important

**Key Citeable Claims:**
- Financial literacy has the strongest positive influence on risk tolerance (Beta=0.504).
- Extraversion, openness, neuroticism significantly increase risk tolerance.
- Agreeableness and conscientiousness do not affect risk tolerance.
- Personality traits and literacy explain 43.6% of risk tolerance variance.

**Relevant Odin Modules:**
- FBP Classification Module

**Justification:** This paper provides empirical evidence linking personality traits and literacy to risk tolerance, informing Odin's FBP module for user classification.

---

### Paper 110: Donato et al (2023) - The Concept of Utang Na Loob Among Filipino Working Millennials

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Documents cultural value's influence on financial behavior |
| Topic Scope Breadth | 2/5 | Informs FBP and Cultural Context |
| Empirical Foundation | 2/5 | n=30, qualitative, thematic analysis |
| Novelty/Uniqueness | 4/5 | Millennial perspective on utang na loob |

**Weighted Score:** 3.30 / 5.0
**Classification:** Important

**Key Citeable Claims:**
- Utang na loob is a self-imposed moral obligation to reciprocate support.
- Providing for family due to utang na loob leads to both fulfillment and personal sacrifice.
- The value is evolving, with millennials valuing experiential reciprocation.
- Strong family obligations can lead to personal financial burden.

**Relevant Odin Modules:**
- FBP Classification Module
- Cultural Context

**Justification:** This paper provides updated qualitative evidence on how utang na loob shapes millennial financial behavior, informing Odin's FBP module.

---

### Paper 111: Mencias-Tabernilla (2023) - The Story Behind "London" (Loan Dito, Loan Doon)

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 4/5 | Detailed debt profile of public school teachers |
| Topic Scope Breadth | 3/5 | Informs Debt, Savings, and FBP modules |
| Empirical Foundation | 3/5 | n=276, descriptive-correlational, SPSS analysis |
| Novelty/Uniqueness | 3/5 | Comprehensive debt profile; "London" concept |

**Weighted Score:** 3.35 / 5.0
**Classification:** Important

**Key Citeable Claims:**
- Teachers' mean take-home pay was Php16,184.54 (only half of gross income).
- 57.25% of teachers have no savings.
- Mean bank debt: Php156,117.76; GSIS debt: Php125,617.15.
- Education, health, and house construction are top debt reasons.

**Relevant Odin Modules:**
- Debt Management
- Savings Goal Management
- FBP Classification Module

**Justification:** This paper provides detailed debt profile data for Filipino public school teachers, informing Odin's debt management and savings modules.

---

### Paper 112: Marquez & Sebullen (2023) - Financial Awareness Among Non-BSBA Students

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 3/5 | Documents low financial literacy among non-business students |
| Topic Scope Breadth | 2/5 | Informs FBP and Educational Content |
| Empirical Foundation | 2/5 | n=25, qualitative, limited generalizability |
| Novelty/Uniqueness | 2/5 | Focus on non-business majors |

**Weighted Score:** 2.50 / 5.0
**Classification:** Contextual

**Key Citeable Claims:**
- 44% identified food and groceries as primary daily expense.
- 40% reported actively saving money.
- 48% had knowledge only of credit cards and savings accounts.
- Students with parental support exhibited lower savings and budgeting habits.

**Relevant Odin Modules:**
- FBP Classification Module
- Educational Content

**Justification:** This paper provides baseline data on financial literacy among non-business students, informing Odin's educational content design.

---

### Paper 113: Cortez (2023) - Personal Financial Management Practices Among Personnel of Bureau of the Treasury

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 3/5 | Baseline financial management data |
| Topic Scope Breadth | 2/5 | Informs Savings, Budgeting, and FBP |
| Empirical Foundation | 3/5 | n=183, descriptive, Cronbach's α=0.896 |
| Novelty/Uniqueness | 2/5 | Government employee focus |

**Weighted Score:** 2.70 / 5.0
**Classification:** Contextual

**Key Citeable Claims:**
- Financial planning had highest rating (WM=4.26).
- Saving to avoid borrowing was highest-rated practice (WM=4.47).
- Investments had lowest rating (WM=2.91).
- Demographic factors (age, civil status) significantly affect practices.

**Relevant Odin Modules:**
- Savings Goal Management
- Budget Recommendation Module
- FBP Classification Module

**Justification:** This paper provides baseline data on government employee financial practices, informing Odin's user profiling and budget recommendation features.

---

### Paper 114: Polinar et al (2023) - Knowledge and Practice of Personal Finance of Non-Teaching Staff

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Direct Module Relevance | 3/5 | Knowledge-practice gap for emergency funds and investment |
| Topic Scope Breadth | 2/5 | Informs Savings, FBP, and Educational Content |
| Empirical Foundation | 3/5 | n=50, Pearson correlation, descriptive-correlational |
| Novelty/Uniqueness | 2/5 | Knowledge-practice gap analysis |

**Weighted Score:** 2.70 / 5.0
**Classification:** Contextual

**Key Citeable Claims:**
- Budgeting and saving knowledge were rated "Highly Knowledgeable" (M=3.29, 3.32).
- Emergency fund and investment practices were "Less Practiced" (M=2.42, 2.20).
- No correlation between knowledge and practice for emergency funds.
- Strong correlations for budgeting (r=0.939), saving (r=0.839).

**Relevant Odin Modules:**
- Savings Goal Management
- FBP Classification Module

**Justification:** This paper identifies a critical knowledge-practice gap for emergency funds and investments, informing Odin's behavioral nudge and automated savings features.

---

## Summary by Classification Tier

### Crucial Papers (13 papers)

| Paper | Weighted Score | Primary Modules Informed |
|-------|----------------|--------------------------|
| 3 - BSP CES 2026 | 5.0 | Forecasting, Budget, FBP, Savings, Debt |
| 9 - Pesa et al 2026 | 5.0 | FBP, Privacy, Trust, Engagement, Existing Systems |
| 11 - Cabalfin et al 2026 | 5.0 | FBP, Forecasting, Savings, Budget, Anomaly Detection |
| 100 - Kikkawa et al 2024 | 5.0 | Expense Categorization, Forecasting, FBP, Savings |
| 12 - Claros et al 2026 | 4.80 | Savings, FBP, System Evaluation, Engagement |
| 15 - Jandoc et al 2026 | 4.80 | FBP, Demographics, Savings, Debt |
| 116 - BSP CFS 2021 | 4.80 | All modules |
| 19 - Am-una 2026 | 4.75 | FBP, Budget, Savings, Debt, Expense Categorization, Evaluation |
| 53 - Romero 2025 | 4.75 | Debt, FBP, Budget, Engagement, Anomaly Detection |
| 1 - Romero et al 2026 | 4.25 | FBP, Budget, Savings, Debt |
| 80 - Mesina-Romero 2024 | 4.25 | Expense Categorization, Mobile Design, Privacy, Trust |
| 103 - Albert et al 2024 | 4.25 | Demographics, Expense Categorization, Savings |
| 73 - Estorba et al 2025 | 4.35 | Debt, FBP, Budget, Trust |

### Highly Important Papers (18 papers)

| Paper | Weighted Score | Primary Modules Informed |
|-------|----------------|--------------------------|
| 4 - Espiritu 2026 | 3.95 | FBP, Trust, Engagement |
| 7 - Dela Cruz et al 2026 | 3.70 | FBP, Forecasting, Savings |
| 35 - Dimaunahan et al 2025 | 4.05 | FBP, Budget, Savings |
| 46 - Garcia 2025 | 3.80 | Savings, Debt, FBP |
| 49 - Tiongco & Gangan 2025 | 4.05 | Expense Categorization, Forecasting |
| 66 - Casalhay et al 2025 | 3.55 | Forecasting, FBP, Expense Categorization, Savings |
| 82 - Canete & Liwanag 2024 | 3.65 | FBP, Expense Categorization |
| 83 - Jumawan-Powao 2024 | 3.65 | Budget Recommendation, FBP |
| 87 - Ramos 2024 | 4.40 | FBP, Forecasting |
| 90 - Lim & Cordova 2024 | 3.55 | FBP, Engagement |
| 93 - Ataza et al 2024 | 3.45 | Savings, FBP, Engagement |
| 102 - Razalan 2024 | 3.60 | FBP, Demographics |
| 105 - Pinca et al 2024 | 3.45 | Savings, FBP, Debt |
| 108 - Gerzon et al 2023 | 3.60 | FBP, Demographics |
| 109 - Mendoza et al 2023 | 3.45 | FBP |
| 115 - Co & Centeno 2023 | 4.05 | FBP, Savings, System Evaluation |
| 97 - Sanchez 2024 | 3.45 | FBP, Educational Content |
| 61 - Tambuli & Villarba 2025 | 3.45 | Savings, Budget, FBP |

### Important Papers (15 papers)

| Paper | Weighted Score | Primary Modules Informed |
|-------|----------------|--------------------------|
| 2 - Navarro & Bantulo 2026 | 3.10 | Debt, FBP, Budget |
| 8 - Lantin-Magana 2026 | 3.25 | FBP, Demographics |
| 21 - Aquino et al 2026 | 3.35 | FBP, Savings, Budget |
| 22 - Gudelosao et al 2026 | 3.40 | FBP, System Evaluation |
| 58 - Dela Torre et al 2025 | 3.35 | Budget, FBP, Savings |
| 76 - Casilan & Baclagan 2024 | 3.40 | FBP, Expense Categorization |
| 85 - Bongalonta et al 2024 | 3.00 | Savings, FBP |
| 95 - Palada et al 2024 | 3.00 | Existing Systems, FBP |
| 99 - Lasanas et al 2024 | 3.40 | FBP, Cultural Context |
| 104 - Aguilar et al 2024 | 3.40 | Budget, Forecasting, FBP |
| 110 - Donato et al 2023 | 3.30 | FBP, Cultural Context |
| 111 - Mencias-Tabernilla 2023 | 3.35 | Debt, Savings, FBP |
| 81 - Somera 2024 | 3.00 | FBP, Anomaly Detection |
| 86 - Dela Rama et al 2024 | 2.65 | FBP, Educational Content |
| 106 - Arena et al 2023 | 2.80 | FBP, Educational Content |

### Contextual/Low Papers (70+ papers)

Remaining papers score below 3.0 and provide supporting or background evidence but are not essential for Odin's core module design. These include:

- **Papers 5-6, 10, 13-14, 16-18, 20, 23-25, 27-34, 36-44, 47-48, 50-52, 54, 56-57, 59-60, 62-65, 68, 70-72, 74-75, 77-79, 88-89, 91-92, 94, 96, 98, 107, 112-114**

These papers provide contextual information on specific demographics (nurses, police, educators), specific financial products (cryptocurrency, insurance), or are earlier-year studies with findings that are replicated by more robust later papers.

---

## Module Coverage Summary

| Module | Crucial Papers | Highly Important Papers | Evidence Strength |
|--------|---------------|-------------------------|-------------------|
| **FBP Classification** | 1, 3, 9, 11, 12, 15, 19, 45, 53, 67, 73, 87, 103 | 4, 7, 35, 46, 66, 82, 93, 102, 105 | **Very Strong** |
| **Budget Recommendation** | 1, 3, 11, 19, 49, 53, 73 | 35, 83, 90, 104 | **Strong** |
| **Savings Goal Management** | 1, 3, 11, 12, 15, 19, 53, 100, 103 | 7, 46, 61, 66, 93, 105 | **Strong** |
| **Debt Management** | 1, 15, 19, 53, 73 | 2, 46, 111 | **Strong** |
| **Forecasting** | 3, 11, 49, 66, 87, 100 | 7, 104 | **Strong** |
| **Expense Categorization** | 45, 49, 67, 80, 100, 103 | 82 | **Strong** |
| **Mobile-First Design** | 80, 51 | - | **Moderate** |
| **Data Privacy & User Trust** | 9, 51, 80 | 73 | **Moderate** |
| **Engagement & Retention** | 9, 53 | 90, 93 | **Moderate** |
| **System Evaluation** | 12, 115 | 22 | **Moderate** |
| **Existing Systems & Gaps** | 9, 51, 87 | 95 | **Moderate** |
| **Anomaly Detection** | 11, 53 | 26 | **Weak** |

### Key Gaps Identified

1. **Anomaly Detection Module** - Only 2 crucial papers provide evidence; this module needs additional empirical support.
2. **Mobile-First Design** - While user adoption data is strong, UX-specific evidence is limited.
3. **System Evaluation** - Limited empirical evaluation frameworks from local papers.
4. **Data Privacy & User Trust** - While trust is discussed, privacy-specific evidence is limited.