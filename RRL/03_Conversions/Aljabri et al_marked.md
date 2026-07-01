Social Network Analysis and Mining (2023) 13:20
https://doi.org/10.1007/s13278-022-01020-5
ORIGINAL ARTICLE
Machine learning‑based social media bot detection: a comprehensive
literature review
Malak Aljabri1 · Rachid Zagrouba3 · Afrah Shaahid2 · Fatima Alnasser2 · Asalah Saleh2 · Dorieh M. Alomari4
Received: 24 October 2022 / Revised: 30 November 2022 / Accepted: 20 December 2022 / Published online: 5 January 2023
© The Author(s) 2023
Abstract
In today’s digitalized era, Online Social Networking platforms are growing to be a vital aspect of each individual’s daily
life. The availability of the vast amount of information and their open nature attracts the interest of cybercriminals to create
malicious bots. Malicious bots in these platforms are automated or semi-automated entities used in nefarious ways while
simulating human behavior. Moreover, such bots pose serious cyber threats and security concerns to society and public
opinion. They are used to exploit vulnerabilities for illicit benefits such as spamming, fake profiles, spreading inappropriate/
false content, click farming, hashtag hijacking, and much more. Cybercriminals and researchers are always engaged in an
arms race as new and updated bots are created to thwart ever-evolving detection technologies. This literature review attempts
to compile and compare the most recent advancements in Machine Learning-based techniques for the detection and clas-
sification of bots on five primary social media platforms namely Facebook, Instagram, LinkedIn, Twitter, and Weibo. We
bring forth a concise overview of all the supervised, semi-supervised, and unsupervised methods, along with the details of
the datasets provided by the researchers. Additionally, we provide a thorough breakdown of the extracted feature categories.
Furthermore, this study also showcases a brief rundown of the challenges and opportunities encountered in this field, along
with prospective research directions and promising angles to explore.
Keywords Social media security · Bot detection · Machine learning · Social bots · Feature engineering · Cybersecurity
1 Introduction
human social interactions where users and their communi-
ties are the base for online growth, commerce, and infor-
In this modern world, OSNs such as Twitter, Facebook, Ins- mation sharing. Different social networks offer a unique
tagram, LinkedIn have become a crucial part of each one’s value chain and target different user segments. For instance,
life (Albayati and Altamimi 2019). It radically impacts daily Twitter is known for being the most famous microblogging
* Malak Aljabri 2 SAUDI ARAMCO Cybersecurity Chair, Department
mssjabri@uqu.edu.sa of Computer Science, College of Computer Science
and Information Technology, Imam Abdulrahman Bin Faisal
Rachid Zagrouba
University, P.O. Box 1982, Dammam 31441, Saudi Arabia
rmzagrouba@iau.edu.sa
3 SAUDI ARAMCO Cybersecurity Chair, Department
Afrah Shaahid
of Computer Information Systems, College of Computer
2190009057@iau.edu.sa
Science and Information Technology, Imam Abdulrahman
Fatima Alnasser Bin Faisal University, P.O. Box 1982, Dammam 31441,
2190003750@iau.edu.sa Saudi Arabia
Asalah Saleh 4 SAUDI ARAMCO Cybersecurity Chair, Department
2160007924@iau.edu.sa of Computer Engineering, College of Computer Science
and Information Technology, Imam Abdulrahman Bin Faisal
Dorieh M. Alomari
University, P.O. Box 1982, Dammam 31441, Saudi Arabia
2180007089@iau.edu.sa
1 Department of Computer Science, College of Computers
and Information Systems, Umm Al-Qura University,
Makkah 21955, Saudi Arabia
Vol.:(0112 33456789)

20 Page 2 of 40 Social Network Analysis and Mining (2023) 13:20
social network for receiving rapid updates and breaking opinion, such activities not only disturb the genuine users’
news. While Instagram usage is mainly by celebrities and experience but also lead to a negative effect on the pub-
businesses for marketing (Meshram et al. 2021). Whereas lic’s and individual’s security. As a result, in recent years,
professional communities use LinkedIn. As social networks' researchers have dedicated a significant amount of attention
popularity grows combined with the availability of vast per- to social media bot detection (Ali and Syed 2022; Ferrara
sonal information that users share makes the same valuable 2018; Rangel and Rosso 2019; Yang et al. 2012) and preven-
features of social platforms for ordinary people a tempting tion (Thakur and Breslin 2021).
target for malicious entities (Adikari and Dutta 2020). The
1.1 Social media platforms
most prevalent form of malware on social media networks
is thought to be bots (Aldayel and Magdy 2022; Cai, Li, and
Zengi 2017b). Some bots are benign. However, the major- OSNs have revolutionized communication technologies
ity of bots are utilized to perform malicious activities such and are now an essential component of the modern web.
as fabricating accounts, faking engagements, social spam- The most popular social networks globally as of January
ming, phishing, and spreading rumors to manipulate public 2022 are shown in Fig. 1, ordered by the number of monthly
Fig. 1 Most popular social networks globally as of January 2022, ordered by no. of monthly active users.https:// www. stati sta. com/ stati stics/
272014/ global- social- netwo rks- ranked- by- number- of- users/
1 3

Social Network Analysis and Mining (2023) 13:20 Page 3 of 40 20
active users in millions. The social media platforms which (Ferrara 2020), creating fake reputations, and suppressing
are included in the scope of our study are namely Twit- political competitors (Pierri et al. 2020; Benkler et al. 2017).
ter, Facebook, Instagram, LinkedIn, and Weibo. On these Despite the fact that bots are extensively used, little research
platforms, user growth and popularity have been increas- has been done to examine how they affect the social media
ing at an exponential rate. These platforms enable users to environment. This indicates that nearly 48 million of the
produce and exchange user-generated content (Kaplan and accounts on Twitter are bots (Sheehan 2018). It was also
Haenlein 2010). For instance, only 2.375 billion people were stated that Facebook acknowledges that 270 million of its
using Facebook in the first quarter of 2019 (Siddiqui 2019), accounts are fake (Sheehan 2018). Further, there is evidence
thereby representing one-third of the world population that social media bots were utilized to attempt to influence
(Caers et al. 2013). One of the most widespread and exten- political communication dates during the US midterm elec-
sively used OSN by people from all walks of life is Twit- tions in 2010. There were also allegations that social bots
ter. Twitter allows individuals to express their sentiments on Twitter played a significant role in the 2016 US presiden-
on different topics such as entertainment, the stock market, tial election (Cresci et al. 2017; Mahesh 2020; Sedhai and
politics, and sports. (Wald et al. 2013). It is one of the fastest Sun 2015). Bots can be employed to spread misinformation
means of circulating information as a result extremely affects to promote a particular view of a public person, grow an
people’s perspectives. Over the past few years, Twitter has account's following, and repost user-generated content. Bot
become a replacement for mainstream media for obtaining detection on OSNs is therefore the most frequently requested
news (Wald et al. 2013). On the other hand, Instagram is an security feature from businesses and law enforcement
OSN for sharing photos and videos and is accessible on both organizations (Kolomeets and Chechulin 2021). The dearth
Android and iOS since 2012. Dated May 2019, there were of publicly accessible datasets for OSNs such as Facebook,
more than a billion users registered on Instagram, according Instagram, and LinkedIn is one of the greatest obstacles in
to collected data (Thejas et al. 2019). Moving on, Facebook this research area. Unlike Twitter, this restriction results
is an online social networking site that makes it convenient from some of these OSNs’ limited data collection policies.
for people to connect and share with family and friends. It
1.3 Types of bots on social media
was developed in 2004 initially for students by Mark Zuck-
erberg. With more than 1 billion users globally, Facebook is
one of the biggest social networks in the current times (San- The term "bot" refers to a robot, a computer program that
tia et al. 2019). One of the most well-known professional works more quickly than humans at recurring, automated
social networks is LinkedIn, a platform that focuses on pro- tasks. More precise terminology can be used to define bots
fessional networking and career advancement (Dinath 2021). in OSNs "a computer software that generates content auto-
Sina-Weibo, also known as Chinese Twitter, was launched in matically and engages with users of social media to rep-
2009, and this microblogging website or application is one licate and possibly modify their behavior" (Benkler et al.
of China’s biggest social media platforms. It offers a plethora 2017). Bots can be used for useful or harmful reasons and
of features which include posting images, instant messaging, often replicate human behavior to some degree (Fonseca
Weibo stories, using location-based hashtags, trending top- Abreu et al. 2020). Good bots can significantly reduce the
ics, etc. Furthermore, it also gives businesses the privilege need for human customer service representatives for some
to set up accounts for the purpose of advertisements and businesses, such as chatbots and news bots that automati-
services (Tenba Group 2022). cally upload new articles or news for journalists or blog-
gers. Bots can be employed for negative as well as positive
1.2 Social media security
purposes. According to (Gorwa and Guilbeault 2020), bots
are responsible for a sizable portion of online activity, are
Security and trustworthiness among users, service provid- used to manipulate algorithms and recommender systems,
ers, platform owners, and third-party supervisors are critical stifle or promote political speech, and can be crucial in the
factors for social media platforms’ success and stable exist- spread of hyper-partisan "fake news." According to (Ben-
ence (Zhang and Gupta 2018). According to recent surveys kler et al. 2017), there are four different categories of social
(Shearer and Mitchell 2022), a considerable segment of the media bots: spambots, social bots, sybil bots, and cyborgs.
population prefers social networks to TV, newspapers, and Promoter bots, URL spambots, and false followers are only
other traditional media when looking for information. Trust a few examples of the various types of spambots that spread
in social networks as a source of information is predicted to harmful links, uninvited messages, and hijack popular sub-
rapidly grow (Kolomeets and Chechulin 2021). As a result, jects on social networks (Meshram et al. 2021). On the
social bots can pose significant security risks by influencing other hand, social bots are algorithmically controlled user
public opinion and disseminating false information (Shao accounts that mimic the activity of human users but carry
et al. 2017), spreading rumors and conspiracy theories out their tasks at a considerably faster rate while successfully
1 3

20 Page 4 of 40 Social Network Analysis and Mining (2023) 13:20
concealing their robotic identity (Ferrara 2018). While networking sites such as Facebook and Twitter, numerous
cyborgs bots are half-human, half-bot accounts that exist ML techniques were employed. For instance, existing ML
between people and bots, sybil bots are anonymous identi- algorithms can determine the user's location, carry out sen-
ties, i.e., user accounts, utilized for a significantly big effect timent analysis, (Aljabri et al. 2021a, b) offer recommen-
(Gorwa and Guilbeault 2020). In this review, the collected dations, and much more. Diverse ML methods have been
papers were incorporating three categories of bots which are successfully deployed to address wide-ranging problems
social bots spambots, and sybil bots. in cybersecurity which include detecting malicious URLS,
classification of firewall log data, phishing attacks detection,
1.4 The different machine learning‑based
etc. (Aljabri et al. 2022a, b, c; AAljabri and Mirza 2022).
techniques and algorithms
However, malicious software can be used to target social
media platforms and carry out cyber-attacks. In terms of
The development of algorithms that allow a computer to social media, several efforts have been undertaken to inves-
learn on its own from data and prior experiences is the tigate ML techniques to detect such types of malware. For
core of ML, a subfield of artificial intelligence (AI). Arthur instance, (Alom et al. 2020) detected Twitter spammers
Samuel was the first to originate the term "Machine Learn- using DL techniques. Moreover, the study conducted by
ing" (Wiederhold and McCarthy 1992). ML system devel- (Kantartopoulos et al. 2020) addressed the effects of hostile
ops prediction models based on previous data and makes attacks and utilized KNN as a measure to tackle the prob-
predictions up until new data are gathered. The amount of lem. The authors presented a methodology that uses SVM
data used to create a model determines its accuracy (Sara- and Ensemble algorithms to effectively detect cyberbullying
nya Shree et al. 2021). The various types of ML techniques (Gupta and Kaushal 2017). Additionally, models have been
include Supervised, Semi-supervised, Unsupervised, and developed for social media systems’ access control (Carmin-
Reinforcement. However, we have only included Supervised, ati et al. 2011). Yet, bot and fake account detection on social
Semi-supervised, and Unsupervised as a part of our study. media platforms are still one of the primary challenges for
Three types are present under supervised category: Clas- cyber security researchers (Thuraisingham 2020).
sification, Regression, and Forecasting. Some of the most
1.6 Key contributions
popular supervised algorithms include Random Forest (RF),
Naïve Bayes (NB), Decision Trees (DT), Logistic Regres-
sion (LR), Support Vector Machine (SVM), Neural Net- This section firstly puts forth the existing literature reviews
works (NN), and many more. Deep learning (DL) is a subset done on different social media platforms as shown in
of supervised ML techniques that employs multiple layers to Table 1. It also briefly discusses the previously used tax-
gradually extract higher-order features from the input data. onomies along with the prevailing gaps. Starting with the
In order to create patterns and process data, this AI technol- literature review on Twitter, (Alothali et al. 2019) included
ogy mimics the actions and processes of the human brain literature concerning from 2010 to 2018 based on vari-
(Gannarapu et al. 2020). Convolutional Neural Networks ous techniques which include Graph-based, Crowdsourc-
(CNNs), Long Short-Term Memory Networks (LSTMs), ing, and ML. They analyzed the common aspects such as
Generative Adversarial Networks (GANs), etc., are some datasets, classifiers, and the selected features employed.
of the well-known DL algorithms. Whereas unsupervised The challenges present in the domain were also addressed.
learning algorithms are namely categorized into Cluster- (Derhab et al. 2021) discussed existing techniques and put
ing and Association which mainly deal with unlabeled data. forth a taxonomy that addressed the state-of-the-art tweet-
Some of the primarily used ones include K-nearest Neighbor based bot detection techniques in the timeline from 2010
(KNN), K-means clustering, Principal Component Analysis to 2020. Based on tweet-based bot detection techniques,
(PCA), etc. However, a small amount of labeled data and a they provided the main features utilized. For tweet-based
large amount of unlabeled data are utilized in semi-super- bot detection, they also described big data analytics shal-
vised learning, which results in a hybrid of supervised and low and DL techniques, in addition to their performance
unsupervised learning (Mahesh 2020). results. Finally, the challenges and open issues in the area
of tweet-based bot detection were presented and discussed
1.5 Machine learning implementation on social
(Derhab et al. 2021). Furthermore, (Orabi et al. 2020) dis-
media security
cussed the studies from 2010 to 2019 on Graph-based,
ML-based, Crowdsourcing, and Anomaly-based. Their
The way people use social media is evolving as a result research revealed some gaps in the literature, such as the
of the proliferation of ML techniques in social media and fact that studies discussed mainly Twitter, and that unsu-
the increased sophistication of cyberattacks on computer pervised ML is rarely used, in addition to the majority
information systems (Aljabri et al. 2021a, b). On social of publicly available datasets being either inaccurate or
1 3

Social Network Analysis and Mining (2023) 13:20 Page 5 of 40 20
Table 1 Summary of existing literature reviews
References Range of Taxonomy Open issue/
papers future dis-
reviewed cussion
Alothali et al. (2019) 2010–2018 Graph-based, crowdsourcing, and machine learning ✓
Derhab et al. (2021) 2010–2020 Shallow learning-based (supervised learning, semi-supervised learning, and unsuper- ✓
vised learning)
Deep learning-based-Deep learning-based
Orabi et al. (2020) 2010–2019 Graph-based, machine-learning based, crowdsourcing, anomaly-based ✓
Gheewala and Patel (2018) 2010–2017 Clustering algorithms, classification algorithms, hybrid ✗
Ezarfelix et al. (2022) 2018–2021 Logistics regression, naive bayes, random forest, support vector machine ✓
Rao et al. (2021) 2015–2020 URL list-based spam filtering techniques, honeypot/honeynet-based techniques, ✓
machine learning and deep learning techniques
insufficiently large. In (Gheewala and Patel 2018), con- • Provide summaries and analysis of the used ML-based
tributed a review on ML twitter spam detection for the (supervised, semi-supervised, and unsupervised) clas-
years 2010–2017 based on Clustering, Classification, and sification techniques to detect various types of bots on
Hybrid algorithms. Some of the issues concluded were some particular social media platforms.
regarding the results being lowered as a result of concerns • Provide a unique taxonomy based on the various ML-
with feature fabrication, class imbalance, spam drift, etc., based techniques which has not been provided in the
for spam detection. The study (Ezarfelix et al. 2022) per- existing literature.
formed was based only on the Instagram platform where • Identify and analyze the most commonly extracted and
a multitude of analyses, and evaluations have been per- used features on each social media platform.
formed on the studies from 2018 to 2021. It was concluded • Study the most affected social media platform from
that in order to detect fake accounts, using NN is the most malicious bots, the class of bots mostly found on these
effective method. (Rao et al. 2021) presented a comprehen- platforms. Additionally, highlight the most studied
sive review of the social spam detection techniques studied social platforms and analyze the gaps of research on
from 2015 to 2020 based on different social spam detec- other platforms.
tion techniques which include Honeypot/Honeynet-based • Examine and analyze the popular public datasets used
techniques, URL List-based spam filtering techniques, for each platform and the methods used for the self-
and ML and DL techniques. Numerous feature analysis collected datasets.
and dimensionality reduction techniques used by differ- • Highlight challenges and gaps in existing research
ent researchers were outlined. A thorough analysis was thereby providing potential directions for further
given, describing the datasets utilized, features used, ML/ research.
DL models used, performance measures used, and pros
and cons of each model. The rest of this paper is structured as follows: Sect. 2
To the best of our knowledge, no study in the literature presents the methodology adopted for this paper. Section 3
has carried out a comprehensive analysis of the existing puts forth a detailed analysis including tables and figures
studies in the time period (2015–2022) in the domain of demonstrating the ML-based techniques used in the exist-
applying ML-based techniques for social media bot detec- ing literature. In Sect. 4 based on all the reviewed stud-
tion (social bots, spambots, sybil bots). For this specific ies, the datasets used, features extracted, and algorithms
timeline, the existing reviews have studied either only ML implemented are discussed thereby performing an exten-
or DL-based studies or only addressed a specific bot type. sive analysis. Section 5 sheds light on the insights gained
We perceived that there was a need for a recent literature and presents a discussion on the challenges and opportuni-
review to be conducted so that researchers could identify the ties in existing research thereby providing future research
findings and gaps in this field and use that information as a directions. Section 6 provides a conclusion to summarize
roadmap for future research directions and further in-depth our literature review.
study. In response to this demand, in this study, we discuss
what is currently known and being researched regarding
the several concepts, theories, and techniques linked to bot
detection on social media platforms.
This paper makes the following key contributions:
1 3

20 Page 6 of 40 Social Network Analysis and Mining (2023) 13:20
2 Methodology 3 Machine learning‑based techniques
for detecting bots on social media
platforms
The objective of this review is to study the existing litera-
ture from 2015 to 2022 in the domain of bot detection and
classification using ML techniques on various social media Numerous studies have been published addressing the use
platforms. We searched for social media bot detection- of ML-based techniques for bot detection. This section
related papers on various well-known databases mainly reviews the existing research studies on the subject by dis-
Google Scholar, Mendeley, IEEE Xplore, ResearchGate, cussing previous studies and findings. The summaries are
ScienceDirect, Elsevier, acm.org, arxiv.org, SpringerLink, organized based on the three different ML types followed
MDPI, etc. The total number of papers reviewed were 105. by different social media platforms and the affecting bot
All these 105 papers were summarized and elaborately types.
discussed in this paper. Figure 2 demonstrates the range
of the reviewed papers. 3.1 Using supervised ML
Figure 3 shows the created taxonomy for the paper. The
first tier is based on ML-based techniques, followed by
Most of the studies we reviewed have implemented super-
the second tier on the type of social media platform and
vised ML and DL to detect social bots, spambots, and sybil
lastly, the third tier is based on the type of social media bot
bots which shall be discussed below.
which includes social bots, spambots, and sybil bots. The
logic behind the taxonomy created in this literature review
3.1.1 Facebook—detecting social bots
is mainly to identify the most effected social media plat-
forms from bots, the class of bots mostly found on those
platforms, and to highlight the most studied social plat- Very few studies were found that used the supervised
forms and analyze the gaps of research on other platforms. approach to detect social bots on Facebook. To improve
This is different from most existing literature reviews classification accuracy, (Wanda et al. 2020) built a super-
which focus on the ML techniques and algorithms used in vised learning architecture using a CNN model. To train and
research which can be inefficient to highlight findings and evaluate the model, the CNN used a Deep Neural Network
identify gaps since many studies use several techniques (DNN) with a number of hidden layers. In order to minimize
and algorithms applied on one platform. the objective function using the model's parameters, it also
used a gradient descent. To optimize and accelerate training
time in the NN, a pooling layer was used. The results with
an optimizer Stochastic Gradient Descent (SGD) m = 0.5
showed a training loss of 0.5058 and a testing loss of 0.5060.
Secondly, 4.4 million publicly generated Facebook post-
ings were collected and described in a dataset by (Dewan
and Kumaraguru 2017). On their dataset of harmful posts,
they used two different filtering techniques: one that used
URL blacklists and another that used human annotations.
They used NB, DT, RF, and SVM models, among other
supervised learning methods. These models are based on
a set of 44 publicly accessible attributes. After evaluation,
25 RF was shown to have the highest accuracy of over 80%.
Based on their findings, they proceed to develop Facebook
20 Inspector (FBI), a browser plug-in that uses a Represen-
tational State Transfer (REST) API to identify harmful
15
Facebook postings in real-time.
10
3.1.2 Facebook—detecting spambots
5
Some studies have identified spambots on Facebook using
0
various data collection techniques. Due to the restrictive
2015 2016 2017 2018 2019 2020 2021 2022
security policies on Facebook, accessing and acquiring
relevant data is challenging.
1 3
srepaP
fo
.oN
Timeline of the Reviewed Papers
Fig. 2 Bar chart showcasing the range of the reviewed papers

Social Network Analysis and Mining (2023) 13:20 Page 7 of 40 20
Fig. 3 Taxonomy of social media bot detection using ML-based techniques
1 3

20 Page 8 of 40 Social Network Analysis and Mining (2023) 13:20
Sahoo and Gupta (2020) implemented a spammer detec- Moreover, (Singh and Banerjee 2019) created a data-
tion system on Facebook. The Particle Swarm Optimiza- set on Facebook using their graph API to be utilized for
tion (PSO) algorithm was used in this study to determine sybil accounts detection. Also, a comparative analysis of
the popularity of the content and feature selection. The various algorithms over the dataset was performed. The
dataset included 1600 profile posts in total. Twelve pro- dataset contained 995 both real and fake accounts. Twenty-
file- and content-based features were chosen after the gen- nine features were extracted including textual, categori-
erated content underwent data pre-processing. The PSO cal, and numerical features. AdaBoost, Bagging, XGBoost,
algorithm used these features as an input parameter to find Gradient Boost (GB), RF, LR, Support Vector Classifier
fraudulent accounts. In this experiment, classifiers RF, RT, (LinearSVC), and ExtraTree algorithms were applied for
Bagging, JRip, J48, and AdaBoost were utilized. Using the evaluation. AdaBoost was the best-performing algorithm
classifier, the detection rate produced the best accuracy with a 99% F1-score.
of 99.5%. However, (Saranya Shree et al. 2021) suggested Natural
Followed by, (Rathore et al. 2018) who introduced an Language Processing (NLP) pre-processing techniques and
efficient spammer detection method called SpamSpotter that ML algorithms such as SVM and NB to classify fake and
uses an Institute for Data, Systems, and Society (IDSS) to genuine profiles on Facebook. A dataset of 516 profiles
differentiate spammers from real Facebook users. A dataset was used and trained until 30 epochs. It predicted 91.5%
made up of 1000 profiles was employed. The framework fake accounts and 90.2% genuine accounts correctly.
made use of features based on profiles and content. They Another strategy for identifying sybils on Facebook was
used the Bayesian Network (BN), RF, Decorate (DE), J48, presented by (Babu et al. 2021). By using the Facebook
JRip, KNN, SVM, and LR as the eight supervised ML clas- graph API, they gathered a dataset of 500 users from a
sifiers. The BN classifier outperformed all others with an survey of 500 Facebook users in order to better understand
accuracy of 0.984. the nature and distinguishing characteristics of sybil. The
tested dataset was used to identify fake profiles using the
3.1.3 Facebook—detecting sybil bots NB classifier. Seven profile-based features were used in the
model. Their suggested solution had a 98% efficiency rate.
We found a reasonable number of studies that thrived in Moving on, (Gupta and Kaushal 2017) has described an
recognizing sybils (Fake profiles) on Facebook. This study approach to detect fake accounts. The key contributions of
proposed by (Albayati and Altamimi 2019) was about a the authors’ work include a collection of a private dataset
smart system known as FBChecker that checks if a profile using the Facebook API through Python wrappers. After
is fake. A set of behavioral and informational attributes were data collection, a set of 17 features was shortlisted which
analyzed and classified by the system using the data mining included likes, comments, shares, tag, apps usage, etc. A
approach. Four data mining algorithms which include KNN, total of 12 supervised ML classification algorithms were
DT, SVM, and NB were used. The RapidMiner data sci- used (from Weka), namely, k-Nearest Neighbor, Naive
ence platform was used to implement the selected classifiers. Bayes, Decision Tree classifiers (J48, C5.0, Reduced
The dataset of 200 profiles was prepared by the authors. A Error Pruning Trees Classification (REPT), Random Tree,
Receiver Operating Characteristic Curve (ROC) graph com- Random Forest), etc. Two types of cross-validation were
parison was created to check the accuracy and all classifiers performed, namely, the holdout method, and tenfold cross-
showed a high accuracy rate, but SVM outperformed with validation. A classification accuracy of 79% was achieved.
an accuracy rate of 98%. The user activities contributed the maximum to the detec-
Subsequently, (Hakimi et al. 2019) proposed supervised tion of fake accounts.
ML techniques based on only five characteristics that play
a key role in distinguishing fake and true users on Face-
book. The important characteristics finalized were Average 3.1.4 Instagram—detecting social bots
Post Likes Received, Average Post Comments, Average
Post Comments Received, Average Post Liked, and Aver- Only one study by (Sen et al. 2018) aimed to detect fake
age Friends. A sample data of 800 users were generated likes on Instagram thereby detecting social bots. A dataset
by Mockaroo. The data were categorized into four clusters: of 151,117 likes of both fake and genuine likes was captured
Inactive User, Assume Fake account User, Fake account and labeled manually by the authors. A limitation of this
user, and Real User. Classifiers namely KNN, SVM, and study was the noisiness of the dataset. However, various
NN were implemented. Results showed that KNN outper- types of features were extracted from the dataset, which were
formed with an accuracy of 0.829. It was concluded that the Network Effect, Internet Overlap, Liking Frequency, Influ-
features “likes”, and “remarks” add a significant value to the ential Poster, Hashtag Features, and User-based features to
job of detection. be used with extensive analysis. LR, RF, SVM, AdaBoost,
1 3

