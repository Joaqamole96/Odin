# Research Synthesis: Savings and Debt Management in PFMS

## Executive Summary

This synthesis examines the structural and behavioral dimensions of savings and debt management in Personal Finance Management Systems (PFMS), with particular attention to the Filipino context. The compiled literature reveals a fragmented but growing body of evidence: savings goal management is treated as a core PFMS function with entity structures centered on target amounts, deadlines, and progress tracking, yet detailed architectural specifications remain underdocumented. Debt management receives comparatively more attention in algorithm-specific papers, particularly around credit scoring, default prediction, and repayment optimization, but less on user-facing behavioral design.

Critically, the literature on **Filipino-specific savings goals and debt patterns** is rich but drawn primarily from survey-based studies rather than PFMS implementations. Filipino young professionals demonstrate strong saving intentions—particularly for emergency funds, retirement, and children's education—but face structural constraints including income volatility, debt cycles, and cultural obligations (utang na loob, family support) that complicate effective financial management. The gap between high financial literacy and poor financial behavior is a recurring theme across multiple Philippine studies.

For Odin, the key implications are: (1) savings goals must support emergency fund creation as a primary use case; (2) debt management must account for multiple loan sources (GSIS, banks, cooperatives, informal lenders) and automatic payroll deductions; (3) surplus handling is a critical but underexplored design area; and (4) behavioral profiling should distinguish between users with high knowledge but low action (the "conscious constraint" pattern).


## 1. Savings Goal Management

### 1.1 Entity Design

**Core attributes** of a savings goal entity in PFMS implementations, as evidenced across the compiled literature, include:

- **Target amount** – the numeric goal the user aims to save
- **Current balance / progress** – how much has been saved toward the goal
- **Target date / deadline** – the time horizon for achieving the goal
- **Goal name / description** – user-defined label for the goal
- **Category/type classification** – e.g., emergency fund, retirement, college, house, vacation

**Additional metadata** identified includes:
- **Goal milestones** – breaking down goals into discrete steps
- **Contribution history** – tracking individual contributions over time
- **Allocation percentage** – what portion of savings or deposits to allocate to each goal

The literature consistently treats savings goals as **time-bound, amount-anchored entities** with progress tracking as the primary user interaction mechanism. However, detailed specifications of priority levels, category tags, or automated contribution schedules are not extensively documented in the compiled papers.

### 1.2 Behavioral and Algorithmic Features

**Automated contribution calculation**: Evidence from PFMS implementations shows systems compute required periodic savings (daily/weekly/monthly) based on target amount, deadline, and current balance. More advanced systems use AI to automatically adjust savings plans based on real-time cash flow analysis. Patra et al. (2025) propose an LSTM-based forecasting approach that predicts future income and expenses to inform feasible savings contributions【58†L48-L53】.

**Progress visualization**: The literature indicates that progress bars and percentage completion are standard visualization methods. The "My Money Manager" app evaluation by Parameswaran & Saad (2025) found that visual progress tracking (pie charts, trend analysis) was highly rated by users【35†L66-L69】. Imawan et al. (2025) similarly found that visual goal progress was a key driver of user engagement【65†L48-L50】.

**Surplus handling**: This is a notable gap in the literature. While the BSP Consumer Expectations Survey (2026) implicitly addresses surplus through saving intention and income allocation data, and the "My Money Manager" app calculates monthly savings as income minus expenses【35†L50-L51】, there is **no explicit discussion** of carry-forward versus reset logic for end-of-period surplus in the compiled papers. This represents a significant design gap for Odin.

**Feasibility validation**: Patra et al. (2025) propose a Monte Carlo simulation approach to validate whether savings goals are achievable given income, expenses, and economic uncertainty【58†L54-L57】. The framework computes feasibility as the proportion of simulated scenarios where final wealth exceeds a target【58†L92-L94】. Tabak et al. (2025) further validate that financial planning behaviors—not just financial literacy—are the strongest predictors of reduced financial vulnerability【47†L33-L37】.

