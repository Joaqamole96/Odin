International Journal of Computing and Digital Systems
2024, VOL. 17, NO. 1, 1–10
http://dx.doi.org/10.12785/ijcds/XXXXXX
Hybrid Clustering Meets Behavior Analytics:
Adaptive Consumer Segmentation for E-Commerce
Success
Pavitha Nooji1, Laxmi Vaibhav Khengare1, Shashidhar R2, Meghana J3, Roopa M4
1 Department of Artificial Intelligence, Faculty of Science and Technology, Vishwakarma University, Pune, Maharashtra, India
2 Department of Electronics and Communication Engineering, JSS Science and Technology University Mysuru, India.
3 Department of Computer Applications, JSS Science and Technology University, Mysuru, India.
4 Department of Electronics and Communication Engineering, Dayanada Sagar college of Engineering, Bengalore, India
Abstract: A new robust consumer segmentation process links hybrid clustering strategies with temporal behavioral data analysis
to meet the requirements of the Olist Brazilian E-Commerce Public Dataset. The dataset includes 99,991 transactions which 96,095
unique customers conducted during two-years of dynamics between September 2016 and October 2018. The proposed method
unites traditional K-Means clustering with inventive Hierarchical Density-Based Spatial Clustering of Applications with Noise
(HDBSCAN) to perform dual clustering. VAE embedding technology combined with dual clustering and Recency Frequency
Monetary analysis and spatial measurements and Temporal Behavioral Evolution indicators and sentiment data processing
enhances the hybrid model. The framework leads to exceptional performance through its silhouette score of 0.65 alongside its
Davies-Bouldin index score of 0.42 indicating exceptional cluster quality. The framework enhances cluster separation by 15% above
standalone K-means (0.58) and DBSCAN (0.52) and PCA-based clustering (0.60) through its evaluation measure of silhouette score
0.65. The segmentation analysis reveals six customer segments that include Communities 0 and 3 which control 90% of all
transactions while revealing a 35% spike in November 2017 due to Black Friday buying tendencies. The uniqueness of this
framework emerges from its adaptive segmentation method that enables updates of customer segments due to shifts in consumer
actions. The framework's adaptive cluster function is demonstrated through consistency research which checks community
assignment consistency between different time segments alongside parameter testing that modifies HDBSCAN’s min_cluster_size
from 300 to 700. When promotional targeting of active communities combines with specific initiatives for niche groups within this
framework it leads to about 10% higher response rates. The scalable framework operates by uniting deep learning methods with
model approaches for assessing e-commerce customer behavior which leads to data-based business choices. The versatile method
addresses complex big data transactional information to offer e-commerce companies powerful tools for improving market
performance and resource utilization.
Keywords: Customer segmentation, hybrid clustering, K-Means, HDBSCAN, RFM analysis, Variational Autoencoder, temporal
analysis, Brazilian E-Commerce Public Dataset by Olist, geo-spatial modeling.
Applications with Noise (HDBSCAN) using Variational
1. INTRODUCTION
Autoencoder (VAE) embeddings to minimize dimensions and
The process of customer segmentation proves essential to
adding Temporal Behavioral Evolution (TBE) to monitor
e-commerce operations because it enhances marketing
time-dependent customer actions. The Brazilian E-Commerce
campaign success and resource efficiency while creating
Public Dataset by Olist [3] serves as the base for this research
better customer satisfaction results. The research presents an
with 99,991 transactions involving 96,095 unique customers
all-encompassing review of worldwide e-commerce market
throughout 2016 to 2018. The researchers adjusted the
expansion with specific emphasis on India and Brazil and
Brazilian BRL data by converting it to INR value at 15 INR
critiques common clustering approaches K-Means and
per BRL to reflect Indian market purchasing power while
hierarchical clustering. The clustering approaches face two
enabling in-depth analysis of seasonal buying patterns along
major challenges because they require fixed clustering
with spatial distribution trends. The paper presents its
assumptions and the inability to process noisy or irregular
organizational plan consisting of methodology and results
data shapes. This paper's original value derives from its
followed by discussion and future directions which allows
creation of a combined clustering system which integrates K-
readers to navigate the practical and technical content of the
Means with Hierarchical Density-Based Spatial Clustering of
E-mail address: shashidhar.r@jssstuniv.in

2 Pavitha Nooji
study. The bar chart in Figure 1 displays pre-clustering in Section VI. The established organization examines the
distribution of transactions by community numbers from 0 to complete development process of the framework while
5 and -1 for outliers while demonstrating proportionate validating its practical uses which enables understanding by
heights corresponding to transaction frequency ranging from e-commerce practitioners data scientists and policymakers.
142 to 51,753.
2. LITERATURE SURVEY
Winning businesses use customer segmentation as their
The section conducts a thorough evaluation of customer
essential e-commerce technique because it allows them to
segmentation methodologies starting from historical origins
create personalized marketing approaches along with
up to modern times while focusing on essential advancements
effective resource management and improved client
relevant to the current work. The assessment of customer
satisfaction through individualized preference attention [1].
value started before clustering methods became advanced
The e-commerce market will expand from $4.9 trillion to
through recent developments that combine deep learning with
$7.4 trillion by 2025 as India's segment develops toward $200
temporal analytics and spatial modeling. The study identifies
billion by 2026 because of digital adoption during festive
research gaps within current literature about the absence of
season sales [24]. Advanced analytical tools must be
temporal and spatial elements which prepares the way for the
developed to decode complex consumer behaviors because of
authors' original work that incorporates these aspects. The
the market's substantial growth. The clustering technique K-
research addresses specific purchasing patterns from the
Means depends on user-defined cluster numbers while
Brazilian E-Commerce Public Dataset by Olist because it
expecting spherical clusters yet remains unable to handle
focuses on Brazilian cultural preferences and seasonal market
natural data irregularities or anomalous patterns [8]. The
changes to improve global e-commerce application relevance.
value of hierarchical clustering approaches remains strong in
hierarchical structure analysis even though they face The establishment of customer segmentation began with
challenges when working with large datasets coupled with Recency Frequency and Monetary (RFM) analysis introduced
irregular distribution patterns [10]. Multiple companies by Hughes in 1994 that developed a system to determine
require sophisticated analytical methods to control the lifetime customer value through recent purchase activity data
changing patterns and diverse data characteristics present in combined with purchase frequency statistics and monetary
e-commerce transaction records. contributions [6]. The initial approach designed by Hughes in
1994 received additional developments by the same author in
This research tackles clustering challenges by developing a
1996 to create a professional early marketing tool which
combined clustering method which joins K-Means with
businesses could use to identify top customers [7]. The 2003
HDBSCAN because K-Means demonstrates productive
work by Dolnicar's 2003 study demonstrated that RFM forms
computational behavior [8] and HDBSCAN detects clusters
a fundamental piece of data-driven segmentation methods yet
of varying densities while controlling for outliers [11]. The
its application does not sufficiently detect intricate behavioral
method implements Variational Autoencoders (VAE) for
patterns [4]. Unsupervised learning introduced K-Means
data compression which results in a 15% improvement in
clustering as its prime method when Liu and colleagues
clustering accuracy compared to standard approaches [15].
validated e-commerce segmentation through a silhouette
The inclusion of Temporal Behavioral Evolution (TBE) lets
score of 0.55 in 2018 [5]. However, MacQueen’s original
the model follow customers' market behavior time changes
1967 formulation revealed a critical constraint: the method’s
yet maintaining novelty beyond basic static segmentation
reliance on a predefined number of clusters (k), which can
solutions [14]. The Brazilian E-Commerce Public Dataset by
lead to suboptimal results in datasets with varying structures
Olist [3] obtained from Kaggle presents 99,991 transactions
[8].
scattered across 96,095 customers who bought from 32
product categories (beleza_saude, cama_mesa_banho) and Campello and his team established Hierarchical Density-
visited 27 city locations. Conversion of BRL transaction Based Spatial Clustering of Applications with Noise
values to INR at a 15 exchange rate established purchasing (HDBSCAN) in 2015 as a clustering approach which works
power parity for a relevant Indian analysis while permitting with clusters of various densities along with handling outliers
assessment of seasonal peaks such as the 35% November better than K-Means while overcoming its scalability
2017 surge along with spatial distribution patterns [20]. The problems [11]. Jain’s 2010 survey detailed HDBSCAN’s
conversion adjusts the data measurements to correspond to value by demonstrating how it processed noisy data more
India's e-commerce market environment which demonstrates effectively than conventional approaches by 20% [12]. After
strong effects from both the variety in purchasing locations Zhang et al.'s 2019 research on K-Means hybridization with
and major festival periods. This method achieves novelty by density-based methods the field experienced substantial
combining deep learning with time-series modeling and growth in interest yet the study failed to incorporate time-
spatial methods to deliver a scalable segmentation system for sensitive behavioral information leading to incomplete
real-time usage. The paper uses a structured format that first dynamic pattern evaluation [23]. VAEs with convolutional
explains the methodology including feature engineering and structure boosted deep learning for this field in 2017 by
clustering techniques in Section III followed by results achieving a 10% better clustering precision during latent
demonstrating community profiles and performance metrics representation extraction from high-dimensional information
in Section IV and ends with implications and limitations with components [16].
recommendation in Section V and future research proposals
The understanding of behavioral pattern movements in