Social Network Analysis and Mining (2023) 13:20 Page 9 of 40 20
XGBoost, NN, and Multilayer Perceptron (MLP) algorithms The bagging classifier showed better performance by suc-
were applied. MLP showed the best results with 83% Pre- cessfully classifying 98% of the accounts. Moreover, the
cision and 81% Recall (AUC of 89%). According to the author presented the best feature types for different sizes
authors, the model's high efficacy in capturing the param- of datasets.
eters that influence genuine liking behavior is the model's Additionally, (Dey et al. 2019) also assessed fake and
main strength. real different Instagram accounts. A publicly labeled data-
set of sixteen accounts was obtained from Kaggle. Twelve
3.1.5 Instagram—detecting spambots profile-based features were extracted from the sample
dataset. Missing Value Treatment, OuSybiltlier Detec-
Two studies were found that used the ML approach for fake tion, and Bivariate Analysis were carried out as a part of
and automated accounts detection on Instagram. Firstly, the Exploratory Data Analysis. Median imputation was
(Akyon and Esat Kalfaoglu 2019) contributed by generat- done to deal with the outliers. For the extent of this paper,
ing two labeled public datasets. A dataset for fake accounts LR, and RF—two supervised classification algorithms
(1203 accounts) and another for bots (1400 accounts). How- were used. Lastly, out of the two mentioned classifiers,
ever, both datasets had problems. The fake accounts data- RF showed the best performance with 92.5% accuracy.
set had an uneven number of real and fake accounts. As Subsequently, the research of (Purba et al. 2020) aimed
a result, the Synthetic Minority Over-sampling Technique- to identify fake users’ behavior. Furthermore, different
for-Nominal and Continuous (SMOTE-NC) algorithm was approaches of classification have been proposed. 2-class
implemented. While cost sensitive genetic algorithm was (authentic, fake) and 4-classes (authentic, spammer,
implemented to correct the automated accounts dataset active fake user, inactive fake user) classifications. The
unnatural bias. Profile-centric features were fed into NB, LR, total number of fake and authentic users in the dataset
SVM, and NN algorithm. SVM and NN provided promising was 32,460 users. They used seventeen features based on
F1-scores for both datasets. 94% with oversampling for fake metadata, media info, media tags, media similarity, and
accounts and 86% for automated accounts dataset. engagement. Using these features with RF, MLP, LR,
Similarly, a method to identify spam posts was also pre- NB, and J48 algorithms showed promising results. RF
sented by (Zhang and Sun 2017). 1983 user profiles and showed an accuracy of up to 91.76% for 4-classes clas-
953,808 media posts made up a manually labeled dataset. sification. Moreover, analysis outcomes showed that meta-
Profile-based, Color Difference Histogram-based, and Media data and statistics results are the foremost predictors for
Post-based feature vectors were extracted from user profiles classification.
and media postings. The near duplicate posts were grouped Nevertheless, (Kesharwani et al. 2021) utilized a six-
into the same clusters using two-pass clustering techniques, layered DL model NN to classify fake and genuine Insta-
Minhash clustering and K-medoids clustering. The best pair gram accounts. The designed model used 12 profile-based
has an accuracy of 96.27%: RF, (maxDepth: 8, numTrees: features. An open dataset of 696 Instagram users available
20, impurity: entropy). on Kaggle was used for this experiment and was collected
using a crawler. The dataset had 10 profile-based features.
3.1.6 Instagram—detecting sybil bots The model’s training was done using 20 epochs and there-
fore giving an accuracy of 93.63%.
Many studies were able to detect sybil bots starting with Quite interestingly, (Bazm and Asadpour 2020) proposed
(Meshram et al. 2021) proposed an automated methodol- a behavioral-based model. A labeled dataset was collected
ogy for fake profiles detection. The authors collected 1203 by the authors including 2000 accounts of both fake and
accounts including real and fake accounts using Instagram genuine users. Seven behavioral features were extracted
API. In addition, a list of eight content- and behavior-based from the dataset. KNN, DT, SVM, RF, and AdaBoost algo-
features were extracted. Authors needed to oversample the rithms were tested and analyzed. AdaBoost showed the best-
dataset using SMOTE-NC before applying any algorithm performing results with an accuracy of 95%. Additionally,
due to the unevenness of the real-fake accounts ratio. After- the Max feature was identified as the most effective for clas-
ward, NN, SVM, and RF algorithms were applied. RF sification followed by standard deviation, following count,
depicted the best-performing results with an accuracy of and entropy. Three of the above-mentioned most effective
97%. features were behavioral.
Whereas, using the same records and features, (Sheikhi Lastly, the work of (Thejas et al. 2019) also focused on
2020) presented a bagging classifier and performed a com- detecting valid and fake likes of Instagram posts by apply-
parative analysis with five well-known ML algorithms, ing automated single and ensembled learning models. A
which were RT, J48, SVM, Radial Basis Function (RBF), labeled dataset of 10,346 observations and 37 features has
MLP, Hoeffding Tree, and NB with 10-cross-validation. been composed. The authors used numeric features and
1 3

20 Page 10 of 40 Social Network Analysis and Mining (2023) 13:20
text-based features to perform extensive analysis of fake Moreover, (Fonseca Abreu et al. 2020) examined whether
likes related patterns. Various single classifiers have been feature set reduction for Twitter bot detection yields com-
used such as LR SVM, KNN, NB, and NN with different parable outcomes to large sets. Five Profile-based features
versions. Adjacent to ensembled-based classifiers as RF with were used for classification. The dataset used consisted of
multiple versions as well. Moreover, bot detection using an 4565 records of both social bots and genuine users. The ML
autoencoder has been experimented. RF showed the highest algorithms tested namely were RF, SVM, NB, and one-class
performance among all with 97% accuracy. SVM. AUC’s greater than 0.9 were obtained by all multi-
class classifiers. However, RF exhibited the best results with
3.1.7 LinkedIn—detecting sybil bots an AUC of 0.9999.
Varol et al. (2017) used more than a thousand features
Only two studies were found on this platform to detect which were based on metadata primarily based on friends,
sybils, (Adikari and Dutta 2020) proposed a methodol- tweet content, sentiment, network patterns, and activity time
ogy for identifying bot-generated profiles based on limited series. A publicly accessible dataset of size 31 K that con-
publicly available data of profiles using data mining tech- tains manually verified Twitter accounts as bots or real was
niques. Many existing research assumes the availability of used to train the model. The model’s accuracy was evaluated
static and dynamic data of a profile, which is not the case using RF, AdaBoost, LR, and DT classifiers. The best per-
with LinkedIn as it has more restrictive privacy policies that formance was depicted by RF of 0.95 AUC. Furthermore, it
impede access to dynamic data. The profile features were was concluded that the most significant sources of data are
extracted from a dataset of 74 profiles only. Thirty-four fake user metadata and content features.
accounts were collected by searching blogs and websites Twenty-eight features were extracted based on profile,
for known LinkedIn fake accounts. The lack of verified fake tweets, and behavior (Knauth 2019). For easy future port-
accounts was a limitation of this research. NN, SVM, PCA, ability, language-agnostic features were mainly focused on.
and Weighted Average algorithms were used in several LR, SVM, RF, AdaBoost, and MLP classifiers were used for
combinations for detecting fake profiles. SVM showed the experiments. AdaBoost outperformed all competitors with
highest accuracy (87.34%) when employing PCA-selected an accuracy of 0.988. Smaller quantities of training data
features with a polynomial kernel. were analyzed, and it was shown that using a few, expres-
Furthermore, (Xiao et al. 2015) proposed a scalable sive characteristics provides good practical benefits for bot
offline framework using the pipeline to identify clusters of identification.
fake accounts on LinkedIn. Cluster-level fake accounts are In this study, after a long process of feature extraction and
identified rather than account-level to detect fake accounts data pre-processing, (Kantepe and Gañiz 2017) employed
after registration rapidly. Statistical features generated ML techniques. Thousand eight hundred accounts were used
by users at or after registration time, such as name, email to get the data from Twitter API and Apache Spark, which
address, company, were grouped into clusters. Cluster-level was In this study, after a long process of feature extrac-
features were exclusively fed into the RF, LR, and SVM tion and data pre-processing, (Kantepe and Gañiz 2017)
models. The authors have collected a set of labeled data for employed ML techniques. One thousand eight hundred
260,644 LinkedIn accounts. RF algorithm’s performance accounts data was obtained with Twitter API and Apache
evidently provided the best results for all metrics; an AUC Spark, which was then used to extract 62 different features.
of 0.95 and a recall of 0.72 at 95% precision for out-sample The features extracted were mainly profile-based features,
test data. Twitter features and periodic features. Four classifiers were
used which include LR, Multinomial Naïve Bayes (MNB),
3.1.8 Twitter—detecting social bots SVM and GB. The highest accuracy result 86% was shown
by the GB trees.
Numerous studies were able to detect social bots on Twit- This research conducted by (Barhate et al. 2020) used
ter starting (Echeverrï£¡a et al. 2018) tested 20 unseen bot two approaches for the detection of bots and analyzed their
classes of varying sizes and characteristics using bot classi- influence in trending a hashtag on Twitter. First, the bot
fiers. Two datasets were collected using Twitter’s API con- probability of a user was calculated using a supervised ML
sisting of 2.5 million accounts. Twenty-nine Profile- and technique and a new feature bot score. A total of 13 fea-
Content-based features were employed for classification. tures were extracted for data pre-processing and Estimation
The classifiers used to test were GB Trees (XGBoost and of Distribution Algorithms (EDA). The data were trained
LightGBoost Model (LGBM)), RF, DT, and AdaBoost. using RF classifier, which produced an AUC result of 0.96.
LGBM showed the highest accuracy rate of 97.84% on both This study also came to the conclusion that bots had a high
the subsampling used—C30K and C500. friend-to-follower ratio and a low follower growth rate.
1 3

Social Network Analysis and Mining (2023) 13:20 Page 11 of 40 20
The dataset that was acquired by (Pratama and Twitter API. They used a publicly available Twitter dataset
Rakhmawati 2019) is from the supporters of the Indone- from Kaggle, which has a total of 37,438 records, as their
sian presidential candidate on Twitter. The top five hashtags offline dataset. Friends count, Followers count, Favorites
for each candidate were used to collect tweets, which were count, Status count, Account age days, and Average tweets
then manually labeled with the accounts' bot characteristics, per day were the six features that were extracted and further
resulting in a limit of about 4.000 tweets. SVM and RF, two used as input to their ML model. They use RF algorithm
ML models, are utilized for bot detection. These two mod- to differentiate between the bots and human accounts. The
els were trained with cross-validation ten-folds to improve outcomes of their methodology demonstrated the effective-
the overall score. From these two models, RF has a higher ness of retrieving, publishing the data, and monitoring the
overall score than SVM of 74% in F1-Score, Accuracy, and estimates.
AUC. Comparing the 10 retrieved features from the dataset, Shukla et al. (2022) proposed a novel AI-driven multi-
they discovered that the account year creation had the big- layer condition-based social media bot detection framework
gest separation between humans and bots. called TweezBot. Moreover, the authors have performed a
Davis et al. (2016) made use of RF classifier to evaluate comparative analysis with several existing models and an
and detect social bots by creating a system called BotOrNot. extensive study of features, and exploratory data. The pro-
A public dataset of 31 K accounts was used to train the posed method analyzed each Twitter-specific user profile
model. From six main groups of characteristics—network, features and activity-centric characteristics, such as profile
user, friend, temporal, content, and sentiment features—the name, location, description, verification status, and listed
framework collected more than 1000 features. These vari- count. 2789 distinct user profiles were used to extract
ous classifiers—one for each category of features and one these features from a public labeled dataset from Kaggle.
for the overall score—were trained using extracted features. ML models used for comparative evaluation and analysis
The system performance was assessed using ten-fold cross- were RF, DT, Bernoulli Naïve Bayes (BNB), CNB, SVC,
validation, and an AUC value of 95% was obtained. and MLP. TweezBot attained a maximum accuracy of
Likewise, a Twitter bot identification technique was also 99.00049%.
presented by (Shevtsov et al. 2022). 15.6 million tweets Since bots are used to manipulate activities in politics as
‘total, including 3.2 million accounts sent during the US well (Fernquist et al. 2018) presented a study on political
Elections, were included in their dataset from Twitter. The Twitter bots and their impact on the September 2018 Swed-
XGBoost algorithm was used to pick 229 features from ish general elections. To identify automatic behavior, an
approximately 337 user-extracted features. Their suggested ML model that is independent of language was developed.
ML pipeline involves training and validating many three ML The training data consist of both bots and genuine accounts.
models which are SVM, RF, and XGBoost. Performance was Three different datasets (Cresci et al. 2015; Gilani et al.
best for XGBoost where their findings indicate that it per- 2017; Varol et al. 2017) were used to train the classification
forms well on the collected dataset compared to the training model. Furthermore, a list of 140 user metadata, Tweet and
data section because of its great generalization capabilities. Time features were extracted. Various algorithms such as
Only 2% of the F1 score is going from 0.916 to 0.896, and AdaBoost, LR, SVM, and NB were tested. RF outperformed
0.03% of the ROC-AUC indicates a decline in performance with an accuracy of 0.957.
from 0.98 to 0. 977. Similarly, (Beğenilmiş and Uskudarli 2018) made use
Additionally, SPY-BOT, a post-filtering method based on of collective behavior features in hashtag-based tweet sets,
ML for social network behavior analysis, was introduced by which were compiled by searching for relevant hashtags.
(Rahman et al. 2021). Six hundred training samples were A dataset of 850 records was utilized to train the model
used to extract eleven characteristics. They contrast the two using algorithms including RF, SVM, and LR. From tweets
ML algorithms LR and SVM throughout the training phase. collected during the 2016 US presidential election, 299 fea-
After comparing outcomes, tuned SVM was the best per- tures were retrieved. To capture the coordinated behavior,
forming. On the validation dataset, their method achieves up the features represent user and temporal synchronization
to 92.7% accuracy while up to 90.1% accuracy was obtained characteristics. These models were developed to distinguish
on the testing dataset. As result, they suggest that the pro- between organic and inorganic, political and non-political,
posed approach able to classify the users’ behavior in Social and pro-Trump or pro-Hillary or neither tweet set behavior.
Network-Integrated Industrial Internet of Things (SN-IIoT). The RF displayed the best outcomes, with an F-measure of
Also, a real-time streaming framework called Shot 0.95. In conclusion, this study found that media utilization
Boundary Determination (SBD) was also suggested by and tweets marked as favorites are the most dominant fea-
(Alothali, Alashwal, et al. 2021a) as a way to detect social tures and user-based features were the most valuable ones.
bots before they launch an attack to protect users. To gather On the other hand, in this approach, (Rodríguez-Ruiz
tweets and extract user profile features, the system uses the et al. 2020) one-class classification was suggested. One
1 3

20 Page 12 of 40 Social Network Analysis and Mining (2023) 13:20
benefit of one-class classifiers is that they do not need than a system that analyzes an account's behavior. However,
examples of abnormal behavior, such as bot accounts. the system's reliance on static analysis reduces its efficiency.
The public dataset (Cresci et al. 2017) was used. Bagging- Ramalingaiah et al. (2021) represented an effective text-
TPMiner (BTPM), Bagging-RandomMine (BRM), One- based bag of words (BoW) model. BoW produces a numer-
Class K-means with Randomly projected features Algorithm ical vector that can be utilized as inputs in different ML
(OCKRA), one-class SVM, and NB were the classifiers that algorithms. Using resulted features from feature selection
were taken into consideration. For categorization, only 13 process, different ML algorithms were implemented like DT,
numerical features were extracted. With an average AUC KNN, LR, and NB to calculate their accuracies and compare
value of 0.921, Bagging-TPMiner outperformed all other it with their classifier which uses the BoW model to detect
classifiers over a number of experiments. Twitter bots from a given training data. The utilized data-
Moreover, (Attia et al. 2022) proposed a new multi-input set from Kaggle with 2792 training entries and 576 testing
DNN technique-based content-based bot detection model. entries for evaluation of their models. As a result, the perfor-
They used the 6760 records from the public PAN 2019 Bots mance of the decision tree gives the highest accuracy which
and Gender Profiling Task (Rangel and Rosso 2019) data- further uses a bag of bots’ algorithm to increase accuracy in
set. The proposed multi-input model includes three phases. detecting bots. Their classifier performs the best as it uses
Their proposed Multi-input model includes 3 phases. The a bag of words model with test data yields an accuracy of
first phase represents the first input as an N-gram model of a over 99%.
3D matrix of 100*8*300 as model input to two-dimensional A ML method based on benchmarking was proposed
CNN. On the other hand, the second phase input is one- by (Pramitha et al. 2021) to choose the best model for bot
dimensional CNN model that has a vector with M length account detection. Dataset obtained from Kaggle with
(100 tweets) as model input. The final phase has the previous 24,631 records then scraping was performed using the Twit-
models with fully connected neural networks to combine ter API to obtain profile features. Furthermore, over-sam-
them. Each model was trained using suitable hyper-param- pling using SMOTE is applied to overcome imbalanced data
eters values. Their model achieved a detection accuracy of and improve the models’ accuracy. Both RF and XGBoost
93.25% and outperforms other newly proposed models in algorithms were evaluated. XGBoost algorithm outperforms
bot detection. RF, with an accuracy of 0.8908. Additionally, after ranking
In the work of (Sayyadiharikandeh et al. 2020) for each fifteen different features, they discovered that three signifi-
class of bots, they recommended training specialized clas- cant features—verified, network, and geo-enable—can iden-
sifiers and combining their conclusions using the maximum tify between human and bot accounts.
rule. In the most recent version of Botometer, they also pro- Many studies implemented effective DL algorithms
duced Ensemble Specialized Classifier (ESC). Addition- instead of ML, such as a Behavior-enhanced Deep Model
ally, the authors used 18 different public labeled datasets (BeDM) proposed by (Cai, Li, and Zengi 2017b) for bot
from Bot Repository, and over 1200 features were extracted. detection using a real-world public labeled dataset of size
Features were divided into 6 categories: metadata, retweet/ 5658 accounts and 5,122,000 tweets from Twitter, which
mention networks, temporal features, content information, have been collected with honeypots. The model fused tweets
and sentiment features. Accordingly, a cross-domain perfor- content as temporal text data and the user posting behavior
mance comparison and analysis was performed using all the information using DL by applying a DNN to detect bots.
18 different datasets. The authors recommend considering The DL frameworks used in the BeDM are CNN and LSTM.
the three types of bot class as in (Cresci et al. 2017) dataset. Compared to Boosting (Gilani et al. 2016; Lee et al. 2006;
Moreover, the authors provided a list of the most informative Morstatter et al. 2016) baselines, the BeDM attained the
features per bot classes in the used public dataset. highest F1 score of 87.32%, which proved the efficacy of
A comprehensive comparative analysis was conducted the model.
by (Shukla et al. 2021) to determine the optimal feature Later in the same year, (Cai, Li, and Zeng 2017a) pro-
encoding, feature selection, and ensembling method. From posed analogous work. Yet, the novel Deep Bot Detection
the Kaggle repository, a total of 37,438 records comprising Model (DBDM) avoids the laborious feature engineering
the training and testing dataset were acquired. Scaling of and automatically learns both behavioral and content rep-
numerical attributes and encoding of categorical attributes resentations based on the user representation. Addition-
were two steps in the pre-processing of the dataset. A total of ally, DBDM took into consideration endogenous and exog-
19 attributes were extracted. The model used the classifiers: enous factors that have an impact on user behavior. DBDM
RF, Adaboost, NN, SVM, and KNN. It was determined that achieved a better results with an F1-score of 88.30%.
employing RF for blending produced the best results and Additionally, (Hayawi et al. 2022) also proposed a DL
the highest AUC score of 93%. Since the proposed approach framework, DeeProBot used eleven user profile metadata-
uses Twitter profile metadata, it can detect bots more quickly based features. Five training and five testing datasets were
1 3

Social Network Analysis and Mining (2023) 13:20 Page 13 of 40 20
used from Bot Repository. Additionally, the text feature was The dataset used in this experiment was from (Cresci et al.
embedded using GLoVe which aided in enhanced learning 2017). All the experiments achieved a detection accuracy
from the features. To detect bots, DeeProBot employed a of more than 99%.
hybrid Deep NN model. On the hold-out test set, DeeProBot Daouadi et al. (2019) proved that a Deep Forest algorithm
gave an AUC of 0.97 for bot detection. combined with thirteen metadata-based features is sufficient
However, in a novel framework called GANBOT (Najari to accurately identify bot accounts on Twitter. Two datasets
et al. 2022) modified the (Generative Adversarial Network) were used which were published by (Lee et al. 2006; Subrah-
GAN concept. The generator and classifier were connected manian et al. 2016). The Twitter API was used to gather the
via an LSTM layer as a shared channel between them, reduc- dataset. The implementation was performed for more than
ing the convergence limitation on Twitter. By raising the 30 conventional algorithms, including Bagging, MLP, Ada-
likelihood of bot identification, the suggested framework Boost, RF, SL, etc. With an accuracy of 97.55%, the Deep
outperformed the existing contextual LSTM technique. A Forest method surpassed the other conventional supervised
total of 8386 from the Cresci2017 dataset were used. Results learning techniques.
were assessed for four distinct vector dimensions: 25D, 50D, In this paper, (Cable and Hugh 2019) implemented the
100D, and 200D; the highest result was 949/0.951 for 200D. algorithms: NB, LR, Kernel SVM, RF, and LSTM-NN to
A total of seventeen state-of-the-art methods for bot identify political trolls across Twitter and compared their
detection were described by (Kenyeres and Kovács 2022) accuracies. A dataset of tweet ids related to the 2016 elec-
together based on DL models. They classified Twitter feeds tions was used by scraping the Twitter API and obtaining a
as bots or humans, based solely on the account’s textual form total of 142,560 unique tweets. The features were extracted
of the tweets. PAN 2019 Bots and Gender Profiling task using several methods: Word count, TF-IDF, and Word
(Rangel and Rosso 2019) dataset was used which consisted embeddings. The LSTM-NN obtained a test accuracy of
of 11,560 labeled users. The core of seven models was based 0.957.
on LSTM networks, four based on Encoder Representations Since it is important to determine the best features for
from Transformers (BERT) models, and one a combination enhancing the detection of social bots. To locate these ideal
of the two. For tweet classification, the best accuracy was features, (Alothali, Hayawi, et al. 2021b) offer a hybrid fea-
obtained using fine-tuned BERT model of 0.828. While for ture selection (FS) technique. This method evaluates profile
account classification, the Adaboost model archived the best metadata features using random forest, naive Bayes, support
accuracy of 0.9. Their findings demonstrate that, even with vector machines, and neural networks. Using a public data-
a small dataset, DL models may compete with Classical set made accessible by Kaggle that had a total of 18 profile
Machine Learning (CML) methods. metadata features, they investigated four feature selection
Moreover, (Martin-Gutierrez et al. 2021) provide a mul- approaches. In order to find the best feature subset, they
tilingual method for detecting suspect Twitter accounts employed filter and wrapper approaches. They discovered
through DL. Dataset used in their work was collected using that, when compared to other FS methods, the cross-valida-
Twitter API of 37,438 Twitter accounts. Several experi- tion attribute evaluation performed the best. According to
ments were conducted using different combinations of their findings, the random forest classifier has the best score
Word Embeddings to obtain a single vector regarding the using six optimal features: favorites count, verified, statuses
text-based features of the user account. These features are count, average tweets per day, lang, and ID.
later on concatenated with the rest of the metadata to build Lastly, (Sengar et al. 2020) proposed both ML and DL
a potential input vector on top of a Dense Network denoted to distinguish bots from genuine users on Twitter. This was
as Bot-DenseNet. The comparison of these experiments done by gathering user activity and profile-based features,
showed that the Bot-DenseNet when using the so-called then applying supervised ML and NLP to accomplish the
RoBERTa Transformer as part of the input feature vector goal. A labeled Twitter dataset which contains more than
with an F1-score of 0.77, produces the best acceptable trade- 5000 users and 200,000 tweets was used to train the classi-
off between performance and feasibility. fiers. After analysis and feature engineering, eight features
In this research, (Ping and Qin 2019) proposed a social were extracted. Different learning models were compared
bot detection model DeBD based on the DL algorithm CNN- and analyzed to determine the best-performing bot detec-
LSTM for Twitter. CNN was used by DeBD to extract the tion system namely KNN, DT, RF, AdaBoost, GB, Gaussian
joint features of the tweet content and their relationship. To Naive Bayes (GNB), MNB, and MLP. Results showed that
carry out the experiments, a dataset of 5132 accounts was NN-based MLP algorithm gave the most accurate prediction
created. Secondly, the potential temporal features of the with an accuracy of 95.08%. A CNN architecture was pro-
tweet metadata were extracted using LSTM. Finally, in order posed for tweet level analysis by combining user and tweet
to achieve the purpose of detecting social bots, the temporal metadata. The MIB Dataset (Cresci et al. 2017) was used.
features were finally fused with the joint content features.
1 3

