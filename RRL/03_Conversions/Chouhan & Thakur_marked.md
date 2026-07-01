International Journal of Technology Research and Management
ISSN (Online): 2348-9006
Vol 12 Issue 07 July 2025
Predicting Customer Behavior Using Machine Learning and Deep
Learning: A Comprehensive Review
Shivani Chouhan1, Srashti Thakur2
Lakshmi Narain College of Technology, Indore (MP)1, 2
shivanichouhan0121@gmail.com1, chouhansrashti00knw@gmail.com2
Abstract: Understanding customer behavior is crucial for businesses aiming to enhance customer
satisfaction, predict churn, and deliver personalized experiences. Recent advancements in machine
learning (ML) and deep learning (DL) have significantly transformed the way organizations analyze and
forecast customer actions across domains such as e-commerce, finance, and social media. This study
presents a comprehensive review of contemporary approaches employed to predict and analyze customer
behavior using various ML algorithms like Decision Trees, Random Forest, Logistic Regression, Support
Vector Machines, Gradient Boosting, Naïve Bayes, and advanced DL models including Long Short-Term
Memory (LSTM) and Transformer-based networks. The reviewed works demonstrate the use of large-
scale structured and unstructured datasets, applying models for tasks such as churn prediction, sentiment
analysis, product recommendation, and trend forecasting. The review also identifies the growing
significance of social media analytics, ethical concerns related to data use, and the superior
performance of ensemble and deep learning models in capturing customer intent. By synthesizing these
findings, this paper highlights the state-of-the-art in predictive customer behavior modeling and suggests
future directions for more interpretable, privacy-conscious, and context-aware intelligent systems.
Keywords: Customer Behavior Prediction, Machine Learning, Deep Learning, Customer Churn, Sentiment
Analysis, Recommendation Systems, LSTM, Transformer, Social Media Analytics, Data Mining, Predictive
Modeling, Consumer Analytics.
1. INTRODUCTION to look at this data and get useful information that will help
other people make decisions. There are many things you can
Sentiment analysis, natural language processing (NLP) find on the internet, like movies, airline reviews, and other
methods, and computational linguistics can be used to find types of social media data. It's also important to look at other
and remove subjective information from text. Reviews, polls, types of data, such as news and publications, as well as the
social media, and other ways let customers express their work done by staff. This is called "sentiment analysis." It's
feelings and ideas. People also use healthcare media to share when you look at a piece of text and try to figure out what the
their thoughts and feelings. Sentiment analysis is a broad person's feelings are. Social media platforms like Twitter,
term that refers to how a person or group of people feel about Facebook and Linkdin have given customers a new way to
a certain issue or situation in a given event, discussion, say what they think about goods, people, and places, and how
forum, interaction, or paper, for example. Sentiment Analysis they think they should be made. The only type of feedback
can be used to figure out how text is polarised at the feature, that users can give is text. Many text messages are sent
phrase, and document level. As people want to share their through social media and online shopping sites every day.
thoughts on a variety of platforms, more people are using the The job of looking at and analysing the mood of the public is
Internet. This has led to an overflow of opinionated content very important. NLP with artificial intelligence skills and text
on the Internet. A tool called sentiment analysis can be used analytics can be used to figure out how negative, neutral, or
Paper ID: 2025/IJTRM/07/2025/45815 1

International Journal of Technology Research and Management
ISSN (Online): 2348-9006
Vol 12 Issue 07 July 2025
positive a person is. Opinion mining and sentiment analysis  Perception: The way customers interpret information
can be done in any field or on any platform. This technology influences how they respond to marketing messages.
has become more common because of its many different  Attitudes and Beliefs: Long-standing opinions or beliefs
applications, which have led to the growth of many about a brand or product can significantly affect buying
businesses and organisations in a wide range of industries, behavior.
such as social media, health care, management, and the  Learning: Prior experiences or exposure to marketing
economy.[1-2] Sentiment analysis can be used to make smart campaigns impact future decisions.
decisions as well as give business information. When you do 2. Personal Factors
opinion mining, there are two ways to do it: sentiment  Age and Life Stage: Preferences change with age,
analysis and sentiment classification. People often use them income level, family size, and stage in life.
together, even though they each have different properties.
 Occupation and Economic Status: These define
The use of sentiment classification lets you group a document
spending capacity and product preferences.
or part of a document based on how it makes you feel.
 Lifestyle and Personality: Individual habits, hobbies,
Sentiment orientation is a type of text classification that uses
and personality traits shape customer choices.
the sentiment orientation of opinion to group text. Feeling
3. Social Factors
orientation is determined by how subjective it is, and this
 Family: Family members often influence buying
affects how the opinion turns out. Subjective analysis can be
decisions, especially in household-related purchases.
used to figure out whether text or review data is subjective or
 Social Groups: Friends, colleagues, and peer networks
objective. In this study, we looked at a few different ways to
can impact trends and preferences.
figure out how people feel. It doesn't matter how many
 Roles and Status: A customer’s position in society or
papers have been written on this subject. There is always a
within a community can shape their behavior and brand
need to improve sentiment analysis accuracy and
choices.
understanding. Sentiment analysis can be used in a lot of
4. Cultural Factors
different ways. There's only one problem: human language is
 Culture: Values, beliefs, and customs passed down
