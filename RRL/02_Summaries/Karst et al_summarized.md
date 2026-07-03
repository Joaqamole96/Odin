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