20 Page 14 of 40 Social Network Analysis and Mining (2023) 13:20
The novel approach gave a staggering improvement. RF and (7973 accounts) was collected using Twitter Rest API and
GB gave the highest accuracy of 99.54%. combined with the public dataset “The Fake Project” (Cresci
et al. 2015). For pre-processing, dataset tokenization, stop
3.1.9 Twitter—detecting spambots word removal, and stemming were applied. User-based and
content-based features were extracted from the dataset. To
Some studies demonstrate the detection of spammers, start- develop the model, a variety of ML methods, including
ing with a hybrid method for identifying automated spam- SVM, ANN, and RF, were applied. With user-based fea-
mers based on their interactions with their followers was pre- tures, the findings showed that SVM had the highest preci-
sented (Fazil and Abulaish 2018). Nineteen distinct features sion (97.45%), recall (98.19%), and F measure (97.32%).
were retrieved, integrating community-based features with In this research, (Eshraqi et al. 2016) determined a clus-
those from other categories like metadata-, content-, and tering algorithm that identified spam tweets (anomaly prob-
interaction-based features. A real public dataset of 11,000 lem) on the basis of the data stream. The dataset consisted
labeled users was used. The performance was analyzed of 50,000 Twitter user accounts and 14 million tweets. The
using three supervised ML techniques namely RF, DT, and pre-processing was done by RapidMiner and then, trans-
BN which were implemented in Weka. All three metrics— ferred into Massive Online Analysis (MOA) for implementa-
DR-0.976, FPR-0.017, and F-score 0.979, were found to be tion. The features extracted were based on Graphs, Content,
the best for RF. Lastly, it was determined that interaction- Time, and Keywords. When using the DenStream algorithm
and community-based features are the most successful for (Cao et al. 2006), regulating needed to be done properly. The
spam identification in comparison after executing a feature model successfully identified 89% of available spam tweets.
ablation test and examining the discrimination capability of Furthermore, the results achieved by the model showed an
various features. accuracy of 99%.
Oentaryo et al. (2016) categorized bots based on their Mateen et al. (2017) used 13 user-, content—as well as
behavior as broadcast, consumption, and spambots. A sys- graph-based features to classify between human and spam
tematic profiling framework was developed which included profiles. The real public dataset used for this study was pro-
a set of features and a classifier bank. Numeric, categori- vided by (Gu 2022) which consisted of 11 K user accounts
cal, and series features were taken into consideration. The and 400 K tweets approximately. Three classifiers namely
private manually labeled dataset used consisted of bots and J48, DE, and NB were used for evaluation. J48 and DE out-
non-bot 159 K accounts. Four supervised ML algorithms performed the other classifiers using the hybrid technique
were employed which include: NB, RF, SVM, and LR. It of combined features by showing a 97.6% precision. Results
was seen that LR outperforms the other classifiers by depict- showed that for the dataset employed, the hybrid technique
ing an F1 score of 0.8228. significantly improved precision and recall. Additionally,
The research conducted by (Heidari et al. 2020) firstly, compared to content- and graph-based features, which dem-
they created a new public data set containing profile- onstrated 92% accuracy, user- and graph-based features cor-
based features for more than 6900 Twitter accounts from rectly classified only 90% of cases.
the (Cresci et al. 2017) dataset where the input feature set Moreover, (Chen et al. 2017a, b) found that over time,
consisted of age, gender, personality, and education from the statistical characteristics of spam tweets in their labeled
users’ online posts. To build their system, they compare the dataset changed, which impacted the effectiveness of the
following classifiers: RF, LR, AdaBoost, Feed-forward NN existing ML classifiers and is known as Twitter spam drift.
(FFNN), SGD. The results showed that the FFNN model Using Twitter's Streaming API, a public dataset of 2 mil-
with 97% accuracy provides the best results as compared lion tweets was gathered. The Web Reputation Technology
with the other classifiers. Lastly, a new bot detection model from Trend Micro was used to identify the tweets that were
was introduced which uses a contextualized representa- considered spam. The Lfun system, which was learned from
tion of each tweet by using Embeddings from Language unlabeled tweets, was proposed. Day 1 training and Day 2 to
Model (ELMO) and Global Vectors for Word Representa- Day 9 testing results showed that RF only obtained DR rang-
tion (GloVe) in the word embedding phase to have a com- ing from 45 to 80%, whereas RF-Lfun increased to 90%. The
plete representation of each tweet’s text. The model created Detection Rate of RF was roughly 85% from Day 2 training
multiple FFNN’s models on top of multilayer bidirectional to Day 10 testing, but that of RF-Lfun was over 95%.
LSTM models to extract different aspects of a tweet’s text. Kumar and Rishiwal (2020) explored and provided a
The model detected bots from human accounts, regardless framework for identifying spammers, content polluters,
of having the same user profile and achieved 94% prediction and bots using a ML approach based on NN usage. A data
accuracy in two different testing datasets. set consisting of 5572 tweets containing the text messages
A spam detection AI approach for Twitter social networks and their categorization labeling was used. Various algo-
was proposed by (Prabhu Kavin et al. 2022). The dataset rithms were trained mainly MNB, Bernoulli, NB, SVM, and
1 3

Social Network Analysis and Mining (2023) 13:20 Page 15 of 40 20
Complementary NB. The most effective and best classifica- showed the best result with a 0.95 F1-score. Additionally,
tion of spam account detection was shown by MNB with an the study depicted that sentiment features add value when
accuracy of 99%. combined with known features to bot detection algorithms.
In this study, (Güngör et al. 2020) used a dataset of 714 Also, (Sadineni 2020) detect spam using a dataset from
tweets that had been manually labeled and retrieved through Kaggle that included 950 users and ten content-based attrib-
the Twitter API. Eight profile-based features and five tweet- utes, demonstrating that SVM and RF outperform NB in
based features were extracted and analyzed. Additionally, a terms of performance.
set of guidelines had been discovered via adding followers On the other hand, (Kudugunta and Ferrara 20182018)
and friend FF rate, and spam accounts had been detected. presented a contextual LSTM architecture based on a DNN
For this experiment, the algorithms NB, J48, and LR were that uses account metadata and tweet text to identify bots at
used. J48 performed the best, achieving an accuracy of the tweet level. The tweet text served as the primary input
97.2%. In conclusion, the accuracy rate increased as a result for the model. It was tokenized and converted into a series of
of the usage of both tweet- and profile-based features. GloVe vectors before being fed into the LSTM, which then
By utilizing a dataset of 82 accounts of tweeters who use fed the data into a 2-layer NN with ReLU activations. High
both Arabic and English, (Al-Zoubi et al. 2017) improved classification accuracy can be attained using the suggested
spam identification. J48, MLP, KNN, and NB were the model. Additionally, the compared techniques for account-
algorithms used and compared in tenfold cross-validation level bot identification that used synthetic minority oversam-
with stratified sampling as a training/testing methodology. pling reached over 99% AUC.
With an accuracy of 94.9, J48 demonstrated the best spam In this study, Arabic spam accounts were detected using
detection ability using the top seven features discovered by text-based data with CNN models and metadata with NN
ReliefF. models by (Alhassun and Rassam 2022) utilizing Twitter's
For bot detection, (Heidari et al. 2021) analyzed the senti- premium API, and a dataset of 1.25 million tweets was
ment features of tweets' content for each account to measure collected. By flagging terminated accounts, data labeling
their impact on the accuracy of ML algorithms. The authors was carried out. 13 features based on tweets, accounts, and
have used (Cresci et al. 2017) dataset of the size of 12,736 graphs were retrieved. The findings demonstrated that the
accounts and 6,637,615 tweets. The bot detection method- suggested combination framework used premium features
ology proposed by the authors is centered on the number to reach an accuracy of 94.27%. The performance of spam
of tweets that show a concentration on extreme opinions detection improved when premium features were compared
for an individual account. Whether the opinions are overly to standard features when used with Twitter.
negative, positive, or neutral, it indicates the user is a bot. An efficient technique for spam identification was intro-
ML models such as RF, NN, SVM, and LR were examined duced by (Inuwa-Dutse et al. 2018). They suggested an
using the proposed sentiment features. The highest result SPD Optimized set of features that are apart from histori-
was achieved using Support Vector Regression (SVR) with cal tweets. They focused on user-related attributes, user
an F1-score of 0.930. accounts, and paired user engagement. MaxEnt, Random
The research work (Rodrigues et al. 2022) focused on Forest, ExtraTrees, SVM, GB, MLP, MLP+, and SVM were
identifying live tweets as spam or ham and performed sen- among the classification models that were utilized and evalu-
timent analysis on both live and stored tweets to classify ated based on three datasets, Honeypot (Lee et al. 2006),
them as either positive, negative, or neutral. The proposed SPDautomated, and SPDmanual. The performance reached
methodology used two different datasets from Kaggle. Vec- a peak of 99.93% when using GB on the SPD Optimized set.
torizers like TF-IDF and BoW models were used to extract This technique can be used in real-time as the first step in a
sentiment features, which were then fed into a variety of ML social media data gathering pipeline to increase the validity
and DL classifiers. The classifiers achieved the highest accu- of research data.
racy rate using LSTM in both spam detection with 98.74% Instead of employing the LCS method, (Sheeba et al.
and sentiment analysis with 73.81% accuracy. 2019) discovered spams using the RF classifier technique.
The work (Andriotis and Takasu 2019) proposed a con- The study used a dataset of 100,000 tweets. Latent Seman-
tent-based approach to identify spambots. Technically, four tic Analysis was used to further identify the account after
public datasets were used in this study, which was (Cresci the RF classifier had identified it as a spambot using Latent
et al. 2017; Varol et al. 2017; Yang et al. 2012, 2013). Col- Semantic Analysis (LSA). The proposed approach delivered
lectively, the datasets contain tweets of nearly up to 20 K benefits in terms of time consumption, high accuracy, and
accounts of both bots and genuine users. The methodology cost effectiveness.
proposed employed metadata, content, and sentiment fea- An approach to spam identification based on DL methods
tures. Furthermore, the performance of the KNN, DT, NB, was developed by (Alom et al. 2020). CNN architecture was
SVM, RF, and AdaBoost algorithms was tested. AdaBoost utilized for the text-based classifier, while CNN and NN
1 3

20 Page 16 of 40 Social Network Analysis and Mining (2023) 13:20
were merged for the combined classifier to classify tweet 71 features based on profiles, metadata, and content were
text and metadata, respectively. On two distinct real-world extracted. The following supervised ML methods were
public datasets, Honeypot (Lee et al. 2006) and 1KS-10 K compared: RF, SVM, NB, DT, and NNET. Even though the
(Yang et al. 2013), the suggested approach's performance increases were not significant after the first six features, RF
was compared to those of five ML-based and two DL-based managed to get the highest average accuracy of 94% by using
state-of-the-art approaches. For the datasets Honeypot and 19 features.
1KS-10KN, the accuracy of 99.68% and 93.12%, respec- In (van der Walt and Eloff 2018) paper, Twitter data were
tively, was attained. mined using the twitter4J API and a non-relational database
In this research, (Reddy et al. 2021) implemented some yielding a total of 169,517 accounts. Engineered traits that
supervised classification algorithms to detect spammers had previously been used to successfully identify fraudulent
on Twitter. Information was obtained from tweepyAPI accounts made by bots were added to a sample of human
which comprised 2798 accounts in the training set and 578 accounts. Without relying on behavioral data, these features
accounts in the test set. Eighteen profile-base features were were applied to several supervised ML models, enabling
extracted. In terms of accuracy, Extreme Machine Learning training on very little data. The results show that engineered
(EML) obtained a better accuracy of 87.5. traits, which were previously employed to identify fake
accounts created by bots, could only reasonably predict fake
3.1.10 Twitter—detecting sybil bots accounts created by humans with an F1 score of 49.75%.
Kondeti et al. (2021) implemented ML to detect fake
Firstly, (Narayan 2021) used ML algorithms for the detection accounts on the Twitter platform. Different ML algorithms
and successful identification of bogus Twitter accounts/bots. were used such as SVM, LR, RF, and KNN along with
The algorithms used were DT, RF, and MNB. The dataset six account metadata features likes, Lang-code, sex-code,
used included 447 Twitter accounts. Twitter API was used status-count, friends-count, followers-count, and favorites-
for the excavation of the data. DT has been found to be more count. Further to improve these algorithms’ accuracy, they
accurate as compared to RF and MNB. used two different normalization techniques such as Z-Score
In their work, (Bindu et al. 2022) proposed three efficient and Min–Max. Their approach achieved high accuracy of
methods to successfully detect fake accounts. The classifi- 98% for both RF and KNN models.
cation algorithms used were as follows: Linear and radial Khaled et al. (2019) suggested a new algorithm—SVM-
SVM, RF, and KNN. The data set used contained a total NN to efficiently detect sybil bots. Four public labeled data-
of 3964 records. RF gave more accurate prediction results sets were used by the authors. A total of 4456 accounts of
accordingly overcoming the overfitting problem. The K-Fold both fake and human classes, result from combining them.
Cross-Validation Scores for RF include a mean of 0.979812 Sixteen user-based numerical features were extracted from
and a standard deviation of 0.019682. On the other hand, the datasets after applying features reduction, and they were
in comparison Radial SVM did not perform well, and then fed into the SVM, NN, and SVM-NN algorithms. The
gave more False Negatives. However, using the Ensemble authors of the researchers assert that their novel SVM-NN
approach, higher accuracy was achieved. uses fewer features than existing models. SVM-NN was
Likewise, (Alarifi et al. 2016) studied the features used the best-performing algorithm as it showed an accuracy of
for detecting sybil accounts. Twitter4j was used to gather a around 98%.
manually labeled sample dataset of 2000 Twitter accounts In the study, (Ersahin et al. 2017) collected their own
(humans, bots, and hybrid-both human and bot tweets). dataset of fake and real accounts using Twitter API. The
Eight content-based features were selected. Four supervised dataset consisted of 1000 accounts’ data later pre-processed
ML algorithms which include J48 (C4.5), Logistic Model using Entropy Minimization Discretization (EMD) on six-
Tree, RF, Logitboost, BN, SMO-P, SMO-R, and multilayer teen user-based numerical features. NB with EMD showed
NN were used. RF performed the best with a DR of 91.39 the best result with 90.41% accuracy.
for two-class and 88.00 for three-class classification. Lastly, However, in order to predict sybil bots on Twitter using
in order to maximize the use of the classifier, the authors deep-regression learning, (Al-Qurishi et al. 2018) intro-
developed an efficient browser plug-in. duced a new model. The authors used two publicly available
David et al. (2017) leveraged a public labeled dataset labeled datasets that had been generated during the 2016 US
from the project BoteDeTwitter to build half of their data set election and collected using Twitter API. The first dataset
related to Spain politics. Using the Twitter API, a sample of consisted of 39,467 profiles and 42,856,800 tweets. Whereas
853 bot profiles and the most recent 1000 tweets from each the second dataset consisted of 3140 profiles and 4,152,799
user's timeline was collected. To create an initial feature set,
1 3

Social Network Analysis and Mining (2023) 13:20 Page 17 of 40 20
tweets. The authors extracted 80 online and offline features improving the conditional probability matrix. Two models
based on Profile-, Content- (Temporal, Topic, Quality, and were built using two different datasets. One dataset (1000)
Emotion-based), and Graph. Accordingly, the features were was crawled by R and the other consisted of spammers pur-
fed into the Deep Learning Component (DLC) FFNN. When chased from the sales platform (600) and legitimate users
fed with noisy and unclear data, the results depicted an crawled from friends and relatives (400). 9 profile-based
accuracy of 86%. Categorical features showed clear segre- features were set as attributes. In the comparison of the per-
gation that all sybil bots disable their geographical location formance with LR, DT, and NB showed a higher precision
and have an unverified account. While numerical features of 0.92.
showed that sybil bots have a noticeably young account age
(recently created). Additionally, the number of re-post and
mentions are significantly higher in the sybil's accounts. 3.1.12 Weibo—detecting spambots
Gao et al. (2020) proposed a content-based method to
detect sybils. The proposed method included three main In this paper, for effective spammer detection, an EML-
phases: CNN, bi-SN-LSTM, and the dense layer and soft- based supervised ML approach was proposed by (Zheng,
max classifier stacked to output the classification results. The Zhang, et al. 2016b). The study started by crawling Weibo
proposed bi-SN-LSTM network, in contrast to the bi-LSTM, data to create a labeled dataset. 1000 messages, both spam
employs SELU as the activation function of its recurrent and normal, were chosen from the collected dataset. Mes-
step, enabling limitless modifications to the state value. The sage content and user behavior-based features were then
proposed model achieved a high F1-score of 99.31% on the extracted for a total of 18 features, which were then fed
“My Information Bubble” (Cresci et al. 2015) dataset. into the classification algorithm. With a TPR of spammers
and non-spammers reaching 99 and 99.95%, respectively,
the experiment and evaluation demonstrated that the sug-
3.1.11 Weibo—detecting social bots gested approach offers good performance.
Zheng, Wang, et al. (2016a) proposed a two-phase-
Data collection, feature extraction, and detection modules based spambot detection approach. In the first phase,
were all included in the DL technique known as TPBot pro- authors took existing work about user features. In the
posed by (Yang et al. 2022). To begin with, the data collec- second phase, the authors introduced content mining
tion module used a web crawler to obtain user data from for spambot detection. Using web crawlers, a dataset of
Sina Weibo using dataset collected by (Wu et al. 2021). 517 accounts and 381,139 tweets was collected. Eight-
Then, depending on each user's profile, the feature extraction een behavioral and content-based features were extracted.
module extracted temporal-semantic and temporal-metadata The experiment results were compared with SVM, DT,
features. Finally, in the detection module, a detection model NB, and BN algorithms. The proposed two-phased method
based on BiGRU was developed. TPBot outperformed base- performed better than the mentioned algorithms with an
lines, by achieving an F1-score of 98.37%. Additionally, accuracy of 90.67%.
experiments were carried out on two Twitter datasets (Cresci However, (Wu et al. 2021) used DNN and active learn-
et al. 2015, 2017) to assess the generalization capabilities of ing (DABot) as a technique to detect bots. They classified
TPBot, and on both datasets, it outperformed the baselines. bots into three types: spammers, bots that engage with
Behavioral analysis and feature study were performed accounts to increase impressions, and bots involve with
by (Dan and Jieqi 2017) to extract the effective features of politics. Thirty features were extracted and classified as
Weibo accounts and build a supervised model to detect bots. metadata, interactions, contents, and time. A data collec-
A dataset of 5840 accounts from the Sina-Weibo data ware- tion of 20 K users and 214,506 posts from all users was
house was used to discriminate between real and bot users. produced as a consequence of the authors manually labe-
Eleven users’ behavioral-based features were extracted and ling the user accounts. Different stages made up the mod-
fed into DT, C4.5, and RF algorithms. The RF algorithm eled architecture: data input for each user, ResNet block,
performed measurably better with a 0.944 F-measure. BiGRU block, Attention layer, and Interference layer.
Moreover, (Huang et al. 2016) built a classifier that com- Another spam detection technique was put forth by
bined NB and Genetic Algorithm on Weibo. The genetic (Xu et al. 2021) and relied on the self-attention Bi-LSTM
algorithm was used to create an optimal threshold matrix NN model in conjunction with ALBERT. Two datasets
which efficiently increased the precision of the model by were employed in the experiment: one self-collected (582
1 3

20 Page 18 of 40 Social Network Analysis and Mining (2023) 13:20
accounts) and the other microblogPCU (2000 accounts). Hashtag, in addition to being effective in detecting new
They converted the text from social network sites into spamming forms.
word vectors using ALBERT and then, input those word In this research work, (Alharthi et al. 2019) proposed
vectors into the Bi-LSTM layer. The final feature vector a semi-supervised ML technique that classified Twitter
was created after feature extraction and combination with accounts as spam or genuine accounts based on their behav-
the information focus of the self-attention layer. To get ior and profile information. A dataset consisting of (500)
the result, the SoftMax classifier performed classification. active Arab users was collected through a Twitter API and
manually labeled. Label spreading and label propagation
algorithms were implemented using 16 extracted features.
3.1.13 Weibo—detecting sybil bots The features (TweetsAverage), (Number of the accounts’
followers to the number of his/her friends), (Tweet Source),
In this research, (Bhattacharya et al. 2021) suggested a and (is all the tweets have the same source?) were proven to
detection model that performed improved prediction of be the most efficient features. The proposed model achieved
fake Weibo accounts using a variety of Ensemble ML the following results an F-measure of 0.89, an accuracy of
algorithms. The 918 HTML pages that made up the public 0.91, and an AUC of 0.90.
Weibo dataset were obtained from Kaggle. Data scraping
was used to construct the fake accounts dataset. Content-
based attributes were extracted. Five supervised models— 3.2.2 Twitter—detecting sybil bots
RF, SVC, NB, LR, and GB—were taken into considera-
tion. For determining the final result, the RF classifier's In this study, (Zeng et al. 2021) used semi-supervised self-
highest F1 score of 0.93, precision, and recall were taken training learning by utilizing a Kaggle data set of real and
into account. Finally, a plot confusion matrix revealed an fake Twitter accounts. In this suggested technique, a self-
inaccurate prediction for 44 accounts, providing the oppor- training method was applied to automatically classify Twit-
tunity for additional research. ter accounts. Further, to effectively reduce the impact of
class imbalance on the identification effect, the resampling
3.2 Using semi‑supervised ML
technique was incorporated into the self-training process.
The proposed framework displayed good identification
Few studies on only two platforms have implemented results on six different base classifiers, particularly for the
semi-supervised ML to detect spambots and sybil bots initial batch of small-scaled labeled Twitter accounts.
which are discussed below.
3.2.3 Weibo—detecting spambots
3.2.1 Twitter—detecting spambots Only a single study based on a semi-supervised approach by
(Ren et al. 2018) detected spambots on Weibo. The authors
Sedhai and Sun (2018) were the earliest that utilized a have collected the dataset (31,147 users and 754,112 tweets)
semi-supervised approach for spam detection. Their pro- using a crawler. Behavioral and Content-based features were
posed S3D approach contains two main components which utilized to feed the model. Compared to NB, LR, SVM, and
are spam detection components in real-time mode, and J48 algorithms, the proposed approach showed better results
model update components in batch mode to periodically in all the evaluation metrics applied.
update the detection models. For spam detection, they
3.3 Using unsupervised ML
apply four detectors which are a blacklisted domain detec-
tor using blacklisted URLs, a near-duplicate detector to
label near-duplicate tweets using clustering, a reliable ham Few studies on only three platforms have implemented unsu-
detector to label tweets that are posted by trusted users and pervised ML to detect social bots, spambots and sybil bots
that do not contain spammy words, and a multi-classifier which are discussed below.
using NB, LR, and RF models to labels the remaining
tweets. Their approach achieved good accuracy results 3.3.1 Facebook—detecting spambots
for spam detection on the public HSpam14 dataset along
with four types of features to represent tweet and cluster Sohrabi and Karimi (2018) carried out the Facebook plat-
form's spam filtering mechanism for posts and comments.
1 3