so hard to understand. There are many different ways to say
through generations play a major role in behavior.
this, including grammatical and cultural differences. An easy-
 Subculture: Regional, religious, or ethnic groups have
to-understand sentence: "My order has been put back." "Did
distinct purchasing patterns.
better than expected." The machine may not be able to
understand. In some cases, "thin" is a good way to describe a  Social Class: Purchasing power, tastes, and preferences
laptop, but it can also be a bad way to describe a wall in an often differ across socioeconomic strata.
apartment. In order to get the most accurate results, sentiment 5. Technological and Digital Influence
analysis needs to be tailored to the needs of the organisation.  Online Reviews and Ratings: Digital feedback
E-commerce is becoming more common these days. Online significantly sways decisions.
shopping is becoming more popular than buying things in  Social Media Influence: Platforms like Instagram,
stores. The opinions and ratings of customers can be used to YouTube, and Twitter affect brand awareness and
verify and publicise a product in the world of e-commerce loyalty.
and other online stores. These ratings and reviews help  Personalization Algorithms: Recommender systems
customers decide if they want to buy a product or not. This and targeted advertisements shape user journeys.
kind of content could have good or bad feedback from 6. Situational Factors
customers. [3]  Purchase Occasion: Special occasions often trigger
Factors Affecting Customer Behavior unique buying patterns.
Customer behavior is influenced by a wide range of  Availability and Convenience: Ease of access, delivery
factors, which can be broadly categorized into psychological, speed, and stock availability influence choices.
personal, social, and cultural domains. Understanding these  Pricing and Offers: Discounts, deals, and value-for-
factors is essential for developing accurate predictive models money perceptions impact final decisions.
and personalized customer strategies:[4]
1. Psychological Factors Machine Learning Approaches
 Motivation: Customers are driven by specific needs or Many methodologies may be used to classify and forecast
desires that guide their decision-making. public opinion. Two of the most extensively used
technologies for opinion mining and prediction are machine
Paper ID: 2025/IJTRM/07/2025/45815 2

International Journal of Technology Research and Management
ISSN (Online): 2348-9006
|     |     |     |     |     |     |     |     |     |     |     | Vol 12 Issue 07 July 2025  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- |

learning and lexicon-based methods. Furthermore, a hybrid  two  words  with  opposing  meanings,  you  may  go  on  to
technique that combines machine learning and lexicon-based  determining  how  other  individuals  are  feeling.  When  a
approaches  have  been  widely  used  [4]  It  improves  the  product  or  service  is  the  main  focus,  aspect  level
outcomes. The machine learning approach relies heavily on  classification is frequently viewed as the ideal strategy. The
classification  and  text  analysis.  Text  pre-processing  is  models employed for opinion mining and product analysis,
required to achieve the goal of text analysis, which is to make  according to [7], are based on as-pect level classification.
business judgments and strategic moves. To train a model  According to client input, product qualities may be extracted
that may be used to predict on a new set of data without  using the aspect level classification procedure, as illustrated
labels, some data must first be collected. The two machine  in Figure 3. The models collect the qualities of the things that
learning techniques are further classified into the following.  the reviewer has determined should be included in the feature
|     |   Supervised  |     | Learning:  |     | From  | a  tagged  | training  | selection. [8]  |     |     |     |     |     |     |     |
| --- | -------------- | --- | ---------- | --- | ----- | ---------- | --------- | --------------- | --- | --- | --- | --- | --- | --- | --- |

