```yaml
paper_id: 10.62986/dp2025.35
designation: local
title: Gender equality, disability, and social inclusion in the Philippines: Progress, challenges, and opportunities in SDG 5 and SDG 10
authors: Albert, J. R. G.; Dacuycuy, C. B.; Quisumbing, A. R.; Basillote, L. B.; Cabalfin, D. L. D.; Vargas, A. R. P.; Luzon, P. E. D.; Mahmoud, M. A.
year: 2025
venue: PIDS Discussion Paper Series
odin_topics:
  - 1.A
  - 2.A
  - 2.B
  - 2.D
  - 4.A
tldr: Examines Philippines' progress on SDG 5 and 10, revealing policy achievements alongside implementation gaps that create complex, intersectional exclusion patterns for marginalized groups.
problem_and_motivation: Significant inequalities persist for women, persons with disabilities, and indigenous peoples despite robust legal frameworks. The intersection of multiple identities creates unique disadvantage patterns that single-issue approaches fail to address, requiring integrated policy responses for evidence-based inclusive development.
approach:
  - Mixed-methods design combining quantitative SDG indicator analysis with qualitative stakeholder interviews and focus groups.
  - Employs Shapley decomposition on merged FIES-LFS data to quantify factors contributing to inequality in working hours.
  - Uses descriptive and intersectional analytics, including National Demographic and Health Survey and Indigenous Peoples Household Survey data.
  - Conducted key informant interviews with government officials and civil society leaders.
  - Applied thematic coding to qualitative data from eight focus group discussions with affected populations.
findings:
  - num: Female disability prevalence is 15%, compared to 9% for males, with rates reaching 55% among women with no formal education.
  - num: Severe disability prevalence varies from 39% among those with no education to just 6% among college graduates.
  - num: Indigenous women's engagement in unpaid family work is more than three times higher than non-Indigenous counterparts.
  - Gender gaps in labor market participation are significantly larger among Indigenous Peoples and Muslim ethnic groups.
  - The GAD budget has become compliance-oriented rather than transformational, with widespread fund misuse and weak accountability.
  - num: Income inequality (Gini) decreased from 0.453 in 2015 to 0.406 in 2023, but the richest 20% still earn nearly 7.4 times more than the poorest 20%.
  - Persistent challenges remain in translating educational parity into economic empowerment and political representation for women.
key_figures_tables:
  - Table 1: Philippines WEF Global Gender Gap Index rankings → Performance has been volatile but remains the top performer in ASEAN.
  - Figure 1: Poverty incidence across basic sectors → Indigenous Peoples face the highest poverty at 32.4% in 2023.
  - Table 13: Select measures of per capita income inequality → Shows consistent but slow decline in Gini coefficient from 0.453 to 0.406.
  - Table 15: Inequality decomposition using household per capita income → Education creates meaningful income differences, but location and sex contribute little to between-group inequality.
  - Table 37: Disability prevalence by sex and ethnicity → Waray women experience the highest disability rate at 31%.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: GEDSI
    definition: Gender equality, disability and social inclusion - condition where all persons have equal rights, opportunities, and fair treatment regardless of various factors.
  - term: GAD Budget
    definition: Gender and Development budget - mandatory 5% allocation of agency budgets for gender programs.
  - term: Shapley Decomposition
    definition: Method to quantify the relative contributions of different factors to overall inequality patterns.
  - term: IPs
    definition: Indigenous Peoples - communities with ancestral domain rights and cultural traditions.
  - term: PWDs
    definition: Persons with disabilities - individuals with long-term physical, mental, intellectual, or sensory impairments.
critical_citations:
  - "[Crenshaw, 1989] — foundational for intersectional analysis framework."
  - "[UN Women, 2024] — provides SDG gender indicators for Philippines."
  - "[Pérez-Brito et al., 2024] — key data on Indigenous Peoples in Philippines."
  - "[World Bank, 2023] — documents persistent gender gaps in access to productive assets."
  - "[WHO, 2011] — ICF framework for understanding disability as interaction between impairments and environment."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: contextual
      justification: Profiles financial and social structures of young professionals' households.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: Describes GEDSI context that shapes financial behaviors of target users.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: contextual
      justification: Poverty and income inequality data imply cyclical financial pressures on marginalized groups.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: contextual
      justification: Income distribution patterns and poverty data provide background for spending cycles.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Contextualizes the policy and social landscape for financial management systems.
  contribution: This paper provides Odin with a foundational understanding of the demographic, cultural, and structural inequalities that shape Filipino young professionals' financial lives. It highlights the importance of culturally sensitive design by detailing specific financial practices, seasonal spending patterns driven by poverty and income volatility, and the lived realities of marginalized groups. The intersectional analysis directly justifies Odin's need to go beyond simple user profiling and incorporate contextual variables like ethnicity, disability, and geographic location into its algorithms for expense categorization, forecasting, and anomaly detection. The findings on GAD budget failures and data gaps inform Odin's design principles around user trust, data privacy, and the importance of generating actionable insights from available data.
  directly_justifies:
    - "Poverty concentration among specific groups (IPs, PWDs, women) justifies targeted financial product design and goal setting in Odin."
    - "Gender disparities in unpaid care work and labor force participation justify forecasting models that account for varying income stability."
    - "Statistical invisibility of marginalized groups justifies Odin's data enrichment and cold-start strategies."
    - "Income inequality patterns justify budget recommendation algorithms that prioritize savings and debt management for vulnerable users."
    - "The disconnect between educational attainment and economic opportunity justifies system design that supports career and financial advancement."
  limits:
    - "The paper focuses on macro-level policy and social structures, not on individual-level financial behaviors or PFMS usage."
    - "Data on income is at the household level, not individual, limiting direct translation to personal finance tracking."
    - "The analysis does not evaluate specific personal finance applications or their effectiveness."
  mapping_rationale: A systematic scan across all 12 functional domains identified the paper's primary relevance to the Filipino Cultural Context and Existing Systems domains. The paper's exhaustive data on Filipino demographics, poverty, inequality, and cultural practices provided high-contextual relevance to topics 1.A, 2.A, 2.B, and 2.D, as it describes the very environment in which Odin's users make financial decisions. It also provides contextual relevance for the landscape of existing systems by detailing the societal and structural problems that a PFMS like Odin must navigate. Topics related to algorithmic modules (e.g., forecasting, anomaly detection, budget recommendation) were considered and rejected because the paper does not discuss or evaluate computational techniques; its relevance is purely contextual, offering the socio-economic background that should inform those algorithms. The paper's discussion of data gaps and "statistical invisibility" is particularly relevant to Odin's cold-start and user profiling challenges. Overall, the paper provides critical background for understanding Odin's target users but offers no direct technical contributions to the system's algorithmic components.
limitations:
  - "The paper's focus on national-level data may not reflect the granular financial behavior needed for a PFMS. [unacknowledged]"
  - "The study does not evaluate the effectiveness of personal finance management tools or digital financial services."
  - "Qualitative data saturation may not capture the full range of experiences for highly marginalized intersectional subgroups."
  - "The study did not undergo formal Institutional Review Board (IRB) approval."
remember_this:
  - "Income inequality (Gini) decreased from 0.453 to 0.406 between 2015 and 2023."
  - "Female disability prevalence is 50% higher than male at 15% versus 10%."
  - "Indigenous women's unpaid family work is over three times higher than non-Indigenous."
  - "The GAD budget is compliance-oriented with weak accountability and widespread misuse."
  - "Data gaps create 'statistical invisibility' for Indigenous Peoples and other marginalized groups."
```