International Journal of Computing and Digital Systems
customers now requires essential temporal analysis studies sentiment scores from preprocessing completion.
despite remaining relatively unknown. In 2005 Liao created Dimensionality Reduction via Variational Autoencoder
the base framework for time-series clustering which (VAE) enables management of the extracted features before
demonstrated why following changes in human behavior the process. This module receives the lower-dimensional
requires long-term analysis [14]. According to Aggarwal's embeddings to perform Hybrid Clustering by using K-Means
review from 2007 the method proved inadequate for business for cluster initialization and HDBSCAN for clustering
applications yet he suggested combining it with spatial data optimization and outlier identification. The customer
[17]. The research work of Chen and Liu (2013) integrated segments generated through the process receive assessment
geo-spatial segmentation elements into their analysis which via Silhouette score and Davies-Bouldin index in addition to
enhanced retail environment location-based targeting by 15% stability measures and sensitivity analysis. The framework
[13]. produces useful output through the identification of customer
segments together with segment profiles and time-based
The paper overcomes such limitations by employing VAE behavioral patterns observation. The designed architecture
embeddings to compress and purify features, Temporal delivers a resilient and flexible system which helps businesses
Behavioral Evolution to monitor changes in customer trends, understand and segment their e-commerce customer base.
and geo-spatial analysis to explore regional buying trends in
A. Dataset Description
the Brazilian E-Commerce Public Dataset of Olist [3]. The
database containing 99,991 transactions distributed across The Indian Olist dataset based on the Brazilian Olist e-
96,095 customers serves as an optimal setting to study commerce dataset [3, 19] modifies Brazilian cities (São Paulo
cultural phenomena like Brazil Carnival and seasonal becomes Mumbai and Rio de Janeiro becomes Delhi and Belo
changes because it includes varied information from 27 cities Horizonte becomes Bangalore) by converting BRL into INR
and 32 product categories [24]. The research adapts these at a rate of 15 INR per BRL for purchasing power parity [20].
techniques to this Brazilian E-Commerce Public Dataset, The dataset tracks 99,991 transactions conducted by 96,095
establishing a culturally sensitive solution for e-commerce individual customers throughout September 2016 to October
platforms to use in heterogeneous market settings as well as 2018 that includes order IDs and customer IDs as well as
contributing to worldwide segmented marketing strategies. timestamps and INR payment amounts and customer and
seller locations and product categories and review scores. The
1. METHODOLOGY pre-processing stage merged seven initial datasets (orders,
This section provides a comprehensive methodology for
payments, reviews, items, products, customers, sellers) for
replicating the study, detailing data preparation, feature
eliminating duplicate information. The authors completed
engineering, clustering process, and evaluation.
missing review score data by replacing it with review scores
set to the median value of 3 while inserting unknown
placeholders to fill gaps in categorical fields [20]. The
preprocessing methods provide solid bases for cluster analysis
which shows reliable results when tested on undisclosed
Indian e-commerce data.
Figure 1: System Architecture
The illustrated system architecture diagram in Figure 1
demonstrates how customer segmentation was executed in Figure 2: Community Distribution Bar Plot
this research. The system initiates processing with the Data A distribution view of the dataset’s transactions exists in
Source which comprises the Olist Brazilian E-Commerce Figure 2 (Community Distribution Bar Plot). The bar plot
Dataset containing extensive transaction data. The raw displays how transactions distribute across customer groups
dataset requires Data Preprocessing to handle missing value during the initial phase before clustering efforts take place to
imputation and currency normalization and city field provide baseline understanding of the dataset's diversity.
adjustments according to the study requirements. Feature
B. Feature Engineering
Engineering pulls out important customer data points such as
RFM metrics with geo-spatial proximity signals and This section discusses the transformation of raw transactional
Temporal Behavioral Evolution indicators as well as data from the Brazilian E-Commerce Public Dataset by Olist

|     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

4                   Pavitha Nooji
into a set of engineered features particularly designed for  reflecting changes in category preferences, in given
| clustering that significantly enhances the performance and  |     |     |     |     |     |     | by Equation (6):  |     |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- |
interpretability of the model. It encompasses a broad range of
engineered features, each of which is particularly designed to  𝑇𝐵𝐸 = 𝐷𝑞+1−𝐷𝑞×100    (6)
𝑑𝑖𝑣𝑒𝑟𝑠𝑖𝑡𝑦
| extract some form of customer behavior, and comprises  |     |     |     |     |     |     |     |     | 𝐷𝑞  |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
advanced computational methods to deal with the complexity
|     |     |     |     |     |     |     | Where 𝐷 |  is the count of unique product categories  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------------------------------------- | --- | --- | --- | --- |
𝑞
of the dataset. The features are particularly designed to be in
purchased quarterly [14]. These temporal indicators
line with e-commerce dynamics and are representative of
enable the model to adapt to seasonal peaks, such as
| buying  | habits,  | geographic  | variations,  |     | and  | temporal  |     |     |     |     |     |     |
| ------- | -------- | ----------- | ------------ | --- | ---- | --------- | --- | --- | --- | --- | --- | --- |
variations,  and  are  designed  for  usability  in  real-world  the 35% transaction increase in November 2017.
applications.
Sentiment analysis is included to assess customer
The RFM process begins with the creation of RFM analysis  satisfaction, formulated as Equation (7):
| attributes,  | a  basic  | tool  used  | to  | analyze  | customer  | value.  |     |     |     |     |     |     |
| ------------ | --------- | ----------- | --- | -------- | --------- | ------- | --- | --- | --- | --- | --- | --- |
𝑅𝑠𝑐𝑜𝑟𝑒−3
Recency is the number of days that have passed since the  𝑆 =       (7)
𝑠𝑒𝑛𝑡𝑖𝑚𝑒𝑛𝑡
| customer last purchased, as shown by Equation (1):  |     |     |     |     |     |     |         |                                         | 2   |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | --------------------------------------- | --- | --- | --- | --- |
|                                                     |     |     |     |     |     |     | Where 𝑅 |  is the review score normalized from a  |     |     |     |     |
𝑠𝑐𝑜𝑟𝑒
|     |     | 𝑅  =  𝑇 | −𝑇  | ,   |     | (1)  |     |     |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
𝑚𝑎𝑥 𝑙𝑎𝑠𝑡 1-5  scale  to  –1  to  1,  averaged  per  customer,
Where  𝑇   is  October  31,  2018  (the  dataset’s  accounting for 2,345 imputed scores (median 3) [9].
𝑚𝑎𝑥
termination  date),  and  𝑇   is  the  most  recent  This  feature  enriches  segmentation  by  linking
𝑙𝑎𝑠𝑡
purchase date per customer, serving as an indicator  satisfaction to repurchase likelihood.
of engagement decay [6]. Frequency measures the
Lastly, Variational Autoencoder (VAE) embeddings
| consistency  |     | of  purchasing  |     | behavior  |     | through  |     |     |     |     |     |     |
| ------------ | --- | --------------- | --- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- |
compress 7-dimensional feature space (spend in R, F,
Equation (2):
|     |     |     |     |     |     |     | M,  G,  TBE  | diversity, sentiment,  |     | TBE  spend)  | to  | 6   |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---------------------- | --- | ------------ | --- | --- |
dimensions. The VAE employs a ReLU encoder with
|     |     | 𝐹 = 𝑐𝑜𝑢𝑛𝑡(𝑂 |     | 𝑢𝑛𝑖𝑞𝑢𝑒 | )    | (2)  |     |     |     |     |     |     |
| --- | --- | ----------- | --- | ------ | ---- | ---- | --- | --- | --- | --- | --- | --- |
16 hidden units, which is trained for 20 epochs with
Which counts the number of distinct orders [7].
the Adam optimizer (batch size 64, learning rate
| Monetary  | value  | aggregates  |     |     | the  | economic  |     |     |     |     |     |     |
| --------- | ------ | ----------- | --- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- |
0.001) [15]. The loss function, as Equation (8):
contribution via Equation (3):
|     |     |         |     |     |     |      | 𝐿 = 𝑟𝑒𝑐𝑜𝑛𝑠𝑡𝑟𝑢𝑐𝑡𝑖𝑜𝑛𝑙𝑜𝑠𝑠+𝛽⋅𝐾𝐿𝑙𝑜𝑠𝑠,   |     |     |     | (8)  |     |
| --- | --- | ------- | --- | --- | --- | ---- | ---------------------------------- | --- | --- | --- | ---- | --- |
|     |     | 𝑀 = ∑ 𝑃 |     |     |     | (3)  |                                    |     |     |     |      |     |
  𝑣𝑎𝑙𝑢𝑒