Social Network Analysis and Mining (2023) 13:20 Page 19 of 40 20
Different exploration techniques and optimization tech- com, dlvr.it, dld.bz, viid.me, and ln.is. The model is made
niques, including PSO, simulated annealing, ant colony up of four sequentially operating parts: a crawler, a duplicate
optimization, and Differential Evolution (DE) could be used filter, a collector, and a bot detector. In order to conduct the
with the suggested filtering strategy. Seven metadata fea- experiment, 500,000 tweets were collected. According to the
tures were recovered from the dataset, which was made up experiments, bot networks and accounts made up a mean of
of 200,000 wall posts and comments on them. They exam- 10.5% of all accounts that employed shortened URLs.
ined the DB index and DE clustering method, SVM, and Interestingly, (Mazza et al. 2019) presented a visuali-
DT, three algorithms with PSO-based feature selection. The zation technique named Retweet Tweet (RTT) for gaining
hybrid algorithm created by integrating SVM and clustering insights into the retweeting behavior of Twitter accounts. For
techniques produced the best outcomes. the purpose of identifying retweeting social bots, Retweet-
Buster (RTBUST), an unsupervised group-analysis method,
3.3.2 Facebook—detecting sybil bots was employed. Using the Twitter Premium Search API, a
dataset of 10 M Italian retweets shared by 1446, 250 unique
Fake Facebook profiles Detection using a group of super- users was compiled. RTBust was built around an LSTM var-
vised and unsupervised mining algorithms was performed iational autoencoder. Based on the results of the Hierarchical
by (Albayati and Altamimi 2020). The main components Density-Based Spatial Clustering (HDBSCAN) algorithm, it
were the Crawler and the analyzer modules. A dataset of was decided whether the account was a bot or legitimate. In
982 profiles and a set of 12 behavioral and profile-based comparison with using it with PCA and TICA, the proposed
features. In the analyzer module, using the mining tool RTBUST technique using the VAE produced the best detec-
RapidMiner Studio, they implemented two unsupervised tion performance, i.e., F1 = 0.87.
algorithms, K-Means and K-Medoids, along with three Anwar and Yaqub (2020) proposed a quick way to isolate
supervised algorithms: ID3, KNN, and SVM. The findings bots from the Twitter discussion space. The dataset used
of the performance evaluation method revealed that super- was unlabeled data collected through Twitter Search API
vised algorithms outperformed unsupervised algorithms in during the 2019 Canadian elections. It consisted of 103,791
terms of accuracy rates. With a 97.7% accuracy rate, ID3 accounts and 546,728 tweets. 13 metadata features were
surpasses other classifiers. extracted using PCA implemented in K-means clustering.
Results showed that bots have a higher rate of retweet per-
3.3.3 Instagram—detecting sybil bots centage, daily tweets, and daily favorite count, which are
incorporated with the known characteristics of bots.
In this paper, (Munoz and Paul Guillen Pinto 2020) detected In this paper, to enhance the detection accuracy of social
fake profiles on Instagram. Web scrapping techniques were bots, (Wu et al. 2020) proposed an improved conditional
used for data extraction on the third-party site to Instagram. GAN to extend imbalanced data sets prior to applying train-
A dataset of 1086 true and false profiles was designed. 17 ing classifiers. The Gaussian kernel density peak clustering
features were extracted based on metadata and multimedia algorithm (GKDPCA), an unsupervised modified cluster-
information. Various ML algorithms such as DT, LR, RF, ing algorithm, was put into practice. 2433 users’ data was
MLP, AdaBoost, GNB, Quadratic Discriminant Analy- compiled into a dataset. On the basis of six different feature
sis, Gaussian process classification, SVM, and NN were types—user meta-data, sentiment, friends, content, network,
deployed. RF obtained the best accuracy of 0.96 as well as and timing, eleven different features were retrieved. With an
the best true and false prediction precision. F1 score of 97.56%, the enhanced CGAN performed better
than the three popular oversampling methods.
3.3.4 Twitter—detecting social bots Khalil et al. (2020) used two unsupervised clustering
algorithms DBSCAN and K-Mean. Six publicly available
A bot detection technique was put forth by (Chen et al. datasets (2232, 3465, and 1969) were used mentioned in
2017a, b) that used shortened URLs and tweeting almost (Kantartopoulos et al. 2020). Eight profile-based features
duplicate content over an extended period of time to look for were extracted. It was concluded that DBSCAN performed
a particular class of malicious bots. This method automati- better by achieving an accuracy of 97.7%.
cally gathered bot groups from real-time Twitter streams as The second contribution of (Barhate et al. 2020) is aimed
opposed to earlier work. The following nine URL shortening at using an unsupervised ML approach. Hashtag data from
services were investigated: bit.ly, ift.tt, ow.ly, goo.gl, tinyurl. the Twitter API was mined and a dataset of 140 K users was
1 3

20 Page 20 of 40 Social Network Analysis and Mining (2023) 13:20
created. Using the PCA and K-means clustering algorithms, studies on Instagram, 9 studies on Weibo, and lastly only
users were divided into four groups based on activity- 2 studies were conducted on LinkedIn. Appendix Table 2
related features. This enabled the analysis of each cluster's summarizes all the reviewed ML-based studies focusing on
bot percentage. The age distribution of users in a trending the dataset used, feature’s type, best-performing algorithm,
hashtag was also plotted by the authors. and the highest result obtained, respectively. With respect to
the most detected type of bot on each platform, Twitter had
3.3.5 Twitter—detecting spambots 36 studies on social bots, Facebook had 7 studies on sybil
bots, Instagram had 8 studies on sybils, Weibo had 5 studies
Some analyses were able to detect spammers successfully on spambots, and lastly, LinkedIn had only 2 studies which
using unsupervised learning methods for instance, (Cresci were on sybils.
et al. 2016) put forth a novel behavioral-based unsuper- Researchers in the reviewed papers used different data-
vised approach for spambots accounts detection, inspired sets both publicly available and self-created to evaluate their
by biological DNA. The proposed methodology extracts models to classify bots from humans on the five addressed
and analyzes digital DNA sequences from users’ actions. social media platforms. A summary of the 38 publicly avail-
The authors manually created a dataset (4929 accounts) able datasets has been provided in Appendix Table 3. From
of verified spambot and genuine accounts. Each account the Appendix Table 3, the most widely used datasets are
got associated with a string that encodes its behavioral MIB datasets which are the Cresci2017 and Cresci2015.
information. Compared to other benchmark work done, However, the Cresci2017 dataset was the most used data-
DNA fingerprinting model achieved the highest result with set by researchers because it includes five distinguished
an MCC of 0.952. types of social media bots, namely genuine accounts, social
Furthermore, (Koggalahewa et al. 2022) proposed an spambots, traditional spambots, fake followers or Sybil, and
unsupervised spammer detection approach. In Stage 1, the a test set consisting of a mix between genuine and social
clustering based on user interest distribution was performed. spambots. Besides the variety of dataset’s bot types, it is
In Stage 2, spam detection was performed based on peer relatively a recent and large labeled dataset consisting of
acceptance. Lastly, by assessing the user’s peer acceptability 12,736 accounts and 6,637,615 tweets in total, which may
against a threshold, a user was categorized as spam or genu- have attracted researchers to conduct their studies using the
ine. Three datasets were used namely Social Honey Pot (Lee Cresci2017 dataset to detect spam and social bots in the
et al. 2006), HSpam14 million Tweets, and The Fake Project Twitter platform. While Cresci2015 includes three fake fol-
(Cresci et al. 2017). Detection accuracies pointed out that lower’s datasets, and two human accounts datasets making it
three features Local Outlier StandardScore (LOSS), Global more efficient in the detection of sybil bots on Twitter. The
Outlier Standard Score (GOSS), and Entropy when com- Fake Project dataset is one of the Cresci2015 which is much
bined gave the best results. SMD performed the best with an more used together with Honeypot dataset to detect spam-
accuracy of approximately 0.98 on the three datasets. bots on Twitter. Different Kaggle’s public datasets were used
to detect different types of bots on Twitter. Due to the major-
ity of papers related to Twitter compared to other platforms,
4 Discussion
more provided datasets are publicly available than the self-
collected (private datasets) one. While other platforms such
To begin with, from all the reviewed studies we noticed that as Facebook and Instagram have more datasets that were
Twitter is the most researched platform with a total of 71 self-created (private datasets). Weibo has almost equal types
studies carried out, followed by 12 studies on Facebook, 11 of datasets while LinkedIn has only self-created. Figure 4
illustrates public and collected datasets on each platform.
50 Despite the fact that there are numerous datasets availa-
ble, some of them only contain human or bot IDs and labels.
40
As a result, scraping is done using the appropriate collection
30
API or method to obtain profile features or other informa-
20 tion from an ID or account. For instance, the Twitter API
is used to gather real-time datasets from publicly accessible
10
Twitter data (Rodrigues et al. 2022). Many researchers have
0
created their own datasets using these collection methods
Twitter Instagram Facebook Weibo LinkedIn
on different platforms as shown in Appendix Table 4. In
No. of Public papers No. of self-created papers
Fig. 4 Datasets distribution on each platform for the reviewed papers
1 3

