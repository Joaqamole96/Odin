```yaml
paper_id: 10.1186/s40537-026-01464-y
designation: international-algorithm-specific
title: Predicting customer buying habits using convolutional neural network
authors: Lou, Z.; Wang, S.; Yu, X.; Song, W.
year: 2026
venue: Journal of Big Data
odin_topics:
  - 6.A
  - 6.B
  - 5.A
  - 5.C
  - 7.B
  - 3.A
tldr: A CNN with hybrid pooling predicts income tiers from demographic and behavioral data, then uses a probability matrix to recommend products, achieving 93.06% income prediction accuracy.
problem_and_motivation: Traditional models struggle with high-dimensional demographic data and non-linear relationships between demographics and behavior. This gap limits the accuracy of personalized retail and product recommendations. There is a need for a more effective method to capture latent spatial patterns in customer data.
approach:
  - Data was collected via a questionnaire from 980 participants covering demographics, shopping habits, and income.
  - Nominal features were converted to numerical values, missing values were imputed, and features were normalized to [0,1].
  - Normalized features were mapped to 20x10 grayscale images to enable CNN processing of spatial patterns.
  - A CNN with hybrid pooling layers (switching between max and average pooling during training) was used for income classification.
  - A purchase probability matrix was constructed from training data to model the likelihood of product category purchases per income tier.
findings:
  - num: The proposed CNN achieved 93.06% accuracy in predicting income levels.
  - num: The model attained precision of 92.95% and recall of 93.21% for income classification.
  - num: The method achieved a mean accuracy of 95% in product recommendation across six categories.
  - Hybrid pooling outperformed max and average pooling variants, improving accuracy by at least 1.5%.
  - The CNN with hybrid pooling demonstrated superior ROC curves compared to benchmark methods.
  - Statistical significance tests (p < 0.05) confirmed the superiority of the proposed model over baselines.
  - Job category, education level, and age were identified as the most important features for income prediction.
key_figures_tables:
  - Figure 1: Flowchart of the proposed three-step methodology → visualizes the data preprocessing, classification, and recommendation pipeline.
  - Figure 2: Architecture of the proposed CNN model with hybrid pooling → shows the two convolutional layers and hybrid pooling structure.
  - Table 5: Performance comparison of income prediction methods → demonstrates the proposed method's superior metrics across all categories.
  - Figure 5: Confusion matrices for income classification → highlights fewer misclassifications in the proposed model.
key_equations:
  - equation: S = {S_avg with probability p, S_max with probability 1-p}
    explanation: Defines the stochastic switching between average and max pooling.
  - equation: S_hybrid = p * S_avg + (1-p) * S_max
    explanation: Computes the final pooling output as a weighted combination.
  - equation: Loss = -Σ(w_i * y_i * log(p_i) + (1-y_i) * log(1-p_i))
    explanation: Weighted cross-entropy loss used to address class imbalance.
definitions:
  - term: CNN
    definition: Convolutional Neural Network, a deep learning model for processing grid-like data.
  - term: Hybrid Pooling
    definition: A pooling strategy that randomly selects between max and average pooling during training.
  - term: WCE
    definition: Weighted Cross-Entropy, a loss function that assigns penalties inversely proportional to class frequency.
  - term: RFM
    definition: Recency, Frequency, Monetary model for customer segmentation.
critical_citations:
  - "[Tong & Tanaka, 2019] — Introduces the hybrid pooling method used in this paper."
  - "[Chen et al., 2022] — A recent benchmark for salary prediction using Random Forest."
  - "[Vemulapati et al., 2023] — A benchmark using LSTM and BiLSTM for income prediction."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      relevance: high
      justification: Core contribution is predicting income as a proxy for financial capacity.
    - code: 6.B
      name: Forecasting Algorithms for Sequential Spending Data
      relevance: medium
      justification: Uses behavioral features for prediction; could be adapted for sequential spending.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      relevance: medium
      justification: Classifies individuals by income, a key behavioral grouping.
    - code: 5.C
      name: Classification Approaches for Financial Behavioral Profiles
      relevance: high
      justification: Proposes a novel CNN-based classification approach for income-based profiles.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      relevance: contextual
      justification: Provides a framework for product recommendation, similar to budget allocation.
    - code: 3.A
      name: Expense Categorization Frameworks
      relevance: low
      justification: Uses product categories, which could map to expense categories.
  contribution: "The paper introduces a CNN-based income classification model, which could inform Odin's expense forecasting module. The hybrid pooling strategy addresses class imbalance, relevant to Odin's diverse user base. The product recommendation matrix offers a framework for budget allocation or expense prediction. The feature importance analysis identifies demographic indicators that could enhance Odin's behavioral profiling."
  directly_justifies:
    - "A CNN with hybrid pooling can effectively classify financial behavior profiles from demographic data."
    - "Converting tabular user data to grayscale images enables spatial feature extraction for behavioral analysis."
    - "Weighted cross-entropy loss improves classification accuracy on imbalanced income data."
    - "The purchase probability matrix can model category-specific spending likelihood."
  limits:
    - "The dataset (N=980) is relatively small for deep learning, potentially limiting generalizability."
    - "The study was conducted on a regional population, which may not reflect Filipino spending patterns."
    - "The model does not incorporate sequential spending data, limiting its use for forecasting."
  mapping_rationale: "A systematic scan across all 12 functional domains and their associated topic codes was performed. The paper was flagged as relevant primarily to the 'Spending Forecasting' domain due to its focus on predicting income and, by extension, purchasing habits. This maps directly to topics 6.A and 6.B. The classification methodology is also highly relevant to 'Behavioral Profiling & Classification' (topics 5.A and 5.C), as it proposes a new approach for categorizing users by income. The product recommendation component is contextually relevant to 'Budget Recommendation' (topic 7.B) and the product categorization is tangentially related to 'Expense Categorization' (topic 3.A). The 'Existing Systems & Gaps' domain was considered but rejected as the paper's primary contribution is a novel method rather than a survey. Similarly, 'Filipino Cultural Context' was rejected as the data is not Filipino-specific. Overall, the paper is highly relevant to Odin's algorithmic design for forecasting and classification modules."
limitations:
  - "The sample size of 980 is relatively small for deep learning models, which may affect generalizability."
  - "The dataset is geographically and culturally specific, potentially limiting applicability to other regions like the Philippines."
  - "The study does not test the model on external, independent datasets, limiting external validation. [unacknowledged]"
  - "The feature set may lack granular cultural or micro-economic indicators that could influence buying choices. [unacknowledged]"
remember_this:
  - "A CNN with hybrid pooling achieved 93.06% accuracy in income prediction."
  - "Product recommendations had a mean accuracy of 95% across six categories."
  - "Job category, education, and age are the most important income predictors."
  - "Hybrid pooling improves generalization and reduces overfitting in CNNs."
  - "The model provides a scalable pipeline for real-time retail personalization."
```