# Topic Registry - 5.C.I

---

## I--Balbal_&_Birant_2026

### Description

Explains that supervised classification is appropriate for customer segment classification when the goal is to assign customers to predefined categories using features from transactional data.
- Learning Expert-Defined Mapping: Proposes a deep learning approach (RFM-Net) where labels are generated using rule-based logic from RFM scores and used as supervised ground truth, employing learning an expert-defined mapping rather than discovering a new segmentation structure.
- Classification Over Clustering: Contrasts the methodology with clustering-based algorithms, which face challenges in fully capturing nonlinear relationships and can lead to suboptimal segmentation outcomes.

---

## I--Harris_&_Austin_2024

### Description

Explains that supervised learning, which relies on labeled datasets, is effective for applications like customer segmentation and credit scoring because it uses historical data to classify information and predict outcomes, aligning with a need to assign users to predefined categories.
- Criteria for Approach Selection: Indicates that the choice between supervised and unsupervised learning is heavily influenced by the nature of the problem, data availability, and desired outcomes, emphasizing that supervised learning is appropriate for tasks with clear, predefined outcomes.
- Role of Labeled Data: Contrasts supervised learning's requirement for a well-defined target variable with unsupervised learning's focus on exploring data without constraints, reinforcing that classification (supervised) is necessary when profiles are fixed and known.

---

## I--Machireddy_2023

### Description

Explains that supervised classification should be chosen over clustering when a bank has predefined criteria or definitions for vulnerability, such as a rule-based system based on debt-to-income ratio and savings thresholds, which aligns with the need for fixed profile taxonomies.
- Supervised Learning Requirements: Details that supervised learning requires historical data labeled with outcomes (e.g., who defaulted) to train a model to classify new customers into predetermined buckets like "at-risk" or "not at-risk," directly addressing the task of assigning users to specified categories.
- Clustering vs. Classification Context: Contrasts the two approaches by noting that clustering (unsupervised learning) identifies naturally occurring groups when the segments are defined in an exploratory fashion, whereas classification is suitable when definitions of vulnerability already exist.

---

## I--Mehta_et-al_2025

### Description

Explains that clustering is typically considered an unsupervised learning task where grouping is based on a pre-specified similarity function, which contrasts with supervised classification where target variables (predefined profiles/categories) guide the learning.
- Applying Supervised Similarity: Suggests applying supervised similarity learning when pre-existing labels are available, such as fixed ratings, fund categories, or client segments, which aligns with the need for assigning users to predefined profiles.
- Using Domain Knowledge Taxonomies: Notes that supervised similarity uses known equivalences, like product taxonomies or analyst coverage, which serve as 'weak labels' to shape embeddings, thereby addressing the use of existing domain knowledge for profile definition.

---

## I--Rabinovich_et-al_2025

### Description

Proposes a novel framework for identifying latent profiles of financial mindset and behavior by modeling nonlinear interactions across multiple psychometric domains, moving beyond conventional segmentation.
- Uncovers Recurring Profiles: Uncovers recurring psychologically grounded financial profiles that generalize across populations and show strong associations with life satisfaction, psychological well-being, and financial health.
- Presents Unsupervised Framework: Presents a two-stage unsupervised framework for behavioral profiling using high-dimensional psychometric data, contrasting with the user's focus on supervised classification for predefined profiles.

---

## I--Yachamaneni_et-al_2025

### Description

Explains that traditional customer profiling methods in finance rely heavily on supervised learning, which requires large labeled datasets for classification.
- Supervised vs. Unsupervised Evaluation: Compares supervised classification and unsupervised clustering by evaluating performance metrics for both methods on downstream tasks like creditworthiness assessment and churn prediction.
- Classification for Fixed Outcomes: Discusses using supervised learning algorithms like XGBoost for classification assignments (credit risk assessment and churn prediction), which are typically fixed outcomes, in contrast to clustering for profile discovery.

---

## I--Yang_et-al_2024

### Description

Explains the application of supervised learning for pricing models to enhance customer identification and targeting when constructing customer feature systems, suggesting a classification approach when categories are predefined.
- Customer Feature Systems: Details the construction of customer feature systems using attributes like debit and credit card transactions, loan applications, and online behavior, which implies a process of assigning users to established profiles based on these features.
- AI for Customer Profiling: Discusses leveraging AI to accurately profile customers, boost consumption, and improve price management, which aligns with the goal of assigning users to predefined behavioral profiles for strategic purposes.
