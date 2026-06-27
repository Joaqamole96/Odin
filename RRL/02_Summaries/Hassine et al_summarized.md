```yaml
paper_id: 10.62345/jads.2025.14.3.1
designation: local-algorithm-specific
title: Inequality, Education and Occupational Change in the Philippines
authors: Belhaj Hassine, N.; Fernandez, F. C.; Lavin, B. A.
year: 2025
venue: Journal of Asian Development Studies
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
  - 5.C
  - 12.A
tldr: Slow growth in college-educated labor supply sustains high wage premiums, while shifts in occupational structure, particularly growth in middle-skill jobs from 2012-2016, have recently narrowed wage inequality.
problem_and_motivation: The Philippines has persistently high income inequality despite poverty reduction and economic growth. The relationship between education, employment structure, and wage inequality remains underexplored. This study analyzes how changes in skill supply and occupational composition have shaped wage distribution over two decades.
approach:
  - Data from Philippine Labor Force Survey (2002-2024), covering wage workers aged 15+.
  - Constructed an occupation crosswalk harmonizing PSOC 1992 and 2012 to create 22 consistent occupation codes.
  - Classified occupations into high-, middle-skill routine, middle-skill nonroutine, and low-skill categories.
  - Used Recentered Influence Function (RIF) regressions to estimate returns to education and occupation across wage quantiles.
  - Applied DiNardo-Fortin-Lemieux (DFL) reweighting to isolate the impact of occupational changes on wage distributions.
findings:
  - num: College wage premium declined from 88% in 2013 to 59% in 2024, but college graduates still earned 80% more than high school graduates.
  - num: Returns to college education and high-skill occupations rise monotonically across wage quantiles, with college coefficients increasing over time.
  - num: Real wages for non-college workers grew 32% from 2012-2024 versus 5% for college workers, narrowing inequality.
  - num: Middle-skill employment share grew by 3.6 percentage points from 2002-2016 but declined by 2.8 points from 2016-2024.
  - Occupational reallocation explains a significant share of non-college wage growth after 2012, particularly for men.
  - num: Youth college graduates (25-34) had 6.7% unemployment in 2024, higher than the 4.4% for non-college peers.
key_figures_tables:
  - "Figure 1: Income and wage Gini trends 2002-2024 → Inequality declined from 2012 onward, with wage Gini falling to 32% by 2024."
  - "Figure 5: College wage premium trend → Premium peaked at 88% in 2013, declined to 59% by 2024."
  - "Figure 8: Returns to education by quantile → College returns increase monotonically across income distribution, widening gaps."
  - "Table 1A: RIF regression on wage Gini → College education has positive and increasing effect on wage inequality over time."
key_equations:
  - equation: "f_{x_{t0}}(w) = ∫ f(w | x, t_w=t0) dF(x | t_x=t0)"
    explanation: "Observed wage density as joint distribution of wages and covariates."
  - equation: "f_{x_{t1}}(w) = ∫ f(w | x, t_w=t0) * ψ_x(x) dF(x | t_x=t0)"
    explanation: "Counterfactual wage density reweighting covariates from t0 to t1."
  - equation: "ψ̂_x = [Pr(t_x=t1 | x)/Pr(t_x=t0 | x)] * [Pr(t_x=t0)/Pr(t_x=t1)]"
    explanation: "Reweighting function estimated via logit model for DFL decomposition."
definitions:
  - term: RIF Regression
    definition: "Recentered Influence Function regression for unconditional quantile effects on wage distribution."
  - term: DFL Reweighting
    definition: "DiNardo-Fortin-Lemieux semiparametric method to decompose wage distribution changes."
  - term: PSOC
    definition: "Philippine Standard Occupational Classification, versions 1992 (ISCO-88) and 2012 (ISCO-08)."
  - term: LFS
    definition: "Labor Force Survey, quarterly nationwide household survey by Philippine Statistics Authority."
  - term: Wage Premium
    definition: "Percentage wage gap between college graduates and high school graduates, reflecting skill valuation."
critical_citations:
  - "[Acemoglu and Autor, 2011] — Framework for skill-task-occupation classification."
  - "[Firpo et al., 2018] — Methodological basis for RIF regression approach."
  - "[DiNardo et al., 1996] — Foundation for DFL decomposition technique."
  - "[Autor, 2019] — Framework for analyzing job polarization and wage inequality."
  - "[World Bank, 2022] — Comprehensive prior analysis of Philippine inequality drivers."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      relevance: medium
      justification: Provides wage and employment data for prime-age workers (25-54), including youth unemployment trends.
    - code: 1.B
      name: Financial Structure of Filipino Young Professionals
      relevance: medium
      justification: Documents wage distribution and returns to education, directly relevant to income structure.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      relevance: medium
      justification: Highlights unemployment and labor market outcomes shaping financial behavior.
    - code: 2.A
      name: Culturally Specific Financial Practices
      relevance: contextual
      justification: Context on labor market structure and wage inequality in Philippine context.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      relevance: low
      justification: Mentions COVID-19 cyclical disruption but not seasonal spending patterns.
    - code: 2.D
      name: Filipino Spending Cycles and "Occasions"
      relevance: low
      justification: Discusses cyclical labor market shifts, not spending cycles.
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      relevance: contextual
      justification: Provides macroeconomic context for personal finance system design.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      relevance: low
      justification: Identifies skills mismatch and occupational polarization as systemic gaps.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: high
      justification: Documents wage premium persistence and occupational shifts that differentiate worker profiles.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Uses occupational and education classifications that inform behavioral profile segmentation.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      relevance: high
      justification: Provides RIF regression and DFL decomposition methodologies applicable to system evaluation.
  contribution: "This paper provides empirical methods (RIF regression, DFL decomposition) applicable to evaluating Odin's algorithmic modules. Its analysis of education and occupational returns offers a framework for segmenting user financial profiles based on income trajectories. The findings on wage premium persistence inform Odin's expense categorization and forecasting modules. The documentation of occupational shifts and skill supply constraints justifies behavioral profiling approaches. The paper's methodological rigor supports system evaluation frameworks for algorithmic modules."
  directly_justifies:
    - "RIF regression methods can evaluate inequality impacts of algorithmic modules."
    - "Occupational classification informs behavioral profile segmentation for PFMS."
    - "Wage premium trends provide baseline for income-based user segmentation."
    - "DFL decomposition methods apply to counterfactual evaluation of financial advice."
  limits:
    - "Focus on wage workers excludes self-employed and informal sector, limiting generalizability to all Filipino workers."
    - "Paper does not address individual-level financial behavior or spending patterns."
    - "Analysis aggregates to 22 occupation codes, which may oversimplify occupational diversity."
    - "DFL decomposition holds wages within occupations fixed, abstracting from within-occupation wage dynamics."
  mapping_rationale: "Systematic scan across all 12 functional domains and 38 topic codes flagged the following as relevant: Filipino Cultural Context (2.A contextual, 2.B low, 2.D low) for the Philippine-specific labor market analysis; Existing Systems & Gaps (4.A contextual, 4.B low) for identifying skills mismatch; Behavioral Profiling (5.A high, 5.C high) as the paper directly uses occupational and education classifications to differentiate worker types; and System Evaluation (12.A high) for its RIF regression and DFL decomposition methodologies. Domains on expense categorization (3.A-3.C), spending forecasting (6.A-6.B), budget recommendation (7.A-7.D), anomaly detection (8.A-8.C), mobile design (9.A-9.B), data privacy (10.A-10.B), user retention (11.A-11.B), savings and debt (13.A-13.C) were considered but rejected as the paper does not address these PFMS-specific functions. The paper is highly relevant methodologically for evaluating algorithmic modules and informing user segmentation, but does not directly address personal finance system design. Its empirical framework for analyzing inequality and occupational shifts provides foundation for behavioral profiling and evaluation modules."
limitations:
  - "Wage data only available from 2002 onward, limiting historical context."
  - "Analysis excludes non-wage workers (self-employed, family workers), missing significant portion of workforce."
  - "LFS occupational classifications changed in 2016, requiring crosswalk that may introduce harmonization errors."
  - "Does not explicitly examine within-occupation wage heterogeneity beyond education grouping."
  - "COVID-19 pandemic effects may confound recent structural trend identification. [unacknowledged]"
remember_this:
  - "College wage premium declined to 59% by 2024 from 88% in 2013."
  - "Non-college wages grew 32% from 2012-2024, outpacing college-educated workers."
  - "Middle-skill employment expanded from 2002-2016 but declined after 2016."
  - "Occupational reallocation explains non-college wage growth after 2012."
  - "Young college graduates face 6.7% unemployment, higher than less-educated peers."
```