|     | dataset,       |     | supervised  | learning  | finds  | patterns  | and  |                  |     |     |     |     |     |     |     |
| --- | -------------- | --- | ----------- | --------- | ------ | --------- | ---- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
|     | correlations.  |     |             |           |        |           |      | Product reviews  |     |     |     |     |     |     |     |
The increased usage of electronic commerce has resulted
|     |   Unsupervised  |     |     | Learning:  | When  | a  dataset  | is  not  |     |     |     |     |     |     |     |     |
| --- | ---------------- | --- | --- | ---------- | ----- | ----------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
in a flood of data that must be analyzed in order to make
labeled, unsupervised learning may be used to infer
educated decisions and complete pertinent activities. Because
patterns from it.
there is no formal reputation system in place, consumers are
| Opinions  |     | can  | be  classified  | based  | on  | how  | the  text  is  |             |       |         |            |      |          |     |            |
| --------- | --- | ---- | --------------- | ------ | --- | ---- | -------------- | ----------- | ----- | ------- | ---------- | ---- | -------- | --- | ---------- |
|           |     |      |                 |        |     |      |                | unfamiliar  | with  | items,  | features,  | and  | quality  | in  | digitally  |
handled. We'll go through a handful of them right now. There
mediated marketplaces, and there are trust difficulties as a
are numerous methods to categories the material, including at
result of virtual connection. To compensate for the lack of
| the  sentence  |     | level.  | The  | viewpoint  | of  | each  | sentence  is  |     |     |     |     |     |     |     |     |
| -------------- | --- | ------- | ---- | ---------- | --- | ----- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
confidence and quality in digitally managed marketplaces,
examined using sentence level classification. Each phrase is
consumers in digitally controlled markets might grade items
assumed to have a single point of view. When the aim is to
|     |     |     |     |     |     |     |     | based  on  | the  | degree  | of  expectation  |     | they  | meet.  It  | is  the  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ------- | ---------------- | --- | ----- | ---------- | -------- |
analyze more than one point of view in a text, sentence-level
|                 |     |     |            |                |     |            |      | consumer's  | responsibility  |     | to  convey  |        | his  or  | her  ideas  | and      |
| --------------- | --- | --- | ---------- | -------------- | --- | ---------- | ---- | ----------- | --------------- | --- | ----------- | ------ | -------- | ----------- | -------- |
| classification  |     | is  | required.  | ‘Furthermore,  |     | sentences  | are  |             |                 |     |             |        |          |             |          |
|                 |     |     |            |                |     |            |      | explain     | whether         | or  | not  the    | goods  | matched  | his         | or  her  |
classified in a distinct manner.
|     |     |     |     |     |     |     |     | expectations.  |     | The  capacity  |     | of  consumers  |     | to  exchange  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------------- | --- | -------------- | --- | ------------- | --- |
Another level of classification is termed document-level
|     |     |     |     |     |     |     |     | knowledge  | about  | the  | quality  | of  a  | product  | might  | assist  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ---- | -------- | ------ | -------- | ------ | ------- |
categorization when attempting to categories the perspective
alleviate customer uncertainty [9]. The capacity of a buyer to
of an entire document. As a result, it is not suitable when a
learn about a product's specifications, as detailed in reviews,
| work  | has  | many  | points  | of  view  | [5]The  | approach  | is  |          |             |            |     |            |           |            |     |
| ----- | ---- | ----- | ------- | --------- | ------- | --------- | --- | -------- | ----------- | ---------- | --- | ---------- | --------- | ---------- | --- |
|       |      |       |         |           |         |           |     | may  be  | a  crucial  | component  |     | in  their  | purchase  | decision.  |     |
unworkable since it is possible for a document to have more
|       |      |             |     |         |           |                 |     | Researchers  | have  | identified  |     | customer  | assessments  |     | as  an  |
| ----- | ---- | ----------- | --- | ------- | --------- | --------------- | --- | ------------ | ----- | ----------- | --- | --------- | ------------ | --- | ------- |
| than  | one  | viewpoint,  |     | making  | document  | classification  |     |              |       |             |     |           |              |     |         |
unresearched topic that might benefit other customers in their
impossible.
decision-making process.
Opinions may also be classified using user-level opinion
What the organization needs to know is why customers
analysis. This isn't a usual occurrence, but the researchers
would trust information provided by strangers, as well as
used it to investigate how a nearby user behaved. [6].'s major
how trust might be established in the consumers themselves.
objective was to assess consumer connectedness using user-
Credibility is a vital component of information sharing, and it
level sentiment analysis based on social media data. Aside
has a big influence on product sales since it encompasses
| from  | that,  | they  | sought  | to  see  | if  customers'  |     | views  of  |     |     |     |     |     |     |     |     |
| ----- | ------ | ----- | ------- | -------- | --------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
consumers' trust and reliability. Customers can not only write
connectedness altered as a result of the study.
reviews on Amazon, but they can also vote on whether or not
| The  | classification  |     | of  | aspects  | is  | another  | level  of  |     |     |     |     |     |     |     |     |
| ---- | --------------- | --- | --- | -------- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
the input of other customers is valuable. If consumers agree
| categorization.  |     | Using  | this  | method,  | product  |     | traits  and  |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------ | ----- | -------- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
with a reviewer's assessment, the voting provides a clear
attributes are highlighted in a phrase. For example, in the
direction and a path for decision-making through the counts.
| statement  | "The  | speaker  |     | of  the  | mobile  | is  excellent,"  | the  |                          |     |     |        |                              |     |     |     |
| ---------- | ----- | -------- | --- | -------- | ------- | ---------------- | ---- | ------------------------ | --- | --- | ------ | ---------------------------- | --- | --- | --- |
|            |       |          |     |          |         |                  |      | The vote of helpfulness  |     |     | is an  | indicator of the quality of  |     |     |     |
speaker serves as a foundation for making a decision. To
evaluations for other customers [10]. Reviews that include
complete the level, each sentence in a phrase can be utilizing
|     |     |     |     |     |     |     |     | helpful  | votes  | considerably  | affect  | a   | customer's  | decision- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ------------- | ------- | --- | ----------- | --------- | --- |
d. The first two phases in the process are to identify the
making process, and these reviews have a higher impact on
intended audience and obtain their feedback. The topic of the
the sales of lesser-known goods than they do on more well-
| previously  |     | indicated  | level  | is  | the  paper,  | paragraph,  | or  |     |     |     |     |     |     |     |     |
| ----------- | --- | ---------- | ------ | --- | ------------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
known ones.
sentences. Once you've discovered the difference between

| Paper ID: 2025/IJTRM/07/2025/45815  |     |     |     |     |     |     |     |     |     |     |     |     |     |         3  |     |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |

International Journal of Technology Research and Management
ISSN (Online): 2348-9006
Vol 12 Issue 07 July 2025
Review mining expectations and the performance of the product.If a product
Data collection is an essential component of every type of has the ability to positively effect a consumer, the customer's
investigation. Previously, researchers obtained reviews from expectations may be hypothesised as the probabilities of this
databases or a URL provided by the firm. A web crawler is occurring. Expectations cannot be idealized as a post-
frequently used to collect data automatically. [11] Collected purchase occurrence since they are a pre-purchase
data using a custom web crawler and stored it in a local phenomenon, but the customer implements them after
database. Utilize d the crawler to divide a huge work into viewing the goods.
smaller tasks and perform them in parallel.
Amazon assessments simply offer a product code and a
quick overview in the absence of a thorough explanation of a
product's attributes. It's difficult to gain relevant information
about a product from reviews if the information supplied is
incorrect. Consumers aren't expected to understand every
detail of a re-product view's description. Aside from
linguistic and emotional research, it is vital to uncover the
characteristics of the product that are enticing customers to
buy. Some of the reviews convey anything directly about the
product, while others provide characteristics that a reviewer
addresses. Product qualities are frequently described using
nouns and phrases. As a feature, an attribute of the subject or
an attribute of the subject's part must be retrieved. In the
review, product features may be mentioned explicitly4 or
implicitly is the year. Explicit qualities can be extracted Figure 1: Word Cloud of Amazon reviews
manually or automatically. The features can be manually
extracted by creating a vocabulary for qualities related to the Unstructured data provides information on consumers'
product feature and then extracting those features from opinions and experiences, product highlights, product feature
reviews. As a consequence, the data is divided into a number highlights, and other services such as product delivery,
of unique classes, which are subsequently extracted. packaging, and other pertinent difficulties. Customers also
give input on how a product or service should be improved,
Customer Satisfaction which includes their personal experiences. This data may also
When a customer is pleased with a product or service, it be utilize d to improve the product or service and create
implies that the product met their expectations. To marketing plans. [19] predicted customer happiness by
comprehend customer satisfaction as a pattern of elements exploiting the technological characteristics of online reviews
and related sensations, we must first recognize that customer and comments, as well as consumer interaction in an online
pleasure is based on the characteristic of the product or community, to predict customer contentment. As a result, a
service under consideration. Customers are pleased when number of essential concerns must be addressed in order to
their needs are addressed. A product that surpasses link product ratings with review material. The reviews
consumers' expectations satisfies their desires. describe technical issues (features), which explain the
A consumer can submit feedback in the form of text as variance in product ratings. Customer ratings based on
well as by rating the product. A lower rating indicates attributes or features can have a significant influence [20]
dissatisfaction, whereas a higher one indicates contentment.
A product rating is one of the most significant ways to assess 2. LITEARTURE REVIEW
a customer's level of satisfaction. One of the greatest methods
to determine how happy a consumer is with a product is to GhorbanTanhaei et al. (2024) developed a predictive
assign ratings to it [12]. A product rating cannot be used to customer relationship management framework using several
assess quality because it is a statement of client satisfaction. machine learning algorithms such as Decision Tree, Random
The study of customer happiness, which measures the Forest, Logistic Regression, Support Vector Machines, and
contentment of each individual consumer, is the fundamental Gradient Boosting. Their model evaluated customer behavior
notion in marketing research [13]. When it comes to using metrics like accuracy, recall, F1-score, and ROC-AUC.
customer satisfaction (CS), it all boils down to the customer's Random Forest and Logistic Regression outperformed the
Paper ID: 2025/IJTRM/07/2025/45815 4