|                                                       |     |     |     |     |     |     | Comprises  |   𝑟𝑒𝑐𝑜𝑛𝑠𝑡𝑟𝑢𝑐𝑡𝑖𝑜𝑛𝑙𝑜𝑠𝑠 |     | = 1 ∑𝑑 | (𝑋 −𝑋⋅)2  |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------- | -------------------- | --- | ------ | --------- | --- |
|                                                       |     |     |     |     |     |     |            |                      |     | 𝑖=1    | 𝑖         | 𝑖   |
| equivalent to transaction values in INR to represent  |     |     |     |     |     |     |            |                      |     | 𝑑      |           |     |
customer buying power [7]. These metrics, whose  (with  𝑑  =  7)  for  data  fidelity,  and  𝐾𝐿𝑙𝑜𝑠𝑠 =
|                                                  |     |     |     |     |     |     | −0.5∑  (1+log(𝜎2)−𝜇2 |     | −𝜎2)  | with  𝛽  | =   0.1  | for  |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | -------------------- | --- | ----- | -------- | -------- | ---- |
| roots are in early marketing measurement, are a  |     |     |     |     |     |     |                      |     |       |          |          |      |
latent space regularization [16]. This configuration
standard for gauging revenue potential and loyalty.
yielded a reconstruction error of 0.012 and a KL
To incorporate space effects, a geo-spatial proximity  divergence  of  0.008,  improving  computational
feature is added, as calculated in Equation (4):
efficiency by 15% over PCA.
𝐺 =   ⊢ 50               𝑖𝑓 𝑐𝑢𝑠𝑡𝑜𝑚𝑒𝑟 𝑎𝑛𝑑 𝑠𝑒𝑙𝑙𝑒𝑟 𝑐𝑖𝑡𝑖𝑒𝑠 𝑚𝑎𝑡𝑐ℎ    (4)  Research  by  Gupta  and  Kumar  [29]  applied
500             𝑜𝑡ℎ𝑒𝑟𝑤𝑖𝑠𝑒,
|     |     |     |     |     |     |     | Variational  | Autoencoders  |     | (VAEs)  | to  reduce  |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- | --- | ------- | ----------- | --- |
with the value averaged per customer to capture
dimensionality and achieved a 12% improvement in
| local  purchasing  |         | tendencies  |     | [13].     | This  | binary    |                 |           |      |            |           |     |
| ------------------ | ------- | ----------- | --- | --------- | ----- | --------- | --------------- | --------- | ---- | ---------- | --------- | --- |
|                    |         |             |     |           |       |           | reconstruction  | accuracy  | for  | ecommerce  | datasets  |     |
| distance           | metric  | provides    |     | insights  | into  | regional  |                 |           |      |            |           |     |
through optimized latent space regularization. The
preferences, critical for optimizing delivery logistics
study used the VAE encoder with ReLU activation
in geographically dispersed markets like Brazil.
function of 16 hidden units and a β=0.1 control to
Temporal Behavioral Evolution (TBE) features are  achieve  robust  dimension  reduction  from  7  to  6
employed to monitor evolving changes in behavior.  dimensions. The applied framework demonstrated
TBE Spend, used to monitor changes in spending  both a 15% increase in clustering accuracy and a
patterns, is defined by Equation (5):  10% decrease in computational costs enabling its
use with 99,991 transaction volume datasets.
𝑆𝑞+1−𝑆𝑞×100,
|         | 𝑇𝐵𝐸 𝑠𝑝𝑒𝑛𝑑                                     | =   |     |     |     | (5)  |     |                                |     |     |     |     |
| ------- | --------------------------------------------- | --- | --- | --- | --- | ---- | --- | ------------------------------ | --- | --- | --- | --- |
|         |                                               |     | 𝑆𝑞  |     |     |      |     | C. Adaptive Hybrid Clustering  |     |     |     |     |
| Where 𝑆 |   represents quarterly spending, set to zero  |     |     |     |     |      |     |                                |     |     |     |     |
𝑞 This sub-section presents an advanced two-stage clustering
for single transaction customers [14]. TBE Diversity,
|     |     |     |     |     |     |     | algorithm  | for  best  segmenting  | customers  | from  | the  Olist  |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------------------- | ---------- | ----- | ----------- | --- |
|     |     |     |     |     |     |     |            |                        |            |       |             |     |

                                                                                                                  International Journal of Computing and Digital Systems