Social Network Analysis and Mining (2023) 13:20 Page 21 of 40 20
Twitter, Twitter API was the most used collection method on various types of platforms are among the less popular
while methods like Twitter4j, Tweepy, ML, Twitter Premium feature types.
Search API, and REST API were less used. Instagram data- In regard to the Twitter platform, 34 studies used profile-
sets were collected using Instagram API, Selenium Web based features followed by 32 studies that used content-
Driver tool, 3rd-party Instagram websites, and some manu- based features and achieved high results. Meta-data-based
ally. For Facebook, mostly used Facebook Graph API to col- features were used in 17 studies. Features based on Tim-
lect data while web crawler was mostly used on the Weibo ing, Statistical, Keywords, Interaction, Periodic, Latent,
platform. Lastly, for LinkedIn in only two studies, the dataset Numeric, Categorical, and Series were used only once by
was collected manually. single studies and achieved reasonable results. Four studies
To distinguish between human and automated users on (Alhassun and Rassam 2022; Al-Qurishi et al. 2018; Mateen
social media platforms, it's critical to identify an ideal col- et al. 2017; Eshraqi et al. 2016) utilized graph-based fea-
lection of attributes (Alothali, Hayawi, et al. 2021b). A gen- tures. It came to the notice that when (Eshraqi et al. 2016)
eral observation was made that bots have a high friend-to- combined graph-based features along with Content, Time,
follower ratio and a low follower growth rate. This can be and Keywords, a very high accuracy of 0.99 was achieved.
done by using a variety of features that have been reported Only 5 studies (Wu et al. 2020; Davis et al. 2016; Inuwa-
in various studies. On the basis of the extracted features Dutse et al. 2018; Sayyadiharikandeh et al. 2020; Varol et al.
in all the reviewed papers, the features were classified into 2017) made use of the network-based features. (Inuwa-Dutse
the following categories: Content/Language, User (Profile), et al. 2018) combined such network- and profile-based fea-
Metadata, Behavioral, Network (Community/Interaction), tures and achieved the highest result AUC 99.93%. The num-
Sentiment, Timing/Temporal, Graph, Numeric/Categorical/ ber of features utilized in all 71 studies ranged from as less
Textual/Series, Statistical¸ User Friends, Media and Engage- as 5 features to as high as 1000 features. (Varol et al. 2017)
ment, Entity and Link¸ Keywords, Internet Overlap, hashtag and (Davis et al. 2016) used approximately 1000 features
features, and Periodic features. Content features are based and achieved an AUC of 0.95 whereas (Fonseca Abreu et al.
on linguistic cues computed through NLP, mainly part-of- 2020) used only 5 profile-based features and still obtained
speech tagging. User features are based on properties of the an AUC of 0.999. Regarding crucial features, interaction-
users’ accounts and users’ relationships. User Meta Data and community-based features hold high value in spambot
features are information regarding the profile's characteris- detection (Fazil and Abulaish 2018).
tics. Locating an information source via metadata is known In regard to the Facebook platform, 7 out of 12 stud-
to be effective. Behavior features are calculated by statistical ies utilized profile-based features followed by content-
properties from the data. Different aspects of information based being used by 5 studies. Moreover, by examining the
diffusion patterns are captured by network features. General- results of this platform’s studies, it can be concluded that
purpose and Twitter-specific sentiment analysis algorithms the highest results were achieved when profile-based and
are used to build sentiment features. Time features include content-based features were combined hence showing a high
statistics of time. Graph features are extracted by modelling accuracy of 0.984 in the research conducted by (Rathore
the social media platform as a social graph model. Descrip- et al. 2018). Noteworthy, textual, Categorial, and Numerical-
tive statistics relative to an account’s social contacts are based features were used only in 1 study.
included in user friend features. Interest Overlap features
include overlap between two users such as Topical affinity.
Appendix Table 5 of the literature review provides exam-
ples of features from the reviewed studies as well as a sum- 50
mary of the features used in various social media platforms. 40
According to the table, the most popular feature types from 30
all the reviewed papers are content-based, profile-based, 20
metadata-based, and behavioral-based features on essentially 10
all types of platforms. Content-based features were utilized 0
in 44 studies, followed by user/profile-based features in 42
studies, metadata-based in 27 studies, and behavioral-based
in 16 studies. User friend, media, engagement, and keywords
No. of Papers
Fig. 5 Bar chart for ML algorithms
1 3

20 Page 22 of 40 Social Network Analysis and Mining (2023) 13:20
Singh and Banerjee (2019) but gave promising results is a helpful way to reduce the impact of class imbalance
(F1-score 0.99). Features such as “likes”, “remarks”, “user when using semi-supervised learning. For the unsupervised
activities” contributed the maximum for the detection of learning approach, the DenStream unsupervised cluster-
sybils. Moving on to the third-most researched platform, ing algorithm achieved the highest result as compared with
Instagram, behavior-, content, and profile-based were used other used clustering algorithms like K-Mean and DBSCAN.
in 4 out of 11 studies. The combination of behavior- and Though this approach has less popularity and performance
content-based features showed the highest performance with compared with the supervised approach (Albayati and
an accuracy of 0.9845. In Weibo-based studies, content- Altamimi 2020), this method offers the benefit of not requir-
based were the most widely used in addition to behavior- ing a labeled dataset. Since, there was only one paper that
based features. Timing as well as semantic features were applied this approach, hence additional investigation into
the least used but, on the contrary, gave the highest results. this particular algorithm is not possible.
Since only 2 studies were found on LinkedIn, they made use To conclude, not much evidence could be drawn from
of profile and statistical features. This platform needs to be this analysis that the most researched bot type or the most
extensively explored using other feature types which include researched social platforms are necessarily the ones most
content-, metadata-, behavioral-based, etc. affected by social bots.
In terms of the different ML-based (supervised, semi-
supervised, and unsupervised) techniques utilized in the
5 Challenges and opportunities
reviewed papers which were built to compare and detect
different types of social bots, Appendix Table 6 presents
a list of all the respective papers that utilized the different In this section, we shall put forth an elaborate discussion
algorithms. This Table 6 highlights the classifier bot type on challenges and future research directions based on our
with the highest performance achieved for each algorithm. study and analysis. The findings showcased that social bot
Figure 5 shows the number of papers that utilized each ML detection is challenging and this challenge is aggravated as
algorithm. As shown, RF is the best-performing and most the social network volume increases. To begin with, the most
applied algorithm among all algorithms in research and detected and researched bot types are social bots (42 stud-
SVM is the second most applied algorithm in research fol- ies), followed by spambots (34 studies), and lastly sybil bots
lowed by NB, DT, and AdaBoost. The least applied algo- (29 studies). Evidentially, Twitter is the most studied social
rithms were GNB, ELM, bi-SN-LSTM, and clustering algo- network with a large number of bots of all types, especially
rithms were the least applied algorithm. For supervised ML, social bots, mainly because of how easy it is to collect data
the best performing algorithms of classical ML algorithms, through their API and the vast collection of accessible pub-
the best performing were RF, JRip, AdaBoost, with their lic datasets. However, social networks such as Instagram,
accuracy reaching up to 99.5%, and the least utilized algo- LinkedIn, and Weibo need further in-depth study. Specifi-
rithms were ID3 and GNB. As for DL algorithms, the best cally, there is a dearth of studies on Facebook and LinkedIn
performing algorithm was CNN with the highest accuracy due to the immense difficulty in obtaining publicly available
of 99.68% achieved though most perform well. The least uti- datasets, which is caused by certain strict privacy policies on
lized and least popular algorithm was ELM, even though it is those networks. LinkedIn, in particular, does not have much
considered simple with less training time. Moreover, it was of recent studies conducted on it. Furthermore, only sybil
noticed that ML classifiers work well with small-size data- bots were found in the publicly available LinkedIn datasets.
sets and DL algorithms with large-size datasets. However, Moreover, with slight modifications, the ML techniques
no algorithm can be considered good or bad as it depends used for Instagram will have the potential to be applied to
on a number of factors such as the dataset size, data pre- LinkedIn. From our studies, we conclude that Cresci2017
processing, and the number and type of features. is the most used dataset in social media bot research due
Further in terms of semi-supervised learning, despite to its classification of bots based on their types. Whereas,
them being powerful techniques in terms of discovering Instagram has a greater number of sybil bots and two studies
patterns in big data only four studies were found: three on based on fake engagements. User and content-based features
Twitter and one on Weibo (Sedhai and Sun 2018; Alhar- are the most frequently used for Instagram thereby show-
thi et al. 2019; Zeng et al. 2021; Zeng et al. 2021). Since ing high-accuracy results. Nevertheless, there is a scope
large datasets are derived from the Twitter platform which for more research on this platform. In terms of features, on
makes labeling an expensive and time-consuming process, twitter (Fonseca Abreu et al. 2020) showed that even with
semi-supervised techniques such as label propagation and 5 significant features, high results can be achieved. There-
label spreading show the ability to be applied more often. fore, new studies can be carried out by using as less features
Moreover, integrating resampling along with self-training as possible. On Facebook, since profile-, content-, textual-,
1 3

Social Network Analysis and Mining (2023) 13:20 Page 23 of 40 20
categorial-, and numerical-based features contributed high was observed in the collected research. Only a few papers
value in various studies, a new research direction can be proposed a ML-technique to detect bots at registration or
explored by combining all the above-mentioned five feature creation in real-time. As none of the existing research are
types. LinkedIn needs to be extensively explored by using designed to catch bots and act before they make connections
feature types which include content-, metadata-, behavioral- with real users. Whereas in practice, it is desired to detect
based, etc. bots as soon as possible after registration in order to prevent
In terms of the reviewed algorithms, it is seen that them from interacting with real users. However, this has its
RF is the best performing in terms of accuracy and the own challenges as the bot’s detection needs to be done from
most applied algorithm among all algorithms on all social the basic information provided during the registration time.
media platforms in the conducted study. SVM is the sec- Lastly, as the great novelist, Patricia Briggs quotes
ond most applied algorithm in research followed by NB, “Knowledge is a better weapon than a sword”. The users on
DT, and AdaBoost. DenStream unsupervised clustering various social media platforms need to gain cybersecurity
algorithm achieved the highest result compared with other awareness in order to not get deceived and be able to distin-
used clustering algorithms like K-mean and DBSCAN. guish between bots and benign accounts and be responsible
Though this approach has less popularity, it has added in situations if a malicious bot was recognized to immedi-
the advantage of not requiring a labeled dataset. Differ- ately report it to the platform.
ent algorithms based on Bayes Theorem were used to
classify Spam and social bots like NB, MNB, GNB, and
NB. However, MNB overperforms the others. Different
6 Conclusion
types of algorithms were used to build Decision Trees like
basic DT, J48, JRip and ID3. DT, and J48 were the most
applied forms. Yet, the JRip algorithm achieved the best This paper made an effort to provide a comprehensive
performance among them on spam detection. Different review of the existing studies in the area of utilizing ML for
types of boosting algorithms were applied such as Ada- bots detection on social media platforms which are affected
Boost, XGBoost, and GradientBoost. AdaBoost was the by three types of bots—social, spam, and sybils to provide a
most applied, whereas GradientBoost performed the best starting point for researchers to identify the knowledge gaps
amongst them on social bots detection. The DL approach in this field and conduct future in-depth research.
was mostly applied to detect social bots type on the Twit- Furthermore, the usage of supervised, semi-supervised,
ter platform. Among the different DL algorithms, CNN and unsupervised ML-based approaches was also summa-
and LSTM were the highest-performing and most promis- rized. Numerous ML and DL methods were analyzed for
ing algorithms in terms of accuracy. bots detection, including KNN, RF, DT, NB, SVM, KNN,
Comparing algorithms on different platforms, RF LSTM, ANN, etc. Visual aids were created to analyze the
achieved the best accuracy result on Weibo and Instagram reviewed papers based on the nature of their datasets, the
platform. While AdaBoost achieved highest Detection Rate various categories of features, as well as the performance of
on Facebook platform. On the other hand, CNN and ANN employed algorithms. From the analysis for bots detection,
achieved highest accuracy on twitter platform. we discovered that RF exhibited the highest performance
Moving on, future enthusiastic researchers are encour- in terms of accuracy and is the most frequently used ML
aged to investigate and conduct studies on unstudied social algorithm. Whereas CNN and LSTM were the highest-per-
media platforms such as TikTok, Telegram which are known forming and promising DL algorithms in terms of accuracy.
to have bots. As seen above, only four studies employed Last but not the least, we addressed and listed some of the
semi-supervised learning techniques, and a few used unsu- challenges, limitations as well as recommended suggestions
pervised technique; therefore, these fields need more explo- that can be utilized by enthusiastic future researchers for
ration and contribution. The semi-supervised approach gives adding more value and thereby contributing to the field of
unlabeled instances the same weight as labeled ones while cybersecurity.
also minimizing the cost of labeling the data. More impor-
tantly, it is advised that researchers make their datasets avail-
able to the scientific community. This will support the train-
Appendix
ing of new models, their testing, and the evaluation of the
existing models. Additionally, new public datasets that con-
tain the most recent type of bots are needed. The main gap See Tables 2, 3, 4, 5 and 6.
1 3

 20  Page 24 of 40 Social Network Analysis and Mining (2023) 13:20
 gnilpmasrevo htiw erocs-1F
)%68( tuohtiw )%49(
)%59( etar noitceteD
)%43.78( ycaruccA )%72.49( ycaruccA )%86.99( ycaruccA )%65.79( erocs 1F )%03.88( erocs-1F ),%23.78( erocs-1F )449.0( erusaem-F
00.88 ,93.19-RD )98.0( erusaem-F )19.0( ycaruccA )%68( ycaruccA )9.49( ycaruccA )339.0( ycaruccA )%89( ycneicffiE )%59( ycaruccA )218979.0( naeM )189.0( ycaruccA
|                |     |            |             |     | )59.0( erocs-1F |     |            | )39.0( erocs-1F |     |             |
| -------------- | --- | ---------- | ----------- | --- | --------------- | --- | ---------- | --------------- | --- | ----------- |
| tluser tsehgiH |     |            | )%3.49( CUA |     |                 |     |            |                 |     | )259.0( CCM |
|                |     | )09.0( CUA |             |     |                 |     | )69.0( CUA | )59.0( CUA      |     |             |
|                |     |            | –           |     |                 | –   |            |                 |     |             |
noitagaporp lebaL ,gnidaerps lebaL
mhtirogla gnimrofrep-tseB
|     |     |     | dohtem EAVC + FR |     |     | gniretsulc snaem-K |     |     |     |     |
| --- | --- | --- | ---------------- | --- | --- | ------------------ | --- | --- | --- | --- |
tnirpregnfi AND
|     | NNA ,MVS | NNA + NNC |     |     |     |     |     |     |     |     |
| --- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
ACPDKG
|     |     |     |     |      | tsooBadA | NNC D2 | naiseyaB tsooBadA |       | nufL-FR |      |
| --- | --- | --- | --- | ---- | -------- | ------ | ----------------- | ----- | ------- | ---- |
|     |     |     |     |      | TD 84J   |        |                   |       | MDBD    |      |
| MVS |     | NNC |     | NNFF |          |        |                   |       | MTSL    | MDeB |
|     | FR  |     | FR  |      |          |        | FR                | FR FR | FR      | FR   |
 ,krowten ,tnetnoc ,sdneirf
|     |                                         | -atem ’sresu ,txet teewT | )elfiorp + tnetnoc( atad | -hparg ,-tnetnoc ,-elfiorP | -itnes ,tnetnoc ,atadateM |                       | )erocs tob( desab elfiorP |     |     |                     |
| --- | --------------------------------------- | ------------------------ | ------------------------ | -------------------------- | ------------------------- | --------------------- | ------------------------- | --- | --- | ------------------- |
|     |                                         | tnetnoc ,elfiorp ,hparG  |                          |                            |                           |  ,tnemitnes ,atadateM |                           |     |     |                     |
|     | tnetnoc ,laroivaheB elfiorp ,laroivaheB |                          |                          |                            |                           |                       |                           |     |     | tnetnoc ,laroivaheB |
tnetnoc ,roivaheB
epyt s’erutaeF
|     |     |     |          |     |     |                 | laroivaheB |     | lacitsitatS | laroivaheB laroivaheB |
| --- | --- | --- | -------- | --- | --- | --------------- | ---------- | --- | ----------- | --------------------- |
|     |     |     | atadateM |     |     | atadateM gnimit |            |     |             |                       |
elfiorP tnetnoC elfiorP desab yraniB tnem tnetnoC elfiorP elfiorP tnetnoC elfiorP elfiorP
esuoheraw atad obieW aniS
snoitcele naidanaC 9102
|     |     | NK01-SK1 topyenoH |  stnuocca stob rettiwT |                   |     | 6102kralC ,7102loraV |     |     |     |                   |
| --- | --- | ----------------- | ---------------------- | ----------------- | --- | -------------------- | --- | --- | --- | ----------------- |
|     |     |                   |                        | snoitcele SU 6102 |     |                      |     |     |     | 6102icserConafetS |
0202dammahuM
7102simlinegB
0202adnilahS 9102ihtrahlA yrotisoper toB stcejorp BIM 8102r namttiL
|     |     | 2202reehtA |     |     |     | 9102 FELC | 7102keetarP |     |     |     |
| --- | --- | ---------- | --- | --- | --- | --------- | ----------- | --- | --- | --- |
9102hitaF )elggaK( 7102runO 1102oahC 2102oahC 7102isreC 7102oahC 6102derF 6102derF
|         | j4rettiwT |     |        |     | 7102alA |     |     |        |     |     |
| ------- | --------- | --- | ------ | --- | ------- | --- | --- | ------ | --- | --- |
| tesataD |           |     | elggaK |     |         |     |     | elggaK |     |     |
libys ,mapS
seuqinhceT LM gnisu noitceteD toB aideM laicoS fo yrammuS  2 elbaT epyt toB
libyS libyS mapS mapS mapS laicoS laicoS libyS mapS mapS laicoS laicoS laicoS laicoS laicoS libyS laicoS libyS libyS mapS laicoS laicoS laicoS mapS laicoS
| mroftalP nIdekniL | margatsnI |     |     |     |     |     | koobecaF margatsnI |     |     |     |
| ----------------- | --------- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- |
rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT
|     |     |     |     |     |     |                                 |     | obieW |     | obieW           |
| --- | --- | --- | --- | --- | --- | ------------------------------- | --- | ----- | --- | --------------- |
|     |     |     |     |     |     | LM desivrepusnU LM desivrepusnU |     |       |     | LM desivrepusnU |
desivrepus-imeS
LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS
euqinhceT
|     |     | LD  |     | LD  |     | LD  |     |     | LD LD | LD  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
 ulgoaflaK tasE dna noykA )0202( ruopdasA dna mzaB  ilraduksU dna şimlineğeB )b7102( igneZ dna ,iL ,iaC
)0202( attuD dna irakidA  .la te ,lawhsalA ,ilahtolA )0202( buqaY dna rawnA )1202( .la te ayrahcattahB )a7102( gneZ dna ,iL ,iaC
|     |                        |                      |  .la te ,iwayaH ,ilahtolA | )8102( .la te ihsiruQ-lA |                                              |     |                       |     | )9102( hguH dna elbaC  |                      |
| --- | ---------------------- | -------------------- | ------------------------- | ------------------------ | -------------------------------------------- | --- | --------------------- | --- | ---------------------- | -------------------- |
|     | )9102( .la te ihtrahlA |  massaR dna nussahlA |                           |                          | )7102( .la te ibuoZ-lA  usakaT dna sitoirdnA |     |                       |     | )b ,a7102( .la te nehC |                      |
|     |                        |                      |                           |                          |                                              |     | )0202( .la te etahraB |     |                        | )7102( iqeiJ dna naD |
)6102( .la te fiiralA )0202( .la te molA )2202( .la te aittA )1202( .la te ubaB )2202( .la te udniB )6102( .la te icserC
)0202( .la te uW
| secnerefeR |        |        | )a1202( | )b1202( |        |     |     |        |     |     |
| ---------- | ------ | ------ | ------- | ------- | ------ | --- | --- | ------ | --- | --- |
|            | )9102( | )2202( |         |         | )9102( |     |     | )8102( |     |     |
1 3

Social Network Analysis and Mining (2023) 13:20  Page 25 of 40  20
| )%55.79( ycaruccA |     | )%5.29( ycaruccA )%48.79( ycaruccA | )%14.09( ycaruccA |     | )%13.99( erocs 1F )%2.79( ycaruccA |     |     |     |
| ----------------- | --- | ---------------------------------- | ----------------- | --- | ---------------------------------- | --- | --- | --- |
)%49( ycaruccA )%08( ycaruccA )%99( ycaruccA )759.0( ycaruccA )%49( ycaruccA )928.0( ycaruccA )179.0( ycaruccA )189.0( ycaruccA )039.0( erocs-1F
|                |           |     | )979.0( erocs-F |              |           |            |     | )29.0( noisicerP |
| -------------- | --------- | --- | --------------- | ------------ | --------- | ---------- | --- | ---------------- |
| tluser tsehgiH |           |     |                 | )9999.0( CUA |           |            |     |                  |
|                | )%59( CUA |     |                 |              | )%39( CUA | )79.0( CUA |     |                  |
NNFF + )MTSL(OMLE + evolG-
MTSL-NS-ib + )ULES + NNC(
mhtirogla gnimrofrep-tseB
mhtirogla naiseyaB TD
MTSL + eVoLG
DME/w BN
| tserof peeD |       |       | maerSneD |     |           |     |       |     |
| ----------- | ----- | ----- | -------- | --- | --------- | --- | ----- | --- |
|             |       | MBGL  |          |     |           |     | NNFF- |     |
|             |       |       |          |     |           | NNK |       | MVS |
|             | FR FR | FR FR | FR FR    | FR  | 84J FR FR |     |       |     |
-met ,sdneirf resu ,krowteN tnemitnes ,tnetnoc ,larop
 ,atadatem ,tnetnoc ,ytitnE
|     |     |     |  ,atadatem ,ytinummoC emit ,tnetnoc ,atadateM |     |     |     |     |     |
| --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- |
 ,emit ,tnetnoc ,hparG
noitcaretni ,tnetnoc
elfiorp ,atadateM
|                |     | elfiorp ,tnetnoC |     |     | elfiorp ,tnetnoC enilemit ,elfiorP |               |     |               |
| -------------- | --- | ---------------- | --- | --- | ---------------------------------- | ------------- | --- | ------------- |
| epyt s’erutaeF |     |                  |     |     | desab tnetnoC                      | desab-tnetnoC |     | desab-elfiorP |
sdrowyek
|     |         |         | desab-resU |         |          |          |         | tnemitneS |
| --- | ------- | ------- | ---------- | ------- | -------- | -------- | ------- | --------- |
|     |         |         |            |         | atadateM | atadateM |         |           |
|     | tnetnoC | elfiorP |            | elfiorP |          |          | elfiorP |           |
knil
 ,6102nainamharbuS 6102rettiwTeDstoB
6102nainamharbuS
5102 ,7102icserC
|     |     | 7102airrevehcE | 7102uGiefouG |     |     | b ,a7102icserC |     |     |
| --- | --- | -------------- | ------------ | --- | --- | -------------- | --- | --- |
6102notyalC 6102ihsovahC 7102inaliG .Z 7102inaliG .Z 7102loraV .O 6102gniygniY
7102keetarP 5102icserC 7102icserC 0202arbuK 9102damhA –9102gnaY b0202gnaY 9102azzaM 7102inaliG 7102icserC 7102icserC
|         | 1102eeL | 1reve4eerF 8102leseB 2102gnaY | 7102tekuB 1102oahC |              | 5102isreC 7102itidA | 7102 loraV |     |     |
| ------- | ------- | ----------------------------- | ------------------ | ------------ | ------------------- | ---------- | --- | --- |
| tesataD |         |                               |                    |              | elggaK              |            |     |     |
|         |         | mapS ,laicoS                  |                    | mapS ,laicoS |                     |            |     |     |
epyt toB
laicoS libyS laicoS laicoS libyS libyS mapS mapS laicoS libyS mapS libyS laicoS libyS laicoS mapS mapS laicoS
| mroftalP |     | koobecaF margatsnI |     |     | koobecaF | koobecaF |     |     |
| -------- | --- | ------------------ | --- | --- | -------- | -------- | --- | --- |
rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT
obieW
LD & LM desivrepuS
LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS
euqinhceT
|     |     |                                                  |                           |     | LD                       | LD  |     |     |
| --- | --- | ------------------------------------------------ | ------------------------- | --- | ------------------------ | --- | --- | --- |
|     |     |                                                  | )8102( hsialubA dna lizaF |     | )7102( lahsuaK dna atpuG |     |     |     |
|     |     |  urugaramuK dna naweD )8102( .la te a¡£ïrrevehcE |                           |     |                          |     |     |     |
)deunitnoc(  2 elbaT
| )9102( .la te idauoaD |                                         |                   | )8102( .la te tsiuqnreF                     |  .la te uerbA acesnoF |                                           |                                           |                       |                                           |
| --------------------- | --------------------------------------- | ----------------- | ------------------------------------------- | --------------------- | ----------------------------------------- | ----------------------------------------- | --------------------- | ----------------------------------------- |
|                       |                                         |                   | )7102( .la te nihasrE )6102( .la te iqarhsE |                       | )0202( .la te rögnüG )1202( .la te alkuhS | )9102( .la te imikaH )2202( .la te iwayaH | )0202( .la te iradieH | )1202( .la te iradieH )6102( .la te gnauH |
|                       | )7102( .la te divaD )6102( .la te sivaD |                   |                                             |                       |                                           |                                           |                       |                                           |
|                       |                                         | )9102( .la te yeD |                                             |                       | )0202( .la te oaG                         |                                           |                       |                                           |
secnerefeR
|     |     | )7102( |     | )0202( |     |     |     |     |
| --- | --- | ------ | --- | ------ | --- | --- | --- | --- |
1 3

 20  Page 26 of 40 Social Network Analysis and Mining (2023) 13:20
|     |     |     | )%36.39( ycaruccA )%7.79( ycaruccA |     |     | )%7.79( ycaruccA |     | )%6.79( noisicerP | )%54.89( ycaruccA | )8228.0( erocs-1F |     |     |
| --- | --- | --- | ---------------------------------- | --- | --- | ---------------- | --- | ----------------- | ----------------- | ----------------- | --- | --- |
)%68( ycaruccA )%89( ycaruccA )889.0( ycaruccA )89.0( ycaruccA )%89( ycaruccA )%99( ycaruccA )%89( ycaruccA )69.0( ycaruccA D002—159./949 )%39( ycaruccA )%99( ycaruccA )198.0( ycaruccA
|     | )%39.99( CUA   | )9.0( ycaruccA |     |     |             |     |     | )77.0( erocs-1F |     |     | )379.0( erocs-F |                |
| --- | -------------- | -------------- | --- | --- | ----------- | --- | --- | --------------- | --- | --- | --------------- | -------------- |
|     | tluser tsehgiH |                |     |     | )%69 >( CUA |     |     |                 |     |     |                 | )47.0( erocs-F |
)78.0( 1F
-snart aTREBoR + teNesneD-toB
|     | mhtirogla gnimrofrep-tseB | tsoobadA + MTSL + eVoLG |     |     |     |     |     |     |     |     |     |     |
| --- | ------------------------- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
MTSL lautxetnoC
MTSL + eVoLG
etaroceD ,84J
MTSL ,NNC
|     |     |     | NN-MVS NACSBD | tsooBadA | NNK ,FR |     |     | remrof |     |     |     | tsooBGX |
| --- | --- | --- | ------------- | -------- | ------- | --- | --- | ------ | --- | --- | --- | ------- |
TD 3DI
|     |     |     | NNA | DMS |     | BNM | MVS |     | MTSL |     | MVS |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
TBG
|     | BG                                                  |                           |               |                            |                      |                 |         |                            | FR FR               | TD RL                  |                   | FR               |
| --- | --------------------------------------------------- | ------------------------- | ------------- | -------------------------- | -------------------- | --------------- | ------- | -------------------------- | ------------------- | ---------------------- | ----------------- | ---------------- |
|     |                                                     |                           |               | roivaheb ,tnetnoc ,elfiorP |                      |                 |         | -atem( noitamrofni elfiorP |                     |                        |                   |                  |
|     |  ,resu ,krowten ,tnuoccA cidoirep ,tnetnoc ,elfiorP | -non ,tnetnoc ,txet teewT |               |                            |                      |                 |         |                            |                     |                        |                   |                  |
|     |                                                     |                           |               |                            |                      |                 |         | -tnetnoc ,desab-elfiorP    |                     |  ,lacirogetac ,ciremuN |                   |                  |
|     |                                                     |                           |               |                            |  tnuocca ,txet teewT |                 |         |                            | desab-hparg ,desab  |                        |                   |                  |
|     |                                                     |                           |               |                            |                      |                 |         |                            | tnetnoc .laroivaheB |                        | tnetnoc ,laropmeT |                  |
|     |                                                     |                           |               |                            | atadatem tnuoccA     |                 |         |                            |                     |                        |                   | stnuocca rettiwT |
|     | epyt s’erutaeF                                      |                           | desab-elfiorP |                            |                      |                 |         |                            |                     |                        | tnetnoc ,resU     |                  |
|     | desimitpo                                           |                           |               |                            |                      |                 |         | txet ,)atad                |                     |                        |                   |                  |
|     |                                                     |                           | desab-resU    |                            |                      | atadatem        |         |                            |                     |                        |                   |                  |
|     |                                                     | tnetnoc                   |               |                            |                      |                 |         |                            | atadateM            |                        |                   |                  |
|     |                                                     |                           | elfiorP       | tnetnoC                    |                      | tnetnoC elfiorP | elfiorP |                            |                     | elfiorP                | seires            | elfiorP          |
tnetaL
–
|     |  ,detamotuaDPS ,topyenoH |  redneg dna stob 9102 NAP |     |     |     |     |     |     |     |     |     |     |
| --- | ------------------------ | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
 ekaf eht“ detcelloC
|     |                       |                | 0202dammahoM | tcejorp ekaf ehT top yenoh laicoS |            | 0202demmahoM | 9102demmahoM |              |                       |                         |           |           |
| --- | --------------------- | -------------- | ------------ | --------------------------------- | ---------- | ------------ | ------------ | ------------ | --------------------- | ----------------------- | --------- | --------- |
|     |                       | ksat gnilfiorp |              |                                   |            |              |              | 7102uGiefouG |                       |                         |           |           |
|     | launamDPS 7102tihacüM |                |              |                                   |            |              |              |              | 9102elehciM           | 1202muhdriN 6102drahciR |           |           |
|     |                       |                |              | 7102icserC                        | 7102icserC |              |              |              | 1202yanarP 0202leumaS | 7102icserC              |           | 9102udnaP |
|     |                       |                | 5102isreC    |                                   | 41mapSH    | 0202yaniV    |              | 1202divaD    |                       |                         | 7102isreC | ”tcejorp  |
|     | tesataD               |                | elggaK       |                                   |            |              |              |              |                       |                         |           | elggaK    |
–
mapS ,laicoS
epyt toB
mapS laicoS laicoS libyS libyS laicoS laicoS mapS libyS mapS mapS libyS libyS laicoS mapS laicoS libyS libyS libyS mapS laicoS mapS laicoS laicoS
|     | mroftalP |     | margatsnI |     |     | koobecaF | koobecaF |     | margatsnI margatsnI |     |     |     |
| --- | -------- | --- | --------- | --- | --- | -------- | -------- | --- | ------------------- | --- | --- | --- |
rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT
|     |     | LD & LM desivrepuS |                 |                 |     | -repusnu & desivrepuS |     |     |                                 |     |     |     |
| --- | --- | ------------------ | --------------- | --------------- | --- | --------------------- | --- | --- | ------------------------------- | --- | --- | --- |
|     |     |                    | LM desivrepusnU | LM desivrepusnU |     |                       |     |     | LM desivrepusnU LM desivrepusnU |     |     |     |
LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS
LM desiv
euqinhceT
|     |     |     | LD  |     | LD  |     |     | LD  |     |     | LD  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
)7102( ziñaG dna epetnaK )2202( .la te awehalaggoK )2202( .la te nivaK uhbarP  itawamhkaR dna amatarP
|                      | )8102( .la te estuD-awunI |     | )1202( .la te inawrahseK |     |                        |                        |                        |                          |  nelliuG luaP dna zonuM |     |     |     |
| -------------------- | ------------------------- | --- | ------------------------ | --- | ---------------------- | ---------------------- | ---------------------- | ------------------------ | ----------------------- | --- | --- | --- |
| )deunitnoc(  2 elbaT |                           |     |                          |     |  ararreF dna atnuguduK |  imimatlA dna itayablA |  imimatlA dna itayablA |  .la te zerreituG-nitraM |                         |     |     |     |
 scávoK dna sereyneK  lawihsiR dna ramuK )1202( .la te marhseM )6102( .la te oyratneO )1202( .la te ahtimarP
|     |     |     | )9102( .la te delahK |               | )1202( .la te itednoK |     |     | )7102( .la te neetaM | )9102( .la te azzaM |                      | )9102( niQ dna gniP |     |
| --- | --- | --- | -------------------- | ------------- | --------------------- | --- | --- | -------------------- | ------------------- | -------------------- | ------------------- | --- |
|     |     |     | )0202( .la te lilahK |               |                       |     |     |                      |                     | )2202( .la te irajaN |                     |     |
|     |     |     |                      | )9102( htuanK |                       |     |     |                      | )0202( otniP        | )1202( nayaraN       |                     |     |
secnerefeR
|     |     | )2202( |     |     |     | )8102( )0202( | )0202( )9102( | )1202( |     |     |     | )9102( |
| --- | --- | ------ | --- | --- | --- | ------------- | ------------- | ------ | --- | --- | --- | ------ |
1 3

Social Network Analysis and Mining (2023) 13:20  Page 27 of 40  20
|     | )%67.19( ycarucca sessalc-4 |     |     |  ycarucca-sisylana tnemitneS |                           |     |     |     |     |                             |
| --- | --------------------------- | --- | --- | ---------------------------- | ------------------------- | --- | --- | --- | --- | --------------------------- |
|     |                             |     |     |                              | -maps fo )%38.0( erocs 1F |     |     |     |     | -acfiissalc etarucca %54.89 |
 ycarucca-noitceted mapS
)%94000.99( ycaruccA
)%5.99( etar noitceteD
|     |                |                  | )99.0 >( ycaruccA |                                  |             | )%5.19( ycaruccA |                 |                |                 | )%45.99( ycaruccA                             |
| --- | -------------- | ---------------- | ----------------- | -------------------------------- | ----------- | ---------------- | --------------- | -------------- | --------------- | --------------------------------------------- |
|     |                | )109.0( ycaruccA | )489.0( ycaruccA  | )5.78( ycaruccA )639.0( ycaruccA |             |                  | )99.0( ycaruccA |                |                 |                                               |
|     |                |                  |                   |                                  |             |                  |                 | serocs 1F tseB | )%38( noisicerP | )%66( erocs-1F )698.0( erocs-F )%99( erocs-1F |
|     | tluser tsehgiH |                  |                   |                                  | )129.0( CUA |                  |                 |                |                 |                                               |
)%47.89( )%18.37(
srem
noit
mhtirogla gnimrofrep-tseB
FR ,RL ,BN ,gnirtsulC
|     |     |     |     |     | reniMPT-gniggaB | yaB evïaN + MVS |     |     |     |     |
| --- | --- | --- | --- | --- | --------------- | --------------- | --- | --- | --- | --- |
WoB + TD
|     |     | toBzeewT TOB-YPS |     |          |     |      |     |     |     | tsooBGX tsooBadA |
| --- | --- | ---------------- | --- | -------- | --- | ---- | --- | --- | --- | ---------------- |
|     |     |                  |     |          |     |      |     |     |     | BG ,FR gniggaB   |
|     |     |                  |     | LME MTSL |     |      |     |     |     |                  |
|     |     |                  |     |          |     | piRJ | CSE |     | PLM |                  |
|     | FR  |                  | NB  |          | FR  |      |     |     |     | FR               |
–
|     |  ,sgat aidem ,tnemegagne |     |     | roivaheb ,tnetnoc egasseM |     |     |  ,laropmet ,skrowten noit |     |  ,ycneuqerf gnikil ,palrevo                       |     |
| --- | ------------------------ | --- | --- | ------------------------- | --- | --- | ------------------------- | --- | ------------------------------------------------- | --- |
|     |                          |     |     |                           |     |     | -nem/teewter ,atadateM    |     |  tenretni ,tceffe krowteN -resu ,serutaef gathsah |     |
 ,ofni aidem ,atadateM -tnetnoc ,desab-elfiorP hparg ,laroivaheb ,txeT  ,noitamrofni tnetnoc  ,resu tnetnoc ,gathsaH atadatem teewT ,resU
 ,retsop laitneuflni  ,lacirogetac ,lautxeT
|     |     | ytiralimis aidem |     |     |     |     |     |     |     | tnetnoc ,laroivaheB |
| --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | ------------------- |
tnetnoc ,roivaheB
|     |                |     |     |     |               | tnetnoc ,elfiorP |     |     |     | serutaef desab |
| --- | -------------- | --- | --- | --- | ------------- | ---------------- | --- | --- | --- | -------------- |
|     | epyt s’erutaeF |     |     |     | desab tnetnoC |                  |     |     |     |                |
tnemitnes laciremun
|     |     | laroivaheB |         | tnemitneS |         |     |     |        |     |         |
| --- | --- | ---------- | ------- | --------- | ------- | --- | --- | ------ | --- | ------- |
|     |     |            | tnuoccA |           |         |     |     | niamod |     |         |
|     |     | elfiorP    | desab   |           | tnetnoC |     |     |        |     | tnetnoC |
resU
 recneuflni margatsnI yrotisoper retemotoB
snoitcelE 0202 SU
7102ardneliahS 9102tnawhseY
|     |            |        |        | 1202ihtuM .P 8102nilgnoH |            |           |     |         |            | 7102peednaS |
| --- | ---------- | ------ | ------ | ------------------------ | ---------- | --------- | --- | ------- | ---------- | ----------- |
|     | 0202otsirK |        |        |                          | 7102icserC | 0202aymoS |     |         |            | 9102abeehS  |
|     |            |        |        |                          |            |           |     | 41mapSH | 8102aridnI | 1202dieaS   |
|     |            | 1202dM |        |                          |            | tesatad   |     |         |            |             |
|     | tesataD    | elggaK | elggaK | elggaK                   | elggaK     |           |     |         |            |             |
SMS
mapS laicoS
epyt toB
libyS laicoS laicoS laicoS mapS mapS mapS mapS mapS mapS libyS laicoS maps laicoS laicoS mapS libyS laicoS libyS
mroftalP margatsnI koobecaF koobecaF koobecaF margatsnI margatsnI koobecaF
rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT rettiwT
obieW
|     |     |     |     | LD & LM desivrepuS |     |     |     |                 |     | LD & LM desivrepuS |
| --- | --- | --- | --- | ------------------ | --- | --- | --- | --------------- | --- | ------------------ |
|     |     |     |     | desivrepus-imeS    |     |     |     | desivrepus-imeS |     |                    |
LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS LM desivrepuS
euqinhceT
)1202( .la te haiagnilamaR )1202( .la te eerhS aynaraS )9102( eejrenaB dna hgniS
)0202( atpuG dna oohaS  .la te hednakirahidayyaS
| )deunitnoc(  2 elbaT |     |     |     | )2202( .la te seugirdoR |     |     |     | )8102( nuS dna iahdeS |     |     |
| -------------------- | --- | --- | --- | ----------------------- | --- | --- | --- | --------------------- | --- | --- |
)1202( .la te namhaR  .la te ziuR-zeugírdoR )2202( .la te vostvehS
|     |                     | )2202( .la te alkuhS | )8102( .la te erohtaR |                     |                 |     |     |     |                   | )0202( .la te ragneS )9102( .la te abeehS |
| --- | ------------------- | -------------------- | --------------------- | ------------------- | --------------- | --- | --- | --- | ----------------- | ----------------------------------------- |
|     | )0202( .la te abruP |                      |                       | )1202( .la te yddeR |                 |     |     |     |                   |                                           |
|     |                     |                      |                       | )8102( .la te neR   | )0202( inenidaS |     |     |     | )8102( .la te neS |                                           |
)0202( ihkiehS
secnerefeR
|     |     |     |     |     | )0202( |     | )0202( |     |     |     |
| --- | --- | --- | --- | --- | ------ | --- | ------ | --- | --- | --- |
1 3

 20  Page 28 of 40 Social Network Analysis and Mining (2023) 13:20
 ta )57.0( llacer ,)59.0( CUA
)8505.0( ssol gniniarT
| )%3.69( ycaruccA )%57.94( erocs 1F | )%72.69( ycaruccA |                                | )%76.09( ycaruccA |
| ---------------------------------- | ----------------- | ------------------------------ | ----------------- |
| )%79( ycaruccA                     |                   | noisicerp %59 )989.0( ycaruccA |                   |
|                                    |                   | ycarucca hgiH                  | )489.0( erocs-F   |
tluser tsehgiH
|     | )59.0( CUA |     | )%99( PRT |
| --- | ---------- | --- | --------- |
noitnetta-fles + MTSL-iB + TREBLA
mhtirogla gnimrofrep-tseB
MVS + )ED ,xedni BD(
dohteM desahp-owT
 URGiB + teNseR
toBPT MLE
NN
| FR FR | FR FR                      | FR                          |                             |
| ----- | -------------------------- | --------------------------- | --------------------------- |
|       | krowten ,tnetnoc ,atadateM | txet morf serutaef citnameS | elfiorp ,atadatem ,citnameS |
 ,snoitcaretni ,atadateM
 resu ,tnetnoc egasseM
elfiorp resu ,tnetnoC
| atadatem tnuoccA |     | gnimit ,stnetnoc | tnetnoc ,roivaheB |
| ---------------- | --- | ---------------- | ----------------- |
epyt s’erutaeF ciremun ,txeT
lacitsitatS roivaheb
atadateM
elfiorP
–
-obiew dna UCPgolborciM
|     |     | knaThsihP ,latoTsuriV )detcelloc-fles( ataD |     |
| --- | --- | ------------------------------------------- | --- |
7102dammahoM
5102nahgnaiX
7102nahuohZ
| 9102sajehT | 7102niaxuW | K 02-DLWS | K 02-DLWS |
| ---------- | ---------- | --------- | --------- |
| 8102eétsE  | 7102runO   |           | 5102uhniZ |
5102oaC
tesataD
epyt toB
| mapS libyS libyS            | laicoS mapS | laicoS libyS mapS mapS | laicoS laicoS mapS mapS |
| --------------------------- | ----------- | ---------------------- | ----------------------- |
| mroftalP koobecaF margatsnI | margatsnI   | koobecaF nIdekniL      |                         |
| rettiwT                     | rettiwT     |                        | rettiwT                 |
|                             |             | obieW obieW            | obieW obieW obieW       |
-repusnU & desivrepuS
LM desivrepusnU
| LM desivrepuS LM desivrepuS | LM desivrepuS LM desivrepuS | LM desivrepuS | LM desivrepuS LM desivrepuS |
| --------------------------- | --------------------------- | ------------- | --------------------------- |
LM desiv
euqinhceT
|     |     | LD LD LD | LD  |
| --- | --- | -------- | --- |
)8102( imiraK dna ibarhoS
)deunitnoc(  2 elbaT  ffolE dna tlaW red nav
|                      | )7102( nuS dna gnahZ |                                     | )b ,a7102( .la te nehC                     |
| -------------------- | -------------------- | ----------------------------------- | ------------------------------------------ |
| )9102( .la te sajehT |                      | )0202( .la te adnaW                 |  .la te ,gnaW ,gnehZ  .la te ,gnahZ ,gnehZ |
|                      | )7102( .la te loraV  |                                     | )2202( .la te gnaY                         |
|                      |                      | )5102( .la te oaiX )1202( .la te uW |                                            |
)1202( .la te uX
| secnerefeR |     |     | )a6102( )b6102( |
| ---------- | --- | --- | --------------- |
)8102(
1 3

Social Network Analysis and Mining (2023) 13:20  Page 29 of 40  20
Table 3  Summary of Public Datasets Information
| Platform Datasets | Papers that used it | No. of papers | Bot type |
| ----------------- | ------------------- | ------------- | -------- |
Twitter Cresci2017 Andriotis and Takasu (2019), Echeverrï£¡a et al.  13 Spam, social
(2018), Fonseca Abreu et al. (2020), Hayawi
et al. (2022), Heidari et al. (2020), Heidari et al.
(2021), Knauth (2019), Sengar et al. (2020),
Kudugunta and Ferrara (2018), Najari et al.
(2022), Ping and Qin (2019), Rodríguez-Ruiz
et al. (2020)
Cresci2015 Bindu et al. (2022), Echeverrï£¡a et al. (2018),  5 Sybil, social
Fernquist et al. (2018), Gao et al. (2020), Khaled
et al. (2019), Prabhu Kavin et al. (2022)
Kaggle Alothali, Alashwal, et al. (2021a), Alothali, Hayawi  10 Spam, sybil, social
et al. (2021b), Shukla et al. (2021), Knauth
(2019), Pramitha et al. (2021), Shukla et al.
(2022), Ramalingaiah et al. (2021), Rodrigues
et al. (2022), Rodríguez-Ruiz et al. (2020), Sad-
ineni (2020)
Honeypot Alom et al. (2020), Cai, Li, and Zeng (2017a),  4 Spam
Inuwa-Dutse et al. (2018), Koggalahewa et al.
(2022)
The fake project Koggalahewa et al. (2022), Prabhu Kavin et al.  2 Spam
(2022)
HSpam14 Koggalahewa et al. (2022), Sedhai and Sun (2018) 2 Spam
Chao2011, Chao2012 Andriotis and Takasu (2019), Eshraqi et al. (2016),  3 Spam
Fazil and Abulaish (2018)
| NSCLab | Chen et al. (2017a, b) | 1   | Spam |
| ------ | ---------------------- | --- | ---- |
O. Varol2017 Wu et al. (2020), Fernquist et al. (2018), Hayawi  3 Social
et al. (2022)
Z. Gilani2017 Echeverrï£¡a et al. (2018), Fernquist et al. (2018),  3 Social
Hayawi et al. (2022)
Onur2017 Andriotis and Takasu (2019), Varol et al. (2017) 2 Spam, social
| 1KS-10KN               | Alom et al. (2020)        | 1   | Spam |
| ---------------------- | ------------------------- | --- | ---- |
| Sheeba2019             | Sheeba et al. (2019)      | 1   | Spam |
| SPDautomate, SPDmanual | Inuwa-Dutse et al. (2018) | 1   | Spam |
PAN 2019 bots and gender profiling task Attia et al. (2022), Kenyeres and Kovács (2022) 2 Social
Yang2019/2020b/2012 Echeverrï£¡a et al. (2018), Hayawi et al. (2022) 2 Social
GuofeiGu2017 Fazil and Abulaish (2018) Mateen et al. (2017) 2 Spam
| US (2020 elections | Shevtsov et al. (2022) | 1   | Social |
| ------------------ | ---------------------- | --- | ------ |
| Littman2018        | Cable and Hugh (2019)  | 1   | Social |
| Roeder2018         | Cable and Hugh (2019)  | 1   | Social |
Botometer repository Barhate et al. (2020), Khalil et al. (2020), Sayyadi- 3 Social
harikandeh et al. (2020)
Subrahmanian2016 Daouadi et al. (2019), Hayawi et al. (2022) 2 Social
Echeverria2017, Besel2018, Chavoshi2016 Hayawi et al. (2022) 1 Social
| Lee2011      | Daouadi et al. (2019) | 1   | Social |
| ------------ | --------------------- | --- | ------ |
| Mohammad2019 | Khalil et al. (2020)  | 1   | Social |
| Clark2016    | Wu et al. (2020)      | 1   | Social |
Mazza2019 Echeverrï£¡a et al. (2018), Hayawi et al. (2022) 2 Spam, social
| Clayton2016     | Davis et al. (2016)             | 1   | Social |
| --------------- | ------------------------------- | --- | ------ |
| BotsDeTwitter   | David et al. (2017)             | 1   | Spam   |
| Begenilmi2017   | Beğenilmiş and Uskudarli (2018) | 1   | Social |
| Abdulrahman2016 | Alarifi et al. (2016)           | 1   | Sybil  |
| Morstatter2016  | Cai, Li, and Zengi (2017b)      |     | Social |
1 3

 20  Page 30 of 40 Social Network Analysis and Mining (2023) 13:20
Table 3  (continued)
| Platform Datasets | Papers that used it             | No. of papers | Bot type    |
| ----------------- | ------------------------------- | ------------- | ----------- |
| Instagram Kaggle  | Kesharwani et al. 2021)         | 1             | Sybil       |
| Free4ever1        | Dey et al. (2019)               | 1             | Sybil       |
| Fatih2019         | Akyon and Esat Kalfaoglu (2019) | 1             | Spam, sybil |
Instagram influencer dataset Saranya Shree et al. (2021) 1 Sybil
Facebook VirusTotal and PhishTank Wanda et al. (2020) 1 Social
| Weibo MicroblogPCU        | Xu et al. (2021)     | 1   | Spam   |
| ------------------------- | -------------------- | --- | ------ |
| Sina Weibo data warehouse | Dan and Jieqi (2017) | 1   | Social |
SWLD-20 K Wu et al. (2021), Yang et al. (2022) 2 Spam, social
| Kaggle | Bhattacharya et al. (2021) | 1   | Sybil |
| ------ | -------------------------- | --- | ----- |
Table 4  Self-collected (private) Datasets and their Collection Methods
| Platform Papers |     | Data collection method | No. of papers |
| --------------- | --- | ---------------------- | ------------- |
Twitter Alarifi et al. (2016), van der Walt and Eloff (2018) Twitter4j 2
| Reddy et al. (2021) |     | Tweepy | 1   |
| ------------------- | --- | ------ | --- |
Alhassun and Rassam (2022), Alothali, Alashwal, et al. (2021a), Al-Qurishi et al.  Twitter API 27
(2018), Al-Zoubi et al. (2017), Anwar and Yaqub (2020), Wu et al. (2020),
Barhate et al. (2020), Beğenilmiş and Uskudarli (2018), Bindu et al. (2022),
Chen et al. (2017a, b), Cable and Hugh (2019), Daouadi et al. (2019), David et al.
(2017), Echeverrï£¡a et al. (2018), Fazil and Abulaish (2018), Fonseca Abreu et al.
(2020), Güngör et al. (2020), Kantepe and Gañiz (2017), Martin-Gutierrez et al.
(2021), Narayan (2021), Oentaryo et al. (2016), Shukla et al. (2022), Rodrigues
et al. (2022), Shevtsov et al. (2022), Pramitha et al. (2021), Varol et al. (2017),
Chen et al. (2017a, b)
Cresci et al. (2016), Shukla et al. (2021), Khaled et al. (2019), Pratama and  Manually 4
Rakhmawati (2019)
| Ersahin et al. (2017)      |     | Machine learning           | 1   |
| -------------------------- | --- | -------------------------- | --- |
| Cai, Li, and Zengi (2017b) |     | Honeypots                  | 2   |
| Mazza et al. (2019)        |     | Twitter premium search API | 1   |
| Alharthali et al. (2019)   |     | Twitter API                | 1   |
| Prabhu Kavin et al. (2022) |     | REST API                   | 1   |
Instagram Meshram et al. (2021), Sheikhi (2020) Instagram API 2
Akyon and Esat Kalfaoglu (2019), Bazm and Asadpour (2020), Sen et al. (2018) Manually 3
| Munoz and Paul Guillen Pinto (2020) |     | Python | 1   |
| ----------------------------------- | --- | ------ | --- |
Munoz and Paul Guillen Pinto (2020), Thejas et al. (2019) Selenium web driver tool 2
| Purba et al. (2020)          |     | 3rd-party Instagram websites | 1   |
| ---------------------------- | --- | ---------------------------- | --- |
| Facebook Wanda et al. (2020) |     | VirusTotal, PhishTank        | 1   |
Babu et al. 2021), Dewan and Kumaraguru (2017), Gupta and Kaushal (2017),  Facebook graph API 6
Rathore et al. (2018), Singh and Banerjee (2019), Sohrabi and Karimi (2018)
| Hakimi et al. (2019) |     | Mockaroo | 1   |
| -------------------- | --- | -------- | --- |
Albayati and Altamimi (2020), Rathore et al. (2018) CRAWLER 2
Weibo Bhattacharya et al. (2021), Ren et al. (2018), Wu et al. (2021), Yang et al. (2022),  Web crawler and data scraping 5
Zheng, Wang, et al. (2016a)
| Huang et al. (2016) |     | Manually | 1   |
| ------------------- | --- | -------- | --- |
LinkedIn Adikari and Dutta (2020), Xiao et al. (2015) Manually 2
1 3