International Journal of Technology Research and Management
ISSN (Online): 2348-9006
Vol 12 Issue 07 July 2025
rest, achieving high precision and recall. The study uncover patterns in consumer behavior. Their model
emphasized the practical value of linking client portfolios achieved a 92% prediction accuracy and emphasized the
with expenditure patterns to guide strategic marketing importance of analyzing language, emotion, and context in
decisions [14]. tweets. This study demonstrated the utility of social media
Prakash et al. (2023) presented a comprehensive data for marketing and decision-making, showcasing the
literature review exploring how AI-driven techniques like potential of machine learning for behavioral trend detection
machine learning, natural language processing (NLP), and [20].
deep learning are used to predict consumer behavior. The Kurat et al. (2024) explored how predictive analytics and
study covered applications such as recommendation engines, various machine learning techniques—such as supervised,
sentiment analysis, and market forecasting while identifying unsupervised, and deep learning—can enhance market
key challenges like data privacy, ethical concerns, and analysis. The study focused on demand forecasting, price
system integration. The work laid the foundation for future optimization, and preference pattern identification using large
research in AI-based consumer behavior prediction [15]. datasets. It also addressed challenges like data quality and
Kothari et al. (2024) proposed a novel Machine algorithmic bias, concluding that ML-driven analytics
Learning-based Customer Behavior Model (MLbCBM), significantly improve strategic decision-making and business
which integrates Logistic Regression, Decision Tree, responsiveness [21].
Random Forest, KNN, SVM, and Naïve Bayes algorithms. Ojika et al. (2024) proposed a conceptual ML framework
The model demonstrated high accuracy rates (up to 89.9%) to analyze e-commerce trends and customer behavior. The
across various classifiers. It uses data collected from e- framework includes advanced analytics like segmentation,
commerce platforms to detect emerging customer behavior sentiment analysis, recommendation systems, and predictive
patterns and facilitate decision-making through a server- modeling. The goal was to increase customer engagement
based processing framework [16]. and conversion rates through data-driven marketing strategies,
Basal et al. (2025) focused on predicting customer churn while acknowledging implementation challenges and
in subscription-based services using machine learning models suggesting future research directions [22].
like Random Forest, Logistic Regression, Gradient Boosting, Elamin et al. (2024) introduced a Bayesian-optimized
and XGBoost. They employed Kaggle datasets and evaluated Long Short-Term Memory (LSTM) model to predict media
performance using confusion matrices and other metrics. The consumption behavior. By integrating Bayesian optimization
study particularly emphasized ethical considerations in with LSTM networks, the model achieved superior accuracy
predictive analytics and recommended targeted retention over other ML approaches such as Random Forest, RNNs,
strategies and integration of new data sources to reduce churn and Gradient Boosting. This study provided a robust
rates [17]. methodology for modeling sequential behavior in rapidly
Babu et al. (2025) introduced a novel application of the evolving media consumption environments [23].
Reformer (Reversible Transformer) model to analyze Chaudhary et al. (2021) investigated consumer behavior
massive social media datasets and predict customer sentiment on various social media platforms using big data analytics.
and industry trends. Their study, particularly relevant for They collected diverse, high-speed data from Facebook,
smart transportation and logistics, demonstrated that the Twitter, LinkedIn, and others, and used machine learning to
Reformer outperformed traditional models in accuracy and build predictive models. The research involved
efficiency. The work highlighted the growing role of social comprehensive preprocessing to clean the data and used
media analytics in real-time strategic business decisions [18]. predictive analytics to understand user engagement and
Chaudhuri et al. (2021) aimed to improve the perception on social platforms [24].
understanding of online consumer purchasing behavior Jamal et al. (2024) conducted a qualitative study
through deep learning. By analyzing over 50,000 analyzing how AI—specifically machine learning and natural
multidimensional web sessions, they evaluated the predictive language processing—affects marketing strategies and
power of deep learning against traditional ML models like customer behavior prediction. By reviewing over 60
Decision Tree, Random Forest, SVM, and ANN. Their publications and case studies, the study highlighted AI’s role
findings showed that deep learning methods yielded superior in enhancing marketing precision while addressing
results, making them suitable for predicting user behavior on challenges related to data quality, integration, and security.
e-commerce platforms [19]. Recommendations included improving AI talent and
Dhiman et al. (2024) analyzed Twitter data using embedding AI into existing platforms for better strategic
Logistic Regression and Multinomial Naïve Bayes to outcomes [25].
Paper ID: 2025/IJTRM/07/2025/45815 5

International Journal of Technology Research and Management
ISSN (Online): 2348-9006
|     |     |     |     |     |     | Vol 12 Issue 07 July 2025  |     |
| --- | --- | --- | --- | --- | --- | -------------------------- | --- |

Khan et al. (2025) examined the impact of packaging  Nisha et al. (2023) conducted a similar study to Juárez-
design on consumer decisions related to educational toys  Varón et al., using the same dataset to examine customer
using  neuromarketing and  machine  learning. Their  model  buying behavior on e-commerce platforms. They compared
analyzed  which  parts  of  the  packaging  drew  customer  traditional  ML  models (DT, SVM, RF, ANN) with deep
attention using eye-tracking and other behavioral indicators.  learning methods and concluded that deep learning models
The  study  revealed  that  visual  elements  significantly  delivered  better  performance.  The  results  provided
influence  purchasing  decisions  and  emphasized  the  meaningful insights for online retail platforms to optimize
importance of social and contextual factors [26].  user engagement and sales forecasting [28].
Juárez-Varón  et  al.  (2020)  explored  online  purchase  Agrawal  et  al.  (2021)  focused  on  customer  churn
prediction using a dataset of over 50,000 web sessions. The  prediction  in  the  telecom  industry  using  a  deep  learning
study identified platform engagement and customer attributes  approach. They developed a multi-layered neural network
as the two main predictors of purchase intent. Comparing  model using features related to customer behavior, service
multiple ML techniques, including DT, SVM, RF, and ANN,  usage, and support history. Achieving an 80.03% accuracy,
they  found  deep  learning  to  outperform  the  others.  The  the  model  helped  identify  high-risk  churn  customers  and
research  offered  insights  valuable  for  e-commerce  allowed companies to understand churn causes and improve
development  and  academic  advancements  in  consumer  customer retention strategies [29].
| analytics [27].  |     |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- |

Table 1: Literature Review Table: Predictive Analytics & ML for Customer Behavior