**Priority-based allocation**: The literature mentions that users can create multiple savings categories and set parameters such as allocation percentages. However, specific algorithms for ranking or prioritizing multiple goals and automating fund distribution are **not detailed** in the compiled papers.

### 1.3 Module Interactions

**Budgeting module**: Savings contributions are treated in several ways:
- As a **"pay yourself first" priority** – the 50/30/20 rule implementation in PFM apps
- As a **residual after expenses** – savings are what remains after all payments and expenses
- As an **automated sweep** – funds saved by the budget planner can be swept into savings

**Forecasting module**: The integration of forecasting and savings is well-documented. AI-powered PFM systems automatically adjust savings plans based on real-time cash flow analysis. LSTM-based forecasting predicts future income, expenses, and savings to inform goal feasibility【58†L48-L53】. The "My Money Manager" app uses 90-day spending patterns to generate savings recommendations【35†L62-L63】.

**Anomaly detection module**: The literature documents that anomaly detection can highlight unusual spending that may impact savings goals【35†L59-L61】. AI systems can also suggest budget adjustments or highlight unusual spending trends.

**Debt management module**: The interaction between savings and debt is addressed through **competing priority resolution**. Some systems allow users to "use funds saved by the budget planner to pay off debt, or sweep into savings". However, specific algorithms for balancing savings accumulation versus debt repayment are **not extensively detailed**.

**Dashboard/overview**: Savings progress is typically integrated into the main financial dashboard alongside cash summary, future balance, budget, and spending limits.


## 2. Debt Management

### 2.1 Entity Design

**Core attributes** of a debt entity in PFMS implementations, as evidenced across the literature:

- **Creditor name / lender** – who the debt is owed to
- **Debt type / product type** – classification of the loan
- **Outstanding balance** – current amount owed
- **Overdue amount** – past-due portion
- **Days past due** – delinquency duration
- **Interest rate** – cost of borrowing
- **Minimum payment** – required periodic payment
- **Due date** – payment deadline
- **Payment history** – record of past payments

**Taxonomy of debt types** supported includes:
- Credit cards
- Personal loans
- Housing loans / mortgages
- Auto loans
- Student loans
- BNPL (Buy Now, Pay Later) obligations

### 2.2 Behavioral and Algorithmic Features

**Repayment strategy selection**: The literature documents both **Avalanche** (highest interest first) and **Snowball** (smallest balance first) strategies. Flores (2025) found that Filipino respondents agreed on the importance of paying high-interest debt first【39†L56】. However, the behavioral outcomes associated with each strategy are not extensively evaluated in the compiled PFMS-specific papers.

**Automated repayment scheduling**: PFM tools offer strategies for paying off debts with easy-to-use widgets. However, detailed mechanisms for recommending or automating minimum payments, extra payments, and payoff timelines are **not extensively documented**.

**Hardship detection**: Mithun et al. (2025) address this through AI-powered credit scoring that predicts loan default risk, with employment type being a strong predictor. The study found that unemployed borrowers had the highest average default rate at 0.14. Esperanza et al. (2025) found that frequent usage of digital lending negatively predicts budget restraint【46†L61-L62】.

**Debt consolidation/simplification**: The literature mentions that PFM tools can help visualize multiple debts. The "My Money Manager" app provides financial summaries with tabs and filters for organized transaction review【35†L65-L66】. However, specific consolidation algorithms are **not detailed**.

**Interest modeling**: The literature does not provide explicit discussion of simple versus compound interest modeling approaches in PFMS debt modules. This is a notable gap.

### 2.3 Module Interactions

**Budgeting module**: Debt payments are typically treated as **fixed obligations** in budget allocation. The 50/30/20 rule implementation categorizes debt payments within the 20% savings/debt category. Esperanza et al. (2025) found that perceived quality of digital lending significantly predicts repayment behavior (PAY) and cautious borrowing (CAUTION)【46†L61-L63】.