Social Network Analysis and Mining (2023) 13:20 Page 31 of 40 20
1 3
LM gnisu noitceteD toB aideM
laicoS
ni
serutaeF
fo
yrammuS
5
elbaT
noitpircseD
mroftalP
srepap
fo
.oN
ti desu taht srepaP
epyt
s’erutaeF
-moc
seuc
citsiugnil
no
desab
era
serutaef
tnetnoC
obieW
,rettiwT
,margatsnI
,koobecaF
44
.la te fiiralA ,)9102( ulgoaflaK tasE dna noykA
egaugnal/tnetnoC
gniggat
hceeps-fo-trap
ylniam
,PLN
hguorht
detup
ihsiruQ-lA ,)2202( massaR dna nussahlA ,)6102( aittA ,)9102( usakaT dna sitoirdnA ,)8102( .la
te
ayrahcattahB ,)0202( .la te uW ,)2202( .la
te
,iL ,iaC ,)a7102( gneZ dna ,iL ,iaC ,)1202( .la
te
sivaD ,)7102( .la te divaD ,)b7102( igneZ dna ,)7102( urugaramuK dna naweD ,)6102( .la
te
,)6102( .la te iqarhsE ,)8102( .la te a¡£ïrrevehcE ,)0202( .la te oaG ,)8102( hsialubA dna lizaF ,)9102( .la te imikaH ,)0202( .la te rögnüG ,)9102( htuanK ,)2202( scávoK dna sereyneK lawihsiR dna ramuK ,)2202( .la te awehalaggoK .la te marhseM ,)7102( .la te neetaM ,)0202( .la te nivaK uhbarP ,)9102( niQ dna gniP ,)1202( ,)1202( .la te yddeR ,)8102( .la te erohtaR ,)2202( ,)0202( .la te ziuR-zeugírdoR ,)8102( .la te neR ,)0202( atpuG dna oohaS ,)0202( inenidaS .la te abeehS ,)0202( .la te hednakirahidayyaS ,)8102( .la te tsiuqnreF ,)0202( ihkiehS ,)9102( ,)2202( .la te vostvehS ,)8102( nuS dna iahdeS uW ,)7102( nuS dna gnahZ ,)7102( .la te loraV ,gnehZ ,)a6102( .la te ,gnaW ,gnehZ ,)1202( .la
te
)b 6102( .la te ,gnahZ
tnuocca
resu
fo
seitreporp
no
desab
era
serutaef
resU
obieW
,nIdekniL
,rettiwT
,margatsnI
,koobecaF
24
,)9102( .la te ihtrahlA ,)0202( attuD dna irakidA
)elfiorp(
resU
spihsnoitaler
sresu
dna
.la te ihsiruQ-lA ,)2202( massaR dna nussahlA .la te ubaB ,)7102( .la te ibuoZ-lA ,)8102( dna şimlineğeB ,)0202( .la te etahraB ,)1202 dna elbaC ,)2202( .la te udniB ,)8102( ilraduksU .la te divaD ,)9102( .la te idauoaD ,)9102( hguH .la te a¡£ïrrevehcE ,)9102( .la te yeD ,)7102( uerbA acesnoF ,)7102( .la te nihasrE ,)8102( dna atpuG ,)0202( .la te rögnüG ,)0202( .la
te
gnauH ,)0202( .la te iradieH ,)7102( lahsuaK epetnaK ,)8102( .la te estuD-awunI ,)6102( .la
te
,)1202 .la te inawrahseK ,)7102( ziñaG dna htuanK ,)0202( .la te lilahK ,)9102( .la te delahK itayablA ,)0202( imimatlA dna itayablA ,)9102( ,)7102( .la te neetaM ,)9102( imimatlA dna ,)2202( .la te nivaK uhbarP ,)1202( nayaraN ,)1202( .la te namhaR ,)2202( .la te alkuhS ,)8102( .la te erohtaR ,)1202( .la te haiagnilamaR ,)8102( nuS dna iahdeS ,)0202( atpuG dna oohaS gnahZ ,)0202( .la te ragneS ,)8102( .la te neS .la te gnaY ,)0202( .la te adnaW ,)7102( nuS dna )2202(

 20  Page 32 of 40 Social Network Analysis and Mining (2023) 13:20
 no tliub era yehT .serutaef krowten yb derutpac era
 eht gnidrager noitamrofni si serutaef atad atem resU -reporp lacitsitats yb detaluclac era serutaef roivaheB  emit eht rof scitsitats ,steewt evitucesnoc ,steewter -areneg tnetnoc fo snrettap gnimit erutpac laropmeT -retni dna etar teewt sa hcus ,noitpmusnoc dna noit  laicos eht gnilledom yb detcartxe era serutaef hparG
|  noitamrofni na gnitacoL .scitsiretcarahc s'elfiorp |     |     |     |  snrettap noisuffid noitamrofni fo stcepsa tnereffiD |     |     |
| --------------------------------------------------- | --- | --- | --- | ---------------------------------------------------- | --- | --- |
 tnemitnes dliub ot desu era smhtirogla sisylana
|                                              |     |     |     |  era skrowten lla ,ycneuqerf eht fo sisab eht nO  tnemitnes cfiiceps rettiwT dna esoprup-lareneG |  sa hcus emit fo scitsitats sedulcni serutaef emiT |     |
| -------------------------------------------- | --- | --- | --- | ------------------------------------------------------------------------------------------------ | -------------------------------------------------- | --- |
| evitceffe eb ot nwonk si atadatem aiv ecruos |     |     |     | cte secnerrucco gathsah ,snoitnem ,steewter                                                      |                                                    |     |
ledom hparg laicos a sa mroftalp aidem
DI tsop ,DI tnuocca :selpmaxE
noitubirtsid emit teewt
|     |     | atad eht morf seit |     |     | cte tsop neewteb |     |
| --- | --- | ------------------ | --- | --- | ---------------- | --- |
noitpircseD
dehgiew
serutaef
obieW ,rettiwT ,margatsnI ,koobecaF
| obieW ,rettiwT ,margatsnI |     |     |     | obieW ,rettiwT ,margatsnI | obieW ,rettiwT ,koobecaF |     |
| ------------------------- | --- | --- | --- | ------------------------- | ------------------------ | --- |
rettiwT ,margatsnI rettiwT ,koobecaF
obieW ,rettiwT
mroftalP
srepap fo .oN
| 72  |                                                                                                     | 61  |                                                    | 8 8 | 7   | 5 4                                                   |
| --- | --------------------------------------------------------------------------------------------------- | --- | -------------------------------------------------- | --- | --- | ----------------------------------------------------- |
|     |  dna amatarP ,)1202( .la te ahtimarP ,)0202( otniP -idayyaS ,)0202( .la te abruP ,)9102( itawamhkaR |     |  yddeR ,)a6102( .la te ,gnaW ,gnehZ ,)8102( .la te |     |     |  aynaraS ,)7102( .la te neetaM ,)6102( .la te iqarhsE |
 buqaY dna rawnA ,)9102( usakaT dna sitoirdnA  ,)9102( .la te idauoaD ,)0202( .la te uW ,)0202(  .la te iwayaH ,)1202( .la te alkuhS ,)8102( .la te  nelliuG luaP dna zonuM ,)1202( .la te marhseM )2202( .la te gnaY ,)1202( .la te uW ,)7102( .la te  ,)b7102( igneZ dna ,iL ,iaC ,)9102( .la te ihtrahlA  ,)0202( ruopdasA dna mzaB ,)a7102( gneZ dna  uW ,)6102( .la te iqarhsE ,)8102( .la te tsiuqnreF  eejrenaB dna hgniS ,)1202( .la te eerhS aynaraS
|     |  ,)1202( .la te zerreituG-nitraM ,)8102( ararreF |     |  neR ,)7102( iqeiJ dna naD ,)6102( .la te icserC |  ,)8102( .la te estuD-awunI ,)6102( .la te sivaD  sitoirdnA ,)2202( .la te seugirdoR ,)1202( .la te |  ,)0202( .la te hednakirahidayyaS ,)1202( .la te |     |
| --- | ------------------------------------------------ | --- | ------------------------------------------------ | --------------------------------------------------------------------------------------------------- | ------------------------------------------------ | --- |
 urugaramuK dna naweD ,)7102( .la te divaD  tsiuqnreF ,)8102( hsialubA dna lizaF ,)7102(  dna atnuguduK ,)1202( .la te itednoK ,)2202(  imiraK dna ibarhoS ,)0202( .la te hednakirah  loraV ,)8102( ffolE dna tlaW red nav ,)8102(  ,)1202( .la te namhaR ,)1202( .la te marhseM  .la te ,gnahZ ,gnehZ ,)9102( htuanK ,)0202(  ,iL ,iaC ,)1202( .la te eerhS aynaraS ,)b6102(  ,)7102( .la te loraV ,)8102( hsialubA dna lizaF  iradieH ,)2202( .la te gnaY ,)6102( .la te sivaD  .la te hednakirahidayyaS ,)9102( usakaT dna  ,)7102( lahsuaK dna atpuG ,)6102( .la te sivaD  ,)8102( .la te ihsiruQ-lA ,)1202( .la te eerhS
|  .la te ,lawhsalA ,ilahtolA ,)0202( .la te molA |     |  ihkiehS ,)9102( ulgoaflaK tasE dna noykA |     |  .la te hednakirahidayyaS ,)8102( .la te neS |     |     |
| ----------------------------------------------- | --- | ----------------------------------------- | --- | -------------------------------------------- | --- | --- |
 ,)b1202( .la te ,iwayaH ,ilahtolA ,)a1202( )0202( .la te uW ,)1202( .la te uW ,)0202( )0202( .la te uW ,)1202( .la te uX ,)0202(  ,)9102( .la te sajehT ,)6102( .la te oyratneO
)2202( massaR dna nussahlA
)9102( niQ dna gniP
ti desu taht srepaP
)1202( .la te
)9102(
seires/lautxet/lacirogetac/ciremuN
)noitcaretni/ytinummoc( krowteN
)deunitnoc(  5 elbaT
laropmet/gnimiT
epyt s’erutaeF
laruoivaheB
tnemitneS
atadateM
hparG
1 3

Social Network Analysis and Mining (2023) 13:20  Page 33 of 40  20
 owt neewteb palrevo edulcni serutaef palrevo tseretnI
|  ,ecnairav dna naeM ,selitrauq ,xam ,nim :selpmaxE      |  ’srewollof ,sdrowyek lanoitomorp ,egatnecrep gat  ,yrogetac egap ,htgnel retemarap ,redneg :selpmaxE                                                                                            |  pihsnoitaler tcerid a evah yhpargoib ni ”ythguan“ |     |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------- | --- |
|  laicos s’tnuocca na ot evitaler scitsitats evitpircseD | -rep egami-non ,htgnel noitpac egareva :selpmaxE  noitacol ,).mmoc/ekil( etar tnemegagne ,egatnec  ni sdrow fo .on ,htgnel eman ,sniamodbus fo .on  ,SPTTH/PTTH sah ,egap no sekil ,elacol ,eman |                                                    |     |
 ,htgnel emanresu tnuoc nehpyh ,emanresu sah
 ,detcetorp si ,noitacol ,eman neercs :selpmaxE
serutaef dneirf resu ni dedulcni era stcatnoc
 dna ”tahc“ sdrow eht fo ecneserp :selpmaxE
| cte yportne dna ,stnemom ,naidem |     | cte htgnel htap ,tnuoc sretemarap |     |
| -------------------------------- | --- | --------------------------------- | --- |
ytinffia lacipot sa hcus sresu
lavretni tsop ,sdrowyek
egami elfiorp
| noitpircseD       |                    |         | maps htiw          |
| ----------------- | ------------------ | ------- | ------------------ |
| rettiwT ,nIdekniL |                    |         | rettiwT ,margatsnI |
| mroftalP          | margatsnI koobecaF |         |                    |
| rettiwT           |                    | rettiwT | rettiwT            |
srepap fo .oN
| 3 2 | 1 1 | 1   | 2 1 |
| --- | --- | --- | --- |
 .la te nehC ,)5102( .la te oaiX ,)6102( .la te sivaD
)8102( .la te neS ,)8102( nuS dna iahdeS
)0202( .la te uW ,)6102( .la te sivaD
)7102( urugaramuK dna naweD
)7102( ziñaG dna epetnaK
)6102( .la te iqarhsE
| ti desu taht srepaP | )0202( .la te abruP |     |     |
| ------------------- | ------------------- | --- | --- |
)b ,a7102(
serutaef gathsah ,palrevo tenretnI
| )deunitnoc(  5 elbaT | tnemegagne dna aideM |     |     |
| -------------------- | -------------------- | --- | --- |
knil dna ytitnE
epyt s’erutaeF
sdneirf resU
| lacitsitatS |     | sdrowyeK |     |
| ----------- | --- | -------- | --- |
cidoireP
1 3

20 Page 34 of 40 Social Network Analysis and Mining (2023) 13:20
Table 6 ML Algorithms in Reviewed Papers
Algorithm Papers that applied it No. of papers Highest classifier Performance
bot type detected measure
(accuracy)
(%)
RF Alarifi et al. (2016), Alothali, Alashwal, et al. (2021a), Alothali, 44 Social 99.545
Hayawi, et al. (2021b), Andriotis and Takasu (2019), Barhate et al.
(2020), Bazm and Asadpour (2020), Beğenilmiş and Uskudarli
(2018), Bhattacharya et al. (2021), Bindu et al. (2022), Chen
et al. (2017a, b), Dan and Jieqi (2017), David et al. (2017), Davis
et al. (2016), Dewan and Kumaraguru (2017), Dey et al. (2019),
Echeverrï£¡a et al. (2018), Fazil and Abulaish (2018), Fonseca Abreu
et al. (2020), Gupta and Kaushal (2017), Shukla et al. (2021), Heidari
et al. (2020), Heidari et al. (2021), Knauth (2019), Kondeti et al.
(2021), Meshram et al. (2021), Munoz and Paul Guillen Pinto (2020),
Narayan (2021), Oentaryo et al. (2016), Pratama and Rakhmawati
(2019), Purba et al. (2020), Shukla et al. (2022), Rathore et al. (2018),
Rodrigues et al. (2022), Sadineni (2020), Sedhai and Sun (2018),
Sen et al. (2018), Sengar et al. (2020), Sheeba et al. (2019), Singh
and Banerjee (2019), Thejas et al. (2019), Varol et al. (2017), van der
Walt and Eloff (2018), Zhang and Sun (2017), Xiao et al. (2015)
SVM Adikari and Dutta (2020), Akyon and Esat Kalfaoglu (2019), Andrio- 35 Sybil 98
tis and Takasu (2019), Bazm and Asadpour (2020), Beğenilmiş and
Uskudarli (2018), Bindu et al. (2022), David et al. (2017), Fernquist
et al. (2018), Fonseca Abreu et al. (2020), Gupta and Kaushal (2017),
Hakimi et al. (2019), Heidari et al. (2021), Khaled et al. (2019),
Kantepe and Gañiz (2017), Knauth (2019), Kumar and Rishiwal
(2020), Albayati and Altamimi (2019), Meshram et al. (2021), Munoz
and Paul Guillen Pinto (2020), Oentaryo et al. (2016), Prabhu Kavin
et al. (2022), Shukla et al. (2022), Rahman et al. (2021), Rathore
et al. (2018), Ren et al. (2018), Rodrigues et al. (2022), Rodríguez-
Ruiz et al. (2020), Sadineni (2020), Saranya Shree et al. (2021), Sen
et al. (2018), Sheikhi (2020), Sohrabi and Karimi (2018), Thejas et al.
(2019), Xiao et al. (2015), Zheng, Wang, et al. (2016a)
NB Akyon and Esat Kalfaoglu (2019), Andriotis and Takasu (2019), Babu 24 Sybil 90.4
et al. 2021), Bhattacharya et al. (2021), David et al. (2017), Ersahin
et al. (2017), Fernquist et al. (2018), Fonseca Abreu et al. (2020),
Güngör et al. (2020), Gupta and Kaushal (2017), Huang et al. (2016),
Albayati and Altamimi (2019), Mateen et al. (2017), Munoz and Paul
Guillen Pinto (2020), Oentaryo et al. (2016), Ren et al. (2018), Rod-
rigues et al. (2022), Rodríguez-Ruiz et al. (2020), Saranya Shree et al.
(2021), Sedhai and Sun (2018), Sheikhi (2020), Purba et al. (2020),
Thejas et al. (2019), Zheng, Wang, et al. (2016a)
ANN Adikari and Dutta (2020), Akyon and Esat Kalfaoglu (2019), Alarifi 17 Sybil, Spam 94
et al. (2016), Alom et al. (2020), Al-Qurishi et al. (2018), Hakimi
et al. (2019), Heidari et al. (2020), Heidari et al. (2021), Kesharwani
et al. 2021), Khaled et al. (2019), Meshram et al. (2021), Munoz and
Paul Guillen Pinto (2020), Shukla et al. (2022), Sen et al. (2018),
Thejas et al. (2019), Yang et al. (2022)
DT Bazm and Asadpour (2020), David et al. (2017), Echeverrï£¡a et al. 13 Social 99
(2018), Fazil and Abulaish (2018), Albayati and Altamimi (2019),
Munoz and Paul Guillen Pinto (2020), Narayan (2021), Shukla et al.
(2022), Ramalingaiah et al. (2021), Rodrigues et al. (2022), Sengar
et al. (2020), Varol et al. (2017), Zheng, Wang, et al. (2016a)
AdaBoost Andriotis and Takasu (2019), Bazm and Asadpour (2020), Echeverrï£¡a 13 Social 98.8
et al. (2018), Fernquist et al. (2018), Heidari et al. (2020), Kenyeres
and Kovács (2022), Knauth (2019), Munoz and Paul Guillen Pinto
(2020), Sahoo and Gupta (2020), Sen et al. (2018), Sengar et al.
(2020), Singh and Banerjee (2019), Varol et al. (2017)
1 3