Author(s)  Year  Objective  Methods /  Dataset /  Key Results  Contribution
|     |     |     | Models Used  | Source  |     |     |     |
| --- | --- | --- | ------------ | ------- | --- | --- | --- |
GhorbanTanh 2024  Forecast  DT, RF, LR,  Client  RF & LR:  ML for strategic
aei et al.  customer actions  SVM, Gradient  spending  High ROC-AUC  CRM with model-
and support  Boosting  behavior data  (0.878), F1  based customer
|     |     | CRM  |     |     |     | (0.766), Recall  | segmentation  |
| --- | --- | ---- | --- | --- | --- | ---------------- | ------------- |
(1.0)
Prakash et al.  2023  Review AI in  ML, NLP, Deep  Literature  -  Broad overview
|     |     | customer  | Learning  | & case studies  |     |     | of tools and         |
| --- | --- | --------- | --------- | --------------- | --- | --- | -------------------- |
|     |     | behavior  |           |                 |     |     | challenges (ethics,  |
prediction  privacy)
Kothari et al.  2024  ML-based  LR, DT, RF,  E- RF (89.9%),  Server-based
Customer  KNN, SVM, NB  commerce  SVM (88.8%),  model analyzing
|     |     | Behavior Model  |     | platforms  |     | NB (88.6%)  | market behavior  |
| --- | --- | --------------- | --- | ---------- | --- | ----------- | ---------------- |
(MLbCBM)
Basal et al.  2025  Predict churn  RF, LR, GB,  Real-world  Accurate  Actionable churn
in subscription  XGBoost  & Kaggle  predictions;  prediction
|     |     | services  |     | datasets  |     | ethical focus  | framework with  |
| --- | --- | --------- | --- | --------- | --- | -------------- | --------------- |
evaluation metrics
Babu et al.  2025  Use  Reformer  Social  Superior  Applied NLP for
Reformer for  (Reversible  media datasets  precision, F1,  market trends and
|     |     | social media- | Transformer)  |     |     | recall  | demand prediction  |
| --- | --- | ------------- | ------------- | --- | --- | ------- | ------------------ |
based insights
Chaudhuri et  2021  Predict e- DL, DT, RF,  50K+ web  DL  Showed DL
al.  commerce  SVM, ANN  sessions  outperformed ML  strength in modeling
|     |     | purchases  |     |     |     |     | purchase behavior  |
| --- | --- | ---------- | --- | --- | --- | --- | ------------------ |
Dhiman et al.  2024  Predict  LR,  Twitter  92% accuracy  Trends from
|     |     | consumer trends  | Multinomial Naïve  | data  |     |     | tweets support       |
| --- | --- | ---------------- | ------------------ | ----- | --- | --- | -------------------- |
|     |     | from Twitter     | Bayes              |       |     |     | marketing decisions  |

| Paper ID: 2025/IJTRM/07/2025/45815  |     |     |     |     |     |     |           6  |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | ------------ |

International Journal of Technology Research and Management
ISSN (Online): 2348-9006
|     |     |     |     |     |     |     |     |     |     | Vol 12 Issue 07 July 2025  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- |

Kurat et al.  2024  Market  DL, Supervised  Real-time  Predictive  ML enables real-
forecasting  & Unsupervised  & historical  accuracy for  time adaptive
using ML &  ML  market data  demand & pricing  market strategies
predictive
analytics
Ojika et al.  2024  Conceptual  Sentiment  Multi- Improved  Comprehensive
ML framework  Analysis,  source data  engagement,  ML-enabled
|     |     |     | for e-commerce  |     |     | Clustering,  |     |     | conversions  |     |     | business decision  |
| --- | --- | --- | --------------- | --- | --- | ------------ | --- | --- | ------------ | --- | --- | ------------------ |
|     |     |     |                 |     |     | Predictive   |     |     |              |     |     | system             |
Modeling
Elamin et al.  2024  Forecast  Bayesian- Media  99% accuracy  Enhanced
media  optimized LSTM  consumption  (better than RF,  temporal modeling
|     |     |     | consumption  |     |     |     | datasets  |     |     | GB)  |     | using Bayesian  |
| --- | --- | --- | ------------ | --- | --- | --- | --------- | --- | --- | ---- | --- | --------------- |
tuning
2021  Predict  Big Data + ML  Facebook,  High-quality  Forecasted user
Chaudhary et
al.  behavior from  Twitter,  results via  interaction trends on
social media use  YouTube, etc.  preprocessing  social platforms
|     |     | 2024  |     | AI’s effect  |     | ML, NLP,  | 60+  |     |     | -   |     | Identified AI  |
| --- | --- | ----- | --- | ------------ | --- | --------- | ---- | --- | --- | --- | --- | -------------- |
Jamal et al.
on marketing  Literature Analysis  studies, cases  benefits, risks in
|     |     |     |     | strategy  |     |     |     |     |     |     |     | marketing and  |
| --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | -------------- |
advertising
| Khan et al.  |     | 2025  |     | Study  |     | ML +  | Eye- |     |     | Visual  |     | Segmented  |
| ------------ | --- | ----- | --- | ------ | --- | ----- | ---- | --- | --- | ------- | --- | ---------- |
packaging  Neuromarketing  tracking  elements  packaging zones via
|     |     |     |     | influence on  |     |     | experiment  |     | influence  |     |     | behavior analysis  |
| --- | --- | --- | --- | ------------- | --- | --- | ----------- | --- | ---------- | --- | --- | ------------------ |
|     |     |     |     | purchase      |     |     | data        |     | decisions  |     |     |                    |
Juárez-Varón  2020  E-commerce  DL, DT, RF,  50K+ web  DL superior in  Aid for platform
et al.  purchase  SVM, ANN  sessions  predictions  development & user
|     |     |     |     | prediction  |     |     |     |     |     |     |     | profiling  |
| --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | ---------- |
Nisha et al.  2023  Predict e- DL vs ML (DT,  Web  DL  Improved online
commerce  RF, SVM, ANN)  session dataset  outperforms ML  purchase forecasting
behavior
Agrawal et al.  2021  Predict  Deep Neural  Telco  80.03%  Identified key
telecom  Network  churn dataset  success rate  churn drivers with
|     |     |     | customer churn  |     |     |     |     |     |     |     |     | actionable insights  |
| --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------- |

  field by enabling the modeling of sequential and unstructured