**Savings module**: Competing priorities between debt repayment and savings accumulation are resolved through user choice, with some systems allowing funds to be directed to either. The BSP survey data shows that debt payments as a share of OFW remittance use declined to 27.2% in Q1 2026.

**Anomaly detection module**: Missed payments and rising balances are detected through AI-powered systems. Mithun et al. (2025) apply machine learning for detecting the anomaly of default. Bader & Haraty (2025) implemented anomaly detection using Isolation Forest, Local Outlier Factor (LOF), and One-Class SVM algorithms【29†L54-L56】.

**Forecasting module**: Income and expense forecasts inform debt repayment feasibility. Ayari et al. (2026) review LSTM and attention mechanisms for sequence-based credit prediction. Chikoore et al. (2026) demonstrate that adaptive credit scoring models can detect concept drift and maintain predictive performance in dynamic environments.

**User alerting/notification**: The literature documents various debt-related alerts:
- Upcoming due dates
- Missed payments
- Interest accumulation warnings
- Overdue notifications

Schwartz (2024) provides experimental evidence that **statement balance warnings** increase full credit card payments by 0.9-1.1%, while minimum payment warnings reduce delinquency by 6.9-8.8%【79†L48-L51】.


## 3. Filipino Savings Goals and Debt Patterns

### 3.1 Top Savings Goals of Filipinos

Based on empirical studies (particularly the BSP Consumer Expectations Survey and Metrobank surveys), the most common savings goals among Filipinos are:

| Rank | Savings Goal | Prevalence | Source |
|------|--------------|------------|--------|
| 1 | **Emergency fund / future needs** | ~21% | Metrobank survey 2025 |
| 2 | **Retirement** | ~23% | Sun Life Asia study |
| 3 | **Children's education** | ~20% | Metrobank survey 2025 |
| 4 | **Buying/improving a home** | ~16% | Metrobank survey 2025 |
| 5 | **Leisure/travel/concerts** | ~14% | Metrobank survey 2025 |
| 6 | **Financial stability** | ~23% (Metro Manila) | PhilStar survey |
| 7 | **Home-related expenses** | ~19% (Metro Manila) | PhilStar survey |

**Demographic variation**: Savings goals vary by location—in Metro Manila, financial stability is the top concern at 23%, followed by home-related expenses at 19% and travel/leisure at 17%. The BSP survey (2026) shows that saving intention varies by income group, with low-income groups having the most pessimistic outlook.

**Temporal perspective**: Retirement savings are viewed as a long-term goal, while emergency funds serve both short-term and medium-term needs. The BSP survey shows that 73.9% of saving households planned to save less than 10% of income in Q1 2026.

### 3.2 Filipino Debt Patterns and Behaviors

**Prevalence of debt**: 
- The debt ratio among Filipino households eased to 11% in Q4 2025
- Philippine household debt reached $60.9 billion as of September 2025
- 47% of Filipino adults maintain outstanding debt, predominantly for daily consumption【64†L39-L40】
- Teachers show particularly high debt levels: 83.1% maintain multiple concurrent loan portfolios

**Drivers of debt accumulation**:
- **Education and professional growth** – top reason for acquiring debt among teachers【61†L44】
- **Illness and death** – second top reason【61†L44】
- **House construction** – third top reason【61†L44】
- **Daily consumption smoothing** – 47% of Filipino adults maintain debt for daily consumption【64†L39-L40】
- **Family obligations** – cultural expectations to support extended family【61†L41】
- **BNPL adoption** – 35% of planned borrowing is through BNPL services

**Debt management behaviors**:
- **Automatic payroll deductions** (APDS) – the primary mechanism through which government loans are deducted from salaries
- **Multiple loan sources** – teachers borrow from GSIS, banks, cooperatives, and informal lenders【61†L41】
- **Debt cycling** – 83.1% of teachers maintain multiple concurrent loan portfolios
- **Informal borrowing** – 72% of Filipinos still prefer informal and unregulated lenders over banks
- **Loan addiction denial** – teachers generally deny being addicted to loans (M=1.96±0.77) despite high debt levels【49†L38】