Social Network Analysis and Mining (2023) 13:20 Page 35 of 40 20
Table 6 (continued)
Algorithm Papers that applied it No. of papers Highest classifier Performance
bot type detected measure
(accuracy)
(%)
KNN Al-Zoubi et al. (2017), Andriotis and Takasu (2019), Bazm and 11 Sybil 98
Asadpour (2020), Fonseca Abreu et al. (2020), Gupta and Kaushal
(2017), Hakimi et al. (2019), Kondeti et al. (2021), Albayati and
Altamimi (2019), Rathore et al. (2018), Sengar et al. (2020), Thejas
et al. (2019)
J48 (DT) Al-Zoubi et al. (2017), Güngör et al. (2020), Gupta and Kaushal 9 Spam 97.6
(2017), Mateen et al. (2017), Rathore et al. (2018), Ren et al. (2018),
Sahoo and Gupta (2020), Sheikhi (2020), Purba et al. (2020)
MLP Al-Zoubi et al. (2017), Knauth (2019), Munoz and Paul Guillen Pinto 7 Social 83
(2020), Purba et al. (2020), Sen et al. (2018), Sengar et al. (2020),
Sheikhi (2020)
CNN Alhassun and Rassam (2022), Alom et al. (2020), Attia et al. (2022), 9 Spam 99.68
Cai, Li, and Zeng (2017a), Cai, Li, and Zengi (2017b), Gao et al.
(2020), Martin-Gutierrez et al. (2021), Ping and Qin (2019), Wu et al.
(2021)
Gradient boost Bhattacharya et al. (2021), Echeverrï£¡a et al. (2018), Inuwa-Dutse 6 Social 99.54
et al. (2018), Kantepe and Gañiz (2017), Sengar et al. (2020), Singh
and Banerjee (2019)
LSTM (RNN) Cai, Li, and Zeng (2017a), Cai, Li, and Zengi (2017b), Hayawi et al. 8 Sybil 99.31
(2022), Kenyeres and Kovács (2022), Mazza et al. (2019), Kudugunta
and Ferrara (2018), Ping and Qin (2019), Wanda et al. (2020)
BN Al-Zoubi et al. (2017), Fazil and Abulaish (2018), Gupta and Kaushal 5 Spam 98.4
(2017), Rathore et al. (2018), Zheng, Wang, et al. (2016a)
MNB Kantepe and Gañiz (2017), Rodrigues et al. (2022), Kumar and Rishi- 5 Spam 99
wal (2020), Narayan (2021), Sengar et al. (2020)
XGBoost Pramitha et al. (2021), Sen et al. (2018), Shevtsov et al. (2022), Singh 4 Social 89.6
and Banerjee (2019)
JRip (DT) Gupta and Kaushal (2017), Rathore et al. (2018), Sahoo and Gupta 3 Spam 99.5
(2020)
Bi-LSTM (RNN) Heidari et al. (2020), Xu et al. (2021) 2 Spam 98.1
BiGRU (RNN) Wu et al. (2021), Yang et al. (2022) 2 Social 98.87
ID3 (DT) Albayati and Altamimi (2020) 1 Sybil 97.7
GNB Kantepe and Gañiz (2017) 1 Social 86
ELM Zheng, Zhang, et al. (2016b) 1 Spam 99
bi-SN-LSTM Gao et al. (2020) 1 Spam F1(99.31)
DenStream Eshraqi et al. (2016) 1 Spam 99
K-means Koggalahewa et al. (2022) 1 Spam 96.9
DBSCAN Mazza et al. (2019) 1 Social 97.7
Author contributions Conceptualization, MA, RZ, AS, FA, AS, DA; Open Access This article is licensed under a Creative Commons Attri-
Methodology, MA, RZ, AS, FA, AS, DA; Formal Analysis, MA, RZ, bution 4.0 International License, which permits use, sharing, adapta-
AS, FA, AS, DA; Writing-Reviewing, MA, RZ, AS, FA, AS, DA; tion, distribution and reproduction in any medium or format, as long
Project Administration, MA. All authors have read and agreed to the as you give appropriate credit to the original author(s) and the source,
published version of the manuscript. provide a link to the Creative Commons licence, and indicate if changes
were made. The images or other third party material in this article are
Funding We would like to thank SAUDI ARAMCO Cybersecurity included in the article's Creative Commons licence, unless indicated
Chair at Imam Abdulrahman Bin Faisal University (IAU) for support- otherwise in a credit line to the material. If material is not included in
ing and funding this research work. the article's Creative Commons licence and your intended use is not
permitted by statutory regulation or exceeds the permitted use, you will
Declarations need to obtain permission directly from the copyright holder. To view a
copy of this licence, visit http://c reati vecom mons.o rg/l icens es/b y/4.0 /.
Conflict of interest The authors declare that there is no conflict of in-
terest.
1 3

20 Page 36 of 40 Social Network Analysis and Mining (2023) 13:20
References conference, CSNet 2021a. https:// doi.o rg/1 0.1 109/ CSNet
52717.2 021.9 61428 2
Alothali E, Hayawi K, Alashwal H (2021b) Hybrid feature selection
Adikari S, Dutta K (2020) Identifying fake profiles in LinkedIn
approach to identify optimal features of profile metadata to
Akyon FC, Esat Kalfaoglu M (2019) Instagram fake and automated
detect social bots in Twitter. Soc Netw Anal Mining. https://
account detection. In: Proceedings—2019 innovations in intel-
doi.o rg/1 0.1 007/s 13278-0 21-0 0786-4
ligent systems and applications conference, ASYU 2019. https://
Alothali E, Zaki N, Mohamed EA, Alashwal H (2019) Detecting
doi.o rg/1 0.1 109/A SYU48 272.2 019.8 94643 7
social bots on Twitter: a literature review. In: Proceedings of
Alarifi A, Alsaleh M, Al-Salman AM (2016) Twitter turing test: iden-
the 2018 13th international conference on innovations in infor-
tifying social machines. Inf Sci. https://d oi.o rg/1 0.1 016/j.i ns.
mation technology, IIT 2018. https://d oi.o rg/1 0.1 109/I NNOV
2016.0 8.0 36
ATIONS.2 018.8 60599 5
Albayati MB, Altamimi AM (2019) An empirical study for detecting
Al-Qurishi M, Alrubaian M, Rahman SMM, Alamri A, Hassan MM
fake Facebook profiles using supervised mining techniques. Inf
(2018) A prediction system of Sybil attack in social network
Slovenia. https://d oi.o rg/1 0.3 1449/i nf.v 43i1.2 319
using deep-regression model. Future Gener Comput Syst.
Albayati M, Altamimi A (2020) MDFP: a machine learning model for
https://d oi.o rg/1 0.1 016/j.f uture.2 017.0 8.0 30
detecting fake Facebook profiles using supervised and unsuper-
Al-Zoubi AM, Alqatawna J, Faris H (2017) Spam profile detection in
vised mining techniques. Int J Simul Syst Sci Technol. https://
social networks based on public features. In: 2017 8th interna-
doi.o rg/1 0.5 013/i jssst.a .2 0.0 1.1 1
tional conference on information and communication systems,
Aldayel A, Magdy W (2022) Characterizing the role of bots’ in polar-
ICICS 2017. https://d oi.o rg/1 0.1 109/I ACS.2 017.7 92195 9
ized stance on social media. Soc Netw Anal Mining. https://d oi.
Andriotis P, Takasu A (2019) Emotional bots: content-based spam-
org/1 0.1 007/s 13278-0 22-0 0858-z
mer detection on social media. In: 10th IEEE international
Alharthi R, Alhothali A, Moria K (2019) Detecting and character-
workshop on information forensics and security, WIFS 2018.
izing Arab spammers campaigns in Twitter. Proc Comput Sci
https://d oi.o rg/1 0.1 109/W IFS.2 018.8 63076 0
163:248–256. https://d oi.o rg/1 0.1 016/j.p rocs.2 019.1 2.1 06
Anwar A, Yaqub U (2020) Bot detection in twitter landscape using
Alhassun AS, Rassam MA (2022) A combined text-based and meta-
unsupervised learning. ACM Int Conf Proc Series. https://d oi.
data-based deep-learning framework for the detection of spam
org/1 0.1 145/3 39695 6.3 40180 1
accounts on the social media platform Twitter. Processes. https://
Attia SM, Mattar AM, Badran KM (2022) Bot detection using multi-
doi.o rg/1 0.3 390/p r1003 0439
input deep neural network model in social media. In: 2022 13th
Ali A, Syed A (2022) Cyberbullying detection using machine learn-
international conference on electrical engineering (ICEENG),
ing. Pak J Eng Technol 3(2):45–50. https://d oi.o rg/1 0.5 1846/
p 71–75. https://d oi.o rg/1 0.1 109/I CEENG 49683.2 022.9 78186 3
vol3is s2pp4 5-5 0
Barhate S, Mangla R, Panjwani D, Gatkal S, Kazi F (2020) Twit-
Aljabri M, Aljameel SS, Mohammad RMA, Almotiri SH, Mirza S,
ter bot detection and their influence in hashtag manipulation.
Anis FM, Aboulnour M, Alomari DM, Alhamed DH, Altamimi
In: 2020 IEEE 17th India council international conference,
HS (2021a) Intelligent techniques for detecting network attacks:
INDICON 2020. https://d oi.o rg/1 0.1 109/I NDIC O N4987 3.
review and research directions. In Sens. https://d oi. org/1 0.3 390/
2020.9 34215 2
s21217 070
Bazm, M. and Asadpour, M. (2020) “Behavioral Modeling of Per-
Aljabri M, Chrouf SM, Alzahrani NA, Alghamdi L, Alfehaid R,
sian Instagram Users to detect Bots.” Available at: https://doi.
Alqarawi R, Alhuthayfi J, Alduhailan N (2021b) Sentiment anal-
org/10.48550/arXiv.2008.03951
ysis of Arabic tweets regarding distance learning in Saudi Arabia
Beğenilmiş E, Uskudarli S (2018) Organized behavior classifica-
during the covid-19 pandemic. Sensors 21(16):5431. https://d oi.
tion of tweet sets using supervised learning methods. ACM
org/1 0.3 390/s 21165 431
Int Conf Proc Series. https://d oi.o rg/1 0.1 145/3 22760 9.3 22766 5
Aljabri M, Altamimi HS, Albelali SA, Al-Harbi M, Alhuraib HT, Alo-
Benkler Y et al (2017) Partisanship, propaganda, and disinformation:
taibi NK, Alahmadi AA, Alhaidari F, Mohammad RM, Salah K
online media and the 2016 U.S. presidential election, search
(2022a) Detecting malicious URLs using machine learning tech-
issue lab. Issue lab. Available at: https://s earch.i ssuel ab.o rg/
niques: review and research directions. IEEE Access 10:121395–
resour ce/p artis anshi p-p ropag anda-a nd-d isinf ormat ion-o nline-
121417. https://d oi.o rg/1 0.1 109/a ccess.2 022.3 22230 7
media-a nd-t he-2 016-u-s -p resid entia l-e lecti on.h tml. Accessed
Aljabri M, Alhaidari F, Mohammad RM, Mirza S, Alhamed DH,
9 Oct 2022
Altamimi HS, Chrouf SM (2022b) An assessment of lexical,
Bhattacharya A, Bathla R, Rana A, Arora G (2021) Application of
network, and content-based features for detecting malicious urls
machine learning techniques in detecting fake profiles on social
using machine learning and deep learning models. Comput Intell
media. In: 2021 9th international conference on reliability, Info-
Neurosci 2022:1–14. https://d oi.o rg/1 0.1 155/2 022/3 24121 6
com technologies and optimization (trends and future direc-
Aljabri M, Alahmadi AA, Mohammad RM, Aboulnour M, Alo-
tions), ICRITO 2021. https://d oi.o rg/1 0.1 109/I CRITO 51393.
mari DM, Almotiri SH (2022c) Classification of firewall log
2021.9 59637 3
data using multiclass machine learning models. Electronics
Bindu K et al (2022) Detection of fake accounts in Twitter using data
11(12):1851. https://d oi.o rg/1 0.3 390/e lectr onics 11121 851
science. Int Res J Mod Eng Technol Sci 4(5), pp. 3552-3556.
Aljabri M, Mirza S (2022) Phishing attacks detection using machine
Cable, J. and Hugh, G. (2019) Bots in the Net: Applying Machine
learning and Deep Learning Models. In: 2022 7th interna-
Learning to Identify Social Media Trolls. rep. Available at: http://
tional conference on data science and machine learning appli-
cs229.stanford.edu/proj2019spr/report/74.pdf
cations (CDMA). https://d oi.o rg/1 0.1 109/c dma54 072.2 022.
Caers R, de Feyter T, de Couck M, Stough T, Vigna C, du Bois C
00034
(2013) Facebook: a literature review. New Media Soc. https://
Alom Z, Carminati B, Ferrari E (2020) A deep learning model for
doi.o rg/1 0.1 177/1 46144 48134 88061
Twitter spam detection. Online Soc Netw Media. https://d oi.
Cai C, Li L, Zeng D (2017a) Detecting social bots by jointly mode-
org/1 0.1 016/j.o snem.2 020.1 00079
ling deep behavior and content information. Int Conf Inf Knowl
Alothali E, Alashwal H, Salih M, Hayawi K (2021a) Real time
Manag Proc Part F131841. https:// doi.o rg/ 10.1 145/ 313284 7.
detection of social bots on Twitter using machine learning and
313305 0
Apache Kafka. In: 2021a 5th cyber security in networking
1 3

Social Network Analysis and Mining (2023) 13:20 Page 37 of 40 20
Cai C, Li L, Zengi D (2017b) Behavior enhanced deep bot detection Ersahin B, Aktas O, Kilinc D, Akyol C (2017) Twitter fake account
in social media. In: 2017b IEEE international conference on detection. Int Conf Comput Sci Eng (UBMK) 2017:388–392.
intelligence and security informatics: security and big data, ISI https://d oi.o rg/1 0.1 109/U BMK.2 017.8 09342 0
2017b. https://d oi.o rg/1 0.1 109/I SI.2 017.8 00488 7 Eshraqi N, Jalali M, Moattar MH (2016) Detecting spam tweets
Cao F, Ester M, Qian W, Zhou A (2006) Density-based clustering in Twitter using a data stream clustering algorithm. In: 2nd
over an evolving data stream with noise. In: Proceedings of international congress on technology, communication and
the sixth SIAM international conference on data mining, 2006. knowledge, ICTCK 2015. https://d oi.o rg/1 0.1 109/I CTCK.
https://d oi.o rg/1 0.1 137/1.9 78161 19727 64.2 9 2015.7 58269 4
Carminati B, Ferrari E, Heatherly R, Kantarcioglu M, Thuraisingham Ezarfelix J, Jeffrey N, Sari N (2022) Systematic literature review:
B (2011) Semantic web-based social network access control. Instagram fake account detection based on machine learning.
Comput Secur 30(2–3):108–115. https://d oi.o rg/1 0.1 016/j. Eng Math Comput Sci J. https://d oi.o rg/1 0.2 1512/e macsj ourn
cose.2 010.0 8.0 03 al.v 4i1.8 076
Chen C, Wang Y, Zhang J, Xiang Y, Zhou W, Min G (2017a) Statisti- Fazil M, Abulaish M (2018) A hybrid approach for detecting automated
cal features-based real-time detection of drifted Twitter spam. spammers in Twitter. IEEE Trans Inf Forensics Secur. https://d oi.
IEEE Trans Inf Forensics Secur. https://d oi. org/1 0.1 109/T IFS. org/1 0.1 109/T IFS.2 018.2 82595 8
2016.2 62188 8 Fernquist J, Kaati L, Schroeder R (2018) Political bots and the Swed-
Chen Z, Tanash RS, Stoll R, Subramanian D (2017b) Hunting mali- ish general election. In: 2018 IEEE international conference on
cious bots on twitter: an unsupervised approach. In: Lecture intelligence and security informatics, ISI 2018. https://d oi.o rg/
notes in computer science (including subseries lecture notes 10.1 109/I SI.2 018.8 58734 7
in artificial intelligence and lecture notes in bioinformatics), Ferrara, E. (2018). Measuring Social Spam and the Effect of Bots on
10540 LNCS. https://d oi.o rg/1 0.1 007/9 78-3-3 19-6 7256-4_4 0 Information Diffusion in Social Media. Computational Social Sci-
Cresci S, di Pietro R, Petrocchi M, Spognardi A, Tesconi M (2015) ences, 229-255. https://doi.org/10.1007/978-3-319-77332-2_13
Fame for sale: efficient detection of fake Twitter followers. Ferrara, E. (2020). What types of COVID-19 conspiracies are
Decis Support Syst. https://d oi.o rg/1 0.1 016/j.d ss.2 015.0 9.0 03 populated by Twitter bots?. First Monday, 25(6). https://doi.
Cresci S, di Pietro R, Petrocchi M, Spognardi A, Tesconi M (2016) org/10.5210/fm.v25i6.10633
DNA-inspired online behavioral modeling and its application Fonseca Abreu JV, Ghedini Ralha C, Costa Gondim JJ (2020) Twitter
to spambot detection. IEEE Intell Syst. https://d oi.o rg/1 0.1 109/ bot detection with reduced feature set. In: Proceedings—2020
MIS.2 016.2 9 IEEE international conference on intelligence and security infor-
Cresci S, Spognardi A, Petrocchi M, Tesconi M, di Pietro R (2017) matics, ISI 2020. https://d oi.o rg/1 0.1 109/I SI498 25.2 020.9 2805
The paradigm-shift of social spambots: evidence, theories, and 25
tools for the arms race. In: 26th international world wide web Gannarapu S, Dawoud A, Ali RS, Alwan A (2020) Bot detection using
conference 2017, WWW 2017 companion. https://d oi.o rg/1 0. machine learning algorithms on social media platforms. In: CITI-
1145/3 04102 1.3 05513 5 SIA 2020—IEEE conference on innovative technologies in intel-
Dan J, Jieqi T (2017) Study of bot detection on Sina-Weibo based on ligent systems and industrial applications, proceedings. https://
machine learning. In: 14th international conference on services doi.o rg/1 0.1 109/C ITISI A5069 0.2 020.9 37177 8
systems and services management, ICSSSM 2017—Proceed- Gao T, Yang J, Peng W, Jiang L, Sun Y, Li F (2020) A content-based
ings. https://d oi.o rg/1 0.1 109/I CSSSM.2 017.7 99629 2 method for Sybil detection in online social networks via deep
Daouadi KE, Rebaï RZ, Amous I (2019) Bot detection on online learning. IEEE Access. https://d oi.o rg/1 0.1 109/A CCESS.2 020.
social networks using deep forest. Adv Intell Syst Comput. 297587 7
https://d oi.o rg/1 0.1 007/9 78-3-0 30-1 9810-7_3 0 Gheewala S, Patel R (2018) Machine learning based twitter spam
David I, Siordia OS, Moctezuma D (2017) Features combination for account detection: a review. In: Proceedings of the 2nd inter-
the detection of malicious Twitter accounts. In: 2016 IEEE national conference on computing methodologies and commu-
international autumn meeting on power, electronics and com- nication, ICCMC 2018. https://d oi.o rg/1 0.1 109/I CCMC.2 018.
puting, ROPEC 2016. https://d oi.o rg/1 0.1 109/R OPEC.2 016. 848799 2
783062 6 Gilani Z, Wang L, Crowcroft J, Almeida M, Farahbakhsh R (2016)
Davis, C. A., Varol, O., Ferrara, E., Flammini, A., & Menczer, F. Stweeler: a framework for Twitter bot analysis. In: WWW 2016
(2016). BotOrNot. Proceedings of the 25th International Con- companion—proceedings of the 25th international conference
ference Companion on World Wide Web - WWW . https://doi. on World Wide Web. https://d oi.o rg/1 0.1 145/2 87251 8.2 88936 0
org/10.1145/2872518.2889302 Gilani Z, Farahbakhsh R, Tyson G, Wang L, Crowcroft J (2017) Of
Derhab A, Alawwad R, Dehwah K, Tariq N, Khan FA, Al-Muhtadi J bots and humans (on Twitter). In: Proceedings of the 2017 IEEE/
(2021) Tweet-based bot detection using big data analytics. IEEE ACM international conference on advances in social networks
Access. https://d oi.o rg/1 0.1 109/A CCESS.2 021.3 07495 3 analysis and mining 2017, p 349–354. https://d oi.o rg/1 0.1 145/
Dewan P, Kumaraguru P (2017) Facebook Inspector (FbI): towards 311002 5.3 11009 0
automatic real-time detection of malicious content on Face- Gorwa R, Guilbeault D (2020) Unpacking the social media bot: a typol-
book. Soc Netw Anal Mining. https://d oi.o rg/1 0.1 007/ ogy to guide research and policy. Policy Internet 12(2):225–248.
s13278-0 17-0 434-5 https://d oi.o rg/1 0.1 002/p oi3.1 84
Dey A, Reddy H, Dey M, Sinha N (2019) Detection of fake accounts in Güngör KN, Ayhan Erdem O, Doğru İA (2020) Tweet and account
Instagram using machine learning. Int J Comput Sci Inf Technol. based spam detection on Twitter, p 898–905. https://d oi.o rg/1 0.
https://d oi.o rg/1 0.5 121/i jcsit.2 019.1 1507 1007/9 78-3-0 30-3 6178-5_7 9
Dinath W (2021) Linkedin: a link to the knowledge economy. In: Pro- Guofei Gu (no date) Welcome to Guofei Gu's Homepage. Available
ceedings of the European conference on knowledge management, at: https://p eople.e ngr.t amu.e du/g uofei/i ndex.h tml. Accessed 12
ECKM. https://d oi.o rg/1 0.3 4190/E KM.2 1.1 78 Oct 2022
Echeverrï£¡a J, de Cristofaro E, Kourtellis N, Leontiadis I, Stringhini Gupta A, Kaushal R (2017) Towards detecting fake user accounts in
G, Zhou S (2018) LOBO. In: Proceedings of the 34th annual facebook. In: ISEA Asia security and privacy conference 2017,
computer security applications conference, p 137–146. https:// ISEASP 2017. https://d oi.o rg/1 0.1 109/I SEASP.2 017.7 97699 6
doi.o rg/1 0.1 145/3 27469 4.3 27473 8
1 3

20 Page 38 of 40 Social Network Analysis and Mining (2023) 13:20
Hakimi AN, Ramli S, Wook M, Mohd Zainudin N, Hasbullah NA, 2021-May. https://d oi.o rg/1 0.2 3919/F RUCT5 2173.2 021.9 4354
Abdul Wahab N, Mat Razali NA (2019) Identifying fake account 21
in facebook using machine learning. In: Lecture notes in com- Kondeti P, Yerramreddy LP, Pradhan A, Swain G (2021) Fake account
puter science (including subseries lecture notes in artificial detection using machine learning, p 791–802. https://d oi.o rg/1 0.
intelligence and lecture notes in bioinformatics), 11870 LNCS. 1007/9 78-9 81-1 5-5 258-8_7 3
https://d oi.o rg/1 0.1 007/9 78-3-0 30-3 4032-2_3 9 Kudugunta S, Ferrara E (2018) Deep neural networks for bot detection.
Hayawi K, Mathew S, Venugopal N, Masud MM, Ho PH (2022) DeeP- Inf Sci. https://d oi.o rg/1 0.1 016/j.i ns.2 018.0 8.0 19
roBot: a hybrid deep neural network model for social bot detec- Kumar G, Rishiwal V (2020) Machine learning for prediction of mali-
tion based on user profile data. Soc Netw Anal Mining. https:// cious or SPAM users on social networks. Int J Sci Technol Res,
doi.o rg/1 0.1 007/s 13278-0 22-0 0869-w 9(2), pp. 926-932
Heidari M, Jones JH, Uzuner O (2020) Deep contextualized word Lee K, Eoff BD, Caverlee J (2006) Seven months with the devils: a
embedding for text-based online user profiling to detect social long-term study of content polluters on Twitter. Icwsm 2011
bots on Twitter. In: IEEE international conference on data mining Mahesh, B. (2020) “Machine Learning Algorithms - A Review,”
workshops, ICDMW, 2020-November. https:// doi. org/ 10. 1109/ International Journal of Science and Research (IJSR), 9(1), pp.
ICDMW5 1313.2 020.0 0071 381–386. Available at: https://d oi.o rg/1 0.2 1275/A RT202 03995.
Heidari M, Jones JHJ, Uzuner O (2021) An empirical study of machine Martin-Gutierrez D, Hernandez-Penaloza G, Hernandez AB, Lozano-
learning algorithms for social media bot detection. In: 2021 IEEE Diez A, Alvarez F (2021) A deep learning approach for robust
international IOT, electronics and mechatronics conference, detection of bots in Twitter using transformers. IEEE Access.
IEMTRONICS 2021—Proceedings. https:// doi. org/ 10. 1109/ https://d oi.o rg/1 0.1 109/A CCESS.2 021.3 06865 9
IEMTRO NICS5 2119.2 021.9 42260 5 Mateen M, Iqbal MA, Aleem M, Islam MA (2017) A hybrid approach
Huang, Y., Zhang, M., Yang, Y., Gan, S., & Zhang, Y. (2016) The for spam detection for Twitter. In: Proceedings of 2017 14th
Weibo Spammers’ Identification and Detection based on international bhurban conference on applied sciences and tech-
Bayesian-algorithm. Proceedings of the 2016 2nd Workshop on nology, IBCAST 2017. https:// doi. org/ 10. 1109/ IBCAST. 2017.
Advanced Research and Technology in Industry Applications. 786809 5
https://doi.org/10.2991/wartia-16.2016.271 Mazza M, Cresci S, Avvenuti M, Quattrociocchi W, Tesconi M (2019)
Inuwa-Dutse I, Liptrott M, Korkontzelos I (2018) Detection of spam- RTbust: exploiting temporal patterns for botnet detection on twit-
posting accounts on Twitter. Neurocomputing. https://d oi.o rg/1 0. ter. In: WebSci 2019—proceedings of the 11th ACM conference
1016/j.n eucom.2 018.0 7.0 44 on web science. https://d oi.o rg/1 0.1 145/3 29252 2.3 32601 5
Kantartopoulos P, Pitropakis N, Mylonas A, Kylilis N (2020) Explor- Meshram EP, Bhambulkar R, Pokale P, Kharbikar K, Awachat A
ing adversarial attacks and defences for fake Twitter account (2021) Automatic detection of fake profile using machine learn-
detection. Technologies. https://d oi.o rg/1 0.3 390/t echno logi ing on Instagram. Int J Sci Res Sci Technol. https://d oi.o rg/1 0.
es8040 064 32628/i jsrst 21833 0
Kantepe M, Gañiz MC (2017) Preprocessing framework for Twitter Morstatter F, Wu L, Nazer TH, Carley KM, Liu H (2016) A new
bot detection. In: 2nd international conference on computer approach to bot detection: striking the balance between preci-
science and engineering, UBMK 2017. https://d oi.o rg/1 0.1 109/ sion and recall. In: 2016 IEEE/ACM international conference on
UBMK.2 017.8 09348 3 advances in social networks analysis and mining (ASONAM),
Kaplan AM, Haenlein M (2010) Users of the world, unite! The chal- p 533–540. https://d oi.o rg/1 0.1 109/A SONAM.2 016.7 75228 7
lenges and opportunities of social media. Bus Horiz. https:// Munoz SD, Paul Guillen Pinto E (2020) A dataset for the detection
doi.o rg/1 0.1 016/j.b ushor.2 009.0 9.0 03 of fake profiles on social networking services. In: Proceed-
Kenyeres A, Kovács G (2022) “Conference: XVIII. Conference on ings—2020 international conference on computational science
hungarian computational linguistics.” Available at: https:// and computational intelligence, CSCI 2020. https:// doi. org/ 10.
www.r esear chgat e.n et/p ublic ation/3 58801 180_T witte r_b ot_ 1109/C SCI51 800.2 020.0 0046
detect ion_u sing_d eep_l earni ng Najari S, Salehi M, Farahbakhsh R (2022) GANBOT: a GAN-based
Kesharwani M, Kumari S, Niranjan V (2021) “Detecting fake social framework for social bot detection. Soc Netw Anal Mining.
media account using deep neural networking. Int Res J Eng https://d oi.o rg/1 0.1 007/s 13278-0 21-0 0800-9
Technol (IRJET), 8(7), pp. 1191-1197. Narayan N (2021) Twitter bot detection using machine learning algo-
Khaled S, El-Tazi N, Mokhtar HMO (2019) Detecting fake accounts rithms. In: 2021 4th international conference on electrical, com-
on social media. In: Proceedings—2018 IEEE international puter and communication technologies, ICECCT 2021. https://
conference on big data, big data 2018. https://d oi.o rg/1 0.1 109/ doi.o rg/1 0.1 109/I CECCT 52121.2 021.9 61684 1
BigDat a.2 018.8 62191 3 Naveen Babu M, Anusha G, Shivani A, Kalyani C, Meenakumari J
Khalil H, Khan MUS, Ali M (2020) Feature selection for unsuper- (2021) Fake profile identification using machine learning. Int J
vised bot detection. In: 2020 3rd international conference on Recent Adv Multidiscip Topics 2(6):273–275
computing, mathematics and engineering technologies: idea Oentaryo RJ, Murdopo A, Prasetyo PK, Lim EP (2016) On profil-
to innovation for building the knowledge economy, ICoMET ing bots in social media. In: Lecture notes in computer science
2020. https://d oi.o rg/1 0.1 109/i CoMET 48670.2 020.9 07413 1 (including subseries lecture notes in artificial intelligence and
Knauth J (2019) Language-agnostic twitter bot detection. In: Inter- lecture notes in bioinformatics), p 10046 LNCS. https://d oi.o rg/
national conference recent advances in natural language pro- 10.1 007/9 78-3-3 19-4 7880-7_6
cessing, RANLP, 2019-September. https://d oi.o rg/1 0.2 6615/ Orabi M, Mouheb D, al Aghbari Z, Kamel I (2020) Detection of bots
978-9 54-4 52-0 56-4_0 65 in social media: a systematic review. Inf Process Manag. https://
Koggalahewa D, Xu Y, Foo E (2022) An unsupervised method doi.o rg/1 0.1 016/j.i pm.2 020.1 02250
for social network spammer detection based on user infor- Pierri F, Artoni A, Ceri S (2020) Investigating Italian disinformation
mation interests. J Big Data. https://d oi.o rg/1 0.1 186/ spreading on Twitter in the context of 2019 European elections.
s40537-0 21-0 0552-5 PLoS ONE. https://d oi.o rg/1 0.1 371/j ourna l.p one.0 22782 1
Kolomeets M, Chechulin A (2021) Analysis of the malicious bots Ping H, Qin S (2019) A social bots detection model based on deep
market. In: Conference of open innovation association, FRUCT, learning algorithm. In: Int Conf Commun Technol Proc, ICCT,
2019-October. https://d oi.o rg/1 0.1 109/I CCT.2 018.8 60002 9
1 3

Social Network Analysis and Mining (2023) 13:20 Page 39 of 40 20
Prabhu Kavin B, Karki S, Hemalatha S, Singh D, Vijayalakshmi R, Saranya Shree S, Subhiksha C, Subhashini R (2021) Prediction of fake
Thangamani M, Haleem SLA, Jose D, Tirth V, Kshirsagar PR, Instagram profiles using machine learning. SSRN Electron J.
Adigo AG (2022) Machine learning-based secure data acquisi- https://d oi.o rg/1 0.2 139/s srn.3 80258 4
tion for fake accounts detection in future mobile communication Sayyadiharikandeh M, Varol O, Yang KC, Flammini A, Menczer F
networks. Wirel Commun Mob Comput. https://d oi.o rg/1 0.1 155/ (2020) Detection of novel social bots by ensembles of specialized
2022/6 35615 2 classifiers. Int Conf Inf Knowl Manag Proc. https:// doi. org/ 10.
Pramitha FN, Hadiprakoso RB, Qomariasih N, Girinoto (2021) Twit- 1145/3 34053 1.3 41269 8
ter bot account detection using supervised machine learning. In: Sedhai S, Sun A (2015) Hspam14: a collection of 14 million tweets for
2021 4th international seminar on research of information tech- hashtag-oriented spam research. In: SIGIR 2015—proceedings
nology and intelligent systems, ISRITI 2021. https://d oi.o rg/1 0. of the 38th international ACM SIGIR conference on research
1109/I SRITI 54043.2 021.9 70278 9 and development in information retrieval. https://d oi.o rg/1 0.
Pratama PG, Rakhmawati NA (2019) Social bot detection on 2019 1145/2 76646 2.2 76770 1
Indonesia president candidate’s supporter’s tweets. Proc Comput Sedhai S, Sun A (2018) Semi-supervised spam detection in Twitter
Sci. https://d oi.o rg/1 0.1 016/j.p rocs.2 019.1 1.1 87 stream. IEEE Trans Comput Soc Syst 5(1):169–175. https://d oi.
Purba KR, Asirvatham D, Murugesan RK (2020) Classification of ins- org/1 0.1 109/t css.2 017.2 77358 1
tagram fake users using supervised machine learning algorithms. Sen I, Singh S, Aggarwal A, Kumaraguru P, Mian S, Datta A (2018)
Int J Electr Comput Eng. https://d oi.o rg/1 0.1 1591/i jece.v 10i3. Worth its weight in likes: towards detecting fake likes on insta-
pp2763-2 772 gram. In: WebSci 2018—proceedings of the 10th ACM confer-
Rahman MA, Zaman N, Asyhari AT, Sadat SMN, Pillai P, Arshah RA ence on web science. https://d oi.o rg/1 0.1 145/3 20106 4.3 20110 5
(2021) SPY-BOT: machine learning-enabled post filtering for Sengar SS, Kumar S, Raina P (2020) Bot detection in social networks
social network-integrated industrial internet of things. Ad Hoc based on multilayered deep learning approach. Sens Transducers
Netw. https://d oi.o rg/1 0.1 016/j.a dhoc.2 021.1 02588 244(5):37–43
Ramalingaiah A, Hussaini S, Chaudhari S (2021) Twitter bot detec- Shao C, Ciampaglia GL, Varol O, Yang K, Flammini A, Menczer F
tion using supervised machine learning. J Phys Conf Series (2017) The spread of low-credibility content by social bots. Nat
1950(1):012006. https://d oi.o rg/1 0.1 088/1 742-6 596/1 950/1/ Commun. https://d oi.o rg/1 0.1 038/s 41467-0 18-0 6930-7
012006 Shearer E, Mitchell A (2022) News use across social media platforms
Rangel F, Rosso P (2019) Overview of the 7th author profiling task at in 2020, Pew Research Center's Journalism Project. Available at:
Pan 2019: Bots and gender profiling in twitter. In: CEUR work- https://w ww.j ourna lism.o rg/2 021/0 1/1 2/n ews-u se-a cross-s ocial-
shop proceedings, p 2380 media-p latfo rms-i n-2 020. Accessed 9 Oct 2022
Rao S, Verma AK, Bhatia T (2021) A review on social spam detection: Sheeba JI, Pradeep Devaneyan S (2019) Detection of spambot using
challenges, open issues, and future directions. Exp Syst Appl. random forest algorithm. SSRN Electron J. https://d oi.o rg/1 0.
https://d oi.o rg/1 0.1 016/j.e swa.2 021.1 15742 2139/s srn.3 46296 8
Rathore S, Loia V, Park JH (2018) SpamSpotter: an efficient spam- Sheehan BT (2018) Customer service chatbots: anthropomorphism
mer detection framework based on intelligent decision support adoption and word of mouth. Griffith University, University of
system on Facebook. Appl Soft Comput J. https://d oi.o rg/1 0. Queensland, Queensland
1016/j.a soc.2 017.0 9.0 32 Sheikhi S (2020) An efficient method for detection of fake accounts
Reddy PM, Venkatesh K, Bhargav D, Sandhya M (2021) Spam on the instagram platform. Revue Intell Artif. https://d oi.o rg/1 0.
detection and fake user identification methodologies in social 18280/r ia.3 40407
networks using extreme machine learning. SSRN Electron J. Shevtsov A, Tzagkarakis C, Antonakaki D, Ioannidis S (2022) Explain-
https://d oi.o rg/1 0.2 139/s srn.3 92009 1 able machine learning pipeline for Twitter bot detection during
Ren H, Zhang Z, Xia C (2018) Online social spammer detection the 2020 US Presidential Elections. Softw Impacts 13:100333.
based on semi-supervised learning. ACM Int Conf Proc Series. https://d oi.o rg/1 0.1 016/j.s impa.2 022.1 00333
https://d oi.o rg/1 0.1 145/3 30242 5.3 30242 9 Shukla R, Sinha A, Chaudhary A (2022) TweezBot: an AI-driven
Rodrigues AP, Fernandes R, Shetty A, Lakshmanna K, Shafi RM online media bot identification algorithm for Twitter social net-
(2022) Real-time Twitter spam detection and sentiment analy- works. Electron (switzerland). https://d oi.o rg/1 0.3 390/e lectr onic
sis using machine learning and deep learning techniques. Com- s11050 743
put Intell Neurosci 2022:1–14. https:// doi. org/ 10. 1155/ 2022/ Shukla H, Jagtap N, Patil B (2021) Enhanced Twitter bot detection
521194 9 using ensemble machine learning. In: Proceedings of the 6th
Rodríguez-Ruiz J, Mata-Sánchez JI, Monroy R, Loyola-González O, international conference on inventive computation technologies,
López-Cuevas A (2020) A one-class classification approach ICICT 2021. https://d oi.o rg/1 0.1 109/I CICT5 0816.2 021.9 35873 4
for bot detection on Twitter. Comput Secur. https:// doi. org/1 0. Siddiqui A (2019) Facebook 2019 Q1 earnings: The social media giant
1016/j.c ose.2 020.1 01715 boasts 2.7 billion monthly active users on its all services, Digi-
Sadineni PK (2020) Machine learning classifiers for efficient spam- tal Information World. Available at: https://w ww.d igita linfo rmat
mers detection in Twitter OSN. SSRN Electron J. https://d oi. ionwor ld.c om/2 019/0 4/f acebo ok-q 1-2 019-r eport.h tml. Accessed
org/1 0.2 139/s srn.3 73417 0 9 Oct 2022
Sahoo SR, Gupta BB (2020) Popularity-based detection of mali- Singh Y, Banerjee S (2019) Fake (sybil) account detection using
cious content in facebook using machine learning approach. machine learning. SSRN Electron J. https://d oi.o rg/1 0. 2139/
Adv Intell Syst Comput. https://d oi.o rg/1 0.1 007/9 78-9 81-1 5- ssrn.3 46293 3
0029-9_1 3 Sohrabi MK, Karimi F (2018) A feature selection approach to detect
Santia GC, Mujib MI, Williams JR (2019) Detecting social bots on spam in the Facebook social network. Arab J Sci Eng. https://
facebook in an information veracity context. In: Proceedings doi.o rg/1 0.1 007/s 13369-0 17-2 855-x
of the 13th international conference on web and social media, Subrahmanian VS, Azaria A, Durst S, Kagan V, Galstyan A, Lerman K,
ICWSM 2019 Zhu L, Ferrara E, Flammini A, Menczer F (2016) The DARPA
1 3

20 Page 40 of 40 Social Network Analysis and Mining (2023) 13:20
Twitter bot challenge. Computer 49(6):38–46. https://d oi.o rg/1 0. Xiao C, Freeman DM, Hwa T (2015). Detecting clusters of fake
1109/M C.2 016.1 83 accounts in online social networks. In: AISec 2015—proceedings
Tenba Group (2022) What is Sina Weibo? Know your Chinese social of the 8th ACM workshop on artificial intelligence and security,
media!, Tenba Group. Available at: https://t enbag roup.c om/w hat- co-located with CCS 2015. https://d oi.o rg/1 0.1 145/2 80876 9.
is-s ina-w eibo-k now-y our-c hines e-s ocial-m edia. Accessed 9 Oct 280877 9
2022 Xu G, Zhou D, Liu J (2021) Social network spam detection based
Thakur S, Breslin JG (2021) Rumour prevention in social networks on ALBERT and combination of Bi-LSTM with self-attention.
with layer 2 blockchains. Soc Netw Anal Mining. https://d oi.o rg/ Secur Commun Netw. https://d oi.o rg/1 0.1 155/2 021/5 56799 1
10.1 007/s 13278-0 21-0 0819-y Yang C, Harkreader R, Gu G (2013) Empirical evaluation and new
Thejas GS, Soni J, Chandna K, Iyengar SS, Sunitha NR, Prabakar N design for fighting evolving twitter spammers. IEEE Trans Inf
(2019) Learning-based model to fight against fake like clicks on Forensics Secur. https://d oi.o rg/1 0.1 109/T IFS.2 013.2 26773 2
Instagram posts. In: Conference proceedings—IEEE SOUTH- Yang Z, Chen X, Wang H, Wang W, Miao Z, Jiang T (2022) A new
EASTCON, 2019-April. https:// doi. org/ 10. 1109/ South eastC joint approach with temporal and profile information for social
on4231 1.2 019.9 02053 3 bot detection. Secur Commun Netw 2022:1–14. https://d oi.o rg/
Thuraisingham B (2020) The role of artificial intelligence and cyber 10.1 155/2 022/9 11938 8
security for social media. In: Proceedings—2020 IEEE 34th Yang C, Harkreader R, Zhang J, Shin S, Gu G (2012) Analyzing
international parallel and distributed processing symposium spammers’social networks for fun and profit: A case study of
workshops, IPDPSW 2020. https://d oi.o rg/1 0.1 109/I PDPS cyber criminal ecosystem on Twitter. In: WWW’12—proceed-
W50202.2 020.0 0184 ings of the 21st annual conference on World Wide Web. https://
van der Walt E, Eloff J (2018) Using machine learning to detect fake doi.o rg/1 0.1 145/2 18783 6.2 18784 7
identities: bots vs humans. IEEE Access. https://d oi.o rg/1 0.1 109/ Zeng Z, Li T, Sun S, Sun J, Yin J (2021) A novel semi-supervised self-
ACCESS.2 018.2 79601 8 training method based on resampling for Twitter fake account
Varol O, Ferrara E, Davis CA, Menczer F, Flammini A (2017) Online identification. Data Technol Appl 56(3):409–428. https://d oi.o rg/
human-bot interactions: detection, estimation, and characteriza- 10.1 108/d ta-0 7-2 021-0 196
tion. In: Proceedings of the 11th international conference on web Zhang W, Sun HM (2017) Instagram spam detection. In: Proceedings
and social media, ICWSM 2017 of IEEE Pacific Rim international symposium on dependable
Wald R, Khoshgoftaar TM, Napolitano A, Sumner C (2013) Predict- computing, PRDC. https://d oi.o rg/1 0.1 109/P RDC.2 017.4 3
ing susceptibility to social bots on Twitter. In: Proceedings of Zhang Z, Gupta BB (2018) Social media security and trustworthiness:
the 2013 IEEE 14th international conference on information overview and new direction. Future Gener Comput Syst. https://
reuse and integration, IEEE IRI 2013. https://d oi.o rg/1 0.1 109/ doi.o rg/1 0.1 016/j.f uture.2 016.1 0.0 07
IRI.2 013.6 64244 7 Zheng X, Zhang X, Yu Y, Kechadi T, Rong C (2016b) ELM-
Wanda P, Hiswati ME, Jie HJ (2020) DeepOSN: bringing deep learning based spammer detection in social networks. J Supercomput
as malicious detection scheme in online social network. IAES 72(8):2991–3005. https://d oi.o rg/1 0.1 007/s 11227-0 15-1 437-5
Int J Artif Intell. https://d oi.o rg/1 0.1 1591/i jai.v 9.i 1.p p146-1 54 Zheng X, Wang J, Jie F, Li L (2016a) Two phase based spammer detec-
Wiederhold G, McCarthy J (1992) Arthur Samuel: Pioneer in machine tion in Weibo. In: Proceedings—15th IEEE international confer-
learning. IBM J Res Dev 36(3):329–331. https://d oi.o rg/1 0.1 147/ ence on data mining workshop, ICDMW 2015. https://d oi.o rg/
rd.3 63.0 329 10.1 109/I CDMW.2 015.2 2
Wu B, Liu L, Yang Y, Zheng K, Wang X (2020) Using improved con-
ditional generative adversarial networks to detect social bots on Publisher's Note Springer Nature remains neutral with regard to
Twitter. IEEE Access. https:// doi. org/ 10. 1109/ ACCESS. 2020. jurisdictional claims in published maps and institutional affiliations.
297563 0
Wu Y, Fang Y, Shang S, Jin J, Wei L, Wang H (2021) A novel frame-
work for detecting social bots with deep neural networks and
active learning. Knowl Based Syst. https://d oi.o rg/1 0.1 016/j.
knosys.2 020.1 06525
1 3