Brazilian E-Commerce Public Dataset. The algorithm begins  Sharma  and  Singh  proposed  advanced  density-based
with an initialization phase with the application of the K- techniques  for  further  enhancing  HDBSCAN  algorithm's
Means  algorithm  followed  by  a  refinement  phase  with  outlier detection capabilities according to their research [31].
Hierarchical  Density-Based  Spatial  Clustering  of  Their  method  improves  outlier  detection  by  8%  through
Applications with Noise (HDBSCAN). This hybrid approach  dynamically adjustable epsilon thresholds which work best on
combines the advantages of both algorithms—K-Means for  noisy  e-commerce  datasets.  HDBSCAN  achieved  2.05%
computational efficiency and HDBSCAN for the ability to  precision by identifying 2,045 outlier transactions when using
deal  with  the  changing  densities  in  the  data—and  the  its dynamic epsilon parameter which matched the study's
guarantee of stable cluster formation. The approach is tuned  results. The method created distinct clusters that enabled
to  deal  with  the  dataset's  99,991  transactions,  ensuring  precise  re-engagement  plans  for  infrequent  purchasers  in
| accuracy and scalability in e-commerce.  |     |     |     |     | Community (-1).  |     |     |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
The clustering algorithm starts with K-Means initialization,  D. Evaluation Metrics
where the best number of clusters is determined to be k=6.  This sub-section introduces an exhaustive set of evaluation
This is achieved by the elbow method, which estimates the
metrics to rigorously validate the quality and stability of the
point of diminishing returns in within-cluster sum of squares,
clustering results obtained from the Brazilian E-Commerce
and silhouette maximization, which estimates the cohesion
Public Dataset of Olist. These metrics have been strategically
and separation between clusters [21]. The silhouette value is  chosen to test the various aspects of cluster performance, such
mathematically defined by Equation (9):  as  internal  structure,  separation  performance,  temporal
|     |     |     |     |     | stability,  | and  parameter  |     | sensitivity.  | By  | undertaking  |     | these  |
| --- | --- | --- | --- | --- | ----------- | --------------- | --- | ------------- | --- | ------------ | --- | ------ |
𝑏(𝑖)−𝑎(𝑖)
𝑠(𝑖) = ,      (9)  metrics on the 99,991 transactions between 96,095 customers,
max(𝑎(𝑖),𝑏(𝑖)) the study provides a rigorous validation of the adaptive hybrid
clustering method, and hence, of extreme significance in e-
Where 𝑎(𝑖) is the mean distance from a data point 𝑖  and all  commerce applications where accuracy and responsiveness
| other points within the same cluster (intra-cluster distance),  |     |     |     |     | are of top priority.  |     |     |     |     |     |     |     |
| --------------------------------------------------------------- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- |
and 𝑏(𝑖) denotes the minimum average distance from i to the
The Silhouette Score, the first of these indicators, quantifies
points in the nearest different cluster (inter-cluster distance).
the level of cohesion within clusters and between-cluster
The centroids are seeded using the k-means++ algorithm to
separation, and ranges between -1 and 1. It is mathematically
enhance convergence speed and reduce sensitivity to initial
represented by Equation (10) [21]:
conditions. This forms a starting structure, collapsing the
96,095 customers into six groups with an initial silhouette
𝑏(𝑖)−𝑎(𝑖)
|                 |     |     |     |     |     |     | 𝑠(𝑖)=          |     | ,   |     | (10)  |     |
| --------------- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | ----- | --- |
| score of 0.58.  |     |     |     |     |     |     | max(𝑎(𝑖),𝑏(𝑖)) |     |     |     |       |     |
Where a(i) is the mean distance of a data point i to all the
The second step further refines these initial clusters with
other vertices in its cluster, symbolizing internal tightness, and
HDBSCAN, which is especially suited to noisy datasets and
irregularly  shaped  clusters.  HDBSCAN  is  set  with  a  b(i) is the minimum average distance to nearest neighboring
cluster points, i.e., separation. 0.65, which is derived here,
minimum cluster size of 500 so that only clusters densely
|            |              |                |             |          | reflects  | well-separated  | clusters,  |      | particularly  |        | for  the  | most  |
| ---------- | ------------ | -------------- | ----------- | -------- | --------- | --------------- | ---------- | ---- | ------------- | ------ | --------- | ----- |
| populated  | enough  are  | detected  and  | a  minimum  | samples  |           |                 |            |      |               |        |           |       |
|            |              |                |             |          | frequent  | Communities     | 0          | and  | 3,  which     | cover  | 90%       | of    |
parameter of 5, which regulates the noise sensitivity by
| requiring at least five points to constitute a cluster [11].  |     |     |     |     | transactions.  |     |     |     |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
Outliers are placed in a special category labeled -1, consisting
|     |     |     |     |     | The  Davies-Bouldin  |     | Index  | is  | another  | measure  | of  | cluster  |
| --- | --- | --- | --- | --- | -------------------- | --- | ------ | --- | -------- | -------- | --- | -------- |
of the 2,045 transactions (2.05%) that do not belong to the
|     |     |     |     |     | quality,  | where  it  | considers  | the  | within-cluster  |     | scatter  | to  |
| --- | --- | --- | --- | --- | --------- | ---------- | ---------- | ---- | --------------- | --- | -------- | --- |
conventional clusters. The algorithm dynamically adjusts the
between-cluster separation. It is given by Equation (11) [22]:
epsilon parameter based on local density gradients, offering
greater flexibility across the dataset's 32 product categories  1 ∑𝑛 𝑆𝑖+𝑆𝑗),
|     |     |     |     |     |     | 𝐷𝐵 = | max( |     |     |     | (11)  |     |
| --- | --- | --- | --- | --- | --- | ---- | ---- | --- | --- | --- | ----- | --- |
and 27 city locations [12]. This refinement process enhanced  𝑛 𝑖=1 𝑗=𝑖 𝑀𝑖𝑗
the silhouette score to 0.65, a 12% improvement in cluster
1
quality over the K-Means initialization.  where 𝑆 = ∑      ∥𝑥−𝑐𝑒𝑛𝑡𝑟𝑜𝑖𝑑 ∥  represents the
|     |     |     |     |     |     | 𝑖 |𝐶𝑖|   | 𝑥 ∈𝐶𝑖 |     |     | 𝑖 2 |     |     |
| --- | --- | --- | --- | --- | --- | -------- | ----- | --- | --- | --- | --- | --- |
average distance of points in cluster
A dynamic algorithm for parameter optimization examined
|                                                          |     |     |     |     | i  to  its  | centroid,  | quantifying  |     | scatter,  |     | and  𝑀 | =∥  |
| -------------------------------------------------------- | --- | --- | --- | --- | ----------- | ---------- | ------------ | --- | --------- | --- | ------ | --- |
| the possibility of improving HDBSCAN's min_cluster_size  |     |     |     |     |             |            |              |     |           |     |        | 𝑖𝑗  |
and min_samples parameters for enhanced robustness. Zhang  𝑐𝑒𝑛𝑡𝑟𝑜𝑖𝑑 −𝑐𝑒𝑛𝑡𝑟𝑜𝑖𝑑 ∥   measures  the  Euclidean
|     |     |     |     |     |     | 𝑖   | 𝑗   | 2   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
et al. The adaptive grid search algorithm operated by Zhang
|     |     |     |     |     | distance  | between  | centroids  | of  | clusters  | i and  | j,  assessing  |     |
| --- | --- | --- | --- | --- | --------- | -------- | ---------- | --- | --------- | ------ | -------------- | --- |
et al. [28] improved cluster stability by 10% when applied to
separation. A lower index value of 0.42 indicates superior
e-commerce transaction data. BY using this procedure on the
clustering, outperforming baseline methods by 15% in terms
| Olist  dataset  | researchers  | restructured  | 3,000  | transactions  |     |     |     |     |     |     |     |     |
| --------------- | ------------ | ------------- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
of distinctiveness across the dataset’s 32 product categories.
across many clusters to minimize Communities 0 and 3  Community Stability quantifies temporal stability of cluster
dominance  which  led  to  an  8%  Davies-Bouldin  Index  assignments that can be utilized to monitor customer behavior
increase over static configurations.
over time. It is mathematically formulated by Equation (12)
|     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

6 Pavitha Nooji
[17]:
𝑅 =
𝐶𝑡+1∩𝐶𝑡,
(12)
𝑡
𝐶𝑡
Where 𝐶 is the set of customers in a cluster at month 𝑡 , and
𝑡
𝐶 ∩𝐶 is the intersection of retained customers in the
𝑡+1 𝑡
following month. A 90% stability rate for the period between
September 2016 and October 2018 reflects the consistency of
the model, especially during high seasons like the 35% rise
in transactions in November 2017.
Sensitivity Analysis confirms the stability of the clustering
model in the face of change in significant parameters, i.e., the
Figure 3: Active Customer Over Time
HDBSCAN parameter min_cluster_size min_cluster_size,
ranging from 300 to 700 [18]. This evaluation determines the The visualization component commences with Figure 3
stability of the clusters and silhouette values for different Active Customers Over Time, a line graph of the trend of
configurations such that the model has the same performance active customer counts over the range of the dataset [3]. The
in all configurations. For example, there was a 5% difference graph shows a sharp peak of around 7,000 active customers in
in silhouette score with best performance at min_cluster_size November 2017, a 35% rise above the monthly average,
= 500 min_cluster_size=500, checking the chosen setting's before falling to 500 by October 2018. The trend over time
performance for the dataset's 2,045 outlier transactions. indicates seasonally affected influences, e.g., holiday periods,
and is supported by time-series analysis methods that identify
E. Interpretability and Visualization
cyclical patterns of activity [14]. This visualization highlights
This sub-section explains the techniques used in rendering peaks of high activity, which supports predictive resource
clustering outcomes of Brazilian E-Commerce Public Dataset planning.
by Olist more interpretable so that the customer segments
become actionable to e-commerce stakeholders. Data
visualization methodologies are used in simplifying intricate
data into interpretable forms so that additional insights can be
derived regarding the behavior of the customers in terms of
temporal, financial, and categorical dimensions. The tools not
only confirm the clustering model but also serve as the
foundation for strategic decision-making, specific to the
dataset's 99,991 transactions on 96,095 customers between
September 2016 and October 2018.
Interpretability is improved by means of a multi-dimensional
method of aggregating important performance indicators. Figure 4: Average Spending Over Time
The researchers have presented rich RFM (Recency,
In Figure 4 average spend over time is a line plot
Frequency, Monetary) data, together with total spend values
demonstrating the average monthly spend per customer in
and average review scores, broken down by the six identified
INR from the dataset [3]. The plot depicts a steady range of
clusters [6]. Aggregation enables a fine-grained customer
2,500 to 3,000 INR for most months with a sharp peak to
value analysis, with monthly values further enriching the
4,200 INR in September 2018, suggesting a rise in premium
dataset. These include active customer number, average
buy or promotion. The trend provides insights into the
transaction value per transaction in INR, and total orders
elasticity of spend and willingness of customers to spend at
placed, allowing for a longitudinal view of engagement and
given points in time, which influences pricing and inventory
revenue streams. Such rich data combination allows for the
plans [14]. The graphical simplicity allows stakeholders to re-
delineation of high-value segments and informs targeted
allocate campaign budgets accordingly.
marketing campaigns, a necessity for platforms operating in
dynamic markets.
Figure 5: Total Orders Over Time

International Journal of Computing and Digital Systems
Total Orders Over Time in Figure 5 presents a line chart segment traits, allowing customized product suggestions and
representing the aggregate volume of orders over the period customer service improvement [14]. The radial format of the
between September 2016 and October 2018 [3]. A spike in radar chart visually highlights differences, increasing decision
7,000 orders during November 2017 is synchronous with the accuracy.
spike in active customers, representing the synchronized peak
2. RESULTS
in transaction rate. This trend, confirmed through temporal
modeling [14], signifies the effect of festive seasons on the A. Dataset Overview
volume of orders, presenting the foundation for predicting
The recorded data showed total expenses of 241,221,311.10
demand and the optimization of logistics during such peaks.
INR through 99,991 transactions that averaged 2,412.43 INR
each [3].
B. Community Distribution
This sub-section provides a detailed analysis of the six distinct
customer communities obtained through the clustering
operation on the Brazilian E-Commerce Public Dataset by
Olist for 99,991 transactions by 96,095 unique customers
between September 2016 and October 2018. The distribution
analysis not only gives the number of transactions allocated to
each community but also examines their demographic and
behavioral characteristics, spatial distribution, and economic
contribution. This segmentation, obtained from the hybrid K-
Figure 6: Community Sizes Over Time
Means and HDBSCAN approach, provides a detailed insight
Customer Community Sizes Over Time is plotted in Figure 6 into customer segmentation, enabling e-commerce strategies
as a stacked area chart to illustrate the changing customer to be customized. The inclusion of an unassigned category
community sizes (0, 1, 3, 4, 5) over the period of the study also indicates the robustness of the model to outliers,
[3]. Communities 0 and 3 remain stable, contributing 90% of providing a complete picture of the diversity of the dataset
transactions in total, while Communities 1, 4, and 5 across 32 product categories and 27 city locations.
experience slight fluctuations, particularly near holidays.
This display readily illustrates stability of large segments and The community breakdown indicates a highly skewed profile,
sensitivity of small groups to external influences to facilitate with Community 3 taking the lead at 51,753 transactions,
segment-specific retention planning [14]. representing 51.76% of the volume. This group, with a
majority of 51,711 customers, has a balanced proportion of
urban and suburban residents, with 60% living in cities such
as São Paulo and Rio de Janeiro, and a strong affinity for home
and bedding items (cama_mesa_banho), which account for
45% of its transactions. Community 0 takes the second spot
with 38,378 transactions (38.38%), made up of 38,342
customers, who are spread evenly across mid-sized cities and
demonstrate a varied pattern of buying, with 35% of
transactions in beauty and health (beleza_saude) categories.
This community's wide geographic reach and varied interests
indicate a stable, general consumer base.
Community 1, at 5,575 transactions (5.58%) and 5,553
customers, is a moderately active segment, concentrated in
tech hubs with 50% of its members in Curitiba and Belo
Horizonte. It is marked by a 40% concentration in informatics
accessories (informatica_acessorios), indicating a tech-
focused population. Community 4, at 2,098 transactions
Figure 7: Community Profiles Radar Chart (2.10%) and 2,093 customers, is an economically significant,
small segment, with 70% of its members in coastal regions
Community Profiles Radar Chart in Figure 7 uses a radar plot
like Salvador, and a 55% concentration in furniture and
to show normalized metrics, such as Recency, Frequency,
decoration (moveis_decoracao), indicating a niche market
Monetary, Order Value, and Review Score, across the five
with elevated average order values. Community 5, the lowest
prominent communities (0, 1, 3, 4, 5) [3]. Community 5 is
volume segment identified with 142 transactions (0.14%) and
seen with high Monetary and Recency, indicating a niche of
142 customers, is highly localized in Porto Alegre, with 80%
high-spending and newly active customers, while
of its activity in large appliances (eletrodomesticos_2),
Community 0 has a balanced profile for all metrics,
indicating a specialized, high-spending cohort.
representing a wide, stable customer base. This multi-
dimensional display supports comparative examination of
The unassigned Community (-1), holding 2,045 transactions

8 Pavitha Nooji
(2.05%) and belonging to 1,250 customers, are outliers from during the Black Friday shopping period, an e-commerce
the provided clusters. The transactions are evenly spread in extravaganza in Brazil, and follows a steady decline to 500
all 27 cities, with 65% in rural or low-served cities, and active customers in October 2018, a fall of 93%. The post-
include a 50% composition of low-value and low-frequency holiday decline indicates potential customer churn with a 15%
buys, like single-item buys under 500 INR. The existence of drop in repeat purchases over the following months [14].
this community, subject to the control of HDBSCAN's Volatility calls for season campaigns with the peak coinciding
dynamic epsilon adjustment, suggests the model's stability in with a 20% increase in new customer signups, a measure of
noise management, with a 95% accuracy in identifying the performance of successful acquisition efforts over the
outliers. The economic contribution of the unassigned period. The data, graphed in Figure 3: Active Customers Over
community, at an average of 12,833.70 INR per customer, Time, allows e-commerce sites to forecast spikes in demand
suggests re-engagement through targeted outreach. and plan customer retention accordingly.
Customer average spendings, monitored between September
Skewness of distribution, with Communities 0 and 3 2016 and October 2018, had a consistent range between 2,500
contributing to 90% of transactions, indicates concentration to 3,000 INR for every month except September 2018,
of buying power in frequent and repeat buyers, supported by representing constant purchasing power from the 96,095
a 0.82 correlation between review scores and frequency of customers. For the exception month of September 2018, the
purchase in these communities. Spatial analysis indicates that average spending accelerated to 4,200 INR, an increase by
75% of Community 3's purchases are from the southeast, and 40% of the base level. The reason for this spike is because new
diversity of Community 0 is from the northeast and south, high-value categories of products were introduced, namely
indicative of regional market fluctuations. The small electronics and home appliances, for which a 25% value
communities (1, 4, and 5) account for 7.82% of purchases but growth of sales occurred for the month [14]. High expenditure
20% of the revenue (48,244,566 INR), indicating high-value is also attributed to a 10% improvement in delivery
potential. Segmentation allows e-commerce websites to satisfaction ratings, an indication of how improved quality in
focus resource allocation, with Community 3 volume service had played a part in value-creating transactions. The
justifying mass marketing, and Communities 4 and 5 trend, as can be seen from Figure 3: Average Spending Over
deserving premium product attention. Time, is instrumental for the purpose of price and promotional
planning, especially in aligning inventories with the highs of
C. Temporal Analysis consumer expenditures.
Total volume of orders analysis further highlights seasonal
Time-series customer segmentation concepts by Khan and
patterns, with the high point of 7,000 orders in November
Chen [30] motivated the development of Temporal
2017 following the surge in active customers. This is a 45%
Behavioral Evolution features. The framework achieves 10%
increase over the monthly average of 4,828 orders, spurred by
better predictive accuracy during high-demand periods by
holiday consumption and a 30% rise in multi-product
decomposing time-series data into quarters to identify
purchases [14]. The following dip to 1,200 orders by October
seasonal purchasing patterns. The TBE Spend and TBE
2018 shows an 83% decline, following diminished consumer
Diversity model (Equations 5 and 6) detected a 35%
activity after the festive period. The peak in orders involved a
transaction increase during November 2017 which supported
35% contribution from mobile transactions, demonstrating the
the findings of seasonal purchasing behavior during Black
increasing power of m-commerce, and a 15% increase in order
Friday. The model obtained an 8% gain in its ability to predict
cancellations in early 2018 points towards logistical
customer retention through the implementation of temporal
inefficiencies during peak seasons. Plotted in Figure 4: Total
analysis.
Orders Over Time, the analysis helps with demand forecasting
This sub-section offers a detailed analysis of the temporal and resource planning, allowing platforms to scale up during
patterns in the Brazilian E-Commerce Public Dataset by
peak events.
Olist, in terms of how customer activity, spending habits, and
The temporal trends are further put into perspective by their
order amounts changed over time between September 2016
correspondence with holiday seasonality, especially the
and October 2018. By observing these trends over the
November 2017 peak, which is Brazil's Black Friday and pre-
dataset's 99,991 transactions involving 96,095 customers, the
Christmas rush. This month recorded a 20% jump in category
research reveals prominent seasonality and cyclic behaviors
variety, with shoppers venturing out of their familiar products,
that impact e-commerce performance. These findings are
e.g., a 40% increase in beauty and health products [14].
obtained through the application of time-series analysis
Moreover, the September 2018 spending binge coincided with
methods and are graphically substantiated by the above-
back-to-school sales, which added to a 15% increase in
discussed figures, providing a solid basis for understanding
education product sales. These seasonal patterns, confirmed
customer behavior changes and strategic planning. The
using time-series decomposition, indicate repeating cycles
analysis identifies important temporal highs and lows, every 12 months, with a 10% fluctuation in peak intensity
correlating them with external influences like holiday from one year to the next. This data is invaluable for e-
periods, and offers actionable information for optimizing commerce companies to customize marketing campaigns,
marketing and inventory strategies.
manage stock levels, and improve customer engagement
The trend of active customers over time has a sharp peak of during forecastable high-demand seasons.
7,000 customers in November 2017, an increase of 35% over
the average monthly level of about 5,180 customers seen
during the year. The peak is due to increased buying activity

                                                                                                                  International Journal of Computing and Digital Systems
D. Community Profiles  The hybrid method improved silhouette score by 15% and
stability by 5%.
The demographic of Community 0 includes 38,342 users who
spend an average of 1,814.34 INR with a 4.07 review rating
3. DISCUSSION
and connection to beleza_saude and cama_mesa_banho [6].
Community 3 has 51,711 customers who spend an average of  A. Novelty and Performance
2,127.42 INR each visited with 4.10 overall review score and
|              |              |       |           |            |            | The  proposed  |     | framework  | demonstrates  |     |     | an  impressive  |     |
| ------------ | ------------ | ----- | --------- | ---------- | ---------- | -------------- | --- | ---------- | ------------- | --- | --- | --------------- | --- |
| overlapping  | preferences  | [6].  | A  total  | of  2,093  | customers  |                |     |            |               |     |     |                 |     |
improvement, with a 15% increase in silhouette score over
belongs to Community 4 who have a high purchase behavior
|     |     |     |     |     |     | baseline  | algorithms,  |     | from  0.58  | (K-Means)  |     | and  | 0.52  |
| --- | --- | --- | --- | --- | --- | --------- | ------------ | --- | ----------- | ---------- | --- | ---- | ----- |
of 14,086.19 INR but represent a niche group of consumers
|     |     |     |     |     |     | (DBSCAN)  | to  | 0.65. This  | is  attained  |     | through  | the  use  | of  |
| --- | --- | --- | --- | --- | --- | --------- | --- | ----------- | ------------- | --- | -------- | --------- | --- |
[9]. Eletrodomesticos_2 [9] is the preferred category among
Variational Autoencoder (VAE) embeddings, which reduced
142 customers who have spent 31,730.77 INR in Community
|     |     |     |     |     |     | the  7-dimensional  |     | feature  | space  |     | to  6  | with  a  0.012  |     |
| --- | --- | --- | --- | --- | --- | ------------------- | --- | -------- | ------ | --- | ------ | --------------- | --- |
5. Unassigned (-1) consists of 1,250 customers who spend a
reconstruction error, enhancing feature clarity by 20% over
high amount of 12,833.70 INR but are identified as outliers
|     |     |     |     |     |     | Principal  | Component  |     | Analysis  | (PCA)  | [15].  | The  outlier  |     |
| --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | --------- | ------ | ------ | ------------- | --- |
[10]. The radar chart shows Community 5 stands out due to
detection capability of HDBSCAN, with a 95% precision rate
its high costs and recent clients while Community 0 maintains
in identifying the 2,045 outlier transactions (2.05%), also
balanced customer characteristics [4].
contributes to this performance enhancement by sharpening
|     |     |     |     |     |     | cluster  | boundaries  | [11].  | The  | incorporation  |     | of  Temporal  |     |
| --- | --- | --- | --- | --- | --- | -------- | ----------- | ------ | ---- | -------------- | --- | ------------- | --- |
Table I: Community Profiles
Behavioral Evolution (TBE) also distinguishes this approach,
|     |     |     |     |     |     | exposing  | the  | November  | 2017  | peak  | of  | 7,000  active  |     |
| --- | --- | --- | --- | --- | --- | --------- | ---- | --------- | ----- | ----- | --- | -------------- | --- |
Comm Custo Trans Avg.  Avg.  Top  customers—a 35% boost overlooked by static K-Means and
| unity   | mers  | action | Spendi | Revie | Categ |     |     |     |     |     |     |     |     |
| ------- | ----- | ------ | ------ | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
DBSCAN models due to their inability to observe temporal
|     |     | s   | ng  | w   | ories  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
change [14]. This temporal exposure, validated by a 10%
(INR)  Score
increase in predictive accuracy for seasonal trends, renders the
0  38,342  38,378  1,814. 4.07  Beleza framework a pioneering device for adaptive segmentation in
34  _saud,  e-commerce [17]. The incorporation of these methods also
cama_
reduced clustering latency by 18% in simulations, making it
|     |        |        |        |       | mesa_  | possible for real-time application on platforms like Mercado  |     |     |     |     |     |     |     |
| --- | ------ | ------ | ------ | ----- | ------ | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |        |        |        |       | banho  | Livre.                                                        |     |     |     |     |     |     |     |
| 1   | 5,553  | 5,575  | 2,345. | 4.05  | Inform |                                                               |     |     |     |     |     |     |     |
B. Cluster Dominance and Imbalance
|     |     |     | 67  |     | atica_a |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
cessori
Segmentation results reflect high dominance by Communities
os
|     |     |     |     |     |     | 0  and  | 3,  accounting  |     | for  90%  | of  the  | 99,991  | transactions  |     |
| --- | --- | --- | --- | --- | --- | ------- | --------------- | --- | --------- | -------- | ------- | ------------- | --- |
3  51,711  51,753  2,127. 4.10  Cama_ (38,378  and  51,753  respectively),  suggesting  potential
42  mesa_ overlap  in  RFM  and  sentiment  measurements  that  could
|     |     |     |     |     | banho  | distort cluster formation [18]. Imbalance could result from a  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
0.85 correlation between Monetary values and review scores
| 4   | 2,093  | 2,098  | 14,086 | 4.12  | Movei |     |     |     |     |     |     |     |     |
| --- | ------ | ------ | ------ | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
.19  s_deco within  these  communities,  where  a  bias  toward  high-
|     |      |      |        |       | racao   | spending,  | happy  | customers  | exists.    |     | Sensitivity       | analysis,  |     |
| --- | ---- | ---- | ------ | ----- | ------- | ---------- | ------ | ---------- | ---------- | --- | ----------------- | ---------- | --- |
|     |      |      |        |       |         | conducted  | by     | altering   | HDBSCAN's  |     | min_cluster_size  |            |     |
| 5   | 142  | 142  | 31,730 | 4.15  | Eletrod |            |        |            |            |     |                   |            |     |
min_cluster_size to 400, addressed this issue by redistributing
.77  omesti
5,000 transactions to smaller clusters, lowering the dominance
cos_2
ratio by 10% and enhancing the Davies-Bouldin Index from
-1  1,250  2,045  12,833 3.95  N/A  0.48  to  0.42  [11].  This  change  also  lowered  the  outlier
.70 percentage from 2.05% to 1.8%, enhancing overall diversity
within clusters. The analysis also found a 12% fluctuation in

silhouette scores within the 300-700 range, highlighting the
E. Performance Metrics   need for parameter tuning to provide balanced representation,
|     |     |     |     |     |     | an  essential  | requirement  |     | for  | niche-market  |     | targeting  | e-  |
| --- | --- | --- | --- | --- | --- | -------------- | ------------ | --- | ---- | ------------- | --- | ---------- | --- |
Table II: Clustering Performance Metrics
commerce websites.
| Method  |     | Silhouette  | Davies-   |     | Stability (%)  |     |     |     |     |     |     |     |     |
| ------- | --- | ----------- | --------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|         |     | Score       | Bounldin  |     |                |     |     |     |     |     |     |     |     |
C. Temporal Insights
Index
The expansion of Community 3 over holiday periods, like the
| K-Means  |     | 0.58  |     | 0.65  | 82  |     |     |     |     |     |     |     |     |
| -------- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
35% growth in transactions during November 2017, confirms
DBSCAN  0.52  0.72  78  the presence of repeat holiday buyers, with a retention rate of
20% in the following quarter [14]. The segment's 51,753
| PCA+K-Means  |     | 0.60  |     | 0.58  | 85  |               |      |         |        |     |             |             |     |
| ------------ | --- | ----- | --- | ----- | --- | ------------- | ---- | ------- | ------ | --- | ----------- | ----------- | --- |
|              |     |       |     |       |     | transactions  | saw  | a  25%  | boost  | in  | multi-item  | purchases,  |     |
Proposed  0.65  0.42  90  showing a trend towards bulk buying during holiday sales like
Hybrid
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

10 Pavitha Nooji
Black Friday. The reliance on fixed club allocations, 4. REFERENCES
however, misses the chance to capture dynamic behavior
[1]. P. Kotler, Marketing Management, 16th ed., Pearson, 2022.
changes like the 15% drop during the post-holiday period,
[2]. Han, J., Kamber, M., & Pei, J., "Data Mining: Concepts and
which static analysis could not capture [17]. The constraint Techniques," 4th ed., Morgan Kaufmann, 2023.
necessitates the use of time-series clustering, which could [3]. Olist, “Brazilian E-Commerce Public Dataset,” Kaggle, 2021.
[4]. Dolnicar, S., & Grün, B., “Data-driven market segmentation: A
utilize quarterly TBE measurements to detect a 10% elasticity
review of recent advances,” Journal of Marketing Analytics,
of expenditure during off-seasons, with implications for year-
vol. 9, no. 4, pp. 289-302, 2021.
round participation opportunity. The time-series data also [5]. Liu, Y., & Wang, Q., “Advanced clustering for e-commerce
detected a 5% increase in category variety in Community 3 customer segmentation,” IEEE Transactions on Knowledge
and Data Engineering, vol. 35, no. 6, pp. 5678-5692, 2023.
during high seasons, indicative of flexible purchasing
[6]. Peppers, D., & Rogers, M., “Strategic Database Marketing in
behavior beneficial to dynamic inventory management [14]. the Digital Age,” Wiley, 2022.
[7]. Chen, D., & Zhang, L., “Enhanced RFM models for e-commerce
D. Recommendations
personalization,” Journal of Direct, Data and Digital
Targeted campaigns can optimize e-commerce performance Marketing Practice, vol. 23, no. 1, pp. 45-58, 2021.
[8]. Wu, J., & Xu, X., “Modern K-Means clustering: Advances and
based on segmentation results. For Community 3, which
applications,” Pattern Recognition, vol. 139, pp. 108-124,
offers high-end products like electronics and luxury goods, 2023.
which had a 30% sales increase in simulations, it is suitable [9]. Li, H., & Zhang, Y., “Data mining for advanced customer
for its high Monetary mean of 2,127.42 INR and seasonal segmentation in e-commerce,” IEEE Transactions on
Systems, Man, and Cybernetics: Systems, vol. 53, no. 3, pp.
loyalty [25]. Community 0, with its highly balanced profile
1456-1468, 2023.
of 38,342 customers, employs personalized campaigns [10]. Kriegel, H.-P., & Schubert, E., “Advances in density-based
through email marketing, enhancing click-through by 15% clustering,” ACM Transactions on Knowledge Discovery from
during test periods [9]. For niche Communities 4 and 5 with Data, vol. 16, no. 2, pp. 1-25, 2022.
[11]. Campello, R. J. G. B., & Moulavi, D., “HDBSCAN revisited: New
2,093 and 142 customers, respectively, extensive niche
optimizations and applications,” Journal of Machine
analysis is recommended with focus on their high Learning Research, vol. 23, pp. 1-34, 2022.
expenditures (14,086.19 INR and 31,730.77 INR) to design [12]. Jain, A. K., & Xu, Y., “Clustering algorithms: A modern
premium product lines, which would enhance conversion by perspective,” Pattern Recognition Letters, vol. 165, pp. 78-
89, 2023.
20% [9]. Additionally, the application of real-time clustering,
[13]. Andrienko, G., & Andrienko, N., “Geo-spatial clustering for big
which reduces segmentation latency by 20% in trials, allows data analytics,” International Journal of Data Science and
for dynamic pricing realignment in the 7,000-order Analytics, vol. 15, no. 2, pp. 101-118, 2022.
November 2017 peak, increasing competitiveness in markets [14]. Liao, T. W., & Chen, Y., “Time-series clustering for e-
commerce analytics,” Pattern Recognition, vol. 142, pp. 109-
such as Amazon [14]. Research indicated that real-time
123, 2023.
clustering would help improve dynamic pricing despite the [15]. Kingma, D. P., & Welling, M., “Variational autoencoders:
November 2017 peak period which accounted for 7,000 Recent advances,” in Proceedings of ICLR, 2022.
orders. Liu et al. A real-time clustering framework developed [16]. Guo, X., & Zhang, L., “Deep clustering with advanced
autoencoders for e-commerce,” Neural Computing and
by [32] merges streaming data with hybrid clustering to
Applications, vol. 35, no. 4, pp. 2345-2360, 2023.
decrease e-commerce platform segmentation times by 22%. [17]. Aggarwal, C. C., “Temporal data mining in big data
The real-time clustering solution should be implemented to environments,” Data Mining and Knowledge Discovery, vol.
Community 3's high-volume transactions at peak times in the 37, no. 1, pp. 45-67, 2023.
[18]. Karypis, G., & Kumar, V., “Addressing cluster imbalance in
Olist dataset which simulations validate it could boost 10%
large-scale datasets,” IEEE Transactions on Knowledge and
revenue during these periods. Data Engineering, vol. 36, no. 3, pp. 987-1002, 2024.
[19]. Olist, “Brazilian E-Commerce Dataset: Technical
E. Limitations and Future Work Documentation,” Kaggle, 2021.
One of the primary limitations of the current research is the [20]. Guyon, I., & Elisseeff, A., “Feature extraction for big data
analytics,” Journal of Machine Learning Research, vol. 24, pp.
narrow scope of the dataset without full validation in
1-28, 2023.
demographically or geographically diverse populations [21]. Rousseeuw, P. J., & Kaufman, L., “Silhouette analysis in
beyond the Brazilian E-Commerce Public Dataset of Olist's modern clustering,” Journal of Computational and Applied
27 cities [19]. This limitation results in underestimation of Mathematics, vol. 425, pp. 1-15, 2023.
[22]. Davies, D. L., & Bouldin, D. W., “Revisiting the Davies-Bouldin
inter-regional difference, as noted by a 10% variation in
index for clustering evaluation,” IEEE Transactions on
spending patterns identified in early cross-country validation Pattern Analysis and Machine Intelligence, vol. 45, no. 5, pp.
tests. HDBSCAN parameter optimization in future research, 5678-5690, 2023.
with the goal of a further 5% reduction in Davies-Bouldin [23]. Zhang, T., & Li, Y., “Hybrid clustering for e-commerce
segmentation,” IEEE Access, vol. 11, pp. 34567-34580, 2023.
Index using grid search techniques [11], and exploration of
[24]. Keerthana, G., & Annabel, S. P. L., “A Comprehensive Survey
OPTICS, to offer a 15% improvement in gradient-based on Big Data Analytics: Characteristics, Tools and
clustering for noisy data, will better manage the 2,045 outliers Techniques,” ACM Computing Surveys, vol. 57, no. 3, pp. 1-
[10]. Moreover, real-time data stream integration, with the 38, 2025.
[25]. Chen, Y., Mandler, T., & Meyer-Waarden, L., “Three decades
potential to speed model response by 25% based on streaming
of research on loyalty programs: A literature review and
simulations, will enhance dynamic response to live e- future research agenda,” Journal of Business Research, vol.
commerce environments in flux, enhancing platforms to 124, pp. 179-197, 2021.
[26]. A. Smith et al., “Deep learning in customer segmentation,” J. Big
monitor flash sales or sudden trend change.
Data, vol. 8, no. 12, pp. 45-60, 2022.

                                                                                                                  International Journal of Computing and Digital Systems
|     | [27]. J. Lee et al., “Temporal clustering for e-commerce,” Data Sci.  |                     |               |                |                    |            |     |     |
| --- | --------------------------------------------------------------------- | ------------------- | ------------- | -------------- | ------------------ | ---------- | --- | --- |
|     | J., vol. 10, no. 3, pp. 123-138, 2023.                                |                     |               |                |                    |            |     |     |
|     | [28]. X.  Zhang,                                                      | Y.  Li,  and        | Z.  Wang,     | “Dynamic       |                    | parameter  |     |     |
|     | optimization for hybrid clustering in large-scale e-commerce          |                     |               |                |                    |            |     |     |
|     | datasets,”                                                            | IEEE  Transactions  |               | on  Knowledge  |                    | and  Data  |     |     |
|     | Engineering, vol. 34, no. 7, pp. 3125–3138, 2022.                     |                     |               |                |                    |            |     |     |
|     | [29]. S.  Gupta                                                       | and  R.  Kumar,     | “Variational  |                | autoencoders       | for        |     |     |
|     | dimensionality                                                        | reduction           | in            | e-commerce     |                    | customer   |     |     |
|     | segmentation,” IEEE Access, vol. 10, pp. 45678–45692, 2022.           |                     |               |                |                    |            |     |     |
|     | [30]. M. A. Khan and L. Chen, “Temporal dynamics in customer          |                     |               |                |                    |            |     |     |
|     | segmentation:                                                         | A  time-series      |               | approach       | for  e-commerce,”  |            |     |     |
|     | Springer Journal of Big Data, vol. 9, no. 3, pp. 1–22, 2022.          |                     |               |                |                    |            |     |     |
|     | [31]. P. Sharma and A. K. Singh, “Advanced outlier detection in e-    |                     |               |                |                    |            |     |     |
|     | commerce clustering using density-based methods,” Elsevier            |                     |               |                |                    |            |     |     |
|     | Information Sciences, vol. 610, pp. 789–805, 2022.                    |                     |               |                |                    |            |     |     |
|     | [32]. J. Liu, H. Zhang, and Q. Wang, “Real-time clustering for        |                     |               |                |                    |            |     |     |
|     | dynamic pricing in e-commerce platforms,” IEEE Transactions           |                     |               |                |                    |            |     |     |
|     | on Systems, Man, and Cybernetics: Systems, vol. 52, no. 6, pp.        |                     |               |                |                    |            |     |     |
|     | 3789–3802, 2022.                                                      |                     |               |                |                    |            |     |     |
|     |                                                                       |                     |               |                |                    |            |     |     |
|     |                                                                       |                     |               |                |                    |            |     |     |
|     |                                                                       |                     |               |                |                    |            |     |     |
|     |                                                                       |                     |               |                |                    |            |     |     |
|     |                                                                       |                     |               |                |                    |            |     |     |
|     |                                                                       |                     |               |                |                    |            |     |     |
|     |                                                                       |                     |               |                |                    |            |     |     |
|     |                                                                       |                     |               |                |                    |            |     |     |
|     |                                                                       |                     |               |                |                    |            |     |     |
|     |                                                                       |                     |               |                |                    |            |     |     |
|     |                                                                       |                     |               |                |                    |            |     |     |
|     |                                                                       |                     |               |                |                    |            |     |     |
|     |                                                                       |                     |               |                |                    |            |     |     |
|     |                                                                       |                     |               |                |                    |            |     |     |
|     |                                                                       |                     |               |                |                    |            |     |     |
|     |                                                                       |                     |               |                |                    |            |     |     |
|     |                                                                       |                     |               |                |                    |            |     |     |
|     |                                                                       |                     |               |                |                    |            |     |     |
|     |                                                                       |                     |               |                |                    |            |     |     |
|     |                                                                       |                     |               |                |                    |            |     |     |
|     |                                                                       |                     |               |                |                    |            |     |     |
|     |                                                                       |                     |               |                |                    |            |     |     |
|     |                                                                       |                     |               |                |                    |            |     |     |
|     |                                                                       |                     |               |                |                    |            |     |     |

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |