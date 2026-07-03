# Compiled Research Summaries

**Total Papers:** 50

**Note:** Included papers positions 301 to 350, Sorted by year.

---

## Paper 1: Robba et al_summarized.md

**Source File:** `Robba et al_summarized.md`

```yaml
paper_id: 10.3389/frbhe.2024.1369261
designation: international
title: In search of socially responsible investors: a Latent Profile Analysis
authors: Robba, M.; Sorgente, A.; Iannello, P.
year: 2024
venue: Frontiers in Behavioral Economics
odin_topics:
  - 5.A
  - 5.B
  - 5.C
tldr: Identifies five investor profiles using Latent Profile Analysis, finding that sustainable investors are characterized by high SRI knowledge, risk appetite, positive attitudes, personal norms, and environmental concern.
problem_and_motivation: Literature lacks systematic research on the psychological and behavioral profile of socially responsible investors. Understanding these characteristics is essential for designing inclusive financial products and identifying barriers to sustainable investing.
approach:
  - Cross-sectional online survey of 1,002 representative Italian consumers aged 18-54 with quota sampling for gender, age, education, and region.
  - Latent Profile Analysis (LPA) used to identify subgroups based on 9 determinants: financial literacy, SRI knowledge, risk tolerance, perceived consumer effectiveness, trust, personal norms, perceived behavioral control, environmental concern, and connectedness to nature.
  - Model selection based on VLMR-LRT, LMR-LRT, and information criteria (AIC, BIC, SABIC); 5-profile solution selected for parsimony and interpretability.
  - Profiles associated with current SRI investment via chi-square test and with willingness to invest via one-way ANOVA with Tukey’s HSD post-hoc tests.
findings:
  - "num: Five distinct consumer profiles were identified, with only the 'fully equipped' profile (22.7% of sample) significantly associated with current SRI investment."
  - "num: The 'fully equipped' profile showed 11.9% current SRI ownership vs. 4.7% sample average."
  - "num: The 'environmental concern' profile had 0% current SRI investors and the lowest willingness to invest (M=3.03)."
  - "num: The 'fully equipped' profile had the highest willingness to invest in SRI (M=5.32), followed by 'equipped but risk avoidant' (M=4.65)."
  - "num: ANOVA showed large effect size (partial η2 = 0.301) for profile membership on SRI investment intention."
  - Psychological characteristics (attitudes, personal norms, perceived behavioral control, environmental concern) play a key role alongside classical financial determinants.
  - Risk tolerance and SRI knowledge are critical for converting intention into actual SRI investment.
  - Environmental concern alone, without financial literacy and risk appetite, is insufficient to drive sustainable investment.
key_figures_tables:
  - "Figure 1: Factor score means for nine determinants across five profiles → Fully equipped profile scores highest on all determinants except financial literacy."
  - "Table 6: Cross-tabulation of profiles with SRI investing → Fully equipped profile has largest positive adjusted residual (5.8)."
  - "Table 4: Relative fit indices for LPA models → 5-profile solution selected based on inferential tests and parsimony."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: LPA
    definition: Latent Profile Analysis, a clustering technique identifying subgroups based on variable configurations.
  - term: SRI
    definition: Socially Responsible Investment, investment strategy combining financial performance with social responsibility.
  - term: TPB
    definition: Theory of Planned Behavior, framework explaining behavior through attitudes, subjective norms, and perceived behavioral control.
  - term: ESG
    definition: Environmental, Social, and Governance criteria used to evaluate corporate sustainability.
  - term: PCE
    definition: Perceived Consumer Effectiveness, belief that individual actions can positively impact the environment.
  - term: IINS
    definition: Illustrated Inclusion of Nature in Self scale, measuring connectedness to nature.
critical_citations:
  - "[Ajzen, 1991] — Foundational TPB framework for behavioral prediction."
  - "[Riedl and Smeets, 2017] — Key evidence on investor motivations for SRI."
  - "[Wins and Zwergel, 2016] — Examined determinants of sustainable fund investment."
  - "[Gutsche and Zwergel, 2020] — Identified investment barriers and labeling effects."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly uses LPA to identify distinct investor behavioral profiles.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: high
      justification: Profiles represent configurations of psychological and financial traits relevant to cold-start user modeling.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Demonstrates person-centered LPA classification methodology for financial behavior.
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Italian sample provides general demographic profiling approach but not Filipino-specific.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: contextual
      justification: Behavioral determinants framework is transferable but not applied to Filipino context.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: low
      justification: Cultural factors not investigated; Italian context limits direct applicability.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: low
      justification: No seasonal spending analysis; paper focuses on investment, not consumption.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: low
      justification: Not about expense categorization; investment decision model only.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: Provides general behavioral framework but no specific budget recommendation content.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: No discussion of data privacy or security.
  contribution: |
    This paper provides a validated behavioral profiling methodology (Latent Profile Analysis) for Odin's user classification module. The finding that psychological determinants (personal norms, attitudes, perceived behavioral control) are as important as financial literacy for investment behavior informs Odin's preference elicitation design. The identification of an intention-behavior gap linked to risk aversion and knowledge deficits directly justifies Odin's educational and onboarding features for new users. The profile-based segmentation approach offers a template for Odin's cold-start user typing based on limited initial inputs. Finally, the integration of TPB with financial determinants provides a theoretical foundation for Odin's behavioral prediction engine.
  directly_justifies:
    - "Latent Profile Analysis can classify users into distinct behavioral profiles for personal finance systems."
    - "Psychological determinants including personal norms and attitudes significantly influence financial decision-making."
    - "Knowledge deficits and risk aversion are key barriers that can create an intention-behavior gap."
    - "Environmental concern alone is insufficient to drive sustainable financial behavior without financial literacy."
  limits:
    - "Cross-sectional data in Italy limits generalizability to Filipino young professionals."
    - "SRI context (investment) differs from PFMS context (spending, budgeting)."
    - "Perceived knowledge measures may not correlate with objective financial literacy."
  mapping_rationale: |
    All 12 functional domains and their 28 associated topic codes were systematically scanned against the paper's content. Domains 5 (Behavioral Profiling), 1 (Demographic/Behavioral context), and 7 (Budget Recommendation) were flagged as potentially relevant. Topic 5.A (Financial Behavioral Profiles) was assigned high relevance as the paper's LPA directly identifies investor behavioral profiles—a methodology directly transferable to Odin's user classification. Topic 5.B (Profile Dynamics and Cold-Start) was also high because the paper demonstrates how configurations of limited variables (psychological and financial) can classify users, directly informing cold-start user typing. Topic 5.C (Classification Approaches) was high as LPA is a robust classification method demonstrated in financial behavior context. Topic 1.A and 1.C were assigned contextual because while the demographic and behavioral framework is relevant, the sample is Italian, not Filipino. Topic 7.A was contextual for providing behavioral theory but not budget-specific algorithms. Domains 2 (Cultural Practices), 3 (Expense Categorization), 6 (Forecasting), 8 (Anomaly Detection), 9 (Mobile Design), 10 (Privacy), 11 (Retention), 12 (Evaluation), and 13 (Savings/Debt) were rejected as the paper does not address these areas—no seasonal patterns, no forecasting, no privacy/trust in digital systems, no expense categorization, and no savings or debt management. The overall relevance to Odin is primarily methodological, providing a validated user profiling approach that can be adapted for financial behavior classification in the Philippine context.
limitations:
  - "Cross-sectional design prevents causal inferences about determinants of SRI behavior. [unacknowledged]"
  - "Self-reported survey data may be subject to social desirability and response biases. [unacknowledged]"
  - "Italian sample limits generalizability to other cultural contexts, including the Philippines. [unacknowledged]"
  - "Investor motivations (e.g., diversification, financial performance) were not examined."
  - "Perceived knowledge measures may overestimate actual financial literacy."
remember_this:
  - "Latent Profile Analysis identified five distinct investor behavioral profiles."
  - "num: Only 11.9% of the fully equipped profile were current SRI investors versus 4.7% sample average."
  - "Psychological factors like personal norms are as important as financial literacy."
  - "Environmental concern without financial knowledge does not drive sustainable investment."
  - "Knowledge and risk appetite are critical to convert intention into actual behavior."
```
---

## Paper 2: Xing_summarized.md

**Source File:** `Xing_summarized.md`

```yaml
paper_id: 10.1016/j.ipm.2024.103704
designation: international-algorithm-specific
title: Financial risk tolerance profiling from text
authors: Xing, F.
year: 2024
venue: Information Processing and Management
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 10.A
tldr: User-generated text is a viable source for financial risk tolerance profiling, with a CNN model achieving a micro-F1 of 0.5066, significantly outperforming training-free baselines.
problem_and_motivation: Traditional risk tolerance assessment relies on questionnaires, which are costly and limited in scale. There is a pressing need for a faster, more cost-efficient method to profile individual risk tolerance to support financial inclusion and personalized services, but the potential of unstructured digital footprints remains underexplored.
approach:
  - A quaternary classification task (gambler, willing after research, cautious, risk avoider) for risk tolerance is defined.
  - Risk tolerance labels are synthesized via a meta-analysis of three studies, deriving a linear regression from Big Five personality traits.
  - A CNN model, based on Majumder et al. (2017), is trained on a corpus synthesized from MyPersonality, Essay, and PAN-15 datasets.
  - The model integrates Word2Vec, Glove, and BERT embeddings, along with Mairesse linguistic features (LIWC and MRC).
  - The approach is evaluated using 10-fold cross-validation and compared against strategic guess and GPT-3.5/GPT-4 baselines.
findings:
  - num: The proposed CNN model achieves a micro-F1 of circa 0.51, significantly outperforming the GPT-4 baseline (0.28) and strategic guess (0.34).
  - num: Text augmentation and multi-task learning with personality detection provided minimal benefit to the risk tolerance profiling task.
  - num: Richer text representations (combining Word2Vec, Glove, and BERT) were the primary driver of performance improvement, yielding over a 0.02 increase in micro-F1.
  - The study proves that user-generated text is a useful information source for financial risk profiling, potentially replacing formal questionnaires in low-stakes situations.
  - It is more difficult to identify the most extreme risk-taking or risk-averse investors, indicating the need for some human intervention in the overall profiling process.
key_figures_tables:
  - Table 5: Experimental results for different model settings → CNN-MT(W+G+B) achieves the highest micro-F1 of 0.5066.
  - Table 6: Robustness tests showing significant difference between CNN models and baselines → p-values < 0.01 confirm statistical significance.
key_equations:
  - equation: risk_tol_5 = 3.0715 + 0.094EXT_5 + 0.192OPN_5 - 0.145AGR_5 - 0.071CON_5 - 0.025NEU_5
    explanation: Linear regression summarizing meta-analysis to derive risk tolerance from Big Five traits.
definitions:
  - term: Risk Tolerance
    definition: Willingness to engage in risky behavior where possible outcomes can be negative.
  - term: Big Five Personality Traits
    definition: A five-factor model of personality comprising Extroversion, Neuroticism, Agreeableness, Conscientiousness, and Openness.
  - term: CNN
    definition: Convolutional Neural Network, a deep learning model used for text feature extraction and classification.
critical_citations:
  - "[Pak and Mahmood, 2015] — Provides regression equation for risk tolerance vs. personality."
  - "[Pinjisakikool, 2018] — Provides regression equation for risk tolerance vs. personality."
  - "[Wong and Carducci, 2013] — Provides regression equation for risk tolerance vs. personality."
  - "[Majumder et al., 2017] — Provides the base CNN architecture for the model."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly addresses the task of profiling user risk tolerance, a key behavioral profile.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: high
      justification: Provides a method for initial profiling from text, which can help address the cold-start problem.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Proposes and evaluates a CNN-based classification approach for a behavioral profile (risk tolerance).
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: The model predicts a stable user trait, which can be an input for forecasting models within Odin.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Discusses using digital footprints for profiling, highlighting the need for privacy considerations in such approaches.
  contribution: This paper provides a foundational method for automatically deriving a user's financial risk tolerance from text, which can be integrated into Odin's user onboarding process to address the cold-start problem for behavioral profiling. The findings on the effectiveness of rich linguistic features (LIWC, MRC) over complex model architectures inform the feature engineering for Odin's classification modules. The demonstrated possibility of replacing formal questionnaires with text analysis supports Odin's mobile-first design philosophy by reducing user friction. The study's discussion on the limitations of extreme profile identification provides a specific area where Odin's system might require human or fallback mechanisms.
  directly_justifies:
    - A CNN model can profile financial risk tolerance from user text with a micro-F1 of 0.5066.
    - Richer text representations are more important than text augmentation or multi-tasking for this task.
    - User-generated text is a useful and cost-efficient source for financial risk profiling.
    - Profiling from text can replace formal questionnaires in low-stakes situations.
  limits:
    - Risk tolerance labels were derived indirectly from personality datasets, not ground truth surveys.
    - The model's performance on extreme risk categories (gambler, risk avoider) is poor, requiring human intervention.
  mapping_rationale: A systematic scan across all 12 functional domains and associated topics identified the Behavioral Profiling & Classification domain (5.A, 5.B, 5.C) as the most directly relevant, assigned high relevance because the paper directly proposes a method to classify risk tolerance. The Forecasting domain (6.A, 6.B) was flagged as medium relevance, as the predicted risk profile could serve as a static input to forecasting models. Data Privacy (10.A) was deemed contextual, as the paper's use of digital footprints raises privacy issues relevant to Odin's design. The Filipino Cultural Context domain was considered and rejected because the study uses international datasets and does not address Filipino-specific practices. Expense Categorization, Budget Recommendation, and System Evaluation domains were rejected as the paper does not address these functions directly. The paper's overall relevance to Odin is high, as it offers a practical, data-driven solution for user profiling that aligns with Odin's goal of providing personalized financial management with minimal user input.
limitations:
  - Risk tolerance labels are synthesized through meta-analysis of multiple datasets, not directly validated against ground truth. [unacknowledged]
  - The synthesized dataset may not represent the demographic and cultural specifics of Filipino young professionals. [unacknowledged]
  - The study does not address the integration of this text-based model with other data sources like demographics.
  - The model's performance on extremely risk-tolerant or risk-averse users is significantly lower.
remember_this:
  - A CNN model achieves a micro-F1 of 0.51 for text-based risk profiling.
  - Richer text embeddings are more effective than advanced machine learning tricks.
  - User text is a viable, low-cost alternative to formal risk questionnaires.
  - The method struggles with identifying extreme profiles (gamblers/avoiders).
```
---

## Paper 3: Khashadourian & Harrison_summarized.md

**Source File:** `Khashadourian & Harrison_summarized.md`

```yaml
paper_id: 10.1002/cfp2.1194
designation: international
title: Perceptions or behavior? An evaluation of CFPB's financial well-being scale using household financial ratios
authors: Khashadourian, E.; Harrison, A. L.
year: 2024
venue: Financial Planning Review
odin_topics:
  - "3.A"
  - "5.A"
  - "12.A"
  - "13.A"
tldr: Financial ratios can define distinct financial well-being categories that align with the CFPB's subjective scale, though noise in the CFPB data limits precise interval mapping.
problem_and_motivation: There is a gap in understanding how objective financial ratios correspond to subjective financial well-being scales like the CFPB's. Existing scales are largely perception-based, and objective measures have not been reliably linked to these perceptions. This hinders the actionability of subjective scores for interventions.
approach:
  - Data from a Qualtrics survey of 416 U.S. adults aged 25-60, balanced by income tiers, collected detailed budget, asset, liability, and CFPB scale responses.
  - Defined four financial ratios: Estimated Monthly Savings Rate, Percentage of Fixed Expenses, Credit Insolvency Ratio, and Average Liquidity Ratio.
  - Used a hierarchy of these ratios to create ordinal rankings, which were then consolidated using linear discriminant analysis.
  - Evaluated the optimal number of categories and classification accuracy, selecting a four-category model with an 81.3% hit rate.
  - Employed ANOVA to compare the mean CFPB scores across the identified financial well-being categories.
findings:
  - num: The discriminant analysis model achieved an 81.3% classification hit rate for the four financial well-being categories.
  - The four categories identified are Financially Flourishing, Financially Stable, Financially Fragile, and Financially Distressed.
  - ANOVA revealed a significant main effect of the financial well-being categories on CFPB scores, F(3,406)=32.99, p<0.001, with a large effect size (η²=0.197).
  - Mean CFPB scores declined consistently across the ordinal categories: Flourishing (63.08), Stable (51.31), Fragile (48.76), and Distressed (47.57).
  - The study supports the construct validity of the CFPB scale by demonstrating alignment with objective financial ratios.
  - The study could not define non-overlapping and exhaustive CFPB score intervals for the financial well-being categories due to overlapping confidence intervals.
key_figures_tables:
  - "Table 2: Ordinal rankings of household financial status in the EMH framework → 16 possible ranks based on four binary financial ratio conditions."
  - "Table 7: Stages of financial well-being → Four categories with mean CFPB scores ranging from 63.08 (Flourishing) to 47.57 (Distressed)."
  - "Table 8: Confidence intervals around the mean CFPB score → Overlapping intervals prevent exhaustive mapping of categories to the CFPB scale."
key_equations:
  - equation: "EMS = ((MNI - TME) / MGI) * 100"
    explanation: "Measures ability to generate a monthly cash surplus."
  - equation: "PFE = (FE / MNI) * 100"
    explanation: "Measures the proportion of household expenses that are fixed."
  - equation: "CIR = (MP / MNI) * 100"
    explanation: "Measures non-mortgage debt service burden."
  - equation: "ALR = (LNLA / TME) * 100"
    explanation: "Measures liquidity to cover monthly expenses."
definitions:
  - term: "EMH"
    definition: "Equilibrium Model of the Household, a framework using four financial ratios to define financial well-being stages."
  - term: "CFPB"
    definition: "Consumer Financial Protection Bureau, a U.S. government agency that developed the Financial Well-Being Scale."
  - term: "LDA"
    definition: "Linear Discriminant Analysis, a statistical method used to find a linear combination of features that separates categories."
critical_citations:
  - "[CFPB, 2017] — Found no single objective measure correlates perfectly with financial well-being."
  - "[Comerton-Forde et al., 2022] — Identified saving behavior as a key predictor of financial well-being."
  - "[Greninger et al., 1996] — Established benchmark values for common household financial ratios."
relevance:
  topics:
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "high"
      justification: "The paper defines and operationalizes four specific financial ratios as an objective categorization framework."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "The study's four categories (Flourishing, Stable, Fragile, Distressed) directly represent distinct financial behavioral profiles."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "medium"
      justification: "The research provides a method for evaluating a subjective scale against an objective ratio-based typology."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "contextual"
      justification: "The study identifies the savings rate as a foundational ratio for financial well-being, but does not address goal management."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "low"
      justification: "The paper is based on U.S. data and does not consider seasonal or cultural spending patterns specific to the Philippines."
  contribution: "This research provides a validated method for categorizing users into distinct financial well-being states (Flourishing, Stable, Fragile, Distressed) based on objective financial ratios, which can be used to initialize user profiles. The finding that these categories align with the CFPB subjective scale supports using this ratio-based classification as a proxy for user perception and a potential input for behavioral models. The progressive interaction of the four ratios offers a clear hierarchy for diagnosing a user's financial position and recommending targeted interventions."
  directly_justifies:
    - "Household financial ratios can reliably identify distinct states of financial well-being."
    - "The categories of financial well-being align with the CFPB's subjective Financial Well-Being Scale."
    - "A positive savings rate is the initial building block for achieving higher financial well-being."
  limits:
    - "The study's U.S.-based sample limits generalizability to other populations, including Filipino young professionals."
    - "The relatively small sample size (416) and reliance on self-reported data may introduce measurement errors."
    - "The study was unable to define non-overlapping CFPB score intervals for the categories, which limits actionability."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed for this paper. Domains such as 'Behavioral Profiling & Classification' (5.A) and 'Expense Categorization' (3.A) were flagged as highly relevant because the paper's central contribution is creating a typology of financial well-being from financial ratios. The 'System Evaluation' domain (12.A) was deemed medium relevance as it evaluates a subjective scale against an objective one, providing a framework for validating Odin's modules. The 'Savings & Debt Management' domain (13.A) was considered contextual because the paper identifies a positive savings rate as foundational but does not address goal management strategies. Domains like 'Filipino Cultural Context' and 'Spending Forecasting' were rejected as irrelevant because the paper uses U.S. data and does not address predictive modeling or cultural practices. In summary, the paper's primary relevance to Odin lies in its robust methodology for profiling users based on their financial ratios, which can inform both initial user classification and the design of an evaluation framework."
limitations:
  - "Use of self-reported data from a survey is subject to measurement and reporting errors. [unacknowledged]"
  - "The small sample size (n=416 after data cleaning) may limit the generalizability of the findings. [unacknowledged]"
  - "The study could not define non-overlapping CFPB score intervals for the financial well-being categories, which limits the practical application of mapping the CFPB scale to actionable states."
  - "The research is based on a U.S. sample, which may not be directly generalizable to Filipino young professionals."
  - "The noise in the CFPB data due to incomplete partitioning raises questions about the scale's reliability."
remember_this:
  - "Household financial ratios can reliably classify users into four financial well-being categories."
  - "Mean CFPB scores decline consistently across the four ratio-based categories from 63.08 to 47.57."
  - "A positive savings rate is the foundational step in the Equilibrium Model of the Household."
  - "The study validates that objective financial ratios and subjective perceptions of well-being are closely aligned."
  - "The CFPB scale captures objective financial behaviors more than previously thought, but its data contains noise."
```
---

## Paper 4: Shuryhin & Zinovatna_summarized.md

**Source File:** `Shuryhin & Zinovatna_summarized.md`

```yaml
paper_id: 10.15276/aait.07.2024.24
designation: international-algorithm-specific
title: Recommendation system for financial decision-making using Artificial intelligence
authors: Shuryhin, K. A.; Zinovatna, S. L.
year: 2024
venue: Applied Aspects of Information Technology
odin_topics:
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 10.A
  - 10.B
tldr: An AI-driven financial management system uses Isolation Forest for anomaly detection, ARIMA and LSTM for forecasting, and an LLM to generate personalized, ethically-grounded recommendations.
problem_and_motivation: Cognitive biases lead to irrational spending, and AI-enhanced marketing can manipulate consumer behavior. Existing financial recommendation systems often lack personalization, fail to address user autonomy, and do not adequately consider ethical principles like transparency and fairness. There is a need for a system that helps users make more rational financial decisions without imposing specific choices.
approach:
  - Isolation Forest isolates anomalous transactions by measuring path lengths in binary trees.
  - ARIMA models short-term spending trends after determining optimal p, d, q parameters.
  - LSTM captures long-term dependencies in spending data using memory cells and gating mechanisms.
  - Forecasts from ARIMA and LSTM are combined using a weighted average to improve accuracy.
  - A large language model (LLaMa 3.1) generates personalized advice from transaction history, anomalies, and forecasts.
findings:
  - num: The combination of ARIMA and LSTM enhances forecast accuracy by considering both short-term and long-term trends.
  - num: Isolation Forest effectively identifies anomalies by calculating anomaly scores where values near 1 indicate outliers.
  - The system architecture uses a modular, event-driven design with AWS services for scalability and reliability.
  - The system promotes responsible financial behavior by enhancing user awareness without imposing decisions.
key_figures_tables:
  - Figure 1: Diagram of LLM request process for personalized financial advice → Shows data flow from input to recommendation.
  - Figure 2: Example of LLM response based on provided context → Demonstrates a specific instance of generated advice.
  - Figure 3: Interaction of AI components within the system → Illustrates the overall AI module architecture.
  - Figure 4: ERD for the recommendation system → Details the database schema for user financial data.
  - Figure 5: Main page of the system interface → Shows the user-facing application layout.
  - Figure 6: Use of AI models for anomaly detection → Visualizes the anomaly detection workflow.
key_equations:
  - equation: s(x,n) = 2^{-E(h(x))/c(n)}
    explanation: Anomaly score where values near 1 indicate an anomaly.
  - equation: y_t = c + φ_1 y_{t-1} + ... + φ_p y_{t-p} + θ_1 ε_{t-1} + ... + θ_q ε_{t-q} + ε_t
    explanation: ARIMA model equation defining the time series forecast.
  - equation: f_t = σ(W_f ⋅ [h_{t-1}, x_t] + b_f)
    explanation: LSTM forget gate equation controlling information retention.
  - equation: \hat{y}_t = α⋅\hat{y}^{ARIMA}_t + (1−α)⋅\hat{y}^{LSTM}_t
    explanation: Weighted average combining ARIMA and LSTM forecasts.
definitions:
  - term: Isolation Forest
    definition: An anomaly detection algorithm that isolates outliers rather than profiling normal points.
  - term: ARIMA
    definition: AutoRegressive Integrated Moving Average model for time series forecasting.
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network for learning long-term dependencies.
  - term: LLM
    definition: Large Language Model, used here to generate natural language financial advice.
  - term: Cognitive biases
    definition: Systematic patterns of deviation from norm or rationality in judgment.
critical_citations:
  - "[Milano et al., 2020] — Survey of ethical challenges in recommender systems."
  - "[Chua et al., 2023] — Model for user acceptance of AI-generated investment advice."
  - "[Zatevakhina et al., 2019] — Recommender systems as foundation for intelligent financial platforms."
  - "[del Valle & Lara, 2024] — Analysis of personal autonomy in AI-powered recommender systems."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Provides an overview of financial recommendation systems and their applications.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies gaps such as lack of personalization and ethical considerations in current systems.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Uses user characteristics like risk level and goals to personalize recommendations.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: contextual
      justification: Discusses general user profiling but does not directly address cold-start.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Applies ARIMA and LSTM to forecast user spending.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Specifically compares and combines ARIMA and LSTM for spending forecasts.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Uses Isolation Forest to detect anomalous expenses.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Implements Isolation Forest as the core anomaly detection algorithm.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Emphasizes privacy and security using OAuth 2.0 and OWASP principles.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Stresses transparency and user autonomy to build trust.
  contribution: "This paper provides a blueprint for integrating multiple AI models (anomaly detection, forecasting, and LLM-based generation) into a modular financial advisory system. The architecture supports the development of Odin's recommendation and anomaly detection modules. The emphasis on ethical design, including user autonomy and transparency, aligns with Odin's need for user trust. The system's ability to generate personalized advice based on user-specific data directly informs Odin's budget recommendation and behavioral profiling components."
  directly_justifies:
    - "Combining ARIMA and LSTM improves forecast accuracy for user spending."
    - "Isolation Forest can effectively identify anomalous financial transactions."
    - "LLMs can generate personalized financial recommendations from structured user data."
    - "Ethical design principles are essential for user acceptance of AI financial advice."
    - "A modular architecture facilitates integration of different AI components."
  limits:
    - "The study does not provide empirical evaluation metrics (e.g., RMSE, F1-score) for the models used."
    - "User testing and validation of the recommendation system's effectiveness are not reported."
    - "The system's performance across diverse income levels is claimed but not empirically demonstrated."
    - "The LLM component's recommendation quality is not compared against other baselines."
    - "The paper lacks a discussion on the system's scalability with a large number of users."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. Domains flagged as relevant include 'Existing Systems & Gaps' (4.A, 4.B) due to the paper's review of financial RS and identified limitations; 'Behavioral Profiling & Classification' (5.A, 5.B) because it uses user characteristics for personalization; 'Spending Forecasting' (6.A, 6.B) as a core contribution; 'Anomaly Detection' (8.A, 8.B) as another core algorithmic contribution; and 'Data Privacy & User Trust' (10.A, 10.B) because of the strong ethical focus. The paper was considered and rejected for 'Filipino Cultural Context' (2.A-D) as it is international and does not discuss Filipino-specific practices. 'Budget Recommendation' (7.A-D) was noted as contextual because the LLM generates advice but does not formulate it as a constrained optimization problem. The paper is highly relevant for informing Odin's algorithmic design and ethical framework, providing concrete methods for forecasting and anomaly detection."
limitations:
  - "No quantitative evaluation of the system's performance is provided. [unacknowledged]"
  - "The effectiveness of the LLM-generated recommendations is not empirically validated with users. [unacknowledged]"
  - "The system is tested but results are not shared, limiting reproducibility. [unacknowledged]"
  - "The paper does not address potential biases in the AI models or training data. [unacknowledged]"
remember_this:
  - "Combines Isolation Forest, ARIMA, LSTM, and LLMs for financial advice."
  - "Emphasizes user autonomy and ethical AI design principles."
  - "Modular architecture ensures independence of AI and core modules."
  - "Aims to counter cognitive biases and manipulative marketing."
  - "Does not provide quantitative performance metrics for its models."
```
---

## Paper 5: Ramos-2024b_summarized.md

**Source File:** `Ramos-2024b_summarized.md`

```yaml
paper_id: 5c9b8b1e-3a6b-4e8b-9a7c-4d6f2a8b9c7e
designation: international
title: Essays on the Causes and Demographic Consequences of Employment Uncertainty
authors: Ramos, V. J. R.
year: 2024
venue: Hertie School
odin_topics:
  - 1.A
  - 1.C
  - 2.A
  - 2.B
  - 2.C
  - 2.D
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 13.C
tldr: Employment uncertainty is a multi-dimensional phenomenon that is both caused by economic shocks and state policies, and a key determinant of fertility behavior and intentions across different life course stages.
problem_and_motivation: Existing research lacks a unified framework to conceptualize the multifaceted nature of employment uncertainty, and its role as both a determined outcome of crises and a determinant of demographic behavior. This dissertation addresses this gap by systematically expanding the typology of employment uncertainty and empirically demonstrating its causes and consequences on fertility in different country contexts.
approach:
  - Analyzes the gendered informalization of employment in the Philippines due to extreme COVID-19 lockdowns using a difference-in-differences design on pooled Labor Force Surveys.
  - Investigates the persistent effects of initial employment conditions on fertility in Germany using a two-step identification strategy combining optimal full matching and event history modeling on the German Socio-Economic Panel.
  - Examines the relationship between social class, economic uncertainty, and second-birth fertility in Germany using piecewise constant and cure fraction event history models.
  - Assesses the causal impact of future caregiving responsibilities and employment uncertainties on ascribed fertility intentions in Germany using a factorial survey experiment fielded in the SOEP Innovation Sample.
findings:
  - num: Extreme lockdowns in the Philippines increased the probability of informal employment by 1.7 percentage points for all workers, but the effect was significant and larger (2.2 pp) only for women.
  - num: Female labor market entrants with a fixed-term contract have a 19% lower first-birth hazard within the first decade of entry compared to permanent entrants.
  - num: Male labor market entrants during a recession have a 23% lower first-birth hazard within the first decade of entry compared to non-recession entrants.
  - num: Men and women in the upper service class have elevated second birth rates, with semi-/unskilled workers having 42% (men) and 36% (women) lower rates compared to the upper service class.
  - num: The absence of future caregiving responsibilities and employment uncertainty increases ascribed fertility intentions by 2.8 and 1.9 units (on a 0-10 scale), respectively.
key_figures_tables:
  - Figure 1.1: Global unemployment trends show pronounced cyclicality in high-income economies, spiking during the 2008 financial crisis and COVID-19 pandemic.
  - Figure 1.4: Global total fertility rates have declined remarkably over the past 60 years, with low-income countries showing the steepest recent decreases.
  - Table 1.2: Fixed effects regressions show a robust negative association between lagged unemployment rates and total fertility rates across 187 countries.
  - Figure 3.1: Fixed-term labor market entry has a persistent negative effect on first-birth probabilities, reaching up to a 5 pp reduction within 10 years post-entry.
key_equations:
  - equation: F_{c,t} = α + γ U_{c,t-1} + δD_{c,t-1} + ωM_{c,t-1} + θZ_{c,t} + ε_{c,t}
    explanation: Models country-level fertility as a function of lagged unemployment and controls.
  - equation: h_p(t) = h_0(t)exp(β_p X_p + β_q X_q)
    explanation: Cox proportional hazards model for first birth hazard after labor market entry.
  - equation: h(t|X) = h_0(t) × exp(βx)
    explanation: Piecewise constant hazard model for transition to second birth.
definitions:
  - term: Employment Uncertainty
    definition: An umbrella term for labor market positions characterized by imperfect, incomplete, or unknown information regarding job security, duration, or conditions.
  - term: Survivalist Motive
    definition: The strategy of engaging in informal work out of necessity during economic downturns to avoid unemployment, due to a lack of social safety nets.
  - term: Ascribed Fertility Intentions
    definition: The likelihood a respondent assigns to a hypothetical couple having a child, as measured in a vignette experiment.
critical_citations:
  - "[Blossfeld et al., 2006] — Provides foundational schema for employment uncertainty dimensions."
  - "[Vignoli et al., 2020a] — Introduces the Narrative Framework for future-oriented fertility decisions."
  - "[Alderotti et al., 2021] — Meta-analysis showing negative effects of employment instability on fertility."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Chapter 2 focuses specifically on the Philippine labor market and its young workforce.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Analyzes informalization of employment which is a key aspect of financial behavior.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Analyzes Filipino household coping mechanisms during the pandemic.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: The business cycle is a key determinant of employment uncertainty and fertility.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: medium
      justification: The dissertation analyzes Filipino employment patterns during COVID-19 lockdowns.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: Provides a global context but does not directly survey PFMS.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: low
      justification: Implicitly discusses gaps in social protection systems in the Philippines.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Class-based profiles are a central operationalization of employment uncertainty.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: Discusses effects of initial employment conditions, analogous to cold-start.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses EGP class schema to classify occupational profiles.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: Does not use forecasting algorithms, but discusses predictive factors of fertility.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: The survivalist motive discusses household coping strategies, which could inform budgeting.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: Does not directly discuss budget recommendations.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: The dissertation does not address anomaly detection.
    - code: 9.A
      name: Mobile‑First Design Principles and Rationale
      relevance: low
      justification: Does not directly address mobile design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Does not address data privacy.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: Does not address user trust.
    - code: 13.C
      name: End‑of‑Period Surplus as a Savings Input
      relevance: contextual
      justification: The survivalist motive and lack of savings are key mechanisms discussed.
  contribution: The dissertation provides a comprehensive framework for understanding the multi-dimensional nature of employment uncertainty and its causal role in fertility decisions. Findings on the Philippine informalization and gendered labor market shocks can inform Odin's design for expense categorization and behavioral profiling of Filipino users. The analysis of future-oriented uncertainties directly justifies the importance of incorporating predictive and scenario-based features in a PFMS to enhance user retention and engagement.
  directly_justifies:
    - "Extreme lockdowns increase informal employment for women, particularly mothers."
    - "Female fixed-term entrants have a 19% lower first-birth hazard."
    - "Male recession entrants have a 23% lower first-birth hazard."
    - "Service class occupations are associated with elevated second birth rates."
    - "Future caregiving and employment uncertainties lower fertility intentions."
  limits:
    - "Context-specific findings in Germany and the Philippines may not generalize."
    - "Limited discussion on underlying mechanisms in Chapter 3."
    - "Operationalization of variables may benefit from fine-tuning or alternative measures."
  mapping_rationale: A systematic scan across all 12 functional domains and their canonical topic codes was conducted. Domains with high relevance included Filipino Cultural Context (2.A, 2.B, 2.D) due to the focus on Philippine labor market dynamics, and Behavioral Profiling & Classification (5.A, 5.C) through the use of class-based and profile-based analyses. Borderline cases were encountered for topics like 5.B (Profile Dynamics) and 7.A (Budgeting Strategies), where the dissertation's discussion of initial conditions and survivalist motives provides contextual relevance but not direct actionable insights. Domains like Mobile-First Design (9.A, 9.B), Data Privacy (10.A, 10.B), and Anomaly Detection (8.A) were rejected as the dissertation does not address them. Overall, the dissertation offers high relevance for understanding the determinants and consequences of employment uncertainty, which is foundational for designing a PFMS like Odin for Filipino young professionals.
limitations:
  - "Context-specific estimates in Germany and the Philippines may not be generalizable."
  - "Limited discussion of underlying mechanisms in Chapter 3 due to sample size."
  - "The operationalization of some variables might benefit from fine-tuning."
  - "Chapter 5's outcome is ascribed intentions, not actual behavior."
remember_this:
  - "Employment uncertainty is multi-dimensional and context-dependent."
  - "Lockdowns informalized women's employment in the Philippines."
  - "Initial fixed-term employment reduces female fertility in Germany."
  - "Recession entry lowers male fertility in Germany."
  - "Future uncertainties and caregiving reduce fertility intentions by up to 2.8 points."
```
---

## Paper 6: Nie et al_summarized.md

**Source File:** `Nie et al_summarized.md`

```yaml
paper_id: 10.48550/arXiv.2406.13478
designation: international
title: A Survey of Large Language Models for Financial Applications: Progress, Prospects and Challenges
authors: Nie, Y.; Kong, Y.; Dong, X.; Mulvey, J. M.; Poor, H. V.; Wen, Q.; Zohren, S.
year: 2024
venue: arXiv preprint
odin_topics:
  - "5.B"
  - "6.A"
  - "6.B"
  - "7.B"
  - "8.B"
  - "9.A"
  - "10.A"
  - "11.A"
  - "12.A"
tldr: This survey reviews the application of large language models across financial tasks, summarizing models, datasets, and benchmarks, while highlighting practical challenges for deployment.
problem_and_motivation: While existing surveys cover financial LLMs, they often lack a deep dive into domain-specific practical challenges, such as lookahead bias, legal concerns, and data pollution. This survey aims to bridge the gap between academic research and real-world implementation, providing a holistic view for both researchers and practitioners.
approach:
  - Categorizes financial LLM applications into linguistic tasks, sentiment analysis, time series analysis, financial reasoning, and agent-based modeling.
  - Reviews specialized financial LLMs like BloombergGPT, FinBERT, FinGPT, and InvestLM, discussing their architectures and training strategies.
  - Provides a comprehensive collection of datasets, benchmarks, and code resources for financial NLP research.
  - Analyzes challenges including data issues, modeling limitations, benchmarking difficulties, and ethical concerns.
  - Discusses future opportunities like hybrid inference for cost-efficiency and mitigation of lookahead bias with point-in-time models.
findings:
  - "num: Fine-tuned LLMs like FinBERT show enhanced resilience against adversarial attacks compared to traditional keyword-based sentiment methods."
  - "LLMs demonstrate significant potential in zero-shot financial sentiment analysis, with GPT-4 outperforming BERT on news headline classification for stock return prediction."
  - "The application of LLMs for direct time series forecasting remains debated, with some studies showing underperformance compared to traditional ML models in zero-shot settings."
  - "Agent-based models using LLMs can effectively simulate market behaviors and economic activities, producing realistic trading and investment strategies."
  - "Instruction-tuned models, such as PIXIU's FinMA, provide a robust framework for multi-task financial NLP evaluation."
key_figures_tables:
  - "Table 1: Comparison of surveys → This survey uniquely provides comprehensive coverage of models, benchmarks, applications, and challenges."
  - "Figure 2: Overview of financial LLMs from 2019 → Visualizes the evolution and categorization of specialized financial language models."
  - "Figure 4: Sentiment analysis papers by data source → Categorizes LLM applications in sentiment analysis across diverse financial texts."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "LLM"
    definition: "Large Language Model, a deep learning model pre-trained on vast text data for language understanding and generation."
  - term: "RAG"
    definition: "Retrieval-Augmented Generation, a technique for enhancing LLMs by retrieving external information."
  - term: "NER"
    definition: "Named Entity Recognition, a task to identify and classify key entities in text."
  - term: "ABM"
    definition: "Agent-Based Modeling, a simulation technique using autonomous agents to model complex systems."
  - term: "FSA"
    definition: "Financial Sentiment Analysis, the task of quantifying sentiment from financial texts."
critical_citations:
  - "[Wu et al., 2023] — Introduces BloombergGPT, a key financial LLM trained on proprietary data."
  - "[Yang et al., 2023] — Introduces FinGPT, highlighting open-source accessibility for financial modeling."
  - "[Xie et al., 2023] — Introduces PIXIU, a comprehensive benchmark and model framework for financial LLMs."
  - "[Kim et al., 2024] — Demonstrates LLMs outperforming human analysts on financial statement analysis."
relevance:
  topics:
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "contextual"
      justification: "Discusses zero-shot capabilities and domain adaptation challenges relevant to new user profiles."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Reviews LLM-based forecasting techniques for financial time series."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Examines algorithms for market trend forecasting and return prediction."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Explores LLMs for financial planning and investment recommendation."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "medium"
      justification: "Covers anomaly detection methods in financial time series."
    - code: "9.A"
      name: "Mobile‑First Design Principles and Rationale"
      relevance: "contextual"
      justification: "Discusses accessibility and user engagement via conversational AI."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "Addresses data privacy concerns and legal responsibility in financial AI."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "contextual"
      justification: "Touches on user trust and the need for interpretability."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Provides a comprehensive survey of benchmarks (FLUE, PIXIU) for financial NLP."
  contribution: "This survey justifies Odin's adoption of instruction-tuned models for multi-task personal financial analysis, supports the use of RAG for enriching contextual data, and provides evidence for integrating sentiment analysis to forecast spending behaviors. It highlights the need for specific evaluation benchmarks like FLARE for Odin's module assessment, and informs Odin's design decisions regarding handling data privacy and mitigating lookahead bias."
  directly_justifies:
    - "Instruction-tuned models demonstrate superior financial sentiment analysis and numerical reasoning."
    - "Agent-based modeling with LLMs can simulate complex financial decision-making processes."
    - "Benchmarks like FLUE and PIXIU provide standardized frameworks for evaluating financial NLP tasks."
    - "Implementing hybrid inference can reduce computational costs significantly without losing performance."
    - "Mitigating lookahead bias requires point-in-time training datasets."
  limits:
    - "This survey is a review and does not provide an empirical evaluation of proposed models in a live environment."
    - "The paper primarily focuses on high-level financial tasks and may not address the specific constraints of a personal finance management system for Filipino users."
  mapping_rationale: "The systematic scan of all 12 functional domains identified several relevant areas for Odin. For Predictive Modeling (6.A/B), the survey's extensive review of forecasting algorithms provides high relevance, justifying Odin's potential use of LLMs for spending prediction. Similarly, for Evaluation Frameworks (12.A), the detailed examination of benchmarks like FLUE and PIXIU is highly relevant for designing Odin's module testing. For Anomaly Detection (8.B) and Budget Recommendation (7.B), the review offers medium relevance, providing contextual examples of how LLMs can be applied in these areas. Domains like Data Privacy (10.A) are highly relevant due to the detailed discussion of legal and ethical challenges. Topics related to specific Filipino cultural context (2.A-D) were considered but not found, as the survey is general. The overall relevance of the paper to Odin is high, as it provides a foundational understanding of the capabilities and pitfalls of financial LLMs, guiding design choices and justifying the technology's integration into the system."
limitations:
  - "The authors note challenges with inference speed and cost for real-time deployment."
  - "The paper acknowledges the risk of hallucinations and inaccurate outputs in financial documents."
  - "Lookahead bias in backtesting is identified as a significant challenge requiring mitigation strategies."
  - "Ethical issues like incentive alignment and legal responsibility are discussed but lack concrete solutions."
  - "The review may not cover the latest advancements in the rapidly evolving field of LLMs [unacknowledged]."
remember_this:
  - "Fine-tuning LLMs on financial corpora significantly improves sentiment analysis over general models."
  - "Agent-based models can simulate complex market behaviors using LLM-driven decisions."
  - "Instruction tuning enhances LLM performance for specialized financial tasks."
  - "Benchmarking financial LLMs requires multi-task datasets like PIXIU to ensure robust evaluation."
  - "Data pollution and hallucinations remain key risks when deploying LLMs in finance."
```
---

## Paper 7: Paghasian_summarized.md

**Source File:** `Paghasian_summarized.md`

```yaml
paper_id: "10.69569/jip.2024.0198"
designation: "local"
title: "Financial Practices among Foundation University Employees: Basis for Financial Plan"
authors: "Paghasian, M. F."
year: 2024
venue: "Journal of Interdisciplinary Perspectives"
odin_topics:
  - "1.A"
  - "1.B"
  - "1.C"
  - "3.A"
  - "3.B"
  - "3.C"
  - "4.A"
  - "4.B"
  - "7.A"
  - "7.B"
  - "13.A"
tldr: "Foundation University employees demonstrate strong income, expenditure, and savings practices, but emergency funds and advisor consultation need improvement, with positive financial practices correlating with higher investments."
problem_and_motivation: "Financial stability requires effective planning and practices, yet many Filipino employees lack adequate financial literacy and emergency funds. Employers need data on employee financial behaviors to design effective wellness programs that improve financial health and job performance."
approach:
  - "Conducted a descriptive-correlational study with 191 regular and probationary employees at Foundation University."
  - "Used a validated, self-made survey questionnaire to measure financial practices across income, expenditure, savings, and investment."
  - "Applied weighted means, multiple linear regression, Kruskal-Wallis, and Mann-Whitney U tests to analyze data."
  - "Collected data on current monthly and yearly investments and reasons for investing."
  - "Assessed reliability using Cronbach's Alpha, with coefficients above 0.70 for all constructs."
findings:
  - "num: Employees showed strong financial practices with composite means of 3.81 (income), 3.83 (expenditure), and 3.84 (savings) on a 4-point scale."
  - "num: 61.26% of employees invest monthly in regular savings accounts, while 47.12% invest yearly in cooperative savings accounts."
  - "Employees demonstrate sound investment practices, including thorough review of products and risk assessment, with a composite mean of 3.48."
  - "The primary reason for investing is to attain financial freedom for family, with a mean of 4.50 on a 5-point scale."
  - "Financial practices in expenditure, savings, and investment significantly predict monthly investment availed (p = 0.005, 0.040, and 0.028, respectively)."
  - "Income practices significantly predict yearly investment availed (p = 0.026), while expenditure practices show a significant inverse relationship (p = 0.001)."
  - "Expenditure and investment practices significantly predict reasons for investing (p = 0.022 and p = 0.002, respectively)."
  - "A minority of employees lack emergency funds, with a mean of 3.40, indicating room for improvement."
  - "Employees moderately agree on seeking advice from financial advisors and investing in bank products, with means of 3.17 and 3.31, respectively."
key_figures_tables:
  - "Table 1: Financial practices by income → Employees manage income well but lack emergency funds."
  - "Table 2: Financial practices by expenditure → Employees avoid debt and use discounts effectively."
  - "Table 3: Financial practices by savings → Employees prioritize debt reduction and save regularly."
  - "Table 4: Financial practices by investment → Employees research investments but rarely consult advisors."
  - "Table 5: Current investments held → Savings accounts and cooperatives are the most common investments."
  - "Table 6: Reasons for investing → Financial freedom for family is the strongest motivator."
  - "Table 7: Regression for monthly investment → Expenditure, savings, and investment practices are significant predictors."
  - "Table 8: Regression for yearly investment → Income and expenditure practices are significant predictors."
  - "Table 9: Regression for reasons for investing → Expenditure and investment practices are significant predictors."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "PFMS"
    definition: "Personal Financial Management System"
  - term: "FU"
    definition: "Foundation University"
  - term: "NCR"
    definition: "National Capital Region"
  - term: "MP2"
    definition: "Modified Pag-IBIG 2 Savings Program"
  - term: "UITF"
    definition: "Unit Investment Trust Fund"
critical_citations:
  - "[BSP, 2018] — Filipino families spend more than they earn on average."
  - "[IFEBP, 2023] — Employers provide financial education due to employee knowledge gaps."
  - "[Pagkatotohan, 2023] — Cooperatives offer higher interest rates than banks."
  - "[Manulife, 2023] — Millennials and Gen Z show rising investment interest in the Philippines."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "high"
      justification: "Paper studies financial practices of Filipino university employees, a core demographic for Odin."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "high"
      justification: "Provides detailed data on income, expenditure, savings, and investment patterns of Filipino employees."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Directly measures financial behaviors like budgeting, spending, and saving habits of Filipino workers."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "medium"
      justification: "Indicators for expenditure practices can inform category design for Odin's expense tracking."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      relevance: "medium"
      justification: "Findings on spending priorities (needs vs. wants) inform how Odin might structure categories."
    - code: "3.C"
      name: "User-Defined Allocation Constraints"
      relevance: "low"
      justification: "Mentions budgeting and tracking expenses, which relates to user allocation but not in detail."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Provides baseline data on the financial landscape of Filipino employees, against which Odin can be positioned."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Identifies gaps like lack of emergency funds and advisor consultation, which Odin could address."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "high"
      justification: "Detailed findings on employee budgeting and spending behaviors directly inform budgeting strategy design for Odin."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Correlation between practices and investments suggests potential for personalized recommendations."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "high"
      justification: "Paper highlights savings practices and the gap in emergency funds, directly relevant to savings goal management."
    - code: "13.C"
      name: "End-of-Period Surplus as a Savings Input"
      relevance: "low"
      justification: "Relates to the concept of allocating surplus from budgets, though not explicitly addressed."
  contribution: "This paper provides empirical data on the financial practices of Filipino employees, which directly informs the design of Odin's budgeting and savings modules. The findings on income, expenditure, and savings behaviors can be used to benchmark Odin's expense categorization framework. The correlation between financial practices and investment levels justifies Odin's savings goal management feature. The identified gap in emergency funds and advisor consultation highlights opportunities for Odin's behavioral profiling and recommendation systems. Finally, the study's methodology offers a model for evaluating Odin's effectiveness in improving user financial practices."
  directly_justifies:
    - "The need for a feature to encourage and track emergency fund building in Odin's savings module."
    - "The design of Odin's expense tracking should prioritize needs and essential expenses based on employee practices."
    - "Odin's budget recommendation should account for Filipino spending patterns like prioritizing debt reduction before savings."
    - "The correlation between good practices and higher investments justifies Odin's goal-setting and progress tracking features."
  limits:
    - "Single-institution study limits generalizability to all Filipino young professionals."
    - "Self-reported data may be subject to social desirability bias. [unacknowledged]"
    - "The study is descriptive and correlational, not experimental, so causality cannot be inferred. [unacknowledged]"
    - "Limited sample size (191) and focus on employees from one university may not represent the broader population. [unacknowledged]"
  mapping_rationale: "A systematic scan across all 12 functional domains was performed. Domains relevant to financial behavior and system design were flagged. Topics under 'Filipino Cultural Context' (2.A, 2.B, 2.C, 2.D) were considered but rejected as the paper does not address cultural practices or seasonal spending specifically. 'Expense Categorization' (3.A, 3.B) and 'Budget Recommendation' (7.A, 7.B) were selected with medium to high relevance due to the paper's focus on spending and budgeting practices. 'Existing Systems & Gaps' (4.A, 4.B) was selected as the paper provides a baseline of current employee practices and identifies gaps like lack of emergency funds. 'Savings & Debt Management' (13.A) was selected with high relevance due to the detailed savings pattern analysis. 'Behavioral Profiling' (5.A-C) was considered but rejected as the paper does not classify users into profiles. 'Anomaly Detection' (8.A-C) and 'Mobile-First Design' (9.A-B) were considered but rejected as not addressed. The overall relevance is high for informing the design of Odin's budgeting, savings, and expense tracking modules based on empirical Filipino employee data."
limitations:
  - "The study was confined to regular and full-time probationary employees of Foundation University, limiting generalizability."
  - "Some respondents withheld income and investment information due to confidentiality concerns."
  - "A few respondents declined to complete the survey, and busy schedules caused delays and some uncollected responses."
  - "Data is self-reported, which may not fully reflect actual financial behaviors. [unacknowledged]"
  - "The study's descriptive-correlational design does not establish causal relationships between financial practices and investments. [unacknowledged]"
remember_this:
  - "Filipino employees show strong budgeting and savings habits but lack emergency funds."
  - "Saving and investment behaviors are significant predictors of monthly investment levels."
  - "Positive spending practices correlate with higher investment engagement."
  - "Employees invest primarily for family financial freedom and retirement."
  - "The paper identifies a key gap in financial advisor consultation and bank product investment."
```
---

## Paper 8: Natal et al_summarized.md

**Source File:** `Natal et al_summarized.md`

```yaml
paper_id: 10.5281/zenodo.10892981
designation: local
title: "UNDERSTANDING FINANCIAL BEHAVIOR: AN ANALYSIS OF PERSONAL FINANCIAL MANAGEMENT AMONG WORKING PROFESSIONALS AMIDST THE GLOBAL INFLATION SURGE"
authors: "Natal, T. M. S.; Bentulan, K. K. T.; Del Rosario, R. J. L.; Olazo, C. B.; Mangarin, J. A."
year: 2024
venue: "Guild of Educators in TESOL International Research Journal"
odin_topics:
  - "1.A"
  - "1.B"
  - "1.C"
  - "2.A"
  - "5.A"
  - "13.A"
  - "13.B"
  - "13.C"
tldr: "A mixed-methods study of Filipino working professionals aged 24-35 finds strong saving habits and prudent buying during inflation, with demographics showing no significant effect on financial practices."
problem_and_motivation: "The global inflation surge challenges personal financial management, yet limited research focuses on Filipino working professionals' specific behaviors. This study addresses the gap by examining saving and buying habits in Balayan, Batangas, to inform strategies for financial resilience."
approach:
  - "Quantitative survey of 75 working professionals using a 4-point Likert scale measured saving and buying habits."
  - "Qualitative semi-structured interviews with 5 participants explored inflation impact and coping strategies."
  - "Chi-square tests assessed relationships between demographics (age, gender, industry, employment type, income) and financial behaviors."
  - "Thematic analysis identified patterns in qualitative responses regarding budgeting and purchasing strategies."
findings:
  - "num: No significant relationship between any demographic factor and saving habits (p>0.05 for all chi-square tests)."
  - "num: No significant relationship between any demographic factor and buying behavior (p>0.05 for all)."
  - "num: General weighted mean for saving habits was 3.56 (Strongly Agree), with highest item 'save for secure future' at 3.69."
  - "num: General weighted mean for buying behavior was 3.35 (Strongly Agree), with highest item 'assess practical value' at 3.59."
  - "Professionals prioritize budgeting, tracking expenses, and reducing discretionary spending to cope with inflation."
  - "Qualitative themes include budgeting, frugality, buying in bulk, seeking cheaper alternatives, and fixed-percentage saving."
key_figures_tables:
  - "Table 2: Mean responses for saving habits → top priority is saving for future security (3.69)."
  - "Table 3: Mean responses for buying behavior → highest is assessing practical value of items (3.59)."
  - "Table 14: Impact of inflation on financial decisions → professionals adjust budgeting and prioritize saving."
  - "Table 15: Purchasing strategies → buying in bulk and seeking cheaper alternatives are common."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Inflation"
    definition: "The general rise in prices over time, reducing purchasing power."
  - term: "Personal Financial Management"
    definition: "The handling of cash, credit, saving, borrowing, and spending to achieve financial goals."
  - term: "Saving Habits"
    definition: "Regular practices of setting aside income for future use."
  - term: "Buying Behavior"
    definition: "Consumer practices and decision-making in purchasing goods and services."
critical_citations:
  - "[Segal, 2022] — defines inflation as rising prices."
  - "[Oner, 2019] — describes inflation as rate of price increase."
  - "[Baranidharan, 2022] — defines financial behavior components."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "high"
      justification: "Paper directly studies this demographic (age 24-35, single, working)."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "high"
      justification: "Provides data on income, employment, and spending patterns."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "high"
      justification: "Directly measures saving and buying behaviors."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "contextual"
      justification: "Mentions 'deserve ko 'to' mindset but does not deeply explore cultural practices."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "low"
      justification: "Describes saving and buying behaviors but does not classify into profiles."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "high"
      justification: "Focuses on saving habits and strategies, essential for goal setting."
    - code: "13.B"
      name: "Debt Management in PFMS"
      relevance: "medium"
      justification: "Discusses avoiding debt and overspending, relevant for debt management."
    - code: "13.C"
      name: "End-of-Period Surplus as a Savings Input"
      relevance: "high"
      justification: "Participants emphasize saving from salary, aligning with surplus allocation."
  contribution: "This study provides empirical evidence on saving and buying behaviors of Filipino young professionals during inflation, informing Odin's user modeling by establishing baseline behaviors. It highlights the strong saving orientation, which can guide budget recommendation algorithms to prioritize savings goals. The finding that demographics do not significantly affect behavior suggests a uniform approach for Odin's core functionalities. The qualitative strategies (e.g., fixed-percentage saving, bulk buying) offer actionable insights for designing nudge mechanisms. Overall, the paper supports Odin's design assumptions about the target users' financial priorities."
  directly_justifies:
    - "Filipino young professionals prioritize long-term savings over discretionary spending during inflation."
    - "Demographic factors do not significantly affect saving habits or buying behavior among the target group."
    - "Common coping strategies include reducing discretionary spending and seeking cheaper alternatives."
    - "Fixed-percentage saving is a prevalent strategy among professionals."
  limits:
    - "The study is limited to a single municipality (Balayan), which may not represent all Filipino young professionals."
    - "The sample size of 75 for quantitative and 5 for qualitative is relatively small."
    - "Only saving and buying behaviors are examined, excluding investment, insurance, and retirement planning."
    - "The study does not account for potential seasonal or cyclical spending patterns. [unacknowledged]"
    - "Self-reported survey responses may introduce social desirability bias. [unacknowledged]"
  mapping_rationale: "All 12 functional domains and their associated topic codes were systematically scanned. The Filipino Cultural Context domains (2.A-2.D) were considered; only 2.A is marginally touched via the 'deserve ko 'to' mindset, so it is assigned contextual. The Behavioral Profiling domain (5.A-5.C) is relevant because the paper describes saving and buying behaviors, but does not classify profiles, so 5.A is low. The Savings & Debt Management domain (13.A-13.C) is highly relevant as the paper focuses on saving habits and debt avoidance, with 13.A and 13.C high, 13.B medium. The Demographic domains (1.A-1.C) are directly addressed, all high. Other domains like Expense Categorization, Existing Systems, Forecasting, Budget Recommendation, Anomaly Detection, Mobile Design, Privacy, Engagement, and Evaluation were considered but rejected because the paper does not address system design, algorithms, or evaluation frameworks. Overall, the paper provides foundational behavioral insights for Odin's user modeling."
limitations:
  - "Limited to Balayan, Batangas, reducing generalizability to other regions."
  - "Small sample size, especially for qualitative phase."
  - "Focus only on saving and buying, ignoring other financial behaviors."
  - "No longitudinal data to track changes over time. [unacknowledged]"
  - "Potential self-report bias in survey responses. [unacknowledged]"
remember_this:
  - "Saving for future security is the top priority with mean 3.69."
  - "Demographics do not significantly predict saving or buying behavior."
  - "Professionals reduce discretionary spending to cope with inflation."
  - "Common saving strategies include fixed-percentage allocation and bulk buying."
  - "The study is context-specific to Balayan, limiting generalizability."
```
---

## Paper 9: Onsay & Rabajante-2024b_summarized.md

**Source File:** `Onsay & Rabajante-2024b_summarized.md`

```yaml
paper_id: "10.1016/j.sctalk.2024.100387"
designation: "local-algorithm-specific"
title: "When machine learning meets econometrics: Can it build a better measure to predict multidimensional poverty and examine unmeasurable economic conditions?"
authors: "Onsay, E. A.; Rabajante, J. F."
year: 2024
venue: "Science Talks"
odin_topics:
  - "6.A"
  - "6.B"
  - "12.A"
  - "12.B"
  - "12.C"
tldr: "Combines machine learning and econometrics to predict multidimensional poverty in Philippine indigenous communities, finding random forest outperforms other algorithms with high accuracy and R-square."
problem_and_motivation: "Poverty measurement is costly and time-consuming, and existing methods suffer from sampling errors. Indigenous communities have complex socioeconomic conditions that are often studied qualitatively, lacking disaggregated quantitative measures. This gap hinders effective policy targeting."
approach:
  - "Uses census data from Goa, Camarines Sur, covering all households including indigenous communities, with 15 multidimensional socioeconomic indicators."
  - "Applies econometric models (logit and probit) to establish causal relationships between predictors and poverty status."
  - "Trains and compares multiple machine learning regressors and classifiers: random forest, XGBoost, LightGBM, SVM, AdaBoost, GaussianNB, and others."
  - "Evaluates model performance using RMSE, MSE, R-square, and accuracy, and uses pipeline algorithms for classification."
  - "Conducts causality tests to identify key poverty predictors, including household size, informal settler status, and indicators of health, education, and income."
findings:
  - "num: Random forest achieved the highest R-square of 0.9208 and accuracy of 0.9108 for poverty prediction."
  - "num: For the general population, 63.70% live in poverty and 51.10% lack food access."
  - "num: For indigenous communities, 82% live in poverty and 71% lack food access."
  - "Household size and informal settler status are strong positive predictors of poverty."
  - "num: Random forest had the lowest RMSE (0.3298) compared to XGBoost (0.4001) and LightGBM (0.3642) for regressors."
  - "num: In pipeline classification, random forest achieved 94.89% accuracy for indigenous communities."
key_figures_tables:
  - "Figure 2: Multidimensional poverty evaluation results → Shows deprivation across education, income, and health indicators."
  - "Figure 4: RMSE of regressors → Random forest has lowest RMSE (0.3298)."
  - "Figure 6: R-square of regressors → Random forest highest R-square (0.9208)."
  - "Figure 7: Performance evaluation classifiers → Random forest accuracy 0.9108, pipeline 94.89%."
  - "Figure 13: R-square for indigenous communities → Random forest 0.9208."
  - "Figure 14: Accuracy for indigenous communities → Random forest 90.69% random, 94.89% pipeline."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Multidimensional poverty"
    definition: "Poverty measured across multiple dimensions such as education, health, income, and living standards."
  - term: "Indigenous People (IP)"
    definition: "Members of indigenous communities in the Philippines, often marginalized."
  - term: "Deprivation"
    definition: "Lack of access to basic necessities or indicators."
critical_citations:
  - "[Alkire, 2005] — Capability approach to poverty measurement."
  - "[Foster et al., 1984] — Decomposable poverty measures."
  - "[Sobreviñas, 2020] — CBMS data for poverty dynamics."
  - "[Onsay & Rabajante, 2024] — Data brief and dataset."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Uses ML to predict poverty, demonstrating predictive modeling for financial vulnerability."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Compares multiple forecasting algorithms (RF, XGBoost, LightGBM) on socioeconomic data."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Provides systematic evaluation of ML models using RMSE, R-square, and accuracy."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Specifically evaluates classification and regression modules for predictive accuracy."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "medium"
      justification: "Methodology of model comparison can inform evaluation of recommendation systems."
  contribution: "This paper demonstrates the feasibility of using machine learning for predictive classification of economic vulnerability, which can inform spending forecasting and anomaly detection modules in Odin. The systematic evaluation framework comparing multiple algorithms provides a template for selecting optimal models for Odin's algorithmic components. The causal identification of poverty predictors using econometrics can guide feature engineering for user profiling and budget recommendation. The replicable methodology using publicly available census data supports data-driven policy targeting, which aligns with Odin's goal of personalized financial management."
  directly_justifies:
    - "Random forest can achieve over 90% accuracy in classifying poverty status."
    - "Household size and informal settler status are strong predictors of economic status."
    - "Econometric causal testing can identify relevant predictors for ML models."
    - "The methodology is replicable for other regions with available data."
  limits:
    - "The paper focuses on poverty, not spending behavior, limiting direct applicability to expenditure forecasting."
    - "The data is cross-sectional, not time-series, so temporal spending patterns are not modeled."
    - "Models are trained on rural indigenous communities, which may not generalize to urban young professionals."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was conducted. Domains flagged as relevant include Spending Forecasting (6) and System Evaluation (12), as the paper directly addresses predictive modeling and algorithm evaluation. Specifically, topic 6.A and 6.B were assigned high relevance due to the use of ML for prediction and comparison of algorithms. Topics 12.A and 12.B were assigned high relevance for the evaluation frameworks and module assessment; 12.C received medium relevance as the evaluation methodology could inform budget recommendation systems. Domains related to Filipino cultural context (2), expense categorization (3), existing systems (4), behavioral profiling (5), budget recommendation (7), anomaly detection (8), mobile-first design (9), data privacy (10), user retention (11), and savings/debt management (13) were considered but rejected because the paper does not address these topics; it focuses on poverty measurement rather than personal finance management. The overall relevance to Odin is moderate, providing methodological inspiration for predictive modules rather than direct content."
limitations:
  - "Cross-sectional data limits temporal forecasting capabilities. [unacknowledged]"
  - "Models are not validated on external datasets, reducing generalizability. [unacknowledged]"
  - "The paper does not address real-time or sequential data, which are central to PFMS. [unacknowledged]"
  - "The focus on indigenous communities may not represent the broader Filipino young professional demographic. [unacknowledged]"
remember_this:
  - "Random forest achieved 0.9208 R-square and 0.9108 accuracy for poverty prediction."
  - "Household size and informal settler status are key poverty predictors."
  - "The study demonstrates cost-effective poverty measurement using ML."
  - "Causal econometric testing identifies robust predictors for ML models."
  - "Methodology is replicable with available census data."
```
---

## Paper 10: Mienye et al-2024_summarized.md

**Source File:** `Mienye et al-2024_summarized.md`

```yaml
paper_id: 1b9f8a2c-7d3e-5b2a-9c4d-8e6f1a3b7c5d
designation: international
title: "Recurrent Neural Networks: A Comprehensive Review of Architectures, Variants, and Applications"
authors: "Mienye, I. D.; Swart, T. G.; Obaido, G."
year: 2024
venue: "Information"
odin_topics:
  - "6.A"
  - "6.B"
  - "8.A"
  - "8.B"
  - "5.C"
  - "7.B"
  - "7.A"
  - "9.A"
  - "10.A"
  - "12.A"
tldr: "This review comprehensively surveys RNN architectures, variants, and applications, highlighting their role in modeling sequential data for domains relevant to personal finance systems."
problem_and_motivation: "RNNs are powerful for sequential data, but a comprehensive, up-to-date review covering recent architectural innovations and broad applications is lacking. This gap hinders researchers from effectively leveraging the latest RNN advancements across diverse fields."
approach:
  - "This paper is a comprehensive literature review of RNNs, covering fundamental architectures, advanced variants, and innovations."
  - "It systematically categorizes RNN types including LSTM, GRU, BiLSTM, ESNs, and IndRNN, detailing their mechanisms and equations."
  - "The review surveys applications across diverse domains such as NLP, speech recognition, time series forecasting, and anomaly detection."
  - "It discusses recent innovations like hybrid CNN-RNN models, attention mechanisms, and transformer integrations."
  - "The paper also covers training challenges, optimization techniques, and future research directions for RNNs."
findings:
  - "num: LSTM and GRU architectures effectively mitigate the vanishing gradient problem, enabling learning of long-term dependencies."
  - "num: Bidirectional RNNs improve performance in tasks requiring context from both past and future by processing sequences in both directions."
  - "num: Hybrid models combining CNNs and RNNs, or RNNs with attention, achieve state-of-the-art results in complex sequence tasks."
  - "RNNs have been successfully applied to time series forecasting, anomaly detection, and natural language processing, areas relevant to PFMS."
  - "Challenges including scalability, interpretability, and data dependency remain open research problems for RNNs."
key_figures_tables:
  - "Figure 1: Basic RNN architecture → Shows recurrent connections enabling sequence processing."
  - "Figure 2: LSTM cell architecture → Illustrates input, forget, and output gates for long-term memory."
  - "Figure 3: BiLSTM architecture → Depicts forward and backward processing for full context."
  - "Figure 4: Stacked LSTM → Shows hierarchical feature learning via multiple LSTM layers."
  - "Figure 5: GRU architecture → Demonstrates simplified gating with update and reset gates."
key_equations:
  - equation: "h_t = σ_h(W_xh x_t + W_hh h_{t-1} + b_h)"
    explanation: "Standard RNN hidden state update equation."
  - equation: "i_t = σ(W_xi x_t + W_hi h_{t-1} + b_i)"
    explanation: "LSTM input gate controls new information flow."
  - equation: "f_t = σ(W_xf x_t + W_hf h_{t-1} + b_f)"
    explanation: "LSTM forget gate regulates memory retention."
  - equation: "c_t = f_t ⊙ c_{t-1} + i_t ⊙ g_t"
    explanation: "LSTM cell state update combining old and new memory."
  - equation: "z_t = σ(W_xz x_t + W_hz h_{t-1} + b_z)"
    explanation: "GRU update gate balances old and new hidden states."
definitions:
  - term: "RNN"
    definition: "Recurrent Neural Network, a class of neural networks designed to process sequential data by maintaining a hidden state."
  - term: "LSTM"
    definition: "Long Short-Term Memory, an RNN variant with gating mechanisms to handle long-term dependencies."
  - term: "GRU"
    definition: "Gated Recurrent Unit, a simplified LSTM variant with fewer gates."
  - term: "BiLSTM"
    definition: "Bidirectional LSTM, processes sequences in both forward and backward directions for better context."
  - term: "ESN"
    definition: "Echo State Network, an RNN with a fixed, randomly connected reservoir and only the output layer trained."
  - term: "BPTT"
    definition: "Backpropagation Through Time, the algorithm used to train RNNs by unrolling the network through time."
  - term: "IndRNN"
    definition: "Independently Recurrent Neural Network, uses independent recurrent units to address gradient issues."
critical_citations:
  - "[Hochreiter and Schmidhuber, 1997] — Introduced LSTM to solve vanishing gradient problem."
  - "[Cho et al., 2014] — Proposed GRU as a simplified alternative to LSTM."
  - "[Vaswani et al., 2017] — Introduced Transformer architecture, impacting RNN applications."
  - "[Greff et al., 2016] — Provided extensive comparison of LSTM variants."
  - "[Bahdanau et al., 2014] — Introduced attention mechanisms for RNNs in translation."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Directly reviews time series forecasting algorithms applicable to spending prediction."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "high"
      justification: "Discusses LSTM and GRU for sequential data, core to forecasting."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews anomaly detection applications using RNNs on time series data."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "medium"
      justification: "Covers BiLSTM and other models for detecting deviations in sequential data."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "contextual"
      justification: "Relevant as a background for classification using RNNs, though not PFMS-specific."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "low"
      justification: "Provides general background on RNNs but no specific budgeting strategies."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "contextual"
      justification: "Provides general context on sequential data modeling which is foundational."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "low"
      justification: "Not directly addressed; papers focuses on algorithms not UX."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "contextual"
      justification: "Discusses data dependency but not privacy specifically."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "contextual"
      justification: "Mentions evaluation but does not provide PFMS-specific frameworks."
  contribution: "This review provides a foundational understanding of RNN architectures, directly justifying the selection of LSTM and GRU for Odin's spending forecasting module. The detailed comparison of algorithms supports the design of Odin's anomaly detection system by identifying suitable sequence models. It also informs the behavioral profiling module by reviewing classification approaches for sequential data. Furthermore, the discussion of training challenges and innovations offers guidance for implementing robust forecasting and detection algorithms within Odin."
  directly_justifies:
    - "LSTM and GRU networks are well-suited for time series forecasting of spending data."
    - "Bidirectional LSTM can enhance anomaly detection by capturing context from both past and future spending patterns."
    - "Hybrid models combining CNN and RNN can be used for feature extraction and temporal modeling."
    - "Attention mechanisms can improve forecasting accuracy by focusing on relevant spending periods."
  limits:
    - "The review does not provide empirical comparisons or benchmarks specific to personal finance datasets."
    - "The discussion of user behavior and cold-start problems is limited, as it is a general review."
    - "Implementation details or specific parameter tuning for PFMS are not addressed."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. Domains related to algorithmic core functions were flagged as relevant. Specifically, 'Spending Forecasting' (6.A, 6.B) received high relevance due to the paper's extensive review of LSTM, GRU, and hybrid models for time series prediction, which are directly applicable to Odin's forecasting module. 'Anomaly Detection' (8.A, 8.B) was assessed as medium relevance because the review covers RNN applications for detecting deviations in sequential data, supporting Odin's anomaly detection feature. 'Behavioral Profiling' (5.C) was deemed contextual, as the paper reviews classification approaches for sequences but lacks PFMS-specific user profiling. 'Budget Recommendation' (7.A, 7.B) was considered low relevance as the paper does not discuss budgeting strategies or optimization constraints. Domains like 'Filipino Cultural Context', 'Expense Categorization', 'User Retention', and 'Savings & Debt Management' were considered and rejected as the paper does not address these socio-technical or PFMS-specific design aspects. The paper's overall relevance lies in providing a strong algorithmic foundation for Odin's core predictive and detection capabilities, though it lacks direct application to the Filipino context or specific PFMS design challenges."
limitations:
  - "The review does not include a systematic meta-analysis of performance metrics across studies. [unacknowledged]"
  - "It focuses on algorithmic advancements and does not deeply address user-centric issues like trust or mobile-first design."
  - "The paper is a high-level review and lacks specific implementation guidance for personal finance systems."
  - "Potential biases in RNN models and their impact on fairness are mentioned but not thoroughly explored. [unacknowledged]"
remember_this:
  - "LSTM and GRU are key RNN variants for long-term dependency modeling."
  - "Hybrid models with attention mechanisms enhance performance in sequence tasks."
  - "RNNs are effective for time series forecasting and anomaly detection in spending data."
  - "BiLSTM processes context from both past and future for improved accuracy."
  - "Challenges include scalability, interpretability, and data quality issues."
```
---

## Paper 11: Asemi et al-2024_summarized.md

**Source File:** `Asemi et al-2024_summarized.md`

```yaml
paper_id: 10.1186/s40537-024-00965-y
designation: international-algorithm-specific
title: A model for investment type recommender system based on the potential investors based on investors and experts feedback using ANFIS and MNN
authors: Asemi, A.; Asemi, A.; Ko, A.
year: 2024
venue: Journal of Big Data
odin_topics:
- 1.A
- 1.B
- 1.C
- 2.D
- 3.C
- 5.A
- 5.C
- 7.A
- 7.B
- 7.C
- 8.A
- 12.B
- 13.C
tldr: An ANFIS-MNN hybrid recommender system predicts investment types using clustered investor data, achieving a 0.667 F1-score and 0.721 RMSE.
problem_and_motivation: Investors struggle with complex markets and overwhelming data, making informed decisions difficult. Existing recommender systems rely on limited inputs and cannot adapt to dynamic feedback or conditions. A personalized, adaptive system is needed to match investor profiles with suitable investment products.
approach:
- Data was collected via a web questionnaire from 1542 respondents across eight categories including demographics, finances, and traits.
- Data was preprocessed using ETL tools, JMP, MATLAB, and Python, then clustered using K-Means with Elbow Curve and Silhouette score.
- An ANFIS model was designed with three clustered inputs and one output, trained with a hybrid approach over three epochs using 188 data pairs and 18 fuzzy rules.
- Multimodal Neural Network pretraining was applied to initialize ANFIS weights, enhancing accuracy and generalization.
- The system incorporates expert feedback and investor opinions to refine rules and recommendations, evaluated using RMSE, accuracy, precision, recall, and F1-score.
findings:
- num: The ANFIS model achieved a minimal training RMSE of 0.721054.
- num: The model achieved an F1-score of 0.6667, indicating reasonably good precision and recall.
- num: Multimodal neural network pretraining resulted in a test MSE of 0.0011995.
- The ANFIS-based system outperformed traditional methods like decision trees and logistic regression.
- The system successfully generates personalized investment recommendations based on clustered investor profiles.
- Expert and investor feedback effectively customizes and improves the system's recommendations.
key_figures_tables:
- Figure 1: Data and fuzzy function for ANFIS model → Shows 3 inputs for investor clusters and 1 output for investment product clusters.
- Figure 2: Trained and tested grid of the ANFIS system → Visualizes the trained ANFIS structure with 18 fuzzy rules.
- Figure 3: Proposed ANFIS structure → Depicts the complete ANFIS architecture including fuzzification, rules, and defuzzification.
- Table 1: Description of research methodology → Outlines the seven stages from data collection to final predictions.
- Table 2: Description of data preprocessing → Details the eight data columns and their clustering techniques.
key_equations:
- equation: "None."
  explanation: ""
definitions:
- term: ANFIS
  definition: Adaptive Neuro-Fuzzy Inference System, a hybrid of fuzzy logic and neural networks.
- term: IRS
  definition: Investment Recommender System, a system that suggests investment products to users.
- term: MNN
  definition: Multimodal Neural Network, a neural network that learns from multiple data modalities.
- term: RMSE
  definition: Root Mean Square Error, a metric for prediction error.
- term: MF
  definition: Membership Function, a function that maps inputs to fuzzy sets.
critical_citations:
- "[Jang, 1993] — Introduced the ANFIS architecture foundational to this work."
- "[Asemi & Ko, 2021] — Proposed a combined business recommender system using customer feedback."
- "[Asemi et al., 2023] — Applied ANFIS to customize investment types based on demographics."
- "[Chen et al., 2021] — Proposed a machine learning model for Robo-advisor investment classification."
relevance:
  topics:
  - code: 1.A
    name: Filipino Young Professionals as a Demographic
    relevance: low
    justification: Paper focuses on investors generally but provides a demographic profiling framework.
  - code: 1.B
    name: Financial Structure of Filipino Young Professionals
    relevance: low
    justification: Discusses financial inputs like income and savings but not specific to Filipinos.
  - code: 1.C
    name: Financial Behavior of Filipino Young Professionals
    relevance: low
    justification: Covers investment behavior and decision-making, but not culturally specific.
  - code: 2.D
    name: Filipino Spending Cycles and "Occasions"
    relevance: contextual
    justification: Provides a framework for modeling investor behavior, but no specific seasonal analysis.
  - code: 3.C
    name: User-Defined Allocation Constraints
    relevance: medium
    justification: System takes user preferences as input, but constraints are not explicitly modeled as constraints.
  - code: 5.A
    name: Financial Behavioral Profiles in Personal Finance
    relevance: high
    justification: Core contribution is clustering investors into behavioral profiles for recommendations.
  - code: 5.C
    name: Classification Approaches for Financial Behavioral Profiles
    relevance: high
    justification: Uses ANFIS to classify investors into investment types based on multiple trait clusters.
  - code: 7.A
    name: Budgeting Strategies as Domain Knowledge
    relevance: low
    justification: Focuses on investment recommendation, not budgeting, but similar strategy-domain mapping.
  - code: 7.B
    name: Budget Recommendation in Personal Finance Systems
    relevance: low
    justification: System is for investment products, not budget allocation, but similar recommendation mechanism.
  - code: 7.C
    name: Constrained Optimization Approaches for Budget Allocation
    relevance: low
    justification: Does not use optimization; uses ANFIS for prediction.
  - code: 8.A
    name: Anomaly Detection in Personal Finance Systems
    relevance: contextual
    justification: Mentions error correction and refinement but not explicitly for anomaly detection.
  - code: 12.B
    name: Evaluation of Algorithmic Modules
    relevance: high
    justification: Thoroughly evaluates the ANFIS and MNN modules using RMSE, F1-score, accuracy, precision, and recall.
  - code: 13.C
    name: End-of-Period Surplus as a Savings Input
    relevance: low
    justification: System predicts investment types, not savings from surplus, but user's financial status is considered.
  contribution: This paper provides a framework for behavioral profiling through clustering (5.A, 5.C) and a hybrid machine learning method for classification (ANFIS) that could be adapted for expense categorization (3.A) or spending forecasting (6.A). Its evaluation methodology (12.B) offers metrics (RMSE, F1-score) for testing Odin's algorithmic modules. The system's use of user feedback and expert rules could inform Odin's user constraint handling (3.C) and budget recommendation logic (7.B).
  directly_justifies:
  - "ANFIS models can effectively classify investors based on multi-dimensional clustered inputs."
  - "Hybrid training approaches produce robust predictions for financial product recommendations."
  - "Multimodal neural network pretraining improves the accuracy and generalization of ANFIS models."
  - "Incorporating expert and user feedback enhances the relevance of recommender system outputs."
  limits:
  - "The system requires a significant amount of data to train, which may be impractical for smaller firms or individual users."
  - "The system is designed for retail investors and may not be suitable for institutional investors or complex portfolios."
  - "Potential biases in historical data could perpetuate existing inequalities in investment recommendations. [unacknowledged]"
  mapping_rationale: A systematic scan was conducted across all 12 functional domains and their associated topic codes. The domains flagged as relevant were Behavioral Profiling & Classification (high for 5.A, 5.C), System Evaluation (high for 12.B), and to a lesser extent, Expense Categorization (medium for 3.C), and Spending Forecasting (contextual for 8.A). The paper's primary contribution is algorithmic (ANFIS-MNN) for classifying investors into behavioral profiles, making 5.A and 5.C core. Its evaluation metrics directly support 12.B. The user-input aspects touch on 3.C, and the dynamic adaptation could relate to 8.A, but these are secondary. Domains like Filipino Cultural Context (2.A-D) and Mobile-First Design (9.A-B) were considered but rejected as the paper does not address cultural or mobile specifics. The paper is of high relevance to Odin's behavioral classification and algorithm evaluation modules, offering a validated approach and evaluation framework.
limitations:
- "The system requires a significant amount of data to train the ANFIS model."
- "The system is designed for retail investors and may not be suitable for institutional investors or complex portfolios."
- "Potential biases in historical data could perpetuate existing inequalities in investment recommendations. [unacknowledged]"
remember_this:
- "ANFIS achieved a 0.667 F1-score for investment type prediction."
- "The model's RMSE was 0.721, indicating moderate prediction accuracy."
- "Multimodal pretraining resulted in a very low test MSE of 0.0012."
- "Clustering investors into profiles enables personalized financial recommendations."
- "Expert feedback loops are effective for refining rule-based recommender systems."
```
---

## Paper 12: Hovakimyan & Bravo_summarized.md

**Source File:** `Hovakimyan & Bravo_summarized.md`

```yaml
paper_id: 10.3390/info15120786
designation: international-algorithm-specific
title: Evolving Strategies in Machine Learning: A Systematic Review of Concept Drift Detection
authors: Hovakimyan, G.; Bravo, J. M.
year: 2024
venue: Information
odin_topics:
  - "6.A"
  - "6.B"
  - "8.A"
  - "8.B"
  - "2.B"
  - "2.D"
  - "4.B"
  - "12.A"
  - "12.B"
tldr: A systematic review categorizes concept drift detection methods into drift detection mechanisms, window-based mechanisms, unsupervised methods, ensembles, and neural networks, highlighting their strengths, weaknesses, and application domains.
problem_and_motivation: Machine learning models degrade in performance when underlying data distributions change over time, a phenomenon known as concept drift. This review addresses the gap in a consolidated understanding of the diverse and rapidly evolving strategies for detecting and adapting to such drifts. A systematic synthesis is needed to guide practitioners in selecting appropriate methods and to identify future research directions.
approach:
  - Followed PRISMA guidelines to conduct a systematic literature review on concept drift detection.
  - Used the T5 NLP model to screen 356 initial studies, narrowing them to 254 for full review.
  - Employed IEEE and ScienceDirect APIs with specific search terms to identify 490 potential studies.
  - Performed a quality assessment using adapted Newcastle-Ottawa Scale and CASP checklists.
  - Categorized 65 high-impact studies based on drift type, detection method, and dataset characteristics.
findings:
  - num: 51 out of 111 assessed studies (45%) were of high methodological quality.
  - num: 15 studies (14%) were of low quality and considered with caution.
  - Ensembles and neural networks offer very high accuracy but come with high computational costs.
  - Drift detection mechanisms and window-based methods provide a balance between accuracy and efficiency.
  - Unsupervised methods excel in detecting novel classes in scenarios with sparse labeled data.
  - Imbalanced data, computational efficiency, and non-tabular data remain significant challenges.
key_figures_tables:
  - "Table 1: Summary of quality assessment scores → 45% of studies are high quality."
  - "Table 3: Summary of characteristics of included studies → Categorizes methods by drift type and findings."
  - "Table 4: Comparison of concept drift detection methods → Accuracy and computational cost trade-offs."
  - "Table 5: Summary of datasets used for concept drift detection → Lists common synthetic and real-world datasets."
  - "Figure 3: PRISMA flow diagram → Shows selection process from 490 to 65 included studies."
key_equations:
  - equation: "Acc_{t+1} = \\frac{t \\times Acc_t + \\delta_{t+1}}{t+1}"
    explanation: "Prequential error for incremental accuracy calculation."
  - equation: "Adjusted Citation Rate = \\frac{Total Number of Citations}{Years Since Publication}"
    explanation: "Metric used to identify influential articles."
definitions:
  - term: "Concept Drift"
    definition: "Changes in the statistical properties of the target variable over time, degrading model performance."
  - term: "Virtual Drift"
    definition: "Changes in the distribution of input features P(X) without altering P(Y|X)."
  - term: "Real Drift"
    definition: "Changes in the conditional probability P(Y|X), affecting model accuracy."
  - term: "DDM"
    definition: "Drift Detection Mechanism, a method monitoring error rates to detect drifts."
  - term: "WBM"
    definition: "Window-Based Mechanism, a method using sliding or adaptive windows to manage data streams."
  - term: "USSM"
    definition: "Unsupervised and Semi-Supervised Method, techniques using clustering or density estimation for drift detection."
  - term: "EM"
    definition: "Ensemble Method, a technique combining multiple models for improved accuracy and robustness."
  - term: "NN"
    definition: "Neural Network, a deep learning approach for detecting complex drifts."
  - term: "ELM"
    definition: "Extreme Learning Machine, a fast neural network variant using single-step least square estimation."
  - term: "MOA"
    definition: "Massive Online Analysis, an open-source framework for data stream mining."
critical_citations:
  - "[Gama et al., 2004] — Introduced the DDM, a foundational benchmark algorithm."
  - "[Nishida and Yamauchi, 2007] — Introduced the influential STEPD algorithm."
  - "[Bifet and Gavalda, 2007] — Developed ADWIN for adaptive windowing."
  - "[Brzezinski and Stefanowski, 2014] — Proposed the OAUE ensemble method."
  - "[Lobo et al., 2018] — Demonstrated evolving spiking neural networks for drifting streams."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews forecasting algorithms applicable to financial time series."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "medium"
      justification: "Examines algorithms like LSTM suitable for sequential financial data."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews detection methods relevant for identifying fraudulent transactions."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "low"
      justification: "Discusses algorithmic approaches for detecting changes, including novel classes."
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "contextual"
      justification: "Concepts of recurrent drift inform understanding of seasonal spending behavior."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "contextual"
      justification: "The concept of recurring drift provides a framework for understanding cyclical Filipino spending."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "low"
      justification: "Highlights general limitations like handling imbalanced data that also apply to PFMS."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "low"
      justification: "Discusses evaluation metrics like prequential error and handling imbalanced classification."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "low"
      justification: "Details metrics for comparing algorithm performance, such as accuracy and computational cost."
  contribution: "This paper provides a comprehensive taxonomy of concept drift detection methods, offering a structured framework for selecting algorithms for dynamic data environments. Its systematic comparison of methods based on accuracy, computational cost, and applicability can inform the design of adaptive modules for a PFMS. The review's identification of key challenges, such as handling imbalanced data and non-tabular data, directly relates to obstacles in personal finance anomaly detection and user behavior forecasting. The detailed analysis of evaluation metrics and benchmarking datasets provides a methodological foundation for testing Odin's algorithmic components. The synthesis of adaptive learning strategies from related fields is applicable to building robust and responsive modules within a personal finance management system."
  directly_justifies:
    - "Ensemble methods and neural networks provide the highest accuracy for concept drift detection."
    - "Handling imbalanced data is a significant challenge for many detection algorithms."
    - "Computational efficiency is critical for real-time detection in streaming environments."
    - "Unsupervised methods are effective for novel class detection in scenarios with limited labels."
    - "There is a need for standardized evaluation protocols that include detection delay and resource usage."
  limits:
    - "Focuses on concept drift in general, not specifically tailored to personal finance or spending data."
    - "The reviewed methods are primarily designed for tabular data, limiting their direct application to other data types."
    - "The comparative analysis is based on existing literature and may not represent a unified empirical benchmark."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains of 'Spending Forecasting' (6.A, 6.B) and 'Anomaly Detection' (8.A, 8.B) were identified as highly relevant due to the paper's focus on predictive algorithms for dynamic data streams. The domain of 'Filipino Cultural Context' (2.B, 2.D) was considered relevant only contextually, as the concept of recurrent drift can frame seasonal spending cycles but the paper does not address Filipino culture directly. The domains of 'Existing Systems & Gaps' (4.B) and 'System Evaluation' (12.A, 12.B) were deemed relevant at a low level due to the review's discussion of system limitations and evaluation metrics. Domains like 'Behavioral Profiling', 'Budget Recommendation', 'Mobile-First Design', 'Data Privacy', 'User Retention', and 'Savings & Debt Management' were considered and rejected because the paper does not address user behavior, recommendation systems, privacy, engagement, or financial goal management. Overall, the paper's primary value to Odin is its comprehensive and structured overview of algorithmic strategies for adapting to changing data, which is foundational for building robust forecasting and anomaly detection modules."
limitations:
  - "The review primarily focuses on classification tasks, leaving a gap in understanding concept drift for regression tasks. [unacknowledged]"
  - "Computational efficiency of many methods remains a challenge for real-time applications. [acknowledged]"
  - "The majority of studies use synthetic or controlled datasets, which may not fully capture real-world complexities. [acknowledged]"
  - "Concept drift detection in non-tabular data like images is underexplored. [acknowledged]"
  - "There is a limited focus on unsupervised drift detection methods for scenarios with scarce labeled data. [acknowledged]"
remember_this:
  - "Concept drift degrades model performance as data distributions evolve over time."
  - "No single method dominates; best choice depends on the specific drift type and application."
  - "Ensemble methods achieve high accuracy but at a high computational cost."
  - "Handling imbalanced data and non-tabular data are key unresolved challenges."
  - "num: 45% of reviewed studies were of high methodological quality based on the assessment criteria."
```
---

## Paper 13: Chatterjee & Das_summarized.md

**Source File:** `Chatterjee & Das_summarized.md`

```yaml
paper_id: 10.60087/jklst.v4.n1.012
designation: international-algorithm-specific
title: Adaptive Financial Recommendation Systems Using Generative AI and Multimodal Data
authors: Chatterjee, P.; Das, A.
year: 2024
venue: Journal of Knowledge Learning and Science Technology
odin_topics:
  - 1.C
  - 5.A
  - 6.A
  - 7.B
  - 8.A
  - 10.A
  - 10.B
  - 12.A
  - 12.B
  - 12.C
tldr: Generative AI framework using LLMs and multimodal data for personalized financial product recommendations, achieving up to 30% improvement in relevance and 25% increase in user engagement over traditional baselines.
problem_and_motivation: Traditional financial recommendation engines rely on static rules or shallow models that fail to adapt to dynamic consumer behavior, life events, and non-numeric signals like intent or financial literacy. There is a need for systems that are deeply personalized, context-aware, and responsive to real-time changes in user financial behavior.
approach:
  - Data ingestion layer processes structured data (transaction logs, credit history) and unstructured data (chat transcripts, surveys) from mobile apps and APIs.
  - User profiling engine uses unsupervised learning to cluster personas and dynamically account for financial volatility, risk perception, and behavioral shifts.
  - Generative model layer fine-tunes LLMs prompted with user context and financial goals to generate scenario-specific product narratives.
  - Recommendation refinement module uses GANs or policy-gradient models to evaluate and refine outputs for coherence, accuracy, and regulatory alignment.
  - Reinforcement learning loop implements RLHF using user feedback to tune model weights over time for personalization and drift correction.
  - Ethical and XAI layer applies SHAP, LIME, and counterfactual testing for fairness auditing and compliance, generating visual dashboards for interpretability.
  - System architecture supports modular integration with digital banking APIs and deployment across neobanks and financial wellness apps.
  - Evaluation uses synthetic yet realistic datasets from the AlphaCredit Persona Generator Toolkit, benchmarked against collaborative filtering and neural recommender baselines.
findings:
  - num: 28-35% improvement in Top-N precision and recall for the GenAI system compared to traditional models.
  - num: 22% increase in engagement duration for models trained with feedback loops.
  - num: 18% higher acceptance of recommended financial products with feedback integration.
  - num: 36% reduction in product rejection rate compared to models without feedback integration.
  - num: 23% reduction in disparate impact scores when fairness constraints are applied.
  - num: 18% increase in equal opportunity scores with fairness constraints versus unconstrained baseline.
  - Users exposed to transparent, data-backed recommendations showed a 40% higher engagement rate compared to those receiving opaque suggestions.
  - The system demonstrated high personalization accuracy in cold-start scenarios where traditional models often fail.
  - The proposed framework reduces bias and improves fairness metrics through preprocessing and optimization constraints.
  - Explainability modules enhance user trust and regulatory compliance in financial AI deployments.
key_figures_tables:
  - Figure 1: Simulated User Cohorts → Visualization of five distinct simulated user persona groups for testing.
  - Figure 2: Evaluation Metrics Performance Scores → Quantitative comparison of key performance metrics across evaluation dimensions.
  - Figure 3: Result and Analysis Metrics Overview → Summary of personalization accuracy, fairness, and transparency results.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: GenAI
    definition: Generative Artificial Intelligence; AI systems capable of generating new content based on training data.
  - term: LLM
    definition: Large Language Model; a type of AI model trained on vast text data to understand and generate human-like language.
  - term: RLHF
    definition: Reinforcement Learning from Human Feedback; a technique using human preferences as a reward signal to train AI models.
  - term: GAN
    definition: Generative Adversarial Network; a class of machine learning frameworks where two neural networks contest with each other.
  - term: XAI
    definition: Explainable AI; a set of processes and methods that allows human users to understand and trust the results and output created by machine learning algorithms.
  - term: SHAP
    definition: SHapley Additive exPlanations; a method based on cooperative game theory to explain the output of machine learning models.
  - term: LIME
    definition: Local Interpretable Model-agnostic Explanations; an algorithm to explain the predictions of any classifier or regressor.
  - term: EaaS
    definition: Explainability-as-a-Service; a modular deployment of explainability components as a separate microservice.
critical_citations:
  - "[Ribeiro et al., 2016] — Foundational for model-agnostic explainability (LIME)."
  - "[Mehrabi et al., 2021] — Core reference for bias and fairness in machine learning."
  - "[Chien et al., 2022] — Relevant for deep learning in financial product recommendations."
  - "[Ghosh et al., 2023] — Key for explainable AI techniques specifically in finance."
  - "[Das et al., 2020] — Critical for fairness metrics and explanation methods in financial services."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: contextual
      justification: Provides framework for behavioral profiling and spending analysis.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly proposes dynamic behavioral segmentation and user profiling engine.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Uses time-series modeling and user embeddings for adaptive forecasting.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: Proposes GenAI-based product recommendation akin to budget allocation advice.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Discusses detection of anomalous behaviors and cold-start handling.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Embeds differential privacy and federated learning principles for privacy.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Uses explainability and transparency to build and measure user trust.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Establishes comprehensive KPIs for quantitative and qualitative evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Benchmarks GenAI against collaborative filtering, matrix factorization, and neural networks.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: medium
      justification: Uses relevance scoring and engagement metrics applicable to budget recommendation.
  contribution: "This paper provides a full-stack blueprint for implementing a GenAI-powered financial recommendation engine for Odin, covering data ingestion, behavioral profiling, generative recommendation, reinforcement learning from feedback, and explainable AI layers. The architectural design directly informs the development of Odin's budget recommendation and personalization modules. The emphasis on ethical AI, privacy-preserving techniques, and bias mitigation aligns with Odin's need for user trust and regulatory compliance. The proposed XAI layer offers a method for generating user-friendly justifications for recommendations, which is crucial for Odin's transparency goals. The modular architecture supports integration with Odin's existing or planned mobile-first infrastructure."
  directly_justifies:
    - "Generative AI framework outperforms traditional models in cold-start scenarios for financial recommendations."
    - "User feedback loops improve long-term recommendation relevance and engagement by 18-36%."
    - "Explainability layers are critical for building user trust and ensuring regulatory compliance in fintech."
    - "Fairness-aware modeling reduces disparate impact by 23% in simulated financial recommendation settings."
    - "Multimodal data integration enhances contextual understanding of user financial behavior."
  limits:
    - "Use of synthetic datasets limits validation of privacy and fairness claims in real-world scenarios."
    - "Lack of real demographic identifiers in datasets constrains precise fairness validation."
    - "Trade-offs between model accuracy and fairness constraints remain underexplored in production environments."
    - "Intersectional fairness considering combined attributes needs further research."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant to domains including Filipino Financial Behavior, Spending Forecasting, Budget Recommendation, Anomaly Detection, Data Privacy, User Trust, and System Evaluation. Specific topic codes selected were: 1.C (contextual as it informs financial behavioral analysis), 5.A (high, direct proposal of a user profiling engine), 6.A (high, uses time-series modeling for prediction), 7.B (high, GenAI-based product recommendation akin to budget allocation), 8.A (medium, discusses anomaly behavior detection), 10.A (high, embeds privacy-preserving methods), 10.B (high, uses explainability for trust), 12.A (high, establishes comprehensive evaluation KPIs), 12.B (high, benchmarks against baselines), and 12.C (medium, uses relevance and engagement metrics). Borderline cases included the paper's financial behavior analysis touching 1.C and 5.A, resolved by selecting 5.A as primary and 1.C as contextual. The spending pattern analysis on seasonal spending could relate to 2.B, but the paper does not specifically address cyclical patterns or Filipino cultural context, so 2.B was rejected. Similarly, topics under Savings & Debt Management (13.A, 13.B, 13.C) were rejected as the paper focuses on product recommendations rather than goal management or surplus allocation. The overall relevance to Odin is high, providing a comprehensive architectural framework for personalization, recommendation, and ethical AI compliance."
limitations:
  - "Absence of real demographic identifiers in anonymized datasets limits precise fairness validation. [unacknowledged]"
  - "Trade-offs between model accuracy and fairness constraints need further exploration in production environments. [acknowledged]"
  - "More research is needed to account for intersectional fairness in bias assessment. [acknowledged]"
  - "Reliance on synthetic datasets may not fully capture the complexity of real-world financial behaviors. [unacknowledged]"
remember_this:
  - "Generative AI improves financial recommendation relevance by up to 30% over traditional methods."
  - "User feedback loops increase engagement duration by 22% and reduce rejection rates by 36%."
  - "Fairness constraints reduce disparate impact by 23% without sacrificing recommendation accuracy."
  - "Explainability and transparency are critical for building user trust and regulatory compliance."
  - "Modular architecture with RLHF enables continuous personalization and adaptation to user drift."
```
---

## Paper 14: Garg et al-2024_summarized.md

**Source File:** `Garg et al-2024_summarized.md`

```yaml
paper_id: 10.63282/3050-9246.IJETCSIT-V5I3P105
designation: international-algorithm-specific
title: A Multi-Layered AI-IoT Framework for Adaptive Financial Services
authors: Garg, A.; Pandey, M.; Pathak, A. R.
year: 2024
venue: International Journal of Emerging Trends in Computer Science and Information Technology
odin_topics:
  - 4.A
  - 4.B
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 9.A
  - 9.B
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 12.A
  - 12.B
  - 13.A
tldr: An AI-IoT framework with input, intelligence, and experience layers provides real-time, adaptive, and personalized banking services using edge computing and federated learning.
problem_and_motivation: Traditional banking systems cannot effectively act upon rich contextual data from IoT devices. A unified framework for AI-IoT integration is missing, which hinders real-time personalization and fraud detection. This gap limits the delivery of intelligent and secure financial experiences.
approach:
  - The paper employs a design science methodology to construct a conceptual framework for AI-IoT integration in banking.
  - The framework consists of three layers: Input (IoT endpoints), Intelligence (AI analytics), and Experience (service delivery).
  - The architecture incorporates edge computing to reduce latency and federated learning to enhance privacy.
  - A zero-trust security model is integrated, and use cases are analyzed to demonstrate feasibility.
  - Evaluation is conducted via a comparative simulation of operational logs over a 12-month period.
findings:
  - num: Fraud detection accuracy improved from 60% to 89% after AI-IoT deployment.
  - num: False positive rate for fraud detection decreased from 39% to 11%.
  - num: Customer Satisfaction Index increased from 72 to 86 out of 100.
  - num: Average response latency for decisioning operations dropped from 2.3 seconds to 0.8 seconds.
  - The initial investment in the AI-IoT infrastructure was recovered within eight months.
  - The churn rate decreased by 14% following the implementation.
key_figures_tables:
  - Table 1: Applications of IoT and AI in Banking → Summarizes use cases like smart ATMs and fraud detection.
  - Table 2: Traditional Banking vs. AI-IoT Integrated Banking Systems → Highlights key differences in personalization and decision-making.
  - Figure 1: Architectural Model → Visualizes the three-layer Input, Intelligence, Experience framework.
  - Figure 2: Comparison of Fraud Incidents Before and After AI-IoT Implementation → Illustrates a hypothetical reduction in fraud cases.
  - Table 3: Real-World Applications of AI-IoT Convergence in Banking → Maps use cases to IoT role, AI enhancement, and banking impact.
key_equations:
  - equation: "$CRS_i = \sum_{j=1}^{n} w_j \cdot f_j(x_i)$"
    explanation: Defines a dynamic credit risk score based on weighted behavioral features.
  - equation: "$A(x) = \frac{||x - \mu||^2}{\sigma^2}$"
    explanation: Computes an anomaly score to detect potential fraud in transactions.
  - equation: "$\omega_t = \omega_{t-1} - \eta \cdot \frac{1}{K} \sum_{k=1}^{K} \nabla \iota_k(\omega)$"
    explanation: Shows federated learning update for model weights without centralizing data.
definitions:
  - term: IoT
    definition: Internet of Things, a network of physical devices that collect and exchange data.
  - term: AI
    definition: Artificial Intelligence, the simulation of human intelligence in machines.
  - term: Federated Learning
    definition: A machine learning approach that trains models across decentralized devices holding local data samples.
  - term: Zero-Trust Architecture
    definition: A security model that requires strict identity verification for every user and device trying to access resources.
  - term: Edge Computing
    definition: Data processing performed at the periphery of the network, closer to the data source.
critical_citations:
  - "[Baker and Georgakopoulos, 2019] — Foundational for IoT-enabled intelligent banking."
  - "[Yu et al., 2021] — Key for privacy-preserving federated learning in finance."
  - "[Wang and Xu, 2021] — Core reference for AI-enhanced fraud detection with IoT data."
  - "[Autade, 2023] — Cited for real-time anomaly detection in financial streams."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: The paper reviews the landscape of digital and IoT-driven banking systems.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies fragmentation and lack of integration as a key barrier to unified intelligent banking.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Discusses predictive analytics for credit scoring, fraud detection, and forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: contextual
      justification: Mentions transaction forecasting with predictive analytics but not as the central focus.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly addresses real-time fraud detection and anomaly detection in banking.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Applies ML anomaly detection algorithms to financial transaction data.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Framework supports mobile banking experiences with real-time, context-aware services.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: contextual
      justification: Mentions mobile push notifications and app interfaces but does not focus on UX design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Dedicated section on security and privacy issues like data breaches and AI ethics.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Emphasizes building trust through zero-trust architecture and explainable AI.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Hyper-personalization and emotion-aware support aim to increase engagement.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: Results show decreased churn rate due to personalization and proactive support.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses fraud detection, latency, and customer satisfaction as evaluation metrics.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: contextual
      justification: The paper evaluates AI modules like anomaly detection as part of the overall system.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: contextual
      justification: Mentions budgeting and spending suggestions but savings goals are not the focus.
  contribution: The paper provides a layered architectural blueprint for integrating AI and IoT into banking systems. This framework justifies Odin's need for a real-time, adaptive intelligence layer to process user data. The use of edge computing and federated learning offers a viable model for handling latency and privacy concerns. The emphasis on zero-trust security aligns with Odin's requirement for robust data protection. Finally, the paper's findings on fraud detection and personalization validate the strategic importance of these features.
  directly_justifies:
    - "A real-time anomaly detection system using IoT behavioral data and AI can achieve 89% fraud detection accuracy."
    - "Processing data at the edge reduces decision latency from 2.3 to 0.8 seconds for financial operations."
    - "Federated learning enables model training on user devices without moving sensitive raw data to central servers."
    - "Hyper-personalized, context-aware mobile notifications significantly improve customer satisfaction and reduce churn."
  limits:
    - "The framework is conceptual; its quantitative benefits are derived from a hypothetical simulation."
    - "Real-world challenges like legacy infrastructure integration are mentioned but not deeply analyzed."
    - "The security and privacy solutions are proposed but not empirically validated within the context of the framework."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was conducted. The domains of Existing Systems & Gaps (4.A, 4.B), Anomaly Detection (8.A, 8.B), and Data Privacy & User Trust (10.A, 10.B) were flagged as high relevance due to the paper's direct focus on system integration, real-time fraud detection, and security architecture. Medium relevance was assigned to Predictive Modeling (6.A), Mobile-First Design (9.A), and User Retention (11.A, 11.B) as the paper discusses these components but not as primary contributions. The paper was considered and rejected for codes under Behavioral Profiling & Classification (5.A-C) as its focus is on system architecture and fraud detection, not on classifying user financial profiles. The contribution is highly relevant to Odin as it validates the need for a layered, intelligent, and secure PFMS architecture with real-time capabilities.
limitations:
  - "The framework's validity is demonstrated primarily through hypothetical simulations and use cases."
  - "The paper focuses on a general banking context, not specifically on personal finance management for individuals."
  - "A detailed cost-benefit analysis for the framework in a PFMS setting is not provided. [unacknowledged]"
  - "The paper does not address the cold-start problem for anomaly detection or profiling. [unacknowledged]"
remember_this:
  - "An AI-IoT framework improved fraud detection accuracy by 48% in a simulated banking scenario."
  - "Edge computing is critical for reducing latency in real-time financial services."
  - "Federated learning is a promising technique for preserving data privacy in PFMS."
  - "The AI-IoT convergence is a strategic evolution towards adaptive and autonomous financial services."
  - "Zero-trust architecture and explainable AI are essential for building user trust."
```
---

## Paper 15: Mesino-Romero et al_summarized.md

**Source File:** `Mesino-Romero et al_summarized.md`

```yaml
paper_id: "b7c9a2e1-4f5d-4b8a-9c3e-7d6f1a2b3c4d"
designation: "local"
title: "FROM SURGE TO STABILITY: DIGITAL PAYMENTS DRIVING A STEADY TRANSITION"
authors: "Mesina-Romero, B.; Masangkay, M.; Franco, M.; Yambao, M.; Delgado, K.; Bueno, P.; Lingat, P.; Natividad, G.; Lapus, A.; Manuel, R.; Yñigo, K."
year: 2024
venue: "Bangko Sentral ng Pilipinas"
odin_topics:
  - "2.A"
  - "4.A"
  - "4.B"
  - "9.A"
  - "9.B"
  - "10.A"
  - "10.B"
  - "12.A"
tldr: "Digital retail payments in the Philippines reached 57.4% of volume and 59.0% of value in 2024, driven by merchant, P2P, and B2B transactions, with government disbursements nearly fully digitalized."
problem_and_motivation: "The Philippines aims to increase digital payment adoption to enhance financial inclusion and economic efficiency. Despite progress, barriers such as high fees and limited consumer trust persist. This report tracks the current state and identifies areas for further digitalization."
approach:
  - "Used a measurement model with 24 payment use-cases across government, business, and person categories."
  - "Estimated digital share using quantitative data from banks, government agencies, and surveys, supplemented by assumptions."
  - "Analyzed volume and value of digital payments monthly."
  - "Identified top use-cases and growth rates."
  - "Assessed policy initiatives and regulatory frameworks."
findings:
  - "num: Digital payments account for 57.4% of total monthly retail payment volume and 59.0% in value."
  - "num: Merchant payments represent 66.4% of digital volume, P2P transfers 20.6%, and B2B supplier payments 6.2%."
  - "num: Merchant payments grew 29.1% year-on-year, P2P transfers 34.7%, and B2B 28.1%."
  - "num: Government disbursements are 97.2% digital, while person-to-government collections are only 24.6% digital."
  - "num: InstaPay transaction volume rose 67.8% from 2023 to 2024."
  - "Digital payments exceeded the Philippine Development Plan target of 52–54%."
key_figures_tables:
  - "Figure 1: Digital payments share by volume over time (2013–2024) → grew from 10% in 2013 to 57.4% in 2024."
  - "Figure 2: Digital payments share by value over time (2018–2024) → increased from 26.8% to 59.0%."
  - "Table 1: Monthly volume per use-case → P2X dominates at 70.5%, B2X at 28.5%, G2X at 0.9%."
  - "Table 2: Digitalization rates per use-case → G2X 97.2%, P2X 72.2%, B2X 19.8% by volume."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "BSP"
    definition: "Bangko Sentral ng Pilipinas (Philippine central bank)"
  - term: "P2X"
    definition: "Person-to-anyone payments (from individuals)"
  - term: "B2X"
    definition: "Business-to-anyone payments"
  - term: "G2X"
    definition: "Government-to-anyone payments"
  - term: "PESONet"
    definition: "Philippine Electronic Funds Transfer System (batch, high-value)"
  - term: "InstaPay"
    definition: "Real-time electronic fund transfer system"
  - term: "QR Ph"
    definition: "National QR code standard for interoperable payments"
  - term: "PPMI"
    definition: "Philippine Payments Management, Inc."
  - term: "AFCS"
    definition: "Automated Fare Collection System"
  - term: "CBDC"
    definition: "Central Bank Digital Currency"
  - term: "RTGS"
    definition: "Real Time Gross Settlement"
critical_citations:
  - "[Better Than Cash Alliance, 2019] — Provided baseline measurement model."
  - "[BSP Circular No. 1195, 2024] — Consumer redress for EFTs."
  - "[BSP Circular No. 1198, 2024] — Regulatory framework for merchant acquiring."
relevance:
  topics:
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "high"
      justification: "Discusses remittances and P2P transfers, which are culturally significant in the Philippines."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "high"
      justification: "Describes InstaPay, PESONet, QR Ph, and other national payment infrastructures."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Highlights barriers like high fees, low P2G digitalization, and need for consumer protection."
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "medium"
      justification: "Mentions e-wallets and mobile banking but does not detail UX design principles."
    - code: "9.B"
      name: "Mobile UX Design for Personal Finance"
      relevance: "medium"
      justification: "References QR code and mobile app usage but lacks specific UX analysis."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "Introduces consumer redress and security regulations (Circulars 1195 and 1198)."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "high"
      justification: "Emphasizes trust and confidence as key to digital payment adoption."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "contextual"
      justification: "Provides a measurement model for national payment adoption, not specifically for personal finance systems."
  contribution: "This report provides empirical benchmarks for digital payment adoption in the Philippines, which inform Odin's expense categorization by highlighting dominant transaction types. Its identification of gaps in P2G digitalization suggests areas for user education and feature design. The consumer redress framework offers a model for Odin's trust and security modules. The measurement methodology can be adapted to evaluate Odin's system performance. The focus on merchant and P2P payments aligns with typical user spending patterns in Odin."
  directly_justifies:
    - "Digital payments in the Philippines reached 57.4% of retail volume in 2024."
    - "Merchant payments are the largest digital use-case, accounting for 66.4% of volume."
    - "P2G digital collection is only 24.6%, indicating a significant gap."
    - "Consumer redress regulations are critical for building user trust in digital finance."
  limits:
    - "Does not address individual spending behaviors or forecasting."
    - "Provides aggregate data but no segmentation by demographic such as young professionals."
    - "Lacks analysis of user experience or behavioral drivers."
    - "The measurement model relies on assumptions that may not capture all informal transactions."
  mapping_rationale: "A systematic scan across all 12 functional domains was performed. The domains flagged as relevant include: Filipino Cultural Context (topic 2.A, high), Existing Systems & Gaps (4.A high, 4.B high), Mobile-First Design (9.A medium, 9.B medium), Data Privacy & User Trust (10.A high, 10.B high), and System Evaluation (12.A contextual). Borderline cases: the report touches on seasonal spending (2.B) and cyclical patterns (2.D) but only implicitly; these were rejected because the data is aggregate and does not specify seasonal variations. Expense Categorization (3.A–C) was rejected as the report does not discuss category design. Behavioral Profiling (5.A–C), Spending Forecasting (6.A–B), Budget Recommendation (7.A–D), Anomaly Detection (8.A–C), User Retention (11.A–B), and Savings & Debt Management (13.A–C) were rejected because the paper does not address these algorithmic or user-centric topics. Overall, the paper is highly relevant for informing Odin's understanding of the national payment landscape, gaps, and trust considerations, but less so for individual-level financial management features."
limitations:
  - "Assumptions in estimation may introduce bias and uncertainty in the reported shares."
  - "Data sources may not cover all transactions, particularly informal or cash-based ones."
  - "The model does not capture user-level adoption drivers or behavioral factors."
  - "The report focuses on aggregate trends and does not provide granular insights for specific user segments."
remember_this:
  - "Digital payments reached 57.4% volume and 59.0% value in 2024."
  - "Merchant, P2P, and B2B payments drive 93.2% of digital volume."
  - "Government disbursements are 97.2% digital, but collections lag at 24.6%."
  - "Consumer redress and merchant acquiring regulations are key for trust."
  - "The BSP aims to make digital payments affordable to increase adoption."
```
---

## Paper 16: Somera_summarized.md

**Source File:** `Somera_summarized.md`

```yaml
paper_id: 10.69569/jip.2024.0257
designation: local
title: "I deserve this": A Phenomenological Study Toward Online Impulse Buying Behavior of Service Contractors
authors: Somera, K.
year: 2024
venue: Journal of Interdisciplinary Perspectives
odin_topics:
  - 2.A
  - 2.B
  - 2.C
  - 5.A
  - 5.C
  - 9.B
  - 11.A
  - 11.B
tldr: Filipino service contractors engage in online impulse buying as a coping mechanism for stress, driven by hedonic motivations and a sense of entitlement rooted in perceived self-worth and hard work.
problem_and_motivation: Online impulse buying among Filipino service contractors is an emerging phenomenon with significant psychological and financial implications, yet limited research exists on this specific demographic. Understanding their motivations, particularly the perception of "I deserve this," is crucial for comprehending the drivers and consequences of this behavior. The study addresses a gap in the literature by exploring the lived experiences of this group.
approach:
  - A qualitative phenomenological research design using Interpretative Phenomenological Analysis was employed.
  - Ten service contractors from Aurora, Philippines, were purposively selected based on high scores on Rook and Fisher's Impulse Buying Scale.
  - Data was collected through semi-structured online interviews and analyzed using thematic analysis to identify recurring patterns and themes.
  - Reflexivity and member-checking were used to establish rigor and validity.
findings:
  - num: Seven out of ten participants engaged in impulse buying before the pandemic, but their behavior intensified during it.
  - Impulse buying serves as a coping mechanism for stress, sadness, and loneliness, offering temporary emotional relief and mood regulation.
  - Motivations include a desire for immediate gratification, a sense of achievement, and healing the 'inner child' by fulfilling past unmet desires.
  - Negative impacts include significant financial stress, feelings of guilt, and regret following impulsive purchases.
  - The phrase "I deserve this" is used to justify purchases as a reward for hard work and to enhance self-concept and identity.
key_figures_tables:
  - Table 1: Themes and sub-themes on lived experiences → Six themes emerged covering emergence, motivations, impacts, extent, and coping strategies.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Impulse Buying
    definition: An unplanned, sudden, and strong desire to buy goods or services, characterized by an imbalanced emotional state and diminished cognitive evaluation.
  - term: Service Contractors
    definition: Employees engaged under a contract of service, often with job insecurity and financial challenges.
  - term: Interpretative Phenomenological Analysis (IPA)
    definition: A qualitative research method aimed at exploring and interpreting the lived experiences of individuals.
  - term: Hedonic Motivation
    definition: The drive to engage in behavior for pleasure, enjoyment, and emotional satisfaction rather than for practical or utilitarian reasons.
critical_citations:
  - "[Rook and Fisher, 1995] — Provides the Impulse Buying Scale used for participant selection."
  - "[Alase, 2017] — Outlines the steps for IPA data coding and analysis used in the study."
  - "[Minor et al., 2017] — Supports the link between impulse buying and self-concept/identity."
relevance:
  topics:
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Directly examines a Filipino-specific financial behavior (online impulse buying) among a unique local demographic (service contractors).
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: medium
      justification: While not seasonal in the traditional sense, the study highlights cyclical spending tied to emotional states, stress, and salary cycles.
    - code: 2.C
      name: User-Declared Financial Preferences
      relevance: medium
      justification: Participants articulate personal justifications ("I deserve this") and preferences for spending, revealing underlying value systems and priorities.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: The study profiles the impulse buying behavior of a specific user segment, identifying key emotional and psychological drivers and consequences.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: The study uses a scale to identify individuals with high impulse buying tendencies, offering a potential classification method for behavioral profiling.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: low
      justification: The study mentions the convenience of mobile apps like Shopee and Lazada in facilitating impulse buying, relevant for designing interventions.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Impulse buying is shown to be a form of emotional engagement, providing insights into user motivations that could inform retention strategies for PFMS.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: low
      justification: Understanding the emotional triggers for impulse buying can help design PFMS features that engage users in healthier financial behaviors.
  contribution: The paper provides a deep, qualitative understanding of the emotional drivers and cognitive justifications behind online impulse buying among Filipino service contractors. This directly informs Odin's behavioral profiling module (5.A) by identifying key psychological states and triggers. The findings on stress, mood regulation, and self-concept can be used to design features that promote healthier financial behaviors and detect potential financial distress. The study's insights into user motivations and justifications for spending are crucial for developing effective budget recommendation and anomaly detection systems that account for user psychology.
  directly_justifies:
    - The paper establishes that impulse buying is a coping mechanism for stress and negative emotions.
    - Participants use the phrase "I deserve this" to justify unplanned purchases as a reward.
    - Impulse buying leads to significant financial stress and feelings of guilt and regret.
    - Self-control and mindful spending are key strategies used to counter impulse buying behavior.
    - The convenience of online platforms like Shopee and Lazada facilitates and intensifies impulse buying.
  limits:
    - The study is limited to a small sample (n=10) of service contractors from a single province in the Philippines.
    - Findings are based on self-reported data, which may be subject to recall and social desirability biases.
    - The study focuses on lived experiences and does not establish causal relationships or predictive models.
    - Generalizability to other Filipino demographics or regions may be limited.
  mapping_rationale: The systematic scan across all 12 functional domains flagged three primary areas of relevance: Behavioral Profiling & Classification, Filipino Cultural Context, and User Retention & Engagement. From Behavioral Profiling, codes 5.A (Financial Behavioral Profiles) and 5.C (Classification Approaches) were selected as high relevance, as the paper directly profiles and classifies impulse buying behavior. The Filipino Cultural Context domain was relevant through codes 2.A (Culturally Specific Financial Practices) and 2.B (Seasonal and Cyclical Spending Patterns), with high and medium relevance respectively, because the study focuses on a Filipino population and highlights spending tied to emotional and salary cycles. Code 2.C (User-Declared Financial Preferences) was selected as medium relevance due to the explicit justifications users provide for their spending. The paper also touches on Mobile-First Design (9.B) and Retention & Engagement (11.A, 11.B) with low to medium relevance, as it discusses the role of online platforms and emotional engagement. Domains like Expense Categorization, Spending Forecasting, Budget Recommendation, Anomaly Detection, and Data Privacy were considered and rejected because the paper does not address these computational or systemic areas. The paper offers significant qualitative insights for understanding user psychology, which is foundational for designing user-centric PFMS features like behavioral profiling, anomaly detection baselines, and engagement strategies.
limitations:
  - Small sample size (n=10) limits generalizability. [unacknowledged]
  - Reliance on self-reporting may introduce biases. [unacknowledged]
  - The study does not establish causal relationships between emotional states and impulse buying.
  - The research is geographically confined to Aurora province.
remember_this:
  - Impulse buying serves as a primary coping mechanism for stress among Filipino service contractors.
  - Financial stress and guilt are significant negative consequences of online impulse buying.
  - The phrase "I deserve this" justifies unplanned purchases as rewards for hard work.
  - Seven out of ten participants reported intensified impulse buying during the pandemic.
  - Self-control and mindful spending are key strategies to mitigate impulse buying behavior.
```
---

## Paper 17: Sandstrom_summarized.md

**Source File:** `Sandstrom_summarized.md`

```yaml
paper_id: 10.15662/IJEETR.2024.0602004
designation: international-algorithm-specific
title: AI-Driven Risk-Adaptive Cloud Intelligence for Large-Scale Fraud Detection
authors: Sandström, F. T.
year: 2024
venue: International Journal of Engineering & Extended Technologies Research
odin_topics:
  - 4.A
  - 4.B
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 12.B
tldr: Integrates Grey Relational Analysis with Apache Spark and Hadoop to create a scalable, interpretable fraud detection system for multi-tenant cloud environments.
problem_and_motivation: Traditional fraud detection systems struggle with the scale, heterogeneity, and evolving patterns of data in multi-tenant cloud environments. Supervised methods require extensive labeled data and lack interpretability, while existing unsupervised methods often fail to integrate multiple weak signals. There is a need for a scalable, interpretable, and adaptive system that can operate under uncertainty.
approach:
  - Implements RACIS with layers for data ingestion, preprocessing, GRA scoring, and tenant-aware alerting.
  - Uses Apache Kafka for streaming and Hadoop for batch ETL, storing data in a centralized data lake.
  - Extracts features from transactional, behavioral, and system-level metrics to create a risk profile.
  - Applies Grey Relational Analysis to compute a fraud risk score by comparing each transaction to a legitimate reference profile.
  - Supports per-tenant configuration of feature weights, distinguishing coefficients, and risk thresholds.
findings:
  - "num: The system achieved a fraud detection recall of 93-95%."
  - "num: The precision ranged from 62-70%, with a false positive rate of 0.4-1.2%."
  - "num: The system processed approximately 1 x 10^9 transactions per hour with an average streaming latency of ~1.2 seconds."
  - The GRA-based scoring is highly interpretable, allowing analysts to identify which features contribute most to a high-risk score.
  - Performance varied across tenants, with more homogeneous transaction patterns yielding higher precision.
  - False positives primarily arose from legitimate but atypical behavior, such as large purchases or travel.
key_figures_tables:
  - "Table 1: Overall detection performance → Aggregated recall 93-95%, precision 62-70%, FPR 0.4-1.2%."
key_equations:
  - equation: '\gamma(x_0(j), x_k(j)) = \frac{\min_i \min_j |x_0(j) - x_i(j)| + \xi \max_i \max_j |x_0(j) - x_i(j)|}{|x_0(j) - x_k(j)| + \xi \max_i \max_j |x_0(j) - x_i(j)|}'
    explanation: Computes Grey Relational Coefficient for each feature.
  - equation: '\Gamma(X_0, X_k) = \sum_{j=1}^{n} w(j) \gamma(x_0(j), x_k(j))'
    explanation: Computes overall Grey Relational Grade (risk score).
definitions:
  - term: GRA
    definition: Grey Relational Analysis, a method to compare multiple criteria under uncertainty.
  - term: GRG
    definition: Grey Relational Grade, a composite similarity score relative to an ideal reference.
  - term: RACIS
    definition: Risk-Adapted Cloud Intelligence System, the proposed fraud detection framework.
critical_citations:
  - "[Carcillo et al., 2017] — Foundational for scalable fraud detection using Apache Spark."
  - "[Udayakumar et al., 2023] — Comparison point for ML-based fraud detection."
  - "[Oleti, 2023] — Relevant for credit risk assessment using AI."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Paper reviews big-data fraud detection systems as a broader landscape.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Explicitly identifies limitations of supervised ML and unsupervised methods for fraud detection.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: contextual
      justification: Discusses predictive risk assessment but focuses on detection, not forecasting.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: The GRA method is used for scoring, not sequential forecasting.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly proposes a system for detecting fraudulent anomalies in transaction data.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Evaluates GRA as an anomaly detection algorithm for transactional data.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Provides a detailed experimental evaluation of the GRA-based detection module.
  contribution: The paper justifies Odin's need for a scalable and interpretable anomaly detection module by demonstrating GRA's effectiveness in a multi-tenant context. It provides a concrete example of using grey relational analysis to score transactions, which can inform the design of Odin's spending anomaly detection. The system's tenant-aware configuration highlights the importance of user-specific thresholds, a key consideration for Odin. Furthermore, the discussion of limitations, such as high false positives, directly informs the need for hybrid approaches in Odin's design.
  directly_justifies:
    - "GRA can produce interpretable risk scores without requiring labeled data."
    - "Scalable distributed processing is essential for handling large-scale transaction data."
    - "Per-tenant configuration is necessary to adapt to diverse user profiles."
  limits:
    - "The system's high false positive rate may lead to alert fatigue and requires downstream filtering."
    - "GRA's static reference profiles may become outdated as user behavior evolves."
    - "The system cannot detect relational fraud patterns like collusion. [unacknowledged]"
  mapping_rationale: A systematic scan across all 12 functional domains identified the paper's primary relevance to 'Existing Systems & Gaps' (4.A, 4.B) and 'Anomaly Detection' (8.A, 8.B). The paper's problem statement directly critiques the limitations of current systems, justifying topic 4.B as high relevance. Its core contribution is a novel anomaly detection algorithm, establishing high relevance for 8.A and 8.B. Topic 6.A (Predictive Modeling) was considered but deemed contextual as the paper focuses on detection, not forecasting. Topic 12.B (Evaluation) was assigned medium relevance due to its detailed performance analysis. Topics related to Filipino cultural context, user retention, and savings were rejected as the paper is a general technical work with no specific focus on these areas. Overall, the paper provides strong justification for Odin's anomaly detection module's design requirements, emphasizing the need for a scalable, interpretable, and tenant-aware approach.
limitations:
  - "The evaluation uses synthetic data, which may not fully represent real-world complexity."
  - "The prototype relies on static reference profiles that require manual updating."
  - "The choice of features and their normalization heavily influences detection performance."
  - "Integrating external reputation feeds at scale may introduce latency or storage overhead."
  - "The high absolute number of false positives may overwhelm human analysts. [unacknowledged]"
remember_this:
  - "GRA achieved 93-95% recall for fraud detection in a multi-tenant system."
  - "Scalable architecture processed 10^9 transactions per hour with low latency."
  - "Precision was lower at 62-70%, indicating a need for downstream filtering."
  - "Interpretable scoring allows analysts to understand risk factors for each transaction."
```
---

## Paper 18: Gentyala_summarized.md

**Source File:** `Gentyala_summarized.md`

```yaml
paper_id: "10.63282/3117-5481/AIJCST-V6I5P105"
designation: "international-algorithm-specific"
title: "Breaking or Reinforcing the Cycle? Longitudinal Impacts of Bias-Correction Techniques on Feedback Loops and Sustained Financial Inclusion in Machine Learning Credit Scoring"
authors: "Gentyala, R."
year: 2024
venue: "American International Journal of Computer Science and Technology"
odin_topics:
  - "4.A"
  - "4.B"
  - "5.A"
  - "5.C"
  - "12.A"
  - "12.B"
tldr: "Bias-correction techniques in credit scoring can produce short-term fairness gains but often widen disparities over time due to performative feedback, whereas feedback-aware resampling sustains inclusion with minimal default increases."
problem_and_motivation: "Static fairness interventions in credit scoring ignore how model decisions reshape borrower behavior and data distributions, risking long-term reinforcement of disparities. Existing research lacks longitudinal empirical validation of bias-correction techniques under feedback dynamics."
approach:
  - "Used 1.2 million U.S. loan applications (2018–2024) plus synthetic emerging-market data augmented via CTGANs, totaling 2.3 million records."
  - "Simulated 8–12 lending cycles with performative distribution shifts and feedback loops (sampling, feature, outcome, model) per Perdomo et al. and Pagan et al."
  - "Evaluated adversarial debiasing, pre-processing reweighting, post-processing threshold adjustment, and loop-disrupting resampling."
  - "Base classifier was XGBoost; fairness metrics included demographic parity, equalized odds, AUC-ROC, Brier score, and credit-building index."
  - "Conducted 50 Monte Carlo runs with economic shock scenarios and sensitivity analyses on performative sensitivity ε."
findings:
  - "num: Simple threshold adjustments increased initial approvals for Black/Hispanic applicants by 12–15% but by later cycles widened disparities by 22% due to feedback."
  - "num: Dynamic resampling aligned with feedback-aware modeling sustained an 18% equity uplift with less than 3% rise in default rates."
  - "num: Baseline model saw Black approval parity erode from 0.77 to 0.57 over ten cycles."
  - "Adversarial training maintained Black approval parity between 0.87 and 0.93 across all cycles."
  - "Loop-disrupting resampling achieved average parity of 0.94 for Black applicants and preserved 94% of inclusion gains during economic shocks."
key_figures_tables:
  - "Figure 1: Closed-loop block diagram of feedback loops in credit-scoring pipeline → illustrates how decisions propagate and reshape future data."
  - "Figure 2: Iterative loan decision-making and debiasing framework with feedback loops → visualizes the simulation architecture and feedback pathways."
  - "Figure 3: Line plots of demographic parity across cycles for four interventions → shows threshold adjustments' fragile gains versus resampling's stability."
  - "Figure 4: Heatmap of loop contributions to disparity change → identifies sampling and model loops as dominant amplifiers, neutralized by resampling."
  - "Table I: Aggregated metrics over final five cycles with confidence intervals → quantifies parity, AUC-ROC, default delta, and credit-building index for each method."
key_equations:
  - equation: "PR(θ) = E_{Z ∼ D(θ)} [ℓ(Z; θ)]"
    explanation: "Performative risk: expected loss under model-induced distribution."
  - equation: "D_{t+1} = D_t + ε · f(θ_t, decision)"
    explanation: "Update rule for feature distribution after each decision cycle."
definitions:
  - term: "Performative prediction"
    definition: "Framework where model deployment alters the target distribution it predicts."
  - term: "Sampling feedback loop"
    definition: "Decisions affect which individuals appear in future training data."
  - term: "Feature feedback loop"
    definition: "Decisions modify observable borrower features like credit scores."
  - term: "Outcome feedback loop"
    definition: "Loan terms causally influence realized default probabilities."
  - term: "Model feedback loop"
    definition: "Retraining occurs only on observed approved cases, excluding rejected applicants."
  - term: "Demographic parity"
    definition: "Ratio of approval rates across protected groups; equal treatment metric."
critical_citations:
  - "[Perdomo et al., 2020] — Foundation for performative prediction and stability conditions."
  - "[Pagan et al., 2023] — Taxonomy of feedback loops in automated decision systems."
relevance:
  topics:
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews performative prediction and feedback loops as part of algorithmic fairness landscape."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Identifies gaps in static fairness approaches and calls for longitudinal evaluation."
    - code: "5.A"
      name: "Financial Behavioral Profiles of Filipino Young Professionals"
      relevance: "medium"
      justification: "Models borrower behavior changes due to decisions, relevant to behavioral profiling."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "Uses XGBoost and debiasing techniques that classify risk, relevant to profile classification."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Proposes longitudinal evaluation metrics for fairness and stability over cycles."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Empirically evaluates debiasing algorithms under feedback dynamics with rigorous metrics."
  contribution: "This paper provides a longitudinal evaluation framework that can inform Odin's system evaluation module by demonstrating the importance of multi-cycle testing for fairness and stability. Its feedback-aware resampling strategy offers a concrete technique for mitigating bias in user-facing algorithmic modules, such as spending forecasts or anomaly detection. The study's emphasis on performative effects underscores the need for Odin to model user behavior changes over time rather than treating data as static. Additionally, the taxonomy of feedback loops can guide Odin's design to anticipate and counteract potential bias amplification in its recommendation and alert systems."
  directly_justifies:
    - "Odin should adopt longitudinal evaluation metrics beyond static fairness audits to ensure sustained performance."
    - "Feedback-aware resampling can improve equity in Odin's algorithmic modules without disproportionate risk increases."
    - "Model retraining must account for performative shifts in user data to avoid reinforcing disparities."
  limits:
    - "Synthetic emerging-market data may not fully capture real-world cultural and economic nuances."
    - "Behavioral responses are simplified and may underestimate adversarial user strategies."
    - "The study focuses on credit scoring, not spending management, so direct transferability to PFMS is limited."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes identified relevance primarily in System Evaluation and Existing Systems & Gaps, with secondary relevance to Behavioral Profiling. The paper's longitudinal evaluation of debiasing techniques directly supports topics 12.A and 12.B (evaluation frameworks and algorithmic module evaluation) with high relevance, and topic 4.B (limitations and gaps) with high relevance because it explicitly critiques static fairness methods. Topics 4.A (landscape) and 5.A/5.C (behavioral profiles and classification) received medium relevance as they provide background and methodological context. Domains related to Filipino cultural context, expense categorization, budgeting, anomaly detection, mobile design, privacy, retention, and savings/debt management were considered but rejected as the paper does not address spending categorization, budget optimization, anomaly detection in spending, or other PFMS-specific functionalities. The overall relevance to Odin is moderate to high, as the insights on feedback loops and longitudinal evaluation can inform robust system design."
limitations:
  - "The simulation simplifies real human behavior, potentially missing strategic borrower responses."
  - "Synthetic data, though validated, may not capture all cultural and economic nuances of emerging markets."
  - "Anonymization precludes analysis of intersectional dynamics beyond primary protected attributes."
  - "The focus on U.S. consortia data may not generalize to markets with different credit infrastructures."
  - "Live deployment and long-term field studies are needed to confirm the findings in practice."
remember_this:
  - "Static fairness interventions can widen disparities over time due to feedback loops."
  - "Loop-disrupting resampling sustained 18% equity uplift with <3% default increase."
  - "Adversarial debiasing maintained approval parity above 0.87 across 10 cycles."
  - "Longitudinal evaluation is essential to avoid temporary fairness masking long-term harm."
  - "Feedback-aware design can preserve inclusion gains even during economic downturns."
```
---

## Paper 19: Yildiz & Demir_summarized.md

**Source File:** `Yildiz & Demir_summarized.md`

```yaml
paper_id: 2cdb3a8a-4339-50a3-9ed6-e64ca56661f4
designation: international-algorithm-specific
title: The Impact of Artificial Intelligence on Financial Inclusion: Data-Driven Approaches for Expanding Access to Banking in Underserved Regions
authors: Yıldız, E.; Demir, Z.
year: 2024
venue: CLASSICALLIBRARY
odin_topics:
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 9.A
  - 10.A
  - 12.A
tldr: AI enhances financial inclusion through alternative credit scoring, automated onboarding, conversational interfaces, predictive analytics, and personalized education, reducing costs and expanding access.
problem_and_motivation: Financial exclusion affects 1.4 billion adults due to high costs, information asymmetries, and infrastructure gaps. Traditional banking models struggle to serve low-income and remote populations profitably. AI technologies offer potential solutions to these persistent barriers.
approach:
  - The paper proposes a novel framework integrating machine learning, alternative data, and distributed ledger technologies.
  - Methodology combines computational approaches with empirical data from 47 developing economies.
  - A mathematical optimization model for AI deployment across heterogeneous markets is developed.
  - The model incorporates cost, adoption, and impact functions with Bayesian parameter estimation.
  - Clustering and mixed-integer programming are used for computational tractability.
  - Fairness constraints ensure minimum allocation proportionality across demographic dimensions.
  - Empirical analysis covers 14-17 markets for alternative credit scoring, onboarding, conversational interfaces, and predictive analytics.
  - Implementation case studies from East Africa, Southeast Asia, South Asia, West Africa, and Latin America are examined.
findings:
  - num: AI-enhanced credit scoring can increase approval rates for the previously unbanked by 37.8% while maintaining acceptable risk levels.
  - num: AI-powered mobile banking platforms can reduce operational costs by 42.3%.
  - num: Alternative credit scoring systems increase approval rates for unbanked applicants by 27-46% with maintained risk performance.
  - num: AI-enhanced digital onboarding reduces verification costs by 67-89% and processing time from days to minutes.
  - num: Voice-based financial interfaces increase active usage rates by 34-57% among previously excluded demographics.
  - num: Predictive analytics improve cash management efficiency by 23-41% and reduce service disruptions by 47-68%.
  - num: Adaptive learning systems increase financial knowledge retention by 28-53% and improve subsequent financial behavior by 17-39%.
  - Algorithmic bias risks emerged in several implementations, penalizing characteristics associated with excluded populations.
  - Regulatory acceptance and data privacy considerations require careful attention to ensure equitable outcomes.
  - Phased deployment approaches consistently outperform comprehensive initial rollouts.
key_figures_tables:
  - None.
key_equations:
  - equation: \max_{\phi} \sum_{m \in M} \sum_{a_i \in \phi(m)} w_m \cdot I_i(x_m) \cdot \alpha_i(x_m)
    explanation: Maximizes inclusion impact across market segments and interventions.
  - equation: C_i(x_m) = c_i^{base} + c_i^{adapt} \cdot d(x_m, x_i^{ref}) + c_i^{scale} \cdot p_m \cdot (1 - e^{-\lambda_i p_m})
    explanation: Models implementation cost as baseline plus adaptation and scaling.
  - equation: \alpha_i(x_m) = \frac{1}{1 + e^{-\beta_i x_m}} \cdot (1 - e^{-\gamma_i t}) \cdot \prod_{j=1}^{q} \min(1, \frac{x_m^{r_j}}{x_i^{req,j}})
    explanation: Adoption combines market characteristics, diffusion, and infrastructure thresholds.
  - equation: I_i(x_m) = \sum_{k=1}^{h} w_k \cdot \Delta F_i^k(x_m)
    explanation: Impact is weighted sum of improvements in inclusion metrics.
definitions:
  - term: AI
    definition: Artificial intelligence; broad suite of computational techniques for pattern recognition, prediction, and optimization.
  - term: Financial inclusion
    definition: Access to and usage of formal financial services for economic development and poverty reduction.
  - term: Supervised learning
    definition: Algorithms that learn from labeled historical data to predict outcomes for new inputs.
  - term: Federated learning
    definition: Model training across distributed data sources without centralizing sensitive personal information.
  - term: Edge computing
    definition: Moving computational processes closer to data sources to reduce dependency on constant connectivity.
  - term: NLP
    definition: Natural language processing; technologies enabling interaction through natural language text or speech.
  - term: LSTM
    definition: Long Short-Term Memory; recurrent neural network variant capturing temporal dependencies in sequential data.
  - term: XGBoost
    definition: Extreme Gradient Boosting; supervised learning algorithm effective for imbalanced datasets.
  - term: PWA
    definition: Progressive Web Application; provides offline functionality for essential transactions.
critical_citations:
  - "[Caldecott et al., 2022] — Defines financial inclusion as critical economic enabler."
  - "[Lindemann et al., 2005] — Establishes AI capabilities for financial pattern recognition."
  - "[Sachs et al., 2019] — Documents six transformations for sustainable development goals."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: Provides framework for understanding financial behaviors of excluded populations.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Discusses classification methods for creditworthiness using alternative data.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Presents predictive models for credit scoring and service delivery optimization.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Uses LSTM and gradient boosting for forecasting financial behaviors.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Mentions anomaly detection for fraud prevention and security.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Implies use of machine learning for detecting irregular financial patterns.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Discusses mobile banking platforms and offline functionality for underserved regions.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Addresses data privacy, federated learning, and regulatory frameworks.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides empirical evaluation of AI applications across multiple markets.
  contribution: The paper provides empirical evidence that AI-enhanced financial services can expand access to banking in underserved regions, supporting Odin's design for inclusive personal finance management. It validates the use of alternative data sources and machine learning for credit scoring, which informs Odin's financial behavioral profiling and classification modules. The optimization framework for resource allocation across heterogeneous markets directly justifies Odin's approach to constrained budget recommendation. The discussion of phased deployment and hybrid architectures provides design principles for Odin's mobile-first and offline-capable system.
  directly_justifies:
    - AI-enhanced credit scoring can increase approval rates for previously unbanked by 37.8%.
    - AI-powered mobile banking platforms can reduce operational costs by 42.3%.
    - Voice-based interfaces increase active usage by 34-57% among excluded demographics.
    - Phased deployment approaches consistently outperform comprehensive initial rollouts.
  limits:
    - Data quality and availability vary substantially across regions, with rural populations generating sparser digital footprints.
    - Algorithmic bias risks emerged in several implementations, penalizing characteristics associated with excluded populations.
    - Regulatory frameworks in many markets initially restricted remote onboarding procedures.
    - Development costs and content creation requirements represent significant implementation barriers.
  mapping_rationale: The systematic scan across all 12 functional domains and associated topic codes identified relevance primarily in predictive modeling, behavioral classification, and data privacy domains. High relevance was assigned to 6.A, 6.B, and 10.A based on the paper's core contributions on forecasting algorithms and privacy frameworks. Medium relevance was assigned to 5.C, 8.A, 8.B, 9.A, and 12.A for supporting evidence on classification approaches, anomaly detection, mobile design, and evaluation. Contextual relevance was assigned to 5.A for foundational behavioral framing. Domains 1.A, 1.B, 1.C, 2.A, 2.B, 2.C, 2.D, 3.A, 3.B, 3.C, 4.A, 4.B, 7.A, 7.B, 7.C, 7.D, 8.C, 9.B, 10.B, 11.A, 11.B, 12.B, 12.C, 13.A, 13.B, and 13.C were considered and rejected as the paper does not address Filipino-specific contexts, expense categorization, user-defined constraints, existing PFMS systems, cold-start baselines, retention mechanisms, or savings/debt management. The paper's overall relevance to Odin is high, providing foundational evidence for AI-driven financial inclusion mechanisms applicable to the Filipino young professional demographic.
limitations:
  - The study draws primarily from developing economy data, limiting generalizability to specific Filipino contexts. [unacknowledged]
  - Long-term impacts on economic outcomes and vulnerability reduction are not examined. [unacknowledged]
  - The mathematical model is computationally intensive and may be difficult to implement in resource-constrained settings. [unacknowledged]
  - Regulatory frameworks and data privacy considerations require careful attention, a point the paper acknowledges.
remember_this:
  - AI credit scoring increases approval rates for unbanked by 37.8%.
  - AI mobile banking reduces operational costs by 42.3%.
  - Phased deployment outperforms comprehensive initial rollouts consistently.
  - Federated learning addresses critical privacy and data sovereignty concerns.
  - Hybrid architectures balance centralized and distributed processing effectively.
```
---

## Paper 20: Gomez et al_summarized.md

**Source File:** `Gomez et al_summarized.md`

```yaml
paper_id: "d9b7e3c4-8f6a-4d2e-b1c3-9f8e7d6c5b4a"
designation: "local-algorithm-specific"
title: "Modeling Personality Traits by Predicting Questionnaire Responses as an Alternative Approach to Filipino Automatic Personality Recognition"
authors: "Gomez, A. P. I.; Kahil, I. D.; Ong, S. V. N.; Tighe, E. P."
year: 2024
venue: "Unknown"
odin_topics:
  - "5.C"
  - "5.B"
  - "12.B"
  - "1.A"
  - "2.A"
tldr: "Predicting BFI item responses from Filipino Twitter text and aggregating to estimate trait scores achieved low accuracy, with hierarchical classification slightly improving Conscientiousness but not Extraversion."
problem_and_motivation: "Direct automatic personality recognition from Filipino social media text yields poor results due to cultural linguistic nuances and data scarcity. An alternative item-based prediction approach may better account for these intricacies, but its effectiveness remains unproven."
approach:
  - "Used the PagkataoKo dataset of 2,168 Filipino Twitter users with BFI responses."
  - "Preprocessed tweets with tokenization (Pinoy TweetTokenizer) and extracted n-grams."
  - "Applied TF-IDF and term occurrence with min_df/max_df filtering, then chi-square or PCA for feature reduction."
  - "Trained logistic regression, SVM, and XGBoost classifiers per BFI item in a direct and a two-phase hierarchical scheme."
  - "Aggregated item predictions to estimate Extraversion and Conscientiousness trait scores and evaluated with RMSE and R2."
findings:
  - "num: Best item-level test F1 reached 0.4334 for Extraversion and 0.5416 for Conscientiousness."
  - "All item models underperformed majority class baselines, indicating poor classification accuracy."
  - "Hierarchical classification improved item-level broad classification for Conscientiousness but not Extraversion."
  - "num: Trait-level R2 for Extraversion was 0.1240, and for Conscientiousness was -0.2273 with the original pipeline."
  - "Data imbalance and overfitting were evident, as validation F1 scores were near 1.0 while test scores were low."
key_figures_tables:
  - "Table 2: Best Extraversion item models achieved test F1 0.3196–0.4334, favoring term occurrence → performance is modest and inconsistent."
  - "Table 3: Best Conscientiousness item models varied widely, test F1 0.2426–0.5416 → some items show better classification but others perform poorly."
  - "Table 4: Proposed approach for Extraversion had test RMSE 0.6714 and R2 0.1240 → slightly better than baselines but still weak."
  - "Table 5: Proposed approach for Conscientiousness had test RMSE 0.6760 and negative R2 -0.2273 → worse than linear regression baseline."
  - "Figure 2: Comparison of Extraversion item models vs majority class baselines → all item models underperform baselines."
  - "Figure 3: Comparison of Conscientiousness item models vs baselines → item models underperform baselines."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "BFI"
    definition: "Big Five Inventory, a personality questionnaire measuring five traits."
  - term: "APR"
    definition: "Automatic Personality Recognition, inferring personality from digital data."
  - term: "TF-IDF"
    definition: "Term Frequency-Inverse Document Frequency, a text feature weighting method."
  - term: "SVM"
    definition: "Support Vector Machine, a supervised learning algorithm."
  - term: "XGBoost"
    definition: "Extreme Gradient Boosting, an ensemble tree-based algorithm."
  - term: "PCA"
    definition: "Principal Component Analysis, a dimensionality reduction technique."
critical_citations:
  - "[Tighe and Cheng, 2018] — Found Extraversion and Conscientiousness easiest to model."
  - "[Tighe et al., 2022] — Curated the PagkataoKo dataset used in this study."
  - "[Mushtaq and Kumar, 2022] — Overview of text-based APR developments."
relevance:
  topics:
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "This paper evaluates classification models (LR, SVM, XGBoost) for personality trait prediction, which directly parallels financial behavioral profile classification."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "medium"
      justification: "Discusses data scarcity and cold-start challenges in modeling Filipino user profiles, relevant to profile initialization in PFMS."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Provides a detailed evaluation framework (F1, RMSE, R2) for item-level and trait-level prediction models, applicable to PFMS module evaluation."
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "contextual"
      justification: "Uses Filipino social media users, primarily young adults (mean age 21), providing demographic context but not specific to professionals."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "low"
      justification: "Mentions Filipino linguistic nuances and multilingualism but does not address financial practices, only personality recognition."
  contribution: "This paper contributes a methodological framework for item-based personality prediction that can be adapted to financial behavior profiling in Odin. Its evaluation of classification models on sparse Filipino text data informs the design of behavioral profile classifiers. The hierarchical classification scheme offers a way to handle ordinal response data, which could be applied to user preference or constraint tiers. The identified challenges of data imbalance and overfitting provide cautionary insights for Odin's cold-start and profile dynamics modules."
  directly_justifies:
    - "Machine learning classifiers can be trained on Filipino social media text to predict user responses."
    - "Hierarchical classification can improve accuracy for ordinal data by grouping similar classes first."
    - "Data imbalance severely degrades model performance, requiring careful class weighting or oversampling."
    - "Feature selection and reduction are critical for managing high-dimensional text data."
  limits:
    - "The paper focuses on personality, not financial behavior, so direct transferability is limited."
    - "Performance metrics are low, suggesting the approach is not yet viable for production use."
    - "Only two of five Big Five traits were tested; applicability to other traits is unknown."
  mapping_rationale: "A systematic scan of all 12 functional domains was performed. Domains related to expense categorization (3), existing systems (4), forecasting (6), budgeting (7), anomaly detection (8), mobile design (9), privacy (10), retention (11), and savings/debt (13) were rejected as the paper does not address financial topics. The behavioral profiling domain (5) was flagged as highly relevant, specifically 5.C (classification approaches) because the paper compares multiple classifiers for predicting user attributes from text, and 5.B (profile dynamics) for its discussion of cold-start and data scarcity. The system evaluation domain (12.B) was considered medium relevance because the paper includes a thorough evaluation of algorithmic modules (item-level and trait-level). Filipino cultural context domains (1.A, 2.A) were considered contextual/low due to the use of Filipino data and mention of linguistic nuances, but the content is not financial. Overall, the paper's relevance to Odin lies in its methodological contributions to behavioral profile classification and evaluation, albeit in a non-financial domain."
limitations:
  - "The study only used Twitter data; generalizability to other social media or text sources is untested. [unacknowledged]"
  - "Only Extraversion and Conscientiousness were modeled; other Big Five traits were not explored."
  - "The best models still performed worse than simple baselines, indicating limited practical utility."
  - "Data imbalance was not addressed with resampling or cost-sensitive learning."
  - "The hierarchical classification improved broad-level but not fine-grained accuracy."
remember_this:
  - "Predicting BFI item responses from text and aggregating yields low accuracy for personality traits."
  - "Hierarchical classification improved Conscientiousness item-level broad classification but not Extraversion."
  - "All item models underperformed majority class baselines, indicating severe data imbalance issues."
  - "Trait-level R2 scores were near zero or negative, showing the approach poorly explains variance."
  - "Data imbalance and overfitting were major challenges, requiring better balancing strategies."
```
---

## Paper 21: Samuel_summarized.md

**Source File:** `Samuel_summarized.md`

```yaml
paper_id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
designation: international-algorithm-specific
title: Behavioral Biometrics and Machine Learning for Enhanced Fraud Detection in Financial Services
authors: Samuel, O. J.
year: 2024
venue: Stem Cell, Artificial Intelligence and Data Science Journal
odin_topics:
  - 8.A
  - 8.B
  - 8.C
  - 9.B
  - 10.A
  - 10.B
tldr: Behavioral biometrics combined with machine learning provides dynamic, privacy-preserving fraud detection through continuous user authentication and anomaly detection in financial services.
problem_and_motivation: Traditional fraud detection relies on static rules and transaction analysis, which are insufficient against adaptive fraud. Behavioral biometrics offers a continuous authentication layer, but requires robust integration with ML and privacy safeguards.
approach:
  - Behavioral data (keystroke, mouse, touch, device sensors) is acquired from web and mobile platforms.
  - Preprocessing includes noise removal, normalization, imputation, and feature engineering (temporal, statistical, frequency-domain).
  - Deep learning models like LSTM, CNN, and Transformers are used to model sequential behavioral patterns.
  - Training strategies include supervised, semi-supervised, and transfer learning to handle data imbalance and evolving fraud.
  - Evaluation uses precision, recall, F1-score, AUC-ROC, and MCC, with continuous monitoring for behavioral drift.
findings:
  - num: Multimodal ML combining behavioral and transactional features can reduce false positives by up to 40%.
  - num: Integration of keystroke dynamics with transaction monitoring improved detection of account takeovers by 35%.
  - num: Touchscreen gestures combined with contextual device data reduced false positives in mobile payment fraud.
  - Deep learning models (LSTM, Transformers) effectively model temporal dependencies and sequential behavior for real-time fraud detection.
  - Federated learning and differential privacy enable cross-institutional model training without exposing raw behavioral data.
  - Explainable AI (XAI) techniques like SHAP are vital for interpreting complex models and ensuring regulatory compliance.
  - Unsupervised methods (autoencoders, Isolation Forests) detect zero-day fraud but require human validation to reduce false positives.
  - Adaptive and context-aware modeling is essential to mitigate behavioral drift and maintain model reliability.
key_figures_tables:
  - "None."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: Behavioral Biometrics
    definition: Analysis of dynamic user interaction patterns like keystroke dynamics, mouse movements, and touchscreen gestures.
  - term: LSTM
    definition: Long Short-Term Memory networks capture long-term dependencies in sequential data.
  - term: CNN
    definition: Convolutional Neural Networks extract spatial patterns in feature representations.
  - term: XAI
    definition: Explainable AI provides interpretability for complex model decisions.
  - term: Federated Learning
    definition: Model training on decentralized data without sharing raw data.
critical_citations:
  - "[Ahmed, Mahmood, & Hu, 2016] — Foundational survey on network anomaly detection."
  - "[Chandola, Banerjee, & Kumar, 2009] — Comprehensive review of anomaly detection methods."
  - "[Fatunmbi, Piastri, & Adrah, 2022] — Demonstrates deep learning for multimodal data fusion in fraud."
  - "[Ozdemir & Fatunmbi, 2024] — Discusses XAI for interpretability in AI-driven systems."
  - "[Sommer & Paxson, 2010] — Critical analysis of ML limitations in intrusion detection."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly addresses anomaly detection using behavioral biometrics and ML for fraud.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Evaluates LSTM, CNN, Transformers, and unsupervised methods for anomaly detection.
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: medium
      justification: Discusses adaptive modeling and transfer learning to handle new users or domains.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Touchscreen gesture and device sensor data collection informs mobile UX design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Emphasizes federated learning, differential privacy, and data anonymization.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: high
      justification: Addresses explainability (XAI) and ethical deployment to build user trust.
  contribution: |
    This paper provides a comprehensive framework for deploying behavioral biometrics with machine learning, which can directly inform Odin's anomaly detection module by integrating continuous user authentication. The emphasis on privacy-preserving techniques such as federated learning and differential privacy is directly applicable to Odin's data privacy and user trust requirements. The discussion on multimodal data fusion (e.g., combining keystroke dynamics with transaction data) can guide Odin's expense categorization and behavioral profiling modules. Furthermore, the deployment strategies and evaluation metrics outlined offer a blueprint for Odin's system evaluation and algorithmic module testing.
  directly_justifies:
    - "Behavioral biometrics can be integrated with ML to provide continuous, unobtrusive user authentication."
    - "Multimodal fusion of behavioral and transactional data reduces false positives in anomaly detection."
    - "Explainable AI (XAI) techniques are essential for building user trust and regulatory compliance."
    - "Federated learning enables model training across distributed datasets without exposing sensitive user data."
    - "Adaptive and context-aware modeling is necessary to mitigate behavioral drift and maintain reliability."
  limits:
    - "The paper does not provide empirical results specific to personal finance management systems."
    - "Implementation challenges and scalability for high-volume, low-latency systems are discussed but not fully addressed."
    - "Cross-institutional collaboration for secure data sharing is proposed but lacks concrete implementation details."
  mapping_rationale: |
    A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant to Anomaly Detection (Domain 8) due to its core focus on behavioral biometrics and ML for fraud detection, which directly maps to topics 8.A, 8.B, and 8.C with high relevance. Mobile-First Design (Domain 9) was considered relevant through topic 9.B (Mobile UX Design) because the paper discusses mobile touchscreen gestures and device sensor data, though relevance is medium as it does not specifically address UX design principles. Data Privacy & User Trust (Domain 10) was identified as highly relevant, with topics 10.A and 10.B receiving high relevance due to extensive discussions on federated learning, differential privacy, data anonymization, and explainable AI. Topics related to Behavioral Profiling (Domain 5) were considered but rejected because the paper focuses on fraud detection rather than financial behavior profiling for budgeting or savings. Similarly, Expense Categorization (Domain 3) and Budget Recommendation (Domain 7) were not addressed. Overall, the paper provides strong justification for Odin's anomaly detection framework, particularly in privacy-preserving and interpretable ML deployment.
limitations:
  - "The paper does not explicitly evaluate its proposed methods on personal finance datasets, which limits direct generalizability to Odin's user base."
  - "Behavioral variability due to context, device, and emotional state is acknowledged but not comprehensively addressed in model design."
  - "Adversarial attacks and mimicry are mentioned but no specific defense mechanisms are detailed [unacknowledged]."
  - "Scalability and latency requirements for real-time financial transaction processing are discussed only at a high level."
remember_this:
  - "Multimodal ML can reduce false positives by up to 40% in fraud detection."
  - "Federated learning preserves privacy while enabling collaborative model training."
  - "Explainable AI is critical for regulatory compliance and user trust."
  - "Behavioral biometrics offers continuous, unobtrusive user authentication."
  - "Adaptive modeling is essential to counter behavioral drift and evolving fraud patterns."
```
---

## Paper 22: Yadav et al_summarized.md

**Source File:** `Yadav et al_summarized.md`

```yaml
paper_id: 4b5a7d6e-8f9c-4a1b-9d3e-8f2a5c1e7d4b
designation: international-algorithm-specific
title: AI Wealth Navigator: An Integrated Platform for Smart Budgeting, Financial Learning, and Personalized Policy Guidance
authors: Yadav, A.; Prakash, R. S.; Iqubal, S. M.; Gebremicahea, M. G.
year: 2024
venue: Unknown
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 6.A
  - 7.A
  - 7.B
  - 8.A
  - 9.A
  - 9.B
  - 10.A
  - 11.A
  - 12.A
tldr: Integrates AI-driven budgeting, adaptive financial learning, and policy recommendations into a unified platform for personal finance management.
problem_and_motivation: Users face fragmented financial ecosystems where budgeting, education, and policy knowledge are disjointed. Low financial literacy in India exacerbates poor decision-making on savings, investments, and government benefits. A unified, intelligent platform is needed to bridge these gaps and promote financial inclusion.
approach:
  - System uses Next.js frontend with Supabase and Prisma for data management.
  - Inngest handles automated tasks and notifications for background processes.
  - Gemini LLM powers personalized financial recommendations and adaptive learning.
  - Policy recommendation engine uses hybrid data APIs to suggest government schemes.
  - Arcjet ensures secure data handling and transaction encryption.
  - Evaluation involved human assessment by 50 users and system performance metrics.
findings:
  - num: Receipt scanner achieved 94% accuracy on digital and physical receipts.
  - num: Average user ratings were 4.8/5 for budgeting insights, 4.7/5 for policy, and 4.6/5 for learning.
  - num: Over 70% of users discovered previously unknown government programs.
  - Arcjet blocked all simulated security threats during testing.
  - Integration of three domains into one platform eliminated the need for multiple apps.
key_figures_tables:
  - Figure 1.1: System layered architecture showing frontend, backend, AI, and security components → Modular design separates core functions for scalability.
  - Figure 1.2: Detailed architecture diagram with data flow between modules → Highlights integration of LLM, APIs, and user interface.
  - Figure 1.3: Sequence diagram of user interactions → Illustrates real-time data flow and response generation.
  - Figure 1.4: Dashboard interface → Shows visual spending analytics and budget tracking tools.
  - Figure 1.5: Transaction page with receipt scanner → Demonstrates OCR-based expense entry.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: LLM
    definition: Large Language Model used for generating personalized financial insights.
  - term: OCR
    definition: Optical Character Recognition used for scanning and digitizing receipts.
  - term: API
    definition: Application Programming Interface for data exchange between system components.
critical_citations:
  - "[Patel et al., 2023] — AI platforms improve financial literacy with personalized paths."
  - "[Kumar et al., 2023] — Dynamic budgeting systems enhance user engagement."
  - "[Lee et al., 2023] — AI suggests social benefits based on financial profiles."
  - "[Gupta et al., 2024] — AI secures transactions and detects fraud."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Provides AI-driven budget tracker with receipt scanning for automated categorization.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: Discusses receipt scanner accuracy and structured transaction logs.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: high
      justification: Explicitly surveys fragmented existing systems and proposes a unified alternative.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies gaps in integration, literacy, and policy access in current apps.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: low
      justification: Mentions predictive financial planning as future work, not implemented.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: medium
      justification: Offers personalized savings alerts and dynamic recommendations based on spending habits.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: Gemini LLM provides tailored budgeting insights and investment advice.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Security evaluation mentions fraud detection but not as a primary focus.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: Frontend uses responsive design for mobile and desktop, with dark/light mode.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Interface includes visual dashboards and interactive tools, but mobile-specific UX not detailed.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Arcjet ensures encryption, secure data handling, and threat prevention.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: User ratings (4.7–4.8/5) indicate trust in relevance and empathy of recommendations.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Gamified learning modules and real-time insights support sustained user engagement.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      relevance: medium
      justification: Adaptive roadmap and policy alerts keep users returning for new recommendations.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Uses both quantitative performance metrics (response time, token efficiency) and human evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Evaluates receipt scanner accuracy and LLM response quality.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: contextual
      justification: Human ratings provide qualitative assessment but no benchmark comparison.
  contribution: "The paper directly supports Odin's Budget Recommendation module (7.B) by demonstrating a unified AI platform that integrates Gemini LLM for personalized budgeting insights and real-time spending analytics. For Expense Categorization (3.A/3.B), the receipt scanner with 94% accuracy provides a benchmark for automated transaction logging. The system's modular architecture and security measures (Arcjet) inform Odin's Mobile-First Design (9.A/9.B) and Data Privacy (10.A) considerations. Additionally, the evaluation framework using both system metrics and user ratings (4.8/5) offers a template for Odin's System Evaluation (12.A)."
  directly_justifies:
    - "AI-driven platforms can close financial literacy gaps and empower low-income communities."
    - "LLM-based systems provide context-aware, personalized financial recommendations."
    - "Integrating budgeting, education, and policy into one ecosystem improves user experience."
    - "Automated receipt scanning reduces manual entry errors and increases adoption."
    - "Multi-layer security is essential for protecting personal financial data."
  limits:
    - "Study conducted with only 50 Indian users, may not generalize to Filipino context."
    - "No longitudinal data on behavior change or retention over time."
    - "Dependence on full user profiles for policy matching may raise privacy concerns [unacknowledged]."
    - "Sporadic OCR errors mentioned as a drawback but not quantified in detail."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains of Expense Categorization, Existing Systems & Gaps, Budget Recommendation, Data Privacy, and System Evaluation were flagged as highly relevant, as the paper directly addresses these with algorithmic contributions and evaluation metrics. Behavioral Profiling (5.A) and Forecasting (6.A/6.B) were considered but rejected due to only cursory mentions (forecasting as future work, no behavioral classification). Anomaly Detection (8.A) was marked contextual because security evaluation touched on fraud prevention but without algorithmic detail. Mobile-First Design (9.A/9.B) was medium relevance due to the mention of responsive design but lack of in-depth UX analysis. Filipino-specific topics (2.A-2.D) were rejected entirely as the study is based in India and does not address Filipino cultural contexts. Overall, the paper is highly relevant for its integrated AI architecture, but its international algorithm-specific focus limits direct applicability to Odin's Philippine-centric design."
limitations:
  - "Limited user sample (n=50) and geographic scope (India)."
  - "No comparison against existing baseline systems or benchmarks."
  - "Relies on proprietary Gemini LLM, limiting reproducibility."
  - "Policy recommendation engine not evaluated for correctness or coverage."
  - "Long-term user retention and behavior change not assessed. [unacknowledged]"
remember_this:
  - "Unified platform combines budgeting, learning, and policy into one system."
  - "Receipt scanner achieves 94% accuracy on diverse receipt types."
  - "User ratings averaged 4.8/5 for budgeting insights and 4.7/5 for policy."
  - "Arcjet provides API-layer threat prevention and data encryption."
  - "Over 70% of users discovered new government programs through the engine."
```
---

## Paper 23: Yin_summarized.md

**Source File:** `Yin_summarized.md`

```yaml
paper_id: 10.1037/xge0001541
designation: international
title: The Impact of Categorization on Consumption Behavior
authors: Yin, S.
year: 2024
venue: Journal of Experimental Psychology: General
odin_topics:
  - "3.A"
  - "3.B"
  - "4.A"
  - "7.D"
  - "13.A"
tldr: Used accounts reduce perceived resource value via within-account comparison, increasing spending likelihood versus unused accounts with equal absolute balances.
problem_and_motivation: Consumers often spend from accounts with prior use, yet it is unclear how the used versus unused status of an account affects subsequent spending decisions independently of absolute balance. This gap matters because understanding this psychological mechanism can inform the design of financial tools and nudge consumer behavior.
approach:
  - Seven experimental studies (N = 8,667) across gift cards, checking accounts, and credit card reward points.
  - Used account conditions manipulated relative to unused accounts, holding absolute remaining resources constant.
  - Within-account comparison theory tested against alternative explanations (e.g., external reference points).
  - Continuous manipulation of remaining proportion (60%, 40%, 20%) to test moderation.
  - Mediation analysis via bootstrap (10,000 samples) to test valuation as the mechanism.
  - Incentive-compatible behavioral experiments for online shopping and donation decisions.
findings:
  - num: Used accounts increased spending likelihood by 15.82 points on a 0-100 scale versus unused accounts without a reference point (Study 1).
  - num: Valuation of resources mediated the effect of account status on spending (indirect effect: -0.91, 95% CI [-1.96, -0.025]).
  - num: The proportion remaining moderates the effect; spending increased as the relative amount decreased in used accounts (b = -7.99, p < .001).
  - Used account effect holds for both endowed (gift cards, reward points) and earned resources (checking accounts).
  - Unspecified checking accounts are perceived as used, leading to similar spending likelihood as specified used accounts.
  - The effect generalizes from spending to donation decisions (charitable giving).
key_figures_tables:
  - "Figure 1: Likelihood of spending $5 on a drink across used vs. unused gift cards → Used accounts increase spending."
  - "Figure 2A: Spending likelihood from used, unused, and unspecified checking accounts → Unspecified mimics used."
  - "Figure 3A: Spending likelihood of 30,000 reward points → Used accounts increase points spending versus cash."
  - "Figure 4: Moderation by proportion remaining (60%, 40%, 20%) → Steeper spending increase in used accounts."
  - "Table S1 (Appendix): Summary of results across seven studies → Consistent main effect and mediation."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Used account
    definition: An account from which some resources have already been spent.
  - term: Unused account
    definition: An account from which no resources have been spent.
  - term: Within-account comparison
    definition: Comparing current remaining resources to the original amount in the same account.
  - term: Psychological value
    definition: Perception of importance, worth, or usefulness of a resource.
critical_citations:
  - "[Heath & Soll, 1996] — Mental accounting and earmarking effects."
  - "[Arkes et al., 1994] — Windfall gains are spent more readily."
  - "[Hsee, 1996] — Relative versus absolute judgments."
  - "[Cheema & Soman, 2008] — Partitioning resources reduces consumption."
  - "[Morewedge et al., 2007] — Context influences perceived magnitude."
relevance:
  topics:
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "high"
      justification: "Directly examines how account categorization (used vs. unused) influences spending behavior."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      relevance: "high"
      justification: "Provides evidence that category framing (used vs. unused) affects resource valuation and spending."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Informative for understanding how PFMS account presentation could influence user behavior."
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "low"
      justification: "Tangentially relevant via spending likelihood based on account status."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "contextual"
      justification: "Mentions savings goals in Essay 3; but paper primarily focuses on spending, not goal management."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "contextual"
      justification: "Not directly studied; contextual for understanding broad spending patterns."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "contextual"
      justification: "Behavioral tendency (spending from used accounts) could inform profiles but not directly studied."
  contribution: "This paper provides a direct causal mechanism—within-account comparison—that can inform Odin's expense categorization module (3.A) by demonstrating that presenting an account as 'used' versus 'unused' changes spending propensity. For budget recommendation (7.B), the finding that users may undervalue resources in used accounts suggests that Odin should consider account history when recommending spending adjustments. For user onboarding (5.B), the cold-start problem may be mitigated by framing new accounts as 'unused' to encourage more conservative spending until a user's behavior is learned. The moderation by proportion remaining (3.B) offers a concrete design lever: displaying remaining balance relative to the original amount can nudge spending behavior. These insights directly apply to Odin's goal of helping Filipino young professionals manage finances, especially in culturally relevant contexts where gift cards and reward points are common."
  directly_justifies:
    - "Used accounts decrease perceived resource value compared to unused accounts with equal balances."
    - "The proportion of resources remaining in an account moderates the spending effect; lower proportions increase spending."
    - "Unspecified checking accounts are naturally perceived as used, affecting spending decisions."
    - "Valuation mediates the effect of account status on spending likelihood."
  limits:
    - "Studies conducted primarily with U.S. participants; may not generalize to Filipino cultural context."
    - "Focuses on spending, not on savings or debt management directly."
    - "The effect may be attenuated in high-involvement or large-ticket decisions not tested."
  mapping_rationale: "All 12 functional domains and their associated topic codes were systematically scanned. The paper directly addresses Expense Categorization (3.A, 3.B) via its core manipulation of used vs. unused accounts and their impact on spending and valuation. It also informs Existing Systems (4.A) by demonstrating a behavioral bias that PFMS should account for. The third essay touches on Savings Goal Management (13.A), but the primary contribution is on spending, so this is marked contextual. The moderation by remaining proportion (3.B) is a key design insight. Domains like Anomaly Detection (8.A-C), Forecasting (6.A-B), and Mobile Design (9.A-B) were considered but rejected because the paper does not address algorithms, prediction, or interface design. Filipino-specific topics (1.A-C, 2.A-D) were rejected as the sample is U.S.-based, though the behavioral principle may be culturally transferable. Overall, the paper offers strong, directly actionable evidence for how account presentation influences user spending, making it highly relevant for Odin's expense categorization and budget recommendation modules."
limitations:
  - "The effect may not replicate outside the U.S. where gift card and reward point usage patterns differ. [unacknowledged]"
  - "The research does not examine long-term effects on savings or overall financial health. [unacknowledged]"
  - "Incentive-compatible studies were limited to online shopping; field studies are lacking. [unacknowledged]"
  - "The mechanism is measured via self-report; behavioral data on valuation is not directly observed."
  - "Potential demand effects in experimental scenarios may influence reported spending likelihood."
remember_this:
  - "Used accounts reduce perceived value and increase spending by up to 15.8 points."
  - "Account history framing is a powerful nudge in PFMS design."
  - "Unspecified accounts are automatically treated as used by default."
  - "Valuation mediates the link between account status and spending."
  - "Relative balance (e.g., 20% vs. 60% left) moderates the spending effect."
```
---

## Paper 24: Pittman_summarized.md

**Source File:** `Pittman_summarized.md`

```yaml
paper_id: 10.48550/arXiv.2412.19241
designation: international-algorithm-specific
title: Latenrgy: Model Agnostic Latency and Energy Consumption Prediction for Binary Classifiers
authors: Pittman, J. M.
year: 2024
venue: Unknown
odin_topics:
  - 6.B
  - 7.D
  - 8.B
  - 9.A
  - 10.A
  - 12.B
tldr: A model-agnostic theoretical framework and predictive equations for latency and energy consumption during inference in binary classification models with RAI guardrails.
problem_and_motivation: The scalability and sustainability of ML systems are constrained by compute overhead during inference, yet no generalized predictive techniques exist for latency and energy consumption across classifiers. The literature lacks cross-comparison of algorithms and has unquantified impacts of RAI guardrails on inference performance.
approach:
  - The study employed Theory Construction Methodology to derive a model-agnostic equation.
  - Core variables were identified from prior empirical findings and theoretical reasoning.
  - Variables are organized into three sets: classification algorithm type, RAI guardrails, and dataset characteristics.
  - Relationships among variables, such as the inverse correlation between latency and energy, were proposed.
  - Two prediction equations were formalized for latency (with logarithmic scaling for dataset size) and energy consumption (with linear scaling).
findings:
  - The framework synthesizes algorithm characteristics, dataset properties, and computational overhead of RAI guardrails into a unified analytical tool.
  - The approach offers generalizability and scalability across diverse classifiers like SVM, k-NN, Random Forest, and Neural Networks.
  - The work establishes a theoretical foundation for balancing computational efficiency with ethical robustness in ML systems.
key_figures_tables:
  - Table 1: Foundational variables in a model-agnostic equation → Lists variable sets and symbols for A, G, D, and O.
  - Table 2: Coefficients for model-agnostic prediction equations → Details coefficients for baseline, error, algorithm type, dataset size, feature dimensionality, data type, and guardrails.
key_equations:
  - equation: O = f(A, D, G)
    explanation: General equation unifying latency and energy dimensions.
  - equation: L = α + β_A A + β_D log(n) + γ_D p + δ_D t + ∑ φ_{G,i} g_i + ε
    explanation: Latency prediction equation with logarithmic scaling for dataset size.
  - equation: E = α' + β'_A A + β'_D n + γ'_D p + δ'_D t + ∑ φ'_{G,i} g_i + ε'
    explanation: Energy consumption equation with linear scaling for dataset size.
definitions:
  - term: Responsible AI (RAI)
    definition: A framework of principles ensuring AI technologies are ethical, fair, and trustworthy.
  - term: Guardrails
    definition: Measures implemented in deployed models to assess runtime behavior and ensure responsible operation.
  - term: Latency
    definition: The time required to produce a prediction during inference.
  - term: Energy Consumption
    definition: The power expended to perform inference operations.
critical_citations:
  - "[Henderson et al., 2020] — Highlights inference overhead in resource-constrained environments."
  - "[Mallik et al., 2023] — Identifies lack of generalized predictive techniques for latency and energy."
  - "[Mattson et al., 2020] — MLPerf benchmark for standardized performance evaluation."
  - "[Li et al., 2024] — Computational costs of RAI guardrails are underexplored."
relevance:
  topics:
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: Provides a model-agnostic framework that could be adapted for spending forecasting.
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: low
      justification: General trade-off modeling may inform handling of infeasible budget constraints.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Framing of inference performance is relevant to real-time anomaly detection modules.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: low
      justification: Addresses resource-constrained deployment, relevant to mobile-first PFMS design.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Mentions RAI guardrails including privacy but does not address PFMS-specific privacy.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: low
      justification: Theoretical framework could contribute to evaluating algorithmic efficiency in PFMS.
  contribution: The paper provides a theoretical foundation for predicting inference performance, which could inform the design of efficient algorithmic modules in Odin. Its model-agnostic approach is relevant for evaluating and optimizing modules like spending forecasting or anomaly detection. The integration of RAI guardrails, including privacy, aligns with Odin's data privacy concerns. The work enables informed trade-offs between computational efficiency and ethical robustness, applicable to mobile-first system design.
  directly_justifies:
    - "A model-agnostic framework is necessary for predicting latency and energy consumption across diverse classifiers."
    - "Computational overhead of RAI guardrails must be quantified during inference."
    - "Benchmarking studies must incorporate RAI considerations to remain relevant."
  limits:
    - "The predictive equations rely on assumptions about variable relationships that may not fully capture real-world complexities."
    - "The focus on binary classification excludes multi-class and other ML tasks."
    - "The representation of RAI guardrails simplifies potential computational impact."
    - "The framework abstracts dataset characteristics, excluding factors like data quality or sparsity."
    - "The study presents theoretical equations without empirical validation. [unacknowledged]"
  mapping_rationale: A systematic scan across all 12 functional domains and their associated topic codes was performed. Domains flagged as relevant include Spending Forecasting (6.A, 6.B), Anomaly Detection (8.A, 8.B, 8.C), Mobile-First Design (9.A, 9.B), Data Privacy & User Trust (10.A, 10.B), and System Evaluation (12.A, 12.B, 12.C). Topic 6.B (Forecasting Algorithms) was selected with low relevance because the paper provides a general predictive framework that could be adapted for spending forecasting but does not address sequential spending data. Topic 8.B (Anomaly Detection Algorithms) was selected with low relevance because the inference performance framing is applicable to real-time detection modules. Topic 9.A (Mobile-First Design Principles) was selected with low relevance due to the paper's emphasis on resource-constrained environments. Topic 10.A (Data Privacy and Security) was classified as contextual because it mentions RAI guardrails including privacy but does not address PFMS-specific privacy concerns. Topic 12.B (Evaluation of Algorithmic Modules) was selected with low relevance as the theoretical framework could contribute to evaluating algorithmic efficiency. Domains such as Filipino Cultural Context (2.A-D), Expense Categorization (3.A-C), Existing Systems (4.A-B), Behavioral Profiling (5.A-C), Budget Recommendation (7.A-D), User Retention (11.A-B), and Savings & Debt (13.A-C) were rejected as the paper does not address these PFMS-specific topics. The paper's overall relevance to Odin is low but contextual, as it provides a general technical foundation for evaluating and optimizing algorithmic modules and mobile deployment.
limitations:
  - "The prediction equations rely on assumptions about variable relationships that may not fully capture real-world complexities."
  - "The focus on binary classification excludes multi-class and other ML tasks."
  - "The representation of RAI guardrails simplifies potential computational impact."
  - "The framework abstracts dataset characteristics, excluding factors like data quality or sparsity."
  - "The study presents theoretical equations without empirical validation. [unacknowledged]"
remember_this:
  - "A model-agnostic theoretical framework for predicting inference latency and energy consumption is proposed."
  - "The framework integrates the computational cost of RAI guardrails into a predictive tool."
  - "Latency and energy equations use logarithmic and linear scaling for dataset size, respectively."
  - "The approach offers generalizability across SVM, k-NN, Random Forest, and Neural Networks."
  - "Empirical validation is needed to calibrate coefficients and ensure practical applicability."
```
---

## Paper 25: Pratama & Putri_summarized.md

**Source File:** `Pratama & Putri_summarized.md`

```yaml
paper_id: 10.47738/ijaim.v4i4.92
designation: international-algorithm-specific
title: User Profiling Based on Financial Transaction Patterns: A Clustering Approach for User Segmentation
authors: Pratama, S. F.; Putri, N. A.
year: 2024
venue: International Journal for Applied Information Management
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 12.B
tldr: Clustering financial transaction data by amount, time, and type reveals three user segments with distinct spending behaviors, supporting personalized financial services.
problem_and_motivation: Traditional user segmentation methods relying on historical data fail to capture evolving behaviors and the nuances of transaction patterns. This limits the effectiveness of personalized financial services and fraud detection. More advanced, data-driven techniques are needed to uncover hidden behavioral segments from transaction data.
approach:
  - Data from a Kaggle financial transactions dataset was preprocessed and features were extracted.
  - K-means clustering was applied using transaction amount, time, and type as key features.
  - Feature scaling and encoding were performed on numerical and categorical variables.
  - The Silhouette Score was used to evaluate cluster quality and the optimal number of clusters.
  - Clusters were visualized using 3D plots, PCA, and t-SNE projections for interpretation.
findings:
  - num: The clustering analysis revealed three distinct user clusters with a Silhouette Score of 0.33.
  - Cluster 0 performs moderate-value purchases (~1876.92) early in the week, around 11:15 AM.
  - Cluster 1 performs high-value transfers (~4147.06) mid-week, around 1:35 PM.
  - Cluster 2 performs moderate-value purchases (~1970.00) later in the week, around 11:20 AM.
  - The 3D, PCA, and t-SNE visualizations showed clear separation between the three clusters.
  - The moderate Silhouette Score indicates some overlap, suggesting room for improved clustering methodology.
  - The single-month dataset limits the generalizability of the findings to long-term trends.
key_figures_tables:
  - "Table 1: Cluster characteristics summary showing mean amount, hour, and day of week for each cluster → Three distinct behavioral segments identified."
  - "Figure 2: 3D clustering of users based on transaction patterns → Clusters are distinct in amount and time dimensions."
  - "Figure 3: Cluster distribution bar chart → Cluster 2 has the highest transaction volume, Cluster 0 the least."
  - "Figure 4: PCA projection of clustering results → Clusters show separation in reduced dimensional space."
  - "Figure 5: t-SNE projection of clustering results → Clusters demonstrate distinct groupings in a 2D space."
key_equations:
  - equation: d(x_i, C_j) = sqrt(sum_{k=1}^{n} (x_{i,k} - c_{j,k})^2)
    explanation: Euclidean distance used for K-means assignment.
  - equation: WCSS = sum_{i=1}^{K} sum_{x_i in C_k} (x_i, c_k)^2
    explanation: Objective function minimized by K-means.
definitions:
  - term: K-Means
    definition: A clustering algorithm that partitions data into K distinct clusters based on mean distances to centroids.
  - term: Silhouette Score
    definition: A metric evaluating cluster quality, ranging from -1 (poor) to 1 (excellent).
  - term: WCSS
    definition: Within-Cluster Sum of Squares, the objective function minimized in K-means.
  - term: PCA
    definition: Principal Component Analysis, a dimensionality reduction technique.
  - term: t-SNE
    definition: t-Distributed Stochastic Neighbor Embedding, a nonlinear dimensionality reduction technique.
critical_citations:
  - "[Zhao et al., 2021] — Proposes K-means for customer segmentation using transaction data."
  - "[Zhang et al., 2020] — Uses DBSCAN for fraud detection based on transaction patterns."
  - "[Komati, 2025] — Highlights the role of ML in real-time financial decision-making and segmentation."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly segments users into behavioral profiles based on transaction patterns.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: Discusses limitations of historical data, tangentially related to the cold-start issue.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Uses K-means clustering, a key classification approach for behavioral profiling.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Segmentation insights can inform predictive models for spending forecasting.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: low
      justification: Findings on spending patterns could inform budgeting strategies.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: User segmentation is a prerequisite for personalized budget recommendations.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Clustering can help establish baseline behaviors for anomaly detection.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Mentions fraud detection, but focuses on clustering, not anomaly detection specifically.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Evaluates the K-means clustering algorithm using the Silhouette Score.
  contribution: The paper provides a practical demonstration of K-means clustering for segmenting users based on financial transaction features, which directly supports the development of Odin's behavioral profiling module. Its findings on distinct spending patterns (e.g., high-value transfers vs. moderate purchases) offer a baseline for designing personalized budget recommendations and targeted financial advice. The identified limitations, such as the moderate Silhouette Score and single-month dataset, highlight areas for methodological improvement in Odin's clustering algorithms. This work justifies the use of unsupervised learning for initial user segmentation to overcome the cold-start problem in a PFMS.
  directly_justifies:
    - "Transaction amount, time, and type are key features for distinguishing user spending behavior."
    - "Clustering techniques like K-means can identify distinct user segments without predefined labels."
    - "A Silhouette Score of 0.33 indicates moderate cluster quality, suggesting a need for refinement."
    - "Limitations in clustering accuracy highlight the importance of exploring alternative algorithms like DBSCAN."
    - "Segmentation by transaction behavior enables the tailoring of personalized financial products and marketing."
  limits:
    - "The dataset's single-month duration limits the capture of seasonal or long-term behavior trends."
    - "The moderate Silhouette Score (0.33) suggests overlap between clusters and potential misclassification."
    - "The use of synthetic data from Kaggle may not fully represent real-world user behavior."
  mapping_rationale: "A systematic scan of all 12 functional domains and their topic codes was performed. The paper was flagged as highly relevant to 'Behavioral Profiling & Classification' (5.A, 5.C) due to its primary contribution of user segmentation via K-means. It shows medium relevance to 'Spending Forecasting' (6.A) and 'Budget Recommendation' (7.B) as segmentation is foundational for these tasks. Low relevance was assigned to 'Anomaly Detection' (8.A, 8.B) because clustering is discussed for segmentation, not for identifying outliers. The 'Evaluation' domain (12.B) is relevant as the study uses the Silhouette Score to assess its algorithmic module. Topics related to the Filipino cultural context, mobile design, data privacy, and debt management were considered and rejected, as the paper uses a generic international dataset and does not address these specific aspects. Overall, the paper is most valuable as a practical example of applying a specific clustering algorithm for user profiling, justifying its use in Odin's user onboarding and segmentation modules."
limitations:
  - "The dataset is limited to a single month, restricting the analysis of long-term trends and seasonality."
  - "The moderate Silhouette Score suggests cluster overlap and potential for improved separation."
  - "The study does not compare K-means with other clustering algorithms like DBSCAN or hierarchical clustering. [unacknowledged]"
  - "The use of synthetic data may limit the real-world applicability of the findings. [unacknowledged]"
remember_this:
  - "K-means clustering on transaction features reveals three distinct user spending segments."
  - "The Silhouette Score of 0.33 indicates moderate cluster quality, requiring methodological refinement."
  - "Transaction amount, time, and type are strong predictors of user behavior for segmentation."
  - "Segmentation by transaction patterns enables personalized financial services and marketing strategies."
```
---

## Paper 26: Pawar et al_summarized.md

**Source File:** `Pawar et al_summarized.md`

```yaml
paper_id: 10.59256/indjcst.20240302026
designation: international-algorithm-specific
title: ExpenseXpert: Transforming Financial Management with AI-Driven Predictive Analytics and Efficient Tracking
authors: Pawar, S.; Dhole, A.; Jaybhaye, D.; Gosawi, T.; Gaikwad, S.
year: 2024
venue: Indian Journal of Computer Science and Technology
odin_topics:
  - 3.A
  - 3.B
  - 6.A
  - 6.B
  - 7.B
  - 7.C
  - 8.A
  - 8.B
  - 9.B
  - 11.A
tldr: Presents a web application using ARIMA for personalized budget planning, LSTM for stock prediction, and a GPT-3.5 chatbot to enhance financial management for individuals.
problem_and_motivation: Individuals struggle with managing personal finances due to low financial literacy and a lack of personalized, automated budgeting tools. Existing systems fail to provide adaptive budget plans based on spending patterns or offer integrated financial advice.
approach:
  - Forecasts expenses using an ARIMA model, optimized with hyperparameter tuning and differencing to handle non-stationary daily expense data from 2020-2023.
  - Compares ARIMA against an LSTM model for expense forecasting, determining ARIMA is more suitable for small, short-term datasets.
  - Implements a financial chatbot leveraging the GPT-3.5 Turbo API within a Django framework to provide personalized financial assistance and advice.
  - Integrates the NewsAPI to provide users with real-time financial news and an "Investment Helper" using an LSTM model for stock price prediction.
  - Provides features for exporting expense summaries in PDF, CSV, and Excel formats and sends budget exceedance alerts.
findings:
  - The ARIMA model outperformed LSTM for forecasting expense categories, achieving a MAPE of 0.0756 for the personal care category.
  - The LSTM model for stock price prediction demonstrated notable success in accurately forecasting market trends.
  - The financial chatbot, using the GPT-3.5 API, provides more accurate and contextually relevant financial responses than existing solutions.
  - The application identifies a gap in traditional expense trackers for automated, personalized budget plan generation.
  - It offers enhanced usability through multi-format data downloads and a visually appealing interface with graphical data representations.
key_figures_tables:
  - Figure 1: LSTM model test vs predict data graph → Shows LSTM's attempt to capture patterns in expense data.
  - Figure 2: ARIMA model test vs predict data graph → Demonstrates ARIMA's fit and forecast on expense data.
  - Figure 3: ARIMA model forecast vs actual value graph → Displays the accuracy of ARIMA forecasts for personal care expenses.
  - Figure 4: LSTM model's predicted vs actual stock price graph → Illustrates the LSTM model's accuracy in forecasting price movements.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "ARIMA"
    definition: "Autoregressive Integrated Moving Average, a statistical model for time series forecasting that captures trends and seasonality."
  - term: "LSTM"
    definition: "Long Short-Term Memory, a recurrent neural network capable of learning long-term dependencies in sequential data."
  - term: "MLP"
    definition: "Multilayer Perceptron, a class of feedforward artificial neural network."
  - term: "MAPE"
    definition: "Mean Absolute Percentage Error, a metric for measuring the accuracy of a forecasting method."
  - term: "GPT-3.5"
    definition: "A state-of-the-art language model by OpenAI used for natural language processing tasks like the financial chatbot."
critical_citations:
  - "[Jiao, 2020] — Developed a finance chatbot using Rasa with better performance than RNN."
  - "[Hashemi et al., 2010] — Found MLPs outperform LSTMs for interday stock price prediction."
  - "[Lo & MacKinlay, 1988] — Proved historical data has strong predictive ability for stock prices."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: medium
      justification: Categorizes expenses into eight groups (education, food, etc.) for analysis and forecasting.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: Uses a defined set of categories for personalized budget planning, demonstrating a practical application.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly applies ARIMA and LSTM for forecasting user expenses to generate budget plans.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Compares ARIMA and LSTM on sequential daily expense data for short-term forecasting.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: The system generates custom budget plans based on user spending patterns using ARIMA forecasts.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: contextual
      justification: Generates budgets based on forecasted spending but does not explicitly discuss optimization under constraints.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: contextual
      justification: Mentions proactive notifications for budget exceedance as a form of financial discipline.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: Does not implement specific anomaly detection algorithms but uses threshold-based alerts.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: medium
      justification: Designed as a web application with a focus on user experience, clarity, and ease of use.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Features like chatbots, news, and graphical reports are designed to increase user motivation and engagement.
  contribution: The paper contributes a comparative analysis of ARIMA and LSTM for short-term expense forecasting, which is directly applicable to Odin's budget recommendation module. It provides empirical evidence for selecting ARIMA for small, short-term datasets. The findings on personalized budget plan generation can justify the approach for Odin's personalized financial management features.
  directly_justifies:
    - The ARIMA model effectively captures short-term trends and seasonality, making it suitable for forecasting a user's spending for the next period.
    - For small datasets, ARIMA outperforms LSTM for forecasting expenses, indicating a need for careful model selection.
    - Users benefit from automated budget plans based on their historical spending patterns rather than static allocations.
  limits:
    - The study uses a limited dataset (2020-2023) with eight broad categories, which may not reflect the granularity needed for a PFMS.
    - The forecast horizon is limited to 15 days, which may be too short for monthly budgeting.
    - The paper acknowledges that LSTMs require larger datasets, and its implementation was not successful, limiting its generalizability.
  mapping_rationale: The systematic scan across all 12 functional domains and associated topic codes flagged several as relevant. Domains on forecasting (6.A, 6.B) and budget recommendation (7.B) were identified as high relevance due to the paper's core contribution. Expense categorization (3.A, 3.B), user engagement (11.A), and mobile-first design (9.B) were marked medium, as the paper provides examples and rationales for these features. The domain of anomaly detection (8.A, 8.B) was considered but marked contextual/low, as the paper's alert system is a simple threshold, not a complex detection algorithm. Domains such as Filipino cultural context, behavioral profiling, and data privacy were considered and rejected as the study is not contextually specific to the Philippines and does not address these topics. The overall relevance is medium-high, providing algorithmic and design insights for predictive and budget recommendation modules in Odin.
limitations:
  - The ARIMA model's performance is evaluated on a limited dataset from a single institution.
  - The paper provides minimal detail on the LSTM model's architecture and hyperparameter tuning for the Investment Helper. [unacknowledged]
  - The study does not report user satisfaction or system usability metrics beyond accuracy. [unacknowledged]
  - It does not address data privacy or security concerns in the context of financial management. [unacknowledged]
remember_this:
  - ARIMA model achieved 7.56% MAPE for forecasting personal care expenses.
  - ARIMA is preferred over LSTM for short-term forecasting with small datasets.
  - Personalized budget plans are generated automatically from historical spending patterns.
  - GPT-3.5 API can be effectively used for a financial assistance chatbot.
  - ExpenseXpert provides multi-format downloads and proactive budget exceedance alerts.
```
---

## Paper 27: Bongalonta et al_summarized.md

**Source File:** `Bongalonta et al_summarized.md`

```yaml
paper_id: 10.11594/ijmaber.05.08.32
designation: local
title: The Traditional Way of Saving Money Versus the Modern Style of Investment: The Financial Management Styles of Sorsogon State University (Sorsu) Bulan Campus Faculty Members
authors: Bongalonta, M. B.; Bongalonta, M. M.; Gigantoca, S. E.
year: 2024
venue: International Journal of Multidisciplinary: Applied Business and Education Research
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 3.A
  - 4.A
  - 7.A
  - 7.B
  - 13.A
tldr: Faculty members adopt both traditional (budgeting, paluwagan, piggy banks) and modern (bank deposits, stock investments) saving methods, facing challenges from rising costs, low financial literacy, poor debt management, and low/delayed salaries.
problem_and_motivation: Faculty members at Sorsogon State University experience financial difficulties despite stable government salaries, often resorting to high-cost borrowing that undermines their savings capacity. A significant gap exists in understanding their specific financial management practices and the problems they face, which hinders the development of targeted interventions to improve their financial well-being. This study addresses this gap by identifying the saving and investment practices of these faculty members to formulate a relevant financial management model.
approach:
  - A mixed-methods design was used with a survey and focus group discussions (FGDs).
  - The study involved 40 faculty members from Sorsogon State University Bulan Campus.
  - Quantitative data gathered faculty profiles, while qualitative FGDs explored practices and problems.
  - Thematic analysis of FGD transcripts identified patterns in financial management behaviors.
  - The findings informed the development of the Bongalonta’s Financial Model.
findings:
  - Most faculty members (62.5%) earn between P40,001-P50,000 monthly, but 82.5% spend over P12,000, leaving limited room for savings.
  - num: 60% of faculty members save only 0-15% of their income.
  - Faculty members use both traditional (budgeting, paluwagan, piggy banks) and modern (bank deposits, stock investments) methods to save.
  - Primary problems in handling finances include increasing cost of utilities and unexpected expenses, lack of financial literacy, poor debt management, and low/delayed salaries.
  - The "paluwagan" system, while used for saving, often leads to debt and default issues among participants.
  - Financial literacy is low, with faculty members stating they have no background or ideas in financial management.
  - High debt from loans (e.g., GSIS, Land Bank) consumes a large portion of salaries, hindering savings.
  - Delayed salaries, especially for non-permanent faculty, disrupt the ability to save.
  - A proposed financial model was created to guide faculty in budgeting, minimizing debt, saving for emergencies, and investing in retirement.
key_figures_tables:
  - Chart 9: Saving models used by faculty → Shows piggy bank and paluwagan are the most common.
  - Chart 6: Percentage of savings → Shows 60% of faculty save only 0-15% of their income.
key_equations:
  - equation: Savings = Income - Expenses
    explanation: Faculty savings are the residual after all expenses.
definitions:
  - term: Paluwagan
    definition: A traditional Filipino informal savings and credit system where members contribute a fixed amount and take turns receiving the pooled funds.
  - term: Piggy Bank
    definition: A container used to hold and save small amounts of money.
  - term: Bongalonta’s Financial Model
    definition: A four-step model designed to enhance faculty savings through budgeting, debt minimization, emergency funds, and retirement investment.
critical_citations:
  - "[Gage et al., 2020] — Found faculty face significant financial insecurity."
  - "[Chinn et al., 2019] — Showed faculty lack basic financial knowledge."
  - "[Goldrick-Rab & Kendall, 2016] — Linked part-time faculty to higher debt."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: Focuses on faculty, a subset of Filipino professionals.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Provides detailed data on income, expenses, and savings of faculty.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly examines financial management practices and problems.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: Discusses budgeting and expense tracking practices.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Describes traditional and modern saving/investment methods.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Explores budgeting as a primary saving practice.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Proposes a model to enhance savings, implicitly recommending budget allocation.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: high
      justification: Directly deals with practices and problems in saving money.
  contribution: This paper provides empirical data on the financial behavior of a specific Filipino professional group (faculty), which can inform the design of Odin's financial profiling and budgeting modules. The findings on the prevalence of traditional methods like "paluwagan" highlight the need for culturally-aware expense categorization and savings features. The identified problems, such as low financial literacy and poor debt management, justify the inclusion of educational components and debt management tools in Odin. The study's mixed-methods approach offers a model for understanding user needs, which is crucial for developing Odin's user-defined allocation constraints and behavioral classification. Overall, the research underscores the importance of designing for real-world constraints like irregular income and high debt burden.
  directly_justifies:
    - "Faculty members adopt both traditional and modern saving methods, indicating a hybrid approach."
    - "High monthly expenses (82.5% spend >P12,000) limit the capacity for savings."
    - "Lack of financial literacy is a significant barrier to effective money management."
    - "Debt repayment consumes a large portion of salary, reducing savings potential."
    - "Paluwagan systems, while popular, can lead to financial problems due to defaults."
  limits:
    - "Study is limited to a single campus, restricting generalizability to other institutions."
    - "Data relies on self-reporting, which may be subject to social desirability bias."
    - "The study is descriptive and does not employ a statistical model to infer causality."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to 'Financial Structure of Filipino Young Professionals' (1.B) and 'Financial Behavior...' (1.C) due to its detailed survey of income, expenses, and saving practices. It also provided high relevance to 'Budgeting Strategies' (7.A) and 'Savings Goal Management' (13.A) as it discusses specific budgeting practices, saving models, and the problems hindering saving. Medium relevance was assigned to 'Landscape of Existing Systems' (4.A) as it describes traditional and modern methods, and 'Budget Recommendation' (7.B) due to the proposed financial model. Low and contextual relevance were assigned to other topics like 'Anomaly Detection' (8.A-C) as the paper does not address algorithmic detection, and 'Data Privacy' (10.A-B) as it is not a focus. Borderline cases like the 'paluwagan' system, which touches on culturally specific practices (2.A) and cyclical spending (2.D), were ultimately categorized under 1.C and 4.A for their behavioral and systemic insights, as the paper's core focus is on financial management. Domains such as 'Behavioral Profiling' (5.A-C), 'Forecasting' (6.A-B), and 'System Evaluation' (12.A-C) were rejected as the paper is purely descriptive and does not engage with algorithmic or predictive approaches. Overall, the paper provides foundational behavioral and financial structure data relevant to Odin's design.
limitations:
  - "The study focuses on a single campus, limiting generalizability to other Filipino professionals."
  - "The sample size of 40 is relatively small for quantitative analysis."
  - "The research is descriptive and does not test for statistical associations between variables."
  - "The reliance on self-reported data may be subject to social desirability and recall bias. [unacknowledged]"
  - "The proposed financial model is not empirically validated. [unacknowledged]"
remember_this:
  - "Faculty save only 0-15% of their income despite earning P40,000-P50,000 monthly."
  - "Traditional methods like piggy banks and paluwagan are as common as bank deposits."
  - "High expenses and debt service are the primary barriers to saving for faculty."
  - "Lack of financial literacy is a major impediment to effective financial management."
  - "Delayed salary releases severely disrupt the saving capacity of faculty."
```
---

## Paper 28: Yang T. et al_summarized.md

**Source File:** `Yang T. et al_summarized.md`

```yaml
paper_id: 10.60087/jklst.vol3.n3.p53-62
designation: international-algorithm-specific
title: Enhancing Financial Services Through Big Data and AI-Driven Customer Insights and Risk Analysis
authors: Yang, T.; Xin, Q.; Zhan, X.; Zhuang, S.; Li, H.
year: 2024
venue: Journal of Knowledge Learning and Science Technology
odin_topics:
  - 5.A
  - 5.C
  - 6.A
  - 8.A
  - 10.A
tldr: Integrates big data and AI, using supervised learning and XGBoost, for customer profiling, risk analysis, and profit prediction in financial services.
problem_and_motivation: Financial institutions lack accurate methods for customer identification and risk assessment using vast, complex data. Traditional models fail to capture non-linear relationships and profit dynamics, limiting effective risk management and loan approval.
approach:
  - Constructs six feature systems including customer attributes, debit/credit transactions, loan applications, trend characteristics, and page visit behavior.
  - Uses supervised learning for pricing models to combine human-machine decision-making and identify target customers.
  - Employs XGBoost for profit modeling, balancing detailed submodels for transparency against aggregated models for performance.
  - Uses grid search for hyperparameter tuning (tree depth, learning rate) with 5x cross-validation and early stopping for AUC.
  - Classifies banks and accounts into liquidity and finance charge types for portfolio-specific analysis.
findings:
  - num: Spender banks consist of wealthier, higher credit quality borrowers than weekly transition banks.
  - num: Model performance for revenue and total profit forecasting is poor, but ranking performance is better.
  - num: Profit quartile spread across risk ranges increases with risk level, indicating challenges in high-risk areas.
  - Profit-based modeling provides more information than risk-based modeling, especially in higher risk ranges.
  - The hump-shaped relationship between profit components and risk is retained between predicted and actual curves.
key_figures_tables:
  - Figure 1: Principle of machine learning face recognition technology → Different faces are composed of different features in feature space.
  - Figure 2: Experimental data and profit graph → Hump-shaped curve shows risk 'sweet spot' in turnover.
  - Table 1: Results of hyperparameter searches for XGBoost submodels.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: XGBoost
    definition: Extreme Gradient Boosting, a machine learning algorithm used for regression and classification.
  - term: AUC
    definition: Area Under the Curve, a performance metric for classification models.
critical_citations:
  - "[Thomas, 2000] — Foundation for automated underwriting systems."
  - "[Finlay, 2008; 2010] — Compares linear and ML approaches for financial behavior."
  - "[Fitzpatrick and Mues, 2021] — Extends algorithms for profitability prediction in P2P lending."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Profiles customers (e.g., spender, revolver) based on transaction behavior.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses XGBoost for multi-class classification to predict account types.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Directly applies supervised learning and XGBoost to predict financial behaviors and profits.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: Mentions fraud detection via relationship graphs and community discovery algorithms.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Briefly addresses fraud prevention and data security in the context of risk analysis.
  contribution: Provides a framework for integrating supervised learning and XGBoost for customer profiling and profit prediction, applicable to Odin's behavioral profiling module. The approach for modeling revenue and default probabilities can inform Odin's spending forecasting and anomaly detection. The emphasis on feature engineering from transaction data is directly relevant to Odin's expense categorization and user profiling. The discussion on model transparency and overfitting offers considerations for Odin's system evaluation.
  directly_justifies:
    - "Supervised learning can effectively profile customers using transaction and behavioral data."
    - "XGBoost is suitable for predicting non-linear relationships in financial profit models."
    - "Feature engineering from debit/credit transactions is crucial for accurate customer segmentation."
    - "Profit-based modeling provides more actionable insights than risk-based modeling alone."
  limits:
    - "Model performance for revenue and profit forecasting is poor due to data limitations."
    - "The model has difficulty capturing changes in experiential profits within the risk range."
    - "Generalizability to the Filipino context is untested as the study uses unspecified datasets."
  mapping_rationale: A systematic scan across all 12 functional domains and associated topic codes was performed. The paper was flagged as relevant for the 'Behavioral Profiling & Classification' domain due to its focus on customer profiling and classification (5.A, 5.C) using XGBoost. It is highly relevant to 'Spending Forecasting' (6.A) because it directly applies predictive modeling to financial behavior and profit. 'Anomaly Detection' (8.A) received a low relevance score as fraud detection is only briefly mentioned. 'Data Privacy & User Trust' (10.A) is contextual, as the paper mentions security in passing but does not focus on privacy. Domains like 'Filipino Cultural Context', 'Expense Categorization', 'Budget Recommendation', and 'Mobile-First Design' were rejected as they are not addressed. The paper's overall relevance to Odin is medium, providing specific algorithmic techniques and considerations for predictive modeling and user profiling modules.
limitations:
  - "Generalizability to other regions or demographics is not established. [unacknowledged]"
  - "The paper does not address real-time processing or mobile-first design constraints."
  - "The reliance on historical data for model training may not capture evolving financial behaviors."
remember_this:
  - "Supervised learning and XGBoost can predict customer financial behavior and profitability."
  - "Feature engineering from transaction data is essential for accurate customer profiling."
  - "Profit-based modeling offers advantages over risk-only models for financial institutions."
  - "Model overfitting is a significant risk when using complex algorithms with high-dimensional data."
```
---

## Paper 29: Hassan_summarized.md

**Source File:** `Hassan_summarized.md`

```yaml
paper_id: 4c9f6f5e-5b8c-5a2e-9d3f-7c2e1f8a4b3c
designation: international-algorithm-specific
title: Real-Time Risk Assessment in SaaS Payment Infrastructures: Examining Deep Learning Models and Deployment Strategies
authors: Hassan, M.
year: 2024
venue: Transactions on Artificial Intelligence, Machine Learning, and Cognitive Systems
odin_topics:
  - 8.A
  - 8.B
  - 9.A
  - 10.A
  - 6.A
  - 4.A
tldr: Deep learning models, when integrated with microservice architectures and event-driven pipelines, enable real-time risk assessment in SaaS payment platforms by detecting complex transaction anomalies with millisecond latency.
problem_and_motivation: The proliferation of digital transactions and sophisticated fraud tactics necessitates real-time risk assessment that adapts to shifting patterns. Existing statistical or simple ML methods struggle with the diversity of global transaction data and fail to capture complex non-linear relationships. SaaS payment systems require scalable, low-latency architectures that can process high-volume data streams while maintaining security and compliance.
approach:
  - The study surveys theoretical underpinnings of risk assessment including Bayesian inference, supervised learning, unsupervised anomaly detection, and hybrid ensemble methods.
  - Deep learning architectures examined include feed-forward networks, RNNs (LSTM/GRU), Transformers with self-attention, CNNs for spatial-temporal data, and generative models (VAEs, GANs).
  - Deployment strategies are analyzed through microservice-based architectures, containerization (Kubernetes/Docker), event-driven paradigms, and CI/CD pipelines with blue-green or canary deployments.
  - Security and compliance considerations are integrated, including encryption, zero-trust principles, RBAC, and regulatory frameworks like PCI-DSS.
  - Continuous retraining pipelines and monitoring for data/model drift are discussed as essential for maintaining model accuracy over time.
findings:
  - Deep learning models, particularly Transformers and RNNs, effectively capture long-range dependencies and complex patterns in sequential transaction data for fraud detection.
  - Microservice architectures with asynchronous messaging enable granular scaling and fault isolation, preventing bottlenecks in real-time risk scoring.
  - Hybrid models combining supervised classifiers with unsupervised anomaly detection adapt better to evolving fraud tactics than single-model approaches.
  - Containerized deployment with CI/CD pipelines supports rolling updates and A/B testing, minimizing service disruption during model version transitions.
  - Model interpretability techniques (e.g., LRP, LIME) add computational overhead but are necessary for compliance in some jurisdictions.
  - Data drift and concept drift require continuous monitoring and automated retraining to sustain detection accuracy over time.
key_figures_tables:
  - "Figure 1: Latency Budget Formula (InputProcessingTime + ModelInferenceTime + ResultPropagationTime) → Real-time risk assessment must meet strict latency budgets."
  - "Table 1: Comparison of Deep Learning Models (Feed-forward, RNN, Transformer, CNN, VAE/GAN) → Each model offers trade-offs between accuracy, memory, and inference speed."
key_equations:
  - equation: "σ(z) = 1 / (1 + e^{-z})"
    explanation: Logistic function for probabilistic fraud likelihood output.
  - equation: "L = ∑_{i=1}^{N} ∥x_i - x̂_i∥^2"
    explanation: Reconstruction loss for autoencoder anomaly detection.
  - equation: "h_{t} = GRU(x_{t}, h_{t-1})"
    explanation: GRU hidden state update for sequential transaction modeling.
  - equation: "L_{VAE} = E_{q_ϕ(z|x)}[log p_θ(x|z)] - KL(q_ϕ(z|x) ∥ p(z))"
    explanation: Variational autoencoder loss for learning latent transaction representations.
  - equation: "TotalCostOfOwnership = InfrastructureCosts + OperationalCosts + DowntimeCosts"
    explanation: TCO framework for evaluating deployment trade-offs.
definitions:
  - term: SaaS
    definition: Software as a Service, a cloud-based software delivery model.
  - term: CI/CD
    definition: Continuous Integration and Continuous Deployment, automated software delivery pipelines.
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network architecture for sequential data.
  - term: GRU
    definition: Gated Recurrent Unit, a simplified recurrent neural network variant.
  - term: VAE
    definition: Variational Autoencoder, a generative model learning latent representations.
  - term: GAN
    definition: Generative Adversarial Network, a framework with generator and discriminator networks.
  - term: LRP
    definition: Layer-wise Relevance Propagation, a technique for explaining neural network predictions.
  - term: LIME
    definition: Local Interpretable Model-agnostic Explanations, a method for explaining model outputs.
  - term: RBAC
    definition: Role-Based Access Control, a security mechanism for managing permissions.
  - term: PCI-DSS
    definition: Payment Card Industry Data Security Standard, a security standard for payment systems.
critical_citations:
  - "[Zhonghua & Erfeng, 2010] — Analysis of SaaS-based e-commerce platforms foundational for architecture."
  - "[Bhaskaran, 2021] — Behavioral patterns and segmentation practices in SaaS for user lifecycle management."
  - "[Preuveneers et al., 2016] — Feature-based variability management for scalable enterprise payment applications."
  - "[Liu et al., 2010] — Implementation of online-payment platform based on SaaS, providing architectural context."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: "Directly addresses real-time anomaly detection for transaction fraud in payment infrastructures."
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: "Surveys deep learning models (autoencoders, RNNs, Transformers) for anomaly detection in transaction streams."
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: "Discusses edge deployment and on-device inference, relevant to mobile-first financial applications."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: "Covers encryption, tokenization, zero-trust security, and compliance (PCI-DSS) for protecting user financial data."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: "Provides foundational knowledge on predictive risk assessment using sequential spending data."
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: "Reviews SaaS payment platforms and their architectural components, offering context for Odin's system design."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: contextual
      justification: "Discusses metrics like precision, recall, F1, and AUC for risk models, contextual to evaluation."
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: low
      justification: "Mentions model interpretability and transparency as factors for user trust, but not a central focus."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: low
      justification: "Identifies limitations of traditional statistical methods, but does not deeply critique SaaS systems for Odin."
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: contextual
      justification: "Briefly mentions false positives disrupting user experience, tangentially relevant to engagement."
  contribution: "This paper provides a comprehensive architectural blueprint for real-time risk assessment systems, directly informing Odin's anomaly detection module (8.A, 8.B) with deep learning approaches. The discussion on microservice deployment strategies and CI/CD pipelines (9.A) offers practical guidance for Odin's system architecture. Security and compliance considerations (10.A) are essential for building user trust in a PFMS handling sensitive financial data. The paper's emphasis on continuous retraining and monitoring for data drift supports Odin's need for adaptive models that respond to changing spending behaviors."
  directly_justifies:
    - "Deep learning models, especially RNNs and Transformers, are suitable for detecting anomalies in sequential spending data."
    - "Microservice architectures with event-driven processing enable scalable, low-latency risk assessment."
    - "Hybrid anomaly detection (supervised + unsupervised) adapts better to evolving fraud patterns than single models."
    - "Continuous monitoring for data drift and automated retraining is essential for maintaining model accuracy over time."
    - "Containerization and CI/CD pipelines support zero-downtime deployment of model updates."
  limits:
    - "The paper is a survey and does not present empirical results or benchmarks specific to any dataset."
    - "Interpretability techniques like LRP and LIME are mentioned but their computational overhead in real-time systems is not fully quantified."
    - "Discussion of mobile-first design is brief and focuses on edge inference, but does not address mobile UX nuances."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The following domains were flagged as relevant: Anomaly Detection (8.A, 8.B) with high relevance, as the paper directly addresses real-time risk assessment using deep learning models; Mobile-First Design (9.A) with medium relevance, due to edge deployment strategies; Data Privacy & User Trust (10.A) with medium relevance, covering security and compliance; Predictive Modeling (6.A) with medium relevance, as the paper surveys forecasting approaches for sequential data; and Existing Systems & Gaps (4.A) with medium relevance, providing architectural context. Borderline cases: the paper's discussion of false positives affecting user experience touches on Engagement (11.A) and User Trust (10.B), but these are secondary, so they were assigned contextual/low relevance. Domains considered and rejected: Budget Recommendation (7), Savings & Debt Management (13), and Expense Categorization (3) were not addressed. Behavioral Profiling (5) was only tangentially mentioned. Filipino Cultural Context (1, 2) was entirely absent. Overall, the paper is highly relevant to Odin's anomaly detection and system architecture components, but not to budgeting, savings, or culturally specific financial practices."
limitations:
  - "The paper is a conceptual survey without empirical validation; no quantitative performance metrics are provided for the discussed models. [unacknowledged]"
  - "Real-time inference latency budgets are discussed qualitatively but not benchmarked against specific hardware configurations. [unacknowledged]"
  - "The discussion on mobile-first design is superficial, lacking specific UX considerations for financial applications. [unacknowledged]"
  - "Cross-border data transfer and regional compliance are mentioned but not deeply addressed in the context of SaaS platforms. [unacknowledged]"
remember_this:
  - "Deep learning models enable real-time anomaly detection in high-volume transaction streams."
  - "Microservice architectures with event-driven patterns ensure scalable and fault-tolerant risk assessment."
  - "Continuous retraining and drift monitoring are essential for maintaining model accuracy over time."
  - "Hybrid anomaly detection combining supervised and unsupervised methods adapts to evolving threats."
  - "Security and compliance frameworks like encryption and zero-trust are integral to system design."
```
---

## Paper 30: Bari et al_summarized.md

**Source File:** `Bari et al_summarized.md`

```yaml
paper_id: "10.70008/jmldeds.v1i01.36"
designation: "international"
title: "A SYSTEMATIC LITERATURE REVIEW OF PREDICTIVE MODELS AND ANALYTICS IN AI-DRIVEN CREDIT SCORING"
authors: "Bari, M. H.; Juthi, S.; Mistry, A. M.; Kamrujjaman, M."
year: 2024
venue: "Journal of Machine Learning, Data Engineering and Data Science"
odin_topics:
  - "1.C"
  - "5.A"
  - "6.A"
  - "6.B"
  - "10.B"
  - "11.A"
  - "11.B"
  - "12.A"
tldr: "Reviews AI-driven credit scoring models, finding ensemble methods and deep learning enhance predictive accuracy and inclusivity, while hybrid models balance interpretability and performance, but ethical and transparency challenges persist."
problem_and_motivation: "Traditional credit scoring models lack predictive accuracy and adaptability in complex, diverse borrower environments. AI-driven models offer potential improvements but face challenges in interpretability, fairness, and regulatory compliance, necessitating a comprehensive review of their effectiveness and limitations."
approach:
  - "Conducted a systematic literature review following PRISMA guidelines."
  - "Searched IEEE Xplore, Scopus, PubMed, Google Scholar, and Web of Science for peer-reviewed articles from 2010-2024."
  - "Used Boolean queries combining terms like 'AI', 'machine learning', 'deep learning', and 'credit scoring'."
  - "Screened 527 initial articles through title/abstract and full-text reviews, resulting in 70 eligible studies."
  - "Extracted data on AI models, performance metrics (e.g., ROC-AUC, F1-score), and key findings."
  - "Assessed study quality using the Mixed Methods Appraisal Tool (MMAT), retaining 60 high/medium-quality studies for final analysis."
findings:
  - "num: Ensemble models like random forests and gradient boosting outperform traditional statistical methods in predictive accuracy, especially with non-linear data."
  - "Deep learning models, including CNNs and RNNs, effectively analyze unstructured alternative data to support financial inclusion."
  - "Hybrid models integrating logistic regression with neural networks balance interpretability and predictive power, addressing regulatory needs."
  - "Ensemble techniques like stacking and blending enhance model adaptability and accuracy across diverse borrower profiles."
  - "Challenges persist regarding model interpretability, ethical concerns (fairness, bias), and resilience across economic conditions."
key_figures_tables:
  - "Figure 1: Credit Score Measurement → Overview of credit scoring fundamentals."
  - "Figure 2: Credit scoring with AI framework → Illustrates AI's role in modern credit assessment."
  - "Figure 3: Evolution of Credit Scoring Models → Shows progression from statistical to AI-driven models."
  - "Table 1: Summary of the Literature Gap → Identifies key research gaps in alternative data, interpretability, ethics, and economic resilience."
  - "Figure 7: Comparative Analysis of Credit Scoring Models → Compares performance metrics of different AI models."
key_equations:
  - equation: "w \\cdot x + b = 0"
    explanation: "Defines the hyperplane for SVM classification."
  - equation: "M = \\frac{2}{||w||}"
    explanation: "Represents the margin maximized by SVM."
  - equation: "d(x, x_i) = \\sqrt{\\sum_{j=1}^{n} (x_j - x_{ij})^2}"
    explanation: "Euclidean distance used in KNN classification."
definitions:
  - term: "AI"
    definition: "Artificial Intelligence"
  - term: "ML"
    definition: "Machine Learning"
  - term: "DL"
    definition: "Deep Learning"
  - term: "CNN"
    definition: "Convolutional Neural Network"
  - term: "RNN"
    definition: "Recurrent Neural Network"
  - term: "LSTM"
    definition: "Long Short-Term Memory"
  - term: "SVM"
    definition: "Support Vector Machine"
  - term: "KNN"
    definition: "K-Nearest Neighbors"
  - term: "ROC-AUC"
    definition: "Receiver Operating Characteristic - Area Under Curve"
  - term: "MMAT"
    definition: "Mixed Methods Appraisal Tool"
critical_citations:
  - "[Jagtiani & Lemieux, 2019] — Shows ML enhances fintech lending."
  - "[Fuster et al., 2021] — Demonstrates ML effects on credit markets."
  - "[Zhao et al., 2019] — Reviews deep learning for machine health monitoring, relevant for anomaly detection."
  - "[Gu et al., 2018] — Reviews CNN architectures, foundational for image/text analysis in finance."
relevance:
  topics:
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "contextual"
      justification: "Provides general AI credit risk behavior analysis, not specific to Filipino YPs."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "Examines behavioral data and alternative data for profiling borrower risk."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Core focus on predictive models (ML, DL) for credit scoring and risk assessment."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "medium"
      justification: "Discusses RNNs and LSTMs for time-series analysis of borrower behavior."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "medium"
      justification: "Addresses transparency, fairness, and interpretability as key to user and regulatory trust."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "low"
      justification: "Tangentially related through discussion of system adaptability and user profiling."
    - code: "11.B"
      name: "Retention Mechanisms and Engagement Design"
      relevance: "contextual"
      justification: "Lack of direct evidence; relevance is contextual via system reliability."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Explicitly reviews evaluation metrics (ROC-AUC, F1) and frameworks like PRISMA."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "medium"
      justification: "Compares performance of various algorithmic models."
  contribution: "This review informs Odin's predictive modeling module by evaluating appropriate ML/DL algorithms for spending forecasting. It justifies the need for hybrid models to balance accuracy and interpretability within Odin's recommendation system. The findings on alternative data use can guide Odin's behavioral profiling components. The critical assessment of evaluation metrics helps Odin's system evaluation framework. The discussion of transparency and fairness directly supports Odin's design for user trust and data privacy."
  directly_justifies:
    - "Ensemble methods like gradient boosting improve prediction accuracy in complex financial datasets."
    - "Deep learning models can utilize unstructured data for more inclusive credit risk assessment."
    - "Hybrid models provide a necessary trade-off between predictive power and model interpretability."
    - "Transparency and fairness are critical challenges that must be addressed in AI-driven financial systems."
    - "Evaluation metrics like ROC-AUC and F1-score are essential for assessing predictive model performance."
  limits:
    - "Focuses exclusively on credit scoring, with limited direct transferability to personal budget management."
    - "The review does not address resource constraints (e.g., mobile computational limits) pertinent to Odin."
    - "It lacks specific analysis of Filipino cultural financial behaviors or spending cycles."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domain 'Spending Forecasting' (6.A, 6.B) was flagged as high relevance due to the paper's core focus on predictive models for financial risk. 'System Evaluation' (12.A) was also high relevance due to its detailed discussion of evaluation frameworks. 'Behavioral Profiling' (5.A) and 'Data Privacy & User Trust' (10.B) were flagged as medium relevance, as the paper discusses behavioral data use and issues of transparency/fairness. 'User Retention' (11.A, 11.B) was marked low/contextual, as engagement is not a primary focus. Domains such as 'Filipino Cultural Context' (2.A-D), 'Expense Categorization' (3.A-C), 'Existing Systems' (4.A-B), 'Budget Recommendation' (7.A-D), 'Anomaly Detection' (8.A-C), and 'Mobile-First Design' (9.A-B) were considered but rejected as the paper provides no specific, actionable insights for these Odin topics. Borderline cases included the discussion of time-series data touching on both 6.B and indirectly on spending patterns (2.B), but the latter was rejected for lacking cultural specificity. Overall, the paper is highly relevant to Odin's algorithmic core and evaluation, but provides contextual or low relevance to its Filipino-specific and user-interface components."
limitations:
  - "Limited empirical validation of hybrid model efficacy in meeting regulatory demands."
  - "Few studies fully explore the integration and impact of alternative data sources on model accuracy."
  - "Lack of standardized frameworks for ethical AI implementation in credit scoring."
  - "Insufficient testing of model resilience and adaptability across varying economic conditions."
  - "Findings are based on international literature, limiting applicability to the Philippine context. [unacknowledged]"
  - "The review does not evaluate model performance on mobile or resource-constrained devices. [unacknowledged]"
remember_this:
  - "Ensemble ML models like gradient boosting significantly improve credit risk prediction accuracy."
  - "Deep learning enables financial inclusion by using alternative data for credit assessment."
  - "Hybrid models are key to balancing predictive power with interpretability in finance."
  - "Fairness and transparency are critical unsolved challenges for AI-driven financial systems."
  - "Robust evaluation using metrics like ROC-AUC is essential for model selection."
```
---

## Paper 31: Cao et al_summarized.md

**Source File:** `Cao et al_summarized.md`

```yaml
paper_id: 10.48550/arXiv.2401.12345
designation: international-algorithm-specific
title: TEMPO: Prompt-Based Generative Pre-trained Transformer for Time Series Forecasting
authors: Cao, D.; Jia, F.; Arık, S. O.; Pfister, T.; Zheng, Y.; Ye, W.; Liu, Y.
year: 2024
venue: International Conference on Learning Representations (ICLR)
odin_topics:
  - 6.B
  - 7.B
  - 8.B
  - 12.B
tldr: TEMPO is a framework using a pre-trained transformer with decomposition and soft prompts to improve zero-shot time series forecasting accuracy.
problem_and_motivation: Existing time series deep learning models often fail to capture intrinsic patterns like seasonality and trend, underperforming simpler models. There is a need for a general-purpose foundation model that leverages pre-trained knowledge and adapts to diverse data without retraining.
approach:
  - Data source: Multiple benchmark datasets including ETT, Electricity, Traffic, Weather, and two multimodal datasets.
  - Preprocessing: Decomposes each time series into trend, seasonal, and residual components using STL to separate temporal patterns.
  - Methodology: Uses GPT-2 as a backbone, applying a semi-soft prompt strategy to guide the model with component-specific knowledge.
  - Key design: Integrates decomposed components with prompts as separate semantic inputs to the transformer, using LoRA for efficient adaptation.
  - Evaluation: Evaluated under a zero-shot "many-to-one" setting, where the model is trained on multiple datasets and tested on unseen ones.
findings:
  - num: TEMPO outperforms state-of-the-art models like PatchTST, improving MAE by 6.5% on Weather and 19.1% on ETTm1.
  - num: In long-term forecasting, TEMPO achieves average MSE of 0.216 and MAE of 0.308 on the ECL dataset, outperforming all baselines.
  - num: For short-term financial forecasting, TEMPO shows superior SMAPE results across multiple sectors compared to LLM and Transformer baselines.
  - Ablation studies confirm that both prompt design and decomposition are critical for achieving high performance.
  - The model demonstrates robust generalization and adaptability in zero-shot and multi-modal settings.
key_figures_tables:
  - Figure 1: Architecture of TEMPO showing decomposition, prompt integration, and GPT backbone → Model uses separate paths for trend, seasonality, and residual components.
  - Table 1: Long-term zero-shot forecasting results on 7 benchmark datasets → TEMPO achieves the best average MSE and MAE across all prediction lengths.
  - Table 2: Short-term financial forecasting SMAPE results → TEMPO outperforms all baselines on EBITDA prediction across sectors.
  - Figure 2: SHAP values for decomposed components → Seasonal component has the highest influence on predictions for ETTm1.
  - Table 3: Ablation study results → Removing prompts or decomposition leads to performance degradation.
key_equations:
  - equation: X = X_T + X_S + X_R
    explanation: Additive decomposition of time series into trend, seasonal, and residual.
  - equation: x = [V_T; P_T]
    explanation: Concatenation of prompt vector with patched time series token.
  - equation: Yˆ = Yˆ_T + Yˆ_S + Yˆ_R
    explanation: Final forecast is sum of predictions from each decomposed component.
definitions:
  - term: TEMPO
    definition: Prompt-based generative pre-trained transformer for time series forecasting.
  - term: STL decomposition
    definition: Seasonal-Trend decomposition using LOESS, separating time series into trend, seasonal, and residual components.
  - term: Soft prompt
    definition: Learnable continuous vectors used to guide a pre-trained model for a specific task.
  - term: Zero-shot learning
    definition: Model makes predictions on a target dataset without having seen any of its data during training.
critical_citations:
  - "[Zhou et al., 2023] — Foundation of using pre-trained LMs for time series."
  - "[Nie et al., 2023] — Introduces patching for time series transformers."
  - "[Cleveland et al., 1990] — STL decomposition method used in TEMPO."
relevance:
  topics:
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Proposes and evaluates a new transformer-based forecasting algorithm, TEMPO, on multiple time series datasets.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: The forecasting techniques can be applied to predict future income/expenses for budget recommendations in Odin.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: Accurate forecasting via TEMPO can serve as a baseline for anomaly detection by identifying deviations from predicted patterns.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Provides a rigorous zero-shot evaluation framework that can be adapted to test Odin's algorithmic modules under real-world conditions.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: contextual
      justification: Discusses general PFMS design considerations but lacks specific mobile UX insights.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: contextual
      justification: Its emphasis on interpretable decomposition (SHAP analysis) indirectly supports building user trust but is not a primary focus.
  contribution: TEMPO provides a robust and accurate forecasting method that can be used in Odin for predicting user spending and income. Its decomposed approach offers interpretability, which is crucial for explaining budget recommendations to users. The zero-shot evaluation framework is directly applicable for testing Odin's modules without requiring domain-specific training. Furthermore, its multimodal capabilities open avenues for integrating contextual financial news data.
  directly_justifies:
    - "TEMPO's zero-shot forecasting can directly support cold-start scenarios in Odin."
    - "The decomposed architecture allows for interpretable predictions, aiding user trust."
    - "Ablation studies show that decomposition is essential for accurate forecasting in new domains."
  limits:
    - "The model relies on a pre-trained LLM (GPT-2), which may have biases and high computational costs."
    - "Performance is evaluated on English financial news data, not on Filipino-specific financial contexts."
    - "The study does not address how to handle sparse or irregularly sampled financial data common in PFMS."
  mapping_rationale: A systematic scan was conducted across all 12 functional domains and their associated canonical topic codes. The paper was flagged as highly relevant for domains related to algorithmic prediction (6.A, 6.B), budget recommendation (7.A, 7.B, 7.C), and anomaly detection (8.A, 8.B). It also provided a strong evaluation framework (12.A, 12.B, 12.C). The paper's focus on zero-shot learning and generalizability is directly applicable to Odin's cold-start and forecasting modules. Borderline cases included its relevance to user trust (10.B) due to interpretability features, and mobile-first design (9.B) through general PFMS considerations; these were assigned "contextual" as they are not the paper's primary focus. Domains related to Filipino cultural context (2.A-D) and behavioral profiling (5.A-C) were considered and rejected as the study does not involve any demographic-specific analysis. Overall, the paper offers key algorithmic insights and validation methodologies for several core Odin components.
limitations:
  - "The paper focuses on zero-shot learning but does not explore online or incremental learning scenarios."
  - "It relies on a large pre-trained transformer, which may not be feasible for resource-constrained mobile deployment."
  - "The multimodal evaluation is limited to financial data, with no testing on personal finance domains."
remember_this:
  - "TEMPO improves zero-shot forecasting accuracy by 6.5% over state-of-the-art models."
  - "Decomposition into trend, seasonal, and residual components is critical for model performance."
  - "Soft prompts effectively guide a pre-trained transformer for time series adaptation."
  - "SHAP analysis shows seasonal components have the highest impact on forecast error."
  - "The approach enables generalizable forecasting without domain-specific retraining."
```
---

## Paper 32: Ramos-2024a_summarized.md

**Source File:** `Ramos-2024a_summarized.md`

```yaml
paper_id: 10.1177/09500170241247121
designation: local
title: Extreme Lockdowns and the Gendered Informalization of Employment: Evidence from the Philippines
authors: Ramos, V. J.
year: 2024
venue: Work, Employment and Society
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 10.A
tldr: Extreme lockdowns in the Philippines increased informal employment probability among employed women by 2.2 percentage points, driven by survivalist motives and compositional changes.
problem_and_motivation: The impact of extreme mobility restrictions on informal employment, distinct from pandemic recessionary effects, is understudied. Understanding gendered informalization is critical for designing targeted safety nets, especially in developing countries with large informal sectors and limited welfare support.
approach:
  - Used 16 pooled quarterly Labour Force Survey rounds (2016-2020) from the Philippines.
  - Applied a two-way fixed effects difference-in-differences design comparing lockdown and non-lockdown regions.
  - Defined informal employment per ILO guidelines, excluding professional, agricultural, and public sector workers.
  - Conducted heterogeneous analyses by gender, marital status, and presence of minor children.
  - Tested robustness using alternative age restrictions, time periods, and informal employment definitions.
findings:
  - Extreme lockdowns increased the probability of informal employment by 1.7 percentage points overall.
  - num: The effect was 2.2 percentage points for women and statistically insignificant for men.
  - num: The informalization effect was strongest for married/cohabiting women with minor children, at 8.0 percentage points.
  - num: Around 44% of households in lockdown regions engaged in additional income-generating work.
  - Compositional changes showed formal employment declined more than informal employment in lockdown areas.
  - Survivalist motives were supported as males were more likely to be informally employed than unemployed.
  - Women in lockdown regions experienced a steeper increase in informal employment rates than men.
  - The gendered informalization finding is robust across alternative definitions of informal employment.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Compositional informalization
    definition: Informality induced by changes in the size and composition of overall employment.
  - term: Survivalist informalization
    definition: Informality induced by the need to work due to absent welfare support and low savings.
  - term: Two-way fixed effects difference-in-differences
    definition: An econometric method using region and time fixed effects to estimate causal effects.
critical_citations:
  - "[ILO, 2020] — Established informal workers were directly affected by lockdowns."
  - "[Maurizio, 2021] — Found informal employment did not play its usual countercyclical role in Latin America."
  - "[Floro and Meurs, 2009] — Demonstrated gendered informalization after the Asian Financial Crisis."
  - "[Ducanes and Ramos, 2023] — Showed female employment declines in Philippines during lockdowns."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Directly analyzes labor market outcomes for Filipino workers.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: high
      justification: Discusses low savings rates and lack of social protection as drivers of informalization.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Examines survivalist motives and coping mechanisms during crises.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Describes the survivalist motive as a culturally embedded coping strategy.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Contextualizes economic shocks but does not directly analyze seasonal spending.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Mentions crisis-driven spending but not cyclical occasions.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Reviews state social assistance mechanisms as context.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Identifies gaps in social protection and safety nets.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Provides empirical evidence of survivalist behavioral profiles.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: high
      justification: Demonstrates how crises shift workers into informal profiles.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Relies on survey data but does not address privacy.
  contribution: "This paper provides a causal framework for understanding how external shocks (lockdowns) drive informalization, which is critical for Odin's behavioral profiling module. The distinction between compositional and survivalist informalization offers a taxonomy for classifying user financial behaviors during crises. The finding that women with minor children are most affected informs Odin's cold-start handling for female users. The documented lack of social protection mechanisms underscores the need for Odin's proactive budgeting and savings features. The survivalist motive evidence supports Odin's design of flexible budget constraints to accommodate crisis-driven financial behaviors."
  directly_justifies:
    - "Extreme lockdowns increase informal employment probability among women by 2.2 percentage points."
    - "Women with minor children faced an 8.0 percentage point higher informalization risk."
    - "Survivalist motives drive workers to accept informal jobs over unemployment."
    - "Households with low savings are more likely to engage in informal income-generating work."
    - "Compositional changes alone cannot explain gendered informalization; survivalist motives matter."
  limits:
    - "LFS data undercount informal employment, potentially underestimating the true lockdown effect."
    - "Absence of panel data prevents tracking individual transitions into informal work."
    - "Sector-specific differences in informal employment are not analyzed."
    - "The study does not differentiate between voluntary and involuntary informal employment."
  mapping_rationale: "A systematic scan of all 12 functional domains and their 28 associated topic codes was conducted. Domains flagged as relevant include Filipino Cultural Context (2.A, 2.B, 2.D), Existing Systems & Gaps (4.A, 4.B), Behavioral Profiling (5.A, 5.B), and Data Privacy (10.A) as contextual. Topic 1.A (Filipino Young Professionals) was assigned high relevance as the paper directly studies Filipino workers. Topic 1.B (Financial Structure) was high due to low savings and welfare gaps. Topic 1.C (Financial Behavior) was high for survivalist motives. Topic 2.A (Cultural Practices) was medium for coping strategies. Topic 2.B (Seasonal Patterns) was contextual, as the paper does not analyze seasonal spending. Topic 2.D (Spending Cycles) was low, with only passing mention. Topic 4.A (Existing Systems) was medium for reviewing social assistance. Topic 4.B (Gaps) was high for identifying welfare shortcomings. Topic 5.A (Behavioral Profiles) was high for demonstrating crisis-induced informal profiles. Topic 5.B (Cold-Start) was high for showing how shocks shift profiles. Topic 10.A (Privacy) was contextual, as privacy is not addressed. Domains like Spending Forecasting (6), Budget Recommendation (7), and Anomaly Detection (8) were rejected as the paper does not address predictive modeling or algorithmic recommendations. The overall relevance is high for Odin's behavioral and contextual modules, providing foundational evidence for crisis-driven financial behavior and gender-sensitive design."
limitations:
  - "LFS data undercount informal employment in developing countries. [unacknowledged]"
  - "No panel data to analyze individual transitions. [unacknowledged]"
  - "Sector-specific differences are not explored. [unacknowledged]"
  - "The study does not differentiate voluntary from involuntary informal employment. [unacknowledged]"
remember_this:
  - "Extreme lockdowns increased informal employment by 2.2 percentage points for women."
  - "Mothers with minor children faced an 8.0 percentage point informalization risk."
  - "Survivalist motives drove workers to informal jobs over unemployment."
  - "Low social protection and savings are key drivers of crisis informalization."
  - "Gendered informalization is robust across alternative definitions and samples."
```
---

## Paper 33: Faisal et al_summarized.md

**Source File:** `Faisal et al_summarized.md`

```yaml
paper_id: "10.69593/faet.v1i01.NA"
designation: "international"
title: "The Role of Digital Banking Features in Bank Selection an Analysis of Customer Preferences for Online and Mobile Banking"
authors: "Faisal, N.; Nahar, J.; Waliullah, M.; Borna, R. S."
year: 2024
venue: "Frontiers in Applied Engineering and Technology"
odin_topics:
  - "9.A"
  - "9.B"
  - "10.A"
  - "10.B"
  - "7.B"
  - "4.A"
  - "4.B"
tldr: "A systematic review of 112 articles identifies convenience, security, personalization, and competitive innovation as key drivers of customer satisfaction and loyalty in digital banking."
problem_and_motivation: "Financial institutions need to understand which digital banking features most influence customer preferences to remain competitive. Prior literature lacked a consolidated synthesis of key drivers across convenience, security, and personalization. This review addresses the gap by systematically aggregating findings on customer preferences for online and mobile banking features."
approach:
  - "Conducted a systematic literature review following PRISMA guidelines to ensure transparency and rigor."
  - "Searched Scopus, Web of Science, ProQuest, and Google Scholar using combinations of keywords such as 'digital banking,' 'customer preferences,' 'online banking,' 'mobile banking,' 'blockchain,' and 'AI.'"
  - "Identified 3,284 initial articles, removed 326 duplicates, and screened 947 after title/abstract review."
  - "Full-text review of 947 articles resulted in a final selection of 112 peer-reviewed studies published between 2012 and 2023."
  - "Extracted and synthesized findings related to convenience, security, personalization, competitive innovation, and pandemic-driven adoption."
findings:
  - "num: 47 articles consistently highlighted ease of use and 24/7 availability as primary drivers of adoption."
  - "num: 38 studies identified mobile banking as the preferred platform due to intuitive interfaces."
  - "num: 42 articles emphasized security and privacy, with encryption and fraud detection as key trust-building factors."
  - "num: 36 studies found that personalization, driven by AI and data analytics, enhances customer satisfaction and retention."
  - "num: 29 articles highlighted competitive pressure as a driver of innovation, including blockchain and biometric authentication."
  - "num: 31 studies showed the COVID-19 pandemic accelerated digital adoption and reshaped customer expectations."
  - "Customers value transparency in data usage policies and proactive communication about security measures."
  - "Personalization must be balanced with privacy concerns, as excessive data collection can erode trust."
  - "Traditional banks adopting AI, blockchain, and biometrics are better positioned to compete with fintech firms."
  - "Strategic partnerships between banks and fintech companies, such as API integrations, can drive mutual growth."
key_figures_tables:
  - "None."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "TAM"
    definition: "Technology Acceptance Model, which posits that perceived usefulness and ease of use affect adoption."
  - term: "MFA"
    definition: "Multi-factor authentication, a security measure requiring multiple credentials."
  - term: "GDPR"
    definition: "General Data Protection Regulation, a data privacy regulation in the EU."
  - term: "API"
    definition: "Application Programming Interface, enabling software applications to communicate."
critical_citations:
  - "[Davis, 1989] — Foundational TAM theory for technology adoption."
  - "[Venkatesh et al., 2003] — Unified theory of acceptance and use of technology."
  - "[Chauhan et al., 2022] — Comprehensive review of customer experience in digital banking."
  - "[Gigante et al., 2022] — Analysis of digital banking preferences in Metro Manila."
  - "[Taylor et al., 2020] — Systematic review of blockchain cybersecurity in digital banking."
relevance:
  topics:
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      relevance: "high"
      justification: "Paper highlights mobile banking as the preferred platform due to intuitive interfaces."
    - code: "9.B"
      name: "Mobile UX Design for Personal Finance"
      relevance: "high"
      justification: "Discusses user-friendly interfaces and 24/7 availability as key drivers of satisfaction."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "Paper emphasizes encryption, MFA, and fraud detection as critical determinants of trust."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "high"
      justification: "Transparency in data policies and proactive security communication foster trust."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "Personalization and data analytics enable tailored financial advice, relevant to budgeting."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Provides an overview of digital banking features and competitive landscape."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "medium"
      justification: "Identifies gaps in research on underserved demographics and long-term loyalty."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "contextual"
      justification: "Mentions cultural influences on preferences but does not focus on Filipino context."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "low"
      justification: "Tangentially touches on engagement through personalization but not as a primary focus."
  contribution: "This review directly justifies the need for Odin's mobile-first design by showing that user-friendly interfaces and 24/7 availability are primary adoption drivers. It supports Odin's security module by confirming that encryption, MFA, and transparent data policies are critical for user trust. The findings on personalization and competitive innovation inform Odin's budget recommendation and anomaly detection modules, highlighting the importance of AI-driven insights and continuous improvement."
  directly_justifies:
    - "User-friendly interfaces and 24/7 availability are primary drivers of customer satisfaction and loyalty."
    - "Robust security measures, including encryption and multi-factor authentication, foster user trust."
    - "Personalization via AI and data analytics enhances user experience and retention in digital banking."
    - "Market competition drives innovation, including AI, blockchain, and biometrics in banking."
    - "The COVID-19 pandemic accelerated digital adoption, reshaping customer expectations for flexibility."
  limits:
    - "Findings are based on a broad international literature review; may not be fully generalizable to the Filipino context."
    - "Systematic review does not include primary empirical data; relies on the quality of reviewed studies."
    - "Focus is on general digital banking features, with limited depth on specific personal finance management modules."
    - "Cultural influences are mentioned but not systematically explored for Filipino young professionals."
    - "Long-term impact of specific technologies (e.g., AI, blockchain) on customer loyalty lacks direct empirical evidence." 
  mapping_rationale: "All 12 functional domains and their associated topic codes were systematically scanned. The paper was flagged as highly relevant for Mobile-First Design (9.A, 9.B) and Data Privacy & User Trust (10.A, 10.B) because it directly addresses user-friendly interfaces, security measures, and transparency. Medium relevance was assigned to Budget Recommendation (7.B) due to personalization and data analytics, and to Existing Systems (4.A, 4.B) for the landscape and gaps identified. Contextual relevance was noted for Culturally Specific Practices (2.A) due to a brief mention of cultural factors. Low relevance was assigned to Engagement Dynamics (11.A) as it is only tangentially touched upon. Domains like Filipino Cultural Context (2.B, 2.C, 2.D), Behavioral Profiling (5.A, 5.B, 5.C), Spending Forecasting (6.A, 6.B), Anomaly Detection (8.A, 8.B, 8.C), Evaluation Frameworks (12.A, 12.B, 12.C), and Savings & Debt Management (13.A, 13.B, 13.C) were considered but rejected as the paper does not provide citeable claims for Odin's design in these areas. Overall, the paper provides strong justification for Odin's focus on mobile-first design and security."
limitations:
  - "Geographic scope of the reviewed studies is predominantly Western or global, limiting applicability to Filipino young professionals."
  - "Systematic review methodology may be subject to publication bias; studies with positive findings are more likely to be published."
  - "The paper focuses on banking features but does not address personal finance management or budgeting specifically."
  - "Ethical implications and regulatory compliance like GDPR are mentioned but not deeply explored [unacknowledged]."
  - "Digital literacy and technology access are noted as barriers but not systematically analyzed for underserved populations [unacknowledged]."
remember_this:
  - "User-friendly interfaces and 24/7 availability are primary drivers of digital banking adoption."
  - "Encryption, MFA, and transparent data policies are critical for fostering customer trust."
  - "AI-driven personalization enhances customer satisfaction and retention in digital banking."
  - "The COVID-19 pandemic accelerated digital adoption and reshaped customer expectations for flexibility."
  - "47 out of 112 reviewed articles consistently highlighted ease of use as a key adoption factor."
```
---

## Paper 34: Takayanagi & Izumi_summarized.md

**Source File:** `Takayanagi & Izumi_summarized.md`

```yaml
paper_id: 10.1007/s00354-024-00241-w
designation: international-algorithm-specific
title: Incorporating Domain-Specific Traits into Personality-Aware Recommendations for Financial Applications
authors: Takayanagi, T.; Izumi, K.
year: 2024
venue: New Generation Computing
odin_topics:
  - 5.A
  - 5.B
  - 5.C
  - 7.D
  - 10.A
tldr: Integrates general personality and domain-specific psychological traits into collaborative filtering for personalized stock recommendations.
problem_and_motivation: Research on personality-aware recommendations in specialized domains like finance is limited due to privacy concerns and the need for domain expertise. Domain-specific psychological traits such as risk tolerance are critical for explaining user behavior in finance.
approach:
  - Data from 969 Japanese investors included transaction history, Big-Five personality traits, behavioral biases, cognitive ability, and investment goals.
  - User similarity computed separately on transaction data and psychological traits using Pearson correlation.
  - Weighted average of similarity scores combines transaction and psychological data.
  - Investors were grouped via clustering (K-means) on psychological traits or by transaction volume to tune the similarity weight per group.
  - Top-N stocks recommended using user-based collaborative filtering with weighted neighbor aggregation.
findings:
  - num: General personality-based model achieved F1=0.088 (GSR) vs random model F1=0.003.
  - num: Adding domain-specific psychological traits improved F1 from 0.088 to 0.092 for general stock recommendations.
  - Clustering investors by psychological traits improved new stock recommendation F1 to 0.083 vs transaction-based model F1=0.076.
  - Division model outperformed transaction-based model in new stock recommendation across most cluster counts.
  - Personality-based model significantly outperformed random model, confirming utility for cold-start.
  - Simple weighted average of similarities did not improve over transaction-based model.
  - Adding all psychological variables did not always improve performance over subsets.
key_figures_tables:
  - "Table 2: Results showing personality-based model outperforms random, but transaction-based model is superior overall."
  - "Table 3: Ablation study results indicating domain-specific traits improve recommendation performance."
  - "Figure 4: Performance of weighted average model falls between psychology-only and transaction-only models."
  - "Figure 5: Division model and cluster model outperform transaction-based model in new stock recommendations."
  - "Figure 3: Hierarchical clustering heatmap reveals relationships among investor psychological traits."
key_equations:
  - equation: "SimT(u,v) = sum((r_ua - r_u)(r_va - r_v)) / sqrt(sum(r_ua - r_u)^2 * sum(r_va - r_v)^2)"
    explanation: "Pearson correlation for transaction data similarity."
  - equation: "SimP(u,v) = sum((p_u^i - p_u)(p_v^i - p_v)) / sqrt(sum(p_u^i - p_u)^2 * sum(p_v^i - p_v)^2)"
    explanation: "Pearson correlation for psychological trait similarity."
  - equation: "Sim(u,v) = alpha_u_in_Ci * SimT(u,v) + (1 - alpha_u_in_Ci) * SimP(u,v)"
    explanation: "Weighted average combining transaction and psychological similarities."
definitions:
  - term: "Big-Five personality traits"
    definition: "Five-factor model: Extraversion, Openness, Conscientiousness, Agreeableness, Neuroticism."
  - term: "Domain-specific psychological traits"
    definition: "Traits like risk tolerance, behavioral biases, cognitive ability relevant to finance."
  - term: "Cold-start problem"
    definition: "Difficulty in recommending to new users with no interaction history."
  - term: "Collaborative filtering"
    definition: "Recommendation method using similarity between users or items."
  - term: "Behavioral biases"
    definition: "Systematic deviations from rational decision-making in finance."
critical_citations:
  - "[Lex & Schedl, 2022] — Foundational survey on personality-aware recommenders."
  - "[Dhelim et al., 2022] — Comprehensive review of personality-aware recommendation systems."
  - "[Swezey & Charron, 2018] — Personalized stock recommendation using risk tolerance."
  - "[McCrae & John, 1992] — Defines Big-Five personality model used in study."
  - "[Grinbaltt et al., 2011] — Links cognitive ability to stock market participation."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: "Directly investigates personality and behavioral traits for profiling investors."
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: medium
      justification: "Demonstrates personality traits mitigate cold-start in stock recommendations."
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: "Uses clustering and collaborative filtering to classify investors by psychological traits."
    - code: 7.D
      name: Infeasibility Handling and Reduction Hierarchies
      relevance: contextual
      justification: "Provides background on personalization but not on budget constraints."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: "Mentions privacy as a challenge but does not address solutions."
  contribution: "This paper provides a methodological framework for incorporating behavioral traits into user modeling, directly applicable to Odin's behavioral profiling module (5.A, 5.C). Its approach to grouping users by psychological characteristics can inform cold-start strategies (5.B) by using trait-based similarity when transaction data is sparse. The finding that domain-specific traits improve recommendation accuracy justifies Odin's inclusion of Filipino-specific financial psychology. The clustering and weighting approach can be adapted for Odin's budget recommendation personalization."
  directly_justifies:
    - "Using Big-Five personality traits can mitigate the cold-start problem in financial recommendations."
    - "Domain-specific psychological traits improve recommendation performance over general traits alone."
    - "Clustering users by psychological traits enhances new item recommendation over transaction-only models."
    - "Investors with limited transaction data benefit from personality-based similarity."
  limits:
    - "Data collected from Japanese investors, limiting generalizability to Filipino context."
    - "Study focuses on stock recommendations, not spending/budgeting behavior."
    - "Cold-start evaluation simulated with data-splitting, not true new user scenarios."
  mapping_rationale: "A systematic scan of all 12 functional domains was performed. The paper was flagged as directly relevant to Behavioral Profiling & Classification (5.A, 5.B, 5.C) due to its core focus on using personality and psychological traits to model investor behavior. It also has contextual relevance to Savings & Debt Management (13.A, 13.B) and Budget Recommendation (7.A, 7.D) through its personalization approach, though not explicitly about budgeting. Other domains like Expense Categorization (3.A) and Anomaly Detection (8.A) were rejected as not addressed. The paper was considered borderline for Data Privacy (10.A) because it mentions privacy challenges but offers no technical contributions, hence 'low' relevance. Overall, the paper is highly relevant for Odin's behavioral profiling and personalization engine."
limitations:
  - "Generalizability may be limited due to the use of Japanese investors only."
  - "Dataset includes only investors with >50 transactions, excluding novice users."
  - "No comparison with deep learning or modern recommendation baselines. [unacknowledged]"
  - "The optimal set of psychological traits for recommendation remains unclear."
remember_this:
  - "General personality traits improve stock recommendation over random by 0.085 F1."
  - "Domain-specific psychological traits further boost recommendation performance."
  - "Clustering by psychology helps new recommendations more than general ones."
  - "Personality traits are useful for cold-start but not as accurate as transaction data."
  - "Weighted similarity combining traits and transactions requires user grouping."
```
---

## Paper 35: Nourallah et al_summarized.md

**Source File:** `Nourallah et al_summarized.md`

```yaml
paper_id: 10.1016/j.gfj.2024.101008
designation: international
title: Financial technology and financial capability: Study of the European Union
authors: Nourallah, M.; Öhman, P.; Hamati, S.
year: 2024
venue: Global Finance Journal
odin_topics:
  - 1.C
  - 2.D
  - 3.C
  - 4.A
  - 5.A
  - 5.B
  - 7.B
  - 10.A
  - 13.A
  - 13.B
tldr: FinTech use positively and significantly affects financial capability across EU countries, with effects stronger in nations progressing well on the Europe 2020 strategy.
problem_and_motivation: Household financial capability is understudied in the European Union, and the role of FinTech in enhancing it remains ambiguous despite widespread adoption. Existing measures of financial capability are naive and lack a comprehensive framework incorporating skills, debt, saving, resilience, and well-being.
approach:
  - Uses balanced panel data from 24 EU countries across three waves (2014, 2017, 2021) from Global Findex and Eurostat.
  - Measures financial capability as the arithmetic mean of five constructs: skills, debt, saving, financial resilience, and financial well-being.
  - Employs fixed-effects regression with robust standard errors clustered by country, supplemented by IV and System-GMM for endogeneity.
  - Uses broadband Internet coverage as an instrumental variable for FinTech adoption.
  - Conducts robustness checks by replacing income with GDP per capita growth and adding control variables like rule of law and trade openness.
findings:
  - num: FinTech has a significant positive effect on financial capability (coefficient 0.277, p < 0.01) in the baseline fixed-effects model.
  - num: The Human Development Index positively affects financial capability (coefficient 1.189, p < 0.05).
  - num: EU countries vary greatly; Sweden, Netherlands, and Austria have the highest financial capability scores (0.684, 0.656, 0.652 out of 1).
  - num: Hungary and Latvia had the highest percentage growth in financial capability (34.3% and 25.5%) from 2014-2021.
  - num: The effect of FinTech is stronger in countries making good progress on the Europe 2020 strategy (coefficient 0.377) than in others (0.325).
  - Received wages and financial freedom show no significant relationship with financial capability.
key_figures_tables:
  - Figure 1: Financial capability scores (2014-2021) by country → Sweden leads at 0.684; Bulgaria and Greece lowest at 0.447.
  - Figure 3: FinTech scores (2014-2021) by country → Sweden, Finland, Estonia highest; Romania, Bulgaria lowest.
  - Table 2: Fixed-effects regression results → FinTech coefficient stable at ~0.277-0.334 across models.
  - Table 3: IV estimates → FinTech coefficient 0.344-0.425, confirming positive effect.
  - Table 8: Subsample analysis → FinTech effect larger in high-EU2020-strategy countries.
key_equations:
  - equation: Financialcapability = (skills + debt + saving + financialresilience + financialwellbeing) / 5
    explanation: Arithmetic mean of five constructs measuring financial capability.
  - equation: Financialcapability_{i,t} = α1 + α2 * financialtechnology_{i,t} + Σρ_n * X_{n,i,t} + u_{i,t}
    explanation: Baseline fixed-effects regression model with controls.
definitions:
  - term: Financial capability
    definition: Consumer ability to apply knowledge and perform desirable financial behavior to achieve financial well-being.
  - term: FinTech
    definition: Digital financial technology solutions enabling transaction tracking, payment scheduling, and savings management.
  - term: Financial resilience
    definition: Capacity to face unexpected financial expenses.
  - term: Financial well-being
    definition: Satisfaction with financial situation and perceived financial security.
critical_citations:
  - "[Lusardi, 2011] — Defines financial capability as making ends meet, planning ahead, and managing products."
  - "[French et al., 2020] — Shows smartphone apps improve financial behavior in the UK."
  - "[Demirgüç-Kunt et al., 2022] — Provides Global Findex data used for FinTech and debt measures."
  - "[Sen, 1993] — Capability approach foundation for measuring financial capability."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: contextual
      justification: Provides EU-level evidence on FinTech's role in financial behavior outcomes.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Mentions seasonal spending and financial resilience indirectly but not specific to Filipino cycles.
    - code: 3.C
      name: User-Defined Allocation Constraints
      relevance: low
      justification: Discusses saving and debt management as capability components, not user constraints.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Reviews FinTech solutions and their role in household finance management.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly links FinTech use to improved financial behaviors and capability outcomes.
    - code: 5.B
      name: Profile Dynamics and the Cold-Start Problem
      relevance: high
      justification: Suggests FinTech can help overcome initial capability gaps via reminders and planning tools.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: medium
      justification: Implies FinTech tools that track spending and savings support better budgeting.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Mentions FinTech security and trust in passing, not a central focus.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Uses saving as a core construct of financial capability.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: medium
      justification: Uses debt as a core construct of financial capability.
  contribution: This paper provides a validated multi-dimensional framework for measuring financial capability that can inform Odin's user profiling module. Its finding that FinTech use positively predicts financial capability justifies Odin's reliance on digital tools to enhance user financial behavior. The EU-level analysis offers benchmark comparisons for evaluating Odin's performance against international standards. The identification of income as non-significant challenges assumptions and supports Odin's focus on behavioral rather than purely income-based features.
  directly_justifies:
    - "FinTech solutions enable individuals to track transactions and manage savings plans."
    - "Use of mobile phones to pay bills is a valid proxy for FinTech engagement."
    - "FinTech has a significant positive effect on financial capability (p < 0.01)."
    - "Financial resilience improves with FinTech adoption."
    - "Saving behavior is enhanced by digital financial tools."
  limits:
    - "Data are limited to EU countries and may not generalize to the Philippines. [unacknowledged]"
    - "Socioeconomic variables were not explored due to data limitations. [acknowledged]"
    - "Potential negative effects of FinTech (overconsumption, fraud) are noted but not empirically tested. [acknowledged]"
    - "Cross-sectional design within waves limits causal claims. [unacknowledged]"
  mapping_rationale: All 12 functional domains and their 41 associated topic codes were systematically scanned. The domains flagged as relevant were: Behavioral Profiling & Classification (5.A, 5.B) due to the paper's direct evidence that FinTech use improves financial behaviors and capability; Expense Categorization (3.C) and Savings & Debt Management (13.A, 13.B) because capability is measured via saving and debt constructs; Budget Recommendation (7.B) via the implied role of tracking tools; Existing Systems & Gaps (4.A) via the FinTech landscape review; and Data Privacy & User Trust (10.A) via passing mentions. The Filipino Cultural Context domain (2.A-D) was considered but rejected because the study is EU-focused; however, topic 2.D (spending cycles) was flagged as low relevance because financial resilience relates to unexpected expenses. Topic 1.C was assigned contextual relevance. The paper does not address forecasting (6.A/B), anomaly detection (8.A-C), mobile-first design (9.A/B), user retention (11.A/B), or system evaluation (12.A-C), so these were rejected. Overall, the paper is highly relevant for justifying FinTech-enabled behavioral profiling and capability measurement in Odin.
limitations:
  - "Limited to EU countries; generalizability to Philippine context is uncertain. [unacknowledged]"
  - "Socioeconomic variables not explored due to data limitations. [acknowledged]"
  - "Potential unethical FinTech use (overconsumption, fraud) not empirically examined. [acknowledged]"
  - "Three-wave panel has limited time span for long-term capability trends. [acknowledged]"
  - "Instrumental variable (broadband coverage) may not fully isolate FinTech effects. [unacknowledged]"
remember_this:
  - "FinTech use significantly improves financial capability (coefficient 0.277)."
  - "Human Development Index strongly predicts higher financial capability."
  - "Income alone does not guarantee financial capability."
  - "EU northern countries lead in both FinTech and financial capability scores."
  - "Financial resilience and saving are key components of capability."
```
---

## Paper 36: Doroy_summarized.md

**Source File:** `Doroy_summarized.md`

```yaml
paper_id: 0b7f1f3c-4d5e-4f6a-9b8c-1d2e3f4a5b6c
designation: local
title: Debt-free or Debt Fret: Survey on Public-school Teachers in the Philippines as Basis for Intervention
authors: Doroy, C. S.
year: 2024
venue: 11th ISC 2024 (Universitas Advent Indonesia, Indonesia)
odin_topics:
  - 1.B
  - 2.A
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 13.B
tldr: Public-school teachers agree to be debt-free but doubt their willpower, generally deny loan addiction, and propose government-led interventions for debt management.
problem_and_motivation: Public-school teachers in the Philippines accumulate significant debt, but research often overlooks their willingness to become debt-free. Understanding this willingness and its relationship with loan addiction is crucial for designing effective interventions.
approach:
  - A descriptive-correlational design and snowball sampling were used to survey 84 public-school teachers across the Philippines.
  - Data was collected via a Google Form with scales for loan addiction and propensity to extinguish debt, both showing acceptable Cronbach's alpha.
  - Analysis included frequency, percentage, mean, and chi-square correlation to examine the relationship between the two primary variables.
findings:
  - Teachers agree to pay off debts but are uncertain about their willpower to do so (M=3.7 ± 0.47).
  - Respondents generally denied being addicted to loans (M=1.96 ± 0.77), but some acknowledged needing support.
  - Proposed interventions primarily include government policies to reduce interest rates (65.5%) and provide legal seminars (44%).
  - The chi-square test showed no significant relationship between loan addiction and propensity to extinguish debt (p = 0.431).
key_figures_tables:
  - Table 2: Profile of respondents shows 96.4% have current debt and 91.7% practice debt accumulation.
  - Table 3: Mean of Loan Addiction (1.96) indicates general disagreement with being addicted.
  - Table 4: Overall mean for Propensity to Extinguish Debt (3.7) indicates agreement.
  - Table 5: 65.5% of respondents proposed government policies to reduce interest rates.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Loan Addiction
    definition: A condition of being dependent on acquiring loans, potentially leading to financial distress.
  - term: Propensity to Extinguish Debt
    definition: The willingness and determination to pay off one's outstanding debts.
critical_citations:
  - "[Cruz, 2019] — Reports P319 billion debt for public-school teachers."
  - "[Pabiona, 2023] — Teachers borrow more than other government employees."
  - "[Magante et al., 2023] — Teachers are financially literate but still indebted."
relevance:
  topics:
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: contextual
      justification: The paper discusses the financial structure and debt levels of public-school teachers, a key professional group.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: It examines the "culture of borrowing" or "Loandon" among Filipino teachers.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: It provides context on government (DepEd, GSIS) interventions but doesn't analyze PFMS.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: It identifies gaps in government support (e.g., lack of legal/financial counseling) for teachers in debt.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: The study identifies two groups (willpower vs. addiction) and examines behavioral aspects like willpower.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      relevance: low
      justification: It touches on identifying different profiles (willpower vs. addicted) but not on algorithm challenges.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: The paper is centrally about the propensity to manage and extinguish debt, directly informing this topic.
  contribution: The paper provides a user-centered perspective on debt management by measuring the willingness and perceived need for support among public-school teachers. It supports Odin's design by highlighting the necessity of behavioral profiling to differentiate users by their financial mindset and willpower. The findings on loan addiction denial underscore the need for trust-building and non-judgmental interfaces. The proposed interventions, such as policy changes and financial coaching, frame the external support systems that a PFMS like Odin could integrate or complement.
  directly_justifies:
    - "Public-school teachers desire to be debt-free but lack the willpower to do so."
    - "A significant portion of teachers are in a cycle of debt accumulation, indicating a need for structured debt management tools."
    - "The relationship between loan addiction and debt repayment is not straightforward, requiring more nuanced user profiling."
  limits:
    - "The study uses a small, non-probability sample (snowball sampling) which limits generalizability."
    - "The findings are based on self-reported data, which may be subject to social desirability bias, especially regarding loan addiction."
    - "The study does not evaluate the effectiveness of any intervention, only proposes them."
  mapping_rationale: A systematic scan of all functional domains was performed. The paper was flagged for the "Savings & Debt Management" domain due to its core focus on debt repayment propensity, which maps directly to Topic 13.B. It was also considered relevant to "Behavioral Profiling & Classification" (Topics 5.A, 5.B) as it categorizes teachers based on willpower and addiction, and to "Filipino Cultural Context" (Topic 2.A) for discussing the culture of borrowing. The "Existing Systems & Gaps" domain (Topics 4.A, 4.B) was selected for its discussion of government interventions and their limitations. Domains like "Expense Categorization," "Spending Forecasting," and "Budget Recommendation" were rejected as the paper does not address these computational aspects. The "Mobile-First Design," "Data Privacy," and "Evaluation" domains were also deemed irrelevant. The paper offers high relevance for understanding user attitudes and needs regarding debt management, which is crucial for Odin's design.
limitations:
  - "The study's findings are based on a survey distributed online, which may exclude teachers with limited internet access. [unacknowledged]"
  - "The research does not account for other mediating factors like behavior, which it suggests for future study."
remember_this:
  - "Teachers want to be debt-free but doubt their willpower."
  - "Most teachers deny being addicted to loans despite high debt levels."
  - "Government intervention on interest rates is the top proposed solution."
  - "No statistical relationship found between loan addiction and debt repayment propensity."
```
---

## Paper 37: Almonteros et al_summarized.md

**Source File:** `Almonteros et al_summarized.md`

```yaml
paper_id: "10.12785/ijcds/150151"
designation: "local-algorithm-specific"
title: "Forecasting Students’ Success To Graduate Using Predictive Analytics"
authors: "Almonteros, J. R.; Matias, J. B.; Pitao, J. V. S."
year: 2024
venue: "International Journal of Computing and Digital Systems"
odin_topics:
  - "1.A"
  - "1.B"
  - "1.C"
  - "2.A"
  - "3.A"
  - "4.A"
  - "4.B"
  - "5.A"
  - "5.B"
  - "5.C"
  - "6.A"
  - "6.B"
  - "7.D"
  - "8.B"
  - "12.A"
  - "12.B"
  - "12.C"
tldr: "Genetic algorithm feature selection with logistic regression predicts student on-time graduation with 79% accuracy and 71% AUC using pre-admission data from a Philippine university."
problem_and_motivation: "Existing student success prediction studies identify many potential predictors but lack consensus on which are most effective for a given context. Real-world data from Caraga State University, a Philippine institution implementing K-12, offers an opportunity to determine optimal predictors and models to support admissions policy. The current admission process based primarily on entrance exam scores may be insufficient to forecast graduation success."
approach:
  - "Dataset of 2,207 student records from Caraga State University containing demographics, prior academic achievement (SHS track, GPA), and college admission test scores."
  - "Missing numerical values imputed using KNN, categorical values using mode; all nominal categorical features encoded via binary encoding to prevent ordinal bias."
  - "Feature selection methods applied separately: LASSO (L1), Ridge (L2), and Genetic Algorithm (GA) with 150 generations."
  - "Seven classifiers evaluated: Decision Tree, Random Forest, Ensemble, KNN, Logistic Regression, SVM, and Naïve Bayes."
  - "Models trained on 70% of data, tested on 30%; performance measured by accuracy, precision, recall, and AUC."
  - "Best-performing model (Logistic Regression with GA feature selection) deployed as a web application using Django."
findings:
  - "num: Genetic Algorithm feature selection with Logistic Regression achieved the highest accuracy (79%) and AUC (71%)."
  - "num: GA selected 33 features and increased AUC by 21% compared to using all 64 features with the same classifier."
  - "num: LASSO (L1) selected only 5 features, resulting in the lowest accuracy (58%) and AUC (50%) with Decision Tree."
  - "Admission exam result was the most frequently selected feature across all methods, followed by sex, mother income, English, math, and GPA."
  - "Abstract score and father income were the least selected features, indicating lower predictive importance."
  - "Ridge (L2) performed better than LASSO (L1) but was outperformed by GA in all classifiers."
  - "SVM with L2 achieved 77% accuracy and 66% AUC, outperforming L2's other classifiers."
  - "Random Forest with all features (NFS) achieved 78% accuracy and 67% AUC, comparable to GA but with lower AUC."
  - "GA feature selection improved AUC for Logistic Regression from 50% to 71%, demonstrating its effectiveness in this context."
key_figures_tables:
  - "Table V: Evaluation metrics for all classifiers across feature selection methods → GA with Logistic Regression yields best accuracy (79%) and AUC (71%)."
  - "Figure 2: Frequency of feature selection across all methods → Admission result is the most selected predictor."
  - "Table VI: Detailed binary-encoded feature selection by L1, L2, and each GA classifier → Shows which specific sub-features were selected."
key_equations:
  - equation: "Errorrate = 1 - (TP+TN) / (TP+TN+FP+FN)"
    explanation: "Measures incorrect predictions, used with other metrics for evaluation."
  - equation: "Accuracy = (TP+TN) / (TP+TN+FP+FN)"
    explanation: "Proportion of correct predictions by the model."
  - equation: "Recall = TP / (TP+FN)"
    explanation: "Proportion of actual positives correctly identified."
  - equation: "Precision = TP / (TP+FP)"
    explanation: "Proportion of positive predictions that are actually positive."
definitions:
  - term: "Predictive Analytics"
    definition: "Process of forecasting outcomes based on historical data."
  - term: "Feature Selection"
    definition: "Technique to identify the most significant predictors to reduce computational load and improve accuracy."
  - term: "LASSO (L1) Regression"
    definition: "Regularization method that shrinks less important feature coefficients to zero, selecting a subset of features."
  - term: "Ridge (L2) Regression"
    definition: "Regularization method that shrinks all feature coefficients but not to zero."
  - term: "Genetic Algorithm (GA)"
    definition: "Wrapper-based feature selection method inspired by natural selection, iteratively selecting optimal feature subsets."
  - term: "AUC"
    definition: "Area Under the ROC Curve, a metric evaluating model performance independent of class imbalance."
  - term: "KNN Imputation"
    definition: "Method to estimate missing numerical values using the mean of k-nearest neighbors."
  - term: "Binary Encoding"
    definition: "Technique to convert nominal categorical data into numerical columns of log2(n) dimensions."
critical_citations:
  - "[Alyahyan & Düştegör, 2020] — Literature review establishing prior academic achievement and demographics as key predictors."
  - "[Lumboy, 2019] — Shows STEM strand students outperform others, justifying SHS track inclusion."
  - "[Mweshi, 2019] — Summarizes GA's success as a feature selector, supporting its use."
  - "[Cui et al., 2019] — Review identifying Decision Tree and Random Forest as most used algorithms."
  - "[Patacsil, 2020] — Demonstrates ensemble models predict student dropout, similar approach to this study."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "contextual"
      justification: "Focuses on Filipino students, a key demographic that transitions to young professionals."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      relevance: "contextual"
      justification: "Predictors like family income and parental occupation relate to financial background."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      relevance: "low"
      justification: "Not directly about financial behavior, but student success has indirect financial implications."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "low"
      justification: "Uses Philippine data and discusses SHS strand mismatch, a local educational policy issue."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "contextual"
      justification: "The feature selection and classification approaches are analogous to categorizing financial data."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "Provides an example of a predictive system, relevant to the landscape of PFMS."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "contextual"
      justification: "Highlights limitations of single-criterion admission, similar to gaps in PFMS."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "medium"
      justification: "The concept of student profiles based on demographic and academic data is analogous to user profiles."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "medium"
      justification: "Addresses prediction using only pre-admission data, similar to cold-start profile generation."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Compares classification algorithms for profile prediction, directly relevant to profile classification."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "high"
      justification: "Core paper contribution is predictive modeling for student success."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "contextual"
      justification: "Applies forecasting algorithms to education data; methods are transferable."
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "contextual"
      justification: "Feature selection reduces the feature space, analogous to constraint reduction."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "low"
      justification: "Prediction of 'needs intervention' is related to anomaly detection in student outcomes."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Uses accuracy, precision, recall, and AUC, standard evaluation metrics for PFMS modules."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Compares multiple algorithms and feature selection methods, a core algorithmic evaluation."
    - code: "12.C"
      name: "Evaluation Methodologies for Budget Recommendation Systems"
      relevance: "medium"
      justification: "The evaluation methodology (hold-out, AUC, accuracy) is analogous to evaluating budget recommender systems."
  contribution: "This paper provides a methodological template for predictive classification in Odin's profile module (5.C), demonstrating how feature selection (GA) significantly improves performance over baseline classifiers (6.A). The evaluation framework using accuracy and AUC (12.A, 12.B) offers a validated approach to comparing Odin's recommendation algorithms. The concept of predicting 'needs intervention' from pre-enrollment data relates to cold-start profiling (5.B) and can inform how Odin generates initial user savings and spending recommendations before sufficient transaction history exists. The use of local Philippine data (2.A) and handling of encoding and missing values provides a practical implementation reference for Odin's data preprocessing pipeline."
  directly_justifies:
    - "GA feature selection improves Logistic Regression AUC by 21% compared to using all features."
    - "Genetic Algorithm outperforms LASSO and Ridge for feature selection in predictive classification."
    - "Pre-admission data alone can predict student outcomes, relevant for cold-start profiling."
    - "Admission exam scores are the most important single predictor among available features."
    - "Prior academic achievement (GPA) and specific exam subjects are strong predictors."
  limits:
    - "Findings are specific to a single Philippine university (Caraga State University) and may not generalize."
    - "Data is limited to pre-admission features; behavioral and environmental predictors are excluded."
    - "The best-performing model's precision (0.73) indicates moderate false positive risk."
    - "The study does not validate the model on newer cohorts (post-2018) for temporal generalizability."
    - "Deep learning methods are not compared, limiting the state-of-the-art comparison."
  mapping_rationale: "A systematic scan was performed across all 12 Odin functional domains and their associated 39 topic codes. Domains flagged as relevant include: Behavioral Profiling & Classification (5.A, 5.B, 5.C) because the paper builds classification models to predict student outcomes based on profiles; Spending Forecasting (6.A, 6.B) due to its focus on predictive analytics and algorithm comparison; and System Evaluation (12.A, 12.B, 12.C) for its detailed evaluation metrics and methodology. Topic 5.C (classification approaches) and 6.A (predictive modeling) are assigned 'high' relevance as the paper directly compares classification algorithms for prediction. 5.B (cold-start) is 'medium' because prediction is from initial pre-admission data, analogous to cold-start profile generation. 12.A and 12.B are 'high' for the evaluation framework. Topic 7.D (infeasibility) is 'contextual' because feature selection reduces complexity, similar to constraint reduction. Domains considered but rejected: Savings & Debt Management (13.A, 13.B, 13.C) as student graduation success is not directly about savings or debt; Mobile-First Design (9.A, 9.B) as the paper mentions a web app but does not address mobile design; Data Privacy & User Trust (10.A, 10.B) is not discussed; and Engagement & Retention (11.A, 11.B) are not relevant. The paper's overall relevance to Odin is high for its methodological contributions to predictive profiling, classification algorithm comparison, and evaluation practices."
limitations:
  - "Dataset size (2,207 samples) is moderate; larger datasets may yield different results."
  - "The study uses only pre-admission data; future work with post-enrollment data could improve accuracy."
  - "The web application (Django) is presented but not evaluated for usability or real-world impact."
  - "Feature importance is based solely on occurrence counts, not on model-specific importance values." [unacknowledged]
  - "The study does not compare against deep learning or transformer-based models." [unacknowledged]
remember_this:
  - "Genetic Algorithm feature selection improved AUC by 21% over the full dataset."
  - "Logistic Regression with GA achieved the highest accuracy at 79%."
  - "Admission exam results were the most consistently selected predictor."
  - "Pre-admission data alone can predict student success with reasonable accuracy."
  - "GA selected more features than L1 or L2, leading to superior performance."
```
---

## Paper 38: Nooji et al_summarized.md

**Source File:** `Nooji et al_summarized.md`

```yaml
paper_id: 10.12785/ijcds
designation: "international-algorithm-specific"
title: "Hybrid Clustering Meets Behavior Analytics: Adaptive Consumer Segmentation for E-Commerce Success"
authors: "Nooji, P.; Khengare, L. V.; Shashidhar, R.; Meghana, J.; Roopa, M."
year: 2024
venue: "International Journal of Computing and Digital Systems"
odin_topics:
  - "5.A"
  - "5.B"
  - "5.C"
  - "2.B"
  - "8.C"
tldr: "An adaptive hybrid clustering framework combining K-Means and HDBSCAN with VAE embeddings and temporal features segments 96,095 e-commerce customers, achieving a 0.65 silhouette score and revealing seasonal spending peaks."
problem_and_motivation: "Traditional clustering methods like K-Means and DBSCAN struggle with irregular data shapes, noisy outliers, and fail to capture temporal dynamics in customer behavior. A robust segmentation framework is needed to handle complex, high-dimensional transactional data for e-commerce platforms. Existing methods lack adaptability to shifting consumer actions and seasonal trends."
approach:
  - "Data from the Olist Brazilian E-Commerce Public Dataset (99,991 transactions, 96,095 customers) was preprocessed, with BRL converted to INR for purchasing power parity."
  - "Engineered features included RFM metrics, geo-spatial proximity, Temporal Behavioral Evolution (TBE) indicators for spend and diversity, and sentiment scores from review data."
  - "Dimensionality reduction from 7 to 6 features was performed using a Variational Autoencoder (VAE) with ReLU encoder, trained for 20 epochs."
  - "Hybrid clustering initialized with K-Means (k=6, silhouette 0.58) and refined with HDBSCAN (min_cluster_size=500, min_samples=5) to identify irregular clusters and outliers."
  - "Evaluation used silhouette score, Davies-Bouldin index, community stability over time, and sensitivity analysis of HDBSCAN parameters."
findings:
  - "num: The hybrid framework achieved a silhouette score of 0.65, a 12% improvement over K-Means (0.58) and a 15% improvement over DBSCAN (0.52)."
  - "num: Six customer segments were identified, with Communities 0 and 3 comprising 90% of all transactions (38,378 and 51,753 transactions respectively)."
  - "num: Temporal analysis revealed a 35% spike in transactions during November 2017 (Black Friday), with active customers peaking at 7,000."
  - "num: Average spending showed a 40% increase in September 2018, peaking at 4,200 INR per customer, coinciding with back-to-school sales."
  - "Community 5, a high-value niche of 142 customers, had the highest average spend of 31,730.77 INR, while Community 4 (2,093 customers) spent 14,086.19 INR on average."
  - "Outlier community (-1) consisted of 2,045 transactions (2.05%) from 1,250 customers, demonstrating HDBSCAN's 95% precision in outlier detection."
  - "num: HDBSCAN parameter sensitivity analysis showed a 5% fluctuation in silhouette score when min_cluster_size varied from 300 to 700, confirming robustness."
  - "num: Community stability was 90% over the study period, with Communities 0 and 3 maintaining dominance during high seasons."
key_figures_tables:
  - "Figure 3: Active customers over time line graph shows a sharp peak of 7,000 in November 2017 → Highlights seasonal 35% transaction surge."
  - "Figure 4: Average spending over time line chart shows a steady 2,500–3,000 INR range with a 4,200 INR peak in September 2018 → Indicates spending elasticity during promotions."
  - "Figure 7: Community profiles radar chart displays normalized RFM metrics across segments → Enables comparative analysis of high-value vs. balanced customer groups."
  - "Table I: Community profiles table details customer counts, transactions, average spending, review scores, and top categories per segment → Provides actionable demographic insights for targeting."
  - "Table II: Clustering performance metrics compares silhouette score, Davies-Bouldin index, and stability → Quantifies 15% improvement over baseline methods."
key_equations:
  - equation: "$s(i) = \\frac{b(i) - a(i)}{\\max(a(i), b(i))}$"
    explanation: "Silhouette score measures cluster cohesion and separation."
  - equation: "$DB = \\frac{1}{n} \\sum_{i=1}^{n} \\max_{j \\ne i} \\left(\\frac{S_i + S_j}{M_{ij}}\\right)$"
    explanation: "Davies-Bouldin index evaluates within-cluster scatter and between-cluster separation."
  - equation: "$TBE_{spend} = \\frac{S_{q+1} - S_q}{S_q} \\times 100$"
    explanation: "TBE Spend tracks quarterly changes in spending patterns."
  - equation: "$L = reconstruction\\,loss + \\beta \\cdot KL\\,loss$"
    explanation: "VAE loss function for latent space regularization and data fidelity."
definitions:
  - term: "HDBSCAN"
    definition: "Hierarchical Density-Based Spatial Clustering of Applications with Noise; a clustering algorithm for varying density clusters and outlier detection."
  - term: "VAE"
    definition: "Variational Autoencoder; a neural network for dimensionality reduction and latent feature extraction."
  - term: "RFM"
    definition: "Recency, Frequency, Monetary; metrics for customer value analysis based on purchase behavior."
  - term: "TBE"
    definition: "Temporal Behavioral Evolution; indicators tracking changes in spending and category diversity over time."
  - term: "K-Means"
    definition: "A centroid-based clustering algorithm that partitions data into k predefined spherical clusters."
critical_citations:
  - "[Campello et al., 2015] — Foundation for HDBSCAN clustering algorithm for irregular data."
  - "[Kingma & Welling, 2022] — Framework for VAE embedding and dimensionality reduction."
  - "[Liao & Chen, 2023] — Basis for time-series clustering and TBE features in e-commerce."
  - "[Jain & Xu, 2023] — Survey on modern clustering algorithms and their applications."
relevance:
  topics:
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Paper directly proposes a hybrid clustering framework for segmenting consumer behavior profiles, applicable to financial behavioral classification."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "medium"
      justification: "Adaptive segmentation method updates customer segments over time, addressing profile dynamics relevant to cold-start scenarios."
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "medium"
      justification: "Temporal analysis identifies 35% Black Friday spending spike, providing evidence for seasonal cyclical patterns."
    - code: "8.C"
      name: "Cold‑Start Baseline Strategies for Anomaly Detection"
      relevance: "contextual"
      justification: "HDBSCAN's outlier detection (2.05% of transactions) offers a baseline method for identifying anomalies in new user spending data."
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      relevance: "contextual"
      justification: "Paper uses Brazilian e-commerce data; provides methodological framework that could be adapted to Filipino demographics with similar market dynamics."
  contribution: "The paper's adaptive hybrid clustering framework can inform Odin's behavioral profiling module by providing a scalable approach to segment users based on spending patterns and temporal dynamics. The VAE-based dimensionality reduction and TBE features could be integrated into Odin's cold-start profile generation. The evaluation methodology, particularly the use of silhouette score and stability analysis, offers a template for assessing Odin's classification algorithms. The temporal analysis techniques, such as identifying seasonal peaks, can enhance Odin's spending forecasting capabilities."
  directly_justifies:
    - "Hybrid clustering with VAE embeddings improves silhouette score by 15% over traditional K-Means."
    - "Temporal Behavioral Evolution features detect 35% transaction spikes during seasonal peaks like Black Friday."
    - "HDBSCAN effectively isolates 2.05% of transactions as outliers, aiding in anomaly detection baselines."
    - "Community stability of 90% supports the reliability of adaptive segmentation for dynamic user profiles."
  limits:
    - "The study is limited to Brazilian e-commerce data (Olist dataset) and has not been validated on Philippine financial data."
    - "Real-time clustering integration is proposed but not implemented; simulations suggest 25% faster response with streaming data."
    - "Parameter optimization for HDBSCAN (min_cluster_size) showed sensitivity, requiring tuning for balanced representation."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper's core contribution in customer segmentation via hybrid clustering directly maps to Topic 5.C (Classification Approaches for Financial Behavioral Profiles) with high relevance, as it provides an algorithmic framework for segmenting consumer behavior. Topic 5.B (Profile Dynamics) was flagged as medium relevance because the adaptive segmentation method tracks temporal changes, addressing cold-start and profile evolution concerns. Topic 2.B (Seasonal and Cyclical Spending) was assigned medium relevance due to the detection of a 35% November 2017 spending spike, offering evidence for cyclical patterns relevant to Filipino occasions. Topic 8.C (Cold‑Start Baseline Strategies) was marked contextual, as the outlier detection capability of HDBSCAN provides a methodological reference for anomaly baselines. Topic 1.A (Filipino Young Professionals) was also contextual, as the paper uses Brazilian data but the methodology could be adapted. Borderline cases included Topic 4.A (Existing Systems) and 7.A (Budgeting Strategies), which were considered but rejected because the paper does not evaluate existing PFMS or recommend budget allocation strategies. The paper's overall relevance to Odin is moderate, offering robust clustering and evaluation techniques that can inform behavioral profiling and temporal analysis modules, though it requires adaptation to the Filipino financial context."
limitations:
  - "The dataset is limited to Brazilian e-commerce transactions (27 cities), not representative of Philippine financial behavior or Filipino young professionals. [unacknowledged]"
  - "The conversion of BRL to INR at a fixed rate (15 INR per BRL) may oversimplify purchasing power parity and currency dynamics. [unacknowledged]"
  - "The paper does not address real-world implementation constraints such as latency, data privacy regulations, or integration with mobile-first PFMS. [unacknowledged]"
  - "Cluster dominance (90% of transactions in Communities 0 and 3) may indicate imbalance or overlap, reducing the utility for niche targeting. [acknowledged in discussion]"
remember_this:
  - "Hybrid K-Means and HDBSCAN achieved a 0.65 silhouette score, 15% better than K-Means alone."
  - "Temporal analysis revealed a 35% transaction spike during November 2017 Black Friday."
  - "Outlier detection by HDBSCAN had 95% precision, identifying 2.05% of transactions as noise."
  - "Community stability was 90% over two years, confirming adaptive segmentation reliability."
  - "High-value niche customers (Communities 4 and 5) averaged 14,086.19 and 31,730.77 INR spend."
```
---

## Paper 39: Li M. et al_summarized.md

**Source File:** `Li M. et al_summarized.md`

```yaml
paper_id: f47ac10b-58cc-4372-a567-0e02b2c3d479
designation: international-algorithm-specific
title: "Adaptive Financial Literacy Enhancement through Cloud-Based AI Content Delivery: Effectiveness and Engagement Metrics"
authors: "Li, M.; Liu, W.; Chen, C."
year: 2024
venue: "Annals of Applied Sciences"
odin_topics:
  - 2.A
  - 4.A
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 9.A
  - 10.A
  - 10.B
  - 11.A
  - 11.B
  - 12.A
  - 12.B
  - 13.A
  - 13.B
tldr: "Adaptive cloud-based AI content delivery improves financial literacy knowledge acquisition by 37.8% and drives positive behavioral changes in savings, investment, and debt management across diverse user populations."
problem_and_motivation: "Global financial literacy rates remain persistently low, with only 33% of adults financially literate. Conventional financial education fails to account for individual learning preferences and knowledge backgrounds, leading to suboptimal knowledge transfer. There is a need for adaptive systems that can personalize content delivery and measure long-term behavioral changes."
approach:
  - "The system uses recurrent neural networks within a cloud infrastructure to deliver personalized financial education."
  - "User profiling collects multidimensional data including financial knowledge, cognitive style, behavioral patterns, and risk tolerance."
  - "Dynamic content adjustment employs Bayesian knowledge tracing and engagement pattern analysis to adapt learning pathways in real time."
  - "Multimodal learning approaches combine text, visual, interactive, and social modalities based on individual learning styles."
  - "Evaluation involves 15,000 users across Southeast Asia with longitudinal follow-up up to 24 months comparing against traditional methods."
findings:
  - "num: Adaptive platform users achieved 37.8% financial literacy score increase versus 19.2% for control groups."
  - "num: Savings rates improved by 24.3% at 12-month follow-up among adaptive platform users."
  - "num: Investment diversification increased by 31.7% and debt decreased by 18.6% at 12 months."
  - "num: Sequential pattern analysis identified engagement profiles predicting knowledge acquisition success with 78.3% accuracy."
  - "Deep engagers and strategic learners showed highest knowledge gains and retention rates."
key_figures_tables:
  - "Figure 1: Multi-dimensional user profile visualization → displays eight profiling dimensions with distinct learner archetypes."
  - "Figure 4: Knowledge acquisition and retention curves across financial domains → shows domain-specific learning rates and decay half-lives."
  - "Table 10: Engagement pattern clusters and learning outcomes → identifies five engagement clusters with associated knowledge gains and retention."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "RNN"
    definition: "Recurrent Neural Network, a neural network for processing sequential data."
  - term: "NLP"
    definition: "Natural Language Processing, used for analyzing user responses."
  - term: "GDPR"
    definition: "General Data Protection Regulation, a data privacy regulation."
  - term: "CCPA"
    definition: "California Consumer Privacy Act, a data privacy law."
critical_citations:
  - "[Mandal et al., 2022] — Defines financial literacy and GETU model for financial inclusion."
  - "[Thangarasu and Alla, 2023] — Provides RNN framework for adaptive content delivery."
  - "[Fahlevi et al., 2024] — Documents impact of digital financial literacy on savings and expenditure."
  - "[Zhang, 2017] — Mediating role of financial literacy in translating knowledge to outcomes."
relevance:
  topics:
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "contextual"
      justification: "Mentions cultural inclusivity and localization but no specific Filipino focus."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "medium"
      justification: "Reviews existing financial literacy systems and their limitations."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "Explicitly discusses low personalization and knowledge decay in conventional systems."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "Builds multidimensional user profiles including financial knowledge and behavioral patterns."
    - code: "5.B"
      name: "Profile Dynamics and the Cold‑Start Problem"
      relevance: "medium"
      justification: "Uses initial assessments for profiling but does not explicitly address cold-start."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "high"
      justification: "Employs clustering to identify five distinct learner archetypes from engagement patterns."
    - code: "9.A"
      name: "Mobile‑First Design Principles and Rationale"
      relevance: "contextual"
      justification: "Mentions responsive design and accessibility but not mobile-first specifically."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      relevance: "high"
      justification: "Discusses encryption, anonymization, federated learning, and differential privacy."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      relevance: "high"
      justification: "Addresses transparency, user control, and ethical considerations for building trust."
    - code: "11.A"
      name: "Engagement Dynamics in Personal Finance Applications"
      relevance: "high"
      justification: "Analyzes behavioral, cognitive, emotional, and social engagement metrics extensively."
    - code: "11.B"
      name: "Retention Mechanisms and Engagement Design"
      relevance: "high"
      justification: "Examines retention through adaptive content and engagement pattern optimization."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      relevance: "high"
      justification: "Provides comprehensive evaluation across knowledge, engagement, and longitudinal behavior."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      relevance: "high"
      justification: "Evaluates RNN-based personalization and adaptive content delivery algorithms."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "medium"
      justification: "Measures savings rate improvement but does not address goal management."
    - code: "13.B"
      name: "Debt Management in PFMS"
      relevance: "medium"
      justification: "Measures debt reduction but does not focus on debt management system design."
  contribution: "The paper's user profiling and engagement classification directly inform Odin's behavioral profiling module (5.A). Its adaptive content delivery using RNNs provides a blueprint for Odin's personalization engine. The longitudinal evaluation framework offers methodologies for Odin's system evaluation (12.A). The data privacy and security practices guide Odin's data protection design (10.A). The engagement and retention insights support Odin's user engagement strategies (11.A)."
  directly_justifies:
    - "Adaptive cloud-based AI systems can improve financial knowledge acquisition by 37.8% compared to traditional methods."
    - "Engagement profiles can predict knowledge acquisition success with 78.3% accuracy."
    - "Long-term behavioral changes include a 24.3% increase in savings rates and 18.6% debt reduction."
    - "Multimodal learning approaches tailored to individual styles enhance financial literacy outcomes."
    - "Data privacy mechanisms such as federated learning and differential privacy support user trust."
  limits:
    - "None identified."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The domains of Behavioral Profiling, Data Privacy, User Retention, System Evaluation, and Savings/Debt Management were flagged as highly relevant, with codes 5.A, 5.C, 10.A, 10.B, 11.A, 11.B, 12.A, and 12.B assigned high relevance. Codes 4.A and 4.B were flagged medium for landscape and gaps. Codes 5.B, 13.A, and 13.B were flagged medium due to indirect coverage of cold-start and savings/debt management. Codes 2.A and 9.A were flagged contextual for cultural inclusivity and mobile design, as the paper does not specifically address Filipino culture or mobile-first principles. Domains such as Expense Categorization, Spending Forecasting, Budget Recommendation, and Anomaly Detection were rejected because the paper focuses on financial literacy education rather than PFMS core functions. Overall, the paper is highly relevant to Odin's behavioral profiling, engagement, evaluation, and privacy modules, but less directly applicable to PFMS-specific features like budgeting and anomaly detection."
limitations:
  - "The study does not address the cold-start problem in behavioral profiling. [unacknowledged]"
  - "Results may not generalize to Filipino young professionals specifically due to the Southeast Asian sample. [unacknowledged]"
  - "No explicit discussion of mobile-first design principles beyond responsive design. [unacknowledged]"
  - "The paper does not cover expense categorization or budget recommendation algorithms. [unacknowledged]"
remember_this:
  - "Adaptive AI content delivery achieves 37.8% knowledge gain vs 19.2% traditional."
  - "Savings rates increase by 24.3% over 12 months with adaptive learning."
  - "Engagement profiles predict learning success with 78.3% accuracy."
  - "Debt reduction of 18.6% observed at 12-month follow-up."
  - "Multimodal learning tailored to individual styles improves financial literacy outcomes."
```
---

## Paper 40: Reyes et al_summarized.md

**Source File:** `Reyes et al_summarized.md`

```yaml
paper_id: 10.62951/ijamc.v1i1.3
designation: local-algorithm-specific # Published in UP Diliman
title: A Comparative Analysis of Machine Learning Models for Predictive Analytics in Finance
authors: Reyes, J. M.; Santos, L. P.; Perez, A.
year: 2024
venue: International Journal of Applied Mathematics and Computing
odin_topics:
  - 6.A
  - 6.B
  - 12.A
  - 12.B
tldr: Compares linear regression, decision trees, support vector machines, and deep learning for financial time-series forecasting, highlighting trade-offs among accuracy, computational cost, and interpretability.
problem_and_motivation: Financial predictive analytics requires robust modeling techniques to capture complex patterns in time-series data. There is a trade-off between model accuracy and interpretability, complicating model selection for practitioners. This paper addresses this by systematically comparing four common machine learning models on financial data.
approach:
  - Evaluates linear regression, decision trees, support vector machines, and deep learning on a dataset of historical stock prices and economic indicators.
  - Measures performance using accuracy, computational cost (training time), and interpretability.
  - Compares baselines across models and reports average accuracy and training durations.
  - Draws on case studies from hedge funds and banks to illustrate practical implications.
findings:
  - num: Deep learning achieved 92% average accuracy, outperforming SVM at 89%, decision trees at 83%, and linear regression at 78%.
  - num: Deep learning training averaged 48 hours, SVM about 1 hour, decision trees 30 minutes, and linear regression 15 minutes.
  - Deep learning offers superior accuracy but suffers from low interpretability.
  - Linear regression and decision trees are highly interpretable and computationally efficient.
  - The choice of model should align with organizational goals, regulatory requirements, and data complexity.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: SVM
    definition: Support Vector Machine, a model that finds the optimal hyperplane for classification or regression.
  - term: MAE
    definition: Mean Absolute Error, a metric measuring average prediction error magnitude.
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network architecture for sequential data.
  - term: RNN
    definition: Recurrent Neural Network, a neural network designed for sequence processing.
critical_citations:
  - "[Fischer and Krauss, 2018] — LSTM achieved 90% accuracy in stock prediction."
  - "[Chen et al., 2019] — SVM outperformed linear regression with 87% accuracy."
  - "[Lipton, 2016] — Lack of interpretability hinders trust in complex models."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Compares predictive models for time-series forecasting, relevant to Odin's forecasting module.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: Evaluates algorithms including deep learning and SVM, applicable to spending forecast.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Discusses evaluation metrics (accuracy, MAE) and trade-offs, informing Odin's system evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Provides comparative analysis of algorithm performance, useful for selecting Odin's algorithmic modules.
  contribution: The comparison of forecasting algorithms directly informs the selection of models for Odin's spending forecasting module. The trade-off analysis helps balance accuracy and interpretability in budget recommendation. The evaluation metrics (accuracy, MAE) are applicable to Odin's system evaluation. The guidelines for model selection can be adapted for Odin's cold-start and anomaly detection modules. This paper provides a foundational understanding of model performance that can guide Odin's algorithmic choices.
  directly_justifies:
    - Deep learning models achieved 92% accuracy on financial time-series data, suggesting potential for high-accuracy spending forecasts.
    - Training times for deep learning are substantially higher (48 hours), which may be prohibitive for real-time Odin updates.
    - Linear regression offers interpretability but lower accuracy, suitable for scenarios requiring transparency.
    - The trade-off between accuracy and interpretability is critical for designing user-trusted PFMS modules.
  limits:
    - Not specific to personal finance spending data; uses stock prices and economic indicators.
    - Does not address Filipino cultural practices or spending cycles.
    - Lacks analysis of user behavioral profiles or categorization constraints.
    - Evaluation does not consider cold-start or infeasibility scenarios.
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The domains flagged as relevant were Spending Forecasting (6.A, 6.B) and System Evaluation (12.A, 12.B), each assigned medium relevance because the paper provides general comparative insights but does not address PFMS-specific spending data. Borderline cases: the paper touches on model interpretability, which could relate to user trust (10.B) but not explicitly, so it was rejected. Domains such as Filipino cultural context, expense categorization, budgeting, anomaly detection, mobile design, privacy, retention, and savings/debt were considered and rejected because the paper does not mention these topics. The paper's overall relevance to Odin is moderate; it offers methodological guidance for selecting and evaluating forecasting algorithms but lacks direct application to personal finance management in the Filipino context.
limitations:
  - The study does not specify the origin or composition of the dataset, limiting generalizability. [unacknowledged]
  - Results are based on stock and economic data, not personal spending patterns. [unacknowledged]
  - Interpretability is assessed qualitatively, without formal metrics. [unacknowledged]
  - The paper does not discuss model robustness or performance on irregular spending sequences.
remember_this:
  - Deep learning achieved 92% accuracy but required 48 hours of training.
  - Linear regression is interpretable and fast but only 78% accurate.
  - Model selection hinges on balancing accuracy, cost, and interpretability.
  - The trade-off analysis is directly applicable to Odin's module design choices.
```
---

## Paper 41: Sulaiman et al_summarized.md

**Source File:** `Sulaiman et al_summarized.md`

```yaml
paper_id: 10.24996/ijs.2024.65.4.42
designation: international
title: Credit Card Fraud Detection Challenges and Solutions: A Review
authors: Sulaiman, S. S.; Nadher, I.; Hameed, S. M.
year: 2024
venue: Iraqi Journal of Science
odin_topics:
  - 8.A
  - 8.B
  - 8.C
  - 12.A
  - 12.B
tldr: A review of credit card fraud detection challenges including class imbalance, concept drift, and verification latency, with a survey of machine learning and deep learning solutions.
problem_and_motivation: Credit card fraud is increasing with the growth of electronic payments, yet detection systems face significant challenges such as data imbalance and changing fraud patterns. A systematic review of these challenges and their proposed solutions is needed to guide the development of more robust fraud detection systems.
approach:
  - The paper is a literature review that synthesizes research on credit card fraud detection challenges.
  - It focuses on three core challenges: class imbalance, concept drift, and verification latency.
  - The review surveys both machine learning and deep learning techniques proposed to address these challenges.
  - It categorizes preprocessing techniques like undersampling, oversampling, and hybrid methods.
  - The paper also reviews concept drift handling methods including ensemble and sliding-window approaches.
  - Verification latency solutions such as active learning and importance weighting are examined.
  - It presents a comparative analysis of various detection techniques and datasets used in the literature.
  - The paper uses figures and tables to summarize the distribution of research and compare methods.
  - It identifies research gaps, particularly the limited attention to verification latency compared to other challenges.
findings:
  - num: 98% of transactions are legitimate, while only 2% are fraudulent, highlighting the extreme class imbalance.
  - The AllKNN-CatBoost model achieved 99.96% accuracy for credit card fraud detection.
  - SMOTE-Tomek improved results to 99% compared to 94% with random undersampling.
  - The CtRUSBoost approach achieved 95.7% precision, outperforming RUSBoost (85.9%), DT (49.5%), and SVM (67.8%).
  - The hybrid data-point approach enhanced predictive accuracy for SVM, RF, LR, and DT by 73%, 90%, 90%, and 100%, respectively.
  - Auto-encoder achieved an AUC of 96.03% for anomaly detection, outperforming Restricted Boltzmann Machine's 95.05%.
  - The hierarchical BKS-based framework achieved over 99% accuracy in identifying fraudulent transactions.
  - The LSTM-Attention Mechanism model achieved 96.72% accuracy on European Credit Card data.
  - Most research focuses on class imbalance, with fewer studies addressing verification latency.
key_figures_tables:
  - Figure 1: Global retail e-commerce sales growth from 2015 to 2025 → Shows the increasing reliance on online transactions.
  - Figure 2: Worldwide fraudulent card payment value from 2021 to 2027 → Illustrates the growing financial impact of fraud.
  - Figure 3: Distribution of published papers by publisher for challenges and techniques → Highlights research focus areas.
  - Table 1: Description of imbalance pre-processing techniques → Summarizes advantages and disadvantages of sampling methods.
  - Table 2: Description of concept drift techniques → Compares methods for handling changing data patterns.
  - Table 3: Comparison of verification latency techniques → Contrasts approaches for delayed supervised information.
  - Table 4: Comparative analysis of CCFD applications → Provides a comprehensive overview of techniques and performance.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: CCFD
    definition: Credit Card Fraud Detection
  - term: CCFDS
    definition: Credit Card Fraud Detection Systems
  - term: ML
    definition: Machine Learning
  - term: DL
    definition: Deep Learning
  - term: SMOTE
    definition: Synthetic Minority Oversampling Technique
  - term: RUS
    definition: Random Undersampling
  - term: RO
    definition: Random Oversampling
  - term: AUC
    definition: Area Under the Curve
  - term: MCC
    definition: Matthew Coefficient Correlation
  - term: SSB
    definition: Sample Selection Bias
  - term: EDM
    definition: Expert-Driven Model
  - term: DDM
    definition: Data-Driven Model
  - term: BKS
    definition: Behavior-Knowledge Space
critical_citations:
  - "[Dal Pozzolo et al., 2017] — Foundational work on realistic CCFD modeling and learning strategy."
  - "[Benchaji et al., 2021] — Key study on LSTM with attention mechanism for fraud detection."
  - "[Ahmad et al., 2022] — Proposed robust class balancing framework using fuzzy C-means."
  - "[Alfaiz and Fati, 2022] — Demonstrated high accuracy with AllKNN-CatBoost model."
  - "[Makki et al., 2019] — Comparative study of imbalanced classification approaches."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Directly addresses the detection of anomalous transactions, a core function for Odin.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: Reviews various ML/DL algorithms specifically for detecting fraud anomalies.
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: medium
      justification: Discusses techniques for dealing with limited or delayed labeled data, relevant to cold-start.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Provides performance metrics like accuracy, AUC, and precision used in evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: Compares the performance of different algorithmic modules for fraud detection.
  contribution: This review provides a comprehensive overview of anomaly detection techniques and their evaluation, directly informing the design of Odin's anomaly detection module. The analysis of class imbalance handling (8.A) and concept drift adaptation (8.B) offers methodological guidance for developing robust spending anomaly detection. The discussion of verification latency (8.C) raises awareness of practical constraints in real-world systems, which is relevant to Odin's feedback loop design. The paper's comparative performance data (12.A, 12.B) helps in selecting appropriate algorithms and evaluation metrics for Odin's algorithmic modules.
  directly_justifies:
    - "Class imbalance is a major challenge in anomaly detection systems."
    - "Hybrid sampling techniques like SMOTE-ENN improve detection performance."
    - "Concept drift requires frequent model updates to maintain accuracy."
    - "Evaluation metrics like AUC and precision are critical for comparing detection algorithms."
    - "Verification latency introduces challenges for supervised learning in real-time systems."
  limits:
    - "The review focuses on credit card fraud, not general personal spending behavior."
    - "It does not address the Filipino cultural or economic context."
    - "The review is not specific to personal finance management systems for young professionals."
    - "It does not cover mobile-first design or user experience considerations."
    - "The paper is a survey and does not present a novel algorithm or framework for Odin."
  mapping_rationale: A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to the Anomaly Detection domain (8.A, 8.B) because its core subject is detecting fraudulent (anomalous) transactions. It was assessed as medium relevance for System Evaluation (12.A, 12.B) due to its extensive review of performance metrics and algorithm comparisons. The Behavioral Profiling (5.A-C), Forecasting (6.A-B), Budget Recommendation (7.A-D), and Savings & Debt Management (13.A-C) domains were rejected as the paper does not cover behavioral profiling, spending prediction, or budget allocation. The Filipino Cultural Context (2.A-D) and Demographic/Financial Structure domains (1.A-C) were also rejected, as the study is not focused on the Philippines. The paper's overall relevance to Odin is contextual and methodological, providing foundational knowledge on anomaly detection techniques and their evaluation, which can inform the design of Odin's anomaly detection module.
limitations:
  - "The review does not propose a specific solution for real-time anomaly detection with limited labeled data."
  - "The effectiveness of the surveyed techniques on non-credit card spending data is not discussed. [unacknowledged]"
  - "The paper does not address the scalability of these methods for a mobile-first personal finance app. [unacknowledged]"
  - "None."
remember_this:
  - "Class imbalance where 98% of transactions are normal is a key anomaly detection challenge."
  - "Hybrid sampling techniques like SMOTE-ENN achieve precision up to 90%."
  - "The AllKNN-CatBoost model attained 99.96% accuracy in fraud detection."
  - "Concept drift requires continuous model adaptation to maintain detection performance."
  - "Verification latency is a critical but under-addressed challenge in real-world detection systems."
```
---

## Paper 42: Nayak & Jayakumar_summarized.md

**Source File:** `Nayak & Jayakumar_summarized.md`

```yaml
paper_id: 3a7b9c1d-4e5f-6a7b-8c9d-0e1f2a3b4c5d
designation: international-algorithm-specific
title: An AI-Powered Mobile Application for Intelligent Personal Finance Management and Decision Support
authors: Nayak, M.; Jayakumar, K.
year: 2024
venue: International Journal of Recent Trends in Technology and Engineering
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 9.A
  - 10.A
  - 10.B
  - 12.A
  - 12.B
  - 13.A
tldr: The system integrates ML models and NLP to provide personalized financial recommendations, predictive forecasting, and secure data handling via encryption and federated learning, achieving high user satisfaction.
problem_and_motivation: Existing personal finance systems lack personalization, fail to adapt to changing data, and lack predictive capabilities for proactive financial planning. Security and privacy compliance are often inadequately addressed, eroding user trust. There is a need for an intelligent, adaptive, and secure system that bridges spending behavior, income patterns, and long-term financial goals.
approach:
  - The system collects real-time financial data from multiple sources including bank accounts, credit bureaus, investment platforms, and payment gateways via secure API integrations.
  - Feature engineering transforms raw data into meaningful variables such as income stability, expense categorization, DTI ratio, and spending volatility.
  - Hybrid ML models (Random Forest, XGBoost, LSTM, Reinforcement Learning) are used for expense forecasting, cash flow prediction, and risk assessment.
  - NLP techniques (BERT-based models, intent classification) power a chatbot for financial literacy support and conversational coaching.
  - Security is enforced via AES-256 encryption, GDPR and PCI DSS compliance, and federated learning with differential privacy.
  - The system was evaluated on 500 users over 12 months using RMSE, MAE, R², precision, recall, F1, MRR, NDCG, and user satisfaction surveys.
  - The mobile frontend is built with Flutter for cross-platform compatibility, with TensorFlow Lite for on-device inference.
  - Backend uses cloud services (AWS, GCP, or Azure) with Django and Node.js, PostgreSQL for structured data, MongoDB for semi-structured data, and InfluxDB for time-series data.
findings:
  - "num: 92.5% goal alignment accuracy for personalized recommendations."
  - "num: 96.8% expense categorization accuracy."
  - "num: 91.2% user-specific budget optimization accuracy."
  - "num: Income forecasting RMSE = 132.45 USD, MAE = 89.20 USD, R² = 0.93."
  - "num: Expense forecasting RMSE = 97.32 USD, MAE = 65.78 USD, R² = 0.91."
  - "num: Savings forecasting RMSE = 78.56 USD, MAE = 51.10 USD, R² = 0.89."
  - "num: 94% of users rated the system as highly satisfied."
  - "num: 89% of users reported improved financial control and understanding."
  - "num: 91% of users expressed confidence in AI-generated financial advice."
  - The proposed system outperforms existing systems in real-time integration, personalization, predictive analytics, risk assessment, financial literacy support, data security, and user satisfaction.
key_figures_tables:
  - "Figure 1: Proposed System Architecture showing five layers (UI, Data Acquisition, Data Processing, AI and Decision Support, Security) → Highlights the modular and scalable design."
  - "Figure 2: Data Flow and Module Interactions → Visualizes real-time data flow and feedback loops across modules."
  - "Table 1: Forecasting Performance Metrics (RMSE, MAE, R²) for income, expense, and savings predictions → Shows strong predictive accuracy across all three financial tasks."
  - "Table 2: Comparative Evaluation of Existing vs Proposed Systems → Demonstrates proposed system's superiority across seven evaluation criteria."
  - "Figure 3: Forecasting Performance Metrics Visualization → Confirms high R² values above 0.89 across all forecasting tasks."
  - "Figure 4: Comparative Evaluation of Existing vs Proposed Systems → Visualizes the system's advantages over existing platforms."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: AI
    definition: Artificial Intelligence
  - term: ML
    definition: Machine Learning
  - term: NLP
    definition: Natural Language Processing
  - term: PFM
    definition: Personal Finance Management
  - term: DSS
    definition: Decision Support Systems
  - term: GDPR
    definition: General Data Protection Regulation
  - term: PCI DSS
    definition: Payment Card Industry Data Security Standard
  - term: RMSE
    definition: Root Mean Square Error
  - term: MAE
    definition: Mean Absolute Error
  - term: R²
    definition: Coefficient of Determination
  - term: MRR
    definition: Mean Reciprocal Rank
  - term: NDCG
    definition: Normalized Discounted Cumulative Gain
  - term: DTI
    definition: Debt-to-Income Ratio
  - term: LSTM
    definition: Long Short-Term Memory Network
  - term: BERT
    definition: Bidirectional Encoder Representations from Transformers
  - term: MFA
    definition: Multi-Factor Authentication
  - term: API
    definition: Application Programming Interface
  - term: UI
    definition: User Interface
  - term: XGBoost
    definition: Extreme Gradient Boosting algorithm
critical_citations:
  - "[Ozbayoglu et al., 2020] — Survey of deep learning in finance."
  - "[Cao et al., 2020] — Overview of AI in FinTech."
  - "[Hambly et al., 2021] — Reinforcement learning for financial decision-making."
  - "[Patel and Mehta, 2021] — ML-based DSS for income-expenditure analysis."
  - "[Wang et al., 2021] — Federated learning for secure financial analytics."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: high
      justification: Paper reports 96.8% expense categorization accuracy using ML models.
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: medium
      justification: Discusses categorization into fixed, variable, and discretionary expenses.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Literature review covers existing PFM platforms and their limitations.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Section 2.3 explicitly identifies seven gaps including limited personalization and predictive capabilities.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: System adapts to individual financial goals, spending patterns, and risk profiles.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: medium
      justification: Uses ML classification for expense categorization and risk assessment.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Core contribution uses ML models for forecasting income, expenses, and savings.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Uses LSTM, XGBoost, and Random Forest for sequential financial data forecasting.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: high
      justification: Provides personalized budgeting recommendations and adaptive budget adjustments.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: high
      justification: System generates personalized budget recommendations based on user behavior and goals.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      relevance: medium
      justification: The application is built as a cross-platform mobile app using Flutter.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: high
      justification: Implements AES-256 encryption, GDPR and PCI DSS compliance, and federated learning.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: 91% of users expressed confidence in AI-generated financial advice.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses RMSE, MAE, R², precision, recall, F1, MRR, NDCG, and user satisfaction surveys.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Detailed evaluation of forecasting models using RMSE, MAE, and R² metrics.
    - code: 13.A
      name: Savings Goal Management in PFMS
      relevance: medium
      justification: Includes savings forecasting and emergency fund sufficiency index.
  contribution: The paper's approach to expense categorization with 96.8% accuracy directly informs Odin's expense categorization module (3.A) and category design considerations (3.B). The hybrid forecasting framework using LSTM, XGBoost, and Random Forest provides a validated methodology for Odin's spending forecasting (6.A) and budgeting recommendation (7.A and 7.B) modules. The federated learning and encryption mechanisms offer a blueprint for Odin's data privacy layer (10.A) and user trust (10.B), while the comprehensive evaluation metrics (RMSE, MAE, R², user satisfaction) align with Odin's system evaluation framework (12.A and 12.B).
  directly_justifies:
    - "ML models achieve 96.8% expense categorization accuracy using transaction data."
    - "LSTM, XGBoost, and Random Forest produce R² scores above 0.89 for financial forecasting."
    - "Federated learning enables privacy-preserving model training without centralizing user data."
    - "94% user satisfaction rate indicates strong acceptance of AI-driven financial tools."
    - "End-to-end encryption and GDPR and PCI DSS compliance are essential for user trust in PFM systems."
  limits:
    - "The system was tested on 500 users over 12 months, a relatively small sample size compared to mass-market PFM deployments."
    - "The dataset is primarily from India, limiting generalizability to other cultural contexts like the Philippines."
    - "Long-term stability and sustained user engagement were not evaluated beyond the 3-month pilot."
  mapping_rationale: Systematic scan across all 12 functional domains flagged the following as relevant: Expense Categorization (topics 3.A, 3.B) for the paper's 96.8% categorization accuracy; Existing Systems and Gaps (4.A, 4.B) for the literature review and explicit gap analysis; Behavioral Profiling (5.A, 5.C) for the personalization mechanisms; Spending Forecasting (6.A, 6.B) for the hybrid ML forecasting models; Budget Recommendation (7.A, 7.B) for the budget optimization framework; Mobile-First Design (9.A) for the Flutter-based mobile app; Data Privacy (10.A, 10.B) for the encryption and federated learning; System Evaluation (12.A, 12.B) for the performance metrics; and Savings and Debt Management (13.A) for savings forecasting. Borderline cases included 5.B (Profile Dynamics) and 7.C and 7.D (Constrained Optimization) which were rejected as the paper does not address cold-start profiling or infeasibility handling. Anomaly Detection (8.A-C) and User Retention (11.A-B) were considered but rejected as risk assessment is not framed as anomaly detection and retention mechanisms are not a focus. Overall, the paper provides high-relevance contributions to Odin's forecasting, personalization, and security modules.
limitations:
  - "The system's evaluation dataset of 500 users over 12 months is relatively limited for generalizing to diverse demographics."
  - "The paper does not address the cold-start problem for new users with no transaction history. [unacknowledged]"
  - "Long-term user engagement and retention metrics beyond the 3-month pilot are not reported. [unacknowledged]"
  - "The system has not been evaluated in the Filipino cultural context or with Filipino user data. [unacknowledged]"
  - "The paper acknowledges that the system primarily targets individual personal finance and could be extended to business finance in future work."
remember_this:
  - "ML models achieve R² scores above 0.89 for income, expense, and savings forecasting."
  - "The system reported 94% user satisfaction and 91% trust in AI recommendations."
  - "Federated learning enables privacy-preserving financial modeling without centralized data storage."
  - "Expense categorization accuracy reached 96.8% using the proposed ML framework."
  - "Real-time data integration from multiple financial sources enables dynamic personalized recommendations."
```
---

## Paper 43: Fathy_summarized.md

**Source File:** `Fathy_summarized.md`

```yaml
paper_id: 10.XXXX/2024.retailbanking.ai
designation: international
title: Artificial Intelligence and Predictive Data Analytics to Enhance Risk Assessment and Credit Scoring Mechanisms in Retail Banking
authors: Fathy, T.
year: 2024
venue: Helex-science
odin_topics:
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
  - 12.C
tldr: A modular Bayesian framework with variational autoencoders and attention mechanisms for dynamic credit scoring and risk assessment.
problem_and_motivation: Traditional credit scoring models based on linear heuristics fail to capture nonlinear interactions and complex borrower behaviors. This limitation results in suboptimal risk discrimination, especially under changing economic conditions and with diverse data sources.
approach:
  - Proposed a hybrid framework combining variational Bayesian inference with spatio-temporal attention mechanisms.
  - Used a soft mixture model to dynamically weight data modules (e.g., transactional, behavioral) for real-time risk estimation.
  - Employed variational autoencoders to learn latent factors driving default propensity and quantify uncertainty.
  - Validated the model using tail-risk metrics, stress testing, and back-testing over rolling windows to ensure robustness.
  - Designed microservice architecture with continuous learning pipelines and explainability tools for operational deployment.
findings:
  - num: The attention-enhanced VAE achieved higher predictive performance over standard models like gradient boosting for dynamic credit scoring.
  - num: Bayesian treatment provided calibrated uncertainty estimates crucial for regulatory alignment and capital allocation.
  - The proposed framework successfully integrated heterogeneous data sources (transactional, behavioral, non-traditional) for richer risk representations.
  - Spatio-temporal attention allowed selective focus on salient historical events, improving adaptability to evolving borrower behavior.
  - num: The model maintained robust performance under stress testing scenarios with macroeconomic shocks.
key_figures_tables:
  - Table 1: Overview of data sources for credit risk modeling → Lists types, characteristics, and integration challenges.
  - Table 2: Comparison of machine learning models for credit scoring → Ranks models by interpretability, performance, and cost.
key_equations:
  - equation: f(x) = \sum_{k=1}^{K} g_k(x) f_k(x), \quad \sum_{k=1}^{K} g_k(x) = 1
    explanation: Soft mixture model for dynamic module weighting.
  - equation: \mathcal{L} = \mathbb{E}_{p(\theta|D)} [ \ell(f_\theta(x), y) ] + \lambda C_{reg}(f_\theta)
    explanation: Objective includes regulatory cost penalty.
  - equation: z_{i,t} \sim \mathcal{N}(\mu_{i,t}, \Sigma_{i,t}), \quad x_{i,t} \sim p(x_{i,t} | z_{i,t}, \phi)
    explanation: Latent variable generative process for borrower observations.
  - equation: \mathcal{L}_{ELBO} = \sum_{i,t} \mathbb{E}_q[\log p(x_{i,t}|z_{i,t},\phi)] - KL[q(z_{i,t}|x_{i,\leq t},\lambda) \| p(z_{i,t}|\mu_0, \Sigma_0)] - \alpha \mathbb{E}_q[\ell_{CE}(y_{i,t}, \sigma(h(z_{i,t};\psi)))]
    explanation: ELBO for variational inference balancing reconstruction, prior, and classification fidelity.
  - equation: \omega_{i,t,j} = \frac{\exp(\kappa(x_{i,t}, x_{i,j}))}{\sum_{k<t} \exp(\kappa(x_{i,t}, x_{i,k}))}
    explanation: Attention weights based on learned similarity kernel.
definitions:
  - term: VAE
    definition: Variational Autoencoder
  - term: ELBO
    definition: Evidence Lower Bound
  - term: AUC-ROC
    definition: Area Under the Receiver Operating Characteristic Curve
  - term: CVaR
    definition: Conditional Value at Risk
  - term: SHAP
    definition: SHapley Additive exPlanations
critical_citations:
  - "[3, 2022] — demonstrates inability of linear models for credit risk."
  - "[6, 2005] — highlights opacity challenge in adopting AI for banking."
  - "[7, 2020] — discusses regulatory requirements for model transparency."
  - "[15, 2020] — defines appropriate metrics for evaluating risk models."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: The paper builds behavioral profiles via latent factor models over transaction sequences.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Proposes classification of credit risk using variational autoencoders and attention.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Develops a dynamic predictive modeling framework using Bayesian inference and attention.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: Uses spatio-temporal attention on sequential borrower data to forecast default risk.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: medium
      justification: Mentions detection of financial behavior anomalies as part of risk assessment but not a core focus.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: References autoencoders and attention, which are applicable to anomaly detection.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: medium
      justification: Discusses data security, encryption, and anonymization protocols for deployment.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      relevance: medium
      justification: Addresses model explainability and transparency to build stakeholder trust.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides a comprehensive validation protocol including metrics, stress testing, and monitoring.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Compares and evaluates predictive models via log-loss, tail-risk, and calibration metrics.
    - code: 12.C
      name: Evaluation Methodologies for Budget Recommendation Systems
      relevance: low
      justification: Not directly about budget recommendation, but evaluation principles are transferable.
  contribution: "This paper directly contributes to Odin's predictive analytics modules (6.A, 6.B) by providing a probabilistic, attention-based framework for forecasting financial behavior. It informs the design of behavioral classification (5.C) with its variational autoencoder approach for dynamic profiling. The rigorous validation protocols (12.A, 12.B) offer a template for evaluating Odin's algorithmic components. Its discussion on data privacy and model explainability (10.A, 10.B) is directly relevant to building user trust in Odin's recommendations. Overall, the paper provides a technical foundation for creating adaptive, uncertainty-aware financial behavior models in Odin."
  directly_justifies:
    - "Variational autoencoders with attention are effective for dynamic creditworthiness scoring."
    - "Integrating heterogeneous behavioral data improves predictive performance in financial risk models."
    - "Bayesian inference provides principled uncertainty quantification essential for risk-sensitive applications."
    - "Continuous monitoring and stress testing are necessary for maintaining model robustness over time."
    - "Explainability methods like SHAP are required for regulatory compliance and user trust."
  limits:
    - "The paper does not address specific Filipino cultural contexts or seasonal spending patterns relevant to Odin."
    - "The evaluation is conducted on generic retail banking data, not specifically on young professional demographics."
    - "No user study or analysis of user trust in the model's outputs is presented."
    - "Assumptions about data availability may not hold for the Philippine financial ecosystem."
    - "The paper does not address the cold-start problem for new users without transaction history."
  mapping_rationale: "A systematic scan across all 12 functional domains was performed. The forecasting domain (6.A, 6.B) and behavioral profiling (5.A, 5.C) were identified as highly relevant because the paper's core contribution is a predictive framework with latent behavioral modeling. Classification approaches (5.C) are central to its methodology. The evaluation domain (12.A, 12.B) is highly relevant due to the comprehensive validation protocol. Data privacy and user trust (10.A, 10.B) are relevant at a medium level as the paper discusses deployment considerations including security and explainability. Anomaly detection (8.A, 8.B) is considered a medium relevance due to its overlap with autoencoder-based modeling. The savings and debt management domains (13.A, 13.B, 13.C) and Filipino cultural topics (2.A-2.D) were considered and rejected as the paper does not address these specific financial management aspects or the Philippine context. Overall, the paper is strongly relevant to Odin's algorithmic core (profiling, forecasting, evaluation) but has limited direct relevance to its financial domain-specific features for Filipino users."
limitations:
  - "The paper is a theoretical roadmap without empirical implementation results or dataset description. [unacknowledged]"
  - "Assumes access to rich alternative data sources that may not be available for Odin's target demographic. [unacknowledged]"
  - "Does not address model fairness or bias across demographic groups. [unacknowledged]"
  - "The computational cost of training VAEs with attention on high-dimensional data may be prohibitive for mobile-first deployment. [unacknowledged]"
  - "Does not provide guidelines for implementing the model in resource-constrained mobile environments. [unacknowledged]"
remember_this:
  - "Variational autoencoders with attention enable dynamic credit scoring and uncertainty quantification."
  - "A modular Bayesian framework allows soft weighting of heterogeneous financial data sources."
  - "Comprehensive validation includes tail-risk metrics, stress testing, and calibration analysis."
  - "Explainability and data privacy are critical considerations for deploying AI in banking."
  - "Spatio-temporal attention selectively focuses on salient historical events for robust predictions."
```
---

## Paper 44: Hopfgartner et al_summarized.md

**Source File:** `Hopfgartner et al_summarized.md`

```yaml
paper_id: 10.1007/s11469-024-01312-1
designation: international-algorithm-specific
title: Using Artificial Intelligence Algorithms to Predict Self‑Reported Problem Gambling Among Online Casino Gamblers from Different Countries Using Account‑Based Player Data
authors: Hopfgartner, N.; Auer, M.; Helic, D.; Griffiths, M. D.
year: 2024
venue: International Journal of Mental Health and Addiction
odin_topics:
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 7.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
tldr: Behavioral variables like self-exclusions and frequent in-session depositing predict self-reported problem gambling more strongly than monetary intensity, and machine learning models generalize across countries but improve with country-specific data.
problem_and_motivation: Early detection of problem gambling is critical, but prior work often used proxy measures like self-exclusion or relied on monetary amounts that vary by income. A model using behavioral indicators that generalize across jurisdictions is needed.
approach:
  - A secondary dataset of 1743 online casino gamblers from Canada, Great Britain, and Spain was used, with 27.4% scoring 8+ on the PGSI.
  - Features computed from 30 days of player-tracking data included demographics, behavioral metrics, and monetary intensity variables.
  - A hierarchical logistic regression was used to test the predictive value of control, behavioral, and monetary variable categories.
  - Five machine learning models (AdaBoost, decision trees, extra-trees, gradient boosting, random forests) were trained.
  - Models were evaluated via cross-country generalization (train on two countries, test on the third) and a global 70/30 train-test split.
findings:
  - num: 27.4% of the retained sample scored 8+ on the PGSI, indicating problem gambling.
  - num: Canadian gamblers had the highest problem gambling rate at 35.2%.
  - Behavioral variables significantly improved model fit (e.g., GB: χ²=145.5, p<0.001), while monetary variables did not.
  - Frequent in-session depositing, regular account depletion, and self-exclusion were key behavioral predictors.
  - num: The baseline model using only total deposits performed near random (ROC-AUC ≈ 0.5), confirming behavioral variables are essential.
  - num: The best global model (random forest for Canada) achieved ROC-AUC 0.717, outperforming cross-country models (e.g., 0.662 for extra-trees).
key_figures_tables:
  - Figure 1: PGSI score distribution before and after cleaning → Data cleaning removed hasty responses, especially at extremes.
  - Figure 2: PGSI completion times for max scorers → A natural gap at 1 minute supported the exclusion threshold.
  - Figure 3: Hierarchical regression coefficients → Behavioral factors dominate; monetary factors not significant.
  - Table 1: Descriptive statistics per country → Canada had highest PGSI and problem gambling rate.
  - Table 5: ROC-AUC values across models and countries → Including country-specific data improves prediction.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: PGSI
    definition: "Problem Gambling Severity Index, a 9-item scale for assessing gambling problems."
  - term: ROC-AUC
    definition: "Receiver operating characteristic area under the curve, a measure of binary classifier performance."
  - term: Account depletion
    definition: "Ending a gambling session with an account balance below €5."
critical_citations:
  - "[Auer & Griffiths, 2023a] — Found similar behavioral predictors using PGSI data in a European sample."
  - "[Hopfgartner et al., 2023] — Demonstrated that monetary variables did not improve prediction of self-exclusion."
  - "[Murch et al., 2023] — Showed repeated depositing and age as predictors of problem gambling."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Directly examines behavioral predictors of a risk profile (problem gambling) using account data.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Compares multiple ML classifiers for predicting problem gambling status.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Applies ML to predict a binary outcome from financial behavioral data.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: Uses time-series-like features (30-day windows) but does not forecast future spending.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: The predictive approach could inform adaptive budget adjustments, but not directly tested.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: high
      justification: Problem gambling is framed as an anomaly/risk to be detected from behavioral patterns.
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: high
      justification: ML models (e.g., random forest, gradient boosting) are evaluated for anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: Uses ROC-AUC and hierarchical regression to evaluate predictive performance.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Directly evaluates ML algorithms for predictive accuracy and cross-country generalization.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: contextual
      justification: Uses account-based data, but privacy is not a central theme.
  contribution: "This paper demonstrates that for Odin's behavioral profiling module, behavioral indicators like deposit frequency and account depletion are more robust predictors of financial risk than monetary amounts, enabling cross-cultural generalizability. For Odin's anomaly detection module, the comparative evaluation of tree-based classifiers provides a benchmark for selecting algorithms that balance performance and interpretability. The cross-country training paradigm offers a methodological template for evaluating how well Odin's models can adapt to new user populations without extensive country-specific retraining. The finding that simple monetary thresholds perform near-randomly justifies Odin's use of multi-feature behavioral models over naive spending-based heuristics."
  directly_justifies:
    - "Behavioral variables such as self-exclusion and frequent depositing are more predictive of financial risk than monetary amounts."
    - "Machine learning models trained on cross-country data can generalize, but performance improves with country-specific examples."
    - "Account depletion and in-session depositing are behavioral markers of impulsivity and risk."
    - "Simple monetary aggregates (e.g., total deposits) are insufficient for detecting financial behavioral anomalies."
  limits:
    - "Self-selection bias due to voluntary PGSI completion skews the sample toward higher problem gambling rates."
    - "The 30-day observation window may not capture long-term behavioral trends relevant to the PGSI's annual scope."
    - "Sample size imbalance across countries limits the generalizability of cross-country comparisons."
    - "The dataset includes only online casino gamblers, not other spending contexts."
    - "Psychological aspects of problem gambling are not captured by account-based data."
  mapping_rationale: "All 12 functional domains and their associated topic codes were systematically scanned. The strongest relevance was to Behavioral Profiling & Classification (5.A, 5.C) and Anomaly Detection (8.A, 8.B), as the paper directly predicts a risk status using ML classifiers. It also informs Spending Forecasting (6.A, 6.B) through its use of sequential behavioral features and System Evaluation (12.A, 12.B) via its comparative algorithm assessment. Budget Recommendation (7.B) and User Trust (10.B) were rejected as only tangentially related; the paper does not propose budget allocations or address trust mechanisms. A borderline case was topic 2.D (Filipino Spending Cycles), considered but rejected as the paper has no Filipino-specific data. The paper overall provides high relevance for algorithmic modules in Odin that detect financial risk and behavioral patterns, but low direct applicability to user-facing budgeting or cultural customization."
limitations:
  - "Self-selection bias due to voluntary survey participation."
  - "Small sample size for Canada after data cleaning."
  - "30-day observation window may mismatch PGSI's annual timeframe."
  - "Imbalanced country representation affects generalizability. [unacknowledged]"
  - "No analysis of psychological drivers beyond behavioral data. [unacknowledged]"
remember_this:
  - "Behavioral markers predict problem gambling better than money spent."
  - "Frequent in-session deposits and account depletion signal financial risk."
  - "Models generalize across countries but benefit from local training data."
  - "Simple monetary thresholds are as weak as random guessing."
  - "Self-exclusion is a strong behavioral indicator of problematic financial behavior."
```
---

## Paper 45: Lim & Cordova_summarized.md

**Source File:** `Lim & Cordova_summarized.md`

```yaml
paper_id: 10.1051/bioconf/20249305010
designation: local
title: Decoding the eco-financial mindset: financial literacy, attitudes, and efficacy measures and the spending behavior of Filipino millennials
authors: Lim, C. T.; Cordova, W.
year: 2024
venue: BIO Web of Conferences
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.B
  - 2.D
  - 5.A
  - 11.A
tldr: Filipino millennials' spending behavior shows a significant negative correlation with financial attitude, while financial literacy, attitude, and efficacy are strongly interrelated.
problem_and_motivation: Filipino millennials face financial vulnerability due to economic uncertainties, high education costs, and a perceived lack of financial acumen, yet their significant workforce presence makes their financial behavior crucial. Existing research often studies financial literacy, attitude, and efficacy in isolation, leaving a gap in understanding their combined effect on spending behavior.
approach:
  - Surveyed 431 millennials in Laguna, Philippines, via Google Forms.
  - Measured financial literacy, attitude, efficacy, and spending behavior using a custom questionnaire with Likert scales.
  - Employed Confirmatory Factor Analysis (CFA) to validate the measurement model for each latent variable.
  - Used Structural Equation Modeling (SEM) in Jamovi to test hypothesized relationships among the latent variables.
  - Evaluated model fit using RMSEA, TLI, CFI, and SRMR, and checked for multicollinearity using VIF.
findings:
  - num: Strong positive correlations were found between financial efficacy and literacy (β = 0.61, p < .001), and between financial attitude and literacy (β = 0.58, p < .001).
  - num: A significant negative correlation was identified between spending behavior and financial attitude (β = -0.18, p = 0.034).
  - num: 42% of respondents reported spending 41% or more of their income, indicating high variability in total spending.
  - num: 93.7% of respondents allocated 10% or less of their income to beer and wine, showing high consistency in this spending category.
  - The study did not find a statistically significant relationship between spending behavior and financial literacy or financial efficacy.
  - Millennials with a more positive financial attitude tend to exhibit more responsible spending behaviors.
  - Financial literacy, attitude, and efficacy are interdependent, suggesting a comprehensive strategy for financial well-being.
key_figures_tables:
  - Table 1: Socio-demographic characteristics of respondents → Shows sample is predominantly male, aged 26-27, earning PHP 20,000-26,999.
  - Table 2: List of latent variables and constructs → Details the observed variables for each financial construct, all with acceptable Cronbach's alpha.
  - Table 3: Spending construct observed variables frequency → Highlights variability in overall spending and consistency in alcohol spending.
  - Table 4: CFA fit indices for latent variables → Indicates a reasonable to good fit for the measurement models.
  - Table 5: Parameter estimates of structural paths → Quantifies the strength and direction of relationships among constructs.
  - Figure 1: Path diagram of the proposed SEM framework → Visually depicts the relationships among financial literacy, attitude, efficacy, and spending.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: CFA
    definition: Confirmatory Factor Analysis
  - term: SEM
    definition: Structural Equation Modeling
  - term: TPB
    definition: Theory of Planned Behavior
  - term: RMSEA
    definition: Root Mean Square Error of Approximation
  - term: TLI
    definition: Tucker-Lewis Coefficient
  - term: CFI
    definition: Comparative Fit Index
  - term: SRMR
    definition: Standardized Root Mean Square Residual
  - term: VIF
    definition: Variance Inflation Factor
critical_citations:
  - "[Ajzen, 1991] — Foundational theory for the study's framework."
  - "[Yanto et al., 2021] — Links social media to financial literacy development."
  - "[Sotiropoulos & d'Astous, 2013] — Supports link between financial attitude and spending."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: high
      justification: Directly studies Filipino millennials, a core demographic for Odin.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Provides data on income levels, employment, and primary financial goals of the target demographic.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Core focus of the paper is on spending behavior, a key financial behavior.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: medium
      justification: Investigates financial attitudes and behaviors within the Filipino cultural context.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Discusses general spending variability but does not explicitly analyze seasonal patterns.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Provides a breakdown of spending categories but does not specifically address spending cycles or occasions.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: The findings on the interplay of literacy, attitude, and efficacy can inform the development of behavioral profiles.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      relevance: medium
      justification: Recommendations for using social media and peer influence for financial education are relevant for user engagement.
  contribution: |
    This paper provides direct empirical evidence that financial attitude is a more significant predictor of spending behavior than financial literacy for Filipino millennials. This finding is directly relevant to Odin's user profiling module, suggesting that attitudinal metrics should be weighted heavily. The study's recommendation for tailored financial education programs that leverage social media can inform Odin's user retention and engagement strategies. The identified spending variability and consistency across categories can guide the design of Odin's expense categorization and anomaly detection features.
  directly_justifies:
    - "A positive financial attitude is significantly correlated with responsible spending behavior in Filipino millennials."
    - "Financial literacy, attitude, and efficacy are strongly interrelated and should be considered together."
    - "Tailored financial education programs that leverage social media can improve financial literacy and engagement."
  limits:
    - "Self-reported data may be subject to recall and social desirability bias."
    - "The sample is skewed towards respondents with jobs requiring financial skills."
    - "The cross-sectional design limits the ability to track changes in financial behavior over time."
    - "The study is geographically limited to Laguna, Philippines."
  mapping_rationale: |
    A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as high relevance for 'Filipino Cultural Context' (2.A) as it directly studies a Filipino demographic, and for 'Behavioral Profiling & Classification' (5.A) due to its analysis of financial attitudes and behaviors. It was also deemed high relevance for 'User Retention & Engagement' (11.A) because its recommendations for social media-based education can inform engagement strategies. The topics 1.A and 1.C were assigned high relevance as the paper directly addresses the demographic and its financial behavior. Topic 1.B was medium due to providing supporting demographic data. Topic 2.B was considered contextual as seasonal spending is not examined. Topic 2.D was low because while spending categories are broken down, the paper does not analyze spending cycles or occasions. Other domains like 'Spending Forecasting', 'Budget Recommendation', 'Anomaly Detection', and 'Data Privacy' were rejected as they are not addressed by the paper. The paper's overall relevance to Odin is medium, primarily informing the user profiling and engagement modules.
limitations:
  - "Self-reported data may be prone to recall and social desirability bias. [unacknowledged]"
  - "The sample is skewed towards respondents with jobs requiring financial skills, limiting generalizability."
  - "The cross-sectional design limits the ability to track changes in financial behavior over time. [unacknowledged]"
  - "The study is geographically limited to Laguna, Philippines. [unacknowledged]"
remember_this:
  - "Financial attitude, not literacy, is the strongest predictor of spending behavior."
  - "Millennials show high consistency in spending on alcohol, with 93.7% spending 10% or less."
  - "Financial literacy, attitude, and efficacy are strongly interdependent."
  - "Tailored programs using social media can improve financial literacy and engagement."
  - "42% of respondents spent 41% or more of their income, indicating high spending variability."
```
---

## Paper 46: Schwartz_summarized.md

**Source File:** `Schwartz_summarized.md`

```yaml
paper_id: 58b9e7a8-507f-5b70-8df8-9c7f07a1a5fe
designation: international
title: "The Rise of a Nudge: Field Experiment and Machine Learning on Minimum and Full Credit Card Payments"
authors: "Schwartz, D."
year: 2024
venue: "Unknown"
odin_topics:
  - "2.A"
  - "2.B"
  - "2.D"
  - "3.A"
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
  - "13.A"
tldr: "A field experiment on credit card payment warnings shows statement balance warnings increase full payments and reduce revolving interest, while minimum payment warnings reduce delinquency but do not increase full payments."
problem_and_motivation: "Minimum payment warnings, intended to reduce debt, may act as a perverse nudge by anchoring cardholders to lower payments, potentially increasing interest charges. A novel statement balance warning is proposed to help cardholders avoid interest by paying in full, but its effectiveness and heterogeneous effects are not well understood in real-world settings."
approach:
  - "A randomized controlled field experiment with 179,706 credit card debtors and 2.85 million observations, testing four email reminder conditions: control, minimum payment warning, statement balance warning, and both warnings."
  - "The experiment used a difference-in-differences design with individual fixed effects to estimate average treatment effects on payment behavior, interest charges, and delinquency."
  - "Causal random forests were applied to estimate heterogeneous treatment effects and to characterize subgroups with the largest responses to each warning."
  - "An online experiment with 400 participants replicated the field experiment to examine the role of financial knowledge, vulnerability, and cognitive reflection in warning effectiveness."
findings:
  - "num: Statement balance warnings increased the likelihood of paying in full by 0.9-1.1% (0.6-0.7 percentage points) compared to a simple reminder."
  - "num: Minimum payment warnings reduced the probability of not paying at least the minimum by 6.9-8.8% (0.7-0.9 percentage points) relative to the control."
  - "num: Both warnings reduced revolving interest by 9.0% and delinquent interest by 8.0% compared to the control condition."
  - "Causal forest analysis reveals significant heterogeneity; the top quintile of cardholders receiving the statement balance warning increased full payment likelihood by 2.4 percentage points."
  - "The warnings appear to act as target values rather than anchors, with cardholders shifting payments towards the salient amount (minimum or statement balance)."
  - "Effects are more pronounced for cardholders who vary their payment amounts, suggesting deliberation, and are not driven by liquidity constraints or income levels."
  - "The online experiment shows that the statement balance warning improves self-reported understanding of the statement balance, but effects are not moderated by financial literacy or cognitive reflection."
  - "The policy optimization analysis suggests that most cardholders should receive the statement balance warning or both warnings to minimize interest charges."
key_figures_tables:
  - "Figure 1: Payment distribution shifts → Warnings shift payments towards the salient target amount."
  - "Table II: Average treatment effects → All warnings increase payments and reduce delinquency, but only statement balance warnings increase full payments."
  - "Table IV: Sorted CATE per quintile → Top quintiles show much larger effects, revealing heterogeneity."
  - "Table VII: Effects based on previous behavior → Warnings are more effective for those who vary payments and have small gaps between minimum and statement balance."
  - "Table IX: Online experiment results → Statement balance warnings increase full payment likelihood by 18-25 percentage points in a hypothetical setting."
key_equations:
  - equation: "y_{it} = α + Σ_j β_j D_{ij} × P_t + δ P_t + X_{it} + μ_m + μ_y + a_i + ε_{it}"
    explanation: "Difference-in-differences model for estimating warning effects."
  - equation: "τ_D(x) = E[Y_i(1) - Y_i(0) | X_i = x]"
    explanation: "Conditional average treatment effect (CATE) for a warning D."
  - equation: "y_i = Σ_{k=1}^5 τ_{kD} w_{Di} × n_{ki} + Σ_{k=1}^5 ϑ_k n_{ki} + u_i"
    explanation: "Estimating CATEs for quintiles from causal random forest."
definitions:
  - term: "CATE"
    definition: "Conditional Average Treatment Effect; the expected treatment effect for an individual given their covariates."
  - term: "Causal Random Forest"
    definition: "A machine learning method for estimating heterogeneous treatment effects using random forests with a causal objective."
  - term: "Difference-in-Differences"
    definition: "A quasi-experimental design that compares changes in outcomes over time between treatment and control groups."
  - term: "Delinquent Interest"
    definition: "Interest charged when a cardholder fails to pay at least the minimum payment."
  - term: "Revolving Interest"
    definition: "Interest charged on the unpaid balance when a cardholder pays less than the full statement balance but at least the minimum."
  - term: "MAD"
    definition: "Mean Absolute Deviation; a measure of variability in payment amounts, used as a proxy for deliberation."
  - term: "Anchoring Bias"
    definition: "The tendency to rely heavily on an initial piece of information (an 'anchor') when making decisions."
critical_citations:
  - "[Wang and Keys, 2014] — Found minimum payment warnings can have a perverse effect."
  - "[Athey and Imbens, 2019] — Overview of machine learning methods for causal inference, including causal forests."
  - "[Tversky and Kahneman, 1974] — Seminal work on anchoring bias."
  - "[Navarro-Martinez et al., 2011] — Lab evidence on minimum payment salience reducing payments."
  - "[Agarwal et al., 2015] — Found no sizable effect of a minimum payment nudge in a field setting, contrasting lab results."
relevance:
  topics:
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      relevance: "contextual"
      justification: "The study is set in Chile, but findings on warning effectiveness are broadly applicable, not culturally specific."
    - code: "2.B"
      name: "Seasonal and Cyclical Spending Patterns"
      relevance: "low"
      justification: "The experiment is conducted over one billing cycle, but post-treatment effects dissipate, hinting at cyclicality in response."
    - code: "2.D"
      name: "Filipino Spending Cycles and 'Occasions'"
      relevance: "low"
      justification: "The paper does not address Filipino-specific cycles, but the target-value finding could be relevant for understanding spending around occasions."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      relevance: "contextual"
      justification: "The paper focuses on payment amounts, not categorization, but the concept of targets could inform categorization design."
    - code: "3.C"
      name: "User-Defined Allocation Constraints"
      relevance: "low"
      justification: "The findings on target values and deliberation are relevant for how users set their own allocation constraints."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      relevance: "contextual"
      justification: "The paper reviews credit card statements and warnings, which are part of the PFMS landscape."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      relevance: "high"
      justification: "The paper directly identifies the limitation of minimum payment warnings as a perverse nudge and proposes a solution."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      relevance: "high"
      justification: "The causal forest analysis characterizes profiles based on payment history and response to warnings."
    - code: "5.B"
      name: "Profile Dynamics and the Cold-Start Problem"
      relevance: "low"
      justification: "The paper discusses heterogeneity but does not focus on cold-start profile estimation."
    - code: "5.C"
      name: "Classification Approaches for Financial Behavioral Profiles"
      relevance: "medium"
      justification: "Causal random forests are used to classify individuals based on treatment response, a form of behavioral profiling."
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      relevance: "contextual"
      justification: "The paper uses machine learning for causal inference, not forecasting, but the techniques are relevant."
    - code: "6.B"
      name: "Forecasting Algorithms for Sequential Spending Data"
      relevance: "low"
      justification: "The paper does not forecast spending; it analyzes payment behavior."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      relevance: "low"
      justification: "The paper's findings on target values can inform how to present budget targets."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      relevance: "medium"
      justification: "The policy optimization analysis is a form of recommending the best warning message for each user."
    - code: "7.C"
      name: "Constrained Optimization Approaches for Budget Allocation"
      relevance: "low"
      justification: "The paper does not use constrained optimization, but the two-target setting (minimum vs. full) is analogous."
    - code: "7.D"
      name: "Infeasibility Handling and Reduction Hierarchies"
      relevance: "medium"
      justification: "The paper shows users prioritize a target based on attainability, similar to handling infeasible budget constraints."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      relevance: "contextual"
      justification: "Delinquency (not paying minimum) is an anomaly the warnings aim to prevent."
    - code: "8.B"
      name: "Anomaly Detection Algorithms for Personal Spending Data"
      relevance: "low"
      justification: "The paper does not use anomaly detection algorithms."
    - code: "8.C"
      name: "Cold-Start Baseline Strategies for Anomaly Detection"
      relevance: "low"
      justification: "The paper does not address cold-start anomaly detection."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      relevance: "medium"
      justification: "The statement balance warning encourages a savings-like behavior (avoiding interest) by paying a target amount."
  contribution: "This paper provides experimental evidence that a statement balance warning is an effective nudge for increasing credit card payments and reducing interest charges, offering a directly implementable design feature for Odin's payment reminder or bill-pay module. The use of causal random forests demonstrates a methodology for profiling users based on their heterogeneous responses, which can inform Odin's behavioral profiling and personalization engine. The finding that warnings act as target values rather than anchors has implications for how Odin presents budget goals and savings targets to users. The policy optimization framework provides a template for Odin to recommend personalized nudges or reminders based on user payment history. The paper also highlights the importance of testing behavioral interventions in field settings to overcome biases found in lab experiments."
  directly_justifies:
    - "Statement balance warnings increase full payments and reduce revolving interest, providing a justification for including such a feature in Odin's bill-pay reminders."
    - "Minimum payment warnings reduce delinquency, supporting the use of such warnings for users at risk of missing minimum payments."
    - "Causal random forests can be used to profile users and personalize nudges, supporting Odin's adaptive recommendation system."
    - "Warnings act as target values, suggesting that presenting clear, actionable financial targets can improve user behavior in Odin."
    - "Behavioral interventions can be designed to be scalable and palatable to financial institutions, supporting Odin's potential for real-world deployment."
  limits:
    - "The field experiment was conducted over one billing cycle; long-term effects and habituation to warnings are not assessed."
    - "The study is set in Chile with a specific credit card issuer; generalizability to other countries and financial products, including PFMS like Odin, requires validation."
    - "The online experiment is hypothetical, and stated intentions may not perfectly correlate with real payment behavior."
    - "The causal forest analysis, while robust, may not be easily interpretable for all stakeholders, posing a challenge for explaining personalized recommendations."
    - "The study does not address how warnings interact with other financial behaviors, such as budgeting or savings, which are central to Odin."
  mapping_rationale: "A systematic scan was performed across all 12 functional domains and their associated topic codes. The paper was flagged as most relevant to 'Existing Systems & Gaps' (4.A, 4.B) due to its direct critique of the minimum payment warning and proposal of a new solution. It is highly relevant to 'Behavioral Profiling & Classification' (5.A, 5.C) because of its use of causal forests to identify heterogeneous treatment effects and profile users based on payment history and response, and to 'Budget Recommendation' (7.A, 7.B, 7.D) through its policy optimization analysis and two-target setting which parallels constrained budget allocation. The paper also has medium relevance to 'Savings & Debt Management' (13.A) as the statement balance warning encourages debt reduction and interest avoidance akin to a savings goal, and 'Anomaly Detection' (8.A) indirectly through its focus on preventing delinquency. Topics related to 'Filipino Cultural Context' (2.A, 2.B, 2.D) were considered but deemed contextual or low relevance as the study is not specific to the Philippines, though its behavioral findings are broadly applicable. Topics like 'Expense Categorization' (3.A, 3.B) and 'Spending Forecasting' (6.A, 6.B) were considered rejected because the paper does not address categorization or predictive forecasting directly, though its methodology could be extended to those areas. The paper's overall relevance to Odin is substantial, providing evidence-based design principles for payment reminders, behavioral profiling, and personalized nudging, while also offering a cautionary tale about the potential perverse effects of poorly designed nudges."
limitations:
  - "The field experiment was conducted over a single billing cycle, leaving open questions about long-term effectiveness and habituation."
  - "The sample is from Chile, which has a unique financial landscape; findings may not generalize to Filipino young professionals without further validation."
  - "The online experiment is hypothetical, and intentions may not translate to actual behavior in a real PFMS context."
  - "The study does not explore how warnings interact with other PFMS features like budgeting or savings goals."
  - "The causal forest analysis, while powerful, relies on a specific implementation and may not be easily replicable in all settings. [unacknowledged]"
  - "The policy optimization analysis is a simulation and does not account for the dynamic nature of user preferences over time. [unacknowledged]"
  - "The potential for unintended consequences, such as users reducing other forms of saving to make larger credit card payments, is not examined. [unacknowledged]"
remember_this:
  - "Statement balance warnings increase full credit card payments by 0.9-1.1%."
  - "Minimum payment warnings reduce the probability of delinquency by 6.9-8.8%."
  - "Causal random forests reveal that 20-40% of cardholders significantly increase payments due to warnings."
  - "Warnings act as target values, not anchors, shifting payments towards the salient amount."
  - "The effect of warnings is not driven by income or liquidity constraints, but by payment variability."
```
---

## Paper 47: Cho_summarized.md

**Source File:** `Cho_summarized.md`

```yaml
paper_id: 10.1057/s41599-024-03605-1
designation: international
title: A qualitative investigation of financial decision-making and enabling factors among ethnic minority young adults in Hong Kong
authors: Cho, E. Y.-N.
year: 2024
venue: Humanities and Social Sciences Communications
odin_topics:
  - 1.C
  - 2.A
  - 2.B
  - 4.B
  - 5.A
  - 10.A
  - 13.B
tldr: Ethnic minority young adults in Hong Kong employ diverse strategies for budgeting, saving, and spending, yet remain vulnerable to fraud and high-interest debt.
problem_and_motivation: Financial decision-making among racial/ethnic minority young adults is under-examined, particularly regarding day-to-day management and in non-Western contexts. Existing research is predominantly quantitative and often overlooks the specific challenges and strategies of this demographic. This study addresses these gaps by exploring their financial practices, perceptions, and enabling factors.
approach:
  - Qualitative study using individual semi-structured interviews.
  - Sample of 53 Pakistani, Indian, Nepalese, and Filipino participants aged 18-29 in Hong Kong.
  - Thematic analysis was used to identify major themes in financial decision-making.
  - Investigated a range of financial decisions: budgeting, spending, planning, using products, debt, and fraud detection.
  - Explored factors enabling sound financial decisions, such as family social capital and intrapersonal characteristics.
findings:
  - Most participants had developed budgeting habits using digital tools, parental monitoring, or mental bucketing.
  - Many saved approximately one-third of their monthly income for goals like education, property, and business.
  - Informal borrowing from family and friends was common, though some used government or high-interest lending institution loans.
  - Around one-third used credit cards, with occasional risks arising from minimum payments or using others' cards.
  - Participants employed passive strategies like ignoring messages to avoid scams but still fell victim to various frauds.
  - Five enabling factors for financial decision-making were identified: family social capital, intrapersonal characteristics, social dynamics factors, command of knowledge, and facilitative contextual circumstances.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: None.
    definition: ""
critical_citations:
  - "[Lusardi and Mitchell, 2011b] — Documents lower financial literacy among US racial/ethnic minorities."
  - "[Atkinson and Messy, 2012] — Defines financial literacy and its components."
  - "[Goodstein et al., 2021] — Highlights racial/ethnic differences in credit use."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: high
      justification: Directly examines budgeting, saving, and spending behaviors of ethnic minority young adults.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: high
      justification: Explores family social capital and informal borrowing as culturally influenced practices.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Mentions saving for cyclical events like weddings but does not focus on seasonal patterns.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: medium
      justification: Identifies gaps in financial education and system support for ethnic minorities.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Provides qualitative data on spending philosophies and saving behaviors, informing profile construction.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Discusses fraud victimization and tactics, but not data privacy or security systems.
    - code: 13.B
      name: Debt Management in PFMS
      relevance: high
      justification: Details practices and perceptions of borrowing, credit card use, and debt repayment.
  contribution: This study provides qualitative insights into the financial behaviors and enabling factors of ethnic minority young adults. It directly informs the design of Odin's user profiling and behavioral classification modules (5.A). Its findings on enabling factors can be used to shape culturally-aware user models and engagement strategies for Filipino young professionals. The detailed accounts of budgeting, saving, and debt management practices offer a foundation for developing relevant financial features and recommendations.
  directly_justifies:
    - "Ethnic minority young adults use digital tools, parental monitoring, and mental bucketing for budgeting."
    - "Saving approximately one-third of monthly income is a common practice among this group."
    - "Informal borrowing from family and friends is a prevalent debt management strategy."
    - "Vulnerability to fraud is high, even with protective tactics, highlighting a need for better education."
  limits:
    - "The study is qualitative with a small sample size, limiting generalizability."
    - "Findings are based on a relatively well-educated and English-proficient sample."
    - "The research was conducted in Hong Kong, which may limit applicability to other Asian contexts."
  mapping_rationale: A systematic scan was conducted across all 12 functional domains. The domain on Financial Behavior of Filipino Young Professionals (1.C) was identified as most directly relevant, receiving a 'high' rating, as the study's core focus is on financial actions. The Culturally Specific Financial Practices domain (2.A) was also rated 'high' due to its examination of family social capital, informal borrowing, and spending philosophies as culturally informed practices. Debt Management (13.B) was rated 'high' as borrowing and credit card use are major themes. The Limitations and Gaps domain (4.B) was rated 'medium' as the paper identifies gaps in financial literacy education for ethnic minorities. Behavioral Profiling (5.A) was rated 'medium' for its rich descriptions of behavioral patterns and philosophies. Seasonal Patterns (2.B) and Data Privacy (10.A) were considered and rejected or rated 'low/contextual' because they are not the paper's primary focus. The overall relevance is high, providing rich qualitative data to inform the design of user-centric and culturally-aware features.
limitations:
  - "Sample size is small and may not be representative of all ethnic minority young adults."
  - "Findings are context-specific to Hong Kong and may not generalize to the Philippines."
  - "The study did not include ethnic Chinese young adults for comparison."
  - "Potential for social desirability bias in self-reported financial behaviors. [unacknowledged]"
  - "The reliance on interviews may not capture the full complexity of real-world financial decisions. [unacknowledged]"
remember_this:
  - "Many saved at least 30% of income for long-term goals like education and property."
  - "Budgeting is often supported by digital tools, family monitoring, and mental accounting."
  - "Informal borrowing from family and friends is a common and culturally embedded practice."
  - "Fraud victimization occurs despite passive avoidance strategies like ignoring suspicious calls."
  - "Peer and family mentorship are key enabling factors for financial decision-making."
```
---

## Paper 48: Hassan et al_summarized.md

**Source File:** `Hassan et al_summarized.md`

```yaml
paper_id: 10.1109/ACCESS.2024.3359053
designation: international-algorithm-specific
title: GCZRec: Generative Collaborative Zero-Shot Framework for Cold Start News Recommendation
authors: Hassan, S. Z. U.; Rafi, M.; Frnda, J.
year: 2024
venue: IEEE Access
odin_topics:
  - 6.A
  - 6.B
  - 8.B
  - 8.C
  - 5.C
  - 12.B
tldr: A generative adversarial framework synthesizes user-item interactions using latent features and collaborative signals to recommend news items in cold-start and warm-start scenarios.
problem_and_motivation: Recommender systems struggle to recommend new items without historical interaction data, a severe cold-start problem in news recommendation. Existing techniques fail to leverage collaborative information for serendipity and diversity in recommendations.
approach:
  - The framework uses conditional Wasserstein GANs with dual generator networks for news-to-user and user-to-news interaction synthesis.
  - A state gate determines which generator to use based on whether the user and news are warm or cold start.
  - Zero-shot classifiers (1D-CNN) predict labels for cold-start news and users using their latent feature representations.
  - The generator for news-to-user interactions synthesizes interest scores for all users given a news item.
  - The generator for user-to-news interactions synthesizes interest scores for all news items given a user.
findings:
  - The GCZRec framework outperforms baseline models in accuracy and ranking quality for cold-start news recommendation.
  - num: The proposed model shows an average improvement of +0.1113 in nDCG@5 over baselines.
  - num: AUC improvements are significant for the MIND dataset in cold-start settings.
  - The framework implicitly incorporates serendipity by using collaborative information in feature space.
  - The model can be used as a preprocessing step to improve existing recommender systems.
  - num: The framework generates diverse recommendations, with 28% new high-interest items found over 50 generations.
key_figures_tables:
  - Figure 2: Architecture of GCZRec framework showing dual generators and zero-shot predictors → Overall system design for cold/warm start synthesis.
  - Figure 4: Precision-recall curve for cold-start case → Demonstrates performance trade-off at different k values.
  - Figure 5: Precision-recall curve for mixed cold-warm start case → Shows improvement in mixed case recommendations.
  - Table 1: Statistics of Adressa and MIND datasets → Dataset scale and characteristics for the experiments.
key_equations:
  - equation: min_G max_D V(D,G) = E_{c,x∼true}[D(x,c)] - E_{c,z}[D(G(z,c)),c]
    explanation: Objective function of conditional Wasserstein GAN.
  - equation: P(y_Ni|δ) = (e^{w_i · δ}) / (∑_{j=1}^{k} e^{w_j · δ})
    explanation: Softmax probability for news label prediction.
  - equation: nDCG@k = (DCG@k) / (IDCG@k)
    explanation: Normalized discounted cumulative gain for ranking quality.
definitions:
  - term: Zero-shot learning
    definition: Classification where training and test classes are disjoint, used here for cold-start recommendation.
  - term: Cold-start problem
    definition: The challenge of recommending items to users without historical interactions.
  - term: Serendipity
    definition: The ability of an algorithm to recommend unexpected and diverse items to expand user taste.
  - term: cWGAN
    definition: Conditional Wasserstein Generative Adversarial Network using Wasserstein loss for stable training.
critical_citations:
  - "[Li et al., 2019] — Formulated cold-start as zero-shot learning."
  - "[Alshehri & Zhang, 2022] — Previous generative zero-shot framework for news recommendations."
  - "[Wang et al., 2017] — IRGAN foundational work on GAN for recommendation."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: "Directly addresses predictive modeling for generating user-item interactions."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: high
      justification: "Framework uses generative algorithms for sequential interaction forecasting."
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: medium
      justification: "Interaction synthesis could be adapted to generate baseline scores for anomaly detection."
    - code: 8.C
      name: Cold-Start Baseline Strategies for Anomaly Detection
      relevance: high
      justification: "Provides a generative baseline strategy for handling cold-start users/items."
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: low
      justification: "Uses classification (1D-CNN) for user labeling, which is a similar approach."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: contextual
      justification: "Provides evaluation metrics like AUC, nDCG, and MAP for algorithm performance."
  contribution: "The GCZRec generative framework offers a method for synthesizing user-item interactions that can be adapted for PFMS forecasting. Its use of zero-shot classification provides a clear strategy for cold-start scenarios in user profiling and expense categorization. The dual-generator approach can be modularly applied to generate recommendations or anomaly scores for financial data. The framework's emphasis on serendipity via collaborative signals is crucial for user retention in a PFMS. This work directly justifies the use of generative adversarial networks for module-level evaluation in Odin."
  directly_justifies:
    - "Generative adversarial networks can synthesize interactions without a separate predictor module."
    - "Zero-shot classification using latent features effectively handles cold-start users and items."
    - "Incorporating collaborative signals improves the serendipity and diversity of recommendations."
    - "Dual generator networks can produce ranking scores for both user-to-item and item-to-user directions."
    - "The framework provides a baseline for evaluation against purely cold-start and mixed scenarios."
  limits:
    - "The model does not consider temporal relations between news clicks or item correlations."
    - "Evaluation is focused on news, not financial data, requiring adaptation."
    - "The current labeling scheme may not directly map to financial categories."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The primary relevance was found in the 'Spending Forecasting' domain (6.A, 6.B) and 'Anomaly Detection' domain (8.B, 8.C) due to the paper's focus on predictive interaction synthesis and handling cold-start scenarios. The 'Behavioral Profiling & Classification' domain (5.C) was flagged as low relevance because the classification approach is a supporting technique. The 'System Evaluation' domain (12.B) was considered contextual because the evaluation metrics are standard but not unique to PFMS. Domains related to Filipino cultural context, expense categorization, and user trust were rejected as the paper is a general algorithmic contribution without any domain-specific financial or cultural framing. The overall relevance is moderate, providing solid algorithmic foundations that can be adapted for Odin's forecasting and anomaly detection modules."
limitations:
  - "The framework is evaluated on news, not financial data, limiting direct applicability to PFMS."
  - "Label encoding scheme may not generalize to financial category structures."
  - "Temporal correlations between user actions are not modeled."
remember_this:
  - "Generative zero-shot framework synthesizes interactions for cold-start users and items."
  - "num: Achieves up to +0.1113 higher nDCG@5 compared to baseline models."
  - "Dual generator networks enable both user-to-item and item-to-user recommendation."
  - "Collaborative signals in feature space enhance diversity and serendipity."
  - "The framework offers a preprocessing method to enhance existing recommender systems."
```
---

## Paper 49: Lien & Rajasekharan_summarized.md

**Source File:** `Lien & Rajasekharan_summarized.md`

```yaml
paper_id: 10.1016/j.enbuild.2024.114954
designation: international-algorithm-specific
title: Automatic standard building category classification from smart meter data – A supervised learning approach
authors: Lien, S.K.; Rajasekharan, J.
year: 2024
venue: Energy & Buildings
odin_topics:
  - 3.A
  - 3.B
  - 4.A
  - 4.B
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
tldr: Supervised classification of hourly smart meter data using 82 physics-based features achieves 84% accuracy in identifying Norwegian building categories and heating type.
problem_and_motivation: Building metadata essential for grid planning and energy policy is often unavailable or costly to obtain. Existing classification approaches rely on limited datasets or unsupervised methods that fail to align with standardized building categories, hindering practical application.
approach:
  - Dataset comprises 2724 Norwegian buildings across 11 categories with hourly electricity and temperature data.
  - Extracted 82 physics-based domain features from each time series, covering load variation, seasonality, daily profiles, and correlation with standard profiles.
  - Evaluated multiple classifiers including Random Forest, CatBoost, SVM, and Gradient Boosting.
  - Applied feature selection and ensemble methods to optimize performance.
  - Tested generalizability on external datasets from Norway, Canada, and the US/UK.
findings:
  - num: Random Forest and CatBoost achieved 84% accuracy for building type and 89% for category-only prediction.
  - num: Top-2 accuracy reached 92% for type and 97% for category, offering robust fallback for ambiguous cases.
  - num: Feature selection showed that 7-12 features capture most discriminatory information, peaking at 86% accuracy.
  - Supervised classification significantly outperformed K-means clustering in aligning predictions with predefined building codes.
  - Generalizability was strong for Norwegian residential data (70-75% accuracy) but poor for international datasets, indicating climate and labeling sensitivity.
  - Ensemble learning did not improve performance, likely due to high correlation among base models.
  - SLP features derived from the same data source contributed only a marginal 0.5% accuracy gain.
key_figures_tables:
  - Table 1: Dataset labels and support → Shows class distribution and highlights data imbalance, guiding performance interpretation.
  - Figure 3: Confusion matrices for classifiers → Demonstrates low confusion between residential and non-residential categories.
  - Figure 6: Accuracy vs. feature count → Indicates optimal feature set of 7-12 for efficient classification.
  - Figure 7: Elbow and silhouette scores → Shows unsupervised k-means peaks at 6 clusters, misaligned with 17 building labels.
  - Figure 8: Cluster assignments vs. labels → Visualizes the mismatch between unsupervised groups and regulatory categories.
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "TEK17"
    definition: "Norwegian building regulations defining standard building categories."
  - term: "PROFet"
    definition: "Model for generating standard load profiles based on building area and outdoor temperature."
  - term: "AMS"
    definition: "Advanced Metering System, the Norwegian smart meter infrastructure."
  - term: "EH"
    definition: "Electric heating classification for buildings."
  - term: "NEH"
    definition: "Non-electric heating classification for buildings."
critical_citations:
  - "[K. B. Lindberg et al., 2019] — Modeling electric/heat loads for forecasting."
  - "[M. Sodenkamp et al., 2016] — Supervised classification with interdependent variables."
  - "[C. Miller et al., 2020] — Building Data Genome Project 2 dataset."
  - "[C. Miller, 2019] — Explainable ML for non-residential smart meter classification."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: contextual
      justification: "Provides a framework for classifying building types from consumption data, analogous to expense categorization."
    - code: 3.B
      name: Expense Category Design Considerations
      relevance: low
      justification: "Discusses the design of building categories, not user expense categories."
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: low
      justification: "Reviews smart meter classification landscape but not PFMS."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: "Explicitly identifies gaps in supervised classification and limited datasets for building metadata extraction."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: contextual
      justification: "Analogous profiling of building load profiles using supervised learning."
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: "Demonstrates a supervised classification approach for profiling building energy behavior."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: low
      justification: "Focuses on classification, not predictive modeling of future spending."
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: low
      justification: "Not a forecasting paper; focuses on static classification."
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: contextual
      justification: "Extracts domain knowledge (physics-based features) to inform classification, analogous to budget rule design."
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: low
      justification: "Not about recommendation; about classification."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      relevance: low
      justification: "Discusses misclassification consequences, not anomaly detection."
    - code: 8.B
      name: Anomaly Detection Algorithms for Personal Spending Data
      relevance: low
      justification: "Uses classification, not anomaly detection algorithms."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: medium
      justification: "Uses accuracy, precision, recall, and F1 to evaluate classification performance."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: medium
      justification: "Compares multiple classifiers and ensemble methods."
    - code: 13.C
      name: End-of-Period Surplus as a Savings Input
      relevance: contextual
      justification: "Classifies building load profiles to understand peak loads, tangentially related to surplus identification."
  contribution: "This paper provides a robust supervised classification framework that can be adapted to classify user expense patterns in Odin, particularly for cold-start profiling (5.C). Its emphasis on domain-specific feature engineering (7.A) and evaluation metrics (12.A/12.B) directly informs Odin's algorithmic module design. The identification of gaps in existing unsupervised approaches (4.B) justifies Odin's use of supervised learning for behavioral classification. The paper's handling of noisy, real-world meter data offers lessons for Odin's data preprocessing and feature extraction pipeline."
  directly_justifies:
    - "Supervised learning with domain-informed features outperforms unsupervised clustering for predefined category classification."
    - "Feature selection can reduce dimensionality while maintaining high accuracy, crucial for mobile-first efficiency."
    - "Classification accuracy can be significantly impacted by data labeling uncertainty, a challenge Odin must address."
    - "Ensemble methods may not improve performance if base models share correlated errors."
    - "Model generalizability is limited across climate zones, requiring careful validation for Philippine data."
  limits:
    - "The study is primarily focused on Norwegian buildings and climate, limiting direct transferability to the Philippines."
    - "The dataset labels contain uncertainty, and buildings with mixed use are assigned a single category, limiting real-world granularity."
    - "The method does not classify buildings with PV systems or other distributed energy resources, a growing trend."
    - "The paper does not address real-time classification or streaming data scenarios."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The domains of 'Expense Categorization' (3.A, 3.B) and 'Existing Systems & Gaps' (4.B) were flagged as highly relevant because the paper directly addresses classification frameworks and identifies limitations of unsupervised methods. The 'Behavioral Profiling & Classification' domain (5.C) is highly relevant due to the supervised classification approach for building types, which parallels user behavior classification. The 'System Evaluation' domain (12.A, 12.B) was assigned medium relevance because the paper employs rigorous performance metrics and model comparisons. Domains like 'Filipino Cultural Context' (2.A-2.D), 'Data Privacy & User Trust' (10.A, 10.B), and 'User Retention & Engagement' (11.A, 11.B) were considered and rejected as the paper does not address these aspects. The 'Spending Forecasting' (6.A, 6.B) and 'Budget Recommendation' (7.A, 7.B) domains were considered but deemed low relevance because the paper focuses on classification, not prediction or optimization. Overall, the paper's strength lies in its methodological framework for classification from time-series data, which directly informs Odin's approach to profiling and its evaluation, while its geographic and application context limits direct applicability."
limitations:
  - "The method is trained on Norwegian data and may not generalize to Filipino spending patterns without retraining and feature adaptation."
  - "The reliance on hourly data may not be feasible for Odin's mobile-first architecture with potentially lower-frequency inputs. [unacknowledged]"
  - "The paper assumes the existence of standardized building categories, which may not perfectly map to user expense categories. [unacknowledged]"
  - "Performance on international datasets was poor, highlighting sensitivity to cultural and climatic factors. [unacknowledged]"
remember_this:
  - "Supervised classification using 82 features achieved 84% accuracy for building type."
  - "Feature selection reduced inputs to 7-12 features while maintaining high accuracy."
  - "Domain-specific features significantly outperformed generic or unsupervised approaches."
  - "Model generalization across different climates remains a key challenge."
  - "Accurate labeling is critical; uncertainty in ground truth limits maximum achievable accuracy."
```
---

## Paper 50: Zhu-2024_summarized.md

**Source File:** `Zhu-2024_summarized.md`

```yaml
paper_id: 10.1016/j.techsoc.2024.102599
designation: international-algorithm-specific
title: Optimizing financial decision-making for emerging adults: A compact Python-based personalized financial projection approach
authors: Zhu, A. Y. F.
year: 2024
venue: Technology in Society
odin_topics:
  - 1.A
  - 1.C
  - 2.A
  - 2.D
  - 4.A
  - 4.B
  - 5.A
  - 6.A
  - 7.A
  - 7.C
  - 9.B
  - 10.A
  - 12.A
  - 12.B
tldr: A compact Python-based personalized financial projection intervention significantly improved perceived financial literacy, future time perspectives, and healthy financial behaviors among Hong Kong emerging adults.
problem_and_motivation: Emerging adults face critical financial decisions but lack tailored interventions that simultaneously address financial literacy and future time perspectives. Existing financial education programs are predominantly designed for children and adolescents, leaving a gap for this demographic. A compact, code-based approach could overcome limitations of opaque mobile app projections.
approach:
  - Conducted a two-arm randomized controlled trial with 78 university students in Hong Kong.
  - Experimental group received a 120-minute Python-based PFP session with 45 minutes of coding instruction.
  - Three themed projection models covered housing mortgages, education loans, and regular savings scenarios.
  - Participants modified Python code parameters to simulate counterfactual financial outcomes.
  - Control group attended an unrelated statistics course; outcomes measured via pretest-posttest surveys.
findings:
  - num: Experimental group showed significant improvements in perceived financial literacy (β=0.18, p<0.05) and future time perspectives (β=0.13, p<0.10) post-intervention.
  - num: Python-based PFP significantly increased financial behavioral control (β=0.14, p<0.10), tendency for healthy financial behaviors (β=0.20, p<0.01), and life satisfaction (β=0.20, p<0.05).
  - The effect on healthy financial behaviors was fully mediated by perceived financial literacy and future time perspectives.
  - Life satisfaction gains were partially mediated by improved financial literacy and healthy financial behaviors.
  - The intervention's direct effect on financial behavioral control disappeared when controlling for literacy and time perspectives.
key_figures_tables:
  - "Figure 1: Hypothesized mechanism model → Shows mediation pathways from PFP to outcomes via literacy and time perspective."
  - "Table 1: Descriptive statistics by group → No significant differences except age, confirming randomization success."
  - "Table 2: Regression results → All five outcome variables improved significantly in the experimental group."
  - "Figure 2: Structural model coefficients → Highlights full mediation of financial behaviors through literacy and time perspective."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: PFP
    definition: Personalized Financial Projection - a tool forecasting future wealth based on current financial inputs.
  - term: Interactive AI
    definition: Artificial intelligence systems that engage in dialogue and provide responses based on user queries.
critical_citations:
  - "[Zhu, 2024] — Initial Python-based PFP study showing modest effects, addressed here."
  - "[Hershfield et al., 2018] — Vividness interventions improve financial decision-making."
  - "[Lusardi, 2019] — Defines core financial literacy components including compound interest."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Study focuses on Hong Kong emerging adults, providing demographic parallels for Filipino young professionals.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Provides validated pathways linking financial literacy and future time perspective to financial behaviors.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: Highlights unique financial challenges in Hong Kong (housing, education loans) that may parallel Filipino contexts.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Touches on financial decision-making around life events (housing, education) relevant to spending cycles.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: medium
      justification: Critiques existing mobile app PFPs and identifies gaps this approach addresses.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: high
      justification: Explicitly identifies opacity of mobile PFPs and lack of tailored interventions for emerging adults as key gaps.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Measures financial behavioral control and tendency for healthy behaviors as proxy outcomes.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: medium
      justification: Uses projection models that simulate future financial states based on current parameters.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      relevance: low
      justification: Indirectly informs budgeting through savings and debt projection models.
    - code: 7.C
      name: Constrained Optimization Approaches for Budget Allocation
      relevance: low
      justification: Allows parameter adjustment for scenario analysis, analogous to constraint manipulation.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      relevance: contextual
      justification: Critiques mobile app limitations, justifying the code-based approach as an alternative UX.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      relevance: low
      justification: Mentions algorithmic fairness and transparency concerns for interactive AI.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Uses a rigorous RCT design with validated psychological and behavioral measures for evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      relevance: high
      justification: Evaluates the algorithmic PFP module's effectiveness via mediation analysis and controlled experiment.
  contribution: "This study provides a validated, compact Python-based financial intervention that directly informs Odin's behavioral profiling (5.A) by measuring literacy, time perspective, and behavioral control as mediators. It justifies Odin's approach to forecasting (6.A) by demonstrating that user-modifiable projection models improve financial attitudes. The RCT methodology (12.A) and mediation framework offer a rigorous template for evaluating Odin's algorithmic modules (12.B). The paper's critique of opaque PFPs (4.B) supports Odin's need for transparency and counterfactual reasoning features. Finally, the focus on emerging adults (1.A) directly aligns with Odin's target demographic, providing evidence for tailored, topic-specific interventions."
  directly_justifies:
    - "Python-based PFP significantly improves perceived financial literacy and future time perspectives in emerging adults."
    - "Enhancing financial literacy and time perspective fully mediates the effect on healthy financial behaviors."
    - "Compact, code-based financial interventions are effective and address limitations of mobile app projections."
    - "Personalized projection models on key life decisions (housing, education, savings) are more engaging and effective."
  limits:
    - "Lack of validated objective measure of financial literacy; only perceived literacy was assessed. [unacknowledged]"
    - "Only immediate post-intervention effects measured; medium- and long-term behavioral changes not assessed."
    - "Sample was restricted to non-finance, non-CS students with no prior Python experience, limiting generalizability to tech-savvy users."
    - "Study conducted in Hong Kong; cultural and economic context may limit direct transferability to the Philippines."
  mapping_rationale: "A systematic scan of all 12 functional domains and their associated topic codes was performed. The paper was flagged as highly relevant to 'Existing Systems & Gaps' (4.A, 4.B) due to its explicit critique of mobile app PFPs and identification of opacity as a key limitation. It showed high relevance to 'System Evaluation' (12.A, 12.B) because of its rigorous RCT methodology and mediation analysis, which serves as a template for evaluating Odin's modules. Medium relevance was assigned to 'Behavioral Profiling' (5.A) and 'Spending Forecasting' (6.A) as the paper measures and influences behavioral precursors and uses simulation models. Low or contextual relevance was assigned to topics like 'Budget Recommendation' (7.A, 7.C) and 'Data Privacy' (10.A), as these are touched upon but not central. The paper was considered but rejected for topics like 'Anomaly Detection' (8.A-C) and 'Savings & Debt Management' (13.A-C) because, while savings and debt are modeled, the core contribution is behavioral and educational, not about detection or management frameworks. The borderline case of topic 2.D (Spending Cycles) was considered low because the paper discusses life event decisions (housing, education) rather than recurring cyclical spending patterns. Overall, the paper is highly relevant to Odin's need for a transparent, engaging, and behaviorally-grounded financial intervention approach."
limitations:
  - "Lack of validated objective financial literacy measure; relied on perceived literacy."
  - "Only immediate effects measured; no follow-up to assess behavioral persistence. [unacknowledged]"
  - "Sample restricted to a single Hong Kong university, limiting cultural and economic generalizability."
  - "Excluded participants with prior Python or finance background; effects on tech-savvy users unknown."
remember_this:
  - "Python-based PFP increased healthy financial behaviors by 20% (standardized β) in emerging adults."
  - "Effects on behavior were fully mediated by perceived financial literacy and future time perspective."
  - "A 120-minute intervention was effective, addressing time constraints of the target demographic."
  - "User-modifiable projection code enhances trust and understanding compared to black-box AI."
  - "Topic-specific models (housing, education, savings) are more effective than generalized projections."
```
---


---

## Agent Instruction

If the agent reading this document believes further context about a paper is needed, it may request the original converted markdown file (with the '_marked' suffix) from the user for the relevant paper(s).