3.  CONCLUSION  data with higher accuracy. Social media analytics, sentiment
analysis, and customer churn prediction have emerged as key
The prediction and analysis of customer behavior have  applications. Despite these advances, challenges remain in
become essential for organizations aiming to retain customers,  terms  of  interpretability,  data  privacy,  and  the  need  for
personalize  services,  and  enhance  business  outcomes.  domain-specific model tuning. Future research should focus
Through this review, it is evident that machine learning and  on developing more explainable AI models, improving real-
deep  learning  techniques  offer  powerful  tools  for  time  prediction  capabilities,  and  integrating  ethical
understanding complex patterns in customer data. Traditional  frameworks for responsible data usage. Ultimately, a hybrid
algorithms  like  Decision  Trees,  Logistic  Regression,  and  approach that balances traditional models with deep learning,
tailored to specific industries, holds the most promise for
| Random  | Forest  | continue  | to  | provide  | valuable  | insights,  |     |     |     |     |     |     |
| ------- | ------- | --------- | --- | -------- | --------- | ---------- | --- | --- | --- | --- | --- | --- |
particularly  when  combined  with  ensemble  techniques.  accurate and actionable customer behavior prediction.
However, the rise of deep learning models such as LSTM and
| Transformer  | architectures  |     | has  | significantly  | advanced  | the  |     |     |     |     |     |     |
| ------------ | -------------- | --- | ---- | -------------- | --------- | ---- | --- | --- | --- | --- | --- | --- |

| Paper ID: 2025/IJTRM/07/2025/45815  |     |     |     |     |     |     |     |     |     |     |     |         7  |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- |

International Journal of Technology Research and Management
ISSN (Online): 2348-9006
Vol 12 Issue 07 July 2025
REFERENCES Computing, Communication, Machine Learning and AI (ICCCMLA).
IEEE.
[16] Kothari, B., & Mani, A. P. (2024). MLbCBM: Machine learning-based
[1] Thelwall, M., Wilkinson, D., & Uppal, S. 2010. Data mining emotion consumer behavior model to analyze emerging trends and influences in
in social network communication: Gender differences in MySpace. market. In Proceedings of Fifth International Conference on
Journal of the American Society for Information Science and Computing, Communications, and Cyber-Security (IC4S 2023) (pp.
Technology, 61(1), 190-199. 397–411). Lecture Notes in Networks and Systems, 1128.
[2] Ting, P. L., Chen, S., Chen, H., & Fang, W. 2017. Using big data and [17] Basal, M., Moulai, K., & Cetin, A. (2025). Predictive analytics for
text analytics to understand how customer experiences posted on customer behavior prediction in artificial intelligence. Economics
yelp.com impact the hospitality industry. Contemporary Management World, 12(2), 142–154.
Research, 13(2), 107-130. [18] Babu, M. A., Ahammad, M., Mahmud, M., & Uddin, M. S. (2025).
[3] Turney, P. D. 2002. Thumbs up or thumbs down?: semantic orientation Social media as a market prophecy: Leveraging ML algorithms for
applied to unsupervised classification of reviews. In Proceedings of the predicting market trends and demand. Transportation Research
40th annual meeting on association for computational linguistics, 417- Procedia, 84, 137–144.
424. Association for Computational Linguistics. Stroudsburg, PA, [19] Chaudhuri, N., Gupta, G., Vamsi, V., & Bose, I. (2021). On the
USA. platform but will they buy? Predicting customers' purchase behavior
[4] Vala, M., & Gandhi, J. 2015. Survey of Text Classification Technique using deep learning. Decision Support Systems, 149, 113622.
and Compare Classifier. International Journal of Innovative Research https://doi.org/10.1016/j.dss.2021.113622 1.
in Computer and Communication Engineering, 3(11), 10809-10813. [20] Dhiman, K., & Tyagi, S. (2024, April 19–20). Machine learning
[5] Wilson, T., Wiebe, J., & Hwa, R. 2004. Just how mad are you? Finding insights: Deciphering consumer behavior from Twitter trends and
strong and weak opinion clauses. In Proceedings of AAAI-04, 21st tweets. 2024 International Conference on Communication, Computing
Conference of the American Association for Artificial Intelligence, and Internet of Things (CCICT). IEEE.
761–769. San Jose, US. https://doi.org/10.1109/CCICT62777.2024.00078
[6] Wilson, T., Wiebe, J., & Hoffmann, P. 2005. Recognizing contextual [21] Kurat, J. (2024, December 17). Enhancing market insights with
polarity in phrase-level sentiment analysis. In Proceedings of Human advanced machine learning and predictive analytics techniques.
Language Technology Conference and Conference on Empirical [22] Ojika, F. U., Onaghinor, O., Esan, O. J., Daraojimba, A. I., &
Methods in Natural Language Processing, 347-354. Ubamadu, B. C. (2024). Creating a machine learning-based conceptual
[7] Woolf, M. 2014. A Statistical Analysis of 1.2 Million Amazon framework for market trend analysis in e-commerce: Enhancing
Reviews unpublished manuscript, June 17, 2014. Available at customer engagement and driving sales growth. International Journal
https://minimaxir.com/2014/06/reviewing-reviews. of Multidisciplinary Research and Growth Evaluation, 5(1), 1647–
[8] Xu, X., Li, Y., & Lu, A. C. C. 2019. A comparative study of the 1656. https://doi.org/10.54660/IJMRGE.2024.5.1.1647-1656
determinants of business and leisure travellers' satisfaction and [23] Elamin, A. E. A. M. A. (2024). Deep learning-based mathematical
dissatisfaction. International Journal of Services and Operations modelling for predictive analysis in media consumer behaviour.
Management, 33(1), 87-112. College of Science and Humanities, Prince Sattam bin Abdulaziz
[9] Xu, X., & Li, Y. 2016. The antecedents of customer satisfaction and University. Published online: March 1, 2024.
dissatisfaction toward various types of hotels: A text mining approach. [24] Chaudhary, K., Alam, M., & Gumaei, A. (2021). Machine learning-
International journal of hospitality management, 55, 57-69. Yang, Y., based mathematical modelling for prediction of social media consumer
& Chute, C. G. 1994. An example-based mapping method for text behavior using big data analytics. Journal of Big Data, 8, Article 73.
categorization and retrieval. In proceedings of ACM Transactions on https://doi.org/10.1186/s40537-021-00454-1
Information Systems (TOIS), 12(3), 252-277. New York, USA. [25] Jamal, A. (2024, December 13). Optimizing market analysis with
[10] Yassine, M., & Hajj, H. 2010. A framework for emotion mining from machine learning algorithms and predictive analytics.
text in online social networks. In proceedings of IEEE International [26] Khan, A., Abdul Hamid, A. B., Siddiqui, H. A., & Tan, C. F. (2025).
Conference on Data Mining Workshops, 1136-1142. IEEE. Shaping business behavior through generative AI: Predicting future
[11] Yi, Y. 1991. A Critical Review of Customer Satisfaction. In Review of consumer trends in marketing. International Journal of Academic
Marketing,Valarie A. Zeithmal, ed. pp. 68-123. Chicago: American Research in Business and Social Sciences, 15(4).
Marketing Association. https://doi.org/10.6007/IJARBSS/v15-i4/25293
[12] Yi, J. and Niblack, W. 2005. Sentiment mining in WebFountain. [27] Juárez-Varón, D., Tur-Viñes, V., Rabasa-Dolado, A., & Polotskaya, K.
Proceedings of the 21st International Conference on Data Engineering, (2020). An adaptive machine learning methodology applied to
1073-1083. IEEE. neuromarketing analysis: Prediction of consumer behaviour regarding
[13] Yoo, K., & Gretzel, U. 2011. Influence of personality on travel-related the key elements of the packaging design of an educational toy. Social
consumer-generated media creation. Computers in Human Behavior, Sciences, 9(9), 162. https://doi.org/10.3390/socsci9090162
27(2), 609-621. [28] Nisha, & Singh, A. S. (2023, March 3–5). Customer behavior
[14] Zhao, Y., Xu, X., & Wang, M. 2019. Predicting overall customer prediction using deep learning techniques for online purchasing. 2023
satisfaction: Big data evidence from hotel online textual reviews. International Conference on Intelligent and Innovative Computing
International Journal of Hospitality Management, 76, 111-121. Applications (INOCON). IEEE.
[15] GhorbanTanhaei, H., Boozary, P., Sheykhan, S., Rabiee, M., Rahmani, https://doi.org/10.1109/INOCON57975.2023.10101102
F., & Hosseini, I. (2024). Predictive analytics in customer behavior: [29] Agrawal, S., Das, A., Gaikwad, A., & Dhage, S. (2021, July 11–12).
Anticipating trends and preferences. Results in Control and Customer churn prediction modelling based on behavioural patterns
Optimization, 17, 100462. Prakash, S., Malli Babu, S., Kumar, P. P., analysis using deep learning. 2021 International Conference on Smart
Devi, S., & Reddy, K. P. (2023, October 7–8). Predicting consumer City and Emerging Technology (ICSCET). IEEE.
behaviour with artificial intelligence. 2023 International Conference on https://doi.org/10.1109/ICSCEE.2018.8538420
Paper ID: 2025/IJTRM/07/2025/45815 8