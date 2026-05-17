# A User Profile System for the Finance Platform of Commerce

## Metadata

```yaml
---
paper_id: "10.1145/3718391.3718436"
designation: international
title: "A User Profile System for the Finance Platform of Commerce"
authors: "Hu, Z.; Qiu, Y.; Hu, S.; Cheng, Z.; Qiu, S."
year: 2024
venue: "2024 the 12th International Conference on Information Technology (ICIT)"
odin_topics: ["4.A", "5.A", "5.C"]
shorthand_tags: ["/profiling-role", "/pfms-intelligent-features", "/classification-vs-clustering", "/classifier-candidates", "/profile-dimensions"]
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[X]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---
```

## TL;DR

User profiling system for finance platforms integrates internal and external data to enable precise marketing, risk control, and decision-making via individual/group profiles, behavior trends, and tag management.

## Problem and Motivation

Web information is too general to solve individual user needs, and enterprises require refined operations and precision marketing using big data. Financial institutions face product homogeneity, declining customer loyalty, and rising churn, making user profiling a critical tool for understanding customers comprehensively. Prior work lacked a systematic user profile model that integrates multiple data sources and mining techniques specifically for finance platforms.

## Approach

- **Data acquisition**: Combines explicit (manual input) and implicit (logging interactions, behavior analysis) methods.
- **Data processing**: Applies word segmentation, data filtering, and normalization to standardize raw data.
- **Tag selection**: Uses fact tags (statistical, e.g., purchase frequency) and model tags (derived for business problems) with subjective/objective weighting methods.
- **User profile model**: Four-layer architecture: Data Collection, Data Storage, Middle (processing & analytics), Data Visualization.
- **System modules**: User Profile (individuals, behavior trends), User Group Profile (group analysis, trends), Tag Information (tag lists and management).
- **Sample grouping algorithm**: K-means clustering groups users by shared characteristics via centroid iteration.

## Findings

- **User profiling significantly improves customer satisfaction and loyalty in financial institutions.**
- The system enables precise marketing, risk control, and informed decision-making by providing comprehensive user behavior and preference insights.
- Cross-industry data integration (breaking information exchange barriers) creates a virtuous cycle that enriches profiles and improves model accuracy.
- K-means clustering effectively segments users into K groups based on distance to centroids, supporting targeted recommendations and analysis.

## Key Figures and Tables

- Figure 1: User Profile Model → Four-layer architecture from data collection to visualization.
- Figure 2: System functionalities → Three modules (User Profile, User Group Profile, Tag Information) with sub-functions.
- Table 1: User characteristics → Lists basic, financial, working, and transaction data fields.

## Key Equations

$$uw_{ij} = tf_{ij} \times idf_i$$
*Term weight equals term frequency times inverse document frequency.*

$$idf_i = \log \frac{\#documents\ in\ collection}{\#documents\ containing\ term\ i}$$
*Rare terms get higher weight; common terms get lower weight.*

$$similarity(c_j, d_k) = c_j \circ d_k = \sum_{i=1}^{n} w_{ij} \times d_{jk}$$
*Similarity between concept and document is the dot product of their weight vectors.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| User profile | A structured representation of a user’s characteristics, behavior, and preferences. |
| K-means clustering | Unsupervised algorithm that partitions users into K groups by minimizing distance to cluster centroids. |
| Fact tag | Tag derived directly from statistical analysis of raw data (e.g., purchase frequency). |
| Model tag | Tag created by associating fact tags with business problems for selection models. |
| Explicit acquisition | User manually provides information (high quality, requires active engagement). |
| Implicit acquisition | System transparently logs user interactions and behavior patterns (richer data). |

## Critical Citations

- [Armstrong et al., 1995] — First user profile system (WebWatcher) shifting from individual to group user modeling.
- [Chen et al., 2021] — Multi-model approach using classification algorithms for user portrait generation from search engine data.

## Relevance to Odin

**Topics:**

4.A — Landscape of Existing Personal Finance Systems

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

**Contribution to Odin:**

This paper provides a foundational system architecture for user profiling that directly informs Odin’s behavioral profiling module. The distinction between fact tags (statistical) and model tags (business-derived) justifies Odin’s two-stage approach: raw spending statistics → behavioral classification. The four-layer model (collection, storage, middle, visualization) offers a template for Odin’s backend design, particularly the middle layer where ML algorithms (including clustering) process user data. Although the paper targets enterprise finance platforms, its K-means grouping demonstration validates unsupervised clustering as a viable cold-start classification method for Odin’s initial user segmentation before supervised labels accumulate.

**Directly justifies:**

- “User profiling systems integrate internal and external data sources to enable precise marketing, risk control, and decision-making in financial platforms.”
- “K-means clustering groups users with similar characteristics without requiring labeled training data, making it suitable for cold-start user segmentation.”
- “Fact tags are derived from statistical analysis of raw data (e.g., transaction frequency), while model tags are constructed by associating fact tags with business problems.”
- “The four-layer user profile architecture (Data Collection, Storage, Middle, Visualization) separates concerns between raw data management and algorithmic processing.”

**Limits of relevance:**

- Paper describes an enterprise finance platform for commerce, not a personal budget management system for individuals.
- All authors and case context are Chinese; Filipino cultural and financial structures not addressed.
- No empirical evaluation of the proposed system — no accuracy, retention, or usability metrics.
- K-means is presented as a sample algorithm without comparison to alternatives (e.g., hierarchical, DBSCAN) or performance tradeoffs.

## Limitations

- No experimental validation or quantitative performance metrics for the proposed system. [unacknowledged]
- Focuses on precision marketing and risk control for enterprises, not personal financial management or user budgeting behavior.
- Chinese regulatory and financial context may not generalize to the Philippines (e.g., data sharing policies, banking infrastructure).
- K-means grouping example lacks evaluation of optimal K, convergence criteria, or handling of mixed data types.
- Does not address profile dynamics over time (concept drift) or cold-start scenarios for new users. [unacknowledged]

## Remember This

- 🔑 User profiling uses fact tags (statistical) + model tags (business logic) — separates raw data from classification.
- 📌 K-means clustering groups users without labels — useful for Odin’s cold-start profiling.
- 💡 Four-layer architecture (Collection → Storage → Middle → Visualization) separates data pipeline from ML logic.
- ⚠️ No empirical validation — the system design is conceptual, not performance-tested.