**Cultural and structural factors**:
- **Utang na loob** – the cultural concept of debt of gratitude that influences financial decision-making
- **Family obligations** – the "tagapagtaguyod na anak" (breadwinner child) role is culturally embedded【44†L28-L31】
- **Paluwagan** – informal rotating savings and credit associations are common【74†L35-L36】
- **BNPL adoption** – driven by convenience and promotions among Filipino Gen Z【30†L35-L37】
- **"London" culture** – the practice of taking loans from multiple sources (loan dito, loan doon)【61†L30】

**Consequences of debt**:
- **Financial stress and anxiety** – freelancers and teachers report significant stress【57†L40-L41】
- **Savings displacement** – teachers have mean savings of only Php1,200, with 57.25% having no savings【61†L38】
- **Impact on retirement preparedness** – high financial acumen but only moderate retirement preparedness
- **Psychological burden** – borrowers experience debt stress that spills into family relationships【64†L44-L45】


## 4. Implications for Odin

### 4.1 Architectural Patterns

The dominant architectural pattern emerging from the literature is a **layered modular architecture** with:

1. **Data layer** – real-time data ingestion from multiple sources (bank APIs, user logs)【29†L52】
2. **AI/Intelligence layer** – predictive modeling, anomaly detection, and behavioral profiling【29†L53-L54】【58†L86-L88】
3. **Decision/Recommendation layer** – budget recommendations, savings feasibility validation【58†L88-L89】
4. **User interface layer** – mobile-first dashboards with progress visualization【35†L64-L66】

The **documented trade-offs** include:
- **Interpretability vs. performance** – deep learning models offer higher accuracy but reduced transparency
- **Complexity vs. usability** – advanced AI features require more data and computational resources【51†L60-L62】
- **Personalization vs. cold-start** – clustering and transfer learning can mitigate initial user data scarcity

### 4.2 Design Principles for Filipino Users

Based on the synthesis, the following design principles emerge:

1. **Emergency fund first** – Given that emergency funds are the top savings goal for ~21% of Filipinos, Odin should prioritize emergency fund creation as a default or strongly recommended goal.

2. **Debt consolidation and tracking** – With multiple loan sources (GSIS, banks, cooperatives, informal lenders)【61†L41】and automatic payroll deductions, Odin must support tracking of multiple debts and automatic deduction awareness.

3. **Cultural obligation accommodation** – The "tagapagtaguyod na anak" (breadwinner) role【44†L28-L31】and utang na loobmean Odin must allow for family support obligations in budget allocation.

4. **Surplus visibility** – Given that surplus is implied by saving intention databut not well-modeled in existing systems, Odin should make end-of-period surplus explicitly visible and actionable.

5. **Behavioral over knowledge** – Financial literacy does not always translate to behavior【37†L48-L49】; Odin should prioritize behavioral interventions (nudges, automated savings) over purely educational content.

### 4.3 Identified Gaps

The literature reveals several gaps relevant to Odin:

1. **Surplus handling logic** – No explicit discussion of carry-forward versus reset logic for end-of-period surplus exists in the compiled papers.
2. **Priority-based savings allocation** – Algorithms for ranking multiple savings goals and automating fund distribution are not detailed.
3. **Debt-savings trade-off algorithms** – How systems should optimally balance competing demands between debt repayment and savings accumulation is underdocumented.
4. **Filipino-specific PFMS evaluation** – No PFMS-specific evaluation studies using Filipino user data were identified in the compiled literature.
5. **Cold-start profiling for Filipino users** – How to initialize behavioral profiles for new Filipino users with limited data is not addressed.

### 4.4 Evaluation Evidence

Evidence regarding the effectiveness of savings and debt management features:

- **Goal setting** increases savings: robo-advisors with goal setting have an intention-to-treat effect of €20/month and a local average treatment effect of €60/month【94†L56-L57】
- **Overspending alerts** reduce daily spending by approximately 5%【94†L58】
- **Statement balance warnings** increase full credit card payments by 0.9-1.1%【79†L48】
- **Minimum payment warnings** reduce delinquency by 6.9-8.8%【79†L50】
- **Adaptive financial education** improves savings rates by 24.3% at 12-month follow-up【50†L36】
- **Financial behavior** explains 62.3% of the variability in financial well-being among Filipino young professionals

### 4.5 Specific Recommendations for Odin

**Savings Module**:
1. Implement **emergency fund** as a default or prioritized goal type
2. Support **multiple savings goals** with target amounts, deadlines, and progress tracking
3. Include **goal milestones** to break down large goals into achievable steps
4. Provide **automated contribution calculation** based on income, expenses, and target date
5. Implement **feasibility validation** using Monte Carlo or similar simulation【58†L54-L57】
6. Make **surplus** explicitly visible and actionable

**Debt Module**:
1. Support **multiple debt types**: credit cards, personal loans, housing loans, auto loans, student loans, BNPL
2. Track **automatic payroll deductions** (APDS) common in Philippine government employment
3. Offer both **Avalanche** (highest interest first) and **Snowball** (smallest balance first) strategies【39†L56】
4. Implement **hardship detection** for users unable to meet minimum payments
5. Provide **debt consolidation visualization** across multiple lenders
6. Include **statement balance warnings** to encourage full payments【79†L48】

**Module Interactions**:
1. **Savings-Budgeting**: Treat savings as a "pay yourself first" priority
2. **Savings-Forecasting**: Use LSTM or similar for income/expense prediction to inform savings feasibility【58†L48-L53】
3. **Savings-Anomaly**: Detect unusual spending that may impact savings goals【35†L59-L61】
4. **Debt-Budgeting**: Treat debt payments as fixed obligations with adjustable parameters
5. **Debt-Savings**: Allow users to choose between debt repayment and savings accumulation
6. **Debt-Anomaly**: Detect missed payments and rising balances【29†L54-L56】


## 5. Key Citations

| Paper | Contribution |
|-------|--------------|
| **Patra et al. (2025)** | LSTM forecasting + Monte Carlo feasibility validation for savings goals【58†L48-L57】 |
| **Tabak et al. (2025)** | Financial planning > financial literacy for reducing vulnerability【47†L33-L37】 |
| **Schwartz (2024)** | Statement balance warnings increase full payments by 0.9-1.1%【79†L48】 |
| **Bader & Haraty (2025)** | Anomaly detection using Isolation Forest, LOF, One-Class SVM【29†L54-L56】 |
| **Nayak & Jayakumar (2024)** | ML expense categorization (96.8% accuracy), forecasting (R²>0.89)【77†L48-L55】 |
| **Lusardi & Mitchell (2023)** | Financial literacy measurement (Big Three); 13% higher wealth per correct answer【93†L50】 |
| **BSP Consumer Expectations Survey (2026)** | Filipino saving intentions (12.4% index), OFW remittance allocation |
| **Mencias-Tabernilla (2023)** | Teacher debt patterns: 83.1% with multiple loans, mean savings Php1,200【61†L36-L38】 |
| **D'Acunto & Rossi (2023)** | Goal setting increases savings by €60/month【94†L56-L57】 |
| **Am-una (2026)** | Conscious constraint framework; budgeting most difficult behavior |
| **Parameswaran & Saad (2025)** | Fixed/variable expense categorization; anomaly detection; savings recommendations【35†L59-L69】 |
| **Imawan et al. (2025)** | Mobile PFM app with goal setting; 4.6/5 usability score【65†L48-L50】 |
| **Co & Centeno (2023)** | Family influence (10.16%) predicts banking intention; surplus as savings input【98†L55-L56】 |
| **Metrobank Survey (2025)** | Top Filipino savings goals: emergency funds (21%), retirement (23%), education (20%) |